# Collab-Group Prompt Template: Post-Sprint Code Review

> Fill in all `{PLACEHOLDER}` values before writing to `/tmp/collab-prompt.txt`.
> Delete this header block and all HTML comments before launching.

---

<!-- INSTRUCTIONS FOR THE MAIN AGENT:

1. Copy everything below the --- line
2. Replace all {PLACEHOLDERS} with actual values
3. Delete HTML comments
4. Write to /tmp/collab-prompt.txt
5. Launch with: _research/_ensemble/ensemble_launch.sh /tmp/collab-prompt.txt

PLACEHOLDERS TO FILL:
  {PHASE_NN}              - Zero-padded phase number (e.g., 04)
  {SPRINT_NN}             - Zero-padded sprint number (e.g., 03)
  {SPRINT_TITLE}          - Human-readable sprint title
  {PHASE_SLUG}            - Phase directory slug (e.g., multiagent_collaboration)
  {BRIEF_CONTEXT}         - 2-3 sentences on what this sprint built
  {XP_PATH}               - Full path to the sprint's xp file
  {IMPL_FILES}            - Lettered list (a-p) of all implementation files changed
  {TEST_FILES}            - Lettered list (a-k) of all test files changed
  {REVIEW_FILES}          - Paths to external review reports (REVIEW--*-P{NN}-S{NN}.md)
  {REVIEW_CRITERIA}       - Sprint-specific review criteria bullet points
-->

{SPRINT_TITLE} — POST-SPRINT CODE REVIEW AND FIXES

CONTEXT: You are reviewing code just implemented in Sprint {SPRINT_NN}
of Phase {PHASE_NN}. {PROJECT_CONTEXT}

{BRIEF_CONTEXT}

MANDATORY READING BEFORE ANY DISCUSSION:
1. Read `_workflows/workflow_collab_group_agent_guidelines.md`
   — collaboration rules for this session.
2. Read your role-specific behavioral contract:
   - codex-1 (LEAD): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_LEAD.md`
   - claude-2 (WORKER): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_WORKER.md`
3. Read the sprint execution plan:
   `{XP_PATH}`
4. Read ALL implementation files:
{IMPL_FILES}
5. Read ALL test files:
{TEST_FILES}

NOTE: Do NOT read any external review reports (REVIEW--*-sprint_*.md)
yet. You will read them in Phase 2 AFTER forming your own independent
assessment in Phase 1. This prevents anchoring bias from external
reviewers' opinions.

TASK: Review all implemented code against the xp specification, then
incorporate external reviews, then apply fixes. Three phases.

REVIEW CRITERIA (for Phase 1):
- Does the code accurately implement what the xp specifies?
{REVIEW_CRITERIA}
- Are field names, types, and defaults consistent across models,
  migrations (Alembic), services, and templates?
- Does the architecture follow project conventions (Quart app factory,
  Blueprints, async SQLAlchemy 2.0 sessions, pydantic-settings config,
  Jinja2 templates, clean Postgres-portable schema)?
- Are async boundaries correct (no blocking I/O on the event loop;
  external calls — Gmail API, HTTP — awaited or run in an executor;
  background/scheduled tasks cancel cleanly)?
- Are tests meaningful and do they cover key invariants?
- Did the sprint stay within its stated scope?

ROLE SPECIALIZATION:
- codex-1 (LEAD): Review, analyze, direct edits. Do NOT edit files yourself.
  Follow the LEAD behavioral contract you read above. In Phase 3, you are
  the approval gate for every edit claude-2 makes — check design against
  failure modes and boundary conditions, verify that tests exercise
  intended semantics rather than merely matching the implementation, and
  require changes if the patch is technically correct but unnecessarily
  brittle or shallow.
- claude-2 (WORKER): Discuss, challenge, then make ALL file edits when
  directed by codex-1 (Phase 3 only). codex-1 approves each edit. Follow
  the WORKER behavioral contract you read above — especially: investigate
  the code independently with structured findings before Phase 1
  discussion, verify all claims against source code, and conduct peer
  review of the REVIEW-SUMMARY using PASS/FLAG/ISSUE format.

FILE OWNERSHIP — HARD RULE:
DO NOT EDIT THE OTHER AGENT'S FILES. ONLY ONE AGENT WRITES TO ANY GIVEN
FILE AT A TIME. If the LEAD is editing a file, the WORKER must WAIT —
even if the LEAD takes 10, 20, or 30 seconds. DO NOT "help" by editing
the same file. If you are the WORKER and want to propose a change, write
it to a `.WORKER` temp file (e.g., `sidebar.py.WORKER`) and tell the
LEAD to incorporate it. If the LEAD seems stalled (2+ minutes of silence),
ASK via message — do NOT preemptively take over their file.

