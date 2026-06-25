# Workflow: Collab-Group Agent Guidelines

> Instructions and behavioral guidelines for AI agents participating in collaborative multi-agent discussion groups on this project.

## Quick Reference

| Item | Value |
|------|-------|
| Applies to | All agents in a collab-group (Codex, Claude, etc.) |
| Purpose | Maximize discussion quality and deliverable accuracy |
| Key principle | Discuss first, write last |
| Deliverable ownership | LEAD agent writes files only after consensus |
| Project | See [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md) and [`../CLAUDE.md`](../CLAUDE.md) for this project's identity, domain, and tech stack. |

---

## 1. Purpose

These guidelines govern how AI agents behave inside a collab-group session. You are reading this because the collab-group prompt instructed you to read this file as your first step. These are authoritative rules, not suggestions.

The goal of every collab-group is genuine collaborative discussion that produces better outcomes than any single agent working alone. The group exists specifically because multiple perspectives, challenges, and critiques improve the quality of architectural decisions, sprint plans, and other deliverables.

These guidelines are adapted from practices developed iteratively through real collab-group sessions across John's projects (March 2026 onward). They reflect observed failure modes and empirically validated practices.

---

## 2. Mandatory Reading Phase

Before any discussion begins, every agent must read the specified context files thoroughly — including BOTH efficiency rules documents:

