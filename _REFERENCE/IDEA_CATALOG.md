# IDEA_CATALOG — the portfolio's ideas, as an outline

> An expansive, deliberately-over-inclusive outline of **every distinct product / product-line / feature / venture idea** found across the MetaProject `_REFERENCE/` docs (ULTIMATE_VISION IDEAS · PRODUCTS · VENTURES · TOPICS · USER_STORIES, SOFTWARE_DEV briefs, the DOMAIN_* / notes / model / strategy docs) **and** the resurfaced "why-I-saved-it" notes from the scattered `_EXTERNAL/` reference-repo indexes (`~/Code/_REFERENCE/external_projects/`). Generated 2026-06-25 from seven parallel extraction passes, then merged here.
>
> **How to read it.** Three levels: **Venture → Product-Line (or feature-cluster) → Idea.** It is intentionally **wide, not deduped** — where two notes sounded even slightly different they were kept as separate bullets, so a subtle distinction you originally intended isn't silently lost. **Pruning, merging, and "these two are the same" calls are yours** — that intent lives in your head, not in the source files. Conventions: `↳ Claude's read:` = my reframing/clarification where I think I can describe the idea better than the terse source note; `(prior-art: repo)` = an idea resurfaced from an external open-source repo you saved as reference; `[name-only]` / `[cryptic]` / `[historical]` flag confidence. A "✦" marks a forward/ideation idea (vs. something already built).

## Cross-cutting patterns & theses (the connective tissue)

These recur across many ventures; I pulled them out so the per-venture sections don't bury them. Each is itself an "idea" — a reusable primitive or a portfolio-wide bet.

- **The implicit-data manifesto** — "observe real behavior; never make the user fill out a form." The single thesis under Divia.AI, DiviaHome replenishment, LegendaryMoney, Sattvasic, GTD. ↳ Claude's read: this is the portfolio's actual north star — *capture-first, infer-later, ask-only-on-conflict* — and most products are one domain's instantiation of it.
- **"First unify, then understand" (scan-and-import data unification)** — v1 of a product just losslessly ingests years of scattered legacy fragments into one clean de-duplicated record; AI inference is explicitly v2. Recurs as the v1 shape of DiviaHome, LegendaryMoney, and Sattvasic.
- **Confidence-aware / suppression-as-first-class-state** — "we don't know yet" / estimated-vs-confirmed must be a normal, renderable output, never a blank. The shared spine of LegendaryMoney's ledger, FracRealHomes' EstimatePacket, and Sattvasic's normalization. ↳ Claude's read: the same data-model seam wearing three domain costumes.
- **Time-decay priority primitive** — "needed within N hours, priority escalating every M hours." Reusable across DiviaHome replenishment, LegendaryMoney, Sattvasic Rx refills, TastyPantry.
- **Lossless-capture-then-parse-later** — preserve the raw NL/source verbatim so interpretation can be redone; the moat version is aixocode's byte-for-byte session archive.
- **Graph-DB convergence core** — one optimized home (Divia.AI Enterprise / proto-divia_ai-enterprise) for the portfolio's core capabilities (graph-DB, knowledge model, task mgmt, research docs); every other product is a **client** of it, not a copy. KingStrat's real business data doubles as the engineering acceptance test.
- **Federated "sign in with Divia"** — one global username federating a user's separate home and work servers; privacy architecture (Global knows *who* you are, not *what* you do) as the marketed product.
- **Recurring autonomous agents — "agent stages, human disposes"** — review/improve/suggest cycles over accumulated implicit data; never auto-commits. An autonomy ladder (L0 reporter → L1 proposer → L2 gated executor → L3 autonomous-with-audit).
- **DiviaCards everywhere** — typed content cards as the universal interchange; "as ubiquitous as http" is the 20-year moonshot.
- **DailySpikeDriver pattern** — a private "idea-of-the-day" playground Build-Line per venture that merges proven slices upward (seen in FracRealHomes and TastyPal). A reusable engineering pattern, not one venture's product.
- **Cross-venture regulatory-tracking agent** — nightly per-state + federal regulatory-change tracker emitting required-app-change diffs; proposed as a shared service across all regulated ventures (CrowdMadness, prediction markets, FracRealHomes, LegendaryMoney).
- **Shared-functionality library / "Rebuild a venture overnight"** — a vetted per-techstack shared library (Python/Flask, SvelteKit, Rust) actively versioned with security-fix-propagation; future-Claude diffs available components against a need and emits an overnight sprint plan ("cookie-JWT like FracRealHomes or Redis-tokens like Patternicity?"). The conceptual root is the Scalara Framework → RosettaMQ lineage.

---

## Divia.AI (the flagship — personal-AI ecosystem; the 30-year arc SAI-4000 → D.I.V.I.A. → DIVIA → Divia.AI)

- **Divia.AI Enterprise** (commercial team server; Rust, after DiviaHome v1 + ~30 days real use)
  - Graph-DB entity-knowledge engine — the converged core capability home; downstream products are clients, not copies
  - Knowledge model · durable task-management · research-documentation handling — the three concentrated core capabilities
  - Enterprise "Research Projects" — `.dvai` LiveDocuments as the marquee knowledge-work feature; B2B beachhead = a continuously-updated portfolio/market dossier (first buyer: KingStratVC)
  - "Morning Briefing" homepage — the Patternicity world-knowledge surface as the default screen a corporate team opens each morning
  - Stable-API implementation-swap — the Python prototype (`proto-divia_ai-enterprise`) exposes a stable API so the Rust rewrite is an implementation-swap clients never feel
  - ✦ "Venture-ideas database" / topic-pages-with-git-merged-ideas as a PoC Enterprise offering for businesses
- **Divia.AI Global (identity/auth SaaS)** — the recurring-revenue identity service
  - "One global Divia.AI username" federating home (DiviaHome) + work (Enterprise) servers; OAuth-style flows, each server a federated node
  - ✦ Context as a first-class axis — user-defined contexts (side business, volunteer org, shared household), each its own server under one identity
  - ✦ Privacy architecture as the product — "your most intimate data never leaves infrastructure you control"
  - ✦ Cross-context queries with explicit per-query consent — "do I have time this week for the school fundraiser?" across work + home calendars
  - ✦ Migration-free-by-design as a marketed promise — placeholder global-identity fields seeded in today's Python prototypes (a `[DEALBREAKER-HOOK]`)
- **Divia.AI Professional** (cross-platform desktop outliner-editor; Rust/Tauri v2 + SvelteKit + TipTap/ProseMirror)
  - Local-first outliner-editor; owns the canonical `.dvai` + DiviaCard implementation the ecosystem reads/writes; the desktop client of Enterprise
  - Adjacency-list tree + TEXT fractional indexing; one outline node = one block row (single-table JSON-properties schema); dual FTS5 (porter + trigram) local search
  - Opt-in / zero-AI-by-default — Claude API with user-supplied key in OS keychain; no bundled model, no training on user data
  - Planned: Loro CRDT collab over DiviaMesh · SQLCipher at-rest encryption + 3-tier key hierarchy · sqlite-vec + Reciprocal-Rank-Fusion hybrid retrieval · `.dvai-open` open mirror · workspaces
  - Shared reusable Rust/Tauri + SvelteKit desktop foundation (base for AIXO.Dev Professional, PatternicityNews Reader, Patternicity.AI Professional)
  - ✦ Notion-style block-based WYSIWYG editor with AI autocompletion (prior-art: novel, Yoopta-Editor, silverbullet, Epiphany)
  - ✦ Opinionated Divia outliner document *syntax* (Org/Markdown/HyperLists-like) with a Tree-sitter grammar (prior-art: syslang)
  - ✦ Office-docs → Markdown ingestion (Word/Excel/images → MD, GPT-4o image parsing) (prior-art: markitdown)
  - ✦ Code-folding / node expand-collapse for the outliner (prior-art: mind, mind.nvim)
- **Divia.AI AgentSwarms** (Rust agent backbone; the OpenClaw/NanoClaw/Hermes "-Claw" agent-harness family — see the separate AgentSwarms research)
  - Agent-hosting & orchestration server — containerized autonomous agents; the "body" in the brain/body/face split; usable standalone, co-deploys with Enterprise
  - DiviaClaw — the named agent-harness sub-brand
  - Recurring autonomous-agent tasks — review/improve/suggest cycles; typed deterministic-vs-probabilistic workflow steps + Haiku→Fable model tiering
  - ✦ Agents as Divia.Network contacts — recurring agents as first-class PKMS entities with people-like pages (view an agent in DiviaContacts like a colleague)
  - ✦ Sell "Swarm runs your dev team's recurring agents" / "Swarm prepares your team's GTD reviews" into every product family
- **DiviaContacts** (CRM-in-the-inbox; thin reader over the PKMS — Streak/Copper model)
  - `diviacontacts-gmail` (Chrome MV3 + InboxSDK) / `-android` (Kotlin) / `-iOS` (Swift) reader-viewers — resolve Gmail senders to People/Companies, surface tasks/events, log activity
  - Relationship-cadence review — "you haven't replied to X in three weeks"; a closed "waiting-on-reply" loop
  - ✦ Cross-mailbox team awareness · PARC-TaskMaster "thrasks" · an agent-accessible task graph via MCP
  - AR storefront-discovery — point your phone camera at a street → overlay the correct Divia.Network links on the stores you see (GPS + compass + light OCR), even for shops without a QR sticker; experimental on `diviacontacts-android`
- **`.dvai` document format & LiveDocuments**
  - `.dvai` — the SQLite-based Divia Document Format (relational rows primary; round-trip import/export first-class)
  - LiveDocuments — documents that refresh themselves on a schedule via a Swarm agent, keeping their own revision history + inline "what changed" diffs inside the SQLite container (a `[DEALBREAKER-HOOK]`)
  - `.dvai-open` parallel format (JSON + Markdown) for lock-in-avoidance / git-diff / interop (OPML, JSON Canvas)
- **DiviaMesh** (sync layer — distinct from the Divia.Network integration layer) — Rust; WebSockets/WebRTC/ZeroMQ + Loro CRDT
- **Divia.Foundation** (planned 501(c)(3) — see also the cross-portfolio "Foundation" notes below)
  - Code Vault / Code Escrow — commercial source released openly after 3–4 years (or immediately on shutdown); ✦ make it a marketed *feature* ("every license includes a guaranteed open-source release date")
  - AI-for-social-good ("$100K–$10M-grade rigor, for free" for nonprofits) · junior-dev training pipeline · open-source-in-the-AI-era licensing advocacy
  - ✦ Divia.Foundation as the open-source release valve for the *whole* portfolio (could cover AIXO.Dev, LegendaryMoney)
- **Knowledge-graph / memory / RAG stack** (mostly resurfaced from `_ORIG.DiviaAI_DiviaLife`)
  - ✦ Temporally-aware dynamic knowledge-graph engine (prior-art: graphiti) + long-term memory layer (prior-art: zep, quivr — "exactly the Divia long-term-memory idea")
  - ✦ "ScaleGraphAI" — LLM-powered web-scraping into a graph — "the exact idea/plan I had for Divia" (prior-art: firecrawl, Scrapegraph-ai)
  - ✦ Graph-based RAG extracting structured data from unstructured text (prior-art: graphrag, R2R "Firebase for RAG", kor, GoLLIE)
  - ✦ Localhost vector search as "the winning ticket" (prior-art: qdrant, milvus) + WASM in-browser vector similarity ("EXACTLY what I wanted") (prior-art: voy, tantara, weaviate) + SQLite vector search (prior-art: sqlite-vss) + semantic GPT cache "perfect for my Divia stack" (prior-art: GPTCache)
  - ✦ Divia prompt router — route prompts to different LLMs by category — "Divia already does this" (prior-art: WilmerAI)
  - ✦ Run open LLMs locally for Divia (prior-art: stableLM, llama.cpp, MLX); self-hosted finetuning + transcript-cleaning (prior-art: tuneAI, mistral-finetune)
- **Divia graph / canvas UI**
  - ✦ Real-time streaming **inline diagrams** from LLM responses instead of plain tokens — "EXACTLY WHAT DIVIA.AI NEEDS … I've been waiting months for this!!" (prior-art: graphologue)
  - ✦ Force-graph node UI using **DiviaCards as the nodes** (prior-art: lit-force-graph, 3d-force-graph); infinite-canvas concept-mapping (prior-art: infinite-canvas); Svelte mindmap (prior-art: svelte-mindmap, NoteWise)
- **Divia console / CLI & editor integrations**
  - ✦ Console Divia.AI app + "Velocity Terminal" exploiting full terminal capabilities (console force-graph, fake-unicode video) — "Mind-blowing" (prior-art: notcurses, vtm)
  - ✦ `divia-cli` markdown-in-terminal app (prior-art: termimad); `dot8-cli` command-bookmark + LLM-help (prior-art: intelli-shell)
  - ✦ Divia's local server exposes an **LSP endpoint** so any editor can edit Divia notes — "CLEVER!" (prior-art: markdown-oxide, logseqlsp); GhostText browser sync (prior-art: nvim-ghost.nvim)
  - ✦ `divia-ai.nvim` / `divia.nvim` Neovim plugin (prior-art: obsidian.nvim); "Divia.AI for Logseq" plug-in (prior-art: logseq); "Divia.AI for VS Code" plug-in (prior-art: dendron); inline image rendering (prior-art: image.nvim)
  - ✦ Google Keep → Divia importer via Google Takeout (prior-art: keep2log)
- **Content / evangelism**
  - ✦ Two-track YouTube engine — "Divia.AI Concepts" + "Command Line Renaissance"
  - **Divia.TV** — "a guide to our video content everywhere, mostly YouTube (monetized) + TikTok tutorials + TikTok lives"
  - **"JS personal Divia.AI PKMS"** — John's own knowledge system where he tags & ingests research (e.g. IdeaBrowser reports) for ongoing editing → feeds KingStrat InsightHub
- **[historical] Divia.Link** — aborted link/URL service (domains slated for deletion Sept 2026)

## DiviaHome (open-source household hub + smart-home device line — "manufacturing and selling smart-home devices and software")

- **DiviaHome Community Edition** (`diviahome-web`, Python/Flask, AGPLv3 + Commercial) — the experimental prototype that gates the entire commercial server line
  - Household "home OS" — four domains: Activity Log (NL DiviaCard capture inbox) · Asana-style tasks · event calendar · `.dvai` document editing; "first unify, then understand"
  - Consumption-driven replenishment / smart-shopping-list loop — observed consumption ("nearly out of milk") → stage a time-decaying grocery item → escalate the errand's priority *before* the staple runs out; runs **nightly**, not weekly
    - ✦ Consumption forecasting, not just thresholds (learn each staple's burn rate) · ✦ per-store routing (bundle low items, time the errand to a likely grocery run) · ✦ household packet as a morning DiviaCard digest in Divia.Life
  - Scan-and-import data-unification release (v1) — SMS logs, receipts, food/meds/purchase notes → one clean de-duplicated record
  - **DiviaHome Global Service** — closed/proprietary federation / message-queue-relay SaaS at `diviahome.com` (NOT a clone of the Community Edition)
- **DiviaHome devices** (separate future hardware repo)
  - **Kitchen-counter ambient voice-capture device** — both an ambient capture surface ("we're out of the good coffee") *and* a morning delivery surface ("before you leave — milk and coffee are on today's list, and the hardware store closes at 6"); "the most demo-able shock-and-awe entry point"
  - **DiviaHome Hub** — router / DNS / DHCP appliance + preinstalled (likely-Rust) commercial DiviaHome server; far-future 2028+ (Shenzhen + tariffs); CLA license decision made now
  - ✦ Minimal Rust appliance OS image for the devices — "Exact idea he had (but in Rust)" (prior-art: gokrazy)
  - Voice stack: ✦ fast local neural TTS (prior-art: piper, mimic3) · ✦ local STT (prior-art: whisper.cpp, whisper-rs, rust-sdl2) · ✦ Mycroft-style assistant core + skills + device-management backend (prior-art: mycroft-core, selene-backend)
  - ✦ Cross-device input sharing (software-KVM / Synergy-like) across DiviaHome devices (prior-art: rkvm)
  - Supporting Rust-server bits: ✦ embed V8/JS (prior-art: rusty_v8) · ✦ dynamic-DNS update (prior-art: dns-update) · ✦ DKIM e-mail delivery (prior-art: mail-send)
- **Divia Agenda** *(spans DiviaHome + DiviaLife — your example idea; I've kept it as its own cluster since it recurs)*
  - Divia Agenda — a GPS-mapped, **forward-looking** daily itinerary/events surface ("inverse of Google Location History")
  - **E-paper desk display for the Divia Agenda** — "Perfect for my Divia Agenda desk-display" (prior-art: esp32-weather-epd)
  - ✦ Agenda-view UI (daily events/tasks view) (prior-art: ms-todo-svelte)

## DiviaLife (closed-source personal "life OS" mobile app — Flutter-first, native Kotlin/Swift later)

- **Divia.Life** — four tabs:
  - **Agenda** — tasks/events + the GPS itinerary view
  - **Journal** — Logseq-style low-friction daily-notes capture feeding the Activity Log
  - **Messages** — Telegram-like ecosystem-native delivery surface (a thread, a DiviaCard — *instead of email*)
  - **Friends & Family** — a configurable aggregated social feed (Instagram/Threads/X/BlueSky via per-network OAuth) — itself an implicit-data engine
- Personal GTD weekly-review system — agent-assisted; the mechanical first pass across the 11 canonical GTD steps compresses the 1–2-hour ritual to a ~20-minute confirm-and-decide; clerk/executive trust boundary (agent stages, never completes/deletes)
  - ✦ Continuous micro-reviews · ✦ two-minute-rule staging (pre-staged reply/calendar-hold, one approval tap) · ✦ adaptive checklist (reorder by what this user lets slide) · ✦ review-the-reviewer quarterly meta-pass · ✦ adversarial cross-vendor review of the packet · ✦ the agent learns the *person* across runs · ✦ review-completion-rate as a product metric
- ✦ DiviaLife terminal/console app via a cross-platform Rust lib + Tauri/Flutter/C++ (prior-art: vtm)
- ✦ Natural-language query over Apple Health data (prior-art: HealthGPT, Stanford CardinalKit)

## Divia.Network (the open, HTTP-like cross-app integration *standard* — "ventures are tech-clients/adopters, not Divia companies")

- Cross-app **fan-out / fan-in bus** — one NL capture ("I had El Pollo Loco for dinner" / "$42 at the hardware store") fans out to TastyPantry (food) + Sattvasic (macros) + LegendaryMoney (expense) + Activity Log; reverses to fan many apps' weekly outputs into one human-paced **"Monday Morning Briefing"**
  - ✦ Ambient capture (fuse GPS + connected-card feed + kitchen device into one high-confidence entry; ask only when sources disagree) · ✦ confidence as a first-class visible thing · ✦ cross-app "Get-Creative" insight ("your late-night fast-food spend tracks with your worst-sleep nights") · ✦ spice-aware fan-out (route the *flavor* dimension of an order to spicemaster3000)
- Agent-driven dispatch — NL capture classified by an AgentSwarms agent → dispatched to multiple downstream apps, each cross-linking back; staging-vs-committing across app boundaries (confirm before commit)
- `Divia.Network/{topic}/` category pages — per-topic directory of adopter apps (finance = LegendaryMoney, food = TastyPantry…); "Certified participants"
- v0 wire/payload contract — versioned cross-app message schema carried via DiviaCards; source-neutral UUIDv7-private-by-default IDs (a `[DEALBREAKER-HOOK]`)
- **Divia.Network as a tutorials/training site** — "online tutorials and training site for the ecosystem of connected apps"; "Managing My Money" microsite (`divia.money → divia.network/managingmymoney/`)
  - ↳ Claude's read: "Divia.Network" is overloaded across the docs — (a) the integration *protocol*, and (b) a public *tutorials site*. Worth deciding if those are one brand or two.
- **Divia.Social** (fediverse) — ✦ a Rust ActivityPub server, contributing the federation crate back upstream (prior-art: rustodon, lemmy, akkoma)
- ✦ DiviaBooks → DiviaNetwork reference-site UI in SvelteKit Material Design (prior-art: m3-svelte)
- 20-yr moonshot — "DiviaCards as ubiquitous as http"

## DiviaCards (the typed-content-card open standard + rendering layer)

- **`divia_cards`** (MIT npm package) — current: 3 flat card types (`nlp_input` / `outline` / `event`); Svelte 5 → framework-agnostic **Web Components** + Shadow DOM + CSS-custom-property theming; working Vue 3 / React 18 demos; Flask-SocketIO real-time card broadcasts
- The **namespaced standard + registry** (forward second Build-Line) — `DiviaCard::<Producer>::<type>` (e.g. `DiviaCard::PatternicityNews::article`, `DiviaCard::LegendaryMoney::transaction(...)`) posted by any app, rendered identically by any app
- One card definition renders identically across every surface — Professional/SvelteKit · DiviaHome/Jinja · Divia.Life/Flutter-webview · DiviaContacts/Gmail
- ✦ DiviaCards as **iframe-sandboxed mini-apps** ("a Notion block with CSS + optional JS/TS") · ✦ a community-contributed DiviaCard **marketplace** · ✦ editable Web Components · ✦ `diviacard://{repo}/{card_id}` cross-repo referenced-card model

