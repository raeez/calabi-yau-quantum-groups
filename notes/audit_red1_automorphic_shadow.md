# Adversarial Audit: theory_automorphic_shadow.tex

## Auditor: Red Team Agent 1 (Beilinson Rectification)
## Date: 2026-04-02
## Target: Theorem 1.1 (Automorphic Correction = Shadow Postnikov Tower)
## Scope: notes/theory_automorphic_shadow.tex, with cross-references to theory_cy_to_chiral_construction.tex, theory_denominator_bar_euler.tex, theory_generalized_root_datum.tex, physics_anomaly_cancellation.tex

---

## FINDING 1: The kappa-rho formula is internally inconsistent and numerically wrong
**Severity: CRITICAL**

The theorem statement (line 144) claims:

    kappa(A_X) = <rho, rho> - |Delta^re_+|

The proof (line 349, equation eq:kappa-rho) gives a DIFFERENT formula:

    kappa(A_X) = <rho, rho> - (1/24) * sum_{alpha in Delta^re_+} 1

These are not the same formula. The theorem says subtract the COUNT of positive real roots. The proof says subtract 1/24 times that count. For K3 x E with 3 real simple roots (these generate infinitely many positive real roots under the Weyl group, but the proof text writes "3/24"), the discrepancy is immediate.

Worse: NEITHER formula gives kappa = 5. The proof claims (rho, rho) = -1/2 for the K3 x E Weyl vector rho = f_2 - (1/2)f_3 + f_{-2}. Then:
- Theorem formula: kappa = -1/2 - 3 = -7/2
- Proof formula: kappa = -1/2 - 3/24 = -1/2 - 1/8 = -5/8

Neither equals 5. The text asserts "confirming kappa(A_{K3 x E}) = 5" without any computation that produces this number from the stated formula. The actual source of kappa = 5 is the weight of Delta_5, which comes from a completely different computation: (1/2) * c_0(phi_{0,1}) = (1/2) * 10 = 5 (as correctly stated in physics_anomaly_cancellation.tex, line 226). The kappa-rho formula (eq:kappa-rho) is simply WRONG as written.

Meanwhile, theory_cy_to_chiral_construction.tex (line 613) gives yet another formula:

    kappa(A_C) = chi^CY(C) = sum_i (-1)^i dim HH_i(C)

For K3 x E, the topological Euler characteristic chi(K3 x E) = 0 (stated explicitly in physics_anomaly_cancellation.tex, line 169). The HH Euler characteristic differs from the topological one, but the note at line 276 of physics_anomaly_cancellation.tex acknowledges the paradox "chi(X) = 0 but kappa = 5" and declares them "different physical quantities" -- without resolving what chi^CY actually evaluates to.

So we have THREE incompatible formulas for kappa:
1. kappa = <rho, rho> - |Delta^re_+| (theorem statement)
2. kappa = <rho, rho> - (1/24) |Delta^re_+| (proof, eq:kappa-rho)
3. kappa = chi^CY(C) = sum (-1)^i dim HH_i(C) (theory_cy_to_chiral_construction.tex)

All three allegedly equal 5 for K3 x E, but no computation demonstrates this for any of them. The Freudenthal-de Vries formula for the Casimir eigenvalue of a Kac-Moody algebra is <rho, rho> = (1/24) sum_{alpha in Delta_+} (alpha, alpha), which for simply-laced algebras with (alpha, alpha) = 2 gives <rho, rho> = |Delta_+|/12. This is different from all three formulas above. The invocation of "Freudenthal-de Vries" at line 352 is either a misquotation or a non-standard version that needs explicit derivation.

**Impact**: The entire proof of part (a) rests on the kappa-rho correspondence. If this formula is wrong, the identification of arity-2 data with real roots + Weyl vector is unsubstantiated.

---

## FINDING 2: The chiral algebra A_X does not exist for a CY3
**Severity: CRITICAL**

The entire theorem is vacuous unless the CY-to-chiral functor Phi produces an actual chiral algebra A_X for a CY threefold X. Examining theory_cy_to_chiral_construction.tex, the construction of Phi proceeds in 4 steps:

- Step 1 (cyclic A_inf to Lie conformal): PROVED for d=2 and d=3 (standard).
- Step 2 (factorization envelope): PROVED (Beilinson-Drinfeld).
- Step 3 (E_2-enhancement via S^d-framing):
  - For d=2: PROVED (Kontsevich-Vlassopoulos).
  - For d=3: **CONJECTURAL** (line 523: "conjectural in full generality for d >= 3 (the negative cyclic refinement at chain level is delicate)").
