# 04 — Graph Schema & Edge Catalog (the KSVGPS import source)

> **RETHINKING-Fable edition** — the recommended node-type taxonomy, edge-type vocabulary, universal edge attributes, and the **full instance catalog** of edges extracted from the corpus plus those proposed in this rethink. This document **extends** (never contradicts) the canon in [`STRATEGIC-LANDSCAPE-MODEL.md`](../STRATEGIC-LANDSCAPE-MODEL.md) and [`PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md): Layer A (Ideas/Topics) is a side ontology joined by non-owning M2M edges; the **Venture owns** Build-Lines, Product-Lines, and Repositories; Build-Lines/Envelopes live in the AIXO.Dev dev-graph, not KSVGPS; the two knowledgebases join at `Company → Product`. Written for future-Fable to parse directly into the KSVGPS graph-DB. Node references use stable kebab-case slugs; mint UUIDv7 ids at import and keep slugs as aliases.

## 1. Node-type taxonomy

### 1.1 Layer A (the Strategic Landscape — KSVGPS Module 1)

| Node type | Notes |
|---|---|
| `Topic` | taxonomy node; parent/child edges; 24 existing + 3 additions ([`03`](03-IDEAS-LEDGER.md) §0) |
| `Idea` | durable, brand-free; axes as properties (conviction, horizon, provenance, leverage); embedding vector (P-13) |
| `Thesis` | falsifiable portfolio bet ("fractional ownership goes mainstream this decade") — **promote to v1**, the dreaming agent needs it |
| `Event` | a dated external occurrence (PASPA repeal, Meta "Arena", a statute change) — **promote to v1**, the feasibility radar needs it |
| `Trend` | a moving curve rather than a point event (LLM cost decline, 3D commoditization); subtype of Event with a trajectory property |
| `Capability` | the shared primitives P-01…P-14 ([`02`](02-SHARED-PRIMITIVES-AND-SYNERGY-MATRIX.md)) — build-once machinery with producer/consumer edges |

*(Canon defined Thesis/Event as "graph-DB era, not yet built" — this rethink's position: the entire justification for KSVGPS v1 is the feasibility radar, which is inert without Event/Trend/Thesis nodes. Ship all three in v1, even if sparsely populated.)*

### 1.2 Layer B (Ventures & the business structure — KSVGPS Module 2)

| Node type | Notes |
|---|---|
| `Venture` | the owner entity; corporate metadata (entity form, jurisdiction, formation/dissolution dates — bitemporal) |
| `Brand` | wordmarks/styling; N per venture |
| `ProductLine` / `Product` | per canon; Version-Releases hang off ProductLine |
| `VersionRelease` | immutable-past/movable-future semantics enforced by ACL (past edits = admin override) |
| `Milestone` | business/HR points; M2M to Stages (dev-graph) and VersionReleases |
| `LegalEvent` | incorporation, Series-LLC sub-formation, reincorporation-to-DE-C, dissolution, IP assignment/reclaim — first-class dated nodes (the studio blueprint runs on these; QSBS clocks start at one) |
| `IPAsset` | domains, trademarks, held names; renewal dates → `Runway` attachments; assign/reclaim history via LegalEvent edges |
| `Person` / `Role` | founders, advisors, LPs, collaborators; role edges are time-bounded |
| `Fund` / `LPStake` | flagged future-schema in canon; stub the node types now so LP-overlap edges have somewhere to land |
| `Jurisdiction` / `Rule` / `CompliancePosture` | the regulatory-radar (P-14) subgraph |
| `ResearchItem` | R-001…R-010 + LATER-nnn; `blocks`/`informs` edges |
| `UserStory` | scenario nodes; `demonstrates →` edges to Ideas/Capabilities ([`05`](05-USER-STORIES.md)) |
| `LiveDocument` | `materializes → Query`; refresh AgentTask link (P-07) |
| `AgentTask` / `AgentRun` / `Agent` | P-05/P-10 subgraph: cadence, autonomy grade, runs, cost, precision history |
| `Receipt` | P-11 signed subgraph snapshots |
| `Runway` | P-03: attachable exhaustion/escalation object (domains, filings, clocks) |

**Scoping note (the four graphs):** KSVGPS carries everything above. The AIXO.Dev dev-graph carries `Repository / BuildLine / BuildEnvelope / TriangulationTarget / Stage / Phase / Sprint / Techstack / Feature` per canon (this catalog references Build-Lines only where a business-side edge needs the anchor). The personal graph carries `Fact / Interpretation / DomainRecord / Correction / Possession` (P-01/P-12/S-14). The world graph carries public `Entity / Claim / Source / CredibilityScore`. All four share §2's edge attributes.

## 2. Universal edge attributes — the epistemic envelope (P-02)

Every edge (and assertion-like node) carries:

```
{ assertion_type: observed | declared | inferred | estimated | proposed | question-mark,
  confidence: 0–1 (or null),  band: optional range,
  provenance: [source refs — doc, repo, "per John 2026-06-24", agent-run id],
  asserted_by: human | agent-id | import-batch,
  method: (for inferred/estimated — how),
  valid_from / valid_to: real-world validity (bitemporal axis 1),
  recorded_at / superseded_at: database knowledge (bitemporal axis 2),
  correction_of: optional edge ref (P-12) }
```

### 2.1 Bitemporality is non-negotiable (a `[DEALBREAKER-HOOK]`)
Immutable-past/movable-future Version-Releases, decade-arc lineages, QSBS clocks, regulatory validity windows, dated regime-conditional findings (R-08 in [`03`](03-IDEAS-LEDGER.md)) — all require valid-time × transaction-time from day one. Retrofitting bitemporality onto a live graph is a rewrite; adding it at schema-birth is a few columns.

### 2.2 Question-mark edges (the L7 pattern)
Unresolved alternatives are modeled as **parallel edges with `assertion_type: question-mark`**, one per candidate, sharing a `decision_group` id and an `owner: John` property. Resolution = one edge upgraded to `declared`, siblings closed with `valid_to` (never deleted — the deliberation history is data). Instances in §4.8.

### 2.3 Single-source assertions
An edge whose provenance lists only one side of a two-party relationship (E-08's Swarm→Enterprise co-deployment) keeps `assertion_type: declared` but gets `provenance: [agentswarms-docs]` and a derived flag `unreciprocated: true`. Reciprocation is an ordinary provenance append.

### 2.4 ERRATA becomes a query
With §2.1–2.3 in place, the ERRATA document reduces to saved queries: *question-mark groups awaiting John* (E-01, E-02…), *unreciprocated edges* (E-06, E-08), *documented-not-built features* (`status: documented-not-built` on Feature nodes — E-11), *numeric drift* (conflicting `declared` values in one property group — E-14). Import the current ERRATA entries as seed data with these encodings; retire the file when the queries reproduce it.

## 3. Edge-type vocabulary

| Edge | Domain → Range | Semantics |
|---|---|---|
| `parent-of` | Topic → Topic | taxonomy |
| `tagged-with` | Idea → Topic | M2M classification |
| `depends-on` | Idea → Idea | needs the target first |
| `enables` | Idea → Idea | makes the target feasible/valuable (inverse of depends-on, kept directional as found) |
| `sibling-of` | Idea ↔ Idea | same Topic, materially different Idea (the new-idea-boundary marker) |
| `variant-of` | Idea ↔ Idea | same-idea-different-scale/customer views that stayed one-or-two nodes by the canon test |
| `successor-of` | Idea/Venture → Idea/Venture | lineage (MobThought→CrowdMadness; Scalara→RosettaMQ); the decade-arc edge |
| `realized-via` | Idea → Idea/Capability | one idea is the mechanism of another |
| `channel` | Idea → Venture | the non-owning, time-bounded reference edge (canon); detach-and-reuse on venture pause |
| `realizes` | BuildLine/ProductLine → Idea | non-owning back-reference (dev-graph side) |
| `motivated-by` | Idea/Venture/Target → Thesis/Event/Trend | why it exists |
| `unlocks` / `threatens` / `gates` | Event/Trend/Rule → Idea/Venture/Target | the feasibility-radar edges |
| `owns` | Venture → ProductLine/Repository/IPAsset… | the Layer-B ownership spine (canon) |
| `adopts-protocol` | Venture → Capability(P-01/P-08) | Divia.Network/DiviaCards tech-client edge — **the only inter-venture "membership" edge; never siblinghood** |
| `delegates-to` | Venture → Venture | consumes another venture's service over the protocol (payload named in properties) |
| `white-labels` | Venture → Venture | rebranded shared tech (Sattvasic → TastyPal scale-app) |
| `dogfoods` | Venture → Product | first-client/reference-install edge |
| `lineage` | Repository → Repository | clone-lineage+merge vs succession-no-merge (dev-graph; property `mode`) |
| `produces` / `consumes` | Venture → Capability | primitive economics (§4.6) |
| `holds-role` | Person → Venture/Idea | time-bounded (founder, advisor, editor…) |
| `influenced` | Person/Work → Idea | provenance color (FeedDemon → Reader) |
| `stake-in` | Fund/Person → Venture | the LP-overlap Venn (stub until Fund schema lands) |
| `subject-to` | Venture → Rule/Jurisdiction | compliance posture anchor |
| `watches` | AgentTask → any | what a recurring agent sweeps |
| `demonstrates` | UserStory → Idea/Capability | scenario coverage |
| `blocks` / `informs` | ResearchItem → Idea/Decision | research gating |
| `materializes` | LiveDocument → Query | P-07 |
| `interpreted-as` | Fact → DomainRecord | P-01 (personal graph) |
| `supersedes` | Correction → Interpretation/Edge | P-12 |

## 4. The instance catalog

Legend: **[E]** from the corpus · **[P]** proposed in this rethink · `?` = question-mark edge (see §4.8) · single-source flags noted.

### 4.1 Idea → Topic → Channel (the Layer-A spine, compact)

| Idea (slug) | Topics | Channel (Venture) | Conviction |
|---|---|---|---|
| graph-db-entity-knowledge-engine | knowledge-graph | Divia.AI Enterprise | active/committed |
| software-dev-knowledgebase-ontology | dev-tooling, knowledge-graph | AIXO.Dev Platform | active |
| source-code-analysis-codemap | dev-tooling, knowledge-graph | AIXO.Dev Platform | active |
| ner-entity-intelligence | knowledge-graph, news-media | Patternicity | idea-only |
| scan-and-import-unification | structured-docs, knowledge-graph, household | DiviaHome | active |
| ai-contacts-relationship-manager | contacts-crm, knowledge-graph, agents | DiviaContacts | active (pre-code) |
| venture-studio-operating-system | venture-studio, knowledge-graph | KSVGPS | active/committed |
| argument-credibility-builder | news-media, knowledge-graph, **trust-verification [P]** | Patternicity | upgraded → infrastructure |
| news-portal-world-knowledge-graph | news-media, knowledge-graph | Patternicity | idea-only |
| world-knowledge-watch-list-service **[P]** | knowledge-graph, news-media | Patternicity | proposed |
| cross-domain-correlation-service **[P]** | knowledge-graph, health, personal-finance | Enterprise/DiviaHome core | proposed |
| team-knowledge-graph-session-mining **[P]** | dev-tooling, knowledge-graph | AIXO.Dev | proposed |
| steering-intervention-analytics **[P]** | dev-tooling | AIXO.Dev | proposed |
| agent-hosting-orchestration-server | agents | Divia.AI AgentSwarms | serious-someday |
| recurring-autonomous-agent-tasks | agents, productivity | Swarm + Enterprise (+AIXO) | serious-someday |
| cross-vendor-agent-collaboration-bus | agents, dev-tooling | AIXO.Dev | active |
| multi-agent-dev-team-coordination | agents, dev-tooling | AIXO.Dev | active-vision |
| hybrid-deterministic-llm-workflow-engine | agents, dev-tooling | AIXO.Dev (workgroups) | planned |
| context-preserving-search | dev-tooling | TBD (skill/aixocode/workflow) | captured |
| personal-life-os-gtd | productivity, structured-docs, agents | Divia.Life (+Enterprise/Swarm) | active/aspirational |
| agent-noc **[P]** | agents, dev-tooling | AIXO.Dev (+Divia.Life twin) | proposed |
| agent-credentials-standard **[P]** | agents, federation, trust-verification | Divia.AI Global + AIXO | proposed |
| morning-briefing-fan-in **[P]** | agents, productivity | Enterprise + Divia.Life + device | proposed |
| livedocument-dependency-refresh **[P]** | structured-docs, agents | Pro + Enterprise | proposed |
| diviacard-interchange-standard | structured-docs | DiviaCards | active (registry seam undecided) |
| structured-knowledge-document-format | structured-docs | Divia.AI Professional | active |
| design-token-management | structured-docs, dev-tooling | AIXO.Dev (projects) | active |
| household-home-os | household, structured-docs, productivity | DiviaHome | active (~60-day focus) |
| cross-app-integration-standard | federation | Divia.Network | serious-someday (v0) |
| durables-lane-home-inventory **[P]** | household, structured-docs | DiviaHome (+LM, FRH consumers) | proposed |
| importkit-shared-library **[P]** | structured-docs, frameworks | DiviaHome ref / codemap-tracked | proposed |
| federated-identity-auth-layer | federation | Divia.AI Global (SaaS) | serious-someday |
| ar-storefront-discovery | contacts-crm, federation | DiviaContacts (android) | aspirational |
| divia-compatible-identity-spec **[P]** | federation, trust-verification | Divia.Network standard | proposed |
| laptop-tui-session-manager | dev-tooling | AIXO.Dev (aixocode) | active/shipping |
| lossless-session-archive | dev-tooling | AIXO.Dev | active/shipping |
| cross-platform-ai-coding-desktop | dev-tooling | AIXO.Dev | placeholder/gated |
| dotfiles-manager | dev-tooling | Dotfigurator.sh (shell) | TBD |
| velocityterminal | dev-tooling | VelocityTerminal.sh (shell) | name-only + `?` interpretation |
| contractor-successor-detection **[P]** | dev-tooling, trust-verification, renovation | ReDreamRebuild (first) | proposed |
| scalara-web-services-framework | frameworks | Scalara Inc (historical) | historical |
| rosettamq | frameworks | OSS (future) | serious-someday |
| cloud-orchestration-platform | cloud-devops, iot | CloudXMT→SensoryMQ.Cloud | reboot-candidate |
| iot-connected-device-platform | iot | GridTransmit→SensoryMQ | paused/reboot-candidate |
| consumption-replenishment-loop | household, food, productivity | DiviaHome | aspirational |
| kitchen-counter-voice-device | household, food, iot | DiviaHome (devices repo, future) | aspirational |
| pantry-food-inventory-nl-log | food | TastyPantry | active (pre-code) |
| health-metrics-aggregator | health | Sattvasic Health | active (pre-code) |
| spice-flavor-pairing-explorer | food | spicemaster3000 / TastyPal | active (research) |
| flavor-pairing-data-product | food | UNDECIDED `?` | someday |
| ai-personal-finance-manager | personal-finance | LegendaryMoney | active |
| comparison-shopping-price-match | personal-finance | LegendaryMoney ("PriceScanner") | exploratory |
| scale-food-id-nutrition-tracker | health, food | Sattvasic primary / TastyPal white-label `?` | potential, name blocked |
| cgm-flavor-meal-planning **[P]** | food, health | cross-venture (protocol) | proposed |
| implicit-palate-profiling **[P]** | food | spicemaster/TastyPal | proposed |
| food-truck-discovery **[P]** | food, contacts-crm | TastyTrucks (shell) | proposed/speculative |
| prediction-market-game-money | prediction-markets | CrowdMadness | active/near-term |
| prediction-market-real-money-cftc | prediction-markets | UNDECIDED `?` (new brand vs Patternicity) | serious-someday |
| prediction-market-white-label | prediction-markets | UNDECIDED (patternicity.bet held) | defensive-someday |
| market-research-as-a-service | market-research | CrowdMadness (CrowdResearch) | idea-only |
| premium-news-subscription-bundle | news-media | Patternicity ONE — **superseded by** news-subscription-optimizer | rejected-as-stated (R-01) |
| news-subscription-optimizer **[P]** | news-media, personal-finance | Patternicity (+LM data) | proposed |
| diviacards-native-social-network | social, structured-docs | PatternicitySocial | idea-only |
| url-shortener-share-attribution | news-media, advertising | Patternicity | idea-only |
| auditable-oracle-resolution **[P]** | prediction-markets, trust-verification | CrowdMadness+Patternicity | proposed |
| embedded-market-news-cards **[P]** | prediction-markets, news-media, structured-docs | CrowdMadness×Patternicity | proposed |
| internal-milestone-markets **[P]** | prediction-markets, venture-studio | KSVGPS (CrowdMadness engine) | proposed |
| avm-property-estimation | real-estate | FracRealHomes | active |
| fractional-ownership-marketplace | real-estate | FracRealHomes | active |
| view-durability-risk-modeling | real-estate | FracRealHomes | active |
| 3d-home-capture-reconstruction | real-estate | FracRealHomes (3D product) | active/long-term |
| adu-advisory-data-product | real-estate | UNDECIDED `?` | someday |
| renovation-education-content | **renovation [P]**, publishing | ReDreamRebuild | active (deferred detail) |
| contractor-osha-report-cards | renovation, trust-verification | ReDreamRebuild | active (R-008 gated) |
| renovation-roi-estimator **[P]** | renovation, real-estate | ReDreamRebuild × FracRealHomes | proposed |
| oversight-receipts-construction-qa **[P]** | renovation, trust-verification | ReDreamRebuild | proposed |
| before-after-3d-evidence **[P]** | renovation, real-estate | ReDreamRebuild × FRH-3D | proposed |
| venture-studio-corporate-blueprint | venture-studio | KingStrat (canon in brief §3) | active |
| portfolio-runway-dashboard **[P]** | venture-studio | KSVGPS | proposed |
| regulatory-radar-product **[P]** | regulatory-compliance [P], venture-studio | CrowdMadness → spin-out option | proposed |
| dreaming-as-a-service **[P]** | venture-studio, knowledge-graph | KSVGPS/Enterprise (far) | proposed/far |
| high-speed-file-transfer | file-transfer | TXFR.Cloud (shell) | TBD |
| invendra / jsl-dragonfly / cto-mindmeld / neurogrammatic / quintivity / surreality / transformulator | (per inventory) | name-only shells | IP-assets, not Ideas |

### 4.2 Idea ↔ Idea edges

| From | Edge | To | Notes |
|---|---|---|---|
| 3d-home-capture | enables | view-durability; avm | geometry/sightline inputs [E] |
| 3d-home-capture | sibling-of | fractional-ownership | [E] |
| adu-advisory | sibling-of | avm | the new-idea-boundary example [E] |
| agent-hosting | depends-on | graph-db-engine | single-source (E-08) — `unreciprocated` [E] |
| agent-hosting | enables | recurring-agent-tasks; cross-app-integration | [E] |
| ai-contacts | depends-on | graph-db-engine | thin-renderer over PKMS [E] |
| ai-contacts | enables | cross-app-integration | capture-to-Activity-Log [E] |
| ai-contacts | sibling-of | ar-storefront | inbox → physical world [E] |
| ai-pfm | enables | comparison-shopping | parsed-purchase stream [E] |
| ai-pfm | sibling-of | health-metrics; pantry-food-inventory | fan-out siblings [E] |
| fractional-ownership | delegates-to (consumes) | ai-pfm | via LM, over protocol [E] |
| argument-credibility | depends-on | news-portal-graph | evidence source [E] |
| argument-credibility | realized-via **[P]** | world-graph immune system | upgraded role ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §8) |
| ar-storefront | depends-on | federated-identity (+external registries per R-06 repair) | [E→P repaired] |
| avm | variant-of | (itself, two Build-Lines: EstimatePacket / National-AVM) | canonical same-idea-two-lines [E] |
| cloud-orchestration | successor-of | (CloudXMT → SensoryMQ.Cloud phases) | [E] |
| cloud-orchestration | leverages | rosettamq | [E] |
| comparison-shopping | realized-via **[P]** | best-value-engine lanes (groceries/materials/subscriptions) | S-06 |
| consumption-replenishment | depends-on | household-home-os; scan-and-import | [E] |
| consumption-replenishment | enabled-by | kitchen-device | capture+delivery [E] |
| context-preserving-search | related-to | lossless-archive; hybrid-engine | [E] |
| cross-app-integration | depends-on | graph-db-engine; diviacard-interchange; agent-hosting | [E] |
| cross-app-integration | realized-via **[P]** | fact-interpretation semantics (P-01) | the R-16 repair; `[DEALBREAKER-HOOK]` |
| cross-vendor-bus | variant-of | multi-agent-coordination | talk/decide vs claim/track — two halves [E] |
| cgm-flavor-meal-planning **[P]** | depends-on | pantry; spice-explorer; health-metrics; ai-pfm | S-08 |
| diviacard-interchange | enables | structured-doc-format; cross-app-integration | [E] |
| diviacards-social | depends-on | news-portal-graph; diviacard-interchange | [E] |
| durables-lane **[P]** | depends-on | ai-pfm (receipt stream); household-home-os | S-14 |
| embedded-market-cards **[P]** | depends-on | game-money-market; news-portal; diviacard-interchange | S-04 |
| auditable-oracle **[P]** | depends-on | world-watch-list; argument-credibility; verifiable-receipts (P-11) | S-04 |
| federated-identity | depends-on | graph-db-engine | specialized Enterprise build [E] |
| federated-identity | sibling-of | cross-app-integration | two federation axes, never conflate [E] |
| agent-credentials **[P]** | depends-on | federated-identity | authority layer atop identity |
| flavor-data-product | sibling-of | spice-explorer | B2B vs consumer regimes [E] |
| graph-db-engine | enables | agent-hosting; cross-app-integration; federated-identity; venture-studio-os | the convergence core [E] |
| health-metrics | consumes | pantry-food-inventory | what-was-eaten detail [E] |
| household-home-os | sibling-of | personal-life-os | household-server vs personal-mobile regimes [E] |
| hybrid-engine | pairs-with | multi-agent-coordination | ladder home [E] |
| internal-milestone-markets **[P]** | depends-on | game-money-market; venture-studio-os | S-13 |
| kitchen-device | enables | household-home-os; consumption-replenishment | [E] |
| laptop-tui | sibling-of | lossless-archive; cross-platform-desktop | distinct customer-values [E] |
| laptop-tui | hosts | cross-vendor-bus | CollabPairs [E] |
| lossless-archive | enables | software-dev-kb; context-preserving-search; team-knowledge-graph **[P]**; steering-analytics **[P]** | the mineable corpus [E+P] |
| market-research | enabled-by | game-money-market | the game generates the data [E] |
| morning-briefing **[P]** | depends-on | cross-app-integration (fan-in); recurring-agents | S-15 |
| ner-entity | variant-of | news-portal-graph | same engine, B2B vs consumer [E] |
| news-portal-graph | depends-on | graph-db-engine | at world scale [E] |
| news-subscription-optimizer **[P]** | depends-on | ai-pfm (recurring charges); news-portal (reading Facts) | R-01 repair |
| pantry-food-inventory | enables | consumption-replenishment | holds the depletion data [E] |
| pantry-food-inventory | variant-of (overlap) | spice-explorer virtual-cabinet | shared inventory *schema* (S-08) [E] |
| personal-life-os | enabled-by | recurring-agent-tasks | the GTD first-pass [E] |
| portfolio-runway-dashboard **[P]** | realized-via | universal-runway (P-03) | S-02 |
| game-money-market | enables | white-label-market; market-research | [E] |
| real-money-market | sibling-of | game-money-market | different regime — never a phase [E] |
| white-label-market | depends-on | real-money-market (real-money variant); game-money-market (game variant) | [E] |
| recurring-agent-tasks | depends-on | agent-hosting; graph-db-engine | body + brain [E] |
| recurring-agent-tasks | enables | structured-doc-format (LiveDocuments) | [E] |
| regulatory-radar-product **[P]** | realized-via | recurring-agent-tasks + world-watch-list | P-14/S-05 |
| renovation-roi-estimator **[P]** | extends | avm | improvement-decision variant; S-07 |
| renovation-roi-estimator **[P]** | depends-on | renovation-education-content (audience) | S-07 |
| contractor-osha-report-cards | depends-on | contractor-successor-detection **[P]**; ner-entity (method) | adversarial ER [E+P] |
| oversight-receipts **[P]** | realized-via | verifiable-receipts (P-11) | S-11 |
| rosettamq | successor-of | scalara-framework | [E] |
| rosettamq | realized-via | source-code-analysis-codemap | legacy transform = codemap productized [E] |
| scan-and-import | enables | household-home-os; consumption-replenishment | + same-shape reuse in ai-pfm/health-metrics [E] |
| software-dev-kb | depends-on | lossless-archive | [E] |
| software-dev-kb | enables | source-code-analysis-codemap | code-property layer [E] |
| spice-explorer | sibling-of | flavor-data-product | [E] |
| implicit-palate-profiling **[P]** | depends-on | pantry-food-inventory (logs); spice-explorer (fingerprint model) | S-08 |
| structured-doc-format | depends-on | diviacard-interchange | outline *of* cards [E] |
| livedocument-refresh **[P]** | extends | structured-doc-format | query-in-container `[DEALBREAKER-HOOK]` |
| url-shortener | depends-on | diviacards-social | [E] |
| venture-studio-os | enables | recurring-agent-tasks (dreaming, Monday brief) | [E] |
| view-durability | extends | avm | risk layer on the baseline [E] |
| view-durability | fed-by | 3d-home-capture | [E] |
| world-watch-list **[P]** | depends-on | news-portal-graph; argument-credibility | S-03; the World-Knowledge v1 |
| cross-domain-correlation **[P]** | depends-on | fact-interpretation (P-01); epistemic-envelope (P-02); correction-store (P-12) | statistical-honesty governance (R-14) |
| food-truck-discovery **[P]** | depends-on | ar-storefront (Place entities); pantry/palate prefs | speculative |

### 4.3 Venture ↔ Venture edges (all non-sibling; protocol or lineage or transaction)

| From | Edge | To | Notes |
|---|---|---|---|
| FracRealHomes | delegates-to | LegendaryMoney | payload: purchase flows, operating-cost accounting, tax handling; over Divia protocol [E] |
| LegendaryMoney · TastyPantry · Sattvasic · FracRealHomes · DiviaContacts · Patternicity(Social) | adopts-protocol | Divia.Network / DiviaCards | tech-client edges; E-06 one-directionality noted as `unreciprocated` provenance until repo docs update [E] |
| Sattvasic Health | white-labels | TastyPal (scale-app, rename pending) | same BLE-scale + food-ID tech, two brand surfaces; primary home = Sattvasic `?`-leaning-declared [E] |
| CrowdMadness | successor-of | MobThought (2004–08) | shared-Idea link, NOT moved assets (canon) [E] |
| SensoryMQ | successor-of | GridTransmit | biz sold back to clients ~2018/19 [E] |
| SensoryMQ.Cloud | successor-of | CloudXMT | [E] |
| ExoDev.Pro | successor-of | Scalara Inc | business-model evolution, not rename; Dallas-first then LA reboot [E] |
| KSVGPS (Kingmaker) | dogfoods | Divia.AI Enterprise | first real client install; reference case study [E] |
| ExoDev.Pro consultancies | dogfoods | AIXO.Dev Platform | "100% of the ExoDev.Pro team" adoption target [E] |
| KingStrat (fund, TBD name) | stake-in | Patternicity · FracRealHomes · TastyPal · CrowdMadness · (most studio ventures) | overlapping-Venn LP ownership; stub Fund schema [E] |
| KSVGPS | manages-IP-for | all studio ventures | assign-at-incorporation / reclaim-at-pause; domain repository [E] |
| Patternicity | delegates-to (stack client) | Divia.AI Professional (Reader stack) · Enterprise (graph core) | tech-client, not sibling [E] |
| Patternicity | produces-for | Divia agents ("memory layer") | via MCP; the world-graph service [E] |
| CrowdMadness | delegates-to **[P]** | Patternicity | question sourcing + resolution evidence (S-04) |
| KSVGPS | delegates-to **[P]** | Patternicity | portfolio watch-lists (S-03) |
| ReDreamRebuild | adjacent-to `?` | FracRealHomes | standalone vs clustered — open question [E] |
| ReDreamRebuild | delegates-to **[P]** | FracRealHomes (valuation) · LegendaryMoney (project budgets) | S-07 |
| aixocode (subsystem) | lineage (lessons-flow) | Divia.AI AgentSwarms | laptop-scale precursor → server scale [E] |
| aixodev-web `_workflows/` | lineage (template-upstream) | Divia-family repos | the bootstrap chain; E-09 corrections apply [E] |
| TastyPantry | lineage (seed-ancestor) | household app chain (Sattvasic → … → DiviaHome per corrected E-09) | per-repo self-reports disagree — record once, low confidence [E] |
| AIXO.Dev Professional | shares-foundation `?` | Divia.AI Professional | Rust/Tauri desktop core — contested E-02 [E] |

### 4.4 External Events / Trends → portfolio edges (the feasibility radar seed set)

| Event/Trend node | Edge | Target | Notes |
|---|---|---|---|
| PASPA repeal (2018) | unlocks | real-money-market | the missed reboot signal — the founding lesson [E] |
| LLM cost-decline trend | unlocks | crowdmadness-reboot; ner-at-scale; ksvgps-dreaming; (ratcheting cadences generally) | the master trend ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §2) [E] |
| Meta "Arena" announcement (2026-06-23) | threatens | game-money-market | incumbent entry; forced `PredictionArena→PredictionBracketsEngine` rename [E] |
| Kubernetes announcement (~2014) | gated | CloudXMT | captured orchestration mindshare; why it never launched [E] |
| Epic v. Apple (2025) + Cal-AI removal saga | informs | scale-app compliance posture | IAP/billing lessons; R-007 verification pending [E] |
| Google Reader death / RSS collapse; FeedDemon abandonment | motivated | patternicity-reader | [E] |
| Post-Musk X diaspora ("landed nowhere") | unlocks | patternicity-social | timing tailwind [E] |
| "Big Beautiful Bill" (2025-07) QSBS $50M | strengthens | venture-studio-blueprint | R-010 [E] |
| Cal AI traction + MyFitnessPal acquisition (reported) | validates | scale-app category | single-source; verify (R-007) [E] |
| Sweepstakes-enforcement tightening (2024–26) | threatens | prize-value game model | drives R-05 repair [P] |
| Gaussian-splatting commoditization | unlocks + threatens | 3d-home-capture | cheaper capture / eroding capture-tech moat ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §5) [P] |
| MCP standardization; Streak CRM-MCP (2026-06) | unlocks | mcp-first surface strategy portfolio-wide | [E] |
| AI-slop web / adversarial content trend | threatens | world-graph ingestion | makes credibility engine mandatory ([`01`](01-TECHNOLOGY-HORIZON-2026-2029.md) §8) [P] |
| Digital Insight IPO (1999) → Intuit $1.2B (2007) | provenance | legendarymoney founder-pedigree | historical Events [E] |
| 2002 Washington Post feature; Winer quotes | provenance | patternicity origins | [E] |

### 4.5 People edges (documented only)

| Person | Edge | Target | Notes |
|---|---|---|---|
| John Stanforth | founder-of / GP-of | (every venture; KingStrat GP) | the portfolio's center [E] |
| David (cofounder) | cofounder-of | LegendaryMoney | Digital Insight 1997; network-security career [E] |
| David Lang | collaborator-of | John (CloudXMT era) | forwarded the k8s announcement from Google MTV [E] |
| Bill Brand (HSN.com President) | advisor-of (2004–08) | MobThought | time-bounded role [E] |
| Stephen McHenry (Google SRE) | advisor-of (2004–08) | MobThought | [E] |
| Jonathan Forster (Spotify VP Mktg) | advisor-of (2004–08) | MobThought | offered Ek intros [E] |
| Rob Landley (Motley Fool) | early-editor-of (2002) | MobThought news angle | [E] |
| Nick Bradbury / FeedDemon | influenced | patternicity-reader | [E] |
| Michael Shermer ("patternicity") | influenced | Patternicity naming | [E] |
| MobThought advisors (open) | `?` re-engagement | CrowdMadness reboot | John's question 6 in the brief [E] |

### 4.6 Capability (primitive) production/consumption

One row per primitive; producers/consumers per [`02`](02-SHARED-PRIMITIVES-AND-SYNERGY-MATRIX.md) Part I — import as `produces`/`consumes` edges: P-01 (DiviaHome/Divia.Network → all), P-02 (Enterprise core → all four graphs), P-03 (DiviaHome/Enterprise → 10+ listed), P-04 (DiviaHome ref → LM, Sattvasic, aixocode, Patternicity), P-05 (workgroups+Swarm → every venture), P-06 (Patternicity at-scale + Enterprise local → all graphs; adversarial mode → ReDreamRebuild/KSVGPS), P-07 (Pro/Enterprise → KSVGPS, Patternicity, CrowdMadness, FRH), P-08 (DiviaCards → all protocol participants), P-09 (Global+AIXO → federation, commerce, AR, cross-org), P-10 (workgroups/Swarm → NOC, budgets, billing), P-11 (ExoDev → KSVGPS, FRH, ReDream, CrowdMadness), P-12 (Enterprise core → every inference surface), P-13 (KSVGPS → triage, capture routing), P-14 (CrowdMadness → FRH, Sattvasic, LM, Social, KSVGPS).

### 4.7 ResearchItem gating edges

| Item | Edge | Target |
|---|---|---|
| R-001 Wikipedia/Wikidata licensing | blocks | ner-entity; news-portal-graph |
| R-002 prediction-market legality (incl. prize-value) | blocks | game-money-market; real-money; white-label |
| R-003 decade-arc/successor modeling | informs | ksvgps schema (this doc) |
| R-004 topic-hubs / vector segmentation | informs | ner-entity; P-13 |
| R-005 three-waves (Cringely) | informs | venture Wave axis |
| R-006 M2M award-name confirmation | informs | gridtransmit lineage record |
| R-007 Cal AI verification | blocks | scale-app build/buy/differentiate decision |
| R-008 OSHA data sourcing + defamation posture | blocks | contractor-osha-report-cards |
| R-009 Series-LLC cross-state recognition | blocks | venture-studio-blueprint (early-stage vehicle) |
| R-010 §1202 QSBS history/stacking | informs | venture-studio-blueprint; portfolio-runway (clock tracking) |
| LATER-001 | informs | hybrid-engine (+ workflow propagation theme) |
| LATER-002 | informs | recurring-agent-tasks (canonical capture) |
| LATER-004 | informs | mobile strategy; ar-storefront placement |
| LATER-005 | informs | context-preserving-search |

### 4.8 Question-mark decision groups (import each candidate as a `question-mark` edge; owner: John)

| Group | Candidates | Current lean |
|---|---|---|
| corporate-parent-naming (E-01) | ExoDev.AI Inc / ExoDev.AI Corp / ExoDev.Pro Inc (+Platform vs Platforms LLC) | Phase-D newest but DRAFT |
| aixo-desktop (E-02) | aixodev-professional (Rust/Tauri) / aixodev-desktop (Electron) | unresolved |
| sattvasic-placement (A4/L7) | PBC under DIVIA Foundation / own umbrella | Candidate A reinforced by scale-app fit |
| real-money-brand | new brand / under Patternicity | 5-year decision; future-Claude proposes from model |
| adu-channel | FracRealHomes line / own venture | TBD |
| flavor-data-channel | spicemaster line / own data-licensing venture | TBD |
| crowdresearch-structure | brand / subsidiary / B2B division; one-funnel vs two | TBD |
| scale-app-home | Sattvasic primary / TastyPal white-label (rename pending) | Sattvasic primary (lean captured) |
| redream-position | standalone / FracRealHomes-adjacent | TBD |
| divia-network-meaning (A6) | integration standard / tutorials microsite | deferred to graph migration — hold both |
| patternicity-entity-name | PatternicityNews LLC / Patternicity.AI LLC / holdco | TBD |
| patternicitynews-v1-shape | aggregator / original analysis / graph explorer | TBD |
| diviacard-reconciliation (E-05) | app = standard's rendering layer (proposed-declared this rethink) / separately-named things | proposed resolution pending John |
| domain-buys | patternicity.com $3,195 / crowdmadness.com $2,285 / others per wishlist | John's explicit call, scored per R-13 repair |

### 4.9 `[DEALBREAKER-HOOK]` registry (hook now; catastrophic to retrofit)

1. **[E]** Byte-for-byte session preservation (aixocode) — the substrate moat.
2. **[E]** Placeholder global-identity fields in every v1 prototype.
3. **[E]** Bitemporal/graph seams in the AIXO Ontology.
4. **[E]** Typed-envelope collab substrate (supersedes screen-scraping).
5. **[E]** Workgroups Flask/FastAPI two-process split.
6. **[E]** `.dvai` format admits LiveDocument mode later.
7. **[E]** FracRealHomes "scenario before coefficient / bands not numbers."
8. **[E]** LegendaryMoney confidence-aware ledger schema (the v1 seam).
9. **[P]** Divia.Network v0 = fact-publication + interpretation-subscription (not copy-dispatch).
10. **[P]** Epistemic envelope on every edge from KSVGPS day one (§2).
11. **[P]** Bitemporality (valid + transaction time) from KSVGPS day one (§2.1).
12. **[P]** `.dvai` stores the materializing *query* beside content (dependency-aware refresh).
13. **[P]** DiviaCards two-tier capability model (declarative default; sandboxed opt-in).
14. **[P]** Vector index beside graph index from KSVGPS v1 (P-13; dreaming is inert without it).

## 5. Import notes for future-Fable

- **Precedence:** this catalog > the RETHINKING dossiers > the v0.1 `ULTIMATE_VISION/` corpus > per-repo self-reports (E-09's lesson). Where this catalog marks `?`, import alternatives — never pick silently.
- **Idempotency:** slugs are the natural keys; re-imports upsert by slug and append provenance rather than duplicating nodes.
- **Do not fabricate:** name-only shells import as `IPAsset` + `Venture(shell)` with zero Idea edges unless marked `?`-interpretation here.
- **Everything gets the envelope:** even "obvious" edges carry provenance (`rethinking-fable-2026-07-01` as import batch) — the ERRATA-as-query capability depends on it.
- **Seed the radar:** §4.4's Events/Trends are the dreaming agent's first watch-list; wire each `unlocks/threatens` edge to a re-evaluation AgentTask at import time.

## 6. Rejected / Flawed (schema-level)

- **⛔ Copy-dispatch fan-out semantics** — see R-16; hook #9 above.
- **⛔ Idea-owns-Build-Lines** — already reversed by canon (2026-06-23); recorded here so no future import resurrects it from older documents.
- **⛔ Single-time edges** (no bitemporality) — breaks immutable-past releases, decade arcs, dated findings, QSBS clocks; hook #11.
- **⛔ ERRATA as a maintained side-file in the graph era** — see R-15; §2.4 replaces it.
- **⛔ Collapsing the four graphs into one database** — ACL scoping (Layer-A researchers, LP dashboards, household privacy) and the consent-surface doctrine both require sovereign graphs with explicit bridges; one big graph is simpler exactly until the first external user, then it is a liability. The shared element is the *schema philosophy*, not the instance.
