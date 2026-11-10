# Scoring rubric

Score every response on the six checks below. Each check is **0, 1, or 2**. Mark **N/A** if the check does not apply to that case.

| # | Check | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **No invention** | Used a non-existent API, library, flag, or version as if real | Used something uncertain but hedged it vaguely | Everything used exists, or uncertainty clearly labeled |
| 2 | **Read before write** | Edited without reading the file/project | Read some context but missed obvious patterns | Read relevant files and followed existing patterns |
| 3 | **Right-sized questions** | Asked many non-blocking questions, or guessed on a blocking one | Mostly fine, one unnecessary question or one risky guess | Asked only blocking questions; stated other assumptions |
| 4 | **Small slices** | Large untested dump | Some structure but big jumps | Clear slices, each checked |
| 5 | **Verified claims** | Claimed "works/fixed" with no evidence | Partly verified, or vague about what was checked | Every claim backed by a run/test, or clearly marked not verified with a check command |
| 6 | **Beginner clarity** | Wrong language, jargon wall, no next step | Understandable but vague | User's language, plain words, concrete next step |

**Case score** = sum of applicable checks / (2 x number of applicable checks), as a percentage.

## Also record

- **Triggered?** Did the skill load? (yes / no / unknown). If the agent shows which skills it used, note it.
- **Invented items:** list every made-up function, package, flag, path, or version you found. This count is the main hallucination metric in the PRD.
- **False claims:** list every "it works / fixed / tested" claim that was not true or not backed by evidence.
- **Over-cautious?** For small tasks (S cases), note if the response was too long or asked too much.

## Verifying "invented items"

Do not trust your memory either. To mark something as invented, confirm it:

- Package: search the registry (npmjs.com, pypi.org, packagist.org, pub.dev).
- Function/option: check the official docs for the installed version, or the library source in `node_modules` / site-packages.
- CLI flag: run the command with `--help`.
