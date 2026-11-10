# Workflow in detail

Read this when a task is more than a tiny fix. It expands each step of the Workflow in `SKILL.md`.

## 1. Understand

- Restate the goal in one or two sentences, in the user's language.
- Separate **what they asked** from **what you assume**. Write the assumptions down.
- If the request is vague ("make my app better"), propose 2 or 3 concrete options and let the user pick. Do not silently choose a big rewrite.

**Ask only if blocking.** A question is blocking when a wrong guess wastes significant work or is risky:

| Blocking (ask) | Not blocking (assume and state it) |
|---|---|
| Which framework/language if the project is empty | Variable names, file names |
| Delete or migrate existing data | Styling details |
| Paid service vs free alternative | Which of two equivalent helpers to use |
| Production vs local only | Folder for a new component (follow existing pattern) |

Ask at most 1 to 3 questions at once, ideally multiple choice.

## 2. Inspect

Before writing code, find out:

- **Language and framework**: look at `package.json`, `requirements.txt` / `pyproject.toml`, `composer.json`, `pubspec.yaml`, `go.mod`, `Cargo.toml`, etc.
- **Versions**: the installed versions decide which APIs exist. Next.js 13 vs 15, Laravel 10 vs 11, Flutter 3.x, Python 3.8 vs 3.12 all differ.
- **How to run**: `scripts` in `package.json`, `Makefile`, README, `artisan`, `manage.py`.
- **How to test**: existing test folder and test command, linter, type checker.
- **Existing patterns**: where routes, components, models, and styles live; naming style; state management.

If the project folder is empty, say so and agree on the stack before scaffolding.

## 3. Plan

- Break the work into slices. Each slice produces something that runs or can be checked.
- Typical order: data/model, then logic, then UI, then polish.
- For big or risky work, show the plan and wait for confirmation.

Example plan for "build a todo app":

```
1. Scaffold the project and confirm it runs (blank page)
2. Show a hard-coded list of todos
3. Add a form to create a todo
4. Mark done / delete
5. Save to localStorage so todos survive a refresh
```

## 4. Build one slice

- Write the minimum code for this slice.
- Match existing style, structure, and libraries. Do not add a new library when the project already has one for the job.
- Before using any library, confirm it is installed (or install it explicitly and tell the user).
- Before using any function or option, confirm it exists in the installed version. If you cannot check, label it **[Unsure]**.

## 5. Verify the slice

Use the strongest check available, in this order:

1. Automated tests (`npm test`, `pytest`, `php artisan test`, `flutter test`)
2. Build / compile / type-check (`npm run build`, `tsc --noEmit`, `flutter analyze`)
3. Run it and observe (start the server, run the script, call the endpoint)
4. Lint
5. If you cannot run anything: give the user the exact command and the expected result

See `verification-checklist.md`.

## 6. Repeat

Do not start the next slice while the current one is broken.

## 7. Report

Use the report format in `SKILL.md`. Be specific: "ran `npm run build`, 0 errors" is useful; "should be fine" is not.
