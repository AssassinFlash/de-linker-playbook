# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "openpyxl>=3.1",
# ]
# ///
"""
每日提醒：GSC 与询盘回流写完后，按 docs/feedback-rules.md 算出当天的「下一步」，同时送到 Mac「提醒事项」
（列表「de-linker 下一步」）和操作者的邮箱。规格见 docs/feedback-rules.md 第 12 节，用法见
docs/daily-reminder.md。

  uv run scripts/daily_reminder.py run                    算一次并送出（每天由 08:30 的定时任务在回流后调用）
  uv run scripts/daily_reminder.py run --pull-exit 1      告诉它今天的回流失败了（标题写「今天取数出错」）
  uv run scripts/daily_reminder.py run --test             标题加「测试」
  uv run scripts/daily_reminder.py run --dry-run          只打印标题和正文，不送

不需要单独装定时：`uv run scripts/gsc_pull.py schedule install` 装的那个每日任务，回流跑完就接着跑本脚本
（回流失败也跑）。哪一路没送到（提醒事项或邮件），写进日志、退出码非 0，另一路照样送。

配置在仓外 ~/.config/de-linker-playbook/config.toml 的 [reminder] 段：
  to = ["...", "..."]           收件人（日常账号 + 工作邮箱）
  smtp_host / smtp_port / smtp_user
  smtp_password_file = "..."    QQ 邮箱授权码所在的文件（权限 600，操作者自己写入）
"""
from __future__ import annotations

import argparse
import os
import smtplib
import ssl
import subprocess
import sys
import tomllib
from datetime import datetime, timedelta
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path

sys.dont_write_bytecode = True  # keep scripts/__pycache__ out of the repo
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402
import next_step as ns  # noqa: E402

LIST_NAME = "de-linker 下一步"
MARK = "（每日提醒自动生成）"
TEST_MARK = "（每日提醒测试）"   # test runs only tick off earlier tests, never the real reminder
SAY_NEXT_AGAIN = "开个对话，跟 AI 说「下一步」，AI 会再算一次，并查是什么原因。"

# Reminders: complete the earlier automatic reminder (its notes carry the marker passed in), then add today's.
APPLESCRIPT = f'''
on run argv
	set t to item 1 of argv
	set b to item 2 of argv
	set mk to item 3 of argv
	tell application "Reminders"
		if not (exists list "{LIST_NAME}") then make new list with properties {{name:"{LIST_NAME}"}}
		set L to list "{LIST_NAME}"
		repeat with r in (reminders of L whose completed is false)
			set nb to body of r
			if nb is not missing value then
				if nb contains mk then set completed of r to true
			end if
		end repeat
		tell L to make new reminder with properties {{name:t, body:b, remind me date:((current date) + 60)}}
	end tell
end run
'''


def log(msg: str) -> None:
    print(f"[{bt.stamp(bt.beijing_now())}] 每日提醒：{msg}", flush=True)


def pull_failed(exit_code: int | None) -> bool:
    return bool(exit_code)


def compose(now: str, pull_exit: int | None, test: bool) -> tuple[str, str, bool]:
    """(title, body, computed) in everyday words (operator 2026-10-15: short, no codes, no logs)."""
    since = (datetime.strptime(now, "%Y-%m-%d %H:%M") - timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    try:
        schema = bt.load_schema()
        svc = bt.sheets_service()
        sid = bt.load_target("main")
        data = {name: bt.read_table(svc, sid, schema, name) for name in schema["x-sheet-order"]}
        text = ns.render_plain(ns.next_step(data, now, since, live=True))
        title, _, body = text.partition("\n\n")   # the title line is the reminder/mail title; not repeated in the body
        computed = True
    except Exception as e:  # details go to the log; the operator gets one plain sentence
        log(f"算下一步出错：{type(e).__name__}: {e}")
        title = "今天没算出下一步"
        body = "今天早上算的时候出了问题（多半是网络或表格连不上）。" + SAY_NEXT_AGAIN
        computed = False
    if pull_failed(pull_exit):
        title = f"今天取数没成功｜{title}"
        body = ("今天早上 GSC 或询盘取数没成功，下面是按上次取到的数据算的。原因 AI 下次对话时会查，你不用管。\n\n"
                + body)
    if test:
        title = f"【测试】{title}"
    body += f"\n\n{TEST_MARK if test else MARK} {now}"
    return title, body, computed


def to_reminders(title: str, body: str, test: bool) -> None:
    r = subprocess.run(["/usr/bin/osascript", "-", title, body, TEST_MARK if test else MARK],
                       input=APPLESCRIPT, text=True, capture_output=True, timeout=120)
    if r.returncode:
        raise RuntimeError((r.stderr or r.stdout).strip())


def to_mail(title: str, body: str, day: str) -> list[str]:
    path = Path(os.environ.get("PLAYBOOK_CONFIG", bt.CONFIG_DIR / "config.toml"))
    cfg = tomllib.loads(path.read_text(encoding="utf-8"))["reminder"]
    to = cfg["to"] if isinstance(cfg["to"], list) else [cfg["to"]]
    pw = Path(os.path.expanduser(cfg["smtp_password_file"])).read_text(encoding="utf-8").strip()
    m = EmailMessage()
    test = title.startswith("【测试】")
    core = title.removeprefix("【测试】").replace("下一步：", "", 1)
    m["Subject"] = ("【测试】" if test else "") + f"de-linker 下一步 · {day}：{core}"
    m["From"] = cfg["smtp_user"]
    m["To"] = ", ".join(to)
    m["Date"] = formatdate(localtime=True)
    m["Message-ID"] = make_msgid(domain="de-linker-playbook.local")
    m.set_content(body)
    with smtplib.SMTP_SSL(cfg["smtp_host"], int(cfg["smtp_port"]), context=ssl.create_default_context(),
                          timeout=60) as s:
        s.login(cfg["smtp_user"], pw)
        refused = s.send_message(m)
    return [a for a in to if a not in refused]


def run(args) -> int:
    now = args.now or bt.stamp(bt.beijing_now())
    title, body, computed = compose(now, args.pull_exit, args.test)
    if args.dry_run:
        print(title + "\n\n" + body)
        return 0
    failed = [] if computed else ["算下一步"]
    try:
        to_reminders(title, body, args.test)
        log(f"提醒事项：已建「{title}」")
    except Exception as e:
        failed.append("提醒事项")
        log(f"提醒事项：没建成（{type(e).__name__}: {e}）")
    try:
        got = to_mail(title, body, now[:10])
        log(f"邮件：已发出，收件 {len(got)} 个地址")
    except Exception as e:
        failed.append("邮件")
        log(f"邮件：没发出（{type(e).__name__}: {e}）")
    log("结束，" + ("无错误" if not failed else "有问题：" + "、".join(failed)))
    return 1 if failed else 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("run")
    p.add_argument("--pull-exit", type=int, help="今天回流任务的聚合退出码；非 0 时标题写「今天取数出错」")
    p.add_argument("--now", help="北京时间「年-月-日 时:分」，默认现在")
    p.add_argument("--test", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    sys.exit(run(args))


if __name__ == "__main__":
    main()
