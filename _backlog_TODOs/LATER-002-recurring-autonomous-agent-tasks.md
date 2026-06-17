# LATER-002 — Recurring Autonomous-Agent Tasks: Where Do They Live Long-Term?

- **Captured:** 2026-06-12, MetaProject session (immediately following [LATER-001](LATER-001-workflow-lineage-and-hybrid-formalization.md)); **revised same day** to add the GTD Weekly Review use-case and the cross-product framing
- **Status:** LATER — scratchpad for weekly backlog review; feeds `divia_ai-agentswarms` Phase 00 research scope
- **Eventual owning projects:** `divia_ai-agentswarms` (primary — the "where do agents run" question), `divia_ai-enterprise` (the GTD/task-management use-case, §5), `aixodev-workgroups` (task definition/assignment, see LATER-001), `aixodev-web` (surfacing/approvals)
- **Related:** LATER-001 · `divia_ai-agentswarms/CLAUDE.md` + `README.md` · `divia_ai-agentswarms/_specs_and_plans/_backlog/_horizon_NEXT.md` (competitive deep-dive item) · `aixodev-aixocode` Phase 8 (Analytics & Knowledge) · [GTD Weekly Review® official checklist (PDF)](https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf)

> **Nature of this file (per John):** a deliberately wide-scope scratchpad. Record *all* ideas we have right now — both to preserve what we were thinking for the future discussion, and to widen the considered space of use-cases, improvement opportunities, and alternate implementations. Nothing here is committed-to; everything here is fair game to discard.

---

## 1. The triggering question

While setting up `_backlog_TODOs/` and its **weekly review routine**, the immediate implementation offer was a Claude Code `/schedule` cloud routine. That works today — but it raises the real question: **where should ongoing "autonomous agent"-level tasks belong long-term within our ecosystem?** Vendor-hosted scheduling (Claude Code cloud routines), local cron, the AIXO.Dev Platform, or our own agent-hosting infrastructure?

This is properly a **Phase 00 research question for `divia_ai-agentswarms`** — and, as §3 below frames it, the question is much bigger than developer tooling: the same capability class shows up in *every* product family we ship.

## 2. Context from `divia_ai-agentswarms` (pulled from its repo docs, 2026-06-12)

- **Divia.AI AgentSwarms** is a Rust server providing **containerized hosting for multiple autonomous Divia.AI agents** — same family as OpenClaw, IronClaw, PicoClaw, NanoClaw, Hermes Agent, and the broader field of agent frameworks/harnesses. Stood up alone, it works like those tools out of the box; its purpose-built role is the **AI backbone of the Divia.AI ecosystem**.
- Hosted agents run in **isolated containers** and maintain **real-time connections (WebSocket, ZeroMQ, etc.)** to the other Divia.AI products, transparently powering AI capabilities everywhere — e.g. the right-sidebar AI chat in Divia.AI Professional, and the intended **Swarm + Enterprise co-deployment** that gives Enterprise's document/task/project features agent-powered upgrades.
- **Phase 00 (Ideation & Research) is NEXT**: a competitive deep-dive of the agent-framework field (architecture, agent lifecycle, scheduling/supervision, isolation/sandboxing models, integration surfaces), feeding the core stack decisions (async runtime, web/RPC framework, container runtime, database).

**The thesis this file extends:** autonomous agents operating within our ecosystem will **continually evolve various processes** — including improving the projects within the AIXO.Dev Platform itself — and recurring "review and improve" work like the weekly `_backlog_TODOs` review will be **handled every week by autonomous agents**, not human-prompted sessions. Crucially, this is *not* a dev-tools-only thesis: §§4–6 show the same recurring-agent capability expressed in completely different products.

## 3. The cross-product frame — one capability, many product-specific expressions

The underlying AI capability — **Swarm-hosted autonomous agents running recurring review/improve/suggest cycles** — is shared infrastructure. What differs per product is the *domain* it's pointed at. This document deliberately holds two contrasting flagship use-cases side by side, plus a ring of satellites, because the contrast is what clarifies the ultimate goal: **explore and dream up every possible way to improve every use-case, across all the products, each in its own domain-specific way, all riding the same underlying AI backbone.**

