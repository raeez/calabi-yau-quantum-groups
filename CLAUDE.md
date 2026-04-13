# CLAUDE.md -- Volume III: CY Categories, Quantum Groups, and BPS Algebras

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol III-specific material.**

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_2-ChirAlg providing input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function.

~319pp, this repo, 17,199 tests. Five parts: I(CY Engine) II(CY Characteristic Datum) III(CY Landscape) IV(Seven Faces of r_CY(z)) V(CY Frontier).

**4 genuine stub chapters** (<50 lines, AP114): quantum_groups_foundations (24), geometric_langlands (28), matrix_factorizations (29), modular_koszul_bridge (13). Develop or comment out. **3 thin chapters** (50-100 lines, may need development): cyclic_ainf (55), cy_categories (70), e1_chiral_algebras (90). **6 formerly listed stubs now developed** (>150 lines): hochschild_calculus, braided_factorization, drinfeld_center, fukaya_categories, quantum_group_reps, derived_categories_cy.

## Main Theorems

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROGRAMME | d=3 conditional on chain-level S^3-framing |
| **CY-B** (E_2-chiral Koszul duality) | PROGRAMME | Depends on CY-A |
| **CY-C** (Quantum group realization) | CONJECTURAL | C(g,q) not constructed. Uses \begin{conjecture}. NEVER \begin{theorem} |
| **CY-D** (Modular CY characteristic) | PROGRAMME | kappa well-defined only when A_C exists |
| **E_3 Koszul (Heisenberg)** | d=2 PROVED | thm:e3-koszul-heisenberg, 39 tests |
| **E_3 Koszul (Yangian)** | COHOMOLOGICAL PROVED | thm:e3-koszul-yangian, 36 tests |
| **E_2 Koszul (Heisenberg)** | d=2 PROVED | thm:e2-koszul-heisenberg, 49 tests |
| **Kummer route Steps 1-4** | PROVED | prop:kummer-orbifold, 85 tests |
| **E_1-chiral bialgebra axioms** | FOUNDATIONAL | sec:e1-chiral-bialgebras, 80 tests |

## The kappa-Spectrum (AP113, CRITICAL)

Bare "kappa" is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript:

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_ch | From chiral algebra A_C via Phi | 3 |
| kappa_BKM | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |
| kappa_cat | From categorical/holomorphic Euler char | 2 = chi(O_{K3}) |
| kappa_fiber | From lattice/fiber structure | 24 (lattice rank) |

kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch and kappa_BKM. Full spectrum: {2,3,5,24}.

## HOT ZONE -- Top 10 Vol III Repeat Offenders

Read this section BEFORE any Edit. These are the AP-CY patterns that fire repeatedly across waves despite being catalogued. Each entry is an operational template, not prose. If you only read 80 lines of Vol III CLAUDE.md, read these.

### HZ3-1. AP-CY6/AP-CY14 (unconstructed A_X in theorem environment)

Decision tree, answer BEFORE writing `\begin{theorem}`:

```
Q1: Does the proof chain pass through A_X for d=3, G(X), C(g,q), or any
    object whose existence is part of the d=3 programme?
    YES -> \begin{conjecture} + \ClaimStatusConjectured. STOP. NEVER theorem.
    NO  -> Q2
Q2: Does it pass through A_X for d=2 (CY-A proved)?
    YES -> \begin{theorem} or \begin{proposition} OK; cite CY-A explicitly.
    NO  -> Q3
Q3: Pure categorical / VOA / Yangian statement (no functor invocation)?
    YES -> \begin{theorem} or \begin{proposition} OK; classical proof.
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than retract.
```

Vol III default: `\begin{conjecture}` regardless. The 11+ instances fixed across 4 commits prove that the LLM pattern-matches on "if X then Y" logical form without checking whether X exists.

### HZ3-2. AP113 (bare kappa)

ZERO TOLERANCE in Vol III. Before writing ANY `\kappa`:

```
(i)  Subscript present?  Required: {ch, cat, BKM, fiber}
(ii) Forbidden subscripts: {global, BPS, eff, total, naive, MacMahon}
     If you wrote BPS, you mean BKM. Rename now.
(iii) Meta-naming "kappa-spectrum" / "kappa-value":
     write \kappa_\bullet to satisfy the grep regex (the bullet denotes
     the indexing variable across the approved set).
```

Decision tree:
- chiral algebra A_C / Phi(C) -> `\kappa_{\mathrm{ch}}`
- Borcherds-Kac-Moody / Igusa weight -> `\kappa_{\mathrm{BKM}}`
- Holomorphic Euler char chi(O_X) -> `\kappa_{\mathrm{cat}}`
- Lattice rank / fiber structure -> `\kappa_{\mathrm{fiber}}`

### HZ3-3. AP-CY11 (conditional propagation)

If a result depends on Conjecture X which depends on CY-A_3, the result IS conditional on CY-A_3. Use `\ClaimStatusConditional` and state the dependency chain. Pattern caught at Tier 2: `cor:kappa-from-charts` was `ProvedHere` despite chaining through `conj:e1-chart-gluing -> CY-A_3`. Fixed in cy_to_chiral.tex L1127.

Template before `\ClaimStatusProvedHere`:

```
Q: Does this result's proof chain reach back to CY-A_3 or any unconstructed object?
   NO  -> ProvedHere OK
   YES -> ClaimStatusConditional + name the chain in the body
```

### HZ3-4. AP-CY7 (CoHA vs E_1-chiral)

The Cohomological Hall Algebra is associative, NOT a chiral algebra. The slogan "the E_1-sector of G(X)" assumes G(X) exists (AP43). Forbidden conflations:

```
"CoHA = E_1-chiral algebra"  WRONG
"E_1-sector of G(X)"          assumes G(X), AP43 violation
"CoHA carries a vertex algebra structure"  WRONG (it carries a Hall product)
```

CoHA is the Hochschild cohomology of the quiver-with-potential category, with the Schiffmann-Vasserot-Yang-Zhao multiplication. The connection to chiral algebras is via the FUNCTOR Phi (CY-A), not by identification.

### HZ3-5. AP-CY3/AP-CY4 (E_2, Drinfeld center, derived center)

Three distinct objects:

```
1. E_2-monoidal category C  =  little 2-disks structure (NOT symmetric).
2. Drinfeld center Z(C)     =  monoidal-category center via half-braidings.
3. Derived center Z^der_ch(A) =  Hochschild cochains, the bulk algebra.
```

NEVER conflate. Drinfeld center Z(Rep^{E_1}(A)) is a category-theoretic operation; derived center Z^der_ch(A) is the bulk operator algebra. The relationship: Drinfeld center IS the categorification of derived center (modular envelope).

### HZ3-6. AP-CY8 (Borcherds denominator vs bar Euler product)

For K3 x E, the identification `Phi_10 = bar Euler product` is an OBSERVATION, not a theorem. It is conditional on:
- CY-A_2 (which IS proved at d=2)
- The Vol I Borcherds-lift identification of bar Euler products

Template: any sentence asserting equality between automorphic forms and bar Euler products MUST cite both CY-A and the Vol I anchor explicitly. Bare "the bar Euler product equals Phi_10" is forbidden.

### HZ3-7. AP-CY17 (MF(W) CY dimension)

For W: A^n -> A^1, the matrix factorization category MF(W) is CY of dimension `n-2`, NOT `n-1`. Mnemonic: ADE in 2 variables gives CY_0 (semisimple). Need 4 variables for CY_2. Need 5 variables for CY_3 (Fermat quintic).

Verification template before any MF(W) CY claim:

```
W: A^n -> A^1, n = ?
MF(W) is CY_{n-2}; check n-2 against the desired CY dimension.
n=2: CY_0 (ADE Lie algebras)
n=3: CY_1
n=4: CY_2 (compact K3 surfaces from quartic)
n=5: CY_3 (compact threefolds from quintic)
```

