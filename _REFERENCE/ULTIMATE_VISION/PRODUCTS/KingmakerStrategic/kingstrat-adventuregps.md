# Brief (Business) — KingStrat AdVentureGPS (KSVGPS)

> **Business-side brief** → the **KSVGPS business knowledgebase** (companies / products / GTM / domains / corporate structure). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (repos · Build Lines · Build Envelopes · techstack · lineage) is the paired **[engineering brief](../../../SOFTWARE_DEV/kingstrat-adventuregps.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Exemplar — sets the business-brief template (2026-06-20).** *(Supersedes the old `kingstratvc-knowledgebase.md`, whose ideas are migrated below.)*

## Identity

| Field | Value |
|---|---|
| **Product (full)** | KingStrat AdVentureGPS |
| **Wordmark** | AdVentureGPS · **URL/acronym** KSVGPS |
| **One-line** | A private venture-studio operating system for a PE/VC firm — Studio Operations control center + LP Dashboard. |
| **Framing metaphor** | VTL ("Vector Tracking Loop") / GPS / air-traffic-control — tracking ventures along their trajectories. |

## Company / corporate structure · Brands

- **Company:** **Kingmaker Strategic Venture Partners LLC** (abbr. **KingStratVC**) — a PE/VC firm; **a *customer*, not a vendor** (it consumes this product, built by the Divia.AI side).
- **Brands:** firm front = *KingmakerStrategic*; product wordmark = *AdVentureGPS*; URL/acronym identity = *KSVGPS* (deliberately distinct, like a ticker vs. a company name; `KSV` retconned to "Kingmaker Strategic Ventures").

## Product Lines → Products

- **Product Line:** the firm's venture-studio operating system — **private, single-firm** (not public/multi-tenant).
  - **Product: KingStrat AdVentureGPS.** Three intended pillars (carried forward from the predecessor): **(1)** a private **knowledge base / intranet** (institutional knowledge, structured docs); **(2)** **portfolio-company tracking** with AI-driven analysis; **(3)** **idea-stage startup pipeline tracking** with the same AI. Two surfaces: **Studio Operations** ("Signal Node" control center + the "Signal Inception" ideation module) and the **LP Dashboard** ("Trajectory Node" LP portal). Inherits DiviaHome's documents/tasks/calendar/Activity-Log infrastructure (via the Enterprise-prototype lineage). *(Distinct from the firm's public website `kingmakerstrategic.com`.)*

## Product Version-Releases

Pre-release (Phase 00). When releases exist, they follow the model's **immutable-past / flexible-future** rule (past = git-matched historical record; future = a movable "marketing sketch" re-bucketable like kanban cards). Future targets sketched today (e.g. "the eventual Rust-server version") can shift `vN` freely until launched.

## Go-to-market / strategic role

**Deliberate dogfooding → the vertical-market reference case study.** KSVGPS is the **first real-world trial-run of a Divia.AI Enterprise client installation**, and becomes the headline case study the moment it works: *"a PE/VC firm's entire deal-flow intranet on Divia.AI Enterprise."*

## Domains (self-contained — from `DOMAIN_MAPPINGS.md`)

- **App (main URL):** **`KSVGPS.kingstrat.ventures`** — a non-wildcard subdomain of `kingstrat.ventures`.
- **Firm front (one canonical):** **`kingmakerstrategic.com`**. Every other `king*` variant **301-redirects** to it: `kingmakerstrategy.com`, `kingstratvc.com`, `kingstrat.vc`, `kingstratventures.com`, and `kingstrat.ventures` **(apex + `www` ONLY — NOT wildcard, so it doesn't capture the `KSVGPS` app subdomain).**

## Ideation & Exploration (capture everything, commit to nothing)

*(Migrated from the predecessor brief — these are the high-value product ideas.)*
- ✦ **The "Monday partners' brief"** — a weekly **AgentSwarms**-hosted sweep of news / SEC filings / funding events across the firm's tracked portfolio + idea-stage startups, delivered as a ready-made briefing. The single most compelling **`.dvai` LiveDocument / Enterprise "Research Project"** demo for a PE/VC buyer.
- ✦ **A LiveDocument dossier per portfolio company** — self-refreshing (filings + funding + news + the firm's notes); partners open a *living* document, not a stale wiki.
- ✦ **Dealflow-as-pipeline DiviaCards** with agent-suggested next-actions (the GTD-reviewer pattern applied to VC dealflow).

## Status

Phase 00 (ideation/research). **Licensing:** KSVGPS is a **proprietary, single-firm internal web service** (private SaaS deployment) — *not* redistributable software: the firm's content is all-rights-reserved IP, access is insider-only, and it's governed by terms-of-use rather than a software license. *(The underlying DiviaHome/proto-divia **engine** is separately AGPLv3 + Commercial dual-licensed; KSVGPS runs it under DiviaAI's commercial grant — engine-license detail in the [engineering brief](../../../SOFTWARE_DEV/kingstrat-adventuregps.md).)* Rebranded from the parked predecessor "KingStratVC Knowledgebase" (2026-06-14) and renamed "VentureGPS" → "AdVentureGPS" (2026-06-15, to avoid a fleet-GPS trademark collision). *(Engineering lineage/git topology → the [engineering brief](../../../SOFTWARE_DEV/kingstrat-adventuregps.md).)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/kingstrat-adventuregps.md`](../../../SOFTWARE_DEV/kingstrat-adventuregps.md).
- Venture: [`../../VENTURES/KingmakerStrategic.md`](../../VENTURES/KingmakerStrategic.md).
- Concept/UX source: `../../../kingstratvc-web_DESIGN_NOTES.md` (VentureGPS-vs-Helix naming session; VTL; Signal/Trajectory nodes; "Signal Inception").
