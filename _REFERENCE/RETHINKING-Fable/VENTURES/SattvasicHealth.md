# Venture Dossier — Sattvasic Health (Rethought)

> A personal **health-metrics aggregator**: a lifetime of scattered health data — labs, CGM, weight/DEXA, Rx/supplements, food/macros — unified into one longitudinal record the person owns, with correlation *hypotheses* as the payoff layer. Corporate placement is a **modeled question-mark by design** (Candidate A: PBC under the planned DIVIA Innovation Foundation · Candidate B: own/informal umbrella) — the canonical L7 open-question relationship, and the scale-app direction lean reinforces Candidate A.

## 1. The seven domains (scope intact, two upgrades)

Blood & labs (cross-lab analyte normalization — the central data-model challenge) · CGM streams · weight/body-comp (smart-scale + DEXA two-source merge) · Rx & supplements (**refill runways = P-03**, CVS + Subscribe & Save integrations) · food/calorie/macro (consumes TastyPantry's what-was-eaten; the **BLE-scale × AI-food-ID** capture path — camera answers *what*, scale answers *how much*) · device & legacy import (ImportKit P-04 adapters + dedup) · trends & correlation.

**Upgrade 1 — the correlation layer relocates and gets governance (R-14).** Cross-domain correlation (foods → headaches; late eating → sleep dips; money-stress × health) properly lives at the *whole-personal-graph* level (the cross-domain correlation service, [`../03`](../03-IDEAS-LEDGER.md) §1 [P]) — Sattvasic is its health-domain *renderer*. Governance is non-negotiable: multiple-hypothesis discipline, effect sizes, hypothesis-not-diagnosis framing, clinician-shareable exports, explicit non-diagnostic product copy — staying firmly on the FDA general-wellness side of the line. The weekly correlation agent (P-05) surfaces *suggestions for the human and their doctor to evaluate* — the purest expression of discover-and-suggest in the portfolio, and the easiest to ruin by overclaiming.

**Upgrade 2 — the scale-app is this venture's product, with a white-label option out.** The BLE-scale + food-ID tech originates here (the health-first home; the lean John captured), with the TastyPal-branded culinary white-label as a secondary, research-gated (R-007), rename-pending possibility (the "TastyCal" name is blocked). The photo-only competitor category's weakness is structural and worsening (R-10) — portion error is geometric and *random*, hence uncalibratable; the scale removes it at the source. Cal-AI's reported traction/acquisition validates the category; its App-Store compliance saga is the cautionary tale (verify both — R-007).

## 2. Ecosystem stance

An independent product that **implements the Divia.Network standard** (the E-06 "standalone" self-description dissolves under the protocol doctrine): the macros interpretation of household Facts (P-01), TastyPantry's downstream consumer, a refill-runway feeder to the nightly packet and Morning Briefing, and a watch-list subscriber to Patternicity (drug recalls, supplement research) with all resolution done locally. License gap to close (likely AGPL+Commercial per siblings — unconfirmed; a Phase-00 checklist item).

## 3. Ideation & Exploration

**Existing (carried):** cross-lab analyte timelines as the Phase-01 first slice · the two-source body-comp merge · refill-runway reordering · import-adapter dedup architecture · the weekly correlation agent · "build the time-decay primitive once, reuse across finance/home/health" (now P-03 formally).

**Proposed (new this rethink):**
- **The CGM × flavor loop (S-08):** contribute glycemic-response history to the "cook tonight" compound query — flavor-forward meal plans that respect *your* measured responses; the personalized-nutrition market claim made concrete and demo-able.
- **Local-first health AI ([`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §4):** on-device models for parsing and first-pass correlation over the most intimate data class in the portfolio — the strongest possible instantiation of "your data never leaves infrastructure you control," and a PBC-story amplifier.
- **Clinician mode:** a physician-facing export (timeline + hypotheses + provenance + effect sizes) that turns the aggregator into an appointment-prep tool — distribution through the person's existing care relationship rather than around it.
- **Correction-store trust surface (P-12):** "you confirmed 14 of 19 suggested entries this month" — visible precision as the trust-building UI pattern shared with LegendaryMoney.
- **The PBC-under-Foundation synergy, stated as strategy:** if Candidate A resolves true, the nonprofit-owned PBC structure is itself the GTM (health data + public-benefit governance + Code Vault = a trust position no VC-backed health app can copy structurally). This is an argument *for* Candidate A to weigh at decision time, not a resolution.
- **Household health, carefully:** opt-in, per-member-consented family views (kids' Rx runways, shared allergy registry feeding TastyPantry/spicemaster exclusions) — the household graph's most sensitive and most valuable extension; per-member consent is the hard requirement.

**Rejected / Flawed:**
- **⛔ The correlation engine as an unguarded auto-insight feed (R-14).** Breadth of data × naive correlation = false positives that erode trust and edge toward medical-device territory. Repair: the governance stack above; correlations are *hypotheses with receipts*.
- **⛔ Photo-only calorie logging as a fallback capture tier positioned as equivalent.** It is not equivalent and the product's own thesis says so; offering it unlabeled would launder known-random error into the longitudinal record. Repair: photo-only entries are allowed but visibly banded as low-confidence estimates (P-02 rendering), with the scale path always suggested.
- **⛔ Resolving the corporate placement editorially.** It is the model's canonical question-mark; both candidates import as alternatives with the documented lean — John resolves it, the graph records when.
