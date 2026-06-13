# Product — DiviaCards (divia_cards)

> A Flask + Svelte app that renders typed text inputs as **"cards," compiled to framework-agnostic
> Web Components.** Surprise finding: it's a **fully-built, working app** — but its "DiviaCard" is a
> local UI-widget concept, not (yet) wired to the ecosystem-wide DiviaCard data concept.

- **Repo:** `divia_cards` · npm `divia-cards` (publishable Web Components) + `divia-cards-frontend` (SvelteKit app).
- **Umbrella:** DiviaCards · **License:** root **Undocumented**; the `web-components/` sub-package is **MIT**.
- **Status:** 🟢 **Fully built & working** (Nov 2025; built by Factory.ai's "droid," Gemini-3-Pro-reviewed; 5 phases; 25 backend tests). Currently dormant.

---

## What it is (consensus)
A Flask backend (app-factory, User + Card models, JWT auth, SocketIO, validators) + a SvelteKit frontend that accepts free-text inputs and renders each as a structured **card** (newest on top), with real-time WebSocket updates and JWT multi-user auth. The signature move: **Svelte 5 card components compiled to framework-agnostic Web Components** (Custom Elements + Shadow DOM), with working **Vue 3 + React 18** demo apps. Three card types — **Outline** (hierarchical), **NLP_Input** (a single text string = "what was previously sent via SMS"), **Event** (name/desc/location/time/attendees). Origin: replace John's "makeshift prototype where I just SMS myself." A deliberate **vanilla-CSS + 3-tier design-token** architecture (chosen over Tailwind because CSS custom properties pierce Shadow DOM). Known gaps: Web Components are read-only; JWT blocklist is in-memory.

> ⚠️ **Two ERRATA items ([`../../ERRATA.md` E-04/E-05`](../../ERRATA.md)):** (1) the index calls this an "early prototype (PLAN + PLAN-v2)" — it's actually a complete, tested app. (2) **"DiviaCard" is overloaded** — here it's a *local UI widget*; in the ecosystem (Professional's BRANDING + LegendaryMoney's v2 vision) it's a *cross-app data-interchange/registry type* (`DiviaCard::LegendaryMoney::transaction`). `divia_cards` predates the ecosystem framing, contains no registry/namespacing, and isn't referenced by any sibling repo. Built on a non-Claude/non-aixodev toolchain (droid + Gemini). **Best read: the original rendering layer & name-source; never reconciled with the ecosystem data concept.**

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo (future phases):** card-type conversion logic; NLP processing for NLP_Input cards; user prefs; card search/filtering; export/import; a mobile app reusing the same Web Components; editable Web Components; `::part()`/`:host`/Constructable-Stylesheets external theming; auto dark-mode.
- ✦ **New (the reconciliation decision):** is `divia_cards` the **rendering layer for the ecosystem DiviaCard**, or a separately-named thing? If the former, it's a real asset — the Web-Components-compilation approach means one card definition renders identically in Divia.AI Professional (SvelteKit), DiviaHome (Flask/Jinja), Divia.Life (Flutter via webview), and Gmail (DiviaContacts) — exactly the "everything is a DiviaCard, everywhere" promise. The NLP_Input card is *already* the Activity-Log capture primitive. ✦ Wire its `nlp_input` card to the Divia.Network fan-out pipeline (it's the same "SMS-to-self → classify later" problem LegendaryMoney/DiviaHome describe). ✦ Decide the toolchain-lineage question — it's the one repo built outside the Claude/aixodev workflow system; either fold it in or consciously keep it as an independent experiment.
