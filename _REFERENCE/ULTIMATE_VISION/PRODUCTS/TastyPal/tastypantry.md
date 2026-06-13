# Product — TastyPantry

> A kitchen **pantry-inventory** app and the **seed prototype** the Divia.Network household apps
> descended from. The canonical "food eaten" node of the ecosystem fan-out.

- **Names:** "TastyPantry by TastyPal" · repo/dir `tastypantry` · umbrella TastyPal — see [`../../VENTURES/TastyPal.md`](../../VENTURES/TastyPal.md).
- **License:** **Undocumented.** **Status:** 🟠 Phase 00 pending, zero code, scaffold only.

---

## What it is (consensus)
A standalone Python/Flask web app for **kitchen pantry-inventory tracking**, organized around five interconnected domains:
1. **Foods / Ingredients** — a catalog matching both packaged products and unpackaged produce/bulk; each food carries an **on-hand inventory quantity**.
2. **Food Logs** — **natural-language consumption entries** ("I ate two quesadillas just now") that **decrement** inventory.
3. **Grocery Receipts** — purchases reconciled against the catalog that **increase** inventory.
4. **Shopping Lists** — **per-store** lists driven by on-hand dropping toward zero; feed back into Receipts after the trip.
5. **Recipes** — **"compound foods"** (quesadilla = tortillas + cheese); logging "2 quesadillas" **cascades decrements** to base ingredients.

### Cross-product role
The "food eaten" slice of the Divia.Network fan-out (food → TastyPantry; macros → Sattvasic; expense → LegendaryMoney — see [`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md)) and the bootstrap seed for the household-app chain.

> ⚠️ ERRATA E-06: TastyPantry's own `CLAUDE.md` calls it *"standalone … not part of any larger platform,"* contradicting that role — yet it carries `_REFERENCE/_EXTERNAL/` symlinks to `sattvasichealth`, `legendarymoney-web`, and `diviahome-web`. The cross-app feed to Sattvasic and the "seed/ancestor" lineage are baseline claims *not stated in-repo*. See [`../../ERRATA.md`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** the five-domain data model is the Phase-00 work; how NL food logs map to structured entries + decrement inventory; the recipe→base-ingredient cascade; receipt ingestion/reconciliation; keep the schema Postgres-portable.
- ✦ **New:** **inventory-depletion → auto shopping list is exactly the nightly-replenishment loop** (LATER-002 / [`../../USER_STORIES/diviahome-nightly-replenishment.md`](../../USER_STORIES/diviahome-nightly-replenishment.md)) — TastyPantry holds the consumption data that powers DiviaHome's time-decaying grocery items and escalating errand priority. ✦ **Wire TastyPantry's inventory to spicemaster3000's "Virtual Spice Cabinet"** — spices are a TastyPantry food category; the two re-invent the same model independently (see [`spicemaster3000.md`](spicemaster3000.md) and [`../../ERRATA.md`](../../ERRATA.md)). ✦ Resolve the standalone-vs-ecosystem framing: the evidence (symlinks, the fan-out role) says it's *in* the ecosystem; its docs lag.