- Step 4 (quantization):
  - For d=2: PROVED.
  - For d=3: **CONJECTURAL** (line 628: "requires the chain-level S^3-framing to be compatible with BV, which is expected but not proved in the literature").

The central theorem is stated for CY THREEFOLDS (d=3). At d=3, both the E_2-enhancement (Step 3) and the quantization (Step 4) are conjectural. The S^3-framing gap is explicitly acknowledged.

The status table in theory_cy_to_chiral_construction.tex (line 725) marks the d=3 E_2-enhancement as "PH/CJ" (proved here / conjectural), conditional on the S^3-framing. This means A_X DOES NOT EXIST as a fully constructed object for CY3s. The theorem asserts properties of A_X (its bar complex computes CE cohomology, its shadow tower matches the BKM root system) without A_X being defined.

This is not a gap that can be papered over. If A_X does not exist, then B(A_X) does not exist, kappa(A_X) is undefined, Theta_{A_X} is undefined, and every claim in parts (a)-(d) of the theorem is literally meaningless.

The K3 x E example might appear to bypass this by being a product CY3, but the product structure alone does not establish the S^3-framing. The K3 component gives an S^2-framing; the elliptic curve gives an S^1-framing; combining them gives S^2 x S^1, which is NOT S^3 (it is homotopy-inequivalent).

**Impact**: The entire theorem is conditional on the existence of A_X for CY3, which rests on two unproved conjectures (S^3-framing and BV-compatibility). This should be stated as a conditional theorem, not an unconditional one.

---

## FINDING 3: The arity-depth induction has a subadditivity gap
**Severity: SERIOUS**

The inductive step of Theorem 4.1 (line 536-607) claims that depth is subadditive: "every depth-(r-1) root can be written as a sum of a lower-depth root and an imaginary simple root, the latter having depth 1" (line 582-584).

This is asserted without proof, and it is not obvious.

The depth function (Definition 2.2, line 220-235) is defined as follows: write alpha = sum n_i delta_i + beta where delta_i are real simple roots and beta is a sum of imaginary simple roots. Then depth(alpha) = |beta| (the number of imaginary summands).

Two problems:

(a) The decomposition alpha = sum n_i delta_i + beta is NOT unique. A positive root may have multiple expressions as a sum of simple roots (real and imaginary). The depth should be the MINIMUM over all such decompositions, but this is not stated. If depth is defined in terms of an arbitrary decomposition, it is not well-defined. If it is the minimum, the subadditivity claim requires proof.

(b) Even assuming well-definedness, subadditivity of depth with respect to root addition (depth(alpha + beta) <= depth(alpha) + depth(beta)) does not follow from the definition. It would follow if every decomposition of alpha + beta could be refined from decompositions of alpha and beta, but this requires that the real root parts combine without interference -- which fails when the Weyl group creates non-trivial identifications.

More seriously: the lower bound argument (lines 577-590) claims that every depth-(r-1) root alpha can be written as alpha = beta + gamma where beta has depth <= a-2 and gamma has depth <= b-2 for some a + b = r + 1. This requires that depth-(r-1) roots are always sums of lower-depth roots. But what about depth-1 imaginary SIMPLE roots? These are, by definition, NOT decomposable as sums of positive roots. The induction handles them at r = 3 (the base case), but the general step implicitly assumes that every root of depth d >= 2 is a sum of roots of depth < d. This is not proved.

For a BKM superalgebra, roots can be "indecomposable" in the sense of not being writable as a sum of two positive roots, even at high depth. The imaginary simple roots at depth d >= 2 would break the induction. Whether such roots exist depends on the specific BKM algebra, but for the K3 x E case with infinitely many imaginary simple roots (from phi_{0,1}), this is a real concern.

**Impact**: The inductive proof of part (c) has a logical gap at the lower bound step. The depth filtration needs a rigorous definition (minimum over decompositions) and the decomposability of non-simple roots at each depth needs proof.

---

## FINDING 4: The CE cohomology for superalgebras uses the WRONG formula
**Severity: SERIOUS**

Equation (eq:ce-bar) at line 738-741 writes:

    H*(B_alpha(A_X)) ~ (bigwedge* n_+*)_alpha

