# Venture — Divia.AI

> A **personal-knowledge & life-organization ecosystem** with a 30-year origin story: own your data,
> capture in natural language, let agents discover-and-suggest. A commercial core (desktop + server +
> agents + mobile) ringed by open-source "home" editions, a nonprofit, and a future identity SaaS.

- **Steward:** **Divia.AI, Inc.** (copyright lines run "© 1996–2026 John Stanforth & Divia.AI, Inc."; the brand-history doc frames the *Divia.AI* identity as "2020–present").
- **Sources:** `divia_ai-professional/BRANDING_and_PRODUCTS.md` (the **canonical naming authority** for the whole ecosystem), `divia_ai-enterprise` README, `divia_ai-agentswarms`, `diviahome-web`, `divialife-flutter`, `diviacontacts-gmail`. Naming/stack conflicts → [`../../ERRATA.md`](../../ERRATA.md).

---

## 1. The 30-year origin lore (consensus, from BRANDING_and_PRODUCTS.md)

The brand carries a deliberate multi-decade arc, each acronym a re-imagining of the same dream — a proactive personal AI assistant:

- **SAI-4000** (1987) — "Simulated Artificial Intelligence." The original concept already imagined passive tracking of tasks, events, finances, health, and calories via wearables.
- **D.I.V.I.A.** (1995) — "Digital Interactive Virtually Intelligent Assistant."
- **DIVIA** (2003–2015) — "Distributed Infrastructure for Virtual Intelligent Agents."
- **Divia.AI** (2020–present) — the current commercial incarnation.

The pitch is "the assistant Siri never became" — proactive, not reactive; **10,000× better, not 10% better.**

## 2. The product family (consensus)

| Product | Repo | Role | License |
|---|---|---|---|
| **Divia.AI Professional** | `divia_ai-professional` | Cross-platform desktop **outliner-editor**; owns `.dvai` + DiviaCards; the desktop client for Enterprise | Proprietary |
| **Divia.AI Enterprise** | `divia_ai-enterprise` | Commercial **Rust team server** (a hardened re-implementation of the DiviaHome server) | Proprietary |
| **Divia.AI AgentSwarms** | `divia_ai-agentswarms` | Rust **agent backbone** — containerized autonomous agents powering AI across the ecosystem | Undocumented (intended proprietary) |
| **DiviaContacts** | `diviacontacts-{gmail,android,iOS}` | Lightweight **CRM-style reader/viewers** of the PKMS (Streak/Copper model) | Proprietary |
| **DiviaHome** | `diviahome-web` | Open-source **household hub** + the experimental prototype that drives the ecosystem | **AGPLv3 + Commercial** |
| **Divia.Life** | `divialife-{flutter,android,iOS}` | Commercial **mobile** app (Agenda / Journal / Messages / Friends & Family) | Proprietary, closed |
| **DiviaCards** | `divia_cards` | Card-rendering layer (typed inputs → Web Components) | Root undocumented; WC sub-package MIT |
| **DiviaMesh** | *(component)* | Multi-device/user **sync protocol** (Rust; WebSockets/WebRTC/ZeroMQ + Loro CRDT) | — |
| **Divia.Network** | *(standard)* | Open, **HTTP-like ecosystem integration layer** / API standards | — |
| **Divia.Foundation** | *(planned)* | A **501(c)(3)** nonprofit arm | — |

Shared vocabulary across all of it: **`.dvai`** (the SQLite-based Divia Document Format), **DiviaCards** (the typed content-block unit — "everything is a DiviaCard"), the **Activity Log** (natural-language capture inbox), and **PKMS** (the personal-knowledge store the desktop/server own and the viewers surface).

## 3. The business model — "prototype open, harden commercial"

The financial engine is a deliberate three-stage ladder:

1. **Prototype in Python, openly (AGPLv3 + Commercial, CLA).** **DiviaHome** (+ the household "lab" apps) is the fast, cheap, public R&D ground. The CLA lets Divia.AI, Inc. **relicense proven functionality into the proprietary products.** *"Explore fast in Python first; converge proven ideas back into commercial products."*
2. **Harden into Rust, commercially.** **Divia.AI Enterprise** is "a higher-performance, locked-down, Rust re-implementation of the DiviaHome server" — *deliberately not started* until DiviaHome reaches a battle-tested v1 + ~30 days of real use (Rust iterates too slowly to commit unvalidated choices). Divia.AI Professional (desktop) is the paid client; Divia.Life (mobile) is the paid companion.
3. **Recurring revenue via identity (SaaS).** A specialized, upgraded build of the Enterprise server becomes the **Divia.AI Global (SaaS) Service** — the central **identity/auth authority** behind "one global Divia.AI username," federating a user's **home server (DiviaHome) and work server (Enterprise).** The Python prototypes already carry placeholder global-identity fields so the later migration is painless. (See [`../USER_STORIES/federated-home-and-work.md`](../USER_STORIES/federated-home-and-work.md).)

