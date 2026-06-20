# PLAN — Bootstrapping the Portfolio Knowledgebase & Reasoning About Two New Ventures

> Working plan (2026-06-20). Pairs with the canonical structural model in **[`_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](_REFERENCE/PROJECT-ORGANIZATION-MODEL.md)** (the *hierarchy*); this doc holds the *method + sequence*. Together: "full big-picture reference doc + detailed plan doc."
>
> **Status:** the model doc is now revised to **v2** (reconciled hierarchy + the **Build Envelope** dimension, named 2026-06-20); this plan is aligned to it.

## The core idea — markdown briefs as the graph-DB bootstrap dataset

Everything written into these briefs is **both** the initial dataset **and** the design-thinking draft for the future KSVGPS graph-DB. Exactly like our `_workflows` evolved over months before we'd formalize them, these briefs are the draft-version of the representations we'll soon model in the graph-DB. Therefore: **isolate each concept as cleanly as possible** — each Product, Build Line, Build Envelope, Stage as a distinct, well-bounded section — because *every statement here must be modeled accurately in the graph-DB prototype later*. The briefs are a deliberate **poor-man's stand-in for the scoped projections** the graph-DB will eventually serve on demand.

## The structural model (per PROJECT-ORGANIZATION-MODEL v2)

`Company/Venture → corporate structure · Brands → Product Lines (families) → Products → [public Version history] → Build Lines (3-part) → Build Envelope · Triangulation Target · Stages → Phases → Sprints`, with Features as graph nodes throughout. The **Build Envelope** (formal: *Architectural Build Envelope*) is the independent "what engineering scale/scope/stack we build FOR" axis — per-venture, reusable copy-on-write, the explicit context handed to Codex so it designs *for that level*, and the home for techstack standardization + continuous improvement (e.g. the future "Flask+FastAPI → async Quart?" question).

## The briefs — structure + principles

- **Self-contained per Product/Venture.** Each brief carries *everything* needed to reason about that project — including its **domains + cross-references/relationships pulled in from `DOMAIN_LIST`/`DOMAIN_MAPPINGS`** — so a tightly-scoped "reason about these 3 projects" discussion never has to parse the portfolio-wide files. (Redundancy with `DOMAIN_*` is intentional and fine.)
- **Clean internal isolation** — each concept a bounded section, so it maps 1:1 to a graph-DB node/edge later.
- **Home + structure:** self-contained per-Product briefs in `_REFERENCE/ULTIMATE_VISION/PRODUCTS/<Umbrella>/` + a README index (confirmed — **not** a separate `BUILD_LINES/` subdir, which would re-fragment scope-ability). Enrich existing briefs; create where missing.
- **The endpoint:** these prototype the scoped projections; eventually a **SKILL** tells the LLM exactly how to query the graph-DB for "the techstack from here, the GTM strategy from there," retiring the makeshift markdown.

## The shared-substrate reasoning (the actual test)

The pattern: **Divia.AI Enterprise server (the graph-DB core)** → **KSVGPS** (R&D/dogfood client + knowledgebase) → **other venture clients** (PatternicityNews, CrowdMadness) building on the *same* graph-DB techstack/capabilities, each with a *different scope*. (See [`_REFERENCE/ARCHITECTURE_CONVERGENCE.md`](_REFERENCE/ARCHITECTURE_CONVERGENCE.md).) Per venture: *"what does it need from the graph-DB techstack + knowledgebase, and how does its scope differ from KSVGPS?"* — done by handing the LLM a small set of **self-contained briefs**, never the whole portfolio.

## Proposed Sequence — briefing batches

> Full portfolio inventory below, batched by reasoning-priority. Flags: **[GRAPH]** graph-DB substrate · **[NEW]** net-new venture (no repo/brief yet) · status: *active* / *scaffold* / *idea-only*. Review & reorder as you like; **Batch 1 is the immediate first batch** (created this round as the exemplar).

**Batch 1 — the graph-DB substrate (foundation for the new-venture reasoning) — DOING NOW**
- **KingStrat AdVentureGPS / KSVGPS** (`kingstrat-adventuregps`, *active*) **[GRAPH]** — the graph-DB R&D + dogfood site. *(Exemplar brief written this round.)*
- **Divia.AI Enterprise** — graph-DB core: `proto-divia_ai-enterprise` (*active*, Python/Flask, stable-API target) + planned Rust `divia_ai-enterprise` (*idea-only*). **[GRAPH]**
- **Divia.AI Professional** (`divia_ai-professional`, *active*) — Rust/Tauri desktop; the stack **PatternicityNews Reader** shares.
- **AIXO.Dev Platform** — the **software-dev knowledgebase** (the peer to KSVGPS's *business* one): `aixodev-web` + the `aixodev-projects` / `aixodev-workgroups` prototypes modeling every project / repo / upstream + **Build Lines · Build Envelopes · Stages/Phases/Sprints** + dev discussions. **[GRAPH]**

> **Two knowledgebases (per model doc v2):** **KSVGPS** = the **business** side (companies / products / GTM / domains / corporate structure); the **AIXO.Dev Platform** = the **software-dev** side (repos, Build Lines, Build Envelopes, Stages/Phases/Sprints, dev discussions). They overlap at `Company → Product`. **Open structure decision:** each brief as one self-contained file with both facets tagged (as in the KSVGPS exemplar), vs. split business-briefs (here in `_REFERENCE`) and software-dev-briefs (in the AIXO.Dev model).

**Batch 2 — the two NEW target ventures (today's focus)** **[NEW]**
- **PatternicityNews** (Patternicity.AI, LLC; *idea-only*) — News + **PatternicityNews Reader** (desktop) + **PatternicitySocial** (DiviaCards) + sub-brands (Patternicity ONE, WTF/WeighTheFacts, Bet, `ptnws.link`).
- **CrowdMadness** (CrowdMadness, Inc.; *idea-only*) — MobThought-reboot prediction-market *game* + **CrowdResearch**.

**Batch 3 — adjacent / referenced ventures (likely to surface in the reasoning)**
- **FracRealHomes** (`fracrealhomes-web` + flutter/android, *scaffold*; **no brief yet**) — the sorting-pass example.
- **LegendaryMoney** (`legendarymoney-web`, *active*) — FracRealHomes leans on it for financial services.
- **DiviaCards** (`divia_cards`, *active*) — the DiviaCard vocabulary PatternicityNews/Social use.
- **Divia.Network** (*idea-only*) — the ecosystem integration layer.

**Batch 4 — the rest of the active AIXO.Dev / Divia.AI portfolio**
- AIXO.Dev: **aixodev-web** **[GRAPH]**, **aixodev-projects** **[GRAPH]**, aixocode, aixodev-codemap, aixodev-collabs, aixodev-workgroups, aixodev-openhands, aixodev-professional.
- Divia.AI: Divia.AI AgentSwarms, DiviaHome **[GRAPH-lineage]**, DiviaContacts (gmail/android/iOS), Divia.Life (flutter/android/iOS), DiviaOS.

**Batch 5 — other portfolio companies (mostly idea-only; lower priority)**
- TastyPal (TastyPantry, spicemaster3000), SattvasicHealth.
- Domain-only ventures: SensoryMQ (+ .Cloud), TXFR.Cloud (+ .App), Invendra, AdEvolve, CTO Mindmeld, JSL Dragonfly, Dotfigurator, VelocityTerminal, GridTransmit, Neurogrammatic, Quintivity, RosettaMQ, Surreality, Transformulator.

*(Corporate-structure ambiguities flagged for the graph-DB to resolve later: Sattvasic Health under DIVIA Foundation vs. its own umbrella; several "question-mark relationships" per `notes-clarifying-UltimateVisionGuide.md` §7.)*

## The two target ventures (seed capture — full briefs in Batch 2)

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

1. **Align** model + plan docs (done: name = Build Envelope; hierarchy reconciled; briefs structure confirmed).
2. **Build the substrate briefs** — Batch 1, self-contained, to the model's detail. *(KSVGPS exemplar done; graph-DB core + Divia.AI Professional next.)*
3. **Reason** about the two new ventures against that substrate (graph-DB needs; how each scope differs from KSVGPS).
4. **Write** the two venture briefs (Batch 2), self-contained.
5. **Breadth-first** each venture's Phase-00 research topics.
6. **Sequence** the topics.
7. **Run** the first topic through the new **multiagent research workflow** (the live test).

## Open items (for your review)

- **Review the Proposed Sequence** — confirm the batching / flag any other entities relevant to today's discussions.
- **Confirm the KSVGPS exemplar brief** sets the right template (then I mass-produce the rest).
- On your go, I'll do the **rest of Batch 1** (graph-DB core + Divia.AI Professional) and **Batch 2/3** during your ~2-hour window.
