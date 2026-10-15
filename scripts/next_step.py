# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "openpyxl>=3.1",
# ]
# ///
"""
下一步：读底表，按 docs/feedback-rules.md 逐条对规则，排优先级，输出第 11 节格式的「下一步」。

  uv run scripts/next_step.py                          读正式底表，打印「下一步」（markdown）
  uv run scripts/next_step.py --format json            同上，输出 JSON（编排用来判断优先级）
  uv run scripts/next_step.py --target sample --now "2026-10-15 09:00"
                                                       用样例表走一遍（样例网址是假的，不抓线上）
  uv run scripts/next_step.py --offline-sample ...     不连网：用脚本内置的样例数据（同样例表）
  uv run scripts/next_step.py --line 获客 --format json
                                                       只看一条线：执行登记「线」= 获客 的对象（邮件、获客线登记的页），
                                                       以及没归因、两线共有的询盘；没登记过的全站页面算营销
  uv run scripts/next_step.py mark --rule W-13 --url URL [--url URL ...] --note "没查出问题"
                                                       记下 AI 已做完的一次性核查（W-13 记在网页收录，
                                                       W-24 用 --id 记在执行登记），之后不再排队
  uv run scripts/next_step.py log-request --url URL [--url URL ...]
                                                       操作者说已在 GSC 请求编入索引后，AI 登记进执行登记
                                                       （编号、认重复同 scripts/execution_log.py；其他动作用那个脚本）

两条编排（营销、获客）和每日提醒都调用本脚本，不另写规则；编排各带 --line，每日提醒不带（两线合看）。脚本只做机械的部分：对规则、排优先级、
阻断类网页规则（W-01 至 W-08）先抓线上现状。起草回信、改页面、找询盘归因证据由 AI 在会话里做。
凭据、表格 ID 的读取方式同 scripts/base_table.py。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
import urllib.robotparser
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urljoin, urlsplit

sys.dont_write_bytecode = True  # keep scripts/__pycache__ out of the repo
sys.path.insert(0, str(Path(__file__).resolve().parent))
import base_table as bt  # noqa: E402
import execution_log as el  # noqa: E402

RULES_DOC = "docs/feedback-rules.md"
GSC_HOME = "https://search.google.com/search-console"
SITE = "https://de-linker.com/"
UA = "Mozilla/5.0 (compatible; de-linker-playbook next_step; +https://de-linker.com/)"
SHOW = 10                      # objects listed by name in one action; the rest are counted
QUEUE = 5                      # rules §11: queue shows at most 5
INDEXED = ("已收录", "已收录但有问题")
REQUEST_NOTE = "在 GSC 请求编入索引"
W24_ACTIONS = ("新发布页面", "改标题或描述", "改正文")
STOPPING_EVENTS = ("真人回复", "永久退信", "认证或信誉拒收", "改址通知")
LINES = ("营销", "获客")
SITE_LINE = "营销"             # a page nobody registered is the site's, i.e. the marketing line's

REVIEW_DO = ("看 AI 起草的信，哪里不满意直接说（语气、长短、重点、用词都行），AI 改了再给你看，来回几轮都行；"
             "你说「可以了」，再从你的邮箱亲手发出")   # rules §10: drafts go through the operator's review
REVIEW_DECIDE = "哪里要改、改到什么时候算可以了、发不发"

REQUEST_HOWTO = (
    f"打开 Search Console（{GSC_HOME}），左上角选资源 {SITE}；在最上面的搜索框粘贴网址，回车；"
    "点「测试实际网址」（Test live URL），等它说可以编入索引；再点「请求编入索引」（Request indexing）。"
    "每个网址只点一次。也可以跟 AI 说「你来点」，AI 在浏览器里代点（要你的浏览器登录着 GSC）")


@dataclass
class Action:
    rule: str
    priority: int
    title: str
    why: str
    you_do: str = "不用你动手"
    you_decide: str = "不用你决定"
    ai_does: str = "无"
    after: str = ""
    skill: str = ""
    anchor: bool = False
    dropped: bool = False
    kind: int = 2              # 0 someone waiting on mail, 1 inquiry report, 2 everything else
    since: str = "9999-99-99"  # 执行日期 of the anchor (older first)
    objects: list[str] = field(default_factory=list)
    variant: str = ""          # request / fix / look / check …, picks the plain wording
    facts: dict = field(default_factory=dict)  # small facts the plain wording needs (company, crawl dates …)

    def sort_key(self) -> tuple:
        return (self.priority, not self.dropped, not self.anchor, self.kind, self.since, self.rule, self.title)


# ---------------------------------------------------------------- reading


def load(args) -> dict[str, list[dict]]:
    schema = bt.load_schema()
    if args.offline_sample:
        return bt.sample_data(schema)
    svc = bt.sheets_service()
    sid = bt.load_target(args.target)
    return {name: bt.read_table(svc, sid, schema, name) for name in schema["x-sheet-order"]}


def latest_by(rows: list[dict], key: str, day: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in sorted(rows, key=lambda r: r.get(day, "")):
        out[r[key]] = r
    return out


def episode(rows: list[dict]) -> list[dict]:
    """The URL's newest checks that all share the newest 收录状态 (newest first)."""
    rows = sorted(rows, key=lambda r: r["检查日期"], reverse=True)
    run = []
    for r in rows:
        if r["收录状态"] != rows[0]["收录状态"]:
            break
        run.append(r)
    return run


def on_line(row_line: str, line: str | None) -> bool:
    return not line or row_line == line


def marked(rows: list[dict], rule: str) -> bool:
    return any(f"已核（{rule}）" in (r.get("备注") or "") for r in rows)


# ---------------------------------------------------------------- live checks (rules §3「先看线上现状」)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def live_state(url: str) -> dict:
    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with opener.open(req, timeout=30) as resp:
            status, headers, body = resp.status, resp.headers, resp.read(400_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        status, headers, body = e.code, e.headers, ""
    except Exception as e:  # network trouble: report it, the action falls back to「AI 先看线上」
        return {"error": f"{type(e).__name__}: {e}"}
    meta = ""
    for tag in re.findall(r"<meta\b[^>]*>", body, flags=re.I):
        if re.search(r"""name\s*=\s*["']?(robots|googlebot)["'\s>]""", tag, flags=re.I):
            m = re.search(r"""content\s*=\s*["']([^"']*)["']""", tag, flags=re.I)
            meta = ", ".join(x for x in (meta, m.group(1) if m else "") if x)
    canonical = ""
    for tag in re.findall(r"<link\b[^>]*>", body, flags=re.I):
        if re.search(r"""rel\s*=\s*["']?canonical""", tag, flags=re.I):
            m = re.search(r"""href\s*=\s*["']([^"']*)["']""", tag, flags=re.I)
            canonical = urljoin(url, m.group(1)) if m else ""
    return {"status": status, "location": headers.get("Location", ""), "robots_meta": meta,
            "x_robots": headers.get("X-Robots-Tag", ""), "canonical": canonical}


_robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}


