<!-- TEMPLATE FILE. Instantiate per _canonical/NEW_PROJECT_GUIDE.md: replace every {{PLACEHOLDER}}, write the <!-- AGENT: … --> blocks, then delete the AGENT comments and this line. -->
# Project Identity

> **The single source of truth for everything project-specific in the workflow system.** This is the ONE file you edit per repository. Every `_workflows/*.md` body is project-agnostic and refers back here (and to the active `techstacks/` doc) instead of hardcoding names, slugs, prefixes, or domain context.

## How this file is used

- **Workflow bodies** (`workflow_*.md`, `_templates/*.md`) never name the project. Where they need a concrete value they say "the project's env-var prefix (see `PROJECT_IDENTITY.md`)" or pull a named field below.
- **Prompt templates** that brief other agents (`_templates/COLLAB_PROMPT_*.md`, `EXTERNAL_REVIEW_PROMPT.md`) carry a `{PROJECT_CONTEXT}` placeholder — fill it from the **Project Context block** at the bottom of this file.
- **Per-stack specifics** (commands, debugging error tables, gotchas) live in the active `techstacks/` doc, not here. This file only points at which stack doc is active.

## Syncing across repositories

The workflow bodies (`workflow_*.md`, `_templates/*.md`, `techstacks/*.md`, `README.md`) are designed to be **byte-identical across every project that uses this system**, so an improvement made in the canonical source can be brought into every repo with no per-project merge work. **`PROJECT_IDENTITY.md` is the deliberate exception: it is per-repo and must NOT be propagated.** When you bring revised workflows into a project, keep this file as-is. The canonical source of the bodies is the MetaProject's `_canonical/project-template/` — see its `NEW_PROJECT_GUIDE.md`.

---

## Identity

| # | Field | Value |
|---|-------|-------|
| 1 | **Full project name** | {{FULL_PROJECT_NAME}} |
| 2 | **Short name / repo / config-dir slug** | `{{SHORT_NAME}}` |
| 3 | **Env-var prefix** (screaming snake) | `{{ENV_PREFIX}}` |
| 4 | **One-line description** | {{ONE_LINE_DESCRIPTION}} |
| 5 | **Brand / business** | {{BRAND}} |
| 6 | **Corporate entity** | {{CORP_ENTITY}} |
| 7 | **Config dir** | `~/.config/{{SHORT_NAME}}/` |
| 8 | **Data dir** | `~/.local/share/{{SHORT_NAME}}/` |
| 9 | **Package / module name** | `{{PACKAGE_NAME}}` |
| 10 | **Ecosystem / sibling projects** | {{ECOSYSTEM_SIBLINGS}} |
| 11 | **Starting phase** | Phase {{STARTING_PHASE}} |

## Active tech stack

The authoritative stack reference — architecture, **Commands & Validation**, **Debugging**, and lessons — is the techstack doc named below. This file does **not** duplicate stack commands; it only names the active doc and records any per-project deviations from the stack defaults.

| Field | Value |
|-------|-------|
| **Active techstack doc** | [`{{ACTIVE_TECHSTACK_DOC}}`]({{ACTIVE_TECHSTACK_DOC}}) |
| **Per-project overrides** | {{STACK_OVERRIDES_OR_NONE}} |

## Constants (NOT project-specific — never parameterize)

These are identical across every sibling project and are written directly into the workflow bodies:

- Branch prefix: `claudecode/@claude/...` (`@claude` is hardcoded)
- Commit prefix: `P{NN}-S{NN}-T{NN}` (sprint task) / `P{NN}-FIX-{num}` (quick fix)
- Sprint doc naming: `sp_{NN}--{slug}.md` (what/why) + `xp_{NN}--{slug}.md` (how)

---

## Project Context block

> Paste this (or a trimmed version) wherever a workflow or prompt template asks for `{PROJECT_CONTEXT}`. It is the canonical, human-readable description of the project for briefing other agents.

<!-- AGENT: Write 3–6 sentences describing this project for other agents: what it is, who it's for, its relationship to sibling/"real" projects, and its tech stack. Derive from the manifest. -->
