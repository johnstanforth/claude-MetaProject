#!/usr/bin/env bash
# bootstrap_pdfvenv.sh — idempotently create/repair the repo-local markdown venv that
# the research-pdf skill's Stage-1 build scripts run under. Self-healing: re-run it any
# time the venv is missing or broken (e.g. a partial wipe). Needs network only when it
# actually has to (re)install the two pinned packages.
#
# Usage:
#   ./bootstrap_pdfvenv.sh                 # create/repair  -> _utilities/research-pdf-builders/.venv
#   .venv/bin/python <project>_build_research_pdf.py        # then run any Stage-1 builder
#
# ─────────────────────────────────────────────────────────────────────────────
# MIGRATION NOTE (2026-06-28): this venv lives INSIDE the repo (repo-local, git-ignored
# via the sibling .gitignore) ONLY because MetaProject is the current, in-flux hub where
# all research-pdf builds are orchestrated. It was moved out of /tmp/pdfvenv because /tmp
# kept getting cleared between sessions. When the real AIXO.Dev Platform takes over project
# management, RELOCATE this venv OUT of the repo (e.g. a ~/.cache home location) and delete
# this script + the sibling .gitignore. It is kept here deliberately as a VISIBLE reminder
# of that future cleanup — and to avoid creating external references that would need
# migrating later. (See ../../_skills/research-pdf/SKILL.md → Prerequisites.)
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$HERE/.venv"
PYBIN="${PYTHON:-python3}"

# Healthy already? (the exact failure mode we hit when /tmp was cleared: markdown present
# as an empty namespace package with no .Markdown attribute) -> nothing to do.
if [ -x "$VENV/bin/python" ] && \
   "$VENV/bin/python" -c "import markdown, pymdownx; assert hasattr(markdown, 'Markdown')" 2>/dev/null; then
  echo "OK: research-pdf venv healthy at $VENV"
  exit 0
fi

echo "Creating/repairing research-pdf venv at $VENV ..."
"$PYBIN" -m venv --clear "$VENV"
"$VENV/bin/pip" install --quiet 'Markdown==3.10.2' 'pymdown-extensions==10.21.3'
"$VENV/bin/python" -c "import markdown, pymdownx; print('venv ready:', '$VENV', '| markdown', markdown.__version__, '| has Markdown:', hasattr(markdown,'Markdown'))"
