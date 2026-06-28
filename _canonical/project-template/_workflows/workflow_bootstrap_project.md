# Workflow: Bootstrap Project Workflows

> Adapt this workflow system for a new project — copy, re-point, re-name, commit.

## Quick Reference

| Item | Value |
|------|-------|
| Trigger | Starting a new git repository that should use this workflow system |
| Input | This project's `_workflows/` directory (37 files, ~4,250 lines) |
| Output | A customized `_workflows/` in the target project + a `_stages_and_phases/` scaffold + an updated `CLAUDE.md` |
| Mode | Normal Claude Code (interactive), solo |
| Time | 30-60 minutes (verbatim copy: 5 min; adaptation pass: 25-55 min depending on tech-stack substitutions) |

---

## 1. When to Use This Workflow

Use this when you have a new git repository for a distinct project and want to install the same structured development workflow — phases, sprints, spec/execution-plan pairs, backlog horizons, collab-group reviews, research protocols — that this project uses.

This workflow produces a **customized copy** of the workflow files. Not a fork. Not a symlink. Each project owns its workflow docs independently and can evolve them over time. The changelog at the top of `README.md` (the "Workflow Updates" log) exists precisely so downstream projects can track what has evolved in the source and decide whether to pull forward specific changes.

---

## 2. Prerequisites

Before starting:

- [ ] The target project has a git repository initialized (first commit or `No commits yet` state is fine)
- [ ] You know the project's name, short-name, tech stack, and the nature of the work (product development, research, analysis, docs, etc.)
- [ ] You have filesystem read access to a source project whose `_workflows/` you are migrating from
- [ ] You've decided where `_workflows/` will live in the target (see Step 3)

---

## 3. Decide the Target Layout

There are two supported placements for the `_workflows/` directory. This choice drives every relative-path substitution below, so fix it before copying.

| Layout | `_workflows/` location | When to choose |
|--------|------------------------|----------------|
| **Root-level** (simpler, newer default) | `{project-root}/_workflows/` | Research/analysis repos, small-scope projects, any repo where workflow docs are primary artifacts and you want them visible at the top level |
| **Nested under specs** (legacy, matches `aixodev-web`) | `{project-root}/_stages_and_phases/_workflows/` | Projects with heavy sprint/phase artifacts where workflows co-locate naturally with specs, backlog, research, and templates |

Both layouts are first-class. The files themselves are identical; only the internal relative-path references differ.

**Heuristic:** If the project is primarily a research/analysis/documentation effort, use root-level. If the project is a product build that will accumulate many `phase_NN--*/` directories and sprint specs, the nested layout may feel more natural.

---

## 4. Gather Project Context