def robots_allows(url: str) -> bool | None:
    root = "{0.scheme}://{0.netloc}/robots.txt".format(urlsplit(url))
    if root not in _robots_cache:
        rp = urllib.robotparser.RobotFileParser(root)
        try:
            rp.read()
        except Exception:
            return None
        _robots_cache[root] = rp
    return _robots_cache[root].can_fetch("Googlebot", url)


def live_ok(url: str, live: dict) -> bool:
    if live.get("error") or live.get("status") != 200:
        return False
    if "noindex" in (live["robots_meta"] + live["x_robots"]).lower():
        return False
    if live["canonical"] and live["canonical"].rstrip("/") != url.rstrip("/"):
        return False
    return robots_allows(url) is not False


def describe_live(url: str, live: dict, today: str) -> str:
    if live.get("error"):
        return f"线上 {today} 没抓到（{live['error']}）"
    parts = [f"HTTP {live['status']}"]
    if live["location"]:
        parts.append(f"跳到 {live['location']}")
    parts.append(f"页面 robots 写的是「{live['robots_meta']}」" if live["robots_meta"] else "页面没写 robots（默认允许收录）")
    if live["x_robots"]:
        parts.append(f"响应头 X-Robots-Tag 是「{live['x_robots']}」")
    if live["canonical"]:
        parts.append("正式地址指向自己" if live["canonical"].rstrip("/") == url.rstrip("/")
                     else f"正式地址指向 {live['canonical']}")
    allowed = robots_allows(url)
    if allowed is not None:
        parts.append("robots.txt 放行" if allowed else "robots.txt 挡住")
    return f"线上 {today} 抓取：" + "，".join(parts)


# ---------------------------------------------------------------- web rules (rules §3)

BLOCKING = {  # 收录状态 -> (rule, needs「应被收录」, what is wrong, how to fix when still wrong)
    "服务器错误（5xx）": ("W-01", False, "服务器出错", "修好服务器错误"),
    "跳转出错": ("W-02", False, "跳转出错", "理清跳转链（太长、循环、链里有坏网址）并修好"),
    "被 robots.txt 挡住": ("W-03", True, "被 robots.txt 挡住", "去掉 robots.txt 里挡住它的那条"),
    "被 noindex 挡住": ("W-04", True, "被 noindex 挡住", "去掉页面上的 noindex"),
    "软 404（看起来像空页）": ("W-05", False, "被 Google 当成空页（软 404）",
                         "页面已删就改成真正的 404；页面应该在就补上真实内容"),
    "要求登录（401）": ("W-06", True, "要求登录才能打开", "让不登录也能打开"),
    "禁止访问（403）": ("W-06", True, "禁止访问", "让不登录也能打开"),
    "其他 4xx 错误": ("W-06", True, "返回 4xx 错误", "查清是哪种 4xx 再修"),
    "404 找不到": ("W-07", True, "404 找不到", "恢复这页，或 301 到新地址"),
}
FIX_ELSEWHERE = {  # 收录状态 -> (rule, what to do) — no live check in the rules, AI fixes in the new-site repo
    "被 robots 挡着却仍被收录": ("W-16", "应被收录就在 robots.txt 里放行；不应收录就去掉阻挡、改用 noindex"),
    "已收录但读不到内容": ("W-17", "用网址检查看清 Google 为什么读不到，然后修可读性"),
}
WAIT_STATES = {
    "已抓取、尚未收录": ("W-14", "不重新提交，不因为这个改写正文，只记账"),
    "正确指向正式页的替代页": ("W-15", "不做事"),
    "已收录": ("W-18", "记 L1，只记账"),
    "已收录但有问题": ("W-18", "记 L1，只记账；「有问题」是增强项或体验项，不算未收录"),
}


def web_actions(data: dict, today: str, live: bool, ledger: dict, line: str | None = None) -> list[Action]:
    log = data["执行登记"]
    registered = {u: e for e in sorted(log, key=lambda e: (e["执行日期"], e["登记编号"]))
                  for u in (e.get("网址"), e.get("旧网址")) if u}
    old_urls = {e["旧网址"] for e in log if e.get("旧网址")}
    by_url: dict[str, list[dict]] = {}
    for r in data["网页收录"]:
        by_url.setdefault(r["网址"], []).append(r)
    hits: list[tuple[str, dict]] = []   # (group key, object info)
    for url, rows in sorted(by_url.items()):
        run = episode(rows)
        r = run[0]
        state = r["收录状态"]
        reg = registered.get(url)
        if not on_line(reg["线"] if reg else SITE_LINE, line):
            continue
        anchor = reg is not None
        should_index = not (reg and reg["动作"] == "下线页面")
        info = {"url": url, "row": r, "reg": reg, "anchor": anchor, "start": run[-1]["检查日期"],
                "dropped": r.get("和上次比") == "掉出收录"}
        requested = [e for e in log if e.get("网址") == url and REQUEST_NOTE in (e.get("内容说明") or "")
                     and e["执行日期"] >= info["start"]]
        if state in BLOCKING:
            rule, needs, _, _ = BLOCKING[state]
            if needs and not should_index:
                ledger.setdefault(f"{state}（已下线，不用管）", []).append(url)
                continue
            if requested:
                ledger.setdefault(f"{state}（{requested[-1]['执行日期']} 已请求编入索引，等 Google 重抓）", []).append(url)
                continue
            if not live or state == "软 404（看起来像空页）":
                hits.append((f"{rule}|look|{anchor}", info))
                continue
            info["live"] = live_state(url)
            if info["live"].get("error") or info["live"].get("status", 0) >= 500:
                info["live"] = live_state(url)        # one retry: a network blip must not read as「still broken」
            if info["live"].get("error"):
                hits.append((f"{rule}|look|{anchor}", info))
                continue
            variant = "request" if live_ok(url, info["live"]) else "fix"
            hits.append((f"{rule}|{variant}|{anchor}", info))
        elif state in FIX_ELSEWHERE:
            hits.append((f"{FIX_ELSEWHERE[state][0]}|fix|{anchor}", info))
        elif state == "跳转页（本身不收录）":
            if url in old_urls:
                ledger.setdefault("跳转页（改网址后的旧网址，正常）", []).append(url)
            else:
                hits.append((f"W-08|check|{anchor}", info))
        elif state == "重复页、Google 选了别的网址为正式地址":
            if (r.get("页面声明的正式地址") or "").rstrip("/") == url.rstrip("/"):
                hits.append((f"W-09|fix|{anchor}", info))
            else:
                ledger.setdefault("重复页，页面自己也声明了别的正式页（看正式页那一行）", []).append(url)
        elif state == "Google 还不知道这个网址":
            new_page = reg and reg["动作"] in ("新发布页面", "改网址（旧址 301 跳新址）") and reg.get("网址") == url
            if new_page and not requested:
                hits.append((f"W-11|request|{anchor}", info))
            else:
                key = "Google 还不知道这个网址（已请求过，等 Google 来抓）" if requested \
                    else "Google 还不知道这个网址（站点地图已交，等 Google 来抓）"
                ledger.setdefault(key, []).append(url)
        elif state == "已发现、尚未抓取":
            if marked(run, "W-13"):
                ledger.setdefault("已发现、尚未抓取（AI 已核过，正常等待）", []).append(url)
            else:
                hits.append((f"W-13|check|{anchor}", info))
        elif state == bt.UNKNOWN_STATE:
            hits.append((f"W-19|map|{anchor}", info))
        elif state in WAIT_STATES:
            ledger.setdefault(state, []).append(url)
        else:
            ledger.setdefault(state, []).append(url)
    return [web_action(key, [i for k, i in hits if k == key], today) for key in dict.fromkeys(k for k, _ in hits)]


