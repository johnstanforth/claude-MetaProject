# LATER-005 — Context-Preserving Search (offload bulk grep/rg so the orchestrator's LLM context lasts longer)

- **Captured:** 2026-06-16, MetaProject session (immediately after a broad QR-code sweep dumped **397 KB** of mostly-irrelevant grep output straight into the orchestrating Claude's context — and didn't even find the target on the first, mis-scoped pass)
- **Status:** LATER — awaiting weekly backlog review; not yet assigned
- **Eventual owning project:** TBD — most likely a **Claude skill** (cf. the `research-pdf` skill), or a feature of **`aixodev-aixocode`** (the session manager), or a **`_workflows/`** workflow doc. Decide during triage.
- **Related:** [[LATER-001-workflow-lineage-and-hybrid-formalization]] (the "hybrid deterministic + LLM workflow" theme — a deterministic search step feeding the LLM is exactly that); each repo's `_workflows/EFFICIENCY_RULES.md` (esp. **E9** — "use system operations like `mv`/`cp` instead of piping file content through LLM context" — this is the same principle, applied to *search results*); the `_skills/research-pdf` precedent (offload heavy work to a subprocess, return only the artifact).

---

## The problem (context, not correctness)

This is **purely about preserving the orchestrating Claude's LLM context** so that a John + Claude collaboration session (with Claude as the main-loop orchestrator) can run as long as possible. It is *not* about search correctness.

When the orchestrator runs a broad `grep`/`rg` across many files, the **raw results flood its context** — often hundreds of KB — even when the search **fails to find what we wanted**. Every such dump permanently consumes context budget the session can't get back. Concrete example from the session that captured this: a single QR-code sweep across the wrong scope returned **397 KB** of minified-JS / saved-web-article noise; a second, correctly-scoped pass still returned 128 hits (most of them noise) before the signal was isolated. That is a lot of irreversible context spent on a lookup whose useful answer was ~5 lines.

## The idea

A **context-preserving search facility** that runs *all* the heavy I/O — many `grep`/`rg`/`find` passes, broad then narrow, with filtering, ranking, dedup, and clustering — in a **disposable context** (a subprocess, a script, or a sub-agent whose own context is throwaway), and returns to the orchestrator **only the final, distilled, relevant results** (file:line + a one-line excerpt, ranked; plus a 1–2 line summary of what was searched and what was excluded). The 300 KB of intermediate noise never crosses back into the orchestrator's context.

## Shapes to consider (decide at triage)

1. **A "search sub-agent" pattern / skill.** Dispatch a cheap agent (or the existing `Explore` agent) to do the sweeping; it returns only the distilled hits. Formalize this as the *default* for any broad/unknown-yield search, so the orchestrator stops running them inline. (Partially possible today; the value is making it a one-call, well-tuned default.)
2. **A wrapper script / skill around `rg`** with smart defaults baked in (see "lessons" below): excludes, scoping, output caps, noise-filtering, ranked/clustered output → returns a compact result blob. Deterministic, cheap, no model tokens for the bulk pass.
3. **An `aixocode` feature** — since `aixodev-aixocode` already manages the session, it could expose a "scoped project search" tool that returns only distilled results to the agent.

## Lessons to bake in (hard-won this session)

- **Scope to the symlinked *project* dirs, not the umbrella dirs.** Searching `~/Code/DiviaAI/` swept in millions of lines of external/build code; searching `_projects/divia*/` (the symlinks) is the right scope. (This is the single biggest noise source.)
- **Exclude by default:** `.git`, `node_modules`, `.venv`/`venv`, `target`, `build`, `dist`, `.svelte-kit`, `.dart_tool`, `.gradle`, `__pycache__`, `_REFERENCE/_EXTERNAL` (saved web articles / vendored refs), `*.lock`, `*.min.js`, `*.map`, and binaries (`-I`).
- **Single-word patterns need post-filtering** before they reach the orchestrator (e.g. a bare `qr` matches minified-JS identifiers `qr()`/`Qr`); cluster + rank + drop obvious noise in the disposable context.
- **Find-then-read keeps context lean:** locate candidate files first, return a compact hit list, and only *then* read the few relevant regions — rather than streaming match bodies.
- Optionally surface a **"searched X / excluded Y / N hits, here are the top K"** one-liner so the orchestrator knows the coverage without seeing the raw output.

## Why it matters

At 20+ projects, "search across everything" is a routine operation, and today it's one of the most context-expensive things the orchestrator does — directly shortening how long you and Claude can work together in one session. Moving the bulk I/O off the orchestrator's context (the same move `EFFICIENCY_RULES.md` E9 already makes for file content) is a high-leverage, compounding win for session longevity.
