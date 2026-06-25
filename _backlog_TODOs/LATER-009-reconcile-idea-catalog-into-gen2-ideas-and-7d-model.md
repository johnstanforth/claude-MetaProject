# LATER-009 — Reconcile IDEA_CATALOG.md into the GEN2 Ideas list, and use the richer dataset to pressure-test the KSVGPS "7-dimensional" knowledge model

- **Captured:** 2026-06-25
- **Status:** open — the wide-net [`IDEA_CATALOG.md`](../_REFERENCE/IDEA_CATALOG.md) was produced this session (merging the `ULTIMATE_VISION/*` docs, the `SOFTWARE_DEV` briefs, the `DOMAIN_*`/notes/model docs, **and** the scattered `_EXTERNAL` reference-repo index notes). Consolidation against the already-imported Ideas is deferred to a KSVGPS graph-DB / Ideas-import pass.
- **Eventual owning project:** KSVGPS (`kingstrat-adventuregps`) Strategic-Landscape / Ideas-Topics model. The canonical Ideas currently live as the ~61 `_REFERENCE/ULTIMATE_VISION/IDEAS/*.md` node files, already imported into the throwaway **`aixodev-GEN2`** database as Layer-A Idea entities.
- **Related:** [`_REFERENCE/IDEA_CATALOG.md`](../_REFERENCE/IDEA_CATALOG.md), `_REFERENCE/ULTIMATE_VISION/IDEAS/`, `~/Code/_REFERENCE/external_projects/` (the resurfaced-prior-art source), `_REFERENCE/STRATEGIC-LANDSCAPE-MODEL.md`, `_REFERENCE/PROJECT-ORGANIZATION-MODEL.md`, `_REFERENCE/GEN2-MODEL-AND-POPULATE-PLAN.md`; [LATER-007](LATER-007-aixodev-web-entity-model-spec-mining.md) (entity-model spec mining), [LATER-008](LATER-008-domains-vs-urls-two-entity-types-in-ksvgps.md) (the domains-vs-URLs split, itself a "7-dimensional modeling enabler").

## The work to revisit

1. **Reconcile** `IDEA_CATALOG.md` against the canonical Ideas already imported into GEN2 (the ~61 `ULTIMATE_VISION/IDEAS/` node files). For each catalog bullet, classify it: already an Idea node · a genuinely new Idea · a *feature / sub-idea* of an existing Idea (finer grain than the current flat Idea layer models) · or a duplicate. The catalog was deliberately **over-inclusive** (duplicates preserved, never flattened), so the dedupe/merge/mis-home calls are John's — that intent lives in his head, not in the source files.
2. **Fold the net-new ideas in** — especially (a) the ideas **resurfaced from the `_EXTERNAL` reference repos** (e.g. the e-paper Divia Agenda desk-display, graphologue's real-time inline LLM diagrams, zero-share's WebRTC P2P for TXFR.App, dano's cross-container media dedup) that no `IDEAS/` node yet captures, and (b) the **cross-cutting patterns/theses** the catalog names (the implicit-data manifesto, "first unify then understand," the confidence-aware/suppression-as-first-class seam, the time-decay-priority primitive).

## Why it matters (the real prize — not just "more ideas")

The headline value is that the catalog surfaced **structure the flat Idea list can't represent** — and that structure is precisely the higher-complexity ("7-dimensional") knowledge representation KSVGPS is trying to reach. The reconciliation is therefore a **dataset for reasoning about the model**, not merely content to import:

- **Sub-grain (Idea ↔ Feature):** many catalog entries are features/sub-features under a product-line, not top-level Ideas → the model may need an Idea-nests-Idea / Idea-has-Feature relationship the current layer lacks.
- **Cross-cutting reusable primitives** (time-decay priority, confidence-aware ledger, scan-and-import) recur across many ventures → these want to be shared **pattern nodes** with many-to-many edges to the products that instantiate them — exactly the higher-order relationship the 7-D model is reaching for.
- **Provenance/lineage types:** an idea resurfaced from an external repo (a prior-art edge), an idea stated in a venture brief, and an idea merely implied by a held domain name are *different provenance kinds* — the model should distinguish them.
- **Relationship shapes that must not collapse:** "same Idea at a different scale" (launch-market AVM vs National-AVM) and "same engine, different customer" (PatternicityNews portal vs the NER B2B data product) are distinct edge shapes, not duplicate nodes.

## Concretely

- Treat `IDEA_CATALOG.md` as a **review worksheet**: John marks dupes / merges / mis-homes; the survivors + their relationships become the GEN2 Ideas update.
- Before re-importing, decide the **Idea-vs-Feature grain** question and whether **cross-cutting patterns** get their own node type.
- Capture any **new relationship dimensions** the reconciliation reveals back into `STRATEGIC-LANDSCAPE-MODEL.md` / `GEN2-MODEL-AND-POPULATE-PLAN.md` — this is the concrete feedstock for refining the KSVGPS 7-D model (alongside LATER-007 and LATER-008).
