# Workflows Guide

> A practical guide to how John and Claude (and sometimes Codex) work together on this project -- the sequences, the files, the conventions, and the lessons learned.

**Audience:** This guide is written for both John (the human developer) and Claude (the AI agent). John reads it to remember how the system works and when to invoke which workflow. Claude reads it at the start of every session to understand the project's development methodology, file conventions, and hard constraints. If you are a different AI agent reading this because you were bootstrapped from this project's workflow system, start with [`workflow_bootstrap_project.md`](workflow_bootstrap_project.md).

**Project context:** This guide's body is project-agnostic -- all project-specific values (name, slug, env prefix, domain, tech stack) live in [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md), the single per-repo source of truth. See it and [`../CLAUDE.md`](../CLAUDE.md) for this project's identity and architecture.

## Workflow Updates

Changes to workflows are logged here so that other projects adapting these workflows can track what evolved and why. Entries are newest-first.

| Date | Workflow | Change | Why |
|------|----------|--------|-----|
| 2026-06-09 | `EFFICIENCY_RULES_COLLAB.md` (CE3) | **Hardened CE3 with a 90-second absolute floor for status checks.** Never send a status check, confirmation re-prompt, or "are you done/stuck?" within 90 seconds of any handoff — for ANY task type, including peer-review requests, edit batches, and validation runs. Added peer-review-of-deliverables to the calibration guide (2-3 min/file) and a second documented failure example. | During Phase 01 Sprint 02 planning, codex-1 (LEAD) sent a status check ~36s after requesting a two-file peer review, before claude-2 had finished reading; codex-1 admitted "I checked too soon." The existing CE3 calibration didn't explicitly cover review requests and had no absolute floor, so a concrete 90-second minimum was added. |
| 2026-04-24 | `workflow_bootstrap_project.md` | **Full refresh for current workflow inventory and root-level layout option.** (1) Replaced the stale 10-file list with the current 37-file inventory (22 active top-level + 8 subdirectory files in `aixocode-collab/` and `ensemble-collab/` + README + 8 deprecated redirects). (2) Added a "Decide target layout" step documenting two first-class placements: root-level `_workflows/` (new default for research/analysis repos) and nested `_specs_and_plans/_workflows/` (legacy, matches `aixodev-web`). (3) Added layout-aware relative-path substitution tables with ready-to-run `sed` recipes for the root-level case. (4) Added condition-driven structural changes for research-only and docs-only projects. (5) Split the bootstrap into 4 reviewable commits (verbatim copy → mechanical substitutions → specs scaffold → CLAUDE.md) instead of a single monolithic commit. (6) Updated the Gather Project Context table to include package manager / lint / type-check / primary-work-mode fields | The original bootstrap workflow (last meaningfully updated 2026-03-14) had drifted badly: it listed 10 files when there were 37, referenced deprecated file names as primary items, omitted the entire post-split sprint pipeline (`start_new_sprint` / `sprint_planning_*` / `execute_sprint_dev_plan` / `sprint_closeout`), the collab-group trio, the roadmap-rescheduling pair, `workflow_code_audit.md`, and both subdirectories. The bootstrap process caught this when the real file count came in at ~4x the documented one. Ship a refreshed version so the next downstream bootstrap starts from accurate material |
| 2026-04-18 | `workflow_research.md` | **Synthesis no-skim rule (HARD) + Entity-inventory preflight check (HARD).** Phase C synthesis agent MUST read every analysis document top-to-bottom (no "I have enough to understand the basic idea" shortcuts) AND must enumerate every first-class entity the project has — consulting any authoritative entity-reference docs plus any new entities the research has proposed — and verify the synthesis scaffold keeps each entity that should remain first-class rather than implicitly replacing the whole inventory. The preflight checklist is produced as a Q1-style question during the Phase B → C gate review, forcing explicit inclusion/exclusion decisions per entity | Prior failure modes: (1) earlier Claude sessions produced lossy synthesis by skimming — defeats depth-first research; work is now being evaluated across multiple AI platforms so max effort is required. (2) Research that correctly pivots to a new strategic frame can over-extend by inferring "therefore drop the existing entity set" — silently removing entities the product still needs. Caught in the `product_development_strategy` research where Stage-2 subagents correctly pivoted to an FDSE/Foundry scaffold but over-extended by implying Projects/Workspaces/Repos should no longer be first-class. Entity-inventory preflight forces this to be decided explicitly with user approval, not inferred |
| 2026-04-17 | `workflow_research.md` | **Phase B → Phase C HARD GATE: main agent STOPS after every subagent track is complete/committed and waits for explicit user approval before starting synthesis.** Rationale: synthesis errors propagate — a misframed synthesis leads to misframed Phase D artifacts, which is expensive to unwind. The gate gives the user the opportunity to spot-check analysis quality, refine synthesis scope, and catch thin/off-scope tracks before they get canonized | Added by the user on 2026-04-17 mid-way through the product-development-strategy research project after observing that Phase B was running well but that committing immediately to a particular synthesis framing without review was risky given that the synthesis shapes every Phase D artifact downstream |
| 2026-04-17 | `workflow_research.md` | **Short-path Write pattern (subagent writes to `/tmp/{project-slug}-{NN}.md`, parent `mv`s to target)** replaces the long-repo-absolute-path-as-primary pattern. Parent agent: on subagent completion, check `/tmp/{project-slug}-{NN}.md`; if present, `mv` to the full target path (~50-token metadata-only operation); if absent, fall back to the response-text extraction path (existing rule). Response-text fallback still mandated as Plan B but is no longer the expected Plan A | 13-of-13 subagents in the product-development-strategy research (Tracks 01-13) hit a Write-tool block on the full 184-char repo-absolute path and had to fall back to response-text. Each fallback forced the parent agent to pipe a ~4K-10K-word analysis through its own context window to persist it — a ~50K-200K token tax per track that dominated research cost. Short paths (15-20 chars, under `/tmp/`) were never blocked in testing; this reduces the per-track persistence cost to ~50 tokens |
| 2026-04-17 | `workflow_research.md` | Added HARD RULE: committed analysis files must be byte-identical to subagent output — **no condensing, no truncation, no references to ephemeral `/private/tmp/.../task.output` paths**. When subagents hit the (common) Write-tool block and return content via fallback response text, the parent agent must inline the FULL content verbatim into the committed markdown, including the complete bibliography with all URLs. The committed file is the permanent record; any `/private/tmp` reference is a dangling pointer. The subagent prompt template now includes explicit fallback instructions directing subagents to return the full analysis — not a summary — if Write is blocked | First `product_development_strategy` research project caught this bug on Tracks 04-07: four analysis docs were committed with "bibliography truncated for brevity" notes pointing at ephemeral task-output paths. User flagged before more tracks committed. Fix: extracted full content from the still-available JSON transcripts, inlined everything, and encoded the rule here so future research projects don't recreate the mistake |
| 2026-04-17 | `workflow_research.md` | Added optional **"Solo Priming Track"** variant: when one track's findings should cascade to every other track's research, dispatch that track solo first, verify its output file, then require every remaining subagent to read it as a prerequisite (via explicit instruction in the prompt). Subagents do not share LLM context — naively launching a "strategic framing" track in the same batch as others does NOT propagate its findings to them | The 21-track `product_development_strategy` research caught the bug: main agent (orchestrator) and subagents do NOT share context, so the initial plan of "front-load the priming track into the initial trio" would have failed silently. Formalizing the pattern prevents recurrence |
| 2026-04-17 | `workflow_research.md` | **Sliding-window subagent dispatch** (max 3 concurrent; re-dispatch into any freed slot as soon as it opens) replaces the previous wait-for-full-batch-of-3 pattern. Network max-3 cap unchanged; only the draining behavior changed. Adds "abandon and re-dispatch" path for stalled subagents | Wait-for-full-batch had a critical failure mode: a single stalled subagent (silent death, network flake, model refusal, tool-call timeout) would block the entire pipeline for hours while the other 2 batch members idled. Sliding-window isolates the stall to 1 of 3 slots, keeping the other two draining the Pending queue |
| 2026-04-17 | `workflow_research.md` | Pulled 2026-04-05 `aixocode` change: README.md is the **dispatch manifest** — written + committed before subagent launch, includes Track table with per-subagent 2-3 sentence assignments + Dispatch Queue section tracking In-flight/Completed/Pending. Enables crash recovery (new session reads README + RESEARCH_PLAN + completed analyses to resume) and human progress monitoring during multi-hour research sessions | Formalizing the pattern validated in the aixocode project's multi-track research sessions; our own 21-track `product_development_strategy` research is the first adopter |
| 2026-05-04 | `EFFICIENCY_RULES_COLLAB.md` + sprint planning template | **Added CE4 (don't narrate work in progress) + interleaved deliverable review.** CE4: working agent must not stream progress updates — next message after "I'll notify" should be the completion notification. Interleaved review: LEAD writes sp_ first and sends for review immediately, then writes xp_. Catches scope errors in the shorter sp_ before investing in the longer xp_; eliminates the serialization delay of batching both files | CE4: observed 6 progress messages in 2 minutes from Codex-1, each forcing a token-burning "Ack" from Claude-2. Interleaved review: sp_ scope errors discovered during xp_ peer review would require rewriting the xp_, wasting the entire xp_ writing investment |
| 2026-05-04 | Sprint planning collab workflow + template | **Replaced scope guidance with owner requirements (floor, not ceiling).** Renamed `{SCOPE_GUIDANCE}` to `{OWNER_REQUIREMENTS}`. Main agent no longer drafts in-scope/out-of-scope bullet points — instead provides only hard minimum requirements. Added explicit "SCOPE DETERMINATION — YOUR JOB" section to template instructing agents to determine full scope through their own analysis of backlog files and adversarial debate. Workflow step 2 rewritten with anti-pattern guidance | Pre-decided scope guidance anchors the collab-group the same way premature external review reading anchors code review. Agents treat main-agent and owner scope bullets as authoritative and don't push back, defeating the purpose of adversarial debate. The backlog files already contain carefully triaged items with clustering annotations from prior collab-group sessions — let the planning agents use those directly |
| 2026-05-04 | Markdown-only collab workflows | **Removed pytest/ruff validation from sprint planning and roadmap rescheduling post-completion steps.** Replaced with a `git diff --name-only` check to verify no source code was accidentally modified. These sessions only edit markdown files — running the full test suite wastes tokens for zero diagnostic value | Identified during Sprint 02 roadmap rescheduling session. The validation step was cargo-culted from code review workflows where it's actually needed |
| 2026-05-04 | `COLLAB_ROLE_WORKER.md` | **Scoped §1 "Investigate Independently" to discussion phases only.** Added explicit scope limitation: the "do not wait passively" directive applies during analysis/discussion, NOT during writing/editing phases when the other agent is producing deliverables. Points to CE1/CE2 for writing-phase behavior | The blanket "never be idle" interpretation caused WORKER agents to thrash during Phase 3 (edit phase) — inventing side-quests, polling for status, and reopening settled decisions. The §1 directive was correct for discussion phases but was being applied universally |
| 2026-05-04 | `COLLAB_PROMPT_ROADMAP_RESCHEDULING.md` | **Removed references to non-existent files** (`_documentation/users_guide/ADDENDUM--gap-analysis.md` and `_REFERENCE/ARCHITECTURE/_draft/ADR--collaboration-tui-only.md`). These were carried over from the `aixocode` project template but don't exist in `codemap` | Agents would fail or waste tokens trying to read files that don't exist in this project |
| 2026-05-04 | `EFFICIENCY_RULES_COLLAB.md` (new) | **New collab-group-specific efficiency rules document** with CE1-CE3. CE1: Don't invent work while waiting — WORKER freelancing on side-quests during write phases. CE2: Don't poll when you'll be notified — status checks when the other agent already said they'd notify. CE3: Give the other agent time to work — premature status checks 60-90 seconds after assigning multi-file edit batches. Split from the general `EFFICIENCY_RULES.md` which retains E1-E10 for all agents. Referenced from agent guidelines mandatory reading | Three distinct failure patterns observed across Sprint 02 collab-group sessions (planning, code review). Each burned significant tokens on both sides of the message bus for zero productive value. Separated from general rules because these patterns only arise in multi-agent sessions |
| 2026-05-04 | `EFFICIENCY_RULES.md` | **Added E8-E11.** E8: Two-attempt rule — stop after 2 failed fixes, report to user (consolidated from sprint execution workflow). E9: Use system operations (`mv`/`cp`) instead of piping file content through LLM context (from 2026-04-17 research incident). E10: Don't silently repeat an expensive workaround — stop and discuss after 2nd repetition (from same research incident). E11: Defer ruff linting to end of coding session — running per-task catches false positives mid-implementation | E8: fix spirals routinely burned 50K+ tokens making code progressively worse. E9/E10: 13-track research session lost >1M tokens to repeated context-pipe workaround. E11: ruff flags unused imports that later tasks need, wasting tokens on false-positive fixes |
| 2026-05-04 | `EFFICIENCY_RULES.md` (new) | **New mandatory efficiency rules document.** Seven rules (E1-E7) codifying observed token-waste patterns: never duplicate subagent work, wait for subagents before acting on their topic, don't re-read files in context, parallelize tool calls, don't over-narrate, ask rather than guess-and-redo, don't generate unsolicited alternatives. Referenced from CLAUDE.md as mandatory reading. Designed as a living document — new rules added via Compound Engineering Stage B findings | Observed pattern: main agent dispatches background subagent then duplicates the same work "while waiting," doubling token consumption. The 5-hour rolling window and weekly cap on Claude Max make this a concrete cost, not a theoretical concern. Collecting all efficiency lessons in one document ensures they propagate to every future session across all projects via workflow migration |
| 2026-05-04 | `workflow_compound_engineering.md` (new) + 3 integration edits | **New dedicated Compound Engineering workflow.** Consolidates the methodology into a single versioned reference document with three stages: (A) Sprint Planning — Compound Investment Check, (B) Post-Sprint — Lessons Capture (the primary stage, replaces the old 5-question checklist in closeout Step 8), (C) Phase Transition — Compound Retrospective. Integrated into `workflow_sprint_closeout.md` (Stage B), `workflow_sprint_planning_solo.md` (Stage A), and `workflow_new_phase.md` (Stage C). Based on prior research (2026-03-14) confirmed against CE v3.3.0 (2026-04) | The old 5-question checklist was too lightweight — answered in seconds, produced no durable artifacts. The new Stage B process systematically converts sprint experience into CLAUDE.md updates, workflow improvements, and techstack document refinements. Single document also provides a clean git-log history for tracking methodology evolution |
| 2026-05-03 | `workflow_build_new_project.md` + `techstacks/` | **New workflow: push-based project generation with architectural discussion.** Agent acts as senior architect for the source project's tech stack: ingests user's scratch-pad notes as diffs, prefills a full Architectural Components Manifest (31 components for Python/Flask), presents condensed summary for collaborative discussion, iterates until approved, then generates the complete project. Tech-stack details (manifest, skeleton instructions, lessons learned) live in `_workflows/techstacks/` as separate documents per stack, reviewable during post-sprint analysis. Python/Flask active; Rust/Tauri placeholder. Includes HARD RULE for local-only git | Complements the pull-based `workflow_bootstrap_project.md`. Streamlines creation of sibling projects — user describes only what's different, everything else is inherited. Tech-stack separation enables iterative refinement of established patterns across projects without bloating the main workflow document |
| 2026-05-03 | All collab-group workflows | **SUSPENDED automated 3-minute steering reminder.** Steer is now manual-only: main agent prints the steer text for the project owner to send via tmux monitor pane when appropriate. Added suspension notes to all affected workflows | On 2026-05-02, the automated steer caused runaway token consumption — agents re-read files, restarted discussions, and generated enormous redundant output, burning through weekly usage limits. Will revisit once delivery mechanism is redesigned |
| 2026-04-05 | `workflow_sprint_code_review_collab.md` | Added HARD RULE: always send 3-minute steering reminder — no longer optional | Code review sessions consistently benefit from mid-session challenge reminder; manual timing showed no benefit over automated default |
| 2026-04-04 | Sprint pipeline | Split monolithic `workflow_new_sprint_solo.md` into `start_new_sprint` + `sprint_planning_solo` + `execute_sprint_dev_plan`; renamed collab variants | Separates planning from execution so a fresh agent can run xp tasks deterministically |
| 2026-04-04 | `workflow_sprint_code_review_collab.md` | Added HARD GATE: main agent must use the template, not write ad-hoc prompts | Ad-hoc prompts caused agents to read external reviews immediately, defeating anti-anchoring design |
| 2026-04-04 | Agent guidelines + collab templates | Added FILE OWNERSHIP hard rule: WORKER must NEVER edit LEAD's files | WORKER agents were preemptively editing files the LEAD was actively writing |
| 2026-04-04 | `workflow_execute_sprint_dev_plan.md` | Auto-generates external review prompt after all xp tasks complete | Removes a manual step that was easy to forget |
| 2026-04-04 | `workflow_sprint_planning_collab.md` | Updated: write "Context and Scope Boundaries" section at top of xp instead of Paste Prompt in sp | Gives the executing agent a clear scope paragraph without needing to read the sp |
| 2026-04-03 | All code review workflows | Changed "Fix only Critical/Major" to "Fix ALL findings within scope" | Agents were deferring Minor issues that could have been fixed in-sprint |
| 2026-04-03 | `workflow_sprint_closeout.md` | Added "zero test failures" hard gate and "no pre-existing failures" rule | Multiple sprints had agents signing off with known failures |
| 2026-04-03 | Sprint planning workflows | Added execution plan gate, scope immutability, test completeness rules | Prevent executing from sp alone, silent scope reduction, and skipped tests |

---

## Workflow Catalog

Every workflow file lives in this directory (`_workflows/`). Some workflows have implementation variants in the `ensemble-collab/` subdirectory -- the top-level router file delegates to `ensemble-collab/` directly.

### Sprint Pipeline (run in this order)

| File | Purpose |
|------|---------|
| [`workflow_start_new_sprint.md`](workflow_start_new_sprint.md) | Shared entry point: create branch, gather context, hand off to planning |
| [`workflow_sprint_planning_collab.md`](workflow_sprint_planning_collab.md) | Plan a sprint via collab-group (delegates to ensemble-collab) |
| [`workflow_sprint_planning_solo.md`](workflow_sprint_planning_solo.md) | Plan a sprint directly (Claude solo with user) |
| [`workflow_execute_sprint_dev_plan.md`](workflow_execute_sprint_dev_plan.md) | **Autonomous execution**: find active sprint, execute xp tasks, generate review prompt |
| [`workflow_sprint_code_review_collab.md`](workflow_sprint_code_review_collab.md) | Post-sprint code review via collab-group (delegates to ensemble-collab) |
| [`workflow_sprint_code_review_solo.md`](workflow_sprint_code_review_solo.md) | Post-sprint code review, solo agent |
| [`workflow_sprint_closeout.md`](workflow_sprint_closeout.md) | Shared endpoint: status updates, README, triage, CLAUDE.md, clean tree |

### Supporting Workflows

| File | Purpose |
|------|---------|
| [`workflow_new_phase.md`](workflow_new_phase.md) | Initialize a new development phase (directory, README, DECISIONS.md) |
| [`workflow_code_audit.md`](workflow_code_audit.md) | Full codebase audit producing categorized findings and remediation roadmap |
| [`workflow_quick_fix.md`](workflow_quick_fix.md) | Single-commit fixes outside sprint context |
| [`workflow_roadmap_rescheduling_collab.md`](workflow_roadmap_rescheduling_collab.md) | Holistic roadmap rescheduling via collab-group |
| [`workflow_roadmap_rescheduling_solo.md`](workflow_roadmap_rescheduling_solo.md) | Lighter roadmap rescheduling by main agent + human |
| [`workflow_claude_md_maintenance.md`](workflow_claude_md_maintenance.md) | Section-by-section verification and update of CLAUDE.md |
| [`workflow_research.md`](workflow_research.md) | Deep research with Opus subagent orchestration |
| [`workflow_ideation.md`](workflow_ideation.md) | Feature brainstorming before sprint planning |
| [`workflow_error_debugging.md`](workflow_error_debugging.md) | Systematic error diagnosis during development |
| [`EFFICIENCY_RULES.md`](EFFICIENCY_RULES.md) | **Mandatory reading** — hard rules for minimizing token waste (subagent discipline, file I/O, output, scope) |
| [`workflow_compound_engineering.md`](workflow_compound_engineering.md) | Compound Engineering review — lessons capture, infrastructure investment, phase retrospectives |
| [`workflow_bootstrap_project.md`](workflow_bootstrap_project.md) | Adapt this workflow system for a new project (pull-based, run from target) |
| [`workflow_build_new_project.md`](workflow_build_new_project.md) | Generate a new sibling project from current project's stack (push-based, run from source) |
| [`workflow_adapt_project_from_clone.md`](workflow_adapt_project_from_clone.md) | Re-identify a freshly rsync'd clone of a sibling project as a new project (reset-based, run from target) |
| [`workflow_collab_group_launch.md`](workflow_collab_group_launch.md) | Launch and manage collab-group sessions (delegates to ensemble-collab) |
| [`workflow_collab_group_agent_guidelines.md`](workflow_collab_group_agent_guidelines.md) | Behavioral rules for agents in collab-groups |

### Deprecated (kept as redirects)

| File | Replaced By | Reason |
|------|-------------|--------|
| `workflow_new_sprint_solo.md` | `start_new_sprint` + `sprint_planning_solo` + `execute_sprint_dev_plan` | Split into pipeline stages |
| `workflow_new_sprint_collab.md` | `start_new_sprint` + `sprint_planning_collab` | Split into pipeline stages |
| `workflow_collab_group_code_review.md` | `workflow_sprint_code_review_collab.md` | Renamed for pipeline consistency |
| `workflow_post_sprint_review.md` | `workflow_sprint_closeout.md` | Consolidated closeout checklist |
| `workflow_backlog_triage.md` | Roadmap rescheduling workflows | Replaced by broader scope |
| `workflow_code_review.md` | `workflow_code_audit.md` | Renamed to distinguish from post-sprint review |
| `workflow_new_sprint.md` | (see `workflow_new_sprint_solo.md` redirect) | Legacy monolithic file |
| `new_sprint.md` | (see chain of redirects) | Legacy pre-`workflow_` prefix |
| `error_debugging.md` | `workflow_error_debugging.md` | Legacy pre-`workflow_` prefix |

### Collab-Group Implementation Variants

Router workflows delegate to the ensemble-collab implementation in the subdirectory:

| Subdirectory | Contents | Backend |
|-------------|----------|---------|
| `ensemble-collab/` | Sprint planning, code review, roadmap rescheduling, launch | Ensemble-backed collaboration |

The router files delegate to `ensemble-collab/` directly (no user prompt needed).

### Tech Stack Reference Documents

Tech-stack-specific details for the build-new-project workflow live in `techstacks/`:

| Document | Stack | Status |
|----------|-------|--------|
| [`techstack--python_quart.md`](techstacks/techstack--python_quart.md) | Python 3.12+ / **Quart (async)** / async SQLAlchemy / aiosqlite→asyncpg / Alembic / Hypercorn / uv | **Active (this project's stack)** |
| [`techstack--python_flask.md`](techstacks/techstack--python_flask.md) | Python 3.12+ / Flask / SQLAlchemy / SQLite / uv | Active (sibling fork; reference for sync Flask projects) |
| [`techstack--rust_tauri.md`](techstacks/techstack--rust_tauri.md) | Rust / Tauri / frontend TBD | Placeholder |

---

## The Primary Development Loop

Every meaningful chunk of work on this project follows this loop. A single iteration produces one sprint's worth of committed, reviewed, documented code.

```
                         +-------------------+
                         |  [1] New Phase    |
                         | (if starting new  |
                         |  thematic body    |
                         |  of work)         |
                         +--------+----------+
                                  |
                                  v
+------------------------------------------------------------------------+
|                                                                        |
|   +------------------+     +-----------------+     +----------------+  |
|   | [2] Sprint       | --> | [3] Human       | --> | [4] Sprint     |  |
|   |     Planning      |     |     Review      |     |     Execution  |  |
|   +------------------+     +-----------------+     +-------+--------+  |
|                                                            |           |
|   +------------------+     +-----------------+             |           |
|   | [8] Sprint       | <-- | [7] Collab-Group| <--+       |           |
|   |     Closeout     |     |     Code Review |    |       |           |
|   +--------+---------+     | (optional)      |    |       |           |
|            |               +-----------------+    |       |           |
|            |                                      |       v           |
|            |               +-----------------+    +--+----------+    |
|            |               | [6] External    | <---- | [5] Post- |    |
|            |               |     Reviews     |       | Execution |    |
|            |               | (optional)      |       | Handoff   |    |
|            |               +-----------------+       +-----------+    |
|            |                                                          |
|            +-------> Next Sprint (back to [2]) --------->             |
|                                                                        |
+------------------------------------------------------------------------+
```

### Step 1: New Phase (when needed)

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_new_phase.md`](workflow_new_phase.md) |
| **When** | Starting a new thematic body of work (not every sprint -- only when the theme changes) |
| **What happens** | Review backlog horizons and previous phase retrospective. Create phase directory with `README.md` and `DECISIONS.md` from templates. Phase 01 Sprint 01 begins immediately. |
| **Output** | `_specs_and_plans/phase_{NN}--{slug}/README.md`, `DECISIONS.md` |

### Step 2: Sprint Planning

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_start_new_sprint.md`](workflow_start_new_sprint.md) (entry point) leading to [`workflow_sprint_planning_solo.md`](workflow_sprint_planning_solo.md) (default) or [`workflow_sprint_planning_collab.md`](workflow_sprint_planning_collab.md) (complex sprints) |
| **When** | Every sprint starts here |
| **What happens** | Claude reads context (CLAUDE.md, ROADMAP.md, backlog, phase README), discusses scope with the human, writes a sprint spec (`sp_`) and an execution plan (`xp_`), commits both. Solo variant: Claude and human iterate directly. Collab variant: Codex + Claude adversarially review scope before the human sees it. |
| **Output** | `sp_{NN}--{slug}.md` (what and why), `xp_{NN}--{slug}.md` (how -- self-contained) |

**Key rule:** The `xp_` is the contract. Implementation MUST NOT begin without an approved execution plan. The `sp_` says what and why; the `xp_` says how, exactly.

### Step 3: Human Review

| Detail | Value |
|--------|-------|
| **Workflow file** | (No separate file -- this is an async gate between planning and execution) |
| **When** | After planning session produces sp + xp docs |
| **What happens** | John reads the sprint spec and execution plan. Asks questions, requests changes, and ultimately approves. This is the only human gate in the loop. |
| **Output** | Approved (possibly revised) `xp_` document |

### Step 4: Sprint Execution

| Detail | Value |
|--------|-------|
| **Workflow file** | Driven by the approved `xp_` document (execution follows its task list) |
| **When** | After human approves the plan |
| **What happens** | Claude runs with `--dangerously-skip-permissions`, reads the approved xp, executes every task autonomously, commits after each task with `P{NN}-S{NN}-T{NN}` prefix. Scope is immutable -- no silent deferrals. Tests must pass after every task. |
| **Output** | One commit per task, all tests passing, working tree clean |

### Step 5: Post-Execution Handoff

| Detail | Value |
|--------|-------|
| **Workflow file** | (End of the execution session -- Claude reports status) |
| **When** | After all xp tasks are committed |
| **What happens** | Claude reports what was done, any blockers encountered, and test results. The human decides what comes next: external reviews, collab-group code review, or direct closeout. |
| **Output** | Status summary in conversation |

### Step 6: External Reviews (optional)

| Detail | Value |
|--------|-------|
| **Workflow file** | Uses template `_templates/EXTERNAL_REVIEW_PROMPT.md` |
| **When** | Before collab-group code review, when the human wants independent perspectives |
| **What happens** | A review prompt is prepared from the template and sent to external reviewers (Gemini, Cursor, KimiK25, etc.). They produce independent review reports that feed into Step 7. This prevents anchoring bias -- external reviewers see the code without knowing the sprint plan. |
| **Output** | `REVIEW--{AgentName}-P{NN}-S{NN}.md` files in the phase directory |

### Step 7: Collab-Group Code Review (optional)

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_sprint_code_review_collab.md`](workflow_sprint_code_review_collab.md) |
| **When** | After complex sprints, or when the human requests adversarial review |
| **What happens** | Three-phase review: (1) each agent reads the code and external reports independently, (2) adversarial discussion identifies findings by severity, (3) the LEAD agent implements all fixes. Hard requirement: fix ALL findings (Critical through Observations). Both validators must pass. |
| **Output** | Fix commits on the sprint branch, zero test failures |

### Step 8: Sprint Closeout

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_sprint_closeout.md`](workflow_sprint_closeout.md) |
| **When** | After execution and review (if any) are both complete |
| **What happens** | Update the sprint spec with post-sprint notes. Update phase README with sprint results. Update backlog horizons (archive completed items, add new items). Update ROADMAP.md. Update CLAUDE.md if the sprint changed architecture, conventions, or dependencies. Verify clean working tree. |
| **Output** | All documentation current, working tree clean, sprint formally closed |

