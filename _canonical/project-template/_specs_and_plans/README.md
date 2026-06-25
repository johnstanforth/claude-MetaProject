<!-- TEMPLATE FILE. Replace {{PLACEHOLDER}} values, then delete this line. -->
# {{FULL_PROJECT_NAME}} -- Specs & Plans

> Index page for all specifications, plans, research, and project-management artifacts for the `{{SHORT_NAME}}` project.

## Quick Navigation

| Area | Path | Description |
|------|------|-------------|
| **Roadmap** | [`ROADMAP.md`](ROADMAP.md) | Forward-looking status, phase history, backlog summary |
| **Project identity** | [`../_workflows/PROJECT_IDENTITY.md`](../_workflows/PROJECT_IDENTITY.md) | Single source of truth: name, slug, env prefix, brand, active tech stack |
| **Workflows** | [`../_workflows/`](../_workflows/) | Development workflow guide (primary loop, supporting workflows, conventions) |
| **Backlog** | [`_backlog/`](_backlog/) | Horizon files (NEXT, LATER, SOMEDAY) and the unsorted queue |
| **Research** | [`_research/`](_research/) | Deep-research documents and analysis |
| **Templates** | [`../_workflows/_templates/`](../_workflows/_templates/) | Sprint specs, phase READMEs, collab-group prompts, review prompts |

## Development Phases

| Phase | Name | Status | Directory |
|-------|------|--------|-----------|
| {{STARTING_PHASE}} | Ideation & Research | **PLANNING** (opened {{CREATION_DATE}}) | [`phase_{{STARTING_PHASE}}--ideation_and_research/`](phase_{{STARTING_PHASE}}--ideation_and_research/) |

## The Primary Development Loop

```
New Phase -> Sprint Planning -> Human Review -> Sprint Execution -> Code Review -> Sprint Closeout
```

See [`../_workflows/README.md`](../_workflows/README.md) for the comprehensive workflow guide.

## Git Conventions

```
claudecode/@claude/phase{NN}-sprint{NN}       # Sprint branches
P{NN}-S{NN}-T{NN} Description                  # Sprint task commit
P{NN}-FIX-{num} Description                    # Quick fix commit
```

All numbers (phase, sprint, task) are zero-padded to two digits.

## Authoritative References

- **Project guide:** [`../CLAUDE.md`](../CLAUDE.md)
- **Project identity:** [`../_workflows/PROJECT_IDENTITY.md`](../_workflows/PROJECT_IDENTITY.md) -- the single per-repo source of truth
- **Workflow guide:** [`../_workflows/README.md`](../_workflows/README.md)
