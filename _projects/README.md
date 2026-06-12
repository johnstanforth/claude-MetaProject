# MetaProject — Index of Managed Projects

This is the master index of every project symlinked into `_projects/`. Each entry is built from that project's own root `README.md` (or, where the README was empty/absent, from its `CLAUDE.md`, plan docs, research synthesis, and git history). The `_projects/` symlinks point at the real working copies elsewhere on disk; this MetaProject directory exists purely to coordinate work that spans more than one of them.

> **Last generated:** 2026-06-12 · **Projects indexed:** 20 (across 8 corporate/product umbrellas)
> Regenerate after adding/removing a symlink or when a project's README changes materially.

---

## Conventions

- **Umbrella** — the parent directory the symlink resolves to (the owning company / product family).
- **Stack** — primary language/framework as stated in the project's README.
- **Status** — the project's own self-reported phase/maturity, cross-checked against commit count and most-recent commit.
- **Repo** — GitHub `origin` remote where one exists; “local-only” means no remote is configured (consistent with the house rule that commits stay local until explicitly pushed).

---

## Master Index

| Project (dir) | Umbrella | What it is | Stack | Status |
|---|---|---|---|---|
| **aixodev-aixocode** | AIXO.Dev | Midnight-Commander-style TUI that wraps CLI coding assistants (Claude Code, Codex, Gemini), archives sessions losslessly, orchestrates multi-agent collaboration | Python 3.12 · Prompt Toolkit · SQLite | **Active build** — Phase 8 in progress; flagship/most-mature (651 commits) |
| **aixodev-web** | AIXO.Dev | The central AIXO.Dev Platform web app: projects, issues, AI-session transcripts, wiki, GitHub integration, notifications, analytics | Python · Flask · PostgreSQL · HTMX/Tailwind | **Active** — the upstream merge target for the prototypes (366 commits) |
| **aixodev-projects** | AIXO.Dev | Prototype: project-tracking model (hierarchy, repos, languages) destined to merge into `aixodev-web` | Python · Flask · SQLAlchemy · SQLite | Phase 01 complete; Phase 02 (theme mgmt) in progress (195 commits) |
| **aixodev-codemap** | AIXO.Dev | Prototype: source-code analysis (symbols, edges, features, clustering); functionality to migrate into `aixodev-web` | Python · Flask · SQLite | Phase 01 — Flask foundation done; extraction/analysis engines deferred (91 commits) |
| **aixodev-collabs** | AIXO.Dev | Prototype: revised multi-agent / multi-LLM **collaboration & decision** models; root of the shared workflow system | Python · Flask (planned) | Phase 00 research active; no app code yet (44 commits) |
| **aixodev-workgroups** | AIXO.Dev | Prototype: runtime **task coordination & assignment** for agent “workgroups”, plus a FastAPI status sidecar | Python · Flask + FastAPI sidecar (planned) | Phase 00 pending; scaffold only (5 commits) |
| **aixodev-openhands** | AIXO.Dev | Research project: analysis of external codebases + comparative deep research (incl. OpenHands) | Research / docs | Phase 01 open-prompt-prototype (65 commits) |
| **aixodev-openhands-claude** | AIXO.Dev | Claude-run companion to `aixodev-openhands` (same charter: external-codebase analysis & deep research) | Research / docs | Research branch; local-only (44 commits) |
| **aixodev-professional** | AIXO.Dev | Earliest-stage scaffold (workflow dirs + a staged “Twilight” Bootstrap theme); README/CLAUDE/specs still empty | TBD | Placeholder — 2 commits, no description or code yet |
| **divia_ai-professional** | DiviaAI | Local-first desktop outliner-editor for structured thinking & writing; SQLite-backed `.dvai` docs, DiviaCards | Rust · Tauri v2 · SvelteKit · TipTap | **Active dev** — real app; Phase 03 (ensemble collab) (243 commits) |
| **divia_ai-enterprise** | DiviaAI | Commercial Rust team server — a locked-down, higher-perf version of the DiviaHome server | Rust (planned) | **Intentional empty placeholder** — not started until DiviaHome v1 has 30 days of real use (no git repo) |
| **divia_cards** | DiviaCards | Flask + Svelte app rendering text inputs as typed “cards”, compiled to framework-agnostic Web Components | Python · Flask · Svelte 5 · SocketIO | Early prototype — PLAN + PLAN-v2 (4 commits, Nov 2025) |
| **diviahome-web** | DiviaHome | Open-source, self-hosted personal/household hub: documents (DDF/`.dvai`), tasks, calendar, AI-assisted Activity Log; the Divia.Network anchor app | Python · Flask · SQLite→Postgres | Phase 00 pending — **current ~60-day singular focus** (6 commits) |
| **divia-gmail** | DiviaHome | Chrome MV3 / InboxSDK extension embedding an Asana-grade task sidebar in Gmail, backed by the DiviaHome / Divia.AI Enterprise server | Browser extension (MV3) → Flask API | Research **complete**; pre-Phase 00 build (19 commits) |
| **legendarymoney-web** | LegendaryMoney | AI-assisted personal finance manager (PFM) for incomplete/messy data: confidence-aware ledger, balance assertions, NL capture | Python · Flask · SQLite→Postgres | Phase 00 pending (7 commits) |
| **sattvasichealth** | SattvasicHealth | Personal health-metrics aggregator: labs, CGM, weight/DEXA, Rx/supplements, calories/macros, trends & correlations | Python · Flask · SQLite→Postgres | Phase 00 pending (4 commits) |
| **tastypantry** | TastyPal | Kitchen pantry-inventory app: foods, food logs, receipts, shopping lists, recipes (compound foods) | Python · Flask · SQLite→Postgres | Phase 00 pending — seed prototype for the Divia.Network siblings (4 commits) |
| **spicemaster3000** | TastyPal | Spice blends, core spices & flavor pairings (Flavor Bible + 6 vendors); John's passion project | Python · Flask (planned) | Phase 00 research/ideation in progress (30 commits) |
| **kingstratvc-web** | KingmakerStrategic | Private PKMS / “company intranet” for a PE/VC firm: portfolio & idea-stage startup tracking; a trial-run of a Divia.AI Enterprise client install | Python · Flask · SQLite→Postgres | Phase 00 pending (4 commits) |

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
- **aixodev-openhands** / **aixodev-openhands-claude** — paired research repos for external-codebase analysis & comparative deep research.
- **aixodev-professional** — empty early scaffold (only a Bootstrap theme staged so far).

