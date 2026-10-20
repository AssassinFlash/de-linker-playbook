# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "openpyxl>=3.1",
# ]
# ///
"""
GSC 数据回流：把 Google Search Console 的收录检查和搜索数据写进底表。

  uv run scripts/gsc_pull.py run                 跑一次：网页收录、网页表现、搜索词，再重算动作进度
  uv run scripts/gsc_pull.py run --dry-run       只取数、打印条数，不写表
  uv run scripts/gsc_pull.py schedule install    在这台 Mac 上装每日定时（launchd，每天 08:30 北京时间）；
                                                 同一条任务先跑本脚本，再跑询盘回流，然后发每日提醒
  uv run scripts/gsc_pull.py schedule status     看定时装没装、上次退出码、日志最后几行
  uv run scripts/gsc_pull.py schedule remove     卸掉定时

写什么：
  网页收录  执行登记里的网址（含旧网址）在前，站点地图里的网址在后，每个网址每天检查一次；
           当天已有那一行就不再查（重跑不耗配额）。每天最多查 --max-inspections 个（默认 1900，
           官方上限每站每天 2000）。
  网页表现  最近 --days 天（默认 10，按太平洋时间），每种搜索类型 × 网址 × 国家 × 设备一行；
           Discover 不给设备，设备写「不区分」。
  搜索词    同上再细分到搜索词（Discover、Google 新闻不给搜索词）。
  两张表都按不重复键覆盖：最近几天的「初步」数会在之后的运行里被「定稿」数覆盖，不会重复。

凭据、表格 ID 的读取方式同 scripts/base_table.py。日志：定时运行写到
~/Library/Logs/de-linker-playbook/gsc-pull.log。任何一步出错，退出码非 0，并在日志里写明。
"""
from __future__ import annotations

import argparse
from xml.sax.saxutils import escape
import os
import re
import subprocess
import sys
import time
import traceback
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True  # keep scripts/__pycache__ out of the repo
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402

SITE = "https://de-linker.com/"
SITEMAP = "https://de-linker.com/sitemaps.xml"
GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
PACIFIC = ZoneInfo("America/Los_Angeles")
SEARCH_TYPES = ["web", "image", "video", "news", "discover", "googleNews"]
NO_DEVICE_TYPES = {"discover"}   # API: "Requests for Discover cannot be grouped by device"
NO_QUERY_TYPES = {"discover", "googleNews"}  # API: "cannot be grouped by query"
INSPECT_GAP = 0.11               # seconds between inspections, keeps under 600/min

LABEL = "com.de-linker-playbook.gsc-pull"
PLIST = Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
LOG = Path.home() / "Library" / "Logs" / "de-linker-playbook" / "gsc-pull.log"
RUN_AT = (8, 30)                 # hour, minute, local time of this Mac


def log(msg: str) -> None:
    print(f"[{bt.stamp(bt.beijing_now())}] {msg}", flush=True)


# ---------------------------------------------------------------- which URLs


