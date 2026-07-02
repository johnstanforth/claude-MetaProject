# Venture Dossier — Lineages & Dormant Assets (Rethought)

> The historical arcs and name-only holdings that give the portfolio its **decade-scale depth** — the data that makes `successor-of` edges, detach-and-reuse, and the feasibility radar real rather than theoretical. Everything here imports as bitemporal lineage edges and IP-asset nodes ([`../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md`](../04-GRAPH-SCHEMA-AND-EDGE-CATALOG.md) §4.3–4.5).

## 1. The four great lineages

### Scalara Inc → ExoDev.Pro (1995→present)
The **Scalara Web Services Framework** (7 generations, C++ then Python, 1995–2012) encapsulated shared server-side functionality so client projects never reinvented the wheel — the conceptual root of today's codemap shared-functionality registry *and* of RosettaMQ. **Scalara Inc** (2002–present, LA; prior names TBD — cross-reference John's LinkedIn) ran project-based web/platform consulting with **no recurring revenue** (clients owned what was built). **ExoDev.Pro** is the business-model evolution: FDSE consulting + vendor-owned licensed platform IP; Dallas incorporates first, then the LA office reboots Scalara's client base ("Scalara is now the LA office" is marketing positioning, not the corporate sequence). **The lesson as an edge:** `no-recurring-revenue → platform-IP-compounds` is the single most important business-model correction in the portfolio's history.

### MobThought → CrowdMadness (2001→present)
`mobthought.com` registered 2001; the venture ran 2004–08 (prediction-market game + the dropped 2002 news-publication angle); stopped over prize-value legal risk; reboot deferred 2010–11 (AdEvolve was thriving); law changed 2018 (PASPA); nobody was watching; rebooted 2026 as CrowdMadness under LLM economics. `crowdresearch.com` held since 2008 — the B2B thesis's quiet 18-year survival. The full treatment: [`CrowdMadness.md`](CrowdMadness.md) §1. **The lesson:** the feasibility radar exists because this arc had no watcher.

### GridTransmit → SensoryMQ (+ CloudXMT → SensoryMQ.Cloud) (~2014→dormant)
**GridTransmit**: national-award-winning (M2M Evolution "Business Impact Award" — exact name to confirm, R-006) GPS fleet-tracking platform, **44,000+ devices across six countries**, carrier contracts with the three leading M2M/IoT wireless providers; the operating business sold back to its main clients ~2018/19. **CloudXMT** (announced on the award stage ~2014/15): a Kubernetes-*precursor* — web-IDE configuration auto-generating, prepackaging, and auto-scaling containers, extending IoT to an AWS-style cloud model *before AWS had IoT features*; headline capability, one-call carrier provisioning replacing 6-week contract negotiations. Never fully launched: Google's Kubernetes announcement (forwarded by collaborator **David Lang**, then at Google MTV) captured the orchestration mindshare. **Validated late anyway:** the 2018 OpenX engagement — 53,000+ server instances reconfigured/upgraded/indexed across geo-distributed datacenters for a co-lo→GCP migration, <$40K/6 weeks vs. outsourcer quotes of $75K+/3 months, via 2 weeks of on-site modeling + ~2 days of orchestration execution. **SensoryMQ** ("Next-Gen Analytics + Machine Intelligence for IoT," subtitle coined pre-ChatGPT) is the idea-stage AI-reimagined successor; SensoryMQ.Cloud its hosting layer, planned to ride open-source RosettaMQ. **Rethink positioning:** any reboot's 2026 wedge is *AI-operated infrastructure* — the OpenX job (model the estate, execute the migration) as a productized agent capability on the Swarm stack — not another orchestrator competing with the Kubernetes ecosystem it lost mindshare to a decade ago.

### The framework line: Scalara Framework → RosettaMQ (1995→future)
**RosettaMQ** (conceived ~2014/15 during GridTransmit): a Rust-based, cross-language modular framework — legacy code in ~a dozen languages transformed into registered modules behind high-performance (millions req/sec) messaging, so migrations *route to extracted modules* instead of rewriting. Ships open-source (`rosettamq.com`); dual nature (a venture we build AND just-another-OSS-dependency our projects consume). Its far target is repaired per R-07: a **retrieval-first expert agent** (versioned framework knowledge graph + codemap extraction via MCP), not a fine-tuned local model. It tames the scattered-language tech debt consulting clients arrive with — which makes it **ExoDev.Pro FDSE tooling** as much as a product: the consulting motion is its distribution.