def url_list(infos: list[dict], extra=None) -> str:
    shown = infos[:SHOW]
    lines = []
    for i in shown:
        bits = [i["url"]]
        if i["anchor"]:
            bits.append(f"登记 {i['reg']['登记编号']}")
        if extra:
            bits.append(extra(i))
        lines.append("    - " + "；".join(b for b in bits if b))
    if len(infos) > SHOW:
        lines.append(f"    - 其余 {len(infos) - SHOW} 个见底表「网页收录」（收录状态 = {infos[0]['row']['收录状态']}）")
    return "\n" + "\n".join(lines)


def web_action(key: str, infos: list[dict], today: str) -> Action:
    rule, variant, anchor = key.split("|")
    anchor = anchor == "True"
    n = len(infos)
    r0 = infos[0]["row"]
    state = r0["收录状态"]
    days = sorted({i["row"]["检查日期"] for i in infos})
    checked = days[-1] if len(days) == 1 else f"{days[0]} 至 {days[-1]}"
    where = "登记过的页" if anchor else "页面"
    pages = f"{n} 个{where}" if n > 1 else ("登记过的页 " if anchor else "") + infos[0]["url"]
    why = f"底表「网页收录」{checked} 的检查：{n} 个网址的收录状态是「{state}」"
    pri_block = 2 if anchor else 3
    common = dict(rule=rule, anchor=anchor, dropped=any(i["dropped"] for i in infos),
                  since=min((i["reg"]["执行日期"] for i in infos if i["reg"]), default="9999-99-99"),
                  objects=[i["url"] for i in infos], variant=variant,
                  facts={"state": state, "crawled": sorted(i["row"]["上次抓取时间（北京时间）"][:10] for i in infos
                                                           if i["row"].get("上次抓取时间（北京时间）"))})
    if rule in ("W-01", "W-02", "W-03", "W-04", "W-05", "W-06", "W-07"):
        _, _, wrong, fix = BLOCKING[state]
        if variant == "request":
            return Action(
                priority=pri_block, **common,
                title=f"在 GSC 给 {pages}各请求编入索引一次" if n > 1 else f"在 GSC 给 {pages} 请求编入索引一次",
                why=why + "，但线上现在已经正常，只是 Google 记的还是旧的抓取。"
                    + url_list(infos, lambda i: describe_live(i["url"], i["live"], today)
                               + (f"；Google 上次抓取 {i['row']['上次抓取时间（北京时间）']}"
                                  if i["row"].get("上次抓取时间（北京时间）") else "")),
                you_do=REQUEST_HOWTO,
                you_decide="不用你决定",
                ai_does="你说「你来点」，AI 就在浏览器里代点；点完 AI 把每个网址登记进执行登记（动作「其他」，内容说明「在 GSC 请求编入索引」）",
                after="告诉 AI「点完了」，AI 登记。之后等 Google 重新抓，底表「网页收录」的状态会变，没有固定时间；登记后这件事不会再排队")
        if variant == "fix":
            return Action(
                priority=pri_block, **common,
                title=f"修 {pages}：{wrong}",
                why=why + "，线上也还不对。" + url_list(infos, lambda i: describe_live(i["url"], i["live"], today)),
                you_do="不用你动手",
                you_decide="AI 在新站仓库改好、开 PR、CI 通过后，你决定上不上",
                ai_does=f"{fix}：在新站仓库按它的 AGENTS.md 走分支、PR、CI；合并上线后，再请求编入索引一次，并登记进执行登记",
                after="上线后 AI 登记；等 Google 重抓，状态会变",
                skill="marketing-seo-audit")
        return Action(  # look: no live check possible here
            priority=pri_block, **common,
            title=f"AI 先看 {pages} 的线上现状：{wrong}",
            why=why + "。脚本没有抓线上，要 AI 先看。" + url_list(infos),
            ai_does="抓线上这个网址，看状态码、robots、X-Robots-Tag、canonical；线上已正常就改为请求编入索引一次，仍不对就修",
            after="AI 看完会说是哪一种",
            skill="marketing-seo-audit")
    if rule in ("W-16", "W-17"):
        return Action(priority=pri_block, **common, title=f"修 {pages}：{state}",
                      why=why + "。" + url_list(infos),
                      you_decide="AI 改好、开 PR 后，你决定上不上",
                      ai_does=FIX_ELSEWHERE[state][1] + "（新站仓库）", after="上线后 AI 登记；等 Google 重抓",
                      skill="marketing-seo-audit")
    if rule == "W-08":
        return Action(priority=3, **common, title=f"AI 核对 {pages} 的跳转是不是有意的",
                      why=why + "，而且执行登记里没有对应的「改网址」。" + url_list(infos),
                      ai_does="看这些网址跳到哪里、为什么跳；是有意的就只记账，错了就在新站仓库修",
                      after="AI 核完告诉你结论；要修的话，上不上由你决定", skill="marketing-seo-audit")
    if rule == "W-09":
        return Action(priority=pri_block, **common,
                      title=f"对齐 {pages} 的正式地址信号" + ("（刚掉出收录）" if common["dropped"] else ""),
                      why=why + "；页面声明自己是正式地址，Google 却选了别的网址。" + url_list(
                          infos, lambda i: f"Google 选的是 {i['row'].get('Google 选的正式地址', '')}；和上次比：{i['row'].get('和上次比', '')}"),
                      you_decide="AI 改好、开 PR 后，你决定上不上",
                      ai_does="对齐 canonical、内链、站点地图、跳转，让它们和 Google 用的一致（新站仓库）",
                      after="上线后 AI 登记；等 Google 重抓", skill="marketing-site-and-schema")
    if rule == "W-11":
        return Action(priority=4, **common,
                      title=f"在 GSC 给新页 {pages} 请求编入索引一次",
                      why=why + "；这是登记过的新页，还没请求过编入索引。" + url_list(infos),
                      you_do=REQUEST_HOWTO,
                      ai_does="你说「你来点」，AI 就代点；点完 AI 登记进执行登记",
                      after="告诉 AI「点完了」，AI 登记。之后只等，不再重复提交")
    if rule == "W-13":
        return Action(priority=4, **common,
                      title=f"AI 核一次 {pages}（已发现、尚未抓取）",
                      why=why + "，还没核过。Google 知道这些网址，但还没来抓。" + url_list(infos),
                      ai_does="逐个看：robots.txt 有没有误挡、站点地图里有没有它、有没有内链指向它、网站响应慢不慢。"
                              "查出问题才修；没问题就用 `uv run scripts/next_step.py mark --rule W-13` 记下「已核」，之后只记账，不反复请求编入索引",
                      after="核完 AI 告诉你结论；要修的话，上不上由你决定",
                      skill="技术问题：marketing-seo-audit；站点地图或内链：marketing-site-and-schema")
    if rule == "W-19":
        return Action(priority=3, **common, title=f"把 {n} 个新的 Google 状态补进对照表",
                      why=why + "，Google 给的英文状态表里还没有。" + url_list(
                          infos, lambda i: f"英文原文：{i['row'].get('Google 状态原文', '')}"),
                      ai_does="查 Google 帮助页，把这个英文状态补进 schema 的 x-map、x-states，重跑回流后再对一次规则",
                      after="不用等你")
    raise ValueError(key)


