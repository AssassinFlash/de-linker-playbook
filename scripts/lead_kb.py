#!/usr/bin/env python3
"""Maintain the private lead-learning knowledge base.

The JSON file is the machine-readable source of truth. The HTML knowledge
workbench reads it directly when served by ``scripts/lead_academy.py``.
"""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
KB_LINK_PATH = (
    ROOT
    / "deliverables"
    / "lead"
    / "00-system"
    / "knowledge"
    / "knowledge-base.json"
)
KB_PATH = KB_LINK_PATH.resolve()
LEAD_ROOT = KB_PATH.parents[2]
VAULT_ROOT = next(
    (parent for parent in KB_PATH.parents if (parent / ".obsidian").is_dir()),
    None,
)
TZ = ZoneInfo("Asia/Shanghai")


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def display_time() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d %H:%M")


def load() -> dict[str, Any]:
    if VAULT_ROOT is None:
        raise SystemExit(f"知识库不在 Obsidian vault 内：{KB_PATH}")
    return json.loads(KB_PATH.read_text(encoding="utf-8"))


def save(data: dict[str, Any]) -> None:
    data["updated_at"] = now_iso()
    KB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=KB_PATH.parent,
        prefix=".knowledge-base.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temp_path = Path(handle.name)
    os.replace(temp_path, KB_PATH)


def next_id(data: dict[str, Any], collection: str, prefix: str) -> str:
    day = datetime.now(TZ).strftime("%Y%m%d")
    stem = f"{prefix}-{day}-"
    used = {
        item["id"]
        for item in data.get(collection, [])
        if item.get("id", "").startswith(stem)
    }
    number = 1
    while f"{stem}{number:03d}" in used:
        number += 1
    return f"{stem}{number:03d}"


def split_values(values: list[str] | None) -> list[str]:
    result: list[str] = []
    for value in values or []:
        result.extend(part.strip() for part in value.split(",") if part.strip())
    return list(dict.fromkeys(result))


EVIDENCE_FIELDS = (
    "claim",
    "type",
    "role",
    "source_url",
    "document_id",
    "excerpt",
    "confidence",
    "tags",
    "status",
)


def evidence_score(item: dict[str, Any], topics: list[str]) -> int:
    haystack = " ".join(
        str(value)
        for value in (
            item.get("claim"),
            item.get("excerpt"),
            item.get("type"),
            item.get("role"),
            " ".join(item.get("tags", [])),
            " ".join(item.get("skills", [])),
        )
    ).casefold()
    score = sum(1 for topic in topics if topic.casefold() in haystack)
    if item.get("confidence") == "high":
        score += 2
    elif item.get("confidence") == "medium":
        score += 1
    return score


