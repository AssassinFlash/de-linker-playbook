# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "imap-tools>=1.7",
# ]
# ///
"""
邮箱 IMAP 回流：只读 chester@de-linker.com，把已登记邮件对上「已发送」，再写邮件反馈。

  uv run scripts/mailbox_pull.py run
  uv run scripts/mailbox_pull.py run --dry-run
  uv run scripts/mailbox_pull.py selftest

只读。imap_tools 的 folder.set(readonly=True) 走 imaplib.select(readonly=True)，
那条命令就是 EXAMINE。取信用 headers_only 和 mark_seen=False，对应 BODY.PEEK。
不调用会改标记、移动或删除的命令。登录时不选任何文件夹。

密码不进仓库。config.toml 的 [mailbox] 只放指针。日志只打条数和登记编号。
正文、地址、主题不进表，也不进日志。每日提醒（主题以「de-linker 下一步」开头，
或 Message-ID 域名是 de-linker-playbook.local）直接跳过。

定时不另装。gsc_pull.py schedule install 的 08:30 任务在询盘回流之后跑本脚本，
再导出看板。更新定时不会立刻跑，不要 kickstart。
"""
from __future__ import annotations

import argparse
import os
import re
import stat
import sys
import tomllib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parseaddr
from pathlib import Path
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402

SHEET = "邮件反馈"
LOG_SHEET = "执行登记"
BEIJING = ZoneInfo("Asia/Shanghai")
OWN = {"chester@de-linker.com", "sales@de-linker.com"}
REMINDER_SUBJECT = "de-linker 下一步"
REMINDER_DOMAIN = "de-linker-playbook.local"
SENT_NAMES = ("已发送", "sent", "sent messages", "sent items", "发件箱")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
ID_RE = re.compile(r"<[^<>\s@]+@[^<>\s]+>")
STATUS_RE = re.compile(r"\b([245]\.\d{1,3}\.\d{1,3})\b")
PENDING = {"待邮箱接入后查证", "查证失败"}
FOUND = "在「已发送」里找到这封信"
MISS = "在「已发送」里没有对上这封信"
MANY = "在「已发送」里对上了多封，没有猜"
NO_ADDRESS = "交付物里没有可对上的收件地址"
REPLY_NOT_NEW = "对上的是回复，不是这次登记的新发信"
INFERRED = "未见退信，按发送日推断已送达，不是投递回执"
NO_CODE = "退信通知没有增强状态码，先按暂时退信，不停地址"


class PullError(RuntimeError):
    pass


@dataclass
class Header:
    uid: str
    message_id: str
    day: str
    subject: str = ""
    from_addr: str = ""
    recipients: set[str] = field(default_factory=set)
    reply_ids: set[str] = field(default_factory=set)
    auto_submitted: str = ""
    content_type: str = ""


def log(msg: str) -> None:
    print(f"[{bt.stamp(bt.beijing_now())}] 邮箱：{msg}", flush=True)


def config_path() -> Path:
    return Path(os.environ.get("PLAYBOOK_CONFIG", bt.CONFIG_DIR / "config.toml"))


def load_mailbox_config(path: Path | None = None) -> dict:
    cfg = path or config_path()
    if not cfg.exists():
        raise PullError("找不到 config.toml")
    data = tomllib.loads(cfg.read_text(encoding="utf-8")).get("mailbox") or {}
    required = ("imap_host", "imap_port", "imap_user", "imap_password_file")
    missing = [key for key in required if not data.get(key)]
    if missing:
        raise PullError("config.toml 的 [mailbox] 缺指针")
    secret = Path(str(data["imap_password_file"])).expanduser()
    if not secret.is_absolute():
        secret = cfg.parent / secret
    return {
        "host": str(data["imap_host"]),
        "port": int(data["imap_port"]),
        "user": str(data["imap_user"]),
        "password_file": secret,
    }


def read_secret(path: Path) -> str:
    if not path.exists() or path.is_symlink() or not path.is_file():
        raise PullError("专用密码文件不存在或不是普通文件")
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode != 0o600:
        raise PullError(f"专用密码文件权限 {mode:03o}，应为 600")
    token = path.read_text(encoding="utf-8").strip()
    if not token or any(ch.isspace() for ch in token):
        raise PullError("专用密码文件必须是一行")
    return token


