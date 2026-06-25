# Workflow: Research

> How to conduct deep research with optional subagent orchestration for this project.

## Quick Reference

| Item | Value |
|------|-------|
| Research directory | `_specs_and_plans/_research/{topic_slug}/` |
| Research branch | `claudecode/research/@claude/{slug}` (optional) |
| Output format | Individual reports + synthesis document |
| Critical Rule | DO NOT edit source code during research sprints |
| Subagent model | **Opus for research subagents** (main orchestrator stays Opus-4-6; never use Sonnet for research tasks — documented factual errors in prior projects) |
| Subagent concurrency | **Sliding window, max 3 concurrent** (never more; re-dispatch into any freed slot as soon as it opens) |
| Crash recovery | README.md is the dispatch manifest — committed before launch, updated after each subagent completes |

---

## Overview

Research sessions produce analysis documents, not code. They answer questions like "How should we design X?", "What do other platforms do for Y?", and "What are the tradeoffs of approach A vs. B?"

Research can be:
- **Standalone:** A dedicated research session before a phase begins
- **Embedded:** Part of sprint planning (Step 4 of `workflow_start_new_sprint.md`)
- **Exploratory:** Open-ended investigation of a technology or pattern

The key output is a **synthesis document** that distills findings into actionable recommendations.

---

## When to Use This Workflow

| Situation | Use Research? | Reason |
|-----------|--------------|--------|
| New phase with unfamiliar domain | Yes | Reduces risk of wrong architecture |
| Feature with multiple viable approaches | Yes | Compare tradeoffs systematically |
| Small, well-understood feature | No | Just implement it |
| Bug fix | No | Use `workflow_error_debugging.md` |
| Understanding existing codebase | Maybe | Quick grep/read is usually sufficient |

---

## Step-by-Step

### Step 1: Define Research Scope

Write down the specific questions you need answered. Vague research produces vague results.

**Good research questions:**
- "What entity model do issue trackers use for workflow automation? Compare Linear, Jira, GitHub Projects, and Shortcut."
- "What are the tradeoffs of ltree vs. closure table vs. materialized path for hierarchical data in SQLite?"
- "How do other platforms handle multi-agent session attribution?"

**Bad research questions:**
- "Research issue tracking" (too broad)
- "How does GitHub work?" (too vague)
- "What should we build next?" (that is ideation, not research)

### Step 2: Create Research Directory

```bash
mkdir -p _specs_and_plans/_research/{topic_slug}/
```

The topic slug should be descriptive:
- `phase05_entity_review/`
- `market_analysis/`
- `joy_of_engineering/`
- `workflow_automation_patterns/`

### Step 3: Create Research README

Create `_specs_and_plans/_research/{topic_slug}/README.md`. For multi-agent research, this README doubles as the **dispatch manifest** (see Step 5 below) — the live source of truth for which tracks are in flight, complete, or pending.

```markdown
# Research: {Title}

| Field | Value |
|-------|-------|
| Status | ACTIVE / COMPLETE / TABLED / ARCHIVED |
| Started | {YYYY-MM-DD} |
| Completed | {YYYY-MM-DD or --} |
| Phase | {N} (if phase-related) or Standalone |
| Agents | @claude (main orchestrator, Opus-4-6), {N} Opus subagents |

## Questions

1. {Specific question 1}
2. {Specific question 2}
3. {Specific question 3}

## Methodology

{How the research will be conducted: platforms to review, papers to read, code to analyze}

## Research Tracks

{For multi-agent research, list every track with enough detail to serve as a dispatch manifest. Each track description must be specific enough that a crashed session can re-dispatch this subagent from this row alone.}

### Area 1: {Area Name}

| # | Track | Slug | Description | Status |
|---|-------|------|-------------|--------|
| 01 | {Track title} | `{track-slug}` | {2-3 sentences: what to read, what to search, what to produce. Include source-list hints.} | Pending |
| 02 | ... | ... | ... | Pending |

### Dispatch Queue (Sliding Window, Max 3 Concurrent)

- **In-flight (≤3):** (currently none)
- **Completed:** (none yet)
- **Pending:** 01, 02, 03, 04, ... (in dispatch order)

When a subagent completes: move its track row from In-flight → Completed, pull the next Pending track into In-flight (staying at ≤3), commit the README update, and launch the next subagent. Never exceed 3 in-flight.

## Output Files

| File | Description | Status |
|------|-------------|--------|
| `analysis-01--{slug}.md` | {Description} | Pending |
| `analysis-02--{slug}.md` | {Description} | Pending |
| `synthesis.md` | Combined findings and recommendations | Pending |

## Follow-Up

{Items that emerged from this research, triaged to sprints or backlog}
```

