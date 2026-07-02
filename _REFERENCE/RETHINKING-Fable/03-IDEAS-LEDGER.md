# 03 — The Ideas Ledger (Rethought & Expanded)

> **RETHINKING-Fable edition** — the full Layer-A ledger, superseding the 61-node `IDEAS/` tree and the 24-node `TOPICS/` taxonomy with one consolidated, expanded document. Every entry is a **Layer-A Idea node** (durable, brand-free, non-owning M2M edges to Topics and Ventures per [`STRATEGIC-LANDSCAPE-MODEL.md`](../STRATEGIC-LANDSCAPE-MODEL.md)). Tags: **[E]** existing (carried forward, restated and upgraded) · **[P]** proposed (new in this rethink) · rejected/flawed items live in the closing register (§R). Shared machinery is *not* duplicated here — capability-shaped ideas reference their primitive (P-01…P-14) in [`02-SHARED-PRIMITIVES-AND-SYNERGY-MATRIX.md`](02-SHARED-PRIMITIVES-AND-SYNERGY-MATRIX.md). Graph import: each `####` heading is one Idea node; edges named inline land in [`04`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §4.

## 0. Topic taxonomy — revisions

Carry the 24 existing Topics forward unchanged, plus **three additions** the corpus outgrew:

- **[P] Renovation & Home Improvement** — ReDreamRebuild's cluster currently has no Topic node (it postdates the taxonomy). Ideas: renovation education content, contractor safety report-cards, renovation-ROI estimation, independent oversight. Adjacent to Real Estate (deliberately separate — improve-a-home vs. value/own-a-home audiences overlap but the ideas cluster distinctly).
- **[P] Regulatory & Compliance Technology** — the regulatory-radar family (P-14) spans five-plus ventures and has no home Topic; without it, compliance ideas mis-cluster under whichever venture first needed them.
- **[P] Trust & Verification Infrastructure** — verifiable receipts (P-11), agent credentials (P-09), credibility scoring, auditable oracles. The portfolio's most distinctive emerging cluster; currently invisible because its instances hide inside six different ventures.

---

## 1. Knowledge Graph & Entity Modeling

#### [E] Graph-DB entity-knowledge engine
One optimized home for the portfolio's core knowledge machinery — every other product a **client, not a copy**. Channel: Divia.AI Enterprise (prototype `proto-divia_ai-enterprise` → Rust). Upgraded framing: the engine's spec is now concrete — typed nodes, **epistemic-envelope edges (P-02), bitemporality, vector+graph+FTS hybrid indices** ([`04`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) is its requirements document). KingStrat's real data remains the acceptance test.

#### [E] Software-dev knowledgebase / Ontology graph
The team's entire dev reality as one queryable graph (AIXO.Dev; the engineering peer of KSVGPS, overlapping at `Company → Product`). `depends-on` → lossless archive; `enables` → codemap. Bitemporal seams are the `[DEALBREAKER-HOOK]`.

#### [E] Source-code analysis / cross-project codemap
Structural + semantic + cross-project comparison; feeds the shared-functionality registry. Upgraded role: its Leiden/community stack is a **direct tech transfer to KSVGPS dreaming** (S-13), and its registry is the metric source that replaces the rejected convergence-diff KPI (§R-09).

#### [E] NER-at-scale entity intelligence
The B2B entity-graph product, distinct from the consumer news portal. Now subsumed as the engine inside **Patternicity World Knowledge** (confirmed a sellable line) — see [P] world-knowledge watch-list service below for its concrete v1.

#### [E] Scan-and-import data unification
"First unify, then understand" — the portfolio's signature v1 shape. Now formalized as **ImportKit (P-04)**; DiviaHome builds the reference, LegendaryMoney/Sattvasic consume, codemap tracks extraction.

#### [E] AI contacts / relationship manager (CRM-in-the-inbox)
Thin Gmail renderer over the PKMS; org task graph as the moat; Streak/Copper model. Research complete (16 tracks). `enables` → capture-to-Activity-Log; extended by S-09 relationship intelligence.

#### [E] Venture-studio operating system
KSVGPS: three modules over the decade-scale idea-arc. Upgraded identity: not an intranet — a **feasibility radar** ([`00`](00-PORTFOLIO-THESIS.md) §6) whose nightly dreaming is link-prediction over the landscape (S-13).

#### [E] Chain-of-thought argument & credibility builder (WeighTheFacts)
Upgraded from side-product to **infrastructure**: the per-source/per-claim credibility engine the world graph *requires* as its immune system against adversarial content ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §8), exposed secondarily as a consumer discernment surface and evidence-chain supplier to market resolution (S-04).

