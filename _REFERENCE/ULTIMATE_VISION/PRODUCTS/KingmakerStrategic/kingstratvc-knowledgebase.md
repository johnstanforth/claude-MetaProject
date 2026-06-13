# Product — KingStratVC Knowledgebase

> A private **PKMS / "company intranet"** for the PE/VC firm Kingmaker Strategic — portfolio &
> idea-stage startup tracking with AI analysis. Also the **first real-world trial-run of a Divia.AI
> Enterprise client install**, implemented as a git fork of DiviaHome.

- **Names:** product **"KingStratVC Knowledgebase"** (per LATER-002) · repo/dir keeps the short name `kingstratvc-web` · firm **Kingmaker Strategic** (abbr. KingStratVC) · in-repo it's styled "KingStrat.vc". Venture detail in [`../../VENTURES/KingmakerStrategic.md`](../../VENTURES/KingmakerStrategic.md).
- **License:** **Inherited DiviaHome AGPLv3 + Commercial** (not yet client-tailored).
- **Status:** 🟠 Phase 00 pending; a **git fork of `diviahome-web`** with a ~5-file client delta.

---

## What it is (consensus)
A private, single-firm intranet (not public/multi-tenant) with three intended pillars: **(1)** a private knowledge base / intranet (structured docs, institutional knowledge); **(2)** **portfolio-company tracking** with AI-driven analysis; **(3)** **idea-stage startup pipeline tracking** with the same AI analysis. Feature set/data model are explicitly unsettled — Phase 00 settles them. Inherits DiviaHome's documents/tasks/calendar/Activity-Log infrastructure.

**Its role in the portfolio — deliberate dogfooding.** KingStratVC is *"a manually-bootstrapped trial-run of what will later become a typical client installation of the Divia.AI Enterprise server."* Since Enterprise is itself being prototyped *as* the Python/Flask DiviaHome app, this is a **git fork of `diviahome-web`**: `main` = a pristine DiviaHome mirror, `kingstrat-main` = the client delta (a tiny ~5-file diff today), stable updates pulled from `upstream`. **Convergence is the discipline:** build what the firm needs here, graduate general infrastructure *down* into DiviaHome, and let the shrinking branch diff measure it — what remains on the delta is, by definition, client-implementation scope vs. product scope.

> ⚠️ ERRATA: the product name **"KingStratVC Knowledgebase" lives only in LATER-002, not yet in the repo** (in-repo it's "KingStrat.vc"); the `_specs_and_plans` docs are **still pristine, un-rebranded DiviaHome**; the "Monday partners' brief" recurring-agent idea isn't in the repo's backlog; it's a plain clone + `upstream` remote, not a GitHub fork. See [`../../ERRATA.md` E-07/E-12`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** AI-driven analysis over portfolio + idea-stage data is the "most distinctive purpose"; defer the client-vs-product classification of each capability until real use decides; convergence-as-discipline (push general parts down into DiviaHome).
- ✦ **New (from LATER-002):** the **Monday partners' brief** — a weekly Swarm-hosted sweep of news / SEC filings / funding events across the firm's tracked portfolio + idea-stage startups, delivered as a ready-made briefing; the single most compelling **`.dvai` LiveDocument / Enterprise "Research Project"** demo for a PE/VC buyer. ✦ **A LiveDocument dossier per portfolio company** (self-refreshing: filings + funding + news + the firm's notes) — partners open a living document, not a stale wiki. ✦ **Dealflow-as-pipeline DiviaCards** with agent-suggested next-actions (the GTD reviewer pattern applied to VC dealflow). ✦ KingStratVC becomes the **reference case study** for Enterprise's vertical-market story the moment it works ("a PE/VC firm's entire deal-flow intranet on Divia.AI Enterprise"). ✦ Track the shrinking `main..kingstrat-main` diff as a literal **"how much of this client's needs became a product feature"** KPI feeding the Enterprise roadmap.