### HZ3-8. AP-CY10 (flop vs Koszul dual)

Birational flop X -> X^+ is a derived equivalence; it PRESERVES kappa_ch. Koszul dual A -> A^! has `kappa(A) + kappa(A^!) = K` (family-dependent conductor). Forbidden conflations:

```
"flop is the Koszul dual"          WRONG
"kappa(A_X) + kappa(A_{X^+}) = 0"  WRONG (flops preserve kappa)
"kappa(A_X) = kappa(A_{X^+})"      RIGHT (flop is autoequivalence)
```

Flop exchanges chambers in the Mukai motion; Koszul exchanges algebra/coalgebra. Different operations entirely.

### HZ3-9. AP-CY12 (shadow class from full tower)

The G/L/C/M classification of a CY chiral algebra MUST be computed from the full shadow tower, NOT from generator counting or non-formality alone. Template:

```
"X has m_3 != 0"  ->  necessary condition for class >= L; not sufficient.
"shadow tower terminates at depth 2"  ->  class L (verified by computation).
"m_n != 0 for all n"  ->  class M (full tower computation required).
"local P^2 has 3 generators"  ->  inadequate for class. Compute the tower.
```

local P^2 IS class M (infinite depth), not class L. Wrong classification was caught in compute/audit/cy_shadow_class_audit.

### HZ3-10. AP-CY13/V2-AP26 (cross-volume Part references)

NEVER hardcode `Part~IV`, `Chapter~12` in Vol III prose. Always use `\ref{part:...}`. Before any cross-volume reference:

```
(i)  Use \ref{part:foo}, never Part~N
(ii) After ANY restructuring, grep ALL THREE volumes for stale Part refs:
     grep -rn 'Part~[IVXL]' chapters/ appendices/ standalone/
(iii) Verify every match resolves to a current part label
```

Vol III's Tier 2 dnp_identification_master.tex Vol II edit caught a stale Part~II reference (Tier 2 Task E4); the canonical Vol I Parts list is in main.tex L822-1400.

## E_1/E_2 Chiral Hierarchy

E_1-chiral (Vol II): associative factorization on C x R. Monoidal rep categories. E_2-chiral (this vol): braided factorization on C x C. Braided monoidal rep categories: habitat of quantum groups. E_1 -> E_2 via Dunn additivity. d=2: S^2-framing of HH_*(C) gives E_2. d=3: holomorphic CS breaks E_2 to E_1; recover E_2 via Drinfeld center Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^der_ch(A)). Drinfeld center is categorified av: E_1-Cat -> E_2-Cat. Quantum groups, Yangians, braided tensor categories natively E_1. E_2 derived.

## CY-Specific Anti-Patterns (AP-CY1 through AP-CY8)

AP-CY1: CY dimension d != complex dimension n. Fuk(X) is CY_n, D^b(Coh(X)) is CY_n. Not real dim 2n.
AP-CY2: CY trace is in HC^-_d(C), NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing.
AP-CY3: E_2 != commutative. E_2 braiding is NOT symmetric. E_2 -> E_inf loses quantum group structure.
AP-CY4: Drinfeld center Z(C) (monoidal category) != derived center Z^der_ch(A) (chiral). State which.
AP-CY5: Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple.
AP-CY6: A_X for CY3 does NOT exist. It IS the d=3 programme. NEVER write as if defined. **Strengthened**: any result whose proof chain passes through A_X at d=3 MUST carry \ClaimStatusConditional and explicitly name CY-A_3 as dependency. Conditionality PROPAGATES through all downstream results.
AP-CY7: CoHA != E_1-chiral algebra. CoHA is associative. "E_1-sector of G(X)" assumes G(X) exists (AP43).
AP-CY8: Borcherds denominator != bar Euler product. Identification requires CY-to-chiral functor. For K3 x E: observation, not theorem.

