# RED TEAM AUDIT: theory_e2_chiral_formalism.tex

**Auditor**: Adversarial mathematical audit (Beilinson principle)
**Date**: 2026-04-02
**Target**: `notes/theory_e2_chiral_formalism.tex` (1243 lines, 5 sections)
**Methodology**: Attack every claim; dismiss nothing without proof; verify references against the literature.

---

## FINDING 1: Ran(X) x Ran(Y) vs Ran(X x Y) -- definitional gap [TIER 1, GENUINE]

**Location**: Section 1.2 (lines 103--145), Definition in Section 1.5 (lines 222--274)

**The issue**: The definition factorizes on Ran(X) x Ran(Y), which parametrizes *independent* finite subsets S_X in X and S_Y in Y. This is NOT the same as Ran(X x Y), which parametrizes finite subsets of the product surface. The key difference:

- Ran(X) x Ran(Y) sees points as living in separate curves; collisions happen only within each factor.
- Ran(X x Y) sees points as living in the surface; a point (x,y) can collide with (x',y') diagonally.

An E_2-algebra on a surface S should be a factorization algebra on Ran(S), not on Ran(pi_1(S)) x Ran(pi_2(S)). The Ayala--Francis framework (cited elsewhere in the monograph at lines 521, 721 of theory_cy_to_chiral_construction.tex) defines E_n-factorization algebras on Ran(M) for an n-manifold M. For M = C (a complex curve viewed as a real 2-manifold), this gives E_2-algebras on Ran(C), not on Ran(R) x Ran(R).

The document attempts to bridge this via the commuting-square diagram (lines 129--143) and identifies this with Dunn additivity. This is the correct *idea* -- Dunn additivity says E_2-Alg(C) = E_1-Alg(E_1-Alg(C)) -- but the geometric implementation needs more care:

1. The factorization isomorphisms (eqs 1--2) only fire when X-points or Y-points are *separately* disjoint. They do not address the diagonal collisions in X x Y where both coordinates approach simultaneously (z -> 0, w -> 0 along a curve in C^2).
2. The double OPE (eq 3, line 172) does handle the mixed case via the Laurent expansion in (z,w), but it is not clear that the Ran(X) x Ran(Y) formalism *encodes* these mixed collisions. In Ran(X) x Ran(Y), the diagonals {x_i = x_j} and {y_i = y_j} are independent; there is no diagonal {(x_i, y_i) = (x_j, y_j)}.

**Diagnosis**: The definition is correct for giving *two commuting E_1 structures*, but the claim that this is equivalent to E_2 (line 145) requires verification that the commuting-square condition plus chirality in both directions actually recovers the full E_2 operad action -- not just the two E_1 actions, but all the higher coherences. The FM operad compatibility (Section 1.4) is stated as part of the definition (item (iv)), which somewhat addresses this by fiat. But then the definition is *overdetermined*: items (i)--(iii) give the Ran(X) x Ran(Y) factorization structure, and item (iv) separately demands the FM operad action. The relationship between these is asserted but not proved.

**Severity**: TIER 1. The definition works by including item (iv), but the text repeatedly claims that the commuting-square condition *alone* gives E_2 (line 145: "This commuting-square condition is the factorization-algebraic incarnation of the Dunn additivity equivalence"). This is misleading. The commuting-square condition gives two commuting E_1 structures; Dunn additivity says this is *equivalent* to E_2, but only in the infinity-categorical sense with all higher coherences, not at the level of a single commuting square.

**Recommendation**: Add a remark after line 145 clarifying that the commuting-square condition is a *shadow* of Dunn additivity, and that the full E_2 equivalence requires the higher coherences packaged in item (iv). Alternatively, state that the definition is the FM-operad action (iv), and (i)--(iii) are consequences. The current structure suggests (i)--(iii) are the definition and (iv) is extra structure, which is backwards.

---

