# Brief (Software-Dev) — Patternicity / PatternicityNews  ·  **INTRO BRIEF (partial)**

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase**. Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/Patternicity/patternicity.md)**. **INTRO BRIEF (2026-06-21):** *partial* draft per the [new-venture intro-brief workflow](../../_workflows/workflow_new_venture_intro_brief.md) — **"what we know / infer"** (cited; `TBD`; *Inference:* labels) + inline **❓ Additional Questions for John**. No-invention. **This venture is idea-only — there is no repo yet**, so most engineering facts are intentions or open questions.

## Project / repos

**What we know / infer**
- **No repo exists yet.** The Reader is explicitly "**NOT YET A REPO**" (`SOFTWARE_DEV/divia_ai-professional.md`). No GitHub remote, no Build-Line scaffold (dossier).
- *Inference:* the venture implies **at least three engineering surfaces** — a news **portal/backend** (+ the NER/entity-graph pipeline), the desktop **Reader**, and later **PatternicitySocial** — likely separate repos.

**❓ Additional Questions for John**
1. What's the intended **repo structure** — e.g. `patternicity-web` (portal + NER pipeline), the Reader (on the Divia.AI Professional stack), `patternicity-social` later? Is there a **DailySpikeDriver-level proto** (`proto-patternicity-web`) you'd drive personally first, à la `proto-tastypal-web`?
2. Is the **NER/entity-graph backend** its own service/repo (the heavy, distinctive part), separate from the reader-facing portal?

## Integration surfaces — how the world-knowledge graph is consumed  *(NEW — John, 2026-06-24)*

**What we know / infer**
- The world-knowledge graph is not just the news site's backend — it's exposed through **four consumption surfaces**, each a distinct engineering integration:
  1. **Divia-agent "memory layer."** The graph is queried as a memory/knowledge layer by the Divia agents inside Divia.AI products and DiviaHome devices ("Hey Divia, what's happening with X?") — so an LLM answer can draw on up-to-date world-knowledge. *Implies a read API/contract the Divia.AI Enterprise agents call.*
  2. **The Reader's right-sidebar agent.** In the desktop Reader, a **Divia agent powered by Claude (Anthropic API)** sits in a right sidebar; right-click a person/company in an article → ask, with the agent reasoning across the **entire Patternicity graph**. *This is the agent-over-graph query path at the desktop tier.*
  3. **"Morning Briefing" homepage of Divia.AI Enterprise.** The world-knowledge surface can be embedded as the default homepage corporate teams open each morning — a high-visibility integration into the Enterprise server's UI.
  4. **MCP server.** An **MCP** endpoint exposes the PatternicityNews world-knowledge DB so an external **Claude desktop** can query current news *past* the model's training cutoff. *A new, distinct service surface (likely its own deployable) with its own auth/rate/licensing posture.*

**❓ Additional Questions for John**
- ⭐ Is the **MCP server** its own repo/service (separate from the portal backend and the Divia-agent read API)? Do the four surfaces share **one read contract** over the graph, or each get a bespoke integration?
- The **memory-layer** path: does Divia.AI Enterprise call Patternicity as an external client (cross-venture service boundary), or is some Patternicity-derived world-knowledge **replicated into** the Enterprise deployment? (A scale + licensing + freshness question.)

## Build Lines · Build Envelopes · Triangulation Target (dated)

**What we know / infer**
- None defined yet. *Inference:* a **Seed-tier** Build Envelope (~5-person startup) for the portal; the **Reader rides Divia.AI Professional's "Desktop" envelope** (Rust/Tauri); the NER/graph pipeline may need a heavier envelope given the data scale.

**❓ Additional Questions for John**
3. What are the **Build Lines** (portal · NER/graph pipeline · Reader · Social), and what **Build Envelope** does each target?
4. What's the **dated Triangulation Target** — the far destination (a major news + entity-intelligence + maybe prediction platform?) and roughly *when* (e.g. 2030)?

## Techstack

**What we know / infer**
- **Reader:** Rust · Tauri v2 · SvelteKit 5 — **shared with Divia.AI Professional** (stated intent, not code) (`SOFTWARE_DEV/divia_ai-professional.md`).
- **Portal + NER pipeline:** **TBD.** NER described as "**LLM and otherwise**" (`PLAN…`) — i.e. LLM + classical NER.
- Graph engine, embedding model, hosting/infra: **TBD — not found.**

**❓ Additional Questions for John**
5. **Portal/backend stack** — Python/Flask seed-tier like the rest of the portfolio, or something heavier given ingestion scale?
6. **NER toolchain** — which LLM(s), which classical NER libraries, and what **embedding model** for the vector side?

