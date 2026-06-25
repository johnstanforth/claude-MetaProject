# Collab-Group Prompt Template: Adversarial Review

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
  {REVIEW_TITLE}            - Descriptive title (e.g., "Cursor Agent Architecture Review")
  {REVIEW_DATE}             - Date of the review being validated (e.g., 2026-04-05)
  {SOURCE_AGENT}            - Name of the agent that produced the review (e.g., "Cursor agent")
  {REVIEW_TYPE}             - Type of review (e.g., "architecture code review", "research report",
                              "security audit", "sprint planning analysis")
  {REVIEW_DESCRIPTION}      - 2-3 sentences describing what the review covers and its scope
  {REVIEW_FILES_LIST}       - Bulleted list of all review files to validate
  {PROJECT_CONTEXT}         - Project-specific context paragraph (tech stack, architecture, etc.)
  {SOURCE_FILES_LIST}       - For code reviews: bulleted list of source files to cross-check.
                              For non-code reviews: bulleted list of primary reference materials.
  {DELIVERABLES_LIST}       - Numbered list of -collab-response.md files to create (1:1 with review files)
  {EVIDENCE_STANDARD}       - Type-specific evidence instructions (see below)

EVIDENCE STANDARD OPTIONS:

For CODE REVIEWS, use:
  Every validation or rejection must cite specific file paths, line
  numbers, and code evidence. "The {SOURCE_AGENT} says X about router.py
  — we verified this by reading lines 82-84 and confirmed the hardcoded
  'ptterm' string" is the minimum bar. Vague agreement like "this seems
  reasonable" will be treated as a failure.

For RESEARCH REPORTS, use:
  Every validation or rejection must cite specific evidence from the
  referenced sources, data, or analysis. If the {SOURCE_AGENT} claims
  "tool X outperforms Y in benchmarks," verify by reading the actual
  benchmark data cited. If the {SOURCE_AGENT} makes architectural
  recommendations, verify the claimed benefits and tradeoffs against the
  actual codebase state and project constraints.

For OTHER REPORT TYPES, adapt the standard to match the domain. The
principle is always: PROVE your conclusion with checkable evidence.
-->

Adversarial Validation — {REVIEW_TITLE} ({REVIEW_DATE})

CONTEXT: {PROJECT_CONTEXT}

An external agent ({SOURCE_AGENT}) produced a {REVIEW_TYPE} of this
project. {REVIEW_DESCRIPTION}

YOUR MISSION is to independently and rigorously validate or reject every
claim, finding, recommendation, and assessment in those reports by
cross-checking against primary sources.

THIS IS ADVERSARIAL VALIDATION. You are NOT here to agree with the
{SOURCE_AGENT}. You are here to PROVE OR DISPROVE its claims. Your work
will be submitted for review by other AI agents and by the human project
owner. You will be judged VERY HARSHLY if you:
- Agree too easily with invalid or imprecise claims
- Fail to verify claims against primary sources
- Miss important issues the {SOURCE_AGENT} overlooked
- Fail to propose BETTER alternatives where they exist
- Cite inaccurate line numbers, file paths, or evidence references

EVIDENCE STANDARD:
{EVIDENCE_STANDARD}

ACCURACY OF YOUR OWN REFERENCES IS CRITICAL: Your response files will
themselves be evaluated by downstream agents who will cross-check YOUR
line numbers, file paths, and citations. If you cite "line 82" but the
relevant code is actually at line 97, that error will be flagged and
will undermine your entire analysis. Double-check every reference you
include.

MANDATORY READING BEFORE ANY DISCUSSION:
1. Read the collaboration guidelines document at
   `_workflows/workflow_collab_group_agent_guidelines.md`
   — this contains the rules for how you must collaborate in this session.
   Read it fully before proceeding to any other reading.
