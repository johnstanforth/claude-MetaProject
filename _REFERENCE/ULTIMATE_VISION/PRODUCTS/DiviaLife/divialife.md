# Product — Divia.Life (Flutter · Android · iOS)

> The commercial, closed-source **mobile** member of the Divia.AI ecosystem — "your personal life,
> organized." A deeply-integrated, local-first client and the mobile capture surface that joins the
> Divia.Network circle. Four tabs; Flutter first, native later.

- **Names:** "Divia.Life" · repos `divialife-flutter` (first build), `divialife-android` (native Kotlin, planned), `divialife-iOS` (native Swift, planned).
- **Umbrella / venture:** DiviaAI / DiviaLife — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **License:** **Proprietary / commercial, closed-source** — explicit ("unlike the open-source DiviaHome (AGPLv3 + Commercial)").
- **Status:** 🟠 flutter = Phase 00 pending, no Flutter scaffold yet, "no sacred cows" for ~6 months. android/iOS = ⚪ empty (not even git repos).

---

## What it is (consensus)
A cross-platform **mobile app** (phone + tablet), local-first (on-device store is the source of truth, fully usable offline, syncs later). **Four tabs:**
1. **Agenda** — tasks + daily events + a **GPS-mapped, time-ordered daily itinerary** of destinations. Framed as the *inverse* of Google Location History: not where you've been, but a forward-looking mapped plan of where you need to go today.
2. **Journal** — **Logseq-style daily notes** (one page per day, low-friction capture; entries are natural-language DiviaCards).
3. **Messages** — **Telegram-like** rich-media DMs (text, images, audio, files) to friends & family.
4. **Friends & Family** — a configurable, user-controlled **aggregated feed** from external social networks (Instagram/Threads, X.com, BlueSky/ATProto) via per-network OAuth.

### Cross-product role
Shares the `.dvai` format + DiviaCards; syncs via **DiviaMesh / Divia.Network** with DiviaHome and the commercial servers — its **"first-ever ecosystem integrations."** The natural **mobile capture surface** for the Divia.Network fan-out (quick Journal/Agenda capture; the gentle "your agents this week" delivery card). Future global Divia.AI identity gives a unified work/home view with context-switching (see [`../../USER_STORIES/federated-home-and-work.md`](../../USER_STORIES/federated-home-and-work.md)).

> ✅ ERRATA resolution: **Divia.Life is Flutter-first, native Swift/Kotlin later** (the native dirs are confirmed empty). The "native Swift/Kotlin" claim elsewhere is a misquote of the table cell *"Flutter (then native Swift/Kotlin)."* See [`../../ERRATA.md` E-03`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** the six Phase-00 forks (state mgmt Riverpod vs Bloc; local store Drift vs Isar vs sqflite; routing; networking; Agenda maps + geolocation; identity-now-or-defer); Agenda "forward-looking location history"; Journal-as-DiviaCards round-tripping; per-network OAuth ingestion adapters normalizing social feeds; DiviaMesh bidirectional sync; native Kotlin/Swift editions once the data model stabilizes; a repository pattern keeping the local store swappable and isolating the eventual sync layer.
- ✦ **New:** **Agenda's GPS itinerary is the perfect surface for the recurring-agent output** — the nightly household packet, the GTD review packet, and the "milk errand climbing the list" all land as a mapped, time-ordered plan ("here's your day, in order, with the grocery run slotted where it fits"). The forward-itinerary framing turns agent suggestions into a route. ✦ **Messages as the agent delivery channel** — recaps and packets arrive as a Divia.Life message thread (agents as contacts), not email; dogfood + demo in one. ✦ The Friends-&-Family aggregator is itself an *implicit-data* engine — "you haven't talked to X in a while, and they just posted Y" — the DiviaContacts relationship-cadence idea, on the consumer side. ✦ Lean into "local-first, your data" as the privacy contrast to the social networks it aggregates.
