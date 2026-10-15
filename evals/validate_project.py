#!/usr/bin/env python3
"""
Project validation for this playbook.

Validates:
- Canonical skills in skills/<name>/SKILL.md
- Frontmatter only name + description (optional license, metadata)
- name matches ^(marketing|lead)- and the directory
- description 300-700 characters
- JSON schema files and skill JSON references
- Excel names mentioned in skills exist in templates/
- Optional: .agents/skills/<name> symlink layer

Usage:
    python evals/validate_project.py [project_root]

Exit codes:
    0 = all checks passed
    1 = one or more checks failed
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
if str(EVALS_DIR) not in sys.path:
    sys.path.insert(0, str(EVALS_DIR))

from utils import collapsed_len, parse_frontmatter_and_body  # noqa: E402
from validate_deliverables import (  # noqa: E402
    json_reference_schema_errors,
    validate_schema_files,
)


def default_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


ALLOWED_SKILL_KEYS = {"name", "description", "license", "metadata"}
NAME_RE = re.compile(r"^(marketing|lead)-[a-z0-9]+(-[a-z0-9]+)*$")
DESC_MIN = 300
DESC_MAX = 700
SUPPORT_REF_PATTERN = re.compile(
    r"(?<![\w/-])((?:references|scripts|assets)/[\w./-]+)"
)


def resolve_project_root(argv: list[str]) -> Path:
    positional = [a for a in argv[1:] if not a.startswith("-")]
    if positional:
        return Path(positional[0]).resolve()
    return default_project_root()


def log(level: str, message: str):
    prefix = {"info": "  ", "ok": "OK", "warn": "WARN", "error": "ERROR"}.get(level, "  ")
    print(f"{prefix} {message}")


def validate_kebab_case(name: str, context: str) -> list[str]:
    errors = []
    if not NAME_RE.match(name):
        errors.append(
            f"{context} name '{name}' must match ^(marketing|lead)- and be kebab-case"
        )
    if len(name) > 64:
        errors.append(f"{context} name '{name}' is too long ({len(name)} > 64)")
    return errors


def validate_skills(project_root: Path) -> tuple[int, set[str]]:
    print("\nValidating skills...")
    errors = 0
    skills_dir = project_root / "skills"
    if not skills_dir.exists():
        log("error", f"Skills directory not found: {skills_dir}")
        return 1, set()

    skill_names: set[str] = set()
    for skill_path in sorted(skills_dir.iterdir()):
        if not skill_path.is_dir():
            continue
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            log("error", f"SKILL.md missing: {skill_path}")
            errors += 1
            continue

        frontmatter, _body = parse_frontmatter_and_body(
            skill_md.read_text(encoding="utf-8")
        )
        if not frontmatter:
            log("error", f"Invalid frontmatter in {skill_md}")
            errors += 1
            continue

        unexpected = set(frontmatter.keys()) - ALLOWED_SKILL_KEYS
        if unexpected:
            log(
                "error",
                f"Forbidden frontmatter key(s) in {skill_md}: {', '.join(sorted(unexpected))}",
            )
            errors += 1

        name = frontmatter.get("name", "")
        if not name:
            log("error", f"Missing 'name' in {skill_md}")
            errors += 1
        else:
            name = str(name)
            for err in validate_kebab_case(name, "Skill"):
                log("error", f"{skill_md}: {err}")
                errors += 1
            if name != skill_path.name:
                log(
                    "error",
                    f"Skill name '{name}' does not match directory '{skill_path.name}'",
                )
                errors += 1
            skill_names.add(name)

        description = frontmatter.get("description", "")
        if not description:
            log("error", f"Missing 'description' in {skill_md}")
            errors += 1
        elif not isinstance(description, str):
            log("error", f"'description' must be string in {skill_md}")
            errors += 1
        else:
            length = collapsed_len(description)
            if "<" in description or ">" in description:
                log("error", f"Description contains angle brackets in {skill_md}")
                errors += 1
            if not (DESC_MIN <= length <= DESC_MAX):
                log(
                    "error",
                    f"Description must be {DESC_MIN}-{DESC_MAX} characters "
                    f"(got {length}) in {skill_md}",
                )
                errors += 1

    log("info", f"Found {len(skill_names)} skills")
    return errors, skill_names


def validate_skill_symlinks(project_root: Path, existing_skills: set[str]) -> int:
    """Warn when the adapter symlink layer is missing or wrong. Never required."""
    print("\nChecking adapter symlinks...")
    warnings = 0
    adapters = project_root / ".agents" / "skills"
    skills_dir = project_root / "skills"
    if not adapters.exists():
        log("warn", f"Adapter directory not found (optional): {adapters}")
        return 1
    for name in sorted(existing_skills):
        link = adapters / name
        canonical = skills_dir / name
        if not link.exists():
            log("warn", f"Missing adapter symlink: {link}")
            warnings += 1
            continue
        if not link.is_symlink():
            log("warn", f"Adapter path is not a symlink: {link}")
            warnings += 1
            continue
        if link.resolve() != canonical.resolve():
            log("warn", f"Adapter symlink target mismatch: {link}")
            warnings += 1
    if warnings == 0:
        log("ok", f"Adapter symlinks present for {len(existing_skills)} skill(s)")
    else:
        log("warn", f"Found {warnings} adapter symlink warning(s)")
    return warnings


def validate_support_references(project_root: Path) -> int:
    print("\nChecking support-file references...")
    warnings = 0
    skills_dir = project_root / "skills"
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        seen = set()
        for match in SUPPORT_REF_PATTERN.finditer(text):
            ref = match.group(1).rstrip("`),.;")
            if "{" in ref or "}" in ref:
                continue
            if ref.endswith("/"):
                continue
            if ref in seen:
                continue
            seen.add(ref)
            target = skill_md.parent / ref
            if not target.exists():
                log("warn", f"{skill_md} references missing support file: {ref}")
                warnings += 1
    if warnings == 0:
        log("ok", "All checked support-file references resolve")
    else:
        log("warn", f"Found {warnings} missing support-file reference(s)")
    return warnings


def load_canonical_deliverables(project_root: Path) -> set[str]:
    templates = project_root / "templates"
    names = set()
    if templates.exists():
        for path in templates.glob("*.xlsx"):
            names.add(path.stem)
    return names


def validate_deliverable_references(project_root: Path) -> int:
    print("\nValidating deliverable references...")
    errors = 0
    allowed = load_canonical_deliverables(project_root)
    pattern = re.compile(r"([\w-]+)\.xlsx")
    skills_dir = project_root / "skills"
    if not skills_dir.exists():
        return 0
    for path in sorted(skills_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            name = match.group(1).strip("-")
            if allowed and name not in allowed:
                log("warn", f"{path} references unknown workbook: {match.group(1)}.xlsx")
                errors += 1
    if errors == 0:
        log("ok", "Workbook references match templates/ (or none found)")
    return 0


def validate_deliverable_quality(project_root: Path) -> int:
    print("\nValidating deliverable quality gates...")
    errors = 0
    for message in validate_schema_files(project_root) + json_reference_schema_errors(
        project_root
    ):
        log("error", message)
        errors += 1
    if errors == 0:
        log("ok", "JSON schema files are parseable")
        log("ok", "Promised JSON deliverables in skills/ have schema mappings")
    return errors


def validate_ledger(project_root: Path) -> int:
    print("\nChecking ledgers...")
    errors = 0
    for rel in ("state/marketing-status.md", "state/lead-status.md"):
        path = project_root / rel
        if not path.exists():
            log("error", f"Missing ledger: {path}")
            errors += 1
            continue
        text = path.read_text(encoding="utf-8")
        if "product_context" not in text:
            log("warn", f"{rel} has no product_context key")
        else:
            log("ok", f"Ledger {rel} present with product_context")
    if (project_root / "state" / "status.md").exists():
        log("error", "Old shared ledger state/status (pre-split) still exists; remove it")
        errors += 1
    errors += validate_loop(project_root)
    return errors


LOOP_KEYS = ("mode", "feedback_read_at", "current_action", "current_action_log")
LOOP_REFS = {
    "skills/marketing-orchestrator/SKILL.md": ("docs/feedback-rules.md", "scripts/next_step.py", "证据闸"),
    "skills/marketing-playbook-standards/SKILL.md": ("docs/feedback-rules.md", "证据闸"),
    "skills/marketing-orchestrator/references/dependency-graph.md": ("证据闸", "evidence_gate"),
}


def validate_loop(project_root: Path) -> int:
    """Operating loop wiring: ledger loop keys, rule/script references, evidence gate on approved deliverables."""
    errors = 0
    ledger = project_root / "state" / "marketing-status.md"
    if ledger.exists():
        head = ledger.read_text(encoding="utf-8").split("---")[1] if ledger.read_text(encoding="utf-8").startswith("---") else ""
        keys = {line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip() for line in head.splitlines() if ":" in line}
        missing = [k for k in LOOP_KEYS if k not in keys]
        if missing:
            log("error", f"state/marketing-status.md lacks loop keys: {', '.join(missing)}")
            errors += 1
        elif keys["mode"] not in ("冷启动", "运营"):
            log("error", f"state/marketing-status.md mode must be 冷启动 or 运营, got {keys['mode']!r}")
            errors += 1
        else:
            log("ok", "Marketing ledger has operating-loop keys")
    for rel in ("docs/feedback-rules.md", "scripts/next_step.py"):
        if not (project_root / rel).exists():
            log("error", f"Missing {rel}")
            errors += 1
    for rel, needles in LOOP_REFS.items():
        path = project_root / rel
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        lost = [n for n in needles if n not in text]
        if lost:
            log("error", f"{rel} does not mention: {', '.join(lost)}")
            errors += 1
    marketing = project_root / "deliverables" / "marketing"
    for path in sorted(marketing.rglob("*.md")) if marketing.exists() else []:
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        front = text.split("---")[1]
        if re.search(r"^status:\s*approved\s*$", front, re.M) and not re.search(r"^evidence_gate:\s*\S", front, re.M):
            log("error", f"{path} is approved without evidence_gate date (approved = passed the evidence gate)")
            errors += 1
    if errors == 0:
        log("ok", "Operating loop wired: rules, next_step script, evidence gate")
    return errors


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv if argv is None else argv)
    if "-h" in argv or "--help" in argv:
        print("Usage: python evals/validate_project.py [project_root]")
        return 0
    project_root = resolve_project_root(argv)
    print(f"Project root: {project_root}")
    skill_errors, existing_skills = validate_skills(project_root)
    deliverable_quality_errors = validate_deliverable_quality(project_root)
    validate_deliverable_references(project_root)
    support_reference_warnings = validate_support_references(project_root)
    symlink_warnings = validate_skill_symlinks(project_root, existing_skills)
    ledger_errors = validate_ledger(project_root)

    total_errors = skill_errors + deliverable_quality_errors + ledger_errors
    total_warnings = support_reference_warnings + symlink_warnings
    print("\n" + "=" * 50)
    if total_errors == 0:
        log("ok", f"All checks passed. {len(existing_skills)} skills.")
        if total_warnings:
            log("warn", f"Validation completed with {total_warnings} warning(s).")
        return 0
    log("error", f"Validation failed with {total_errors} error(s) and {total_warnings} warning(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