def scrub(text: str, secret: str = "") -> str:
    if secret:
        text = text.replace(secret, "")
    return EMAIL_RE.sub("…", text)[:180]


def norm_id(value: str) -> str:
    value = (value or "").strip()
    match = ID_RE.search(value)
    if match:
        return match.group(0).casefold()
    bare = value.strip("<>").strip()
    if "@" in bare and " " not in bare:
        return f"<{bare}>".casefold()
    return ""


def ids_in(value: str) -> set[str]:
    return {item.casefold() for item in ID_RE.findall(value or "")}


def domain_of(message_id: str) -> str:
    bare = message_id.strip("<>")
    return bare.split("@", 1)[1].casefold() if "@" in bare else ""


def is_reminder(header: Header) -> bool:
    subject = header.subject.lstrip()
    return subject.startswith(REMINDER_SUBJECT) or domain_of(header.message_id) == REMINDER_DOMAIN


def beijing_day(value: datetime | None) -> str:
    if value is None or value.tzinfo is None:
        return ""
    return value.astimezone(BEIJING).strftime("%Y-%m-%d")


def pick_sent(folders: list[tuple[str, tuple[str, ...]]]) -> str | None:
    flagged = [name for name, flags in folders if "\\Sent" in flags]
    if len(flagged) == 1:
        return flagged[0]
    folded = {name.casefold(): name for name, _flags in folders}
    for candidate in SENT_NAMES:
        if candidate.casefold() in folded:
            return folded[candidate.casefold()]
    return None


def addresses_in(text: str) -> set[str]:
    return {item.casefold() for item in EMAIL_RE.findall(text or "")} - OWN


def new_send(action: str) -> bool:
    return action in {"发出首封", "发出跟进"}



def choose_sent(folders: list[tuple[str, tuple[str, ...]]], messages) -> str | None:
    """Prefer the sent folder that actually has mail. Tencent lists Sent Messages and also accepts 已发送."""
    names = {name: flags for name, flags in folders}
    candidates = [name for name, flags in folders if "\\Sent" in flags or name.casefold() in {item.casefold() for item in SENT_NAMES}]
    for extra in ("已发送", "Sent Messages", "Sent"):
        if extra not in candidates and messages(extra) is not None:
            candidates.append(extra)
    if not candidates:
        return None
    ranked = sorted(candidates, key=lambda name: (
        (messages(name) or 0) > 0,
        name == "已发送",
        "\\Sent" in names.get(name, ()),
    ), reverse=True)
    return ranked[0]


def match_sent(row: dict, sent: list[Header], recipients: set[str]) -> tuple[Header | None, str]:
    if not recipients:
        return None, NO_ADDRESS
    day = row.get("执行日期") or ""
    hits = [msg for msg in sent if not is_reminder(msg) and msg.day == day and msg.recipients & recipients]
    if new_send(row.get("动作") or ""):
        fresh = [msg for msg in hits if not msg.reply_ids]
        if hits and not fresh:
            return None, REPLY_NOT_NEW
        hits = fresh
    if not hits:
        return None, MISS
    if len(hits) > 1:
        return None, MANY
    return hits[0], FOUND


def bounce_event(code: str) -> str:
    if not code:
        return "暂时退信"
    parts = code.split(".")
    if len(parts) == 3 and parts[1] == "2" and parts[2] == "2":
        return "暂时退信"
    if code.startswith("4."):
        return "暂时退信"
    if code.startswith("5.7"):
        return "认证或信誉拒收"
    if code.startswith("5."):
        return "永久退信"
    return "暂时退信"


def classify_reply(text: str) -> str:
    folded = (text or "").casefold()
    if any(word in folded for word in ("unsubscribe", "opt out", "opt-out", "remove me", "退订", "不要再发", "stop emailing")):
        return "拒绝或退订"
    if any(word in folded for word in ("quote", "quotation", "price list", "sample", "rfq", "报价", "样品", "价格")):
        return "要报价、规格、价格或样品"
    if any(word in folded for word in ("too expensive", "already have a supplier", "太贵", "已有供应商")):
        return "提出反对"
    return "其他"


