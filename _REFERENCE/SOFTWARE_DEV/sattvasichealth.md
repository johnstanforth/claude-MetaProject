# Brief (Software-Dev) — `sattvasichealth`

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase** (repo · upstreams · Build Lines · Build Envelopes · Stages→Phases→Sprints · lineage · `[DEALBREAKER-HOOK]`s · dev discussions). Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/SattvasicHealth/sattvasichealth.md)** (the `Company → Product` overlap anchors both). Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Status: STUB / scaffold-only** — Phase 00 pending, **zero application code, no Build Lines defined yet**; the sections below report only what the source files actually state and do **not** invent Build Lines / Envelopes / lineage. *Good-enough bootstrap.*

## Project / repo

| Field | Value |
|---|---|
| **Repo / dir** | `sattvasichealth` (local working copy at `~/Code/SattvasicHealth/sattvasichealth`) |
| **GitHub** | **None yet** — `DOMAIN_MAPPINGS.md`: *"local repo `sattvasichealth`; no GitHub remote yet."* |
| **Techstack** | Python 3.12+ · `uv` (`pyproject.toml` source of truth; `uv.lock` committed) · Flask (app-factory `create_app()` + Blueprints + Jinja2) · SQLAlchemy 2.0 (Flask-SQLAlchemy) · **SQLite→PostgreSQL** · Flask-Migrate/Alembic · pydantic-settings (env prefix `SATTVASIC_`) · Bootstrap (CDN, tentative) · pytest · Ruff. Type checker: **none yet** (add mypy only if explicitly decided). Platforms: Linux, macOS. |
| **License (repo)** | **Undocumented** — no LICENSE file, no statement (a notable gap vs. its dual-licensed siblings). Likely AGPLv3 + Commercial to match siblings — **not confirmed** (open item; see business brief). |
| **Maps to business Product** | Sattvasic Health *(business side: [brief](../ULTIMATE_VISION/PRODUCTS/SattvasicHealth/sattvasichealth.md))*. |

## Build Lines · Build Envelopes · Triangulation Target

**None defined yet.** The repo is **Phase 00 pending, docs-only, with zero application code**, so no Build Lines, Build Envelopes, or Triangulation Target have been declared in any source file. (The app scaffold — `app/`, `migrations/`, `pyproject.toml` — is created during the first build phase.) The planned single near-term surface is the **Python/Flask web application** described above, on a **SQLite→Postgres** path. Build-Line / Build-Envelope / Triangulation-Target structure is **TBD (Phase 00 output)** — deliberately not invented here.

## Stages → Phases → Sprints

Currently **Phase 00 (Ideation & Research) — PENDING** (the *next* step; the phase directory is not yet created); **0 sprints, no application code**. What exists is the **bootstrapped scaffold only**: the `_workflows/` development-workflow system (sprint pipeline + ensemble-collab + techstacks + templates), a `_specs_and_plans/` scaffold (README, ROADMAP, `_backlog/` horizons, `_research/`), `README.md`, and `CLAUDE.md`. Phase-00 goals (from the docs): settle the **core data model** and feature priorities — including which import adapters and integrations land in the first build phase — and a Phase-01 first slice of **one metric domain end-to-end** (e.g. a cross-lab analyte/lab-result timeline). Git conventions: branches `claudecode/@claude/phase{NN}-sprint{NN}`; commits `P{NN}-S{NN}-T{NN}`; local-only by default.

## Git topology / lineage (self-reported — disputed)

- **Self-reported bootstrap lineage:** Sattvasic Health was **bootstrapped from TastyPantry** (itself bootstrapped from `aixodev-collabs`) — the workflow-system/scaffold inheritance, not application code.
- ⚠️ **ERRATA E-09 (lineage self-reports disagree).** Across repos the "who-cloned-from-whom" story is inconsistent: LegendaryMoney's docs say `DiviaHome → Sattvasic → TastyPantry → aixodev-collabs`; **Sattvasic Health says it came directly from TastyPantry**; DiviaHome says it came *from* Sattvasic Health. Per-repo self-reports are not authoritative — record the actual lineage once. See [`../ERRATA.md`](../ERRATA.md).
- **Reference symlinks (read-only, git-ignored):** `_REFERENCE/_EXTERNAL/` → `aixodev-collabs` (workflow-system source), `aixodev-web` (Flask/SQLite→Postgres pattern reference), and **`tastypantry`** (the sibling it integrates with for food/calorie/macro data).

