# VENTURES — The Businesses Behind the Products

> The non-engineering layer: corporate structure, ownership, licensing, monetization, and
> go-to-market across the whole portfolio. **Layered** — this README is the holding/corporate map
> spanning every family; the sibling docs go deep on one business each.

- **Created:** 2026-06-12 · Consensus first, then **Ideation & Exploration**. Naming conflicts flagged to [`../../ERRATA.md`](../../ERRATA.md).

> ⚠️ **Read [`ERRATA.md` E-01](../../ERRATA.md) before treating any corporate name as final.** The top of the corporate tree is named three different ways across the repos, and the newest (the `aixodev-web` Phase-D research canon) *retires* the oldest. These docs lead with the most-recent model but flag it as **unconfirmed pending John's decision.**

---

## 1. The two families + the independents

There are **two genuinely separate corporate/product families**, plus a handful of independently-branded ventures that nonetheless share tech and philosophy:

| Family | Steward entity (as currently named) | What the family sells | Open-source? |
|---|---|---|---|
| **ExoDev / AIXO.Dev** | ExoDev.Pro, Inc. → AIXO.Dev Platforms LLC *(Phase-D canon; older docs: "ExoDev.AI, Inc.")* | Dev-team collaboration platform + Forward-Deployed Engineering consulting | Mostly proprietary; `aixocode` is MIT |
| **Divia.AI** | Divia.AI, Inc. (+ Divia.Foundation, a planned 501(c)(3)) | Personal-knowledge / life-organization ecosystem (desktop, server, mobile, agents) | Hybrid: commercial core + AGPL "home" editions |
| **LegendaryMoney** | LegendaryMoney LLC (Peoria, Arizona) | AI personal-finance manager | Dual AGPLv3 + Commercial |
| **Kingmaker Strategic** | Kingmaker Strategic (PE/VC firm) | *Customer*, not vendor — runs the KingStratVC Knowledgebase intranet (a Divia.AI Enterprise client trial) | Inherits DiviaHome's AGPL+Commercial |
| **TastyPal** | (informal umbrella) | TastyPantry (pantry app) + spicemaster3000 (a potential standalone flavor-tech startup) | Undocumented |
| **SattvasicHealth** | (informal umbrella) | Personal health-metrics aggregator | Undocumented |

**The crucial relationship:** ExoDev/AIXO.Dev and Divia.AI are *separate companies and separate product families* — but they deliberately **cross-pollinate**: a shared `_workflows/` development methodology seeded almost every repo, and two desktop apps (the planned AIXO.Dev Professional and the shipping Divia.AI Professional) intend to share a near-identical Rust/Tauri foundation so lessons flow both ways. They are not one business; they are two businesses run by the same person with shared engineering DNA.

## 2. The licensing strategy (the pattern that recurs)

A consistent **"prototype open, harden commercial"** play runs through Divia.AI and the independents:

