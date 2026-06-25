# Workflow: Sprint Code Review (Solo)

> Solo agent code review after sprint execution. Reads the implementation and external review reports, categorizes findings, implements fixes, validates, and produces a review summary. This is the solo alternative to `workflow_sprint_code_review_collab.md`.

## Quick Reference

| Item | Value |
|------|-------|
| Input | Completed sprint + external review files (`REVIEW--*.md`) |
| Output | Fixes committed + `REVIEW-SUMMARY--P{NN}-S{NN}.md` |
| Validation | `uv run pytest tests/ -v` + `uv run ruff check .` -- ZERO failures |
| Technology | Python 3.12+ library (uv; SQLite WAL archival storage); code-primary |
| Fix rule | Fix ALL findings within scope; defer ONLY if fixing widens into another sprint's scope |
| External review files | `REVIEW--{AgentName}-P{NN}-S{NN}.md` in the phase directory |

---

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
                                                                | REVIEW (SOLO)     |
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

Before starting the code review, ALL of the following must be true:

- [ ] Sprint execution is complete (`workflow_execute_sprint_dev_plan.md` finished)
- [ ] All sprint tasks are committed with `P{NN}-S{NN}-T{NN}` prefixes
- [ ] Post-sprint notes have been added to the sp file
- [ ] External review prompt was generated and sent to reviewers
- [ ] External review files are present in the phase directory (or user has confirmed none are coming)
- [ ] Validation suite passes: `uv run pytest tests/ -v` + `uv run ruff check .`

---

## Step 1: Confirm External Reviews

Check for external review files in the phase directory:

```bash
ls _specs_and_plans/phase_{NN}--{slug}/REVIEW--*-P{NN}-S{NN}.md 2>/dev/null
```

Expected naming: `REVIEW--{AgentName}-P{NN}-S{NN}.md` (e.g., `REVIEW--Gemini-P05-S04.md`, `REVIEW--Cursor-P05-S04.md`).

**If no review files are found:**

Ask the user:

> "No external review files found in the phase directory. Options:
> 1. Wait for external reviews to be collected
> 2. Proceed with self-review only (no external input)
> 3. Point me to the review files if they are in a different location
>
> Which would you prefer?"

Do not proceed without an explicit answer. External reviews are valuable -- skipping them should be a deliberate choice, not an oversight.

**If review files are found:**

List them and confirm with the user:

> "Found {N} external review(s): {list filenames}. Proceeding with code review."

---

## Step 2: Read Implementation and Reviews

Read documents in this specific order. The order matters -- it builds context from plan to implementation to critique.

### 2a. Execution Plan (first)

Read `xp_{NN}--{slug}.md` to understand:
- What was supposed to be built
- Critical Rules that governed execution
- Task-by-task implementation details
- Acceptance criteria

This establishes the baseline for evaluating whether the implementation matches the plan.

### 2b. External Review Files

Read each `REVIEW--{AgentName}-P{NN}-S{NN}.md` file. For each review, note:
- Findings by severity (Critical / Major / Minor / Observation)
- Specific file paths and line numbers cited
- Recommendations made
- Overall assessment

Track which reviewers agree on the same findings -- consensus findings are higher priority.

### 2c. Implementation Files

Read all implementation files that were modified during the sprint:

```bash
git diff --name-only claudecode/@claude/phase{NN}-sprint{PREV}..HEAD | grep -v "^tests/" | grep -v "^_specs_and_plans/"
```

For each file, evaluate:
- Does the implementation match the xp's task details?
- Are there issues the external reviewers identified?
- Are there issues the external reviewers missed?

### 2d. Test Files

Read all test files that were added or modified:

```bash
git diff --name-only claudecode/@claude/phase{NN}-sprint{PREV}..HEAD | grep "^tests/"
```

For each test file, evaluate:
- Do tests cover the functionality described in the xp?
- Are there missing edge cases?
- Are assertions meaningful (not just "assert True")?
- Do tests follow existing patterns in the test suite?

---

## Step 3: Categorize and Triage Findings

For every finding from the external reviews AND from your own review, create a categorized assessment.

### 3a. Assess Each External Finding

For each finding from the external reviews, determine your position:

| Position | Meaning | Action |
|----------|---------|--------|
| **Agree** | The finding is valid and should be fixed | Fix it |
| **Partially Agree** | The finding has merit but the recommendation is wrong or incomplete | Fix with a modified approach |
| **Disagree** | The finding is incorrect, irrelevant, or based on a misunderstanding | Document why and skip |

### 3b. Assign Severity

Every finding (from external reviews and your own) gets a severity:

| Severity | Criteria | Response |
|----------|----------|----------|
| **Critical** | Security vulnerability, data loss risk, application crash, incorrect behavior | Must fix now |
| **Major** | Missing validation, broken edge case, inconsistent pattern, missing tests for new code | Must fix now |
| **Minor** | Code style, naming, minor refactoring opportunity, documentation gap | Fix if within scope |
| **Observation** | Suggestion for future improvement, alternative approach worth considering | Fix if trivial, otherwise defer |

### 3c. Determine Scope

For each finding you will address, determine whether the fix is within this sprint's scope:

- **Within scope:** The fix modifies files changed in this sprint, or fixes a direct consequence of this sprint's changes. **Fix it.**
- **Outside scope:** The fix requires new migrations, new API endpoints, changes to unrelated subsystems, or work that belongs in a different sprint. **Defer it** with a clear note explaining why.

The bar for deferral is high. If you can fix it without widening the sprint's footprint, fix it. Deferral is for cases where the fix would genuinely constitute new feature work.

