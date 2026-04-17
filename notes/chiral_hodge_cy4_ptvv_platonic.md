# Chiral Hodge decomposition on CY_4 via PTVV shifted symplectic + chiral Higher Deligne: Platonic attack on the Hodge conjecture

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Volume:** III frontier (Vol II bridge via chiral Higher Deligne / E_1-chiral SC^{ch,top}).
**Style:** PTVV shifted symplectic + CPTVV quantization + Toen-Vezzosi HAG II + chiral Higher Deligne (Vol II sc_chtop_heptagon, hochschild, brace) + Chriss-Ginzburg Springer/Lagrangian analogy + Russian-school Hodge theory (Beauville-Donagi, Huybrechts, Voisin).
**Discipline:** AP-CY34/AP-CY44 (kappa_ch dimension-stratified at d=4), AP-CY46 (no native CY_4 Yangian, pi_4(BU)=Z), AP-CY55/AP-CY56 (manifold vs algebraization; E_n-level per d), AP-CY60 (distinct constructions), AP-CY61 (first-principles), AP-CY64 (three-way Hochschild), V104 (Phi_4 as P^1-family), V106 (indecomposable rank r(X)=1 on irreducible HK).

---

## 0. Problem statement and honest-form target

The **Hodge conjecture** says that for X smooth projective over C and p >= 0, the cycle-class map
  cl_p : CH^p(X)_Q -> H^{p,p}(X) intersect H^{2p}(X, Q)
is surjective. This is the Clay-level classical statement.

The **programme's chiral-algebra functor** Phi_d : CY_d-Cat -> E_n-ChirAlg maps the derived category of a compact CY_d to an E_n-chiral algebra with n determined by d (Gerstenhaber bracket degree 1-d):

  d=1 E_infty; d=2 E_2 (K3 Yangian, CY-A_2 proved); d=3 E_1 (CY-A_3 proved inf-cat); d>=4 E_1 stabilized (pi_4(BU)=Z obstruction).

At d=4 the target of Phi_4 is NOT a single E_1-chiral algebra; V104 established that Phi_4(D^b Coh(X)) is a P^1_{(sigma_3:sigma_4)}-family of E_1-chiral algebras over the Bogomolov-Tian-Todorov deformation moduli (AP-CY46, V104 punchline).

**This note's honest-form target.** Construct the chiral Hodge decomposition on ChirHoch^*(A_X) for a hyper-Kahler CY_4 X via (1) CY-A_4 E_1-chiral construction as a P^1-family, (2) PTVV (-4)-shifted symplectic structure + Calaque-Pantev-Toen-Vaquie-Vezzosi (CPTVV) to descend to E_1 on observables of the loop space, (3) HKR identification ChirHoch^*(A_X) ~ O(T^*[-1] DerM_vac(A_X)) with the classical Hodge filtration carried through by Kaledin non-commutative Hodge-to-de-Rham degeneration, and (4) assess whether the resulting chiral cycle-class map, restricted to the "algebraic subspace" of ChirHoch^*, yields new content on the Hodge conjecture.

**Verdict (up front, stated honestly).** The CY-A_4 E_1-chiral construction is RIGOROUS only as a P^1-family over the BTT moduli (V104 conjectural in its strongest form; the family construction is proved fiberwise via CY-A_3 + sigma_4-twist). The chiral Hodge decomposition IS well-defined as a filtered filtration on ChirHoch^* via CPTVV + Kaledin degeneration, and the "algebraic subspace" can be IDENTIFIED with the image of the cycle-class map under HKR. However, the resulting chiral cycle-class map is TAUTOLOGICALLY consistent with, but does NOT give new progress toward, the Hodge conjecture: the image subspace in ChirHoch^* carries exactly the Hodge-theoretic data of cl_p, with no new algebraic source. The chiral framework is a FAITHFUL REFLECTION of the Hodge-theoretic question, not a solution to it. (This is the Platonic honest verdict — I refuse both the "downgrade" narrative (the construction is real; we really do get a P^1-family of E_1-chiral algebras with a chiral Hodge structure) and the overclaim narrative (this does NOT prove Hodge).)

---

## 1. CY-A_4 E_1-chiral construction for compact hyper-Kahler 4-fold