- **AGPLv3 + Commercial dual-license (CLA-based)** for the *home/prototype* editions — **DiviaHome**, **LegendaryMoney**, and (intended) the other Divia "lab" apps. The AGPL community edition builds an audience and proves the product; a Contributor License Agreement lets the steward company **relicense the proven functionality into proprietary products.**
- **Proprietary / commercial, closed-source** for the *paid* products — **Divia.AI Professional**, **Divia.AI Enterprise**, **Divia.Life**.
- **MIT** for the one true developer-tool outlier — **`aixocode`** (declared in `pyproject.toml`), which notably contrasts with its own proprietary sibling `aixodev-web`.
- **Undocumented** for many pre-code repos — a gap to close (see the license column in [`../../../_projects/README.md`](../../../_projects/README.md) and [`ERRATA.md` E-12/M`](../../ERRATA.md)).

The dual-license + CLA is the financial engine of the Divia.AI model: **DiviaHome (AGPL) is the R&D lab; Divia.AI Enterprise (proprietary, Rust) is the product the lab's lessons harden into; Divia.AI Global (SaaS) is the eventual recurring-revenue identity layer.**

## 3. How products ladder up to revenue

- **ExoDev/AIXO.Dev:** consulting (Forward-Deployed Software Engineers embedded in client orgs) funds and pulls through the platform (per-seat SaaS). See [`ExoDev.md`](ExoDev.md).
- **Divia.AI:** free/open home editions → paid desktop (Professional) → paid team server (Enterprise) → recurring identity SaaS (Global). See [`DiviaAI.md`](DiviaAI.md).
- **LegendaryMoney:** open home edition → a future proprietary commercial product (same dual-license logic). See [`LegendaryMoney.md`](LegendaryMoney.md).
- **Kingmaker Strategic:** not a vendor — the **first real-world client install** that de-risks the Enterprise product. See [`KingmakerStrategic.md`](KingmakerStrategic.md).
- **TastyPal / spicemaster3000:** spicemaster articulates a genuine consumer/B2B opportunity (a large spice + personalized-nutrition market, a data moat); TastyPantry is ecosystem plumbing. See [`TastyPal.md`](TastyPal.md).

## 4. Ideation & Exploration (venture-level — capture everything, commit to nothing)

- ✦ **A clean holding structure** that names the relationship explicitly: a personal holding entity over *both* ExoDev.Pro, Inc. and Divia.AI, Inc., so the shared-IP flows (the `_workflows/` methodology, the Rust/Tauri desktop foundation, cross-learnings) have a legitimate home instead of being informal. (Resolves the E-01 ambiguity by *design* rather than by edict.)
- ✦ **Divia.Foundation as the open-source release valve for the *whole* portfolio**, not just Divia.AI — a single 501(c)(3) "Code Vault / Code Escrow" that releases commercial source after 3–4 years (or immediately on company shutdown), funds junior-dev training, and runs the "$100K–$10M project rigor, for free, for nonprofits" program the BRANDING doc imagines. Could cover AIXO.Dev and LegendaryMoney too.
- ✦ **One global Divia.AI identity that federates *across families*** — sign in once and see your work tasks (AIXO.Dev Platform / Enterprise), your home (DiviaHome), your money (LegendaryMoney), your health (Sattvasic) — the Divia.AI Global SaaS as the portfolio-wide account layer, not just a Divia.AI-internal one.
- ✦ **The consultancies (ExoDev.Pro Dallas/LA) as Divia.AI's first enterprise customers** — dogfood Divia.AI Enterprise inside the consulting business; every client engagement becomes a reference deployment. The two families' GTMs reinforce each other.
- ✦ **A unified "implicit-data, discover-and-suggest" brand promise** as the portfolio's through-line — the same principle (observe real behavior, surface insight; never make the user fill out a form about themselves) sells TastyPantry, Sattvasic, LegendaryMoney, DiviaHome, and the agent products. Worth a canonical cross-portfolio design-principles manifesto (LATER-002 §11 already proposes promoting it).
- ✦ **Recurring-autonomous-agent capability (Swarm) sold into every family** — "Swarm runs your dev team's recurring agents" *and* "Swarm prepares your team's GTD reviews" are both sellable; none of the OpenClaw-family competitors are positioned as an ecosystem backbone. (See LATER-002.)
- ✦ **Spin-out optionality:** spicemaster3000 and LegendaryMoney are the two products with the clearest path to *independent* venture-scale outcomes (real markets, real moats, their own brands/LLCs) — worth tracking which ventures stay portfolio-internal vs. which could raise/spin out.
- ✦ **A portfolio "category" story** — ExoDev plays the "Palantir analog" (forward-deployed engineering platform); Divia.AI plays the "personal Palantir / personal data ontology" analog (your life's data unified into one legible graph you own). Naming the symmetry could make both pitches sharper.

*(Detailed, sourced venture content continues in the per-family docs.)*
