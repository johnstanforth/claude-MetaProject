# Research Workflow for Codex

This workflow is for deep research performed by Codex in this repository family. It adapts the Claude/Opus-oriented process in `workflow_research.md` to Codex capabilities, Codex tool rules, and Codex subagent constraints while preserving the same output standard: a large, auditable research corpus followed by a synthesis, not a light survey.

Use this when the user asks Codex for extensive deep research, decision-grade investigation, broad technology evaluation, market/regulatory/data-source discovery, or an ambitious product concept analysis. For Claude/Opus sessions, continue to use `workflow_research.md`; for Codex sessions, this file is the controlling workflow where the two differ.

## Output Standard

A full deep-research run is a corpus, not a summary.

The reference standard is `_REFERENCE/_EXTERNAL/kingstrat-adventuregps/_research/entity_model_and_graph_db/`: 47 individual analysis files, a static `RESEARCH_PLAN.md`, a live `README.md` manifest, a `SYNTHESIS_BRIEF.md` handoff, and a decision-grade `synthesis.md`. The point is not to copy that subject matter. The point is to copy the rigor, corpus scale, track specificity, source discipline, capstone analysis, and hard synthesis gate.

The FracRealHomes `next_gen_zillow_estimate` run is now the Codex validation exemplar for this workflow. It produced 73 analysis files, 27,232 lines across the 73 analyses plus research README and plan, explicit subagent manifests, supplemental spot-check tracks after user review, a gated Phase C synthesis prompt, a context-blocked one-shot synthesis attempt, seven accepted packetized synthesis reader packets, and a 960-line refreshed final `synthesis.md`. Future Codex runs should treat that result as evidence that Codex can match the Claude-style corpus standard when the workflow is followed rigorously.

For a broad ambiguous research request, expect dozens of tracks, not four to eight overview documents. A small first-pass survey is valid only when the user explicitly asks for a first pass, a feasibility scan, or a lightweight research memo.

Minimum artifacts for full deep research:

| File | Purpose |
|------|---------|
| `README.md` | Live manifest, status board, dispatch queue, completed outputs, known gaps, and resume instructions |
| `RESEARCH_PLAN.md` | Static scope, research questions, track map, dependencies, source strategy, and acceptance bar |
| `analysis-NN--slug.md` | One full research report per track, with sources and recommendations |
| `analysis-NN--capstone-*.md` | Cross-track comparisons, decision matrices, unknown-unknown sweeps, and prior-art reconciliation |
| `SYNTHESIS_BRIEF.md` | Machine-readable handoff that captures corpus state and synthesis instructions before synthesis begins |
| `phase_c_packets/packet-NN--slug.md` | Durable Phase C extraction layer with read ledgers; use one packet for small full-corpus runs and multiple packets for larger runs |
| `synthesis.md` | Final integrated synthesis written only after all analysis files are complete and either directly read in full or represented by accepted packets whose readers read them in full |

Optional but recommended artifacts for Codex runs:

| File | Purpose |
|------|---------|
| `PHASE_C_SYNTHESIS_SUBAGENT_PROMPT.md` | Reviewable clean-context subagent prompt for the hard-gated synthesis run, especially when the user wants to inspect the launch instructions before approval |
| `PHASE_C_PACKET_SYNTHESIS_SUBAGENT_PROMPT.md` | Reviewable prompt for the final packet-based synthesizer |
| `first_pass_YYYY-MM-DD/` | Archive location for early lightweight or superseded research so later runs do not confuse first-pass notes with accepted Phase B corpus files |

## Codex Capability Model

Codex can read and write the local repository, run shell commands, browse the web when needed, use local tooling, and commit local git changes. Codex can also access subagent tools in this harness, but those tools have a strict authorization rule.

Subagents may be spawned only if the user explicitly asks for subagents, delegation, or parallel agent work. Requests for depth, thoroughness, research, investigation, or detailed analysis do not count as permission to spawn subagents. If the user asks for "extensive deep research" but does not explicitly authorize subagents, Codex must run this workflow in solo full-corpus mode instead of downgrading the result to a short memo.

When subagents are explicitly authorized, use them for independent sidecar tracks that materially advance the corpus. Do not delegate the immediate blocking task that the main agent needs next. Do not duplicate delegated work locally. Track agent IDs, close completed agents, and keep the parent responsible for final quality, integration, and commits.

Codex subagents are not Claude subagents. The current harness can support the practical pattern where a child writes a full report to `/tmp/{project-slug}-{NN}.md` and the parent moves it into the research corpus, but the parent must verify the file exists, has the expected line count, is not truncated, is ASCII/format-clean if required, and contains the required sections and URLs before accepting it. If `/tmp` handoff fails in a future harness, require the child to return the full Markdown report in its final response or write directly to a disjoint workspace file under parent-specified ownership.

Clean-context synthesis is useful but not a magic 1M-token guarantee. A spawned subagent can be launched with `fork_context: false` so it starts from the prompt instead of the parent thread, but the public Codex manual does not guarantee a specific usable context size for every model/session. For full deep-research runs, the durable packet layer is the default way to control context and preserve late-supplement flexibility. Before any final synthesis, measure the corpus with `wc -l -w -c`; if one-shot synthesis is attempted for a small or explicitly requested run, the prompt must explicitly block rather than silently skim if context is insufficient.

## Core Rules

1. No light skim for a deep-research request. If the requested scope is broad, create a broad track map and execute it.
2. No synthesis before the raw corpus exists. Final synthesis starts only after all planned analyses are complete.
3. No skim synthesis. In direct mode, the synthesis author must read every completed analysis file in full. In packetized mode, each packet reader must read every assigned analysis file in full, and the final synthesizer must read every accepted packet in full. Packetization is a distribution method, not permission to drop files.
4. No source-list theater. Every material claim should be traceable to a cited source, local file, explicit inference, or stated recommendation.
5. No hidden truncation. Committed analysis files must be complete. Do not replace bibliography sections with "truncated for brevity" notes.
6. No source code edits during research unless the user explicitly changes the task from research to implementation.
7. No remote git operations in this repository family. Local commits are expected for completed research artifacts.
8. No soft-wrapped Markdown. Keep paragraphs and list items as single logical lines, matching the repository documentation convention.
9. Preserve user and unrelated worktree changes. Read the tree state before editing, and never revert unrelated changes.
10. Use files as durable state. Long research runs must be resumable from `README.md`, `RESEARCH_PLAN.md`, completed analyses, and git commits.
11. No accepting partial child output. A subagent track is complete only after the parent verifies a durable full report and moves or commits it into the corpus.
12. No silent context failure. If a subagent or synthesis attempt hits context limits, record the failed agent ID or blocked file, retry with narrower scope when appropriate, or split into smaller packets. Do not smooth over the failure.
13. Supplemental user spot-checks remain Phase B. If the user asks for extra tracks while reviewing the corpus, create a Phase B supplement, update the manifest, and keep synthesis gated.
14. Post-synthesis supplemental research must refresh the synthesis. If new `analysis-NN--*.md` files are added after `synthesis.md` already exists, create a new packet, update the synthesis from all accepted packets, update the manifest, and remove stale corpus-count/status language.

## Directory Layout

Create research output under:

```text
_research/{topic_slug}/
```

Use lowercase kebab or snake style for `{topic_slug}` based on local convention. Prefer descriptive slugs over abbreviations.

Recommended structure:

```text
_research/{topic_slug}/
  README.md
  RESEARCH_PLAN.md
  analysis-01--problem-framing.md
  analysis-02--baseline-landscape.md
  ...
  analysis-46--unknown-unknowns-and-dealbreakers.md
  analysis-47--prior-art-reconciliation.md
  SYNTHESIS_BRIEF.md
  synthesis.md
```