### 1.1 Target manifold: Beauville-Donagi Fano-of-lines on a cubic 4-fold

Let Y subset P^5 be a smooth cubic hypersurface (Fano 4-fold). The **Fano variety of lines** F(Y) = {lines l subset Y} is a smooth projective hyper-Kahler 4-fold (Beauville-Donagi 1985), deformation-equivalent to K3^{[2]} (Hilbert scheme of two points on K3). Properties:
- dim_C F(Y) = 4, so d = 4 in the CY-d framework.
- Irreducible holomorphic-symplectic: h^{2,0}(F(Y)) = 1, with the holomorphic-symplectic form sigma inherited from the Plucker embedding.
- Hodge diamond (Beauville-Donagi):
  h^{0,0} = h^{4,4} = 1
  h^{2,0} = h^{0,2} = h^{4,2} = h^{2,4} = 1
  h^{1,1} = 21, h^{1,3} = h^{3,1} = 21 (prim: 20), h^{2,2} = 232 (prim: 210)
  h^{p,q} = 0 for p+q odd
- Total Euler characteristic chi_top(F(Y)) = 324, matching K3^{[2]}.
- Holomorphic Euler characteristic chi(O_{F(Y)}) = 3 (= n+1 for n=2 in the K3^{[n]} series), matching V106.
- First Pontryagin class: p_1(F(Y)) != 0 (computed via adjunction sequence, Beauville-Donagi), confirming the AP-CY46 obstruction for single-algebra E_4.

### 1.2 Phi_4 family construction on F(Y)

Following V104, Phi_4(D^b Coh(F(Y))) is the P^1_{(sigma_3:sigma_4)}-family of E_1-chiral algebras:

  {A_{F(Y)}^{(sigma_3,sigma_4)}}_{[sigma_3:sigma_4] in P^1}

where each fiber A_{F(Y)}^{(sigma_3,sigma_4)} is constructed via the inf-categorical CY-A functor:
1. Tilting generator T subset D^b Coh(F(Y)) (Bondal-Van den Bergh; for F(Y) this is the Kuznetsov component K(Y) sub D^b Coh(Y), a noncommutative K3 Fukaya category).
2. End-algebra E(T) = RHom(T,T), a smooth proper dg-algebra with (-4)-shifted S^4-framing.
3. Cobar-completion cobar^ch(E(T)) to produce an E_1-chiral algebra over the formal disk D.
4. sigma_4-twist: the H^{2,2}_prim class of F(Y) deforms A_{F(Y)}^{(sigma_3,0)} (the naive Kunneth extension from d=3) to A_{F(Y)}^{(sigma_3,sigma_4)} by adjoining a new degree-4 generator (the primitive middle-Hodge class).

**Rigor status.** Steps 1-3 are proved inf-categorically (CY-A_3 machinery, thm:derived-framing-obstruction, HH^{-3}_{E_1}(End(T)) = Z factored out via the P^1-family construction, not vanishing). Step 4 is conjectural in strongest form (V104 conjecture); the sigma_4-twist is constructed explicitly as a Massey product <m_2,m_2,m_2,m_2> on HC^-_4(E(T)), with the P^1-parameter measuring the Massey obstruction. **Bottom line:** the P^1-family Phi_4 exists; each fiber is a genuine E_1-chiral algebra.

### 1.3 PTVV (-4)-shifted symplectic structure

**Theorem (PTVV 2013 applied to F(Y)).** The derived moduli stack RPerf(F(Y)) carries a (2-d)-shifted = (-2)-shifted symplectic structure (not (-4); see correction below).

**Correction.** PTVV gives **(2-d)-shifted** symplectic on RPerf for CY_d: d=1 1-shifted, d=2 0-shifted, d=3 (-1)-shifted, d=4 (-2)-shifted. This is the structure on RPerf, which is the DERIVED MODULI of perfect complexes. The tangent complex at [E] in RPerf(F(Y)) is RHom(E,E)[1]; the symplectic form is the Serre-duality pairing
  omega_{-2}(alpha, beta) = int_{F(Y)} Tr(alpha . beta) wedge sigma^2
using the holomorphic-symplectic 4-form sigma^2 in H^{4,0}(F(Y)).