---

## Supporting Workflows

These workflows are not part of the primary loop but support it at specific moments.

### Quick Fix

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_quick_fix.md`](workflow_quick_fix.md) |
| **When** | Bug fix, typo, config tweak -- anything that takes one commit and <30 minutes |
| **Commit prefix** | `P{NN}-FIX-{num} Description` |
| **Key constraint** | Single issue, single commit, on the current branch. If it would take multiple commits or touch multiple subsystems, it needs a sprint. |

### Roadmap Rescheduling

| Detail | Value |
|--------|-------|
| **Workflow files** | [`workflow_roadmap_rescheduling_solo.md`](workflow_roadmap_rescheduling_solo.md) (main agent + human) or [`workflow_roadmap_rescheduling_collab.md`](workflow_roadmap_rescheduling_collab.md) (collab-group) |
| **When** | Between phases, after a major milestone, or when the backlog has accumulated enough items to warrant re-evaluation |
| **What happens** | Empty the UNSORTED_QUEUE by sorting every item into the correct horizon (NEXT / LATER / SOMEDAY). Re-evaluate existing items for promotion or demotion. Archive implemented items. Update ROADMAP.md. Identify natural clusters without producing sprint specs. |
| **Output** | Updated `UNSORTED_QUEUE.md`, horizon files, `ROADMAP.md` |

### CLAUDE.md Maintenance

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_claude_md_maintenance.md`](workflow_claude_md_maintenance.md) |
| **When** | After sprints that change schema, add dependencies, alter architecture, or introduce new conventions |
| **What happens** | Section-by-section comparison of CLAUDE.md against the actual codebase. Update any sections that have drifted. Target length: under 500 lines (Anthropic recommends <200, but our project complexity justifies more). |
| **Output** | Updated `CLAUDE.md` |

