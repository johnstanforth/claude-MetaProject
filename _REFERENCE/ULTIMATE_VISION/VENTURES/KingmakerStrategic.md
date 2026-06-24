# Venture — Kingmaker Strategic (KingStratVC)

> A private-equity / venture-capital firm that is, in portfolio terms, a **customer rather than a
> vendor** — the **first real-world client install** that de-risks the Divia.AI Enterprise product,
> while also being a product in its own right: the **KingStratVC Knowledgebase.**

- **The firm:** **Kingmaker Strategic** — a private equity & VC firm, commonly abbreviated **KingStratVC**.
- **The product:** **KingStratVC Knowledgebase** (per the LATER-002 naming decision) — a private PKMS / "company intranet." Repo/dir keeps the developer short-name **`kingstratvc-web`** ("Knowledgebase" is a descriptive noun, not needed at code level).
- **License:** currently **inherited DiviaHome AGPLv3 + Commercial** (not yet client-tailored). **Source:** `kingstratvc-web` (README, CLAUDE.md, GIT-BRANCHING.md).

---

## 1. Consensus

**What it is.** A private, single-firm **PKMS / internal company intranet** for Kingmaker Strategic — *not* public or multi-tenant. Three intended pillars:
1. **Private knowledge base / intranet** — structured docs, internal references, institutional knowledge.
2. **Portfolio-company tracking** — records, status, and AI-driven analysis of active portfolio companies.
3. **Idea-stage startup tracking** — the firm's pipeline of startups in development, same AI-assisted analysis.

Feature set and data model are explicitly **not yet settled** — Phase 00 exists to settle them.

