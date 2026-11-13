# Pre-launch security checklist

Run through this before a web app, API, or bot goes online, or whenever the user asks "is it ready to deploy?".

Report each item as done, not applicable, or needs work. Do not claim the app is "secure"; say which items you checked.

## Secret & Privacy Shield (AI & Tool Safety)

- [ ] **No secret forwarding:** Secrets, API keys, tokens, and `.env` files are never passed to external tools, search tools, or protocol extensions.
- [ ] **Automatic redaction:** Any credentials appearing in logs or error traces are masked as `[REDACTED_SECRET]`.
- [ ] **No environment dump:** No commands or scripts execute `printenv`, `process.env`, or dump system variables into chat or files.
- [ ] **Local privacy boundary:** All proprietary user data and credentials remain strictly on the local machine.

## Secrets in Code & Repository

- [ ] No API keys, passwords, tokens, or database URLs are hard-coded in source files
- [ ] Secrets live in environment variables (`.env`) and `.env` is in `.gitignore`
- [ ] A `.env.example` exists with placeholder values only
- [ ] No secrets in git history (if one was committed, tell the user to **rotate the key**, removing it from the file is not enough)
- [ ] Frontend code does not contain secret keys (anything in browser JS is public; `NEXT_PUBLIC_` / `VITE_` variables are visible to everyone)

## Input and data

- [ ] User input is validated on the server, not only in the browser
- [ ] Database queries use parameters / the ORM, not string concatenation (prevents SQL injection)
- [ ] User-generated content is escaped when rendered (prevents XSS); avoid `dangerouslySetInnerHTML` / `{!! !!}` / `v-html` with user data
- [ ] File uploads check type and size

## Authentication and access

- [ ] Passwords are hashed with a proper library (bcrypt, argon2, framework default), never stored in plain text
- [ ] Every protected route/API checks the user is logged in **and** allowed to access that specific record
- [ ] Database rules are set (e.g. Supabase RLS enabled, Firebase rules not left in test mode)

## Configuration

- [ ] Debug mode is off in production (`APP_DEBUG=false`, `DEBUG=False`, etc.)
- [ ] CORS allows only the domains that need it, not `*` for authenticated APIs
- [ ] HTTPS is used in production
- [ ] Error messages shown to users do not reveal stack traces or internal details

## Dependencies

- [ ] Run the stack's audit tool if available (`npm audit`, `pip-audit`, `composer audit`) and report the results honestly
- [ ] No unused or unknown packages were added

## Cost and abuse

- [ ] Paid APIs (AI, SMS, email) have rate limits or usage caps so a bot cannot run up a bill
- [ ] Forms have basic spam protection if public

If you cannot check an item (for example, hosting settings you have no access to), list it under "Not verified" with instructions for the user.
