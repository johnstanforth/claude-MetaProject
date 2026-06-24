# Product — TastyCal *(working title — name BLOCKED)*

> An **AI photo-based calorie / nutrition tracking app** with a hardware twist: it pairs the AI food-photo view with a **Bluetooth-connected scale** so true portion *weight* — not a photo-only guess — anchors the calorie/macro estimate. A **potential / under-consideration** product-line; the **product concept is unchanged**, but the name "TastyCal" is now **blocked** (domain taken by a third party) and the direction needs more research before committing. **"TastyCal" is retained below only as a working label**, not a chosen name.

- **Names:** "TastyCal (by TastyPal)" is a **working title / placeholder — BLOCKED, pending rename**. `tastycal.com` is **registered to a third party**, so the name is unavailable; a new name (and which audience/home it ships under) awaits further research. repo/dir `tastycal` (none yet) · umbrella TastyPal — see [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- **License:** **Undocumented** (no repo yet). **Status:** 🔵 **Potential / under consideration**, **name blocked** — a recalled concept, zero code, not a committed product-line, and the working title is unavailable. John on the concept: *"still might be, I guess."*
- **Domain:** intended **`tastycal.com`** is **NOT available — registered to a third party**, so "TastyCal" cannot be the shipping name. (Previously recalled by John as registered to us; that recollection is now corrected.) A replacement name + domain is an open research item.

---

## What it is (the recalled concept)

A consumer **AI calorie / nutrition tracker** in the same surface category as the breakout app **"Cal AI"** — point the camera at a plate, the AI identifies the foods, and it logs calories and macros. The product was conceived earlier, then forgotten and documented nowhere until now; this brief is its first capture. What makes it a *TastyPal* product rather than a me-too clone is the differentiator below and the food-database tie-ins TastyPal already owns.

### The differentiator — photo **plus** a Bluetooth scale (the thesis)

John never believed in **photo-ONLY** portion estimation — eyeballing grams from a 2-D image is the weak link in every photo-first tracker. TastyCal **combines the AI photo view with a Bluetooth-connected scale** that measures the food's **actual weight**, then correlates that true portion size with the AI-identified food type. AI answers *what* the food is; the scale answers *how much*; together they yield a **materially more accurate** calorie/macro estimate than photo-estimation alone. The scale is the moat — the part a photo-only competitor cannot cheaply match.

### Competitive context — "Cal AI" (→ R-007)

The category reference point is **Cal AI**, an AI photo calorie-tracker reportedly built by a **high-school-student founder**, reportedly **acquired by MyFitnessPal in a nine-figure deal**, and reportedly **pulled from the App Store by Apple** over a payment-screen / App-Review policy violation. Two things follow: (1) Cal AI's surprising popularity and a clean acquisition comp are evidence the **category is worth entering**; (2) its App-Store removal is a concrete **compliance lesson** for any consumer app we ship here. First-pass source evidence — the product/acquisition/removal picture **and** the accuracy critique of photo-only estimation that validates the scale thesis — is now captured below in the **[Cal AI competitive / accuracy dossier](#cal-ai-competitive--accuracy-dossier-raw-evidence--to-be-modeled-in-ksvgps-later)**; the deep-research item is **R-007** in [`../../../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../../../_backlog_TODOs/RESEARCH-BACKLOG.md) — reference both for the build/buy/differentiate decision.

## Origin — shared tech with Sattvasic Health (white-label framing)

TastyCal is **not new hardware** — it's a **second brand surface on tech already planned for [Sattvasic Health](../SattvasicHealth/sattvasichealth.md)**. John had already designed the **Bluetooth-connected scale** as part of Sattvasic Health's health/nutrition tracking (its food/calorie/macro domain). Cal AI's popularity makes him consider **white-labeling** that Sattvasic-Health scale-based approach as a **TastyPal-branded** app, reaching a **different audience**:

- **Sattvasic Health** — the **health/wellness** audience: longitudinal health-metrics aggregation, labs/CGM/weight/macros, the correlation engine.
- **TastyCal (by TastyPal)** — the **culinary / TastyPal** audience: the same scale + AI-food-ID, framed around food and cooking rather than clinical health tracking.

Net: the **same underlying scale + AI-food-ID tech, two brand surfaces** — one health-first, one food-first. (Engineering view of the shared stack: the [TastyPal engineering brief](../../../SOFTWARE_DEV/tastypal.md) and [Sattvasic Health engineering brief](../../../SOFTWARE_DEV/sattvasichealth.md).)

### Direction — primary home is Sattvasic Health; the TastyPal white-label is the secondary, research-gated possibility (John's current lean)

John's **current lean** (captured as *considered, not committed*): the **primary / original home of the scale-app is the "real, health-based" version inside [Sattvasic Health](../SattvasicHealth/sattvasichealth.md)** — the serious, health-first nutrition tracker where the BLE-scale + AI-food-ID tech originates. This lean is **reinforced if Sattvasic Health is structured as a Public Benefit Corp (PBC) owned by the nonprofit Divia.Foundation**, since a PBC-under-the-Foundation home strengthens the **health-first + nonprofit** branding the scale-app fits best (see the Sattvasic Health brief's [PBC-under-Divia.Foundation framing](../SattvasicHealth/sattvasichealth.md)).

