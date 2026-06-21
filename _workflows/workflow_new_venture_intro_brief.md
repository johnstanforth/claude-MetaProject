# Workflow — New-Venture Intro Brief (the interview-as-you-draft loop)

> Rough-draft v1 (2026-06-21). Formalizes the process used to stand up the PatternicityNews + CrowdMadness briefs. Pairs with [`../_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](../_REFERENCE/PROJECT-ORGANIZATION-MODEL.md) (the structural model) and [`workflow_cross_venture_future_scenario.md`](workflow_cross_venture_future_scenario.md) (its downstream sibling).

## Purpose

Stand up a new or under-documented venture as a **two-file intro brief** (business-side + engineering-side, per the two-knowledgebase split) that is simultaneously (a) a *draft of everything we already know or can infer*, and (b) a *structured interview* that surfaces everything we don't. Claude does the brilliant-but-laborious part — reasoning across the entire portfolio to think of every facet that needs an answer, and inductively assembling the answers as they arrive; John does the easy-for-him part — answering questions that, once asked, he can answer off the top of 25 years of head-knowledge (or flag as unknown / research-needed). The result is a thorough, start-to-finish brief that would take John days-to-weeks to write from scratch, produced as a by-product of an easy Q&A.

## Why this format wins (John's framing)

- **Asking is cheaper than writing.** A good question lets John answer in one breath what he'd never sit down to author; and *different* questions about the same venture make him think about it in different ways, surfacing insights several reasoning-layers deeper than a blank page ever would.
- **Per-section questions beat an appendix.** Questions live **inline, under the section they belong to**, so John reads "here's what we know / here's the gap" with full local context — not a wall of questions divorced from the material.
- **More questions are better.** Err toward over-asking. Each question is a cheap probe; the cost of a missing question is a silent gap in the model.

## The rules (the no-invention contract)

1. **No invention.** Every stated fact must trace to a source (a `_REFERENCE/` doc, a managed repo, a prior brief, or an explicit John answer). Cite it.
2. **`TBD` / `Unknown (not in source files)` for every gap** — never paper over a gap with a plausible guess. A flagged gap becomes a question.
3. **Inferences are labeled as inferences** (e.g. "*Inference:* Patternicity Bet may tie to CrowdMadness — sources don't say"). Never launder an inference into a fact.
4. **Delegate the source-sweep.** Reading every cross-venture doc is context-heavy grunt work → dispatch Opus research subagents to return citation-rich dossiers, preserving the orchestrator's context for the synthesis + question-writing (which must stay the orchestrator's). See [`../_backlog_TODOs/LATER-005-context-preserving-search-workflow.md`](../_backlog_TODOs/LATER-005-context-preserving-search-workflow.md).
5. **`[Backlog:RESEARCH]` shorthand.** When John's answer is "I think X, but we need to research it" (a known dependency — e.g. Wikipedia licensing), append it to [`../_backlog_TODOs/RESEARCH-BACKLOG.md`](../_backlog_TODOs/RESEARCH-BACKLOG.md).

## The steps

1. **Scope the facets.** Enumerate every facet the two briefs need, from the model — *business:* company / corporate structure + subsidiaries / brands / Product Lines / Products / GTM + monetization / domains / Product Version-Releases; *engineering:* repos / Build Lines / Build Envelopes / Triangulation Target (dated) / Stages→Phases→Sprints / lineage + convergence / `[DEALBREAKER-HOOK]`s / license — plus the **venture-studio facets** (next section).
2. **Sweep the sources** (delegated). One citation-rich dossier per venture: every fact/mention/inference with a `path` citation + an explicit "NOT FOUND IN SOURCES" gap list.
3. **Draft the two files in intro-brief format.** Each `##` section = a short **"What we know / infer"** block (cited) followed by an **"❓ Additional Questions for John"** block. Distribute questions to the business vs. engineering file by facet; cross-venture questions go where the decision lives.
4. **Over-ask.** Include every question from prior rounds plus more; let the reframing (below) widen the net.
5. **John answers** — any depth, any order; skips stay `TBD`; `[Backlog:RESEARCH]` items route to the research backlog.
6. **Graduate the brief.** Fold answers in; the intro/partial brief becomes a filled brief; surviving gaps stay flagged. Re-run as the venture matures (the feedback loop).

## The framing that widens the questions — KSVGPS's three audiences, and the pre-incorporation layer

KSVGPS is **not primarily a PE/VC CRM.** It serves **three audiences through three modules/portals**, and the newly-central one — the **pre-incorporation idea-stage** — is what the OpenClaw analogy describes (where ideas live *inside the founder's head and early notebooks* before there's even a name, let alone a company):

- **Module 1 — GP Strategic Landscape & Ideation** *(audience: the ~3–5 Kingmaker Strategic **GPs**, incl. John)*. The pre-incorporation layer. An idea enters the moment John thinks of it — "a next-gen Zillow estimate that 3D-wireframes adjacent lots in Unreal Engine to find their max-build" lived *nameless for years* here before becoming **FracRealHomes** — and *immediately* benefits from the integrated graph-DB cross-venture view, **even before John has mentioned it to another GP.** This is the layer the John×Claude cross-venture reasoning operates in, soon augmented by **nightly autonomous-agent "wildly-imaginative dreaming" runs** (Claude scanning every idea overnight, pulling scoped-projections, ideating cross-venture features and "what Jan-2030 looks like" before anyone's thought of them — see [`workflow_cross_venture_future_scenario.md`](workflow_cross_venture_future_scenario.md) and [`../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md`](../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md)). It raises "brainstorming inside one founder's head" to what a well-organized boutique VC firm's research bench could do — for an audience of *one GP plus Claude*.
- **Module 2 — Venture Studio Operations Center** *(audience: an active venture's **Board/Directors + "C-level"**)*. (Renamed from "Studio Operations" — in greater-LA, "Studio" reads as Hollywood.) The operational-coordination layer once a venture has a small team: *not* an Asana-replacement for every employee, but where the investor/Director ↔ C-level strategy and initiatives are coordinated (in a 10–20-person startup, "C-level" is just the couple people running daily ops, matching their business-card titles). Replaces the old in-person-meetings + email-threads + Excel-P&L-vs-budget + PowerPoint world. **This module ≈ the venture's incorporation→dissolution window.**
- **Module 3 — LP Dashboard** *(audience: **investors/LPs**, several of whom are also expert-advisors)*. Real-time performance + transparency, replacing 90-day quarterly reports — because AI now *accelerates venture lifecycles* (2M downloads in week one, or a fast "the advisors said it's not viable, we paused it"), so a quarterly cadence is badly misaligned, and an LP-advisor who could jump in to course-correct needs far finer-grained visibility.

**The lifecycle flow across the modules** (the key dynamic): an idea originates in **Module 1**; when it becomes an operational venture, its Module-1 status flips to "operational" and the Board/C-level coordination runs in **Module 2** (≈ incorporation→dissolution) while LPs watch **Module 3**; when a venture **pauses/dissolves it returns to Module 1** (the Strategic Landscape). MobThought is the worked arc: operational ~2004–2008 (Module 2) → paused → it sat in Module 1 (a reboot was *discussed* in 2010–2011 but deferred because **AdEvolve** was going well and they didn't want to divert resources) → **rebooted as CrowdMadness in 2026**, which now gets its *own* Module-2 start/end. So **Module 1 is the persistent home across the whole decade-arc; Module 2 is the operational window.**

Implications that **change the questions** to ask about any venture (now across all three audiences):

- **Where in the lifecycle is it?** Module 1 (pre-incorporation idea), Module 2 (operational), or back-in-Module-1 (paused/dissolved, awaiting reboot)? What's its predecessor/reboot lineage? — model the **decade-arc**, not incorporation→dissolution. (MobThought→CrowdMadness is the canonical `successor-of` case; logged `[Backlog:RESEARCH] R-003`.) So ask: *when did the idea first occur to you? how long was it nameless? what paused or unblocked it?*
- **People & relationships are first-class**, at every layer: GPs (Module 1), the Board/Directors + C-level a venture would form (Module 2), and the LP-advisors (Module 3). MobThought ran with advisor-collaborators like Bill Brand (President, HSN.com), Stephen McHenry (Chancellor of Worldwide SRE, Google), Jonathan Forster (first hire / VP Marketing, Spotify). So ask: *who would you build this with — co-founders, Directors, LP-advisors?*
- **External-environment dependencies an autonomous agent should track.** CrowdMadness is feasible *now* because LLM agents can do nightly what cost tens of millions in legal — track every state/federal regulatory change and translate it into required app changes. So ask: *what external environment — regulatory, platform, data-licensing — gates this, and what would an agent watch?* (→ `[Backlog:RESEARCH]`.)
- **Dated milestones + the three views' cadence.** Build Lines & Triangulation Targets carry frequently-updated absolute dates (the model doc's *Dated Triangulation Targets* section); Module 3's whole point is those dates + metrics updating in real time, not quarterly. So ask: *roughly when v1 / seed / far Target — and what real-time metrics would an LP want?*
- **Operational-coordination needs (Module 2).** When this venture has a small team, what investor↔C-level coordination lives here? So ask: *who would run daily ops, who's on the Board, what decisions/initiatives need coordinating?*

## The intro-brief file skeleton

Both files — business `_REFERENCE/ULTIMATE_VISION/PRODUCTS/<Umbrella>/<slug>.md` and engineering `_REFERENCE/SOFTWARE_DEV/<slug>.md` — open with the standard paired-brief banner (marked **"INTRO BRIEF — partial; open questions inline"** until answers graduate it), then per section:

```
## <Facet>
**What we know / infer** — cited bullets; `TBD` for gaps; *Inference:* labels for inferences.

**❓ Additional Questions for John**
1. …
2. …
```

## Cross-references

- Structural model: [`../_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](../_REFERENCE/PROJECT-ORGANIZATION-MODEL.md) · plan: [`../PLAN-new-ventures-from-portfolio-knowledgebase.md`](../PLAN-new-ventures-from-portfolio-knowledgebase.md).
- Downstream sibling: [`workflow_cross_venture_future_scenario.md`](workflow_cross_venture_future_scenario.md).
- Research-topic destination: [`../_backlog_TODOs/RESEARCH-BACKLOG.md`](../_backlog_TODOs/RESEARCH-BACKLOG.md).
