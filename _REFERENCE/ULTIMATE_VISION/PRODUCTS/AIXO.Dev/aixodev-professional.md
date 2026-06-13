# Product — AIXO.Dev Professional

> The *planned* cross-platform **Rust/Tauri desktop edition** of the AIXO.Dev Platform — offline-first,
> with full sync on reconnect. A long-horizon placeholder, deliberately gated, and the subject of a
> live cross-repo naming/stack contradiction.

- **Names:** "AIXO.Dev Professional" · repo/dir `aixodev-professional`.
- **Umbrella:** AIXO.Dev · **License:** **Proprietary** ("© AIXO.Dev Platform LLC, an ExoDev.AI Company. All Rights Reserved." — the only explicit copyright among the AIXO prototypes).
- **Status:** ⚪ Forward-looking placeholder — README only, **no code** (empty CLAUDE/specs/research; a staged "Twilight" Bootstrap theme of undecided relevance).

## What it is (consensus, per *this repo's* README)
The planned **Rust/Tauri v2 + SvelteKit** desktop edition of the platform and an explicit **sub-project of `aixodev-web`**: offline-capable via embedded Rust server logic (the "coding on a train" use-case — no Internet/SaaS needed), with full bidirectional sync to the AIXO.Dev servers on reconnect. Its desktop stack is meant to **converge with Divia.AI Professional's** Rust/Tauri foundation so lessons flow both ways (separate corporate families; shared shell/runtime/storage/sync; distinct app/domain layers). **Long-horizon (v3/v4 era)**, gated behind a chain of preconditions: aixodev-web's eventual Rust-server migration → which is "architecturally similar to" the planned Divia.AI Enterprise server → which is gated behind DiviaHome reaching v1.

> ⚠️ **Cross-repo contradiction ([`../../ERRATA.md` E-02`](../../ERRATA.md)):** `aixodev-web`'s own docs call the desktop edition "**AIXO.Dev Desktop**" (`aixodev-desktop`), **Electron-first** (Tauri an open ADR), and don't corroborate a Rust *server* migration. This repo's README is self-flagged "rough-draft, tentative" — so it's the *aspirational* side of a genuine name + stack + framing disagreement. **A John decision.**

## Ideation & Exploration (capture everything, commit to nothing)
- **From the repo:** embedded Rust server inside the desktop app; offline-first + reconcile-on-reconnect; the Twilight theme's long-term role undecided; a Phase-00-on-open to settle desktop architecture + offline-server/sync + the Divia convergence.
- ✦ **New:** the **shared Rust/Tauri desktop foundation with Divia.AI Professional** is the single most concrete piece of AIXO↔Divia engineering cross-pollination in the whole portfolio — worth a small shared "desktop core" library (shell/runtime/local-store/sync) that both products depend on, owned in a neutral place, so the convergence is real code rather than aspiration. ✦ Settle the name/stack question *before* any work starts (it's currently the portfolio's clearest unresolved contradiction) — and if Rust/Tauri wins, the offline-embedded-server pattern is genuinely differentiating for a dev platform ("your whole platform, on a plane").