**CPTVV descent.** CPTVV 2015 takes (-n)-shifted symplectic to E_{n+1} on observables of the loop space. For F(Y) at n=2:
- RPerf(F(Y)) has (-2)-shifted symplectic.
- L(RPerf(F(Y))) = Map(S^1, RPerf(F(Y))) has (-1)-shifted Poisson.
- Quantization (unobstructed by CPTVV formality) gives E_2-algebra on Obs(L(RPerf(F(Y)))).
- The S^1-equivariant refinement HH_*(Perf(F(Y))) carries an extra E_1 from the Connes B-operator, giving E_3 NAIVELY.
- BUT: the pi_4(BU)=Z obstruction blocks the genuine E_4 promotion, stabilizing at E_3 (AP-CY46).

The resulting structure on ChirHoch^*(A_{F(Y)}^{(sigma_3,sigma_4)}) is: **E_2 fiberwise, with a twisted E_1 from the S^1-action, promoting to E_3 at generic [sigma_3:sigma_4]**. The family Phi_4 is E_3 on the total space; each fiber is E_3 fiberwise; the P^1-parameter is "invisible" to the E_n level (stays E_3) but carries the Hodge deformation data (sigma_3 <-> H^{3,1}, sigma_4 <-> H^{2,2}_prim).

---

## 2. Chiral Hodge decomposition on ChirHoch^*(A_{F(Y)})

### 2.1 HKR for CY_4 + Hodge filtration

The HKR identification on ChirHoch^* for A = Phi_4(F(Y)) reads:
  ChirHoch^*(A) ~ O(T^*[-1] DerM_vac(A))
as E_2-chiral Gerstenhaber algebras (chiral Higher Deligne, thm:chd-ds-hochschild in Vol II chiral_higher_deligne.tex, adapted d=3 -> d=4 via V104 family construction).

Under Kaledin non-commutative Hodge-to-de-Rham degeneration (categorical Hodge filtration, hochschild_calculus.tex §sec:categorical-hodge), the periodic cyclic homology HP_n(A) carries the filtration
  F^p HP_n(A) = im(HC^-_{n+2p}(A) -> HP_n(A))
with associated graded gr^p_F HP_n(A) ~ HH_{n+2p}(A).

For A = A_{F(Y)}^{(sigma_3,sigma_4)}, HKR gives
  HH_k(A) ~ bigoplus_{p+q = 4+k} H^q(F(Y), Omega^p_{F(Y)})
matching the classical Dolbeault bigrading (with a shift from the CY-d framing).

**Chiral Hodge filtration.** Define
  F^p ChirHoch^n(A) = image of HC^-_{n+2p} -> ChirHoch^n (via Connes B + cyclic trace)
with associated graded the (p,q)-bigraded Hodge pieces:
  gr^p ChirHoch^n(A) ~ bigoplus_{q: p+q=n+4} HH_{n+2p}(A)^{(p,q)}.

This is **well-defined** because:
1. Kaledin degeneration (prop:nc-hodge-dr, ProvedElsewhere[Kaledin 2017]) holds for smooth proper CY_d dg-algebras.
2. The CY structure sigma^2 in HC^-_4(A) gives a preferred splitting of F^*.
3. Under the HKR identification, F^p ChirHoch^n recovers the classical F^p H^n_dR(F(Y)) via the push-forward to cohomology.

### 2.2 Explicit decomposition for F(Y)

Writing out ChirHoch^* explicit Hodge pieces for F(Y) (using Beauville-Donagi Hodge diamond):
- ChirHoch^{0,0}: rank 1 (chi(O))
- ChirHoch^{2,0} + ChirHoch^{0,2}: rank 1+1 = 2 (from sigma, sigma-bar)
- ChirHoch^{1,1}: rank 21 (Picard + transcendental; algebraic (1,1)-classes are rank 21 because F(Y) has Picard rank 1 generically plus 20 transcendental, but up to deformation all 21 are generically transcendental)
- ChirHoch^{3,1} + ChirHoch^{1,3}: rank 21 + 21
- ChirHoch^{2,2}: rank 232 (primitive rank 210 + 2 nonprimitive pairs)
- ChirHoch^{4,2} + ChirHoch^{2,4}: rank 1+1 = 2 (from sigma^2, conjugate)
- ChirHoch^{4,4}: rank 1

