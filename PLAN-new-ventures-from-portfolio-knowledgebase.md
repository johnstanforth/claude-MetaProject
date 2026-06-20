# PLAN — Bootstrapping the Portfolio Knowledgebase & Reasoning About Two New Ventures

> Working plan (2026-06-20). Pairs with the canonical structural model in **[`_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`](_REFERENCE/PROJECT-ORGANIZATION-MODEL.md)** (which captures the *hierarchy*); this doc holds the *method + sequence*. Together: "full big-picture reference doc + detailed plan doc."
>
> **Status note:** the model doc still needs a revision pass (the reconciled hierarchy below + the new Build-Profile dimension); held until the dimension's name is picked, then revised in one clean pass. This plan doc uses the *reconciled* hierarchy already.

## The core idea — markdown briefs as the graph-DB bootstrap dataset

Everything written into these briefs is **both** the initial dataset **and** the design-thinking draft for the future KSVGPS graph-DB. Exactly like our `_workflows` evolved over months of iteration before we'd formalize them, these briefs are the draft-version of the representations we'll soon model in the graph-DB. Therefore: **isolate each concept as cleanly as possible** — each Product, Build Line, Build Profile, Stage as a distinct, well-bounded section — because *every statement here must be modeled accurately in the graph-DB prototype later*. The briefs are a deliberate **poor-man's stand-in for the scoped projections** the graph-DB will eventually serve on demand.

## The structural model (reconciled 2026-06-20)

