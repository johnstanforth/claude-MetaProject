# Brief (Software-Dev) — `fracrealhomes`

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase** (repos · upstreams · Build Lines · Build Envelopes · Triangulation Targets · Stages→Phases→Sprints · lineage · `[DEALBREAKER-HOOK]`s · dev discussions). Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/FracRealHomes/fracrealhomes.md)** (the `Company → Product` overlap anchors both). Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Status: scaffold** (Phase 00 pending; pre-code). *Good-enough bootstrap — anchored on the PROJECT-ORGANIZATION-MODEL FracRealHomes worked example + the `fracrealhomes-web` SORTING-PASS / dealbreakers research.*

## Project / repos

| Repo / dir | Surface | Techstack | License | Status |
|---|---|---|---|---|
| **`fracrealhomes-web`** | Python/Flask web application (primary surface) | Python 3.12+ · `uv` · Flask (app-factory + Blueprints + Jinja2) · SQLAlchemy 2.0 · SQLite→PostgreSQL · Flask-Migrate/Alembic · pydantic-settings (`FRACREALHOMES_`) · Bootstrap (CDN, tentative) · pytest · Ruff | Proprietary / commercial, closed-source (© 2026 Fractional Reality Homes LLC) | Phase 00, pre-code |
| **`fracrealhomes-flutter`** | Cross-platform Flutter/Dart mobile app (iOS + Android); **mirrors the web app** | Dart 3.x · Flutter (stable) · `flutter pub` · state-mgmt / on-device-store / offline-sync **Phase-00 pending** · `flutter test`/`analyze` · `dart format` | Proprietary / commercial, closed-source | Phase 00, pre-code (placeholder) |
| **`fracrealhomes-android`** | Native **Kotlin/Android** **3D virtual-home capture & reconstruction** app (Zillow-3D-Home equivalent); **separate long-term product**, not a throwaway | Kotlin · Android · Gradle (AGP, Kotlin DSL) · UI/arch/DI/data/capture/AR/3D-reconstruction **open, firmed in Phase 01** · `./gradlew build`/`test`/`lint` | Proprietary / commercial, closed-source | Phase 00, pre-code (placeholder) |

- **GitHub remotes:** **Unknown (not in source files)** — all three repos are described as **local-only, no remote**; `fracrealhomes-web` CLAUDE.md explicitly forbids any remote-git interaction ("NEVER interact with remote git servers").
- **Maps to business Products:** `fracrealhomes-web` + `fracrealhomes-flutter` → the **EstimatePacket** product (web + mobile surfaces); `fracrealhomes-android` → the **FracRealHomes 3D Home** product. *(Business side: [brief](../ULTIMATE_VISION/PRODUCTS/FracRealHomes/fracrealhomes.md).)*

## Build Lines · Build Envelopes · Triangulation Target

