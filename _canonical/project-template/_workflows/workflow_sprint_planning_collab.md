# Workflow: Sprint Planning (Collab-Group)

> Delegates to the `ensemble-collab` path. This replaces the old `workflow_new_sprint_collab.md`.

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
                               | COLLAB-GROUP       |
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

- [ ] `workflow_start_new_sprint.md` has been run (branch exists, context gathered)
- [ ] User has chosen "collab-group" as the planning path

---

## Path

This project uses the ensemble-collab path for all collab-group sessions.

Follow: [`_workflows/ensemble-collab/workflow_new_sprint_collab.md`](ensemble-collab/workflow_new_sprint_collab.md)

---

## After the Collab-Group Session

When the collab-group session completes, the main agent must verify and commit the output. The collab-group produces the same two deliverables as solo planning:

- Sprint spec (`sp_{NN}--{slug}.md`) -- what and why
- Execution plan (`xp_{NN}--{slug}.md`) -- how (self-contained)

### Verification Checklist

Run through every item before committing. Collab-group sessions sometimes produce files with naming or structural issues that must be corrected.

| Check | Pass? |
|-------|-------|
| Sprint spec filename follows `sp_{NN}--{slug}.md` pattern | |
| Execution plan filename follows `xp_{NN}--{slug}.md` pattern | |
| Both files are in the phase directory (flat), not in a subdirectory | |
| xp has "Context and Scope Boundaries" as the **first** section | |
| xp is self-contained (no external doc references for implementation details) | |
| Commit prefix in xp matches `P{NN}-S{NN}` pattern | |
| Every task in the sp has a corresponding detail section in the xp | |
| xp task details include files, implementation steps, and tests | |
| sp has all required sections: metadata table (with Phase, Sprint, Status=PLANNING, Date, Branch with `claudecode/@claude/` prefix, Commit Prefix, Predecessor), Goals, Non-Goals, Tasks table, Acceptance Criteria, Deliverables, Post-Sprint Notes placeholder | |

### Common Naming Errors to Fix

Collab-group sessions have historically produced these errors:

| Error | Fix |
|-------|-----|
| Files placed in a subdirectory (e.g., `sprint_03/sp_03--...`) instead of flat in the phase directory | Move files to `_stages_and_phases/phase_{NN}--{phase_slug}/` |
| Misnamed files (e.g., `sprint_spec_03.md` instead of `sp_03--{slug}.md`) | Rename to correct pattern |
| Missing "Context and Scope Boundaries" section in xp | Add it as the first section, before any other content |
| xp references external documents instead of inlining implementation details | Inline the referenced content |
| Branch name missing `claudecode/@claude/` prefix in metadata | Correct to `claudecode/@claude/phase{NN}-sprint{NN}` |

### Commit Planning Documents

After verification and any corrections:

```bash
git add _stages_and_phases/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md
git add _stages_and_phases/phase_{NN}--{phase_slug}/xp_{NN}--{sprint_slug}.md
git commit -m "P{NN}-S{NN}-T00 Sprint {NN} planning: {brief description}"
```

The `T00` prefix indicates planning commits (before execution begins).

### Hand Off

Tell the user:

> Sprint {NN} planning is complete. Two documents committed:
>
> - Sprint spec: `_stages_and_phases/phase_{NN}--{phase_slug}/sp_{NN}--{sprint_slug}.md`
> - Execution plan: `_stages_and_phases/phase_{NN}--{phase_slug}/xp_{NN}--{sprint_slug}.md`
>
> **Next steps:**
> 1. Review both documents -- are goals correct? Tasks complete? Critical Rules sufficient?
> 2. If changes are needed, we can revise or you can edit directly.
> 3. When approved, launch a fresh session with `--dangerously-skip-permissions` and run `workflow_execute_sprint_dev_plan.md`.

---

## When to Use Collab-Group vs Solo Planning

| Scenario | Recommendation |
|----------|---------------|
| Complex sprint with many dependencies | Collab-group |
| Straightforward continuation sprint | Solo (`workflow_sprint_planning_solo.md`) |
| New phase Sprint 01 (scope definition) | Collab-group |
| Research or documentation sprint | Solo |
| Sprint touches unfamiliar subsystems | Collab-group |
| Architectural changes requiring adversarial review | Collab-group |

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_start_new_sprint.md` | Prerequisite -- creates branch and gathers context |
| `workflow_sprint_planning_solo.md` | Solo alternative to this collab-group workflow |
| `workflow_execute_sprint_dev_plan.md` | Executes the approved xp (next step after human review) |
| `workflow_sprint_code_review_solo.md` | Solo code review after execution + external reviews |
| `workflow_sprint_code_review_collab.md` | Collab-group code review (alternative to solo) |
| `workflow_sprint_closeout.md` | Sprint closing checklist (shared endpoint) |