### AdEvolve (2005–2014) — the historical gate
A marketing company, thriving enough in 2010–11 to *defer the MobThought reboot* — the portfolio's clearest example of a **resource-priority gate** (not a dependency edge; a competing-attention fact). Historical marker; domain held; no current product.

## 2. The name-only inventory (IP-assets, not Ideas)

Per the modeling rule ([`../03`](../03-IDEAS-LEDGER.md) §11): import as `IPAsset` (+ `Venture(shell)` where an entity is named), **zero fabricated theses**, question-mark interpretation edges only where a plausible reading exists, all renewal dates on P-03 runways, all subject to the R-13 annual keep/drop review.

| Asset / shell | What's actually known | `?` interpretation (if any) |
|---|---|---|
| **TXFR.Cloud, Inc.** (`txfr.cloud/.app/.link`; BUY `txfr.com`) | high-speed B2B file transfer (Aspera-like) + device-to-device mobile app; UUID-keyed QR-coded transfers | coherent as stated; dormant — revisit against agent-era data-movement needs |
| **Invendra, Inc.** (`invendra.com/.cc`; BUY `.ai`) | name + one explicit *musing* (TikTok-Shop fulfillment automation for scaling creators) | keep the musing as a `?` edge, nothing more |
| **Dotfigurator.sh / Dotfigurate.me** (`dot8.me`) | OSS dotfiles manager + sharing network | plausible aixocode-adjacent community wedge |
| **VelocityTerminal.sh** | name only, OSS project category | `?`: performance terminal emulator/runtime beside the aixocode Rust/ratatui path |
| **JSL Dragonfly Ltd.** (`jsldragonfly.com`/`jsld.com`) | ad-revenue/YouTube category, no description | none — hold |
| **CTO Mindmeld Publishing, LLC** (`ctomindmeld.com`) | LLC name implies publishing | `?`: John's 25-year-CTO knowledge productized (book/newsletter/course) — name-implied only |
| **Neurogrammatic · Quintivity · Surreality · Transformulator** (+aliases) | bare domains, no entity, no description | none — pure holdings; `surreality.ai` noted as a possible defensive grab in source notes |
| **mobthought.com** (2001) | the lineage anchor | keep as historical/redirect asset — it *documents* the arc |

## 3. Ideation & Exploration

**Existing (carried):** RosettaMQ's language-SDK roadmap (Rust/C++/Python/Go/PHP/Ruby+) · the codemap "Scalara Framework Python revival" extraction target · SensoryMQ's analytics-first IoT framing.

**Proposed (new this rethink):**
- **Lineage as data, systematically:** every arc above imports with dated `successor-of`, `gated`, and `validated-by` edges — the dreaming agent's training set for recognizing *current* shelved-idea reactivation moments (what does 2027's PASPA-repeal-equivalent look like, and for which dormant asset?).
- **The OpenX engagement as a case-study asset:** written up (numbers are already captured) as ExoDev.Pro FDSE marketing collateral — a real, quantified, pre-brand proof of the forward-deployed model.
- **RosettaMQ × FDSE bundling:** every legacy-modernization engagement seeds RosettaMQ modules; the OSS framework accumulates real-world extractions the way the AGPL labs accumulate features — consulting as the framework's data-collection loop.
- **A dormancy review ritual:** the name-only inventory surfaced to GPs annually (with runway costs and any new `?`-edge evidence the dreaming agent attached) — conscious keep/drop instead of renewal-by-inertia (R-13 operationalized).

**Rejected / Flawed:**
- **⛔ Rebooting CloudXMT as an orchestrator.** That war ended in ~2015; the mindshare loss was structural, not a timing accident. Repair: the AI-operated-infrastructure wedge above — sell the *operation*, not the orchestrator.
- **⛔ Backfilling theses onto name-only domains.** Fabricated purposes pollute Layer A and mislead the dreaming agent. Repair: the §2 modeling rule — assets hold value as *options*; options are only valuable if the graph knows they're unexercised.
- **⛔ The R-07 fine-tune target** — repaired in [`../01`](../01-TECHNOLOGY-HORIZON-2026-2029.md) §11; recorded here because RosettaMQ is its home.
