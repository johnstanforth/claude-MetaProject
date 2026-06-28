# Collab-Group Prompt Template: Sprint Planning

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
  {PHASE_NN}              - Zero-padded phase number (e.g., 04)
  {SPRINT_NN}             - Zero-padded sprint number (e.g., 04)
  {SPRINT_TITLE}          - Human-readable sprint title
  {SPRINT_SLUG}           - Lowercase hyphenated slug (e.g., workspace-ux-and-agent-context)
  {PHASE_SLUG}            - Phase directory slug (e.g., multiagent_collaboration)
  {BRIEF_CONTEXT}         - 2-3 sentences of project context (NOT scope decisions)
  {PRIOR_SPRINT_SUMMARY}  - What the previous sprint built (2-3 sentences)
  {TEST_COUNT}            - Current passing test count
  {OWNER_REQUIREMENTS}    - Hard requirements from owner (floor, not ceiling) or "no hard requirements"
  {CONTEXT_FILES}         - Numbered list of files the agents should read (items 2+)
  {SOURCE_FILES}          - Numbered list of key source files for current state
  {FORMAT_REFERENCE_XP}   - Path to a prior xp file to use as format reference
  {PREV_SP_PATH}          - Path to the previous sprint's sp file
-->

PHASE {PHASE_NN}, SPRINT {SPRINT_NN} PLANNING — {SPRINT_TITLE}

CONTEXT: You are planning Sprint {SPRINT_NN} of Phase {PHASE_NN}
for this project. {PROJECT_CONTEXT}

{PRIOR_SPRINT_SUMMARY}

{BRIEF_CONTEXT}

{TEST_COUNT}+ tests currently pass.

MANDATORY READING BEFORE ANY DISCUSSION:
1. Read `_workflows/workflow_collab_group_agent_guidelines.md`
   — collaboration rules for this session.
2. Read your role-specific behavioral contract:
   - codex-1 (LEAD): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_LEAD.md`
   - claude-2 (WORKER): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_WORKER.md`
{CONTEXT_FILES}

Also read as FORMAT REFERENCE for the execution plan:
   {FORMAT_REFERENCE_XP}

Read key source files for current state:
{SOURCE_FILES}

TASK: Plan Sprint {SPRINT_NN} — but FIRST, run the pre-planning gate
below. If the gate says STOP, do NOT plan a sprint. If the gate says
PROCEED, continue to scope discussion and deliverables.

PRE-PLANNING GATE (run this BEFORE any scope discussion):
1. Read the Phase README goals/scope section.
2. Read the ROADMAP.md "Phase completion criteria" and "Phase assessment"
   note (if one exists) for the current phase.
3. Check the NEXT and LATER horizons for items that align with this
   phase's goals.
4. Answer: "Is there a coherent sprint's worth of work remaining that
   aligns with this phase's goals?"
   - If a recent Phase assessment note in ROADMAP.md says RECOMMEND
     TRANSITION, answer NO unless you see clear phase-aligned work
     that the assessment missed.
   - If a recent note says WINDING DOWN, proceed but note this may be
     the final sprint for this phase.
   - Consider LATER items too — if NEXT is thin but LATER has items
     that could be pulled forward for this phase, that counts.
   - Cross-phase items (bug fixes, polish unrelated to phase goals)
     alone do NOT justify continuing the phase.
5. If YES — state your reasoning briefly, then proceed to scope
   discussion and planning below.
6. If NO — both agents must discuss and converge on this verdict. Then
   write a short assessment (5-10 lines) explaining:
     - What has been delivered against phase goals
     - What remains (if anything)
     - Your recommendation: run the rescheduling workflow to assess
       phase transition
   Do NOT write sp_ or xp_ files. Signal that work is concluded after
   writing the assessment.

OWNER REQUIREMENTS (minimum deliverables — the floor, not the ceiling):
{OWNER_REQUIREMENTS}

SCOPE DETERMINATION — YOUR JOB, NOT THE OWNER'S:
The backlog files you read above (NEXT, LATER, SOMEDAY horizons) were
carefully triaged by a prior collab-group with clustering annotations.
YOUR job is to determine the full sprint scope through independent
analysis and adversarial debate. The owner requirements above set the
MINIMUM — you must include those. But the CEILING is yours to decide:
pull in additional backlog items, defer items that don't fit, split
items across sprints, or identify natural clusters. Do NOT treat the
owner requirements as the complete scope — they are the floor. Do NOT
defer to the main agent's framing of what "should" be in this sprint.
Read the backlog, read the code, debate each other, and converge on
the scope that produces the best sprint.