def looks_like_bounce(header: Header) -> bool:
    local = header.from_addr.split("@", 1)[0]
    subject = header.subject.casefold()
    return (
        local in {"mailer-daemon", "postmaster", "mailer"}
        or "delivery-status" in header.content_type.casefold()
        or any(word in subject for word in ("undeliver", "delivery status", "failure notice", "退信", "未送达"))
    )


def event_row(row: dict, day: str, kind: str, reply_id: str = "", code: str = "", reply_class: str = "", note: str = "") -> dict:
    level = bt.EVENT_LEVEL[kind]
    out = {
        "事件日期": day,
        "登记编号": row["登记编号"],
        "收件公司": row.get("收件公司") or "",
        "事件类型": kind,
        "反馈级别": level,
    }
    if code:
        out["退信状态码"] = code
    if reply_class:
        out["回复分类"] = reply_class
    if reply_id:
        out["回信 Message-ID"] = reply_id
    if note:
        out["备注"] = note
    return out


def linked(header: Header, sent_id: str, extra_ids: set[str]) -> bool:
    return sent_id in header.reply_ids or sent_id in extra_ids


def plan(rows: list[dict], sent: list[Header], inbox: list[Header], addresses_for, peek_bounce, peek_class) -> dict:
    """Return log updates, feedback rows, contradictory inferred rows, and counts. No personal fields leave this function except Message-IDs already destined for the sheet."""
    updates, feedback, drop = [], [], []
    sent_by_id = {msg.message_id: msg for msg in sent if msg.message_id}
    inbox = [msg for msg in inbox if not is_reminder(msg)]
    pending = found = failed = 0
    for row in rows:
        if row.get("渠道") != "邮件":
            continue
        sent_msg = None
        sent_id = norm_id(row.get("邮件 Message-ID") or "")
        if row.get("查证结果") in PENDING or not sent_id:
            pending += 1
            sent_msg, evidence = match_sent(row, sent, addresses_for(row))
            if sent_msg is None:
                failed += 1
                if row.get("查证结果") != "查证失败" or row.get("查证证据") != evidence:
                    changed = {k: v for k, v in row.items() if k != "_row"}
                    changed["查证结果"] = "查证失败"
                    changed["查证证据"] = evidence
                    updates.append(changed)
                continue
            found += 1
            sent_id = sent_msg.message_id
            changed = {k: v for k, v in row.items() if k != "_row"}
            changed.update({
                "查证结果": "已查证",
                "查证证据": FOUND,
                "邮件 Message-ID": sent_msg.message_id,
            })
            updates.append(changed)
        else:
            sent_msg = sent_by_id.get(sent_id)
        if not sent_id:
            continue
        day = (sent_msg.day if sent_msg else "") or row.get("执行日期") or ""
        bounces = []
        replies = []
        for msg in inbox:
            extra: set[str] = set()
            code = ""
            if looks_like_bounce(msg):
                code, extra = peek_bounce(msg)
                if linked(msg, sent_id, extra):
                    bounces.append((msg, code))
                    continue
            if sent_id in msg.reply_ids and not looks_like_bounce(msg):
                replies.append(msg)
        if bounces:
            for msg, code in bounces:
                kind = bounce_event(code)
                feedback.append(event_row(
                    row, msg.day or day, kind, reply_id=msg.message_id, code=code,
                    note="" if code else NO_CODE,
                ))
        else:
            feedback.append(event_row(row, day, "未见退信（推断已送达）", note=INFERRED))
        for msg in replies:
            if msg.auto_submitted.casefold().startswith("auto-"):
                feedback.append(event_row(row, msg.day or day, "自动回复", reply_id=msg.message_id))
            else:
                feedback.append(event_row(
                    row, msg.day or day, "真人回复", reply_id=msg.message_id, reply_class=peek_class(msg),
                ))
    return {"updates": updates, "feedback": feedback, "drop_inferred": drop, "pending": pending, "found": found, "failed": failed}


def contradictory(existing: list[dict], feedback: list[dict]) -> list[dict]:
    bounced = {row["登记编号"] for row in feedback if row["事件类型"] not in {"已发送里找到", "未见退信（推断已送达）", "自动回复", "真人回复"}}
    return [row for row in existing if row.get("事件类型") == "未见退信（推断已送达）" and row.get("登记编号") in bounced]