### Code Audit

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_code_audit.md`](workflow_code_audit.md) |
| **When** | Before major refactoring phases, after rapid feature-building, periodically as a health check |
| **What happens** | Systematic audit of part or all of the codebase. Produces categorized findings (Security, Architecture, Code Quality, Tests, Frontend, Dependencies) with severity levels (Critical, High, Medium, Low) and a remediation roadmap organized as sprints. |
| **Output** | Findings document + remediation roadmap |
| **Exemplar** | Phase 3 (265 findings, 7 category documents, 5 remediation sprints) |

### Research

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_research.md`](workflow_research.md) |
| **When** | Before a new phase begins, when evaluating technology choices, when a question requires deep investigation |
| **What happens** | Opus subagents (never Sonnet -- documented factual errors) investigate specific questions in parallel. Each produces a report. A synthesis document distills findings into actionable recommendations. No source code is edited during research. |
| **Output** | Individual reports + synthesis doc in `_specs_and_plans/_research/{topic_slug}/` |
| **Branch** | `claudecode/research/@claude/{slug}` (optional) |

### Ideation

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_ideation.md`](workflow_ideation.md) |
| **When** | Large, ambiguous feature areas where the scope is unclear before sprint planning |
| **What happens** | Diverge first (brainstorm all possibilities without filtering), then converge (select what to build). ~30-60 minutes of conversation. Most sprints do NOT need ideation -- skip directly to sprint planning if scope is already clear from the backlog. |
| **Output** | Ideation document or inline section in the sprint spec |

### Error Debugging

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_error_debugging.md`](workflow_error_debugging.md) |
| **When** | Runtime errors during development or execution sessions |
| **What happens** | Stack-agnostic method: read the actual error (not just the symptom), categorize, locate the source, check recent changes, fix minimally, run validators to confirm, with a 2-attempt escalation rule. The stack-specific error tables, common scenarios, and diagnostic commands live in the active techstack doc's **Debugging** section (`techstacks/techstack--*.md`). |
| **Output** | Fixed code + passing tests |

