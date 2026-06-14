# ANALYSIS — `DOMAIN_LIST.md` vs. the `ULTIMATE_VISION` Guide

> ⚠️ **SUPERSEDED (2026-06-14)** — the *interpretations* below are re-judged in [`REVISED_ANALYSIS_UltimateVision.md`](REVISED_ANALYSIS_UltimateVision.md), which reconciles most of these findings via John's time / entity-layer / lineage reframing (corporate-vs-marketing-vs-personal layers, project types, historical/successor lineage, reserved-domain ≠ operational-entity, open-question relationships). **Read that first.** This file is retained as the original *as-found* discrepancy record and for the **§F** ExoDev git-archaeology timeline.

> A reconciliation pass: every divergence, mismatch, and contradiction between the **validated**
> `DOMAIN_LIST.md` (John-reviewed; whatever data is present is verified-accurate, though some entries
> are still missing) and the **constructed** `ULTIMATE_VISION/` Guide (aggregated from a read-only
> sweep of ~24 repos). **Report only — no corrections were made to either source.**

- **Compiled:** 2026-06-13 · MetaProject session.
- **Updated:** 2026-06-13 · added **§F — forensic git timeline** of the ExoDev.AI → ExoDev.Pro pivot
  (requested for a team discussion on whether that decision was ever truly locked down).
- **Anchor of truth:** `DOMAIN_LIST.md` (and its sibling `DOMAIN_WISHLIST.md`). Where the Guide
  disagrees with the validated list, the validated list wins.
- **Direction note:** the validated list is **accurate-but-incomplete**. So:
  - Guide says X, validated says **not‑X** → **a Guide error** (high confidence). → §A, §D.
  - Validated has an entity the Guide lacks → **a Guide completeness gap** (the Guide claims to be
    "the complete picture of every product, every venture"). → §B.
  - Guide has an entity the validated list lacks → **probably just missing from the list, not a Guide
    error** — flagged for confirmation, not correction. → §C.
- **Severity:** 🔴 structural / load‑bearing (corporate hierarchy, ownership) · 🟠 should reconcile
  (naming, status, membership) · 🟡 minor (formatting, completeness of long-tail).

---

## 0. Executive summary — the five things that matter most

1. **🔴 The validated list overturns the Guide's headline corporate-structure choice (ERRATA E‑01).**
   The Guide leads with the "Phase‑D" model in which **ExoDev.Pro, Inc. is the parent and "ExoDev.AI"
   is *retired*.** The validated list keeps **`ExoDev.AI Corp.` as the live corporate parent**, with
   **both** `ExoDev.Pro, Inc.` **and** `AIXO.Dev Platforms, LLC` as its subsidiaries. E‑01 is
   effectively *decided* — against the model the Guide chose to lead with. (§A1) **§F (git forensics)
   shows this pivot was an explicit John-directed decision on 2026‑04‑19 that never left the
   `aixodev-web` research draft — and the June `DOMAIN_LIST.md` reverts to the ExoDev.AI‑parent model.**
2. **🔴 Sattvasic Health is not an "independent / informal" venture — it's a subsidiary of the
   Foundation.** Validated: **`Sattvasic Health, LLC` is a "Public Benefit Corporation" under `The
   DIVIA Innovation Foundation`** (a Divia.AI-family non-profit that already owns registered domains).
   The Guide calls SattvasicHealth an "(informal umbrella)… Undocumented," standalone. (§A4)
3. **🔴 TastyPal is a real company with a different product roster.** Validated: **`TastyPal, Inc.`**
   owns **TastyPal App + TastyPantry + TastyTrucks**. The Guide calls TastyPal an "informal umbrella"
   holding **TastyPantry + spicemaster3000** — and **never mentions TastyTrucks or TastyPal App at
   all.** (§A5, §B1)
4. **🟠 The Foundation is mis-named and mis-statused.** Guide: "**Divia.Foundation** *(planned)* 501(c)(3)."
   Validated: "**The DIVIA Innovation Foundation**," already operating (registered domains + a
   subsidiary). (§A3)
5. **🟡→🟠 The Guide's "complete picture of every venture" is a strict subset of the portfolio.**
   The validated list contains **at least 8 portfolio companies the Guide never mentions** — AdEvolve,
   CrowdMadness, CTO Mindmeld Publishing, Fractional Reality Homes, Invendra, Patternicity.AI,
   SensoryMQ, TXFR.Cloud — plus DiviaOS, LegendaryFinancial.AI, TastyTrucks, three ad-revenue
   projects, John's books, and a basket of inventory domains. (§B)

