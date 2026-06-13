# User Story — The Agent-Assisted GTD Weekly Review

> A Swarm-hosted agent does the mechanical first pass of David Allen's *Getting Things Done* Weekly
> Review, so the 1–2-hour chore compresses to a ~20-minute confirm-and-decide session. It attacks
> GTD's single biggest failure mode — *skipping the review* — by holding the door open every week.

- **Status:** Aspirational; fully developed in [LATER-002 §5](../../../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md). Belongs to **Divia.AI Enterprise + Swarm** (the intended co-deployment).
- **Demonstrates:** the clerk/executive trust boundary; the same recurring-agent capability as the dev-side stories, pointed at *personal* work instead of code.

---

## The narrative

The GTD **Weekly Review** is the keystone ritual that keeps the whole system trusted — and GTD's most notoriously skipped practice, because done properly it's a 1–2-hour clerical slog competing with everything else on a Friday. The biggest point of failure in the methodology is a mostly-mechanical chore. That is exactly the shape of problem a recurring agent is best at.

All week, captures have funneled into Divia **Inboxes** from every surface — the Divia.AI Professional desktop, Divia.Life (Journal, Agenda, quick capture), the DiviaHome kitchen device, DiviaContacts-logged emails and calls. Ahead of the human's review session, the agent does the **first pass** across the canonical 11 GTD steps:

- **Collect / IN-to-zero:** sweep every Inbox; pre-clarify each capture — actionable? next-action phrased as a concrete verb? project association suggested? 2-minute items flagged.
- **Empty Your Head (the implicit principle):** surface open loops the human never explicitly captured — commitments made in passing in logged calls/emails/messages ("you told Sarah you'd send the contract; no task exists for that").
- **Review Action Lists:** pre-mark actions that observable data says are done (the email *was* sent); flag stale ones.
- **Calendars (past & upcoming):** auto-mine last week's residue; draft prep actions for next week.
- **Waiting-For:** aging report; detect arrivals (the reply *did* come in); draft follow-up nudges.
- **Project Lists:** **stalled-project detection** — flag every project violating the "≥1 next-action" invariant or unmoved in N weeks; *draft* candidate next actions.
- **Someday/Maybe:** re-rank against current life context; resurface items whose stated preconditions came true ("you said *someday, after the kitchen remodel* — the Activity Log says it finished").
- **Be Creative:** 2–3 provocations mined from implicit data ("you've journaled about X three times this month — make it a project?").

Then it delivers a **review packet** — *"Your review packet is ready: 14 items clarified, 3 stalled projects, 2 aged waiting-fors, 3 creative prompts. ~20 minutes."* The human sits down to **confirm and decide**, not to dig out.

**The trust boundary (the heart of it):** the agent **never completes, deletes, or commits** anything. GTD's entire psychological payoff depends on the human personally renegotiating their own commitments; automate *that* and the method hollows out. The agent is the clerk; the human is the executive. For personal-life data this stays at the L0/L1 rung of the autonomy ladder deliberately — and probably longer than dev-tooling tasks do.

## Why it matters

It directly attacks GTD's #1 failure mode (skipping the review), which means the trusted system stays trusted even on overloaded weeks — "mind like water" becomes sustainable rather than aspirational, and the **Get Creative** phase (the first thing humans drop when tired) actually happens every week, with the agent holding the door open. It's also the marquee proof that the *same* Swarm recurring-agent capability that improves software projects (the dev-side stories) improves *anyone's* life-management — same backbone, completely different brain.

## Ideation & Exploration (capture everything, commit to nothing)

- ✦ **Continuous micro-reviews:** silent daily mini-passes (clarify new captures, detect arrivals, update staleness counters) so the weekly review never faces a mountain — the weekly session becomes a true checkpoint, not a dig-out. (Allen's dream, minus the discipline cost.)
- ✦ **Two-minute-rule staging:** GTD says do anything under two minutes now; the agent pre-stages the draft (the reply, the calendar hold, the renewal click) so each "do" is one approval tap.
- ✦ **Adaptive checklist:** reorder/weight the 11 steps by what *this* user actually lets slide (their waiting-fors rot; their someday/maybe is pristine) — the implicit principle applied to the review itself.
- ✦ **Review-the-reviewer:** a quarterly meta-pass where the agent reports its own precision ("you accepted 71% of my drafted next-actions; rejections cluster around family commitments") and proposes recalibration — trust through measured humility.
- ✦ **Adversarial review:** run the packet as a collab-group (the aixocode pattern) — one agent proposes, a second (different vendor) critiques before it reaches the human, catching lazy aggregation.
- ✦ **The agent learns the *person*:** "John always rejects drafted nudges to family members" — memory across runs is the whole Divia.AI premise (the dev-side twin is learning the *team*). Memory of what was deferred, rejected, and why.
- ✦ **Cross-app Get-Creative:** draw the "creative and courageous" prompts from the *whole* ecosystem's implicit data — journal themes (Divia.Life), eating adventurousness (TastyPal), spending patterns (LegendaryMoney) — surfacing project ideas no single app could see.
- ✦ **Review-completion rate as a product metric:** the Sunday-evening packet's open/complete rate becomes the headline KPI that proves the feature is working.
