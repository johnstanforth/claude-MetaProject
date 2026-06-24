# GEN2 Repo Reconciliation — database repos vs. on-disk repos (2026-06-23)

> Cross-references the **Repository** rows now in the `aixodev-GEN2` database (the "aspirational future" repo names, attached to current/far-horizon Build-Lines) against the repos that **actually exist on disk** (the `_projects/` symlinks) and their **real git remotes**. Goal: find existing repos that closely match a *current Build-Line* so they can be **adopted almost as-is** (de-frozen from "scavenge-source" → the real repo for that Build-Line), rather than re-created from scratch.
>
> ⚠️ All names are **working drafts** — freely rearrangeable right now; decide each on its own merits, don't defer (see [`GEN2-MODEL-AND-POPULATE-PLAN.md`](GEN2-MODEL-AND-POPULATE-PLAN.md)). Every repo except `aixodev-GEN2` and the **5 now-adopted** ones (see the **Done** table in §1) is "frozen scavenge-source" status today. Code-maturity below is from the `_projects/README.md` index (an automated scan misreads nested `src/` layouts); git remotes were verified live via `git remote -v`.

## 1. Reconciliation table — DB Repository × on-disk reality

Split into **pending** (still to adopt/create), **🔍 still investigating** (unaccounted-for on-disk dirs), and **✅ done** (already adopted/migrated) below.

### Pending — still to adopt or create

| DB repo (Build-Line `[status]`) | Owner | On disk? | Git remote (real) | Verdict |
|---|---|---|---|---|
| **divialife-flutter** (LifeCardMessenger `current`) | DiviaHome | ✅ yes | `DiviaLife/divialife-flutter` | ADOPT (scaffold-only, Phase 00) — repo + remote exist, no app code yet |
| **fracrealhomes-web** (EstimatePacket `current`) | FracRealHomes | ✅ yes | LOCAL-ONLY | ADOPT + create GitHub remote (scaffold-only, Phase 00) |
| **legendarymoney-web** (ConfidenceLedger `current`) | LegendaryMoney | ✅ yes | LOCAL-ONLY | ADOPT + create remote (Phase 00, ~7 commits) |
| **sattvasichealth-community** (VitalsDataLake `current`) | Sattvasic Health | ✅ as `sattvasichealth` | LOCAL-ONLY | RENAME & ADOPT — `sattvasichealth` → `sattvasichealth-community` (+ create remote) |
| **tastypantry-community** (CommunityPantry `current`) | TastyPal | ✅ as `tastypantry` | `TastyPal/tastypantry` | RENAME & ADOPT — `tastypantry` → `tastypantry-community` |
| **divia_ai-enterprise** (WorkgroupServer `far-horizon`) | Divia.AI | ✅ yes | LOCAL-ONLY | KEEP placeholder — far-horizon Rust rewrite; intentionally not started |
| divia_ai-globalservice (DiviaGlobalService `current`) | Divia.AI | ❌ no | — | CREATE (aspirational) |
| diviahome-service (GlobalHomeService `current`) | DiviaHome | ❌ no | — | CREATE (the closed federation-relay SaaS) |
| legendarymoney-community (HouseholdLedger `current`) | LegendaryMoney | ❌ no | — | CREATE |
| legendarymoney-flutter (ConfidenceLedger `current`) | LegendaryMoney | ❌ no | — | CREATE |
| sattvasichealth-globalservice (VitalsGlobalService `current`) | Sattvasic Health | ❌ no | — | CREATE |
| fracrealhomes-dailyspikedriver (DailySpikeDriver `current`, personal) | FracRealHomes | ❌ no | — | CREATE — your planned Gmail/Zillow-parsing spike |
| tastypal-backend / tastypal-web (TastePalatesEngine `current`) | TastyPal | ❌ no | — | CREATE (TastyPal is pre-code) |
| tastypal-flutter (TastyPalMobile `current`) | TastyPal | ❌ no | — | CREATE |
| tastypantry-flutter (TastyPantryMobile `current`) | TastyPal | ❌ no | — | CREATE (disk `tastypantry` is the *web* edition) |
| tastytrucks-flutter / tastytrucks-gps (`current`) | TastyPal | ❌ no | — | CREATE |

