<!--
PROVENANCE: This twin-track (Claude + Codex) research method was inherited via the
workflow system (originally a kingstrat-adventuregps proposal, validated on a large
technical-research run) and adapted for this project. The braided
mechanism is domain-neutral; its load-bearing primitive is the irreversible-fork hunt,
a software-architecture concept. This is an advanced, rarely-needed variant — for most
research on this project, the solo workflow_research.md is the right tool.

STATUS: v2. v2 (2026-06-24, after the workflow's first real run in a sibling project)
corrects the CENTRAL framing — the default is PARITY mode (both agents do the SAME
task; the breadth-vs-depth difference is a property of the agents' STYLES, not a topic
split). The original wording ("Codex = wide-net discovery track, Claude = depth track")
accidentally read as "give the agents different topics," and the first run did exactly
that — good research, but it destroyed the head-to-head comparison. See "The principle"
and "Two modes". Do it the parity way.
-->

# Workflow: Multiagent Research — Braided Claude + Codex Twin-Track

> Deep research where **both agents work the *same* task in parallel** — they differ in *style*, not topic: Codex casts wide (breadth), Claude goes deep — then Claude merges the two corpora, **diffs** them, and **dispatches follow-up depth tracks** for whatever Codex surfaced that Claude missed. The `-multiagent` sibling of solo `workflow_research.md`.

## Quick Reference

| Item | Value |
|------|-------|
| When to use | Broad, high-stakes research where Codex's wide-net discovery materially *adds* to Claude's depth — e.g. settling a data model, an external-integration design, or a build-vs-buy decision with a wide option space. Small, tightly-scoped questions stay on solo `workflow_research.md`. |
| Variant of | `workflow_research.md` (Claude solo). The braid wraps it with a parallel Codex track + a merge gate; it does **not** replace it. |
| Claude track mechanics | `workflow_research.md` Phase A/B/C — breadth-first survey → sliding-window depth subagents (max 3 concurrent **Opus**) → user-gated synthesis. Inherit all of it (dispatch manifest, no-skim rule, SYNTHESIS_BRIEF, watchdog + short-path patterns). |
| Codex track mechanics | Claude drives Codex via the **codex skill** (`codex exec`, model + effort) as delegated agent(s) it oversees — see "Driving Codex in this environment" below. For a single-project run do **1–few passes**, not 40–60. |
| Default mode | **PARITY** — both agents get the *same* research questions and work blind; the breadth-vs-depth difference comes from their *styles*, not a topic split. (Complementary mode — splitting topics by agent strength — is a separate, deliberate, post-calibration choice; see "Two modes".) |
| Late audit | Optionally re-run Codex to adversarially stress-test the *written* synthesis — opt-in, for high-stakes decisions (Step 6). |
| Output | One unified synthesis answering the research questions — e.g. a recommended design, an option comparison with a pick, or a defined build scope that feeds the next `sp_`/`xp_`. |
| Owner gate | John approves the merged findings before synthesis, and the synthesis before it becomes canon. |
| Sacred invariant | **Codex output is triaged INPUT, never a binding verdict.** Final calls stay Claude+John. |
| Subagent model | **Opus only** for Claude research subagents (never Sonnet — documented factual errors). Codex track defaults to **gpt-5.5 at xhigh** effort. |
| Concurrency | Each Codex agent consumes a dispatch slot. **Target: combined ≤ 8** (Claude subagents ≤ 5, Codex the rest); **fall back to combined 5** (3 Claude + 2 Codex) on any harness thread/window error. Empirically 5–10 simultaneous has run clean in sibling repos, but one project hit a ~6-agent limit — hence the fallback. |

---

## Overview

This workflow runs **two agents on the same research task in parallel** and exploits that they have **different styles, not different jobs**: Codex casts the widest net (more options, tools, prior-art, edge cases — and, in practice, more sections/chapters), with `Fact:`/`Inference:`/`Recommendation:`/`Confidence:` tagging and citations; Claude goes deeper and tighter (named patterns, the specific source/incident, sharper recommendations). The payoff is threefold: the **overlap** between them is a trust signal, the **Codex-unique** findings are exactly the things Claude alone would have missed, and a **dispatch-more loop** turns those gaps into new Claude depth tracks. Both agents' raw output is **triaged input** — final calls stay Claude+John.

The Claude track *is* the existing solo research workflow. The only new material here is the **parallel Codex track on the same questions** and the **Merge & Triage gate** that diffs and folds the two corpora into one. If you understand `workflow_research.md`, you already understand 80% of this.

The three research workflows form a family — pick by scope:

| Workflow | Use when |
|----------|----------|
| `workflow_research.md` | Default. Claude-only; focused or broad. |
| `research_workflow_CODEX.md` | Codex-only wide-net survey (rare standalone use). |
| **`workflow_research_multiagent.md`** (this) | Broad + high-stakes, where Codex's discovery genuinely widens the net beyond what Claude alone would find. |

---

## The principle — same task, different styles

**Both agents research the SAME questions, in parallel, blind to each other.** Do NOT split the work by topic. The breadth-vs-depth difference is a property of the *agents*, not the assignment:

- **Codex casts wide.** On any task it naturally produces more, broader sections — surfacing options, tools, prior-art, and edge cases a focused pass misses, with `Fact:`/`Inference:`/`Recommendation:`/`Confidence:` tagging and citations. Validated on the workflow's first real run (a sibling project): given identical blind tasks, Codex produced ~2.6× the breadth of Claude and reliably surfaced real findings Claude missed (on a code-reading task it even read the *test suites* Claude's tracks skipped).
- **Claude goes deep.** Tighter, better-organized, names the canonical pattern, cites the specific source/incident, turns a topic into a decision.

