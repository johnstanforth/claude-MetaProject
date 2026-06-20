# Brief (Business) — Divia.Network

> **Business-side brief** → the **KSVGPS business knowledgebase** (companies / products / GTM / domains / corporate structure). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (anticipated repo · Build Lines · techstack · lineage) is the paired **[engineering brief](../../../SOFTWARE_DEV/divia_network.md)** — which is a **STUB** because this is **idea-only (no repo yet)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Idea-only entity: most specifics are TBD; this brief deliberately carries "Unknown (not in source files)" rather than inventing.**

## Identity

| Field | Value |
|---|---|
| **Product / Standard (full)** | Divia.Network |
| **Wordmark** | Divia.Network (dot, capital "N" in prose; repo/dir form would be `divia-network` / `divia_network`, but **no repo exists**). |
| **One-line** | The open, **HTTP-like ecosystem integration layer / API standard** that connects the Divia family of apps — the "connected Divia.Network ecosystem." |
| **Type** | A **standard / integration layer** (per VENTURES/DiviaAI.md, where it is the "(standard)" row), *not* a shippable app. |
| **Status** | **Idea-only / aspirational (a v2 capability).** The contract that carries the cross-app fan-out is "still being designed" (**v0**). |

**⚠️ Name overload (documented, unresolved — discrepancy A6).** The term "Divia.Network" carries **two different meanings** across the source files, and the conflict is **deliberately deferred** (do NOT resolve it here):

- **As an integration layer / API standard** — the meaning this brief follows (the ULTIMATE_VISION Guide: VENTURES/DiviaAI.md, the fan-out user story, the READMEs).
- **As an education property** — `DOMAIN_MAPPINGS.md` (a naming-authority file) describes Divia.Network's *only* concrete use as an **"online tutorials and training site for the ecosystem of connected apps"** (the microsite at `divia.network`, with redirects like `divia.money → divia.network/managingmymoney/`).

John has confirmed the term genuinely drifted (and that a forgotten earlier prototype exists); per `REVISED_ANALYSIS_UltimateVision.md` item **A6**, the canonical reconciliation is **deferred to the future KingStrat AdVentureGPS graph-DB migration** — the ULTIMATE_VISION Markdown is explicitly NOT to be edited to resolve it now. This brief records both meanings and commits to neither.

## Company / corporate structure · Brands

- **Venture / steward:** **Divia.AI, Inc.** (the "Divia.AI Family of Companies"). `DOMAIN_MAPPINGS.md` nests Divia.Network under Divia.AI, Inc.; VENTURES/DiviaAI.md and ULTIMATE_VISION/README scope it the same way. **No source places it under any other umbrella.**
- **Brand:** part of the **Divia.AI** family brand (alongside DiviaHome, Divia.Life, DiviaContacts, Divia.AI Professional/Enterprise/AgentSwarms, DiviaCards, DiviaMesh, Divia.Foundation). Subject to the ecosystem-wide brand-spelling drift noted in `ERRATA.md` E-07 ("Divia.Network" dot/capital in prose vs. `divia_*` repo/dir names).

## Product Lines → Products

- **Product Line:** the **Divia.AI family of connected apps** — Divia.Network is the **connective tissue** of that line, not a member app. It is the "open HTTP-like standards" layer over which the family's apps integrate.
- **Product / Standard: Divia.Network.** Defined (in the Guide) as the open integration layer that:
  - **Fans one capture out to many apps** — the canonical "fan-out" (see User Story below): one natural-language sentence parsed by several products at once.
  - **Reverses to fan-*in*** — the same layer can fan many apps' weekly outputs *into* one human-paced digest (the "Monday Morning Briefing" idea, from LATER-002).
  - **"Serves humans, apps, *and* agents uniformly"** — the standard is the bus all three speak over; recurring agents can even be modeled as **Divia.Network "contacts."**
