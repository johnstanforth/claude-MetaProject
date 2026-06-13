# LATER-001 — Workflow Lineage Tracking & Hybrid (Deterministic + LLM) Workflow Formalization

- **Captured:** 2026-06-12, MetaProject session (while indexing the new `divia_ai-swarm` / `divialife-*` bootstraps)
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

3. **Choosing the right ancestor for the next bootstrap.** This directly serves the original bootstrapping goal. The documented chain (`aixodev-collabs → tastypantry → sattvasichealth → diviahome-web → legendarymoney-web`) identifies the current tip — which is why `divia_ai-swarm` and `divialife-flutter` correctly cloned from DiviaHome rather than the older `aixodev-collabs` root. Cloning from a stale sibling resurrects already-fixed problems. Lineage makes "which one do I copy from?" a lookup instead of an 8-repo diff.

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

## Possible next actions (for weekly review)

- [ ] Fold Part 1 + Part 2 into `aixodev-workgroups` Phase 00 scoping when that project's research phase opens (it is currently scaffold-only, 5 commits).
- [ ] Inventory which existing workflow steps are secretly deterministic (file-existence gates, length checks, test/lint exit codes) as candidate first targets for the hybrid engine.
- [ ] Decide whether the lineage map itself (which repo forked which, at what point) should become data *inside* the workgroups prototype rather than prose in `_projects/README.md`.
- [ ] Re-assignable: to Claude/Codex agents working within `aixodev-workgroups` once it has an active phase.
