# Workflow: Ideation

> Feature brainstorming and scope selection before formal sprint planning.

## Quick Reference

| Item | Value |
|------|-------|
| When to use | Large, ambiguous feature areas with many possible directions |
| Output | Ideation document (`sp_{NN}--ideation--{slug}.md`) or inline in sprint spec |
| Duration | 30-60 minutes of conversation |
| Key principle | Diverge first (no filtering), then converge (select scope) |
| Exemplar | Phase 4 Sprint 06 ideation session |

---

## Overview

Ideation is an **optional** step before formal sprint planning. Use it when the feature area is large enough that you need to brainstorm all possibilities before selecting what to build.

Most sprints do NOT need ideation. If the scope is already clear from the backlog, skip directly to `workflow_start_new_sprint.md`.

---

## When to Use Ideation

| Situation | Use Ideation? |
|-----------|--------------|
| Backlog item says "Add X" with clear requirements | No, go straight to sprint planning |
| Backlog item says "Improve the import experience" (vague) | Yes |
| Starting a new phase with broad goals | Yes |
| Multiple competing approaches to a feature | Yes (or use `workflow_research.md` first) |
| Bug fix or technical debt | No |

---

## Step-by-Step

### Step 1: Define the Feature Area

State the broad area clearly. Examples:
- "Real-time collaboration features for the issue tracker"
- "Developer experience improvements for the import pipeline"
- "Analytics and reporting capabilities"

### Step 2: Divergent Phase — Brainstorm Everything

Generate ALL possible features, enhancements, and ideas within the area. No filtering, no prioritization, no feasibility analysis. The goal is volume.

Techniques:
- **User story brainstorm:** "As a [role], I want [feature] so that [benefit]"
- **Platform comparison:** What do Linear, Jira, GitHub, Notion do in this area?
- **Pain point inventory:** What is frustrating about the current implementation?
- **Technology exploration:** What new capabilities do our dependencies enable?
- **Subagent brainstorm:** Spawn 2-3 Sonnet subagents to brainstorm independently, then merge lists

Write every idea down, even ones that seem impractical. Bad ideas often inspire good ones.

### Step 3: Organize into Tiers

Sort the brainstormed ideas into three tiers:

| Tier | Criteria | Action |
|------|----------|--------|
| **Must-Have** | Essential for the feature area to be useful; high impact, reasonable effort | Include in the upcoming sprint(s) |
| **Nice-to-Have** | Improves the feature but not essential; moderate impact | Include if time permits, or defer to next sprint |
| **Future** | Good idea but too large, too complex, or depends on infrastructure we do not have yet | Add to backlog LATER or SOMEDAY |

### Step 4: Technical Feasibility Check

For Must-Have items, do a quick feasibility assessment:
- Can we implement this with the current architecture?
- Does it require schema changes? New dependencies?
- What is the rough effort (Small / Medium / Large)?
- Are there any blockers or prerequisites?

For items where feasibility is uncertain, spawn a quick research subagent:
```
Assess the technical feasibility of implementing {feature} in this project.
Current tech stack: see `_workflows/PROJECT_IDENTITY.md` / `CLAUDE.md`.
Current architecture: {brief description of relevant subsystem}.
Output: 1 paragraph with feasibility assessment and estimated effort.
DO NOT edit any source code.
```

### Step 5: Convergent Phase — Select Sprint Scope

With the human, select which items to include in the sprint:

1. All Must-Have items form the core of the sprint
2. Nice-to-Have items are included based on estimated capacity
3. Future items go to the backlog

Discuss with the human:
- "Here are the 5 Must-Have items. Do you agree with the prioritization?"
- "We have capacity for 2-3 Nice-to-Have items. Which are most important to you?"
- "These 8 items are deferred to the backlog. Any you want to promote?"

### Step 6: Document the Ideation

Write an ideation document if the brainstorm was substantial (20+ ideas, multiple tiers):

```markdown
# Sprint {NN} Ideation: {Feature Area}

## Feature Area
{Description of the broad area explored}

## All Ideas (Brainstorm Output)

### Must-Have
1. {Idea} — {one-line description}
2. ...

### Nice-to-Have
1. {Idea} — {one-line description}
2. ...

### Future (Deferred to Backlog)
1. {Idea} — {one-line description} → {NEXT/LATER/SOMEDAY}
2. ...

## Selected Scope
{List of items selected for the sprint, with brief rationale}

## Deferred Items
{Items explicitly moved to the backlog, with horizon assignments}
```

File naming: `sp_{NN}--ideation--{slug}.md` (the `--ideation--` infix distinguishes it from the formal sprint spec).

For smaller ideation sessions, include the brainstorm directly in the sprint spec's Goals section.

### Step 7: Transition to Sprint Planning

With the scope selected, write the formal sprint spec (`sp_{NN}--{slug}.md`) and execution plan (`xp_{NN}--{slug}.md`) following `workflow_start_new_sprint.md`.

The ideation document becomes a reference artifact — it captures the ideas that were deferred and why.

---

## Tips for Effective Ideation

1. **Separate divergence from convergence.** Do not evaluate ideas while brainstorming. The critical voice kills creativity. Brainstorm first, filter second.

2. **Include the human early.** Ideation benefits from the human's domain knowledge and product intuition. This is a conversation, not a solo exercise.

3. **Time-box the brainstorm.** 15-20 minutes of divergent thinking is usually enough. Diminishing returns set in quickly.

4. **Write everything down.** Even "bad" ideas should be captured. They inform future decisions and prevent re-brainstorming.

5. **Do not over-scope.** A sprint should be completable in one execution session (1-3 hours). If the Must-Have list has more than 10 items, it is too large — split into multiple sprints.

---

## Related Workflows

- `workflow_start_new_sprint.md` — Formal sprint planning (follows ideation)
- `workflow_research.md` — Deep research for technical feasibility questions
- `workflow_roadmap_rescheduling_solo.md` — Where deferred ideas go
