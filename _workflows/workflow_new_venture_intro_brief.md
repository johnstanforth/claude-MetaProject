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

## The framing that widens the questions — KSVGPS models the *pre-incorporation* idea-stage

KSVGPS is **not primarily a PE/VC CRM.** ~20–40% of Kingmaker Strategic is the straightforward PE/VC side (a CRM + a "radar" that surfaces breakout projects — an OpenClaw at 2M downloads in week one — for small near-angel deals; no real complexity). The other **~60–80% is a venture studio**, and *that* is what KSVGPS exists to model: the place ideas live **before incorporation** — the equivalent of "inside Peter Steinberger's head and his early notebooks during the year he built OpenClaw before the first release" — extended across **a dozen-plus idea-stage ventures and dozens of people** John has worked with over 25+ years, each at its own maturity (some still nameless; some graduated to domains + branding; most still mostly in-head or shared with one or two would-be partners).

Implications that **change the questions** to ask about any venture:

- **Decade-scale idea-arcs, not incorporation→dissolution.** Model the arc: *vague idea (years) → named → prototyped → small team → seed → PMF*, and sometimes *→ wound-down/paused → rebooted years later* as a successor. The canonical case is **MobThought (2004–2008) → CrowdMadness** — already the lead example in the KSVGPS entity-model research's `successor-of` / `historically-owned` modeling. So ask: *when did this idea first occur to you? how long has it lived in your head? what's its predecessor/lineage? what paused or unblocked it?*
- **People & relationships are first-class.** Ventures form around specific people (e.g. LegendaryMoney = John + David Lang + a few). Early MobThought ran with advisor-collaborators like Bill Brand (President, HSN.com), Stephen McHenry (Chancellor of Worldwide SRE, Google), and Jonathan Forster (first hire / VP Marketing, Spotify). So ask: *who would you build this with? who are the advisors / would-be partners?*
- **External-environment dependencies an autonomous agent should track.** CrowdMadness is feasible *now* and wasn't in 2005 because LLM agents can do nightly what used to cost tens of millions in legal — track every state/federal regulatory change and translate it into required app changes (2018 PASPA repeal → FanDuel/DraftKings → Polymarket/Kalshi + CFTC, none of which existed during MobThought). So ask: *what external environment — regulatory, platform, data-licensing — gates this venture, and what would an agent need to watch?* These usually become `[Backlog:RESEARCH]` items.
- **Dated milestones.** Build Lines & Triangulation Targets carry frequently-updated absolute dates ("in 36 months" → a concrete 2029 date) so the portfolio is sliceable by date for future-scenario reasoning (see [`workflow_cross_venture_future_scenario.md`](workflow_cross_venture_future_scenario.md) and the model doc's *Dated Triangulation Targets* section). So ask: *roughly when do you imagine v1 / the seed / the far Target?*

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
