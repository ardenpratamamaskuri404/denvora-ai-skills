# Test suite

These tests check whether denvora-ai-skills **actually** changes AI behavior. They are manual, prompt-based tests: you run the same prompt with and without the skill and score the response.

> We do not publish improvement numbers until they come from real runs recorded in `results/`. No invented statistics.

## Files

| File | Purpose |
|---|---|
| [test-cases.md](test-cases.md) | 15 test prompts with expected behaviors |
| [scoring-rubric.md](scoring-rubric.md) | How to score each response (0-2 per check) |
| [results/TEMPLATE.md](results/TEMPLATE.md) | Copy this to record a test run |

## How to run a test round

1. **Pick an agent and model** (for example: Antigravity + Gemini, or Claude). Write them down; results differ per model.
2. **Baseline run (without the skill):**
   - Make sure the skill is **not** installed (or temporarily move its folder out).
   - Start a **new** agent session for each test case.
   - Paste the prompt exactly as written. Use the fixture project if the case needs one.
   - Save the full response (copy text or screenshots).
3. **Skill run (with the skill):**
   - Install the skill (see the main README).
   - Start a new session again and paste the same prompt.
   - Save the full response.
4. **Score both** with [scoring-rubric.md](scoring-rubric.md).
5. **Record** in a copy of `results/TEMPLATE.md`, named like `results/2026-11-10-antigravity-gemini.md`.
6. **Turn every failure into a fix:** if the AI still guessed or over-claimed with the skill on, add or sharpen a rule or example in `SKILL.md` or a reference file, then re-run that case.

## Tips for fair results

- One new session per prompt, so earlier answers do not leak into later ones.
- Do not help the AI during the run. If it asks a question, give the short answer listed in the test case (if any) and nothing more.
- Run each case at least twice if you can; AI output varies.
- Note when the skill **did not trigger**. That is a description problem, not a rules problem, and is worth an issue on its own.

## Fixtures

Some cases need a small project to work on. Use any small real project in the stack named in the case, or create one with the stack's official starter (for example `npm create vite@latest`). Write down which one you used in the results file so others can repeat it.