The **TastyPal-adjacent, white-labeled, rebranded version** — mass-market appeal, especially **younger users**, benefiting from **TastyPal food-DB tie-ins** (TastyPantry inventory, taste preferences, recipes) — is a **secondary possibility that needs more research before deciding whether (and what) to build, and what to rename it.** The "TastyCal" label is itself blocked (see the header), so the white-label, if pursued, ships under a yet-to-be-chosen name. In short: **primary = the Sattvasic Health (health-first) scale-app; secondary = the TastyPal white-label, research-gated and pending rename** — same tech underneath, two candidate brand surfaces, with the health-first one currently in front.

## TastyPal tie-ins (why it belongs under TastyPal)

A TastyCal user living in the TastyPal world arrives with **food databases the health audience doesn't have**, which sharpen both the AI food-ID and the logging UX:

- **Pantry inventory** via [TastyPantry](tastypantry.md) — what's actually on hand narrows the AI's food-identification candidates (you're far likelier to be eating what's in your pantry).
- **Taste preferences** — the palate/flavor signal (the spicemaster3000 "taste fingerprint" line of work in [`tastypal.md`](tastypal.md)).
- **Recipes** — TastyPantry's compound-food / recipe model lets a logged dish resolve to its base-ingredient macros instead of a single opaque photo guess.

These tie-ins are the concrete reason a scale-and-AI tracker is **stronger as a TastyPal product** than as a standalone clone — and the reason the *same* tech reads differently to the TastyPal audience than to the Sattvasic-Health audience.

## Cal AI competitive / accuracy dossier (raw evidence — to be modeled in KSVGPS later)

> **Captured raw evidence** for the build/buy/differentiate decision (→ **R-007**). This is a first-pass capture of one well-argued third-party source to be **modeled in KSVGPS later**, not a finished analysis; the open verification items are flagged inline and in R-007. The throughline: independent builders, arguing from different angles, **converge on the same conclusion John already holds** — that **photo-only portion estimation is the broken link**, which is exactly what a **BLE-scale × AI-food-ID** combo fixes.
>
> **Source:** Reddit *r/CoachingSoftware* (cross-posted *r/fitmeals*), **"CalAI just got pulled from the App Store — and it exposes a bigger problem with AI calorie tracking,"** by **u/r1setraining**, ~2026-04-16/17 — <https://www.reddit.com/r/CoachingSoftware/comments/1sn4up8/>. (Single-source, opinion-and-practitioner-thread; treat as raw evidence pending the R-007 verification pass.)

### What Cal AI is (the comp)