## DiviaOS (open-source OS / desktop-environment project under DiviaHome LLC)

- **DiviaWM / VelocityWM** (window manager / Wayland compositor)
  - ✦ Build a Rust Wayland compositor on smithay building blocks (prior-art: smithay, strata); or customize a Python tiling WM, PyO3-rustifying hot paths, first feature = `<super>`-key floating-window overview (prior-art: qtile)
  - ✦ Lua-configured compositor (prior-art: mlua) · ✦ CLI to control it / switch windows (prior-art: stratactl) · ✦ configurable hotkey daemon (prior-art: kagi)
  - ✦ Predictable productivity-focused desktop UX — vertical icon rows + sliding app nav; "AI as copilot" instantly jumping to any window (incl. tmux in a specific alacritty window) (prior-art: material-shell, veshell)
  - ✦ Cross-platform window switcher / ctrl-space launcher-switcher parity on Windows (prior-art: window-switcher)
- **DiviaLauncher** — ✦ a Flow/Niagara-style app launcher (prior-art: lawnchair, Ulauncher, rofi); ✦ a smallest-possible (~1MB static) cross-platform launcher input box (prior-art: fltk-rs); ✦ integrated alacritty+tmux tree-view of sessions/windows
- ✦ Divia clipboard-history manager replacing the GNOME one (prior-art: gnome-shell-extension-clipboard-indicator)

