# AGENTS.md - Calabi-Yau Quantum Groups

## Charter

This file is the always-on Codex constitution for Volume III. It is optimized for Codex with GPT-5.4-style agentic work: persistent tool use, explicit verification, tight scope control, and sharp stopping criteria. `CLAUDE.md` may remain richer and more experimental, but `AGENTS.md` must be the stable operating system that still works after compaction, context loss, or model drift.

Use this file for:

- durable repo-wide invariants;
- task routing and operating modes;
- claim-state and definition discipline;
- cross-volume propagation rules;
- verification and convergence gates;
- the current dated risk map when live repo state materially changes behavior.

Do not use this file for temporary chatter, local TODO spam, or motivational prose that does not change execution.

Today's date is 2026-04-17. All commits authored by Raeez Lorgat only. No LLM attribution anywhere.

## /chriss-ginzburg-rectify (TOP-LEVEL INJUNCTION)

When the user invokes `/chriss-ginzburg-rectify` (or the skill `chriss-ginzburg-rectify`) on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. Analyse the **whole file**, **chunk by chunk**, **linearly from start to finish**, with **small chunk size**. Every line must pass under your eyes.

Binding rules:

- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do not sample. Do not jump. Do not read section heads via Grep and call it Phase 1. Do not read only opening + closing + dense midsection.
- Chunk size: ~250-500 lines per Read call, at most. Large chunks (1000+ lines) approaching the 25000-token Read cap are forbidden.
- Linear progression: start at line 1. Each Read starts exactly where the previous one ended (offset = prev_offset + prev_limit). No ranges skipped; none revisited unless a Phase 3 edit requires re-reading a chunk.
- Coverage is a proof obligation: the sum of all Phase 1 `limit` values equals the file line count; starting offsets form a contiguous cover of [1, EOF]. If you cannot state this, Phase 1 is incomplete.
- Grep does NOT substitute for Phase 1 reading. Grep is Phase 3 cross-file propagation (AP5), not the global diagnostic.
- If a Read fails with the 25000-token cap, cut `limit` in half and retry. Never "skip ahead past the oversized region."
- A 5000-line chapter takes ~10-20 small Reads. That is the cost; it is not negotiable.

## MANUSCRIPT HYGIENE (TOP-LEVEL INJUNCTION, ZERO TOLERANCE)

**NO ANTIPATTERN TAGS OR METADATA LEAKAGE INTO THE MANUSCRIPT OR STANDALONE PAPERS PROPER.**

Reader-facing prose (the compiled `main.pdf` PLUS every standalone paper in `standalone/`, `notes/` when published, or shipped to arXiv/journal) must contain zero manuscript-internal discipline noise. Every violation below is a HARD VIOLATION and must be stripped before commit.

**Prohibited in manuscript prose:**

