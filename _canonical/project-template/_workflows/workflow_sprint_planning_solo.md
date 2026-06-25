# Workflow: Sprint Planning (Solo)

> Planning-only workflow for sprints where Claude plans directly with the human. Produces the sprint spec (`sp_`) and execution plan (`xp_`), commits them, and hands off to human review. Execution is handled by `workflow_execute_sprint_dev_plan.md`.

## Quick Reference

| Item | Value |
|------|-------|
| Branch naming | `claudecode/@claude/phase{NN}-sprint{NN}` |
| Commit prefix | `P{NN}-S{NN}-T{NN} Description` |
| Sprint spec | `sp_{NN}--{slug}.md` (what and why) |
| Execution plan | `xp_{NN}--{slug}.md` (how, self-contained) |
| Prerequisite | `workflow_start_new_sprint.md` has been run (branch exists, context gathered) |
| Output | Two committed documents + hand-off instructions |
| Validation suite | `uv run pytest tests/ -v` + `uv run ruff check .` (no mypy) |

---

## Pipeline Position

```
  +-----------------------+    +--------------------+
  | workflow_new_phase.md |--->| start_new_sprint   |
  | (Phase 01 only)       |    | (branch + context) |
  +-----------------------+    +--------------------+
                                        |
                                        v
                                  YOU ARE HERE
                                        |
                                        v
                               +--------------------+
                               | SPRINT PLANNING    |
                               | SOLO               |
                               | (this workflow)    |
                               +--------------------+
                                        |
                                        v
                               +--------------------+
                               | Human Review       |
                               | (async)            |
                               +--------------------+
                                        |
                                        v
                               +--------------------+
                               | execute_sprint     |
                               | _dev_plan          |
                               | (autonomous)       |
                               +--------------------+
                                        |
                                        v
                               +--------------------+
                               | External Reviews   |
                               | (Gemini, Cursor,   |
                               |  KimiK25, etc.)    |
                               +--------------------+
                                        |
                                        v
                               +--------------------+
                               | sprint_code_review |
                               | (solo or collab)   |
                               +--------------------+
                                        |
                                        v
                               +--------------------+
                               | sprint_closeout    |
                               +--------------------+
```

---

## Prerequisites

Before starting this workflow, ALL of the following must be true:

- [ ] `workflow_start_new_sprint.md` has been run
- [ ] Sprint branch exists: `claudecode/@claude/phase{NN}-sprint{NN}`
- [ ] Context has been gathered (CLAUDE.md, phase README, previous sprint notes, backlog horizons)
- [ ] User has chosen "solo" as the planning path

---

## Step 1: Research Sprint Scope

With context already gathered during `workflow_start_new_sprint`, discuss scope with the user.

### 1a. Review Available Inputs

Read (if not already in context):

- **Backlog NEXT horizon** (`_specs_and_plans/_backlog/_horizon_NEXT.md`) -- items ready for implementation
- **Backlog UNSORTED_QUEUE** (`_specs_and_plans/_backlog/_UNSORTED_QUEUE.md`) -- recently triaged items
- **Previous sprint's `sp_` doc** -- post-sprint notes, follow-up items, lessons learned
- **Phase README** -- phase goals, sprint history, remaining work
- **Phase DECISIONS.md** -- any ADRs that constrain upcoming work

### 1b. Discuss Scope with the User

Present a proposed scope and ask for feedback:

- What is the primary goal of this sprint?
- Which backlog items should be pulled in?
- What follow-up items from the previous sprint must be addressed?
- Are there dependencies on external systems or human actions?
- What is explicitly out of scope?

Iterate until the user is satisfied with the sprint scope. This is a conversation -- the first proposal is rarely the final one.

### 1c. Compound Engineering Planning Check

Before finalizing scope, run **Stage A (Sprint Planning — Compound Investment Check)** from [`workflow_compound_engineering.md`](workflow_compound_engineering.md):

- Does this sprint include at least one task that improves development infrastructure (tests, docs, tooling, DX)?
- Are there items flagged in the previous sprint's Compound Engineering Findings that haven't been picked up?
- If no infrastructure work is planned, note this as a conscious decision in the sp file.

This check takes 2-3 minutes and ensures the project's compound rate doesn't stall.

---

## Step 2: Write Sprint Spec (`sp_{NN}--{slug}.md`)

Create the sprint spec in the phase directory: `_specs_and_plans/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md`

### Required Sections

