<p align="center">
  <img src="assets/denvora-logo.png" alt="denvora-ai-skills" width="640">
</p>

<p align="center">
  <strong>Make any AI coding assistant careful, honest, and safe for your project.</strong><br>
  A universal open-source Agent Skill for Claude Code, OpenCode, Cursor, Windsurf, GitHub Copilot, Cline, Codex, Gemini CLI, Google Antigravity, and any chat AI.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="scripts/validate-skill.py"><img src="https://img.shields.io/badge/skill_spec-validated-brightgreen.svg" alt="Skill Spec Validated"></a>
  <a href="docs/supported-agents.md"><img src="https://img.shields.io/badge/agents-70%2B_supported-purple.svg" alt="70+ Agents Supported"></a>
  <img src="https://img.shields.io/badge/version-v0.1.0-orange.svg" alt="Version v0.1.0">
  <img src="https://img.shields.io/badge/languages-English_%7C_Indonesian-teal.svg" alt="English and Indonesian">
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#what-it-changes">What It Changes</a> ·
  <a href="#project-safety--security">Project Safety</a> ·
  <a href="docs/installation.md">Installation Guide</a> ·
  <a href="docs/supported-agents.md">Supported Agents</a> ·
  <a href="docs/prompt-templates.md">Prompt Templates</a> ·
  <a href="#bahasa-indonesia">Bahasa Indonesia</a>
</p>

---

## Why denvora-ai-skills?

When building with AI (especially when vibe coding or learning), you often can't review every single line the AI writes. By default, many AI coding assistants fall into destructive habits:

- **Inventing APIs:** calling functions, packages, CLI flags, or versions that do not exist.
- **Blind editing:** rewriting files without reading your existing project structure first.
- **Making a mess of your project:** touching unrelated files, adding unnecessary packages, or leaving broken code and temporary debug logs behind.
- **Unverified claims:** saying *"Done, everything works!"* without running a build or test.
- **Guessing loops:** trying random fixes when an error happens instead of finding the root cause.

**denvora-ai-skills** is a set of structured working rules that your AI assistant loads automatically. It enforces verification, small incremental slices, project cleanliness, and transparent confidence labels on every task.

---

## Quick Start

### 1. Install with the Skills CLI (70+ AI Coding Agents)

