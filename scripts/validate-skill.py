#!/usr/bin/env python3
"""Validate the skill folder and repository Markdown links before a commit or release.

Checks:
  - SKILL.md exists and starts with YAML frontmatter (single-line or multiline >-/|)
  - frontmatter has `name` and `description`
  - `name` matches the folder name and uses lowercase letters, digits, hyphens
  - `description` is not empty and is at most 1024 characters
  - skill folder contains only `.md` files (enforces SECURITY.md 100% Plain Markdown claim)
  - every relative Markdown link in the skill points to a file inside the skill folder
  - every relative Markdown link in root docs, docs/, and tests/ resolves to an existing target
  - warns if SKILL.md exceeds 2,000 words

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
WORD_WARN_LIMIT = 2000
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse simple YAML frontmatter, including folded (>-) and literal (|) scalars."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    data: dict[str, str] = {}
    current_key: str | None = None
    multiline_style: str | None = None
    buffer: list[str] = []

    def flush_current() -> None:
        nonlocal current_key, multiline_style, buffer
        if current_key is None:
            return
        if multiline_style and multiline_style.startswith("|"):
            data[current_key] = "\n".join(buffer).strip()
        else:
            data[current_key] = " ".join(part for part in buffer if part).strip()
        current_key = None
        multiline_style = None
        buffer = []

    for line in lines[1:]:
        if line.strip() == "---":
            flush_current()
            return data
        if current_key is not None and (line.startswith((" ", "\t")) or not line.strip()):
            buffer.append(line.strip())
            continue
        flush_current()
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            key = key.strip()
            raw_val = value.strip()
            if raw_val in (">", ">-", "|", "|-"):
                current_key = key
                multiline_style = raw_val
                buffer = []
            else:
                data[key] = raw_val.strip('"').strip("'")
    return None  # no closing ---


def check_links(md_file: Path, skill_dir: Path | None = None) -> list[str]:
    errors: list[str] = []
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
        rel = md_file.relative_to(ROOT).as_posix()
        if not resolved.exists():
            errors.append(f"{rel}: broken link -> {target}")
        elif skill_dir is not None and skill_dir not in resolved.parents and resolved != skill_dir:
            errors.append(f"{rel}: link points outside the skill folder -> {target}")
    return errors


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    label = skill_dir.relative_to(ROOT).as_posix()

    if not skill_md.is_file():
        return [f"{label}: SKILL.md is missing"], warnings

    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    if fm is None:
        return [f"{label}/SKILL.md: missing or unclosed YAML frontmatter (--- ... ---)"], warnings

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

    word_count = len(content.split())
    if word_count > WORD_WARN_LIMIT:
        warnings.append(
            f"{label}/SKILL.md is {word_count} words (target <= {WORD_WARN_LIMIT}) — consider moving detail to references/"
        )

    resolved_skill_dir = skill_dir.resolve()
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and path.suffix.lower() != ".md":
            rel = path.relative_to(ROOT).as_posix()
            errors.append(f"{rel}: non-Markdown file inside skill folder (must remain 100% Plain Markdown)")

    for md_file in sorted(skill_dir.rglob("*.md")):
        errors.extend(check_links(md_file, resolved_skill_dir))

    return errors, warnings


def validate_repo_docs() -> list[str]:
    errors: list[str] = []
    doc_files: list[Path] = []
    for root_md in sorted(ROOT.glob("*.md")):
        doc_files.append(root_md)
    for folder in ("docs", "tests"):
        folder_path = ROOT / folder
        if folder_path.is_dir():
            for md_file in sorted(folder_path.rglob("*.md")):
                if "node_modules" not in md_file.parts:
                    doc_files.append(md_file)

    for md_file in doc_files:
        errors.extend(check_links(md_file, skill_dir=None))
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
    all_warnings: list[str] = []
    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        status = "OK" if not errors else f"{len(errors)} problem(s)"
        print(f"[{status}] {skill_dir.relative_to(ROOT).as_posix()}")
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    doc_errors = validate_repo_docs()
    doc_status = "OK" if not doc_errors else f"{len(doc_errors)} problem(s)"
    print(f"[{doc_status}] repository Markdown links (root, docs/, tests/)")
    all_errors.extend(doc_errors)

    for warn in all_warnings:
        print(f"  [WARN] {warn}")
    for err in all_errors:
        print(f"  - {err}")

    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