## AIXO.Dev / ExoDev (the dev-tooling family + the consulting studio)

- **AIXO.Dev Platform** (`aixodev-web`) — "Linear + GitHub + Slack for human-AI development teams"; AI agents are full team members
  - Projects · issues (real-time SocketIO, @mentions, `#123` cross-refs, blocks/dupes/parent, templates) · AI-session transcripts (lossless JSONB) with a rich session viewer (progressive tool-call cards, Edit-diff visualization, subagent hierarchy) · per-project versioned wiki (`[[wiki links]]`, revert/diff, Google-Docs-style inline comments) · GitHub integration (`fixes #N`, webhooks) · notifications · analytics dashboards (burndown, contributor activity) · ZIP export/import with SHA-256 manifests (GDPR/CCPA portability) · background workers
  - The **"Ontology" knowledge graph** the team owns — DomainGraph + ClientDomainGraph + EngagementGraph (Palantir-Foundry-modeled; ~25→75 tables; graph-DB deferred: Neo4j / Apache AGE / SurrealDB); bitemporal time-travel; Code-Property-Graph security audits (Joern); a `[DEALBREAKER-HOOK]`
  - Entity-model expansion — Topics/knowledge-mgmt · Planning Units (Goal→Initiative→Phase→Sprint) · DevTask-vs-Issue · Teams + AI-agents-as-members · Workflows · Backlogs + prioritization (RICE/ICE/MoSCoW/WSJF) · session-derived time-tracking · Software-Project library · Saved Views + Custom Fields (the no-migration "Evolvability Hatch")
  - First-class **AI-Agent entity** — model/persona/routing, token budgets, distinct audit/billing/retire; unified with Users via DevTeamMembership
  - Named agent cast, each backed by a different frontier model — @maximus (Architect), @codaramus/@claudius (Guardian/QA), @maxxyscripto/@gemmascripto (frontend), @milton (documentarian); each with a self-editing **`SOUL.md`** that accumulates expertise over months/years
  - ✦ "Mind-blowing" concepts — zero-effort time tracking from session idle-gaps · `@agent` mention → autonomous agent execution · platform-verified sprint workflows (@person/@agent/@platform-verified steps) · Session→Issue→Task auto-pipeline · per-sprint agent performance analytics · research-project → knowledge-base auto-build
  - ✦ An "Agent NOC" inside the platform (last run / findings / pending approvals / cost / autonomy per recurring task) · ✦ graduation-as-a-productized-ritual (certificate + case-study generator; graduation-rate-as-marketing) · ✦ agents as tracked contributors with reputations / craft-score
  - **Engagement Receipts** — cryptographically-signed (ed25519) proof-bundles of what an engagement delivered ("no competitor ships this within 18 months")
  - AIXO MCP server — expose session data / analytics / project context as MCP tools to any Claude-class agent
