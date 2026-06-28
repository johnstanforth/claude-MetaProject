# Workflow: Sprint Code Review (Collab-Group)

> Delegates to the `ensemble-collab` path. This replaces the old `workflow_collab_group_code_review.md`. Includes critical guidance on the anti-anchoring template design.

## Pipeline Position

```
  +-------------------+    +-----------+    +--------------+    +-------------------+
  | start_new_sprint  |--->| Planning  |--->| Human Review |--->| execute_sprint    |
  +-------------------+    +-----------+    +--------------+    | _dev_plan         |
                                                                +-------------------+
                                                                       |
                                                                       v
                                                                +-------------------+
                                                                | External Reviews  |
                                                                | (Gemini, Cursor,  |
                                                                |  KimiK25, etc.)   |
                                                                +-------------------+
                                                                       |
                                                                       v
                                                                 YOU ARE HERE
                                                                       |
                                                                       v
                                                                +-------------------+
                                                                | SPRINT CODE       |
                                                                | REVIEW (COLLAB)   |
                                                                | (this workflow)   |
                                                                +-------------------+
                                                                       |
                                                                       v
                                                                +-------------------+
                                                                | sprint_closeout   |
                                                                +-------------------+
```

---

## Prerequisites

Before launching the code review collab-group, ALL of the following must be true:

- [ ] Sprint execution is complete (`workflow_execute_sprint_dev_plan.md` finished)
- [ ] All sprint tasks are committed with `P{NN}-S{NN}-T{NN}` prefixes
- [ ] Post-sprint notes have been added to the sp file
- [ ] External review prompt was generated and sent to reviewers
- [ ] External review files are present in the phase directory (`REVIEW--{AgentName}-P{NN}-S{NN}.md`)
- [ ] Validation suite passes: `uv run pytest tests/ -v` + `uv run ruff check .`

---

## Path

This project uses the ensemble-collab path for all collab-group sessions.

Follow: [`_workflows/ensemble-collab/workflow_collab_group_code_review.md`](ensemble-collab/workflow_collab_group_code_review.md)

---

## Common Rules

These rules are **hard requirements** that the ensemble-collab variant enforces.

### Fix Everything Possible

**HARD REQUIREMENT:** Fix ALL findings -- Critical, Major, Minor, AND Observations. Every item identified during the three-phase review process must be addressed with a concrete code change. The only acceptable reason to defer a finding is if fixing it would widen the change into a different sprint's scope (e.g., the fix requires a new migration, a new API endpoint, or touches an unrelated subsystem). Deferred items must be written to the backlog with an explicit reference to the finding ID.

### Zero Test Failures

**HARD GATE:** The full validation suite must pass before the session is considered complete:

```bash
uv run pytest tests/ -v
uv run ruff check .
```

"There is no such thing as a pre-existing failure." If a test was failing before the review started, it must be fixed during the review or explicitly marked as an approved `xfail` in the initial prompt. The session does not end until both commands exit cleanly.

**Exception:** Approved xfails listed in the initial collab-group prompt are acceptable. These must be enumerated by test name, not by category or glob.

### External Review Prompt Is Already Generated

The `workflow_execute_sprint_dev_plan.md` step generates the external review prompt as its final action. By the time you reach this workflow, the review prompt has already been sent, external reviewers have responded, and their review files are in the phase directory. You do not need to generate the review prompt -- just confirm the review files are present.

---

## HARD GATE: Use the Template

**MUST** use `_workflows/_templates/COLLAB_PROMPT_CODE_REVIEW.md` to construct the collab-group prompt. Do NOT write ad-hoc prompts. This is a hard gate, not a suggestion.

### Why This Is a Hard Gate

The template implements a **three-phase anti-anchoring design** that is critical to the quality of the review. Ad-hoc prompts consistently defeat this design by accidentally exposing external reviews too early. The three phases:

#### Phase 1: Independent Review

Both agents read the implementation code and form their OWN findings BEFORE reading any external reviews. The prompt MUST say "Do NOT read external reviews yet." This ensures the collab-group develops an independent perspective rather than merely validating or rubber-stamping external opinions.

The template's `MANDATORY READING` section deliberately lists implementation files and test files but explicitly states:

> "NOTE: Do NOT read any external review reports (REVIEW--*-sprint_*.md) yet. You will read them in Phase 2 AFTER forming your own independent assessment in Phase 1. This prevents anchoring bias from external reviewers' opinions."

