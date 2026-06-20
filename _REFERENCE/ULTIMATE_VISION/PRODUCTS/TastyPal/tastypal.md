# Brief (Business) — TastyPal

> **Business-side brief** → the **KSVGPS business knowledgebase** (company / corporate structure / brands / Product Lines / Products / GTM / domains / Product Version-Releases). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repos · Build Lines · Build Envelopes · techstack · lineage) is the paired **[engineering brief](../../../SOFTWARE_DEV/tastypal.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Venture-level brief — consolidates the prior single-product `spicemaster3000.md` + `tastypantry.md` files (now superseded).** *Good-enough bootstrap.*

## Identity

| Field | Value |
|---|---|
| **Venture (full)** | TastyPal |
| **Company** | **TastyPal, Inc.** |
| **One-line** | An informal culinary umbrella holding a consumer kitchen brand (the TastyPal app + the TastyPantry pantry-inventory app) and a standalone flavor-tech bet (the `spicemaster3000` project). |
| **Framing metaphor** | "Your real kitchen, understood" — pantry + spice + recipe unified into one consumer story (a *new-this-session* aspiration; see Ideation). |

## Company / corporate structure · Brands

- **Company:** **TastyPal, Inc.** — the legal/conceptual umbrella; informal "culinary umbrella" holding several distinct bets.
- **Brand family (per `DOMAIN_MAPPINGS.md`):** parent brand **TastyPal**; **Software Product `TastyPal App`**; **Subsidiary `TastyPantry by TastyPal`**; **Subsidiary `TastyTrucks by TastyPal`**; and the **`spicemaster3000` project** (working-title flavor-tech app, positioned fully standalone).
- **Ecosystem tie (contested):** TastyPantry is also framed as **Divia.AI ecosystem plumbing** — the canonical "food eaten" node of the Divia.Network fan-out and the seed prototype the household apps descended from — but its own in-repo docs call it *"standalone … not part of any larger platform,"* contradicting that role (see [`../../../ERRATA.md`](../../../ERRATA.md) E-06). `spicemaster3000` is **correctly** standalone (zero Divia/TastyPal references in its docs; only tie is the AIXO.Dev workflow methodology and John personally — ERRATA E-06).

## Product Lines → Products

- **Product Line:** TastyPal's consumer culinary line — an informal umbrella, not (yet) a single unified product. Holds the following Products / subsidiaries:
  - **Product: TastyPal App.** The parent-brand software product. Details (scope, surfaces, feature set) **TBD — not described in the source files** beyond the brand/domain record; the *new-this-session* aspiration is a unifying "pantry + spice + recipe = your real kitchen, understood" consumer brand if the standalone bets prove out (see Ideation).
  - **Product: TastyPantry** (subsidiary **"TastyPantry by TastyPal"**). A kitchen **pantry-inventory** app organized around five interlocking domains: **Foods/Ingredients** (each with an on-hand quantity), **natural-language Food Logs** ("I ate two quesadillas" → decrement inventory), **Grocery Receipts** (increment inventory), **per-store Shopping Lists** (driven by depletion), and **Recipes as compound foods** (logging "2 quesadillas" cascades decrements to base ingredients). Its venture meaning is mostly **infrastructural** — the "food eaten" slice of the Divia.Network fan-out (food → TastyPantry; macros → Sattvasic; expense → LegendaryMoney) and the bootstrap seed for the household-app chain. No business model is documented; treat it as Divia.AI ecosystem plumbing rather than an independent business.
  - **Product: TastyTrucks** (subsidiary **"TastyTrucks by TastyPal"**). **Documented only as a brand + domain record** in `DOMAIN_MAPPINGS.md` (`tastytrucks.app` + alias; BUY-DOMAIN `tastytruck.com` / `tastytrucks.com`). **No description, scope, status, or repo is in the source files — Unknown (not in source files).**
  - **Product: spicemaster3000** (working title; the standalone flavor-tech bet). A web app to **explore spice blends, individual core spices, and flavor pairings** — for home cooks and spice enthusiasts. The one product in the venture with a genuine, articulated **venture thesis** (below). Positioned **fully standalone** (no Divia/TastyPal ties in its docs). *(Engineering note: the `spicemaster3000` repo is being reframed as the **`proto-tastypal-web` DailySpikeDriver-level Build Line driving the TastyPal web app** — see the [engineering brief](../../../SOFTWARE_DEV/tastypal.md). That is a software-dev-side modeling decision; the consumer brand framing here is unchanged.)*

## The spicemaster3000 venture thesis

*(From the `spicemaster3000` synthesis + vision docs — the one bet in the venture with an articulated commercial opportunity.)*

- **Market:** cites a **$23.6B global spice market (2035)** and a **$48B personalized-nutrition market (2030)**.
- **The gap:** a survey of **35+ existing apps** found **none scoring above a C** on flavor profiling / blend building / flavor-bridge discovery — a "massive unoccupied product space."
- **The moat:** the assembled data is hard to replicate — **23,690 pairings / 595 subjects** parsed from *The Flavor Bible* (6 rank tiers, ETHEREAL → AVOID), **25,595 FlavorDB molecules**, **6 vendor catalogs** (Penzeys, Burlap & Barrel, The Spice House, See Smell Taste, Morton & Bassett, Everest), ratio-based blend formulas, and an **18-track research corpus** (~18,400 lines, 200+ sources). *(Data-count erratum: 23,690/595 is authoritative-on-disk vs a report-card table's 23,378/584 — see [`../../../ERRATA.md`](../../../ERRATA.md).)*
- **B2B expansion ideas:** a **Restaurant Partnership API** and a **White-Label Platform** (Penzeys / Burlap & Barrel / The Spice House each running a co-branded blend-builder on their own site).
- **Personal resonance:** a partner's "Indian food" anecdote drives the "Indian food is not one thing" thesis; John's **Nasrani / Saint-Thomas-Christian family lineage (~2,000 years to Cochin, Kerala)** anchors the spice-trade-history deep-dive. The closing line of both major docs: *"It is time to build."*

## Product Version-Releases

Pre-release across the venture (all bets are Phase 00 or earlier). When releases exist, they follow the model's **immutable-past / flexible-future** rule (past = git-matched historical record; future = a movable "marketing sketch" re-bucketable like kanban cards). No public version numbers have been assigned yet — **TBD**.

## Go-to-market / strategic role

- **spicemaster3000** is positioned as the **most spin-out-able consumer product in the portfolio** — real market, real moat, a clean standalone brand, and a charismatic founder story (the Kerala lineage, the partner anecdote). Of all the non-dev products, it is the one most able to stand entirely on its own. GTM specifics beyond the B2B API / white-label ideas above are **TBD — not in source files.**
- **TastyPantry**'s strategic role is **infrastructural**, not commercial: it is the consumption-data node powering DiviaHome's nightly-replenishment loop (time-decaying grocery items + escalating errand priority — LATER-002) and the seed of the Divia.Network household-app fan-out.
- **TastyPal App / TastyTrucks** GTM — **Unknown (not in source files).**

## Domains (self-contained — from `DOMAIN_LIST.md` + `DOMAIN_MAPPINGS.md`)

- **Company (TastyPal, Inc.):** **`tastypal.com`** — redirect/alias **`tastypal.cc`**.
- **TastyPal App:** **`tastypal.app`** — redirect/alias **`tastypalapp.com`**.
- **TastyPantry by TastyPal:** **`tastypantry.app`** — redirect/aliases **`tastypantryapp.com`**, **`tastypantry.food`**, **`tastypantry.kitchen`**, **`tastypantry.life`**, **`tastypantry.recipes`**. **BUY-DOMAIN target: `tastypantry.com`** (not yet owned).
- **TastyTrucks by TastyPal:** **`tastytrucks.app`** — redirect/alias **`tastytrucksapp.com`**. **BUY-DOMAIN targets: `tastytruck.com`, `tastytrucks.com`** (not yet owned).
- **spicemaster3000:** **no dedicated domain in the source files** — recorded only as a GitHub project (`@johnstanforth/spicemaster3000`). Any future product domain is **TBD** (likely under the TastyPal brand if the standalone bet rolls up; not stated).
- **Registrar / dates (from `DOMAIN_LIST.md`, all via Spaceship.com):** `tastypal.app` (reg. 2018-05-08, exp. 2027-05-08) · `tastypal.cc` (reg. 2026-03-04, exp. 2027-03-04) · `tastypal.com` (reg. 2017-11-10, exp. 2026-11-10) · `tastypalapp.com` (reg. 2022-02-25, exp. 2027-02-25) · `tastypantry.app` (reg. 2026-05-28, exp. 2027-05-28) · `tastypantry.food` / `.kitchen` / `.life` / `.recipes` (all reg. 2026-03-04, exp. 2027-03-04) · `tastypantryapp.com` (reg. 2026-05-28, exp. 2027-05-28). *(`tastytrucks.*` dates not listed in `DOMAIN_LIST.md` — Unknown.)*

## Ideation & Exploration (capture everything, commit to nothing)

**From the spicemaster3000 corpus** *(a small selection of a very large set — Track 18 alone enumerates ~50 features across 13 categories):*

- A 12-axis **"taste fingerprint"** (radar profile), supertaster detection, dietary/allergy integration (incl. Jain no-allium), and **exposure-gap-vs-genuine-dislike** differentiation (3-state model with gentle re-introduction — the implicit-data principle applied to palate).
- An interactive **blend builder** (ratio sliders, real-time flavor radar, base/accent/heat auto-classification, synergy/masking modeling, AI-suggested ratios, "what-if" simulation, a 50+ classic-templates library) and a **Flavor Bridge Explorer** ("Mexican → Indian: cumin is the bridge") — flagged as potentially the single most distinctive feature.
- Discovery surfaces: an interactive **flavor-space map** (UMAP, pathfinding), guided "flavor journeys," "surprise me."
- A **"Virtual Spice Cabinet"** (virtual inventory + freshness tracking + "what can I make right now") and **Pantry Auto-Replenishment** — which independently re-invents TastyPantry's inventory/shopping-list model, scoped to spices, *with no cross-reference between the two repos.*
- Community / smart-kitchen: "taste-twin" matching, Bluetooth smart-scale guided dispensing, AR spice ID.
- Far-horizon moonshots: a **Universal Flavor Translator** ("give me the Mexican version of butter chicken"), genomic taste profiling (23andMe TAS2R38/OR6A2 import), a **Spice Genome Project** (GC-MS of 200+ spices, open-licensed), collective taste intelligence at 1M profiles, the 2031 "cook tonight like our Oaxaca trip, from what's in my cabinet, calibrated for my supertaster guest" scenario.

**From the TastyPantry corpus:**

- The five-domain data model is the Phase-00 work: how NL food logs map to structured entries + decrement inventory; the recipe→base-ingredient cascade; receipt ingestion/reconciliation; keeping the schema Postgres-portable.
- **Inventory-depletion → auto shopping list is exactly the nightly-replenishment loop** (LATER-002 / `diviahome-nightly-replenishment`): TastyPantry holds the consumption data that powers DiviaHome's time-decaying grocery items and escalating errand priority.

**✦ New this session (venture-level):**

- ✦ **Wire the two together** — spicemaster3000's "Virtual Spice Cabinet" *is* a specialized TastyPantry; the obvious synergy is a shared inventory substrate (spices as a TastyPantry food category) feeding both apps. Neither repo currently acknowledges the other; this is the clearest unexploited cross-product opportunity in the portfolio (see [`../../../ERRATA.md`](../../../ERRATA.md) E-06).
- ✦ **spicemaster3000 as the most spin-out-able consumer product** — real market, real moat, a clean standalone brand, a charismatic founder story.
- ✦ **The Flavor Bible dataset as a licensable B2B asset** — the cleaned, structured pairing corpus could be a data product in its own right (to recipe apps, CPG R&D, the very spice vendors it catalogs), independent of the consumer app.
- ✦ **A TastyPal consumer brand** that unifies pantry + spice + recipe into one "your real kitchen, understood" story — turning the informal-umbrella TastyPal into an actual consumer line if the standalone bets prove out.

## Status

- **Venture:** informal culinary umbrella; **no business model documented** beyond the spicemaster3000 thesis.
- **TastyPantry:** 🟠 Phase 00 **pending**, zero code, scaffold only.
- **spicemaster3000:** 🟡 Phase 00 research **in progress** (a large corpus); only skeleton Flask code.
- **TastyPal App / TastyTrucks:** **Unknown (not in source files)** — brand + domain records only.
- **Licensing (business-side):** **Undocumented** for all bets — both extant repos carry no license; no commercial/proprietary terms are stated in the source files. *(Engineering-side license detail → the [engineering brief](../../../SOFTWARE_DEV/tastypal.md).)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/tastypal.md`](../../../SOFTWARE_DEV/tastypal.md).
- Venture: [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- Errata (standalone-vs-ecosystem contradiction E-06; data-count erratum): [`../../../ERRATA.md`](../../../ERRATA.md).
- Cross-product / Divia.Network fan-out: `../../USER_STORIES/divia-network-fanout.md` · nightly replenishment: `../../USER_STORIES/diviahome-nightly-replenishment.md`.
- *(Supersedes the prior single-product files `spicemaster3000.md` + `tastypantry.md` in this directory.)*
