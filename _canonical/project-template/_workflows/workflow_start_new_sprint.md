# Workflow: Start New Sprint

> Shared entry point for every sprint. Creates the branch, gathers context, and hands off to the appropriate planning workflow. Every sprint begins here.

## Quick Reference

| Item | Value |
|------|-------|
| Branch naming | `claudecode/@claude/phase{NN}-sprint{NN}` |
| Commit prefix | `P{NN}-S{NN}-T{NN} Description` |
| Sprint spec | `sp_{NN}--{slug}.md` (what and why) |
| Execution plan | `xp_{NN}--{slug}.md` (how, self-contained) |
| Planning workflows | `workflow_sprint_planning_solo.md` or `workflow_sprint_planning_collab.md` |
| Technology | Python 3.12+ library (uv; SQLite WAL archival storage); code-primary |
| Validation suite | `uv run pytest tests/ -v` + `uv run ruff check .` |

---

## Pipeline Position

```
                          YOU ARE HERE
                               |
                               v
  +-----------------------+    +--------------------+    +--------------+
  | workflow_new_phase.md |--->| START NEW SPRINT   |--->| Planning     |
  | (Phase 01 only)       |    | (this workflow)    |    | (solo or     |
  +-----------------------+    +--------------------+    |  collab)     |
                                                         +--------------+
                                                               |
                                                               v
                                                         +--------------+
                                                         | Human Review |
                                                         | (async)      |
                                                         +--------------+
                                                               |
                                                               v
                                                    +-------------------------+
                                                    | execute_sprint_dev_plan |
                                                    | (autonomous)            |
                                                    +-------------------------+
                                                               |
                                                               v
                                                    +-------------------------+
                                                    | External Reviews        |
                                                    | (Gemini, Cursor, etc.)  |
                                                    +-------------------------+
                                                               |
                                                               v
                                                    +-------------------------+
                                                    | sprint_code_review      |
                                                    | (solo or collab)        |
                                                    +-------------------------+
                                                               |
                                                               v
                                                    +-------------------------+
                                                    | workflow_sprint_closeout |
                                                    +-------------------------+
```

---

## Step 1: Determine Sprint Context

Before creating any branch or files, gather the context needed to plan effectively.

### Is this a new phase?

If yes, follow `workflow_new_phase.md` first. That workflow creates the phase directory, README, and DECISIONS.md, then returns here for Sprint 01 planning. Starting a new phase automatically means starting Sprint 01 of that phase.

### Continuing an existing phase?

Read the following, in this order:

1. **`CLAUDE.md`** -- project conventions, architecture, tech stack, current state
2. **Phase README** (`_specs_and_plans/phase_{NN}--{slug}/README.md`) -- phase goals, sprint table, what is done and what remains
3. **Previous sprint's `sp_` doc** -- post-sprint notes, follow-up items, lessons learned, deviations
4. **Backlog NEXT horizon** (`_specs_and_plans/_backlog/_horizon_NEXT.md`) -- items ready for implementation, tagged for this phase
5. **Phase DECISIONS.md** -- any ADRs that constrain upcoming work
6. **UNSORTED_QUEUE** (`_specs_and_plans/_backlog/_UNSORTED_QUEUE.md`) -- recently triaged items that may be relevant

### Key questions to answer before proceeding:

- What is the primary goal of this sprint?
- What follow-up items from the previous sprint must be addressed?
- Are there backlog items tagged for this phase that should be pulled in?
- Are there dependencies on external systems, human actions, or other sprints?
- Is this a feature sprint, hardening sprint, research sprint, or documentation sprint?

---

## Step 2: Determine Sprint Number

Scan the phase directory for the highest existing sprint number:

```bash
ls _specs_and_plans/phase_{NN}--{slug}/sp_*.md 2>/dev/null | sort | tail -1
```

The new sprint number is the highest existing sprint number + 1, zero-padded to two digits.

If no sprint specs exist yet (Sprint 01 of a new phase), use `01`.

