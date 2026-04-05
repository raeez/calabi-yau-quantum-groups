# Quality Audit: Calabi-Yau Quantum Groups (Volume III)

**Auditor standard**: Chriss-Ginzburg, Kac, Etingof lecture notes, Beilinson-Drinfeld.
**Date**: 2026-04-02
**Scope**: All 22 chapter files (chapters/theory/, examples/, connections/), working_notes.tex, and 22 detailed notes files (notes/).

---

## EXECUTIVE SUMMARY

The project has two faces that are drastically different in quality:

1. **The chapter files** (905 total lines across 22 files) are **skeletal stubs**. Of 93 declared sections, approximately 60 contain nothing beyond a `\section{}` header and `\label{}`. Zero `\begin{proof}` environments. Zero `\ClaimStatus` annotations. The four "Main Theorems" (CY-A through CY-D) are *stated* but not proved in the chapter files. No chapter would survive a referee report, let alone Inventiones.

2. **The notes files** (~20,000 lines across 22 files) contain the actual mathematical substance: 148 theorems/propositions/lemmas, 63 proofs, 42 conjectures, 51 claim-status annotations, and 13 warning environments. Several of these (theory_cy_to_chiral_construction.tex, theory_automorphic_shadow.tex, theory_e2_chiral_formalism.tex, theory_coha_e1_sector.tex) are serious mathematical documents that could, with work, become publishable sections. The **computational foundation** (827 passing tests across 11 modules) is solid.

The distance between the two is the central problem. The book has a skeleton and it has organs, but they are not yet in the same body.

**Overall verdict**: The programme is genuine and mathematically serious. The central insight (automorphic correction = shadow obstruction tower, denominator identity = bar Euler product) is compelling and computationally verified. But the monograph as written is an extended abstract, not a text. Approximately 15-20% of the programme is proved, 40-50% is a rigorous proof sketch that could be completed, and 30-40% is conjectural or aspirational.

---

## I. DOES EVERY OBJECT EARN ITS PLACE?

### Objects that earn their place

1. **The generalized root datum** (Definition in notes/theory_generalized_root_datum.tex): Axioms CY1-CY7 are precisely motivated by the K3xE and toric CY3 examples. Every axiom has a specific geometric origin. This definition solves the problem of unifying BKM superalgebras, affine Yangians, and CoHAs under a single framework. **Verdict: earned.**

2. **The E2-chiral algebra** (Definition in notes/theory_e2_chiral_formalism.tex, lines 222-274): The formal definition via factorization on Ran(X) x Ran(Y) with the FM operad compatibility is careful, precise, and necessary. It solves the problem of having a chiral-algebraic home for braided monoidal structures. The five-part definition is tight. **Verdict: earned.**

3. **The Lie conformal algebra L_C** (Construction in notes/theory_cy_to_chiral_construction.tex, lines 241-273): This packages the Gerstenhaber bracket and CY pairing into a single datum. The lambda-bracket formula (eq. lambda-bracket) is explicit and the verification is complete. **Verdict: earned, and this is genuinely new packaging of known structures.**

4. **The critical CoHA** (notes/theory_coha_e1_sector.tex): The identification CoHA = E1-sector of G(X) is well-motivated, the Schiffmann-Vasserot and RSYZ results are correctly cited, and the operadic layer (E1 to E2 via Drinfeld double) is clearly explained. **Verdict: earned.**

### Objects that do NOT earn their place

1. **"Quantum vertex chiral group" G(X)**: This is the central object of the monograph and it is NEVER DEFINED. The closest thing to a definition is the assemblage at the end of k3_times_e.tex (lines 142-150), which is a list of properties, not a definition. The notes/theory_qvcg_koszul.tex begins by *using* G(X) without defining it. A reader looking for "Definition: quantum vertex chiral group" will find nothing.

   **This is a fatal gap.** Chriss-Ginzburg defines the Steinberg variety before studying it. Kac defines the Kac-Moody algebra before proving the character formula. The central object of this volume exists as a slogan, not as mathematics.

   **Recommendation**: Write a precise definition. Is G(X) the BKM superalgebra g_X? The chiral algebra A_X? The pair (A_X, g_X)? The E2-chiral algebra Phi(C)? The braided monoidal category Rep^{E2}(A_X)? These are all different objects. Pick one and define it.

