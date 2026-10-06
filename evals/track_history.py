"""
Track eval history across skill executions.

History lives at deliverables/marketing/00-system/eval-history/history.json.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path


def _history_file(project_root: str | Path) -> Path:
    return (
        Path(project_root)
        / "deliverables"
        / "marketing"
        / "00-system"
        / "eval-history"
        / "history.json"
    )


def update_history(project_root: str | Path, skill_name: str, grading: dict) -> dict:
    """Append a grading result to the skill's history."""
    history_file = _history_file(project_root)
    history_file.parent.mkdir(parents=True, exist_ok=True)
    if history_file.exists():
        history = json.loads(history_file.read_text(encoding="utf-8"))
    else:
        history = {"skills": {}}
    if skill_name not in history["skills"]:
        history["skills"][skill_name] = {"runs": [], "best_pass_rate": 0.0}
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pass_rate": grading.get("summary", {}).get("pass_rate", 0.0),
        "passed": grading.get("summary", {}).get("passed", 0),
        "total": grading.get("summary", {}).get("total", 0),
    }
    history["skills"][skill_name]["runs"].append(entry)
    if entry["pass_rate"] > history["skills"][skill_name]["best_pass_rate"]:
        history["skills"][skill_name]["best_pass_rate"] = entry["pass_rate"]
    history_file.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return history


def get_trend(project_root: str | Path, skill_name: str) -> str:
    """Return trend indicator for a skill's eval history."""
    history_file = _history_file(project_root)
    if not history_file.exists():
        return "no_data"
    history = json.loads(history_file.read_text(encoding="utf-8"))
    runs = history.get("skills", {}).get(skill_name, {}).get("runs", [])
    if len(runs) < 2:
        return "insufficient_data"
    last = runs[-1]["pass_rate"]
    prev = runs[-2]["pass_rate"]
    if last > prev:
        return "improving"
    if last < prev:
        return "declining"
    return "stable"


def weakest_skill(project_root: str | Path) -> tuple[str, float]:
    """Find the skill with lowest pass_rate across all runs."""
    history_file = _history_file(project_root)
    if not history_file.exists():
        return "", 0.0
    history = json.loads(history_file.read_text(encoding="utf-8"))
    worst_skill, worst_rate = "", 1.0
    for name, data in history.get("skills", {}).items():
        runs = data.get("runs", [])
        if runs and runs[-1]["pass_rate"] < worst_rate:
            worst_rate = runs[-1]["pass_rate"]
            worst_skill = name
    return worst_skill, worst_rate


def needs_eval(project_root: str | Path, staleness_days: int = 30) -> list[str]:
    """Find skills not evaluated within staleness_days."""
    history_file = _history_file(project_root)
    if not history_file.exists():
        return []
    history = json.loads(history_file.read_text(encoding="utf-8"))
    stale = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=staleness_days)
    for name, data in history.get("skills", {}).items():
        runs = data.get("runs", [])
        if not runs:
            stale.append(name)
        elif datetime.fromisoformat(runs[-1]["timestamp"]) < cutoff:
            stale.append(name)
    return stale