## FINDING 2: [d_X, d_Y] = 0 claim -- correct at genus 0, contradicted at genus >= 1 [TIER 1, GENUINE INCONSISTENCY]

**Location**: Lines 413--423 (Section 2.2) vs lines 806--826 (Section 3.4)

**The issue**: Section 2.2 states unequivocally:

> "The commutativity d_X . d_Y = d_Y . d_X follows from the E_2-compatibility... [d_X, d_Y] = 0."

This is stated as a proved fact (ClaimStatusProvedHere). Then Section 3.4 states:

> "[d_X, d_Y] = kappa(A) . omega_g at genus g >= 1"

which is marked ClaimStatusConjectured.

These two statements directly contradict each other. The resolution is implicit (genus 0 vs genus >= 1), but Section 2.2 makes NO genus restriction. The E_2 bar complex is defined for a general E_2-chiral algebra, and [d_X, d_Y] = 0 is stated as a theorem (with proof). The genus-g curvature in Section 3.4 is specific to A = Phi(C) for a CY category, but the issue is that Section 2.2 proves [d_X, d_Y] = 0 *unconditionally*, which would mean Section 3.4's conjecture is automatically false.

**Diagnosis**: The likely intended distinction is:
- At genus 0 (on a fixed curve, without modular integration): [d_X, d_Y] = 0 genuinely holds.
- At genus g >= 1 (after coupling to the moduli space M_{g,n}): the curvature kappa(A) . omega_g appears.

But this distinction is never stated. The bar complex of Section 2 is defined on Ran(X) x Ran(Y) for fixed curves X, Y -- which is the genus-0 setting. Section 3.4 implicitly changes the arena to include integration over moduli. The reader is left to guess this.

**Severity**: TIER 1 (logical inconsistency in the text as written). The mathematics is likely sound once the genus restriction is made explicit, but the current presentation contains a flat contradiction.

**Recommendation**: Add to Section 2.2 (after line 419) an explicit remark: "This commutativity holds at genus 0, i.e., on fixed curves X, Y. At genus g >= 1, when the bar-cobar complex is coupled to the moduli space M_{g,n}, the commutator acquires a curvature term; see Section 3.4." Similarly, Section 3.4 should explicitly state that the [d_X, d_Y] = 0 of Section 2.2 is being modified by the passage to families over M_{g,n}.

---

## FINDING 3: Braiding from transposition -- symmetric group vs braid group [TIER 2, PARTIALLY ADDRESSED]

**Location**: Lines 484--547 (Section 2.3)

**The issue (as posed)**: "Transposing two E_1 structures gives a symmetry, not a braiding." This concern asks: does sigma (transposition of E_1 factors) give only an involution (Z/2 action), or a genuine braiding (Z action)?

**Analysis after reading**: The text handles this better than the attack suggests, but with a subtle gap. The construction (lines 485--507) defines beta = sigma . tau, where sigma is the transposition involution and tau is the graded swap. This composite is an involution: beta^2 = id at the level of the bar complex.

The *braiding* (non-trivial monodromy) comes from the *proof sketch* of the R-matrix proposition (lines 536--547), which invokes the fundamental group pi_1(FM_3(C)) = P_3 (the pure braid group). The monodromy of the factorization algebra around the diagonals gives the non-trivial braiding. This is geometrically correct: pi_1(Conf_2(C)) = Z gives the braiding, and the generator corresponds to one point winding around another in the complex plane.

**However**, there is a gap in the exposition: the braiding beta as *defined* in eq (13) is just sigma . tau, which is an involution. The R-matrix in eq (14) is a *different* object -- it is the monodromy of the factorization algebra. The text never explicitly connects these two constructions. Line 511 says the braiding "evaluated on the chiral envelope... takes the form of a universal R-matrix" but this evaluation involves analytic continuation (monodromy), which is never discussed in the algebraic definition.