2. **The "quantum chiral algebra"** (chapters/theory/quantum_chiral_algebras.tex, line 7): "A quantum chiral algebra is a chiral algebra A equipped with an E2-enhancement such that the representation category Rep^{E2}(A) is a braided monoidal category equivalent to a quantum group representation category." This is a *description*, not a definition. The phrase "equivalent to a quantum group representation category" is not a mathematical condition -- it is a prayer. Which quantum group? In what sense equivalent? This is definition-by-aspiration.

   **Recommendation**: Either define "quantum chiral algebra" as "E2-chiral algebra" (dropping the quantum group equivalence from the definition and making it a theorem/conjecture), or specify the precise structure that makes it "quantum."

3. **Chapters that are pure section headers**: The following chapters contain ZERO mathematical content beyond section titles:
   - en_factorization.tex (14 lines, 4 empty sections)
   - quantum_groups_foundations.tex (14 lines, 4 empty sections)
   - modular_koszul_bridge.tex (11 lines, 3 empty sections)
   - geometric_langlands.tex (14 lines, 4 empty sections)

   These do not earn their place. They are promises, not chapters.

---

## II. DOES EVERY PARAGRAPH FORCE THE NEXT?

### Where the logic flows

The introduction (chapters/theory/introduction.tex) is well-structured. The progression: question -> E1/E2 hierarchy -> relation to Vols I-II -> CY3 root data -> automorphic/shadow identification -> main results -> guide -- this is a competent roadmap.

The notes/theory_cy_to_chiral_construction.tex has the best logical flow of any document in the project. The four-step construction (cyclic A-inf -> Lie conformal -> factorization envelope -> E2 enhancement -> quantization) is laid out with each step depending explicitly on the output of the previous one. Claim statuses are marked. The transitions between steps are explicit.

### Where the logic breaks

1. **The d=2 vs d=3 gap in CY-A**: Theorem CY-A in cy_to_chiral.tex (line 21) claims the functor Phi works for "CY categories of dimension d=2." But the introduction (line 110) claims Phi works for all d, and for d=3 it "produces a quantum vertex chiral group." The notes (theory_cy_to_chiral_construction.tex, Section "Step 3") are honest: for d=2 the E2-enhancement is proved; for d=3, the S^3-framing gives E3, and one restricts to E2 -- but Warning warn:cy3-symmetric (line 495-498 of the notes) acknowledges this restriction LOSES the non-trivial braiding at the topological level, and the quantum corrections come from "higher homotopy data" that is not constructed.

   **The chapter file HIDES this gap. The notes file REVEALS it.** This is the most serious scope-honesty failure in the text.

   **Recommendation**: The chapter theorem statement must restrict to d=2 and explicitly state that d=3 is conditional on constructing the S^3-framing at the chain level (which the notes flag as open, Question 2 in working_notes.tex).

2. **The gap between factorization envelope and quantization**: Step 2 (factorization envelope) produces a *classical* factorization algebra (Proposition prop:fact-properties part (iv) in the notes). Step 4 (quantization) should deform it to a quantum chiral algebra. But Step 4 is essentially empty in both the chapter file and the notes. The notes say:

   > "The quantum chiral algebra A_C is the quantization of Fact_X(L_C) determined by the CY trace."

   This is a single sentence claiming to solve the hardest part of the problem. What quantization procedure? Deformation quantization a la Kontsevich? BV quantization? The CY trace determines a Maurer-Cartan element -- in which dgla? This is where the bridge from classical to quantum should be built, and it is a load-bearing beam that is missing.

3. **Theorem CY-C (quantum_group_reps.tex, line 10-13)**: "For a simple Lie algebra g and generic q, the braided monoidal category Rep_q(g) arises as Rep^{E2}(A_C) for a CY category C = C(g,q)." What is C(g,q)? It is never defined. The KL equivalence (line 18-22) is at root of unity, not generic q. The claimed recovery of the Kac-Moody vertex algebra V_k(g) at level k from q = exp(pi i/(k+h^v)) confuses: at generic q this is irrational level, and the categories are semisimple. The interesting case (root of unity) is not developed.

   **This is enthusiasm bridging a logical gap.** The slogan "CY categories produce quantum groups" requires specifying WHICH CY category produces WHICH quantum group, with a proof or at least a precise conjecture.