Number files with zero-padded two-digit prefixes. If the corpus exceeds 99 tracks, use three digits from the start.

## Phase 0: Classify the Request

Before researching, classify the user's ask:

| Request type | Codex behavior |
|--------------|----------------|
| "quick answer", "short overview", "first pass", "rough scan" | Produce a lightweight answer or a small memo, with sources if current facts are involved |
| "research", "investigate", "compare" with narrow scope | Create a focused research directory with enough tracks to answer the question defensibly |
| "extensive deep research", "as broadly and thoroughly as possible", "decision-grade", "all possible factors", "vast amount" | Run this full workflow with a large track map, capstones, synthesis brief, and synthesis gate |
| "use subagents", "parallel agents", "delegate tracks" | Use explicit-subagent mode, still following all corpus and gate rules |

If the user gives a broad deep-research request without a track count, Codex should choose a corpus scale that fits the ambiguity and stakes. Do not ask the user whether they meant a light skim unless the request is genuinely contradictory.

## Phase 1: Grounding Pass

Start from the local project, not the web.

Read the local files that define project intent, workflow constraints, and relevant prior work. At minimum, inspect root project docs, `CLAUDE.md`, `_workflows/README.md`, `workflow_research.md`, any user-mentioned files, and any domain-specific specs, plans, backlog items, or reference artifacts that the user identifies.

Use `rg` and `rg --files` first. Search for exact phrases from the user request, domain terms, project names, and related concept words. If the user mentions "read any files containing X", run an explicit `rg -l "X"` and record the files inspected.

Record the grounding set in `README.md` or `RESEARCH_PLAN.md`:

```markdown
## Grounding Sources Read

- `README.md`
- `CLAUDE.md`
- `_workflows/workflow_research.md`
- `_workflows/EFFICIENCY_RULES.md`
- `_stages_and_phases/...`
```

Also record any explicitly relevant files that were not read and why. This prevents accidental overclaiming.

## Phase 2: Define Research Questions and Decision Outputs

Write the research questions before creating tracks. A good deep-research plan has five to ten core questions that anchor the corpus.

Each question should make the desired output concrete:

- What decision will this research enable?
- What product, architecture, data, legal, operational, or market uncertainty does it reduce?
- What evidence would change the recommendation?
- Which facts are likely to be current, jurisdiction-specific, licensed, or otherwise unstable enough to require web verification?
- Which topics require primary sources rather than summaries?

For product-concept research, include both feasibility questions and product-shape questions. For technical architecture research, include implementation, migration, operations, and failure-mode questions. For regulatory research, include jurisdiction, authority, date, enforcement, and unresolved ambiguity.

## Phase 3: Create the Research Plan

Before executing tracks, create `RESEARCH_PLAN.md`.

The plan must be specific enough that a future Codex session or explicitly authorized subagent can execute any track from its row alone.

Each track row should include:

| Field | Requirement |
|-------|-------------|
| Track | `NN` |
| Output file | Exact `analysis-NN--slug.md` path |
| Cluster | Thematic group |
| Assignment | Two to five sentences with concrete questions and expected comparisons |
| Source strategy | Primary sources, local files, government sites, vendor docs, papers, datasets, or other required source classes |
| Dependencies | Prior tracks that must be read first, if any |
| Acceptance bar | What makes the analysis complete enough to commit |
| Status | Pending, In-flight, Complete, Blocked |

Do not make a vague row like "Research data sources". Split it into narrower tracks such as parcel/assessor records, building permits, MLS/comps, geospatial hazards, regulatory data, and vendor licensing.

For broad research, plan clusters and waves:

- Foundation tracks: problem framing, user jobs, current-state baseline, vocabulary, assumptions.
- Domain-data tracks: each major data family, primary source, vendor category, or jurisdiction.
- Technical tracks: ingestion, storage, modeling, feature engineering, uncertainty, explainability, operations.
- Product tracks: user workflows, UX surfaces, explanation formats, trust, sales and support consequences.
- Compliance tracks: licenses, privacy, fair housing, appraisal/AVM rules, jurisdictional regulation.
- Case-study tracks: realistic geographies or representative scenarios.
- Capstone tracks: comparison matrix, target architecture, unknown-unknowns and dealbreakers, prior-art reconciliation, final recommendation inputs.

For major ambiguous work, 30 to 60 tracks is normal. For focused decision research, 10 to 20 tracks may be enough. Fewer than 10 tracks should be treated as a survey unless the question is narrow.

## Phase 4: Create the README Manifest

Create `README.md` before execution begins. This file is the live state of the research run.

Required sections:

```markdown
# {Research Title}

## Status

Phase: Phase A planning / Phase B analysis / Phase C synthesis gate / Phase D synthesis complete
Last updated: {date if useful}
Current mode: Codex solo full-corpus / Codex explicit-subagent

## Objective

## Grounding Sources Read

## Research Questions

## Track Status

| Track | File | Cluster | Status | Notes |
|-------|------|---------|--------|-------|

## Dispatch Queue

## Completed Outputs

## Known Gaps and Follow-ups

## Resume Instructions
```

The manifest is not paperwork. It is the crash-recovery state and the user's progress view. Update it after each completed track or coherent batch.

If the project expects local commits after logical units, commit the initial `README.md` and `RESEARCH_PLAN.md` before a long execution wave.

## Phase 5A: Execute in Codex Solo Full-Corpus Mode

Use this path when the user has not explicitly authorized subagents.

Solo mode still means full research. It does not mean "write one synthesis from a skim".

Execution rules:

1. Work track by track from the `RESEARCH_PLAN.md`.
2. Use local files for project grounding and web browsing for current, jurisdictional, vendor, legal, market, or data-source facts.
3. Prefer primary sources for laws, regulations, official datasets, standards, APIs, technical docs, and product claims.
4. Write each `analysis-NN--slug.md` as a complete report before moving on.
5. Update `README.md` status after each track or after a small batch.
6. Commit periodically so a later session can resume without reconstructing work from chat history.
7. Do not begin synthesis until every planned analysis is complete or explicitly marked out of scope with a reason.

Solo mode can still be ambitious because the corpus is persisted in files. Codex should use the repository as long-term memory and keep the run resumable across context compaction.

## Phase 5B: Execute in Explicit-Subagent Mode

Use this path only when the user explicitly asks for subagents, delegation, or parallel agent work.

Codex subagent rules:

1. Do a quick local plan first. Identify the immediate critical path task for the main agent and the independent sidecar tasks for subagents.
2. Spawn only concrete, bounded, self-contained tracks.
3. Keep at most three research agents active unless the current harness or user explicitly allows a different cap. If the user authorizes a larger cap, use it opportunistically, but respect the actual harness limit. In the FracRealHomes validation run, the user authorized up to 10 and the effective open-thread cap was 6.
4. Do not launch overlapping tracks that will duplicate source discovery or analysis.
5. Verify local prerequisite paths before launch. Do not put guessed, stale, topic-equivalent, or remembered filenames into a child prompt.
6. Do not launch a track whose required prerequisite analysis files are still in flight unless the child prompt explicitly says those dependencies are unavailable and must not be relied on.
7. Do not hand off the parent agent's immediate blocking task.
8. While agents run, do meaningful non-overlapping work locally.
9. Use `wait_agent` sparingly, only when the next local step needs the result.
10. Close agents after their results have been captured.
11. Record agent IDs, assigned tracks, launch time, completion state, and handoff location in `README.md`.
12. Parent Codex remains accountable for checking completeness, citations, formatting, and integration.
13. Prefer batches of independent tracks. For broad research, a rolling queue works well: launch a wave, accept/commit finished outputs, close completed agents, then launch the next wave.
14. Treat context-window failures as normal recoverable events. Close the failed agent, record it in the manifest, and retry with a narrower prompt that reads only necessary local excerpts and spends context on the assigned research.
15. Treat local-file mismatch failures as preventable parent errors. Fix the prompt's exact paths and retry rather than asking the child to infer "closest matching" prerequisites.
16. For each returned track, perform an acceptance gate before moving it into the corpus: `wc -l`, required-section scan, TODO/TBD/truncation scan, source URL scan, ASCII scan if local convention requires it, prerequisite-mismatch scan, and a quick content check against the user request.
17. Move accepted `/tmp` reports into the corpus with the exact planned filename. Do not mark a track complete from an agent's final status alone.
18. Commit coherent batches. For large runs, committing after each successful wave prevents losing progress and makes resume instructions meaningful.