---

## Step 4: Implement Fixes

Address ALL findings that are within scope, starting with Critical severity and working down.

### For each fix:

1. **Implement the fix.** Make the code change.
2. **Run targeted tests.** Verify the fix does not break anything:
   ```bash
   uv run pytest tests/{relevant_test_file}.py -v
   ```
3. **Commit the fix.**
   ```bash
   git add <specific files>
   git commit -m "P{NN}-S{NN} Review fix: {brief description of what was fixed}"
   ```

### Commit conventions for review fixes:

- Use `P{NN}-S{NN} Review fix: {description}` format (no task number -- these are review-driven, not plan-driven)
- Group related fixes into a single commit when they touch the same file and address the same concern
- Keep unrelated fixes in separate commits for clean git history

### 2-Attempt Rule

The **2-attempt rule** applies here too ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)): if a fix fails after 2 attempts, STOP and flag for human review.

---

## Step 5: Full Validation

After ALL fixes are applied, run the complete validation suite:

```bash
uv run pytest tests/ -v
uv run ruff check .
```

**HARD GATE: BOTH must pass with ZERO failures.** There is no such thing as a "pre-existing failure." If any test fails or any lint check fails, it must be fixed before the review is considered complete.

If the full suite was passing before the review fixes and now fails, one of the fixes introduced a regression. Identify which fix caused it and correct it.

---

## Step 6: Write Review Summary

Create a review summary document:

```
_specs_and_plans/phase_{NN}--{slug}/REVIEW-SUMMARY--P{NN}-S{NN}.md
```

### Required Structure:

```markdown
# Code Review Summary: Phase {NN}, Sprint {NN}

| Field | Value |
|-------|-------|
| Sprint | {NN} — {Title} |
| External Reviews | {N} ({list reviewer names}) |
| Findings Total | {N} |
| Findings Fixed | {N} |
| Findings Deferred | {N} |
| Findings Disagreed | {N} |
| Date | {YYYY-MM-DD} |

## External Review Sources

| Reviewer | Findings | Agreed | Partially | Disagreed |
|----------|----------|--------|-----------|-----------|
| {Name} | {N} | {N} | {N} | {N} |
| Self-review | {N} | -- | -- | -- |

## Findings Addressed

### Critical

{List each critical finding with: source, description, fix applied, commit hash}

### Major

{List each major finding with: source, description, fix applied, commit hash}

### Minor

{List each minor finding with: source, description, fix applied, commit hash}

### Observations Addressed

{List each observation that was fixed, with: source, description, fix applied}

## Findings Deferred

| # | Source | Severity | Description | Reason for Deferral | Destination |
|---|--------|----------|-------------|---------------------|-------------|
| 1 | {Reviewer} | {Sev} | {Description} | {Why it widens scope} | {Backlog/Next sprint} |

## Findings Disagreed

| # | Source | Severity | Description | Reason for Disagreement |
|---|--------|----------|-------------|------------------------|
| 1 | {Reviewer} | {Sev} | {Description} | {Why the finding is invalid} |

## Final Assessment

{2-3 paragraphs summarizing:
- Overall quality of the sprint implementation
- How well it matched the execution plan
- Areas of strength
- Areas that need attention in future sprints
- Whether the deferred items are significant enough to affect the next sprint}

## Validation

```
uv run pytest tests/ -v    -- {PASS/FAIL} ({N} tests)
uv run ruff check .        -- {PASS/FAIL}
```
```

### Commit the Summary

```bash
git add _specs_and_plans/phase_{NN}--{slug}/REVIEW-SUMMARY--P{NN}-S{NN}.md
git commit -m "P{NN}-S{NN} Code review summary"
```

---

## Step 7: Hand Off

Report to the user:

```
Sprint {NN} code review complete.

Findings: {N} total
  - Fixed: {N} (Critical: {N}, Major: {N}, Minor: {N}, Observations: {N})
  - Deferred: {N} (see review summary for details)
  - Disagreed: {N}

Validation: pytest {PASS/FAIL} | ruff {PASS/FAIL}

Review summary saved to:
  _specs_and_plans/phase_{NN}--{slug}/REVIEW-SUMMARY--P{NN}-S{NN}.md

Next step:
  Run workflow_sprint_closeout.md to close out the sprint.
```

If there are deferred items, highlight them:

> "Note: {N} findings were deferred because fixing them would widen the sprint scope. These should be triaged during closeout to the backlog or next sprint."

---

## When to Use Solo vs Collab Code Review

| Scenario | Recommendation |
|----------|---------------|
| Straightforward sprint, minor findings expected | **Solo** (this workflow) |
| Complex sprint with architectural changes | Collab-group (`workflow_sprint_code_review_collab.md`) |
| Multiple external reviews with conflicting findings | Collab-group |
| Sprint that touched security-sensitive code | Collab-group |
| Sprint with no external reviews (self-review only) | **Solo** |
| Quick turnaround needed | **Solo** |

---

## Related Workflows

| Workflow | Relationship |
|----------|-------------|
| `workflow_execute_sprint_dev_plan.md` | Precedes this workflow (produces the implementation to review) |
| `workflow_sprint_code_review_collab.md` | Collab-group alternative to this solo review |
| `workflow_sprint_closeout.md` | Follows this workflow (closes the sprint) |
| `workflow_code_audit.md` | Periodic full-codebase audit (different scope and purpose) |
| `workflow_start_new_sprint.md` | Entry point for the next sprint after closeout |
