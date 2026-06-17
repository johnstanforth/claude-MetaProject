# ERRATA — Cross-Project Discrepancy Log

> **Purpose (a top priority of this effort):** catalogue every contradiction — major, minor, or
> subtle/framing — that has crept in across the 24 projects (and across documents *within* a single
> project) as they were written and edited at different times over the past year. We **surface**
> these rather than silently resolving them: several are John's to decide.

- **Compiled:** 2026-06-12, from the read-only harvest sweep. Each entry cites the conflicting sources.
- **Severity:** 🔴 needs a John decision (load-bearing) · 🟠 should reconcile (naming/framing) · 🟡 minor/within-project drift.
- **How to use:** when a single repo's self-description disagrees with this reference, check here first. Resolved items get struck through with the resolution noted.

---

## 🔴 E-01 — The corporate parent has three competing identities

The top of the corporate tree is named **three different ways**, and the newest version explicitly *retires* the oldest:

| Source | Top entity | Subsidiary / product co. | Regional consultancies |
|---|---|---|---|
| John's global `CLAUDE.md` + in-repo `aixodev-aixocode/CLAUDE.md` | **ExoDev.AI, Inc.** | "AIXO.Dev Platform LLC" (author field) | "ExoDev.Pro - Dallas", "ExoDev.Pro - Los Angeles" |
| `aixodev-aixocode/_REFERENCE/PRODUCT_AND_NAMING.md` | **ExoDev.AI Corporation** | **AIXO.Dev Platforms LLC** (plural) "An ExoDev.AI Company" | "ExoDevPro Dallas/LA, **Inc.**" (dotless) |
| `aixodev-web` Phase-D research canon (Apr 2026, marked DRAFT/internal) | **ExoDev.Pro, Inc.** (Dallas HQ) — *explicitly retires "ExoDev.AI"* | **AIXO.Dev Platforms LLC** (plural) | "ExoDev.Pro Dallas/LA **LLC**" (dotted) |

Conflicts: **ExoDev.AI, Inc.** vs **ExoDev.AI Corporation** vs **ExoDev.Pro, Inc.**; "Platform" vs "Platforms" LLC; "ExoDevPro" vs "ExoDev.Pro"; consultancies as **Inc.** vs **LLC**. The Phase-D research is newest but is flagged aspirational/draft; John's `CLAUDE.md` is the live operating instruction but uses the oldest name. **Decision needed:** which corporate naming is canonical going forward? The VENTURES docs lead with the Phase-D model but flag it as unconfirmed pending this decision.

## 🔴 E-02 — The AIXO.Dev desktop edition: two names, two stacks, two framings

- `aixodev-professional`'s **own README** says it *is* **"AIXO.Dev Professional" (`aixodev-professional`)**, a **Rust/Tauri v2 + SvelteKit** desktop edition, an explicit **sub-project of `aixodev-web`**, sharing a Rust/Tauri foundation with Divia.AI Professional.
- `aixodev-web`'s **own docs** call the desktop edition **"AIXO.Dev Desktop" (`aixodev-desktop`)**, **Electron-first** (Tauri vs Electron an *open* ADR), and never use "professional."
- The MetaProject `_projects/README.md` sided with the `aixodev-professional` / Rust-Tauri version.

Direct cross-repo contradiction on **name, stack, and framing.** Related: the **"eventual Rust-server migration of aixodev-web"** is asserted by `aixodev-professional`'s README and the MetaProject index, but is **not corroborated in `aixodev-web`'s own docs** (which mention only "Rust-leaning shared libraries" via FFI, not a server rewrite). **Decision needed:** is the desktop edition `aixodev-professional` (Rust/Tauri) or `aixodev-desktop` (Electron)?

## 🔴 E-03 — Divia.Life: native Swift/Kotlin vs Flutter-first

- `divia_ai-professional/BRANDING_and_PRODUCTS.md`: Divia.Life = **native Swift/Kotlin**.
- `divia_ai-enterprise` README **and** `divialife-flutter` (the actual product repo): **Flutter first → native Swift/Kotlin editions later**.

**Resolution (high confidence):** `divialife-flutter` is authoritative — **Flutter is the first build; native Kotlin/Swift are later (SOMEDAY) editions** once the data model stabilizes (the native dirs are confirmed empty). The "native Swift/Kotlin" claim is almost certainly a misquote of the table cell *"Flutter (then native Swift/Kotlin)."* **Action:** correct `BRANDING_and_PRODUCTS.md` when repos are next edited.

## 🔴 E-04 — `divia_cards` is a finished app, not an "early prototype"

