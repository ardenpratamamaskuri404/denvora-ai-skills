# Verification checklist

Use this before you say "done", "fixed", or "it works".

## The rule

A claim is **[Certain]** only if you have evidence from this session:

- You ran a command and saw the output, or
- You read the exact code or doc that proves it.

Otherwise it is **[Likely]** or **[Unsure]**, and you must say so.

## Before claiming a slice works

- [ ] The code is saved in the right file(s)
- [ ] Every import/package used is actually installed (checked `package.json`, lock file, `requirements.txt`, etc.)
- [ ] Every function, method, option, and flag used exists in the installed version
- [ ] The strongest available check was run (tests, build, type-check, run, lint)
- [ ] The output was read, not just the exit code (warnings can matter)
- [ ] Nothing else was broken: related tests or pages still work

## Before claiming a bug is fixed

- [ ] The original error was reproduced first (or the user's exact error was read)
- [ ] After the change, the same steps no longer produce the error
- [ ] The root cause is explained, not just the symptom hidden (e.g. not wrapping everything in `try/catch` to silence it)

## When you cannot run anything

Some environments do not allow running code. Then:

1. Say clearly: "I could not run this here."
2. Give the exact command(s) to run, in a copyable block.
3. Say what the user should see if it works, and what to send you if it does not.

Example:

```
I couldn't run this here. Please run:

    npm run dev

Then open http://localhost:3000. You should see the todo list.
If you see an error, copy the full message from the terminal and send it to me.
```

## Common checks by stack

These are typical commands. Always confirm they exist in the project (e.g. check `scripts` in `package.json`) before relying on them.

| Stack | Run | Test | Static check |
|---|---|---|---|
| Node / React / Next.js | `npm run dev` | `npm test` | `npm run build`, `npx tsc --noEmit`, `npm run lint` |
| Python | `python main.py` / `uvicorn app.main:app --reload` | `pytest` | `python -m py_compile file.py`, `ruff check .` |
| Laravel / PHP | `php artisan serve` | `php artisan test` | `php -l file.php` |
| Flutter | `flutter run` | `flutter test` | `flutter analyze` |

## Words to avoid without evidence

"should work", "this will fix it", "everything is done", "fully tested", "production ready".
Replace them with what you actually checked.
