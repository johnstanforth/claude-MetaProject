# GEN2 Model Revision (Owners · Product-Lines · Build-Line Generations) + Populate Plan

> **Working spec, 2026-06-23 (John + Claude).** Consolidates the model revisions agreed across this session — the **Owner (Party) supertype**, **Product-Line ⇄ Build-Line** structure, and **Build-Line Generations** — plus the venture-by-venture populate plan. This is the build target for the next `aixodev-GEN2` schema/UI pass; once it stabilizes it folds back into the canonical [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) + [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md). Optimizing for the **v1 graph-DB accuracy**, not SQLite-scope convenience. **Status: design only — nothing below is built in the running app yet** (the server on :5000 still holds the prior Venture-owned schema with the 12 ventures + seed topics/ideas).
>
> ⚠️ **The §9–§10 venture / product / ownership assignments are WORKING DRAFTS — freely rearrangeable right now; decide each on its own merits.** Some names/owners are John's working guesses (a few seeded from last year's Claude trademark research, used to jog memory); the *model* (§1–§8) is the **stable** part, the *populate names/placements* are still being experimented with. Only a few are firm (e.g. "Divia.AI, Inc." ≈ 99% certain). Treat the rest as editable drafts, not canon — and **do not defer a change waiting for any sign-off**: if it's right to change now, change it. (The names lock only once John presents the finished model to the Divia cofounders / KSV GPs, after which they get much harder to change — so the value is in arranging them well *while they're still fluid*, not in waiting.)

## 1. Owner (a.k.a. "Party") supertype — distinct subtypes, NOT flattened

Different kinds of thing can own repos/build-lines and all map to a GitHub-style account/org handle. Model that shared capability as a thin **`Owner`** supertype, with **first-class subtype tables** so KSVGPS keeps its richness (GP-portfolio functions attach to `Venture` only).

- **`Owner`** — `id`, `slug` (unique handle: `fracrealhomes` · `johnstanforth` · `DiviaAI`), `display_name`, `kind` (`venture` | `person` | `organization`), timestamps.
- **`Venture`** (1:1 `owner_id`) — the rich KSVGPS entity (GP-portfolio company). Carries venture-specific fields.
- **`Person`** (1:1 `owner_id`) — a human owner (you, a teammate) = the GitHub "Personal" account.
- **`Organization`** (1:1 `owner_id`) — `org_kind` (`oss-project` | `nonprofit` | `external-company`) — e.g. `Dotfigurator`, `VelocityTerminal`. Distinct from a Venture so KSVGPS treats it differently.
- **Display-name vs. slug (naming convention):** `display_name` is the **human spelling** — proper words, spaces, punctuation (e.g. *Sattvasic Health*, *Divia.AI*); `slug` is the **machine handle** — lowercase, no spaces, GitHub-style (e.g. `sattvasichealth`, `divia-ai`). Repos and local-dirs always use the slug form. The same split applies to Product-Line / Build-Line display labels vs. their slugs.
- **UI:** keep **Ventures / People / Organizations** as separate top-level menus (each a filtered view of `Owner` by `kind`) — mirrors GitHub's Personal-vs-Organization split.

## 2. Repositories

- **`Repository`** — `owner_id` (FK → Owner), `name`, `local_dir`, `remote_url`, `default_branch`, `CHECK(local_dir OR remote_url)`, **`UNIQUE(owner_id, name)`** (GitHub semantics: `johnstanforth/foo` ≠ `DiviaAI/foo`). *(This is where the `(owner, name)` uniqueness intuition lands — on the repo, not the Build-Line.)*
- **`repository_techstacks`** (M2M) — `repository_id`, `techstack_id`, `layer` (`backend` | `frontend` | `mobile` | `desktop` | `infra`). Kills the stack-combinatorics problem; agents pull the `layer`-appropriate stack.

## 3. Build-Lines + ownership

