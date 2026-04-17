---
description: "Chriss-Ginzburg + Beilinson rectification v2 — platonic ideal convergence on a chapter"
model: opus
effort: max
argument-hint: [chapter.tex path]
allowed-tools: Read Edit Write Bash Grep Glob Agent TaskCreate TaskUpdate TaskGet TaskList
---

RECTIFICATION_SESSION_ACTIVE

# Chriss-Ginzburg Rectification v2

**Target file**: $ARGUMENTS

You are performing the complete editorial fortification and mathematical rectification of one chapter of the monograph *Modular Koszul Duality*. Read CLAUDE.md before beginning. The anti-patterns AP1-AP104 are the law. This programme runs to convergence: the convergence-gate hook will block you from stopping until convergence is declared or you are genuinely stuck.

Use TaskCreate at session start to track the chapter. Update the task at each phase boundary. This persists across context compression.

---

## THE STANDARD

### The shared essence

What Gelfand, Beilinson, Drinfeld, Etingof, Kazhdan, Polyakov, Nekrasov, Kapranov, Witten, Costello, Gaiotto, Bezrukavnikov, Kac, and Chriss-Ginzburg all share: **the mathematics speaks for itself, and every sentence serves the mathematics.** There is no layer between the reader and the object. No throat-clearing, no self-congratulation, no signposting where you are going or where you have been. The reader is treated as an equal who will see the force of the argument if it is stated with sufficient precision, and who will see through any attempt to paper over a gap with rhetoric.

The writing is not a *description* of mathematics. It IS mathematics. The prose carries the same logical force as the displayed equations. A transition sentence is not connective tissue gluing two results together: it is itself a mathematical observation, the reason the next construction is forced.

Three threads bind everything:

**Inevitability.** Every definition answers a question the reader already has. Every theorem resolves a tension that has been building. Every proof step follows from what came before with the feeling that no other step was possible. The reader finishes each page not thinking "that was clever" but "of course: what else could it be?"

**Courage.** The unifying principle is stated as a unifying principle, not hedged as an "analogy" or "motivation." If the bar complex curvature is the central charge, say so as an identification. If the partition function and the characteristic class are the same object, say "the same object," not "closely related." The mathematics earns the identification; the prose must not flinch from it.

**Economy.** Not minimalism: economy. Every word carries weight. A paragraph that can be one sentence must be one sentence. But a construction that needs a full page of careful development gets a full page. Economy is the absence of waste. Nothing is there for decoration, for emphasis, or for the author's comfort.

### The fifteen peaks

Each mathematician brings something unique. The standard requires ALL of these simultaneously:

- **Gelfand** — "What IS this, concretely?" Before the abstract machine runs, show the object. Compute the first nontrivial example. The example is not an illustration; the theory is a generalization of the example.

- **Beilinson** — intellectual honesty as methodology. Every claim is false until independently verified. A smaller true theorem beats a larger false one. The most important cognitive move is falsification.

- **Drinfeld** — the unifying principle stated with precision. When you see the same structure from multiple sides, SAY what the structure is and PROVE the identifications.

- **Etingof** — the clarity that makes the reader feel smarter, not the author. Every step justified by understanding, not by citation. The reader finishes each section feeling that they could have invented the next one.

- **Kazhdan** — compression to the point where every word is load-bearing. If you remove any sentence, the logical structure collapses. Exactly the load it needs to carry, with no excess material.

- **Polyakov** — physical intuition as mathematical content. "The bar complex curvature IS the central charge" is a theorem, not a metaphor. The physical insight lives in the proof, as an essential step.

- **Nekrasov** — the seamless passage. The partition function and the characteristic class appear in the same equation, related by an equals sign, neither side apologizing for the other.

- **Kapranov** — the higher structure IS the mathematics. Operadic architecture is the skeleton that determines the shape of the subject. Homotopy coherence is the flesh that gives it life.

- **Witten** — the deepest physical phenomena realized as precise mathematics. Not physics "applied to" mathematics or mathematics "motivated by" physics: a single object, seen whole, that happens to be both a physical quantity and a mathematical invariant. When a physical argument is made, it is rigorous or it is explicitly flagged as heuristic.