PROCESS (three phases, strictly in order):

PHASE 1 — INDEPENDENT REVIEW: Both agents read the xp and all code/test
files thoroughly. Then discuss findings item-by-item based on YOUR OWN
analysis only. Challenge each other's assessments. Categorize each finding
by severity (Critical / Major / Minor / Observation). Do NOT read the
external review yet. Do NOT make any file edits. Build a shared list of
agreed findings before moving to Phase 2.

IMPORTANT: At the end of Phase 1, the LEAD agent must WRITE the
consensus findings to the review summary file:
  {PHASE_DIR}/REVIEW-SUMMARY--P{PHASE_NN}-S{SPRINT_NN}.md
The summary must include: assigned IDs (C1, M1, M2, m1, o1, etc.),
severity, and one-line description for each finding. This file serves
as both the session checkpoint and the permanent record of the review.

PHASE 2 — EXTERNAL REVIEW ANALYSIS: Now read the external review reports:
{REVIEW_FILES}
Read ALL available review reports. Discuss each external finding
item-by-item. For each one, reach consensus:
  - AGREE: The finding is valid and verified against the source code.
    Cite the file path and line number(s) that confirm it.
  - DISAGREE: The finding is invalid or incorrect. Cite the specific
    file path and line number(s) that disprove the claim. If the
    reviewer cited evidence that does not exist (e.g., test functions,
    file paths, or line numbers that are fabricated), flag this
    explicitly — hallucinated evidence is a distinct and serious
    failure mode, not merely a "false positive."
  - PARTIALLY AGREE: The finding identifies a real issue but the
    characterization, severity, or recommended fix is wrong. Cite the
    evidence for what's accurate and what's not.
Do NOT make any file edits during Phase 2. Conclude the external review
discussion and produce a final consolidated findings list before Phase 3.

IMPORTANT: At the end of Phase 2, the LEAD agent must UPDATE the
review summary file with:
1. A CONSOLIDATED FINDINGS LIST merging Phase 1 and Phase 2 results.
   Each item: ID, severity, description, whether from Phase 1 or
   added from external reviews, any reclassifications.
2. An EXTERNAL REVIEWER REPORT CARD section that evaluates each
   external reviewer's performance:
   - What they correctly identified (hits)
   - What they missed that the collab-group found (misses)
   - What they flagged that was incorrect or not a real issue (false positives)
   - What evidence they fabricated (hallucinations) — cited test names,
     function names, file paths, or line numbers that do not exist in
     the codebase. This is categorically worse than false positives and
     indicates the reviewer cannot be trusted for verification tasks.
   - Overall assessment of each reviewer's accuracy and thoroughness
   This gives the project owner a performance evaluation of each
   external review agent for calibration purposes.
The updated file is the authoritative input for Phase 3 edits.

PHASE 3 — FIXES: After full review consensus from Phases 1 and 2,
codex-1 directs claude-2 to make specific code edits. For each fix:
  1. codex-1 describes the exact change needed (file, location, what
     to change and why)
  2. claude-2 implements the change
  3. claude-2 runs pytest to verify no regressions
  4. codex-1 verifies the change matches the consensus

After ALL fixes are applied, claude-2 runs the FULL validation suite
one final time (ruff is deferred to this point per EFFICIENCY_RULES.md
§ E11 — running it per-fix wastes tokens on false positives like
imports that appear "unused" mid-session but are needed by later fixes):
  uv run pytest tests/ -v
  uv run ruff check .
BOTH must pass before codex-1 does the final verification pass.
Do not signal readiness without clean validation.

NOTE: The REVIEW-SUMMARY and EXTERNAL REVIEWER REPORT CARD produced
in this session will be evaluated by downstream agents as part of the
project's multi-stage quality pipeline. Ensure all line-number
citations and file-path references are accurate and verifiable.

GIT — HARD RULE:
DO NOT run git add or git commit. Write your deliverable files only.
The main agent (orchestrating this session) will review all changes
and handle git commits after the session concludes.

CRITICAL REMINDERS:
- THREE PHASES, STRICTLY IN ORDER. No reading the external review during
  Phase 1. No file edits until Phase 3.
- MANDATORY VERIFICATION: After all edits in Phase 3, codex-1 must verify
  the final state of all changed files matches the review consensus.
- DISCUSS FIRST, EDIT LAST. Both agents must share independent analysis
  and challenge each other's assumptions in Phases 1 and 2 BEFORE any
  file edits happen in Phase 3.
- APPROVAL GATE: claude-2 makes all file edits. codex-1 reviews and
  approves each edit — checking design quality, failure modes, boundary
  conditions, and test correctness. codex-1 must require changes if
  an edit is technically correct but brittle, shallow, or does not match
  the review consensus.
