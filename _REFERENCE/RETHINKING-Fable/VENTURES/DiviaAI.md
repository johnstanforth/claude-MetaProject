# Venture Dossier — Divia.AI (Rethought)

> The personal-knowledge & life-organization ecosystem: a commercial core (desktop · server · agents · mobile) ringed by open-source home editions, a planned nonprofit, and a future identity SaaS — the **personal-graph pole** of the Four Graphs ([`../00-PORTFOLIO-THESIS.md`](../00-PORTFOLIO-THESIS.md) §3). Steward: **Divia.AI, Inc.** This dossier folds in all products (Professional, Enterprise, AgentSwarms, DiviaContacts, DiviaHome, Divia.Life, DiviaCards, Divia.Network, DiviaMesh, Foundation, Global).

## 1. Identity and the thirty-year arc

SAI-4000 (1987, passive tracking of tasks/events/finances/health via wearables) → D.I.V.I.A. (1995) → DIVIA (2003–15) → **Divia.AI** (2020–present): four acronyms, one dream — a *proactive* personal intelligence. The 2026 statement of it: **"Siri answers; Divia notices."** The system observes real behavior across every capture surface, unifies it into a graph the user owns, and stages suggestions a human confirms — the Universal Loop ([`../00`](../00-PORTFOLIO-THESIS.md) §2) pointed at a whole life. (The "10,000×" formulation is retired — [`../03-IDEAS-LEDGER.md`](../03-IDEAS-LEDGER.md) R-02.)

## 2. The product family (one table, roles clarified)

| Product | Role | Stack/status | License |
|---|---|---|---|
| **DiviaHome** | open household hub; the public R&D lab; the Python ancestor that gates the whole commercial server line | Flask; pre-code, the ~60-day focus | AGPLv3 + Commercial (CLA) |
| **Divia.AI Professional** | local-first desktop outliner-editor; owns `.dvai` + DiviaCards vocabulary; Enterprise's desktop client | Rust/Tauri v2 + SvelteKit; Phases 1–2 done, 03 in flight | Proprietary |
| **Divia.AI Enterprise** | the commercial team server = **the portfolio's graph-DB convergence core**; downstream products are clients, not copies | Python prototype (`proto-divia_ai-enterprise`) → Rust (gated on DiviaHome v1 + 30 days' use) | Proprietary |
| **Divia.AI AgentSwarms** | the agent **body**: containerized recurring/autonomous agents powering ecosystem AI | Rust; Phase 00 next | intended proprietary (declare it) |
| **DiviaContacts** | thin CRM-style readers where people already work (Gmail first); server-side intelligence | MV3+InboxSDK design settled; research complete, pre-code | Proprietary |
| **Divia.Life** | commercial mobile: Agenda (forward GPS itinerary) · Journal (daily notes) · Messages · Friends & Family feed | Flutter first, native later (E-03 resolved) | Proprietary |
| **DiviaCards** | the typed-card interchange standard (P-08, two-tier) + the `divia_cards` rendering layer (role assigned per E-05 proposal) | standard live-as-concept; renderer built | standard open; renderer MIT sub-package |
| **Divia.Network** | the open, http-like integration standard — **fact-publication + interpretation-subscription** (P-01) | v0 contract in design | open standard |
| **DiviaMesh** | multi-device sync transport (CRDT — Loro; WebSocket/WebRTC/ZeroMQ) | component, unbuilt | — |
| **Divia.Foundation** | planned 501(c)(3): Code Vault escrow, junior-dev pipeline, AI-for-nonprofits | planned | — |
| **Divia.AI Global** | future identity SaaS — the *reference implementation* of the open identity capability (not a mandatory spine — R-03) | far; placeholder fields already in prototypes | — |

## 3. The business ladder (unchanged in shape, sharpened in wording)

1. **Prototype open** (DiviaHome + labs; AGPL+CLA) — the audience-building, idea-proving tier; the CLA lets proven functionality relicense commercially.
2. **Harden commercial** (Professional desktop, Enterprise server, Divia.Life mobile) — Rust re-implementations begun only after prototypes are battle-tested.
3. **Recur via identity** (Global SaaS) — federated "one global username" across home/work servers, sold as a service; **optional to the protocol**, competitive as an implementation.

**Deployment repair (R-12):** Enterprise's default tier is **private-tenancy cloud (BYO-VPC)**; office-LAN/on-prem becomes the *regulated* tier. Self-hosting remains the DiviaHome community promise. This aligns the server line with how 2026 SMEs actually buy and unblocks DiviaContacts' reach-the-server-from-anywhere architecture.

**Enterprise's marquee feature:** **Research Projects** — agent-tended `.dvai` LiveDocuments (P-07) with dependency-aware refresh ([`../03`](../03-IDEAS-LEDGER.md) §2 [P]); first named buyer KSVGPS (the Monday partners' brief and per-portfolio-company dossiers).

## 4. The ecosystem mechanics, upgraded

