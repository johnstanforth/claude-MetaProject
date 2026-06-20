# Brief (Software-Dev) — `divia_network` *(STUB — idea-only, no repo yet)*

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase** (repos · upstreams · Build Lines · Build Envelopes · techstack · lineage). Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/DiviaAI/divia_network.md)** (the `Company → Product/Standard` overlap anchors both). **This is a STUB:** Divia.Network is **idea-only — there is no repo, no code, and no Build Lines yet.** It records the *anticipated* engineering role only; everything concrete is **TBD / Unknown (not in source files)**. Do **not** invent repos, stacks, dates, or numbers.

## Project / repo

| Field | Value |
|---|---|
| **Repo / dir** | **None — no repo exists.** Idea-only. (A future repo would plausibly be `divia-network` / `divia_network`, but **none is created or named in any source.**) |
| **GitHub** | **None.** |
| **Techstack** | **Unknown (not in source files).** Anticipated to align with the Divia.AI server stack (the Rust Enterprise core / AgentSwarms backbone), but **not specified** — do not assume. |
| **License** | **Unknown (not in source files).** As an *open* "HTTP-like standard," an open contract/spec is plausible, but no license is documented. |
| **Maps to business Product/Standard** | Divia.Network (the open ecosystem integration layer / API standard). |
| **Status** | **Idea-only / aspirational (v2).** The v0 contract is "still being designed." A "forgotten earlier prototype" is referenced by John but **undocumented**. |

## Build Lines · Build Envelopes · Triangulation Target

**No Build Lines yet.** There is no engineering codebase delivering Divia.Network, so there are **no Build Lines, no Build Envelopes, and no Triangulation Target to record** at this time. These will be defined if/when the standard graduates from idea to a built spec/implementation — most likely as a contract *emergent from* the first real cross-app integrations (the fan-out), not as a greenfield repo.

- **Anticipated Build Envelope (speculative, not committed):** would inherit the Divia.AI "Seed → Enterprise" trajectory — prototype the contract in the open Python `diviahome-web` lab, then harden into the Rust Enterprise/AgentSwarms core. **Unconfirmed.**
- **Triangulation Target (anticipated):** a stable, open, versioned cross-app **integration standard** ("HTTP-like") that any Divia app (and external "certified participants" like FracRealHomes) can speak — carrying both fan-*out* (one capture → many apps) and fan-*in* (many apps → one digest), uniformly for humans, apps, and agents. **Aspirational only.**

## Anticipated engineering role (idea-only)

Divia.Network is anticipated to be the **federation / integration layer atop the Divia.AI Enterprise graph-DB core** — the open, HTTP-like API standard over which the Divia family of apps integrate. It is **plumbing, not an app**: it would define how a natural-language capture in DiviaHome's Activity Log, once classified by an **AgentSwarms** agent, is **dispatched to multiple downstream apps** (TastyPantry / Sattvasic Health / LegendaryMoney), each recording its own slice and cross-linking back to the original. The **first real cross-app integrations are the proving ground** for its v0 contract — i.e. the standard is expected to be *discovered by building the integrations*, not designed up-front in isolation.

Note the **two distinct "federation" axes** (do not conflate): Divia.Network = **app-to-app integration** (this entity); **Divia.AI Global (SaaS)** = **identity/auth federation** ("one global Divia.AI username" across home/work servers). Different layers; both aspirational.

## Dependencies (anticipated)

| Depends on | Why (anticipated) | Status |
|---|---|---|
| **Divia.AI Enterprise** (`divia_ai-enterprise`) | The **graph-DB convergence core** the network would sit atop; the one hub where shared core functionality concentrates — downstream products are clients, not copies. | Enterprise itself is **not started** (no repo); this is a dependency on a not-yet-existing core. → [eng brief](divia_ai-enterprise.md) |
| **DiviaCards** (`divia_cards`) | The **typed content-block payload / public contract** apps would exchange over the network. | Repo exists (local only); → [eng brief](divia_cards.md) |
| **Divia.AI AgentSwarms** (`divia_ai-agentswarms`) | Hosts the **agents that perform** the fan-out classification + cross-app delegation. | Intended proprietary Rust backbone. |
| **DiviaHome** (`diviahome-web`) | **Capture origin** (the Activity Log) and the open prototype where the v0 contract's lessons are learned; gating foundation (DiviaHome v1 "unify, then understand"). | Pre-code (Phase 00). |
| **DiviaMesh** *(component)* | Lower-level **sync protocol** (Rust; WebSockets/WebRTC/ZeroMQ + Loro CRDT). **Distinct** layer — sync vs. integration; the prose boundary between the two is not crisply drawn (e.g. `divialife.md`: "syncs via DiviaMesh / Divia.Network"). | Component, undocumented. |

## Git topology / lineage

**None yet — no repo, no lineage.** If/when built, the anticipated relationship is **client-of / standard-over** the Divia.AI Enterprise core (succession/clone-lineage topology → **TBD**). The "forgotten earlier prototype" John references could become a lineage ancestor once located, but it is currently **Unknown (not in source files)**.

## `[DEALBREAKER-HOOK]`s

**None defined yet (idea-only).** Identifying the irreversible forks is premature with no Build Line. **Anticipated candidates** to watch when the standard is first built (speculative, not committed):

- **The v0 wire/payload contract shape** — versioned cross-app message schema (carried via DiviaCards?); getting the envelope/versioning wrong now would force a later rewrite once multiple apps speak it.
- **Source-neutral, federation-ready IDs** — consistent with the entity-model synthesis's "UUIDv7-private-by-default / source-neutral IDs" hooks already honored in the KingStrat graph-DB spikes, so cross-app references survive federation.
- **The agent-authority / trust boundary** — staging-vs-committing across app boundaries (an agent staging entries in four apps, committed only on confirmation) as a first-class contract concern.

*(These mirror hooks already surfaced upstream in the graph-DB R&D; they are listed here only as anticipated, not as decided.)*

## Cross-references

- Paired business brief (carries the concept): [`../ULTIMATE_VISION/PRODUCTS/DiviaAI/divia_network.md`](../ULTIMATE_VISION/PRODUCTS/DiviaAI/divia_network.md).
- Anticipated core dependency: [`divia_ai-enterprise.md`](divia_ai-enterprise.md) · payload contract: [`divia_cards.md`](divia_cards.md).
- Model: [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md).
