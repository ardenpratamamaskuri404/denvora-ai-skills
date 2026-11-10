# Contributing to denvora-ai-skills

Thanks for helping! This project gets better mostly through **real cases**: moments where an AI still guessed, over-claimed, or confused a beginner. You do not need to be an expert to help.

Kamu boleh menulis issue atau PR dalam Bahasa Indonesia atau English.

## Ways to help

| Effort | What you can do |
|---|---|
| 2 minutes | Star the repo, or report a case with the ["AI still hallucinated" issue template](https://github.com/ardenpratamamaskuri404/denvora-ai-skills/issues/new?template=hallucination-report.yml) |
| 15 minutes | Run a few cases from [tests/test-cases.md](tests/test-cases.md) and share your results |
| 1 hour | Propose a new rule or example, translate prompt templates, or add a stack reference |

Look for issues labeled **good first issue** if you want somewhere to start.

## Project layout

```
skills/denvora-ai-skills/
  SKILL.md            <- the core rules (keep it short)
  references/         <- detailed guides the AI reads only when needed
tests/                <- prompt-based test cases, scoring rubric, results
scripts/              <- validate and package the skill
docs/                 <- install guide, supported agents
```

## Principles for changes

1. **Every rule should come from a real failure.** Link the issue or describe the case in your PR.
2. **Keep `SKILL.md` short.** It is loaded into the AI's context each time the skill triggers. Put detail and long examples in `references/` and link to them.
3. **Do not make small tasks slow.** A rule that adds questions or long reports to a one-line fix is a regression. Check case S1 in the test suite.
4. **No invented claims.** Docs and READMEs must not include statistics or "tested on X" claims unless there is a result file in `tests/results/` backing it up.
5. **Write for beginners.** Plain words, short sentences.

## Making a change

1. Fork the repo and create a branch: `git checkout -b fix/short-description`
2. Edit the skill or docs.
3. Validate:

   ```bash
   python scripts/validate-skill.py
   ```

4. Test your change on at least one agent with the relevant cases from `tests/test-cases.md`. Say in the PR which agent and model you used.
5. Add a line under **Unreleased** in [CHANGELOG.md](CHANGELOG.md) if the change affects users.
6. Open a pull request using the template.

## Commit messages

We use short [Conventional Commits](https://www.conventionalcommits.org/) style prefixes:

- `feat(skill):` new rule or reference
- `fix(skill):` correct a rule that misbehaved
- `docs:` README and guides
- `test:` test cases or results
- `build:` / `ci:` scripts and workflows
- `chore:` everything else

## Adding a stack reference (v1.x)

Stack-specific guides (Next.js, Laravel, Flutter, FastAPI, ...) go in `skills/denvora-ai-skills/references/stacks/<stack>.md`. Focus on what AIs commonly get wrong for that stack: version differences, invented config keys, outdated patterns. Link it from `SKILL.md` with one line saying when to read it.

## Code of conduct

Be kind and patient, especially with beginners. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
