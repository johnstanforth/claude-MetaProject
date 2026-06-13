# Product — spicemaster3000

> John's culinary passion project — a **flavor-tech** app for spice blends, core spices, and flavor
> pairings — and, on the evidence of its research corpus, the portfolio's most credible **standalone
> consumer/B2B venture.** Fully independent of the Divia ecosystem.

- **Names:** "spicemaster3000" (working title) · repo/dir `spicemaster3000` · umbrella TastyPal — see [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- **License:** **Undocumented.** **Status:** 🟡 Phase 00 research **in progress** (a huge corpus); only skeleton Flask code. Positioned **fully standalone** (no Divia/TastyPal ties; only link is the AIXO.Dev workflow methodology + John).

---

## What it is (consensus)
A Python/Flask web app to **explore spice blends, individual spices, and flavor pairings** — for home cooks and spice enthusiasts. Backed by an unusually deep research corpus: **18 analysis tracks** (~18,400 lines, 200+ sources), a parsed *Flavor Bible* dataset of **23,690 pairings / 595 subjects** (6 rank tiers, from ETHEREAL to AVOID), 6 vendor catalogs (Penzeys, Burlap & Barrel, The Spice House, See Smell Taste, Morton & Bassett, Everest), and ratio-based blend formulas. Recommended architecture: SQLite + sqlite-vec for an MVP (offline NetworkX graph analytics → precomputed results), Postgres + pgvector later; FlavorGraph 300D embeddings for similarity/recommendation.

**The venture thesis** (from the synthesis + vision docs): a large spice + personalized-nutrition market; a surveyed gap (35+ apps, none above a C on flavor profiling / blend building / bridge discovery); a hard-to-replicate **data moat**; B2B paths (a Restaurant Partnership API; a White-Label Platform for spice companies). Personal resonance: a partner's "Indian food" anecdote and John's **Nasrani / Saint-Thomas-Christian lineage** (~2,000 years to Cochin, Kerala). Closing line: *"It is time to build."*

## Ideation & Exploration (capture everything, commit to nothing)
*(A small selection of a very large corpus — Track 18 alone enumerates ~50 features across 13 categories.)*
- **Taste personalization:** a 12-axis **taste fingerprint** (radar), supertaster detection, dietary/allergy integration (incl. Jain no-allium), **exposure-gap-vs-genuine-dislike** differentiation (3-state model with gentle re-introduction).
- **Blend builder:** ratio sliders + real-time flavor radar + base/accent/heat auto-classification + synergy/masking modeling; AI-suggested ratios; "what-if" blend simulation; a 50+ classic templates library.
- **Discovery:** the **Flavor Bridge Explorer** ("Mexican → Indian: cumin is the bridge" — flagged the single most distinctive feature); an interactive **flavor-space map** (UMAP, pathfinding); guided "flavor journeys"; "surprise me."
- **Community/smart-kitchen:** user **Spice Cabinets** (virtual inventory + freshness + "what can I make right now"); **Pantry Auto-Replenishment**; "taste-twin" matching; Bluetooth smart-scale guided dispensing; AR spice ID.
- **Moonshots (vision doc):** a **Universal Flavor Translator** ("give me the Mexican version of butter chicken"); genomic taste profiling (23andMe TAS2R38/OR6A2 import); a **Spice Genome Project** (GC-MS of 200+ spices, open-licensed); collective taste intelligence at 1M profiles; the 2031 "cook tonight like our Oaxaca trip, from what's in my cabinet, for my supertaster guest" scenario.
- ✦ **New:** the cleaned **Flavor Bible pairing dataset is a licensable B2B asset** in its own right (to recipe apps, CPG R&D, the spice vendors it catalogs). ✦ The **"Virtual Spice Cabinet" is a specialized TastyPantry** — the clearest unexploited cross-product synergy in the portfolio (shared inventory substrate; neither repo references the other — [`../../ERRATA.md`](../../ERRATA.md)). ✦ Of all the non-dev products this is the **most spin-out-able** (real market, real moat, clean standalone brand, charismatic founder story).
