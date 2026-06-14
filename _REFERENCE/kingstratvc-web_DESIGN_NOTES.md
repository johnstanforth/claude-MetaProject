# kingstratvc-web — Design Notes (Gemini naming/concept session)

> Distilled, organized design input for the **`kingstratvc-web`** product, extracted from a brainstorming
> chat with Google Gemini (John steering) on **2026-06-14**. The chat's open question was the product
> **name** ("KingStrat Helix? or KingStrat VentureGPS?") but it grew into a full concept + UI/UX direction.

- **Source:** `Gmail - Gemini chat about \`kingstratvc-web\` …KingStrat Helix… KingStrat VentureGPS….pdf` (in this dir). The PDF is a Gmail print of the Gemini chat; its tables + ASCII mockups got column-shredded by the print, so this doc (and the companion **`kingstratvc-web_gemini-naming-transcript.md`**) are the legible versions.
- **Status:** 🟠 **Ideation — committed to nothing.** The name is **undecided**; figures in the mockups are illustrative. Treat as a design seed (same "capture every idea, commit to nothing" ethos as `ULTIMATE_VISION/`).
- **Reconstruction caveat:** rebuilt best-effort from a mangled PDF; the PDF remains the source of truth for exact wording.

---

## 1. The product, in one line

The **strategic operating system of Kingmaker Strategic Venture Partners LLC** — a private-equity/venture-studio control center that tracks every portfolio company as one interconnected, engineered system aimed at a precise financial destination (not a folder of isolated bets).

## 2. The naming question (still open)

Gemini generated candidates across three thematic angles, then pivoted to a navigation theme that became the front-runner:

| Theme | Candidates | Vibe |
|---|---|---|
| **Bio-Digital / "genetic code"** (CRISPR analogy) | `KingStrat Helix`, `KingStrat Catalyst`, `KingStrat Synthesis` | studio-as-gene-editor; deep-tech |
| **Sovereign Power** ("Kingmaker") | `The Sovereign Stack`, `KingStrat Citadel`, `KingStrat Vanguard` | command/authority/asymmetric advantage |
| **Deep-Tech Infrastructure** | `KingStrat Kernel`, `KingStrat Ledger` / `KingStrat Matrix` | foundational, systemic |
| **★ Navigation / tracking** (the pivot) | **`KingStrat VentureGPS`**, `KingStrat VTL` (Project VTL), `KingStrat Ephemeris` | GPS/telemetry; the one the session built on |

