# LATER-013 — Revisit "playground" vs "spike" as Ceremony semantics (and whether the Ceremony axis needs both terms)

- **Captured:** 2026-06-28 (John + Claude), while relabeling the GEN2 Roadmap-horizon axis to five values.
- **Status:** open — not blocking; the GEN2 Ceremony axis currently uses `playground` and that stays. This captures a terminology nuance to settle later.
- **Owning project:** cross-venture (GEN2 / KSVGPS modeling). Related: the GEN2 three-axis split (Ceremony / Roadmap-horizon / Lifecycle) and [LATER-010](LATER-010-build-line-lifecycle-status-independent-of-succeeds-edge.md).

## The nuance

`playground` and `spike` mean subtly different things to John and to working engineers, and we should decide whether the **Ceremony** axis needs both terms (or a rename) rather than collapsing them:

- **spike** — a throwaway probe to *test ONE specific thing*, then discard. Short-lived, single-question, deleted after the answer is obtained. (This is the classic XP/agile meaning.)
- **playground** — an ongoing, *daily-dogfooding / experimentation* build-line where many ideas get tried continuously (e.g. John's `fracrealhomes-dailyspikedriver`). It is NOT thrown away; it is a standing surface. Ideas that prove out get **lift-and-shift promoted** into the current-stable build-line.

## Worked example (FracRealHomes Property-Valuation product-line)

- **DailySpikeDriver** = the `playground` build-line — daily dogfood where new valuation ideas are tried. Roadmap-horizon = `daily-prototype`.
- **EstimatePacket** = the `current-stable` build-line — proven ideas are lift-and-shift promoted here. Roadmap-horizon = `current-stable`.
- **National-AVM** = the committed long-range build-line (~36–48mo). Roadmap-horizon = `far-horizon`.

So in this example the *same* product-line spans three roadmap horizons across three build-lines, and the playground→current-stable promotion is a real workflow we want the model to express.

## What to revisit

1. Does the **Ceremony** axis need a distinct `spike` value in addition to `playground` (e.g. a true throwaway probe vs. a standing dogfood surface), or is `playground` sufficient?
2. If both are kept, define them crisply in the GEN2 Ceremony seed (`CeremonyLevel`) and document the promotion workflow (playground → current-stable) somewhere durable.
3. Confirm this terminology against the canonical [`_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](../_REFERENCE/PROJECT-ORGANIZATION-MODEL.md) Build-Line definitions when that model is next touched.

## Context — why this came up now

We were collapsing the old single-timeline "roadmap" mental model into **three orthogonal axes**: Ceremony (`playground`/`standard`/`formal`), Roadmap-horizon (now five values: `daily-prototype`/`current-stable`/`far-horizon`/`future-planned`/`someday-maybe`), and Lifecycle (`active`/`maintained`/`frozen-reference`/`archived`). The old roadmap value `retired` was folded into Lifecycle `archived`. During that discussion John flagged that "spike" had been the wrong label for the playground ceremony — hence this item.
