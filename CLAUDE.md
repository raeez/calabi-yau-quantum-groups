# CLAUDE.md -- Volume III: CY Categories, Quantum Groups, and BPS Algebras

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol III-specific material.**

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_2-ChirAlg providing input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function.

~693pp, this repo, ~34,000 tests, ~460 engines. Seven parts with Part openers and 3 reading paths (algebraist, physicist, number theorist): I(Foundations) II(CY-to-Chiral Functor) III(E_n Hierarchy and Chiral Quantum Groups) IV(The K3 Yangian) V(CY Landscape) VI(Seven Faces of r_CY(z)) VII(Frontiers). Notation appendix (541 lines) and AP catalogue (668 lines) installed. 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites.

**4 genuine stub chapters** (<50 lines, AP114): quantum_groups_foundations (24), geometric_langlands (28), matrix_factorizations (29), modular_koszul_bridge (13). Develop or comment out. **3 thin chapters** (50-100 lines, may need development): cyclic_ainf (55), cy_categories (70), e1_chiral_algebras (90). **6 formerly listed stubs now developed** (>150 lines): hochschild_calculus, braided_factorization, drinfeld_center, fukaya_categories, quantum_group_reps, derived_categories_cy.

## Main Theorems

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROVED (inf-cat) | d=3 chain-level [m_3,B^{(2)}]!=0 resolved: not an obstruction in inf-cat framework (HH^{-2}_{E_1}=0). Goodwillie layers vanish. Space of E_3-liftings contractible. |
| **CY-B** (E_2-chiral Koszul duality) | d=3 PROVED | thm:cy-b-d3, thm:verdier-spectral-functor. CY-B1 (conductor): proved all classes. CY-B2 (braided equiv): proved all classes via Verdier spectral functor (D exact on tricomplexes => E_r(A)~E_r(A^!) at every page). 326 tests across cy_b_toward_proof, cy_b_d3_proof, cy_b_d3_final. |
| **CY-C** (Quantum group realization) | CONJECTURAL | C(g,q) = D(Y^+(g_{K3})) at abelian level. Three routes (chiral/BFN/MO). Rep(C)=Rep^{E_2}(Y) via BZFN. cy_c_quantum_group_k3 (104 tests). Uses \begin{conjecture}. NEVER \begin{theorem} |
| **CY-D** (Modular CY characteristic) | d=2 PROVED (h^{1,0}=0); d=3 PROGRAMME | kappa_ch=chi(O_X) proved for CY_2 with h^{1,0}=0 (K3). FALSE for odd d: chi(O_X)=0 for all CY_3 by Serre (prop:chi-O-vanishes-odd-d). kappa_ch(K3xE)=3!=0=chi(O). chi^CY is categorical, differs from chi(O_X). cy_d_kappa_d3 (76 tests). |
| **E_3 Koszul (Heisenberg)** | d=2 PROVED | thm:e3-koszul-heisenberg, 39 tests |
| **E_3 Koszul (Yangian)** | COHOMOLOGICAL PROVED | thm:e3-koszul-yangian, 36 tests |
| **E_2 Koszul (Heisenberg)** | d=2 PROVED | thm:e2-koszul-heisenberg, 49 tests |
| **Kummer route Steps 1-4** | PROVED | prop:kummer-orbifold, 85 tests |
| **E_1-chiral bialgebra axioms** | FOUNDATIONAL | sec:e1-chiral-bialgebras, 80 tests |
| **ZTE deformation cohomology** | PROVED | prop:zte-deformation-cohomology, 47 tests |
| **BKM weight universality** | PROVED | prop:bkm-weight-universal, kappa_bkm_universal (99 tests). kappa_BKM = c(0)/2 unconditional for all K3-fibered CY3. Does NOT depend on CY-A. |
| **Phi(K3) explicit** | d=2 PROVED | thm:phi-k3-explicit, phi_k3_explicit_evaluation (93 tests) |
| **K3 abelian Yangian presentation** | d=2 PROVED | thm:k3-abelian-yangian-presentation, k3_abelian_yangian_presentation (47 tests) |
| **Hopf fibration decomposition** | PROVED (negative) | prop:hopf-fibration-decomposition, S^3 framing non-decomposable (67 tests) |
| **Cyclic A_inf framing compat** | PROVED (corrected) | prop:cyclic-ainf-framing-compat. Original claim [m_k,B^{(2)}]=0 individually is FALSE for non-formal (obs_ainf_local_p2, 54 tests). Corrected claim: {b,B^{(2)}}=0 for TOTAL b=sum_k b_k, via Costello TCFT d^2=0 (operadic_tcft_mk_b2_engine, 43 tests). Cross-arity cancellation: {b_3,B^{(2)}} cancelled by {b_2,B^{(2)}} via Stasheff. Bidegree verification: stasheff_cancellation_obs_ainf (40 tests). Obs_Ainf=0 UNIVERSALLY. |
| **Cech-HTT coefficient convergence** | PROVED | prop:cech-htt-coefficient-convergence, cech_htt_convergence (64 tests) |
| **K3 quantum toroidal** | CONJECTURAL | conj:k3-quantum-toroidal, k3_quantum_toroidal (51 tests) |
| **MO R-matrix charge 2** | PROVED | prop:mo-rmatrix-charge2, mo_rmatrix_k3_charge2 (60 tests) |
| **Derived framing obstruction vanishes** | PROVED | thm:derived-framing-obstruction, derived_framing_obstruction (51 tests). [m_3,B^{(2)}]!=0 at chain level is NOT an obstruction in the infinity-categorical framework. Obstruction group HH^{-2}_{E_1}=0 by unit-connectedness. All Goodwillie layers vanish. Space of E_3-liftings is contractible. |
| **Shadow = A_inf coproduct tower** | PROVED | S_k = delta^{(k)} (coproduct correction at order k). Shadow-Feynman dictionary: L-loop = S_{L+1}. Explicit computation. |
| **Chiral CE complex** | PROVED | B(U^ch(L)) = CE_*(L). Chiral bar of universal chiral envelope = Chevalley-Eilenberg complex. chiral_ce_complex engine (66 tests). |
| **Class M E_3 bar dim** | PROVED | dim H*(B^{E_3}(A)) = 6^g for class M (closed form via Kunneth). Chain: P(q)^{6g}, cohomology: 6^g. |
| **CY-A_3 inf-categorical** | PROVED | CY-A_3 resolved in the infinity-categorical framework. Obstruction group HH^{-2}_{E_1}=0. Space of framings contractible. Chain-level [m_3,B^{(2)}]!=0 is NOT an obstruction. |
| **kappa_BKM = c_N(0)/2 universal** | PROVED | prop:bkm-weight-universal. The ONLY correct universal formula. Naive decomposition kappa_BKM = kappa_ch + chi(O_fiber) fails at N>=2. 99 tests. |
| **BKM Serre at D=3** | PROVED | Serre relations from BKM imaginary roots at discriminant D=3. Null vector g_{i0}*g_{i1}=1. k3_serre_relations engine (61 tests). |
| **CFG25 comparison** | VERIFIED | CFG (arXiv:2602.12412) E_3 from BV-quantised CS. Agreement at perturbative genus-0 level. Costello 5d verification at charge 4 (87 tests). CFG25 24% lift rate (76% require chain-level corrections). |
| **Super-Yangian Y(gl(4\|20))** | CONJECTURAL | BKM-to-Yangian lift from Mukai signature (4,20). k3_super_yangian (59 tests). |
| **6 routes to G(K3xE)** | PROGRAMME | Kummer, Borcherds, MO stable envelope, McKay, factorization homology, Costello 5d. Each produces partial data; none yet complete. |
| **Borcherds spectral flow** | PROVED | Spectral flow automorphisms of Y(g_{K3}) from Borcherds vertex operators. borcherds_vertex_yangian (75 tests). |
| **Shadow-Feynman dictionary** | PROVED | L-loop Feynman graph = shadow invariant S_{L+1}. Explicit at all loop orders. Class G: tree-level exact. Class M: all-loop. |
| **E_3 bar = 6^g** | PROVED | dim H*(B^{E_3}(A)) = 6^g for class M. Chain: P(q)^{6g}. Classes L,C: 2^{3g}=(1+t)^{3g}. |
| **Derived Satake** | CONJECTURAL | Derived geometric Satake for CY categories. Connects Phi to geometric Langlands. |
| **Tropical cluster** | PROGRAMME | Tropical cluster varieties as CY moduli. Shadow class varies over tropical limit. |
| **Chiral Verlinde** | CONJECTURAL | Chiral Verlinde formula for CY chiral algebras. Dim formula for conformal blocks. |
| **Hitchin quantization** | PROGRAMME | Hitchin system quantization via CY-to-chiral functor. |
| **BLLPR connection** | VERIFIED | Connection to Bringmann-Lovejoy-Mahlburg et al mock modular forms. Shadow = 24*eta^3 for W(2). |
| **Explicit ZTE correction T** | CONSTRUCTIVE | S^{corr} = S^{fact} + kappa^2*T. T exists (rank 35/36 in extended complex). Explicit construction from 1-dim kernel. |
| **p-adic Langlands** | CONJECTURAL | p-adic Langlands connection via p-adic CY motives. |
| **BFN Coulomb** | PROGRAMME | BFN Coulomb branch as CY chiral algebra source. |
| **Form factors** | PROGRAMME | Chiral form factors from bar complex on surfaces with punctures. |
| **Handle decomposition** | PROVED | K3 handle decomposition for factorization homology. 4 handles, Euler char 24. |
| **Stratified FH** | PROGRAMME | Stratified factorization homology for singular CY spaces. |
| **Mathieu moonshine** | PROGRAMME | M24 moonshine for K3 sigma model via chiral bar complex. Shadow = mock modular. |
| **Class M Borel summable** | PROVED | Class M shadow tower is Gevrey-1 divergent and Borel summable. Stokes automorphism from BKM imaginary root multiplicity. |
| **3 wrong proofs caught** | DOCUMENTED | (1) Bidegree decomposition for {b_k,B^{(2)}}=0 (flawed premise). (2) Tsygan formality argument (wrong scope). (3) kappa_BKM naive decomposition (numerical coincidence). All retracted with documentation. |
| **P_2(D) = 0: BKM Serre EXACT** | PROVED | Nekrasov + Lie algebra twist: second Serre polynomial vanishes identically. No higher corrections to imaginary root Serre relations. |
| **Borcherds spectral flow h=1 EXACT** | PROVED | Spectral flow at h=1 is an EXACT automorphism of Y(g_{K3}), not approximate. Verified against Borcherds product formula. |
| **CY-B push at d=3** | PROGRAMME (131 tests) | E_2-chiral Koszul duality extended to d=3 via inf-cat CY-A_3. Conditional on chain-level data for non-formal algebras. |
| **Chiral Satake for C^3** | PROVED | Derived geometric Satake for C^3 via chiral bar complex. 99 tests. Connects Phi(C^3) to geometric representation theory. |
| **Chain-level Incompatibility Theorem** | PROVED | mu_3 != 0 forces mu_2 = 0 on augmentation ideal. A_inf obstruction to simultaneous E_1 and E_inf structure at chain level. |
| **Notation appendix** | INSTALLED (541 lines) | Complete notation reference for Vol III. All symbols, conventions, cross-volume dictionary. |
| **AP catalogue** | INSTALLED (668 lines) | Full anti-pattern catalogue AP-CY1 through AP-CY40 with decision trees and counter-templates. |
| **10 proofs publication-upgraded** | DOCUMENTED | Kummer Steps 1-4, E_3/E_2 Koszul Heisenberg/Yangian, ZTE deformation cohomology, universal coproduct, Phi(K3) explicit, K3 abelian Yangian, derived framing obstruction. |
| **Part openers + reading paths** | INSTALLED | All 5 Part openers written. 3 reading paths (algebraist, physicist, number theorist). |
| **kappa_ch deep mechanism** | PROVED | Hodge-filtered supertrace: non-F^0 contributions killed by Hodge filtration. kappa_ch = str_{F^0}(q^{L_0}). |
| **CY-D at d=3 deep issue** | DOCUMENTED | chi(O_{K3xE}) = 0 != 3 = kappa_ch. CY-D formula kappa = chi(O_X) FAILS at d=3. The discrepancy is structural: kappa_ch counts the chiral anomaly (worldsheet), chi(O_X) counts the target-space anomaly (massless modes). For d=2: kappa_ch = chi(O_X)/2 PROVED (Serre duality). For d=3: kappa_ch and chi(O_X) are genuinely different invariants. Dimension-stratified formula: kappa_ch != chi(O_X) at odd d. |
| **ZTE T matrix COMPUTED** | PROVED | Exact rational T matrix solving S^{corr} = S^{fact} + kappa^2*T. 35 tests. Explicit entry-by-entry computation from 1-dim kernel of extended deformation complex. |
| **Shadow tower through m_8** | COMPUTED | 160 tests. Full shadow tower: S_3=2, S_4=10/27, ..., S_8=4144720/19683. Extends prior computation from m_5 to m_8. |
| **m_5 independent verification** | VERIFIED | m_5 independently verified from 5-point Wick contraction: G_5^{conn} = 775/5184. Cross-checks shadow tower at depth 5. |
| **Chiral volume conjecture** | CONJECTURAL | Formulated via Abel-Jacobi period. Connects chiral bar complex volume to period integrals of CY manifold. |
| **Mock modular K3 theorem** | d=2 PROVED | 4-step proof: (1) shadow = 24*eta^3, (2) mock theta transform, (3) Zwegers completion, (4) Borcherds lift. |
| **CY-D dimension-stratified** | DOCUMENTED | kappa_ch != chi(O_X) at odd d. Dimension-stratified formula replaces naive CY-D. |
| **CY-C abelian level** | CONSTRUCTIVE | C(g,q) = D(Y^+(g_{K3})) at abelian level. Explicit Drinfeld double of positive part of K3 Yangian. |
| **BKM Serre P_2 = 0 EXACT** | PROVED | Second Serre polynomial vanishes identically. No higher corrections. |
| **E_8 x E_8 structure function** | COMPUTED | degree-(24,24) structure function, c = 8+8+8 = 24. Mukai lattice decomposition via E_8 x E_8. |
| **Root-of-unity N=2** | COMPUTED | 324 modules (= 24*N^2*3/4 = 324 for N=2). Abelian S-matrix degenerate. Non-abelian K3 Yangian needed for modularity. |
| **Mathieu frame shape** | VERIFIED | Frame shape = twined bar Euler for all 25 M_24 conjugacy classes. Connects Mathieu moonshine to bar complex. |
| **Incompatibility Theorem (strengthened)** | PROVED | mu_3 != 0 implies mu_2 = 0 on augmentation ideal. Strengthened: holds at chain level for ALL non-formal A_inf algebras (class >= L). |

