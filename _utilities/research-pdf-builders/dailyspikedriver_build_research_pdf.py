#!/usr/bin/env python3
"""build_research_pdf.py (manifest variant) — Stage 1 of the `research-pdf` skill.

DailySpikeDriver Phase 00 pre-synthesis corpus -> ONE styled HTML file (branded
cover + auto TOC + sections). Section order/labels come from the DOCS manifest.
Run with the markdown venv:

    /tmp/pdfvenv/bin/python /tmp/dailyspikedriver_build_research_pdf.py

CSS copied verbatim from the prior compendium builds (one shared design system).
"""
import markdown, html as htmlmod, re, os

# ══ CONFIG — EDIT PER PROJECT ════════════════════════════════════════════════
KICKER    = "FracRealHomes &middot; DailySpikeDriver"
TITLE     = "DailySpikeDriver"
SUBTITLE  = "Phase 00 &mdash; Real-Estate Landscape Survey &amp; Feature Innovation"
OUT_HTML  = "/tmp/dailyspikedriver-compendium.html"   # UNIQUE per project — avoid /tmp collisions!
BASE      = "/home/jstanforth/Code/FracRealHomes/fracrealhomes-dailyspikedriver/_specs_and_plans/_research/phase00_gmail_and_listings"
COVER_META = (
    "Research Plan &amp; Dispatch Manifest &nbsp;+&nbsp; 13 analyses + 3 Codex passes + 4 scorecards<br>"
    "Phase 00 (Ideation &amp; Research) &middot; parity twin-track &middot; ~96K words<br>"
    "Owner Gate &mdash; pre-synthesis review &middot; 2026-06-24"
)
COVER_NOTE = "Corpus paused at the pre-synthesis Owner Gate for human review &mdash; synthesis pending. The Research Plan and Dispatch Manifest open the document; the 13 Claude depth analyses, 3 Codex parity passes, and 4 parity scorecards follow as the evidence to review."

# Ordered section manifest: (filename, sec_label). TOC label is each file's first H1.
# No synthesis yet (pre-synthesis gate). The machine-prompt doc (CODEX_PROMPTS.md) is omitted.
DOCS = [
    ("RESEARCH_PLAN.md",                          "Research Plan & Scope"),
    ("README.md",                                 "Dispatch Manifest"),
    ("analysis-01--gmail-api-full.md",            "Claude Depth &middot; Area A — Gmail & Ingestion"),
    ("analysis-02--ingestion-architecture.md",    "Claude Depth &middot; Area A — Gmail & Ingestion"),
    ("analysis-03--listing-email-parsing.md",     "Claude Depth &middot; Area A — Gmail & Ingestion"),
    ("analysis-04--oss-realestate-libs.md",       "Claude Depth &middot; Area B — Data Sourcing"),
    ("analysis-05--commercial-data-providers.md", "Claude Depth &middot; Area B — Data Sourcing"),
    ("analysis-06--photos-media-pipeline.md",     "Claude Depth &middot; Area B — Data Sourcing"),
    ("analysis-07--open-datasets.md",             "Claude Depth &middot; Area B — Data Sourcing"),
    ("analysis-08--feature-teardown.md",          "Claude Depth &middot; Area C — Features & UX"),
    ("analysis-09--discovery-ux-maps.md",         "Claude Depth &middot; Area C — Features & UX"),
    ("analysis-10--ai-llm-features.md",           "Claude Depth &middot; Area C — Features & UX"),
    ("analysis-11--wild-features.md",             "Claude Depth &middot; Area C — Features & UX"),
    ("analysis-12--listing-data-model.md",        "Claude Depth &middot; Area C — Features & UX"),
    ("analysis-13--quart-async-data-validation.md", "Claude Depth &middot; Area D — Async Foundations"),
    ("codex-area-a-gmail.md",                     "Codex Parity (breadth) &middot; Area A"),
    ("codex-area-b-data.md",                      "Codex Parity (breadth) &middot; Area B"),
    ("codex-area-cd-features.md",                 "Codex Parity (breadth) &middot; Area C+D"),
    ("COMPARISON_SCORECARD.md",                   "Comparison Scorecard &middot; Rollup"),
    ("COMPARISON_SCORECARD--area-a.md",           "Comparison Scorecard &middot; Area A"),
    ("COMPARISON_SCORECARD--area-b.md",           "Comparison Scorecard &middot; Area B"),
    ("COMPARISON_SCORECARD--area-cd.md",          "Comparison Scorecard &middot; Area C+D"),
]
# ══ END CONFIG ═══════════════════════════════════════════════════════════════

# Markdown engine — superfences so ```mermaid fences become <pre class="mermaid">.
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
                return line[2:].strip()
    return os.path.basename(path)
def toc_from_h1(path):
    return htmlmod.escape(re.sub(r'\s+', ' ', first_h1(path).replace('`', '')).strip())
def slug(fname):
    return re.sub(r'[^a-z0-9]+', '-', os.path.splitext(fname)[0].lower()).strip('-') or 'sec'

missing = [f for f, _ in DOCS if not os.path.exists(os.path.join(BASE, f))]
if missing:
    raise SystemExit("MISSING manifest files (bundle would be incomplete):\n  " + "\n  ".join(missing))
sections = [(slug(f), toc_from_h1(os.path.join(BASE, f)), sec, conv(os.path.join(BASE, f)))
            for f, sec in DOCS]

# ── CSS — the shared design system (palette: navy #0b2e4f + #33506b/#c8d4df/#e8eef4). ──
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

# ── MERMAID — inline the vendored renderer offline if any diagram is present. ──
ndiagrams = body.count('class="mermaid"')
mermaid_block = ""
if ndiagrams:
    candidates = [
        os.path.expanduser("~/.claude/skills/research-pdf/vendor/mermaid.min.js"),
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
        print(f"WARNING: {ndiagrams} mermaid block(s) but no vendored mermaid.min.js — will print as raw text.")

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
