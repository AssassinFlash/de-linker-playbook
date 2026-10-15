# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "openpyxl>=3.1",
# ]
# ///
"""
执行登记：操作者说「我发了 / 上线了 / 更新了 / 发出去了」，或新站上线了一批 PR → AI 查证 → 写进底表「执行登记」。
流程（什么时候登、怎么问、怎么选动作）在 skills/marketing-execution-log/SKILL.md；本脚本只做机械的部分。

  uv run scripts/execution_log.py check --url URL --expect "关键句" [--expect ...] [--old-url 旧网址]
                       只查证、不写表：抓线上，看能不能打开、关键句在不在
  uv run scripts/execution_log.py add --channel 网站 --action 改正文 --desc "一句话" --url URL --expect "关键句" ...
                       查证 → 认重复 → 编号 → 写一行 → 重算动作进度；打印编号和查证结论
  uv run scripts/execution_log.py add --from-json 文件.json
                       一次登多行（补登用）：JSON 是数组，每项用执行登记的中文列名，另可带
                       "expect": [...]、"证据前缀": "..."；字段含义同下面的参数
  uv run scripts/execution_log.py recheck --id E-YYYYMMDD-NN [--url 新网址] [--expect ...] [--note "原因"]
                       对已登记的一行重新查证（查证失败、弄清原因后），就地改这一行；证据里「线上复核」之前的
                       部分（PR 链接等）保留，只重做线上那一段；--note 记进备注
  uv run scripts/execution_log.py show [--date YYYY-MM-DD] [--id ID ...] [--source 来源 ...]
                       把登记过的行打印出来（核对用）

查证规则：
  网站          抓网址（不跟跳转）：HTTP 200 且每个 --expect 都在页面里 → 已查证；否则 → 查证失败（照写一行，
                「下一步」会按 E-01 排队弄清原因）。改网址时另抓 --old-url，要 301/308 跳到新网址。
                网站必须给至少一个 --expect（标题或口述里的关键句）。
  LinkedIn / 其他平台
                有网址就抓：200 且关键句都在 → 已查证；404/410 → 查证失败；其余（要登录、999、跳登录页）→
                未查证（无法公开访问）。没网址 → 未查证（无法公开访问），证据写原因。
  邮件          不抓，记「待邮箱接入后查证」；「邮箱 IMAP 回流」在「已发送」里找到后回填。
  --verify 结果 --evidence 证据   直接给结论（如 GSC 后台里的操作外部看不到），不抓。
  线上抓不到（网络错误，重试 3 次）→ 不写表，退出码 2，过一会再登。

重复：同一执行日期、同一渠道、同一动作、同一对象（网址；邮件看收件公司 + 外展序列 + 第几封；都没有就看内容说明）
已经有一行 → 不写，打印那一行的编号，退出码 3。确实是同一天又做了一次，加 --again。
编号：E-执行日期-当天序号（两位），按执行日期往后顺延，全表唯一。
凭据、表格 ID 的读取方式同 scripts/base_table.py；--target sample 写样例表（演练用，build --target sample 可复原）。
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urljoin

sys.dont_write_bytecode = True  # keep scripts/__pycache__ out of the repo
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402

SHEET = "执行登记"
UA = "Mozilla/5.0 (compatible; de-linker-playbook execution_log; +https://de-linker.com/)"
TRIES = 3
VERIFIED, FAILED, PRIVATE, MAIL = "已查证", "查证失败", "未查证（无法公开访问）", "待邮箱接入后查证"
MOVE = "改网址（旧址 301 跳新址）"
RECHECK = "线上复核"  # evidence = <PR 证据>；线上复核；<抓取结论>; recheck keeps the part before it
ARG_COLS = {  # CLI flag -> column
    "date": "执行日期", "line": "线", "channel": "渠道", "action": "动作", "desc": "内容说明", "url": "网址",
    "old_url": "旧网址", "company": "收件公司", "sequence": "外展序列", "nth": "第几封", "planned": "计划共几封",
    "next_date": "下一封计划日期", "deliverable": "对应交付物", "source": "来源", "note": "备注",
}


class Unreachable(Exception):
    pass


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url: str) -> dict:
    """One GET without following redirects; retries network errors, not HTTP answers."""
    opener = urllib.request.build_opener(_NoRedirect)
    last = ""
    for i in range(TRIES):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
        try:
            with opener.open(req, timeout=30) as resp:
                return {"status": resp.status, "location": "",
                        "body": resp.read(2_000_000).decode("utf-8", "replace")}
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location", "")
            return {"status": e.code, "location": urljoin(url, loc) if loc else "", "body": ""}
        except Exception as e:  # network trouble: try again, then give up without writing
            last = f"{type(e).__name__}: {e}"
            time.sleep(2 * (i + 1))
    raise Unreachable(f"{url} 没抓到（{last}）")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text)).strip().casefold()


def page_title(body: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", body, flags=re.I | re.S)
    return re.sub(r"\s+", " ", html.unescape(m.group(1))).strip() if m else ""


def verify(channel: str, url: str, expects: list[str], old_url: str = "") -> tuple[str, str]:
    """(查证结果, 查证证据) for one action, by the rules in this file's docstring."""
    if channel == "邮件":
        return MAIL, ""
    if not url:
        return PRIVATE, "没有公开网址，按操作者口述记录"
    got = fetch(url)
    status, body = got["status"], got["body"]
    if channel != "网站":
        if status == 200 and all(flat(x) in flat(body) for x in expects):
            return VERIFIED, f"HTTP 200，标题「{page_title(body)}」" + "".join(f"，找到「{x}」" for x in expects)
        if status in (404, 410):
            return FAILED, f"HTTP {status}，这个地址打不开"
        where = f"，跳到 {got['location']}" if got["location"] else ""
        return PRIVATE, f"HTTP {status}{where}：要登录才能看，按操作者口述记录"
    if status != 200:
        where = f"，跳到 {got['location']}（不是这个地址本身）" if got["location"] else ""
        return FAILED, f"HTTP {status}{where}"
    page = flat(body)
    missing = [x for x in expects if flat(x) not in page]
    parts = [f"HTTP 200，标题「{page_title(body)}」"]
    parts += [f"找到「{x}」" for x in expects if x not in missing]
    if missing:
        parts += [f"没找到「{x}」" for x in missing]
    if old_url:
        old = fetch(old_url)
        moved = old["status"] in (301, 308) and old["location"].rstrip("/") == url.rstrip("/")
        parts.append(f"旧地址 HTTP {old['status']}" + (f" 跳到 {old['location']}" if old["location"] else ""))
        if not moved:
            return FAILED, "，".join(parts) + "：旧地址没有 301 跳到新地址"
    return (FAILED if missing else VERIFIED), "，".join(parts)