DELIVERABLE FILE NAMING (follow these EXACTLY):
- Sprint spec: _stages_and_phases/phase_{PHASE_NN}--{PHASE_SLUG}/sp_{SPRINT_NN}--{SPRINT_SLUG}.md
- Execution plan: _stages_and_phases/phase_{PHASE_NN}--{PHASE_SLUG}/xp_{SPRINT_NN}--{SPRINT_SLUG}.md
- Both files go FLAT in the phase directory (NO sprint subdirectory)

Sprint branch: claudecode/@claude/phase{PHASE_NN}-sprint{SPRINT_NN}
Commit prefix: P{PHASE_NN}-S{SPRINT_NN}-T{NN}

CRITICAL: The execution plan (xp) must be SELF-CONTAINED. An executing
agent must be able to implement every task by reading only the xp file.
Do NOT write "implement the model from the ADR" or "follow the schema
in the research doc." Instead, INLINE all field names, types, enums,
DDL, config shapes, and implementation details directly into the xp
task descriptions. If the source material defines a 15-field data model,
all 15 fields must appear in the xp.

CONTEXT AND SCOPE BOUNDARIES: The xp must begin with a
"## Context and Scope Boundaries" section as its FIRST content section.
Write one solid paragraph setting overall perspective (what this sprint
does, what it must NOT touch, key constraints), then add a
"### Scope Boundary To Preserve" list and a "### Critical Rules" list.
This section is the first thing the executing agent reads. There is NO
Paste Prompt — the executing agent finds the xp directly.

ROLE SPECIALIZATION:
- codex-1 (LEAD): Architect scope, define tasks, write deliverable files.
  Do NOT let claude-2 write the deliverable files. Follow the LEAD
  behavioral contract you read above — especially: open with structure
  not conclusions, ask the WORKER to pressure-test specific areas,
  change position explicitly when evidence warrants it, and hold for
  genuine peer review before treating deliverables as settled.
- claude-2 (WORKER): Read code, challenge scope decisions, verify
  technical feasibility, review deliverables for accuracy. Follow the
  WORKER behavioral contract you read above — especially: investigate
  independently with structured mini-reports, verify all claims against
  source code, discover gaps the LEAD and prompt both missed, and
  conduct peer review as a quality gate using PASS/FLAG/ISSUE format.

DELIVERABLE WRITING ORDER — INTERLEAVED REVIEW:
The LEAD should write the sp_ file FIRST and send it for peer review
immediately, THEN write the xp_ file. Do NOT batch both files and
block the WORKER for the entire duration. The sp_ is shorter and
defines scope — catching a scope error early avoids wasting tokens on
an xp_ that would need to be rewritten. The WORKER reviews the sp_
while the LEAD writes the xp_, then reviews the xp_ and checks
cross-file consistency when it arrives. While writing, do NOT send
progress updates — just send the review request when each file is
ready (see EFFICIENCY_RULES_COLLAB.md CE4).

FILE OWNERSHIP — HARD RULE:
DO NOT EDIT THE OTHER AGENT'S FILES. ONLY ONE AGENT WRITES TO ANY GIVEN
FILE AT A TIME. The LEAD owns all canonical deliverable files (sp_, xp_).
The WORKER NEVER writes to canonical files directly. If the WORKER wants
to draft content, write it to a `.WORKER` temp file (e.g.,
`xp_03--slug.md.WORKER`). The LEAD reads the draft and incorporates it.
If the LEAD seems slow, WAIT — do NOT preemptively take over their file.

GIT — HARD RULE:
DO NOT run git add or git commit. Write your deliverable files only.
The main agent (orchestrating this session) will review all changes
and handle git commits after the session concludes.

CRITICAL REMINDERS:
- DISCUSS FIRST, WRITE LAST. The LEAD agent must NOT write any deliverable
  files until AFTER thorough discussion and genuine consensus. Both agents
  must share independent analysis and challenge each other's assumptions
  BEFORE any files are written.
- MANDATORY PEER REVIEW: After the LEAD writes deliverables, the non-LEAD
  agent MUST review all files before signaling that work is concluded.