The transition from "algebraic transposition" to "analytic monodromy" is the heart of the matter, and it is elided. The braiding on Rep^{E_2}(A) is NOT beta = sigma . tau (which would be a symmetry). It is the monodromy representation of pi_1(Conf_2(C)) = Z, which happens to be detected by the FM operad action. The text conflates these.

**Severity**: TIER 2. The final answer is correct (E_2 gives braiding from monodromy), and the proof sketch gives the right argument. But the explicit definition of beta (eq 13) as sigma . tau gives only an involution, which contradicts "braiding" until the analytic continuation step is supplied. This is a presentation issue, not a mathematical error, but it is confusing.

**Recommendation**: Rewrite the transition from the algebraic beta (eq 13) to the R-matrix (eq 14). The key point is that beta is the *algebraic* skeleton of the braiding, but the actual braiding on representations is the monodromy, which is a deformation of beta by the OPE coefficients. State this explicitly.

---

## FINDING 4: E_2 Koszul self-duality claim [TIER 2, IMPRECISE]

**Location**: Lines 692--695

**The claim**: "E_2 is Koszul as an operad: the Koszul dual cooperad E_2^! is equivalent (up to suspension) to E_2 itself, by the self-duality of the E_2 operad (a theorem of Getzler--Jones and Fresse)."

**The issue**: This is imprecise in a way that matters.

1. The Koszul dual of E_2 as a *quadratic* operad is the Gerstenhaber cooperad Ger^!, which is NOT E_2 but rather the *suspension* of the Gerstenhaber operad: E_2^! = Ger^! = Ger{2} (up to operadic suspension). The statement "equivalent to E_2 itself" is correct only because H_*(E_2) = Ger and Ger is self-dual up to suspension. But the chain-level E_2 operad is NOT self-dual -- it is only *formal* (equivalent to its homology) over characteristic zero, and this formality is exactly the Kontsevich--Tamarkin theorem of Section 4.

2. The Getzler--Jones result (1994) establishes the Koszul duality of the *homology* operad Ger, not of E_2 itself at the chain level. The chain-level statement requires formality (Tamarkin, Fresse--Willwacher). Attributing chain-level self-duality to Getzler--Jones is an overstatement.

3. More importantly: the bar-cobar adjunction for E_2 at the chain level requires a choice of formality quasi-isomorphism, hence a choice of Drinfeld associator. This is acknowledged in Section 4.2 (lines 890--899) but NOT in Section 3.1 where the bar-cobar adjunction is stated and "proved." The proof sketch in Section 3.1 uses "E_2 is Koszul" without noting the associator dependence. This means the "Koszul locus" (line 671) and the inversion theorem (lines 670--678) implicitly depend on a choice of associator, which should be stated.

**Severity**: TIER 2. The mathematical content is correct once all the dependencies are assembled, but the proof sketch in Section 3.1 is misleading about the inputs. The associator dependence of the E_2 bar-cobar adjunction is a non-trivial feature (it is the GRT_1-torsor structure), not a technicality.

**Recommendation**: Add a remark after the proof in Section 3.1 (line 714) stating: "The bar-cobar adjunction for E_2 at the chain level depends on a choice of Drinfeld associator (equivalently, a formality quasi-isomorphism for E_2). The statements above hold for any such choice; different choices give equivalent but non-canonically isomorphic adjunctions. See Section 4.2 for details."

---

## FINDING 5: E_2-Koszul duality conjecture -- insufficient evidence [TIER 2, GENUINE CONCERN]

**Location**: Lines 747--798 (Conjecture 3.3)

**The claim**: Rep^{E_2}(A) = Rep^{E_2}(A^{!_{E_2}})^{rev} as braided monoidal categories.

**The issue**: The evidence presented is:
1. It reduces to E_1 Koszul duality (known).
2. For affine KM, it predicts level-rank duality (known independently).
3. The braiding reversal has an operadic explanation.
4. For CY_2, it predicts categorical mirror symmetry.