#### [E] News portal over a world-knowledge graph
PatternicityNews — the entity-graph as the news explorer; the venture's entry point and promotion surface. Open v1 fork (aggregator vs. analysis vs. graph-explorer) remains John's call; the graph-explorer differentiator is what nothing else offers.

#### [P] World-knowledge watch-list service — *the concrete v1 of "Patternicity World Knowledge"*
Subscribers register entity watch-lists (portfolio companies, merchants, drugs, parcels, contractors); the service returns entity-keyed event feeds with credibility scores and evidence links. Privacy-correct by construction (watch-lists in, events out — see S-03). First five customers are sibling ventures; the B2B product is the same API with billing. Topic: knowledge-graph + news-media. `depends-on` → world graph, credibility engine. **This, not a dashboard, is the sellable unit.**

#### [P] Cross-domain correlation service (statistical-honesty edition)
The correlation engine relocated to where it belongs — *across* the whole personal graph (money × sleep × food × calendar-load), not inside one health app — with multiple-hypothesis discipline, effect sizes, and hypothesis-not-diagnosis framing (thesis §5). Channel: Enterprise/DiviaHome core; Sattvasic renders the health view. `depends-on` → P-01, P-02, P-12.

#### [P] Team knowledge graph from session mining
The lossless archive × entity extraction × codemap structure = "what does this team collectively know about X" (S-10). Channel: AIXO Ontology. Distinct customer-value from the archive itself (knowledge retrieval vs. preservation).

#### [P] Steering-intervention analytics (collaboration science)
Mine CollabPair transcripts for which human interventions measurably improve agent outcomes; publishable research and a product tier ("what steering works, for your team, from your own data"). Only possible because capture is lossless — a moat-demonstrating product. Channel: AIXO analytics.

## 2. AI Agents & Orchestration

#### [E] Agent-hosting & orchestration server
Swarm — containerized autonomous agents, the ecosystem "body." Phase-00 competitive dive vs. the OpenClaw family; differentiation axes = recurring scheduled tasks + ecosystem integration. Resident-vs-ephemeral resolves to *ephemeral execution + durable externalized memory* ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §1).

#### [E] Recurring autonomous-agent tasks
The one capability, many domains (LATER-002). Now formalized as P-05 with the autonomy ladder and AgentTask/AgentRun graph modeling; every per-domain "reviewer" idea below is an instance, not a separate build.

#### [E] Cross-vendor agent collaboration bus
Typed envelopes, engine-owned FSM, append-only log; owns only the cross-vendor bridge. Laptop CollabPair shipping; server engine designed. Findings (tests-arbitrate; cost-is-existential) carried as dated, regime-conditional assertions (§R-08).

#### [E] Multi-agent dev-team coordination ("Asana for agents")
Workgroups — claim/lock/hand-off/dependency task queue; the "brain"; home of the autonomy ladder and the SOMEDAY task market.

#### [E] Hybrid deterministic + LLM workflow engine
Typed steps, code-enforced gates, per-step effort tiers. Upgraded confidence: this is where the industry converged — build it; the moat is the encoded-workflow *library*, not the engine ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §7).

#### [E] Context-preserving search
Disposable-context search returning only distilled hits; orchestrator-context preservation. Still correct; candidate homes unchanged (skill / aixocode feature / workflow doc).

#### [E] Personal "life OS" / GTD weekly-review system
Divia.Life surfaces + the agent-prepared review packet; clerk/executive boundary; L0/L1 deliberately.

#### [P] Agent NOC (operations center for the agent fleet)
Promoted from scattered ✦ ideation to a first-class Idea: every recurring task across the org — last run, findings, approvals pending, cost (P-10), autonomy grade, precision history (P-12) — as an `aixodev-web` dashboard with Divia.Life's "your agents this week" card as its consumer twin. The sellable ops layer for client agent fleets.