### Empirical (AP-CY9-13, from 50-commit error archaeology)
AP-CY9: Jacobi form discriminant constraint. For phi_{k,m} of index m, only discriminants D with D=0 or D=3 mod 4 (m=1) can appear. NEVER fill coefficient table with sequential D-values. Verify discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention, NOT 1.
AP-CY10: Flop != Koszul dual. Birational flop X->X^+ is derived equivalence PRESERVING kappa. Koszul dual A^! has kappa(A)+kappa(A^!)=rho_K. Flop exchanges chambers; Koszul exchanges algebra/coalgebra. kappa(A_X)=kappa(A_{X+}) for flop, NOT kappa(A_X)+kappa(A_{X+})=0.
AP-CY11: Conditional d=3 transitivity. If Result B depends on Result A which depends on CY-A_3, then B is ALSO conditional on CY-A_3. Use \ClaimStatusConditional and state the dependency chain. DEFAULT environment for new Vol III formal statements is \begin{conjecture} unless proof is COMPLETE and UNCONDITIONAL.
AP-CY12: Shadow class from full computation. G/L/C/M must be determined by computing full shadow tower, NOT by counting generators. Non-formality (m_3!=0) does NOT by itself determine shadow depth. local P^2 is class M (infinite depth), not class L.
AP-CY13: Cross-volume Part number staleness. After ANY Part restructuring in ANY volume, grep ALL THREE volumes for stale Part references. Part numbers are the most fragile cross-reference. Use \ref{part:...} exclusively, never hardcode. **Strengthened**: run grep -rn 'Part~[IVXL]' chapters/ notes/ and verify EVERY match. 7+ stale refs survived a single restructuring.

### Deep Empirical (AP-CY14-19, from 100-commit deep archaeology)
AP-CY14: Unconstructed object inhabits theorem environment. ANY statement whose proof chain passes through G(X) at d=3, A_{K3xE}, or any unconstructed object MUST use \begin{conjecture}, NEVER \begin{theorem}/\begin{proposition}. The LLM pattern-matches on logical structure ("if X then Y") without checking whether X exists. 11+ instances fixed across 4 commits. DEFAULT in Vol III is \begin{conjecture}.
AP-CY15: README scope inflation beyond .tex ground truth. README must not claim "verified" or "proved" for structural analogies or pattern matches. The README accumulates stronger claims than the .tex supports because the LLM optimizes for impressiveness. After README edits, verify every "proved"/"verified" against corresponding \ClaimStatus tag.
AP-CY16: Matrix size conflation in group quotients. Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5. O(Lambda^{3,2}) quotient by +/-I_5 (5x5). When two groups of different rank appear in the same formula, the LLM harmonizes subscripts to whichever appears more frequently.
AP-CY17: MF(W) CY dimension is n-2, NOT n-1. For W: A^n -> A^1, MF(W) is CY_{n-2} (Dyckerhoff). ADE in 2 variables: CY_0 (semisimple). Need 4 variables for CY_2. The n-1 vs n-2 error changes which families are CY_2.
AP-CY18: Lattice theta series comparison. Verify q-power divergence by DIRECT COMPUTATION. Leech theta: minimum norm^2=4, first correction at q^2 not q^1. The match with 1/eta^24 extends through q^1. Never conflate j(tau) coefficients with V_Lambda character coefficients.
AP-CY19: A-hat genus argument halving. A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi (first pole of sin(x/2) at x=2*pi). NEVER drop the /2 in the argument, which gives spurious radius pi. Appeared in 3+ independent computations.
AP-CY20: Normal bundle vs spectral parameters. The Z x Z grading from the normal bundle N_{C/Y} of a curve C in a CY threefold Y connects to the quantum toroidal parameters (q,t) through the Omega-background, NOT through the bundle grading directly. The intermediary mechanism (equivariant localization on the Omega-background, Nekrasov partition function, refinement) must be stated explicitly. NEVER write "N_{C/Y} grading = (q,t) parameters" as a direct identification. Counter: before any claim relating normal bundle gradings to quantum group parameters, name the intermediary mechanism and cite the equivariant/Omega-background passage.

