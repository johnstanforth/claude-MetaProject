# Brief (Business) — DiviaCards (Divia.AI Semantic Smart Cards)

> **Business-side brief** → the **business knowledgebase** (companies / open standards / brands / GTM / domains / downstream consumers). Self-contained (domains + cross-refs pulled in). Its **software-dev facet** (the `divia_cards` repo · the card-type vocabulary/schema · Web-Components compilation · techstack) is the paired **[engineering brief](../../../SOFTWARE_DEV/divia_cards.md)**. Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. *(Replaces the old single-file `divia_cards.md`; all still-valid content migrated below, engineering content moved to the paired engineering brief.)*

## Identity

| Field | Value |
|---|---|
| **Standard (full)** | Divia.AI Semantic Smart Cards |
| **Wordmark / short** | **DiviaCards** |
| **Token shape** | `DiviaCard::<Producer>::<type>` (e.g. `DiviaCard::PatternicityNews::article`) — a namespaced, cross-app structured-type vocabulary that producer apps post and consumer apps render. |
| **One-line** | The ecosystem-wide vocabulary of typed content "cards" — the shared data-interchange/registry types that any Divia.AI (or partner) app can post, and any app can render identically. |
| **Status** | 🟢 **Active.** |

## Company / corporate structure · Brands

- **Owning venture / steward:** **Divia.AI, Inc.** (the personal-knowledge & life-organization ecosystem). DiviaCards is one of that venture's offerings — see the venture brief [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **Modeled as:** in the domain map, DiviaCards is a **"Project / Open Standard"** under Divia.AI (sibling to Divia.Network and the DiviaContacts product line), *not* a subsidiary LLC. It is its own umbrella in `PRODUCTS/DiviaCards/` because the term spans the whole ecosystem and is consumed cross-venture.
- **Brands:** standard name = *Divia.AI Semantic Smart Cards*; everyday wordmark = *DiviaCards*; the per-instance type token is *`DiviaCard`* (singular) in `DiviaCard::Producer::type` form.

## Product Lines → Products