- **The fan-out is now the fact/interpretation model (P-01).** One immutable Fact; typed interpretation edges; apps subscribe. Ambient fusion (GPS + card charge + kitchen-device utterance → one high-confidence Fact) is interpretation-of-interpretations. The `[DEALBREAKER-HOOK]`: the v0 Divia.Network contract must be written this way (catalog hook #9).
- **The kitchen device's viability case is edge AI** ([`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §4): on-device transcription/classification + speaker attribution; only typed Facts leave the device. *"The device hears everything; the network hears only what you'd have typed."* This is the consumer trust story Alexa-class devices cannot tell.
- **Agents are protocol citizens.** Recurring agents are PKMS entities with people-like pages (DiviaContacts renders an agent like a colleague); deliveries land as Divia.Life Messages/Journal cards, not email; every agent carries P-05 autonomy grades and, later, P-09 credentials.
- **The Morning Briefing (S-15)** is the daily heartbeat: one fan-in digest — corporate skin on the Enterprise homepage, personal skin in Divia.Life, spoken skin on the device — doubling as the approval queue.
- **Trust architecture is the marketing.** Zero-AI-by-default (Pro), local-first everywhere, visible confidence, the Foundation's Code Vault ("every commercial license includes a guaranteed open-source release date"), and a NEAR-term **local-only AI tier** (edge models; zero cloud calls) — a coherent "never orphaned, never surveilled" position no cloud-native competitor can copy structurally.

## 5. Per-product notes (what changed in the rethink)

- **DiviaHome:** v1 = ImportKit reference build (P-04) + Activity Log; v2 = interpretation layer. Its highest-leverage unbuilt asset is not a feature but the **household demo loop** (nightly replenishment → morning packet) — the portfolio's most demo-able sequence. The durables lane (S-14: warranties, returns, home inventory) is its second interpretation lane after food/money/health.
- **Professional:** the vocabulary beachhead (`.dvai` + DiviaCards). LiveDocument mode requires the *query stored in the container* (hook #12). Editor-stack relitigations (E-11) are normal pre-1.0 churn — record decisions bitemporally rather than fighting drift.
- **Enterprise:** the graph engine spec is [`../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) — epistemic envelope, bitemporality, question-mark edges, vector+graph+FTS. Its first two clients (KSVGPS, the household) exercise disjoint halves of the schema; that is the acceptance test.
- **AgentSwarms:** differentiate on the two axes competitors ignore — *recurring scheduled tasks* and *ecosystem/protocol integration*. Resolution: ephemeral execution + durable externalized memory. Typed workflow steps with effort tiers (P-10) from day one. Declare the license in Phase 00.
- **DiviaContacts:** the thin-renderer/server-side-intelligence split means agent capabilities ship as server deploys (no extension-review latency) — say this in the Enterprise pitch. Capture-to-Activity-Log is its bridge into the fan-out; the relationship-cadence review plus S-09 (world events about *your* people, resolved locally) is its expansion arc.
- **Divia.Life:** Agenda's forward itinerary is the natural surface for agent output (packets as mapped, time-ordered plans). The Friends & Family aggregator is an implicit-data engine and should feed the relationship-cadence loop, not just display feeds.
- **DiviaCards:** two-tier standard per R-04 (declarative default, sandboxed-interactive opt-in with capability manifests). The registry seam (`DiviaCard::Producer::type`) is the protocol's vocabulary — its first cross-company consumer is PatternicityNews's article card, and S-04 adds `DiviaCard::CrowdMadness::market`.
- **Divia.Network:** governance doctrine is canon (open protocol; adopters are tech-clients, never siblings). The A6 name overload (integration layer vs. tutorials site) stays a modeled question-mark until graph migration.

## 6. Ideation & Exploration

**Existing (carried, sharpened):** DiviaCard marketplace (now two-tier per R-04) · `.dvai-open` mirror format · input-vector vision (desktop/voice/receipt/health feeds) · LiveDocuments as Enterprise Research Projects · agents-as-contacts · Code-Vault-as-marketed-feature · the two-track YouTube engine · Google Calendar bidirectional sync · `.dvai` round-trip Pro↔Home · federated context axis (beyond home/work: side business, volunteer org, shared household) · cross-context queries under explicit grants · migration-free-by-design as a marketed promise.

**Proposed (new this rethink):**
- **The local-only AI tier** (Pro + Home): all AI features runnable on-device; the trust wedge sharpened to its point.
- **Cross-domain correlation service** with statistical honesty (R-14 governance) at the Enterprise/Home core — the ecosystem's unique breadth (money × sleep × food × calendar) exercised safely.
- **The durables lane** (S-14) — receipts → possessions → warranty runways → insurance-grade home inventory.
- **Divia-compatible identity spec** — the published standard that makes R-03's repair real; Global as reference IdP.
- **Agent Credentials (P-09)** co-authored with AIXO — principal, scope, autonomy grade, spend caps; the missing rail for L3 autonomy and agentic commerce.
- **Correction-store analytics for the household** — "your household's agent precision this month" as a trust-building surface (P-12 made visible).
- **Interpretation SLAs in the protocol** — subscriptions declare freshness/confidence floors, so downstream apps can render honestly ("estimated, 2 days stale").

**Rejected / Flawed:**
- **⛔ Mandatory portfolio-wide "sign in with Divia"** — R-03; repair = optional capability + reference IdP.
- **⛔ Copy-dispatch fan-out** — R-16; repair = P-01 (hook #9).
- **⛔ Unrestricted JS mini-app cards** — R-04; repair = two-tier.
- **⛔ Office-LAN as Enterprise's default deployment** — R-12; repair = private-tenancy cloud default, on-prem regulated tier.
- **⛔ "10,000× better" pitch** — R-02; repair = "Siri answers; Divia notices" + measured deltas.
- **⛔ Treating E-06's "standalone" self-descriptions as errors to edit away** — the protocol doctrine dissolves the contradiction: independent products that *implement the standard* ([`../00`](../00-PORTFOLIO-THESIS.md) §8).