def title_checks(data: dict, line: str | None = None) -> list[Action]:
    todo = [e for e in data["执行登记"] if on_line(e["线"], line) and e["动作"] in W24_ACTIONS and e["查证结果"] == "已查证"
            and e.get("网址") and "已查（W-24）" not in (e.get("备注") or "")]
    if not todo:
        return []
    lines = "\n" + "\n".join(f"    - {e['登记编号']}（{e['执行日期']}，{e['动作']}）：{e['网址']}" for e in todo)
    return [Action(rule="W-24", priority=4, anchor=True, since=min(e["执行日期"] for e in todo),
                   objects=[e["登记编号"] for e in todo],
                   title=f"AI 查一次 {len(todo)} 个登记过的页的标题和描述" if len(todo) > 1
                   else f"AI 查一次 {todo[0]['网址']} 的标题和描述",
                   why="底表「执行登记」里这些页新发布或改过，已查证上线，还没按 Google 的标题缺陷清单查过：" + lines,
                   ai_does="打开线上页面，对照规则文件 W-24 的清单逐条看标题和 meta description；命中才改命中的那一处（交给 marketing-copy-editing），"
                           "没命中什么都不做；查完用 `uv run scripts/next_step.py mark --rule W-24 --id 登记编号` 记下",
                   you_decide="要改的话，改后的标题和描述先给你看，改到你满意再决定上不上",
                   after="查完 AI 告诉你结论")]


# ---------------------------------------------------------------- mail rules (rules §4)


def mail_actions(data: dict, today: str, ledger: dict, line: str | None = None) -> list[Action]:
    log = [e for e in data["执行登记"] if e["渠道"] == "邮件" and on_line(e["线"], line)]
    if not log:
        return []
    events: dict[str, list[dict]] = {}
    for ev in data["邮件反馈"]:
        events.setdefault(ev["登记编号"], []).append(ev)
    latest = {eid: max(evs, key=lambda r: (r["事件日期"], bt.LEVEL_RANK.get(r.get("反馈级别", "L0"), 0)))
              for eid, evs in events.items()}
    acts: list[Action] = []
    trouble = []
    for e in log:
        ev = latest.get(e["登记编号"])
        if not ev:
            continue
        who, eid, kind, day = e.get("收件公司", ""), e["登记编号"], ev["事件类型"], ev["事件日期"]
        why = f"底表「邮件反馈」{day}：{who}（登记 {eid}）的最新事件是「{kind}」"
        code = ev.get("退信状态码") or ""
        common = dict(anchor=True, since=e["执行日期"], objects=[eid], facts={"who": who, "code": code})
        if kind == "真人回复":
            cat = ev.get("回复分类") or "其他"
            why += f"，回复分类「{cat}」"
            if cat == "要报价、规格、价格或样品":
                acts.append(Action(rule="M-01", priority=1, kind=0, **common, title=f"回复{who}的报价请求", you_do=REVIEW_DO,
                                   why=why + "。有真人在等我们回。",
                                   you_decide=REVIEW_DECIDE,
                                   ai_does="停掉这条冷序列，按报价路径起草回信（这封回信本身不算询盘），按你的意见改到你满意",
                                   after="发出后跟 AI 说一声，AI 查证并登记进执行登记", skill="lead-service-quotation"))
            elif cat == "提出反对":
                acts.append(Action(rule="M-02", priority=1, kind=0, **common, title=f"回应{who}提出的反对", you_do=REVIEW_DO,
                                   why=why + "。", you_decide=REVIEW_DECIDE,
                                   ai_does="停掉这条冷序列，起草回应反对的回信，按你的意见改到你满意", after="发出后跟 AI 说一声，AI 登记",
                                   skill="lead-service-objection"))
            elif cat == "拒绝或退订":
                acts.append(Action(rule="M-04", priority=2, **common, title=f"停掉给{who}的序列（对方拒绝或退订）",
                                   why=why + "。", ai_does="不再写后续邮件；台账和交付物里把这条序列标为已停",
                                   after="不用等什么"))
            else:
                acts.append(Action(rule="M-03", priority=1, kind=0, **common, title=f"回复{who}的来信",
                                   why=why + "。这封信要人来回。", you_do="读这封回信，回复对方",
                                   you_decide="回不回、怎么回由你定；需要的话让 AI 起草",
                                   ai_does="停掉这条冷序列，记 L2；你要的话起草回信", after="发出后跟 AI 说一声，AI 登记"))
        elif kind == "永久退信" and not code.endswith(".2.2"):
            acts.append(Action(rule="M-05", priority=2, **common, title=f"停用{who}的这个邮箱地址（永久退信 {code}）",
                               why=why + f"，退信状态码 {code}。原样重发没有用。",
                               you_decide="要不要为同一个人另找公开邮箱",
                               ai_does="停用这个地址；你说要找，AI 只找公开邮箱，找到后先核对再给你，找不到不编",
                               after="不用等什么", skill="找：lead-contact-discovery；发前核对：lead-data-validation"))
        elif kind in ("暂时退信", "永久退信"):
            trouble.append(who)
            ledger.setdefault("邮件暂时退信（服务器会自己重试，一般至少 4–5 天，到时按最终结果再看）", []).append(f"{who}（{eid}）")
        elif kind == "认证或信誉拒收":
            trouble.append(who)
            acts.append(Action(rule="M-07", priority=2, **common, title=f"查清发信域名为什么被{who}的邮件服务器拒收",
                               why=why + f"，状态码 {code}。问题在发信域名的 SPF、DKIM、DMARC 或发信 IP，不在文案。",
                               ai_does="查发信域名公开的 DNS 记录，写清缺什么；改 DNS 需要有域名管理权限的人",
                               after="AI 查完告诉你缺什么"))
        elif kind == "改址通知":
            acts.append(Action(rule="M-09", priority=3, **common, title=f"停用{who}的旧地址",
                               why=why + "。", ai_does="停用旧地址；通知里给了新地址就先核对再交给你，没给就只停",
                               after="不用等什么", skill="lead-data-validation"))
        elif kind == "自动回复":
            ledger.setdefault("自动回复（不算回复，照原计划走）", []).append(f"{who}（{eid}）")
    if len(set(trouble)) > 1:
        acts.append(Action(rule="M-08", priority=2, anchor=True, objects=sorted(set(trouble)),
                           title="先少发几封：不止一家收件公司接连退信或拒收",
                           why=f"底表「邮件反馈」：{'、'.join(sorted(set(trouble)))} 都出现了暂时退信或拒收。",
                           you_do="接下来几天少发几封，等错误变少再慢慢加回", after="AI 每天看退信有没有变少"))
    acts += sequence_actions(log, latest, today, ledger)
    return acts