- **`BuildLine`** — `name` (**non-unique** — a human label; identity is `id`, so "DailySpikeDriver" can recur freely), `build_envelope_id` (single FK, conditional), `ceremony_level_id` (FK → the rigor/formality entity — see §11), `description`.
- **`build_line_owners`** (M2M) — `build_line_id`, `owner_id`, `role`. **Co-ownership is unlimited:** a Build-Line can be owned by `[Venture] + [Person:John] + [Person:David] + …` (the Digital-Insight-1997 two-devs-plus-the-company case). Only `UNIQUE(build_line_id, owner_id)` (no dup owner); no "single account" limit anywhere. `role` (e.g. `sponsor`/`lead`/`contributor`) is also the future ACL/permissions hook.
- **`build_line_repositories`** (M2M) — `build_line_id`, `repository_id`, `role`, `status`, `is_primary`. Which repos a Build-Line uses (web/flutter/android/…); a repo is shared across Build-Lines only when the stack stays continuous.
- **`Stage`** (reset `v1→v2→v3` per Build-Line) → **`Phase`** → **`Sprint`**. A techstack pivot makes a *new* Build-Line starting at `v1`, never a `v5` of the old one.

## 4. Build-Line Generations & lineage

- **`build_line_edges`** — `source_build_line_id`, `target_build_line_id`, `edge_type`, `note`, `UNIQUE(source, target, edge_type)`, `CHECK(source ≠ target)`. A real M2M-cross-reference (the linked-list), edited **only on the Build-Line detail page**, never a top-level menu.
- **`edge_type` values:** `succeeds` (**= the Generation link**: `source` is the next-gen successor of `target`, e.g. `aixodev-GEN2 --succeeds--> aixodev-web`) · `forked-from` (a personal experiment forked off a main line) · `merges-into` (the GitHub-PR-upstream flow).
- **Generation number is DERIVED** (`1 + length of the succeeds-chain behind it`) → shown as a "Gen N" badge; not a stored int (avoids renumber-drift). ORM exposes `BuildLine.successors` / `.predecessors` and a derived `.generation`.
- **The techstack-pivot rule is a HEURISTIC, not DB-enforced.** `build_line_edges` lets you add a `succeeds` between *any* two Build-Lines, so deliberate exceptions are fine — e.g. `aixodev-web` → `aixodev-GEN2` is a clean-rebuild `succeeds` even though both stay Python/Flask. The rule ("techstack change → new Build-Line at v1; same techstack → same Build-Line, just a repo rename") guides the common case; the edge table never blocks the rare "exception that proves the rule."
- **Personal-Build-Line creation convention (confirmed):** default to a **standalone** spike (fresh project) unless you're modifying existing product code, in which case **fork-from-current** (`forked-from` edge); either way a **`merges-into`** edge records the upstream graduation, and a `playground` ceremony-level + a Person co-owner marks it personal/experimental. (Claude-era lift-and-shift makes the standalone path cheap — partial functionality moves between lines without git-clone/merge ceremony.)
- **No techstack denormalization.** The techstacks live on `repository_techstacks`; "find all Python/Flask Build-Lines succeeded by Rust ones" is a clean multi-hop join now and a native graph traversal in v1. The ORM association-proxy gives `build_line.successors[0].techstacks` without copying.
- **Payoff (future AIXO.Dev security/CVE tracking):** a CVE matched to a techstack → the affected (production-deployed) Build-Lines → automatically re-check their `succeeds` successors and record a "verified the Rust successor is not also vulnerable to this JWT flaw" status. Needs zero new schema beyond this edge + the existing techstack links.

### Lifecycle / maintenance status — a separate axis from the `succeeds` edge (PROPOSED 2026-06-28; **`Repository.lifecycle_status` field IMPLEMENTED in `aixodev-GEN2` 2026-06-28, commit `34441cf`**; tracked: `_backlog_TODOs/LATER-010`)

