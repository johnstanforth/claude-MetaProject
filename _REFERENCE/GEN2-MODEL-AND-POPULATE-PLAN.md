# GEN2 Model Revision (Owners · Product-Lines · Build-Line Generations) + Populate Plan

> **Working spec, 2026-06-23 (John + Claude).** Consolidates the model revisions agreed across this session — the **Owner (Party) supertype**, **Product-Line ⇄ Build-Line** structure, and **Build-Line Generations** — plus the venture-by-venture populate plan. This is the build target for the next `aixodev-GEN2` schema/UI pass; once it stabilizes it folds back into the canonical [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) + [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md). Optimizing for the **v1 graph-DB accuracy**, not SQLite-scope convenience.

## 1. Owner (a.k.a. "Party") supertype — distinct subtypes, NOT flattened

Different kinds of thing can own repos/build-lines and all map to a GitHub-style account/org handle. Model that shared capability as a thin **`Owner`** supertype, with **first-class subtype tables** so KSVGPS keeps its richness (GP-portfolio functions attach to `Venture` only).

- **`Owner`** — `id`, `slug` (unique handle: `fracrealhomes` · `johnstanforth` · `DiviaAI`), `display_name`, `kind` (`venture` | `person` | `organization`), timestamps.
- **`Venture`** (1:1 `owner_id`) — the rich KSVGPS entity (GP-portfolio company). Carries venture-specific fields.
- **`Person`** (1:1 `owner_id`) — a human owner (you, a teammate) = the GitHub "Personal" account.
- **`Organization`** (1:1 `owner_id`) — `org_kind` (`oss-project` | `nonprofit` | `external-company`) — e.g. `Dotfigurator`, `VelocityTerminal`. Distinct from a Venture so KSVGPS treats it differently.
- **UI:** keep **Ventures / People / Organizations** as separate top-level menus (each a filtered view of `Owner` by `kind`) — mirrors GitHub's Personal-vs-Organization split.

## 2. Repositories

- **`Repository`** — `owner_id` (FK → Owner), `name`, `local_dir`, `remote_url`, `default_branch`, `CHECK(local_dir OR remote_url)`, **`UNIQUE(owner_id, name)`** (GitHub semantics: `johnstanforth/foo` ≠ `DiviaAI/foo`). *(This is where the `(owner, name)` uniqueness intuition lands — on the repo, not the Build-Line.)*
- **`repository_techstacks`** (M2M) — `repository_id`, `techstack_id`, `layer` (`backend` | `frontend` | `mobile` | `desktop` | `infra`). Kills the stack-combinatorics problem; agents pull the `layer`-appropriate stack.

## 3. Build-Lines + ownership

- **`BuildLine`** — `name` (**non-unique** — a human label; identity is `id`, so "DailySpikeDriver" can recur freely), `build_envelope_id` (single FK, conditional), `research_scope` (`playground` = the DailySpikeDriver/personal-experiment class · `optimization-target`), `description`.
- **`build_line_owners`** (M2M) — `build_line_id`, `owner_id`, `role`. **Co-ownership:** a personal DailySpikeDriver is `[Venture:FracRealHomes] + [Person:John]`; a teammate's is a separate line, same name, no collision.
- **`build_line_repositories`** (M2M) — `build_line_id`, `repository_id`, `role`, `status`, `is_primary`. Which repos a Build-Line uses (web/flutter/android/…); a repo is shared across Build-Lines only when the stack stays continuous.
- **`Stage`** (reset `v1→v2→v3` per Build-Line) → **`Phase`** → **`Sprint`**. A techstack pivot makes a *new* Build-Line starting at `v1`, never a `v5` of the old one.

## 4. Build-Line Generations & lineage (the new part)

- **`build_line_edges`** — `source_build_line_id`, `target_build_line_id`, `edge_type`, `note`, `UNIQUE(source, target, edge_type)`, `CHECK(source ≠ target)`. A real M2M-cross-reference (the linked-list), edited **only on the Build-Line detail page**, never a top-level menu.
- **`edge_type` values:** `succeeds` (**= the Generation link**: `source` is the next-gen successor of `target`, e.g. `aixodev-GEN2 --succeeds--> aixodev-web`; the Python/Flask→Rust jump) · `forked-from` (a personal experiment forked off a main line) · `merges-into` (the GitHub-PR-upstream flow).
- **Generation number is DERIVED** (`1 + length of the succeeds-chain behind it`) → shown as a "Gen N" badge; not a stored int (avoids renumber-drift). ORM exposes `BuildLine.successors` / `.predecessors` and a derived `.generation`.
- **No techstack denormalization.** The techstacks live on `repository_techstacks`; "find all Python/Flask Build-Lines succeeded by Rust ones" is a clean multi-hop join now and a native graph traversal in v1. The ORM association-proxy gives `build_line.successors[0].techstacks` without copying.
- **Payoff (future AIXO.Dev security/CVE tracking):** a CVE matched to a techstack → the affected (production-deployed) Build-Lines → automatically re-check their `succeeds` successors and record a "verified the Rust successor is not also vulnerable to this JWT flaw" status. Needs zero new schema beyond this edge + the existing techstack links.