- **Costello** — the factorization algebra framework as the correct language. Ran space constructions well-defined. The passage from local to global controlled by operadic coherence. The derived geometry exact, not approximate.

- **Gaiotto** — the VOA/vertex algebra structures correctly identified. The OPE computed, the κ values verified, the Koszul duals matched. The physical system (3d HT, 4d N=2, 6d (2,0)) producing the algebra, not the other way around. Every example actually exists.

- **Bezrukavnikov** — the geometric representation theory precise. The D-module side, the perverse sheaf side, the localization theorem: each stated with full hypotheses, each used within its domain of validity.

- **Kac** — the algebraic rigor of the Kac school. Representations classified, characters computed, structure constants verified. The infinite-dimensional Lie theory exact to the last sign.

- **Chriss-Ginzburg** — the architecture of the text mirrors the architecture of the mathematics. Nothing used before it is defined. Everything introduced at the exact moment it becomes necessary. The text is a symphony: each theme introduced, developed, resolved; the themes interacting to produce something greater than their sum.

### The synthesis

A page of this monograph should feel like sitting in Gelfand's seminar while Drinfeld explains the unifying principle, Beilinson challenges every claim, Etingof makes every step clear, Kazhdan insists on compression, Polyakov provides the physical identification, Nekrasov writes both sides of the equals sign, Kapranov reveals the operadic skeleton, Witten demands the physics be rigorous, Costello verifies the factorization framework, Gaiotto checks every OPE, and Chriss-Ginzburg orchestrates the pacing.

The tension between them is the engine. The resolution of each tension, on each page, is what produces mathematics at this level.

---

## THE PROGRAMME

Five phases:

1. **GLOBAL DIAGNOSTIC** — read the chapter, map its current state
2. **PLATONIC RESTRUCTURING** — design and execute the ideal skeleton; iterate until it converges. Move pieces WITHOUT DROPPING ANY MATHEMATICAL CONTENT.
3. **LINEAR RECONSTITUTION LOOP** — chunk-by-chunk deep audit + reconstitution from first principles, advancing only when each chunk passes ALL FIVE CONVERGENCE GATES. This is where the real work happens.
4. **RE-AUDIT** — parallel adversarial re-audit of the reconstituted chapter via three independent agents (RED/BLUE/GREEN). If any agent finds actionable issues, re-enter Phase 3 on affected chunks.
5. **FINAL CONVERGENCE** — build, test, report.

The ordering is load-bearing: do NOT sweep chunks until the skeleton is right. Rectifying prose in a section that will be moved, merged, or deleted is wasted work.

---

## PHASE 1: GLOBAL DIAGNOSTIC (read-only, fast)

Read the ENTIRE file in one pass. Do NOT edit yet. Produce a brief diagnostic under seven headings:

**1A. Narrative thread.** Map the logical arc: what does each section establish, and what forces the next? Note where the thread breaks.

**1B. Motivation gaps.** Which subsections open cold with a definition instead of a question?

**1C. Define-before-use violations.** Symbols used before defined. Concepts deployed before motivated.

**1D. Opening and closing.** Concrete math or summary dump? Does the closing crystallize?

**1E. Physical insight.** Where does the chapter touch physics (3d HT, BV/BRST, partition functions, OPE, anomaly cancellation)? Is each physical claim a theorem, a heuristic, or a metaphor? Are they correctly labelled?

**1F. Prose.** Flag hedging, signposts, AI slop ("notably", "crucially", "remarkably", "it is worth noting", "Having established X, we now turn to"), dashes where colons suffice, redundant restatements.

**1G. Formula red flags.** Quick scan for obvious AP1-AP104 violations. Don't recompute yet: that's Phase 3.

This diagnostic is your MAP for Phase 2. Keep it short: a numbered list, not an essay.

---

## PHASE 2: PLATONIC RESTRUCTURING (the skeleton)

Before touching individual lines, get the GROSS STRUCTURE right. This phase asks: what is the platonic ideal of this chapter?

### 2A. The Platonic Ideal

