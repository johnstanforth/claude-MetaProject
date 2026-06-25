#!/usr/bin/env python3
"""build_research_pdf.py (manifest variant) — Stage 1 of the `research-pdf` skill.

A curated, EXPLICITLY-ORDERED set of Markdown research docs -> ONE styled HTML file
(branded cover + auto TOC + sections), ready for Chrome headless --print-to-pdf.
Unlike the glob variant, the section order/labels come from the DOCS manifest below
(needed because this corpus mixes analysis-A01 / claude-external-N / codex-* names a
numeric glob can't order). Run with the markdown venv:

    /tmp/pdfvenv/bin/python /tmp/aixovault_build_research_pdf.py

CSS block copied verbatim from the prior compendium builds so all PDFs share one
design system. See SKILL.md for the Chrome command and rationale.
"""
import markdown, html as htmlmod, re, os

# ══ CONFIG — EDIT PER PROJECT ════════════════════════════════════════════════
KICKER    = "AIXO.Dev &middot; aixovault"
TITLE     = "aixovault"
SUBTITLE  = "Phase 00 &mdash; Public API Surface &amp; Extraction / Migration Design"
OUT_HTML  = "/tmp/aixovault-compendium.html"     # UNIQUE per project — avoid /tmp collisions!
BASE      = "/home/jstanforth/Code/AIXO.Dev/aixodev-aixovault/_specs_and_plans/_research/phase00_api_and_extraction"
COVER_META = (
    "Synthesis &nbsp;+&nbsp; Dispatch Manifest &nbsp;+&nbsp; 28-document research corpus<br>"
    "Twin-track &middot; Claude depth (13) + external (6) &middot; Codex breadth (7) + scorecard &amp; triage (2)<br>"
    "Owner-Gate ratification &middot; 2026-06-24"
)
COVER_NOTE = "The completed synthesis opens the document &mdash; its five Owner-Gate decisions await John&rsquo;s ratification; the dispatch manifest and the full 28-document twin-track corpus follow as the evidence behind it."

# Ordered section manifest: (filename, sec_label). TOC label is taken from each
# file's first H1. Synthesis LEADS (per the project owner). Pure prompt/brief
# process docs (CODEX_DISCOVERY_PROMPT.md, SYNTHESIS_BRIEF.md) are intentionally omitted.
DOCS = [
    ("synthesis.md",                              "Synthesis"),
    ("README.md",                                 "Dispatch Manifest"),
    ("analysis-A01--api-shape.md",                "Claude Depth &middot; Area A — API Surface"),
    ("analysis-A02--parseresult-contract.md",     "Claude Depth &middot; Area A — API Surface"),
    ("analysis-A03--registry.md",                 "Claude Depth &middot; Area A — API Surface"),
    ("analysis-B04--config-seam.md",              "Claude Depth &middot; Area B — Config Seam"),
    ("analysis-B05--logging-exceptions.md",       "Claude Depth &middot; Area B — Config Seam"),
    ("analysis-C06--claude-code-port.md",         "Claude Depth &middot; Area C — Extraction & Migration"),
    ("analysis-C07--storage-port.md",             "Claude Depth &middot; Area C — Extraction & Migration"),
    ("analysis-C08--pipeline-port.md",            "Claude Depth &middot; Area C — Extraction & Migration"),
    ("analysis-C09--web-grafts.md",               "Claude Depth &middot; Area C — Extraction & Migration"),
    ("analysis-C10--host-migration.md",           "Claude Depth &middot; Area C — Extraction & Migration"),
    ("analysis-D11--lossless-tests.md",           "Claude Depth &middot; Area D — Lossless Tests"),
    ("analysis-DM1--claude-ai-dataloss-audit.md", "Claude Depth &middot; Dispatch-More"),
    ("analysis-DM2--byte-first-raw-layer.md",     "Claude Depth &middot; Dispatch-More"),
    ("claude-external-1--api-di.md",              "Claude External Deep-Dive"),
    ("claude-external-2--lossless.md",            "Claude External Deep-Dive"),
    ("claude-external-3--formats.md",             "Claude External Deep-Dive"),
    ("claude-external-4--sqlite-archival.md",     "Claude External Deep-Dive"),
    ("claude-external-5--schema-evolution.md",    "Claude External Deep-Dive"),
    ("claude-external-6--secure-parsing.md",      "Claude External Deep-Dive"),
    ("codex-discovery-1--codex-api-di.md",        "Codex Discovery (breadth)"),
    ("codex-discovery-2--codex-lossless.md",      "Codex Discovery (breadth)"),
    ("codex-discovery-3--codex-formats.md",       "Codex Discovery (breadth)"),
    ("codex-discovery-4--sqlite-archival.md",     "Codex Discovery (breadth)"),
    ("codex-discovery-5--schema-evolution.md",    "Codex Discovery (breadth)"),
    ("codex-discovery-6--secure-parsing.md",      "Codex Discovery (breadth)"),
    ("codex-internal-extraction.md",              "Codex Internal Extraction"),
    ("MERGE_AND_TRIAGE.md",                       "Merge & Triage"),
    ("COMPARISON_SCORECARD.md",                   "Comparison Scorecard"),
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

# Build the ordered section list; FAIL LOUD if any manifest file is missing so the
# bundle is provably complete.
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