### Cross-Programme (AP150-AP157 + FM24, from current session)
AP150: Agent confabulation of non-existent structures. Agents stitch disparate results (e.g. a categorical equivalence from paper A + a representation-theoretic identity from paper B) into composite structures that do not exist in the literature or the manuscript. The stitching looks plausible because each ingredient is real, but the composite arrow has never been constructed. Counter: before writing any composite diagram or multi-step identification, verify EACH ARROW independently. If any arrow is unverified, the composite is conjectural and must use \begin{conjecture}.
AP151: Convention clash from coexisting hbar definitions. Two definitions of hbar (e.g. hbar = log(q) vs hbar = (log q)/(2*pi*i), or hbar as deformation parameter vs hbar as Planck constant) can coexist in the same chapter when material is drawn from different sources. The discrepancy cascades silently through all formulas that depend on hbar. Counter: before introducing ANY hbar, grep the current file and all imported chapters for existing definitions. If a second convention is needed, introduce a distinct symbol (hbar', hbar_1, Psi) with an explicit bridge identity. One file, one hbar.
AP152: "Ordered" ambiguity between labeled and time-ordered. "Ordered product" can mean (a) labeled/indexed product (combinatorial, the E_1 ordered bar B^ord) or (b) time-ordered/radially-ordered product (analytic, the OPE). These are DIFFERENT operations producing different algebraic structures. Counter: every use of "ordered" must specify WHICH ordering: "labeled-ordered" (combinatorial), "time-ordered" (analytic/radial), or "normally-ordered" (Wick). Bare "ordered" is forbidden.
AP153: E_3 scope inflation. E_3 algebra structure on Hochschild cochains (Deligne conjecture) applies to E_inf algebras, NOT to E_1 algebras. The E_3 claim requires the input to be at least E_inf (commutative). For E_1 inputs, Hochschild cochains carry only E_2 structure (Dunn additivity: E_1 tensor E_2 = E_3, but the E_1 input contributes E_1 not E_inf). Counter: before claiming E_3 structure, verify the input algebra is E_inf. If the input is E_1, the correct structure level is E_2.
AP154: Two E_3 structures conflated (algebraic vs topological). Even when E_3 structure is correctly invoked, there are two distinct E_3 structures: (a) the algebraic E_3 from Deligne's conjecture on HH*(A) for E_inf A, and (b) the topological E_3 from framed little 3-disks on configuration spaces of R^3. These agree under formality but differ at the chain level. Counter: specify which E_3 (algebraic Deligne or topological configuration-space) and state whether formality is assumed.
AP155: Overclaiming novelty for known invariants from new framework. When the CY-to-chiral functor Phi recovers a known invariant (e.g. Euler characteristic, Mukai vector, Donaldson-Thomas count) through a new construction, the INVARIANT is not new, only the CONSTRUCTION PATH is. Counter: before claiming novelty, check whether the output invariant already appears in the literature under a different name. If it does, state: "Phi recovers the known invariant X (originally due to [ref]) via a new construction path through the chiral bar complex."
AP156: Weierstrass P_1 convention ambiguity. The function variously denoted P_1, wp_1, or zeta_tau in the elliptic function literature can mean either (a) theta_1'(z,tau)/theta_1(z,tau) (the logarithmic derivative of theta_1, quasi-periodic) or (b) the Weierstrass zeta function zeta(z;Lambda) (which differs by a linear term involving eta_1). These differ by Im(z)-dependent terms that matter for modular transformation. Counter: before writing P_1 or any first-order elliptic function, specify which convention (theta_1'/theta_1 vs Weierstrass zeta_tau) and state the quasi-periodicity explicitly.
AP157: Degeneration-type dependence. Limits of CY manifolds (large complex structure, conifold, orbifold, tropical, maximal unipotent monodromy) produce different chiral algebras with different kappa values. A statement proved "in the degeneration limit" is meaningless without specifying WHICH degeneration. Counter: every degeneration-limit claim must name the degeneration type (large complex structure / conifold / orbifold / MUM / tropical / other) and state whether the result is specific to that degeneration or holds for all degenerations.
FM24: B-cycle sign error from i^2. In genus >= 1, the B-cycle integral involves factors of i (from the imaginary part of the period matrix). The error i^2 = 1 (instead of i^2 = -1) propagates silently and produces |q| = 1 instead of |q| < 1 for the nome, destroying convergence of all q-expansions. Counter: after any computation involving B-cycle integrals, verify that |q| < 1 (convergence of q-expansion). If |q| = 1, trace back to an i^2 sign error. Additionally, verify that Im(tau) > 0 is preserved by all transformations.

