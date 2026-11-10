#!/usr/bin/env python3
"""Validate the skill folder before a commit or release.

Checks:
  - SKILL.md exists and starts with YAML frontmatter
  - frontmatter has `name` and `description`
  - `name` matches the folder name and uses lowercase letters, digits, hyphens
  - `description` is not empty and is at most 1024 characters
  - every relative Markdown link in the skill points to a file that exists

Usage: python scripts/validate-skill.py
Exit code 0 = OK, 1 = problems found.
Standard library only, no install needed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MAX_DESCRIPTION = 1024
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse simple `key: value` frontmatter (single-line values only)."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return None  # no closing ---


def check_links(md_file: Path, skill_dir: Path) -> list[str]:
    errors = []
    text = md_file.read_text(encoding="utf-8")
    # Ignore links inside fenced code blocks.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for target in LINK_PATTERN.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue  # external URL, mailto, or in-page anchor
        path_part = target.split("#", 1)[0]
        if not path_part:
            continue
        resolved = (md_file.parent / path_part).resolve()
        if not resolved.exists():
            rel = md_file.relative_to(ROOT).as_posix()
            errors.append(f"{rel}: broken link -> {target}")
        elif skill_dir not in resolved.parents and resolved != skill_dir:
            rel = md_file.relative_to(ROOT).as_posix()
            errors.append(f"{rel}: link points outside the skill folder -> {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    label = skill_dir.relative_to(ROOT).as_posix()

    if not skill_md.is_file():
        return [f"{label}: SKILL.md is missing"]

    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fm is None:
        return [f"{label}/SKILL.md: missing or unclosed YAML frontmatter (--- ... ---)"]

    name = fm.get("name", "")
    description = fm.get("description", "")

    if not name:
        errors.append(f"{label}/SKILL.md: frontmatter is missing `name`")
    elif not NAME_PATTERN.match(name):
        errors.append(f"{label}/SKILL.md: `name` must be lowercase letters, digits and hyphens (got '{name}')")
    elif name != skill_dir.name:
        errors.append(f"{label}/SKILL.md: `name` '{name}' does not match folder '{skill_dir.name}'")

    if not description:
        errors.append(f"{label}/SKILL.md: frontmatter is missing `description`")
    elif len(description) > MAX_DESCRIPTION:
        errors.append(
            f"{label}/SKILL.md: `description` is {len(description)} chars (max {MAX_DESCRIPTION})"
        )

    for md_file in sorted(skill_dir.rglob("*.md")):
        errors.extend(check_links(md_file, skill_dir.resolve()))

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("Error: skills/ folder not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print("Error: no skills found in skills/", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        status = "OK" if not errors else f"{len(errors)} problem(s)"
        print(f"[{status}] {skill_dir.relative_to(ROOT).as_posix()}")
        all_errors.extend(errors)

    for err in all_errors:
        print(f"  - {err}")

    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
