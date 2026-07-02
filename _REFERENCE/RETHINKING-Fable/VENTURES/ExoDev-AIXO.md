# Venture Dossier — ExoDev / AIXO.Dev (Rethought)

> The developer-collaboration family: the **AIXO.Dev Platform** (software for human+AI dev teams) pulled through by **forward-deployed engineering consulting** — the Palantir Foundry/FDSE analog pair, and the **dev-graph pole** of the Four Graphs. This dossier folds in aixocode, aixodev-web, and the prototype fleet (codemap, collabs, workgroups, projects, openhands, professional).

## 1. Corporate structure (open decision, modeled as alternatives)

The corporate parent has three competing identities (E-01: ExoDev.AI Inc / ExoDev.AI Corp / ExoDev.Pro Inc, plus Platform-vs-Platforms LLC) — imported as a question-mark decision group, **owner: John** ([`../04`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §4.8). Structure regardless of name: a consulting parent (Dallas HQ; the "Palantir analog"), a product subsidiary owning the platform (the "Foundry analog"), regional services LLCs (Dallas · LA · planned Chicago/NYC/Ireland). **Lineage:** ExoDev.Pro is a *business-model evolution* of Scalara Inc (2002–present, LA) — project-builds-with-no-recurring-revenue → FDSE consulting + licensed-platform recurring revenue; Dallas incorporates first, then the LA office reboots Scalara's client base. The company is pre-seed/pre-customer; Phase-D business metrics (pricing tiers, WPAA north-star, Graduation Rate ≥60%/70% with "<50% = model in jeopardy", NRR/LTV targets, regulated-first vertical focus, services ≤15–35% ring-fence) are imported as *declared-aspirational* with DRAFT provenance.

## 2. What the family sells

1. **The AIXO.Dev Platform** — "Linear + GitHub + Slack for human-AI development teams": agents as full team members with persistent personalities (self-editing `SOUL.md`), assigned tasks, tracked contributions. `aixodev-web` is the hub (projects, issues, lossless transcripts, wiki, GitHub, analytics); `aixocode` (MIT) is the shipping laptop cockpit; the desktop edition is the E-02 question-mark.
2. **Forward-Deployed Software Engineering** — embed 3–4 days/week, ship a production workflow on real client data by day 5, *graduate* the client's engineers to solo operation by week ~8, leave. Consulting funds the platform; platform IP compounds vendor-side. The $20K 5-day Deployment Week is the pilot wedge; **graduation is a productized, receipt-bearing ritual** (P-11).

## 3. The platform's strategic core: the Ontology (dev-graph)

Make the graph the product: every project · repo · Build-Line · Stage/Phase/Sprint · discussion · session transcript as one queryable, **bitemporal** graph the team owns (hook #3), with the lossless archive as its corpus. The three-graph triumvirate (DomainGraph / ClientDomainGraph / EngagementGraph) plus Code Property Graph audits. It shares schema philosophy with KSVGPS ([`../04`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md)) and overlaps it only at `Company → Product`.

**The moat stack, in order of defensibility:** (1) the byte-for-byte session archive (can't be retro-collected — hook #1); (2) the encoded-workflow library (CollabPair templates, sprint gates, review recipes — executable institutional knowledge; engines commoditize, libraries don't); (3) the Ontology built from (1); (4) Engagement Receipts + graduation certificates (P-11); (5) the agent-cast brand layer (@maximus, @codaramus, @milton — genuinely useful for cognitive-diversity-by-design, but a *story*, not a moat).

## 4. The prototype fleet (roles, one line each)

- **aixocode** 🟢 — the shipping MC-style TUI wrapping CLI coding tools; three modes (TUI / tmux / direct PTY); CollabPairs (2 agents + human, guarded review workflow); the preservation guarantee; the open-core MIT wedge (ship the missing LICENSE file). Its collab subsystem is the laptop-scale precursor whose lessons flow to AgentSwarms.
- **aixodev-web** 🟡 — the server half; session-ingest with raw-JSONB preservation; the merge target for the fleet (the "merge target" claim is single-source from the prototypes' side — encode with `unreciprocated` provenance until corroborated).
- **aixodev-collabs** 🟠 — the next-gen cross-vendor decision engine (typed envelopes, engine-owned FSM, append-only log, secretary seat, budget breakers). Findings (tests-arbitrate; independent-answer-first; cost-is-existential 150:1) import as **dated, regime-conditional assertions** (R-08 in [`../03`](../03-IDEAS-LEDGER.md)).
- **aixodev-workgroups** 🟠 — the task "brain" (claim/lock/hand-off/dependency; Flask + FastAPI sidecar — hook #5); home of the autonomy ladder and the P-10 cost ledger; the Agent NOC's data source.
- **aixodev-codemap** 🟡 — structural + semantic + cross-project code mapping; the shared-functionality registry that (a) feeds reuse-stewardship agents, (b) replaces the convergence-diff KPI (R-09), and (c) tech-transfers its Leiden/community stack to KSVGPS dreaming (S-13).
- **aixodev-projects** 🟢 — the design-token system (DB-as-source-of-truth; DESIGN.md ⇄ DTCG round-trip); position as the portfolio's design layer; candidate standalone open tool.
- **aixodev-openhands** 🟡 — external-agent-codebase research; keeps AIXO in the *session-capture wrapper* lane (decline file-based persistence that conflicts with the guarantee); source of the cache/cost discipline; bring its model policy into line with the always-Opus rule (E-10).
- **aixodev-professional** ⚪ — the desktop placeholder inside the E-02 question-mark; the shared Rust/Tauri "desktop core" with Divia.AI Professional remains the most concrete AIXO↔Divia engineering cross-pollination — a small neutral shared library, if E-02 resolves toward Tauri.

## 5. Ideation & Exploration

**Existing (carried):** synchronized replay (collab events × terminal streams) · CollabPair templates as institutional knowledge · steer-message A/B evaluation · knowledge extraction (ADRs from archives) · AIXO MCP server · the long parser roadmap (Codex/Gemini/aider/…) · container sandboxing · crash reattachment · Rust/ratatui migration path · cross-client DomainGraph ("seen this in 17 orgs") · decision-as-PR over graph branches · Engagement Receipts · Agent NOC · the "joy of engineering" feature set (Braintrust review, craft score, learning journals) with the two-vocabulary discipline (mission language for ICs, FDSE/graduation language for enterprise buyers — E-11/J).

**Proposed (new this rethink):**
- **Team knowledge graph from session mining** and **steering-intervention analytics** ([`../03`](../03-IDEAS-LEDGER.md) §1 [P]) — the archive monetized as understanding, incl. publishable human-AI-collaboration research (credibility marketing that money can't buy).
- **Extend the preservation guarantee to autonomous runs** — every recurring/Swarm session archived like a human session; autonomous work deserves *more* audit, not less.
- **Agent Credentials (P-09), co-authored with Divia** — the rail the cross-org-negotiation moonshot actually needs; standards participation is NEAR-term cheap and MID-term decisive.
- **The workflow library as a sellable catalog** — versioned, tested, org-customizable recipes ("Security Review v3") shipped like a rulebook, with the hybrid engine ([`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §7) as the runner.
- **Cost-honesty as a product surface** — per-task, per-agent, per-engagement token economics (P-10) exposed to clients; BYOK plus visible spend builds the trust the enterprise tier needs.
- **KSVGPS as a platform showcase** — the venture graph running on the same engine family demonstrates "your domain as a queryable graph" to non-software buyers (FDSE's expansion market beyond dev teams).

**Rejected / Flawed:**
- **⛔ "N=2 is the right scale" as doctrine** — dated, cost-regime-conditional (R-08); store bitemporally, re-evaluate on curve moves.
- **⛔ AI-council review as default gate** — theater vs. tests; reserve councils for irreversible decisions ([`../02`](../02-SHARED-PRIMITIVES-AND-SYNERGY-MATRIX.md) Part IV).
- **⛔ Moats claimed on commoditizing layers** (agent harness mechanics, TUI polish, orchestration engines) — the [`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §9 compass: archives, workflows, receipts, and distribution compound; frameworks don't.
- **⛔ Resolving E-01/E-02 editorially in docs** — they are John-owned question-mark groups; model alternatives, stop re-litigating in prose.