### New APs from 6d hCS Session (AP-CY21-AP-CY26, April 2026)
AP-CY21: E_3 bar dimensions for non-free-field algebras are OPEN. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes, but the COHOMOLOGY depends on the shadow class. For class G: P(q)^{3g} (formal, infinite). For class L: (1+t)^{3g} (dim 2^{3g}). For class C: (1+t)^{3g} (charge conservation kills d_4). For class M: INFINITE-DIMENSIONAL (d_4 survives). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
AP-CY22: Miki automorphism is algebra-specific, NOT operadic. The S_3 permutation of (q_1,q_2,q_3) comes from the Weyl group of the CY torus, not from the E_3 operad in general. Counterexample: k[x]/(x^2) is E_3 but has no Miki. Counter: never derive Miki from the E_3 operad alone; always state it requires the specific algebra U_{q,t}(gl_hat_hat_1).
AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
AP-CY24: Docstring ground-truth confabulation. Agents produce correct CODE but fabricate "ground truth" values in docstrings. The function computes correctly; the docstring claims wrong values for n ≥ 4. Counter: verify EVERY numerical value in docstrings against the actual function output. Especially dangerous for OEIS sequences.
AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
AP-CY26: Verdier duality parameter inversion does NOT invert σ_2. For the Heisenberg, k^! = -k comes from Shapovalov form transposition (Verdier duality transposes the inner product), NOT from σ_2(-h_i) = -σ_2 (FALSE: σ_2 is degree-2 homogeneous, hence EVEN under h_i → -h_i). Counter: derive k^! from Shapovalov/Verdier, not from σ_2 inversion.

## 6d Holomorphic CS Programme (established April 2026)

The Costello programme constructs chiral quantum groups from holomorphic CS at each dimension:
- 3d hol CS → Kac-Moody (PROVED, Costello-Gwilliam)
- 5d hol CS → Affine Yangian (PROVED, Costello 2013)
- 6d hol theory → Quantum toroidal (CONJECTURAL, Costello-Francis-Gwilliam route)

Key results established in Vol III:
- E_1-chiral bialgebra axioms (Section 7 of e1_chiral_algebras.tex, ~400 lines, NEW MATH)
- E_3 bar cohomology: (1+t)^{3g} for classes L,C; fails for class M
- Kummer route: ∫_{K3} F via CY-A_2 only (Steps 1-4 PROVED, Step 5 conjectural)
- K3 Yangian: degree-(24,24) structure function from Mukai lattice
- Borcherds lift = resummation (additive Saito-Kurokawa = perturbative, multiplicative Borcherds = non-perturbative)
- Class M = mock modular (κ_ch = -h|_{q^{-1/8}})
- Center-hocolim obstruction: >92% of K3×E Drinfeld center invisible to local charts
- MO stable envelopes bypass center-hocolim for global braiding
- Two-parameter R-matrix: R_ch(u,v) = R_1(u)R_2(v)R_12(u-v) (Zamolodchikov factorization)
- E_2 → E_3 promotion is the DERIVED center (higher Deligne), not iterated Drinfeld center