SAFE_COLUMNS = {"查证证据", "备注", "收件公司", "事件类型", "回复分类", "反馈级别", "查证结果", "退信状态码"}


def safe_rows(rows: list[dict]) -> None:
    for row in rows:
        blob = " ".join(str(row.get(col) or "") for col in SAFE_COLUMNS)
        if EMAIL_RE.search(blob) or "\n" in blob:
            raise PullError("准备写入的说明里有地址或换行，已停下")


class LiveBox:
    def __init__(self, cfg: dict, secret: str):
        from imap_tools import MailBox

        self.secret = secret
        self.box = MailBox(cfg["host"], port=cfg["port"], timeout=60)
        try:
            self.box.login(cfg["user"], secret, initial_folder=None)
        except Exception as exc:
            raise PullError(f"登录失败：{scrub(str(exc), secret)}") from None

    def close(self) -> None:
        try:
            self.box.logout()
        except Exception:
            pass

    def folders(self) -> list[tuple[str, tuple[str, ...]]]:
        return [(item.name, tuple(item.flags)) for item in self.box.folder.list()]

    def messages(self, folder: str) -> int | None:
        try:
            return int(self.box.folder.status(folder, ["MESSAGES"]).get("MESSAGES", 0))
        except Exception:
            return None

    def unseen(self, folder: str) -> int:
        try:
            return int(self.box.folder.status(folder, ["UNSEEN"]).get("UNSEEN", 0))
        except Exception as exc:
            raise PullError(f"读未读数失败：{scrub(str(exc), self.secret)}") from None

    def headers(self, folder: str) -> list[Header]:
        from imap_tools import AND

        try:
            self.box.folder.set(folder, readonly=True)
            out = []
            for msg in self.box.fetch(AND(all=True), mark_seen=False, headers_only=True, bulk=50):
                out.append(header_from(msg))
            return out
        except Exception as exc:
            raise PullError(f"读取文件夹失败：{scrub(str(exc), self.secret)}") from None

    def peek_bounce(self, header: Header) -> tuple[str, set[str]]:
        return peek_limited(self, header, want="bounce")

    def peek_class(self, header: Header) -> str:
        kind, _ids = peek_limited(self, header, want="class")
        return kind


def header_from(msg) -> Header:
    headers = {str(k).casefold(): " ".join(v) if isinstance(v, (list, tuple)) else str(v) for k, v in (msg.headers or {}).items()}
    message_id = norm_id(headers.get("message-id") or "")
    recipients = {str(item).casefold() for item in (msg.to or ())}
    recipients |= {str(item).casefold() for item in (msg.cc or ())}
    recipients |= addresses_in(headers.get("to", ""))
    recipients |= addresses_in(headers.get("cc", ""))
    recipients -= OWN
    reply_ids = ids_in(headers.get("in-reply-to", "")) | ids_in(headers.get("references", ""))
    sender = parseaddr(headers.get("from") or getattr(msg, "from_", "") or "")[1].casefold()
    return Header(
        uid=str(msg.uid),
        message_id=message_id,
        day=beijing_day(msg.date),
        subject=msg.subject or headers.get("subject", ""),
        from_addr=sender,
        recipients=recipients,
        reply_ids=reply_ids,
        auto_submitted=headers.get("auto-submitted", ""),
        content_type=headers.get("content-type", ""),
    )


def peek_limited(source: LiveBox, header: Header, want: str) -> tuple[str, set[str]]:
    """BODY.PEEK one candidate, keep only a status code or a reply class, then drop the text."""
    try:
        source.box.folder.set("INBOX", readonly=True)
        found = None
        for msg in source.box.fetch(mark_seen=False, headers_only=False, uid_list=[header.uid], bulk=False):
            found = msg
            break
        if found is None:
            return ("", set()) if want == "bounce" else ("其他", set())
        text = "\n".join(part for part in (found.text, found.html) if part)
        if want == "bounce":
            code = ""
            match = STATUS_RE.search(text)
            if match:
                code = match.group(1)
            return code, ids_in(text)
        kind = classify_reply(text)
        del text
        return kind, set()
    except Exception as exc:
        raise PullError(f"读取退信或回复分类失败：{scrub(str(exc), source.secret)}") from None


