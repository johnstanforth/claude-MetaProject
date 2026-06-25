# Workflow: New Phase

> How to create and initialize a new development phase for this project.

## Quick Reference

| Item | Value |
|------|-------|
| Phase directory | `_specs_and_plans/phase_{NN}--{slug}/` |
| Required files | `README.md`, `DECISIONS.md` |
| Templates | `_workflows/_templates/PHASE_README_TEMPLATE.md`, `DECISION_TEMPLATE.md` |
| First branch | `claudecode/@claude/phase{NN}-sprint01` |
| Key input | Backlog horizons, previous phase retrospective |

---

## Overview

A **phase** is a thematic grouping of sprints that share a common goal. Phases typically span 3-12 sprints and focus on a single major initiative (e.g., "Gmail Ingestion," "Listing Discovery UI," "Valuation Overlays").

Starting a new phase **automatically starts Sprint 01** of that phase. The phase infrastructure (directory, README, DECISIONS.md) and Sprint 01 planning documents are the first commits on the Sprint 01 branch.

---

## When to Start a New Phase

Start a new phase when:
- The previous phase is complete (all sprints done, retrospective written)
- The next body of work has a different theme or goal than the current phase
- The backlog has accumulated enough related items to justify a dedicated phase

Do NOT start a new phase for:
- A single sprint of work (just add it to the current phase)
- Unrelated small fixes (use `workflow_quick_fix.md`)
- Research that may or may not lead to implementation (use `workflow_research.md` first)

---

## Step-by-Step

### Step 1: Review and Discuss Scope

Before creating any files, discuss with the human:

1. **Read the backlog:**
   - `_specs_and_plans/_backlog/_horizon_NEXT.md` — items ready for implementation
   - `_specs_and_plans/_backlog/_horizon_LATER.md` — items that may be ready to graduate
   - `_specs_and_plans/_backlog/_horizon_SOMEDAY.md` — aspirational items to consider

2. **Read the previous phase retrospective** (post-sprint notes from the final sprint)

3. **Run Compound Engineering Phase Retrospective.** Follow **Stage C** of [`workflow_compound_engineering.md`](workflow_compound_engineering.md): read all Compound Engineering Findings sections from the phase's sprint sp files, identify cross-sprint patterns, produce a "Phase Compound Summary" in the phase README, and assess where we are on the Adoption Ladder. This is a 10-15 minute review that surfaces systemic issues and validates that the phase's infrastructure investments paid off.

4. **Discuss with the human:**
   - What is the primary goal of this phase?
   - What backlog items should be included?
   - What is explicitly out of scope?
   - How many sprints do we estimate? (Rough guess is fine; phases can grow)
   - Are there any dependencies or prerequisites?

### Step 2: Choose Phase Number and Slug

- Phase number: next sequential number (zero-padded two digits)
- Slug: lowercase, hyphen-separated, descriptive of the phase theme

Examples (illustrative):
| Phase | Slug | Full Directory Name |
|-------|------|-------------------|
| 00 | `ideation_and_research` | `phase_00--ideation_and_research` |
| 01 | `gmail_ingestion` | `phase_01--gmail_ingestion` |
| 02 | `listing_discovery_ui` | `phase_02--listing_discovery_ui` |
| 03 | `valuation_overlays` | `phase_03--valuation_overlays` |
| 04 | `fractional_co_purchase` | `phase_04--fractional_co_purchase` |

Note: slugs use underscores (not hyphens) to match the directory naming convention (Phase 00 above).

### Step 3: Create Phase Directory

```bash
mkdir -p _specs_and_plans/phase_{NN}--{slug}/
```

### Step 4: Create Phase README

Create `_specs_and_plans/phase_{NN}--{slug}/README.md` using the template at `_workflows/_templates/PHASE_README_TEMPLATE.md`.

The README must include:

```markdown
# Phase {N}: {Title}

## Overview

{2-3 paragraphs describing the phase goal, motivation, and expected outcomes.}

## Scope

### In Scope
- {Bulleted list of what this phase covers}

### Out of Scope
- {Bulleted list of what this phase explicitly does NOT cover}

## Sprint Plan

| Sprint | Title | Status | Branch |
|--------|-------|--------|--------|
| 01 | {Title} | PLANNING | `claudecode/@claude/phase{NN}-sprint01` |

## Key Decisions

See `DECISIONS.md` for architectural decision records (ADRs).

## References

- {Links to relevant research, backlog items, external docs}
```

### Step 5: Create DECISIONS.md

Create `_specs_and_plans/phase_{NN}--{slug}/DECISIONS.md` using the template at `_workflows/_templates/DECISION_TEMPLATE.md`.

This file will accumulate ADRs as the phase progresses. Start with a header:

```markdown
# Phase {N} Decisions

Architectural Decision Records for Phase {N}: {Title}.

## ADR Index

| ID | Title | Status | Date |
|----|-------|--------|------|
| (none yet) | | | |

---

(ADRs will be added below as decisions are made during sprint execution.)
```

### Step 6: Create Sprint 01 Branch

```bash
# Branch from main or the last sprint of the previous phase
git checkout main  # or: git checkout claudecode/@claude/phase{NN-1}-sprint{LAST}
git checkout -b claudecode/@claude/phase{NN}-sprint01
```

### Step 7: Check UNSORTED_QUEUE and Consider Roadmap Rescheduling

Before proceeding to Sprint 01 planning, check the UNSORTED_QUEUE item count:

```bash
# Count items in the UNSORTED_QUEUE
grep -c '^- ' _specs_and_plans/_backlog/_UNSORTED_QUEUE.md || echo "0 items"
```

**Ask the user:** "The UNSORTED_QUEUE currently has N items. Starting a new phase is a natural point for roadmap rescheduling. Would you like to run a rescheduling session first? If so, collab-group or solo?"

- If collab-group: run `workflow_roadmap_rescheduling_collab.md`
- If solo: run `workflow_roadmap_rescheduling_solo.md`
- If skip: proceed directly to sprint planning

### Step 8: Follow Sprint Planning Workflow

**Ask the user:** "Ready for Sprint 01 planning. Should we use a collab-group (Codex + Claude discuss and plan) or solo (I plan directly with you)?"

- If collab-group: continue with `workflow_sprint_planning_collab.md`
- If solo: continue with `workflow_sprint_planning_solo.md`

The phase infrastructure and Sprint 01 planning documents are committed together:

```bash
git add _specs_and_plans/phase_{NN}--{slug}/README.md
git add _specs_and_plans/phase_{NN}--{slug}/DECISIONS.md
git add _specs_and_plans/phase_{NN}--{slug}/sp_01--{sprint_slug}.md
git add _specs_and_plans/phase_{NN}--{slug}/xp_01--{sprint_slug}.md
git commit -m "P{NN}-S01-T00 Phase {NN} infrastructure and Sprint 01 planning"
```

### Step 9: Update Top-Level README

Update `_specs_and_plans/README.md` to include the new phase in the phase table. Commit this as part of the planning commit or as a separate follow-up.

---

## Phase Lifecycle

| Status | Meaning |
|--------|---------|
| PLANNING | Phase directory created, scope being defined |
| ACTIVE | At least one sprint in progress or complete |
| COMPLETE | All planned sprints done, retrospective written |
| PAUSED | Work suspended, may resume later |

---

## Related Workflows

- `workflow_sprint_planning_solo.md` — Sprint planning within a phase (always follows phase creation)
- `workflow_sprint_planning_collab.md` — Sprint planning via collab-group (alternative to solo)
- `workflow_roadmap_rescheduling_collab.md` / `workflow_roadmap_rescheduling_solo.md` — Holistic backlog and roadmap review (recommended at phase boundaries)
- `workflow_research.md` — Research that informs phase planning
