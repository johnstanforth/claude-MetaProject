# Workflow: Adapt New Project From Clone (Reset-Based)

> Turn a freshly-rsynced copy of a sibling project into a clean new project — swap the identity file, reset stale content, re-point, commit. The third member of the project-creation family, alongside `workflow_bootstrap_project.md` (pull, blank target) and `workflow_build_new_project.md` (push, generated skeleton).

## Quick Reference

| Item | Value |
|------|-------|
| Trigger | You `rsync`/`cp`'d a complete sibling project into a new directory and want to repurpose it as a distinct new project |
| Input | A directory that is a full copy of a source project (workflows + specs + CLAUDE.md + README + content), already on disk |
| Output | The same directory, re-identified to the new project: identity file swapped, stale content reset, references re-pointed, a clean first commit |
| Mode | Normal Claude Code (interactive), solo |
| Time | 15-30 minutes (no copying to do — the time is all in *resetting* content and writing one identity file) |

---

## 1. When to Use This (vs. the other two)

| Your situation | Workflow |
|----------------|----------|
| New project dir is **empty**; you want to *pull* the workflow system in from a source and adapt it | `workflow_bootstrap_project.md` |
| You are **inside the source project** and want to *generate* a new sibling with an architectural discussion + fresh skeleton | `workflow_build_new_project.md` |
| You **already rsync'd/copied a whole sibling project** into the new dir and want to repurpose it in place | **This workflow** |

The defining trait: **nothing needs to be copied — everything is already here.** The source project's files, content, identity, and (possibly) git history are all sitting in the target directory. The work is not *assembly*; it is *re-identification and cleanup*.

---

## 2. The Core Mental Model: This Is a RESET, Not a Copy

The bootstrap and build workflows both *add* the right things to a clean space, so their dominant failure mode is **omission** — forgetting to copy something needed. Both carry long "What NOT to Copy" lists.

Clone-adapt has the **inverse risk profile.** Everything — including the things bootstrap tells you *not* to copy — is already present, populated with the *previous project's* identity and content. The dominant failure mode here is **residue**: a stale name, a backlog item from the old domain, a ROADMAP describing the wrong product, a self-referential reference symlink, or the source project's git history. Treat the clone as guilty until proven adapted.

**The payoff of a refactored workflow system:** once a project's workflow bodies are project-agnostic and all identity lives in a single `_workflows/PROJECT_IDENTITY.md` (see `PROJECT_IDENTITY.md`), the identity half of this workflow collapses to **replacing one file**. The bulk of the remaining work is resetting the project's *content* docs.

---

## 3. Prerequisites

- [ ] The new directory contains a complete copy of a source project (verify `CLAUDE.md`, `_workflows/`, `_specs_and_plans/` are present and currently describe the *source* project).
- [ ] You know which source project it was cloned from (needed for the residue grep and to recognize what's stale).
- [ ] You have the new project's identity ready, or are prepared to gather it in Step 4.
- [ ] Decide whether the new project keeps the clone's **tech stack** (Step 7 stays a near-no-op) or a **different** one (Step 7 points at a different techstack doc).

---

## 4. Write the New `PROJECT_IDENTITY.md`

Everything project-specific is driven by one file. Open the clone's `_workflows/PROJECT_IDENTITY.md` (it still holds the *source* project's values) and rewrite every field for the new project: full name, short-name/slug, env-var prefix, one-line description, brand/entity, config + data dirs, package name, ecosystem siblings, active techstack doc, validation commands, starting phase, and the **Project Context block** at the bottom.

If any identity field is unknown, **STOP and ask the human.** A wrong value here propagates into every prompt template that pulls `{PROJECT_CONTEXT}`.

This single file is the entire identity surface. The workflow bodies (`workflow_*.md`, `_templates/*.md`, `techstacks/*.md`, `README.md`) are project-agnostic and read from it — you do **not** edit them per project.

---

## 5. Map the Blast Radius

Confirm the identity really is confined to `PROJECT_IDENTITY.md` + the content docs, and find any residue to reset.

```bash
cd /path/to/new-project
SRC_SLUG="fracrealhomes-dailyspikedriver"      # the source project's slug
SRC_PREFIX="FRACREALHOMES_DSD_"                 # the source env-var prefix

# Every file still carrying the source identity, repo-wide:
grep -rilE "${SRC_SLUG}|${SRC_PREFIX}|<source brand words>" . \
  --exclude-dir=.git --exclude-dir=_REFERENCE | sort

# In a fully-refactored clone, the only _workflows hit should be PROJECT_IDENTITY.md.
grep -rilE "${SRC_SLUG}|${SRC_PREFIX}" _workflows/ | grep -v PROJECT_IDENTITY.md
```

Hits fall into three zones, handled differently below:

| Zone | Examples | How it's handled |
|------|----------|------------------|
| **A. Identity file** | `_workflows/PROJECT_IDENTITY.md` | Step 4 — rewritten for the new project |
| **B. Content docs** | `CLAUDE.md`, `README.md`, `LICENSE.md`, `_specs_and_plans/ROADMAP.md`, `_specs_and_plans/README.md`, phase dirs, backlog horizons, `DECISIONS.md` | Step 6 — *reset*: the old content is wrong for the new project, not just mis-named |
| **C. Non-text residue** | `_REFERENCE/_EXTERNAL/` symlinks, a carried-over `.git/`, `instance/`/data dirs, `.env`, OAuth secrets, `*.sqlite3` | Steps 8-9 — re-point, re-init, or delete |

**If `_workflows/` bodies still hold scattered identity** (the clone came from an *older, pre-refactor* project), run the legacy substitution pass from `workflow_bootstrap_project.md` § 7 first, then extract the values into `PROJECT_IDENTITY.md`. Going forward, clones of refactored projects skip this entirely.

