# Workflow: Execute Sprint Dev Plan

> Deterministic autonomous execution of a pre-approved execution plan (xp). Designed for a fresh agent session with `--dangerously-skip-permissions`. The xp is the contract -- execute it faithfully.

## Quick Reference

| Item | Value |
|------|-------|
| Mode | `claude --dangerously-skip-permissions` |
| Input | Approved `xp_{NN}--{slug}.md` (committed, human-reviewed) |
| Output | All tasks implemented, committed, tested; review prompt generated |
| Validation | `uv run pytest tests/ -v` + `uv run ruff check .` -- ZERO failures |
| Technology | Python 3.12+ library (uv; SQLite WAL archival storage); code-primary |
| Commit format | `P{NN}-S{NN}-T{NN} Description` |

---

## Pipeline Position

```
  +-------------------+    +-----------------+    +--------------+
  | start_new_sprint  |--->| Planning        |--->| Human Review |
  +-------------------+    | (solo/collab)   |    | (async)      |
                           +-----------------+    +--------------+
                                                        |
                                                        v
                                                  YOU ARE HERE
                                                        |
                                                        v
                                              +---------------------+
                                              | EXECUTE SPRINT      |
                                              | DEV PLAN            |
                                              | (this workflow)     |
                                              +---------------------+
                                                        |
                                                        v
                                              +---------------------+
                                              | External Reviews    |
                                              | (Gemini, Cursor,    |
                                              |  KimiK25, etc.)     |
                                              +---------------------+
                                                        |
                                                        v
                                              +---------------------+
                                              | sprint_code_review  |
                                              | (solo or collab)    |
                                              +---------------------+
                                                        |
                                                        v
                                              +---------------------+
                                              | sprint_closeout     |
                                              +---------------------+
```

---

## Prerequisites

Before starting execution, ALL of the following must be true:

- [ ] Sprint planning is complete (solo or collab-group)
- [ ] Sprint spec (`sp_{NN}--{slug}.md`) is committed
- [ ] Execution plan (`xp_{NN}--{slug}.md`) is committed
- [ ] Human has reviewed and approved the xp
- [ ] Agent is running in autonomous mode (`--dangerously-skip-permissions`)
- [ ] Working tree is clean (`git status` shows nothing to commit)
- [ ] On the correct sprint branch (`claudecode/@claude/phase{NN}-sprint{NN}`)

---

## Step 1: Find the Active Sprint

Scan the phase directory for the highest non-COMPLETE sprint:

```bash
# List sprint specs, most recent first
ls -t _specs_and_plans/phase_*--*/sp_*.md 2>/dev/null

# Check status of the most recent sprint spec
grep -i "Status" _specs_and_plans/phase_{NN}--{slug}/sp_{NN}--{slug}.md
```

**HARD GATE — Status Check:** The sp_ file's `Status` field must be `APPROVED` or `IN PROGRESS`. If it shows `PLANNING`, the sprint has not been reviewed and approved by the project owner — **STOP immediately** and report:

> "Sprint {NN} status is PLANNING. The sprint spec and execution plan must be reviewed and approved by the project owner before execution can begin. The status field in the sp_ file must be set to APPROVED."

Confirm the execution plan exists:

```bash
ls _specs_and_plans/phase_{NN}--{slug}/xp_{NN}--{slug}.md
```

**HARD GATE — xp File Check:** If the xp file does not exist, **STOP immediately**. Report to the user:

> "No execution plan found for Sprint {NN}. The xp file must be created and approved before execution can begin. Run `workflow_start_new_sprint.md` to create the plan."

Do not attempt to execute from the sp file alone. The xp is the implementation contract.

---

## Step 2: Read Sprint Spec for Context

Read the sprint spec (`sp_{NN}--{slug}.md`) for orientation:

- Phase and sprint metadata
- Goals and non-goals (scope boundaries)
- Task table (overview of what needs to be done)

This is for context only. The xp is the authoritative source for implementation details.

---

## Step 3: Read the Execution Plan

Read the full execution plan (`xp_{NN}--{slug}.md`). Process it in this order:

### 3a. Context and Scope Boundaries

Read the "Pre-Execution Findings" and "Critical Rules" sections first. These establish:

- Current state of relevant code (file paths, function signatures, patterns)
- Hard constraints on what you may and may not modify
- Sprint-specific rules beyond the standard set