- **Use-case A (§4)** — *AIXO.Dev Platform (ExoDev.AI family):* continually improving **software projects** and the development process itself. Audience: dev teams. Domain objects: repos, backlogs, workflows, sessions.
- **Use-case B (§5)** — *Divia.AI Enterprise + Swarm (Divia.AI family):* the **GTD Weekly Review**, agent-assisted. Audience: any human managing their work/life. Domain objects: inboxes, projects, next-actions, calendars, someday/maybes.
- **Satellites (§6)** — TastyPal, Sattvasic Health, LegendaryMoney, DiviaContacts, DiviaHome, KingStrat: each gets its own recurring-agent expression.

### The cross-cutting principle: discover-and-suggest from implicit data — don't interrogate

A principle evident throughout most of the products across our entire ecosystem and product families: **it is far better to discover-and-suggest what human-users might like, based on their implicit real-world choices, than to explicitly ask them to fill out forms about themselves.** (Don't ask the user to enumerate "foods I like" — observe what they actually ate.) Implicit real-world data surfaces insights that even the human-user themselves may not realize ahead of time. Recurring autonomous agents are the natural *consumers* of this principle: they are the thing that periodically sweeps the accumulated implicit data and turns it into suggestions, drafts, and discoveries. Nearly every idea in §§4–7 is an instance of it.

## 4. Use-case A — AIXO.Dev Platform: continually improving software projects

The ExoDev.AI expression: agents as **true co-developer partners** (the core AIXO.Dev vision) who don't just write code on demand but carry recurring stewardship of the projects and of the development *process itself* — the meta-maintenance that human teams chronically drop because it's important-but-never-urgent. The implicit-data principle applies here too: the agents work from what the repos, sessions, and backlogs *actually show* (captured losslessly by aixocode), not from what developers self-report in status meetings.

Candidate inventory of recurring agent-level tasks we can already name (to be grown during weekly reviews):

| # | Task | Cadence | Today | Natural long-term home |
|---|------|---------|-------|------------------------|
| 1 | `_backlog_TODOs` review: aggregate, refine, propose re-assignments | Weekly | Human + Claude session | Swarm agent → reports into aixodev-web |
| 2 | `_projects/README.md` index regeneration (done by hand this very session) | On change / daily sweep | Manual | Agent task |
| 3 | Workflow-update propagation sweeps across the bootstrapped repos (LATER-001's "recall problem") | On upstream workflow change | Nobody | workgroups-defined, agent-executed |
| 4 | Repo hygiene heartbeat across all 24 projects: uncommitted changes, stale branches, unpushed-when-intended commits, failing validation suites | 3x Weekly | Nobody | Agent task |
| 5 | Documentation drift detection (each repo's README vs. its actual state) | 2x Monthly | Nobody | Agent task |
| 6 | Per-project backlog grooming (NEXT/LATER/SOMEDAY aging, "last reviewed" staleness) | Weekly–monthly | Sprint ritual, inconsistent | Agent task |
| 7 | Research refresh: re-run competitive landscapes (e.g. Swarm's own agent-framework deep-dive) and diff against the prior edition | Monthly | One-shot research docs | Agent task — research docs become living documents |
| 8 | aixocode session-archive analytics digests (Phase 8 tie-in: what did the team's AI sessions do this week?) | Weekly | Phase 8 features, on-demand | Platform-side agent |
| 9 | Dependency / security-advisory sweeps across all repos | 2x Weekly | Nobody | Agent task |
| 10 | Knowledge-graph rebuilds (graphify) + drift detection | On change | Manual per-session rule | Agent task |
| 11 | Cost ledger: aggregate token/effort spend across all agents & routines | Weekly | Nobody | Platform-side, self-accounting (see §9) |

Note the pattern: most of these are **exactly the MetaProject's mission** (cross-project loose-end catching) — which suggests the long-term meta-maintenance agent's working context is *this repo*, with its symlinks as the reach into every project.

## 5. Use-case B — the GTD Weekly Review, agent-assisted (Divia.AI Enterprise + Swarm)

### 5.1 What the GTD Weekly Review is

In David Allen's *Getting Things Done* methodology, the **Weekly Review®** is the maintenance ritual that keeps the whole system alive. The [official David Allen Company checklist](https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf) structures it as **three phases, eleven steps**:

- **GET CLEAR** — *(1)* Collect Loose Papers and Materials (gather everything into the in-tray); *(2)* Get "IN" to Zero (process completely all outstanding papers, journal/meeting notes, voicemails, dictation, emails); *(3)* Empty Your Head (put in writing any uncaptured new projects, action items, waiting-for's, someday/maybe's).
- **GET CURRENT** — *(4)* Review Action Lists (mark off completed; capture further steps); *(5)* Review Previous Calendar Data (mine the past week for remaining actions/reference); *(6)* Review Upcoming Calendar (capture actions triggered by what's coming); *(7)* Review Waiting-For List (follow up; check off received); *(8)* Review Project (and Larger Outcome) Lists (evaluate every project one by one, **ensuring at least one current next-action on each**); *(9)* Review Any Relevant Checklists.
- **GET CREATIVE** — *(10)* Review Someday/Maybe List (activate what's become live; delete what's dead); *(11)* Be Creative and Courageous ("any new, wonderful, hare-brained, creative, thought-provoking, risk-taking ideas to add into your system???").

### 5.2 Why GTD adherents treat it as the keystone — and why they skip it

Allen calls the Weekly Review the **"critical success factor"** of GTD. The method's entire psychological payoff — the trusted system, the "mind like water" state where nothing gnaws at you because everything is captured and current — **only holds if the system is actually reviewed regularly**. A stale system stops being trusted; an untrusted system means the brain quietly takes back the job of remembering everything, and the practitioner is back where they started.

And yet the Weekly Review is also GTD's **most notoriously skipped practice**: done properly it takes 1–2 focused hours, it's clerical and effortful, and it competes with everything else on a Friday afternoon. "I fell off the wagon because I stopped doing weekly reviews" is the canonical GTD failure story. **The single biggest point of failure in the methodology is a mostly-mechanical chore.** That is precisely the shape of problem recurring autonomous agents are best at.

### 5.3 The agent-assisted design: first pass by agent, judgment by human

The ecosystem already funnels captures from every surface into Divia-app **Inboxes**: the Divia.AI Professional desktop app, the Divia.Life mobile apps (Journal, Agenda, quick capture), the **DiviaHome kitchen-counter device**, DiviaContacts-logged emails and calls. Scattered TODO notes from throughout the week, captured wherever the human happened to be — exactly GTD's "collect" ideal, already implemented as product surfaces.

The autonomous agent then does the **first pass** ahead of the human's review session:

| GTD step | Agent first pass | What stays human |
|---|---|---|
| Collect / IN to zero | Sweep all Divia Inboxes; pre-clarify each capture: actionable? next-action phrased as a concrete verb; project association suggested; 2-minute candidates flagged | Final disposition of anything ambiguous |
| Empty Your Head | **Implicit-principle applied:** surface open loops the human never explicitly captured — commitments made in passing in logged calls/emails/messages/Activity Log ("you told Sarah you'd send the contract; no task exists for that") | Confirming which detected loops are real commitments |
| Review Action Lists | Pre-mark actions that observable data says are done (the email *was* sent); flag stale ones | Renegotiating commitments with oneself — **the heart of GTD, never automated** |
| Previous / Upcoming Calendar | Auto-mined residue from last week + drafted prep actions for next week | Judgment on what matters |
| Waiting-For | Aging report; detect arrivals (the reply *did* come in); draft follow-up nudges | Deciding to send the nudge |
| Project Lists | **Stalled-project detection**: flag every project violating the ≥1-next-action invariant or unmoved in N weeks; *draft* candidate next actions | Choosing the action; killing or keeping projects |
| Someday/Maybe | Re-rank against current life context; resurface items whose stated preconditions came true ("you said *someday, after the kitchen remodel* — the Activity Log says it finished") | The yes/no |
| Be Creative | 2–3 provocations mined from implicit data ("you've journaled about X three times this month — make it a project?") | The actual creativity and courage |

**The trust boundary (important):** the agent **never completes, deletes, or commits** anything — it stages proposals. GTD's psychology depends on the human personally renegotiating their commitments; automate that and the method hollows out. The agent is the **clerk**; the human remains the **executive**. (This is the L0/L1 rung of the autonomy ladder in §9, and for personal-life data it should probably *stay* there longer than dev-tooling tasks do.)

**The payoff:** the 1–2-hour chore compresses to a ~20-minute confirm-and-decide session delivered as a ready-made **review packet**. That directly attacks GTD's #1 failure mode (skipping the review) — and thereby *accelerates everything GTD advertises on the tin*: the trusted system stays trusted even on overloaded weeks, "mind like water" becomes sustainable rather than aspirational, and the Get Creative phase — the part humans skip first when tired — actually happens, every week, with the agent holding the door open.

### 5.4 Why this belongs to Divia.AI Enterprise

This use-case sits squarely inside **Divia.AI Enterprise's** scope — the PKMS-plus-Asana-style project/task-management server — with the AI capabilities supplied, as always, by the **connected Divia.AI AgentSwarms server** (the intended Swarm + Enterprise co-deployment from §2). It is exactly the kind of "dramatically upgraded, agent-powered capability" the Enterprise positioning promises, and a marquee demo of it: *"Enterprise doesn't just store your tasks — it prepares your Weekly Review."* Note the contrast with Use-case A: **same backbone, same recurring-agent pattern, completely different brain** (Enterprise's task graph vs. workgroups' project/workflow ledger) and completely different domain.

## 6. Satellite expressions across the other product families

Each one is the implicit-data principle plus a recurring agent, expressed in a different domain:

- **TastyPal / TastyPantry** — *(John's example)* an agent reviews all the foods the user actually ate this week and researches other foods/recipes online they might also enjoy — discovery from real eating behavior, never a "what foods do you like?" form. Same pattern inward: notice staples depleting from consumption patterns and draft the shopping list before being asked.
- **Sattvasic Health** — weekly correlation pass over labs/CGM/weight/macros/Rx: surface *hypotheses* ("sleep-quality dips follow late-eating days") as suggestions for the human (and their doctor) to evaluate — insights the user wouldn't think to query for.
- **LegendaryMoney** — nightly and weekly ledger reviews: confidence-aware anomaly surfacing, balance-assertion drift, recurring-charge changes; *learn* categorization rules from the user's observed corrections instead of asking them to configure rules.
- **DiviaContacts** — relationship-cadence review from logged email/call activity: "you haven't replied to X in three weeks — and last time you said you would." Drafts the reconnection, never sends it.
- **DiviaHome** — the household's review, deliberately run **nightly rather than weekly**: maintenance schedules and chore rhythms *learned* from the Activity Log, and — critically — **consumption-driven replenishment** that only a daily cadence can catch. When observed usage patterns imply a staple is running low ("we're nearly out of milk"), the nightly agent adds it to a **time-decaying grocery list** (e.g. a "needed within 72 hrs, priority escalating every 24 hrs" item) and correspondingly **raises the weighted priority of the grocery-run errand** as that deadline approaches. The kitchen-counter device doubles as both a capture surface feeding §5 and a delivery surface for the household packet. (The weekly cadence elsewhere in this list is the *default*; replenishment-driven domains like the household want a tighter nightly loop.)
- **KingStratVC Knowledgebase** — weekly sweep of news/filings/funding events across the firm's tracked portfolio and idea-stage startups, delivered as a Monday partners' brief. *(Product naming, settled: the firm is **Kingmaker Strategic**, commonly abbreviated **KingStratVC**; the product-facing name is "**KingStratVC Knowledgebase**," while the repository/directory keeps the developer-level short name **`kingstratvc-web`**. "Knowledgebase" is a descriptive noun for what the application does — there's no need to carry it at the code level.)*

## 7. The hosting spectrum — a migration path, not a binary choice

```
(a) ad-hoc human-prompted session          ← where the weekly review starts
(b) Claude Code /schedule cloud routine    ← available today, zero infra
(c) local cron + headless CLI agent        ← self-hosted, vendor-CLI-dependent
(d) Platform-dispatched hybrid workflow    ← task DEFINED in the owning product's brain (LATER-001 engine)
(e) Swarm-hosted resident agent            ← task EXECUTED by our own infrastructure
```

Each step trades convenience for ownership and integration depth. Key insight: **(d) and (e) are not alternatives — they're the two halves of the end state.** The owning product defines *what/when/who-approves*; Swarm provides *the agent that does it*. The dev-ecosystem tasks (§4) can start at (a)/(b) today; the consumer use-cases (§§5–6) effectively *require* (e), since "mail your family's inboxes to a vendor cron job" is not a product.

**Pragmatic near-term position:** run the weekly `_backlog_TODOs` review as (a) or (b) now; keep the routine's prompt/definition **committed as a file** (not trapped in a vendor dashboard) so it stays portable across the whole spectrum; and treat every week's friction notes as **requirements-gathering for Swarm/workgroups Phase 00**. The recurring tasks we run before Swarm exists are Swarm's best possible product research.

## 8. The ownership question (a Phase 00 design axis)

**Proposed separation of concerns — the brain/body/face split, instantiated per product family:**

| Role | AIXO.Dev expression (Use-case A) | Divia.AI expression (Use-case B) |
|---|---|---|
| **Brain** (task definitions, schedules, approval queues, run history) | `aixodev-workgroups` → AIXO.Dev Platform | **Divia.AI Enterprise** (task/project graph) |
| **Body** (containers, lifecycle, supervision, model routing, credentials, real-time connections) | Swarm (or a Platform-side runner — open question) | **Divia.AI AgentSwarms** |
| **Face** (dashboards, approvals, digests, packet delivery) | `aixodev-web` | Professional / Divia.Life / DiviaHome surfaces |

The two-column table *is* the §3 thesis in architectural form: same body, different brains and faces.

**Open design tensions to resolve in Phase 00:**

1. **Resident vs. ephemeral agents.** Long-lived *resident* with identity and accumulated memory, woken weekly — or an ephemeral job stamped out per run? (Resident = relationship/memory/the "decades" vision; ephemeral = cheap, reproducible, stateless. Likely answer: ephemeral execution + durable externalized memory, giving both.)
2. **The cross-umbrella wrinkle.** Swarm is a **Divia.AI** product; the AIXO.Dev Platform is **ExoDev.AI**; meta-maintenance tasks span both families plus the household apps. Options: (a) Swarm is generic infrastructure with per-umbrella deployments; (b) dev-process agents run Platform-side while Swarm serves only product-AI; (c) one Swarm install hosts agents for both families with tenancy boundaries. This also affects Swarm's *commercial* story — both "runs your dev-team's recurring agents" *and* "prepares your team's GTD reviews" are sellable Enterprise features, and none of the OpenClaw-family competitors are positioned as an *ecosystem backbone* with deep product integration. Potential positioning edge for the competitive deep-dive.
3. **Standalone-mode parity.** Swarm's "works like OpenClaw out of the box" promise implies recurring-task scheduling should work *without* any brain present — which argues for a minimal built-in scheduler in Swarm, with the owning products as the richer optional brains.

## 9. Identity, memory, trust, autonomy

- **Autonomy ladder** (graduation criteria per task, not global): **L0** reporter (read-only digest) → **L1** proposer (drafts PRs/diffs/nudges/next-actions for human approval) → **L2** executor with deterministic gates (LATER-001's code-enforced checks as guardrails) → **L3** fully autonomous with after-the-fact audit. Dev tasks like index regeneration can earn L2 quickly; **personal-life tasks (§5–6) should deliberately linger at L0/L1** — both for trust and because (per §5.3) human disposition *is the product* in the GTD case.
- **Agent sessions ARE sessions.** aixocode's lossless-preservation guarantee should extend to autonomous runs: every Swarm agent session captured byte-for-byte like human CLI sessions. Autonomous work with *less* audit trail than interactive work would be backwards — arguably it needs *more*. For personal-data agents this shades into privacy architecture: the audit trail itself is intimate data and stays on the user's own servers.
- **Memory:** recurring agents should accumulate memory across runs — what was deferred, what the human rejected and why, which suggestion styles land. (The GTD reviewer that remembers "John always rejects drafted nudges to family members" is learning the *person*, which is the whole Divia.AI premise — and the dev-agent equivalent is learning the *team*, which is the whole AIXO.Dev premise. Same mechanism again.)
- **Self-accounting:** every autonomous run records its own token/cost spend; every weekly digest includes its own cost line. Trust in autonomous agents is partly built from boring, honest bookkeeping.
- **The recursive loop, guarded:** agents improving the workflows that define agent tasks is the explicit goal ("continually evolving various processes") — and the moment where LATER-001's lineage tracking stops being optional. An agent doing a propagation sweep *needs* version-vector data; an agent editing workflow definitions needs its changes to flow through the same proposal/approval gates as code.

## 10. Wild ideation (explicitly invited — capture everything)

**Cross-product / infrastructure:**

- **Agent NOC**: an aixodev-web dashboard of all recurring autonomous tasks — last run, findings, pending approvals, cost, autonomy level. The "ops center" for your agent fleet. (Natural aixocode Phase 8 / Platform analytics descendant; the consumer twin is a gentler "your agents this week" card in Professional/Divia.Life.)
- **Monday Morning Briefing**: a meta-agent aggregating *all* weekly agents' outputs into one human-paced digest. One inbox item, not eleven. (For a household: one briefing spanning GTD packet + pantry + health + money — the Divia.Network fan-out run in reverse, as a fan-*in*.)
- **Ecosystem-native delivery surfaces**: agents deliver recaps not by email but through the ecosystem itself — a message thread in **Divia.Life Messages**, an entry in **DiviaHome's Activity Log**, a DiviaCard in the daily Journal page. Agents become *contacts* — entities in the Divia.AI PKMS with people-like pages (DiviaContacts viewing an agent's page the way it views a colleague's). Dogfooding and product demo in one.
- **Adversarial weekly review**: run reviews as a collab-group (the aixocode pattern): one agent proposes, a second (different vendor — Codex) critiques before it reaches John. Catches lazy aggregation; mirrors the existing Claude+Codex collab workflows.
- **One gardener vs. a fleet**: a single named, long-lived persona handling all meta-maintenance (relationship, memory, trust accrue to one identity) vs. a fleet of single-purpose agents (isolation, least-privilege, easier autonomy-ladder grading). Hybrid: one *identity*, many *task bodies*.
- **Agents filing LATER-NNN items themselves**: `_backlog_TODOs/` as an agent-writable inbox — the weekly reviewer both consumes the backlog and *appends* to it when it notices cross-project loose ends. (And the GTD twin: the §5 agent appending to the *human's* someday/maybe list — same behavior, different inbox.)
- **Living research documents → Divia.AI Enterprise "Research Projects" + `.dvai` LiveDocuments**: recurring-research agents maintain versioned editions of competitive landscapes with diff-summaries — "what changed in the agent-framework field since March." First customer: Swarm's own Phase 00 deep-dive. **This deserves promotion from a footnote to a first-class product feature.** On the commercial side it becomes a marquee capability of **Divia.AI Enterprise's "Research Projects"**: a research project is an *agent-tended, continuously-updated body of knowledge*, not a one-shot report. The natural substrate is the **Divia Document Format** — the SQLite-based `.dvai` files — extended with a **"LiveDocument"** mode (working name): a `.dvai` document that knows how to refresh itself, holds its own revision history inside the SQLite container, renders inline "what changed since last refresh" diffs, and is driven on a schedule by a Swarm-hosted research agent. One format + one agent pattern then serves both dev-side living research (Swarm's competitive deep-dive, re-run monthly) and consumer/commercial knowledge work (a KingStratVC portfolio dossier, a Sattvasic-Health literature watch, a LegendaryMoney market brief) — each in its own domain, all on the same backbone.
- **Dogfooding chain**: aixocode's collab subsystem + Phase 7 workflow orchestration is the *local, laptop-scale precursor* of what Swarm does at server scale. Lessons should flow aixocode → Swarm deliberately, and aixocode could later gain a "remote agent" pane showing your Swarm fleet beside your local terminals.
- **Divia.Network as agent transport**: agents as first-class Divia.Network participants — the same open integration layer that fans out "I had El Pollo Loco for dinner" carries agent→app notifications and app→agent task requests. The standard then serves humans, apps, *and* agents uniformly.
- **Task market (SOMEDAY-grade, probably overkill)**: the brain as a marketplace where idle Swarm agents bid on queued tasks by declared capability/cost. Noted for completeness; revisit only if static assignment proves limiting.
- **Effort-tiered scheduling → typed Swarm workflow steps** (LATER-001 echo): the Swarm scheduler budgets per-step model tiers — Haiku-medium for the mechanical aggregation pass, Fable-xhigh for the synthesis/judgment pass *within the same weekly task*. **This may warrant a deeper conceptual reframe.** Rather than "model tiers bolted onto a task," model the recurring task as a **workflow defined on the Divia.AI AgentSwarms server** whose steps are explicitly **typed as either deterministic (plain code — a `git pull`, a SQL aggregate, a file diff) or probabilistic (an LLM call)**. Deterministic steps are cheap, reproducible, and need no model at all; each **probabilistic** step then *additionally* declares its effort tier (Haiku-medium for mechanical clarification, Fable-xhigh for judgment/synthesis). This makes cost, reproducibility, and *where the AI actually is* legible at the workflow level, and it dovetails cleanly with LATER-001's deterministic-gate guardrails — the gates simply *are* the deterministic steps. It's the Swarm-server expression of the same brain/body split: the workflow definition is brain-side; the typed-step execution is body-side.

**GTD-specific magnifiers (extending §5.3):**

- **Continuous micro-reviews**: the agent runs silent daily mini-passes (clarify new captures, detect arrivals, update staleness counters) so the weekly review never faces a mountain. The weekly session becomes a true *checkpoint* rather than a dig-out. (Allen's dream, minus the discipline cost.)
- **The Sunday-evening packet** (ties to "agents as contacts"): a Divia.Life message — "Your review packet is ready: 14 items clarified, 3 stalled projects, 2 aged waiting-fors, 3 creative prompts. ~20 minutes." Review-completion rate becomes a product metric.
- **Two-minute-rule staging**: GTD says do anything under two minutes immediately; the agent pre-stages drafts for the two-minute items (the reply, the calendar hold, the renewal click) so the human's "do" is one approval tap each.
- **Adaptive checklist**: the canonical 11 steps, but reordered/weighted by what this user actually lets slide (their waiting-fors rot; their someday/maybe is pristine) — the implicit principle applied to the review *itself*.
- **Review-the-reviewer**: a quarterly meta-pass where the agent reports its own precision ("you accepted 71% of my drafted next-actions; rejections cluster around family commitments") and proposes recalibration. Trust through measured humility.
- **Cross-app Get Creative**: the §11 "creative and courageous" prompts drawn from the *whole* ecosystem's implicit data — journal themes (Divia.Life), eating adventurousness (TastyPal), spending patterns (LegendaryMoney) — surfacing project ideas no single app could see.

## 11. Next actions (for weekly review)

- [ ] Add "where do recurring autonomous-agent tasks live" to `divia_ai-agentswarms` Phase 00 ideation scope (alongside the competitive deep-dive in its `_horizon_NEXT.md`), including §8's three design tensions; cross-reference this file.
- [ ] When `divia_ai-enterprise` eventually activates (post-DiviaHome-v1 per its placeholder status), fold §5 (agent-assisted GTD Weekly Review) into its requirements as a marquee Swarm+Enterprise co-deployment feature.
- [ ] Consider promoting §3's **implicit-data principle** ("discover-and-suggest, don't interrogate") into a canonical ecosystem-wide design-principles doc — it's load-bearing across at least six products and currently lives nowhere official.
- [ ] Decide the near-term weekly-review mechanism — manual session vs. `/schedule` cloud routine (offer currently open) — and commit its prompt/definition as a portable file either way.
- [ ] Pick 2–3 tasks from the §4 inventory as early pilots (suggested: #1 weekly review, #2 index regeneration, #4 repo-hygiene heartbeat) and start logging friction notes as Swarm/workgroups requirements.
- [ ] When `aixodev-workgroups` Phase 00 opens, reconcile its task-assignment model with §8's brain/body/face split (joint review with LATER-001).
- [ ] During Swarm's competitive deep-dive, explicitly evaluate each framework's answer to *recurring scheduled tasks* and *ecosystem/product integration* — the axes where Swarm intends to differentiate (now for both dev-team and consumer/GTD workloads).

---

*GTD and Weekly Review® are trademarks of the David Allen Company; methodology details above per the official checklist ([gettingthingsdone.com PDF](https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf)).*