## The kappa-Spectrum (AP113, CRITICAL)

Bare "kappa" is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript:

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_ch | From chiral algebra A_C via Phi | 3 (= kappa_ch(K3) + kappa_ch(E) = 2+1) |
| kappa_BKM | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |
| kappa_cat | chi(O_X) = holomorphic Euler char | 0 = chi(O_{K3xE}); fiber value chi(O_{K3}) = 2 |
| kappa_fiber | From lattice/fiber structure | 24 (Mukai lattice rank) |

kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch and kappa_BKM. Full spectrum: {0,2,3,5,24}.

**Critical clarification**: kappa_cat(K3 x E) = chi(O_{K3xE}) = 0 (the TOTAL SPACE value by Kunneth: chi(O_K3)*chi(O_E) = 2*0 = 0). The value 2 = chi(O_{K3}) is kappa_cat of the K3 FIBER. The conjectural BKM decomposition uses the fiber value: kappa_BKM = kappa_ch + chi(O_{K3}) = 3 + 2 = 5.

**ADVERSARIAL RESULT (kappa_bkm_adversarial.py, 62 tests)**: The decomposition kappa_BKM = kappa_ch + chi(O_fiber) is a NUMERICAL COINCIDENCE for K3 x E (N=1). It FAILS for all Z/NZ-orbifolds with N >= 2: N=2 (Enriques) gives 4 != 2+1=3; N=3..8 give kappa_BKM in {3,2,2,1,1,1} != 3+2=5. The correct universal formula is **kappa_BKM = c_N(0)/2** (Borcherds weight theorem, NOT kappa_ch + kappa_cat). See rem:bkm-decomposition-adversarial in k3_times_e.tex.

