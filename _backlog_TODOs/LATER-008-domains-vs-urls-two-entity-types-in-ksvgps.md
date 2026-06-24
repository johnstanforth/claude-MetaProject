# LATER-008 — Model Domains vs. customer-facing URLs as two distinct entity-types in the KSVGPS graph-DB

- **Captured:** 2026-06-24
- **Status:** open — deferred to the KSVGPS v1.0 graph-DB build (the domain-data import, ~this week). Triggered while building the GEN2 `Domain` entity (the registrar-shaped half of this).
- **Eventual owning project:** KSVGPS (`kingstrat-adventuregps`) graph-DB / Strategic-Landscape model. (`aixodev-GEN2` builds the registrar-shaped `Domain` half now.)
- **Related:** `_REFERENCE/DOMAIN_LIST.md`, `_REFERENCE/DOMAIN_MAPPINGS.md`, `_REFERENCE/STRATEGIC-LANDSCAPE-MODEL.md`, `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`; the GEN2 `Domain` / `DomainEdge` model.

## The decision to revisit

When we import domain data into the real KSVGPS graph-database, **model TWO distinct entity-types, not one:**

1. **Domain** — a **registrar-shaped** record. One row per *registered* domain (the registrable FQDN). Carries `registrar`, creation/expiration dates (UTC), RDAP data. **No subdomains** — a subdomain is not a separate registration, so it doesn't fit the registrar shape. This is the entity GEN2 builds now.

2. **URL** — a **customer-facing / PR-&-marketing** record. Models **what the customer SEES**, which is a genuinely different concern: it **includes subdomains** (e.g. `KSVGPS.kingstrat.ventures`) **and** specific paths (e.g. `divia.ai/diviaprofessionaldesktop/`), and has **no `registrar` concept**. The **`FRONTS → {Venture | Product-Line | Build-Line}`** relationship lives HERE (a URL fronts a product), *not* on the Domain. Typo-protection and defensive-stakeout reasoning is also fundamentally URL-level — it's about *what a customer might type or land on*, not what a registrar assigned.

## Why this matters (don't collapse them)

- **They answer different questions.** "What do we own · when does it expire · who's the registrar" is a *Domain* question. "What does a customer land on · what product does this URL front · what's our defensive-typo posture" is a *URL* question.
- **GEN2 deliberately blurs them (acceptable for the throwaway):** GEN2 keeps 301-redirect targets like `→ divia.ai/diviaprofessionaldesktop/` as `DomainEdge.target_path` *inside the Domain graph*. That technically mixes Domain and URL concepts — fine for the prototype, but the real graph-DB should split them cleanly (a path-redirect target is a URL-level fact, not a Domain-level one).
- **It's a "7-dimensional modeling" enabler.** John's intent: the real graph-DB should let future-Claude reason across the Domain ↔ URL ↔ {Venture/Product/Build-Line} relationships *all at once* — especially when brainstorming live with C-level execs and the KingStrat GPs who are thinking aloud and weighing decision trade-offs (acquire this typo domain? retire that redirect? rebrand this product?). The more domains/URLs are in play simultaneously, the more this hold-every-relationship-in-context reasoning is exactly where Claude outperforms an unaided human — so the model has to support it.

## Concretely, at import time

- Keep **Domain** as built in GEN2 (registrar-shaped; no subdomains; registrar/dates/RDAP).
- Add a **URL** entity: `url` (full — scheme/subdomain/path), `kind` (canonical · redirect-301 · typo-defense · hold/stakeout · vanity), and the polymorphic **`FRONTS → {Venture | Product-Line | Build-Line}`** edge (native in a graph-DB; deferred out of GEN2's SQLite).
- Relate the two: a **URL `SITS_ON` / `RESOLVES_VIA` a Domain** (the registrable domain a URL depends on) — so "if this domain lapses, which customer-facing URLs break?" is a one-hop query.
- Migrate GEN2's `DomainEdge` redirect + `target_path` data into the cleaner Domain-vs-URL split (each `target_path` becomes a URL node).
