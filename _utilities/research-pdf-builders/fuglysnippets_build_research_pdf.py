#!/usr/bin/env python3
"""build_research_pdf.py (H2-split variant) — Stage 1 of the `research-pdf` skill.

ONE chaptered Markdown doc (ANALYSIS-fugly-snippets.md) -> ONE styled HTML file
(branded cover + auto chapter-TOC + per-chapter sections), ready for Chrome headless
--print-to-pdf. Splits a SINGLE document on its top-level '## ' headings (fence-aware,
so '#'-comments inside ```code``` are never mistaken for headings) so each section
(§1..§7 + the preamble Overview) becomes its own page-broken section with a real TOC
entry. Run with the markdown venv:

    /tmp/pdfvenv/bin/python <this-script>.py

See ../../_skills/research-pdf/SKILL.md for the Chrome command and rationale. The CSS
block below is copied verbatim from the other builders so the PDFs share one design
system. (Variant copied from workgroups-devplan_build_research_pdf.py, 2026-06-28.)
"""
import markdown, html as htmlmod, re, os

# ══ CONFIG — EDIT PER PROJECT ════════════════════════════════════════════════
KICKER    = "Kingmaker Strategic &middot; MetaProject Meta-Research"
TITLE     = "Fugly-Snippets Archaeology"
SUBTITLE  = "Venture-Precursor Map &amp; GEN3-Model Question Set"
OUT_HTML  = "/tmp/fuglysnippets-compendium.html"   # UNIQUE per project — avoid /tmp collisions!
SRC       = "/home/jstanforth/Code/_claude.MetaProject/_meta-research/revisiting_rethinking_personal_projects/ANALYSIS-fugly-snippets.md"
RUNHEAD   = "Fugly-Snippets Archaeology &middot; GEN3-Model Question Set"   # constant per-page section label (running header)
COVER_META = (                                 # free HTML under the cover rule; <br> between lines
    "Single analysis &middot; 55 snippet-dirs cataloged (2017&ndash;2024)<br>"
    "Revisiting / Rethinking Personal Projects &middot; drafted 2026-06-25"
)
COVER_NOTE = "Working scratchpad &mdash; Task 1 of 2; the GEN3-model doc follows once the question set stabilizes."
# ══ END CONFIG ═══════════════════════════════════════════════════════════════

# Markdown engine — identical to the corpus build script (superfences for mermaid).
def _mermaid_fence(source, language, css_class, options, md, **kwargs):
    return f'<pre class="mermaid">{htmlmod.escape(source)}</pre>'

EXTS = ['abbr', 'attr_list', 'def_list', 'footnotes', 'md_in_html', 'tables',
        'sane_lists', 'pymdownx.tilde', 'pymdownx.superfences', 'toc']
EXT_CFG = {'pymdownx.superfences': {'custom_fences': [
    {'name': 'mermaid', 'class': 'mermaid', 'format': _mermaid_fence}]}}
md = markdown.Markdown(extensions=EXTS, extension_configs=EXT_CFG, output_format='html5')

def conv_text(text):
    md.reset()
    return md.convert(text)

# ── Split the single book on top-level '## ' headings, FENCE-AWARE so that
#    '#'-prefixed comment lines inside ```code``` fences are never split on. ──
raw = open(SRC, encoding='utf-8').read()
preamble_lines, chunks = [], []          # chunks: list of (title, [lines])
cur_title, cur, in_fence = None, [], False
for ln in raw.split('\n'):
    s = ln.lstrip()
    if s.startswith('```') or s.startswith('~~~'):
        in_fence = not in_fence
        cur.append(ln); continue
    if not in_fence and ln.startswith('## '):
        if cur_title is None:
            preamble_lines = cur
        else:
            chunks.append((cur_title, cur))
        cur_title, cur = ln[3:].strip(), [ln]
    else:
        cur.append(ln)
if cur_title is None:
    preamble_lines = cur
else:
    chunks.append((cur_title, cur))

def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-') or 'sec'
def clean_label(t):
    return htmlmod.escape(t.replace('`', ''))

# Section list: (section_id, toc_label, sec_label, html_body). Preamble (the H1
# title + intro blockquote) leads as "Overview"; each chapter/appendix follows.
sections = []
pre_html = conv_text('\n'.join(preamble_lines).strip())
if pre_html.strip():
    sections.append(("overview", "Overview", RUNHEAD, pre_html))
for title, body_lines in chunks:
    sid = slug(title)
    sections.append((sid, clean_label(title), RUNHEAD, conv_text('\n'.join(body_lines))))

if not sections:
    raise SystemExit("No sections parsed — check SRC path / the '## ' heading structure.")

# ── CSS — copied verbatim from the corpus build script (shared design system). ──
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
<html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title>
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