### Step 4: Create Research Branch (Optional)

For standalone research that should not be on a sprint branch:

```bash
git checkout main
git checkout -b claudecode/research/@claude/{slug}
```

For research embedded in sprint planning, stay on the sprint branch.

### Step 5: Conduct Research

#### Single-Agent Research

For focused, well-scoped questions, a single Opus session is sufficient:

1. Read relevant existing code and documentation
2. Use WebSearch/WebFetch tools for external sources
3. Analyze findings
4. Write analysis documents
5. Write synthesis

#### Multi-Agent Research (Subagent Orchestration)

For broad surveys requiring parallel investigation, use the orchestration pattern below.

**Phase A: Breadth-First Survey (main Opus-4-6 orchestrator)**
- The main agent reads the research questions.
- Identifies investigation tracks (typically 12-25 for comprehensive research).
- **Writes `README.md` as the dispatch manifest** (see "README as Dispatch Manifest" below).
- **Writes `RESEARCH_PLAN.md`** with full per-track scope, questions, sources.
- **Commits both before launching any subagent** — this is the resumable checkpoint.

**README as Dispatch Manifest:**

The `README.md` written in Phase A serves three purposes: (1) lets the human monitor progress while subagents are running, (2) provides a crash-recovery recipe if the session is interrupted (a new session reads README + RESEARCH_PLAN + any completed analysis files and resumes from the next Pending track), and (3) documents exactly what each subagent was asked to investigate.

The README MUST include:
- Standard header (Status, Started, Phase, Agents)
- Research questions being answered
- **Track table** — one row per subagent with: number, title, slug, 2-3 sentence description of the specific assignment, and Status column (Pending / In-flight / Complete / Failed)
- **Dispatch Queue** section — shows which tracks are currently In-flight (max 3), Completed, and Pending (in dispatch order)
- **Output files table** — one row per expected analysis file with Status

**Phase B: Depth-First Analysis (Sliding Window, Max 3 Concurrent Opus Subagents)**

- **CRITICAL: At most 3 Opus subagents in flight at any moment.** Never 4+. The max-3 cap exists because Claude Code dispatches WebFetch requests from the client machine; too many concurrent subagents saturate the outbound network connection (especially on residential ISPs), causing agent failures and incomplete results.
- **Sliding-window dispatch, NOT wait-for-full-batch dispatch.** As soon as any one subagent completes, immediately pull the next Pending track into its freed slot and launch. Do not wait for the other two in-flight subagents to finish first.
- Each subagent is assigned one track and produces a standalone analysis document.
- Subagents should NOT coordinate with each other (independence ensures diversity of findings).
- **Use Opus** for research subagents (never Sonnet — documented factual errors in prior projects). The main orchestrator stays Opus-4-6. For non-research tasks, decide per-situation.
- **After each subagent completes**, update the Track table (mark Complete), update the Dispatch Queue (move from In-flight → Completed, promote next Pending), and commit. This maintains the checkpoint for crash recovery.

**Why sliding window replaced wait-for-full-batch:**

The previous pattern ("launch 3, wait for all 3, then launch next 3") had a critical failure mode: if one subagent stalled, hung, or silently died (which happens intermittently for reasons that are hard to diagnose — network flakiness, model refusal, tool-call timeouts, upstream API issues), the other 2 subagents in its batch would complete but the entire pipeline would block waiting for the hung one. Users reported hours of wasted time on a single stalled track while 18 other tracks sat idle.

The sliding-window pattern fixes this: a hung subagent ties up only 1 of 3 slots, not the whole pipeline. The other 2 slots continue to drain and refill from the Pending queue. A human can kill and re-dispatch (or abandon) a stuck subagent without having lost progress on anything else.

**Sliding-window dispatch pattern:**

```
T+0:  Launch tracks 1, 2, 3 (3 in-flight)
T+5:  Track 2 completes → commit; launch track 4 (in-flight: 1, 3, 4)
T+7:  Track 1 completes → commit; launch track 5 (in-flight: 3, 4, 5)
T+12: Track 3 completes → commit; launch track 6 (in-flight: 4, 5, 6)
T+15: Track 4 completes → commit; launch track 7 (in-flight: 5, 6, 7)
... (continues until Pending queue is empty and all in-flight have drained)
```

