# 02 — Shared Primitives & the Cross-Venture Synergy Matrix (Rethought)

> **RETHINKING-Fable edition** — the portfolio's build-once machinery (fourteen **Primitives**, P-01…P-14) and the compound capabilities that emerge when ventures combine (fifteen **Synergies**, S-01…S-15). Primitives become **Capability nodes** in the KSVGPS graph; synergies become typed inter-venture edge clusters (formalized in [`04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §4.6–4.7). The governing rule from [`00-PORTFOLIO-THESIS.md`](00-PORTFOLIO-THESIS.md): ventures are independent companies connected by an open protocol — so every synergy below names its **payload** (what actually crosses the boundary) and its **consent surface** (who grants it). A synergy that can't name both is a slogan, not a capability.

---

## Part I — The Fourteen Primitives (build once, consume everywhere)

Each primitive lists: what it is, the **canonical home** (which venture builds and owns the reference implementation), **consumers**, and the graph-modeling note. Status tags: 🟢 shipping · 🟡 designed/partial · 🟠 captured-only.

### P-01 · Fact + Interpretations capture model 🟡

One immutable, verbatim **Fact** node per capture (sentence, receipt, photo, reading), with typed **Interpretation edges** to domain records — never dispatched copies (full argument: [`00-PORTFOLIO-THESIS.md`](00-PORTFOLIO-THESIS.md) §4). **Home:** DiviaHome (the Activity Log) defines it; Divia.Network specifies the publication/subscription contract. **Consumers:** every capture surface and every domain app in the portfolio. **Graph note:** `Fact —interpreted-as→ DomainRecord` edges carry the P-02 envelope; corrections re-point edges, never rewrite Facts. **`[DEALBREAKER-HOOK]`:** the v0 protocol contract must be fact-subscription, not copy-dispatch.

### P-02 · The epistemic envelope 🟡

