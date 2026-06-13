# Product — aixodev-openhands

> A research/analysis workspace that studies external agent codebases (OpenHands and four others) and
> feeds the lessons back into aixocode and aixodev-web — plus a real "Open Prompt Prototype" of
> prompt-files-build-the-app micro-apps.

- **Repo:** `aixodev-openhands` · **Umbrella:** AIXO.Dev · **License:** Undocumented (own repo); vendored OpenHands TS client is MIT.
- **Status:** 🟡 Phase 00 research **complete** (Claude 26-chapter analysis + a Codex track set); **Phase 01 "Open Prompt Prototype" actually built** — 11 React/FastAPI micro-apps (conversations, hud, kanban, llm, mcp, projects, scheduled, skills, status, vibe, shared), JSON storage, no tests/CI.

## What it is (consensus)
A sibling research repo (to aixocode/aixodev-web) whose output is product decisions, not a shipped product. It analyzes **OpenHands** (All Hands AI's MIT-cored open-core agent harness; $18.8M Series A; event-sourcing + discriminated-union polymorphism + ToM-SWE three-tier memory) and harvests UI/architecture patterns via a localhost no-auth dashboard adapted from `personal-ai-devbox`. **Most important adoption:** map ToM-SWE's three-tier memory onto aixocode Phase 8 analytics. **Most important *defensive* point:** AIXO must **decline** OpenHands' file-based per-conversation persistence — it conflicts with aixocode's byte-for-byte `*_sessions.db` preservation guarantee. Positions aixocode as a *different lane* from agent harnesses: a session-capture wrapper around third-party CLIs, with the preservation guarantee + multi-tool wrapping as the moat.

> ⚠️ This repo's `CLAUDE.md` **permits Sonnet subagents** and pins older Opus versions — contradicts John's standing "always Opus, never Sonnet" rule. See [`../../ERRATA.md` E-10`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From research (15 ranked recs):** three-tier ToM-SWE memory for analytics; per-tool rule-based session cleaning; an `AixoLLM` wrapper centralizing Anthropic `cache_control` (80%+ cache savings); `pg_advisory_lock` around Alembic; OAuth device flow (RFC 8628) with server-side revoke; a StuckDetector + new TUI states; BM25 search over the cleaned corpus; JSON-repair fallback to a cheaper model; MCP CRUD subcommands. Speculative: a hypothetical `aixodev-agent` (augment, don't wrap), an AIXO.Dev Community+Pro open-core split, logical multi-tenancy via `org_id`, ACP as a future external-CLI bridge standard.
- ✦ **New:** the `cache_control`/cost discipline learned here is directly the **effort-tiered / token-economics** concern at the heart of LATER-001/002 and `aixodev-collabs` — consolidate the portfolio's "how we keep agent costs honest" knowledge in one place, sourced from this repo's analysis. ✦ Bring this repo's model policy into line with the global rule (a concrete ERRATA fix).
