# Idea — Agent-hosting & orchestration server

> Layer-A Idea node (durable · brand-free). Model: [`STRATEGIC-LANDSCAPE-MODEL.md`](../../STRATEGIC-LANDSCAPE-MODEL.md). **Bootstrap seed.**

- **Topic(s):** [ai-agents-orchestration](../TOPICS/ai-agents-orchestration.md).
- **One-line:** A server that hosts **multiple autonomous AI agents in isolated containers** — the "AI backbone" that transparently powers AI features across a whole product ecosystem (standalone like OpenClaw/Hermes; designed to co-deploy and integrate).
- **Axes (Idea-level):** Conviction = **serious-someday** (just bootstrapped; Phase 00 NEXT) · Horizon = **~3yr / far** (Rust + Cargo settled, everything else deferred to Phase 00) · Provenance = the OpenClaw/IronClaw/PicoClaw/NanoClaw/Hermes agent-framework family · Leverage = the server-scale successor to aixocode's laptop-scale collaboration subsystem (lessons flow aixocode → here); real-time transports (WebSocket, ZeroMQ).
- **Idea↔Idea edges:** `depends-on` → [graph-DB entity-knowledge engine](graph-db-entity-knowledge-engine.md) (the co-deployed Enterprise core it powers — asserted from this side only, ERRATA E-08) · `enables` → [recurring autonomous-agent tasks](recurring-autonomous-agent-tasks.md) (the body that runs them) · `enables` → [cross-app integration standard](cross-app-integration-standard.md) (hosts the agents that perform the fan-out).
- **Channel (Idea→Venture, time-bounded):** [Divia.AI AgentSwarms](../PRODUCTS/DiviaAI/divia_ai-agentswarms.md) (just bootstrapped; Phase 00 NEXT; license undocumented/intended-proprietary).
- **Realized by (Build Lines, Layer B):** TBD — `divia_ai-agentswarms` (Rust; Phase 00 not yet scoped beyond "Rust + Cargo"). The "body" in the brain/body/face split (LATER-002 §8).
- **Research:** Phase-00 competitive deep-dive of the OpenClaw-family field (architecture, agent lifecycle, scheduling/supervision, isolation/sandboxing, integration surfaces) — see the AgentSwarms brief.
- **Notes:** Source = [AgentSwarms product brief](../PRODUCTS/DiviaAI/divia_ai-agentswarms.md) + [`LATER-002`](../../../_backlog_TODOs/LATER-002-recurring-autonomous-agent-tasks.md) §2/§8. Resident-vs-ephemeral resolution likely "ephemeral execution + durable externalized memory."
