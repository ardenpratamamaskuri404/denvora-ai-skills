# Tool & External Reference Orchestration

Read this when your AI environment provides external tools, documentation lookups, codebase indexing, or protocol-based extensions (such as MCP servers or IDE extensions).

This guide establishes how `denvora-ai-skills` acts as the **Architect & Evaluator** while coordinating with external tools as **Sensors & Executors**—guaranteeing high precision without risking secret leaks or project damage.

---

## 1. Division of Responsibility

| Role | Responsibility | Guardrail |
|---|---|---|
| **Skill (Denvora)** | Formulates structured requests, defines PRDs/slices, filters sensitive data, and evaluates results. | **The Shield & Architect** — enforces honesty, small steps, and secret redaction. |
| **Tools & Extensions** | Queries live documentation, inspects codebase AST/symbols, checks database schemas, or runs browser checks. | **The Sensors & Hands** — provides factual evidence instead of training-data guesses. |

---

## 2. The Secret & Privacy Shield (Strict Guardrails)

When calling any external tool, search engine, documentation fetcher, or protocol-based tool:

### 🚫 1. Absolute Secret Blacklist
**NEVER** pass or inspect files containing sensitive credentials as tool parameters or context payloads:
- `.env`, `.env.*`
- `credentials.json`, `client_secrets.json`
- `id_rsa`, `*.pem`, `*.key`, `*.keystore`
- Token files, database passwords, or private signing certificates.

### 🔒 2. Automatic Redaction (`[REDACTED_SECRET]`)
If an error message, stack trace, or terminal output contains an API key, bearer token, or password, **redact it immediately** before passing it into any tool argument or chat response:

```text
// Bad:
tool_call({ query: "Error with key sk-live-9382104810293" })

// Good:
tool_call({ query: "Error with key [REDACTED_SECRET]" })
```

### 🚫 3. No Environment Variable Dumping
Never invoke commands or tools that dump `process.env`, `env`, or system configuration into chat logs or external servers.

---

## 3. Four Workflow Protocols for Tool Usage

### Protocol A: Reference & Documentation Lookups (Anti-Hallucination)
When you are unsure whether an API, method, or config option exists in the installed framework version:
1. **Formulate a targeted query:** Search for the exact library name, installed version, and method (e.g. `"Next.js 15 cookies() await requirement"`).
2. **Do not dump unrelated code:** Send only the specific function signature or error message.
3. **Compare with installed versions:** Confirm that the documentation matches what is actually listed in `package.json`, `requirements.txt`, or `composer.json`.

### Protocol B: Codebase Tracing & Symbol Search
In large repositories:
1. **Use symbol search over full rewrites:** Trace callers, type declarations (`.d.ts`), and interfaces before modifying a file.
2. **Inspect boundaries:** Understand where data enters and exits the component.
3. **Touch only target files:** Having tool access to the whole repository is **not** permission to reorganize unrelated folders.

### Protocol C: Skeptical Evaluation (Never Trust Tool Output Blindly)
Tools and external sources can return outdated or generic answers:
1. **Treat tool output as an unverified suggestion (`[Likely]` or `[Unsure]`).**
2. **Validate locally:** After applying a suggestion, run the project's actual build or test command (`npm run build`, `npm test`, etc.).
3. **Do not claim success** until the local check passes.

### Protocol D: Graceful Fallback
If an external tool or protocol extension is not available in the user's environment:
- **Do not fail or crash.**
- **Fall back to local inspection:** Read local type definitions (`node_modules/`, `site-packages/`, `vendor/`), run `--help` commands, or check manifest files directly.
- Label any remaining unverified assumptions with **[Unsure]** / **[Belum yakin]**.
