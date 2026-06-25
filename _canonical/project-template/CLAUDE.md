<!-- TEMPLATE FILE. Instantiate per _canonical/NEW_PROJECT_GUIDE.md: replace every {{PLACEHOLDER}}, write the <!-- AGENT: … --> blocks, then delete the AGENT comments and this line. -->
# CLAUDE.md — {{FULL_PROJECT_NAME}} Guide

## Project Overview

<!-- AGENT: Write the project overview from the manifest — what {{FULL_PROJECT_NAME}} is, who it's for, its domain, and (if applicable) its relationship to a "real"/main sibling Build-Line. Include the naming line: short name / repo / config dir `{{SHORT_NAME}}`; env prefix `{{ENV_PREFIX}}`; package `{{PACKAGE_NAME}}`. Keep the structure/tone of a sibling project's CLAUDE.md Project Overview. -->

## CRITICAL: Reason Step by Step

Before answering any question, reason step by step. Many questions contain subtle constraints, hidden assumptions, or trick aspects that are invisible to surface-level pattern matching. Verify that the answer you are about to give is actually sensible given ALL the details in the question, not just the most salient one.

## Tech Stack

The single source of truth for this project's identity and active stack is [`_workflows/PROJECT_IDENTITY.md`](_workflows/PROJECT_IDENTITY.md); the authoritative stack reference (architecture, **Commands & Validation**, **Debugging**, lessons) is [`{{ACTIVE_TECHSTACK_DOC}}`](_workflows/{{ACTIVE_TECHSTACK_DOC}}).

| Component | Choice |
|-----------|--------|
| **Stack** | {{STACK_ONELINE}} |
| **Package manager** | `uv` (or the stack equivalent) |
| **Tests / lint** | see the active techstack doc's **Commands & Validation** section |
| **Platforms** | Linux, macOS |

<!-- AGENT: If the project has stack specifics worth surfacing here (e.g. "never block the event loop" for async, or a key architectural rule), add a short paragraph. Otherwise this section can stay minimal and defer to the techstack doc. -->

## Product & Naming

| Context | Value |
|---------|-------|
| Corporate entity | {{CORP_ENTITY}} |
| Business / service / brand | {{BRAND}} |
| This project | {{FULL_PROJECT_NAME}} |
| Short name / repo / config dir | `{{SHORT_NAME}}` |
| Env-var prefix (screaming snake) | `{{ENV_PREFIX}}` |
| Package / module name | `{{PACKAGE_NAME}}` |
| Config directory | `~/.config/{{SHORT_NAME}}/` |
| Data directory | `~/.local/share/{{SHORT_NAME}}/` |
| Ecosystem / siblings | {{ECOSYSTEM_SIBLINGS}} |

## License

<!-- AGENT: One line stating the license intent (e.g. "Proprietary / commercial, closed-source — © {{COPYRIGHT_YEAR}} {{CORP_ENTITY}}."). See LICENSE.md. -->

## Development Workflows

This project's `_workflows/` system is the shared, project-agnostic workflow system; all per-project identity lives in [`_workflows/PROJECT_IDENTITY.md`](_workflows/PROJECT_IDENTITY.md) (the one file edited per repo), and all per-stack specifics (commands, debugging) live in the active `techstacks/` doc. The comprehensive guide is [`_workflows/README.md`](_workflows/README.md); the specs index is [`_specs_and_plans/README.md`](_specs_and_plans/README.md). The canonical source of the workflow bodies is the MetaProject's `_canonical/project-template/`.

| Phase | Name | Status | Directory |
|-------|------|--------|-----------|
| {{STARTING_PHASE}} | Ideation & Research | **PLANNING** (opened {{CREATION_DATE}}) | `_specs_and_plans/phase_{{STARTING_PHASE}}--ideation_and_research/` |

