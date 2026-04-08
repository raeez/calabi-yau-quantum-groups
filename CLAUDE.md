# CLAUDE.md — Calabi-Yau Quantum Groups

## What This Is

Research monograph by Raeez Lorgat. Volume III of the modular Koszul duality programme. Volumes I (~2,453pp, ~/chiral-bar-cobar) and II (~1,478pp, ~/chiral-bar-cobar-vol2) built the bar-cobar machine for chiral algebras and its 3D HT QFT interpretation. This volume constructs the **geometric source**: the functor from Calabi-Yau categories to chiral algebras that provides the input data for the entire programme.

**Title**: *CY Categories, Quantum Groups, and BPS Algebras*

**Current status**: 206 pages, clean build, 17,199 tests passed. Abstract written (35 lines). 12 skeletal stub chapters require development or removal (AP114).

## The Central Question

A CY category C of dimension d carries a cyclic A-infinity structure: a non-degenerate trace Tr: HH_*(C) -> k[-d] on Hochschild homology. The cyclic bar complex CC_*(C) with its S^d-framing is the primary invariant.

A chiral algebra A carries a bar complex B(A), a factorization coalgebra on Ran(X), with the full modular structure controlled by Theta_A (Vol I).

**The programme**: construct a precise functor Phi: CY_d-Cat -> E_2-ChirAlg that:
1. Takes a CY category (Fukaya, derived, matrix factorization, or more general) as input
2. Extracts the cyclic A-infinity structure and its S^d-framing
3. Produces a chiral algebra A_C on a curve X via factorization envelope
4. Lifts to an E_2-chiral algebra whose representation category is braided monoidal
5. Realizes the CY trace as the modular characteristic kappa(A_C)

Vol III is the geometric source of chiral algebras. The CY categories are abstract categorical inputs; the output is the chiral algebra data that Vols I-II then process through bar-cobar duality, the shadow obstruction tower, and the HT QFT machine. The flow is: **CY category -> chiral algebra -> bar complex -> modular characteristic -> partition function**.

## The E_1/E_2 Chiral Hierarchy

The key structural ingredient, extending the E_1 theory from Vol II:

- **E_1-chiral algebras** (Vol II, Part I): associative factorization on C x R. Representation categories are monoidal.
- **E_2-chiral algebras** (this work): braided factorization on C x C. Representation categories are braided monoidal: the natural habitat of quantum groups.
- **The E_1 -> E_2 passage** via Dunn additivity: E_2 ~ E_1 tensor E_1.
- **The CY connection**: for d=2, the S^2-framing of HH_*(C) provides an E_2-algebra structure on cyclic homology: the braiding.
- **The d=3 story**: holomorphic Chern-Simons breaks E_2 to E_1. Braiding is recovered via the Drinfeld center Z(Rep^{E_1}(A)) ~ Rep^{E_2}(Z^der_ch(A)). This is the categorified averaging map av: E_1-Cat -> E_2-Cat.

The Drinfeld center Z(Rep^{E_1}(A)) ~ Rep^{E_2}(Z^der_ch(A)) provides the categorical incarnation of the bulk-boundary correspondence: E_1 boundary -> E_2 bulk via the center construction.

## E_1/Ordered as Primitive (PERMANENT, 2026-04-08)

**The E_1/ordered story is the natural primitive across all three volumes.** In Vol III, this has a specific incarnation: the E_1-chiral algebra (boundary) is the primitive object; the E_2-chiral algebra (bulk) is obtained from it by the Drinfeld center construction; quantum groups (Rep_q(g)) are the natural categorification of E_1 data. The averaging map av: g^{E_1} -> g^mod from Vol I becomes the center construction Z: E_1-Cat -> E_2-Cat in Vol III. The passage from E_1 to E_2 is the higher-categorical analogue of Sigma_n-coinvariance.

**Consequence for Vol III architecture:** Quantum groups, Yangians, and braided tensor categories are NATIVELY E_1 objects. The E_2/braided structure arises via the Drinfeld center, which is the categorified averaging map. The CY-to-chiral functor Phi should be understood as lifting E_1 data (the boundary A-infinity-algebra from the CY category) to E_2 data (the bulk chiral algebra): this is the center construction in the factorization setting. See Vol I `princ:e1-primacy` for the full architectural thesis.

**Where E_1 enters at d=3:** Holomorphic Chern-Simons on a CY threefold produces an E_1-chiral algebra (not E_2). The holomorphic direction along the curve gives the chiral structure; the real direction from the 3d bulk gives the E_1/topological colour. The braided (E_2) structure is recovered via the Drinfeld center. This is the Vol III incarnation of the Vol I averaging map: the E_1 data is primary, the E_2 data is derived.

## Main Theorems (Targets) — Status

