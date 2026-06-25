# Tech Stack: Python / Quart (async) Web Application

> Architectural components, skeleton generation instructions, and lessons learned for Python/**Quart** (async Flask) web applications. Referenced by `workflow_build_new_project.md`. Forked from `techstack--python_flask.md` — Quart mirrors Flask's app-factory / Blueprint / Jinja2 model but is **async-native (ASGI)**, so the data layer, server, background tasks, and tests all differ. Keep this document evolving independently of the Flask one.

## Last Reviewed

| Date | Context | Changes |
|------|---------|---------|
| 2026-06-24 | Forked from `techstack--python_flask.md` for a Python/Quart (async) build-line | First version. Converted WSGI→ASGI (Hypercorn), Flask-SQLAlchemy→async SQLAlchemy 2.0, Flask-Migrate→Alembic (async template), Flask-Login/JWT→Quart-Auth, sync test client→async (pytest-asyncio), and promoted in-process async background tasks (APScheduler) to first-class. |

---

## Why Quart (and when not to)

Quart is a re-implementation of the Flask API on top of `asyncio`/ASGI. You keep almost everything Flask developers know — `create_app()` factory, Blueprints, `request`/`g`/`current_app` contexts, Jinja2 templates, the decorator-based routing — but view functions are `async def`, I/O is awaited, and the app is served by an ASGI server.

**Choose Quart when** the app does meaningful concurrent I/O: calling external APIs, running scheduled/background ingestion, websockets/SSE, or many slow-but-not-CPU-bound requests. A flagship motivating case is a **scheduled external-API ingestion service** (e.g. polling Gmail) running inside the web app.

**Stay on Flask when** the app is request/response CRUD with no background work and the team wants the larger sync ecosystem (Flask-Login, Flask-Admin, etc.) — see `techstack--python_flask.md`.

**The one rule that governs everything:** never block the event loop. Any synchronous, blocking call (a sync DB driver, `requests`, `time.sleep`, heavy CPU, or a sync SDK like the Google API client) must be `await`ed against an async equivalent or pushed off the loop with `asyncio.to_thread(...)` / a thread/process executor. A single blocking call stalls every concurrent request.

**Package layout:** the house default is a top-level **`app/`** package (`from app import create_app`), mirroring the Flask doc. A project *may* choose a distinctly-named or `src/`-layout package instead (more common for importable libraries than for apps); if so, document it in the project's `CLAUDE.md`. This doc writes `app/` throughout.

---

## Commands & Validation

> The canonical command set for this stack — the **single source of truth**. A project's `PROJECT_IDENTITY.md` points here (and records any per-project deviations); workflow bodies refer to "the validation suite" / "the active techstack's Commands & Validation" rather than re-deriving commands. The default uv/Python commands are also written out inline in the execution-oriented workflows for convenience; this table is authoritative if they ever diverge.

| Purpose | Command |
|---------|---------|
| Install dependencies (incl. dev) | `uv sync --group dev` |
| **Validation suite** — both must pass before every commit | `uv run pytest tests/ -v` **and** `uv run ruff check .` |
| Run a single test | `uv run pytest tests/path/to/test_file.py::test_name -v` |
| Type check (optional in this family) | `uv run mypy app/` |
| Dev server | `uv run quart --app run:app run --debug` (app factory `create_app()`) |
| Production server | `uv run hypercorn run:app --bind 0.0.0.0:8000` |
| Create a migration (autogenerate) | `uv run alembic revision --autogenerate -m "..."` |
| Apply migrations | `uv run alembic upgrade head` |
| Migration state | `uv run alembic current` / `uv run alembic history` |

---

## Architectural Components Manifest

When creating a new Python/Quart project, the following components require decisions. The agent prefills answers from the source project's established patterns and the user's notes, then presents the full manifest for collaborative discussion.

Components marked **"inherit from source"** are decisions already made in the source project — the agent should prefill these and only ask if the user's notes explicitly contradict them or if there's genuine ambiguity.

### Core Platform

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 1 | **Python version** | 3.12+ | `.python-version` pinned to `3.12` | Never — inherit from source |
| 2 | **Package manager** | `uv` | `pyproject.toml` + `uv.lock` committed; `uv sync --group dev` for install | Never — inherit from source |
| 3 | **Build backend** | `hatchling` | Configured in `pyproject.toml` `[build-system]` | Never — inherit from source |
| 4 | **Web framework** | **Quart 0.19+** | App factory (`create_app()`), Blueprint-based routing, `async def` views | Never — inherit from source |
| 5 | **ASGI entry point** | `run.py` | `from app import create_app; app = create_app()` — served by an ASGI server, not WSGI | Never — inherit from source |
| 6 | **ASGI server** | **Hypercorn** | Quart's reference server. Dev: `quart --app run:app run --debug`. Prod: `hypercorn run:app --bind 0.0.0.0:8000` | Ask only if user wants Uvicorn/Daphne specifically |

### Data Layer

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 7 | **ORM** | **SQLAlchemy 2.0+ (async)** | `create_async_engine` + `async_sessionmaker[AsyncSession]`. **Not** Flask-SQLAlchemy (sync-only). Declarative models in `app/models/`; engine/sessionmaker built in the app factory | Never — inherit from source |
| 8 | **DB driver (local dev)** | **aiosqlite** | `sqlite+aiosqlite:///instance/{project}_dev.sqlite3`; WAL mode via a `connect` event/pragma | Only if user mentions PostgreSQL/MySQL explicitly |
| 9 | **DB driver (prod path)** | **asyncpg** | `postgresql+asyncpg://...` — keep the schema clean and Postgres-portable from day one | Inherit; confirm when the PostgreSQL move is scheduled |
| 10 | **Migrations** | **Alembic (async template)** | `alembic init -t async migrations`; `uv run alembic revision --autogenerate -m "..."` / `uv run alembic upgrade head`. **Not** Flask-Migrate (Flask/sync-bound) | Never — inherit from source |
| 11 | **Per-request session** | `g`-scoped `AsyncSession` | Open in `@app.before_request`, commit/rollback + close in `@app.teardown_request`/`teardown_appcontext`; or an `async with` dependency. One session per request; never share an `AsyncSession` across tasks | Never — inherit from source |
| 12 | **Settings management** | pydantic-settings | `BaseSettings` subclass in `app/settings.py`; `.env` support; `SecretStr` for keys/tokens | Never — inherit from source |

### Frontend & UI

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 13 | **Template engine** | Jinja2 (async) | Server-side rendering; templates in `app/templates/`. In Quart, **`await render_template(...)`** (rendering is a coroutine) | Never — inherit from source |
| 14 | **CSS approach** | Bootstrap (plain) | See "HTML/CSS Theme Strategy" below | **Always ask.** Three paths: (a) Tailwind (utility-first, build step), (b) Bootstrap default/custom palette, (c) Bootstrap from a purchased theme as a design guide. Shapes all HTML/CSS generation — not deferrable. |
| 15 | **Theme source** | None (default Bootstrap) | See "HTML/CSS Theme Strategy" below | **Ask if CSS approach is Bootstrap-based.** (a) default Bootstrap CDN, (b) custom colors via Sass vars / CSS custom properties, (c) purchased theme as a design guide — extract tokens, never copy the package. |
| 16 | **JavaScript SPA framework** | **None (server-rendered)** | No React/Vue/Svelte | **Always ask if user's notes don't mention it.** If they describe heavy client interactivity, ask: server-rendered + HTMX/Alpine.js, or a full SPA? |
| 17 | **JavaScript interactivity** | Vanilla JS + Bootstrap JS | Progressive enhancement on server-rendered pages | Ask if features suggest HTMX/Alpine.js |
| 18 | **Realtime (websockets/SSE)** | None | Quart supports websockets (`@app.websocket`) and SSE natively — a genuine reason to pick Quart | Ask if user mentions live updates, chat, notifications, progress streams |
| 19 | **Map / visualization libraries** | None | | Ask if user mentions maps (Leaflet, Mapbox), charts (Chart.js, D3), dashboards |

#### HTML/CSS Theme Strategy

This decision is a three-way fork that shapes how every template and stylesheet is generated. The agent must resolve it during Step 2 before any files are created. (Framework-agnostic — identical to the Flask stack.)

**Path A — Tailwind CSS:**
- Utility-first CSS framework; no pre-built components.
- Requires a build step (`npx tailwindcss` or equivalent) during development.
- Best for projects designed from scratch or where the team has strong Tailwind experience.
- If chosen: add `tailwindcss` to dev tooling, configure `tailwind.config.js`, add the build command to Quick Start.

**Path B — Bootstrap (default or custom palette):**
- Component-rich CSS framework; works out of the box via CDN.
- For custom colors: extract a palette (primary, secondary, accent, background, text) and apply via Bootstrap's Sass variables or CSS custom properties. Distinctive look without importing third-party theme code.
- Best for prototypes and projects that need to look presentable quickly without a designer.

**Path C — Bootstrap with purchased theme as design guide:**
- Use a previously purchased theme set (e.g., from WrapBootstrap.com) as a **visual reference and color/component guide**, not a wholesale import.
- **HARD RULE: Never copy the full theme package into the project.** These theme sets are bloatware — dozens of CSS classes, multiple framework versions (HTML, Vue, React, Angular), demo pages, and unused assets. Copying them in creates maintenance nightmares and huge unused footprints.
- **Process when using a purchased theme:**
  1. **Identify the single version** matching the stack. For server-rendered Jinja2 projects, use ONLY the plain-HTML version. Ignore all others.
  2. **Extract the design tokens:** color palette (hex/RGB for primary, secondary, accent, backgrounds, text, borders), typography (families, sizes, weights), spacing scale, border-radius, shadows.
  3. **Extract specific component patterns** needed: nav bar, card layouts, form styling, table styling, widget patterns. Reference the structure as a guide but rewrite clean for the project's actual needs.
  4. **Build a project-specific stylesheet** from the extracted tokens (Bootstrap Sass with overridden variables, or standalone CSS custom properties). Clean, minimal, zero unused classes.
  5. **Document the theme source** in `CLAUDE.md` or `DESIGN.md`: theme name, where purchased, which version referenced, which tokens extracted. A paper trail for licensing and future designers.
- **Why this instead of importing:** LLM code generation can reproduce a theme's visual character from design tokens alone, fully optimized for the pages the project actually builds. A purchased theme's value is in its design decisions, not its (inevitably bloated) CSS implementation.

### Auth & Security

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 20 | **Authentication** | **Quart-Auth** | Cookie/session-based auth, Quart-native (`@login_required`, `current_user`, `login_user`). **Not** Flask-Login/Flask-JWT-Extended (Flask-bound). For token APIs, pair Quart-Auth or add JWT via `pyjwt` | User mentions OAuth, token-only APIs, social login, or "no auth needed" |
| 21 | **Request/response validation** | **Quart-Schema** (recommended) | pydantic-based request/response validation with automatic OpenAPI/Swagger docs — a strong Quart-native fit since pydantic-settings is already in the stack | Ask/offer when the app exposes JSON APIs |
| 22 | **Authorization / roles** | None | No role-based access by default | User describes multi-user, admin panels, permissions |
| 23 | **CORS** | Not configured | Add **Quart-CORS** if needed (not Flask-CORS) | User mentions a separate frontend, mobile app, or third-party API consumers |
| 24 | **Rate limiting** | None | `quart-rate-limiter` if needed | User mentions abuse protection or public endpoints |

### Testing & Quality

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 25 | **Test framework** | **pytest + pytest-asyncio** | `uv run pytest tests/ -v`; `asyncio_mode = "auto"` in config; `tests/conftest.py` with async app/client/db fixtures | Never — inherit from source |
| 26 | **Test client** | Quart async test client | `async with app.test_app() as t: client = t.test_client()` (drives lifespan, so `before_serving`/`after_serving` run); `resp = await client.get(...)` | Never — inherit from source |
| 27 | **Test DB strategy** | **in-memory aiosqlite** | `sqlite+aiosqlite:///:memory:` with **`StaticPool`** + a single shared connection (so every async session sees the same in-memory DB); async **SAVEPOINT**-based rollback isolation per test | Never — inherit from source |
| 28 | **Linter** | Ruff | `uv run ruff check .`; config in `pyproject.toml` | Never — inherit from source |
| 29 | **Type checker** | None | Optional in this family (matches the Flask default) | Only if user explicitly requests it |
| 30 | **Browser / E2E testing** | None | | Ask if UI-heavy features warrant Playwright (async API fits well) |

### External Integrations

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 31 | **External APIs** | None (per project) | Prefer `httpx.AsyncClient` for raw async HTTP. **Sync SDKs (e.g. the Google API Python client for Gmail) must be wrapped in `asyncio.to_thread(...)`** so they don't block the loop. Credentials via env / `SecretStr`; OAuth client secrets & tokens stay OUT of git | **Always ask if user's notes mention third-party services.** Each needs: client library choice, credential management, rate-limit + retry strategy, error handling. |
| 32 | **Background / scheduled tasks** | **In-process asyncio** | First-class in Quart: `app.add_background_task(coro)` for fire-and-forget, and **APScheduler `AsyncIOScheduler`** (started in `@app.before_serving`, shut down in `@app.after_serving`) for cron/interval jobs — e.g. a periodic Gmail ingestion poll. Reach for Celery/RQ only when you need a separate worker fleet or durable queues | Ask if user describes scheduled jobs, long-running imports, or polling |
| 33 | **File storage** | Local filesystem | `instance/uploads/`, `static/exports/` (e.g. listing photos) | Ask if user mentions S3/cloud storage or large media |
| 34 | **Email / notifications** | None | Use an async client or `asyncio.to_thread` around a sync mailer | Ask if user mentions transactional email or alerts |

### Deployment & Operations

| # | Component | Current Default | Notes | Ask If... |
|---|-----------|----------------|-------|-----------|
| 35 | **Deployment target** | Local only | Served by Hypercorn; if containerized, the image runs `hypercorn run:app` (ASGI), not a WSGI server | Ask if user mentions Docker, Vercel, Railway, Fly, etc. |
| 36 | **CI/CD** | None | | Ask if user mentions GitHub Actions or automated pipelines |
| 37 | **Logging** | Quart/stdlib logging | `app.logger`; add `structlog` if structured logs are wanted | Ask if user mentions observability/log aggregation |
| 38 | **Monitoring** | None | | Ask if user mentions uptime, metrics, alerting |

---

## How to Use the Manifest

### Prefilling

When running `workflow_build_new_project.md` Step 2, the agent:

1. **Reads this document** to load the full component list.
2. **Reads the source project's `CLAUDE.md`** to verify current defaults are still accurate.
3. **Reads the user's scratch-pad notes** and marks each component as **Inherited**, **Specified by user**, or **Ambiguous / needs discussion**.
4. **Presents a condensed manifest** — inherited items shown but not requiring confirmation; ambiguous ones flagged with a question.

### Condensed Manifest Format (for presenting to user)

```
ARCHITECTURAL MANIFEST — {Project Name}

Inherited from {source project} (confirm or override):
  Python 3.12+ / uv / hatchling / Quart 0.19 / Hypercorn (ASGI)
  async SQLAlchemy 2.0 / aiosqlite (→ asyncpg) / Alembic (async)
  pydantic-settings / Jinja2 / Bootstrap / Quart-Auth
  pytest + pytest-asyncio / Ruff / No type checker / Local deployment

From your notes:
  [items the agent extracted from the user's notes]

Questions (need your input):
  1. Frontend interactivity: Your notes mention {X feature} —
     server-rendered + HTMX/Alpine.js, or full SPA?
  2. External APIs: You mention {service} — async client or sync SDK
     wrapped via asyncio.to_thread? Credentials available?
  3. Background tasks: Scheduling {job} — in-process APScheduler, or a
     separate worker (Celery/RQ)?
  ...
```

The user responds, the agent updates the manifest, and iteration continues until approval. When the user says "looks good," the manifest is finalized and drives Steps 3+ of the build workflow.

---

## Skeleton Generation

After the manifest is approved, generate these files. The agent reads the source project's actual files (not this document's descriptions) to pick up the latest patterns, then adapts them.

### Configuration Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `pyproject.toml` | Yes | New project/package name. Same Python version and ruff/pytest config structure. Core deps: `quart`, `hypercorn`, `sqlalchemy[asyncio]`, `aiosqlite` (and `asyncpg` for the Postgres path), `alembic`, `pydantic-settings`, `quart-auth`. Add from manifest: `httpx`, `quart-schema`, `quart-cors`, `apscheduler`, `google-api-python-client`/`google-auth-oauthlib`, etc. Set `[tool.pytest.ini_options] asyncio_mode = "auto"`. |
| `.python-version` | Yes | Copy verbatim |
| `.gitignore` | Yes | Copy/adapt — ensure `.env`, OAuth `client_secret*.json` / `token*.json`, and `*.sqlite3`/`*.db` are ignored |
| `.env.example` | Yes | Adapt env var prefix to the project's short name (e.g., `{SHORTNAME}_ENV`, `{SHORTNAME}_DATABASE_URL`). Add vars for external API keys/secrets from the manifest. |

### Application Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `app/__init__.py` | Yes | `create_app()` factory: load settings, init the async engine + `async_sessionmaker`, register Blueprints (start empty), wire `before_request`/`teardown` for the request-scoped `AsyncSession`, and register `@app.before_serving`/`@app.after_serving` to start/stop background schedulers and dispose the engine. |
| `app/config.py` | Yes | `get_settings()` + a helper to map settings into `app.config`. Adapt settings class name. |
| `app/settings.py` | Yes | pydantic-settings `BaseSettings`. Adapt class name, env var names, `DATABASE_URL` default (`sqlite+aiosqlite:///instance/{project}_dev.sqlite3`); `SecretStr` for API keys/OAuth secrets. |
| `app/extensions.py` | Yes | The async engine + `async_sessionmaker` (created in the factory, referenced here), plus extension instances: `AuthManager()` (Quart-Auth), `QuartSchema()` / `cors` if chosen. **No** Flask-SQLAlchemy `db` object. |
| `app/db.py` | Yes | Session plumbing: `async def get_session()` returning the request-scoped `AsyncSession` from `g`; engine/sessionmaker accessors; the `connect` pragma for SQLite WAL/foreign-keys. |
| `app/models/__init__.py` | Yes | Declarative `Base` (`class Base(DeclarativeBase): ...`); models created during sprint execution. Ensure all models are imported where Alembic's `target_metadata` is defined. |
| `app/api/__init__.py` | Yes | `register_api_blueprints(app)` with an empty list |
| `app/views/__init__.py` | Yes | `register_view_blueprints(app)` with an empty list |
| `run.py` | Yes | `from app import create_app` / `app = create_app()` / `if __name__ == "__main__": app.run()` (dev). Production runs `hypercorn run:app`. |

### Migration Setup (Alembic, async)

```bash
uv run alembic init -t async migrations    # async env.py template
# edit migrations/env.py: import the app's settings for the DB URL,
# and set target_metadata = Base.metadata (import all models so autogenerate sees them)
uv run alembic revision --autogenerate -m "initial schema"
uv run alembic upgrade head
```

### Test Files

| Source file | Generate | Adaptations |
|------------|----------|-------------|
| `tests/__init__.py` | Yes | Empty file |
| `tests/conftest.py` | Yes | Async fixtures (pytest-asyncio): an `app` fixture (testing settings, in-memory `sqlite+aiosqlite:///:memory:` engine with `StaticPool` + shared connection so all sessions see one DB), an async `client` via `app.test_app()`, and a `db_session` fixture using an async nested-transaction (SAVEPOINT) rollback per test. Set the testing env var (e.g. `{SHORTNAME}_ENV=testing`) BEFORE importing the app — pydantic-settings reads env at import time. |

### Directories

```
instance/
static/
static/css/
static/js/
static/uploads/   (with .gitkeep)
static/exports/   (with .gitkeep)
migrations/       (populated by `alembic init -t async` above)
app/templates/
app/templates/base.html        (minimal base template with Bootstrap CDN)
app/templates/index.html       (extends base, "Hello {project_name}")
```

### Functional Verification

After skeleton generation, these commands must all succeed:

```bash
cd {target_dir}
uv sync --group dev                                  # Installs all dependencies
uv run python -c "from app import create_app; create_app(); print('create_app OK')"
uv run alembic upgrade head                          # Applies the initial migration
uv run pytest tests/ -v                              # 0 collected (pass) or smoke tests pass
uv run ruff check .                                  # Clean
uv run quart --app run:app run --debug               # Dev server starts (manual verification)
# Production form: uv run hypercorn run:app
```

---

## Lessons Learned

Hard-won lessons from real projects built with this stack. Review and update during post-sprint analysis (see `workflow_build_new_project.md` Step 15).

### The event loop is sacred

- **One blocking call stalls every concurrent request.** Audit views/services for sync I/O: a sync DB driver, `requests`, blocking file reads of large files, `time.sleep`, heavy CPU, and especially **sync third-party SDKs** (the Google API Python client is sync). Wrap unavoidable blocking work in `await asyncio.to_thread(fn, ...)` or an executor. This is the single most common Quart bug class.
- A stray un-`await`ed coroutine silently no-ops and emits `RuntimeWarning: coroutine '...' was never awaited`. Treat that warning as an error.

### App factory & lifecycle

- The `create_app()` factory carries over from Flask almost unchanged. The new pieces are **`@app.before_serving` / `@app.after_serving`** — the correct place to start/stop APScheduler, warm caches, open shared clients, and dispose the engine. (`before_serving` runs once the event loop exists, unlike module import time.)
- The `extensions.py` pattern still avoids circular imports, but the async engine is created in the factory (it needs the running loop / settings), not at module import.

### Async SQLAlchemy & sessions

- Use **one `AsyncSession` per request**, scoped to `g`, opened in `before_request` and closed in `teardown`. Never share a session across concurrent tasks — sessions are not safe for concurrent use.
- Avoid implicit lazy-loading after the session/await boundary (it raises `MissingGreenlet`). Eager-load what a response needs with `selectinload(...)`, or keep access inside the `async with session` block.
- Keep the schema Postgres-portable: the dev driver is `aiosqlite`, the prod driver is `asyncpg`. Avoid SQLite-only constructs so the same Alembic migrations apply to both.

### Testing

- **In-memory async SQLite needs `StaticPool` and a single shared connection**, otherwise each session gets a fresh empty `:memory:` database and tests mysteriously see no tables. This is the #1 async-test gotcha.
- Async **SAVEPOINT-based rollback isolation** (the async analogue of the Flask `db_session` fixture) gives real per-test isolation without recreating the DB each test. Use `pytest-asyncio` with `asyncio_mode = "auto"` so `async def test_*` just works.
- Drive the app through `app.test_app()` (an async context manager) so `before_serving`/`after_serving` actually run during tests — important when background schedulers or shared clients are involved.
- Set the testing env var in `conftest.py` via `os.environ` BEFORE any app import — `pydantic-settings` reads env vars at import time.

### Settings

- `pydantic-settings` with `.env` support is the reliable configuration pattern. `SecretStr` for sensitive values (API keys, OAuth client secret, Gmail tokens) prevents accidental logging. `extra='ignore'` in `SettingsConfigDict` prevents crashes from unrecognized env vars.

### Background tasks

- For periodic work (e.g. polling Gmail for new listing emails), **APScheduler `AsyncIOScheduler`** running in-process is the lightest correct option: start it in `before_serving`, shut it down in `after_serving`, and have jobs use the same async engine/sessionmaker. Only graduate to Celery/RQ when you need a separate worker fleet, durable queues, or multi-process scale.
- Make scheduled jobs idempotent and overlap-safe (a slow run shouldn't stack on the next tick) — set `max_instances=1` / `coalesce=True`.

### Frontend

- Server-rendered Jinja2 + Bootstrap (CDN) is the fastest path to a presentable UI. In Quart remember `await render_template(...)`. Migration path if it outgrows server rendering: (1) HTMX for progressive interactivity, (2) a JS framework for specific views, (3) full SPA only if the whole app is highly interactive.
- **Purchased Bootstrap themes are design guides, not code imports** — extract design tokens (colors, typography, spacing, component shapes) and generate clean project-specific CSS; never copy the bloated theme package. Reference only the single framework version matching the stack.
- **The CSS approach decision is not deferrable** — Tailwind vs Bootstrap produces fundamentally different HTML. Resolve it in the architectural discussion, not the first sprint.

---

## Debugging

> The **stack-specific half** of [`../workflow_error_debugging.md`](../workflow_error_debugging.md). That workflow holds the stack-agnostic method (read the error → categorize → locate → check recent changes → fix → verify, plus the 2-attempt escalation rule); this section holds the Quart/async-specific error tables, scenarios, and commands. Debugging this stack centers on async boundaries, the dev server, async SQLAlchemy sessions, Alembic migrations, Jinja2 templates, route/request errors, and external integrations (e.g. the Gmail API).

### Quick reference

| Resource | Command / Path |
|----------|---------------|
| Run all tests | `uv run pytest tests/ -v` |
| Run specific test | `uv run pytest tests/path/to/test_file.py::test_function -v` |
| Run with stdout shown | `uv run pytest tests/ -v -s` |
| Stop at first failure | `uv run pytest tests/ -x --tb=short` |
| Lint | `uv run ruff check .` |
| Dev server | `uv run quart --app run:app run --debug` (app factory `create_app()`) |
| Dev server log | `logs/dev_server.log` (if launched via the dev-server script) |
| Migration state | `uv run alembic current` / `uv run alembic history` |
| SQLite shell (inspect dev DB) | `sqlite3 <db_file>` then `.schema` |

### Where the error surfaces

| Source | Location |
|--------|----------|
| Test failure | Terminal output from `pytest` |
| Lint error | Terminal output from `uv run ruff check .` |
| Import error | Traceback at collection time (`pytest` fails before any test runs) |
| Request / 500 error | Dev server console or `logs/dev_server.log` (full traceback with `--debug`) |
| Template error | `jinja2.exceptions.*` (`TemplateNotFound`, `UndefinedError`) |
| DB error | `sqlalchemy.exc.*` / `sqlite3.OperationalError` |
| Async error | `RuntimeWarning: coroutine '...' was never awaited`, `RuntimeError: ... event loop`, a hung request |
| External / Gmail | `google.auth.*` / `googleapiclient.errors.HttpError` (401/403/429) |

### Error categories

| Category | Symptoms | Typical Cause |
|----------|----------|---------------|
| **ImportError** | `ModuleNotFoundError`, `cannot import name` | Missing dependency in `pyproject.toml`, circular import (common with `create_app` ↔ blueprints/models), typo in import path |
| **AttributeError** | `'X' object has no attribute 'Y'` | Renamed model attribute, wrong variable, module shadowing |
| **Async boundary** | `coroutine was never awaited`, request hangs, `event loop is already running` | A missing `await`, blocking I/O (sync `requests`, blocking DB driver, `time.sleep`) on the event loop, or starting a new loop inside a running one |
| **Quart / routing** | 404 on a route that should exist, 405, `working outside of request/app context` | Blueprint not registered, wrong URL rule, accessing `request`/`g` outside a context, sync view doing blocking work |
| **Template (Jinja2)** | `TemplateNotFound`, `UndefinedError`, blank/garbled page | Wrong template path/name, variable not passed to `render_template`, autoescape on raw HTML |
| **Database (async SQLAlchemy)** | `sqlalchemy.exc.*`, `MissingGreenlet`, `no such column`, locked DB | Using a sync session in async context, lazy-load outside a session, schema/migration drift, WAL contention |
| **Migration (Alembic)** | `Target database is not up to date`, autogenerate empty/wrong | DB not upgraded (`alembic upgrade head`), model not imported into the migration env, non-portable SQLite-only construct |
| **Config / settings** | `ValidationError` from pydantic-settings, missing key | Env var not set (this project's env-var prefix — see [`../PROJECT_IDENTITY.md`](../PROJECT_IDENTITY.md)), missing `.env`, wrong type |
| **External / Gmail** | `HttpError 401/403/429`, OAuth refresh failure | Expired/missing token, scopes insufficient, rate-limited, secrets not loaded |

### Locate the source

**Python exceptions:** read the traceback bottom-to-top, find the first `app/` frame, open it at the indicated line. Check: is a value `None` that shouldn't be? Is a coroutine missing an `await`? Is the attribute name correct?

**Request / 500 errors:** reproduce with the dev server in `--debug` for the full interactive traceback; confirm the blueprint is registered in `create_app()` and the URL rule matches; check you're inside the right context (`request`, `g`, `current_app`) — Quart contexts are async-task-local.

**Async issues:** grep the failing path for sync I/O that blocks the loop (`requests`, blocking DB calls, `time.sleep`, heavy CPU) and move it to `await` / `asyncio.to_thread`/an executor; confirm every coroutine call is `await`ed (a stray un-awaited coroutine emits the `never awaited` warning and silently no-ops).

**Database / migration issues:** inspect the dev DB (`sqlite3 <db_file>` then `.schema`); check migration state (`uv run alembic current` vs `history`, run `upgrade head` if behind); reproduce against a throwaway/fixture DB, never important local data — and preserve any ingested raw payloads (e.g. raw Gmail/Zillow/Redfin email bytes), don't delete them to "clean up" a repro.

### Common scenarios

**A request hangs or logs "coroutine was never awaited"** — Almost always a missing `await` or blocking I/O on the event loop. Audit the view/service for synchronous network/DB/file calls and for coroutine calls used without `await`. Use `asyncio.to_thread(...)` (or an executor) for unavoidable blocking work.

**`sqlalchemy.exc.MissingGreenlet` / lazy-load errors** — You touched a lazily-loaded relationship outside an active async session, or mixed sync and async session APIs. Eager-load what the response needs (`selectinload`), or keep the work inside the `async with session` block. Use the async engine/session everywhere.

**`sqlite3.OperationalError: database is locked`** — SQLite + WAL has limited write concurrency. Usually a test or request left a session open, or two writers collided. Ensure sessions are closed (use the dependency/context manager), set a `busy_timeout`, and keep write transactions short.

**Alembic autogenerate produces an empty or wrong migration** — The model wasn't imported into the migration environment's metadata, so Alembic can't see it. Ensure all models are imported where `target_metadata` is defined, then re-run `uv run alembic revision --autogenerate -m "..."` and review the script before `upgrade head`. Avoid SQLite-only constructs so the migration stays Postgres-portable.

**`jinja2.exceptions.TemplateNotFound` / `UndefinedError`** — Check the template name/path relative to the templates folder and confirm every variable the template uses is passed to `render_template(...)`. For values that may be absent, guard in the template rather than relying on silent undefined.

**Gmail API returns 401/403/429** — 401/403: the OAuth token is expired/missing or scopes are insufficient — refresh the token and verify the requested scopes. 429: you're rate-limited — add backoff/retry and reduce request volume in the scheduled ingestion task. Never commit `client_secret*.json` / `token*.json` (they're git-ignored).

**pydantic-settings `ValidationError` at startup** — A required setting is missing or mistyped. Settings read from env (this project's env-var prefix — see [`../PROJECT_IDENTITY.md`](../PROJECT_IDENTITY.md)) and `.env`. Confirm the variable is present and correctly typed; copy `.env.example` to `.env` for local dev.

**Reading a 500 in the browser (debug mode)** — With the dev server in `--debug`, an unhandled exception renders an interactive traceback page in the browser — click a frame to inspect it, like Flask's Werkzeug debugger. The traceback also prints to the dev server console. **Never run debug mode in any shared/exposed environment** — the interactive console is a remote-code-execution risk.

**`AttributeError: module 'app' has no attribute 'X'` (module shadowing) / stale imports** — A local variable named `app` (or the package name) can shadow the module, and stale bytecode can mask a fix. Two checks: (1) inside the app package, don't reuse the package name as a local variable; (2) clear stale caches: `find . -type d -name __pycache__ -exec rm -rf {} +` then re-run.

### Quick diagnostic commands

```bash
# Tests + lint
uv run pytest tests/ -v --tb=short
uv run ruff check .

# Import sanity (fails fast if imports/circulars are broken)
uv run python -c "import app; print('app OK')"

# App factory sanity (does the app build?)
uv run python -c "from app import create_app; create_app(); print('create_app OK')"

# Async DB connectivity (engine connects + a trivial query runs)
uv run python -c "
import asyncio
from sqlalchemy import text
from app import create_app
from app.db import get_engine   # adapt to the actual accessor
async def main():
    create_app()
    async with get_engine().connect() as conn:
        await conn.execute(text('SELECT 1'))
    print('DB OK')
asyncio.run(main())
"

# Migration state
uv run alembic current
uv run alembic history

# Inspect the dev DB read-only
sqlite3 -readonly <db_file> "PRAGMA integrity_check;"
```

---

## Evolution Notes

When this document is updated (new patterns, deprecated approaches, lessons), add an entry to the "Last Reviewed" table at the top. This is a **fork** of the Flask tech-stack doc and is meant to evolve **independently** — do not try to keep one document covering both Flask and Quart. As real Quart projects are built, fold their lessons back here so downstream projects and post-sprint review agents can see what changed and when.
