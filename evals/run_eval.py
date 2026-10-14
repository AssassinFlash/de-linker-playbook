#!/usr/bin/env python3
"""
Master eval runner.

Runs project-level checks and writes a report under
deliverables/marketing/00-system/eval-reports/.

Usage:
    python evals/run_eval.py [project_root]

Exit codes:
    0 = all checks passed
    1 = one or more checks failed
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def default_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def resolve_project_root(argv: list[str]) -> Path:
    positional = [a for a in argv[1:] if not a.startswith("-")]
    if positional:
        return Path(positional[0]).resolve()
    return default_project_root()


def run_script(project_root: Path, name: str) -> dict:
    script = project_root / "evals" / f"{name}.py"
    result = subprocess.run(
        [sys.executable, str(script), str(project_root)],
        capture_output=True,
        text=True,
    )
    return {
        "name": name,
        "passed": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


LEDGERS = ("state/marketing-status.md", "state/lead-status.md")


def check_ledger(project_root: Path) -> dict:
    missing = [rel for rel in LEDGERS if not (project_root / rel).exists()]
    return {
        "name": "ledger",
        "passed": not missing,
        "details": "Found " + ", ".join(LEDGERS) if not missing else "Missing " + ", ".join(missing),
    }


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv if argv is None else argv)
    if "-h" in argv or "--help" in argv:
        print("Usage: python evals/run_eval.py [project_root]")
        return 0

    project_root = resolve_project_root(argv)
    report_dir = (
        project_root / "deliverables" / "marketing" / "00-system" / "eval-reports"
    )
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_file = report_dir / f"eval-report-{timestamp}.json"

    checks = [
        run_script(project_root, "validate_project"),
        run_script(project_root, "validate_deliverables"),
        check_ledger(project_root),
    ]

    passed = sum(1 for c in checks if c["passed"])
    failed = sum(1 for c in checks if not c["passed"])

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "project_root": str(project_root),
        "summary": {"passed": passed, "failed": failed, "total": len(checks)},
        "checks": checks,
    }

    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'=' * 60}")
    print(f"Eval Report: {report_file}")
    print(f"Passed: {passed}/{len(checks)}")
    if failed:
        print(f"Failed: {failed}")
        for c in checks:
            if not c["passed"]:
                print(f"  FAIL {c['name']}")
                if "details" in c:
                    print(f"     {c['details']}")
                if "stdout" in c:
                    print(c["stdout"])
        return 1
    print("All eval checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
