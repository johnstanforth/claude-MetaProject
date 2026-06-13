# LATER-002 — Recurring Autonomous-Agent Tasks: Where Do They Live Long-Term?

- **Captured:** 2026-06-12, MetaProject session (immediately following [LATER-001](LATER-001-workflow-lineage-and-hybrid-formalization.md))
- **Status:** LATER — scratchpad for weekly backlog review; feeds `divia_ai-swarm` Phase 00 research scope
- **Eventual owning project:** `divia_ai-swarm` (primary — the "where do agents run" question), with hard dependencies on `aixodev-workgroups` (task definition/assignment, see LATER-001) and `aixodev-web` (surfacing/approvals)
- **Related:** LATER-001 · `divia_ai-swarm/CLAUDE.md` + `README.md` · `divia_ai-swarm/_specs_and_plans/_backlog/_horizon_NEXT.md` (competitive deep-dive item) · `aixodev-aixocode` Phase 8 (Analytics & Knowledge)

> **Nature of this file (per John):** a deliberately wide-scope scratchpad. Record *all* ideas we have right now — both to preserve what we were thinking for the future discussion, and to widen the considered space of use-cases, improvement opportunities, and alternate implementations. Nothing here is committed-to; everything here is fair game to discard.

---

## 1. The triggering question

While setting up `_backlog_TODOs/` and its **weekly review routine**, the immediate implementation offer was a Claude Code `/schedule` cloud routine. That works today — but it raises the real question: **where should ongoing "autonomous agent"-level tasks belong long-term within our ecosystem?** Vendor-hosted scheduling (Claude Code cloud routines), local cron, the AIXO.Dev Platform, or our own agent-hosting infrastructure?

This is properly a **Phase 00 research question for `divia_ai-swarm`**, and should be added to its ideation scope alongside the already-queued competitive deep-dive.

## 2. Context from `divia_ai-swarm` (pulled from its repo docs, 2026-06-12)

- **Divia.AI Swarm** is a Rust server providing **containerized hosting for multiple autonomous Divia.AI agents** — same family as OpenClaw, IronClaw, PicoClaw, NanoClaw, Hermes Agent, and the broader field of agent frameworks/harnesses. Stood up alone, it works like those tools out of the box; its purpose-built role is the **AI backbone of the Divia.AI ecosystem**.
- Hosted agents run in **isolated containers** and maintain **real-time connections (WebSocket, ZeroMQ, etc.)** to the other Divia.AI products, transparently powering AI capabilities everywhere — e.g. the right-sidebar AI chat in Divia.AI Professional, and the intended **Swarm + Enterprise co-deployment** that gives Enterprise's document/task/project features agent-powered upgrades.
- **Phase 00 (Ideation & Research) is NEXT**: a competitive deep-dive of the agent-framework field (architecture, agent lifecycle, scheduling/supervision, isolation/sandboxing models, integration surfaces), feeding the core stack decisions (async runtime, web/RPC framework, container runtime, database).

**The thesis this file extends:** autonomous agents operating within our ecosystem will **continually evolve various processes** — including improving the projects within the AIXO.Dev Platform itself. Recurring meta-maintenance work like the weekly `_backlog_TODOs` review is therefore very likely to become **one of the tasks handled every week by an autonomous agent**, not by a human-prompted session. The weekly review is probably our *first concrete instance* of this class.

## 3. Candidate inventory — recurring agent-level tasks we can already name

A starting taxonomy, to be grown during weekly reviews:

