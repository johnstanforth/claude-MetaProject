# PLAN — Bootstrapping the Portfolio Knowledgebase & Reasoning About Two New Ventures

> Working plan (2026-06-20). Pairs with the canonical structural model in **[`_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](_REFERENCE/PROJECT-ORGANIZATION-MODEL.md)** (the *hierarchy*); this doc holds the *method + sequence*. Together: "full big-picture reference doc + detailed plan doc."
>
> **Status:** the model doc is now revised to **v2** (reconciled hierarchy + the **Build Envelope** dimension, named 2026-06-20); this plan is aligned to it.

## The core idea — markdown briefs as the graph-DB bootstrap dataset

Everything written into these briefs is **both** the initial dataset **and** the design-thinking draft for the future KSVGPS graph-DB. Exactly like our `_workflows` evolved over months before we'd formalize them, these briefs are the draft-version of the representations we'll soon model in the graph-DB. Therefore: **isolate each concept as cleanly as possible** — each Product, Build Line, Build Envelope, Stage as a distinct, well-bounded section — because *every statement here must be modeled accurately in the graph-DB prototype later*. The briefs are a deliberate **poor-man's stand-in for the scoped projections** the graph-DB will eventually serve on demand.

## The structural model (per PROJECT-ORGANIZATION-MODEL v2)

`Company/Venture → corporate structure · Brands → Product Lines (families) → Products → [Product Version-Releases] → Build Lines (3-part) → Build Envelope · Triangulation Target · Stages → Phases → Sprints`, with Features as graph nodes throughout. (**Product Version-Releases** = public release milestones `v1.0…vN.0` split by a moving "today" marker: immutable git-matched past + a flexible, kanban-movable future "marketing sketch.") The **Build Envelope** (formal: *Architectural Build Envelope*) is the independent "what engineering scale/scope/stack we build FOR" axis — per-venture, reusable copy-on-write, the explicit context handed to Codex so it designs *for that level*, and the home for techstack standardization + continuous improvement (e.g. the future "Flask+FastAPI → async Quart?" question).

## The briefs — structure + principles

- **Self-contained per Product/Venture.** Each brief carries *everything* needed to reason about that project — including its **domains + cross-references/relationships pulled in from `DOMAIN_LIST`/`DOMAIN_MAPPINGS`** — so a tightly-scoped "reason about these 3 projects" discussion never has to parse the portfolio-wide files. (Redundancy with `DOMAIN_*` is intentional and fine.)
- **Clean internal isolation** — each concept a bounded section, so it maps 1:1 to a graph-DB node/edge later.
- **Home + structure (DECIDED 2026-06-20):** **two briefs per project** — a **business-side** brief in `_REFERENCE/ULTIMATE_VISION/PRODUCTS/<Umbrella>/` and an **engineering-side** brief in `_REFERENCE/SOFTWARE_DEV/` — with **both sets kept here in MetaProject `_REFERENCE/`**, *not* in the `kingstrat-adventuregps` / `aixodev-*` project repos, for the next ~1–2 weeks while we bootstrap the graph-DB spikes (so "does capability X serve *both* the business-side and engineering-side data models?" can be reasoned about with both file-sets in one tree). **Separate files, not one tagged file** — so an engineering-scope projection ("pull the techstack from Divia.AI Enterprise") never drags in the business side's dozens-of-LLCs corporate-structure noise. Enrich existing briefs; create where missing.
- **The endpoint:** these prototype the scoped projections; eventually a **SKILL** tells the LLM exactly how to query the graph-DB for "the techstack from here, the GTM strategy from there," retiring the makeshift markdown.

## The shared-substrate reasoning (the actual test)

The pattern: **Divia.AI Enterprise server (the graph-DB core)** → **KSVGPS** (R&D/dogfood client + knowledgebase) → **other venture clients** (PatternicityNews, CrowdMadness) building on the *same* graph-DB techstack/capabilities, each with a *different scope*. (See [`_REFERENCE/ARCHITECTURE_CONVERGENCE.md`](_REFERENCE/ARCHITECTURE_CONVERGENCE.md).) Per venture: *"what does it need from the graph-DB techstack + knowledgebase, and how does its scope differ from KSVGPS?"* — done by handing the LLM a small set of **self-contained briefs**, never the whole portfolio.

## Proposed Sequence — briefing batches

> Full portfolio inventory below, **ordered as a dependency graph** (2026-06-20) so each later batch can lean on the reference pages written by earlier ones — both when reasoning about and when writing the newer items. Flags: **[GRAPH]** graph-DB substrate · **[NEW]** net-new venture (no repo/brief yet) · status: *active* / *scaffold* / *idea-only*.

**Batch 1 — knowledgebase scope (everything-business + everything-engineering) — DOING NOW**
- **KingStrat AdVentureGPS / KSVGPS** (`kingstrat-adventuregps`, *active*) **[GRAPH]** — the graph-DB R&D + dogfood site; the **business**-knowledgebase exemplar. *(Two-file exemplar — business + engineering — written this round.)*
- **AIXO.Dev Platform** — the **software-dev** knowledgebase (the peer to KSVGPS's *business* one): `aixodev-web` + the `aixodev-projects` / `aixodev-workgroups` prototypes modeling every project / repo / upstream + **Build Lines · Build Envelopes · Stages/Phases/Sprints** + dev discussions. **[GRAPH]** *(absorbs the formerly-separate `aixodev-web` / `aixodev-projects` bullets.)*

> **Two knowledgebases (per model doc v2):** **KSVGPS** = the **business** side (companies / products / GTM / domains / corporate structure); the **AIXO.Dev Platform** = the **software-dev** side (repos, Build Lines, Build Envelopes, Stages/Phases/Sprints, dev discussions). They overlap at `Company → Product`. **Structure decision (DECIDED 2026-06-20):** split into **two sets of briefs** — business-side (`_REFERENCE/ULTIMATE_VISION/PRODUCTS/<Umbrella>/`) and engineering-side (`_REFERENCE/SOFTWARE_DEV/`) — but **both sets stay here in MetaProject `_REFERENCE/`**, *not* in the `kingstrat-adventuregps` / `aixodev-*` repos, for the next ~1–2 weeks while we bootstrap the graph-DB spikes. Separate files (not one tagged file) so an engineering projection ("pull the techstack from Divia.AI Enterprise") never drags in the business side's dozens-of-LLCs corporate-structure noise.

**Batch 2 — technology foundations (graph-DB core, desktop stacks, card vocabulary)**
- **Divia.AI Enterprise** — graph-DB core: `proto-divia_ai-enterprise` (*active*, Python/Flask, stable-API target) + planned Rust `divia_ai-enterprise` (*idea-only*). **[GRAPH]**
- **Divia.AI Professional** (`divia_ai-professional`, *active*) — Rust/Tauri desktop; the stack **PatternicityNews Reader** shares.
- **DiviaCards** (`divia_cards`, *active*) — the DiviaCard vocabulary PatternicityNews / PatternicitySocial use.
- **Divia.Network** (*idea-only*) — the ecosystem integration layer.

**Batch 3 — other B2C small-startup web apps in the connected Divia.Network ecosystem**
- **FracRealHomes** (`fracrealhomes-web` + flutter/android, *scaffold*; **no brief yet**) — the sorting-pass example.
- **LegendaryMoney** (`legendarymoney-web`, *active*) — FracRealHomes leans on it for financial services.
- **TastyPal** (TastyPal app/mobile + **TastyPantry** app/mobile). *Note:* the current **`spicemaster3000`** should become **`proto-tastypal-web`** — i.e. the **DailySpikeDriver-level** Build Line for the TastyPal web app.
- **SattvasicHealth**

**Batch 4 — the two NEW target ventures (today's focus)** **[NEW]**
- **PatternicityNews** (Patternicity.AI, LLC; *idea-only*) — News + **PatternicityNews Reader** (desktop) + **PatternicitySocial** (DiviaCards) + sub-brands (Patternicity ONE, WTF/WeighTheFacts, Bet, `ptnws.link`).
- **CrowdMadness** (CrowdMadness, Inc.; *idea-only*) — MobThought-reboot prediction-market *game* + **CrowdResearch**.

**Batch 5 — the rest of the active AIXO.Dev / Divia.AI portfolio** (lower priority)
- **AIXO.Dev:** aixocode, aixodev-codemap, aixodev-collabs, aixodev-workgroups, aixodev-openhands, aixodev-professional.
- **Divia.AI:** Divia.AI AgentSwarms, DiviaHome **[GRAPH-lineage]**, DiviaContacts (gmail/android/iOS), Divia.Life (flutter/android/iOS), DiviaOS.

**Batch 6 — other portfolio companies (mostly idea-only; lowest priority)**
- *(For now, the only goal for this batch is to **parse all existing files** — U_V Guide, `DOMAIN_*` docs, etc. — into same-format Reference Brief files; **not** planning to discuss/expand these this week, until we start building specific projects.)*
- Domain-only ventures: SensoryMQ (+ .Cloud), TXFR.Cloud (+ .App), Invendra, AdEvolve, CTO Mindmeld, JSL Dragonfly, Dotfigurator, VelocityTerminal, GridTransmit, Neurogrammatic, Quintivity, RosettaMQ, Surreality, Transformulator.

*(Corporate-structure ambiguities flagged for the graph-DB to resolve later: Sattvasic Health under DIVIA Foundation vs. its own umbrella; several "question-mark relationships" per `notes-clarifying-UltimateVisionGuide.md` §7.)*

## The two target ventures (seed capture — full briefs in Batch 4)

### PatternicityNews — `Patternicity.AI, LLC` (~5-person startup)
- **Products:** **PatternicityNews** (news website/portal) + **PatternicityNews Reader** (desktop; *same stack as Divia.AI Professional, later AIXO.Dev Professional*); later **PatternicitySocial** (X-like; posts **`DiviaCard`** structured types — `DiviaCard::PatternicityNews::article` — with embedded/interactive functionality). Sub-brands: Patternicity ONE (premium-news bundle), WTF/WeighTheFacts (chain-of-thought argument builder), Patternicity Bet.
- **Domains:** `Patternicity*` (incl. `Patternicity.AI`, `patternicity.news`, `patternicity.pro`) + `ptnws.link` / `ptn-link*` (URL-shortener: unique links tracking article-sharing).
- **Core tech:** built on the graph-DB knowledgebase substrate; the ongoing investment is **parsing + NER** (LLM *and* otherwise) modeling **every person/place/company in every article** via the graph's complex relationships.
- **Primary data source:** the **Wikipedia static dump + periodic updates** → internal copy → parse + model + **prime NER** from it.
- **Data-architecture to design carefully:** **topic-hubs** (likely dozens of graphs/clusters with inter-vertices — TBD) and, especially, **vector-search segmentation** (segment topics so vector distance is meaningful *within* a topic — better sub-sub-subtopic accuracy — not treating "all of Canada" as the same distance from "all of horses").

### CrowdMadness — `CrowdMadness, Inc.`
- A **reboot of MobThought** (~2004–2008 prediction-market game) — like Polymarket/Kalshi but **intended as a game** (massively-scalable). Gamified mechanics **TBD/placeholder** today. + **CrowdResearch** (market-research-as-a-service portal).
- **Why it's here:** the second case for the cross-venture reasoning test — *"like Project A, but techstack from Project B, plus KSVGPS ideas"* — proving the LLM can reason across ventures **without** reading the whole U_V Guide first.

## The sequence (steps)

1. **Align** model + plan docs (done: name = Build Envelope; hierarchy reconciled; two-file briefs structure + dependency-graph batch order confirmed; Version-Releases named).
2. **Build the substrate briefs** — Batches 1–3 (knowledgebase scope → tech foundations → ecosystem apps), two files each, to the model's detail. *(KSVGPS two-file exemplar done; AIXO.Dev Platform + Batch 2 next.)*
3. **Reason** about the two new ventures against that substrate (graph-DB needs; how each scope differs from KSVGPS).
4. **Write** the two venture briefs (Batch 4), two files each, self-contained.
5. **Breadth-first** each venture's Phase-00 research topics.
6. **Sequence** the topics.
7. **Run** the first topic through the new **multiagent research workflow** (the live test).

## Open items (for your review)

- **Confirm the two-file KSVGPS exemplar** (business brief + engineering brief) sets the right template — review the **business side first** per John's instruction, before I mass-produce the rest.
- On your go, I'll finish **Batch 1** (the AIXO.Dev Platform software-dev knowledgebase) and proceed through **Batches 2–3** (then the new ventures in Batch 4) during your window.
