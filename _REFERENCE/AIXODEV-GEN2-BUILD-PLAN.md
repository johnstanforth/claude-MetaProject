# `aixodev-GEN2` — Build & Lift-and-Shift Plan (v0.5)

> Plan (2026-06-22), John + Claude. The **first project built fully in the new model**: a Python/Flask web app whose entire v0.5 purpose is **CRUD for the new-model entities**, so John can create/edit Projects · Build-Lines · Stages · Phases · Sprints · Ideas · Topics in a UI. This is the migration proposal's **BL-B "PostgresModeledGraph"** ([`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md)). Source inventory + the base recommendation are in the Appendix of [`AIXODEV-WEB-HISTORY-CATALOG.md`](AIXODEV-WEB-HISTORY-CATALOG.md).

## Status & re-entry notes (2026-06-22)

*(Written so this doc is a complete post-compact re-entry point — re-reading it + the pointers below is all that's needed to continue.)*

- **Steps 1–5 are DONE and committed** in `aixodev-GEN2`. Step 1 (repo) + Step 2 (scaffold) @ `28b8df6`; **Steps 3 + 4 + 5 @ `9a1d0d8`** (the combined Codex task — full v0.5 entity model + generic-factory CRUD UI/API + the `flask seed-import` markdown importer). **The build now resumes at the iterate-and-eyeball loop** (John runs `./run_dev_server.sh`, requests changes; ~10–20 disposable passes; then the "take it seriously" demarcation → Postgres+LTREE + migrations + the Evolvability Hatch).
- **What `9a1d0d8` contains (Claude-reviewed + independently verified):** all 17 entities with correct constraints (Repository `CHECK(local_dir OR remote_url)`, `project_repositories` association-object + `UNIQUE`, `idea_channels` dated channel-symlink, typed `idea_edges`, `BuildLine.idea_id` NOT NULL + `research_scope`, re-bucketable `TriangulationTarget`, `stage_milestones` M2M); ONE `register_crud_blueprint` factory driving list/create/edit/delete + JSON API for the 13 standalone entities; explicit relationship screens (Idea⇄Topics, Idea→Venture channels, Idea⇄Idea edges, Project⇄Repositories, Stage⇄Milestones); a Project re-parent cycle-guard. **6 pytest pass; real `seed-import` loaded 25 topics + 62 ideas + 83 tag-links.** SQLite drop-and-regenerate, no migrations — no auth/Alembic/health-endpoint/Docker (verified absent).
- **Known minor items (non-blocking; throwaway phase):** 5 of 62 ideas didn't auto-link a Topic (their `Topic(s)` bullets don't use the canonical `../TOPICS/<slug>.md` link form — best-effort parser, editable in the UI); `datetime.utcnow()` + legacy `Query.get()` deprecation warnings (cosmetic; address at the demarcation, not now).
- **Codex model question — RESOLVED:** the `skill-codex` wrapper prints a misleading `[codex-wrapper] Launching with profile: work ... [gpt-5.5 : high]` banner, but the **Codex usage panel confirmed billing decremented `gpt-5.3-codex-spark`** — i.e. `-m gpt-5.3-codex-spark --config model_reasoning_effort=xhigh` *did* take effect. Trust the usage panel over the banner; no wrapper fix needed.
- **Re-entry pointers:** the entity *semantics* live in [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) + [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md); the as-built schema is in `aixodev-GEN2/app/models/` (`strategy.py`/`ventures.py`/`project.py`/`build.py`); the source `-workgroups` schema is in **Appendix AP.4 of [`AIXODEV-WEB-HISTORY-CATALOG.md`](AIXODEV-WEB-HISTORY-CATALOG.md)**.

## The framing (confirmed 2026-06-22)

