# Brief (Business) — Divia.AI Professional

> **Business-side brief** → the **business knowledgebase** (company / corporate structure / brands / Product Lines / Products / GTM / domains / Product Version-Releases). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repo · techstack · Build Lines · Build Envelopes · Triangulation Target · lineage · license · `[DEALBREAKER-HOOK]`s) is the paired **[engineering brief](../../../SOFTWARE_DEV/divia_ai-professional.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge.

## Identity

| Field | Value |
|---|---|
| **Product (full)** | Divia.AI Professional |
| **Short form** | Divia.AI (Pro) |
| **One-line** | A local-first, cross-platform desktop **outliner-editor** for structured thinking and writing — *"an outliner that preserves writing flow, grows into structure, and keeps the user's data legible and owned."* |
| **Ecosystem role** | The product that **owns the ecosystem's core vocabulary** (the `.dvai` document format + DiviaCards), and the **desktop client** for the future Divia.AI Enterprise server. |

## Company / corporate structure · Brands

- **Company / steward:** **Divia.AI, Inc.** (copyright lines run "© 1996–2026 John Stanforth & Divia.AI, Inc."; the brand-history doc frames the *Divia.AI* identity as "2020–present" — copyright-vs-brand-era drift noted in [`../../../ERRATA.md` E-14](../../../ERRATA.md)).
- **Venture / umbrella:** **DiviaAI** — a personal-knowledge & life-organization ecosystem (commercial core ringed by open-source "home" editions, a nonprofit, and a future identity SaaS). See [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **Brand-naming authority:** this product's repo owns the canonical **`BRANDING_and_PRODUCTS.md`** — the naming authority for the whole DiviaAI ecosystem.
- **Brand-spelling note:** prose brand "**Divia.AI**" (dot + caps) vs repo/dir `divia_ai-*` and package `divia-ai-professional`; the `.dvai` format also has three acronym expansions in active use. Pervasive low-stakes drift catalogued in [`../../../ERRATA.md` E-07](../../../ERRATA.md).

## Product Lines → Products

- **Product Line:** the **Divia.AI family of products** (the commercial desktop/server/agents/mobile core of the ecosystem).
  - **Product: Divia.AI Professional.** A **local-first** professional outliner-editor. Six product principles: outliner-native interaction; **write-first, structure-later**; local-first trust; desktop reliability; **AI is opt-in (zero AI by default)**; phase complexity aggressively. Two end-user page types over one internal outline-of-cards: **Outliner** and **Note/Prose**.

### The vocabulary it owns (canonical for the whole ecosystem)

- **`.dvai` — the Divia Document Format:** a SQLite single-file document format. A parallel open **`.dvai-open`** (JSON+Markdown) format is *planned* for lock-in avoidance and interop (OPML, JSON Canvas, etc.). *(The `.dvai` acronym has three expansions in use — [`../../../ERRATA.md` E-07](../../../ERRATA.md). Technical format detail lives in the [engineering brief](../../../SOFTWARE_DEV/divia_ai-professional.md).)*
- **DiviaCards:** the fundamental content unit — *"everything is a DiviaCard"* (a Notion-block analog, but with CSS + optional JS/TS → iframe-isolated mini-apps). Planned: open-source types + a community marketplace, with a global referenced-card model (`diviacard://{repo}/{card_id}` canonical URLs, Figma-style override + Notion-style sync). *(Note: "DiviaCard" is overloaded — a local UI widget in the `divia_cards` repo vs. a cross-app data-interchange type in the ecosystem framing; the two have never been reconciled — [`../../../ERRATA.md` E-05](../../../ERRATA.md).)*

## Cross-product role (within the DiviaAI ecosystem)

- **Pro = the desktop client of Divia.AI Enterprise** (shared codebase / shared stack). Pro deliberately **excludes** server-side / multi-tenant / cloud concerns — those belong to **Divia.AI Enterprise** (the Rust team server; see [`./divia_ai-enterprise.md`](./divia_ai-enterprise.md)). Pro + Enterprise together hold the full PKMS; the **DiviaContacts** family are thin reader/viewers of it.
- **AI features** are planned on the **Claude API with a user-provided key** (in the OS keychain) — no bundled model, no autocomplete, no training on user data. The agents that would power AI features are hosted by **Divia.AI AgentSwarms** — *but that Pro-sidebar / Swarm relationship is asserted from Swarm's side only* ([`../../../ERRATA.md` E-08](../../../ERRATA.md)).
- **Collaboration** is planned as a **Loro Tree+Map CRDT** over the **DiviaMesh** transport (not yet built).

## Product Version-Releases

Pre-1.0 (active development; **Phases 1–2 complete, Phase 03 in flight**). No public `v1.0` released yet. When releases exist they follow the model's **immutable-past / movable-future** rule (past = git-matched historical record; future = a re-bucketable "marketing sketch"). The far-future "Enterprise-connected" and "collaboration" capabilities are sketched as later versions and can slide freely until shipped. *(Engineering Stages/Phases/Sprints → the [engineering brief](../../../SOFTWARE_DEV/divia_ai-professional.md).)*

## Go-to-market / strategic role

- **The trust-first, local-first wedge.** The **opt-in / zero-AI-by-default** stance is positioned as a *marketed trust feature* — the anti-"AI slop" promise (your data is owned, on-disk, in a format the app can explain) — paired with the venture-wide **Code Vault** guarantee (a promised open-source release date on every commercial license; see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md) §4).
- **The vocabulary beachhead.** Because Pro *defines* `.dvai` + DiviaCards, it anchors every downstream ecosystem pitch (Enterprise "Research Projects," cross-app DiviaCard interchange, the DiviaCard marketplace).
- **Market framing** (ecosystem-level, from BRANDING / youtube-strategy): today's assistants are reactive and shallow; a proactive ecosystem that *owns and unifies your real data* is a **10,000× improvement, not 10%** — "the assistant Siri never became."

## Domains (self-contained — from `DOMAIN_LIST.md` / `DOMAIN_MAPPINGS.md`)

- **Canonical product page:** **`divia.ai/diviaprofessionaldesktop/`** (under the company domain `divia.ai`).
- **Redirects/aliases → the canonical page:** **`divia.pro`**, **`diviapro.com`**, **`diviaprofessional.com`** (all 301 → `divia.ai/diviaprofessionaldesktop/`).
- *(Company apex `divia.ai` carries its own alias set — `diviaai.com`, `divia.cc`, `divia.co.in`, `divia.co.uk`, `divia.in`, `divia.one`, `divia.tv`, `divia.uk`, `divia.work` — owned at the venture/company level, not this product.)*

## Ideation & Exploration (capture everything, commit to nothing)

*(Migrated from the prior brief + BRANDING/research — high-value product ideas; none committed.)*
- The 30-year origin lore (SAI-4000 → D.I.V.I.A → DIVIA → Divia.AI) and the "input-vector" vision (desktop + voice + receipt photo + health feeds → one collective personal intelligence).
- **DiviaCards as iframe-sandboxed JS/TS mini-apps** + a community **marketplace**; the parallel **`.dvai-open`** (JSON+Markdown) format; per-card revision history with Tier-1 (referenced) vs Tier-2 (embedded) cards + an aggregate activity stream.
- **Opt-in AI** (summarize-subtree / expand-outline / rewrite via the Claude API; accept-reject only; a configurable monthly cost cap); MLO-style computed task priority; a public DiviaCard type registry; WYSIWYG beyond marks (tables/images/math); typewriter/focus modes.
- ✦ **`.dvai` LiveDocuments** (from LATER-002) — a self-refreshing mode (a Swarm agent updates the document on a schedule; revision history + "what changed" diffs live inside the SQLite container). This is the substrate for Enterprise "Research Projects" and the KingStrat partners' brief. *(Not yet in the repo — [`../../../ERRATA.md` E-12](../../../ERRATA.md).)*
- ✦ Position **opt-in/zero-AI-by-default** as a marketed trust feature, paired with the **Code Vault** "you'll never be orphaned" promise.

## Status

🟢 **Active development — a genuinely working app**, not just research/planning. **Phases 1–2 complete; Phase 03 in flight** (per the `_projects/` index, Phase 03 = ensemble-collab rearchitecture, ~243 commits). macOS is the primary active dev platform; Linux/Windows are target direction. **License:** **Proprietary / commercial** — "© 1996–2026 John Stanforth & Divia.AI, Inc. All rights reserved." *(Several "settled" claims are actively re-litigated — the ADR-002 WYSIWYG decision is cited-as-live in one place and sits withdrawn in another, and a TipTap→ProseMirror editor migration is in question; test-count and `-codex`-dir residue also drift — see [`../../../ERRATA.md` E-11 / E-14](../../../ERRATA.md). Engineering detail → the [engineering brief](../../../SOFTWARE_DEV/divia_ai-professional.md).)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/divia_ai-professional.md`](../../../SOFTWARE_DEV/divia_ai-professional.md).
- Venture: [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- Sibling product (server Pro connects to): [`./divia_ai-enterprise.md`](./divia_ai-enterprise.md).
- Discrepancies: [`../../../ERRATA.md`](../../../ERRATA.md) (E-05 DiviaCard meaning · E-07 brand/`.dvai` spelling · E-08 Enterprise↔Swarm · E-11 ADR-002 / capability-ahead-of-reality · E-12 LiveDocuments · E-14 test-count & copyright drift).