### Bootstrap Project

| Detail | Value |
|--------|-------|
| **Workflow file** | [`workflow_bootstrap_project.md`](workflow_bootstrap_project.md) |
| **When** | Starting a new project that should use this workflow system |
| **What happens** | Creates a customized copy (not a fork or symlink) of the `_specs_and_plans/` directory in the target project. Adapts workflow files to the target project's tech stack, conventions, and naming. Each project owns its workflow docs independently and can evolve them. |
| **Output** | A complete `_specs_and_plans/` directory in the target project |

---

## The Collab-Group System

A collab-group is a collaborative session between two AI agents (typically Claude and Codex) that produces better outcomes through adversarial review. The system is governed by three top-level workflow files and one implementation subdirectory.

### Governing Files

| File | Role |
|------|------|
| [`workflow_collab_group_launch.md`](workflow_collab_group_launch.md) | How to start and manage a collab-group session (delegates to ensemble-collab) |
| [`workflow_collab_group_agent_guidelines.md`](workflow_collab_group_agent_guidelines.md) | Behavioral rules every agent must follow inside a collab-group |
| [`workflow_collab_group_code_review.md`](workflow_collab_group_code_review.md) | Three-phase post-sprint code review via collab-group (delegates to ensemble-collab) |

### Implementation Path

