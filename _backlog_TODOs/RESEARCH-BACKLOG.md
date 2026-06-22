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

### R-003 — The Idea/Venture two-layer model: durable Ideas & Topics, time-bounded Venture channels, multi-decade arcs
- **What:** The graph-DB entity model for the KSVGPS Strategic Landscape (Module 1), now designed in [`STRATEGIC-LANDSCAPE-MODEL.md`](../_REFERENCE/STRATEGIC-LANDSCAPE-MODEL.md): a **two-layer** structure — durable, brand-free **Ideas** (tagged many-to-many to a **Topic** taxonomy, carrying their own research) above time-bounded **Venture/brand channels** (Layer B), connected by a **channel symlink** (Idea→Venture, time-bounded; **detaches on pause/pivot** so the Idea returns to Layer A for reuse). Plus: `successor-of` / `historically-owned` / `depends-on` / `variant-of` / `enables` edges; the *same-idea-different-scale* rule; **a Build Line realizes an Idea** (one Idea → several Build Lines across scale); the dimensional axes re-homed (Conviction/Horizon/Provenance/Leverage on Ideas; Wave/Founder-fit on Venture-instantiations); and **ACL-scoping** (a firm researcher sees Layer A only; a GP sees both). MobThought→CrowdMadness is the canonical multi-decade case — already the lead example in `kingstrat-adventuregps`'s entity-model research (`analysis-03--lineage-successor.md`).
- **Why it matters / criticality:** `shaping` — this is the core KSVGPS business-side graph-DB schema; the markdown bootstrap (`STRATEGIC-LANDSCAPE-MODEL.md` + the `ULTIMATE_VISION/IDEAS/` and `TOPICS/` trees) is the manual proto-version we iterate before implementing it.
- **Trigger / venture:** KSVGPS graph-DB / the venture-studio reframing (John confirmed the two-layer model 2026-06-22).
- **Status:** open — design in progress (the markdown bootstrap is being built).

### R-004 — Topic-hub + vector-segmentation architecture for a million-entity news graph
- **What:** For PatternicityNews's entity graph — **topic-hubs** (dozens of graphs/clusters with inter-vertices: one partitioned graph vs. many?) and **vector-search segmentation** so distance is meaningful *within* a topic (per-topic vs. global embedding spaces; topic-boundary definition; entity-resolution / dedup at scale).
- **Why it matters / criticality:** `shaping` — PatternicityNews's central ongoing engineering investment and a likely `[DEALBREAKER-HOOK]`.
- **Trigger / venture:** PatternicityNews (data-architecture).
- **Status:** open.

### R-005 — The "three waves of business" (Cringely, ~1999–2000) and its modern applicability
- **What:** Deep-dive into Robert X. Cringely's **"three waves"** model — first-wave (garage / new-market pioneers; "Navy SEALs who take the beach, 10× the normal soldier"), second-wave (the regular army scaling/expanding), third-wave (the "police force" maintaining a successful/monopoly position, e.g. 1990s Microsoft). Plus the corollaries: why 2nd/3rd-wave firms innovate by **acquiring** first-wave companies rather than internally; and why the *people* who excel at first-wave work (ambitious new-market ideation) differ fundamentally from third-wave operators (scaling to a billion users — e.g. the Google-SRE lift-and-shift of the YouTube acquisition). Find Cringely's original source + modern equivalents/critiques (Christensen disruption, Geoffrey Moore's TALC/chasm, founder-vs-operator literature).
- **Why it matters / criticality:** `shaping` — a core lens for the **KSVGPS Strategic-Landscape dimensional model** (the *business-wave* and *founder-fit* axes): it explains why John (a first-wave person) treats far-future scaling stages as "a different company I wouldn't run," and how to tag an idea's wave / scale / who-runs-it over its arc.
- **Trigger / venture:** KSVGPS Strategic-Landscape modeling (John-flagged). Candidate first-test topic for the multiagent research workflow.
- **Status:** open.

### R-006 — Confirm the GridTransmit M2M-Evolution award (exact name, category, year)
- **What:** Confirm the precise name of the award GridTransmit won at the **M2M Evolution conference** (~2014/2015) — John recalls a "Business Impact Award" or similar; verify the exact title/category/year (the *M2M Evolution* conference later rebranded to *IoT Evolution*). A factual-record confirmation, not a deep research topic.
- **Why it matters / criticality:** `enriching` — provenance/credibility detail for the GridTransmit case study and the SensoryMQ reboot story.
- **Trigger / venture:** GridTransmit / SensoryMQ ([`iot-connected-device-platform`](../_REFERENCE/ULTIMATE_VISION/IDEAS/iot-connected-device-platform.md)). John-flagged (2026-06-22).
- **Status:** open.
