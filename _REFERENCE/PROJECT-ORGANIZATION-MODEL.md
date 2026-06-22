# Project Organization Model — Ventures, Build Lines, Build Envelopes, Triangulation

> **Cross-venture organizing model** — applies to *every* portfolio company, which is why it lives in `_REFERENCE/`. Co-developed by John + Claude, 2026-06-17→20. It replaces flat "v1 vs v2" thinking with separated, orthogonal axes.

## The problem it solves

"v1 vs v2" secretly collapses several **independent axes** into one number:

1. **Which *product*?** A daily personal tool, the near-term shippable product, and a 3–5-yr enterprise vision are **different products** — different audiences, lifecycles, sometimes different *companies* — not stages of one thing.
2. **How mature within it?** Each product has its own version progression, re-triaged every backlog pass.
3. **How far toward the destination?** Each has a far "where we're ultimately going" that decides which *fork* to take today (the **Triangulation Target**).
4. **At what engineering scale are we building *right now*?** A 20-person-startup Python/Flask build vs. a 10,000-person regulated-enterprise build (the **Build Envelope**).

Collapsing these is why a far-future concern *feels like it "blows up" the near-term build*, and it's the root of the chronic **"this'll never get built"** dread and the **"I can see 37 chess-moves ahead but can't act on move 1"** paralysis. **The unlock:** you don't need to hold all 37 moves — only the few *irreversible forks* (the `[DEALBREAKER-HOOK]`s). Separate the axes, capture the irreversible forks, and everything else is free to fall into place later.

## The model

```
Company / Venture
 ├─ corporate structure · Brands
 └─ Product Lines        (families of related products — the standard business meaning)
     └─ Products         (individual offerings)
         ├─ Product Version-Releases  (v1.0 … vN.0 — a "moving symlink" across Build Lines)
         └─ Build Lines  (the engineering codebases that deliver the Product)
             ├─ Build Envelope        ← the engineering scale/scope/stack being built FOR
             ├─ Triangulation Target  ← the far destination guiding forks
             └─ Stages   (Build-Line-local milestones; public Stages → the Product's Version-Releases)
                 └─ Phases → Sprints  (the existing execution machinery — unchanged)
Features = graph nodes throughout (Requester-Source · Build Line · target Version · dealbreaker-flag · typed relations)
```

- **Company / Venture** — the legal/conceptual entity ("a conceptual grouping of related ideas that evolves toward a holistic whole").
- **Product Line** — a **family** of related products (standard meaning), e.g. FracRealHomes' consumer-diligence line vs. its B2B ADU-data line.
- **Product** — an individual offering within a line, with public **Product Version-Releases** (`v1.0…vN.0`) that behave like a **moving symlink**, pointing to whichever **Build Line** currently delivers each one.
- **Build Lines** — the **engineering codebases** (repos/stacks) delivering a Product, named descriptively per-venture; **some are private** (a personal playground that never ships). They relate by **clone-lineage + merge** (shared stack) or **succession, no-merge** (a different-stack successor, e.g. `proto-divia_ai-enterprise` Python → Rust `divia_ai-enterprise`).
- **Stages** — a Build-Line-local milestone (its internal `v1/v2/v3`); on a *public* Build Line, certain Stages get **promoted to the Product's public Version-Releases** (private Build Lines have Stages but no Version-Releases). Each Stage is delivered via the existing **Phases → Sprints**, unchanged.
- **Features** — modeled as **graph nodes, not free-text kanban cards** (the board is the human *view*; the graph is the model). Each carries **Requester-Source** (John / research / business-dev / dogfooding / partner-deal), its Build Line + target Version, a `[DEALBREAKER-HOOK]` flag, and typed relations.

## Product Version-Releases — immutable past, movable future

A **Product Version-Release** is a public release milestone (`v1.0 … vN.0`) of a Product. A **moving "today" marker** splits the sequence into two halves that behave very differently — the whole point of the name (not "Version *history*," which implies git-style immutability and a past-only tense):

- **Past (before today) — immutable, git-matched.** Released versions are a historical record pinned to what actually shipped (the git history). Web-app-wise they stay editable, but only behind a root-level admin-override ACL — never moved casually.
- **Future (after today) — a flexible "marketing sketch."** Unreleased version numbers are **movable like kanban cards**: re-bucketable, re-numberable, pushable further out by anyone (e.g. a marketing teammate). A far target sketched *today* — "v5.0 = the National-AVM Build Line" — can slide to v6.0, then v7.0, as nearer ideas claim the lower numbers; marketing can align branding around a conceptual "v7.0" a year before anything exists.

