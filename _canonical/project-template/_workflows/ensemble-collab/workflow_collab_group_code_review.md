# Workflow: Collab-Group Code Review (ensemble-collab)

> Legacy ensemble-script implementation of the post-sprint code review collab-group.

## Overview

This workflow uses the `/collab` skill to launch a two-agent code review session (codex + claude) that reviews sprint implementation, incorporates external review reports, and applies fixes. The session follows a strict three-phase process: independent review, external review analysis, and fix application.

**Prerequisites from the router document apply:**
- **Fix Everything Possible** — all findings must be addressed (Critical/Major/Minor/Observations)
- **Zero Test Failures** — full validation suite must pass
- **External Review Prompt** — must be prepared and sent before this session

---

## Pre-Launch Checklist

### 1. Collect External Reviews

Before launching the collab-group, external reviews must already be complete:

1. Verify `REVIEW-PROMPT--P{NN}-S{NN}.md` was sent to external reviewers
2. Collect all review reports into the phase directory:
   - `REVIEW--{AgentName}-P{NN}-S{NN}.md` (one per reviewer)
3. Note the file paths for the prompt template

### 2. Prepare the Prompt

Fill in the template at `_templates/COLLAB_PROMPT_CODE_REVIEW.md`:

| Placeholder | How to fill |
|-------------|-------------|
| `{PHASE_NN}` | Zero-padded phase number |
| `{SPRINT_NN}` | Zero-padded sprint number |
| `{SPRINT_TITLE}` | Human-readable sprint title |
| `{PHASE_SLUG}` | Phase directory slug |
| `{BRIEF_CONTEXT}` | 2-3 sentences on what the sprint built |
| `{XP_PATH}` | Full path to the sprint's xp file |
| `{IMPL_FILES}` | Lettered list of all implementation files changed |
| `{TEST_FILES}` | Lettered list of all test files changed |
| `{REVIEW_FILES}` | Paths to external review reports |
| `{REVIEW_CRITERIA}` | Sprint-specific review criteria |

Write the filled prompt to `/tmp/collab-code-review.txt`.

### 3. Verify Context Files

- [ ] `CLAUDE.md`
- [ ] `_workflows/workflow_collab_group_agent_guidelines.md`
- [ ] Sprint execution plan (xp file)
- [ ] All implementation files listed in the prompt
- [ ] All test files listed in the prompt
- [ ] All external review reports

### 4. Run Baseline Validation

Record the baseline state before the review session modifies anything:

```bash
uv run pytest tests/ -v
uv run ruff check .
```

Note any pre-existing failures. If there are failures, either fix them first or list them as approved xfails in the prompt.

### 5. Verify Working Tree

```bash
git status  # Must be clean
```

---

## Launch

```
/collab code-review /tmp/collab-code-review.txt
```

This launches a 2-party session: `codex` (LEAD) + `claude` (WORKER).

**After launch, tell the user the tmux session names for direct agent access:**
```
Agent panes:
  tmux attach -t {team-name}-codex-1
  tmux attach -t {team-name}-claude-2
```

**Agent roles:**
- **codex (LEAD):** Reviews code, analyzes findings, directs fixes, acts as approval gate
- **claude (WORKER):** Reviews code, challenges assumptions, makes ALL file edits, runs validation

The ensemble script handles agent spawning, prompt delivery, and output collection.

**3-Minute Steer — SUSPENDED (2026-05-03).** See `workflow_collab_group_launch.md` for details and the manual steer text. The main agent must print the steer message for the project owner to send manually if/when appropriate — do NOT send it automatically.

---

## Monitor and Verify Deliverables

### During the Session

The `/collab` skill provides periodic status updates. The code review session runs three strictly ordered phases:

**Phase 1 — Independent Review** (typically 5-10 min)
- Both agents read the xp and all code/test files
- They discuss findings item-by-item from their own analysis
- They do NOT read external reviews yet
- Output: consensus findings list with severity ratings
- LEAD writes `REVIEW-SUMMARY--P{NN}-S{NN}.md` with Phase 1 findings

**Phase 2 — External Review Analysis** (typically 3-8 min)
- Both agents now read all external review reports
- They evaluate each external finding: AGREE / DISAGREE / PARTIALLY AGREE
- Output: consolidated findings list, external reviewer report card
- LEAD updates the review summary file

**Phase 3 — Fixes** (typically 10-20 min)
- LEAD directs specific code edits
- WORKER implements each fix
- WORKER runs validation after each fix
- LEAD verifies each fix matches the consensus
- Final full validation suite run

### Expected Deliverables

- [ ] `REVIEW-SUMMARY--P{NN}-S{NN}.md` — findings list, external reviewer report card
- [ ] Code fixes applied to implementation and test files
- [ ] All tests passing
- [ ] Ruff clean

---

## Post-Completion: Main Agent Review and Commit

The collab-group agents write files but DO NOT commit. The main agent (Claude, orchestrating the session) must review all changes before committing. Run `git status` and `git diff` to see exactly what the agents wrote. Read each modified file and code fix to verify correctness.

### Verification

### 1. Review Session Output

Read the transcript from the `/collab` output. Verify:
- Phase ordering was respected (no external review reading during Phase 1)
- No file edits happened before Phase 3
- LEAD acted as approval gate (not rubber-stamping)
- WORKER ran validation after each fix
- Final validation passed

### 2. Run Full Validation

```bash
uv run pytest tests/ -v
uv run ruff check .
```

**HARD GATE:** Both must pass with zero failures. If they do not, the session is not complete.

### 3. Review the Summary

Read `REVIEW-SUMMARY--P{NN}-S{NN}.md` and verify:
- All findings have IDs and severity ratings
- Consolidated list merges Phase 1 and Phase 2 findings
- External reviewer report card evaluates each reviewer
- No findings were silently dropped

### 4. Verify Fix Completeness

Cross-reference the consolidated findings list against the actual code changes:
- Every Critical/Major finding must have a corresponding fix
- Minor findings and Observations should have fixes unless deferred with justification
- Deferred items must be written to the backlog

---

## Archive Session

Archive the full session directory from `/tmp/ensemble/<TEAM_ID>/` to the central archive:

```bash
TEAM_ID="<team-id>"
cp -r "/tmp/ensemble/$TEAM_ID" ~/Code/_ensemble/sessions/$(date +%Y-%m-%d)--$TEAM_ID
```

The archive location is `~/Code/_ensemble/sessions/` with naming convention `{YYYY-MM-DD}--{team-id}`. This is the one-and-only archive directory for all collab-group sessions across all projects. The archived directory contains `messages.jsonl` (full conversation), `prompts/` (injected prompts), and `summary.txt` (session summary).
---

## Report to User

Summarize the code review outcome:

1. **Findings** — total count by severity (Critical/Major/Minor/Observation)
2. **Fixes applied** — count and brief description of key changes
3. **Deferred items** — any findings not fixed, with justification and backlog destination
4. **External reviewer performance** — brief summary of each reviewer's accuracy
5. **Validation** — test suite and linter status (must be green)
6. **Files modified** — list of all files changed during the review
