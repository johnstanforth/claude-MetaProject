# Product — Sattvasic Health

> A personal **health-metrics aggregator** that unifies a lifetime of scattered health data — labs,
> CGM, weight/DEXA, Rx/supplements, calories/macros — into one longitudinal record, with a future
> **correlation engine** as the payoff.

- **Names:** "Sattvasic Health" · repo/dir `sattvasichealth` · env prefix `SATTVASIC_`.
- **License:** **Undocumented** (no LICENSE, no statement — a notable gap vs its dual-licensed siblings).
- **Status:** 🟠 Phase 00 pending; docs-only, zero code. Python 3.12+ · Flask · SQLite→Postgres.

---

## What it is (consensus)
*"Aggregates a lifetime of health data scattered across labs, devices, and apps into one unified, longitudinal record,"* then graphs/trends/(future) correlations. **Seven domains:**
1. **Blood & Lab Results** — normalize the same analyte across labs (Quest, LabCorp) onto one timeline with reference ranges.
2. **CGM Data** — continuous-glucose streams (e.g. Abbott Libre); a prime correlation candidate.
3. **Weight & Body Composition** — frequent smart-scale data + occasional high-accuracy **DEXA** scans on one timeline.
4. **Rx & Vitamin/Supplement Management** — **refill-runway** calculations; intended CVS + Amazon Subscribe & Save integrations.
5. **Food, Calorie & Macro Tracking** — **integrates with sibling TastyPantry.**
6. **Device & Legacy-Data Import** — unify Libre/Quest/scale/BP/Fitbit (incl. sleep)/ketone exports ("many 'new' sources are really import adapters for an existing export format").
7. **Trends & Correlation Analysis** — the payoff layer (e.g. "eating certain foods → headaches ~2h later").

### Cross-product role
Consumes TastyPantry food data for macros (the "health" reader of the Divia.Network fan-out).

> ⚠️ ERRATA E-06: Sattvasic's own docs say it is *"a standalone project, not part of any larger platform,"* integrating **only** with TastyPantry. **LegendaryMoney names it as an ecosystem sibling; Sattvasic doesn't reciprocate** — a one-directional ecosystem membership to reconcile. The recurring weekly-correlation agent (LATER-002) is **not** in the repo. See [`../../ERRATA.md`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** cross-lab analyte normalization onto one timeline (the central data-model challenge); the two-source body-composition merge (scale + DEXA); a refill-runway model; the import-adapter architecture for legacy/device sources (with dedup); the future correlation engine (foods→headaches, CGM vs food logs, sleep vs metrics); a Phase-01 first slice (one metric domain end-to-end, e.g. a lab-result timeline).
- ✦ **New:** the **recurring weekly correlation agent** (LATER-002 §6) — a weekly pass over labs/CGM/weight/macros/Rx that surfaces *hypotheses* ("sleep-quality dips follow late-eating days") as suggestions for the human and their doctor to evaluate — insights the user wouldn't think to query. The purest expression of discover-and-suggest in the health domain. ✦ The refill-runway model is the **same time-decay primitive** as DiviaHome's grocery replenishment and LegendaryMoney's scheduled outflows — build it once, reuse across all three. ✦ Sattvasic + TastyPantry + LegendaryMoney through one Activity Log enables cross-domain insight no single app could see ("late-night fast-food spend tracks with worst-sleep nights"). ✦ Close the license gap (likely AGPL+Commercial like its siblings — confirm).
