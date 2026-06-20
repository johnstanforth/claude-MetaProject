# Brief — KingStrat AdVentureGPS (KSVGPS)

> **Self-contained product brief** structured per the [Project Organization Model](../../../PROJECT-ORGANIZATION-MODEL.md). Everything needed to reason about this product in a scoped discussion is contained here (domains/cross-refs pulled in from `DOMAIN_*`, intentionally). Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge when this brief is ingested. **Exemplar — sets the brief template (2026-06-20).** *(Supersedes the stale `kingstratvc-knowledgebase.md`, which describes the parked predecessor `kingstratvc-web`.)*

> **Facet note** (per the [two-knowledgebases split](../../../PROJECT-ORGANIZATION-MODEL.md)): the *business-facet* sections — Identity · Company/corporate-structure/Brands · Product Lines → Products · Domains · Status & history — bootstrap the **KSVGPS** (business) graph-DB; the *software-dev-facet* sections — **Build Lines · Build Envelopes**, and the repo/git-lineage detail — bootstrap the **AIXO.Dev Platform** (software-dev) graph-DB. Whether both facets stay in one self-contained file (as here) or split into two is a structure-decision pending confirmation.

## Identity

| Field | Value |
|---|---|
| **Product (full)** | KingStrat AdVentureGPS |
| **Wordmark** | AdVentureGPS |
| **URL / acronym** | KSVGPS |
| **Repo / dir** | `kingstrat-adventuregps` · GitHub `@KingStratVC/kingstrat-adventuregps` |
| **One-line** | A portfolio-tracking / venture-studio operating system for a PE/VC firm — Studio Operations control center + LP Dashboard. |
| **Framing metaphor** | VTL ("Vector Tracking Loop") / GPS / air-traffic-control — tracking ventures along their trajectories. |

## Company / corporate structure · Brands

- **Company:** **Kingmaker Strategic Venture Partners LLC** (abbr. **KingStratVC**) — a PE/VC firm. **It is a *customer*, not a vendor** (the firm consumes this product; the product is built by the Divia.AI side).
- **Brands:** firm front = *KingmakerStrategic*; product wordmark = *AdVentureGPS*; URL/acronym identity = *KSVGPS* (deliberately distinct — like a ticker vs. a company name; `KSV` retconned to "Kingmaker Strategic Ventures").

## Product Lines → Products

