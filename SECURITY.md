# Security

## What this skill is

denvora-ai-skills is **plain Markdown instructions** for AI coding assistants. The skill folder (`skills/denvora-ai-skills/`) contains:

- No executable scripts
- No network calls
- No telemetry or data collection
- No API keys or accounts

The AI reads these instructions as text. You can open every file and read exactly what it tells the AI to do.

The `scripts/` folder at the repo root (validate and package) is for maintainers and CI only. It is **not** part of the installed skill.

## What the skill tells the AI about safety

The core rules ask the AI to:

- Never put secrets (API keys, passwords) in code or commits
- Ask before deleting files, dropping data, overwriting config, or running destructive commands
- Run a [security checklist](skills/denvora-ai-skills/references/security-checklist.md) before anything goes online

These are instructions, not guarantees. AI models can still make mistakes. Always review what your AI does, keep backups, and use version control (git).

## Verify what you install

Before installing any skill from anyone, including this one:

1. Read `SKILL.md` and the files in `references/`.
2. Check that the skill folder contains only `.md` files.
3. Install from the official repo: `ardenpratamamaskuri404/denvora-ai-skills`.

## Reporting a vulnerability

If you find something in this repo that could cause harm (for example, an instruction that makes an AI leak secrets or run dangerous commands, or a compromised release file):

- **Please do not open a public issue.**
- Use GitHub's private vulnerability reporting: **Security** tab > **Report a vulnerability** on this repository.
- If that is not available, contact the maintainer via [@ardenpratamamaskuri404](https://github.com/ardenpratamamaskuri404).

Please include what you found, how to reproduce it, and the version or commit. We aim to respond within 7 days.
