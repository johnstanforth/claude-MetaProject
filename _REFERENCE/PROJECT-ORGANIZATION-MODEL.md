# Project Organization Model — Ventures, Build Lines, Product Versions, Triangulation

> **Cross-venture organizing model** — applies to *every* portfolio company (FracRealHomes, KingStrat AdVentureGPS, the Divia.AI products, …), which is why it lives in `_REFERENCE/`. Co-developed by John + Claude, 2026-06-17/18. It replaces flat "v1 vs v2" thinking with separated, orthogonal axes.

## The problem it solves

"v1 vs v2" secretly collapses **three independent axes** into one number:

1. **Which *thing* is this part of?** A daily personal tool, the near-term shippable product, and a 36-month enterprise vision are **different products — different audiences, stacks, lifecycles** — *not* stages of one thing.
2. **How mature within that thing?** Each has its own internal version progression, re-triaged every backlog pass.
3. **How far toward the destination?** Each has a far "where we're ultimately going" that decides which *fork* to take today.

Collapsing these is why a far-future concern (an enterprise feature) *feels like it "blows up" the near-term build*, and it's the root of two chronic problems: the recurring **"this will never actually get built"** dread, and the **"I can see 37 chess-moves ahead but can't act on move 1"** paralysis. **The unlock:** you don't need to hold all 37 moves — you need only the few *irreversible forks* (the `[DEALBREAKER-HOOK]`s, below). Separate the axes, capture the irreversible forks, and everything else is free to fall into place later.

## The model

- **Venture** — the top concept (e.g. FracRealHomes; KingStrat AdVentureGPS). "A conceptual grouping of related ideas that evolves over time toward a holistic whole."
- **Product Line** — the venture's **public Version sequence** (`v1.0 → vN.0`): what the market sees / what's "in production." A *stable external identity* that internally behaves like a **moving symlink**, pointing to whichever **Build Line** currently delivers it. (FracRealHomes `v1–v4` → the middle Build Line; `v5+` → the National-AVM Line.)
- **Build Lines** — the **engineering codebases** (repos / stacks) that actually deliver the product. **Named descriptively, per-venture.** Some are **public** (they deliver Product Versions); some are **private** (a personal playground that never ships). Build Lines relate by:
  - **clone-lineage + merge** — shared stack, features flow between them (e.g. a private playground merging up into the public product); or
  - **succession, no-merge** — a different-stack successor (e.g. `proto-divia_ai-enterprise` Python → `divia_ai-enterprise` Rust; the `v4 → v5` jump from the middle Build Line to the National-AVM Line).
- **Phases → Sprints** — the **existing execution machinery *inside* a Build Line, unchanged.** Product Versions are *release milestones* reached by progressing a Build Line through its Phases/Sprints. A single Build Line ships several Product Versions over its life.
- **Triangulation Target** — each Build Line's **far destination**, used to judge forks: *"does this choice keep the Target reachable, or does the easy path force a rewrite?"* (John's 25-year methodology — see below.) Defined *per Build Line* (even the private playground may have one, rarely).
- **Features** — modeled as **graph nodes, not free-text kanban cards** (the kanban board is the human *view*; the graph is the real model). Each carries: **Requester-Source** (John / research / business-dev / dogfooding / partner-deal / C-level), **Build Line + target Product Version**, a **`[DEALBREAKER-HOOK]` flag**, and typed **relations** (to theses, ventures, entities, other Build Lines, other portfolio products).

### Reconciling the vocabulary (the "Stages vs Phases+Sprints" question)

There is **no new "Stage" layer.** The public **Product Versions** *are* the milestones; the existing **Phases → Sprints stay exactly as they are** as the in-Build-Line execution. Hierarchy:

```
Venture
 └─ Product Line  (public Versions v1.0 … vN.0)   ← what the market sees (a moving symlink)
      └─ delivered by ─→ Build Line(s)  (engineering codebases; some private)
                          └─ Phases → Sprints      ← existing execution machinery (unchanged)
```