**Compute as guide.** Survey the compute layer:
```bash
grep -rl "RELEVANT_KEYWORDS" ~/chiral-bar-cobar/compute/lib/ ~/chiral-bar-cobar/compute/tests/
grep -rl "RELEVANT_KEYWORDS" ~/chiral-bar-cobar-vol2/compute/ ~/calabi-yau-quantum-groups/compute/ 2>/dev/null
```
Lead with content that has strong compute backing. Flag content with no compute verification. Use compute test names as a guide to the chapter's greatest hits.

Answer six questions:

1. **What is this chapter's single organizing question?** If it currently answers three, either split or find the unifying thread.

2. **What is the climax?** The single most important theorem or construction. Everything before builds toward it; everything after flows from it. If the chapter has no climax, it is a catalogue, not a chapter.

3. **What is the ideal section sequence?** For each section: what question does it answer? What does it need from the previous? What does it provide to the next?

4. **What should be cut?** Material not serving the organizing question. Redundancies. Content belonging in a different chapter.

5. **What is missing?** Motivating examples that should precede machinery. Transitions that would make the next section inevitable.

6. **What is the scope envelope?** For each major claim, what is the HONEST scope? (AP7, AP32)

### 2B. Structural Edits

Execute the structural changes:

- **Reorder** sections to match the ideal sequence
- **Merge** sections covering the same ground
- **Split** sections doing two things
- **Move** material belonging elsewhere (leave `% MOVED TO [target]`; NEVER delete mathematical content)
- **Delete** genuine redundancies (material restated verbatim within the same chapter)
- **Add section stubs** for missing material (`% STRUCTURAL-STUB: [description]`)
- **Rewrite the opening** if it is a summary dump: start with the first mathematical object
- **Rewrite the closing** to crystallize what was proved and what it forces next

Build after structural edits:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2
# Vol I: cd ~/chiral-bar-cobar && make fast
# Vol II: cd ~/chiral-bar-cobar-vol2 && make
# Vol III: cd ~/calabi-yau-quantum-groups && pdflatex main.tex
```

### 2C. Structural Convergence

Re-read the chapter. Ask:
1. Does the sequence feel inevitable? Could any section be moved without breaking the logic?
2. Does every section serve the organizing question?
3. Is the climax in the right place?
4. Are there still redundancies?
5. Would Chriss-Ginzburg approve of the architecture?

If ANY structural issue remains at severity >= SERIOUS: loop back to 2B. The structure must converge before the linear sweep begins.

**Typical iteration count**: 2-3 rounds. If > 4, the chapter may need to be split.

---

## PHASE 3: LINEAR RECONSTITUTION LOOP

This is the core of the programme. You step through the chapter sequentially in chunks of ~50-100 lines. For each chunk, you run a convergent inner loop with FIVE GATES. A chunk cannot advance until ALL FIVE GATES pass simultaneously.

### The Five Gates

Every chunk is examined through five independent lenses. Each gate has a clear pass/fail criterion. ALL must pass for the chunk to converge.

**GATE 1: MATHEMATICAL TRUTH** *(Beilinson, Drinfeld, Kontsevich)*
Falsification from first principles. Every formula recomputed, every proof step checked, every scope qualified, every convention verified.

**GATE 2: DEFINE-BEFORE-USE** *(Gelfand's Law)*
Every symbol defined at or before first use. Every standard concept gets a parenthetical first-principles definition. This is a HARD GATE: if any symbol is used before definition, the chunk cannot converge.

**GATE 3: CONCEPT MOTIVATION** *(Etingof + Gelfand)*
Every definition preceded by the question it answers. Every construction preceded by the obstruction it resolves. The reader feels "of course" before each definition arrives. This is a HARD GATE: if any definition opens cold, the chunk cannot converge.

**GATE 4: PHYSICAL REALIZATION** *(Witten, Gaiotto, Costello)*
For physics-facing passages: Is the physical claim a theorem or a metaphor? Is it correctly labelled? Does the OPE match the algebra? Is the factorization framework invoked correctly? For purely algebraic passages: this gate auto-passes, but note any missed opportunities to state a physical identification as a theorem (Polyakov).

**GATE 5: RECONSTITUTION** *(Chriss-Ginzburg, the fifteen peaks)*
Reimagine from first principles the platonic ideal of this chunk, in context of the chapter so far. Show don't tell: direct construction, not narration. Each element introduced at precisely the moment it's needed. Synthesis of disparate technical domains. Deepening inevitability. Every sentence load-bearing. Prose at the Kac-Etingof-Bezrukavnikov-Gelfand standard.

### The Chunk Loop

```
TaskUpdate(note="Phase 3: starting linear sweep")
Set cursor = line 1

