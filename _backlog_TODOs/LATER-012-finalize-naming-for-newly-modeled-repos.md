# LATER-012 — Revisit & finalize naming / Product-Line structure for a batch of newly-modeled repos

- **Captured:** 2026-06-28 (John + Claude), while populating the GEN2 DB with the on-disk `~/Code` repo inventory.
- **Status:** open — the repos were **added to GEN2 today with their current (on-disk) names as placeholders**; names + Product-Line/Build-Line structure to be finalized later.
- **Owning project:** cross-venture (GEN2 / KSVGPS modeling). Distinct from [LATER-011](LATER-011-decide-fate-of-aixodev-openhands-repo.md) (which is "what even is this repo"); these are real repos that just need name/structure decisions.

## Repos to revisit (added today under placeholder names/PLs)

- **`divia_cards`** — maybe rename to **`divia_ai-diviacards`** (or similar), to reflect that it's the Divia.AI **DiviaCards** standard/implementation. (Added under the **Divia.AI** owner — there is no separate "DiviaCards" owner in the model.)
- **`fracrealhomes-android`** — this is the **3D-virtual-home** app, a **different Product-Line / Build-Line** from the `-flutter` consumer app. Its name should change to differentiate it **away from** the `-flutter ⇒ -android | -iOS` pattern (that pattern signals "same Product-Line, cross-platform-first, native versions as later Build-Lines"). We had a different name for the 3D-home product — recover/decide it. (Added today under a placeholder **"FracRealHomes 3D Home"** Product-Line, `roadmap=current`.)
- **`sattvasichealth`** — likely splits into **different Product-Lines for the `-web` vs `-flutter`** surfaces; revisit the single-repo placeholder.
- **`tastypantry`** — probably follows the standard `-flutter ⇒ -android | -iOS` future/planned pattern (under the **TastyPantry** Product-Line within the TastyPal umbrella owner); confirm + expand the native siblings.
- **`dotfig_proto_cc`** — needs **multiple Build-Lines** and more careful thought about the overall options/positioning before finalizing name/structure. (Added under a placeholder **"Dotfigurator"** PL.)
- **`velocityterminal`** — same: needs **more Build-Lines**, etc. (Added under a placeholder **"VelocityTerminal"** PL.)

## The naming-pattern rule to preserve

`-flutter ⇒ -android | -iOS` is **meaningful**: it indicates "all the **same** Product-Line, built cross-platform-first, with native `-android`/`-iOS` versions as **later** Build-Lines (typically future/planned, ~6+ months out)." So any repo that does NOT fit that meaning (e.g. the FracRealHomes 3D-home Android app, which is its own Product-Line) should be **renamed** so it doesn't falsely imply the pattern.
