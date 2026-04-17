# CG-Rectify Interactive Resume Prompt — paste verbatim into a fresh Claude session

## What this is

A direct-session kickstart for the **chriss-ginzburg-rectify** rectification loop on this volume of the *Modular Koszul Duality* monograph. This is NOT the cron architecture (`cg_rectify_kickstart.md`); this is the interactive-session architecture. Paste the prompt below into a fresh Claude session and it will resume exactly where the previous session left off: pick the next pending queue entry, invoke the full five-phase skill with small chunks and parallel adversarial audits, register any new anti-patterns/cache entries as it finds them, commit and mark the entry on completion.

## How it differs from the cron kickstart

| | `cg_rectify_kickstart.md` (cron) | this file (interactive) |
|---|---|---|
| Execution model | Scheduled remote agent, one chapter per firing | Live session, sequential through the queue |
| Context per chapter | Fresh (via `RemoteTrigger`) | Shared across chapters in the same session |
| Chunk size | ~50–100 lines | **~50 lines (small)** — the user is watching |
| Phase 4 adversaries | Dispatched via `Agent(run_in_background=true)` within the tick | Dispatched via `Agent(run_in_background=true)` in a single parallel batch |
| Human presence | None | Yes — user is interactive and may redirect |
| Queue update | Per-tick `[x]` / `[~]` write + commit + push | Per-chapter `[x]` / `[~]` write; commit only on explicit request |

## The kickstart prompt

Copy everything between the `=== BEGIN ===` and `=== END ===` markers below and paste it into a fresh Claude session.

```
=== BEGIN ===

You are resuming the interactive chriss-ginzburg-rectify loop on this volume of the *Modular Koszul Duality* monograph. A prior session (or sessions) ran the same loop — queue progress is tracked per-chapter in this volume's queue file. Your job is to pick up from the next pending entry and run the full five-phase skill.

Before doing ANYTHING, in order:

1. Detect the volume. Run `pwd` and match against these absolute paths:
   - `/Users/raeez/chiral-bar-cobar` → Volume I (*Modular Koszul Duality*, bar–cobar & modular characteristic)
   - `/Users/raeez/chiral-bar-cobar-vol2` → Volume II (A∞ chiral algebras & 3D HT QFT)
   - `/Users/raeez/calabi-yau-quantum-groups` → Volume III (CY categories, quantum groups, BPS algebras)
   State which volume you are in.

2. Read `CLAUDE.md` in full (this volume's project instructions). Internalize:
   - The HOT ZONE (HZ-1 through HZ-10 if present) and the top-5 most-violated AP classes for this volume.
   - The Wrong Formulas Blacklist (B-entries) and the consolidated APs (AP-RMATRIX, AP-KAPPA, AP-DESUSP, AP-SC-BAR, AP-TOPOLOGIZATION, AP-LABEL-DISCIPLINE, etc.).
   - The **Manuscript Metadata Hygiene (CONSTITUTIONAL, ZERO TOLERANCE)** section: no AP identifiers, wave/campaign/session timestamps, blacklist slugs, or `RECTIFICATION-FLAG` markers in typeset prose. Grep-gate before every commit.
   - Volume-specific kappa/convention rules (Vol I: bare κ OK; Vol II: SC^{ch,top} semantics; Vol III: κ subscript mandatory from {ch, cat, BKM, fiber}).

3. Locate this volume's queue file:
   - Vol I: `notes/cg_rectify_redo_queue_2026_04_17.md`
   - Vol II: `notes/cg_rectify_redo_queue.md` (scaffold if missing; enumerate chapters from `main.tex` minus abstract/preface/introduction)
   - Vol III: `notes/chriss_ginzburg_full_rectify_queue.md`
   Read the queue. Find the FIRST `[ ]` or `[~]` entry matching `- \[[ ~]\] \`chapters/…`.

4. Skim the first-principles cache at `notes/first_principles_cache_comprehensive.md` (Vol I) or the equivalent for this volume. Pay attention to the most recent Pattern entries (numbering continues linearly — the last ~10 patterns capture the patterns most likely to recur).

5. Claim the next pending entry — do NOT skip around, do NOT pick the short ones, do NOT pattern-match across files. Linear order.

For the claimed file, invoke the skill via

    Skill(skill="chriss-ginzburg-rectify", args="<absolute path>")

and execute all five phases. No phase may be shortcut.

**Phase 1** (global diagnostic, read-only). For files ≤3000 lines: read end-to-end. For >3000 lines: sample strategically (opening preamble, section heads, a dense technical mid-section, and the closing). Produce the 7-heading diagnostic (narrative thread, motivation gaps, define-before-use violations, opening/closing, physical-insight labels, prose hygiene, formula red flags). Keep it to a numbered list, not an essay.