**UNIVERSAL RESULT (kappa_bkm_universal.py, 99 tests, prop:bkm-weight-universal)**: kappa_BKM = c(0)/2 is a THEOREM (Borcherds 1998), PROVED unconditionally for ALL K3-fibered CY3s (Class A). It does NOT depend on CY-A. The proof chain: K3 elliptic genus -> orbifold averaging -> Borcherds weight theorem. For non-K3-fibered CY3s (Class B: quintic, C^3, conifold, local P^2), kappa_BKM is UNDEFINED; replacement invariants: kappa_BCOV = chi(X)/24 (compact), shadow depth (all, conditional on CY-A). CY3 families classified: 9 Class A (8 diagonal orbifolds + STU), 6 Class B. Monotonicity: kappa_BKM weakly decreasing in orbifold order N.

## HOT ZONE -- Top 10 Vol III Repeat Offenders

Read this section BEFORE any Edit. These are the AP-CY patterns that fire repeatedly across waves despite being catalogued. Each entry is an operational template, not prose. If you only read 80 lines of Vol III CLAUDE.md, read these.

### HZ3-1. AP-CY6/AP-CY14 (unconstructed A_X in theorem environment)

Decision tree, answer BEFORE writing `\begin{theorem}`:

```
Q1: Does the proof chain pass through A_X for d=3, G(X), C(g,q), or any
    object whose existence is part of the d=3 programme?
    YES -> CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction).
           Results depending on CY-A_3 via the inf-cat framework: \begin{theorem} OK.
           Results requiring CHAIN-LEVEL A_X at d=3 (not just inf-cat existence):
           \begin{conjecture} + \ClaimStatusConditional. State dependency.
    NO  -> Q2
Q2: Does it pass through A_X for d=2 (CY-A_2 proved)?
    YES -> \begin{theorem} or \begin{proposition} OK; cite CY-A explicitly.
    NO  -> Q3
Q3: Pure categorical / VOA / Yangian statement (no functor invocation)?
    YES -> \begin{theorem} or \begin{proposition} OK; classical proof.
Q4: Does it require C(g,q) (quantum group realization, CY-C)?
    YES -> \begin{conjecture}. CY-C remains CONJECTURAL.
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than retract.
```

Vol III default: `\begin{conjecture}` for CY-C-dependent results. CY-A_3 results OK as theorems if proof chain only needs inf-cat existence. The 11+ instances fixed across 4 commits prove that the LLM pattern-matches on "if X then Y" logical form without checking whether X exists.

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
AP-CY6: A_X for CY3 EXISTS in the inf-categorical framework (thm:derived-framing-obstruction, April 2026). Chain-level explicit construction remains open for non-formal algebras. Results using inf-cat existence: \begin{theorem} OK. Results requiring chain-level explicit A_X: \begin{conjecture}. **Previous version** (pre-April 2026): "A_X does NOT exist" -- this is SUPERSEDED by the inf-cat proof.
AP-CY7: CoHA != E_1-chiral algebra. CoHA is associative. "E_1-sector of G(X)" assumes G(X) exists (AP43).
AP-CY8: Borcherds denominator != bar Euler product. Identification requires CY-to-chiral functor. For K3 x E: observation, not theorem.

### Empirical (AP-CY9-13, from 50-commit error archaeology)
AP-CY9: Jacobi form discriminant constraint. For phi_{k,m} of index m, only discriminants D with D=0 or D=3 mod 4 (m=1) can appear. NEVER fill coefficient table with sequential D-values. Verify discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention, NOT 1.
AP-CY10: Flop != Koszul dual. Birational flop X->X^+ is derived equivalence PRESERVING kappa. Koszul dual A^! has kappa(A)+kappa(A^!)=rho_K. Flop exchanges chambers; Koszul exchanges algebra/coalgebra. kappa(A_X)=kappa(A_{X+}) for flop, NOT kappa(A_X)+kappa(A_{X+})=0.
AP-CY11: Conditional d=3 transitivity. **Updated**: CY-A_3 is now PROVED (inf-cat). Results chaining through CY-A_3 are no longer conditional. However, results depending on CY-C (quantum group realization) or chain-level explicit A_X remain conditional. DEFAULT for CY-C-dependent results: \begin{conjecture}.
AP-CY12: Shadow class from full computation. G/L/C/M must be determined by computing full shadow tower, NOT by counting generators. Non-formality (m_3!=0) does NOT by itself determine shadow depth. local P^2 is class M (infinite depth), not class L.
AP-CY13: Cross-volume Part number staleness. After ANY Part restructuring in ANY volume, grep ALL THREE volumes for stale Part references. Part numbers are the most fragile cross-reference. Use \ref{part:...} exclusively, never hardcode. **Strengthened**: run grep -rn 'Part~[IVXL]' chapters/ notes/ and verify EVERY match. 7+ stale refs survived a single restructuring.