### 🔍 Still investigating — on-disk dirs not yet accounted for (2026-06-24)

A sweep of `~/Code/<Owner>/` across John's two dev machines — **@jsdesk** (Linux desktop, the one live-probed) and **@jsmacmini** (Mac mini, from a dir-tree John pasted, not yet probed) — for project dirs created over the past few years that **haven't** come up in our modeling discussions and aren't in the Pending/Done tables or the §3 already-placed list. Goal: identify each and check whether it (or its domain) was missed in `DOMAIN_LIST` / the v0.1 docs. The **Server/Host** column tags where each lives (some repos exist on only one machine). Convention: a `_domain.tld` (underscore-prefixed) dir is a **website/template container** for that domain — all empty here, so each is effectively a *domain to verify*.

On **@jsdesk**, only 3 dirs have real content + git history (★) and the rest are empty stubs; the **@jsmacmini** rows are repos that exist **only on the Mac** — including the `DiviaFoundation` repo that was missing on @jsdesk:

| Dir (`~/Code/<Owner>/…`) | Owner | Server/Host | State | Git (remote · commits) | Likely identity / to investigate |
|---|---|---|---|---|---|
| **`aixodev-LEGACY`** | AIXO.Dev | @jsdesk | content (48) | origin → `aixodev/aixodev-web` · **366 commits** | ★ Real repo — a legacy clone of `aixodev-web` (origin points there; carries `.bsync-snap` files). Pre-rewrite snapshot/archive? Compare vs current `aixodev-web`; decide keep-as-archive vs retire. |
| **`dotfig_proto_cc`** | Dotfigurator | @jsdesk | content (13) | local-only · 4 commits | ★ Real repo — a dotfiles/config-tooling prototype (atuin, fish, `_documentation`). Never modeled. Is **Dotfigurator** a tool/venture to add to GEN2? |
| **`velocityterminal`** | VelocityTerminal | @jsdesk | content (9) | local-only · 2 commits | ★ Real repo — early scaffold (specs + research + CLAUDE.md). **VelocityTerminal** is noted as a non-venture owner; this is its actual repo. Model it? |
| `DiviaFoundation/` | DiviaFoundation | @jsdesk | **empty** | — | Owner folder — **empty on @jsdesk because its repo `opensoftwarelib-web` lives on @jsmacmini** (see below). Sync/move it over. |
| `fracreality-adu-eval` | FracRealHomes | @jsdesk | **empty** | — | Stub. Name ⇒ **ADU** (accessory-dwelling-unit) evaluation tool — a planned FracRealHomes sub-product not in the model. |
| `fracreality-avm` | FracRealHomes | @jsdesk | **empty** | — | Stub. **AVM** = automated valuation model — likely the "next-gen Zillow estimate" engine; reconcile with `fracrealhomes-web`'s EstimatePacket Build-Line. |
| `tastypal-mobile` | TastyPal | @jsdesk | **empty** | — | Stub. Pending table calls this `tastypal-flutter` (TastyPalMobile) — same thing pre-stubbed under a different name? Reconcile. |
| `tastypal-web` | TastyPal | @jsdesk | **empty** | — | Stub. **Discrepancy:** Pending table lists `tastypal-web` as ❌-not-on-disk CREATE, yet this (empty) dir exists. |
| `txfrapp-android` · `txfrapp-ios` | TXFR.Cloud | @jsdesk | **empty** | — | Stubs — planned native apps. |
| `txfrcloud-cli` · `txfrcloud-daemon` · `txfrcloud-web` | TXFR.Cloud | @jsdesk | **empty** | — | Stubs — planned CLI / daemon / web. **The entire TXFR.Cloud repo set is empty** — the venture exists (recently added) but none of its repos are in the GEN2 model yet. |
| **`opensoftwarelib-web`** | DiviaFoundation | **@jsmacmini** | not probed (Mac) | ? | ★ The **Divia.Foundation** repo you remembered — explains the empty `DiviaFoundation/` on @jsdesk. Likely an open-source-software-library web app. Probe + decide its home. |
| `ensemble` | DiviaAI | **@jsmacmini** | not probed (Mac) | ? | Mac-only & unmodeled — likely the multi-agent **ensemble/collab tooling** (cf. `~/Code/_ensemble/`). Identify; is `DiviaAI/` the right home? |
| `aixodev-openhands-claude` | AIXO.Dev | **@jsmacmini** | not probed (Mac) | ? | The **retired `openhands-claude` fork** (its @claude research line was merged back into `aixodev-openhands`, per `_projects/README`). Mac-only leftover — archive or delete? |

