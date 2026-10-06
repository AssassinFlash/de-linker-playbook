"""
Lead generation Markdown export utility.
Writes Markdown files with YAML frontmatter under deliverables/lead/.
"""
from __future__ import annotations

from pathlib import Path
from datetime import date
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

LEAD_PHASE_DIRS = {
    "00-system",
    "01-icp",
    "02-companies",
    "03-contacts",
    "04-market",
    "05-usp",
    "06-outreach",
    "07-targeted",
    "08-linkedin",
    "09-seo",
    "10-sales",
    "99-archive",
}


def _require_yaml():
    if yaml is None:
        raise ImportError("PyYAML required: pip install pyyaml")
    return yaml


def write_deliverable_markdown(
    output_path: str | Path,
    frontmatter: dict[str, Any],
    content: str,
    archive_existing: bool = True,
) -> Path:
    """
    Write a Markdown file with YAML frontmatter to deliverables/.

    If the file already exists and archive_existing is True,
    moves the old file to 99-archive/ with a date suffix.

    Args:
        output_path: Full path for the .md file
        frontmatter: Dict for YAML frontmatter
        content: Markdown body content
        archive_existing: Whether to archive existing file

    Returns:
        Path to written file
    """
    yaml_mod = _require_yaml()
    output_path = Path(output_path)

    if output_path.exists() and archive_existing:
        _archive_file(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fm_str = yaml_mod.dump(
        frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False
    )
    full_content = f"---\n{fm_str}---\n\n{content}"

    output_path.write_text(full_content, encoding="utf-8")
    return output_path


def read_frontmatter(file_path: str | Path) -> dict[str, Any]:
    """Read YAML frontmatter from a Markdown file."""
    yaml_mod = _require_yaml()
    file_path = Path(file_path)
    if not file_path.exists():
        return {}

    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}

    end = text.index("---", 3)
    fm_text = text[3:end].strip()
    return yaml_mod.safe_load(fm_text) or {}


def update_frontmatter(file_path: str | Path, updates: dict[str, Any]) -> None:
    """Update specific frontmatter fields without changing the body."""
    yaml_mod = _require_yaml()
    file_path = Path(file_path)
    text = file_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return

    end = text.index("---", 3)
    fm_text = text[3:end].strip()
    body = text[end + 3:].lstrip("\n")

    fm = yaml_mod.safe_load(fm_text) or {}
    fm.update(updates)

    write_deliverable_markdown(file_path, fm, body, archive_existing=False)


def _find_lead_root(file_path: Path) -> Path | None:
    parts = file_path.resolve().parts
    for i, part in enumerate(parts):
        if part == "deliverables" and i + 1 < len(parts) and parts[i + 1] == "lead":
            return Path(*parts[: i + 2])
    current = file_path.parent
    while current != current.parent:
        if current.name in LEAD_PHASE_DIRS:
            return current.parent
        current = current.parent
    return None


def _archive_file(file_path: Path) -> Path:
    """Move file to 99-archive/ with a date suffix under deliverables/lead/."""
    lead_root = _find_lead_root(file_path)
    if lead_root is None:
        archive_dir = file_path.parent / "99-archive"
    else:
        relative = file_path.relative_to(lead_root)
        archive_dir = lead_root / "99-archive" / relative.parent

    archive_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    archive_name = f"{file_path.stem}_{today}{file_path.suffix}"
    archive_path = archive_dir / archive_name
    file_path.rename(archive_path)
    return archive_path