def vault_root() -> Path:
    return (Path(__file__).resolve().parents[1] / "deliverables").resolve()


def emails_in_file(path: Path, root: Path) -> set[str]:
    try:
        path = path.resolve()
    except OSError:
        return set()
    if root not in path.parents and path != root:
        return set()
    if not path.is_file() or path.stat().st_size > 1_000_000:
        return set()
    if path.suffix.lower() not in {".md", ".txt", ".html", ""}:
        return set()
    try:
        return addresses_in(path.read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return set()


def addresses_for_row(row: dict) -> set[str]:
    root = vault_root()
    found: set[str] = set()
    raw = (row.get("对应交付物") or "").strip()
    if raw:
        candidate = Path(raw)
        options = [candidate] if candidate.is_absolute() else [root / raw, root / raw.removeprefix("deliverables/")]
        for option in options:
            found |= emails_in_file(option, root)
    company = (row.get("收件公司") or "").strip()
    if company and not found:
        contacts = root / "lead" / "03-contacts"
        if contacts.is_dir():
            needle = company.casefold()
            files = [p for p in contacts.rglob("*") if p.is_file() and needle in p.name.casefold()][:20]
            for path in files:
                found |= emails_in_file(path, root)
    return found


def apply(dry: bool) -> int:
    cfg = load_mailbox_config()
    secret = read_secret(cfg["password_file"])
    schema = bt.load_schema()
    svc = bt.sheets_service()
    sid = bt.load_target("main")
    log_rows = bt.read_table(svc, sid, schema, LOG_SHEET)
    existing = bt.read_table(svc, sid, schema, SHEET)
    box = LiveBox(cfg, secret)
    try:
        folders = box.folders()
        sent_name = choose_sent(folders, box.messages)
        if not sent_name:
            raise PullError("没有找到已发送文件夹")
        before = box.unseen("INBOX")
        sent = box.headers(sent_name)
        inbox = box.headers("INBOX")
        result = plan(log_rows, sent, inbox, addresses_for_row, box.peek_bounce, box.peek_class)
        after = box.unseen("INBOX")
    finally:
        box.close()
        secret = ""
    if before != after:
        raise PullError(f"未读数变了：{before}→{after}，不写表")
    safe_rows(result["updates"])
    safe_rows(result["feedback"])
    now = bt.stamp(bt.beijing_now())
    for row in result["updates"]:
        row["查证时刻（北京时间）"] = now
    drop = contradictory(existing, result["feedback"])
    log(
        f"文件夹 {scrub(sent_name)}，已发送 {len(sent)}，收件箱 {len(inbox)}，待查证 {result['pending']}，对上 {result['found']}，"
        f"没对上 {result['failed']}，事件 {len(result['feedback'])}，未读 {before}→{after}"
    )
    if dry:
        log("演练，不写表")
        return 0
    if result["updates"]:
        bt.upsert_rows(svc, sid, schema, LOG_SHEET, result["updates"], now, existing=log_rows)
    if drop:
        delete_rows(svc, sid, drop)
        existing = [row for row in existing if row not in drop]
    if result["feedback"]:
        bt.upsert_rows(svc, sid, schema, SHEET, result["feedback"], now, existing=existing)
    bt.refresh_progress(svc, sid, schema, now)
    log("已写表并重算动作进度")
    return 0


def delete_rows(svc, sid: str, rows: list[dict]) -> None:
    numbers = []
    for row in rows:
        n = row.get("_row")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise PullError("邮件反馈行缺少行号，不写表")
        numbers.append(n)
    meta = svc.spreadsheets().get(
        spreadsheetId=sid, fields="sheets(properties(sheetId,title))"
    ).execute(num_retries=bt.RETRIES)
    props = next((s["properties"] for s in meta.get("sheets", []) if s["properties"]["title"] == SHEET), None)
    if not props:
        raise PullError("底表里没有邮件反馈页")
    requests = [{
        "deleteDimension": {
            "range": {"sheetId": props["sheetId"], "dimension": "ROWS", "startIndex": n - 1, "endIndex": n}
        }
    } for n in sorted(set(numbers), reverse=True)]
    svc.spreadsheets().batchUpdate(spreadsheetId=sid, body={"requests": requests}).execute(num_retries=bt.RETRIES)


def selftest() -> int:
    sent = Header(
        uid="1", message_id="<out@example.test>", day="2026-10-20", subject="hello",
        from_addr="chester@de-linker.com", recipients={"buyer@customer.test"},
    )
    other = Header(
        uid="2", message_id="<other@example.test>", day="2026-10-20",
        recipients={"buyer@customer.test"},
    )
    reminder = Header(
        uid="3", message_id="<n@de-linker-playbook.local>", day="2026-10-20",
        subject="de-linker 下一步", recipients={"chester@de-linker.com"},
    )
    reply = Header(
        uid="4", message_id="<reply@customer.test>", day="2026-10-21",
        from_addr="buyer@customer.test", reply_ids={"<out@example.test>"},
    )
    auto = Header(
        uid="5", message_id="<auto@customer.test>", day="2026-10-21",
        reply_ids={"<out@example.test>"}, auto_submitted="auto-replied",
    )
    bounce = Header(
        uid="6", message_id="<bounce@mx.test>", day="2026-10-21",
        from_addr="mailer-daemon@mx.test", subject="Undelivered Mail",
    )
    row = {
        "登记编号": "E-20261020-01", "渠道": "邮件", "动作": "发出首封", "执行日期": "2026-10-20",
        "收件公司": "Customer", "查证结果": "待邮箱接入后查证",
    }
    addresses = lambda _row: {"buyer@customer.test"}  # noqa: E731
    no_bounce = lambda _msg: ("", set())  # noqa: E731
    quote = lambda _msg: "要报价、规格、价格或样品"  # noqa: E731

    assert is_reminder(reminder)
    assert pick_sent([("INBOX", ("\\Inbox",)), ("已发送", ("\\Sent",))]) == "已发送"
    assert pick_sent([("Sent Items", ())]) == "Sent Items"
    assert choose_sent([("Sent Messages", ()), ("INBOX", ())], lambda name: 3 if name == "已发送" else 0) == "已发送"
    one, evidence = match_sent(row, [sent, reminder], {"buyer@customer.test"})
    assert one is sent and evidence == FOUND
    assert match_sent(row, [sent, other], {"buyer@customer.test"})[1] == MANY
    assert match_sent(row, [], set())[1] == NO_ADDRESS
    assert bounce_event("5.1.1") == "永久退信"
    assert bounce_event("5.2.2") == "暂时退信"
    assert bounce_event("4.2.1") == "暂时退信"
    assert bounce_event("5.7.26") == "认证或信誉拒收"
    assert classify_reply("Please unsubscribe me") == "拒绝或退订"
    assert classify_reply("Can you send a quote?") == "要报价、规格、价格或样品"
    assert "@" not in FOUND and "@" not in MISS

    planned = plan([row], [sent, reminder], [reply, auto], addresses, no_bounce, quote)
    assert planned["found"] == 1
    kinds = {item["事件类型"] for item in planned["feedback"]}
    assert kinds == {"未见退信（推断已送达）", "自动回复", "真人回复"}
    human = next(item for item in planned["feedback"] if item["事件类型"] == "真人回复")
    assert human["回复分类"] == "要报价、规格、价格或样品"
    assert human["反馈级别"] == "L2"
    assert "buyer@customer.test" not in str(planned)

    bounced = plan([row], [sent], [bounce], addresses, lambda _msg: ("5.1.1", {"<out@example.test>"}), quote)
    assert {item["事件类型"] for item in bounced["feedback"]} == {"永久退信"}
    assert bounced["feedback"][0]["退信状态码"] == "5.1.1"
    old = {"登记编号": "E-20261020-01", "事件类型": "未见退信（推断已送达）", "_row": 4}
    assert contradictory([old], bounced["feedback"]) == [old]

    print("selftest ok")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--dry-run", action="store_true")
    sub.add_parser("selftest")
    args = ap.parse_args()
    try:
        if args.command == "selftest":
            raise SystemExit(selftest())
        raise SystemExit(apply(args.dry_run))
    except PullError as exc:
        log(f"出错，没跑完：{exc}")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
