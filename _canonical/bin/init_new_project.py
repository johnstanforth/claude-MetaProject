#!/usr/bin/env python3
"""init_new_project.py -- scaffold a new project from the canonical template.

The deterministic, mechanical first steps of the New Project workflow
(see ../NEW_PROJECT_GUIDE.md). Everything here is code you can vet and
git-commit, then improve over time. The non-deterministic, domain-aware
prose (the `<!-- AGENT: ... -->` blocks in the instantiated docs) is left
for a follow-up Claude/human pass.

What it does:
  1. Pick the owning Organization/umbrella (from the orgs already under
     ~/Code, or type a new one).
  2. Take a GitHub origin URL and parse the repo name from it. The repo
     name becomes the directory name. (No git remote is configured --
     house rule is local-only; the URL is recorded in genesis.json for
     later manual use.)
  3. mkdir ~/Code/<Org>/<repo>, rsync the canonical template in, `git init`.
  4. Collect the project manifest (identity + active techstack), with
     sensible defaults; write it to _research/genesis.json.
  5. Substitute every {{PLACEHOLDER}} across the instantiated files and
     strip the `<!-- TEMPLATE FILE ... -->` marker lines.
  6. Print the remaining (agent-written) steps.

Usage:
    python3 _canonical/bin/init_new_project.py [--dry-run]
                                               [--code-dir DIR]
                                               [--template-dir DIR]

Stdlib only. Prototype -- review before trusting.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# --- paths -------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent          # _canonical/bin
CANONICAL_DIR = SCRIPT_DIR.parent                     # _canonical
DEFAULT_TEMPLATE = CANONICAL_DIR / "project-template"
DEFAULT_CODE_DIR = Path.home() / "Code"

# Placeholder one-liners for the stacks that have a techstack doc today.
# Anything not listed here is asked interactively.
STACK_ONELINERS = {
    "techstacks/techstack--python_quart.md":
        "Python 3.12+ / uv / Quart (async Flask) / async SQLAlchemy 2.0 / aiosqlite->asyncpg / Alembic / Jinja2",
    "techstacks/techstack--python_flask.md":
        "Python 3.12+ / uv / Flask / SQLAlchemy 2.0 / SQLite->Postgres / Jinja2",
    "techstacks/techstack--rust_tauri.md":
        "Rust / Tauri / Cargo",
}

TEMPLATE_MARKER = re.compile(r"^\s*<!--\s*TEMPLATE FILE")


# --- small prompt helpers ----------------------------------------------------

def ask(prompt: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        ans = input(f"{prompt}{suffix}: ").strip()
        if ans:
            return ans
        if default is not None:
            return default
        print("  (required)")


def confirm(prompt: str, default: bool = False) -> bool:
    d = "Y/n" if default else "y/N"
    ans = input(f"{prompt} [{d}]: ").strip().lower()
    if not ans:
        return default
    return ans in ("y", "yes")


def ask_choice(prompt: str, options: list[str], allow_new: bool = True) -> str:
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    if allow_new:
        print("  N. (enter a new value)")
    while True:
        ans = input("  choose: ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            return options[int(ans) - 1]
        if allow_new and ans.lower() == "n":
            return ask("  new value")
        print("  invalid choice")


# --- derivations -------------------------------------------------------------

def list_organizations(code_dir: Path) -> list[str]:
    """Org umbrellas = the directories directly under ~/Code (minus dot/underscore)."""
    if not code_dir.is_dir():
        return []
    return sorted(
        p.name for p in code_dir.iterdir()
        if p.is_dir() and not p.name.startswith((".", "_"))
    )


def parse_repo_name(url: str) -> str:
    """Extract the bare repo name from an ssh or https GitHub URL.

    git@github.com:Org/my-repo.git  -> my-repo
    https://github.com/Org/my-repo  -> my-repo
    """
    name = url.strip().rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]
    # ssh form with no slash before the repo (rare): git@host:repo.git
    if ":" in name and "/" not in url:
        name = name.split(":")[-1]
    return name


def derive_env_prefix(slug: str) -> str:
    """txfrcloud-protomolecule -> TXFRCLOUD_PROTOMOLECULE_ (a default; override at prompt)."""
    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", slug).strip("_").upper()
    return f"{cleaned}_" if cleaned else "PROJECT_"


def list_techstacks(template_dir: Path) -> list[str]:
    ts_dir = template_dir / "_workflows" / "techstacks"
    if not ts_dir.is_dir():
        return []
    return sorted(f"techstacks/{p.name}" for p in ts_dir.glob("techstack--*.md"))


# --- the mechanical work -----------------------------------------------------

def scaffold(dest: Path, template_dir: Path, dry_run: bool) -> None:
    print(f"\n  mkdir -p {dest}")
    print(f"  rsync   {template_dir}/ -> {dest}/")
    print(f"  git init {dest}")
    if dry_run:
        return
    dest.mkdir(parents=True, exist_ok=False)
    rsync = shutil.which("rsync")
    if rsync:
        subprocess.run([rsync, "-a", f"{template_dir}/", f"{dest}/"], check=True)
    else:  # fallback if rsync isn't available
        shutil.copytree(template_dir, dest, dirs_exist_ok=True)
    subprocess.run(["git", "init", "-q", str(dest)], check=True)


def substitute_placeholders(dest: Path, mapping: dict[str, str]) -> int:
    """Replace {{KEY}} across text files and drop the TEMPLATE-marker lines.

    Returns the count of files modified. Skips the _workflows/ body files
    (they contain no placeholders) and anything that isn't UTF-8 text.
    """
    changed = 0
    for path in sorted(dest.rglob("*")):
        if path.is_dir() or path.name == "genesis.json":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        original = text
        # strip the "<!-- TEMPLATE FILE ... -->" first-line markers
        text = "\n".join(
            line for line in text.split("\n") if not TEMPLATE_MARKER.match(line)
        )
        for key, val in mapping.items():
            text = text.replace("{{" + key + "}}", val)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def write_genesis(dest: Path, manifest: dict[str, str], dry_run: bool) -> None:
    out = dest / "_research" / "genesis.json"
    print(f"  write   {out}")
    if dry_run:
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


# --- main --------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a new project from the canonical template.")
    ap.add_argument("--dry-run", action="store_true", help="print the plan; create nothing")
    ap.add_argument("--code-dir", type=Path, default=DEFAULT_CODE_DIR, help="root that holds the Org dirs")
    ap.add_argument("--template-dir", type=Path, default=DEFAULT_TEMPLATE, help="the canonical project-template dir")
    args = ap.parse_args()

    template_dir = args.template_dir.resolve()
    if not template_dir.is_dir():
        print(f"ERROR: template dir not found: {template_dir}", file=sys.stderr)
        return 2

    print("=== init_new_project ===")
    if args.dry_run:
        print("(dry run -- nothing will be created)\n")

    # 1. Organization / owner
    orgs = list_organizations(args.code_dir)
    org = ask_choice("Owning organization / umbrella:", orgs) if orgs else ask("Owning organization / umbrella")

    # 2. GitHub origin URL -> repo name (no remote configured; local-only house rule)
    origin_url = ask("GitHub origin URL (used only to derive the repo name; no remote is configured)")
    slug = parse_repo_name(origin_url)
    slug = ask("Repo / dir / short name", default=slug)

    dest = args.code_dir / org / slug
    if dest.exists() and any(dest.iterdir()):
        print(f"ERROR: target already exists and is non-empty: {dest}", file=sys.stderr)
        return 1

    # 3. Manifest (identity + active techstack), with sensible defaults
    today = _dt.date.today()
    techstacks = list_techstacks(template_dir)
    active_ts = ask_choice("Active techstack doc:", techstacks) if techstacks \
        else ask("Active techstack doc (e.g. techstacks/techstack--python_quart.md)")
    stack_oneline = STACK_ONELINERS.get(active_ts) or ask("Tech-stack one-liner")

    manifest = {
        "FULL_PROJECT_NAME": ask("Full project name", default=slug),
        "SHORT_NAME": slug,
        "ENV_PREFIX": ask("Env-var prefix (SCREAMING_SNAKE_)", default=derive_env_prefix(slug)),
        "ONE_LINE_DESCRIPTION": ask("One-line description"),
        "BRAND": ask("Brand / business name", default=""),
        "CORP_ENTITY": ask("Corporate entity (for LICENSE)", default=""),
        "COPYRIGHT_YEAR": str(today.year),
        "PACKAGE_NAME": ask("Package / module name", default="app"),
        "ECOSYSTEM_SIBLINGS": ask("Ecosystem / sibling projects", default="None"),
        "ACTIVE_TECHSTACK_DOC": active_ts,
        "STACK_ONELINE": stack_oneline,
        "STACK_OVERRIDES_OR_NONE": ask("Per-project stack overrides", default="None"),
        "STARTING_PHASE": ask("Starting phase", default="00"),
        "CREATION_DATE": today.isoformat(),
    }
    # extra provenance recorded in genesis.json (not a template placeholder)
    genesis = dict(manifest)
    genesis["github_origin_url"] = origin_url
    genesis["organization"] = org
    genesis["created_by"] = "init_new_project.py"

    # Summary + confirm
    print("\n--- plan ---")
    print(f"  organization : {org}")
    print(f"  target dir   : {dest}")
    print(f"  origin url   : {origin_url}  (remote NOT configured -- local-only)")
    for k, v in manifest.items():
        print(f"  {k:<24}: {v}")
    if not confirm("\nProceed?", default=not args.dry_run):
        print("aborted.")
        return 0

    # 4-5. Scaffold, write genesis, substitute placeholders
    scaffold(dest, template_dir, args.dry_run)
    write_genesis(dest, genesis, args.dry_run)
    if args.dry_run:
        print("\n(dry run complete -- nothing was created)")
        return 0
    n = substitute_placeholders(dest, manifest)
    print(f"  substituted placeholders in {n} files")

    # 6. Next steps (the non-deterministic remainder)
    print(f"""
=== scaffolded: {dest} ===

Deterministic steps are done. Remaining (a Claude/human pass):
  1. Fill the `<!-- AGENT: ... -->` prose blocks (CLAUDE.md overview,
     README intro, PROJECT_IDENTITY Project Context, ROADMAP stance,
     phase_00 goals, DECISIONS ADR context). The manifest is in
     _research/genesis.json.
  2. Verify nothing is left:  grep -rn '{{{{' .   and   grep -rn '<!-- AGENT:' .
  3. If a build project: run the active techstack's Skeleton Generation,
     then its Commands & Validation suite (e.g. uv sync && pytest && ruff).
  4. Commit (local-only, no remote, no Co-Authored-By). See NEW_PROJECT_GUIDE.md.

  GitHub origin (recorded, NOT configured): {origin_url}
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
