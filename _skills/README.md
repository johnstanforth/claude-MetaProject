# `_skills` — Cross-Project Claude Skills (source of truth)

Git-tracked **source** for Claude Code skills that are useful across many projects (not specific to one repo). Each skill is a directory containing a `SKILL.md` plus any bundled assets (scripts, templates).

## Source vs. deployed

Claude Code loads skills from `~/.claude/skills/<name>/`. That deployed location is **not** git-tracked. So each cross-project skill has two copies:

| Copy | Path | Edit here? | Git-tracked? |
|------|------|-----------|--------------|
| **Source** | `_skills/<name>/` (this dir) | **YES** — all changes here | Yes (MetaProject) |
| **Deployed** | `~/.claude/skills/<name>/` | NO — never edit directly | No |

## Deploy / redeploy

After editing a skill's source, copy the whole directory to the deployed path:

```bash
cp -r ~/Code/_claude.MetaProject/_skills/<name>/. ~/.claude/skills/<name>/
```

Then restart / reload the Claude session so the updated skill is picked up.

## Skills here

- **`research-pdf`** — generate a polished, tablet-ready PDF compendium from a set of Markdown research docs (branded cover + auto TOC + styled sections, with inline MermaidJS diagrams rendered to SVG **offline** via a vendored `vendor/mermaid.min.js`), via python-markdown + custom CSS rendered by Chrome headless. Invoke with `/research-pdf` or let it trigger on a PDF-export request.

## Note on propagation (the open meta-question)

This source→deploy `cp` is itself a small **manual migration step** — the same class of problem tracked in [`_backlog_TODOs/LATER-001`](../_backlog_TODOs/LATER-001-workflow-lineage-and-hybrid-formalization.md) (how workflow/skill revisions propagate consistently across 20+ projects). A globally-deployed skill sidesteps *per-repo* copying entirely (one deploy serves every project), but the source→deploy hop still wants a process. Until that's formalized, the rule is simply: **edit source here, redeploy with the `cp` above, don't edit the deployed copy.**
