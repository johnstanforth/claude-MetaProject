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
  - Product-Line: **Divia.AI Global Service** (online/hosted SaaS subscription service at `divia.ai`)
    - Current Build-Line: **DiviaGlobalService**  ·  repo: `divia_ai-globalservice`
  - Product-Line: **Divia.AI Professional** (desktop outliner)
    - Current Build-Line: **DesktopOutliner**  ·  repo: `divia_ai-professional`
  - Product-Line: **Divia.AI Enterprise** (teams/workgroups server)
    - Current Build-Line: **DiviaServerPrototype**  ·  repo: `proto-divia_ai-enterprise`
    - Far-horizon Build-Line: **WorkgroupServer**  ·  repo: `divia_ai-enterprise`   ·  **`succeeds` DiviaServerPrototype** — Gen 2; the Rust techstack pivot is *exactly* what makes it a generation (this was inverted in the edit — see Q&A 1)
- **DiviaHome**
  - Product-Line: **DiviaHome (service)** (online/hosted SaaS subscription service at `diviahome.com`)
    - Current Build-Line: **GlobalHomeService**  ·  repo: `diviahome-service`
  - Product-Line: **DiviaHome: Community Edition** (self-hosted open-source household hub)
    - Current Build-Line: **CommunityHomeHub**  ·  repo: `diviahome-community` *(renamed from `diviahome-web` — same techstack & scope, so the SAME Build-Line; just a repo rename, NOT a Gen-2/`succeeds`. You had this one right — see Q&A 1.)*
  - *(DiviaLife dropped as a standalone venture — its Divia.Life product-line now lives under DiviaHome; see Q&A 5.)*
  - Product-Line: **Divia.Life** (cross-platform mobile app, with messaging of DiviaCard types/objects)
    - Current Build-Line: **LifeCardMessenger**  ·  repo: `divialife-flutter`
- **LegendaryMoney**
  - Product-Line: **LegendaryMoney (service)** (AI personal-finance manager)
    - Current Build-Line: **ConfidenceLedger**  ·  repo: `legendarymoney-web` + repo: `legendarymoney-flutter` 
  - Product-Line: **LegendaryMoney: Community Edition** (self-hosted open-source personal-finance manager web application)
    - Current Build-Line: **HouseholdLedger**  ·  repo: `legendarymoney-community`
- **Kingmaker Strategic**
  - Product-Line: **AdVentureGPS / KSVGPS** (venture-studio OS)
    - Current Build-Line: **AdVentureGPS**  ·  repo: `kingstrat-adventuregps`
- **TastyPal**
  - Product-Line: **TastyPal (service)** (online/hosted website/service for taste-preferences, finding restaurants your taste-palate will like, "others like you also like" recommendation engine, coordination of TastyPal+TastyPantry mobile apps, etc)
    - Personal Build-Line x `johnstanforth`:  **TastySpikeDriver**   ·  repo: `spicemaster3000` *(repo to be renamed; old `spicemaster3000` placed here = a personal playground line co-owned by `tastypal` + `johnstanforth`)*
    - Current Build-Line: **TastePalatesEngine**  ·   repo: `tastypal-web`
  - Product-Line: **TastyPal** (mobile app for taste-preferences, finding restaurants your taste-palate will like, others like you also like, etc)
    - Current Build-Line: **TastePalatesEngine**  ·   repo: `tastypal-flutter`
      - *(Q&A 2: yes — one Build-Line can span multiple Product-Lines and bundle `-web` + `-flutter` repos; see the recommendation there.)*
  - Product-Line: **TastyPantry (by TastyPal)** (household kitchen/pantry inventory app)
    - Current Build-Line: **CorePantryMobile**  ·  repo: `tastypantry-flutter`
  - Product-Line: **TastyPantry: Community Edition** (self-hosted household kitchen/pantry inventory web app)
    - Current Build-Line: **CommunityPantry**  ·  repo: `tastypantry-community`
  - Product-Line: **TastyTrucks (by TastyPal)** (online site showing the location of food-trucks in your area, showing which ones match your TastyPal taste-preferences, etc; combines our award-winning GridTransmit/SensoryMQ GPS/IoT Fleet-Tracking platform with the food-trucks use-case)
    - Current Build-Line: **TastySpatialGPS** ·  repo: `tastytrucks-web` +  repo: `tastytrucks-flutter`
- **SattvasicHealth**
  - Product-Line: **SattvasicHealth** (health-metrics aggregator)
    - Current Build-Line: **VitalsAggregator**  ·  repo: `sattvasichealth`