#### Phase 2: External Review Analysis

NOW the agents read the external review reports. They evaluate each external finding against their own consensus from Phase 1:
- **AGREE** -- the finding is valid, add to shared findings list
- **DISAGREE** -- the finding is invalid, state why
- **PARTIALLY AGREE** -- the issue is real but the recommended fix is wrong

This phase also produces an **External Reviewer Report Card** evaluating each external reviewer's accuracy -- hits, misses, and false positives.

#### Phase 3: Fixes

The LEAD agent directs the WORKER agent to make specific code edits based on the consolidated findings from Phases 1 and 2. Validation runs after each change. The full suite must pass before the session ends.

### Why Ad-Hoc Prompts Defeat Anti-Anchoring

The most common failure mode: an ad-hoc prompt lists the external review files in the "mandatory reading" section alongside the implementation files. This causes agents to read external reviews immediately, collapsing Phases 1 and 2 into a single pass. The agents anchor on the external reviewers' framing and lose the ability to form independent assessments. Findings the external reviewers missed go undetected because the agents are primed to look for what the external reviewers found.

The template prevents this by:
1. Listing external review file paths in a SEPARATE section with an explicit "do NOT read yet" instruction
2. Structuring the three phases with clear boundaries
3. Requiring Phase 1 consensus to be WRITTEN to the review summary file before Phase 2 begins

**If you find yourself thinking "I'll just write a quick prompt instead of using the template" -- stop.** Use the template. Fill in the placeholders. The template exists because multiple collab-group sessions failed before it was created.

---

## 3-Minute Steering Reminder — SUSPENDED (2026-05-03)

The automated 3-minute steering reminder is **suspended**. The main agent MUST NOT send it automatically.

**Why suspended:** On 2026-05-02, the automated steer caused runaway token consumption — agents re-read files, restarted discussions, and generated enormous volumes of redundant output. This burned through weekly usage limits and made sessions unaffordable. The steer message itself is still valuable for encouraging genuine debate, but must be sent **manually by the project owner** via the tmux monitor pane at an appropriate moment. See `workflow_collab_group_launch.md` for the manual steer text to print for the project owner.

**Future:** We will revisit automated steering once we can redesign the delivery mechanism or find a less disruptive formulation.

---

## After the Collab-Group Session

When the collab-group session completes, verify the output:

### Verification Checklist

| Check | Pass? |
|-------|-------|
| Review summary exists: `REVIEW-SUMMARY--P{NN}-S{NN}.md` | |
| Review summary has Phase 1 independent findings section | |
| Review summary has Phase 2 external review analysis section | |
| Review summary has External Reviewer Report Card section | |
| Review summary has consolidated findings list | |
| All fix commits use `P{NN}-S{NN} Review fix: {description}` format | |
| Full validation passes: `uv run pytest tests/ -v` | |
| Full validation passes: `uv run ruff check .` | |

### Hand Off

Report to the user:

> Sprint {NN} collab-group code review complete.
>
> Findings: {N} total
>   - Fixed: {N} (Critical: {N}, Major: {N}, Minor: {N}, Observations: {N})
>   - Deferred: {N} (see review summary for details)
>   - Disagreed: {N}
>
> Validation: pytest PASS | ruff PASS
>
> Review summary saved to:
>   `_stages_and_phases/phase_{NN}--{phase_slug}/REVIEW-SUMMARY--P{NN}-S{NN}.md`
>
> Next step:
>   Run `workflow_sprint_closeout.md` to close out the sprint.

---

## When to Use Collab-Group vs Solo Code Review

| Scenario | Recommendation |
|----------|---------------|
| Complex sprint with architectural changes | **Collab-group** (this workflow) |
| Multiple external reviews with conflicting findings | **Collab-group** |
| Sprint that touched security-sensitive code | **Collab-group** |
| Straightforward sprint, minor findings expected | Solo (`workflow_sprint_code_review_solo.md`) |
| Sprint with no external reviews (self-review only) | Solo |
| Quick turnaround needed | Solo |

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_execute_sprint_dev_plan.md` | Precedes this workflow (produces the implementation to review) |
| `workflow_sprint_code_review_solo.md` | Solo alternative to this collab-group review |
| `workflow_sprint_closeout.md` | Follows this workflow (closes the sprint) |
| `workflow_code_audit.md` | Periodic full-codebase audit (different scope and purpose) |
| `workflow_start_new_sprint.md` | Entry point for the next sprint after closeout |