4. **The Langlands conjecture (working_notes.tex, line 313-319)**: The claim G(C,G)^! = G(C, ^LG) is stated as a conjecture with "evidence" listed as: Feigin-Frenkel center, root/coroot exchange, SYZ, Kapustin-Witten. But none of these constitute evidence for THIS specific conjecture, because G(C,G) has not been defined. The evidence supports *some* relationship between Langlands and Koszul duality, but not this particular formulation.

---

## III. IS Theta_A THE SINGLE ORGANIZING THREAD?

### Assessment of coherence

The 22 chapter files were written as a unified outline -- they share notation, cross-reference consistently, and the Part structure (I through VI) tells a coherent story. The introduction and working notes maintain a clear master narrative: CY category -> cyclic A-inf -> Lie conformal -> factorization envelope -> E2 chiral -> quantum group, with Theta_A connecting the CY side to the bar-cobar machine of Vol I.

However, the 22 notes files were written independently and show it:

- **theory_cy_to_chiral_construction.tex**: Focuses on the functor Phi. Theta_A appears only at the very end.
- **theory_automorphic_shadow.tex**: This IS the Theta_A story. It is the heart of the programme.
- **theory_coha_e1_sector.tex**: The CoHA story. Theta_A does not appear.
- **theory_e2_chiral_formalism.tex**: The E2 formalism. Theta_A does not appear.
- **theory_kl_e2_chiral.tex**: Kazhdan-Lusztig in E2 framework. Theta_A is mentioned peripherally.
- **theory_qvcg_koszul.tex**: Koszul duality for QVCGs. Theta_A appears as a tool but not as the organizing principle.
- **The 10 physics notes**: Theta_A appears in none of them.

**Verdict**: Theta_A is the organizing thread in the introduction and in theory_automorphic_shadow.tex. It is NOT the organizing thread of the other 20 notes. The CoHA material, the KL material, the Hitchin material, and the physics material could all be rewritten to make the connection to Theta_A explicit, but currently they read as independent essays.

The **denominator identity = bar Euler product** is the strongest thread. It appears in the introduction, in theory_automorphic_shadow.tex, in theory_denominator_bar_euler.tex, and in k3_times_e.tex. If the monograph has a single organizing result, it is this one, not Theta_A per se.

**Recommendation**: Write a "red thread" paragraph at the beginning of each chapter file that explicitly states what that chapter contributes to the Theta_A story. Currently, only the introduction and the automorphic shadow note do this.

---

## IV. IS SCOPE HONEST AT EVERY CLAIM BOUNDARY?

### Claim status in chapter files

**There are ZERO ClaimStatus annotations in any chapter file.** This is a hard violation of the project's own conventions (main.tex defines five ClaimStatus commands). Every theorem in the chapter files -- CY-A, CY-B, CY-C, CY-D, plus the E1/E2 Koszul dualities, CY Hochschild duality, and Drinfeld center equivalence -- is stated without any indication of whether it is proved, conjectured, or heuristic.

This means a reader of the compiled monograph cannot tell what is proved and what is not. **This is unacceptable by any standard.**

### Claim status in notes files

Three notes files use ClaimStatus annotations: theory_cy_to_chiral_construction.tex (17 claims tagged), theory_e2_chiral_formalism.tex (24 tags), theory_generalized_root_datum.tex (10 tags). The remaining 19 notes files do not use them.

Where present, the annotations are honest:
- The Gerstenhaber structure on HH(C) is correctly tagged [PE] (proved elsewhere).
- The Lie conformal algebra L_C is correctly tagged [PH] (proved here).
- The E2 enhancement for d=2 is tagged [PH]; the d=3 case is correctly more guarded.
- The E2-chiral Koszul duality is correctly marked as a **conjecture** in e2_chiral_algebras.tex (line 59).

### Conjectures vs theorems: specific scope failures

1. **Theorem CY-B** (braided_factorization.tex, line 13): Stated as a theorem. In the notes (theory_denominator_bar_euler.tex), the title says "proof sketch" and the abstract says "rigorous sketch." The body uses "Proof sketch" headers repeatedly. A proof sketch is not a proof. **Should be labeled Theorem-Conjecture or the proof should be completed.**

