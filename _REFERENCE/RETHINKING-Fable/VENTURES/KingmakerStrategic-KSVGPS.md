# Venture Dossier — Kingmaker Strategic / KSVGPS (Rethought)

> The PE/VC firm (**Kingmaker Strategic Venture Partners LLC**, "KingStratVC") that is a **customer, not a vendor** — and its product, **KingStrat AdVentureGPS (KSVGPS)**: the venture-studio operating system, the first real Divia.AI Enterprise client install, and the destination graph this entire corpus imports into. Upgraded identity: not an intranet — a **feasibility radar** ([`../00-PORTFOLIO-THESIS.md`](../00-PORTFOLIO-THESIS.md) §6).

## 1. The three modules over the decade-scale idea-arc

- **Module 1 — GP Strategic Landscape & Ideation** (the ~3–5 GPs): the pre-incorporation layer where ideas live from the moment John thinks of them, often nameless for years; Layer-A Ideas/Topics + research + the nightly dreaming runs. **The persistent home across the whole arc.**
- **Module 2 — Venture Studio Operations Center** (an active venture's board + C-level): investor↔C-level strategy and initiatives, replacing meetings/email/Excel/PowerPoint; ≈ incorporation→dissolution. On pause/dissolution the idea **returns to Module 1** (MobThought: operational 2004–08 → shelved → rebooted as CrowdMadness 2026 — the lifecycle's proof case).
- **Module 3 — LP Dashboard** (investors, several also expert-advisors): real-time transparency replacing the 90-day quarterly report; AI-accelerated venture lifecycles make quarterly cadence structurally misaligned. Upgrade: LP snapshots as **signed receipts (P-11)** — continuously *verifiable* reporting, not just continuous reporting.

ACL scoping is the load-bearing requirement that forces the two-layer split: a researcher gets Layer A only; GPs get both; LPs get Module 3 projections. Not expressible unless Idea and Venture are separate entities — the canon's hardest constraint, honored in [`../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md).

## 2. The venture-studio corporate blueprint (canon)

Kingmaker Strategic Ventures LLC (the operating firm) → a **Texas Series-LLC fund** ("KingStrat V.Studio Fund IV", name TBD) spinning up cheap per-venture **sub-LLCs** (PatternicityNews LLC, FracRealHomes LLC, TastyPal LLC; exceptions like ExoDev.Pro incorporate straight to a corporation for branding) → at maturity, **reincorporation as a Delaware C-corp**, starting the **IRS §1202 QSBS clock** (5-year hold → up to $50M gain exclusion post-2025). Open legal questions gated by R-009 (Series-LLC cross-state recognition) and R-010 (§1202 mechanics/stacking). Ownership across ventures is an **overlapping-Venn of LP stakes — never corporate siblinghood** (the doctrine).

**KSVGPS as the outsourced support department:** shared legal/finance/marketing/**IP-asset** systems so earliest-stage teams defer support hires past ~10 FTEs. The **IP-asset repository** (domains, trademarks, names) assigns IP to a startup at incorporation and **reclaims it at pause/closure**, managed in perpetuity until GPs consciously discard — with every renewal a P-03 runway (the CrowdMadness.com loss is the founding cautionary tale). LegalEvents (formation, reincorporation, assignment, reclaim) are first-class dated nodes; QSBS clocks hang off them.

## 3. What KSVGPS v1 actually is (the build this week)

The graph-DB realization of the two-layer model, per [`../04`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md): epistemic-envelope edges (hook #10), bitemporality (hook #11), question-mark decision groups, vector index beside the graph (hook #14), Event/Trend/Thesis nodes promoted to v1, this corpus as the seed import. Engine lineage: `diviahome-web → proto-divia_ai-enterprise` (Python/Flask), succession-no-merge toward the Rust Enterprise server later; KingStrat's real firm data is the acceptance test ("optimize once; business data doubles as the validation set").

**The four capabilities that justify it, in shipping order:**
1. **The import + Sorting Hat (P-13):** every capture embeds, clusters to its nearest Idea/Topic/venture, and lands placed rather than lost — "hundreds of ideas a day" becomes capture-and-place.
2. **The portfolio runway dashboard (S-02):** every rotting deadline (renewals, filings, windows, clocks) in one escalating view; pays for itself on the first prevented domain loss.
3. **The Monday partners' brief + LiveDocument dossiers (P-07):** agent-swept news/filings/funding across portfolio and pipeline, dependency-aware refresh, evidence-linked via the Patternicity watch-list service (S-03).
4. **The nightly dreaming (S-13):** embedding + link prediction + community detection proposing question-mark edges; dated Triangulation Targets re-evaluated against tracked Events — the engine that would have flagged the MobThought reboot in 2018 instead of 2026.

## 4. Ideation & Exploration

**Existing (carried):** the Monday partners' brief · per-portfolio-company LiveDocument dossiers · dealflow-as-pipeline cards with agent-suggested next actions · the graduated-features convergence discipline (build freely in the client fork; graduate general infrastructure down into the product) · the reference-case-study GTM ("a PE/VC firm's entire deal-flow intranet on Enterprise") · VTL/GPS framing (Signal Inception / Signal Node / Trajectory Node).

**Proposed (new this rethink):**
- **Internal milestone prediction markets (S-13):** GPs stake play-money on venture milestones via the CrowdMadness engine — calibration history as a firm decision-asset and the market engine's zero-regulatory-surface first deployment.
- **The blast-radius query:** any Event/Rule change → every affected venture/idea/target automatically (the P-14 subgraph joined to the landscape) — the GP's "what does this news mean for us" answered structurally.
- **Signed LP reporting (P-11)** and **signed IP-assignment events** — the studio's paper trail as verifiable receipts.
- **Advisor-graph activation:** People nodes with time-bounded roles (the MobThought bench: Brand, McHenry, Forster) queryable for re-engagement when a related idea reactivates — institutional relationships that survive venture pauses.
- **Dreaming-as-a-service (far):** the ideation engine offered to other studios/PE firms once Enterprise is GA — hold as a dated far target.
- **Question-mark hygiene as a weekly ritual:** the open-decision queue (§4.8 of the catalog) surfaced to John on a cadence, oldest-first, so modeled alternatives converge instead of accumulating.

**Rejected / Flawed:**
- **⛔ The shrinking client-fork diff as the convergence KPI** — gameable, confounded (R-09). Repair: graduated-feature count + falling Independent-Implementation-Rate via codemap's registry.
- **⛔ KSVGPS as "a PE/VC CRM."** The CRM slice is the easy 20–40%; building toward it first optimizes the least-differentiated surface. Repair: the venture-studio OS + feasibility radar is the product; CRM views are projections over the graph, added late and cheaply.
- **⛔ Deferring Event/Thesis nodes to a later schema phase (as the canon's v0.5 bootstrap did).** Correct for the markdown era, wrong for the DB: the dreaming engine and blast-radius query — the reasons to build KSVGPS at all — are inert without them. Repair: ship sparse-but-present in v1 (already promoted in [`../04`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §1.1).
- **⛔ Unbounded "buy every name" (R-13).** Repair: scored wishlist + annual conscious keep/drop review, with runways doing the watching; the purchase decision stays John's.
