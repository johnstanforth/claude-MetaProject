# Venture Dossier — LegendaryMoney (Rethought)

> An AI personal-finance manager for **messy, incomplete, real-world money** — a confidence-aware ledger that estimates rather than abstains. Own LLC (Peoria, AZ), own brand, dual AGPLv3+Commercial, the portfolio's clearest independent spin-out path — and, quietly, the **epistemic reference implementation** for the whole portfolio: the P-02 envelope was invented here.

## 1. The product

A self-hosted PFM built for the opposite of tidy records: natural-language capture ("I had El Pollo Loco for dinner" → an inferred transaction with merchant, category, and an **estimated amount with a confidence band**); **balance assertions as first-class data** ("I have $23 in my wallet" vs. last week's $36 → balance-gap differencing generates plug entries); every transaction tagged confirmed/inferred/estimated with provenance, **no debit/credit column ever shown**; cash, informal, and virtual accounts ("money Mom owes me", the trip fund) as first-class citizens. Six proposed domains: Accounts & Balances · Transactions · Activity Log (the lossless money inbox, typed or spoken) · the Inference & Estimation Engine (the distinctive heart: priors, reconciliation, confidence modeling, the P-12 learning loop) · Budgets/Goals/Insights (forgiving, range-based; the **financial runway** view) · Scan-and-Import (the v1 core, on ImportKit P-04).

**Roadmap (load-bearing):** v1 = unify (years of scattered fragments → one clean confidence-aware ledger; deep NL explicitly out of scope). v2 = understand (the full agent: NL classification, ambient GPS/voice/connected-card fusion via P-01 interpretation-of-interpretations, and LegendaryMoney-namespaced DiviaCards as the public contract). The confidence-aware ledger schema is the irreversible v1 seam (hook #8).

## 2. Positioning and the founder wedge

"Built for NOT ACCOUNTANTS, by the people who built the internet-banking platforms accountants trust": John + David, met 1997 at Digital Insight — John one of two developers who rewrote the flagship internet-banking app that drove the 1999 IPO and the $1.2B Intuit acquisition (2007); David built/ran its network-security function; both followed by decades at Intuit/BlackLine/SigFig/Early Warning (Zelle). The wedge is rare and defensible; it can anchor the brand. Audience: younger, cash-heavy, gig/under-banked users whose financial record is texts, screenshots, and half-memories. Mission framing: the financial-literacy gap as a *systemic* failure (the obesity-epidemic analogy) that behind-the-scenes AI accounting finally closes. Emotional flagship: **lead with runway** ("how many days can I coast?") — the anti-guilt budget.

## 3. Ecosystem stance (protocol, not family)

A standalone brand that **implements the Divia.Network standard**: the "expense" interpretation of household Facts; the delegated financial-services provider for FracRealHomes (purchase flows, operating-cost accounting, tax handling — S-12, where informal accounts scale up to "co-owner #3 owes the reserve fund"); the recurring-charge data source for the news-subscription optimizer (S-06/R-01 repair) and the budget rail for the remodel stack (S-07). It carries placeholder global-identity fields (hook #2) and may adopt Divia-compatible identity — its choice, per the open-protocol doctrine.

## 4. Ideation & Exploration

**Existing (carried):** the 8-principle creed (accessible-not-accounting · incomplete-by-default · confidence-over-false-precision · estimate-don't-abstain · capture-losslessly-parse-later · reconcile-from-anchors · natural-language-first · no-shame-no-audit-voice) · the learning loop · bank/card/payment-app connectors atop the import adapters · separate mobile-capture apps · the compound dinner query (answered fully in S-08) · confidence bands as the visible product aesthetic · the nightly/weekly ledger-review agent (anomalies, assertion drift, recurring-charge changes; learns rules from corrections instead of asking for configuration) · spin-out optionality.

**Proposed (new this rethink):**
- **PriceScanner as the best-value engine (S-06), three lanes:** groceries; **materials** (the 5-Lowe's discontinued-flooring hunt as a standing agent watch across regional stores); **recurring services/subscriptions** (the ledger already sees every recurring charge — surface cheaper equivalents and stale subscriptions). Whether feature, second Product-Line, or standalone stays a modeled question-mark.
- **Runway objects everywhere (P-03):** scheduled outflows, bill due-dates, reserve funds, and return windows as first-class rotting deadlines feeding the morning packet.
- **The durables lane (S-14):** purchases spawn Possession records (warranty runways, return countdowns, insurance inventory) — the receipt stream's third interpretation.
- **Anomaly staging with autonomy graduation:** disputed-charge drafts, renewal cancellations, and balance-transfer suggestions staged at L1, graduating per-action-type toward L2 under P-09 spend-cap credentials — agentic *money* actions are the highest-trust-bar case in the portfolio; get the plumbing right here and everything else inherits it.
- **Financial-runway sharing as a household primitive:** an opt-in, coarse-grained "can we afford the big grocery run this week?" signal to DiviaHome's nightly packet — cross-app value without exposing the ledger.
- **The correction store as the moat framing (P-12):** years of a user's own confirmations are what make *their* priors sharp; say it in the marketing — "it gets you, because you taught it, and your teaching stays yours."

**Rejected / Flawed:**
- **⛔ "Extensive PFM market research already gathered" (claimed in-repo; directory empty — E-11).** Not a plan flaw but an integrity hazard: imported as `documented-not-built`. Repair: run the research or delete the claim before Phase 00 opens.
- **⛔ Treating PriceScanner as necessarily-a-LegendaryMoney-feature.** The materials lane serves ReDreamRebuild's audience and the subscriptions lane serves Patternicity's — it is a *capability with three venture channels*, and forcing it into one app forfeits two audiences. Repair: model it as its own Idea (already done in the ledger) and let the channel question stay open.
- **⛔ Plaid-first connector strategy as the default v1 assumption.** The product's whole thesis is *incomplete data handled honestly*; leading with aggregator connectors re-imports the tidy-records worldview (and its breakage/consent problems) before the confidence engine exists to absorb it. Repair: connectors stay Later (as the roadmap already says) — v1 proves the estimate-and-reconcile engine on the messy sources competitors ignore; connectors then *enrich* rather than define the ledger.