### 3b. Full Task List

Read every task detail section (T01 through TNN). For each task, note:

- Files to modify or create
- Implementation steps
- Required tests
- Dependencies on other tasks

### Hard Rules for Execution

These rules are non-negotiable. Violating any of them is a sprint failure.

1. **Scope immutability.** The approved xp scope must not be changed, reduced, deferred, or dropped during execution. If a task proves harder than expected, implement it anyway or STOP and report a blocker. Never silently skip or defer a task.

2. **Test completeness.** Any test changes required by the xp's tasks are mandatory within this sprint. If code changes break existing tests, fix them. If new features need new tests (per task details), write them. Zero failures at the end.

3. **Self-contained execution.** The xp contains all implementation details needed. Do not reference external documents (ADRs, research docs) for implementation guidance -- if the xp is missing details, that is a planning failure. Note it but proceed with your best judgment.

---

## Step 4: Execute All Tasks

For each task T01 through TNN, in the sequence specified by the xp:

### 4a. Implement

- Make the code changes described in the task
- Follow existing patterns in the codebase (check similar files before writing new code)
- Stay within the task's scope -- do not gold-plate or add unrequested features

### 4b. Test

Run the targeted tests relevant to the task:

```bash
uv run pytest tests/{relevant_test_file}.py -v
```

If the task introduces new functionality, also run the broader test suite to catch regressions:

```bash
uv run pytest tests/ -v
```

### 4c. Fix Failures (2-Attempt Rule)