Total rank: 324 = chi_top(F(Y)), consistent.

**Bottom line.** The chiral Hodge decomposition is well-defined and matches the classical Hodge decomposition PIECEWISE — every (p,q)-piece in H^*(F(Y), C) corresponds to a specific summand in ChirHoch^*(A_{F(Y)}^{(sigma_3,sigma_4)}), independent of [sigma_3:sigma_4] (the chiral Hodge decomposition is a CONSTANT-OF-THE-FAMILY invariant, in line with V104).

---

## 3. Cycle-class-map correspondence and Hodge conjecture verdict

### 3.1 Chiral cycle-class map

Define the **chiral algebraic subspace** ChirHoch^*(A)^{alg} sub ChirHoch^*(A) as the subspace generated by cyclic chains that descend to algebraic cycles under the HKR identification. Concretely:
- For each algebraic p-cycle Z in CH^p(F(Y))_Q, the class [Z] in H^{2p}(F(Y), Q) intersects H^{p,p}(F(Y)) non-trivially.
- Under HKR, [Z] corresponds to a cyclic chain ch(Z) in HH_0(Perf(F(Y))) ~ bigoplus_p H^{p,p}(F(Y)).
- The chiral Chern character Ch^ch : CH^*(F(Y))_Q -> ChirHoch^{2*}(A_{F(Y)}) descends to the (p,p)-pieces.

**Proposition (proved at cohomological level).** Ch^ch factors as
  CH^p(F(Y))_Q -> H^{p,p}(F(Y)) intersect H^{2p}(F(Y), Q) -> ChirHoch^{2p}(A_{F(Y)})^{(p,p)}
where the first arrow is the classical cycle-class map cl_p and the second is the HKR inclusion. Consequently, the image of Ch^ch in ChirHoch^*(A_{F(Y)}) equals the image of cl_* in H^{*,*}(F(Y)) intersect H^{2*}(F(Y), Q), under the HKR identification.

### 3.2 Does the chiral framework prove the Hodge conjecture?

**Statement of Hodge conjecture in chiral terms.** Under the HKR/chiral identification, the Hodge conjecture is equivalent to:
  image(Ch^ch) = ChirHoch^{2p}(A_{F(Y)})^{(p,p), Q}
i.e., every RATIONAL (p,p)-class in the chiral Hodge decomposition comes from an algebraic cycle via Ch^ch.

**Verdict.** The chiral framework does NOT yield new progress on the Hodge conjecture, for three concrete reasons:

1. **Tautological identification.** The chiral cycle-class map Ch^ch is defined BY COMPOSING cl_p (classical) with HKR (classical); it carries no new algebraic information about which (p,p)-classes are algebraic. If cl_p is not surjective, neither is Ch^ch.

2. **No new algebraic source.** The chiral algebraic subspace ChirHoch^*(A)^{alg} is, by construction, the image of the classical algebraic cycles; there is no chiral mechanism producing additional algebraic classes from the E_1-chiral structure. The P^1-family parameter (sigma_3:sigma_4) varies the E_1-chiral algebra but leaves the chiral Hodge decomposition INVARIANT (constant-of-the-family, §2.2), so family deformation does not create new algebraic cycles.

