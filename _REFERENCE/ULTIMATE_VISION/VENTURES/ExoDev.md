# Venture — ExoDev / AIXO.Dev

> The developer-collaboration family: a **platform** for human + AI software teams, pulled through by
> a **forward-deployed engineering consultancy.** "Bring back the joy of engineering."

- **Sources:** `aixodev-aixocode` (`_REFERENCE/PRODUCT_AND_NAMING.md`, `ELEMENTS-ENTITIES…`, `joy_of_engineering/VISION…`), `aixodev-web` (the Apr-2026 Phase-D product-development research suite). Marked DRAFT/aspirational where noted; the company is pre-seed/pre-office/pre-customer — nearly all business "facts" are projected.
- **Naming caveat:** see [`ERRATA.md` E-01](../../ERRATA.md). Three corporate-naming layers exist; this doc leads with the newest (Phase-D) and flags it.

---

## 1. Corporate structure (consensus = "contested"; newest model shown)

The most recent canon (the `aixodev-web` Phase-D research, Apr 2026) defines a **two-tier structure** and explicitly retires the older "ExoDev.AI" branding:

- **ExoDev.Pro, Inc.** — parent, Dallas HQ, founded 2026. *The "Palantir analog."* Runs the consulting business.
- **AIXO.Dev Platforms LLC** (note plural) — product subsidiary. *The "Foundry analog."* Owns the software platform.
- **ExoDev.Pro Dallas LLC** / **ExoDev.Pro Los Angeles LLC** — regional services LLCs (future: NYC, Chicago, Ireland). The first/internal customers; expansion "to other cities in late 2026 / early 2027."

> **Older, still-in-use names** (flagged in ERRATA): John's `CLAUDE.md` and aixocode's in-repo docs say **"ExoDev.AI, Inc."** with **"ExoDev.Pro - Dallas/Los Angeles."** aixocode's `PRODUCT_AND_NAMING.md` says **"ExoDev.AI Corporation"** with **"ExoDevPro … Inc."** Pick one (a John decision).

### 1a. Lineage — Scalara Inc → ExoDev.Pro (a business-model evolution, not a rename)