1. **[`EFFICIENCY_RULES.md`](EFFICIENCY_RULES.md)** — general rules for all agents (E1-E10)
2. **[`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md)** — collab-group-specific rules (CE1-CE2+)

These are mandatory reading for every collab-group session, in addition to whatever files the prompt specifies.

**Rules:**
- Read ALL files listed in the prompt's mandatory reading section before posting any substantive analysis.
- Do not skim. The prompt will specify files for a reason -- understanding them fully is a prerequisite for useful discussion.
- Your first message after reading should share specific findings, not just "I've read everything and I agree."
- If the reading list includes a large document (e.g., a 1000+ line spec or ADR), read the entire document. Do not stop at the executive summary.

**Why this matters:** Sessions where agents skip reading and jump to discussion produce shallow consensus that misses important details in the source material. The strongest collab-group sessions have consistently been ones where both agents completed thorough reading passes before engaging.

---

## 3. Discuss First, Write Last

The LEAD agent must NOT write any deliverable files until genuine discussion has concluded and both agents have reached consensus on every major decision point.

**Rules:**
- Share your analysis, proposals, and concerns via team messages first.
- The LEAD agent should outline their proposed approach and explicitly invite challenge before writing anything.
- Non-LEAD agents should share their own independent analysis, not just react to the LEAD's proposal.
- Files are written only after both agents have explicitly confirmed agreement on scope, structure, and content.

**Why this matters:** Without this rule, the LEAD agent tends to read quickly and begin writing deliverables within the first few minutes, which collapses the session into a single-agent task with the other agent reduced to a rubber-stamp reviewer. This defeats the entire purpose of the collab-group.

---

## 4. Challenge Each Other

Agents must actively question, critique, and push back on each other's proposals. Agreement should be earned through argument, not assumed.

**Rules:**
- When another agent proposes something, ask "why not X instead?" before agreeing.
- Identify risks, failure modes, and downsides for every proposed item.
- If you disagree, say so clearly and explain why. Do not soften disagreements to be polite.
- If you agree, explain specifically what convinced you -- not just "sounds good."
- Ask scope questions: "Is this too much for one sprint?" / "Are we over-engineering this?" / "What will we regret if we get this wrong?"
- Play devil's advocate even on points you tentatively agree with -- stress-testing decisions produces better outcomes.

**Why this matters:** AI agents have a strong tendency toward premature agreement. Left unchecked, two agents will converge on the first reasonable-sounding proposal within 3-4 messages, producing deliverables no better than a single agent would. The most valuable collab-group sessions are the ones where agents challenged each other on scope, architecture, naming, and risk -- producing final decisions that neither agent would have reached alone.

---

## 5. Consider Risks and Downsides

For every item proposed for inclusion in a deliverable, explicitly discuss potential problems.

**Rules:**
- What could go wrong with this approach?
- What are the dependencies and ordering constraints?
- What is the minimum viable slice vs. the full vision?
- Are we over-engineering for hypothetical future needs?
- Are we under-engineering in a way we'll regret when building the next layer?
- What failure modes exist at integration boundaries?

**Why this matters:** Optimism bias is a consistent pattern in AI-generated plans. Agents tend to propose ambitious scope with insufficient attention to risk. Explicit risk discussion has caught real issues in past sessions (e.g., scope creep in sprint planning, naming conventions that would have broken execution).

---

## 6. Lead Agent Coordination

The LEAD agent has specific coordination responsibilities.

**Rules:**
- Coordinate the discussion flow: propose topics, track open questions, drive toward resolution.
- Do not dominate the conversation. Actively solicit the other agent's independent analysis.
- Maintain a running list of agreed decisions and open questions.
- Write deliverable files only after consensus (see Section 3).
- When writing, incorporate contributions from all agents, not just your own analysis.

**Non-LEAD agent (WORKER) responsibilities:**
- Provide independent analysis, not just reactions to the LEAD's proposals.
- Review all deliverables written by the LEAD for accuracy, completeness, and consistency.
- Flag errors in file naming, paths, cross-references, and content before signaling that work is concluded.
- **Do NOT write to the same deliverable files as the LEAD.** If you need to draft content for the LEAD to incorporate, write it to a temporary file with a `.WORKER` extension (e.g., `xp_03--slug.md.WORKER`). The LEAD reads your draft and incorporates it into the canonical file. This prevents conflicting cross-edits that corrupt the deliverable. The `.WORKER` files are cleaned up by the main agent after the session ends.

---

## 7. File Ownership Rules — HARD RULE

**THE RULE:**
- **LEAD agent** owns ALL canonical deliverable files (`sp_`, `xp_`, source code, review summaries).
- **WORKER agent** NEVER writes to a canonical file directly. Not even if the LEAD is "taking too long." Not even if "it's just a small change." Not even if you think you're helping.
- If the WORKER needs to draft content, write it to a file with a `.WORKER` extension (e.g., `xp_03--slug.md.WORKER`, `sidebar.py.WORKER`). The LEAD reads the `.WORKER` file and incorporates it into the canonical file. The `.WORKER` files are cleaned up by the main agent after the session.

**THE FAILURE MODE THIS PREVENTS:**
The LEAD says "I'm editing `issue_service.py` now." The LEAD starts making changes. Three seconds later, the WORKER thinks "they're taking a while, I'll just make the change myself" and starts editing the same file. Now both agents are writing to the same file simultaneously, and one agent's changes silently overwrite the other's. This has happened in at least 3 real sessions. It destroys work.

**IF YOU ARE THE WORKER AND YOU WANT TO MAKE A CHANGE:**
1. Write your proposed change to `{filename}.WORKER` (e.g., `issue_service.py.WORKER`)
2. Tell the LEAD: "I wrote my proposed edit to `issue_service.py.WORKER` — please review and incorporate into the canonical file."
3. Wait for the LEAD to confirm they incorporated it.
4. DO NOT touch the canonical file yourself. Period.

**Exception:** During code review Phase 3, the WORKER edits source files as directed by the LEAD — this is the one case where the WORKER writes to canonical files, because the LEAD explicitly directed each change.

---

## 8. Mandatory Peer Review of Deliverables

Before any agent signals that the collab-group work is concluded, the non-LEAD agent must review all written deliverables.

**Rules:**
- After the LEAD writes files, the non-LEAD agent must read them and verify:
  - File names and paths match project conventions and workflow requirements.
  - Internal cross-references (task numbers, file paths, branch names) are consistent.
  - Content accurately reflects the discussion consensus, not just one agent's initial proposal.
  - No items from the agreed scope are missing.
  - Non-goals and scope boundaries are correctly stated.
- If errors are found, flag them specifically (file, line number, what's wrong, what it should be).
- The LEAD must fix all flagged issues before the group signals completion.
- This review step is not optional -- it has caught real errors in every session where it was practiced.

**Why this matters:** Peer review of deliverables has caught file naming/path errors and stale cross-references that would have propagated into the execution session and caused failures.

---

## 9. Session Lifecycle

Auto-disband is disabled for this project's collab-group sessions. Sessions end **only** when the project owner manually disbands via the monitor TUI (`d` key). There are no trigger words or completion-pattern matching that can terminate your session.

You may use natural language freely -- words like "done", "complete", "finished" are fine in technical discussion. Focus on the substance of the work, not on avoiding specific vocabulary.

---

## 10. Scope Discipline

Be ruthless about keeping deliverables appropriately scoped.

**Rules:**
- Sprint plans should be achievable in a focused sprint. Do not try to implement an entire specification in one sprint.
- Identify the foundational layer that everything else depends on, and scope the sprint to just that.
- Explicitly list non-goals -- items that are intentionally deferred, not forgotten.
- If an item is "nice to have," it belongs in the follow-up section, not the task list.
- When in doubt about scope, prefer smaller. A well-executed narrow sprint is more valuable than an ambitious sprint that runs out of time.

---

## 11. Validation Before Signaling Ready

Before any agent signals that work is ready for review or that the session is wrapping up, the **full validation suite** must pass:

```bash
uv run pytest tests/ -v
uv run ruff check .
```

Both must pass. This is not optional -- agents must not signal completion with known test or lint failures.

**Note:** The two checks above (`pytest` and `ruff`) are the complete validation suite for this project. (mypy is optional in this build-line.)

**When to run each check:**

- **pytest** — run after each individual edit or fix, to catch regressions immediately. A test failure that goes undetected for several edits is expensive to unwind.
- **ruff** — run once at the end, after all edits are complete and pytest passes. Do NOT run ruff after each individual edit — it wastes tokens on false positives (e.g., imports flagged as "unused" mid-session that are needed by later edits). See [`EFFICIENCY_RULES.md` § E11](../EFFICIENCY_RULES.md#e11-defer-ruff-linting-to-end-of-coding-session) for the full rationale.

**Summary:** pytest catches runtime errors and must be run per-edit. ruff catches style/lint issues and should be run once at the end. Both are required before signaling completion.

---

## 12. Summary of Anti-Patterns to Avoid

These are failure modes observed in real collab-group sessions:

| Anti-Pattern | What Happens | Prevention |
|---|---|---|
| Premature writing | LEAD writes files in first 5 minutes, other agent rubber-stamps | Discuss first, write last (Section 3) |
| Shallow agreement | Both agents agree within 3 messages without challenge | Challenge each other (Section 4) |
| Scope creep | Sprint plan grows to cover an entire phase | Scope discipline (Section 10) |
| Skipped reading | Agent posts analysis based on summaries, misses key details | Mandatory reading phase (Section 2) |
| Conflicting cross-edits | Both agents write to the same file, corrupting deliverable | **HARD RULE:** WORKER never writes canonical files. Use `.WORKER` temp files (Section 7) |
| Impatient takeover | WORKER edits a file because LEAD "took too long" (3-10 seconds) | Wait. Ask via message if 2+ minutes of silence. DO NOT preemptively edit (Section 7) |
| No peer review | Deliverables contain path errors, stale references | Mandatory peer review (Section 8) |
| Premature disbanding | Session ends before edit-pass work lands | Only the project owner disbands; agents should keep working until told to stop |
| Echo chamber tail | 6-8 messages of "acknowledged" / "standing by" after work concludes | Natural outcome; project owner will disband when ready |
| Idle-time side-quests | WORKER "investigates" unsolicited topics while LEAD writes | **HARD RULE CE1:** Stand by means stand by. See [`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md) |
| Status polling | WORKER sends "still writing?" every few minutes | **HARD RULE CE2:** Acknowledge once, then wait silently. See [`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md) |
| Premature status checks | LEAD demands progress 60-90 seconds after assigning work | **HARD RULE CE3:** Wait at least 2-5 min depending on task size. See [`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md) |
| Play-by-play narration | Working agent sends "still patching..." updates every 30 seconds | **HARD RULE CE4:** Next message after "I'll notify when done" should BE the completion. See [`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md) |
