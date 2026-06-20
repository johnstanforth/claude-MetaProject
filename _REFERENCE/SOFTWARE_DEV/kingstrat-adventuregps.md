# Brief (Software-Dev) — `kingstrat-adventuregps`

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase** (repos · upstreams · Build Lines · Build Envelopes · Stages/Phases/Sprints · dev discussions). Paired **[business brief](ULTIMATE_VISION/PRODUCTS/KingmakerStrategic/kingstrat-adventuregps.md)** (the `Company → Product` overlap anchors both). Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Exemplar — sets the engineering-brief template (2026-06-20).** *(Software-dev briefs live in `_REFERENCE/SOFTWARE_DEV/` — confirmed; kept in MetaProject for now, not in the project repo, per the bootstrap decision.)*

## Project / repo

| Field | Value |
|---|---|
| **Repo / dir** | `kingstrat-adventuregps` |
| **GitHub** | `@KingStratVC/kingstrat-adventuregps` · `git@github.com:KingStratVC/kingstrat-adventuregps.git` |
| **Techstack** | Python · Flask · SQLAlchemy · SQLite → Postgres |
| **License (engine)** | AGPLv3 + Commercial (CLA) dual-license, inherited from the DiviaHome lineage; KSVGPS operates under DiviaAI's **commercial grant**, so no AGPL §13 network-copyleft attaches to the private deployment. *(KSVGPS-as-product is itself a proprietary internal web service — [business brief](../ULTIMATE_VISION/PRODUCTS/KingmakerStrategic/kingstrat-adventuregps.md).)* |
| **Maps to business Product** | KingStrat AdVentureGPS (KSVGPS) |

## Build Lines · Build Envelopes · Triangulation Target

| Build Line | Build Envelope | Role / status |
|---|---|---|
| **Graph-DB spikes** (Phase-00 spikes in this repo) | "Spike" (solo · throwaway-validation · Python) | Prove the irreversible graph-DB seams on KingStrat's *real* data; feed the architecture, not a shipped surface. |
| **AdVentureGPS app** *(near-term product)* | "Studio" (small internal tool · Python/Flask/SQLite→Postgres · the firm's studio team) | The shippable venture-studio OS the firm dogfoods; delivers the Product's business-side Version-Releases. |
| *(far-future)* runs on the **Rust Divia.AI Enterprise server** | "Enterprise" (Rust commercial server) | Succession, no-merge — when the graph-DB core graduates to Rust, KSVGPS becomes a client of it. |

- **Triangulation Target (app Build Line):** a mature venture-studio OS whose knowledgebase is a faithful, queryable graph of the whole portfolio — one engine serving studio ops, the LP dashboard, and AI agents reasoning over the portfolio.

## Stages → Phases → Sprints

Currently **Phase 00** (ideation/research). Major in-flight work: the entity-model / graph-DB deep research (47 Claude analyses + the Codex extension run) and the spike battery (S1 = pin the canonical-event envelope first). Research corpus lives in-repo at `_specs_and_plans/_research/`.

## Graph-DB R&D role + the convergence chain & discipline

KSVGPS is **where the Divia.AI Enterprise graph-DB architecture is figured out and dogfooded** (`ARCHITECTURE_CONVERGENCE.md`): its Phase-00 spikes prove the graph-DB seams by **importing KingStrat's own real data** — companies / entities / domains / relationships, *most of which lives in this MetaProject's `DOMAIN_*` and `ULTIMATE_VISION/` markdown* (these briefs are the v1 import set). The architecture then **merges upstream → `proto-divia_ai-enterprise`** → (far-future, gated) the Rust **`divia_ai-enterprise`**.

**Convergence is the discipline** *(carried from the predecessor):* build what the firm needs here, **graduate general infrastructure *upstream* into the prototype server**, and let the **shrinking `main..kingstrat-main` branch diff measure it** — what remains on the delta is, by definition, client-implementation scope vs. product scope. Track that diff as a literal **"how much of this client's needs became a product feature" KPI** feeding the Enterprise roadmap.

## Git topology / lineage

- **Lineage:** `diviahome-web` → `proto-divia_ai-enterprise` (the Enterprise-server prototype; itself a diviahome-web fork) → **`kingstrat-adventuregps`** (downstream client). A *separate, now-parked* predecessor — **`kingstratvc-web`** ("KingStratVC Knowledgebase," a direct diviahome-web fork) — was the original first-trial-run, superseded by this repo on the 2026-06-14 reorg + 2026-06-15 rename.
- **Branches:** `main` = pristine mirror of the upstream prototype; `kingstrat-main` = the AdVentureGPS client delta. Stable updates pulled from `upstream`.

## `[DEALBREAKER-HOOK]`s

The entity-model synthesis's irreversible hooks to honor at v1: the **canonical-event envelope + codec registry**, **UUIDv7-private-by-default**, **source-neutral IDs**, **suppression-as-first-class-state**, the **visibility label**. (Detail: `_specs_and_plans/_research/entity_model_and_graph_db/`.) Plus: model **"question-mark" corporate-structure relationships** as first-class (e.g. Sattvasic Health's placement under the DIVIA Foundation vs. its own umbrella).

## Cross-references

- Paired business brief: [`ULTIMATE_VISION/PRODUCTS/KingmakerStrategic/kingstrat-adventuregps.md`](ULTIMATE_VISION/PRODUCTS/KingmakerStrategic/kingstrat-adventuregps.md).
- Architecture: [`ARCHITECTURE_CONVERGENCE.md`](ARCHITECTURE_CONVERGENCE.md) · [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md).