A useful framing for the whole report: **the validated `DOMAIN_LIST.md` resolves several open ERRATA
items** (E‑01 corporate naming, E‑06 Sattvasic's membership) — and in two cases it resolves them in
the *opposite* direction from the one the Guide leans toward. Those are the headline corrections.

---

## A. Direct contradictions (Guide says X; validated says not‑X) 🔴/🟠

### A1. 🔴 Corporate parent of the ExoDev / AIXO.Dev family — the big one

| | The Guide | Validated `DOMAIN_LIST.md` (§ "ExoDev.AI Family of Companies", lines 92–123) |
|---|---|---|
| Top entity | **`ExoDev.Pro, Inc.`** (Dallas HQ) — and "**explicitly retires the older 'ExoDev.AI' branding**" | **`ExoDev.AI Corp.`** (domain `exodev.ai`) — alive and at the top |
| `AIXO.Dev Platforms, LLC` | a **subsidiary of `ExoDev.Pro, Inc.`** | a **subsidiary of `ExoDev.AI Corp.`** — a **sibling** of `ExoDev.Pro, Inc.`, not nested under it |
| `ExoDev.Pro, Inc.` | the parent | a **subsidiary of `ExoDev.AI Corp.`** |

- **Where:** `VENTURES/ExoDev.md` §1, `VENTURES/README.md` §1 (table), and `ERRATA.md` **E‑01** — all
  lead with the Phase‑D model and tag "ExoDev.AI" as the *oldest, retired* name.
- **Why it matters:** This is the single most load-bearing discrepancy. The validated list **keeps
  `ExoDev.AI Corp.` as the corporate parent** — so "ExoDev.AI" is *not* retired; it is the live top of
  the tree, with `ExoDev.Pro, Inc.` and `AIXO.Dev Platforms, LLC` underneath it as two subsidiaries.
- **Note:** the validated form `ExoDev.AI Corp.` matches the **`PRODUCT_AND_NAMING.md`** variant in
  E‑01 ("ExoDev.AI Corporation" + "AIXO.Dev Platforms LLC, *An ExoDev.AI Company*"), **not** the
  Phase‑D research the Guide elevated. The Guide's own product-doc copyright lines ("…*An ExoDev.AI
  Company*", see §D2) silently corroborate the validated model even while the Guide's prose calls it
  obsolete. **E‑01 is effectively answered by the validated list.**

### A2. 🟠 ExoDev.Pro – Chicago: "future" in the Guide, **existing** in the validated list

- **Guide** (`VENTURES/ExoDev.md` line 17): regional LLCs are Dallas + LA today, with "**(future: NYC,
  Chicago, Ireland)**."
- **Validated** (lines 101–106): three established regional subsidiaries — **`ExoDev.Pro - Dallas, LLC`**,
  **`ExoDev.Pro - Los Angeles, LLC`**, **and `ExoDev.Pro - Chicago, LLC`** — each with a live
  client-portal subdomain (`dallas.` / `losangeles.` / `chicago.exodev.pro`).
- **So:** Chicago has graduated from "future" to a standing regional subsidiary. (NYC and Ireland are
  Guide-only and unconfirmed by the list — see §C.)

### A3. 🟠 The Foundation: wrong name, wrong status

- **Guide:** "**Divia.Foundation**" — a "**(planned)**" 501(c)(3) nonprofit arm
  (`VENTURES/README.md`, `VENTURES/DiviaAI.md` §4 + product table, `README.md`,
  `PRODUCTS/DiviaHome/diviahome.md`, `USER_STORIES/federated-home-and-work.md`).
- **Validated** (lines 78–82): "**The DIVIA Innovation Foundation**," an existing **Non‑profit
  Organization** that already holds registered domains (`diviafoundation.org` + `.com/.net/.shop`
  aliases).
- **So:** (a) the canonical name is **"The DIVIA Innovation Foundation,"** not "Divia.Foundation"
  (the latter is also flagged as brand-drift in E‑07); (b) it is **not merely "planned"** — it is
  established and, per A4, already has an operating subsidiary.

### A4. 🔴 Sattvasic Health's ownership — Foundation subsidiary, not "independent / standalone"

- **Guide:** SattvasicHealth = "**(informal umbrella)**… **Undocumented**" license, grouped under
  "**Independent / emerging**" ventures (`README.md`, `VENTURES/README.md` §1 table). ERRATA **E‑06**
  debates whether it's even in the Divia.Network ecosystem.
- **Validated** (lines 83–90): **`Sattvasic Health, LLC`** is a **"Project / Subsidiary / Public
  Benefit Corporation"** sitting **directly under `The DIVIA Innovation Foundation`** — i.e. inside
  the Divia.AI family, with a clear corporate parent and a `BUY-DOMAIN: sattvasic.ai`.
