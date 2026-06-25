#!/usr/bin/env python3
"""build_research_pdf.py — Stage 1 of the `research-pdf` skill.

Markdown research docs -> ONE styled HTML file (branded cover + auto TOC + sections),
ready for Chrome headless `--print-to-pdf`. Run with the markdown venv:

    /tmp/pdfvenv/bin/python /tmp/<project>_build_research_pdf.py

Mermaid diagrams render automatically: ```mermaid fences become real SVG diagrams
in the PDF, offline, via a vendored mermaid.js (see "MERMAID" below). EDIT the CONFIG
block per project. The CSS block IS the design system (palette-swap the navy to re-brand).
See SKILL.md for the full recipe, the Chrome command, and the rationale.
"""
import markdown, html as htmlmod, glob, re, os

# ══ CONFIG — EDIT PER PROJECT ════════════════════════════════════════════════
KICKER    = "AIXO.Dev &middot; Workgroups"     # small uppercase line above the cover title
TITLE     = "Phase 00 Foundations"             # big cover wordmark
SUBTITLE  = "Foundations for an external deterministic state server &mdash; the context-preservation scratchpad"
OUT_HTML  = "/tmp/aixodev-workgroups-compendium.html"  # UNIQUE per project — avoid /tmp collisions!
COVER_META = (                                 # free HTML under the cover rule; <br> between lines
    "Synthesis &nbsp;+&nbsp; Research Plan &amp; Dispatch Manifest &nbsp;+&nbsp; 45 analyses<br>"
    "Phase 00 Research (Ideation &amp; Research) &middot; ~198K words<br>"
    "Synthesis complete &middot; 2026-06-18"
)
COVER_NOTE = "The decision-grade synthesis opens the document, followed by the Research Plan &amp; Dispatch Manifest; the 45 analyses follow as deep-dives."

# Research source dir(s). BASE holds RESEARCH_PLAN.md, README.md and analysis-*.md.
# APPX unused here (appendices empty); front matter is prepended in the section block.
BASE = "/home/jstanforth/Code/AIXO.Dev/aixodev-workgroups/_specs_and_plans/_research/workgroups_foundations"
APPX = BASE
APPENDICES = [                                 # (toc_label, sec_label, filename-in-APPX) — optional
]
# Worked example — the AdVentureGPS run this skill was distilled from:
#   KICKER  = "KingStrat &middot; Kingmaker Strategic Venture Partners"
#   TITLE   = "AdVentureGPS";  SUBTITLE = "Entity Model &amp; Graph-Database Research"
#   BASE = ".../kingstrat-adventuregps/_specs_and_plans/_research/entity_model_and_graph_db"
#   APPX = ".../kingstrat-adventuregps/_specs_and_plans/phase_00--ideation_and_research"
#   APPENDICES = [("Appendix A &middot; Entity Model Draft Spec", "Appendix A", "ENTITY_MODEL_DRAFT_SPEC.md"),
#                 ("Appendix B &middot; Platform Vision &amp; Federation", "Appendix B", "DIVIA_PLATFORM_VISION_AND_FEDERATION.md")]
# ══ END CONFIG ═══════════════════════════════════════════════════════════════

# Markdown engine: superfences (replaces fenced_code) so ```mermaid fences become
# <pre class="mermaid"> for the renderer; the rest of 'extra' is kept explicitly.
def _mermaid_fence(source, language, css_class, options, md, **kwargs):
    return f'<pre class="mermaid">{htmlmod.escape(source)}</pre>'

EXTS = ['abbr', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'tables',
        'sane_lists', 'pymdownx.tilde', 'pymdownx.superfences', 'toc']
EXT_CFG = {'pymdownx.superfences': {'custom_fences': [
    {'name': 'mermaid', 'class': 'mermaid', 'format': _mermaid_fence}]}}
md = markdown.Markdown(extensions=EXTS, extension_configs=EXT_CFG, output_format='html5')

def conv(path):
    md.reset()
    with open(path, encoding='utf-8') as f:
        return md.convert(f.read())