def sequence_actions(log: list[dict], latest: dict, today: str, ledger: dict) -> list[Action]:
    seqs: dict[str, list[dict]] = {}
    for e in log:
        seqs.setdefault(e.get("外展序列") or e["登记编号"], []).append(e)
    acts = []
    for seq, rows in seqs.items():
        if any(latest.get(e["登记编号"], {}).get("事件类型") in STOPPING_EVENTS for e in rows):
            continue
        last = max(rows, key=lambda e: (e.get("第几封") or 0, e["执行日期"]))
        who = last.get("收件公司", "")
        if last["查证结果"] == "待邮箱接入后查证" and not any(e["登记编号"] in latest for e in rows):
            ledger.setdefault("等「邮箱 IMAP 回流」接上再查证", []).append(f"{who}（{last['登记编号']}）")
            continue
        n, plan, nxt = last.get("第几封"), last.get("计划共几封"), last.get("下一封计划日期")
        if n and plan and n >= plan:
            ledger.setdefault("序列计划封数已发完、没有回复（停，记账）", []).append(f"{who}（{seq}）")
        elif nxt and n and plan and nxt <= today:
            acts.append(Action(rule="M-11", priority=2, anchor=True, since=last["执行日期"], objects=[last["登记编号"]],
                               facts={"who": who, "n": int(n) + 1},
                               title=f"给{who}发计划内的第 {int(n) + 1} 封", you_do=REVIEW_DO,
                               why=f"底表「执行登记」{last['登记编号']}：序列 {seq} 已发第 {int(n)} 封，计划共 {int(plan)} 封，"
                                   f"下一封计划日期 {nxt} 已到；没有回复、没有退信。",
                               you_decide=REVIEW_DECIDE,
                               ai_does="下一封文案还没写就先补上；都写好了只差顺序就排好；给你看过、按你的意见改到你满意",
                               after="发出后跟 AI 说一声，AI 查证并登记",
                               skill="文案没写：lead-followup-sequence；只差顺序：lead-email-sequence-strategy"))
        elif nxt and nxt > today:
            ledger.setdefault("序列在等下一封的日期", []).append(f"{who}（{nxt}）")
        else:
            ledger.setdefault("序列没写计划封数和下一封日期（不代定，只记账）", []).append(f"{who}（{seq}）")
    return acts


# ---------------------------------------------------------------- inquiry & log rules (rules §5, §6)


def inquiry_actions(data: dict, since: str, ledger: dict, line: str | None = None) -> list[Action]:
    rows = data["询盘"]
    if not rows:
        return []   # said once under「在等的」
    line_of = {e["登记编号"]: e["线"] for e in data["执行登记"]}
    # an attributed inquiry belongs to its action's line; an unattributed one to both (north star is shared)
    new = [r for r in rows if (r.get("写入时刻（北京时间）") or "") > since
           and (not r.get("归因登记编号") or on_line(line_of.get(r["归因登记编号"], ""), line))]
    acts = []
    if new:
        lines = "\n" + "\n".join(
            f"    - 询盘 {r['询盘内部编号']}：{r.get('公司', '')}，{r.get('创建时刻（北京时间）', '')} 创建，状态「{r['状态']}」，"
            + (f"归因到 {r['归因登记编号']}" if r.get("归因登记编号") else "未归因") for r in new)
        acts.append(Action(rule="Q-01", priority=1, kind=1, objects=[str(r["询盘内部编号"]) for r in new], variant="report",
                           facts={"companies": [r.get("公司", "") for r in new]},
                           title=f"报告 {len(new)} 条新询盘",
                           why=f"底表「询盘」{since} 之后写进来的新行：" + lines,
                           you_do="询盘本身照现有流程处理（每日摘要会发到团队邮箱），这里只是告诉你",
                           after="不用等什么"))
        loose = [r for r in new if not r.get("归因登记编号")]
        if loose:
            acts.append(Action(rule="Q-01", priority=4, objects=[str(r["询盘内部编号"]) for r in loose], variant="attribute",
                               title=f"AI 给 {len(loose)} 条未归因的新询盘找归因证据",
                               why="底表「询盘」：" + "、".join(str(r["询盘内部编号"]) for r in loose) + " 还没有「归因登记编号」。",
                               ai_does="找证据（同一公司的回信、带 UTM 的链接……）把它挂到某次执行登记上；有证据才填编号和依据，没有就留空",
                               after="没有证据就一直留空，照样计入询盘总数"))
    total = len(rows)
    ledger.setdefault(f"询盘总数 {total} 条（北极星）；按动作归因的只记账，0–9 条不改页、不改序列", []).append("—")
    return acts