| # | Task | Cadence | Today | Natural long-term home |
|---|------|---------|-------|------------------------|
| 1 | `_backlog_TODOs` review: aggregate, refine, propose re-assignments | Weekly | Human + Claude session | Swarm agent → reports into aixodev-web |
| 2 | `_projects/README.md` index regeneration (done by hand this very session) | On change / weekly sweep | Manual | Agent task |
| 3 | Workflow-update propagation sweeps across the bootstrapped repos (LATER-001's "recall problem") | On upstream workflow change | Nobody | workgroups-defined, agent-executed |
| 4 | Repo hygiene heartbeat across all 24 projects: uncommitted changes, stale branches, unpushed-when-intended commits, failing validation suites | Weekly | Nobody | Agent task |
| 5 | Documentation drift detection (each repo's README vs. its actual state) | Monthly | Nobody | Agent task |
| 6 | Per-project backlog grooming (NEXT/LATER/SOMEDAY aging, "last reviewed" staleness) | Weekly–monthly | Sprint ritual, inconsistent | Agent task |
| 7 | Research refresh: re-run competitive landscapes (e.g. Swarm's own agent-framework deep-dive) and diff against the prior edition | Quarterly | One-shot research docs | Agent task — research docs become living documents |
| 8 | aixocode session-archive analytics digests (Phase 8 tie-in: what did the team's AI sessions do this week?) | Weekly | Phase 8 features, on-demand | Platform-side agent |
| 9 | Dependency / security-advisory sweeps across all repos | Weekly | Nobody | Agent task |
| 10 | Knowledge-graph rebuilds (graphify) + drift detection | On change | Manual per-session rule | Agent task |
| 11 | Cost ledger: aggregate token/effort spend across all agents & routines | Weekly | Nobody | Platform-side, self-accounting (see §6) |

Note the pattern: most of these are **exactly the MetaProject's mission** (cross-project loose-end catching) — which suggests the long-term meta-maintenance agent's working context is *this repo*, with its symlinks as the reach into every project.

## 4. The hosting spectrum — a migration path, not a binary choice

```
(a) ad-hoc human-prompted session          ← where the weekly review starts
(b) Claude Code /schedule cloud routine    ← available today, zero infra
(c) local cron + headless CLI agent        ← self-hosted, vendor-CLI-dependent
(d) workgroups hybrid-workflow dispatch    ← task DEFINED in the Platform (LATER-001 engine)
(e) Swarm-hosted resident agent            ← task EXECUTED by our own infrastructure
```

Each step trades convenience for ownership and integration depth. Key insight: **(d) and (e) are not alternatives — they're the two halves of the end state.** The Platform (workgroups → aixodev-web) defines *what/when/who-approves*; Swarm provides *the agent that does it*.

**Pragmatic near-term position:** run the weekly review as (a) or (b) now; keep the routine's prompt/definition **committed as a file** (not trapped in a vendor dashboard) so it stays portable across the whole spectrum; and treat every week's friction notes as **requirements-gathering for Swarm/workgroups Phase 00**. The recurring tasks we run before Swarm exists are Swarm's best possible product research.

## 5. The ownership question (a Phase 00 design axis)

**Proposed separation of concerns:**

- **`aixodev-workgroups` → AIXO.Dev Platform** = the *brain/ledger*: task definitions (hybrid deterministic+LLM workflows per LATER-001), schedules, assignment, approval queues, run history.
- **`divia_ai-swarm`** = the *body/runtime*: containers, agent lifecycle, supervision, model routing & effort tiering, credentials, real-time connections.
- **`aixodev-web`** = the *face*: dashboards, approvals, digests.

**Open design tensions to resolve in Phase 00:**

1. **Resident vs. ephemeral agents.** Is the weekly reviewer a long-lived *resident* with identity and accumulated memory, woken weekly — or an ephemeral job stamped out from a workflow definition each time? (Resident = relationship/memory/the "decades" vision; ephemeral = cheap, reproducible, stateless. Likely answer: ephemeral execution + durable externalized memory, giving both.)
2. **The cross-umbrella wrinkle.** Swarm is a **Divia.AI** product; the AIXO.Dev Platform is **ExoDev.AI**; meta-maintenance tasks span both families plus the household apps. Options: (a) Swarm is generic infrastructure with per-umbrella deployments; (b) dev-process agents run Platform-side while Swarm serves only product-AI; (c) one Swarm install hosts agents for both families with tenancy boundaries. This also affects Swarm's *commercial* story — "runs your dev-team's recurring agents" is a sellable Enterprise feature, and none of the OpenClaw-family competitors are positioned as an *ecosystem backbone* with deep product integration. Potential positioning edge for the competitive deep-dive.
3. **Standalone-mode parity.** Swarm's "works like OpenClaw out of the box" promise implies recurring-task scheduling should work *without* the Platform present — which argues for a minimal built-in scheduler in Swarm, with the Platform as the richer optional brain.

## 6. Identity, memory, trust, autonomy

- **Autonomy ladder** (graduation criteria per task, not global): **L0** reporter (read-only digest) → **L1** proposer (drafts PRs/diffs/backlog edits for human approval) → **L2** executor with deterministic gates (LATER-001's code-enforced checks as guardrails) → **L3** fully autonomous with after-the-fact audit. The weekly reviewer starts at L0/L1; mechanical tasks like index regeneration could earn L2 quickly.
- **Agent sessions ARE sessions.** aixocode's lossless-preservation guarantee should extend to autonomous runs: every Swarm agent session captured byte-for-byte like human CLI sessions. Autonomous work with *less* audit trail than interactive work would be backwards — arguably it needs *more*.
- **Memory:** the weekly reviewer should accumulate memory across runs (what was deferred, what John rejected and why) — the same pattern as Claude Code's per-project memory dir, but owned by our infrastructure.
- **Self-accounting:** every autonomous run records its own token/cost spend; the weekly digest includes its own cost line. Trust in autonomous agents is partly built from boring, honest bookkeeping.
- **The recursive loop, guarded:** agents improving the workflows that define agent tasks is the explicit goal ("continually evolving various processes") — and the moment where LATER-001's lineage tracking stops being optional. An agent doing a propagation sweep *needs* version-vector data; an agent editing workflow definitions needs its changes to flow through the same proposal/approval gates as code.

## 7. Wild ideation (explicitly invited — capture everything)

- **Agent NOC**: an aixodev-web dashboard of all recurring autonomous tasks — last run, findings, pending approvals, cost, autonomy level. The "ops center" for your agent fleet. (Natural aixocode Phase 8 / Platform analytics descendant.)
- **Monday Morning Briefing**: a meta-agent that aggregates *all* weekly agents' outputs into one human-paced digest. One inbox item, not eleven.
- **Ecosystem-native delivery surfaces**: agents deliver recaps not by email but through the ecosystem itself — a message thread in **Divia.Life Messages**, an entry in **DiviaHome's Activity Log**, a DiviaCard in the daily Journal page. Agents become *contacts* — entities in the Divia.AI PKMS with people-like pages (DiviaContacts viewing an agent's page, the way it views a colleague's). Dogfooding and product demo in one.
- **Adversarial weekly review**: run the review as a collab-group (the aixocode pattern): one agent proposes the aggregation/re-assignments, a second (different vendor — Codex) critiques before it reaches John. Catches lazy aggregation; mirrors the existing Claude+Codex collab workflows.
- **One gardener vs. a fleet**: a single named, long-lived "ecosystem gardener" persona handling all meta-maintenance (relationship, memory, trust accrue to one identity) vs. a fleet of single-purpose agents (isolation, least-privilege, easier autonomy-ladder grading). Hybrid: one *identity*, many *task bodies*.
- **Agents filing LATER-NNN items themselves**: `_backlog_TODOs/` as an agent-writable inbox — the weekly reviewer both consumes the backlog and *appends* to it when it notices cross-project loose ends (which is exactly the MetaProject memory-rule I already follow interactively; the autonomous version is the same behavior with a different trigger).
- **Living research documents**: recurring-research agents (taxonomy #7) maintain versioned editions of competitive landscapes with diff-summaries — "what changed in the agent-framework field since March." First customer: Swarm's own Phase 00 deep-dive.
- **Dogfooding chain**: aixocode's collab subsystem + Phase 7 workflow orchestration is the *local, laptop-scale precursor* of what Swarm does at server scale (sessions, supervision, multi-agent coordination). Lessons should flow aixocode → Swarm deliberately, and aixocode could later gain a "remote agent" pane showing your Swarm fleet beside your local terminals.
- **Divia.Network as agent transport**: agents as first-class Divia.Network participants — the same open integration layer that fans out "I had El Pollo Loco for dinner" can carry agent→app notifications and app→agent task requests. The integration standard then serves humans, apps, *and* agents uniformly.
- **Task market (SOMEDAY-grade, probably overkill)**: workgroups as a marketplace where idle Swarm agents bid on queued tasks by declared capability/cost. Noted for completeness; revisit only if static assignment proves limiting.
- **Effort-tiered scheduling** (LATER-001 echo): the Swarm scheduler budgets per-step model tiers — Haiku-medium for the mechanical aggregation pass, Fable-xhigh for the synthesis/judgment pass *within the same weekly task*.

## 8. Next actions (for weekly review)

- [ ] Add "where do recurring autonomous-agent tasks live" to `divia_ai-swarm` Phase 00 ideation scope (alongside the competitive deep-dive in its `_horizon_NEXT.md`), including §5's three design tensions; cross-reference this file.
- [ ] Decide the near-term weekly-review mechanism — manual session vs. `/schedule` cloud routine (offer currently open) — and commit its prompt/definition as a portable file either way.
- [ ] Pick 2–3 tasks from the §3 inventory as early pilots (suggested: #1 weekly review, #2 index regeneration, #4 repo-hygiene heartbeat) and start logging friction notes as Swarm/workgroups requirements.
- [ ] When `aixodev-workgroups` Phase 00 opens, reconcile its task-assignment model with §5's brain/body split (joint review with LATER-001).
- [ ] During Swarm's competitive deep-dive, explicitly evaluate each framework's answer to *recurring scheduled tasks* and *ecosystem integration* — the two axes where Swarm intends to differentiate.
