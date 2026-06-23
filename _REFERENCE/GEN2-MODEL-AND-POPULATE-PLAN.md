# GEN2 Model Revision (Owners · Product-Lines · Build-Line Generations) + Populate Plan

> **Working spec, 2026-06-23 (John + Claude).** Consolidates the model revisions agreed across this session — the **Owner (Party) supertype**, **Product-Line ⇄ Build-Line** structure, and **Build-Line Generations** — plus the venture-by-venture populate plan. This is the build target for the next `aixodev-GEN2` schema/UI pass; once it stabilizes it folds back into the canonical [`PROJECT-ORGANIZATION-MODEL.md`](PROJECT-ORGANIZATION-MODEL.md) + [`STRATEGIC-LANDSCAPE-MODEL.md`](STRATEGIC-LANDSCAPE-MODEL.md). Optimizing for the **v1 graph-DB accuracy**, not SQLite-scope convenience. **Status: design only — nothing below is built in the running app yet** (the server on :5000 still holds the prior Venture-owned schema with the 12 ventures + seed topics/ideas).

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

- **`BuildLine`** — `name` (**non-unique** — a human label; identity is `id`, so "DailySpikeDriver" can recur freely), `build_envelope_id` (single FK, conditional), `research_scope` (`playground` = the DailySpikeDriver/personal-experiment class · `optimization-target`; see §11-B on the key-name), `description`.
- **`build_line_owners`** (M2M) — `build_line_id`, `owner_id`, `role`. **Co-ownership is unlimited:** a Build-Line can be owned by `[Venture] + [Person:John] + [Person:David] + …` (the Digital-Insight-1997 two-devs-plus-the-company case). Only `UNIQUE(build_line_id, owner_id)` (no dup owner); no "single account" limit anywhere. `role` (e.g. `sponsor`/`lead`/`contributor`) is also the future ACL/permissions hook.
- **`build_line_repositories`** (M2M) — `build_line_id`, `repository_id`, `role`, `status`, `is_primary`. Which repos a Build-Line uses (web/flutter/android/…); a repo is shared across Build-Lines only when the stack stays continuous.
- **`Stage`** (reset `v1→v2→v3` per Build-Line) → **`Phase`** → **`Sprint`**. A techstack pivot makes a *new* Build-Line starting at `v1`, never a `v5` of the old one.

## 4. Build-Line Generations & lineage

- **`build_line_edges`** — `source_build_line_id`, `target_build_line_id`, `edge_type`, `note`, `UNIQUE(source, target, edge_type)`, `CHECK(source ≠ target)`. A real M2M-cross-reference (the linked-list), edited **only on the Build-Line detail page**, never a top-level menu.
- **`edge_type` values:** `succeeds` (**= the Generation link**: `source` is the next-gen successor of `target`, e.g. `aixodev-GEN2 --succeeds--> aixodev-web`) · `forked-from` (a personal experiment forked off a main line) · `merges-into` (the GitHub-PR-upstream flow).
- **Generation number is DERIVED** (`1 + length of the succeeds-chain behind it`) → shown as a "Gen N" badge; not a stored int (avoids renumber-drift). ORM exposes `BuildLine.successors` / `.predecessors` and a derived `.generation`.
- **The techstack-pivot rule is a HEURISTIC, not DB-enforced.** `build_line_edges` lets you add a `succeeds` between *any* two Build-Lines, so deliberate exceptions are fine — e.g. `aixodev-web` → `aixodev-GEN2` is a clean-rebuild `succeeds` even though both stay Python/Flask. The rule ("techstack change → new Build-Line at v1; same techstack → same Build-Line, just a repo rename") guides the common case; the edge table never blocks the rare "exception that proves the rule."
- **Personal-Build-Line creation convention (confirmed):** default to a **standalone** spike (fresh project) unless you're modifying existing product code, in which case **fork-from-current** (`forked-from` edge); either way a **`merges-into`** edge records the upstream graduation, and `research_scope=playground` + a Person co-owner marks it personal/experimental. (Claude-era lift-and-shift makes the standalone path cheap — partial functionality moves between lines without git-clone/merge ceremony.)
- **No techstack denormalization.** The techstacks live on `repository_techstacks`; "find all Python/Flask Build-Lines succeeded by Rust ones" is a clean multi-hop join now and a native graph traversal in v1. The ORM association-proxy gives `build_line.successors[0].techstacks` without copying.
- **Payoff (future AIXO.Dev security/CVE tracking):** a CVE matched to a techstack → the affected (production-deployed) Build-Lines → automatically re-check their `succeeds` successors and record a "verified the Rust successor is not also vulnerable to this JWT flaw" status. Needs zero new schema beyond this edge + the existing techstack links.

## 5. Product-Lines, the PL⇄BL structure, Version-Releases