def log_actions(data: dict, ledger: dict, line: str | None = None) -> list[Action]:
    acts = []
    seen = {r["网址"] for r in data["网页收录"]}
    for e in data["执行登记"]:
        if not on_line(e["线"], line):
            continue
        if e["查证结果"] == "查证失败":
            acts.append(Action(rule="E-01", priority=2, anchor=True, since=e["执行日期"], objects=[e["登记编号"]],
                               title=f"弄清登记 {e['登记编号']} 为什么查证失败",
                               why=f"底表「执行登记」{e['登记编号']}（{e['执行日期']}，{e['动作']}）：查证结果是「查证失败」。"
                                   f"查证证据：{e.get('查证证据', '')}",
                               you_do="回答 AI 一句：链接是不是给错了，还是还没真正上线",
                               ai_does="按你的回答再查一次；弄清以前这一行不算 L0",
                               after="AI 再查一次后更新这一行"))
        elif e["查证结果"] == "未查证（无法公开访问）" and e["渠道"] in ("LinkedIn", "其他平台"):
            ledger.setdefault("非 Google 渠道的登记（反馈还没接进底表）", []).append(e["登记编号"])
        elif e["渠道"] == "网站" and e.get("网址") and e["网址"] not in seen:
            ledger.setdefault("登记过、还没有收录检查（等下一次 08:30 回流）", []).append(e["登记编号"])
    return acts


# ---------------------------------------------------------------- assemble & render


def data_dates(data: dict, line: str | None = None) -> str:
    def newest(sheet: str, col: str) -> str:
        days = [str(r.get(col, ""))[:10] for r in data[sheet] if r.get(col)]
        return max(days) if days else "还没有数"
    return ("底表数据：网页收录最新检查 " + newest("网页收录", "检查日期")
            + "；网页表现最新 " + newest("网页表现", "日期（太平洋时间）")
            + "；邮件反馈最新 " + newest("邮件反馈", "事件日期")
            + "；询盘最新 " + newest("询盘", "创建时刻（北京时间）")
            + "；执行登记 " + (f"{len(data['执行登记'])} 条" if not line else
                               f"{line}线 {sum(e['线'] == line for e in data['执行登记'])} 条（全表 {len(data['执行登记'])} 条）"))


def waiting_notes(data: dict, line: str | None = None) -> list[str]:
    notes = []
    if line == "获客" and not any(e["线"] == "获客" for e in data["执行登记"]):
        notes.append("执行登记里还没有获客线的登记：还没发过外展邮件，邮件规则（M-01 至 M-15）没有对象；"
                     "外展文案出来、操作者发出后登记，第二天起才有可对的")
    if not data["网页表现"] and line != "获客":
        notes.append("网页表现、搜索词还没有数：GSC 一般晚 2–3 天出数")
    if not data["询盘"]:
        notes.append("询盘表还是空的：在等「询盘回流 L3」")
    if not data["邮件反馈"]:
        notes.append("邮件反馈还是空的：在等「邮箱 IMAP 回流」")
    return notes


def next_step(data: dict, now: str, since: str, live: bool, line: str | None = None) -> dict:
    today = now[:10]
    ledger: dict[str, list[str]] = {}
    acts = web_actions(data, today, live, ledger, line) + title_checks(data, line) \
        + mail_actions(data, today, ledger, line) + inquiry_actions(data, since, ledger, line) + log_actions(data, ledger, line)
    acts.sort(key=Action.sort_key)
    return {"generated_at": now, "since": since, "line": line or "全部", "rules": RULES_DOC, "data": data_dates(data, line),
            "actions": [asdict(a) for a in acts],
            "ledger": [{"what": k, "count": len(v) if v != ["—"] else None, "items": v if v != ["—"] else []}
                       for k, v in ledger.items()],
            "waiting": waiting_notes(data, line), "site": site_summary(data, today)}


def site_summary(data: dict, today: str) -> dict:
    latest = latest_by(data["网页收录"], "网址", "检查日期")
    week = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=8)).strftime("%Y-%m-%d")
    perf = [r for r in data["网页表现"] if r["日期（太平洋时间）"] >= week]
    return {"pages": len(latest), "indexed": sum(r["收录状态"] in INDEXED for r in latest.values()),
            "has_perf": bool(data["网页表现"]), "impressions_7d": sum(r.get("展示", 0) for r in perf),
            "clicks_7d": sum(r.get("点击", 0) for r in perf), "inquiries": len(data["询盘"])}


def render(result: dict) -> str:
    acts = result["actions"]
    ledger = "；".join(f"{x['what']} {x['count']} 个" if x["count"] else x["what"] for x in result["ledger"]) or "无"
    out = []
    if acts:
        a = acts[0]
        out += [f"**下一步：{a['title']}**", "",
                f"- **为什么**：{a['why']}（规则 {a['rule']}，P{a['priority']}）",
                f"- **你要做的**：{a['you_do']}",
                f"- **你要决定**：{a['you_decide']}",
                f"- **AI 会做的**：{a['ai_does']}" + (f"（方法 skill：{a['skill']}）" if a["skill"] else ""),
                f"- **做完以后**：{a['after']}", ""]
        rest = acts[1:]
        out.append(f"**还在排队的**（按优先级，共 {len(rest)} 件）：" if rest else "**还在排队的**：没有")
        for i, b in enumerate(rest[:QUEUE], 1):
            out.append(f"{i}. P{b['priority']} {b['title']}（规则 {b['rule']}）")
        if len(rest) > QUEUE:
            out.append(f"…另有 {len(rest) - QUEUE} 件，问 AI「排队的都有什么」可以看全部")
    else:
        out += ["**下一步：今天没有要动的**", "",
                "- **为什么**：底表里所有对象都只命中「只记账」的规则（P5）。",
                "- **你要做的**：不用你动手", "- **你要决定**：不用你决定",
                "- **AI 会做的**：冷启动阶段还没走完的话，接着做阶段工作；否则从方法 skill 里挑下一项新工作",
                "- **做完以后**：明天早上再看一次"]
    out += ["", f"**只在记账的**：{ledger}"]
    if result["waiting"]:
        out.append("**在等的**：" + "；".join(result["waiting"]))
    scope = "" if result.get("line", "全部") == "全部" else f"只看{result['line']}线。"
    out += ["", f"_{scope}{result['data']}。规则：{result['rules']}。生成于 {result['generated_at']}（北京时间）。_"]
    return "\n".join(out)


# ---------------------------------------------------------------- plain wording (daily reminder)
# The operator reads this every morning: everyday words, no rule codes, no P levels, no table names.