- **So:** the validated list **decides E‑06's ownership question**: Sattvasic is *not* an orphan
  independent — it is a public-benefit subsidiary of the Divia non-profit. The Guide's "informal /
  undocumented / standalone" framing is wrong on placement. (Its PBC status also implies a
  mission/license posture different from "just another AGPL sibling," which the Guide's ideation
  speculates about.)

### A5. 🔴/🟠 TastyPal — a company, with a different roster

- **Guide:** "**TastyPal (informal umbrella)**" holding **TastyPantry + spicemaster3000**
  (`VENTURES/TastyPal.md`, `VENTURES/README.md` §1, `README.md`).
- **Validated** (lines 240–258): "**Company: `TastyPal, Inc.`**" (`tastypal.com`) holding **three**
  things — **`TastyPal App`** (`tastypal.app`), **`TastyPantry by TastyPal`** (`tastypantry.app`), and
  **`TastyTrucks by TastyPal`** (`tastytrucks.app`).
- **So:** 🟠 "informal umbrella" → actually an incorporated **`TastyPal, Inc.`**; 🔴 the membership
  diverges: the Guide is **missing TastyPal App and the entire TastyTrucks subsidiary** (§B1) and
  instead attaches **spicemaster3000**, which the validated list does not list under TastyPal (or
  anywhere) — and which the Guide itself describes as having "**no… TastyPal ties**" (§C1). The
  Guide's TastyPal venture doc is built around the wrong two products.
- **Related:** the Guide insists "TastyPantry = **Divia.AI ecosystem plumbing, not an independent
  business**" (`PRODUCTS/TastyPal/tastypantry.md`, E‑06). The validated corporate home for TastyPantry
  is **`TastyPal, Inc.`** — which actually supports TastyPantry's own repo self-description (the
  "standalone" side of E‑06) over the Guide's "Divia plumbing" reading.

### A6. 🟠 "Divia.Network" means two different things

- **Guide:** Divia.Network = the "**open, HTTP‑like ecosystem integration layer / API standard**" —
  the protocol that carries the cross-app fan-out (`VENTURES/DiviaAI.md` product table;
  `USER_STORIES/divia-network-fanout.md`; used this way throughout).
- **Validated** (lines 41–51): Divia.Network's **only** description is a **"online tutorials and
  training site for the ecosystem of connected apps"** (`divia.network`, with training microsite
  redirects like `divia.money → divia.network/managingmymoney/`).
- **So:** the term is **overloaded** (much like "DiviaCard," cf. E‑05): the validated reference treats
  `divia.network` as an education/tutorials property, while the Guide treats "Divia.Network"
  exclusively as an integration protocol and **never mentions the tutorials/training role.** Needs a
  reconciling decision — are these one brand spanning both, or two things that need distinct names?

### A7. 🟠 KingStratVC product name

- **Guide:** product = "**KingStratVC Knowledgebase**" (per LATER‑002), in-repo styled "KingStrat.vc"
  (`PRODUCTS/KingmakerStrategic/kingstratvc-knowledgebase.md`, `VENTURES/KingmakerStrategic.md`).
- **Validated** (lines 184–188): firm "**Kingmaker Strategic**" (`kingmakerstrategic.com`); product
  "**Kingmaker Strategic Knowledgebase**" (`kingstratvc.com`).
- **So:** the validated **product name uses the full words — "Kingmaker Strategic Knowledgebase"** —
  not the abbreviation "KingStratVC Knowledgebase." (Feeds the broader KingStratVC naming snarl in
  E‑07. The repo short-name `kingstratvc-web` and domain `kingstratvc.com` are consistent.)

### A8. 🟠 Kingmaker Strategic — portfolio company vs. "external customer"

- **Guide:** Kingmaker Strategic is "**a customer rather than a vendor**… the first **real-world
  client install**" (`VENTURES/KingmakerStrategic.md`, `VENTURES/README.md`).
- **Validated:** Kingmaker Strategic is listed under **"Venture Studio Portfolio Companies"** — the
  same bucket as John's other owned ventures (LegendaryMoney, TastyPal, Patternicity, etc.).
- **So:** the validated list frames Kingmaker as **one of John's own portfolio companies**, which fits
  a *controlled dogfooding* entity better than the Guide's "external real-world client" language. Worth
  confirming the intended relationship (owned portfolio co. used as a reference install vs. arm's-length
  customer) — the two framings imply different things for the "first paying Enterprise customer" story.

---

## B. Validated entities & products **absent** from the Guide (completeness gaps)

