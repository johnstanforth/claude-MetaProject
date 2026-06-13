# Product — DiviaHome

> The open-source, self-hosted **household hub** — and the **experimental prototype that drives the
> whole Divia.Network ecosystem.** The direct Python ancestor of the Rust Enterprise server, and the
> single highest-leverage unbuilt thing in the portfolio.

- **Names:** "DiviaHome" (the web repo is one piece of a broader DiviaHome product that also includes planned mobile apps + smart-home devices) · repo/dir `diviahome-web`.
- **Umbrella / venture:** DiviaAI (the open "lab" tier) — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **License:** **Dual AGPLv3 + Commercial (CLA-based)** — explicit; "© 2026 John Stanforth & Divia.AI, Inc." (full AGPL/CLA texts deferred to first publish).
- **Status:** 🟠 The **current ~60-day singular focus**, but still pre-code (Phase 00 PENDING; rich vision docs, empty backlog). Python 3.12+ · Flask · SQLAlchemy · SQLite→Postgres.

---

## What it is (consensus)
The personal/household, open-source edition of the Divia.AI ecosystem — and its fast, cheap, public R&D ground ("explore fast in Python first; converge proven ideas into the commercial products"). Loudly **"Experimental, Volatile, No Sacred Cows"** for ≥6 months. Four interconnected domains:
1. **Activity Log** — an inbox-style, AI-assisted capture surface; each free-form NL entry is a DiviaCard ("natural-language text input"), stored losslessly. *(AI classification/delegation is explicitly **v2**.)*
2. **Task Management** — Asana-style (lifecycle, assignment to household members, comment threads, attachments).
3. **Event Calendaring** — web calendar, assignable events, participants; later bidirectional Google Calendar sync.
4. **Document Editing (DDF / `.dvai`)** — the same outliner-of-DiviaCards model as Divia.AI Professional, with round-trip `.dvai` interop a first-class goal. Open Phase-00 question: app-DB-authoritative vs `.dvai`-file-authoritative, and the SQLite-`.dvai`-vs-Postgres-portability tension.

**The v1 mission — data unification.** v1 is a **"scan-and-import" project**: pull years of scattered legacy fragments (hundreds-to-thousands of SMS logs of food/meds/purchases/receipts) into one clean, de-duplicated, unified record displayed elegantly inside DiviaHome. Motto: **"first unify, then understand."**

### Cross-product role
- **The ecosystem anchor.** The Divia.Network fan-out (food→TastyPantry, macros→Sattvasic, expense→LegendaryMoney) originates from its Activity Log (see [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md)). These are the ecosystem's first-ever cross-app integrations; their lessons define the Divia.Network v0 contract.
- **The Python ancestor of Divia.AI Enterprise** — Enterprise is "a locked-down, higher-perf Rust re-implementation of this server." **DiviaHome v1 gates the entire commercial server line** (Enterprise → Global SaaS).
- Carries **placeholder global-identity fields** now for the future Divia.AI Global federation.

> ⚠️ ERRATA: the **nightly consumption-driven replenishment** loop and the **kitchen-counter voice device** (LATER-002) are **not in this repo** — it lists only a future "DiviaHome devices" repo. Brand-spelling drift ("Divia.AI"/"Divia.Network" vs `divia_ai-*`) and a "DiviaHome umbrella vs this web repo vs Divia.Life" naming ambiguity. See [`../../ERRATA.md` E-07/E-12`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** the v2 Divia.AI agent (NL classification/parsing + cross-app delegation); global identity + federated servers; Google Calendar bidirectional sync; full `.dvai` round-trip with Professional; DiviaHome smart-home/voice devices (Embedded/IoT) as a separate product; DiviaMesh sync; the Divia.Network "open HTTP-like standards"; Divia.Foundation.
- ✦ **New (from LATER-002):** the **nightly household-review loop** — consumption-driven replenishment (usage implies "running low on milk" → a time-decaying grocery item → escalating errand priority), delivered through the kitchen device which doubles as capture *and* delivery surface. The most demo-able "shock-and-awe" entry point into the whole ecosystem (see [`../../USER_STORIES/diviahome-nightly-replenishment.md`](../../USER_STORIES/diviahome-nightly-replenishment.md)).
- ✦ **Position the "scan-and-import / first unify, then understand" mission as the portfolio's signature pattern** — LegendaryMoney and Sattvasic share the exact same v1 shape (unify scattered legacy fragments first; infer later); building the scan-and-import engine well here pays off across three products.
- ✦ **DiviaHome as the recurring-stewardship agent's *consumer* twin** — the same "weekly/nightly review that catches what humans drop" capability that maintains the dev portfolio (LATER-002 §4) maintains the household; same mechanism, different brain.
