# New Project Guide (Canonical)

> **For a future Claude instance running in the MetaProject.** This is the authoritative how-to for creating a new project repository from the canonical template in `_canonical/project-template/`. Read it top to bottom before creating a project. The design rationale (why this exists, the drift problem it solves, the proposed sync/audit companions) lives in a longer proposal doc — `txfrcloud-protomolecule/_specs_and_plans/_research/metaproject-canonical-project-creation-proposal.md` — but everything you need to *execute* a creation is self-contained here.

---

## 1. The principle (read first)

The shared `_workflows/` development system used by ~30 sibling repos historically propagated by a **serial clone chain** (`aixodev-collabs → tastypantry → … → aixodev-aixovault → fracrealhomes-dailyspikedriver → …`). Every clone was a point-in-time snapshot that immediately began to drift, and cloning a *new* project from a sibling meant inheriting that sibling's mid-flight, drifted state — requiring git surgery to reconstruct a clean baseline.

This template inverts the direction. **`_canonical/project-template/` is the single, always-clean source.** You create a new project by copying it and filling in **one** file's worth of identity, not by cloning a drifting sibling. This is possible because the workflow system was refactored so that:

- **All per-project identity** lives in a single `_workflows/PROJECT_IDENTITY.md`.
- **All per-stack specifics** (commands, debugging) live in the active `_workflows/techstacks/techstack--*.md`.
- **Everything else** (`workflow_*.md`, `_templates/*.md`, `README.md`) is project-agnostic and byte-identical across all repos.

So the per-project surface is tiny: `PROJECT_IDENTITY.md` (deterministic fill) plus two genuinely bespoke docs (`CLAUDE.md` overview + `README.md` intro).

---

## 2. What's in the template

```
_canonical/project-template/
├── CLAUDE.md                     # skeleton — {{placeholders}} + <!-- AGENT: … --> prose
├── README.md                     # skeleton
├── LICENSE.md                    # templated (proprietary default; swap for OSS if needed)
├── .gitignore                    # generic Python/web default — TAILOR per stack
├── .python-version               # 3.12 — change/remove for non-Python stacks
├── _workflows/                   # canonical project-agnostic bodies + techstacks/ + _templates/
│   └── PROJECT_IDENTITY.md        # TEMPLATE — the one file you fully own per repo
├── _stages_and_phases/           # the scheduled execution plan
│   ├── README.md  ROADMAP.md     # skeletons
│   └── phase_00--ideation_and_research/   # README.md + DECISIONS.md skeletons
├── _backlog/                     # 4 empty horizon files
├── _research/.gitkeep            # research outputs land here
├── _status_reports/README.md     # reviews / audits scaffold
├── _documentation/README.md      # product-docs scaffold
└── _REFERENCE/                   # reference material (committed + git-ignored)
    ├── README.md                 # the _REFERENCE convention
    └── _assets/_screenshots/     # git-ignored scratch (scaffolded empty)
```

`_REFERENCE/` ships only the `README.md` convention doc and the empty git-ignored `_assets/_screenshots/` scaffold. `_REFERENCE/_EXTERNAL/` (the machine-specific reference symlinks) is intentionally NOT shipped — create it at instantiation if the new project needs reference symlinks.

---

## 3. The manifest (the inputs you gather)

Creating a project is driven by a small manifest — the same Q&A you'd ask the user. Where a business-side venture brief already exists (`_workflows/workflow_new_venture_intro_brief.md`), inherit its fields and only ask the deltas. Aim for the answers, not a long interview.