The Guide's README claims to capture "**the complete picture of every product, every venture.**" The
validated list shows the following are missing from it. (Most are business/domain entities that likely
had **no harvested code repo**, so the omission is a *scope* artifact of the repo-only sweep — but per
the Guide's own completeness claim, they belong on the radar.)

### B1. 🔴 Within families the Guide *does* cover

- **`TastyTrucks by TastyPal`** — a whole subsidiary (`tastytrucks.app`; `BUY tastytruck.com`,
  `tastytrucks.com`; cf. the recent "Add TastyTruck domain recommendation" commit and the
  `DOMAIN_WISHLIST.md` priority rows). **Entirely absent from the Guide.**
- **`TastyPal App`** (`tastypal.app`) — the flagship app of `TastyPal, Inc.`, distinct from
  TastyPantry. **Absent.**
- **`LegendaryFinancial.AI`** — a **subsidiary of `LegendaryMoney LLC`** (`legendary.financial`; `BUY
  legendaryfinancial.ai`, a `DOMAIN_WISHLIST.md` priority). **Absent** (the Guide mentions only vague
  "separate mobile-capture apps").
- **`DiviaOS`** (`diviaos.com`) — an open-source software project under `DiviaHome LLC`. **Absent.**
- **`DiviaHome LLC` / `Divia.Life LLC`** — the validated list elevates these to **named subsidiary
  legal entities** of `Divia.AI, Inc.`; the Guide treats both only as products/repos, never as LLCs.
- **`DiviaHome Community Edition`** — the validated canonical name for the open edition
  (`diviahome.com/communityedition/`, with `divia.ai/diviahome/` and `divia.ai/diviahomeserver/`
  redirecting to it). The Guide just calls it "DiviaHome." Also: validated frames `DiviaHome LLC` as a
  company "**manufacturing and selling smart-home devices and software**," a stronger claim than the
  Guide's "open-source household hub (with planned devices)."
- **The DiviaCards open standard** — validated names it "**Divia.AI Semantic Smart Cards (aka
  DiviaCards)**," a *Project / Open Standard* under `Divia.AI, Inc.` with its **own domain
  `divia.cards`** (+ `diviacards.com`, `diviasmartcards.com`). The Guide has the *concept* and the
  `divia_cards` *app* but never the standard's canonical name or domain — info that could help settle
  E‑05 (the "data concept" = the `divia.cards` open standard, distinct from the `divia_cards` renderer).

### B2. 🟠 Whole portfolio companies the Guide never mentions

Validated "Venture Studio Portfolio Companies" with **zero** Guide footprint (confirmed by grep):

- **`AdEvolve, Inc.`** (`adevolve.com`)
- **`CrowdMadness, Inc.`** — `CrowdMadness` prediction-market/betting (`crowdmadness.app`) **+
  `CrowdResearch`** market-research portal (`crowdresearch.com`)
- **`CTO Mindmeld Publishing, LLC`** (`ctomindmeld.com`)
- **`Fractional Reality Homes, LLC`** (styled `frac|real|homes`; `fracreal.homes` + a large alias set)
- **`Invendra, Inc.`** (`invendra.com`; `BUY invendra.ai`)
- **`Patternicity.AI, LLC`** (`patternicity.ai`) — a substantial venture in its own right:
  `Patternicity News` (`patternicity.news`), `PatternicitySocial` (`patternicity.social`),
  `Patternicity URL Shortener` (`ptnws.link`), `Patternicity Bet`, `Patternicity ONE`,
  `PatternicityNews Professional`. **None of this is in the Guide.**
- **`SensoryMQ, Inc.`** (`sensorymq.com`) **+ `SensoryMQ.Cloud, LLC`** (`sensorymq.cloud`; `BUY
  sensorymq.ai`)
- **`TXFR.Cloud, Inc.`** (`txfr.cloud`) **+ `TXFR.App`** (`txfr.app`) — high-speed file-transfer
  (Aspera-class) service

### B3. 🟡 Long-tail also absent

- **Ad-revenue / YouTube projects:** `JSL Dragonfly` (`jsldragonfly.com`), `Dotfigurator.sh`
  (+ `Dotfigurate.me` social), `VelocityTerminal.sh`.
- **Remaining domain inventory:** `gridtransmit.com`, `mobthought.com`, `neurogrammatic.com`,
  `quintivity.com`, `rosettamq.com`, `scalara.com`, `surreality.com`, `transformulator.dev`.
  *(Note `rosettamq.com` and `scalara.com` correspond to "RosettaMQ" and the "Scalara Framework"
  the Guide mentions only as code/extraction concepts in `aixodev-codemap` / `divia_ai-enterprise` —
  so the names appear, but the validated list reveals they are also held domains.)*
- **John Stanforth's books + personal brand:** *The DIVIA Mentality*, *The Neurodivergent DIVIA
  Mentality*, *The Success Playbook*, *Billion-Dollar Platforms*, and the author brand
  (`johnstanforth.com`, `stanforth.org`, `BUY stanforth.ai`). Out of the Guide's repo scope, but part
  of the validated portfolio.