| Path | Description |
|------|-------------|
| `ensemble-collab/` | Ensemble-backed collaboration |

The subdirectory contains its own variants of `workflow_collab_group_launch.md`, `workflow_collab_group_code_review.md`, `workflow_new_sprint_collab.md`, and `workflow_roadmap_rescheduling_collab.md`.

### Collab-Group Composition

Collab-groups are always **two-party**: one LEAD agent and one WORKER agent. The LEAD agent is responsible for writing deliverable files; the WORKER agent challenges, critiques, and reviews.

| Session Type | Template | Deliverables |
|-------------|----------|-------------|
| Sprint Planning | `_templates/COLLAB_PROMPT_SPRINT_PLANNING.md` | Sprint spec (`sp_`) + execution plan (`xp_`) |
| Code Review | `_templates/COLLAB_PROMPT_CODE_REVIEW.md` | Fix commits + review summary |
| Roadmap Rescheduling | `_templates/COLLAB_PROMPT_ROADMAP_RESCHEDULING.md` | Updated UNSORTED_QUEUE, horizons, ROADMAP.md |

### Three-Phase Code Review Process

1. **Phase 1 -- Independent Reading:** Each agent reads the sprint's changes and any external review reports. No discussion yet -- each forms their own independent assessment.
2. **Phase 2 -- Adversarial Discussion:** Agents share findings, challenge each other's assessments, assign severity levels (Critical, Major, Minor, Observation). Genuine disagreements are surfaced and resolved through discussion.
3. **Phase 3 -- Fix Implementation:** The LEAD agent implements fixes for ALL findings. Both validators (`uv run pytest tests/ -v` and `uv run ruff check .`) must pass before the session ends.

