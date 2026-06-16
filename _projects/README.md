# MetaProject — Index of Managed Projects

This is the master index of every project symlinked into `_projects/`. Each entry is built from that project's own root `README.md` (or, where the README was empty/absent, from its `CLAUDE.md`, plan docs, research synthesis, and git history). The `_projects/` symlinks point at the real working copies elsewhere on disk; this MetaProject directory exists purely to coordinate work that spans more than one of them.

> **Last generated:** 2026-06-15 · **Projects indexed:** 29 (across 10 corporate/product umbrellas)
> Regenerate after adding/removing a symlink or when a project's README changes materially.

---

## Conventions

- **Umbrella** — the parent directory the symlink resolves to (the owning company / product family).
- **Stack** — primary language/framework as stated in the project's README.
- **Status** — the project's own self-reported phase/maturity, cross-checked against commit count and most-recent commit.
- **Repo** — GitHub `origin` remote where one exists; “local-only” means no remote is configured (consistent with the house rule that commits stay local until explicitly pushed).

---

## Master Index

| Project (dir) | Umbrella | What it is | Stack | Status | License(s) |
|---|---|---|---|---|---|
| **aixodev-aixocode** | AIXO.Dev | Midnight-Commander-style TUI that wraps CLI coding assistants (Claude Code, Codex, Gemini), archives sessions losslessly, orchestrates multi-agent collaboration | Python 3.12 · Prompt Toolkit · SQLite | **Active build** — Phase 8 in progress; flagship/most-mature (651 commits) | MIT ✅ |
| **aixodev-web** | AIXO.Dev | The central AIXO.Dev Platform web app: projects, issues, AI-session transcripts, wiki, GitHub integration, notifications, analytics | Python · Flask · PostgreSQL · HTMX/Tailwind | **Active** — the upstream merge target for the prototypes (366 commits) | Commercial/Proprietary ✅ |
| **aixodev-projects** | AIXO.Dev | Prototype: project-tracking model (hierarchy, repos, languages) destined to merge into `aixodev-web` | Python · Flask · SQLAlchemy · SQLite | Phase 01 complete; Phase 02 (theme mgmt) in progress (195 commits) | Commercial/Proprietary ✅ |
| **aixodev-codemap** | AIXO.Dev | Prototype: source-code analysis (symbols, edges, features, clustering); functionality to migrate into `aixodev-web` | Python · Flask · SQLite | Phase 01 — Flask foundation done; extraction/analysis engines deferred (91 commits) | Commercial/Proprietary ✅ |
| **aixodev-collabs** | AIXO.Dev | Prototype: revised multi-agent / multi-LLM **collaboration & decision** models; root of the shared workflow system | Python · Flask (planned) | Phase 00 research active; no app code yet (44 commits) | Commercial/Proprietary ⚠️ |
| **aixodev-workgroups** | AIXO.Dev | Prototype: runtime **task coordination & assignment** for agent “workgroups”, plus a FastAPI status sidecar | Python · Flask + FastAPI sidecar (planned) | Phase 00 pending; scaffold only (5 commits) | Commercial/Proprietary ⚠️ |
| **aixodev-openhands** | AIXO.Dev | Research repo: analysis of external codebases + comparative deep research (incl. OpenHands); the consolidated repo after the former `aixodev-openhands-claude` fork was merged back | Research / docs | Phase 01 open-prompt-prototype (65 commits) | Commercial/Proprietary ⚠️ |
| **aixodev-professional** | AIXO.Dev | **Planned** Rust/Tauri cross-platform **desktop edition** of the AIXO.Dev Platform (sub-project of `aixodev-web`): offline-first via embedded Rust logic + full sync on reconnect; desktop stack to converge with Divia.AI Professional | Rust · Tauri (planned) | Forward-looking placeholder — no code yet; long-horizon (v3/v4 era), gated behind the web platform's eventual Rust-server migration (3 commits) | Commercial/Proprietary ✅ |
| **divia_ai-professional** | DiviaAI | Local-first desktop outliner-editor for structured thinking & writing (SQLite-backed `.dvai` docs, DiviaCards); also the **desktop client for the Divia.AI Enterprise server** | Rust · Tauri v2 · SvelteKit · TipTap | **Active dev** — real app; Phase 03 (ensemble collab) (243 commits) | Commercial/Proprietary ✅ |
| **divia_ai-enterprise** | DiviaAI | Commercial Rust team/workgroups server — a locked-down, higher-perf Rust re-implementation of the DiviaHome server (Divia.AI Professional is its desktop client; DiviaMesh / Loro-CRDT sync). A specialized build later becomes the **Divia.AI Global (SaaS)** identity/auth service | Rust (planned) | **Paused placeholder** — now has a provisional origin-context README; not started until DiviaHome v1 + ~30 days real use (no git repo) | Commercial/Proprietary ✅ |
| **proto-divia_ai-enterprise** | DiviaAI | Python/Flask **prototype of the Divia.AI Enterprise server** — the proprietary commercial team server in fast-iteration Python form (functionally the exact product the eventual Rust `divia_ai-enterprise` will be; only the language differs). Downstream fork of `diviahome-web` (AGPL lab): `diviahome-main` = pristine mirror, `main` = Enterprise dev line; upstream of `kingstrat-adventuregps` | Python · Flask · SQLite→Postgres | Phase 00 pending — rebranded from a `diviahome-web` clone (2026-06-14) | Commercial/Proprietary ✅ |
| **divia_ai-swarm** | DiviaAI | Rust server providing **containerized hosting for autonomous Divia.AI agents** — the **AI backbone of the ecosystem** (OpenClaw/NanoClaw-family agent harness). Designed to run alongside Divia.AI Enterprise and transparently power AI features everywhere (e.g. the AI chat sidebar in Divia.AI Professional) | Rust · Cargo (components TBD in Phase 00) | Just bootstrapped — workflow/specs scaffold only; Phase 00 (incl. competitive deep-dive of agent frameworks) next (5 commits) | Commercial/Proprietary ⚠️ |
| **diviacontacts-gmail** | DiviaAI | **DiviaContacts** Gmail extension — a CRM-style **reader/viewer** for the Divia.AI PKMS inside Gmail: resolves email people/companies to their entities, views their PKMS pages, surfaces tasks/events, logs emails & calls (Streak is the parallel). Carried over with full history from the former `divia-gmail` task-sidebar repo | Chrome MV3 · InboxSDK | Research **complete**; pre-Phase 00 build (20 commits) | Commercial/Proprietary ✅ |
| **diviacontacts-android** | DiviaAI | **DiviaContacts** Android app — *planned* mobile reader/viewer for the Divia.AI PKMS | mobile-native (planned) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |
| **diviacontacts-iOS** | DiviaAI | **DiviaContacts** iPhone/iPad app — *planned* mobile reader/viewer for the Divia.AI PKMS | mobile-native (planned) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |
| **divia_cards** | DiviaCards | Flask + Svelte app rendering text inputs as typed “cards”, compiled to framework-agnostic Web Components | Python · Flask · Svelte 5 · SocketIO | Early prototype — PLAN + PLAN-v2 (4 commits, Nov 2025) | MIT (web-components); root undoc. ⚠️ |
| **diviahome-web** | DiviaHome | Open-source, self-hosted personal/household hub: documents (DDF/`.dvai`), tasks, calendar, AI-assisted Activity Log; the Divia.Network anchor app | Python · Flask · SQLite→Postgres | Phase 00 pending — **current ~60-day singular focus** (6 commits) | Dual: AGPLv3 & Commercial ✅ |
| **divialife-flutter** | DiviaLife | **Divia.Life** — the commercial, closed-source **cross-platform mobile app** of the Divia.AI ecosystem. Four tabs: **Agenda** (tasks/events + GPS-mapped itinerary), **Journal** (Logseq-style daily notes), **Messages** (Telegram-like rich media), **Friends & Family** (curated cross-network social feed). Local-first; syncs via DiviaMesh/Divia.Network | Flutter · Dart 3 (state mgmt & local store TBD in Phase 00) | Phase 00 pending — bootstrapped from DiviaHome; explicitly **volatile/no-sacred-cows** for ~6 months; no app code yet (3 commits) | Commercial/Proprietary ✅ |
| **divialife-android** | DiviaLife | *Planned* native **Android (Kotlin)** edition of Divia.Life, to follow once the Flutter build settles the product & data model | Kotlin (planned) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |
| **divialife-iOS** | DiviaLife | *Planned* native **iPhone/iPad (Swift)** edition of Divia.Life, to follow once the Flutter build settles the product & data model | Swift (planned) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |
| **legendarymoney-web** | LegendaryMoney | AI-assisted personal finance manager (PFM) for incomplete/messy data: confidence-aware ledger, balance assertions, NL capture | Python · Flask · SQLite→Postgres | Phase 00 pending (7 commits) | Dual: AGPLv3 & Commercial ✅ |
| **sattvasichealth** | SattvasicHealth | Personal health-metrics aggregator: labs, CGM, weight/DEXA, Rx/supplements, calories/macros, trends & correlations | Python · Flask · SQLite→Postgres | Phase 00 pending (4 commits) | Dual: AGPLv3 & Commercial ⚠️ |
| **tastypantry** | TastyPal | Kitchen pantry-inventory app: foods, food logs, receipts, shopping lists, recipes (compound foods) | Python · Flask · SQLite→Postgres | Phase 00 pending — seed prototype for the Divia.Network siblings (4 commits) | Dual: AGPLv3 & Commercial ⚠️ |
| **spicemaster3000** | TastyPal | Spice blends, core spices & flavor pairings (Flavor Bible + 6 vendors); John's passion project | Python · Flask (planned) | Phase 00 research/ideation in progress (30 commits) | Undocumented ⚠️ |
| **kingstratvc-web** | KingmakerStrategic | _**Superseded** (parked) by `kingstrat-adventuregps` 2026-06-14; kept for reference._ Private PKMS / “company intranet” for a PE/VC firm: portfolio & idea-stage startup tracking; a trial-run of a Divia.AI Enterprise client install. **Now a git fork of `diviahome-web`** (shares its history; client delta on `kingstrat-main`) | Python · Flask · SQLite→Postgres | Phase 00 pending — git fork of `diviahome-web` (+1 client commit) | Dual: AGPLv3 & Commercial ✅ (inherited) |
| **kingstrat-adventuregps** | KingmakerStrategic | **KingStrat AdVentureGPS** — portfolio-tracking / venture-studio operating system for Kingmaker Strategic Venture Partners LLC (Studio Operations + LP Dashboard; VTL/GPS + air-traffic-control framing). Replaces `kingstratvc-web`; downstream client of `proto-divia_ai-enterprise` (`main` = pristine Enterprise-prototype mirror; `kingstrat-main` = client delta). App domain `KSVGPS.kingstrat.ventures` | Python · Flask · SQLite→Postgres | Phase 00 pending — rebranded from a `kingstratvc-web` clone (2026-06-14); renamed VentureGPS → AdVentureGPS (2026-06-15) | Commercial/Proprietary ✅ |
| **fracrealhomes-web** | FracRealHomes | **FracRealHomes (Web)** — Pacaso-style fractional-ownership residential real-estate venture: create, co-purchase, and long-term-manage shared homes. Core tech is a "next-gen Zillow estimate" — extends Zillow/Redfin valuation with investor-grade data points, most distinctively an Unreal-Engine 3D model of each parcel's max-permitted volumetric build (setbacks/height/jurisdiction rules, e.g. LA County's below-grade-basement exemption) to price in view-blocking risk. Blends Zillow/Redfin (discovery) + Pacaso (fractional co-purchase) + Airbnb (ops) + Asana (multi-owner maintenance/cost/tax mgmt). Standalone startup but a Divia.Network participant; leans on `legendarymoney-web` for financial services | Python 3.12 · Flask · SQLite→Postgres (planned) | Empty placeholder — symlinked 2026-06-15; bootstrap + Phase 00 pending | Commercial/Proprietary ⚠️ |
| **fracrealhomes-flutter** | FracRealHomes | **FracRealHomes (Flutter)** — *planned* cross-platform Flutter/Dart mobile app mirroring the web app's functionality | Flutter · Dart (planned) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |
| **fracrealhomes-android** | FracRealHomes | **FracRealHomes (Android)** — *planned* spike/PoC native Kotlin app researching Zillow-style 3D virtual-home walkthrough scanning (in-home photo capture → assembled 3D walkthrough); feeds the Unreal-Engine neighborhood-model idea (interior 3D + neighbor max-build wireframes + Google Earth imagery) | Kotlin (planned, spike/PoC) | Empty placeholder — new dir, no code yet | Commercial/Proprietary ⚠️ |