2. **Theorem CY-C** (quantum_group_reps.tex, line 10): Stated as a theorem. No proof, no proof sketch, no reference. The CY category C(g,q) is undefined. **This is a conjecture at best, a programme at worst.**

3. **Theorem CY-D** (modular_trace.tex, line 9): Stated as a theorem. The identification kappa(A_C) = chi^CY(C) is computationally verified for K3xE and toric CY3 (notes and compute tests). But the general statement has no proof. **Should be Theorem (for specific cases) + Conjecture (in general).**

4. **Proposition prop:drinfeld-chiral-derived-center** (drinfeld_center.tex, line 15): Z(Rep^{E1}(A)) = Rep^{E2}(Z^der_ch(A)). This is stated as a proposition. It is a deep result that, in full generality, requires the machinery of Lurie's Higher Algebra plus substantial work on chiral derived centers. No proof or reference is given. **Should cite Ben-Zvi--Francis--Nadler or Lurie, or be marked as requiring further argument.**

### What IS proved

The following results have genuine proofs (in the notes, not in the chapters):

- The Lie conformal algebra L_C from a CY category (Construction + verification, ~50 lines of proof)
- Properties of the CY factorization envelope (Proposition, ~15 lines)
- E2 enhancement for d=2 (Theorem + proof sketch, ~40 lines)
- Arity-2 shadow = real root data (Proposition + proof, ~50 lines in theory_automorphic_shadow.tex)
- Denominator identity = bar Euler product at arity 2-6 for K3xE (computationally verified, 827 tests pass)

The following are honest proof sketches that could be completed:
- E2 enhancement for d=3 (restricted, with caveats about symmetry)
- Arity-r shadow captures depth <= r-2 roots (proof by induction sketch)
- CoHA as E1-sector for toric CY3 (following Schiffmann-Vasserot, RSYZ)

The following are conjectural or programmatic:
- E2-chiral Koszul duality (Conjecture 6.7 in e2_chiral_algebras.tex)
- Quantum group realization CY-C
- Langlands = Koszul duality
- Wall-crossing = MC gauge equivalence
- All 10 physics conjectures

---

## V. THE WORKING_NOTES.TEX STATUS TABLE

The status table lists everything as "Draft." Here is the real status:

### Proved or essentially proved (would survive a referee, given the notes)
| Component | Real status |
|-----------|------------|
| Generalized root datum axioms CY1-CY7 | **Solid definition**, proved adequate for K3xE and toric examples |
| E2-chiral algebra formalism | **Solid definition + basic properties proved** (notes have 1243 lines) |
| CY-to-chiral functor (d=2) | **Steps 1-3 proved**, Step 4 (quantization) sketched |
| CoHA = E1-sector | **Proved for toric CY3** via Schiffmann-Vasserot + RSYZ |
| Drinfeld = chiral center | **Proved elsewhere** (Ben-Zvi-Francis-Nadler, Lurie) |

### Rigorous proof sketch, completable with serious effort
| Component | Real status |
|-----------|------------|
| Automorphic = shadow obstruction tower | **Strong sketch** (1239 lines, parts (a)-(c) argued, part (d) computational) |
| Denominator = bar Euler product | **Proof sketch** (993 lines), relies on CY-A which is only done for d=2 |
| CY2 -> CY3 fibration | **Sketch** (961 lines), Borcherds lift machinery known |
| E2-chiral Koszul duality | **Conjecture** with evidence from E1 case |
| Higgs sheaves as CY2 QVCGs | **Sketch** (829 lines) |

### Conjectural
| Component | Real status |
|-----------|------------|
| CY-to-chiral functor (d=3) | **Conditional** on chain-level S^3-framing (flagged as open) |
| Quantum group realization CY-C | **Conjecture**, C(g,q) undefined |
| QVCG Koszul duality | **Conjecture** (Langlands connection) |
| KL in E2-chiral framework | **Conjecture** with evidence |

### Aspirational / wishful thinking
| Component | Real status |
|-----------|------------|
| All 10 physics notes | **Physics conjectures**, many beautifully formulated but none proved |
| Celestial holography / CY QG | **Speculative** (W_{1+inf} = G(C^3) identification is real, rest is programmatic) |
| 3d mirror symmetry / CY2 | **Speculative** |
| S-duality = Langlands = Koszul | **Triple identification is aspirational** |