ExoDev.Pro's Los Angeles presence has a real predecessor: **Scalara Inc** (2002–present, Greater Los Angeles), John's web-development / web-services consulting firm (**with a few prior name changes** — *TBD; cross-reference John's LinkedIn résumé to confirm the names + exact date-ranges across these ventures*), which built and used the open-source **Scalara Web Services Framework** (1995–2012; see the [`scalara-web-services-framework`](../IDEAS/scalara-web-services-framework.md) Idea node). The shift to ExoDev.Pro is **conceptual on several axes, not a corporate rename:**

- **Business model:** Scalara = **project-based web/platform-building** → ExoDev.Pro = **FDSE consulting, primarily AI-based** (the Palantir Forward-Deployed-Software-Engineer model).
- **Recurring revenue + platform IP:** Scalara had **none** — it was retained to *build* platforms *for* clients, who then **owned and operated their own** platform afterward (no recurring revenue beyond the build engagement). ExoDev.Pro instead **licenses built-in platforms (e.g. the AIXO.Dev Platform) to clients** (the Palantir Foundry/AIP model), so the platform IP compounds vendor-side and revenue recurs.
- **Geography:** Scalara = **one LA office** → ExoDev.Pro = **several regional offices** (Dallas HQ + LA + planned others).

**The realistic sequence (vs. the marketing framing):** John is relocating **LA → Dallas** and founding **ExoDev.Pro, Inc. (Dallas HQ) first**; only *afterward* does he return to **reboot the remnants of Scalara's LA client-base / address-book as a new "ExoDev.Pro – Los Angeles" office** taking Scalara's place. The line *"Scalara Inc is now the LA office of ExoDev.Pro"* is a **marketing positioning** (leverage Scalara's credibility, re-introduce to past clients) — *not* the literal corporate sequence. *(This lineage also helps ground the E-01 corporate-identity question — it explains where the ExoDev.Pro regional-office structure comes from.)*

## 2. What the family sells

**Two intertwined revenue motions:**

1. **The AIXO.Dev Platform (software).** Positioned as **"Linear + GitHub + Slack for human-AI development teams"** — a platform where AI agents are *full team members* with persistent personalities, assigned tasks, and tracked contributions, working alongside humans across hundreds of projects over years. Products:
   - **`aixocode`** — the shipping laptop-side TUI (the bridge between CLI coding tools and the platform). *Power-user, "see under the hood."*
   - **AIXO.Dev Platform (Web)** (`aixodev-web`) — the central server (projects, issues, AI-session transcripts, wiki, analytics, GitHub).
   - **Planned clients:** AIXO.Dev for macOS/Linux (desktop), iPad/Android (tablet), iOS/Android (mobile) — all future. *(Desktop name/stack is itself contested — see [`ERRATA.md` E-02](../../ERRATA.md).)*
2. **Forward-Deployed Software Engineering (consulting).** The Palantir-style motion: **FDSEs embed 3–4 days/week in a client org**, ship a production workflow on the client's real data by engagement day 5, then **"graduate"** the client's own engineers to solo operation by week ~8 and leave. Consulting funds the platform; the platform's IP compounds vendor-side across engagements. Claimed category: **"Forward-Deployed Engineering Platform."**

## 3. Business model & metrics (Phase-D, aspirational)

- **Pricing:** 5-tier per-seat SaaS — Starter $40 / Team $75 / Business $125 / Enterprise $175–225 / Regulated-OnPrem $225–350 per seat/mo (+ on-prem infra $150–400K/yr). A **fixed $20K, 5-day paid "AIXO Deployment Week"** is the top-of-funnel pilot (not free; target ≥40% convert in 60 days). Engagements list $50K–$400K/mo (launch-discounted for the first ~20 customers in exchange for case studies). BYOK token policy (no markup).
- **North-star metric:** **WPAA** = Weekly Production Agent-Actions (human-approved).
- **Single most diagnostic KPI:** **Graduation Rate** (client engineers operating solo) — target ≥60% of first 10 clients, ≥70% by #20; *"<50% = business model in jeopardy."*
- **Targets:** NRR 140%+, LTV:CAC 30:1+; revenue $6–9M (2026) → $90–130M (2028) → $700M–1.1B (2030); Series A deferred to 2027 at $12–20M ARR. Vertical focus: old-school manufacturing + regulated enterprise (200–5,000 employees), regulated-first (SOC2 → ISO42001 → HIPAA → FedRAMP).
- **#1 governance discipline:** ring-fence the platform from services revenue (the ThoughtWorks/Pivotal cautionary tale) — keep services ≤15–35% of revenue.

## 4. Mission & culture — "the joy of engineering"

The emotional core: AI agents as **true co-developers and partners**, *"not assistants, not autocomplete"* — a force multiplier that *amplifies* human engineers rather than replacing them, and brings back the joy of building. Informed by John's 25+ years as a startup CTO / VP-Engineering running distributed teams of 30–50 developers across 5+ timezones (FinTech, IoT, online advertising, online auctions). The recurring flagship image: **"30 developers across 5 timezones,"** each with AI co-developers who learn the team over decades.

**The named agent cast** (each backed by a *different* frontier model, for genuine cognitive diversity): **@maximus** the Architect (Claude, Stoic/Marcus-Aurelius persona), **@codaramus** the Guardian/QA (a cross-model verifier), **@maxxyscripto / @gemmascripto** the creative frontend (Gemini + Google Stitch — name being revised), **@milton** the documentarian (NotebookLM-grounded, an *Office Space* homage). Agents have self-editing `SOUL.md` files that accumulate expertise over months/years.

> ⚠️ Positioning tension ([`ERRATA.md` E-11/J`](../../ERRATA.md)): the Phase-D positioning doc explicitly **bars** "joy of engineering" and "AI-native" from *enterprise* sales messaging (reserve them for senior-IC blog content), even though they're the mission's heart. Two audiences, two vocabularies.

## 5. Cross-family relationships

- **Separate company from Divia.AI** — but the two share the `_workflows/` development methodology, and **AIXO.Dev Professional (planned) is meant to share a Rust/Tauri desktop foundation with Divia.AI Professional** (shipping). Lessons flow both ways; app/domain layers stay distinct. (See [`ERRATA.md` E-02](../../ERRATA.md) — the AIXO desktop's name/stack is unsettled.)
- **The consultancies are the platform's first customers** — adoption success is defined as "100% of the ExoDev.Pro team."

## 6. Ideation & Exploration (capture everything, commit to nothing)

**From the Phase-D "shock and awe" research (`aixodev-web`):**
- **8 moonshots:** claim the FDSE-platform category; the multi-vendor agent "triumvirate" as a teachable pattern; an FDSE-curated **cross-client DomainGraph** ("we've seen this pattern in 17 similar orgs"); live graph-branch **"decision-as-PR"** for org choices; foundation-model-native graph reasoning; multi-week autonomous project ownership; regulated-industry dominance; cross-org agent-to-agent negotiation.
- **Engagement Receipts** — cryptographically-signed (ed25519) proof bundles of what was delivered in an engagement ("no competitor can ship this within 18 months").
- **The Ontology / knowledge graph** as the platform's strategic core — DomainGraph + ClientDomainGraph + EngagementGraph, modeled on Palantir Foundry (graph-DB choice deferred: Neo4j / Apache AGE / SurrealDB). Bitemporal time-travel over the graph; Code Property Graph security audits (Joern).
- **AIXO MCP server** exposing session data / analytics / project context as MCP tools to any Claude-class agent.

**From aixocode's own bigger-ideas docs:**
- **CollabPair templates as executable institutional knowledge** ("Security Review," "DB-Migration Review" as shareable org-wide 3-phase recipes); the lossless session archive **mined as a knowledge base** ("which steering interventions during CollabPairs actually help? how does an agent's performance change as its SOUL.md grows?"); async human-AI **pair-programming across timezones with checkpoint handoffs** (see [`../USER_STORIES/aixo-agent-dev-team.md`](../USER_STORIES/aixo-agent-dev-team.md)); multi-LLM **"AI-council"** cross-review.

**✦ New this session (venture-level):**
- ✦ **The consulting business as Divia.AI's reference deployment** — run Divia.AI Enterprise *inside* ExoDev.Pro and let every FDSE engagement double as a live Enterprise demo; the two families' GTMs cross-sell.
- ✦ **"Graduation" as a productized ritual** — the moment a client's engineers go solo becomes a tracked, certificate-bearing milestone (an Engagement Receipt variant) and a case-study generator; graduation-rate-as-marketing.
- ✦ **A recurring-agent NOC inside the platform** (LATER-002's "Agent NOC") sold as the operations center for a client's agent fleet — last run, findings, pending approvals, cost, autonomy level per recurring task.
- ✦ **The session archive as the moat that compounds** — position the byte-for-byte preservation guarantee as the thing competitors *can't* retrofit: years of real human+AI development captured losslessly is an irreplaceable training/analytics asset that grows with every engagement.
- ✦ **Open-core wedge** — keep `aixocode` MIT (already true) as the free top-of-funnel that feeds the proprietary platform; an "AIXO.Dev Community" tier could pre-empt an OSS competitor the way the Phase-D competitive research suggests.