**The market framing** (BRANDING / youtube-strategy docs): a "$48B personalized-nutrition," health-literacy, and personal-data-ownership story; the recurring thesis that today's assistants are reactive and shallow, and that a *proactive ecosystem that owns and unifies your real data* is a 10,000× improvement. Target for Enterprise: SMEs deployed on the company office network, administered by corporate IT, from a handful of users to thousands per location.

## 4. Divia.Foundation (the nonprofit arm)

A planned **501(c)(3)** with a striking mission set:
- **Code Vault / Code Escrow** — commercial source is released openly after 3–4 years (or *immediately* if the company shuts down), guaranteeing the community is never orphaned.
- **AI for social good** — "$100K–$10M-grade project rigor, for free" for nonprofits; a junior-developer training pipeline (addressing the "junior-dev crisis" the strategy docs dwell on); thoughtful-middle-ground advocacy on open-source-in-the-AI-era licensing.

## 5. Cross-ecosystem mechanics (consensus)

- **The Divia.Network fan-out** — a single NL capture (*"I had El Pollo Loco for dinner"* / *"$42 at the hardware store"*) lands in DiviaHome's Activity Log and an agent fans it out to TastyPantry (food), Sattvasic Health (macros), LegendaryMoney (expense). These are the ecosystem's **first-ever cross-app integrations** and the proving ground for the Divia.Network v0 contract. (See [`../USER_STORIES/divia-network-fanout.md`](../USER_STORIES/divia-network-fanout.md).)
- **Swarm + Enterprise co-deployment** — Swarm hosts the agents that power Enterprise's AI features (and Pro's right-sidebar chat). *Note: asserted from Swarm's side only — see [`ERRATA.md` E-08](../../ERRATA.md).*
- **DiviaContacts** are thin viewers; the full PKMS stays in Professional (desktop) + Enterprise (server), with DiviaHome as the interim dev/test server.

## 6. Ideation & Exploration (capture everything, commit to nothing)

**From the BRANDING / vision / youtube-strategy docs:**
- **DiviaCards as iframe-sandboxed mini-apps** — a "Notion block with CSS + optional JS/TS," a community-contributed **DiviaCard marketplace**, and a parallel **`.dvai-open`** (JSON+Markdown) format for lock-in avoidance / git-diff / interop with OPML, JSON Canvas, etc.
- **The "input-vector" vision** — desktop typing + text-to-self + kitchen-counter voice + receipt photos + 3rd-party health/glucose feeds all flowing into one collective personal intelligence.
- **A two-track YouTube content engine** ("Divia.AI Concepts" + "Command Line Renaissance") evangelizing the 30-year arc, the proactive-vs-reactive "Siri gap," and the open-source-in-the-AI-era debate.
- **`.dvai` LiveDocuments + Enterprise "Research Projects"** (promoted in LATER-002) — `.dvai` documents that refresh themselves on a schedule via a Swarm agent, keeping their own revision history and inline "what changed" diffs inside the SQLite container. The marquee Enterprise knowledge-work feature.

**✦ New this session (venture-level):**
- ✦ **Divia.AI Global as the portfolio-wide account layer** — federate identity not just across home/work Divia servers but across *every* product (money, health, dev), making "sign in with Divia" the spine of the whole portfolio. (Also in [`README.md`](README.md) §4.)
- ✦ **Agents as Divia.Network contacts** — recurring agents are first-class PKMS entities with people-like pages (DiviaContacts viewing an agent the way it views a colleague); delivery surfaces become ecosystem-native (a thread in Divia.Life Messages, an Activity-Log entry, a DiviaCard in the Journal) instead of email. (From LATER-002 — dogfooding + demo in one.)
- ✦ **Enterprise's "Research Projects" as the B2B beachhead** — the LiveDocument concept sold to firms like Kingmaker Strategic (a continuously-updated portfolio/market dossier) is a sharper enterprise wedge than generic "team docs."
- ✦ **Make the Code Vault a marketed *feature*, not just an ethic** — "every Divia.AI commercial license includes a guaranteed open-source release date" is a genuine trust differentiator for buyers wary of vendor lock-in; pair it with the AGPL home editions as a coherent "you'll never be orphaned" promise.
- ✦ **A single cross-portfolio "discover-and-suggest" manifesto** owned here — the implicit-data principle is the through-line of Divia.AI *and* LegendaryMoney *and* Sattvasic *and* TastyPantry; canonizing it once (LATER-002 §11) makes every product pitch land harder.
- ✦ **DiviaHome devices (the kitchen-counter voice unit) as the consumer wedge** — the always-listening household capture surface that feeds the nightly replenishment loop ([`../USER_STORIES/diviahome-nightly-replenishment.md`](../USER_STORIES/diviahome-nightly-replenishment.md)) is the most demo-able, most "shock-and-awe" entry point into the whole ecosystem.
