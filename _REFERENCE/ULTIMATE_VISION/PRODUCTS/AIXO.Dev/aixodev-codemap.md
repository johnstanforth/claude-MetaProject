# Product — aixodev-codemap

> A source-code analysis prototype that maps a codebase at three levels — structural call graphs,
> semantic "feature inventory," and AI-mediated cross-project comparison. Research claims no existing
> tool combines all three. Folds into `aixodev-web`.

- **Repo:** `aixodev-codemap` · **Umbrella:** AIXO.Dev · **License:** Proprietary (`LicenseRef-Proprietary`, "AIXO.Dev Platform LLC").
- **Status:** 🟡 Phase 0 research complete (21-track, ~168K words); **Phase 1 prototype 2 of 6 sprints** (Python structural extraction only; 139 tests). Flask · SQLAlchemy · SQLite.

## What it is (consensus)
Three analysis levels over a 12-table schema (polymorphic `symbols`, universal `code_edges`, `features`/`feature_memberships`/`feature_equivalences`, append-only `scan_versions`): **(1)** structural — call graphs, symbols, edges, module deps (built; tree-sitter, pyan3, Jedi, vulture); **(2)** semantic — a "feature inventory" of named clusters (designed; igraph Leiden community detection + LLM labeling — *unbuilt*); **(3)** AI-mediated **cross-project comparison** (designed). Signature use case: *"which of my 40 repos implement JWT auth, how do they differ, which should be canonical?"* → presence detection → semantic equivalence → structural comparison → an LLM quality verdict. Graphify is a **selective-extraction source, not a fork** (John's call). Feeds a planned "shared functionality registry" (Independent Implementation Rate, Version Fragmentation Index).

## Ideation & Exploration (capture everything, commit to nothing)
- **From research/backlog:** graph-DB layers (Apache AGE / Neo4j / FalkorDB / DuckDB+DuckPGQ); SCIP ingestion; Rust extraction (tree-sitter-rust + cargo-modules + rust-analyzer); cross-language Python→Rust edges via PyO3; mutation testing as a migration gate; property/contract (Pact) tests for extracted libs; `sqlite-vec` → `pgvector` embeddings (UniXcoder/VoyageCode3); FTS5 symbol search; Strangler-Fig/InnerSource migration governance; the "comprehension debt" of AI-generated code. Named extraction targets: **RosettaMQ** (Rust) and a **"Scalara Framework"** Python revival.
- ✦ **New:** point codemap at the *whole MetaProject* — its cross-project comparison is exactly the tool the LATER-002 "shared functionality registry" + "documentation-drift detection" recurring agents need; the registry it produces is the data backbone for the stewardship agent that catches reuse-vs-reimplementation across all 24 repos. ✦ Use it to *measure* the convergence John keeps describing (prototypes merging into aixodev-web; KingStrat's shrinking delta) with hard numbers instead of intuition.
