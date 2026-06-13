# Product — aixodev-projects

> Began as a project-tracker prototype; its center of gravity is now a **sophisticated design-theme
> management system** — DB-as-source-of-truth for design tokens, with bidirectional industry-standard
> interchange and framework-native CSS output. Destined to merge into `aixodev-web`.

- **Repo:** `aixodev-projects` · **Umbrella:** AIXO.Dev · **License:** Proprietary (`LicenseRef-Proprietary`).
- **Status:** 🟢 Phase 01 complete; **Phase 02 (Theme Management) complete** (13 sprints, 912 tests, ruff clean). Most mature of the AIXO.Dev prototypes. Flask · SQLAlchemy · SQLite (Bootstrap 5 CDN + Jinja2, no SPA).

## What it is (consensus)
Two layers: **(1)** the original project-tracker (Project / ProjectLanguage / ProjectRepository; parent-child hierarchy, auto-slugs); **(2)** the now-dominant **Theme Management System** — the authoritative DB-as-source-of-truth for design themes (8-table schema; imports 6 commercial Bootstrap/SCSS themes up to ~2,954 tokens each; CRUD/import/export/diff/versioning UI; **bidirectional DESIGN.md (Google) + W3C DTCG JSON** interchange, round-trip-proven; framework-native output for Tailwind 4 `@theme`, Bootstrap `_variables.scss` (Dart-Sass-verified), and CSS custom properties; DaisyUI semantic-role coverage). "Prototype Freedom" stance (ADR-008): no production users; the one surviving cross-project constraint is **PostgreSQL portability** for the eventual merge into `aixodev-web`.

> Baseline drastically understates this repo ("project-tracking model") — see [`../../ERRATA.md`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From backlog:** a TypingMind-style project-scoped AI chat (import all prior Claude Code chats separated by project); theme inheritance chains (base corporate → product → project); multiple themes per project; Stitch MCP integration; import from public DESIGN.md catalogs; generate-theme-from-URL; a full Sass AST evaluator; a DB-backed `frontend-design` plugin replacement; a native-Python (or Python+Rust) DESIGN.md CLI to drop the Node dependency.
- **From backlog (cross-product):** DiviaCard Svelte components floated as an intermediary for Bootstrap→Tailwind conversion — a rare AIXO↔Divia idea-level link.
- ✦ **New:** position the theme system as the **design layer for the whole portfolio** — one DB-as-source-of-truth could theme aixodev-web, aixocode's TUI themes, *and* the Divia apps, turning a prototype into shared infrastructure. ✦ Ship the round-trip DESIGN.md/DTCG engine as a standalone open tool (the interchange is genuinely novel and could seed an AIXO.Dev community wedge).
