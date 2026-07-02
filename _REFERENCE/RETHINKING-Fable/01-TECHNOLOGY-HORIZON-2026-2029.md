# 01 — Technology Horizon 2026–2029 (Rethought)

> **RETHINKING-Fable edition** — the AI/LLM capability curve as of mid-2026, projected three years out, mapped onto concrete portfolio unlocks. Written so the KSVGPS graph can model **Technology-Trend nodes** with `unlocks →` edges to Ideas and Triangulation Targets (the nightly dreaming agent's raw material — see [`00-PORTFOLIO-THESIS.md`](00-PORTFOLIO-THESIS.md) §6). Dates are banded estimates, deliberately coarse: **NOW** (shipping mid-2026), **NEAR** (~2027), **MID** (~2028–29). Every claim here should be stored bitemporally and re-checked by the dreaming agent — this document is a snapshot of a moving frontier, not scripture.

## 1. Reasoning models and long-horizon agents

- **NOW:** frontier models (Fable-class) sustain multi-hour agentic sessions with tool use, structured outputs, and adversarial self-verification; multi-agent orchestration with deterministic control flow is practical and cheap enough for recurring jobs. **Unlocks:** every LATER-002 recurring agent (GTD reviewer, ledger reviewer, dev stewardship, Monday partners' brief, nightly dreaming) is buildable *today* on scheduled cloud runs — the gating work is product surface and trust plumbing, not model capability.
- **NEAR:** reliable multi-day task ownership with checkpointing; agents that maintain their own working memory across sessions without bespoke scaffolding. **Unlocks:** AIXO's "multi-week autonomous project ownership" moonshot becomes a supervised reality (L2 with daily human gates); Swarm's resident-vs-ephemeral question resolves decisively toward *ephemeral execution + durable externalized memory* because the externalized-memory half is what improves.
- **MID:** agent fleets with learned division of labor; cross-org agent transactions under credentialed authority. **Unlocks:** the ExoDev "cross-org agent-to-agent negotiation" moonshot — gated less by capability than by the **agent-credential standard** proposed in [`03-IDEAS-LEDGER.md`](03-IDEAS-LEDGER.md) (P-09).

## 2. The cost curve — the load-bearing assumption

- Iso-capability inference cost has fallen roughly 10× every 12–18 months since 2023 and shows no saturation; cached-input pricing and batch tiers compound it. **Planning rule:** anything affordable once-a-week today is affordable nightly in ~18 months and continuously in ~36. Design cadences to *ratchet* (weekly → nightly → continuous) rather than fixing them.
- **Consequences per venture:** CrowdMadness's nightly 50-state regulatory sweep (the reboot's entire feasibility case) gets an order of magnitude cheaper by launch; Patternicity's NER-at-scale corpus refresh moves from batch-daily toward streaming; KSVGPS "dreaming" can afford link-prediction over the *whole* landscape nightly; the household loop (DiviaHome) fits in consumer-grade budgets.
- **The discipline that stays:** the collabs research finding that *input-token re-reading dominates cost ~150:1* remains true at every price point — scoped context projection (Build-Line/Envelope-scoped views, the orchestrator-context-preservation directive) is a permanent architecture principle, not a 2026 workaround. Effort-tiering (cheap models for mechanical steps, frontier for judgment) likewise persists because the *ratio* between tiers persists even as absolute prices fall.

## 3. Context, memory, and why the graphs still win

- **NOW→MID:** multi-million-token contexts and provider-side memory features keep expanding; it becomes possible to hold an entire venture brief corpus (this one) in a single frontier-model context.
- **The claim to reject preemptively:** *"big context makes the graph-DB unnecessary."* False for this portfolio, for four structural reasons: (1) **ACLs** — Layer-A-only researchers, LP-scoped dashboards, per-household privacy cannot be enforced inside an undifferentiated context blob; (2) **provenance and bitemporality** — "what did we believe on March 3rd, asserted by whom" is a query over structured assertions, not over prose; (3) **consent surfaces** — cross-graph bridges must be *inspectable grants*, which requires the bridge to be a first-class object; (4) **write-back** — agents don't just read the model, they propose edges to it, and proposals need a place to land. **The synthesis:** context is the *working set*, the graph is the *institution*. GraphRAG-style hybrid retrieval (graph traversal + vector similarity + full-text) is the durable pattern; KSVGPS should ship graph + vector + FTS indices together from v1.

## 4. On-device and local models — the privacy unlock

- **NOW:** 3–30B-class models run well on phone/laptop NPUs; local transcription (Whisper-class and better) is essentially free; structured classification at the edge is reliable for bounded taxonomies.
- **Unlocks (this is the DiviaHome kitchen device's entire viability case):** always-listening ambient capture becomes *privacy-viable* when the audio never leaves the device — local wake/segment/transcribe/classify, with only typed, reviewable Facts (not audio, not raw transcripts) crossing to the household server. Speaker diarization at the edge gives household-member attribution ("who said we're out of coffee") which the routing layer needs (personal vs. household captures). **Sell the architecture explicitly:** "the device hears everything; the network hears only what you'd have typed." This inverts the Alexa/Google trust problem and is the single strongest consumer differentiator available to DiviaHome.
- **NEAR:** local models handle first-pass interpretation of most Facts (food parsing, merchant guessing, task extraction), escalating to frontier models only for ambiguity — an effort-tier ladder that reaches into the home. Divia.AI Professional's opt-in AI gains a "local-only mode" tier: AI features with zero cloud calls, the trust-first wedge sharpened to a point no cloud competitor can match.
- **MID:** per-user adapter-tuning on-device (your own correction history fine-tunes your own local parser). The learning loop (P-12) becomes partially local — corrections improve *your* model without your data training anyone else's.

## 5. Multimodal — vision, speech, and 3D

- **Vision NOW:** receipt OCR/parsing is solved; food-photo identification is good and improving (portion estimation from photos alone remains structurally broken — the BLE-scale thesis holds and hardens: *what* from the camera, *how much* from the scale); construction-defect recognition from photos (the wrong-order roof tiles) is within reach of a fine-tuned or well-prompted multimodal pass — a ReDreamRebuild "second pair of eyes" feature by NEAR.
- **Speech NOW:** real-time, speaker-attributed, noise-robust transcription on cheap hardware — the kitchen device, call logging (DiviaContacts), and voice money-capture (LegendaryMoney) all ride this.
- **3D NEAR:** Gaussian-splatting-class reconstruction is commoditizing fast — phone-walkthrough → navigable interior model drops from specialist pipeline to SDK. **Consequence for FracRealHomes:** the `fracrealhomes-android` 3D-capture bet gets *cheaper and less differentiated* every quarter; the durable value shifts from the capture tech itself to (a) the **rights-clean first-party geometry** (Google's photoreal tiles forbid analytical use — owning your own geometry stays valuable) and (b) the **derived analytics** (sightlines, legal-max-build envelopes, view-durability deltas). Plan the 3D product as a data-acquisition instrument for the valuation engine, not as a wow-demo — the wow will be table stakes by 2028.
- **AR NEAR→MID:** visual positioning services + multimodal models make the point-your-camera storefront overlay much more tractable than the cautious "later, fun feature" framing assumed — but see the registry critique in [`03-IDEAS-LEDGER.md`](03-IDEAS-LEDGER.md) (federate onto Overture/OSM + GS1, don't build a proprietary place registry).

## 6. Agentic infrastructure — protocols, identity, and commerce

- **MCP is the settled substrate (NOW):** every portfolio surface should assume MCP as the way third-party agents reach it — the AIXO MCP server (session data), the Patternicity world-knowledge connector (the discovery loop past training cutoffs), Streak's 2026 CRM-MCP precedent for DiviaContacts, and KSVGPS itself exposing the venture graph to John's own Claude sessions. "MCP-first surface area" is a portfolio-wide design rule, not a per-product idea.
- **Agent identity & authority (NEAR — the gap the portfolio should fill):** cross-org agent actions need verifiable "who sent you, with what authority, at what autonomy grade" — verifiable-credential rails (did:web, selective disclosure) exist but no de-facto *agent authority* standard has won. The Divia.AI Global identity work + the autonomy ladder + Engagement-Receipt signing add up to a credible **Agent Credentials** proposal (P-09): an agent carries a signed credential naming its principal, scope, autonomy grade, and audit endpoint. This is simultaneously the missing piece for ExoDev's cross-org moonshot, Divia's federation story, and the trust architecture generally — and standards are land-grabs: NEAR-term participation matters even if adoption is MID.
- **Agentic commerce (NEAR):** agent-initiated purchases (the replenishment loop's L3 endgame, PriceScanner's "buy the clearance flooring at store #5") will run into merchant-side agent-verification and payments rails that are actively forming; the trust boundary (explicit per-staple graduation, spend caps, after-the-fact audit) is exactly the shape regulators and card networks are converging on. Build the approval/audit plumbing now; attach the payment rails when they stabilize.

## 7. Structured generation and the hybrid engine — John's bet is the industry's direction

Typed tool calls, schema-constrained outputs, and deterministic validation gates have become the *standard* way serious agent systems ship. The LATER-001 hybrid deterministic+LLM workflow engine — explicit typed steps, code-enforced gates that cannot be hallucinated past, per-step model/effort routing — is not a speculative idea; it is early convergence on what the field standardized. **Implications:** (a) build it with confidence, it will not be throwaway; (b) the differentiator is not the engine but the *library of encoded workflows* (the `_workflows/` corpus, CollabPair templates, sprint gates) — executable institutional knowledge is the moat, engines commoditize; (c) the same typed-step model is what makes agent runs *auditable*, which feeds the cost ledger (P-10) and the Agent NOC.

## 8. Entity resolution, data quality, and the adversarial turn

- **NOW:** LLM-assisted entity resolution is cheap enough to make the Patternicity world graph and the OSHA contractor report-cards feasible at small-team scale — the "why now" holds.
- **The new risk that arrives with it (NEAR):** as AI-generated content floods the open web, *ingestion becomes adversarial* — entity graphs built from public text inherit coordinated misinformation, SEO-slop, and data poisoning. **Consequence:** source-credibility weighting is not optional infrastructure for Patternicity; it is the immune system. This reframes **WeighTheFacts**: not a side product but the *internal credibility engine* (per-source, per-claim reliability scoring with evidence chains) that the news graph needs anyway — exposed as a consumer surface secondarily. The same engine serves CrowdMadness market resolution (auditable evidence for settlements) and ReDreamRebuild (public-record verification posture).
- **Same pattern, small scale:** contractor identity games (dissolve the LLC, re-form under a new name to escape a bad record) make ReDreamRebuild's report-cards an *adversarial* entity-resolution problem — and `successor-of` edge detection across Secretary-of-State filings is precisely the graph capability the portfolio already builds for venture lineage. One capability, benign and adversarial deployments.

## 9. What gets cheaper vs. what stays scarce (the planning compass)

| Gets dramatically cheaper 2026→2029 | Stays scarce (the moats to hold) |
|---|---|
| Tokens, reasoning depth, agent-hours | Losslessly captured *history* (can't be retro-collected) |
| NER, classification, translation, transcription | Entity-resolved, provenance-carrying, *corrected* graphs |
| Code generation, migration mechanics | Encoded institutional workflows + graduated trust |
| 3D reconstruction, multimodal perception | Rights-clean first-party data (geometry, pairings, OSHA, forecasts) |
| Building yet another agent framework | Distribution, protocol adoption, credential authority |
| Demos of everything above | Regulatory-compliance track record; audit trails; brand trust |

**The compass:** invest where the right column compounds; rent everything in the left column; never build a moat out of anything on the left.

## 10. Per-venture unlock timeline (banded)

| Venture | NOW (2026) | NEAR (~2027) | MID (~2028–29) |
|---|---|---|---|
| DiviaHome | Activity Log + scan-and-import; weekly agent review | on-device kitchen capture; nightly replenishment; consumption forecasting | L2/L3 graduated auto-reorder; whole-home ambient context |
| Divia.AI Pro/Enterprise | `.dvai` + opt-in Claude-API AI | LiveDocuments/Research Projects; local-only AI tier | CRDT collaboration; federated identity GA |
| AgentSwarms | scheduled cloud routines suffice | Swarm v1: containerized recurring agents + typed steps | fleet economics; credentialed cross-org actions |
| LegendaryMoney | v1 unify (imports, ledger, assertions) | v2 NL + ambient fusion (GPS+card+voice); ledger-review agent | agentic bill/renewal actions under caps |
| Sattvasic | import adapters; one-domain slice | BLE-scale + food-ID capture; weekly correlation hypotheses | clinician-grade longitudinal reports; local-first health AI |
| TastyPal/spicemaster | pairing-data app; blend builder | shared inventory substrate; palate-from-logs | CGM-informed flavor-forward meal planning |
| Patternicity | NER pipeline + entity graph MVP; MCP connector | credibility engine; Reader; Morning Briefing surface | B2B world-knowledge subscriptions; streaming graph |
| CrowdMadness | regulatory-radar agent prototype | game launch with per-state gating; market-dossier LiveDocs | real-money/CFTC decision point; RegTech spin-out option |
| FracRealHomes | manual-validated EstimatePackets | 3D capture → geometry inputs; permit watch | multi-market AVM; co-ownership ops platform |
| ReDreamRebuild | SEO content + OSHA dataset assembly | photo defect-spotting assistant; materials price-tier tools | contractor-graph with successor detection |
| KSVGPS | graph-DB v1 + this corpus imported | nightly dreaming (link prediction, target re-bucketing) | LP dashboard; feasibility radar across all ventures |
| AIXO.Dev | session archive + CollabPairs shipping | server E2E sync; workgroups + collabs engines; Ontology v1 | cross-client DomainGraph; agent reputations |

## 11. Rejected / Flawed (horizon-level call-outs)

- **⛔ "A fine-tuned local LLM trained on RosettaMQ's reference material" as the flagship far target (RosettaMQ).** Fine-tuning as the *knowledge-delivery* mechanism is the wrong default in 2026-era practice: retrieval over a versioned, current corpus beats baked-in weights for accuracy, updatability, and auditability, and per-framework fine-tunes go stale with every release. **Repair:** the target is right, the mechanism should be *retrieval-first* — a RosettaMQ expert agent = frontier or local model + the framework's versioned knowledge graph via MCP + codemap's structural extraction; reserve adapter-tuning for style/convention, not facts.
- **⛔ Gating ventures on speculative capability jumps.** Nothing in this portfolio needs AGI-grade breakthroughs; every roadmap item above rides curves already in motion (cost, context, multimodal, edge). Any plan that "waits for the models to get good enough" is misreading the constraint — the binding constraints are product surface, trust plumbing, data acquisition, and distribution. **Repair:** the dreaming agent should track *cost thresholds* and *rail maturity* (payments, credentials), not capability rumors.
- **⛔ "N=2 is the right scale" canonized as a durable law (collabs research).** It was the right answer for 2026-cost synchronous debate; it is cost-regime-contingent, and asynchronous fan-out patterns with cheap verification already exceed N=2 productively. **Repair:** store it as a *dated, regime-conditional finding* — exactly the kind of assertion whose edge carries `valid_from/valid_to` and gets re-evaluated when the cost curve moves. (It is also the canonical example of why the graph needs bitemporal edges.)
- **⛔ Photo-only calorie estimation ever becoming "good enough" and stranding the scale thesis.** The error is geometric (no depth, occluded ingredients), not a model-quality gap — better models narrow *identification* error, not *portion* error, and the error is random hence uncalibratable. The BLE-scale differentiation *strengthens* as photo apps proliferate and their inaccuracy becomes common knowledge. Hold the thesis.