**Implementation notes:**
- Use the Agent tool with `run_in_background: true` so the main agent receives completion notifications without polling.
- On each completion notification: (a) verify the analysis file was written, (b) update README, (c) commit, (d) launch the next Pending track (if any).
- If a subagent appears stuck for longer than a reasonable threshold (e.g., 30+ minutes for a typical 10-minute research task), the main agent may abandon it, mark Failed in the Track table, and re-dispatch as a new track at the end of the Pending queue.
- Never exceed 3 in-flight. If this means launching fewer than 3 at startup (e.g., only 2 pending tracks remain at the end), that's correct.

**Dispatch discipline — the "phantom launch" failure mode (added 2026-06-15):**

The single most common orchestration bug is updating the dispatch manifest to show a track *In-flight* but **never actually issuing the `Agent` tool call for it.** It happens because the refill step bundles a manifest edit + a commit + a launch into one turn, and it is easy to do the edit and commit and end the turn *without* the launch — especially when a completion notification arrives mid-turn and shifts attention. The manifest then *claims* N in-flight while only N−1 (or fewer) agents are truly running, and the pipeline silently under-fills or stalls with no error.

**The manifest "In-flight" list is a CLAIM, not proof.** A track is actually running only if (a) its `Agent` call returned an `agentId`, and (b) on a later cycle its `/tmp/{slug}-NN.md` file exists (subagents using the incremental-write pattern create it within their first few tool calls).

**Mitigation (cheap, every cycle):** after launching the next track, glance at `/tmp` — every *In-flight* track except the just-launched one should already have a file. A track marked In-flight with no `/tmp` file and no remembered `agentId` was never launched ("phantom") → relaunch it. If nothing is running but the queue is non-empty, you under-filled → launch up to the cap. (Observed repeatedly 2026-06-14/15: tracks 10, 20, 26, and 41 were each phantom-marked and caught only by this `/tmp`-absence check. The fix each time was a real `Agent` call.)

**Stream-watchdog considerations for long-running subagents (added 2026-04-19):**

The Claude Code runtime monitors subagents with a stream-idle watchdog that fires when no stream activity (tool calls, output tokens) occurs for a threshold period. The threshold is configurable via environment variables, but defaults may be too aggressive for research subagents that gather data for 10+ minutes and then compose a single large (3K+ line) final output.

**Observed failure mode (2026-04-19, Track 22.C first attempt):** a research subagent completed all its web-fetch and analysis work, emitted "I have enough comprehensive data. Now let me write the full analysis to `/tmp/aixo-NN.md`" — then the runtime watchdog fired with "Agent stalled: no progress for 600s (stream watchdog did not recover)." The entire gathered context was lost. Diagnosis: the stall occurred during LLM-composition of the final massive Write call, when no tokens were streamed for longer than the watchdog threshold.

**Configurable env vars** (per Claude Code docs, env-vars page at `code.claude.com/docs/en/env-vars`):