| Field → placeholder | Example | Notes |
|---|---|---|
| Full project name → `{{FULL_PROJECT_NAME}}` | `TXFR.Cloud — TXFRCloudProtomolecule (Build-Line)` | headline name |
| Short name / slug → `{{SHORT_NAME}}` | `txfrcloud-protomolecule` | repo dir + config/data dir |
| Env-var prefix → `{{ENV_PREFIX}}` | `TXFRCLOUD_PROTO_` | screaming snake, trailing `_` |
| One-line description → `{{ONE_LINE_DESCRIPTION}}` | "…a high-speed file-transfer service." | |
| Brand → `{{BRAND}}` | `TXFR.Cloud` | |
| Corporate entity → `{{CORP_ENTITY}}` | `TXFR.Cloud LLC` | for LICENSE |
| Copyright year → `{{COPYRIGHT_YEAR}}` | `2026` | |
| Package/module name → `{{PACKAGE_NAME}}` | `app` | house web default; stack-dependent |
| Ecosystem siblings → `{{ECOSYSTEM_SIBLINGS}}` | "`txfrcloud-service` (real); …" | or "none" |
| Active techstack doc → `{{ACTIVE_TECHSTACK_DOC}}` | `techstacks/techstack--python_quart.md` | must exist in `_workflows/techstacks/` (else §6) |
| Stack one-liner → `{{STACK_ONELINE}}` | `Python 3.12+ / uv / Quart / SQLAlchemy 2.0 / SQLite→Postgres` | |
| Per-project stack overrides → `{{STACK_OVERRIDES_OR_NONE}}` | "mypy optional" / "None" | deviations from stack defaults |
| Starting phase → `{{STARTING_PHASE}}` | `00` | usually 00; `01` if skipping ideation |
| Creation date → `{{CREATION_DATE}}` | `2026-06-25` | today (ask if unknown — the runtime can't read the clock reliably) |

Plus two non-placeholder inputs:
- **Placement** — which corporate/product umbrella → which on-disk directory (see §4 / `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`).
- **Primary work mode** — build app / research-only / docs-only (decides whether §5 runs).

---

## 4. Steps to create a project

### Step 1 — Gather the manifest (§3). Confirm it back to the user before creating anything.

### Step 2 — Resolve placement
From `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md` + the `_projects/` registry, determine the standardized target directory under the correct umbrella, e.g. `~/Code/<Umbrella>/{{SHORT_NAME}}`. Confirm the path with the user.

### Step 3 — Instantiate the template
```bash
TPL="$HOME/Code/_claude.MetaProject/_canonical/project-template"
DEST="<target dir from Step 2>"
mkdir -p "$DEST"
rsync -a "$TPL/" "$DEST/"
cd "$DEST" && git init
```
Because the template is release-clean, there is **no residue to scrub and no git surgery** — this is the whole point.

### Step 4 — Fill the per-project files
- **Deterministic substitution** across the instantiated files: replace every `{{PLACEHOLDER}}` with its manifest value, and delete the `<!-- TEMPLATE FILE … -->` header line from each file. Files: `_workflows/PROJECT_IDENTITY.md`, `CLAUDE.md`, `README.md`, `LICENSE.md`, `_stages_and_phases/README.md`, `_stages_and_phases/ROADMAP.md`, `_stages_and_phases/phase_00…/README.md` + `DECISIONS.md`, the four `_backlog/` headers.
- **Agent-written prose** for the genuinely bespoke parts marked `<!-- AGENT: … -->`: `CLAUDE.md` Project Overview, `README.md` intro, `PROJECT_IDENTITY.md` Project Context block, `ROADMAP.md` stance, `phase_00` goals, `DECISIONS.md` ADR context/consequences. Write these from the manifest + domain understanding (look at a sibling project's CLAUDE.md for tone). Delete the `AGENT` comments when done.
- **Verify** no markers remain: `grep -rn '{{' .` and `grep -rn '<!-- AGENT:' .` should both be empty.

### Step 5 — Per-stack skeleton (build projects only; skip for research/docs-only)
Open the active techstack doc (`_workflows/{{ACTIVE_TECHSTACK_DOC}}`) and run its **Skeleton Generation** section to produce a functional app skeleton (the logic is also described in `_workflows/workflow_build_new_project.md`). Then run its **Commands & Validation** to confirm green (e.g. `uv sync --group dev && uv run pytest tests/ -v && uv run ruff check .`). Tailor `.gitignore` / `.python-version` to the stack.

### Step 6 — First commit(s) (local-only — house rule, no remote, no `Co-Authored-By`)
Split for reviewability, e.g.:
```bash
git add _workflows .gitignore .python-version && git commit -m "Initialize {{SHORT_NAME}} workflow system from canonical template"
git add CLAUDE.md README.md LICENSE.md _stages_and_phases _backlog _research _status_reports _documentation _REFERENCE && git commit -m "Add {{FULL_PROJECT_NAME}} project docs and Phase {{STARTING_PHASE}} scaffold"
# + a skeleton commit if Step 5 ran
```

### Step 7 — Make it reachable (keep this LIGHT — see §8)
Add a symlink so the MetaProject orchestrator can reach the new repo:
```bash
ln -s ../../<Umbrella>/{{SHORT_NAME}} "$HOME/Code/_claude.MetaProject/_projects/{{SHORT_NAME}}"
```
**Do NOT** auto-write `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md` entries or fully regenerate the registry index yet — per John, the org-model/registry standardization is deliberately deferred while things iterate. Just note the new project to the user so they can register it when they choose.

### Step 8 — Report
Path, commits, validation result, and the next step (Phase {{STARTING_PHASE}} ideation via `_workflows/workflow_start_new_sprint.md`).

---

## 5. The standardized layout (decided 2026-06 — the GEN2 layout)

This template **defines the standard directory layout** for all future projects, which fixes the drift across the fleet (e.g. some repos had `_research/` at project root, others under `_specs_and_plans/`). The previously-open question is now **decided**: the overloaded `_specs_and_plans/` is split into three root-level directories —

- **`_backlog/`** — unscheduled ideas (the four horizon files).
- **`_research/`** — investigations, analyses, syntheses (at project **root**).
- **`_stages_and_phases/`** — the scheduled execution plan: `ROADMAP.md` + phases + sprint plans (renamed from `_specs_and_plans/`; the name ties to the GEN2 **Stages → Phases → Sprints** hierarchy).

…plus three standard scaffolds: **`_status_reports/`** (reviews/audits), **`_documentation/`** (product docs), and **`_REFERENCE/`** (a convention `README.md` + a git-ignored `_assets/_screenshots/`).

This template is the single definition of the standard — when a layout decision changes, **edit `_canonical/project-template/` to match**, never scatter it across repos. To bring an *existing* (drifted) repo up to this standard, follow **`MIGRATE_ADAPT.md`** — the migration playbook that lists the known drift patterns and the merge-don't-clobber gotchas.

---

## 6. If the chosen stack has no techstack doc yet

The template ships techstack docs for the stacks built so far (Python/Quart, Python/Flask, a Rust/Tauri placeholder). The fleet will add Rust (e.g. `txfrcloud-service`, tokio), Flutter, Kotlin, Swift, etc. If the manifest names a stack with no `techstacks/techstack--{stack}.md`:

1. Author it during the create run, following the structure of `techstack--python_quart.md` (Architectural Components Manifest, **Commands & Validation**, Skeleton Generation, **Debugging**, Lessons Learned).
2. Point `PROJECT_IDENTITY.md`'s "Active techstack doc" at it.
3. **Contribute it back** to `_canonical/project-template/_workflows/techstacks/` so the next project on that stack inherits it. (This is the upstreaming discipline — see §9.)

---

## 7. Templated vs. agent-written — the split

| Generated by deterministic substitution | Written by the agent (domain-aware) |
|---|---|
| `PROJECT_IDENTITY.md` identity table + active-stack pointer | `PROJECT_IDENTITY.md` Project Context block |
| `LICENSE.md`, backlog headers, `_stages_and_phases/README.md` | `CLAUDE.md` Project Overview |
| `ROADMAP.md` tables, `phase_00` structure, `DECISIONS.md` identifiers | `README.md` intro; `ROADMAP` stance; `phase_00` goals; ADR context/consequences |

Rationale: identity is mechanical and must be exact; the overview/intro genuinely vary by domain (a file-transfer service reads differently from a real-estate one) and benefit from the agent actually understanding the project.

---

## 8. What NOT to do (John's explicit constraints)

- **No automated sync tool.** Bringing existing repos up to the new standard is a deliberate, **manual, one-time, walk-through-each-project** activity (see §9) — John wants to review each delta personally. Do not build or run a bulk push.
- **No org-model / registry auto-writes during create** (Step 7 stays light). Deferred while the model iterates.
- **Never hand-edit `_workflows/` *body* files in a downstream repo.** Project-specifics go in `PROJECT_IDENTITY.md` or `CLAUDE.md`. Body changes happen only in the canonical (§9).
- **Never clone from a sibling to create a new project.** Use this template. (The three legacy creation workflows — `workflow_bootstrap_project.md`, `workflow_build_new_project.md`, `workflow_adapt_project_from_clone.md` — survive only as fallbacks: porting into a pre-existing/foreign repo, or genuinely forking a specific project's *content*.)

---

## 9. Maintaining the canonical (the two-direction loop)

The canonical only stays authoritative if improvements flow back into it. Improvements are usually discovered *while working in a downstream repo* (e.g. the identity-isolation refactor was first built in `fracrealhomes-dailyspikedriver`). The discipline:

1. Make and test the workflow improvement in whatever repo surfaced it.
2. **Port it into `_canonical/project-template/_workflows/`** (this directory) — the canonical now leads.
3. New projects inherit it automatically. Existing repos get it during the manual standardization pass.

**Bringing an existing repo to standard (manual, deferred):** for one repo at a time — `diff -r _canonical/project-template/_workflows  <repo>/_workflows` (excluding `PROJECT_IDENTITY.md`), review the delta with John, and apply the canonical version by hand. This is a one-time fix per repo; everything created from this template onward is already conformant.

---

## 10. Verification checklist for a freshly created project

- [ ] `grep -rn '{{' .` and `grep -rn '<!-- AGENT:' .` return nothing (all placeholders filled, all guidance prose written).
- [ ] No `<!-- TEMPLATE FILE … -->` header lines remain.
- [ ] `_workflows/PROJECT_IDENTITY.md` fully reflects the new project; its "Active techstack doc" points at a doc that exists.
- [ ] `CLAUDE.md` / `README.md` describe the new project in its own domain terms.
- [ ] If a build project: the techstack's validation suite is green.
- [ ] `git log` shows a clean first-commit sequence; working tree clean; no remote.
- [ ] The user has been told the new project exists (and, optionally, a `_projects/` symlink was added).