A Product Version is, concretely, a **release-tag on a Build Line's Phase/Sprint timeline.** The Product Line is the cross-Build-Line *public continuity* (it survives the `v4→v5` jump to a new stack); the Build Line is the *engineering substrate* (it may be replaced under the Product Line).

## `[DEALBREAKER-HOOK]` — the triangulation primitive

A **`[DEALBREAKER-HOOK]`** is a concern that *belongs* to the far Triangulation Target (normally "defer"), **except that getting it wrong now forces a later rewrite** — so it must be **hooked into the near-term Build Line today** (cheap now, catastrophic to retrofit). It is the operational form of John's **"triangulate to where you want to be"**: at each fork, take the path that keeps the destination reachable, even when the "easy" fork looks simpler. (The myopic easy-fork is how teams end up throwing away v2 for a v3 rewrite, v3 for v4, forever; the triangulated path is how a "needs 2–3 servers in 1997" system compounds into a "$1.2B, hundreds of machines across 7 datacenters" platform over ten years *without* a throwaway rewrite.)

This is **one fractal principle at three scales**: it is identical to the entity-model synthesis's *reversible-vs-irreversible* thesis (*pay the irreversible design cost now, defer the implementation*) and to the `ARCHITECTURE_CONVERGENCE` chain (*build the prototype so the Rust rewrite is an impl-swap, not a throwaway*). Fork-choice, architecture, portfolio — the same move. **Most far-future concerns genuinely defer; a small, precious set are `[DEALBREAKER-HOOK]`s. Finding *that set* — not building the future — is the whole job at v1.**

## Worked example — FracRealHomes

| Build Line | Audience / stack | Role | In the Product Line? |
|---|---|---|---|
| **DailySpikeDriver** | John only · Python/Flask · idea-of-the-day playground (Zillow/Redfin replica, Gmail/Zillow-email triage, structured capture) | dogfood + experiment; **merges up** into EstimatePacket Line | **No** — private, never released |
| **EstimatePacket Line** *(middle)* | the venture / buyers · Python/Flask · ~18 mo, 50–100-person-company scale | the real near-term product (the SORTING-PASS diligence scope) | **Yes** — delivers public **v1.0 → v4.0** |
| **National-AVM Line** | enterprise · different stack · 36 mo+ | the far-future public AVM (Codex's home; a categorization bucket for now) | **Yes (later)** — delivers public **v5.0+** (succession, no-merge) |

**Product Line:** FracRealHomes' public Versions — `v1–v4` realized by EstimatePacket Line (same-repo upgrades), `v5+` realized by National-AVM Line (a different-stack successor; the symlink repoints). **DailySpikeDriver feeds the public Build Line via merge but never appears in the Product Line** — so John's "I want a Zillow-email triage parser for *my own use*" is a first-class DailySpikeDriver feature that creates **zero** obligation on the venture's PRD.

## Two benefits beyond clarity

1. **Scoped context-projection (with the graph-DB).** Once Build Lines + their scope/goals/Targets are modeled, an agent discussion can be handed a **Build-Line-scoped projection** that includes *only* relevant context — a Codex discussion about the National-AVM Line is auto-redacted of DailySpikeDriver items *and* of decisions already rejected-for-earlier-Lines; a "Line-2 + Line-3" discussion drops the playground entirely. **Build Lines become natural context-scoping boundaries** — directly serving the orchestrator-context-preservation directive and the scoped-context-projection capability.
2. **The Sorting-Hat matrix.** Every incoming idea routes into the **(Build Line × Product Version, with a Triangulation Target at the far end of each)** matrix. This turns "hundreds of ideas a day = noise I have to block out" into "every idea has a home" — a **cognitive offload from *hold-or-discard* to *capture-and-place*.** The multidimensional layout is what frees the horizon of ideas instead of drowning in it.

## Status

Model **v1**, co-developed 2026-06-17/18. Applies cross-venture. The graph-DB realization (scoped projections, feature-as-node modeling) and the per-venture Build-Line maps are downstream work; this doc is the conceptual canon other docs (the multiagent research workflow; per-venture roadmaps) reference.