- **`ProductLine`** — `owner_id` (FK → Owner; usually a Venture, but a Person/Org can ship products too), `slug`, `name`, `description`.
- **`product_line_build_lines`** (M2M) — `product_line_id`, `build_line_id`, `status` (`current` | `planned` | `far-horizon` | `retired`), `UNIQUE(pl, bl)`. The structural "which Build-Lines build this product." Lets EstimatePacket (`current`) **and** National-AVM (`far-horizon`) both belong to FracRealHomes' Valuation Product-Line; a Build-Line can belong to zero Product-Lines (pure experiment), one, or several (a shared backend feeding many app Product-Lines).
- **`VersionRelease`** — `product_line_id`, `version`, `release_date`, `status`, `stage_id` (the moving symlink → `[Build-Line→Stage]`); `version_release_milestones` (M2M). *(Soft invariant: a release's stage's Build-Line should be one of its Product-Line's associated Build-Lines.)*
- **`Milestone`** — `name`, `milestone_date`, `team`, `description`; `stage_milestones` (M2M) + `version_release_milestones` (M2M). Business/HR (bonus-linked, team-scoped); may later be authored in KSVGPS and synced back.
- **The "(service)" vs "Community Edition" split means different things per venture.** For most (e.g. **LegendaryMoney**) the AGPLv3 self-host edition and the commercial closed SaaS are roughly the *same product* under different licenses (with a Python-open → Rust-commercial / CLA-relicensing caveat). For **DiviaHome** it is *not*: the Community Edition (AGPLv3 + Commercial, CLA-governed Python/Flask, free on GitHub) is one thing, but the **Global Service** at `diviahome.com` is a separate federation / message-queue-relay SaaS (TBD) — **not** a commercial clone of the GitHub app. DiviaHome's dual-license + CLA exists to clear a **future smart-home-hardware product-line** (a "DiviaHome Hub" device — router / DNS / DHCP + a preinstalled, likely-Rust, commercial DiviaHome server matching the Python community functionality; the CLA legally clears rewriting contributed Python → Rust for that closed product). Far-future (2028+; hardware via Shenzhen + tariff/trade complexity) — a `[DEALBREAKER-HOOK]`-style license decision made *now* for a future scenario. *(More detail — incl. the high-priority China trademark plan for "Divia" names — lives in the ~100-page "Divia Trademark Guide" research from last summer, to be re-imported into KSVGPS as we build the graph-DB.)*

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
- **Migration:** the existing ventures → `Owner(kind=venture)` + `Venture` rows; **drop the DiviaLife Owner** (folded into DiviaHome). Topics/Ideas/links unaffected. Hard-gate `export-all-data` first.

---

## 9. Populate plan — SUMMARY  *(authoritative editable hierarchy is §10)*

| Venture (display) | Product-Lines | Current Build-Line(s) |
|---|---|---|
| **Divia.AI** | Global Service · Professional · Enterprise | DiviaGlobalService · DesktopOutliner · DiviaServerPrototype (+ WorkgroupServer `far-horizon`, Rust, `succeeds`) |
| **DiviaHome** | Service · Community Edition · Divia.Life · *(future: DiviaHome Hub hardware)* | GlobalHomeService · CommunityHomeHub · LifeCardMessenger |
| **LegendaryMoney** | Service · Community Edition | ConfidenceLedger (web+flutter) · HouseholdLedger |
| **Kingmaker Strategic** | AdVentureGPS / KSVGPS | AdVentureGPS |
| **TastyPal** | *under discussion — see §10 + §11-A* | *(central backend + per-app clients)* |
| **Sattvasic Health** | Service · Community Edition | VitalsGlobalService · VitalsDataLake |
| **FracRealHomes** | Property Valuation *(+ future ADU-Evaluation)* | EstimatePacket `current` (+ National-AVM `far-horizon`); personal DailySpikeDriver × John |
| **CrowdMadness** | CrowdMadness | PredictionArena *(pre-code)* |
| **Patternicity** | PatternicityNews · …News Reader · Patternicity.Social | PTNewsFeed · PTNewsReaderApp · PTSocialNews *(pre-code)* |
| *Deferred:* **AIXO.Dev** (BL-A…E) · **ExoDev.Pro** (no software PL) | | |

---

## 10. Populate plan — EDITABLE HIERARCHY  *(edit freely and resend; `display name` uses proper spelling, slugs/repos use the machine form)*

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
  - Product-Line: **Divia.Life** (cross-platform mobile app, with messaging of DiviaCard types/objects) *(absorbed from the retired DiviaLife venture)*
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
- **TastyPal**  *(structure under discussion — see §11-A for the revised "central backend + per-app clients" recommendation; the rows below are your current sketch)*
  - Product-Line: **TastyPal (service)** (the `tastypal.com` central SaaS backend powering all three apps: taste-preferences, restaurant matching, "others like you also like" engine, cross-app coordination)
    - Personal Build-Line × `johnstanforth`: **TastySpikeDriver**  ·  repo: `spicemaster3000` *(repo to be renamed; personal playground co-owned by `tastypal` + `johnstanforth`)*
    - Current Build-Line: **TastePalatesEngine**  ·  repo: `tastypal-web`
  - Product-Line: **TastyPal** (mobile app — taste-preferences / restaurant matching subset)
    - Current Build-Line: **TastePalatesEngine**  ·  repo: `tastypal-flutter`
  - Product-Line: **TastyPantry (by TastyPal)** (household kitchen/pantry inventory app)
    - Current Build-Line: **CorePantryMobile**  ·  repo: `tastypantry-flutter`
  - Product-Line: **TastyPantry: Community Edition** (self-hosted pantry web app; federates with `tastypal.com`)
    - Current Build-Line: **CommunityPantry**  ·  repo: `tastypantry-community`
  - Product-Line: **TastyTrucks (by TastyPal)** (food-truck locator matched to your TastyPal taste-preferences; combines the award-winning GridTransmit/SensoryMQ GPS/IoT fleet-tracking platform with the food-trucks use-case)
    - Current Build-Line: **TastySpatialGPS**  ·  repos: `tastytrucks-web` + `tastytrucks-flutter`
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
  - Product-Line: **ADU-Evaluation-Service** *(? — future)*
    - Current Build-Line: [TBD]
- **CrowdMadness**
  - Product-Line: **CrowdMadness** (prediction-market game)
    - Current Build-Line: **PredictionArena**  ·  (pre-code)
- **Patternicity**
  - Product-Line: **PatternicityNews** (news portal)
    - Current Build-Line: **PTNewsFeed**  ·  (pre-code)
  - Product-Line: **PatternicityNews Reader** (cross-platform desktop RSS/News reading app)
    - Current Build-Line: **PTNewsReaderApp**  ·  (pre-code)
  - Product-Line: **Patternicity.Social** (Twitter/BlueSky/Mastodon-like social network for discussion)
    - Current Build-Line: **PTSocialNews**  ·  (pre-code)

### Deferred (think more first)

- **AIXO.Dev** — multiple product-lines (Platform · aixocode · Professional); maps to BL-A…E in [`MIGRATION-AND-SELF-HOSTING-PROPOSAL.md`](MIGRATION-AND-SELF-HOSTING-PROPOSAL.md). Confirm the breakdown later.
- **ExoDev.Pro, Inc.** — services/holding firm; **no software Product-Line for now** (its software is AIXO.Dev); client-engagement SDK etc. TBD est. 2027.

---

## 11. Open questions (for your decision — reply inline, I'll fold in)

**A — TastyPal structure (revised after your clarification: one central backend serving three app-clients).**

Your layout: `tastypal.com` is the **central SaaS backend** holding all server-side functionality; **TastyPal / TastyPantry / TastyTrucks** are three mobile apps each exposing a named subset; **TastyPantry: Community Edition** is a self-host Python/Flask app that *federates* back to the global service. The model handles this cleanly via the M2M — here's the revised shape I'd propose (replacing the earlier "one TastePalatesEngine spanning everything" sketch):

- **One shared backend Build-Line** — `TastyServiceBackend` (repo `tastypal-web` / `tastypal-service`) — associated `current` with **all three** app Product-Lines (the "shared infra Build-Line feeding multiple Product-Lines" case `product_line_build_lines` was built for).
- **One Build-Line per mobile app** — `TastyPalMobile` (`tastypal-flutter`), `TastyPantryMobile` (`tastypantry-flutter`), `TastyTrucksMobile` (`tastytrucks-flutter`) — each `current` for its own app Product-Line.
- **TastyPantry: Community Edition** — its own Product-Line + `CommunityPantry` Build-Line (`tastypantry-community`), which *federates* with the backend (a relationship we can model explicitly later; for now a `note`).
- *(Optionally a **"TastyPal Platform"** Product-Line if you ever sell/position the `tastypal.com` service itself as a product, vs. treating it purely as shared infra.)*

The win vs. your current §10 sketch: the backend is **its own** Build-Line shared across the app Product-Lines, and each app is **its own** Build-Line — instead of conflating `-web` + `-flutter` into one line listed twice. **→ Take this to your colleagues; tell me which Product-Lines / Build-Lines to actually create.**

**B — Is `research_scope` the right key-name?**

- **What it is:** a per-Build-Line flag — `playground` (throwaway/experimental — hands-off, vibe-code-it-now, research = OFF) vs `optimization-target` (serious/production-bound — research = ON). The "engineering SortingHat": *whether to invest rigor/optimization in this line at all.*
- **Where it's used:** only on the Build-Line (and as a future scoping signal for agents). It is **distinct from the Build Envelope** — the *Envelope* is the "build it FOR this scale/team/timeframe/stack" context handed to Codex to stop it over-engineering to IANA-200-page specs. So the "don't over-spec / right-size the solution" job you described is the **Build Envelope's**, not `research_scope`'s.
- **Naming:** the current name works but "research" is a bit oblique. If we rename, I'd suggest **`build_disposition`** or **`rigor_mode`** (values `playground` / `optimization-target`) over `architecture_scope` (which would wrongly imply architecture-sizing — that's the Envelope's job). **→ Keep `research_scope`, or rename to `build_disposition` / `rigor_mode`?** (No rush — a tiny rename whenever you decide.)
