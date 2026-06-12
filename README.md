# MetaProject

A lightweight **cross-project coordination workspace** for managing John's other Claude Code projects. Use it for tasks that span multiple projects, multiple git repositories, or that involve changes to the projects themselves — work that sits outside the scope of any single project's intra-repository development.

## Layout

- **`_projects/`** — symlinks to the editable working copies of every managed project.
  - **`_projects/README.md`** — generated index of all projects (descriptions, stacks, statuses, and cross-project relationships).
- **`CLAUDE.md`** — coordination rules for AI agents working in this repo.

## Notes

- Each symlinked project is its own git repository with its own conventions — changes made there are committed in that sub-repo, following its own rules.
- See [`CLAUDE.md`](CLAUDE.md) for the full working rules.