> **Cross-host notes:** (1) `DiviaHome/diviahome-web` still exists on **@jsmacmini** under the **old** name — it's the same repo as the renamed `diviahome-community`, so the Mac copy needs the same dir + remote rename we applied on @jsdesk, or it'll drift. (2) Most empty stubs and `_domain.tld` containers exist on **both** machines; only genuinely Mac-only dirs are added as `@jsmacmini` rows above.

**Empty `_`-prefixed website/domain containers** (your CMS convention — all empty, so really a checklist of *domains to verify against `DOMAIN_LIST`*):

- **DiviaAI** `_divia.ai` · **DiviaHome** `_diviahome.com` · **LegendaryMoney** `_legendarymoney.com`
- **TastyPal** `_tastycal.com` _(⚠️ unfamiliar — TastyCal?)_ · `_tastypal.com` · `_tastypantry.com` · `_tastytrucks.app`
- **TXFR.Cloud** `_txfr.app` · `_txfr.cloud` · **VelocityTerminal** `_velocityterminal.sh`
- **`_WEBSITES/`** `_ctomindmeld.com` · `_divia.foundation` · `_johnstanforth.com` · `_jsldragonfly.com` _(⚠️ unfamiliar — JSL Dragonfly?)_ · `_kingmakerstrategic.com` · `_stanforth.ai`

_(Also: `~/Code/FracReality` is a symlink → `FracRealHomes` — a brand alias of the venture folder, not a separate repo.)_

### ✅ Done — already adopted / migrated (2026-06-23)

These DB `Repository` rows now point at the real on-disk repo — `local_dir` set (absolute, for the always-Linux server) and `remote_url` corrected to the true remote. No code moved: the repos stay at `~/Code/{Venture}/{repo}`; only the DB records were reconciled (the Build-Line links already existed).

| DB repo (Build-Line) | Owner | `local_dir` (absolute) | `remote_url` (corrected) | What was done |
|---|---|---|---|---|
| **divia_ai-professional** (DesktopOutliner) | Divia.AI | `/home/jstanforth/Code/DiviaAI/divia_ai-professional` | `git@github.com:DiviaAI/divia_ai-professional.git` | ✅ Adopted as-is — real active app; DB backfilled |
| **proto-divia_ai-enterprise** (DiviaServerPrototype) | Divia.AI | `/home/jstanforth/Code/DiviaAI/proto-divia_ai-enterprise` | `git@github.com:DiviaAI/proto-divia_ai-enterprise.git` | ✅ Adopted as-is — DB backfilled |
| **kingstrat-adventuregps** (AdVentureGPS) | Kingmaker Strategic | `/home/jstanforth/Code/KingmakerStrategic/kingstrat-adventuregps` | `git@github.com:KingStratVC/kingstrat-adventuregps.git` | ✅ Adopted as-is — DB backfilled |
| **spicemaster3000** (TastySpikeDriver, personal) | TastyPal | `/home/jstanforth/Code/TastyPal/spicemaster3000` | `git@github.com:johnstanforth/spicemaster3000.git` | ✅ Adopted as-is — DB backfilled |
| **diviahome-community** (CommunityHomeHub) | DiviaHome | `/home/jstanforth/Code/DiviaHome/diviahome-community` | `git@github.com:DiviaHome/diviahome-community.git` | ✅ Renamed & adopted — GitHub repo `diviahome-web`→`diviahome-community`; `proto-divia` upstream + own origin updated; local dir + `_projects` symlink moved; DB backfilled |

