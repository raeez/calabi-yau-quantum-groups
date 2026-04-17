# CLAUDE.md -- Volume III: CY Categories, Quantum Groups, and BPS Algebras

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol III-specific material.**

## /chriss-ginzburg-rectify: READ THE WHOLE FILE, CHUNK BY CHUNK, LINEARLY (TOP-LEVEL INJUNCTION)

When the user invokes `/chriss-ginzburg-rectify` (or the skill `chriss-ginzburg-rectify`) on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. You must analyse the **whole file**, **chunk by chunk**, **linearly progressing from start to finish**, with **small chunk size**. Every line must pass under your eyes.

**Binding rules**:
- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do NOT sample. Do NOT jump. Do NOT read section heads via Grep and call it Phase 1. Do NOT read only opening + closing + dense midsection.
- **Chunk size: ~250-500 lines per Read call, at most**. Large chunks (1000+ lines) that approach the 25000-token Read cap are forbidden: they compress context and invite skimming. Prefer many small Reads to few large ones.
- **Linear progression**: start at line 1. Each subsequent Read starts exactly where the previous one ended (offset = prev_offset + prev_limit). No ranges are skipped; no ranges are revisited unless a Phase 3 edit requires re-reading a specific chunk.
- **Coverage is a proof obligation**. Before leaving Phase 1, verify: the sum of (limit) across all Phase 1 Reads equals the file line count, and the starting offsets form a contiguous cover of [1, EOF]. If you cannot state this, Phase 1 is incomplete.
- Grep does NOT substitute for Phase 1 reading. Grep is Phase 3 cross-file propagation (AP5), not the global diagnostic.
- If a Read fails with the 25000-token cap, cut the `limit` in half and retry. Never "skip ahead past the oversized region."

This injunction applies to EVERY invocation of `/chriss-ginzburg-rectify`, on files of any size. A 5000-line chapter takes ~10-20 small Reads. That is the cost; it is not negotiable. (Instance that prompted this rule: cy_to_chiral.tex 5166 lines, 2026-04-17 — strategic sampling attempted and was rejected by the user.)

## MANUSCRIPT HYGIENE (TOP-LEVEL INJUNCTION)

**NO ANTIPATTERN TAGS OR METADATA LEAKAGE INTO THE MANUSCRIPT OR STANDALONE PAPERS PROPER.**

Reader-facing prose (the compiled `main.pdf` PLUS every standalone paper in `standalone/`, `notes/` when published, or shipped to arXiv/journal) must contain zero manuscript-internal discipline noise. Concretely: every violation below is a HARD VIOLATION and must be stripped before commit.