def first_h1(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return re.sub(r'\s+', ' ', line[2:].strip())
    return os.path.basename(path)

# Build the ordered section list: (section_id, toc_label, sec_label, html_body).
# Default shape: synthesis first -> numbered analyses -> appendices. Missing
# optional files are skipped, so this adapts to any project's doc layout.
sections = []
# Front matter: the decision-grade synthesis LEADS, then Research Plan + Dispatch Manifest, BEFORE the analyses.
FRONT = [
    ("synthesis", "Synthesis &mdash; Decision-Grade Integration", "Synthesis", f"{BASE}/synthesis.md"),
    ("research-plan", "Research Plan &amp; Scope", "Research Plan &amp; Scope", f"{BASE}/RESEARCH_PLAN.md"),
    ("dispatch-manifest", "Dispatch Manifest &amp; Status", "Dispatch Manifest &amp; Status", f"{BASE}/README.md"),
]
for _sid, _toc, _sec, _path in FRONT:
    if os.path.exists(_path):
        sections.append((_sid, _toc, _sec, conv(_path)))
analyses = sorted(glob.glob(f"{BASE}/analysis-*.md"),
                  key=lambda p: int(re.search(r'analysis-(\d+)', p).group(1)))
total = len(analyses)
for a in analyses:
    n = int(re.search(r'analysis-(\d+)', a).group(1))
    label = first_h1(a).replace("Analysis:", "").strip()
    sections.append((f"a{n:02d}", f"{n:02d} &middot; {htmlmod.escape(label)}",
                     f"Research Analysis {n:02d} of {total}", conv(a)))
for toc_label, sec_label, fname in APPENDICES:
    p = f"{APPX}/{fname}"
    if os.path.exists(p):
        sid = re.sub(r'[^a-z0-9]+', '-', sec_label.lower()).strip('-')
        sections.append((sid, toc_label, sec_label, conv(p)))

if not sections:
    raise SystemExit("No source docs found — check BASE / APPX / APPENDICES in the CONFIG block.")

# ── CSS — the design system. Palette swap: replace the navy #0b2e4f and its
#    companion shades (#33506b, #c8d4df, #e8eef4) to re-brand; the rest stays. ──
CSS = """
@page { size: Letter; margin: 16mm 15mm 18mm 15mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; margin: 0; }
h1,h2,h3,h4,h5 { font-family: 'Helvetica Neue', Arial, sans-serif; line-height: 1.25; color: #0b2e4f; margin: 1.05em 0 0.4em; }
h1 { font-size: 19pt; border-bottom: 2px solid #0b2e4f; padding-bottom: 4px; }
h2 { font-size: 14.5pt; border-bottom: 1px solid #c8d4df; padding-bottom: 2px; }
h3 { font-size: 12.5pt; }
h4 { font-size: 11pt; color: #33506b; }
p { margin: 0.5em 0; }
a { color: #1264a3; text-decoration: none; }
strong { color: #14202b; }
code { font-family: Menlo, Consolas, monospace; font-size: 0.84em; background: #f2f4f7; padding: 1px 4px; border-radius: 3px; }
pre { background: #f6f8fa; border: 1px solid #dfe3e8; border-radius: 5px; padding: 8px 10px; white-space: pre-wrap; word-wrap: break-word; font-size: 8.4pt; line-height: 1.4; }
pre code { background: none; padding: 0; font-size: inherit; }
pre.mermaid { background: none; border: none; padding: 0; text-align: center; page-break-inside: avoid; }
pre.mermaid svg { max-width: 100%; height: auto; }
blockquote { margin: 0.6em 0; padding: 0.25em 0.9em; border-left: 3px solid #9bb4cc; background: #f4f7fa; color: #33414d; }
table { border-collapse: collapse; width: 100%; margin: 0.7em 0; font-size: 8.5pt; table-layout: auto; }
th, td { border: 1px solid #c2ccd6; padding: 4px 6px; text-align: left; vertical-align: top; word-break: break-word; overflow-wrap: anywhere; }
th { background: #e8eef4; font-family: 'Helvetica Neue', Arial, sans-serif; }
tr { page-break-inside: avoid; }
ul, ol { margin: 0.4em 0 0.4em 1.1em; padding-left: 0.8em; }
li { margin: 0.18em 0; }
hr { border: none; border-top: 1px solid #d0d7de; margin: 1em 0; }
.section { page-break-before: always; }
.sec-label { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 8pt; letter-spacing: 0.10em; text-transform: uppercase; color: #8595a4; margin-bottom: 2px; }
.cover { page-break-after: always; text-align: center; padding-top: 25%; }
.cover .kicker { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11pt; letter-spacing: 0.22em; text-transform: uppercase; color: #7a8a99; }
.cover h1 { font-size: 33pt; border: none; color: #0b2e4f; margin: 0.25em 0 0; }
.cover .sub { font-size: 15pt; color: #33506b; margin-top: 0.5em; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 400; }
.cover .rule { width: 38%; margin: 1.6em auto; border-top: 2px solid #0b2e4f; }
.cover .meta { font-size: 11pt; color: #556; font-family: 'Helvetica Neue', Arial, sans-serif; line-height: 1.9; }
.cover .note { margin-top: 2.4em; font-size: 9.5pt; color: #889; font-style: italic; font-family: Georgia, serif; }
.toc { page-break-after: always; }
.toc h1 { font-size: 17pt; }
.toc ol { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10pt; line-height: 1.65; padding-left: 1.4em; }
.toc li { margin: 0.12em 0; }
.toc a { color: #0b2e4f; }
"""

toc = "\n".join(f'<li><a href="#{sid}">{label}</a></li>' for sid, label, _, _ in sections)
body = "\n".join(
    f'<section class="section" id="{sid}"><div class="sec-label">{sec_label}</div>\n{html_body}\n</section>'
    for sid, _, sec_label, html_body in sections
)

# ── MERMAID — if any diagram is present, inline the vendored renderer (offline).
#    Render the PDF with `--virtual-time-budget=15000` so mermaid finishes first.
ndiagrams = body.count('class="mermaid"')
mermaid_block = ""
if ndiagrams:
    candidates = [
        os.path.expanduser("~/.claude/skills/research-pdf/vendor/mermaid.min.js"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor", "mermaid.min.js"),
        "/tmp/mermaid.min.js",
    ]
    mjs_path = next((p for p in candidates if os.path.exists(p)), None)
    if mjs_path:
        mjs = open(mjs_path, encoding="utf-8").read()
        mermaid_block = (f"<script>{mjs}</script>\n"
                         "<script>mermaid.initialize({ startOnLoad: true, theme: 'neutral' });</script>")
        print(f"mermaid: {ndiagrams} diagram(s); inlined {os.path.basename(mjs_path)} "
              f"({len(mjs):,} bytes). RENDER WITH --virtual-time-budget=15000.")
    else:
        print(f"WARNING: {ndiagrams} mermaid block(s) found but no vendored mermaid.min.js — "
              "they will print as raw text. Vendor it with:\n"
              "  curl -sS -o ~/.claude/skills/research-pdf/vendor/mermaid.min.js "
              "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js")

COVER = f"""
<div class="cover">
  <div class="kicker">{KICKER}</div>
  <h1>{TITLE}</h1>
  <div class="sub">{SUBTITLE}</div>
  <div class="rule"></div>
  <div class="meta">{COVER_META}</div>
  <div class="note">{COVER_NOTE}</div>
</div>"""
TOC = f'<div class="toc"><h1>Contents</h1><ol>{toc}</ol></div>'
doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{TITLE} — Research Compendium</title>
<style>{CSS}</style></head>
<body>
{COVER}
{TOC}
{body}
{mermaid_block}
</body></html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(doc)
print(f"HTML written: {OUT_HTML}  ({len(doc):,} bytes)")
print(f"Sections: {len(sections)}" + (f"  ·  mermaid diagrams: {ndiagrams}" if ndiagrams else ""))
