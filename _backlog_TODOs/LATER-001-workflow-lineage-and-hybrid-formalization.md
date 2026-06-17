# LATER-001 — Workflow Lineage Tracking & Hybrid (Deterministic + LLM) Workflow Formalization

- **Captured:** 2026-06-12, MetaProject session (while indexing the new `divia_ai-agentswarms` / `divialife-*` bootstraps)
- **Updated:** 2026-06-16 — John re-raised the core propagation problem at 20+-project scale and asked to "revisit cross-project workflows"; the new `research-pdf` skill surfaced a third propagation model. See the [2026-06-16 update](#2026-06-16-update--scale-re-framing--the-global-skill-propagation-model) section below.
- **Status:** LATER — awaiting weekly backlog review; not yet assigned to a sprint
- **Eventual owning project:** `aixodev-workgroups` (prototype), ultimately re-merged into the upstream AIXO.Dev Platform web service (`aixodev-web`) per the standard prototype → product convergence pattern
- **Related:** `_projects/README.md` ("Shared workflow lineage", "Prototype → product convergence"); each repo's `_workflows/README.md` "Workflow Updates" changelog; `kingstratvc-web/GIT-BRANCHING.md` (the fork-promotion precedent)

---

## Part 1 — Why tracking workflow lineage/provenance matters after bootstrap

**Origin of the question (John):** the original purpose of copy/clone bootstrapping was simply to initialize new projects cheaply while migrating the hard-won, iteratively-improved lessons encapsulated in the workflow docs. Once a project is set up, does the lineage of where its workflows came from still matter?

**Short answer:** for day-to-day work inside any one project, no — agents follow the local `_workflows/` docs and provenance is invisible. The lineage earns its keep at a handful of specific moments that are near-certain to occur with 24+ projects, and at those moments it is the difference between a cheap lookup and an archaeology dig.

### The five moments where lineage activates

1. **Routing fixes downstream (the "recall" problem).** The workflows are copied, not referenced — vendored code without a package manager. When a workflow instruction is discovered to systematically mislead agents (an ambiguous closeout step, a sprint rule that backfires), that's a bug in *N* projects. Lineage tells you which N and which *version* each has: "DiviaLife forked from DiviaHome *after* rule X was added; TastyPantry forked *before*" determines who needs the patch. Supply-chain teams keep SBOMs for vendored code for exactly this reason — copy-paste without provenance is how orphaned, unpatchable copies happen.

2. **Routing improvements upstream.** The flow is bidirectional. A downstream fork (e.g. `divialife-flutter` adapting the system to Flutter) will learn things that generalize. Lineage identifies the trunk — the "most evolved" copy where improvements should land so the *next* bootstrap inherits them. Without it, every lesson stays siloed in whichever repo learned it, and the accumulated-lessons engine stops compounding.

3. **Choosing the right ancestor for the next bootstrap.** This directly serves the original bootstrapping goal. The documented chain (`aixodev-collabs → tastypantry → sattvasichealth → diviahome-web → legendarymoney-web`) identifies the current tip — which is why `divia_ai-agentswarms` and `divialife-flutter` correctly cloned from DiviaHome rather than the older `aixodev-collabs` root. Cloning from a stale sibling resurrects already-fixed problems. Lineage makes "which one do I copy from?" a lookup instead of an 8-repo diff.

4. **A pointer to lost rationale.** Bootstrapped copies carry the rules but not the scar tissue — the *why* lives in the ancestor's git history and sprint retrospectives. When an agent in a thin new repo hits an ambiguous workflow rule, "this came from DiviaHome" is a one-line citation to a much richer context it can consult instead of guessing.

5. **Raw data for eventual formalization.** The lineage map is the requirements evidence for extracting a real shared artifact: it shows which parts stayed byte-identical across all forks (→ shared core) versus which were adapted per stack (→ per-techstack overlays — the `_workflows/techstacks/` directory shows that overlay structure already emerging organically). See Part 2.

### The promotion precedent

`kingstratvc-web` already executed the endgame of this logic once: it was promoted from "doc-copy lineage" to an actual **git fork** of `diviahome-web`, converting informal provenance into real git ancestry so propagation becomes `git pull upstream` instead of manual diffing (pristine `main` mirror + `kingstrat-main` client delta). Where lineage matters enough, promote it to git ancestry; the README-index lineage note is the poor-man's version for repos where a fork isn't appropriate.

### Recommended fidelity (for now)

Keep it cheap: the one-sentence lineage note in `_projects/README.md` plus each repo's "Workflow Updates" changelog in `_workflows/README.md`. Together they form a poor-man's version vector — enough to compute which updates a sibling is missing. Don't build formal version numbers or sync tooling until a propagation sweep actually hurts.

---

## Part 2 — Formalizing workflows in `aixodev-workgroups`: the hybrid deterministic/probabilistic model

Formalization of the workflow system is **already planned scope** for the experimental `aixodev-workgroups` prototype. Two distinct rationales:

### Rationale A — Abstract-across-projects + versioning

Lift the individually-evolving, per-repo workflow copies into a shared, versioned system (the natural fix for everything in Part 1): one abstraction across projects, per-project instantiation, explicit versions so fixes and improvements propagate deliberately instead of by manual copy.

### Rationale B — Crossing the "deterministic vs. probabilistic code" split

**Current state:** every workflow is implemented as a natural-language LLM prompt — entirely on the *probabilistic* side of the split. A workflow today is a multi-page prompt containing a dozen steps, all entrusted to LLM compliance.

**Target state:** a workflow becomes a set of rules defined within the Python/Flask web app (temporarily in the `aixodev-workgroups` prototype; ultimately re-merged into the upstream AIXO.Dev Platform web service), where each step is explicitly typed as either:

- **LLM step** — a natural-language instruction dispatched to a model, or
- **Deterministic step** — Python-level code: e.g. a filesystem check that an earlier file-write actually happened, that the produced file exceeds N specified chars, that a required doc exists, that a validation suite exited 0.

**Why this matters:** several of the workflow system's hardest invariants are *already deterministic in nature* but currently enforced only by prose an LLM must remember from a long prompt — e.g. the execution-plan gate ("STOP if no approved `xp_` file exists") and the zero-test-failures closeout rule are, today, LLM-compliance hopes; in a hybrid engine they become code-enforced gates that cannot be skipped or hallucinated past.

### Bonus: per-step model tiering

Once steps are individually dispatched by an engine rather than bundled into one giant prompt, each step can be routed to the model/effort tier its difficulty warrants — e.g. **Claude Haiku at medium effort** for simple mechanical steps vs. **Claude Fable at xhigh effort** for hard analysis/design steps. Significant cost and latency efficiency vs. today's one-model-runs-the-whole-prompt approach.

---

## 2026-06-16 update — scale re-framing + the global-skill propagation model

**John's re-framing (2026-06-16).** While creating the `research-pdf` skill, John re-raised this exact theme and asked to capture it: *workflow updates made inside one project have no uniform meta-workflow/process for migrating consistently to all other projects.* The new framing is **scale**: the old "just manually update each project when we migrate" was fine at two or three projects (and at fork/bootstrap time), but it's a materially different requirements scenario at **20+ projects**. This sharpens Part 1 (moments 1–2: routing fixes downstream/upstream) and Rationale A (abstract-across-projects + versioning) from "near-certain to occur eventually" into "actively hurting now."

**New data point — a third propagation model.** The `research-pdf` skill introduced a propagation model the original capture didn't consider. We now have three:

1. **Doc-copy lineage** (vendored `_workflows/` copies + the `_projects/README.md` lineage note) — the Part 1 status quo; cheap to bootstrap, expensive to patch across N forks.
2. **Git-fork promotion** (the `kingstratvc-web` precedent) — convert informal provenance into real git ancestry so propagation is `git pull upstream`; for repos where a fork is appropriate.
3. **Global skill deploy** (NEW, 2026-06-16) — source-of-truth in MetaProject `_skills/<name>/`, deploy-copied once to `~/.claude/skills/<name>/`. A single deploy serves **every** project with **zero per-repo copies**. Best fit for **project-agnostic capabilities** (e.g. PDF generation) that need no per-project customization — it sidesteps the per-repo fan-out problem entirely.

**The honest catch.** Model 3 eliminates per-repo copying but **re-instantiates the migration problem at the source→deploy hop**: the `cp _skills/<name>/ → ~/.claude/skills/<name>/` is itself a remembered manual step (and it must be re-run per machine/environment). So global skills don't *solve* propagation; they *relocate* it from "N repos" to "one deploy step that can still drift." That deploy hop wants the same kind of process (a `deploy-skills` script, a hook, or CI) — see `_skills/README.md`, which documents the manual `cp` as the interim rule.

**A distinction worth formalizing.** The meta-workflow John is asking for needs, as an explicit early step, a **routing decision**: is this shared artifact *project-agnostic* (→ Model 3, global skill, deploy once) or *project-specialized* (→ Model 1/2, vendored copy + lineage or git-fork)? Choosing the right propagation model per artifact is itself part of the missing process.

**Also surfaced today — multi-session coordination.** A live `/tmp` filename collision (this session vs. a concurrent `aixodev-collabs` PDF build sharing `/tmp/build_research_pdf.py`) is the same coordination gap at the session level, and is why John has git-worktrees on this week's agenda. Per-session temp-namespacing + worktrees belong in the same formalization.

---

## 2026-06-16 (cont.) — centralizing the cross-project workflow SOURCE in MetaProject

**Trigger.** While building the `research-pdf` skill (Model 3, global-skill deploy), John proposed pulling the cross-project `_workflows/` *source* into MetaProject and managing it in one place — edit here, deploy out to the 20+ project `_workflows/` — instead of editing each repo's copy. Mid-discussion he recognized this is not a new problem but a direct extension of *this* item (Part 1 routing + Rationale A versioning), and chose to **capture-and-defer** rather than half-build a source dir that this week's graph-DB work will reshape anyway. This section preserves the full context so the LATER-001 working session doesn't lose it.

**Investigation findings (2026-06-16) — the workflows are already converged; the only divergence is instantiation.** Comparing every fork's `_workflows/` (diviahome / legendarymoney / sattvasichealth / aixodev-collabs / tastypantry / kingstrat) with project-name tokens filtered out: the full set (~25 `workflow_*.md` + the `README.md` changelog + `techstacks/`, `_templates/`, `ensemble-collab/`, `EFFICIENCY_RULES*`) is present in every fork with **identical workflow *process* content**, synced to the 2026-06-09 baseline. Every fork difference is **pure per-project instantiation** — project-name tokens (`DIVIAHOME_ENV` vs `KINGSTRATVC_ENV`) and embedded project-*description* prose (diviahome's "household management" vs legendarymoney's "Gen-Z PFM") — **not** workflow improvements. The **only** real process improvement anywhere is **kingstrat's `workflow_research.md`** (the 2026-06-15 lessons: phantom-launch discipline, the hard pre-synthesis gate, Option-B "don't /clear" synthesis, no-soft-wrap) — 471 vs 443 lines ahead of the trunk; the other two kingstrat diffs are only the env-prefix example.

**The key reframe — there is no clean "source" to copy; the source is a *template*.** Because each fork has its name/description baked in, no repo holds a canonical generic version. The true source-of-truth is a **genericized template** with `{{placeholders}}` (e.g. `{{SHORTNAME}}_ENV`, project-description). "Centralize the workflows" therefore *is* "build the templatize-and-deploy mechanism" (Rationale A / Part 2) — the same task — which is why deferring the dir until that mechanism is designed is the correct call, not a punt.

**The seed plan, if/when the dir is built (captured, not executed).** Seed from the **diviahome trunk** baseline (all forks are synced to it) + overlay **kingstrat's `workflow_research.md`** (the lone improvement); then genericize the name/description instantiations into `{{placeholders}}`. The dir also holds the `_workflows/README.md` **revision changelog**, which becomes the central log of workflow revisions going forward. Two candidate layouts were floated: flat `_workflows-src/` (sibling to `_skills/`, no churn) vs. grouped `_sources/{skills,workflows}/` (cleaner taxonomy, but moves the just-created `_skills/`). Undecided — part of the deferred design.

**Where the `{{placeholder}}` values come from — two new sibling backlog items (cross-refs).** The hard part of templatize-and-deploy is knowing *what each `{{var}}` should be per project*. That data already exists, just scattered (UV_Guide, `DOMAIN_*` docs, per-repo `CLAUDE.md`) and not organized for lookup. Two items were filed to converge on it: **(a) kingstrat-adventuregps `_horizon_LATER`** — once the kingstrat graph-DB models the **full inventory of all projects + git-repos** (beyond the 2026-06-15 7-dimensional entity mapping), it becomes the **authoritative lookup** for every per-project substitution value (Claude pulls "what is `{{SHORTNAME}}_ENV` / the description / the repo for project X" from the graph instead of guessing) — the secondary-confirmation data source that makes templatized deployment reliable; **(b) aixodev-projects `_horizon_LATER`** — that prototype (tracking all projects' metadata, merging to `aixodev-web`) predates the graph-DB discussions, so its cross-project-info scope is out of date; revisit to **LEVERAGE, not reinvent**, the kingstrat graph-DB, and host the actual cross-platform *sync/propagation* implementation (deploying shared workflows/skills/templates across the 20+ repos with graph-sourced substitution) there, built on the graph-DB.

**The full migration/dependency chain (2026-06-16, John's "design-hat" refinement — supersedes the loose "kingstrat graph-DB" phrasing above).** The graph-DB's permanent home is **not** kingstrat; kingstrat is the R&D + dogfood site. Accurate flow: **(1)** the **KingStrat spikes** figure out the **graph-DB architecture**; **(2)** import KingStrat's own data (companies / entities / domains — most already in this project's `DOMAIN_*` and `UV_Guide` markdown) into it, **dogfooding + validating** the architecture on real business data (the business requirements *are* the engineering-validation dataset; the running KSVGPS service is the deliverable non-technical staff & investors see); **(3)** **merge upstream → `proto-divia_ai-enterprise`** (same Python/Flask stack → inherits the DB architecture) — the **prototype** of "the Divia.AI Enterprise server," exposing a deliberately-**stable API**. **(4) Branch point (a "DecisionNode" — two *parallel* tracks, NOT sequential):** **Track A (far-future, gated)** = the Rust `divia_ai-enterprise` commercial server, built only *after* a complete prototype exists (the prototype's whole purpose), so it is far off and is the **single permanent optimized home** of the core; **Track B (now, in parallel)** = `aixodev-projects` and `aixodev-web` build directly against the **prototype immediately**, *not* blocked on Track A — the stable API is the contract, so Track A's eventual Rust rewrite is a transparent implementation-swap and clients don't change. **(5)** Consequence — **clean scope via issue-routing:** when `aixodev-web` work (6+ months ongoing) surfaces a server-side issue, it's fixed in `proto-divia_ai-enterprise` (or noted "already fixed in `divia_ai-enterprise`"), never duplicated in the client. `aixodev-projects` still **merges back → `aixodev-web`**; `aixodev-web` carries an **intentional, significant dependency** on the server (much of its task-management + non-technical research-doc functionality is *really best implemented* server-side), not a thin "client implementation" like kingstrat.

**Why it matters (the strategic realization, John 2026-06-16).** Organizing the projects correctly doesn't just cut sync overhead — it lets us **concentrate core-functionality optimization in ONE place** (graph-DB performance, etc., in the Divia.AI Enterprise server) instead of maintaining ~5 separate copies of the same functionality; and it makes the **real business data the engineering's validation set** (entering the actual KingStrat companies / entities / domains *is* the graph-DB acceptance test), so correct engineering and a stakeholder-visible working KSVGPS become the *same* deliverable. It is the same "concentrate where most-effective" principle as the global-skill (Model 3) and workflow-template centralization — now applied to the **product core**, not just the dev-infrastructure.

**Net for the LATER-001 working session.** The three propagation models (doc-copy lineage / git-fork / global-skill) plus this finding point at a concrete v1: a **genericized workflow template set in MetaProject** + a **deploy step that substitutes graph-sourced per-project values** + the **aixodev-projects** prototype as the place that implements the sync. The research-pdf skill is the working precedent for the "edit-source-here, deploy-out" half.

---

## Possible next actions (for weekly review)

- [ ] **(2026-06-16)** Define the **propagation-model routing rule** — project-agnostic capability → global skill (Model 3, deploy once); project-specialized workflow → vendored copy + lineage / git-fork (Model 1/2) — and make "which model?" an explicit step whenever a new shared artifact is created.
- [ ] **(2026-06-16)** Give MetaProject `_skills/` a real **deploy mechanism** (a `deploy-skills` script / hook / CI) so source→`~/.claude/skills/` redeploys can't silently drift, instead of a remembered manual `cp`.
- [ ] **(2026-06-16)** Fold **multi-session hygiene** (git-worktrees + per-session `/tmp` namespacing) into the same formalization — prompted by today's live `/tmp` collision.
- [ ] **(2026-06-16)** When building the workflow-source dir: seed from the diviahome trunk + kingstrat's `workflow_research.md`, genericize name/description into `{{placeholders}}`, and pick the layout (flat `_workflows-src/` vs grouped `_sources/`). Deferred until the templatize-deploy mechanism + the graph-DB substitution source exist.
- [ ] **(2026-06-16)** Track the two sibling items filed today: kingstrat graph-DB as the per-project `{{var}}` lookup source (kingstrat `_horizon_LATER`); aixodev-projects re-scoped to host cross-project sync on the graph-DB (aixodev-projects `_horizon_LATER`).
- [ ] Fold Part 1 + Part 2 into `aixodev-workgroups` Phase 00 scoping when that project's research phase opens (it is currently scaffold-only, 5 commits).
- [ ] Inventory which existing workflow steps are secretly deterministic (file-existence gates, length checks, test/lint exit codes) as candidate first targets for the hybrid engine.
- [ ] Decide whether the lineage map itself (which repo forked which, at what point) should become data *inside* the workgroups prototype rather than prose in `_projects/README.md`.
- [ ] Re-assignable: to Claude/Codex agents working within `aixodev-workgroups` once it has an active phase.
