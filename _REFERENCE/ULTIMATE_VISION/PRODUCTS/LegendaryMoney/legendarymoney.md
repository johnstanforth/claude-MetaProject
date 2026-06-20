# Brief (Business) — LegendaryMoney

> **Business-side brief** → the **business knowledgebase** (company / corporate structure / brands / Product Lines / Products / GTM / domains / Product Version-Releases). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repo · Build Lines · Build Envelopes · techstack · Stages→Phases→Sprints · lineage · license · `[DEALBREAKER-HOOK]`s) is the paired **[engineering brief](../../../SOFTWARE_DEV/legendarymoney.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Status: docs-only** (Phase 00 pending; pre-code). *Good-enough bootstrap — mined from `legendarymoney-web`'s README / CLAUDE.md / LICENSE.md, the prior VENTURE+PRODUCT briefs, and `DOMAIN_*`. (Supersedes the old single-file `legendarymoney.md`, whose still-valid content is migrated below; its engineering content moved to the paired engineering brief.)*

## Identity

| Field | Value |
|---|---|
| **Product (full)** | LegendaryMoney |
| **Wordmark** | LegendaryMoney |
| **One-line** | An AI personal-finance manager built for messy, incomplete, real-world money — "Quicken for the rest of us." |
| **Framing metaphor** | A confidence-aware ledger that **estimates rather than abstains**, captures in natural language, and reconciles from balance anchors — "the opposite of finance software built for tidy, complete records." |
| **Heritage tagline** | "Quicken for Millennials" → "…for Gen Z" → "…for Gen Alpha" (the generational label kept changing; the through-line — meet younger people where they are, never punish imperfect records — did not). |

## Company / corporate structure · Brands

- **Company / commercial steward:** **LegendaryMoney LLC** — an Arizona limited liability company, **Peoria, AZ**. Copyright holder of record (`© 2026 LegendaryMoney LLC (Peoria, Arizona) & John Stanforth`).
- **Subsidiary:** **LegendaryFinancial.AI** (listed under LegendaryMoney LLC in `DOMAIN_MAPPINGS.md`). Role/scope: **Unknown (not in source files)** — appears only as a corporate-structure + domains entry. *(Model as a "question-mark" corporate-structure relationship.)*
- **Corporate-structure relationship to ExoDev.AI / KingStrat / Divia umbrellas:** **Unknown (not in source files)** — the repo describes LegendaryMoney as a **standalone product with its own brand and identity** (own LLC) that *also participates* in Divia.Network; it is not placed under any parent holding entity in the source files. *(Model as a "question-mark" corporate-structure relationship.)*
- **Founders:** cofounders **John** (Stanforth) and **David** — veteran FinTech builders (heritage story below).
- **Brand:** single brand = *LegendaryMoney* (product, LLC, and domains all share the name).

## Product Lines → Products

- **Product Line:** a standalone consumer **personal-finance-manager (PFM)** line — self-hosted, household-scoped, natural-language-first; "the anti-Quicken." *(No second Product Line is defined in the source files.)*
  - **Product: LegendaryMoney (web app).** Repo `legendarymoney-web` is **only the web-application piece** of the broader product; LegendaryMoney **mobile apps (Android/iOS)** and any **companion devices** are intended to live in their own repositories *(not yet created — placeholders)*. Six **proposed** feature domains (Phase 00 settles them): **(1) Accounts & Balances** (incl. cash/wallet + informal accounts; balance assertions as first-class inputs); **(2) Transactions** (each tagged confirmed / inferred / estimated, with a confidence band + provenance — *no debit/credit column ever exposed*); **(3) Activity Log** (a lossless natural-language money inbox; typed or **spoken** via a DiviaHome device); **(4) the Inference & Estimation Engine** — the distinctive heart (merchant/category priors, balance-gap reconciliation, confidence modeling, a learning loop); **(5) Budgets / Goals / Insights** (forgiving, range-based — incl. the "remaining financial runway" view + virtual-envelope budgeting); **(6) Scan-and-Import** (the v1 core; see below).

## Product Version-Releases

The product's public roadmap is the **load-bearing v1/v2 split** (the source files describe it as "v1/v2," predating the PROJECT-ORGANIZATION-MODEL's formal Version-Releases; future numbers stay movable like kanban cards per the model's immutable-past / flexible-future rule):

- **v1 — Unify & capture.** A **scan-and-import / data-unification** project: gather years of scattered legacy fragments into **one clean, confidence-aware ledger.** Scope: the accounts / balances / transactions model; balance assertions; **lossless** natural-language capture in the Activity Log; basic, transparent estimation; multi-user household. **Deep natural-language AI is explicitly out of scope for v1.** Motto: *"first unify, then understand."*
- **v2 — Understand & infer.** The full **Divia.AI agent**: natural-language classification & parsing, advanced inference/reconciliation, and the ambient **GPS / voice / connected-card "shock-and-awe"** intelligence — plus **publishing LegendaryMoney-namespaced DiviaCard types** to the global DiviaCards registry as the public cross-app contract (engine/registry mechanics → the [engineering brief](../../../SOFTWARE_DEV/legendarymoney.md)).

## Go-to-market / strategic role

- **Positioning:** *built for "NOT ACCOUNTANTS," by people who previously helped build the billion-dollar platforms that accountants trust.* Explicitly the **polar opposite of "vibe-coded AI slop"** money apps — a 20-plus-year vision from veteran FinTech builders.
- **The founder-pedigree wedge (the credibility story).** Cofounders **John and David** met in **1997** on the original dev team at **Digital Insight Corporation**. John was one of only two developers who rewrote its flagship Internet-banking app (1997–99); that product drove the **1999 IPO**, grew Digital Insight into the **world's largest Internet-banking company** (larger than its next seven competitors combined), and led to the **$1.2B Intuit acquisition (2007)** and later NCR integration (where it remains the world's largest Internet-banking service). David helped **create and run** its Networking and Network-Security departments (at one point the company's only network engineer). Both then spent 20-plus years there, plus a decade-plus more on Network-Security teams at **Intuit, BlackLine, SigFig, Early Warning (Zelle)** and others — safeguarding hundreds of billions in transaction data for 300-plus banks/credit unions and their millions of customers under constant regulatory-compliance pressure. The wedge: *"the people who built the internet-banking platform your bank runs on, now building the anti-Quicken."*
- **Mission:** make money management **accessible** — a 20-year-old should not need double-entry ("double-ledger") accounting to manage bills, escape the paycheck-to-paycheck trap, or plan for retirement. Framed as a **financial-literacy-gap** problem (explicitly analogized to the post-1950s American obesity epidemic — a systemic, not personal, failing) that modern AI can finally close by doing the accounting *behind the scenes.*
- **Audience:** younger, often **cash-heavy**, frequently **unbanked / under-banked** — gig and side-hustle earners whose financial record is a scatter of texts, screenshots, and half-remembered purchases.
- **Ecosystem stance:** a **standalone brand** that **also participates in Divia.Network** — strategy decided as *"own finance-native models internally; LegendaryMoney-defined DiviaCards as the public cross-app contract."* It is the personal-finance sibling of DiviaHome / TastyPantry / Sattvasic Health (DiviaHome's own README names LegendaryMoney as the ecosystem's finance sibling). The signature ecosystem demo: one sentence — *"I had El Pollo Loco for dinner"* — fanning out into a TastyPantry food-log entry, Sattvasic Health macros, and a **LegendaryMoney estimated dining expense.** *(This is the "expense" node of the Divia.Network fan-out — see [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md).)*

## Cross-venture relationships

- **FracRealHomes → LegendaryMoney (LegendaryMoney is the *provider*).** The **FracRealHomes** venture (`fracrealhomes-web`) **delegates complex financial-services capabilities to LegendaryMoney over the Divia protocol / Divia.Network** rather than reimplementing them — delegated capabilities include real-estate **purchase flows**, **long-term operating-cost accounting**, and **tax-implication** handling. Here LegendaryMoney is the **consumed financial-services platform**; FracRealHomes is the consumer. *(FracRealHomes is its own venture — detail in its own [`../FracRealHomes/fracrealhomes.md`](../FracRealHomes/fracrealhomes.md); not described here.)*
- **Divia.Network siblings (peer integration, not dependency):** DiviaHome · TastyPantry · Sattvasic Health — first-ever cross-app integrations over the Divia.Network vision. *(Note: integration reciprocity is uneven — Sattvasic Health does **not** name LegendaryMoney back; see [`../../../ERRATA.md`](../../../ERRATA.md).)*

## Domains (self-contained — from `DOMAIN_LIST.md` / `DOMAIN_MAPPINGS.md`)

- **Company (LegendaryMoney LLC):** **`legendarymoney.com`** (registered Jul 2018) — redirect/alias **`legendary.money`** (registered May 2024).
- **Software Product (`LegendaryMoney App`):** **`legendarymoney.app`** (registered Feb 2022) — redirect/alias **`legendarymoneyapp.com`** (registered Feb 2022).
- **Subsidiary (LegendaryFinancial.AI):** **`legendary.financial`** (registered Sep 2025). **To buy** (flagged `BUY-DOMAIN`): `legendaryfinancial.ai`, `legendaryfinancialai.com`.
- *(All registrar = Spaceship.com per `DOMAIN_LIST.md`.)*

## Ideation & Exploration (capture everything, commit to nothing)

*(Migrated from the predecessor briefs + repo README/ROADMAP — high-value product ideas, not commitments.)*

- **8-principle design creed:** accessible-not-accounting · incomplete-by-default · confidence-over-false-precision · estimate-don't-abstain · capture-losslessly-parse-later · reconcile-from-anchors · meet-users-in-natural-language · **no-shame-no-audit-voice.**
- **The learning loop:** user confirms / corrects / splits inferred entries; the engine sharpens *this user's* merchant/category priors from their own history (the implicit-data principle applied to money).
- **Informal / virtual accounts as first-class:** "money Mom owes me," a roommate split scribbled on a junk-mail envelope, a trip fund, a savings jar — not afterthoughts.
- **Connectors (Later):** bank / card / payment-app connectors (Plaid-style or direct) layered atop the import-adapter architecture; separate **mobile-capture apps** feeding the same household server (placeholder repos).
- **The compound cross-app query** — *"I'm hungry, what are my options for dinner?"* answered from **TastyPantry** (food on hand) + **LegendaryMoney** (spendable tonight, given scheduled outflows) — the inverted "remaining financial runway" view.
- ✦ **Confidence bands as a *visible* product aesthetic** — make estimated-vs-confirmed a first-class visual language (the thing screenshots sell); turn "incomplete data" from an apology into the differentiator.
- ✦ **Lead with "financial runway"** ("how many days can I coast?") as the flagship anxiety-reducer — the emotional opposite of guilt-driven budgeting.
- ✦ **The recurring ledger-review agent** (LATER-002 §6) — a nightly/weekly pass surfacing anomalies, balance-assertion drift, and recurring-charge changes, **learning categorization rules from observed corrections instead of asking the user to configure them.** *(Forward-decision; not yet in the repo — see ERRATA below.)*
- ✦ **Spin-out optionality** — of all portfolio products, LegendaryMoney has the clearest path to an **independent venture** (own LLC, own brand, real market, credible team); worth tracking as a potential raise / spin-out.

## Status

**Phase 00 — Ideation & Research (PENDING).** Docs-only: a polished (~30 KB) README, `CLAUDE.md`, `LICENSE.md`, and the inherited workflow/specs scaffold — **zero application code, no phases or sprints.** Project stance: explicitly **experimental + volatile → "no sacred cows"** for ≥6 months (from June 2026). The next step is to open Phase 00 and settle the **confidence-aware ledger model**, the **inference/estimation engine**, the **scan-and-import architecture**, and the v1 vertical-slice scope.

- **License (summary):** **Dual-licensed AGPLv3 + Commercial (CLA-based)** — the community release is AGPLv3; under a CLA, **LegendaryMoney LLC** retains the right to relicense commercially so prototyped functionality can fold into proprietary products. One of only two repos with a real, explicit license statement (alongside DiviaHome). *(Full license/CLA mechanics → the [engineering brief](../../../SOFTWARE_DEV/legendarymoney.md).)*

> ⚠️ ERRATA: the repo asserts *"extensive PFM-market deep research already gathered"* but its `_research/` is effectively empty (`.gitkeep` only) — claimed, not present (see [`../../../ERRATA.md`](../../../ERRATA.md) E-11). The recurring-agent "ledger reviewer" (LATER-002 §6) is a forward-decision **not yet propagated into the repo** (E-12).

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/legendarymoney.md`](../../../SOFTWARE_DEV/legendarymoney.md).
- Venture file: [`../../VENTURES/LegendaryMoney.md`](../../VENTURES/LegendaryMoney.md).
- Divia.Network fan-out user story (the "expense" node): [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md).
- Consuming venture (financial-services dependency): [`../FracRealHomes/fracrealhomes.md`](../FracRealHomes/fracrealhomes.md).
- Conceptual model: [`../../../PROJECT-ORGANIZATION-MODEL.md`](../../../PROJECT-ORGANIZATION-MODEL.md) · discrepancies: [`../../../ERRATA.md`](../../../ERRATA.md) (E-11 capability-ahead-of-reality · E-12 LATER-002 propagation).
