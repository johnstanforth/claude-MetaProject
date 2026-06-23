# `aixodev-GEN2` — Build & Lift-and-Shift Plan (v0.5)

> Plan (2026-06-22), John + Claude. The **first project built fully in the new model**: a Python/Flask web app whose entire v0.5 purpose is **CRUD for the new-model entities**, so John can create/edit Projects · Build-Lines · Stages · Phases · Sprints · Ideas · Topics in a UI. This is the migration proposal's **BL-B "PostgresModeledGraph"** ([`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md)). Source inventory + the base recommendation are in the Appendix of [`AIXODEV-WEB-HISTORY-CATALOG.md`](AIXODEV-WEB-HISTORY-CATALOG.md).

## The framing (confirmed 2026-06-22)

- **One new repo: `aixodev-GEN2`.** Every existing repo is a **frozen "scavenge-source"** — never edited. We **re-implement** chosen functionality in GEN2 (not `git pull`), verify GEN2 works with its small feature subset, and **only ever edit GEN2.**
- v0.5 stack: **Python · Flask · SQLAlchemy · SQLite→Postgres-portable · server-rendered Jinja/HTMX/Bootstrap** (the `aixodev-projects` stack). **No auth** in v0.5 (single-user, local) — defer until multi-user is needed. Relational Postgres + LTREE for deep hierarchies (per the [migration decision §3.2](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md)); the real graph-DB stays a v1 concern validated in KSVGPS.
- Once the UI works, **Build-Lines are defined *in the UI*** — GEN2 becomes the authoritative organizer, the first project expressed in the model it enforces.

## Lift-and-shift sources (read-only)

| From | Lift | How |
|---|---|---|
| **`aixodev-projects`** (BASE) | The running **Flask app skeleton** (app-factory · blueprints · services · Jinja+Bootstrap templates · Alembic · SQLite→Postgres discipline) **and** the working **Project / ProjectRepository / ProjectLanguage CRUD** (models · `project_service.py` cycle-guard · views · templates · tests). **Strip the entire design-theme/token subsystem** (8 tables, irrelevant). | *Re-implement* the lifted code into GEN2 (clean copy, not a clone), verify each piece runs. |
| **`aixodev-workgroups`** (SCHEMA) | The better **Repository/association design** — a shareable `Repository` entity (`CHECK(local_dir OR remote_url)`), a `project_repositories` association object (`role`/`is_primary`), and `projects.local_path` — with ready SQLAlchemy 2.0 ORM in `DEV_PLAN.md §1.1` / `analysis-09`. | *Implement fresh* from its design (no code exists to lift). |
| **`aixodev-codemap`** (PATTERNS) | Only the **API-envelope + test-fixture patterns** — not its domain tables (wrong shape). | Optional reference. |
| **`aixodev-web`** (LATER) | Mature **auth/RBAC/admin** + the lossless-session-ingest API — *only if/when* GEN2 needs multi-user or session capture. | Deferred past v0.5. |

## The v0.5 entity model (what the CRUD UI edits)

Relational schema (LTREE for deep trees; adjacency for shallow), grouped by the two layers. Net-new entities (everything except Project/Repository/Techstack) are implemented fresh, following the lifted CRUD pattern.

- **Layer A — Strategic Landscape:** `Topic` (taxonomy, ltree) · `Idea` (durable; the four axes Conviction/Horizon/Provenance/Leverage) · `idea_topics` (M2M) · `idea_edges` (typed: `depends-on`/`variant-of`/`enables`/`successor-of`).
- **Layer B — Ventures & engineering:** `Venture` (brand) · `idea_channels` (the time-bounded **channel-symlink** Idea→Venture: `start_date`/`end_date`) · `Project` (hierarchy + `local_path`) · `Repository` + `project_repositories` (the workgroups design) · `Techstack` (first-class).
- **Build structure:** `BuildEnvelope` (named/reusable: scale·scope·team·timeframe·stack) · `BuildLine` (**owned by an Idea**; `build_envelope_id`; `techstack_id`; the **`research_scope` flag** playground/optimization) · `TriangulationTarget` (dated; `build_line_id`; **re-bucketable** across Build-Lines) · `Stage` (engineering span, `build_line_id`) · `Milestone` (business point, dated; some = Product Version-Releases) · `stage_milestones` (M2M, the Stage⟷Milestone join) · `Phase` (`stage_id`) · `Sprint` (`phase_id`).
- **Evolvability hatch (recommended):** `custom_field_definitions`/`custom_field_values` (per [`LATER-007`](../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md) B-10) so further axes land as data, not migrations.

CRUD UI = list / create / edit / delete for each entity + manage the relationships (tag an Idea to Topics, channel an Idea to a Venture, attach Build-Lines to an Idea, attach a Build-Envelope + Techstack + research-flag to a Build-Line, Stages→Phases→Sprints, Stage⟷Milestone).

## Steps

1. **[John] Create the empty repo:** `~/Code/AIXO.Dev/aixodev-GEN2` + `git init` + the GitHub remote + the `_projects/aixodev-GEN2` symlink (as with `divia_ai-agentswarms`). *(Or tell me to do the local `mkdir`/`git init`.)*
2. **[Claude or Codex] Scaffold** the Flask app by re-implementing `aixodev-projects`' skeleton into GEN2 (app-factory, blueprints, services, templates, Alembic, `run_dev_server.sh`); **strip themes.**
3. **[Claude or Codex] Schema:** implement the v0.5 entity model above — lift Project/ProjectRepository/Techstack (graft the workgroups Repository design), then add the net-new Build-Line/Build-Envelope/Stage/Milestone/Phase/Sprint/Idea/Topic/Target entities + relationships; Alembic migrations; Postgres-portable (`db.JSON`, named constraints, LTREE where deep).
4. **[Claude or Codex] CRUD UI + API** for every entity, following the lifted pattern; tests per entity.
5. **[Claude or Codex] Seed-import** the **v0.1 markdown bootstrap** (`_REFERENCE/ULTIMATE_VISION/{IDEAS,TOPICS}/` + the briefs' Build-Line/Stage tables) as the first dataset — validating the schema on real data and giving John the whole portfolio to edit on day one.
6. **[Both] Verify:** the app runs; the UI creates/edits all entities; the markdown imports cleanly; each lifted piece works in GEN2's small-subset context.

## Execution

The plan is structured to be runnable by **Codex** (John may say *"use codex with gpt-5.3-codex-spark at xhigh to execute the plan"* → delegated via the `skill-codex` plugin) or by Claude. Lift-and-shift discipline: **re-implement, don't `git pull`; verify GEN2 works at each step**, even though it holds a small fraction of any source repo's features.

## Cross-references

- Source inventory + GEN2-base rationale: [`AIXODEV-WEB-HISTORY-CATALOG.md`](AIXODEV-WEB-HISTORY-CATALOG.md) (Appendix AP.4).
- The model: [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) · [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md) · [`CODEMAP-AND-SHARED-FRAMEWORK-MODEL.md`](CODEMAP-AND-SHARED-FRAMEWORK-MODEL.md).
- The bigger plan + preserved ideas to fold in: [`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md) · [`../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md`](../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md).
