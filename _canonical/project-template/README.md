<!-- TEMPLATE FILE. Instantiate per _canonical/NEW_PROJECT_GUIDE.md: replace every {{PLACEHOLDER}}, write the <!-- AGENT: … --> blocks, then delete the AGENT comments and this line. -->
# {{FULL_PROJECT_NAME}}

<!-- AGENT: Write a 1–2 paragraph description of {{FULL_PROJECT_NAME}} from the manifest — what it is, who it's for, and its relationship to any "real"/main sibling. -->

See [`CLAUDE.md`](CLAUDE.md) for the full project guide and [`_specs_and_plans/ROADMAP.md`](_specs_and_plans/ROADMAP.md) for status.

## Status

**Phase {{STARTING_PHASE}} (Ideation & Research) — opened {{CREATION_DATE}}.** There is no application code yet. This repository currently holds the development workflow system (`_workflows/`), the specs/backlog scaffold (`_specs_and_plans/`), and the project docs. The application skeleton is scaffolded in a later phase.

## Tech Stack

| Component | Choice |
|-----------|--------|
| Stack | {{STACK_ONELINE}} |
| Package manager | `uv` (or stack equivalent) |

Identity + active stack: [`_workflows/PROJECT_IDENTITY.md`](_workflows/PROJECT_IDENTITY.md). Architecture + commands + debugging: [`{{ACTIVE_TECHSTACK_DOC}}`](_workflows/{{ACTIVE_TECHSTACK_DOC}}).

## Quick Start

The exact commands live in the active techstack doc's **Commands & Validation** section. (Not yet applicable until the app is scaffolded.)

## Repository Layout

```
{{SHORT_NAME}}/
├── CLAUDE.md                 # Project guide (read first)
├── README.md                 # This file
├── LICENSE.md                # License
├── _workflows/               # Workflow system (project-agnostic bodies + PROJECT_IDENTITY.md + techstacks)
├── _specs_and_plans/         # Specs, roadmap, backlog horizons, research
│   ├── README.md
│   ├── ROADMAP.md
│   ├── _backlog/             # NEXT / LATER / SOMEDAY / UNSORTED_QUEUE
│   ├── _research/
│   └── phase_{{STARTING_PHASE}}--ideation_and_research/
└── _REFERENCE/_EXTERNAL/     # Read-only symlinks to sibling projects (git-ignored)
```

## License

<!-- AGENT: One line, e.g. "Proprietary / commercial, closed-source. © {{COPYRIGHT_YEAR}} {{CORP_ENTITY}}. See LICENSE.md." -->