def sitemap_urls() -> list[str]:
    def locs(url: str) -> list[str]:
        req = urllib.request.Request(url, headers={"User-Agent": "de-linker-playbook gsc_pull"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return re.findall(r"<loc>\s*(.*?)\s*</loc>", resp.read().decode("utf-8"))

    urls: list[str] = []
    for sub in locs(SITEMAP):
        urls += locs(sub) if sub.endswith(".xml") else [sub]
    return list(dict.fromkeys(urls))


def urls_to_inspect(log_rows: list[dict]) -> list[str]:
    registered = [u for r in sorted(log_rows, key=lambda r: r["登记编号"], reverse=True)
                  for u in (r.get("网址"), r.get("旧网址")) if u and u.startswith(SITE)]
    return list(dict.fromkeys(registered + sitemap_urls()))


# ---------------------------------------------------------------- URL Inspection


def beijing_minute(iso: str | None) -> str | None:
    if not iso:
        return None
    t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return bt.stamp(t)


def inspection_row(schema: dict, url: str, day: str, res: dict, log_rows: list[dict]) -> dict:
    st = res.get("indexStatusResult", {})

    def given(key: str) -> str | None:  # *_UNSPECIFIED = Google gave nothing (usually: not crawled yet)
        v = st.get(key)
        return None if not v or v.endswith("_UNSPECIFIED") else v

    raw = {
        "检查日期": day, "网址": url, "登记编号": bt.latest_registration(log_rows, url, day) or None,
        "语言": bt.language(url),
        "上次抓取时间（北京时间）": beijing_minute(st.get("lastCrawlTime")),
        "Google 选的正式地址": st.get("googleCanonical"), "页面声明的正式地址": st.get("userCanonical"),
        "_coverage": st.get("coverageState") or "(Google 没给 coverageState)",
        "_robots": given("robotsTxtState"), "_indexing": given("indexingState"), "_fetch": given("pageFetchState"),
    }
    return bt.translate_inspection(schema, raw)


def pull_inspections(gsc, schema: dict, existing: list[dict], log_rows: list[dict], day: str,
                     limit: int) -> tuple[list[dict], list[str]]:
    done = {r["网址"] for r in existing if r["检查日期"] == day}
    todo = [u for u in urls_to_inspect(log_rows) if u not in done]
    skipped = max(0, len(todo) - limit)
    todo = todo[:limit]
    log(f"网页收录：今天已查 {len(done)} 个，待查 {len(todo)} 个" + (f"，超出每日上限未查 {skipped} 个" if skipped else ""))
    rows, errors = [], []
    for u in todo:
        try:
            res = gsc.urlInspection().index().inspect(
                body={"inspectionUrl": u, "siteUrl": SITE, "languageCode": "en-US"}).execute(num_retries=bt.RETRIES)
            rows.append(inspection_row(schema, u, day, res["inspectionResult"], log_rows))
        except Exception as e:  # keep going; one bad URL must not lose the rest
            errors.append(f"网页收录 {u}: {e}")
        time.sleep(INSPECT_GAP)
    # 和上次比 needs the history of each URL
    history = [r for r in existing if r["网址"] in {x["网址"] for x in rows}]
    bt.compare_with_previous(history + rows)
    return rows, errors


# ---------------------------------------------------------------- Search Analytics


def query_all(gsc, body: dict) -> tuple[list[dict], str | None]:
    rows, start = [], 0
    meta = None
    while True:
        resp = gsc.searchanalytics().query(siteUrl=SITE, body={**body, "rowLimit": 25000, "startRow": start}) \
            .execute(num_retries=bt.RETRIES)
        meta = meta or resp.get("metadata")
        got = resp.get("rows", [])
        rows += got
        if len(got) < 25000:
            break
        start += len(got)
    return rows, (meta or {}).get("firstIncompleteDate")


def pull_search(gsc, schema: dict, sheet: str, start: str, end: str, log_rows: list[dict]) -> tuple[list[dict], list[str]]:
    with_query = sheet == "搜索词"
    out, errors = [], []
    for t in SEARCH_TYPES:
        if with_query and t in NO_QUERY_TYPES:
            continue
        dims = ["date", "page"] + (["query"] if with_query else []) + ["country"] \
            + ([] if t in NO_DEVICE_TYPES else ["device"])
        try:
            rows, incomplete = query_all(gsc, {"startDate": start, "endDate": end, "dimensions": dims,
                                               "type": t, "dataState": "all"})
        except Exception as e:
            errors.append(f"{sheet} {t}: {e}")
            continue
        for r in rows:
            k = dict(zip(dims, r["keys"]))
            day, url = k["date"], k["page"]
            raw = {
                "日期（太平洋时间）": day, "网址": url,
                "登记编号": bt.latest_registration(log_rows, url, day) or None, "语言": bt.language(url),
                "_type": t, "_country": k["country"], "_device": k.get("device"),
                "展示": int(r["impressions"]), "点击": int(r["clicks"]),
                "平均排名": round(r["position"], 1),
                "数据状态": "初步" if incomplete and day >= incomplete else "定稿",
            }
            if with_query:
                raw["搜索词"] = k["query"]
            out.append(bt.translate_search_row(schema, sheet, raw))
    return out, errors


# ---------------------------------------------------------------- run


def run(days: int, limit: int, dry: bool) -> int:
    schema = bt.load_schema()
    sid = bt.load_target("main")
    sheets = bt.sheets_service()
    gsc = bt.google_service("searchconsole", "v1", GSC_SCOPES)
    now_t = bt.beijing_now()
    now, today = bt.stamp(now_t), now_t.date().isoformat()
    log(f"开始（{'试跑，不写表' if dry else '写正式底表'}）")

    log_rows = bt.read_table(sheets, sid, schema, "执行登记")
    existing_idx = bt.read_table(sheets, sid, schema, "网页收录")
    errors: list[str] = []

    idx_rows, errs = pull_inspections(gsc, schema, existing_idx, log_rows, today, limit)
    errors += errs

    end = datetime.now(PACIFIC).date()
    start = (end - timedelta(days=days - 1)).isoformat()
    perf_rows, errs = pull_search(gsc, schema, "网页表现", start, end.isoformat(), log_rows)
    errors += errs
    query_rows, errs = pull_search(gsc, schema, "搜索词", start, end.isoformat(), log_rows)
    errors += errs
    log(f"取到：网页收录 {len(idx_rows)} 行；网页表现 {len(perf_rows)} 行、搜索词 {len(query_rows)} 行"
        f"（太平洋时间 {start} 至 {end.isoformat()}）")

    if not dry:
        for sheet, rows, existing in (("网页收录", idx_rows, existing_idx), ("网页表现", perf_rows, None),
                                      ("搜索词", query_rows, None)):
            added, updated = bt.upsert_rows(sheets, sid, schema, sheet, rows, now, existing=existing)
            log(f"写入 {sheet}：新增 {added} 行，覆盖 {updated} 行")
        n = bt.refresh_progress(sheets, sid, schema, now)
        log(f"动作进度：重算 {n} 行")

    for e in errors:
        log(f"出错 {e}")
    log(f"结束，{'有 ' + str(len(errors)) + ' 处出错' if errors else '无错误'}")
    return 1 if errors else 0


# ---------------------------------------------------------------- schedule (launchd)


def plist_text() -> str:
    uv = subprocess.run(["/usr/bin/which", "uv"], capture_output=True, text=True).stdout.strip() \
        or "/opt/homebrew/bin/uv"
    script = Path(__file__).resolve()
    reminder = script.with_name("daily_reminder.py")
    inquiry = script.with_name("inquiry_pull.py")
    env_path = f"{Path(uv).parent}:/usr/local/bin:/usr/bin:/bin"
    # GSC, then inquiry, then the daily reminder. The reminder runs even if a pull
    # failed; --pull-exit is 1 when either pull failed. Exit non-zero if any failed.
    # Label and 08:30 are unchanged.
    chain = (
        f"'{uv}' run --quiet '{script}' run; g=$?; "
        f"'{uv}' run --quiet '{inquiry}' run; i=$?; "
        f"'{uv}' run --quiet '{reminder}' run --pull-exit $(( (g != 0 || i != 0) ? 1 : 0 )); r=$?; "
        f"[ $g -eq 0 ] && [ $i -eq 0 ] && [ $r -eq 0 ]"
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>{LABEL}</string>
  <key>ProgramArguments</key>
  <array><string>/bin/zsh</string><string>-c</string><string>{escape(chain)}</string></array>
  <key>WorkingDirectory</key><string>{script.parents[1]}</string>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>{env_path}</string></dict>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>{RUN_AT[0]}</integer><key>Minute</key><integer>{RUN_AT[1]}</integer></dict>
  <key>StandardOutPath</key><string>{LOG}</string>
  <key>StandardErrorPath</key><string>{LOG}</string>
</dict>
</plist>
"""


def schedule(action: str) -> int:
    domain = f"gui/{os.getuid()}"
    if action == "install":
        LOG.parent.mkdir(parents=True, exist_ok=True)
        PLIST.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["launchctl", "bootout", f"{domain}/{LABEL}"], capture_output=True)
        PLIST.write_text(plist_text(), encoding="utf-8")
        r = subprocess.run(["launchctl", "bootstrap", domain, str(PLIST)], capture_output=True, text=True)
        print(r.stdout + r.stderr or f"installed {PLIST}; runs daily at {RUN_AT[0]:02d}:{RUN_AT[1]:02d}; log {LOG}")
        return r.returncode
    if action == "remove":
        subprocess.run(["launchctl", "bootout", f"{domain}/{LABEL}"], capture_output=True)
        PLIST.unlink(missing_ok=True)
        print(f"removed {LABEL}")
        return 0
    r = subprocess.run(["launchctl", "print", f"{domain}/{LABEL}"], capture_output=True, text=True)
    if r.returncode:
        print("not installed")
        return 1
    for line in r.stdout.splitlines():
        if any(k in line for k in ("state =", "last exit code", "runs =")):
            print(line.strip())
    if LOG.exists():
        print(f"--- {LOG} (last 15 lines)")
        print("\n".join(LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-15:]))
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("run")
    p.add_argument("--days", type=int, default=10)
    p.add_argument("--max-inspections", type=int, default=1900)
    p.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("schedule")
    s.add_argument("action", choices=["install", "status", "remove"])
    args = ap.parse_args()
    if args.command == "run":
        try:
            sys.exit(run(args.days, args.max_inspections, args.dry_run))
        except Exception as e:  # traceback for debugging, then one plain line that the daily reminder quotes last
            traceback.print_exc()
            log(f"出错，没跑完：{type(e).__name__}: {e}")
            sys.exit(1)
    sys.exit(schedule(args.action))


if __name__ == "__main__":
    main()
