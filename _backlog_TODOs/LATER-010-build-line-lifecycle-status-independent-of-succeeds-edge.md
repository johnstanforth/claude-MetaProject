# LATER-010 — Build-Line / Repository lifecycle status (active · maintained · frozen-reference · archived), INDEPENDENT of the `succeeds` generation edge

- **Captured:** 2026-06-28 (John + Claude), while reviewing the GEN2 generation/supersession model against the `aixodev-web` → `aixodev-GEN2` case.
- **Status:** **partially implemented (2026-06-28)** — after John+Claude discussed it against the faceted-search "Explore Projects" work, the core decision was made and **`Repository.lifecycle_status ∈ {active, maintained, frozen-reference, archived}` (default `active`, independent of `succeeds`) shipped in `aixodev-GEN2`** (commit `34441cf`), with the "Include legacy projects?" facet toggle (hides `frozen-reference`/`archived` by default) and seeded values (proto→`frozen-reference`, Community Editions→`maintained`, rest→`active`). **Still open:** (2) the `MIGRATE_ADAPT.md` migration-gate wiring, (3) the CVE "production-deployed" formalization, and the optional `BuildLine.lifecycle_status` rollup (work-items below).
- **Eventual owning project:** `aixodev-GEN2` (the GEN2 graph-DB schema + UI), folding back into the canonical `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md` once it stabilizes.
- **The design note lives here (reference it directly):** `_REFERENCE/GEN2-MODEL-AND-POPULATE-PLAN.md` §4 → the sub-section **"Lifecycle / maintenance status — a separate axis from the `succeeds` edge."** Also related: `_REFERENCE/GEN2-REPO-RECONCILIATION.md` (the prose "frozen scavenge-source" / "superseded-parked" categories this formalizes), `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`, and `_canonical/MIGRATE_ADAPT.md` (the standardization pass this status gates).

## The originating scenario (so a cold reader has the "why")

We now have `aixodev-web` (Gen 1) and its clean-rebuild successor `aixodev-GEN2` (Gen 2), and we're lift-and-shifting functionality from `-web` into `-GEN2` while evolving the new GEN2 model. We want a way to mark `aixodev-web` (and its preserved rsync clone `aixodev-LEGACY`) as **archived / frozen-reference** so we do **not** run it through the migration/adapt standardization pass — it's just legacy reference source going forward. The same will be true for `-GEN2` when a `-GEN3` eventually supersedes it. **But it won't always be true:** a *production-deployed* `-GEN2` that we keep maintaining for months while building `-GEN3` is still a living repo and must stay in scope. So "archived" cannot be derived from "has a successor" — it must be its own, independent status.

## The finding (what the model already has vs. lacks)

- **Has:** the supersession/generation edge — `build_line_edges` with `edge_type = 'succeeds'` (`aixodev-GEN2 --succeeds--> aixodev-web`), generation number derived from the chain. The edge is pure lineage and (correctly) does **not** auto-archive the predecessor.
- **Lacks:** a first-class, independent lifecycle/maintenance status. The closest existing pieces are wrong-shaped: `product_line_build_lines.status` (`current`/`planned`/`far-horizon`/`retired`) is a *roadmap position* and *membership-scoped*; `build_line_repositories.status` is a *repo-role within a BL*; and "frozen scavenge-source" / "superseded-parked" live only in the reconciliation doc's prose. The §4 CVE payoff already *assumes* a "(production-deployed)" status that isn't modeled.

## The work to implement

1. Add **`Repository.lifecycle_status ∈ { active, maintained, frozen-reference, archived }`** (repo-global), orthogonal to *both* the `succeeds` edge *and* `product_line_build_lines.status`. Optionally expose a Build-Line rollup (`BuildLine.lifecycle_status`, derived or set) for the generational unit.
2. Wire the **migration gate:** a repo whose `lifecycle_status` is `frozen-reference` or `archived` is **exempt** from the `MIGRATE_ADAPT.md` standardization pass; `active` / `maintained` repos stay in scope. (This is the concrete payoff John named — "so we DON'T need to run the whole migration/adapt process" on legacy gens.)
3. Use it to formalize the **"production-deployed"** distinction the §4 CVE-tracking payoff needs (active/maintained = deployed surface to re-check; frozen/archived = skip).
4. Seed the obvious values: `aixodev-web` / `aixodev-LEGACY` → `frozen-reference`; `aixodev-GEN2` → `active`; `kingstratvc-web` (superseded by `kingstrat-adventuregps`) → `frozen-reference`/`archived`.

## Constraints / gotchas

- **Do NOT overload `product_line_build_lines.status = retired`** for this — it's a different axis (roadmap position, membership-scoped); conflating them makes queries drift.
- Keep it **independent of the `succeeds` edge** — that independence is the whole point (a superseded predecessor may be `maintained` *or* `frozen`).
- Cheap to add **now**, while the generations model is design-only, vs. retrofitting after the schema ships.
