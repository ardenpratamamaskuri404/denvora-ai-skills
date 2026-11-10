# Supported agents

denvora-ai-skills is a standard Agent Skill (a folder with `SKILL.md`), so any tool that supports Agent Skills can load it. "Supported" below means two different things, and we keep them separate on purpose:

- **Install path verified:** we confirmed where the files go.
- **Behavior tested:** someone ran the [test suite](../tests/README.md) on this agent and recorded results in `tests/results/`.

We do not claim an agent is "tested" until a results file exists.

## Status

| Agent | `-a` value | Project folder | Global folder | Install path verified | Behavior tested |
|---|---|---|---|---|---|
| Google Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` | Yes (Skills CLI v1.5.18, Windows) | Not yet |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` | From CLI config | Not yet |
| Claude (app, `.skill` upload) | n/a | n/a | Upload in Settings | Package builds; upload not yet tested | Not yet |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` | From CLI config | Not yet |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` | From CLI config | Not yet |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | From CLI config | Not yet |
| OpenAI Codex | `codex` | `.agents/skills/` | `$CODEX_HOME/skills/` | From CLI config | Not yet |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` | From CLI config | Not yet |
| GitHub Copilot | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` | From CLI config | Not yet |
| Cline | `cline` | `.agents/skills/` | `~/.agents/skills/` | From CLI config | Not yet |
| Any chat AI | n/a | Tell it to read / paste `SKILL.md` | n/a | n/a | Not yet |

"From CLI config" means the folder comes from the agent table inside the [Skills CLI](https://github.com/vercel-labs/skills) (v1.5.18), not from our own end-to-end test. Folder locations can change when agents update; if you see a difference, please [open an issue](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=install-problem.yml).

## Known differences

None recorded yet. When you test on an agent, add notes here, for example: "Agent X does not load files in `references/` automatically; it only reads them when the AI decides to open them."

## Help us test

1. Install the skill on your agent.
2. Run some cases from [tests/test-cases.md](../tests/test-cases.md).
3. Add a results file to `tests/results/` (copy the [template](../tests/results/TEMPLATE.md)) and open a PR.
4. Update the "Behavior tested" column for that agent in the same PR.
