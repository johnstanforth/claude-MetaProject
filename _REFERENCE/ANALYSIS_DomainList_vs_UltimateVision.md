# ANALYSIS — `DOMAIN_LIST.md` vs. the `ULTIMATE_VISION` Guide

> A reconciliation pass: every divergence, mismatch, and contradiction between the **validated**
> `DOMAIN_LIST.md` (John-reviewed; whatever data is present is verified-accurate, though some entries
> are still missing) and the **constructed** `ULTIMATE_VISION/` Guide (aggregated from a read-only
> sweep of ~24 repos). **Report only — no corrections were made to either source.**

- **Compiled:** 2026-06-13 · MetaProject session.
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
   effectively *decided* — against the model the Guide chose to lead with. (§A1)
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