**Phase 2** (platonic restructuring). Execute only load-bearing structural edits: fix metadata leaks (AP identifiers, wave-N, blacklist slugs /B\d+, empty `\textup{()}` artifacts, orphan labels), heal broken cross-references (grep `\ref{...}` against targets), de-duplicate labels if there is an actual *collision* (multi-labels on one env are fine; same label on distinct envs is a bug). Avoid heavy restructuring on an already-rectified chapter.

**Phase 3** (linear reconstitution loop — THIS IS WHERE THE WORK IS).
- Small chunk size: ~50 lines. The user is watching; work fast with tight verdicts.
- Five gates per chunk: (G1) mathematical truth, (G2) define-before-use, (G3) concept motivation, (G4) physical realization, (G5) Chriss-Ginzburg reconstitution / fifteen-peak standard.
- Gate 1: verify every formula FROM FIRST PRINCIPLES against `chapters/examples/landscape_census.tex` and the `compute/` layer. Do NOT pattern-match across occurrences (AP3). Known traps: κ values (AP1/AP-KAPPA), r-matrix level prefix (AP126/AP-RMATRIX), Sugawara shift on av(r) (FM11), five-object discipline B ≠ A^i ≠ A^! ≠ Z^der (AP25/AP34/AP50), T^c(s^{-1}\bar A) with augmentation ideal (AP132), desuspension lowers degree (AP45), η = d log is bar coefficient, not connection 1-form (AP117 — η_{ij} is a SCALAR; the connection 1-form is the t_ij-valued sum Σ t_ij η_ij).
- Gate 2 is HARD: every symbol defined at or before first use. Add parenthetical first-principles definitions for standard concepts (D-module, Ran space, prime form, Hodge bundle, MC element, etc.) at first use.
- Gate 3 is HARD: every definition preceded by the question it answers.
- Gate 4: OPE / BV / BRST / anomaly / partition-function identifications correctly labelled theorem (with citation), heuristic (with evidence), or metaphor (with honest label). No physical derivation presented as mathematical proof.
- Gate 5: Chriss-Ginzburg register. **No AI slop** (notably, crucially, moreover, remarkably, furthermore, interestingly, delve, leverage, cornerstone, tapestry). **No em-dashes** in body text (`---` / U+2014). **No throat-clearing** ("this chapter shows", "the structural reading of this chapter is that", "we now", "having established", "let us"). **No hedging** in mathematical claims (seems to, appears to, arguably, perhaps). If the mathematics is clear, state it; if unclear, mark conjectural. **Courage**: identifications stated as identifications — "the partition function IS the Hodge class", not "is closely related to".
- After every 3 fixes: build (or grep-balance if pdflatex unavailable: `grep -c '\\begin{'` == `grep -c '\\end{'`).
- After every formula change: grep all three volumes (AP5) at `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`.
- Safety valve: if a chunk won't converge after 11 iterations, mark `% RECTIFICATION-FLAG: [gate, reason]` and advance. Eleven is generous; most chunks converge in 2–3.

**Phase 4** (parallel adversarial re-audit). Dispatch THREE agents in a **single message** using `Agent(subagent_type="general-purpose", run_in_background=true)` (not sequentially). Scripted roles:
- **RED** — adversarial falsification of every edit this session landed. Load `CLAUDE.md` AP catalogue. Verify formulas from first principles. Cross-check AP-compliance on all edits. Check ~170 `\begin{}`/`\end{}` balance. Scan the chapter for unrelated AP violations.
- **BLUE** — consistency audit. Cross-reference resolution (`\ref` targets exist). Formula consistency with `landscape_census.tex`. AP5 cross-volume. Begin/end balance + proof-pair balance. Metadata-hygiene grep (`\bAP\d+\b`, `\bHZ-\d+\b`, `/B\d+`, `first_principles_cache`, `RECTIFICATION-FLAG`, `Pattern \d+`, `Cache #\d+`, `wave-\d+`, `\barity\b` must all return 0).
- **GREEN** — quality vs. fifteen-peak standard. Prose hygiene. Connective tissue at every section boundary (three-sentence rule: where-are-we / what-forces-next / what-is-the-answer). Define-before-use end-to-end. Physical claim labelling. Opening-and-closing crystallization. Inventiones-referee verdict.

All three agents report back in under 500 words each. Merge findings. Any agent's CRITICAL/SERIOUS finding triggers Phase 3 re-entry on the affected chunks only. If all three report CONVERGED (zero actionable findings at severity ≥ MODERATE), proceed to Phase 5.