**Current lean: `KingStrat VentureGPS`** — but Helix is still in play. *(John's decision.)*

## 3. Core concept — VentureGPS / the Vector Tracking Loop (VTL)

The load-bearing metaphor, driven by John: a **Vector Tracking Loop**, borrowed from GPS receivers / Kalman filtering. A conventional receiver tracks each satellite in an **isolated silo**; a *vector* loop fuses **all channels at once** through one **centralized estimation engine**, so a weak/noisy channel is held on-lock by the strength of the others.

Applied to the venture studio: portfolio companies are **not** isolated high-risk bets — the platform **aggregates every company's operational signals + capital efficiency + strategic velocity into a single co-dependent loop**, so the studio's shared infrastructure and playbooks dynamically prop up any company hitting "drift/noise" and keep the **whole fund locked on target**. The welcome/"About the System" screen is where the VTL metaphor gets explained to users.

## 4. Dual-node architecture (the key structural idea)

The VTL splits into two specialized modes — which map **1:1 onto the dual audience** of the reframed product (see [[../memory]] / `LATER-003`):

| Node | Audience | Tracks | = product role |
|---|---|---|---|
| **Signal Node** *(Studio Operations)* | internal C-suite / operators / studio engineers | ground-level operational signals, product-market milestones, GTM execution vectors; runs live interventions | **venture-studio operational control center** |
| **Trajectory Node** *(LP Dashboard)* | external LP investors | macro estimate of the fund's absolute trajectory, capital velocity, long-term yield path | **LP investor portal** |

Gemini's framing: *Signal Node = "where are we right now, per company"; Trajectory Node = "where is the whole fund headed."* One captures, one integrates.

## 5. Metrics vocabulary (proposed)

- **Fund Velocity Index (FVI)** — aggregate fund acceleration (e.g. "3.8x").
- **Capital Deployment Efficiency (CDE)** — how efficiently capital converts to realized value.
- **Yield Trajectory / Estimated Yield Velocity** — projected return path (e.g. "~28% YoY").
- **Systemic Moat Index (SMI)** — risk-governance score of the studio's defensibility (proprietary data loops, infra decoupling, structural/compliance leverage).
- **Per-company Velocity + Lock status** — e.g. *Company A [4.8x · Lock: Strong]* vs *Company B [2.1x · Lock: Drift/Noise] → Active Intervention*.

## 6. Core modules (sketched in the session)

1. **Signal Inception / Acquisition** — model a new sector/target: teardown sandbox, game-theoretic leverage estimation (disruption vector %, defensive-moat %), an "infrastructure bootstrapper" that spins up a new build on the studio's reusable AI infra + governance/LP-allotment rails.
2. **Active Portfolio Tracking Loops** (Signal Node) — per-company velocity + lock + signal channels (Prod/Mktg/Exec: Clear/Drift/Stalled).
3. **Intervention Sandbox** — allocate studio resources to a drifting company (target → vector → resource unit → playbook → auto-termination criteria); broadcasts the result to the Trajectory Node.
4. **Cross-Loop Telemetry** — the unified high-density board treating the whole portfolio as one co-dependent loop.
5. **Velocity & Yield Estimation** (Trajectory Node) — the LP-facing macro view + the "Asymmetric Decoupling Chart" (studio-accelerated fund trajectory vs. a noisy/siloed legacy-venture benchmark).
6. **Systemic Moat Index panel** — moat-depth bars per vector (proprietary data-loop maturity, infrastructure decoupling, structural arbitrage/compliance) + a "corrosion friction & auto-restabilization" log.

## 7. UI/UX direction

A deliberate **aerospace / mission-control telemetry aesthetic** — explicitly **not** a generic SaaS dashboard. *Key principle (John's correction): the audience is institutional LPs + operators, not developers — the high-precision "instrument" look is about conveying authority/sophistication, not because anyone is reading code.*

- **"Low-Chrome Dark Mode" palette:** Deep Obsidian background · **Neon Cyber Green** (active, on-lock signals) · **Amber** (warning / drift) · **Muted Telemetry Gray** (non-critical labels).
- **Typography:** **monospace** for all data/telemetry (IBM Plex Mono · SF Mono · Fira Code · Share Tech Mono); clean **industrial sans** for headers. High density, sharp (0–2px) corners, no soft consumer rounding.
- **Components:** telemetry **progress bars** rendered in block characters; a live **terminal system-log**; **delta/metric tags** (`SIG GAIN: +4`, `DRIFT: 0.02`); a live **"VTL Action" intervention trigger** modal when a company drifts into the amber zone.

## 8. How it connects to the rest of the portfolio

- **Directly realizes the reframing** (memory `kingstratvc-ideation-platform-reframing`): Signal Node = the studio control center; Trajectory Node = the LP portal. The "ideation platform" surfaces as the **Signal Inception** module.
- **Chronology-aware provenance** (`LATER-003`): the "tracking loop / trajectory over time" model *is* the chronology-aware datastore — every company's velocity/lock is a time series; interventions are timestamped events. Pairs with the **Postgres TZ-aware UTC** decision.
- **`aixodev-projects` theme system** could supply the design tokens for this dark-telemetry theme (DB-as-source-of-truth → DESIGN.md/DTCG → CSS), turning a prototype into the design layer here.

## 9. Open questions / decisions pending

- **Name:** VentureGPS vs Helix (vs the others). *(John.)*
- Is "VentureGPS / VTL" the **public** brand or just the internal **system** framing under a cleaner public name?
- How literal to take the telemetry aesthetic for an **LP** audience (impressive vs. overwrought) — the Trajectory Node may want a calmer register than the Signal Node.
- Relationship to the existing repo name `kingstratvc-web` and the canonical app domain **`kingstrat.ventures`** (the product name above the code-level short-name).
