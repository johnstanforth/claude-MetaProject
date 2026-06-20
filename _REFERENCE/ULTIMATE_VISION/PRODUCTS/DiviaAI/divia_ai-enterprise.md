# Brief (Business) — Divia.AI Enterprise

> **Business-side brief** → the **KSVGPS business knowledgebase** (companies / products / GTM / domains / corporate structure). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repos · Build Lines · techstack · convergence · license) is the paired **[engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. *(Replaces the old single-file `divia_ai-enterprise.md`, whose still-valid content is migrated below; its engineering content moved to the [engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md).)*

## Identity

| Field | Value |
|---|---|
| **Product (full)** | Divia.AI Enterprise |
| **Short form** | Divia.AI Enterprise (prototype) — the active Python/Flask form; "Divia.AI Enterprise" unqualified = the eventual Rust commercial server (same product, different stack). |
| **One-line** | The commercial, IT-administered **team server** of the Divia.AI ecosystem — structured documents, tasks, calendar, and an AI-assisted capture inbox — for organizations from a handful to thousands of users per location. |
| **Portfolio role** | The **graph-DB core** of the whole portfolio: the one convergence hub where shared core functionality concentrates; downstream products are **clients of it, not copies** (engineering detail → [engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md)). |

## Company / corporate structure · Brands

- **Company / steward:** **Divia.AI, Inc.** (copyright lines run "© 1996–2026 John Stanforth & Divia.AI, Inc."; the *Divia.AI* commercial identity is framed as "2020–present").
- **Venture:** **DiviaAI** — the personal-knowledge & life-organization ecosystem (commercial core ringed by open-source "home" editions, a nonprofit, and a future identity SaaS). See [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **Brand position within the venture:** Divia.AI Enterprise is the **commercial server tier** — paired with the **Divia.AI Professional** desktop client, descended from the open-source **DiviaHome** "lab," and (long-term) the base for the **Divia.AI Global (SaaS)** identity service.

## Product Lines → Products

- **Product Line:** the **Divia.AI family of products** (Divia.AI, Inc.'s commercial line — Professional desktop, Enterprise server, AgentSwarms, DiviaContacts, etc.).
  - **Product: Divia.AI Enterprise** — the multi-user organization **team server**: full client-server workgroup collaboration (centralized management, permissions/roles, shared workspaces, version history, real-time multi-user editing) with Divia.AI Professional as its desktop client. Organized around four interconnected feature domains shared with the DiviaHome lab: **(1) Activity Log** (AI-assisted natural-language capture inbox), **(2) Task Management** (Asana-style — assignment, comment threads, attachments), **(3) Event Calendaring** (assignable/movable events, participants; later bidirectional Google Calendar sync), **(4) Document Editing** (DDF / `.dvai` outliner-of-DiviaCards, round-trip interop with Professional). Deployment: self-hosted on the company office network, administered by corporate IT — **not** a single-household app and **not** public-internet multi-tenancy.

## Product Version-Releases

Pre-release (Phase 00). The product's **v1 mission is "scan-and-import" data unification** — pull years of scattered legacy fragments (hundreds-to-thousands of SMS logs of food/meds/purchases/receipts) into one clean, de-duplicated, unified record. Motto: **"first unify, then understand."** The AI processing layer (the Divia.AI agent's natural-language classification / parsing / cross-app delegation) is an explicit **v2** concern, built after the unified corpus exists. **Identity is staged:** v1 serves one organization with many user accounts and carries **placeholder global-identity fields**; v2 layers in the global Divia.AI identity/auth (federated home + work servers) via the Divia.AI Global SaaS. When releases exist they follow the model's **immutable-past / movable-future** rule (the eventual "Rust-server version" is a future target that can re-bucket freely until launched).

## Go-to-market / strategic role

- **"Research Projects" as the marquee knowledge-work feature** — agent-tended, continuously-updated bodies of knowledge built on `.dvai` LiveDocuments (documents that refresh themselves on a schedule and keep their own revision history). The first named buyer is **KingStratVC** — a self-refreshing portfolio/market dossier per portfolio company — a sharper B2B wedge than generic "team docs."
- **Dogfood-and-demo first installs:** the consultancies (**ExoDev.Pro**) and the recurring-agent GTD review are natural early Enterprise use-cases. The first real-world client installation is **KingStrat AdVentureGPS (KSVGPS)** — a PE/VC firm's entire deal-flow intranet running on the Enterprise core (engine/lineage detail → [engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md)).
- **Target market** (DiviaContacts reframing): SMEs, deployed on the company office network, administered by corporate IT, from a handful to thousands of users per location.
- **The strategic endgame — Divia.AI Global (SaaS):** a specialized, upgraded build of Enterprise becomes the proprietary internal **Divia.AI Global (SaaS) Service** — the central identity/auth authority behind "one global Divia.AI username," federating a user's home (DiviaHome) and work (Enterprise) servers. (See [`../../USER_STORIES/federated-home-and-work.md`](../../USER_STORIES/federated-home-and-work.md).)

## Domains (self-contained — from `DOMAIN_MAPPINGS.md` / `DOMAIN_LIST.md`)

- **Canonical company domain:** **`divia.ai`** (registrar Spaceship.com); the company front for Divia.AI, Inc. and the parent of the product pages.
- **Enterprise product page (canonical):** **`divia.ai/diviaenterpriseserver/`**.
  - **Redirect/alias:** **`diviaenterprise.com`** → `divia.ai/diviaenterpriseserver/`.
- **Company-domain aliases that 301 to `divia.ai`** (selection from the registry): `diviaai.com`, `divia.cc`, `divia.co.in`, `divia.co.uk`, `divia.in`, `divia.one`, `divia.tv`, `divia.uk`, `divia.work`.
- *(No Enterprise-specific domain beyond `diviaenterprise.com` exists in the source files; the GitHub org is `@DiviaAI` — repo/GitHub detail is engineering-side.)*

## Ideation & Exploration (capture everything, commit to nothing)

*(Migrated from the predecessor brief — still-valid business-side ideas.)*
- ✦ **"Research Projects" / `.dvai` LiveDocuments** as the B2B beachhead (KingStratVC the first buyer) — see GTM above.
- ✦ **A single canonical Enterprise definition** reconciling the historical three framings (collaboration/sync server vs. Asana-PKMS-+-Swarm vs. "Pro's server"). This brief + the [engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md) are that single source of truth; the convergence-chain framing (Enterprise = the graph-DB core) is now primary.
- ✦ **The Code Vault as a marketed feature** (venture-level) — "every Divia.AI commercial license includes a guaranteed open-source release date," paired with the AGPL home editions as a coherent "you'll never be orphaned" promise (a trust differentiator for lock-in-wary buyers). The Code Vault is a **Divia.Foundation** mechanism, not a property of this server's license.
- ✦ **Agents as Divia.Network contacts** — recurring agents become first-class PKMS entities with people-like pages; delivery surfaces become ecosystem-native (a Divia.Life Messages thread, an Activity-Log entry, a Journal DiviaCard) instead of email.

## Status

Phase 00 (ideation/research). **Product licensing:** Divia.AI Enterprise is a **proprietary, closed-source commercial product** of Divia.AI, Inc. — both the active Python/Flask prototype **and** the eventual Rust build are closed/commercial (**not** AGPL, **not** dual-licensed; the AGPLv3 + Commercial dual-license belongs only to the upstream open-source **DiviaHome** lab and does not flow down). *(Engine/repo/license-topology detail → [engineering brief](../../../SOFTWARE_DEV/divia_ai-enterprise.md).)* The active build is the **Python/Flask prototype** (`proto-divia_ai-enterprise`, Phase 00 PENDING); the **Rust commercial server** is deliberately **not started** until the prototype reaches a working v1 plus ~30 days of real-world use.

> **Reconciliation note vs. the old brief.** The prior single-file brief framed "Divia.AI Enterprise" as primarily the *Rust* `divia_ai-enterprise` server and treated the Python form as upstream-only. Per `ARCHITECTURE_CONVERGENCE.md`, the live `proto-divia_ai-enterprise` repo, and `DOMAIN_MAPPINGS.md`, the **Product** "Divia.AI Enterprise" is delivered by **two engineering Build Lines** — the *active* Python/Flask prototype and the *future* Rust server (same product, succession-no-merge) — and the product's defining portfolio role is the **graph-DB convergence core**. *(Earlier `Swarm`/`AI-backbone` co-deployment framing was asserted only from AgentSwarms' side — historical ERRATA E-08; not load-bearing here.)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/divia_ai-enterprise.md`](../../../SOFTWARE_DEV/divia_ai-enterprise.md).
- Venture: [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- Upstream ancestor (lineage context): [`../DiviaHome/diviahome.md`](../DiviaHome/diviahome.md).
- First client installation: [`../KingmakerStrategic/kingstrat-adventuregps.md`](../KingmakerStrategic/kingstrat-adventuregps.md).