THEN = {  # 收录状态 -> what Google saw last time, in everyday words
    "服务器错误（5xx）": "网站出错打不开", "跳转出错": "页面跳转出了问题", "被 robots.txt 挡住": "网站设置挡着不让 Google 看",
    "被 noindex 挡住": "页面上写着「别收录我」", "软 404（看起来像空页）": "页面看起来像空页",
    "要求登录（401）": "页面要登录才能看", "禁止访问（403）": "页面不让外人看", "其他 4xx 错误": "页面打不开",
    "404 找不到": "页面打不开（找不到）",
}
OPEN_GSC = [f"打开 {GSC_HOME} ，左上角选 {SITE}",
            "把下面一个网址粘到最上面的搜索框，按回车",
            "点「测试实际网址」，等它说「可以编入索引」",
            "点「请求编入索引」",
            "换下一个网址，重复第 2–4 步"]
SAY_NEXT = "开个对话，跟 AI 说「下一步」"
REVIEW_STEPS = ["你看过，哪里不满意直接说，AI 改了再给你看，来回几轮都行",
                "你说「可以了」，再从你的邮箱亲手发出，发完跟 AI 说「发了」"]


def _when(days: list[str]) -> str:
    if not days:
        return "很久以前"
    a, b = days[0], days[-1]
    fa = f"{int(a[5:7])} 月 {int(a[8:10])} 日"
    if a == b:
        return fa
    return fa + "到" + (f" {int(b[8:10])} 日" if a[:7] == b[:7] else f" {int(b[5:7])} 月 {int(b[8:10])} 日")


def plain_action(a: dict) -> dict:
    """{title, why, steps, urls, you} — you=True when the operator has something to do."""
    r, v, f, objs = a["rule"], a["variant"], a["facts"], a["objects"]
    n, who = len(objs), f.get("who", "")
    pages = f"{n} 个页面" if n > 1 else "1 个页面"
    if r in ("W-01", "W-02", "W-03", "W-04", "W-05", "W-06", "W-07"):
        then = THEN.get(f.get("state", ""), "页面有问题")
        if v == "request":
            return {"title": f"去 Google 后台点几下，让 Google 重新看 {pages}", "you": True,
                    "why": f"Google 上次看这些页面是在 {_when(f.get('crawled', []))}，那时{then}。现在页面早就好了，"
                           "但 Google 还没回来看，所以这些页一直搜不到。",
                    "steps": OPEN_GSC[:4] + (OPEN_GSC[4:] if n > 1 else []), "urls": objs,
                    "after": "嫌麻烦的话，跟 AI 说「你来点」，AI 帮你点。做完跟 AI 说一声「点完了」，之后等 Google 来看就行。"}
        if v == "fix":
            return {"title": f"AI 要修 {pages}：{then}", "you": True,
                    "why": f"这些页面现在还是{then}，Google 收录不了。", "urls": objs,
                    "steps": [SAY_NEXT + "，AI 会在网站代码里改好", "AI 改好后会问你「上不上线」，你回答就行"]}
        return {"title": f"AI 要看一下 {pages}现在是不是好的", "you": False, "urls": objs,
                "why": f"Google 记的是{then}，要先看看网站上现在是不是还这样。"}
    if r in ("W-16", "W-17", "W-09", "W-08", "W-19"):
        what = {"W-16": "网站设置不让 Google 看，它却收录了", "W-17": "Google 收录了但读不到内容",
                "W-09": "Google 把它当成了别的页面的重复", "W-08": "会自动跳到别的页面，要确认是不是故意的",
                "W-19": "Google 给了一个新的状态说法，AI 要把它翻译进表里"}[r]
        return {"title": f"AI 要处理 {pages}：{what}", "you": False, "urls": objs, "why": what + "。",
                "after": "要改网站的话，AI 改好后会问你「上不上线」。"}
    if r == "W-11":
        return {"title": "去 Google 后台点几下，告诉 Google 有新页面", "you": True, "urls": objs,
                "why": "这是你新发布的页面，Google 还不知道它。点一次能让 Google 早点来看。",
                "steps": OPEN_GSC[:4] + (OPEN_GSC[4:] if n > 1 else []),
                "after": "嫌麻烦的话，跟 AI 说「你来点」。做完跟 AI 说一声「点完了」。"}
    if r == "W-13":
        return {"title": f"AI 检查 {pages}：Google 知道" + ("它们" if n > 1 else "它") + "，但还没来看", "you": False,
                "why": "看看是不是网站哪里挡住了 Google，有问题才修。"}
    if r == "W-24":
        return {"title": f"AI 检查 {pages}的标题和简介写得对不对", "you": False,
                "why": "这些是你新发或改过的页面，按 Google 的要求检查一次。"}
    if r == "M-01":
        return {"title": f"回复 {who}：对方要报价", "you": True,
                "why": f"{who} 回信了，想要报价、规格、价格或样品。有人在等我们。",
                "steps": [SAY_NEXT + "，AI 会起草回信", *REVIEW_STEPS]}
    if r in ("M-02", "M-03"):
        what = "对方提出了顾虑" if r == "M-02" else "对方回信了"
        return {"title": f"回复 {who}：{what}", "you": True, "why": f"{who} {what}，有人在等我们。",
                "steps": [SAY_NEXT + "，AI 会帮你起草回信", *REVIEW_STEPS]}
    if r == "M-04":
        return {"title": f"不再给 {who} 发后续邮件", "you": False, "why": "对方说不想再收。"}
    if r == "M-05":
        return {"title": f"{who} 的邮箱地址不存在了", "you": True,
                "why": "信被退回来，说这个地址不存在，再发也收不到。",
                "steps": ["要不要另找这个人的公开邮箱？在对话里跟 AI 说一声「找」或「不找」就行"]}
    if r == "M-07":
        return {"title": f"AI 查一下为什么 {who} 不收我们的信", "you": False,
                "why": "对方的邮件服务器拒收，问题多半出在我们发信域名的设置上，不是信的内容。"}
    if r == "M-08":
        return {"title": "这几天少发几封外展邮件", "you": True,
                "why": "好几家公司的邮件服务器在退我们的信，发太多会更糟。", "steps": ["这几天少发几封，等退信变少再慢慢加回"]}
    if r == "M-09":
        return {"title": f"不再用 {who} 的旧邮箱地址", "you": False, "why": "对方通知说换了地址。"}
    if r == "M-11":
        return {"title": f"给 {who} 发第 {f.get('n')} 封跟进邮件", "you": True, "why": "按计划今天该发了，对方还没回信。",
                "steps": [SAY_NEXT + "，AI 会准备好这封信", *REVIEW_STEPS]}
    if r == "Q-01" and v == "report":
        return {"title": f"有 {n} 条新询盘", "you": True, "why": "来自：" + "、".join(f.get("companies", [])) + "。",
                "steps": ["照平时的流程处理询盘就行，这里只是告诉你"]}
    if r == "Q-01":
        return {"title": f"AI 查一下 {n} 条新询盘是哪次推广带来的", "you": False, "why": "有证据才记上，没有就留空。"}
    if r == "E-01":
        return {"title": f"说一句：{objs[0]} 那次登记的链接对不对", "you": True,
                "why": "AI 打不开你给的链接。", "steps": [f"{SAY_NEXT}，告诉 AI 链接是不是给错了，还是还没上线"]}
    return {"title": a["title"], "you": a["you_do"] != "不用你动手", "why": a["why"].split("\n")[0]}


