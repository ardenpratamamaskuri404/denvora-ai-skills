# Debugging protocol

Use this whenever something fails: an error message, a blank page, wrong output, a failing test.

The goal is to find the **root cause from evidence**, not to try random fixes until something sticks.

## Step 1: Get the full error

- Read the whole message: error type, text, file, line number, stack trace.
- If the user only said "it doesn't work", ask for:
  - the exact error text (copy-paste, not a summary)
  - what they did right before it happened
  - where it appears (terminal, browser console, phone screen)
- For a browser app, ask them to open DevTools (F12) > Console and copy any red errors.

## Step 2: Reproduce

- Find the exact command or click steps that trigger the problem.
- If you can run it yourself, reproduce it before changing anything.
- If it only happens sometimes, note when (first load, after login, on mobile only).

## Step 3: Form one hypothesis

- Read the code at the location in the stack trace. Read it, do not guess what it contains.
- Write one hypothesis with a confidence label:
  - "[Likely] `data` is undefined because the fetch has not finished when the component renders."
- Common root causes to consider:
  - Wrong or missing import, package not installed, version mismatch
  - Undefined/null value, typo in a name, wrong file path
  - Async timing (using data before it arrives)
  - Environment: missing `.env` value, wrong port, server not running
  - Cache/build leftovers (try a clean restart only after ruling out the code)

## Step 4: Test with one change

- Make **one** change, or add a log/print to confirm the hypothesis.
- Do not change several things at once; you will not know which one mattered.

## Step 5: Check the result

- Re-run the same steps from Step 2.
- **Fixed:** confirm, then remove any temporary debug logs.
- **Not fixed:** undo the change (do not leave failed attempts in the code), update the hypothesis using what you learned, go back to Step 3.

## Step 6: Stop after 3 failed attempts

If three hypotheses fail:

1. Stop changing code.
2. Re-read the original error from scratch.
3. Check versions and official docs for the exact library/function involved.
4. Tell the user honestly:
   - what you tried
   - what you have ruled out
   - what you think is happening now, with a confidence label
   - what information would help (logs, versions, a screenshot)

## Anti-patterns

| Do not | Why |
|---|---|
| Wrap code in `try/catch` just to hide the error | The bug is still there, now silent |
| Reinstall everything as a first step | Slow, rarely the cause, hides the real issue |
| Rewrite the whole file | Introduces new bugs, loses the original evidence |
| Say "fixed" without re-running | Unverified claim |
| Blame the user's environment without evidence | Often wrong, and unhelpful |

## Explaining the fix to a beginner

Keep it to three parts:

1. **What was wrong** (one sentence, plain words)
2. **What I changed** (file and line)
3. **How you can confirm** (the command or click steps)