and then adds a parenthetical: "where the exterior algebra accounts for the super-grading: symmetric powers for even/bosonic roots, exterior powers for odd/fermionic roots."

This parenthetical CONTRADICTS the displayed formula. The displayed formula says "bigwedge* n_+^*" (exterior algebra). For a Lie SUPERalgebra, the CE complex uses:
- Exterior powers of EVEN part: bigwedge* (n_{+,0})^*
- Symmetric powers of ODD part: Sym* (n_{+,1})^*

The correct formula for the CE complex of a Lie superalgebra n_+ = n_{+,0} + n_{+,1} is:

    C^*(n_+, k) = bigwedge*(n_{+,0}^*) tensor Sym*(n_{+,1}^*)

This is NOT "bigwedge* n_+^*". The exterior algebra of the full n_+ would give exterior powers of BOTH even and odd parts, which is wrong. The companion note theory_denominator_bar_euler.tex (lines 490-496) gets this right, explaining that even root spaces contribute (1 - q^alpha) and odd root spaces contribute (1 + q^alpha)^{-1}. But the main automorphic shadow note writes bigwedge* n_+^* and only corrects itself in the parenthetical, creating a misleading equation.

The Euler-Poincare formula at line 751-757 is then stated correctly with separate products over even and odd roots. But equation (eq:ce-bar) on which it rests is wrong as displayed.

On the bar-complex side: the claim that "the bar complex of a dg algebra with both even and odd generators has the same sign structure as the super CE complex" (theory_denominator_bar_euler.tex, lines 504-508) is asserted without proof. This requires that the chiral algebra A_X is a superalgebra in the correct sense -- that the BKM Z/2-grading lifts to a Z/2-grading on A_X compatible with the bar differential. This depends on the CY-to-chiral functor Phi preserving the fermion number grading. Given that Phi is conjectural for d=3 (Finding 2), this compatibility is also conjectural.

**Impact**: The displayed CE formula is wrong. The correction in the parenthetical and the subsequent Euler-Poincare formula happen to give the right answer, but the logical chain has a broken link. Additionally, the super-sign compatibility between bar and CE requires proof.

---

## FINDING 5: The "operadic complexity conjecture" invalidates the shadow-L_infinity identification at all arities
**Severity: SERIOUS**

The proof mechanism (Section 6, "The structural mechanism") rests on three facts. Fact 2 (lines 963-985) is:

    "The shadow Postnikov tower Theta^{<=r}_A is the finite-arity truncation of the transferred L_infinity structure on H*(B(A))."

The text then states (lines 974-977):

    "This identification is proved at arities 2, 3, 4 in Vol I (Proposition 4.12, shadow-formality at low arity) and conjectured at all arities (the operadic complexity conjecture, Conjecture 4.15)."

This is devastating. The inductive theorem (Theorem 4.1) claims the depth-arity correspondence at ALL arities r >= 2. But the identification of shadow components S_r with L_infinity operations ell_r is only proved for r = 2, 3, 4. For r >= 5, it is a CONJECTURE.

The inductive step of Theorem 4.1 at arity r+1 uses the identification of Theta_{r+1} with the L_infinity operation ell_{r+1} (line 596-601: "the transferred L_infinity operation ell_{r+1} on H*(B(A_X))"). If the shadow-L_infinity identification is conjectural for r >= 5, then the inductive proof of Theorem 4.1 is valid only for r <= 4 (capturing roots of depth <= 2). Beyond that, both the inductive step and the multiplicity counting are conditional on Conjecture 4.15 of Vol I.

This means part (c) of the main theorem should be stated as: proved for arity <= 4 (depth <= 2), conjectural for higher arities. The denominator identity (part d) similarly depends on the full tower, so it too is conditional.

**Impact**: The main theorem is unconditionally proved only for arities 2, 3, 4 (parts a, b, and the depth-2 case of part c). Parts c (general r) and d depend on the operadic complexity conjecture, which is unproved.

---

## FINDING 6: The Feigin-Frenkel theorem is not stated for BKM superalgebras
**Severity: SERIOUS**

The proof of part (d), Step 1 (lines 725-734) claims:

    "For a Lie algebra g with enveloping algebra U(g) and the associated vertex algebra V(g), the chiral bar complex B(V(g)) is quasi-isomorphic to the Chevalley-Eilenberg cochain complex C*(n_+, k). This is the content of the Feigin-Frenkel theorem (for affine Kac-Moody algebras) generalized to BKM superalgebras."