| Variable | Effect |
|----------|--------|
| `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | Idle-timeout threshold in milliseconds |
| `CLAUDE_ENABLE_STREAM_WATCHDOG=1` | Enable event-level watchdog (all providers) |
| `CLAUDE_ENABLE_BYTE_WATCHDOG` | Byte-level watchdog (Anthropic-route only; default-on) |

Note that the observed 600-second behavior may be a circuit-breaker above the configured timeout rather than the timeout itself — the exact 600s threshold is not documented publicly. Treat these settings empirically.

**Recommended settings BEFORE launching Claude Code for a research-heavy session:**

```bash
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=900000    # 15 minutes
export CLAUDE_ENABLE_STREAM_WATCHDOG=1          # event-level on
# CLAUDE_ENABLE_BYTE_WATCHDOG defaults on for Anthropic routes; leave default.
```

Env vars cannot be changed mid-session — if a session is already running at default settings, exit and relaunch with the above exported. (Same pattern as the collab skill's extended-watchdog wrapper scripts at `/Users/{user}/.claude/skills/collab/`.)

**Relaunch cost-benefit (updated 2026-06-15):** relaunching mid-project wipes the orchestrator's entire conversational context — which, on a long collaborative session, is itself a large, high-value, hard-to-rebuild asset (it is *why* the main agent understands the human's intent so well). Relaunch ONLY when env vars genuinely must change AND the accumulated context is not worth preserving. In particular, **do NOT relaunch merely to switch to a "research-optimal" model** — that reasoning is obsolete once the default main-loop model is already the strongest available for research. (Historically the relaunch also down-set Opus 4.6, which beat 4.7 for research; under Opus 4.8 there is no better-for-research model to switch to, so that leg of the rationale is gone.) If the research env vars are already live for the session, **stay in it** — the continuity is worth more than the marginal setting.

**Two subagent-prompt mitigations** that make subagents more watchdog-resilient even at default timeouts:

1. **Write the output file early and update incrementally.** Instruct the subagent to create `/tmp/{project-slug}-NN.md` within its first 3–5 tool calls as a skeleton (section headers + 1–2-sentence placeholders), then expand each section by overwriting the file with updated content. This keeps the stream active during the composition phase and ensures partial output is recoverable if the watchdog does fire.

2. **Breadth-first before depth-first within the subagent's own work.** Instruct the subagent to cover all major sections at summary-level first, THEN deepen the highest-priority sections. If the watchdog fires mid-deepening, the skeleton is still useful. This also aligns with the commit-often philosophy — the partial file written mid-session can be recovered and optionally re-dispatched for completion rather than starting over.

**Re-dispatch protocol for watchdog-killed subagents:**

1. Check `/tmp/{project-slug}-NN.md` for partial output. If present and non-trivial, the analysis already has useful content — review and decide whether to (a) keep as-is, (b) re-dispatch to complete the remaining sections, or (c) re-dispatch fresh. The incremental-write pattern is what makes (b) viable.
2. If `/tmp` file is empty or absent (the stall happened before any Write): mark the track Failed in the dispatch manifest and re-dispatch with explicit stall-avoidance instructions (see examples 22.C retry, 2026-04-19).
3. Update the Research Tracks table with Failed status, note the failure mode, and re-dispatch as a new subagent at the end of the Pending queue.

**When to prefer env-var increase vs. prompt-level mitigation:**

- **Env-var increase** (recommended for research-heavy sessions): handles the failure mode at the runtime level; works regardless of how subagent is prompted; requires a session restart to apply.
- **Prompt-level mitigation** (always include in research subagent prompts): handles the specific "silent final composition" stall; works mid-session without restart; also benefits crash-recovery because partial files are always available.

Use both together for long research sessions. Prompt-level is cheap insurance; env-var is the structural fix.

**Subagent prompt pattern:**
```
You are researching {track_topic} for this project.

Context: {brief project description}

Questions to answer:
1. {Specific question for this track}
2. {Specific question for this track}

Output — Primary: Write your findings to a SHORT path: /tmp/{project-slug}-{NN}.md (e.g., /tmp/aixo-14.md). Use this short path, NOT the long repo-absolute path — long paths have been observed to trigger Write-tool restrictions in subagent runtimes. Absolute paths under /tmp are universally writable and Write has never been blocked there in our testing. The parent agent will `mv` the file into its final location after you finish.

Output — Fallback (if Write still fails somehow): Return the FULL analysis content as your final response text, starting with a `# PLEASE PERSIST TO: {full target path}` header on the first line. Do NOT abbreviate, condense, or summarize when using the fallback path — return every section in full, including the complete bibliography with all URLs inline. The parent agent will extract the content and save it verbatim.

FORMATTING — no soft-wrapped lines (HARD RULE): write all Markdown prose as unbroken lines — each paragraph and each list item is ONE line that soft-wraps in the renderer. Insert a newline ONLY at real semantic boundaries (a blank line between paragraphs, list items, headings, table rows, fenced code). Do NOT hard-wrap prose at a fixed column width (~80 cols).

