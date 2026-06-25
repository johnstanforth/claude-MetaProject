# Efficiency Rules

> Hard rules for minimizing token waste and maximizing the value of every Claude Code session. These rules are **mandatory reading** — referenced from CLAUDE.md and enforced in every session.

## Why This Document Exists

Token usage directly maps to subscription limits (5-hour rolling window, weekly cap on Claude Max). Every wasted token shortens the working session and reduces the total work that can be accomplished. These rules codify trial-and-error lessons from real sessions where specific patterns were observed to waste tokens without producing proportional value.

This document is a living reference. When a new efficiency problem is identified during a session, add it here as part of the Compound Engineering Stage B review (see `workflow_compound_engineering.md`). The goal is to make each session more efficient than the last — the same compounding principle that drives the rest of our workflow system.

**Collab-group agents:** In addition to this document, collab-group sessions have their own supplementary efficiency rules in [`EFFICIENCY_RULES_COLLAB.md`](EFFICIENCY_RULES_COLLAB.md). Both documents are mandatory reading for collab-group agents.

---

## Rule Index

| # | Rule | Category | Added |
|---|------|----------|-------|
| E1 | [Never duplicate subagent work](#e1-never-duplicate-subagent-work) | Subagents | 2026-05-04 |
| E2 | [Wait for subagents before acting on their topic](#e2-wait-for-subagents-before-acting-on-their-topic) | Subagents | 2026-05-04 |
| E3 | [Don't re-read files already in context](#e3-dont-re-read-files-already-in-context) | File I/O | 2026-05-04 |
| E4 | [Parallelize independent tool calls](#e4-parallelize-independent-tool-calls) | Tool use | 2026-05-04 |
| E5 | [Don't narrate what you're about to do in detail](#e5-dont-narrate-what-youre-about-to-do-in-detail) | Output | 2026-05-04 |
| E6 | [Stop and ask rather than guess-and-redo](#e6-stop-and-ask-rather-than-guess-and-redo) | Decision making | 2026-05-04 |
| E7 | [Don't generate alternatives the user didn't ask for](#e7-dont-generate-alternatives-the-user-didnt-ask-for) | Scope | 2026-05-04 |
| E8 | [Two-attempt rule: stop after 2 failed fixes](#e8-two-attempt-rule-stop-after-2-failed-fixes) | Error recovery | 2026-05-04 |
| E9 | [Use system operations instead of LLM-context operations](#e9-use-system-operations-instead-of-llm-context-operations) | Subagents / File I/O | 2026-05-04 |
| E10 | [Don't silently repeat an expensive workaround](#e10-dont-silently-repeat-an-expensive-workaround) | Decision making | 2026-05-04 |
| E11 | [Defer ruff linting to end of coding session](#e11-defer-ruff-linting-to-end-of-coding-session) | Validation | 2026-05-04 |

---

## E1: Never Duplicate Subagent Work

**HARD RULE.** When you dispatch a background subagent to perform a task, do NOT start doing that same task yourself "while waiting." This doubles token consumption for zero additional value.

**The failure pattern:**
1. Agent dispatches a subagent to research topic X
2. Agent says "Let me quickly check for X myself while waiting"
3. Both the subagent AND the main agent burn tokens researching X
4. The subagent's results arrive but the main agent has already done the work
5. Net result: 2x tokens spent, no time saved (the human barely notices the few seconds of wait time)

**The correct pattern:**
1. Dispatch the subagent
2. Work on a **genuinely different** task that doesn't overlap with the subagent's scope — or simply wait
3. When the subagent completes, use its results

**What counts as "genuinely different":** If the main agent's work and the subagent's work will produce overlapping information, it's duplication. If they're truly independent (e.g., subagent researches online while main agent audits local files on a different topic), parallel work is fine.

**When in doubt:** Wait. The cost of a 30-second idle period is negligible. The cost of duplicating a 10-minute research task is not.

---

## E2: Wait for Subagents Before Acting on Their Topic

When a subagent is dispatched to gather information that will inform the next step, do NOT proceed with that next step using partial information. Wait for the subagent to complete, then proceed with complete information.

**The failure pattern:**
1. Dispatch subagent to research best practices for X
2. Start writing the implementation based on what you already know about X
3. Subagent returns with findings that change the approach
4. Rewrite the implementation

**The correct pattern:**
1. Dispatch subagent
2. Wait (or work on unrelated tasks)
3. Read subagent results
4. Proceed with complete information

---

## E3: Don't Re-Read Files Already in Context

If a file was read earlier in the conversation and hasn't been modified since, don't read it again. The content is still in context. This wastes tool calls and context space.

**Exception:** If the conversation has been running long enough that earlier content may have been compressed, re-reading is appropriate. Use judgment — if you can recall the file's content clearly, don't re-read it.

---

## E4: Parallelize Independent Tool Calls

When multiple tool calls are independent (no data dependency between them), issue them all in a single message. Don't serialize calls that could run in parallel.

**Bad:** Read file A → wait → Read file B → wait → Read file C → wait
**Good:** Read files A, B, C simultaneously in one message

This is already a system-level instruction, but it's repeated here because violations are a common source of wasted round-trips.

---

## E5: Don't Narrate What You're About to Do in Detail

A brief one-sentence status update before starting work is fine. A multi-paragraph explanation of your plan, followed by executing that plan, wastes output tokens on text the user will see duplicated in the actual work.

**Bad:** "I'm going to read file X to understand the current implementation, then I'll check file Y for the test patterns, then I'll modify file Z to add the new feature, making sure to follow the existing conventions I find in file X..."
**Good:** "Let me read the implementation and tests, then make the change."

---

## E6: Stop and Ask Rather Than Guess-and-Redo

When a decision point has two plausible paths and the user's preference isn't clear, ask. A one-sentence question costs ~50 tokens. Guessing wrong and redoing the work costs thousands.

**Applies especially to:** Architectural decisions, file organization choices, naming conventions, scope boundaries, and anything where the user has expressed preferences in the past.

---

## E7: Don't Generate Alternatives the User Didn't Ask For

When the user asks for X, implement X. Don't also generate Y and Z "in case they prefer those." If the user wants alternatives, they'll ask.

**The failure pattern:** User asks for a function that does X. Agent writes three versions — one with approach A, one with approach B, one with approach C — and asks "which do you prefer?" This burns 3x the tokens of just implementing the most appropriate approach.

**The correct pattern:** Implement the best approach. If there's a genuine architectural choice that the user should weigh in on, ask the question (per E6) instead of implementing all options.

---

## E8: Two-Attempt Rule — Stop After 2 Failed Fixes

**HARD RULE.** If you attempt to fix a problem (test failure, lint error, runtime bug) and your fix doesn't work, you get exactly one more attempt with a different approach. If that also fails, **STOP immediately.** Do not continue trying. Report to the user what you tried, what failed, and what you suspect the root cause is.

**Why this rule exists:** Without it, agents enter "fix spirals" — each failed attempt introduces new problems, the agent tries to fix those, creating more problems, and so on. These spirals routinely burn tens of thousands of tokens while making the code progressively worse. A 30-second question to the user almost always resolves what the agent was spiraling on, because the user has context the agent lacks (design intent, external constraints, "that test is actually wrong").

**The failure pattern:**
1. Agent implements a change. Tests fail.
2. Agent applies fix attempt 1. Tests still fail (or different tests fail).
3. Agent applies fix attempt 2. Tests still fail.
4. ❌ Agent applies fix attempt 3, 4, 5, 6... each one introducing new issues
5. After 15 minutes and 50K+ tokens, the code is in worse shape than before attempt 1

**The correct pattern:**
1. Agent implements a change. Tests fail.
2. Agent applies fix attempt 1. Tests still fail.
3. Agent applies fix attempt 2. Tests still fail.
4. ✅ Agent STOPS. Writes: "Attempted X (failed because Y) and Z (failed because W). Suspect root cause is [theory]. Flagging for human review."
5. User responds with the missing context. Agent applies the correct fix in one attempt.

**Where this applies:**
- Sprint execution (fixing test/lint failures after implementing a task)
- Code review (applying review fixes)
- Error debugging sessions
- Any context where the agent is repeatedly trying and failing to make something work

This rule is referenced from multiple workflow documents. The canonical definition is here; workflow documents point here rather than restating the rule.

---

## E9: Use System Operations Instead of LLM-Context Operations

**HARD RULE.** When a file needs to move from point A to point B, use a system command (`mv`, `cp`). Do NOT read the file's content into the LLM context and then write it back out to the new location. The system command costs ~50 tokens. Reading and rewriting a 5,000-word file through the LLM context costs 50,000-200,000 tokens.

**The incident that created this rule (2026-04-17):**

During the `product-development-strategy` research project in `aixodev-web`, 13 research subagents each produced a 4,000-10,000-word analysis document. Each subagent tried to write its output to the full repo-absolute path (184 characters), but the Write tool blocked the long path. Every subagent fell back to returning its content as response text. The parent (main) agent then had to read each ~10,000-word analysis from the subagent's response, pipe it through its own context window, and `Write` it to the target file — a **~50K-200K token tax per track**. Across 13 tracks, this dominated the entire research session's cost.

**The fix:** Instruct subagents to write to a short `/tmp/{slug}-{NN}.md` path (15-20 chars, universally writable). On completion, the parent agent runs `mv /tmp/{slug}-{NN}.md {full_target_path}` — a ~50-token metadata operation with zero content transfer through the LLM context. This reduced per-track persistence cost from ~50K-200K tokens to ~50 tokens.

**The general principle:** Any time you find yourself about to read a file just to write its contents somewhere else, stop and use `mv` or `cp`. This applies to:
- Moving subagent output files to their final location
- Copying template files to a new project directory
- Relocating files as part of a refactor

The detailed implementation for research subagents (short-path-first, response-text-fallback-second) is documented in [`workflow_research.md` § Write-tool handling](workflow_research.md).

---

## E10: Don't Silently Repeat an Expensive Workaround

**HARD RULE.** When something breaks and you improvise a workaround on the fly, that workaround may "work" in the sense that it produces the correct result — but it may also be far more expensive than the right fix. If you're about to repeat the same workaround more than once or twice, **STOP and discuss the workaround itself with the user** before proceeding. The workaround may be the problem.

**How this differs from E8 (two-attempt rule):** E8 covers the case where a fix *fails* — you try twice, it doesn't work, you stop. E10 covers the case where a workaround *succeeds* but is expensive, and you're about to repeat it many times. The workaround never "fails" in the E8 sense, so E8 never triggers — but the cumulative cost is enormous.

**The incident that created this rule (2026-04-17, `product-development-strategy` research):**

13 research subagents each tried to write their output to a long repo-absolute path (184 chars). The Write tool blocked the long path for Track 01. The agent improvised a workaround: have the subagent return its full ~10,000-word analysis as response text, then the parent agent reads that response through its own context window and writes it out. This workaround *worked* — the file got written. So the agent used the same workaround for Track 02. And Track 03. And all 13 tracks.

Each repetition cost ~50K-200K tokens (reading a 10,000-word document through the LLM context to write it out). Across 13 tracks, this added up to **over 1 million tokens of avoidable waste** that dominated the entire research session's cost.

**What should have happened:** After Track 01 (or at most Track 02), the agent should have stopped and said: "The Write tool is blocking long paths. My workaround is to pipe the content through my context, but that costs ~100K tokens per track and I have 12 more tracks to go. Can we discuss a better approach?" The user would have suggested (or the agent could have proposed) writing to `/tmp/{slug}-{NN}.md` and then using `mv` — a ~50-token operation per track. The fix was trivially simple; the waste came from not discussing it.

**The general principle:** A workaround that's acceptable once may be unacceptable at scale. Before repeating any workaround, estimate the cost of repeating it N times (where N is how many times it will be needed) and compare to the cost of finding a proper fix. If `N × workaround_cost` is significantly more than `discussion_cost + proper_fix_cost`, stop and discuss.

**Trigger:** Any time you notice you're about to do the same non-trivial workaround for the 2nd or 3rd time, that's the signal to pause and discuss with the user.

---

## E11: Defer Ruff Linting to End of Coding Session

**HARD RULE.** During sprint execution and code review fix passes, run `pytest` after each task to catch regressions immediately — but defer `ruff check` to one final pass after all tasks are complete.

**Why pytest per task:** A test failure on T01 that isn't caught until T05 means the agent has been building on a broken foundation for 4 tasks. The fix may require unwinding work across multiple commits. The cost of running pytest after each task is well justified by the regressions it catches.

**Why NOT ruff per task:** Ruff findings are almost always cosmetic mid-sprint — unused imports, import ordering, minor style issues. They don't affect runtime behavior, and they're frequently false positives when the sprint has multiple tasks:

**The observed waste pattern:**
1. T01 adds `from app.models import Foo, Bar, Baz` — all three will be used across T01-T03
2. T01 only uses `Foo`
3. Ruff flags `Bar` and `Baz` as unused imports (F401)
4. Agent edits the file to remove `Bar` and `Baz`
5. T02 needs `Bar` — agent re-adds it
6. Ruff flags `Baz` as unused
7. Agent removes `Baz`
8. T03 needs `Baz` — agent re-adds it

Each unnecessary edit cycle burns tokens on file reads, edits, and re-validation — for imports that were always intended to be used. Multiply this across a 10-task sprint and it becomes significant.

**The correct pattern:**
1. Run `uv run pytest tests/ -v` after each task. Fix any failures immediately (per E8).
2. After all tasks are complete and pytest passes, run `uv run ruff check .` once.
3. Fix all ruff findings in a single batch pass.
4. Commit the ruff fixes (either as part of the final task commit or as a separate lint-fix commit).

**What about ruff's bug-detecting rules?** Ruff includes rules that catch real bugs (F821 undefined name, B rules for bugbear, S rules for security). In practice, these are almost always also caught by pytest — an undefined name will cause a test to fail. The rare security rule that wouldn't surface in tests is not worth running ruff 12 times per sprint to catch.

**Where this applies:**
- Sprint execution (`workflow_execute_sprint_dev_plan.md`) — pytest per task, ruff at the end
- Collab-group code review Phase 3 fixes — pytest per fix, ruff once after all fixes
- Any coding session that involves multiple sequential file edits

---

## Adding New Rules

When you identify a new efficiency problem during a session:

1. **Document it here** with a rule number (E8, E9, ...), a clear title, the failure pattern, and the correct pattern
2. **Add it to the Rule Index** table at the top
3. **Update CLAUDE.md** if the rule is important enough to warrant a direct mention (most rules are covered by the CLAUDE.md reference to this document)
4. **Record it as a Compound Engineering finding** in the sprint's post-sprint notes

Rules should be based on **observed problems**, not hypothetical ones. Each rule exists because the failure pattern actually happened and wasted real tokens.
