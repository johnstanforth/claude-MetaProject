# Venture — LegendaryMoney

> An AI personal-finance manager **for messy, incomplete, real-world money** — "Quicken for the rest
> of us." Its own LLC, a serious founder pedigree, and a dual-license path to a commercial product.

- **Steward:** **LegendaryMoney LLC** (Peoria, Arizona) & John Stanforth.
- **License:** **Dual AGPLv3 + Commercial (CLA-based)** — explicit and documented (one of only two repos with a real license statement, alongside DiviaHome).
- **Source:** `legendarymoney-web` (README ~30KB, CLAUDE.md, LICENSE.md, ROADMAP).

---

## 1. Consensus

**The product.** A standalone, self-hosted Python/Flask **PFM built for incomplete data** — "the opposite of traditional finance software built for tidy complete records." Core mechanics:
- **Natural-language capture:** *"I had El Pollo Loco for dinner"* → an inferred transaction (merchant, category, **estimated amount with a confidence band**).
- **Balance assertions as first-class data:** *"I have $23 in my wallet"* vs last week's *"$36"* → reconciled by **balance-gap differencing** that generates estimated "plug" entries.
- **Every transaction carries a precision level** (confirmed / inferred / estimated) + confidence band + provenance trail — *"without the user ever touching a debit/credit column."*
- **Cash/wallet and informal accounts** ("money Mom owes me," a roommate split scribbled on a junk-mail envelope, a trip fund) are first-class, not afterthoughts.

**The founders & the credibility story.** Cofounders **John and David**, who met in **1997 on the original dev team at Digital Insight Corporation** — John was one of only two developers who rewrote its flagship internet-banking app (1997–99), drove the **1999 IPO**, grew it into the world's largest internet-banking company, through the **$1.2B Intuit acquisition (2007)** and later NCR integration. Both then spent 20+ years there plus a decade+ on Network Security teams at Intuit, BlackLine, SigFig, and Early Warning (Zelle). The positioning leans hard on this: *not "vibe-coded AI slop" — "built for NOT ACCOUNTANTS, by people who previously helped build the billion-dollar platforms that accountants trust."*

**Positioning:** "Quicken for Millennials → Gen Z → Gen Alpha"; audience skews younger, cash-heavy, gig/under-banked. A financial-literacy-gap mission framing (explicitly analogized to the obesity epidemic).

**Roadmap shape (the load-bearing v1/v2 split):**
- **v1 = scan-and-import / data unification** — gather years of scattered fragments (SMS meal/purchase logs, bank/card CSV/OFX, CashApp/Venmo/PayPal histories, receipt photos) into **one clean confidence-aware ledger.** Deep NL AI is *explicitly out of scope for v1.* Motto: *"first unify, then understand."*
- **v2 = understand & infer** — the full Divia.AI agent (NL classification, advanced reconciliation, ambient GPS/voice/connected-card "shock-and-awe"), plus **publishing LegendaryMoney-namespaced DiviaCard types to the global DiviaCards registry** (e.g. `DiviaCard::LegendaryMoney::transaction(...)`) as the public cross-app contract.

**Ecosystem stance:** a **standalone product with its own brand that also participates in Divia.Network** — strategy decided as "own finance-native models internally; DiviaCards as the public contract." Carries placeholder fields for the future global Divia.AI identity.

## 2. Ideation & Exploration (capture everything, commit to nothing)

**From the repo (README / ROADMAP):**
- An **8-principle design creed** — accessible-not-accounting; incomplete-by-default; confidence-over-false-precision; estimate-don't-abstain; capture-losslessly-parse-later; reconcile-from-anchors; meet-users-in-natural-language; **no-shame-no-audit-voice.**
- A **learning loop** — user confirms/corrects/splits inferred entries; the engine sharpens merchant/category priors from *this* user's history (the implicit-data principle applied to money).
- **Bank/card/payment-app connectors** (Plaid-style or direct) layered atop the import-adapter architecture (Later); **separate LegendaryMoney mobile-capture apps** feeding the same household server (placeholder repos, not yet created).
- A **"remaining financial runway"** view (forgiving, range-based budgeting) and the compound query *"I'm hungry, what are my options for dinner?"* answered from TastyPantry (food on hand) + LegendaryMoney (spendable tonight given scheduled outflows).

**✦ New this session:**
- ✦ **The recurring-agent ledger reviewer** (LATER-002) — a nightly/weekly pass that surfaces anomalies, balance-assertion drift, and recurring-charge changes, and *learns categorization rules from the user's observed corrections instead of asking them to configure rules.* Not yet captured in the repo (its backlog is empty — see [`ERRATA.md` E-12`](../../ERRATA.md)).
- ✦ **"Financial runway" as a flagship anxiety-reducer** — lead the product with "how many days can I coast?" rather than spreadsheets; the emotional opposite of guilt-driven budgeting apps.
- ✦ **The founder story as the wedge** — "the people who built the internet-banking platform your bank runs on, now building the anti-Quicken" is a rare, defensible trust narrative; it could anchor the whole brand.
- ✦ **Confidence bands as a *visible* product aesthetic** — make estimated-vs-confirmed a first-class visual language (the thing screenshots sell), turning "incomplete data" from an apology into the differentiator.
- ✦ **Spin-out optionality** — of all the portfolio products, LegendaryMoney has the clearest path to an independent venture (own LLC, own brand, real market, credible team); worth tracking as a potential raise/spin-out.