This asymmetry is deliberate: re-bucketing a *future* version takes seconds; rewriting the *released past* takes an admin override. It's what lets **every idea get thrown at the build-lines matrix** at fine granularity — "great idea, but that's v7.0 scope, not v4.0 and not the next few" becomes a first-class triage move — replacing the coarse GTD "Someday/Maybe" list and the vague "Someday" backlog with a placeable, re-bucketable future.

## Build Envelope (formal: **Architectural Build Envelope**) — an independent axis

A **Build Envelope** is a **named, per-venture, reusable** definition of *the engineering scale, scope, team, timeframe, and stack a thing is built FOR* — e.g. `Build Envelope "Seed": 6 mo · ~20-person startup · 5–7-person dev team · Python/Flask`. (Named after the real-estate sense: the buildable zone within a lot once terrain and setbacks are accounted for — *the ground you're actually allowed to build on right now*.)

- **Independent of Build Lines** — Build Lines won't share Envelopes 1:1 across ventures, so this is its own variable, not a Build-Line attribute folded in.
- **Reusable, copy-on-write across projects** — like pulling `_workflows` into a new repo and adapting; this formalizes the organically-grown "Python/Flask-at-the-seed-tier across 20+ projects" pattern, and gives the **continuous-improvement loop a home** (e.g. "should the Flask+FastAPI tier move to async Quart?" → research once, propagate the answer to every project on that Envelope).
- **The explicit context handed to Codex** so it designs *for that Envelope* instead of reverting to IANA-grade enterprise specs just to mint a cross-project `user_id`. (This is the same over-calibration the Build Lines first exposed.)
- **Pairs as two axes:** **Triangulation Target (where we're going) × Build Envelope (the ground we may build on now).** Each Build Line centers on one Build Envelope.

## Dated Triangulation Targets & future-scenario projection

Each **Triangulation Target** (and major Build-Line milestone) carries a **frequently-updated absolute-date estimate** — "in 36 months" is stored as a concrete date (e.g. `2029-Q2`), re-checked every planning pass as milestones move and `v1→v2→v3` re-sequence. Two payoffs: (1) the date makes "triangulate to where you want to be" **measurable** — the backlog horizons (NEXT/LATER/SOMEDAY → Stages→Phases→Sprints) are the path that closes the gap between today and the dated Target; (2) the portfolio becomes **sliceable by date** — "what state is every venture in as of {future date}?" is a cross-venture query (a manual read of the briefs today; a SQL-slice across the graph-DB later) that powers **future-scenario reasoning** (e.g. "what happens to a paper grocery receipt in Jan 2030?" — see [`../_workflows/workflow_cross_venture_future_scenario.md`](../_workflows/workflow_cross_venture_future_scenario.md)). Conclusions from such reasoning are written back both forward (the future version's features) and backward (the backlog steps that build toward them).

## Layer A — the Strategic Landscape (Ideas & Topics) above the ventures

Everything above is **Layer B** — Ventures/brands and the engineering structure that delivers them. Above it sits **Layer A: the durable, brand-free Idea/Topic layer** (KSVGPS Module 1, the "Strategic Landscape"), where ideas live independent of any brand, carry their own research, and connect to ventures via a **time-bounded "channel" symlink** (the prediction-market idea channelled MobThought → CrowdMadness; detaches and returns to Layer A when a venture pauses/pivots, staying reusable). Crucially, **a Build Line *realizes* an Idea inside a Venture** — so one Idea can be delivered by several Build Lines across scale (the AVM Idea → both the EstimatePacket and National-AVM Build Lines): the chain is `Topic → Idea → (channel) → Venture → Build Line → Version-Release`. The full Layer-A model — node-types, edges, the channel symlink, ACL scoping, and how the dimensional axes re-home onto the two layers — is the canonical [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md).

## Two knowledgebases — business (KSVGPS) vs. software-dev (AIXO.Dev)

The portfolio is modeled across **two** graph-DB knowledgebases — both on the Divia.AI Enterprise graph-DB technology — split by domain so each stays free of the other's noise:

- **KSVGPS — the business side:** Companies · corporate structure + subsidiary LLCs · Brands · Product Lines · Products · GTM strategies · domains · a Product's public Version-Releases. *No dev/technical/software notes.*
- **AIXO.Dev Platform — the software-dev side** (prototyping now in `aixodev-projects` + `aixodev-workgroups`): every project · repo · repo-remote/upstream · **Build Line · Build Envelope · Stage → Phase → Sprint** · techstack · lineage/convergence relations · dev-team discussions — modeled in extreme detail.

**Build Lines and Build Envelopes are engineering-team concepts — they live in the AIXO.Dev model, not KSVGPS.** The two knowledgebases **share an overlap/union anchored at `Company → Product`** (the business anchor the software-dev side hangs repos/Build-Lines off). So a self-contained brief that bootstraps both carries a clear **business facet** (→ KSVGPS) and a **software-dev facet** (→ AIXO.Dev).

## `[DEALBREAKER-HOOK]` — the triangulation primitive

A **`[DEALBREAKER-HOOK]`** is a concern that *belongs* to the far Triangulation Target (normally "defer"), **except that getting it wrong now forces a later rewrite** — so it must be **hooked into the near-term Build Line today** (cheap now, catastrophic to retrofit). It is John's **"triangulate to where you want to be"** made operational: at each fork, take the path that keeps the destination reachable, even when the "easy" fork looks simpler. (The myopic easy-fork is how teams throw away v2 for a v3 rewrite, forever; the triangulated path is how a "needs 2–3 servers in 1997" system compounds into a "$1.2B, 7 datacenters" platform over ten years *without* a throwaway rewrite.)

It is **one fractal principle at three scales** — identical to the entity-model synthesis's *reversible-vs-irreversible* thesis and the `ARCHITECTURE_CONVERGENCE` chain. **Most far-future concerns genuinely defer; a small, precious set are `[DEALBREAKER-HOOK]`s. Finding *that set* — not building the future — is the whole job at v1.**

## Worked example — FracRealHomes

| Build Line | Build Envelope | Role | In the Product's Version-Releases? |
|---|---|---|---|
| **DailySpikeDriver** | "Playground" (John only, Python/Flask, idea-of-the-day) | dogfood + experiment; **merges up** into EstimatePacket Line | **No** — private, never released |
| **EstimatePacket Line** *(middle)* | "Seed" (6–18 mo · ~50–100-person startup · ~20–40-person dev · Python/Flask) | the near-term product (the SORTING-PASS diligence scope) | **Yes** — delivers public **v1.0 → v4.0** |
| **National-AVM Line** | "Enterprise" (3–5 yr · regulated multi-market · different stack) | the far-future public AVM (Codex's home; a categorization bucket for now) | **Yes (later)** — delivers public **v5.0+** (succession, no-merge) |

The FracRealHomes **Venture** may carry multiple **Product Lines** (consumer-diligence vs. a B2B ADU-data line); the table above is the main diligence Product. DailySpikeDriver feeds the public Build Line via merge but never appears in the public Version-Releases — so "I want a Zillow-email triage parser *for my own use*" is a first-class DailySpikeDriver feature that creates **zero** obligation on the venture's PRD.

## Two benefits beyond clarity

1. **Scoped context-projection (with the graph-DB).** Once Build Lines + Build Envelopes + goals are modeled, an agent discussion can be handed a **scoped projection** containing *only* relevant context — a National-AVM-Line / Enterprise-Envelope discussion is auto-redacted of DailySpikeDriver items and of decisions already rejected-for-earlier-Lines. **Build Lines + Envelopes become natural context-scoping boundaries** — serving the orchestrator-context-preservation directive.
2. **The Sorting-Hat matrix.** Every incoming idea routes into the **(Product × Build Line × Version, at a Build Envelope, toward a Triangulation Target)** matrix — turning "hundreds of ideas a day = noise I have to block out" into "every idea has a home": a cognitive offload from *hold-or-discard* to *capture-and-place*.

## Connection to existing structure

This generalizes the **prototype → product convergence** chain (`ARCHITECTURE_CONVERGENCE.md`) — a different-stack succession between Build Lines is the proto-divia→Rust-divia pattern; a shared-stack clone-lineage is the kingstrat-cloned-from-proto-divia pattern. And it is the same reversible-vs-irreversible principle as the entity-model synthesis, at the portfolio scale.

## Status

Model **v2** (2026-06-20). Applies cross-venture. The graph-DB realization (scoped projections, feature-as-node modeling, Build-Envelope reuse) and the per-venture briefs are downstream work; the markdown **briefs in `_REFERENCE/ULTIMATE_VISION/` are the manual proto-version of that graph-DB** (see `PLAN-new-ventures-from-portfolio-knowledgebase.md`). This doc is the conceptual canon other docs reference.
