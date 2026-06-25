# CANON-001 — Canonicalize `run_dev_server.sh` (skeleton-gen for new projects + standardize across the fleet)

- **Captured:** 2026-06-25, while working in `txfrcloud-protomolecule`
- **Status:** OPEN — gated by CANON-002 (settle the template layout first)
- **Related:** `_canonical/NEW_PROJECT_GUIDE.md`; the per-stack **Skeleton Generation** sections in `_canonical/project-template/_workflows/techstacks/`; `../_backlog_TODOs/LATER-001` (cross-project propagation)

`run_dev_server.sh` is an MC-style (`/sbin/service`-pattern) Quart/Flask dev-server controller — `start|stop|restart|status|logs`, with PID-file tracking, port-conflict detection, and graceful SIGTERM→SIGKILL. It originated as the Flask `dev_server.sh` (aixodev-web), was adapted to Quart in `fracrealhomes-dailyspikedriver`, and was pulled into `txfrcloud-protomolecule` on 2026-06-25 (env-prefix / banner / default-port tokenized; default port 5055 to avoid colliding with the sibling on 5050). It is generic web-dev infrastructure that essentially every Quart/Flask project wants.

**Two halves (the create + propagate pattern):**
1. **New projects** — fold it into each web techstack doc's **Skeleton Generation** section, with the port and env-prefix tokenized, so `init_new_project.py` / the New Project workflow emits it automatically.
2. **Existing projects** — standardize it across the fleet's web projects as part of the deliberate, **manual, one-repo-at-a-time** cleanup (no automated sync).

**Why deferred:** don't bake it into Skeleton Generation until the `_canonical/project-template/` directory structure is settled (CANON-002) — the script's paths (`logs/`, `.dev-server.pid`, `run.py`) and its placement depend on the finalized layout. Look into both together.
