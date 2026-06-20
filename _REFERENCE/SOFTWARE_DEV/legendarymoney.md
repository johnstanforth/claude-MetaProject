# Brief (Software-Dev) — `legendarymoney`

> **Software-dev-side brief** → the **AIXO.Dev Platform software-dev knowledgebase** (repo · upstreams · Build Lines · Build Envelopes · Triangulation Target · Stages→Phases→Sprints · lineage · license · `[DEALBREAKER-HOOK]`s · dev discussions). Paired **[business brief](../ULTIMATE_VISION/PRODUCTS/LegendaryMoney/legendarymoney.md)** (the `Company → Product` overlap anchors both). Each `##`/`###` section is bounded so it maps cleanly to a graph-DB node/edge. **Status: docs-only** (Phase 00 pending; pre-code). *Good-enough bootstrap — mined from `legendarymoney-web`'s README / CLAUDE.md / LICENSE.md; engineering content split out of the prior single-file business brief.*

## Project / repo

| Field | Value |
|---|---|
| **Repo / dir** | `legendarymoney-web` — the **web-application piece only** (mobile Android/iOS apps + companion devices intended as their own repos, **not yet created**). |
| **GitHub** | **None yet** — local repo `legendarymoney-web`, no GitHub remote (per `DOMAIN_MAPPINGS.md`). |
| **Techstack** | Python 3.12+ · `uv` (`pyproject.toml` single source of truth; `uv.lock` committed) · Flask (app factory `create_app()`, Jinja2 templates, Blueprint routing) · SQLAlchemy 2.0+ (Flask-SQLAlchemy; models in `app/models/`) · **SQLite → PostgreSQL** · Flask-Migrate/Alembic · pydantic-settings (`BaseSettings`; env prefix `LEGENDARYMONEY_`) · Bootstrap (CDN, **tentative**) · pytest · Ruff. **Type checker:** none yet (mypy only if explicitly decided). |
| **Deployment / platforms** | Self-hosted, **local-network only** (Raspberry Pi 5 / home server / any Linux or macOS box). Dev on Linux. |
| **License** | **Dual AGPLv3 + Commercial (CLA-based)** — see License section. |
| **Maps to business Product** | LegendaryMoney ([business brief](../ULTIMATE_VISION/PRODUCTS/LegendaryMoney/legendarymoney.md)). |

## Build Lines · Build Envelopes · Triangulation Target

*(Source files describe a single repo on a "v1/v2" roadmap; they do **not** name distinct Build Lines or a formal Build Envelope. The rows below map the documented surfaces onto the model — Build Envelope names not in source files are marked.)*

| Build Line | Build Envelope | Role / status |
|---|---|---|
| **`legendarymoney-web` (PFM web app)** | "Seed"-class (Python · Flask · SQLite→Postgres · small household/self-host scope) — *Envelope name not formally defined in source files.* | The shippable self-hosted PFM; delivers the Product's v1 (unify & capture) then v2 (understand & infer). Phase 00 pending, pre-code. |
| **LegendaryMoney mobile apps** *(future)* | Mobile-capture (stack TBD) — *not in source files.* | Separate **mobile-capture apps** feeding the same household server; **placeholder repos, not yet created.** |
| **Companion devices** *(future)* | TBD — *not in source files.* | Capture surfaces (incl. voice via a DiviaHome kitchen device); **own repos, not yet created.** |

- **Triangulation Target:** **Unknown (not formally stated as a "Triangulation Target" in source files).** Inferred from the roadmap: a mature, confidence-aware PFM whose unified ledger anchors a full Divia.AI agent (NL classification + ambient GPS/voice/connected-card reconciliation), publishing **LegendaryMoney-namespaced DiviaCards** to the global registry as the cross-app contract.

## Stages → Phases → Sprints

Currently **Phase 00 — Ideation & Research (PENDING / next up)**; the phase directory is **not yet created**. No application code, phases, or sprints exist. The inherited dev workflow system, specs scaffold, and `_backlog/` (empty at bootstrap) are in place. Phase 00 settles: the **confidence-aware ledger model**, the **inference/estimation engine**, the **scan-and-import architecture**, and the v1 vertical-slice scope.

## The v1/v2 build split (engineering shape)

- **v1 = scan-and-import / data unification.** Implement import adapters to gather scattered legacy fragments — hundreds-to-thousands of SMS/text logs (meals, purchases, receipt amounts, cash received, money owed), bank/card **CSV/OFX** exports, CashApp/Venmo/PayPal histories, receipt photos, notes — into **one uniform, data-cleaned, confidence-aware ledger.** Many apparently-distinct "sources" are really just import adapters for an existing export format. **Lossless** NL capture in the Activity Log + basic, transparent estimation. **Deep NL AI classification/delegation is explicitly out of scope for v1.** Motto: *"first unify, then understand."*
- **v2 = understand & infer.** The full Divia.AI agent (NL classification & parsing, advanced inference/reconciliation, ambient GPS/voice/connected-card intelligence) + **publishing LegendaryMoney-namespaced DiviaCard types** to the global DiviaCards registry (e.g. `DiviaCard::LegendaryMoney::transaction(amount, currency, vendor=ForeignKey(...))`) as the public cross-app contract. Internal schema stays private and evolvable; the DiviaCard is the public contract.

## Ledger & estimation data-model (the central engineering bet)

