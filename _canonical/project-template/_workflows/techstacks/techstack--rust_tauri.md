# Tech Stack: Rust / Tauri Desktop Application

> Architectural components, skeleton generation instructions, and lessons learned for Rust/Tauri desktop applications. Referenced by `workflow_build_new_project.md`.

## Last Reviewed

| Date | Context | Changes |
|------|---------|---------|
| 2026-05-03 | Placeholder created | Awaiting content from a Rust/Tauri project's Claude instance |

---

## Status: PLACEHOLDER

This document should be written by a Claude instance running within an existing Rust/Tauri project (e.g., `divia-desktop` or similar) that has accumulated:

- Established Cargo workspace layout and conventions
- Tauri configuration patterns (tauri.conf.json, capabilities, permissions)
- Frontend framework integration (Svelte, React, Vue — whichever the source project uses)
- Build tooling and cross-platform compilation patterns
- Testing patterns for both Rust backend and frontend
- Lessons learned from real development (workarounds, gotchas, performance considerations)

### What to Write

Follow the structure of `techstack--python_flask.md`:

1. **Architectural Components Manifest** — the full list of components that need decisions for a Rust/Tauri app. Examples:
   - Rust edition and MSRV
   - Cargo workspace layout (single crate vs. workspace)
   - Tauri version and plugin set
   - Frontend framework and bundler
   - State management (Tauri state, frontend store)
   - Database (SQLite via rusqlite/sqlx, or other)
   - IPC patterns (Tauri commands, events)
   - CSS framework
   - Testing (cargo test, frontend unit tests, Tauri integration tests)
   - Packaging and distribution (DMG, MSI, AppImage, etc.)

2. **Skeleton Generation** — file-by-file tables showing what to generate and how to adapt from the source project

3. **Lessons Learned** — hard-won patterns from real Rust/Tauri development

4. **Debugging** — the stack-specific half of [`../workflow_error_debugging.md`](../workflow_error_debugging.md): the error-category table, common scenarios, and diagnostic commands for this stack. For Rust/Tauri, expect to cover `cargo` build / borrow-checker errors, `cargo test` failures, Tauri IPC/command + permission errors, the frontend console + webview devtools, async runtime (tokio) issues, and packaging/code-signing failures. Mirror the structure of the `## Debugging` section in `techstack--python_quart.md`.

5. **Commands & Validation** — the canonical command set this stack's projects point to from `PROJECT_IDENTITY.md`: build (`cargo build`), the validation suite (`cargo test`, `cargo clippy`, `cargo fmt --check`), dev/run (`cargo tauri dev`), and release/packaging (`cargo tauri build`). Mirror the `## Commands & Validation` section in `techstack--python_quart.md`.

### How to Fill This In

From a Claude Code session in the Rust/Tauri source project:

```
Read _workflows/techstacks/techstack--rust_tauri.md (placeholder)
and _workflows/techstacks/techstack--python_flask.md (reference structure)

Fill in the Rust/Tauri techstack document based on this project's
established patterns, conventions, and lessons learned.
```

The Claude instance in that project has the full context of the Cargo workspace, Tauri config, frontend setup, and development history — it is the authoritative source for this document's content.