### Local Prerequisite Preflight

Before spawning a subagent, the parent must create the local-file list from the filesystem or manifest, not from memory or a previous summary.

Use exact-path discovery:

```bash
find _research/{topic_slug} -maxdepth 1 -type f -name 'analysis-[0-9][0-9]--*.md' | sort
rg --files _research/{topic_slug} README.md CLAUDE.md _workflows | sort
```

For each `Read first` path in the prompt, run a preflight check:

```bash
for f in \
  README.md \
  CLAUDE.md \
  _research/{topic_slug}/README.md \
  _research/{topic_slug}/RESEARCH_PLAN.md \
  _research/{topic_slug}/analysis-NN--exact-slug.md
do
  test -f "$f" || echo "MISSING: $f"
done
```

Preflight rules:

- If a file is required and missing, do not launch the child. Fix the path, wait for the dependency track, or mark the child track blocked.
- If a file is optional and missing, either omit it from the prompt or label it explicitly as optional and unavailable.
- If the intended dependency is thematic rather than exact, resolve the exact current filename in the parent before launch. Do not ask the child to guess.
- If the manifest and disk disagree, inspect and correct the manifest before launching dependent children.
- If tracks are launched in parallel, do not list same-wave outputs as prerequisites unless they already exist on disk and have passed parent acceptance.

Subagent prompts should say one of these, as appropriate:

```text
All local prerequisite paths listed below were verified by the parent before launch.
```

or:

```text
No prior analysis files are required for this track. Use the research README/plan for context and perform independent primary-source research.
```

Avoid this pattern:

```text
Read analysis-24--some-remembered-title.md if present, otherwise use closest matching files.
```

That pattern creates noise, makes the child spend context on file discovery, and can bias the research if the child chooses a weaker substitute.

Subagent prompts should be precise. Include:

- The research directory path.
- The exact output file name.
- The track assignment.
- Local grounding files that must be read, using parent-verified exact paths.
- A statement that required local paths were verified by the parent before launch.
- Required source classes.
- Required report structure.
- Instruction not to edit source code.
- Instruction not to revert unrelated changes.
- Instruction to write the full Markdown report to `/tmp/{project-slug}-{NN}.md` when the current harness supports parent-readable `/tmp` handoff.
- Instruction to return the full Markdown report if direct file persistence is unavailable.
- Instruction to include full URLs and bibliography.
- Instruction to distinguish facts, inferences, and recommendations.
- Instruction to keep within a target size range when useful, usually 250-500 lines for a normal research track and longer for capstones.
- Current date, because law, maps, prices, product docs, and public officials can change.
- Instruction that if a required local prerequisite is missing despite parent verification, the child should stop and report `PREREQUISITE_PATH_MISMATCH` instead of substituting the closest file.

Template:

```text
You are running Track {NN}: {Title} for a Codex deep-research project.

Repository: {repo path}
Research directory: {research dir}
Output target after parent acceptance: {analysis-NN--slug.md}
Temporary handoff: /tmp/{project-slug}-{NN}.md

The parent verified that all required local paths below exist before launch. If any required path is missing, stop and report PREREQUISITE_PATH_MISMATCH. Do not silently substitute closest matching files.

Read first:
- {local grounding doc 1}
- {local grounding doc 2}
- {RESEARCH_PLAN.md}

Assignment:
{2-5 sentence track brief}

Source strategy:
{primary sources, official docs, datasets, vendor docs, papers, local files}

Write a complete Markdown analysis to the temporary handoff path with:
- Summary
- Methodology
- Findings with numbered F1/F2/F3 headings
- Recommendations or implications with numbered R1/R2/R3 headings
- Risks, gaps, and confidence
- Sources with complete URLs

Distinguish facts, inferences, recommendations, and open questions. Use authoritative/current sources where possible. Do not edit application source code. Do not modify unrelated research files. If you cannot write the output file in a way the parent can inspect, return the complete Markdown report in your final response, not a summary.
```

Parent acceptance commands should look like:

```bash
wc -l /tmp/{project-slug}-{NN}.md
rg -n "^(#|##)|https?://|TODO|TBD|FIXME|truncated|Sources|PREREQUISITE_PATH_MISMATCH|requested local filenames|closest matching|not present on disk|not present in the research directory" /tmp/{project-slug}-{NN}.md
LC_ALL=C grep -nP '[^\x00-\x7F]' /tmp/{project-slug}-{NN}.md
mv /tmp/{project-slug}-{NN}.md _research/{topic_slug}/analysis-NN--slug.md
```

If the acceptance scan finds a prerequisite mismatch note, classify it before accepting:

- Acceptable: the prompt explicitly marked the prerequisite optional or same-wave unavailable, and the report correctly avoided relying on it.
- Not acceptable: the child mapped guessed filenames to "closest matching" files, missed required local context, or used outdated dependency names. Retry with corrected exact paths.

## Phase 5C: Supplemental Spot-Check Batches Before Synthesis

Use this path when the user reviews the Phase B corpus before approving synthesis and raises additional topics, corrections, or "make sure this is covered" notes. If `synthesis.md` already exists, use Phase 10A instead.

Supplemental rules:

1. Treat the work as a Phase B supplement, not Phase C synthesis.
2. Scan the existing corpus first with `rg` to determine whether each topic is already covered.
3. Do not create duplicate tracks when coverage is already strong. Instead, add a short manifest coverage note if useful.
4. Create new supplemental `analysis-NN--slug.md` tracks only for thin or missing coverage.
5. Add a `Supplemental Spot-Check Tracks` section to `README.md` with agent IDs, status, and notes.
6. Update the manifest status to something like `PHASE_B_SUPPLEMENT_IN_PROGRESS_SYNTHESIS_GATED`, then `PHASE_B_SUPPLEMENT_COMPLETE_SYNTHESIS_GATED`.
7. Keep the Phase C gate intact. Do not create `synthesis.md` while supplemental tracks are in flight.
8. Commit the supplemental batch separately so the review history is clear.

The FracRealHomes validation run used this pattern for:

- Overlay map layers, source visibility, and weighting-factor conversion.
- California wildfire map updates, utility ignition, and insurance stress.
- High-voltage power lines, EMF science versus public sentiment, and valuation.
- Cascadia Subduction Zone, liquefaction/tsunami, and media-salience risk.
- General news/scientific/regulatory/pop-culture shock event modeling and human override ranges.

## Phase 6: Analysis File Quality Bar

Each `analysis-NN--slug.md` must be self-contained enough to be useful months later.

Required structure:

```markdown
# Analysis NN: {Title}

## Summary

## Methodology

## Findings

### F1. {Finding}

### F2. {Finding}

## Recommendations / Implications

### R1. {Recommendation}

## Risks, Gaps, and Confidence

## Sources
```