> **License(s) column** — **✅** = stated in the repo (a `LICENSE`/`LICENSE.md` file, or an explicit declaration in `pyproject.toml`/README); **⚠️** = **inferred, pending John's confirmation** (the repo is silent or pre-code). Two buckets per request — **Commercial/Proprietary** vs **Dual: AGPLv3 & Commercial** — plus the real-world outliers **MIT** and **Undocumented**.
>
> **Inference notes for the ⚠️ rows (please confirm/correct):**
> - The AIXO.Dev prototypes (`collabs`, `workgroups`, `openhands`) and `divia_ai-swarm` are assumed **Commercial/Proprietary** by family default (their stated-license AIXO/Divia siblings are proprietary).
> - The empty mobile placeholders (`diviacontacts-android/iOS`, `divialife-android/iOS`) inherit their family's commercial license.
> - `tastypantry` and `sattvasichealth` are assumed **Dual AGPLv3 & Commercial** because `divia_ai-enterprise`'s README explicitly lists them among the four AGPL "lab" apps (with DiviaHome + LegendaryMoney) — even though their own repos are silent.
> - `spicemaster3000` is genuinely **Undocumented** (standalone, no stated license, commercial framing).
> - `aixocode` declares **MIT** in `pyproject.toml` but has *no `LICENSE` file*; `divia_cards` ships its Web-Components sub-package as MIT but has no root license; `kingstratvc-web` carries DiviaHome's dual license *inherited, not yet client-tailored*.
>
> Full license-coverage discussion in [`../_REFERENCE/ERRATA.md`](../_REFERENCE/ERRATA.md). This index, `STATUS.md`, the per-product/venture docs, and the cross-project discrepancy log now live under [`../_REFERENCE/`](../_REFERENCE/README.md).