The corrected hierarchy (supersedes the model doc's earlier "Product Line = version sequence"):

```
Company / Venture
 ├─ corporate structure · Brands
 └─ Product Lines        (families of related products — standard meaning)
     └─ Products         (individual offerings)
         ├─ public Version history  (v1.0 … vN.0 — the "moving symlink" across Build Lines)
         └─ Build Lines  (the 3-part engineering codebases that deliver the Product)
             ├─ Build Profile        ← NEW independent dimension (see below)
             ├─ Triangulation Target (per Build Line — the far destination)
             └─ Stages   (Build-Line-local milestones; public Stages → the Product's Versions)
                 └─ Phases → Sprints  (existing execution machinery, unchanged)
Features = graph nodes throughout (Requester-Source · Build Line · target Version · dealbreaker-flag · typed relations)
```

**The new independent dimension — `Build Profile`** *(working name; pending the pick from the options in the cover note)*: a **per-venture, reusable** definition of *the engineering scale/scope/stack a thing is built FOR* — e.g. `Build Profile "Seed": 6 mo · ~20-person startup · 5–7-person dev team · Python/Flask`. It is **decoupled from Build Lines** (a Build Line in one venture and another won't share a Profile), **copy-on-write across projects** (like pulling `_workflows` into a new repo, then adapting), the **explicit context handed to Codex** so it designs *for that level* (not IANA-grade enterprise), and the **home for techstack standardization + continuous improvement** (e.g. a future "move the Flask+FastAPI tier to async Quart?" research, validated once and propagated to every project on that Profile). Pairs as two axes: **Triangulation Target (where we're going) × Build Profile (at what scale we build now).**

## The briefs — structure + principles

- **Self-contained per Product/Venture.** Each brief carries *everything* needed to reason about that project — including its **domains + cross-references/relationships pulled in from `DOMAIN_LIST`/`DOMAIN_MAPPINGS`** — so a tightly-scoped "reason about these 3 projects" discussion never has to parse the portfolio-wide files to extract a few bits. (Redundancy with `DOMAIN_*` is intentional and fine.)
- **Clean internal isolation** — each concept a bounded section, so it maps 1:1 to a graph-DB node/edge later.
- **Home:** enrich the existing `_REFERENCE/ULTIMATE_VISION/PRODUCTS/<Umbrella>/<product>.md` + `VENTURES/` briefs to this detail (extend, don't duplicate), plus a README-style **index/inventory**. *(Recommended over a separate `BUILD_LINES/` subdir, which would re-fragment the scope-ability we're after; final call at step ②.)*
- **The endpoint:** these prototype the scoped projections; eventually a **SKILL** tells the LLM exactly how to query the graph-DB for "the techstack from here, the GTM strategy from there," retiring the makeshift markdown.

## The shared-substrate reasoning (the actual test)

The pattern: **Divia.AI Enterprise server (the graph-DB core)** → **KSVGPS** (client implementation + knowledgebase) → **other venture clients** (PatternicityNews, CrowdMadness) building on the *same* graph-DB techstack/capabilities, each with a *different scope*. (See [`_REFERENCE/ARCHITECTURE_CONVERGENCE.md`](_REFERENCE/ARCHITECTURE_CONVERGENCE.md).) Per venture, the reasoning exercise is: *"what does it need from the graph-DB techstack + knowledgebase, and how does its scope differ from KSVGPS?"* — done by handing the LLM a small set of **self-contained briefs**, never the whole portfolio.

## The two target ventures (seed capture — full briefs come in step ④)

### PatternicityNews — `PatternicityNews LLC` (~5-person startup)
- **Products:** **PatternicityNews** (news website/portal app/service) + **PatternicityNews Reader** (desktop app; *same techstack as Divia.AI Professional, later AIXO.Dev Professional*). Later: **PatternicitySocial** (an X.com-like network to post/discuss news, supporting PatternicityNews-defined **`DiviaCard`** structured types — each card type carries embedded/interactive functionality).
- **Domains:** `Patternicity*` (incl. `Patternicity.AI`) + all `ptn-link*` (a URL-shortener: unique reference links generated when users share articles, to track sharing).
- **Core tech:** built on the graph-DB knowledgebase substrate. The ongoing investment is **parsing + NER (Named Entity Recognition)** with leading/bleeding-edge tech (LLM *and* otherwise), modeling **every person/place/company/etc. in every news article** via the graph-DB's complex relationships.
- **Primary data source:** download the **Wikipedia static dump + periodic update releases** → maintain an internal copy → parse + model in the graph-DB + **prime NER** starting from the Wikipedia dataset.
- **Data-architecture concerns to design carefully:** **topic-hubs** — for graph modeling (likely *dozens* of graphs/clusters with vertices between them — TBD), and **especially for vector search**: segment topic-searches so vector distance is meaningful *within* a topic (better accuracy finding sub-sub-subtopics), rather than treating "everything about Canada" as the same distance from "everything about horses."

### CrowdMadness
- A **reboot of MobThought** — the prediction-market game some of the team built ~2004–2008. Like Polymarket/Kalshi, but **intended as a game** (massively-scalable web app/service). Gamified mechanics are **TBD/placeholder** for today.
- **Why it's here:** it's the second case for the cross-venture reasoning test — *"like Project A, but with the techstack from Project B, plus ideas from KSVGPS"* — proving the LLM can reason over facts **across** ventures **without** reading the 500-page every-project U_V Guide first.

## The sequence

1. **Align** this plan doc + the model doc (pick the Build-Profile name; confirm the hierarchy + briefs structure).
2. **Enrich/build the substrate briefs** — the relevant existing entities (Divia.AI Enterprise / the graph-DB core, KSVGPS, Divia.AI Professional, etc.), self-contained, to the model's detail.
3. **Reason** about the two new ventures against that substrate (graph-DB needs; how each scope differs from KSVGPS).
4. **Write** the two venture briefs (PatternicityNews, CrowdMadness) — self-contained, domains/cross-refs pulled in.
5. **Breadth-first** to imagine each venture's Phase-00 research topics.
6. **Sequence** the topics.
7. **Run** the first topic through the new **multiagent research workflow** (the live test).

## Open items to settle (step 1)

- **Build-Profile name** — pick from the 5–7 options.
- **Briefs structure** — confirm self-contained-per-Product briefs + index (vs. a `BUILD_LINES/` subdir).
- **Substrate scope** — which existing entities need briefs *first* to reason about PatternicityNews + CrowdMadness (likely: the Divia.AI Enterprise graph-DB core, KSVGPS, Divia.AI Professional).
