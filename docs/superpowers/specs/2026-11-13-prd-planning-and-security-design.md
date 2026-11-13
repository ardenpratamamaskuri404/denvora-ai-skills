# Spec: PRD Blueprint, Tool Synergy & Secret Protection Shield

**Date:** 2026-11-13  
**Branch:** `feat/v0.2-enhancements`  
**Status:** Approved  

---

## 1. Goal

Enhance `denvora-ai-skills` with:
1. **PRD & Architecture Blueprint (`references/prd-blueprint.md`)**: A standardized, beginner-friendly format for turning vague user requests or large features into clear Product Requirements Documents and slice breakdowns before writing code.
2. **Tool & External Reference Synergy Protocol (`references/tool-orchestration.md`)**: A universal, non-leaky protocol guiding how AI coding agents formulate queries, orchestrate external tools/references, and skeptically evaluate results without relying on hallucinated APIs.
3. **Secret & Privacy Protection Shield**: Absolute guardrails preventing the exposure of `.env`, API keys, passwords, credentials, or private keys to chat logs, external tools, or committed code, including automatic redaction (`[REDACTED_SECRET]`).
4. **Kiro Integration**: Official support for **Kiro** (AWS-built agentic IDE & CLI featuring Spec-Driven Development, `.kiro/skills/`, and steering rules), reflected across `README.md`, `docs/installation.md`, and `docs/supported-agents.md`.

---

## 2. File Changes

### New Files
- `skills/denvora-ai-skills/references/prd-blueprint.md`
- `skills/denvora-ai-skills/references/tool-orchestration.md`

### Modified Files
- `skills/denvora-ai-skills/SKILL.md`: Update task scaling, Golden Rule #13 (Secret Shield), and link to PRD blueprint and tool orchestration.
- `skills/denvora-ai-skills/references/security-checklist.md`: Add comprehensive secret hygiene, credential isolation, and tool safety checks.
- `README.md`: Add Kiro to header, quick start (`-a kiro`), native configuration, and feature descriptions.
- `docs/installation.md`: Add complete Kiro installation section (`.kiro/skills/`, steering rules, MCP context).
- `docs/supported-agents.md`: Add Kiro to agent compatibility table.
- `product/PRD.md`: Update requirements and roadmap to reflect PRD blueprint, tool orchestration, secret shield, and Kiro.
- `CHANGELOG.md`: Record all new additions under `[Unreleased]`.

---

## 3. Constraints & Validation Criteria
- All skill files in `skills/denvora-ai-skills/` must be 100% Markdown (`.md`).
- `SKILL.md` must stay under 2,000 words.
- All internal repository Markdown links must be valid.
- `npm run validate` must pass with 0 errors.