*(Verbatim from the PROJECT-ORGANIZATION-MODEL FracRealHomes worked example, plus the android 3D-capture Build Line which the model's table — scoped to the diligence Product — does not itself enumerate.)*

| Build Line | Build Envelope | Role / status | In the Product's Version-Releases? |
|---|---|---|---|
| **DailySpikeDriver** | "Playground" (John only · Python/Flask · idea-of-the-day) | Private dogfood + experiment playground; **merges up** into the EstimatePacket Line. A "Zillow-email triage parser *for my own use*" is a first-class DailySpikeDriver feature with **zero** obligation on the venture's PRD. | **No** — private, never released |
| **EstimatePacket Line** *(middle, near-term product)* | "Seed" (6–18 mo · ~50–100-person startup · ~20–40-person dev · Python/Flask) | The **near-term shippable product** — the SORTING-PASS diligence scope (EstimatePacket). The codebase that delivers the web + mobile surfaces. | **Yes** — delivers public **v1.0 → v4.0** |
| **National-AVM Line** | "Enterprise" (3–5 yr · regulated multi-market · different stack) | The far-future public/national AVM (Codex's research home; a categorization bucket for now). | **Yes (later)** — delivers public **v5.0+** (**succession, no-merge**) |
| **3D-Capture Line** *(`fracrealhomes-android`)* | "3D-Product" (native Kotlin/Android · long-term · capture/AR/photogrammetry — Phase 01 firms the stack) | The dedicated **3D virtual-home capture & reconstruction** product (Zillow-3D-Home equivalent); deliberately **separate** from the mobile app. Output feeds the layered Unreal-Engine neighborhood model + the valuation engine's geometry/sightline inputs. **Long-term product, NOT a spike** (only its Phase 01 is spike-scoped, to de-risk camera/AR/reconstruction). | Its own product's releases *(scheme TBD; distinct from the EstimatePacket Version-Releases)* |

- **Triangulation Target (EstimatePacket Line):** a mature, human-reviewed fractional-diligence engine whose **evidence spine** (source → evidence → entity → observation → model/scenario → estimate → published snapshot) supports honest, suppression-aware EstimatePackets across markets — *triangulating toward* the National-AVM Line without a throwaway rewrite (hence the dealbreaker-hooks below, hooked at v1).
- **Triangulation Target (National-AVM Line):** a multi-market, regulated, national AVM platform (the enterprise FracRealHomes Codex's research over-calibrates *for*) — reached by **succession (no merge)** from the Seed-Envelope EstimatePacket Line, the same proto→Rust succession pattern as the Divia chain.
- **Triangulation Target (3D-Capture Line):** a production capture→reconstruct→deliver pipeline whose interior 3D + measurements/sightlines are a rights-clean, first-party analytical input (not just a cinematic display).

## Stages → Phases → Sprints

Currently **Phase 00 (Ideation & Research) — pending** across all three repos; **0 sprints, no application code**. The major in-flight artifact is the **`fracrealhomes-web` research corpus**: a **73-track Codex deep-research run** ("next-gen Zillow estimate," `analysis-01..73` + `synthesis.md` + 7 Phase-C packets), triaged by a Claude **SORTING-PASS** into a v1 set / 💎 keep-regardless / ⏳ defer. Per-repo Phase-00 goals: settle product direction + core data model (web), mobile parity + state-mgmt/offline stack (flutter), capture-vs-view boundary + reconstruction approach (android). The `android` repo explicitly scopes its **Phase 01 to spikes only** (camera/AR/depth/reconstruction de-risking) before any Phase-02+ product build.

## Convergence / lineage

- **Bootstrap lineage:** all three repos were **push-bootstrapped from `kingstrat-adventuregps`** (via `workflow_build_new_project.md`), inheriting the shared `_workflows/` system + specs scaffold; project `CLAUDE.md`/`README.md`/`LICENSE.md` were generated fresh. This is a **workflow-inheritance** lineage, *not* a code-fork lineage — each is a **standalone single-`main` repo** (no upstream fork, no client-mirror branch, unlike the kingstrat→proto-divia chain).
- **Build-Line relations:** **DailySpikeDriver → EstimatePacket Line** = shared-stack **clone-lineage + merge-up** (Python/Flask). **EstimatePacket Line → National-AVM Line** = **succession, no-merge** (different/enterprise stack). **3D-Capture Line** = independent native-Kotlin product feeding the others via a hand-off contract (Unreal/web), not a merge.
- **Cross-venture integration (not a lineage):** `legendarymoney-web` is consumed **over the Divia protocol / Divia.Network** for financial services — a runtime client→service dependency, not a code ancestor.
- **`_REFERENCE/_EXTERNAL/` (read-only symlinks):** `fracrealhomes-web` already symlinks `kingstrat-adventuregps`; candidate future symlinks noted in its CLAUDE.md = `legendarymoney-web` + a sibling Flask app (`diviahome-web` / `tastypantry`) for patterns.

## `[DEALBREAKER-HOOK]`s

The irreversible v1 seams the SORTING-PASS / dealbreakers analysis (`analysis-60`) imply — cheap to hook now, catastrophic to retrofit (hooked into the **EstimatePacket Line**, the near-term Build Line):

- **The thin evidence spine in SQLAlchemy** — `Source → EvidenceItem → CanonicalEntity → FeatureObservation → Model/Scenario → EstimateOutput → PublicationSnapshot`. Get the spine in at v1 even if most stages are stubs.
- **`Property` ≠ `Parcel`** — model them as distinct entities with a **many-to-many** relation (a property's value depends on *neighbor* parcels via view corridors). Collapsing them is an irreversible data-model mistake.
- **Source-neutral canonical IDs** — the primary key must be an internal canonical ID, **never a vendor ID** (vendor lock-in / rights-contamination trap; D17).
- **Suppression / `unknown` / `review_required` as first-class output states** — not an exception path. "We don't know yet" must be a normal, renderable estimate state (R2 go/no-go: *suppression must be a normal product state, not an exception*).
- **Immutable published snapshots** — buyers see **approved snapshots**, not live runs; every snapshot carries source manifest + model version + reviewer decisions + rights lane. Prevents the "sales overrides inconvenient evidence" failure (D16, R9).
- **A field-level rights ledger (principle now, full machinery later)** — rights travel with every feature (`source × field × transformation × output-lane`, with post-termination survival); a feature with unknown training rights never enters a training set, a display-only field never renders in a buyer packet (D1, R3). v1 keeps a tiny `SourceRegistry` + observed-vs-effective dates; the full ledger is deferred.
- **Counsel-approved output lanes** — separate `public_discovery` / `registered_buyer_diligence` / `internal_acquisition` / `fractional_share_pricing` / `seller_owner_packet` / `investor_material` / `credit_lender_support`; the same output may be permitted in one lane and forbidden in another (R4). **No credit/lender/appraiser lane** until regulated-AVM/appraisal obligations are intentionally designed.
- **Scenario-before-coefficient view-risk** — express view-durability as labeled **bands** (`Current Observed` / `Legal Maximum Screen` / `Likely Rebuild` / `Filed Permit` / `Human Reviewed`), never a precise dollar discount, until labels mature (D11, R6). Browser-first/static maps; **defer Unreal/Cesium** as the analytical source of truth (D12 — Unreal/photoreal tiles are display, not analysis; Google 3D-tile terms forbid analytical use).
- **Legal-classification gate before any share estimate** — a fractional 1/8 share's legal form (LLC interest / TIC / private-residence-club / securities-style) is a **front-door gate**, not a footnote; whole-home estimates may exist before legal review, **fractional share estimates may not** (D7, R7).
- **First-party data capture from day one** — log cost actuals, owner-use, support, resale/view events; nearly free now, the only proprietary label store FracRealHomes will ever own (D6, F4).

## Cross-references

- Paired business brief: [`../ULTIMATE_VISION/PRODUCTS/FracRealHomes/fracrealhomes.md`](../ULTIMATE_VISION/PRODUCTS/FracRealHomes/fracrealhomes.md).
- Organizing model + the canonical FracRealHomes worked example (the 3 Build Lines): [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md).
- Source corpus (in `fracrealhomes-web`): `_specs_and_plans/_research/next_gen_zillow_estimate/SORTING-PASS--codex-research-v1-vs-deferred.md` · `analysis-60--unknown-unknowns-and-dealbreakers.md` · `analysis-32` (the Pacaso 8× figures) · `synthesis.md`.
- Cross-venture dependency: **LegendaryMoney** (`legendarymoney-web`) over the Divia protocol *(its own engineering brief — TBD)*.
