# Tech Stack: Python / Flask Web Application

> Architectural components, skeleton generation instructions, and lessons learned for Python/Flask web applications. Referenced by `workflow_build_new_project.md`.

## Last Reviewed

| Date | Context | Changes |
|------|---------|---------|
| 2026-05-03 | Initial creation from `aixodev-projects` patterns | First version |

---

## Commands & Validation

> The canonical command set for this stack — the **single source of truth**. A project's `PROJECT_IDENTITY.md` points here (and records any per-project deviations); workflow bodies refer to "the validation suite" rather than re-deriving commands.

| Purpose | Command |
|---------|---------|
| Install dependencies (incl. dev) | `uv sync --group dev` |
| **Validation suite** — both must pass before every commit | `uv run pytest tests/ -v` **and** `uv run ruff check .` |
| Run a single test | `uv run pytest tests/path/to/test_file.py::test_name -v` |
| Type check (optional in this family) | `uv run mypy app/` |
| Dev server | `uv run flask --app run:app run --debug` (app factory `create_app()`) |
| Create a migration | `uv run flask db migrate -m "..."` |
| Apply migrations | `uv run flask db upgrade` |
| Migration state | `uv run flask db current` / `uv run flask db history` |

---

## Architectural Components Manifest

When creating a new Python/Flask project, the following components require decisions. The agent prefills answers from the source project's established patterns and the user's notes, then presents the full manifest for collaborative discussion.

Components marked **"inherit from source"** are decisions already made in the source project — the agent should prefill these and only ask if the user's notes explicitly contradict them or if there's genuine ambiguity.

### Core Platform

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 1 | **Python version** | 3.12+ | `.python-version` pinned to `3.12` | Never — inherit from source |
| 2 | **Package manager** | `uv` | `pyproject.toml` + `uv.lock` committed; `uv sync --group dev` for install | Never — inherit from source. If the source ever migrates (e.g., `pip` → `uv`), update this row |
| 3 | **Build backend** | `hatchling` | Configured in `pyproject.toml` `[build-system]` | Never — inherit from source |
| 4 | **Web framework** | Flask 3.x | App factory pattern (`create_app()`), Blueprint-based routing | Never — inherit from source |
| 5 | **WSGI entry point** | `run.py` | `from app import create_app; flask_app = create_app()` | Never — inherit from source |

### Data Layer

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 6 | **ORM** | SQLAlchemy 2.0+ | Via Flask-SQLAlchemy; declarative models in `app/models/` | Never — inherit from source |
| 7 | **Database (local dev)** | SQLite | WAL mode; `instance/{project}_dev.sqlite3` | Only if user mentions PostgreSQL, MySQL, or another DB explicitly |
| 8 | **Migrations** | Flask-Migrate (Alembic) | `flask db migrate` / `flask db upgrade`; `migrations/` directory | Never — inherit from source |
| 9 | **Settings management** | pydantic-settings | `BaseSettings` subclass in `app/settings.py`; `.env` file support | Never — inherit from source |

### Frontend & UI

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 10 | **Template engine** | Jinja2 | Server-side rendering; templates in `app/templates/` | Never — inherit from source |
| 11 | **CSS approach** | Bootstrap (plain) | See detailed guidance below | **Always ask.** Three paths: (a) Tailwind CSS (utility-first, built from scratch), (b) Bootstrap with default theme or custom colors, (c) Bootstrap theme from an existing purchased theme set. The choice affects the entire HTML/CSS generation strategy — it's not a detail that can be deferred. |
| 12 | **Theme source** | None (default Bootstrap) | See detailed guidance below | **Ask if the CSS approach is Bootstrap-based.** Options: (a) default Bootstrap (CDN, no customization), (b) custom colors only (extract a palette, apply via Bootstrap Sass variables or CSS custom properties), (c) purchased theme set as a design guide — extract only the specific version and components needed, never copy the full theme package. See "HTML/CSS Theme Strategy" below. |
| 13 | **JavaScript SPA framework** | **None (server-rendered)** | No React, Vue, Svelte, etc. | **Always ask if user's notes don't mention it.** This is the most common ambiguity — the source project may not have an SPA, but the new project might need one. If the user's notes describe heavy client-side interactivity (dashboards, real-time updates, drag-and-drop), ask whether they want server-rendered pages with HTMX/Alpine.js or a full SPA framework. |
| 14 | **JavaScript interactivity** | Vanilla JS + Bootstrap JS | For progressive enhancement on server-rendered pages | Ask if user describes interactive features that suggest HTMX, Alpine.js, or similar |
| 15 | **Map / visualization libraries** | None | | Ask if user mentions maps (Leaflet, Mapbox), charts (Chart.js, D3), or dashboards |