def same_event(a: dict, b: dict) -> bool:
    if any(a.get(k) != b.get(k) for k in ("执行日期", "渠道", "动作")):
        return False
    if a.get("网址") or b.get("网址"):
        return (a.get("网址") or "").rstrip("/") == (b.get("网址") or "").rstrip("/")
    if a.get("收件公司") or b.get("收件公司"):
        return all(str(a.get(k, "")) == str(b.get(k, "")) for k in ("收件公司", "外展序列", "第几封"))
    return a.get("内容说明") == b.get("内容说明")


def check_row(schema: dict, r: dict) -> None:
    props = schema["$defs"][SHEET]["properties"]
    for col, v in r.items():
        if col not in props:
            raise SystemExit(f"执行登记没有「{col}」这一列")
        enum = props[col].get("enum")
        if enum and v not in enum:
            raise SystemExit(f"「{col}」只能是：{'、'.join(enum)}（收到「{v}」）")
        if props[col].get("format") == "date":
            date.fromisoformat(v)
        if props[col].get("format") == "uri" and not str(v).startswith(("https://", "http://")):
            raise SystemExit(f"「{col}」要写完整网址（收到「{v}」）")
    for col in schema["$defs"][SHEET]["required"]:
        if col not in ("登记编号", "登记时刻（北京时间）") and not r.get(col):
            raise SystemExit(f"缺「{col}」")
    if r["动作"] == MOVE and not r.get("旧网址"):
        raise SystemExit(f"动作「{MOVE}」要同时给 --old-url")