CRITICAL: This is a research-only session. DO NOT edit any source code files.
```

> **Note (2026-06-15):** the "no soft-wrapped lines" rule above is a project-wide documentation convention (see the repo `CLAUDE.md` → *Documentation Conventions*), not research-specific — it applies to every analysis, the synthesis, briefs, and any doc a subagent writes. Include it in every report-writing subagent prompt; prior analyses are inconsistent on it, so state it explicitly.

**Write-tool handling: short-path-first, fallback-second (HARD RULE)**

Empirical history (as of 2026-04-17): 13-of-13 subagents in the product-development-strategy research project hit a Write-tool block when targeting the full repo-absolute path (184 chars). Every one of those runs had to fall back to returning content via response text, forcing the parent agent to copy a ~4,000-10,000-word analysis through its own context window to `Write` it out — a ~50K-200K token tax per track that dominated the research cost.

The short-path experiment (introduced 2026-04-17 starting with Track 14): instruct subagents to write to `/tmp/{project-slug}-{NN}.md` — a very short (15-20 char), universally writable absolute path. The parent agent, on subagent completion, runs `mv /tmp/{project-slug}-{NN}.md {full target path}` — a ~50-token file-metadata operation with no content transfer through the parent's context.

**Parent agent dispatch protocol for Tracks that use the short-path pattern:**

1. In the subagent prompt, explicitly state the short path (e.g., `/tmp/aixo-14.md`) as the Primary output destination, with the response-text fallback as Secondary. Do NOT give the subagent the long target path as Primary — that is precisely what has been getting blocked.
2. On subagent completion, first check if `/tmp/{project-slug}-{NN}.md` exists. If yes: `mv /tmp/{project-slug}-{NN}.md {full target path}`. Done. Skip the response-text extraction entirely.
3. If the short-path file does not exist, fall back to the response-text extraction path (see below).
4. Update the Research Tracks table to mark the track Complete, update the Dispatch Queue, commit.

**Subagents return response text ONLY as fallback.** When that happens, the hard rule for the parent agent remains: **the committed analysis file must be byte-identical in content to what the subagent produced, with zero truncation, condensation, or external references.** Specifically:

1. **Never condense per-company profiles, methodology, or sources** when extracting from a subagent's response to a file. The temptation to save space is real; resist it. Every section the subagent produced must land in the committed file.
2. **Never reference ephemeral paths** (`/private/tmp/claude-501/.../task.output`, `/tmp/...`, etc.) in committed markdown. Those paths are session-local and will not exist for any future reader. If you want to note where the raw transcript came from, paraphrase the source attribution inline (e.g., "primary sources: vendor pricing pages, earnings transcripts, ...") but do not point to a temp path.
3. **Inline the full bibliography with URLs.** Every citation the subagent produced must appear in the committed file. Do not write "bibliography truncated for brevity" or "full sources in subagent output" — the subagent output will be gone in 24 hours; the committed file is forever.
4. **Extract-and-write pattern for the fallback path** — when a subagent returns content via the `# PLEASE PERSIST TO:` header, the parent agent's job is: (a) locate that header, (b) capture everything from the header to the end of the subagent's response (excluding any trailing `## Report (for parent agent)` or metadata footer), (c) write that content verbatim to the target file, (d) optionally remove the persist header itself. Do not paraphrase. Do not abbreviate. Do not summarize.
5. **When the subagent JSON transcript is still available at session time and the response-text path truncated the content** (rare but possible), the parent agent can parse the JSON at `/private/tmp/claude-501/.../task.output` to recover the complete text — but the output must still be inlined into the committed markdown, not referenced by path.

**Why this matters:** the committed research files are the permanent record. They feed future synthesis passes, future artifact production, future re-reads by new agents in new sessions. Any reference to a `/private/tmp/...` path is a dangling pointer. Any "truncated for brevity" note is a promise the future can't keep.

**Optional Phase B variant: Solo Priming Track**

Subagents do **not** share context with each other or with the main agent — every Agent-tool invocation is a fresh session with an empty context window, seeded only by its prompt. This means the sequencing of which track runs first does NOT naturally share insights between subagents. If one track's findings need to inform every other track's research (e.g., a strategic-framing track that reframes the whole research project), you must explicitly wire that in:

1. **Identify the priming track** — the single track whose findings should influence every other subagent's approach.
2. **Dispatch that track SOLO first.** Do not launch any other tracks in parallel with it. Wait for completion and verify the `analysis-{slug}.md` file exists and is non-trivial.
3. **For every remaining track, add a mandatory pre-read instruction to the subagent prompt:**
   ```
   PREREQUISITE (before beginning your research): Read the completed analysis at
   {path to priming analysis file}. This document contains the strategic framing
   that informs all research on this project. Your findings should be interpreted
   through this lens where applicable.
   ```
4. **Only then start the sliding-window dispatch** for the remaining tracks.

