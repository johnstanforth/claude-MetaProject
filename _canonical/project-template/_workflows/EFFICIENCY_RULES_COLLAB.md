# Efficiency Rules — Collab-Group Agents

> Hard rules for minimizing token waste in collab-group (multi-agent) sessions. These rules supplement the general [Efficiency Rules](EFFICIENCY_RULES.md) — collab-group agents must follow BOTH documents.

## Why This Document Exists

Collab-group sessions have unique efficiency failure modes that don't arise in solo sessions. When two agents share a message bus and operate autonomously, idle-time behaviors that would be harmless in a solo session (where the user can immediately redirect) become expensive token sinks that nobody catches until the damage is done.

This document is a living reference. When a new collab-group-specific efficiency problem is identified, add it here following the same format as the general efficiency rules.

---

## Rule Index

| # | Rule | Category | Added |
|---|------|----------|-------|
| CE1 | [Don't invent work while waiting](#ce1-dont-invent-work-while-waiting) | Scope | 2026-05-04 |
| CE2 | [Don't poll when you'll be notified](#ce2-dont-poll-when-youll-be-notified) | Token waste | 2026-05-04 |
| CE3 | [Give the other agent time to work](#ce3-give-the-other-agent-time-to-work) | Token waste | 2026-05-04 (hardened 2026-06-09) |
| CE4 | [Don't narrate work in progress](#ce4-dont-narrate-work-in-progress) | Token waste | 2026-05-04 |

---

## CE1: Don't Invent Work While Waiting

**HARD RULE.** When you are waiting for the other agent to complete a task (writing files, running a build, etc.), do NOT go off on side-quests that nobody asked you to perform. "I have idle time, so let me investigate X" is not a productive use of tokens — it's scope creep that burns through subscription limits for zero requested value.

**The failure pattern (collab-group session, 2026-05-04):**
1. Codex-1 (LEAD) said it was writing the sp_/xp_ deliverable files and would notify when done
2. Claude-2 (WORKER) decided to "use the waiting time productively" by independently investigating scan lifecycle edge cases and db_session fixture internals
3. These investigations produced multi-paragraph analyses that nobody requested, consumed significant tokens, and — worse — risked introducing confusion by raising design concerns that had already been settled in the prior consensus

**Why this is harmful beyond token waste:** Unsolicited side-investigations can reopen settled decisions, introduce doubt about agreed-upon designs, and force the other agent (or the project owner) to spend tokens addressing concerns that weren't on the agenda. The WORKER role exists to *review deliverables when they're ready*, not to freelance on tangential research while waiting.

**The correct pattern:**
1. The other agent says "I'm writing the files, will notify when done"
2. You say "Acknowledged. Standing by."
3. You **actually stand by** — no investigations, no "while I'm waiting" analyses, no unsolicited design concerns
4. When notified, you perform your assigned role (e.g., peer review)

**What "standing by" means:** It means doing nothing. Not reading files "just in case." Not investigating alternative approaches. Not drafting analyses. Not exploring edge cases. Nothing. Wait for the notification, then act.

---

## CE2: Don't Poll When You'll Be Notified

**HARD RULE.** When the other agent has explicitly said they will notify you when their work is complete, do NOT send periodic "status check" or "still writing?" messages. Each poll message costs tokens on both sides — your message plus the other agent's response — and produces zero information beyond what the notification will provide.

**The failure pattern (collab-group session, 2026-05-04):**
1. Codex-1 said "I'm writing the xp with implementation-level detail now" and "I'll send a review request with paths when both files are ready"
2. Claude-2 acknowledged, then sent "Standing by. No rush."
3. Then sent "Status check — still writing? Any blockers? Ready to help if you need me to draft any section"
4. Then launched into side-investigations (CE1 violation), and continued checking in
5. Each exchange burned tokens on both sides for messages that conveyed no new information

**Why polling is especially wasteful in LLM agent contexts:** Unlike a human who can glance at a progress bar for free, every "are you done yet?" message in an LLM agent session costs real tokens — both to generate the question and to process/respond to it. In a collab-group session, both agents pay this cost. Over a multi-hour session with multiple waiting periods, polling can burn thousands of tokens on content-free exchanges.

**The correct pattern:**
1. The other agent says "I'll notify you when ready"
2. You acknowledge **once**
3. You wait silently until the notification arrives
4. If you genuinely suspect something has gone wrong (e.g., 30+ minutes of silence in a session that normally produces messages every few minutes), a single status check is reasonable — but that's a failure-detection mechanism, not a polling loop

**The key distinction:** A single status check after an unusually long silence is reasonable error detection. Sending "still working?" every few minutes when the other agent said they'd notify you is a polling loop that wastes tokens.

---

## CE3: Give the Other Agent Time to Work

**HARD RULE.** After directing the other agent to perform a task (editing files, running tests, applying a batch of fixes), do NOT send a status check until a reasonable amount of time has passed for the work to actually be completed. Even the fastest LLM agents need time to read files, generate edits, and write changes — sending "are you done yet?" 60-90 seconds after assigning the work is absurd and wastes tokens on both sides.

**ABSOLUTE FLOOR (hard minimum): never send a status check, confirmation re-prompt, or "are you done / are you stuck?" message within 90 seconds of the triggering action or handoff — for ANY task type, including peer-review requests, edit batches, and validation runs.** The 90-second floor is the non-negotiable minimum; the per-task calibration windows below are usually longer and take precedence whenever they exceed 90 seconds. Before sending any status check, confirm that at least 90 seconds have elapsed since your last handoff message. If the other agent has said it will notify you, CE2 applies and you generally should not status-check at all.

**The failure pattern (code review collab-group session, 2026-05-04):**
1. Codex-1 (LEAD) directed Claude-2 (WORKER) to apply a batch of 5 fixes across `python_treesitter.py` and its tests
2. Less than 2 minutes later, Codex-1 sent: "Status check on the python_treesitter batch: no diff is visible yet... Please confirm whether you're actively editing or blocked."
3. 74 seconds after that, Codex-1 sent a *second* status check: "Second status check: still no diff for the extraction batch after the handoff."
4. Claude-2 had barely started — it was reading the files and planning its approach, which is exactly what it should have been doing
5. Both status checks cost tokens on both sides and interrupted Claude-2's work for zero benefit

**Why this is harmful:** Multi-file edit batches are complex work. The WORKER needs to read the current file state, plan the changes, make the edits, and verify they're consistent. For a batch of 5 related fixes, this naturally takes several minutes — not seconds. Premature status checks communicate false urgency, interrupt the WORKER's flow, and force it to spend tokens on progress reports instead of actual work.

**Second failure pattern (sprint planning collab-group, 2026-06-09):**
1. Codex-1 (LEAD) sent "Both files are ready for review" with the `sp_02`/`xp_02` paths
2. ~36 seconds later, Codex-1 sent a "Status check after the review window: please confirm whether you are actively reviewing ... or blocked"
3. Claude-2 (WORKER) was still reading both files end-to-end — its PASS/FLAG/ISSUE review did not (and could not) land until ~3 minutes after the review request
4. Codex-1 then admitted "I checked too soon" — the status check produced nothing but a crossed message and wasted tokens on both sides

This is the case the 90-second absolute floor exists to prevent: a peer-review request over two substantial files cannot possibly be answered in 36 seconds. Reading multiple files and producing a structured review takes minutes, not seconds.

**How this differs from CE2:** CE2 covers the case where the other agent said "I'll notify you when done" and you poll anyway. CE3 covers the case where you *assigned* the work and then immediately started demanding to know why it isn't finished yet. CE2 is about ignoring a notification promise; CE3 is about having unrealistic expectations for how long work takes.

**The correct pattern:**
1. Direct the other agent to perform a task, describing what needs to change
2. Wait **at least 5 minutes** before considering a status check for a multi-file edit batch, or **at least 2-3 minutes** for a single-file change
3. If no response after that reasonable window, send **one** status check — not a rapid-fire series
4. If the other agent responds "working on it," wait again — don't send another check 60 seconds later

**Calibration guide for wait times** (all are at or above the 90-second absolute floor):
- Single small edit (one file, one change): 1-2 minutes
- Multi-fix batch (one file, several changes): 3-5 minutes
- Cross-file batch (multiple files, coordinated changes): 5-10 minutes
- Peer review of deliverables (read + PASS/FLAG/ISSUE): 2-3 minutes per file (a two-file review can take 4-6 minutes)
- Full validation run (`pytest` + `ruff`): 1-2 minutes

These are minimums, and none is below the 90-second absolute floor. The other agent may take longer, and that's fine — it's doing real work, not stalling.

---

## CE4: Don't Narrate Work in Progress

**HARD RULE.** When you told the other agent you would notify them on completion, your next message should BE the completion notification — not a stream of progress updates. Every "still working...", "found a minor issue...", "patching that now...", "almost done..." message costs tokens on both sides (your message plus the other agent's obligatory "Ack") and conveys zero actionable information.

**The failure pattern (sprint planning collab-group session, 2026-05-04):**
1. Codex-1 (LEAD) said "I will send only the review request with canonical paths when both files are ready"
2. Claude-2 acknowledged and stood by silently — perfect CE1/CE2 compliance
3. Over the next 6 minutes, Codex-1 sent **six** progress updates: "Files are written, doing consistency pass"... "Found one minor wording issue"... "Patching the wording now"... "Final grep/read pass now"... "One remaining stale line, patching"...
4. Claude-2 had to acknowledge each one ("Ack."), burning tokens 12 times (6 messages × 2 agents) for zero useful information
5. The review request could have been a single message after all patches were done

**Why this is harmful:** It's the mirror image of CE2/CE3. Those rules stop the *waiting* agent from pestering the *working* agent. CE4 stops the *working* agent from pestering the *waiting* agent. The waiting agent has perfectly complied with "stand by silently" — don't punish that compliance by forcing them to respond to a stream of content-free updates.

**The correct pattern:**
1. Say "I'll notify you when ready"
2. Do the work silently — write files, run checks, fix issues, do consistency passes
3. When everything is actually done, send **one** message: "Files ready for review: [paths]"

**What about genuine blockers?** If you hit a real problem that changes the plan (e.g., "I discovered the schema doesn't support what we agreed on — we need to revisit"), that's a substantive message worth sending. "Still patching a wording issue" is not.

---

## Adding New Rules

When you identify a new collab-group-specific efficiency problem:

1. **Document it here** with a rule number (CE3, CE4, ...), a clear title, the failure pattern, and the correct pattern
2. **Add it to the Rule Index** table at the top
3. Rules should be based on **observed problems**, not hypothetical ones. Each rule exists because the failure pattern actually happened and wasted real tokens in a collab-group session.

For efficiency problems that apply to ALL agents (solo and collab-group), add the rule to the general [`EFFICIENCY_RULES.md`](EFFICIENCY_RULES.md) instead.