- **CY-A** (CY-to-chiral functor): Construction of Phi: CY_d-Cat -> E_2-ChirAlg via E_2-factorization envelope.
  - **d=2: PROVED.** All three steps (cyclic A-infinity -> Lie conformal -> factorization envelope -> E_2 enhancement) are unconditional.
  - **d=3: PROGRAMME.** Steps (1) and (2) are unconditional. Step (3) (the E_2 lift) is conditional on the chain-level S^3-framing construction. The E_1 structure from holomorphic Chern-Simons is unconditional; the E_2 recovery via Drinfeld center is the programme.
- **CY-B** (E_2-chiral Koszul duality): Bar-cobar adjunction in the E_2-chiral setting, CY trace as curvature.
  - **Status: PROGRAMME.** Depends on CY-A at the relevant dimension. The bar-cobar machinery from Vol I transports; the new content is the E_2-enhancement of the adjunction.
- **CY-C** (Quantum group realization): Rep^{E_2}(A_C) is braided monoidal equivalent to C itself, when C arises from a quantum group (generalizing Kazhdan-Lusztig).
  - **Status: CONJECTURAL.** The CY category C(g,q) is not constructed in general. The theorem is a conjecture until the construction exists. Uses \begin{conjecture}, NOT \begin{theorem} (AP40).
- **CY-D** (Modular CY characteristic): kappa(A_C) = chi^CY(C), genus-g obstruction recovers GW/Hochschild invariants.
  - **Status: PROGRAMME.** kappa is well-defined only when the chiral algebra A_C exists, which is unconditional only at d=2. At d=3, conditional on CY-A step (3). The kappa-spectrum notation (AP113) must be used: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber are distinct invariants.

## The kappa-Spectrum (AP113, CRITICAL)

For CY manifolds of dimension d >= 3, a single CY manifold can give rise to MULTIPLE chiral algebraizations, each with its own kappa. Bare "kappa" is FORBIDDEN in Vol III. ALWAYS subscript:

- **kappa_ch**: from the chiral algebra A_C constructed via Phi. For K3 x E: kappa_ch = 3 (complex dimension of the CY threefold).
- **kappa_BKM**: from the Borcherds-Kac-Moody algebra associated to the lattice. For K3 x E: kappa_BKM = 5 (weight of the Igusa cusp form Delta_5).
- **kappa_cat**: from the categorical/holomorphic Euler characteristic. For K3 x E: kappa_cat = 2 = chi(O_{K3}).
- **kappa_fiber**: from the lattice/fiber structure. For K3 x E: kappa_fiber = 24 (rank of the lattice).

The kappa(K3 x E) = 3 vs 5 contradiction that appeared in this volume arose from conflating kappa_ch and kappa_BKM. Four algebras see four aspects of the same manifold. The full kappa-spectrum Spec_kappa(K3 x E) = {2, 3, 5, 24} is the correct invariant.

## Architecture (Five Parts)

**Part I -- The CY Engine** (part:cy-categories)
- Introduction (328 lines)
- CY categories (70 lines -- **STUB**, AP114)
- Cyclic A-infinity structures (55 lines -- **STUB**, AP114)
- Hochschild calculus (36 lines -- **STUB**, AP114)
- E_1-chiral algebras (90 lines -- near-stub)
- E_2-chiral algebras (156 lines)
- E_n-factorization and higher chiral structure (308 lines)

**Part II -- The CY Characteristic Datum** (part:bridge)
- CY-to-chiral functor (1,547 lines -- substantial)
- Quantum chiral algebras (163 lines)
- The modular trace (143 lines)
- Quantum groups foundations (24 lines -- **STUB**, AP114)
- Braided factorization (45 lines -- **STUB**, AP114)
- Drinfeld center and bulk algebras (39 lines -- **STUB**, AP114)

**Part III -- The CY Landscape** (part:examples)
- Toroidal and elliptic examples (5,806 lines -- substantial, includes K3 x E)
- Toric CY3 CoHA (389 lines)
- Fukaya categories (32 lines -- **STUB**, AP114)
- Derived categories of CY manifolds (27 lines -- **STUB**, AP114)
- Matrix factorizations (29 lines -- **STUB**, AP114)
- Quantum group representations (42 lines -- **STUB**, AP114)

**Part IV -- The Seven Faces of r_CY(z)** (part:connections)
- Bar-cobar bridge to Volume I (530 lines)
- CY holographic datum (905 lines)
- Modular Koszul bridge (13 lines -- **STUB**, AP114)

**Part V -- The CY Frontier** (part:frontier)
- Geometric Langlands and CY quantum groups (28 lines -- **STUB**, AP114)

**12 skeletal stub chapters** (< 50 lines, no theorems): cy_categories, cyclic_ainf, hochschild_calculus, quantum_groups_foundations, braided_factorization, drinfeld_center, fukaya_categories, derived_categories_cy, matrix_factorizations, quantum_group_reps, modular_koszul_bridge, geometric_langlands. Each must be developed or commented out of \include (AP114).