For tracks that compare options, include a matrix and a narrative. For tracks that evaluate data sources, include coverage, authority, freshness, granularity, cost/licensing, API/export access, update cadence, failure modes, and product fit. For regulatory tracks, include jurisdiction, authority, effective date if available, enforcement mechanism, ambiguity, and primary-source links. For modeling tracks, include target variables, feature candidates, labels, leakage risks, uncertainty, validation, monitoring, and human review. For product tracks, include target users, workflow consequences, explainability, trust, and operational burden.

Normal tracks should be substantial. In the FracRealHomes validation run, accepted tracks commonly landed around 250-450 lines, with longer files for permit platforms, source/legal tracks, case studies, capstones, and supplemental shock modeling. Do not pad a thin topic, but if a broad track is only a few dozen lines, it is almost certainly a skim, a too-broad assignment, or a source gap that must be explicitly stated and possibly split. Capstone tracks should usually be among the longest files because they read and reconcile prior analyses.

Every analysis must distinguish:

- Facts from sources.
- Inferences drawn by Codex.
- Recommendations.
- Open questions.
- Known gaps.

Every accepted analysis should also include:

- Complete source URLs for material current/public-source claims.
- Effective dates or publication dates for laws, maps, regulations, agency releases, and time-sensitive datasets.
- Licensing/terms caveats when data could be displayed, cached, transformed, or used for model features.
- Model/product implications, not just source description.
- Admin or human-review implications when automated evidence is incomplete or high-risk.

## Phase 7: Capstone Tracks

A decision-grade deep-research corpus needs capstones. Do not skip them just because the raw tracks feel complete.

Recommended capstones:

| Capstone | Purpose |
|----------|---------|
| Comparative matrix | Puts candidates, data sources, architectures, jurisdictions, or strategies side by side |
| Target architecture / operating model | Converts findings into a concrete system or process shape |
| Unknown-unknowns and dealbreakers | Adversarially searches for reasons the emerging recommendation could fail |
| Prior-art reconciliation | Compares findings against local project assumptions, earlier research, and known examples |
| MVP / sequencing plan | Separates v1, later, and someday work without losing the larger vision |

Capstones must cite earlier analysis files and external sources. They should correct weak assumptions, identify contradictions, and surface disagreements rather than smoothing them away.

## Phase 8: Phase B -> Phase C Gate

After all planned analyses and capstones are complete, stop before synthesis.

Hard gate:

1. Update `README.md` with all track statuses.
2. Ensure every completed analysis is committed or staged for commit according to local repo practice.
3. Run corpus checks: file count, line count, TODO/TBD/truncation scan, and `git status --short`.
4. Summarize the corpus state for the user.
5. Ask for explicit approval to begin synthesis.

Do not infer gate approval from the original research request. The gate exists because synthesis canonizes the framing. It gives the user a chance to spot thin tracks, redirect the framing, or request additional analysis before the final synthesis is written.

If the user wants to inspect the eventual synthesis subagent prompt before approval, write `PHASE_C_SYNTHESIS_SUBAGENT_PROMPT.md` as a gated artifact and commit it. This file is not permission to launch the subagent. It is a reviewable launch plan.

If the user explicitly instructs Codex in advance to run analysis and synthesis in one uninterrupted pass, still create the gate artifact and make the gate visible in `README.md`. In repositories that treat the gate as a hard workflow rule, stop anyway and wait.

## Phase 9: Synthesis Brief, Packet Plan, or Launch Prompt

Before writing `synthesis.md`, write `SYNTHESIS_BRIEF.md`, a packet plan, or an equivalent user-reviewable `PHASE_C_SYNTHESIS_SUBAGENT_PROMPT.md`.

The synthesis brief is a machine-readable handoff from the research corpus to the packet readers and final synthesis author. It should be concise but complete. If using subagents for packet reading or final synthesis, the launch prompt can carry the same content plus the exact child-agent instructions.

Required sections:

```markdown
# Synthesis Brief: {Research Title}

## Task

## Corpus

## Must-Read Rule

## Emerged Answer / Architecture / Recommendation

## Cross-Cutting Convergence

## Contradictions and Tensions

## Corrections to Apply

## Track Index

## Open Questions

## Suggested Synthesis Structure

## Explicit Constraints
```

The brief must name every analysis file. It should also call out weak tracks, overconfident claims, source limitations, and areas where the synthesis must not overreach.

For packetized synthesis, the brief or prompt must also include:

- The packet count and packet boundaries.
- Exact parent-verified file lists for each packet.
- The expected packet output filenames under `phase_c_packets/`.
- The selected high-priority original analyses, if any, that the final synthesizer should reread directly in addition to packets.
- A rule that packet readers must stop with `PREREQUISITE_PATH_MISMATCH` if a required file is missing.
- A rule that the final synthesizer must read every accepted packet in full and disclose packet coverage in `synthesis.md`.

For direct clean-context synthesis, the launch prompt must also include:

- Parent launch notes: wait for explicit user approval, launch with `fork_context: false`, use high reasoning, and do not spawn further subagents on the first attempt unless the user asks.
- A non-negotiable no-skim rule requiring every required input file to be read start-to-finish.
- A line-count/read-ledger requirement.
- A context-blocked fallback: if the subagent cannot honestly complete the full read, it must not write `synthesis.md`; it should write a blocked note such as `/tmp/{project-slug}_phase_c_context_blocked.md`.
- The exact required file list.
- The desired synthesis structure and mandatory concepts to preserve.
- A final verification checklist for the child agent.

Measure corpus size before writing the prompt:

```bash
wc -l -w -c _research/{topic_slug}/analysis-[0-9][0-9]--*.md _research/{topic_slug}/README.md _research/{topic_slug}/RESEARCH_PLAN.md
du -ch _research/{topic_slug}/analysis-[0-9][0-9]--*.md _research/{topic_slug}/README.md _research/{topic_slug}/RESEARCH_PLAN.md | tail -1
```

## Phase 10: Synthesis

Write `synthesis.md` only after the raw corpus is complete and either the synthesis author has read every analysis file in full or accepted packet readers have read every assigned analysis file in full and the final synthesizer has read every accepted packet in full.

Required synthesis qualities:

- Integrated recommendation, not a stitched summary.
- Clear separation between evidence, inference, and recommendation.
- Decision-grade treatment of tradeoffs, not just pros and cons.
- Explicit discussion of dealbreakers, uncertainties, validation steps, and deferred topics.
- Corrections to local project assumptions where the research changed the frame.
- Practical next steps, spikes, or implementation roadmap if relevant.
- Confidence read.

Recommended structure:

```markdown
# Synthesis: {Research Title}

## Executive Recommendation

## What the Research Changed

## Core Findings

## Recommended Direction

## Architecture / Operating Model / Product Shape

## Data Sources / Evidence Base

## Risks and Dealbreakers

## Validation Spikes

## v1 vs Later

## Open Questions

## Explicit Gate for Implementation

## Confidence Read
```

Default packetized synthesis pattern:

For full deep-research runs, packetization is the standard Phase C intermediate, not merely a fallback. The final `synthesis.md` should be written from accepted packets plus any selected high-priority original files needed for detail, conflict resolution, or user-specified emphasis.

A one-packet run is valid. The packet is not supposed to be a straight copy of `synthesis.md`; it is a structured extraction layer with a read ledger, source/data/model/product/legal implications, conflicts, and must-preserve points. The synthesis is the integrated recommendation that uses that extraction layer. Keeping even a single packet gives future supplemental tracks somewhere clean to attach.