#### HTML/CSS Theme Strategy

This decision is a three-way fork that shapes how every template and stylesheet is generated. The agent must resolve it during Step 2 before any files are created.

**Path A — Tailwind CSS:**
- Utility-first CSS framework; no pre-built components.
- Requires a build step (`npx tailwindcss` or equivalent) during development.
- Best for projects where the UI is being designed from scratch or where the team has strong Tailwind experience.
- If chosen: add `tailwindcss` to dev dependencies, configure `tailwind.config.js`, add the build command to the Quick Start section.

**Path B — Bootstrap (default or custom palette):**
- Component-rich CSS framework; works out of the box via CDN.
- For custom colors: extract a palette (primary, secondary, accent, background, text) and apply via Bootstrap's Sass variables (`$primary`, `$secondary`, etc.) or CSS custom properties. This produces a distinctive look without importing any third-party theme code.
- Best for prototypes and projects that need to look presentable quickly without a designer.

**Path C — Bootstrap with purchased theme as design guide:**
- Use a previously purchased theme set (e.g., from WrapBootstrap.com) as a **visual reference and color/component guide**, not as a wholesale import.
- **HARD RULE: Never copy the full theme package into the project.** These theme sets are bloatware by nature — dozens of CSS classes, multiple framework versions (HTML, Vue, React, Angular), demo pages, and assets that will never be used. Copying them in creates maintenance nightmares and huge unused asset footprints.
- **Process when using a purchased theme:**
  1. **Identify the single version** that matches the project's stack. If the theme includes plain-HTML, Vue, React, and Angular versions, use ONLY the plain-HTML version (for server-rendered Jinja2 projects) or ONLY the Vue version (if an SPA was chosen). Ignore all other versions entirely.
  2. **Extract the design tokens:** color palette (hex/RGB values for primary, secondary, accent, backgrounds, text, borders), typography (font families, sizes, weights), spacing scale, border-radius values, shadow definitions.
  3. **Extract specific component patterns** needed for the project: navigation bar style, card layouts, form styling, table styling, dashboard widget patterns. Reference the theme's HTML structure as a guide but rewrite it clean for the project's actual needs.
  4. **Build a project-specific stylesheet** using the extracted tokens. This can be Bootstrap Sass with overridden variables, or a standalone CSS file with custom properties. The result should be a clean, minimal stylesheet that produces the theme's visual character without importing the theme's actual CSS files.
  5. **Document the theme source** in the project's CLAUDE.md or a `DESIGN.md` file: theme name, where it was purchased, which version was referenced, and which design tokens were extracted. This creates a paper trail for licensing and for future designers who may want to reference the original.
- **Why this approach instead of importing the theme:** LLM code generation is now good enough to reproduce a theme's visual character from design tokens alone. The generated CSS will be fully optimized for the specific pages the project actually builds, with zero unused classes. A purchased theme's value is in its design decisions (colors, typography, component shapes), not in its CSS implementation — which is inevitably bloated because it has to cover every possible page layout the theme vendor imagined.

