# LATER-004 — Mobile Cross-Platform Strategy (Flutter-first → native v2/v3; the camera/AR substrate split)

- **Captured:** 2026-06-16, MetaProject session (while reframing `fracrealhomes-android` as a long-term 3D product and setting up `diviacontacts-android`)
- **Status:** LATER — a standing strategy + a set of revisit triggers; not a single sprint. Several component parts are mirrored as pointers in the individual repos (see "Where this is mirrored").
- **Spans projects:** `divialife-flutter` / `divialife-android` / `divialife-iOS` (DiviaLife); `diviacontacts-android` / `diviacontacts-gmail` / `diviacontacts-iOS` (DiviaContacts, Divia.AI); `fracrealhomes-flutter` / `fracrealhomes-android` (FracRealHomes).
- **Related:** each repo's `README.md` / `_specs_and_plans/ROADMAP.md`; `_projects/README.md` ("Cross-Project Relationships"); [[techstack-docs-generic-vs-project-specific]]; the generic `_workflows/techstacks/techstack--kotlin_android.md`.

---

## Why this note exists

This consolidates cross-project product-scoping reasoning that would otherwise stay scattered — the kind of thing that, before this MetaProject existed, got lost as a throwaway sidenote with no parallel note in the *other* affected projects to resurface it at the right time. The "QR-code sticker in the storefront window" idea (§4) is the worked example: the *idea itself* turned out to be well-documented — in `kingstrat-adventuregps`'s Divia-platform **federation research** (where the entity-model / federated-identity work lives) — but its **cross-project product placement** (which app owns the AR surface, and why) was never consolidated. **Search-scope lesson:** an earlier `divia*`-scoped search missed it precisely because it lives under KingmakerStrategic, not a `divia*` repo; it took an *all-managed-projects* sweep (2026-06-16) to find it. This note consolidates the strategy + the idea's provenance + its product home so none of it is lost again.

## 1. The pattern: Flutter-first → native v2/v3 (only when warranted)

Several mobile products start as a **cross-platform Flutter app** (one codebase, iOS + Android), and *some* later get **native editions** — Android (Kotlin) and/or iOS (Swift) — rebuilt to optimize for each platform's hardware, UX conventions, and store specifics. The native rebuild is **not automatic**: it's a "v2/v3" investment justified only when real-world usage shows it's worth a second codebase.

- **Divia.Life** (`divialife-flutter`) is the canonical case: built Flutter-first; `divialife-android` (Kotlin) and `divialife-iOS` (Swift) are **deliberate future-parking-areas** (README-only as of 2026-06-16). Realistically it takes **~12–18 months of real-world `divialife-flutter` usage** to even decide whether the specialized native versions are worth building (the Flutter build is "no sacred cows" for its first ~6 months while the product/data model settle).
- **FracRealHomes** follows the same split: `fracrealhomes-flutter` (the listings + co-ownership + management app, cross-platform) plus `fracrealhomes-android` (a *native-now* dedicated app, below).

## 2. The native-now exceptions, and WHY they're native now

Two Android apps are **native Kotlin from the start**, because their core reason for existing targets native-specific hardware/capabilities:

- **`fracrealhomes-android`** — 3D virtual-home **capture & reconstruction** (the Zillow-3D-Home equivalent): camera/AR/3D-reconstruction is the whole point.
- **`diviacontacts-android`** — the DiviaContacts mobile reader/viewer **and** the venture's experimental substrate for **AR storefront-discovery** (see §3).

## 3. The product-scoping insight (John's "101 requirements / puzzle pieces")

Flutter *can* access the camera — so this is **not** a hard technical constraint, and simple camera features may well live in the Flutter apps too. The skew comes from two softer-but-real forces that make us deliberately **scope camera/AR-heavy experimentation to the app where it fits best**:

1. **Native hardware access** — a native Kotlin app has the most direct access to camera/AR/3D hardware (ARCore, Camera2, depth, etc.).
2. **Google Play permission/performance profile** — a completely separate concern from technical capability. `diviacontacts-android` is a Contacts/CRM app that **already requires higher-threshold Play permissions** (Call Log, SMS/MMS, Contacts). Adding camera/AR there does **not** push its permission/performance profile to a new extreme. Putting the same AR experimentation into a **Flutter messaging app like Divia.Life** *would* skew that app to a permission/perf extreme — for a feature most Divia.Life users would rarely touch.

So `diviacontacts-android` is the right **experimental substrate** for AR, and `fracrealhomes-android` for 3D capture — and the learnings transfer to the eventual Divia.Life native builds (§5).

## 4. The "QR-code sticker in the storefront window" idea (provenance: kingstrat federation research)