- **`Divia.Link`** — an **aborted** project (domains scheduled for deletion Sept 2026). The Guide's
  "complete picture" doesn't record that it existed and was killed.

---

## C. In the Guide but **not** in the validated list (confirm — likely just missing data, not errors)

Because the validated list is **accurate‑but‑incomplete**, these are flagged for confirmation, **not**
as Guide errors. Most are real code repos or planned components that simply have **no dedicated domain
entry yet**.

1. **`spicemaster3000`** — the Guide gives it a full product + venture treatment under TastyPal; the
   validated list doesn't mention it anywhere. Given the list *does* carry TastyTrucks as TastyPal's
   second subsidiary (§B1), confirm whether spicemaster3000 belongs under `TastyPal, Inc.`, is a
   future standalone venture (its own brand/LLC, as the Guide argues), or simply hasn't been added.
2. **`Divia.AI Swarm`, `Divia.AI Global (SaaS)`, `DiviaMesh`** — ecosystem components/planned services
   in the Guide; no domains in the validated list (expected if domain-less today). Confirm whether any
   needs a domain/entity entry (e.g. a future `Divia.AI Global` identity service likely lives under
   `divia.ai`).
3. **The AIXO.Dev Flask prototypes** — `aixodev-projects`, `aixodev-codemap`, `aixodev-collabs`,
   `aixodev-workgroups`, `aixodev-openhands` — are code repos slated to merge into `aixodev-web`; none
   have (or likely need) their own domains, so their absence from the list is expected.
4. **`AIXO.Dev Professional`** desktop edition — in the validated list this is a product line under
   `AIXO.Dev Platforms, LLC` with only `BUY-DOMAIN: aixodev.pro / aixo.pro` (no live domain), matching
   its ⚪ placeholder status; consistent, just noting the desktop name/stack itself is still contested
   (E‑02), which the domain list doesn't resolve.

---

## D. Naming, spelling & formatting nuances 🟡/🟠

1. **🟠 "AIXO.Dev Platform**s** LLC" (plural) vs "AIXO.Dev Platform LLC" (singular).** Validated uses
   the **plural** ("`AIXO.Dev Platforms, LLC`", line 107; domain `aixo.devplatforms.llc`). The Guide's
   `VENTURES/ExoDev.md` correctly notes the plural, but several **product-doc copyright quotes** render
   it **singular** — "© **AIXO.Dev Platform LLC**, An ExoDev.AI Company" (`aixodev-web.md` line 9,
   `aixodev-professional.md` line 8, `aixodev-codemap.md` line 7). Those are faithful quotes of repo
   text, but they diverge from the validated canonical (plural). Cf. E‑01 / E‑14.
2. **🟡 Regional-LLC styling.** Validated: "`ExoDev.Pro - Dallas, LLC`" (dotted, hyphen, comma). Guide:
   "ExoDev.Pro Dallas LLC." Same entity, different punctuation — resolves the "dotted vs dotless /
   Inc. vs LLC" sub-question of E‑01 in favor of **dotted `ExoDev.Pro` + `LLC`**.
3. **🟡 DiviaContacts mobile naming.** Validated: "`DiviaContacts for iPhone/iPad`" (repo
   `…-iOS`). Guide: "DiviaContacts for… iOS." Cosmetic.
4. **🟡 KingStratVC styling.** Guide notes in-repo styling "**KingStrat.vc**" (implying a `.vc`
   domain); the validated domain is **`kingstratvc.com`**. Cf. A7 / E‑07.
5. **🟡 "Divia.Foundation" vs "The DIVIA Innovation Foundation"** — see A3 (also an E‑07 brand-drift
   item).

---

## E. How this interacts with the existing `ERRATA.md`

The validated `DOMAIN_LIST.md` is, in effect, **new evidence that closes or redirects several open
ERRATA items** — in two cases *against* the direction the Guide leaned:

| ERRATA item | Guide's lean | What the validated list says | Net |
|---|---|---|---|
| **E‑01** corporate parent (🔴) | Phase‑D: `ExoDev.Pro, Inc.` is parent; "ExoDev.AI" retired | `ExoDev.AI Corp.` **is** the parent; `ExoDev.Pro, Inc.` + `AIXO.Dev Platforms, LLC` are its subsidiaries | **Decided — opposite of the Guide's lead** (A1) |
| **E‑06** Sattvasic / TastyPantry membership (🔴) | "standalone vs ecosystem — undecided" | Sattvasic = PBC subsidiary of **The DIVIA Innovation Foundation**; TastyPantry = subsidiary of **`TastyPal, Inc.`** | **Ownership decided**; both have real corporate homes (A4, A5) |
| **E‑05** "DiviaCard" overload (🔴) | two unreconciled meanings | validated names the standard "**Divia.AI Semantic Smart Cards**" (`divia.cards`) | Adds a canonical name/domain for the data-concept side (B1) |
| **E‑07** brand-spelling drift (🟠) | many variants | confirms "The DIVIA Innovation Foundation," `kingstratvc.com`, dotted `ExoDev.Pro`, plural `Platforms` | Several spellings **pinned** (A3, A7, D) |

