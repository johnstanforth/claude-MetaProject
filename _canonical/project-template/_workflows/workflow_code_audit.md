# Workflow: Code Audit

> How to conduct a comprehensive, periodic code audit and create a remediation roadmap.
>
> **Note:** This is the full codebase audit workflow (periodic, multi-pass). It is distinct from the post-sprint collab-group code review (`workflow_sprint_code_review_collab.md`), which reviews a single sprint's changes.

## Quick Reference

| Item | Value |
|------|-------|
| Output | Categorized findings document + remediation roadmap |
| Finding categories | Security, Architecture, Code Quality, Tests, Frontend, Dependencies |
| Severity levels | Critical, High, Medium, Low |
| Exemplar | Phase 3 (265 findings, 7 category documents, 5 remediation sprints) |
| Key lesson | Test coverage BEFORE major refactors |

---

## Overview

A code review is a systematic audit of part or all of the codebase. It produces:
1. **Categorized findings** — every issue identified, with severity and location
2. **Remediation roadmap** — an ordered plan to address findings, organized as sprints

Code reviews are typically done:
- Before a major refactoring phase (to know what to fix)
- After a rapid feature-building phase (to pay down debt)
- When onboarding to an unfamiliar codebase
- Periodically (every 3-6 months) as a health check

---

## Step-by-Step

### Step 1: Define Review Scope

Determine what is being reviewed:

| Scope | When to Use | Effort |
|-------|-------------|--------|
| Full codebase | Before a major phase, periodic health check | Large (1-2 sessions) |
| Specific module | Targeted concern about one area | Medium (1 session) |
| Specific concern | "Are we handling auth correctly everywhere?" | Small (part of a session) |
| Recent changes | After a feature sprint | Small |

For full codebase reviews, break the review into passes:

```
Pass 1: Security (auth, input validation, secrets, injection)
Pass 2: Architecture (patterns, separation of concerns, coupling)
Pass 3: Code Quality (naming, complexity, duplication, error handling)
Pass 4: Tests (coverage, quality, flaky tests, missing cases)
Pass 5: Frontend (accessibility, responsiveness, JS patterns)
Pass 6: Dependencies (versions, vulnerabilities, unused deps)
```

### Step 2: Conduct the Review

For each file or module in scope:

1. Read the code
2. Check against the project's conventions (see CLAUDE.md)
3. Look for common issues in each category
4. Document every finding

**What to look for in each category:**

#### Security
- Authentication bypasses (missing `@login_required` decorators)
- Authorization gaps (missing `@project_access()` checks)
- SQL injection (raw SQL without parameterization)
- XSS (unescaped user input in templates)
- Secret exposure (hardcoded keys, secrets in logs)
- CSRF protection gaps
- Input validation (missing or insufficient)
- File upload validation

#### Architecture
- Circular imports
- Business logic in route handlers (should be in services)
- Direct database queries in views (should go through services)
- Inconsistent patterns across similar modules
- Missing abstraction layers
- Tight coupling between unrelated modules

#### Code Quality
- Functions longer than 50 lines
- Deeply nested conditionals (>3 levels)
- Duplicated code across files
- Inconsistent naming conventions
- Missing error handling (bare except, swallowed exceptions)
- Dead code (unused functions, commented-out blocks)
- Missing type hints on public functions

#### Tests
- Modules with no test coverage
- Tests that do not assert anything meaningful
- Missing edge case tests (empty input, None, boundary values)
- Tests that depend on execution order
- Flaky tests (intermittent failures)
- Missing integration tests for API endpoints

#### Frontend
- Missing accessibility attributes (aria labels, alt text)
- Inline JavaScript (should be in separate files)
- Inconsistent UI patterns across pages
- Missing loading states
- Missing error states
- Broken responsive behavior

#### Dependencies
- Outdated packages with known vulnerabilities
- Unused dependencies in `pyproject.toml`
- Missing dependency pins (unpinned transitive deps)
- Dev dependencies in production group

### Step 3: Write Findings Document

Organize findings by category and severity:

```markdown
# Code Review Findings: {Scope}

| Date | Reviewer | Scope |
|------|----------|-------|
| {YYYY-MM-DD} | @claude | {Description of scope} |

## Summary

| Category | Critical | High | Medium | Low | Total |
|----------|----------|------|--------|-----|-------|
| Security | 2 | 5 | 8 | 3 | 18 |
| Architecture | 0 | 3 | 12 | 7 | 22 |
| Code Quality | 1 | 8 | 15 | 10 | 34 |
| Tests | 0 | 6 | 9 | 4 | 19 |
| Frontend | 0 | 2 | 7 | 5 | 14 |
| Dependencies | 1 | 1 | 2 | 0 | 4 |
| **Total** | **4** | **25** | **53** | **29** | **111** |

## Security Findings

### SEC-001 [Critical]: Missing auth check on admin endpoint
- **File:** `app/api/admin.py:45`
- **Description:** The `/admin/stats` endpoint does not have `@admin_required`
- **Impact:** Any authenticated user can access admin statistics
- **Recommendation:** Add `@admin_required` decorator

### SEC-002 [High]: Raw SQL in analytics query
- **File:** `app/services/analytics_service.py:112`
- **Description:** User input is interpolated into SQL string without parameterization
- **Impact:** Potential SQL injection
- **Recommendation:** Use parameterized queries (never f-string/format SQL)

{...more findings...}

## Architecture Findings
{...}

## Code Quality Findings
{...}
```

### Step 4: Create Remediation Roadmap

Group findings into remediation sprints, ordered by:
1. **Critical and High severity items first** — these are blocking issues
2. **Dependencies between fixes** — some fixes enable others
3. **Related items together** — fixing all auth issues in one sprint is more efficient

```markdown
# Remediation Roadmap

## Sprint 1: Critical Security Fixes
- SEC-001: Add auth to admin endpoint
- SEC-002: Parameterize analytics queries
- SEC-003, SEC-004: Additional security hardening
Estimated effort: Small

## Sprint 2: Test Coverage Foundation
- TEST-001 through TEST-006: Add missing test files
- Rationale: Test coverage must exist BEFORE we refactor
Estimated effort: Medium

## Sprint 3: Architecture Improvements
- ARCH-001: Extract business logic from route handlers
- ARCH-002: Standardize service patterns
- Requires: Sprint 2 (tests to verify no regressions)
Estimated effort: Large

## Sprint 4: Code Quality Cleanup
- CQ-001 through CQ-015: Refactor long functions, remove duplication
- Requires: Sprint 2 (tests) and Sprint 3 (architecture)
Estimated effort: Medium

## Sprint 5: Frontend and Dependencies
- FE-001 through FE-005: Accessibility improvements
- DEP-001: Update vulnerable dependencies
Estimated effort: Medium
```

### Step 5: Execute Remediation

Create remediation sprints following `workflow_new_sprint.md`. Each sprint in the roadmap becomes a formal sprint with its own spec and execution plan.

**Key lesson from Phase 3:** Always establish test coverage BEFORE starting major refactors. Phase 3 Sprint 2 added tests, and Sprints 3-5 used those tests to verify that refactors did not introduce regressions.

---

## Finding Severity Guidelines

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| **Critical** | Security vulnerability, data loss risk, application crash | Fix immediately (next sprint) |
| **High** | Incorrect behavior, missing auth check, failing tests | Fix in current phase |
| **Medium** | Code smell, inconsistent pattern, missing tests | Fix when working in that area |
| **Low** | Style issue, minor improvement, documentation gap | Fix if convenient |

---

## Tips for Effective Code Reviews

1. **Be systematic.** Review every file in scope, do not skip files that "look fine." The worst bugs hide in code that looks correct at a glance.

2. **Check patterns, not just code.** If one endpoint is missing auth, check ALL endpoints for the same pattern.

3. **Count, do not just list.** Quantifying findings (111 total, 4 critical) makes the scope of work tangible.

4. **Give context in findings.** "Missing auth check" is vague. "The `/admin/stats` endpoint at `admin.py:45` lacks `@admin_required`, allowing any authenticated user to access admin statistics" is actionable.

5. **Propose specific fixes.** "Improve error handling" is vague. "Add try/except around the database query at line 78 and return a 500 response with a descriptive message" is actionable.

6. **Test coverage first.** This is the single most important lesson from Phase 3. Without tests, refactoring is a gamble.

---

## Phase 3 as Exemplar

Phase 3 (Code Review & Remediation) is the canonical example of this workflow:

- **Scope:** Full codebase (all `app/` code)
- **Findings:** 265 items across 7 categories
- **Output:** 7 category documents, 1 remediation roadmap
- **Remediation:** 5 sprints over Phase 3
- **Key outcome:** Zero regressions because tests were added before refactoring

Files: `_stages_and_phases/phase_03--code_review_remediation/`

---

## Related Workflows

- `workflow_start_new_sprint.md` — Each remediation sprint follows sprint workflow
- `workflow_error_debugging.md` — When findings require investigation
- `workflow_roadmap_rescheduling_solo.md` — Lower-severity findings may go to backlog