Detailed results:
- Kummer route: ∫_{T^4} H_1 = rank-16 Heis, Z_2-inv = rank-8, 16 twisted sectors h=1/2, orbifold κ_ch=2, resolution 8+32-16=24=Mukai rank. Steps 1-4: prop:kummer-orbifold (PROVED). Step 5: conj:kummer-route.
- Hopf axioms: all 5 verified at spin 2 (50 tests): coassociativity (Δ_w⊗id)∘Δ_{z+w}=(id⊗Δ_z)∘Δ_w, counit ε=vacuum projection, antipode S(T_n)=(2Ψ-3)T_n, quasi-triangularity Δ^{op}≠Δ, K-matrix K(z)=e^{-z d/du}.
- A_∞ bar W_{1+∞}: m_3(T,T,T)=-2T (cubic shadow α=2), m_4(T,T,T,T)=(40/27)T (quartic S_4=10/27), class M confirmed.
- K3 center obstruction: level 0: Obs=25/26, level 1: 1199/1248. >92% non-local. Controlled by BKM imaginary roots.
- Drinfeld center K3 Heisenberg: 49-dim double (24+24+1), Fock char 1/η^{48}, R=exp(ω^{ij}J_i⊗J_j*).
- Quantum toroidal Koszul dual: G(x;q^{-1})=1/G(x;q), φ: U_{q^{-1},t^{-1}}→U_{q,t}^{cop}, Miki commutes with inversion.
- E_n Koszul cascade: E_1→E_2→E_3 tower terminates at n=3 for CY inputs (E_1-stabilization at d≥4).
- Logarithmic center: class M ⟹ non-semisimple Drinfeld center (conjectural). Mock modular: κ_ch=-h|_{q^{-1/8}}.
- Categorical S-matrix: charge-2 S_{(2)}(u)=g(u+h_2)g(h_2-u), E_3 factorizes as S^{E_3}=S^{E_2}(u)S^{E_2}(v)S^{E_2}(u-v).
- Shadow class → QGL analytic type: G=polynomial, L=rational, C=convergent, M=Gevrey-1 divergent (Borel).

Latest frontier results (late April 2026):
- UNIVERSAL COPRODUCT: Δ_z(e_s) = Σ_{a+b+k=s} (-1)^k C(N_R-b,k) z^k e_a^L · e_b^R. Closed-form for ALL spins. z-degree at spin s is exactly s. Cross-terms: s-1 types.
- COASSOCIATIVITY IS TRIVIAL via Miura: T_0(u)·T_1(u-w)·T_2(u-w-z) is associative by commutativity of factors. Mode-level verification unnecessary. The algebraic proof IS Miura multiplicativity.
- bc SYSTEM: (1+t)^{3g} holds for fermionic class C (same charge conservation, 230 tests). Chain level differs: F(q)^6 vs P(q)^6. Cohomology identical.
- S³ ≠ S² × S¹: Hopf fibration is nontrivial. CY-A₃ framing cannot be decomposed. Relative chiral A_{K3,rel} bypasses by different mechanism (elliptic fibration).
- K3 KOSZUL CONDUCTOR = 0 (free-field/KM branch). NOT 13 (Virasoro) or 24 (lattice rank).
- κ_ch = χ^CY STATUS: proved at d=2 via Serre duality S_C=[2] killing one-loop correction. Status discrepancy in manuscript (conjectured in cy_to_chiral, proved in modular_koszul_bridge) — reconcile to ProvedHere.
- CoHA(A₁ McKay) = gl(1|1) ≠ W₂. Central charge coincidence (both c=0) does NOT imply isomorphism.

