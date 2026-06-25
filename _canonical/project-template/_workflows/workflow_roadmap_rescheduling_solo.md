# Workflow: Roadmap Rescheduling (Solo)

> The main Claude agent works directly with the human to reprioritize the backlog and update the roadmap, without launching a collab-group session.

## Quick Reference

| Item | Value |
|------|-------|
| Applies to | The main Claude agent working directly with the human |
| Input files | UNSORTED_QUEUE, NEXT, LATER, SOMEDAY, ROADMAP.md, phase READMEs |
| Output files | Updated UNSORTED_QUEUE (emptied), NEXT, LATER, SOMEDAY, ROADMAP.md |

---

## 1. Overview

This is the solo roadmap rescheduling workflow for this project. The main Claude agent performs the analysis and proposes changes directly to the human for approval.

**Use this when** the human decides a solo pass is appropriate for the current situation. The human always decides when to run rescheduling and which variant to use.

**Goals:**
- Empty the UNSORTED_QUEUE by sorting every item into the correct horizon
- Re-evaluate existing horizon items for promotion or demotion
- Identify items that have been implemented and should be archived
- Update ROADMAP.md to reflect the current state and forward plan
- Annotate natural clusters of related items (without producing sprint specs)

---

## 2. Step-by-Step

### Step 1: Gather and Read Context

Read all context files before analysis:

1. `CLAUDE.md` -- current project state, tech stack, architecture
2. `_specs_and_plans/ROADMAP.md` -- forward plan
3. Current phase README -- sprint history and status
4. Most recent sprint `sp_` doc -- follow-ups and outcomes
5. All four backlog files:
   - `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md`
   - `_specs_and_plans/_backlog/_horizon_NEXT.md`
   - `_specs_and_plans/_backlog/_horizon_LATER.md`
   - `_specs_and_plans/_backlog/_horizon_SOMEDAY.md`

Report to the user: "UNSORTED_QUEUE has N items. NEXT has N items. LATER has N items. SOMEDAY has N items. Here's what I found..."

### Step 2: Phase Health Check

Before sorting items, assess the current phase:
- Read the current Phase README goals/scope section
- Read the phase progress and completion criteria in ROADMAP.md
- Compare stated goals against delivered outcomes

Present to the user with one of three verdicts:
- **ACTIVE** -- significant work remains aligned with this phase's goals
- **WINDING DOWN** -- remaining items are thin; 1-2 more sprints at most
- **RECOMMEND TRANSITION** -- phase goals are substantially met; recommend planning the next phase

Record the verdict -- it will be written into ROADMAP.md as a timestamped phase assessment note.

### Step 3: Identify Implemented Items

Cross-reference backlog items against completed sprints:
- Check CLAUDE.md phase/sprint history
- Check phase README sprint tables
- Check recent sprint sp_ post-sprint notes

Present to the user: "These N items appear to be already implemented: {list}. Should I archive them?"

### Step 4: Sort UNSORTED_QUEUE

For each item in the queue, propose a horizon:

```
UNSORTED_QUEUE -> Proposed sorting:

NEXT:
- {Item A} -- Reason: directly relevant to current phase, clear implementation path
- {Item B} -- Reason: small scope, no dependencies

LATER:
- {Item C} -- Reason: needs design work, depends on Item A
- {Item D} -- Reason: valuable but not current focus

SOMEDAY:
- {Item E} -- Reason: aspirational, no clear timeline

Do you agree with this sorting?
```

Wait for the user to approve, adjust, or discuss.

### Step 5: Re-evaluate Existing Horizon Items

Review items already on NEXT, LATER, SOMEDAY:
- Propose promotions (LATER -> NEXT) with reasoning
- Propose demotions (NEXT -> LATER) with reasoning
- Flag stale items for archival

Present proposed changes and wait for approval.

### Step 6: Annotate Natural Clusters

Note items that group together naturally:
```
These items cluster together and could form a natural sprint:
- Item A, Item B, Item C -- all relate to entity model migrations
```

Do NOT produce formal sprint specs. Just annotate the clustering. This informs future sprint planning but does not commit to scope.

### Step 7: Refresh Planned Phases in ROADMAP.md

Review the Planned Phases section in ROADMAP.md:
- Are descriptions still accurate?
- Did current-phase work change what the next phase should focus on?
- Do phase completion criteria need updating?

Present proposed changes and wait for approval.

### Step 8: Update Files

After the user approves all changes:

1. Empty the UNSORTED_QUEUE (move items to horizons or archive)
2. Update NEXT, LATER, SOMEDAY with moves, promotions, demotions
3. Add "Previous Items with Disposition" entries for archived items
4. Update ROADMAP.md to reflect current state (including phase assessment note and refreshed planned phases)

### Step 9: Commit Atomically

```bash
git add _specs_and_plans/_backlog/ _specs_and_plans/ROADMAP.md
git commit -m "Roadmap rescheduling (solo): {N} items sorted, {N} archived, ROADMAP updated"
```

---

### After Rescheduling

**Ask the user** what they'd like to do next:

- **"Ready for sprint planning?"**
  - If the user wants to proceed directly to the next sprint via `workflow_start_new_sprint.md`.
- **"Should we start a new phase first?"**
  - If the phase health check recommended TRANSITION.

Do not assume which path -- always ask.

---

## 3. Relationship to Other Workflows

```
workflow_sprint_closeout.md  ---> THIS FILE (when UNSORTED_QUEUE has accumulated items)
THIS FILE                    ---> workflow_start_new_sprint.md (sprint planning)
                             ---> workflow_new_phase.md (if phase transition recommended)
```

This workflow replaces the earlier `workflow_backlog_triage.md` as the authoritative process for re-evaluating the backlog. See the backlog files themselves for horizon definitions and conventions.
