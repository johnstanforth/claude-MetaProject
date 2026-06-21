# RESEARCH Backlog — cross-venture research topics

Standing aggregation of topics we know we need to **research** before (or while) committing a venture's architecture or business model. Distinct from the `LATER-{NNN}` deferred-TODO items (which are decisions/obligations): this file is a flat, growing list of **research questions**, the destination for the `[Backlog:RESEARCH]` shorthand used in venture-brief answers. Reviewed to pick topics for the **multiagent research workflow** (the early-wide-net + late-adversarial-audit Claude×Codex process).

> Convention: one `###` entry per topic — *what · why-it-matters · trigger/venture · criticality · status*. **Criticality:** `blocking` (a route can't be committed without it) · `shaping` (changes the design) · `enriching` (nice to know). **Status:** open / queued / researching / done. Captured topics survive even after they graduate — note where they went, don't delete.

---

### R-001 — Wikipedia static-dump licensing for a commercial derived entity-graph
- **What:** Can we ingest the Wikipedia static dump + periodic updates into an internal copy and build a **commercial** NER-primed entity graph (people / places / companies + relationships) on top of it? CC BY-SA share-alike scope, attribution obligations, the derivative-work-vs-separate-database line, and **Wikidata (CC0)** as an alternative/complement.
- **Why it matters / criticality:** `blocking` for PatternicityNews — Wikipedia is its *primary* NER-priming source, and share-alike could encumber the derived graph that is the venture's core moat.
- **Trigger / venture:** PatternicityNews (tech/data-architecture). John-flagged in the first question round.
- **Status:** open.

### R-002 — Prediction-market / gambling legality, incl. prize-value games (2004 → present)
- **What:** The full regulatory arc, in **two layers**. **(a) The market layer:** the **2018 PASPA repeal** (Murphy v. NCAA) → legal sports betting → FanDuel/DraftKings; then **Polymarket / Kalshi**, the **CFTC** event-contract regime, per-state rules, **and the *current* state-AG enforcement/litigation against Polymarket & Kalshi** (which states bar them, on what theory). **(b) The prize-value layer — the one that actually stopped MobThought in 2008:** even a **play-money / prizes-only "game"** can be deemed gambling if prizes carry enough value. MobThought gave non-cash prizes (e.g. big-screen TVs to winners predicting CBS *Big Brother* outcomes), and state AGs could read that as **constructively circumventing** anti-gambling law. So "we're just a game" is **not** automatically safe — the line between a lawful sweepstakes/game and constructive gambling (prize value · consideration · chance-vs-skill) must be researched **even if CrowdMadness only ever does gamified non-cash prizes.**
- **Why it matters / criticality:** `blocking` + the venture's reason-to-exist-now. The prize-value risk means this gates *every* version, not just a hypothetical real-money one. Also scopes a core feature — an **autonomous agent that tracks state/federal regulatory change nightly** and emits required-app-change diffs (the LLM-economics thesis: thousands in engineering vs. the tens-of-millions in legal that made the model infeasible in 2005).
- **Trigger / venture:** CrowdMadness. John-flagged (incl. the current Polymarket/Kalshi state-AG fights and the MobThought *Big Brother* prize-value precedent).
- **Status:** open.

### R-003 — Modeling multi-decade idea-arcs with pause/reboot in the graph-DB
- **What:** How to represent a venture that spans decades with a gap: vague idea (pre-name) → named → prototype → wind-down/pause → **reboot-as-successor** years later, with `successor-of` / `historically-owned` edges across a moving "today," distinct from a simple rename or a v2. MobThought→CrowdMadness is the canonical case — already the lead example in `kingstrat-adventuregps`'s entity-model research (`_specs_and_plans/_research/entity_model_and_graph_db/analysis-03--lineage-successor.md`).
- **Why it matters / criticality:** `shaping` for the KSVGPS business-side graph-DB schema (the venture-studio reframing makes decade-arcs the norm, not the exception).
- **Trigger / venture:** KSVGPS graph-DB / the venture-studio reframing.
- **Status:** open.

### R-004 — Topic-hub + vector-segmentation architecture for a million-entity news graph
- **What:** For PatternicityNews's entity graph — **topic-hubs** (dozens of graphs/clusters with inter-vertices: one partitioned graph vs. many?) and **vector-search segmentation** so distance is meaningful *within* a topic (per-topic vs. global embedding spaces; topic-boundary definition; entity-resolution / dedup at scale).
- **Why it matters / criticality:** `shaping` — PatternicityNews's central ongoing engineering investment and a likely `[DEALBREAKER-HOOK]`.
- **Trigger / venture:** PatternicityNews (data-architecture).
- **Status:** open.