### Key Collab-Group Constraints

These are hard requirements from `workflow_collab_group_agent_guidelines.md`:

- **No auto-disband.** The session continues until all deliverables are committed and both agents confirm completion.
- **Discuss first, write last.** The LEAD agent must not write any deliverable files until genuine discussion has concluded and both agents have reached consensus.
- **Mandatory peer review.** The WORKER agent must review every deliverable file before it is committed. The LEAD does not merge its own work unchallenged.
- **File ownership.** Only the LEAD agent writes to deliverable files. The WORKER agent contributes through discussion and review, not direct file edits.
- **Mandatory reading phase.** Every agent must read ALL specified context files thoroughly before posting any substantive analysis.

---

## Tips and Lessons Learned

Accumulated across John's projects that use this workflow system, and refined here as this project evolves. Organized by category.

### Sprint Planning and Execution

**The xp is the contract.** The execution plan (`xp_`) must be fully self-contained -- every command, every file path, every expected outcome. During execution, Claude follows the xp and nothing else. If information is not in the xp, it does not exist for the execution session. This is why the human review step (Step 3) matters: it is the last chance to catch missing context before autonomous execution begins.

**One commit per task.** Each task in the execution plan gets exactly one commit with a `P{NN}-S{NN}-T{NN}` prefix. This makes the sprint's history readable and bisectable. If a task requires changes to multiple files, they all go in one commit. If a change touches multiple tasks, something is wrong with the task boundaries.