- **The gap (John + Claude, 2026-06-28):** the `succeeds` edge models *lineage/generation* but deliberately does **not** lock or archive the predecessor — correct, but it means there is currently **no first-class way to say "this Build-Line / repo is archived legacy reference; skip it."** The existing status fields are the wrong shape: `product_line_build_lines.status` (`current`/`planned`/`far-horizon`/`retired`) is a *roadmap position* and is *membership-scoped* (per Product-Line; a BL can belong to many); `build_line_repositories.status` is a repo's *role* within a BL; and `GEN2-REPO-RECONCILIATION.md`'s "frozen scavenge-source" / "superseded-parked" categories live only in prose. The CVE-tracking payoff just above already *assumes* a distinct "(production-deployed)" status that is not yet modeled.
- **Proposed addition:** a first-class **lifecycle / maintenance status**, orthogonal to *both* the `succeeds` edge *and* the roadmap `product_line_build_lines.status`. Put it on the **Repository** (repo-global — the on-disk repo is the unit the standardization/migration pass operates on), optionally rolled up to the Build-Line: **`Repository.lifecycle_status ∈ { active, maintained, frozen-reference, archived }`**.
- **Why it MUST be independent of `succeeds`:** a superseded predecessor is sometimes dead-and-frozen and sometimes still in production — *same edge, different lifecycle*:

| Case | `succeeds` edge | `lifecycle_status` | Standardization / migration |
|---|---|---|---|
| `aixodev-web` superseded by `aixodev-GEN2` | predecessor | `frozen-reference` | **exempt** — legacy source only |
| a production `-GEN2` maintained while `-GEN3` is built | predecessor | `maintained` | **in scope** — it's a living repo |

