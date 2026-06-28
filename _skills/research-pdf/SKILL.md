---
name: research-pdf
description: Generate a polished, tablet-ready PDF compendium from a set of Markdown research/analysis docs — branded cover, auto table of contents, and styled sections — using python-markdown + custom CSS rendered by Chrome headless (no pandoc/LaTeX needed). Use when the user asks to export research, analyses, a synthesis, or a report as a nicely-formatted PDF for reading on a tablet or printing.
---

# research-pdf — tablet-ready research PDF compendium

Turn a set of Markdown research docs into ONE polished, consistently-branded PDF (cover → table of contents → sections) that's comfortable to read on a tablet or print. This skill is the single canonical recipe; its source lives in MetaProject (`_skills/research-pdf/`) and is deploy-copied to `~/.claude/skills/research-pdf/` — see "Maintenance" at the end.

## When to use

- The user asks for a PDF export of research / analyses / a synthesis / a report — anything where reading dozens of Markdown files in a terminal is painful.
- You have one or more Markdown source docs. The canonical shape is `synthesis.md` + `analysis-NN.md` ×N + appendices, but any ordered set works.
- The goal is a document that looks *designed* — not a raw `md`-dump.

## The pipeline (two stages)

```bash
# Stage 1 — Markdown -> one styled HTML file (uses the markdown venv):
/tmp/pdfvenv/bin/python /tmp/<project>_build_research_pdf.py     # writes /tmp/<project>-compendium.html

# Stage 2 — HTML -> PDF (Chrome's Blink engine renders the CSS, then prints):
google-chrome --headless --no-sandbox --disable-gpu \
  --virtual-time-budget=15000 \
  --no-pdf-header-footer \
  --print-to-pdf=/abs/path/<Project>_Research-Compendium.pdf \
  file:///tmp/<project>-compendium.html
```

(`--virtual-time-budget=15000` lets Chrome finish rendering any mermaid diagrams before printing; it's harmless when there are none, so it's always in the command.)

That's the entire mechanism. The polish lives in the CSS inside the Stage-1 script; Chrome contributes the best-in-class CSS renderer and a clean print-to-PDF path.

## Prerequisites (one-time)

- **Google Chrome** — expected at `/usr/bin/google-chrome` (verified Chrome 149; `google-chrome-stable` is the same binary). Nothing to install.
- **The markdown venv** — a tiny venv with `Markdown` + `pymdown-extensions`. When building from the **MetaProject build hub** it's persisted **repo-local** at `_utilities/research-pdf-builders/.venv` and created/repaired by that dir's idempotent **`bootstrap_pdfvenv.sh`** — run it once, or any time the venv is lost. (It used to live at `/tmp/pdfvenv`, but `/tmp` kept getting cleared between sessions, which silently turns `markdown` into an empty namespace package with no `.Markdown` attribute. The repo-local spot is a deliberate stopgap with a MIGRATION NOTE — relocate it out of the repo once the real platform owns project management.) The underlying recipe, if you ever build the venv by hand at any path:

```bash
python3 -m venv <venv-dir>            # e.g. _utilities/research-pdf-builders/.venv  (or /tmp/pdfvenv ad-hoc)
<venv-dir>/bin/pip install --quiet 'Markdown==3.10.2' 'pymdown-extensions==10.21.3'
```

