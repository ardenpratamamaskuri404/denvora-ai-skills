# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-11-10

First draft of the skill and project structure.

### Added

- Core skill `skills/denvora-ai-skills/SKILL.md`: golden rules (never invent, read before write, blocking questions only, small slices, verify then claim, evidence-based debugging, honest uncertainty, protect the user's work), confidence labels (Certain / Likely / Unsure, with Indonesian equivalents), task scaling, report format, and red flags.
- References: workflow, verification checklist, debugging protocol, beginner communication guide (EN/ID), pre-launch security checklist.
- Test suite: 15 prompt-based cases, scoring rubric, results template.
- Scripts: `validate-skill.py`, `package-skill.sh`, `package-skill.ps1` (builds the `.skill` file for Claude).
- GitHub: CI validation, release workflow that attaches the `.skill` file to tagged releases, issue templates (including "AI still hallucinated / AI masih ngawang"), pull request template.
- Docs: README with logo, installation guide, supported agents table, prompt templates in English and Indonesian, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY.

### Verified

- `npx skills add <repo> --list` (Skills CLI v1.5.18) discovers the skill.
- Project-scope install for Antigravity places files in `.agents/skills/denvora-ai-skills/` (Windows).
- Validator passes; packaging produces an archive with the skill folder at the top level.

### Not yet verified

- Antigravity loading and following the skill in a live session.
- Claude `.skill` upload.
- Behavior on any agent via the test suite (no results recorded yet).

[Unreleased]: https://github.com/ardenpratamamaskuri404/denvora-ai-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ardenpratamamaskuri404/denvora-ai-skills/releases/tag/v0.1.0