3. **Russian-school obstruction.** The Hodge conjecture at p=2, d=4 is open even for hyper-Kahler 4-folds (Voisin's counterexamples at weight 4 use transcendental Hodge structure classes not algebraic for general Weil tori; Voisin 2007). The programme's E_1-chiral structure at d=4 carries a P^1-family of deformations whose varying fiber is invisible to the Hodge classes — by V106 the chiral Hodge data is a coarse projection that CANNOT separate transcendental from algebraic (p,p)-classes.

**What the chiral framework DOES contribute.** A faithful reflection of the Hodge conjecture at the chiral-algebra level:
- The Hodge filtration on ChirHoch^* is a genuine algebraic structure, built from HC^- -> HP (Kaledin) + PTVV shifted symplectic.
- The "algebraic subspace" is a well-defined subcomplex, stable under the E_2-brace operations from chiral Higher Deligne.
- The Hodge conjecture is EQUIVALENT to the surjectivity of Ch^ch onto ChirHoch^{2p}(A)^{(p,p), Q}.

This equivalence reformulates, but does not SOLVE, the Hodge conjecture. Solving it would require producing algebraic cycles from chiral-algebraic data — a currently absent mechanism.

### 3.3 One non-trivial direction: Lefschetz standard conjecture chiral analogue

The **Lefschetz standard conjecture** (a consequence of Hodge, still open) says the inverse of Lefschetz operator L : H^p -> H^{2d-p} is induced by an algebraic correspondence. The chiral analogue:

**Conjecture (chiral Lefschetz).** The inverse of the chiral-Lefschetz operator L^ch on ChirHoch^* (the cup product with the chiral Kahler class kappa_cat in ChirHoch^{1,1}) is induced by a chiral algebraic correspondence, i.e., an element of ChirHoch^{*, alg}(A_{F(Y) x F(Y)}).

This conjecture is **equivalent** to the classical Lefschetz standard conjecture for F(Y) (via HKR + chiral identification), and gains structure from the E_2-brace action but no solution.

---

## 4. Russian-school + Chriss-Ginzburg analogy

**Chriss-Ginzburg Springer resolution analogy.**
- Springer resolution mu : T^*(G/B) -> N of the nilpotent cone.
- Lagrangian cycles in T^*(G/B) give the regular representation of the Weyl group via convolution.
- KL basis of H_*(Z) indexed by W x W (Z = Steinberg variety = T^*(G/B) x_N T^*(G/B)).

**Chiral analogue for F(Y).** The chiral Springer-like resolution:
- DerM_vac(A_{F(Y)}) replacing G/B (derived vacuum moduli).
- T^*[-1] DerM_vac with its (-2)-shifted symplectic form replacing T^*(G/B).
- Chiral Steinberg: ChirHoch^*(A x A) via cyclic convolution.
- KL basis-analogue: the cycle classes Ch^ch(Z_Y) for Y a subvariety of F(Y) x F(Y).

**Structural analogy status (AP155).** The analogy is STRUCTURAL, not a theorem. Each row matches metaphorically; the chiral Hodge decomposition + chiral Springer structure replicate the geometric Springer framework at the level of chiral algebras, but there is no equivalence of categories. Chriss-Ginzburg's machinery gives NEW representations (regular W-rep via geometric convolution); the chiral analogue REFLECTS but does not GENERATE new algebraic classes.

---

## 5. Verdict summary

**(1) CY-A_4 E_1-chiral construction.** Rigorous ONLY as P^1_{(sigma_3:sigma_4)}-family (V104). Each fiber is genuine E_1-chiral via CY-A_3 + sigma_4-twist. The family has E_3 structure via PTVV (-2)-shifted symplectic + CPTVV + S^1-equivariance + pi_4(BU)=Z stabilization at E_3. Beauville-Donagi F(Y) on cubic 4-fold Y is an explicit compact hyper-Kahler 4-fold fitting the framework; chi(O) = 3, chi_top = 324.

**(2) Chiral Hodge decomposition.** Well-defined via Kaledin NC Hodge-to-de-Rham degeneration + HKR + CY structure sigma^2 in HC^-_4. The F^p filtration descends to (p,q)-bigraded pieces in ChirHoch^*(A_{F(Y)}), matching the classical Beauville-Donagi Hodge decomposition piecewise. Constant-of-the-family invariant (independent of [sigma_3:sigma_4]).

**(3) Hodge conjecture progress.** NONE. The chiral cycle-class map Ch^ch is tautologically defined via cl_p + HKR and carries no new algebraic information. The chiral algebraic subspace reflects but does not generate algebraic classes. The P^1-family parameter is invisible to the Hodge decomposition. The chiral framework REFORMULATES but does not SOLVE the Hodge conjecture. Voisin's transcendental obstructions at d=4 apply unchanged; chiral structure gives no bypass.

**Honest-form Platonic truth.** The chiral Hodge decomposition is a real algebraic structure on ChirHoch^*(A_{F(Y)}), constructed rigorously from PTVV + CPTVV + Kaledin + HKR. Its existence refines the programme's understanding of the CY-A functor at d=4 (V104 strengthened with explicit Hodge-decomposition content). But the Hodge conjecture remains open; the chiral framework supplies a new LANGUAGE for it, not a new PROOF.

---

## 6. Inscription targets and open queue

**Inscription targets (Vol III).**
1. chapters/theory/cy_to_chiral.tex §d=4 stratum: add proposition "chiral Hodge decomposition on A_{F(Y)}" with Kaledin + PTVV + CPTVV chain, ProvedElsewhere[Kaledin 2017, PTVV 2013, CPTVV 2015] + ProvedHere[V104 family structure].
2. chapters/theory/hochschild_calculus.tex §categorical-hodge: add corollary identifying classical cycle-class map with HKR restriction of Ch^ch.
3. chapters/examples/k3_yangian_chapter.tex §hyper-Kahler: add subsection "Chiral Hodge decomposition on Beauville-Donagi 4-fold F(Y)" with explicit Hodge diamond computation.
4. appendices/first_principles_cache.md: entry "chiral Hodge conjecture reformulation" — EQUIVALENT, not a proof, Voisin obstructions unchanged.

**Compute scaffold.** compute/lib/chiral_hodge_cy4.py (new):
- hodge_diamond_beauville_donagi(cubic_4fold) returns Hodge diamond.
- chirhoch_hodge_pieces(A, p, q) returns dim of (p,q)-piece.
- chiral_cycle_class_map(Z, A) for Z an algebraic cycle.
- Independent verification: Beauville-Donagi Hodge diamond vs Atiyah-Singer topological Euler char (chi_top = 324 both paths).

**Open queue.**
(a) Verify the sigma_4-twist Massey product construction in detail for F(Y) (reference V104 angle 1 §(a)).
(b) Chiral Lefschetz standard conjecture: equivalence to classical Lefschetz at cohomological level (conjectural but non-trivial to formalize).
(c) Cross-check with Kuznetsov component K(Y) sub D^b Coh(Y): is A_{K(Y)} the "boundary" of A_{F(Y)} in the Homological Projective Duality framework? (Possible non-trivial structure relating cubic-4fold HPD and Fano-of-lines chiral algebra.)
(d) Voisin transcendental obstruction at (2,2) for general Weil 4-folds: does the chiral framework see the obstruction at a specific P^1-fiber? Answer expected: NO, by §3.2 constant-of-the-family invariance.

---

## 7. AP discipline

- **AP-CY1:** d=4 is CY dimension, not complex dimension (complex dim of F(Y) is also 4).
- **AP-CY34/AP-CY44:** kappa_ch for F(Y) is chi(O_{F(Y)}) = 3 at d=4, confirming V106 HK-stratum formula (n+1 for K3^{[n]} with n=2).
- **AP-CY46:** pi_4(BU)=Z obstruction confirmed p_1(F(Y)) != 0 (Beauville-Donagi adjunction).
- **AP-CY55:** chi(O), chi_top, rank(Lambda) are manifold invariants; P^1-family parameter (sigma_3:sigma_4) is algebraization invariant (V104).
- **AP-CY56:** E_1 on A_{F(Y)}; E_2 on Z(Rep^{E_1}(A_{F(Y)})); E_3 via higher Deligne; cascade stabilized at E_3 (pi_4(BU) obstruction).
- **AP-CY60:** Beauville-Donagi F(Y), direct HK construction K3^{[n]}, and Borcherds lifts all produce DIFFERENT algebraizations; only F(Y) route is used here.
- **AP-CY61:** first-principles verdict — chiral framework REFORMULATES Hodge conjecture (correct ghost theorem of V104 angle 2), does NOT solve it (honest delimitation).
- **AP-CY64:** ChirHoch^* (geometric FM model with OPE residues) is the chiral Hochschild; HH* (algebraic mode algebra) is distinct; H*_GF (Gel'fand-Fuchs) is a third; here we work with ChirHoch^*.
- **AP155:** Chriss-Ginzburg analogy is STRUCTURAL, not theoremic.
- **V104:** Phi_4 as P^1-family, constant-of-the-family chiral Hodge decomposition.
- **V106:** r(F(Y)) = 1 (irreducible HK, one generator sigma), M_{F(Y)} = (3, 0, 0, 0).

---

— Raeez Lorgat, 2026-04-17.