> Also recorded this pass: the **Build-Line `forked-from` edges** mirroring the real git `upstream` chain — **AdVentureGPS ← DiviaServerPrototype ← CommunityHomeHub** (i.e. `kingstrat-adventuregps` ← `proto-divia_ai-enterprise` ← `diviahome-community`). First-class **repo→repo** provenance is queued as GEN2 backlog **NEXT-001** (the graph DB shouldn't have to read git `upstream` remotes to reason about clone lineage).

## 2. The clear "adopt almost as-is" set (your real question)

> ✅ **All five below have since been adopted** (2026-06-23) — see the **Done** table in §1. Retained here for the original rationale.

**Yes — there's a clean core that can move over with little/no re-implementation**, because the existing repo's name, stack, and purpose already match a *current* Build-Line:

1. **`divia_ai-professional` → DesktopOutliner** — the strongest by far: a real, active application (not a scaffold). De-freeze and point the Build-Line at it.
2. **`proto-divia_ai-enterprise` → DiviaServerPrototype** — real Flask prototype (the proto-divia⟷kingstrat chain you want to preserve).
3. **`kingstrat-adventuregps` → AdVentureGPS** — the KSVGPS repo itself; exact match, real Flask fork.
4. **`spicemaster3000` → TastySpikeDriver** — personal playground; remote's already on `johnstanforth/`, matching the Person-co-owned Build-Line.
5. **`diviahome-web` → CommunityHomeHub** (rename to `diviahome-community`) — the rename you already planned; same Flask/scope.

The next tier (`divialife-flutter`, `fracrealhomes-web`, `legendarymoney-web`, plus the `sattvasichealth`→`-community` and `tastypantry`→`-community` renames) are real repos too, but **Phase-00 scaffolds** — "adopting" them is mostly re-pointing the Build-Line to the existing scaffold + (for the LOCAL-ONLY ones) creating the GitHub remote, rather than salvaging substantial code.

## 3. On-disk repos NOT yet placed in the model (unassigned scavenge-sources)

These exist but have no DB Build-Line yet — mostly because their venture was deferred or the variant wasn't populated:

- **AIXO.Dev (deferred):** `aixodev-aixocode` (the 651-commit flagship TUI), `aixodev-web`, `aixodev-projects`, `aixodev-codemap`, `aixodev-collabs`, `aixodev-workgroups`, `aixodev-openhands`, `aixodev-professional`. *(`aixodev-projects` is the literal base GEN2 was lifted from.)*
- **DiviaAI extras:** `divia_ai-agentswarms`, the `diviacontacts-{gmail,android,iOS}` family (DiviaContacts was dropped as a sub-family), `divia_cards` (DiviaCards umbrella not modeled).
- **Future native mobile:** `divialife-android`, `divialife-iOS`, `fracrealhomes-flutter`, `fracrealhomes-android` — real dirs, but the populate only placed the current/primary repo per Build-Line.
- **Superseded/parked:** `kingstratvc-web` (replaced by `kingstrat-adventuregps`).

## 4. Summary

- **23 DB repos:** 11 exist on disk (5 strong adopt-as-is + 5 rename/scaffold-adopt + 1 far-horizon placeholder), **12 are aspirational** (to be created).
- **✅ Done (2026-06-23):** the **5 clean wins** are now **adopted** — `local_dir` + corrected remotes backfilled, and `diviahome-web` fully renamed to `diviahome-community` (see the **Done** table in §1).
- **Remaining:** 5 next-tier scaffold/rename adoptions (`divialife-flutter`, `fracrealhomes-web`, `legendarymoney-web`, `sattvasichealth`→`-community`, `tastypantry`→`-community`) + the 1 far-horizon placeholder + **12 aspirational** creates.
- **~14 on-disk repos** are unplaced scavenge-sources (AIXO.Dev cluster + DiviaContacts/DiviaCards + native-mobile variants + superseded kingstratvc-web) — they await ventures/Build-Lines that were deferred or dropped in this populate pass.
