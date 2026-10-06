#!/usr/bin/env python3
"""
Verify Collect phase produced sufficient data before dispatch.

Usage:
    python evals/verify_collect.py <collected_data.json> [phase_level]

Exit codes:
    0 = PASS — data collection sufficient
    1 = FAIL — data collection insufficient (do not dispatch)
    2 = usage error
"""
import json
import sys
from pathlib import Path

MIN_REQUIREMENTS = {
    "foundation": {"data_points": 30, "tool_calls": 50, "sources": 5},
    "seo_content": {"data_points": 20, "tool_calls": 30, "sources": 4},
    "cro_growth": {"data_points": 15, "tool_calls": 10, "sources": 3},
}


def verify_collect(collected_data: dict, phase_level: str = "foundation") -> dict:
    """
    Verify collected data meets minimum requirements.
    Returns verdict with pass/fail and specific gaps.
    """
    reqs = MIN_REQUIREMENTS.get(phase_level, MIN_REQUIREMENTS["cro_growth"])

    data_points = len(collected_data.get("data_points", []))
    tool_calls = collected_data.get("tool_calls", {}).get("total", 0)
    sources = len(set(
        dp.get("source", "") for dp in collected_data.get("data_points", [])
        if dp.get("source")
    ))

    gaps = []
    if data_points < reqs["data_points"]:
        gaps.append(f"数据点不足: {data_points}/{reqs['data_points']}")
    if tool_calls < reqs["tool_calls"]:
        gaps.append(f"工具调用不足: {tool_calls}/{reqs['tool_calls']}")
    if sources < reqs["sources"]:
        gaps.append(f"数据源不足: {sources}/{reqs['sources']}")

    empty_count = sum(
        1 for dp in collected_data.get("data_points", [])
        if not dp.get("data") or dp.get("verified") is False
    )
    if data_points > 0 and empty_count > data_points * 0.3:
        gaps.append(
            f"空/无效数据点过多: {empty_count}/{data_points} "
            f"({empty_count / max(data_points, 1) * 100:.0f}%)"
        )

    tiers = collected_data.get("tool_calls", {}).get("by_tier", {})
    if not tiers.get("T1", 0) and not tiers.get("T2", 0):
        gaps.append("基础搜索层未使用——至少要用网页搜索查证")

    passed = len(gaps) == 0
    verdict = {
        "passed": passed,
        "phase_level": phase_level,
        "data_points": data_points,
        "required_data_points": reqs["data_points"],
        "tool_calls": tool_calls,
        "required_tool_calls": reqs["tool_calls"],
        "sources": sources,
        "required_sources": reqs["sources"],
        "gaps": gaps,
        "verdict": "PASS — 数据采集达标，可以继续" if passed
                   else f"FAIL — {len(gaps)} 项不达标",
    }

    verdict_path = Path("/tmp/collect-verdict.json")
    verdict_path.write_text(json.dumps(verdict, ensure_ascii=False, indent=2))

    return verdict


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: python evals/verify_collect.py <collected_data.json> [foundation|seo_content|cro_growth]")
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"} else 2)

    data_file = Path(sys.argv[1])
    if not data_file.exists():
        print(f"File not found: {data_file}")
        sys.exit(2)

    phase = sys.argv[2] if len(sys.argv) > 2 else "foundation"

    try:
        collected = json.loads(data_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(2)

    result = verify_collect(collected, phase)
    print(result["verdict"])
    print(f"  数据点: {result['data_points']}/{result['required_data_points']}")
    print(f"  工具调用: {result['tool_calls']}/{result['required_tool_calls']}")
    print(f"  数据源: {result['sources']}/{result['required_sources']}")

    if not result["passed"]:
        print("\nSTOP — do not continue. Fix gaps first:")
        for gap in result["gaps"]:
            print(f"  -> {gap}")
        sys.exit(1)

    sys.exit(0)