**Suggested next step (when you're ready to make edits):** treat the validated `DOMAIN_LIST.md` as the
tie-breaker for E‑01 and E‑06, update `VENTURES/ExoDev.md` §1 + `VENTURES/README.md` §1 to restore
`ExoDev.AI Corp.` as the parent, re-home Sattvasic under the Foundation and TastyPantry/TastyTrucks
under `TastyPal, Inc.`, rename "Divia.Foundation" → "The DIVIA Innovation Foundation," and either fold
the missing portfolio companies (§B) into the Guide or explicitly scope the Guide as
"repos-with-code only." **Per your instruction, none of that was done here — this is report-only.**

---

## F. Forensic timeline — the ExoDev.AI → ExoDev.Pro pivot (git archaeology)

> Added 2026-06-13 at John's request, to set context for a team discussion on *whether the Phase‑D
> "retire ExoDev.AI" decision was ever actually locked down.* All timestamps are **git author dates**
> (Pacific, `-0700`) from the symlinked source repos. **Short answer: it was a real, explicit,
> John-directed decision — but it was made inside a DRAFT research project, never propagated to the
> operating docs, and the most recent validated artifact (June's `DOMAIN_LIST.md`) has since reverted
> to the ExoDev.AI‑parent model.** That is exactly why the discrepancy in §A1 exists.

### F.1 The one-paragraph story

The **ExoDev.AI corporate parent** model was established in **early–mid March 2026** and baked into
`aixodev-aixocode`'s `PRODUCT_AND_NAMING.md` (a **three‑tier / three‑brand** structure:
`ExoDev.AI Corporation` parent → `AIXO.Dev Platforms LLC` product co. + `ExoDev.Pro` consultancies).
Five weeks later, the **"Phase D" Product‑Development research** ran inside `aixodev-web`
(2026‑04‑17 → 04‑25). Its 11 client‑facing artifacts were first drafted **still using ExoDev.AI**,
passed a **"User Review hard gate"** on **04‑18**, and on **2026‑04‑19 at 09:41** John committed the
pivot: **retire the separate ExoDev.AI Corp brand and collapse the three brand tiers into a *two‑tier*
model** — `ExoDev.Pro, Inc.` as the customer‑facing parent + `AIXO.Dev Platform` as its product
subsidiary, the old "civilizational parent" voice becoming one of **three voice registers inside the
single ExoDev.Pro, Inc. entity.** The change touched **only** the `aixodev-web` research artifacts. It
was **never** carried back to `aixodev-aixocode`'s naming docs (frozen 04‑02 / 04‑11), to John's global
`CLAUDE.md`, or anywhere else — and June's validated `DOMAIN_LIST.md` is back on `ExoDev.AI Corp.` as
parent.

### F.2 Chronology

| When (author date, `-0700`) | Repo | Commit | Event |
|---|---|---|---|
| 2026‑02‑28 | `aixodev-web` | `d014d54` | Repo's first commit ("Initial spec documents before starting work"); pre‑ExoDev naming. |
| **2026‑03‑07 02:58** | `aixodev-web` | `0864f22` | **First appearance of "ExoDev.AI"** — "Standardize product naming and rebrand to AIXO.Dev Platform (Web)." *The ExoDev.AI era begins.* |
| 2026‑03‑09 16:24 | `aixodev-web` | `d538c28` | First "ExoDev.Pro" — as the **consulting subsidiary**, coexisting under the ExoDev.AI parent. |
| 2026‑03‑18 22:25 | `aixodev-aixocode` | `48bab26` | aixocode's first commit; already carries both ExoDev.AI (parent) + ExoDev.Pro (consultancy). |
| **2026‑03‑19 05:05** | `aixodev-aixocode` | `357d90b` | **"Update PRODUCT_AND_NAMING.md with corrected corporate structure"** — pins the **three‑tier ExoDev.AI Corporation model the June `DOMAIN_LIST.md` still matches.** |
| 2026‑04‑02 16:06 | `aixodev-aixocode` | `fb7e304` | **Last edit to `PRODUCT_AND_NAMING.md`** (ELEMENTS‑ENTITIES reframing). *Frozen here — never updated for the pivot.* |
| 2026‑04‑11 03:24 | `aixodev-aixocode` | `7a5c4cd` | **Last edit to aixocode `CLAUDE.md`** — still "ExoDev.AI, Inc." |
| 2026‑04‑17 → 04‑18 | `aixodev-web` | (Tracks 21–24) | **Phase D research sprint** (Palantir/FDSE/ontology). 11‑artifact "Product Development" suite committed **04‑18** (`e2cc8ac`), **still using "ExoDev.AI Corp."** |
| 2026‑04‑18 09:29 | `aixodev-web` | `3a39516` | **"Phase D COMPLETE; Phase D → User Review hard gate live."** John reviews. |
| **2026‑04‑19 09:41:32** | `aixodev-web` | **`838d3be`** (author: **John Stanforth**) | **THE PIVOT** — *"Phase D artifacts — Phase 1a revisions: **retire ExoDev.AI brand, two‑tier entity model**, Los Angeles spelling, ClientDomainGraph rename, FDSERole entity removed."* Rewrote 11 artifacts; also standardized **"Platform**s**" (plural)** and moved founder URLs `exodev.ai/*` → `exodev.pro/*`. |
| 2026‑04‑19 (later) | `aixodev-web` | `14aea25` | Phase 1b follow‑up (DomainGraph triumvirate, Organization entity). |
| 2026‑04‑24 21:53 | `aixodev-web` | `6ed9d17` | `synthesis.md` **top summary** updated to "*Corporate structure (post‑2026‑04‑19): parent `ExoDev.Pro, Inc.`… replacing retired ExoDev.AI Corporation brand*" — **but its body §5.5/§8 still describe the old three‑brand ExoDev.AI‑parent model** (the doc is internally self‑contradictory; see F.4). |
| 2026‑04‑24 → 04‑25 | `aixodev-web` | `b14d917` | Phase 3 "cross‑artifact consistency pass: align… corporate vocabulary across 6 artifacts." |
| 2026‑04‑25 | `aixodev-web` | `66bd11b` | Research project's **last commit.** The pivot has now touched **only** this repo's research artifacts. |
| **2026‑06‑13** | `_REFERENCE` | (`DOMAIN_LIST.md`) | The **validated** list uses **`ExoDev.AI Corp.`** as parent again (three‑tier). *The most recent John‑reviewed artifact is on the pre‑pivot model.* |

### F.3 The exact decision wording (commit `838d3be`, file `07-positioning-and-messaging.md`)

The pivot's rationale is stated verbatim in the diff — note it cites **John's own direction that day**:

> *"**Per user direction 2026‑04‑19** and synthesis §5.5. The prior **three‑brand framing (separate
> ExoDev.AI Corp civilizational parent) is retired.** The architecture is now **two‑tier** —
> `ExoDev.Pro, Inc.` as the **customer‑facing parent** plus `AIXO.Dev Platform` as its flagship
> **product subsidiary** — with **four voice registers** layered across it."*