- **aixocode** (`aixodev-aixocode`, MIT — the open-core top-of-funnel wedge) — Midnight-Commander-style TUI wrapping CLI coding assistants (Claude Code, Codex, Gemini…)
  - MC four-zone TUI (sidebar tree, tabs, F-key bar, 5 themes, fuzzy command palette, snapshots); three modes (default TUI / `--tmux-session` / `--direct` PTY passthrough)
  - **Lossless AI-coding-session capture & archive** — byte-for-byte, never deleted/truncated/schema-changed; the compounding moat (a `[DEALBREAKER-HOOK]`); long cross-tool parser roadmap (Codex, Gemini, aider, Cline, Roo, Goose, OpenCode, IDE parsers)
  - **CollabPairs** — 2 agents + human in a shared chat with a guarded 3-phase `code_review_v1`; "N=2 is the right scale; tests arbitrate, not rhetoric"
  - AgentEngine mode — a worker-agent runtime that long-polls the Platform task queue (documented, not yet built)
  - ✦ CollabPair templates as executable institutional knowledge ("Security Review" / "DB-Migration Review" as shareable org-wide recipes) · ✦ mine the archive ("which steering interventions actually help? how does performance change as SOUL.md grows?") · ✦ async cross-timezone pair-programming with checkpoint handoffs (Dallas 5pm → Bangalore 9am) · ✦ a "remote agent" pane showing the Swarm-hosted fleet beside local terminals · ✦ Rust/ratatui migration · `aixotest` visual-testing tool
  - ✦ `nvim-aixodev` — Telescope project chooser, git-root vs worktree session loading, also configurable from the web UI (prior-art: project.nvim); ✦ context-bundling of related files (prior-art: aider)
- **aixodev-codemap** — source-code analysis: structural call-graphs/symbols (L1) · semantic feature inventory (L2) · AI-mediated cross-project comparison (L3); "Which of my 40 repos implement JWT auth, and how do they compare?"
  - Shared-functionality registry — "Independent Implementation Rate" + "Version Fragmentation Index"; canonical-version selection; security carve-out (extract auth/crypto at 2 implementations); vulnerability flag → fix-once → propagate-to-all-consumers (CVE → techstack → affected Build-Lines → recheck Rust successors)
  - ✦ "Rebuild a venture overnight" · ✦ Build-Envelope → executable starter-kit · ✦ framework reference-docs substrate inside the platform · ✦ far-future: a fine-tuned local LLM trained on RosettaMQ material that scans legacy code and proposes the most elegant architecture
  - ✦ Code-analysis / "Code Reading" feature (prior-art: Juggluco, saved specifically as a test target)
- **aixodev-collabs** — next-gen cross-vendor collaboration bus (supersedes the screen-scraping `ensemble` engine): typed-envelope mail bus + engine-owned task FSM + append-only event log + progress watchdog + human-steering surface (a `[DEALBREAKER-HOOK]`)
- **aixodev-workgroups** — external, deterministic, vendor-neutral **state-server** that offloads `LLM_Rule`/`LLM_Task`/`LLM_Workflow` state out of the orchestrator's context window (run for days without `/compact`)
  - Hybrid **deterministic-gate** workflows — interleave probabilistic LLM steps with deterministic `Code_Task` gates that run **entirely off-context** (the defining innovation); per-step model/effort tiering
  - Cross-repo **rule-sync** — define `LLM_Rule` once → propagate to ~24 repos with recorded local overrides (provenance + regenerate + PR-per-repo + drift detection)
  - Multi-agent dev-team coordination ("Asana for agents") — claim/lock/hand-off/dependency-ordering; Flask system-of-record + FastAPI status sidecar (high-frequency heartbeats off the slow LLM path); ✦ SOMEDAY a "task market" (idle agents bidding on queued tasks)
- **aixodev-openhands** — research/analysis workspace + an "Open Prompt Prototype" (11 React/FastAPI micro-apps); feeds ranked recommendations (e.g. ToM-SWE three-tier agent memory) upstream
- **aixodev-projects** — design-token management: DB-as-source-of-truth, DESIGN.md (Google) ⇄ W3C DTCG JSON round-trip, framework-native CSS (Tailwind 4 `@theme`, Bootstrap, DaisyUI); also the original project-tracker (Project/ProjectLanguage/ProjectRepository); ✦ ship the round-trip engine as a standalone open community tool
- **aixodev-GEN2** — the throwaway Python/Flask CRUD app that edits the new-model entities (Ventures · Build-Lines · Build-Envelopes · Stages · Phases · Sprints · Milestones · Ideas · Topics · Repositories) in a UI
  - Owner (Party) supertype (Venture/Person/Organization, GitHub-style handles) · Build-Line **Generations & lineage** edges (succeeds/forked-from/merges-into; "Gen N" badge; CVE-recheck-successors payoff) · repo→repo clone-lineage provenance
  - **CeremonyLevel** — a first-class, prompt-bearing rigor entity (playground/standard/formal) with versioned, **agent-specific prompt presets** auto-injected on agent spawn (Claude vs Codex, lead vs worker); self-improving (A/B competing prompt variants, eval-scored); Ceremony × Build-Envelope = the agent's full auto-assembled "mission briefing" ("no more read 30 docs first"); auto-escalation on graduation
  - ↳ Claude's read: this is quietly one of the most leveraged ideas in the whole corpus — *the collaboration operating-agreement as versioned, eval-tuned data that every future agent inherits instantly.*
  - Nightly autonomous **"dreaming" agent** — re-evaluates Triangulation-Target placement as tech/regulatory reality shifts ("this once-impossible Target is now feasible → pull it into the current Build-Line") · cross-venture future-scenario projection (the portfolio sliceable by date) · the **Sorting-Hat idea-routing matrix** ("every idea has a home: Product × Build-Line × Version, at a Build-Envelope, toward a Triangulation Target") · scoped context-projection (hand an agent only the relevant context, auto-redacted of playground items + rejected decisions)
  - ✦ Future ontology node-types — **Thesis** (a falsifiable portfolio bet) and **Event/Phenomenon** (a real-world trend the portfolio reacts to)
  - Self-hosting bootstrap — the platform models its own development in the graph; git-history ingest pulls existing Phase/Sprint structures into Build-Lines