- **Product Line:** the firm's venture-studio operating system (internal B2B tooling).
  - **Product:** **KingStrat AdVentureGPS** — two audiences/surfaces: **Studio Operations** (the "Signal Node" studio control center, incl. the "Signal Inception" ideation module) and the **LP Dashboard** ("Trajectory Node" LP portal). *(Distinct from the firm's public website `kingmakerstrategic.com`.)*

## Build Lines · Build Envelopes · Triangulation Targets · Version history

KSVGPS is a **client of the Divia.AI Enterprise graph-DB server** *and* the **R&D + dogfood site** where that graph-DB architecture is figured out (see Graph-DB relationship). Its Build Lines:

| Build Line | Build Envelope | Role / status |
|---|---|---|
| **Graph-DB spikes** (this repo's Phase-00 spikes) | "Spike" (solo, throwaway-validation, Python) | Prove the irreversible graph-DB seams on KingStrat's *real* data; outputs feed the architecture, not a shipped surface. |
| **AdVentureGPS app** *(the near-term product)* | "Studio" (small internal tool · Python/Flask/SQLite→Postgres · the firm's studio team) | The shippable venture-studio OS the firm dogfoods. **Delivers the Product's public Version history (v1.0 → …).** |
| *(far-future)* runs on the **Rust Divia.AI Enterprise server** | "Enterprise" (Rust commercial server) | Succession relation, no-merge — when the graph-DB core graduates to Rust, KSVGPS becomes a client of it (see convergence chain). |

- **Triangulation Target (app Build Line):** a mature venture-studio OS whose knowledgebase is a faithful, queryable graph of the whole portfolio — so the same engine serves studio ops, the LP dashboard, and AI agents reasoning over the portfolio.
- **Line-relation:** KSVGPS is a **git client downstream of `proto-divia_ai-enterprise`** — `main` = pristine mirror of the prototype server; `kingstrat-main` = the AdVentureGPS client delta. (Clone-lineage; receives upstream graph-DB improvements.)

## Graph-DB relationship (KSVGPS's defining role)

KSVGPS is **where the Divia.AI Enterprise graph-DB architecture is figured out and dogfooded** (`ARCHITECTURE_CONVERGENCE.md`): its Phase-00 spikes prove the graph-DB seams by **importing KingStrat's own real data** — companies / entities / domains / relationships, *most of which literally lives in this MetaProject's `DOMAIN_*` and `ULTIMATE_VISION/` markdown* (these very briefs are the v1 import set). The business requirement (stakeholders/investors see a working KSVGPS) *is* the graph-DB acceptance test. The proven architecture then **merges upstream → `proto-divia_ai-enterprise`** → (far-future, gated) the Rust **`divia_ai-enterprise`**. **Origin of the graph-DB decision:** John concluded the cross-entity relationships (corporate-structure vs. marketing-entity distinctions; unresolved "question-mark" relationships like the Sattvasic-Health-vs-DIVIA-Foundation placement) are too messy to keep accurately in flat Markdown — KSVGPS's graph DB is meant to absorb these reference docs and model exactly those subtleties.

## Domains (self-contained — from `DOMAIN_MAPPINGS.md`)

- **App (main URL):** **`KSVGPS.kingstrat.ventures`** — a non-wildcard subdomain of `kingstrat.ventures`.
- **Firm front (one canonical):** **`kingmakerstrategic.com`**. Every other `king*` variant **301-redirects** to it: `kingmakerstrategy.com`, `kingstratvc.com`, `kingstrat.vc`, `kingstratventures.com`, and `kingstrat.ventures` **(apex + `www` ONLY — the redirect must NOT be wildcard, so it doesn't capture the `KSVGPS` app subdomain).**
- **GitHub:** `git@github.com:KingStratVC/kingstrat-adventuregps.git`.

## Status & history

- **Phase 00** (ideation/research). Stack: Python · Flask · SQLAlchemy · SQLite→Postgres. License: Commercial/Proprietary.
- **Lineage:** rebranded from a `kingstratvc-web` clone (the parked "KingStratVC Knowledgebase," a `diviahome-web` fork) on **2026-06-14**; **renamed** "KingStrat VentureGPS" → "KingStrat AdVentureGPS" on **2026-06-15** (old name collided with an existing fleet-management GPS company).
- **Major in-flight work:** the entity-model / graph-DB deep research (47 Claude analyses + the Codex extension run) and the spike battery (S1 = pin the canonical-event envelope first).

## Open questions / `[DEALBREAKER-HOOK]`s

- The entity-model synthesis's irreversible **`[DEALBREAKER-HOOK]`s** to honor at v1: the canonical-event envelope + codec registry, UUIDv7-private-by-default, source-neutral IDs, suppression-as-first-class-state, the visibility label (see `_specs_and_plans/_research/entity_model_and_graph_db/`).
- **Corporate-structure ambiguities** this graph must model as first-class "question-mark relationships" (e.g. Sattvasic Health's placement under the DIVIA Foundation vs. its own umbrella).

## Cross-references

- Architecture: [`../../../ARCHITECTURE_CONVERGENCE.md`](../../../ARCHITECTURE_CONVERGENCE.md) (the graph-DB convergence chain) · [`../../../PROJECT-ORGANIZATION-MODEL.md`](../../../PROJECT-ORGANIZATION-MODEL.md).
- Concept/UX source: `../../../kingstratvc-web_DESIGN_NOTES.md` (VentureGPS-vs-Helix naming session; VTL concept; Signal/Trajectory nodes; "Signal Inception").
- The research corpus lives in the repo: `kingstrat-adventuregps/_specs_and_plans/_research/`.