Requires [Node.js](https://nodejs.org/) 18+ (which includes `npx`).

```bash
# Interactive install (auto-detects your installed AI agents)
npx skills add ardenpratamamaskuri404/denvora-ai-skills

# Or install globally across all your projects
npx skills add ardenpratamamaskuri404/denvora-ai-skills -g
```

Or target your preferred AI coding assistant directly:

```bash
# Claude Code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a claude-code

# OpenCode
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a opencode

# Cursor
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cursor

# Windsurf
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a windsurf

# GitHub Copilot
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a github-copilot

# Cline / Roo Code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cline
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a roo

# OpenAI Codex CLI / Gemini CLI
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a codex
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a gemini-cli

# Google Antigravity
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity

# Install to ALL detected agents at once
npx skills add ardenpratamamaskuri404/denvora-ai-skills --all
```

*(Add `-g` to any command above to install globally instead of only in the current project.)*

### 2. Using `CLAUDE.md`, `AGENTS.md`, or `.cursorrules`?

If you prefer native rule files, copy `skills/denvora-ai-skills` into your project (or `.agents/skills/denvora-ai-skills/`) and add this line to your `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or `.windsurfrules`:

```markdown
Always read and follow `.agents/skills/denvora-ai-skills/SKILL.md` (and its linked files in `references/` when relevant) for all coding, debugging, and verification tasks.
```

### 3. Using ChatGPT, Claude Web, DeepSeek, or another Chat AI?

- **Claude Desktop / Web:** Upload `denvora-ai-skills.skill` from [Releases](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/releases) under **Settings → Skills**.
- **Any Chat AI or App Builder:** Tell the AI to read [`skills/denvora-ai-skills/SKILL.md`](skills/denvora-ai-skills/SKILL.md), or paste its contents at the start of your chat.

Full instructions for every tool: **[docs/installation.md](docs/installation.md)**.

---

## What It Changes

| Typical AI Behavior | With `denvora-ai-skills` |
|---|---|
| Uses a method it "remembers" from an older version | Checks your installed version first, or labels it **[Unsure]** |
| Overwrites a file without reading it | Reads the file and follows your project's existing patterns |
| Modifies unrelated files or adds unneeded packages | Touches only relevant files and reuses existing dependencies |
| Dumps 500 lines of untested code in one reply | Builds in small, verifiable slices one step at a time |
| Claims *"This should work!"* without checking | Runs tests/build and reports exact output, or gives you the check command |
| Guesses randomly when an error occurs | Reads the full error, tests one hypothesis at a time, and reverts failed tries |
| Overwhelms beginners with jargon | Replies in your language with plain explanations and copyable commands |

### Honest Verification Report

At the end of every normal or large task, the AI provides a clear status summary:

```text
What I did:    Added a loading guard to src/app/profile/page.tsx
Verified:      [Certain] npm run build passed with 0 errors
Not verified:  Mobile viewport layout. Check with: npm run dev
Assumptions:   Kept your existing Tailwind CSS utility classes
Next step:     Add an error fallback if the profile request fails
```

---

## Project Safety & Security

We designed **denvora-ai-skills** so it is completely safe to use on personal, team, and client projects:

1. **100% Plain Markdown:** The skill folder (`skills/denvora-ai-skills/`) contains only `.md` text instructions. There are **no executable scripts**, **no network requests**, **no telemetry**, and **no hidden hooks** inside the skill.
2. **Non-Destructive by Rule:**
   - **No unrequested changes:** The AI is instructed to modify *only* the files required for your request and leave unrelated files untouched.
   - **No dependency bloat:** It will not install or upgrade packages without checking existing dependencies and asking first.
   - **No leftover clutter:** Temporary debug logs (`console.log`, `print`), scratch scripts, and failed fix attempts must be cleaned up before finishing.
   - **No destructive commands without consent:** Commands that delete files, reset git history (`git reset --hard`), drop database tables (`migrate:fresh`), or overwrite `.env` require explicit confirmation.
   - **Rollback on failure:** If an edit breaks the build or existing tests and cannot be fixed right away, the AI is instructed to revert the broken edit so your project stays in a working state.

Read the full security policy in **[SECURITY.md](SECURITY.md)**.

---

## Architecture

```text
skills/denvora-ai-skills/
├── SKILL.md                         # Core rules (compact so it uses minimal context tokens)
└── references/                      # Loaded on demand only when relevant
    ├── workflow.md                  # Understand → Inspect → Plan → Build → Verify → Report
    ├── verification-checklist.md    # Evidence requirements for [Certain] claims
    ├── debugging-protocol.md        # Root-cause debugging (one change at a time)
    ├── beginner-communication.md    # Clear, friendly communication guide (EN / ID)
    └── security-checklist.md        # Pre-deployment security checklist
```

---

## Benchmarking & Quality Suite

A skill should prove its value with real tests, not marketing numbers. The [`tests/`](tests/README.md) directory includes:

- **[15 realistic test prompts](tests/test-cases.md)** covering app building, bug fixing, editing existing code, non-existent library traps, vague requests, tiny tasks, and destructive command safety.
- **[A 0–2 scoring rubric](tests/scoring-rubric.md)** measuring hallucination counts, verification honesty, and slice discipline with and without the skill.
- **[A results template](tests/results/TEMPLATE.md)** for recording reproducible benchmarks across different agents and models.

---

## Bahasa Indonesia

**denvora-ai-skills** adalah *Agent Skill* open-source universal yang membuat asisten coding AI bekerja lebih teliti, jujur, dan aman bagi project kamu. Bisa digunakan di **Claude Code**, **OpenCode**, **Cursor**, **Windsurf**, **GitHub Copilot**, **Cline**, **Roo Code**, **Codex**, **Gemini CLI**, **Google Antigravity**, **Claude Desktop/Web**, maupun AI chat seperti **ChatGPT** dan **DeepSeek**.

### Apa manfaat utamanya?

- **Anti-halusinasi:** AI tidak mengarang fungsi, library, flag CLI, atau versi yang tidak ada.
- **Baca sebelum menulis:** AI memeriksa struktur folder dan versi library di project kamu sebelum mengubah kode.
- **Menjaga project tetap rapi & aman:** Tidak mengubah file yang tidak berkaitan, tidak menambah package sembarangan, tidak meninggalkan sampah kode debug, dan meminta izin sebelum menjalankan perintah berisiko.
- **Bertahap & terverifikasi:** Membangun fitur sedikit demi sedikit (*small slices*) dan mengecek setiap tahap.
- **Transparan:** Memberi label tingkat keyakinan **[Pasti] / [Kemungkinan] / [Belum yakin]** serta laporan jujur mengenai apa yang sudah dan belum dites.

### Cara Instalasi Cepat

```bash
# Otomatis mendeteksi AI agent yang terpasang di komputer kamu
npx skills add ardenpratamamaskuri404/denvora-ai-skills

# Atau pasang langsung ke agent pilihanmu (tambahkan -g untuk global di semua project):
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a claude-code
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a opencode
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cursor
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a windsurf
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a github-copilot
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a cline
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity
```

**Menggunakan AI chat biasa atau punya file aturan sendiri (`CLAUDE.md` / `AGENTS.md` / `.cursorrules`)?**
Cukup salin folder `skills/denvora-ai-skills` ke dalam project kamu, lalu berikan instruksi ini ke AI:

```text
Baca skills/denvora-ai-skills/SKILL.md dan ikuti seluruh aturannya selama percakapan ini.
```

Panduan selengkapnya:
[Panduan Instalasi](docs/installation.md) · [Daftar Agen AI yang Didukung](docs/supported-agents.md) · [Template Prompt (ID/EN)](docs/prompt-templates.md) · [Laporkan Kasus Halusinasi AI](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=hallucination-report.yml)

---

## Contributing

Contributions, benchmark results, and real-world failure reports are very welcome!

- Found a prompt where an AI still hallucinated or skipped verification? **[Open an AI Hallucination Report](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=hallucination-report.yml)**.
- Want to improve the rules, add stack references, or submit test results? Read **[CONTRIBUTING.md](CONTRIBUTING.md)**.

## License

[MIT](LICENSE) © 2026 Arden Pratama Maskuri