This pattern costs one ~10-minute solo run up front but guarantees that every subsequent subagent's context includes the priming findings. Use it sparingly — only when one track's findings truly need to cascade. For most research projects, all tracks are parallel peers and the priming-track pattern is unnecessary overhead.

**Phase B → Phase C GATE (HARD RULE — user review required)**

After every subagent track is complete (all rows in the Research Tracks table marked Complete and all analysis files committed), the main agent MUST STOP and request user review before beginning Phase C synthesis. The synthesis is a long, expensive, context-heavy operation that commits to a particular reading of the underlying analyses; the user needs the opportunity to:

- spot-check the analysis files for quality, framing, or bias they want corrected
- refine the synthesis scope (which threads to emphasize, which tensions to resolve)
- catch any tracks that completed but produced thin or off-scope output before it gets canonized in synthesis

The gate is: main agent posts a "Phase B complete, N/N tracks committed, ready for your review — awaiting approval before Phase C" message and waits. Do NOT start synthesis until the user explicitly approves. This gate exists because synthesis errors propagate: a misframed synthesis leads to misframed Phase D artifacts, which is very expensive to unwind.

**Phase C: Synthesis (main Opus-4-6 orchestrator, gated on user approval)**
- The main agent reads ALL subagent reports **IN FULL**. **No-skim rule (HARD):** the synthesis agent must read every analysis document top-to-bottom, no exceptions, no "I've seen the gist" or "this track is covered by that other track" shortcuts. Prior failure mode: earlier Claude sessions read only portions, said "I have enough to understand the basic idea," and produced lossy synthesis that disregarded significant sections the subagents wrote. That defeats the entire point of depth-first parallel research — subagents wrote 4K-10K-word analyses precisely so the synthesis could pattern-match across the full surface, not skim the summaries. The work is being evaluated across multiple AI platforms (human reviewers + peer models like GPT/Gemini); give it maximum effort. If you find yourself thinking "I don't need to re-read analysis-NN for this section," that's the failure mode; re-read it anyway.
- Produces a comprehensive synthesis document.
- Identifies contradictions between reports and resolves them, especially between subagent recommendations and authoritative project docs that subagents may not have had in their prompt context.
- **Names specific passages needing correction.** An explicit "Where subagents correctly pivoted vs where the pivot over-extended" section that calls out which research findings to keep, which to narrow, and which to reject — citing the specific analysis file and section number for each correction. This section is non-optional even when the research went well; at minimum it says "nothing to correct."
- Extracts actionable recommendations.
- If any tracks remained Failed / Abandoned, the synthesis explicitly notes the gap and proposes whether to re-run or proceed without.

### Step 6: Write Output Documents

#### Individual Analysis Documents

```markdown
# Analysis: {Track Title}

## Summary
{2-3 sentence overview of findings}

## Methodology
{What was examined, what sources were consulted}

## Findings

### {Finding Category 1}
{Detailed analysis with examples, comparisons, code snippets}

### {Finding Category 2}
{...}

## Recommendations
{Specific, actionable recommendations based on findings}

## Sources
- {Links, references, platform documentation consulted}
```

#### The hard gate + producing the synthesis (Option-B pattern, added 2026-06-15)

**The hard gate.** After all analysis tracks are written and committed (Phase B complete), **STOP.** Post a "Phase B complete, N/N committed, ready for review" status and WAIT for the human's explicit approval before writing the synthesis. The human reviews the raw analyses first; the synthesis must not pre-empt that review. (For a multi-wave research project, the gate fires per wave-set, but the eventual `synthesis.md` is single and combined.)

**Write a `SYNTHESIS_BRIEF.md` before synthesizing.** Much of the judgment needed to synthesize well lives in the orchestrator's *conversation* — the human's reframes and priorities, which subagents over-reached, the cross-cutting convergence, the corrections to apply, the open questions — and **not** in any single analysis file. Capture it in a terse, machine-readable `SYNTHESIS_BRIEF.md` (no human-courtesy prose): the task, the emerged answer/architecture, the convergence signals, the corrections-to-apply, a one-line-per-track index, the open questions, and the required output structure. Commit it. This brief is what lets a *clean-context* agent synthesize at full quality without the conversation.

**Produce the synthesis with the Option-B pattern — do NOT `/clear` the orchestrator.** Synthesis is the integrative "reduce" step over the whole corpus. The instinct to `/clear` (or relaunch) the main session first is a 200k-context-era artifact and is now usually the wrong trade:

