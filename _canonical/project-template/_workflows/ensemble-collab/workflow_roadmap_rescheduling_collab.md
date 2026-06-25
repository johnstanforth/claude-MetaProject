# Workflow: Roadmap Rescheduling (ensemble-collab)

> Legacy ensemble-script implementation of the roadmap rescheduling collab-group.

## Overview

This workflow uses the `/collab` skill to launch a two-agent session (codex + claude) that performs a full roadmap rescheduling. The skill manages the session via legacy ensemble scripts — spawning agent processes, piping the prompt, and collecting output.

---

## Pre-Launch Checklist

Complete ALL items before launching the session.

### 1. Prepare the Prompt

Fill in the template at `_templates/COLLAB_PROMPT_ROADMAP_RESCHEDULING.md`:

| Placeholder | How to fill |
|-------------|-------------|
| `{UNSORTED_COUNT}` | Count items in `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md` |
| `{TEST_COUNT}` | Run `uv run pytest tests/ -v --tb=no -q` and count passes |
| `{PHASE_NN}` | Current phase number, zero-padded |
| `{SPRINT_NN}` | Most recent sprint number, zero-padded |
| `{BRIEF_STATUS}` | 2-3 sentences on current project state |
| `{RECENT_SP_PATH}` | Path to the most recent sprint's sp file |
| `{PHASE_README_PATH}` | Path to the current phase's README |

Write the filled prompt to `/tmp/collab-roadmap-rescheduling.txt`.

### 2. Verify Context Files Exist

Confirm these files are present and up to date:

- [ ] `CLAUDE.md`
- [ ] `_specs_and_plans/ROADMAP.md`
- [ ] `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md`
- [ ] `_specs_and_plans/_backlog/_horizon_NEXT.md`
- [ ] `_specs_and_plans/_backlog/_horizon_LATER.md`
- [ ] `_specs_and_plans/_backlog/_horizon_SOMEDAY.md`
- [ ] `_workflows/workflow_collab_group_agent_guidelines.md`
- [ ] Current phase README
- [ ] Most recent sprint sp file

### 3. Verify Working Tree

```bash
git status  # Must be clean — no uncommitted changes
```

---

## Launch

Use the `/collab` skill to start the ensemble session:

```
/collab roadmap-rescheduling /tmp/collab-roadmap-rescheduling.txt
```

This launches a 2-party session: `codex` (LEAD) + `claude` (WORKER).

The ensemble script handles:
- Agent process spawning
- Prompt delivery to both agents
- Output collection

**Agents:** Always `codex,claude` (2-party). Codex is LEAD, Claude is WORKER.

**After launch, tell the user the tmux session names for direct agent access:**
```
Agent panes:
  tmux attach -t {team-name}-codex-1
  tmux attach -t {team-name}-claude-2
```

**3-Minute Steer — SUSPENDED (2026-05-03).** See `workflow_collab_group_launch.md` for details and the manual steer text. The main agent must print the steer message for the project owner to send manually if/when appropriate — do NOT send it automatically.

---

## Monitor and Verify Deliverables

### During the Session

The `/collab` skill provides periodic status updates. The session typically runs 8-15 minutes. Key milestones:

1. Both agents confirm they have read all mandatory files
2. Phase health check verdict is stated (ACTIVE / WINDING DOWN / RECOMMEND TRANSITION)
3. UNSORTED_QUEUE items are being discussed and sorted
4. LEAD begins writing deliverable files
5. WORKER reviews deliverables

### Expected Deliverables

When the session concludes, verify these files were written or updated:

- [ ] `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md` (should be empty except header)
- [ ] `_specs_and_plans/_backlog/_horizon_NEXT.md` (updated)
- [ ] `_specs_and_plans/_backlog/_horizon_LATER.md` (updated)
- [ ] `_specs_and_plans/_backlog/_horizon_SOMEDAY.md` (updated)
- [ ] `_specs_and_plans/ROADMAP.md` (phase assessment note added, backlog summary updated)

---

## Post-Completion: Main Agent Review and Commit

The collab-group agents write files but DO NOT commit. The main agent (Claude, orchestrating the session) must review all changes before committing. Run `git status` and `git diff` to see exactly what the agents wrote. Read each modified file to verify correctness.

### Verification

### 1. Review Session Output

The `/collab` skill outputs the session transcript when the session ends. Review for:
- Did both agents read all mandatory files before discussion?
- Was there genuine discussion before writing?
- Did the WORKER review deliverables after the LEAD wrote them?
- Was the phase health check verdict well-reasoned?

### 2. Verify Deliverable Quality

- UNSORTED_QUEUE is empty (all items sorted or archived)
- Horizon files have clear categories and descriptions
- ROADMAP.md has a timestamped phase assessment note
- No items were silently dropped (compare pre/post counts)
- Items marked "implemented" actually were implemented (spot-check against CLAUDE.md)

### 3. Verify No Source Code Changes

Roadmap rescheduling sessions edit only markdown files. Run `git diff --name-only` and confirm no files under `app/`, `tests/`, or `migrations/` were modified. If source code was accidentally changed, investigate before committing. Do NOT run pytest or ruff — this session does not touch code and validation would waste tokens for zero diagnostic value.

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

Summarize the rescheduling outcome:

1. **Phase health verdict** — ACTIVE / WINDING DOWN / RECOMMEND TRANSITION
2. **UNSORTED_QUEUE** — how many items were sorted and where they went
3. **Horizon changes** — notable promotions, demotions, or archival
4. **ROADMAP updates** — what changed in planned phases
5. **Recommendation** — what the user should do next (plan next sprint, start new phase, etc.)