The Feigin-Frenkel theorem is proved for AFFINE Kac-Moody algebras (the specific case of g being finite-dimensional semisimple, with affine being the loop algebra). The text asserts that this "generalizes to BKM superalgebras" without citation, proof, or even a precise statement of what the generalization says.

BKM superalgebras differ from Kac-Moody algebras in several crucial ways:
1. They have imaginary simple roots with arbitrary multiplicities (not just real simple roots).
2. They are Lie SUPERalgebras, with odd generators contributing symmetric (not exterior) factors to CE.
3. The positive subalgebra n_+ is infinitely generated (the imaginary roots provide infinitely many generators at each depth).
4. The vertex algebra V(g_X) associated to a BKM superalgebra is NOT the same as the Kac-Moody vacuum module -- it is a much larger object.

The "semi-infinite cohomology" interpretation (line 733-734) is invoked but not defined. Semi-infinite cohomology is a well-developed subject for Virasoro and affine algebras (Feigin, Frenkel, Garland-Lepowsky), but its extension to general BKM superalgebras is non-trivial. The convergence issues alone (infinitely many generators) require care.

A search of the codebase for "Feigin-Frenkel" combined with "BKM" or "generalized" returns no results. This generalization is asserted but nowhere established.

**Impact**: The key quasi-isomorphism B(A_X) ~ C*_CE(n_+) that underlies the denominator identity proof is unproved for the relevant class of algebras.

---

## FINDING 7: The collision r-matrix does NOT literally encode the Gram matrix
**Severity: MODERATE**

Part (a) claims (lines 307-335) that the collision r-matrix r(z) = Res^{coll}_{0,2}(Theta_{A_X}) determines the Gram matrix A_{ij} = (delta_i, delta_j) via the OPE:

    [h_i, e_j](z) ~ (A_ij * e_j(w)) / (z - w)

This identifies the Gram matrix with the OPE COEFFICIENTS of the Chevalley generators. But this requires:

1. That A_X contains Chevalley generators e_i, f_i, h_i corresponding to the real simple roots. This presupposes that A_X is the vertex algebra of a Kac-Moody algebra -- but A_X is constructed from a CY3 category via the functor Phi (which is conjectural for d=3, see Finding 2). There is no argument that Phi(D^b(Coh(X))) contains Kac-Moody generators.

2. That the OPE poles of the Chevalley generators are determined by the Gram matrix in the standard way. This is true for Kac-Moody vertex algebras V_k(g), but A_X is not a Kac-Moody vertex algebra in general -- it is a quantum chiral algebra whose structure depends on the full CY category. The identification of the real root OPE with Kac-Moody OPE is an assertion, not a consequence of the construction.

3. For K3 x E specifically: the text claims the Gram matrix is ((2,-2,-2),(-2,2,-2),(-2,-2,2)). This is correct for the lattice Lambda^{2,1}_{II}, but the question "does the collision r-matrix of A_{K3xE} literally encode this matrix?" requires knowing A_{K3xE} explicitly. Since A_{K3xE} has not been constructed (Finding 2), this cannot be verified.

**Impact**: The claim that arity-2 data determines the real roots is plausible but relies on A_X containing Kac-Moody-type generators, which is not proved.

---

## FINDING 8: Two incompatible descriptions of the bar Euler product
**Severity: MODERATE**

The theorem statement (line 167-174, eq:denom-bar) gives the denominator identity as:

    prod_{alpha in Delta_+} (1 - e^{-2pi i <alpha, z>})^{mult(alpha)}
    = prod_{n >= 1} det_{H*(B^{(n)}(A_X))} (1 - q^n * sigma)^{(-1)^{|sigma|+1}}

The right-hand side involves a product over bar ARITY n, with sigma running over a "basis of bar generators." But the denominator identity on the left involves a product over ROOTS alpha. These are completely different indexing sets. The bar arity n is a positive integer labeling the n-fold bar component; the root alpha is a lattice vector.

The proof (Section 5, Definition 5.1, eq:bar-euler-def and eq:bar-euler-chi) gives a DIFFERENT formula for the bar Euler product:

    Z_B(A; q) = prod_{alpha in Lambda_+} (1 - q^alpha)^{(-1)^{k+1} dim H^k(B_alpha(A))}

This is a product over ROOT LATTICE vectors alpha, not over bar arities n. The two formulas (theorem eq:denom-bar vs proof eq:bar-euler-def) use different indexing and different notation. The reconciliation is never explicitly performed.