## Integration surface (engineering)

- **TastyPantry → Sattvasic Health (food → macros):** the only integration the repo's own docs assert. TastyPantry specifies *what* was eaten; Sattvasic Health records calorie/macro detail and rolls it into daily/weekly/monthly trends. No shared code dependency (the two are developed independently per the docs).
- **Divia.Network fan-out (intended, not in-repo):** Sattvasic Health is meant to be the **macros reader** of the cross-app NL fan-out (DiviaHome Activity Log → TastyPantry / Sattvasic / LegendaryMoney). This membership is **one-directional / not stated in-repo** — ERRATA E-06. The recurring weekly-correlation agent (LATER-002 §6) is likewise **not** in the repo.
- **Bluetooth-scale + AI-food-ID nutrition capture (planned; white-label-able stack):** a planned-from-the-start capture path for the Food/Calorie/Macro domain pairs a **Bluetooth-connected (BLE) scale** with **AI food identification** — the AI photo view classifies *what* the food is, the scale reads its *actual weight*, and the two fuse into an accurate per-portion calorie/macro estimate (deliberately **not** photo-only portion estimation — the accuracy critique behind **R-007 / "Cal AI"**). Engineering-wise this is a **BLE pairing + scale-read + food-ID-inference + photo/weight-correlation** component. It is also the **shared / white-label-able stack that feeds TastyCal**: the same component would back a TastyPal-branded app, **TastyCal (by TastyPal)** (a 🔵 potential / under-consideration TastyPal product-line), for a different audience — so the component boundary should be drawn once rather than forked per brand surface. Business framing: [business brief](../ULTIMATE_VISION/PRODUCTS/SattvasicHealth/sattvasichealth.md); TastyCal side: [`tastypal.md`](tastypal.md) (engineering) / [`../ULTIMATE_VISION/PRODUCTS/TastyPal/tastycal.md`](../ULTIMATE_VISION/PRODUCTS/TastyPal/tastycal.md) (business).

## `[DEALBREAKER-HOOK]`s

**None recorded yet** (Phase 00 pending). Candidate irreversible-fork concerns implied by source material — to be confirmed/declared during Phase 00, **not asserted as committed**:
- **Cross-lab analyte normalization** onto one timeline (the central data-model challenge — getting the canonical-analyte/units/reference-range model wrong is expensive to retrofit).
- **SQLite→Postgres portability** — "keep the schema clean and Postgres-portable; avoid SQLite-specific features that won't translate" (a stated design constraint already).
- **Import-adapter / dedup architecture** for legacy/device sources ("many 'new' sources are really import adapters for an existing export format").
- *(All TBD — the model's point is that finding the small precious set of true hooks is itself Phase-00 work.)*

## Cross-references

- Paired business brief: [`../ULTIMATE_VISION/PRODUCTS/SattvasicHealth/sattvasichealth.md`](../ULTIMATE_VISION/PRODUCTS/SattvasicHealth/sattvasichealth.md).
- ERRATA (E-06 ecosystem membership; E-09 lineage): [`../ERRATA.md`](../ERRATA.md).
- Model: [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md).
- **Shared BLE-scale + AI-food-ID stack / white-label to TastyCal:** [`tastypal.md`](tastypal.md) (TastyCal engineering section) · business brief [`../ULTIMATE_VISION/PRODUCTS/TastyPal/tastycal.md`](../ULTIMATE_VISION/PRODUCTS/TastyPal/tastycal.md) · competitive-research **R-007** (Cal AI) in [`../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../_backlog_TODOs/RESEARCH-BACKLOG.md).