- **Product Line:** the ecosystem's shared content-interchange standard — **the typed content-block unit** ("everything is a DiviaCard"). Two facets of the *same* name, which the ecosystem has **never formally reconciled** (see ERRATA below):
  - **(a) The vocabulary / open standard** — the namespaced cross-app data-interchange & registry types (`DiviaCard::Producer::type`) that producer apps publish and consumer apps consume. This is the forward-looking, ecosystem-wide concept.
  - **(b) The rendering layer** — the original `divia_cards` app that coined the name: typed text inputs rendered as framework-agnostic Web Components (the technical asset that *could* become the standard's rendering layer). Engineering detail → the [engineering brief](../../../SOFTWARE_DEV/divia_cards.md).
- Shared ecosystem vocabulary DiviaCards sits beside: **`.dvai`** (the SQLite Divia Document Format), the **Activity Log** (NL capture inbox), and **PKMS** (the personal-knowledge store). DiviaCards is the **typed content-block unit** within all of these.

## Downstream consumers (forward-references — detailed in their own briefs)

DiviaCards is consumed **cross-venture**; it is a vocabulary other products depend on, not a standalone app a user "uses." Recorded here as forward-pointers only — these ventures get their own briefs later:

- **PatternicityNews / PatternicitySocial** *(Patternicity venture)* — PatternicitySocial is *"a social network similar to X.com, Bluesky, or Mastodon, with full support for the DiviaCards open standard so users can post and discuss Patternicity News articles as structured `DiviaCard::PatternicityNews::article` elements"* (from `DOMAIN_MAPPINGS.md`). **The headline future consumer.**
- **LegendaryMoney** *(Divia.AI ecosystem)* — its v2 vision publishes `DiviaCard::LegendaryMoney::transaction(...)` to a "global DiviaCards registry" (the data-concept facet; see ERRATA E-05).
- **Divia.AI Professional** — its BRANDING doc names DiviaCards as the desktop's owned content type (`.dvai` + DiviaCards).
- **The Divia.Network fan-out** — a single NL capture lands as a natural-language DiviaCard in the Activity Log, then an agent fans its meaning out across products. DiviaCards is the carrier unit of that story (see [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md)).

## Go-to-market / strategic role

DiviaCards is **infrastructure, not a sold product** — its GTM value is as the **interoperability spine** that makes "an ecosystem, not an app" self-evident. The pitch: *one card definition renders identically everywhere* — Divia.AI Professional (SvelteKit), DiviaHome (Flask/Jinja), Divia.Life (Flutter via webview), Gmail (DiviaContacts) — delivering the *"everything is a DiviaCard, everywhere"* promise. Aspirational ideation (capture-only) includes a **community DiviaCard marketplace** of iframe-sandboxed "Notion-block-with-CSS" mini-apps and a parallel **`.dvai-open`** (JSON+Markdown) interchange format for lock-in avoidance.

## Product Version-Releases

Pre-release as an *open standard* (no published versioned spec). The *rendering-layer app* `divia_cards` is itself fully built (the npm sub-package is at `0.1.0`) but the standard/vocabulary it implies is unversioned. When releases exist they follow the model's **immutable-past / flexible-future** rule (past = git-matched record; future = a movable "marketing sketch" re-bucketable like kanban cards). *(Build-side stages/phases → the [engineering brief](../../../SOFTWARE_DEV/divia_cards.md).)*

## Domains (self-contained — from `DOMAIN_LIST.md` / `DOMAIN_MAPPINGS.md`)

- **Canonical:** **`divia.cards`** (the open-standard home).
- **Redirects/aliases → `divia.cards`:** **`diviacards.com`**, **`diviasmartcards.com`**.
- *(All registered via Spaceship.com; `diviacards.com` since Mar 2022, `divia.cards` and `diviasmartcards.com` since May 2023.)*

## Ideation & Exploration (capture everything, commit to nothing)

*(Migrated from the predecessor brief — business/standard-level ideas; build-side ideas moved to the engineering brief.)*

- ✦ **DiviaCards as iframe-sandboxed mini-apps** — a "Notion block with CSS + optional JS/TS," a community-contributed **DiviaCard marketplace**, and a parallel **`.dvai-open`** (JSON+Markdown) format for lock-in avoidance / git-diff / interop (OPML, JSON Canvas, etc.). *(From the Divia.AI BRANDING / vision docs.)*
- ✦ **The reconciliation decision (the open business question):** is the `divia_cards` app the **rendering layer for the ecosystem DiviaCard standard**, or a separately-named thing? If the former, the Web-Components-compilation approach is a real asset — one card definition renders identically across every surface, exactly the "everything is a DiviaCard, everywhere" promise.
- ✦ **The NL capture card as ecosystem primitive** — the rendering layer's `nlp_input` card is *already* the Activity-Log NL-capture unit; wiring it to the Divia.Network fan-out is the same "SMS-to-self → classify later" problem LegendaryMoney / DiviaHome describe.

## Status

🟢 **Active** (the vocabulary/standard is a live, cross-venture concept). **Licensing (business view):** the *standard/vocabulary* has no published license of its own; the *rendering-layer app* `divia_cards` carries an MIT Web-Components sub-package over an otherwise-undocumented root (engine-license detail → the [engineering brief](../../../SOFTWARE_DEV/divia_cards.md)). **Open reconciliation:** the term **"DiviaCard" is overloaded** — a local UI-widget meaning (the app) vs. a cross-app data-interchange/registry-type meaning (the standard); the two **have never been reconciled or wired together** (see ERRATA). This brief treats DiviaCards-the-standard as the primary entity and `divia_cards`-the-app as its name-source / candidate rendering layer.

> ⚠️ **ERRATA ([`../../../ERRATA.md` E-04 / E-05](../../../ERRATA.md)):** **E-04** — the old `_projects/README.md` index calls `divia_cards` an "early prototype"; it is actually a fully-built, tested app (Nov 2025; built by Factory.ai's "droid," Gemini-3-Pro-reviewed). **E-05** — "DiviaCard" means two unrelated things (local UI widget vs. cross-app registry type); the app predates the ecosystem framing, contains no registry/namespacing, and isn't referenced by any sibling repo. *(Detail in the engineering brief.)*

## Cross-references

- Paired engineering brief: [`../../../SOFTWARE_DEV/divia_cards.md`](../../../SOFTWARE_DEV/divia_cards.md).
- Owning venture: [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- Fan-out user story (DiviaCards as carrier unit): [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md).
- Discrepancies: [`../../../ERRATA.md`](../../../ERRATA.md) (E-04 status · E-05 name overload).
