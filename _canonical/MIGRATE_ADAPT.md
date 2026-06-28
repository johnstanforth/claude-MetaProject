# Migrating an Existing Repo to the Canonical Standard

> **For a future Claude instance bringing a pre-existing, drifted sibling repo up to the current `_canonical/project-template/` standard.** Read this FIRST — before you start diffing — then `NEW_PROJECT_GUIDE.md` §9. This doc front-loads the *why* and the *known drift patterns* so the migration is a **guided correction, not a blind delta-hunt**. It pairs with `NEW_PROJECT_GUIDE.md` (which covers creating *new* projects); this one covers reconciling *existing* ones.

## 1. Why this exists — the drift story

The shared development system historically propagated by a **serial clone chain** (`aixodev-collabs → … → aixodev-aixovault → fracrealhomes-dailyspikedriver → …`). Every clone was a point-in-time snapshot that immediately began to **drift**, and cloning a *new* project from a sibling inherited that sibling's mid-flight, drifted state. The canonical template (`_canonical/project-template/`) inverts this — it is the single always-clean source, pushed *out* — but the ~30 repos that predate it still carry accumulated drift. This doc is the playbook for reconciling them, **one repo at a time, with John reviewing each delta** (no bulk/automated push — `NEW_PROJECT_GUIDE` §8/§9).

The key mindset: a straight `diff -r` against the template *will* surface the differences, but without the context below it reads as "a pile of random mismatches." The drift is not random — it has known shapes, listed in §3. Correct the known shapes first; then triage whatever remains.

## 2. The structural change this doc primarily captures (the GEN2 layout, 2026-06)

The largest recent change split the overloaded `_specs_and_plans/` grab-bag into **three root-level directories**, to match the GEN2 model and stop one directory from meaning three different things:

| New (canonical) | Was | Holds |
|---|---|---|
| `_backlog/` | `_specs_and_plans/_backlog/` | unscheduled ideas (NEXT / LATER / SOMEDAY / UNSORTED horizons) |
| `_research/` | `_specs_and_plans/_research/` | investigations, analyses, syntheses |
| `_stages_and_phases/` | `_specs_and_plans/` (renamed) | the scheduled execution plan — ROADMAP + phases + sprint plans; the name ties to the GEN2 **Stages → Phases → Sprints** hierarchy |

Plus three standard scaffolds that several repos had evolved independently but the template lacked: **`_status_reports/`** (reviews/audits), **`_documentation/`** (product docs), and **`_REFERENCE/`** (with `README.md` + a git-ignored `_assets/_screenshots/`).

## 3. Known drift patterns — the checklist (correct these first)

This is the high-value part: the specific mismatches observed across the fleet, so you fix the *known* ones before hunting unknowns.

| Pattern you may find | Seen in | Correct to |
|---|---|---|
| `_research/` at **project root** | aixodev-web | **keep** — root `_research/` is the new standard |
| `_research/` under `_specs_and_plans/` | kingstrat, fracrealhomes, txfrcloud-protomolecule | **move** to root `_research/` |
| ⚠️ **`_research/` in BOTH places** (a drift artifact) | suspected on some repos — *verify per repo* | **MERGE, do not clobber** — move the `_specs_and_plans/_research/` contents into the root `_research/`, reconcile any duplicate filenames by inspection, then delete the now-empty old dir. A blind `git mv _specs_and_plans/_research _research` **fails or clobbers** when the target already exists. |
| `_specs_and_plans/` (consolidated) | kingstrat, fracrealhomes, txfrcloud-protomolecule | **rename** → `_stages_and_phases/`, and pull `_backlog/` + `_research/` out to root |
| `_backlog/` under `_specs_and_plans/` | most | **move** to root `_backlog/` |
| no `_status_reports/` | kingstrat, fracrealhomes | **add** the scaffold |
| `_status_reports/` already present | aixodev-web, aixodev-aixocode, divia_ai-professional | **keep** (now standard) |
| lowercase `documentation/` | aixodev-web | **rename** → `_documentation/` |
| `_documentation/` already present | aixodev-aixocode, divia_ai-professional | **keep** |
| no `_REFERENCE/README.md` | most | **add** the convention README + `_assets/_screenshots/` scaffold |
| `_REFERENCE/PRODUCT_DEVELOPMENT/` (committed reference content) | aixodev-web | **keep** — committed named subdirs under `_REFERENCE/` are correct (only `_EXTERNAL/` and `_assets/` are git-ignored) |