- **One new repo: `aixodev-GEN2`.** Every existing repo is a **frozen "scavenge-source"** — never edited. We **re-implement** chosen functionality in GEN2 (not `git pull`), verify GEN2 works with its small feature subset, and **only ever edit GEN2.**
- v0.5 stack: **Python · Flask · SQLAlchemy · server-rendered Jinja/HTMX/Bootstrap** (the `aixodev-projects` stack). **No auth** in v0.5 (single-user, local).
- **No Sacred Cows — throwaway-fast iteration (critical).** GEN2 has *no users but John, who isn't even using it except to eyeball prototypes.* So for the **first ~48 hours / first ~10–20 plan→build→replan passes** there are **NO migrations** — each pass just **drops the local SQLite DB and regenerates the schema** from the models. Iterate hard toward a *minimal, barely-working* CRUD UI; treat every version as disposable. **Codex must be told this explicitly** — it tends to defend a 10-minute-old "production" schema; here there is nothing precious to protect.
- **The "take it seriously" demarcation:** once we have a minimally-usable, stable version, we **(a) move to Postgres + LTREE and (b) add the Evolvability Hatch** (custom-fields, [`LATER-007`](../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md) B-10) — *that* is the point we adopt proper Alembic migrations and stop dropping the DB. Not before. (The real graph-DB stays a v1 concern validated in KSVGPS.)
- Once the UI works, **Build-Lines are defined *in the UI*** — GEN2 becomes the authoritative organizer, the first project expressed in the model it enforces.

## Lift-and-shift sources (read-only)

| From | Lift | How |
|---|---|---|
| **`aixodev-projects`** (BASE) | The running **Flask app skeleton** (app-factory · blueprints · services · Jinja+Bootstrap templates · Alembic · SQLite→Postgres discipline) **and** the working **Project / ProjectRepository / ProjectLanguage CRUD** (models · `project_service.py` cycle-guard · views · templates · tests). **Strip the entire design-theme/token subsystem** (8 tables, irrelevant). | *Re-implement* the lifted code into GEN2 (clean copy, not a clone), verify each piece runs. |
| **`aixodev-workgroups`** (SCHEMA) | The better **Repository/association design** — a shareable `Repository` entity (`CHECK(local_dir OR remote_url)`), a `project_repositories` association object (`role`/`is_primary`), and `projects.local_path` — with ready SQLAlchemy 2.0 ORM in `DEV_PLAN.md §1.1` / `analysis-09`. | *Implement fresh* from its design (no code exists to lift). |

## The v0.5 entity model (what the CRUD UI edits)

Relational schema (LTREE for deep trees; adjacency for shallow), grouped by the two layers. Net-new entities (everything except Project/Repository/Techstack) are implemented fresh, following the lifted CRUD pattern.

- **Layer A — Strategic Landscape:** `Topic` (taxonomy, ltree) · `Idea` (durable; the four axes Conviction/Horizon/Provenance/Leverage) · `idea_topics` (M2M) · `idea_edges` (typed: `depends-on`/`variant-of`/`enables`/`successor-of`).
- **Layer B — Ventures & engineering:** `Venture` (brand) · `idea_channels` (the time-bounded **channel-symlink** Idea→Venture: `start_date`/`end_date`) · `Project` (hierarchy + `local_path`) · `Repository` + `project_repositories` (the workgroups design) · `Techstack` (first-class).
- **Build structure:** `BuildEnvelope` (named/reusable: scale·scope·team·timeframe·stack) · `BuildLine` (**owned by an Idea**; `build_envelope_id`; `techstack_id`; the **`research_scope` flag** playground/optimization) · `TriangulationTarget` (dated; `build_line_id`; **re-bucketable** across Build-Lines) · `Stage` (engineering span, `build_line_id`) · `Milestone` (business point, dated; some = Product Version-Releases) · `stage_milestones` (M2M, the Stage⟷Milestone join) · `Phase` (`stage_id`) · `Sprint` (`phase_id`).
- *(Deferred — the **Evolvability Hatch** (custom-fields, [`LATER-007`](../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md) B-10) is **not** in the rapid-iteration phase; it lands at the "take it seriously" demarcation, alongside Postgres + LTREE + migrations.)*

