# LATER-007 — Mine the old `aixodev-web` entity-model spec (so no idea is lost), then treat it as a backlog source

- **Captured:** 2026-06-22, MetaProject session (the migration/self-hosting reorganization).
- **Status:** LATER — the old spec is **moved to backlog as a *mining source*, not a build target**; `aixodev-web` v0.5 is built for the *new* model's types (see [`../_REFERENCE/MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](../_REFERENCE/MIGRATION-AND-SELF-HOSTING-PROPOSAL.md) §1b).
- **Owning project:** `aixodev-web` (the v0.5 PostgresModeledGraph Build-Line, and later v1).
- **The source doc:** `_projects/aixodev-web/_specs_and_plans/phase_05--entity_model_and_platform_vision/reference--entity_model_specification.md` (v1.0, 2026-03-11; 12 entity families, ~75 tables). Predates the Build-Line/Triangulation-Target model — its overlaps are partly coincidental, and it mixes time-horizons (exactly the over-scope the new model cures), so we do **not** pull it in wholesale. Companion: [`../_REFERENCE/AIXODEV-WEB-HISTORY-CATALOG.md`](../_REFERENCE/AIXODEV-WEB-HISTORY-CATALOG.md).

## Why this file exists

The old spec is ~80% of the v0.5 schema spine *as plumbing* — but its highest-value **ideas** are a handful of cross-cutting mechanisms that are **absent from the current model and not the Build-Line/Stage pair we already flagged**. This file preserves them so the recurring "don't lose any idea we previously captured" rule holds, while the active build proceeds on the new model only.

## Preserved ideas (file these; nothing lost)

| # | Idea | Disposition | Old-spec § |
|---|---|---|---|
| **B-1 ★** | **`ResearchProject` / `ResearchItem`** typed-research containers (source/finding/experiment/conclusion/question/note + confidence; cross-linked to the AI session that produced them) — attach to **Ideas (Layer A)**. The model says "research lives on the Idea" but gives it no structure; this is also what the research-recovery workflow writes into. | KEEP/adapt | §5 |
| **B-2 ★** | **`Goal` / `KeyResult`** OKR spine with **auto-rollup from completed issues/Features**, re-pointed at **Milestones/Stages** (drop "Initiative"). Makes "the dated Target is measurable" a *mechanism*, not an assertion. | ADAPT | §6 |
| **B-3 ★** | **`Agent`** as a first-class entity, separate from `User` (model/persona/`soul_file`/token-budget/permissions/mention-handle). The model is saturated with agents but has no entity for one. | KEEP | §8, §16.3 |
| **B-4** | **ltree-for-deep-hierarchies + the polymorphic `(entity_type, entity_id)` tagging pattern** — the storage substrate for Topic taxonomies + Idea↔Idea edges on the Postgres host. | KEEP (engineering canon) | §16.1–.2 |
| **B-5** | **Issue/Feature ≠ DevTask** split (request vs. execution); DevTask carries a **polymorphic person-or-agent assignee**. | ADAPT | §7, §16.4 |
| **B-6** | **`adoption_decisions`** (rationale / alternatives / decided-by / date) as the per-Build-Line dependency + **`[DEALBREAKER-HOOK]` decision log** (registry itself → codemap). | ADAPT | §12 |
| **B-7** | Pluggable **`prioritization_scores`** (RICE/ICE/MoSCoW/WSJF + manual override) as the **Sorting-Hat** scoring backend — *placement input, not venture ranking* (respect John's metric-distrust). | ADAPT | §10 |
| **B-8** | **`@aixodev` platform-verified workflow steps** (machine-checks "tests passing / branch clean / plan exists") — the executable form of the project's own CLAUDE.md process rules. | KEEP (defer full engine) | §9, §19.3 |
| **B-9** | Dated **health-snapshot / update log** on Milestones + Triangulation-Targets (gives "re-checked every planning pass" an audit trail; feeds future-scenario projection). | ADAPT | §6 `initiative_updates` |
| **B-10 ★** | **Custom-fields** (`custom_field_definitions`/`_values`) as the model's **no-migration evolvability hatch** — lets the net-new axes (Build-Envelope, dated-Target, research-scope flag, the four Idea axes Conviction/Horizon/Provenance/Leverage) land as *data*, not a migration per axis. Promote from "Phase-6 nice-to-have" to a **v0.5 enabler**. | KEEP (promote) | §15 |

**File first (the four that fill genuine gaps in the current model):** **B-1, B-2, B-3, B-10.**

## Explicit drops (recorded so they aren't re-litigated)

`initiatives`-as-a-top-level-container (superseded by Stage/Milestone — keep only its update-log, B-9) · `backlogs`/`backlog_items` horizon containers (retired by the re-bucketable future Version-Releases + the Sorting-Hat — keep the *scoring*, B-7, drop the *containers*) · §18 tiered sprint plan · §16.5 naming conventions.

## Also flagged (handle in v0.5, not here)

- **Two competing entity-model specs** exist (the Phase-5 engineering `reference--entity_model_specification.md` vs. the product-strategy `03-entity-model-spec-v2.md`) — reconcile during the v0.5 schema design.