- **FracRealHomes**
  - Product-Line: **Property Valuation** (the diligence/estimate product)
    - Personal Build-Line x `johnstanforth`:  **DailySpikeDriver**   ·  repo: `fracrealhomes-johnstanforth`   
      - *(I want to build `fracrealhomes-johnstanforth` soon — a small Python/Flask spike, starting with Gmail-parsing of Zillow/Redfin emails. Personal-Build-Line process — standalone vs fork-from-current — in Q&A 3.)*
      - *(Q&A 4: yes — `build_line_owners` allows unlimited co-owners, e.g. `fracrealhomes` + `johnstanforth` + `davidlang`; confirmed, with implications reasoned through there.)*
    - Current Build-Line: **EstimatePacket** `current`  ·  repo: `fracrealhomes-web`
    - Far-horizon Build-Line: **National-AVM** `far-horizon`  ·  (succeeds EstimatePacket)
  - Product-Line: **ADU-Evaluation-Service** (?) — future
    - Current Build-Line: [TBD]
- **CrowdMadness**
  - Product-Line: **CrowdMadness** (prediction-market game)
    - Current Build-Line: **PredictionArena**  ·  (pre-code)
- **Patternicity**
  - Product-Line: **PatternicityNews** (news portal)
    - Current Build-Line: **PTNewsFeed**  ·  (pre-code)
  - Product-Line: **PatternicityNews Reader** (cross-platform desktop RSS/News reading app)
    - Current Build-Line: **PTNewsReaderApp**  ·  (pre-code)
  - Product-Line: **Patternicity.Social** (Twitter/BlueSky/Mastodon-like social network to discuss )
    - Current Build-Line: **PTSocialNews**  ·  (pre-code)



### Deferring These for Now:  (I want to think more about these first)

- **AIXO.Dev**  *(FLAG: multiple product-lines; you already have BL-A…E in MIGRATION-AND-SELF-HOSTING-PROPOSAL.md — confirm the breakdown)*
  - Product-Line: **AIXO.Dev Platform** (the web app)
    - Current Build-Line: **PlatformGraph** (= GEN2 / BL-B)  ·  repo: `aixodev-GEN2`
  - Product-Line: **aixocode** (the TUI)
    - Current Build-Line: **(name?)**  ·  repo: `aixodev-aixocode`
  - Product-Line: **AIXO.Dev Professional** (desktop) — future
    - Current Build-Line: **(name?)**
- **ExoDev.Pro, Inc.**  *(FLAG: services/holding firm — likely no software Product-Line; its software is AIXO.Dev)*
  - *(John confirmed-- no software Product-Line for now; client-engagement SDK, etc, TBD est. 2027)*

---

## 11. Q&A (answered 2026-06-23 — reply inline under any answer; I'll fold your replies back in)