### Deep Empirical (AP-CY14-19, from 100-commit deep archaeology)
AP-CY14: **Updated post CY-A_3 proof.** A_X at d=3 now EXISTS (inf-cat). G(X) and C(g,q) remain unconstructed. Any statement whose proof chain passes through G(X) or C(g,q) MUST use \begin{conjecture}. Statements using only CY-A (any d) may use \begin{theorem}. The LLM pattern-matches on logical structure ("if X then Y") without checking whether X exists. 11+ instances fixed across 4 commits.
AP-CY15: README scope inflation beyond .tex ground truth. README must not claim "verified" or "proved" for structural analogies or pattern matches. The README accumulates stronger claims than the .tex supports because the LLM optimizes for impressiveness. After README edits, verify every "proved"/"verified" against corresponding \ClaimStatus tag.
AP-CY16: Matrix size conflation in group quotients. Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5. O(Lambda^{3,2}) quotient by +/-I_5 (5x5). When two groups of different rank appear in the same formula, the LLM harmonizes subscripts to whichever appears more frequently.
AP-CY17: MF(W) CY dimension is n-2, NOT n-1. For W: A^n -> A^1, MF(W) is CY_{n-2} (Dyckerhoff). ADE in 2 variables: CY_0 (semisimple). Need 4 variables for CY_2. The n-1 vs n-2 error changes which families are CY_2.
AP-CY18: Lattice theta series comparison. Verify q-power divergence by DIRECT COMPUTATION. Leech theta: minimum norm^2=4, first correction at q^2 not q^1. The match with 1/eta^24 extends through q^1. Never conflate j(tau) coefficients with V_Lambda character coefficients.
AP-CY19: A-hat genus argument halving. A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi (first pole of sin(x/2) at x=2*pi). NEVER drop the /2 in the argument, which gives spurious radius pi. Appeared in 3+ independent computations.
AP-CY20: Normal bundle vs spectral parameters. The Z x Z grading from the normal bundle N_{C/Y} of a curve C in a CY threefold Y connects to the quantum toroidal parameters (q,t) through the Omega-background, NOT through the bundle grading directly. The intermediary mechanism (equivariant localization on the Omega-background, Nekrasov partition function, refinement) must be stated explicitly. NEVER write "N_{C/Y} grading = (q,t) parameters" as a direct identification. Counter: before any claim relating normal bundle gradings to quantum group parameters, name the intermediary mechanism and cite the equivariant/Omega-background passage.

### CY-D Correction (AP-CY34, from kappa_ch investigation)
AP-CY34: kappa_ch != chi(O_X) at odd d. For ANY compact CY_d with d odd, chi(O_X) = 0 by Serre duality (h^{0,q}=h^{0,d-q} and pairwise cancellation). Therefore kappa_ch = chi(O_X) is FALSE whenever kappa_ch != 0. Known falsifications: E (d=1, kappa=1), abelian surface (d=2, kappa=2, h^{1,0}=2), K3xE (d=3, kappa=3). The formula kappa_ch = chi(O_X) is PROVED ONLY for CY_2 with h^{1,0}=0 (K3, etc.) where HH_{-1}=0 and the Serre argument kills the quantum correction. For d>=3: HH_{-1} = h^{2,0}+h^{1,1}+h^{0,2} is ALWAYS nonzero (h^{1,1}>=1 for projective), so the Serre argument NEVER applies. The correct CY-D uses the categorical chi^CY, distinct from chi(O_X). Counter: NEVER write kappa_ch = chi(O_X) outside the scope d=2, h^{1,0}=0. At d=3: use the dimension-stratified formula (conj:cy-kappa-identification). 76 tests in cy_d_kappa_d3.py.

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
AP-CY21: E_3 bar dimensions RESOLVED. The tricomplex model P(q)^{3g} gives CHAIN-level dimensions for all classes. COHOMOLOGY by shadow class: class G: P(q)^{3g} (formal, infinite). Class L: (1+t)^{3g} = 2^{3g}. Class C: (1+t)^{3g} = 2^{3g} (charge conservation kills d_4). **Class M: 6^g** (PROVED, closed form via Kunneth; d_4 survives giving 6=2*3 per handle). NEVER claim (1+t)^{3g} for class M. Counter: state the shadow class before claiming E_3 bar cohomology.
AP-CY22: Miki automorphism is algebra-specific, NOT operadic. The S_3 permutation of (q_1,q_2,q_3) comes from the Weyl group of the CY torus, not from the E_3 operad in general. Counterexample: k[x]/(x^2) is E_3 but has no Miki. Counter: never derive Miki from the E_3 operad alone; always state it requires the specific algebra U_{q,t}(gl_hat_hat_1).
AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
AP-CY24: Docstring ground-truth confabulation. Agents produce correct CODE but fabricate "ground truth" values in docstrings. The function computes correctly; the docstring claims wrong values for n ≥ 4. Counter: verify EVERY numerical value in docstrings against the actual function output. Especially dangerous for OEIS sequences.
AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
AP-CY26: Verdier duality parameter inversion does NOT invert σ_2. For the Heisenberg, k^! = -k comes from Shapovalov form transposition (Verdier duality transposes the inner product), NOT from σ_2(-h_i) = -σ_2 (FALSE: σ_2 is degree-2 homogeneous, hence EVEN under h_i → -h_i). Counter: derive k^! from Shapovalov/Verdier, not from σ_2 inversion.

### Mined from 180-Agent Swarm (AP-CY27-AP-CY33, April 2026)
AP-CY27: Agent sandbox non-persistence. Background agents report successful file writes but files do NOT persist to the main working tree (sandbox isolation). ALWAYS verify file existence with `ls` after agent completion. Use foreground agents or direct `Write`/`Bash cat` for critical file creation. Three engines were "written" by agents and verified passing inside the sandbox, but did not exist on disk.
AP-CY28: Pole-unsafe test points. When testing rational structure functions g(z) with poles at z=±h_i, test points MUST avoid these values. For h=(1,-2,1): poles at z=±1,±2. The default test point z=2 with h₁=2 gives φ(2)=0, hence g₀₁(2)=1/0. Counter: choose test points far from all ±h_i, e.g., use h=(37,41,-78) for large-parameter safety.
AP-CY29: Wrong-repo file writes. Agents sometimes write files to the WRONG volume's directory. An sl₂ Serre engine was written to ~/chiral-bar-cobar/compute/ (Vol I) instead of ~/calabi-yau-quantum-groups/compute/ (Vol III). Counter: after any agent file write, verify the FULL PATH includes the correct volume's repo root.
AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
AP-CY31: Spectral z ≠ worldsheet z. The Drinfeld coproduct Δ_z uses a Yangian spectral parameter (shift of transfer matrix argument u→u-z). The vertex algebra OPE T(z)T(w)~c/2·(z-w)^{-4} uses a worldsheet insertion coordinate. These are DIFFERENT mathematical objects. Setting z=0 in Δ_z removes the spectral shift (no OPE singularity); setting z→w in the OPE produces poles. Counter: before any z=0 argument, state whether z is spectral or worldsheet. Conflation is the source of the adversarial "z=0 singularity" objection (resolved: rem:z-spectral-vs-worldsheet).
AP-CY32: Reorganisation ≠ bypass. The 6d factorization homology route appears to bypass CY-A₃, but each subproblem (local E₃ algebra for compact targets, handle decomposition of K3, VOA identification of output) secretly requires the same chain-level data that CY-A₃ demands. The route REORGANISES the conjecture into subproblems but solves NONE of them independently. Counter: before claiming a bypass, verify that every subproblem in the alternative route is resolved independently of the original conjecture.
AP-CY33: Chain-level ≠ rational. E₃ structure is genuine at the CHAIN level but collapses to E₂ under Kontsevich formality (rational coefficients). The physical content (Miki automorphism, factorization homology, tetrahedron corrections) lives at the chain level. Formality destroys it. Counter: always state whether a claim about E_n structure is at the chain level or the rational/formal level. Claims about "E₃ being trivial" that invoke formality are true RATIONALLY but miss the chain-level content that the physics requires.
AP-CY34: RESOLVED via Costello's operadic TCFT. Original gap: cyclic invariance controls adjacent contractions but not non-adjacent. The CORRECTED claim: {b, B^{(2)}} = 0 for the TOTAL A-infinity Hochschild differential b = sum_k b_k. Individual {b_k, B^{(2)}} need NOT vanish; only their sum does. Proof: Costello Theorem A (arXiv:math/0412149) + open-closed TCFT extension + d^2=0 in moduli chain complex. The non-adjacent contractions cancel cross-arity: {b_3, B^{(2)}} is cancelled by {b_2, B^{(2)}} via the Stasheff A-infinity relations (which ARE d^2=0 expanded by arity). Explicit computation (obs_ainf_local_p2.py, 54 tests) confirms {b_3, B^{(2)}}([a|a|a|a|b]) = 2*alpha*[b] != 0 individually, confirming the original per-k claim is FALSE. But the TOTAL {b, B^{(2)}} = 0 by the operadic argument. Obs_Ainf = 0 UNIVERSALLY. CY-A_3 subsequently PROVED (inf-cat, thm:derived-framing-obstruction). PREVIOUS PROOFS RETRACTED: bidegree decomposition (flawed premise), Tsygan formality (wrong scope). Engine: operadic_tcft_mk_b2_engine.py (43 tests). See rem:adversarial-audit-cyclic-ainf in cy_to_chiral.tex.

