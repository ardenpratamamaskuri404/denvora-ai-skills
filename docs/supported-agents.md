# Supported AI Agents

**denvora-ai-skills** follows the standard Agent Skills specification (`skills/<skill-name>/SKILL.md`), so it works across any AI coding assistant that supports Agent Skills, native rule files (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`), or file/prompt context.

To keep our documentation transparent, we separate two things:

- **Install path verified:** we confirmed the CLI flag and target directory from the official [Skills CLI](https://github.com/vercel-labs/skills) (v1.5.18) or direct installation tests.
- **Behavior benchmarked:** a full 15-case benchmark from [`tests/test-cases.md`](../tests/test-cases.md) has been recorded in [`tests/results/`](../tests/results/).

## Agent Compatibility Matrix

| AI Assistant / Agent | Skills CLI Flag (`-a`) | Project Directory | Global Directory | Install Path Status | Benchmark Status |
|---|---|---|---|---|---|
| **Claude Code** | `claude-code` | `.claude/skills/` | `~/.claude/skills/` | Verified (CLI config) | Pending first run |
| **Kiro** | `kiro` | `.kiro/skills/` | `~/.kiro/skills/` | Verified (CLI config & steering) | Pending first run |
| **OpenCode** | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` | Verified (CLI config) | Pending first run |
| **Cursor** | `cursor` | `.agents/skills/` | `~/.cursor/skills/` | Verified (CLI config) | Pending first run |
| **Windsurf** | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | Verified (CLI config) | Pending first run |
| **GitHub Copilot** | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` | Verified (CLI config) | Pending first run |
| **Cline** | `cline` | `.agents/skills/` | `~/.agents/skills/` | Verified (CLI config) | Pending first run |
| **Roo Code** | `roo` | `.roo/skills/` | `~/.roo/skills/` | Verified (CLI config) | Pending first run |
| **OpenAI Codex CLI** | `codex` | `.agents/skills/` | `$CODEX_HOME/skills/` | Verified (CLI config) | Pending first run |
| **Gemini CLI** | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` | Verified (CLI config) | Pending first run |
| **Google Antigravity** | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` | Verified end-to-end | Pending first run |
| **Antigravity CLI** | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` | Verified (CLI config) | Pending first run |
| **Continue** | `continue` | `.continue/skills/` | `~/.continue/skills/` | Verified (CLI config) | Pending first run |
| **AiderDesk** | `aider-desk` | `.aider-desk/skills/` | `~/.aider-desk/skills/` | Verified (CLI config) | Pending first run |
| **Zed** | `zed` | `.agents/skills/` | `~/.agents/skills/` | Verified (CLI config) | Pending first run |
| **Trae** | `trae` | `.trae/skills/` | `~/.trae/skills/` | Verified (CLI config) | Pending first run |
| **Goose** | `goose` | `.goose/skills/` | `~/.config/goose/skills/` | Verified (CLI config) | Pending first run |
| **Kilo Code** | `kilo` | `.kilocode/skills/` | `~/.kilocode/skills/` | Verified (CLI config) | Pending first run |
| **Warp** | `warp` | `.agents/skills/` | `~/.agents/skills/` | Verified (CLI config) | Pending first run |
| **Claude Desktop / Web** | `.skill` upload | n/a | Upload in Settings → Skills | Archive verified | Pending first run |
| **ChatGPT / DeepSeek / Web AIs** | Prompt / file | Paste or attach `SKILL.md` | Custom instructions | Universal | Pending first run |

> The Skills CLI supports **70+ coding agents** out of the box (including Amp, Augment, Devin, Droid, Firebender, ForgeCode, Junie, Kimi Code CLI, OpenHands, Qoder, Qwen Code, Replit, Rovo Dev, Zencoder, and more). Run `npx skills add ardenpratamamaskuri404/denvora-ai-skills` without `-a` to let the CLI detect your installed agents automatically.

## Contributing Benchmark Results

Want to help benchmark an agent you use daily?

1. Install the skill on your preferred agent.
2. Run test cases from [`tests/test-cases.md`](../tests/test-cases.md) with and without the skill.
3. Record your scores using [`tests/results/TEMPLATE.md`](../tests/results/TEMPLATE.md) and open a Pull Request.
