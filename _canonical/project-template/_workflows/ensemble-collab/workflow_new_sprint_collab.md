# Workflow: New Sprint Planning (ensemble-collab)

> Legacy ensemble-script implementation of the sprint planning collab-group.

## Overview

This workflow uses the `/collab` skill to launch a two-agent session (codex + claude) that plans a new sprint. The session produces a sprint spec (`sp_`) and an execution plan (`xp_`) through adversarial discussion — the LEAD architect defines scope while the WORKER challenges feasibility and reviews deliverables.

---

## Pre-Launch Checklist

### 1. Determine Sprint Context

Before preparing the prompt, gather:

- **Phase and sprint numbers:** What phase are we in? What sprint number is this?
- **Previous sprint outcome:** Read the previous sprint's `sp_` file for post-sprint notes and follow-ups
- **Phase goals:** Read the phase README for what this phase is trying to accomplish
- **Backlog state:** Read `_specs_and_plans/_backlog/_horizon_NEXT.md` for items ready for implementation
- **Roadmap state:** Read `_specs_and_plans/ROADMAP.md` for phase health and planned phases

### 2. Gather Requirements and Context for the User

The `{OWNER_REQUIREMENTS}` placeholder conveys **minimum requirements** (the floor) from the project owner — not scope decisions. The collab-group agents determine the full scope themselves through adversarial debate, using the backlog files, ROADMAP, phase README, and their own independent analysis. The main agent must NOT pre-decide what is in-scope or out-of-scope, as this anchors the collab-group and defeats the purpose of their discussion.

**What goes in requirements vs. what the collab-group decides:**

| Main agent / owner provides | Collab-group decides |
|------------------------------|---------------------|
| Minimum deliverables that MUST be in the sprint (the floor) | Full scope �� what else fits naturally alongside the requirements |
| Hard constraints (dependencies, blocked items, timeline) | Task breakdown, ordering, and sizing |
| Context the agents can't derive from files (owner priorities, external factors) | Whether backlog items should be pulled in, deferred, or split |

**Process:**
1. Read the NEXT horizon, ROADMAP, and previous sprint's follow-up items
2. Ask the user: "Any hard requirements or constraints for Sprint NN? The collab-group will determine full scope from the backlog."
3. If the user has requirements, include them verbatim as `{OWNER_REQUIREMENTS}`
4. If the user has no specific requirements, use a brief statement like: "No hard requirements beyond what the backlog and phase goals indicate. Determine scope through your own analysis and debate."
5. **Run the Compound Engineering Planning Check** (Stage A of [`workflow_compound_engineering.md`](../workflow_compound_engineering.md)): verify that any Compound Engineering findings from the previous sprint are visible in the backlog files the collab-group will read

**Anti-pattern to avoid:** Do NOT draft bullet points saying "Sprint should cover X, Y, Z" or "Out of scope: A, B, C." This pre-decides the scope and the collab-group will treat it as authoritative rather than debating it. The backlog files already contain carefully triaged items with clustering annotations — let the collab-group use those directly.

### 3. Prepare the Prompt

Fill in the template at `_templates/COLLAB_PROMPT_SPRINT_PLANNING.md`:

| Placeholder | How to fill |
|-------------|-------------|
| `{PHASE_NN}` | Zero-padded phase number |
| `{SPRINT_NN}` | Zero-padded sprint number |
| `{SPRINT_TITLE}` | Human-readable sprint title |
| `{SPRINT_SLUG}` | Lowercase hyphenated slug |
| `{PHASE_SLUG}` | Phase directory slug |
| `{BRIEF_CONTEXT}` | 2-3 sentences of project context (NOT scope decisions) |
| `{PRIOR_SPRINT_SUMMARY}` | What the previous sprint built |
| `{TEST_COUNT}` | Current passing test count |
| `{OWNER_REQUIREMENTS}` | Hard requirements from the owner (floor, not ceiling) — or "no hard requirements" |
| `{CONTEXT_FILES}` | Numbered list of files the agents should read |
| `{SOURCE_FILES}` | Key source files for current state |
| `{FORMAT_REFERENCE_XP}` | Path to a prior xp file as format reference |
| `{PREV_SP_PATH}` | Path to the previous sprint's sp file |

Write the filled prompt to `/tmp/collab-sprint-planning.txt`.

### 4. Verify Context Files

- [ ] `CLAUDE.md`
- [ ] `_workflows/workflow_collab_group_agent_guidelines.md`
- [ ] Phase README
- [ ] Previous sprint sp file
- [ ] `_specs_and_plans/_backlog/_horizon_NEXT.md`
- [ ] `_specs_and_plans/ROADMAP.md`
- [ ] Format reference xp file
- [ ] All source files listed in the prompt

### 5. Create Sprint Branch

```bash
# Continuing from previous sprint:
git checkout claudecode/@claude/phase{NN}-sprint{PREV}
git checkout -b claudecode/@claude/phase{NN}-sprint{NN}

# Starting a new phase (Sprint 01):
git checkout main
git checkout -b claudecode/@claude/phase{NN}-sprint01
```

### 6. Verify Working Tree

```bash
git status  # Must be clean
```

---

## Launch