The `_projects/README.md` index calls `divia_cards` an "early prototype — PLAN + PLAN-v2." **It is actually a fully-built, working, tested application** (built Nov 2025 by Factory.ai's "droid" CLI, Gemini-3-Pro-reviewed): working Flask backend, JWT auth, SocketIO, SvelteKit frontend, **Svelte→Web Components** compilation, 25 passing backend tests, and **working Vue 3 + React 18 demo apps.** Status correction needed. Compounding issue → **E-05**.

## 🔴 E-05 — "DiviaCard" means two unrelated things

The word **DiviaCard** is overloaded with no link between the two meanings:
- **In `divia_cards` (Nov 2025):** a *local UI widget* — a Flask `Card` row of type `outline | nlp_input | event`, rendered as a framework-agnostic Web Component.
- **In the ecosystem (divia_ai-professional BRANDING + LegendaryMoney v2 vision, 2026):** a *cross-app data-interchange / registry type* — e.g. `DiviaCard::LegendaryMoney::transaction(...)` published to a "global DiviaCards registry."

`divia_cards` predates the ecosystem framing, contains no registry/namespacing, and isn't referenced by any sibling repo's `_REFERENCE/_EXTERNAL/`. **Best current read:** `divia_cards` is the original *rendering layer* and name-source; the ecosystem later repurposed the term as a data concept; the two have **never been reconciled or wired together.** **Decision needed:** is `divia_cards` the rendering layer for the ecosystem DiviaCard, or a separately-named thing?

## 🔴 E-06 — Three "standalone" projects deny an ecosystem they belong to

The Divia.Network membership is asserted **one-directionally**:
- **`tastypantry`** `CLAUDE.md`: *"standalone … not part of any larger platform … no shared dependencies."* Yet it carries `_REFERENCE/_EXTERNAL/` symlinks to `sattvasichealth`, `legendarymoney-web`, and `diviahome-web`, and its NL food-log model is the canonical Divia.Network "I ate two quesadillas" capture. The baseline's lineage (tastypantry = seed/ancestor) and the food→SattvasicHealth macro feed are **not stated in-repo.**
- **`sattvasichealth`** README/`CLAUDE.md`: *"a standalone project … not part of any larger platform,"* integrating **only** with TastyPantry. **LegendaryMoney's** docs name Sattvasic Health as an ecosystem sibling; **Sattvasic Health does not reciprocate.**
- **`spicemaster3000`:** fully standalone — **zero** Divia/TastyPal references anywhere; its only tie is the AIXO.Dev workflow methodology and John personally. (This one is *correctly* standalone; flagged so the VENTURES/PRODUCTS docs don't over-claim it as a Divia.Network app.)

**Decision needed:** are TastyPantry and Sattvasic Health *in* the Divia.Network ecosystem (update their docs) or genuinely standalone (update the index/this reference)? The evidence says they're meant to be in it; their docs lag.

## 🟠 E-07 — Brand-spelling drift: dots, underscores, and casing

A pervasive, low-stakes-but-everywhere inconsistency:
- **Product brand vs repo name:** "**Divia.AI**" / "**Divia.Network**" / "**Divia.Life**" / "**Divia.Foundation**" (dot, capital) in prose, vs repo/dir names `divia_ai-*`, umbrella "DiviaLife", `divialife-*` (underscore/no-dot).
- **`.dvai` format has three expansions in active use:** "DVAI Document Format" / "Divia Document Format (DDF)" / "DVAI format" — sometimes within a single repo.
- **KingStratVC:** firm "Kingmaker Strategic"; product styled "**KingStrat.vc**" in-repo vs "**KingStratVC**" (GitHub org / env prefix) vs the LATER-002 product name "**KingStratVC Knowledgebase**."
- **iOS dir casing:** `divialife-iOS` / `diviacontacts-iOS` (capital-OS) vs docs' `divialife-ios` (lowercase).

**Action:** pick canonical spellings in a naming appendix; not blocking, but it's the kind of skew this reference exists to end.

## 🟠 E-08 — The Enterprise ↔ Swarm relationship is asserted from one side only

- `divia_ai-agentswarms` frames **Divia.AI Enterprise** as "a PKMS + **Asana-style** task/project server" that **co-deploys with Swarm** so Swarm can power Enterprise's AI features.
- `divia_ai-enterprise`'s **own README** frames itself as a **collaboration/sync server** and **never mentions Swarm or an "AI backbone" at all.**
- `divia_ai-professional`'s BRANDING frames Enterprise as the full collaboration server whose desktop client is Pro (no Asana framing, no Swarm).

Three partly-overlapping pictures of the same server; the Swarm co-deployment exists only in Swarm's docs. **Action:** write one canonical Enterprise definition (the VENTURES/PRODUCTS docs attempt this) and reconcile.

## 🟠 E-09 — The bootstrap-lineage "root" is wrong (and self-reports disagree)

- The `_projects/README.md` index says **`aixodev-collabs` is the root** of the shared `_workflows/` system. The git history says `aixodev-collabs` is a **middle link**: the chain is `aixodev-codemap → aixodev-projects → aixodev-collabs → aixodev-workgroups`, and the `_workflows/` corpus itself predates all four (it traces back toward `aixodev-web` / the original workflow set).
- **Self-reported chains disagree across repos:** LegendaryMoney's docs say `DiviaHome → Sattvasic → TastyPantry → aixodev-collabs`; Sattvasic Health says it came **directly from TastyPantry**; DiviaHome says it came from Sattvasic Health. The "who-cloned-from-whom" story is inconsistent.

**Action:** record the actual lineage once (a STATUS/VENTURES appendix) and stop trusting per-repo self-reports.

## 🟠 E-10 — Model-discipline deviations vs John's "always Opus, never Sonnet" rule

- **`aixodev-openhands/CLAUDE.md`** pins Opus 4.6, warns that `model:"opus"` resolves to Opus 4.7, and **explicitly permits Sonnet subagents for "simple mechanical tasks."** This **contradicts John's standing global rule** (always Opus; never Sonnet) — flagged 2026-06-12 when John re-affirmed the rule. **Action:** bring this repo's model policy into line.
- **`diviacontacts-gmail`'s** entire ~69k-word research corpus was produced by **Claude Fable 5** (per John's explicit 2026-06-11 directive, doubling as a Fable-class capability test) — **not Opus.** Not a violation (John directed it), but recorded so the provenance is clear.

## 🟠 E-11 — Capability documented ahead of reality

Several repos describe features as if present that depend on unbuilt work:
- **aixocode `AgentEngine` mode** is a core concept in the entity/PROLOGUE docs but is **not in the implemented feature list** — it depends entirely on the unbuilt server integration (Sprint 05).
- **`divia_ai-professional` ADR-002 (WYSIWYG/Typora)** is cited as the live decision in `CLAUDE.md`/`AGENTS.md`, while a *withdrawn* copy of the same ADR sits in `_REFERENCE/ARCHITECTURE/` and an active TipTap→ProseMirror migration is already questioning the "settled" editor.
- **Several Phase-00-pending repos** (legendarymoney-web especially) assert "extensive deep research already gathered," but their `_research/` directories contain only `.gitkeep` — the research is claimed, not present in-repo.

## 🟡 E-12 — LATER-002 forward-decisions not yet propagated to the repos (expected)

Canonical decisions captured in the MetaProject's `_backlog_TODOs/LATER-002` have **no footprint in the product repos yet** — expected, since LATER-002 *is* the capture point, but listed so they get pushed down later:
- **`.dvai` "LiveDocuments"** + **Divia.AI Enterprise "Research Projects"** — absent from divia_ai-professional/-enterprise/-swarm.
- **Typed Swarm workflow steps** (deterministic-vs-probabilistic + Haiku→Fable tiers) — absent from `divia_ai-agentswarms`.
- **DiviaHome nightly consumption-driven replenishment** + **kitchen-counter voice device** — absent from `diviahome-web` (it lists only a future "DiviaHome devices" repo; no nightly review, grocery, or replenishment logic).
- **"KingStratVC Knowledgebase"** product name — absent from `kingstratvc-web` (in-repo it's "KingStrat.vc").

## 🟡 E-13 — Heritage & symlink integrity

- **`diviacontacts-gmail`'s** README/`CLAUDE.md` claim it was "carried over with full git history from `divia-gmail`." The git log starts at *"Initial commit: project placeholder"* and is self-contained; **no `divia-gmail` directory exists anywhere.** Looks renamed-in-place / freshly initialized, not history-grafted. (The `_projects/README.md` repeats the "full history" claim.)
- **Broken reference symlinks:** `diviacontacts-gmail/_REFERENCE/_EXTERNAL/diviahome-web` → `…/DiviaAI/diviahome-web` (does not exist; the real one is `…/DiviaHome/diviahome-web`). `aixodev-web`'s external symlinks point to `/Users/jstanforth/…` (macOS paths, dangling on this Linux host).

## 🟡 E-14 — Within-project numeric/label drift (non-blocking)

Captured for completeness; none load-bearing:
- **aixocode test counts:** ROADMAP/in-repo CLAUDE.md say 1732/1682/50; the global CLAUDE.md says 1714/1693/21; the Users Guide cites "1241+"; AGENTS.md is staler still.
- **aixocode Users Guide** says Codex/Gemini parsers are "Phase 7" while the ROADMAP places them in Phase 8 (Phase 7 was Workflow Orchestration, already closed).
- **aixodev-web table count:** "25 tables" (CLAUDE.md) vs "27" (status report) vs "~47/~75" (entity vision).
- **divia_ai-professional test counts:** 37 vs 39 Rust across docs; repo-structure blocks still say `divia_ai-professional-codex/`.
- **spicemaster3000 data counts:** 23,690 pairings / 595 subjects (authoritative, verified on disk) vs a report-card table's 23,378 / 584.
- **divia_ai-professional copyright** runs "© 1996–2026" while the brand history says "Divia.AI (2020–present)."

---

### Cross-cutting pattern

Almost every 🔴/🟠 item is the same root cause: **the ecosystem-level story was written into many repos at different times, and the repos drifted** — newer strategic decisions (the FDSE pivot, the corporate rename, the DiviaContacts repositioning, the LATER-002 agent decisions) landed in *some* docs and not others. That is exactly the skew this `_REFERENCE/` is built to absorb: once each repo points back here and sheds its non-technical vision text, there's one place to keep correct.