---

## 6. Reset Project-Specific CONTENT (the step bootstrap never has to do)

These files were copied wholesale and describe the **old project's work**. Renaming isn't enough — the content itself is wrong. Reset each to a new-project baseline.

| File / dir | Action |
|------------|--------|
| `CLAUDE.md` | Rewrite the Project Overview, naming table, tech-stack notes, and known-gotchas for the new project. Keep structural sections and house rules (git rules, reasoning rule, doc conventions). Most important single file. |
| `README.md` (project root) | Rewrite entirely (name, description, quick-start, status). |
| `LICENSE.md` | Update the entity/copyright line if the owning entity differs. |
| `_specs_and_plans/ROADMAP.md` | Reset to a fresh roadmap: new name, Phase 00/01, zero sprints, empty history, backlog summary all zeros. |
| `_specs_and_plans/README.md` | Re-identify the specs index; keep the navigation structure. |
| `_specs_and_plans/phase_00--*/` (and any `phase_NN`) | Reset Phase 00's `README.md`/`DECISIONS.md` from `_workflows/_templates/`; delete later phase dirs outright. |
| `_specs_and_plans/_backlog/_horizon_*.md`, `_UNSORTED_QUEUE.md` | Empty them — the clone's items belong to the old domain. Keep the header format, drop the items. |
| `_specs_and_plans/_research/` | Delete inherited research; keep the empty dir. |
| Any `sp_*.md` / `xp_*.md`, `PRODUCT_AND_NAMING.md`, `reference--*.md` | Delete — each project writes its own. |

Rule of thumb: **if the file documents *what the project is or has done*, reset it; if it documents *how we work*, it's already generic — leave it.**

---

## 7. Confirm the Active Tech Stack

If the new project keeps the clone's stack, this is just a check — `PROJECT_IDENTITY.md` already names the active `techstacks/` doc and the validation commands. If the stack differs, point `PROJECT_IDENTITY.md` at the correct `techstacks/techstack--*.md` (the per-stack architecture + **Debugging** section live there, not in the generic workflow bodies). All `techstacks/*.md` ship with the clone, so the right one is already present.

---

## 8. Re-point or Remove `_REFERENCE/` Symlinks

A clone usually drags the source's reference symlinks along — including a **self-referential one** pointing back at the source (e.g. `_REFERENCE/_EXTERNAL/{source-slug} -> .../{source-slug}`). These are git-ignored but misleading.

```bash
ls -la _REFERENCE/_EXTERNAL/      # inventory the symlinks
```

Keep the ones the new project genuinely references; **delete the self-referential one** and any that don't apply; add new-project-relevant ones. (Reference symlinks are READ-ONLY targets — never edit through them.)

---

## 9. Reset Git History

```bash
git log --oneline 2>&1 | head -3   # "no commits yet" → fresh; otherwise inherited history
git remote -v                       # MUST be empty — a clone must never inherit the source's remote
```

- **No history** (fresh `git init`): good — proceed to the first commit.
- **Inherited history**: with the human's confirmation, `rm -rf .git && git init` to drop the source's history (or keep it only if the human wants the lineage). Never keep an inherited remote (`git remote remove <name>`). House rule: local-only; never push.

---

## 10. Verify

- [ ] `grep -rilE "{source identity tokens}" . --exclude-dir=.git --exclude-dir=_REFERENCE` returns only `PROJECT_IDENTITY.md`-sourced content and intentional provenance (changelogs/exemplars).
- [ ] `_workflows/PROJECT_IDENTITY.md` is fully rewritten for the new project; no `_workflows/` body still names the source.
- [ ] `CLAUDE.md`, project `README.md`, `ROADMAP.md`, specs `README.md` all describe the new project.
- [ ] Backlog horizons + `_UNSORTED_QUEUE.md` are empty (header-only); Phase 00 reset from templates; no source `sp_`/`xp_`/research left.
- [ ] `PROJECT_IDENTITY.md` points at the correct active `techstacks/` doc; validation commands match the stack.
- [ ] `_REFERENCE/_EXTERNAL/` has no self-referential or irrelevant symlinks; no inherited git remote.
- [ ] A clean first commit is ready.

---

## 11. Initial Commits

There's no "verbatim copy" baseline to preserve (the copy happened outside git), so split along *reset* vs *re-identify*:

```bash
git add -A && git commit -m "Import sibling-project clone as new-project baseline"   # optional snapshot of as-cloned state
git commit -m "Reset project content for {new-slug} (CLAUDE.md, README, ROADMAP, specs, backlog)"
git commit -m "Re-identify: rewrite PROJECT_IDENTITY.md; re-point references"
```

If you dropped inherited history in Step 9, the first commit *is* the new project's root commit. Per house rules: local commits only, no `git push`, no `Co-Authored-By` trailers, no `--amend`/force without approval.

---

## 12. Post-Adaptation: First Real Work

Validate the adaptation by starting the new project's Phase 00/01 immediately via `workflow_new_phase.md` → `workflow_start_new_sprint.md`. Anything still reading as the old project surfaces fast — fix it in place. If the workflow system is shared, log notable fixes in the README "Workflow Updates" changelog.

---

## 13. Quick Command (for invoking this workflow)

```
Read _workflows/workflow_adapt_project_from_clone.md and follow it to re-identify
this rsync'd clone as a new project.

Cloned from: {source-slug}
New project: rewrite _workflows/PROJECT_IDENTITY.md with —
  - Full name / slug / env prefix / one-line description
  - Brand + corporate entity / ecosystem siblings (or "none")
  - Active techstack doc (same as clone | different: ...)
  - Starting phase (00 | 01)
```
