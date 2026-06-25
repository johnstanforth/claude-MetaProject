# Collab-Group Prompt Template: Roadmap Rescheduling

> Fill in all `{PLACEHOLDER}` values before writing to `/tmp/collab-prompt.txt`.
> Delete this header block and all HTML comments before launching.

---

<!-- INSTRUCTIONS FOR THE MAIN AGENT:

1. Copy everything below the --- line
2. Replace all {PLACEHOLDERS} with actual values
3. Delete HTML comments
4. Write to /tmp/collab-prompt.txt
5. Launch with: _research/_ensemble/ensemble_launch.sh /tmp/collab-prompt.txt
6. Print the manual steer text for the project owner (see workflow_collab_group_launch.md)

PLACEHOLDERS TO FILL:
  {UNSORTED_COUNT}      - Number of items in the UNSORTED_QUEUE
  {TEST_COUNT}          - Current passing test count
  {PHASE_NN}            - Current phase number (e.g., 04)
  {SPRINT_NN}           - Most recent sprint number (e.g., 04)
  {BRIEF_STATUS}        - 2-3 sentences on current project state
  {RECENT_SP_PATH}      - Path to the most recent sprint's sp file
  {PHASE_README_PATH}   - Path to the current phase's README
-->

ROADMAP RESCHEDULING — HOLISTIC BACKLOG REPRIORITIZATION

CONTEXT: You are performing a full roadmap rescheduling for this
project. {PROJECT_CONTEXT}
{BRIEF_STATUS}
The UNSORTED_QUEUE has {UNSORTED_COUNT} items that need to be sorted
into horizons. {TEST_COUNT}+ tests currently pass.

MANDATORY READING BEFORE ANY DISCUSSION:
1. Read `_workflows/workflow_collab_group_agent_guidelines.md`
   — collaboration rules for this session.
2. Read your role-specific behavioral contract:
   - codex-1 (LEAD): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_LEAD.md`
   - claude-2 (WORKER): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_WORKER.md`
3. Read `CLAUDE.md` (project context, architecture, conventions)
4. Read `_specs_and_plans/ROADMAP.md` (authoritative project status)
5. Read `{PHASE_README_PATH}` (current phase goals, sprint history)
6. Read `{RECENT_SP_PATH}` (most recent sprint — follow-ups and closeout notes)
7. Read ALL four backlog files:
   a. `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md`
   b. `_specs_and_plans/_backlog/_horizon_NEXT.md`
   c. `_specs_and_plans/_backlog/_horizon_LATER.md`
   d. `_specs_and_plans/_backlog/_horizon_SOMEDAY.md`

TASK: Review the entire project backlog, roadmap, and phase state.
Determine what has been implemented, what remains, and how to organize
the forward plan. Produce updated versions of all backlog horizon files,
the ROADMAP, and phase assessment.

PROCESS:
1. READ all listed files thoroughly.

2. PHASE HEALTH CHECK — Assess the current phase before sorting items.
   Read the current Phase README (goals, scope, sprint history) and the
   ROADMAP.md "Phase completion criteria" and "Phase N outcome so far"
   sections. Compare stated goals against delivered outcomes. Produce a
   one-paragraph assessment with one of three verdicts:
     - ACTIVE: significant work remains aligned with this phase's goals
     - WINDING DOWN: remaining items are thin; 1-2 more sprints at most
     - RECOMMEND TRANSITION: phase goals are substantially met; recommend
       the user plan the next phase
   Both agents must discuss and converge on this verdict before
   proceeding. Record the verdict and reasoning — it will be written
   into ROADMAP.md as a timestamped "Phase assessment" note.

3. IDENTIFY items that have already been implemented (cross-reference
   against CLAUDE.md phase/sprint history and phase READMEs).
4. SORT all UNSORTED_QUEUE items into NEXT, LATER, or SOMEDAY.
   Remove them from UNSORTED_QUEUE as you sort them.
5. RE-EVALUATE existing NEXT/LATER/SOMEDAY items — promote, demote,
   or archive as appropriate given current project state.
6. ANNOTATE items that cluster naturally together with a brief note
   (e.g., "clusters with X and Y for a natural sprint"). Do NOT
   produce formal sprint specs.
7. REFRESH PLANNED PHASES — Review the Planned Phases section in
   ROADMAP.md. Are the descriptions still accurate given what was
   learned during the current phase? Did current-phase work change
   what the next phase should focus on? Update descriptions and
   bullet points to reflect current understanding. Also review and
   update the "Phase completion criteria" for the current phase and
   any upcoming phases.
8. UPDATE ROADMAP.md to reflect current reality: phase assessment
   note, backlog summary counts, refreshed planned phases.

OUTPUT FORMAT for horizon files:
- Active items at the top, organized by category
- Each item: one-line title + description, source reference if known
- "Previous Items with Disposition" section at the bottom with
  one-line entries: "- {Title} — {disposition} ({reference})"
  Example: "- Agent context injection — implemented in P04-S04 (T05-T07)"

UNSORTED_QUEUE must be EMPTY after this process. Every item either
moves to a horizon or gets archived with a disposition note.

DELIVERABLES (written by codex-1 ONLY after full discussion):
- `_specs_and_plans/_backlog/_UNSORTED_QUEUE.md` (should be empty except header)
- `_specs_and_plans/_backlog/_horizon_NEXT.md`
- `_specs_and_plans/_backlog/_horizon_LATER.md`
- `_specs_and_plans/_backlog/_horizon_SOMEDAY.md`
- `_specs_and_plans/ROADMAP.md` (phase assessment note, backlog summary, refreshed planned phases)

ROLE SPECIALIZATION:
- codex-1 (LEAD): Analyze, propose sorting, write updated files.
  Do NOT let claude-2 write the deliverable files. Follow the LEAD
  behavioral contract you read above — especially: open with structure
  not conclusions, ask the WORKER to pressure-test sorting decisions,
  and change position when the WORKER presents evidence that an item
  belongs in a different horizon.
- claude-2 (WORKER): Read all files, challenge sorting proposals,
  verify implemented-vs-remaining, review deliverables for accuracy.
  Follow the WORKER behavioral contract you read above — especially:
  independently verify which items have been implemented by reading
  source code, challenge horizon placements with evidence, and conduct
  peer review of updated horizon files using PASS/FLAG/ISSUE format.

FILE OWNERSHIP — HARD RULE:
DO NOT EDIT THE OTHER AGENT'S FILES. ONLY ONE AGENT WRITES TO ANY GIVEN
FILE AT A TIME. The LEAD owns all canonical deliverable files. The WORKER
NEVER writes to canonical files directly. If the WORKER wants to draft
content, write it to a `.WORKER` temp file. The LEAD reads the draft and
incorporates it. If the LEAD seems slow, WAIT — do NOT take over.

GIT — HARD RULE:
DO NOT run git add or git commit. Write your deliverable files only.
The main agent (orchestrating this session) will review all changes
and handle git commits after the session concludes.

CRITICAL REMINDERS:
- DISCUSS FIRST, WRITE LAST. The LEAD agent must NOT write any
  deliverable files until AFTER thorough discussion and genuine
  consensus. Both agents must share independent analysis and
  challenge each other's assumptions BEFORE any files are written.
- MANDATORY PEER REVIEW: After the LEAD writes deliverables, the
  non-LEAD agent MUST review all files before signaling that work
  is concluded.