- **Mermaid** (diagram rendering) — a vendored `vendor/mermaid.min.js` (mermaid@11, ~3.3 MB) ships **inside this skill**, so ```` ```mermaid ```` diagrams render **offline** with nothing to install. The build script auto-inlines it whenever a doc contains mermaid blocks. (To refresh: `curl -sS -o vendor/mermaid.min.js https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js`.)

## How to run it

1. **Copy the bundled script to a project-unique `/tmp` path** (this skill ships `build_research_pdf.py` alongside this file). Name it per-project — e.g. `cp <skill-dir>/build_research_pdf.py /tmp/<project>_build_research_pdf.py` — so parallel sessions never clobber each other.
2. **Edit the CONFIG block** at the top of that copy: `KICKER`, `TITLE`, `SUBTITLE`, `COVER_META`, `COVER_NOTE`, the source `BASE`/`APPX` paths, and the `APPENDICES` list. A worked example (the AdVentureGPS run) is in the comments. Set `OUT_HTML` to a project-unique name too.
3. **Run Stage 1** with the venv; it prints the output path, byte size, and section count. Sanity-check the count.
4. **Run Stage 2** (the Chrome command above) to produce the PDF.
5. **Hand the PDF path to the user. Do NOT git-commit the PDF** (often 10–20 MB; repos carry `*.pdf` in `.gitignore`).

## The design system (the "magic")

- **Typography:** **Georgia** serif body (easy long-form reading) + **Helvetica Neue/Arial** sans headings/tables/TOC/cover. System fonts only — instant, deterministic, offline. This serif-body / sans-heading split is the biggest reason it reads designed rather than web-dumped.
- **Brand palette:** one deep navy (`#0b2e4f`) for headings, rules, and the cover, with three companion tints (`#33506b`, `#c8d4df`, `#e8eef4`). Re-brand by swapping those four hexes in the CSS.
- **Print-safe tables:** collapsed borders, tinted sans header row, `8.5pt`, cell `word-break`/`overflow-wrap`, and `page-break-inside: avoid` on rows — wide research tables wrap instead of overflowing and don't split across pages.
- **Structure:** a standalone branded **cover**, an **auto-generated clickable TOC** (built from the section list, so it can't drift), and each source doc as a `<section>` with `page-break-before: always` topped by a small grey **section label** ("Research Analysis 07 of 47", "Appendix B").
- **`print-color-adjust: exact`** forces Chrome to honor background fills (table headers, code, quotes) that browsers otherwise drop when printing.
- **Mermaid diagrams render to real SVG.** A ```` ```mermaid ```` fence becomes `<pre class="mermaid">` (via a `pymdownx.superfences` custom fence); the vendored mermaid.js runs inside the same Chrome pass and replaces it with a diagram. Offline and deterministic (pinned mermaid@11). Diagrams are centered and capped at page width, and avoid splitting across a page break.

## Why Chrome + CSS (and the pandoc question)

The output looks "next-level" because the whole document is laid out in **CSS, rendered by Chrome's Blink engine** (the most complete CSS-for-print renderer there is). For *designed, branded reading documents* this is genuinely the right tool, not a fallback.

- **Pandoc's default** route uses **LaTeX** (needs a multi-GB TeX install). Superb typesetting (math, footnotes, bibliographies), but page *design* is governed by LaTeX templates — a steeper, less web-friendly idiom for a custom cover and web-style tables. Fonts are actually easy in pandoc; the friction is the overall design system.
- **Pandoc's HTML engines** (`--pdf-engine=weasyprint` / `wkhtmltopdf`) are closer to this approach but their CSS support trails Chrome's (weasyprint by a notch, wkhtmltopdf by a decade).
- **Install pandoc only if** a future need appears that Chrome can't serve well: (a) academic-grade math/citations; (b) one-source export to `.docx`/`.epub`/slides (pandoc's real superpower); or (c) automatic **printed page numbers / running headers** — the one honest gap in the Chrome approach (Chrome headless can't render CSS Paged-Media margin boxes, so these PDFs deliberately have no page numbers and rely on the clickable TOC). The lightweight way to experiment with page numbers is `pip install weasyprint` in the same venv — no TeX.

## Gotchas

- **`/tmp` filename collisions across concurrent sessions are real.** Multiple sessions share `/tmp`; generic names like `/tmp/build_research_pdf.py` collide (observed 2026-06-16: another session's `aixodev-collabs` build occupied that exact name). Always **Read a `/tmp` path before Writing it** and **suffix temp artifacts per project**.
- **`file://` needs an absolute path** with three slashes (`file:///tmp/...`).
- **Both stages are idempotent** — re-run after editing any source doc.
- **Harmless Chrome log noise:** `PHONE_REGISTRATION_ERROR` / GCM / `Failed to log in to GCM` lines are Chrome phoning home; they don't affect the PDF.
- **Letter is the default** paper size (US). For A4, change `@page { size: Letter }` → `A4` in the CSS (not via a Chrome flag, so the HTML preview and PDF agree).
- **Mermaid renders automatically** (on by default, vendored offline) — no action needed. If the build script prints `WARNING: … no vendored mermaid.min.js`, the `vendor/` asset is missing; re-fetch it with the curl in Prerequisites. **Authoring convention:** diagrams in research docs are authored as **inline mermaid only** — no ASCII-art companion files (the PDF and GitHub both render mermaid; see the MetaProject Documentation Conventions).
- **No soft-wrapped lines** in source Markdown (cross-project Documentation Convention): one unbroken line per paragraph/list-item.

## Verify

- Stage 1 prints `HTML written: ... (N bytes)` and the section count — confirm it matches your doc set.
- Stage 2 prints `<bytes> written to file ...` and exits 0.
- Optional: `pdfinfo OUT.pdf` → `Pages`, `Page size: ... (letter)`, `Producer: Skia/PDF` (Chrome's engine).
- Eyeball the first pages: cover alone, TOC on its own page, first section fresh with its grey label.

## Provenance & maintenance

- **Distilled from** the AdVentureGPS "Entity Model & Graph-DB Research" compendium (2026-06-15): 48 docs (1 synthesis + 47 analyses + 2 appendices) → **522 pages, 16,104,520 bytes**, Letter, `Skia/PDF m149`, built in ~6 s. Toolchain: Chrome 149, `Markdown==3.10.2`, `pymdown-extensions==10.21.3`.
- **Source of truth:** `~/Code/_claude.MetaProject/_skills/research-pdf/` (git-tracked: `SKILL.md`, `build_research_pdf.py`, `vendor/mermaid.min.js`). **After editing the source, redeploy** by copying the whole directory to `~/.claude/skills/research-pdf/` (the deployed copy is NOT edited directly; copying the directory carries `vendor/` along). See `_skills/README.md` for the convention.
