# Workflow: Collab-Group Launch (ensemble-collab)

> Legacy ensemble-script implementation of the collab-group launch workflow.

## Overview

This workflow uses the `/collab` skill to launch collaboration sessions via legacy ensemble scripts. It covers both built-in workflow presets (sprint planning, code review, roadmap rescheduling) and ad-hoc sessions.

---

## ⚠️ Two ways to launch — `/collab` skill (preferred) vs. manual script (fallback)

The **preferred** launch is the **`/collab` skill** (`~/.claude/skills/collab/SKILL.md`): invoke it via the Skill tool (or `/collab {preset} /tmp/collab-{preset}.txt`). The skill bundles **launch + monitoring as ONE flow** — its Step 1 launches the team, and its Step 3 starts a *background watcher* that completes when the team disbands, so the orchestrating Claude receives a harness notification the moment the session finishes.

**But in some orchestration contexts the `/collab` skill is NOT surfaced to the Claude instance** (it is installed on disk but absent from that session's available-skills list — e.g. certain Claude Code CLI sessions). When that happens, do **NOT** abandon the workflow — **replicate the skill's full flow manually** with the underlying scripts. The crucial point: the bare launch script is only the skill's **Step 1**; you MUST also run the **Step 3** watcher, or you get **no disband notification** (the launcher spawns the team and returns immediately — it does not block until disband).

1. **Launch (= skill Step 1)** — from the project root, run the launcher in the BACKGROUND:
   ```bash
   cd /path/to/project && ~/Code/_ensemble/ensemble_launch.sh /tmp/collab-{preset}.txt   # run_in_background: true
   ```
   It spawns the team + a feed-poller, prints "Team is live!", then RETURNS (~12s). **Two different identifiers are in play — do NOT confuse them:** (a) the **run-dir id** is a **UUID** (e.g. `e999a0f3-…`), read from `/tmp/collab-team-id.txt` (= the newest `/tmp/ensemble/<uuid>/` dir) — use it for the watcher's `RD` and the archive (steps 2–3); (b) the **tmux team-name** is the `collab-<timestamp>-…` string printed as "Team created (collab-…)" — use it ONLY for the agent panes (`collab-<timestamp>-codex-1` / `collab-<timestamp>-claude-2`). ⚠️ The run dir is **NOT** `/tmp/ensemble/collab-<timestamp>` — that path does not exist, and a watcher pointed there silently never fires (this bit us 2026-06-24).

2. **Disband-watcher (= skill Step 3) — DO NOT SKIP.** This is the step the bare script omits, and the reason a manual launch gives no notification. Immediately start a background task that completes on disband:
   ```bash
   RUN_ID="$(cat /tmp/collab-team-id.txt)"; RD="/tmp/ensemble/$RUN_ID"   # RUN_ID = the UUID run-dir id, NOT the collab-<timestamp> tmux name
   while [ ! -f "$RD/.finished" ] && [ ! -f "$RD/summary.txt" ]; do sleep 8; done && echo COLLAB_COMPLETE && cat "$RD/summary.txt"
   ```
   Run with `run_in_background: true`, `timeout: 600000`. `ensemble-service` writes `.finished`/`summary.txt` on disband → the background task completes → the harness notifies the orchestrating Claude, identical to what the `/collab` skill produces. (Functionally equivalent: loop `collab-poll.sh "$RUN_ID"` until it returns `---STATUS:DONE`.)

3. **On disband** — proceed to "Post-Completion: Main Agent Review and Commit" below, then **ALWAYS archive the session** (per `## Archive Session` below — `cp -r /tmp/ensemble/$RUN_ID ~/Code/_ensemble/sessions/$(date +%Y-%m-%d)--$RUN_ID` — `RUN_ID="$(cat /tmp/collab-team-id.txt)"`), and only then clean up the poller/bridge PIDs + tmux session. **The archive is mandatory for EVERY collab-group session and is a step the `/collab` skill does NOT do for you** — cleanup kills processes but not the session dir, so archive first (or at least before any prune). Don't skip it.

**Rule of thumb:** `ensemble_launch.sh` alone ≠ the `/collab` skill. The skill = **launch + watcher**. Launch via the skill when it is available; when it is not, launch via the script **and** start the watcher, to reach the identical end-result (including the disband notification). *(Documented 2026-06-23 after a session launched via the bare script and lost the disband notification — the script is a strict subset of the skill.)*

---

## Pre-Launch Checklist

Complete ALL items before launching any collab-group session.

### 1. Choose Session Type

| Type | Command | Prompt Template |
|------|---------|----------------|
| Sprint planning | `/collab sprint-planning` | `_templates/COLLAB_PROMPT_SPRINT_PLANNING.md` |
| Code review | `/collab code-review` | `_templates/COLLAB_PROMPT_CODE_REVIEW.md` |
| Roadmap rescheduling | `/collab roadmap-rescheduling` | `_templates/COLLAB_PROMPT_ROADMAP_RESCHEDULING.md` |
| Ad hoc | `/collab` | Custom prompt |

For built-in presets, see the dedicated workflow documents:
- Sprint planning: [`workflow_new_sprint_collab.md`](workflow_new_sprint_collab.md)
- Code review: [`workflow_collab_group_code_review.md`](workflow_collab_group_code_review.md)
- Roadmap rescheduling: [`workflow_roadmap_rescheduling_collab.md`](workflow_roadmap_rescheduling_collab.md)

### 2. Prepare the Prompt

1. Copy the appropriate template from `_workflows/_templates/`
2. Fill in ALL `{PLACEHOLDER}` values
3. Delete HTML comments and the instruction header
4. Write the completed prompt to the type-specific file in `/tmp/`:
   - Sprint planning → `/tmp/collab-sprint-planning.txt`
   - Code review → `/tmp/collab-code-review.txt`
   - Roadmap rescheduling → `/tmp/collab-roadmap-rescheduling.txt`
   - Ad hoc → `/tmp/collab-adhoc.txt`

   Using per-type filenames means subsequent runs of the same collab type only need to edit the project-specific details rather than regenerating the entire prompt.

### 3. Gather Context Files

Ensure all files referenced in the prompt exist and are up to date. At minimum:

- [ ] `CLAUDE.md` — project guide
- [ ] `_workflows/workflow_collab_group_agent_guidelines.md` — agent collaboration rules
- [ ] Sprint/phase files referenced in the prompt

### 4. Verify Working Tree

```bash
git status  # Must be clean — no uncommitted changes
```

---

## Launch: Built-In Preset

For sprint planning, code review, or roadmap rescheduling:

```
/collab {preset} /tmp/collab-{preset}.txt
```

Where `{preset}` is one of: `sprint-planning`, `code-review`, `roadmap-rescheduling`. The prompt file matches the preset name.

This launches a 2-party session: `codex` (LEAD) + `claude` (WORKER). The ensemble script handles:
- Agent process spawning
- Prompt delivery to both agents
- Output collection

**After launch, ALWAYS tell the user the tmux session names for direct agent access:**

```
Agent panes (for direct observation/debugging):
  tmux attach -t {team-name}-codex-1
  tmux attach -t {team-name}-claude-2
```

Where `{team-name}` is the team name printed by `collab-launch.sh` (e.g., `collab-1777787767116-5692`). The monitor TUI only shows message-bus traffic; the individual agent panes show the full agent output including file reads, tool calls, and reasoning.

**3-Minute Steer — SUSPENDED (2026-05-03):**

> **Why suspended:** The automated 3-minute queued steering reminder caused severe problems during collab-group sessions on 2026-05-02. It triggered runaway token consumption — agents would re-read files, restart discussions, and generate enormous volumes of redundant output in response to the steer. This burned through weekly usage limits and made sessions unaffordable. The feature is suspended until we can redesign the delivery mechanism or find a less disruptive formulation.

The steer message itself remains valuable — it just needs to be sent **manually by the project owner** via the tmux monitor pane (`s` key) at a moment that makes sense for the session's actual state, rather than on a fixed timer.

**After launch, print the following message for the project owner to manually send if/when appropriate:**

```
────────────────────────────────────────────────────────
MANUAL STEER (copy-paste into monitor pane `s` key when ready):

Reminder from the project owner: Take the time to fully read and discuss
the issues at hand. Critically evaluate tradeoffs, failure modes, and
opportunities to improve the design. The goal is NOT to quickly merge or
lightly rewrite existing material, but to converge on the BEST outcome
through genuine debate. Challenge each other's assumptions. Identify what's
wrong or incomplete, not just what's right.
────────────────────────────────────────────────────────
```

Use the same steer text for ALL session types (sprint planning, code review, roadmap rescheduling). Do NOT send role-specific messages — role specialization is already in the prompt. The main agent MUST NOT send this automatically; it is the project owner's decision when (or whether) to send it.

## Launch: Ad-Hoc Session

For custom collaboration tasks:

```
/collab /tmp/collab-adhoc.txt
```

Ad-hoc sessions use the same 2-party setup. The project owner may manually send a steer message via the monitor pane if desired.

---

## Monitor

The `/collab` skill provides periodic status output during the session. Key events to watch:

1. **Session started** — both agents have been spawned
2. **Mandatory reading complete** — agents confirm file reads
3. **Discussion phase** — agents exchange analysis
4. **Writing phase** — LEAD writes deliverables
5. **Review phase** — WORKER reviews deliverables
6. **Session complete** — both agents signal done

The transcript is available after the session ends.

---

## Post-Completion: Main Agent Review and Commit

The collab-group agents write files but DO NOT commit. The main agent (Claude, orchestrating the session) is responsible for reviewing all changes and committing them. This ensures quality control, keeps git history clean, and avoids token-wasteful commits by Codex.

### 1. Review All Changed Files

Run `git status` and `git diff` to see exactly what the agents wrote. Read each deliverable file in full before committing. Look for: completeness, accuracy, consistency with project conventions, and any artifacts from the collab process (e.g., `.WORKER` temp files that should be cleaned up).

### 2. Verify Deliverables Exist

Check that all expected output files were created or updated. The specific files depend on the session type:

- **Sprint planning:** `sp_{NN}--{slug}.md` and `xp_{NN}--{slug}.md` in the phase directory
- **Code review:** `REVIEW-SUMMARY--P{NN}-S{NN}.md` in the phase directory, plus code fixes
- **Roadmap rescheduling:** Updated backlog horizon files and ROADMAP.md

### 2. Run Validation

```bash
uv run pytest tests/ -v
uv run ruff check .
```

Both must pass. Even non-code sessions may accidentally modify files.

### 3. Review Session Quality

Read the transcript output and verify:
- Both agents read all mandatory files before discussion
- There was genuine adversarial discussion (not rubber-stamping)
- The WORKER reviewed deliverables after the LEAD wrote them
- The session followed the appropriate process for its type

---

## Archive Session

Archive the full session directory from `/tmp/ensemble/<RUN_ID>/` (RUN_ID = the UUID run-dir id from `/tmp/collab-team-id.txt`, NOT the `collab-<timestamp>` tmux name) to the central archive:

```bash
RUN_ID="$(cat /tmp/collab-team-id.txt)"   # the UUID run-dir id (NOT the collab-<timestamp> tmux name)
cp -r "/tmp/ensemble/$RUN_ID" ~/Code/_ensemble/sessions/$(date +%Y-%m-%d)--$RUN_ID
```

The archive location is `~/Code/_ensemble/sessions/` with naming convention `{YYYY-MM-DD}--{run-id}` (run-id = the UUID). This is the one-and-only archive directory for all collab-group sessions across all projects. The archived directory contains `messages.jsonl` (full conversation), `prompts/` (injected prompts), `summary.txt` (session summary), and `replay.html`.
---

## Report to User

After verification, provide a summary:
1. **Session type** and duration
2. **Deliverables produced** — list files created or modified
3. **Key decisions** — notable scope changes, deferrals, or disagreements resolved
4. **Validation result** — test suite and linter status
5. **Next step** — what the user should do (review deliverables, approve plan, commit, etc.)