- AP/AP-CY tag citations ("(AP-CY60)", "(see AP-CY72)", "per AP-CY55", "violates AP113"). The catalogue lives in `CLAUDE.md` / `appendices/anti_pattern_catalogue.tex` (development tree only, NOT `\input`'d by `main.tex`).
- Session timestamps ("2026-04-17 inscription", "the 2026-04-17 campaign", "earlier phrasing superseded").
- Commit hashes in parentheses ("(commit cade61c)").
- Manuscript-version self-reference ("first edition of this volume", "the earlier formulation").
- Healing-status commentary ("was previously wrong", "is now healed", "retracted and replaced", "(status upgraded)").
- Audit language ("the adversarial swarm", "the agent found", "per the audit").
- Internal `RECTIFICATION-FLAG` markers in non-comment prose.

**Where metadata belongs:** commit messages, `notes/` changelog files, the AP catalogue, `CLAUDE.md`, the first-principles cache. The PDF is for Drinfeld, Beilinson, Etingof — not for the rectification audit trail.

**Before every commit that touches `chapters/`, `standalone/`, `main.tex`, `preface`, or any appendix INCLUDED by `main.tex`, grep:**

```bash
grep -rn 'AP-CY\|AP1[0-9]\{2\}\|2026-\|commit [a-f0-9]\{7\}\|inscription\|campaign\|healed\|first edition\|earlier phrasing\|superseded across\|adversarial audit\|the agent found\|RECTIFICATION-FLAG' \
  chapters/ standalone/ main.tex preface 2>/dev/null | grep -v ':[0-9]*:\s*%'
```

Zero hits is the commit gate. Each hit either (a) strips the metadata while preserving the mathematical claim verbatim, or (b) migrates the content to `notes/` / a commit message / the catalogue.

The AP catalogue `\input` in `main.tex` (L1239) is commented out as of 2026-04-17. Any future reintroduction requires explicit user approval.

## Identity

Volume III constructs the geometric source: the functor Phi: CY_d-Cat -> E_n-ChirAlg providing input data for the Vols I-II bar-cobar machine. Flow: CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function.

E_n scope of Phi is d-dependent (FM43):

- d=1: E_infinity (commutative)
- d=2: E_2 (braided)
- d>=3: E_1 (ordered)

At d>=3 the E_2 braided structure lives on the Drinfeld center Z(Rep^{E_1}(A)), NOT on A itself. Writing `Phi: CY_d-Cat -> E_2-ChirAlg` unconditionally is WRONG at d>=3. Always scope `(n=2 for d<=2; n=1 for d>=3)`.

Volume: ~838pp (2026-04-17), ~34,000 tests, ~460 engines. Seven parts with Part openers and 3 reading paths (algebraist, physicist, number theorist): I(Foundations) II(CY-to-Chiral Functor) III(E_n Hierarchy and Chiral Quantum Groups) IV(The K3 Yangian) V(CY Landscape) VI(Seven Faces of r_CY(z)) VII(Frontiers). Notation appendix (541 lines) and AP catalogue (668 lines) installed. 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites.

**Stub status:** 4 genuine stubs <50 lines (AP114): `quantum_groups_foundations` (24), `geometric_langlands` (28), `matrix_factorizations` (29), `modular_koszul_bridge` (13). 3 thin chapters 50-100 lines (`cyclic_ainf` 55, `cy_categories` 70, `e1_chiral_algebras` 90). 6 formerly-stubs now developed >150 lines: `hochschild_calculus`, `braided_factorization`, `drinfeld_center`, `fukaya_categories`, `quantum_group_reps`, `derived_categories_cy`.

## Programme Map

Volume III asks a single question:

> In what precise sense can a Calabi-Yau category produce a quantum chiral algebra whose bar data, trace, and modular characteristic match the modular Koszul duality programme from Volumes I and II?

Primary targets (dimension-scoped):

- **CY-A**: Phi: CY_d-Cat -> E_n-ChirAlg (n=inf at d=1; n=2 at d<=2; n=1 at d>=3).
- **CY-B**: d-dependent Koszul duality (E_2-Koszul at d=2; E_1-Koszul at d=3 inducing E_2 on Drinfeld center via Verdier spectral functor).
- **CY-C**: quantum-group realization (CONJECTURAL; abelian level: C(g,q) = D(Y^+(g_{K3}))).
- **CY-D**: modular CY characteristic (tri-stratum: odd-d Serre / strict-CY even-d / holomorphic-symplectic even-d).

Current hard status boundary:

- **CY-A** is unconditional for d=2 and PROVED at d=3 in the infinity-categorical framework (`thm:derived-framing-obstruction`: HH^{-2}_{E_1}=0, Goodwillie vanishing, E_3-liftings contractible). Chain-level explicit construction at d=3 remains open for non-formal algebras.
- **CY-A_3 dependent results** may now use `\begin{theorem}` IF they rely only on inf-cat existence. Results requiring chain-level framing data at d=3 use `\begin{conjecture}` + `\ClaimStatusConditional`.
- **G(X) and C(g,q)** (quantum group realization, CY-C) are NOT constructed objects. CY-C remains CONJECTURAL. Abelian level: C(g,q) = D(Y^+(g_{K3})).
- **CoHA** is associative data, not automatically the E_1 sector of a larger chiral object (AP-CY7). SV theorem: CoHA ≅ Y^+.
- **Borcherds denominator identities** are not automatically bar Euler products (AP-CY8).

## 6d Holomorphic CS Programme (April 2026, Wave-14 2026-04-17)

The Costello programme constructs chiral quantum groups from holomorphic CS at each dimension:

- 3d hol CS -> Kac-Moody (PROVED, Costello-Gwilliam)
- 5d hol CS -> Affine Yangian (PROVED, Costello 2013)
- 6d hol theory -> Quantum toroidal (CONJECTURAL, Costello-Francis-Gwilliam route)

Key results established in Vol III:

- **E_1-chiral bialgebra** (Section 7 of `e1_chiral_algebras.tex`, ~400 lines, NEW MATH): the correct Hopf framework. Coproduct on E_1 (ordered) side of Swiss-cheese; E_infinity averaging kills Hopf data.
- **E_3 bar cohomology**: (1+t)^{3g} = 2^{3g} for classes L,C; **6^g for class M** (PROVED via Kunneth, closed form).
- **Kummer route**: integral over K3 via CY-A_2 only. Steps 1-4 PROVED; Step 5 conjectural.
- **K3 Yangian**: degree-(24,24) structure function from Mukai lattice.
- **Borcherds lift = resummation**: additive (Saito-Kurokawa) = perturbative; multiplicative (Borcherds product) = non-perturbative.
- **Class M = mock modular**: kappa_ch = -h|_{q^{-1/8}}.
- **Center-hocolim obstruction**: >92% of K3xE Drinfeld center invisible to local charts; MO stable envelopes bypass it.
- **Two-parameter R-matrix**: R_ch(u,v) = R_1(u)R_2(v)R_12(u-v) (Zamolodchikov factorization).
- **E_2 -> E_3 promotion**: derived center (higher Deligne), NOT iterated Drinfeld center.

## Wave-14 Panoramic Synthesis (2026-04-17, Platonic Ideal)

ONE atomic phenomenon: chiral Koszul reflection. THREE lenses: operadic / holographic / geometric. FOUR generating identities G1-G4. ONE universal trace identity kappa_BKM = c_N(0)/2 bridging Vol I K(A)-trace and Vol III kappa_BKM via Phi.

Architectural spine:

```
CY_d category --Phi--> E_n-chiral algebra --B^{ord}--> bar complex --D_Ran--> Koszul dual A^! --Rep^{E_2}--> chiral QG
                          |                    |                 |
                          v                    v                 v
              Universal extension       V_4 four-phenotype    Universal Trace Identity
              theorem (sigma_tot*-      CY-direction          (CONJ.): Vol I K(A) and
              generic fixed under      classification         Vol III kappa_BKM are two
              elliptic iteration)      (P_1/P_2/P_3/P_4)      reflections of one Phi-bridged
                                       with Künneth fusion    trace
```

Status by dimension:

- **d=1**: E_infinity (commutative). PROVED. Trivial. CY-D stratum (I) odd: Xi = 0.
- **d=2**: E_2 (braided). PROVED (CY-A_2). Phi_2(K3) = H_Muk, kappa_ch=2.
- **d=3**: E_1 (ordered). PROVED (inf-cat, CY-A_3). Chain-level [m_3, B^{(2)}] != 0 resolved as non-obstruction (HH^{-2}_{E_1}=0). K3 abelian Yangian (6-part presentation). Six independent constructions approach G(K3xE); only Route 4 = Phi; convergence = CY-C (CONJECTURAL; AP-CY60).
- **d=4**: P^1-family Phi_4 (CONSTRUCTION). CY-D stratum (II) strict-CY at sextic: Xi = 2; stratum (III) holomorphic-symplectic K3^[2]: Xi = 3 = n+1. BCOV F_2 zero-correction theorem (PROVED).
- **d=5**: Z/2-gerbe Phi_5 (CONSTRUCTION + Theorem at K3xK3xE via Whitney/Wu w_5 vanishing). Universal Serre Cancellation: Xi = 0 for compact CY_5 (PROVED).

**Architectural anchors (2026-04-17 rewrite-loop):**

1. **Universal extension theorem** (`k3_yangian_chapter.tex`): for every sigma_tot*-generic CY input X, M_{X x E^k} = M_X for all k. Subsumes K3-anchored fixed-point. CY^generic sub-category closed under V_4 Künneth (`prop:sigma-generic-closed-under-products`).
2. **V_4 four-phenotype classification** (`k3_yangian_chapter.tex`, `thm:v4-cy-direction-classification`): every CY direction Y belongs to one of four phenotypes by V_4-Fourier support: P_1 (single-character, K3^[n] absorber), P_2 (anti-pair, E/T^4 doubling), P_3 (par-pair, conifold), P_4 (three-character, K3^BKM/LP^2/quintic maximal). Closed under Künneth fusion; P_4 absorbing, P_1 identity.
3. **CY-D tri-stratum theorem** (`cy_d_kappa_stratification.tex`, `thm:cy-d-tri-stratum`): three mutually-exclusive strata (odd-d Serre / strict-CY even-d / holomorphic-symplectic even-d) governed by Beauville-Bogomolov classification. The kappa_ch landscape lives entirely in even d.
4. **Universal Trace Identity** (`chapters/connections/bar_cobar_bridge.tex`): bridging diagram closed at full structural level on signature-(b,2) Mukai gradings for b>=1 (logarithmic-finite-type class). `thm:universal-trace-identity-k3-fibered` + `thm:universal-trace-identity-non-k3-fibered` via Bruinier-Funke regularised lift. Only open frontier: numerical evaluation of c_gamma(n) at specific X in {quintic, LP^2, conifold}.

## Main Theorems (2026-04-17)

| Theorem | Status | Notes |
|---------|--------|-------|
| **CY-A** (CY-to-chiral functor) | d=2 PROVED; d=3 PROVED (inf-cat) | d=3 chain-level [m_3, B^{(2)}] != 0 resolved: not an obstruction in inf-cat framework (HH^{-2}_{E_1}=0). Goodwillie layers vanish. Space of E_3-liftings contractible. |
| **CY-B** (E_n-chiral Koszul duality) | d=2 PROVED; d=3 PROVED (inf-cat) | d=2: E_2-Koszul on A directly (A is E_2). d=3: E_1-Koszul on A via B_{E_3}(A), inducing E_2 on Drinfeld center Z(Rep^{E_1}(A)) via Verdier spectral functor. `thm:cy-b-d3`, `thm:verdier-spectral-functor`. CY-B1 (conductor): proved all classes. CY-B2 (braided equiv on center): proved all classes. 326 tests. |
| **CY-C** (Quantum group realization) | CONJECTURAL | Abelian level: C(g,q) = D(Y^+(g_{K3})). Three routes (chiral/BFN/MO). Rep(C) = Rep^{E_2}(Y) via BZFN. `cy_c_quantum_group_k3` (104 tests). Uses `\begin{conjecture}`. NEVER `\begin{theorem}`. |
| **CY-D** (Modular CY characteristic) | d=2 PROVED; d=3 tri-stratum | Hodge-supertrace reading kappa_ch = chi(O_X) PROVED unconditionally for compact CY_d via `thm:kappa-hodge-supertrace-identification` (cy_d_kappa_stratification.tex:177), giving chi(O_{K3xE}) = 0. The Heisenberg-level reading kappa_ch^{Heis} is additive under products and gives kappa_ch^{Heis}(K3xE) = 2+1 = 3 != 0 (cf. AP289, `rem:beauville-kappa-formula-subscript-split`). chi^CY is categorical, distinct from chi(O_X). `cy_d_kappa_d3` (76 tests). Dimension-stratified: tri-stratum theorem. |
| **E_3 Koszul (Heisenberg)** | d=2 PROVED | `thm:e3-koszul-heisenberg`, 39 tests |
| **E_3 Koszul (Yangian)** | COHOMOLOGICAL PROVED | `thm:e3-koszul-yangian`, 36 tests |
| **E_2 Koszul (Heisenberg)** | d=2 PROVED | `thm:e2-koszul-heisenberg`, 49 tests |
| **Kummer route Steps 1-4** | PROVED | `prop:kummer-orbifold`, 85 tests |
| **E_1-chiral bialgebra axioms** | FOUNDATIONAL | `sec:e1-chiral-bialgebras`, 80 tests |
| **ZTE deformation cohomology** | PROVED | `prop:zte-deformation-cohomology`, 47 tests |
| **BKM weight universality** | PROVED | `prop:bkm-weight-universal`, `kappa_bkm_universal` (99 tests). kappa_BKM = c(0)/2 unconditional for all K3-fibered CY3. Does NOT depend on CY-A. |
| **Phi(K3) explicit** | d=2 PROVED | `thm:phi-k3-explicit`, `phi_k3_explicit_evaluation` (93 tests) |
| **K3 abelian Yangian presentation** | d=2 PROVED | `thm:k3-abelian-yangian-presentation`, `k3_abelian_yangian_presentation` (47 tests) |
| **Hopf fibration decomposition** | PROVED (negative) | `prop:hopf-fibration-decomposition`, S^3 framing non-decomposable (67 tests) |
| **Cyclic A_inf framing compat** | PROVED (corrected) | `prop:cyclic-ainf-framing-compat`. Original claim [m_k, B^{(2)}] = 0 individually is FALSE for non-formal (`obs_ainf_local_p2`, 54 tests). Corrected: {b, B^{(2)}} = 0 for TOTAL b = sum_k b_k, via Costello TCFT d^2=0 (`operadic_tcft_mk_b2_engine`, 43 tests). Cross-arity cancellation: {b_3, B^{(2)}} cancelled by {b_2, B^{(2)}} via Stasheff. Obs_Ainf = 0 UNIVERSALLY. |
| **Cech-HTT coefficient convergence** | PROVED | `prop:cech-htt-coefficient-convergence`, `cech_htt_convergence` (64 tests) |
| **K3 quantum toroidal** | CONJECTURAL | `conj:k3-quantum-toroidal`, `k3_quantum_toroidal` (51 tests) |
| **MO R-matrix charge 2** | PROVED | `prop:mo-rmatrix-charge2`, `mo_rmatrix_k3_charge2` (60 tests) |
| **Derived framing obstruction vanishes** | PROVED | `thm:derived-framing-obstruction`, `derived_framing_obstruction` (51 tests). HH^{-2}_{E_1} = 0 by unit-connectedness. All Goodwillie layers vanish. Space of E_3-liftings contractible. |
| **Shadow = A_inf coproduct tower** | PROVED | S_k = delta^{(k)} (coproduct correction at order k). Shadow-Feynman: L-loop = S_{L+1}. |
| **Chiral CE complex** | PROVED | B(U^ch(L)) = CE_*(L). `chiral_ce_complex` engine (66 tests). |
| **Class M E_3 bar dim** | PROVED | dim H*(B^{E_3}(A)) = 6^g for class M (closed form via Kunneth). Chain: P(q)^{6g}. |
| **CY-A_3 inf-categorical** | PROVED | Obstruction group HH^{-2}_{E_1} = 0. Space of framings contractible. Chain-level [m_3, B^{(2)}] != 0 is NOT an obstruction. |
| **kappa_BKM = c_N(0)/2 universal** | PROVED | The ONLY correct universal formula. Naive decomposition kappa_BKM = kappa_ch + chi(O_fiber) fails at N>=2. 99 tests. |
| **BKM Serre at D=3** | PROVED | Serre relations from BKM imaginary roots at discriminant D=3. Null vector g_{i0} * g_{i1} = 1. `k3_serre_relations` engine (61 tests). |
| **CFG25 comparison** | VERIFIED | CFG (arXiv:2602.12412) E_3 from BV-quantised CS. Agreement at perturbative genus-0. Costello 5d verification charge 4 (87 tests). 35% lift rate (76% require chain-level corrections). |
| **Super-Yangian Y(gl(4\|20))** | CONJECTURAL | BKM-to-Yangian lift from Mukai signature (4,20). `k3_super_yangian` (59 tests). Distinct from GENERAL-RANK super-Riccati Y(sl(m\|n)) PROVED at (1\|1), (2\|1), (1\|2), (2\|2), (3\|1), (3\|2), (3\|3). Super-complementarity: kappa(Y(sl(m\|n))) + kappa(Y(sl(n\|m))^!) = **max(m,n)** (NOT 0). |
| **6 routes to G(K3xE)** | PROGRAMME (CY-C) | Six independent CONSTRUCTIONS (not six applications of Phi; AP-CY60): Kummer, Borcherds, MO stable envelope, McKay, factorization homology, Costello 5d. Only Route 4 uses Phi. Convergence = CY-C (CONJECTURAL). |
| **Borcherds spectral flow** | PROVED | Spectral flow automorphisms of Y(g_{K3}) from Borcherds vertex operators. `borcherds_vertex_yangian` (75 tests). h=1 EXACT. |
| **Shadow-Feynman dictionary** | PROVED | L-loop Feynman graph = shadow invariant S_{L+1}. Class G: tree-level exact. Class M: all-loop. |
| **E_3 bar = 6^g** | PROVED | dim H*(B^{E_3}(A)) = 6^g for class M. Chain: P(q)^{6g}. Classes L,C: 2^{3g} = (1+t)^{3g}. |
| **Derived Satake** | CONJECTURAL | Derived geometric Satake for CY categories. |
| **Chiral Satake for C^3** | PROVED | Derived geometric Satake for C^3 via chiral bar complex. 99 tests. Connects Phi(C^3) to geometric representation theory. |
| **Tropical cluster** | PROGRAMME | Tropical cluster varieties as CY moduli. |
| **Chiral Verlinde** | CONJECTURAL | Chiral Verlinde formula for CY chiral algebras. |
| **Hitchin quantization** | PROGRAMME | Hitchin system quantization via CY-to-chiral functor. |
| **BLLPR connection** | VERIFIED | Bringmann-Lovejoy-Mahlburg mock modular forms. Shadow = 24*eta^3 for W(2). |
| **Explicit ZTE correction T** | COMPUTED | Exact rational T matrix solving S^{corr} = S^{fact} + kappa^2 * T. 35 tests. Explicit entry-by-entry from 1-dim kernel. |
| **p-adic Langlands** | CONJECTURAL | p-adic Langlands via p-adic CY motives. |
| **BFN Coulomb** | PROGRAMME | BFN Coulomb branch as CY chiral algebra source. |
| **Form factors** | PROGRAMME | Chiral form factors from bar complex on surfaces with punctures. |
| **Handle decomposition** | PROVED | K3 handle decomposition for factorization homology. 4 handles, Euler char 24. |
| **Stratified FH** | PROGRAMME | Stratified factorization homology for singular CY spaces. |
| **Mathieu moonshine** | PROGRAMME | M24 moonshine for K3 sigma model via chiral bar complex. Frame shape = twined bar Euler for all 25 M_24 classes. |
| **Class M Borel summable** | PROVED | Gevrey-1 divergent and Borel summable. Stokes automorphism from BKM imaginary root multiplicity. |
| **3 wrong proofs caught** | DOCUMENTED | (1) Bidegree decomposition for {b_k, B^{(2)}} = 0 (flawed premise). (2) Tsygan formality (wrong scope). (3) kappa_BKM naive decomposition (numerical coincidence). All retracted. |
| **P_2(D) = 0: BKM Serre** | CONJECTURAL (AP40-corrected 2026-04-17) | Second Serre polynomial conjecturally vanishes. Engine `bkm_serre_higher_order.py` self-declares CONJECTURAL; manuscript previously stated as theorem (AP40 violation). Healed via downgrade in `working_notes.tex` `conj:bkm-serre-exact`. Leading-order P_1(D) = -2D PROVED; higher-order tagged `\begin{conjecture}`. Independent verification at order eps^2 outstanding. |
| **Borcherds spectral flow h=1 EXACT** | PROVED | Not approximate. Verified against Borcherds product through 10 Fourier coefficients. |
| **CY-B push at d=3** | PROGRAMME (131 tests; inf-cat framework) | E_1-chiral Koszul duality (inducing E_2 on center via Verdier spectral functor) extended to d=3 via inf-cat CY-A_3. Chain-level for non-formal algebras is CONDITIONAL on explicit framing data (AP-CY11/14 scope). Main `CY-B` row above states d=2 + d=3 PROVED at inf-cat level (`thm:cy-b-d3`, 326 tests); this row records the narrower push-theorem scope. |
| **Chain-level Incompatibility Theorem (strengthened)** | PROVED | mu_3 != 0 forces mu_2 = 0 on augmentation ideal. A_inf obstruction to simultaneous E_1 and E_infinity structure at chain level. Holds for ALL non-formal A_inf algebras (class >= L). |
| **Notation appendix** | INSTALLED (541 lines) | Complete notation reference for Vol III. |
| **AP catalogue** | INSTALLED (668 lines) | AP-CY1 through AP-CY40 with decision trees and counter-templates. `\input` commented in main.tex 2026-04-17. |
| **10 proofs publication-upgraded** | DOCUMENTED | Kummer Steps 1-4, E_3/E_2 Koszul Heisenberg/Yangian, ZTE deformation cohomology, universal coproduct, Phi(K3) explicit, K3 abelian Yangian, derived framing obstruction. |
| **Part openers + reading paths** | INSTALLED | All 7 Part openers written (35-63 lines each). 3 reading paths (algebraist, physicist, number theorist). |
| **kappa_ch deep mechanism** | PROVED | Hodge-filtered supertrace: non-F^0 contributions killed by Hodge filtration. kappa_ch = str_{F^0}(q^{L_0}). |
| **CY-D at d=3 deep issue** | DOCUMENTED | chi(O_{K3xE}) = 0 != 3 = kappa_ch^{Heis}(K3xE) (Heisenberg-level additive reading). The Hodge-supertrace reading kappa_ch = chi(O_X) coincides with kappa_cat unconditionally on compact CY_d via `thm:kappa-hodge-supertrace-identification`, giving 0 for K3xE. The two readings differ by delta kappa_ch = kappa_ch^{Heis} - chi(O_X); at d=2 with h^{1,0}=0 they coincide (Serre duality kills the quantum correction, `prop:cy-kappa-d2`); at d=3 with h^{1,0}=0 delta kappa_ch = chi_top/24 (BCOV); at d=3 on K3xE the fiber h^{1,0}(E) = 1 breaks the d=2 hypothesis and produces delta = 3. Tri-stratum formula replaces naive CY-D. |
| **ZTE T matrix COMPUTED** | PROVED | Exact rational T matrix, 35 tests. Explicit entry-by-entry from 1-dim kernel. |
| **Shadow tower through m_8** | COMPUTED | 160 tests. S_3=2, S_4=10/27, ..., S_8 = 4144720/19683. |
| **m_5 independent verification** | VERIFIED | G_5^{conn} = 775/5184 from 5-point Wick contraction. |
| **Chiral volume conjecture** | CONJECTURAL | Abel-Jacobi period. Connects chiral bar volume to CY period integrals. |
| **Mock modular K3 theorem** | d=2 PROVED | 4-step proof: (1) shadow = 24*eta^3, (2) mock theta transform, (3) Zwegers completion, (4) Borcherds lift. |
| **CY-D dimension-stratified** | PROVED (tri-stratum) | kappa_ch != chi(O_X) at odd d. Tri-stratum theorem: odd-d Serre / strict-CY even-d / holomorphic-symplectic even-d. |
| **CY-C abelian level** | CONSTRUCTIVE | C(g,q) = D(Y^+(g_{K3})) at abelian level. Explicit Drinfeld double of positive part of K3 Yangian. |
| **E_8 x E_8 structure function** | COMPUTED | degree-(24,24), c = 8+8+8 = 24. Mukai lattice decomposition via E_8 x E_8. |
| **Root-of-unity N=2** | COMPUTED | 324 modules (= 24*N^2*3/4 = 324 for N=2). Abelian S-matrix degenerate. Non-abelian K3 Yangian needed for modularity. |
| **Mathieu frame shape** | VERIFIED | Frame shape = twined bar Euler for all 25 M_24 conjugacy classes. |
| **BP conductor polynomial identity** | PROVED (sympy-verified, 2026-04-16) | c(BP_k) + c(BP_{-k-6}) = 196. c-98 = -24u - 96/u in u=k+3 (odd). c=98 has roots k = -3 +/- 2i only. Replaces meaningless kappa(BP_{-3}) = 49/3. Vol I: `bp_self_duality.tex` healing target. |
| **W_N central-charge conductor** | PROVED (cubic, multi-source, wave 7+8) | K^c_N := c(W_N^k) + c(W_N^{k'}) = 4N^3 - 2N - 2. Values K_2=26, K_3=100, K_4=246, K_5=488. Third difference = 24 constant. Multi-source verified including K_kappa(W_4) = (13/12) * 246 = 533/2. |
| **W_N kappa-conductor** | PROVED | K^kappa_N := kappa + kappa' = K^c_N * (H_N - 1). DISTINCT invariant from K^c. Both correctly called "Koszul conductor"; naming discipline (K^c vs K^kappa) required to avoid AP-CY55-type confusion. |
| **delta F_2(W_3) = (c+204)/(16c)** | PROVED (multi-source, wave 7) | 204 = 4*51 from 3 independent verifications: 4-graph sum, large-c tadpole limit, universal N-formula at N=3. ProvedElsewhere -> ProvedHere. |
| **CY-C pentagon correction** | HEALED (Vol III commit `cade61c`) | Pentagon stratification {3, 12, 24} is GENERATOR RANK rho^{R_i}, NOT kappa_ch. Hodge supertrace invariant = 0 route-independent for K3 x E. AP-CY71. |

**Cumulative Vol III**: ~838pp, ~34,000 tests, ~460 engines, 22/290 Independent-Verification coverage.

## Commands

```bash
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

**Independent verification coverage (2026-04-16, cross-volume):**

- Vol III: 22 / 290 ProvedHere
- Vol II:  61 / 1322
- Vol I:   49 / 2496
- **Total: 132 / 4108 disjointly-verified = 3.2%**

**All three volumes: AUDIT RESULT: PASS** (zero tautologies, zero orphans). Orphan healings applied Option 1 across-the-board (no downgrades). Vol II expansion installed 15 new decorators on triality-y-algebra + SC heptagon + climax theorems. Vol I additions: shadow tower S_6, S_7, S_8 (c-exponent = r-3, (5c+22)-exponent = floor((r-2)/2)); S_9(Vir_c) = -1280(2025c^2 + 15570c + 29554)/[3c^6 * (5c+22)^3] via Riccati recurrence. Campaign advances incrementally.

## The kappa-Spectrum (AP113 + AP-CY55, CRITICAL)

Bare `kappa` is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript.

**AP-CY55**: the four kappas split into two TYPES. Conflating them is forbidden.

**Manifold invariants** (topological, fixed by the geometry, INDEPENDENT of algebraization):

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| `kappa_cat` | chi(O_X) = holomorphic Euler char | 0 = chi(O_{K3xE}); fiber value chi(O_K3) = 2 |
| `kappa_fiber` | Lattice rank / fiber structure | 24 (Mukai lattice rank) |

**Algebraization invariants** (depend on WHICH chiral/BKM algebra is constructed):

| Subscript | Meaning | K3 x E value |
|-----------|---------|--------------|
| `kappa_ch^{Heis}` | From chiral algebra A_C via Phi, Heisenberg-level (additive) reading | 3 (= kappa_ch^{Heis}(K3) + kappa_ch^{Heis}(E) = 2 + 1). Distinct from the Hodge-supertrace reading kappa_ch(K3 x E) = chi(O_{K3 x E}) = 0 (thm:kappa-hodge-supertrace-identification, `cy_d_kappa_stratification.tex:177`); see `rem:beauville-kappa-formula-subscript-split` and AP289 (Kunneth-multiplicative vs additive). |
| `kappa_BKM` | From Borcherds-Kac-Moody algebra | 5 (weight of Delta_5) |

Saying "algebraizations share kappa_cat" is VACUOUS: kappa_cat and kappa_fiber are topological invariants of the manifold and cannot vary between algebraizations. Only kappa_ch^{Heis} (additive) and kappa_BKM depend on the algebraization; the Hodge-supertrace reading kappa_ch = chi(O_X) is Kunneth-multiplicative and coincides with kappa_cat on compact CY_d with h^{1,0}=0 (`thm:kappa-hodge-supertrace-identification`).

kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch^{Heis} and kappa_BKM (and, separately, kappa_ch^{Heis} vs Hodge-supertrace kappa_ch). Full spectrum: {0, 2, 3, 5, 24}.

**Critical clarification (AP-CY68)**: kappa_cat(K3 x E) = chi(O_{K3xE}) = 0 (TOTAL SPACE, Kunneth: chi(O_K3) * chi(O_E) = 2 * 0 = 0; Hodge-supertrace kappa_ch agrees via `thm:kappa-hodge-supertrace-identification`). The value 2 = chi(O_K3) is kappa_cat of the K3 FIBER. The conjectural BKM decomposition uses the fiber value and the Heisenberg-level reading: kappa_BKM = kappa_ch^{Heis} + chi(O_K3) = 3 + 2 = 5.

**ADVERSARIAL RESULT** (`kappa_bkm_adversarial.py`, 62 tests): the decomposition kappa_BKM = kappa_ch^{Heis} + chi(O_fiber) is a NUMERICAL COINCIDENCE for K3 x E (N=1). It FAILS for all Z/NZ-orbifolds with N >= 2. Correct universal formula: **kappa_BKM = c_N(0)/2** (Borcherds weight theorem). See `rem:bkm-decomposition-adversarial` in `k3_times_e.tex`.

**UNIVERSAL RESULT** (`kappa_bkm_universal.py`, 99 tests, `prop:bkm-weight-universal`): kappa_BKM = c(0)/2 is a THEOREM (Borcherds 1998), PROVED unconditionally for ALL K3-fibered CY3s (Class A). Does NOT depend on CY-A. Proof chain: K3 elliptic genus -> orbifold averaging -> Borcherds weight theorem. For non-K3-fibered CY3s (Class B: quintic, C^3, conifold, local P^2), kappa_BKM is UNDEFINED; replacement: kappa_BCOV = chi(X)/24. CY3 families: 9 Class A (8 diagonal orbifolds + STU), 6 Class B. Monotonicity: kappa_BKM weakly decreasing in orbifold order N.

## HOT ZONE — Top Vol III Repeat Offenders

Read this section BEFORE any Edit.

### HZ3-1. AP-CY6/AP-CY14 (unconstructed A_X in theorem environment)

Decision tree, answer BEFORE writing `\begin{theorem}`:

```
Q1: Does the proof chain pass through A_X for d=3, G(X), C(g,q), or any
    object whose existence is part of the d=3 programme?
    YES -> CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction).
           Results depending on CY-A_3 via inf-cat framework: \begin{theorem} OK.
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

Vol III default: `\begin{conjecture}` for CY-C-dependent results.

**E_1-chiral notions collapse to two on the Koszul locus (HEALED 2026-04-17 in Vol I `thm:e1-chiral-notions-collapse`, `algebraic_foundations.tex`):** notions (A) strict ChirAss, (B) A_inf in End^{ch}_A, (C) EK quantum VA, (E) factorization on Ran^{ord}(X) are mutually Quillen-equivalent on the Koszul locus via Stasheff truncation + Etingof-Kazhdan + Beilinson-Drinfeld D-module realization. Only (D) double-A_inf remains genuinely distinct (open problem, `conj:double-ainfty-notion-D-relation`). Operational registry is two: ordinary E_1-chiral input + speculative (∞,2)-enhancement. Outside the Koszul locus the five-fold distinction still applies.

### HZ3-2. AP113 (bare kappa)

ZERO TOLERANCE. Before writing ANY `\kappa`:

```
(i)  Subscript present?  Required: {ch, cat, BKM, fiber}
(ii) Forbidden subscripts: {global, BPS, eff, total, naive, MacMahon}
     If you wrote BPS, you mean BKM. Rename now.
(iii) Meta-naming "kappa-spectrum" / "kappa-value":
     write \kappa_\bullet (bullet = indexing variable across approved set).
```

Decision tree:

- chiral algebra A_C / Phi(C) -> `\kappa_{\mathrm{ch}}`
- Borcherds-Kac-Moody / Igusa weight -> `\kappa_{\mathrm{BKM}}`
- Holomorphic Euler char chi(O_X) -> `\kappa_{\mathrm{cat}}`
- Lattice rank / fiber structure -> `\kappa_{\mathrm{fiber}}`

### HZ3-3. AP-CY11 (conditional propagation)

If a result depends on Conjecture X which depends on CY-A_3, the result IS conditional on CY-A_3. Use `\ClaimStatusConditional` and state the dependency chain.

Template before `\ClaimStatusProvedHere`:

```
Q: Does this result's proof chain reach back to CY-A_3 or any unconstructed object?
   NO  -> ProvedHere OK
   YES -> ClaimStatusConditional + name the chain in the body
```

### HZ3-4. AP-CY7 (CoHA vs E_1-chiral)

The Cohomological Hall Algebra is associative, NOT a chiral algebra. Forbidden conflations:

```
"CoHA = E_1-chiral algebra"                 WRONG
"E_1-sector of G(X)"                         assumes G(X), AP43 violation
"CoHA carries a vertex algebra structure"   WRONG (Hall product)
```

CoHA is Hochschild cohomology of the quiver-with-potential category, with SVYZ multiplication. Connection to chiral algebras is via Phi (CY-A), not by identification. SV theorem: CoHA ≅ Y^+.

### HZ3-5. AP-CY3/AP-CY4 (E_2, Drinfeld center, derived center)

Three distinct objects:

```
1. E_2-monoidal category C  =  little 2-disks structure (NOT symmetric).
2. Drinfeld center Z(C)     =  monoidal-category center via half-braidings.
3. Derived center Z^der_ch(A) =  Hochschild cochains, the bulk algebra.
```

NEVER conflate. Drinfeld center is the categorification of derived center (modular envelope).

### HZ3-6. AP-CY8 (Borcherds denominator vs bar Euler product)

For K3 x E, `Phi_10 = bar Euler product` is an OBSERVATION conditional on:

- CY-A_2 (PROVED at d=2)
- Vol I Borcherds-lift identification of bar Euler products

Any sentence equating automorphic forms and bar Euler products MUST cite both CY-A and the Vol I anchor explicitly.

### HZ3-7. AP-CY17 (MF(W) CY dimension)

For W: A^n -> A^1, MF(W) is CY of dimension `n-2`, NOT `n-1`.

```
W: A^n -> A^1, n = ?
MF(W) is CY_{n-2}; check n-2 against desired CY dimension.
n=2: CY_0 (ADE Lie algebras, semisimple)
n=3: CY_1
n=4: CY_2 (compact K3 surfaces from quartic)
n=5: CY_3 (compact threefolds from quintic)
```

### HZ3-8. AP-CY10 (flop vs Koszul dual)

Birational flop X -> X^+ is a derived equivalence; it PRESERVES kappa_ch. Koszul dual A -> A^! has kappa(A) + kappa(A^!) = K (family-dependent conductor).

```
"flop is the Koszul dual"          WRONG
"kappa(A_X) + kappa(A_{X^+}) = 0"  WRONG (flops preserve kappa)
"kappa(A_X) = kappa(A_{X^+})"      RIGHT (flop is autoequivalence)
```

### HZ3-9. AP-CY12 (shadow class from full tower)

G/L/C/M classification MUST be computed from the full shadow tower, NOT generator counting or non-formality alone.

```
"X has m_3 != 0"                        necessary for class >= L; not sufficient.
"shadow tower terminates at depth 2"    class L (verified by computation).
"m_n != 0 for all n"                    class M (full tower computation required).
"local P^2 has 3 generators"            inadequate for class. Compute the tower.
```

Local P^2 IS class M (infinite depth), NOT class L.

### HZ3-10. AP-CY13/V2-AP26 (cross-volume Part references)

NEVER hardcode `Part~IV`, `Chapter~12` in Vol III prose. Always use `\ref{part:...}`.

```
(i)  Use \ref{part:foo}, never Part~N
(ii) After ANY restructuring, grep ALL THREE volumes for stale Part refs:
     grep -rn 'Part~[IVXL]' chapters/ appendices/ standalone/
(iii) Verify every match resolves to a current part label
```

### HZ3-11. Independent Verification Protocol (cross-volume, 2026-04-16)

**STANDALONE — all material to use this protocol is contained here.**

#### Why this exists

The 2026-04-16 adversarial audit of Vol III found many `\ClaimStatusProvedHere` theorems backed by test suites tautological by construction: engines hardcoded data tables like `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with the verified identity (`weight := c_0 / 2`) built into the row itself. No claim was genuinely verified.

This failure mode propagates silently:

1. tex prose paraphrases a partial result universally ("proved unconditionally");
2. engine takes the paraphrase as definition and hardcodes target values;
3. tests check arithmetic identities against the hardcoded table;
4. CLAUDE.md inherits the paraphrase without scope;
5. next session reads CLAUDE.md, not the .tex.

Rules that fix this ("always verify", "never hardcode") proved ineffective. The protocol replaces them with a mechanical, machine-checked invariant.

#### The mechanical invariant

Every test claiming to verify a ProvedHere theorem must declare:

- `derived_from`: canonical names of data/papers/conventions the formula came from.
- `verified_against`: canonical names of independent data/papers/conventions the test uses to compute its expected value.
- `disjoint_rationale`: one-sentence explanation why the two sets are genuinely independent.

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
        "Mukai/Betti gives rank as topological invariant without HH_* or "
        "chiral construction. Independent derivations."),
)
def test_total_dimension_24():
    ...
```

Decorator registers the test, performs disjointness check at import time, preserves test behaviour. No-op on pass.

#### Enforcement

- `make verify-independence`          — summary audit
- `make verify-independence-verbose`  — lists every uncovered claim

Audit scrapes `chapters/`, `appendices/`, `notes/`, `working_notes.tex` for `\ClaimStatusProvedHere` tags, imports every test module to populate registry, reports:

- ProvedHere claims found (count).
- Claims with at least one independent decorator (coverage).
- Tautological decorations (should be zero; they fail at import).
- Orphan entries: decorators whose `claim` label is not actually ProvedHere.

Exit status: `0` on clean pass, `2` on any tautology or orphan. Coverage percentage is a metric, NOT a gate — enforcing a floor would incentivize low-quality "independent" tests.

#### Three healings when honest decoration fails

1. **Find a disjoint verification source.** Best outcome.
2. **Restrict the scope.** Replace `\begin{theorem}` with `\begin{proposition}[for the 8 diagonal Z/NZ symplectic orbifolds]` and note the general case is conjectural.
3. **Downgrade status.** Replace `\ClaimStatusProvedHere` with `\ClaimStatusConjectured`. Fallback: a "proved" claim without independent test should not be tagged as proved.

Audit does NOT automatically choose; it surfaces the choice. Vol III working queue: `notes/tautology_registry.md` (seeded 2026-04-16: `prop:bkm-weight-universal`, `thm:derived-framing-obstruction`, `prop:cy-a-three-saga-resolution-costello`, `prop:p2-vanishes-exact`, `sec:k3e-six-routes`).

#### Protocol for new theorems

Before writing `\ClaimStatusProvedHere`:

1. Ask: "What is my independent verification source?"
2. If you cannot name one: restrict scope or use `\ClaimStatusConjectured`.
3. Write the test with `@independent_verification(...)` from day one.
4. Run `make verify-independence` before commit.

Decorator is an assertion about mathematical practice, not a bureaucratic tag. A claim without independent verification cannot be distinguished from a circular fit.

#### Files (cross-volume, identical code)

- `compute/lib/independent_verification.py`           — decorator + registry + disjointness check
- `compute/scripts/audit_independent_verification.py` — .tex scrape + registry cross-check
- `compute/tests/test_independent_verification_infra.py` — self-test (7 tests of the infra)
- `notes/INDEPENDENT_VERIFICATION.md`                 — protocol doc
- `notes/tautology_registry.md`                       — Vol III working queue

### HZ3-12. AP-CY61 (first-principles investigation, mandatory)

When challenged on a mathematical claim, do NOT just swap labels. Investigate from first principles. For every confusion, mistake, or wrong claim, answer ALL THREE:

(a) What does the claim get RIGHT? (the ghost of a true theorem)
(b) What does it get WRONG? (the precise conflation)
(c) What is the CORRECT mathematical relationship?

Every wrong claim contains the seed of a correct theorem — extract it. If you cannot state the correct theorem, you do not understand the error.

Examples (this protocol uncovered them):

- "categorified averaging" wrong; factorisation E_1 ->^Z E_2 ->^{Sym} E_inf real.
- "CoHA = bar complex" wrong; Schiffmann-Vasserot CoHA ≅ Y^+ real.
- "kappa(BP_{-3}) = 49/3" wrong as value; c(k) + c(-k-6) = 196 polynomial identity real.
- "Gravitational Yangian Y(Vir_{13})" wrong; shadow tower coalgebra structure real.

### HZ3-13. AP-CY83 (standalone-vs-chapter drift, MUST-CHECK at submission)

Standalones submitted to journals systematically LEAK caveats present in parent chapters. Pattern consistent across waves 6+7 of 2026-04-16 swarm:

- BP self-dual point warning in `bp_self_duality.tex` Prop 4.7 dropped in 2 cross-reference files.
- L^sh Eisenstein poles disclaimer in `chapters/connections/arithmetic_shadows.tex` violated in `standalone/arithmetic_shadows.tex`.
- ChirHoch {0,2} occupation (chapter, correct) stated as {0,1,2} amplitude (standalone, misleading).
- CY-A_3 status overclaim cascade in `programme_summary.tex`: three contradictory framings in one document.

Counter: before any standalone is shipped, diff against chapter version. Every "this fails when X" warning in chapter must be present (or honestly handled) in the standalone.

### HZ3-14. AP-CY84 (amplitude vs occupation, prose discipline)

- "H^i concentrated in {0, 2}" — OCCUPATION (H^1 = 0 specifically).
- "H^i concentrated in [0, 2]" — AMPLITUDE (H^i = 0 for i > 2).

NEVER write "{0, 1, 2}" to mean "amplitude <= 2". Either the middle index is populated (occupation) or it is an amplitude bound (interval). Mixing collapses provable facts into apparent contradictions.

## E_n Chiral Hierarchy (CY dimension -> native E_n level)

Gerstenhaber bracket on HH*(C,C) has degree 1-d. This determines native E_n level:

| d | Native E_n | Bracket degree | Mechanism |
|---|-----------|---------------|-----------|
| 1 | E_infinity (commutative) | 0 | Abelian Lie conformal; symmetric factorization |
| 2 | E_2 (braided) | -1 (Lie = lambda-bracket) | S^2-framing of HH_*(C) gives E_2 directly |
| 3 | E_1 (ordered) | -2 (shifted Lie) | Holomorphic CS breaks E_2 to E_1; CoHA is associative |
| >=4 | E_1 stabilized | <=(-3) | pi_d(BU)=KU^{-d} obstruction (2-periodic, Z at even d) + pi_d(BSp) subset pi_d(BO)=KO^{-d} (8-periodic, Z/2 at d=5 mod 8); no native braiding. pi_d(BU) is 2-periodic NOT 8-periodic; 8-periodicity is real Bott (BO/BSp). AP-CY73. |

**E_2 at d=3 is DERIVED, not native**: the E_2 braiding on Rep categories of d=3 chiral algebras comes from the Drinfeld center Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^der_ch(A)), NOT from A itself. A is E_1; only its representation category acquires E_2 braiding via the center.

E_3 at d=3 is the DERIVED CENTER (higher Deligne): HH*(B_{E_3}(A), B_{E_3}(A)). Structure on observables of the field theory, not on the CY chiral algebra Phi(C).

Drinfeld center is categorified av: E_1-Cat -> E_2-Cat. Quantum groups, Yangians, braided tensor categories NATIVELY E_1. E_2 DERIVED.

## Three Hochschild Theories (NEVER CONFLATE)

| Name | Input | Output | Concentration |
|------|-------|--------|---------------|
| Topological HH | E_1-algebra | E_2 (Deligne) | Unbounded |
| **Chiral** ChirHoch | E_infinity-chiral | E_infinity (Thm H) | **{0, 1, 2}** |
| Categorical HH | dg category | E_2 with CY shifted Poisson | Dim-d shifted |

Geometry determines which: curve X -> chiral; R -> topological; CY category -> categorical. Bare "Hochschild" must carry qualifier. ChirHoch infinite at critical level k = -h^v only (Feigin-Frenkel). HH*(Weyl algebra) = 1-dim NOT infinite (AP-CY64). H*_Gel'fand-Fuchs unbounded (polynomial ring; not ChirHoch, not THH).

## Scope Boundaries (CY-A, CY-B, CY-C, CY-D)

**CY-A (Phi functor):**

- d=1: Phi outputs E_infinity (commutative). PROVED trivial.
- d=2: Phi outputs E_2 (braided). PROVED (CY-A_2). Phi_2(D^b(K3)) = H_Muk (Mukai Heisenberg, signature (4,20)).
- d=3: Phi outputs E_1 (ordered). PROVED inf-cat. Chain-level [m_3, B^{(2)}] != 0 is NOT an obstruction (HH^{-2}_{E_1} = 0). Chain-level explicit for non-formal algebras OPEN.
- d>=4: Phi outputs E_1 stabilized. CONSTRUCTION at d=4 (P^1-family), d=5 (Z/2-gerbe).

**CY-B (Koszul duality):**

- d=2: E_2-Koszul on A directly.
- d=3: E_1-Koszul on A via B_{E_3}(A), inducing E_2 on Drinfeld center Z(Rep^{E_1}(A)) via Verdier spectral functor. 131 tests. Chain-level conditional for non-formal.
- CY-B1 (conductor): PROVED all classes.
- CY-B2 (braided equiv on center): PROVED all classes.

**CY-C (Quantum group realization):**

- CONJECTURAL. NEVER `\begin{theorem}`.
- Abelian level: C(g,q) = D(Y^+(g_{K3})). Three routes (chiral/BFN/MO). Rep(C) = Rep^{E_2}(Y) via BZFN.
- Six independent routes to G(K3 x E): six DIFFERENT constructions (not six applications of Phi; AP-CY60). Convergence = CY-C.
- **Pentagon correction (AP-CY71)**: stratification {3, 12, 24} is GENERATOR RANK rho^{R_i}, NOT kappa_ch. Hodge supertrace invariant = 0 route-independent for K3 x E.

**CY-D (Modular characteristic, TRI-STRATUM theorem):**

| Stratum | d-parity | Class | kappa_ch |
|---------|----------|-------|----------|
| (I) | odd d | Serre | Xi = 0 |
| (II) | even d | strict-CY | nonzero (e.g., K3 stratum d=2: kappa_ch = 2 via Hodge supertrace, matching kappa_ch^{Heis} at d=2 with h^{1,0}=0; CY_4 sextic: Xi = 2) |
| (III) | even d | holomorphic-symplectic | Xi = n+1 (K3^[2]: Xi = 3) |

Hodge-supertrace kappa_ch = chi(O_X) PROVED unconditionally for compact CY_d via `thm:kappa-hodge-supertrace-identification`. For CY_2 with h^{1,0}=0 (K3) the Heisenberg-level reading coincides (`prop:cy-kappa-d2`). At odd d with h^{1,0}=0 the two readings diverge: chi(O_X) = 0 by Serre, while the Heisenberg-level reading picks up the BCOV quantum correction delta kappa_ch = chi_top/24. For K3xE (d=3, fiber h^{1,0}(E)=1): kappa_ch^{Heis} = 3 (additive) != 0 = chi(O_{K3xE}) (Kunneth-multiplicative). chi^CY is categorical, distinct from chi(O_X). At d=3: CY-D formula is the tri-stratum theorem, not chi(O_X).

## Pre-Edit Verification Protocol

Before editing any surface touching r-matrices, kappa formulas, bar/cobar/Koszul-dual/desuspension, d=3 theorem environments, shadow class, SC-formality, MF(W) CY dimension, cross-volume Part references, or hardcoded test oracles: write a `PRE-EDIT` fenced block in commentary. Fill it in; end with `verdict: ACCEPT` or `verdict: REJECT`.

### PE-1. r-matrix write (AP126, AP141)

```
## PRE-EDIT: r-matrix
family:                    [Heis / KM / Vir / W_N / lattice / Yangian / CY]
r(z) written:              [full formula with level prefix]
level parameter symbol:    [k / k+h^v / hbar / c / Psi]
convention:                [trace-form k*Omega/z / KZ Omega/((k+h^v)*z)]
AP126 check (trace-form):  r(z)|_{k=0} = [_]    expected: 0
match?                     [Y/N]
AP141 grep check:          bare \Omega/z instances in edit scope: [N]
source:                    [landscape_census.tex:LINE / compute/module.py]
verdict:                   [ACCEPT / REJECT]
```

### PE-2. kappa formula write (AP1, AP39)

```
## PRE-EDIT: kappa
family:                    [Heis / Vir / KM / W_N / bc / betagamma / other]
kappa formula written:     [_]
census citation:           landscape_census.tex:LINE
AP136 boundary (W_N):      formula uses [H_N / H_{N-1} / H_N - 1]
  substitute N=2:          [_]  expected c/2 (W_2 = Vir)
evaluation at k=0:         [_]  expected [dim(g)/2 for KM, 0 for Heis, c/2 for Vir]
wrong variants avoided:
  NOT kappa(W_N) = c*H_{N-1}   NOT kappa(Heis) = k/2
verdict:                   [ACCEPT / REJECT]
```

### PE-3. kappa-spectrum (AP113 + AP-CY55)

```
## PRE-EDIT: Vol III kappa subscript discipline
object:                    [CY manifold X]
invariant type:            [manifold (cat/fiber) / algebraization (ch/BKM)]
subscript written:         [_]
subscript in approved set? [Y/N]   # {ch, cat, BKM, fiber}
forbidden subscript used?  [Y/N]   # STOP if Y
AP-CY55 type-match:        algebraizations cannot vary kappa_{cat,fiber}? [Y/N]
grep AFTER write:          bare `\kappa[^_]` hits: [N]
verdict:                   [ACCEPT / REJECT]
```

### PE-4. bar complex formula (AP132, AP22)

```
## PRE-EDIT: bar complex
object written:            B(A) = [_]
T^c argument:              [s^{-1} \bar A / s^{-1} A / s \bar A / bare A]
AP132 augmentation:        \bar A = ker(epsilon) present?  [Y/N]   # must be Y
AP22 desuspension:         |s^{-1} v| = |v| [-1 / +1]              # must be -1
coproduct type:            [deconcatenation T^c / coshuffle Sym^c / coLie]
grading:                   cohomological |d|=+1?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

### PE-5. Vol III kappa write (AP113, zero tolerance)

```
## PRE-EDIT: Vol III kappa
subscript written:         [ch / cat / BKM / fiber / OTHER]
subscript present?         [Y/N]   # must be Y; bare kappa FORBIDDEN
subscript justification:   [chiral shadow / categorified / BKM / fiber correction]
census citation:           landscape_census_cy.tex:LINE
grep BEFORE write:         bare `\kappa[^_]` hits: [N]
grep AFTER write:          bare `\kappa[^_]` hits: [N]
delta = 0?                 [Y/N]   # must be Y
verdict:                   [ACCEPT / REJECT]
```

### PE-7. Label creation (AP124, AP125)

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma]
label written:             \label{prefix:name}
prefix match (AP125):      theorem->thm, prop->prop, conj->conj, def->def, rem->rem, lem->lem
match?                     [Y/N]   # must be Y
AP124 duplicate check (grep all three volumes):
  Vol I matches:           [N]
  Vol II matches:          [N]
  Vol III matches:         [N]
  delta = 1?               [Y/N]   # must be Y
if duplicate, rename with volume suffix and update all \ref
verdict:                   [ACCEPT / REJECT]
```

### PE-8. Cross-volume formula (AP5, AP3)

```
## PRE-EDIT: cross-volume formula
formula:                   [_]
Vol I grep:                [hits, canonical form]
Vol II grep:               [hits, canonical form]
Vol III grep:              [hits, canonical form]
consistent across volumes? [Y/N]
if inconsistent:
  canonical volume:        [Vol I / II / III]
  other volumes updated same session?  [Y/N]  # must be Y (AP5)
convention conversion?     [OPE(I) -> lambda(II) / motivic(III) / NA]
verdict:                   [ACCEPT / REJECT]
```

### PE-10. Scope quantifier (AP6, AP7, AP32, AP139)

```
## PRE-EDIT: scope quantifier
statement:                 [_]
genus:                     [g=0 / g=1 / g>=2 / all g / UNSPECIFIED -> REJECT]
degree:                    [n=_ / all n / UNSPECIFIED -> REJECT]
d (CY):                    [d=2 / d=3 / d>=4 / UNSPECIFIED -> REJECT]
AP32 weight tag:           [(UNIFORM-WEIGHT) / (ALL-WEIGHT + delta F_g^cross) / NA]
AP139 free-variable audit:
  variables on LHS:        {_}
  variables on RHS:        {_}
  LHS superset RHS?        [Y/N]
AP36 implies vs iff:       [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

### PE-11. Differential form type (AP117, AP130)

```
## PRE-EDIT: differential form
what:                      [connection 1-form / bar propagator / Arnold / KZ]
form written:              [_]
expected type:
  connection 1-form: r(z) dz  (NOT d log)
  KZ:                sum r_{ij} dz_{ij}
  Arnold form:       d log(z_i - z_j)  (bar coefficient, NOT connection)
  bar propagator:    d log E(z,w)  (weight 1 ALWAYS, AP27)
match?                     [Y/N]
space the form lives on:   [fiber Sigma_g / base M-bar_{g,n} / FM_n(X) / Ran(X)]
AP130 fiber-base:          object on fiber vs class on base correctly distinguished? [Y/N]
verdict:                   [ACCEPT / REJECT]
```

Refusal criteria: reject own edit if any `match?` = N, any blank source, any FORBIDDEN ticked, grep delta mismatch.

## Canonical Checks

Verify before trusting a sentence or test:

```text
kappa(H_k) = k
kappa(Vir_c) = c/2
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^N 1/j

r^KM(z) = k*Omega/z
r^Heis(z) = k/z
r^Vir(z) = (c/2)/z^3 + 2T/z

c_bc(lambda) = 1 - 3(2*lambda-1)^2
c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
c_bc + c_bg = 0

B(A) = T^c(s^{-1} A-bar),   A-bar = ker(epsilon)
|s^{-1}v| = |v| - 1
d_bar^2 = 0
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24
F_2 = 7*kappa/5760
eta(tau) = q^(1/24) * prod_{n>=1}(1-q^n)
Cauchy normalization = 1/(2*pi*i)

K_BP = 196
BP conductor polynomial identity: c(BP_k) + c(BP_{-k-6}) = 196  (polynomial in k)
W_N central-charge conductor:     K^c_N = 4N^3 - 2N - 2        (K_2=26, K_3=100, K_4=246, K_5=488)
W_N kappa-conductor:              K^kappa_N = K^c_N * (H_N - 1)
delta F_2(W_3) = (c + 204)/(16c)

genus-2 stable graph count:
  7 total connected stable strata at g=2, n=0
  6 edge-bearing Feynman types under at-least-one-edge convention

kappa_ch^{Heis}(K3 x E) = 3   # Heisenberg-level additive reading; cf. Hodge-supertrace kappa_ch(K3 x E) = 0 via thm:kappa-hodge-supertrace-identification
kappa_BKM(K3 x E) = 5
kappa_cat(K3 x E) = 0           # TOTAL SPACE, not fiber value 2
kappa_fiber(K3 x E) = 24        # Mukai lattice rank
local P^2 = class M, not class L

# Universal formulas
kappa_BKM = c_N(0)/2             # ONLY correct universal formula (Borcherds weight)
kappa_ch  = str_{F^0}(q^{L_0})   # Hodge-filtered supertrace
E_3 bar:  (1+t)^{3g} = 2^{3g}   for classes L, C
          6^g                    for class M (Kunneth, chain P(q)^{6g})

# Homotopy / topology (AP181-AP185, AP-CY73)
pi_3(BU) = 0                     # Bott: pi_odd(BU) = 0; confusion with pi_3(U) = Z
pi_4(BU) = Z                     # obstruction GROUP, not automatic E_2 structure
pi_d(BU) is 2-periodic           # complex Bott (NOT 8-periodic; that's pi_d(BO))
pi_d(BSp) ⊂ pi_d(BO) = KO^{-d}   # 8-periodic (real Bott)
kappa_ch = chi(S)/2              # for local surfaces Tot(K_S -> S) ONLY
McKay(C^3/Z_n) = n copies of oriented n-cycle, NOT K_{n,n}

# SC / operadic (AP165-AP172, AP176)
B(A) is E_1 coalgebra            # NOT SC-coalgebra; SC on derived center pair
SC^! = (Lie, Ass, shuffle)       # NOT self-dual; closed dim = (n-1)! vs 1
A^! is SC^!-algebra = (Lie,Ass)  # NOT SC-algebra
"arity" BANNED                   # AP176 CONSTITUTIONAL; use "degree" everywhere

# Gerstenhaber / Hochschild (AP-CY69, AP-CY78)
S^d-framing on HH_*(C)           # Connes B-operator, HOMOLOGY
Gerstenhaber bracket on HH^*     # COHOMOLOGY, degree 1-d
(2-d)-shifted Poisson on HH^*    # PTVV: n-shifted has bracket degree -n; for n=2-d gives d-2
```

## Forbidden Forms

Grep and fix immediately:

```text
Omega/z                               # bare level-stripped r-matrix (AP126)
(c/2)/z^4                             # Virasoro quartic r-matrix term (AP19)
c*H_{N-1}                             # wrong W_N harmonic-number form (AP136)
T^c(s^{-1} A)                         # bar complex forgot augmentation ideal (AP132)
|s^{-1}v| = |v|+1                     # desuspension wrong direction (AP22)
eta(tau) = prod(1-q^n)                # missing q^(1/24) (FM13)
K_BP = 2                              # wrong Bershadsky-Polyakov conductor (AP140)
kappa(K3 x E) = 5                     # unqualified Vol III kappa (AP113)
local P^2: class L                    # AP-CY12 misclassification
MF(W) is CY_{n-1}                     # wrong matrix-factorization dimension (AP-CY17)
Part~IV / Chapter~12 hardcoded refs   # stale architecture refs (AP-CY13)
"B(A) is SC coalgebra"                # FALSE: E_1 coalgebra (AP165)
(SC^{ch,top})^! ~ SC^{ch,top}         # FALSE: SC^!=(Lie,Ass,shuffle) (AP166)
"E_3-chiral"                          # FALSE: E_3-TOPOLOGICAL with conformal vector (AP168)
"arity" anywhere in manuscript        # BANNED (AP176 CONSTITUTIONAL)
pi_3(BU) = Z                          # WRONG: pi_3(BU) = 0 (B69, AP181)
pi_d(BU) 8-periodic                   # WRONG: 2-periodic; 8-periodic is BO (AP-CY73)
kappa_ch = h^{1,1}                    # WRONG when h^{0,2}!=0 (B70, AP182)
McKay(Z_3) = K_{3,3}                  # WRONG: 3 copies of oriented 3-cycle (B71, AP183)
"excision gives B(A) tensor B(A)"     # WRONG: B_L tensor_A B_R (one copy, over A) (B72, AP184)
"pi_4(BU)=Z provides E_2"             # WRONG: obstruction group, not guarantee (B73, AP185)
kappa_BKM = kappa_ch + chi(O_fiber)   # COINCIDENCE at N=1; FALSE N>=2 (AP-CY37)
"ChirHoch is finite while THH is infinite"  # WRONG: HH*(Weyl)=1-dim (AP-CY64)
"r = Omega_g" in R = 1 + hbar*r + ... # WRONG: r + r^{21} = Omega, not r = Omega (AP-CY74)
"Phi(D^b(K3)) = N=4 SCA"              # WRONG: Phi = H_Muk (AP-CY75)
"HH^1(Q_5) = k^{101} (Kodaira-Spencer)" # WRONG: KS in HH^2 under Kontsevich HKR (AP-CY76)
"Delta_5 in S_5(Sp_4(Z))"             # WRONG: lives on paramodular subgroup (AP-CY77)
"(2-d)-shifted bracket degree 1-d"    # WRONG: degree d-2 under PTVV (AP-CY78)
"principal W(sl_2) = Ising at c=1/2"  # WRONG: principal W(sl_2) = Virasoro, c=2 at kappa=1 (AP-CY79)
"Gepner ring = corners (0,0)+(d,d)"   # WRONG: anti-diagonal p+q=d (AP-CY80)
"stabilize by 2k squares = 2k steps"  # WRONG: k uv-pairs = k Knörrer steps (AP-CY81)
"Cl_4 ≅ M_2(C) Z/2-graded"            # WRONG: ungraded M_2(+)M_2; graded M_{2|2} (AP-CY82)
```

## Scope Boundaries: Vol III Invariant Lock

### E_1 / E_2 hierarchy

- E_1-chiral algebras: associative factorization on C x R; representation categories are monoidal.
- E_2-chiral algebras: braided factorization on C x C; representation categories are braided monoidal.
- E_2 is braided, NOT symmetric in general.
- E_1 -> E_2 via Dunn additivity is structural, not automatic at the level of every candidate.
- Drinfeld center is NOT the same as derived/chiral center without explicit hypotheses.

### Object discipline

Never conflate:

- `A` (algebra)
- `B(A)` (bar coalgebra)
- `A^i = H^*(B(A))` (dual coalgebra)
- `A^! = (A^i)^vee` (dual algebra)
- `Z^{der}_{ch}(A)` (derived/chiral center = bulk)
- `Z(Rep^{E_1}(A))` (Drinfeld center of monoidal category)

Definition-first discipline is non-negotiable for: G(X), any "quantum vertex chiral group", A_X or A_{K3 x E} at d=3, C(g,q), any center construction, any "bulk algebra" language, any claim that sells CoHA as if it were already the chiral object itself.

### Load-bearing d=3 boundaries

- CY-A is unconditional for d=2; PROVED inf-cat at d=3. Chain-level for non-formal: OPEN.
- Any d=3 theorem requiring chain-level S^3 framing, chart gluing, or unconstructed A_X is not ProvedHere without scope.
- CoHA is associative; may be evidence for E_1 sector; NOT identical to E_1-chiral algebra.
- Local P^2 is class M (full shadow tower), NOT class L (leading Lie-type approximation).
- MF(W) has CY dimension n-2 for W: A^n -> A^1 (NOT n-1).

## Cross-Volume Anti-Pattern Index

All of the following are in force here. Vol I and Vol II catalogues live in their respective `CLAUDE.md`s; Vol III AP-CY catalogue is enumerated below.

### Vol I (critical subset)

- AP1/AP9/AP39/AP48/AP136: kappa family-specific, never write from memory.
- AP5/AP12: grep ALL THREE volumes after every correction.
- AP19/AP21: Vir r-matrix = (c/2)/z^3 + 2T/z (NOT z^4, NOT z^2).
- AP22/AP132: bar = T^c(s^{-1} A-bar), A-bar = ker(epsilon).
- AP40: env matches tag; Vol III default `\begin{conjecture}`.
- AP113: bare kappa forbidden in Vol III.
- AP117/AP126/AP141: r-matrix level prefix mandatory.
- AP124/AP125: label prefix + cross-volume uniqueness.
- AP150: resolution propagation atomic across all three volumes.
- AP165/AP166/AP172: B(A) is E_1 coalgebra; SC not self-dual; A^! is SC^!-algebra.
- AP176: "arity" BANNED; use "degree" universally.
- AP177: S_2 = c/2 (not c/12); c/12 = S_2/3! divided-power coefficient.
- AP181-AP185: pi_3(BU)=0, kappa_ch=chi(S)/2 domain, McKay directed, excision vs coproduct, obstruction group vs enabler.

### Vol II (V2-AP subset)

- V2-AP26/V2-AP30: stale Part references.
- V2-AP29/V2-AP32: AI slop / artifact drift.
- V2-AP31: proof-after-conjecture.
- V2-AP34: OPE vs lambda-bracket convention.
- V2-AP35: connective drift.
- V2-AP36/V2-AP39: cross-volume context.

### Vol III (AP-CY1-67)

**Core (AP-CY1-8):**

- AP-CY1: CY dim d != complex dim n. Fuk(X) is CY_n, NOT CY_{2n}.
- AP-CY2: CY trace in HC^-_d(C), NOT HH_d -> k. Negative cyclic refinement essential for S^d-framing.
- AP-CY3: see HZ3-5. Plus: E_2 -> E_inf loses quantum group structure.
- AP-CY4: see HZ3-5.
- AP-CY5: Kazhdan-Lusztig requires root of unity. Generic q: Rep_q(g) semisimple.
- AP-CY6: see HZ3-1. Pre-April-2026 "A_X does NOT exist" SUPERSEDED by inf-cat proof.
- AP-CY7: see HZ3-4.
- AP-CY8: see HZ3-6.

**Empirical (AP-CY9-20):**

- AP-CY9: Jacobi form discriminant constraint. c(-1)=2 for phi_{0,1} in EZ convention.
- AP-CY10: see HZ3-8.
- AP-CY11: see HZ3-3. DEFAULT for CY-C-dependent: `\begin{conjecture}`.
- AP-CY12: see HZ3-9.
- AP-CY13: see HZ3-10. 7+ stale refs survived a single restructuring.
- AP-CY14: see HZ3-1. G(X) and C(g,q) remain unconstructed chain-level; must use `\begin{conjecture}`.
- AP-CY15: README scope inflation beyond .tex ground truth.
- AP-CY16: matrix size conflation (Sp_4 vs O(Lambda^{3,2})).
- AP-CY17: see HZ3-7.
- AP-CY18: Leech theta minimum norm^2 = 4. Never conflate j(tau) coefficients with V_Lambda character.
- AP-CY19: A-hat(x) = (x/2)/sinh(x/2). Convergence radius = 2*pi.
- AP-CY20: normal bundle vs spectral parameters. Intermediary mechanism (Omega-background) must be stated.

**Session 6d hCS (AP-CY21-26):**

- AP-CY21: E_3 bar cohomology: (1+t)^{3g} classes L,C; 6^g class M.
- AP-CY22: Miki is algebra-specific, NOT operadic.
- AP-CY23: E_1-chiral bialgebra (not E_infinity vertex bialgebra) is correct Hopf framework.
- AP-CY24: docstring ground-truth confabulation.
- AP-CY25: R = (id ⊗ S) ∘ Delta(1) is WRONG. Use half-braiding.
- AP-CY26: sigma_2 is EVEN under h_i -> -h_i. k^! = -k from Shapovalov, not sigma_2.

**180-agent swarm (AP-CY27-33):**

- AP-CY27: agent sandbox non-persistence. ALWAYS `ls` to verify after agent writes.
- AP-CY28: pole-unsafe test points. Use h=(37,41,-78) for safety.
- AP-CY29: wrong-repo file writes. Verify FULL PATH after agent writes.
- AP-CY30: factored != solved. YBE does NOT imply ZTE.
- AP-CY31: spectral z != worldsheet z.
- AP-CY32: reorganisation != bypass.
- AP-CY33: chain-level E_3 != rational E_3 (formality destroys it).

**53-agent K3 session (AP-CY34-40):**

- AP-CY34: RESOLVED via Costello operadic TCFT. Total {b, B^{(2)}} = 0; per-k FALSE.
- AP-CY34a/AP-CY44: kappa_ch != chi(O_X) at odd d. Tri-stratum at d=3.
- AP-CY35: superalgebra rank inflation. Y(gl(4|20)) CONJECTURAL.
- AP-CY36: RTT-OPE dictionary incompleteness.
- AP-CY37: kappa_BKM = kappa_ch + chi(O_fiber) is COINCIDENCE N=1; FALSE N>=2.
- AP-CY38: class M E_3 bar = 6^g (Kunneth), NOT infinite.
- AP-CY39: Incompatibility Theorem. mu_3 != 0 forces mu_2 = 0 on aug.
- AP-CY40: ProvedHere with no proof block. Grep for ProvedHere + \begin{proof}.

**290-agent session (AP-CY41-52):**

- AP-CY41: internal contradictions from partial updates. Grep all three volumes after status change.
- AP-CY42: phi_{0,1} normalization. c(-1)=1 vs c(-1)=2. Factor is kappa_ch(K3).
- AP-CY43: shadow-Feynman tautology at L>=4. Verify via independent computation.
- AP-CY44: see AP-CY34a.
- AP-CY45: N=2 root-of-unity gives TRIVIAL double braiding. Non-abelian needs N>=3.
- AP-CY46: no native CY_4 Yangian. pi_4(BU)=Z obstructs E_4. Use "p_1-twisted double current algebra".
- AP-CY47: structure function degree from Mukai rank, NOT Lie algebra dimension.
- AP-CY48: 3d->6d lift rate is only 24%. 6d NOT a dimensional upgrade of 3d.
- AP-CY49: agent tautological tests (10%). Every test needs 2+ independent sources.
- AP-CY50: duplicate agent launches. Check registry before relaunch.
- AP-CY51: rate-limited agents write engines+tests but not manuscript. Check disk first.
- AP-CY52: mega-file anti-pattern. Split files >3000 lines.

**User-identified conceptual (AP-CY53-61):**

- AP-CY53: pi_1(Conf_2) ordered vs unordered. Ordered = 0 for d>=3; unordered = Z/2.
- AP-CY54: "categorified averaging" wrong. Center is RIGHT ADJOINT to forgetful, not averaging.
- AP-CY55: see "kappa-Spectrum" section. kappa_cat and kappa_fiber are MANIFOLD invariants.
- AP-CY56: E_n level conflation. At d=3, A is E_1 NATIVE. E_2 lives on Z(Rep^{E_1}(A)).
- AP-CY57: narration instead of construction. R-matrix IS the universal half-braiding.
- AP-CY58: CY-B E_n scope uniformity. d=2 is E_2-Koszul; d=3 is E_1-Koszul inducing E_2 on center.
- AP-CY59: multiple algebraizations from single functor. Phi(D^b(K3)) = H_Muk; BKM/Conway are DIFFERENT constructions.
- AP-CY60: six routes != six applications of Phi.
- AP-CY61: see HZ3-12. First-principles investigation mandatory.

**Geometric vs Algebraic Model Conflations (AP-CY62-67, critical):**

- **AP-CY62**: geometric vs algebraic chiral Hochschild model. Two chain-level models: (a) geometric C^*_{ch,geom} (FM compactifications, log forms, 3-component differential), (b) algebraic C^*_{ch,alg} (End^ch_A, Gerstenhaber bracket differential). Quasi-isomorphic for logarithmic chiral algebras. At genus >= 1, geometric carries curve-dependent data algebraic lacks. **Counter**: specify "geometric (FM)" or "algebraic (bar/operadic)" when chain-level structure matters. Bare `C^*_ch(A,A)` forbidden in chain-level arguments. **Triggers**: "C^*_ch(A,A)" without model qualifier; "the derived center Z^der_ch" without model when E_n claimed; FM integration language mixed with formal-variable language.
- **AP-CY63**: BD chiral operad vs algebraic End^ch. BD uses D-module maps; algebraic End^ch uses formal Laurent series. Isomorphic after 4-step bridge (choose point, choose coordinate, trivialise D-module, identify spectral variables). **Counter**: never write "the chiral endomorphism operad" without specifying BD or algebraic. **Triggers**: "the chiral endomorphism operad on FM_k(C)"; mixing D-module with formal Laurent series.
- **AP-CY64**: three-way Hochschild confusion (ChirHoch / HH* / H*_GF). ChirHoch* concentrated in {0,1,2} (Thm H). HH*(Weyl) = 1-dim. H*_GF unbounded. "ChirHoch is finite while THH is infinite" is WRONG (HH*(Weyl) = 1-dim). Genuine "fails to concentrate" = H*_GF, not THH. At critical level k=-h^v only: ChirHoch* infinite (Feigin-Frenkel), HH* finite. **Triggers**: "ChirHoch is finite while THH is infinite"; "Theorem H has no classical analogue"; "concentration fails for topological Hochschild"; "Gel'fand-Fuchs agrees with ChirHoch".
- **AP-CY65**: spectral parameter provenance. z in R(z) has three-part origin: (a) algebraic (tau_z creating evaluation modules), (b) geometric (holomorphic translation on C), (c) representation-theoretic (z = u - v). "Topological Drinfeld centre has no spectral parameters" is FALSE: Yangian Y(g) has evaluation modules V_u. Correct: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. **Triggers**: "spectral parameters from the chiral structure"; "topological center has no spectral parameters"; "R(z) comes from the derived center"; "E_2 braiding carries spectral parameters".
- **AP-CY66**: BZFN ambient category is NOT tunable. BZFN uses SAME S on both sides. Two centres come from TWO DIFFERENT ALGEBRAS: chiral A (in IndCoh(Ran)) vs mode algebra A_mode (in Vect). **Counter**: never say "applying BZFN in two different ambient categories." Say: "two different algebras, each with its own BZFN equivalence." **Triggers**: "applying BZFN in two different ambient categories"; "the same algebra viewed in D-modules vs Vect"; "varying S in BZFN".
- **AP-CY67**: "spectral parameters from FM_k(C)" is narration, not construction. End^ch_A has formal algebraic variables; FM enters via comparison theorem. **Counter**: replace with "spectral parameters from End^ch_A, identified with relative position coordinates on the formal disk via the local-global comparison." **Triggers**: "spectral parameters from FM_k(C)"; "the chiral endomorphism operad on FM_k(C)".

**Higher-order ramification guards (AP-CY62-67):** WRONG REASONING: "Because ChirHoch is finite-dimensional, the Drinfeld center is finite" (Drinfeld center is a CATEGORY); "The spectral parameter distinguishes chiral from topological" (Yangian has spectral params despite being topological); "The curve geometry is what makes quantum groups possible" (partially right: curve creates tau_z, but once Yangian exists, spectral params persist regardless).

**Preface CG-rectify (AP-CY68-73, 2026-04-17 session):**

- **AP-CY68**: fiber-vs-total-space kappa_cat for K3-fibered CY_3. kappa_cat(X) = chi(O_X) is TOTAL-SPACE; for K3 x E it is 2*0 = 0 by Kunneth, NOT 2. Value 2 is chi(O_K3), FIBER invariant. Naive BKM decomposition kappa_BKM = kappa_ch + chi(O_fiber) = 3 + 2 = 5 at N=1 uses chi(O_fiber), NOT kappa_cat of total space. **Counter**: kappa-spectrum tables for K3 x E must show kappa_cat = 0 explicitly; fiber value for BKM decomposition labeled chi(O_fiber) or kappa_cat(fiber), never bare kappa_cat.
- **AP-CY69**: Hochschild homology vs cohomology for Connes vs Gerstenhaber. S^d-framing (Connes B-operator hierarchy, KV 2015) lives on HH_* (homology); Gerstenhaber bracket of degree 1-d lives on HH^*(C,C) (cohomology). **Counter**: always specify "Hochschild homology HH_* carries S^d-framing via Connes B; Hochschild cohomology HH^*(C,C) carries the Gerstenhaber bracket of degree 1-d."
- **AP-CY70**: internal-development metadata in reader-facing prose. Session timestamps, commit hashes, manuscript-version self-reference, internal AP-tag citations, healing-status commentary. Migrate to commit messages / notes/ changelog.
- **AP-CY71**: Hodge supertrace is kappa_cat, NOT kappa_ch. sum (-1)^q h^{0,q}(X) = chi(O_X) = kappa_cat (manifold invariant). For K3 x E: 1-1+1-1 = 0 = kappa_cat; kappa_ch(K3 x E) = 3 (additive under products). Ghost theorem: kappa_ch IS route-independent (correct), but via CATEGORICAL INVARIANCE of Phi_3(C), NOT via Hodge supertrace formula. The stratification theorem `thm:kappa-stratification-by-d` asserts kappa_ch = Hodge supertrace for d <= 5 but this fails at d=1 (E: 1 vs 0) and d=3 (K3 x E: 3 vs 0); scope audit pending. **Counter**: when asserting kappa_ch route-independence, cite categorical invariance of Phi_3(C), not the Hodge supertrace.
- **AP-CY72**: "S^d = (decomposition)" framing-decomposition shorthand vs manifold equality. "S^4 = S^2 x S^2" is literally wrong topology (H^2 differs) but used consistently for "E_4-framing splits per K3 factor via Kunneth." **Counter**: replace with explicit framing-decomposition ("the E_4-framing of Phi_4(C_{K3xK3}) splits as Kunneth product of two E_2-framings, one per K3 factor, compatible with KV S^2-action").
- **AP-CY73**: pi_d(BU) 8-periodicity vs 2-periodicity. pi_d(BU) = KU^{-d} is 2-PERIODIC (complex Bott): Z at even d, 0 at odd d. 8-periodicity belongs to pi_d(BO) = KO^{-d} (real Bott) or to an Sp-refined tower. **Counter**: either (a) pi_d(BO) + 8-periodicity, or (b) pi_d(BU) + 2-periodicity + explicit Sp-refinement invocation at d ≡ 5.

**CG-rectify campaign batch (AP-CY74-78, 2026-04-17):**

- **AP-CY74**: Drinfeld-Jimbo classical r-matrix equated with Casimir Omega. Wrong: "r = Omega_g". Ghost theorem: r DOES satisfy r + r^{21} = Omega (Drinfeld 1986). Precise error: the symmetry CONSTRAINT mistaken for the object; quasi-triangular element cannot be symmetric. Correct: r = Omega/2 + r_{sk} with skew Drinfeld-Sklyanin part. **Counter**: write r + r^{21} = Omega explicitly and decompose.
- **AP-CY75**: Phi(D^b(K3)) conflated with N=4 SCA. Both have kappa_ch = 2, but DIFFERENT algebras. N=4 SCA (c=6) is K3 sigma-model chiral algebra; Phi(D^b(Coh(K3))) = H_Muk (rank-24 free-boson VOA, signature (4,20)) per CY-A_2. N=4 SCA is NOT in image of Phi. **Counter**: name the specific algebra and its construction; never "the K3 chiral algebra" without qualifier.
- **AP-CY76**: quintic Hochschild grading and Kodaira-Spencer slot. Under Kontsevich HKR convention HH^p = ⊕_{q+r=p} H^q(∧^r T_X), KS (q,r)=(1,1) lives in HH^2 NOT HH^1. Correct quintic: HH^0=k, HH^1=0, HH^2=k^{101} (KS), HH^3=k^4 (Yukawa), HH^4=k^{101}, HH^6=k. **Counter**: declare HKR grading convention at first use; Vol III default p=q+r.
- **AP-CY77**: Borcherds cusp form Delta_N on full Sp_4(Z) vs paramodular subgroup. Writing "Delta_5 in S_5(Sp_4(Z))" WRONG: no weight-5 cusp form exists on full Sp_4(Z). Delta_5 lives on paramodular subgroup Gamma_para ⊂ Sp_4(Q) via accidental iso O^+(2,3) ≃ PGSp_4. **Counter**: always specify paramodular subgroup when writing BKM/Borcherds weight below 10 on Sp_4(Q).
- **AP-CY78**: (2-d)-shifted Poisson bracket degree. Under PTVV: n-shifted has bracket of cohomological degree -n. For n = 2-d, bracket has degree d-2 (NOT 1-d). Verification: d=1 gives -1 (Gerstenhaber); d=2 gives 0 (ordinary Poisson); d=3 gives +1 (BV). **Counter**: state PTVV convention; compute bracket degree as d-2.

**CG-rectify matrix_factorizations batch (AP-CY79-82):**

- **AP-CY79**: Virasoro-at-c=2 vs Ising-at-c=1/2 for principal W(sl_2). Principal W(sl_2) = Virasoro; for kappa_ch = mu(A_1) = 1, AP1 forces c = 2. Ising VOA at c=1/2 is SEPARATE. No factor-of-4 matching. **Counter**: principal W(sl_2) is Virasoro; level fixed by kappa match; Ising not in image.
- **AP-CY80**: Gepner (c,c)-ring Hodge indices — anti-diagonal p+q=d, NOT corners. For quintic: h^{3,0} + h^{2,1} + h^{1,2} + h^{0,3} = 1+101+101+1 = 204. **Counter**: state p+q=d explicitly and verify indices.
- **AP-CY81**: Knörrer stabilization — 2k squares reorganize into k uv-pairs. Iterated Knörrer MF(W + Sum u_i v_i) ≃ MF(W) uses uv-form, so stabilizing by 2k-variable quadratic form is k Knörrer steps, NOT 2k.
- **AP-CY82**: Cl_n Morita triviality requires Z/2-graded Morita + complex Bott 2-periodicity. Ungraded Cl_4(C) ≅ M_2(C) ⊕ M_2(C); graded Cl^C_4 ≅ M_{2|2}(C). **Counter**: specify Z/2-graded Morita explicitly; invoke complex Bott 2-periodicity (not real 8-periodicity, AP-CY73).

**Anti-pattern placement rule (2026-04-17).** All AP-CY entries live in `CLAUDE.md` and `notes/first_principles_cache_comprehensive.md`. AP entries DO NOT go into manuscript LaTeX files (`chapters/`, `appendices/`, `standalone/`). The historical `notes/anti_pattern_catalogue.tex.archive` is frozen and not appended to. New findings: one-line in CLAUDE.md + full ghost-theorem analysis in the cache markdown.

### Cross-programme (AP150-AP157 + FM24)

- AP150: agent confabulation of non-existent composite arrows. Verify EACH ARROW independently.
- AP151: hbar convention clash. grep all existing definitions before introducing new hbar.
- AP152: "ordered" ambiguity (labeled vs time-ordered). Specify.
- AP153: E_3 scope inflation. E_3 requires E_infinity input, not E_1.
- AP154: two E_3 structures (algebraic Deligne vs topological configuration-space). Specify.
- AP155: overclaiming novelty for known invariants from new framework. Check literature first.
- AP156: Weierstrass P_1 convention ambiguity (theta_1'/theta_1 vs zeta_tau).
- AP157: degeneration-type dependence. Name LCS/conifold/orbifold/MUM/tropical.
- FM24: B-cycle sign error from i^2. Verify |q| < 1 and Im(tau) > 0 after B-cycle integrals.

### Opus/GPT-5.4-specific mitigations

- AP-CY24: docstring ground-truth confabulation. Verify EVERY docstring value.
- AP150: composite arrow confabulation. Verify each arrow.
- Sign errors in bar differentials arity-3+. Pin sign conventions with explicit tests.
- AP-CY25: R = (id ⊗ S) ∘ Delta(1) WRONG. Use half-braiding.
- AP-CY26: sigma_2 EVEN under h_i -> -h_i. k^! = -k from Shapovalov.
- Drinfeld center and derived/chiral center are distinct without explicit hypotheses.

### Failure modes from 2026-04-14 CG rectification

- **FM42**: bulk substring replacement corruption. Never bulk-replace short substrings in common words. After any bulk replace, grep `ldegree|ndegree|rdegree|pdegree|tdegree`. Compound-word checklist: {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity}.
- **FM43**: E_n output scope of Phi. d<=2: E_2; d>=3: E_1. Always scope `(n=2 for d<=2; n=1 for d>=3)`.
- **FM44**: agent rate limiting. >10 concurrent agents -> mass rate limiting (27/31 failed). Batches of 3.
- **FM45**: agent skill fidelity gap. Subagents get ~200-word brief, not full 15K-word `/chriss-ginzburg-rectify` skill. For full-quality rectification, invoke skill directly.
- **FM46**: stale line counts. Update after content campaigns.

### Top-3 first-principles cache entries (highest recurrence)

| Wrong claim | Ghost theorem | Correct relationship | Type |
|-------------|---------------|---------------------|------|
| "Drinfeld center = categorified averaging" | av and Z factor: E_1 ->^Z E_2 ->^{Sym} E_inf | Center CONSTRUCTS braiding (step 1). Averaging DESTROYS it (step 2). | construction/narration |
| "CoHA = bar complex" | SV theorem: CoHA ≅ Y^+ | CoHA is ALGEBRA; bar is COALGEBRA. Character M(q) coincidence reflects SV iso. | algebra/coalgebra |
| "{b_k, B^{(2)}} = 0 individually" | TOTAL {b, B^{(2)}} = 0 true | Per-k FALSE. Cross-arity cancellation via Stasheff. Operadic d^2 = 0. | part/whole |

Full cache (45 entries, ghost theorems, cross-programme ~264 entries / 30 confusion types): `notes/first_principles_cache_comprehensive.md`.

## Vol II Cross-Awareness

Vol III results informing Vol II:

- **E_1-chiral bialgebra** (~400 lines) is the correct Hopf home. E_infinity vertex bialgebra destroys Hopf.
- **SC^{ch,top}** lives on derived center pair (C^•_{ch}(A,A), A), NOT on B(A). B(A) is E_1 coassociative coalgebra.
- **Topologization**: SC^{ch,top} -> E_3-TOPOLOGICAL via Sugawara at non-critical level k != -h^v (cohomological proof). Chain-level for class M may fail.
- **Three Hochschild theories** (chiral/topological/categorical) never conflated.
- **Universal Trace Identity** (Wave-14 reconstitution) bridges Vol I K(A) complementarity and Vol III kappa_BKM via Phi on logarithmic-finite-type class.

Vol II cross-volume AP catalogue: `~/chiral-bar-cobar-vol2/CLAUDE.md` (V2-AP1-V2-AP39).

## Vol I Cross-Awareness

Vol III results informing/correcting Vol I:

- **BP conductor polynomial identity** c(BP_k) + c(BP_{-k-6}) = 196 replaces meaningless kappa(BP_{-3}) = 49/3. Vol I healing target: `bp_self_duality.tex`.
- **K_BP = 196** (NOT 2). Global Koszul conductor; ghost-number/grading shifts are LOCAL (AP140).
- **W_N central-charge conductor K^c_N = 4N^3 - 2N - 2** (K_2=26, K_3=100, K_4=246, K_5=488). DISTINCT from kappa-conductor K^kappa_N = K^c_N * (H_N - 1).
- **delta F_2(W_3) = (c + 204)/(16c)**, three independent paths. ProvedHere.
- **Six-routes K3 x E CY-C pentagon** stratification is generator rank rho^{R_i}, NOT kappa_ch.
- **Super-Yangian complementarity** kappa + kappa' = max(m, n) for Y(sl(m|n)) (NOT 0).
- **kappa_BKM = c_N(0)/2** universal (Borcherds weight) — Vol I cross-volume bridge for complementarity studies.

Vol I cross-volume AP catalogue: `~/chiral-bar-cobar/CLAUDE.md` (AP1-AP235).

## Design Axioms for Codex/GPT-5.4

1. **Exact scope before reasoning.** Name file, theorem label, definition, convention, family, status boundary BEFORE solving.
2. **Verification before verbosity.** Short instruction + falsifiable check > long exhortation.
3. **Reasoning effort is a last-mile knob.** Before escalating effort, tighten task definition, output contract, verification loop.
4. **Durable rules, triggered playbooks, mechanical hooks.** Always-on here; deep workflows in skills; deterministic enforcement in hooks or grep-based checks.
5. **Local truth surfaces over inherited summaries.** Live `.tex`, compute, tests, logs, diffs OUTRANK memory, prior chats, metadata prose.
6. **Self-contained state beats hidden context.** Externalize plan, assumptions, blockers, verification in a durable note.
7. **Smaller true claims beat larger false ones.** Objective is surviving hostile rereading, not impressive prose.
8. **Add instructions only when they change behavior.** Remove decorative meta-rules, duplicated guidance, vague slogans.

### GPT-5.4 Prompt Architecture

When composing task prompts for Codex agents or sub-agents, use XML-tagged blocks:

- `<task>`: concrete job + repository context
- `<structured_output_contract>`: exact shape, ordering, brevity requirements
- `<default_follow_through_policy>`: act without asking routine questions; stop only when missing detail changes correctness/safety
- `<verification_loop>`: verify result against task requirements before finalizing
- `<grounding_rules>`: ground every claim in evidence; label hypotheses
- `<missing_context_gating>`: do not guess; retrieve with tools or state unknowns
- `<completeness_contract>`: resolve fully; check for follow-on fixes and edge cases
- `<dig_deeper_nudge>`: after first finding, check for second-order failures, empty-state, stale state
- `<action_safety>`: keep changes scoped; avoid unrelated refactors; call out risky actions
- `<tool_persistence_rules>`: keep using tools until evidence suffices

**Anti-patterns**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs; unsupported certainty without grounding.

## Codex-Native Operating Stance

- Default deliverable: a verified change or a precisely named blocker, NOT an outline.
- Default reasoning: `medium`. Escalate to `high`/`xhigh` only for load-bearing proof surgery, chapter-scale architecture, or stalled frontier synthesis AFTER the workflow itself has been sharpened.
- No plan theater. If a plan exists, it cashes out into edits, checks, or a blocker.
- Tool persistence. First plausible answer is not enough; stop only when the relevant falsifier passes or the blocker is real.
- Dependency-first execution. Read before editing; verify prerequisites before downstream claims.
- Parallel evidence gathering. Batch independent greps, file reads, log checks, targeted tests whenever not tightly coupled.
- Skill-first specialization. If a task matches a repo skill, use the skill instead of reconstructing.
- `AGENTS.md`, `CLAUDE.md`, READMEs, and prior agent prose are operational guides, NOT mathematical evidence.

## Claude-Codex Parity Rule

No durable Claude-side workflow is allowed to remain Claude-only. Any always-on skill, hook, loop, or metacognitive control that changes behavior must have a Codex-native home:

- `AGENTS.md` for always-on rules;
- `.agents/skills/` for triggered workflows;
- `.codex/hooks/` for mechanical routing and guardrails.

If `CLAUDE.md` grows a durable behavior and Codex lacks an analogue, either (1) add the Codex analogue in the same session, or (2) explicitly mark the parity gap as unresolved debt.

### Claude -> Codex parity map

| Claude Skill | Codex Skill | Trigger |
|-------------|-------------|---------|
| `/build` | `vol3-build-surface` | build, test, compile, verify |
| `/audit [target]` | `vol3-beilinson-loop` | audit, falsify, red-team, pressure-test |
| `/rectify [file]` | `vol3-beilinson-loop` | rectify, fortify, tighten, repair |
| `/chriss-ginzburg-rectify [file]` | `vol3-chriss-ginzburg-rectification` | chapter-scale structural rewrite, CG convergence |
| `/verify [claim]` | `vol3-pre-edit-verification` + `vol3-claim-verification` | verify formula, invariant, computational claim |
| `/propagate [pattern]` | `vol3-cross-volume-propagation` | AP5 sweep, cross-volume formula/status fix |
| `/compute-engine [name]` | `vol3-compute-engine` | new engine with multi-path tests |
| `/rectify-all` | `vol3-swarm-orchestration` | full-volume parallel rectification (user-authorized) |
| `/beilinson-swarm` | `vol3-swarm-orchestration` | parallel chapter rectification (user-authorized) |
| `/research-swarm [topic]` | `vol3-swarm-orchestration` | frontier synthesis, research architecture |

**Both `/rectify` and `/chriss-ginzburg-rectify` available in BOTH Claude and Codex.** Use `vol3-beilinson-loop` for targeted chapter/proof repair; `vol3-chriss-ginzburg-rectification` for chapter-scale structural rewriting with convergent loop.

Codex-specific: swarm-style decomposition permitted only when the user explicitly authorizes sub-agents; absent that, use the same workflow locally without spawning agents.

## Session Entry Protocol

For any nontrivial task:

1. **Lock the exact target.** File(s), labels, formulas, conventions, task type (audit / rectification / verification / compute / frontier).
2. **Read the live target before editing.** Never patch by pattern alone.
3. **Inspect the dirty surface.** Current diff in touched repo; cross-volume diffs when relevant.
4. **Lock the conventions.** Grading, shifts, OPE vs lambda-bracket, E_1 vs E_2, CY dim vs manifold dim, kappa subscripts.
5. **Name the claim state.** proved / proved elsewhere / conditional / conjectural / heuristic / open.
6. **Name the narrowest falsifier.** Targeted `pytest`, grep, local computation, proof trace, `make fast`.
7. **Only then edit.**

Vol III-specific session entry:

1. Read `~/chiral-bar-cobar/CLAUDE.md` first (canonical cross-volume).
2. Then this file (kappa-spectrum, AP-CY1-82).
3. Check AP113: bare kappa -> subscripted `kappa_{ch,BKM,cat,fiber}`.
4. Check AP114: do not cite theorems from 4 stub chapters.
5. CY-A: d=2 PROVED, d=3 PROVED (inf-cat). Chain-level [m_3, B^{(2)}] != 0 is NOT an obstruction.
6. CY-C is CONJECTURE. NEVER `\begin{theorem}` for CY-C. Abelian level: C(g,q) = D(Y^+(g_{K3})).
7. E_1-chiral bialgebra: correct Hopf home. E_infinity vertex bialgebra loses R-matrix.
8. E_3 bar: 2^{3g} for L,C. 6^g for M (PROVED, Kunneth closed form).
9. Kummer route Steps 1-4 PROVED; Step 5 conjectural.
10. kappa_BKM = c_N(0)/2 universal (NOT kappa_ch + chi(O_fiber)).
11. B(U^ch(L)) = CE_*(L) PROVED.
12. Super-Yangian Y(gl(4|20)) K3 case CONJECTURAL. General-rank Y(sl(m|n)) PROVED at small rank with complementarity max(m,n).
13. Class M Borel summable (Gevrey-1), NOT convergent.
14. ZTE correction T COMPUTED (exact rational, 35 tests).
15. Mock modular K3 THEOREM at d=2 (4-step proof).
16. CY-D: kappa_ch != chi(O_X) at odd d. Tri-stratum theorem.
17. Incompatibility: mu_3 != 0 implies mu_2 = 0 on aug (chain level, all non-formal).
18. Mathieu moonshine: frame shape = twined bar Euler for all 25 M_24 classes.
19. Root-of-unity N=2: 324 modules; abelian S-matrix degenerate.
20. E_8 x E_8 structure function: degree-(24,24), c = 24.
21. BKM Serre P_2(D)=0 CONJECTURAL (AP40-corrected 2026-04-17). Leading P_1(D) = -2D PROVED.
22. BP conductor polynomial identity c(BP_k) + c(BP_{-k-6}) = 196.
23. W_N central-charge conductor K^c_N = 4N^3 - 2N - 2 (K_2=26, K_3=100, K_4=246, K_5=488).
24. W_N kappa-conductor K^kappa_N = K^c_N * (H_N - 1); DISTINCT invariant.
25. delta F_2(W_3) = (c + 204)/(16c) ProvedHere.

## The Resonance Loop

For nontrivial tasks, run until `CONVERGED` or `BLOCKED`.

0. **Scope Lock.** Surface, dependent labels/formulas/conventions, task type.
1. **Invariant Lock.** Grading, shifts, bar/cobar/Koszul-dual identity, open/closed color, OPE vs lambda-brackets, genus/degree/filtration/family scope, Vol I/II/III conventions.
2. **Read the Surface.** Live target before editing. Never pattern-patch.
3. **RED Pass.** Attack logic/mathematics: hidden hypotheses, circularity, sign/degree errors, formula drift, overclaimed biconditionals, false identifications, proofs silently assuming conclusion.
4. **BLUE Pass.** Attack consistency: theorem/proof/status mismatch, label drift, stale Part refs, duplicated formulations, compute/manuscript disagreement, README overclaim, cross-volume inconsistencies.
5. **GREEN Pass.** Attack structural gaps: missing definitions, objects used before axiomatization, missing lemmas, dangling references, places where true statement is weaker than advertised.
6. **Patch in Dependency Order.** Fix `CRITICAL` + `SERIOUS` first, then `MODERATE`. For each fix: re-read local context, recompute/re-derive independently, make smallest truthful edit, search for downstream advertisements.
7. **Propagate.** Grep Vol III / Vol II / Vol I. Verify sameness of object/convention before editing a verbal match. Update genuine duplicates same session or leave explicit pending note.
8. **Verify.** Targeted `pytest` / grep / proof trace / log inspection / `make fast` for load-bearing rewrites.
9. **Re-Audit.** Hostilely reread own rewrite. Try to break it.
10. **Convergence.** `CONVERGED`: no known actionable `MODERATE+` finding; narrowest verification passes. `BLOCKED`: exact blocker named precisely.

## Convergent Writing Loop

For introductions, prefaces, chapter openings, architectural rewrites:

1. Write a first truthful draft.
2. Reimagine structure under hostile and compression-minded rereading.
3. Rewrite from scratch rather than line-polishing a bad skeleton.
4. Run a Beilinson audit on the rewritten surface.
5. Repeat until no actionable `MODERATE+` finding remains.

Minimum standard:

- preface/introduction scale: 3+ iterations.
- chapter openings and major transitions: 2+ iterations.

Structural moves worth preferring when they fit: deficiency opening; unique-survivor framing; instant computation; forced transition; decomposition table; true dichotomy; sentence-as-theorem compression.

## Operating Modes

### Mode 1 — Default Research Mode

Ordinary manuscript/notation/compute/proof maintenance. Loop: identify target, read local source, inspect nearby diff/dependencies, make smallest defensible correction, run narrowest falsifier, propagate shared formula/status, stop when coherent.

### Mode 2 — Deep Beilinson Audit

Trigger: audit / review / red-team / challenge / falsify / pressure-test. Audit live surface (`main.tex`, current `\input` graph, dirty diff, logs, compute/tests). RED / BLUE / GREEN passes mandatory. Findings are mathematical bugs, not editorial trivia.

### Mode 3 — Beilinson Rectification Loop

Trigger: fix / rectify / converge / tighten / repair. Identify claims + dependencies; classify by severity; fix CRITICAL + SERIOUS first; rerun narrowest falsifier; re-audit; repeat until `MODERATE+` zero.

### Mode 4 — Multi-Path Claim Verification

Trigger: "is this formula correct?" Minimum: 3 genuinely independent paths for load-bearing numerical/computational claims; 2 for test oracles when 3 impractical. Allowed path families: direct computation; equivalent formula; limiting/degenerate case; symmetry/duality; cross-family; literature with convention check; degree/weight/sign/units; numerical evaluation; operadic/factorization consistency; descent to classical/PVA/shadow.

Mandatory Vol III overlays:

- AP-CY1: CY dim != real dim.
- AP-CY2: CY trace in HC^-_d, not HH_d.
- AP-CY5: quantum-group claims specify q regime.
- AP-CY6/11/14: CY-A_3 inf-cat PROVED; CY-C conditionality propagates.
- AP-CY7: CoHA is not automatically E_1-chiral.
- AP-CY8: denominator identity not automatically bar Euler product.
- AP-CY12: shadow class from full tower.
- AP49: cross-volume convention conversion.

### Mode 5 — Cross-Volume Propagation Sweep

Trigger: change formula / theorem status / definition / notation / convention / summary / claim touching kappa, Theta, bar/cobar, CoHA, E_1/E_2, Borcherds products, quantum groups, centers, shadow towers.

Protocol: grep Vol III, grep Vol II, grep Vol I, verify sameness before editing, update genuine duplicates or explicitly mark pending. Never paste formulas between volumes without convention conversion.

### Mode 6 — Compute Rectification Mode

Trigger: `.py` engine / test oracle / table value / hardcoded coefficient / numerical claim edit.

Rules:

- Every hardcoded value records source and normalization.
- Engine and test must NOT derive from same mental model.
- Prefer exact arithmetic when claim is exact.
- When formula changes, audit neighboring comments/docstrings/tests for stale reasoning.
- If a compute result matters for the prose, it matters enough for an independent executable check.
- Build artifacts are never evidence.

Prevents AP10, AP38, AP80, AP122, AP123, AP128, AP140, and "engine + test agree on same wrong number" failures.

### Mode 7 — Frontier Research Mode

Trigger: new theorems / definitions / constructions / CY3 frontier architecture.

1. Define the object before naming the programme around it.
2. Test toy models before general prose.
3. Search for counterexamples early.
4. Separate construction, evidence, conditional, conjecture, heuristic, slogan explicitly.
5. Never upgrade frontier claim to theorem status in the same pass that first drafts its proof.
6. Default new Vol III formal frontier statements to `\begin{conjecture}`.

Prevents AP36, AP40, AP42, AP43, AP-CY6, AP-CY11, AP-CY14.

## Claim-State Governance

Every serious statement belongs to exactly one of:

- `\ClaimStatusProvedHere`
- `\ClaimStatusProvedElsewhere`
- `\ClaimStatusConditional`
- `\ClaimStatusConjectured`
- `\ClaimStatusHeuristic`
- `\ClaimStatusOpen`

Rules:

- Status is part of the mathematics, not decoration.
- theorem/proposition/lemma/corollary environments are for proof-bearing or genuinely cited results only.
- Conjectural/heuristic material does not belong in theorem-like environments.
- If proof chain passes through an unconstructed d=3 chain-level object, result is at least `Conditional`, often `Conjectured`.
- If proof proves less than the sentence claims, weaken the sentence.
- Do not strengthen both statement and status in the same unchecked pass.
- When status changes, update environment, label prefix, surrounding prose, downstream advertisements, compute/docs surface.

## Current Empirical Risk Map (2026-04-17)

### Last-100-commit archaeology

- **Vol I** dominated by rectification, build-noise cleanup, formula/convention repair, compute/test synchronization. Repeated AP126/AP141, AP124/AP125, AP136, AP137, AP140, AP29, AP128. SC^{ch,top} critical correction (AP165) and AP166-AP175 represent major structural fix wave.
- **Vol II** dominated by rectification, convention repair, cross-volume propagation, AP40 env/status drift, AP44 divided-power drift, AP32 uniform-weight, V2-AP26/V2-AP30 stale Part refs, V2-AP31 proof-after-conjecture, V2-AP32/V2-AP35 artifact/connective drift, S_2=c/12 divided-power confusion (AP177/FM30).
- **Vol III** dominated by build noise, compute/test frontier corrections, AP113 kappa-subscript repair, AP-CY6/AP-CY11/AP-CY14 conditionality failures, AP-CY12 shadow-depth misclassification, AP-CY13 stale Part refs, AP-CY17/AP-CY18/AP-CY19 geometric/computational drift, README/doc scope inflation, pi_3(BU)/kappa_ch=h^{1,1}/McKay corrections (AP181-AP183), AP-CY62-82 model/convention corrections, Wave-14 Platonic synthesis.

### Current dirty hotspots (Vol III)

- `kappa_ch` vs `kappa_BKM` for K3 x E.
- Level prefix in CY r-matrices.
- local P^2 from class L to class M.
- pi_3(BU) = 0 in `chapters/theory/fukaya_categories.tex` (AP181).
- kappa_ch = chi(S)/2 domain (local surfaces only, not conifold) (AP182).
- McKay quiver of C^3/Z_3 in `chapters/examples/toric_cy3_coha.tex` (AP183).
- Synchronized updates across `chapters/theory/introduction.tex`, `chapters/connections/cy_holographic_datum_master.tex`, `chapters/examples/toroidal_elliptic.tex`, `compute/lib/modular_cy_characteristic.py`, `compute/lib/swiss_cheese_cy3_e1.py`, tests.
- CY-D tri-stratum theorem inscription and propagation.
- Wave-14 Universal Trace Identity bridging-diagram closures.

Treat all as live audit surfaces, not settled facts.

## Context and Memory Hygiene

For substantial tasks:

- Keep a short explicit plan or self-contained audit note.
- After each major phase, restate target, current status, open risks, next falsification step.
- Anchor conclusions to exact file paths, theorem labels, test names.
- Prefer durable notes under `compute/audit/` or `notes/audit_*.md` for major audits.
- Write notes so a newcomer with only the current working tree can continue without hidden chat context.
- Do not let summaries harden into truth without rereading source.

## Beilinson Gate — Post-Edit Mental Hook

After editing any `.tex` or `.py` file, explicitly check:

- did the edit change truth conditions or only presentation;
- is the claim status still honest;
- does surrounding environment match status macro;
- did a definition become load-bearing, and if so, is it present;
- did a shared formula require propagation;
- did a cross-volume convention bridge require conversion;
- does compute layer still support the formula;
- hidden CY3 existence assumptions;
- proof silently assuming conclusion;
- dirty-diff hotspot required fresh reread rather than local patch.

For `.tex` re-check at minimum: AP40 env/status mismatch; AP113 unqualified kappa; AP165 B(A) not attributed SC; AP166 SC not claimed self-dual; AP176 no "arity"; AP181 pi_3(BU) = 0; AP182 kappa_ch = chi(S)/2 domain; AP-CY6/11/14 d=3 existence and conditionality; AP-CY12 shadow depth from incomplete evidence; AP-CY13 stale Part refs; AP-CY15 README/summary overclaim; AP-CY62-82 geometric/algebraic model conflations; AP-CY68-73 preface-level recurrences; AP-CY70 no metadata in reader-facing prose; V2-AP26/V2-AP35 stale structural refs.

For `.py` re-check: hardcoded expected values vs independent verification; source and normalization conventions in literals and docstrings; exact arithmetic vs floating approximation where exactness claimed; engine/test independence; AP113 subscripted invariants; AP140 family-specific conductors; adjacent tests/comments/README stale descriptions; independent-verification decorator present for `\ClaimStatusProvedHere` claims.

## Convergence Gate — Stop-Time Mental Hook

For audit/rectification sessions, do not stop until you can honestly say one of:

- `CONVERGED`: modified surface is coherent and verified.
- `BLOCKED`: exact blocker named.

Do not end with a vague half-fix.

## Pre-Commit Gate

Before any commit:

1. Run narrowest build/test verification matching the change.
2. Inspect diff for build artifacts, logs, PDFs, accidental noise.
3. Grep touched surfaces for highest-risk anti-patterns matching the change.
4. **Run manuscript hygiene grep** (zero hits in typeset prose):
   ```bash
   grep -rn 'AP-CY\|AP1[0-9]\{2\}\|2026-\|commit [a-f0-9]\{7\}\|inscription\|campaign\|healed\|first edition\|earlier phrasing\|superseded across\|adversarial audit\|the agent found\|RECTIFICATION-FLAG' \
     chapters/ standalone/ main.tex preface 2>/dev/null | grep -v ':[0-9]*:\s*%'
   ```
5. If `RECTIFICATION-FLAG` entered the diff, resolve or record a precise tracked follow-up.
6. Ensure no AI attribution in commit message or metadata.
7. Ensure all commits remain authored by Raeez Lorgat only.

## Verification Commands

Narrowest relevant slice first.

Vol III build:

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast
```

Independent verification (HZ3-11):

```bash
make verify-independence          # summary
make verify-independence-verbose  # per-claim coverage
```

Cross-volume propagation:

```bash
cd ~/chiral-bar-cobar && make fast
cd ~/chiral-bar-cobar-vol2 && make
```

Compute: targeted `pytest` first; broader suite only if local slice passes and scope warrants.

## Repo-Local Skills and Hooks

Codex-native skills under `.agents/skills/`, hook configuration under `.codex/`.

Use:

- `vol3-beilinson-loop`: hostile audit + rectification.
- `vol3-chriss-ginzburg-rectification`: chapter-scale structural fortification.
- `vol3-claim-verification`: formula/theorem/comparison checks.
- `vol3-cross-volume-propagation`: AP5/AP49-style sweeps.
- `vol3-build-surface`: build/test/log triage.
- `vol3-frontier-research`: new theorem architecture, conjectural synthesis.
- `vol3-compute-engine`: executable witnesses, engine scaffolding, test-surface design.
- `vol3-pre-edit-verification`: mandatory pre-edit check blocks on high-risk surfaces.
- `vol3-swarm-orchestration`: Codex analogue of Claude swarm routines (user-authorized).

High-value hook surfaces:

- `session_start_context.py`: startup context loading.
- `user_prompt_router.py`: skill routing, rectification-mode hints.
- `pre_tool_use_policy.py`: destructive-command and pre-commit guardrails.
- `post_tool_use_review.py`: build/test failure blocking.
- `stop_continue.py`: convergence enforcement.

Architectural rule: keep this file compressive + always-on; move repeated deep workflows into skills; move deterministic enforcement into hooks; do not bloat the constitutional layer with playbook detail.

## LaTeX and Compute Library Conventions

- All macros in `main.tex` preamble. NEVER `\newcommand` in chapters (use `\providecommand`).
- Memoir class, EB Garamond (newtxmath + ebgaramond).
- Tags: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConditional`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`.
- Label everything with prefix-matched labels (`\label{def:}`, `\label{thm:}`, `\label{prop:}`, `\label{conj:}`). Cross-reference with `\ref`.
- Do not add packages without checking compatibility.
- Do not create new `.tex` files when content belongs in existing chapters.
- Compute engines live in `compute/lib/`; tests in `compute/tests/`. Every `\ClaimStatusProvedHere` theorem requires `@independent_verification(...)` decorated test.

## Git Discipline

- All commits authored by Raeez Lorgat. NEVER credit an LLM.
- `git stash` FORBIDDEN (AAP16). Use `git diff > patch.diff` + `git apply`.
- Never `git checkout` / `git restore` / `git reset` / `git clean` on tracked files without explicit user authorization.
- Constitution: `concordance.tex` (Vol I); this file (Vol III).
- Commits are authored events, not narrations. Commit messages describe what changed and why, not "the agent performed X".

## Final Meta-Rule

The dominant failure mode of this programme is not lack of sophistication. It is confusing two objects, two conventions, two statuses, or two levels of validity that happen to look similar in a special case.

Before trusting any sentence, name all five:

- the object;
- the convention;
- the status;
- the verification path;
- the scope.

If you cannot name all five, the sentence is not ready.
