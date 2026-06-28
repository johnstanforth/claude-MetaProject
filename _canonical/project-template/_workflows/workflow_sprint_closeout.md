# Workflow: Sprint Closeout

> The single authoritative checklist for closing a sprint, regardless of how it was planned or reviewed. Both the solo sprint workflow and any future collab-group sprint workflow converge here.

## Quick Reference

| Item | Value |
|------|-------|
| Applies to | The main Claude agent (or human) closing out a sprint |
| When to run | After sprint execution AND code review/audit (if any) are both concluded |
| Inputs | Sprint sp doc with post-sprint notes, code review summary (if any) |
| Outputs | Updated sp, phase README, backlog, CLAUDE.md |

---

## 1. Prerequisite: Code Review Must Be Done First

**STOP.** Before running this closeout workflow, confirm that the code audit has been conducted for this sprint (or that the user has explicitly decided to skip it). The correct post-execution sequence is:

1. Sprint execution completes (all tasks committed)
2. Code audit (`workflow_code_audit.md`) with fixes applied
3. **This workflow** -- sprint closeout

If the code audit has not been run yet, **ask the user** before proceeding. Do not start updating docs, ROADMAP, or sprint status until review fixes are committed.

---

## 2. Overview

Every sprint ends with the same closeout steps, whether the sprint was:
- Planned by the main agent + user directly (`workflow_start_new_sprint.md`)
- Planned by a future collab-group workflow
- Reviewed via code audit (`workflow_code_audit.md`)

This workflow is the shared endpoint. All planning and review paths should direct the main agent here after their respective work concludes.

---

## 3. Checklist

Run through every item. Do not skip steps -- each one has been added because skipping it caused a real problem in a past sprint.

### Step 1: Verify Tests Pass -- ZERO FAILURES REQUIRED

```bash
uv run pytest tests/ -v
uv run ruff check .
```

**HARD GATE: BOTH must pass with ZERO failures.** There is no such thing as a "pre-existing failure." If any test fails or any ruff check fails, it must be fixed before the sprint can close -- even if the failure appears unrelated to this sprint's changes. Every sprint must leave the validation suite fully green.

If fixing a failure requires decisions beyond your authority, STOP and report the blocker to the human/user/project owner. Do NOT close out a sprint with known test failures.

**Note:** The two checks above (`pytest` and `ruff`) are the complete validation suite for this project. Every sprint must leave both green with zero failures. (mypy is optional in this build-line — if the project later opts into type-checking, add `uv run mypy src/` here as a third gate.)

### Step 2: Update Sprint Status

In the sprint spec (`sp_{NN}--{slug}.md`), update the metadata table:

```markdown
| Status | COMPLETE |
| Completed | {YYYY-MM-DD} |
```

### Step 3: Verify Post-Sprint Notes

The sprint spec must have post-sprint notes covering:
- Summary of what was accomplished
- Test metrics (before/after counts)
- Any deviations from the plan
- Reference to code audit summary (if a code audit was conducted)

If notes are missing or incomplete, add them now.

### Step 4: Update Phase README

Update the sprint table in the phase's `README.md`:

```markdown
| Sprint | Title | Status | Branch |
|--------|-------|--------|--------|
| 01 | {Title} | COMPLETE | `claudecode/@claude/phase{NN}-sprint01` |
```

If Sprint N+1 scope is already known, add a PLANNING row for it.

### Step 5: Update ROADMAP.md

Update `_stages_and_phases/ROADMAP.md` to reflect progress from the just-completed sprint. ROADMAP.md is the authoritative forward-looking record for the project.

Check and update:
- **Project Status Summary table** -- current phase, test count, sprints completed
- **Completed Phases section** -- if a phase was concluded, update its sprint table and outcome
- **Current Phase section** -- update sprint status, add new sprint rows if planning has started
- **Backlog summary** -- adjust if items were resolved or new items emerged

This step ensures ROADMAP.md stays current with every sprint, not just during periodic roadmap rescheduling runs.

### Step 6: Triage Follow-Up Items

Every item in the sprint spec's Follow-Up section must be triaged to exactly one destination:

| Destination | File to Update | When |
|-------------|---------------|------|
| Next sprint | Note for Sprint N+1 planning | High priority, directly related |
| Unsorted Queue | `_backlog/_UNSORTED_QUEUE.md` | Needs prioritization in next rescheduling |
| Backlog NEXT | `_backlog/_horizon_NEXT.md` | Important, fits in this phase, clearly NEXT |
| Backlog LATER | `_backlog/_horizon_LATER.md` | Good idea, not this phase |
| Backlog SOMEDAY | `_backlog/_horizon_SOMEDAY.md` | Aspirational |
| ADR | Phase's `DECISIONS.md` | Architectural decision to record |

