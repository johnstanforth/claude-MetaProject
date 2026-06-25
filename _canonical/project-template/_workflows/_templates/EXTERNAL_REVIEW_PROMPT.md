# External Review Prompt Template

> Fill in all `{PLACEHOLDER}` values before saving as `REVIEW-PROMPT--P{NN}-S{NN}.md`
> in the phase directory. Delete this header block and all HTML comments.
>
> This template is for EXTERNAL REVIEWERS (Gemini, Cursor, KimiK25, etc.).
> Do NOT confuse with `COLLAB_PROMPT_CODE_REVIEW.md`, which is the collab-group
> prompt for the internal code review session that happens AFTER external reviews.
>
> The external reviewer reads the code, writes a report, and returns it.
> They do NOT participate in three-phase discussions, they do NOT read other
> external reviews, and they do NOT make edits. Keep the prompt simple.

<!-- PLACEHOLDERS TO FILL:
  {PHASE_NN}              - Zero-padded phase number (e.g., 05)
  {SPRINT_NN}             - Zero-padded sprint number (e.g., 03)
  {SPRINT_TITLE}          - Human-readable sprint title
  {BRIEF_CONTEXT}         - 2-4 sentences on what this sprint built
  {SP_PATH}               - Path to the sprint spec file
  {XP_PATH}               - Path to the execution plan file
  {IMPL_FILES}            - Lettered list of implementation files with one-line descriptions
  {TEST_FILES}            - Lettered list of test files with one-line descriptions
  {COMMIT_LOG}            - Sprint commit log (git log --oneline)
  {REVIEW_CRITERIA}       - Sprint-specific review criteria sections
  {PHASE_DIR}             - Phase directory path for the deliverable
  {DELIVERABLE_FILENAME}  - e.g., REVIEW--{YourAgentName}-P05-S03.md
-->

---

# Code Review Request: Phase {PHASE_NN}, Sprint {SPRINT_NN} — {SPRINT_TITLE}

You are reviewing work just completed on this project. {PROJECT_CONTEXT} {BRIEF_CONTEXT}

## Your Task

Perform a thorough review measuring whether the implementation consistently and accurately reflects the execution plan, and whether the architecture is sound. Write a comprehensive analysis report.

## Documents to Read (in this order)

1. **Project context** — read the agent-info file appropriate for your agent:

   | Agent | File |
   |-------|------|
   | Claude | `CLAUDE.md` |
   | Codex | `AGENTS.md` |
   | Gemini | `GEMINI.md` |
   | Other | `CLAUDE.md` (most comprehensive) |

2. **Sprint Specification:** `{SP_PATH}`
3. **Execution Plan:** `{XP_PATH}`
4. **Implementation files** (read ALL of these):
{IMPL_FILES}
5. **Test files** (read ALL of these):
{TEST_FILES}

## Sprint Commits

```
{COMMIT_LOG}
```

## Review Criteria

{REVIEW_CRITERIA}

## Deliverable

Write your analysis to: `{PHASE_DIR}/{DELIVERABLE_FILENAME}`

Replace `{YourAgentName}` with your agent name (e.g., `Gemini`, `Cursor`, `Claude`, `Codex`, `KimiK25`).

Structure the report with clear sections matching the review criteria above. For each issue found, specify:
- **Severity:** Critical / Major / Minor / Observation
- **Location:** file path and line number or function name
- **Description:** what's wrong or concerning
- **Recommendation:** what should be changed

End with an overall assessment and top 3 items to address before proceeding.
