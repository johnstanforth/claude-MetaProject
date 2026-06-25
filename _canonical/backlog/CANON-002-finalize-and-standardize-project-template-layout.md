# CANON-002 — Finalize & standardize the project-template directory structure

- **Captured:** 2026-06-25, while working in `txfrcloud-protomolecule`
- **Status:** OPEN — John reviewing with the team before locking the standard
- **Related:** `_canonical/project-template/`; `_canonical/NEW_PROJECT_GUIDE.md` §5 (open layout questions); `../_backlog_TODOs/LATER-001`

The canonical `project-template/` ships a **v0** directory layout. It needs to be finalized (with John + team), and then existing repos brought to the standard — there is already drift across the ~30 repos (e.g. some keep `_research/` at the project root, others at `_specs_and_plans/_research/`).

**Open layout questions to settle in `_canonical/project-template/`:**
- `_research/` location — project root vs. `_specs_and_plans/_research/` (John has floated moving it to the project root).
- Any other directory-placement conventions that differ across existing repos (surface them as found).

**Process:** decide each question by **editing `_canonical/project-template/`** (the single definition of the standard), then run a **manual, one-repo-at-a-time** pass per `NEW_PROJECT_GUIDE.md` §9 — `diff -r` each repo's tree against the template, review the delta with John, apply by hand. No automated sync. It's a one-time fix; everything created from the template onward is already conformant. **Gates CANON-001.**
