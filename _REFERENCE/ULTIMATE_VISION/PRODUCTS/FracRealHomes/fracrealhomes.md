# Brief (Business) — FracRealHomes

> **Business-side brief** → the **business knowledgebase** (companies / corporate structure / brands / Product Lines / Products / GTM / domains / Product Version-Releases). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repos · Build Lines · Build Envelopes · techstack · Stages→Phases→Sprints · lineage · `[DEALBREAKER-HOOK]`s) is the paired **[engineering brief](../../../SOFTWARE_DEV/fracrealhomes.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Status: scaffold** (Phase 00 pending; pre-code). *Good-enough bootstrap — mined from the `fracrealhomes-web` research corpus + the PROJECT-ORGANIZATION-MODEL worked example.*

## Identity

| Field | Value |
|---|---|
| **Product (full)** | FracRealHomes |
| **Wordmark** | **frac\|real\|homes** (pipe-styled on the website / in marketing) |
| **One-line** | A Pacaso-style venture streamlining the creation, co-purchase, and long-term management of fractional-ownership residential properties, anchored by a "next-gen Zillow estimate" investor-grade valuation engine. |
| **Framing metaphor** | "Next-gen Zillow estimate" — a Zillow/Redfin-grade AVM baseline *extended* with the data points real-estate **investors** care about; flagship differentiator = **view-durability** (a parcel's *future* legal-max-build / view-blocking risk, not just its current view). |
| **First market (beachhead)** | Manhattan Beach / South Bay LA (coastal-luxury, view-dependent). |

## Company / corporate structure · Brands

- **Company:** **Fractional Reality Homes LLC** (the corporate/legal entity; from `DOMAIN_MAPPINGS.md` and the repos' `LICENSE.md` / `© 2026 Fractional Reality Homes LLC`).
- **Brand / business / service name:** **FracRealHomes**, styled **frac|real|homes** on the website and in marketing.
- **Ecosystem stance:** a **standalone startup** — its own venture with its own equity investors — that is *also* a **certified participant in the Divia.Network** connected ecosystem. Both are true at once: independent company, networked participant.
- **Corporate-structure relationship to ExoDev.AI / KingStrat / Divia umbrellas:** **Unknown (not in source files)** — the repos describe FracRealHomes as a standalone venture and a Divia.Network participant, but do not place `Fractional Reality Homes LLC` under any parent holding entity. *(Model as a "question-mark" corporate-structure relationship.)*

## Product Lines → Products

- **Product Line (primary): the fractional-ownership consumer-diligence line.** A buyer-facing diligence + valuation product for fractional luxury residential ownership. Its flagship Product is the **EstimatePacket** (see below). *(The PROJECT-ORGANIZATION-MODEL worked example notes the FracRealHomes **Venture** may carry multiple Product Lines — e.g. a consumer-diligence line vs. a B2B ADU-buildability-data line — but only the consumer-diligence line is concrete today.)*
  - **Product — the FracRealHomes EstimatePacket (the "next-gen Zillow estimate").** A structured, human-reviewed **decision-grade diligence packet** for a property — *not* a single hero number and *not* a national public AVM. It decomposes into side-by-side, deltas-explained components: whole-home value **range** · naïve pro-rata 1/8-share value · **modeled fractional share fair value** (the differentiator) · annual carry / operating-cost sketch · reserves/capex · **view-durability scenario** · liquidity · confidence · review-status. Positioning is **"more complete diligence for fractional luxury ownership," NOT "more accurate than Zillow"** (an honest, defensible, benchmark-safe claim).
  - **Product surfaces (one product, three client surfaces):**
    - **FracRealHomes (Web)** — the Python/Flask web application; primary surface for discovery, valuation detail, co-purchase coordination, and multi-owner operations. *(Repo `fracrealhomes-web`.)*
    - **FracRealHomes (Mobile)** — the cross-platform Flutter/Dart app (iOS + Android) **mirroring the web app** on phone/tablet. *(Repo `fracrealhomes-flutter`.)*
- **Product (distinct, long-term): FracRealHomes 3D Home — the 3D virtual-home capture & reconstruction app.** The venture's **Zillow-3D-Home equivalent**: a user walks a property capturing photos/AR frames, and the app assembles a navigable interior 3D model. **A dedicated long-term product, NOT a throwaway spike**, deliberately kept **separate** from the mobile app (different use-case, different audience — capture-side: listing agents, real-estate photographers, sellers, field staff). Its output feeds downstream into the layered Unreal-Engine neighborhood model and the valuation engine's geometry/sightline inputs. *(Repo `fracrealhomes-android`, native Kotlin/Android. The engineering brief models this as its own Build Line.)*

## The product blend (what FracRealHomes fuses)

- **Zillow / Redfin** — property discovery, listings/parcel browsing, AVM-style valuation baseline (table stakes).
- **Pacaso** — fractional (e.g. 1/8-share) co-purchase and co-ownership structuring for luxury vacation homes.
- **Airbnb** — operations: owner-use scheduling / availability.
- **Asana** — multi-owner project management for maintenance, operating-cost, and tax coordination over long-term ownership.
- **The differentiator on top:** the **fractional value bridge** (whole-home → pro-rata → furnishing/turnkey → calendar/use → cost/reserve → view-risk → governance/liquidity → share fair value, made *visible*) plus the **view-durability** scenario — neither of which Zillow/Pacaso expose.

## Cross-venture dependency — LegendaryMoney (financial services)

FracRealHomes **delegates complex financial-services capabilities to `legendarymoney-web`** (a separate modern-Internet-banking platform, also a Divia.Network participant) **over the Divia protocol**, rather than reimplementing them. Delegated capabilities: real-estate **purchase flows**, **long-term operating-cost accounting**, and **tax-implication** handling. This dependency is what makes otherwise-poor-ROI "manage operating costs and tax implications" features tractable inside what would otherwise be "just a real-estate site." *(LegendaryMoney is its own venture — detailed in its own brief, not here.)*

## Go-to-market / strategic role

- **v1 GTM = a narrow, human-reviewed buyer-diligence packet for one launch market (Manhattan Beach / South Bay), one ownership structure** — *not* a public national AVM. Validate via a **10–25-parcel manual validation program** before a broad app build.
- **Honest positioning (load-bearing):** sell **completeness of diligence**, not accuracy superiority. "Here is what is known, uncertain, and review-required" — never "here is the exact share value and exact future view-loss discount."
- **Suppression as a normal product state:** the product is allowed (and expected) to say "we don't know yet" for any lane lacking evidence — this is a GTM/trust posture, not just an engineering detail.

## Domains (self-contained — from `DOMAIN_LIST.md` + `DOMAIN_MAPPINGS.md`)

- **Canonical domain:** **`fracreal.homes`**.
- **Redirects / aliases (all → `fracreal.homes`):** `fracreal.com` · `fracrealhomes.com` · `fracreality.com` · `fracreality.homes` · `fracrealityhomes.com` · `fracrealty.com` · `fractionalreality.homes` · `fractionalrealityhomes.com` · `fractionalrealty.homes` · `fractionalrealtyhomes.com`.
- **To-buy (not yet owned):** `fractionalreality.com` · `fractionalrealty.com` (flagged `BUY-DOMAIN` in `DOMAIN_MAPPINGS.md`).
- **Registrar / dates (from `DOMAIN_LIST.md`):** all on **Spaceship.com**; e.g. `fracreal.homes` (reg. Aug 8 2024, exp. Aug 8 2026), `fracrealhomes.com` (Aug 8 2024 → Aug 8 2026), `fracreal.com` & `fracreality.com` & `fracrealty.com` (Aug 25 2022 → Aug 24 2026), `fracreality.homes` (Aug 21 2025 → Aug 21 2026), `fracrealityhomes.com` (Sep 2 2025 → Sep 2 2026).
- **Which domain serves which surface (web vs. app subdomains):** **Unknown (not in source files)** — the canonical/alias list does not assign per-surface subdomains.

## Product Version-Releases

Pre-release (scaffold / Phase 00, pre-code). When releases exist they follow the model's **immutable-past / movable-future** rule. The engineering brief sketches a future shape — the **EstimatePacket Line** delivers public **v1.0 → v4.0** and the far-future **National-AVM Line** delivers **v5.0+** — but those are *movable marketing-sketch* targets, re-bucketable until launched, and live on the software-dev side; no released versions exist yet.

## Ideation & Exploration (the durable "result #47" wins — capture, commit to nothing)

*(From the SORTING-PASS "💎 keep regardless" set — sharp, hard-won domain insights worth preserving even where the mechanism is deferred.)*

- ✦ **The Pacaso 8× liquidity trap** — Pacaso listing pages show whole-home value as *exactly 8× the 1/8 share price*, yet the *same home's* resale shares list at *different* prices. So a 1/8 share ≠ whole-home/8; the displayed whole-home value is marketing arithmetic, not an appraisal. **This is the empirical heart of the fractional bridge** (and the differentiator vs. Pacaso's own marketing).
- ✦ **Current view ≠ durable view** — model current view, current premium, and *future durability* as **separate outputs**; the *durability delta* is the value-add (the current view may already be priced into comps).
- ✦ **"Scenario before coefficient / widen the range, don't move the number"** — in sparse luxury data, express risk as bands + confidence, never as a calibrated dollar discount.
- ✦ **Bruce's Beach as an entity-resolution / comp-exclusion test** — the $20M SB-796 reparative saleback (Lots 8&9, the lifeguard admin site) is **not** the hillside park and must be excluded as a comp; a concrete pass/fail diligence test. *(Also tracked as the project's one SOMEDAY backlog item.)*
- ✦ **The Cascadia "Really Big One" null result** — a verified high-media-salience event with *no statistically significant price effect*: media shock ≠ price shock; don't discount without market data.

## Status

**Scaffold (Phase 00 — Ideation & Research — pending; pre-code).** All three repos hold only the inherited workflow system, specs/backlog scaffold, and project docs; the `fracrealhomes-web` repo additionally holds a **73-track Codex research corpus** ("next-gen Zillow estimate") plus a Claude **SORTING-PASS** triaging it into v1 vs. deferred. **License:** proprietary / commercial, closed-source (© 2026 Fractional Reality Homes LLC) — *not* AGPL/open-source. *(Engineering lineage / Build Lines / techstack / dealbreaker-hooks → the [engineering brief](../../../SOFTWARE_DEV/fracrealhomes.md).)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/fracrealhomes.md`](../../../SOFTWARE_DEV/fracrealhomes.md).
- Cross-venture dependency: **LegendaryMoney** (`legendarymoney-web`) — financial services over the Divia.Network / Divia protocol *(its own brief — TBD)*.
- Organizing model + the canonical FracRealHomes worked example: [`../../../PROJECT-ORGANIZATION-MODEL.md`](../../../PROJECT-ORGANIZATION-MODEL.md).
- Source corpus (in `fracrealhomes-web`): `_specs_and_plans/_research/next_gen_zillow_estimate/SORTING-PASS--codex-research-v1-vs-deferred.md` · `analysis-60--unknown-unknowns-and-dealbreakers.md` · `synthesis.md`.
