# Product — TastyCal

> An **AI photo-based calorie / nutrition tracking app** with a hardware twist: it pairs the AI food-photo view with a **Bluetooth-connected scale** so true portion *weight* — not a photo-only guess — anchors the calorie/macro estimate. A **potential / under-consideration** product-line under the TastyPal venture, parallel to TastyPantry and TastyTrucks.

- **Names:** "TastyCal (by TastyPal)" · repo/dir `tastycal` (none yet) · umbrella TastyPal — see [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- **License:** **Undocumented** (no repo yet). **Status:** 🔵 **Potential / under consideration** — a recalled concept, zero code, not a committed product-line. John on it: *"still might be, I guess."*
- **Domain:** intended **`tastycal.com`** (John recalls it as registered; **not yet recorded in [`../../../DOMAIN_LIST.md`](../../../DOMAIN_LIST.md)** — a registry gap to reconcile, not a confirmed entry).

---

## What it is (the recalled concept)

A consumer **AI calorie / nutrition tracker** in the same surface category as the breakout app **"Cal AI"** — point the camera at a plate, the AI identifies the foods, and it logs calories and macros. The product was conceived earlier, then forgotten and documented nowhere until now; this brief is its first capture. What makes it a *TastyPal* product rather than a me-too clone is the differentiator below and the food-database tie-ins TastyPal already owns.

### The differentiator — photo **plus** a Bluetooth scale (the thesis)

John never believed in **photo-ONLY** portion estimation — eyeballing grams from a 2-D image is the weak link in every photo-first tracker. TastyCal **combines the AI photo view with a Bluetooth-connected scale** that measures the food's **actual weight**, then correlates that true portion size with the AI-identified food type. AI answers *what* the food is; the scale answers *how much*; together they yield a **materially more accurate** calorie/macro estimate than photo-estimation alone. The scale is the moat — the part a photo-only competitor cannot cheaply match.

### Competitive context — "Cal AI" (→ R-007)

The category reference point is **Cal AI**, an AI photo calorie-tracker reportedly built by a **high-school-student founder**, reportedly **acquired by MyFitnessPal in a nine-figure deal**, and reportedly **pulled from the App Store by Apple** over a payment-screen / App-Review policy violation. Two things follow: (1) Cal AI's surprising popularity and a clean acquisition comp are evidence the **category is worth entering**; (2) its App-Store removal is a concrete **compliance lesson** for any consumer app we ship here. The full product/acquisition/removal picture and the accuracy critique of photo-only estimation are queued as deep-research item **R-007** in [`../../../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../../../_backlog_TODOs/RESEARCH-BACKLOG.md) — reference it for the build/buy/differentiate decision.

## Origin — shared tech with Sattvasic Health (white-label framing)

TastyCal is **not new hardware** — it's a **second brand surface on tech already planned for [Sattvasic Health](../SattvasicHealth/sattvasichealth.md)**. John had already designed the **Bluetooth-connected scale** as part of Sattvasic Health's health/nutrition tracking (its food/calorie/macro domain). Cal AI's popularity makes him consider **white-labeling** that Sattvasic-Health scale-based approach as a **TastyPal-branded** app, reaching a **different audience**:

- **Sattvasic Health** — the **health/wellness** audience: longitudinal health-metrics aggregation, labs/CGM/weight/macros, the correlation engine.
- **TastyCal (by TastyPal)** — the **culinary / TastyPal** audience: the same scale + AI-food-ID, framed around food and cooking rather than clinical health tracking.

Net: the **same underlying scale + AI-food-ID tech, two brand surfaces** — one health-first, one food-first. (Engineering view of the shared stack: the [TastyPal engineering brief](../../../SOFTWARE_DEV/tastypal.md) and [Sattvasic Health engineering brief](../../../SOFTWARE_DEV/sattvasichealth.md).)

## TastyPal tie-ins (why it belongs under TastyPal)

A TastyCal user living in the TastyPal world arrives with **food databases the health audience doesn't have**, which sharpen both the AI food-ID and the logging UX:

- **Pantry inventory** via [TastyPantry](tastypantry.md) — what's actually on hand narrows the AI's food-identification candidates (you're far likelier to be eating what's in your pantry).
- **Taste preferences** — the palate/flavor signal (the spicemaster3000 "taste fingerprint" line of work in [`tastypal.md`](tastypal.md)).
- **Recipes** — TastyPantry's compound-food / recipe model lets a logged dish resolve to its base-ingredient macros instead of a single opaque photo guess.

These tie-ins are the concrete reason a scale-and-AI tracker is **stronger as a TastyPal product** than as a standalone clone — and the reason the *same* tech reads differently to the TastyPal audience than to the Sattvasic-Health audience.

## Status

- **Product-line:** 🔵 **Potential / under consideration** — a working-draft concept, not a committed TastyPal product-line. Recalled this session; documented here for the first time.
- **Code / repo:** none. No repo, stack, or phase exists yet.
- **Domain:** intended `tastycal.com` (recalled as owned; not yet in `DOMAIN_LIST.md`).
- **License:** **Undocumented** (no repo).

## Cross-references

- Venture / umbrella: [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- Sibling TastyPal product-lines: [`tastypantry.md`](tastypantry.md) (pantry inventory — tie-in source) · [`tastypal.md`](tastypal.md) (venture business brief, where TastyCal is listed).
- **Shared scale tech / white-label source:** [`../SattvasicHealth/sattvasichealth.md`](../SattvasicHealth/sattvasichealth.md) (Sattvasic Health business brief — the Bluetooth-scale + AI-food-ID origin).
- Engineering form: [`../../../SOFTWARE_DEV/tastypal.md`](../../../SOFTWARE_DEV/tastypal.md) (TastyCal engineering section) · [`../../../SOFTWARE_DEV/sattvasichealth.md`](../../../SOFTWARE_DEV/sattvasichealth.md) (shared BLE-scale + AI-food-ID stack).
- Competitive research: **R-007 — "Cal AI"** in [`../../../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../../../_backlog_TODOs/RESEARCH-BACKLOG.md).
</content>
</invoke>
