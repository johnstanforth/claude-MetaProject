# Brief (Business) — Patternicity / PatternicityNews  ·  **INTRO BRIEF (partial)**

> **Business-side brief** → the **KSVGPS business knowledgebase**. Self-contained (domains pulled in). Paired **[engineering brief](../../../SOFTWARE_DEV/patternicity.md)**. **INTRO BRIEF (2026-06-21):** a *partial* draft per the [new-venture intro-brief workflow](../../../../_workflows/workflow_new_venture_intro_brief.md) — each section is **"what we know / infer"** (cited; `TBD` for gaps; *Inference:* labels) followed by **❓ Additional Questions for John** inline. No-invention: only sourced facts. Sources swept: MetaProject `_REFERENCE/` (`DOMAIN_LIST`/`DOMAIN_MAPPINGS`/`DOMAIN_WISHLIST`, the analysis docs, sibling briefs) + the `kingstrat-adventuregps` repo.

## Identity

**What we know / infer**
- **Company / venture:** `Patternicity.AI, LLC` (`DOMAIN_MAPPINGS.md`; listed as an `Organization / Venture` in `kingstrat-adventuregps/.../ENTITY_MODEL_DRAFT_SPEC.md`). Sized a **"~5-person startup"** (`PLAN…`).
- **Flagship product:** **PatternicityNews** — a "news website/portal" (`DOMAIN_MAPPINGS.md`).
- *Inference:* "**Patternicity**" is Michael Shermer's coined term — the human tendency to find meaningful patterns in noise — which fits a news/pattern-finding venture. **Sources do not state the etymology or any framing metaphor.**
- One-line / tagline: **TBD**.

**❓ Additional Questions for John**
1. What's the one-sentence "what Patternicity is" you'd give an investor? Is the **parent brand** "Patternicity" with PatternicityNews as its flagship product — or is PatternicityNews effectively the venture's whole identity?
2. Is the Shermer "patternicity" meaning the intended namesake / brand story? Is there a framing metaphor (the way KSVGPS uses GPS / air-traffic-control)?
3. Why this name for a *news* company specifically — is "finding the patterns across the news" the core product thesis (i.e. the entity-graph *is* the product), or just an evocative name?

## Company / corporate structure · Brands

**What we know / infer**
- Patternicity.AI, LLC sits under the **"Venture Studio Portfolio Companies"** heading in `DOMAIN_MAPPINGS.md` — a flat list with **no parent entity**, alongside LegendaryMoney, TastyPal, FracRealHomes, SensoryMQ, etc. It is **NOT** under the Divia.AI or ExoDev families.
- **Brand family** (from `DOMAIN_MAPPINGS.md`): apex **Patternicity.AI**; products **PatternicityNews**, **PatternicityNews Professional / Reader**, **Patternicity ONE**, **PatternicityWTF / WeighTheFacts**, **PatternicitySocial**, **Patternicity URL Shortener**, **Patternicity Bet**.
- Jurisdiction (DE/TX/AZ…), founding date, PBC/nonprofit status, headcount beyond "~5": **TBD — not found in sources.**

**❓ Additional Questions for John**
4. Is Patternicity.AI, LLC truly **standalone**, or does it belong under an umbrella (a Patternicity holdco, or the Kingmaker venture-studio side that "owns" your early ventures)?
5. It consumes Divia.AI tech (the graph-DB core, DiviaCards, and the Divia.AI Professional desktop stack). Is there an intended **commercial/ownership** relationship with Divia.AI, or purely a **tech-client** relationship like KSVGPS?
6. Of {ONE, WTF/WeighTheFacts, Bet, the URL shortener} — which are **first-class products**, which are **features** of the news product, and which are **sub-brands**? (The sources list them flatly as "Product/Service" entries.)

## Product Lines → Products