The primary store is LegendaryMoney's **own relational schema** (SQLAlchemy; SQLite now, Postgres later). The modeling challenge is a **ledger where amounts and balances are uncertain**: every transaction tagged **confirmed / inferred / estimated**, carrying a **confidence band + provenance trail**, plus **balance assertions** (point-in-time anchors) that reconciliation flexes the ledger around (anchor-to-anchor **balance-gap differencing** → estimated "plug" entries) — all **without ever exposing a debit/credit column.** **Open question (the prototype exists to answer it):** whether the long-term source of truth is the structured ledger, the raw captured NL corpus, or a hybrid — treat as unsettled.

## Users & Identity (engineering)

- **v1:** one self-hosted instance = **one household**, with **multiple user accounts** (family / roommates) — shared budgets, split expenses, "who owes whom," per-user capture. **Local-network only; not public-internet multi-tenancy.**
- **v2 / ecosystem:** a **global Divia.AI identity** (one global username per user) usable across servers, coordinated by a central SaaS identity service.
- **v1 accommodation:** include **placeholder fields** for the future global identity/username so later global OAuth (or equivalent) layers in **without a painful migration.**

## Cross-venture integration — FracRealHomes consumes LegendaryMoney (not a lineage)

`legendarymoney-web` is **consumed by `fracrealhomes-web` over the Divia protocol / Divia.Network** for financial services — a **runtime client→service dependency, not a code ancestor or merge.** FracRealHomes delegates real-estate **purchase flows**, **long-term operating-cost accounting**, and **tax-implication** handling to LegendaryMoney rather than reimplementing them; **LegendaryMoney is the provider, FracRealHomes the consumer.** *(FracRealHomes engineering detail → [`fracrealhomes.md`](fracrealhomes.md); this integration is also noted as a candidate `_REFERENCE/_EXTERNAL/` symlink in FracRealHomes' CLAUDE.md.)*

## Git topology / lineage

- **Lineage:** the dev workflow/scaffold was **bootstrapped from DiviaHome → Sattvasic Health → TastyPantry → `aixodev-collabs`** (per the repo README; ⚠️ the cross-repo bootstrap chain is **self-reported inconsistently** — see [`../ERRATA.md`](../ERRATA.md)). This is a **workflow-system lineage, not a shared-code dependency** — LegendaryMoney is developed independently, integrating with siblings only at the Divia.Network API layer.
- **Branches / remotes:** **Unknown (not in source files)** beyond the standard sprint-branch convention `claudecode/@claude/phase{NN}-sprint{NN}` and the `P{NN}-S{NN}-T{NN}` commit prefix; no GitHub remote yet.
- **Reference symlinks (`_REFERENCE/_EXTERNAL/`, read-only):** `diviahome-web` (bootstrap origin / sibling hub), `tastypantry`, `sattvasichealth`, `divia_ai-professional`, `divia_ai-enterprise` (commercial Divia.AI products for ecosystem/branding reference), `aixodev-collabs` (workflow origin), `aixodev-web` (Flask/SQLite→Postgres pattern reference).

## License

**Dual-licensed: AGPLv3 + Commercial (CLA-based)** — explicit and documented in `LICENSE.md` (`© 2026 LegendaryMoney LLC (Peoria, Arizona) & John Stanforth`):

- **Community release:** GNU **Affero GPL v3 (AGPLv3)** — so home/self-host users can install it.
- **Commercial:** under a **Contributor License Agreement (CLA)**, **LegendaryMoney LLC** (Arizona LLC, Peoria, AZ) — the commercial steward — retains the right to **relicense the code commercially**, specifically so functionality prototyped here can fold into proprietary, non-FOSS products.
- **Maturity:** a prototype-stage **summary of intent** — the full AGPLv3 text and the CLA are added when the project is first published publicly. One of only two repos in the portfolio with a real license statement (alongside DiviaHome).

## `[DEALBREAKER-HOOK]`s

*(The source files do **not** use the `[DEALBREAKER-HOOK]` tag. These are the irreversible-fork candidates the docs flag as get-it-right-now seams — surfaced here for modeling; confirm during Phase 00.)*

- **Confidence-aware ledger schema** — per-transaction **precision level (confirmed/inferred/estimated) + confidence band + provenance trail**, and **balance assertions as first-class anchors.** Retrofitting uncertainty onto a precise double-entry schema is the catastrophic-to-reverse fork.
- **Capture-losslessly, parse-later** — always preserve the raw natural-language input verbatim so structured interpretation can be redone/improved; losing the raw corpus is irreversible.
- **Postgres-portability constraint** — SQLite now but design numeric types, timestamps, provenance fields, and Alembic migrations to translate cleanly to Postgres; avoid SQLite-only features.
- **Global-identity placeholder fields (v1)** — reserve the future global Divia.AI username/identity fields in v1 so v2 global OAuth layers in without a painful migration.
- **DiviaCard public-contract boundary** — keep the internal finance-native schema decoupled from the LegendaryMoney-namespaced DiviaCard interchange types (own models internally; DiviaCards as the public contract), so the internal schema stays evolvable.

## Cross-references

- Paired business brief: [`../ULTIMATE_VISION/PRODUCTS/LegendaryMoney/legendarymoney.md`](../ULTIMATE_VISION/PRODUCTS/LegendaryMoney/legendarymoney.md).
- Consuming venture (financial-services client): [`fracrealhomes.md`](fracrealhomes.md).
- Conceptual model: [`../PROJECT-ORGANIZATION-MODEL.md`](../PROJECT-ORGANIZATION-MODEL.md) · discrepancies: [`../ERRATA.md`](../ERRATA.md) (E-11 capability-ahead-of-reality · E-12 LATER-002 propagation · bootstrap-chain inconsistency).