Deepest frontier results (late April 2026, final wave):
- A_∞ COPRODUCT THEORY: The shadow tower IS the A_∞ correction tower. Δ^{A_∞} = Δ^{Yangian} + ℏ²δ^{(3)} + ℏ³δ^{(4)} + ... where δ^{(k)} has coefficient = shadow S_k. Class G: truncation exact. Class M: infinite corrections. The shadow invariants are coproduct correction coefficients.
- z=0 RESOLVED: The adversarial "OPE singularity at z=0" objection is a CATEGORY ERROR. z is a Yangian spectral parameter, NOT a worldsheet coordinate. No OPE poles. Δ_0 is cocommutative, admits antipode, satisfies counit.
- FACTORIZATION ⊗: A ⊗_{E_1} B = colim_{z_1<z_2} A(z_1) ⊗ A(z_2). NOT symmetric (ordering matters). IS strictly associative (ordered config space contractible). np.kron = E_∞ quotient, kills quantum group.
- K3 MUKAI SIGNATURE: encoded in ω^{ij} = diag(+1,...,-1,...), NOT through imaginary h_i. Unitarity g·g(-)=1 unconditional (algebraic, no reality assumption).
- COPRODUCT COMBINATORICS: N(s,p) = s-p terms at z^p in spin s. GF: F(x,y) = x/((1-x)²(1-xy)). Total terms: s(s+1)/2. Subleading z^{s-2}: (s-1)ψ_2^R + J^L·J^R (universal).
- NON-ABELIAN sl₂: Coassociativity via TRACE of matrix Lax (fails for individual entries). Serre null vector: g_{i0}·g_{i1}=1 from affine imaginary root.
- κ=χ SCOPING: d=2 ProvedHere (modular_koszul_bridge), d≥3 Conjectured (cy_to_chiral). Already correct, no discrepancy.
- ZAMOLODCHIKOV TETRAHEDRON: COMPUTED NEGATIVE RESULT. The Yang R-matrix does NOT satisfy ZTE. The factored S_{ijk}=R_{ij}R_{ik}R_{jk} fails at O(κ²) where κ=h₁h₂h₃. At κ=0: trivially satisfied (Kapranov-Voevodsky). At generic κ: genuine obstruction. The correct E_3 3-particle S-operator requires CORRECTIONS beyond pairwise products. Engine: zamolodchikov_tetrahedron_engine.py (~1200 lines, 34 tests). THIS PROVES E_3 IS GENUINELY NONTRIVIAL.

Compute engines: holomorphic_cs_chiral_engine.py, k3_yangian.py, k3_double_current_algebra.py, drinfeld_center_k3_heisenberg.py, e3_two_parameter_rmatrix.py, categorical_s_matrix_e3.py, e2_koszul_heisenberg.py, e1_koszul_three_families.py, a_infinity_bar_w1inf.py, e1_chiral_bialgebra_engine.py, chiral_coproduct_spin3_engine.py, e3_bar_bc (230 tests). ~1,800+ tests.

## Dependencies on Vols I-II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I | Bar-cobar machine, Theta_A, kappa, five theorems, G/L/C/M | CY bar complex, modular trace, shadow depth |
| II | SC^{ch,top}, PVA descent, DK bridge, E_1 sector, H(T) | E_1 chiral theory, braided structure, bulk-boundary |

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol III
cd ~/chiral-bar-cobar && make fast                                # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Vol III tests
```

## Session Entry (Vol III additions)

1. Read ~/chiral-bar-cobar/CLAUDE.md first (canonical).
2. Then this file (kappa-spectrum, AP-CY1-8, AP-CY21-26).
3. Check AP113: bare kappa -> subscripted kappa_{ch,BKM,cat,fiber}.
4. Check AP114: do not cite theorems from 12 stub chapters.
5. CY-A: d=2 PROVED, d=3 PROGRAMME. Scope EVERY CY-A claim by dimension.
6. CY-C is CONJECTURE. NEVER \begin{theorem} for CY-C (AP40).
7. E_1-chiral bialgebra: the correct Hopf home. E_∞ vertex bialgebra loses R-matrix (AP-CY23).
8. E_3 bar: (1+t)^{3g} for class L,C ONLY. Fails for class M (AP-CY21).
9. Kummer route Steps 1-4 are PROVED (prop:kummer-orbifold). Step 5 conjectural.
10. Borcherds lift = resummation. The additive/multiplicative = perturbative/non-perturbative.

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
