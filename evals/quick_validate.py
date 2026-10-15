#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6",
# ]
# ///
"""Quick validation for a single canonical skill directory."""
import re
import sys
from pathlib import Path

ALLOWED_PROPERTIES = {"name", "description", "license", "metadata"}
NAME_RE = re.compile(r"^(marketing|lead)-[a-z0-9]+(-[a-z0-9]+)*$")
DESC_MIN = 300
DESC_MAX = 700


def validate_skill(skill_path):
    """Basic validation of a skill at skills/<name>/."""
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"
    frontmatter_text = match.group(1)
    try:
        import yaml
    except ImportError:
        raise SystemExit("缺 PyYAML，无法解析 frontmatter：用 `uv run evals/<脚本>.py` 跑（依赖写在脚本头），或先 `pip install pyyaml`。")
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except Exception as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Forbidden or unexpected key(s) in SKILL.md frontmatter: "
            f"{', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )
    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if not name:
        return False, "Missing 'name' in frontmatter"
    if not NAME_RE.match(name):
        return False, (
            f"Name '{name}' must match ^(marketing|lead)- and be kebab-case "
            f"without leading/trailing or doubled hyphens"
        )
    if len(name) > 64:
        return False, f"Name is too long ({len(name)} characters). Maximum is 64."
    if skill_path.is_dir() and name != skill_path.name:
        return False, f"Name '{name}' does not match directory '{skill_path.name}'"

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    collapsed = " ".join(description.split())
    if not collapsed:
        return False, "Missing 'description' in frontmatter"
    if "<" in collapsed or ">" in collapsed:
        return False, "Description cannot contain angle brackets (< or >)"
    if not (DESC_MIN <= len(collapsed) <= DESC_MAX):
        return False, (
            f"Description must be {DESC_MIN}-{DESC_MAX} characters "
            f"(got {len(collapsed)})"
        )
    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: python evals/quick_validate.py <skill_directory>")
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"} else 1)
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
