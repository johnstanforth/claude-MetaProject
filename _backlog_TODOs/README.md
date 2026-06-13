# `_backlog_TODOs` — Cross-Project Backlog

Deferred TODO items captured during MetaProject (cross-project) work — ideas, rationale, and future obligations that span multiple projects or don't yet have a clear owning project, recorded here so they survive the end of the conversation that produced them.

## Conventions

- **One file per item:** `LATER-{NNN}-{slug}.md` — `NNN` zero-padded, monotonically increasing, never reused.
- **Write for a cold reader.** Each file must carry enough context (capture date, originating discussion, full rationale) that a future agent or human who wasn't in the originating conversation can act on it.
- **Header fields:** capture date · status · eventual owning project (if known) · related docs.

## Weekly review routine

These items are reviewed on a **weekly cadence**: aggregate related items, refine scope, and when an item becomes focused enough, re-assign it to the agents (Claude / Codex) working within the relevant individual project — typically as input to that project's sprint planning.

Items **graduate** out of this directory by being adopted into a project's own `_specs_and_plans/_backlog/` (NEXT / LATER / SOMEDAY) or directly into a sprint. When that happens, update the LATER file's status with where it went — don't delete it; the trail is the point.

## Relationship to per-project backlogs

Individual projects keep their own `_specs_and_plans/_backlog/` horizons. This directory is **only** for items that (a) span more than one project, (b) belong to a project that doesn't exist yet, or (c) were captured mid-conversation in MetaProject and haven't been triaged anywhere else yet.