### Auth & Security

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 16 | **Authentication** | JWT (Flask-JWT-Extended) | Token-based auth | User mentions OAuth, session-based auth, social login, or "no auth needed" |
| 17 | **Authorization / roles** | None | No role-based access in current project | User describes multi-user, admin panels, or permission systems |
| 18 | **CORS** | Not configured | | User mentions API consumed by a separate frontend, mobile app, or third-party |

### Testing & Quality

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 19 | **Test framework** | pytest | `uv run pytest tests/ -v`; `tests/conftest.py` with app/client/db_session fixtures | Never — inherit from source |
| 20 | **Test DB strategy** | SQLite in-memory | `sqlite:///:memory:` for speed; SAVEPOINT-based rollback isolation per test | Never — inherit from source |
| 21 | **Linter** | Ruff | `uv run ruff check .`; config in `pyproject.toml` | Never — inherit from source |
| 22 | **Type checker** | None | Source project doesn't use mypy | Only if user explicitly requests type checking |
| 23 | **Browser / E2E testing** | None | | Ask if user describes UI-heavy features that warrant Playwright or Selenium |

### External Integrations

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 24 | **External APIs** | None | | **Always ask if user's notes mention third-party services.** Each integration needs: API client library (or raw `httpx`), credentials management (env vars), rate limiting strategy, and error handling. List them explicitly in the manifest. |
| 25 | **Background tasks** | None | No Celery, RQ, or APScheduler | Ask if user describes scheduled jobs, long-running imports, or async processing |
| 26 | **File storage** | Local filesystem | `instance/uploads/`, `static/exports/` | Ask if user mentions S3, cloud storage, or large file handling |
| 27 | **Email / notifications** | None | | Ask if user mentions transactional email, alerts, or notification systems |

### Deployment & Operations

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 28 | **Deployment target** | Local only | No Docker, no cloud hosting | Ask if user mentions deployment, Docker, Vercel, Railway, etc. |
| 29 | **CI/CD** | None | | Ask if user mentions GitHub Actions, automated testing, or deployment pipelines |
| 30 | **Logging** | Flask default | No structured logging configured | Ask if user mentions observability, structured logging, or log aggregation |
| 31 | **Monitoring** | None | | Ask if user mentions uptime, metrics, or alerting |

---

## How to Use the Manifest

### Prefilling

When running `workflow_build_new_project.md` Step 2, the agent:

1. **Reads this document** to load the full component list
2. **Reads the source project's `CLAUDE.md`** to verify current defaults are still accurate
3. **Reads the user's scratch-pad notes** and marks each component as:
   - **Inherited** — same as source, no discussion needed (show as pre-filled)
   - **Specified by user** — user's notes explicitly chose this (show as pre-filled with user's choice)
   - **Ambiguous / needs discussion** — not mentioned by user and the default may not be right (highlight for discussion)
4. **Presents a condensed manifest** showing all components, with inherited ones shown but not requiring confirmation, and ambiguous ones flagged with a question

### Condensed Manifest Format (for presenting to user)

```
ARCHITECTURAL MANIFEST — {Project Name}

Inherited from {source project} (confirm or override):
  Python 3.12+ / uv / hatchling / Flask 3.x / SQLAlchemy 2.0 / SQLite
  Flask-Migrate / pydantic-settings / Jinja2 / Bootstrap / pytest / Ruff
  JWT auth / No type checker / Local deployment only

From your notes:
  [items the agent extracted from the user's notes]

Questions (need your input):
  1. Frontend interactivity: Your notes mention {X feature} —
     server-rendered with HTMX/Alpine.js, or full SPA (React/Vue)?
  2. External APIs: You mention {service} — do you have API access?
     What client library preference?
  3. Background tasks: Importing {data sources} — synchronous on
     request, or background job queue?
  ...
```

The user responds, the agent updates the manifest, and iteration continues until the user approves. Each turn is a "diff" against the manifest. When the user says "looks good" or equivalent, the manifest is finalized and drives Steps 3+ of the build workflow.