Presumably the claim is that the bar-arity decomposition B(A_X) = bigoplus_n B^{(n)}(A_X) refines the root-lattice decomposition B(A_X) = bigoplus_alpha B_alpha(A_X), and after appropriate reorganization the two products agree. But this reorganization is non-trivial (it requires showing that the bar arity and the root grading are compatible in a specific way) and is not carried out.

**Impact**: The theorem statement and its proof use different formulas that are not shown to be equivalent. The identification requires a non-trivial combinatorial argument relating bar arity to root grading.

---

## FINDING 9: The depth function for K3 x E is described imprecisely
**Severity: MODERATE**

Lines 237-242 describe the depth function for K3 x E:

    "An imaginary root alpha = (n, l, m) with nm > 0 has depth equal to its distance from the boundary of the positive cone, as measured by the minimal number of imaginary simple root additions needed to reach alpha from a real root orbit."

This is a description, not a definition. The phrase "minimal number of imaginary simple root additions needed to reach alpha from a real root orbit" is ambiguous:
- Does "reach from a real root orbit" mean alpha = w(delta_i) + sum of imaginary simples, for some w in W?
- Or does it mean alpha = beta + sum of imaginary simples, where beta is any real positive root?
- What if alpha cannot be reached from any real root orbit by adding imaginary simple roots?

For BKM algebras, the imaginary simple roots are not necessarily "deep" -- they can sit at the boundary of the positive cone (null vectors with (alpha, alpha) = 0). The depth of an imaginary simple root should be 1 by the definition at line 228 ("depth(alpha) >= 1 for imaginary roots"), but the informal description at line 237 says depth equals "distance from the boundary," which for a null vector ON the boundary would be 0.

**Impact**: Minor confusion in exposition. The formal definition (Definition 2.2) is adequate, but the informal description is misleading and potentially contradicts it.

---

## SUMMARY TABLE

| # | Finding | Severity | Type |
|---|---------|----------|------|
| 1 | kappa-rho formula is internally inconsistent and numerically wrong | CRITICAL | Mathematical error |
| 2 | Chiral algebra A_X does not exist for CY3 (S^3-framing gap) | CRITICAL | Missing prerequisite |
| 3 | Depth subadditivity asserted without proof; decomposability of non-simple roots unproved | SERIOUS | Logical gap |
| 4 | CE formula for superalgebras displays the wrong formula (bigwedge instead of bigwedge tensor Sym) | SERIOUS | Mathematical error |
| 5 | Shadow-L_infinity identification conjectural for arity >= 5 (operadic complexity conjecture) | SERIOUS | Conditional on conjecture |
| 6 | Feigin-Frenkel theorem not established for BKM superalgebras | SERIOUS | Missing generalization |
| 7 | Collision r-matrix does not literally encode Gram matrix without Kac-Moody generators in A_X | MODERATE | Circular reasoning |
| 8 | Two incompatible formulas for bar Euler product not reconciled | MODERATE | Presentation gap |
| 9 | Depth function for K3 x E imprecisely described | MODERATE | Expositional |

## OVERALL ASSESSMENT

The theorem as stated is **not proved**. It has two CRITICAL issues:

1. The foundational kappa = <rho, rho> - ... formula (Finding 1) is mathematically inconsistent across three different versions and does not yield the claimed value kappa = 5 from any of them. This undermines part (a).

2. The chiral algebra A_X for CY3s does not exist as a constructed object (Finding 2). The S^3-framing and BV-compatibility needed for d=3 are both acknowledged as conjectural in the companion note. This makes every assertion about A_X for CY3 vacuous.

Even setting aside these critical issues, the inductive proof of part (c) has logical gaps (Findings 3, 5), the CE cohomology is misstated (Finding 4), and the generalization of Feigin-Frenkel to BKM superalgebras is unproved (Finding 6).

**What IS established**: For CY2 (d=2), where A_X exists via the S^2-framing (Kontsevich-Vlassopoulos), parts (a) and (b) are plausible (modulo fixing the kappa formula). The denominator identity for the specific case of Kac-Moody algebras (not BKM) follows from the classical Feigin-Frenkel theorem. The dictionary between shadow tower and automorphic correction is a compelling organizational framework.

**What is NOT established**: The theorem for CY3, which is the case of actual interest (K3 x E, toric CY3, etc.). The conditional nature of the result should be made explicit in the theorem statement.
