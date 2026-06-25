<!-- TEMPLATE FILE. Replace {{PLACEHOLDER}} values and write the <!-- AGENT: … --> blocks, then delete the AGENT comments and this line. -->
# Phase {{STARTING_PHASE}} -- Decisions (ADRs)

> Architecture Decision Records for {{SHORT_NAME}}. One entry per decision, newest first. Use [`../../_workflows/_templates/DECISION_TEMPLATE.md`](../../_workflows/_templates/DECISION_TEMPLATE.md) for new entries.

## ADR-002: Tech stack + process

**Date:** {{CREATION_DATE}}
**Status:** Accepted

**Context:** <!-- AGENT: why this stack was chosen; relationship to any sibling/"real" project. -->

**Decision:** Created from the MetaProject canonical template (`_canonical/project-template/`). Active stack: {{STACK_ONELINE}} (active techstack doc: [`../../_workflows/{{ACTIVE_TECHSTACK_DOC}}`](../../_workflows/{{ACTIVE_TECHSTACK_DOC}})). The workflow system is the shared, refactored layout: project-agnostic bodies + a single per-repo `PROJECT_IDENTITY.md` + per-stack `techstacks/` docs.

**Consequences:** <!-- AGENT: note any consequences, e.g. validation gate, data-preservation rules. -->

---

## ADR-001: Project name and identity — {{FULL_PROJECT_NAME}}

**Date:** {{CREATION_DATE}}
**Status:** Accepted

**Context:** <!-- AGENT: why this project exists and why it needs distinct operational identifiers. -->

**Decision:** Brand **{{BRAND}}** (corporate entity {{CORP_ENTITY}}). Operational identifiers: repo / short name / config dir `{{SHORT_NAME}}`, env-var prefix `{{ENV_PREFIX}}`, config dir `~/.config/{{SHORT_NAME}}/`, data dir `~/.local/share/{{SHORT_NAME}}/`, package `{{PACKAGE_NAME}}`. The canonical record is [`../../_workflows/PROJECT_IDENTITY.md`](../../_workflows/PROJECT_IDENTITY.md).

**Consequences:** All downstream naming derives from this; identifiers avoid collision with sibling projects on the same machine.