Direct one-shot synthesis without packets is acceptable only for lightweight/survey work, narrow focused research where the user did not request the full deep-research workflow, or an explicit user request to skip the packet layer. If a direct one-shot is attempted and context blocks, preserve the blocked note and switch to the packet procedure below.

Packet sizing guidance:

| Corpus size | Default packet count | Notes |
|-------------|----------------------|-------|
| 1-10 analysis files or up to about 5,000 source lines | 1 packet | Use `packet-01--full-corpus.md` or a topic-specific name. Parent may write it directly if context is sufficient and every file is read in full. |
| 11-25 analysis files or about 5,000-12,000 source lines | 2-3 packets | Split by semantic cluster first, then line count. |
| 26-50 analysis files or about 12,000-25,000 source lines | 4-6 packets | This is usually the point where multiple packet readers materially improve quality and context hygiene. |
| 51-90 analysis files or about 25,000-45,000 source lines | 6-10 packets | Use the maximum user-authorized/harness-practical concurrency, but keep packet boundaries coherent. |
| More than 90 analysis files or more than about 45,000 source lines | 8-10 packets plus possible super-synthesis | Consider a second-level synthesis layer only if packets themselves become too large for a clean final pass. |

Heuristics:

- Prefer semantic coherence over exact packet size.
- Target about 2,500-5,000 source lines or 5-12 normal analysis files per packet.
- Split a packet if it would exceed about 7,500 source lines, 15 normal analysis files, or a mix of unusually long capstones/legal/source reports.
- Keep capstones with the tracks they reconcile when possible, but split them out if they are large enough to dominate a packet.
- Include project/workflow/research README/plan context in packet 01 unless there is a better reason to dedicate a separate context packet.
- If subagents are explicitly authorized, use reader subagents for multi-packet runs. Without explicit authorization, the parent Codex can still create packets sequentially.
- The final `synthesis.md` must disclose the packetized read method and packet coverage.
- Do not use packetization to evade the no-skim rule. It is a distribution method, not a summarization shortcut.

Packet creation procedure:

1. If this is a recovery from a context-blocked one-shot attempt, close the context-blocked agent and preserve its final status in the manifest. Record the agent ID, last fully read file, blocked file/range, and blocked note path. If no one-shot was attempted, record that packetization was selected as the standard Phase C path.
2. If a blocked note or partial `synthesis.md` exists, inspect it. Reject any partial `synthesis.md` unless the child explicitly completed the no-skim read. Delete or archive partial output before proceeding so it cannot be mistaken for accepted Phase C work.
3. Preflight the corpus from disk, not memory:

```bash
find _research/{topic_slug} -maxdepth 1 -type f -name 'analysis-[0-9][0-9]--*.md' | sort
wc -l _research/{topic_slug}/analysis-[0-9][0-9]--*.md _research/{topic_slug}/README.md _research/{topic_slug}/RESEARCH_PLAN.md
```

4. Split packets by semantic cluster and rough line count using the sizing guidance above.
5. For each reader packet, provide exact parent-verified file paths. Do not ask readers to discover or infer filenames. If any required path is missing, the reader must stop with `PREREQUISITE_PATH_MISMATCH` rather than substituting a closest match.
6. Require each reader to write one `/tmp/{project-slug}-phasec-packet-NN.md` handoff and to avoid repository edits. If `/tmp` handoff is not available, require the complete packet in the final response.
7. Require each packet to include these sections:

```markdown
# Phase C Reader Packet NN: {Title}

## Scope And Files Read

## Read Confirmation

## Key Extracted Findings

## Source/Data Implications

## Model/Architecture Implications

## Product/UX/Admin Implications

## Legal/Compliance/License Risks

## Conflicts/Tensions/Corrections Needed

## Must-Preserve Points For Final Synthesis

## Candidate Synthesis Structure Notes

## Sources And File References
```

8. The `Read Confirmation` section must be a table with exact path, `wc -l`, last line read, and status. A packet that only summarizes a cluster without a read ledger is not accepted.
9. Require readers to classify historical prerequisite-mismatch notes inside older analysis files. If all assigned paths now exist and were fully read, those old notes can be treated as historical parallel-wave artifacts. If an assigned prerequisite is actually missing, the packet is blocked.
10. Parent acceptance checks for each packet:

```bash
wc -l /tmp/{project-slug}-phasec-packet-NN.md
rg -n "^(#|##)|TODO|TBD|FIXME|truncated|PREREQUISITE_PATH_MISMATCH|requested local filenames|closest matching|not present on disk|not present in the research directory|CONTEXT_LIMIT_BLOCKED|https?://" /tmp/{project-slug}-phasec-packet-NN.md
LC_ALL=C grep -nP '[^\x00-\x7F]' /tmp/{project-slug}-phasec-packet-NN.md
```

11. Run a consolidated coverage check after all packets return. Verify that every expected `analysis-NN--*.md` file and required context file appears in at least one accepted packet.
12. Move accepted packets into `_research/{topic_slug}/phase_c_packets/` with stable names such as `packet-01--product-and-baseline.md`.
13. Write `PHASE_C_PACKET_SYNTHESIS_SUBAGENT_PROMPT.md`. It should explain why packetization was used, name every packet file, name selected high-priority original analyses for direct rereading, preserve the original desired synthesis structure and mandatory concepts, require a packet no-skim read, and specify a packet-synthesis blocked note such as `/tmp/{project-slug}_phase_c_packet_synthesis_context_blocked.md`.
14. Commit the accepted packets, packet-synthesis prompt, and manifest update as a checkpoint before launching the final packet synthesizer. This makes the synthesis resumable if the final synthesizer fails.
15. Launch one final synthesizer with `fork_context: false`. It should read the packet-synthesis prompt from disk, write only `synthesis.md`, not spawn subagents, and stop with the packet blocked note if it cannot complete the packet no-skim read.
16. Parent verifies the final `synthesis.md`: line count, required section scan, mandatory-concept scan, placeholder/truncation scan, ASCII scan if required, blocked-note absence, and a read-through for coherence. Then update the manifest to the completed synthesis status and commit.

The FracRealHomes validation run used this procedure successfully after the one-shot child blocked before `analysis-01`. Six initial reader packets totaling 1,143 lines were accepted, a packet-synthesis prompt was committed, and a final clean-context packet synthesizer produced an 808-line synthesis. Later, five post-synthesis tracks were added, Packet 07 was created as a 147-line supplemental packet, and the final synthesis was refreshed to 960 lines from all seven packets. Treat this as the current best known pattern for very large Codex research corpora.

## Phase 10A: Post-Synthesis Supplemental Research Refresh

Use this path when `synthesis.md` already exists and the user asks for additional deep-research topics, new analysis tracks, or a broadened scope.

The default is a refreshed synthesis, not a loose addendum. An addendum is acceptable only if the user explicitly asks for a separate addendum or the late material is intentionally out of scope for the canonical synthesis.

Procedure:

1. Search the existing corpus first. Use `rg` against `analysis-*.md`, `phase_c_packets/`, and `synthesis.md` to determine whether the new topics are already covered, thinly covered, or missing.
2. If coverage is already strong, add a manifest note or small synthesis clarification instead of creating duplicate tracks.
3. If new research is needed, append continuous numbered tracks such as `analysis-69--slug.md`. Do not renumber older analyses.
4. Update `README.md` before launching work. Use a status such as `PHASE_B_SUPPLEMENT_IN_PROGRESS_POST_SYNTHESIS` or `PHASE_B_SUPPLEMENT_COMPLETE_POST_SYNTHESIS` until the synthesis refresh is complete.
5. Execute the new tracks under the normal Phase 5A or 5B rules. The same acceptance checks apply: line count, section/source scan, TODO/truncation scan, prerequisite-mismatch scan, ASCII/format check if required, and content review.
6. Commit the accepted new analysis files as their own checkpoint when the batch is complete.
7. Create the next packet under `phase_c_packets/`, for example `packet-07--connectivity-utilities-resilience-and-owner-use-continuity.md`.
8. The supplemental packet must read every new analysis file in full and include the standard packet sections, especially `Read Confirmation` with exact path, `wc -l`, last line read, and status.
9. The supplemental packet should explicitly explain that it is a bridge from late analyses into the already packetized synthesis. It should not pretend to be a full replacement for earlier packets.
10. The parent may write the supplemental packet directly if the late batch fits in context and the parent has read the new files in full. Otherwise, launch an authorized packet-reader subagent with exact parent-verified paths.
11. Refresh `synthesis.md` from all accepted packets, including the new packet. If the original run had only one packet, the late supplement becomes `packet-02--*.md` and the refreshed synthesis uses packet 01 plus packet 02. Do not synthesize only from the new packet and append a summary to the bottom.
12. If the existing synthesis was packetized, the refresh can use the accepted packets as the compressed record for prior tracks plus the new packet for late tracks. Directly reread selected original analyses only when needed to preserve detail, resolve conflicts, or satisfy the prompt.
13. Update the synthesis header, scope, method, executive summary, output families, model architecture, source matrix, roadmap, risk register, open questions, next decisions, implementation guardrails, and corpus read confirmation wherever the late tracks change the product recommendation.
14. Update `README.md` so it no longer says the late tracks require an addendum or refreshed synthesis. The status should move to a completed synthesis state such as `PHASE_D_SYNTHESIS_COMPLETE_TRACKS_01_73`.
15. Run stale-language checks tailored to the old corpus state. Search for old track ranges, packet counts, and pending-refresh language:

```bash
rg -n "01-68|six accepted|six Phase C|Complete for tracks 01-68|require a synthesis addendum|require.*refreshed synthesis|post-synthesis supplemental tracks .* require|PHASE_B_SUPPLEMENT_COMPLETE_POST_SYNTHESIS" _research/{topic_slug}
```

16. Run normal verification:

```bash
wc -l _research/{topic_slug}/analysis-[0-9][0-9]--*.md _research/{topic_slug}/README.md _research/{topic_slug}/RESEARCH_PLAN.md | tail -1
wc -l _research/{topic_slug}/phase_c_packets/packet-*.md _research/{topic_slug}/synthesis.md | tail -1
git diff --check
git status --short
```

17. Commit the supplemental packet, refreshed `synthesis.md`, and manifest update. Use a commit message that makes the refresh explicit, such as `Research: refresh synthesis for tracks 69-73`.

Required final state:

- The new analysis files exist and are committed.
- The new packet exists and has a read ledger.
- `synthesis.md` states the new full corpus range and packet count.
- `README.md` states the new full corpus range and completed synthesis status.
- Stale references to the previous corpus range are gone except where intentionally historical.
- The final response links the packet, synthesis, README, and commit hash.

## Phase 11: Verification and Commit

Before final response:

1. Run `git status --short`.
2. Check that all expected research files exist.
3. Count analysis files and compare with `README.md`.
4. Use `rg` to find accidental placeholders such as `TODO`, `TBD`, `Pending`, `In-flight`, `truncated`, `bibliography omitted`, or `CONTEXT_LIMIT_BLOCKED`.
5. Check that README track statuses match the files on disk.
6. For Markdown-only work, no application tests are normally required; say that explicitly.
7. Commit local research artifacts when the repository convention expects commits.
8. Final response should link the created files, mention verification, and include the commit hash if committed.

Suggested checks:

```bash
rg --files _research/{topic_slug}
rg -n "TODO|TBD|Pending|In-flight|truncated|bibliography omitted|CONTEXT_LIMIT_BLOCKED" _research/{topic_slug}
wc -l _research/{topic_slug}/*.md
find _research/{topic_slug} -maxdepth 1 -type f -name 'analysis-[0-9][0-9]--*.md' | wc -l
git status --short
```

## Common Failure Modes

### Lightweight Skim

Failure: The user asks for extensive deep research and Codex produces a handful of short docs plus a synthesis.

Prevention: Create a track map first. For broad work, plan dozens of analyses and capstones. Do not write synthesis until the corpus exists.

### First-Pass Summary Drift

Failure: Codex produces something accurate but summary-like, then treats it as the deep-research deliverable.

Prevention: If the user compares the output to a reference corpus or asks for "40+ sections" / "extensive tracks", create or revise the Codex workflow and rerun as a corpus. Archive the first pass so it does not become the accepted synthesis.

### Premature Synthesis

Failure: Codex reads local docs and immediately forms a recommendation.

Prevention: Separate Phase B analysis from Phase C synthesis. Preserve the hard gate.

### Source-List Theater

Failure: A report lists sources but does not make claims traceable.

Prevention: Use inline citations, source-specific findings, and explicit inference labels.

### Phantom Subagent Work

Failure: The parent assumes delegated work happened, but no durable file or complete response exists.

Prevention: Track agent IDs and handoffs. Verify actual output before marking a track complete.

### Context Exhaustion In A Child Agent

Failure: A child agent reads too much local context, exhausts the model context, and returns no usable output.

Prevention: Record the failed agent ID, close it, and retry with a narrower prompt. Tell the retry to read targeted local snippets instead of whole prior files when the assignment mainly needs fresh external research.

### Unverified `/tmp` Handoff

Failure: A child says it wrote `/tmp/project-NN.md`, but the parent moves or marks complete without checking content.

Prevention: Run line count, section/source scans, ASCII/format checks, and a content spot-check before moving the file into the corpus.

### Prerequisite Filename Drift

Failure: Parent prompts include stale or guessed filenames, so the child reports that "requested local filenames were named differently" and maps to closest matching files.

Causes: The parent wrote prompts from memory, a compacted summary, a legacy plan, or an earlier file naming scheme instead of current `find`/manifest output. A separate variant happens when parallel tracks list same-wave analyses as prerequisites before those files exist.

Prevention: Run local prerequisite preflight before every subagent launch. Use exact current paths, omit unavailable optional files, and do not launch tracks with required dependencies that are still in flight. Instruct the child to stop with `PREREQUISITE_PATH_MISMATCH` if a required file is missing rather than substituting.

### Duplicated Subagent Work

Failure: Parent and child both research the same topic, wasting time and confusing conclusions.

Prevention: Assign disjoint tracks and keep the parent on non-overlapping work while agents run.

### Duplicate Supplemental Track

Failure: The user asks whether a topic is covered, and Codex launches a new track without checking the existing corpus.

Prevention: `rg` the corpus first. If already covered, add a coverage note. Create supplemental tracks only for genuine gaps or materially thin coverage.

### Stale Synthesis After Late Supplements

Failure: Codex creates post-synthesis analysis files but leaves `synthesis.md` and `README.md` describing the old corpus range.

Prevention: Use Phase 10A. Create the next packet, refresh the synthesis from all accepted packets, update the manifest, and scan for stale old ranges such as `01-68`, old packet counts, or "requires refreshed synthesis" language.

### Lost Orchestrator Judgment

Failure: Individual tracks are good but nobody reconciles contradictions.

Prevention: Require capstone tracks, `SYNTHESIS_BRIEF.md`, accepted packets, and a synthesis that names tensions directly.

### Overfitting to the Exemplar