This evidence is suggestive but logically circular in part. Item (2) is evidence *for* the conjecture only if the E_2-enhancement of V_k(g) and the identification with the KL category are independently established -- which they are (Section 5.2). Item (4) is a prediction, not evidence.

The real concern is deeper: E_2-Koszul duality at the level of *representation categories* is considerably harder than E_1-Koszul duality. The key issue is that the bar-cobar adjunction must preserve not just the module categories but also the *braided monoidal structure*. This requires:
- The bar functor B_{E_2} to be an E_2-monoidal functor (claimed in (iii) of the bar-cobar theorem, line 681).
- The Koszul dual A^{!_{E_2}} to inherit an E_2-structure (claimed in Definition 3.2).
- The passage from coalgebras to algebras (linear duality) to be compatible with the E_2-structure.

Each of these steps works for E_1 because E_1-coalgebras are just coassociative coalgebras. For E_2, the coalgebra side involves the Gerstenhaber cooperad, and linear duality must respect the Lie bracket structure. This is where the GRT dependence becomes critical: the Koszul dual A^{!_{E_2}} depends on the choice of associator, and the conjecture must hold for *all* choices (or for a specific canonical choice).

The text does not acknowledge this issue. Fresse's work (referenced at line 695, 866) on E_n-operads shows that the bar-cobar adjunction for E_2 is GRT-equivariant, which means the conjecture should be GRT-equivariant as well. This is a non-trivial structural constraint that is not mentioned.

**Severity**: TIER 2. The conjecture is reasonable and likely correct, but the evidence section should acknowledge the GRT dependence and state whether the conjecture is expected to hold canonically or only up to GRT action.

**Recommendation**: Add to the evidence list: "(5) GRT equivariance: the conjecture is expected to hold for any choice of Drinfeld associator, with the equivalence functors forming a GRT_1-torsor. This follows from the GRT-equivariance of the E_2 bar-cobar adjunction (Fresse)."

---

## FINDING 6: The CY3 and AP-CY3 discussion -- correct but could be sharper [TIER 3, PRESENTATION]

**Location**: Lines 309--314 (Remark on E_2 vs E_infty), cross-referenced with theory_cy_to_chiral_construction.tex lines 469--513

**The claim**: The remark at line 309 correctly states that E_2 braiding is not symmetric and references AP-CY3. The companion note (theory_cy_to_chiral_construction.tex) has a detailed discussion of the CY3 case: S^3-framing gives E_3, which restricts to E_2 via Dunn, but the restricted braiding is "symmetric to first order" because pi_1(Conf_2(R^3)) = Z/2.

**Analysis**: The attack question asks whether CY3 gives E_3 (not E_2), and whether E_3 kills the quantum group structure. The monograph handles this correctly:
- CY3 gives E_3, which restricts to E_2 (Prop at line 474 of theory_cy_to_chiral_construction.tex).
- E_3 makes the braiding symmetric at the topological level (pi_1 = Z/2), but quantum corrections from pi_2 restore non-trivial structure.
- The warning at line 495 of theory_cy_to_chiral_construction.tex explicitly addresses this.

However, the E_2-chiral formalism note itself (the document under audit) does NOT discuss this. The only reference to the CY3 issue is the one-line "cf. anti-pattern AP-CY3" at line 314. A reader of this note alone would not understand the CY3 subtlety.

**Severity**: TIER 3 (cross-reference adequacy). The mathematics is correct and handled elsewhere. This note could benefit from a one-paragraph remark in Section 5.3 explaining that CY_3 categories produce E_3, which restricts to E_2 with additional symmetry constraints on the braiding.

**Recommendation**: No action needed in this note if the reader is expected to consult theory_cy_to_chiral_construction.tex. If this note is meant to be self-contained, add a remark after line 1119 or in Section 5.3 explaining the CY3 vs CY2 distinction.

---

## FINDING 7: pi_1(FM_3(C)) = P_3 claim [TIER 3, CORRECT]

**Location**: Lines 537--538