**Run both validators.** Every task commit must leave the test suite and linter clean:

```bash
uv run pytest tests/ -v       # All tests passing
uv run ruff check .            # No lint violations
```

This is not optional. "I'll fix the tests later" is not an acceptable position during sprint execution.

**The two-attempt rule ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)).** If a task fails twice (e.g., tests break and two fix attempts do not resolve it), STOP and report a blocker to the human. Do not enter an infinite loop of retries. The human may have context that changes the approach entirely.

**Clean working tree -- every sprint, no exceptions.** The final task of every sprint must include a `git status` check. If there are uncommitted files (including spec edits, plan updates, or gitignore changes), commit them. The sprint is not done until the working tree is clean.

**Paste prompt in sp, not xp.** When the human provides a paste prompt (initial context block), include it in the sprint spec (`sp_`), not the execution plan (`xp_`). The sp captures "what and why" including the human's original request. The xp captures "how" and must be self-contained without referencing external conversation.

**Scope immutability.** The approved xp scope must not be changed, reduced, deferred, or dropped during execution. If a task proves harder than expected, implement it anyway or STOP and report a blocker. Never silently skip or defer a task.

### Code Review

**External reviews prevent anchoring bias.** Sending code to external reviewers (Gemini, Cursor, KimiK25, etc.) before the collab-group code review ensures that the reviewers see the code fresh, without the context of the sprint plan. This catches a different class of issues than the agents who wrote the code would find.

**Fix everything possible.** During collab-group code review, fix ALL findings -- Critical, Major, Minor, AND Observations. The only acceptable reason to defer is if the fix would widen the change into a different sprint's scope (new migration, new API endpoint, unrelated subsystem). Deferred items must be written to the backlog with explicit finding ID references.

**Test coverage before refactoring.** This lesson comes from Phase 3 (265 findings, 5 remediation sprints). When auditing or refactoring, ensure adequate test coverage exists BEFORE making structural changes. Writing tests after the refactor means you are testing against a potentially broken baseline.

### Collab-Groups

**Two heads are genuinely better than one -- if the rules are followed.** The value of collab-groups is in adversarial challenge, not rubber-stamping. The WORKER agent must push back on the LEAD's proposals with specific concerns. Sessions where the WORKER simply agrees with everything produce the same output as a solo session at twice the cost.

**Discuss before writing.** The most common failure mode in early collab-group sessions was the LEAD agent writing deliverables immediately and then "discussing" them as fait accompli. The guideline is explicit: no files are written until consensus is reached through genuine discussion.

**The reading phase is not optional.** Agents that skip or skim the mandatory reading phase produce shallow analysis that misses important details in the source material. The strongest sessions are consistently those where both agents complete thorough reading passes.

### Backlog and Project Health

**Triage everything.** Every idea, bug, improvement, or "we should consider..." gets written down. The UNSORTED_QUEUE catches it all, and roadmap rescheduling sessions sort items into the appropriate horizon (NEXT / LATER / SOMEDAY). An idea that is not recorded is an idea that is lost.

