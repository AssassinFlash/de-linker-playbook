# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100",
#   "google-auth>=2.20",
#   "requests>=2.31",
# ]
# ///
"""
本地运营看板：从底表导出只读 JSON，再用本机页面读它。

  uv run scripts/dashboard.py self-check          不连网，核对计数和打码
  uv run scripts/dashboard.py export              读底表，写出仓外 JSON（不写表、不发信）
  uv run scripts/dashboard.py open                在 127.0.0.1 打开页面

JSON 在 ~/.config/de-linker-playbook/dashboard.json，权限 600，不进仓库。
这是操作者自己看的页面。申请正文写在这份本地 JSON 里，不写回底表。
密钥、表格 ID、IP、浏览器标识和支付凭证不进 JSON，也不进日志。
每天 08:30 的定时任务在邮箱回流之后、每日提醒之前调用 export。导出时另读 GA4 近 7 天汇总，只进这份本地 JSON，不写底表。
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta
from html import unescape
import json
import os
import re
import sys
import tomllib
from zoneinfo import ZoneInfo
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[1]
PAGE = Path(__file__).with_name("dashboard.html")
OUT = Path.home() / ".config" / "de-linker-playbook" / "dashboard.json"
HOST = "127.0.0.1"
PORT = 8766
LEVELS = ("L0", "L1", "L2", "L3")
INQUIRY_STATUSES = ("询盘已收到", "形式发票已开", "已完成", "已取消")
CUMULATIVE = {"L1": {"L1", "L2", "L3"}, "L2": {"L2", "L3"}, "L3": {"L3"}}


def is_url(value) -> bool:
    return isinstance(value, str) and value.startswith(("http://", "https://"))


def text_of(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return unescape(value).strip()
    return str(value).strip()


def plain(value, depth: int = 0) -> str:
    """Readable text for a nested Woo value. Empty when there is nothing to show."""
    if depth > 5 or value is None:
        return ""
    if isinstance(value, bool):
        return "是" if value else "否"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, str):
        return unescape(value).strip()
    if isinstance(value, list):
        bits = [plain(item, depth + 1) for item in value[:24]]
        return "、".join(bit for bit in bits if bit)
    if isinstance(value, dict):
        unit = plain(value.get("unit"), depth + 1) if "unit" in value else ""
        if any(key in value for key in ("min", "max", "value")):
            low, high, single = plain(value.get("min"), depth + 1), plain(value.get("max"), depth + 1), plain(value.get("value"), depth + 1)
            if single and not low and not high:
                core = single
            elif low and high and low != high:
                core = f"{low}–{high}"
            else:
                core = low or high or single
            return f"{core} {unit}".strip()
        bits = []
        for key, item in value.items():
            if key in {"unit", "source", "evidence", "fingerprint"}:
                continue
            bit = plain(item, depth + 1)
            if bit:
                bits.append(bit)
        return "；".join(bits)
    return ""


def num(value) -> int:
    if value in (None, ""):
        return 0
    return int(value)


def optional_num(value):
    if value in (None, ""):
        return None
    return int(value)


def address_of(block) -> str:
    if not isinstance(block, dict):
        return ""
    parts = [text_of(block.get(key)) for key in ("address_1", "address_2", "postcode", "city", "state", "country")]
    return ", ".join(part for part in parts if part)


def meta_map(order: dict) -> dict:
    found = {}
    meta = order.get("meta_data")
    if not isinstance(meta, list):
        return found
    for item in meta:
        if isinstance(item, dict) and isinstance(item.get("key"), str):
            found[item["key"]] = item.get("value")
    return found


SPEC_LABEL = {
    "dimensions_mm": "尺寸",
    "weight_kg": "重量",
    "ip_rating": "防护等级",
    "operating_temp_c": "工作温度",
    "phases": "相数",
    "display": "显示",
    "ac_output_kw_nominal": "交流额定功率",
    "ac_output_kw_max": "交流最大功率",
    "backup_power_kw": "备电功率",
    "battery_voltage_range_v": "电池电压",
    "comms": "通讯",
    "euro_efficiency_pct": "欧洲效率",
    "max_efficiency_pct": "最大效率",
    "max_battery_charge_a": "最大充电电流",
    "max_battery_discharge_a": "最大放电电流",
    "max_input_current_per_mppt_a": "每路 MPPT 最大输入电流",
    "max_isc_per_mppt_a": "每路 MPPT 最大短路电流",
    "max_pv_input_power_w": "最大光伏输入功率",
    "max_pv_input_v": "最大光伏输入电压",
    "mppt_voltage_range_v": "MPPT 电压",
    "n_mppt": "MPPT 路数",
    "grid_codes": "并网标准",
    "start_voltage_v": "启动电压",
    "ups_switchover_ms": "UPS 切换",
    "nominal_voltage": "额定电压",
}
DOC_LABEL = {"proformas": "形式发票", "invoice": "发票", "quotes": "报价", "adjustments": "调整"}
DOC_FIELDS = (
    ("status", "状态"), ("reason", "原因"), ("created_at", "创建"), ("expires_at", "到期"),
    ("issued_at", "开出"), ("due_date", "到期日"), ("service_date", "服务日"),
    ("voided_at", "作废"), ("void_reason", "作废原因"), ("superseded_at", "被替换"),
    ("superseded_reason", "替换原因"), ("accepted_at", "接受"), ("type", "类型"),
    ("original_invoice_reference", "原发票号"), ("trigger", "触发"),
)
FIELD_LABEL = {
    "tv_b2b_project_title": "项目",
    "tv_b2b_project_ref": "项目编号",
    "tv_b2b_vat_id_submitted": "增值税号",
    "tv_b2b_vies_status": "VIES",
    "tv_b2b_tax_treatment": "税务处理",
    "tv_b2b_order_flow": "订单流程",
    "tv_b2b_invoice_number": "发票号",
    "tv_b2b_freight_reason": "运费说明",
    "tv_b2b_freight_confirmation_note": "运费确认",
    "tv_b2b_quote_expires_at": "报价到期",
    "_linker_locale": "语言",
    "_linker_inquiry_topic": "主题",
    "_linker_inquiry_source": "入口",
    "_wc_order_attribution_source_type": "来源类型",
    "_wc_order_attribution_utm_source": "UTM 来源",
    "_wc_order_attribution_device_type": "设备",
    "_wc_order_attribution_session_pages": "会话页数",
    "_wc_order_attribution_session_entry": "进站页",
    "tv_b2b_customer_status_at_order": "下单时客户状态",
    "tv_payment_terms_snapshot": "付款条款",
    "tv_b2b_commercial_terms_snapshot": "商务条款",
    "tv_b2b_freight_verdict_snapshot": "运费结论",
}
SKIP_META = {
    "tv_b2b_material_snapshot", "tv_b2b_document_ledger_v2", "tv_b2b_policy_snapshot",
    "tv_b2b_quote_operation_fingerprint", "tv_b2b_quote_operation_key",
    "_wc_order_attribution_user_agent", "_shipping_hash", "_coupons_hash", "_fees_hash", "_taxes_hash",
    "tv_b2b_company_snapshot", "tv_b2b_order_vat_snapshot", "tv_b2b_effective_payment_terms_v2",
}
VIA = {"checkout": "站内结账", "dlk-quote": "报价单", "linker_contact": "联系表单", "store-api": "商店接口"}
TOPIC = {"partnership": "合作", "offer": "报价", "general": "一般咨询", "contact": "联系表单", "proforma": "形式发票"}


def specs_of(material) -> list[dict]:
    technical = material.get("technical") if isinstance(material, dict) else None
    spec = technical.get("specifications") if isinstance(technical, dict) else None
    if not isinstance(spec, dict):
        return []
    rows = []
    for key, value in spec.items():
        text = plain(value)
        if text:
            rows.append({"label": SPEC_LABEL.get(key, key), "value": text})
    return rows


def materials_of(raw) -> list[dict]:
    if not isinstance(raw, str) or not raw.strip():
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []
    rows = data.get("materials") if isinstance(data, dict) else None
    return [row for row in rows if isinstance(row, dict)] if isinstance(rows, list) else []


def documents_of(raw) -> list[dict]:
    if not isinstance(raw, str) or not raw.strip():
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, dict):
        return []
    docs = []
    for kind, label in DOC_LABEL.items():
        block = data.get(kind)
        rows = block if isinstance(block, list) else ([block] if isinstance(block, dict) else [])
        for row in rows:
            if not isinstance(row, dict):
                continue
            fields = []
            for key, name in DOC_FIELDS:
                text = plain(row.get(key))
                if text:
                    fields.append({"label": name, "value": text})
            reference = plain(row.get("reference")) or plain(row.get("document_type"))
            if reference or fields:
                docs.append({"kind": label, "reference": reference, "fields": fields})
    return docs


def project_live_order(order: dict) -> dict:
    """Operator view of one inquiry. Drops IP, browser id, and payment tokens."""
    billing = order.get("billing") if isinstance(order.get("billing"), dict) else {}
    meta = meta_map(order)
    materials = materials_of(meta.get("tv_b2b_material_snapshot"))
    by_product = {}
    for row in materials:
        by_product[str(row.get("product_id"))] = row
    items = []
    used = set()
    for raw in order.get("line_items") or []:
        if not isinstance(raw, dict):
            continue
        matched = by_product.get(str(raw.get("product_id")))
        material = matched.get("material") if isinstance(matched, dict) else {}
        if not isinstance(material, dict):
            material = {}
        identity = material.get("identity") if isinstance(material.get("identity"), dict) else {}
        if matched is not None:
            used.add(id(matched))
        items.append({
            "name": text_of(raw.get("name")) or text_of(identity.get("model")) or "未命名",
            "sku": text_of(raw.get("sku")) or text_of(identity.get("manufacturer_part_number")),
            "quantity": raw.get("quantity"),
            "total": text_of(raw.get("total")),
            "manufacturer": text_of(identity.get("manufacturer")),
            "model": text_of(identity.get("model")),
            "partNumber": text_of(identity.get("manufacturer_part_number")),
            "specs": specs_of(material),
        })
    for row in materials:
        if id(row) in used:
            continue
        material = row.get("material") if isinstance(row.get("material"), dict) else {}
        identity = material.get("identity") if isinstance(material.get("identity"), dict) else {}
        items.append({
            "name": text_of(identity.get("model")) or text_of(identity.get("manufacturer_part_number")) or "未命名",
            "sku": text_of(identity.get("manufacturer_part_number")),
            "quantity": row.get("quantity"),
            "total": "",
            "manufacturer": text_of(identity.get("manufacturer")),
            "model": text_of(identity.get("model")),
            "partNumber": text_of(identity.get("manufacturer_part_number")),
            "specs": specs_of(material),
        })
    fields = []
    for key, label in FIELD_LABEL.items():
        text = plain(meta.get(key))
        if text:
            fields.append({"label": label, "value": text})
    shipping = order.get("shipping") if isinstance(order.get("shipping"), dict) else {}
    ship_lines = []
    for row in order.get("shipping_lines") or []:
        if not isinstance(row, dict):
            continue
        title = text_of(row.get("method_title"))
        amount = text_of(row.get("total"))
        if title or amount:
            ship_lines.append(" ".join(part for part in (title, amount) if part))
    number = order.get("number")
    if isinstance(number, bool):
        number = ""
    return {
        "id": str(order.get("id") or ""),
        "number": text_of(number),
        "company": text_of(billing.get("company")),
        "contact": " ".join(part for part in (text_of(billing.get("first_name")), text_of(billing.get("last_name"))) if part),
        "email": text_of(billing.get("email")),
        "phone": text_of(billing.get("phone")),
        "address": address_of(billing),
        "shipAddress": address_of(shipping),
        "note": text_of(order.get("customer_note")),
        "topic": TOPIC.get(text_of(meta.get("_linker_inquiry_topic")), text_of(meta.get("_linker_inquiry_topic"))),
        "via": VIA.get(text_of(order.get("created_via")), text_of(order.get("created_via"))),
        "payment": text_of(order.get("payment_method_title")),
        "currency": text_of(order.get("currency")),
        "total": text_of(order.get("total")),
        "project": text_of(meta.get("tv_b2b_project_title")),
        "projectRef": text_of(meta.get("tv_b2b_project_ref")),
        "items": items,
        "shipping": "；".join(ship_lines),
        "documents": documents_of(meta.get("tv_b2b_document_ledger_v2")),
        "fields": fields,
    }


def fetch_live_inquiries() -> list[dict]:
    import inquiry_pull as ip

    key, secret = ip.load_secrets()
    fetch = ip.make_fetcher(key, secret)
    page = 1
    orders = []
    while page <= ip.MAX_PAGES:
        batch, _total, pages = fetch(page, True)
        orders.extend(batch)
        if not batch or len(batch) < ip.PER_PAGE or (pages and page >= pages):
            break
        page += 1
    projected = []
    for order in orders:
        if not isinstance(order, dict):
            continue
        rec = project_live_order(order)
        created = order.get("date_created_gmt")
        if isinstance(created, str) and created.strip():
            try:
                rec["created"] = ip.gmt_to_beijing(created)
            except Exception:
                rec["created"] = created.strip()
        issued = ""
        for item in order.get("meta_data") or []:
            if isinstance(item, dict) and item.get("key") == ip.ISSUED_META and item.get("value") not in (None, ""):
                try:
                    issued = ip.unix_to_beijing(item.get("value"))
                except Exception:
                    issued = ""
                break
        rec["issued"] = issued
        status = order.get("status")
        rec["status"] = ip.STATUS_ZH.get(status, text_of(status))
        projected.append(rec)
    return projected


def merge_inquiry(row: dict, live: dict) -> dict:
    item = {
        "id": str(row.get("询盘内部编号") or live.get("id") or ""),
        "number": text_of(row.get("单号") or live.get("number")),
        "company": text_of(row.get("公司") or live.get("company")),
        "created": text_of(row.get("创建时刻（北京时间）") or live.get("created")),
        "status": text_of(row.get("状态") or live.get("status")),
        "issued": text_of(row.get("形式发票签发时刻（北京时间）") or live.get("issued")),
        "attribution": text_of(row.get("归因登记编号")),
        "attributionBasis": text_of(row.get("归因依据")),
        "source": text_of(row.get("来源类型")),
        "device": text_of(row.get("设备类型")),
        "pages": row.get("会话页数") if isinstance(row.get("会话页数"), int) else "",
        "sheetNote": text_of(row.get("备注")),
        "contact": live.get("contact") or "",
        "email": live.get("email") or "",
        "phone": live.get("phone") or "",
        "address": live.get("address") or "",
        "shipAddress": live.get("shipAddress") or "",
        "note": live.get("note") or "",
        "topic": live.get("topic") or "",
        "via": live.get("via") or "",
        "payment": live.get("payment") or "",
        "currency": live.get("currency") or "",
        "total": live.get("total") or "",
        "project": live.get("project") or "",
        "projectRef": live.get("projectRef") or "",
        "items": live.get("items") or [],
        "shipping": live.get("shipping") or "",
        "documents": live.get("documents") or [],
        "fields": live.get("fields") or [],
    }
    return item


def build_payload(tables: dict[str, list[dict]], exported_at: str, live: list[dict] | None = None, live_error: str = "", ga4: dict | None = None) -> dict:
    logs = {text_of(row.get("登记编号")): row for row in tables.get("执行登记", [])}
    actions = []
    for row in tables.get("动作进度", []):
        log = logs.get(text_of(row.get("登记编号")), {})
        url = ""
        for key in ("网址", "网址或收件公司"):
            if is_url(row.get(key)):
                url = row[key]
                break
        if not url and is_url(log.get("网址")):
            url = log["网址"]
        company = text_of(log.get("收件公司"))
        if not company and not is_url(row.get("网址或收件公司")):
            company = text_of(row.get("网址或收件公司"))
        actions.append({
            "date": text_of(row.get("执行日期") or log.get("执行日期")),
            "id": text_of(row.get("登记编号")),
            "registeredAt": text_of(log.get("登记时刻（北京时间）")),
            "line": text_of(row.get("线") or log.get("线")),
            "channel": text_of(row.get("渠道") or log.get("渠道")),
            "category": text_of(row.get("动作大类") or log.get("动作大类")),
            "action": text_of(row.get("动作") or log.get("动作")),
            "summary": text_of(row.get("内容说明") or log.get("内容说明")),
            "evidence": text_of(log.get("查证证据")),
            "verifiedAt": text_of(log.get("查证时刻（北京时间）")),
            "note": text_of(log.get("备注") or row.get("备注")),
            "source": text_of(log.get("来源")),
            "oldUrl": text_of(log.get("旧网址")) if is_url(log.get("旧网址")) else "",
            "url": url,
            "company": company,
            "verified": text_of(row.get("查证结果") or log.get("查证结果")),
            "level": text_of(row.get("当前最高级别")),
            "indexStatus": text_of(row.get("收录状态")),
            "compared": text_of(row.get("和上次比")),
            "impressions7": optional_num(row.get("近 7 天展示")),
            "clicks7": optional_num(row.get("近 7 天点击")),
            "impressions7De": optional_num(row.get("近 7 天展示（德国）")),
            "clicks7De": optional_num(row.get("近 7 天点击（德国）")),
            "queries7": text_of(row.get("近 7 天主要搜索词")),
            "mailEvent": text_of(row.get("最新邮件事件")),
            "attributed": num(row.get("归因询盘数")) if row.get("归因询盘数") not in (None, "") else 0,
            "feedbackDate": text_of(row.get("最近一次反馈日期")),
        })
    actions.sort(key=lambda row: (row["date"], row["id"]), reverse=True)

    by_status = {name: 0 for name in INQUIRY_STATUSES}
    issued = attributed = 0
    by_date = {}
    unique = {}
    for row in tables.get("询盘", []):
        key = str(row.get("询盘内部编号"))
        prev = unique.get(key)
        if prev is None:
            unique[key] = row
            continue
        merged = dict(prev)
        for field, value in row.items():
            if merged.get(field) in (None, "") and value not in (None, ""):
                merged[field] = value
        unique[key] = merged
    live_by_id = {str(row.get("id")): row for row in (live or []) if row.get("id")}
    seen = set()
    inquiry_items = []
    for key, row in unique.items():
        seen.add(key)
        inquiry_items.append(merge_inquiry(row, live_by_id.get(key, {})))
    for key, row in live_by_id.items():
        if key not in seen:
            inquiry_items.append(merge_inquiry({}, row))
    inquiry_items.sort(key=lambda row: row.get("created") or "", reverse=True)
    for row in unique.values():
        by_status[row.get("状态", "")] = by_status.get(row.get("状态", ""), 0) + 1
        if row.get("形式发票签发时刻（北京时间）"):
            issued += 1
        if row.get("归因登记编号"):
            attributed += 1
        day = str(row.get("创建时刻（北京时间）") or "")[:10]
        if len(day) == 10:
            by_date[day] = by_date.get(day, 0) + 1

    levels = [row.get("level") for row in actions]
    ladder = {"L0": len(actions)}
    for name, accepted in CUMULATIVE.items():
        ladder[name] = sum(level in accepted for level in levels)

    history: dict[str, list[dict]] = {}
    for row in tables.get("网页收录", []):
        url = row.get("网址", "")
        if not is_url(url):
            continue
        history.setdefault(url, []).append({
            "checked": text_of(row.get("检查日期")),
            "status": text_of(row.get("收录状态")),
            "verdict": text_of(row.get("收录结论")),
            "compared": text_of(row.get("和上次比")),
            "reason": text_of(row.get("原因说明")),
            "robots": text_of(row.get("robots 是否放行")),
            "indexable": text_of(row.get("是否允许收录")),
            "fetch": text_of(row.get("抓取结果")),
            "fetchedAt": text_of(row.get("上次抓取时间（北京时间）")),
            "googleCanonical": text_of(row.get("Google 选的正式地址")),
            "declaredCanonical": text_of(row.get("页面声明的正式地址")),
            "language": text_of(row.get("语言")),
            "level": text_of(row.get("反馈级别")),
            "actionId": text_of(row.get("登记编号")),
        })
    pages = []
    for url, checks in history.items():
        checks.sort(key=lambda row: row["checked"], reverse=True)
        latest = dict(checks[0])
        latest["url"] = url
        latest["history"] = checks
        pages.append(latest)
    pages.sort(key=lambda row: (row["checked"], row["url"]), reverse=True)
    reason_by_url = {row["url"]: row.get("reason", "") for row in pages}
    for row in actions:
        row["reason"] = reason_by_url.get(row["url"], "")

    performance = []
    for row in tables.get("网页表现", []):
        performance.append({
            "date": text_of(row.get("日期（太平洋时间）")),
            "url": row.get("网址", "") if is_url(row.get("网址")) else "",
            "country": text_of(row.get("国家")),
            "device": text_of(row.get("设备")),
            "type": text_of(row.get("搜索类型")),
            "impressions": num(row.get("展示")),
            "clicks": num(row.get("点击")),
            "ctr": text_of(row.get("点击率")),
            "position": text_of(row.get("平均排名")),
            "actionId": text_of(row.get("登记编号")),
        })
    queries = []
    for row in tables.get("搜索词", []):
        queries.append({
            "date": text_of(row.get("日期（太平洋时间）")),
            "query": text_of(row.get("搜索词")),
            "url": row.get("网址", "") if is_url(row.get("网址")) else "",
            "type": text_of(row.get("搜索类型")),
            "country": text_of(row.get("国家")),
            "device": text_of(row.get("设备")),
            "impressions": num(row.get("展示")),
            "clicks": num(row.get("点击")),
            "ctr": text_of(row.get("点击率")),
            "position": text_of(row.get("平均排名")),
            "actionId": text_of(row.get("登记编号")),
        })

    return {
        "exportedAt": exported_at,
        "ladder": ladder,
        "ladderRule": "L0 已执行：做了，搜索还没看到。L1 已被看到：已收录或已有展示。L2 有互动：有点击或邮件回复。L3 有转化：有询盘归因到这次动作。L1、L2、L3 是累计口径，到了更高一级也算进前面。",
        "inquiries": {
            "total": len(unique),
            "byStatus": by_status,
            "issued": issued,
            "attributed": attributed,
            "byDate": [{"date": day, "count": by_date[day]} for day in sorted(by_date)],
            "items": inquiry_items,
            "liveError": live_error,
            "rule": "列表含形式发票申请的正文，供本机查看。底表仍只留最小列。联系表单若已进订单，也会出现在这里。",
        },
        "gsc": {
            "performanceRows": len(tables.get("网页表现", [])),
            "queryRows": len(tables.get("搜索词", [])),
            "indexRows": len(tables.get("网页收录", [])),
            "indexUrls": len(pages),
        },
        "actions": actions,
        "pages": pages,
        "performance": performance,
        "queries": queries,
        "mail": mail_payload(tables.get("邮件反馈", [])),
        "ga4": ga4 or empty_ga4(),
    }



def mail_payload(rows: list[dict]) -> dict:
    events = []
    for row in rows:
        events.append({
            "date": text_of(row.get("事件日期")),
            "id": text_of(row.get("登记编号")),
            "company": text_of(row.get("收件公司")),
            "event": text_of(row.get("事件类型")),
            "level": text_of(row.get("反馈级别")),
            "bounce": text_of(row.get("退信状态码")),
            "replyClass": text_of(row.get("回复分类")),
            "replyId": text_of(row.get("回信 Message-ID")),
            "note": text_of(row.get("备注")),
            "writtenAt": text_of(row.get("写入时刻（北京时间）")),
        })
    events.sort(key=lambda row: (row["date"], row["id"]), reverse=True)
    return {
        "connected": True,
        "total": len(events),
        "events": events,
        "rule": "只含已登记邮件上的事件。未见退信是推断，不是投递回执。不存正文和地址。每日提醒不进表。",
    }



GA4_RULE = "只统计同意分析的访客，没有建模补齐，所以比真实访问少。不能和 GSC 点击对账。反馈规则不用站内行为，这些数不进底表。"
GA4_TZ = ZoneInfo("Europe/Berlin")
CHANNEL_ZH = {
    "Direct": "直接访问",
    "Organic Search": "自然搜索",
    "Organic Social": "自然社媒",
    "Referral": "外部引荐",
    "Paid Search": "付费搜索",
    "Paid Social": "付费社媒",
    "Email": "邮件",
    "Display": "展示广告",
    "Unassigned": "未分类",
}
INQUIRY_EVENTS = {"generate_lead", "form_submit", "form_start", "purchase"}
PATH_QUERY = re.compile(r"[?#].*$")


def empty_ga4(error: str = "") -> dict:
    return {
        "connected": False,
        "error": error,
        "window": "",
        "timezone": "Europe/Berlin",
        "sessions": 0,
        "users": 0,
        "pageViews": 0,
        "sources": [],
        "landings": [],
        "events": [],
        "inquiryEvents": [],
        "byDate": [],
        "rule": GA4_RULE,
    }


def ga4_window() -> tuple[str, str]:
    end = datetime.now(GA4_TZ).date()
    start = end - timedelta(days=6)
    return start.isoformat(), end.isoformat()


def clean_path(value: str) -> str:
    if "@" in (value or ""):
        return ""
    return PATH_QUERY.sub("", value or "") or "/"


def shape_ga4(totals: dict, sources: list[dict], landings: list[dict], events: list[dict], days: list[dict], start: str, end: str) -> dict:
    inquiry = [row for row in events if row["name"] in INQUIRY_EVENTS or any(word in row["name"] for word in ("inquiry", "quote", "contact", "proforma"))]
    return {
        "connected": True,
        "error": "",
        "window": f"{start} 至 {end}",
        "timezone": "Europe/Berlin",
        "sessions": int(totals.get("sessions") or 0),
        "users": int(totals.get("totalUsers") or 0),
        "pageViews": int(totals.get("screenPageViews") or 0),
        "sources": sources,
        "landings": [row for row in landings if row.get("path")],
        "events": events,
        "inquiryEvents": inquiry,
        "byDate": days,
        "rule": GA4_RULE,
    }


def _ga4_rows(data: dict) -> list[dict]:
    dims = [item["name"] for item in data.get("dimensionHeaders", [])]
    mets = [item["name"] for item in data.get("metricHeaders", [])]
    out = []
    for row in data.get("rows", []):
        item = {name: value["value"] for name, value in zip(dims, row.get("dimensionValues", []))}
        item.update({name: int(value["value"]) for name, value in zip(mets, row.get("metricValues", []))})
        out.append(item)
    return out


def fetch_ga4() -> dict:
    import base_table as bt
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import service_account

    cfg = Path(os.environ.get("PLAYBOOK_CONFIG", bt.CONFIG_DIR / "config.toml"))
    prop = str(tomllib.loads(cfg.read_text(encoding="utf-8")).get("ga4", {}).get("property_id") or "")
    if not prop.isdigit():
        raise RuntimeError("GA4 媒体资源编号没配")
    cred = Path(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", bt.CONFIG_DIR / "service-account.json"))
    creds = service_account.Credentials.from_service_account_file(
        cred, scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    session = AuthorizedSession(creds)
    start, end = ga4_window()
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport"

    def run(body: dict) -> dict:
        resp = session.post(url, json={"dateRanges": [{"startDate": start, "endDate": end}], **body}, timeout=60)
        if resp.status_code != 200:
            raise RuntimeError(f"GA4 {resp.status_code}")
        return resp.json()

    totals = _ga4_rows(run({"metrics": [{"name": "sessions"}, {"name": "totalUsers"}, {"name": "screenPageViews"}]}))
    total = totals[0] if totals else {}
    sources = []
    for row in _ga4_rows(run({
        "dimensions": [{"name": "sessionDefaultChannelGroup"}, {"name": "sessionSource"}],
        "metrics": [{"name": "sessions"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 8,
    })):
        channel = row["sessionDefaultChannelGroup"]
        sources.append({
            "label": CHANNEL_ZH.get(channel, channel),
            "channel": channel,
            "source": "直接输入" if row["sessionSource"] == "(direct)" else row["sessionSource"],
            "sessions": row["sessions"],
        })
    landings = []
    for row in _ga4_rows(run({
        "dimensions": [{"name": "landingPagePlusQueryString"}],
        "metrics": [{"name": "sessions"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 8,
    })):
        path = clean_path(row["landingPagePlusQueryString"])
        if path:
            landings.append({"path": path, "sessions": row["sessions"]})
    events = [{"name": row["eventName"], "count": row["eventCount"]} for row in _ga4_rows(run({
        "dimensions": [{"name": "eventName"}],
        "metrics": [{"name": "eventCount"}],
        "orderBys": [{"metric": {"metricName": "eventCount"}, "desc": True}],
        "limit": 12,
    }))]
    days = []
    for row in _ga4_rows(run({
        "dimensions": [{"name": "date"}],
        "metrics": [{"name": "sessions"}],
        "orderBys": [{"dimension": {"dimensionName": "date"}}],
    })):
        raw = row["date"]
        days.append({"date": f"{raw[0:4]}-{raw[4:6]}-{raw[6:8]}", "sessions": row["sessions"]})
    return shape_ga4(total, sources, landings, events, days, start, end)


def self_check() -> int:
    tables = {
        "动作进度": [
            {"登记编号": "E-20261018-01", "执行日期": "2026-10-18", "线": "营销", "渠道": "网站", "动作大类": "页面",
             "动作": "更新页面", "网址": "https://de-linker.com/", "查证结果": "已查证", "当前最高级别": "L1",
             "收录状态": "已收录", "和上次比": "没变", "近 7 天展示": 3, "近 7 天点击": 1, "归因询盘数": 0,
             "内容说明": "首页标题改了"},
            {"登记编号": "E-20261017-01", "执行日期": "2026-10-17", "线": "获客", "渠道": "邮件", "动作": "发出开发信",
             "网址或收件公司": "Secret GmbH", "内容说明": "写给 secret@example.com", "查证结果": "已查证", "当前最高级别": "L0"},
            {"登记编号": "E-20261016-01", "执行日期": "2026-10-16", "线": "营销", "渠道": "网站", "动作": "发布页面",
             "网址": "https://de-linker.com/de/", "当前最高级别": "L3", "归因询盘数": 1},
        ],
        "执行登记": [
            {"登记时刻（北京时间）": "2026-10-18 09:40", "登记编号": "E-20261018-01", "线": "营销", "渠道": "网站",
             "动作": "更新页面", "网址": "https://de-linker.com/", "内容说明": "不要出现",
             "查证证据": "线上标题已是新的", "查证结果": "已查证"},
        ],
        "询盘": [
            {"询盘内部编号": 1, "单号": "S-1", "公司": "Secret GmbH", "状态": "已取消", "创建时刻（北京时间）": "2026-10-14 16:12"},
            {"询盘内部编号": 2, "单号": "S-2", "公司": "Other GmbH", "状态": "询盘已收到", "归因登记编号": "E-20261016-01"},
            {"询盘内部编号": 2, "状态": "询盘已收到"},
        ],
        "网页收录": [
            {"网址": "https://de-linker.com/", "检查日期": "2026-10-19", "收录状态": "未收录", "和上次比": "变了", "原因说明": "还没抓到"},
            {"网址": "https://de-linker.com/", "检查日期": "2026-10-20", "收录状态": "已收录", "和上次比": "没变", "原因说明": "已经在索引里"},
            {"网址": "不是网址", "检查日期": "2026-10-20", "收录状态": "已收录"},
        ],
        "网页表现": [],
        "搜索词": [],
    }
    live = project_live_order({
        "id": 2,
        "number": "S-2",
        "status": "inquiry-received",
        "currency": "EUR",
        "total": "120.00",
        "payment_method_title": "Order &amp; Proforma",
        "customer_note": "请报 10 台",
        "customer_ip_address": "10.9.8.7",
        "customer_user_agent": "SecretAgent",
        "created_via": "dlk-quote",
        "billing": {
            "first_name": "Ada", "last_name": "L", "company": "Other GmbH",
            "email": "buyer@example.com", "phone": "+49 1", "address_1": "Street 1",
            "postcode": "10115", "city": "Berlin", "country": "DE",
        },
        "line_items": [{"name": "Hybrid 10kW", "sku": "HY-10", "quantity": 2, "total": "100.00", "product_id": 9}],
        "meta_data": [
            {"key": "tv_b2b_project_title", "value": "柏林项目"},
            {"key": "_stripe_source_id", "value": "src_secret"},
            {"key": "tv_b2b_material_snapshot", "value": json.dumps({
                "materials": [{"product_id": 9, "quantity": 2, "material": {
                    "identity": {"manufacturer": "Fox", "model": "H3", "manufacturer_part_number": "H3-10"},
                    "technical": {"specifications": {"ip_rating": {"value": "IP65"}}},
                }}]
            })},
            {"key": "tv_b2b_document_ledger_v2", "value": json.dumps({
                "proformas": [{"reference": "PF-9", "status": "issued", "created_at": "2026-10-18"}]
            })},
        ],
    })
    live_blob = json.dumps(live, ensure_ascii=False)
    assert live["email"] == "buyer@example.com"
    assert live["note"] == "请报 10 台"
    assert live["payment"] == "Order & Proforma"
    assert live["items"][0]["specs"][0]["value"] == "IP65"
    assert live["documents"][0]["reference"] == "PF-9"
    for forbidden in ("10.9.8.7", "SecretAgent", "src_secret"):
        assert forbidden not in live_blob, forbidden
    payload = build_payload(tables, "2026-10-20 12:00", [live])
    blob = json.dumps(payload, ensure_ascii=False)
    assert payload["ladder"] == {"L0": 3, "L1": 2, "L2": 1, "L3": 1}, payload["ladder"]
    assert payload["inquiries"]["total"] == 2
    assert payload["inquiries"]["byStatus"]["已取消"] == 1
    assert payload["inquiries"]["attributed"] == 1
    assert payload["inquiries"]["byDate"] == [{"date": "2026-10-14", "count": 1}]
    opened = {row["id"]: row for row in payload["inquiries"]["items"]}
    assert opened["1"]["company"] == "Secret GmbH"
    assert opened["1"]["number"] == "S-1"
    assert opened["2"]["email"] == "buyer@example.com"
    assert opened["2"]["note"] == "请报 10 台"
    assert opened["2"]["items"][0]["name"] == "Hybrid 10kW"
    assert opened["2"]["attribution"] == "E-20261016-01"
    mail = next(row for row in payload["actions"] if row["id"] == "E-20261017-01")
    assert mail["company"] == "Secret GmbH"
    assert mail["summary"] == "写给 secret@example.com"
    web = next(row for row in payload["actions"] if row["id"] == "E-20261018-01")
    assert web["evidence"] == "线上标题已是新的"
    assert web["summary"] == "首页标题改了"
    assert web["reason"] == "已经在索引里"
    assert payload["pages"][0]["history"][0]["reason"] == "已经在索引里"
    assert "spreadsheet" not in blob
    assert "10.9.8.7" not in blob
    sample = shape_ga4(
        {"sessions": 1, "totalUsers": 1, "screenPageViews": 1},
        [{"label": "直接访问", "channel": "Direct", "source": "直接输入", "sessions": 1}],
        [{"path": clean_path("/?email=buyer@example.com"), "sessions": 1}, {"path": "/", "sessions": 1}],
        [{"name": "page_view", "count": 1}],
        [{"date": "2026-10-19", "sessions": 1}],
        "2026-10-14", "2026-10-20",
    )
    assert sample["sessions"] == 1 and sample["sources"][0]["label"] == "直接访问"
    assert sample["landings"] == [{"path": "/", "sessions": 1}]
    assert sample["inquiryEvents"] == []
    print("self-check ok")

    return 0



def export() -> int:
    import base_table as bt

    schema = bt.load_schema()
    sid = bt.load_target("main")
    sheets = bt.sheets_service()
    tables = {name: bt.read_table(sheets, sid, schema, name) for name in
              ("执行登记", "网页收录", "网页表现", "搜索词", "邮件反馈", "询盘", "动作进度")}
    live = []
    live_error = ""
    try:
        live = fetch_live_inquiries()
    except Exception as exc:
        message = str(exc)
        if any(token in message.lower() for token in ("ck_", "cs_", "secret", "consumer")):
            message = exc.__class__.__name__
        live_error = message[:180] or exc.__class__.__name__
        print(f"live inquiries unavailable: {live_error}")
    try:
        ga4 = fetch_ga4()
    except Exception as exc:
        ga4 = empty_ga4(type(exc).__name__)
        print(f"ga4 unavailable: {type(exc).__name__}")
    payload = build_payload(tables, bt.stamp(bt.beijing_now()), live, live_error, ga4)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(OUT)
    os.chmod(OUT, 0o600)
    ladder = payload["ladder"]
    inquiries = payload["inquiries"]
    gsc = payload["gsc"]
    print(f"wrote {OUT}")
    print(f"L0 {ladder['L0']} L1 {ladder['L1']} L2 {ladder['L2']} L3 {ladder['L3']} "
          f"inquiries {inquiries['total']} issued {inquiries['issued']} attributed {inquiries['attributed']}")
    print(f"index {gsc['indexRows']} performance {gsc['performanceRows']} queries {gsc['queryRows']}")
    print(f"status {inquiries['byStatus']}")
    print(f"inquiry items {len(inquiries['items'])} live error {inquiries['liveError'] or 'none'}")
    return 0


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send(self, code: int, body: bytes, content_type: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html"):
            self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
            return
        if path == "/data.json":
            if not OUT.exists():
                body = json.dumps({"error": "还没有导出"}).encode()
                self._send(404, body, "application/json; charset=utf-8")
                return
            self._send(200, OUT.read_bytes(), "application/json; charset=utf-8")
            return
        self._send(404, b"not found", "text/plain; charset=utf-8")


def open_page() -> int:
    if not OUT.exists():
        print(f"missing {OUT}; run: uv run scripts/dashboard.py export", file=sys.stderr)
        return 1
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://{HOST}:{PORT}/"
    print(url)
    webbrowser.open(url)
    try:
        thread.join()
    except KeyboardInterrupt:
        server.shutdown()
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("self-check")
    sub.add_parser("export")
    sub.add_parser("open")
    args = ap.parse_args()
    if args.command == "self-check":
        sys.exit(self_check())
    if args.command == "export":
        sys.exit(export())
    sys.exit(open_page())


if __name__ == "__main__":
    main()
