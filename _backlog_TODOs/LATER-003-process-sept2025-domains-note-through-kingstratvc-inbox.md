# LATER-003 — Process the Sept-2025 "domains" email-note through the KingStratVC Inbox (NL input-event dogfood)

- **Captured:** 2026-06-14, MetaProject session (while mapping the symlinked repos into `_REFERENCE/DOMAIN_MAPPINGS.md`)
- **Status:** LATER — **blocked on the `kingstrat-venturegps` Inbox feature**; not yet assigned to a sprint
- **Eventual owning project:** `kingstrat-venturegps` (the new Inbox / natural-language input-event funnel + the downstream workflows that project will define)
- **The artifact:** [`../_REFERENCE/notes-domains-sept2025.md`](../_REFERENCE/notes-domains-sept2025.md) — an email John sent to himself, **Sep 3, 2025, 12:49 AM**, parked in this repo for safekeeping.
- **Related design material:** [`../_REFERENCE/kingstratvc-web_DESIGN_NOTES.md`](../_REFERENCE/kingstratvc-web_DESIGN_NOTES.md) + the reconstructed [`…_gemini-naming-transcript.md`](../_REFERENCE/kingstratvc-web_gemini-naming-transcript.md) — the **"KingStrat VentureGPS" / Vector-Tracking-Loop** concept, the **dual-node** (Signal Node = studio control center / Trajectory Node = LP portal) architecture, and the telemetry UI direction for this product.

---

## #TODO

Once the new **Inbox** feature is working in `kingstrat-venturegps`, ingest `notes-domains-sept2025.md` as a single **natural-language input event** — the *same* intake funnel a kitchen-counter DiviaHome device dictation would use (the Divia.Network "one capture in → structured entries out" pattern). Then run it through the workflows set up in `kingstrat-venturegps` to clarify, classify, and route its contents.

This doubles as an early **dogfood / test case** for that funnel: a real, messy, multi-topic NL note is exactly the kind of input the Inbox is meant to absorb and process — and it overlaps directly with the venture-ideas-database concept the note itself proposes (see "KingStrat InsightHub" below).

## Design decision — temporal data (Postgres, timezone-aware UTC)

When this note **and** the structured domain data (`../_REFERENCE/DOMAIN_LIST.md`, `../_REFERENCE/DOMAIN_MAPPINGS.md`, `../_REFERENCE/domains_rdap.jsonl`) are imported into the real `kingstrat-venturegps` knowledge base, store all timestamps in a **Postgres database with timezone-aware UTC handling** — persist the canonical UTC instant, render in the user's local timezone. This avoids the off-by-one-day artifact visible in the flat `DOMAIN_LIST.md` table, where RDAP **Creation Dates (UTC)** sit a calendar day apart from the registrar panel's **local-time Expiration Dates** (≈46 rows). The raw UTC timestamps are already preserved in `domains_rdap.jsonl`, so the canonical instants survive the import intact. This is the general pattern for the whole **chronology-aware provenance model**: record *when* every fact was true in UTC; render and reason in context.

## What's in the note (so future-us knows what we're processing)

A raw brain-dump of domain + venture ideas, including:
- **Book / SEO domains:** `billiondollarplatforms.com`, the `rustdevelopment.*` set (flagged "needs keyword research"), the DIVIA Mentality book domains.
- **Divia ecosystem:** `divia.tv` (a guide to video content), `divia.shop` / `diviafoundation.shop` (affiliate marketing routed to the Foundation), Foundation-on-TikTok ideas, a LanceDB (tantivy+vector) FAQ search for the Foundation page.
- **`johnstanforth.com`** author-page plan (short bio now → full linked-ventures page in 2026).
- **Legendary.Financial** — a *fractional-CFO-for-small-business* venture idea (+ `legendaryfinancial.ai`); the origin of today's `LegendaryFinancial.AI` subsidiary entry.
- **KingmakerStrategic** — the IdeaBrowser / Greg-Isenberg observation and the **"KingStrat InsightHub / InsightCenter"** venture-ideas-database concept (floated as a possible Divia.AI Enterprise PoC). Directly relevant to the `kingstrat-venturegps` → ideation-platform / venture-studio reframing.
- **"Other domains to consider":** assorted `.ai` variants; `tastytrucks.com` pricing.

> **When processing, reconcile — don't treat as net-new.** This note is ~9 months old; several items have since been acted on (e.g. `diviafoundation.shop` registered; `legendaryfinancial.ai` and `tastytrucks.com` now on `DOMAIN_WISHLIST.md`; `divia.tv` registered). Diff its ideas against the current `DOMAIN_MAPPINGS.md` / `DOMAIN_WISHLIST.md` to surface only what's still open.

## Why it's parked here for now

Saved arbitrarily in `_REFERENCE/` purely for future reference — it has no organizational home yet *by design*. Giving it one (clarify → classify → route) is precisely the job of the Inbox funnel once it exists, which is the whole point of using it as the first real input.