### DiviaAI — the commercial Divia.AI products

- **divia_ai-professional** — the real, in-development cross-platform desktop outliner (Rust/Tauri/SvelteKit). Defines the ecosystem's core vocabulary: the `.dvai` document format and DiviaCards. · `git@github.com:DiviaAI/divia_ai-professional.git`
- **divia_ai-enterprise** — the commercial team server, deliberately **not yet started** (a Rust hardening of the DiviaHome server). Held as an empty placeholder until DiviaHome reaches a battle-tested v1.

### DiviaHome — open-source personal/household edition

- **diviahome-web** — the self-hosted Flask hub and the **experimental prototype that drives the whole Divia.Network ecosystem**; the current primary focus.
- **divia-gmail** — a Gmail-embedded task sidebar that surfaces the DiviaHome / Divia.AI Enterprise server inside the inbox (research phase complete).

### DiviaCards

- **divia_cards** — typed content-block (“card”) definitions as reusable Web Components; the rendering layer the ecosystem's `DiviaCard` concept builds on.

### TastyPal

- **tastypantry** — pantry inventory; the first sibling cloned from `aixodev-collabs` and the seed the other household apps descend from. · `git@github.com:TastyPal/tastypantry.git`
- **spicemaster3000** — spice/flavor-pairing app (working title); a standalone culinary passion project with a substantial research corpus. · `git@github.com:johnstanforth/spicemaster3000.git`

### Standalone household / vertical apps

- **legendarymoney-web** (LegendaryMoney) — AI-assisted PFM built around incomplete-information.
- **sattvasichealth** (SattvasicHealth) — personal health-metrics aggregation & correlation.
- **kingstratvc-web** (KingmakerStrategic) — private PE/VC intranet; a manual trial-run of a future Divia.AI Enterprise client deployment.

---

## Cross-Project Relationships

**The Divia.Network ecosystem.** A recurring vision ties several apps together: a single natural-language capture (*“I had El Pollo Loco for dinner”*) fans out across **DiviaHome** (Activity Log), **TastyPantry** (food eaten), **Sattvasic Health** (calories/macros), and **LegendaryMoney** (an estimated dining expense) — coordinated by a Divia.AI agent over the open **Divia.Network** integration layer. These are the ecosystem's first-ever cross-app integrations, and all four share the `.dvai` format, the DiviaCards vocabulary, and the “Activity Log” pattern.

**Prototype → product convergence.** Two parallel “prototype now, merge later” patterns run through the index:
- *AIXO.Dev:* `aixodev-projects`, `aixodev-codemap`, `aixodev-collabs`, and `aixodev-workgroups` are fast Flask prototypes whose proven pieces fold back into **`aixodev-web`**.
- *Divia:* **`diviahome-web`** is the fast Python proving ground; its battle-tested ideas later harden into the Rust **`divia_ai-enterprise`** server (and inform **`divia_ai-professional`**). **`kingstratvc-web`** is a client-specific implementation that will converge toward the DiviaHome server, keeping only its firm-specific customization.

**Shared workflow lineage.** Almost every prototype was bootstrapped from a common `_workflows/` development system that originates in **`aixodev-collabs`**, cloned down the chain: `aixodev-collabs → tastypantry → sattvasichealth → diviahome-web → legendarymoney-web`, with `aixodev-workgroups` and `kingstratvc-web` branching off the same root. They all share the same sprint pipeline (New Phase → Sprint Planning → Human Review → Execution → Code Review → Closeout) and git conventions (`claudecode/@claude/phase{NN}-sprint{NN}` branches, `P{NN}-S{NN}-T{NN}` commits, local-only by default).

**Common tech defaults.** The web prototypes overwhelmingly share one stack: Python 3.12+, `uv`, Flask (app-factory + Blueprints + Jinja2), SQLAlchemy 2.0, **SQLite now → PostgreSQL later**, pytest + Ruff. The desktop/native outliers are `divia_ai-professional` (Rust/Tauri/SvelteKit), the planned `divia_ai-enterprise` (Rust), and `divia-gmail` (a browser extension).

---

## Maintenance

This file is a generated index, not a hand-maintained source of truth — each project's own `README.md` remains authoritative. To refresh: re-read every `_projects/*/README.md`, fall back to `CLAUDE.md`/plan/research/git for the empties (`aixodev-professional`, `divia_ai-enterprise`, `divia_cards`, `divia-gmail`, plus any newcomers), and regenerate the tables above.