```
/collab sprint-planning /tmp/collab-sprint-planning.txt
```

This launches a 2-party session: `codex` (LEAD) + `claude` (WORKER).

**After launch, tell the user the tmux session names for direct agent access:**
```
Agent panes:
  tmux attach -t {team-name}-codex-1
  tmux attach -t {team-name}-claude-2
```

**Agent roles:**
- **codex (LEAD):** Architects scope, defines tasks, writes deliverable files (sp and xp)
- **claude (WORKER):** Reads code, challenges scope decisions, verifies technical feasibility, reviews deliverables for accuracy

The ensemble script handles agent spawning, prompt delivery, and output collection.

**3-Minute Steer — SUSPENDED (2026-05-03).** See `workflow_collab_group_launch.md` for details and the manual steer text. The main agent must print the steer message for the project owner to send manually if/when appropriate — do NOT send it automatically.

---

## Monitor and Verify Deliverables

### During the Session

The `/collab` skill provides periodic status output. The sprint planning session follows this flow:

1. **Pre-planning gate** (2-3 min) — agents assess whether a coherent sprint's worth of work remains for this phase. If NO, they write a short assessment and stop without producing sp/xp files.

2. **Scope discussion** (5-10 min) — agents discuss goals, non-goals, task breakdown, and dependencies. Genuine adversarial discussion is expected.

3. **Deliverable writing** (5-10 min) — LEAD writes sp and xp files. The xp must be self-contained (all implementation details inlined, not referenced).

4. **Peer review** (3-5 min) — WORKER reviews both deliverables for accuracy and completeness.

### Expected Deliverables

If the pre-planning gate passes:

- [ ] `sp_{NN}--{slug}.md` — sprint spec (goals, non-goals, tasks, paste prompt at end)
- [ ] `xp_{NN}--{slug}.md` — execution plan (self-contained, all details inlined)

If the pre-planning gate fails (no more phase-aligned work):

- [ ] Short assessment paragraph (may be in transcript only or written to ROADMAP.md)

---

## Post-Completion: Main Agent Review and Commit

The collab-group agents write files but DO NOT commit. The main agent (Claude, orchestrating the session) must review all changes before committing. This ensures quality control and keeps git history clean.

### 1. Review Changed Files

Run `git status` and `git diff` to see exactly what the agents wrote. Read each deliverable file in full. Verify:
- Pre-planning gate was evaluated honestly
- Both agents read all mandatory files before discussion
- WORKER genuinely challenged scope decisions (not rubber-stamping)
- WORKER reviewed deliverables after LEAD wrote them
- xp file is self-contained (no "see the ADR" or "follow the schema in X")

### 2. Review Deliverables

**Sprint Spec (`sp_`):**
- Has all required sections (metadata table, goals, non-goals, tasks, paste prompt)
- Task count is reasonable (5-12 typical; more than 15 suggests splitting)
- Each task is one-commit-sized
- Paste prompt at the end references the xp file path

**Execution Plan (`xp_`):**
- Pre-execution findings are thorough
- Critical Rules include all 6 standard rules plus sprint-specific additions
- Task details are self-contained (field names, types, implementation steps inlined)
- Acceptance checklist is concrete and verifiable
- No external references that an executing agent would need to look up

### 3. Verify No Source Code Changes

Sprint planning sessions edit only markdown files. Run `git diff --name-only` and confirm no files under `app/`, `tests/`, or `migrations/` were modified. If source code was accidentally changed, investigate before committing. Do NOT run pytest or ruff — this session does not touch code and validation would waste tokens for zero diagnostic value.

### 4. Set Status to APPROVED (Hard Gate for Execution)

After the user has reviewed the sp_ and xp_ files and confirmed they are ready:

1. Update the `Status` field in the sp_ file from `PLANNING` to `APPROVED`
2. Commit the status change

```bash
# Update status in the sp_ file (the main agent edits the Status field)
git add _specs_and_plans/phase_{NN}--{slug}/sp_{NN}--{slug}.md
git commit -m "P{NN}-S{NN}-T00 Approve Sprint {NN} for execution"
```

**This is the final gate before execution.** The `workflow_execute_sprint_dev_plan.md` will check for `APPROVED` status and refuse to proceed if the sp_ still shows `PLANNING`. Do NOT set this status until the user explicitly approves.

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

Present the sprint plan for human review:

1. **Pre-planning gate result** — PROCEED or STOP (with reasoning)
2. **Sprint scope** — goals and non-goals in 2-3 sentences
3. **Task count** — number of tasks and estimated complexity
4. **Key decisions** — notable scope choices or trade-offs from the discussion
5. **Deliverable paths** — exact file paths for sp and xp
6. **Next step** — human reviews the plan, then launches execution session

**Explicitly tell the user the exact next command to run.** This is important because the user should run the execution workflow, not the xp file directly:

> To execute this sprint, launch a fresh Claude Code session and tell it:
>
> ```
> Read and follow _workflows/workflow_execute_sprint_dev_plan.md
> ```
>
> Do NOT tell the agent to read the xp file directly — the execution workflow handles finding the sprint, checking the APPROVED gate, reading the xp, and following the correct task-by-task process.
