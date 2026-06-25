# research-pdf-builders

Archived, project-specific **Stage-1 build scripts** for the `research-pdf` skill — kept for future reference and re-runs. Each script turns a curated set of Markdown research docs into ONE styled, self-contained HTML file (branded cover + auto table-of-contents + per-doc sections); Chrome headless then prints that HTML to the final PDF under `_generated/`. The canonical recipe, the design-system CSS, the venv/Chrome prerequisites, and the maintenance notes all live in [`../../_skills/research-pdf/SKILL.md`](../../_skills/research-pdf/SKILL.md) — these files are the concrete, already-run *instances*, not the source of truth.

## The two-stage pipeline

```bash
# Stage 1 — Markdown -> one styled HTML file (needs the throwaway markdown venv at /tmp/pdfvenv;
#           recreate it per SKILL.md "Prerequisites" if /tmp was cleared):
/tmp/pdfvenv/bin/python <script>.py            # writes the /tmp/<project>-compendium.html named in its CONFIG

# Stage 2 — HTML -> PDF (Chrome's Blink engine renders the CSS, then prints):
google-chrome --headless --no-sandbox --disable-gpu --virtual-time-budget=15000 \
  --no-pdf-header-footer --print-to-pdf=/abs/out/<Name>.pdf file:///tmp/<project>-compendium.html
```

## Scripts here

| Script | Project / run | Variant | Sections |
|--------|---------------|---------|----------|
| `aixovault_build_research_pdf.py` | aixovault (AIXO.Dev) — Phase 00 API & extraction | **manifest** | 30 (synthesis leads) |
| `dailyspikedriver_build_research_pdf.py` | FracRealHomes · DailySpikeDriver — Phase 00 landscape survey | **manifest** | 22 (pre-synthesis) |

**"Manifest" variant** — the section order and per-section labels come from an explicit `DOCS = [(filename, label), …]` block in the CONFIG, instead of from a numeric `analysis-*.md` glob (the canonical skill's default). Reach for it when a corpus mixes naming schemes a numeric glob can't order — here: `analysis-A01`, `claude-external-N`, `codex-*`, plus scorecards and triage docs. The script **fails loud** if any manifest file is missing, so a built bundle is provably complete.

## Reusing one

Copy a script, edit the CONFIG block at the top (`KICKER` / `TITLE` / `SUBTITLE` / `BASE` / `OUT_HTML` / `COVER_META` / `COVER_NOTE`) and the `DOCS` manifest, then run the two stages above. The CSS block (the design system) is copied verbatim across every builder; palette-swap the navy `#0b2e4f` and its three companion tints to re-brand.

> The paths inside these scripts are project-specific (absolute `BASE`, `/tmp` `OUT_HTML`) and reflect the exact run that produced the committed PDFs — they are reference copies, not generic tools. The shared boilerplate (CSS + markdown engine + mermaid + cover/TOC machinery) is duplicated into each file on purpose, so any one script is self-contained and runnable in isolation.