- **Public data contract:** the apps speak **DiviaCards** (the typed content-block unit) over the network; the cross-app fan-out's first integrations use the natural-language **Activity Log** capture as origin. *(Whether DiviaCards "is" the wire format or merely the payload type carried by the network → **Unknown (not in source files)**.)*

## The canonical user story — the Divia.Network Fan-Out

The reason the standard exists, quoted from the sources: a user says one ordinary sentence — *"I had El Pollo Loco for dinner"* (or *"$42 at the hardware store"*) — captured verbatim as a natural-language **DiviaCard** into **DiviaHome's Activity Log**. On the next agent pass, a **Divia.AI AgentSwarms** agent classifies it and **fans the meaning out** over Divia.Network to the products that each own a slice:

- **TastyPantry** → a food-eaten entry (decrements pantry inventory);
- **Sattvasic Health** → that food's calories/macros into the day's intake;
- **LegendaryMoney** → an estimated dining expense (merchant, category, inferred amount with a confidence band);
- **DiviaHome's Activity Log** → keeps the original sentence as durable source of truth, cross-referenced to all three.

These are described as the ecosystem's **"first-ever cross-app integrations"** and the **proving ground for the Divia.Network v0 contract**. (Full narrative + ideation: [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md).)

## Relationship to neighboring Divia layers

| Layer | What it is (per sources) | Relationship to Divia.Network |
|---|---|---|
| **DiviaMesh** | Lower-level **multi-device/user sync protocol** — a "(component)" (Rust; WebSockets/WebRTC/ZeroMQ + Loro CRDT). | **Distinct layer** (separate rows in VENTURES/DiviaAI.md). DiviaMesh = sync; Divia.Network = cross-app integration. The boundary is *not crisply drawn* in prose — `divialife.md` pairs them as "syncs via DiviaMesh / Divia.Network." |
| **DiviaCards** | The typed content-block unit ("everything is a DiviaCard"). | The **public payload/contract** apps exchange over the network. |
| **Divia.AI AgentSwarms** | Rust agent backbone hosting the autonomous agents. | Hosts the agents that **perform** the fan-out classification/delegation. |
| **DiviaHome** | Open-source household hub + ecosystem prototype. | **Capture origin** (the Activity Log) and the dev/test ground where the v0 contract's lessons are learned. |
| **Divia.AI Global (SaaS)** | Future central **identity/auth** authority ("one global Divia.AI username"). | **Identity federation** is a *different* axis (see federated-home/work story); not the same thing as Divia.Network's app-integration layer, though both are "federation." |

## Go-to-market / strategic role

- **The "ecosystem, not an app" proof.** The fan-out is the demo that makes "an ecosystem, not a single app" self-evident — *no single product could produce it; the value is in the connections.* Divia.Network is what turns a pile of standalone apps into a portfolio with a moat.
- **Membership is currently one-directional / aspirational.** Several apps that *should* be Divia.Network participants currently **describe themselves as standalone** — TastyPantry and Sattvasic Health especially (logged in `ERRATA.md` **E-06**); `spicemaster3000` is fully standalone and should **not** be over-claimed as a Divia.Network app. Other products are described only as **participants in** (not owners of) Divia.Network: LegendaryMoney ("a standalone brand that also participates in Divia.Network"), FracRealHomes ("a certified participant in the Divia.Network connected ecosystem," consuming `legendarymoney-web` "over the Divia protocol"), SattvasicHealth, DiviaContacts.
- **No standalone GTM motion of its own** (it is plumbing, not a product a customer buys). Its commercial value accrues to the apps it connects and to the **Divia.AI Enterprise** convergence core beneath it. **Pricing / packaging / channel → Unknown (not in source files).**

## Domains (self-contained — from `DOMAIN_LIST.md` / `DOMAIN_MAPPINGS.md`)

All Divia.Network domains are **owned / registered** (per `DOMAIN_LIST.md`; `divia.network` is RDAP-confirmed), primarily via Spaceship.com — **not aspirational placeholders.** Note: in `DOMAIN_MAPPINGS.md` these domains are attached to the *tutorials/training-site* meaning (the A6 overload).