```markdown
# Sprint {NN}: {Title}

| Field | Value |
|-------|-------|
| Phase | {N} -- {Phase Name} |
| Sprint | {NN} |
| Status | PLANNING |
| Date | {YYYY-MM-DD} |
| Branch | `claudecode/@claude/phase{NN}-sprint{NN}` |
| Commit Prefix | `P{NN}-S{NN}` |
| Predecessor | Sprint {NN-1} -- {Previous Title} |

## Goals

{2-5 bullet points describing what this sprint accomplishes}

## Non-Goals

{Explicit boundaries -- what this sprint does NOT do}

## Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| T01 | {Short name} | {One-line description} | Pending |
| T02 | ... | ... | Pending |

## Acceptance Criteria

{Bulleted list of conditions that must be true for the sprint to be considered complete}

## Deliverables

{Links to files or artifacts produced by this sprint, if known}

## Post-Sprint Notes

{Placeholder -- filled after execution}
```

### Guidelines for Writing Tasks

- Each task should be completable in one commit
- Tasks should be ordered by dependency (T01 before T02 if T02 depends on T01)
- Include test tasks explicitly -- do not assume tests are implicit
- 5-12 tasks is typical; more than 15 suggests the sprint should be split
- Each task description should be specific enough to be unambiguous but concise enough to scan in a table
- If a task requires human action, tag it explicitly in the description (e.g., "[Human] Configure GitHub OAuth")

---

## Step 3: Write Execution Plan (`xp_{NN}--{slug}.md`)

Create the execution plan in the same phase directory: `_specs_and_plans/phase_{NN}--{phase_slug}/xp_{NN}--{sprint_slug}.md`

The execution plan is the document a fresh agent session reads to execute the sprint autonomously. It must be **self-contained** -- the agent should not need to read any other files to implement the sprint.

**Self-containment rule:** The xp must inline all implementation details needed for autonomous execution. The test for self-containment: **could a fresh Claude session execute this sprint by reading only the xp file?** If the answer is no, the xp needs more detail. Specifically:

- If a task implements a data model, the xp must include **all field names, types, and status/type enums** -- not just "implement the model from the ADR."
- If a task creates a database schema, the xp must include the **complete DDL** or model definitions -- not just table names.
- If a task implements a configuration surface, the xp must include the **full field list with defaults** and an example snippet.
- If a task follows patterns from external research, the xp must describe the pattern inline -- not reference a research document.

### Required Sections (in order)

#### 3a. Context and Scope Boundaries (REQUIRED -- must be first section)

This section is **mandatory** and must appear first in every execution plan. It establishes the mental frame for the entire sprint.

```markdown
## Context and Scope Boundaries

{One paragraph setting overall perspective: what this sprint builds, where it fits
in the phase, and what the agent should keep in mind throughout execution.}

### Scope Boundary To Preserve

- {Explicit boundary 1 -- e.g., "This sprint modifies only the session subsystem; do not touch issue or wiki models."}
- {Explicit boundary 2}
- {Explicit boundary 3}

### Critical Rules

1. **Run `uv run pytest tests/ -v` after every task.** Tests must pass before committing. Defer `uv run ruff check .` to one final pass after all tasks are complete — see [`EFFICIENCY_RULES.md` § E11](EFFICIENCY_RULES.md#e11-defer-ruff-linting-to-end-of-coding-session). Both must pass before the sprint is done, but running ruff per-task wastes tokens on false positives (e.g., imports that appear "unused" mid-sprint but are needed by later tasks).
2. **Keep the schema clean and Postgres-portable; treat migrations carefully.** Generate an Alembic migration for every model change, review the autogenerated migration before applying it, and avoid SQLite-specific behavior that won't translate to PostgreSQL. Never hand-edit a live database file. Preserve ingested source data (e.g. raw Gmail/Zillow/Redfin email payloads) — store the original bytes alongside any parsed fields so a bad parse can be reprocessed.
3. **Commit after each task.** Use the `P{NN}-S{NN}-T{NN} Description` format. Do not batch multiple tasks into one commit.
4. **2-attempt rule ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)): if 2 fix attempts fail, STOP and flag for human review.** Do not continue spiraling.
5. **Clean working tree.** The final task must leave `git status` clean. Commit ALL files including spec/plan updates.
6. **Follow existing patterns.** Check how similar features are implemented before writing new code.
7. **Do not broaden scope.** If you discover something that needs fixing but is outside this sprint's scope boundaries, note it in post-sprint notes -- do not fix it now.
{8+. Sprint-specific rules as needed.}
```

#### 3b. Conventions

```markdown
## Conventions

- Commit prefix: `P{NN}-S{NN}-T{NN}`
- Branch: `claudecode/@claude/phase{NN}-sprint{NN}`
- Technology: Python 3.12+ Quart (async Flask) web app (uv; async SQLAlchemy 2.0; SQLite → PostgreSQL; Alembic; Jinja2)
- Validation: `uv run pytest tests/ -v` + `uv run ruff check .`
```

#### 3c. Pre-Execution Findings

Document what was discovered during planning:

```markdown
## Pre-Execution Findings

### Current State
- The `{relevant_service}.py` currently handles X via Y pattern
- The `{Model}` model has columns: ...
- The API endpoint at `/api/v1/...` accepts: ...

### Patterns to Follow
- All new services should follow the pattern in `{example_service}.py`
- New API endpoints need both API (JSON) and view (HTML) routes
```

#### 3d. Responsibility Tagging

Only include this section when human steps exist:

```markdown
## Responsibility

| # | Task | Owner | Notes |
|---|------|-------|-------|
| T01 | {Description} | [Claude] | |
| T02 | {Description} | [Human] | {Why human is needed} |
```

#### 3e. Execution Sequence

```markdown
## Execution Sequence

T01 -> T02 -> T03 (sequential, each depends on previous)
T04, T05 (independent, can be done in any order after T03)
T06 -> T07 (T07 is the final cleanup/docs task)
```

#### 3f. Task Details

For each task, provide enough detail for unambiguous implementation:

```markdown
## Task Details

### T01: {Task title}

**Files to modify:**
- `{path/to/file.py}` -- {what changes and why}

**Implementation:**
1. {Specific step 1}
2. {Specific step 2}
3. {Specific step 3}

**Tests:**
- {What to test and where}
```

#### 3g. Risks

```markdown
## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| {Description} | Low/Medium/High | Low/Medium/High | {How to mitigate} |
```

---

## Step 4: Verify Planning Output

Before committing, verify the planning documents against this checklist:

| Check | Pass? |
|-------|-------|
| Sprint spec filename follows `sp_{NN}--{slug}.md` pattern | |
| Execution plan filename follows `xp_{NN}--{slug}.md` pattern | |
| xp has "Context and Scope Boundaries" as the **first** section | |
| xp is self-contained (no external doc references for implementation details) | |
| Commit prefix in xp matches `P{NN}-S{NN}` pattern | |
| Every task in the sp has a corresponding detail section in the xp | |
| xp task details include files, implementation steps, and tests | |
| sp has all required sections: metadata table, Goals, Non-Goals, Tasks, Acceptance Criteria, Deliverables, Post-Sprint Notes | |

If any check fails, fix it before committing.

---

## Step 5: Commit Planning Documents

```bash
git add _specs_and_plans/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md
git add _specs_and_plans/phase_{NN}--{phase_slug}/xp_{NN}--{sprint_slug}.md
git commit -m "P{NN}-S{NN}-T00 Sprint {NN} planning: {brief description}"
```

The `T00` prefix indicates planning commits (before execution begins).

---

## Step 6: Hand Off and Approval Gate

Tell the user:

> Sprint {NN} planning is complete. Two documents committed:
>
> - Sprint spec: `_specs_and_plans/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md`
> - Execution plan: `_specs_and_plans/phase_{NN}--{phase_slug}/xp_{NN}--{sprint_slug}.md`
>
> **Next steps:**
> 1. Review both documents -- are goals correct? Tasks complete? Critical Rules sufficient?
> 2. If changes are needed, we can revise in this session or you can edit directly.
> 3. When approved, I will update the sp_ status to APPROVED and commit.
> 4. Then launch a fresh session with `--dangerously-skip-permissions` to run `workflow_execute_sprint_dev_plan.md`.

Do not begin execution in this session. The planning session ends here. The two-session separation exists because planning benefits from conversation while execution benefits from uninterrupted autonomous work.

### Set Status to APPROVED (Hard Gate for Execution)

After the user explicitly approves:

1. Update the `Status` field in the sp_ file from `PLANNING` to `APPROVED`
2. Commit the status change

```bash
git add _specs_and_plans/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md
git commit -m "P{NN}-S{NN}-T00 Approve Sprint {NN} for execution"
```

**This is the final gate before execution.** The `workflow_execute_sprint_dev_plan.md` will check for `APPROVED` status and refuse to proceed if the sp_ still shows `PLANNING`. Do NOT set this status until the user explicitly approves.

**Explicitly tell the user the exact next command to run:**

> To execute this sprint, launch a fresh Claude Code session and tell it:
>
> ```
> Read and follow _workflows/workflow_execute_sprint_dev_plan.md
> ```
>
> Do NOT tell the agent to read the xp file directly — the execution workflow handles finding the sprint, checking the APPROVED gate, reading the xp, and following the correct task-by-task process.

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_start_new_sprint.md` | Prerequisite -- creates branch and gathers context |
| `workflow_sprint_planning_collab.md` | Collab-group alternative to this solo workflow |
| `workflow_execute_sprint_dev_plan.md` | Executes the approved xp (next step after human review) |
| `workflow_sprint_code_review_solo.md` | Solo code review after execution + external reviews |
| `workflow_sprint_code_review_collab.md` | Collab-group code review (alternative to solo) |
| `workflow_sprint_closeout.md` | Sprint closing checklist (shared endpoint) |
| `workflow_new_phase.md` | Creating a new phase (prerequisite for Sprint 01) |