**Phase 5** (final convergence).
1. Re-read with fresh eyes.
2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. If pdflatex is unavailable in the environment, fall back to grep balance check.
3. Tests: `make test` if available.
4. Report: chunks processed, iterations, findings fixed by severity (CRITICAL/SERIOUS/MODERATE/MINOR), gate-failure distribution, RECTIFICATION-FLAGs left open, Phase 4 verdicts, final line count, build/test status.
5. Mark queue entry: `[ ]` → `[x]` with a one-paragraph completion note (what was fixed, which agents converged, residual flags). Write cursor `% RESUME-FROM: <chunk>` if marking `[~]` partial.

**As you discover new anti-patterns or cache violations, write them to the metacognitive architecture.** New patterns go into `notes/first_principles_cache_comprehensive.md` with next-in-sequence numbering (read the tail, take the next `Pattern N`). New APs go into `CLAUDE.md` under the "AP234-235" / latest-AP block (`AP236 (…): …`). This file is the author's working notebook; the manuscript is the reader-facing object. NEVER reference Pattern N or AP N in typeset prose; ALWAYS register them in the notebook.

**Constitutional rules (non-negotiable).**

- Author is always `Raeez Lorgat`. NO AI attribution. No `Co-Authored-By: Claude`.
- `git stash` is FORBIDDEN. Use `git diff > patch.diff` + `git apply`.
- NEVER `--no-verify` / `--no-gpg-sign` unless explicitly requested.
- NEVER downgrade a model without user permission.
- NEVER revert mathematical content to fix a build error (FM35 constitutional). Build errors are LaTeX; mathematics is never at fault.
- Before every Edit touching an r-matrix / κ / bar complex / label / Vol III κ / cross-volume formula / scope quantifier / differential form: fill the relevant PE-1..PE-12 pre-edit verification template as a fenced block in your reply, end with `verdict: ACCEPT`, THEN invoke Edit. See CLAUDE.md §Pre-Edit Verification Protocol.
- The "arity" ban (AP176) is CONSTITUTIONAL. `grep -rn '\barity\b' chapters/ appendices/ standalone/` MUST return 0.
- **Manuscript metadata hygiene is CONSTITUTIONAL.** No AP\d+, HZ-\d+, /B\d+, wave-\d+, campaign, session dates, "inscription", "healed", "first edition", "earlier phrasing", "adversarial" labels, or `RECTIFICATION-FLAG` markers in typeset prose (outside `%` comments). Grep-gate on every commit.
- **Chriss-Ginzburg register is the standard.** If the user (or a self-audit) says "that's not how Chriss-Ginzburg would write" — they are right. Rewrite to state the mathematics directly, no throat-clearing, no "the structural reading of this chapter", no "four geometric inputs carry this identity" when you can just say the four things.

**Avoid shallow corrections (AP186).** A "term swap without mathematical content" is a red flag. If the hook warns AP186 and your edit is genuinely principled (e.g., fixing a define-before-use, reframing a physics-mnemonic proof as a heuristic remark, healing a broken cross-reference), explain briefly why it is not a shallow swap. If you are not sure, STOP and investigate from first principles before editing.

**Small chunk size.** The user has been burned by agents that read 500 lines at a time and declare a chapter converged without touching anything. ~50 lines per chunk. Five-gate verdict per chunk. Iterate on failures. Advance only when all five gates pass at severity ≥ MODERATE.

When you finish a file: mark the queue entry `[x]`, append a completion log line with the date and key fixes, commit (`git add <file> <queue> <cache> <CLAUDE.md>; git commit -m "CG-rectify: <filename> — <one-line summary>"`; NO co-authored-by), push, then pick the next `[ ]`. One file per session unless the user asks you to chain.

Start now by: `pwd && cat CLAUDE.md | head -100` to confirm the volume, then read the queue file, then pick the next entry.

=== END ===
```

## Bookkeeping

- This file lives at `notes/cg_rectify_interactive_resume.md` in all three volume repos. The prompt text itself is identical; the queue-file path resolves from the detected volume.
- The cron architecture (`cg_rectify_kickstart.md`) and the interactive architecture (this file) are independent and can coexist. A cron tick picks up where interactive work leaves off and vice versa, because both update the same queue file.
- When the user wants to resume after a compaction or new session, they paste the prompt above. No other setup is needed.

## Authorship

All commits authored by Raeez Lorgat. No AI attribution. No emoji in commit messages. No `Co-Authored-By:`.
