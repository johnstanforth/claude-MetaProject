# Venture Dossier — FracRealHomes (Rethought)

> **Fractional Reality Homes LLC** (brand: frac|real|homes) — a Pacaso-style venture streamlining the creation, co-purchase, and long-term multi-owner management of fractional luxury residential properties, anchored by an investor-grade valuation engine ("next-gen Zillow estimate"). Standalone startup; a certified Divia.Network protocol adopter; beachhead: Manhattan Beach / South Bay coastal-luxury.

## 1. The product architecture (three products, one evidence graph)

- **The EstimatePacket** — a human-reviewed, decision-grade diligence packet per property: whole-home value **range** · naïve pro-rata share value · **modeled fractional-share fair value** · carry/operating sketch · reserves/capex · **view-durability scenario** · liquidity · confidence · review status. Positioning is *completeness of diligence*, never accuracy-superiority; "we don't know yet" is a normal product state. Surfaces: web (Flask) + mobile mirror (Flutter).
- **The 3D Home product** (`fracrealhomes-android`, native Kotlin) — walkthrough capture → navigable interior model. Repositioned per [`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §5: a **data-acquisition instrument** whose durable value is rights-clean first-party geometry/sightlines feeding the valuation engine (capture tech itself commoditizes via splatting; Google's photoreal tiles forbid analytical use, so owned geometry stays scarce).
- **The co-ownership operations layer** — Airbnb-style owner-use scheduling + Asana-style multi-owner maintenance/cost/tax coordination, with **money mechanics delegated to LegendaryMoney over the protocol** (S-12): co-owner splits as informal accounts, reserve funds as P-03 runways, purchase flows and tax handling consumed rather than rebuilt.

**The empirical heart:** the **Pacaso 8× liquidity trap** — listing pages show whole-home value as exactly 8× the ⅛-share price while the same home's resale shares list at different prices; a share ≠ home/8. The **fractional value bridge** (whole-home → pro-rata → turnkey → calendar → reserves → view-risk → governance/liquidity → share fair value, every step visible) is the product's reason to exist. Domain gems preserved as first-class test assertions: **Bruce's Beach** as the entity-resolution/comp-exclusion pass-fail case; the **Cascadia null result** (high media salience, no measurable price effect — never discount without market data); **"scenario before coefficient / widen the range, don't move the number"** (hook #7); the legal-classification front-door gate (LLC-interest / TIC / private-residence-club / securities-style) before any share estimate.

## 2. The Idea set (Layer A)

Five distinct Ideas channel here: **AVM** (one Idea, two Build-Lines across scale — EstimatePacket now, National-AVM far; the canonical same-idea-different-scale case) · **view-durability risk** (current view ≠ durable view; the durability *delta* is the value-add; the flagship differentiator neither Zillow nor Pacaso exposes) · **co-ownership marketplace** · **3D capture & reconstruction** · **ADU-advisory** (distinct customer/value; channel question-mark: FRH line vs. own venture). New this rethink: shared surfaces with ReDreamRebuild (S-07) — see below.

## 3. Ideation & Exploration

**Existing (carried):** the 10–25-parcel manual validation program before any broad build · suppression-as-normal-state · view-risk as labeled bands (Current Observed / Legal Maximum / Likely Rebuild / Filed Permit / Human Reviewed) · the multi-Product-Line future (consumer diligence vs. B2B ADU-data) · Unreal-Engine layered neighborhood display (display-only; analytics stay first-party).

**Proposed (new this rethink):**
- **The Renovation-ROI Estimator (S-07):** the EstimatePacket machinery pointed at *improvement* decisions — post-reno value bands by material tier, the informed-vs-default $150K delta made explicit; joint surface with ReDreamRebuild, each venture keeping its audience skin.
- **Permit/zoning watch via the world graph (S-03):** per-parcel watch-lists (filings, zoning items, disaster events) from the Patternicity service feeding view-durability and carry scenarios — the EstimatePacket becomes a *living* document (P-07) rather than a point-in-time PDF.
- **Governance receipts (S-11/P-11):** co-ownership votes, reserve disbursements, and use-scheduling decisions signed and attached to the share — a verifiable governance history that travels with resale, directly attacking the information asymmetry inside the liquidity trap.
- **Before/after 3D evidence (S-07):** pre/post-remodel captures as valuation training data, marketing proof, and dispute evidence — three consumers, one walkthrough.
- **Turnkey-furnishing valuation from the durables lane (S-14):** the home-inventory interpretation of receipts pricing the "turnkey" bridge step from data instead of estimate.
- **Contractor-safety input for operations (S-07):** ReDreamRebuild's OSHA report-cards informing vendor selection for co-owned-home maintenance — a lookup, not a merger.
- **Fractional-share market analytics as a data product (far):** the accumulating resale-vs-bridge dataset is the industry's missing price-discovery layer; hold as a dated far target.

**Rejected / Flawed:**
- **⛔ The 3D product as a wow-demo bet.** Capture commoditizes quarterly; a cinematic-tour app will be table stakes by 2028. Repair (already reflected above): build it as the geometry/sightline instrument for the valuation engine — the analytics are the moat, the viewer is packaging.
- **⛔ Any "more accurate than Zillow" drift.** The honest-positioning discipline is load-bearing (benchmark-safe, trust-building, and the only claim a sparse luxury market can support); accuracy-superiority claims invite exactly the benchmark war the venture cannot win at v1. Repair: completeness-of-diligence language enforced in every surface, per the source discipline.
- **⛔ Building payments/accounting/tax in-house.** The delegation edge to LegendaryMoney is the portfolio's cleanest composition-without-merger example; rebuilding it would burn the beachhead budget on undifferentiated plumbing. Repair: protocol delegation (S-12), with the seam explicitly modeled.