And the same commit reassigned the parent's identity inside `ExoDev.Pro, Inc.`:

> *(before)* `### §4.1 ExoDev.AI Corporation — Civilizational register` / "Parent holding company voice."
> *(after)*  `### §4.1 Founder / CEO civilizational layer (within ExoDev.Pro, Inc.)` / "Founder‑driven
> public voice **on behalf of the ExoDev.Pro, Inc. parent**."

So this was **not AI drift** — it was a deliberate, dated, John‑authored decision. The open question is
purely about its **scope and finality** (F.5).

### F.4 Why the discrepancy survived: the pivot never propagated, and even its own source stayed split

1. **Confined to a DRAFT research project.** Every changed file lives under
   `aixodev-web/_specs_and_plans/_research/product_development_strategy/PRODUCT_DEVELOPMENT/` — the
   suite the Guide itself flags as "marked DRAFT/aspirational… pre‑seed/pre‑office/pre‑customer"
   (`VENTURES/ExoDev.md`). It was never promoted to canon.
2. **The operating docs were already frozen before it happened.** aixocode's `PRODUCT_AND_NAMING.md`
   (the actual naming authority) was last edited **2026‑04‑02**, and its `CLAUDE.md` **2026‑04‑11** —
   both **before** the 04‑19 pivot. Neither was reopened. (At HEAD, `ExoDev.AI` still appears in
   aixocode's `CLAUDE.md`, `README.md`, `PRODUCT_AND_NAMING.md`, users‑guide, workflow, and product‑spec.)
3. **Even the synthesis that drove it was only half‑updated.** `synthesis.md`'s headline table row was
   updated to the post‑pivot model on 04‑24, but its body (§5.5 "*three related brands with a shared
   ExoDev.AI Corp parent*", §8 governance) still carries the **old** model — so the single most
   authoritative Phase‑D document **contradicts itself** on this exact point.
4. **June reverts.** The validated `DOMAIN_LIST.md` (2026‑06‑13) re‑affirms `ExoDev.AI Corp.` as the
   parent — so the newest John‑reviewed artifact is back on the model the pivot tried to retire.

### F.5 What this means for the team discussion (open questions, not conclusions)

- **Was it ever ratified beyond the research draft?** Git says **no** — the decision is real and dated,
  but it lived and died inside one DRAFT artifact suite. Nothing in any *operating* doc adopted it,
  and the June reference reverts. So "did we lock it down?" → **not in any binding/propagated sense.**
- **Three lenses were entangled in one decision.** The 04‑19 change simultaneously touched (a) **legal
  corporate structure**, (b) **brand/voice architecture** (its primary driver — "three brand tiers →
  one legal entity with three voice registers"), and (c) **platform data‑tenancy** (Organizations/
  Depts in the DB schema). The "retire ExoDev.AI" wording was chiefly a **brand‑architecture
  simplification**; whether John meant it as a *binding legal restructuring* (dissolving `ExoDev.AI
  Corp.` as the holding entity) is unstated — and the persistence of `exodev.ai` (registered) +
  `exodev.com` (buy‑list) + the June list all point to `ExoDev.AI Corp.` continuing as the legal parent.
- **The Chicago thread is downstream of this.** In the Phase‑D entity model, **Dallas/LA were the only
  offices**, with **NYC/Toronto/Chicago as "Q4 2027+ candidates,"** modeled as **Depts under one
  ExoDev.Pro Organization, not separate tenants.** The validated `DOMAIN_LIST.md` now lists
  **Dallas / LA / Chicago as three standing regional subsidiary LLCs** each with a live portal
  subdomain — i.e. reality moved past the Phase‑D "future candidate" framing (cf. §A2).
- **Net recommendation for the discussion:** treat the 04‑19 pivot as a **proposal that was drafted and
  endorsed in research but never operationalized**, and treat the June `DOMAIN_LIST.md` as the current
  *de facto* canon (ExoDev.AI Corp. parent). The decision to make is whether to (i) **re‑adopt** the
  Phase‑D two‑tier ExoDev.Pro‑parent model and finally propagate it everywhere, or (ii) **formally
  retire the pivot** and keep ExoDev.AI Corp. as the holding parent. Either way the goal is one model,
  propagated to `PRODUCT_AND_NAMING.md` + both `CLAUDE.md`s + this `_REFERENCE/` at once. *(Per your
  instruction, no such change was made here.)*

---

## Appendix — quick cross-reference

| # | Sev | Topic | Guide | Validated `DOMAIN_LIST.md` |
|---|---|---|---|---|
| A1 | 🔴 | ExoDev parent | `ExoDev.Pro, Inc.`; "ExoDev.AI" retired | `ExoDev.AI Corp.` is parent (ExoDev.Pro + AIXO.Dev Platforms are subsidiaries) |
| A2 | 🟠 | Chicago consultancy | "future" | existing `ExoDev.Pro - Chicago, LLC` (`chicago.exodev.pro`) |
| A3 | 🟠 | Foundation name/status | "Divia.Foundation (planned)" | "The DIVIA Innovation Foundation" (operating) |
| A4 | 🔴 | Sattvasic ownership | informal/independent/undocumented | PBC subsidiary of The DIVIA Innovation Foundation |
| A5 | 🔴 | TastyPal | informal umbrella: Pantry + spicemaster3000 | `TastyPal, Inc.`: App + Pantry + Trucks |
| A6 | 🟠 | Divia.Network | integration protocol/standard | tutorials & training site |
| A7 | 🟠 | KingStratVC product name | "KingStratVC Knowledgebase" | "Kingmaker Strategic Knowledgebase" |
| A8 | 🟠 | Kingmaker relationship | external customer / client install | own venture-studio portfolio company |
| B1 | 🔴 | Missing in covered families | — | TastyTrucks, TastyPal App, LegendaryFinancial.AI, DiviaOS, DiviaHome/Divia.Life LLCs, DiviaCards standard (`divia.cards`) |
| B2 | 🟠 | Missing whole companies | — | AdEvolve, CrowdMadness(+CrowdResearch), CTO Mindmeld, Fractional Reality Homes, Invendra, Patternicity.AI(+line), SensoryMQ(+Cloud), TXFR.Cloud(+App) |
| B3 | 🟡 | Missing long-tail | — | JSL Dragonfly, Dotfigurator, VelocityTerminal, 8 inventory domains, books, personal brand, Divia.Link (aborted) |
| C1 | ⚪ | spicemaster3000 | full TastyPal product | not listed (confirm placement) |
| D1 | 🟠 | Platform**s** LLC | singular in some copyright quotes | plural "AIXO.Dev Platforms, LLC" |

*End of analysis. No source files were modified.*
