# `_REFERENCE/` — Reference material (committed docs + machine-local resources)

> Holds reference material for this project — **both** committed reference content (briefs, external specs, prior-art docs you want versioned with the repo) **and** machine-local, git-ignored resources (symlinks to sibling projects, binary assets, debug screenshots). The committed-vs-ignored split is enforced by the project `.gitignore`.

## What goes where

- **Committed reference content** — named subdirectories directly under `_REFERENCE/` (e.g. `_REFERENCE/PRODUCT_DEVELOPMENT/`, `_REFERENCE/<source-name>/`). Versioned with the repo. Use this for external specs, briefs, and prior-art you want kept alongside the code. Anything under `_REFERENCE/` that is **not** `_EXTERNAL/` or `_assets/` is committed by default.
- **`_REFERENCE/_EXTERNAL/`** — *git-ignored.* Machine-specific **symlinks** to sibling projects elsewhere under `~/Code/` (read-only references). Created per-project at instantiation; never committed, because the paths are machine-local. Treat everything reached through these symlinks as **read-only** unless explicitly directed otherwise (see the project's `CLAUDE.md` → Agent Rules). This directory is intentionally **not shipped** by the canonical template — create it when the project needs reference symlinks.
- **`_REFERENCE/_assets/`** — *git-ignored.* Scratch space for binary / large reference assets that must never be committed: downloaded references, large PDFs, generated artifacts.
  - **`_REFERENCE/_assets/_screenshots/`** — the standard drop-spot for debug / testing screenshots captured during a session. Shipped as an empty scaffold so every project has the directory ready; its contents are git-ignored.

## The gitignore rules that govern this directory

```
_REFERENCE/_EXTERNAL        # machine-local symlinks — never committed
_REFERENCE/_assets          # binary/scratch assets incl. _screenshots/ — never committed
```

Put versioned reference material in a **named subdirectory** under `_REFERENCE/`; put throwaway or machine-local material under `_EXTERNAL/` or `_assets/`.