---

## By Umbrella

### AIXO.Dev — the developer-collaboration platform

The umbrella John's CLAUDE.md describes in depth. **`aixodev-web`** is the central platform; several smaller Flask prototypes each prove out one slice in a fast, throwaway-friendly form and then converge back into `aixodev-web`. **`aixodev-aixocode`** is the laptop-side TUI that captures CLI-tool sessions and feeds the platform.

- **aixodev-aixocode** — flagship TUI session manager & multi-agent collaboration host. Most mature project in the whole index. · `git@github.com:aixodev/aixodev-aixocode.git`
- **aixodev-web** — the platform web app (issues, transcripts, wiki, analytics, GitHub). Merge target for the prototypes below. · `git@github.com:aixodev/aixodev-web.git`
- **aixodev-projects** — project-structuring prototype → `aixodev-web`. · `git@github.com:aixodev/aixodev-projects.git`
- **aixodev-codemap** — code-analysis prototype → `aixodev-web`. · `git@github.com:aixodev/aixodev-codemap.git`
- **aixodev-collabs** — multi-agent collaboration/decision-model prototype; also the source of the shared `_workflows/` system every sibling is bootstrapped from. · `git@github.com:aixodev/aixodev-collabs.git`
- **aixodev-workgroups** — task-coordination prototype with a FastAPI status sidecar. · `git@github.com:aixodev/aixodev-workgroups.git`
- **aixodev-openhands** — research repo for external-codebase analysis & comparative deep research; now the consolidated repo (the retired `aixodev-openhands-claude` fork's @claude research line was merged back and labeled as branch `openhands/research/@claude/code_analysis-phaseD1`).
- **aixodev-professional** — **AIXO.Dev Professional**, the *planned* Rust/Tauri cross-platform **desktop edition** of the platform and a **sub-project of `aixodev-web`**. Offline-first (embedded Rust server logic runs locally — the "coding on a train" use-case, no Internet/SaaS needed) with full bidirectional sync to the AIXO.Dev servers on reconnect. Its desktop tech stack is intended to **converge with Divia.AI Professional** (a separate corporate/product family) at the shell/runtime/storage/sync layers, sharing lived-experience lessons across both products. **Long-horizon (v3/v4 era)**, gated behind the web platform's eventual Rust-server migration (itself gated behind the not-yet-existent Divia.AI Enterprise architecture). Today a forward-looking placeholder — workflow scaffold + staged "Twilight" Bootstrap theme, no application code yet.

### DiviaAI — the commercial Divia.AI products

- **divia_ai-professional** — the real, in-development cross-platform desktop outliner (Rust/Tauri/SvelteKit). Defines the ecosystem's core vocabulary (the `.dvai` document format and DiviaCards) and doubles as the **desktop client for the Divia.AI Enterprise server**. · `git@github.com:DiviaAI/divia_ai-professional.git`
- **divia_ai-enterprise** — the commercial team server, deliberately **not yet started** (a Rust hardening of the DiviaHome server; Divia.AI Professional is its desktop client; DiviaMesh / Loro-CRDT sync). Held as a placeholder until DiviaHome reaches a battle-tested v1 (+ ~30 days of real use). **Strategic endgame:** a specialized, hardened build is later repurposed as the **Divia.AI Global (SaaS) Service** — the central global-identity/auth authority behind the "one global username, federated home + work servers" model the household-app READMEs reference. Now carries a **provisional origin-context README** (relocated 2026-06-12 from DiviaHome; not yet a git repo).
- **proto-divia_ai-enterprise** — the **Python/Flask prototype of the Divia.AI Enterprise server** (the proprietary commercial team server in fast-iteration Python form; functionally the exact product the eventual Rust `divia_ai-enterprise` will be, only the language differing). A downstream fork of `diviahome-web` (the AGPL lab) — `diviahome-main` mirrors the lab, `main` carries the Enterprise delta — and itself the upstream of `kingstrat-adventuregps`. Rebranded from a `diviahome-web` clone 2026-06-14. · `git@github.com:DiviaAI/proto-divia_ai-enterprise.git`
- **divia_ai-swarm** — **Divia.AI Swarm**, a Rust server providing **containerized hosting for autonomous Divia.AI agents** — the planned **AI backbone of the ecosystem**. Same family as autonomous-agent harnesses like OpenClaw/IronClaw/PicoClaw/NanoClaw/Hermes Agent and usable standalone like them, but its designed-for role is deployment **alongside Divia.AI Enterprise**: hosted agents keep real-time connections (WebSocket, ZeroMQ) to the other Divia.AI products and transparently power their AI features — e.g. the AI chat in Divia.AI Professional's right sidebar. Just bootstrapped (workflow/specs scaffold from DiviaHome); Phase 00 next, including a competitive deep-dive of existing agent frameworks and the core Rust component decisions (async runtime, RPC framework, container runtime, database). · `git@github.com:DiviaAI/divia_ai-swarm.git`
- **DiviaContacts** — a sub-family of lightweight, **CRM-style reader/viewer** clients for the Divia.AI PKMS. The desktop/server flagships (Divia.AI Professional / Enterprise) remain the *full* PKMS; these are scoped-down, immediate-access viewers — **Streak** is the closest market parallel:
  - **diviacontacts-gmail** — the Gmail extension (Chrome MV3 · InboxSDK): resolves email senders to People/Companies in the PKMS, views their pages, surfaces tasks/events, and logs emails & calls. Carried over with full git history from the former `divia-gmail` task-sidebar project (renamed/repositioned 2026-06-12); research complete, pre-Phase 00. · `git@github.com:DiviaAI/diviacontacts-gmail.git`
  - **diviacontacts-android** — *planned* Android client (new empty placeholder).
  - **diviacontacts-iOS** — *planned* iPhone/iPad client (new empty placeholder).

### DiviaHome — open-source personal/household edition

- **diviahome-web** — the self-hosted Flask hub and the **experimental prototype that drives the whole Divia.Network ecosystem**; the current primary focus.

### DiviaLife — the mobile member of the Divia.AI family

**Divia.Life** is the commercial, closed-source phone-and-tablet app of the Divia.AI ecosystem — "your personal life, organized": Agenda (tasks/events + GPS itinerary), Journal (daily notes), Messages (rich media), and a Friends & Family feed aggregating external social networks. A **deeply integrated, local-first client**: on-device store is source of truth, sharing `.dvai`/DiviaCards shapes and syncing over DiviaMesh/Divia.Network with DiviaHome and the commercial Divia.AI servers.

- **divialife-flutter** — the **Flutter (Dart) first build** and the repo where the product gets figured out; explicitly early-stage/volatile ("no sacred cows") for ~6 months from June 2026. Phase 00 (data model, state mgmt, local store) is the next step. · `git@github.com:DiviaLife/divialife-flutter.git`
- **divialife-android** — *planned* native **Kotlin** edition (new empty placeholder).
- **divialife-iOS** — *planned* native **Swift** edition (new empty placeholder).

### DiviaCards

- **divia_cards** — typed content-block (“card”) definitions as reusable Web Components; the rendering layer the ecosystem's `DiviaCard` concept builds on.

### TastyPal

- **tastypantry** — pantry inventory; the first sibling cloned from `aixodev-collabs` and the seed the other household apps descend from. · `git@github.com:TastyPal/tastypantry.git`
- **spicemaster3000** — spice/flavor-pairing app (working title); a standalone culinary passion project with a substantial research corpus. · `git@github.com:johnstanforth/spicemaster3000.git`

### Standalone household / vertical apps

- **legendarymoney-web** (LegendaryMoney) — AI-assisted PFM built around incomplete-information.
- **sattvasichealth** (SattvasicHealth) — personal health-metrics aggregation & correlation.
- **kingstrat-adventuregps** (KingmakerStrategic) — **KingStrat AdVentureGPS**: the portfolio-tracking / venture-studio operating system for Kingmaker Strategic Venture Partners LLC (Studio Operations + LP Dashboard; VTL/GPS + air-traffic-control framing; app domain `KSVGPS.kingstrat.ventures`). A downstream client of `proto-divia_ai-enterprise` (the Enterprise-server prototype): `main` = pristine mirror of the prototype, `kingstrat-main` = the AdVentureGPS client delta. Rebranded from a `kingstratvc-web` clone 2026-06-14; renamed VentureGPS → AdVentureGPS 2026-06-15. · `git@github.com:KingStratVC/kingstrat-adventuregps.git`
- **kingstratvc-web** (KingmakerStrategic) — _**superseded** (parked) by `kingstrat-adventuregps` on 2026-06-14; kept for reference._ Was a private PE/VC intranet trial-run forked from `diviahome-web`.

### FracRealHomes — fractional-ownership residential real estate

**FracRealHomes** (corporate entity *Fractional Reality Homes LLC*; branded *frac|real|homes*) is a Pacaso-style venture that streamlines the creation, co-purchase, and long-term management of fractional-ownership residential properties. Its core technology is John's long-running "next-gen Zillow estimate" idea: model every parcel the way Zillow/Redfin do (property + macroeconomic data points) but extend it with the data points real-estate *investors* care about — most distinctively, an Unreal-Engine 3D model of each parcel's **maximum-permitted volumetric build** under that jurisdiction's exact rules (setbacks, height, and e.g. LA County's below-grade-basement exemption), so the model can price in *view-blocking risk* — a tear-down-and-rebuild next door erasing the "forever views" a buyer paid a premium for (cf. the 2022 Bruce's Beach reversion in Manhattan Beach). The product blends Zillow/Redfin discovery, Pacaso-style fractional co-purchase, Airbnb-like operations, and Asana-like project management for multi-owner maintenance, operating-cost, and tax coordination. It is a standalone startup (its own equity investors) but a certified **Divia.Network** participant, so its heavier financial-services needs (purchase, long-term operating costs, tax) lean on `legendarymoney-web` over the Divia protocol rather than being reimplemented from scratch.

- **fracrealhomes-web** — the Python/Flask web application (Zillow/Redfin × Pacaso × Airbnb × Asana, for fractional homes). Empty placeholder symlinked 2026-06-15; bootstrap + Phase 00 pending.
- **fracrealhomes-flutter** — *planned* cross-platform Flutter/Dart mobile app mirroring the web app's functionality. Empty placeholder.
- **fracrealhomes-android** — *planned* spike/PoC native Kotlin app researching Zillow-style **3D virtual-home walkthrough scanning** (in-home photo capture → assembled 3D walkthrough), feeding the Unreal-Engine neighborhood model (high-detail interior 3D + neighbor max-build wireframes + Google Earth imagery, "fading out" from 4K interior detail to street-level views blocks away). Empty placeholder.

---

## Cross-Project Relationships

**The Divia.Network ecosystem.** A recurring vision ties several apps together: a single natural-language capture (*“I had El Pollo Loco for dinner”*) fans out across **DiviaHome** (Activity Log), **TastyPantry** (food eaten), **Sattvasic Health** (calories/macros), and **LegendaryMoney** (an estimated dining expense) — coordinated by a Divia.AI agent over the open **Divia.Network** integration layer. These are the ecosystem's first-ever cross-app integrations, and all four share the `.dvai` format, the DiviaCards vocabulary, and the “Activity Log” pattern. **Divia.Life** (`divialife-flutter`) joins this circle as the **mobile capture surface** — a deeply integrated, local-first client whose own first ecosystem integrations (Divia.Life ↔ DiviaHome ↔ the commercial servers, via DiviaMesh/Divia.Network) are expected to teach the ecosystem what works.

**The Divia.AI agent backbone.** `divia_ai-swarm` is the planned Rust server hosting autonomous Divia.AI agents in isolated containers (OpenClaw/NanoClaw-family harness, usable standalone). Its designed-for deployment is **Swarm + Enterprise running together**: hosted agents hold real-time connections to the other Divia.AI products and transparently power their AI capabilities — `divia_ai-enterprise`'s document/task/project features and the AI chat sidebar in `divia_ai-professional`.

**Prototype → product convergence.** Two parallel “prototype now, merge later” patterns run through the index:
- *AIXO.Dev:* `aixodev-projects`, `aixodev-codemap`, `aixodev-collabs`, and `aixodev-workgroups` are fast Flask prototypes whose proven pieces fold back into **`aixodev-web`**.
- *Divia:* **`diviahome-web`** is the fast Python proving ground; its battle-tested ideas later harden into the Rust **`divia_ai-enterprise`** server (and inform **`divia_ai-professional`**). **`kingstratvc-web`** is a client-specific implementation — now literally a **git fork of `diviahome-web`** (shared history) — that pulls product updates from `upstream` onto a pristine `main` mirror and keeps its firm-specific customization as a visible delta on `kingstrat-main`; convergence = that delta shrinking as general features graduate up into DiviaHome.

**Reader/viewer clients vs. full PKMS.** The **DiviaContacts** family (`diviacontacts-gmail` + the planned `diviacontacts-android` / `diviacontacts-iOS`) are deliberately *not* full apps: they are thin, CRM-style **reader/viewers** that surface and log activity against the Divia.AI PKMS, while the heavy lifting stays in the full PKMS flagships (`divia_ai-professional` desktop + the planned `divia_ai-enterprise` server). `diviahome-web` is the interim dev/test server they target while the commercial servers are built. The closest market analogue is Streak/Copper-style CRM-in-Gmail. (**Divia.Life** is the contrast case on mobile: a full first-class app, not a reader/viewer — note the two families' parallel structure, each with a lead implementation plus planned native android/iOS placeholder repos.)

**Shared workflow lineage.** Almost every prototype was bootstrapped from a common `_workflows/` development system that originates in **`aixodev-collabs`**, cloned down the chain: `aixodev-collabs → tastypantry → sattvasichealth → diviahome-web → legendarymoney-web`, with `aixodev-workgroups` branching off the same root (`kingstratvc-web` has since been re-created as a git fork of `diviahome-web`, inheriting the same workflow system through it). The two newest repos extend the chain from DiviaHome: `diviahome-web → divia_ai-swarm` (adapted for Rust/cargo) and `diviahome-web → divialife-flutter` (adapted for Flutter/Dart, via `workflow_bootstrap_project.md`). They all share the same sprint pipeline (New Phase → Sprint Planning → Human Review → Execution → Code Review → Closeout) and git conventions (`claudecode/@claude/phase{NN}-sprint{NN}` branches, `P{NN}-S{NN}-T{NN}` commits, local-only by default).

**Common tech defaults.** The web prototypes overwhelmingly share one stack: Python 3.12+, `uv`, Flask (app-factory + Blueprints + Jinja2), SQLAlchemy 2.0, **SQLite now → PostgreSQL later**, pytest + Ruff. The desktop/native outliers are `divia_ai-professional` (Rust/Tauri/SvelteKit), the planned `divia_ai-enterprise` (Rust), the planned `aixodev-professional` (Rust/Tauri desktop edition of the AIXO.Dev Platform), `divia_ai-swarm` (Rust agent-hosting server), `divialife-flutter` (Flutter/Dart mobile), and `diviacontacts-gmail` (a browser extension).

**Cross-family shared desktop stack.** Although AIXO.Dev and Divia.AI/DiviaHome are entirely separate corporate/product families, two of their desktop apps are meant to share a **near-identical Rust/Tauri foundation**: **`divia_ai-professional`** (shipping today) and the planned **`aixodev-professional`**. The intent is that hard-won lessons and optimizations from each product's desktop work flow into the other, while their application/domain layers stay distinct (an outliner-editor vs. an AIXO.Dev Platform client).

---

## Maintenance

This file is a generated index, not a hand-maintained source of truth — each project's own `README.md` remains authoritative. To refresh: re-read every `_projects/*/README.md`, fall back to `CLAUDE.md`/plan/research/git for the README-less ones (`diviacontacts-android`, `diviacontacts-iOS`, `divialife-android`, `divialife-iOS`, `divia_cards`, `fracrealhomes-web`, `fracrealhomes-flutter`, `fracrealhomes-android`), plus any newcomers, and regenerate the tables above. (Note: `divia_ai-enterprise` and `aixodev-professional` now carry provisional/forward-looking READMEs.)