Failure: Codex copies the exact 47-track shape from the reference even when the problem is smaller or structurally different.

Prevention: Copy the standard of rigor, not the exact count. Let scope determine track count.

### Vendor-Claim Capture

Failure: Vendor docs and marketing pages become unchallenged facts.

Prevention: Prefer primary docs, public records, official datasets, independent standards, and direct API/licensing documentation. Label vendor claims as vendor claims.

### Local Context Loss

Failure: The research drifts away from the product's actual goals.

Prevention: Start from local grounding docs, include prior-art reconciliation, and require capstones to compare findings back to project assumptions.

## Example Seed Track Map: FracRealHomes Next-Gen Property Estimate

This is not a completed research plan. It is a reusable seed map for the current FracRealHomes concept: a next-generation property estimate that combines financial valuation, operating cost, future resale, regulatory constraints, neighborhood and citywide data, and high-end vacation-home intangibles such as white-water ocean views.

Tailor this map before execution. Add, remove, split, and reorder tracks based on the user's latest scope and the local project files.

### Cluster A: Product Frame and Existing Baseline

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 01 | `analysis-01--estimate-product-frame.md` | Define what the next-gen estimate should decide, explain, and influence for fractional vacation-home buyers, managers, and sellers. Separate valuation, suitability, risk, liquidity, and operating-cost outputs. |
| 02 | `analysis-02--fractional-owner-jobs-to-be-done.md` | Research user motivations and constraints for 1/8th luxury fractional ownership, including emotional value, scheduling, liquidity, trust, and post-purchase operations. |
| 03 | `analysis-03--zillow-redfin-avm-baseline.md` | Establish current consumer AVM baselines, public explanation gaps, known limitations, and where a fractional luxury property estimate can be meaningfully different. |
| 04 | `analysis-04--luxury-vacation-home-value-drivers.md` | Identify value drivers that matter disproportionately in high-end vacation homes compared with primary residences, including views, privacy, access, design, provenance, and operating convenience. |

### Cluster B: Property and Transaction Data

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 05 | `analysis-05--mls-comps-and-listing-data.md` | Research MLS, listing, sales-comps, and listing-history data requirements, limits, licenses, and feature opportunities. |
| 06 | `analysis-06--parcel-assessor-tax-records.md` | Research parcel, assessor, tax, lot, building, and ownership data available from counties, states, and aggregators. |
| 07 | `analysis-07--recorder-deed-title-hoa-data.md` | Research recorder, deed, title, easement, HOA, covenant, and ownership-structure records relevant to fractional ownership and resale. |
| 08 | `analysis-08--permit-history-and-renovation-signals.md` | Research building permit histories, inspection records, remodel permits, code enforcement, and how permit signals affect value, risk, and operating cost. |
| 09 | `analysis-09--physical-condition-and-material-quality.md` | Research data sources and modeling approaches for condition, materials, fixtures, appliance age, roof/HVAC/plumbing/electrical life, and reserve planning. |
| 10 | `analysis-10--photos-computer-vision-and-description-mining.md` | Research image, listing text, and computer-vision features for property quality, views, finishes, deferred maintenance, and luxury cues. |
| 11 | `analysis-11--floor-plan-lidar-drone-and-3d-data.md` | Research floor plans, LiDAR, drone imagery, photogrammetry, 3D reconstruction, and view analysis for richer property understanding. |

### Cluster C: Location, Neighborhood, and Intangibles

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 12 | `analysis-12--ocean-view-and-viewshed-modeling.md` | Research methods and data for ocean-view, white-water-view, sunset-view, obstruction-risk, elevation, and line-of-sight valuation. |
| 13 | `analysis-13--beach-access-and-recreation-proximity.md` | Research beach access, trail access, parking, walk time, grade, congestion, and recreation amenities relevant to vacation-home desirability. |
| 14 | `analysis-14--noise-traffic-and-nuisance.md` | Research noise, traffic, airport, rail, nightlife, construction, event, and nuisance data that can materially affect vacation use. |
| 15 | `analysis-15--schools-safety-and-civic-quality.md` | Research schools, crime, emergency response, civic services, governance quality, and how much each matters for fractional luxury buyers. |
| 16 | `analysis-16--amenities-retail-dining-and-lifestyle.md` | Research restaurants, retail, gyms, marinas, clubs, cultural amenities, healthcare, and lifestyle signals for second-home markets. |
| 17 | `analysis-17--microclimate-air-sun-wind-and-comfort.md` | Research microclimate, marine layer, wind, sun exposure, air quality, heat, humidity, and seasonal comfort factors. |
| 18 | `analysis-18--hazards-insurance-and-climate-risk.md` | Research wildfire, flood, seismic, landslide, storm surge, sea-level rise, insurance availability, and premium risk. |

### Cluster D: Permitting, Zoning, and Regulatory Context

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 19 | `analysis-19--manhattan-beach-planning-zoning-and-permits.md` | Deep dive Manhattan Beach planning, zoning, permits, coastal constraints, view and height issues, remodel timelines, and official data sources. |
| 20 | `analysis-20--california-coastal-commission-and-lcp.md` | Research California Coastal Commission, local coastal programs, coastal permits, appeals, and how coastal regulation affects value and redevelopment optionality. |
| 21 | `analysis-21--adu-short-term-rental-and-occupancy-rules.md` | Research ADU, short-term rental, occupancy, rental restrictions, transient occupancy tax, and use constraints relevant to fractional ownership. |
| 22 | `analysis-22--historic-hoa-covenant-and-private-restrictions.md` | Research private restrictions, HOAs, historic districts, design review, architectural controls, and recorded covenants. |
| 23 | `analysis-23--fractional-ownership-legal-and-disclosure-risks.md` | Research ownership structure, securities/timeshare/fractional disclosures, resale rights, governance, and jurisdiction-specific risk areas. |

### Cluster E: Operating Cost, Lifecycle Cost, and Resale

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 24 | `analysis-24--insurance-taxes-hoa-and-utilities.md` | Research recurring cost drivers, data sources, volatility, and forecasting for insurance, taxes, HOA, utilities, and local assessments. |
| 25 | `analysis-25--maintenance-reserves-and-capex-modeling.md` | Research lifecycle reserve models for luxury residential assets, including preventive maintenance, replacement schedules, and shared-owner expectations. |
| 26 | `analysis-26--rental-revenue-and-use-offsets.md` | Research whether rental revenue, exchange programs, or owner-use offsets should be modeled, including legal and operational constraints. |
| 27 | `analysis-27--fractional-resale-liquidity-and-discount-premium.md` | Research resale liquidity, fractional discount or premium, share pricing, exit friction, buyer pool depth, and holding-period assumptions. |

### Cluster F: Data Providers, Public Sources, and Licensing

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 28 | `analysis-28--national-property-data-vendors.md` | Compare national property data vendors and aggregators such as ATTOM, CoreLogic, ICE/Black Knight, LightBox, Regrid, Estated, Precisely, and similar sources. |
| 29 | `analysis-29--government-open-data-and-records-portals.md` | Research city, county, state, and federal open-data portals, permit systems, GIS systems, and public-record access patterns. |
| 30 | `analysis-30--geospatial-environmental-and-census-data.md` | Research geospatial, environmental, hazard, demographic, mobility, and civic datasets from sources such as Census, USGS, NOAA, FEMA, EPA, state agencies, and local GIS. |
| 31 | `analysis-31--data-licensing-refresh-and-compliance.md` | Research licensing, caching, redistribution, attribution, update cadence, derived-data rights, and audit requirements. |