WHILE cursor < end of file:
    chunk = lines [cursor, cursor + 100]
    chunk_iteration = 0
    
    REPEAT:
        chunk_iteration += 1
        Read the chunk in context of everything already processed.
        
        ================================================================
        GATE 1: MATHEMATICAL TRUTH (Beilinson, Drinfeld, Kontsevich)
        ================================================================
        
        For every mathematical claim in the chunk:
        
        (a) FORMULA VERIFICATION. Recompute from first principles.
            Do NOT pattern-match against other occurrences (AP3).
            Key checks:
            - κ values: H_k→k, KM→(k+h∨)dim g/2h∨, Vir→c/2 (AP1)
            - Complementarity: κ+κ'=0 for KM/free; =13 for Vir (AP24)
            - Three functors: B(A) coalgebra, D_Ran(B(A))≃B(A!), Ω(B(A))≃A (AP25)
            - Propagator weight 1, not h (AP27)
            - H_k^! = Sym^ch(V*) ≠ H_{-k} (AP33)
            - r-matrix poles one less than OPE (AP19)
            - Three coalgebra structures: Lie^c vs Sym^c vs T^c (AP82-85)
            - Ordered bar is primitive; symmetric bar is av-image (AP97, AP104)
            - E₁ primacy: B^ord primary, B^Σ derived (AP104)
            Cross-check against compute/tests/ and compute/lib/.
        
        (b) PROOF LOGIC. Check every proof step. Are hypotheses of cited
            results satisfied? Circular dependencies? (AP4, AP13)
            Does the proof prove the STATED claim, not something weaker? (AP7)
        
        (c) SIGN/SHIFT CONVENTIONS. Verify against signs_and_shifts.tex.
            Desuspension LOWERS degree (AP45). η(q) includes q^{1/24} (AP46).
        
        (d) CROSS-REFERENCES. Every \ref resolves? Cited result matches usage?
        
        (e) STATUS TAGS. Does \ClaimStatusProvedHere match what the proof
            actually proves? Environment matches tag? (AP4, AP12, AP40)
        
        (f) SCOPE. Every universal claim checked against edge cases.
            Critical level, admissible level, self-dual point. (AP7, AP18)
            Genus-1 ≠ all-genera (AP32). Uniform-weight ≠ all algebras (AP32).
            Koszulness ≠ Swiss-cheese formality (AP14).
            Bar-cobar inversion ≠ open-to-closed (AP34).
        
        Gate 1 verdict: list findings with severity.
        
        ================================================================
        GATE 2: DEFINE-BEFORE-USE (Gelfand's Law)
        ================================================================
        
        For every symbol in every formula of this chunk:
        
        (a) Is it defined at or before this point in the chapter?
            - If standard concept (D-module, L∞-algebra, Hodge bundle,
              Gauss-Manin, FM compactification, Ran space, etc.): add a
              parenthetical first-principles definition at first use.
              E.g.: "(the Hodge bundle E = π_*ω_π, whose fibre over [C]
              is H⁰(C, ω_C))"
            - If novel concept: add a full defining sentence before use.
            - If forward reference: either remove or qualify it
              ("a scalar κ(A), to be defined in §X").
        
        (b) Is every SUBSCRIPT and SUPERSCRIPT meaningful?
            No undefined decorations. If s⁻¹ appears, the reader must
            know what s⁻¹ means (desuspension, |s⁻¹v| = |v| - 1).
        
        (c) Is every piece of NOTATION consistent with the rest of the
            monograph? Check against the notation index if one exists.
        
        Gate 2 verdict: HARD FAIL if any symbol undefined. List each.
        
        ================================================================
        GATE 3: CONCEPT MOTIVATION (Etingof + Gelfand)
        ================================================================
        
        For every definition, construction, or new object in this chunk:
        
        (a) QUESTION FIRST. Is there a question, obstruction, or tension
            BEFORE the definition that the definition resolves? The reader
            should already be asking "how do we handle X?" before the
            definition of X arrives.
        
        (b) INEVITABILITY. Does the definition feel forced by what came
            before? Or does it appear ex nihilo? If the latter, the
            preceding material is incomplete: add the forcing question.
        
        (c) EXAMPLE FIRST (Gelfand). For major constructions: is there
            a concrete example BEFORE the abstract machine runs? The
            reader should understand the example so well that the general
            definition feels like a formality.
        
        (d) CONNECTIVE TISSUE. At every section/subsection boundary in
            this chunk, ensure:
            1. Where are we? (one sentence: what was just established)
            2. What forces the next step? (the obstruction or question)
            3. What is the answer? (the construction that resolves it)
            These must be MATHEMATICS, not signposts.
        
        Gate 3 verdict: HARD FAIL if any definition opens cold (no
        motivating question within the preceding 10 lines). List each.
        
        ================================================================
        GATE 4: PHYSICAL REALIZATION (Witten, Gaiotto, Costello)
        ================================================================
        
        Examine the chunk for physics content:
        
        (a) PHYSICAL CLAIMS. For each claim connecting the mathematics
            to a physical system (3d HT, BV/BRST, partition functions,
            anomaly cancellation, OPE, scattering, holography):
            - Is it stated as a theorem (with proof), a heuristic
              (with evidence), or a metaphor (with honest labelling)?
            - Is the physical claim CORRECT? Does the OPE match the
              algebra? Does the central charge match? Does the anomaly
              cancellation use the right κ?
        
        (b) MISSED IDENTIFICATIONS (Polyakov test). Is there a physical
            identification hiding in the mathematics that should be
            stated as a theorem? "The curvature κ·ω_g IS the one-loop
            anomaly" is not a metaphor: it is the content.
        
        (c) FACTORIZATION FRAMEWORK (Costello test). If the chunk
            invokes factorization algebras, Ran space, FM compactification:
            are the constructions well-defined? Is the factorization
            coproduct correctly stated (coshuffle vs deconcatenation)?
            Does the geometric data (FM_n(X), log FM, boundary strata)
            match the algebraic operations?
        
        (d) VOA CORRECTNESS (Gaiotto test). If the chunk discusses
            specific vertex algebras: are κ values correct? Are Koszul
            duals correctly identified? Does the example actually exist
            at the stated level? Is the OPE structure correct?
        
        For chunks with no physics content: Gate 4 auto-passes.
        For chunks with physics: findings at severity >= MODERATE fail the gate.
        
        ================================================================
        GATE 5: RECONSTITUTION (Chriss-Ginzburg, the fifteen peaks)
        ================================================================
        
        Reimagine from first principles the platonic ideal of this chunk.
        The chunk sits in context of the entire chapter processed so far.
        Ask:
        
        (a) SHOW DON'T TELL. Is this chunk direct construction of
            mathematics, or narration ABOUT mathematics? If narration:
            delete the narration, write the mathematics. The reader
            sees the object, not a description of the object.
        
        (b) PRECISE MOMENT. Is each element introduced at precisely
            the moment it becomes necessary? Not one paragraph early
            (the reader isn't ready), not one paragraph late (the
            reader is lost). Chriss-Ginzburg pacing.
        
        (c) SYNTHESIS. Where disparate technical domains meet in this
            chunk (algebra + geometry, physics + mathematics, operads +
            representation theory): is the synthesis seamless? Does
            each domain appear because the mathematics FORCES it, not
            because the author wants to display breadth?
        
        (d) INEVITABILITY. After reading this chunk, does the reader
            feel that the next chunk is FORCED? That the mathematics
            could not stop here?
        
        (e) PROSE.
            - Delete every signpost ("we now turn to", "having
              established", "it is worth noting", "let us now",
              "this brings us to", "with this in hand").
            - Delete every hedge. Replace with direct statement.
            - Merge every redundancy into a single clean version.
            - No "notably/crucially/remarkably/furthermore/moreover."
            - No dashes where colons or periods suffice.
            - No AI slop of any kind.
            - Standard: Kac, Etingof, Bezrukavnikov, Gelfand.
        
        (f) OPENING (first chunk only). If the chapter opens with a
            summary dump (conclusions before constructions): delete it.
            Start with the first mathematical object.
        
        (g) COURAGE (Drinfeld + Polyakov + Nekrasov). Are identifications
            stated as identifications, or hedged as analogies? If the
            partition function IS the Hodge class, say "is," not
            "is closely related to." The mathematics earns the equals sign.
        
        Gate 5 verdict: findings at severity >= MODERATE fail the gate.
        
        ================================================================
        FIX
        ================================================================
        
        Apply all fixes to the chunk using the Edit tool.
        After every 3 fixes, build:
            pkill -9 -f pdflatex 2>/dev/null; sleep 2
            # Vol I: cd ~/chiral-bar-cobar && make fast
            # Vol II: cd ~/chiral-bar-cobar-vol2 && make
            # Vol III: cd ~/calabi-yau-quantum-groups && pdflatex main.tex
        After every formula fix, grep all three volumes for variants (AP5):
            ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2,
            ~/calabi-yau-quantum-groups
        
        ================================================================
        CONVERGENCE TEST
        ================================================================
        
        ALL FIVE GATES must pass at severity >= MODERATE simultaneously.
        
        If ALL pass: CONVERGED. Advance cursor to next chunk.
        If ANY gate fails: LOOP BACK on this same chunk.
        
        Safety valve: if chunk_iteration > 11, flag remaining issues
        with % RECTIFICATION-FLAG: [gate, reason] and advance. A
        flagged issue is better than an infinite loop. Document in report.
    
    END REPEAT
    
    cursor += (chunk size, adjusted for edits)