- **Primary:** **`divia.network`** — registered 2022-02-25, expires 2027-02-25 (Spaceship.com; RDAP-confirmed).
- **Redirect / aliases:** `divia.net`, `divianetwork.com`, `divia.wiki`, `divia.blog`, `divia.page`, `divia.wtf`.
- **Training-microsite redirect (the only documented *content* use of the site):** `divia.money → divia.network/managingmymoney/` (or similar).
- **Note:** no `divia-network.*` / `divia_network.*` domain exists; the hyphen/underscore forms appear only as the user-story filename and in prose.

## Status

**Idea-only / aspirational — v2 capability; v0 contract "still being designed."** Gated behind **DiviaHome v1's "scan-and-import data unification" foundation** ("first unify, then understand"). A "forgotten earlier prototype" is referenced by John but its design is **not documented (Unknown)**. The integration-layer-vs-tutorials-site meaning is **deferred** (discrepancy A6) to the future KingStrat AdVentureGPS graph-DB migration; do not resolve in the Markdown now. **No release / no Product Version-Releases yet.** Engineering specifics (repo, stack, ancestry) → the paired **[engineering brief](../../../SOFTWARE_DEV/divia_network.md)** (a stub, "no Build Lines yet"). *"Good-enough bootstrapped."*

## Ideation & Exploration (capture everything, commit to nothing)

*(From the fan-out user story + the DiviaAI venture/product docs — high-value, not commitments.)*

- ✦ **Reverse the arrow (fan-*in*):** the same network that fans one capture out to four apps can fan four apps' weekly outputs *into* one **Monday Morning Briefing** (GTD packet + pantry + health + money). "The standard serves humans, apps, *and* agents uniformly."
- ✦ **Ambient, multi-signal capture:** GPS + connected-card feed + kitchen-device voice fused into one high-confidence entry; the agent only asks the human when sources disagree.
- ✦ **Confidence as a first-class, visible thing:** every derived entry shows *how sure* it is and *which signal* produced it, so corrections sharpen the priors (the learning loop).
- ✦ **The trust boundary holds across apps:** the agent *stages* the derived entries; nothing commits to a ledger/pantry/health record until a human one-tap confirm (or an auto-confirm above a per-domain learned threshold).
- ✦ **Ecosystem-native delivery surfaces:** recaps arrive as a DiviaCard in the Divia.Life Journal or a Messages thread — not email — dogfooding the network and demoing it at once.
- ✦ **Agents as Divia.Network contacts:** recurring agents are first-class PKMS entities with people-like pages (DiviaContacts viewing an agent the way it views a colleague).
- ✦ **Cross-app Get-Creative:** with eating, spending, and health all flowing through one log, surface insights no single app could see ("late-night fast-food spend tracks with your worst-sleep nights").

## Cross-references

- Paired engineering brief (**STUB — idea-only**): [`../../../SOFTWARE_DEV/divia_network.md`](../../../SOFTWARE_DEV/divia_network.md).
- Venture: [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- Canonical user story: [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md).
- Federation context: [`../../USER_STORIES/federated-home-and-work.md`](../../USER_STORIES/federated-home-and-work.md) · [`../../USER_STORIES/diviahome-nightly-replenishment.md`](../../USER_STORIES/diviahome-nightly-replenishment.md).
- Convergence core it would sit atop: [`divia_ai-enterprise.md`](divia_ai-enterprise.md) · payload contract: [`../DiviaCards/divia_cards.md`](../DiviaCards/divia_cards.md).
- Name-overload discrepancy: `../../../ANALYSIS_DomainList_vs_UltimateVision.md` §A6 · deferral: `../../../REVISED_ANALYSIS_UltimateVision.md` (A6) · membership errata: `../../../ERRATA.md` E-06/E-07.
