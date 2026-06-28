# Workflow: Build New Project (Push-Based)

> Generate a new sibling project from the current project's conventions, tech stack, and workflow system. The "push" complement to `workflow_bootstrap_project.md` (which is "pull"-based).

## Quick Reference

| Item | Value |
|------|-------|
| Trigger | User wants a new project that shares the current project's tech stack and workflow system |
| Where it runs | **In the current (source) project's Claude Code session** |
| Input | Target directory path + scratch-pad notes describing the new project |
| Output | A complete project skeleton in the target directory: git repo, CLAUDE.md, README.md, app skeleton, workflows, specs scaffold |
| Mode | Normal Claude Code (interactive), solo |
| Time | 30-60 minutes |
| Tech stack details | `_workflows/techstacks/` (see [Tech Stack Index](#tech-stack-index)) |

---

## Tech Stack Index

Tech-stack-specific details — architectural components, skeleton generation instructions, and lessons learned — live in separate documents under `_workflows/techstacks/`. The main workflow references these by stack; the separation allows post-sprint review agents to read just the relevant stack document rather than parsing the entire workflow.

| Document | Stack | Status |
|----------|-------|--------|
| [`techstack--python_quart.md`](techstacks/techstack--python_quart.md) | Python 3.12+ / Quart (async) / async SQLAlchemy / aiosqlite→asyncpg / Alembic / Hypercorn / uv | **Active** — this project's stack |
| [`techstack--python_flask.md`](techstacks/techstack--python_flask.md) | Python 3.12+ / Flask / SQLAlchemy / SQLite / uv | **Active** — sibling fork for sync Flask projects |
| [`techstack--rust_tauri.md`](techstacks/techstack--rust_tauri.md) | Rust / Tauri / frontend TBD | **Placeholder** — awaiting content from a Rust/Tauri project's Claude instance |

To add a new stack: create `techstacks/techstack--{stack_slug}.md` following the structure of the Python/Flask document, and add a row to this index.

---

## 1. When to Use This vs. Bootstrap

| Scenario | Use This Workflow | Use `workflow_bootstrap_project.md` |
|----------|-------------------|-------------------------------------|
| New project with **same tech stack** as current project | **Yes** — inherit everything, only specify diffs | No |
| New project with a **completely different tech stack** | No | **Yes** — the pull-based approach lets the target project's Claude instance adapt from scratch |
| Porting workflows to an **existing project** that already has code | No | **Yes** — bootstrap is less invasive, doesn't generate app skeleton |
| Quick prototype that extends a pattern established in this project | **Yes** | No |

**Key insight:** This workflow treats the user's scratch-pad notes as **diffs against the current project**. If the current project is a Python/Flask app and the user says "Python/Flask app, Rx manager with refill runway," the agent understands: same tech stack, same conventions, different domain — generate accordingly.

---

## 2. Architectural Discussion

**This is the most important step. No files are created until it concludes with an approved manifest.**

The agent's role in this step is that of a **senior software engineer and expert-level architect** for the source project's tech stack. The user comes to the agent with an idea — maybe polished, maybe rough scratch-pad bullets — and the agent's job is to:

1. Understand what the user is describing
2. Map it onto the established tech stack's architectural components
3. Prefill every decision that can be inherited or inferred
4. Surface only the genuinely ambiguous decisions for discussion
5. Iterate until the user approves a complete manifest

### 2a. Read the Inputs

1. **Read the current project's `CLAUDE.md` in full** — this is the baseline for everything.
2. **Read the relevant tech stack document** from `_workflows/techstacks/` — this contains the full architectural components manifest with "Ask If..." guidance for each component.
3. **Read the user's notes** — scratch-pad bullets, outliner fragments, short paragraphs, whatever format they provided.

### 2b. Interpret the User's Notes as Diffs

The user's notes are **diffs against the current project**. The agent interprets:

- **What's explicitly the same** — user says "Python/Flask app" → confirm same stack, inherit all defaults
- **What's new domain content** — user describes data models, features, integrations → this is the project's unique identity, not a stack decision
- **What implies a stack decision** — user says "GPS map view" → implies a map library (Leaflet? Mapbox?). User says "sync with Google Calendar API" → implies an HTTP client library and OAuth flow. User says "import CSV data" → is that synchronous or does it need background jobs?
- **What's not mentioned but needs to be asked** — the "Ask If..." column in the tech stack document identifies these. The most common: does this project need a JavaScript SPA framework? What about client-side interactivity beyond server-rendered pages?

### 2c. Prefill and Present the Manifest

Using the tech stack document's Architectural Components Manifest, the agent prefills every component and presents a condensed summary. The format should make it easy for the user to scan inherited decisions quickly and focus on the items that need discussion.

**Condensed manifest format:**

```
ARCHITECTURAL MANIFEST — {Project Name}

Target: {directory path}
Short name / package: {derived_name}
Description: {1-2 sentences drafted from user's notes}

INHERITED FROM {source project} (confirm or override):
  Python 3.12+ / uv / hatchling / Flask 3.x / SQLAlchemy 2.0 / SQLite
  Flask-Migrate / pydantic-settings / Jinja2 / Bootstrap / pytest / Ruff
  JWT auth / No type checker / Local deployment only

FROM YOUR NOTES:
  - {Domain model 1}: {agent's interpretation}
  - {Domain model 2}: {agent's interpretation}
  - {Integration}: {agent's interpretation}
  ...

QUESTIONS (need your input):
  1. {Component N}: {specific question based on "Ask If..." guidance}
  2. {Component M}: {specific question}
  ...

PRIMARY WORK MODE: {sprint execution / research + analysis / mixed}
STARTING PHASE: {0 or 1}
```

### 2d. Iterate

The user responds — confirming most items, correcting some, answering questions. Each response is a **diff against the manifest**. The agent updates the manifest and, if new ambiguities surface, asks follow-up questions.

The iteration continues until the user says something like "looks good," "approved," or "let's go." The agent should NOT proceed to Step 3 without explicit approval.

**What "approved" means:** The manifest is now the **project generation spec**. Every component decision in it drives the skeleton generation, CLAUDE.md content, and dependency list. The agent should not revisit these decisions during generation unless it discovers a technical conflict (e.g., two chosen libraries are incompatible).

### 2e. The Right Number of Questions

The agent should aim for **3-7 questions** in the initial presentation, not 15+. Most components are inherited. The tech stack document's "Ask If..." column is the guide — only surface questions where the user's notes create genuine ambiguity.

If the user's notes are thorough and unambiguous, the initial presentation might have zero questions: "I've prefilled everything from your notes and the source project. Here's the manifest — does this look right?"

If the user's notes are sparse (just a project name and one-line description), more questions are needed — but still targeted, not exhaustive. Frame them as "here's what I'd default to, but these items could go either way."

### Example: Sattvasic Health

User provides:
```
## Sattvasic Health (prototype)
- Python/Flask app
- Rx manager (with refill runway => CVS Rx refills)
- Vitamin manager (with refill runway => Amazon Sub&Save ordering)
- import old/legacy data from everywhere else
    - all Libre CGM data
    - all Quest blood-test labwork
    - all old scale/weight/BP spreadsheets
    - Fitbit data (including sleep stages)
    - data from BP monitor mobile app
    - data from ketone monitor mobile app
```

Agent presents:
```
ARCHITECTURAL MANIFEST — Sattvasic Health

Target: (need from you)
Short name / package: sattvasic
Description: Personal health data management — Rx/vitamin tracking
  with refill runway calculations, plus unified import of health
  device data (CGM, labs, weight, BP, Fitbit, ketones).

INHERITED FROM aixocollabs:
  Python 3.12+ / uv / hatchling / Flask 3.x / SQLAlchemy 2.0 / SQLite
  Flask-Migrate / pydantic-settings / Jinja2 / Bootstrap / pytest / Ruff
  JWT auth / No type checker / Local deployment only

FROM YOUR NOTES:
  - Domain models: Rx, Vitamin, CGM Reading, Lab Result, Weight/BP
    Measurement, Fitbit Session, Ketone Reading (+ refill runway
    calculations for Rx and Vitamins)
  - Integrations: CVS (Rx refills), Amazon Sub&Save (vitamin orders),
    plus data importers for: Libre CGM, Quest labs, spreadsheet
    (weight/BP), Fitbit API, BP monitor app export, ketone monitor
    app export
  - Heavy data import emphasis — multiple legacy formats

QUESTIONS:
  1. Frontend interactivity: With "refill runway" dashboards and
     health data timelines, do you want server-rendered pages
     (Jinja2 + maybe HTMX for dynamic bits) or a richer JS
     framework? Bootstrap tables/charts may be sufficient for a
     prototype.
  2. Chart/visualization library: Health data (CGM, weight, BP
     over time) strongly suggests time-series charts. Chart.js
     via CDN? Or defer visualization to a later phase?
  3. External API access: Do you have API credentials for CVS and
     Amazon Sub&Save, or are those manual-entry features for now?
     Same question for Fitbit (has an OAuth API).
  4. Background jobs: Importing 6+ data sources — synchronous
     Flask requests, or should we plan for a task queue (e.g., RQ
     or Celery) for long-running imports?
  5. Target directory: Where should this project live?

PRIMARY WORK MODE: Sprint execution
STARTING PHASE: 0 (ideation) or 1 (first build)?
```

### Example: DiviaHome

User provides:
```
## DiviaHome (prototype)
- Python/Flask app
- Tasks => import all prior MyLifeOrganized task data
    - task data was previously exported to CSVs
    - also add the MLO-format parsers for direct extraction
- Events => sync with Google Calendar API
- GPS map view (like Google Timeline) => Divia AGENDA
    - map tasks + events to daily views
        - unfinished tasks roll-over to next day
```

Agent presents:
```
ARCHITECTURAL MANIFEST — DiviaHome

Target: (need from you)
Short name / package: diviahome
Description: Personal task/event organizer with MyLifeOrganized
  import, Google Calendar sync, and GPS-based daily timeline views.

INHERITED FROM aixocollabs:
  Python 3.12+ / uv / hatchling / Flask 3.x / SQLAlchemy 2.0 / SQLite
  Flask-Migrate / pydantic-settings / Jinja2 / Bootstrap / pytest / Ruff
  JWT auth / No type checker / Local deployment only

FROM YOUR NOTES:
  - Domain models: Task (with rollover logic), Event, DailyView,
    GPS Location/Track
  - Integrations: Google Calendar API (bidirectional sync),
    MyLifeOrganized (CSV import + MLO-format parser)
  - GPS/map feature — daily timeline view

QUESTIONS:
  1. Map library: "GPS map view like Google Timeline" — Leaflet.js
     (open source, free) or Google Maps JS API (requires API key,
     closer to the Timeline UX you're describing)? Or defer the
     map to a later phase and start with a list-based daily view?
  2. Frontend interactivity: The daily view with tasks + events +
     map is fairly interactive. Server-rendered with HTMX for the
     list portions + a JS map widget? Or does this warrant a
     richer frontend from the start?
  3. Google Calendar sync: This needs OAuth 2.0 credentials and a
     Google Cloud project. Do you have those set up? Sync
     direction: pull from Google → local, push local → Google,
     or bidirectional?
  4. Background jobs: Google Calendar sync and MLO import — run
     synchronously, or plan for a background task queue?
  5. Target directory: Where should this project live?

PRIMARY WORK MODE: Sprint execution
STARTING PHASE: 0 or 1?
```

---

## 3. Create Target Directory and Git Init

```bash
mkdir -p {target_dir}
cd {target_dir}
git init
```

**HARD RULE — Local Git Only:** The generated `CLAUDE.md` MUST include the following rule in its Git rules section, and the agent MUST obey it during this workflow:

> **NEVER interact with remote git servers.** No `git push`, `git pull`, `git fetch`, `git remote add`, `gh` commands, or any other operation that contacts GitHub, GitLab, Bitbucket, or any remote server. All git operations are strictly local. If the user wants to set up a remote, they will do it manually outside of Claude Code.

---

## 4. Generate Project Skeleton

This step generates the tech-stack-specific application scaffold. The agent reads the current project's source tree to understand the live patterns, then generates an equivalent minimal skeleton for the new project.

**The skeleton must be functional** — after this step, the tech stack's validation commands must all succeed (e.g., for Python/Flask: `uv sync --group dev`, `uv run pytest tests/ -v`, `uv run ruff check .`).

**Instructions for skeleton generation are in the tech stack document.** Read the "Skeleton Generation" section of the relevant techstack file:

- Python/Quart (async) → [`techstack--python_quart.md` § Skeleton Generation](techstacks/techstack--python_quart.md#skeleton-generation)
- Python/Flask → [`techstack--python_flask.md` § Skeleton Generation](techstacks/techstack--python_flask.md#skeleton-generation)
- Rust/Tauri → [`techstack--rust_tauri.md`](techstacks/techstack--rust_tauri.md) (placeholder)

The approved manifest from Step 2 drives which dependencies to include, which extensions to configure, and which directories to create.

### Stacks Without a Document

For tech stacks not yet documented in `_workflows/techstacks/`:

1. Read the current project's source tree to identify the foundational layer
2. List the files you would generate and the patterns you would replicate
3. **Present the plan to the user for approval** before generating any files
4. Generate the skeleton after approval
5. After the project is built, **write the tech stack document** so the next project benefits from this work

---

## 5. Generate CLAUDE.md

This is the most important generated file. Use the current project's `CLAUDE.md` as a **structural template** — same sections, same conventions, same level of detail — but with the new project's identity and domain.

### Sections to Generate

| Section | Source | Adaptation |
|---------|--------|------------|
| **Project Overview** | Rewrite entirely | New project name, description, domain context from the approved manifest. No "migration context" unless user specifies one. |
| **Tech Stack** | Copy table structure | Fill from the approved manifest. Update project-specific notes (e.g., remove "Matches `aixodev-web`" references). Add any components that were decided during the architectural discussion (map libraries, SPA framework, etc.). |
| **Quick Start** | Copy, adapt package name | Same `uv sync`, `uv run flask run`, `uv run pytest`, `uv run ruff` commands (or equivalent for the stack) |
| **Development Phases & Stages** | Generate fresh | Start with Phase 0 or Phase 1 as approved. Empty phases table. Same workflow links (adapted paths). |
| **Git conventions** | Copy verbatim | Same branch naming, commit prefixes |
| **Git rules** | Copy + add the local-only HARD RULE | All existing rules plus: **NEVER interact with remote git servers** (see Step 3) |
| **Agent rules** | Copy, adapt references | Same Opus-for-research rule. Remove project-specific reference-project entries unless user specifies new ones. |
| **Key File Locations** | Generate from actual structure | Reflect the directories created in Steps 4-8 |
| **Ensemble Collab-Groups** | Copy if user wants collab support | Same ensemble setup references |

### Sections to NOT Include

- **Migration Context** — unless the user explicitly mentions a migration target
- **Session Data Preservation Guarantee** — `aixocode`-specific, not a general pattern
- **"Message to My Future Self"** — project-specific; the new project may develop its own
- **References to sibling projects** — unless the user specifies them
- **graphify section** — unless the user requests it

### The Local-Only Git HARD RULE

The generated CLAUDE.md MUST include this in the Git rules section:

```markdown
- **NEVER interact with remote git servers.** No `git push`, `git pull`, `git fetch`,
  `git remote add`, `gh` commands, or any other operation that contacts GitHub, GitLab,
  Bitbucket, or any remote server. All git operations are strictly local. If the user
  wants to set up a remote, they will do it manually outside of Claude Code.
```

---

## 6. Generate README.md

Create a project-level `README.md` with:

- Project name and one-paragraph description
- Tech stack summary (table or bullet list, from the approved manifest)
- Quick start section (install, run dev server, run tests, lint)
- Project status (Phase 0 or 1, as approved)
- Directory structure overview (reflecting what was actually created)

Keep it concise — 50-80 lines. The README is for human orientation, not exhaustive documentation.

---

## 7. Copy and Adapt Workflow Files

Follow the same two-commit pattern from `workflow_bootstrap_project.md`:

### 7a. Verbatim Copy

```bash
cp -r {source_project}/_workflows/. {target_dir}/_workflows/
```

This includes the `techstacks/` subdirectory. The new project gets the full set of tech stack documents — even stacks it doesn't use. This is intentional: the new project may spawn further sibling projects with different stacks.

Commit as: `Migrate workflow docs verbatim from {source_project_name}`

### 7b. Mechanical Substitutions

Apply the substitutions from `workflow_bootstrap_project.md` Steps 7a-7e:

- **Project names** (7a): Replace source project name and short-name with target's
- **Relative paths** (7b): Adjust based on layout choice (root-level is the default for new projects)
- **Tech stack** (7c): For same-stack projects, this is mostly a no-op — just verify. For different stacks, substitute test/lint/dev-server commands.
- **Structural changes** (7d): Apply any condition-driven changes (research-only, no DB, etc.)
- **Preserve core patterns** (7e): The two-session pattern, sp/xp naming, commit prefixes, Critical Rules, etc.

Commit as: `Adapt migrated workflows: paths, project names, tech stack`

### 7c. Verify

```bash
# No leaked source-project references
grep -rn "{source_short_name}\|{source_full_name}" {target_dir}/_workflows/
# Should return only intentional cross-references (e.g., in the changelog noting the origin)
```

---

## 8. Create Specs and Plans Scaffold

```bash
mkdir -p {target_dir}/_backlog
mkdir -p {target_dir}/_research
```

### 8a. Backlog Horizon Files

Create four files with headers:

- `_backlog/_horizon_NEXT.md`
- `_backlog/_horizon_LATER.md`
- `_backlog/_horizon_SOMEDAY.md`
- `_backlog/_UNSORTED_QUEUE.md`

Use the same header format as the current project's horizon files.

### 8b. Templates

```bash
cp -r {source_project}/_workflows/_templates/. {target_dir}/_workflows/_templates/
```

Adapt project-name references in templates. The structural patterns (SPRINT_TEMPLATE, PHASE_README_TEMPLATE, DECISION_TEMPLATE, COLLAB_PROMPT_*, EXTERNAL_REVIEW_PROMPT, COLLAB_ROLE_*) are all reusable.

### 8c. Specs Index

Create `_stages_and_phases/README.md` with navigation table, primary-loop summary, and git conventions — adapted for the new project.

### 8d. ROADMAP.md

Create `_stages_and_phases/ROADMAP.md` with:

- Project name and one-line description
- Current status (Phase 0 or 1)
- Empty "Completed Phases" section
- "Planned Phases" section seeded from the approved manifest if it implied a multi-phase vision
- Backlog summary (all zeros)

---

## 9. Seed the Backlog (Optional)

If the user's scratch-pad notes describe features, data models, or integrations, the agent should triage them into the backlog horizons:

- **NEXT** — items clearly needed for the first sprint(s)
- **LATER** — items mentioned but not immediately needed
- **SOMEDAY** — stretch goals or vague ideas
- **UNSORTED_QUEUE** — anything ambiguous (the roadmap rescheduling workflow will sort these)

This step is optional — skip it if the user's notes were purely about the tech stack with no feature descriptions.

---

## 10. Initial Commits

Split across reviewable commits:

```bash
# Commit 1: Project skeleton (pyproject.toml, app scaffold, tests, config)
git add pyproject.toml .python-version .gitignore .env.example run.py app/ tests/
git commit -m "Initial project skeleton: Flask app factory, settings, test fixtures"

# Commit 2: Project docs (CLAUDE.md, README.md)
git add CLAUDE.md README.md
git commit -m "Add CLAUDE.md project guide and README"

# Commit 3: Workflow files (verbatim copy)
git add _workflows/
git commit -m "Migrate workflow docs verbatim from {source_project_name}"

# Commit 4: Workflow adaptation
# (make substitutions first, then commit)
git add _workflows/
git commit -m "Adapt migrated workflows: paths, project names, tech stack"

# Commit 5: Specs scaffold (backlog, templates, index, roadmap)
git add _stages_and_phases/
git commit -m "Add specs scaffold: backlog horizons, templates, index, roadmap"
```

Adjust commit grouping if some steps were skipped (e.g., no backlog seeding).

**Per Git Rules:**
- Local commits only — no `git push`
- No `--no-verify`, `--amend`, or destructive operations
- No `Co-Authored-By` trailers

---

## 11. Validate

Run the full validation suite in the target project:

```bash
cd {target_dir}
uv sync --group dev
uv run pytest tests/ -v        # Should pass (0 tests collected is OK)
uv run ruff check .            # Should pass clean
```

If either fails, fix the issue before proceeding. The skeleton must be in a green state.

### Verification Checklist

- [ ] `uv sync --group dev` succeeds
- [ ] `uv run pytest tests/ -v` passes (0 collected or all pass)
- [ ] `uv run ruff check .` passes clean
- [ ] `uv run flask run --debug` starts without errors (manual check — tell user to verify)
- [ ] `CLAUDE.md` has correct project name, tech stack from approved manifest, and the local-only git HARD RULE
- [ ] `README.md` has correct project name and quick-start commands
- [ ] `_workflows/README.md` references the correct project name
- [ ] `grep -rn "{source_short_name}" {target_dir}/` returns only intentional references
- [ ] Backlog horizons exist (if applicable)
- [ ] `_stages_and_phases/ROADMAP.md` exists with correct project name
- [ ] `git log --oneline` shows a clean 5-commit sequence
- [ ] Working tree is clean

---

## 12. What NOT to Copy

These are source-project-specific and must not appear in the target:

- **Phase directories** (`phase_01--*/`, etc.) — new project starts fresh
- **Research documents** in source `_research/` — target's research is its own concern
- **Sprint specs and execution plans** (`sp_*.md`, `xp_*.md`) — each project writes its own
- **Source project's `CLAUDE.md`** — target gets a generated one (Step 5)
- **Source project's `ROADMAP.md`** — target gets a fresh one (Step 8d)
- **Source project's `README.md`** — target gets a generated one (Step 6)
- **`PRODUCT_AND_NAMING.md`** — source-project-specific corporate hierarchy
- **`ENSEMBLE.md` / `ENSEMBLE-*.md`** — per-project collab setup docs
- **`_REFERENCE/` directory** — source-project-specific symlinks
- **Any `reference--*.md` files** — project-specific technical references
- **Source project's `.claude/` or `.codex/`** — agent config is per-project
- **Source project's `instance/` data** — runtime state, not part of skeleton
- **Source project's `migrations/` data** — schema is project-specific

---

## 13. Report to User

After all commits, present a summary:

```
New project "{Full Project Name}" created at {target_dir}.

Commits:
  1. {hash} Initial project skeleton
  2. {hash} CLAUDE.md + README
  3. {hash} Workflow docs (verbatim)
  4. {hash} Workflow adaptation
  5. {hash} Specs scaffold

Validation: pytest PASS | ruff PASS

Next steps:
  1. cd {target_dir}
  2. Review CLAUDE.md and README.md
  3. Start a new Claude Code session in that directory
  4. Begin Phase 0 (research/ideation) or Phase 1 (first sprint)
     using workflow_new_phase.md → workflow_start_new_sprint.md
```

---

## 14. Quick Command (for invoking this workflow)

From a Claude Code session **in the current project**:

```
Read and follow _workflows/workflow_build_new_project.md

New project:
  Target: /path/to/new-project
  Name: {Project Name}
  Notes:
    - {bullet points describing the project}
    - {features, data models, integrations}
    - {anything that differs from current project}
```

The agent reads the tech stack document, interprets the notes as diffs against the current project, prefills the architectural manifest, and presents it for discussion. Anything not mentioned is inherited.

---

## 15. Post-Sprint Review: Tech Stack Document Maintenance

As part of the Compound Engineering Stage B review (see [`workflow_compound_engineering.md`](workflow_compound_engineering.md) § Stage B), the agent or the user should consider whether the current tech stack document accurately reflects the latest learnings.

**Trigger questions for the reviewing agent:**

- Did this sprint introduce a new tool, library, or pattern that should become the default for new projects? (e.g., migrating from `pip` to `uv`, adding `HTMX` as a standard progressive-enhancement layer)
- Did this sprint discover a gotcha, workaround, or anti-pattern that future projects should avoid?
- Did a component decision from the manifest prove wrong or suboptimal? Should the "Current Default" or "Ask If..." guidance change?
- Is there a new "Lesson Learned" entry to add?

**Process:**

1. Read `_workflows/techstacks/techstack--{current_stack}.md`
2. Compare its content against what the project actually uses now
3. If there's a meaningful delta, propose an update to the tech stack document
4. Add an entry to the "Last Reviewed" table at the top of the document
5. Commit the update as part of the sprint closeout

This keeps the tech stack documents as living references that improve with every project — the same iterative refinement approach that evolved the workflow documents themselves.