**Its real role in the portfolio — a deliberate dogfooding instance.** KingStratVC is *"a manually-bootstrapped trial-run of what will later become a typical client installation of the Divia.AI Enterprise server."* Since Enterprise is itself currently being prototyped *as* the Python/Flask **DiviaHome** app, KingStratVC is technically a **git fork of `diviahome-web`**:
- `main` = a pristine DiviaHome mirror; `kingstrat-main` = the client delta (today a tiny **5-file** diff). Stable product updates are pulled from `upstream`. (Branch model documented in `GIT-BRANCHING.md`; it's a plain clone + `upstream` remote, not a GitHub fork — forking a *private* repo needs a paid plan.)
- **Convergence is the design discipline:** build whatever the firm needs here freely; over time **graduate general-purpose infrastructure *down* into DiviaHome** and retire the local copy, leaving KingStratVC as a thin **client customization.** Whatever stays on the delta is, by definition, client-implementation scope vs. generally-available product scope. The shrinking branch diff *is* the running record of convergence.

**The business meaning.** Kingmaker Strategic is the venture that proves the Enterprise *client-install* motion end-to-end — a real firm, real portfolio data, real institutional-knowledge needs — before there's a single paying Enterprise customer. It's the bridge between the open DiviaHome lab and the commercial Enterprise product.

## 2. Ideation & Exploration (capture everything, commit to nothing)

**From the repo:**
- AI-driven analysis layered over portfolio + idea-stage data is the *"most distinctive purpose"* of the product.
- The "defer client-vs-product classification until real use decides" principle — *"build it, learn from it, and let real use decide where it belongs."*

**✦ New this session:**
- ✦ **The Monday partners' brief (recurring agent, from LATER-002)** — a weekly Swarm-hosted sweep of news / SEC filings / funding events across the firm's tracked portfolio and idea-stage startups, delivered as a ready-made partners' briefing. The single most compelling demo of a "Research Project / LiveDocument" for a PE/VC buyer. *(Not yet in the repo's backlog — [`ERRATA.md` E-12`](../../ERRATA.md).)*
- ✦ **KingStratVC as the reference case study for Enterprise's vertical-market story** — "we built a PE/VC firm's entire deal-flow intranet on Divia.AI Enterprise in N weeks" is a sales asset the moment it works; the firm doubles as a logo + testimonial.
- ✦ **A `.dvai` LiveDocument per portfolio company** — each company gets a self-refreshing dossier (filings, funding, news, the firm's own notes) that an agent keeps current; the partners open a living document, not a stale wiki page.
- ✦ **Dealflow-as-pipeline DiviaCards** — model idea-stage startups as typed cards moving through stages, with the same agent-suggested next-actions the GTD reviewer uses for tasks (cross-pollinating the Enterprise task graph into VC dealflow).
- ✦ **Convergence metric as a product KPI** — track the shrinking `main..kingstrat-main` diff as a literal measure of "how much of what this client needed became a general product feature" — a clean internal signal for what to build into Enterprise next.

## 3. The venture-studio corporate blueprint *(John, 2026-06-24)*

The cookie-cutter entity structure KingStrat intends to reuse for **most** portfolio startups (still tentative; the open legal questions are queued as research). It is a **time-staged** structure — a cheap earliest-stage vehicle that converts to the investor-standard form once a venture proves out.

- **Kingmaker Strategic Ventures, LLC** = the operating PE/VC firm (structured however is most common for PE firms).
- **"KingStrat V.Studio Fund IV"** (exact name TBD) = a **Texas Series-LLC**, which lets the parent spin up subsidiary-LLCs cheaply (John recalls ~$25 each — to confirm). Early ventures are created as **sub-LLCs inside the Series-LLC** — e.g. **PatternicityNews, LLC**, **FracRealHomes, LLC**, **TastyPal, LLC**. *(Known risk: a Series-LLC is a state-specific construct and may not be uniformly honored by other states' courts — possibly acceptable *because* it only serves the earliest, time-bounded stage before reincorporation. → [`R-009`](../../../_backlog_TODOs/RESEARCH-BACKLOG.md).)*
- **Exceptions skip the sub-LLC stage:** e.g. **ExoDev.Pro, Inc.** likely incorporates straight to a corporation — for branding at the $50K/month corporate-consulting tier, not for entity-structure legal reasons.
- **Reincorporation at maturity** (post-MVP, a few PMF-iterations, formalized investment/hiring): the LLC → **Delaware Chapter-C corporation**. Two reasons: (1) the investor-preferred jurisdiction/courts; (2) it **starts the IRS-Section-1202 (QSBS) clock** — hold 5 years → exclude up to **$50M** of gain (raised from $10M by the **July 2025 "Big Beautiful Bill"**; a major earliest-stage-investor upside KSVGPS should track precisely per venture). A non-DE-HQ'd company also registers as a **Foreign Corporation** in its home state (e.g. a CA-HQ corp with the CA Secretary of State + Franchise Tax Board). → [`R-010`](../../../_backlog_TODOs/RESEARCH-BACKLOG.md).
- **Ownership across the portfolio:** an **overlapping-Venn of KingStrat-LP ownership**, but each venture is otherwise an **independent company** — *not* a corporate sibling of the Divia/ExoDev families (and only a **tech-client** of Divia via the Divia.Network open protocol — see [`STRATEGIC-LANDSCAPE-MODEL.md`](../../STRATEGIC-LANDSCAPE-MODEL.md)).

**KSVGPS as the ventures' outsourced support dept.** Part of the venture-studio premise: by giving earliest-stage teams streamlined shared systems (legal / finance / marketing / **IP-asset management**), KSVGPS lets them focus on the core product and **defer "support-function" hires** until perhaps >10 FTEs. Concretely this includes a **domain-name management system** — a database of every domain's renewal dates + reminders so names are **never lost to oversight** (the **CrowdMadness.com** cautionary tale: MobThought owned it for years, forgot to renew it amid the post-pause chaos, and a reseller now prices it in the thousands). KSVGPS thus serves as the **core IP-asset repository** for each idea, **re-assigning** IP to a startup at incorporation and **reclaiming** it if the startup pauses/closes (managed in perpetuity until the GPs consciously discard it). *This is exactly what the GEN2 **Domain entity** (owner_id, renewal/expiry dates, RDAP) was built to model — renewal-date notifications are a marginal add once domains live in the graph.*

*(This blueprint is cross-venture; it is canon here and pointer-referenced from [`PROJECT-ORGANIZATION-MODEL.md`](../../PROJECT-ORGANIZATION-MODEL.md). It reaches past the current GEN2 schema — Fund / LP-ownership / the LLC→C-corp reincorporation event / IP-asset assign-reclaim are not yet modeled entities — so treat those as a future-schema question, not a today obligation.)*