---

## Skeleton Generation

After the manifest is approved, generate these files for the new project. The agent reads the source project's actual files (not this document's descriptions) to pick up the latest patterns, then adapts them.

### Configuration Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `pyproject.toml` | Yes | New project name, package name, description. Same Python version, same core dependency versions, same ruff/pytest config structure. Remove source-project-specific dependencies. Add dependencies from the approved manifest (e.g., `httpx` if external APIs were specified, `Flask-Login` if session auth was chosen instead of JWT, map/chart libraries if specified). |
| `.python-version` | Yes | Copy verbatim |
| `.gitignore` | Yes | Copy verbatim — the source project's gitignore is comprehensive across Python/Node/Rust stacks |
| `.env.example` | Yes | Adapt env var prefix to new project's short name (e.g., `KINGSTRATVC_ENV` → `{SHORTNAME}_ENV`). Add env vars for any external API keys from the manifest. |

### Application Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `app/__init__.py` | Yes | Same `create_app()` factory. Adapt: settings import path, env var names, blueprint registration (start empty). Remove source-specific CLI commands. |
| `app/config.py` | Yes | Same `get_settings()` + `settings_to_flask_config()`. Adapt settings class name. |
| `app/settings.py` | Yes | Same pydantic-settings `BaseSettings` pattern. Adapt: class name, env var names, database filename, any new settings from manifest (API keys as `SecretStr`, etc.). |
| `app/extensions.py` | Yes | Same `db = SQLAlchemy()` + `migrate = Migrate()`. Add other extension instances if manifest specified them (e.g., `login_manager = LoginManager()` for session auth). |
| `app/models/__init__.py` | Yes | Empty — models created during sprint execution |
| `app/api/__init__.py` | Yes | Same `register_api_blueprints()` with empty list |
| `app/views/__init__.py` | Yes | Same `register_view_blueprints()` with empty list |
| `run.py` | Yes | Nearly verbatim — same `create_app()` + `flask_app.run()` |

### Test Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `tests/__init__.py` | Yes | Empty file |
| `tests/conftest.py` | Yes | Same fixture pattern (app, client, runner, db_session with SAVEPOINT rollback). Adapt: env var names, settings import, app import. |

### Directories

```
instance/
static/
static/css/
static/js/
static/uploads/   (with .gitkeep)
static/exports/   (with .gitkeep)
migrations/       (will be populated by flask db init later)
```

If the manifest specified a templates directory for Jinja2 (which it should by default):

```
app/templates/
app/templates/base.html        (minimal base template with Bootstrap CDN)
app/templates/index.html       (extends base, "Hello {project_name}")
```

### Functional Verification

After skeleton generation, these commands must all succeed:

```bash
cd {target_dir}
uv sync --group dev                # Installs all dependencies
uv run pytest tests/ -v            # 0 collected (pass) or basic smoke tests pass
uv run ruff check .                # Clean
uv run flask run --debug           # Starts without errors (manual verification by user)
```

---

## Lessons Learned

This section records hard-won lessons from real projects built with this stack. Review and update during post-sprint analysis (see `workflow_build_new_project.md` Step 15).

### Package Management

- **`uv` replaced `pip` + `python3 -m venv`** — `uv` handles virtualenv creation, dependency resolution, and lockfile management in one tool. All new projects use `uv sync --group dev` for setup and `uv run` as the command prefix. If a lesson is learned that changes this preference, update both this document and the source project's `CLAUDE.md`.

### App Factory Pattern

- The `create_app()` factory with `config_name` parameter for env switching (development/testing/production) has been stable across all Flask projects. Do not deviate without strong justification.
- The `extensions.py` pattern (instantiate extensions at module level, `init_app()` inside the factory) avoids circular imports and is the standard Flask pattern.

### Testing