CRUD UI = list / create / edit / delete for each entity + manage the relationships (tag an Idea to Topics, channel an Idea to a Venture, attach Build-Lines to an Idea, attach a Build-Envelope + Techstack + research-flag to a Build-Line, Stages→Phases→Sprints, Stage⟷Milestone).

## Build steps (the content of each pass)

1. **[John] Create the empty repo:** `~/Code/AIXO.Dev/aixodev-GEN2` + `git init` + the GitHub remote + the `_projects/aixodev-GEN2` symlink (as with `divia_ai-agentswarms`). *(Or tell me to do the local `mkdir`/`git init`.)*
2. **Scaffold** — re-implement `aixodev-projects`' Flask skeleton into GEN2 (app-factory · blueprints · services · Jinja+Bootstrap templates · `run_dev_server.sh`); **strip themes**; **SQLite, no migrations.**
3. **Schema (drop-and-regenerate)** — implement the v0.5 entity model above: lift Project/ProjectRepository/Techstack (graft the workgroups Repository design), then add the net-new Build-Line/Build-Envelope/Stage/Milestone/Phase/Sprint/Idea/Topic/Target entities + relationships. **`create_all`-style regeneration each pass — NO Alembic** until the demarcation. Postgres-portable *in spirit* (`db.JSON`, named constraints) but don't over-engineer.
4. **CRUD UI + API** — list/create/edit/delete + relationship management for each entity, following the lifted pattern; a few smoke tests per entity (not exhaustive — it's throwaway).
5. **Seed-import** the **v0.1 markdown bootstrap** (`_REFERENCE/ULTIMATE_VISION/{IDEAS,TOPICS}/` + the briefs' Build-Line/Stage tables) so John edits the whole portfolio on day one.
6. **[Claude] Verify** the pass: app runs, UI CRUDs the entities, markdown imports.

*Expect to run the plan→build→eyeball→replan cycle **~10–20 times over the first couple days** — each pass disposable (drop the DB, regenerate) — converging on a minimal, stable, barely-working CRUD UI. Only **then** the demarcation (Postgres + LTREE, migrations, the Evolvability Hatch).*

## Execution model — Claude orchestrates, Codex builds, Claude reviews & commits

**Claude is the main orchestrator and the quality gate; Codex is the fast builder.** Per build-step (steps #2–#5, and each re-iteration) — *not* the whole plan at once:

1. **Claude writes a narrowly-scoped "Step-N only" coding task** — one step's content, with precise acceptance criteria + the explicit "no sacred cows / drop-and-regenerate, don't defend the schema" instruction.
2. **Claude delegates it to Codex** via the `skill-codex` plugin (e.g. *"use codex with gpt-5.3-codex-spark at xhigh to execute this Step-N task"*).
3. **Codex builds it in its own context** — so the implementation detail does **not** burn Claude's orchestrator context.
4. **Claude reviews the result adversarially** — does it match the assigned task? Is it correct, *minimal*, and high-quality? **Code quality is the highest priority** — if Codex over-engineered, added unrequested machinery, or implemented something poorly, **Claude pushes back and re-delegates to Codex to fix it differently** (citing the specific problem). Repeat until it passes.
5. **Claude does the git commit** of the reviewed/approved work — only after it passes review. Lift-and-shift discipline holds: **re-implement, don't `git pull`; verify GEN2 works** with its small subset at each step.

*This run is also an **experiment**: does the `skill-codex` path give fast, subagent-level builds that complete quickly **without consuming Claude's main-loop context** — distinct from the back-and-forth collab-group? We'll learn across the ~10–20 passes.*

## Cross-references

- Source inventory + GEN2-base rationale: [`AIXODEV-WEB-HISTORY-CATALOG.md`](AIXODEV-WEB-HISTORY-CATALOG.md) (Appendix AP.4).
- The model: [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) · [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md) · [`CODEMAP-AND-SHARED-FRAMEWORK-MODEL.md`](CODEMAP-AND-SHARED-FRAMEWORK-MODEL.md).
- The bigger plan + preserved ideas to fold in: [`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md) · [`../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md`](../_backlog_TODOs/LATER-007-aixodev-web-entity-model-spec-mining.md).