#### [P] Agent Credentials standard
Verifiable agent authority: principal, scope, autonomy grade, spend caps, audit endpoint (P-09; [`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §6). Channel: Divia.AI Global + AIXO jointly; a standards land-grab with NEAR-term participation value. `enables` → agentic commerce, cross-org negotiation, the replenishment L3 endgame.

#### [P] Morning Briefing fan-in engine
The S-15 digest pipeline as its own Idea (distinct customer-value: *one calm daily surface* vs. the per-app staging queues). Channel: Enterprise (corporate skin) + Divia.Life (personal) + kitchen device (spoken).

#### [P] LiveDocument dependency-aware refresh
P-07's enabling insight as a buildable unit: documents declare `materializes → Query`; the graph knows which documents a change staleness-touches; refresh becomes event-driven instead of scheduled. Channel: Pro (format) + Enterprise (engine). `[DEALBREAKER-HOOK]`: the `.dvai` container must store the query alongside the content.

## 3. Structured Documents, Cards & Interchange

#### [E] Cross-app typed-card interchange standard & registry (DiviaCards)
Namespaced `Producer::type` vocabulary. Upgraded with the **two-tier split** (declarative vs. sandboxed-interactive — §R-04 repair); the `divia_cards` app is assigned the *rendering-layer* role (resolving E-05 by decision rather than deferral).

#### [E] Structured-knowledge document format (`.dvai` / LiveDocument)
Outline-of-cards in SQLite, revision history inside the container; LiveDocument mode per P-07.

#### [E] Design-token management system (DB-as-source-of-truth)
Round-trip DESIGN.md ⇄ DTCG; the portfolio's design layer; standalone-open-tool wedge candidate. Unchanged and healthy.

#### [E] Household "home OS" (Activity-Log / task / calendar / document hub)
DiviaHome — the ecosystem anchor and Enterprise's Python ancestor; v1 = unification; gates the commercial server line.

#### [E] Cross-app integration standard (fan-out / fan-in bus)
Divia.Network — upgraded to **fact-publication + interpretation-subscription semantics** (P-01; §R-16). The open-protocol doctrine (tech-clients, not siblings) is its governance model. The A6 name overload (integration layer vs. tutorials site) stays deferred to graph migration — model both as alternatives.

#### [P] The durables lane (home inventory / warranty / insurance)
S-14 as an Idea node: receipts → Possession nodes → warranty/return runways, manuals, insurance-grade inventory. Channels: DiviaHome (household record) with LegendaryMoney (purchase link) and FracRealHomes (turnkey valuation) as consumers. Nobody will ever catalog their house by hand; the receipt stream does it implicitly.

#### [P] ImportKit as a shared library (possibly OSS)
P-04 extracted: adapters + dedup + provenance as a published library — an AGPL/community wedge that seeds the protocol (every ImportKit adopter emits protocol-shaped Facts). The Scalara/RosettaMQ "encapsulate shared functionality" principle applied to the current portfolio's most-duplicated code.

## 4. Federation, Identity & Network

#### [E] Federated identity & auth layer
"One global username" federating home/work servers; placeholder fields already in prototypes (`[DEALBREAKER-HOOK]` honored). Governance repaired per §R-03: an *optional* capability of the open standard; Divia.AI Global competes as reference IdP.

#### [E] AR storefront-discovery
Point-camera → federated-entity overlay. Registry approach repaired per §R-06 (federate onto Overture/OSM + GS1 GLN + did:web; build the overlay, not the registry). Feasibility upgraded by VPS + multimodal ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §5).

#### [P] "Divia-compatible identity" specification
The §R-03 repair as its own deliverable: the spec any IdP can implement (auth flows, credential formats, selective disclosure, agent-credential extension). Cheap to draft, strategically large — it is what makes "open protocol" true for identity rather than aspirational.

## 5. Developer Tooling & AI-Assisted Coding

#### [E] Laptop TUI multi-tool coding-session manager
aixocode — shipping, most product-complete in the portfolio; MC-style TUI; MIT open-core wedge (ship the missing LICENSE file).

#### [E] Lossless AI-coding-session capture & archive
Byte-for-byte preservation; the compounding moat; the `[DEALBREAKER-HOOK]` substrate. Extended to autonomous runs: every Swarm/recurring session captured like a human session (autonomous work deserves *more* audit trail, not less).

#### [E] Cross-platform offline-first AI-coding desktop
The planned desktop edition — name/stack contested (E-02, a John decision); the shared Rust/Tauri "desktop core" with Divia.AI Professional remains the most concrete AIXO↔Divia engineering cross-pollination.

#### [E] Dotfiles manager (Dotfigurator.sh + Dotfigurate.me)
OSS dotfiles manager + sharing network. Thin but coherent; plausible aixocode-adjacent community wedge (dev-environment capture is adjacent to session capture). Conviction TBD.

#### [E] VelocityTerminal *(name-only)*
No description in sources. **Proposed interpretation (speculative):** a performance-focused terminal emulator or terminal-UI runtime — which would slot naturally beside the aixocode Rust/ratatui migration path as either its rendering substrate or a spin-off brand. Hold as IP-asset until John confirms intent.

#### [P] Contractor successor-entity detection (adversarial entity resolution)
P-06's adversarial mode as a standalone capability/product: track legal-entity re-formations (dissolve/re-form to shed records) across Secretary-of-State + licensing + OSHA data. First consumer: ReDreamRebuild report-cards; generalizes to vendor diligence anywhere (KSVGPS deal diligence included). Rare, defensible, and morally satisfying.

## 6. Frameworks & Runtime Infrastructure

#### [E] Scalara Web Services Framework *(historical)*
Seven generations, C++→Python, 1995–2012; the "encapsulate shared functionality" root of codemap's registry and RosettaMQ.

#### [E] RosettaMQ
Rust cross-language module framework; legacy code → registered modules behind high-performance messaging; ships OSS; dual venture/dependency nature. Far-target repaired per §R-07 (retrieval-first expert agent, not fine-tune-first).

#### [E] Cloud orchestration platform (CloudXMT → SensoryMQ.Cloud)
Validated-but-unlaunched Kubernetes-precursor lineage; OpenX 53K-server validation. Reboot-candidate; honest framing: the 2026 wedge is *AI-operated* infrastructure (agents that model + execute migrations — the OpenX job as a product), not another orchestrator.

#### [E] IoT / connected-device platform (GridTransmit → SensoryMQ)
Award-winning 44K-device fleet history → AI-reimagined successor. Paused; the lineage is the asset; any reboot should ride the Swarm/agent stack rather than rebuild device plumbing.

## 7. Consumer & Household

#### [E] Consumption-driven replenishment / smart-shopping-list loop
Nightly cadence; time-decaying items; escalating errands (P-03, P-05). The most demo-able shock-and-awe loop in the portfolio.

#### [E] Kitchen-counter ambient voice-capture device
Both ends of the household loop (capture + delivery). Upgraded with the **edge-AI privacy architecture** ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §4): on-device transcription/classification + speaker attribution; only typed Facts leave the device. "The device hears everything; the network hears only what you'd have typed."

#### [E] Pantry / food-inventory + NL food-log app (TastyPantry)
Five-domain model; recipes as compound foods. Upgraded per §R-11: inventory as a **confidence-aware ledger of atoms** — estimated quantities with bands, decremented by consumption priors, reconciled at receipt anchors; e-receipt/API ingestion over manual entry.

#### [E] Health-metrics aggregator + correlation engine (Sattvasic)
Seven domains; cross-lab normalization; refill runways. Correlation layer relocated per the cross-domain service [P] above; FDA general-wellness guardrails per §R-14.

#### [E] Spice / flavor-pairing explorer (spicemaster3000)
The flavor-tech bet: blend builder, Flavor Bridge Explorer, taste fingerprint, the pairing-data moat. Most spin-out-able consumer product; keep integration protocol-only (S-08).

#### [E] Flavor-pairing licensable data product
The corpus as B2B asset (recipe apps, CPG R&D, vendor white-labels) — distinct Idea from the consumer app.

#### [E] AI personal-finance manager (LegendaryMoney)
The confidence-aware ledger; estimate-don't-abstain; balance-anchor reconciliation; the founder-pedigree wedge. v1 unify / v2 infer intact.

#### [E] Comparison-shopping / price-match app (PriceScanner)
Upgraded into the **best-value engine** (S-06) with three lanes: groceries, **materials** (the 5-Lowe's clearance hunt as a standing agent watch), and **recurring services/subscriptions**.

#### [E] Scale + AI-food-ID nutrition tracker (ex-"TastyCal", name blocked)
BLE-scale × food-photo-ID; the thesis *strengthens* as photo-only apps proliferate (§R-10). Primary home: Sattvasic (health-first, PBC-compatible); TastyPal white-label secondary, research-gated, rename pending.

#### [P] CGM-informed flavor-forward meal planning
S-08's crown: "cook tonight" recommendations optimizing flavor (fingerprint), health (your CGM response history), feasibility (pantry), budget (ledger), and time (Agenda). The $48B personalized-nutrition claim as a concrete, demo-able feature — and the single best showcase of why the open protocol matters (five products, one answer).

#### [P] Implicit palate profiling from food logs
Derive the taste fingerprint from what was *actually eaten* (TastyPantry logs + restaurant Facts) instead of quizzes — exposure-gap vs. genuine-dislike from behavior; the implicit-data principle applied to spicemaster's personalization layer.

#### [P] Food-truck discovery & tracking *(gives TastyTrucks a thesis)*
The name-only TastyTrucks brand interpreted: live food-truck discovery (location feeds + schedules + menus as protocol Facts), preference-matched alerts ("your favorite truck is 6 blocks away until 2pm"), tied into Place entities and the AR overlay. Speculative; cheap to validate; hold as brand + Idea pair.

## 8. Media, Markets & World Knowledge

#### [E] Game-money prediction market (CrowdMadness)
The MobThought reboot; brackets motif; prize legality gated per §R-05 (launch reputation-only; graduate prizes per-state behind the radar).

#### [E] Real-money CFTC-regulated market
Distinct Idea (different regime); brand undecided (game-tone wrong for regulated trading); not-John founder-fit; ~3yr horizon.

#### [E] White-label prediction-market platform
B2B co-branded markets; `patternicity.bet` held defensively. Upgraded: **dogfood the embedded-market card on PatternicityNews first** (S-04) — the white-label pitch then ships with a live reference deployment.

#### [E] Market-research-as-a-service (CrowdResearch)
The B2B side; the game as data-generation engine. The 2008-held domain is quiet evidence of the thesis's durability.

#### [E] Premium-news subscription bundle (Patternicity ONE)
Carried, but see §R-01 — the bundled-resale mechanism is rejected; the repaired form is the subscription optimizer below.

#### [E] DiviaCards-native social network (PatternicitySocial)
The publish-to-the-world surface homed *outside* Divia by doctrine; the DiviaCards headline consumer; the post-X diaspora opening.

#### [E] URL-shortener / share-attribution
`ptnws.link` share tracking; a feature-scale Idea kept for its distinct value (attribution loops feed the cross-promo engine).

#### [P] Auditable oracle / resolution-as-a-service
S-04's resolution mechanism as its own product: evidence-chained, receipt-sealed (P-11) event resolution sold to *other* prediction markets, sweepstakes, and parametric-insurance products. The world graph + credibility engine monetized where the pain (resolution disputes) is sharpest.

#### [P] Embedded market cards in news (`DiviaCard::CrowdMadness::market`)
The article-page live-market unit as a first-class card type — the concrete artifact that joins Patternicity, CrowdMadness, and DiviaCards, and the white-label demo.

#### [P] News-subscription optimizer *(the repaired Patternicity ONE)*
Track the household's actual reading (Reader/portal Facts) against its paid subscriptions (LegendaryMoney sees the charges); recommend keep/cancel/rotate; one dashboard for news spend. Ships without publisher deals; upgrade path to real bundling if/when agentic micropayment rails mature (per-article licensing) — the mechanism-contingent version of the original idea.

#### [P] Internal milestone prediction markets (venture-studio dogfood)
GPs stake play-money on portfolio milestones inside KSVGPS (S-13); calibration history as a firm asset; the market engine's first deployment, de-risked to zero regulatory surface (internal, no prizes).

## 9. Real Estate & Renovation

#### [E] AVM / property-value estimation
One Idea, two Build-Lines across scale (EstimatePacket now, National-AVM far) — the canonical same-idea-different-scale demonstration.

#### [E] Fractional-ownership / co-ownership marketplace
Pacaso-fused-with-Airbnb-and-Asana; the fractional value bridge made visible; the 8×-liquidity-trap insight as the empirical heart; money rails delegated (S-12).

#### [E] View-durability risk modeling
Current view ≠ durable view; bands not coefficients; the flagship differentiator neither Zillow nor Pacaso exposes.

#### [E] 3D home capture & reconstruction
Rights-clean first-party geometry feeding valuation. Repositioned per [`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §5: a data-acquisition instrument whose *derived analytics* are the durable value (capture tech commoditizes).

#### [E] ADU-advisory data product
Parcel + permitting rules + AI → ADU-potential reports; distinct customer from the AVM; the canonical new-idea-boundary example.

#### [E] Renovation education content venture (ReDreamRebuild core)
Full-spectrum-then-choose methodology; spotting bad work; the $150K→$910K flagship case study (non-disparagement constraint honored — generic failures only, never the named contractor).

#### [E] Contractor OSHA safety report-cards
Public-record per-contractor safety scorecards clustered *into* ReDreamRebuild for SEO compounding; defensibility posture per R-008; hardened by [P] successor-entity detection (§5).

#### [P] Renovation-ROI Estimator
S-07's product: EstimatePacket machinery pointed at improvement decisions — post-reno value bands by material tier, the "informed $150K vs. default $150K" delta made explicit. Joint ReDreamRebuild × FracRealHomes surface; each venture keeps its own audience skin.

#### [P] Independent-oversight receipts (construction QA)
The friend-checks-the-roof-3×-week practice productized: third-party milestone reviews, photo-documented, signed (P-11) — the paper trail that converts disputes into settlements. Content-first (how-to guides), service/marketplace later.

#### [P] Before/after 3D evidence capture
Walkthrough captures pre/post-remodel: marketing proof for ReDreamRebuild case studies, valuation training data for the AVM, dispute evidence for oversight — three consumers, one capture.

## 10. The Firm (meta)

#### [E] Venture-studio corporate blueprint
Series-LLC sub-LLCs → Delaware C-corp reincorporation → QSBS clocks (R-009/R-010); KSVGPS as outsourced legal/finance/IP department; the domain/IP-asset repository with assign/reclaim.

#### [P] Portfolio runway dashboard
S-02: every rotting deadline across every venture (renewals, filings, windows, clocks) in one escalating view — the GP's morning packet. First KSVGPS module to ship after import, because it pays for itself on the first prevented CrowdMadness.com-style loss.

#### [P] Regulatory radar as a product (RegTech spin-out option)
P-14/S-05 proven internally, then sold: jurisdiction-rule graphs + per-client compliance-posture diffs + staged change proposals. Wave-2/3, not-John founder-fit; hold as a dated Triangulation Target on the CrowdMadness line.

#### [P] Dreaming-as-a-service *(far)*
KSVGPS's link-prediction ideation engine (S-13) offered to other venture studios/PE firms once Enterprise is GA — the "feasibility radar" as the wedge that differentiates the whole Enterprise line from generic knowledge bases. Far-horizon; capture now, price later.

## 11. Name-only IP-asset inventory (hold; no forced theses)

`neurogrammatic.com` · `quintivity.com` · `surreality.com` · `transformulator.dev` (+aliases) · JSL Dragonfly Ltd (`jsldragonfly.com`) · CTO Mindmeld Publishing LLC (`ctomindmeld.com`) · Invendra Inc (`invendra.com`; sole hint = the TikTok-Shop-fulfillment musing, explicitly a musing) · TXFR.Cloud Inc (`txfr.cloud/.app/.link` — high-speed transfer, Aspera-like; coherent but dormant) · AdEvolve (2005–2014, historical marker; gated the MobThought reboot 2010–11) · Dotfigurator/VelocityTerminal (see §5). **Modeling rule:** these are **IP-asset + Venture-shell nodes, not Ideas** — do not fabricate theses in the graph; attach `question-mark` interpretation edges where a plausible reading exists (Invendra, VelocityTerminal, TastyTrucks) and let the dreaming agent revisit them against the moving frontier.

---

## §R — The Rejected / Flawed register

Each entry: the claim as found → why it fails → the repair that makes it viable. These are the only backward-references to the prior corpus, by design.

- **R-01 · Patternicity ONE as premium-news bundled resale.** Publishers do not license bundle-resale to small aggregators (NYT's Apple-News exit is the market's verdict); the mechanism is dead on arrival. **Repair:** the news-subscription optimizer (§8) now; true bundling only if agentic per-article payment rails mature (mechanism-contingent, trackable by the dreaming agent).
- **R-02 · The "10,000× better, not 10%" pitch.** Unfalsifiable, hype-pattern-matched, and contradicts the portfolio's own honest-uncertainty discipline. **Repair:** proactive-vs-reactive contrast + measured deltas ([`00`](00-PORTFOLIO-THESIS.md) §8).
- **R-03 · Divia identity as the mandatory portfolio account spine.** Collapses the open-protocol doctrine into suite-hood; concentrates a honeypot the privacy stance disclaims. **Repair:** optional identity capability of the standard; Global as reference IdP; the [P] "Divia-compatible identity" spec (§4).
- **R-04 · DiviaCards as unrestricted JS/TS iframe mini-apps + marketplace.** Third-party code inside the most-private PKMS is a supply-chain and exfiltration nightmare as stated. **Repair:** the two-tier standard — declarative cards default (schema+template, safe everywhere), sandboxed interactive cards behind capability manifests + signing + review (§3).
- **R-05 · "It's a game, so prizes are safe."** The exact assumption that killed MobThought in 2008, and sweepstakes-model enforcement has *tightened* since. **Repair:** launch reputation/leaderboard-only; graduate prizes per-state behind the regulatory radar's green lights; treat prize-value as a first-class jurisdiction variable in the compliance graph.
- **R-06 · A proprietary Global Registry of physical Places for AR discovery.** Rebuilds Google/OSM/Overture at hobby scale; the registry is the least defensible layer. **Repair:** federate — Overture/OSM IDs + GS1 GLN + did:web verifiable links; own the *overlay experience and the entity-link trust*, not the base map.
- **R-07 · A fine-tuned local LLM as the RosettaMQ expert.** Fine-tuning bakes stale facts into weights; frameworks version faster than tunes. **Repair:** retrieval-first expert (versioned knowledge graph + codemap extraction via MCP); adapters only for style ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §11).
- **R-08 · "N=2 is the right scale" as a law.** Cost-regime-contingent finding, already superseded in async fan-out practice. **Repair:** store as a dated, conditional assertion with `valid_from/to`; re-evaluate on cost-curve moves — the canonical demo of bitemporal edges.
- **R-09 · The shrinking client-delta diff as a convergence KPI.** Gameable, confounded by legitimate client-scope growth. **Repair:** graduated-feature count + falling Independent-Implementation-Rate via codemap's registry; keep the diff story as narrative color.
- **R-10 · Photo-only calorie tracking (the whole category's premise).** Portion error is geometric and *random*, hence uncalibratable — better models fix identification, not portions. **Repair (ours):** the BLE-scale × food-ID thesis, which strengthens as the category grows and its inaccuracy becomes folk knowledge.
- **R-11 · TastyPantry's inventory accuracy resting on manual logs/receipt entry.** Contradicts the no-forms philosophy; real households will not maintain it. **Repair:** confidence-aware inventory (estimates + bands + prior-driven decrements + receipt-anchor reconciliation) and e-receipt/API ingestion — the ledger epistemics ported to atoms (§7).
- **R-12 · Enterprise as an office-LAN, IT-administered deployment (as the default).** A 2000s deployment story; SMEs are cloud-first, and the LAN default conflicts with DiviaContacts' reach-the-server-from-anywhere extension. **Repair:** private-tenancy cloud (BYO-VPC) as the default Enterprise tier; LAN/on-prem as the *regulated* tier — mirroring AIXO's own tiering. Self-hosting remains the DiviaHome/community promise.
- **R-13 · "Buy every name we might ever want," unbounded.** Right instinct (the CrowdMadness.com lesson), but unbounded it is a slow leak and a clutter of never-used renewals. **Repair:** the KSVGPS domain system scores each asset (attached Idea conviction × brand quality × repurchase cost) and runs an annual keep/drop review — "managed in perpetuity until the GPs *consciously* discard it" operationalized, with P-03 runways doing the watching.
- **R-14 · The health correlation engine, unguarded.** Auto-surfaced food→symptom claims walk into FDA general-wellness/medical-device territory and can genuinely mislead. **Repair:** hypothesis-framing with effect sizes and multiple-comparison discipline; clinician-shareable exports; explicit non-diagnostic product copy; correlation service governance per §1 [P].
- **R-15 · ERRATA as a standalone document, forever.** A side-ledger drifts like the docs it audits. **Repair:** encode contradictions natively as epistemic-edge data (single-source provenance, question-mark alternatives, documented-not-built status); ERRATA becomes a saved query ([`04`](04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §2.4).
- **R-16 · The fan-out as copy-dispatch.** Corrections fracture, provenance duplicates. **Repair:** Fact + Interpretation subscription (P-01) — the `[DEALBREAKER-HOOK]` on the Divia.Network v0 contract.