- **SAVEPOINT-based test isolation** (the `db_session` fixture in `conftest.py`) is non-negotiable for any project with database tests. It provides real rollback isolation without the overhead of recreating the database per test. The pattern was refined over multiple projects — copy it verbatim.
- Setting `KINGSTRATVC_ENV=testing` (or equivalent) in `conftest.py` via `os.environ` BEFORE any app imports is load-bearing — `pydantic-settings` reads env vars at import time.

### Settings

- `pydantic-settings` with `.env` file support has been the most reliable configuration pattern. `SecretStr` for sensitive values prevents accidental logging. The `extra='ignore'` setting in `SettingsConfigDict` prevents crashes from unrecognized env vars.

### Frontend

- Bootstrap via CDN is the fastest path to a presentable UI for prototypes. If a project outgrows server-rendered pages, the migration path is: (1) add HTMX for progressive interactivity, (2) if that's insufficient, introduce a JS framework for specific views, (3) full SPA only if the entire app is highly interactive.
- No project has yet needed a full SPA — all have been well-served by server-rendered Jinja2 + Bootstrap + optional HTMX. This may change, and that's what the manifest question about "JavaScript SPA framework" is for.
- **Purchased Bootstrap themes are design guides, not code imports.** Over 10+ years, a dozen or more theme sets were purchased from WrapBootstrap.com. These were originally intended as full HTML/CSS starting points. With LLM code generation, the better approach is to extract design tokens (colors, typography, spacing, component shapes) and generate project-specific CSS from those tokens. This produces clean, minimal stylesheets with zero unused classes — versus the massive bloatware packages these themes ship as. Many themes include 3-5 framework versions (HTML, Vue, React, Angular); only ever reference the single version matching the project's stack.
- **The CSS approach decision is not deferrable.** It affects how every template is generated: Tailwind utility classes produce fundamentally different HTML than Bootstrap component classes. Resolve this in the architectural discussion, not during the first sprint.

---

## Debugging

> The **stack-specific half** of [`../workflow_error_debugging.md`](../workflow_error_debugging.md). That workflow holds the stack-agnostic method; this section holds the Flask (sync) error tables, scenarios, and commands. Debugging this stack centers on the dev server, Flask-SQLAlchemy sessions, Flask-Migrate migrations, Jinja2 templates, route/request errors, and any external integrations.

### Quick reference

| Resource | Command / Path |
|----------|---------------|
| Run all tests | `uv run pytest tests/ -v` |
| Run specific test | `uv run pytest tests/path/to/test_file.py::test_function -v` |
| Stop at first failure | `uv run pytest tests/ -x --tb=short` |
| Lint | `uv run ruff check .` |
| Dev server | `uv run flask --app run:app run --debug` (app factory `create_app()`) |
| Migration state | `uv run flask db current` / `uv run flask db history` |
| SQLite shell (inspect dev DB) | `sqlite3 <db_file>` then `.schema` |

### Where the error surfaces

| Source | Location |
|--------|----------|
| Test failure | Terminal output from `pytest` |
| Lint error | Terminal output from `uv run ruff check .` |
| Import error | Traceback at collection time (`pytest` fails before any test runs) |
| Request / 500 error | Dev server console (full interactive Werkzeug traceback with `--debug`) |
| Template error | `jinja2.exceptions.*` (`TemplateNotFound`, `UndefinedError`) |
| DB error | `sqlalchemy.exc.*` / `sqlite3.OperationalError` |
| Config / settings | `ValidationError` from pydantic-settings at startup |

### Error categories