def prepare(schema: dict, item: dict, now: str) -> dict:
    """Fill defaults, verify, and return a full row without its 登记编号."""
    item = dict(item)
    expects = item.pop("expect", []) or []
    prefix = item.pop("证据前缀", "")
    r = {k: v for k, v in item.items() if v not in (None, "")}
    r.setdefault("执行日期", now[:10])
    r.setdefault("线", "营销")
    r.setdefault("来源", "操作者口述")
    r["动作大类"] = bt.prop(schema, SHEET, "动作")["x-category"].get(r.get("动作", ""), "")
    given = r.get("查证结果")
    if not given and r.get("渠道") == "网站" and r.get("网址") and not expects:
        raise SystemExit("网页查证要至少一个 --expect（标题或口述里的关键句）")
    check_row(schema, {**r, "查证结果": given or VERIFIED})
    if given:
        if not r.get("查证证据") and given != MAIL:
            raise SystemExit("直接给查证结果时要写 --evidence（为什么这样判）")
        if given != MAIL:
            r["查证时刻（北京时间）"] = now
        return r
    result, evidence = verify(r["渠道"], r.get("网址", ""), expects, r.get("旧网址", ""))
    r["查证结果"] = result
    if evidence or prefix:
        r["查证证据"] = "；".join(x for x in (prefix, evidence) if x)
    if result != MAIL:
        r["查证时刻（北京时间）"] = bt.stamp(bt.beijing_now())
    return r


def register(svc, sid: str, schema: dict, rows: list[dict], now: str, again: bool = False) -> list[dict]:
    """Number and write prepared rows; rows that repeat an existing one come back with 重复 and are not written.
    Returns every row (written ones carry their new 登记编号). Recomputes 动作进度 when anything was written."""
    existing = bt.read_table(svc, sid, schema, SHEET)
    seen = list(existing)
    out, new = [], []
    for r in rows:
        dup = None if again else next((e for e in seen if same_event(e, r)), None)
        if dup:
            out.append({**r, "重复": dup["登记编号"]})
            continue
        prefix = "E-" + r["执行日期"].replace("-", "") + "-"
        seq = max([int(e["登记编号"].rsplit("-", 1)[1]) for e in seen if e["登记编号"].startswith(prefix)], default=0)
        if seq >= 99:
            raise SystemExit(f"{r['执行日期']} 已有 99 条，编号两位不够用：先改 schema 的登记编号格式")
        row = {"登记编号": f"{prefix}{seq + 1:02d}", "登记时刻（北京时间）": now, **r}
        seen.append(row)
        new.append(row)
        out.append(row)
    if new:
        bt.upsert_rows(svc, sid, schema, SHEET, new, now, existing=existing)
        bt.refresh_progress(svc, sid, schema, now)
    return out


def describe(r: dict) -> str:
    target = r.get("网址") or r.get("收件公司") or r.get("内容说明")
    if r.get("重复"):
        return f"已登记过 {r['重复']}（{r['执行日期']}，{r['动作']}，{target}），没有再写"
    tail = f"：{r['查证证据']}" if r.get("查证证据") else ""
    return f"{r['登记编号']}  {r['执行日期']}  {r['渠道']} / {r['动作']}  {target}\n    查证：{r['查证结果']}{tail}"


def cmd_check(args) -> int:
    channel = args.channel or "网站"
    result, evidence = verify(channel, args.url, args.expect, args.old_url or "")
    print(f"{result}：{evidence}" if evidence else result)
    return 0 if result == VERIFIED else 1


def cmd_add(args) -> int:
    schema = bt.load_schema()
    now = bt.stamp(bt.beijing_now())
    if args.from_json:
        items = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
    else:
        item = {col: getattr(args, flag) for flag, col in ARG_COLS.items() if getattr(args, flag) not in (None, "")}
        if args.verify:
            item["查证结果"] = args.verify
            item["查证证据"] = args.evidence
        elif args.evidence:
            item["证据前缀"] = args.evidence
        item["expect"] = args.expect
        items = [item]
    rows = [prepare(schema, it, now) for it in items]
    svc = bt.sheets_service()
    out = register(svc, bt.load_target(args.target), schema, rows, now, again=args.again)
    for r in out:
        print(describe(r))
    written = [r for r in out if not r.get("重复")]
    print(f"写入 {len(written)} 行，重复 {len(out) - len(written)} 行；"
          f"查证失败 {sum(r['查证结果'] == FAILED for r in written)} 行")
    return 3 if len(out) == 1 and out[0].get("重复") else 0