## Dependencies on Volumes I and II

| Volume | Provides | Used here |
|--------|----------|-----------|
| I (Modular Koszul Duality) | Bar-cobar machine, Theta_A, kappa(A), five theorems (A-D+H), shadow obstruction tower, G/L/C/M classification | CY bar complex, modular trace, shadow depth of CY chiral algebras |
| II (A-infinity Chiral Algebras and 3D HT QFT) | SC^{ch,top}, PVA descent, DK bridge, E_1 sector, holographic modular Koszul datum | E_1 chiral theory, braided structure, bulk-boundary, H(T) for CY systems |

## REGRESSION SAFEGUARDS (PERMANENT, 2026-04-08)

The 78-agent session on 2026-04-08 fundamentally upgraded the programme's self-understanding. The following 20 constraints are HARD RULES that override any default behavior. A future agent must understand ALL 20 from the first token.

1. **RS-1: The Heisenberg is the CG opening, NOT the atom.** (AP108)
2. **RS-2: B^ord is the primitive, B^Sigma is the shadow.** (AP65, AP97, AP104)
3. **RS-3: Physics IS the homotopy type, not a "bridge" or "application."** (AP106, AP115)
4. **RS-4: Costello/Dimofte/Gaiotto content belongs in the mathematical core.**
5. **RS-5: Show, do not tell.** Never "This chapter constructs..." (AP106, AP109, AP111)
6. **RS-6: The convergent writing loop is mandatory.** First-pass prose is never final.
7. **RS-7: The symmetric bar is NOT the default.** "The bar complex" means B^ord. (AP82, AP85, AP102)
8. **RS-8: "Abelian CS" = Heisenberg.** Same OPE. (AP105)
9. **RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.**
10. **RS-10: Single-pass agent work without audit is forbidden.**
11. **RS-11: kappa without subscripts is FORBIDDEN in Vol III.** Always kappa_ch, kappa_BKM, kappa_cat, kappa_fiber. (AP113, CRITICAL FOR THIS VOLUME)
12. **RS-12: The programme is three volumes, not two.**
13. **RS-13: In Vol II, gravity is the climax (Part VI), not middle content.**
14. **RS-14: Introduction orients, Overture instantiates.**
15. **RS-15: Koszul programme before higher_genus in the dependency DAG.**
16. **RS-16: No forward-reference trailers.** (AP109)
17. **RS-17: No "What this chapter proves" remark blocks.** (AP111)
18. **RS-18: r^coll(z) differs from the Laplace-transform r(z) for odd generators.** (AP107)
19. **RS-19: The preface is a complete survey, not a compressed summary.**
20. **RS-20: Memory files with stale page counts or rejected designs are not current.** (AP112)

## The Multi-Path Verification Mandate

Inherited from Vol I. **Every computational result must be supported by multiple independent computations that all point to the same result.** Minimum: 3 genuinely independent verification paths per numerical claim. See Vol I CLAUDE.md for the full verification path taxonomy (8 methods). The compute/ layer is the verification engine; every formula needs corresponding multi-method tests. Cross-volume propagation (AP49) is especially critical: Vol III uses motivic/categorical conventions that differ from both Vol I (OPE modes) and Vol II (lambda-brackets). NEVER paste a formula between volumes without explicit convention conversion and independent numerical verification.

## The Beilinson Principle

Inherited from Vol I. Every claim is false until independently verified. The six hostile examiners (Beilinson, Witten, Costello, Gaiotto, Drinfeld, Kontsevich) apply. All anti-patterns AP1-AP115 from Vol I carry over.

