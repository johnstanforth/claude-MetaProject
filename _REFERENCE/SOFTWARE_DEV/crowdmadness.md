# Brief (Software-Dev) — CrowdMadness  ·  **INTRO BRIEF (partial)**

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase**. Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/CrowdMadness/crowdmadness.md)**. **INTRO BRIEF (2026-06-21):** *partial* draft per the [new-venture intro-brief workflow](../../_workflows/workflow_new_venture_intro_brief.md) — **"what we know / infer"** (cited; `TBD`; *Inference:* labels) + inline **❓ Additional Questions for John**. No-invention. **Idea-only — no repo yet**; most engineering facts are open questions. The MobThought-era history is *(per John, this session)*.

## Project / repos

**What we know / infer**
- **No repo exists yet.** *Inference:* the venture implies two engineering surfaces — the **CrowdMadness game** (real-time, mass-scale) and the **CrowdResearch** B2B survey/admin portal — likely separate repos sharing the forecast data.

**❓ Additional Questions for John**
1. Intended **repo structure** (game · CrowdResearch portal · shared forecast-data backend)? A **DailySpikeDriver-level proto** (`proto-crowdmadness-*`) you'd drive first?

## Build Lines · Build Envelopes · Triangulation Target (dated)

**What we know / infer**
- None defined. *Inference:* the game's "massively-scalable" framing implies a **heavier-than-Seed** Build Envelope (real-time markets, high concurrency); CrowdResearch can be a Seed-tier web app.

**❓ Additional Questions for John**
2. **Build Lines** + their **Build Envelopes**? **Dated Triangulation Target** (a mass-scale prediction game + a forecast-data business — ~when)?

## Techstack

**What we know / infer**
- **TBD — nothing in sources.** No language/framework, hosting, payments/wallet, or blockchain mentioned (the dossier explicitly found *no* blockchain references).

**❓ Additional Questions for John**
3. Anticipated **stack** — does it follow the portfolio's Python/Flask seed tier, or does "massively-scalable real-time markets" push toward something else (event-driven, a different runtime)?
4. **Any blockchain/smart-contract element**, or purely a centralized ledger? (Polymarket is on-chain; Kalshi is not — which model, if either?)

## The core engineering bet — market mechanism + resolution  ·  ⭐

**What we know / infer**
- Described only as "prediction market / multiplayer betting / game." **The actual market mechanism is unspecified** (order-book vs. AMM/LMSR vs. parimutuel), and the **resolution/oracle** (who decides outcomes) is undefined. *Inference:* both are likely `[DEALBREAKER-HOOK]`s — hard to swap post-launch.

**❓ Additional Questions for John**
5. ⭐ **Market mechanism** — order-book, an **AMM / LMSR** (log market scoring rule, the classic for thin play-money markets), or **parimutuel**? Any early thinking from the MobThought design?
6. ⭐ **Resolution / oracle** — who/what resolves a market? *Inference (mine):* **PatternicityNews's entity/event graph could feed both the market *questions* and their *auto-resolution*** (news event detected → market resolves). Is that the intended cross-venture link?

## Graph-DB scope vs. KSVGPS / Patternicity  ·  ⭐ the substrate test

**What we know / infer**
- Named a **downstream client of the Divia.AI Enterprise graph-DB core**, sharing the techstack "each with a different scope" (`PLAN…`). But *Inference:* a prediction market is shaped more like a **ledger + time-series** (positions, prices, resolutions) than KSVGPS's relationship graph — so **how much it actually needs the graph-DB is an open, and revealing, question.**
- One concrete cross-venture data idea exists in the sources: "**Possible links to CrowdMadness events to signify why we think trends will happen**" (`notes-domains-sept2025.md`) — i.e. CrowdMadness market-events as evidence for *why* a trend is predicted.

**❓ Additional Questions for John**
7. ⭐ **Does CrowdMadness even need the graph-DB core, and for what?** Where's the line between the graph-DB (entities/events/relationships, shared with Patternicity) and a **ledger/time-series store** (positions, order flow, prices)? **This is exactly the "like Project A, techstack from Project B, different scope" test** the Batch-4 exercise is meant to run.
8. How does its graph-DB scope **differ** from KSVGPS (bounded portfolio) and Patternicity (millions of news entities)?

## Cross-venture links  ·  ⭐

**What we know / infer**
- **Patternicity "Bet" ↔ CrowdMadness:** the sources keep them **separate** (Bet = a Patternicity.AI product with only a domain; no source links them). *Inference (mine, explicitly unconfirmed):* the elegant design would be a **`DiviaCard::CrowdMadness::market` embedded inside a PatternicityNews article** — i.e. DiviaCards as the integration seam between the two new ventures, and "Patternicity Bet" = that embed.
- **News → market resolution:** see Q6 — Patternicity's event graph as CrowdMadness's question-source + oracle.

**❓ Additional Questions for John**
9. ⭐ **Is Patternicity Bet = CrowdMadness embedded in the news product** (via a DiviaCard market card), or are they genuinely separate? (Answering this wires together — or cleanly separates — the two Batch-4 ventures.)
10. Should CrowdMadness markets be **postable/embeddable as DiviaCards** across the ecosystem (so a market can live in a news article, a social post, etc.)?

## `[DEALBREAKER-HOOK]`s (candidates)

**What we know / infer**
- *Inference (candidates — driven by John's answer to "play vs. real money"):* **(a)** the play-money-vs-real-money decision itself (real-money ⇒ a CFTC/KYC/AML/state-licensing fork, `R-002`); **(b)** the **market mechanism**; **(c)** **ledger/position integrity** (an append-only, auditable settlement ledger); **(d)** the **resolution oracle**; **(e)** whether markets are **DiviaCard-embeddable** from day one.

**❓ Additional Questions for John**
11. Which of these are the **irreversible v1 forks** you want hooked now even while the game itself is a play-money prototype?

## Regulatory-tracking subsystem (an engineering feature, not just ops)

**What we know / infer**
- *(per John)* the LLM-economics unlock is an **autonomous agent that nightly tracks per-state + federal regulatory change** and emits the **required-app-change diffs**. *Inference:* this is a reusable subsystem (other regulated ventures could share it) and ties to `R-002`.

**❓ Additional Questions for John**
12. Do you want the **regulatory-tracking agent** modeled as a CrowdMadness Build-Line component (and a candidate **shared service** across the portfolio's regulated ventures)?

## Lineage / convergence

**What we know / infer**
- **Successor of MobThought** (`successor-of` edge — the canonical entity-model example; see the business brief). **Graph-DB client** of Divia.AI Enterprise. No code lineage yet (net-new build).

**❓ Additional Questions for John**
13. Does any **MobThought-era code/design** survive to seed the reboot, or is CrowdMadness a clean-sheet build inheriting only the idea + the data model?

## Cross-references

- Paired business brief: [`../ULTIMATE_VISION/PRODUCTS/CrowdMadness/crowdmadness.md`](../ULTIMATE_VISION/PRODUCTS/CrowdMadness/crowdmadness.md).
- Cross-venture: [`patternicity.md`](patternicity.md) (the Bet/embed + news→resolution link) · graph-DB core [`divia_ai-enterprise.md`](divia_ai-enterprise.md) · [`divia_cards.md`](divia_cards.md) (market-as-card).
- Research: `R-002` (gambling/prediction-market legality) + `R-003` (decade-arc modeling) in [`../../_backlog_TODOs/RESEARCH-BACKLOG.md`](../../_backlog_TODOs/RESEARCH-BACKLOG.md). Model: [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md).