### Summary arithmetic
- **Proved**: ~15-20% of the programme
- **Rigorous sketch**: ~30-35%
- **Conjectural with evidence**: ~20-25%
- **Aspirational**: ~20-30%

---

## VI. WOULD THE RUSSIAN ELITE FIND THIS SATISFACTORY?

### What Beilinson would say

"You have not defined your central object. You have an interesting dictionary between BKM algebras and bar complexes, supported by computation, but you present four theorems without proofs in your chapter files while hiding the actual mathematics in auxiliary notes. The chapter files are an extended abstract. Write a paper proving one theorem completely -- CY-A for d=2 -- and submit that. The rest belongs in a programme announcement."

### What Kac would say

"The K3xE chapter is the best part. The lattice theory is correct, the BKM construction follows Gritsenko-Nikulin faithfully, the denominator identity is the real thing. But you claim your bar-complex Euler product EQUALS Delta_5, and the proof is a sketch that assumes the existence of the CY-to-chiral functor which you have not constructed for d=3. Your argument is circular: CY-A requires constructing Phi for CY3; the automorphic shadow identification requires CY-A for CY3; but CY-A is only done for CY2. The K3xE example is CY3."

### What Etingof would say

"The quantum groups chapter (quantum_groups_foundations.tex) is 14 lines of section headers. This is not a chapter. You cite Kazhdan-Lusztig at generic q and at root of unity in the same paragraph without distinguishing them. Your Theorem CY-C conflates Rep_q(g) at generic q (semisimple, uninteresting) with Rep_q(g) at root of unity (the KL story). I cannot tell whether you are claiming a new proof of Kazhdan-Lusztig, a generalization of it, or merely an analogy to it."

### What Bezrukavnikov would say

"The Drinfeld center proposition (drinfeld_center.tex line 15) is a deep result -- essentially the center of an E1-monoidal category is E2. You state it without proof or reference. In the derived setting, this requires significant machinery. You should either cite Ben-Zvi-Francis-Nadler or prove it. More importantly, the 'CY enhancement of the Drinfeld center' (Section 12.3) is an empty section. What IS the CY enhancement? This is presumably where the interesting new mathematics lives, and it is blank."

### What Gelfand would say

"Too many definitions, not enough examples. Your K3xE and C^3 examples are good. Where are the others? What does your functor Phi produce for the quintic? For an Enriques surface? For a non-toric CY3 with compact 4-cycles? You acknowledge these as open questions but then you don't work any examples that are not already in the literature. The value of a construction is demonstrated by computing with it."

---

## VII. CHAPTER-BY-CHAPTER RECOMMENDATIONS

### Part I: CY Categories and Cyclic Structures

**introduction.tex** (119 lines): The best chapter file. Clear, well-structured, honest about the programme. **Recommendation**: Add ClaimStatus tags to the four main theorem statements.

**cy_categories.tex** (65 lines): Definitions are standard and correct. The CY trace definition (def:cy-trace) correctly requires HC^- lifting. Examples are appropriate but minimal. **Recommendation**: Merge with cyclic_ainf.tex into a single chapter. Add the HKR decomposition from the notes. Add the AP-CY2 warning about HC^- vs HH.

**cyclic_ainf.tex** (51 lines): Adequate overview but thin. The cyclic invariance sign in Definition 3.4 (line 27) uses +/- without specifying the sign -- this must be made explicit (the sign is (-1)^{(|a_0|+1)(|a_1|+...+|a_n|+n)}). The S^d-framing section is a single paragraph. **Recommendation**: Expand substantially from notes/theory_cy_to_chiral_construction.tex Section 1 (the S^d-framing review).

**hochschild_calculus.tex** (23 lines): Three of four sections are empty. The one theorem (CY Hochschild duality) claims "the Gerstenhaber bracket on HH^* corresponds to the Connes B-operator on HH_*." **This is wrong.** The Gerstenhaber bracket corresponds to the Lie derivative (contraction with the BV operator); the Connes B-operator corresponds to the de Rham differential under HKR. These are different operations. **Recommendation**: Fix the theorem statement. This is a foundational error that must not appear in the final text.

### Part II: E1 and E2 Chiral Theories

