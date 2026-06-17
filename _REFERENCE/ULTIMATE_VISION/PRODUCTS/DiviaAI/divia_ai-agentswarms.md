# Product — Divia.AI AgentSwarms

> The Rust server that provides **containerized hosting for autonomous Divia.AI agents** — the intended
> **AI backbone of the whole ecosystem.** In the OpenClaw/NanoClaw family; usable standalone, designed
> to co-deploy with Enterprise and transparently power AI features everywhere.

- **Names:** "Divia.AI AgentSwarms" · repo/dir `divia_ai-agentswarms` · code id `divia-agentswarms` · env prefix `DIVIA_AGENTSWARMS_`.
- **Umbrella / venture:** DiviaAI — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **License:** **Undocumented** (intended proprietary, by ecosystem analogy — not stated in-repo).
- **Status:** 🟠 Just bootstrapped — workflow scaffold + README/CLAUDE only; Rust + Cargo settled; **Phase 00 (Ideation & Research) is NEXT.**

---

## What it is (consensus)
A Rust server hosting **multiple autonomous Divia.AI agents in isolated containers** — explicitly the same family as **OpenClaw / IronClaw / PicoClaw / NanoClaw / Hermes Agent.** Standalone, it works "out of the box" like those tools (an IT dept could stand it up like OpenClaw/Hermes). Its designed-for role is the **AI backbone**: containerized agents hold **real-time connections (WebSocket, ZeroMQ, etc.)** to the other products and transparently power their AI ("shock and awe") features — explicitly the right-sidebar AI chat in Divia.AI Professional, and the agent-powered upgrades to Enterprise's document/task/project features. Everything beyond "Rust + Cargo" is deferred to Phase 00: async runtime (likely Tokio), web/RPC framework, real-time transport, container/sandbox runtime, database.

### Phase 00 scope (four tracks)
1. A **competitive deep-dive** of the OpenClaw/IronClaw/PicoClaw/NanoClaw/Hermes field (architecture, agent lifecycle, scheduling/supervision, isolation/sandboxing, integration surfaces) — positioning how Swarm *differs and improves.*
2. **Stack selection** (async runtime, web/RPC framework, container runtime, DB).
3. **Agent isolation & resource model** (per-agent CPU/memory/network limits, cross-container invariants).
4. **Integration architecture** (the real-time protocol for Enterprise/Professional/other clients).

*(Rich competitive lore on the OpenClaw family already lives in `divia_ai-professional/_research/autonomous_agents_landscape_2025_2026.md` — e.g. OpenClaw's WhatsApp/Telegram messaging-app control plane, ClawHub skills, the Clawd→Moltbot→OpenClaw rename, NemoClaw/NanoClaw variants.)*

## Cross-product role
The **body** in the brain/body/face split (LATER-002 §8): owning products define *what/when/who-approves*; Swarm provides the agent that executes. It's the server-scale successor to aixocode's laptop-scale collaboration subsystem (lessons flow aixocode → Swarm). The Swarm↔Enterprise AI co-deployment is currently asserted only from Swarm's side ([`../../ERRATA.md` E-08`](../../ERRATA.md)).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** standalone "works like OpenClaw out of the box" parity (implies a minimal built-in scheduler, with owning products as the richer optional brains); position Swarm as the *ecosystem backbone* — a differentiator none of the OpenClaw-family competitors claim.
- ✦ **New (from LATER-002):** **typed workflow steps** — model a recurring Swarm task as a workflow whose steps are explicitly **deterministic (plain code: a git pull, a SQL aggregate, a file diff) or probabilistic (an LLM call)**, with each probabilistic step declaring its effort tier (Haiku-medium for mechanical passes, Fable-xhigh for judgment/synthesis). Makes cost, reproducibility, and "where the AI actually is" legible at the workflow level, and dovetails with the deterministic-gate guardrails. *(Not yet in the repo — [`../../ERRATA.md` E-12`](../../ERRATA.md).)*
- ✦ **Swarm as the body for every recurring-agent story in this reference** — the GTD reviewer, the household nightly loop, the dev-stewardship agent, the KingStratVC partners' brief all run *on* Swarm; the competitive deep-dive should explicitly evaluate each framework's answer to **recurring scheduled tasks** and **ecosystem/product integration** (the two axes Swarm intends to win).
- ✦ **Resident-vs-ephemeral resolution** (LATER-002 §8) — likely "ephemeral execution + durable externalized memory," giving both the cheap-reproducible job model and the long-lived relationship/memory the "decades" vision needs.
- ✦ **Declare a license in Phase 00** — a commercial-intent Rust server with no stated license is a gap to close alongside Enterprise's proprietary stance.