**Compound Engineering.** After every sprint, look for opportunities to improve the development infrastructure itself -- not just the product. Better templates, better test fixtures, better tooling, better documentation. This compounding effect means each subsequent sprint is faster and more reliable than the last. Based on the [Compound Engineering](https://every.to/guides/compound-engineering) methodology by Every, Inc. See [`workflow_compound_engineering.md`](workflow_compound_engineering.md) for the full three-stage process (planning check, lessons capture, phase retrospective) and integration points.

**ROADMAP.md is the single view of the future.** After each sprint closeout and roadmap rescheduling session, ROADMAP.md must be updated to reflect reality. It is the authoritative reference for project status, phase history, and forward plans. If ROADMAP.md and the backlog disagree, something is wrong.

---

## Quick Reference: Which Workflow Do I Need?

| Situation | Workflow |
|-----------|----------|
| Starting a brand new body of work | [`workflow_new_phase.md`](workflow_new_phase.md) |
| Planning the next sprint (straightforward) | [`workflow_start_new_sprint.md`](workflow_start_new_sprint.md) then [`workflow_sprint_planning_solo.md`](workflow_sprint_planning_solo.md) |
| Planning the next sprint (complex, many dependencies) | [`workflow_start_new_sprint.md`](workflow_start_new_sprint.md) then [`workflow_sprint_planning_collab.md`](workflow_sprint_planning_collab.md) |
| Executing a planned sprint | Follow the approved `xp_` document |
| Closing out a completed sprint | [`workflow_sprint_closeout.md`](workflow_sprint_closeout.md) |
| Code review after a sprint (collab-group) | [`workflow_sprint_code_review_collab.md`](workflow_sprint_code_review_collab.md) |
| Full codebase health audit | [`workflow_code_audit.md`](workflow_code_audit.md) |
| Quick bug fix or typo correction | [`workflow_quick_fix.md`](workflow_quick_fix.md) |
| Reprioritizing the backlog and roadmap | [`workflow_roadmap_rescheduling_solo.md`](workflow_roadmap_rescheduling_solo.md) or [`..._collab.md`](workflow_roadmap_rescheduling_collab.md) |
| CLAUDE.md has drifted from reality | [`workflow_claude_md_maintenance.md`](workflow_claude_md_maintenance.md) |
| Need to investigate a technology or approach | [`workflow_research.md`](workflow_research.md) |
| Large ambiguous feature, unclear scope | [`workflow_ideation.md`](workflow_ideation.md) |
| Runtime error during development | [`workflow_error_debugging.md`](workflow_error_debugging.md) |
| Setting up workflows for a new project | [`workflow_bootstrap_project.md`](workflow_bootstrap_project.md) |
| Launching a collab-group session | [`workflow_collab_group_launch.md`](workflow_collab_group_launch.md) |
| Understanding collab-group behavior rules | [`workflow_collab_group_agent_guidelines.md`](workflow_collab_group_agent_guidelines.md) |

---

## Key Conventions

### Branch Naming

```
claudecode/@claude/phase{NN}-sprint{NN}       # Sprint branches (e.g., claudecode/@claude/phase05-sprint04)
claudecode/research/@claude/{slug}              # Research branches
```

The `claudecode/` prefix identifies sessions running in Claude Code. `@claude` is hardcoded — if we later add other agent platforms, we'll revisit branch namespace conventions at that time.

### Commit Convention

```
P{NN}-S{NN}-T{NN} Description              # Sprint task commit (e.g., P05-S04-T03 Add session export API)
P{NN}-FIX-{num} Description                # Quick fix commit
```

All numbers (phase, sprint, task) are zero-padded to two digits.

### Product Naming

- **Identity:** Project name, repo/slug, brand, corporate entity, env-var prefix, and ecosystem siblings all live in [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md) -- the single per-repo source of truth.
- See [`../CLAUDE.md`](../CLAUDE.md) for the project overview and tech stack.

### Validation Commands

Both commands must pass before any commit:

```bash
uv run pytest tests/ -v       # Run the full test suite
uv run ruff check .            # Run the linter
```

(mypy is optional in this build-line — add `uv run mypy src/` as a third gate only if the project opts into type-checking.)

### Sprint Document Naming

```
sp_{NN}--{slug}.md             # Sprint spec (what and why)
xp_{NN}--{slug}.md             # Execution plan (how -- self-contained)
```

Sprint docs live in the phase directory: `_specs_and_plans/phase_{NN}--{slug}/`.

---

## How This Guide Relates to Other Documents

This workflows README is one node in a network of project documentation. Here is how the pieces fit together.

### PROJECT_IDENTITY.md (this directory)

[`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md) is the single source of truth for everything project-specific — name, slug, env-var prefix, brand/entity, ecosystem siblings, the active tech stack, and the validation commands. It is the ONE file edited per repository; every workflow body in this directory is project-agnostic and reads from it. When syncing workflow improvements between projects, sync the bodies and replace this one file. See its header for the full rationale.

### CLAUDE.md (Project Root)

[`../CLAUDE.md`](../CLAUDE.md) is the authoritative project guide -- tech stack, architecture, database schema, API endpoints, conventions, environment variables, and known gotchas. It is the first thing Claude reads at the start of every session. This workflows README links to it for context but does not duplicate its contents. CLAUDE.md references this directory for workflow details.

### ROADMAP.md

[`../_specs_and_plans/ROADMAP.md`](../_specs_and_plans/ROADMAP.md) is the authoritative reference for project status, phase history, and forward plans. It is updated on every sprint closeout and roadmap rescheduling session. The workflows in this directory produce the changes that ROADMAP.md documents.

### _specs_and_plans/README.md

[`../README.md`](../README.md) is the index page for the entire specs-and-plans directory. It provides quick navigation to phases, backlog, research, templates, and workflows. The workflows section in that README should link here for the comprehensive guide.

### Phase READMEs

Each phase directory (`phase_{NN}--{slug}/`) has its own `README.md` tracking sprint status, key decisions, and phase-level retrospective. Phase READMEs are updated during sprint closeout (Step 8 of the primary loop).

### Sprint Specs and Execution Plans

Sprint specs (`sp_`) and execution plans (`xp_`) live in their phase directory. They are produced by the sprint planning workflows (Step 2) and updated during sprint closeout (Step 8). The `xp_` is the contract that drives sprint execution.

### Templates Directory

[`../_workflows/_templates/`](../_workflows/_templates/) contains templates used by several workflows:

| Template | Used By |
|----------|---------|
| `PHASE_README_TEMPLATE.md` | `workflow_new_phase.md` |
| `SPRINT_TEMPLATE.md` | `workflow_sprint_planning_solo.md`, `workflow_sprint_planning_collab.md` |
| `DECISION_TEMPLATE.md` | `workflow_new_phase.md` (for DECISIONS.md) |
| `COLLAB_PROMPT_SPRINT_PLANNING.md` | `workflow_sprint_planning_collab.md` |
| `COLLAB_PROMPT_CODE_REVIEW.md` | `workflow_sprint_code_review_collab.md` |
| `COLLAB_PROMPT_ROADMAP_RESCHEDULING.md` | `workflow_roadmap_rescheduling_collab.md` |
| `EXTERNAL_REVIEW_PROMPT.md` | `workflow_sprint_code_review_collab.md` (pre-requisite) |

### Backlog Horizons

[`../_specs_and_plans/_backlog/`](../_specs_and_plans/_backlog/) contains the prioritized backlog files: `_horizon_NEXT.md`, `_horizon_LATER.md`, `_horizon_SOMEDAY.md`, and `UNSORTED_QUEUE.md`. These are read during sprint planning and updated during sprint closeout and roadmap rescheduling.

---

## Revision History

| Date | Change |
|------|--------|
| 2026-04-03 | Initial creation: comprehensive workflows guide covering 16 active + 6 deprecated workflows, primary loop, collab-group system, lessons learned |
