# Contributing to denvora-ai-skills

Thank you for your interest in contributing! **denvora-ai-skills** improves primarily through **real-world cases**—moments where an AI coding assistant invented an API, skipped verification, or behaved in a way that confused a developer or beginner.

*(Anda dapat menulis Issue atau Pull Request dalam Bahasa Indonesia maupun Bahasa Inggris.)*

## Ways to Contribute

| Time Needed | How You Can Help |
|---|---|
| **2 minutes** | Star the repo or submit an [AI Hallucination / Inaccuracy Report](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=hallucination-report.yml) when an AI makes an unverified claim or invents code |
| **15 minutes** | Run a few benchmark prompts from [`tests/test-cases.md`](tests/test-cases.md) on your preferred AI agent and share the results |
| **1 hour** | Propose a sharper rule or example, improve documentation, or add a framework-specific reference guide |

Look for issues labeled **`good first issue`** if you want a clear place to start.

## Repository Structure

```text
skills/denvora-ai-skills/
  SKILL.md            <- Core rules (kept compact to save context window tokens)
  references/         <- Detailed guides loaded by the AI on demand
tests/                <- 15 benchmark test prompts, scoring rubric, and results template
scripts/              <- Maintainer scripts to validate and package the skill
docs/                 <- Installation guide, supported agents table, and prompt templates
```

## Design Principles for Changes

1. **Every rule must solve a real failure.** Link the issue or describe the real AI failure case in your Pull Request.
2. **Keep `SKILL.md` concise.** `SKILL.md` is loaded into the AI's context whenever the skill activates. Keep the core file tight and place detailed checklists or examples in `references/`.
3. **Never compromise user project safety.** Every rule should protect the user's codebase from unrequested changes, leftover debug clutter, or destructive commands.
4. **Keep small tasks fast.** A rule that forces a 10-step plan on a one-line variable rename is a regression (test against case `S1` in [`tests/test-cases.md`](tests/test-cases.md)).
5. **No unverified claims.** Never add statistics or benchmark numbers to the documentation unless backed by a recorded test run in `tests/results/`.
6. **Write clearly for beginners.** Use plain, direct language.

## Submitting a Pull Request

1. Fork the repository and create a branch:
   ```bash
   git checkout -b feat/short-description
   ```
2. Make your changes in `skills/denvora-ai-skills/` or `docs/`.
3. Run the validator script to check frontmatter, character limits, and links:
   ```bash
   python scripts/validate-skill.py
   ```
4. Test your change on at least one AI coding assistant using relevant cases from [`tests/test-cases.md`](tests/test-cases.md).
5. Add an entry under **[Unreleased]** in [`CHANGELOG.md`](CHANGELOG.md) if your change affects users.
6. Open a Pull Request using the PR template.

## Commit Message Style

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat(skill):` new rule or reference guide
- `fix(skill):` refinement to an existing rule
- `docs:` documentation updates
- `test:` benchmark test cases or recorded results
- `build:` / `ci:` packaging scripts and GitHub Actions workflows
- `chore:` maintenance and repository configuration

## Code of Conduct

Please be respectful, patient, and welcoming—especially toward beginners. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