A universal attribute block for derived assertions: `{assertion_type: observed|declared|inferred|estimated|question-mark, confidence, band, provenance[], asserted_by, method, valid_from/to, recorded_at, correction_of?}`. Invented independently three times (LegendaryMoney's ledger, FracRealHomes' scenario bands, DiviaContacts' link-don't-copy) — it is one schema. **Home:** the Divia.AI Enterprise graph core (it is a property of *edges*, so it lives with the graph engine). **Consumers:** all four graphs; ERRATA-class contradictions become native data (single-source assertions, contested alternatives) rather than a side document. **Graph note:** this envelope IS the edge schema — see [`04`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §2.

### P-03 · The universal runway (time-decay priority) 🟠

One primitive: `{resource, predicted_exhaustion_at, escalation_curve, staged_action}` — a deadline that *rots*, escalating priority as exhaustion approaches, with a pre-staged action awaiting approval. Instances already independently described: milk (DiviaHome), Rx/supplement refills (Sattvasic), scheduled outflows and financial runway (LegendaryMoney), spice freshness (spicemaster), waiting-for rot (GTD), **domain renewals (KSVGPS — the CrowdMadness.com cautionary tale)**, warranty/return windows (S-14), QSBS 5-year clocks and filing deadlines (KSVGPS), regulatory comment windows (CrowdMadness). **Home:** DiviaHome/Enterprise shared core. **Consumers:** ten-plus listed. **Graph note:** model as a **Runway node** attached to any resource node; the escalation curve is data, so agents at any cadence can read "how urgent now." The KSVGPS domain-management system and the household milk loop are *the same feature* — build once.

### P-04 · ImportKit (scan-and-import engine) 🟡

Adapters (SMS, CSV/OFX, receipts, lab exports, device dumps, mail archives), dedup, provenance stamping, and unified-record display — the "first unify, then understand" v1 shape shared verbatim by DiviaHome, LegendaryMoney, and Sattvasic, and structurally by aixocode (`scan`/`import`) and Patternicity (corpus ingestion). **Home:** DiviaHome builds the reference; codemap's shared-functionality registry tracks it as the first extraction target into a shared library. **Consumers:** all unify-first ventures. **Graph note:** every imported record's provenance chain terminates in an **ImportBatch node** — auditability of the unified record is what makes later inference trustworthy.

### P-05 · Recurring-agent loop + trust boundary + autonomy ladder 🟡

The scheduled review/improve/suggest cycle with clerk/executive staging and per-task-type autonomy grades (L0→L3), graduation history, and audit lines. **Home:** brain = `aixodev-workgroups` (task definitions, grades, approvals), body = Divia.AI AgentSwarms (execution), face = each product's staging surface. **Consumers:** every venture (the table in [`00`](00-PORTFOLIO-THESIS.md) §2). **Graph note:** **AgentTask nodes** carry `{cadence, autonomy_grade, approval_queue, run_history}`; runs emit **AgentRun nodes** with cost (P-10) and findings edges. The Agent NOC and Divia.Life's gentle "your agents this week" card are two renderings of the same nodes.

### P-06 · Entity resolution service (incl. adversarial mode) 🟡

Mention → durable node resolution with confidence and merge/split history: merchants (LegendaryMoney), foods (TastyPantry), people/companies (DiviaContacts), parcels and comps (FracRealHomes — Bruce's Beach as the canonical exclusion test), world entities at scale (Patternicity), contractors across LLC re-formations (ReDreamRebuild — *adversarial* resolution via `successor-of` detection over Secretary-of-State filings). **Home:** Patternicity builds the at-scale engine; the Enterprise core hosts the personal/org-scale version. **Consumers:** all graphs. **Graph note:** resolution decisions are themselves assertions with envelopes — a merge can be confidence-banded and reversed.

### P-07 · LiveDocument = materialized graph view 🟠

A `.dvai` document defined as `{graph query + template + refresh AgentTask}`, keeping revision history and inline what-changed diffs inside its SQLite container. Instances: the Monday partners' brief, per-portfolio-company dossiers (KSVGPS), per-entity news dossiers (Patternicity), market dossiers (CrowdMadness), per-parcel diligence packets (FracRealHomes), Enterprise "Research Projects" (the B2B beachhead). **Home:** Divia.AI Professional owns the format; Enterprise + Swarm run the refresh. **Graph note:** model the LiveDocument as a node with a `materializes → Query` edge — then "which documents go stale if this subgraph changes" is itself a query (dependency-aware refresh, cheap and correct).

### P-08 · Typed cards, two-tier (DiviaCards) 🟡

The cross-app content vocabulary `DiviaCard::<Producer>::<type>`, split into **Tier 1: declarative cards** (schema + template; safe in any surface including Gmail and email digests; 95% of types) and **Tier 2: sandboxed interactive cards** (capability-manifest, iframe-isolated, signed; the marketplace tier). **Home:** the DiviaCards standard under Divia.AI, with the `divia_cards` Web-Components app as the reference rendering layer (resolving ERRATA E-05 by *role assignment*: the app is the standard's renderer). **Consumers:** all protocol participants; PatternicitySocial is the headline external consumer. **Graph note:** card *types* are nodes (`CardType`), producers/consumers link by `publishes`/`renders` edges — the registry is a subgraph, not a new system.

### P-09 · Identity federation + Agent Credentials 🟠

"One global username" federating home/work servers (OAuth-style; placeholder fields already carried in v1 prototypes) — extended with the **agent authority layer**: a verifiable credential naming an agent's principal, scope, autonomy grade, spend caps, and audit endpoint (did:web + selective disclosure). **Home:** Divia.AI Global (SaaS) as reference IdP — *optional per the open-protocol doctrine* (see the thesis §8 rejection of mandatory portfolio-wide sign-in). **Consumers:** federation (Divia servers), AR storefront trust, agentic commerce (S-06, S-12), cross-org agent negotiation (ExoDev moonshot). **Graph note:** credentials are nodes with `authorizes(scope, grade, expiry)` edges — revocation is an edge close, auditable bitemporally.

### P-10 · Agent cost ledger + effort tiering + secretary supervision 🟡

Every AgentRun records tokens/cost/model-tier; task definitions declare per-step effort tiers (cheap models for mechanical steps, frontier for judgment); a low-cost "secretary seat" supervises expensive seats (progress ledgers, budget circuit-breakers). **Home:** collabs/openhands research → workgroups (the brain records it) + Swarm (the body reports it). **Consumers:** the Agent NOC, household budgets, per-engagement client billing (ExoDev), KSVGPS dreaming budgets. **Graph note:** cost hangs off AgentRun nodes; "what does this recurring insight actually cost per month" becomes a query — the honesty layer for the whole agent economy.

### P-11 · Verifiable receipts (signed proof bundles) 🟠

ed25519-signed, content-addressed bundles proving *what was delivered/decided/observed, when, by whom*. Instances: Engagement Receipts (ExoDev — the origin), graduation certificates, **LP reporting snapshots (KSVGPS)**, co-ownership governance votes and reserve disbursements (FracRealHomes), independent-oversight milestone sign-offs (ReDreamRebuild — the friend-checks-the-roof formalized), market resolutions with evidence chains (CrowdMadness). **Home:** ExoDev/AIXO builds it; portfolio-wide library. **Graph note:** a Receipt node signs a *subgraph snapshot* — the graph and the receipt system are one design (content-addressed subgraph hashes).

### P-12 · The correction store (learning loop) 🟡

Human confirm/correct/reject events as first-class, queryable data that agents mine to sharpen per-user priors — and the substrate for "review-the-reviewer" (the agent reports its own precision and recalibrates). **Home:** the Enterprise core (corrections are edges on Interpretations). **Consumers:** every inference surface; NEAR-term it also feeds per-user local adapters ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §4). **Graph note:** `Correction —supersedes→ Interpretation` edges; precision metrics are aggregates over them. **The moat framing:** competitors can copy features; they cannot copy years of a user's accumulated corrections.

### P-13 · Embedding-based conceptual routing (the Sorting Hat) 🟠

Every Layer-A Idea/Topic node carries an embedding; new captures/ideas auto-cluster to the nearest venture/topic ("parse my Zillow emails" lands in FracRealHomes; OSHA report-cards land in ReDreamRebuild) — John's "conceptual clustering akin to vector-search embeddings" made literal. **Home:** KSVGPS (Module 1 routing); the same mechanism scoped down routes captures inside the personal graph. **Consumers:** KSVGPS triage, the Sorting-Hat matrix, DiviaHome capture routing, DiviaContacts email→entity suggestions. **Graph note:** ship vector indices beside graph indices from v1 ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §3); nightly link-prediction proposals are `question-mark` edges awaiting GP confirmation — **ideation as a graph operation**.

### P-14 · Regulatory radar 🟠

A recurring agent watching statutes, agency actions, and case law per jurisdiction, diffing against a venture's compliance posture, and staging required-change proposals. **Home:** CrowdMadness (its feasibility case *is* this primitive). **Consumers:** CrowdMadness (gambling/prize/CFTC per state), FracRealHomes (securities-adjacent co-ownership structures, RE licensing), Sattvasic (FDA general-wellness boundary, HIPAA adjacency), LegendaryMoney (financial-data rules), PatternicitySocial (platform/content law), KSVGPS (QSBS, Series-LLC recognition — R-009/R-010). **Graph note:** jurisdictions, rules, and venture-compliance-postures are nodes; a rule change is an Event node whose edges identify every affected venture *automatically* — the portfolio-wide blast-radius query. **Spin-out option:** this is a sellable RegTech data product once proven internally (see [`03`](03-IDEAS-LEDGER.md) P-idea 14).

---

## Part II — The Synergy Matrix

Compact index of the load-bearing inter-venture links; each cell names the synergy deep-dive and the payload. (Formal edges: [`04`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §4.6.)

| Producer ↓ / Consumer → | payload | via | deep-dive |
|---|---|---|---|
| Patternicity → KSVGPS | world events touching portfolio companies/ideas | world-graph query, firm-scoped | S-03 |
| Patternicity → CrowdMadness | question sourcing + resolution evidence chains | world-graph query + credibility engine | S-04 |
| Patternicity → LegendaryMoney | merchant entities, recalls, price-context news | entity feed (consented) | S-03 |
| Patternicity → Divia agents | the "memory layer" (current-events context) | MCP connector | S-03 |
| CrowdMadness → Patternicity | crowd-forecast priors on world events | data product | S-04 |
| CrowdMadness → portfolio | regulatory radar as shared capability | P-14 | S-05 |
| LegendaryMoney → FracRealHomes | purchase flows, operating-cost accounting, tax handling | Divia protocol delegation | S-12 |
| LegendaryMoney ↔ TastyPantry ↔ Sattvasic | the fan-out interpretations of one Fact | P-01 over Divia.Network | S-01 |
| TastyPantry → Sattvasic | what-was-eaten detail for macros | interpretation subscription | S-08 |
| TastyPantry ↔ spicemaster | shared inventory substrate (spices as category) | shared schema, separate deployments | S-08 |
| Sattvasic ↔ TastyPal | BLE-scale + food-ID tech, two brand surfaces | white-label | S-08 |
| Sattvasic + spicemaster + CGM → meal planning | flavor-forward, glycemic-aware "cook tonight" | cross-domain query (consented) | S-08 |
| ReDreamRebuild ↔ FracRealHomes | renovation-ROI ↔ valuation engine; shared RE audience | data + content cross-links | S-07 |
| ReDreamRebuild → DiviaHome | contractor safety data for home-maintenance vendor choice | lookup API | S-07 |
| 3D-capture → FracRealHomes AVM | rights-clean geometry/sightlines | internal Build-Line hand-off | S-07 |
| PriceScanner ↔ ReDreamRebuild | materials price-tier hunting (the 5-Lowe's story, automated) | SKU/price feed | S-06 |
| DiviaContacts ↔ Divia.Life ↔ Patternicity | relationship cadence + world events about *your* people | local resolution against PKMS | S-09 |
| aixocode archive → AIXO Ontology → codemap | mined sessions → team knowledge, reuse registry | internal | S-10 |
| ExoDev receipts → KSVGPS / FracRealHomes / ReDreamRebuild / CrowdMadness | verifiable-proof primitive | P-11 | S-11 |
| KSVGPS ↔ CrowdMadness | internal milestone prediction markets (dogfood) | play-money engine, firm-internal | S-13 |
| DiviaHome ↔ everything | Facts, runways, the nightly packet, the Morning Briefing | P-01/P-03/fan-in | S-01/S-02/S-15 |

## Part III — Synergy deep-dives

### S-01 · The fan-out, upgraded to interpretations
One Fact, many interpretation subscriptions (P-01) — the canonical dinner sentence plus its inverse, ambient fusion: GPS place-visit + card charge + kitchen-device utterance fuse into *one* high-confidence Fact instead of three weak ones, with the agent asking a human only when sources disagree. **Payload:** typed interpretations. **Consent:** per-app subscription grants, per-domain auto-confirm thresholds. **New here:** fusion is an interpretation-of-interpretations — the graph model handles it without new machinery.

### S-02 · The universal runway across every domain
P-03 instantiated portfolio-wide, with the unifying observation that **KSVGPS domain-renewal management and DiviaHome milk replenishment are the same primitive** — one escalation engine, one staging surface, domains from groceries to QSBS clocks. **Proposed extension:** a *portfolio runway dashboard* in KSVGPS — every rotting deadline across every venture (renewals, filings, comment windows, warranty expirations on firm assets) in one prioritized view; the GP version of the household's morning packet.

### S-03 · Patternicity as the portfolio's external sensor
The world graph answers "what happened outside that touches what we hold inside" for every other graph: portfolio-company news → the Monday partners' brief (KSVGPS); merchant recalls/price events → ledger annotations (LegendaryMoney); drug/supplement research and recalls → health-record flags (Sattvasic); permit filings, zoning changes, disaster events → parcel-risk updates (FracRealHomes); OSHA enforcement news → contractor report-card refreshes (ReDreamRebuild). **Payload:** entity-keyed event feeds, scoped to the subscriber's own entity list — the subscriber sends *watch-lists*, Patternicity returns events; personal/firm data never flows outward. **This is the strongest argument for the entity-graph-as-product:** every sibling venture is a design-partner customer of "Patternicity World Knowledge" before a single external client signs.

### S-04 · Prediction markets fused with the world graph
Three mutually-reinforcing loops: (1) **question sourcing** — market-worthy questions generated from graph events ("will the FTC block X?"); (2) **resolution with evidence** — markets settle against the world graph with WeighTheFacts-style evidence chains attached (an auditable oracle — a genuine differentiator vs. resolution disputes plaguing incumbents), sealed as P-11 receipts; (3) **forecast-enriched knowledge** — crowd priors flow back as a Patternicity data-product layer ("the crowd puts 73% on this outcome"). Plus the embedded-market surface: PatternicityNews articles carry their own live market card (`DiviaCard::CrowdMadness::market`) — the "CNN Predictions" white-label concept **dogfooded on the portfolio's own news property first**.

### S-05 · The regulatory radar as shared infrastructure → RegTech option
P-14 built once for CrowdMadness, subscribed by five-plus ventures, each maintaining a compliance-posture subgraph the radar diffs against. The nightly required-change proposal lands as a staged PR-like object (hybrid-engine typed steps; deterministic gates for the geofence/config changes; human approval — L2). Once proven on the portfolio, the radar's jurisdiction-rule graph is a **sellable data product** to other regulated startups — the "LLM-economics inversion" packaged.

### S-06 · PriceScanner generalized: the best-value engine
The grocery price-matcher is one instance of a general capability: **full-spectrum price/quality visibility before purchase** — which is *literally the ReDreamRebuild teaching methodology* ("see the $6 tier so you choose the $2.99 tier intelligently") in software form. Lanes: groceries (v1); **materials** (flooring/counters/fixtures across regional big-box + specialty stores, including clearance/discontinued-stock hunting — John's 5-Lowe's odyssey automated as a standing agent watch); **recurring services and subscriptions** (the ledger already sees every recurring charge — surface cheaper equivalents; this lane is also the *repaired* Patternicity ONE, see [`03`](03-IDEAS-LEDGER.md) R-01). **Consent/trust:** watch-lists and staged buy-proposals under P-09 spend caps; the agent never buys ungated.

### S-07 · The remodel stack (ReDreamRebuild × FracRealHomes × 3D × money)
The compound product John's own $150K→$910K story implies: (1) **Renovation-ROI Estimator** — EstimatePacket machinery pointed at *improvement* decisions (current value → post-reno bands by material tier, with the informed-choice delta made visible); (2) **before/after 3D captures** as evidence and marketing (and as valuation-engine training data); (3) **contractor selection** informed by safety report-cards and successor-entity detection (P-06 adversarial); (4) **independent-oversight receipts** — milestone sign-offs by a third-party reviewer, signed (P-11), creating the paper trail that turned John's 300 photos into a settlement; (5) **budget runway** for the project in LegendaryMoney (informal project account, reserve tracking); (6) **materials hunting** via S-06. Same audience at adjacent moments (value → improve → sell), so the two ventures cross-link content and data without corporate fusion.

### S-08 · Kitchen intelligence (the full food loop)
TastyPantry (what's on hand) + spicemaster (flavor space + taste fingerprint) + Sattvasic (macros, CGM) + LegendaryMoney (spendable tonight) + Divia.Life Agenda (time before next event) jointly answer the compound question *"I'm hungry — what are my options?"* with answers ranked by feasibility (inventory), taste (fingerprint + adventurousness), health (glycemic response history — the personalized-nutrition claim made concrete), budget, and time. **Design decisions embedded:** the shared inventory substrate is a shared *schema* consumed by separate deployments (companies stay separate; a household's single instance is a deployment choice); palate data comes *implicitly from logs* (exposure-gap vs. genuine-dislike detected from what was actually eaten — never a quiz); the pantry itself becomes a **confidence-aware ledger of atoms** — estimated inventory with bands, decremented by consumption priors, reconciled at receipt-scan "anchors" exactly as LegendaryMoney reconciles balances (P-02 reuse, and the repair for TastyPantry's manual-logging fragility).

### S-09 · Relationship intelligence with a privacy-correct join
DiviaContacts (org relationships), Divia.Life Friends & Family (personal feeds), and Patternicity (world events) combine into "your friend's company just raised; you haven't spoken in three weeks; here's a drafted congratulation-reconnection" — with the join done **locally**: the world graph publishes public events; resolution against *your* contacts happens inside *your* PKMS; nothing about who you know leaves your infrastructure. The consumer twin of the FDSE "we've seen this pattern" moat, built without a data honeypot.

### S-10 · Mining the development record
The lossless session archive × entity extraction (P-06) × codemap's structural graph yields: a **living team-knowledge graph** ("what do we collectively know about dependency X; who last touched this subsystem and what did they learn"); **steering-intervention analytics** (which human interventions in CollabPairs measurably improve outcomes — mineable only because capture is lossless); **SOUL.md growth curves** (agent capability trajectories as data); and the reuse-vs-reimplement stewardship agent fed by the shared-functionality registry. This is the AIXO Ontology's content strategy: the archive is the corpus, the graph is the index, the agents are the librarians.

### S-11 · Verifiable receipts everywhere (P-11 instances)
One signing library, five products: engagement receipts + graduation certificates (ExoDev), LP snapshots (KSVGPS — quarterly reports become continuously-verifiable), co-ownership votes/disbursements (FracRealHomes — governance travels with the share at resale, directly attacking the Pacaso liquidity trap's information asymmetry), oversight sign-offs (ReDreamRebuild), market resolutions (CrowdMadness). Receipts sign content-addressed subgraph snapshots, so the graph engine and receipt system co-design.

### S-12 · Fractional-ownership operations on money rails
FracRealHomes delegates money mechanics to LegendaryMoney over the protocol: co-owner expense splits are **informal-accounts** ("co-owner #3 owes the reserve fund" = "money Mom owes me," scaled); reserve funds are runway objects (P-03) with contribution escalation; purchase flows and tax handling ride the delegated services. The marketplace stays a real-estate company; the fintech stays a fintech; the protocol carries the seam — the portfolio's cleanest worked example of *composition without merger*.

### S-13 · The venture graph that ideates (KSVGPS dreaming)
Nightly: (1) embed and cluster all new captures (P-13); (2) run link prediction + community detection (Leiden — imported from codemap's stack, a direct AIXO→KSVGPS tech transfer) proposing `question-mark` edges ("this new tariff Event shortens the path to Idea X"; "these two Ideas share an unbuilt dependency — a shared library candidate"); (3) re-evaluate dated Triangulation Targets against tracked Events (the feasibility radar — the MobThought-reboot detector); (4) stage everything for GP confirmation — dreaming proposes, humans dispose, confirmed edges compound. **Plus the dogfood market:** GPs stake play-money on venture milestones via the CrowdMadness engine (firm-internal); calibration history becomes a decision-quality asset and the market engine's first live deployment.

### S-14 · The durables lane (home inventory, warranties, insurance)
A third interpretation lane for receipts (beyond expense and pantry): durable goods create **Possession nodes** in the household graph — warranty runways (P-03), return-window countdowns, manuals auto-fetched, and a continuously-current **home inventory** that serves insurance documentation, the remodel stack (S-07 — what's in the house pre/post), and FracRealHomes turnkey-furnishing valuation. Nobody catalogs their house; the receipt stream does it implicitly — discover-and-suggest applied to *stuff*.

### S-15 · The Morning Briefing (fan-in)
The reverse of S-01: one human-paced digest assembled from every subscribed source — GTD packet deltas, household runways, ledger anomalies, health flags, world events on your watch-list, agent-fleet status — rendered as one DiviaCard stack on the Enterprise homepage (corporate), in Divia.Life (personal), and spoken by the kitchen device (household). One fan-in pipeline, three audience skins; every item deep-links to its staging surface so the briefing is also the approval queue. The daily heartbeat that makes the whole ecosystem *felt*.

## Part IV — Rejected / Flawed (synergy-level)

- **⛔ "Everything integrates with everything."** Undisciplined integration is a tax: each edge adds protocol surface, consent complexity, and failure modes. **Repair:** an integration ships only when it names payload + consent surface + a user story it serves (every S-item above does); all else stays a Layer-A idea. spicemaster3000's zero-integration purity is a *feature* (spin-out cleanliness) — wire it via protocol subscriptions only, never shared infrastructure.
- **⛔ The shared inventory substrate as a shared database.** Tempting reading of the TastyPantry↔spicemaster convergence; wrong — separate companies, separate deployments. **Repair:** shared *schema + card types*; a single household instance is a deployment choice, not an architecture.
- **⛔ Multi-LLM "AI-council" review as a default quality gate.** The portfolio's own research says tests arbitrate better than rhetoric, and council rituals burn tokens on theater. **Repair:** deterministic gates first (hybrid engine), single adversarial verifier second, full councils reserved for irreversible/judgment-heavy decisions ([DEALBREAKER-HOOK]-class choices) — and store *that* policy as a dated finding like N=2 (see [`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §11).
- **⛔ The convergence-diff KPI (KingStrat's shrinking `main..kingstrat-main` delta as the product-generalization metric).** Diff size is gameable and confounded — a legitimately growing client feature-set grows the delta while convergence proceeds. **Repair:** measure *graduated-feature count* and *reuse rate* via codemap's registry (Independent Implementation Rate falling = real convergence); keep the shrinking-diff as narrative color only.
