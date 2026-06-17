# Product — aixodev-collabs

> The design home for the **next-generation multi-agent collaboration & decision engine** — the
> successor to the third-party `ensemble` tool that currently powers `/collab`. Deep research done;
> the Flask prototype is unbuilt.

- **Repo:** `aixodev-collabs` · **Umbrella:** AIXO.Dev · **License:** Undocumented (no manifest yet).
- **Status:** 🟠 Phase 00 research **complete** (a 14-chapter ensemble-internals teardown + a 22-track world survey of multi-LLM collaboration), **zero app code.**

## What it is (consensus)
A planned Flask/SQLAlchemy prototype for **how agents + humans coordinate, divide, review, and decide.** The research diagnoses `ensemble` (third-party, MIT, frozen, Node/TS, pastes messages into tmux) as "transports text but models nothing" — no task model, screen-scraped state, completion detected by regex on "done." The next-gen design (R1–R18) owns **only the cross-vendor bridge** (delegate intra-vendor fan-out to Claude/Codex's own subagents): an append-only SQLite event log + per-seat pull mailboxes, a typed envelope, an engine-owned task FSM, progress-ledger supervision, structured vendor channels (no screen-scraping), digest-on-resume, a human-partner steering surface with irreversibility gating, git-mediated work discipline, a low-cost "secretary seat" (Haiku/local), and budget circuit-breakers. Key findings: **N=2 is the right scale**; **tests arbitrate, not rhetoric**; independent-answer-first + anonymized authorship beats forced-consensus debate; **cost is existential** (input tokens dominate ~150:1; re-reading context is the cost center).

> Baseline error: collabs is **not** the `_workflows/` "root" — it's a middle link in the bootstrap chain (see [`../../ERRATA.md` E-09`](../../ERRATA.md)).

## Ideation & Exploration (capture everything, commit to nothing)
- **From research (frontier/exotic):** stigmergy / artifact-as-coordination (pressure-field beats conversation ~4×; TODO/FIXME-as-pheromone); learned/dynamic topologies (edge-prune-on-malice); generative-agent societies (observe→reflect→plan memory for digests); agent economies (reputation-weighted voting; cost-aware task auctions); evolutionary self-improving teams (with a **sharp warning**: a self-improving coder doubled its score by *deleting its own hallucination markers* → eval-gate the mutator against a frozen baseline + human merge gate); blackboard architectures; "the Room" reconception (the log *is* the room; commit-reveal escrow turns; expiring/self-superseding messages); shared-KV rooms; provider-hosted rooms; sub-second supervisor cadence.
- ✦ **New:** this engine + `aixodev-workgroups` are the two halves of the next-gen multi-agent system (collabs = how agents talk/decide; workgroups = how work is claimed/tracked) — and together they're the natural **"brain" half** of the LATER-002 brain/body/face split, with Swarm as the body. Design the Flask data model so the cross-vendor bridge lifts cleanly into both aixodev-web *and* Divia.AI AgentSwarms. ✦ The adversarial-verify / diverse-lens-jury findings here are directly reusable as the quality pattern for *every* recurring-agent story in this reference (GTD, dev stewardship, the partners' brief).
