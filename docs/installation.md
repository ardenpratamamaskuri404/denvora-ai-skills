# Installation Guide

**denvora-ai-skills** is a universal Agent Skill. It works with **Claude Code**, **OpenCode**, **Cursor**, **Windsurf**, **GitHub Copilot**, **Cline**, **Roo Code**, **OpenAI Codex**, **Gemini CLI**, **Google Antigravity**, **Continue**, **AiderDesk**, **Claude Desktop/Web**, and **any chat-based AI** (ChatGPT, DeepSeek, Gemini, etc.).

Choose the installation method that matches your setup.

---

## Option 1: Skills CLI (Recommended — 70+ Coding Agents)

> **Prerequisite:** [Node.js](https://nodejs.org/) 18 or newer (includes `npx`). Verify with `node --version`.

### Interactive install (auto-detects your installed AI tools)

Run inside your project folder:

```bash
npx skills add ardenpratamamaskuri404/denvora-ai-skills
```

Or install **globally** so the skill is available in every project on your machine:

```bash
npx skills add ardenpratamamaskuri404/denvora-ai-skills -g
```

### Direct install for a specific AI agent

Pass `-a <agent>` for project scope, or add `-g` for global scope:

```bash
# Claude Code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a claude-code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a claude-code -g

# OpenCode
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a opencode
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a opencode -g

# Cursor
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cursor
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cursor -g

# Windsurf
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a windsurf
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a windsurf -g

# GitHub Copilot
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a github-copilot
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a github-copilot -g

# Cline / Roo Code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cline
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a roo

# OpenAI Codex CLI
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a codex

# Gemini CLI
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a gemini-cli

# Google Antigravity
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity -g

# Install to ALL detected agents at once
npx skills add ardenpratamamaskuri404/denvora-ai-skills --all
```

### Useful CLI flags

| Flag | Description |
|---|---|
| `-a <agent>` | Target a specific agent (`claude-code`, `opencode`, `cursor`, `windsurf`, `antigravity`, etc.) |
| `-g`, `--global` | Install globally (user-level) instead of only in the current project |
| `--copy` | Copy files directly instead of creating symlinks (recommended on Windows if symlinks require admin permissions) |
| `-y`, `--yes` | Skip interactive confirmation prompts |
| `--list` | List available skills in the repository without installing |

### Update or uninstall

```bash
npx skills update denvora-ai-skills
npx skills remove denvora-ai-skills
npx skills remove denvora-ai-skills -g
```

---

## Option 2: Manual Copy (No Node.js Required)

1. Download this repository (**Code** → **Download ZIP**) and extract it, or clone it with `git clone`.
2. Copy the folder `skills/denvora-ai-skills` (the entire folder including `SKILL.md` and `references/`) into your agent's skills directory:

| AI Tool | Project Folder | Global Folder |
|---|---|---|
| **Claude Code** | `.claude/skills/denvora-ai-skills/` | `~/.claude/skills/denvora-ai-skills/` |
| **OpenCode** | `.agents/skills/denvora-ai-skills/` | `~/.config/opencode/skills/denvora-ai-skills/` |
| **Cursor** | `.agents/skills/denvora-ai-skills/` | `~/.cursor/skills/denvora-ai-skills/` |
| **Windsurf** | `.windsurf/skills/denvora-ai-skills/` | `~/.codeium/windsurf/skills/denvora-ai-skills/` |
| **GitHub Copilot** | `.agents/skills/denvora-ai-skills/` | `~/.copilot/skills/denvora-ai-skills/` |
| **Cline** | `.agents/skills/denvora-ai-skills/` | `~/.agents/skills/denvora-ai-skills/` |
| **Roo Code** | `.roo/skills/denvora-ai-skills/` | `~/.roo/skills/denvora-ai-skills/` |
| **OpenAI Codex** | `.agents/skills/denvora-ai-skills/` | `~/.codex/skills/denvora-ai-skills/` |
| **Gemini CLI** | `.agents/skills/denvora-ai-skills/` | `~/.gemini/skills/denvora-ai-skills/` |
| **Google Antigravity** | `.agents/skills/denvora-ai-skills/` | `~/.gemini/antigravity/skills/denvora-ai-skills/` |
| **Continue** | `.continue/skills/denvora-ai-skills/` | `~/.continue/skills/denvora-ai-skills/` |
| **AiderDesk** | `.aider-desk/skills/denvora-ai-skills/` | `~/.aider-desk/skills/denvora-ai-skills/` |

*(Note: `~` refers to your home directory: `C:\Users\<username>` on Windows, `/Users/<username>` on macOS, `/home/<username>` on Linux.)*

3. Start a **new session / conversation** in your AI tool so it loads the newly added skill.

---

## Option 3: Native Rules Files (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`)

If your workflow uses project rule files such as `AGENTS.md` (OpenCode, Codex, Cursor, Zed), `CLAUDE.md` (Claude Code), `.cursorrules`, `.windsurfrules`, or `.github/copilot-instructions.md`:

1. Copy the `skills/denvora-ai-skills` folder into `.agents/skills/denvora-ai-skills/` (or anywhere in your project).
2. Add this single pointer to your `AGENTS.md`, `CLAUDE.md`, or rules file:

```markdown
Always read and follow `.agents/skills/denvora-ai-skills/SKILL.md` (and its linked files in `references/` when relevant) for all coding, debugging, and verification tasks.
```

---

## Option 4: Claude Desktop & Web (`.skill` Upload)

1. Go to the [Releases page](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/releases) and download `denvora-ai-skills.skill` (or `denvora-ai-skills.zip`).
2. Open Claude → **Settings** → **Skills** (or **Capabilities**), and upload the file.
3. Enable the skill and start a new conversation.

Want to build the `.skill` archive yourself from source?

```bash
# macOS / Linux
./scripts/package-skill.sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\scripts\package-skill.ps1
```

---

## Option 5: Any Chat AI (ChatGPT, DeepSeek, Gemini Web, Bolt, Lovable, v0)

If you use a browser chat or app builder that does not have a skills directory:

- **If the AI can read files in your workspace:** drop `skills/denvora-ai-skills/` into your project and send:
  ```text
  Read skills/denvora-ai-skills/SKILL.md and follow its rules for this entire session.
  ```
- **If using a plain chat window:** copy the contents of [`skills/denvora-ai-skills/SKILL.md`](../skills/denvora-ai-skills/SKILL.md) into your custom instructions or paste it at the start of the conversation.

See [prompt-templates.md](prompt-templates.md) for ready-to-copy prompts in English and Indonesian.

---

## Keeping Your Project Clean (Git Hygiene)

- **Want your whole team to share these AI rules?** Install at project scope and commit `.agents/skills/` (or `.claude/skills/`).
- **Working on a personal or client repo where you don't want extra files committed?** Either:
  1. Install **globally** with `-g` (`npx skills add ardenpratamamaskuri404/denvora-ai-skills -g`), which puts nothing inside your project folder, OR
  2. Add `.agents/` and `skills-lock.json` to your `.git/info/exclude` or `.gitignore`.

---

## Verify It Works

1. Start a **new** conversation in your AI tool.
2. Ask a normal coding question, e.g. *"Fix this error: TypeError: Cannot read properties of undefined"*.
3. You should see the AI:
   - Read or ask for the relevant file before editing anything.
   - Tag key claims with **[Certain] / [Likely] / [Unsure]** (or **[Pasti] / [Kemungkinan] / [Belum yakin]**).
   - End with a concise verification report showing what was tested and what was not.

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `npx: command not found` | Install Node.js 18+ from [nodejs.org](https://nodejs.org/) and restart your terminal, or use **Option 2 (Manual Copy)** |
| Skill is installed but AI ignores it | Start a **new** chat session. You can also explicitly tell the agent: *"Use the denvora-ai-skills skill."* |
| Symlink permission error on Windows | Add `--copy` to the install command: `npx skills add ardenpratamamaskuri404/denvora-ai-skills --copy` |
| Want to check where skills are installed | Run `npx skills list` (or `npx skills list -g` for global skills) |
| Still having trouble? | [Open an installation issue](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=install-problem.yml) |