When unsure which horizon an item belongs to, put it in the UNSORTED_QUEUE. The roadmap rescheduling workflow (`workflow_roadmap_rescheduling_solo.md`) will sort it properly.

If a code audit produced deferred items (in the review summary), those must also be triaged here. Do not leave any follow-up or deferred item without a home.

### Step 7: Update CLAUDE.md (if needed)

Check whether the sprint changed anything that CLAUDE.md documents:

| Change | CLAUDE.md Section to Update |
|--------|----------------------------|
| New development phase started or phase status changed | Development Phases table |
| New API endpoint added | API Endpoints Overview |
| New model or table added | Database Schema |
| New service module added | Project Structure |
| New workflow added | Development Phases & Stages (workflow reference) |
| Convention changed | Conventions section |
| New dependency added | Tech Stack |
| New known issue discovered | Known Issues / Gotchas |

See `workflow_claude_md_maintenance.md` for the full section-by-section checklist.

### Step 8: Compound Engineering Review

Follow **Stage B (Lessons Capture)** of [`workflow_compound_engineering.md`](workflow_compound_engineering.md). This is the primary Compound Engineering integration point — not a lightweight checklist but a systematic process for extracting lessons and converting them into durable artifacts.

**Summary of what Stage B requires:**

1. Review the sprint's xp, post-sprint notes, code review summary, and git log
2. Answer the five Compound questions (C1-C5): patterns emerged, harder than expected, what to tell the next agent, process friction, infrastructure improved
3. Decide each finding's destination: CLAUDE.md, workflow doc, techstack doc, backlog, code, or this workflow's appendix
4. Write "Compound Engineering Findings" in the sp file's post-sprint notes
5. **Apply findings immediately** — update CLAUDE.md, workflow docs, and techstack docs during this closeout session, not later

Read the full Stage B process in `workflow_compound_engineering.md` § Stage B before proceeding. Do not substitute a lighter-weight version — the systematic process is what makes improvements compound.

### Step 9: Verify Clean Working Tree

```bash
git status
```

Must show `nothing to commit, working tree clean`. If there are uncommitted changes from the closeout process, commit them:

```bash
git add <files>
git commit -m "P{NN}-S{NN} Sprint closeout: status, README, follow-up triage"
```

### Step 10: Report to User

Summarize to the user:
- Sprint status updated to COMPLETE
- Phase README updated
- ROADMAP.md updated
- Follow-up items triaged (list destinations)
- CLAUDE.md updated (if applicable)
- Clean working tree confirmed
- Sprint is ready for the next phase of work

### Step 11: Chain to Next Step

After reporting, **ask the user** what they'd like to do next:

- **"Should we run roadmap rescheduling before the next sprint?"**
  - Suggest this especially if: NEXT horizon is thinning, the phase has run 4+ sprints, or the UNSORTED_QUEUE has accumulated items.
- **"Ready for the next sprint? Solo planning?"**
  - If the user wants to proceed directly to planning.
- **"Should we start a new phase?"**
  - If the rescheduling workflow recommended PHASE TRANSITION, or if the user indicates the phase is wrapping up.

Do not assume which path -- always ask.

---

## 4. Copy-Paste Checklist

For quick use during closeout:

```markdown
## Sprint {NN} Closeout

- [ ] Tests pass (`uv run pytest tests/ -v`)
- [ ] Lint passes (`uv run ruff check .`)
- [ ] Sprint status updated to COMPLETE with date
- [ ] Post-sprint notes verified (summary, metrics, deviations, review reference)
- [ ] Phase README sprint table updated
- [ ] ROADMAP.md updated (status summary, phase progress, test count)
- [ ] All follow-up items triaged (every item has a destination)
- [ ] All code audit deferred items triaged (if audit was conducted)
- [ ] CLAUDE.md updated (if sprint changed documented items)
- [ ] Compound Engineering assessment noted
- [ ] Working tree is clean
- [ ] Reported to user
```

---

## 5. Relationship to Other Workflows

```
workflow_start_new_sprint.md              ---> Sprint Execution ---> Code Audit ---> THIS FILE
(future collab-group sprint workflow)    ---> Sprint Execution ---> Code Audit ---> THIS FILE

THIS FILE ---> Next sprint planning (workflow_start_new_sprint.md)
           ---> Roadmap rescheduling (workflow_roadmap_rescheduling_solo.md)
           ---> New phase (workflow_new_phase.md)
```

All sprint planning and review paths converge on this closeout workflow. After closeout, the project is ready for the next sprint planning cycle.
