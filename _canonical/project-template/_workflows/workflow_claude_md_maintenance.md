# Workflow: CLAUDE.md Maintenance

> How to keep the project guide accurate as the codebase evolves.

## Quick Reference

| Item | Value |
|------|-------|
| File | `CLAUDE.md` (project root) |
| Target length | Under 500 lines (Anthropic recommends <200; our project complexity justifies more) |
| Update triggers | Schema changes, new dependencies, architecture changes, convention changes |
| Verification | Compare documented state to actual codebase |

---

## Overview

`CLAUDE.md` is the primary context document that every Claude session reads. If it is inaccurate, every session starts with wrong assumptions. Keeping it accurate is a maintenance task that should happen regularly, not just when problems arise.

The document serves two audiences:
1. **Claude instances** — need accurate technical details to make correct decisions
2. **Human developers** — need a reliable overview of the project's architecture and conventions

---

## When to Update CLAUDE.md

| Trigger | What to Update |
|---------|---------------|
| New model or table added | Database Schema section, model table |
| Model field renamed or removed | Database Schema section, Key Design Notes |
| New dependency added | Tech Stack section |
| Dependency version bumped significantly | Tech Stack section (exact versions) |
| New external integration added (e.g. Gmail API) | External Integrations / Architecture section |
| New public API function/class | Public API section, Architecture section |
| New CLI command added | Quick Start section |
| Convention changed (naming, patterns, etc.) | Conventions section |
| New environment variable required | Environment Variables section |
| New known issue discovered | Known Issues / Gotchas section |
| New workflow or tooling added | Key File Locations, relevant section |
| Dev phase completed | Development Phases table |
| Project structure changed | Project Structure tree |

---

## Step-by-Step

### Step 1: Identify What Changed

Check what has changed since the last CLAUDE.md update:

```bash
# When was CLAUDE.md last modified?
git log --oneline -1 -- CLAUDE.md

# What changed since then?
git log --oneline {last_claude_md_commit}..HEAD

# Any new files in key directories?
ls app/models/
ls app/api/
ls app/views/
ls app/services/
```

### Step 2: Section-by-Section Review

Go through each major section of CLAUDE.md and verify accuracy:

#### Tech Stack
- [ ] Python version matches: `python3.12 --version`
- [ ] uv version matches: `uv --version`
- [ ] Key package versions match: check `pyproject.toml` or `uv pip list`
- [ ] SQLite version matches: `sqlite3 --version`
- [ ] Node.js version matches: `node --version`
- [ ] All listed dependencies still exist in `pyproject.toml`
- [ ] No new significant dependencies are missing from the list

#### Quick Start
- [ ] All commands work as documented
- [ ] Prerequisites are still accurate
- [ ] Database name and user are correct

#### Architecture
- [ ] Blueprint count matches: count files in `app/api/` and `app/views/`
- [ ] App factory description is accurate
- [ ] Config description matches `app/settings.py` and `app/config.py`

#### Database Schema
- [ ] Table count matches: count model classes in `app/models/`
- [ ] Model file table is accurate (all files listed, all models listed)
- [ ] Key design notes are still true
- [ ] Migration file reference is correct (or updated if new migrations exist)

#### Roles and Permissions
- [ ] Role hierarchy is accurate
- [ ] Decorator names and behavior match source code

#### Project Structure
- [ ] Directory tree matches actual filesystem
- [ ] File descriptions are accurate
- [ ] No new significant files are missing

#### Development Phases
- [ ] Phase table reflects current state (status, directory names)
- [ ] Active phase is marked correctly

#### External Integrations
- [ ] All external services (e.g. the Gmail API) are listed with status
- [ ] Required scopes/credentials and env vars are documented
- [ ] Rate-limit / retry / error-handling behavior is noted

#### Conventions
- [ ] All documented conventions still hold
- [ ] No new conventions are missing
- [ ] Import patterns are accurate
- [ ] Auth decorator behavior is accurately described

#### Environment Variables
- [ ] All required variables are listed
- [ ] Default values are correct
- [ ] New variables are documented
- [ ] Removed variables are cleaned up

#### Known Issues / Gotchas
- [ ] All listed issues are still relevant
- [ ] No new gotchas have been discovered that are not listed
- [ ] Workarounds are still accurate

### Step 3: Make Updates

Edit CLAUDE.md to reflect the current state. Follow these principles:

**Be precise.** Wrong information is worse than missing information. If you are unsure about a detail, verify it before writing.

**Be concise.** Every line in CLAUDE.md competes for context window space. Remove information that is no longer relevant. Do not add paragraphs where a bullet point suffices.

**Use tables.** Tables are more scannable than prose for reference information (versions, file paths, endpoint lists).

**Update, do not append.** When a version changes, update the existing line. Do not add "Updated on {date}" annotations — the git history tracks that.

### Step 4: Verify Against Actual Codebase

After making edits, verify key claims:

```bash
# Verify the app builds (app factory imports cleanly)
uv run python -c "
from app import create_app
create_app()
print('app create_app OK')
"

# Verify registered blueprints / routes
grep -rn "register_blueprint" app/ 2>/dev/null

# Verify tech versions
python3 --version
uv --version

# Verify config/env keys are documented
grep -rE "<ENV_PREFIX>[A-Z_]+" app/ 2>/dev/null    # <ENV_PREFIX>: this project's env prefix (see _workflows/PROJECT_IDENTITY.md)
```

### Step 5: Check Document Length

```bash
wc -l CLAUDE.md
```

Target: under 500 lines. If the document is growing beyond this:
- Move detailed reference information to separate files
- Link to those files from CLAUDE.md
- Keep CLAUDE.md focused on what Claude needs for day-to-day development

Anthropic's recommendation is under 200 lines for most projects. A focused web app like this project's should comfortably stay near that target; let CLAUDE.md grow only as the app's surface (models, blueprints, integrations) and phase history justify it, not indefinitely.

### Step 6: Commit

```bash
git add CLAUDE.md
git commit -m "P{NN}-S{NN}-T{NN} Update CLAUDE.md: {what changed}"
```

Or if done outside sprint context:
```bash
git commit -m "Update CLAUDE.md: {summary of changes}"
```

---

## Maintenance Schedule

| Frequency | Action |
|-----------|--------|
| Every sprint | Quick scan: did this sprint change anything CLAUDE.md documents? |
| Every phase | Full section-by-section review |
| After dependency updates | Update Tech Stack versions |
| After schema changes | Update Database Schema section |
| After new conventions | Update Conventions section |

---

## Related Workflows

- `workflow_start_new_sprint.md` — CLAUDE.md may need updating as part of sprint cleanup
- `workflow_sprint_closeout.md` — Compound Engineering Stage B (lessons capture) may update CLAUDE.md
- `workflow_compound_engineering.md` — CLAUDE.md is a primary destination for Compound Engineering findings
- `workflow_code_audit.md` — Findings may reveal CLAUDE.md inaccuracies
