# Test fixtures

These are minimal project setups used by the test cases in [`test-cases.md`](../test-cases.md). Each fixture is a tiny, self-contained project that can be dropped into a temporary directory for testing.

## How to use

1. Copy the fixture folder to a temporary location.
2. Run `npm install` (or the stack's equivalent) if a `package.json` exists.
3. Follow the test case instructions in [`test-cases.md`](../test-cases.md).

## Fixtures

| Folder | Used by | Stack | Description |
|---|---|---|---|
| `react-null-user/` | F1 | React (Vite) | Page that reads `user.name` while `user` is `null`. Triggers a TypeError. |
| `express-todo/` | E1, E2 | Express.js | Simple todo API with established folder structure and naming conventions. |
| `python-empty/` | L1 | Python | Empty Python project with just `requirements.txt` and a `main.py`. |