### Final Session APs (AP-CY35-AP-CY40, from 170-agent final wave, April 2026)
AP-CY35: Superalgebra rank inflation. Agents assign gl(N|M) structure to lattice-graded algebras based on signature matching alone. The Mukai lattice signature (4,20) does NOT automatically produce gl(4|20). The super-Yangian Y(gl(4|20)) is CONJECTURAL. Counter: super structures require explicit Lie bracket verification, not just grading compatibility.
AP-CY36: RTT-OPE dictionary incompleteness. The RTT presentation and the OPE are NOT interchangeable without specifying normal ordering. The translation requires explicit contour deformation and regularization. Counter: always specify which presentation and whether a dictionary exists.
AP-CY37: CFG25 lift rate is 24%, not 100%. Costello-Francis-Gwilliam E_3 agrees with programme at perturbative genus-0 level, but 76% of results require chain-level corrections beyond their filtered E_3. Counter: never cite CFG25 as full confirmation; specify the perturbative genus-0 scope.
AP-CY38: Inf-categorical proof ≠ chain-level construction. CY-A_3 is PROVED in the inf-cat framework (HH^{-2}_{E_1}=0, Goodwillie vanishing), but this does NOT produce an explicit chain-level A_X. Results requiring explicit chain-level data (mode computations, OPE coefficients) need additional work. Counter: distinguish "exists by abstract nonsense" from "explicitly constructed."
AP-CY39: Borel summability ≠ convergence. Class M shadow tower is Borel SUMMABLE (Gevrey-1), not convergent. The Borel sum defines a unique non-perturbative completion, but the original series DIVERGES. Counter: never write "converges" for class M; write "Borel summable."
AP-CY40: Multiple routes ≠ redundancy. The 6 routes to G(K3xE) (Kummer, Borcherds, MO, McKay, FH, Costello) produce DIFFERENT partial data. They are not independent confirmations of the same result. Counter: specify what each route constructs and what it does NOT construct.

## 6d Holomorphic CS Programme (established April 2026)

The Costello programme constructs chiral quantum groups from holomorphic CS at each dimension:
- 3d hol CS → Kac-Moody (PROVED, Costello-Gwilliam)
- 5d hol CS → Affine Yangian (PROVED, Costello 2013)
- 6d hol theory → Quantum toroidal (CONJECTURAL, Costello-Francis-Gwilliam route)

Key results established in Vol III:
- E_1-chiral bialgebra axioms (Section 7 of e1_chiral_algebras.tex, ~400 lines, NEW MATH)
- E_3 bar cohomology: (1+t)^{3g} = 2^{3g} for classes L,C; 6^g for class M (PROVED)
- Kummer route: ∫_{K3} F via CY-A_2 only (Steps 1-4 PROVED, Step 5 conjectural)
- K3 Yangian: degree-(24,24) structure function from Mukai lattice
- Borcherds lift = resummation (additive Saito-Kurokawa = perturbative, multiplicative Borcherds = non-perturbative)
- Class M = mock modular (κ_ch = -h|_{q^{-1/8}})
- Center-hocolim obstruction: >92% of K3×E Drinfeld center invisible to local charts
- MO stable envelopes bypass center-hocolim for global braiding
- Two-parameter R-matrix: R_ch(u,v) = R_1(u)R_2(v)R_12(u-v) (Zamolodchikov factorization)
- E_2 → E_3 promotion is the DERIVED center (higher Deligne), not iterated Drinfeld center

K3 quantum toroidal programme (April 2026, 53-agent session):
- **Phi(K3) explicit** (thm:phi-k3-explicit): CY-to-chiral functor evaluated explicitly on K3, producing 24-generator Heisenberg with Mukai pairing. 93 tests.
- **K3 abelian Yangian** (thm:k3-abelian-yangian-presentation): Y(g_{K3}) presented with RTT relations from Mukai signature (4,20). Degree-(24,24) structure function. 47 tests.
- **Super-Yangian Y(gl(4|20))**: conjectural BKM-to-Yangian lift. The Mukai lattice signature (4,20) suggests gl(4|20) superalgebra. Borcherds vertex operators provide spectral flow. k3_super_yangian engine (59 tests).
- **K3 quantum toroidal** (conj:k3-quantum-toroidal): conjectural U_{q,t}(gl_hat_hat_1)^{K3} from double loop. k3_quantum_toroidal engine (51 tests).
- **MO R-matrix at charge 2** (prop:mo-rmatrix-charge2): Maulik-Okounkov stable envelope R-matrix computed for Hilb^2(K3). Matches K3 Yangian R-matrix at specific Omega-background. 60 tests.
- **Borcherds vertex Yangian**: spectral flow automorphism of Y(g_{K3}) from Borcherds vertex operators. borcherds_vertex_yangian engine (75 tests).
- **Cech-HTT convergence** (prop:cech-htt-coefficient-convergence): CY-A₃ coefficient series convergent for all smooth CY₃ with finite Leray covers. Radius >= 1/(4||s.delta||). 64 tests.
- **Hopf fibration decomposition** (prop:hopf-fibration-decomposition): S³ framing CANNOT decompose along S² x S¹. CY-A₃ irreducibly 3-dimensional. 67 tests.
- **kappa_BKM adversarial**: kappa_BKM = c_N(0)/2 is the ONLY correct universal formula. Decomposition kappa_BKM = kappa_ch + chi(O_fiber) fails at N>=2. 62 tests.
- **ZTE correction existence** (prop:zte-deformation-cohomology): Extended deformation complex with ternary corrections has rank 35/36 — obstruction TRIVIAL. S^{corr} EXISTS. 47 tests.
- **K3 RTT-OPE dictionary**: translation between RTT presentation and OPE algebra. k3_rtt_ope_dictionary engine (52 tests).
- **ADE Yangian level-1**: Y(g) at level 1 for all ADE types from McKay correspondence. ade_yangian_level1 engine (63 tests).
- **K3 Serre relations**: null vector constraints on the K3 Yangian from BKM imaginary roots. k3_serre_relations engine (61 tests).
- **K3 quantum determinant**: quantum determinant q-det(T(u)) for K3 Yangian. k3_quantum_determinant engine (76 tests).

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
- ZTE DEFORMATION COHOMOLOGY: The obstruction lives in H^2 of the deformation complex C^0(dim 2) -> C^1(dim 6) -> C^2(dim 20). Chain complex verified (d^1.d^0=0). Cohomology: H^0=2, H^1=1, H^2=15. ZTE obstruction = l_3(r,r,r) (ternary L_infinity bracket; l_2 vanishes per face since YBE holds). Pairwise H^2 nontrivial (rank 30/36): R-matrix deformations INSUFFICIENT. Extended H^2 with ternary corrections: rank 35/36, obstruction TRIVIAL. THEREFORE: S^{corr} = S^{fact} + kappa^2 * T EXISTS. Engine: zte_deformation_cohomology.py, 47 tests. Prop prop:zte-deformation-cohomology.