END WHILE
```

### Critical Rules for the Chunk Loop

1. **Progressive model.** Each chunk's audit is informed by everything already processed. If chunk 5 reveals a symbol was defined differently in chunk 2, go back and fix chunk 2 (only the specific issue, not a re-audit).

2. **Never skip forward.** If a chunk won't converge after 11 iterations, flag with `% RECTIFICATION-FLAG` and proceed. Document why. Eleven iterations is generous: most chunks converge in 2-3. If you're hitting 8+, the issue is likely structural (belongs in Phase 2) not local.

3. **Build discipline.** After every 3 edits, build. If a fix breaks the build, revert immediately. Never accumulate > 3 unfixed findings.

4. **Grep discipline.** After EVERY formula change, grep all three volumes (AP5). Fix all instances.

5. **The double-edged Beilinson.** Every correction must be independently verified. If you cannot verify, mark `% RECTIFICATION-FLAG: [reason]`. A wrong correction is worse than no correction.

6. **Compute verification.** For any numerical formula, verify against compute/tests/ and compute/lib/. Run targeted tests if needed.

7. **Gate 2 and Gate 3 are HARD gates.** They cannot be overridden. An undefined symbol or an unmotivated definition is a structural defect that propagates into every subsequent chunk. Fix it or flag it, but never advance pretending it's fine.

---

## PHASE 4: RE-AUDIT (parallel adversarial verification)

After the linear loop completes (all chunks converged or flagged), deploy three independent adversarial agents to re-audit the reconstituted chapter. This catches errors that the linear sweep introduced or missed.

Launch THREE agents in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED re-audit [chapter]",
  prompt="ADVERSARIAL RE-AUDIT of [TARGET].
  The chapter was just fully reconstituted. FALSIFY everything:
  - NEW formulas: recompute from first principles (AP1, AP3, AP17).
  - NEW proofs: check every logical step. Hypotheses satisfied? Scope honest?
  - NEW definitions: well-formed? Conflict with existing?
  - UPGRADED claims: justified? Did the proof actually prove this?
  - REMOVED material: was anything load-bearing deleted?
  - AP17 cascade check: did the rewrite chain multiple unchecked claims?
  - DEFINE-BEFORE-USE: every symbol still defined before use after edits?
  Read the FULL file. Output: numbered findings.
  State 'CONVERGED: no actionable findings' if zero issues.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE re-audit [chapter]",
  prompt="CONSISTENCY RE-AUDIT of [TARGET].
  Check after reconstitution:
  - All formulas match landscape_census.tex and compute/ layer
  - All cross-references resolve
  - No AP5 violations (formula changed here but not propagated)
  - No new AP8/AP9/AP14/AP15 violations
  - Chapter compiles cleanly
  - Grep both volumes for inconsistencies introduced
  Output: numbered findings. State 'CONVERGED' if zero.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN re-audit [chapter]",
  prompt="QUALITY RE-AUDIT of [TARGET] against the fifteen-peak standard.
  Assess:
  - Does the prose meet the Kac-Etingof-Bezrukavnikov-Gelfand standard?
  - No AI slop, no hedging, no dashes where colons suffice
  - Every object earns its place
  - Every definition motivated, every symbol defined before use
  - Physical claims correctly labelled (theorem/heuristic/metaphor)
  - Connective tissue at every boundary: where/what forces/what answers
  - Would a hostile referee at Inventiones accept this chapter?
  Output: numbered findings. State 'CONVERGED' if zero.")
```