**Where it's documented (found 2026-06-16):** the idea lives in **`kingstrat-adventuregps`** — `_specs_and_plans/phase_00--ideation_and_research/DIVIA_PLATFORM_VISION_AND_FEDERATION.md` **§5 "The identity-link surface"**, grounded technically in `_specs_and_plans/_research/entity_model_and_graph_db/analysis-43--federated-identity-registry-models.md` **§4**. It was worked out there because that repo hosts the Divia-platform entity-model / federated-identity research — so it's *not* under Divia.Life or DiviaContacts (which answers John's open question), though the original note already leaned to DiviaContacts (below).

**The idea (gist).** §5 names four **identity-link surfaces**, all riding on one federated identity (a mutable human handle → a permanent registry UUID):
- **`divia.me/{handle}`** — a Linktree-style personal identity URL.
- **`Divia.Network/{company}/{location}` shop-window QR** — a Divia.Network-branded **QR sticker in a shop window** resolving to that exact store's location URL.
- **business-card QR** — a QR serving **machine-readable, continuously-updated** contact JSON ("no more pen-struck-out phone numbers"; John intends to early-adopt later in 2026).
- **AR overlay (a "later, fun feature")** — verbatim *"likely in a **DiviaContacts** mobile app (maybe also a consumer **Divia.Life** app if fun enough)"*: point your phone camera at the street → it overlays the correct `Divia.Network` links on the stores you see, via **GPS + compass + light OCR of store names — even for shops without a QR sticker.**

So the AR overlay was **already flagged for DiviaContacts** (Divia.Life a maybe), corroborating the placement below.

**Technical grounding (analysis-43 §4):** the shop-window QR is a **dynamic QR** (encodes a *stable URL*, not raw data → reprint never needed), following GS1-GLN / Handle prefix-delegation (`Divia.Network/{company}/{location}`; the company owns its sub-namespace); endpoints serve a `did:web` document + **signed Verifiable Credentials** with **selective disclosure** (public-by-default, more-on-consent).

**Product placement (this note's addition):** the **AR storefront-discovery surface** is owned by **`diviacontacts-android`** — DiviaContacts' core job is *resolving People, **Places**, and Companies to PKMS/Divia.Network entities*, and the AR view extends that from the inbox to the physical world. Its detailed AR option-space (which now cites this provenance) lives in `diviacontacts-android`'s `ROADMAP.md` as Phase-01-experimental.

> Terminology caution: "Divia.Network" is overloaded — in `DOMAIN_MAPPINGS.md` `divia.network` is a tutorials/training microsite; in the fan-out user story it's the open integration layer/protocol; in the federation research (and here) **`Divia.Network/{company}/{location}`** is the **Global Registry of public Place/Company identities**. Reconcile these senses when the registry is actually scoped.

## 5. The convergence (why the experiments matter beyond their own apps)

Camera/AR/3D hardware learnings **and real usage data** from `diviacontacts-android` (AR) and `fracrealhomes-android` (3D) become the **evidence base** for deciding and building the eventual native **`divialife-android`** (Kotlin) and **`divialife-iOS`** (Swift) v2/v3 editions — and for scoping them per platform (the iOS edition would lean on Apple's stack: ARKit, RoomPlan, etc.). One venture's native spike de-risks another venture's native rebuild.

## Where this is mirrored (parallel pointers, so it resurfaces in context)

- `divialife-android/README.md`, `divialife-iOS/README.md` — the "future-parking-area / Flutter-first / ~12–18 months" framing + the camera/AR-learnings-feed-here note.
- `diviacontacts-android` — README/ROADMAP (the AR storefront-discovery option-space + the "why AR lives here" rationale) + a `_horizon_LATER.md` pointer to this note.
- `fracrealhomes-android/_specs_and_plans/_backlog/_horizon_LATER.md` — pointer: its 3D/camera learnings feed the Divia.Life native v2/v3 decision.
- `divialife-flutter/_specs_and_plans/_backlog/_horizon_LATER.md` — pointer: the ~12–18-month-usage trigger for deciding on native editions.
- `_projects/README.md` — "Cross-Project Relationships" paragraph (condensed).

## Revisit triggers

- **`divialife-flutter` reaches ~12–18 months of real-world usage** → evaluate whether native `divialife-android` / `divialife-iOS` editions are warranted (and with what scope).
- **`diviacontacts-android` and/or `fracrealhomes-android` complete their Phase-01 camera/AR/3D spikes** → harvest the hardware lessons + usage data as input to the Divia.Life native decision, and promote any reusable Android findings into the shared `techstack--kotlin_android.md`.
- **The Divia.Network Global Registry gets scoped** → flesh out the QR-sticker / storefront-identity mechanism and reconcile the overloaded "Divia.Network" terminology.
