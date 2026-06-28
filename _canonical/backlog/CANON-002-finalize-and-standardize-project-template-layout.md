# CANON-002 — Finalize & standardize the project-template directory structure

- **Captured:** 2026-06-25, while working in `txfrcloud-protomolecule`
- **Layout finalized:** 2026-06-28 (the GEN2 split)
- **Status:** LAYOUT FINALIZED — existing-repo standardization ONGOING (manual, one repo at a time, via `MIGRATE_ADAPT.md`)
- **Related:** `_canonical/project-template/`; `_canonical/NEW_PROJECT_GUIDE.md` §5 (the decided layout); `_canonical/MIGRATE_ADAPT.md` (the migration playbook); `../_backlog_TODOs/LATER-001`

## Resolved — the GEN2 layout (2026-06-28)

The previously-open layout questions are **decided and implemented in `_canonical/project-template/`**. The overloaded `_specs_and_plans/` was split into three root-level directories, plus three new standard scaffolds:

- `_backlog/` — unscheduled ideas (4 horizon files) — *was* `_specs_and_plans/_backlog/`
- `_research/` — investigations / analyses / syntheses (project root) — *was* `_specs_and_plans/_research/`
- `_stages_and_phases/` — ROADMAP + phases + sprint plans (renamed from `_specs_and_plans/`; the name matches the GEN2 **Stages → Phases → Sprints** hierarchy)
- `_status_reports/`, `_documentation/`, `_REFERENCE/` (convention `README.md` + git-ignored `_assets/_screenshots/`) — new standard scaffolds
- `.gitignore` drift fixed: the `.env.example`-swallow bug (`!.env.example`), the `.claude/*` commit-settings-and-hooks convention, `.dev-server.pid`, `.bsync-*`.

`NEW_PROJECT_GUIDE.md` §2/§5 were updated to match, and all template + scaffolder (`bin/`) path references were swept to the new paths.

## Remaining — standardize the ~30 existing repos (ongoing)

There is drift across the fleet (some keep `_research/` at project root, others under `_specs_and_plans/`; some lack `_status_reports/` / `_documentation/`). Bring each existing repo to standard **one at a time**, per **`MIGRATE_ADAPT.md`** (the playbook: the known drift patterns, the **merge-don't-clobber** gotcha for repos that have `_research/` in *both* places, and the internal reference-update sweep) and `NEW_PROJECT_GUIDE.md` §9 (manual; `diff -r` each repo against the template; review each delta with John; no automated sync). **Gates CANON-001.**