**Prohibited in manuscript prose:**
- AP/AP-CY tag citations (e.g., "(AP-CY60)", "(see AP-CY72)", "per AP-CY55", "violates AP113"). The catalogue is at `appendices/anti_pattern_catalogue.tex` and is development-tree-only (NOT \input'd by main.tex). Tags live there and in CLAUDE.md, nowhere else.
- Session timestamps ("2026-04-17 inscription", "the 2026-04-17 campaign", "earlier phrasing superseded").
- Commit hashes in parentheses (e.g., "(commit cade61c)").
- Manuscript-version self-reference ("first edition of this volume", "the earlier formulation").
- Healing-status commentary ("was previously wrong", "is now healed", "retracted and replaced", "(status upgraded)").
- Audit language ("the adversarial swarm", "the agent found", "per the audit").
- Internal RECTIFICATION-FLAG markers in non-comment prose.

**Where metadata belongs:** commit messages, `notes/` changelog files, the AP catalogue, CLAUDE.md, first-principles cache. The PDF is for Drinfeld, Beilinson, Etingof — not for the rectification audit trail.

**Before every commit that touches a file under `chapters/`, `standalone/`, `main.tex`, `preface`, or an appendix INCLUDED by main.tex, grep:**
`AP-CY|AP1[0-9]\{2\}|2026-|commit [a-f0-9]\{7\}|inscription|campaign|healed|first edition|earlier phrasing|superseded across|adversarial audit|the agent found|RECTIFICATION-FLAG`

Each hit either (a) strips the metadata while preserving the mathematical claim verbatim, or (b) migrates the content to `notes/` / a commit message / the catalogue.

The AP catalogue input in main.tex (L1239) is commented out 2026-04-17. Any future reintroduction of `\input{appendices/anti_pattern_catalogue}` requires explicit user approval.

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_n-ChirAlg (n=inf at d=1, n=2 at d=2, n=1 at d>=3) providing input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function. At d>=3 the E_2 braided structure lives on the Drinfeld center Z(Rep^{E_1}(A)), not on A itself.

~693pp, this repo, ~34,000 tests, ~460 engines. Seven parts with Part openers and 3 reading paths (algebraist, physicist, number theorist): I(Foundations) II(CY-to-Chiral Functor) III(E_n Hierarchy and Chiral Quantum Groups) IV(The K3 Yangian) V(CY Landscape) VI(Seven Faces of r_CY(z)) VII(Frontiers). Notation appendix (541 lines) and AP catalogue (668 lines) installed. 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites.

**4 genuine stub chapters** (<50 lines, AP114): quantum_groups_foundations (24), geometric_langlands (28), matrix_factorizations (29), modular_koszul_bridge (13). Develop or comment out. **3 thin chapters** (50-100 lines, may need development): cyclic_ainf (55), cy_categories (70), e1_chiral_algebras (90). **6 formerly listed stubs now developed** (>150 lines): hochschild_calculus, braided_factorization, drinfeld_center, fukaya_categories, quantum_group_reps, derived_categories_cy.

## Main Theorems

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROVED (inf-cat) | d=3 chain-level [m_3,B^{(2)}]!=0 resolved: not an obstruction in inf-cat framework (HH^{-2}_{E_1}=0). Goodwillie layers vanish. Space of E_3-liftings contractible. |
| **CY-B** (E_n-chiral Koszul duality) | d=3 PROVED | d=2: E_2-Koszul on A directly (A is E_2). d=3: E_1-Koszul on A via B_{E_3}(A), inducing E_2 on Drinfeld center Z(Rep^{E_1}(A)). thm:cy-b-d3, thm:verdier-spectral-functor. CY-B1 (conductor): proved all classes. CY-B2 (braided equiv on center): proved all classes via Verdier spectral functor. 326 tests across cy_b_toward_proof, cy_b_d3_proof, cy_b_d3_final. |
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
| **CFG25 comparison** | VERIFIED | CFG (arXiv:2602.12412) E_3 from BV-quantised CS. Agreement at perturbative genus-0 level. Costello 5d verification at charge 4 (87 tests). CFG25 35% lift rate (76% require chain-level corrections). |
| **Super-Yangian Y(gl(4\|20))** | CONJECTURAL | BKM-to-Yangian lift from Mukai signature (4,20). k3_super_yangian (59 tests). |
| **6 routes to G(K3xE)** | PROGRAMME (CY-C) | Six independent CONSTRUCTIONS (not six applications of Phi; AP-CY60): Kummer, Borcherds, MO stable envelope, McKay, factorization homology, Costello 5d. Only Route 4 uses Phi. Convergence = CY-C (CONJECTURAL). |
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
| **CY-B push at d=3** | PROGRAMME (131 tests) | E_1-chiral Koszul duality (inducing E_2 on center) extended to d=3 via inf-cat CY-A_3. Conditional on chain-level data for non-formal algebras. |
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
| **BKM Serre P_2 = 0** | CONJECTURAL (AP40-corrected 2026-04-17) | Second Serre polynomial conjecturally vanishes. Engine \texttt{bkm\_serre\_higher\_order.py} self-declares STATUS=CONJECTURAL; manuscript previously stated as theorem (AP40 violation). Healed via downgrade in working_notes.tex `conj:bkm-serre-exact`. Independent verification (perturbative ε² Fourier expansion) outstanding. |
| **E_8 x E_8 structure function** | COMPUTED | degree-(24,24) structure function, c = 8+8+8 = 24. Mukai lattice decomposition via E_8 x E_8. |
| **Root-of-unity N=2** | COMPUTED | 324 modules (= 24*N^2*3/4 = 324 for N=2). Abelian S-matrix degenerate. Non-abelian K3 Yangian needed for modularity. |
| **Mathieu frame shape** | VERIFIED | Frame shape = twined bar Euler for all 25 M_24 conjugacy classes. Connects Mathieu moonshine to bar complex. |
| **Incompatibility Theorem (strengthened)** | PROVED | mu_3 != 0 implies mu_2 = 0 on augmentation ideal. Strengthened: holds at chain level for ALL non-formal A_inf algebras (class >= L). |
| **BP conductor identity** | PROVED (sympy-verified, 2026-04-16) | c(BP_k) + c(BP_{-k-6}) = 196 polynomial identity. c-98 = -24u-96/u in u=k+3 (odd). c=98 has roots k=-3+/-2i only. Replaces meaningless kappa(BP_{-3})=49/3. Vol I: bp_self_duality.tex healing target. |
| **W_N central-charge conductor** | PROVED (cubic, multi-source, wave 7+8) | K^c_N := c(W_N^k)+c(W_N^{k'}) = 4N^3 - 2N - 2. Values K_2=26, K_3=100, K_4=246, K_5=488. Third difference = 24 constant. Multi-source verified including K_kappa(W_4) = (13/12)*246 = 533/2. |
| **W_N kappa-conductor** | PROVED | K^kappa_N := kappa+kappa' = K^c_N * (H_N - 1). Distinct invariant from K^c. Both correctly called "Koszul conductor"; naming discipline (K^c vs K^kappa) required to avoid AP-CY55-type confusion. |
| **delta F_2(W_3) = (c+204)/(16c)** | PROVED (multi-source, wave 7) | 204 = 4*51 from 3 independent verifications: 4-graph sum, large-c tadpole limit, universal N-formula at N=3. Promote ProvedElsewhere -> ProvedHere. |

## Commands

```
# Build (Vol III)
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # quick build
make                                                              # full build with bibliography
make test                                                         # all ~34,000 tests

# Single test / engine
python3 -m pytest compute/tests/test_<name>.py -v
python3 compute/<engine>.py                                       # run engine standalone

# Independent verification audit (HZ3-11 protocol)
make verify-independence                                          # summary
make verify-independence-verbose                                  # per-claim coverage

# Cross-volume builds
cd ~/chiral-bar-cobar && make fast                                # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
```

**Independent verification coverage (2026-04-16, post-reconstitution + cross-volume orphan healing + Vol I scraper alias fix + Vol II continuation expansion + shadow tower r=6,7,8 + moonshine unified):** Vol III 22/290, Vol II 61/1322, Vol I 49/2496. **All three volumes: AUDIT RESULT: PASS** (zero tautologies, zero orphans). Cross-volume totals: 132 disjointly-verified ProvedHere claims / 4108 total (3.2%). Orphan healings applied Option 1 across-the-board (strongest form, no downgrades). Vol II expansion installed 15 new decorators on triality-y-algebra + SC heptagon + climax theorems; 26 new tests pass. Vol I additions: shadow tower higher coefficients S_6, S_7, S_8 (all rational in c; exact denominator pattern verified direct-computation at r=4..9: c-exponent = r−3, (5c+22)-exponent = ⌊(r−2)/2⌋; earlier report of c^(r-2) was off-by-one and is corrected here) + `S_9(Vir_c) = −1280(2025c² + 15570c + 29554)/[3c^6·(5c+22)^3]` extended via Riccati recurrence (main thread 2026-04-17) + chiral moonshine unified (Monster/Conway/Thompson/Mathieu). Campaign advances incrementally.

## The kappa-Spectrum (AP113 + AP-CY55, CRITICAL)

Bare "kappa" is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript.

**AP-CY55**: The four kappas fall into two types. Conflating them is forbidden:

**Manifold invariants** (topological, fixed by the geometry, INDEPENDENT of algebraization):

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_cat | chi(O_X) = holomorphic Euler char | 0 = chi(O_{K3xE}); fiber value chi(O_{K3}) = 2 |
| kappa_fiber | Lattice rank / fiber structure | 24 (Mukai lattice rank) |

**Algebraization invariants** (depend on which chiral/BKM algebra is constructed):

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| kappa_ch | From chiral algebra A_C via Phi | 3 (= kappa_ch(K3) + kappa_ch(E) = 2+1) |
| kappa_BKM | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |

Saying "algebraizations share kappa_cat" is VACUOUS: kappa_cat and kappa_fiber are topological invariants of the manifold and cannot vary between algebraizations. Only kappa_ch and kappa_BKM depend on the algebraization.

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

### HZ3-11. Independent Verification Protocol (cross-volume, 2026-04-16)

**STANDALONE -- all material to use this protocol is contained here. Do not follow pointers unless you need historical context.**

#### Why this exists

The 2026-04-16 adversarial audit of Vol III found that many `\ClaimStatusProvedHere` theorems were backed by test suites that were tautological by construction: engines hardcoded data tables like `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with the verified identity (`weight := c_0 / 2`) built into the row itself. The "99-test cross-validation" amounted to `Fraction(10, 2) == 5` checks against the same table. No claim was genuinely verified; the tests were arithmetic against the hardcoded derivation.

This failure mode propagates silently because:
1. tex prose paraphrases a partial result universally ("proved unconditionally");
2. the engine takes the paraphrase as definition and hardcodes target values;
3. tests check arithmetic identities against the hardcoded table;
4. CLAUDE.md inherits the paraphrase without scope;
5. the next session reads CLAUDE.md, not the .tex.

Rules that fix this failure mode ("always verify", "never hardcode") proved ineffective. The protocol replaces them with a mechanical, machine-checked invariant.

#### The mechanical invariant

Every test claiming to verify a ProvedHere theorem must declare:

- `derived_from`: canonical names of data/papers/conventions the formula came from.
- `verified_against`: canonical names of independent data/papers/conventions the test uses to compute its expected value.
- A one-sentence `disjoint_rationale` explaining why the two sets are genuinely independent (not renamed).

If `derived_from ∩ verified_against` is nonempty (case/whitespace-insensitive), the test module fails to import. The tautology becomes an audit failure, not a silent pass.

#### Decorator API (use verbatim)

```python
from compute.lib.independent_verification import independent_verification

@independent_verification(
    claim="thm:phi-k3-explicit",                   # label in .tex
    derived_from=[
        "HKR isomorphism on D^b(Coh(K3))",
        "Hodge diamond of K3",
    ],
    verified_against=[
        "Mukai 1984 lattice rank 24 for H^*(K3, Z)",
        "Classical Betti numbers b_0 + b_2 + b_4 = 24",
    ],
    disjoint_rationale=(
        "HKR reconstructs total_dim via polyvector cohomology on K3; "
        "Mukai/Betti gives the rank as a topological invariant from "
        "the K3 lattice without any HH_* or chiral construction. "
        "Independent derivations."),
)
def test_total_dimension_24():
    ...
```

The decorator registers the test, performs the disjointness check at import time, and preserves test behaviour. It is a no-op on pass.

#### Enforcement

- `make verify-independence`           -- summary audit
- `make verify-independence-verbose`   -- lists every uncovered claim

The audit scrapes `chapters/`, `appendices/`, `notes/`, and `working_notes.tex` for `\ClaimStatusProvedHere` tags, imports every test module to populate the registry, and reports:

  - ProvedHere claims found (count).
  - Claims with at least one independent decorator (coverage).
  - Tautological decorations (should be zero; they fail at import).
  - Orphan entries: decorators whose `claim` label is not actually ProvedHere.

Exit status: `0` on clean pass, `2` on any tautology or orphan. Coverage percentage is a metric, not a gate -- enforcing a coverage floor would incentivize low-quality "independent" tests.

#### Three healings when honest decoration fails

1. **Find a disjoint verification source.** Best outcome. Example: `thm:phi-k3-explicit` uses HKR on K3 to compute rank 24, but Mukai lattice theory gives rank 24 independently.
2. **Restrict the scope.** Replace `\begin{theorem}` with `\begin{proposition}[for the 8 diagonal Z/NZ symplectic orbifolds]` and note the general case is conjectural. This is the honest reading of `prop:bkm-weight-universal`.
3. **Downgrade status.** Replace `\ClaimStatusProvedHere` with `\ClaimStatusConjectured`. This is the fallback: a "proved" claim without independent test should not be tagged as proved.

The audit does NOT automatically choose; it surfaces the choice. The Vol III working queue is in `notes/tautology_registry.md` (seeded 2026-04-16 with: `prop:bkm-weight-universal`, `thm:derived-framing-obstruction`, `prop:cy-a-three-saga-resolution-costello`, `prop:p2-vanishes-exact`, `sec:k3e-six-routes`).

#### Protocol for new theorems

Before writing `\ClaimStatusProvedHere`:

1. Ask: "What is my independent verification source?"
2. If you cannot name one: restrict scope or use `\ClaimStatusConjectured`.
3. Write the test with `@independent_verification(...)` from day one.
4. Run `make verify-independence` before commit.

The decorator is an assertion about mathematical practice, not a bureaucratic tag. A claim without independent verification cannot be distinguished from a circular fit.

#### Files (cross-volume, identical code)

- `compute/lib/independent_verification.py`     -- decorator + registry + disjointness check
- `compute/scripts/audit_independent_verification.py` -- lint: .tex scrape + registry cross-check
- `compute/tests/test_independent_verification_infra.py` -- self-test (7 tests of the infra)
- `notes/INDEPENDENT_VERIFICATION.md`           -- protocol doc
- `notes/tautology_registry.md` (Vol III only at seed) -- known-tautological claims awaiting healing

Coverage snapshot at installation (2026-04-16):

  - Vol I:   0 / 2275 ProvedHere claims.
  - Vol II:  0 / 1134.
  - Vol III: 2 /  283.

This gap is the cross-volume healing queue. Closing it is a multi-session project; the gate is that the gap must close through GENUINE independent verification or explicit status downgrade, never through tautological decoration.

### HZ3-12. AP-CY61 (first-principles investigation, mandatory)

When challenged on a mathematical claim, do NOT just swap labels. Investigate from first principles. For every confusion, mistake, or wrong claim, answer ALL THREE:
(a) What does the claim get RIGHT? (the ghost of a true theorem)
(b) What does it get WRONG? (the precise conflation)
(c) What is the CORRECT mathematical relationship?

Every wrong claim contains the seed of a correct theorem -- extract it. If you cannot state the correct theorem, you do not understand the error.

Examples (this protocol is the one that uncovered them):
- "categorified averaging" wrong; factorisation E_1 ->^Z E_2 ->^{Sym} E_inf real
- "CoHA = bar complex" wrong; Schiffmann-Vasserot CoHA = Y^+ real
- "kappa(BP_{-3}) = 49/3" wrong as a value; c(k) + c(-k-6) = 196 polynomial identity real (sympy 2026-04-16)
- "Gravitational Yangian Y(Vir_{13})" wrong (Vir has no Yangian construction in the literature); shadow tower coalgebra structure real

### HZ3-13. AP-CY83 (standalone-vs-chapter drift, MUST-CHECK at submission)

Standalones submitted to journals systematically LEAK caveats present in their parent chapters. The pattern is consistent across waves 6 + 7 of the 2026-04-16 swarm:
- BP self-dual point warning in `bp_self_duality.tex` Prop 4.7 -> dropped in 2 cross-reference files.
- L^sh Eisenstein poles disclaimer in `chapters/connections/arithmetic_shadows.tex` -> violated in `standalone/arithmetic_shadows.tex`.
- ChirHoch `{0,2}` occupation (chapter, correct) -> stated as `{0,1,2}` amplitude (standalone, misleading).
- CY-A_3 status overclaim cascade in `programme_summary.tex`: three contradictory framings in one document.

Counter: before any standalone is shipped, diff against the chapter version. Every "this fails when X" warning in the chapter must be present (or honestly handled) in the standalone.

### HZ3-14. AP-CY84 (amplitude vs occupation, prose discipline)

"H^i concentrated in {0, 2}" -- OCCUPATION (H^1 = 0 specifically).
"H^i concentrated in [0, 2]" -- AMPLITUDE (H^i = 0 for i > 2).

NEVER write "{0, 1, 2}" to mean "amplitude <= 2". Either the middle index is populated (occupation) or it is an amplitude bound (interval). Mixing collapses provable facts into apparent contradictions; the wave 4 ChirHoch "contradiction" between `chiral_center_theorem.tex` and `en_chiral_operadic_circle.tex` was wave 6 resolved as exactly this discipline failure (both `{0,2}` and `[0,2]` were correct; they describe different things).

## E_n Chiral Hierarchy (CY dimension -> native E_n level)

The Gerstenhaber bracket on HH*(C,C) has degree 1-d. This determines the native E_n level:

| d | Native E_n | Bracket degree | Mechanism |
|---|-----------|---------------|-----------|
| 1 | E_infty (commutative) | degree 0 | Abelian Lie conformal; symmetric factorization |
| 2 | E_2 (braided) | degree -1 (Lie = lambda-bracket) | S^2-framing of HH_*(C) gives E_2 directly |
| 3 | E_1 (ordered) | degree -2 (shifted Lie) | Holomorphic CS breaks E_2 to E_1; CoHA is associative |
| >=4 | E_1 stabilized | degree <=(-3) | pi_d(BU)=KU^{-d} obstruction (2-periodic, Z at even d) + pi_d(BSp) subset pi_d(BO)=KO^{-d} refinement (8-periodic, Z/2 at d=5 mod 8); no native braiding. NEVER call pi_d(BU) 8-periodic -- it is 2-periodic; the 8-periodicity is real Bott (BO/BSp). AP-CY73. |

**E_2 at d=3 is DERIVED, not native**: The E_2 braiding on Rep categories of d=3 chiral algebras comes from the Drinfeld center Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^der_ch(A)), NOT from A itself. The chiral algebra A is E_1; only its representation category acquires E_2 braiding after passing through the center.

E_3 at d=3 is the DERIVED CENTER (higher Deligne): HH*(B_{E_3}(A), B_{E_3}(A)). This is a structure on the observables of the field theory, not on the CY chiral algebra Phi(C).

Drinfeld center is categorified av: E_1-Cat -> E_2-Cat. Quantum groups, Yangians, braided tensor categories natively E_1. E_2 derived.

## CY-Specific Anti-Patterns (AP-CY1 through AP-CY8)

AP-CY1: CY dimension d != complex dimension n. Fuk(X) is CY_n, D^b(Coh(X)) is CY_n. Not real dim 2n.
AP-CY2: CY trace is in HC^-_d(C), NOT just HH_d -> k. Negative cyclic refinement essential for S^d-framing.
AP-CY3: see HZ3-5. Plus: E_2 -> E_inf loses quantum group structure.
AP-CY4: see HZ3-5.
AP-CY5: Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple.
AP-CY6: see HZ3-1. Plus: pre-April-2026 statement "A_X does NOT exist" is SUPERSEDED by the inf-cat proof (thm:derived-framing-obstruction).
AP-CY7: see HZ3-4.
AP-CY8: see HZ3-6.

### Empirical (AP-CY9-13, from 50-commit error archaeology)
AP-CY9: Jacobi form discriminant constraint. For phi_{k,m} of index m, only discriminants D with D=0 or D=3 mod 4 (m=1) can appear. NEVER fill coefficient table with sequential D-values. Verify discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention, NOT 1.
AP-CY10: see HZ3-8.
AP-CY11: see HZ3-3. Plus: DEFAULT for CY-C-dependent results: \begin{conjecture}.
AP-CY12: see HZ3-9.
AP-CY13: see HZ3-10. Plus: 7+ stale refs survived a single restructuring; use \ref{part:...} exclusively.

### Deep Empirical (AP-CY14-19, from 100-commit deep archaeology)
AP-CY14: see HZ3-1. Plus: G(X) and C(g,q) remain unconstructed; statements through them MUST use \begin{conjecture}. 11+ instances fixed across 4 commits.
AP-CY15: README scope inflation beyond .tex ground truth. README must not claim "verified" or "proved" for structural analogies or pattern matches. The README accumulates stronger claims than the .tex supports because the LLM optimizes for impressiveness. After README edits, verify every "proved"/"verified" against corresponding \ClaimStatus tag.
AP-CY16: Matrix size conflation in group quotients. Sp_4 quotient by +/-I_4 (4x4), NOT +/-I_5. O(Lambda^{3,2}) quotient by +/-I_5 (5x5). When two groups of different rank appear in the same formula, the LLM harmonizes subscripts to whichever appears more frequently.
AP-CY17: see HZ3-7. Plus: ADE in 2 variables = CY_0 (semisimple); the n-1 vs n-2 error changes which families are CY_2 (Dyckerhoff).
AP-CY18: Lattice theta series comparison. Verify q-power divergence by DIRECT COMPUTATION. Leech theta: minimum norm^2=4, first correction at q^2 not q^1. The match with 1/eta^24 extends through q^1. Never conflate j(tau) coefficients with V_Lambda character coefficients.
AP-CY19: A-hat genus argument halving. A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi (first pole of sin(x/2) at x=2*pi). NEVER drop the /2 in the argument, which gives spurious radius pi. Appeared in 3+ independent computations.
AP-CY20: Normal bundle vs spectral parameters. The Z x Z grading from the normal bundle N_{C/Y} of a curve C in a CY threefold Y connects to the quantum toroidal parameters (q,t) through the Omega-background, NOT through the bundle grading directly. The intermediary mechanism (equivariant localization on the Omega-background, Nekrasov partition function, refinement) must be stated explicitly. NEVER write "N_{C/Y} grading = (q,t) parameters" as a direct identification. Counter: before any claim relating normal bundle gradings to quantum group parameters, name the intermediary mechanism and cite the equivariant/Omega-background passage.

### CY-D Correction (AP-CY34a/AP-CY44, from kappa_ch investigation)
AP-CY34a (also AP-CY44): kappa_ch != chi(O_X) at odd d. For ANY compact CY_d with d odd, chi(O_X) = 0 by Serre duality (h^{0,q}=h^{0,d-q} and pairwise cancellation). Therefore kappa_ch = chi(O_X) is FALSE whenever kappa_ch != 0. Known falsifications: E (d=1, kappa=1), abelian surface (d=2, kappa=2, h^{1,0}=2), K3xE (d=3, kappa=3). The formula kappa_ch = chi(O_X) is PROVED ONLY for CY_2 with h^{1,0}=0 (K3, etc.) where HH_{-1}=0 and the Serre argument kills the quantum correction. For d>=3: HH_{-1} = h^{2,0}+h^{1,1}+h^{0,2} is ALWAYS nonzero (h^{1,1}>=1 for projective), so the Serre argument NEVER applies. The correct CY-D uses the categorical chi^CY, distinct from chi(O_X). Counter: NEVER write kappa_ch = chi(O_X) outside the scope d=2, h^{1,0}=0. At d=3: use the dimension-stratified formula (conj:cy-kappa-identification). 76 tests in cy_d_kappa_d3.py. (NOTE: number AP-CY34 was reused below for the TCFT/m_3 saga; this entry is renamed AP-CY34a to disambiguate. AP-CY44 is the cross-programme synonym.)

### Manifold vs Algebraization Invariants (AP-CY55)
AP-CY55: kappa_cat = chi(O_X) and kappa_fiber = rank(Lambda) are TOPOLOGICAL invariants of the MANIFOLD, NOT properties of the algebraization. Saying "algebraizations share kappa_cat" is VACUOUS. Only kappa_ch and kappa_BKM depend on the algebraization. Counter: every kappa-spectrum table or discussion MUST distinguish manifold invariants (kappa_cat, kappa_fiber) from algebraization invariants (kappa_ch, kappa_BKM). NEVER present all four as the same type. NEVER assert that kappa_cat "agrees" between algebraizations as if this were meaningful.

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

### 290-Agent Session APs (AP-CY35-AP-CY52, from ~290-agent comprehensive wave, April 2026)
AP-CY35: B^{(j)} hierarchy confusion. B^{(0)} = Connes B (mixed complex). B^{(j>=1)} = Connes HIERARCHY (S^d-framing). The mixed complex axiom [b, B^{(0)}]=0 does NOT extend to [b, B^{(j)}]=0. Three "proofs" were wrong because of this confusion. Counter: always specify which B^{(j)} and never assume the mixed complex identity for j>=1.
AP-CY36: kappa_ch formula gives wrong value. The formula Sigma(-1)^i dim HH_i gives chi_top (=24 for K3), NOT kappa_ch (=2). The correct formula is the Hodge-filtered supertrace Sigma(-1)^q h^{0,q}. The Serre duality kills non-F^0 contributions. Counter: never compute kappa_ch as alternating sum of HH_i dimensions. Use str_{F^0}(q^{L_0}).
AP-CY37: kappa_BKM = kappa_ch + kappa_cat is a COINCIDENCE for N=1. The correct universal formula is kappa_BKM = c_N(0)/2 (Borcherds weight theorem). Fails for 7/8 diagonal Siegel orbifolds. Counter: use c_N(0)/2, never the naive decomposition.
AP-CY38: Class M E_3 bar != infinite. It's 6^g (proved via Kunneth). The d_4 kills Lambda^0 and Lambda^3, leaving [0,3,3,0] at g=1. Counter: state "6^g (closed form via Kunneth)" for class M, not "infinite."
AP-CY39: Incompatibility Theorem. For single-object cyclic A_inf CY_3: mu_3!=0 forces mu_2=0 on augmentation ideal. Cross-arity cancellation is IMPOSSIBLE at the naive level. The TCFT B^{(2)} differs from naive pairwise contraction. Counter: never assume mu_2 and mu_3 can coexist on the same graded piece at the chain level.
AP-CY40: ProvedHere with no proof block. A theorem carrying \ClaimStatusProvedHere MUST have a \begin{proof} block. The adversarial agent found thm:cy-to-chiral-d3 had ProvedHere but no proof. Counter: grep for ProvedHere and verify a \begin{proof} block follows within 50 lines.
AP-CY41: Internal contradictions from partial updates. When upgrading a conjecture to theorem, ALL instances must be updated. The session found ~30 locations still saying "open" after CY-A_3 was proved. Counter: after any status change, grep all three volumes for the old status string and update every match.
AP-CY42: phi_{0,1} normalization. c(-1)=1 (standard Gritsenko-Nikulin) vs c(-1)=2 (K3 elliptic genus = 2*phi_{0,1}). The factor of 2 is kappa_ch(K3). Propagated silently across 3 engines. Counter: state which normalization convention is in force and verify against the K3 elliptic genus.
AP-CY43: Shadow-Feynman tautology at L>=4. The Feynman engine calls the shadow recursion, making the match tautological. Independent verification requires computing m_k directly (e.g., from k-point conformal blocks). Counter: for L>=4, verify via an independent computation path, not through the shadow recursion.
AP-CY44: see AP-CY34a. Root cause: additivity vs multiplicativity.
AP-CY45: N=2 root-of-unity gives TRIVIAL double braiding. q^2=1 at N=2. Non-abelian MTC requires N>=3 where q^2!=1. Counter: verify q^2 != 1 before claiming modular (non-symmetric) structure.
AP-CY46: No native CY_4 Yangian. pi_4(BU)=Z obstructs E_4. The correct structure is a p_1-twisted double current algebra. The cascade max is E_3 for ALL d>=3. Counter: never write "E_4 Yangian" or "CY_4 Yangian." Use "p_1-twisted double current algebra."
AP-CY47: Structure function degree from Mukai rank, NOT Lie algebra dimension. For E_8 x E_8: degree (24,24) from 24 Mukai directions, NOT (500,500) from dim(e_8)*2. Counter: verify structure function degree against Mukai lattice rank.
AP-CY48: 3d->6d lift rate is only 24%. Algebraic structures lift 100%, topological 0%. 6d is NOT a dimensional upgrade of 3d. Counter: state the lift rate and specify which structures lift and which do not.
AP-CY49: Agent tautological tests. 10% of agent-produced tests are tautological (testing hardcoded values against themselves). Must verify via independent computation paths. Counter: every test must have at least two independent verification sources (AP10 protocol).
AP-CY50: Duplicate agent launches. When relaunching failed agents, check the agent registry to avoid running the same task twice. Duplicate launches waste compute and create merge conflicts. Counter: check the agent registry before any relaunch. Use unique task IDs.
AP-CY51: Rate-limited agents write engines+tests but not manuscript. When an agent is rate-limited, check disk for persisted files before relaunching from scratch. Counter: check disk for persisted files before relaunching. Resume from persisted state.
AP-CY52: Mega-file anti-pattern. Files >3000 lines should be split. toroidal_elliptic.tex was 7190 lines; k3_times_e.tex was 5986 lines. Both needed splitting. Counter: when a .tex file exceeds 3000 lines, split it by section. Target 1000-2000 lines per file.

### Geometric vs Algebraic Model Conflations (AP-CY62--AP-CY67, 2026-04-16 adversarial swarm)

AP-CY62: Geometric vs algebraic chiral Hochschild model. Two chain-level models: (a) geometric C^*_{ch,geom} (FM compactifications, log forms, 3-component differential), (b) algebraic C^*_{ch,alg} (End^ch_A, Gerstenhaber bracket differential). Quasi-isomorphic for logarithmic chiral algebras. The comparison is only a REMARK, not a named theorem. At genus >= 1, geometric carries curve-dependent data algebraic lacks. Counter: specify "geometric (FM)" or "algebraic (bar/operadic)" when chain-level structure matters. Bare C^*_ch(A,A) forbidden in chain-level arguments. **Triggers**: "C^*_ch(A,A)" without model qualifier; "the derived center Z^der_ch" without model when E_n claimed; FM integration language mixed with formal-variable language.

AP-CY63: BD chiral operad vs algebraic End^ch. BD defines chiral operations via D-module maps. Algebraic End^ch uses formal Laurent series. Isomorphic after 4-step bridge (choose point, choose coordinate, trivialise D-module, identify spectral variables). Counter: never write "the chiral endomorphism operad" without specifying BD or algebraic. Bridge Proposition ABSENT from manuscript. **Triggers**: "the chiral endomorphism operad on FM_k(C)"; mixing D-module language with formal Laurent series.

AP-CY64: Three-way Hochschild confusion (ChirHoch/HH*/H*_GF). ChirHoch* concentrated in {0,1,2} (Theorem H). HH*(A_mode) concentrated in {0} for Weyl algebra (dim 1). H*_GF unbounded (polynomial ring). "ChirHoch is finite while THH is infinite" is WRONG (HH*(Weyl) = 1-dim). Genuine "fails to concentrate" = H*_GF, not THH. At critical level k=-h^v ONLY: ChirHoch* infinite (Feigin-Frenkel), HH* finite. **Triggers**: "ChirHoch is finite while THH is infinite"; "Theorem H has no classical analogue"; "concentration fails for topological Hochschild"; "Gel'fand-Fuchs agrees with ChirHoch".

AP-CY65: Spectral parameter provenance. z in R(z) has three-part origin: (a) algebraic (translation automorphism tau_z creating evaluation modules), (b) geometric (holomorphic translation on curve C), (c) representation-theoretic (z = u - v). "Topological Drinfeld centre has no spectral parameters" is FALSE: Yangian Y(g) has evaluation modules V_u. Correct claim: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. **Triggers**: "spectral parameters from the chiral structure"; "topological center has no spectral parameters"; "R(z) comes from the derived center"; "E_2 braiding carries spectral parameters".

AP-CY66: BZFN ambient category is NOT tunable. BZFN uses SAME S on both sides. Two centres come from TWO DIFFERENT ALGEBRAS: chiral A (in IndCoh(Ran)) vs mode algebra A_mode (in Vect). Counter: never say "applying BZFN in two different ambient categories." Say: "two different algebras, each with its own BZFN equivalence." **Triggers**: "applying BZFN in two different ambient categories"; "the same algebra viewed in D-modules vs Vect"; "varying S in BZFN".

AP-CY67: "Spectral parameters from FM_k(C)" is narration, not construction. End^ch_A has formal algebraic variables; FM enters via comparison theorem (a comparison, not a definition). Counter: replace "spectral parameters from FM_k(C)" with "spectral parameters from End^ch_A, identified with relative position coordinates on the formal disk via the local-global comparison." **Triggers**: "spectral parameters from FM_k(C)"; "the chiral endomorphism operad on FM_k(C)".

**Higher-order ramification guards (AP-CY62--AP-CY67):** WRONG REASONING: "Because ChirHoch is finite-dimensional, the Drinfeld center is finite" (Drinfeld center is a CATEGORY); "The spectral parameter distinguishes chiral from topological" (Yangian has spectral params despite being topological); "The curve geometry is what makes quantum groups possible" (partially right: curve creates tau_z, but once Yangian exists, spectral params persist regardless).

### Preface CG-rectify (AP-CY68--AP-CY73, 2026-04-17 session)

AP-CY68: Fiber-vs-total-space kappa_cat for K3-fibered CY_3. kappa_cat(X) = chi(O_X) is TOTAL-SPACE; for K3 x E it is 2*0 = 0 by Kunneth, not 2. The value 2 is chi(O_K3), a FIBER invariant. The naive BKM decomposition kappa_BKM = kappa_ch + chi(O_fiber) = 3 + 2 = 5 at N=1 uses chi(O_fiber), NOT kappa_cat of total space. Counter: kappa_bullet-spectrum tables for K3 x E must show kappa_cat = 0 explicitly; if the fiber value is needed for a BKM decomposition, label it chi(O_fiber) or kappa_cat(fiber), never bare kappa_cat. Cross-volume propagation commit 2f7d220 (quantum_chiral_algebras.tex L870/L1020, cy_holographic_datum_master.tex L973).

AP-CY69: Hochschild homology vs cohomology for Connes vs Gerstenhaber. S^d-framing (Connes B-operator hierarchy, KV 2015) lives on HH_bullet (homology); Gerstenhaber bracket of degree 1-d lives on HH^bullet(C,C) (cohomology). Conflating them as "Hochschild complex receives S^d-framing and Gerstenhaber bracket" loses the degree shift that determines native E_n level. Counter: always specify "Hochschild homology HH_bullet carries S^d-framing via Connes B; Hochschild cohomology HH^bullet(C,C) carries the Gerstenhaber bracket of degree 1-d." Instance: preface L79 (fixed chunk 5).

AP-CY70: Internal-development metadata in reader-facing prose. Session timestamps (2026-04-17 inscription), commit hashes (commit cade61c), manuscript-version self-reference (first edition of this volume), internal AP-tag citations in prose (AP-CY60), healing-status commentary (the original presentation is healed). None of this is meaningful to external readers. Grep for: 2026-, commit , inscription, campaign, AP-CY, healed, first edition, earlier phrasing, pre-2026-, superseded across the volume. Migrate to commit messages / notes/ changelog. Instances: 6 preface sites (fixed chunks 4-7).

AP-CY71: Hodge supertrace is kappa_cat, NOT kappa_ch. The formula sum (-1)^q h^{0,q}(X) = chi(O_X) = kappa_cat (manifold invariant). For K3 x E: 1-1+1-1 = 0 = kappa_cat; kappa_ch(K3 x E) = 3 (additive under products). Writing "kappa_ch is the Hodge supertrace, hence route-independent and equal to 0 on K3 x E" is wrong. Ghost theorem: kappa_ch IS route-independent (correct), but via CATEGORICAL INVARIANCE of Phi_3(C), not via the Hodge supertrace formula. The stratification theorem thm:kappa-stratification-by-d asserts kappa_ch = Hodge supertrace for d <= 5 but this fails at d=1 (E: 1 vs 0) and d=3 (K3 x E: 3 vs 0); scope audit pending. Counter: when asserting kappa_ch route-independence, cite categorical invariance of Phi_3(C), not the Hodge supertrace.

AP-CY72: "S^d = (decomposition)" framing-decomposition shorthand vs manifold equality. "S^4 = S^2 x S^2" is literally wrong topology (H^2 differs) but used consistently across Vol III for "the E_4-framing splits per K3 factor via Kunneth." Counter: replace with explicit framing-decomposition statement ("the E_4-framing of Phi_4(C_{K3xK3}) splits as the Kunneth product of two E_2-framings, one per K3 factor, compatible with the KV S^2-action"). Instances: preface L610, introduction.tex L249/L1404, en_factorization.tex L2685, m3_b2_saga.tex L1228, hopf_fibration_s3_framing.py.

AP-CY73: pi_d(BU) 8-periodicity vs 2-periodicity. pi_d(BU) = KU^{-d} is 2-periodic (complex Bott): Z at even d, 0 at odd d. 8-periodicity belongs to pi_d(BO) = KO^{-d} (real Bott) or to an Sp-refined tower. Writing "pi_d(BU) is 8-periodic by Bott periodicity and trivial at d mod 8 in {1, 3, 7}" conflates the two K-theories. Counter: either (a) pi_d(BO) + 8-periodicity, or (b) pi_d(BU) + 2-periodicity + explicit Sp-refinement invocation at d ≡ 5. Instances: preface L894, CLAUDE.md CY-A entry, en_factorization.tex e1-stabilization-cy theorems.

### CG-rectify campaign batch (AP-CY74--AP-CY78, 2026-04-17 in-session rectification of cyclic_ainf / hochschild_calculus / quantum_groups_foundations / modular_trace)

AP-CY74: Drinfeld-Jimbo classical r-matrix equated with the Casimir Ω. Wrong claim: "r = Ω_g (quadratic Casimir)" in the expansion R = 1 + ℏr + O(ℏ^2). Ghost theorem: r does satisfy r + r^{21} = Ω (Drinfeld 1986). Precise error: the symmetry CONSTRAINT r + r^{21} = Ω is mistaken for the object r; a quasi-triangular element cannot be symmetric (R = R^{21} forces R^2 = 1, trivial quantization). Correct relationship: r = Ω/2 + r_{sk} with r_{sk} = Σ_{α>0} E_α ∧ F_α the skew Drinfeld-Sklyanin part; the skew part carries the Lie-bialgebra cobracket, the symmetric part is forced by quasi-triangularity. Counter: when writing the classical r-matrix, state r + r^{21} = Ω explicitly and decompose. Instance: quantum_groups_foundations.tex L97 fixed 2026-04-17.

AP-CY75: Φ(D^b(K3)) conflated with the N=4 SCA. Both have κ_ch = 2, but they are DIFFERENT algebras. N=4 SCA (c=6) is the K3 sigma-model chiral algebra (Mathieu-moonshine target); Φ(D^b(Coh(K3))) = H_Muk (Mukai Heisenberg, rank-24 free-boson VOA, signature (4,20)) per Theorem CY-A_2 / thm:phi-k3-explicit. N=4 SCA is NOT in the image of Φ on any Vol III categorical input. Shared-invariant trap: κ_ch = 2 on both because the supertrace rank agrees, masking structural difference. Counter: name the specific algebra ("Mukai Heisenberg" or "N=4 SCA") and its construction; never use "the K3 chiral algebra" without qualifier. Instance: modular_trace.tex L65 fixed 2026-04-17.

AP-CY76: Quintic Hochschild grading and the Kodaira-Spencer slot. Writing "HH^1(Q_5) = H^1(T_Q) = k^{101} (Kodaira-Spencer)" places KS in Hochschild degree 1. Under the Kontsevich HKR convention HH^p = ⊕_{q+r=p} H^q(∧^r T_X) adopted in Vol III (cy_categories.tex ex:hh-k3), the KS contribution (q,r)=(1,1) lives in HH^2, not HH^1. Correct Kontsevich HKR for quintic: HH^0=k, HH^1=0 (simply connected), HH^2=k^{101} (Kodaira-Spencer), HH^3=k^4 (central, Yukawa), HH^4=k^{101}, HH^6=k. The "Hodge-style" convention (p = q - r or naive H^p(T)) places KS in HH^1 and conflicts with Kontsevich. Counter: declare the HKR grading convention at first use; Vol III default is Kontsevich p=q+r. Instances: cyclic_ainf.tex L165, derived_categories_cy.tex L96-99 fixed 2026-04-17.

AP-CY77: Borcherds cusp form Δ_N on full Sp_4(Z) vs paramodular subgroup. Writing "Δ_5 ∈ S_5(Sp_4(Z))" for the weight-5 Gritsenko-Nikulin Borcherds product is WRONG: no weight-5 cusp form exists on full Sp_4(Z) (standard Igusa forms are χ_10 weight 10 and χ_35 weight 35). Δ_5 lives on a paramodular subgroup Γ_para ⊂ Sp_4(Q), via the accidental isomorphism O^+(2,3) ≃ PGSp_4. Group-refinement error invisible at the symbol level. Counter: always specify the paramodular subgroup when writing a BKM/Borcherds weight below 10 on Sp_4(Q). Instance: modular_trace.tex L151 fixed 2026-04-17.

AP-CY78: (2-d)-shifted Poisson bracket degree. Writing "the (2-d)-shifted Poisson bracket on HH^\bullet(C) has degree 1-d" is off by one. Under PTVV convention: an n-shifted Poisson structure has bracket of cohomological degree -n. For n = 2-d, the bracket has degree d-2 (not 1-d). Verification: d=1 gives -1 (Gerstenhaber, correct); d=2 gives 0 (ordinary Poisson, correct); d=3 gives +1 (BV, correct). The "1-d" formula fails at d=2 (gives -1, wrong: should be 0) and d=3 (gives -2, wrong: should be +1). Counter: state the PTVV convention at first use; compute the bracket degree as d-2, not 1-d. Instance: hochschild_calculus.tex L22 fixed 2026-04-17.

**Anti-pattern placement rule (2026-04-17).** All AP-CY entries live in `CLAUDE.md` and the metacognitive cache `notes/first_principles_cache_comprehensive.md`. AP entries DO NOT go into manuscript LaTeX files (chapters/, appendices/, standalones/). The historical `notes/anti_pattern_catalogue.tex.archive` is kept as a frozen development-tree artefact; it is not the canonical locus and should not be appended to. New findings go to CLAUDE.md (one-line rule + instance) and the cache markdown (full ghost-theorem analysis).

### CG-rectify matrix_factorizations batch (AP-CY79--AP-CY82, 2026-04-17)

AP-CY79: Virasoro-at-c=2 vs Ising-at-c=1/2 for principal W(sl_2). Conflates two distinct chiral algebras that both appear near A_1 LG models. The principal W-algebra of sl_2 is the Virasoro vertex algebra (at a level-dependent c via Drinfeld-Sokolov); for κ_ch = μ(A_1) = 1, AP1 formula κ_ch^Vir = c/2 forces c = 2. The Ising VOA at c = 1/2 is a SEPARATE chiral algebra (the half-hypermultiplet/free-Majorana-fermion system) with κ_ch = 1/4, not 1. Narration equating the LG output with "Ising/free fermion" across a "Clifford stabilization normalization" is wrong: there is no factor-of-4 matching that takes c=1/2 to c=2. Counter: the principal W-algebra of sl_2 is Virasoro; the level is fixed by the κ match; Ising is not in the image. Instance: matrix_factorizations.tex L173 fixed 2026-04-17.

AP-CY80: Gepner (c,c)-ring Hodge indices — anti-diagonal p+q=d vs corners (0,0)+(d,d). The Gepner (c,c)-ring dimension for a CY_d is ∑_{p+q=d} h^{p,q}, i.e. the sum along the anti-diagonal of the Hodge diamond. For the quintic (d=3): h^{3,0}+h^{2,1}+h^{1,2}+h^{0,3} = 1+101+101+1 = 204. Writing "h^{0,0}+h^{2,1}+h^{1,2}+h^{3,3}" gives the same numerical sum (both include corner 1+1 and mid 101+101) but mislabels the indices: the corners (0,0) and (d,d) are always 1 for a connected smooth proper CY, not the Gepner anti-diagonal. Counter: state p+q=d explicitly and verify indices. Instance: matrix_factorizations.tex L372 fixed 2026-04-17.

AP-CY81: Knörrer stabilization count — reorganization of quadratic form into uv-pairs halves the count. A sum of 2k squares x_1²+...+x_{2k}² reorganizes into k uv-pairs via x_j²+x_{j+1}² = (x_j+ix_{j+1})(x_j-ix_{j+1}) = u v. Iterated Knörrer MF(W + ∑u_i v_i) ≃ MF(W) uses the uv-form, so stabilizing by a 2k-variable quadratic form is k Knörrer steps, not 2k. Example: W̃_{A_1} = x²+y²+z²+w² (4 variables) = u_1 v_1 + u_2 v_2 (k=2 Knörrer steps, not "four stabilizations"). Counter: count Knörrer steps by the number of uv-pairs after reorganization, not by the raw number of squared variables. Instance: matrix_factorizations.tex L167 fixed 2026-04-17.

AP-CY82: Cl_n Morita triviality requires Z/2-graded Morita + complex Bott 2-periodicity. Ungraded Clifford algebras over C have a 2-periodicity: Cl_{2k}(C) ≅ M_{2^k}(C), Cl_{2k+1}(C) ≅ M_{2^k}(C) ⊕ M_{2^k}(C). But Z/2-graded Cl_n has a DIFFERENT 2-periodicity: Cl^C_2 ≅ M_{1|1}(C) (super-matrix algebra), and Cl^C_{2k} is Z/2-graded-Morita trivial for all k ≥ 1. Writing "Cl_4 ≅ M_2(C) as Z/2-graded" is wrong: ungraded Cl_4(C) ≅ M_2(C) ⊕ M_2(C), graded Cl^C_4 ≅ M_{2|2}(C). Counter: specify Z/2-graded Morita explicitly; invoke complex Bott 2-periodicity (not real 8-periodicity, AP-CY73). Instance: matrix_factorizations.tex L171 fixed 2026-04-17.

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

Session-by-session archaeology blocks (53/129/180/230-agent waves with running test counts) -> migrated to `~/.claude/projects/-Users-raeez-calabi-yau-quantum-groups/memory/session_log_archaeology.md`. The Main Theorems table above is the canonical statement of each result; the archaeology file preserves the historical engine + test count narrative.

## Roadmap: The Platonic Ideal (post-2026-04-17 rewrite-loop session)

The architectural spine: universal extension theorem + V_4 four-phenotype CY-direction classification + CY-D tri-stratum theorem (all inscribed in the 2026-04-17 rewrite-loop session per notes/loop_session_2026_04_17_progress.md).

```
CY_d category --Phi--> E_1-chiral algebra --B^{ord}--> bar complex --D_Ran--> Koszul dual A^! --Rep^{E_2}--> chiral QG
                          |                    |                 |
                          |                    |                 v
              Universal extension       V_4 four-phenotype    Universal Trace
              theorem (sigma_tot*-      classification of      Identity (CONJ.):
              generic CY fixed         CY directions          Vol I K(A) and
              under elliptic           (P_1/P_2/P_3/P_4)      Vol III kappa_BKM
              iteration)              with Künneth fusion     are two reflections
                                                              of one Phi-bridged trace
```

At each step: E_1 (ordered) is the primitive; E_2 (braided) via Drinfeld center; E_3 (6d hCS) via derived center; E_∞ (symmetric) kills Hopf.

Status by dimension:
- d=1: E_∞ (commutative). PROVED. Trivial. CY-D stratum (I) odd: Ξ = 0.
- d=2: E_2 (braided). PROVED (CY-A_2). K3 lattice VOA, Phi_2(K3)=H_Muk, κ_ch=2.
- d=3: E_1 (ordered). PROVED (inf-cat, CY-A_3). Chain-level [m_3,B^{(2)}]!=0 resolved as non-obstruction (HH^{-2}_{E_1}=0, Goodwillie vanishing). K3 abelian Yangian theorem (6-part presentation). 6 independent constructions approach G(K3xE) (only Route 4 = Phi; convergence = CY-C, CONJECTURAL; AP-CY60). Yangian/toroidal from CoHA. CY-D stratum (I) odd: Ξ = 0.
- d=4: P^1-family Phi_4 (CONSTRUCTION). CY-D stratum (II) strict-CY at sextic: Ξ = 2; stratum (III) holomorphic-symplectic K3^[2]: Xi = 3 = n+1. BCOV F_2 zero-correction theorem (PROVED).
- d=5: Z/2-gerbe Phi_5 (CONSTRUCTION + Theorem at K3xK3xE via Whitney/Wu w_5 vanishing). Universal Serre Cancellation: Ξ = 0 universally for compact CY_5 (PROVED).

### Architectural anchors (2026-04-17 rewrite-loop):

(1) **Universal extension theorem** (k3_yangian_chapter.tex): For every sigma_tot*-generic CY input X, M_{X x E^k} = M_X for all k. Subsumes K3-anchored fixed-point. CY^generic sub-category closed under V_4 Künneth (prop:sigma-generic-closed-under-products).

(2) **V_4 four-phenotype classification** (k3_yangian_chapter.tex thm:v4-cy-direction-classification): Every CY direction Y belongs to one of four phenotypes by V_4-Fourier support: P_1 (single-character, K3^[n] absorber), P_2 (anti-pair, E/T^4 doubling), P_3 (par-pair, conifold), P_4 (three-character, K3^BKM/LP^2/quintic maximal). Closed under Künneth fusion; P_4 absorbing, P_1 identity.

(3) **CY-D tri-stratum theorem** (cy_d_kappa_stratification.tex thm:cy-d-tri-stratum): Three mutually-exclusive strata (odd-d Serre / strict-CY even-d / holomorphic-symplectic even-d) governed by Beauville-Bogomolov classification. The kappa_ch landscape lives entirely in even d.

### Seven-part structure (rearchitecture REALISED as item 5, LOSSLESS)

Full proposal (7 parts, ~32 chapters, dependency map, structural rationale) -> `notes/vol3_rearchitecture_proposal.tex`. Current realised length ~838pp. **No page target.** Vol III is as many pages as the mathematics demands — the inner music of the E_n hierarchy at every CY dimension, the K3 Yangian in full, the CY landscape, and the frontier programmes. A short Part is short because its content is concentrated; a long Part is long because its content demands the room. Logical dependencies: I -> II -> III -> {IV, V} -> VI -> VII; Parts IV and V are independent.

**Realised seven-part structure** (main.tex):
- Part I (line 523): Foundations: CY Categories and Cyclic A_inf
- Part II (line 576): The CY-to-Chiral Functor
- Part III (line 632): The E_n Hierarchy and Chiral Quantum Groups
- Part IV (line 709): The K3 Yangian
- Part V (line 794): The CY Landscape
- Part VI (line 851): The Seven Faces of r_CY(z)
- Part VII (line 904): Frontiers

All seven Parts open with substantive prose blocks (35-63 lines each, audited 2026-04-17): Part I (40 lines, bar-cobar input/output), II (44 lines, four-step Phi construction + CY-A_2/A_3 status), III (56 lines, operadic structures + K3 path guidance), IV (63 lines, K3 family climax + six routes + kappa-spectrum), V (43 lines, horizontal survey + shadow class classification + LG/CY correspondence), VI (41 lines, seven r-matrix interpretations + Vol I-II synthesis), VII (35 lines, four open frontiers: Langlands / nonabelian / Zamolodchikov / Sp_4(Z) modularity).

**Item 5 (chapter rearchitecture): REALISED LOSSLESSLY**. Items 1-4, 6-12, 11a + missing M1-M6 inscribed in the 2026-04-17 rewrite-loop session. **Item 11b (Universal Trace Identity bridging-diagram construction): COMPLETE on the entire logarithmic-finite-type class** (chapters/connections/bar_cobar_bridge.tex).

Of 26 chapter assignments, 22 match the proposal exactly; 4 placements refine the proposal organically without moving any content:
- `quantum_chiral_algebras` retained in Part II (proposal: Part III): the boundary algebra OPE + codim-2 defect mechanism is the chiral-construction ENGINE feeding Part III, so it sits with the CY-to-Chiral functor as its constructive payload.
- `derived_categories_cy` retained in Part IV (proposal: Part V): the chapter is K3-specific (Phi_2(K3), HMS for K3) and reads naturally as the lead chapter of the K3 Yangian Part.
- `modular_trace` retained in Part V (proposal: Part II): the chi-O-vanishes-odd-d / BKM modularity content is a CY-landscape-survey result organised by manifold class, not a CY-to-Chiral construction.
- `k3_quantum_toroidal_chapter` retained in Part IV (proposal: Part V): K3 quantum toroidal is structurally tied to the K3 Yangian climax and reads naturally as its toroidal extension.

These four refinements are intentional and were never executed as a "move" — they reflect content evolution between the 2026-April proposal draft and the realised manuscript. The realised seven-part structure is canonical; the proposal stands as the architectural rationale.

**Item 11b detail**: thm:universal-trace-identity-k3-fibered closes the K3-fibered case; thm:universal-trace-identity-non-k3-fibered closes the non-K3-fibered case via the Bruinier-Funke regularised lift (constructions a/b/c: chiral functoriality + Eisenstein-cusp-Trinity-supertrace + Borcherds-product expansion at non-unimodular Λ). The cross-volume bridging diagram closes at full structural level on signature-(b,2) Mukai gradings for b ≥ 1; the only remaining open frontier is numerical evaluation of c_γ(n) at specific X ∈ {quintic, LP², conifold} — a case-by-case modular-form computation, not a structural obstruction.

### Five load-bearing open problems (updated April 2026, ~230-agent final session)

1. **CY-B (E_n-chiral Koszul duality)**: PROGRAMME (131 tests). At d=2: E_2-Koszul on A directly (A is E_2). At d=3: E_1-Koszul on A via B_{E_3}(A), inducing E_2 on Drinfeld center Z(Rep^{E_1}(A)). The conductor formula kappa(A)+kappa(A^!)=rho_K is about the E_1-Koszul dual. Depends on CY-A (now proved). Extended to d=3 via inf-cat CY-A_3. Chain-level conditional on explicit framing data for non-formal algebras. The next structural theorem after CY-A.
2. **Nonabelian K3 Yangian**: The passage from abelian Y(g_{K3}) (PROVED, 24 generators, thm:k3-abelian-yangian-presentation) to the full nonabelian Yangian. Matrix Miura, sl_2 Serre constraints (P_2=0 leading order PROVED; conjecturally exact at all orders, AP40-corrected 2026-04-17, 70 tests at leading order). Super-Yangian Y(gl(4|20)) conjectural. E_8 x E_8 structure function computed: degree-(24,24), c=8+8+8=24.
3. **ZTE correction**: S^{corr}=S+κ²T NOW COMPUTED (exact rational T matrix, 35 tests). Previously constructive (rank 35/36 in extended complex); now explicit entry-by-entry from 1-dim kernel. The correction giving genuine E_3 structure beyond pairwise factorization.
4. **Sp_4(Z) modularity**: E_3 S-matrix -> Siegel modular forms -> Phi_10. Fourier-Jacobi = E_2->E_3 restriction proved. Full pipeline open. Mathieu moonshine connection: frame shape = twined bar Euler for all 25 M_24 conjugacy classes.
5. **Root-of-unity CY quantum groups**: Kazhdan-Lusztig at root of unity for CY categories. Modular tensor categories from Phi. CY-C remains conjectural but abelian K3 case now fully specified: C(g,q) = D(Y^+(g_{K3})), Rep = Rep^{E_2}(Y) via BZFN, R-matrix = MO. Root-of-unity N=2: 324 modules, abelian S-matrix degenerate (non-abelian needed for modularity). Chiral volume conjecture FORMULATED (Abel-Jacobi period).

Compute engines (~460 total, ~34,000 tests). Full catalogue -> `compute/ENGINES.md`. Load-bearing engines for individual theorems are cited in the Main Theorems table above with their test counts.

## Dependencies on Vols I-II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I | Bar-cobar machine, Theta_A, kappa, five theorems, G/L/C/M | CY bar complex, modular trace, shadow depth |
| II | SC^{ch,top}, PVA descent, DK bridge, E_1 sector, H(T) | E_1 chiral theory, braided structure, bulk-boundary |

## Build

(See "## Commands" near the top of this file for the full target list.)

## Session Entry (Vol III additions)

0. If working on Vol I or its standalones, read `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/MASTER_PUNCH_LIST.md` first (9 P0, 16 P1, 16 upgrade paths from the 2026-04-16 adversarial swarm). New AP entries proposed in `notes/new_ap_entries_20260416.md` (AP-CY68 through AP-CY100).

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
14. Super-Yangian Y(gl(4|20)) K3 case is CONJECTURAL (AP-CY35). Never \begin{theorem}. DISTINCT from the GENERAL-RANK super-Riccati Y(sl(m|n)) (session 2026-04-17, `chapters/examples/super_riccati_shadow_tower_platonic.tex`, commit 7a3ea3c): the latter is PROVED at small rank (1|1), (2|1), (1|2), (2|2), (3|1), (3|2), (3|3) via explicit parity-sign recurrence `S_r = -(1/(2rκ_ℓ)) Σ (-1)^{(j-1)(k-1)|ℓ|} f(j,k) jk S_j S_k`. The K3 Y(gl(4|20)) remains conjectural as a specific physical model with Mukai (4,20) signature. Super-complementarity κ(Y(sl(m|n))) + κ(Y(sl(n|m))^!) = **max(m, n)** (NOT 0; Virasoro c+c'=26 analogy REFUTED by direct symbolic computation, Blacklist B86).
15. Class M: Borel summable (Gevrey-1), NOT convergent (AP-CY39).
16. CFG25 agreement: 35% lift rate at perturbative genus-0 only (AP-CY37).
17. 3 wrong proofs caught and retracted this session. The Beilinson principle works.
18. ZTE correction T COMPUTED (exact rational, 35 tests). Previously constructive; now explicit.
19. Mock modular K3: THEOREM at d=2 (4-step proof). Class M = mock modular.
20. CY-D: kappa_ch != chi(O_X) at odd d. Dimension-stratified formula required.
21. Incompatibility: mu_3 != 0 implies mu_2 = 0 on augmentation ideal (chain level, all non-formal).
22. Mathieu moonshine: frame shape = twined bar Euler for all 25 M_24 classes.
23. Root-of-unity N=2: 324 modules, abelian S-matrix degenerate.
24. E_8 x E_8: structure function degree-(24,24), c = 8+8+8 = 24.
25. BKM Serre P_2(D)=0 conjecturally exact (AP40-corrected 2026-04-17): leading-order $P_1(D) = -2D$ proved; higher-order vanishing tagged \begin{conjecture} (engine bkm_serre_higher_order.py self-declares CONJECTURAL). Independent verification at order ε² outstanding.
26. m_5 independently verified: G_5^{conn} = 775/5184 from 5-point Wick contraction.
27. Chiral volume conjecture FORMULATED (Abel-Jacobi period).

## New Failure Modes (2026-04-14 CG Rectification Campaign)

**FM42. Bulk substring replacement corruption.** replace_all "arity"→"degree" corrupts singularity→singuldegree, complementarity→complementdegree, unitarity→unitdegree, regularity→reguldegree, modularity→moduldegree, parity→pdegree. 45 corruptions introduced and fixed. COUNTER: never bulk-replace short substrings; grep `ldegree|ndegree|rdegree|pdegree|tdegree` after any bulk replace. Checklist: {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity}.

**FM43. E_n output scope of Φ.** Φ outputs E_2 at d≤2, E_1 at d≥3. Writing `Φ: CY_d-Cat → E_2-ChirAlg` is WRONG at d≥3. Found in 5 files. COUNTER: always scope with `(n=2 for d≤2; n=1 for d≥3)`.

**FM44. Agent rate limiting.** >10 concurrent agents → mass rate limiting (27/31 failed). COUNTER: batches of 3.

**FM45. Agent skill fidelity gap.** Subagents get ~200-word brief, not the full 15K-word /chriss-ginzburg-rectify skill. Good for violation scanning, insufficient for deep reconstitution. COUNTER: invoke skill directly in main conversation per file.

**FM46. Stale line counts.** Preface assessment line counts drift as chapters grow. 8 counts were off by up to 3x. COUNTER: update after content campaigns.

## Cached First-Principles Analyses (AP-CY61 dictionary)

**Full cache (45 entries, ghost theorems, cross-programme ~264 entries / 30 confusion types, full type taxonomy table)**: `notes/first_principles_cache_comprehensive.md`.

**Top 3 critical entries** (highest recurrence, check these FIRST; full table in cache):

| Wrong claim | Ghost theorem | Correct relationship | Type |
|-------------|---------------|---------------------|------|
| "Drinfeld center = categorified averaging" | av and Z factor: E_1->^Z E_2->^{Sym} E_inf | Center CONSTRUCTS braiding (step 1). Averaging DESTROYS it (step 2). | construction/narration |
| "CoHA = bar complex" | SV theorem: CoHA cong Y^+ | CoHA is ALGEBRA; bar is COALGEBRA. Character M(q) coincidence reflects SV iso. | algebra/coalgebra |
| "{b_k, B^{(2)}}=0 individually" | TOTAL {b,B^{(2)}}=0 true | Per-k FALSE. Cross-arity cancellation via Stasheff. Operadic d^2=0. | part/whole |

## Cross-Volume Anti-Patterns

Vol I APs (AP2-AP157) and Vol I Failure Modes (FM24, FM42-46) live in
`~/chiral-bar-cobar/CLAUDE.md`. Vol II APs (V2-AP1-V2-AP39) live in
`~/chiral-bar-cobar-vol2/CLAUDE.md`. Both files are ALREADY loaded per the
Session Entry directive (item 1). They are not duplicated here. The Vol III-only
"New Failure Modes" block above (FM42-46 in the Vol III campaign context) is
the canonical Vol III statement; the same numeric FMs in Vol I/II carry the
upstream cross-volume context.


## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.

### User-Identified Conceptual Anti-Patterns (AP-CY53-AP-CY58, from manuscript review)

AP-CY53: π₁(Conf₂) ordered vs unordered confusion. π₁(Conf₂(R^d)) = 0 for d≥3 (ORDERED, S^{d-1} simply connected). π₁(UConf₂(R^d)) = Z/2 (UNORDERED). NEVER confuse ordered and unordered configuration spaces. Counter: always specify ordered/unordered.

AP-CY54: "Categorified averaging" for Drinfeld center. The Drinfeld center is the RIGHT ADJOINT to the forgetful functor BrMon→Mon (categorified COMMUTANT z(A)={a:ab=ba}), NOT a categorified averaging map. The averaging map E₁→E_∞ DESTROYS quantum group data. The center E₁→E₂ CONSTRUCTS braiding via half-braidings. Counter: write "categorified center" or "right adjoint to forgetful", never "categorified averaging".

AP-CY55: κ_cat presented as algebraization-dependent. κ_cat = χ(O_X) is a TOPOLOGICAL invariant of the MANIFOLD, not a property of the algebraization. Saying "algebraizations share κ_cat" is VACUOUS (like saying "both share gravity"). Only κ_ch and κ_BKM depend on the algebraization. Counter: separate manifold invariants (κ_cat, κ_fiber) from algebraization invariants (κ_ch, κ_BKM).

AP-CY56: E_n level conflation across CY dimensions. At d=3, A = Φ₃(C) is E₁ (NATIVE). E₂ lives on Z(Rep^{E₁}(A)), NOT on A. NEVER say "E₂-chiral algebra" at d=3 when referring to A itself. The E_n level of A is determined by the Gerstenhaber bracket degree (1-d): d=1→E_∞, d=2→E₂, d≥3→E₁. Counter: always state which object carries the E_n structure (A vs Rep(A) vs Z(Rep(A))).

AP-CY57: Narration instead of construction (Chriss-Ginzburg violation). Saying "the E₂ structure gives the R-matrix" without constructing the half-braiding mechanism. The R-matrix IS the universal half-braiding σ_M(N): M⊗N→N⊗M in Z(Rep^{E₁}(A)). It is CONSTRUCTED from the center, not "given by" or "recovered via" it. Counter: every claim "X gives Y" must be backed by an explicit construction.

AP-CY58: CY-B E_n scope uniformity. CY-B is d-DEPENDENT: E₂-Koszul at d=2 (A is natively E₂), E₁-Koszul at d=3 (A is E₁, inducing E₂ on center via Verdier spectral functor). NEVER say "E₂-chiral Koszul duality" uniformly across all d. Counter: always state the d-dependent E_n level.

AP-CY59: Multiple algebraizations from single functor. Φ(D^b(Coh(K3))) = H_{Muk}. PERIOD. ONE output. The BKM algebra g_{Δ₅} comes from the Borcherds lift (DIFFERENT construction). The Conway module comes from the Leech lattice VOA (DIFFERENT construction). Saying "Φ distinguishes three algebras" is NONSENSE — Φ gives one. Counter: for each algebra, state which CONSTRUCTION produces it. Different κ values come from different constructions, not different applications of Φ.

AP-CY60: Six routes ≠ six applications of Φ. The six routes to G(K3×E) are six DIFFERENT mathematical constructions (Φ, Borcherds lift, lattice VOA, Kummer, sigma model, BLLPR). NOT six applications of the same functor. Their convergence is the CONTENT of CY-C (conjectural), not a consequence of functoriality. Counter: for each route, name the construction and state what it produces independently.

AP-CY61: Shallow correction without first-principles investigation. When a mathematical claim is challenged, do NOT just swap labels (e.g. "averaging"->"right adjoint"). ALWAYS investigate the actual mathematical relationship from first principles. Find: (1) what the claim gets RIGHT (the ghost of a true theorem), (2) what it gets WRONG (the precise conflation), (3) the correct mathematical statement connecting the objects. Every wrong claim contains the seed of a correct theorem -- extract it. Examples: "categorified averaging" is wrong but the factorization E_1 ->^Z E_2 ->^{Sym} E_inf is real; "CoHA = bar complex" is wrong but the character coincidence reflects the Schiffmann-Vasserot theorem CoHA = Y^+; "SN bracket vanishes" is false for non-toric but reveals two independent E_1 mechanisms (operadic vs equivariant). Counter: before any correction, write down the first-principles analysis. If you cannot state the correct theorem, you do not understand the error.