- **`/clear` buys nothing a subagent doesn't, and costs the collaboration.** Clearing collapses the orchestrator to a blank state — the *same* blank state a fresh subagent starts in (same model, reloaded CLAUDE.md/memory, zero conversation). So it destroys the accumulated context while gaining no advantage over just dispatching a clean subagent.
- **Better: dispatch ONE clean Opus subagent** with the `SYNTHESIS_BRIEF` + grounding docs to read every analysis (no-skim) and draft `synthesis.md`. The orchestrator **stays alive**, then reads the ~15–25k-token draft back into its still-rich context and iterates on it with the human. Net = clean-context draft quality **+** preserved collaboration context **+** human-in-the-loop review. Strictly better than clear-and-resynthesize.
- **Why a clean context still helps the *draft* (signal-to-noise, not space):** by Phase-B-end the orchestrator's window is full of per-track `mv`/commit/manifest churn that is noise for synthesis and dilutes attention across files that must be weighed evenly. A fresh subagent holds only the substance. At 1M, capacity is rarely the constraint; *attention quality* is.
- **Rule of thumb:** subagents for the independent *map* steps (the analyses); a clean-subagent draft **+** living-orchestrator-plus-human review for the integrative *reduce* step (the synthesis). Keep the human gate on the reduce.
- **Corpus-size check first:** `cat analysis-*.md | wc -w` × ~1.4 ≈ tokens. If the corpus fits one window (it usually will under 1M), a single synthesis subagent is correct; only if it does not fit should you go map-reduce (subagents pre-digest clusters → orchestrator reduces).

#### Synthesis Document

```markdown
# Research Synthesis: {Title}

## Executive Summary
{One paragraph: what was researched, key findings, primary recommendation}

## Research Scope
{What was covered, what agents participated, methodology}

## Key Findings

### {Theme 1}
{Cross-cutting finding that emerged from multiple analysis tracks}

### {Theme 2}
{...}

## Recommendations

| Priority | Recommendation | Rationale | Effort |
|----------|---------------|-----------|--------|
| 1 | {Specific action} | {Why} | {S/M/L} |
| 2 | {Specific action} | {Why} | {S/M/L} |

## Unresolved Questions
{Questions that remain open and may need further investigation}

## Appendix: Source Reports
- `analysis-{track-1}.md` — {one-line summary}
- `analysis-{track-2}.md` — {one-line summary}
```

### Step 7: Commit Research Artifacts

```bash
git add _specs_and_plans/_research/{topic_slug}/
git commit -m "P{NN}-S{NN}-T{NN} Research: {brief description}"
```

Or for standalone research:
```bash
git commit -m "Research: {brief description}"
```

---

## Research Project Lifecycle

| Status | Meaning | Action |
|--------|---------|--------|
| ACTIVE | Research is in progress | Continue investigation |
| COMPLETE | All questions answered, synthesis written | Archive and reference from phase docs |
| TABLED | Paused, may resume later | Document what remains and why it was paused |
| ARCHIVED | No longer relevant | Keep for historical reference |

Update the README status field when the lifecycle changes.

---

## Tips for Effective Research

1. **Start with existing code.** Before researching external patterns, understand what this project already does. Many "new" features are extensions of existing patterns.

2. **Cite sources.** Every claim should be traceable to a source (URL, file path, or platform documentation).

3. **Be specific about tradeoffs.** "X is better" is not useful. "X has O(1) lookup but O(n) insert; Y has O(log n) for both" is useful.

4. **Separate facts from opinions.** Label recommendations clearly as recommendations, not findings.

5. **Write for future readers.** Research documents should be understandable by someone who was not part of the research session. Include enough context to stand alone.

6. **Subagent independence matters.** Do not pre-bias subagents with conclusions. Let them discover findings independently — contradictions between reports are valuable signal.

---

## Reference: Phase 5 Sprint 01 as Exemplar

Phase 5 Sprint 01 used 4 parallel Opus subagents to produce ~6,900 lines of analysis across 4 research tracks. The Opus main agent then synthesized findings into a comprehensive entity model specification. This is the canonical example of multi-agent research orchestration.

Files: `_specs_and_plans/_research/phase05_entity_review/`

---

## Related Workflows

- `workflow_start_new_sprint.md` — Research embedded in sprint planning
- `workflow_ideation.md` — Brainstorming that may follow research
- `workflow_new_phase.md` — Phases often start with research
