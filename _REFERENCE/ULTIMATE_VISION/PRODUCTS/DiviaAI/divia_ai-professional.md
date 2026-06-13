# Product — Divia.AI Professional

> The real, in-development cross-platform **desktop outliner-editor** for structured thinking and
> writing — and the product that **defines the ecosystem's core vocabulary** (`.dvai`, DiviaCards).
> Also the desktop client for the future Divia.AI Enterprise server.

- **Names:** "Divia.AI Professional" · repo/dir `divia_ai-professional` (some blocks still say `divia_ai-professional-codex`) · package `divia-ai-professional`.
- **Umbrella / venture:** DiviaAI — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md). **Owns the canonical `BRANDING_and_PRODUCTS.md`.**
- **License:** **Proprietary / commercial** ("© 1996–2026 John Stanforth & Divia.AI, Inc.").
- **Status:** 🟢 A genuinely working Rust/Tauri v2 + SvelteKit 5 + TipTap app. Phases 1–2 complete; Phase 3 (rearchitecture) in planning.

---

## What it is (consensus)
A **local-first** professional outliner-editor — *"an outliner that preserves writing flow, grows into structure, and keeps the user's data legible and owned."* Six principles: outliner-native interaction; **write-first, structure-later**; local-first trust; desktop reliability; **AI is opt-in (zero AI by default)**; phase complexity aggressively. **Works today:** the outliner editor (TipTap 3/ProseMirror; adjacency-list tree + TEXT fractional indexing for sibling order), the `.dvai` SQLite document format, dual-FTS5 (porter + trigram) local search, DiviaCards (task + event types) prototyped as first-class. macOS is the active dev platform; Linux/Windows are direction.

### The vocabulary it owns (canonical for the whole ecosystem)
- **`.dvai` — the DVAI / Divia Document Format:** a SQLite single-file format (`application_id` "DVAI", `user_version` migrations, WAL→DELETE for sharing), FTS5 + sqlite-vec + Reciprocal-Rank-Fusion hybrid search (only FTS5 built), optional SQLCipher at-rest encryption with a 3-tier key hierarchy. A parallel open **`.dvai-open`** (JSON+Markdown) format is planned for lock-in avoidance and interop (OPML, JSON Canvas, etc.). *(Note: `.dvai` has three acronym expansions in use — see [`../../ERRATA.md` E-07`](../../ERRATA.md).)*
- **DiviaCards:** the fundamental content unit — *"everything is a DiviaCard"* (a Notion-block analog, but with CSS + optional JS/TS → iframe-isolated mini-apps). Two end-user page types over one internal outline-of-cards: **Outliner** and **Note/Prose**. Planned: open-source + a marketplace + community types, with a global referenced-card model (`diviacard://{repo}/{card_id}` canonical URLs, Figma-style override + Notion-style sync).

### Cross-product role
Excludes server-side/multi-tenant/cloud (that's Enterprise — Pro is its desktop client, shared codebase). AI features planned on the **Claude API with a user-provided key** in the OS keychain (no bundled model, no autocomplete, no training on user data). Collaboration engine = **Loro Tree+Map CRDT** (planned; DiviaMesh transport).

## Ideation & Exploration (capture everything, commit to nothing)
- **From BRANDING / research:** the 30-year origin lore (SAI-4000 → D.I.V.I.A → DIVIA → Divia.AI); DiviaCards as iframe-sandboxed JS widgets + a marketplace; the `.dvai-open` parallel format; the "input-vector" vision (desktop + voice + receipt photo + health feeds → one collective intelligence); per-card revision history with Tier-1 (referenced) vs Tier-2 (embedded) cards and an aggregate activity stream.
- **From backlog:** opt-in AI (summarize-subtree / expand-outline / rewrite via Claude API, accept-reject only, a configurable monthly cost cap); MLO-style computed task priority; a public DiviaCard type registry; WYSIWYG beyond marks (tables/images/math); typewriter/focus modes; virtual scrolling for 10K+ nodes; SQLCipher encryption; Loro CRDT + presence cursors; sqlite-vec hybrid search; FlatBuffers zero-copy JS↔WASM; "game-level <8ms keystroke latency."
- ✦ **New:** `.dvai` **LiveDocuments** (from LATER-002) — give the format a self-refreshing mode (a Swarm agent updates it on a schedule; revision history + "what changed" diffs live inside the SQLite container). This is the substrate for Enterprise "Research Projects" and the KingStratVC partners' brief. *(Not yet in the repo — [`../../ERRATA.md` E-12`](../../ERRATA.md).)* ✦ Resolve the **ADR-002 (WYSIWYG) "withdrawn vs cited"** ambiguity and the live TipTap→ProseMirror migration question — the "settled editor" is actively being re-litigated (see ERRATA). ✦ Position the **opt-in/zero-AI-by-default** stance as a *marketed trust feature* (the anti-"AI slop" promise), pairing it with the Code-Vault guarantee.
