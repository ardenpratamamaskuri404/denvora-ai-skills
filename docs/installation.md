# Installation guide

Pick **one** method. The Skills CLI (Option A) is the easiest.

> **Requirements for Option A:** [Node.js](https://nodejs.org/) 18 or newer (it includes `npx`). Check with `node --version`.

---

## Option A: Skills CLI (recommended)

### Project scope (only this project)

Run in your project folder:

```bash
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity
```

This puts the skill in `.agents/skills/denvora-ai-skills/` inside your project. Commit that folder if you want your whole team to use the same rules.

### Global scope (all your projects)

```bash
npx skills add ardenpratamamaskuri404/denvora-ai-skills -a antigravity -g
```

This puts the skill in `~/.gemini/antigravity/skills/denvora-ai-skills/`.

### Useful flags

| Flag | What it does |
|---|---|
| `-a <agent>` | Which agent to install for. Use `'*'` for every agent the CLI supports. |
| `-g` | Install globally instead of in the current project |
| `--copy` | Copy files instead of creating a symlink (useful on Windows or if symlinks cause problems) |
| `-y` | Skip confirmation prompts |
| `--list` | Show the skills in the repo without installing |

Other agents: replace `antigravity` with `antigravity-cli`, `claude-code`, `cursor`, `windsurf`, `codex`, `gemini-cli`, `github-copilot`, `cline`, and more. See [supported-agents.md](supported-agents.md).

### Update or remove

```bash
npx skills update denvora-ai-skills
npx skills remove denvora-ai-skills
```

---

## Option B: Manual copy

1. Download this repo (green **Code** button > **Download ZIP**) and unzip it, or `git clone` it.
2. Copy the folder `skills/denvora-ai-skills` (the whole folder, not just `SKILL.md`) to:

   | Scope | Antigravity | Antigravity CLI |
   |---|---|---|
   | Project | `<your-project>/.agents/skills/` | `<your-project>/.agents/skills/` |
   | Global | `~/.gemini/antigravity/skills/` | `~/.gemini/antigravity-cli/skills/` |

   `~` means your home folder: `C:\Users\<you>` on Windows, `/Users/<you>` on macOS, `/home/<you>` on Linux.

3. The result should look like:

   ```
   .agents/
     skills/
       denvora-ai-skills/
         SKILL.md
         references/
   ```

4. **Start a new agent session** (new conversation). Agents scan for skills when a session starts.

> [!NOTE]
> Some older Antigravity versions and guides use `.agent/skills/` (no "s"). If the skill is not detected in `.agents/skills/`, check your agent's docs for the folder it scans.

---

## Option C: Claude (upload a `.skill` file)

1. Go to the [Releases page](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/releases) and download `denvora-ai-skills.skill` (or `.zip`) from the latest release.
2. In Claude, open **Settings** and find the **Skills** section (in some versions it is under **Capabilities**), then upload the file.
3. Make sure the skill is turned on, then start a new chat.

To build the file yourself instead of downloading it:

```bash
# macOS / Linux
./scripts/package-skill.sh

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\scripts\package-skill.ps1
```

The file appears in `dist/`.

---

## Option D: Any other AI (no skill support)

If your AI tool does not support skills (for example a plain chat window), you can still use the rules:

- **If the AI can read files in your project:** copy the `skills/denvora-ai-skills` folder into your project and tell it:

  ```
  Read skills/denvora-ai-skills/SKILL.md and follow it for this whole conversation.
  ```

- **If it cannot read files:** paste the contents of `SKILL.md` at the start of the chat, then ask your question.

More ready-to-copy prompts: [prompt-templates.md](prompt-templates.md).

---

## Check that it works

1. Start a **new** agent session.
2. Ask something like: `Fix this error: TypeError: Cannot read properties of undefined`.
3. Signs the skill is active:
   - The AI asks for or reads the actual code before changing it.
   - It uses labels like **[Certain] / [Likely] / [Unsure]** (or **[Pasti] / [Kemungkinan] / [Belum yakin]**).
   - It ends with a short report: what it did, what it verified, what it did not.

If none of this happens, see [Troubleshooting](#troubleshooting).

---

## Troubleshooting

| Problem | Try this |
|---|---|
| `npx: command not found` | Install Node.js 18+ from [nodejs.org](https://nodejs.org/), then reopen the terminal |
| Skill installed but AI ignores it | Start a **new** session. Check the folder contains `SKILL.md` directly inside `denvora-ai-skills/`. You can also say: "Use the denvora-ai-skills skill." |
| Installed in the wrong place | Run `npx skills list` to see where skills are installed |
| Symlink errors on Windows | Re-run with `--copy` |
| Still stuck | [Open an install issue](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=install-problem.yml) with the command and full output |