**Q&A 1 — When is it a NEW Build-Line / `succeeds` (Gen 2), vs the SAME Build-Line?** *(covers your Divia.AI-Enterprise and DiviaHome-Community notes — which pointed opposite ways, so here's the single rule.)*

The discriminator is **techstack**:
- **Techstack CHANGES** (Python/Flask → Rust): a **new Build-Line**, a new generation, starting internally at **Stage v1**, linked by a **`succeeds`** edge. → So **WorkgroupServer (Rust) DOES `succeed` DiviaServerPrototype (Python)** — the Rust pivot is *precisely* what makes it a Gen-2, not what disqualifies it. (Your Enterprise note had this inverted.)
- **Techstack STAYS THE SAME** (just renaming `diviahome-web` → `diviahome-community`, same Flask, same scope): the **SAME Build-Line** — no new generation, no `succeeds`, just rename the Repository (or swap it in `build_line_repositories`). → Your DiviaHome-Community note had this **right**.

Mnemonic: **`succeeds` = a techstack pivot; same techstack = same Build-Line.** Stages (v1→v4) progress *within* one Build-Line on one techstack; crossing to a new techstack starts a new Build-Line at v1 linked by `succeeds`. *(Applied in §10: WorkgroupServer marked `succeeds`; CommunityHomeHub marked same-BL repo rename.)*

**Q&A 2 — Can one Build-Line span multiple Product-Lines AND bundle multiple repos (`-web` + `-flutter`)?**

**Yes on both.** `product_line_build_lines` is M2M (a Build-Line can belong to many Product-Lines) and `build_line_repositories` is M2M (a Build-Line can bundle many repos — exactly like FracRealHomes' EstimatePacket = {web, flutter, android}). So your "TastePalatesEngine" with `tastypal-web` + `tastypal-flutter`, in both the service and mobile Product-Lines, is fully valid.

My recommendation: decide by whether the mobile app is a **separate product** (its own release cadence / market identity → keep it a separate Product-Line, sharing the one Build-Line via the M2M, or split into its own Build-Line) or a **client of the same product** (→ one "TastyPal" Product-Line, one "TastePalatesEngine" Build-Line bundling both repos with `role`=backend/service vs mobile). From your description (mobile = a subset-functionality client of the `tastypal.com` service), I'd lean **one Product-Line + one Build-Line + two repos** — cleaner, with the web/flutter distinction living on the repo `role`, not duplicated in the product structure. But the model supports your two-PL version too. (Note: Flask vs Flutter are different techstacks, but here they're *parallel components*, not a `succeeds` succession — different rule from Q&A 1.) **→ Your call: consolidate to one TastyPal PL, or keep service/mobile as two?**

**Q&A 3 — Process for creating personal Build-Lines (standalone vs git-cloned from the Current Build-Line)?**

Both are first-class, and `build_line_edges` records which:
- **Standalone spike** — fresh Python/Flask, unrelated to the main codebase's structure (e.g., a Gmail-parser that just needs IMAP + regex). No `forked-from` edge; when it contributes code upstream, add a **`merges-into`** edge to the Current Build-Line. Best for self-contained modules.
- **Fork-from-current** — git-clone the Current Build-Line's repo and hack in-context. Add a **`forked-from`** edge; PR features up via **`merges-into`**. Best when prototyping a change *to* the existing product.

For your **`fracrealhomes-johnstanforth` Gmail-parser**: it's a fairly self-contained parser feeding EstimatePacket's valuation inputs, so I'd default to a **standalone spike** (`research_scope=playground`, co-owned `fracrealhomes` + `johnstanforth`) with a **`merges-into` EstimatePacket** edge once a feature is ready to graduate.

**Proposed convention (needs your sign-off):** personal Build-Lines default to **standalone** unless you're modifying existing product code, in which case **fork-from-current**; either way a **`merges-into`** edge records the upstream graduation, and `research_scope=playground` + a Person co-owner marks it personal/experimental. **→ Does that match how you want this process to work?**

**Q&A 4 — Can a Build-Line have multiple person-owners + the venture (e.g., `fracrealhomes` + `johnstanforth` + `davidlang`)?**

**Yes, unlimited.** `build_line_owners` is a true M2M; the only uniqueness is `(build_line_id, owner_id)` (can't add the *same* owner twice), so any number of distinct owners is fine. Your Digital Insight 1997 example = one Build-Line owned by `[Venture] + [Person:John] + [Person:David]`, `research_scope=optimization-target` (a serious rebuild, not a playground). **No "single personal account" constraint exists anywhere — confirmed by design.** Implications:
- The link's **`role`** column distinguishes them (venture = `sponsor`; the two devs = `lead`/`contributor`) — useful for display and a future ACL/permissions hook (who can edit/merge).
- The Build-Line shows up under **all three** owners' detail pages — correct, it's genuinely shared.
- Ownership ≠ Product-Line association ≠ generation-lineage stay independent (the three-orthogonal-relations principle), so co-owning doesn't entangle the product structure.
- If we ever add a "primary owner," it'd be a `role`/flag on the link, **never** a structural single-owner limit.

**Q&A 5 — Structure changes I applied from your edits** *(verify these):*
- **DiviaLife removed as a standalone venture**; "Divia.Life" is now a Product-Line under **DiviaHome**. At populate time I'll drop the DiviaLife Owner and create the Divia.Life PL under DiviaHome.
- The recurring **"(service)" vs "Community Edition"** split (Divia.AI Global Service; DiviaHome service + community; LegendaryMoney service + community; TastyPantry + community) = just multiple Product-Lines per Venture — fully supported; it cleanly encodes the commercial-hosted-SaaS vs AGPL-self-hosted dual-license pattern.
- **AIXO.Dev** + **ExoDev.Pro** deferred (ExoDev confirmed no software Product-Line; client-engagement SDK ~2027).
- **Net populate count:** 12 ventures → **11** (DiviaLife gone); AIXO.Dev + ExoDev deferred → **9 ventures populated now**: Divia.AI, DiviaHome, LegendaryMoney, Kingmaker Strategic, TastyPal, SattvasicHealth, FracRealHomes, CrowdMadness, Patternicity. *(The DiviaLife Owner row is deleted in the migration; ExoDev.Pro + AIXO.Dev remain as Owner/Venture rows with no Product-Lines/Build-Lines yet.)*
