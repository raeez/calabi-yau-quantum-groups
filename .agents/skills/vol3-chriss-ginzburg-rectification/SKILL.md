---
name: vol3-chriss-ginzburg-rectification
description: Restructure a Volume III chapter or substantial section when the user requests architectural or exposition repair. Do not use for local typos or routine single-lemma corrections.
---

# Volume III structural rectification

Read the root contract, its research reference, the full target, and directly relevant dependencies.
Locate claims in `metadata/theorem_registry.md`, then verify against current TeX.
For construction scope use `chapters/theory/cy_to_chiral.tex`. This repository has no chapter concordance file.

Identify the organizing question, central theorem or construction, and dependency order.
Determine which sections establish each prerequisite and where definitions, examples, or proof support are missing.
Make the architecture follow those dependencies. Move concrete computations earlier when they motivate the abstraction.
Reorder, merge, or split sections only where the mathematical argument requires it. Preserve substantive content.
Use decomposition tables, explicit alternatives, and direct mathematical transitions when they clarify the proof.
Rewrite an opening or closing when it obscures the actual question or conclusion.
Keep definitions before use and use examples to motivate general machinery.

Inspect each changed portion in its new context. Check signs, hypotheses, scope, computation, and proof completeness.
Use `vol3-beilinson-loop` for a substantial proof audit when needed, without duplicating its checks.
Remove roadmap prose, decorative transitions, vague intuition, and self-congratulation.
Use literal mathematical statements. Do not let prose imply a stronger result than the proof establishes.
Repair the statement, proof, or construction without quietly weakening the requested theorem target.
Identify a genuinely unavailable construction and the exact remaining obligation.

After coherent structural edits, build the applicable manuscript entry point in the assigned worktree.
Run relevant independent computations where the changed claim has an executable witness.
Check affected references and advertisements elsewhere in the assigned scope. Return unassigned propagation paths to their owner.

Completion means the requested structure is coherent, mathematical claims have their stated evidence, and applicable checks pass.
Repeat review only when a change or unresolved concern warrants it. Fixed pass counts are not required.
A bounded investigation may return an exact unresolved obligation, attempted routes, evidence, and next step.
That handoff does not claim completion of the theorem or chapter repair.
