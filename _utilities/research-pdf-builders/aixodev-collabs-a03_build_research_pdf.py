#!/usr/bin/env python3
"""aixodev-collabs-a03_build_research_pdf.py — Stage 1 of the `research-pdf` skill (project copy).

Customized for aixodev-collabs Phase 00 Research Activity 03 ("Stateless Turns &
the Agent-Native Group Chat"): an explicitly-ordered O'Reilly-style mini-book —
the README dispatch manifest as front matter, ten numbered chapters (ch01–ch10,
section labels "Chapter NN of 10"), then the consolidated sources-and-claims.md as
Appendix A. That shape is a *manifest* (like rethinking-fable_/aixovault_), not a
numeric analysis-NN glob, so section order comes from the GROUPS manifest below and
the build FAILS LOUD if any listed file is missing. The nested three-group TOC
presentation (group headers + indented entries) is borrowed from the book-tree
variant; the markdown engine, CSS design system, mermaid inlining, and cover/section
assembly are verbatim from the prior compendium builds. Three inline ```mermaid
diagrams live in ch01/ch05/ch07 — the vendored mermaid renders them offline, so
Stage 2 MUST keep --virtual-time-budget=15000.

Run with the repo-local markdown venv (bootstrap_pdfvenv.sh creates it):

    .venv/bin/python aixodev-collabs-a03_build_research_pdf.py
"""
import markdown, html as htmlmod, re, os

# ══ CONFIG — aixodev-collabs · P00 Research Activity 03 ══════════════════════
KICKER    = "AIXO.Dev &middot; aixodev-collabs &middot; Phase 00 Research Activity 03"
TITLE     = "Stateless Turns &amp; the Agent-Native Group Chat"
SUBTITLE  = "How stateless LLM conversations actually work &mdash; and the design of the Room, the ensemble successor"
OUT_HTML  = "/tmp/aixodev-collabs-a03-compendium.html"   # UNIQUE per project — avoid /tmp collisions!
BASE      = "/home/jstanforth/Code/AIXO.Dev/aixodev-collabs/_research/stateless_turns_and_agent_groupchat"
COVER_META = (
    "P00-A03 &middot; completed 2026-07-02<br>"
    "10 chapters + dispatch manifest + sources appendix<br>"
    "branch <code>claudecode/research/@claude/stateless-turns-agent-groupchat</code><br>"
    "Claude Fable 5 &middot; July 2026"
)
COVER_NOTE = ("An O'Reilly-style mini-book for senior Python architects: the verified physics of stateless, "
              "turn-by-turn LLM conversations across providers, then the design of the Room &mdash; the async, "
              "threaded, reaction-capable agent group chat that succeeds ensemble. Start with the Dispatch "
              "Manifest; ten chapters and the sources appendix follow.")

# Ordered section manifest, split into the three natural groups. Each entry is
# (relpath-from-BASE, sec_label). TOC label is taken from each file's first H1.
# The ten chapters' sec_labels are auto-numbered ("Chapter NN of 10").
CHAPTER_DOCS = [
    "ch01--the-stateless-turn.md",
    "ch02--prompt-caching-economics.md",
    "ch03--provider-state-ladders.md",
    "ch04--hypothesis-verdicts.md",
    "ch05--the-room-design.md",
    "ch06--reactions-and-signals.md",
    "ch07--turn-scheduling-and-attendance.md",
    "ch08--transport-analysis.md",
    "ch09--python-implementation-blueprint.md",
    "ch10--migration-and-evaluation.md",
]
_nc = len(CHAPTER_DOCS)
GROUPS = [
    ("Front Matter", [("README.md", "Dispatch Manifest")]),
    ("The Mini-Book", [(f, f"Chapter {i:02d} of {_nc}")
                       for i, f in enumerate(CHAPTER_DOCS, 1)]),
    ("Appendix", [("sources-and-claims.md", "Appendix A")]),
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
def slug(rel):
    return re.sub(r'[^a-z0-9]+', '-', os.path.splitext(rel)[0].lower()).strip('-') or 'sec'

# Build the ordered section list; FAIL LOUD if any manifest file is missing so the
# bundle is provably complete.
all_docs = [f for _, docs in GROUPS for f, _ in docs]
missing = [f for f in all_docs if not os.path.exists(os.path.join(BASE, f))]
if missing:
    raise SystemExit("MISSING manifest files (bundle would be incomplete):\n  " + "\n  ".join(missing))

# Flatten into sections + build a nested TOC (group header rows + indented entries).
sections = []       # (sid, toc_label, sec_label, html_body)
toc_items = []
for gtitle, docs in GROUPS:
    toc_items.append(f'<li class="toc-group"><b>{gtitle}</b></li>')
    for f, sec_label in docs:
        path = os.path.join(BASE, f)
        sid = slug(f)
        h1 = toc_from_h1(path)
        toc_items.append(f'<li>&nbsp;&nbsp;&nbsp;<a href="#{sid}">{h1}</a></li>')
        sections.append((sid, h1, sec_label, conv(path)))

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
.toc ol { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10pt; line-height: 1.65; padding-left: 1.4em; list-style: none; }
.toc li { margin: 0.12em 0; }
.toc li.toc-group { margin: 0.6em 0 0.15em -1.0em; color: #0b2e4f; font-size: 10.5pt; }
.toc a { color: #0b2e4f; }
"""

toc = "\n".join(toc_items)
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
<html lang="en"><head><meta charset="utf-8"><title>{TITLE} — {SUBTITLE}</title>
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
