# PRD Blueprint, Tool Synergy & Secret Protection Implementation Plan

> **For agentic workers:** Implementation plan for branch `feat/v0.2-enhancements`. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement PRD blueprint, tool orchestration protocol, secret & privacy protection shield, and Kiro IDE integration.

**Architecture:** Add on-demand reference guides following progressive disclosure, harden core rules in `SKILL.md` with secret redaction and tool safety, and expand documentation across README and docs.

**Spec:** `docs/superpowers/specs/2026-11-13-prd-planning-and-security-design.md`

## Global Constraints
- Only Markdown (`.md`) files inside `skills/denvora-ai-skills/`.
- `SKILL.md` must stay under 2,000 words.
- All internal repository Markdown links must be valid.
- `npm run validate` must pass with 0 errors.

---

### Task 1: Create PRD & Architecture Blueprint (`references/prd-blueprint.md`)
- [ ] Write `skills/denvora-ai-skills/references/prd-blueprint.md` with structured templates for Overview, Scope, Tech Stack, Data Models, Slices, and Verification Criteria.

### Task 2: Create Tool & External Reference Synergy Protocol (`references/tool-orchestration.md`)
- [ ] Write `skills/denvora-ai-skills/references/tool-orchestration.md` covering query formulation, secret filtering, tool execution bounds, skeptical review, and fallback to local files.

### Task 3: Harden Core Rules in `SKILL.md` & `references/security-checklist.md`
- [ ] Update `SKILL.md` to reference PRD blueprint in Big Tasks, expand Rule #13 with Secret & Privacy Shield (`[REDACTED_SECRET]`, file blacklist, no environment dumps), and reference `tool-orchestration.md`.
- [ ] Update `references/security-checklist.md` with secret isolation, tool boundary, and sensitive file checks.

### Task 4: Integrate Kiro Support Across Documentation
- [ ] Update `README.md` with Kiro in header, quick start (`-a kiro`), and native steering/skills guide.
- [ ] Update `docs/installation.md` with dedicated Kiro setup guide (`.kiro/skills/`, steering files, CLI).
- [ ] Update `docs/supported-agents.md` adding Kiro to the compatibility table.

### Task 5: Update PRD & Changelog
- [ ] Update `product/PRD.md` with new features and Kiro support.
- [ ] Update `CHANGELOG.md` under `[Unreleased]`.

### Task 6: Validate & Verify
- [ ] Run `npm run validate`.
- [ ] Check word count of `SKILL.md`.
- [ ] Verify git status and commit changes cleanly.