If tests fail after implementation, you get **exactly 2 attempts** to fix them. After 2 failures, STOP and flag for human review. Do not continue spiraling. See [`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes) for the full rule and rationale.

### 4d. Commit

```bash
git add <specific files>
git commit -m "P{NN}-S{NN}-T{NN} Description of what was done"
```

Rules:
- One commit per task. Do not batch multiple tasks into one commit.
- Use the `P{NN}-S{NN}-T{NN}` prefix. Phase number is not zero-padded; sprint and task numbers are.
- Commit message should be in imperative mood and concise.
- For complex changes, include a commit body with bullet points.

### 4e. Proceed to Next Task

After a successful commit, proceed to the next task in sequence. If the xp specifies that some tasks are independent, they can be done in any order.

---

## Step 5: Full Validation

After ALL tasks are complete, run the full validation suite:

```bash
uv run pytest tests/ -v
uv run ruff check .
```

**HARD GATE: BOTH must pass with ZERO failures.** There is no such thing as a "pre-existing failure." If any test fails or any lint check fails, it must be fixed before proceeding -- even if the failure appears unrelated to this sprint's changes.

The **2-attempt rule** applies ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)): if fixing a validation failure requires more than 2 attempts, STOP and report the blocker to the user.

---

## Step 6: Post-Sprint Notes

Add post-sprint notes to the sprint spec (`sp_{NN}--{slug}.md`). Update the existing "Post-Sprint Notes" section with:

```markdown
## Post-Sprint Notes

### Summary
{2-3 sentences describing what was accomplished and any deviations from the plan.}

### Metrics
- Tasks completed: {N}/{total}
- Tests added: {N}
- Tests passing: {N}/{total}
- Commits: {N}
- Files modified: {N}

### Deviations
{What changed from the plan and why. If nothing changed, say "Executed as planned."}

### Lessons Learned
{What would you do differently? What patterns emerged? What was harder or easier than expected?}
```

Update the sprint status to IN PROGRESS (not COMPLETE -- that happens during closeout):

```markdown
| Status | IN PROGRESS |
```

---

## Step 7: Generate External Review Prompt

Generate a review prompt for external reviewers using the template at `_workflows/_templates/EXTERNAL_REVIEW_PROMPT.md`.

### 7a. Gather Implementation Data

```bash
# Get the commit log for this sprint
git log --oneline claudecode/@claude/phase{NN}-sprint{PREV}..HEAD

# Get the list of changed files
git diff --name-only claudecode/@claude/phase{NN}-sprint{PREV}..HEAD

# Separate implementation files from test files
git diff --name-only claudecode/@claude/phase{NN}-sprint{PREV}..HEAD | grep -v "^tests/"
git diff --name-only claudecode/@claude/phase{NN}-sprint{PREV}..HEAD | grep "^tests/"
```

### 7b. Fill the Template

Copy the template and fill all `{PLACEHOLDER}` values:

- `{PHASE_NN}` -- zero-padded phase number
- `{SPRINT_NN}` -- zero-padded sprint number
- `{SPRINT_TITLE}` -- human-readable sprint title from the sp
- `{BRIEF_CONTEXT}` -- 2-4 sentences on what this sprint built
- `{SP_PATH}` -- path to the sprint spec file
- `{XP_PATH}` -- path to the execution plan file
- `{IMPL_FILES}` -- lettered list of implementation files with one-line descriptions
- `{TEST_FILES}` -- lettered list of test files with one-line descriptions
- `{COMMIT_LOG}` -- sprint commit log from `git log --oneline`
- `{REVIEW_CRITERIA}` -- sprint-specific review criteria sections
- `{PHASE_DIR}` -- phase directory path
- `{DELIVERABLE_FILENAME}` -- `REVIEW--{YourAgentName}-P{NN}-S{NN}.md`

### 7c. Save and Commit

Save the review prompt as:

```
_specs_and_plans/phase_{NN}--{slug}/REVIEW-PROMPT--P{NN}-S{NN}.md
```

Commit the review prompt together with the post-sprint notes update:

```bash
git add _specs_and_plans/phase_{NN}--{slug}/REVIEW-PROMPT--P{NN}-S{NN}.md
git add _specs_and_plans/phase_{NN}--{slug}/sp_{NN}--{slug}.md
git commit -m "P{NN}-S{NN} Post-sprint notes and external review prompt"
```

---

## Step 8: Hand Off

Report to the user with the following information:

```
Sprint {NN} execution complete.

Tasks: {N}/{total} completed
Validation: pytest {PASS/FAIL} | ruff {PASS/FAIL}
Commits: {N} (list commit hashes or oneline)

Review prompt saved to:
  _specs_and_plans/phase_{NN}--{slug}/REVIEW-PROMPT--P{NN}-S{NN}.md

Next steps (code review is ALWAYS required after sprint execution):
  1. Send review prompt to external reviewers (Gemini, Cursor, KimiK25, etc.)
  2. Collect review files as REVIEW--{AgentName}-P{NN}-S{NN}.md in the phase directory
  3. Run code review: workflow_sprint_code_review_collab.md (or solo variant)
  4. Run sprint closeout: workflow_sprint_closeout.md
```

Code review is not optional — every sprint execution is followed by a code review session before closeout. If any tasks failed or were blocked, include them prominently in the report with the failure details.

---

## Context Management

### When to `/clear`

- Between unrelated tasks (if context is cluttered with irrelevant error traces)
- After 2 failed correction attempts (fresh context often reveals the issue)
- When switching from one subsystem to a completely different one
- **Never** clear in the middle of a multi-file change

### What to read first in a fresh session

1. The execution plan (`xp_` document) -- this is the primary context
2. `CLAUDE.md` -- project conventions, if not already loaded
3. Relevant source files -- only as needed for each task

### Fresh session discipline

- Each execution session is self-sufficient from the plan
- Do not rely on context from the planning session
- Do not assume the human remembers planning discussions
- The plan IS the contract

---

## Error Recovery

### Test failure after implementation

Apply the **2-attempt rule** ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)): attempt a fix, if it fails try a different approach, if that also fails STOP and flag for human review.

### Merge conflicts

Should not happen if branching from the previous sprint tip. If they do occur: stop and flag for human review.

### Missing dependency or prerequisite

If a task depends on something not in the plan, note it and skip to the next independent task. Flag the blocked task for human review.

### Dev server lifecycle

- Stop the dev server before making bulk file changes or running migrations
- Restart after changes are complete and tests pass
- Dev server: N/A — this project is a library (no dev server)
- Dev server logs: check terminal output

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_start_new_sprint.md` | Entry point that leads here through planning |
| `workflow_sprint_planning_solo.md` | Solo planning (produces the xp this workflow executes) |
| `workflow_sprint_planning_collab.md` | Collab planning (produces the xp this workflow executes) |
| `workflow_sprint_code_review_solo.md` | Solo code review (next step after external reviews) |
| `workflow_sprint_code_review_collab.md` | Collab code review (alternative to solo) |
| `workflow_sprint_closeout.md` | Sprint closing checklist (final step) |
| `workflow_error_debugging.md` | Diagnosing failures during execution |