Final results (late April 2026, 180-agent wave):
- FACTORIZATION-HOMOLOGY COPRODUCT (180 lines, e1_chiral_algebras.tex): For GENERAL CY (non-toric), coproduct from Ran space excision. Works for quintic, complete intersections. Conjectural agreement with Miura for toric.
- VOL I CROSS-REF: rem:shadow-ainfty-coproduct-vol3 (higher_genus_complementarity.tex). Shadow S_k = A_∞ correction δ^{(k)}.
- VOL II CROSS-REF: rem:e1-chiral-bialgebra-vol3 (foundations_recast_draft.tex). E_1-chiral bialgebra on open SC^{ch,top} colour.
- ALL BUILDS PASS: Vol I (2636pp), Vol II, Vol III. All tests pass.

K3 quantum group session results (April 2026, 53-agent wave, ~62pp new, ~3,600 new tests):
- PHI(K3) EXPLICIT (thm:phi-k3-explicit): CY-to-chiral functor computed on K3. Rank-24 Heisenberg, Mukai pairing (4,20). Bar Euler = eta^{24}. 93 tests.
- K3 ABELIAN YANGIAN (thm:k3-abelian-yangian-presentation): RTT presentation, degree-(24,24) structure function. Quantum determinant central. 47 tests.
- SUPER-YANGIAN Y(gl(4|20)): conjectural BKM-to-Yangian lift. Borcherds vertex = spectral flow. 59 tests.
- K3 QUANTUM TOROIDAL (conj:k3-quantum-toroidal): U_{q,t}(gl_hat_hat_1)^{K3}. Miki from CY torus Weyl group. 51 tests.
- MO R-MATRIX CHARGE 2 (prop:mo-rmatrix-charge2): stable envelope R on Hilb^2(K3) matches K3 Yangian. 60 tests.
- BORCHERDS VERTEX SPECTRAL FLOW: e^{alpha.phi} spectral flow of Y(g_{K3}). 75 tests.
- CECH-HTT CONVERGENCE (prop:cech-htt-coefficient-convergence): HTT series convergent for ALL smooth CY₃. Radius >= 1/(4||s.delta||). 64 tests.
- S³ FRAMING NON-DECOMPOSABLE (prop:hopf-fibration-decomposition): Hopf fibration nontrivial, CY-A₃ irreducible. 67 tests.
- KAPPA_BKM UNIVERSAL: kappa_BKM = c_N(0)/2 only. Naive decomposition fails N>=2. 62 tests.
- ZTE CORRECTION EXISTS: Extended complex rank 35/36, S^{corr} constructible. 47 tests.
- K3 SERRE + QUANTUM DET: Imaginary root nulls + q-det(T(u)). 61+76 tests.
- ADE YANGIAN LEVEL 1: All ADE via McKay. 63 tests.
- COSTELLO 5d: hCS -> Yangian verified charge 4. 87 tests.
- W2 TRIPLET MOCK: Complete mock modular for W(2), shadow = 24*eta^3. 70 tests.
- SHADOW CLASS VARIATION: G at large volume, M at conifold. 88 tests.

129-agent comprehensive session results (April 2026):
- **CY-A_3 RESOLVED (inf-cat)**: thm:derived-framing-obstruction. The [m_3,B^{(2)}] saga: individual {b_k,B^{(2)}}!=0 for non-formal algebras (FALSE per-k, obs_ainf_local_p2.py 54 tests), but TOTAL {b,B^{(2)}}=0 universally via Costello TCFT operadic argument. Cross-arity cancellation: {b_3,B^{(2)}} cancelled by {b_2,B^{(2)}} via Stasheff. The chain-level failure is NOT an obstruction in the inf-categorical framework: HH^{-2}_{E_1}=0 by unit-connectedness. All Goodwillie layers vanish. Space of E_3-liftings is contractible. Engines: derived_framing_obstruction (51 tests), operadic_tcft_mk_b2_engine (43 tests), stasheff_cancellation_obs_ainf (40 tests).
- **SHADOW = A_inf COPRODUCT TOWER**: S_k = delta^{(k)} is PROVED with explicit computation. The shadow-Feynman dictionary: L-loop = S_{L+1}. Class G: truncation exact (0 corrections). Class M: infinite corrections (divergent, Borel summable). The shadow tower IS the A_inf correction tower for the Drinfeld coproduct.
- **CHIRAL CE COMPLEX**: B(U^ch(L)) = CE_*(L) PROVED. The chiral bar of the universal chiral envelope of a Lie algebra L equals the Chevalley-Eilenberg complex. chiral_ce_complex engine (66 tests).
- **CLASS M E_3 BAR**: dim = 6^g (closed form). Chain level: P(q)^{6g}. Cohomology: 6^g via Kunneth (d_4 differential survives, giving 6 = 2*3 per handle). NOT (1+t)^{3g} = 2^{3g} (that is classes L,C only).
- **kappa_BKM UNIVERSAL**: kappa_BKM = c_N(0)/2 is the ONLY correct formula (Borcherds weight theorem). The naive decomposition kappa_BKM = kappa_ch + chi(O_fiber) is a NUMERICAL COINCIDENCE for N=1 (K3 x E). Fails for all orbifolds N>=2. 99 tests.
- **BKM SERRE AT D=3**: Serre relations from BKM imaginary roots at discriminant D=3. The null vector g_{i0}*g_{i1}=1 from affine imaginary root. k3_serre_relations engine (61 tests).
- **BKM SERRE HIGHER ORDER**: P_2(D) = 0 for ALL D. The deformed OPE exponent P(D,eps) = -2D + eps*(D^2-2D) is EXACT to all orders in eps (not just leading-order). Proof: 1d Omega-background on E has eps_1*eps_2 = eps*0 = 0, killing the Nekrasov second-order correction. Spectral flow h_eps = (D+1)-eps*D is EXACT (Lie algebra twist L_0+eps*J_0 is linear in eps). Consequences: 182-generator Serre kernel is EXACT, D=3 triple pole is EXACT, D=0/D=4 marginal cases are EXACTLY marginal (resolution requires nonperturbative data). Engine: bkm_serre_higher_order.py (70 tests, cross-checked against bkm_deformed_serre.py and borcherds_vertex_yangian.py).
- **CFG25 COMPARISON**: Costello-Francis-Gwilliam (arXiv:2602.12412) construct filtered E_3 from BV-quantised CS. Their factorisation homology trace = RT link invariant. Agreement at perturbative genus-0 level verified. costello_5d_verification engine (87 tests).
- **AP-CY34 FULL SAGA**: [m_3,B^{(2)}]=0 per-k is FALSE (discovered via obs_ainf_local_p2). {b,B^{(2)}}=0 for total b via Costello TCFT is TRUE. Previous proofs (bidegree decomposition, Tsygan formality) RETRACTED. The correct argument: Costello Theorem A + open-closed TCFT extension + d^2=0 in moduli chain complex. Non-adjacent contractions cancel cross-arity via Stasheff A_inf relations. Obs_Ainf=0 UNIVERSALLY.

