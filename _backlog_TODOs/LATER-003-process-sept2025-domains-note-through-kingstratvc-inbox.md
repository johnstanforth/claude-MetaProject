# LATER-003 — Process the Sept-2025 "domains" email-note through the KingStratVC Inbox (NL input-event dogfood)

- **Captured:** 2026-06-14, MetaProject session (while mapping the symlinked repos into `_REFERENCE/DOMAIN_MAPPINGS.md`)
- **Status:** LATER — **blocked on the `kingstratvc-web` Inbox feature**; not yet assigned to a sprint
- **Eventual owning project:** `kingstratvc-web` (the new Inbox / natural-language input-event funnel + the downstream workflows that project will define)
- **The artifact:** [`../_REFERENCE/notes-domains-sept2025.md`](../_REFERENCE/notes-domains-sept2025.md) — an email John sent to himself, **Sep 3, 2025, 12:49 AM**, parked in this repo for safekeeping.

---

## #TODO

Once the new **Inbox** feature is working in `kingstratvc-web`, ingest `notes-domains-sept2025.md` as a single **natural-language input event** — the *same* intake funnel a kitchen-counter DiviaHome device dictation would use (the Divia.Network "one capture in → structured entries out" pattern). Then run it through the workflows set up in `kingstratvc-web` to clarify, classify, and route its contents.

This doubles as an early **dogfood / test case** for that funnel: a real, messy, multi-topic NL note is exactly the kind of input the Inbox is meant to absorb and process — and it overlaps directly with the venture-ideas-database concept the note itself proposes (see "KingStrat InsightHub" below).

## What's in the note (so future-us knows what we're processing)

A raw brain-dump of domain + venture ideas, including:
- **Book / SEO domains:** `billiondollarplatforms.com`, the `rustdevelopment.*` set (flagged "needs keyword research"), the DIVIA Mentality book domains.
- **Divia ecosystem:** `divia.tv` (a guide to video content), `divia.shop` / `diviafoundation.shop` (affiliate marketing routed to the Foundation), Foundation-on-TikTok ideas, a LanceDB (tantivy+vector) FAQ search for the Foundation page.
- **`johnstanforth.com`** author-page plan (short bio now → full linked-ventures page in 2026).
- **Legendary.Financial** — a *fractional-CFO-for-small-business* venture idea (+ `legendaryfinancial.ai`); the origin of today's `LegendaryFinancial.AI` subsidiary entry.
- **KingmakerStrategic** — the IdeaBrowser / Greg-Isenberg observation and the **"KingStrat InsightHub / InsightCenter"** venture-ideas-database concept (floated as a possible Divia.AI Enterprise PoC). Directly relevant to the `kingstratvc-web` → ideation-platform / venture-studio reframing.
- **"Other domains to consider":** assorted `.ai` variants; `tastytrucks.com` pricing.

> **When processing, reconcile — don't treat as net-new.** This note is ~9 months old; several items have since been acted on (e.g. `diviafoundation.shop` registered; `legendaryfinancial.ai` and `tastytrucks.com` now on `DOMAIN_WISHLIST.md`; `divia.tv` registered). Diff its ideas against the current `DOMAIN_MAPPINGS.md` / `DOMAIN_WISHLIST.md` to surface only what's still open.

## Why it's parked here for now

Saved arbitrarily in `_REFERENCE/` purely for future reference — it has no organizational home yet *by design*. Giving it one (clarify → classify → route) is precisely the job of the Inbox funnel once it exists, which is the whole point of using it as the first real input.