## 4. gitignore drift (reconcile every repo's `.gitignore`)

Specific generic items that drifted *out* of newer repos / the old template and must be restored (observed by comparing `aixodev-web`'s gitignore against the drifted template):

- **`!.env.example`** (and `!.env.staging.example`) — a real bug: a bare `.env.*` rule **silently swallows the committed example config**. Ensure `.env.example` is committable while `.env` (real secrets) stays ignored.
- **`.claude/*` + `!.claude/settings.json` + `!.claude/hooks/`** — commit project-level Claude Code config, ignore user-local.
- **`.dev-server.pid`** and **`.bsync-*`** — the house dev-server PID file and bsync snapshots.
- **`_REFERENCE/_assets`** and **`_REFERENCE/_EXTERNAL`** ignored.

Leave **stack-specific** ignores (Tailwind `output.css`, `node_modules/`, `app/static/uploads/*`, `.playwright-cli/`, app `data/`) in the **per-stack** `.gitignore` tailoring — they do not belong in the generic baseline.

## 5. The reference-update gotcha (do not skip)

**Moving or renaming a directory does NOT update the path references inside the repo's docs and workflows.** After relocating, sweep for stale references:

```
grep -rn '_specs_and_plans' .
# → rewrite to: _research/ · _backlog/ · _stages_and_phases/<README|ROADMAP|phase_*>
```

When the canonical template itself was restructured, it carried **~180** such references across ~25 files; every downstream repo will have its own set. Update them or the workflows will point at directories that no longer exist. Don't forget `CLAUDE.md` ("Key File Locations"), `_workflows/PROJECT_IDENTITY.md`, and the workflow bodies.

## 6. The procedure (one repo at a time)

1. **Read this doc + `NEW_PROJECT_GUIDE` §9 first** — get up to speed on the principles before touching anything.
2. `diff -r _canonical/project-template <repo>/` excluding the genuinely-per-project files (`_workflows/PROJECT_IDENTITY.md`, and the bespoke `CLAUDE.md` / `README.md`).
3. **Walk the §3 checklist first** (the known patterns), then triage the remaining deltas.
4. **Relocate dirs — merge where the target already exists** (the both-places case, §3); never blind-clobber. `git mv` is fine only when the target is absent.
5. **Sweep references** (§5).
6. **Reconcile `.gitignore`** (§4).
7. **Add missing scaffolds** (`_status_reports/`, `_documentation/`, `_REFERENCE/README.md`, `_REFERENCE/_assets/_screenshots/`).
8. **Validate** — the techstack's test/lint suite stays green; nothing references a moved dir (`grep` returns clean).
9. **Review the full delta with John before committing** — manual, one-at-a-time, his explicit constraint.

## 7. What NOT to do

- **No bulk / automated push** across repos (`NEW_PROJECT_GUIDE` §8). One repo, reviewed, at a time.
- **Don't blind-`git mv` a directory whose target already exists** (the both-places drift) — you will error or clobber. Merge the contents.
- **Don't hand-edit `_workflows/` *body* files** in the downstream repo to fix drift — body changes happen in the canonical and propagate (`NEW_PROJECT_GUIDE` §9). In a downstream repo you reconcile only *layout*, *identity* (`PROJECT_IDENTITY.md`), *reference material*, and `.gitignore`.

---

*This doc captures the legacy/migration context as of the 2026-06 GEN2 layout change. When a future layout decision lands, update `_canonical/project-template/` (the single definition of the standard) and refresh §2/§3 here.*