Ask the human (or read from the target project's existing CLAUDE.md / README.md):

| Field | Example | Used For |
|-------|---------|----------|
| **Full project name** | "AIXO.Dev Collabs" / "Divia AI Desktop Pro" | Replaces the source project name in headers and prose |
| **Short name** | "aixocollabs" / "divia" / "aixocode" | Replaces source short-name in branch patterns, env-var prefixes, slugs |
| **Tech stack** | "Python 3.12 + Typer + SQLite" / "SvelteKit + Supabase" / "Research-only (no code)" | Adjusts test/lint commands, dev-server references, migration references |
| **Package manager** | "uv" / "pnpm" / "npm" / "None" | Adjusts all CLI command examples |
| **Test command** | "uv run pytest tests/ -v" / "pnpm test" / "None" | Referenced in execution and verification steps |
| **Dev server command** | "uv run flask run" / "pnpm dev" / "None" | Appears in sprint-execution workflow |
| **Lint command** | "uv run ruff check ." / "pnpm lint" / "None" | Added to verification steps if available |
| **Type-check command** | "uv run mypy src/" / "pnpm check" / "None" | Optional, same treatment as lint |
| **Database** | "PostgreSQL" / "SQLite" / "Supabase" / "None" | Adjusts migration references |
| **Has migrations?** | Yes / No | If no, strip migration references from Critical Rules templates |
| **Deployment target** | "Vercel" / "Docker Compose" / "Local only" / "N/A (research)" | Adjusts deployment references |
| **Primary work mode** | "Sprint execution" / "Research + analysis" / "Mixed" | Determines which workflows are primary vs. rarely used |
| **Starting phase number** | Usually 0 (ideation) or 1 (first build phase) | For CLAUDE.md's phases table |

Record these in a scratch doc (or inline in the chat) — you'll reference them throughout.

---

## 5. Create Directory Structure

**Root-level layout:**

```bash
cd /path/to/target-project
mkdir -p _workflows
mkdir -p _backlog
mkdir -p _research
mkdir -p _stages_and_phases/_templates
```

**Nested layout:**

```bash
cd /path/to/target-project
mkdir -p _stages_and_phases/_workflows
mkdir -p _backlog
mkdir -p _research
mkdir -p _stages_and_phases/_templates
```

---

## 6. Copy the Workflow Files Verbatim

Start with a byte-identical copy. Do not adapt yet. A clean verbatim baseline makes the subsequent adaptation commit easy to review.

**Root-level layout:**

```bash
cp -r /path/to/source/_workflows/. /path/to/target/_workflows/
```

**Nested layout:**

```bash
cp -r /path/to/source/_stages_and_phases/_workflows/. /path/to/target/_stages_and_phases/_workflows/
```

**Verify:**

```bash
diff -r /path/to/source/_workflows/ /path/to/target/_workflows/   # should print nothing
find /path/to/target/_workflows -type f | wc -l                    # should match source count
```

Commit this verbatim copy as a dedicated commit before touching a single word of adaptation. This matters because (a) the diff for the adaptation commit becomes readable, and (b) if the adaptation pass ever needs to be redone, you have a clean baseline to return to.

### Current File Inventory (37 files, snapshot at 2026-04-24)

**Top-level files (29):**

| Category | Files |
|----------|-------|
| Index | `README.md` |
| **Sprint Pipeline (active)** | `workflow_start_new_sprint.md`, `workflow_sprint_planning_solo.md`, `workflow_sprint_planning_collab.md` (router), `workflow_execute_sprint_dev_plan.md`, `workflow_sprint_code_review_solo.md`, `workflow_sprint_code_review_collab.md` (router), `workflow_sprint_closeout.md` |
| **Supporting (active)** | `workflow_new_phase.md`, `workflow_code_audit.md`, `workflow_quick_fix.md`, `workflow_roadmap_rescheduling_solo.md`, `workflow_roadmap_rescheduling_collab.md` (router), `workflow_claude_md_maintenance.md`, `workflow_research.md`, `workflow_ideation.md`, `workflow_error_debugging.md`, `workflow_bootstrap_project.md` (this file), `workflow_collab_group_launch.md` (router), `workflow_collab_group_agent_guidelines.md`, `workflow_collab_group_code_review.md` (router) |
| **Deprecated redirects** | `workflow_new_sprint.md`, `workflow_new_sprint_solo.md`, `workflow_new_sprint_collab.md`, `workflow_post_sprint_review.md`, `workflow_backlog_triage.md`, `workflow_code_review.md`, plus legacy pre-`workflow_`-prefix stubs `new_sprint.md` and `error_debugging.md` |

**Subdirectory files (8):**

| Subdirectory | Files | Purpose |
|--------------|-------|---------|
| `aixocode-collab/` | `workflow_collab_group_launch.md`, `workflow_collab_group_code_review.md`, `workflow_new_sprint_collab.md`, `workflow_roadmap_rescheduling_collab.md` | Native `aixocode`-control-socket-driven collab implementations |
| `ensemble-collab/` | Same four files | Legacy ensemble-backed collab implementations |

The top-level "router" files for sprint-planning-collab, sprint-code-review-collab, roadmap-rescheduling-collab, collab-group-launch, and collab-group-code-review all delegate to one of these subdirectories based on a user prompt at the start of the session.

---

## 7. Apply Mechanical Substitutions

After the verbatim copy is committed, make a **single dedicated adaptation commit** that applies mechanical substitutions. Use `sed` or equivalent — no need to manually edit each file for obvious patterns.

### 7a. Project-Name Substitutions

| Find (source context) | Replace With | Where it appears |
|-----------------------|--------------|------------------|
| Full source project name (e.g., `AIXO.Dev Platform (Web)`) | `{Full Project Name}` | README headers, section headers, prose |
| Source short-name in slugs/branches (e.g., `aixodev` in `aixodev/@claude/...`) | `{short_name}` | Branch patterns |
| Source short-name in uppercase env vars (e.g., `AIXODEV_`) | `{SHORT_NAME}_` | Env var prefixes |
| Source repo name (e.g., `aixodev-web`) | `{target_repo_name}` | Cross-references |
| Source corporate/platform umbrella (e.g., `AIXO.Dev Platform` when it refers to the broader platform) | **Usually preserve** | Context-dependent — if the target project is part of the same corporate umbrella, keep it |

**Judgment call:** Be surgical with "umbrella" references. A workflow that says "this project is part of the AIXO.Dev Platform family" is true for sibling projects in the ExoDev.AI universe, not true for a totally unrelated downstream adopter. Substitute the specific-project-name references and preserve the umbrella references unless the target project is outside the umbrella entirely.

### 7b. Relative-Path Substitutions

These depend on your layout choice from Step 3. The workflows were originally authored assuming the **nested layout**, so the root-level case requires more adjustments.

**If you chose nested layout (`_stages_and_phases/_workflows/`):** paths mostly already work. Verify they resolve correctly:

| Source path in workflows | Resolves to |
|--------------------------|-------------|
| `../../CLAUDE.md` | `{project-root}/CLAUDE.md` ✓ |
| `../ROADMAP.md` | `{project-root}/_stages_and_phases/ROADMAP.md` ✓ |
| `../_templates/` | `{project-root}/_stages_and_phases/_templates/` ✓ |
| `../_backlog/` | `{project-root}/_backlog/` ✓ |
| `../README.md` | `{project-root}/_stages_and_phases/README.md` ✓ (specs index, not project README) |

**If you chose root-level layout (`_workflows/`):** rewrite paths as follows:

| Source path | New path | Why |
|-------------|----------|-----|
| `../../CLAUDE.md` | `../CLAUDE.md` | One-up now reaches project root |
| `../ROADMAP.md` | `../_stages_and_phases/ROADMAP.md` | ROADMAP lives in specs dir |
| `../_templates/` | `../_stages_and_phases/_templates/` | Templates live in specs dir |
| `../_backlog/` | `../_backlog/` | Backlog lives in specs dir |
| `../README.md` | `../_stages_and_phases/README.md` | Specs index, not project README |
| `../PRODUCT_AND_NAMING.md` | `../_stages_and_phases/PRODUCT_AND_NAMING.md` | If target project has one |
| `_stages_and_phases/_workflows/` (narrative references) | `_workflows/` | Workflows are now at root |

**Suggested sed invocation for root-level layout:**

```bash
cd /path/to/target/_workflows
for f in *.md */*.md; do
  sed -i \
    -e 's|\.\./\.\./CLAUDE\.md|../CLAUDE.md|g' \
    -e 's|\.\./ROADMAP\.md|../_stages_and_phases/ROADMAP.md|g' \
    -e 's|\.\./_templates/|../_stages_and_phases/_templates/|g' \
    -e 's|\.\./_backlog/|../_backlog/|g' \
    -e 's|\.\./PRODUCT_AND_NAMING\.md|../_stages_and_phases/PRODUCT_AND_NAMING.md|g' \
    -e 's|_stages_and_phases/_workflows/|_workflows/|g' \
    "$f"
done
# NOTE: ../README.md substitution is ambiguous — sometimes references the project root README,
# sometimes the specs index README. Handle by hand after the mechanical pass.
```

After sed, grep for the original patterns to confirm none leaked through:

```bash
grep -rn -E "\.\./\.\./CLAUDE\.md|\.\./_templates/|\.\./_backlog/" _workflows/
# Should print nothing.
```

### 7c. Tech-Stack Substitutions

| Find | Replace With | Applies if... |
|------|--------------|---------------|
| `uv run pytest tests/ -v` | `{test_command}` | Not a Python/uv project |
| `uv run ruff check .` | `{lint_command}` | Not Ruff |
| `uv run mypy src/` | `{type_check_command}` | Not mypy |
| `uv run python -m flask` / `uv run flask` | `{framework_cli}` | Not Flask |
| `./dev_server.sh` | `{dev_server_command}` | Different dev-server pattern |
| `logs/dev_server.log` | `{log_path}` or remove | Different logging setup |
| `flask db migrate` / `flask db upgrade` | `{migration_command}` / `{migration_apply}` or remove section | Different or no DB |
| `PostgreSQL` | `{database}` | Different DB |
| `brew services start postgresql@16` | `{db_start_command}` or remove | Not macOS / not Postgres |

### 7d. Structural Changes (condition-driven)

| Condition | Action |
|-----------|--------|
| No database / no migrations | Remove the migration references from Critical Rules templates and execution-sequence examples |
| No dev server | Remove the dev-server lifecycle section from sprint-execution workflows |
| No hooks infrastructure | Remove hook-related sections from `workflow_error_debugging.md` |
| Frontend-only project | Simplify error debugging to browser console + build errors |
| Monorepo | Add workspace/package scoping to branch naming conventions |
| **Research-only project** | Elevate `workflow_research.md` to primary; flag the sprint pipeline as "rarely used — present for completeness"; keep `workflow_ideation.md`, `workflow_code_audit.md`, and `workflow_quick_fix.md` as secondary |
| **Docs-only project** | Keep research + ideation + bootstrap; deprecate sprint pipeline entirely |

### 7e. Sections to Always Keep As-Is

Do not adapt these — they are the conceptual backbone and should survive intact:

- The two-session pattern (Plan → Human Review → Execute)
- The `sp_` / `xp_` file naming convention
- The commit prefix convention (`P{N}-S{NN}-T{NN}`)
- The branch naming convention (with short-name adapted)
- Critical Rules concept and structure
- Compound Engineering review process (`workflow_compound_engineering.md`)
- Fresh-session discipline guidance
- Post-sprint notes structure
- The Workflow Updates changelog at the top of README.md (preserve entries verbatim — it documents the origin project's evolution)

---

## 8. Create Template Files

Copy and adapt templates from the source `_templates/`:

```bash
cp -r /path/to/source/_stages_and_phases/_templates/. /path/to/target/_stages_and_phases/_templates/
```

**Current template inventory (7 templates):**

| Template | Adaptations Needed |
|----------|-------------------|
| `SPRINT_TEMPLATE.md` | Branch-name pattern |
| `PHASE_README_TEMPLATE.md` | Branch-name pattern |
| `DECISION_TEMPLATE.md` | None (fully generic) |
| `COLLAB_PROMPT_SPRINT_PLANNING.md` | Project-name references, commit prefix |
| `COLLAB_PROMPT_CODE_REVIEW.md` | Project-name references, validation commands |
| `COLLAB_PROMPT_ROADMAP_RESCHEDULING.md` | Project-name references |
| `EXTERNAL_REVIEW_PROMPT.md` | Project-name references, tech-stack context |

Skip this step if the target project has no sprint/planning artifacts (e.g., pure research repo).

---

## 9. Create Backlog Horizon Files

Create three empty horizon files with header comments:

```markdown
# Backlog: Horizon NEXT

> Features we're confident we want and have enough design clarity to implement
> in the next 1-2 phases.
>
> **Last reviewed:** {today's date}

---

(No items yet — add features as they're identified during development.)
```

Create `_horizon_NEXT.md`, `_horizon_LATER.md`, `_horizon_SOMEDAY.md`, and `UNSORTED_QUEUE.md`.

Skip this step if the target project has no backlog-management needs.

---

## 10. Create Specs Index

Create `_stages_and_phases/README.md` with:

- Quick navigation table (phases, backlog, workflows, templates, research)
- The primary-loop summary (New Phase → Planning → Review → Execute → Code Review → Closeout)
- Git conventions (branch naming, commit prefixes)
- Link to the project-root `CLAUDE.md` as authoritative reference
- Link to `_workflows/README.md` for the comprehensive workflow guide

Skip if `_stages_and_phases/` won't exist (root-only layout with no specs artifacts).

---

## 11. Update Target Project's CLAUDE.md

Add (or extend) a "Workflows" section in the target `CLAUDE.md`:

- Development phases table (initially just Phase 00 or Phase 01)
- Git branch-naming convention (adapted for this project's short-name)
- Git commit-prefix convention
- Link to the `_workflows/` directory and its README
- Clean working tree rule
- Primary-loop summary (one paragraph)
- Pointer to `workflow_bootstrap_project.md` for downstream bootstraps from this project

Include the key Git Rules inline (always commit after work, never push without approval, never amend, etc.) — these are project-level constants, not workflow-specific.

---

## 12. Initial Commits

Split the migration across at least three commits so the diff is reviewable:

```bash
# Commit 1: verbatim migration
git add _workflows/ README.md
git commit -m "Migrate workflow docs verbatim from {source-project-name}"

# Commit 2: mechanical substitutions (paths + project names + tech stack)
git add _workflows/
git commit -m "Adapt migrated workflows: paths, project names, tech stack"

# Commit 3: templates + backlog + specs index (skip if not applicable)
git add _stages_and_phases/
git commit -m "Add specs scaffold: templates, backlog horizons, index"

# Commit 4: CLAUDE.md
git add CLAUDE.md
git commit -m "Scaffold project CLAUDE.md with workflows section"
```

Keeping these as separate commits means any one layer can be redone in isolation later without touching the others. A single-commit bootstrap is tempting for brevity but loses that flexibility.

**Per the source project's Git Rules:**
- Local commits only; no `git push` without explicit human approval
- No `--no-verify`, `--amend`, or destructive operations without explicit approval
- No `Co-Authored-By` trailers — git author is sufficient

---

## 13. Verify

- [ ] `diff -r` against the source `_workflows/` shows only intentional changes (names, paths, tech-stack substitutions)
- [ ] All `workflow_*.md` files reference the correct target project name
- [ ] Branch-naming pattern uses the correct short-name
- [ ] Test/lint commands match the target's actual tooling (or are flagged as N/A)
- [ ] Dev-server and DB references match (or are removed)
- [ ] `grep -rn "AIXO.Dev Platform (Web)\|aixodev-web\|openhands/@\|aixodev-openhands" _workflows/` returns only intentional cross-references
- [ ] Templates are in place (if applicable)
- [ ] Backlog horizons exist (if applicable)
- [ ] `CLAUDE.md` has the Workflows section with correct paths
- [ ] Working tree is clean
- [ ] `git log --oneline` shows a clean 2-4 commit sequence for the bootstrap

---

## 14. What NOT to Copy

These are source-project-specific and should not be ported:

- **Phase directories** (`phase_01--*/`, etc.) — the new project starts fresh
- **Research documents** in the source's `_research/` — target-project research is its own concern
- **Sprint specs and execution plans** (`sp_*.md`, `xp_*.md`) — each project writes its own
- **Hook-related runtime infrastructure** — unless the target project also uses Claude Code hooks
- **`PRODUCT_AND_NAMING.md`** — describes the source project's corporate hierarchy
- **Any `reference--*.md` files** in the source — project-specific technical references
- **Source project's `CLAUDE.md`** — the target gets its own, adapted
- **Source project's `ROADMAP.md`** — the target will build its own over time

---

## 15. Post-Bootstrap: First Real Work

After bootstrapping, immediately start the target project's Phase 0 (ideation/research) or Phase 1 (first build phase) using `workflow_new_phase.md` → `workflow_start_new_sprint.md`. This validates that the adapted workflows work correctly in the new project context.

If any workflow reference turns out to be wrong for the new project during Phase 0/1, fix it in-line and commit the correction. The workflows should be living documents that evolve with the project — and the "Workflow Updates" log at the top of `_workflows/README.md` is where those evolutions get recorded for posterity.

---

## 16. Quick Command (for invoking this workflow)

In a new Claude Code session on the target project:

```
Read the bootstrap workflow at /path/to/source/_workflows/workflow_bootstrap_project.md
and follow it to install the development workflow system for this project.

Project details:
- Full name: {Full Project Name}
- Short name: {short_name}
- Repo name: {repo_name}
- Tech stack: {stack}
- Package manager: {pm}
- Test command: {test_cmd} (or "N/A")
- Dev server: {dev_cmd} (or "N/A")
- Database: {db} (migrations: yes/no)
- Primary work mode: {sprint execution | research + analysis | mixed | docs-only}
- Target layout: {root-level | nested under _stages_and_phases}
- Source project: {path to source's _workflows/}
```