**Cal AI** is the viral AI-photo calorie tracker — point the camera at a plate, it IDs the foods and logs calories/macros. Reportedly **$30M+ revenue** and **acquired by MyFitnessPal in a nine-figure deal** — the popularity + a clean acquisition comp are the evidence the **category is worth entering**.

### The App-Store-removal / compliance story (the cautionary tale)

- **The claim:** Cal AI was reportedly **pulled from the Apple App Store on 2026-04-16**. ⚠️ **UNVERIFIED** — later commenters dispute it (*"it's still on the app store"*), so whether it was fully pulled, briefly pulled, or reinstated is **unconfirmed** (resolve in R-007).
- **Why (the alleged violation):** a developer ("Arib") exposed that Cal AI's **payment screen looked like a native iOS in-app-purchase sheet but was actually Stripe**, via a private **Superwall** integration — routing payments **outside Apple IAP** to dodge the **30% commission**. Post-**Epic v. Apple (2025)**, US developers **may** link out to external payment, but may **not** make the external interface **look like a native iOS purchase screen** without disclosure — Cal AI crossed that line.
- **What made it worse:** the Superwall flow was reportedly optimized to add **friction to CANCELLATION** (hard to exit subscriptions) → a **complaint avalanche** → which is what forced Apple's hand.
- **Practitioner notes:** another dev reports trying Stripe and being **shut down by Apple on first submission**; the recommended safe path is **accept Apple IAP + join the Apple Small Business Program** (drops the commission **30% → 15% on the first $1M**).
- **Lesson for us:** if we ever **white-label or resell** an AI nutrition tool, **audit its subscription / billing practices first** — reputation rides on the reseller, not just the original builder.

### The accuracy critique (the core — this is what validates the scale thesis)

- **Reported error rates:** simple whole foods (banana, plain chicken) **≈ 10–20%**; mixed / home-cooked / restaurant / saucy dishes **≈ 30–40%**; homemade-meal studies **≈ 50%** (i.e. guessing half the time).
- **Why that's fatal:** on a **2,000-cal diet**, **20% = ±400 cal/day**, **30% = ±600 cal** — *a whole meal's worth of calories invisible* — which **destroys** any deficit or macro target.
- **Why photo-only fails (the four failure modes):**
  1. **Portion estimation — THE problem.** AI can ID *"pasta"* but cannot tell **80g vs 200g** from a single 2-D angled photo (varied lighting, unknown plate diameter, **no depth cues**). This is the single biggest error source — and **exactly what a scale fixes.**
  2. **Ingredient opacity.** Oil, sauce sugars, hidden cheese are **invisible in a photo** — and "hidden calories" are precisely **where dieters hemorrhage their deficit**.
  3. **Cultural / regional dishes.** Models trained on **Western food datasets** → biriyani / injera / adobo have **less training data** → **compounding error** on exactly the cuisines TastyPal's flavor work cares about.
  4. **False precision / the trust feedback loop.** A **confident number** plus macros **to 2 decimals** makes users **trust a wrong output** — *"false precision is more dangerous than admitted uncertainty."*
- **🔑 KEY — the calibration rebuttal (preserve exactly).** One commenter argued the inaccuracy is fine **if you only track up/down trends** — treat the app's number as a **constant baseline** to re-calibrate against. The OP **rebuts** this: the error is **NOT uniform / linear — it is RANDOM**, so it **cannot even be calibrated away as a relative trend**. **This is the strongest argument for measuring real weight:** random photo error is **uncorrectable** (you can't subtract a moving, direction-less bias), whereas a **scale removes the random portion-estimation error at the source.**

### Practitioner consensus (independent voices converging on weight / precise quantity)