**The claim**: "FM_3(C) has fundamental group isomorphic to the pure braid group P_3 on three strands."

**Verification**: FM_n(C) is a compactification of Conf_n(C), and the inclusion Conf_n(C) -> FM_n(C) is a homotopy equivalence (the boundary strata are contractible in the relevant sense). So pi_1(FM_n(C)) = pi_1(Conf_n(C)). For n=3, Conf_3(C) has pi_1 = P_3 (the pure braid group on 3 strands). The full braid group B_3 arises from the *unordered* configuration space Conf_3(C)/S_3.

The text then claims three generators sigma_12, sigma_13, sigma_23 satisfying the braid relation sigma_12 sigma_23 sigma_12 = sigma_23 sigma_12 sigma_23. This is INCORRECT for the *pure* braid group. The pure braid group P_3 has generators A_{ij} (one point going around another and returning), not sigma_i (one strand crossing over the next). The braid relation sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2 is a relation in B_3 (the full braid group), not P_3.

**Wait -- let me reconsider**: The text uses sigma_{12}, sigma_{13}, sigma_{23} as *generators of the pure braid group*, not the standard Artin generators sigma_1, sigma_2 of B_3. For P_3, the generators are indeed indexed by pairs (i,j), and there are relations among them (the pure braid relations), but they are NOT the Artin braid relation. The relation sigma_12 sigma_23 sigma_12 = sigma_23 sigma_12 sigma_23 written at line 543 is the Artin braid relation for B_3, not a relation in P_3. In P_3, the generators A_{ij} satisfy different relations (e.g., A_{ij} and A_{kl} commute when {i,j} and {k,l} are disjoint, and there are conjugation relations otherwise).

**Diagnosis**: The proof sketch conflates the pure braid group P_3 (the fundamental group of the *ordered* configuration space) with the braid group B_3 (fundamental group of the *unordered* configuration space). The braid relation cited is a B_3 relation. The QYBE derivation from the braid relation is correct for B_3, not for P_3 directly. The connection is that the QYBE comes from the representation theory of B_n (via the R-matrix), and B_n acts on the tensor product A^{otimes n} (not just P_n). So the proof works, but the stated group is wrong: it should be B_3 (acting on ordered configurations via the Artin representation), or equivalently, pi_1(Conf_3(C)/translation) = B_3.

Actually, on further reflection: the pi_1 of the *labeled* configuration space is P_n, and the QYBE for the R-matrix R_{ij} does follow from P_n relations (each R_{ij} = monodromy of A_{ij}). The relation in P_3 that gives the QYBE is the Kohno relation (a consequence of the pure braid relations), not the Artin braid relation as written. The text writes the Artin relation instead of the correct pure braid relation. This is a presentation error.

**Severity**: TIER 3 (minor mathematical error in proof sketch). The conclusion (QYBE from monodromy) is correct. The intermediate claim (braid relation in P_3) is stated imprecisely.

**Recommendation**: Replace "satisfying the braid relation sigma_12 sigma_23 sigma_12 = sigma_23 sigma_12 sigma_23" with the correct pure braid group relations, or switch to stating that B_3 acts on the unordered configuration space and the QYBE follows from the Artin braid relation for B_3.

---

## FINDING 8: Iterated bar equivalence B_Y(B_X(A)) = B_X(B_Y(A)) [TIER 2, NEEDS PROOF]

**Location**: Lines 380--389 (eq 8)

**The claim**: B_{E_2}(A) = B_Y(B_X(A)) ~ B_X(B_Y(A)), with the equivalence from Dunn additivity.

**The issue**: This is the statement that the iterated bar construction is symmetric: bar-first-in-X-then-in-Y is equivalent to bar-first-in-Y-then-in-X. This is stated as a consequence of Dunn additivity, but Dunn additivity says E_2 ~ E_1 tensor E_1, which is a statement about *algebras*, not about *bar constructions*.

