# Verification checklist

Use this checklist before claiming a task is "done", "fixed", or "working".

## The evidence rule

A claim is **[Certain]** (or **[Pasti]**) only when you have direct evidence from this session:

- You ran a command and inspected its output, or
- You read the exact project file or official documentation that proves it.

Otherwise, label it **[Likely]** (**[Kemungkinan]**) or **[Unsure]** (**[Belum yakin]**).

## Before claiming a slice works

- [ ] Code is saved in the right file(s), following existing project structure
- [ ] Every imported package is listed in the project's dependency file (`package.json`, `requirements.txt`, `composer.json`, etc.)
- [ ] Every function, method, prop, and CLI flag exists in the installed version
- [ ] Unrelated files were **not** modified, moved, or reformatted
- [ ] No temporary debug logs (`console.log`, `print`, `dd`), scratch scripts, or `.bak` files are left behind
- [ ] No real logic was silently replaced with hardcoded mock data, skipped tests (`.skip`/`xit`), or weakened assertions
- [ ] The strongest available check was run **after the final edit** (tests, build, type-check, run, or lint) and its output was inspected
- [ ] Static build/type-check is not confused with runtime verification (compilation passing does not prove UI/API behavior works)
- [ ] Existing tests and build still pass

## Before claiming a bug is fixed

- [ ] The original error message and stack trace were read (or reproduced)
- [ ] After the fix, the steps that triggered the error no longer fail
- [ ] Any failed fix attempts from earlier hypotheses were reverted cleanly
- [ ] The root cause is fixed, not silently swallowed with an empty `try/catch`

## When you cannot run commands

Some AI environments (such as web chat windows) cannot execute terminal commands. In that case:

1. State clearly: "I could not run this command in this environment."
2. Provide the exact command(s) in a copyable code block.
3. Describe what the user should see if it works, and what error output to share if it fails.

Example:

```text
[Not verified] I cannot run terminal commands here. Please run:

    npm run build

You should see "Compiled successfully". If an error appears, copy the full message from the terminal and paste it here.
```

## Common verification commands by stack

Always check the project's `package.json` / `Makefile` / `README.md` first to see which scripts are configured.

| Stack | Run | Test | Build / Static check |
|---|---|---|---|
| Node / React / Next.js | `npm run dev` | `npm test` | `npm run build`, `npx tsc --noEmit`, `npm run lint` |
| Python / FastAPI / Django | `python main.py` / `uvicorn app.main:app --reload` | `pytest` | `python -m py_compile <file>.py`, `ruff check .` |
| Laravel / PHP | `php artisan serve` | `php artisan test` | `php -l <file>.php` |
| Flutter / Dart | `flutter run` | `flutter test` | `flutter analyze` |
| Go | `go run .` | `go test ./...` | `go vet ./...`, `go build ./...` |

## Phrases to avoid without evidence

Do not say: *"should work"*, *"this will fix it"*, *"everything is done"*, *"fully tested"*, or *"production ready"* unless backed by verification output. State specifically what you checked.
