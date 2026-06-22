# LATER-006 — Claude's rich output should live in a rendered, consolidated UI surface (not scattered TUI chat)

- **Captured:** 2026-06-22, MetaProject session (immediately after a Mermaid diagram failed to render in the Claude Code TUI / a copy-paste into Typora lost the ` ```mermaid ` fence).
- **Status:** LATER — explicitly "a discussion for later" (John); not yet assigned to a sprint.
- **Eventual owning project(s):** **Divia.AI Professional** (`divia_ai-professional`) — the desktop app where John keeps notes and where Claude is intended to be integrated; **`aixodev-aixocode`** (today's Claude Code session manager / the TUI where output currently scatters); possibly **`aixodev-web`** (server-side surfacing).
- **Related:** [`LATER-005-context-preserving-search-workflow.md`](LATER-005-context-preserving-search-workflow.md) (same "preserve the orchestrator/collaboration experience" theme) · the `_skills/research-pdf` skill (an existing "render rich content *outside* the TUI" precedent) · Divia.AI Professional's "everything is a DiviaCard" + `.dvai` LiveDocument model.

## The triggering observation

Rich content Claude produces — **Mermaid diagrams especially, but also long analyses, decision write-ups, and tables** — does not render in the Claude Code TUI, and copy-pasting the on-screen output into a renderer (Typora) silently **drops the ` ```mermaid ` fence** (the TUI swallows the fence lines when it draws the diagram). More broadly: a lot of high-value information (the two-layer model discussion, the venture briefs' reasoning, diagrams) currently lives **scattered across long chat messages in the TUI scrollback**, rather than in consolidated, navigable, *rendered* files alongside John's own notes.

## The idea (revisit later)

Once Claude is integrated into **Divia.AI Professional** (where John's notes live, with native rendering of Mermaid / DiviaCards / LiveDocuments), Claude should be able to **write responses — including diagrams — directly to specific files/cards that show up in that UI**, so all related information sits together and renders correctly, instead of in ephemeral TUI chat. The collaboration shifts from "long messages I have to copy-paste and re-fence" to "Claude updates the living document/card I'm already looking at."

## Why it matters

- **Consolidation:** related facts/diagrams/decisions live with the notes they belong to (a venture's LiveDocument / a topic's card), not in chronological chat scrollback.
- **Rendering:** Mermaid, tables, and structured content display as intended — no fence-stripping, no copy-paste fidelity loss.
- **Provenance + reuse:** output becomes durable, addressable, and queryable (a step toward the KSVGPS graph-DB bootstrap, where these markdown drafts already aim to live).

## Shapes to consider (decide at triage)

1. **Divia.AI Professional as the surface** — Claude writes/updates `.dvai` LiveDocuments / DiviaCards that John has open; the "Research Project" / self-refreshing-dossier pattern, but driven by an interactive Claude session.
2. **`aixocode` writes to files** — the session manager exposes a "write this response/diagram to `<file>`" affordance so rich output lands in a chosen file (rendered in Typora / the IDE) instead of only the TUI.
3. **A hybrid + a heuristic** — Claude decides what belongs inline in chat vs. what should be written to a file/card (diagrams, long structured artifacts → file; conversational reasoning → inline).

## Immediate stopgap (already in use)

When a diagram is meant to be saved, either re-add the ` ```mermaid ` / ` ``` ` fences around the pasted block, or ask Claude to **write the diagram straight to a file** (fences intact) rather than relying on copy-paste from the TUI.