The bar construction is a functor, and the claim is that B_Y . B_X ~ B_X . B_Y as functors E_2-Alg -> E_2-Coalg. This requires that the bar construction commutes with the Dunn decomposition, which is a non-trivial statement. For *strict* algebras (not just homotopy algebras), the iterated bar construction is manifestly symmetric because the two bar differentials act on independent tensor factors. But for homotopy E_2-algebras (which is the relevant case in the chiral setting), the iterated bar construction involves higher homotopies, and the commutativity is a theorem (following from the formality of E_2 over char 0), not a tautology.

**Severity**: TIER 2. The claim is correct (it follows from E_2 formality + Dunn), but "consequence of Dunn additivity" understates the proof. Dunn alone is not sufficient; formality is needed for the chain-level statement.

**Recommendation**: Add: "The equivalence of the two iterated bar constructions follows from Dunn additivity together with the Kontsevich--Tamarkin formality of Section 4: over char(k) = 0, the E_2 bar construction can be computed at the level of homology (Gerstenhaber algebras), where the symmetry is manifest."

---

## FINDING 9: CY_2 proposition -- d_Y identified with Connes B-operator [TIER 2, QUESTIONABLE]

**Location**: Lines 1108--1117 (Section 5.3)

**The claim**: For a CY_2 category C, the E_2 bar complex has d_Y = the Connes B-operator of HH_*(C).

**The issue**: The Connes B-operator B: HH_n(C) -> HH_{n+1}(C) is a degree +1 operator satisfying B^2 = 0 and bB + Bb = 0 (where b is the Hochschild differential). In the bar complex description, B is the cyclic rotation operator. The claim identifies d_Y (the Y-direction bar differential, which involves Y-direction OPE residues) with B.

This identification is geometrically motivated (the Y-direction encodes the cyclic structure) but requires verification:
1. B has degree +1 on Hochschild homology. The bar differential d_Y has bar-degree -1 (line 398). These are compatible only with appropriate degree conventions.
2. B is defined on the cyclic bar complex, not on the iterated bar complex. The identification requires showing that the Y-bar construction of the X-bar complex reduces to the cyclic bar complex in the appropriate limit.
3. The claim that Delta_Y = "dual of the cyclic cup product on HH^*(C)" is similarly non-obvious and unstated elsewhere.

This entire proposition is marked CJ (conjectured), so it is not being presented as proved. But the specific identification d_Y = B should be flagged as requiring significant work to establish.

**Severity**: TIER 2. The identification is likely correct (it is the natural guess), but it is more than a conjecture -- it is a specific structural prediction that could be verified or falsified by computation.

**Recommendation**: Note that the identification d_Y = B is a non-trivial structural prediction. A computation for the simplest non-trivial CY_2 category (e.g., D^b(Coh(T^2)) or the A_1 Fukaya category) would provide evidence.

---

## FINDING 10: "Three S^1-factors in S^3" claim in companion note [TIER 1, GENUINE ERROR ELSEWHERE]

**Location**: NOT in the audited file, but in theory_cy_to_chiral_construction.tex line 489, referenced by the audited file's Section 6 (which describes the CY-to-chiral functor).

**The claim**: "The three S^1-factors in S^3 give three E_1-structures."

**The issue**: S^3 does NOT have three S^1-factors. S^3 is not a product of circles. The Hopf fibration gives S^1 -> S^3 -> S^2, but this is a fibration, not a product decomposition. There is no canonical way to extract three independent S^1-actions from S^3.