## Graph-DB & data architecture  ·  ⭐ the cross-venture substrate test

**What we know / infer** (all from `PLAN…`, the only source describing this)
- Built on the **Divia.AI Enterprise graph-DB core as a client** (like KSVGPS) — but at a *very* different scale: **millions of public entities** (every person/place/company in every article) + public read traffic.
- **Primary data source:** the **Wikipedia static dump + periodic updates** → internal copy → parse + model + **prime NER** from it.
- **Ongoing core investment:** parsing + NER modeling **every person/place/company in every article** via the graph's relationships.
- **Topic-hubs:** "likely dozens of graphs/clusters with inter-vertices — TBD."
- **Vector-search segmentation:** segment topics so vector distance is meaningful *within* a topic ("not treating 'all of Canada' as the same distance from 'all of horses'").

**❓ Additional Questions for John**
7. ⭐ **How does Patternicity's graph-DB scope differ from KSVGPS's?** KSVGPS = a bounded internal portfolio; this = millions of public entities + public traffic. Same **Divia.AI Enterprise core instance** consumed as a client, or its **own deployment / fork** at that scale? (This is the heart of the shared-substrate test.)
8. ⭐ **Topic-hubs:** one **partitioned** graph or **many graphs** with cross-edges ("inter-vertices")? What *defines* a topic boundary, and who/what assigns an entity to a hub?
9. ⭐ **Vector-segmentation:** **per-topic** vector spaces or one **global** space with topic-scoped queries? What gets embedded — entities, articles, or both?
10. **Entity-resolution** (the hard part): same person across thousands of articles = one node. What's the entity-ID / dedup scheme — reuse KSVGPS's **source-neutral-ID / UUIDv7-private-by-default** `[DEALBREAKER-HOOK]`s, or something new?
11. **Wikipedia ingestion:** licensing (`R-001`), update cadence beyond "periodic," storage scale, and whether **Wikidata (CC0)** is a cleaner complement/alternative to the CC BY-SA dump.

## DiviaCards integration

**What we know / infer**
- PatternicitySocial posts/renders **`DiviaCard::PatternicityNews::article`** — the *canonical example token* for the entire DiviaCards namespacing standard (`SOFTWARE_DEV/divia_cards.md`).
- But the article-card type is **not yet implemented** in the `divia_cards` repo, and is tied to the **unresolved namespacing/registry `[DEALBREAKER-HOOK]` / ERRATA E-04/E-05** ([`../ERRATA.md`](../ERRATA.md)): "DiviaCard" today means a local UI widget; the cross-app interchange type has no registry.

**❓ Additional Questions for John**
12. What does an **article-card** actually need — a typed schema, embedded/interactive functionality, the `diviacard://{repo}/{card_id}` referenced-card model? Does Batch-4 PatternicityNews work require the **DiviaCards registry/namespacing decision (E-04/E-05)** to be settled first?

## `[DEALBREAKER-HOOK]`s (candidates)

**What we know / infer**
- *Inference (candidates — not yet ratified):* the **entity-ID / source-neutral scheme**; the **topic-hub partition**; **per-topic vs. global vectors**; the **Wikipedia-derived-data license posture** (R-001); the **DiviaCard article-type/registry** (E-05).

**❓ Additional Questions for John**
13. Which of these do you see as the **irreversible v1 forks** — the ones cheap to get right now and catastrophic to retrofit?

## Lineage / convergence

**What we know / infer**
- **Graph-DB client** of Divia.AI Enterprise (the convergence chain: `diviahome-web → proto-divia_ai-enterprise → clients`). The **Reader** is a *shared-stack* relationship with Divia.AI Professional, not necessarily a fork.

**❓ Additional Questions for John**
14. Is the **Reader** a **fork** of Divia.AI Professional, or an **independent app on the same stack template**? (Determines whether feature-merge flows between them.)

## Cross-references

- Paired business brief: [`../ULTIMATE_VISION/PRODUCTS/Patternicity/patternicity.md`](../ULTIMATE_VISION/PRODUCTS/Patternicity/patternicity.md).
- Substrate + siblings: [`divia_ai-enterprise.md`](divia_ai-enterprise.md) (graph-DB core) · [`divia_ai-professional.md`](divia_ai-professional.md) (shared Reader stack) · [`divia_cards.md`](divia_cards.md) (the card standard).
- Research: `R-001` (Wikipedia licensing) + `R-004` (topic-hub/vector-segmentation) in [`../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../_backlog_TODOs/RESEARCH-BACKLOG.md). Model: [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md).