**e1_chiral_algebras.tex** (44 lines): Adequate summary of Vol II material. The E1-Koszul duality theorem (line 37-44) cites Vol II correctly but gives the equivalence as Rep^{E1}(A) = Rep^{E1}(A^!)^{rev} without conditions. **Recommendation**: State the hypotheses (Koszul property, etc.).

**e2_chiral_algebras.tex** (66 lines): The most important chapter in the book after the introduction, and it has real content. The formal definition (via Ran(X) x Ran(Y)), Lurie's theorem on E2 = braided, and the E2 bar complex are all present. The E2-chiral Koszul duality is honestly marked as a conjecture. **Recommendation**: Import the formal definition from notes/theory_e2_chiral_formalism.tex (lines 222-274), which is cleaner and more precise than the chapter version.

**en_factorization.tex** (14 lines): Empty. Four section headers, no content. **Recommendation**: Either fill from the literature (Ayala-Francis, Costello-Gwilliam) or merge the relevant material into e2_chiral_algebras.tex and delete this file.

### Part III: The Bridge

**cy_to_chiral.tex** (39 lines): States CY-A for d=2 only (correct scope in the theorem statement, though the introduction overclaims). The four-step construction is outlined but not developed. **Recommendation**: Import the full construction from notes/theory_cy_to_chiral_construction.tex. This is the most important proof in the book and it deserves 30+ pages, not 2.

**quantum_chiral_algebras.tex** (31 lines): Definition-by-aspiration problem noted above. The R-matrix construction (lines 18-25) uses Theta_A correctly. **Recommendation**: Define "quantum chiral algebra" = "E2-chiral algebra with finite-dimensional weight spaces and an R-matrix satisfying QYBE," dropping the quantum-group-equivalence aspiration from the definition.

**modular_trace.tex** (26 lines): States CY-D. Three of four sections empty. **Recommendation**: Import genus expansion and shadow obstruction tower material from the notes.

### Part IV: Quantum Groups and Braided Monoidal Structure

**quantum_groups_foundations.tex** (14 lines): Empty. **Recommendation**: This standard material (U_q(g), R-matrix, YBE) is in every quantum groups textbook. Either write a 10-page review or drop the chapter and cite Chari-Pressley / Etingof-Schiffmann.

**braided_factorization.tex** (28 lines): States CY-B as a theorem. No proof. **Recommendation**: Import from notes/theory_denominator_bar_euler.tex, downgrade to Theorem-Sketch or mark with ClaimStatus.

**drinfeld_center.tex** (28 lines): The proposition Z(Rep^{E1}(A)) = Rep^{E2}(Z^{der}_{ch}(A)) is stated without proof or reference. **Recommendation**: Cite Ben-Zvi-Francis-Nadler, "Integral Transforms and Drinfeld Centers in Derived Algebraic Geometry," or provide a proof. Fill the empty sections from notes/theory_drinfeld_chiral_center.tex.

### Part V: The Standard Landscape

**k3_times_e.tex** (155 lines): **The best chapter in the book.** Detailed lattice theory, explicit Gram matrix, Weyl vector computation, BKM construction, denominator identity in both sum and product form, phi_{0,1} Fourier coefficients. The only chapter that feels like it was written by someone who computed things. **Recommendation**: Add proofs for the lemma (Sp4/SO isomorphism) and state the Gritsenko-Nikulin reference explicitly. Tag the "eight QVCGs" conjecture with ClaimStatusConjectured.

**toric_cy3_coha.tex** (79 lines): Good content. Schiffmann-Vasserot and RSYZ theorems correctly stated and attributed. The "CoHA as E1-sector" section is clear. The root datum from toric geometry (Section 14.6) is explicit. **Recommendation**: Add proofs or proof references for the two main theorems. Compute one non-trivial example beyond C^3 and the conifold.

**fukaya_categories.tex** (22 lines): Almost empty. One example (elliptic curve). **Recommendation**: Either write the chapter (Fukaya categories of K3, CY3 Fukaya categories, wrapped Fukaya) or merge the elliptic curve example into another chapter and drop this file.

**derived_categories_cy.tex** (19 lines): The HMS statement (line 10-13) is the only content. **Recommendation**: Either develop into a serious chapter (exceptional collections, stability conditions, tilting) or merge into cy_categories.tex.

