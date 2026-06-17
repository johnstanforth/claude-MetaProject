# Product — aixocode

> The flagship, most-mature product in the entire portfolio: a Midnight-Commander-style terminal/TUI
> that **wraps CLI coding assistants**, captures their sessions losslessly, manages many at once, and
> orchestrates multi-agent collaboration — the laptop-side bridge to the AIXO.Dev Platform.

- **Names:** `aixocode` (always lowercase) · repo/dir `aixodev-aixocode` · also ships a second binary `aixotest`.
- **Umbrella / venture:** AIXO.Dev — see [`../../VENTURES/ExoDev.md`](../../VENTURES/ExoDev.md).
- **License:** **MIT** (declared in `pyproject.toml`; *no top-level LICENSE file exists* — a gap). Notably the *only* MIT product among proprietary AIXO.Dev siblings — see [`../../ERRATA.md`](../../ERRATA.md).
- **Status:** 🟢 Most product-complete app in the portfolio. Phases 0–7 complete; Phase 8 in progress; ~45 sprints, ~651 commits, ~1,700 tests. Stack: Python 3.12+, Prompt Toolkit, SQLite (WAL), TOML, `uv`.

---

## What it is (consensus)

`aixocode` sits between the CLI coding tools developers use daily and the centralized AIXO.Dev Platform:

```
CLI Coding Tools  ←→  aixocode (local)  →  AIXO.Dev Platform (server)
```

Three jobs: **(1)** manage multiple LLM-tool instances in organized workspaces; **(2)** preserve their session logs **losslessly** (the highest-priority architectural constraint); **(3)** act as the local runtime that can power platform-defined agent personalities. Three operating modes: the default **TUI**, `--tmux-session` (libtmux; one tool per window), and `--direct` (transparent PTY passthrough).

### What works today
- The full **MC-style TUI**: four-zone layout, workspace/terminal sidebar tree, tab bar scoped to the workspace, F-key bar, 5 themes, fuzzy command palette (F4), adaptive layout, notifications, workspace snapshots, help/details overlays.
- **Lossless Claude Code archival**: JSONL parsed and stored to a per-tool SQLite archive (`claude_code_sessions.db`) preserving `raw_data` byte-for-byte; 22 hook event types via a CLI receiver; offline scan/import.
- The **CLI suite**: `scan`, `import`, `archive`, `stats`, `sync`, `hook-event`, `config`.
- **Native multi-agent collaboration** (the Phase 4/6/7 crown jewel): **CollabPairs** (2 agents + a human in a shared CHAT), structured message routing, a co-manager control socket (16 commands), a guarded 3-phase `code_review_v1` workflow, transcript history/search/export, durable workflow-summary artifacts. (Built to fully replace the third-party `ensemble` engine — achieved in Phase 6.)
- A **resilient offline-first sync queue** (exponential backoff + circuit breaker) and **local analytics** (`aixocode stats`, time-varying rate-card pricing).
- **`aixotest`**: an in-tree TUI visual-testing tool with `.golden`/`.xocap` capture formats and an `/aixotest` Claude command.

### Owned vocabulary (the entity model)
**LLM Tool** (a CLI assistant) · **CodingEngine** (an LLM Tool + working dir + context files) · **Workspace** (= Folder; sidebar org unit) · **CollabPair** (ephemeral 2-agent + human session; the data model supports N → a future "CollabGroup") · **LLM Tool Session** (the lossless archival record) · **AgentEngine mode** (a worker-agent runtime that long-polls the Platform's task queue — *documented but not yet built*).

### The Preservation Guarantee (load-bearing)
`*_sessions.db` files must **never** be deleted, truncated, or schema-changed without John's explicit manual approval + a manual backup — even for additive changes, even under `--dangerously-skip-permissions`. `raw_data` preserves original JSONL byte-for-byte; scan/import work fully offline; default retention is `keep_forever`. (`queue.db` and `collaboration.db` are operational and safe to clean.)

## Cross-product role
- The laptop-side **client of `aixodev-web`** (the central platform). Contract is aligned both sides; **live E2E sync is the biggest unbuilt gap** (server integration is Sprint 05, not yet live).
- Demarcation: the Platform owns orgs/projects/agents/tasks/personalities; aixocode owns workspaces, terminals, CollabPairs, and the session archives. Agent personalities defined on the Platform are *executed* locally by aixocode's AgentEngine mode.
- aixocode's local collab subsystem is the **laptop-scale precursor of Divia.AI AgentSwarms** at server scale; lessons are meant to flow aixocode → Swarm.

## Ideation & Exploration (capture everything, commit to nothing)

**From the backlog/research (`_horizon_*`, PROLOGUE, ADRs):**
- **Synchronized replay** — join collaboration events with each terminal's output stream to replay "what the team said + what each terminal was doing + when messages were delivered/deferred" (flagged a major product advantage).
- **CollabPair templates as institutional knowledge**; **A/B eval framework for steer messages** (measure social-dynamic impact of interventions); **multi-LLM AI-council review**; **knowledge extraction** (derive ADRs from archives); **skills discovery** (catalog Claude Code Skill usage across sessions); an **AIXO MCP server** exposing session data/analytics as MCP tools.
- A long parser roadmap: Codex, Gemini, aider, Cline, Roo Code, Goose, OpenCode, LLM CLI, plus IDE-conversation parsers (Cursor SQLite, VS Code Copilot chat) and billing connectors (Cursor CSV/API, Copilot OTel).
- **Container sandboxing** (Bubblewrap/Docker); **crash reattachment** to dead PTYs (aspirational); **Rust/ratatui migration** of the core (the reason Prompt Toolkit was chosen — it maps cleanly to ratatui).
- Cross-mode collaboration (tmux/direct/server-relay delivery adapters); first-class shared artifacts; per-agent worktree isolation; future composer commands (`/phase`, `/checkpoint`, `/nudge @agent`).

**✦ New this session:**
- ✦ **The "remote agent" pane** — show your Swarm-hosted fleet beside your local terminals, making aixocode the single cockpit for local + server agents (LATER-002's dogfooding chain made concrete).
- ✦ **aixocode as the recurring-stewardship agent's body** — the LATER-002 meta-maintenance agent (repo-hygiene heartbeats, backlog grooming, doc-drift sweeps across all repos) runs *as* an aixocode AgentEngine instance whose working context is the MetaProject; the autonomy-ladder grades per task.
- ✦ **Extend the Preservation Guarantee to autonomous runs** — every Swarm/recurring agent session captured byte-for-byte like a human session (autonomous work deserves *more* audit trail, not less).
- ✦ **Ship the missing `LICENSE` file** — aixocode declares MIT but has no license file; the MIT-amid-proprietary-siblings choice is a deliberate open-core wedge worth making explicit and intentional (see [`../../VENTURES/ExoDev.md`](../../VENTURES/ExoDev.md) ideation).
- ✦ **"CollabGroup" when N>2 finally ships** — the data model already supports it; the first 3-agent session (proposer + two diverse-lens critics, the adversarial-verify pattern) is a natural Phase-8+ demo.