| Category | Symptoms | Typical Cause |
|----------|----------|---------------|
| **ImportError** | `ModuleNotFoundError`, `cannot import name` | Missing dependency in `pyproject.toml`, circular import (common with `create_app` ↔ blueprints/models), typo in import path |
| **AttributeError** | `'X' object has no attribute 'Y'` | Renamed model attribute, wrong variable, module shadowing |
| **Flask / routing** | 404 on a route that should exist, 405, `working outside of request/application context` | Blueprint not registered, wrong URL rule, accessing `request`/`g`/`current_app` outside a context |
| **Template (Jinja2)** | `TemplateNotFound`, `UndefinedError`, blank/garbled page | Wrong template path/name, variable not passed to `render_template`, autoescape on raw HTML |
| **Database (Flask-SQLAlchemy)** | `sqlalchemy.exc.*`, `DetachedInstanceError`, `no such column`, locked DB | Attribute access after the session closed, schema/migration drift, a session left open, WAL contention |
| **Migration (Flask-Migrate)** | `Target database is not up to date`, autogenerate empty/wrong | DB not upgraded (`flask db upgrade`), model not imported into the migration env, non-portable SQLite-only construct |
| **Config / settings** | `ValidationError` from pydantic-settings, missing key | Env var not set (this project's env-var prefix — see [`../PROJECT_IDENTITY.md`](../PROJECT_IDENTITY.md)), missing `.env`, wrong type |

### Locate the source

**Python exceptions:** read the traceback bottom-to-top, find the first `app/` frame, open it at the indicated line. Check: is a value `None` that shouldn't be? Is the attribute name correct? Is the object detached from its session?

**Request / 500 errors:** reproduce with the dev server in `--debug` for the full interactive Werkzeug traceback; confirm the blueprint is registered in `create_app()` and the URL rule matches; check you're inside an application/request context.

**Database / migration issues:** inspect the dev DB (`sqlite3 <db_file>` then `.schema`); check migration state (`uv run flask db current` vs `history`, run `flask db upgrade` if behind); reproduce against a throwaway/fixture DB, never important local data.

### Common scenarios

**`sqlalchemy.orm.exc.DetachedInstanceError`** — You accessed an attribute (often a lazy relationship) after the request's session was torn down. Access what you need before the session closes, or eager-load with `joinedload`/`selectinload`.

**`sqlite3.OperationalError: database is locked`** — SQLite + WAL has limited write concurrency. Usually a session left open or two writers collided. Ensure sessions are committed/closed, set a `busy_timeout`, and keep write transactions short.

**Flask-Migrate autogenerate produces an empty or wrong migration** — The model wasn't imported into the migration environment, so it can't be seen. Ensure all models are imported where the metadata is defined, then re-run `uv run flask db migrate -m "..."` and review the script before `flask db upgrade`. Avoid SQLite-only constructs so the migration stays Postgres-portable.

**`jinja2.exceptions.TemplateNotFound` / `UndefinedError`** — Check the template name/path relative to the templates folder and confirm every variable the template uses is passed to `render_template(...)`. Guard possibly-absent values in the template.

**Reading a 500 in the browser (debug mode)** — With `--debug`, an unhandled exception renders the interactive Werkzeug debugger in the browser — click a frame to inspect it. **Never run debug mode in any shared/exposed environment** — the interactive console is a remote-code-execution risk.

**`AttributeError: module 'app' has no attribute 'X'` (module shadowing) / stale imports** — A local variable named `app` can shadow the package, and stale bytecode can mask a fix. (1) Don't reuse the package name as a local variable; (2) clear caches: `find . -type d -name __pycache__ -exec rm -rf {} +` then re-run.

### Quick diagnostic commands

```bash
# Tests + lint
uv run pytest tests/ -v --tb=short
uv run ruff check .

# Import sanity
uv run python -c "import app; print('app OK')"

# App factory sanity
uv run python -c "from app import create_app; create_app(); print('create_app OK')"

# Migration state
uv run flask db current
uv run flask db history

# Inspect the dev DB read-only
sqlite3 -readonly <db_file> "PRAGMA integrity_check;"
```

---

## Evolution Notes

When this tech stack document is updated (new patterns, deprecated approaches, lessons learned), add an entry to the "Last Reviewed" table at the top. This allows downstream projects and post-sprint review agents to see what changed and when.
