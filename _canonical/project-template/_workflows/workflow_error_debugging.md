# Workflow: Error Debugging

> The **stack-agnostic method** for diagnosing and fixing runtime/test errors. The error-category table, common scenarios, and diagnostic commands are stack-specific and live in the **Debugging** section of this project's active techstack doc (`_workflows/techstacks/techstack--*.md` — the active one is named in [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md)). Read that section alongside this method; together they are the complete debugging guide.

## The loop

Diagnose → hypothesize → verify → fix → confirm. Resist the urge to change code before you understand the error. A fix applied to a misunderstood error usually just moves the symptom.

## Step 1: Read the actual error

Read the real error message and the **full traceback** before doing anything else — not just the last line, and not the downstream symptom. The last line is the exception; the cause is usually mid-stack. Find the first frame that references your own code (not stdlib/framework frames). Where the error surfaces — test output, lint output, dev-server console/log, browser, external API — is stack-specific; the techstack Debugging section lists the sources for your stack.

## Step 2: Categorize

Match the symptom to a category (import, attribute, routing, template, database, migration, config, external integration, …). The category narrows where to look and what to suspect. The per-stack "symptoms → typical cause" table is in the techstack Debugging section — use it to turn a raw traceback into a hypothesis.

## Step 3: Locate the source

Read the traceback bottom-to-top and open the first frame in your own code at the indicated line. Check the obvious culprits for that category: a value that's unexpectedly `None`/empty, a wrong/renamed name, a missing `await`, an unregistered route, a session/transaction misuse, schema/migration drift. The techstack Debugging section gives the stack-specific locate-the-source drills (e.g. how to inspect the dev DB or reproduce a 500).

## Step 4: Check recent changes

Most errors during active development were introduced by a recent change.

```bash
git log --oneline -10        # what changed recently?
git diff HEAD~1              # what exactly changed in the last commit?
git status                   # what is modified but uncommitted?
git log --oneline -5 -- path/to/suspect/file
```

If the error started after a specific commit, `git diff` that commit to see exactly what changed.

## Step 5: Fix and verify

1. Make the **smallest change** that resolves the root cause — not the symptom.
2. Re-run the specific failing test first, then the **full validation suite**. Both validators must pass with zero failures before the work is done. The exact validation commands and the per-stack quick diagnostic commands are in the active techstack doc (its **Commands & Validation** and **Debugging** sections; the active doc is named in [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md)).
3. For a UI/page issue, verify in the browser: rendered output, dev-console errors, and failed network requests (4xx/5xx, wrong content types, slow responses).

## Escalation: when to stop

**During a sprint execution session:** apply the **2-attempt rule** ([`EFFICIENCY_RULES.md` § E8](EFFICIENCY_RULES.md#e8-two-attempt-rule-stop-after-2-failed-fixes)) — if 2 fix attempts fail, STOP, document what you tried, and flag for human review. Move to the next independent task if possible.

**Outside a sprint:** if the fix is non-trivial, file a follow-up backlog item; don't spend more than ~15 minutes without progress; consider whether the issue reveals a deeper architectural problem worth a dedicated sprint or a roadmap note.

## Related

- **Your active techstack doc's `## Debugging` section** (`_workflows/techstacks/techstack--*.md`) — the stack-specific error tables, common scenarios, and diagnostic commands. This is the other half of this workflow.
- `workflow_start_new_sprint.md` — error handling during sprint execution (2-attempt rule)
- `workflow_quick_fix.md` — fixing an error as a standalone commit
- [`PROJECT_IDENTITY.md`](PROJECT_IDENTITY.md) / `CLAUDE.md` — project identity, active stack, validation commands, and known gotchas
