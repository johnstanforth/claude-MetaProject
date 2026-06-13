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
