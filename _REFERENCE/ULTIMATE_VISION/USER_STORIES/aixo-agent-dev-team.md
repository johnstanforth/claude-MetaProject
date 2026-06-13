# User Story — The Cross-Timezone Human + AI Dev Team

> Named AI agents — each backed by a different frontier model — work as full team members alongside
> human developers, carrying context across timezones and across projects, over months and years.
> The AIXO.Dev vision made concrete in a day of work.

- **Status:** Partly real today (aixocode CollabPairs + lossless session capture ship now); the persistent-named-agent, team-scale version is aspirational (gated behind aixocode↔aixodev-web server integration). Quoted from `aixodev-aixocode`'s bigger-ideas docs and `aixodev-web`'s "Joy of Engineering" vision.
- **Demonstrates:** agents as co-developers (not autocomplete); the lossless archive as shared team memory; the dev-side twin of the GTD/household recurring-agent stories.

---

## The narrative

A feature needs building. On the AIXO.Dev Platform, it's decomposed and the sub-tasks land with the agents best suited to them — **@maximus** the Architect (Claude; Stoic, big-picture) shapes the approach and hands a database-migration slice to a schema specialist; **@codaramus** the Guardian (a different vendor's model, for genuine cognitive diversity) is queued to review; **@milton** the documentarian (NotebookLM-grounded) will update the docs. No human had to context-switch to relay any of it.

On the developer's laptop, **`aixocode`** is where the work actually happens. A **CollabPair** — two agents plus the human in a shared CHAT — opens for the tricky part: one agent proposes, the human steers, a second agent (a different vendor) critiques before anything is final. The whole session is **captured losslessly** to the local SQLite archive, byte-for-byte, the way every session is.

Then the timezone handoff: the developer in **Dallas** hits a checkpoint at 5pm and hands off. A developer in **Bangalore** picks it up at 9am their time, **resumes the CollabPair with full context** — the agents provide the continuity, so nothing is re-explained — and continues where Dallas left off. Months later, @maximus, having seen a security-vulnerability pattern on a FinTech project, **recognizes the same pattern on an IoT project** and flags it — institutional knowledge that doesn't walk out the door when a senior engineer leaves.

**What's real today vs. aspirational:** aixocode's CollabPairs (2 agents + human, group chat, a guarded code-review workflow), the lossless archive, and multi-tool wrapping are **shipping now** (Phases 4/6/7 complete). The persistent named-agent personalities with self-editing `SOUL.md`, the platform-side task assignment, the cross-project knowledge transfer, and the AgentEngine runtime that executes platform agents locally are **aspirational** — gated behind the not-yet-live aixocode↔aixodev-web server integration (see [`STATUS.md`](../../STATUS.md) and [`ERRATA.md` E-11`](../../ERRATA.md)).

## Why it matters

It's the AIXO.Dev thesis in one scene: AI agents as **true co-developers and partners**, amplifying humans rather than replacing them, and bringing back the joy of engineering. And it's the dev-side mirror of the GTD and household stories — the *same* recurring/collaborative-agent capability, pointed at code and the development process instead of personal life. The lossless archive is the connective tissue: local-first on the laptop, mined for team intelligence on the platform.

## Ideation & Exploration (capture everything, commit to nothing)

- ✦ **CollabPair templates as executable institutional knowledge:** a "Security Review" or "DB-Migration Review" pairing becomes a shareable, org-wide 3-phase recipe — the team's hard-won process, encoded and re-runnable.
- ✦ **Mine the archive as a knowledge base:** "which steering interventions during CollabPairs actually improve outcomes? how does an agent's performance change as its SOUL.md grows?" — the lossless capture turns into a research corpus on human+AI collaboration itself.
- ✦ **The recurring stewardship agent (LATER-002):** the weekly meta-maintenance that human teams chronically drop — backlog grooming, doc-drift detection, repo-hygiene heartbeats, dependency sweeps — handled every week by an agent whose working context is the cross-project MetaProject, with its symlinks as the reach into every repo.
- ✦ **Multi-LLM "AI-council" review:** several frontier models critique and cross-check each other before a verdict reaches the human — the adversarial-verify pattern as a quality gate in CI.
- ✦ **A "remote agent" pane in aixocode:** show your Swarm-hosted fleet beside your local terminals — aixocode's local collab subsystem is the laptop-scale precursor of what Swarm does at server scale; lessons flow aixocode → Swarm deliberately.
- ✦ **Agents as tracked contributors with reputations:** persistent identities accrue a record (what they shipped, what got reverted, what reviews caught) — the "agents as colleagues" idea taken to its logical end, including a craft-score that rewards quality over speed.
- ✦ **Engagement Receipts:** cryptographically-signed proof bundles of what an agent-augmented engagement actually delivered — a moat the Phase-D research argues no competitor can ship quickly (see [`../VENTURES/ExoDev.md`](../VENTURES/ExoDev.md)).
