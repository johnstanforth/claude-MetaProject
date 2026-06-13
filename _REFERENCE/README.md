# `_REFERENCE/` — The Official Cross-Project Reference Guide

> **One authoritative home for the entire landscape** of inter-related products, ventures, and
> cross-app user stories spanning every project John is building — so the business/product/market
> knowledge lives *here, once*, instead of drifting across two dozen repositories that were each
> written at different times with slightly different pictures of the whole.

- **Created:** 2026-06-12, MetaProject session (immediately following [LATER-002](../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md))
- **Source material:** an exhaustive read-only sweep of *all* non-sprint Markdown across the 24 symlinked projects (10 Opus harvest agents, one per umbrella). Nothing here is invented; every claim traces to a project's own docs, with discrepancies logged rather than silently resolved.
- **Status:** **First edition.** Foundation + product/venture/user-story docs are being written; see the build-status table in [`ULTIMATE_VISION/README.md`](ULTIMATE_VISION/README.md).

---

## Why this exists

The `_projects/README.md` index answered *"what are all these repos?"* This directory answers the bigger questions the repos themselves keep re-answering, inconsistently:

- **What are we actually building, in full?** Every product, with every committed feature *and* every wild idea anyone has had for it.
- **What are the businesses behind them?** The corporate structure, the licensing, the monetization, the go-to-market — the non-engineering layer.
- **How do they fit together?** The cross-app stories (the Divia.Network fan-out, the agent-assisted GTD review, the federated home/work identity) that no single repo can tell on its own.

The motivating realization (from the LATER-002 session): the same vision, written into 24 repos months apart, has **skewed**. One repo says Divia.Life is native Swift/Kotlin; another says Flutter-first. One says `aixodev-collabs` is the workflow "root"; the git history says it's a middle link. The corporate parent is "ExoDev.AI, Inc." in one doc and "ExoDev.Pro, Inc." in another. Rather than chase 24 drifting copies forever, we consolidate the canonical picture **here** and (later) point the repos back at it.

## The longer-term plan (John's intent)

1. **Now:** build this reference as the single authoritative source (read-only sweep of the repos; no repo files modified).
2. **Next few weeks:** review and refine it.
3. **Then:** add a symlink inside each project pointing back to this `_REFERENCE/` resource, **and remove the non-technical vision/branding/product material from the individual repos** wherever it isn't load-bearing for that repo's technical implementation. A future Claude working inside, say, `legendarymoney-web` can then follow the symlink to read *exactly* the product/venture context relevant to its task — without having to read the entire every-product-and-venture database for a simple code change.

The win: per-repo `CLAUDE.md`/`README.md` files shrink to technical truth; the ecosystem story stays correct in one place; the skew stops compounding.

## Directory layout

```
_REFERENCE/
├── README.md                  # this file
├── STATUS.md                  # current state of every project (what works now + the next big phase)
├── ERRATA.md                  # ★ the discrepancy log — contradictions across (and within) projects
└── ULTIMATE_VISION/           # the future-version "Guide" of everything we're trying to build
    ├── README.md              # vision overview + full index + build status
    ├── PRODUCTS/<Umbrella>/   # one doc per product, grouped by corporate/product umbrella
    ├── VENTURES/              # the businesses — layered: a corporate-map README + one doc per family
    └── USER_STORIES/          # cross-product narrative scenarios (the ecosystem in motion)
```

## Conventions every document here follows

- **Consensus first, ideation last.** Each product/venture/user-story doc leads with the **known / agreed / already-decided** material, then closes with an **"Ideation & Exploration"** section holding every speculative, "maybe," someday, or wildly-ambitious idea — captured in full, committed to nothing. (Per John: *capture every idea; the point is to widen the considered space, not to pre-commit.*)
- **Discrepancies are surfaced, not smoothed.** Where the source repos disagree, the doc notes it inline and points to [`ERRATA.md`](ERRATA.md). We never silently pick a winner on something that is John's to decide.
- **Repo names vs product names.** Documents use the product-facing name in prose (e.g. *Divia.Life*, *KingStratVC Knowledgebase*) and the repo/dir short-name in code/paths (e.g. `divialife-flutter`, `kingstratvc-web`).
- **Provenance.** Claims are attributable to the harvested source docs; "Ideation" items note where they came from (a repo's backlog, a research track, or *new this session* — i.e. dreamed up during consolidation).

## For future Claude instances

Read [`STATUS.md`](STATUS.md) for the current-state snapshot, [`ERRATA.md`](ERRATA.md) before trusting any single repo's self-description, and the relevant `ULTIMATE_VISION/PRODUCTS/<Umbrella>/<product>.md` for deep product context. When this reference and a single repo's older docs disagree, **this reference is the intended canonical source** — but check `ERRATA.md`, because some conflicts are still awaiting John's decision.
