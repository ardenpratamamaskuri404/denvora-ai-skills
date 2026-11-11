# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- **Stronger Core Guardrails (`SKILL.md`):**
  - Golden Rules #10–13 covering no silent hardcoded mocks or weakened/skipped tests, checking local installed sources (`node_modules/`, `.d.ts`, `site-packages/`, `vendor/`), matching the user's OS and shell (Windows PowerShell vs Unix bash/zsh), and never echoing `.env` secrets or running unverified remote scripts.
  - Anti-rationalization table (`Common excuses — do not fall for these`) and re-verification reminder after final cleanup edits.
  - Bilingual report template with Indonesian labels (`Yang saya kerjakan:`, `Sudah dicek:`, `Belum dicek:`, `Asumsi:`, `Langkah berikutnya:`).
- **Stack Version Pitfalls Reference (`skills/denvora-ai-skills/references/stack-pitfalls.md`):**
  - On-demand version trap guide for Next.js (13/14 vs 15+), Tailwind CSS (v3 vs v4), React (17/18/19), Laravel (9/10/11+), Python, and Flutter/Dart.
- **Ready-to-Use Benchmark Fixtures (`tests/fixtures/`):**
  - Minimal reproducible projects (`react-null-user/`, `express-todo/`, `python-empty/`) linked from `tests/test-cases.md`.
- **README & CI Enhancements:**
  - Added live GitHub Actions badge, "Why This Instead of a Plain Rules File?" comparison, real Before vs. After demo, Mermaid workflow/debugging diagrams, Update & Uninstall instructions (EN/ID), and a 10-second smoke test.
  - Updated `scripts/validate-skill.py` to support multiline YAML frontmatter (`>-`/`|`), enforce Markdown-only files inside `skills/`, warn on high word count, and validate links across root docs, `docs/`, and `tests/`.
  - Updated `package.json` with `private: true` and maintainer `scripts` (plus cross-platform `scripts/run-validate.mjs` wrapper), and generalized `.github/ISSUE_TEMPLATE/install-problem.yml` for all supported agents.

## [0.1.0] - 2026-11-10

Initial public draft of **denvora-ai-skills**.

### Added

- **Core Universal Skill (`skills/denvora-ai-skills/SKILL.md`):**
  - 9 Golden Rules covering anti-hallucination (never invent), read-before-write, project cleanliness and non-destructive editing, data/git protection, blocking-only questions, small verified slices, evidence-based debugging, and honest uncertainty.
  - Confidence labels (`[Certain]` / `[Likely]` / `[Unsure]` and Indonesian equivalents `[Pasti]` / `[Kemungkinan]` / `[Belum yakin]`).
  - Automatic task scaling (tiny tasks get concise answers; normal/large tasks follow the structured slice workflow).
  - Standardized end-of-task verification report format.
- **On-Demand Reference Guides (`skills/denvora-ai-skills/references/`):**
  - `workflow.md` — step-by-step slice execution and project hygiene rules.
  - `verification-checklist.md` — evidence standards and per-stack verification commands.
  - `debugging-protocol.md` — root-cause debugging (one hypothesis at a time, revert failed tries, stop after 3 failed attempts).
  - `beginner-communication.md` — plain-language communication guide with English and Indonesian examples.
  - `security-checklist.md` — pre-launch security checklist for web apps and APIs.
- **Universal Agent Documentation (`docs/`):**
  - `installation.md` — installation commands and manual paths for 70+ agents via the Skills CLI (`claude-code`, `opencode`, `cursor`, `windsurf`, `github-copilot`, `cline`, `roo`, `codex`, `gemini-cli`, `antigravity`, etc.), native rules files (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`), Claude `.skill` upload, chat AI usage, and git hygiene tips.
  - `supported-agents.md` — compatibility matrix separating verified install paths from recorded behavior benchmarks.
  - `prompt-templates.md` — copy-paste prompts in English and Indonesian.
- **Benchmarking Suite (`tests/`):**
  - 15 realistic test cases across 7 categories, a 0–2 scoring rubric, and a reproducible results template.
- **Tooling, CI & Community Files:**
  - `scripts/validate-skill.py` (frontmatter and link validator) and `scripts/package-skill.sh` / `scripts/package-skill.ps1` (`.skill` / `.zip` packager).
  - GitHub Actions workflows for continuous validation (`validate.yml`) and automated release packaging (`release.yml`).
  - Issue templates (AI Hallucination Report, Install Problem, Idea) and Pull Request template.
  - `SECURITY.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`.

[Unreleased]: https://github.com/ardenpratamamaskuri404/denvora-ai-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ardenpratamamaskuri404/denvora-ai-skills/releases/tag/v0.1.0