def cmd_recheck(args) -> int:
    schema = bt.load_schema()
    svc = bt.sheets_service()
    sid = bt.load_target(args.target)
    now = bt.stamp(bt.beijing_now())
    rows = bt.read_table(svc, sid, schema, SHEET)
    old = next((r for r in rows if r["登记编号"] == args.id), None)
    if not old:
        raise SystemExit(f"执行登记里没有 {args.id}")
    url = args.url or old.get("网址", "")
    if old["渠道"] == "网站" and url and not args.expect:
        raise SystemExit("重新查证网页也要 --expect")
    result, evidence = verify(old["渠道"], url, args.expect, old.get("旧网址", ""))
    kept = old.get("查证证据", "")  # PR evidence before「线上复核」stays; only the live check is redone
    prefix = kept.split(RECHECK)[0] + RECHECK if RECHECK in kept else ""
    evidence = "；".join(x for x in (prefix, evidence) if x)
    note = f"{now[:10]} 重新查证（原结果：{old['查证结果']}" + (f"，原网址 {old['网址']}" if args.url else "") + "）"
    if args.note:
        note += f"：{args.note}"
    row = {**old, "网址": url or None, "查证结果": result, "查证证据": evidence or None,
           "查证时刻（北京时间）": None if result == MAIL else bt.stamp(bt.beijing_now()),
           "备注": "；".join(x for x in (old.get("备注"), note) if x)}
    bt.upsert_rows(svc, sid, schema, SHEET, [row], now, existing=rows)
    bt.refresh_progress(svc, sid, schema, now)
    print(describe(row))
    return 0 if result == VERIFIED else 1


def cmd_show(args) -> int:
    schema = bt.load_schema()
    rows = bt.read_table(bt.sheets_service(), bt.load_target(args.target), schema, SHEET)
    rows = [r for r in rows if (not args.date or r["执行日期"] == args.date) and (not args.id or r["登记编号"] in args.id)
            and (not args.source or r["来源"] in args.source)]
    for r in rows:
        print(json.dumps({k: v for k, v in r.items() if k != "_row"}, ensure_ascii=False))
    print(f"共 {len(rows)} 行")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", choices=["main", "sample"], default="main")
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check")
    c.add_argument("--url", required=True)
    c.add_argument("--expect", action="append", default=[])
    c.add_argument("--old-url")
    c.add_argument("--channel")
    a = sub.add_parser("add")
    a.add_argument("--from-json")
    a.add_argument("--date", help="执行日期，默认今天（北京时间）")
    a.add_argument("--line", help="营销（默认）| 获客")
    a.add_argument("--channel")
    a.add_argument("--action")
    a.add_argument("--desc")
    a.add_argument("--url")
    a.add_argument("--old-url")
    a.add_argument("--company")
    a.add_argument("--sequence")
    a.add_argument("--nth", type=int)
    a.add_argument("--planned", type=int)
    a.add_argument("--next-date")
    a.add_argument("--deliverable")
    a.add_argument("--source", help="操作者口述（默认）| 新站 PR | 补登")
    a.add_argument("--expect", action="append", default=[])
    a.add_argument("--verify", help="直接给查证结果（不抓线上），要配 --evidence")
    a.add_argument("--evidence", help="配 --verify 时是查证证据；否则加在自动查证结论前面（如 PR 链接）")
    a.add_argument("--note")
    a.add_argument("--again", action="store_true", help="同一天同一对象确实又做了一次")
    r = sub.add_parser("recheck")
    r.add_argument("--id", required=True)
    r.add_argument("--url")
    r.add_argument("--expect", action="append", default=[])
    r.add_argument("--note", help="弄清的原因，记进备注")
    s = sub.add_parser("show")
    s.add_argument("--date")
    s.add_argument("--id", action="append")
    s.add_argument("--source", action="append", help="只看某种来源（可多次），如 --source 新站PR --source 补登")
    args = ap.parse_args()
    if args.command == "add" and not args.from_json and not (args.channel and args.action and args.desc):
        raise SystemExit("add 要 --channel、--action、--desc（或 --from-json）")
    try:
        sys.exit({"check": cmd_check, "add": cmd_add, "recheck": cmd_recheck, "show": cmd_show}[args.command](args))
    except Unreachable as e:
        print(f"线上抓不到，没有写表：{e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
