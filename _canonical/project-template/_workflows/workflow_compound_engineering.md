# Workflow: Compound Engineering Review

> Systematic process for capturing lessons learned, improving development infrastructure, and ensuring each sprint makes subsequent sprints easier. Based on Compound Engineering practices originated by Dan Shipper and Kieran Klaassen at Every, Inc.

## Quick Reference

| Item | Value |
|------|-------|
| Applies to | Main Claude agent + human, at sprint boundaries |
| When to run | See [Integration Points](#integration-points) — multiple touchpoints across the sprint lifecycle |
| Inputs | Sprint artifacts, code changes, session transcripts, current CLAUDE.md and workflow docs |
| Outputs | Updated CLAUDE.md, updated workflow/techstack docs, new backlog items, lessons documented |
| Source | [Compound Engineering: The Definitive Guide](https://every.to/guides/compound-engineering) by Every, Inc. |

---

## 1. Background

Compound Engineering is a methodology for AI-assisted software development created by Dan Shipper (CEO) and Kieran Klaassen (CTO) at Every, Inc. The core principle: **each unit of engineering work should make subsequent units easier, not harder.** The methodology has a four-phase loop — Plan, Work, Review, Compound — where the "Compound" phase is the distinctive contribution that most development teams lack.

Our workflow system independently evolved many of the same patterns (spec-driven planning, autonomous execution, multi-agent review). What we've been missing is a systematic Compound phase — turning sprint experience into durable infrastructure improvements.

### The Key Insight

Most development teams do retrospectives. Few teams systematically convert retrospective findings into concrete artifacts that future sessions consume automatically. The difference between "we should document that pattern" and actually adding it to CLAUDE.md (where every future agent reads it on startup) is the difference between learning and compounding.

### The 80/20 Inversion

Compound Engineering allocates roughly 80% of effort to planning and review, 20% to writing code. Our existing sprint workflow already reflects this: the sp/xp planning process and post-sprint code review consume more time than autonomous execution. This workflow formalizes the "Compound" portion of that investment.

---

## 2. The Three Stages

Compound Engineering applies at three points in the sprint lifecycle, not just at closeout. Each stage has a different focus and produces different artifacts.

### Stage A: Sprint Planning — Compound Investment Check

**When:** During sprint planning (Step 2 of `workflow_sprint_planning_solo.md` or the scope discussion in `workflow_sprint_planning_collab.md`).

**Purpose:** Ensure the sprint allocates effort to infrastructure improvements alongside features.

**Process:**

1. **Review the NEXT horizon and UNSORTED_QUEUE** for infrastructure items — test improvements, documentation gaps, tooling enhancements, developer experience fixes.

2. **Ask the 50/50 question:** "Does this sprint include at least one task that improves the development infrastructure itself — not just the product?" This doesn't mean literally 50% of tasks must be infrastructure. It means: don't plan a sprint that is 100% feature work with zero investment in the system that builds features.

3. **Check for stale patterns.** Read the most recent sprint's post-sprint notes and any Compound Engineering findings from the last closeout. Are there items flagged as "should be improved next sprint" that haven't been picked up?

4. **If no infrastructure work is planned:** Note this explicitly in the sp file as a conscious decision, not an oversight. Some sprints are legitimately 100% feature work — but it should be deliberate.

**Artifacts produced:** A note in the sprint spec (sp file) under a "Compound Engineering" heading, documenting either: (a) which infrastructure improvements are included and why, or (b) why this sprint has none.

### Stage B: Post-Sprint Review — Lessons Capture

**When:** After code review fixes are applied, before sprint closeout. This is the primary Compound Engineering step.

**Purpose:** Systematically extract lessons from the sprint and convert them into durable artifacts.

**Process:**

1. **Review what happened.** Read the sprint's:
   - Execution plan (xp file) — what was planned
   - Post-sprint notes in the sp file — what actually happened
   - Code review summary (if one exists) — what was found and fixed
   - Git log for the sprint — the actual sequence of work

2. **Answer the five Compound questions:**

   | # | Question | What to look for |
   |---|----------|-----------------|
   | C1 | **What patterns emerged?** | Repeated code structures, common test setups, recurring architectural decisions. If you wrote similar code three times, there's a pattern to extract. |
   | C2 | **What was harder than expected?** | Tasks that took longer, required debugging, or needed multiple attempts. These are the richest source of lessons — the gap between the plan and reality is where learning lives. |
   | C3 | **What would we tell the next agent?** | If a fresh Claude instance were starting the next sprint right now, what would you want it to know that isn't already in CLAUDE.md? Gotchas, workarounds, "don't do X because Y." |
   | C4 | **What tooling or process friction did we hit?** | Test fixtures that were awkward to use, workflow steps that felt unnecessary, validation commands that took too long, missing dev scripts. |
   | C5 | **What infrastructure did we improve?** | Tests added, documentation updated, tooling enhanced, developer experience improved. Celebrate these — they're the compound interest paying forward. |

3. **For each finding, decide its destination:**

   | Finding type | Destination | Example |
   |-------------|-------------|---------|
   | Pattern or convention future agents should follow | **CLAUDE.md** — add to the relevant section | "Always use SAVEPOINT-based test isolation for DB tests" |
   | Workflow improvement | **Workflow document** — update the specific workflow | "The code review template should require mypy checks" |
   | Tech stack lesson | **Techstack document** — update `_workflows/techstacks/` | "pydantic-settings requires env vars set BEFORE app import" |
   | Bug or issue to fix | **Backlog** — add to UNSORTED_QUEUE or NEXT horizon | "The conftest.py fixture leaks connections under X condition" |
   | Reusable code pattern | **Code** — extract to a utility, add a test | "The slug-generation logic is duplicated in 3 places" |
   | Process that worked well | **This document's Appendix** — record what to keep doing | "Collab-group code review caught 3 issues solo review missed" |

4. **Write the findings.** Create a "Compound Engineering Findings" section in the sprint's sp file (post-sprint notes area) with the format:

   ```markdown
   ### Compound Engineering Findings

   **Patterns emerged:**
   - {finding + destination}

   **Harder than expected:**
   - {finding + destination}

   **Tell the next agent:**
   - {finding + destination}

   **Process friction:**
   - {finding + destination}

   **Infrastructure improved:**
   - {item}
   ```

5. **Apply the findings immediately.** Do not defer "update CLAUDE.md" to a later sprint. The whole point of compounding is that the improvement lands NOW so the NEXT sprint benefits. During this same closeout session:
   - Update CLAUDE.md if findings warrant it
   - Update workflow documents if process improvements were identified
   - Update techstack documents if stack lessons were learned
   - Add backlog items for anything that can't be applied immediately

### Stage C: Phase Transition — Compound Retrospective

**When:** During phase transition (when `workflow_new_phase.md` is run to start a new phase).

**Purpose:** Zoom out from individual sprint lessons to phase-level patterns.

**Process:**

1. **Read all Compound Engineering Findings sections** from the phase's sprint sp files.

2. **Identify cross-sprint patterns:**
   - Did the same type of friction appear in multiple sprints? (Systemic issue, not one-off.)
   - Did infrastructure investments pay off? (Reduced time, fewer bugs, better DX in later sprints.)
   - What was the phase's overall compound rate — did sprints get easier as the phase progressed, or harder?

3. **Produce a "Phase Compound Summary"** in the phase README:
   ```markdown
   ### Compound Engineering Summary

   **Infrastructure investments:** {what was built for the system, not just the product}
   **Lessons propagated to CLAUDE.md:** {count and brief descriptions}
   **Workflow improvements made:** {list}
   **Recurring friction not yet resolved:** {items that appeared in 2+ sprints}
   **Compound rate assessment:** {easier / stable / harder — with evidence}
   ```

4. **Review the Adoption Ladder.** Compound Engineering defines a maturity model:
   - Stage 0: Manual development (no AI)
   - Stage 1: Chat-based assistance (copy-paste)
   - Stage 2: Agentic tools with line-by-line review
   - Stage 3: Plan-first, PR-only review (autonomous implementation)
   - Stage 4: Idea to PR on single machine
   - Stage 5: Parallel cloud execution (multiple features simultaneously)

   At each phase transition, assess where we are on this ladder and whether the phase's work moved us forward.

---

## 3. Integration Points

This workflow does NOT run as a standalone session. Its stages integrate into existing workflows at specific points.

| Stage | Integrates Into | Where Exactly |
|-------|----------------|---------------|
| **A: Planning Check** | `workflow_sprint_planning_solo.md` or `workflow_sprint_planning_collab.md` | During scope discussion, before writing the sp/xp files |
| **B: Lessons Capture** | `workflow_sprint_closeout.md` Step 8 | Replaces the current lightweight checklist with the full Stage B process |
| **C: Phase Retrospective** | `workflow_new_phase.md` | After reviewing the previous phase's outcomes, before planning Phase N+1 |

The main workflow documents should reference this document at the appropriate step rather than inlining the full process.

---

## 4. The 50/50 Principle

Compound Engineering recommends allocating roughly 50% of effort to features and 50% to system improvements. This is aspirational, not prescriptive — the actual ratio depends on project maturity.

**How to apply it practically:**

- **Early phases (Phase 0-2):** Infrastructure investment is naturally high — you're building the foundation. The 50/50 rule is often exceeded (more infrastructure than features). This is correct.
- **Middle phases (Phase 3-5):** Feature work dominates, but each sprint should include at least 1-2 infrastructure tasks. Test coverage improvements, documentation updates, workflow refinements.
- **Late phases (Phase 6+):** If sprints are getting harder, not easier, the compound rate has stalled. Dedicate a hardening sprint (100% infrastructure) to restore it.

**Signals that compound rate is stalling:**
- Test suite is slower than 2 sprints ago
- CLAUDE.md hasn't been updated in 3+ sprints
- New agents spend significant time re-discovering patterns that should be documented
- The same type of bug keeps appearing across sprints
- Workflow friction that was noted in a previous sprint's findings still hasn't been addressed

---

## 5. "Plans Are the New Code"

One of Compound Engineering's key insights: in an AI-assisted workflow, the plan is the primary artifact. Plans are cheaper to fix than code bugs. A well-written execution plan (xp file) that specifies the wrong approach wastes one sprint. A poorly written plan that gets "fixed" during execution wastes the sprint AND leaves no documentation of why the approach was changed.

**Implications for our workflow:**
- The xp file is worth investing time in. It's not bureaucracy — it's the spec that drives autonomous execution.
- When execution deviates from the plan, document why in post-sprint notes. The deviation is a signal: either the plan was wrong (improve planning) or something unexpected happened (document the surprise for future agents).
- Post-sprint notes that say "completed as planned" are as valuable as notes about deviations — they confirm the planning process worked.

---

## 6. Version History

This document tracks the evolution of our Compound Engineering practices. When the upstream methodology is revised or when our own experience produces new insights, update this document and add an entry here.

| Date | Change | Source |
|------|--------|--------|
| 2026-05-04 | Initial creation. Consolidated from prior research (2026-03-14 `claude_code_workflows` analysis) and online research confirming CE v3.3.0 (2026-04). Three-stage integration model (Planning Check, Lessons Capture, Phase Retrospective). | Prior research + online confirmation |

### Upstream Sources to Monitor

- [Every.to Compound Engineering Guide](https://every.to/guides/compound-engineering) — canonical source
- [GitHub: EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) — reference implementation
- [Will Larson's analysis](https://lethain.com/everyinc-compound-engineering/) — independent evaluation (2026-01-19)

---

## Appendix: What Works Well (Preserve These)

Record practices from our own experience that align with or extend Compound Engineering principles. These are "things to keep doing" — the positive counterpart to lessons learned.

*(Add entries as they emerge from Stage B reviews.)*
