# Product — aixodev-workgroups

> The prototype for **runtime agent task-coordination & assignment** — how agents + humans claim,
> lock, divide, hand off, sequence, and track work as a "workgroup." The most direct AIXO-side home
> for "where recurring autonomous-agent tasks get assigned."

- **Repo:** `aixodev-workgroups` · **Umbrella:** AIXO.Dev · **License:** Undocumented.
- **Status:** 🟠 Phase 00 **pending** (not started); zero code. Planned: Flask system-of-record **+ a FastAPI status sidecar**.

## What it is (consensus)
A planned two-process prototype: **Flask** as the durable system-of-record (tasks, assignments, claim/lock, hand-off, dependency ordering, conflict resolution) plus a dedicated **FastAPI + Uvicorn status sidecar** sharing one SQLAlchemy schema, handling high-frequency "currently working on…" / time-tracking heartbeats out-of-band so they aren't queued behind the slow LLM request path. The single-process-async-vs-two-process question is the central Phase-00 design bet. Same "Prototype Freedom" posture; merges into `aixodev-web` (the sidecar may become an async route group, a separate service, or a background worker on re-merge). Anticipated gotchas pre-recorded: SQLite write-contention between the two processes; keeping their engines/sessions consistent.

## Relevance to LATER-001/002
This is the prototype for the **task-definition/assignment "brain"** in the brain/body/face split: the owning product defines *what/when/who-approves*; Swarm provides *the agent that does it*. Pairs with `aixodev-collabs` (the messaging/decision substrate). Together they're where "recurring autonomous-agent tasks live and get assigned" on the AIXO.Dev side.

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** validate the Flask/FastAPI split in Phase 00; research claiming/locking, division/hand-off, dependency ordering, progress reporting, and inter-agent conflict resolution.
- ✦ **New:** make this the home of the **autonomy ladder** (L0 reporter → L1 proposer → L2 gated executor → L3 autonomous with audit) — task definitions carry their own autonomy grade, approval queue, and run history (LATER-002 §8/§9). ✦ The "task market (SOMEDAY)" idea — idle Swarm agents bidding on queued tasks by declared capability/cost — would live here as the assignment policy, if static assignment ever proves limiting. ✦ Self-accounting: every task definition records the token/cost spend of its runs, so the cost-ledger recurring agent (LATER-002 §4 #11) reads straight from the workgroups brain.
