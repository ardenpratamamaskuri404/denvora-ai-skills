# Security & Project Safety Policy

## 1. What is inside the installed skill?

**denvora-ai-skills** is a collection of **plain Markdown (`.md`) instructions** for AI coding assistants. The installed skill directory (`skills/denvora-ai-skills/`) contains:

- **No executable code or scripts**
- **No network requests or external API calls**
- **No telemetry, analytics, or data collection**
- **No credentials, tokens, or hidden hooks**

When your AI assistant loads this skill, it simply reads the Markdown files as text instructions. You can inspect every file in [`skills/denvora-ai-skills/`](skills/denvora-ai-skills/) before installing.

*(Note: The `scripts/` folder at the repository root contains maintainer utilities for validating Markdown links and building release archives in CI. Those scripts are **not** included inside `skills/denvora-ai-skills/` and are never installed into your project or agent.)*

---

## 2. How the skill protects your project from getting messed up

A major risk when using AI coding assistants is that an overly aggressive agent can break working code, pollute your repository, or run destructive commands. **denvora-ai-skills** enforces strict non-destructive safeguards:

1. **Read Before Write:** The AI must read existing files and inspect your project's configuration (`package.json`, `requirements.txt`, `composer.json`, etc.) before making any changes.
2. **Scoped Edits Only:** The AI is instructed to touch *only* the files directly needed for your request—never reformatting, moving, or refactoring unrelated files.
3. **Dependency Discipline:** The AI must prefer existing libraries and built-in features over installing new packages, and must ask before adding or upgrading dependencies.
4. **No Leftover Clutter:** Any temporary debug logs (`console.log`, `print`), scratch scripts, or failed fix attempts must be cleaned up before finishing a task.
5. **Explicit Confirmation for Destructive Actions:** The AI is forbidden from deleting files, overwriting `.env` or configuration files, resetting databases (`migrate:fresh`, `prisma migrate reset`), or running destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean`, `push --force`) without asking you first and explaining what will be lost.
6. **Git Hygiene:** The AI will not create commits, switch branches, or push code unless you explicitly ask it to.
7. **Rollback Broken Changes:** If a change breaks your build or existing tests and cannot be resolved immediately, the AI is instructed to revert the broken edit rather than leaving your project in a broken state.
8. **Pre-Launch Security Checklist:** Before you deploy an application, the skill provides a [Pre-Launch Security Checklist](skills/denvora-ai-skills/references/security-checklist.md) covering secrets, input validation, authentication, CORS, and dependency audits.

> **Important reminder:** Agent Skills are behavioral instructions, not OS-level sandboxes. Always use version control (`git`) and review terminal commands before approving them in your editor.

---

## 3. Verifying before you install

Before installing any third-party skill (including this one):

1. Inspect [`skills/denvora-ai-skills/SKILL.md`](skills/denvora-ai-skills/SKILL.md) and [`skills/denvora-ai-skills/references/`](skills/denvora-ai-skills/references/).
2. Confirm that `skills/denvora-ai-skills/` contains only `.md` files.
3. Install only from the official repository: `ardenpratamamaskuri404/denvora-ai-skills`.

---

## 4. Reporting a security issue

If you discover anything in this repository that could cause unsafe AI behavior, expose secrets, or compromise a release artifact:

- **Please do not open a public issue.**
- Report it privately via GitHub's **Security → Report a vulnerability** tab on this repository, or contact the maintainer via [@ardenpratamamaskuri404](https://github.com/ardenpratamamaskuri404).

Please include a description of the issue, steps to reproduce, and the affected version or commit. We aim to respond within 7 days.
