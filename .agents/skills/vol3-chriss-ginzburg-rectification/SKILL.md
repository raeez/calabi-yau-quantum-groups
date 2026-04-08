---
name: vol3-chriss-ginzburg-rectification
description: Use when a whole chapter or substantial section of the Calabi-Yau Quantum Groups manuscript needs architectural fortification, platonic restructuring, prose hardening, define-before-use repair, or chapter-level convergence at the Chriss-Ginzburg standard. Trigger on Chriss-Ginzburg, chapter fortification, platonic rewrite, restructure this chapter, make the architecture inevitable, or full chapter rectification.
---

# Vol III Chriss-Ginzburg Rectification

Read `AGENTS.md` first. Pair this skill with `vol3-beilinson-loop`: Beilinson keeps the mathematics honest; Chriss-Ginzburg makes the chapter architecture match the mathematics.

Use this skill for chapter-scale work, not for a one-line typo or a single local lemma.

## The standard

The goal is not "nicer prose." The goal is a chapter whose textual architecture mirrors the mathematical architecture:

- every section answers a specific question;
- every definition arrives exactly when the reader needs it;
- every theorem resolves a tension that has been built up honestly;
- every transition is itself mathematical content, not narration;
- no object is used before it is defined;
- no rhetorical polish is allowed to hide a gap, conjecture, or status boundary.

The reader should feel inevitability, not authorial staging.

## Phase 1: Global diagnostic

Read the whole chapter before editing. Diagnose briefly:

1. What is the chapter's single organizing question?
2. What is the climax theorem or construction?
3. What does each section establish, and what forces the next one?
4. Where does the thread break?
5. Which definitions arrive cold, before the reader has a reason to want them?
6. Where are define-before-use violations?
7. Does the opening start with mathematics, or with summary/roadmap prose?
8. Does the closing crystallize the answer, or merely stop?
9. Which results are compute-backed, and which are only asserted?

Keep this diagnostic short. It is a map, not a mini-essay.

## Phase 2: Platonic architecture

Before line-editing, get the skeleton right.

Decide:

- the exact organizing question;
- the exact climax;
- the ideal section order;
- what should be merged;
- what should be split;
- what should be moved elsewhere;
- what is genuinely redundant;
- what definitions/examples/bridges are missing;
- where the honest scope of each major claim actually ends.

Then execute structural edits:

- reorder sections when logic demands it;
- move motivation before abstraction;
- move definitions before first real use;
- cut roadmap and throat-clearing prose;
- add short structural stubs if a missing bridge is load-bearing;
- rewrite openings that begin with summary dumps;
- rewrite closings so the answered question is explicit.

Do not spend time polishing sections that should be moved or deleted.

## Phase 3: Linear fortification loop

After the skeleton converges, work sequentially through the chapter in manageable chunks.

For each chunk:

1. Re-read it in context of what now precedes it.
2. Run the Beilinson audit on the mathematics.
3. Fortify the exposition:
   - every paragraph must earn its place;
   - transitions must say why the next step is forced;
   - definitions must answer a live question;
   - examples should precede general machinery whenever that strengthens inevitability;
   - duplicated motivation must be collapsed.
4. Remove prose sludge:
   - no "notably", "crucially", "remarkably", "it is worth noting", "we now turn to", "having established", "with this in hand", or similar scaffolding;
   - no patronizing roadmap paragraphs;
   - no self-congratulatory tone;
   - no vague "intuition" paragraphs that fail to cash out mathematically.
5. Re-audit the edited chunk for both truth and structure.

Do not advance until the chunk is locally coherent.

## Prose constraints

- Treat the reader as an equal.
- Prefer direct mathematical statements to commentary about the mathematics.
- Use short, load-bearing transitions.
- A sentence that can be a clause should become a clause.
- A full page is allowed when the mathematics needs it.
- Economy is not brevity; it is absence of waste.

## Hard guardrails

- Never use style to smuggle in an unproved claim.
- Never "clarify" by making a statement stronger than the proof.
- Never let a beautiful narrative outrun a weak construction.
- If a chapter needs a weaker true theorem, weaken it.
- If a central object is still aspirational, say so and define the available substitute precisely.

## Verification

- Build after structural edits.
- For load-bearing rewrites, run the narrowest relevant `pytest` slice and/or `make fast`.
- Propagate status/formula/definition changes across the repo when they are advertised elsewhere.

## Exit rule

End only at:

- `CONVERGED`: the chapter's structure and local mathematics are coherent, and the relevant verification passes.
- `BLOCKED`: exact blocker named.

If the chapter still feels like commentary wrapped around mathematics rather than mathematics speaking directly, it is not converged.