**matrix_factorizations.tex** (16 lines): A single sentence about ADE singularities and W-algebras. **Recommendation**: This is potentially one of the most important chapters (MF(x^N) -> W_N is the key test case for the programme). Develop it with the explicit computation: MF(x^2) gives the free fermion = bc system; MF(x^3) gives the Zamolodchikov W_3 algebra. Or drop and note as future work.

**quantum_group_reps.tex** (25 lines): The CY-C theorem statement with the problems noted above. **Recommendation**: Rewrite as a conjecture. Define C(g,q). Separate the generic-q and root-of-unity cases.

### Part VI: Connections

**bar_cobar_bridge.tex** (16 lines): Empty. **Recommendation**: This should be the chapter that ties Vol III back to Vol I. Import from notes/theory_automorphic_shadow.tex (the central identification).

**modular_koszul_bridge.tex** (11 lines): Empty. **Recommendation**: Either fill or delete. This is the thinnest file in the project.

**geometric_langlands.tex** (14 lines): Empty. **Recommendation**: Import from notes/theory_qvcg_koszul.tex and notes/physics_sduality_langlands.tex, but mark everything as conjectural.

---

## VIII. SPECIFIC MATHEMATICAL ERRORS AND CONCERNS

1. **hochschild_calculus.tex line 19**: "the Gerstenhaber bracket on HH^* corresponds to the Connes B-operator on HH_*" is WRONG. The Gerstenhaber bracket is a degree -1 Lie bracket; the Connes B-operator is a degree +1 differential. They live in different worlds. Under CY duality, the Gerstenhaber bracket on HH^* corresponds to the BV operator (divergence operator) on HH_*, not the B-operator. Fix this.

2. **k3_times_e.tex line 48**: The isomorphism uses {+/- I_5} but the lattice Lambda^{3,2} has rank 5, so the identity matrix is I_5. However, line 47 writes "Sp_4(Z)/{+/- I_5}" -- this should be "Sp_4(Z)/{+/- I_4}" since Sp_4 acts on a rank-4 module. The SO side has I_5 (rank 5 lattice). Check this.

3. **quantum_group_reps.tex line 12**: q = exp(pi i/(k+h^v)). At generic q, k is irrational and V_k(g) is not a standard object. The standard parametrization for the KL equivalence is q = exp(2 pi i / (k+h^v)) with k a positive integer (or rational, for the logarithmic case). Verify the exact normalization.

4. **cyclic_ainf.tex line 27**: The cyclic invariance sign "+/-" must be made explicit. For a cyclic A-inf algebra of dimension d, the precise sign is:
   <mu_n(a_1,...,a_n), a_0> = (-1)^{|a_0|(|a_1|+...+|a_n|+n-1) + d(n-1)} <mu_n(a_0,a_1,...,a_{n-1}), a_n>
   Leaving this as "+/-" is sloppy and invites sign errors downstream.

5. **cy_to_chiral.tex line 29**: "Phi(C) is a chiral algebra whose underlying graded vector space is HH_*(C)." This cannot be literally true -- a chiral algebra on a curve X has fibers at points of X, and these fibers are infinite-dimensional (Fock spaces). The correct statement is that the **vacuum representation** of Phi(C) has character determined by HH_*(C), or that the generating fields are in bijection with HH^{*+1}(C). The Fock space structure from Step 2 (Sym^* of currents) is the actual underlying graded vector space.

---

## IX. THE COMPUTATIONAL FOUNDATION

The computational side is strong: 827 tests pass across 11 modules covering phi_{0,1} Fourier coefficients, C^3 DT partitions, modular lattice data, topological vertex, Igusa product formula, affine Yangian gl_1, BKM shadow obstruction tower, elliptic Hall algebra, CY Euler characteristics, WKB denominator, and Higgs P^1 CoHA.

This is the project's best asset and should be leveraged more aggressively. The arity-2 through arity-6 verification for K3xE (matching shadow obstruction tower projections with BKM root data) is the most convincing evidence for the programme's correctness.

**Recommendation**: The monograph should include explicit numerical tables from these computations. Show the reader the first 20 root multiplicities of g_{Delta_5}, the matching shadow obstruction tower components, and the numerical verification. This is what Kac would do.

---

## X. WHAT WOULD MAKE THIS PUBLISHABLE

### Short-term (1-3 months): One publishable paper