What IS true: S^3 has an SO(4)-action, and SO(4) ~ (SU(2) x SU(2)) / Z/2. Each SU(2)-factor contains an S^1 (the maximal torus). So there are *two* independent S^1-actions, not three. The Dunn decomposition E_3 ~ E_2 x E_1 gives a decomposition into an E_2-factor and an E_1-factor (two E_1's inside E_2, plus one more E_1), but this is a decomposition of the *operad*, not of the sphere.

This error is in the companion note, not the audited file. But the audited file's Section 6 depends on the CY-to-chiral functor, which uses this construction.

**Severity**: TIER 1 (genuine error in a dependency). The claim "three S^1-factors in S^3" is false. The correct statement is that E_3 ~ E_1 tensor E_1 tensor E_1 (by iterated Dunn), so an E_3-algebra has three E_1-structures. This is an operadic statement, not a topological decomposition of S^3. The note should say "the three E_1-factors in the Dunn decomposition E_3 ~ E_1^{tensor 3}" rather than "the three S^1-factors in S^3."

**Recommendation**: Fix theory_cy_to_chiral_construction.tex line 489 to refer to the iterated Dunn decomposition rather than non-existent S^1 factors of S^3.

---

## SUMMARY TABLE

| # | Location | Description | Severity | Type |
|---|----------|-------------|----------|------|
| 1 | Sec 1.2, 1.5 | Ran(X) x Ran(Y) vs Ran(X x Y): definition needs FM datum (iv) for E_2, commuting square alone insufficient | TIER 1 | Definitional gap |
| 2 | Sec 2.2 vs 3.4 | [d_X, d_Y] = 0 stated unconditionally, contradicted by genus >= 1 curvature | TIER 1 | Internal inconsistency |
| 3 | Sec 2.3 | beta = sigma . tau gives involution, not braiding; monodromy step is elided | TIER 2 | Presentation gap |
| 4 | Sec 3.1 | E_2 "self-duality" conflates homology Ger with chain-level E_2; associator dependence suppressed | TIER 2 | Imprecision |
| 5 | Sec 3.3 | E_2-Koszul duality conjecture lacks GRT equivariance discussion | TIER 2 | Missing context |
| 6 | Remark l.309 | AP-CY3 handling correct but thin in this note | TIER 3 | Presentation |
| 7 | Sec 2.3 proof | P_3 vs B_3: Artin braid relation cited for pure braid group | TIER 3 | Minor error in proof sketch |
| 8 | Sec 2.2 | Iterated bar symmetry claimed from Dunn alone; actually needs formality | TIER 2 | Understated proof |
| 9 | Sec 5.3 | d_Y = Connes B-operator identification unverified | TIER 2 | Untested prediction |
| 10 | Dependency | "Three S^1-factors in S^3" in theory_cy_to_chiral_construction.tex is false | TIER 1 | Genuine error elsewhere |

**TIER 1 findings (must fix)**: 3 (Findings 1, 2, 10)
**TIER 2 findings (should fix)**: 5 (Findings 3, 4, 5, 8, 9)
**TIER 3 findings (minor/presentation)**: 2 (Findings 6, 7)

---

## DISPOSITION OF ORIGINAL ATTACK VECTORS

1. **Ran(X) x Ran(Y) vs Ran(X x Y)**: GENUINE GAP (Finding 1). The definition compensates with item (iv), but the text is misleading about what gives E_2.

2. **[d_X, d_Y] = 0 claim**: GENUINE INCONSISTENCY (Finding 2). The genus-0 vs genus->=1 distinction is never stated.

3. **Braiding from transposition**: PARTIALLY GENUINE (Finding 3). The text gets the right answer but the explicit formula (eq 13) gives an involution, not a braiding. The monodromy step (the actual source of non-trivial braiding) is correctly invoked in the proof sketch but not connected to the definition.

4. **E_2-Koszul duality and GRT**: GENUINE CONCERN (Findings 4, 5). The GRT dependence is acknowledged in Section 4 but suppressed in Section 3 where it matters most.

5. **AP-CY3 (CY3 -> E_3 -> E_2)**: FALSE ALARM for the audited note. The monograph handles this correctly in theory_cy_to_chiral_construction.tex. The claim that E_3 "kills quantum group structure" is wrong -- E_3 restricts to E_2, and the extra symmetry only constrains the braiding to first order. However, the companion note has a genuine error about "three S^1-factors in S^3" (Finding 10).
