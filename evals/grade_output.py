"""Grade skill output against eval assertions."""
from __future__ import annotations

from pathlib import Path


def create_grading_template(assertions: list[str], output_dir: Path | None = None) -> dict:
    """Create an empty grading template for a grader to fill."""
    return {
        "expectations": [
            {"text": a, "passed": None, "evidence": ""} for a in assertions
        ],
        "summary": {"passed": 0, "failed": 0, "total": len(assertions), "pass_rate": 0.0},
        "execution_metrics": {},
        "timing": {},
        "claims": [],
        "user_notes_summary": {"uncertainties": [], "needs_review": [], "workarounds": []},
        "eval_feedback": {"suggestions": [], "overall": ""},
    }


def finalize_grading(grading: dict) -> dict:
    """Calculate summary stats from filled-in expectations."""
    expectations = grading["expectations"]
    passed = sum(1 for e in expectations if e.get("passed") is True)
    failed = sum(1 for e in expectations if e.get("passed") is False)
    total = len(expectations)
    grading["summary"] = {
        "passed": passed,
        "failed": failed,
        "total": total,
        "pass_rate": round(passed / total, 2) if total > 0 else 0.0,
    }
    return grading
