# STATUS — Where Every Project Stands

> A current-state snapshot of all 24 managed projects: **what's real today**, and **the one or two
> big things that matter next** — not an exhaustive backlog. Where a project's honest status is
> "Phase 00 research is next," that's what it says. Human judgment applied to surface what's
> *important*, not every pending minor item (those live in each repo's own backlog).

- **As of:** 2026-06-12 · **Basis:** the read-only harvest sweep (see [`README.md`](README.md)).
- **Legend:** 🟢 real working software · 🟡 in active build · 🟠 docs/research only, pre-code · ⚪ empty placeholder.
- Status here is *what the repos actually show*, which sometimes differs from how they describe themselves — see [`ERRATA.md`](ERRATA.md).

---

## AIXO.Dev (ExoDev family — developer collaboration platform)

**🟢 aixodev-aixocode** — *The flagship; most mature thing in the whole portfolio.* Phases 0–7 complete, Phase 8 (Analytics, Knowledge & Ecosystem Expansion) in progress (~4 of 7 sprints), ~45 sprints shipped, ~651 commits, ~1,700+ tests. **Works today:** the full Midnight-Commander-style TUI (workspaces, themes, command palette, collaboration view); lossless Claude Code session archival to SQLite; the whole CLI suite (`scan`/`import`/`archive`/`stats`/`sync`/`hook-event`/`config`); native multi-agent collaboration (CollabPairs + group chat + a guarded code-review workflow); resilient offline sync queue; local analytics. **Next big thing:** the Codex & Gemini session parsers and — the real gap — **live AIXO.Dev server integration** (today the sync target is stubbed; aixocode and aixodev-web are contract-aligned but not yet wired E2E), plus the long-promised **AgentEngine mode** (run platform-defined agent personalities locally).

**🟡 aixodev-web** — *The central platform and strategic hub.* Phases 1–4 complete; Phase 5 (entity-model & platform vision) active; ~695 tests, 25-table schema, 19 API blueprints. **Works today:** project management, issue tracking, lossless AI-session transcript viewer, per-project wiki, GitHub integration, real-time notifications, analytics dashboards, the session-ingest API. **Next big thing:** implement the Phase-5 entity model — the **"Ontology" knowledge-graph** (DomainGraph + ClientDomainGraph + EngagementGraph, ~25→75 tables) — and stand up the **FDSE consulting + platform GTM** (the Palantir-style "Forward-Deployed Software Engineer" strategy from the Apr-2026 Phase-D research). *Note: the most recent activity is product/venture strategy research, not app code.*

**🟢 aixodev-projects** — Phase 01 complete; Phase 02 (Theme Management) **complete** (13 sprints, 912 tests). Grew well past "project tracker" into a serious **design-theme management system** (DB-as-source-of-truth, DESIGN.md ⇄ W3C DTCG interchange, framework-native CSS export for 6 commercial themes). **Next:** Phase 03 (undefined); eventual merge of proven pieces into `aixodev-web`.

**🟡 aixodev-codemap** — Phase 0 research complete (21-track); Phase 1 prototype 2 of 6 sprints (Python **structural** extraction only — symbols/edges; 139 tests). **Next:** the semantic layer — feature-inventory + Leiden clustering, the web UI, and cross-project comparison ("which of my 40 repos implement JWT, and which is canonical?").

**🟠 aixodev-collabs** — Phase 00 research **complete** (a deep ensemble-internals teardown + a 22-track survey of multi-LLM collaboration), zero app code. The design home for the **next-generation cross-vendor collaboration bus** that supersedes the third-party `ensemble` engine. **Next:** build the Flask prototype implementing that R1–R18 design (typed mail bus, cross-vendor task FSM, progress watchdog, human-steering surface).

**🟠 aixodev-workgroups** — Phase 00 pending, zero code. The prototype for **runtime agent task-coordination & assignment** (Flask system-of-record + a FastAPI status sidecar). Conceptual sibling of `aixodev-collabs` and the natural AIXO-side home for "where recurring agent tasks get assigned" (LATER-001/002). **Next:** Phase 00 research to validate the two-process architecture bet.

**🟡 aixodev-openhands** — Phase 00 research complete + a real Phase-01 "Open Prompt Prototype" (11 React/FastAPI micro-apps, JSON storage, no tests). Primarily a **research/analysis workspace** (studied OpenHands & four other external codebases). **Next:** feed its 15 ranked recommendations (notably ToM-SWE three-tier agent memory) into aixocode's Phase 8 and aixodev-web.

**⚪ aixodev-professional** — Forward-looking placeholder; README only, no code. The *planned* **Rust/Tauri desktop edition of the AIXO.Dev Platform**, gated behind aixodev-web's eventual Rust-server migration (v3/v4 era). Intends to share a Rust/Tauri foundation with Divia.AI Professional. **Next:** nothing until deliberately opened — then a Phase 00 to settle desktop architecture. *(Its name & stack conflict with how `aixodev-web` describes the desktop edition — see ERRATA.)*

## DiviaAI (commercial Divia.AI products)

**🟢 divia_ai-professional** — *A genuinely working app, not a plan.* Rust/Tauri v2 + SvelteKit + TipTap local-first **outliner-editor**. Phases 1–2 complete; Phase 3 (rearchitecture) in planning. **Works today:** outliner editing, the `.dvai` SQLite document format, dual-FTS5 local search, DiviaCards (task/event) prototyped. **Defines the ecosystem's core vocabulary** (`.dvai`, DiviaCards) and is the desktop client for the future Enterprise server. **Next big thing:** Phase 3 rearchitecture (possible TipTap→ProseMirror migration), real collaboration (Loro CRDT / DiviaMesh), at-rest encryption, and opt-in AI (Claude API, user-supplied key, "zero AI by default").

**⚪→🟠 divia_ai-enterprise** — *Intentional empty placeholder* — a single provisional README, **not yet even a git repo.** The commercial Rust team server: "a higher-performance, locked-down Rust re-implementation of the DiviaHome server." **Deliberately not started** until DiviaHome reaches a battle-tested v1 + ~30 days of real use. **Next big thing (strategic):** once begun, harden DiviaHome into Rust — and ultimately spin a specialized build into the **Divia.AI Global (SaaS)** identity/auth service behind the "one global username, federated home+work servers" model.

**🟠 divia_ai-swarm** — Just bootstrapped: workflow scaffold + README/CLAUDE only; Phase 00 is next. The Rust server for **containerized hosting of autonomous Divia.AI agents** — the intended **AI backbone of the whole ecosystem** (OpenClaw/NanoClaw family; usable standalone, designed to co-deploy with Enterprise). **Next big thing:** the Phase 00 competitive deep-dive of the agent-framework field + the core Rust stack decisions (async runtime, RPC, container runtime, DB) — and (new in LATER-002) typed deterministic-vs-probabilistic workflow steps.

**🟠 diviacontacts-gmail** — Research **complete** (16 tracks, ~69k words), pre-Phase-00, no code yet. A Chrome MV3 + InboxSDK **CRM-style reader/viewer** that surfaces the Divia.AI PKMS inside Gmail (entity resolution, task/event surfacing, email/call logging) — **Streak/Copper is the explicit model.** **Next:** build the v0 stub-data prototype, then the real extension against the DiviaHome dev/test server. *(Research was done with Fable 5, per John's directive — see ERRATA.)*

**⚪ diviacontacts-android / diviacontacts-iOS** — Empty placeholders (single 0-byte README each). Planned mobile reader/viewers; scope documented only externally in the gmail repo's family table.

## DiviaHome (open-source household hub)

**🟠 diviahome-web** — *The current ~60-day singular focus, but still pre-code* (Phase 00 PENDING; rich vision docs, empty backlog). The open-source, self-hosted **household hub** and the **experimental prototype that drives the whole Divia.Network ecosystem** — and the direct Python ancestor of the Rust Enterprise server. Four domains: Activity Log (NL DiviaCard capture inbox), Asana-style tasks, calendar, `.dvai` document editing. **Next big thing:** Phase 00 → a **v1 "scan-and-import" data-unification** release that pulls years of scattered legacy SMS/food/med/purchase logs into one clean record ("first unify, then understand").

## DiviaLife (commercial mobile)

**🟠 divialife-flutter** — Phase 00 pending; no Flutter scaffold yet, explicitly "no sacred cows / volatile" for ~6 months. The closed-source **mobile** app of the Divia.AI ecosystem: four tabs — **Agenda** (tasks/events + GPS itinerary), **Journal** (Logseq-style daily notes), **Messages** (Telegram-like), **Friends & Family** (aggregated social feed). **Next big thing:** Phase 00 (state mgmt, local store, data model) → a first end-to-end vertical slice of one tab. *(Authoritative on the Flutter-first / native-later question — see ERRATA.)*

**⚪ divialife-android / divialife-iOS** — Empty (not even git repos). Planned native Kotlin / Swift editions, to follow once the Flutter build settles the product & data model.

## DiviaCards

**🟢 divia_cards** — *Surprise: a fully-built, working, tested app* (Nov 2025, built by Factory.ai's "droid," Gemini-reviewed; 5 phases, 25 backend tests). A Flask + Svelte 5 app that renders typed text inputs as **"cards," compiled to framework-agnostic Web Components** (with working Vue & React demos). **Caveat:** its "DiviaCard" is a *local UI-widget* concept and is **not wired to** the ecosystem-wide DiviaCard data-interchange concept — same name, different thing (see ERRATA). **Next:** reconcile with the ecosystem vocabulary; add editable Web Components. Currently dormant.

## TastyPal

**🟠 tastypantry** — Phase 00 pending, zero code; the seed prototype the household apps descended from. A kitchen **pantry-inventory** app (foods, NL food logs, receipts, per-store shopping lists, recipes as compound foods). **Next:** Phase 00 (5-domain data model) → a Foods/inventory vertical slice. *(Self-describes as "standalone," contradicting its Divia.Network role — see ERRATA.)*

**🟡 spicemaster3000** — Phase 00 research **in progress** with a *huge* corpus (18 analysis tracks + a parsed Flavor Bible dataset of ~23,690 pairings + 6 vendor catalogs); only skeleton code. John's culinary passion project; positioned **fully standalone** (no Divia ties). **Next big thing:** build the Flask MVP (the recommended ~12-feature v1: flavor profiling, blend builder, spice encyclopedia, exposure-gap discovery).

## Standalone verticals

**🟠 legendarymoney-web** (LegendaryMoney) — Phase 00 pending, docs-only, **dual-licensed AGPLv3 + Commercial**. An AI-assisted **PFM for messy/incomplete data**: confidence-aware ledger, balance assertions, NL capture ("I had El Pollo Loco for dinner" → estimated expense). Real founder pedigree (John + David, ex-Digital Insight → $1.2B Intuit acquisition). **Next big thing:** Phase 00 → a **v1 scan-and-import** that unifies scattered money fragments into one confidence-aware ledger.

**🟠 sattvasichealth** (SattvasicHealth) — Phase 00 pending, docs-only, license **undocumented**. A personal **health-metrics aggregator** (labs, CGM, weight/DEXA, Rx/supplements, calories/macros) with a future **correlation engine** as the payoff. **Next:** Phase 00 → one metric domain end-to-end (e.g. a cross-lab analyte timeline). *(Its docs deny ecosystem membership — see ERRATA.)*

**🟠 kingstratvc-web** (KingmakerStrategic) — Phase 00 pending; a **git fork of `diviahome-web`** with a tiny 5-file client delta. A private **PKMS / "company intranet"** for a PE/VC firm (portfolio + idea-stage startup tracking) — and a **trial-run of a future Divia.AI Enterprise client install**. Product-facing name (per LATER-002): **KingStratVC Knowledgebase** (not yet reflected in-repo). **Next big thing:** Phase 00 to settle the intranet/portfolio/dealflow model, then converge shared infra back down into DiviaHome.

---

### Portfolio shape at a glance

- **Shipping/working software (🟢):** aixocode, aixodev-web, aixodev-projects, divia_ai-professional, divia_cards. (Five real apps; aixocode and divia_ai-professional are the most product-complete.)
- **Active build (🟡):** aixodev-codemap, aixodev-openhands, spicemaster3000.
- **Docs/research, pre-code (🟠):** aixodev-collabs, aixodev-workgroups, divia_ai-swarm, diviacontacts-gmail, diviahome-web, divialife-flutter, tastypantry, legendarymoney-web, sattvasichealth, kingstratvc-web.
- **Empty/placeholder (⚪):** aixodev-professional, divia_ai-enterprise (no git repo), diviacontacts-android/iOS, divialife-android/iOS.
- **The critical-path bet right now:** **DiviaHome v1** gates the entire commercial Divia.AI server line (Enterprise → Global SaaS). It is the current 60-day focus and the highest-leverage unbuilt thing in the portfolio.