def validate_data(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if VAULT_ROOT is None or VAULT_ROOT not in KB_PATH.parents:
        errors.append(f"knowledge-base.json 未解析到 Obsidian vault：{KB_PATH}")
    ids: set[str] = set()
    for collection in ("documents", "evidence", "questions", "feedback"):
        for item in data.get(collection, []):
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{collection}: item without id")
                continue
            if item_id in ids:
                errors.append(f"duplicate id: {item_id}")
            ids.add(item_id)

    documents = {item["id"]: item for item in data.get("documents", [])}
    evidence = {item["id"] for item in data.get("evidence", [])}
    for item in data.get("documents", []):
        vault_path = LEAD_ROOT / item.get("vault_path", "")
        if not vault_path.is_file():
            errors.append(f"{item['id']}: vault document missing: {vault_path}")
    for item in data.get("evidence", []):
        doc_id = item.get("document_id")
        if doc_id and doc_id not in documents:
            errors.append(f"{item['id']}: unknown document_id {doc_id}")
        if not item.get("source_url") and not doc_id:
            errors.append(f"{item['id']}: needs source_url or document_id")
    for item in data.get("questions", []):
        for evidence_id in item.get("evidence_ids", []):
            if evidence_id not in evidence:
                errors.append(f"{item['id']}: unknown evidence_id {evidence_id}")
        for group, group_ids in item.get("option_evidence", {}).items():
            for evidence_id in group_ids:
                if evidence_id not in evidence:
                    errors.append(
                        f"{item['id']}: option {group} has unknown evidence_id {evidence_id}"
                    )
        for evidence_id in item.get("resulting_evidence_ids", []):
            if evidence_id not in evidence:
                errors.append(
                    f"{item['id']}: unknown resulting_evidence_id {evidence_id}"
                )
    for item in data.get("feedback", []):
        for evidence_id in item.get("affected_evidence_ids", []):
            if evidence_id not in evidence:
                errors.append(
                    f"{item['id']}: unknown affected_evidence_id {evidence_id}"
                )
    return errors


def print_summary(data: dict[str, Any]) -> None:
    print(f"逻辑路径：{KB_LINK_PATH}")
    print(f"Obsidian 实路径：{KB_PATH}")
    print(f"Obsidian 根：{VAULT_ROOT}")
    print(f"资料 {len(data.get('documents', []))} 份")
    active = sum(
        1 for item in data.get("evidence", []) if item.get("status") == "active"
    )
    archived = sum(
        1
        for item in data.get("evidence", [])
        if item.get("status") in {"archived", "superseded"}
    )
    print(f"证据 {len(data.get('evidence', []))} 条（active {active}，archived/superseded {archived}）")
    print(f"问题 {len(data.get('questions', []))} 个")
    print(f"反馈 {len(data.get('feedback', []))} 条")
    print(f"最近更新：{data.get('updated_at', '')}")


def search_items(data: dict[str, Any], query: str) -> list[dict[str, Any]]:
    needle = query.casefold()
    hits: list[dict[str, Any]] = []
    for doc in data.get("documents", []):
        haystack = " ".join(
            str(value)
            for value in (
                doc.get("id"),
                doc.get("title"),
                doc.get("summary"),
                doc.get("vault_path"),
                " ".join(doc.get("topics", [])),
            )
        )
        if needle in haystack.casefold():
            hits.append({"collection": "documents", **doc})
    for item in data.get("evidence", []):
        haystack = " ".join(
            str(value)
            for value in (
                item.get("id"),
                item.get("claim"),
                item.get("excerpt"),
                item.get("type"),
                item.get("role"),
                " ".join(item.get("tags", [])),
            )
        )
        if needle in haystack.casefold():
            hits.append({"collection": "evidence", **item})
    for item in data.get("questions", []):
        haystack = " ".join(
            str(value)
            for value in (
                item.get("id"),
                item.get("text"),
                item.get("answer"),
                item.get("assessment"),
                " ".join(item.get("evidence_ids", [])),
            )
        )
        if needle in haystack.casefold():
            hits.append({"collection": "questions", **item})
    for item in data.get("feedback", []):
        haystack = " ".join(
            str(value)
            for value in (
                item.get("id"),
                item.get("text"),
                item.get("decision"),
                " ".join(item.get("applied_to", [])),
            )
        )
        if needle in haystack.casefold():
            hits.append({"collection": "feedback", **item})
    return hits


def format_search_hit(hit: dict[str, Any]) -> str:
    collection = hit.get("collection")
    item_id = hit.get("id", "")
    if collection == "evidence":
        return f"{item_id} [证据/{hit.get('type')}/{hit.get('role')}] {hit.get('claim')}"
    if collection == "documents":
        return f"{item_id} [资料] {hit.get('title')} — {hit.get('vault_path')}"
    if collection == "questions":
        return f"{item_id} [问题/{hit.get('status')}] {hit.get('text')}"
    return f"{item_id} [反馈] {hit.get('text')}"


def cmd_summary(_: argparse.Namespace) -> int:
    print_summary(load())
    return 0


def cmd_validate(_: argparse.Namespace) -> int:
    data = load()
    errors = validate_data(data)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    data["validation"] = {
        "valid": True,
        "validated_at": now_iso(),
        "logical_path": str(KB_LINK_PATH),
        "real_path": str(KB_PATH),
        "vault_root": str(VAULT_ROOT),
        "document_count": len(data.get("documents", [])),
    }
    save(data)
    print("OK knowledge-base.json is valid")
    print_summary(data)
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    data = load()
    hits = search_items(data, args.query)
    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return 0
    if not hits:
        print("没有匹配项")
        return 0
    for hit in hits:
        print(format_search_hit(hit))
    return 0


def cmd_trace_question(args: argparse.Namespace) -> int:
    data = load()
    question = next(
        (item for item in data.get("questions", []) if item["id"] == args.id),
        None,
    )
    if question is None:
        raise SystemExit(f"没有这个问题：{args.id}")
    evidence_by_id = {item["id"]: item for item in data.get("evidence", [])}
    documents = {item["id"]: item for item in data.get("documents", [])}
    print(f"{question['id']} [{question['status']}] {question['text']}")
    print(f"问题类型：{question['question_type']}")
    if question.get("knowledge_snapshot"):
        print(f"知识快照：{question['knowledge_snapshot']}")
    if question.get("selection_rationale"):
        print(f"选题依据：{question['selection_rationale']}")
    if question.get("target_company_context"):
        print("目标身份卡：")
        print(json.dumps(question["target_company_context"], ensure_ascii=False, indent=2))
    if question.get("analysis_chain"):
        print("分析链路：")
        for step in question["analysis_chain"]:
            name = step.get("step", "step")
            detail = {
                key: value
                for key, value in step.items()
                if key not in {"step", "method"}
            }
            method = f" — {step['method']}" if step.get("method") else ""
            print(f"- {name}{method}")
            if detail:
                print(f"  {json.dumps(detail, ensure_ascii=False)}")
    if question.get("option_evidence"):
        print("选项证据：")
        for group, group_ids in question["option_evidence"].items():
            print(f"- {group}: {', '.join(group_ids)}")
    for evidence_id in question.get("evidence_ids", []):
        item = evidence_by_id.get(evidence_id)
        if item is None:
            print(f"- {evidence_id}: MISSING")
            continue
        doc = documents.get(item.get("document_id"))
        vault_path = LEAD_ROOT / doc["vault_path"] if doc else None
        print(f"- {evidence_id} [{item['type']}/{item['role']}] {item['claim']}")
        if doc:
            print(f"  资料：{doc['title']} ({doc['vault_path']})")
        if vault_path:
            print(f"  vault 文件：{vault_path} — {'OK' if vault_path.is_file() else 'MISSING'}")
        if item.get("source_url"):
            print(f"  来源：{item['source_url']}")
    if question.get("evidence_gaps"):
        print("证据缺口：")
        for gap in question["evidence_gaps"]:
            print(f"- {gap}")
    return 0


def cmd_brief(args: argparse.Namespace) -> int:
    data = load()
    topics = split_values(args.topic)
    role = args.role or ""
    candidates = [
        item
        for item in data.get("evidence", [])
        if item.get("status") == "active" and (not role or item.get("role") == role)
    ]
    if topics:
        candidates = [
            item for item in candidates if evidence_score(item, topics) > 0
        ]
    candidates.sort(
        key=lambda item: (
            evidence_score(item, topics),
            {"high": 3, "medium": 2, "low": 1}.get(item.get("confidence"), 0),
            item.get("id", ""),
        ),
        reverse=True,
    )
    candidates = candidates[: args.limit]
    documents = {item["id"]: item for item in data.get("documents", [])}
    payload = []
    for item in candidates:
        doc = documents.get(item.get("document_id"))
        payload.append(
            {
                "id": item["id"],
                "claim": item["claim"],
                "type": item["type"],
                "role": item["role"],
                "confidence": item["confidence"],
                "tags": item.get("tags", []),
                "document_id": item.get("document_id", ""),
                "vault_path": doc.get("vault_path", "") if doc else "",
                "source_url": item.get("source_url", ""),
            }
        )
    result = {
        "skill": args.skill,
        "topics": topics,
        "role": role or "all",
        "knowledge_updated_at": data.get("updated_at"),
        "evidence": payload,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    print(f"知识库检索 — {args.skill}")
    print(f"主题：{', '.join(topics) if topics else '全部'}；角色：{role or '全部'}")
    if not payload:
        print("没有匹配的 active 证据；应创建新调研任务，不得凭记忆提问。")
        return 0
    for item in payload:
        print(
            f"- {item['id']} [{item['type']}/{item['role']}/{item['confidence']}] "
            f"{item['claim']}"
        )
        if item["vault_path"]:
            print(f"  {item['vault_path']}")
    return 0


def update_evidence_record(
    data: dict[str, Any],
    evidence_id: str,
    changes: dict[str, Any],
    reason: str,
) -> dict[str, Any]:
    item = next(
        (entry for entry in data.get("evidence", []) if entry["id"] == evidence_id),
        None,
    )
    if item is None:
        raise SystemExit(f"没有这条证据：{evidence_id}")
    before = {key: item.get(key) for key in changes}
    item.setdefault("revision_history", []).append(
        {
            "changed_at": now_iso(),
            "reason": reason,
            "before": before,
            "after": changes,
        }
    )
    item.update(changes)
    item["updated_at"] = now_iso()
    return item


def cmd_update_evidence(args: argparse.Namespace) -> int:
    data = load()
    changes: dict[str, Any] = {}
    for field in ("claim", "type", "role", "source_url", "document_id", "excerpt", "confidence", "status"):
        value = getattr(args, field)
        if value is not None:
            changes[field] = value
    if args.tag is not None:
        changes["tags"] = split_values(args.tag)
    if not changes:
        raise SystemExit("至少要改一个字段")
    item = update_evidence_record(data, args.id, changes, args.reason)
    errors = validate_data(data)
    if errors:
        raise SystemExit("\n".join(errors))
    save(data)
    print(f"已更新 {item['id']}；修订历史 {len(item.get('revision_history', []))} 条")
    return 0


def cmd_archive_evidence(args: argparse.Namespace) -> int:
    data = load()
    changes = {
        "status": "archived",
        "archived_reason": args.reason,
    }
    item = update_evidence_record(data, args.id, changes, args.reason)
    save(data)
    print(f"已归档 {item['id']}，后续检索不会再使用")
    return 0


def cmd_add_feedback(args: argparse.Namespace) -> int:
    data = load()
    item = {
        "id": next_id(data, "feedback", "F"),
        "created_at": now_iso(),
        "source": args.source,
        "text": args.text,
        "scope": args.scope,
        "decision": args.decision,
        "applied_to": split_values(args.applied_to),
        "affected_evidence_ids": split_values(args.evidence),
        "status": args.status,
    }
    data.setdefault("feedback", []).append(item)
    errors = validate_data(data)
    if errors:
        raise SystemExit("\n".join(errors))
    save(data)
    print(f"已写入 {item['id']}: {item['text']}")
    return 0


def cmd_add_question(args: argparse.Namespace) -> int:
    data = load()
    evidence_ids = split_values(args.evidence)
    known = {item["id"] for item in data.get("evidence", [])}
    missing = [item for item in evidence_ids if item not in known]
    if missing:
        raise SystemExit(f"未知证据 ID：{', '.join(missing)}")
    inactive = [
        item["id"]
        for item in data.get("evidence", [])
        if item["id"] in evidence_ids and item.get("status") != "active"
    ]
    if inactive:
        raise SystemExit(f"问题不能引用非 active 证据：{', '.join(inactive)}")
    item = {
        "id": next_id(data, "questions", "Q"),
        "created_at": now_iso(),
        "asked_at": now_iso(),
        "skill": args.skill,
        "text": args.text,
        "question_type": args.type,
        "evidence_ids": evidence_ids,
        "selection_rationale": args.rationale,
        "knowledge_snapshot": data.get("updated_at", ""),
        "analysis_chain": [
            {
                "step": "retrieve",
                "method": "只从 active evidence 中选择与问题主题相关的证据",
                "evidence_ids": evidence_ids,
            },
            {
                "step": "ask",
                "method": args.rationale,
            },
        ],
        "option_evidence": {},
        "evidence_gaps": [],
        "status": args.status,
        "answer": "",
        "assessment": "",
        "resulting_evidence_ids": [],
    }
    data.setdefault("questions", []).append(item)
    save(data)
    print(f"已登记 {item['id']}")
    return 0


def cmd_update_question(args: argparse.Namespace) -> int:
    data = load()
    question = next(
        (item for item in data.get("questions", []) if item["id"] == args.id),
        None,
    )
    if question is None:
        raise SystemExit(f"没有这个问题：{args.id}")
    try:
        payload = json.loads(args.json)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON 无效：{exc}") from exc
    allowed = {
        "text",
        "question_type",
        "selection_rationale",
        "target_company_context",
        "option_labels",
        "evidence_ids",
        "option_evidence",
        "analysis_chain",
        "evidence_gaps",
        "status",
    }
    changes = {key: value for key, value in payload.items() if key in allowed}
    if not changes:
        raise SystemExit("没有可更新字段")
    before = {key: question.get(key) for key in changes}
    question.setdefault("revision_history", []).append(
        {
            "changed_at": now_iso(),
            "reason": args.reason,
            "before": before,
            "after": changes,
        }
    )
    question.update(changes)
    question["updated_at"] = now_iso()
    errors = validate_data(data)
    if errors:
        raise SystemExit("\n".join(errors))
    save(data)
    print(f"已更新 {args.id}；修订历史 {len(question['revision_history'])} 条")
    return 0


def cmd_answer_question(args: argparse.Namespace) -> int:
    data = load()
    question = next(
        (item for item in data.get("questions", []) if item["id"] == args.id),
        None,
    )
    if question is None:
        raise SystemExit(f"没有这个问题：{args.id}")
    question.update(
        {
            "answered_at": now_iso(),
            "answer": args.answer,
            "assessment": args.assessment,
            "status": args.status,
            "resulting_evidence_ids": split_values(args.evidence),
        }
    )
    errors = validate_data(data)
    if errors:
        raise SystemExit("\n".join(errors))
    save(data)
    print(f"已回写 {args.id}")
    return 0


def cmd_add_evidence(args: argparse.Namespace) -> int:
    data = load()
    doc_id = args.document_id
    if doc_id and doc_id not in {item["id"] for item in data.get("documents", [])}:
        raise SystemExit(f"未知资料 ID：{doc_id}")
    item = {
        "id": next_id(data, "evidence", "E"),
        "created_at": now_iso(),
        "claim": args.claim,
        "type": args.type,
        "role": args.role,
        "source_url": args.source_url or "",
        "document_id": doc_id or "",
        "excerpt": args.excerpt or "",
        "confidence": args.confidence,
        "tags": split_values(args.tag),
        "skills": split_values(args.skill),
        "status": args.status,
        "updated_at": now_iso(),
        "revision_history": [],
    }
    data.setdefault("evidence", []).append(item)
    save(data)
    print(f"已写入 {item['id']}: {item['claim']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_summary = sub.add_parser("summary", help="显示知识库数量")
    p_summary.set_defaults(func=cmd_summary)

    p_validate = sub.add_parser("validate", help="检查 ID 和引用")
    p_validate.set_defaults(func=cmd_validate)

    p_search = sub.add_parser("search", help="搜索全部知识库")
    p_search.add_argument("query")
    p_search.add_argument("--json", action="store_true")
    p_search.set_defaults(func=cmd_search)

    p_trace = sub.add_parser("trace-question", help="展开问题的证据和 vault 文件")
    p_trace.add_argument("id")
    p_trace.set_defaults(func=cmd_trace_question)

    p_brief = sub.add_parser("brief", help="为当前方法检索一组可引用证据")
    p_brief.add_argument("--skill", default="lead-icp-analysis")
    p_brief.add_argument("--topic", action="append", default=[])
    p_brief.add_argument("--role", default="")
    p_brief.add_argument("--limit", type=int, default=12)
    p_brief.add_argument("--json", action="store_true")
    p_brief.set_defaults(func=cmd_brief)

    p_feedback = sub.add_parser("add-feedback", help="写入操作者或系统反馈")
    p_feedback.add_argument("--text", required=True)
    p_feedback.add_argument("--source", default="operator")
    p_feedback.add_argument("--scope", default="lead-teach")
    p_feedback.add_argument("--decision", required=True)
    p_feedback.add_argument("--applied-to", action="append", default=[])
    p_feedback.add_argument("--evidence", action="append", default=[])
    p_feedback.add_argument("--status", default="applied")
    p_feedback.set_defaults(func=cmd_add_feedback)

    p_question = sub.add_parser("add-question", help="登记即将提问的问题")
    p_question.add_argument("--skill", default="lead-icp-analysis")
    p_question.add_argument("--text", required=True)
    p_question.add_argument("--type", default="evidence_synthesis")
    p_question.add_argument("--evidence", action="append", default=[])
    p_question.add_argument("--rationale", required=True)
    p_question.add_argument("--status", default="asked")
    p_question.set_defaults(func=cmd_add_question)

    p_answer = sub.add_parser("answer-question", help="回写用户回答和判断")
    p_answer.add_argument("id")
    p_answer.add_argument("--answer", required=True)
    p_answer.add_argument("--assessment", required=True)
    p_answer.add_argument("--status", default="answered")
    p_answer.add_argument("--evidence", action="append", default=[])
    p_answer.set_defaults(func=cmd_answer_question)

    p_update_question = sub.add_parser("update-question", help="更新问题分析快照并保留历史")
    p_update_question.add_argument("id")
    p_update_question.add_argument("--json", required=True)
    p_update_question.add_argument("--reason", required=True)
    p_update_question.set_defaults(func=cmd_update_question)

    p_evidence = sub.add_parser("add-evidence", help="追加入库证据")
    p_evidence.add_argument("--claim", required=True)
    p_evidence.add_argument("--type", required=True)
    p_evidence.add_argument("--role", required=True)
    p_evidence.add_argument("--source-url", default="")
    p_evidence.add_argument("--document-id", default="")
    p_evidence.add_argument("--excerpt", default="")
    p_evidence.add_argument("--confidence", default="medium")
    p_evidence.add_argument("--tag", action="append", default=[])
    p_evidence.add_argument("--skill", action="append", default=[])
    p_evidence.add_argument("--status", default="active")
    p_evidence.set_defaults(func=cmd_add_evidence)

    p_update = sub.add_parser("update-evidence", help="修订证据并保留历史")
    p_update.add_argument("id")
    p_update.add_argument("--claim")
    p_update.add_argument("--type")
    p_update.add_argument("--role")
    p_update.add_argument("--source-url")
    p_update.add_argument("--document-id")
    p_update.add_argument("--excerpt")
    p_update.add_argument("--confidence")
    p_update.add_argument("--tag", action="append")
    p_update.add_argument("--status", choices=["active", "disputed", "superseded", "archived"])
    p_update.add_argument("--reason", required=True)
    p_update.set_defaults(func=cmd_update_evidence)

    p_archive = sub.add_parser("archive-evidence", help="从检索中归档证据")
    p_archive.add_argument("id")
    p_archive.add_argument("--reason", required=True)
    p_archive.set_defaults(func=cmd_archive_evidence)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
