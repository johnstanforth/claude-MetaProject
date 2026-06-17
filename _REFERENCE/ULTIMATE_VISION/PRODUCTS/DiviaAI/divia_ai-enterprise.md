# Product — Divia.AI Enterprise

> The commercial **Rust team server** — "a higher-performance, locked-down, Rust re-implementation of
> the DiviaHome server" — paired with the Divia.AI Professional desktop client. Deliberately not
> started yet; its specialized descendant becomes the **Divia.AI Global (SaaS)** identity service.

- **Names:** "Divia.AI Enterprise" · repo/dir `divia_ai-enterprise`.
- **Umbrella / venture:** DiviaAI — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **License:** **Proprietary / commercial** (server license + per-seat client licenses; explicitly **not** AGPL). Stated in prose only; no LICENSE file.
- **Status:** ⚪→🟠 Intentional empty placeholder — a single provisional README, **not yet even a git repo.** Begins only after **DiviaHome v1 + ~30 days of real use.**

---

## What it is (consensus)
A commercial Rust team server for full client-server workgroup collaboration: centralized management, permissions/roles, shared workspaces, version history, real-time multi-user editing — with Divia.AI Professional as its desktop client. The **developer-honest framing:** Enterprise *is* "a higher-performance, locked-down, Rust-based version of the Python/Flask DiviaHome server" (the marketing version is "rather more elaborate 😀"). Early direction: Rust + Tokio; **DiviaMesh** client-server sync (WebSockets) with a **Loro/CRDT** document model; eventual **RosettaMQ Framework** base (+ Cloudflare Rust libs); multi-tenant, locked-down.

**The sequencing rationale** (a portfolio-defining decision): prototype + converge in Python first (DiviaHome + the lab apps), *then* harden into Rust — because Rust iterates slowly and committing functionality before daily-use validation would lock in unvalidated choices.

### The strategic endgame — Divia.AI Global (SaaS)
A specialized, upgraded build of Enterprise becomes the proprietary internal **Divia.AI Global (SaaS) Service**: the central identity/auth authority behind "one global Divia.AI username," federating a user's home (DiviaHome) and work (Enterprise) servers. The Python prototypes already carry **placeholder global-identity fields** so the later migration is painless. (See [`../../USER_STORIES/federated-home-and-work.md`](../../USER_STORIES/federated-home-and-work.md).)

> ⚠️ Framing conflicts ([`../../ERRATA.md` E-08`](../../ERRATA.md)): this README never mentions **Swarm** or an "AI backbone," yet `divia_ai-agentswarms` describes Enterprise as "a PKMS + Asana-style task server co-deployed with Swarm for AI." The Swarm co-deployment is asserted only from Swarm's side. Target market (per the DiviaContacts reframing): SMEs, deployed on the company office network, administered by corporate IT, from a handful to thousands of users per location.

## Ideation & Exploration (capture everything, commit to nothing)
- **From the README:** Divia.AI Global as the long-term identity/auth/federation layer; per-server "client roles" (a DiviaHome server acting as a federated node under Global); "prototype-in-Python, harden-in-Rust" as explicit methodology; the four-app "lab" as the discovery ground for the Divia.Network v0 contract; eventual RosettaMQ + Cloudflare-Rust migration; a possible **Divia.Foundation "Code Vault"** release later. Open questions: which DiviaHome v1 learnings carry vs. get redesigned for Rust; the Enterprise-vs-Global codebase boundary (shared vs. fork).
- ✦ **New:** **"Research Projects" as Enterprise's marquee knowledge-work feature** (from LATER-002) — agent-tended, continuously-updated bodies of knowledge built on `.dvai` LiveDocuments; the first buyer is KingStratVC (a self-refreshing portfolio dossier). *(Not yet in the repo — [`../../ERRATA.md` E-12`](../../ERRATA.md).)* ✦ **Write one canonical Enterprise definition** that reconciles the three framings (collaboration/sync server vs. Asana-PKMS+Swarm vs. Pro's-server) — Enterprise is described three different ways across the repos and needs a single source of truth (this doc is the start). ✦ The consultancies (ExoDev.Pro) and the recurring-agent GTD review are both natural first Enterprise use-cases — dogfood and demo in one.