- **Payoff:** (1) `frozen-reference` / `archived` becomes the **gate that exempts a repo from the `_canonical/MIGRATE_ADAPT.md` standardization pass** (don't migrate legacy scavenge-source). (2) It formalizes the "(production-deployed)" distinction the CVE-tracking payoff already needs. (3) Do **not** overload `retired` for this — keep lifecycle a separate axis or queries drift. Cheap to add now while `build_line_edges` is still design-only.

## 5. Product-Lines, the PL⇄BL structure, Version-Releases

- **`ProductLine`** — `owner_id` (FK → Owner; usually a Venture, but a Person/Org can ship products too), `slug`, `name`, `description`.
- **`product_line_build_lines`** (M2M) — `product_line_id`, `build_line_id`, `status` (`current` | `planned` | `far-horizon` | `retired`), `UNIQUE(pl, bl)`. The structural "which Build-Lines build this product." Lets EstimatePacket (`current`) **and** National-AVM (`far-horizon`) both belong to FracRealHomes' Valuation Product-Line; a Build-Line can belong to zero Product-Lines (pure experiment), one, or several (a shared backend feeding many app Product-Lines — the TastyPal case).
- **`VersionRelease`** — `product_line_id`, `version`, `release_date`, `status`, `stage_id` (the moving symlink → `[Build-Line→Stage]`); `version_release_milestones` (M2M). *(Soft invariant: a release's stage's Build-Line should be one of its Product-Line's associated Build-Lines.)*
- **`Milestone`** — `name`, `milestone_date`, `team`, `description`; `stage_milestones` (M2M) + `version_release_milestones` (M2M). Business/HR (bonus-linked, team-scoped); may later be authored in KSVGPS and synced back.
- **The "(service)" vs "Community Edition" split means different things per venture.** For most (e.g. **LegendaryMoney**) the AGPLv3 self-host edition and the commercial closed SaaS are roughly the *same product* under different licenses (with a Python-open → Rust-commercial / CLA-relicensing caveat). For **DiviaHome** it is *not*: the Community Edition (AGPLv3 + Commercial, CLA-governed Python/Flask, free on GitHub) is one thing, but the **Global Service** at `diviahome.com` is a separate federation / message-queue-relay SaaS (TBD) — **not** a commercial clone of the GitHub app. DiviaHome's dual-license + CLA exists to clear a **future smart-home-hardware product-line** (a "DiviaHome Hub" device — router / DNS / DHCP + a preinstalled, likely-Rust, commercial DiviaHome server matching the Python community functionality; the CLA legally clears rewriting contributed Python → Rust for that closed product). Far-future (2028+; hardware via Shenzhen + tariff/trade complexity) — a `[DEALBREAKER-HOOK]`-style license decision made *now* for a future scenario. *(More detail — incl. the high-priority China trademark plan for "Divia" names — lives in the ~100-page "Divia Trademark Guide" research from last summer, to be re-imported into KSVGPS as we build the graph-DB.)*

## 6. Idea / Topic ontology (side, non-owning)

- `Topic`, `Idea`, `idea_topics`, `idea_edges` — unchanged. `owner_ideas` (M2M, non-owning: `relates-to`/`realizes`/`motivated-by`, optional dates) links any **Owner** to Ideas (so Persons and OSS Orgs can link too, not just Ventures).
- Future graph-DB nodes (documented, not built): **Thesis**, **Event/Phenomenon**.

## 7. UI/UX

- **Menus:** Ventures · People · Organizations (Owner by `kind`); Repositories; Build-Lines; Product-Lines; Version-Releases; Build (Envelopes/Stages/Phases/Sprints/Milestones/Targets); Ceremony Levels; Strategy (Topics/Ideas).
- **Venture (Owner) detail = outline view:** each Product-Line as a node → its Build-Lines as leaves (with `current`/`far-horizon` `status` badge) → plus an "Unassigned / experimental Build-Lines" section (owned but not yet tied to a Product-Line) → plus the Owner's Repositories. Click straight into any Build-Line.
- **Build-Line detail:** owners (co-ownership) · repos (role/status) · stages · Product-Line memberships · ceremony-level · **Lineage/Generations** section (`this Build-Line {succeeds, is-succeeded-by, forked-from, merges-into} [pick another Build-Line]` → writes a `build_line_edges` row; shows the "Gen N" badge).

## 8. Schema diff (from the current GEN2)

- **Add** `Owner` + subtypes `Person`, `Organization`; **`Venture` becomes a subtype** (`owner_id` 1:1).
- **Add** `build_line_owners` (M2M) · `product_line_build_lines` (M2M) · `build_line_edges` · `owner_ideas` (rename of `venture_ideas`) · `CeremonyLevel` (+ `BuildLine.ceremony_level_id`; see §11).
- **Change** `Repository.venture_id → owner_id` (+ `UNIQUE(owner_id, name)`) · `ProductLine.venture_id → owner_id` · `BuildLine.venture_id` → `build_line_owners` M2M · `BuildLine.research_scope` → `BuildLine.ceremony_level_id`.
- **Keep** everything else (Repository/Techstack/`repository_techstacks`/`build_line_repositories`/Stage/Phase/Sprint/Milestone/`stage_milestones`/`version_release_milestones`/VersionRelease/BuildEnvelope/TriangulationTarget/Topic/Idea/`idea_topics`/`idea_edges`).
- **Migration:** the existing ventures → `Owner(kind=venture)` + `Venture` rows. Topics/Ideas/links unaffected. Hard-gate `export-all-data` first.

---

## 9. Populate plan — SUMMARY  *(authoritative editable hierarchy is §10; all names are working drafts — see top banner)*

| Venture (display) | Product-Lines | Current Build-Line(s) |
|---|---|---|
| **Divia.AI** | Global Service · Professional · Enterprise | DiviaGlobalService · DesktopOutliner · DiviaServerPrototype (+ WorkgroupServer `far-horizon`, Rust, `succeeds`) |
| **DiviaHome** | Service · Community Edition · Divia.Life · *(future: DiviaHome Hub hardware)* | GlobalHomeService · CommunityHomeHub · LifeCardMessenger |
| **LegendaryMoney** | Service · Community Edition | ConfidenceLedger (web+flutter) · HouseholdLedger |
| **Kingmaker Strategic** | AdVentureGPS / KSVGPS | AdVentureGPS |
| **TastyPal** | Platform (web superset) · TastyPal/TastyPantry/TastyTrucks (mobile verticals) · TastyPantry CE · Professional Services | TastePalatesEngine (backend+web) · per-app mobile lines · TastySpatialGPS · CommunityPantry |
| **Sattvasic Health** | Service · Community Edition | VitalsGlobalService · VitalsDataLake |
| **FracRealHomes** | Property Valuation *(+ future ADU-Evaluation)* | EstimatePacket `current` (+ National-AVM `far-horizon`); personal DailySpikeDriver × John |
| **CrowdMadness** | CrowdMadness | PredictionBracketsEngine *(pre-code)* |
| **Patternicity** | PatternicityNews · …News Reader · Patternicity.Social · …AI Intelligence Services · …AI Professional | PTNewsFeed · PTNewsReaderApp · PTSocialNews *(pre-code)* |
| *Deferred:* **AIXO.Dev** (BL-A…E) · **ExoDev.Pro** (no software PL) | | |

---

## 10. Populate plan — EDITABLE HIERARCHY  *(working drafts — freely rearrangeable now, decide on merits; not pending any gate; `display name` uses proper spelling, slugs/repos use the machine form)*

- **Divia.AI**
  - Product-Line: **Divia.AI Global Service** (online/hosted SaaS subscription service at `divia.ai`)
    - Current Build-Line: **DiviaGlobalService**  ·  repo: `divia_ai-globalservice`
  - Product-Line: **Divia.AI Professional** (desktop outliner)
    - Current Build-Line: **DesktopOutliner**  ·  repo: `divia_ai-professional`
  - Product-Line: **Divia.AI Enterprise** (teams/workgroups server)
    - Current Build-Line: **DiviaServerPrototype**  ·  repo: `proto-divia_ai-enterprise`
    - Far-horizon Build-Line: **WorkgroupServer**  ·  repo: `divia_ai-enterprise`  ·  **`succeeds` DiviaServerPrototype** (Gen 2 — the Rust techstack pivot)
- **DiviaHome**
  - Product-Line: **DiviaHome (service)** (closed/proprietary federation-relay SaaS at `diviahome.com` — NOT a clone of the Community Edition; see §5)
    - Current Build-Line: **GlobalHomeService**  ·  repo: `diviahome-service`
  - Product-Line: **DiviaHome: Community Edition** (self-hosted open-source household hub; AGPLv3 + Commercial, CLA)
    - Current Build-Line: **CommunityHomeHub**  ·  repo: `diviahome-community` *(renamed from `diviahome-web` — same techstack & scope ⇒ same Build-Line, just a repo rename)*
  - Product-Line: **Divia.Life** (cross-platform mobile app, with messaging of DiviaCard types/objects) *(TENTATIVE placement under DiviaHome — whether "DiviaLife" was ever meant to be its own venture is unconfirmed, possibly an earlier mis-answer; pending review)*
    - Current Build-Line: **LifeCardMessenger**  ·  repo: `divialife-flutter`
  - Product-Line: **DiviaHome Hub** *(FUTURE — smart-home hardware device; preinstalled Rust commercial server; far-future 2028+; TBD — see §5 licensing note)*
- **LegendaryMoney**
  - Product-Line: **LegendaryMoney (service)** (AI personal-finance manager)
    - Current Build-Line: **ConfidenceLedger**  ·  repos: `legendarymoney-web` + `legendarymoney-flutter`
  - Product-Line: **LegendaryMoney: Community Edition** (self-hosted open-source personal-finance manager web app)
    - Current Build-Line: **HouseholdLedger**  ·  repo: `legendarymoney-community`
- **Kingmaker Strategic**
  - Product-Line: **AdVentureGPS / KSVGPS** (venture-studio OS)
    - Current Build-Line: **AdVentureGPS**  ·  repo: `kingstrat-adventuregps`
- **TastyPal**  *(structure confirmed §11-A)*
  - Product-Line: **TastyPal Platform** (the `tastypal.com` web product — the "Yelp-for-taste-palates" SUPERSET: all three verticals' functionality via the website; the shared backend + taste-palate AI models live here)
    - Current Build-Line: **TastePalatesEngine**  ·  repos: `tastypal-backend` + `tastypal-web`  ·  the shared engine/backend — **also powers the three mobile apps** (linked `current` to their PLs via the M2M)
    - Personal Build-Line × `johnstanforth`: **TastySpikeDriver**  ·  repo: `spicemaster3000` *(playground; to be renamed; co-owned `tastypal` + `johnstanforth`)*
  - Product-Line: **TastyPal** (mobile app — the restaurant/taste-matching vertical; small, light, focused)
    - Current Build-Line: **TastyPalMobile**  ·  repo: `tastypal-flutter`  *(uses the TastePalatesEngine backend)*
  - Product-Line: **TastyPantry** (mobile app — the pantry/recipes vertical)
    - Current Build-Line: **TastyPantryMobile**  ·  repo: `tastypantry-flutter`
  - Product-Line: **TastyPantry: Community Edition** (self-hosted pantry web app; federates with `tastypal.com`)
    - Current Build-Line: **CommunityPantry**  ·  repo: `tastypantry-community`
  - Product-Line: **TastyTrucks** (mobile app — the food-truck-locator vertical)
    - Current Build-Line: **TastyTrucksMobile**  ·  repo: `tastytrucks-flutter`
    - Current Build-Line: **TastySpatialGPS**  ·  repo: `tastytrucks-gps`  ·  the food-truck GPS / fleet-tracking service (the GridTransmit/SensoryMQ lineage); `current` for this PL alongside the mobile app
  - Product-Line: **TastyPal Professional Services** (culinary consultants tuning restaurant menus from the taste-palate AI models — a *services* line; no software Build-Line, like ExoDev.Pro)
- **Sattvasic Health**
  - Product-Line: **Sattvasic Health (service)** (health-metrics aggregator service)
    - Current Build-Line: **VitalsGlobalService**  ·  repo: `sattvasichealth-globalservice`
  - Product-Line: **Sattvasic Health: Community Edition** (self-hosted open-source health-metrics aggregator)
    - Current Build-Line: **VitalsDataLake**  ·  repo: `sattvasichealth-community`
- **FracRealHomes**
  - Product-Line: **Property Valuation** (the diligence/estimate product)
    - Personal Build-Line × `johnstanforth`: **DailySpikeDriver**  ·  repo: `fracrealhomes-johnstanforth` *(to build soon — a standalone Python/Flask spike, Gmail-parsing of Zillow/Redfin emails first; `merges-into` EstimatePacket on graduation)*
    - Current Build-Line: **EstimatePacket** `current`  ·  repo: `fracrealhomes-web`
    - Far-horizon Build-Line: **National-AVM** `far-horizon`  ·  `succeeds` EstimatePacket
  - Product-Line: **ADU-Evaluation-Service** *(exact name TBD — future)*
    - Far-horizon Build-Line: [TBD]
- **CrowdMadness**
  - Product-Line: **CrowdMadness** (prediction-market game)
    - Current Build-Line: **PredictionBracketsEngine**  ·  (pre-code) *(renamed from "PredictionArena" to avoid collision with Meta's newly-announced "Arena" prediction market, NYT 2026-06-23 — saved in the CrowdMadness venture brief)*
- **Patternicity**
  - Product-Line: **PatternicityNews** (news portal)
    - Current Build-Line: **PTNewsFeed**  ·  (pre-code)
  - Product-Line: **PatternicityNews Reader** (consumer-focused cross-platform desktop RSS/News reading app)
    - Current Build-Line: **PTNewsReaderApp**  ·  (pre-code)
  - Product-Line: **Patternicity.Social** (Twitter/BlueSky/Mastodon-like social network for news-related discussion)
    - Current Build-Line: **PTSocialNews**  ·  (pre-code)
  - Product-Line: **Patternicity.AI Intelligence Services** (world-knowledge & business-data subscription services for corporate clients; Palantir-style long-term licensing, delivered via FDSE client engagements from ExoDev.Pro regional offices)
    - Far-horizon Build-Line: [TBD]
  - Product-Line: **Patternicity.AI Professional** (business-intelligence cross-platform desktop app — a Bloomberg-terminal-style high-density UI, not a consumer app; engineering-wise close to Divia.AI Professional)
    - Far-horizon Build-Line: [TBD]

### Deferred (think more first)

- **AIXO.Dev** — multiple product-lines (Platform · aixocode · Professional); maps to BL-A…E in [`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md). Confirm the breakdown later.
- **ExoDev.Pro, Inc.** — services/holding firm; **no software Product-Line for now** (its software is AIXO.Dev); client-engagement SDK etc. TBD est. 2027.

---

## 11. Ceremony Level — from a flag to a first-class, prompt-bearing entity

*(§11-A — TastyPal structure — CONFIRMED by John; reflected in §10.)*

You took "rename `research_scope`" and turned it into a much better idea: make the rigor/formality value a **first-class entity** (`CeremonyLevel`) that humans define per project and that **carries the behind-the-scenes prompt presets** injected for Claude/Codex. I'm strongly for it. **Key-name: `ceremony_level`** (you liked it; it's the agile term-of-art for exactly "how much process formality"). Here's the analysis you asked for.

### Synonyms + extensible values — three ramifications to design around (so it doesn't bite later)

1. **Keep an explicit ORDINAL.** Levels must stay *comparable* ("is this build more formal than that one?", "escalate the rigor on graduation"). So `CeremonyLevel` carries a numeric `sort_order` (e.g. `playground`=10, `standard`=50, `formal`=90). New levels slot in by ordinal; comparisons/escalation keep working.
2. **Synonyms are ALIASES of one canonical level — not separate values.** `low` and `playground` should be the *same* level (one `id`, one ordinal, two display aliases), `high`/`formal` the same — otherwise filters/queries drift and "low" vs "playground" silently split your data. So: `ceremony_level_aliases(level_id, alias)`; the BuildLine stores the canonical `ceremony_level_id`; the UI lets you type/show any alias but always resolves to the canonical level. You get the "wider set of words" with zero drift.
3. **Global defaults + per-project overrides.** "Define them in the web-UI per project" → levels are global by default, with optional per-Owner overrides of the *prompt text* (not the ordinal/identity). Start global in v0.5; add per-Owner template overrides at the real-platform stage.

### Your bigger vision (prompt templates + evals) — YES, and here's where it lives

Each `CeremonyLevel` becomes the anchor for **versioned, agent-specific prompt presets** that get injected behind the scenes:
- `ceremony_prompt_templates(level_id, agent_target ∈ {claude, codex, generic}, role ∈ {lead, worker, solo}, template_text, version, is_active, eval_score, created_at)`.
- So a Build-Line tagged `formal` auto-injects the high-rigor preset (spec-first, adversarial review, full coverage); `playground` injects "vibe-code it, skip the ceremony, optimize for speed" — **separately tuned for Claude vs Codex**, and for collab-group **lead vs worker** roles.

This is bigger than a throwaway-SQLite concern, so my recommendation on **scope**: build the **minimal `CeremonyLevel` entity now** in GEN2 (id · slug · `display_name` · `sort_order` · `description` · `is_default`, + aliases, + `BuildLine.ceremony_level_id`, seeded `playground`/`standard`/`formal`) so the FK, the ordinal, the aliases, and "define levels in the UI" all exist — and **defer the prompt-template + eval machinery to the real AIXO.Dev Platform** (`aixodev-web`), where prompts, evals, and per-project overrides belong. The GEN2 schema is then *ready* for that layer without over-building the prototype.

### The wildly-imaginative part (what this unlocks)

- **Ceremony × Build-Envelope = the agent's full "mission briefing."** Envelope says *what scale/stack to build for*; ceremony says *how much process formality* — together they're the complete, auto-assembled context preset handed to any agent on spawn. No more "read 30 docs first."
- **Self-improving presets.** Track build outcomes against the level used → score the templates → A/B competing prompt variants per level → the presets *get better over time* (your "evals of prompt-refinement"). The collaboration literally compounds.
- **Cascade + auto-escalation.** Ceremony can inherit (Venture default → Product-Line → Build-Line) and *escalate on graduation*: a `playground` line's `merges-into` edge can auto-flip the receiving Stage to `formal`. The "training wheels come off" automatically when code heads for production.
- **The real prize (you named it):** the web-UI becomes the place where you + I **co-author and version the collaboration presets** — the durable "operating agreement." Every future Claude/Codex instance inherits a stable, eval-tuned baseline and hits peak human-AI collaboration *instantly*, right out of the gate, without re-deriving it from dozens of documents. That's a genuine compounding-alignment flywheel, and it's exactly the AIXO.Dev thesis (make the collaboration legible, reusable, improvable) made concrete at the Build-Line level.

**→ Decisions for you:** (a) key-name **`ceremony_level`** + the **`CeremonyLevel` entity** — good? (b) initial levels/aliases (I propose `playground` {low, vibe} · `standard` {medium, normal} · `formal` {high, rigorous} — edit freely); (c) confirm we build the **minimal entity now** and defer the prompt-template/eval system to `aixodev-web`. *(Resolved — approved; we shipped the minimal `CeremonyLevel` entity in GEN2, with the prompt-template/eval system deferred to `aixodev-web`.)*