1b. Read your role-specific behavioral contract:
   - codex-1 (LEAD): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_LEAD.md`
   - claude-2 (WORKER): Read the DO NOT EDIT section of
     `_workflows/_templates/COLLAB_ROLE_WORKER.md`

THEN — PASS 1 (Form Independent Opinions):
2. Read ALL of the {SOURCE_AGENT}'s review files to form your own
   overall opinions BEFORE discussing any specific file:
{REVIEW_FILES_LIST}
3. Read the project's CLAUDE.md for overall project context and constraints.

THEN — Read the primary source materials that the {SOURCE_AGENT}
references. You MUST read these to verify claims:
{SOURCE_FILES_LIST}

TASK — PASS 2 (File-by-File Validation):

After both agents have read everything and shared their initial overall
impressions, proceed to validate each review file one at a time.
For EACH review file, the team must:

A) Go through EVERY claim, finding, severity rating, and recommendation
   in the file, point by point.

B) For each claim:
   - READ the primary source material referenced
   - VERIFY whether the claim is factually accurate
   - ASSESS whether the severity rating is appropriate
   - EVALUATE whether the recommendation is the BEST approach, or
     whether a BETTER alternative exists
   - If the claim is WRONG or MISLEADING, explain exactly why with
     primary source evidence
   - If the claim is VALID but the recommendation is suboptimal,
     propose a better approach

C) ADDITIONALLY, for each file's scope:
   - Identify issues the {SOURCE_AGENT} MISSED entirely
   - Propose improvements neither the {SOURCE_AGENT} nor the current
     state has considered
   - Note any claims that may have been true when the review was written
     but have changed since (check git log if needed)

D) Write a response file with the codex-1 LEAD agent's pen.

DELIVERABLES (written by codex-1 ONLY after thorough discussion of each):

For each review file, write a corresponding response file with
`-collab-response` appended to the original filename:

{DELIVERABLES_LIST}

EACH RESPONSE FILE MUST contain:
- A header identifying the review file being validated
- Date and agent composition
- For EVERY claim/finding in the review file:
  - The original claim (quoted or paraphrased)
  - VERDICT: VALIDATED / REJECTED / PARTIALLY VALID / NEEDS CONTEXT
  - EVIDENCE: Specific references (file paths + line numbers for code
    reviews; source citations for research; data references for analyses)
  - SEVERITY ASSESSMENT: Agree/disagree with the {SOURCE_AGENT}'s rating
  - BETTER ALTERNATIVE (if applicable): A superior approach with rationale
- A section for MISSED ISSUES not identified in the review
- A section for ADDITIONAL RECOMMENDATIONS beyond what either the current
  state or the {SOURCE_AGENT} has considered
- An overall assessment of the review file's accuracy and utility

PROCESS — How to work through the files:

1. Both agents share their overall impressions from Pass 1 reading
2. Discuss areas of agreement and disagreement at a high level
3. Then, for each file (in order):
   a. Claude (WORKER) shares their detailed point-by-point analysis
   b. Codex (LEAD) shares their independent point-by-point analysis
   c. They debate every point of disagreement aggressively
   d. They converge on consensus for each claim
   e. Codex (LEAD) writes the -collab-response.md file
   f. Claude (WORKER) reviews the written file for accuracy and
      VERIFIES that all cited line numbers and file paths are correct
   g. Any corrections are made before moving to the next file
4. After all files are written, both agents do a final cross-check
   to ensure consistency across all response files

SCOPE: This is a READ-ONLY validation exercise. Do NOT modify any
source code or primary materials. Do NOT modify the {SOURCE_AGENT}'s
original review files. Only CREATE the new -collab-response.md files.

<!-- For code reviews, include this additional scope note:
SCOPE NOTE FOR CODE REVIEWS: When verifying code claims, read the
actual source files line by line. Do not rely on summaries or your
prior knowledge of the codebase — the {SOURCE_AGENT} may have read
a different version of a file, or may have misidentified line numbers.
Your own line-number citations must be accurate to the current HEAD.
-->

QUALITY BAR: Your output will be reviewed by other AI agents and by
the project owner as part of a multi-stage evaluation pipeline. Every
claim you validate or reject must be backed by specific, checkable
evidence. Lazy agreement is worse than honest disagreement. If the
{SOURCE_AGENT} got something wrong, SAY SO and prove it. If the
{SOURCE_AGENT} missed something important, FIND IT and document it.
If you can think of a better approach than what either the current
state or the {SOURCE_AGENT} proposes, INCLUDE IT with full rationale.

CRITICAL REMINDERS (these are repeated here because they are non-negotiable):

- DISCUSS FIRST, WRITE LAST. The LEAD agent must NOT write any response
  files until AFTER thorough discussion and genuine consensus on that
  specific file's findings. Both agents must share independent analysis
  and challenge each other's assessments BEFORE any files are written.

- MANDATORY PEER REVIEW: After the LEAD writes each response file, the
  WORKER agent MUST review it for accuracy — especially verifying that
  all cited line numbers, file paths, and evidence references are correct
  — before the team moves on to the next file. Every response file must
  reflect the genuine consensus of BOTH agents, not just one agent's view.

- CHALLENGE EVERYTHING: Do not assume the {SOURCE_AGENT} is correct just
  because it wrote something confidently. Do not assume each other is
  correct just because a point sounds reasonable. VERIFY against primary
  sources. DEBATE the implications. PROVE your conclusions.
