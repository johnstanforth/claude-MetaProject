# User Story — The Nightly Household Replenishment Loop

> Why the household review runs **nightly, not weekly**: only a daily cadence catches consumption-driven
> replenishment in time. "We're nearly out of milk" has to become a time-decaying grocery item and an
> escalating errand *before* the milk actually runs out.

- **Status:** Aspirational; from John's LATER-002 note (now folded into [LATER-002 §6](../../../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md)). Belongs to **DiviaHome** (+ the DiviaHome kitchen device + Swarm agents).
- **Demonstrates:** why cadence is domain-specific; implicit consumption data → proactive, time-aware action.

---

## The narrative

Every night, after the household has gone quiet, a DiviaHome agent does the household's review. Most of it is the familiar implicit-data sweep — maintenance schedules and chore rhythms *learned* from the Activity Log rather than configured. But the reason it's **nightly** rather than weekly is **replenishment**, which a weekly cadence would chronically miss.

The household has been logging consumption all week — some of it typed, much of it ambient (the kitchen-counter device hears "we're out of the good coffee," receipts get scanned, food logs decrement TastyPantry inventory). Tonight the agent notices a pattern: based on usage, **the milk is running low.** So it does two coupled things:

1. **Adds milk to a time-decaying grocery item** — not a flat to-do, but something like *"milk — needed within 72 hrs, priority escalating every 24 hrs."* Tonight it's gentle; tomorrow night it's firmer; the night after it's urgent.
2. **Raises the weighted priority of the grocery-run errand itself** as that deadline approaches — so the errand surfaces higher in the morning's plan exactly when it needs to, and the family isn't blindsided by an empty carton at breakfast on day three.

By morning, the household packet reflects it: a quietly-updated shopping list and a grocery-run errand that's climbed the priority order on its own. Nobody filled out a form; nobody remembered to add milk. The system watched, inferred, and **staged the right action at the right time.**

**What's real today vs. aspirational:** none of it is built — DiviaHome is pre-code (Phase 00), and the nightly-review / replenishment logic and the kitchen device live only in LATER-002, not yet in the repo (see [`ERRATA.md` E-12`](../../ERRATA.md)). The TastyPantry inventory/depletion model and the Activity Log capture pattern that this depends on *are* designed, in `tastypantry` and `diviahome-web` respectively.

## Why it matters

It's the crisp argument that **recurring-agent cadence is a per-domain design decision**, not a global setting — the dev-side weekly review and the GTD weekly review are weekly because their loops are weekly; the household's replenishment loop is nightly because milk doesn't wait for Friday. And it's a uniquely demo-able "shock-and-awe" moment: the system adding milk to the list *before you noticed*, with urgency that rises like a real deadline.

## Ideation & Exploration (capture everything, commit to nothing)

- ✦ **Time-decay priority as a reusable primitive:** "needed within N hrs, priority escalating every M hrs" isn't milk-specific — it's a general scheduling shape (a waiting-for that rots, a bill that's due, a medication refill runway). Build it once; reuse it across DiviaHome, LegendaryMoney, and Sattvasic (Rx refills).
- ✦ **Consumption forecasting, not just thresholds:** learn each staple's burn rate (a household of four drinks milk faster than one) and predict the run-out date, so the 72-hour window is computed, not fixed.
- ✦ **Per-store routing:** because TastyPantry tracks per-store shopping lists, the agent can bundle the milk with whatever else is low *at that store* and time the errand for when a grocery run is already likely (calendar + location patterns).
- ✦ **The kitchen device as both capture and delivery surface:** it hears "we're out of coffee" (capture) and, in the morning, says "before you leave — milk and coffee are on today's list, and the hardware store closes at 6" (delivery). One device, both ends of the loop.
- ✦ **Cross-app replenishment:** Sattvasic's supplement runway + LegendaryMoney's "is there budget for a big grocery run this week?" feed the same nightly packet — the household sees one coherent "here's what needs buying and whether you can afford it" view.
- ✦ **Trust boundary stays:** the agent stages the list and the errand-priority bump; it never *places an order* unless the household has explicitly graduated a specific staple to auto-reorder (and even then, with an after-the-fact audit line).
- ✦ **The household packet as a Divia.Life message:** delivered as a morning DiviaCard, not a notification spew — "3 things low, 1 errand climbing, 2 chores due" — one calm item to glance at over coffee.