def render_plain(result: dict) -> str:
    acts = [dict(a, plain=plain_action(a)) for a in result["actions"]]
    out = []
    if acts:
        p = acts[0]["plain"]
        out += [f"下一步：{p['title']}", "", p["why"]]
        if p.get("steps"):
            out += ["", "怎么做：" if p["you"] else "AI 会这样做："] + [f"{i}. {x}" for i, x in enumerate(p["steps"], 1)]
        if p.get("urls"):
            shown = p["urls"][:SHOW]
            out += ["", "网址：" if len(p["urls"]) > 1 else "网址："] + shown
            if len(p["urls"]) > SHOW:
                out.append(f"……还有 {len(p['urls']) - SHOW} 个，跟 AI 要完整名单")
        if p.get("after"):
            out += ["", p["after"]]
        if not p["you"]:
            out += ["", "这件不用你做。想让 AI 现在就做，" + SAY_NEXT + "。"]
        rest = acts[1:]
        if rest:
            out += ["", "之后还有："]
            for b in rest[:QUEUE]:
                out.append(f"- {b['plain']['title']}" + ("" if b["plain"]["you"] else "（不用你做）"))
            if len(rest) > QUEUE:
                out.append(f"- 另外还有 {len(rest) - QUEUE} 件")
    else:
        out += ["下一步：今天没有要你做的事", "", "网站和邮件都在正常等反馈。"]
    st = result["site"]
    line = f"网站现在：{st['pages']} 个页面里，Google 已收录 {st['indexed']} 个"
    line += "，其余的大多在等 Google 来看，正常。" if st["pages"] > st["indexed"] else "。"
    if st["has_perf"]:
        line += f"最近一周被搜到 {st['impressions_7d']} 次，点进来 {st['clicks_7d']} 次。"
    else:
        line += "有多少人搜到、点进来，要再等两三天才有数。"
    if st["inquiries"]:
        line += f"询盘一共 {st['inquiries']} 条。"
    out += ["", line]
    return "\n".join(out)


# ---------------------------------------------------------------- write-backs


def mark(args) -> int:
    schema = bt.load_schema()
    svc = bt.sheets_service()
    sid = bt.load_target(args.target)
    now = bt.stamp(bt.beijing_now())
    note = f"已核（{args.rule}）{now[:10]}：{args.note}" if args.rule == "W-13" else f"已查（W-24）{now[:10]}：{args.note}"
    if args.rule == "W-13":
        rows = bt.read_table(svc, sid, schema, "网页收录")
        latest = latest_by(rows, "网址", "检查日期")
        todo = []
        for url in args.url:
            r = latest.get(url)
            if not r:
                raise SystemExit(f"网页收录里没有 {url}")
            todo.append({**r, "备注": "；".join(x for x in (r.get("备注"), note) if x)})
        added, updated = bt.upsert_rows(svc, sid, schema, "网页收录", todo, now, existing=rows)
    else:
        rows = bt.read_table(svc, sid, schema, "执行登记")
        by_id = {r["登记编号"]: r for r in rows}
        todo = []
        for eid in args.id:
            if eid not in by_id:
                raise SystemExit(f"执行登记里没有 {eid}")
            r = by_id[eid]
            todo.append({**r, "备注": "；".join(x for x in (r.get("备注"), note) if x)})
        added, updated = bt.upsert_rows(svc, sid, schema, "执行登记", todo, now, existing=rows)
    print(f"记下 {updated} 行（{args.rule}）")
    return 0


def log_request(args) -> int:
    schema = bt.load_schema()
    svc = bt.sheets_service()
    sid = bt.load_target(args.target)
    now = bt.stamp(bt.beijing_now())
    day = args.date or now[:10]
    new = [el.prepare(schema, {"执行日期": day, "线": "营销", "渠道": "网站", "动作": "其他", "内容说明": REQUEST_NOTE,
                               "网址": url, "来源": "操作者口述", "查证结果": el.PRIVATE,
                               "查证证据": "GSC 后台里的操作，外部看不到；按操作者口述记录"}, now)
           for url in args.url]
    for r in el.register(svc, sid, schema, new, now):  # same numbering and duplicate check as scripts/execution_log.py
        print(el.describe(r))
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", choices=["main", "sample"], default="main")
    sub = ap.add_subparsers(dest="command")
    ap.add_argument("--format", choices=["text", "plain", "json"], default="text",
                    help="text = 规则第 11 节格式（会话用）；plain = 大白话短版（每日提醒用）；json = 给编排")
    ap.add_argument("--now", help="北京时间「年-月-日 时:分」，默认现在")
    ap.add_argument("--since", help="询盘「新行」从哪个时刻算起，默认 --now 往前 24 小时；编排传台账里的「上次读反馈」")
    ap.add_argument("--line", choices=LINES, help="只看一条线（编排用）；不带 = 两线合看（每日提醒）")
    ap.add_argument("--no-live", action="store_true", help="不抓线上（阻断类规则改为「AI 先看线上」）")
    ap.add_argument("--offline-sample", action="store_true", help="不连网，用脚本内置的样例数据")
    m = sub.add_parser("mark")
    m.add_argument("--rule", choices=["W-13", "W-24"], required=True)
    m.add_argument("--url", action="append", default=[])
    m.add_argument("--id", action="append", default=[])
    m.add_argument("--note", required=True)
    r = sub.add_parser("log-request")
    r.add_argument("--url", action="append", required=True)
    r.add_argument("--date", help="执行日期，默认今天")
    args = ap.parse_args()
    if args.command == "mark":
        if (args.rule == "W-13") != bool(args.url) or (args.rule == "W-24") != bool(args.id):
            raise SystemExit("W-13 用 --url，W-24 用 --id")
        sys.exit(mark(args))
    if args.command == "log-request":
        sys.exit(log_request(args))
    now = args.now or bt.stamp(bt.beijing_now())
    since = args.since or (datetime.strptime(now, "%Y-%m-%d %H:%M") - timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    sample = args.offline_sample or args.target == "sample"
    result = next_step(load(args), now, since, live=not (args.no_live or sample), line=args.line)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json"
          else render_plain(result) if args.format == "plain" else render(result))


if __name__ == "__main__":
    main()