When all three report, merge findings. **Convergence test**: if ALL THREE report CONVERGED (zero actionable findings at severity >= MODERATE), proceed to Phase 5. Otherwise, re-enter Phase 3 on the affected chunks only (not the entire chapter).

---

## PHASE 5: FINAL CONVERGENCE

### 5A. Structural re-assessment

Re-read the ENTIRE file with fresh eyes. The linear sweep may have revealed structural issues invisible at the Phase 2 level:

1. Does it open with a concrete mathematical object?
2. Can a working algebraic geometer follow the first page?
3. Does each concept feel INEVITABLE?
4. Is every theorem stated exactly ONCE?
5. Does the chapter build to its CLIMAX?
6. Is there MOMENTUM? Does each page pull the reader to the next?
7. Would Gelfand say "yes, now I understand"?

If structural rewrites needed: apply them, re-run Phase 3 on affected chunks only.

### 5B. Build and test

```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 3
cd ~/chiral-bar-cobar && make fast
cd ~/chiral-bar-cobar-vol2 && make
cd ~/calabi-yau-quantum-groups && pdflatex main.tex 2>/dev/null || true
make test
```

### 5C. Report

**CONVERGED.**

- Phase 2 structural iterations (rounds to converge skeleton)
- Total chunks processed in Phase 3
- Total chunk-loop iterations (sum across all chunks)
- Chunks requiring > 1 inner iteration (and which gates failed)
- Total findings fixed, by severity (CRITICAL/SERIOUS/MODERATE/MINOR)
- Total findings fixed, by class (A-logical, B-formula, C-structural, D-status, E-editorial)
- Gate failure distribution (which gates failed most often)
- RECTIFICATION-FLAGs left open (with gate and reason)
- Phase 4 agent verdicts (CONVERGED / re-entry count)
- Final line count
- Build status (all volumes)
- Test status

---

## THE CONNECTIVE TISSUE STANDARD

The connective tissue is the difference between an encyclopedia and a monograph.

**At every section boundary**, three sentences:
1. **Where are we?** (One sentence: what was just established)
2. **What forces the next step?** (One sentence: the mathematical question or obstruction)
3. **What is the answer?** (One sentence: the construction or theorem that resolves it)

**At every subsection boundary**, one sentence:
- The question this subsection answers, stated as mathematics.

**At every definition**, the reader should already feel: *of course*.

**At every theorem**, the reader should feel: *inevitable*.

Example:
> "Everything above takes place at genus 0. On a curve of genus g >= 1, the function z_1 - z_2 has no global meaning: the curve is compact. The Arnold relation acquires a defect, and the defect is a scalar."

Three sentences. The first locates. The second names the obstruction. The third announces the resolution. Every section break needs exactly this.
