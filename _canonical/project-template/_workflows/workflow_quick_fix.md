# Workflow: Quick Fix

> How to make a single fix or small change outside the formal sprint context.

## Quick Reference

| Item | Value |
|------|-------|
| Commit prefix | `P{NN}-FIX-{num} Description` |
| Branch | Current branch (do not create a new one) |
| Scope | Single issue, single commit |
| Tests required | Yes, always |
| When NOT to use | Multi-file refactors, new features, anything taking >30 minutes |

---

## Overview

Not every change needs a full sprint. A quick fix is a single, focused commit that addresses one specific issue. It is appropriate for:
- Bug fixes discovered during testing or usage
- Typo corrections in code or documentation
- Small configuration adjustments
- Test additions for uncovered edge cases
- Dependency version bumps

---

## When to Use Quick Fix vs. Sprint

| Scenario | Quick Fix? | Sprint? |
|----------|-----------|---------|
| One-line bug fix | Yes | No |
| Fix a failing test | Yes | No |
| Add a missing import | Yes | No |
| Rename a variable across 2 files | Yes | No |
| Add a new API endpoint | No | Yes |
| Refactor a service module | No | Yes |
| Change spans 5+ files | No | Yes |
| Change requires migration | Maybe | Usually yes |
| Change takes >30 minutes | No | Yes |

Rule of thumb: if you can describe the change in one sentence and implement it in one commit, it is a quick fix.

---

## Step-by-Step

### Step 1: Identify the Issue

Clearly state what is wrong and what the fix should be.

```
Issue: The `/api/v1/projects/<slug>/issues` endpoint returns 500 when the
project has no milestones because `milestone.name` is called on None.

Fix: Add a None check before accessing `milestone.name` in `issue_service.py`.
```

### Step 2: Make the Fix

Fix the issue on the current branch. Do not create a new branch for a quick fix.

Keep the change minimal:
- Fix only the identified issue
- Do not refactor surrounding code
- Do not add unrelated improvements
- Do not modify files outside the fix scope

### Step 3: Write or Run Tests

Every fix must be verified:

```bash
# Run the specific test file
uv run pytest tests/test_issue_service.py -v

# If no test covers this case, add one
# Then run it
uv run pytest tests/test_issue_service.py::test_issues_without_milestones -v

# Run the full suite to check for regressions
uv run pytest tests/ -v
```

If the fix is for a bug that had no test coverage, add a test that:
1. Reproduces the original bug (would have failed before the fix)
2. Passes with the fix applied

### Step 4: Commit

Use the quick fix commit prefix:

```bash
git add app/services/issue_service.py tests/test_issue_service.py
git commit -m "P05-FIX-01 Handle None milestone in issue list endpoint"
```

**Numbering:** `FIX-{num}` numbers are sequential within a phase. Check `git log --oneline --grep="FIX-"` to find the next number.

### Step 5: Document

If the fix reveals a recurring pattern or architectural issue, add it to one of:
- The current sprint's follow-up section (if a sprint is in progress)
- The backlog (`_specs_and_plans/_backlog/_horizon_NEXT.md`)
- CLAUDE.md's Known Issues section (if it is a gotcha others will hit)

---

## Verification Requirements

Before considering a quick fix complete:

- [ ] The specific issue is resolved
- [ ] Tests pass (existing + any new ones)
- [ ] No regressions in the full test suite
- [ ] The commit message clearly describes what was fixed and why
- [ ] The working tree is clean

---

## Anti-Patterns

| Anti-Pattern | Why It Is Wrong |
|-------------|----------------|
| "Quick fix" that touches 10 files | That is a sprint, not a quick fix |
| Quick fix without running tests | May introduce regressions |
| Quick fix on a new branch | Unnecessary branch overhead for one commit |
| Batching 3 quick fixes in one commit | Each fix should be independently revertable |
| Quick fix that changes behavior, not just correctness | That is a feature change, needs a sprint |

---

## Related Workflows

- `workflow_start_new_sprint.md` — For changes that are too large for a quick fix
- `workflow_error_debugging.md` — For diagnosing the issue before fixing it
