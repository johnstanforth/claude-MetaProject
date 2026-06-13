# Product — LegendaryMoney

> An AI personal-finance manager built for **messy, incomplete, real-world money** — "Quicken for the
> rest of us." A confidence-aware ledger that estimates rather than abstains, captures in natural
> language, and reconciles from anchors.

- **Names:** "LegendaryMoney" · repo/dir `legendarymoney-web` · steward **LegendaryMoney LLC** (Peoria, AZ). Venture detail in [`../../VENTURES/LegendaryMoney.md`](../../VENTURES/LegendaryMoney.md).
- **License:** **Dual AGPLv3 + Commercial (CLA-based)** — explicit.
- **Status:** 🟠 Phase 00 pending; docs-only (a polished ~30KB README), zero code. Python 3.12+ · Flask · SQLite→Postgres.

---

## What it is (consensus)
A standalone, self-hosted **PFM that embraces incomplete data** — "the opposite of finance software built for tidy complete records." Core mechanics:
- **Natural-language capture:** "I had El Pollo Loco for dinner" → an inferred transaction (merchant, category, **estimated amount + confidence band**).
- **Balance assertions** as first-class data ("I have $23 in my wallet" vs last week's "$36") reconciled by **balance-gap differencing** that generates estimated plug entries.
- Every transaction carries a **precision level** (confirmed / inferred / estimated) + confidence band + provenance — *without the user ever touching a debit/credit column.*
- **Cash/wallet and informal accounts** (money Mom owes me; a roommate split; a trip fund) are first-class.

Six proposed domains: Accounts & Balances, Transactions, Activity Log (lossless NL money inbox), the **Inference & Estimation Engine** (the distinctive heart), forgiving Budgets/Goals/Insights ("remaining financial runway"), and Scan-and-Import. **v1 = scan-and-import / data unification** (deep NL AI is explicitly out of scope for v1); **v2 = understand & infer** + publishing **LegendaryMoney-namespaced DiviaCards** to the global registry. Motto: *"first unify, then understand."*

### Cross-product role
A standalone brand that **also participates in Divia.Network** ("own finance-native models internally; DiviaCards as the public contract"). The "expense" node of the fan-out (see [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md)); carries placeholder global-identity fields.

> ⚠️ ERRATA: the recurring-agent "ledger reviewer" (LATER-002) and the "extensive PFM research already gathered" claim are **not in the repo** (its `_research/` is empty). See [`../../ERRATA.md` E-11/E-12`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** an 8-principle creed (accessible-not-accounting; incomplete-by-default; confidence-over-false-precision; estimate-don't-abstain; capture-losslessly; reconcile-from-anchors; meet-in-natural-language; **no-shame-no-audit-voice**); a learning loop (corrections sharpen priors); bank/card/payment-app connectors (Plaid-style or direct) over the import-adapter architecture; separate mobile-capture apps feeding the household server; the "remaining financial runway" view; the compound cross-app query "what are my options for dinner?" (TastyPantry food + LegendaryMoney spendable).
- ✦ **New:** the **recurring ledger-review agent** (LATER-002 §6) — nightly/weekly anomaly surfacing, balance-assertion drift, recurring-charge changes, **learning categorization rules from observed corrections instead of asking the user to configure them**. ✦ Make **confidence bands a visible product aesthetic** (the screenshot-selling differentiator), turning "incomplete data" from an apology into the brand. ✦ Lead with **"financial runway"** (how many days can I coast?) as the anxiety-reducer — the emotional opposite of guilt-driven budgeting. ✦ The founder pedigree ("the people who built the internet-banking platform your bank runs on, now building the anti-Quicken") is the wedge.