## 5. Product-Lines, the PL⇄BL structure, Version-Releases

- **`ProductLine`** — `owner_id` (FK → Owner; usually a Venture, but a Person/Org can ship products too), `slug`, `name`, `description`.
- **`product_line_build_lines`** (M2M) — `product_line_id`, `build_line_id`, `status` (`current` | `planned` | `far-horizon` | `retired`), `UNIQUE(pl, bl)`. The structural "which Build-Lines build this product." Lets EstimatePacket (`current`) **and** National-AVM (`far-horizon`) both belong to FracRealHomes' Valuation Product-Line; a Build-Line can belong to zero Product-Lines (pure experiment) or several (shared infra).
- **`VersionRelease`** — `product_line_id`, `version`, `release_date`, `status`, `stage_id` (the moving symlink → `[Build-Line→Stage]`); `version_release_milestones` (M2M). *(Soft invariant: a release's stage's Build-Line should be one of its Product-Line's associated Build-Lines.)*
- **`Milestone`** — `name`, `milestone_date`, `team`, `description`; `stage_milestones` (M2M) + `version_release_milestones` (M2M). Business/HR (bonus-linked, team-scoped); may later be authored in KSVGPS and synced back.

## 6. Idea / Topic ontology (side, non-owning)

- `Topic`, `Idea`, `idea_topics`, `idea_edges` — unchanged. `owner_ideas` (M2M, non-owning: `relates-to`/`realizes`/`motivated-by`, optional dates) links any **Owner** to Ideas (so Persons and OSS Orgs can link too, not just Ventures).
- Future graph-DB nodes (documented, not built): **Thesis**, **Event/Phenomenon**.

## 7. UI/UX

- **Menus:** Ventures · People · Organizations (Owner by `kind`); Repositories; Build-Lines; Product-Lines; Version-Releases; Build (Envelopes/Stages/Phases/Sprints/Milestones/Targets); Strategy (Topics/Ideas).
- **Venture (Owner) detail = outline view:** each Product-Line as a node → its Build-Lines as leaves (with `current`/`far-horizon` `status` badge) → plus an "Unassigned / experimental Build-Lines" section (owned but not yet tied to a Product-Line) → plus the Owner's Repositories. Click straight into any Build-Line.
- **Build-Line detail:** owners (co-ownership) · repos (role/status) · stages · Product-Line memberships · **Lineage/Generations** section (`this Build-Line {succeeds, is-succeeded-by, forked-from, merges-into} [pick another Build-Line]` → writes a `build_line_edges` row; shows the "Gen N" badge).

## 8. Schema diff (from the current GEN2)

- **Add** `Owner` + subtypes `Person`, `Organization`; **`Venture` becomes a subtype** (`owner_id` 1:1).
- **Add** `build_line_owners` (M2M) · `product_line_build_lines` (M2M) · `build_line_edges` · `owner_ideas` (rename of `venture_ideas`).
- **Change** `Repository.venture_id → owner_id` (+ `UNIQUE(owner_id, name)`) · `ProductLine.venture_id → owner_id` · `BuildLine.venture_id` → `build_line_owners` M2M.
- **Keep** everything else (Repository/Techstack/`repository_techstacks`/`build_line_repositories`/Stage/Phase/Sprint/Milestone/`stage_milestones`/`version_release_milestones`/VersionRelease/BuildEnvelope/TriangulationTarget/Topic/Idea/`idea_topics`/`idea_edges`).
- **Migration:** the 12 ventures → `Owner(kind=venture)` + `Venture` rows (small custom script; Topics/Ideas/links unaffected). Hard-gate `export-all-data` first.

---

## 9. Populate plan — TABLE  *(Venture | Product-Line(s) | Current Build-Line [primary repo])*

| Venture | Product-Line(s) | Current Build-Line [primary repo] |
|---|---|---|
| **Divia.AI** | Divia.AI Professional · Divia.AI Enterprise | **OutlinerDesktop** [`divia_ai-professional`] · **WorkgroupsServer** [`proto-divia_ai-enterprise`] |
| **DiviaHome** | DiviaHome | **HomeHub** [`diviahome-web`] |
| **DiviaLife** | Divia.Life | **LifeMobile** [`divialife-flutter`] |
| **LegendaryMoney** | LegendaryMoney | **ConfidenceLedger** [`legendarymoney-web`] |
| **Kingmaker Strategic** | AdVentureGPS (KSVGPS) | **AdVentureGPS** [`kingstrat-adventuregps`] |
| **TastyPal** | TastyPantry *(+ TastyPal app, TastyTrucks?)* | **PantryCore** [`tastypantry`] *(others TBD)* |
| **SattvasicHealth** | SattvasicHealth | **VitalsAggregator** [`sattvasichealth`] |
| **FracRealHomes** | Property Valuation *(+ ADU-Evaluation?)* | **EstimatePacket** `current` [`fracrealhomes-web`] **+ National-AVM** `far-horizon` |
| **CrowdMadness** | CrowdMadness | **PredictionArena** *(pre-code)* |
| **Patternicity** | PatternicityNews | **PatternFeed** *(pre-code)* |
| **AIXO.Dev** | *FLAG — multiple (Platform · aixocode · Professional); maps to BL-A…E* | *your breakdown needed* |
| **ExoDev.Pro, Inc.** | *FLAG — services firm; likely no Product-Line* | — |

---

## 10. Populate plan — EDITABLE HIERARCHY  *(edit this freely and resend; add/rename/reorder Product-Lines and Current Build-Lines)*

- **Divia.AI**
  - Product-Line: **Divia.AI Professional** (desktop outliner)
    - Current Build-Line: **OutlinerDesktop**  ·  repo: `divia_ai-professional`
  - Product-Line: **Divia.AI Enterprise** (teams/workgroups server)
    - Current Build-Line: **WorkgroupsServer**  ·  repo: `proto-divia_ai-enterprise`
- **DiviaHome**
  - Product-Line: **DiviaHome** (self-hosted household hub)
    - Current Build-Line: **HomeHub**  ·  repo: `diviahome-web`
- **DiviaLife**
  - Product-Line: **Divia.Life** (cross-platform mobile life app)
    - Current Build-Line: **LifeMobile**  ·  repo: `divialife-flutter`
- **LegendaryMoney**
  - Product-Line: **LegendaryMoney** (AI personal-finance manager)
    - Current Build-Line: **ConfidenceLedger**  ·  repo: `legendarymoney-web`
- **Kingmaker Strategic**
  - Product-Line: **AdVentureGPS / KSVGPS** (venture-studio OS)
    - Current Build-Line: **AdVentureGPS**  ·  repo: `kingstrat-adventuregps`
- **TastyPal**  *(John: you mentioned TastyPal app + spicemaster prototype + TastyPantry + TastyTrucks — fill in below)*
  - Product-Line: **TastyPal app** (?)
    - Current Build-Line: **(name?)**  ·  early prototype: "spicemaster"
  - Product-Line: **TastyPantry** (pantry inventory)
    - Current Build-Line: **PantryCore**  ·  repo: `tastypantry`
  - Product-Line: **TastyTrucks** (?)
    - Current Build-Line: **(name?)**
- **SattvasicHealth**
  - Product-Line: **SattvasicHealth** (health-metrics aggregator)
    - Current Build-Line: **VitalsAggregator**  ·  repo: `sattvasichealth`
- **FracRealHomes**
  - Product-Line: **Property Valuation** (the diligence/estimate product)
    - Current Build-Line: **EstimatePacket** `current`  ·  repo: `fracrealhomes-web`
    - Far-horizon Build-Line: **National-AVM** `far-horizon`  ·  (succeeds EstimatePacket)
  - Product-Line: **ADU-Evaluation-Service** (?) — future
    - Current Build-Line: **(name?)**
- **CrowdMadness**
  - Product-Line: **CrowdMadness** (prediction-market game)
    - Current Build-Line: **PredictionArena**  ·  (pre-code)
- **Patternicity**
  - Product-Line: **PatternicityNews** (news portal)
    - Current Build-Line: **PatternFeed**  ·  (pre-code)
- **AIXO.Dev**  *(FLAG: multiple product-lines; you already have BL-A…E in MIGRATION-AND-SELF-HOSTING-PROPOSAL.md — confirm the breakdown)*
  - Product-Line: **AIXO.Dev Platform** (the web app)
    - Current Build-Line: **PlatformGraph** (= GEN2 / BL-B)  ·  repo: `aixodev-GEN2`
  - Product-Line: **aixocode** (the TUI)
    - Current Build-Line: **(name?)**  ·  repo: `aixodev-aixocode`
  - Product-Line: **AIXO.Dev Professional** (desktop) — future
    - Current Build-Line: **(name?)**
- **ExoDev.Pro, Inc.**  *(FLAG: services/holding firm — likely no software Product-Line; its software is AIXO.Dev)*
