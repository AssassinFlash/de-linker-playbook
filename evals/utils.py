"""Utility functions for eval scripts."""
import re
from pathlib import Path


def parse_frontmatter_and_body(content: str) -> tuple[dict, str]:
    """Return (frontmatter mapping, body). Empty mapping if no YAML header."""
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, content
    try:
        import yaml
    except ImportError:
        raise SystemExit("缺 PyYAML，无法解析 frontmatter：用 `uv run evals/<脚本>.py` 跑（依赖写在脚本头），或先 `pip install pyyaml`。")
    try:
        loaded = yaml.safe_load(match.group(1))
    except Exception:
        return {}, content
    if not isinstance(loaded, dict):
        return {}, content
    return loaded, match.group(2)


def collapsed_len(text: str) -> int:
    """Length after folding whitespace, matching playbook description gates."""
    return len(" ".join(str(text).split()))


def parse_skill_md(skill_path: Path) -> tuple[str, str, str]:
    """Extract name, description, and body from a SKILL.md file."""
    skill_md = skill_path / "SKILL.md" if skill_path.is_dir() else skill_path
    content = skill_md.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter_and_body(content)
    name = frontmatter.get("name", "") or ""
    description = frontmatter.get("description", "") or ""
    return str(name), str(description), body