**Primary loop:** New Phase → Sprint Planning → Human Review → Sprint Execution → Code Review → Sprint Closeout. The `sp_` says "what and why"; the `xp_` says "how, exactly" and is the contract. **Playground caveat (personal/experimental Build-Lines):** use as much or as little of this ceremony as a piece of work warrants — a quick spike does not need a full `sp_`/`xp_` pair, but anything substantial should still produce one for clarity and resumability.

### Branch Naming

```
claudecode/@claude/phase{NN}-sprint{NN}       # Sprint branches
claudecode/research/@claude/{slug}            # Research branches
```

### Commit Prefix

```
P{NN}-S{NN}-T{NN} Description
```

For work outside a formal sprint, use descriptive messages without the prefix.

## Git Rules

- **Always commit locally after completing work.** At the end of every task or logical unit of work, stage and commit all modified and new files with a descriptive message. Do NOT leave uncommitted changes.
- **NEVER interact with remote git servers.** No `git push`, `git pull`, `git fetch`, `git remote add`, or `gh` commands. All git operations are strictly local. If John wants a remote, he will set it up manually.
- **Never amend** previous commits unless explicitly asked. **Never force-push** or use destructive git operations without explicit permission.
- **No `Co-Authored-By` lines.** The git author field is sufficient.
- **Create the sprint branch BEFORE any planning.** All sprint work (spec, plan, research, code) lives on the sprint branch.
- **Execution-plan gate (for formal sprints):** Sprint implementation should not begin without an approved `xp_`. For informal spikes this is relaxed — but capture what you learned in the backlog/ROADMAP afterward.
- **Zero test failures:** Every sprint must leave the validation suite (the active techstack's **Commands & Validation**) with ZERO failures. There is no such thing as a "pre-existing failure."
- **Clean working tree:** Every sprint ends with a clean working tree (commit ALL files, including spec/plan updates).

## Agent Rules

- **Always use Opus** for research and analysis subagents. Never use Sonnet for research tasks (documented factual errors in prior projects).
- **Reference projects are READ-ONLY.** `_REFERENCE/_EXTERNAL/` holds git-ignored symlinks to actively-developed sibling projects. Read freely but **NEVER** edit files under any reference symlink.
- **When uncertain, ask.** A wrong guess still costs time — stop and ask John rather than guess-and-redo.

## Documentation Conventions

**No soft-wrapped lines in Markdown** (applies to all reports, research, specs, briefs, and docs — including subagent output). Write prose with NO manual/soft line-wrapping inside paragraphs: each paragraph and list item is ONE unbroken line that soft-wraps in the renderer. Insert a newline ONLY at real semantic boundaries — a blank line between paragraphs, list items, headings, table rows, and fenced code blocks. Rationale: a one-sentence edit changes one line (not a re-flowed block), so diffs stay clean. When editing a doc that is already soft-wrapped, do not reflow it wholesale; apply the rule to new/rewritten content. (Cross-project convention shared across John's repos. Note: the inherited collab-prompt templates in `_workflows/_templates/` are intentionally hard-wrapped for terminal paste — that is a deliberate exception.)

## Key File Locations

| Purpose | Path |
|---------|------|
| Project overview / product spec | `README.md` |
| **Project identity (single source of truth)** | `_workflows/PROJECT_IDENTITY.md` |
| Specs & plans index | `_specs_and_plans/README.md` |
| Roadmap | `_specs_and_plans/ROADMAP.md` |
| Backlog horizons | `_specs_and_plans/_backlog/` (NEXT, LATER, SOMEDAY, UNSORTED_QUEUE) |
| Research archive | `_specs_and_plans/_research/` |
| Workflows guide | `_workflows/README.md` |
| Active tech-stack reference | `_workflows/{{ACTIVE_TECHSTACK_DOC}}` |
| Reference projects (read-only) | `_REFERENCE/_EXTERNAL/` (git-ignored symlinks) |

## Known Gotchas

(None captured yet. Add hard-won lessons here as they are discovered.)
