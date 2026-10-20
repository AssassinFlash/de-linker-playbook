# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "openpyxl>=3.1",
# ]
# ///
"""
询盘回流 L3：把网站上的形式发票申请对进底表「询盘」，再重算动作进度。

  uv run scripts/inquiry_pull.py run
                       按四个计入状态全量对账并写表
  uv run scripts/inquiry_pull.py run --dry-run
                       只取数、打印条数，不写表
  uv run scripts/inquiry_pull.py run --audit-order-attribution
                       不传 include_meta，只打印订单来源字段名和有没有，不写表、不打印字段值
  uv run scripts/inquiry_pull.py run --dry-run --audit-order-attribution
                       两样一起：打印字段名/存在性和对账条数，不写表

定时不另装。`uv run scripts/gsc_pull.py schedule install` 的那条 08:30 任务先跑 GSC，
再跑本脚本，然后发每日提醒。标签和钟点不变。

网站读取用标准库。文件头里的依赖是 scripts/base_table.py 已经在用的那一组，没有新包。
Woo 只读密钥不进仓库。config.toml（PLAYBOOK_CONFIG，否则
~/.config/de-linker-playbook/config.toml）只放指针：

  [woocommerce]
  consumer_key_file = "~/.config/de-linker-playbook/woo-consumer-key"
  consumer_secret_file = "~/.config/de-linker-playbook/woo-consumer-secret"

两个文件各一行，权限 600。日志只打条数、内部编号和字段名；出错也不打印响应正文。
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import stat
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True  # keep scripts/__pycache__ out of the repo
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402

ORDERS_URL = "https://de-linker.com/wp-json/wc/v3/orders"
STATUSES = "inquiry-received,proforma-issued,completed,cancelled"
ISSUED_META = "_linker_proforma_issued"
ATTR_PREFIX = "_wc_order_attribution_"
SHEET = "询盘"
PER_PAGE = 100
TIMEOUT = 60
RETRIES = 3
MAX_PAGES = 200
MAX_BODY = 16 * 1024 * 1024
PRESERVE = ("归因登记编号", "归因依据", "备注")
STATUS_ZH = {
    "inquiry-received": "询盘已收到",
    "proforma-issued": "形式发票已开",
    "completed": "已完成",
    "cancelled": "已取消",
}
RETRY_CODES = {429, 500, 502, 503, 504}
SAFE_KEY = re.compile(r"^[A-Za-z0-9_.:-]{1,80}$")
SAFE_SLUG = re.compile(r"^[a-z0-9-]{1,40}$")
TOKEN = re.compile(r"[\x21-\x7e]+")
UNIX_TEXT = re.compile(r"[0-9]{10,11}")
# getTimestamp() is seconds since the epoch. Keep a wide but finite window.
UNIX_MIN, UNIX_MAX = 946684800, 4102444800


class PullError(Exception):
    """Operator-safe failure. The message must not contain a response body."""


class Retryable(PullError):
    pass


class MappingError(Exception):
    """Safe row-mapping failure. The message must not contain field values."""


class _BadIssued:
    pass


BAD_ISSUED = _BadIssued()


def log(msg: str) -> None:
    print(f"[{bt.stamp(bt.beijing_now())}] 询盘：{msg}", flush=True)


def _same(a, b) -> bool:
    if a in (None, "") and b in (None, ""):
        return True
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < 1e-9
    return str(a) == str(b)


# ---------------------------------------------------------------- secrets


def config_path() -> Path:
    return Path(os.environ.get("PLAYBOOK_CONFIG", bt.CONFIG_DIR / "config.toml"))


def resolve_secret_path(raw: str, cfg: Path) -> Path:
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = cfg.parent / path
    return path


def check_secret_file(label: str, path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"{label} not found: {path}")
    st = path.lstat()
    if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode):
        raise SystemExit(f"{label} must be a regular file with mode 600")
    mode = stat.S_IMODE(st.st_mode)
    if mode != 0o600:
        raise SystemExit(f"{label} permissions {mode:03o}, expected 600")


def read_token(label: str, path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise SystemExit(f"{label} is not utf-8") from None
    token = text.strip()
    if not TOKEN.fullmatch(token):
        raise SystemExit(f"{label} must be one line")
    return token


def load_secrets(path: Path | None = None) -> tuple[str, str]:
    cfg_path = path or config_path()
    if not cfg_path.exists():
        raise SystemExit(f"missing config {cfg_path}")
    try:
        data = tomllib.loads(cfg_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError:
        raise SystemExit(f"config {cfg_path} is not valid toml") from None
    woo = data.get("woocommerce")
    if not isinstance(woo, dict):
        raise SystemExit(f"{cfg_path}: missing [woocommerce]")
    found: list[tuple[str, Path]] = []
    for label in ("consumer_key_file", "consumer_secret_file"):
        raw = woo.get(label)
        if not isinstance(raw, str) or not raw.strip():
            raise SystemExit(f"{cfg_path}: [woocommerce] {label} is empty")
        found.append((label, resolve_secret_path(raw.strip(), cfg_path)))
    for label, secret_path in found:
        check_secret_file(label, secret_path)
    key, secret = (read_token(label, secret_path) for label, secret_path in found)
    return key, secret


# ---------------------------------------------------------------- Woo GET


def orders_query(page: int, audit: bool) -> str:
    pairs = [("status", STATUSES), ("per_page", str(PER_PAGE)), ("page", str(page))]
    if not audit:
        pairs.append(("include_meta", ISSUED_META))
    return urllib.parse.urlencode(pairs, safe=",")


def header_int(headers, name: str) -> int | None:
    if headers is None:
        return None
    getter = getattr(headers, "get", None)
    value = getter(name) if getter else None
    if value is None and getter:
        value = getter(name.lower())
    if value is None:
        return None
    text = str(value).strip()
    if not text.isdigit():
        raise PullError("响应头无法读取")
    return int(text)


def parse_orders_body(raw: bytes, page: int) -> list:
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise PullError(f"第 {page} 页不是 JSON") from None
    if isinstance(data, dict):
        code = data.get("code")
        if isinstance(code, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,64}", code):
            raise PullError(f"接口错误 {code} 第 {page} 页")
        raise PullError(f"第 {page} 页不是订单列表")
    if not isinstance(data, list):
        raise PullError(f"第 {page} 页不是订单列表")
    return data


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ARG002
        raise PullError(f"HTTP {code} 拒绝跳转")


def build_opener():
    return urllib.request.build_opener(_NoRedirect)


def request_page(opener, key: str, secret: str, page: int, audit: bool):
    url = ORDERS_URL + "?" + orders_query(page, audit)
    try:
        token = base64.b64encode(f"{key}:{secret}".encode("ascii")).decode("ascii")
    except UnicodeEncodeError:
        raise PullError("密钥不是 ASCII") from None
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "User-Agent": "de-linker-playbook inquiry_pull",
        },
        method="GET",
    )
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            total = header_int(resp.headers, "X-WP-Total")
            pages = header_int(resp.headers, "X-WP-TotalPages")
            raw = resp.read(MAX_BODY + 1)
    except PullError:
        raise
    except urllib.error.HTTPError as e:
        code = getattr(e, "code", None)
        try:
            e.close()
        except Exception:
            pass
        if code in RETRY_CODES:
            raise Retryable(f"HTTP {code} 第 {page} 页") from None
        raise PullError(f"HTTP {code} 第 {page} 页") from None
    except (urllib.error.URLError, TimeoutError):
        raise Retryable(f"网络错误 第 {page} 页") from None
    if len(raw) > MAX_BODY:
        raise PullError(f"第 {page} 页响应过大")
    try:
        return parse_orders_body(raw, page), total, pages
    finally:
        del raw


def request_page_retry(opener, key: str, secret: str, page: int, audit: bool, sleep=time.sleep):
    last: Retryable | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            return request_page(opener, key, secret, page, audit)
        except Retryable as e:
            last = e
            if attempt == RETRIES:
                raise
            log(f"第 {page} 页临时失败，重试 {attempt}")
            sleep(attempt)
    raise last  # pragma: no cover


def make_fetcher(key: str, secret: str, opener=None):
    client = opener or build_opener()

    def fetch(page: int, audit: bool):
        return request_page_retry(client, key, secret, page, audit)

    return fetch


# ---------------------------------------------------------------- project / audit


def _scalar_id(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value if value > 0 else None
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def meta_key_names(order: dict) -> tuple[list[str], int]:
    meta = order.get("meta_data")
    names: list[str] = []
    unsafe = 0
    if not isinstance(meta, list):
        return names, unsafe
    for item in meta:
        if not isinstance(item, dict):
            unsafe += 1
            continue
        key = item.get("key")
        if isinstance(key, str) and SAFE_KEY.fullmatch(key):
            names.append(key)
        else:
            unsafe += 1
    return names, unsafe


def project_order(order: dict) -> dict:
    """Copy the sheet fields only. Nested billing / meta values are not retained."""
    billing = order.get("billing")
    company = None
    if isinstance(billing, dict):
        raw = billing.get("company")
        if isinstance(raw, str):
            company = raw.strip() or None
    issued = None
    meta = order.get("meta_data")
    if isinstance(meta, list):
        for item in meta:
            if not isinstance(item, dict) or item.get("key") != ISSUED_META:
                continue
            value = item.get("value")
            if value in (None, ""):
                issued = None
            elif isinstance(value, str) or (isinstance(value, int) and not isinstance(value, bool)):
                issued = value
            else:
                issued = BAD_ISSUED
            break
    number = order.get("number")
    if isinstance(number, bool) or not isinstance(number, (int, str)):
        number = None
    created = order.get("date_created_gmt")
    status = order.get("status")
    return {
        "id": _scalar_id(order.get("id")),
        "number": number,
        "company": company,
        "created_gmt": created if isinstance(created, str) else None,
        "status": status if isinstance(status, str) else None,
        "issued": issued,
    }


def scrub(order: dict, audit: bool) -> dict:
    rec = project_order(order)
    if audit:
        names, unsafe = meta_key_names(order)
        rec["meta_keys"] = names
        rec["unsafe_key_count"] = unsafe
        rec["number_matches_id"] = (
            rec["id"] is not None and rec["number"] is not None and str(rec["number"]) == str(rec["id"])
        )
    return rec


def gmt_to_beijing(value: str) -> str:
    text = value.strip()
    if not text:
        raise MappingError("缺创建时刻")
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        raise MappingError("创建时刻无法换算") from None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return bt.stamp(parsed)


def unix_to_beijing(value) -> str:
    if isinstance(value, str):
        text = value.strip()
        if not UNIX_TEXT.fullmatch(text):
            raise MappingError("签发时刻无法换算")
        value = int(text)
    if isinstance(value, bool) or not isinstance(value, int):
        raise MappingError("签发时刻无法换算")
    if not UNIX_MIN <= value <= UNIX_MAX:
        raise MappingError("签发时刻无法换算")
    return bt.stamp(datetime.fromtimestamp(value, timezone.utc))


def to_sheet_row(rec: dict) -> dict:
    oid = rec.get("id")
    if not isinstance(oid, int):
        raise MappingError("缺内部编号")
    number = rec.get("number")
    if isinstance(number, int) and not isinstance(number, bool):
        number = str(number)
    if not isinstance(number, str) or not number.strip():
        raise MappingError(f"id {oid} 缺单号")
    status = rec.get("status")
    if status not in STATUS_ZH:
        if isinstance(status, str) and SAFE_SLUG.fullmatch(status):
            raise MappingError(f"id {oid} 状态无法映射 {status}")
        raise MappingError(f"id {oid} 状态无法映射")
    created = rec.get("created_gmt")
    if not isinstance(created, str) or not created.strip():
        raise MappingError(f"id {oid} 缺创建时刻")
    issued = rec.get("issued")
    issued_bj = None
    if issued is BAD_ISSUED:
        raise MappingError(f"id {oid} 签发时刻无法换算")
    if issued not in (None, ""):
        try:
            issued_bj = unix_to_beijing(issued)
        except MappingError:
            raise MappingError(f"id {oid} 签发时刻无法换算") from None
    return {
        "询盘内部编号": oid,
        "单号": number.strip(),
        "公司": rec.get("company") or None,
        "创建时刻（北京时间）": gmt_to_beijing(created),
        "状态": STATUS_ZH[status],
        "形式发票签发时刻（北京时间）": issued_bj,
    }


def rows_from_projected(records: list[dict]) -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    errors: list[str] = []
    seen: set[int] = set()
    for rec in records:
        try:
            row = to_sheet_row(rec)
        except MappingError as e:
            errors.append(str(e))
            continue
        if row["询盘内部编号"] in seen:
            errors.append(f"id {row['询盘内部编号']} 重复")
            continue
        seen.add(row["询盘内部编号"])
        rows.append(row)
    return rows, errors


def format_id_list(ids: list[int]) -> str:
    if not ids:
        return "无"
    if len(ids) > 40:
        return f"{ids[0]}…{ids[-1]} 共 {len(ids)}"
    return ",".join(str(i) for i in ids)


def audit_lines(records: list[dict]) -> list[str]:
    ids = sorted(r["id"] for r in records if isinstance(r.get("id"), int))
    lines = [f"审计 {len(records)} 笔，不写表，不记录字段值，id {format_id_list(ids)}"]
    counts: dict[str, int] = {}
    for rec in records:
        for key in set(rec.get("meta_keys") or []):
            counts[key] = counts.get(key, 0) + 1
    attr = [k for k in sorted(counts) if k.startswith(ATTR_PREFIX)]
    attr_text = "，".join(f"{k} {counts[k]}" for k in attr) if attr else "无"
    lines.append("订单来源字段名及存在笔数：" + attr_text)

    def has(part: str) -> str:
        return "有" if any(part in k for k in attr) else "无"

    # Names come from this response. Presence only; values (including user agent) are not printed.
    lines.append(
        "来源类型 " + has("source_type")
        + "，referrer " + has("referrer")
        + "，UTM " + has("utm_")
        + "，会话 " + has("session_")
        + "，设备 " + has("device_type")
        + "，浏览器标识字段 " + has("user_agent")
    )
    unsafe = sum(int(r.get("unsafe_key_count") or 0) for r in records)
    if unsafe:
        lines.append(f"跳过 {unsafe} 个不安全字段名")
    matched = sum(1 for r in records if r.get("number_matches_id"))
    lines.append(f"单号与内部编号相同 {matched}，不同 {len(records) - matched}")
    issued = counts.get(ISSUED_META, 0)
    lines.append(f"{ISSUED_META} 存在 {issued}/{len(records)}")
    return lines


# ---------------------------------------------------------------- reconcile


def merge_preserved(existing: list[dict], incoming: list[dict]) -> list[dict]:
    by_id = {}
    for row in existing:
        oid = row.get("询盘内部编号")
        if isinstance(oid, int) and not isinstance(oid, bool):
            by_id[oid] = row
    merged = []
    for row in sorted(incoming, key=lambda r: r["询盘内部编号"]):
        item = dict(row)
        old = by_id.get(item["询盘内部编号"])
        if old:
            for col in PRESERVE:
                if old.get(col) not in (None, ""):
                    item[col] = old[col]
        merged.append(item)
    return merged


def stale_rows(existing: list[dict], incoming: list[dict]) -> list[dict]:
    ids = {r["询盘内部编号"] for r in incoming}
    return [r for r in existing if r.get("询盘内部编号") not in ids]


def diff_counts(existing: list[dict], merged: list[dict]) -> tuple[int, int]:
    spec = bt.load_schema()["$defs"][SHEET]
    cols = [c for c in bt.columns(spec) if not c.startswith("写入时刻")]
    by_key = {bt.row_key(spec, r): r for r in existing}
    added = updated = 0
    for row in merged:
        old = by_key.get(bt.row_key(spec, row))
        if old is None:
            added += 1
        elif any(not _same(old.get(c), row.get(c)) for c in cols):
            updated += 1
    return added, updated


def _sheet_id(svc, sid: str, title: str) -> int:
    try:
        meta = svc.spreadsheets().get(
            spreadsheetId=sid, fields="sheets(properties(sheetId,title))"
        ).execute(num_retries=bt.RETRIES)
    except Exception:
        raise PullError("读表结构失败") from None
    props = next((s["properties"] for s in meta.get("sheets", []) if s["properties"]["title"] == title), None)
    if props is None or "sheetId" not in props:
        raise PullError(f"底表里没有「{title}」页")
    return props["sheetId"]


def delete_stale_rows(svc, sid: str, stale: list[dict]) -> None:
    """Delete rows that left the four statuses. Never blank them: the sheet has no empty rows."""
    if not stale:
        return
    numbers = []
    for row in stale:
        n = row.get("_row")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise PullError("现有行缺少行号，不写表")
        numbers.append(n)
    gid = _sheet_id(svc, sid, SHEET)
    requests = [{
        "deleteDimension": {
            "range": {
                "sheetId": gid,
                "dimension": "ROWS",
                "startIndex": n - 1,
                "endIndex": n,
            }
        }
    } for n in sorted(set(numbers), reverse=True)]
    svc.spreadsheets().batchUpdate(spreadsheetId=sid, body={"requests": requests}).execute(num_retries=bt.RETRIES)
    bt._grid_rows.pop((sid, SHEET), None)


def apply_inquiry_rows(svc, sid: str, schema: dict, rows: list[dict], existing: list[dict], now: str):
    merged = merge_preserved(existing, rows)
    stale = stale_rows(existing, merged)
    if any(not isinstance(r.get("_row"), int) or isinstance(r.get("_row"), bool) or r["_row"] < 2 for r in stale):
        raise PullError("现有行缺少行号，不写表")
    added, updated = bt.upsert_rows(svc, sid, schema, SHEET, merged, now, existing=existing)
    delete_stale_rows(svc, sid, stale)
    return added, updated, len(stale)


class LiveTable:
    def __init__(self):
        self.schema = bt.load_schema()
        self.sid = bt.load_target("main")
        self.svc = bt.sheets_service()
        self.now = bt.stamp(bt.beijing_now())

    def read(self) -> list[dict]:
        return bt.read_table(self.svc, self.sid, self.schema, SHEET)

    def write(self, rows: list[dict], existing: list[dict]):
        return apply_inquiry_rows(self.svc, self.sid, self.schema, rows, existing, self.now)

    def refresh(self) -> int:
        return bt.refresh_progress(self.svc, self.sid, self.schema, self.now)


def collect(fetch, audit: bool) -> list[dict]:
    out: list[dict] = []
    seen: set[int] = set()
    total = None
    total_pages = None
    page = 1
    while page <= MAX_PAGES:
        raw_batch, page_total, page_pages = fetch(page, audit)
        if not isinstance(raw_batch, list):
            raise PullError(f"第 {page} 页不是列表")
        if page == 1 and page_total is None:
            raise PullError("缺少总条数，不写表")
        if page_total is not None:
            if total is None:
                total = page_total
            elif total != page_total:
                raise PullError("总条数在翻页中变化")
        if page_pages is not None:
            if total_pages is None:
                total_pages = page_pages
            elif total_pages != page_pages:
                raise PullError("总页数在翻页中变化")
        batch = []
        for order in raw_batch:
            if not isinstance(order, dict):
                raise PullError(f"第 {page} 页有非对象条目")
            batch.append(scrub(order, audit))
        del raw_batch
        for rec in batch:
            oid = rec.get("id")
            if isinstance(oid, int) and oid in seen:
                raise PullError(f"第 {page} 页重复 id {oid}")
            if isinstance(oid, int):
                seen.add(oid)
        out.extend(batch)
        if total is not None and len(out) > total:
            raise PullError(f"条数超出响应头 {total}")
        if total == 0 or (total is not None and len(out) >= total):
            break
        if total_pages is not None and page >= total_pages:
            break
        if len(batch) < PER_PAGE:
            break
        page += 1
    else:
        raise PullError("翻页超过上限")
    if total is not None and len(out) != total:
        raise PullError(f"条数不一致 响应头 {total} 实际 {len(out)}")
    return out


def _run(dry: bool, audit: bool, fetch_page, table) -> int:
    if fetch_page is None:
        key, secret = load_secrets()
        fetch_page = make_fetcher(key, secret)
        del key, secret
    mode = "审计，不写表" if audit else "试跑，不写表" if dry else "写正式底表"
    log(f"开始（{mode}）")
    records = collect(fetch_page, audit)
    if audit:
        for line in audit_lines(records):
            log(line)
        if not dry:
            log("结束，无错误")
            return 0
    rows, errors = rows_from_projected(records)
    if errors:
        for item in errors:
            log(f"出错 {item}")
        log(f"结束，有 {len(errors)} 处出错")
        return 1
    table = table or LiveTable()
    existing = table.read()
    merged = merge_preserved(existing, rows)
    removed = stale_rows(existing, merged)
    counts: dict[str, int] = {}
    for row in merged:
        counts[row["状态"]] = counts.get(row["状态"], 0) + 1
    status_txt = "，".join(f"{name} {counts[name]}" for name in STATUS_ZH.values() if counts.get(name))
    extra = f"（{status_txt}）" if status_txt else ""
    log(f"取到 {len(merged)} 笔{extra}，id {format_id_list([r['询盘内部编号'] for r in merged])}")
    if any("_row" not in r for r in removed):
        raise PullError("现有行缺少行号，不写表")
    if dry or audit:
        added, updated = diff_counts(existing, merged)
        log(f"不写表：会新增 {added}，覆盖 {updated}，移除 {len(removed)}")
        log("结束，无错误")
        return 0
    added, updated, n_removed = table.write(merged, existing)
    n = table.refresh()
    log(f"写入 {SHEET}：新增 {added} 行，覆盖 {updated} 行，移除 {n_removed} 行")
    log(f"动作进度：重算 {n} 行")
    log("结束，无错误")
    return 0


def run(dry: bool, audit: bool, *, fetch_page=None, table=None) -> int:
    try:
        return _run(dry, audit, fetch_page, table)
    except PullError as e:
        log(f"出错 {e}")
        log("结束，有 1 处出错")
        return 1
    except Exception as e:
        log(f"出错 {type(e).__name__}")
        log("结束，有 1 处出错")
        return 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("run")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--audit-order-attribution", action="store_true")
    args = ap.parse_args()
    sys.exit(run(args.dry_run, args.audit_order_attribution))


if __name__ == "__main__":
    main()