**Additional CY-specific pitfalls**:
- **AP-CY1**: CY dimension d != complex dimension n. For a CY manifold X of complex dimension n, Fuk(X) is CY of dimension n, D^b(Coh(X)) is CY of dimension n. Do not confuse with real dimension 2n.
- **AP-CY2**: The CY trace is a class in HC^-_d(C), NOT just a map HH_d -> k. The negative cyclic refinement is essential for the S^d-framing.
- **AP-CY3**: E_2 != commutative. E_2-algebras have a braiding but it is NOT symmetric in general. The symmetrization E_2 -> E_infty loses the quantum group structure.
- **AP-CY4**: Drinfeld center != derived center in general. Z(C) (Drinfeld center of a monoidal category) and Z^der_ch(A) (chiral derived center) agree under specific hypotheses. State which center you mean.
- **AP-CY5**: Kazhdan-Lusztig equivalence requires q a root of unity (or specific rationality conditions on k). At generic q, Rep_q(g) is semisimple and the story simplifies; the interesting structure is at roots of unity.
- **AP-CY6**: A_X does NOT exist for CY3. The chiral algebra of a Calabi-Yau threefold is the single load-bearing gap. CY-A is proved for d=2; for d=3, A_X is conditional on chain-level S^3-framing construction. NEVER write "A_X for CY3" as if it were a defined object.
- **AP-CY7**: CoHA != E_1-chiral algebra. The critical CoHA (Schiffmann-Vasserot, RSYZ) is an associative algebra; calling it "the E_1-sector of G(X)" assumes G(X) exists and has a CoHA inside it. The correct statement: "the CoHA is the target that the E_1-sector of G(X) should match, IF G(X) exists."
- **AP-CY8**: Borcherds denominator identity != bar Euler product. The identification requires the CY-to-chiral functor to exist in the relevant dimension. For K3 x E (d=3), Delta_5 is computed from the lattice, not from a chiral algebra (which doesn't exist yet). The "bar Euler product" interpretation is an OBSERVATION about the product formula, not a theorem derived from the bar complex.

## Anti-Patterns (inherited from Vols I-II + Vol III-specific)

All anti-patterns AP1-AP115 from Vol I CLAUDE.md apply here. The following are the most frequently triggered in this volume:

**AP38 -- Literature normalization convention in hardcoded values.** The BKM shadow obstruction tower engine hardcoded phi_{0,1} Fourier coefficients in the DVV convention (f(0,0)=20, f(1,0)=-252) instead of the Eichler-Zagier convention (f(0,0)=10, f(1,0)=108). The BKM identity was documented as FALSE for phi_{0,1}. **Rule: when hardcoding values from the literature, ALWAYS record the source paper and normalization convention.**

**AP42 -- Correct at sophisticated level, false at naive level.** "Scattering diagram = shadow obstruction tower" holds at the motivic Hall algebra level, but naive BCH pair-commutator does NOT reproduce phi_{0,1} multiplicities (commit 72ba062). The gap measures higher BPS bound-state contributions. **Rule: state the level of validity explicitly.**

**AP43 -- Central object defined by aspiration, not by axioms.** G(X) ("quantum vertex chiral group") used in ~20 locations without formal definition. "Quantum chiral algebra" defined as "equivalent to quantum group representation category": a prayer, not a definition. **Rule: MUST formally define before use. The central object of a volume MUST have a \\begin{definition}.**

**AP35 -- Accidentally correct theorem.** The [d_X, d_Y] = 0 identity was stated for all genera but qualified to genus 0 (commit a0ff317). Check whether genus-extension claims rest on genus-0 proofs. **Rule: verify proof steps independently of the conclusion.**

**AP36 -- Biconditional overclaim.** CY-C was stated as "Theorem" but is a conjecture: the CY category C(g,q) is not constructed in general. CY-A was stated for all d but only d=2 is proved. **Rule: before writing "Theorem," verify the proof exists in THIS manuscript.**

**AP40 -- LaTeX environment contradicts claim status.** CY-C was in a theorem environment despite being conjectural. Each claim in k3_times_e.tex was relabeled Theorem/Conjecture/Observation (commit a0ff317). **Rule: environment MUST match status.**

**AP113 -- In multi-kappa contexts (CY threefolds), bare "kappa" is FORBIDDEN.** ALWAYS subscript: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber. (CRITICAL for Vol III: kappa(K3 x E) = 3 vs 5 contradiction arose from missing subscripts.)

**AP114 -- Stub chapters (<50 lines, no theorems) create false coverage.** Comment out \\include or develop. (CRITICAL for Vol III: 12 skeletal stub chapters found 2026-04-08.)

**AP115 -- Architectural commitments in CLAUDE.md MUST be enacted in .tex source.** The metadata-source gap is the most dangerous anti-pattern.

**AP44-AP49 (from the 139-fix three-volume rectification swarm, April 2026):**
- **AP44**: OPE mode != lambda-bracket coefficient (divided-power 1/n! factor). T_{(3)}T=c/2 -> {T_lambda T}=(c/12)lambda^3.
- **AP45**: Desuspension LOWERS degree: |s^{-1}v| = |v|-1, not |v|+1.
- **AP46**: eta(q) = q^{1/24} prod(1-q^n). The q^{1/24} is NOT optional.
- **AP47**: MC3 proved on evaluation-generated core. DK-4/5 is downstream, not part of MC3.
- **AP48**: kappa depends on the full algebra, not the Virasoro subalgebra. kappa=c/2 for Virasoro and holomorphic VOAs with dim V_1=0 (V-natural: kappa=12=c/2, RESOLVED). Lattice: kappa=rank (V_Lambda: kappa=24 != 12=kappa(V-natural) at same c=24). General VOAs with dim V_1>0: compute from bar complex.
- **AP49**: Cross-volume formula paste without convention conversion. Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic/categorical.

**AP59-AP61 (from the seven-faces swarm, April 7 2026):**
- **AP59**: Three distinct invariants must never be conflated: p_max(A) (generator OPE pole order) != k_max(A) (collision depth = p_max - 1) != r_max(A) (shadow depth, arity at which the obstruction tower terminates). The betagamma system is the archetypal witness: p_max(betagamma) = 1, k_max(betagamma) = 0, r_max(betagamma) = 4 (class C). Conflation produces wrong classifications. **Rule: when discussing "depth", always specify which invariant.**
- **AP60**: Status inflation when combining new and known content. When a theorem combines a new identification with classical results, do NOT tag the entire theorem ProvedHere. Restrict the ProvedHere claim to genuinely new content.
- **AP61**: Hardcoded values from CLAUDE.md descriptions inherit conflations. **Rule: never copy a numerical invariant from a CLAUDE.md description without verifying against (1) the OPE table, (2) landscape_census.tex, (3) at least one cross-engine comparison.**

## Anti-Patterns from the 2026-04-07 Frontier Research Swarm (AP62-AP80)

From the 125-agent session. See Vol I CLAUDE.md for FULL descriptions with examples and derivations. Summary:
- **AP62**: Bar cohomology "depends only on dim(g)" TRUE for Euler char, FALSE for individual dims
- **AP63**: CE(g_-) != chiral bar for multi-generator algebras (Orlik-Solomon correction)
- **AP64**: Same cohomology, different gradings -> different sequences (CE weight vs PBW degree)
- **AP65**: ORDERED (E1) bar is PRIMITIVE; unordered is derived quotient losing quantum group data
- **AP66**: Partition-type GFs (free fields) are NOT D-finite; interacting algebras ARE
- **AP67**: Strong generation != FREE strong generation (W(p) Koszulness OPEN)
- **AP68**: PVA slab ghost c != chiral algebra kappa (SVir kappa = (3c-2)/4, NOT (c+11)/2)
- **AP69**: tau_shadow satisfies kappa-DEFORMED KdV, NOT standard KdV. Obstruction kappa(kappa-1)
- **AP70**: Shadow L^sh(s) has POLES at s=1,2; negative integers are trivial zeros
- **AP71**: Shadow kappa != Dyson beta != Painleve parameter
- **AP72**: W-algebra NOP bar does NOT have d^2=0; needs full singular OPE + Orlik-Solomon
- **AP73**: BV=bar chain-level: PROVED G/L, CONDITIONAL C/M
- **AP74**: Shadow Eisenstein proof cites FALSE Bernoulli-Dirichlet identity
- **AP75**: Koszulness != H^k=0 in conformal weight grading (only PBW degree)
- **AP76**: Y_{1,1,1} has c=0 (NOT 3); kappa=Psi from Heisenberg channel
- **AP77**: Stokes ratio tests on convergent series give spurious instanton actions
- **AP78**: Hardy-Ramanujan 1729 "coincidence" in delta_F_2 is illusory
- **AP79**: W(p) has 4 strong generators, not 2
- **AP80**: Agents can produce engine without test file

## Anti-Patterns from the 2026-04-08 Bar/SC/E_1 Primacy Research (AP81-AP104)

From the 22-agent bar construction / Swiss-cheese / E_1 primacy investigation. See Vol I CLAUDE.md for FULL descriptions with proofs and derivations. These arise at the OPERADIC LAYER.
- **AP81**: Operadic bar of P-algebra != operadic bar of operad P. Use B_P(A) vs BP.
- **AP82**: Three coalgebra structures on bar: Lie^c (Harrison/coLie), Sym^c (coshuffle/cocommutative), T^c (deconcatenation/coassociative). NEVER conflate.
- **AP83**: Coshuffle (2^n terms) != deconcatenation (n+1 terms).
- **AP84**: B_{Com}(A) is cofree coLie, NOT cocommutative. CE complex is cocommutative; operadic bar is coLie.
- **AP85**: Factorization coproduct (Vol I, Sym^c) != deconcatenation coproduct (Vol II, T^c). Different objects, different geometries.
- **AP86**: FM_n(X) connected; only boundary strata factor as FM_{|S|} x FM_{n-|S|+1}.
- **AP87**: SC^{ch,top,!} mixed-sector dim = (k-1)! * C(k+m,m), NOT (k-1)! * m!.
- **AP88**: Cooperad P^i vs operad P^! notation collision. P^i = cooperad; P^! = (P^i)^v.
- **AP89**: B_{SC}(A) for one-coloured A is ill-formed. SC requires two-coloured (V_c, V_o).
- **AP90**: Promotion functor A -> (A,A): self-action gives SC input. Closed = B_{Com}(A), open = B_{Ass}(A).
- **AP91**: Curved d^2 = kappa * omega_g NOT a coderivation at g >= 1. Factor-2 cross-term discrepancy. Period-corrected D^{(g)} required.
- **AP92**: Algebra-level mu_0 (genus 0, strict) vs fiberwise d_fib^2 = kappa * omega_g (genus >= 1, Hodge). Different scales.
- **AP93**: delta_F_g^cross in CLOSED sector, NOT mixed sector. "Mixed channels" != "mixed sector."
- **AP94**: Polynomial Hilbert series != polynomial RING. ChirHoch^*(Vir_c) total dim <= 4. NEVER write C[Theta].
- **AP95**: ChirHoch != Gel'fand-Fuchs of Diff(S^1). Unrelated invariants at different categorical levels.
- **AP96**: Shadow algebra A^sh is bigraded LIE ALGEBRA, NOT ring. Bracket of degree 0, arity map -2.
- **AP97**: Averaging av: g^{E_1} -> g^mod is LOSSY. av(r(z)) = kappa; R-matrix strictly richer.
- **AP98**: kappa Eulerian weight parity-dependent. Even desuspension -> symmetric weight 2. Odd -> Harrison weight 1.
- **AP99**: K11 Lagrangian criterion CONDITIONAL on perfectness + bar-cobar normal-complex identification.
- **AP100**: Theorem C: eigenspace (C1) unconditional; scalar F_g = kappa * lambda_g (C2) uniform-weight only.
- **AP101**: "qi, not merely iso on cohomology" is tautological. Use "qi of A-infinity-algebras" vs "chain qi."
- **AP102**: Theorems MUST specify which bar: B^ord, B^Sigma, or B^Lie.
- **AP103**: Cotriple bar (monadic, always defined) != operadic bar (P^i-coalgebra, Koszul locus).
- **AP104**: E_1/ordered is PRIMITIVE; modular/symmetric is av-image. NEVER present ordered as "auxiliary." (Particularly relevant for Vol III CY/DT structures where the CoHA is naturally E_1.)

## Anti-Patterns AP105-AP115 (from 2026-04-08 architectural convergence)

- **AP105**: Heisenberg = abelian KM at level k = boundary algebra of abelian U(1) CS. Same algebra: OPE J(z)J(w) ~ k/(z-w)^2 (double pole), lambda-bracket {J_lambda J} = k*lambda. NEVER treat "abelian CS boundary" as different from Heisenberg.
- **AP106**: NEVER open a chapter with "This chapter constructs/proves/studies..." The opening states the PROBLEM. CG deficiency opening replaces meta-expository announcement.
- **AP107**: r^coll(z) (bar collision residue) != r(z) (Laplace transform of lambda-bracket). Coincide for even E-infinity algebras; diverge for odd generators.
- **AP108**: Heisenberg is the CG OPENING, NOT the atom of E_1 theory. The atom is a nonlocal chiral algebra (Yangian, EK quantum VA).
- **AP109**: NEVER list results before proving them. Let theorems appear when the mathematics demands them.
- **AP110**: Each volume's preface tells its OWN story. Cross-volume connections go in delineated subsections.
- **AP111**: NEVER create "What this chapter proves" blocks. Restructure the chapter if clarity is needed.
- **AP112**: NEVER trust page counts from memory files without a fresh build.
- **AP113**: In multi-kappa contexts (CY threefolds), bare "kappa" is FORBIDDEN. ALWAYS subscript: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber. (CRITICAL for Vol III: kappa(K3 x E) = 3 vs 5 contradiction arose from missing subscripts.)
- **AP114**: Stub chapters (<50 lines, no theorems) create false coverage. Comment out \\include or develop. (CRITICAL for Vol III: 12 skeletal stub chapters found 2026-04-08.)
- **AP115**: Architectural commitments in CLAUDE.md MUST be enacted in .tex source. The metadata-source gap is the most dangerous anti-pattern.

**Meta^6-rule (from AP106-AP115):** the same error can recur at the EXPOSITORY-ARCHITECTURAL level. AP106-AP115 catch errors in the PROSE LAYER: narration vs construction (AP106), collision vs Laplace r-matrix (AP107), CG opening vs atom (AP108), previews (AP109), cross-volume narration (AP110), result-listing blocks (AP111), stale page counts (AP112), kappa polysemy (AP113, CRITICAL for Vol III), stub chapters (AP114, CRITICAL for Vol III), metadata-source gap (AP115). The deepest errors are in the INTERFACE BETWEEN ARCHITECTURAL INTENT AND TEXTUAL REALITY.

## Agent Anti-Patterns (AAP1-AAP18)

Cross-volume agent workflow anti-patterns. See Vol I CLAUDE.md for full descriptions. Summary: AAP1 (tool-markup leak), AAP2 (fragmented renames), AAP3 (formula duplication), AAP4 (proof after conjecture), AAP5 (artifact noise), AAP6 (status oscillation), AAP7 (intra-file inconsistency), AAP8 (README drift), AAP9 (premature relaunch -> cascading rate limits), AAP10 (engine without test file), AAP11 (test expectations encode AP10), AAP12 (asymptotic tolerance too tight), AAP13 (silent model downgrade without testing), AAP14 (worktree branch collisions), AAP15 (parallel pdflatex SIGKILL races), AAP16 (git stash FORBIDDEN), AAP17 (truncated agent reports: verify via diff), AAP18 (confabulating operadic theory: compute or cite).

## The Dual Imperative

Maximalist ambition synergizes with maximal truth-seeking. Precision enables ambition. When claims outrun proofs, strengthen the proof first.

## The Epistemic Hierarchy

Trust these sources in this order. When they conflict, the higher-ranked source wins:

1. **Direct computation** -- symbolic verification via compute/ modules, dimensional analysis, limiting cases
2. **The .tex source itself** -- the actual theorem statement and proof text, read in full with +/-100 lines of context
3. **The build system** -- compiler errors, undefined references, test failures
4. **Published literature** -- original papers with verified arXiv/DOI identifiers
5. **concordance.tex** (Vol I) -- the constitution, but verify its claims against 1-4
6. **This file (CLAUDE.md)** -- operational instructions; mathematical claims may lag behind source
7. **Memory files** -- historical context; may be stale; always verify before acting on

## Beilinson Rectification Loop -- Chapter-Level Protocol

When instructed to "run the Beilinson loop on [TARGET]" (where TARGET is a chapter .tex path), execute the following **convergent iterative loop**. The loop has three stages per iteration and repeats until convergence (Stage 3 audit returns zero actionable findings).

### ITERATION N (repeat until convergence)

**Stage 1: DEEP BEILINSON AUDIT** (read-only, adversarial, parallel, falsification-maximizing)

Launch THREE parallel Agent tool calls:
- RED audit: deep falsification of every mathematical claim
- BLUE audit: staleness + consistency check against Vols I-II
- GREEN audit: completeness + frontier gap analysis

All three run in background. Merge findings into a FINDINGS REGISTER with deduplication. Classify each: (A) logical/circular, (B) formula, (C) structural, (D) status, (E) editorial. Severity: CRITICAL > SERIOUS > MODERATE > MINOR.

**Stage 2: ADVANCE** (rewrite, rescaffold, close gaps)

Stage 2a: SURGICAL FIXES (build-gated). For each finding from Stage 1 with severity >= MODERATE, in dependency order: read, compute independently, apply minimal fix, grep both ~/chiral-bar-cobar AND ~/chiral-bar-cobar-vol2 AND ~/calabi-yau-quantum-groups for all variant forms (AP5), fix all instances. Build gate: after every 3 fixes, run `make fast`.

Stage 2b: RECONSTITUTE + ADVANCE. Against the Chriss-Ginzburg standard: every object earns its place, every paragraph forces the next, scope is honest. Close gaps, prove unproved lemmas, upgrade conjectures where the proof exists.

**Stage 3: RE-AUDIT** (adversarial verification of what was just written)

Launch THREE parallel Agent tool calls: RED re-audit, BLUE re-audit, GREEN re-audit. Convergence test: if ALL THREE report zero actionable findings at severity >= MODERATE, proceed to FINALIZE. Otherwise, findings become input to next iteration.

**FINALIZE**: Build all three volumes. Run full tests. Grep for new AP violations. Update concordance if theorem status changed.

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol III
cd ~/chiral-bar-cobar && make fast                                # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Vol III tests
```

Same engine as Volumes I-II: memoir, EB Garamond, newtxmath, thmtools, microtype.

**CAUTION**: Watcher spawns competing pdflatex; always kill before builds.

## Session Entry

1. Read this file -- especially the Beilinson Principle, AP-CY1 through AP-CY8, and AP113/AP114
2. Build: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`
3. Run tests: `make test`
4. `git log --oneline -10` for recent context
5. Read relevant .tex source before any edit -- never write from memory or description
6. After each change: build + test. After each correction: grep all three volumes for variants (AP5)
7. Never guess a formula -- compute it or cite it
8. At session end: build all three volumes, run tests, summarize errors found by class

## Critical Pitfalls -- MEMORIZE THESE

**Five objects that must never be conflated (inherited from Vol I):**
- A: the algebra. B(A): the bar coalgebra. A^i = H*(B(A)): the dual coalgebra. A^! = (A^i)^v: the dual algebra.
- Omega(B(A)) = A (bar-cobar INVERSION, not duality). A^! is obtained by VERDIER/LINEAR duality, not cobar.
- Z^der_ch(A) = H*(C^bullet_ch(A,A), delta): the chiral derived center (UNIVERSAL BULK). This is NOT the bar complex.

**Vol III-specific pitfalls:**
- CY-A at d=2: PROVED. CY-A at d=3: PROGRAMME. NEVER write "CY-A is proved" without specifying d.
- CY-C is a CONJECTURE. NEVER use \\begin{theorem} for CY-C. (AP40)
- kappa in Vol III MUST carry a subscript: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber. (AP113)
- The CoHA is an associative algebra. It is NOT a chiral algebra. It is the TARGET that the E_1-sector of the conjectural G(X) should match. (AP-CY7)
- A_X for CY3 does NOT exist as a defined object. It is the content of the d=3 programme. (AP-CY6)
- G(X) ("quantum vertex chiral group") is used but NOT defined. This is AP43. (AP-CY7)
- The Borcherds denominator identity = bar Euler product identification requires the CY-to-chiral functor to exist. For K3 x E (d=3), this is an observation, not a theorem. (AP-CY8)
- 12 stub chapters exist. Do not cite theorems from them. (AP114)

**Grading**: COHOMOLOGICAL (|d|=+1). Bar uses DESUSPENSION.
**Koszul duality**: Com^! = Lie (NOT coLie). Chiral Koszulness != classical Koszulness.
**E_2 != commutative**: E_2-algebras have a braiding but it is NOT symmetric in general. (AP-CY3)

## The Symphonic Standard (PERMANENT)

**The monograph must move like the greatest symphony the world has ever known.** Every sentence carries mathematical weight. Every construction is inevitable. Every theorem earns its place by solving a problem the reader already feels. This standard applies to ALL writing: manuscript, standalone papers, working notes, concordance, preface, introduction, appendices. No exceptions.

### The Voices and What They Demand

**Gelfand** (functorial inevitability): Every definition is a theorem in disguise. The right level of generality is natural, not maximal. Constructions have a "could not be otherwise" quality.

**Beilinson** (falsification and depth): No false ideas survive. Sparse, surgical prose. The epistemic hierarchy is always visible.

**Drinfeld** (deformation-theoretic soul): Quantum groups emerge from geometry. The R-matrix is a shadow of the MC element. Every construction has a deformation-theoretic origin.

**Kazhdan** (D-modules as language): The correct categorical framework is substance, not decoration. No shortcuts in geometric arguments.

**Etingof** (crystal clarity): Every fact earns its keep through computation. A graduate student can follow the argument on first reading.

**Nekrasov** (partition functions as algebra): The generating function IS the mathematical object. No gap between physics and mathematics.

**Polyakov** (the functional integral is real): The OPE is a consequence of locality. Physical reasoning is the deepest layer.

**Kapranov** (higher categories as substance): Operads have geometric content. Categorical structures solve problems, never invoked for their own sake.

**Ginzburg** (the Chriss-Ginzburg standard): Every object solves a problem. Every paragraph forces the next. No dead weight. The architecture of text mirrors mathematics.

**Costello** (factorization algebras as rigorous physics): Perturbative QFT is a theorem. The physical story comes first, then framework, then results.

**Gaiotto** (dualities as tools): Dualities compute invariants. Worked examples are where the theory proves itself.

**Witten** (physical insight precedes proof): The deep structure is geometric. The introduction states what is true in three pages, not thirty. No hedging.

### Prose Laws (apply to ALL writing in the programme)

1. **No AI slop.** Zero tolerance for: "notably", "crucially", "remarkably", "it is worth noting", "interestingly", "this is particularly significant." Delete them.
2. **No hedging where the mathematics is clear.** Proved -> state it. Open -> state it. No "we believe that" when the status is known.
3. **No em dashes for subordinate clauses.** Use colons, semicolons, or separate sentences.
4. **No passive voice hedging.** "It can be shown that" -> state the theorem.
5. **Every paragraph forces the next.** Momentum from mathematical necessity.
6. **State once, prove once, use everywhere.** No duplication.
7. **Every chapter opens with the problem it solves.** Not "In this chapter we study..." (AP106)
8. **Scope is always explicit.** "For all" specifies the universe. "Proved" specifies hypotheses.
9. **The physical and mathematical are unified.** Not separate sections but woven together.
10. **Comparison with prior work is surgical.** One sentence per paper.

## LaTeX Rules

- All macros in main.tex preamble -- NEVER \newcommand in chapter files (use \providecommand)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic, \ClaimStatusOpen
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref.
- Do not add packages without checking preamble compatibility
- Do not create new .tex files when content belongs in existing chapter

## What NOT To Do

- Do not write "kappa" without a subscript in any CY threefold context (AP113)
- Do not cite theorems from stub chapters (AP114)
- Do not use \\begin{theorem} for CY-C or any conjectural claim (AP40)
- Do not write "A_X for CY3" as if it is a defined object (AP-CY6)
- Do not write "the CoHA is the E_1-chiral algebra" (AP-CY7)
- Do not confuse CY dimension d with complex dimension n (AP-CY1)
- Do not paste formulas from Vol I or Vol II without convention conversion (AP49)
- Do not add packages without checking preamble compatibility
- Do not create new .tex files when content belongs in existing chapter

## Git -- HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.