### Cluster G: Modeling Architecture

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 32 | `analysis-32--feature-store-and-property-entity-model.md` | Design the property, parcel, building, owner/share, permit, geospatial, and estimate feature model needed for the estimate. |
| 33 | `analysis-33--valuation-modeling-comps-hedonic-and-ml.md` | Research valuation approaches including comps, hedonic regression, repeat-sales, gradient boosting, ensembles, appraisal adjustments, and luxury-market sparse-data handling. |
| 34 | `analysis-34--intangibles-and-experience-value-modeling.md` | Research how to model qualitative and experience-driven value such as views, design, privacy, access, aesthetics, and prestige without hiding uncertainty. |
| 35 | `analysis-35--permit-risk-and-redevelopment-optionality-model.md` | Research modeling approaches for permitting friction, remodel feasibility, entitlement optionality, delays, and regulatory risk. |
| 36 | `analysis-36--operating-cost-and-reserve-forecast-model.md` | Research long-term cost forecasting, capex reserves, maintenance events, inflation, climate/insurance shocks, and owner share allocation. |
| 37 | `analysis-37--uncertainty-explainability-and-confidence.md` | Research confidence intervals, explanation UX, data quality scoring, source provenance, and human-review triggers. |
| 38 | `analysis-38--human-in-the-loop-appraisal-and-ops-workflow.md` | Research where expert appraisal, local broker knowledge, property management, and manual review should enter the estimate pipeline. |

### Cluster H: Product Experience

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 39 | `analysis-39--estimate-scorecard-and-narrative-ux.md` | Design the buyer-facing explanation, scorecard, narrative, and confidence surfaces for the next-gen estimate. |
| 40 | `analysis-40--map-layers-3d-and-scenario-exploration.md` | Research map layers, 3D visualization, scenario toggles, view corridors, renovation scenarios, and Unreal/Cesium-style long-term visualization possibilities if locally relevant. |
| 41 | `analysis-41--manager-admin-and-data-quality-workflows.md` | Research internal workflows for data ingestion, review, overrides, quality assurance, support, and owner communications. |

### Cluster I: Case Studies

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 42 | `analysis-42--manhattan-beach-white-water-view-case-study.md` | Apply the full framework to a Manhattan Beach white-water ocean view scenario using official local sources where possible. |
| 43 | `analysis-43--mountain-resort-case-study.md` | Apply the framework to an Aspen/Vail/Park City style mountain resort market with snow, access, HOA, STR, and wildfire considerations. |
| 44 | `analysis-44--lakefront-case-study.md` | Apply the framework to a lakefront second-home market with dock, water-level, flood, access, and seasonal-use factors. |
| 45 | `analysis-45--urban-luxury-condo-case-study.md` | Apply the framework to an urban luxury condo or pied-a-terre where HOA, building services, views, noise, and rules dominate. |
| 46 | `analysis-46--non-coastal-emerging-market-case-study.md` | Apply the framework to a non-coastal emerging second-home market to test whether the model overfits coastal luxury examples. |

### Cluster J: Capstones

| Track | Suggested file | Assignment |
|-------|----------------|------------|
| 47 | `analysis-47--data-source-comparison-matrix.md` | Compare all identified data sources by authority, coverage, cost, granularity, freshness, licensing, integration difficulty, and estimate value. |
| 48 | `analysis-48--target-estimate-architecture.md` | Propose the target data/model/product architecture, including v1, later, and someday layers. |
| 49 | `analysis-49--unknown-unknowns-and-dealbreakers.md` | Adversarially search for fatal flaws, hidden regulatory traps, data licensing blockers, modeling invalidity, market mismatch, and operational burdens. |
| 50 | `analysis-50--prior-art-and-local-assumption-reconciliation.md` | Reconcile findings with local FracRealHomes docs, prior project assumptions, Zillow/AVM prior art, luxury fractional models, and any Unreal Engine visualization ambitions. |
| 51 | `analysis-51--mvp-roadmap-and-validation-spikes.md` | Convert the corpus into a sequenced research-to-product roadmap, including cheapest validation spikes and first production data integrations. |

This seed map intentionally looks large. A future Codex run can trim it, but should not silently collapse it into a short memo when the user has asked for exhaustive deep research.

### Expansion Tracks Proven Useful In The FracRealHomes Validation Run

The successful FracRealHomes run expanded beyond the seed map to 73 tracks. Future runs on similarly broad product/data/modeling concepts should consider adding explicit tracks for these topics instead of burying them inside generic hazard or UX tracks:

| Topic | Why it matters |
|-------|----------------|
| Zillow/Zestimate reverse engineering | Treats incumbent AVMs as serious baselines and prevents "Zillow plus a few extra fields" thinking |
| Redfin/Realtor/AVM baseline comparison | Separates table-stakes consumer AVM signals from FracRealHomes-specific extensions |
| Zillow Prize and AVM literature | Grounds modeling assumptions in ensemble, sparse-data, and error-band lessons |
| Permit platform systems | Identifies Accela, EnerGov, OpenGov, Tyler, custom portals, records friction, and API/scraping limits |
| GIS portal/source inventory | Turns "use public maps" into a catalog of ArcGIS, Socrata, CKAN, FeatureServer, WMS/WFS, OGC API, and downloads |
| Layer UX and source-visible weighting | Ensures wildfire/flood/noise/power-line/etc. layers can be toggled, sourced, and converted into auditable factors |
| Data licensing and derived rights | Prevents unlawful use of MLS photos, basemaps, OSM, vendor data, or government disclaimers |
| Source bibliography and citation index | Gives the synthesis author and future builders a source map instead of scattered URLs |
| Supplemental wildfire utility/insurance track | Separates CAL FIRE FHSZ, CPUC HFTD, PSPS, utility WMPs, FAIR/DIC routing, and event causality |
| Supplemental high-voltage/EMF sentiment track | Separates physical infrastructure, visual/easement effects, EMF science, public sentiment, wildfire linkage, and insurance |
| Supplemental Cascadia/media-shock track | Models the difference between official hazard facts, public salience, luxury demand elasticity, and weak/mixed price evidence |
| Supplemental shock-event register track | Captures news, science, map, insurance, lawsuit, and pop-culture shocks before comps catch up |
| Supplemental ADU buildability and ancillary data-product track | Identifies partner/licensing opportunities from the same parcel, zoning, permit, and graph data needed for the core estimate |
| Supplemental broadband/connectivity track | Separates provider coverage, exact-address orderability, installed service, measured quality, mobile coverage, and remote-work readiness |
| Supplemental utility services and EV-readiness track | Separates water, sewer, septic, electric, gas, propane, EV, fire-flow, and utility adequacy from generic service-area claims |
| Supplemental satellite/fixed-wireless/failover track | Covers Starlink, WISPs, cellular failover, multi-WAN, telemetry, backup power, and managed connectivity resilience |
| Supplemental solar/storage/generator resilience track | Treats solar, batteries, generators, critical loads, outage scenarios, PSPS, and EV load management as owner-use and reserve/capex features |
| Supplemental essential-services/last-mile continuity track | Models stocking, delivery, package access, roads, vendors, emergency response, manager capability, and the split between positive remoteness and operational friction |

When the user provides new spot-check notes after reading the corpus, append supplemental tracks instead of rewriting earlier tracks. Keep the numbering continuous. If synthesis has not started, keep the Phase C gate intact. If synthesis already exists, use Phase 10A to create a new packet and refresh the synthesis.

## Final Response Pattern

After completing a research workflow stage, keep the final response concise:

- State what was created or updated.
- Link the main files.
- State whether tests were run or skipped.
- State commit hash if committed.
- State the next gate or requested user decision.

Do not paste long research content into the final response when the files already contain it.