- **HeyChef.co dev:** most tools *"reverse-engineer the meal from the **PLATE** (the Output)"* — inherently inaccurate; HeyChef instead starts from the **RECIPE + PRECISE QUANTITIES (the Input)**, with nutrition computed from the **Ciqual (ANSES) food database** — *"moves effort from guessing to planning."* **🔑 KEY** — philosophically **identical to TastyCal's measure-the-input thesis** (measure what goes in, don't reverse-guess from a photo of the output).
- **Another builder:** place a **fork / spoon next to the plate** as a size reference — a **crude proxy for what a real scale does properly**; *"if you don't know the exact weight of your food you are always guessing."*
- **"Input Performance AI" dev:** users **prefer a 10-second scanner** over searching + guessing grams; he personally **tolerates ~85% accuracy for convenience** (especially at restaurants); his app lets you **edit each ingredient's grams**. **🔑 KEY** — the **convenience-vs-accuracy tradeoff is real**, and the scale's job is to **deliver accuracy *without* losing the 10-second speed.**
- **OP's bottom line:** **manual weighing ≈ 85% accuracy**, and photo+AI can be **INaccurate by about that same margin**; *"the camera is good at recognizing ingredients but not portions, and portions dictate the calories."*

### 🔑 KEY takeaway (the thesis validation)

Strong third-party validation that **(a)** photo-only **portion estimation is the broken link**, **(b)** the error is **random and therefore uncorrectable** (not a calibratable trend), and **(c)** independent builders **converge** on **weight / precise-quantity / recipe-input** as the fix — which is **exactly what a BLE-scale × AI-food-ID delivers** (the camera IDs *what*, the scale measures *how much*). Bonus: a concrete **App-Store-compliance cautionary tale** for any consumer app — and especially for **white-labeling/reselling** one.

### Open items to verify (→ R-007)

- Whether Cal AI was **actually pulled** from the App Store (fully / briefly / reinstated) — the source's headline claim is **disputed in its own comments**.
- The **$30M+ revenue** and **nine-figure MyFitnessPal acquisition** figures (single-source / informal).
- The **Superwall-via-Stripe** mechanism and the **cancellation-friction → complaint-avalanche → Apple action** chain.
- The **error-rate ranges** (10–20% / 30–40% / ~50%) and the **homemade-meal study** they cite.
- The **Epic v. Apple (2025)** external-payment / disclosure rule as applied here, and the **Apple Small Business Program 30%→15%** detail.

## Status

- **Product-line:** 🔵 **Potential / under consideration** — a working-draft concept, not a committed TastyPal product-line.
- **Name:** **"TastyCal" is a working title and is now BLOCKED** — `tastycal.com` is registered to a third party, so the name is unavailable; a rename + further research is pending before any commit.
- **Direction:** **primary home = the health-first scale-app inside Sattvasic Health** (esp. if Sattvasic is a PBC under Divia.Foundation); the **TastyPal-adjacent white-label** is a **secondary, research-gated possibility** that itself needs a new name.
- **Code / repo:** none. No repo, stack, or phase exists yet.
- **Domain:** intended `tastycal.com` is **registered to a third party — not available** (corrects the earlier "recalled as owned" note).
- **License:** **Undocumented** (no repo).

## Cross-references

- Venture / umbrella: [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- Sibling TastyPal product-lines: [`tastypantry.md`](tastypantry.md) (pantry inventory — tie-in source) · [`tastypal.md`](tastypal.md) (venture business brief, where TastyCal is listed).
- **Shared scale tech / white-label source:** [`../SattvasicHealth/sattvasichealth.md`](../SattvasicHealth/sattvasichealth.md) (Sattvasic Health business brief — the Bluetooth-scale + AI-food-ID origin).
- Engineering form: [`../../../SOFTWARE_DEV/tastypal.md`](../../../SOFTWARE_DEV/tastypal.md) (TastyCal engineering section) · [`../../../SOFTWARE_DEV/sattvasichealth.md`](../../../SOFTWARE_DEV/sattvasichealth.md) (shared BLE-scale + AI-food-ID stack).
- Competitive research: **R-007 — "Cal AI"** in [`../../../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../../../_backlog_TODOs/RESEARCH-BACKLOG.md).
</content>
</invoke>