You give them the **same** assignment, let those styles play out, then **diff** the results — the overlap is the trust signal, the Codex-unique findings are the prize.

> ⚠️ **THE TRAP — do not repeat the first run's mistake.** "Codex's style is wide-net discovery" does **not** mean "give Codex the discovery topics and Claude the deep topics." Splitting the topics by agent is *complementary* mode (below): it yields good research but **destroys the comparison**, because the two agents never work the same ground, so you cannot measure overlap or see what Codex uniquely catches — the whole point. **In parity mode the topic list is identical for both agents.** If you catch yourself writing *different* prompts for Codex vs Claude, stop: either you are deliberately in complementary mode (say so in the manifest) or you are about to repeat the mistake.

Codex output is always **triaged input, never a binding verdict**; because its wide net includes some unverified secondary sources, the **Claude diff/cross-check is what filters them.** Welcome its breadth across the whole surface; the final design/schema/integration calls stay Claude+John.

## Two modes (and which to use)

| Mode | What | When |
|------|------|------|
| **Parity (DEFAULT)** | Both agents get the **identical** research questions, work blind, then Claude diffs them + dispatches follow-ups for the gaps + (optionally) writes a comparison scorecard. | While **calibrating** the agents (learning each one's edges) and for **foundational / high-stakes** research where the cross-check and maximum coverage justify the duplicated effort. Use this unless you have a specific reason not to. |
| **Complementary** | Split the topics by agent strength (e.g. Claude on internal/source questions, Codex on external prior-art). No head-to-head; cheaper. | **Only once calibrated** — when you already know each agent's edges, don't need the comparison, and want to save tokens. A deliberate, *stated* choice — never the silent default. |

Parity costs more (the agents duplicate effort by design) — that *is* the price of the comparison and the cross-check, and for foundational research still settling the design it is worth paying. **State the chosen mode explicitly in the dispatch manifest** so the next session knows which one it is running and why.

---

## The sequence (six steps, named gates)

### 1. Scope + dispatch (Claude)

Per `workflow_research.md` Phase A: read the relevant source material (the research questions, any reference projects under `_REFERENCE/_EXTERNAL/`, prior research in `_specs_and_plans/_research/`, and `CLAUDE.md`) and settle the **research questions once** — in parity mode they are SHARED by both agents. Then emit the dispatch artifacts:

- (a) the **Claude depth-track index** + `README.md` dispatch manifest (**state the MODE — parity or complementary**) + `RESEARCH_PLAN.md`. Commit before launching any subagent (the resumable checkpoint).
- (b) the **Codex prompt(s)** built from the **same** research questions (parity mode), framed to play to Codex's wide-net style and carrying the project context (see `PROJECT_IDENTITY.md`) so Codex designs *for that envelope*, not for enterprise specs. Tell Codex its output **will be compared head-to-head against an independent agent's** and to work **blind** (do not read the other agent's files). Claude launches this via the codex skill in Step 2 — no manual hand-off. *(Complementary mode is the ONLY case where (a) and (b) cover different topics by strength — and the manifest must say the comparison is being skipped.)*

Match Claude's depth-subagents' reading to the task — e.g. for a code-reading task, instruct them to read the **test suites**, not just the implementation (that is where Codex out-read Claude in the validation run).

### 2. Twin-track research (parallel, blind — neither blocks the other)

Both agents work the **same** questions, independently and blind, so the overlap is real signal:

- **Codex track** — Claude launches the prompt(s) via the **codex skill** (`codex exec`, default gpt-5.5 / xhigh) as delegated agent(s), overseen like research subagents (see "Driving Codex in this environment"). Codex's native mode is to go wide in **1–few passes** (one pass per cluster of questions produces many sections), so you don't pre-decompose it the way Claude's tracks are decomposed. Have each pass write its output to a file the parent moves into the research directory.
- **Claude track** runs `workflow_research.md` Phase B: sliding-window dispatch, **max 3 concurrent Opus subagents** (combined with Codex, see the Concurrency row), README updated + committed after each completion. Claude's depth tracks are dispatched from **Claude's own reading of the shared questions** — blind to Codex's output — to keep the comparison honest.

Launch order barely matters (Codex is usually faster); just stay under the combined concurrency cap.

### 3. Merge, diff & dispatch-more (Claude) — the load-bearing step

Claude reads **both** corpora **in full** (no-skim; delegate heavy reading to Opus subagents, ingesting Codex's passes for breadth and its `Fact:`/citations for specifics). Then:

- **Diff the two corpora** (parity mode): for each shared question note the **overlap** (where both converge — high confidence), the **Codex-unique** findings (the prize — what Claude alone would have missed), the **Claude-unique** findings, and any **disagreements/errors** (this is where you cross-check Codex's unverified secondary sources). Optionally capture it in a `COMPARISON_SCORECARD.md` (breadth metric, overlap, unique-per-agent, errors caught) — it proves the run's value and keeps calibrating the agents.
- **Dedupe & reconcile** overlapping findings; reconcile contradictions (especially where Codex's recommendations conflict with project constraints or prior research).
- **Flag the irreversible architectural forks** — cheap-now / catastrophic-to-retrofit decisions (e.g. the data model / on-disk schema shape, public API and module-seam boundaries, external-integration contracts such as the Gmail ingestion format, and anything that would force a painful data migration later). Surface them as a short "decide-now" list for the Owner Gate.
- **The dispatch-more loop (the originally-intended payoff):** for each valuable **Codex-unique** finding, dispatch a **new Claude depth track** to verify it (against source/fixtures) and go deeper — Codex's breadth surfaces the lead, Claude's depth nails it down. (Conversely, a Claude-found-interesting item can spawn a wide-net Codex pass.) Add these tracks, then re-merge.

Output: one deduped, reconciled findings set **+** the irreversible-forks decide-now list **+** (parity) the comparison scorecard.

### 4. Owner Gate (John) — HARD GATE

John reviews the merged findings and the decide-now list, resolves the irreversible forks, and may add or redirect tracks. **Do not begin synthesis until John explicitly approves.** (Same hard gate as `workflow_research.md` Phase B→C; here it also covers the merge, since a misframed merge propagates into synthesis.)

### 5. Synthesis (Claude)

Per `workflow_research.md` Phase C and the Option-B pattern (write a `SYNTHESIS_BRIEF.md`; dispatch one clean Opus subagent to draft `synthesis.md` reading everything no-skim; the living orchestrator + John iterate on the draft — do **not** `/clear`). Mine `analysis-NN` for citations/numbers, Codex passes for breadth, each for its topic-map. Apply the standard framing-question backbone (below). The synthesis output is the research deliverable that feeds the next `sp_`/`xp_` sprint plan.

### 6. Late adversarial audit (Codex) — OPT-IN

For high-stakes decisions, have Codex stress-test the *written* synthesis for seams — data-integrity gaps, schema-evolution and migration traps, async/concurrency hazards, and external-API failure modes. Claude+John triage the findings (still: triaged input, never binding). Fold accepted corrections back into `synthesis.md`. Skip this step for lower-stakes research.

---

## Driving Codex in this environment (the codex skill)

In this environment Claude drives Codex directly — no manual hand-off. Claude authors the Codex prompt(s) (Step 1 — in parity mode, built from the *same* research questions as Claude's tracks) and launches Codex itself via the **codex skill** (`codex exec`), specifying the model and reasoning effort (**default: gpt-5.5 at xhigh**; override per run). The Codex run is then a **delegated agent Claude oversees exactly like a research subagent track** — launch (preferably in the background so completion notifies the orchestrator), monitor, then ingest its output at the Merge & Triage gate.

**Scale to the project, not a portfolio.** The source run had a Codex *parent* spawn 40–60 Codex subagents; that is overkill here. Run **1–few Codex passes** — each a wide-net prompt over a cluster of research questions — and add passes only if a gap surfaces. Have Codex write each pass to a file (or return it as final text) so Claude can move it into the research directory alongside the Claude analyses.

**Concurrency discipline (hard-won).** Each Codex agent consumes a dispatch slot alongside Claude's Opus subagents. **Target: combined ≤ 8** — up to **5 Claude** depth subagents plus the Codex pass(es). Empirically 5–10 simultaneous agents have run clean across sibling repos, but one project hit a **~6-agent harness limit**, so **fall back to combined 5 (3 Claude + 2 Codex)** the moment the harness throws a thread / context-window error. Launch order barely matters (Codex is usually faster; stalls are unpredictable network/server load), so no preset lead-time — just stay under the cap and scale back on error.

### Exact codex-skill invocation (reference — learned 2026-06-24, codex skill v1.3.0)

The codex skill wraps the Codex CLI. The canonical non-interactive call:

```bash
codex exec --skip-git-repo-check -m gpt-5.5 --config model_reasoning_effort="xhigh" \
  --sandbox <read-only|workspace-write|danger-full-access> [--full-auto] \
  -C <working-dir> "YOUR PROMPT" </dev/null 2>/dev/null
```

Flags and gotchas that cost real time to discover (so future-Claude doesn't repeat the archaeology):

- **`--skip-git-repo-check`** — always include it.
- **`-m` model** — one of `gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.3-codex-spark`, `gpt-5.3-codex`. **`--config model_reasoning_effort="<xhigh|high|medium|low>"`** sets effort. Default for research: **gpt-5.5 / xhigh**.
- **`</dev/null` is mandatory in a harness.** `codex exec` ALWAYS reads stdin and concatenates it with the positional prompt; if stdin isn't closed it blocks **forever** (symptom: zero bytes out, zero CPU, looks hung). Append `</dev/null`.
- **`2>/dev/null`** suppresses Codex's thinking tokens (stderr). Keep it on except when debugging.
- **Sandbox modes** — `read-only` (no edits, **no network**); `workspace-write --full-auto` (edits, no network); `danger-full-access --full-auto` (**network** + broad access). **Wide-net web discovery needs `danger-full-access`** — there is no narrower mode that grants network. Mitigation: run with `-C <scratch dir>` so Codex's CWD is isolated from the repo, and have it write only its one output file there (the parent then `mv`s it into the research directory).
- **High-impact flags** (`--full-auto`, `--sandbox danger-full-access`, `--skip-git-repo-check`) require user confirmation per the skill — get John's standing approval for the passes once, then proceed.
- **No intermediate output / timeouts.** Codex writes its result only at completion; if killed early the output file is silently empty (no error). Run each pass as a **detached background** process (not subject to the foreground 600s cap) and budget by effort: low ~150s · medium ~300s · high ~600s · **xhigh ~1200s**.
- **Resume** (no new config flags; inherits model/effort/sandbox): `echo "follow-up" | codex exec --skip-git-repo-check resume --last 2>/dev/null`.
- **Codex is a colleague, not an authority** — it has its own knowledge cutoff; verify its claims and push back when you know better. Identify yourself as Claude when resuming to debate a disagreement.

## The framing-question backbone (always-true, technical)

Apply to every finding at the Merge and Synthesis steps:

1. **What is the irreversible fork here?** Cheap to get right now, catastrophic to retrofit?
2. **What is the simplest v1** that does *not* foreclose the far vision (the broader feature set this experiment might grow into)?
3. **What does it cost to retrofit later** if we guess wrong now?
4. **What do the project's data-integrity needs demand** of this decision — preserving ingested source data, a clean Postgres-portable schema, safe migrations?
5. **Does this keep clean separation of concerns** — domain/services independent of the web/HTTP layer and external APIs?
6. **What do the app's surfaces need** — do the web UI and the background ingestion service each get what they require from this decision?

---

## Scope notes

This twin-track (Claude + Codex) variant is heavier than the solo `workflow_research.md`. Use it only when a research question genuinely benefits from a second independent agent's wide-net coverage alongside Claude's depth — and, in **parity mode**, from the head-to-head cross-check. For most research on this project — a single-developer playground — the solo `workflow_research.md` is sufficient; reach for this twin-track version when the decision space is wide and the cost of missing an option is high, or while you are still calibrating how Claude and Codex differ on this project's material.

What stays domain-neutral and always applies: the **same-task parity** principle (and its trap), the twin-track parallelism, the Merge/diff gate, the dispatch-more loop, the Owner Gate, the synthesis pattern, and the optional late adversarial audit.

---

## Related Workflows

- `workflow_research.md` — the solo Claude research workflow; **this braid's Claude track is that workflow.** Inherit its dispatch, no-skim, gating, and watchdog/short-path mechanics.
- `research_workflow_CODEX.md` — the Codex-side research playbook; the braid's Codex track follows it.
- `workflow_ideation.md` — brainstorming/scope selection that may precede research.
- `workflow_start_new_sprint.md` — where the synthesis feeds the `sp_`/`xp_` sprint plan.
