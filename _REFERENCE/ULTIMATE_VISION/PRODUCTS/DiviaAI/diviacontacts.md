# Product — DiviaContacts (Gmail · Android · iOS)

> A family of lightweight, **CRM-style reader/viewer** clients that surface the Divia.AI PKMS where
> people already work — starting in Gmail. The explicit model is **Streak/Copper** (CRM-in-Gmail).
> Thin renderers, not full apps; the heavy PKMS stays in Professional + Enterprise.

- **Repos:** `diviacontacts-gmail` (real), `diviacontacts-android` + `diviacontacts-iOS` (empty placeholders).
- **Umbrella / venture:** DiviaAI — see [`../../VENTURES/DiviaAI.md`](../../VENTURES/DiviaAI.md).
- **License:** gmail = **Proprietary** (README prose, no file); android/iOS = **Undocumented**.
- **Status:** 🟠 gmail = research **complete** (16 tracks, ~69k words), pre-Phase-00, no code. android/iOS = ⚪ empty (single 0-byte README each).

---

## What it is (consensus)
**DiviaContacts for Gmail** — a Chrome **MV3 + InboxSDK** extension (Preact + TypeScript in a Shadow DOM; all server traffic via the background service worker). On email-open it **resolves senders to their People/Companies entities** in the Divia.AI PKMS (the Copper/Streak zero-click model), shows their existing pages/notes/docs, **surfaces & manages that entity's tasks and events**, and **logs activity** (emails, calls) back against the person/place/company — keeping the PKMS history complete without leaving Gmail. Identity spine: per-mailbox `(account_email, gmail_thread_id)` + the durable RFC 5322 `Message-ID` for cross-account union. Link-don't-copy privacy posture (IDs + metadata + optional snippet; never bodies). Architecture decided: Workspace Add-ons are disqualified (can't reach a private LAN server; UI ceiling); a thin renderer behind a swappable `DiviaBackend` (Stub ↔ Http).

**Positioning (central):** *Streak* — the CRM that lives inside Gmail (and, fittingly, the makers of InboxSDK). Target market (post-pivot): **Divia.AI Enterprise SMEs**, on the company network, IT-administered; DiviaHome is the interim dev/test server exposing the same REST API. **The moat thesis:** "the organizational task graph is the moat" — Gemini sees one mailbox; the Enterprise server sees the org's task graph, comment threads, and sender→client/project maps. All intelligence is server-side; the extension stays a thin, fast renderer.

**DiviaContacts for Android / iOS** — empty placeholders; planned mobile reader/viewers, scope documented only in the gmail repo's family table.

> ⚠️ ERRATA: the "carried over with full git history from `divia-gmail`" claim isn't corroborated by the git log; the research corpus was produced by **Fable 5** (per John's directive, a capability test); the `_REFERENCE/diviahome-web` symlink is broken. See [`../../ERRATA.md` E-10/E-13`](../../ERRATA.md).

## Ideation & Exploration (capture everything, commit to nothing)
- **From the research (frontier):** cross-mailbox **team awareness** ("this thread already has a task — Sarah created it"); a closed **`waiting`-on-reply loop** (auto-unblocks when the reply arrives); sender-identity resurfacing (open any email from a vendor → see all their open tasks); visible duplicate prevention; a "Today for this team" strip; **Capture-to-Activity-Log** (one click turns an email into a DiviaCard in the ecosystem inbox); resurrected forgotten ideas — PARC TaskMaster "thrasks" (thread+task fusion cards) + two-week red/green deadline bars (user-tested 4.11/5, shipped by nobody in 23 years).
- **LLM horizon:** suggest-and-confirm task extraction; commitment-aware `waiting` ("they promised the contract by Friday"); link-time thread→task summarization; an **agent-accessible task graph via MCP** (Streak shipped MCP June 2026 — precedent set); daily brief / meeting prep from the task graph.
- ✦ **New:** **Capture-to-Activity-Log is the bridge that wires DiviaContacts into the Divia.Network fan-out** — an email becomes a DiviaCard the same agent pipeline classifies and delegates ([`../../USER_STORIES/divia-network-fanout.md`](../../USER_STORIES/divia-network-fanout.md)). ✦ The "thin renderer, server-side intelligence" pattern means new agent capabilities ship as server deploys (no Chrome-review latency) — a structural advantage worth making explicit in the Enterprise pitch. ✦ Recurring-agent fit: the DiviaContacts **relationship-cadence review** (LATER-002 §6) — "you haven't replied to X in three weeks, and last time you said you would" — drafts the reconnection, never sends it.