Also verify the branch listing to confirm no orphaned branches exist:

```bash
git branch --list "claudecode/@claude/phase{NN}-sprint*" | sort | tail -3
```

The sprint number in the branch must match the sprint number in the spec file.

---

## Step 3: Create Sprint Branch

### Branching from previous sprint in the same phase:

```bash
git checkout claudecode/@claude/phase{NN}-sprint{PREV}
git checkout -b claudecode/@claude/phase{NN}-sprint{NN}
```

### Branching for Sprint 01 of a new phase:

```bash
# From main or the last sprint of the previous phase
git checkout main  # or: git checkout claudecode/@claude/phase{PREV_NN}-sprint{LAST}
git checkout -b claudecode/@claude/phase{NN}-sprint01
```

### Branch Naming Rules

| Rule | Detail |
|------|--------|
| Pattern | `claudecode/@claude/phase{NN}-sprint{NN}` |
| Prefix | `claudecode/@claude/` -- identifies Claude Code sessions |
| Phase number | Two-digit zero-padded (e.g., `phase05`) |
| Sprint number | Two-digit zero-padded (e.g., `sprint03`) |
| Linear chain | Each sprint branches from the previous sprint's tip |
| No rebase | Never rebase sprint branches onto main mid-phase |
| No force-push | Never force-push sprint branches |

---

## Step 4: Hand Off to Planning

With the branch created and context gathered, hand off to the appropriate planning workflow.

**Ask the user:**

> "Branch `claudecode/@claude/phase{NN}-sprint{NN}` is ready. Plan this sprint via **solo** (I plan directly with you) or **collab-group** (Codex + Claude discuss and plan)?"

### Solo planning

Follow: [`workflow_sprint_planning_solo.md`](workflow_sprint_planning_solo.md)

Best for:
- Straightforward continuation sprints
- Research or documentation sprints
- Small-scope sprints (under 8 tasks)

### Collab-group planning

Follow: [`workflow_sprint_planning_collab.md`](workflow_sprint_planning_collab.md)

Best for:
- Complex sprints with many dependencies
- New phase Sprint 01 (scope definition)
- Sprints touching unfamiliar subsystems
- Architectural changes requiring adversarial review

---

## After Planning Completes

Planning produces two committed documents:

1. **Sprint spec (`sp_{NN}--{slug}.md`)** -- what the sprint accomplishes and why. Includes the paste prompt for the execution session.
2. **Execution plan (`xp_{NN}--{slug}.md`)** -- how each task is implemented. Self-contained: a fresh agent can execute the sprint by reading only this file.

Both are committed with the `P{NN}-S{NN}-T00` prefix (planning commit).

### Human review (mandatory)

The human reviews both documents before execution begins:

- Are the goals correct? Scope appropriate?
- Are the tasks complete? Dependencies ordered correctly?
- Are Critical Rules sufficient?
- Is the risk assessment realistic?
- Are there any [Human]-tagged tasks that require action before execution?

If changes are needed, revise the documents and commit the updates. The plan is not approved until the human says so.

### Execution

Once the human approves, proceed to [`workflow_execute_sprint_dev_plan.md`](workflow_execute_sprint_dev_plan.md). This is typically run in a fresh agent session with `--dangerously-skip-permissions` for autonomous execution.

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_new_phase.md` | Prerequisite for Sprint 01 of a new phase |
| `workflow_sprint_planning_solo.md` | Solo planning path (produces sp + xp) |
| `workflow_sprint_planning_collab.md` | Collab-group planning path (produces sp + xp) |
| `workflow_execute_sprint_dev_plan.md` | Autonomous execution of an approved xp |
| `workflow_sprint_code_review_solo.md` | Solo code review after execution + external reviews |
| `workflow_sprint_code_review_collab.md` | Collab-group code review (alternative to solo) |
| `workflow_sprint_closeout.md` | Sprint closing checklist (shared endpoint) |
| `workflow_roadmap_rescheduling_solo.md` | Holistic backlog and roadmap review between sprints |