Extract a single paper: "The CY-to-chiral functor for CY2 categories." Contains:
- Definition of E2-chiral algebra (from notes, already solid)
- Construction of Phi for d=2 (Steps 1-3 from notes, already solid)
- The K3 example worked completely
- Computational verification

This is publishable at a strong journal (Compositio, Selecta, possibly JAMS depending on depth of examples).

### Medium-term (6-12 months): The monograph core

To make the monograph itself publishable:
1. Import all notes content into chapter files
2. Add ClaimStatus annotations to every theorem/proposition/conjecture
3. Write proofs for CY-A (d=2), the automorphic shadow identification (for K3xE specifically), and the denominator = bar Euler product (for K3xE specifically)
4. Mark everything else as conjectural
5. Fill or delete all empty chapters
6. Define "quantum vertex chiral group" precisely

### Long-term: Completing the programme

The d=3 case of CY-A, CY-C in full generality, the Langlands connection -- these are research problems, not editorial tasks. They should be stated as conjectures with the evidence clearly laid out, not as theorems.

---

## SUMMARY TABLE

| Chapter file | Lines | Theorems | Proofs | Empty sections | Grade |
|-------------|-------|----------|--------|----------------|-------|
| introduction.tex | 119 | 0 | 0 | 0 | B+ |
| cy_categories.tex | 65 | 0 | 0 | 0 | B |
| cyclic_ainf.tex | 51 | 0 | 0 | 1 | B- |
| hochschild_calculus.tex | 23 | 1 | 0 | 3 | D (error) |
| e1_chiral_algebras.tex | 44 | 2 | 0 | 1 | C |
| e2_chiral_algebras.tex | 66 | 3 | 0 | 0 | B |
| en_factorization.tex | 14 | 0 | 0 | 4 | F |
| cy_to_chiral.tex | 39 | 1 | 0 | 2 | C |
| quantum_chiral_algebras.tex | 31 | 0 | 0 | 2 | D |
| modular_trace.tex | 26 | 1 | 0 | 3 | C- |
| quantum_groups_foundations.tex | 14 | 0 | 0 | 4 | F |
| braided_factorization.tex | 28 | 1 | 0 | 2 | C- |
| drinfeld_center.tex | 28 | 1 | 0 | 2 | C |
| k3_times_e.tex | 155 | 4 | 0 | 0 | A- |
| toric_cy3_coha.tex | 79 | 2 | 0 | 0 | B+ |
| fukaya_categories.tex | 22 | 0 | 0 | 4 | F |
| derived_categories_cy.tex | 19 | 0 | 0 | 3 | F |
| matrix_factorizations.tex | 16 | 0 | 0 | 3 | F |
| quantum_group_reps.tex | 25 | 1 | 0 | 2 | D |
| bar_cobar_bridge.tex | 16 | 0 | 0 | 3 | F |
| modular_koszul_bridge.tex | 11 | 0 | 0 | 2 | F |
| geometric_langlands.tex | 14 | 0 | 0 | 3 | F |

8 of 22 chapter files are graded F (empty stubs).

| Notes file | Lines | Theorems | Proofs | Conjectures | Grade |
|-----------|-------|----------|--------|-------------|-------|
| theory_automorphic_shadow.tex | 1239 | 6 | 4 | 0 | A- |
| theory_e2_chiral_formalism.tex | 1243 | - | 5 | - | A- |
| theory_coha_e1_sector.tex | 1175 | 14 | 5 | 1 | B+ |
| theory_qvcg_koszul.tex | 1184 | 7 | 6 | 2 | B+ |
| theory_kl_e2_chiral.tex | 1157 | 12 | 4 | 3 | B |
| theory_denominator_bar_euler.tex | 993 | 7 | 7 | 0 | B+ |
| theory_cy2_cy3_fibration.tex | 961 | 5 | 2 | 3 | B |
| theory_cy_to_chiral_construction.tex | 783 | 11 | 7 | 0 | A- |
| theory_higgs_cy2_qvcg.tex | 829 | 15 | 2 | 1 | B |
| theory_drinfeld_chiral_center.tex | 667 | 9 | 6 | 3 | B |
| theory_generalized_root_datum.tex | 651 | 9 | 6 | 1 | A- |
| Compute modules (11 files, 827 tests) | - | - | - | - | A |

The notes are where the mathematics lives. The chapters are where it should live but does not yet.
