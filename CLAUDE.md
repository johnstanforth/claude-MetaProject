# CLAUDE.md — MetaProject

## Project Overview

**MetaProject** (`~/Code/_claude.MetaProject`) is a lightweight **cross-project coordination workspace**. It exists for tasks that span multiple projects, multiple git repositories, or that involve changes to the projects themselves — i.e. work that sits *outside* the scope of any single project's intra-repository development.

The `_projects/` subdirectory holds **symlinks to the real working copies** of every managed project. `_projects/README.md` is a generated index of those projects (descriptions, stacks, statuses, and cross-project relationships); regenerate it when symlinks are added/removed or a project's README changes materially.

This is **not** a build/application project — it has no application code, tests, or sprint pipeline of its own.

## Repository Layout

```
_claude.MetaProject/
├── CLAUDE.md              # This file — coordination rules for AI agents
├── README.md             # MetaProject overview
└── _projects/
    ├── README.md         # Generated index of all managed projects
    └── <symlinks…>       # Editable symlinks to each managed repo's working copy
```

## Working Across Projects (the symlinked repos)

- The `_projects/*` symlinks are **editable working copies** of other git repositories — MetaProject's purpose includes changing the projects themselves.
- **Each symlinked project is its own git repo with its own conventions.** Before changing files in one, read that project's own `CLAUDE.md` and follow its rules.
- When a task changes files inside a symlinked project, **commit those changes inside that sub-repo** (not in MetaProject), following that project's git rules — including local-only-by-default and no Co-Authored-By lines.
- Keep MetaProject's own files (this `CLAUDE.md`, `README.md`, the `_projects/` index) committed in the **MetaProject** repo.

## Git Rules (this repo)

MetaProject uses a **lightweight flow** — no sprint/phase pipeline, no `sp_`/`xp_` execution-plan gate, no `P{NN}-S{NN}-T{NN}` commit prefixes, no per-task branch requirement. Plain descriptive commits directly on `main` are fine.

- **Always commit locally after completing work.** At the end of every task or logical unit of work, stage and commit all modified and new files with a descriptive message. Do NOT leave uncommitted changes.
- **NEVER git push** unless John explicitly asks. All commits are local-only by default.
- **Never amend** previous commits unless explicitly asked.
- **Never force-push** or use destructive git operations without explicit permission.
- **No Co-Authored-By lines.** Do not add `Co-Authored-By` trailers to commit messages. The git author field is sufficient.
- **Cross-repo commits:** when committing inside a symlinked project, follow *that* repo's git rules, not these.

## Efficiency Rules

- **Don't duplicate subagent work.** Don't redo (in the main thread or another agent) what a subagent has already been dispatched to do.
- **Wait for subagents before acting on their topic.** Let a dispatched subagent finish before taking dependent action on what it's investigating.
- **Don't re-read files already in context.** Reuse what's already been read this session.
- **Stop and ask rather than guess-and-redo.** When a requirement is unclear, ask John rather than guessing and risking rework.

## Agent Rules

- **Always use Opus** for research and analysis subagents. Never use Sonnet for research tasks (documented factual errors in prior projects).

## Documentation Conventions (cross-project)

**No soft-wrapped lines in Markdown.** Write prose with NO manual/soft line-wrapping inside paragraphs: each paragraph and each list item is ONE unbroken line that soft-wraps in the renderer. Insert a newline ONLY at real semantic boundaries — a blank line between paragraphs, list items, headings, table rows, and fenced code blocks. Do NOT hard-wrap prose at a fixed column width (e.g. ~80 cols). Rationale: a one-sentence edit changes one line rather than re-flowing a block, so diffs stay clean and reviewable, and the rendered output is identical either way. This applies to all reports, research analyses, specs, briefs, and docs (including subagent output) — across this MetaProject **and** every managed sub-repo. When editing an already-soft-wrapped doc, apply the rule to new/rewritten content; do not reflow the whole file as a side effect. Each managed repo should also carry this rule in its own `CLAUDE.md` so subagents scoped to that repo inherit it.

## CRITICAL: Reason Step by Step

Before answering any question, reason step by step. Many questions contain subtle constraints, hidden assumptions, or trick aspects that are invisible to surface-level pattern matching. Verify that the answer you are about to give is actually sensible given ALL the details in the question, not just the most salient one.
