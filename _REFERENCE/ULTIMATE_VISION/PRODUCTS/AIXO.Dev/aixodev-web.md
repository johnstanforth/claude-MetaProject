# Product — AIXO.Dev Platform (Web)

> The central platform and strategic hub of the AIXO.Dev family: "**Linear + GitHub + Slack for
> human-AI development teams**" — where AI agents are full team members with persistent personalities,
> assigned tasks, and tracked contributions. The merge target the laptop tools and prototypes feed.

- **Names:** customer-facing "**AIXO.Dev Platform**"; internal "AIXO.Dev Platform (Web)" · repo/dir `aixodev-web` · package `aixodev-web` v0.3.0.
- **Umbrella / venture:** AIXO.Dev — see [`../../VENTURES/ExoDev.md`](../../VENTURES/ExoDev.md).
- **License:** **Proprietary** (`LicenseRef-Proprietary`; "© AIXO.Dev Platform LLC, An ExoDev.AI Company. All Rights Reserved").
- **Status:** 🟡 Real working Flask/PostgreSQL app. Phases 1–4 complete; Phase 5 (entity model & platform vision) active; ~695 tests, 25-table schema, 19 API blueprints. *Most recent activity is product/venture strategy research (the Apr-2026 Phase-D suite), not app code.*

---

## What it is (consensus)

An API-first (`/api/v1/*`) web platform for human + AI software teams. **What works today:**
- **Project management** (hierarchical projects; 5 roles) and **issue tracking** (types/statuses/labels/milestones/relations/templates/comments/activity, real-time via SocketIO).
- **AI session transcripts** — ingests Claude Code JSONL + Claude.ai exports, preserves raw JSONB losslessly, renders a session viewer (syntax highlighting, thinking-trace toggles, subagent hierarchy, annotations).
- **Per-project wiki** (hierarchy, versioning/revert, `[[wiki links]]`), **GitHub integration** (OAuth, repo/branch/commit/PR browser, `fixes #N` auto-linking, webhooks), **real-time notifications**, **analytics dashboards** (Chart.js), an **admin panel**, **ZIP export/import** with SHA-256 manifests, background workers (Dramatiq/Redis), and the **session-ingest API** (`POST /api/v1/sessions/ingest`).
- Stack: Python 3.11, Flask 3.1, SQLAlchemy 2.0, PostgreSQL 16, SocketIO/eventlet/Redis, Jinja2/HTMX/Tailwind, JWT + GitHub OAuth, Playwright e2e. Extensive docs (13-ch user guide, 11-ch admin guide, 14-ch engineering guide).

### Two collaboration paradigms, deliberately contrasted
- **aixocode's synchronous CollabPair** (2 agents + human, fresh/temporary) — the laptop pattern.
- **The Platform's asynchronous "dozens-of-agents, Asana-model" coordination** (persistent agents, task queues) — the server pattern. The Platform owns the persistent agent personalities (each with a self-editable `SOUL.md`, each backed by a specific model engine); aixocode's AgentEngine mode executes them locally.

## Cross-product role
- **The server half of the aixocode↔web client/server split**, and the intended **merge target** for the Flask prototypes (`aixodev-projects`, `aixodev-codemap`, `aixodev-collabs`, `aixodev-workgroups`). *Caveat: the "merge target" framing is asserted in the index and the prototypes' docs but is **not corroborated inside `aixodev-web`'s own docs** — see [`../../ERRATA.md` E-09/E-02`](../../ERRATA.md).*
- Its `_workflows/` system is the **upstream template that seeded the Divia family** (the bootstrap workflow uses "Divia AI Desktop Pro" as its worked example).
- Planned desktop edition — **contested**: `aixodev-web`'s docs call it "AIXO.Dev Desktop" (`aixodev-desktop`, Electron-first); `aixodev-professional`'s own README calls itself the Rust/Tauri "AIXO.Dev Professional." See [`aixodev-professional.md`](aixodev-professional.md) and [`../../ERRATA.md` E-02`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)

**From the backlog + the Phase-D research:**
- **The "Ontology" knowledge graph** as the platform's strategic core — a three-graph triumvirate (DomainGraph + ClientDomainGraph + EngagementGraph), Palantir-Foundry-modeled, expanding the schema ~25→75 tables (graph-DB choice deferred: Neo4j / Apache AGE / SurrealDB). Bitemporal time-travel; Code Property Graph security audits (Joern).
- **AIXO MCP server** (Schema MCP + Data MCP endpoints); **knowledge extraction** → auto-wiki/ADRs from transcripts; PostgreSQL full-text session search; AI session analysis (Haiku summaries → deeper dives → quality scoring); cross-tool import adapters; a browser extension for bug reporting; multi-LLM "ai-council" cross-review; session-type security presets (the "lethal trifecta"); container sandboxing.
- **30-feature "shock and awe" catalog** — persistent named agents (the "10/10"); cross-vendor lossless ingestion; **Engagement Receipts** (ed25519-signed delivery proofs); multi-week autonomous project ownership; autonomous multi-repo refactoring; "Ask-the-DomainGraph-anything."
- **The "Joy of Engineering" features** — Braintrust PR review (all agents critique), a Craft Score, agent onboarding "first impressions," learning journals, team session replays, personality workshops, an "Ensemble Jam" guest-agent disruption, a watercooler channel.

**✦ New this session:**
- ✦ **Make the Ontology the product, not a feature** — "your team's entire software-development reality as one queryable graph you own" is the platform's sharpest story and the natural home for the recurring-stewardship agents (LATER-002 §4 inventory: doc-drift, backlog grooming, dependency sweeps all become graph-aware agent tasks reporting into the web UI).
- ✦ **Reconcile the desktop edition decision in one doc** (name + stack), then point both repos at it — this is the single most concrete cross-repo contradiction in the AIXO.Dev family.
- ✦ **The Agent NOC** (LATER-002) lives here — an `aixodev-web` dashboard of every recurring autonomous task across the org: last run, findings, pending approvals, cost, autonomy level. The "ops center" for the agent fleet, and the consumer twin of Divia.Life's gentler "your agents this week" card.
- ✦ **Resolve the "joy of engineering" vocabulary split deliberately** — keep the mission language for IC/community channels, the FDSE/graduation language for enterprise buyers, and document *which audience gets which* so the two don't bleed (per the Phase-D positioning correction).