**What we know / infer** (all from `DOMAIN_MAPPINGS.md` unless noted)
- **PatternicityNews** — the news portal (`patternicity.news`).
- **PatternicityNews Professional = the Reader** — a "cross-platform desktop **RSS-newsreader**" at `patternicity.news/rssnewsreader/` (front `patternicity.pro`). **Slated to share Divia.AI Professional's exact Rust/Tauri/SvelteKit desktop stack** (`SOFTWARE_DEV/divia_ai-professional.md`) — *stated intent, not yet code*.
- **Patternicity ONE** — "monthly subscription for **bundles of premium/paid news sites** such as NYT and WaPo" (`patternicity.one` → `/subscriptions/`).
- **PatternicityWTF / WeighTheFacts** — a web service that "constructs **chain-of-thought arguments with cross-referenced news evidence**"; *secondary use* = an **AI-generated YouTube channel** for a **20–30-year-old** audience, "irreverent but evidence-driven," presenting **both sides of the political aisle** (`patternicity.news/WeighTheFacts/`, front `patternicity.wtf`).
- **PatternicitySocial** — an **X/Bluesky/Mastodon-like** social network with "full support for the **DiviaCards open standard**" so users post/discuss articles as **`DiviaCard::PatternicityNews::article`** elements (`patternicity.social`). The DiviaCards "headline future consumer."
- **Patternicity URL Shortener** — under Social; `ptnws.link`; "unique links **tracking article-sharing**."
- **Patternicity Bet** — `patternicity.bet`. **Has a domain and ZERO descriptive text in any source.**

**❓ Additional Questions for John**
7. **PatternicityNews v1** — is it an aggregator (Ground-News-style), an original-analysis outlet, or a **graph-of-the-news explorer**? What's the single thing it does that nothing else does?
8. **WTF / WeighTheFacts** — is this a consumer-facing debate/reasoning tool, or an internal **credibility-scoring / argument engine** that powers the news product (or both)? Is the AI-generated YouTube channel a real GTM channel or an experiment?
9. ⭐ **Patternicity Bet** — what is it? *Inference (mine, unconfirmed by any source):* a prediction-market tie-in — possibly **CrowdMadness embedded in the news product** ("bet on this headline's outcome"). The dossier is explicit that nothing links Bet to CrowdMadness — so: is Bet (a) CrowdMadness-in-the-news, (b) a sports-betting affiliate, (c) a lightweight engagement feature, or (d) something else?
10. **Patternicity ONE** — is "reselling bundled NYT/WaPo access" a real licensing model you intend to pursue, or a placeholder? What does ONE actually bundle (ad-free + Reader + Social + premium passthrough)?
11. Is there a product I'm missing — e.g. a B2B **entity-intelligence / API** product built directly on the news graph?

## Product Version-Releases

**What we know / infer**
- Pre-release; **idea-only**; no version numbers assigned. (Once releases exist, the immutable-past / movable-future "marketing sketch" rule applies.)

**❓ Additional Questions for John**
12. Which product ships **first** (the portal? the Reader?), and what's the rough **dated** sketch (e.g. v1 portal ~2027)? Which are explicitly "**v3+ / someday**" products (Social? Bet?)?
13. Working backward from a far Target — what does "Patternicity at its full vision" look like, and roughly when?

## Target market / GTM / monetization

**What we know / infer**
- Monetization signals: **ONE = subscription**; **WTF** targets 20–30-year-olds with a YouTube channel; the **shortener = sharing attribution**; "~5-person startup."
- Formal GTM / pricing / market-sizing / competitive positioning: **TBD — not found.**

**❓ Additional Questions for John**
14. Who is the **core reader/user**, and what's the wedge vs. Ground News, AllSides, Google News, Perplexity, Apple News?
15. What's the **monetization mix**, and the **primary** at v1 (subscription / ads / a B2B data-or-API product off the entity graph / Bet)?
16. Is the **entity graph itself** a sellable product (B2B data/API), or strictly the engine behind the consumer surfaces?