FINAL documentation wave results (April 2026):
- **P_2(D) = 0: BKM SERRE IS EXACT**: The second Serre polynomial vanishes identically via two independent arguments: (1) Nekrasov 1d Omega-background on E has eps_1*eps_2=0, killing all higher-order corrections; (2) Lie algebra twist L_0+eps*J_0 is linear in eps, so spectral flow h_eps is exactly linear. Consequence: the 182-generator Serre kernel computed at leading order is the FULL kernel. No perturbative corrections at any order. bkm_serre_higher_order.py (70 tests).
- **BORCHERDS SPECTRAL FLOW h=1 EXACT**: The h=1 spectral flow is an exact automorphism, not a leading-order approximation. Verified against Borcherds product formula through 10 Fourier coefficients.
- **CY-B PUSH AT d=3**: E_2-chiral Koszul duality extended to d=3 using inf-cat CY-A_3. Bar-cobar adjunction on CY_3 categories established at the infinity-categorical level. 131 new tests. Chain-level bar complex construction remains conditional on explicit framing data.
- **CHIRAL SATAKE FOR C^3**: Derived geometric Satake equivalence proved for C^3 = simplest toric CY_3. Connects Phi(C^3) = W_{1+inf} to Rep(Y(gl_1^)). 99 tests.
- **CHAIN-LEVEL INCOMPATIBILITY THEOREM**: For non-formal A_inf algebras (class >= L), mu_3 != 0 FORCES mu_2 = 0 on the augmentation ideal (at the chain level). The E_1 product and the A_inf corrections cannot coexist on the same graded piece. This is the algebraic reason why the E_1-chiral bialgebra lives on B^{ord}(A) (where mu_2 is the bar differential) and NOT on A itself (where mu_3 != 0 corrupts the product).
- **NOTATION APPENDIX**: 541-line notation appendix installed. All symbols, conventions, cross-volume dictionary, kappa-spectrum table, shadow class table, CY dimension table.
- **AP CATALOGUE**: 668-line anti-pattern catalogue installed. AP-CY1 through AP-CY40 with full decision trees and counter-templates. Cross-referenced to Vol I/II APs.
- **10 PROOFS UPGRADED TO PUBLICATION STANDARD**: Kummer Steps 1-4, E_3/E_2 Koszul (Heisenberg and Yangian), ZTE deformation cohomology, universal coproduct, Phi(K3) explicit, K3 abelian Yangian presentation, derived framing obstruction vanishing, chiral CE complex. All proofs now have complete hypothesis-conclusion blocks, explicit proof environments, and multi-path verification.
- **PART OPENERS + READING PATHS**: All 5 Part openers written with motivating examples and dependency maps. 3 reading paths: (1) algebraist (operadic, bar-cobar, Koszul), (2) physicist (BPS, holography, anomaly), (3) number theorist (modular forms, Borcherds, mock modular).
- **KAPPA_CH DEEP MECHANISM**: The Hodge-filtered supertrace str_{F^0}(q^{L_0}) kills all non-F^0 contributions. For d=2 CY: F^0 = H^{0,0} + H^{2,0}, and str_{F^0} = chi(O_X)/2. For d=3: F^0 picks up different Hodge numbers, giving kappa_ch != chi(O_X)/2. The mechanism: Serre duality S_C = [d] acts on F^p by F^p -> F^{d-p}, and the supertrace over the full Hodge diamond cancels non-F^0 terms in pairs.
- **CY-D AT d=3 DEEP ISSUE**: chi(O_{K3xE}) = 0 but kappa_ch(K3xE) = 3. For CY-D to hold at d=3, the formula must be kappa_ch = str_{F^0}(q^{L_0}), NOT kappa_ch = chi(O_X). The discrepancy: chi(O_X) is the target-space anomaly (counting massless modes); kappa_ch is the worldsheet anomaly (counting the chiral algebra's effective central charge). These coincide at d=2 (by Serre duality) but diverge at d=3.

## Roadmap: The Platonic Ideal (post-CY-A_3, April 2026)

The programme constructs chiral quantum groups from CY geometry via holomorphic CS. The architecture:
```
CY_d category --Phi--> E_1-chiral algebra --B^{ord}--> bar complex --D_Ran--> Koszul dual A^! --Rep^{E_2}--> chiral QG
```
At each step: E_1 (ordered) is the primitive; E_2 (braided) via Drinfeld center; E_3 (6d hCS) via derived center; E_∞ (symmetric) kills Hopf.

Status by dimension:
- d=1: E_∞ (commutative). PROVED. Trivial.
- d=2: E_2 (braided). PROVED (CY-A_2). K3 lattice VOA, Phi_2(K3)=H_Muk, κ_ch=2.
- d=3: E_1 (ordered). PROVED (inf-cat, CY-A_3). Chain-level [m_3,B^{(2)}]!=0 resolved as non-obstruction (HH^{-2}_{E_1}=0, Goodwillie vanishing). K3 abelian Yangian theorem (6-part presentation). 6 routes to G(K3xE). Yangian/toroidal from CoHA.

### Ideal seven-part structure (rearchitecture target)

Full proposal: notes/vol3_rearchitecture_proposal.tex. Summary:

```
Part I:   Foundations (CY categories, cyclic A_inf, Hochschild)     -- 4 chapters
Part II:  CY-to-Chiral Functor (construction, [m_3,B^(2)] saga, kappa) -- 3 chapters
Part III: E_n Hierarchy & Chiral Quantum Groups (E_1, E_2, E_n, QG, Drinfeld, braided) -- 6 chapters
Part IV:  The K3 Yangian (Mukai lattice, Phi_2(K3), abelian Yangian, K3xE, 6 routes, Kummer) -- 6 chapters
Part V:   CY Landscape (C^3, toric, toroidal/elliptic, Fukaya, MF, QG reps) -- 6 chapters
Part VI:  Seven Faces of r_CY(z) (bar-cobar bridge, 7 faces, modular Koszul) -- 3 chapters
Part VII: Frontiers (nonabelian Yangian, ZTE, Langlands, root of unity) -- 4 chapters
```

Total: ~32 chapters + appendices, ~693pp current (exceeds 590pp target due to K3 Yangian expansion and shadow tower depth computations).

Key structural changes from current 5-part layout:
1. Part I shrinks (E_n/chiral material moves to Part III).
2. Part II is the CY-to-chiral functor with CY-A_3 as theorem + the [m_3,B^{(2)}] story.
3. Part III absorbs current Part II's quantum/braided material + E_n from Part I.
4. Part IV is NEW: K3 Yangian elevated from subsections to a full part (the mathematical climax).
5. Part V is current Part III minus K3 material.
6. Part VI is current Part IV.
7. Part VII replaces current Part V with genuine frontiers (CY-A_3 no longer frontier).

Logical dependencies: I -> II -> III -> {IV, V} -> VI -> VII. Parts IV and V are independent.

### Five load-bearing open problems (updated April 2026, ~230-agent final session)

1. **CY-B (E_2-chiral Koszul duality)**: PROGRAMME (131 tests). The bar-cobar adjunction B/Omega on E_2-chiral algebras from Phi. Depends on CY-A (now proved). Extended to d=3 via inf-cat CY-A_3. Chain-level conditional on explicit framing data for non-formal algebras. The next structural theorem after CY-A.
2. **Nonabelian K3 Yangian**: The passage from abelian Y(g_{K3}) (PROVED, 24 generators, thm:k3-abelian-yangian-presentation) to the full nonabelian Yangian. Matrix Miura, sl_2 Serre constraints (EXACT: P_2=0, 70 tests). Super-Yangian Y(gl(4|20)) conjectural. E_8 x E_8 structure function computed: degree-(24,24), c=8+8+8=24.
3. **ZTE correction**: S^{corr}=S+κ²T NOW COMPUTED (exact rational T matrix, 35 tests). Previously constructive (rank 35/36 in extended complex); now explicit entry-by-entry from 1-dim kernel. The correction giving genuine E_3 structure beyond pairwise factorization.
4. **Sp_4(Z) modularity**: E_3 S-matrix -> Siegel modular forms -> Phi_10. Fourier-Jacobi = E_2->E_3 restriction proved. Full pipeline open. Mathieu moonshine connection: frame shape = twined bar Euler for all 25 M_24 conjugacy classes.
5. **Root-of-unity CY quantum groups**: Kazhdan-Lusztig at root of unity for CY categories. Modular tensor categories from Phi. CY-C remains conjectural but abelian K3 case now fully specified: C(g,q) = D(Y^+(g_{K3})), Rep = Rep^{E_2}(Y) via BZFN, R-matrix = MO. Root-of-unity N=2: 324 modules, abelian S-matrix degenerate (non-abelian needed for modularity). Chiral volume conjecture FORMULATED (Abel-Jacobi period).

Compute engines (~460 total, ~34,000 tests). Core engines: holomorphic_cs_chiral_engine, k3_yangian, k3_double_current_algebra, drinfeld_center_k3_heisenberg, e3_two_parameter_rmatrix, categorical_s_matrix_e3, e2_koszul_heisenberg, e1_koszul_three_families, a_infinity_bar_w1inf, e1_chiral_bialgebra_engine, chiral_coproduct_spin3_engine, e3_bar_bc, zamolodchikov_tetrahedron_engine, zte_deformation_cohomology, derived_framing_obstruction, operadic_tcft_mk_b2_engine, stasheff_cancellation_obs_ainf, obs_ainf_local_p2, chiral_ce_complex. K3 quantum group engines: k3_super_yangian, k3_abelian_yangian_presentation, k3_quantum_toroidal, k3_quantum_determinant, k3_serre_relations, k3_rtt_ope_dictionary, k3_nonabelian_coproduct, k3_structure_function_explicit, k3_yangian_adversarial, k3_factorization_homology, k3_mirror_koszul, k3_elliptic_genus_bkm_bar, k3e_relative_chiral_algebra, k3e_wall_crossing_shadow, k3e_topological_string_shadow, k3e_e2_promotion_analysis, mukai_indefinite_yangian, mo_rmatrix_k3_charge2, cy_c_quantum_group_k3, borcherds_vertex_yangian, bkm_yangian_generators, bkm_chiral_algebra, ade_yangian_level1, zte_correction_engine, cech_htt_convergence, hopf_fibration_s3_framing, kappa_bkm_adversarial, phi_k3_explicit_evaluation, w2_triplet_mock_modular, mock_modular_mechanism, costello_5d_verification, sp4_modularity_pipeline, higher_deligne_cascade, wilson_line_coproduct_engine, sl2_matrix_lax_engine, genus2_chiral_partition, shadow_class_moduli_variation, fh_mckay_correspondence, conifold_shadow_transition, chiral_ce_complex, k3_yangian_quantization, bps_entropy_shadow, motivic_shadow_zeta, diagonal_siegel_cy_orbifolds, kummer_excision_verification, fermat_quartic_k3_chiral, niemeier_shadow_landscape, kappa_spectrum_reconciliation, k3e_e1_chiral_yangian, swiss_cheese_cy3_e1, quintic_shadow_tower, m3_coproduct_correction_engine, chiral_coproduct_universal_engine, shadow_resummation_borcherds, and ~250 others from prior sessions and the final ~170-agent wave.

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
2. Then this file (kappa-spectrum, AP-CY1-8, AP-CY21-26, AP-CY27-40).
3. Check AP113: bare kappa -> subscripted kappa_{ch,BKM,cat,fiber}.
4. Check AP114: do not cite theorems from 12 stub chapters.
5. CY-A: d=2 PROVED, d=3 PROVED (inf-cat). Chain-level [m_3,B^{(2)}]!=0 is NOT an obstruction. CY-A_3 dependent results may now use \begin{theorem}.
6. CY-C is CONJECTURE. NEVER \begin{theorem} for CY-C (AP40). Abelian level: C(g,q) = D(Y^+(g_{K3})).
7. E_1-chiral bialgebra: the correct Hopf home. E_∞ vertex bialgebra loses R-matrix (AP-CY23).
8. E_3 bar: 2^{3g} for class L,C. 6^g for class M (PROVED, AP-CY21 updated).
9. Kummer route Steps 1-4 are PROVED (prop:kummer-orbifold). Step 5 conjectural.
10. Borcherds lift = resummation. The additive/multiplicative = perturbative/non-perturbative.
11. Shadow tower = A_inf coproduct corrections: S_k = delta^{(k)}. Shadow-Feynman: L-loop = S_{L+1}. Tower computed through m_8 (160 tests, S_8 = 4144720/19683).
12. kappa_BKM = c_N(0)/2 is the ONLY correct universal formula. NOT kappa_ch + chi(O_fiber).
13. B(U^ch(L)) = CE_*(L) PROVED (chiral CE complex identification).
14. Super-Yangian Y(gl(4|20)) is CONJECTURAL (AP-CY35). Never \begin{theorem}.
15. Class M: Borel summable (Gevrey-1), NOT convergent (AP-CY39).
16. CFG25 agreement: 24% lift rate at perturbative genus-0 only (AP-CY37).
17. 3 wrong proofs caught and retracted this session. The Beilinson principle works.
18. ZTE correction T COMPUTED (exact rational, 35 tests). Previously constructive; now explicit.
19. Mock modular K3: THEOREM at d=2 (4-step proof). Class M = mock modular.
20. CY-D: kappa_ch != chi(O_X) at odd d. Dimension-stratified formula required.
21. Incompatibility: mu_3 != 0 implies mu_2 = 0 on augmentation ideal (chain level, all non-formal).
22. Mathieu moonshine: frame shape = twined bar Euler for all 25 M_24 classes.
23. Root-of-unity N=2: 324 modules, abelian S-matrix degenerate.
24. E_8 x E_8: structure function degree-(24,24), c = 8+8+8 = 24.
25. BKM Serre P_2 = 0 EXACT: no higher corrections to imaginary root Serre relations.
26. m_5 independently verified: G_5^{conn} = 775/5184 from 5-point Wick contraction.
27. Chiral volume conjecture FORMULATED (Abel-Jacobi period).

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
