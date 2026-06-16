# LATER-004 — Mobile Cross-Platform Strategy (Flutter-first → native v2/v3; the camera/AR substrate split)

- **Captured:** 2026-06-16, MetaProject session (while reframing `fracrealhomes-android` as a long-term 3D product and setting up `diviacontacts-android`)
- **Status:** LATER — a standing strategy + a set of revisit triggers; not a single sprint. Several component parts are mirrored as pointers in the individual repos (see "Where this is mirrored").
- **Spans projects:** `divialife-flutter` / `divialife-android` / `divialife-iOS` (DiviaLife); `diviacontacts-android` / `diviacontacts-gmail` / `diviacontacts-iOS` (DiviaContacts, Divia.AI); `fracrealhomes-flutter` / `fracrealhomes-android` (FracRealHomes).
- **Related:** each repo's `README.md` / `_specs_and_plans/ROADMAP.md`; `_projects/README.md` ("Cross-Project Relationships"); [[techstack-docs-generic-vs-project-specific]]; the generic `_workflows/techstacks/techstack--kotlin_android.md`.

---

## Why this note exists

This is exactly the kind of cross-project product-scoping reasoning that, before this MetaProject existed, got lost as a throwaway sidenote inside one project's conversation — with no parallel note in the *other* affected projects to resurface it when the time was right. The "QR-code sticker in the storefront window" idea below is a concrete casualty: it had been discussed but was **written down nowhere** (a full read of `_REFERENCE/` confirmed it's absent — the only QR/registry hits were unrelated: TXFR's file-transfer QR codes and the DiviaCards "global registry"), and John couldn't recall whether it had been framed under Divia.Life or DiviaContacts. This note records the strategy and the idea so both survive.

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

## 4. The "QR-code sticker in the storefront window" idea (recorded for the first time)

**The idea:** a business registers in the **Divia.Network Global Registry** (a registry of Place/Company identities), receives a Divia.Network ID/URL, and puts a **Divia.Network QR-code sticker in its storefront window**. A mobile app can then (a) **scan the window sticker** to resolve that storefront to its Divia.Network / PKMS entity, and (b) offer an **AR camera view that overlays nearby buildings/stores/Places with their Divia.Network identity (ID/URL)**.

**Where it belongs — resolved:** this is a **DiviaContacts** capability, and it lives in **`diviacontacts-android`**. DiviaContacts' core job is *resolving People, **Places**, and Companies to their PKMS/Divia.Network entities* (Streak-style, today in the Gmail inbox); the AR storefront view simply extends that resolution **from the inbox to the physical world**. (This also answers John's open question: the idea is DiviaContacts, not Divia.Life — and it had never been written down under either.) The detailed AR/QR option-space lives in `diviacontacts-android`'s `ROADMAP.md` as Phase-01-experimental.

> Terminology caution: "Divia.Network" is overloaded. In `DOMAIN_MAPPINGS.md` `divia.network` is described as a tutorials/training microsite; in the fan-out user story it's the open integration layer/protocol; here "Divia.Network **Global Registry**" is a (currently aspirational) registry of public Place/Company identities. Reconcile these senses when the registry concept is actually scoped.

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