- **ExoDev.Pro** (the consulting studio — "Palantir analog"; AIXO.Dev Platforms LLC = "Foundry analog")
  - Forward-Deployed Software Engineering — FDSEs embed 3–4 days/week, ship a production workflow by day 5, "graduate" client engineers by week ~8; the **EngagementGraph**
  - $20K fixed 5-day "AIXO Deployment Week" top-of-funnel pilot · 5-tier per-seat SaaS pricing (Starter $40 → Regulated-OnPrem $225–350) · internal EngagementGraph ops platform (prospect→Graduated→PostGrad, regional-LLC attribution, compounding-IP math)
  - National-LLC expansion ladder — Dallas → LA → NYC/Toronto → 6–8 domestic + 2–3 international by 2028–2030
  - ✦ Consulting business as Divia.AI's reference deployment — run Divia.AI Enterprise inside ExoDev.Pro; every engagement doubles as a live Enterprise demo
  - 8 Phase-D "shock-and-awe" moonshots — claim the FDSE-platform category · the multi-vendor "triumvirate" as a teachable pattern · FDSE-curated cross-client DomainGraph ("we've seen this pattern in 17 similar orgs") · live graph-branch "decision-as-PR" · foundation-model-native graph reasoning · multi-week autonomous project ownership · regulated-industry dominance · cross-org agent-to-agent negotiation
  - "ExoDev Godot Hub" — a coming-soon Godot-related hub at exodev.com [cryptic]
- **AIXO.Dev clients** — AIXO.Dev Professional (offline-first desktop, Rust/Tauri vs Electron name/stack contested) · AIXO.Dev tablet · AIXO.Dev mobile (future)
- **Context-preserving search** — run heavy search I/O in a disposable context, return only distilled hits to the orchestrator (owning project undecided: a Claude skill, an aixocode feature, or a `_workflows/` doc)
- ✦ AI coding-engineer features — full-SDLC AI engineer that specs, asks clarifying questions, then builds (prior-art: gpt-engineer, jacob); chain specialty GPT agents to spin up MVPs (prior-art: khorosgpt); COBOL→Rust modernization (prior-art: CornCob); cross-tool usage metrics (prior-art: cursor-credits); multi-agent collab (prior-art: ensemble, GPTeam)

## KingmakerStrategic (KingStrat — the venture-studio / PE-VC firm; the dogfooding instance)

- **KingStratVC Knowledgebase** (`kingstratvc-web`) — a private single-firm PKMS / company intranet (NOT public/multi-tenant)
  - Private knowledge base · portfolio-company tracking (AI-driven analysis) · idea-stage startup pipeline tracking · a deliberate trial-run of a future Divia.AI Enterprise client install (a git fork of diviahome-web with a shrinking client delta)
  - ✦ Monday partners' brief (recurring Swarm sweep of news/SEC filings/funding events) · ✦ a `.dvai` LiveDocument per portfolio company (self-refreshing dossier) · ✦ dealflow-as-pipeline DiviaCards · ✦ convergence metric as a KPI (the shrinking `main..kingstrat-main` diff = "client need → general feature")
- **KingStrat AdVentureGPS (KSVGPS)** — the venture-studio operating system / business knowledge-graph
  - Three audience-modules — GP Strategic-Landscape & Ideation view · Venture-Studio Operations Center · LP Dashboard
  - **Vector Tracking Loop (VTL)** core engine — fuse all portfolio companies' signals into "a single co-dependent loop" via one centralized estimation engine (Kalman-filter analogy); aerospace/mission-control telemetry UI aesthetic ("Low-Chrome Dark Mode," Deep Obsidian + Neon Cyber Green + Amber, monospace telemetry type)
  - Signal Inception/Acquisition module (model a new sector: teardown sandbox, game-theoretic leverage estimation) · Active Portfolio Tracking Loops (per-company velocity + lock) · Intervention Sandbox & Resource Allocation · Cross-Loop Telemetry · "Asymmetric Decoupling Chart" · Systemic Moat Index (SMI) panel · Live Studio Intervention Trigger form
  - Metrics vocabulary — Fund Velocity Index (FVI), Capital Deployment Efficiency (CDE), Yield Trajectory, Systemic Moat Index, per-company Velocity + Lock
  - The **Strategic Landscape (Module 1)** — a durable, brand-free Ideas & Topics layer with its own research, channel-symlinked to ventures, researcher-vs-GP ACL scoping
  - KSVGPS as the ventures' outsourced support dept — shared legal/finance/marketing + a **domain-management / renewal-reminder system** (no name ever lost — the crowdmadness.com cautionary tale) + a core IP-asset repository (re-assigns IP at incorporation, reclaims on pause/close)
  - Venture-studio corporate blueprint — cheap Texas Series-LLC ("KingStrat V.Studio Fund IV") → ~$25 sub-LLCs → reincorporate to Delaware C-corp at maturity; QSBS / §1202 clock tracking per venture
  - China "Divia" trademark plan — the ~100-page "Divia Trademark Guide" research re-imported into KSVGPS
  - Brand candidates brainstormed (none committed) — KingStrat Helix / Catalyst / Synthesis / Citadel / Vanguard / Kernel / Ledger / Matrix / VTL / Ephemeris; "The Sovereign Stack" [name-only]
- **KingStrat InsightHub / InsightCenter** — "a venture-ideas database for all our ongoing research, planning, early-stage incubator work," an IdeaBrowser-equivalent built deeper; workflow: IdeaBrowser → JS Divia.AI PKMS → augment → publish to InsightHub (on Divia.AI Enterprise); links venture-ideas to CrowdMadness events "to signify why we think trends will happen"; ✦ "Insight Outside" blog name [idle]

## FracRealHomes (Fractional Reality Homes — "frac|real|homes")

- **EstimatePacket / buyer-diligence line** (`fracrealhomes-web` Flask + `fracrealhomes-flutter` mobile)
  - A human-reviewed fractional-diligence engine producing "honest, suppression-aware EstimatePackets across markets"
  - Fractional-ownership / co-ownership **marketplace** (Pacaso + Airbnb + Asana) — thesis = the "Pacaso 8× liquidity trap" (a 1/8 share ≠ whole-home ÷ 8), a visible "fractional value bridge"; first market Manhattan Beach / South Bay LA; legal-classification gate (LLC interest / TIC / private-residence-club / securities) as a front-door gate
  - The evidence spine — Source → EvidenceItem → CanonicalEntity → FeatureObservation → Model/Scenario → EstimateOutput → PublicationSnapshot; `Property` ≠ `Parcel` (M2M, value depends on neighbor parcels via view corridors); source-neutral canonical IDs; immutable published snapshots; **field-level rights ledger** (source × field × transformation × output-lane, post-termination survival); counsel-approved output lanes
  - **View-durability risk modeling** — model a parcel's future view-blocking / legal-max-build risk, not just its current view (the flagship differentiator neither Zillow nor Pacaso expose); expressed as labeled bands (Current Observed / Legal Maximum Screen / Likely Rebuild / Filed Permit / Human Reviewed) — "scenario before coefficient," never a precise dollar discount
  - First-party data capture from day one (cost actuals, owner-use, support, resale/view events) — the only proprietary label store FracRealHomes will own
  - **DailySpikeDriver** — the private "idea-of-the-day" Python/Flask dogfood line; first feature = a Zillow/Redfin email-triage parser "for my own use"; ✦ listing-image acquisition (prior-art: zillow-listing-image-extractor) · ✦ county parcel-map/assessor GIS → shapefiles scraper "WAIT, WHAT???" (prior-art: shapefile-ags)