## Domains (self-contained — from `DOMAIN_LIST.md` + `DOMAIN_MAPPINGS.md`, registrar Spaceship.com)

**What we know / infer**
- **Apex / company:** `patternicity.ai` (reg 2023-05-04) → aliases `patternicityai.com`, `patterncityai.com` (typo), `ptn-ai.com`, plus `.app/.blog/.buzz/.cc/.fun/.life/.live/.net/.network`.
- **News:** `patternicity.news` (2023-05-04) → `patternicitynews.com`, `ptnws.com`.
- **Reader (Professional):** front `patternicity.pro` → `patternicity.news/rssnewsreader/`.
- **ONE:** `patternicity.one` → `/subscriptions/`. **WTF:** `patternicity.wtf` → `/WeighTheFacts/`. **Social:** `patternicity.social` (2023-05-04) → `patternicitysocial.com`, `patternicity.chat`. **Shortener:** `ptnws.link` (2025-09-02) → `patternicity.click`, `patternicity.link`, `ptn-ai.link`. **Bet:** `patternicity.bet` (2026-03-04).
- **BUY-DOMAIN target:** `patternicity.com` — **available at $3,195 via HugeDomains** (`DOMAIN_WISHLIST.md`).
- Note: the PLAN's `ptn-link*` is **not** an owned domain (the real shorteners are `ptnws.link` / `ptn-ai.link`).

**❓ Additional Questions for John**
17. Is **`patternicity.com` ($3,195)** a priority buy? Which domain is the **canonical front** — `patternicity.ai`, `patternicity.news`, or (eventually) `patternicity.com`?

## Venture origin, people & external dependencies  *(venture-studio facets — new this round)*

**What we know / infer**
- **Nothing** in the sources about the idea's origin, the people, or the gating external dependencies. (The domains' 2023 registration is the earliest hard signal that the idea was live by then.)

**❓ Additional Questions for John**
18. **When did the Patternicity idea first occur to you**, and how long has it lived in your head? Any **predecessor / earlier name** lineage (the MobThought→CrowdMadness pattern)?
19. **Who would you build this with** — co-founders, the ~5 people, any advisors or would-be partners already in the picture?
20. ⭐ **External dependencies an autonomous agent should track:** news-publisher licensing/ToS (for aggregation + the ONE bundle), **Wikipedia/Wikidata licensing** (the NER source — already logged as `[Backlog:RESEARCH] R-001`), platform risk (YouTube for WTF; X/Bluesky/ActivityPub interop for Social), and any regulatory angle for Bet. Which of these are **gating / blocking**?
21. **Why is Patternicity feasible NOW** when it wasn't before — what does LLM economics unlock here (NER at scale? AI-generated WTF video? cheap entity-resolution)? *(This is the "why now" the venture-studio reframing wants captured.)*

## Status

**What we know / infer**
- **idea-only** (`PLAN…`). Domains registered 2023 (anchors), 2025 (shorteners), 2026 (gTLD expansion). **No repo; no prior brief** (this is the first). License: **TBD**.

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/patternicity.md`](../../../SOFTWARE_DEV/patternicity.md).
- Consumes: DiviaCards ([`../DiviaCards/divia_cards.md`](../DiviaCards/divia_cards.md)) · the Divia.AI Professional stack ([`../DiviaAI/divia_ai-professional.md`](../DiviaAI/divia_ai-professional.md)) · the Divia.AI Enterprise graph-DB core ([`../DiviaAI/divia_ai-enterprise.md`](../DiviaAI/divia_ai-enterprise.md)).
- Workflow + model: [`../../../../_workflows/workflow_new_venture_intro_brief.md`](../../../../_workflows/workflow_new_venture_intro_brief.md) · [`../../../PROJECT-ORGANIZATION-MODEL.md`](../../../PROJECT-ORGANIZATION-MODEL.md).
