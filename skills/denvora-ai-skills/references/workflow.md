# Workflow in detail

Read this when a task is more than a tiny fix. It expands each step of the Workflow in `SKILL.md`.

## 1. Understand

- Restate the goal in one or two sentences, in the user's language.
- Separate **what they asked** from **what you assume**. Write the assumptions down.
- If the request is vague ("make my app better"), propose 2 or 3 concrete options and let the user pick. Do not silently start a large rewrite.

**Ask only if blocking.** A question is blocking when a wrong guess wastes significant work or risks losing data:

| Blocking (ask first) | Not blocking (choose a sensible default and state it) |
|---|---|
| Which framework/language if the folder is empty | Variable or helper function names |
| Deleting, resetting, or migrating existing user data | Minor UI spacing or styling details |
| Paid service vs free alternative | Which existing project helper to reuse |
| Upgrading a major dependency version | Folder for a new component (follow existing project layout) |

Ask at most 1 to 3 questions at once, ideally multiple choice.

## 2. Inspect

Before writing any code, inspect the project:

- **Language and framework:** check `package.json`, `requirements.txt` / `pyproject.toml`, `composer.json`, `pubspec.yaml`, `go.mod`, `Cargo.toml`, etc.
- **Installed versions:** installed versions determine which APIs exist (e.g., Next.js App Router vs Pages Router, Tailwind v3 vs v4, React 18 vs 19, Laravel 10 vs 11). See [stack-pitfalls.md](stack-pitfalls.md) for common version traps.
- **How to run and test:** check `scripts` in `package.json`, `Makefile`, `README.md`, test folders, linter, and type checker.
- **Existing conventions:** check where routes, components, models, and styles live, how errors are handled, and which libraries are already installed.

If the project folder is empty, confirm the stack with the user before scaffolding.

## 3. Plan

- Break the work into small, checkable slices.
- Typical order: data/model → core logic → UI → edge cases.
- For large features or structural changes, show the plan and wait for confirmation before modifying files.

Example plan for "build a todo app":

```text
1. Scaffold the project and confirm the blank page runs
2. Render a static list of sample todos
3. Add a form to create a new todo
4. Add complete and delete actions
5. Persist todos to localStorage so they survive page refresh
```

## 4. Build one slice (without making a mess)

- Write the minimum code needed for the current slice.
- **Touch only relevant files.** Do not reformat, rename, or move unrelated files.
- **Reuse existing packages.** Do not install a new dependency if the project already has a tool for the job. Ask before adding or upgrading packages.
- **Verify APIs exist** in the installed version before calling them. If you cannot verify, label it **[Unsure]**.

## 5. Verify the slice

Use the strongest check available, in this order:

1. Automated tests (`npm test`, `pytest`, `php artisan test`, `flutter test`, `go test ./...`)
2. Build / compile / type-check (`npm run build`, `npx tsc --noEmit`, `flutter analyze`, `cargo check`)
3. Run and observe (start dev server, run script, test endpoint)
4. Lint (`npm run lint`, `ruff check .`)
5. If commands cannot be run in your environment: provide the exact command for the user to run and describe the expected output.

If your change breaks the build or existing tests and you cannot fix it immediately, **revert the broken change** so the user's project is never left in a broken state.

See [verification-checklist.md](verification-checklist.md).

## 6. Repeat

Do not start the next slice while the current slice is broken or unverified.

## 7. Report

Use the report format in `SKILL.md`. Be specific: "`npm run build` exited with 0 errors" is useful; "should be fine" is not.