- **AVM / property-value estimation** — "the next-gen Zillow estimate"; "the same Idea at any scale" → a near-term launch-market AVM (EstimatePacket Line) and a far-future **National-AVM** (multi-market, regulated) are two scale/timing Build-Lines of one Idea
- **FracRealHomes 3D Home** (`fracrealhomes-android`, native Kotlin — a distinct long-term product, NOT a spike) — walk a property capturing photos/AR/depth → assemble a navigable interior 3D model; rights-clean first-party geometry/sightline input feeding the valuation engine (+ a layered Unreal neighborhood model)
- **ADU-advisory data product** — aggregate property details + local permitting rules → AI-generated on-demand report on any property's ADU-building potential, sold as a data/advisory service (channel undecided: a FracRealHomes line or its own venture)

## LegendaryMoney

- **LegendaryMoney PFM** (`legendarymoney-web`, self-hosted local-network-only, AGPLv3 + Commercial) — "Quicken for the rest of us"; an AI PFM built for messy/incomplete money
  - **Confidence-aware ledger** — every transaction tagged confirmed / inferred / estimated + confidence band + provenance, **without ever exposing a debit/credit column**; balance assertions as first-class anchors ("I have $23 in my wallet" → balance-gap differencing → estimated "plug" entries); cash/wallet/informal accounts first-class ("money Mom owes me," roommate split, trip fund)
  - 8-principle creed — accessible-not-accounting · incomplete-by-default · estimate-don't-abstain · no-shame-no-audit-voice
  - v1 scan-and-import (SMS logs, bank/card CSV/OFX, CashApp/Venmo/PayPal, receipt photos → one ledger); v2 understand & infer (full Divia.AI agent + ambient GPS/voice/connected-card); learning loop (sharpens this user's merchant/category priors)
  - Publish `DiviaCard::LegendaryMoney::transaction(...)` to the global registry; LegendaryMoney as **financial-services provider to FracRealHomes** over Divia.Network (purchase / operating-cost / tax flows)
  - ✦ "Remaining financial runway" view as the flagship anxiety-reducer ("how many days can I coast?") · ✦ confidence bands as a visible product aesthetic · ✦ founder story as the wedge ("the people who built your bank's platform, now building the anti-Quicken") · ✦ recurring-agent ledger reviewer (nightly anomaly + balance-drift sweep)
  - Compound cross-app query — "I'm hungry, what are my options for dinner?" from TastyPantry (food on hand) + LegendaryMoney (spendable tonight)
- **PriceScanner** [working name] — a comparison-shopping app: parse purchases (incl. grocery receipts) and price-match each SKU across local stores (Ralphs · Vons · Sprouts · Trader Joe's) + online (Walmart+, Amazon Subscribe & Save); undecided whether standalone / second LegendaryMoney line / PFM feature
- **LegendaryFinancial.AI** — a fractional-CFO service for small businesses (".ai solves the lack of the .com and pitches the value-prop better")
- ✦ Prior-art PFM references — bank-transaction monitor (prior-art: MoneyWatch), registers + investment-portfolio tracking (prior-art: jamesottinger_MoneyWatch), Flutter budget app (prior-art: FEUP_ESOF_MoneyWatch)

## Patternicity (news / world-knowledge / pattern-finding)

- **PatternicityNews** — a news portal built on a self-maintaining **world-knowledge graph** (every person/place/company in every article parsed + modeled; "finding the patterns across the news" *is* the product); seeded from a Wikipedia dump + periodic updates; "why now" = LLM economics making NER-at-scale cheap
  - NER pipeline (LLM + classical); topic-hubs (dozens of graphs with cross-edges); topic-segmented vector search ("not treating 'all of Canada' as the same distance from 'all of horses'"); entity-resolution (one node per real-world entity across thousands of articles)
- **NER-at-scale entity intelligence** — the self-maintaining entity graph of the public world offered as a **B2B entity-intelligence data/API** (same-engine-different-customer)
- **Patternicity.AI Intelligence Services** — world-knowledge + business-data subscription services for corporate clients (Palantir-style); delivered via FDSE engagements; **Patternicity.AI Professional** = a Bloomberg-terminal-style high-density desktop app on the shared Rust/Tauri stack
- **WeighTheFacts (PatternicityWTF)** — a web service constructing chain-of-thought arguments with cross-referenced news evidence, "both sides of the aisle, irreverent but evidence-driven" (`patternicity.wtf`); secondary = an AI-generated YouTube channel for 20–30-year-olds
- **PatternicityNews Reader / Professional** — a cross-platform desktop RSS-newsreader on the shared Divia.AI Professional stack; right-sidebar Divia agent ("right-click a person/company → ask, agent reasons across the entire graph")
- **PatternicitySocial** — an X/Bluesky/Mastodon-like network with first-class DiviaCards (post/discuss articles as `DiviaCard::PatternicityNews::article`); the headline future consumer of DiviaCards; ActivityPub interop
- **Patternicity ONE** — a single monthly subscription bundling premium/paid news sites (NYT, WaPo) — a one-bill aggregated passthrough (licensing feasibility open)
- **Patternicity Bet** — a CrowdMadness market embedded in a news article via a DiviaCard market-card (vs a separate product)
- **URL-shortener / share-attribution** (`ptnws.link`) — mint unique links to track article-sharing (kept as its own Idea for the distinct value)
- World-knowledge **consumption surfaces** — a Divia-agent "memory layer" ("Hey Divia, what's happening with X?") · the Enterprise "Morning Briefing" homepage · an MCP server exposing current news past a model's training cutoff

## CrowdMadness (prediction markets — the MobThought reboot)

- **CrowdMadness** — a massively-scalable prediction-market **game** (play-money / prizes; "like Polymarket/Kalshi, but a game"); the PredictionBracketsEngine; gated by the prize-value legality layer (the MobThought *Big Brother* precedent)
  - Market mechanism fork (order-book vs AMM/LMSR vs parimutuel) · resolution/oracle subsystem (candidate: PatternicityNews's entity/event graph feeds both the questions and their auto-resolution) · append-only auditable settlement/position ledger
  - CrowdMadness markets as **DiviaCard-embeddable** (in a news article, a social post) · market-events as evidence for InsightHub trend theses
- **Real-money, CFTC-regulated prediction market** — a 1:1 Polymarket/Kalshi competitor positioned as commodities-style trading, not gambling (a distinct Idea — different regulatory regime; founder-fit "not-John"; brand must avoid "bet"/gambling; `patternicity.bet` a defensive redirect)
- **White-label prediction-market platform** — partner brands run their own markets on our compliance + engine ("CNN Predictions" embedded in the article a reader is on)
- **CrowdResearch** — online market-research-as-a-service for SMEs: a self-serve client-admin portal to provision surveys, with the aggregated crowd-forecast/sentiment data sold B2B (the play-money game as the top-of-funnel data-generation engine)

## SattvasicHealth

- **Sattvasic Health** (`sattvasichealth`, Flask; possibly a PBC under a planned DIVIA Innovation Foundation 501c3) — a personal health-metrics aggregator + correlation engine
  - Unify a lifetime of scattered health data — labs (cross-lab analyte normalization onto one timeline) · CGM · weight/body-comp (scale + DEXA merge) · Rx/supplements (refill-runway) · food/calorie/macro (consumes TastyPantry) · device/legacy import — then graph → trend → (future) **correlate** ("certain foods → headaches ~2 hours later")
  - ✦ Recurring weekly-correlation agent (LATER-002 §6) · import-adapter/dedup architecture
  - **Bluetooth-scale + AI-food-ID nutrition capture** — an AI photo classifies the food, the scale reads its actual weight, the two fuse into an accurate per-portion estimate (deliberately not photo-only); the reusable BLE-pairing + scale-read + food-ID component is **white-label-able** (backs TastyPal's TastyCal)
- ✦ Prior-art — an AI longevity assistant correlating health data "very similar to Sattvasic" (prior-art: Sequel); wireless CGM pulling from Libre/Sibionics with better graphing + a hidden 1-min Bluetooth mode (prior-art: Juggluco); ESP32 Dexcom/Libre real-time reader (prior-art: Dexcom_Follow, LibreLinkUp_gist); health charts UI (prior-art: fl_chart); NL-SQL over fitness FIT files (prior-art: query_fit_data_using_nl)

## TastyPal (the "your real kitchen, understood" family)

- **TastyPal Platform** (`tastypal.com`) — the "Yelp-for-taste-palates" superset; shared backend + taste-palate AI models; **TastyPal Professional Services** (culinary consultants tuning restaurant menus from the models); `tastypal.ai` "chef-consultants for restaurants" site
- **TastyPantry** (`tastypantry`) — a kitchen pantry-inventory app: Foods/Ingredients · NL Food Logs ("I ate two quesadillas" → decrement) · Grocery Receipts · per-store Shopping Lists · **Recipes-as-compound-foods** (logging a dish cascades decrements to base ingredients); the canonical Divia.Network "food eaten" capture node; the seed prototype the household apps descended from
- **spicemaster3000** (`spicemaster3000`, Flask — the standalone flavor-tech bet, "the most spin-out-able consumer product")
  - Interactive blend builder (ratio sliders, real-time flavor radar, base/accent/heat auto-classification) · **Flavor Bridge Explorer** ("Mexican → Indian: cumin is the bridge" — potentially the single most distinctive feature) · 12-axis "taste fingerprint" radar + supertaster detection + exposure-gap-vs-genuine-dislike · "Virtual Spice Cabinet" (freshness, "what can I make right now," spice auto-replenishment)
  - Data moat — parsed *Flavor Bible* (23,690 pairings / 595 subjects) + FlavorDB molecules + 6 vendor catalogs; FlavorGraph 300D embeddings; the PDF parser (`utilities/verifier.py`)
  - ✦ Universal Flavor Translator ("give me the Mexican version of butter chicken") · ✦ Restaurant Partnership API · ✦ White-Label co-branded blend-builder (Penzeys / Burlap & Barrel / The Spice House) · ✦ genomic taste profiling (23andMe TAS2R38/OR6A2 import) · ✦ Bluetooth smart-scale guided dispensing · ✦ Spice Genome Project (GC-MS of 200+ spices, open-licensed)
- **Flavor-pairing licensable data product** — the cleaned corpus as a B2B data/API asset (recipe apps, CPG R&D, the very spice vendors it catalogs) — a distinct Idea from the consumer explorer
- **TastyCal** [name BLOCKED] — an AI-photo + Bluetooth-scale calorie/nutrition tracker; a TastyPal vertical white-labeling Sattvasic's BLE-scale + AI-food-ID stack; beats photo-only competitors ("Cal AI") via true portion *weight*
- **TastyTrucks** — a food-truck-locator vertical (brand + domain only); **TastySpatialGPS** — food-truck GPS/fleet-tracking (the GridTransmit/SensoryMQ lineage)
- ✦ Wire-together seam — spicemaster3000's "Virtual Spice Cabinet" *is* a specialized TastyPantry (spices as a TastyPantry food category)

## SensoryMQ (IoT — the GridTransmit successor)

- **IoT / connected-device platform** — GridTransmit (award-winning GPS fleet-tracking, 44,000+ devices, 6 countries; sold back to clients ~2018) → **SensoryMQ**, its paused, AI-reimagined successor ("Next-Gen Analytics + Machine Intelligence for IoT")
- **SensoryMQ.Cloud** — a hosted cloud-orchestration platform: CloudXMT (a Kubernetes-precursor) → reimagined; headline = a web-IDE call like `TMobile_M2M_Provider.provision_new_device()` automating a manual 6-week carrier contract negotiation; OpenX-validated (53,000+ server instances); proprietary IoT calls layered on open-source RosettaMQ
- ✦ Prior-art — Rust secrets/config vault with a TUI + multi-language wrappers (prior-art: envkey); minimal Rust appliance image (prior-art: gokrazy); SMQPlayer rewrite in Go (prior-art: savvy-cli); eBPF Rust IoT runtime security (prior-art: pulsar); CVE-database companion (prior-art: kepler); "Utaka System" device-security CLI (prior-art: cosmo-cli); serverless-Rust deploy foundation (prior-art: shuttle)

## RosettaMQ / Scalara (the shared cross-language framework lineage)

- **RosettaMQ** — a planned Rust, cross-language modular framework that transforms legacy code (~a dozen languages) into registered RosettaMQ modules behind a high-performance (millions req/s) microservices fabric; legacy migrations route requests to extracted modules instead of rewriting; planned public open-source (`rosettamq.com`); "the ultimate realization of the Code Map vision"
  - ✦ Far Triangulation Target — a fine-tuned local LLM trained on RosettaMQ reference material that scans legacy code and proposes the most elegant best-practice architecture
  - ✦ Prior-art — Lua-configurable Rust servers (prior-art: mlua); P2P/gossip clustering (prior-art: chitchat); ZeroMQ bindings incl. Kotlin (prior-art: kotlin-zmq)
- **Scalara Web Services Framework** [historical] — an open-source web-services framework (7 generations, C++→Python, 1995–2012); the conceptual root of today's codemap / shared-functionality library; forward life = RosettaMQ
- **AIXO.Dev shared-functionality library per techstack** — a vetted Python/Flask stack, a vetted SvelteKit stack, etc., actively versioned with security-fix-propagation across all projects

## TXFR.Cloud / TXFR.App (high-speed file transfer — see the dedicated TXFRCloud catalog)

- **TXFR.Cloud** — a high-speed file-transfer service (Aspera-like enterprise B2B); planned `txfrcloud-cli` / `-daemon` / `-web`; `txfr.link` = UUID-keyed individual transfers with QR codes; intended as the Divia.AI ecosystem's file-management/transfer backbone (Divia.AI SSO)
  - ✦ Core desktop app (Svelte + Rust + Tantivy) superfast full-text search "exactly like my TXFR.Cloud application" (prior-art: buzee-tauri, xplorer) · ✦ `txfr_console` TUI file explorer ("halfway between broot + mc," image preview) (prior-art: xplr, yazi) · ✦ bidirectional sync (unison-like) with `.txfr_sync_ignore` "Exactly what I wanted" (prior-art: duet) · ✦ file-level Time-Machine (prior-art: httm) · ✦ cross-container media-stream dedup "definitely should integrate" (prior-art: dano) · ✦ cross-platform backup engine (prior-art: restic) · ✦ Rust NFS mount better-than-FUSE + fsspec data-science interface (prior-art: nfsserve, pyxet) · ✦ in-app HW-accelerated crypto (prior-art: RustCrypto, botan-rs) · ✦ BitTorrent/WebTorrent transport (prior-art: rqbit, webtorrent)
- **TXFR.App** — a mobile app for simple device-to-device transfer
  - ✦ Client-side secure **P2P over WebRTC** — "EXACTLY WHAT I WANTED FOR TXFR.App logic" (NAT traversal + local connection negotiation) (prior-art: zero-share) · ✦ a Rust→WebAssembly version covering browsers + mobile + servers together

## Invendra

- **Invendra, Inc.** — venture (domains held; product largely undefined); strongest hint: a **TikTok Shop fulfillment platform, automating order management for "Scaling Creators"** (`invendra.ai`)
- ✦ Invendra.Cloud storefront features — wire-level payment processing (Stripe/PayPal/Braintree) "use in Invendra.Cloud" (prior-art: hyperswitch); a markdown-first CMS / Substack-Mailchimp-Netlify alternative (prior-art: markdown-ninja); a website builder with a Pinegrow-like right-sidebar (prior-art: Visually); a serverless deploy foundation (prior-art: shuttle)

## Dotfigurator (open-source dotfiles tooling — ad-revenue project)

- **Dotfigurator.sh** — a dotfiles-manager application; **Dotfigurate.me** — a companion social network for sharing dotfiles configs; `dot8.me` short alias
- **dot8 CLI / tmux-velocity tooling** — ✦ a `dot8` snippet manager with LLM auto-suggest + flags-vs-data recognition (prior-art: pet, intelli-shell) · ✦ a multi-repo git updater with saved per-command output (prior-art: git-repo-updater, mprocs) · ✦ a GitHub-release universal binary installer for `~/Applications` with stable/beta channels (prior-art: dra, ubi, cargo-binstall) · ✦ YAML-driven whole-machine config (prior-art: flechade, dotter) · ✦ a Python "GUM"-style TUI utility (prior-art: go-fuzzyfinder, gum)
- **tmux session management** (`tmux-velocity` / `tmv` / `tm`) — ✦ a workspace/session-manager TUI (prior-art: mynav, smug, airmux) · ✦ a `tmv` window/session switcher usable inside or outside tmux with cross-platform clipboard (prior-art: tmux-fzf, easyjump.tmux) · ✦ a hierarchical tree-view of sessions→windows (prior-art: tav, twm) · ✦ a "VelocityTerminal" suite of Rust terminal apps (git-log viewer, tmux-fingers copy/paste) (prior-art: serie, tmux-thumbs)

## ReDreamRebuild (renovation & remodeling education-content venture — SEO-led ad + affiliate)

- Renovation/remodeling education-content site — "see the entire quality/price spectrum first, then make an informed value choice" as the signature teaching frame; material selection across the full price-quality spectrum (flooring → counters, roofs, fixtures, lights); "how to spot bad contractor work" (wrong-order roof-tile layering); before/after case studies (John's own $150K→$910K SoCal project as the hero piece)
- **Contractor OSHA safety report-cards** — per-contractor "safety report-card" tracking OSHA / state safety-compliance violations over time for every contractor in a state (integrated into the content site as an SEO compounder; content + data as a two-layer moat)
- ✦ Independent third-party quality-oversight as a content (and possible service) theme · ✦ affiliate depth on materials at multiple price tiers

## Cross-portfolio / studio-level & corporate-structure ideas

- **ExoDev corporate structure** — ExoDev.AI Corp. (holding parent, name TBD) over ExoDev.Pro, Inc. (consulting, Dallas HQ) + AIXO.Dev Platforms LLC (product) + regional services LLCs (Dallas / LA / Chicago, with per-office client PM portals like `dallas.exodev.pro`); Scalara Inc. as the LA predecessor
- ✦ A clean personal **holding structure** naming the relationship over both ExoDev.Pro, Inc. and Divia.AI, Inc.; a portfolio "category" story (ExoDev = "Palantir analog," Divia.AI = "personal Palantir / personal data ontology"); spin-out optionality tracking (which ventures stay internal vs. could raise/spin out — LegendaryMoney the clearest path)
- **The DIVIA Innovation Foundation** — an operating 501(c)(3); `divia.shop` / `diviafoundation.shop` affiliate-marketing site whose commissions go entirely to the foundation ("Leverage Technology to Do Well + Do GOOD"; reframe the FTC affiliate disclaimer as "a way to help the foundation"); a single "divia foundation" TikTok account combining foundation content + shop posts; a local LanceDB search on the foundation page answering "why isn't it free?"

## Personal brand, books & content (John Stanforth)

- **Books** — *The DIVIA Mentality: AI-Augmented Superpowers* · *The Neurodivergent DIVIA Mentality: 21-Day Map to Realize ADHD Superpowers* · *The Success Playbook* (co-authored, Ray Brehm et al.) · *Billion-Dollar Platforms: Hard-Won Lessons from 25 Years of Python, C++, and Rust Development in Los Angeles*
- **Personal site / blog** — `johnstanforth.com` author page (later an author page with linked ventures) · `stanforth.ai` (possible new blog / replacement) · "Insight Outside" blog name [idle] · "LA CTO group" (monthly in-person)
- **Rust-development SEO/content microsites** — `rustdevelopment.la` / `rustdevelopmentlosangeles.com` / `rustdevelopmentdallas.com` / `rustdevelopment.com` (keyword-research pending) · `billiondollarplatforms.com/rustdevelopmentlosangeles/` landing page

## Name-only / latent / TBD (held domains or brand names with no described product yet)

- **VelocityTerminal** (`velocityterminal.sh`) — a terminal/CLI tool/suite (also surfaces inside Divia console + Dotfigurator); an earlier abandoned partial-progress project to modernize before adoption [cryptic]
- **JSL Dragonfly** (`jsldragonfly.com`) — JSL Dragonfly Ltd., classified as an ad-revenue / YouTube project [name-only]
- **CTO Mindmeld Publishing, LLC** (`ctomindmeld.com`) — a publishing/media-content venture; possibly a "CTO mind-meld" advisory/content site [name-only]
- **AdEvolve, Inc.** [historical, 2005–2014] — a marketing company; `adevolve.ai` a possible AI-branded revival
- **Neurogrammatic** (`neurogrammatic.com`) — implies a "neuro-grammar"/NLP product; nothing beyond the name [name-only]
- **Quintivity** (`quintivity.com`) — implies a productivity/"quint-activity" product; nothing beyond the name [name-only]
- **Surreality** (`surreality.com` / `.ai`) — held "just so no one else gets it"; nothing beyond the name [name-only]
- **Transformulator** (`transformulator.dev` / `trfl.dev`) — a "transform-ulator" dev-tool; nothing beyond the name [name-only]

## Loose / not-yet-homed ideas (surfaced in passing; venture attribution unclear)

- An "omm"-style keyboard-driven CLI task manager backed by a cross-platform Rust common-lib with CRDT multi-user editing (prior-art: omm)
- Photo-editing / image-restoration (e.g. wedding photos) (prior-art: UnpromptedControl, clarity-upscaler) · line-level multilingual OCR (prior-art: surya)
- SMS/MMS/call-log reading for a mobile app (prior-art: sms-backup-plus) · geo-query "nearby places" via LLM (prior-art: ChatGeoPT)
- Messaging-channel integrations — Telegram bots (prior-art: teloxide, grammers), a terminal Signal client (prior-art: gurk-rs), an FB Messenger bot · a Rust Spotify client "YAAAY!!!" (prior-art: rspotify)
- An audiobook organizer/tagger + Libby downloader (prior-art: audiobook_tagger, libby-download-extension)
- A read-it-later reader app (Omnivore/ElevenReader-style) — possible Patternicity feature (prior-art: omnivore)
- Video-conferencing in Rust (Zoom-like) (prior-art: zoom-rs)
