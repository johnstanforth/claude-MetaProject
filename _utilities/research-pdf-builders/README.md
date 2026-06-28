# research-pdf-builders

Archived, project-specific **Stage-1 build scripts** for the `research-pdf` skill — kept for future reference and re-runs. Each script turns a set of Markdown research docs into ONE styled, self-contained HTML file (branded cover + auto table-of-contents + per-doc sections); Chrome headless then prints that HTML to the final PDF under `_generated/`. The canonical recipe, the design-system CSS, the venv/Chrome prerequisites, and the maintenance notes all live in [`../../_skills/research-pdf/SKILL.md`](../../_skills/research-pdf/SKILL.md) — these files are the concrete, already-run *instances*, not the source of truth.

## The two-stage pipeline

```bash
# Stage 1 — Markdown -> one styled HTML file (needs the throwaway markdown venv at /tmp/pdfvenv;
#           recreate it per SKILL.md "Prerequisites" if /tmp was cleared):
/tmp/pdfvenv/bin/python <script>.py            # writes the /tmp/<project>-compendium.html named in its CONFIG

# Stage 2 — HTML -> PDF (Chrome's Blink engine renders the CSS, then prints):
google-chrome --headless --no-sandbox --disable-gpu --virtual-time-budget=15000 \
  --no-pdf-header-footer --print-to-pdf=/abs/out/<Name>.pdf file:///tmp/<project>-compendium.html
```

## The three variants

All five scripts share the same CONFIG-block + design-system-CSS + cover/TOC machinery; they differ only in **how the section list is assembled**:

- **glob** (the canonical skill default) — sections come from a numeric `analysis-*.md` glob, preceded by a small `FRONT` list of front-matter docs (synthesis, research plan, dispatch manifest). Best for a uniform `analysis-NN.md` corpus.
- **manifest** — sections come from an explicit `DOCS = [(filename, label), …]` block, and the script **fails loud** if any listed file is missing (so a built bundle is provably complete). Reach for it when a corpus mixes naming schemes a numeric glob can't order — e.g. `analysis-A01`, `claude-external-N`, `codex-*`, plus scorecards and triage docs.
- **H2-split** — splits ONE chaptered Markdown "book" on its top-level `##` headings (fence-aware, so `#`-comment lines inside ` ``` ` code fences are never mistaken for headings), one section per chapter, so a single long document gets a real chapter-level TOC.

## Scripts here

| Script | Project / run | Variant | Sections |
|--------|---------------|---------|----------|
| `aixodev-workgroups_build_research_pdf.py` | AIXO.Dev Workgroups — Phase 00 Foundations corpus | **glob** | 48 (synthesis + plan + manifest + 45 analyses) |
| `agentswarms_build_research_pdf.py` | Divia.AI AgentSwarms — agent-harness landscape corpus | **glob** | 37 (synthesis + plan + manifest + 34 analyses) |
| `aixovault_build_research_pdf.py` | aixovault (AIXO.Dev) — Phase 00 API & extraction | **manifest** | 30 (synthesis leads) |
| `dailyspikedriver_build_research_pdf.py` | FracRealHomes · DailySpikeDriver — Phase 00 landscape survey | **manifest** | 22 (pre-synthesis) |
| `workgroups-devplan_build_research_pdf.py` | AIXO.Dev Workgroups — DEV_PLAN developer build guide | **H2-split** | 17 (overview + 16 chapters/appendices) |
| `fuglysnippets_build_research_pdf.py` | MetaProject meta-research — Fugly-Snippets venture-precursor archaeology + GEN3-model question set | **H2-split** | 8 (overview + §1–§7) |

## Reusing one

Pick the variant that matches your corpus shape (above), copy that script, edit the CONFIG block at the top (`KICKER` / `TITLE` / `SUBTITLE` / `BASE` / `OUT_HTML` / `COVER_META` / `COVER_NOTE`, plus the `FRONT`/`DOCS`/`SRC` that the variant uses), then run the two stages above. The CSS block (the design system) is copied verbatim across every builder; palette-swap the navy `#0b2e4f` and its three companion tints to re-brand.

> The paths inside these scripts are project-specific (absolute `BASE`/`SRC`, `/tmp` `OUT_HTML`) and reflect the exact run that produced the committed PDFs — they are reference copies, not generic tools. The shared boilerplate (CSS + markdown engine + mermaid + cover/TOC machinery) is duplicated into each file on purpose, so any one script is self-contained and runnable in isolation.
