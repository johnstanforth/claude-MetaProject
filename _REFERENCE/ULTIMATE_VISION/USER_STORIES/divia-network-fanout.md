# User Story — The Divia.Network Fan-Out

> The canonical ecosystem moment: a single natural-language capture, dispatched and parsed by several
> different products at once, over the open Divia.Network integration layer. This is the story the
> whole Divia.AI ecosystem is built to make true.

- **Status:** Aspirational (a v2 capability) — but the *capture surfaces* exist or are being built today, and the worked examples are quoted verbatim from `diviahome-web` and `legendarymoney-web`.
- **Demonstrates:** discover-and-suggest from implicit data; the Divia.Network v0 contract; the "first-ever cross-app integrations" the ecosystem is being designed around.

---

## The narrative

It's evening. The user says — out loud to the **DiviaHome kitchen-counter device**, or typed into **Divia.Life** on their phone, or into the **DiviaHome** web app — one ordinary sentence:

> *"I had El Pollo Loco for dinner."*

Nothing is filled in. No form, no category dropdown, no amount. The sentence is captured **verbatim** as a natural-language **DiviaCard** and dropped, losslessly, into the **Activity Log** inbox. That's the whole user-facing interaction. Everything else happens *for* them.

Later — on the next agent pass — a **Divia.AI AgentSwarms**-hosted agent picks the card up and classifies it (*food-related, and a purchase*). It doesn't try to be clever in one place; it **fans the meaning out** across the products that each own a slice of it:

- **TastyPantry** records a **food-eaten** entry — `quantity=2` of `Food("quesadilla")` if that's what "El Pollo Loco for dinner" decomposes to — and decrements on-hand inventory accordingly (cascading through the recipe → base-ingredient model).
- **Sattvasic Health** records that food's **calories and macronutrients** into the day's intake, where it can later surface correlations the user never thought to ask for.
- **LegendaryMoney** records an **estimated dining expense** — merchant *El Pollo Loco*, category *dining/fast-food*, amount inferred from this user's priors **with a confidence band** — to be confirmed later against a card charge or a wallet-balance gap.
- **DiviaHome's Activity Log** keeps the original sentence as the durable source of truth, now cross-referenced to all three derived entries.

A parallel example, from the same docs: *"$42 at the hardware store"* → a **LegendaryMoney** transaction (and, if it implied supplies, a nudge elsewhere). The pattern is identical: **one sentence in; structured, cross-linked entries out, across four products, with the human never touching a field.**

**What's real today vs. aspirational:** the capture surfaces are real or in-build (DiviaHome's Activity Log, Divia.Life's quick capture, the planned kitchen device). The *fan-out* — agent classification, parsing, and cross-app delegation — is explicitly **v2** work, gated behind DiviaHome v1's "scan-and-import data unification" foundation ("first unify, then understand"). The Divia.Network contract that carries the fan-out is "still being designed" (v0). See [`ERRATA.md` E-06`](../../ERRATA.md): TastyPantry and Sattvasic Health currently *describe themselves* as standalone even though this story is exactly their reason to exist.

## Why it matters

This is the implicit-data principle in its purest form: the system learns what you eat by watching you eat, what you spend by watching you spend — and turns one frictionless sentence into a complete, multi-domain record. It's also the demo that makes "an ecosystem, not an app" self-evident: no single product could produce this; the value is in the *connections.*

## Ideation & Exploration (capture everything, commit to nothing)

- ✦ **Reverse the arrow (fan-*in*):** the same Divia.Network that fans one capture out to four apps can fan four apps' weekly outputs *into* one **Monday Morning Briefing** — a single human-paced digest spanning the GTD packet + pantry + health + money (from LATER-002). The standard serves humans, apps, *and* agents uniformly.
- ✦ **Ambient capture, not just spoken:** GPS says you were at El Pollo Loco at dinnertime; the connected-card feed shows a $12.40 charge; the kitchen device heard "dinner." The agent fuses these into one high-confidence entry and only asks the human when sources disagree ("Was that missing $12 the El Pollo Loco dinner?"). The "shock-and-awe" version of the story.
- ✦ **Confidence as a first-class, visible thing:** every derived entry shows *how sure* it is and *why* (which signal produced it), so the user can correct at a glance — and each correction sharpens the priors (the learning loop).
- ✦ **The trust boundary holds even here:** the agent *stages* the four entries; nothing is committed to the ledger / pantry / health record until the human's one-tap confirm (or it auto-confirms only above a learned confidence threshold the user sets per domain).
- ✦ **Delivery surfaces become ecosystem-native:** the "here's what I recorded from your dinner" recap arrives as a DiviaCard in the Divia.Life Journal or a Messages thread — not an email — dogfooding the ecosystem and demoing it at once.
- ✦ **Cross-app Get-Creative:** with eating (TastyPantry), spending (LegendaryMoney), and health (Sattvasic) all flowing through one log, an agent can surface insights no single app could see — "your late-night fast-food spend tracks with your worst-sleep nights" — the implicit principle compounding across domains.
- ✦ **Spice-aware fan-out:** route the *flavor* dimension of "El Pollo Loco" to spicemaster3000 ("you keep ordering smoky-citrus profiles — here's a blend to make it at home"), wiring the standalone flavor bet into the household ecosystem (see [`../VENTURES/TastyPal.md`](../VENTURES/TastyPal.md)).
