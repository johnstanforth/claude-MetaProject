#!/usr/bin/env python3
"""gridtransmit_build_research_pdf.py — Stage 1 of the `research-pdf` skill (project copy).

Customized for the GridTransmit Legacy Codebase Compendium: a nested 4-book layout
(README/TOC + 00_preface + NN_chapter per book) rather than the stock flat
synthesis.md + analysis-NN.md shape. Only the CONFIG + section-assembly block differ
from the canonical ~/.claude/skills/research-pdf/build_research_pdf.py; the markdown
engine, CSS design system, mermaid inlining, and cover/TOC/doc assembly are verbatim.
"""
import markdown, html as htmlmod, glob, re, os

# ══ CONFIG — GridTransmit compendium ═════════════════════════════════════════
KICKER    = "ExoDev.AI &middot; SensoryMQ / SensoryMQ.Cloud"
TITLE     = "The GridTransmit Compendium"
SUBTITLE  = "Four Legacy Repositories (2013–2015), Read for the SensoryMQ Reboot"
OUT_HTML  = "/tmp/gridtransmit-compendium.html"  # UNIQUE per project — avoid /tmp collisions
COVER_META = (
    "4 books &middot; 43 chapters &middot; ~97,700 words<br>"
    "Go &middot; Clojure &middot; Python / Django<br>"
    "Reverse-engineered for the SensoryMQ successor &middot; 2026-07-01"
)
COVER_NOTE = "Start with the Compendium Overview &amp; Cross-Repo Synthesis; the four books follow as deep-dives."

ANALYSIS_DIR = "/home/jstanforth/Code/GridTransmit/_analysis"
BOOKS = [
    ("01-gridcomm-go-server",        "1", "The GridComm Go Server"),
    ("02-cljdealer-clojure-adapter", "2", "cljdealer (Clojure)"),
    ("03-admin-billing",             "3", "Admin & Billing"),
    ("04-iskyspotter-django",        "4", "iSkySpotter (Django)"),
]
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
                return re.sub(r'\s+', ' ', line[2:].strip()).replace('`', '')
    return os.path.basename(path)

# ── Build the ordered section list for the nested 4-book compendium:
#    front-matter overview → (per book: Contents, Preface, chapters) → editorial appendix.
sections = []

overview = f"{ANALYSIS_DIR}/README.md"
if os.path.exists(overview):
    sections.append(("overview",
                     "Compendium Overview &amp; Cross-Repo Synthesis",
                     "Overview &middot; Cross-Repo Synthesis",
                     conv(overview)))

def chapter_files(bookdir):
    d = f"{ANALYSIS_DIR}/{bookdir}"
    ordered = []
    readme = f"{d}/README.md"
    if os.path.exists(readme):
        ordered.append(("TOC", readme))
    numbered = []
    for p in glob.glob(f"{d}/*.md"):
        m = re.match(r'(\d+)_', os.path.basename(p))
        if m:
            numbered.append((int(m.group(1)), p))
    for n, p in sorted(numbered):
        ordered.append((n, p))
    return ordered

for bookdir, bnum, btitle in BOOKS:
    bt = htmlmod.escape(btitle)
    for key, path in chapter_files(bookdir):
        h1 = htmlmod.escape(first_h1(path))
        if key == "TOC":
            sid = f"b{bnum}-toc"
            toc_label = f"<b>Book {bnum} &middot; {bt}</b> &mdash; Contents"
            sec_label = f"Book {bnum} of 4 &middot; {bt} &middot; Contents"
        elif key == 0:
            sid = f"b{bnum}-c00"
            toc_label = f"&nbsp;&nbsp;&nbsp;{bnum}.0 &middot; {h1}"
            sec_label = f"Book {bnum} of 4 &middot; {bt}"
        else:
            sid = f"b{bnum}-c{key:02d}"
            toc_label = f"&nbsp;&nbsp;&nbsp;{bnum}.{key} &middot; {h1}"
            sec_label = f"Book {bnum} of 4 &middot; {bt} &middot; Chapter {key}"
        sections.append((sid, toc_label, sec_label, conv(path)))

appx = f"{ANALYSIS_DIR}/_SHARED_CONTEXT.md"
if os.path.exists(appx):
    sections.append(("appendix-brief",
                     "Appendix &middot; Editorial Brief &amp; Shared Context",
                     "Appendix &middot; Editorial Brief",
                     conv(appx)))

if not sections:
    raise SystemExit("No source docs found — check ANALYSIS_DIR / BOOKS in the CONFIG block.")

# ── CSS — the design system (verbatim from the canonical skill script). ──
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
.toc ol { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10pt; line-height: 1.65; padding-left: 1.4em; list-style: none; }
.toc li { margin: 0.12em 0; }
.toc a { color: #0b2e4f; }
"""

toc = "\n".join(f'<li><a href="#{sid}">{label}</a></li>' for sid, label, _, _ in sections)
body = "\n".join(
    f'<section class="section" id="{sid}"><div class="sec-label">{sec_label}</div>\n{html_body}\n</section>'
    for sid, _, sec_label, html_body in sections)

# ── MERMAID — inline the vendored renderer offline when diagrams are present. ──
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
        print(f"WARNING: {ndiagrams} mermaid block(s) found but no vendored mermaid.min.js.")

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
