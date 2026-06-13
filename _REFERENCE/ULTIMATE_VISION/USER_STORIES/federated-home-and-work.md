# User Story — One Identity, Federated Home and Work

> Sign in once, with one global Divia.AI username, and see both lives at once — your tasks at work
> (a Divia.AI Enterprise server) and your tasks at home (a DiviaHome server) — switching context
> without switching accounts. The endgame the whole Divia.AI server line is being built toward.

- **Status:** Aspirational — the **Divia.AI Global (SaaS)** identity layer doesn't exist yet. But the Python prototypes are **already carrying placeholder global-identity fields** today, specifically so this can arrive without a painful migration.
- **Demonstrates:** why the server line is sequenced the way it is; data ownership + federation as the long-term moat.

---

## The narrative

A user has two Divia worlds. At the office, their team runs a **Divia.AI Enterprise** server — projects, shared documents, the team task graph, administered by corporate IT. At home, they self-host **DiviaHome** — the household hub, the Activity Log, the family's tasks and calendar. Today those would be two separate accounts, two logins, two silos.

In the federated future, they're one. A single **global Divia.AI identity** — "one global username" — authenticates against the central **Divia.AI Global (SaaS)** service, and from there the user's clients can reach *both* servers. The **Divia.Life** mobile app shows a unified view and lets them flip between **"tasks at work"** and **"tasks at home"** with a context switch, not a re-login. The home server and the work server stay independent and separately owned — Global is just the identity/auth authority that federates them (OAuth-style flows; each server is a federated node).

Crucially, this is **why the server line is sequenced the way it is.** DiviaHome (open, Python) is the lab. Divia.AI Enterprise is "a higher-performance, locked-down, Rust re-implementation of the DiviaHome server" — *deliberately not started* until DiviaHome hits a battle-tested v1 + ~30 days of real use. And then a specialized, upgraded build of that Enterprise server becomes **Divia.AI Global** — the recurring-revenue identity layer. The placeholder identity fields in today's prototypes are the seed of all of it.

**What's real today vs. aspirational:** entirely aspirational at the behavior level — Enterprise isn't started (not even a git repo), Divia.Life is pre-code, and Global doesn't exist. What *is* real is the **deliberate forward-compatibility:** DiviaHome and LegendaryMoney both carry placeholder global-identity fields now (confirmed in their docs). An open design question remains: whether a customer's Enterprise server and Divia.AI's own central Global SaaS share a codebase or fork (see [`../VENTURES/DiviaAI.md`](../VENTURES/DiviaAI.md)).

## Why it matters

It's the through-line that makes the Divia.AI server roadmap a *strategy* rather than a pile of apps: open lab → hardened commercial server → recurring-revenue identity SaaS, each gating the next. And it's a genuine differentiator — "one identity, your data, federated across the servers *you* control" is the data-ownership promise the whole ecosystem is premised on, expressed as a single login.

## Ideation & Exploration (capture everything, commit to nothing)

- ✦ **Federate across the *whole portfolio*, not just home/work Divia:** "sign in with Divia" could span work (AIXO.Dev Platform / Enterprise), home (DiviaHome), money (LegendaryMoney), health (Sattvasic), and dev (aixocode) — making Divia.AI Global the account spine of everything John builds (see [`../VENTURES/README.md`](../VENTURES/README.md) §4).
- ✦ **Context as a first-class axis:** beyond "work vs. home," let the user define contexts (a side business, a volunteer org, a shared household) each backed by its own server, all under one identity — the federation model generalizes past two nodes.
- ✦ **Privacy architecture as the product:** because the audit trail and personal data live on *the user's own servers*, "your most intimate data never leaves infrastructure you control; Global only knows who you are, not what you do" is a sharp, sellable privacy stance — especially paired with the Divia.Foundation Code-Vault guarantee.
- ✦ **Agents respect the boundary:** a recurring agent acting on home data runs against the home server; a work agent against Enterprise — the federation boundary is also the agent-authority boundary, so personal-life agents (GTD, household) stay at a lower autonomy rung than work agents by construction.
- ✦ **Cross-context queries with explicit consent:** "do I have time this week to take on the school fundraiser?" answered across the work calendar *and* the home calendar — powerful, but gated behind an explicit per-query cross-context grant, never silent.
- ✦ **Migration-free by design as a marketed promise:** "start free at home, bring your identity to work, never re-create your account" — the placeholder-fields-now discipline becomes a user-facing guarantee of continuity.
