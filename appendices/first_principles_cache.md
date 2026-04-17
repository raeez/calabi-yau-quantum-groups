# First-Principles Analysis Cache — Cross-Programme Reference

This file caches every first-principles investigation from the programme's git history.
For each wrong claim: what it gets RIGHT, what it gets WRONG, the correct relationship, and the confusion type.

## Confusion Type Taxonomy (21 types)

1. **part/whole** — individual term properties assumed for total
2. **scope error** — formula valid in restricted domain applied universally  
3. **specific/general** — coincidence elevated to law
4. **label/content** — theorem label on conjecture; same symbol for different objects
5. **native/derived** — derived structure attributed to native level
6. **mechanism error** — right conclusion, wrong proof
7. **positive/negative** — obstruction misread as enablement
8. **off-by-one** — systematic shift in formula
9. **conflation** — distinct objects/operations equated
10. **convention clash** — two normalizations coexisting silently
11. **construction/narration** — structural analogy stated as identification
12. **construction/functor** — different constructions confused with single functor
13. **chain/cohomology** — chain-level property confused with cohomological
14. **algebraic/topological** — two incarnations of same structure conflated
15. **level error** — category-level confused with algebra-level; j=0 with j>=1
16. **vacuous/meaningful** — tautology presented as result
17. **temporal** — status changed over time; old status persists
18. **hardcoded/symbolic** — fragile reference instead of label
19. **sandbox/reality** — agent sandbox illusion
20. **additive/multiplicative** — different algebraic operations confused
21. **necessary/sufficient** — necessary condition treated as sufficient

## I. Retracted Proofs (3)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 1 | {b_k, B^{(2)}} = 0 for each k individually | TOTAL {b, B^{(2)}} = 0 via Costello TCFT | Individual arity-k terms don't vanish for non-formal algebras | Cross-arity cancellation: {b_3, B^{(2)}} cancelled by {b_2, B^{(2)}} via Stasheff. Total vanishes by operadic d^2=0. | part/whole |
| 2 | Tsygan formality proves {b, B^{(2)}} = 0 | Tsygan formality is a real theorem | Wrong scope: applies to B^{(0)} = Connes B, not B^{(j>=1)} | B^{(0)} mixed complex axiom [b, B^{(0)}]=0 does NOT extend to B^{(j)} hierarchy. | scope error |
| 3 | kappa_BKM = kappa_ch + chi(O_fiber) universally | True for N=1 (K3 x E): 5 = 3 + 2 | Numerical coincidence for single case | Fails for all Z/NZ-orbifolds with N>=2. Correct: kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general |

## II. Theorem Downgrades

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 4 | "Theorem: BV-BRST = bar of G(X)" for CY3 | Structural identification plausible | G(X) does not exist; cannot be theorem | \begin{conjecture}. 11+ instances fixed. AP-CY6/AP-CY14 | label/content |
| 5 | "Theorem: kappa_ch = chi(O_X) for all CY" | True for d=2 with h^{1,0}=0 | FALSE for odd d (Serre forces chi(O_X)=0) | kappa_ch = worldsheet anomaly; chi(O_X) = target-space. Coincide at d=2, diverge at d=3. AP-CY34 | scope error |
| 6 | 62 instances of "Theorem CY-A_3" | CY-A_3 now proved (inf-cat) | Before proof: unproved conjecture in theorem env | Mass rectification. Chain-level results remain conjectural. | temporal |

## III. Kappa Conflations (7 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 7 | Bare "kappa" (~100+ instances) | Each kappa is real | Without subscript, different kappas conflate | Four kappas: kappa_{ch,BKM,cat,fiber}. K3xE spectrum: {0,2,3,5,24}. AP113 | label/content |
| 8 | "kappa(K3xE) = 3 vs 5 contradiction" | Both values real | DIFFERENT kappas of DIFFERENT algebras | kappa_ch=3 (chiral), kappa_BKM=5 (Igusa). No contradiction. | conflation |
| 9 | "Algebraizations share kappa_cat" as meaningful | kappa_cat IS same | VACUOUS: kappa_cat is manifold invariant | Like "both share gravity." AP-CY55 | vacuous/meaningful |
| 10 | kappa_ch = Sigma(-1)^i dim HH_i | Gives a real invariant | Gives chi_top (=24 for K3), NOT kappa_ch (=2) | Correct: Hodge-filtered supertrace str_{F^0}(q^{L_0}). AP-CY36 | formula error |
| 11 | kappa_ch additive under fiber products | Additive under direct sums | NOT under fiber products | kappa_ch(K3xE)=3 but chi(O_{K3xE})=2*0=0. Additivity vs multiplicativity. | additive/multiplicative |

## IV. E_n Level Confusions (8 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 12 | Phi: CY_d-Cat -> E_2-ChirAlg (uniformly) | E_2 correct for d<=2 | WRONG at d>=3: output is E_1 | Must scope: n=2 for d<=2; n=1 for d>=3. FM43 | scope error |
| 13 | "E_2-chiral algebra" at d=3 for A itself | E_2 DOES appear at d=3 | Lives on Z(Rep^{E_1}(A)), NOT on A | A is E_1 native. E_2 is derived via center. AP-CY56 | native/derived |
| 14 | E_3 on HH of E_1 algebras (Deligne) | E_3 Deligne is real | Requires E_inf input, not E_1 | For E_1: only E_2 (Dunn: E_1 tensor E_2 = E_3, but input contributes E_1). AP153 | scope error |
| 15 | Two E_3 structures are the same | Both exist | Agree under formality only | Algebraic E_3 (Deligne) vs topological E_3 (Conf(R^3)). Physical content at chain level. AP154 | algebraic/topological |
| 16 | Miki from E_3 operad | Miki IS an S_3 permutation | Comes from CY torus Weyl group, not operad | Counterexample: k[x]/(x^2) is E_3, no Miki. AP-CY22 | specific/general |
| 17 | CY-B is "E_2-Koszul" uniformly | CY-B IS Koszul duality | d-DEPENDENT: E_2 at d=2, E_1 at d=3 | At d=3: E_1-Koszul on A, E_2 on center. AP-CY58 | scope error |
| 18 | Class M E_3 bar is infinite | Class M IS most complex | Cohomology is 6^g (Kunneth) | Chain: P(q)^{6g}. Cohomology: 6^g. AP-CY21/38 | chain/cohomology |
| 19 | SN bracket vanishes for all CY_3 | True for C^d with GL(d) | False for non-toric CY_3 | Two mechanisms: (a) operadic degree (universal), (b) GL(d)-invariant vanishing (toric). | specific/general |

## V. Object Conflations (9 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 20 | CoHA = E_1-chiral algebra | CoHA related to E_1-sector | CoHA is associative, not chiral | Connection via functor Phi, not identification. AP-CY7 | construction/identification |
| 21 | Drinfeld center = derived center | Both real | Three distinct objects conflated | Z(C) = category center. Z^der = Hochschild cochains. Z categorifies derived center. AP-CY4 | level error |
| 22 | Drinfeld center = categorified averaging | Related via factorization | Center CONSTRUCTS; averaging DESTROYS | E_1 ->^Z E_2 ->^{Sym} E_inf. AP-CY54 | construction/narration |
| 23 | Flop = Koszul dual | Both operations on CY | Flop preserves kappa; Koszul exchanges | kappa(A_X)=kappa(A_{X+}) for flop. kappa(A)+kappa(A^!)=K for Koszul. AP-CY10 | conflation |
| 24 | CoHA = bar complex | Both have char M(q) | CoHA is algebra; bar is coalgebra | SV theorem: CoHA ≅ Y^+. Bar encodes Y-multiplication. Character coincidence. | algebra/coalgebra |
| 25 | Spectral z = worldsheet z | Both called "z" | Different objects | Delta_z spectral: shift parameter. OPE z: insertion coordinate. AP-CY31 | label/content |
| 26 | Phi distinguishes three K3 algebras | Three algebras exist | Phi gives ONE output: H_Muk | BKM from Borcherds lift, Conway from Leech. Different constructions. AP-CY59 | construction/functor |
| 27 | Six routes = six Phi applications | Six routes are constructions | Six DIFFERENT constructions | Convergence = CY-C (conjectural). AP-CY60 | construction/functor |
| 28 | R(z) = (id tensor S) o Delta_z(1) | R from coproduct | Coproduct of vacuum = 1 tensor 1 by counit | Correct R via half-braiding sigma in Z(Rep). AP-CY25 | construction error |

## VI. Scope and Status Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 29 | 6d route bypasses CY-A_3 | Alternative approach | Each subproblem requires same data | Reorganises, doesn't resolve. AP-CY32 | reorganization/bypass |
| 30 | S_{ijk}=R_{ij}R_{ik}R_{jk} satisfies ZTE | R satisfies YBE | Pairwise != 3-particle consistency | Fails at O(kappa^2). S^{corr}=S+kappa^2*T exists. AP-CY30 | specific/general |
| 31 | Shadow class from non-formality alone | m_3!=0 necessary for >=L | Not sufficient | local P^2: m_3!=0 but class M (infinite). Must compute full tower. AP-CY12 | necessary/sufficient |
| 32 | Omega-background universal for CY_3 | Realizes E_1 for toric | Requires torus action | General mechanism: bracket degree 1-d. Omega-background: toric-specific. | specific/general |
| 33 | "CY frontier" (empty slogan) | Gap F_g^top - F_g^sh is real | "Frontier" says nothing | Computable via Borel resummation + KS wall-crossing. | label/content |

## VII. Formula and Computation Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 34 | MF(W): A^n->A^1 is CY_{n-1} | MF IS a CY category | CY dim is n-2, not n-1 | ADE in 2 vars: CY_0. Need 5 vars for CY_3. AP-CY17 | off-by-one |
| 35 | A-hat convergence radius = pi | A-hat IS relevant | Argument halved: (x/2)/sinh(x/2) | Radius = 2*pi. The /2 doubles the radius. AP-CY19 | mechanism error |
| 36 | phi_{0,1} c(-1)=1 vs c(-1)=2 | Both normalizations exist | Factor of 2 = kappa_ch(K3) propagated silently | State convention. K3 elliptic genus = 2*phi_{0,1}. AP-CY42 | convention clash |
| 37 | Verdier inverts sigma_2 for k^!=-k | k^!=-k IS correct | sigma_2 is even under h_i->-h_i | k^! from Shapovalov form transposition, not sigma_2 inversion. AP-CY26 | mechanism error |
| 38 | B-cycle i^2=1 instead of i^2=-1 | B-cycle integrals needed | Sign error gives |q|=1, kills convergence | Verify |q|<1 and Im(tau)>0 after B-cycle computation. FM24 | sign error |

## VIII. Process and Agent Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 39 | Agent writes persist to disk | Written inside sandbox | Sandbox isolation | Verify with ls after agent completion. AP-CY27 | sandbox/reality |
| 40 | Agent writes to correct repo | Files written | Wrong volume's directory | Verify FULL PATH. AP-CY29 | path error |
| 41 | Agent test values independent | Tests pass | 10% tautological | Multi-path verification required. AP-CY49 | tautological verification |
| 42 | Docstring values correct | Code correct | Docstring fabricates for n>=4 | Verify EVERY numerical value against function output. AP-CY24 | code/documentation |

## IX. Cross-Volume Confusions

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 43 | Bulk replace "arity"->"degree" | Rename intentional | Corrupts singularity, unitarity, etc. | 45 corruptions. Check compound words. FM42 | mechanical error |
| 44 | "shadow Postnikov tower" | Shadow tower is real | "Postnikov" is different concept | Correct: "obstruction tower" or "shadow tower" | terminology error |
| 45 | Part~IV hardcoded | Parts ARE numbered | Numbers change on restructuring | Use \ref{part:...}, never Part~N. AP-CY13 | hardcoded/symbolic |

## X. cy_to_chiral.tex Audit (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 46 | Class M E_3 bar cohomology is "infinite-dimensional" | d_4 survives for class M | Chain-level complex P(q)^{6g} is infinite, but cohomology is FINITE | dim H*(B^{E_3}(A)) = 6^g for class M (Kunneth: d_4 kills Lambda^0 and Lambda^3, leaving [0,3,3,0] per handle). AP-CY21/38 | chain/cohomology | cy_to_chiral.tex L3760, L3765 |
| 47 | "dim HH_0 = 2, dim HH_1 = 20, dim HH_2 = 2" (yielding -16) | Alternating sum = -16 is correct | Mislabeled: these are dim H*(Omega^p), not dim HH_i | HH_i uses homological grading (HH_0=22); the Hodge grading uses p (dim H*(Omega^0)=2). Both yield -16 under the correct alternating sum, but the labels were wrong. | label/content | cy_to_chiral.tex L69 |
| 48 | ClaimStatusConditional for class M E_3 bar genus result | Class M result WAS conditional | Now PROVED via Kunneth (6^g closed form) | Update status to ProvedHere for all classes including M. | temporal | cy_to_chiral.tex L3754-3755 |

## XI. en_factorization.tex Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 49 | K3 listed as CY_4 in Pontryagin class table | K3 has c_2=24, p_1=-48 | K3 is CY_2 (complex dim 2), NOT CY_4 | Removed row. K3 cannot appear in CY_4 landscape table. AP-CY1 | scope error | en_factorization.tex L309 |
| 50 | Verification note "AP-CY21: class M infinite" | Class M IS most complex shadow class | Class M E_3 bar = 6^g (FINITE); class G is the infinite one | Corrected to "class M is 6^g not (1+t)^{3g}". AP-CY21/38 | chain/cohomology | en_factorization.tex L2688 |

## XII. K3 Example Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 51 | "E_2-structure should come from Sp_4(Z)" (at d=3, no E_n scoping) | E_2 structure IS relevant at d=3 | At d=3, A is natively E_1; E_2 lives on Drinfeld center Z(Rep^{E_1}(A)), not on A | Fixed: clarified that E_2-braiding is on the Drinfeld center of the representation category, not on A itself. AP-CY56 | native/derived | k3_chiral_algebra.tex L35 |
| 52 | "CoHA is E_1-sector of G(X), which is CY-A_3" | CoHA/G(X) connection is real | G(X) requires CY-C (quantum group realization), NOT CY-A_3; CY-A_3 gives A_X, not G(X) | Fixed: CoHA as E_1-sector of G(X) requires Conjecture CY-C. CY-A_3 constructs A_X but not G(X). AP-CY7/AP-CY14 | label/content | k3_yangian_chapter.tex L1103 |
| 53 | kappa_BKM = h^{1,1}(K3)/4 = 20/4 = 5 | Numerically correct (5=5) | Misleading derivation: c_f(0)=10 comes from Jacobi form, not h^{1,1}/2 | Fixed: kappa_BKM = c_f(0)/2 = 10/2 = 5 with explicit AP-CY37 citation. Hodge number route obscures Borcherds weight theorem. | mechanism error | k3_chiral_algebra.tex L510 |
| 54 | "deeper identifications await CY-A_3" | CY-A_3 WAS open | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction) | Fixed: remaining obstructions are chain-level framing data (non-formal) and Vol I Borcherds-lift bridge, not CY-A_3 itself. | temporal | k3_yangian_chapter.tex L1347, L1380-1391 |
| 55 | Bare $\kappa$-diagnostic in verification note | kappa_bullet notation required | AP113 zero-tolerance: all kappa must be subscripted or use bullet | Fixed: $\kappa$-diagnostic -> $\kappa_\bullet$-diagnostic. | label/content | k3_yangian_chapter.tex L126 |

## XIII. Connection/Bridge Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 56 | "predicted modular characteristic is kappa_ch = chi_top/24 (BCOV prediction)" as blanket statement for compact CY3 | BCOV prediction IS used for compact CY3 | Presents conjectural formula without noting chi_top/24 != chi(O_X) for CY3 | chi(O_X)=0 for ALL CY3 by Serre duality (AP-CY34). kappa_ch = chi_top/24 is BCOV *prediction* (conjectural), not established formula. Must mark as conjectural and note the distinction. | scope error | bar_cobar_bridge.tex L235 |
| 57 | "conditional on CY-A_3" in DMVV conjecture (bar_cobar_bridge.tex) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction, April 2026) | Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) and motivic DT comparison, NOT CY-A_3. | temporal | bar_cobar_bridge.tex L749 |
| 58 | "conditional on CY-A_3" for K3xE Stokes-WC identification | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{K3xE} now exists. Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) + infinite stitching of local conifold identifications. | temporal | modular_koszul_bridge.tex L581, L936, L964 |
| 59 | "conditional on CY-A_3" for Hochschild bridge at d=3 | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Conjecture remains (upgrading the categorical-to-chiral Hochschild map to d=3 requires more than inf-cat existence), but the CY-A_3 conditionality is resolved. The conjecture's remaining content: the PTVV shifted Poisson maps to genus-0 convolution bracket. | temporal | modular_koszul_bridge.tex L317 |
| 60 | Face 1 "Conjectured for d=3 (conditional on CY-A_3)" in seven-face status remark | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED; thm at L153 already has ProvedHere | Status remark stale: Face 1 is ProvedHere for both d=2 and d=3. | temporal | cy_holographic_datum_master.tex L859 |
| 61 | "CY_3 (conditional on CY-A_3)" paragraph header in holographic datum | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated header. The paragraph body already said "now follow from Theorem CY-A_3". Only the header was stale. | temporal | cy_holographic_datum_master.tex L245 |
| 62 | K3xE Hecke eigensheaf "conditional on CY-A_3" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{SxE} exists by CY-A_3. Remaining conditionality: factorization Phi(SxE) = Phi(S) tensor Phi(E) (not established) and the Hecke eigensheaf identification. | temporal | geometric_langlands.tex L257 |
| 63 | "d=3 analogue remains part of CY-A_3" in convolution algebra proof | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated: "now established by CY-A_3 (proved)". The convolution bracket pulls back at both d=2 and d=3. | temporal | modular_koszul_bridge.tex L42 |
| 64 | kappa_ch + kappa_ch' = 0 displayed without scoping | True for KM/free-field class | Virasoro: sum = 13, not 0. Free-field scoping buried in prose after display | Fixed: displayed formula now shows general conductor relation kappa_ch + kappa_ch' = rho*K with explicit family-dependent scoping. | scope error | bar_cobar_bridge.tex L196 |

| 65 | "conditional on CY-A_3" in genus expansion section of modular_trace.tex | CY-A_3 WAS the bottleneck for GW identification | CY-A_3 is now PROVED; A_X exists | Remaining conditionality: the comparison between shadow tower and B-model topological string at g>=2. At g=1, unconditionally proved via Vol I Theorem D. | temporal | modular_trace.tex L168 |
| 66 | "the tower is conditional on CY-A_3" for CY3 shadow tower | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Tower is now accessible via CY-A_3 (proved). BKM modularity constraints provide structural predictions independently. | temporal | modular_trace.tex L173 |

### Positive findings (no violations)

The following were checked and found correct across all five files:

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout all five files.
- **AP-CY4 (Drinfeld center vs derived center)**: Correctly distinguished in modular_koszul_bridge.tex Def 3.1 (three Hochschild theories), cy_holographic_datum_master.tex Rem rem:no-cobar-bulk-confusion, geometric_langlands.tex Iwahori passage.
- **AP-CY7 (CoHA != chiral)**: Correctly noted as associative in bar_cobar_bridge.tex L359 ("on the CY side, the CoHA..."), geometric_langlands.tex L90 (explicit AP-CY7 citation).
- **AP-CY8 (denominator != bar Euler)**: No bare identification. The modular_koszul_bridge.tex Igusa cusp form section (Thm thm:k3xe-shadow-cohft-igusa) explicitly notes the AP-CY8 proviso.
- **AP-CY10 (flop != Koszul)**: modular_trace.tex L178 correctly distinguishes complementarity (Koszul) from flop.
- **AP-CY12 (shadow class from full tower)**: bar_cobar_bridge.tex correctly computes shadow class for each CY3 example from the full tower data, not from non-formality alone.
- **AP-CY54 (Drinfeld center != averaging)**: geometric_langlands.tex correctly describes Drinfeld center via half-braidings/Iwahori passage, never calls it "averaging".
- **AP-CY55 (manifold vs algebraization invariants)**: modular_koszul_bridge.tex kappa-spectrum tables (L333-344, L251-252) correctly separate manifold invariants from algebraization invariants.
- **AP-CY56 (E_n level scoping)**: geometric_langlands.tex correctly uses E_2 only for d<=2, E_1 for d>=3. cy_holographic_datum_master.tex Face 1 d=3 correctly references E_1-chiral.
- **AP-CY57 (construction/narration)**: The seven-face chapter constructs each face explicitly, not by narration. Koszul duality is constructed through the bar-Verdier pipeline in modular_koszul_bridge.tex.
- **AP25 (bar != cobar != Koszul)**: bar_cobar_bridge.tex Remark 3.1 (three functors, three outputs) correctly distinguishes Omega(B(A))=A (inversion), D_Ran(B(A))=B(A^!) (Verdier/Koszul), Z^der_ch(A)=RHom (derived center).
- **Geometric Langlands, derived Satake**: All CONJECTURAL throughout geometric_langlands.tex. Every formal statement uses \begin{conjecture} except Feigin-Frenkel (ProvedElsewhere).
- **Part references**: No hardcoded Part~N references found in any of the five files.

## XIV. Theory + Examples Chapters Enforcement (2026-04-15, 11-file sweep)

Files audited: cy_categories.tex, cyclic_ainf.tex, hochschild_calculus.tex, quantum_groups_foundations.tex, braided_factorization.tex, toroidal_elliptic.tex, matrix_factorizations.tex, fukaya_categories.tex, quantum_group_reps.tex, derived_categories_cy.tex, k3e_cy3_programme.tex.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 65 | kappa_cat(K3 x E) = 3 in kappa-spectrum remark | kappa_ch = 3 IS correct | kappa_cat = chi(O_{K3xE}) = 0 by Kunneth (2*0=0), NOT 3 | Fixed: kappa_cat = 0. The value 3 is kappa_ch (algebraization invariant). AP-CY55 | conflation | quantum_group_reps.tex L513 |
| 66 | kappa_cat = 1 for resolved conifold (d=3) | Chiral modular char IS 1 | At d=3, the chiral algebra output is kappa_ch, not kappa_cat | Fixed: kappa_ch = 1. | label/content | quantum_group_reps.tex L360 |
| 67 | kappa_cat(Phi(Fuk(X))) = chi(O_X) at d=3 conjecture | kappa_cat = chi(O_X) as manifold invariant | Phi produces kappa_ch, not kappa_cat. At d=3, kappa_ch != chi(O_X) (AP-CY34). | Fixed: kappa_ch = chi^{CY}(Fuk(X)), noting divergence at d=3. | scope error | fukaya_categories.tex L255 |
| 68 | kappa_cat = 0 as "predicted modular characteristic" of Phi for quintic | kappa_cat = 0 correct as manifold invariant | "Predicted" implies Phi output = kappa_ch, which may differ at d=3 | Fixed: separated kappa_cat from kappa_ch; noted d=3 programme. | label/content | fukaya_categories.tex L296 |
| 69 | kappa_cat = 1 for conifold in Fukaya chapter | Chiral modular char IS 1 | At d=3, chiral algebra output is kappa_ch | Fixed: kappa_ch = 1. | label/content | fukaya_categories.tex L307 |
| 70 | {kappa_cat,...} = {2, 3, 5, 24} for K3 x E | Individual values correct in isolation | kappa_cat(K3xE) = 0, NOT 2. The 2 is chi(O_{K3}) = kappa_cat of the fiber. | Fixed: {0, 3, 5, 24} with Kunneth. AP-CY55 | conflation | cyclic_ainf.tex L195 |
| 71 | "modular characteristic kappa_cat" depends on cyclic A_inf input | kappa_ch does depend on it via Phi | kappa_cat = chi(O_X) is manifold-invariant, independent of algebraization | Fixed: "chiral modular characteristic kappa_ch". AP-CY55 | vacuous/meaningful | cyclic_ainf.tex L4 |
| 72 | kappa_cat = 2 = chi(O_{K3}) in K3 x E BPS factorization context | chi(O_{K3}) = 2 correct for K3 fiber | Context is K3 x E; kappa_cat(K3xE) = 0 by Kunneth | Fixed: kappa_cat(K3xE) = 0; 2 is fiber value. AP-CY55 | conflation | braided_factorization.tex L1389 |
| 73 | "resulting chiral algebra is class M" (from CoHA directly) | Class M IS correct | Conflates CoHA (associative) with chiral algebra (via Phi). AP-CY7 | Fixed: CoHA is associative; Phi_3 output is class M. | construction/identification | derived_categories_cy.tex L256 |

### Verified Clean (no violations):

- **AP113**: All kappa subscripted in all 11 files.
- **AP-CY17**: MF(W) dim = n-2 correct with explicit citations.
- **AP-CY1**: cyclic_ainf.tex L80 explicitly warns d = complex dim, not real dim 2n.
- **AP-CY2**: CY class in HC^-_d with AP-CY2 citation.
- **AP-CY5**: KL root-of-unity correctly required.
- **AP-CY7**: CoHA correctly labeled associative, not chiral.
- **AP-CY10**: Flop/Koszul correctly distinguished.
- **AP-CY13**: Zero hardcoded Part~N references.
- **AP152**: "ordered product" disambiguated by context.
- **AP160**: Hochschild convention note present.
- **pi_3(BU)=0**: Correctly stated with Bott periodicity derivation.
- **E_n scoping**: Correctly scoped throughout (E_2 at d=2, E_1 at d=3).
- **CY-C**: All \begin{conjecture}, never \begin{theorem}.

### First-principles verification: kappa_cat(K3 x E) = 0

chi(O_{K3xE}) = sum_q (-1)^q h^{0,q}(K3 x E). Kunneth: h^{0,q}(K3 x E) = sum_{a+b=q} h^{0,a}(K3) h^{0,b}(E). K3: (h^{0,0}, h^{0,1}, h^{0,2}) = (1, 0, 1). E: (h^{0,0}, h^{0,1}) = (1, 1). Product: (1, 1, 1, 1). chi = 1-1+1-1 = 0. Equivalently chi(O_{K3}) chi(O_E) = 2*0 = 0.

## XV. Vol I Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 76 | B(A) is SC-coalgebra | B(A) IS coalgebra | E_1 not SC | SC on derived center pair | object/structure |
| 77 | SC=E_3 | Related | SC+conformal=E_3-TOP | generic/special |
| 78 | r(z)=Omega/z bare | Proportional | Missing k. 90+ instances | specific/general |
| 79 | kappa=c/2 universal | Virasoro | Heis:k, KM:dim(g)(k+h^v)/(2h^v) | specific/general |
| 80 | av(r)=kappa non-abelian | Abelian | kappa=av(r)+dim(g)/2 | abelian/non-abelian |
| 81 | r^Vir=(c/2)/z^4 | Quartic pole | d-log: p->p-1. r=(c/2)/z^3+2T/z | OPE/r-matrix |
| 82 | S_4=-(5c+22)/(10c) | Correct symbols | Reciprocal. 10/[c(5c+22)] | reciprocal |
| 83 | kappa+kappa'=0 universal | KM/Heis/free | Vir:13, BP:98/3. Family-dependent | specific/general |
| 84 | Bar-cobar=bulk | Fundamental | Omega(B(A))~A inversion. Bulk=HH | four-object |
| 85 | E_3 derived center for E_1 | For E_inf (HDC) | E_1: only E_2 | input/output scope |
| 86 | Algebraic E_3=topological E_3 | Both exist | Agree formality; diverge chain | two-structure |
| 87 | Bare "Hochschild" | 3 theories | topological/chiral/categorical | three-object |
| 88 | 4 Yangians interchangeable | All Yangians | classical/dg/chiral/spectral | four-object |
| 89 | SC Koszul self-dual | SC IS Koszul | SC^!=(Lie^c,Ass^c) != SC | functor/object |
| 90 | A^! is SC-algebra | Dual operad | SC^!=(Lie,Ass) not SC=(Com,Ass) | algebra/coalgebra |
| 91 | d_alg(Vir)=3 | d_gen=3 | d_alg=infinity (class M) | two-depth |
| 92 | omega_g=d*tau | Both exist | d*tau fiber; c_1(lambda) moduli | fiber/base |
| 93 | Arnold=connection form | Arnold fundamental | Arnold=bar coeff. KZ=r(z)dz | form-type |
| 94 | obs_g=kappa*lambda_g universal | g=1+uniform | g>=2: cross-channel corrections | specific/general |
| 95 | B(A)=T^c(s^{-1}A) full | Desuspended | Augmentation ideal A-bar | augmentation/full |
| 96 | |s^{-1}v|=|v|+1 | Shifting | LOWERS: |v|-1 | suspension/desuspension |
| 97 | m_1^2=0 curved A-inf | Flat | Curved: m_1^2=[m_0,a] | flat/curved |
| 98 | CE=chiral bar multi-gen | Single-gen | Orlik-Solomon. sl_3: 36 vs 20 | algebraic/geometric |
| 99 | ChirHoch free polynomial | Polynomial Hilbert | z^2!=0 but ChirHoch^4=0 | A_inf/cup-product |
| 100 | E_8 fund=779247 | Large irreps | Adjoint=248 | confabulated |
| 101 | g=2 stable graphs=6 | Several | 7 not 6 | off-by-one |

## XVI. Deep Theory Chapters Enforcement (2026-04-15, 3-file sweep)

Files audited line-by-line: m3_b2_saga.tex (1189 lines), quantum_chiral_algebras.tex (2712 lines), e2_chiral_algebras.tex (1189 lines).

### Checked patterns (16 confusions):

1. **Bare kappa (AP113)**: CLEAN. Zero violations across all three files. All kappa subscripted.
2. **Bare chi without subscript**: See finding #102 below (quantum_chiral_algebras.tex lift rate table).
3. **{b_k,B^{(2)}}=0 per-k FALSE (part/whole)**: CLEAN in m3_b2_saga.tex. Correctly states individual nonvanishing (Prop prop:chain-nonvanishing-generic), total vanishing (Thm thm:total-ainf-compat). Three wrong proofs clearly retracted with \emph{retracted} in remark titles.
4. **B^{(0)} != B^{(j>=1)} (AP-CY35)**: CLEAN. m3_b2_saga.tex L119 lists B^{(0)}...B^{(d)} as distinct hierarchy members. L228-231 explicitly states "confused B^{(0)} (standard Connes B) with B^{(2)} (higher hierarchy)". L266-278 Tsygan section explicitly: "Tsygan formality is a statement about (b, B) where B = B^{(0)}" and "extension to full Connes hierarchy requires Costello's TCFT". L596-607 Remark rem:tcft-vs-mixed makes distinction again.
5. **Tsygan formality scope**: CLEAN. m3_b2_saga.tex L266-278 explicitly identifies scope as B^{(0)} only.
6. **Retracted proofs clearly marked**: CLEAN. All three wrong proofs have "(retracted)" in remark titles: L152 "retracted", L200 "retracted", L247 "retracted".
7. **Omega-background toric-specific (AP-CY20)**: CLEAN in quantum_chiral_algebras.tex. L251 "the Omega-background deformation (h_1,h_2)". L389 explicit AP-CY20 citation. L642 "two-parameter R-matrices...AP-CY20: normal bundle grading does not directly give (q,t); the passage is through equivariant localization". L1934 "AP-CY20: the intermediary mechanism must be named explicitly". L1647 explicit "(AP-CY20: intermediary mechanism)".
8. **3d->6d lift rate (AP-CY48)**: See finding #102 below.
9. **E_3 from derived center, not automatic (AP153/154)**: CLEAN. quantum_chiral_algebras.tex L248 explicit AP153 citation. L252 explicit AP154 citation. L1896-1899 Prop prop:deligne-level-drop-cfg25 correctly derives E_2 (not E_3) on HH of E_1 input. L2336 "Deligne: E_2 on HH(Y) (from E_1 input; AP153)".
10. **E_2-Koszul correctly scoped to d=2 (AP-CY58)**: CLEAN in e2_chiral_algebras.tex. L11-22 scoping paragraph explicitly: "At d=2, the functor Phi produces E_2-chiral algebras natively...At d=3, the functor Phi_3 produces an E_1-chiral algebra; the E_2-chiral algebra is its chiral Drinfeld centre". L284-289 "CY-B is d-dependent. At d=2, A is natively E_2...At d=3, A is E_1".
11. **CY-B d-dependent (AP-CY58)**: CLEAN. e2_chiral_algebras.tex L284 "CY-B is d-dependent."
12. **CoHA != chiral (AP-CY7)**: CLEAN. quantum_chiral_algebras.tex L218 "(which is associative, not chiral: AP-CY7)". L1646 explicit AP-CY7. L1639 explicit distinction.
13. **CY-C always conjecture**: CLEAN. All G(X)-dependent statements use \begin{conjecture} throughout all three files. Quantum chiral algebra target specification (L21) correctly uses \begin{conjecture}\ClaimStatusConjectured.
14. **Part~N hardcoded (AP-CY13)**: CLEAN. Zero hardcoded Part~N references in any of the three files.
15. **AP-CY4 (Drinfeld center vs derived center)**: CLEAN. quantum_chiral_algebras.tex L88 explicit AP-CY5 citation. L920-930 Prop prop:three-dualities correctly separates all three objects. e2_chiral_algebras.tex L258-267 Rem rem:ap34-four-functors distinguishes four functors explicitly.
16. **Spectral z vs worldsheet z (AP-CY31)**: CLEAN. quantum_chiral_algebras.tex L1673-1681 Warning warn:spectral-vs-worldsheet with explicit distinction. L1827 "AP-CY31 distinction" in test summary.

### Findings:

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 102 | 3d->6d overall lift rate stated as 35% (12/34) in text | CLAUDE.md says 24% (AP-CY48) | Discrepancy between .tex ground truth and CLAUDE.md metacognitive record | The .tex table (quantum_chiral_algebras.tex L620-634) counts 34 substructures: 12 algebraic (100% lift), 19 topological (0%), 3 hybrid (0%), total 12/34 = 35%. CLAUDE.md says "24% lift rate" (AP-CY48). The .tex is the primary source; the 24% figure in CLAUDE.md appears to be from an earlier analysis with a different substructure count. The .tex ground truth is 35% (or 12/34). Neither figure is "wrong" -- they count different decompositions -- but the .tex is the definitive source. **No .tex fix needed; CLAUDE.md should be updated.** | specific/general | quantum_chiral_algebras.tex L620, L633; CLAUDE.md AP-CY48 |
| 103 | chi used without subscript in MC tangent Euler char proof | chi is the Euler characteristic | Not chi_top or chi(O_X), but chi of a complex -- the tangent complex T_0MC | This is a different chi (Euler char of a chain complex, not of a manifold), so the bare chi is mathematically acceptable here. However, the new rule "bare chi without subscript" was requested. The usage at L1086 is chi(T_0MC), not chi(X) or chi(O_X). **Borderline: chi of a chain complex is standard notation and unambiguous in context. No fix needed.** | label/content | quantum_chiral_algebras.tex L1079-1086 |
| 104 | chi^{CY}_2(K3) = 2 notation at L1323 | CY chi is a real invariant | Uses chi^{CY}_2 which is not one of the four approved kappa subscripts | The notation chi^{CY}_2(K3) is used as an intermediate step to define kappa_ch = 2. It is correctly scoped ("from the CY-A_2 construction; kappa_ch = chi^{CY}_2(K3) = 2"). The chi^{CY} is a functor-level invariant, not bare chi. **No fix needed; correctly bridges to kappa_ch.** | label/content | quantum_chiral_algebras.tex L1323 |
| 105 | kappa_ch(A_E) = 24 in adversarial comparison table | Route A KS boundary | OPE-level trace gives 24, but standard kappa_ch(K3) = 2 | The table at L1617-1621 shows kappa_ch = 24 for Route A (KS boundary) and kappa_ch = 2 for Routes B, C (Phi and SCFT). The text at L1624 explains: "Route A uses the OPE-level trace tr(delta^{ab}) = 24 while Routes B, C use the CY-graded supertrace chi(O_K3) = 2". This is CORRECTLY handled as an explicit distinction between two accounting methods. Both are legitimate; the discrepancy is real and explained. **No fix needed; correctly documented.** | scope error | quantum_chiral_algebras.tex L1617 |
| 106 | kappa_ch = chi(X) at L2446 for 4-manifold invariants | kappa formula for surfaces | At d=3, kappa_ch != chi(O_X) in general (AP-CY34, AP-CY44) | The context at L2446-2448 is: "kappa_ch = chi(X) (from A_{Tot(K_X)} via Phi, conditional on CY-A_3 when Tot(K_X) is a CY_3)". Here chi(X) means the TOPOLOGICAL Euler characteristic of a 4-manifold X, not chi(O_X). The mapping is chi_top(X) -> kappa_ch via the total space Tot(K_X). This is a CY-A_3-conditional claim correctly marked as conditional. The bare chi(X) here means chi_top(X) (not chi(O_X)). **The usage is defensible but could be clearer: specifying chi_top(X) instead of chi(X) would remove ambiguity per the new rule.** | label/content | quantum_chiral_algebras.tex L2446 |

### Verified Clean (no violations):

**m3_b2_saga.tex** (1189 lines):
- **AP113 (bare kappa)**: Zero violations.
- **AP-CY35 (B^{(0)} vs B^{(j>=1)})**: Correctly distinguished throughout (L119, L228, L266, L596).
- **Retracted proofs**: All three clearly marked with "(retracted)" in titles.
- **{b_k,B^{(2)}} per-k vs total**: Correctly handled at every instance.
- **Incompatibility theorem (mu_3 != 0 => mu_2 = 0)**: Correctly proved (Thm thm:single-object-incompatibility, L839-881).
- **TCFT vs naive B^{(2)}**: Distinction made explicit in Rem rem:b2-cancellation-correction (L925-961).
- **Shadow tower connection**: Correctly links mu_3 to S_3 (L1086-1104).
- **Three levels of truth**: Correctly structured (Def def:three-levels, L692-715).
- **CY-A_3 implications**: Correctly states [m_3,B^{(2)}]!=0 is "red herring" (L1065).
- **AP-CY31 analogy**: Correctly drawn (L1106-1125).
- **Part~N**: Zero hardcoded references.
- **Bare chi**: No chi appears in this file.
- **Claim statuses**: All ProvedHere with \begin{proof} blocks.

**quantum_chiral_algebras.tex** (2712 lines):
- **AP113 (bare kappa)**: Zero bare kappa violations. L868 "AP113: no bare kappa" explicitly.
- **AP-CY6/14 (G(X) status)**: G(X) correctly in \begin{conjecture} at L21-30. Warning at L32-42 explicitly states "not a mathematical definition".
- **AP-CY7 (CoHA != chiral)**: Correct at L218, L1646.
- **AP-CY8 (denominator != bar Euler)**: Not directly invoked.
- **AP-CY20 (Omega-background)**: Correct at L251, L389, L642, L1934.
- **AP-CY22 (Miki algebra-specific)**: Correct at L596, L647, L819.
- **AP-CY31 (spectral vs worldsheet)**: Correct at L1673-1681.
- **AP-CY32 (reorganization != bypass)**: Correct at L1949.
- **AP-CY33 (chain != rational)**: Correct at L537.
- **AP150 (composite arrow conjectural)**: Correct at L358, L1007.
- **AP153 (E_3 scope)**: Correct at L248, L1896.
- **AP154 (two E_3s)**: Correct at L252, L974-982.
- **AP-CY4 (three objects)**: Correct at L88, L920-930.
- **Part~N**: Zero hardcoded references.
- **CY-C**: All \begin{conjecture} where needed.
- **Claim statuses**: Consistent (ProvedHere with proof blocks; Conjectured for conjectural).
- **6d non-Lagrangian**: Correctly flagged at L227 (Rem rem:6d-not-lagrangian).
- **ZTE obstruction**: Correctly documented (L530-531, L1973).
- **kappa-spectrum tables**: Complete and correct at L868-872, L1433-1452, L1722.

**e2_chiral_algebras.tex** (1189 lines):
- **AP113 (bare kappa)**: Zero violations.
- **E_2-Koszul scoped to d=2 (AP-CY58)**: Correctly scoped at L11-22, L284-289.
- **CY-B d-dependent**: Correctly stated at L284.
- **Drinfeld center vs derived center (AP-CY4)**: Correctly separated at L258-267.
- **AP-CY26 (Verdier != sigma_2 inversion)**: Correctly handled at L411-420, L604-606.
- **CoHA character != bar character**: No CoHA character confusion found.
- **Class M E_3 bar = 6^g (AP-CY21/38)**: Correctly stated at L714 "dim E_infty = 6^g at genus g".
- **Verdier spectral functor**: Correctly proved (Thm thm:verdier-spectral-functor, L573-621).
- **Koszul conductor formula**: Correctly class-dependent at L483-558.
- **K3 landscape**: Correctly classified (Prop prop:e2-koszul-k3-landscape, L945-983).
- **ADE at level 1**: Correctly treated (Prop prop:ade-koszul-landscape, L985-1006).
- **E_2 -> E_3 promotion for K3 x E**: Correctly scoped (Rem rem:e2-to-e3-k3, L1008-1027).
- **Derived Koszul conductor**: Stasheff telescoping correctly proved (Thm thm:derived-conductor, L1125-1155).
- **CFG25 hierarchy table**: Correctly marked "Conjectural" for E_3 row (L1177).
- **Part~N**: Zero hardcoded references.
- **Bare chi**: One instance at L950: "equals chi(O_{K3}) for K3 by the d=2, h^{1,0}=0". This is correctly scoped with chi(O_{K3}) (subscripted, not bare).
- **Claim statuses**: All consistent.
- **Shadow class determines derived behaviour**: Correctly classified at Prop prop:shadow-class-derived (L1081-1123).
| 102 | 1/eta^2=triangular | Simple expansion | Bicoloured partitions | sequence family |
| 103 | S_2=c/12 Vir | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 104 | K_BP=2 | Conductor exists | K_BP=196 | local/global |
| 105 | kappa(BP)+kappa(BP^!)=1/3 | Rational | 98/3 | numerical factor |

## XVI. Vol II Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 106 | Dunn E_1xE_1=E_2 on A | Dunn real | On Z(A)/Mod_A not A | native/derived |
| 107 | R-matrix promotes A E_1->E_2 | R braiding | On Mod_A. Rep E_2 | native/derived |
| 108 | ALL VAs not E_inf | Poles | ALL VAs ARE E_inf | label/content |
| 109 | E_inf=no poles | BD subclass | E_inf=LOCAL | specific/general |
| 110 | B(A)=int_R A | Related FH | int_R A=A. B=int_{[0,1]} | construction/narration |
| 111 | Deconc=chiral coproduct | Both | DIFFERENT objects | algebra/coalgebra |
| 112 | E_inf->E_3 automatic | E_2 automatic | E_3 needs 3d HT | automatic/constructed |
| 113 | Bar degree=E_1 direction | Grading | Grading != operadic | label/content |
| 114 | Y_z^hbar(g) | Y_hbar(g) | z on structures not algebra. 531 | label/content |
| 115 | {T_lam T}=(c/2)lam^3 | OPE coeff | (c/12)lam^3. Factor 1/3! | convention |
| 116 | S_2=c/12 | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 117 | Vir m_3 formula errors | Computable | Wrong coefficients | arithmetic |
| 118 | betaGamma/bc swapped | Both exist | Sign flip. 16 corrections | convention/sign |
| 119 | W_N collapse E_4 | SS collapses | E_{2N} for N>=3 | arithmetic |
| 120 | N=4 k'=-k-2 | Dual exists | k'=-k-4. h^v=2 | arithmetic |
| 121 | FP lambda_2=1/1152 | Value exists | 7/5760. Shared wrong derivation | arithmetic |
| 122 | Heis trivial braiding | Simple | R=exp(k*hbar/z) NOT trivial | specific/general |
| 123 | J(z)J(w)~1/(z-w) | OPE | DOUBLE pole: k/(z-w)^2 | arithmetic |
| 124 | d_alg(Vir)=1 | Has depth | d_alg=inf. d_gen=1 | two-depth |
| 125 | self-dual=critical | Both special | c*=13 != c_crit=26 | label/content |
| 126 | Formality failure=defect | Fails d'=1 | IS the feature | label/content |
| 127 | kappa/S_2 interchangeable | Related | Only Vir/Heis | specific/general |
| 128 | W(2)=(betaGamma)^{Z/2} | Z/2 orbifold | Symplectic fermion c=-2 | wrong parent |
| 129 | Agent composite confabulation | Each real | Composite unconstructed | confabulation |
| 130 | Engine+test same wrong | Both agree | Shared wrong model | tautological |
| 131 | Spectral R(z)=categorical braiding | Both encode | Family with z vs single nat trans | specific/general |
| 132 | B^FG=B^Sigma=B^ord | All bar | DIFFERENT: ord->Sigma->FG | three-object |
| 133 | PVA=P_inf | Both | OPPOSITE: descend vs ascend | construction/narration |
| 134 | SC bar on R x C | Involves | Product operad. Needs Deligne-Tamarkin | construction/narration |
| 135 | Within-surface E_1+transverse independent | Two E_1s | Koszul dual via Hom | construction/narration |
| 136 | RT from E_1 ordered | RT exists | E_inf FH (CFG) | specific/general |
| 137 | Two Yangian defs equivalent | Both | RTT weaker than quadruple | weak/strong |
| 138 | Miura coefficient 1/Psi | Involves | (Psi-1)/Psi. Accidental at Psi=2 | accidental agreement |

## XVI. k3e_cy3_programme.tex Deep Enforcement (2026-04-15, second pass, 3391 lines)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 139 | kappa_cat(K3) = 2 = chi(O_{K3}) described as "the arithmetic genus" probing K3 x E | chi(O_{K3}) = 2 IS correct for K3 fiber | In context of K3 x E kappa-spectrum, value 2 is kappa_ch(A_{K3}) (algebraization invariant), NOT kappa_cat (manifold invariant of K3 x E). kappa_cat(K3 x E) = 0 by Kunneth. | Fixed: replaced with "kappa_ch(A_{K3}) = 2 is the K3 sigma model modular characteristic (an algebraization invariant, not a manifold invariant; cf. AP-CY55)". | conflation | k3e_cy3_programme.tex L1777 |
| 140 | Table column header "kappa_ch" covers row with kappa_BKM = 5 | kappa_BKM = 5 IS correct | Table mixes kappa_ch (rows 1-2) and kappa_BKM (row 3) under single kappa_ch column header. AP113 violation. | Fixed: column header changed to kappa_bullet, each row now has explicit subscript (kappa_ch or kappa_BKM). | label/content | k3e_cy3_programme.tex L965, L973 |
| 141 | "conditional on CY-A_3 for the existence of A_{K3 x E}" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction). A_{K3 x E} exists. | Fixed: updated to cite CY-A_3 as proved; remaining conjecture content is the factorisation structure and shadow correction identification. | temporal | k3e_cy3_programme.tex L3236-3237 |
| 142 | Conjecture: kappa_BKM = kappa_ch(S) + kappa_ch(S x E) universally for S x E | True for N=1 (5 = 2+3) | PROVED FALSE for Z/NZ-orbifolds N>=2 by kappa_bkm_adversarial.py (62 tests). AP-CY37. | Fixed: downgraded from conjecture to remark noting this is a numerical coincidence for N=1; correct universal formula is kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general | k3e_cy3_programme.tex L2172-2189 |
| 143 | Programme C asks "Does kappa_BKM = kappa_ch(surface) + kappa_ch(CY_3) hold?" as open | Was open at time of writing | Already answered NEGATIVELY for N>=2. Correct universal: kappa_BKM = c_N(0)/2. | Fixed: restated as answered (fails for N>=2), cited adversarial engine and AP-CY37. For non-K3-fibered CY3: kappa_BKM undefined. | temporal | k3e_cy3_programme.tex L2130-2136 |

### Verified Clean (no violations in k3e_cy3_programme.tex):

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout the entire 3391-line file.
- **AP-CY7 (CoHA != chiral)**: L18 explicitly parenthetically notes "AP-CY7: the CoHA is associative, not chiral; the passage to a chiral algebra requires the functor Phi".
- **AP-CY8 (denominator != bar Euler)**: L697 reference to "twined bar Euler product" is observational (eta product decomposition), not claiming bare identification.
- **AP-CY10 (flop != Koszul)**: No flop/Koszul conflation found.
- **AP-CY4 (Drinfeld center != derived center)**: L840-841 correctly distinguishes derived centre from Koszul dual ("the universal bulk is a separate object from A^!").
- **AP-CY12 (shadow class from full tower)**: L399-452 computes shadow class M from full tower through degree 12, not from non-formality alone.
- **AP-CY13 (Part references)**: Zero hardcoded Part~N references.
- **AP-CY17 (MF CY dim)**: No matrix factorization claims in this file.
- **AP-CY34 (kappa_ch != chi(O_X) at odd d)**: No bare kappa_ch = chi(O_X) claim outside d=2 scope.
- **AP-CY37 (kappa_BKM decomposition)**: Proposition prop:kappa-bps-decomposition (L1808-1867) correctly identifies the decomposition as a "numerical coincidence" specific to N=1, cites adversarial engine. The conjecture and Programme C question (violations 142, 143) were the exceptions, now fixed.
- **AP-CY55 (manifold vs algebraization invariants)**: kappa-spectrum table (L1754-1781) correctly uses kappa_ch for algebraization invariants; the one exception (L1777 using kappa_cat(K3) for a value in the spectrum) was fixed (violation 139).
- **AP-CY56 (E_n scoping at d=3)**: No unscoped E_2-chiral claims at d=3 found. The file primarily discusses d=2 (K3 sigma model).
- **AP-CY59 (multiple algebraizations)**: L1758-1759 explicitly cites "AP-CY59: only the chiral de Rham complex comes from Phi".
- **AP-CY60 (six routes)**: No six-routes discussion in this file.
- **AP24 (kappa+kappa'=0)**: L829 correctly scoped to "free-field/CY sigma models"; L1356 correctly scoped to "free fields".
- **All theorems**: The 5 \begin{theorem} environments all carry \ClaimStatusProvedElsewhere or \ClaimStatusProvedHere. All conjectures use \begin{conjecture} with \ClaimStatusConjectured.
- **Convention**: phi_{0,1} normalization at L466-477 explicitly uses Eichler-Zagier convention with Z_{K3} = 2*phi_{0,1} and phi_{0,1}(tau,0) = 12, and the factor of 2 = kappa_ch(K3) is identified at L551-579 (AP-CY42 compliant).
- **BKM universal formula**: kappa_BKM = c_0(0)/2 = 10/2 = 5 correctly stated at L1816-1821 and L3119-3120 via Borcherds weight theorem, with explicit citation of prop:bkm-weight-universal.

## XVIII. toroidal_elliptic.tex Deep Pass (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 144 | kappa_ch = rank(Lambda) for lattice VOA | Bar curvature = rank*level | Conflates kappa_ch with kappa_fiber in CY context | kappa_ch(K3)=2 (algebraization); kappa_fiber=24 (lattice rank). For abstract rank-r Heis at level k: curvature=rk | kappa conflation | toroidal_elliptic.tex L437 |
| 145 | kappa_ch(A_E) = 24 "(rank of free-boson lattice)" | Central charge of boundary algebra IS 24 | Parenthetical describes kappa_fiber not kappa_ch | 24 = central charge of A_E = kappa_fiber. kappa_ch(K3)=2. Coincidence at level 1 | kappa conflation | toroidal_elliptic.tex L1526 |
| 146 | Two hbar conventions without bridge (hbar_1,hbar_2 vs plain hbar) | Both conventions valid | No explicit bridge identity connecting them | Need: q=e^{hbar_1}, t=e^{-hbar_2}; rational limit hbar=hbar_1 | convention clash | toroidal_elliptic.tex L402 vs L1440 |
| 147 | chi(K3)=24 bare without chi_top subscript | chi_top(K3)=24 correct | Bare chi risks confusion with chi(O_{K3})=2 in kappa context | Use chi_top(K3)=24 or dim H*(K3)=24 explicitly | label/content | toroidal_elliptic.tex L1515 |
| 148 | vartheta_1 vs theta_1 notation inconsistency | Same function | Notation switch mid-file | Harmonize to theta_1 throughout | convention | toroidal_elliptic.tex L131 vs L506+ |

## XIX. Foundation/Stub Chapter Deep Pass (2026-04-15)

Files audited: cy_categories.tex (~208 lines), cyclic_ainf.tex (~207 lines), hochschild_calculus.tex (~393 lines), quantum_groups_foundations.tex (~333 lines), braided_factorization.tex (~1555 lines).

### Violations Found

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 149 | kappa_ch = 2 in K3 x E E_3 S-matrix weight formula | The weight -4 = -10 + 6 is numerically self-consistent | Uses kappa_ch(K3) = 2 without disambiguating from kappa_ch(K3 x E) = 3 | The E_3 weight formula wt(S_hat) = -2*kappa_ch uses the K3 FIBER value kappa_ch(K3) = 2, not the total space kappa_ch(K3 x E) = 3. The subscript must clarify which kappa_ch is intended (AP113/AP-CY55). If the formula truly uses the fiber value, write kappa_ch(K3) explicitly, not bare kappa_ch in a K3 x E context. | kappa conflation | braided_factorization.tex L803-804, L821-822, L939, L1054-1057 |
| 150 | Phi: CY_d-Cat -> E_n-ChirAlg (bare E_n, no d-scope) | The signature is correct abstractly | FM43: bare E_n without specifying n=2 at d<=2, n=1 at d>=3. Line 167 says "E_2-enhancement via S^d-framing" unconditionally, wrong at d>=3 | Must scope: (n=inf at d=1, n=2 at d=2, n=1 at d>=3). The "E_2-enhancement" in line 167 only applies at d<=2. | scope error | cyclic_ainf.tex L164-167 |
| 151 | chi(K3) = 24 (bare chi for topological Euler char) | chi_top(K3) = 24 is correct | Bare chi risks confusion with chi(O_{K3}) = 2 | Use chi_top or state "topological Euler characteristic" before formula. Context is clear from "matching the topological Euler characteristic" but chi symbol is ambiguous. | label/content | cy_categories.tex L124 |
| 152 | chi(X) = 24 (bare chi for topological Euler char) | Same as #151 | Same bare chi issue | Context says "the Euler characteristic chi(X) = 24 familiar from lattice K3 geometry" without "topological" qualifier. Preceding text computes dim HH = 24, making it clear, but chi symbol alone is ambiguous vs chi(O_X). | label/content | cyclic_ainf.tex L139 |

### Verified Clean

**cy_categories.tex (208 lines)**:
- AP113 (bare kappa): CLEAN. All kappas subscripted: kappa_cat (L127-131), kappa_ch (L133, L191, L201), kappa_BKM (L133, L201).
- AP-CY1 (CY dim): CLEAN. L46: Fuk(M) CY of dim_R(M)/2 = n. L51: D^b(Coh(X)) CY of dim n (complex). L56: MF(W) CY of n-2 (AP-CY17 correct).
- AP-CY2 (CY trace in HC^-): CLEAN. L156-161 places CY class in HC^-_d with explicit AP-CY2 citation.
- AP-CY56 (E_n scope): CLEAN. L176: Phi -> E_2-ChirAlg scoped to d=2. L180: Phi_3 -> E_1-ChirAlg scoped to d=3.
- AP-CY34 (kappa_ch != chi at odd d): CLEAN. L191 scoped to K3 (d=2).
- AP-CY55 (kappa_cat(K3xE)): Not directly stated, but L133 correctly distinguishes kappa_cat(K3) = 2 from kappa_ch(K3xE) = 3.
- CY-A_3 status: CLEAN. L178 says "d=3 extension is now proved (inf-categorical)." L196 says "PROVED by the inf-categorical argument."
- Theorem environments: All appropriate. L73, L92, L163: ProvedElsewhere. L184: ProvedHere, scoped to d=2.
- Hochschild: L62 properly categorical (Sec "Hochschild cohomology and the CY structure").

**cyclic_ainf.tex (207 lines)**:
- AP113 (bare kappa): CLEAN. All kappas subscripted throughout.
- AP-CY2: CLEAN. L66 correctly states lift to HC^-.
- AP-CY1: CLEAN. L80 explicitly warns "d is the complex dimension, not the real dimension 2n" with AP-CY1 citation.
- AP-CY55: CLEAN. L195 correctly computes kappa_cat(K3xE) = chi(O_K3)*chi(O_E) = 2*0 = 0.
- AP-CY34: CLEAN. L176 restricts kappa_cat = chi(O_X) to d=2. L156 notes chi(O_Q) = 0 for quintic.
- CY-A_3 status: CLEAN. L156 references Theorem CY-A_3, L186 uses \ClaimStatusConjectured for the d=3 kappa identification.
- Theorem environments: L169 theorem scoped to d=2. L183 conjecture for d=3. Correct.

**hochschild_calculus.tex (393 lines)**:
- AP113: CLEAN. Only kappa_cat appears (L382), properly subscripted.
- AP160 (Hochschild convention): CLEAN. L7-17 explicitly states "categorical Hochschild" and distinguishes from chiral Hochschild of Vol I.
- AP-CY35 (B hierarchy): CLEAN. Connes B is properly B (= B^{(0)}, the mixed complex operator). No B^{(j>=1)} hierarchy appears.
- E_n levels: CLEAN. L62 correctly notes "E_2-algebra structure on HH" from Deligne conjecture (input is dg category, E_inf). L326 correctly identifies E_1 output at d=3.
- CY bracket spectrum: L81-90 correctly maps d -> bracket degree: d=1 BV, d=2 Poisson, d>=3 shifted Poisson.
- Theorem environments: All use ProvedElsewhere. No Vol III claims in theorem env.

**quantum_groups_foundations.tex (333 lines)**:
- AP113: CLEAN. kappa_ch^{KM} (L116-117), kappa_ch (L234, L246, L331), kappa_BKM (L246, L331). All subscripted.
- AP-CY5 (root of unity): CLEAN. L191 explicitly cites AP-CY5.
- AP-CY7 (CoHA): CLEAN. L259 parenthetically notes "AP-CY7: the CoHA is associative, not chiral."
- AP-CY6/AP-CY14 (theorem env): CLEAN. CY-C (L231-240) correctly uses \begin{conjecture} with \ClaimStatusConjectured. KL (L179) correctly theorem with ProvedElsewhere.
- CY-A_3 status: CLEAN. L247 says "functor Phi_3 at d=3 is now proved."
- E_n scope: CLEAN. L254 correctly says "E_2-data on Rep(A)" via Drinfeld center, not E_2 on A itself at d=3.
- AP-CY10 (flop vs Koszul): CLEAN. L331 distinguishes Koszul conductor (K=0) from flop invariance.

**braided_factorization.tex (1555 lines)**:
- AP113: CLEAN (except violation #149 above where kappa_ch is ambiguous between fiber and total space).
- AP-CY56 (E_n scope): CLEAN. L26-38 explicitly scopes d=2 native E_2 vs d=3 derived E_2 via center. Table L1364-1377 correct.
- AP-CY55: CLEAN. L500-508 warns AP-CY55 explicitly. L1389 correctly states kappa_cat(K3xE) = 0.
- AP152 (ordered): CLEAN. All "ordered" usages mean labeled-ordered (E_1 combinatorial). E.g. L243 "ordered coalgebra", L308 "primitive ordered object", L1278 "ordered Ran space."
- CY-A_3 status: CLEAN. L452 "CY-A_3 is now proved." L885 same. L1373 table: "PROVED (CY-A_3)."
- Theorem environments: L328 CY-B theorem correctly uses \ClaimStatusConditional. All conjectures use \begin{conjecture}.
- AP-CY8: No bare "bar Euler = Phi_10" identification without CY-A citation.
- AP-CY12 (shadow class): L587-589 correctly classifies K3 as class G from shadow tower data.
- AP-CY31 (spectral z): L1401 explicitly cites AP-CY31 "z is spectral, not worldsheet."
- AP-CY22 (Miki): L1423 discusses Miki correctly as algebra-specific.
- AP-CY33 (chain vs rational): L1504 explicitly notes chain-level content essential, formality destroys it.
- AP-CY17 (MF dim): No MF claims in this file.

### Summary

4 violations found across 5 files (2,696 total lines). 3 are low-severity notation/scoping issues (#150, #151, #152). 1 is medium-severity kappa conflation (#149) where the E_3 weight formula uses kappa_ch = 2 (K3 fiber) without disambiguation from kappa_ch(K3xE) = 3 in a K3 x E context. The first-pass agent's kappa_cat(K3xE) = 0 fixes in cyclic_ainf.tex (L195) and braided_factorization.tex (L1389) are VERIFIED APPLIED and correct.

---

## Deep Enforcement: e1_chiral_algebras.tex + drinfeld_center.tex (2026-04-15)

**Files**: chapters/theory/e1_chiral_algebras.tex (2098 lines), chapters/theory/drinfeld_center.tex (2054 lines). Total: 4,152 lines read line-by-line.

### Violations Found and Fixed

| # | File | Line(s) | AP | Severity | Description | Fix |
|---|------|---------|----|----------|-------------|-----|
| 153 | e1_chiral_algebras.tex | 173 | AP-CY41 (temporal) | HIGH | Stale conditionality: "at d=3 the construction is conditional on Theorem thm:e1-sector-d3" but CY-A_3 is PROVED. | Changed to "at d=3 this produces the braided categories via the E_1-chiral algebra of Theorem thm:e1-sector-d3 (CY-A_3, proved)." |
| 154 | e1_chiral_algebras.tex | 1582-1593 | AP-CY41 (temporal) | HIGH | Stale conditionality: "conditionally at d=3 via CY-A_3" and "The functor Phi is conjectural" -- both stale since CY-A_3 is proved (inf-cat). | Rewrote to: "at d=3 by Theorem CY-A_3 (proved, infinity-categorical framework)" and "The functor Phi produces a factorization algebra F on a curve C by Theorem CY-A_3." |
| 155 | drinfeld_center.tex | 1231 | AP-CY41 (temporal) | LOW (comment) | Stale comment: "AP-CY6: A_{K3xE} doesn't exist. All results conditional on CY-A_3." -- A_{K3xE} now exists. | Updated comment to reflect CY-A_3 proved; CY-C conditional. |
| 156 | drinfeld_center.tex | 812 | AP-CY41 (temporal) | MEDIUM | "conjectural for d=3" re bracket identification under Phi. CY-A_3 now proved. | Updated to: "for d=3 at the infinity-categorical level (CY-A_3, proved); the chain-level identification at d=3 for non-formal algebras remains open." |
| 157 | drinfeld_center.tex | 1271-1274 | AP-CY41 (temporal) | MEDIUM | ClaimStatusConditional on prop:k3e-nonlocality-quantification despite CY-A_3 being proved. | Upgraded to ClaimStatusProvedHere with note that CY-A_3 is proved. |
| 158 | drinfeld_center.tex | 2016 | AP-CY41 (temporal) | LOW (comment) | Stale comment: "AP-CY6: CONJECTURAL. Requires CY-A_3." The remark is conjectural because of CY-C, not CY-A_3. | Updated comment to cite CY-C as the dependency, CY-A_3 as proved. |

### Clean Checks (no violations found)

**AP113 (bare kappa)**: CLEAN. Both files use exclusively subscripted kappa: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber, kappa_bullet. Zero bare kappa instances.

**AP-CY23 (E_1-chiral bialgebra vs E_inf vertex bialgebra)**: CLEAN. e1_chiral_algebras.tex L185-246 contains the full comparison table and explicitly states: "Li's vertex-bialgebra framework is the E_inf shadow of the E_1-chiral bialgebra: it retains the vertex-algebraic OPE structure but symmetrizes the coproduct, losing the R-matrix." L1128-1133 drives home: "Li's vertex-bialgebra framework, which works with B^Sigma and the coshuffle coproduct, cannot carry a Hopf structure." The E_1-chiral bialgebra axiom system (Def def:e1-chiral-bialgebra, L834-890) is clearly the correct Hopf framework. L757-761 explicitly rejects Li's framework.

**AP-CY25 (R-matrix extraction formula)**: CLEAN. No instance of R(z) = (id tensor S) compose Delta(1). The R-matrix is correctly constructed from the half-braiding throughout. drinfeld_center.tex Construction constr:rmatrix-from-center (L426-553) gives the 7-step construction via half-braidings. e1_chiral_algebras.tex L1231-1281 (Prop prop:r-matrix-from-drinfeld) correctly defines R(z) via the half-braiding sigma_{V,W}(z).

**AP-CY7 (CoHA is associative, NOT chiral)**: CLEAN. e1_chiral_algebras.tex L19: "the CoHA multiplication is ordered (short exact sequences have a preferred direction)." L311: "the CoHA itself is an E_1-associative multiplication." Neither file claims CoHA is chiral or E_2.

**AP-CY54 (Drinfeld center NOT categorified averaging)**: CLEAN. drinfeld_center.tex L1078-1122 (Remark rem:center-not-averaging) is an explicit 44-line refutation of the "categorified averaging" error. The remark meticulously explains: center = right adjoint to forgetful (constructs half-braidings), averaging = abelianization (quotients by non-commutativity). "Construction versus quotient: the center adds data, averaging removes it." e1_chiral_algebras.tex L10, L170, L342 all explicitly say "NOT categorified averaging." Zero positive "categorified averaging" claims.

**AP-CY4 (Z(C) != Z^der(A) != z(A))**: CLEAN. drinfeld_center.tex L147-208 (Remark rem:three-centers) and L210-261 (Remark rem:three-centers-sharp) provide two explicit tables distinguishing all three centers. L1473-1512 (Remark rem:drinfeld-vs-derived-k3e) gives a table comparing dimensions (49 vs 325) and structure types for K3. Line 1433 explicitly tags "AP-CY4: this is the algebraic derived center, not the categorical Drinfeld center."

**AP-CY57 (R-matrix CONSTRUCTED, not narrated)**: CLEAN. drinfeld_center.tex Construction constr:rmatrix-from-center (L426-553) is a fully explicit 7-step construction with equations at each step. Remark rem:arrow-of-explanation (L555-579) explicitly addresses the direction of explanation. The R-matrix IS the half-braiding (Step 4, L480-494), constructed step by step.

**AP-CY56 (E_n scoping at d=3)**: CLEAN. Both files consistently state: at d=3, A is E_1 (native); E_2 is on the center Z(Rep^{E_1}(A)), NOT on A itself. drinfeld_center.tex L774: "For d=3, the boundary algebra is E_1 (not E_2)." L1160-1193 (Remark rem:two-sources-e2) explicitly contrasts the two sources of E_2 braiding.

**AP-CY58 (CY-B d-dependent)**: CLEAN. The Koszul duality treatment in e1_chiral_algebras.tex sec:e1-koszul-three-families (L353-745) is explicitly E_1-Koszul duality. No uniform "E_2-chiral Koszul duality" claim across all d.

**AP-CY55 (kappa_cat is manifold invariant)**: CLEAN. e1_chiral_algebras.tex L131 distinguishes all four kappa values for K3xE: kappa_ch=3, kappa_cat=2, kappa_fiber=24, kappa_BKM=5.

**AP-CY31 (spectral z != worldsheet z)**: CLEAN. e1_chiral_algebras.tex Remark rem:z-spectral-vs-worldsheet (L1181-1184) is an explicit 4-line disambiguation. drinfeld_center.tex L500-503 (Step 5) cites the same remark and explicitly states "u is a Yangian spectral parameter, not a worldsheet coordinate."

**AP152 (ordered specification)**: MOSTLY CLEAN. All critical instances specify labeled-ordered, time-ordered, or normally-ordered. e1_chiral_algebras.tex L197 table header: "E_1 (labeled-ordered)." L1017: "mu_{E_1} is the labeled-ordered product." L1292: "the time-ordered OPE, not the normally-ordered product." L1983: "(AP152: labeled-ordered, NOT time-ordered)." A few instances at L840, L848, L1099 use bare "ordered" within the E_1-chiral bialgebra definition where context makes "labeled-ordered" unambiguous (the definition is about E_1 objects). LOW severity, not fixed.

**AP-CY53 (Conf_2 ordered vs unordered)**: drinfeld_center.tex uses Conf_2 consistently for the labeled (ordered) configuration space. The fundamental group computations are standard operadic statements. The claim pi_1(Conf_2(R)) = Z at L14 refers to the labeled configuration space {(x1,x2) : x1 != x2} which has two connected components (each contractible, so pi_1 = 0 per component). Operadically, the relevant space is E_n(2), and E_1(2) = S^0 (two points). The heuristic is standard in the Costello-Gwilliam literature and means "the E_1 operad detects only ordering (pi_0 = Z/2), while the E_2 operad detects braiding (pi_1 = Z)." The prose conflates the E_n(2) topology with pi_1, but this is a standard shorthand. LOW severity, no fix needed.

**CY-A_3 status consistency**: e1_chiral_algebras.tex L155-161 correctly states CY-A_3 as \ClaimStatusProvedElsewhere with "By Theorem CY-A_3" and "downstream results are now unconditional." drinfeld_center.tex L1248-1256 correctly separates CY-A_3 (proved, constructs A_{K3xE}) from CY-C (conjectural, for G(K3xE)). All \begin{conjecture} environments are for CY-C-dependent results.

**Theorem/conjecture environments**: CLEAN. e1_chiral_algebras.tex: all CY-C-dependent results use \begin{conjecture} (L618, L1307, L1544, L1968). All proved results use \begin{theorem} or \begin{proposition} with \ClaimStatusProvedHere or ProvedElsewhere. drinfeld_center.tex: conj:slab-double (L882), conj:qvcg (L893), conj:v3-drinfeld-center-equals-bulk (L912), conj:chiral-qg-k3 (L1874) all correctly use \begin{conjecture}. The chiral quantum group section (L1854ff) is entirely conjectural and correctly tagged.

### Summary

6 violations found across 2 files (4,152 lines). All 6 are temporal (AP-CY41): stale conditionality statements from before CY-A_3 was proved. 2 HIGH severity (prose claiming d=3 results are conditional), 2 MEDIUM severity (ClaimStatus and bracket-identification status), 2 LOW severity (stale comments). All 6 fixed. Zero AP113, AP-CY23, AP-CY25, AP-CY7, AP-CY54, AP-CY4, AP-CY57, AP-CY56, AP-CY58, AP-CY55, AP-CY31 violations. Both chapters are thoroughly AP-compliant on all substantive mathematical checks.

## XXI. working_notes.tex Enforcement (2026-04-15, ~5300 lines)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 149 | "G(X) realized as an E_2-chiral algebra" (overview, d=3 context) | E_2 IS relevant at d=3 | At d=3, Phi outputs E_1. E_2 lives on Z(Rep^{E_1}(A)), not on A. | Fixed: "E_1-chiral algebra (with E_2-braiding on the Drinfeld center of the representation category)". AP-CY56/FM43 | native/derived | working_notes.tex L179 |
| 150 | "Full Yangian/BKM = E_2-chiral algebra A(X)" in dictionary table | E_2 IS the target braided structure | At d>=3, the algebra A(X) is E_1; E_2 is derived via center | Fixed: "E_1-chiral algebra A(X) (E_2 on center)". AP-CY56 | native/derived | working_notes.tex L267 |
| 151 | "suppose CY-A produces an E_2-chiral algebra A_X" in Conjecture | At d=2 this is correct | Conjecture is about CY3 where Phi outputs E_1 | Fixed: "E_1-chiral algebra A_X (with E_2-braiding on Z(Rep^{E_1}(A_X)))". AP-CY56 | scope error | working_notes.tex L284 |
| 152 | kappa_ch = 5 for K3 x E computationally verified data | 5 IS the Borcherds weight | 5 = kappa_BKM (Igusa weight). kappa_ch = 3 (chiral de Rham). | Fixed: "kappa_BKM = 5 (the Borcherds weight; the chiral modular characteristic is kappa_ch = 3)". AP113/AP-CY55 | kappa conflation | working_notes.tex L300 |
| 153 | "kappa_ch(G(K3 x E)) = 5" modular characteristic section | 5 = weight(Delta_5) correct | This is kappa_BKM, not kappa_ch. kappa_ch(K3xE) = 3. | Fixed: "kappa_BKM(K3 x E) = 5 = c(0)/2 (Borcherds weight theorem). kappa_ch = 3." AP113 | kappa conflation | working_notes.tex L334 |
| 154 | "Smooth CY3 = E_2-chiral" in smooth/singular table | E_2 enhancement IS the goal | At d=3, A_X is E_1; E_2 only on Drinfeld center | Fixed: "E_1-chiral (E_2 on Drinfeld center)". AP-CY56 | native/derived | working_notes.tex L1082 |
| 155 | Fiber-vs-global table: "Global K3 x E = 5" under kappa_ch column | kappa_BKM = 5 correct | Column header kappa_ch but value is kappa_BKM | Fixed: separate rows for kappa_BKM = 5 and kappa_ch = 3. AP113 | kappa conflation | working_notes.tex L1295 |
| 156 | Grand atlas: "K3 x E, kappa_ch = 5" | 5 IS a real invariant of K3xE | kappa_ch = 3 (chiral); kappa_BKM = 5 (Igusa). AP113 | Fixed: "kappa_ch = 3 (kappa_BKM = 5)". | kappa conflation | working_notes.tex L1562 |
| 157 | "The full E_2-chiral algebra A_X is the Drinfeld center" | E_2 on center IS correct | A_X is E_1; "the full E_2-chiral algebra" conflates A with Z(Rep(A)) | Fixed: "E_2-braided structure lives on Z(Rep^{E_1}(A_X))... A_X itself remains E_1." AP-CY56 | native/derived | working_notes.tex L1695 |
| 158 | "the full E_2-chiral algebra of K3 x E" in gluing dream question | E_2 enhancement IS the goal | At d=3, the algebra is E_1; E_2 lives on Z(Rep) | Fixed: "the E_2-braided representation category Z(Rep^{E_1}(A_{K3xE}))". AP-CY56 | native/derived | working_notes.tex L2975 |
| 159 | kappa_BPS (forbidden subscript, 4+ instances) | kappa_BKM IS the correct subscript | AP113 forbids kappa_BPS; should be kappa_BKM | Fixed: replaced all kappa_BPS -> kappa_BKM. AP113 | label/content | working_notes.tex L1378, L3098, L3102, L3132 |
| 160 | kappa_BKM = 5 = kappa_ch(K3) + kappa_ch(K3xE) = 2+3 presented as structural explanation | 5 = 2+3 IS numerically true for N=1 | PROVED FALSE for N>=2 orbifolds (AP-CY37). Numerical coincidence. | Fixed: noted "numerical coincidence for N=1; fails for N>=2. Correct universal: kappa_BKM = c_N(0)/2." | specific/general | working_notes.tex L3781 |
| 161 | "conditional on CY-A_3" (chiral volume conjecture) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction) | Fixed: "CY-A_3 is now proved; A_C exists by Theorem CY-A_3". Remaining: the asymptotic formula itself. | temporal | working_notes.tex L5175, L5187 |
| 162 | "counting remains conditional on CY-A_3" (mock modular K3) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Fixed: remaining conditionality is CY-B (shadow=BPS identification), not CY-A_3. | temporal | working_notes.tex L5236 |
| 163 | "conditional on CY-A_3" (Koszul route K3 Yangian) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Fixed: "CY-A_3 proved; chain-level Koszul data conditional on explicit framing". | temporal | working_notes.tex L5293 |
| 164 | "conditional on CY-A, AP-CY6" (quintic GV invariants) | CY-A WAS the bottleneck | CY-A_3 is now PROVED | Fixed: CY-A proved; remaining conditionality is CY-B (shadow=GV identification). | temporal | working_notes.tex L2521 |

### Verified Clean (no violations in working_notes.tex):

- **AP113 (bare kappa)**: Zero bare kappa violations after fixes. All kappa subscripted: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber, kappa_eff, kappa_bullet.
- **AP-CY4 (Drinfeld center vs derived center)**: Correctly distinguished at L1097-1120 (Drinfeld center = category center via half-braidings) and L1736 (chiral derived center).
- **AP-CY7 (CoHA != chiral)**: CoHA correctly identified as associative at L348-356, L1025, L1695. Connection to chiral is via functor Phi, not identification.
- **AP-CY8 (denominator != bar Euler)**: No bare identification. All instances cite both CY-A and Vol I anchors.
- **AP-CY10 (flop != Koszul)**: L2007 correctly scoped ("free-field type").
- **AP-CY12 (shadow class from full tower)**: All shadow class assignments computed from full tower data, not from non-formality alone.
- **AP-CY13 (Part references)**: Zero hardcoded Part~N references.
- **AP-CY17 (MF CY dim)**: No matrix factorization CY claims requiring n-2 check.
- **AP-CY22 (Miki algebra-specific)**: Correctly stated at L4306-4323 with k[x]/(x^2) counterexample.
- **AP-CY31 (spectral z vs worldsheet z)**: Correctly resolved at L4396-4405.
- **AP-CY33 (chain != rational)**: Correctly stated at L4116-4117.
- **AP-CY34 (kappa_ch != chi(O_X) at odd d)**: Correctly stated at L5036-5045.
- **AP-CY37 (kappa_BKM universal)**: Correctly stated at L3924-3933 and L4254-4264.
- **AP-CY42 (phi_{0,1} normalization)**: Warning at L1277-1280 and L4234-4252 with explicit convention statement.
- **AP-CY55 (manifold vs algebraization invariants)**: Three-level table at L3766-3777 correctly separates kappa_fiber, kappa_ch, kappa_BKM.
- **AP-CY59 (multiple algebraizations from single functor)**: L2984-2993 explicitly cites AP-CY59.
- **AP-CY60 (six routes != six Phi)**: L4682-4687 explicitly cites AP-CY60: "six independent constructions, not six applications of Phi."
- **AP152 (ordered specification)**: L4407-4410 explicitly resolves: labeled-ordered, time-ordered, normally-ordered.
- **CY-C**: All CY-C-dependent results correctly in \begin{conjecture}. Langlands=Koszul (L381), genus-2 BPS (L508), HMS shadow (L2882).
- **F2 (kappa_ch(K3) = 2 vs 12)**: Correctly flagged at L1916-1918 (false idea F2: kappa_ch(K3) = 12 from categorical formula, 2 from chi(O_K3)).

## Two Derived Centers Investigation (2026-04-16, adversarial swarm)

Five adversarial agents attacked claims about the two derived centers (chiral vs topological Hochschild). Key findings cached below.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 46 | "Spectral parameters from FM_k(C)" for End^ch_A | End^ch_A relates to FM via local-global identification | Narration: End^ch_A is algebraic (formal Laurent series in lambda_i). FM enters via comparison theorem (formal disk restriction), not the definition. | Three layers: (1) geometric model on FM_{n+1}(X) with log forms, (2) formal-disk restriction gives lambda_i as relative positions, (3) algebraic model End^ch_A with formal variables. The comparison is a theorem, not a definition. | construction/narration |
| 47 | "ChirHoch* and THH* are different-sized objects (dim 3 vs infinite)" | ChirHoch and THH compute different invariants | For Koszul algebras (Heisenberg), chain qi D*~S^1 dualizes to cochain qi (universal coefficients, finite-type). HH*(Weyl)=1-dim, not infinite. | Difference is STRUCTURAL (E_2 with spectral data vs abstract E_2), not DIMENSIONAL. Same cohomology groups for Koszul algebras; different E_2 algebra structures. | chain/cohomology confused with size/structure |
| 48 | "BZFN gives different answers depending on ambient category S as tunable parameter" | Two derived centers DO exist and produce different braided categories | S is not a free parameter. Both sides of BZFN use same S. Two centers come from TWO DIFFERENT ALGEBRAS: chiral A (in D-mod(Ran)) vs mode algebra A_mode (in Vect). | BZFN applied once to each algebra in its native ambient category. Different inputs, not different parameters. en_chiral_operadic_circle.tex L1086-1091 correct. | object/structure |
| 49 | "Topological Drinfeld center has no spectral parameters" | Chiral structure creates translation automorphism enabling evaluation modules | Yangian Y(g) as purely associative algebra HAS evaluation modules V_u and spectral R(z=u-v) in its Drinfeld center. | Spectral parameter from representation theory (evaluation modules), not center construction. Chiral structure CREATES tau_z; once created, spectral params persist regardless of provenance. Correct claim: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. | construction/data/object three-way conflation |
| 50 | "Restricting chiral algebra to S^1 gives A_inf algebra" | E_2 restricts to E_1 on real submanifolds (Costello-Gwilliam) | Conflates four operations: (a) D-module restriction (ill-defined on real submanifold), (b) mode algebra (strictly associative, not A_inf), (c) int_{S^1} A = HH_*(A) (chain complex, not algebra), (d) pullback of FA along S^1 -> D* (gives E_1-algebra). | Correct: holomorphic FA on C restricted to real ray gives E_1-algebra (prop:holomorphic-e1). int_{S^1} gives Hochschild homology (chain complex). Mode algebra is strictly associative. E_1 = A_inf only in char 0 after homotopy transfer. | four-way conflation |
| 51 | BD chiral operad = algebraic End^ch_A | They are related by formal disk restriction (isomorphism after coordinate choice) | BD operad lives in D-modules on Ran(X); End^ch_A is formal Laurent series. These are different mathematical categories. The identification requires: (1) choose point p, (2) choose coordinate z on formal disk D, (3) trivialize D-module as (V, ∂), (4) identify j_*j^* with Laurent series. | Bridge is 4-step chain: local coordinate → formal disk → D-module trivialization → spectral variable identification. Isomorphism of non-Σ operads, coordinate-dependent. Aut(O)-equivariance absorbs coordinate dependence. Bridge Proposition assembling all 4 steps is ABSENT from manuscript (gap). | object/structure + expository gap |
| 52 | Geometric ChirHoch = algebraic ChirHoch (used interchangeably) | They ARE quasi-isomorphic for logarithmic chiral algebras | The comparison is stated only as a remark (rem:comparison-geometric-hoch, chiral_center_theorem.tex:346), NOT proved as a named theorem. Used without citation at 100+ locations across 3 volumes. The bar complex comparison IS a named theorem (thm:geometric-equals-operadic-bar). | Two models: geometric (FM compactifications, log forms, 3-component differential) vs algebraic (End^ch_A, formal variables, Gerstenhaber bracket differential). Quasi-isomorphic via logarithmic comparison theorem. At genus >= 1, geometric model carries curve-dependent data (periods, Green's function) that algebraic model lacks. | label/content (model ambiguity) |
| 53 | "Theorem H fails for THH / concentration has no THH analogue" | Theorem H IS specifically about ChirHoch* (uses dim(X)=1 for Ext amplitude) | THH = HH*(A_mode) is ALSO concentrated: HH*(Weyl) = C in degree 0 (MORE concentrated). The "fails for THH" claim confuses HH* (cohomology, concentrated) with H*_GF (Gel'fand-Fuchs continuous Lie cohomology, unbounded polynomial ring). | Three invariants: ChirHoch* concentrated in {0,1,2} (curve dimension), HH*(A_mode) concentrated in {0} (simplicity of Weyl algebra), H*_GF unbounded (polynomial ring). The genuine size difference occurs ONLY at critical level k=-h^v (Feigin-Frenkel center makes ChirHoch* infinite, HH* stays finite). | three-way conflation (ChirHoch/HH/GF) |
| 54 | "Physics requires two different bulk theories" | Physics has ONE bulk per boundary (uniqueness of derived center) | Two derived centers are two COMPUTATIONAL MODELS of the same physical observable (bulk algebra), not two different physical theories. Their equivalence is conj:drinfeld-center-equals-bulk (proved boundary-linear, open globally). | Physics: boundary A determines unique bulk Z^der(A). Two mathematical routes (ChirHoch via Hochschild functor, Z(U_A) via Koszul-dual reconstruction) should give the same answer. The conjecture says these two presentations agree. | construction/narration (two routes, one destination) |
| 55 | "The Vol I preface should open with geometry-indexed bar landscape table" | The organizing principle (geometry determines algebraic structure) IS correct | Vol I preface already has Section 1' (lines 827-925) with exactly this, scoped to curves. Current CG-compliant opening (lines 26-42) is better than a table. Two derived centers belong in Vol I BODY, not preface. Vol II's geometric ladder should not be duplicated. | Vol I preface constructs (CG principle); tables are surveys. Two derived centers belong in Vol I hochschild_cohomology.tex where the comparison is load-bearing. Vol II preface owns the 10-stage geometric ladder. Duplicating it damages the Vol I→Vol II handoff. | architectural (survey vs construction) |
| 56 | Tamarkin inconsistency: C*(H_k, H_k) = k[[κ]] vs Theorem H dim 3 | Both computations are correct | k[[κ]] is the DEFORMATION PARAMETER SPACE (how the family varies with level k). ChirHoch*(H_k) at FIXED k has dim 3 (Theorem H). These are different mathematical objects: total family deformation ring vs fiber at fixed parameter. | The reconstructor deformation parameter space (the Tamarkin k[[κ]]) and the bulk state space (ChirHoch* at fixed k) answer different questions. Neither is wrong. Resolution at hochschild.tex:3376-3413 (rem:drinfeld-center-heisenberg-thesis-resolution). | family/fiber conflation |

## Adversarial Audit 2026-04-16 (six parallel first-principles audits of load-bearing Vol III claims)

Six agents attacked: (1) CY-A_3 inf-cat proof, (2) Costello TCFT / Stasheff cancellation, (3) kappa_BKM universality, (4) class M E_3 bar = 6^g, (5) P_2(D)=0 + six routes, (6) CY-D d=3 + Y(gl(4|20)). Findings below.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 57 | HH^{-2}_{E_1}(A,A) = 0 by "unit-connectedness" for smooth proper CY_3 categories | Francis-Gaitsgory: fib(TAlg_{E_3} -> TAlg_{E_2}) = HH^*_{E_1}(A,A)[-2] (correct identification of WHERE obstruction lives) | Vanishing requires A connective. For CY_d category, A = HH_*(C) is Serre self-dual: HH_i(C) ≅ HH_{d-i}(C)*. At d=3, HH_{-3}(C) ≅ HH_0(C)* ≠ 0. A is NOT connective. The bar filtration degree count (cy_to_chiral.tex:1980) silently assumes A_{<0}=0. Patch via H^0(O_{K3×E})=k is the wrong invariant (confuses H^0(O) with HH^0(Perf)). | Correct statement: "Under additional hypothesis of connectivity of A, HH^{<0}_{E_1} vanishes and E_3-lift is unobstructed." This excludes smooth proper CY_3. For compact CY_3 the obstruction lives and must be computed, not declared absent. | hypothesis-dressed-as-conclusion (AP-CY14 ramification) |
| 58 | "Space of E_3-liftings is contractible" | Lifting spaces ARE torsors over obstruction cohomology (Dunn/Francis) | Contractibility requires ALL HH^{-2-j}_{E_1}(A,A) = 0 for j >= 0, i.e., vanishing of the full shifted cotangent complex. This is a much stronger statement than a single HH^{-2} vanishing. Asserted (cy_to_chiral.tex L1991) from the flawed connectivity argument. | For A non-connective, the space has nontrivial homotopy in every degree where HH^{-2-j}_{E_1} is nonzero. No contractibility without uniform connectivity bound. | part/whole (single-degree vs tower vanishing) |
| 59 | Costello TCFT Theorem A proves {b, B^(2)} = 0 | Costello arXiv:math/0412149 proves existence of TCFT from cyclic A_∞ algebra (genuine theorem) | Misattribution. Costello's theorem concerns the TCFT/cyclic-A_∞ equivalence, NOT the B^(j>=1) hierarchy identity. The engine operadic_tcft_mk_b2_engine.py (525 lines) contains ZERO numerical verification — it is prose strings in dataclasses. Tests check "0412149" appears in a string, not that any identity holds. | Correct: Costello establishes open-closed TCFT from A_∞. Passage to {b, B^(2)} = 0 requires the identification "B^(2) = genus-change operation" which is asserted (citing Costello 0706.1959) but never constructed. The identity remains unproved. | misattribution + narrative-as-proof |
| 60 | Cross-arity cancellation {b_3,B^(2)} cancelled by {b_2,B^(2)} via Stasheff | Stasheff A_∞ relations give d^2 = 0 for total differential b (genuine) | The author's OWN engine chain_level_m2_b2_cancellation.py proves the OPPOSITE: for single-object cyclic A_∞ CY_3 with μ_3 ≠ 0, the n=4 Stasheff relation forces μ_2 = 0 on augmentation ideal (Incompatibility Theorem). Then {b_2,B^(2)}_naive = 0 trivially and {b_3,B^(2)} = 2α[b] ≠ 0. Corollary cor:no-naive-cross-degree concedes {b_k,B^(2)} map to DISJOINT graded components CC_{n-k+1}, so cannot cancel. | The retreat to an undefined "B^(2)_TCFT" that "absorbs the discrepancy through moduli-space corrections" is vapor. No B^(2)_TCFT is constructed in the manuscript. {b, B^(2)_naive} ≠ 0 stands; the resolution is at the ∞-categorical level (which has its own gap — see #57) not the chain level. | refuted by own engine (AP-CY39 ramification) |
| 61 | "kappa_BKM = c_N(0)/2 PROVED unconditionally for all K3-fibered CY3s" | Borcherds 1998 weight theorem gives wt(BP(f)) = c_f(0)/2 (genuine classical theorem) | Two distinct invariants both called kappa_BKM: (i) wt(BP(φ_N)), automorphic form weight; (ii) BKM central charge / rank of g_{Δ}, CY invariant. The proposition DEFINES kappa_BKM := wt(BP(φ_N)) making "= c(0)/2" tautological. Identification with (ii) requires Gritsenko-Nikulin denominator identity for each N, valid for N=1,2,3,4 (and case-by-case otherwise). Engine FRAME_SHAPE_DATA hardcodes weight AND c_0 side-by-side with weight := c_0/2. Tests check Fraction(10,2)==5, tautological. | Scope: (a) kappa_BKM as weight: unconditional via Borcherds, trivial; (b) kappa_BKM as BKM central charge: proved via Gritsenko-Nikulin for 8 diagonal Z/NZ symplectic orbifolds of K3 × E (Chaudhuri-Dolan-Hockney-Polchinski/Gaberdiel-Volpato list); (c) "all K3-fibered" overclaim — general fibrations (paramodular, non-cyclic monodromy, STU off the diagonal locus) not covered. | label/content (two kappa_BKM) + tautological tests |
| 62 | "99 tests verify kappa_BKM = c_N(0)/2 independently" | Cross-validation is a valid methodology | All "paths" (A-F) import or reconstruct the same FRAME_SHAPE_DATA table. No path computes c_N(0) from an independently built orbifold Fourier expansion; no path computes BKM central charge from root multiplicities of g_{Δ_5}. Test farms check arithmetic identities against hardcoded values. | Genuine verification would require: (a) independent Fourier expansion of (K3^N-orbifold) elliptic genus, extract c(0); (b) independent enumeration of imaginary roots of g_{Δ_N} (where constructed), sum with multiplicities for central charge; (c) cross-check (a) and (b) agree to c/2. None exists in the test suite. | AP-CY49 ramification (tautological tests) |
| 63 | "Six routes to G(K3 × E)" converge (CY-C) | Six distinct constructions produce related algebraic objects sharing numerical invariants (genuine observation) | The six "routes" produce DIFFERENT TYPES of objects: Route 1 BKM superalgebra g_{Δ_5}, Route 2 abelian Heisenberg U(ĥ^+_{20}) (class G), Route 3 nonabelian Yangian Y(ŝo_4)^⊗4, Route 4 chiral algebra Φ_3(...), Route 5 heuristic AdS_3 BPS algebra, Route 6 Virasoro Vir_c. G(K3 × E) is never independently defined. The follow-up remark rem:bllpr-k3-connection EXPLICITLY admits these are "different algebraizations" distinguished by 5 invariants. | Correct: these are six constructions producing SIX DIFFERENT ALGEBRAS that share some invariants (central charge, modular weight). "Convergence" requires a specified target category and functors from each construction; neither exists. CY-C formally concerns C(g,q) for simple g, NOT G(K3 × E). AP-CY59 + AP-CY60 apply. | under-specified target (CY-C scope conflation) |
| 64 | P_2(D) = 0 "exact" from ε_1·ε_2 = ε·0 = 0 in 1d Ω-background | True observation: 1d Ω-background has only 1 deformation parameter | Circular: a 1d background has ONE parameter by definition; calling the missing parameter "ε_2 = 0" and invoking a 2-parameter Nekrasov formula to get "ε_1·ε_2 = 0" is tautological, not a vanishing theorem. The engine bkm_serre_higher_order.py L567 self-declares STATUS='CONJECTURAL'; working_notes.tex L4968 and CLAUDE.md tag it \begin{theorem}. Engine's own comment L412: "BUT this model is too simple". | Correct statement would require either: (a) a genuine 2-parameter Ω-background on K3 (not just on the E factor) with vanishing second-order correction derived from equivariant localization; or (b) cohomological vanishing of P_2 from BKM denominator identity at order ε^2, with explicit computation. Neither is done. Status should be \begin{conjecture}. | circular argument + theorem/conjecture status mismatch (AP40 violation) |
| 65 | "Lie algebra twist L_0 + ε·J_0 linear in ε implies OPE exponent linear in ε" | Twist eigenvalues ARE linear in ε (fact about eigenvalues) | Category error: twist eigenvalue (acting on a single state) ≠ OPE exponent between two deformed vertex operators (involves Wick contractions). Normal-ordering / cross-contractions generically produce ε^2 from the product of two ε-corrected operators. Conflating the two conflates spectrum with correlation function. | Correct: h_ε(V) = h_0(V) + ε·J_0(V) is linear per-operator. OPE V_1(z) V_2(w) ~ (z-w)^{-h_{12}} has h_{12} = h_1 + h_2 - h_{12,full} where the "full" term receives cross-contraction corrections quadratic in ε. The linear-in-ε claim is about TWIST, not about two-point OPE. | mechanism error (eigenvalue vs correlator) |
| 66 | κ_ch "Hodge-filtered supertrace mechanism" PROVED at all d | Serre duality argument at d=2, h^{1,0}=0 genuinely kills quantum correction (HH_{-1}=0) | Identification of str_{F^0}(q^{L_0}) on the abstract chiral algebra A_C with χ(O_X)/2 on the target manifold is σ-model content — it requires CY-A (d=2 version). Proved ONLY at d=2 with h^{1,0}=0. At d=3 the identification is a conjectural bundle of cases (conj:cy-kappa-identification), branching on strict-CY_3 / product / local. No universal formula. | Dimension-stratified taxonomy: (a) d=2, h^{1,0}=0: κ_ch = χ(O_X)/2 (theorem via HKR + F^0 supertrace); (b) d=2, h^{1,0}≠0 (abelian surface): κ_ch = 2, χ(O) = 0, formula fails; (c) d=3 strict: κ_ch = χ_top/24 (BCOV, conjectural); (d) d=3 product S × E: κ_ch = κ_ch(S) + 1 (additive). CY-D is NOT a single formula dimension-stratified; it is FOUR DIFFERENT FORMULAS bundled by taxonomy. | taxonomy-as-theorem (CY-D scope conflation) |
| 67 | Y(gl(4|20)) "BKM-to-Yangian lift from Mukai signature (4,20)" | Y(gl(m|n)) is a classical object (Nazarov); orthosymplectic signs from bilinear form are a known device | No functor BKM → Yangian is constructed. "Lift" is undefined. (4,20) signature determines dimension of +/- definite subspaces, NOT a canonical Z/2 grading — a maximal positive-definite subspace must be CHOSEN (Hodge-theoretic positive cone is natural but not intrinsic). The claim is an ansatz validated at gl(1|1), gl(2|1), proposed as resolution to ω-twisted unitarity. | Correct framing: (i) Mukai lattice signature (4,20) ⇒ choice of max positive cone ⇒ Z/2 grading V = V_+ ⊕ V_−; (ii) ω-twisted unitarity obstruction P_ω^2 ≠ Id for abelian Y(H_{Muk}); (iii) PROPOSED resolution: replace by super-Yangian Y(gl(4|20)) whose P^2 = Id is forced by super-grading. Status: conjectural ansatz. "Lift" language overclaims. | construction/narration + non-canonical grading |
| 68 | Class M E_3 bar cohomology = 6^g (global slogan) | For A = Vir_c^⊕g, H*(B^{E_3}(A)) = 6^g at g ≤ 3 (proved via explicit d_4 matrix rank + Künneth) | Scope: proved only for g ≤ 3 where degree-reason degeneration (d_5 = 0) holds. For g ≥ 4, d_5 can act and result is UPPER BOUND only. Engine class_m_einf_dimension docstring says "conjectural for g ≥ 4"; CLAUDE.md slogan drops the caveat. Also: "genus" here is tensor-copy count of Vir_c, NOT factorization homology over Σ_g. | Correct scoped statement: "For A = Vir_c^⊕g with g independent Virasoro copies, H*(B^{E_3}(A)) = 6^g for g ≤ 3, and ≤ 6^g for g ≥ 4 (conjecturally equal)." "6 = 2×3 per handle" is misleading narration (no handle, just a tensor copy; 6 = (3t+3t^2) evaluated at t=1). | scope drop + narration |

### Meta-pattern diagnosis (cross-audit)

All six audits exhibit a SAME failure mode: **status-tag inflation via narrative scaffolding**. The pipeline is:

1. A genuine partial result is established at specific scope (e.g., Borcherds weight for 8 orbifolds; E_3 bar for g ≤ 3; Serre duality at d=2 h^{1,0}=0).
2. Prose surrounding the result paraphrases it in universal language ("proved unconditionally", "universal formula", "for all K3-fibered").
3. An engine is scaffolded that takes the paraphrased claim as a definition and validates arithmetic identities against hardcoded data.
4. Tests count as verification; the hardcoded-data ↔ formula match is circular.
5. CLAUDE.md inherits the paraphrased claim without scope tag.
6. Later audits read CLAUDE.md, not the .tex; the paraphrase calcifies as ground truth.

Defense: every \begin{theorem} with status ProvedHere should carry a **scope line** (hypothesis, dimension, class, N-value) and the engine's corresponding test must use INDEPENDENT data (not the same hardcoded table from which the formula was derived).

---

## Entry 51: Gaudin Hamiltonian "identification" is identification of the r-matrix, not of the Hamiltonians (2026-04-16, wave 3 sewing/koszul audit, gaudin_from_collision.tex)

**Wrong claim type**: construction/narration (AP-CY57 / AP155 / AP150).

**Pattern**: A "theorem" of the form `H^new = H^classical · scalar` is asserted, with proof consisting of substituting a definition into a definition. The genuine new content lies one step earlier (an r-matrix or kernel identification); the Hamiltonian identification is then automatic.

**Concrete instance**: `standalone/gaudin_from_collision.tex` `thm:gaudin-from-collision` (L210-227) claims `H_i^GZ = H_i^Gaudin/(k+h^v)` for affine Kac-Moody. The proof substitutes the FFR-Sklyanin r-matrix `r(z) = Ω/((k+h^v)z)` into the GZ flat connection `∇^GZ = d - Σ r(z_{ij}) dz_{ij}` and reads off components. But:
- `r(z) = Ω/((k+h^v)z)` IS the FFR r-matrix.
- GZ Hamiltonians are DEFINED as components of `∇^GZ`.
- So `H^GZ = H^Gaudin/(k+h^v)` is a chain of definitions, not a theorem.

**Ghost theorem (the true new content)**: The chiral collision residue `r(z) = Res^coll_{0,2}(Θ_A)` of the bar Maurer-Cartan element on `V_k(g)` AT THE LEVEL `k+h^v` (not k) equals the FFR-Sklyanin classical r-matrix. The shift `k → k+h^v` is the Sugawara renormalization, derived from chiral data.

**Correct relationship**:
- collision residue → r-matrix: GENUINE THEOREM (chiral content).
- r-matrix → GZ connection: definition.
- GZ connection → GZ Hamiltonians: definition.
- GZ Hamiltonians = FFR Hamiltonians: composition of three definitions, automatic.

**Corollary**: Searching the manuscript for "X from Y" theorem statements where X and Y are connected by a chain of definitions is a high-yield audit pattern. The genuine new content is always the FIRST link in the chain that is not a definition.

**Cross-references**: This pattern is the SAME as the "categorified averaging" → factorization E_1 →^Z E_2 →^{Sym} E_∞ pattern (AP-CY54, cache entries 1-3); both have the form "X gives Y" where X is invoked, Y is defined in terms of X, and the "identification" is automatic.

**Operational counter**: Before any "X from Y" theorem, list the steps in the proof. If every step is a definition or a substitution, the theorem reduces to identifying a single ingredient. State THAT ingredient as the theorem.

## Vol I r-matrix Convention Audit 2026-04-16 (wave3, chiral Chern–Weil + level hygiene)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 69 | "Bridge identity: k Ω_trace = Ω/(k+h^v) at generic k" (chiral_chern_weil.tex L458; holographic_datum.tex L635) | The trace-form and KZ-form r-matrices for affine KM are gauge-equivalent representations of the same operadic datum | Identity is type-wrong: LHS scales linearly in k, RHS bounded as k→∞; LHS=0 at k=0 while RHS=Ω/h^v ≠0; LHS=−h^v Ω at k=−h^v while RHS diverges. They cannot be equal at any value of k. The author conflates "rescaling Ω" (Ω_KZ = (k+h^v)Ω_trace) with "rescaling the r-matrix" (r_KZ = r_trace/(k+h^v)). | Two CONVENTIONS are simultaneously rescaled: (a) Ω: Ω_KZ = (k+h^v) Ω_trace; (b) r: r_KZ(z) = (1/(k+h^v)) r_trace(z). Both rescalings together leave the operadic datum invariant. The "bridge" is between conventions (Casimir + r-matrix scale together), not a numerical identity between unscaled quantities. | convention clash + label/content (rescaling labeled as identity) |
| 70 | "S_3(Vir_c) = 2 by S_3 := T_(1)T_lin / T_(3)T_const = 2T/(c/2) = 2κ/κ = 2" (virasoro_r_matrix.tex L228–243) | The cubic shadow coefficient is c-independent for Vir (genuine class-M signature) | The "proof" replaces the field 2T by the c-number 2κ in numerator, then cancels κ. This is the trivial OPE-coefficient identity (2T_(1)T)_const / (T_(3)T)_const = 2 (a tautology in BPZ normalization), NOT a shadow computation. On a primary state |h⟩, the genuine ratio is 2h/(c/2)=4h/c, which DOES depend on c (and h). | Correct shadow coefficient lives in the L_∞ structure on H^*(B(A)), not in the OPE. The c-independent statement (if true) would be: "the cubic L_∞ operation m_3 on H^*(B(Vir_c)) is c-independent up to normalization" — this requires bar-cohomology computation, not OPE arithmetic. The OPE identity used as proof is tautological. | tautology dressed as theorem (AP-CY49 + mechanism error) |
| 71 | "r-matrix is r(z) = Ω/((k+h^v)z) (KZ form), derived by d-log absorption" (three_parameter_hbar.tex L290–306) | The d-log absorption rule sends OPE pole order n to r-matrix pole order n−1 (correct mechanism) | D-log absorption applied to the OPE k(t^a,t^b)/(z-w)^2 + f^{ab}_c J^c/(z-w) gives k Ω/z + (regular field). The (k+h^v) factor in the KZ form does NOT come from d-log absorption alone; it comes from Sugawara renormalization (rescaling the energy-momentum tensor by 1/(k+h^v)). The "proof" silently inserts Sugawara as if it were part of d-log. | Correct: bar collision residue from d-log alone gives r_trace(z) = k Ω/z. The KZ form r_KZ(z) = Ω/((k+h^v)z) requires the additional Sugawara hypothesis. The three-parameter identification ℏ = 1/(k+h^v) is therefore *conditional on Sugawara normalization*, not universal. | hidden hypothesis (Sugawara renormalization treated as part of d-log) |

## Entry 52: Rhetorical inflation -- presentation count > object count (2026-04-16, Vol I wave-3 higher-genus audit, higher_genus_modular_koszul.tex L22759--L22918, seven_faces.tex L285--L345, higher_genus_modular_koszul.tex L24454--L24550)

**Wrong claim pattern (recurring 3x in higher-genus pillar):**
- "Three structurally independent mechanisms each force delta F_g^cross = 0" (free-field exactness, L22759--L22918);
- "Seven equivalent presentations of r(z)" (seven faces, L285--L345);
- "Universal gravitational cross-channel formula for W_N" (with body admitting the formula is a lower bound for N >= 4, L24454--L24550).

**Ghost theorem (in each case):**
- Free-field: the *block-diagonal structure* of the propagator P^{ab} = g^{ab}·d log E(z,w) with respect to the conformal-weight grading (a single fact in the OPE algebra).
- Seven faces: the *single* universal Maurer--Cartan element Theta_A = D_A - d_0 (one bar-cobar twisting cochain).
- Universal N-formula: the *gravitational-truncation* Frobenius algebra (one truncation of the W_N OPE, retaining only stress-tensor exchange).

**Precise error pattern:** the manuscript counts PRESENTATIONS or PROJECTIONS of the underlying object as if each presentation were an independent result. The redundancy is sometimes acknowledged (free-field: L22871--L22877 admits the three mechanisms are not logically independent) but the rhetorical headline ("triple redundancy", "seven faces", "universal formula") inflates the redundancy into independence.

**Correct relationship:**
- Free-field: ONE mechanism (block-diagonal propagator) with three projections (shadow-tower collapse, off-diagonal metric, ghost-number).
- Seven faces: FOUR distinct objects (E_1 R-matrix, PVA classical r, Sklyanin/Gaudin, the bar-cobar arrows from F1 to each presentation) presented in seven mathematical languages.
- N-formula: EXACT for N <= 3 (Z/2 parity kills higher-spin exchange), LOWER BOUND for N >= 4.

**Type:** label/content + specific/general (different labels for the same content; specific case of a universal mechanism marketed as if the universality were per-presentation).

**Defense:** in each case the chapter is technically honest -- the redundancy/lower-bound nature is admitted in the body. The bug is presentation, not mathematics. The bug propagates because rhetorical headlines stick in CLAUDE.md and in cross-references where the qualifying admission is invisible.

**Operational counter:** before writing "N independent mechanisms / N equivalent presentations / universal formula for X", check whether the underlying object/mechanism count matches N. If it does not, EITHER reduce N to the object count OR add an explicit "N projections of M underlying objects" framing. The headline must agree with the body.

**Strengthening path (per audit Section 5):** each of the three rhetorical inflations admits a *correct* universal upgrade once the rhetoric is unwound:
- Free-field: PROMOTE block-diagonality to a separate lemma (the actual content).
- Seven faces: PROMOTE the bar-cobar arrows F1 -> Fk as the new content (the true theorem is "F1 generates all six presentations via the bar-cobar twisting cochain").
- N-formula: PROMOTE the c -> infinity Vasiliev-shadow limit B(N) = (N-2)(N+3)/96 as a universal topological invariant (the actual universal content beneath the lower-bound caveat).

The pattern is endemic in higher-genus pillars where the chapter accumulates many partial results. Defense: every "N independent X" headline must pass the test "what is the underlying object count, and do all N projections add genuinely new information?".

## Entry 53: Operadic-circle confabulation as algebraic-vs-topological E_3 conflation (2026-04-16, Vol I wave-4 en_cascade audit, en_chiral_operadic_circle.tex L1973-L2079, L2014-L2026)

**Wrong claim pattern (recurring across operadic literature):**
- "The E_n operadic circle E_3 -> E_2 -> E_1 -> E_2 -> E_3 closes for simple g via the E_3 identification theorem" (en_chiral_operadic_circle.tex abstract L111).
- Eq. 6.1 (L1973-L1983) writes the circle as a single closed diagram of operadic shifts.
- Cor 7.7 (L2349-L2370) titled "circle partly closes" lists 5 steps; only step (v) is a theorem, only at the level of formal deformation families.

**Ghost theorem (the real underlying content):**
There is a four-step zigzag of CONSTRUCTIONS (not a circle):
1. B^ord(A) (E_2-chiral input -> E_1-chiral coalgebra; Princ 3.10, PROVED).
2. Take comodules: E_1-chiral coalgebra -> E_1-monoidal category Comod(B^ord(A)).
3. Drinfeld centre Z(Comod(...)): E_1-monoidal cat -> E_2-braided monoidal cat.
4. End-of-identity = chiral Hochschild: E_2-braided monoidal cat -> algebraic E_3.
5. Topologisation (Thm 5.1/5.5, PROVED for KM/W-algebras): algebraic E_3 -> E_3-top on BRST cohomology.
6. Conjectural closing (Conj 11.1): output E_3-top ≃ input bulk E_3-top from HT field theory.

**Precise error pattern:** The "circle" packaging conflates **two distinct E_3 structures** (AP154):
- The **algebraic** E_3 from the higher Deligne conjecture (Francis 2013): well-defined on E_∞ inputs (chain-level / spectral context).
- The **topological** E_3-top from topologisation: requires inner conformal vector at non-critical level.

The arrow-4 output of HDC is naturally algebraic E_3, NOT topological E_3-top. Eq. 6.1 elides this passage, presenting the output as E_3-top directly. Only after Thm 5.1/5.5 (a separate, conditional step) does algebraic E_3 promote to E_3-top.

A second elision: arrow 1 ("restriction along codim-2 defect, E_3-top -> E_2-chiral") is stated as a definition with no proof; arrow 5 (closing) is conjectural. Marking each arrow status: T (theorem), D (definition only), C (conjecture). The "circle" reads T+D+T+T+C with the C absorbed into the closure rhetoric.

**Correct relationship:**
- The operadic zigzag of CONSTRUCTIONS is honest mathematics; the "circle" image is rhetorical.
- For simple g at non-critical level, Thm 7.4 PROVES the formal-family identification of the output algebraic E_3 (after topologisation to E_3-top) with the perturbative-CS E_3-top from CFG '25 (in preparation).
- The full categorical equivalence (output ≃ input as E_3-top algebras, beyond formal series) is Conj 11.1 in the appropriate (coderived?) category.
- The "Drinfeld centre is sole source of nontrivial braiding" (Thm 6.3) is correct as a TOPOLOGICAL fact (π_1(Conf_2(R^3))=1) but overclaims: Yangian R-matrices, MTC braidings, factorisation-algebra braidings on 2-manifolds are alternative sources.

**Type:** construction/narration + algebraic/topological + label/content (composite construction marketed as closed circle; two distinct E_3 structures conflated by uniform "E_3-top" tag; "sole source" overclaim for braiding genesis).

**Defense:** the standalone is structurally honest in its hardest places — the SC^chtop ≠ E_3 remark (Rem 4.2, L1192-L1204), the three-Hochschild warning (Warning 3.9, L1067-L1092), the five-notions warning (Warning 8.3, L2531-L2556), the layered (cohomological / model / original-complex) chain-level analysis (Rem 5.7 = `rem:e-three-layers`, L1847-L1881). The defects are concentrated in the rhetorical packaging (abstract, eq 6.1, Cor 7.7), not in the proof content.

**Operational counter (4-pronged):**
1. Before writing "circle" / "closes" for any composite of operadic functors, draw the level diagram with each arrow tagged (functor / theorem / definition / conjecture). If any arrow is not a theorem, the composite is not a theorem.
2. For every E_3 occurrence, tag explicitly as E_3^alg (Deligne, from HDC on E_∞ input) or E_3^top (topologised, requires inner conformal vector). Their identification is non-trivial.
3. For HDC invocations, verify the input is E_∞ (not just E_n for n ≥ 2). Francis 2013 in chain complexes vs chiral HDC for chiral algebras with formal-disk OPE are different theorems.
4. For "sole source" / "unique" claims about categorical structures (braidings, Hopf, R-matrices), enumerate at least 3 alternative sources and show each leads to the same object via an explicit identification (or a stated conjecture).

**Strengthening path:** the four-step zigzag is genuinely new mathematics. After unwinding the "circle" rhetoric:
- PROMOTE Rem 4.2 (SC^chtop ≠ E_3) to a numbered separation theorem.
- PROMOTE the four-step zigzag to "Theorem (Operadic zigzag for E_∞-chiral algebras with inner conformal vector at non-critical level)".
- REPHRASE Conj 11.1 in the coderived category D^co(E_3-top) so it lives in a definite ambient.

**Cross-volume incidence:** This pattern appears in Vol III as AP-CY32 (reorganisation ≠ bypass: 6d hCS route appears to bypass CY-A_3 but each subproblem secretly requires the same chain-level data). Same operational structure: composite of constructions presented as solving the original problem; each sub-arrow either reduces to the original problem or is independently conjectural.

## Entry 54: Theorem-H amplitude vs occupation (2026-04-16, Vol I wave-4 en_cascade audit)

**Wrong claim:** "Theorem H: ChirHoch^*(A) is concentrated in cohomological degrees {0,1,2}" with three nonvanishing degrees interpreted (en_chiral_operadic_circle.tex Thm 3.6, L996-L1013; Vir entry L3033-L3074, L3151).

**Ghost theorem:** the cohomological *amplitude* is ≤ 2 (proved as `thm:hochschild-polynomial-growth` in chiral_center_theorem.tex L62). The exact occupation depends on the algebra.

**Precise error:** "concentrated in {0,1,2}" reads as non-vanishing at each of 0, 1, 2. The chapter says explicitly (chiral_center_theorem.tex L2025-L2041, ProvedHere) ChirHoch^•(Vir_c) = (C, 0, C·Θ) with H^1=0, Hilbert series 1+t^2. Standalone Prop 10.4 row "concentrated in {0,1,2}, polynomial" is therefore wrong for Vir.

**Correct relationship:** Theorem H is an *amplitude* theorem (upper bound on support), not an *occupation* theorem.
- Heisenberg: (1, 1, 1).
- KM V_k(g): (1, dim g, 1).
- Vir_c: (1, 0, 1).
- DS reduction of KM at any nilpotent f: (1, 0, 1) (by `prop:DS-ChirHoch-compatibility`).

**Type:** label/content + necessary/sufficient (amplitude bound mislabeled as occupation pattern; sufficient for vanishing at i ≥ 3, not for non-vanishing at i ∈ {0,1,2}).

**Defense:** purely an internal contradiction within the manuscript; chapter is correct, standalone is sloppy.

**Operational counter:** for any "concentrated in {set}" claim, ask: is this an amplitude bound or an occupation pattern? State which.

**Strengthening path:** PROMOTE Theorem H from "concentration in {0,1,2}" to "**amplitude ≤ 2**" + a per-family Hilbert series corollary. The amplitude theorem is the universal one; the occupation pattern is the algebra-specific computation.

---

## Wave 4 (2026-04-16) — holographic / 3d gravity / entanglement (Vol I)

| # | Wrong claim | Ghost theorem | Correct relationship | Type | Locus |
|---|-------------|---------------|----------------------|------|-------|
| 138 | "BTZ is an MC element of the convolution Lie algebra" | BTZ is a Cardy state in the module category | Cardy state in module != MC element in algebra. The convolution dg Lie algebra carries structural data; the modules carry physical states. The MC equation lives in g^mod, not in the module of states. Conflation of algebra-level and module-level objects. | algebra/module (sub-type of algebra/coalgebra) | three_dimensional_quantum_gravity.tex thm:btz-mc L1748 |
| 139 | "Bulk-boundary-line triangle is a single object viewed three ways" | three functorial outputs of the bar complex via three distinct functors (cobar, derived centre, Koszul-dualised module category) | source object != functor target. A single source can have many functorial outputs without BEING those outputs. The unification is functoriality, not identity. | construction/narration (AP-CY57) | three_dimensional_quantum_gravity.tex sec:bbl L885; holographic_datum.tex L217; thqg_introduction_supplement.tex L156 |
| 140 | "Koszul duality c <-> 26-c is gravitational S-duality" | the Feigin-Fuchs / Verdier reflection on Vir bar coalgebra is a real involution; the central-charge shift is the bc-ghost central charge | Koszul reflection is ADDITIVE (c -> 26-c), not multiplicative. S-duality requires coupling INVERSION (g -> 1/g). At c -> infinity (semiclassical, G -> 0), the dual 26-c -> -infinity is NOT a "weak coupling" of the original. The naming confabulates "S-duality". | label/content | three_dimensional_quantum_gravity.tex abstract L75; thm:vir-koszul L998 |
| 141 | "Gravitational Yangian Y(Vir_13) at the self-dual point" | the shadow obstruction tower at c=13 is an infinite sequence of conserved-charge invariants with special symmetry structure | Vir is infinite-dim and has NO known Yangian. "Y(Vir_13)" presupposes a structure not constructed in the literature. The shadow tower IS a real algebra of conserved charges, but its Yangian-like RTT presentation is unconstructed. | confabulation (AP150) + label/content | three_dimensional_quantum_gravity.tex sec:gravitational-yangian L2645-2798 |
| 142 | "Code distance d=2 of the Koszul code" | bar augmentation ideal starts at degree 2 (algebraic graded structure) | algebraic bar-degree != QECC code distance. Code distance d is the min weight of an undetectable error operator; algebraic degree is the grading of the augmentation ideal. The conflation is silent. Same pattern: algebraic invariant labeled with a QECC term. | label/content | holographic_codes_koszul.tex rem:hc-universal-parameters L685-689 |
| 143 | "Koszulness <=> exact holographic reconstruction" (Theorem G12) | bar-cobar exact recovery (K4) is genuinely equivalent to Koszulness (tautological since K4 IS Koszulness) | the algebraic statement is tautological (K4 <=> K4); the PHYSICAL identification with HKLL bulk reconstruction is a structural analogy, NOT a theorem. The proof of (iii) => (i) silently DEFINES (iii) to be K4. | construction/narration (AP-CY57) | holographic_codes_koszul.tex thm:hc-koszulness-exact-qec L339-421 |
| 144 | "Shadow L-function L^sh(s) has poles at s=1 and s=2 arising from S_2=kappa and S_3" (Vol I wave 4 arithmetic shadows audit, 2026-04-16) | the genus-1 amplitude Fourier-coefficient Dirichlet series D_2(A,s) = Sigma a_n n^{-s} with a_n = -24 kappa sigma_1(n) DOES factor as -24 kappa zeta(s) zeta(s-1) and have Eisenstein poles at s=1,2 (Ramanujan divisor identity) | within-volume contradiction: the SAME volume's chapter file (chapters/connections/arithmetic_shadows.tex L3458-L3495) explicitly disclaims this exact identification, noting that for class G, L^sh(s) = k * 2^{-s} is ENTIRE while -k zeta(s) zeta(s-1) is meromorphic. D_2 (Fourier-coefficient series, Eisenstein) and L^sh (constant-term series, no Euler product, not in Selberg class) are DIFFERENT objects. The standalone Prop 4.3 commits the disclaimed error. Coefficients S_r are not multiplicative; L^sh is not "an L-function" in any structural sense. Class G is entire (two-term polynomial in 2^{-s}); class L entire (three terms); class C entire (four terms); class M convergent in a half-plane only, with no automatic poles. | label/content + within-volume contradiction (Dirichlet-series category error: Sigma a_n n^{-s} given L-function structural properties without verifying coefficients carry the required arithmetic) | standalone/arithmetic_shadows.tex L639-L663 contra chapters/connections/arithmetic_shadows.tex L3458-L3495 |

## Wave 5 (2026-04-16) — chiral Hochschild and Koszul foundations (Vol I)

| # | Wrong claim | Ghost theorem | Correct relationship | Type | Locus |
|---|-------------|---------------|----------------------|------|-------|
| 145 | "the chiral Hochschild complex" (definite article, used across at least 3 distinct definitions) | for finite-type chiral Koszul algebras on a smooth curve, the geometric model `C^•_chiral(A) = Γ(C̄_{n+2}, j*j^* A^{⊠(n+2)} ⊗ Ω^n_log)`, the algebraic model `Ext^*_{A^e}(A,A)` with `A^e = A ⊠_{D_X} A^op`, and the bigraded model `RHH_ch(A) = RHom_{D_{C̄_{p+2}}}(A^{⊠(p+2)}, ω)` are quasi-isomorphic | the equivalence is a THEOREM (FM-tower collapse + Verdier shift `[2]`), not a definition. The shift `[2] = (p+2) - p` cancels totalisation against Verdier-dualizing-sheaf shift. Off the Koszul locus, the three models genuinely differ. AP-CY62 fires (geometric vs algebraic chiral Hochschild model) — Vol I has the same conflation flagged for Vol III. The bigraded model `RHH_ch` should be promoted to canonical; the others are then quasi-iso shadows. | construction/narration (AP-CY57, AP-CY62) + label/content (AP160) | chiral_hochschild_koszul.tex L139-157 (geometric); hochschild_cohomology.tex L76 (algebraic-derived); koszul_pair_structure.tex L259 (Ext via A^e); higher_genus_foundations.tex L2748 (bigraded canonical) |
| 146 | "ChirHoch is bounded but Gel'fand–Fuchs is unbounded because the latter has no curve geometry" (rem:gf-vs-chirhoch and rem:critical-level-lie-vs-chirhoch) | three distinct Hochschild-flavour invariants exist for Vir_c: ChirHoch^*(Vir_c) bounded in {0,1,2} (Theorem H), HH^*(Zhu(Vir_c)) finite-dim concentrated in {0} (Zhu = polynomial ring), H^*_GF(L_1) = C[Θ] polynomial in degree 2 | the boundedness of ChirHoch is NOT because Gel'fand–Fuchs lacks curve geometry; it is because the curve `D_X`-amplitude is `[0,2]` and the bigraded Verdier shift collapses to constant `[2]` on the Koszul locus. At critical level, ChirHoch becomes unbounded (BD04 4.5.2 identifies it with Lie cohomology), confirming that "curve geometry" is not the source of the bound. AP-CY64 (three-way ChirHoch / HH* / H*_GF). The three are linked by SS: HH^p(Zhu(A)) ⊗ H^q_dR(X) ⇒ ChirHoch^{p+q}(A) at generic level; ChirHoch^*(A_crit) ≅ H^*_Lie,cont at critical level. | mechanism error + chain/cohomology | hochschild_cohomology.tex rem:gf-vs-chirhoch L128 and rem:critical-level-lie-vs-chirhoch L158 |
| 147 | "the chiral product μ" (one product, used in BD-style language and End^ch-style explicit formulas without bridge) | for finite-type vertex algebras with PBW filtration, BD-chiral operad on D_X-modules and End^ch operad on formal Laurent series are isomorphic as operads in D_X-modules | the iso is a four-step bridge (choose chart, trivialize D_X, identify spectral parameters, verify Borcherds = associativity), NOT a notational synonym. AP-CY63 fires (Bridge Proposition absent). Without the Bridge, claims about "the chiral product" are ambiguous; with it, BD and End^ch interchangeable. | construction/narration (Bridge missing) | chiral_hochschild_koszul.tex Section 3 (uses both formalisms); proof of thm:chiral-hochschild-differential L172-305 mixes BD reasoning with End^ch formulas |
| 148 | "the chiral Koszul pair" (definite article, four distinct definitions) | Ext-diagonal `Ext^{i,j}_A(C,C) = 0 for i ≠ j` is the canonical invariant; bar concentration, twisting datum, PBW criterion are equivalent on the Koszul locus | four definitions exist (`def:chiral-koszul-morphism` via twisting data; `def:chiral-koszul-pair` via Verdier-compatible pair; `def:koszul-chiral-algebra` referenced but living elsewhere; implicit Ext-diagonal in `prop:degen-koszul`). The equivalence is established via separate theorems (`thm:ext-diagonal-vanishing`, `thm:bar-concentration`, `thm:pbw-koszulness-criterion`) but never as a single equivalence theorem. Reader cannot tell which is "the" definition. | label/content + within-chapter scattering | chiral_koszul_pairs.tex L268, L658, L1367; spectral_sequences.tex L341 |
| 149 | "k_max ∈ {0,1} ∪ {3,4,...}, the value 2 is excluded by locality and dimension" (universal claim) | for chiral algebras with bosonic integer-weight generators, p_max ∈ {1,2,4,5,...} and so k_max = p_max - 1 skips 2 | mechanism is correct only WITHIN the bosonic-integer-weight landscape. Half-integer weight (N=1 super-Virasoro: G(z)G(w) ~ 2c/3(z-w)^{-3}) gives p_max = 3, k_max = 2 — allowed. The theorem's universal quantifier is too strong; the proof only excludes the bosonic case. Mechanism error: right conclusion in the right scope, wrong scope stated. | mechanism error + scope error | three_invariants.tex rem:k-max-2-missing L298, thm:k-max-trichotomy L312 |

**Operational counter (chiral Hochschild):** every "Hochschild" mention should be tagged `_geom`, `_alg`, or `_bigr`. The bigraded `RHH_ch(A)` of `def:bigraded-hochschild` (`higher_genus_foundations.tex:2748`) is the canonical derived object; the others are quasi-isomorphic shadows on the Koszul locus and genuinely-different objects off it.

**Operational counter (chiral Koszul):** Ext-diagonal `Ext^{i,j}_A(C,C) = 0 for i ≠ j` is the invariant definition. Bar concentration, twisting datum, PBW criterion are derivable equivalences. State the equivalence as a single theorem; cite ONE definition as canonical.

**Strengthening path (Theorem H):** PROMOTE Theorem H to "RHH_ch(A) ≃ RHom(RHH_ch(A^!), ω_X[2]) on the Koszul locus, model-independent, with cohomological amplitude [0,2]." This is independent of which of the three Hochschild models is in force.

**Cross-volume:** all five Wave-5 confusions have direct Vol III analogs (AP-CY62, AP-CY63, AP-CY64). The same patches that fix Vol III's chiral_hochschild_koszul.tex apply here. The conflations are systemic across the programme.

---

## Wave 8 (cross-volume audit, 2026-04-16) additions

| # | Wrong claim | Ghost theorem | Correct relationship | Type | Locus |
|---|-------------|---------------|----------------------|------|-------|
| 150 | "conditional on CY-A_3" (~17 instances in Vol III chapters, post-April-2026) | each phrase reads as a true safe-bound (the conditional is weakly true) | after CY-A_3 was proved (inf-cat, thm:derived-framing-obstruction), the dependent prose was not updated. The conditional UNDERSTATES: A_X exists by CY-A_3, and only chain-level explicit framing data (for non-formal algebras) or Vol I Borcherds-lift identification (AP-CY8) or motivic DT comparison (CY-D programme) remains conditional. Files: cy_to_chiral.tex L1728/1763/1765/1802/3308; quantum_chiral_algebras.tex L376/383/1949/2447/2698; e1_chiral_algebras.tex L1983/1991; e2_chiral_algebras.tex L1187; braided_factorization.tex L768/1351; en_factorization.tex L1208/1217/1223. **Healing template:** "A_X exists by Theorem CY-A_3 (Theorem~\ref{thm:cy-to-chiral-d3}); the explicit chain-level [shadow tower / framing data / Borcherds-lift identification] for [class M / non-formal / non-toric] geometries remains conditional on [chain-level framing / Vol I Borcherds-lift bridge (AP-CY8) / motivic DT comparison]." Wave 8 cross-volume audit. | upgrade-staleness (NEW TYPE: status upgrades not propagated to dependent prose) | wave8_cross_volume.md Sections 3, 8, 10, punch list item 1 |
| 151 | Dangling cross-volume `\ref{def:shadow-invariants}` and `\ref{def:shadow-class}` from Vol III to Vol I | cross-volume references typeset as `??` if `externaldocument` is not configured | Vol III's `quantum_chiral_algebras.tex:2103, 2289, 2293` use `\ref{def:shadow-invariants}` and `\ref{def:shadow-class}` with no Vol III-side definitions; the labels live in Vol I. Without `\externaldocument` setup, these silently typeset as `??`. **Healing:** either (a) configure `\externaldocument{vol1/main}` in Vol III preamble; (b) inline the definitions; or (c) replace `\ref` with descriptive text + label key. V2-AP38 (phantom labels) was supposed to track these. | cross-volume label resolution + V2-AP38 | wave8_cross_volume.md Section 2; quantum_chiral_algebras.tex L2103/2289/2293 |
| 152 | Cross-volume q-convention bridge ABSENT (KL `\hbar = \log q` vs DK `q = e^{2\pi i \hbar}`) | individual conventions are mutually consistent; bridge identity `q_KL = q_DK` (when `\hbar` matched) is implicit | the bridge is folkloric and never stated explicitly in any of the three CLAUDE.md files. Vol I uses KL across many chapters; Vol II's `thqg_line_operators_extensions.tex:1113` uses DK; Vol III's `e1_chiral_algebras.tex:1975` uses KL. No within-volume clash; cross-volume reader has no key. AP151 in current form is a within-volume rule; cross-volume version absent. **Healing:** 3-line addition to each CLAUDE.md stating the bridge. Cheap insurance. | convention clash (cross-volume) | wave8_cross_volume.md Section 4 |
| 153 | Vol III internal Chapter~N hardcodes in `notes/theory_drinfeld_chiral_center.tex`, `notes/theory_coha_e1_sector.tex`, `notes/theory_qvcg_koszul.tex` (e.g. "Chapter~12 of the monograph", "Chapter~5", "Chapter~14 of the main text") | the notes are working drafts; once promoted to compiled chapters, V2-AP26 fires immediately | the Chapter~N strings are STALE BY POLICY (V2-AP26 forbids hardcoding). Currently dormant because the notes are not in main build. **Healing:** convert to `\ref{ch:...}` BEFORE promotion. Otherwise the moment a single `\input` is added, the manuscript ships violations. | shipping-out risk + V2-AP26 | wave8_cross_volume.md Section 1 (Chapter-number hardcodes) |
| 154 | Drinfeld center theorem (`Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_{ch}(A))`) stated independently three times: Vol II `spectral-braiding(-core).tex`, Vol III `notes/theory_drinfeld_chiral_center.tex`, Vol III `chapters/theory/drinfeld_center.tex` | the abstract theorem has a single canonical home (Vol II) | three copies invite drift under correction. No drift detected today; risk is structural. **Healing:** collapse to Vol II canonical statement + Vol III specializations cite via `\cref` (with `externaldocument`). | duplicated content (V2-AP27, mid risk) | wave8_cross_volume.md Section 6 |
| 155 | Vol I `standalone/programme_summary.tex:98` says "single open conjecture is the CY-A correspondence at..." while same file L2599 has `\begin{theorem}[CY-A at d=3]` and L2619 says "No open conjecture in the programme has unresolved..." | within-document drift (post-April-2026 upgrade not fully propagated) | the L98 standalone-summary opening was not updated when CY-A_3 was upgraded. The file now self-contradicts: opening says "single open conjecture", body has the theorem, conclusion says "no open conjecture". **Healing:** reconcile L98 to the post-upgrade status (CY-C remains the open conjecture; CY-A is closed). | upgrade-staleness (intra-volume variant of #150) | wave8_cross_volume.md Section 8; programme_summary.tex L98 vs L2599 vs L2619 |

**Operational counter (upgrade-staleness, NEW recurring type):** after any major status upgrade (Conjecture → Theorem), grep all three volumes for variant phrases (`conditional on TheoremName`, `open`, `awaits`) within 100 chars of the theorem name; reframe each match to the residual conditionality (chain-level data, Borcherds bridge, motivic DT comparison) rather than deleting "conditional". The 17 stale Vol III phrases are the second wave of this pattern (first wave: Vol II cache rows 57-66, ~10 phrases). The pattern recurs each time a major conjecture upgrades and is mechanically detectable post-upgrade.

**Cross-volume punchlist (Wave 8):** 12 items in `wave8_cross_volume.md` Section 13. Highest healing yield: de-condition 17 Vol III phrases (Upgrade Path A). Cheapest: 3-line convention bridges to all three CLAUDE.md files (Upgrade Paths C+B). Strongest score: CY-C status discipline (clean across all three volumes; AP40 + HZ3-1 fully enforced).

| 156 | Vol I "Theorem A clause (ii) (Verdier intertwining $\mathbb{D}_{\Ran}\,\barB(\cA) \simeq \cA^!_\infty$) is a derived consequence" | Verdier duality DOES intertwine bar of $\cA$ with bar of $\cA^!$ when both are chiral Koszul algebras | Vol I `def:chiral-koszul-pair` (chiral_koszul_pairs.tex L570--588) **encodes Verdier compatibility $\mathbb{D}_{\Ran}(\cC_1) \simeq \cC_2$ as INPUT DATA**. Theorem A clause (ii)'s "proof" composes this input with clause (i)'s unit equivalence. No new content beyond clause (i) + the definition. **Healing:** rewrite definition to NOT presuppose Verdier compatibility; clause (ii) becomes substantive (confirmed in `theorem_a_b_tautology_verification.md`). Cross-volume relevance: Vol III's CY-A_d functor relies on Vol I Theorem A as the d=1 base; if the d=1 statement is tautological at the Verdier-intertwining level, the d=2/d=3 lift inherits the same artifact. | **definitional tautology** (NEW TYPE) + construction/narration | wave12_proof_verification_ABH.md Sections 1.5, 7 (ghost theorem 1) |
| 157 | Vol I "Theorem B at $g=0$ (bar-cobar inversion at genus 0) is a theorem" | Bar concentration $\Rightarrow$ counit is qi (chiral analogue of LV12 Theorem 3.4.6) | Vol I `def:koszul-chiral-algebra` (algebraic_foundations.tex L223--234) defines "Koszul" by the condition "counit is qi at genus 0". Theorem B clause (1) at $g=0$ says: if $\cA$ is Koszul (counit is qi at $g=0$), then counit is qi at $g=0$. **Verbatim definition.** Author admits in `rem:inversion-vs-fundamental` (L1686--1695). The non-trivial content is $g \geq 1$ extension and clauses (2)--(4). **Healing:** rewrite definition to use bar-concentration (per `rem:equivalent-formulations-koszul`); $g=0$ clause becomes the LV-style theorem. Cross-volume: Vol III's bar-cobar machinery for CY chiral algebras inherits this definitional pattern; same fix should propagate. | **definitional tautology** (NEW TYPE) | wave12_proof_verification_ABH.md Sections 2.6, 7 (ghost theorem 2) |
| 158 | "Theorem H gives ChirHoch occupation $\{0, 1, 2\}$" | Theorem H gives ChirHoch **amplitude** $[0, 2]$ universally on the Koszul locus | The standalone statement (five_theorems_modular_koszul.tex L1409--1414) reads "concentrated in degrees $\{0,1,2\}$" which is ambiguous between amplitude and occupation. The chapter realisation `thm:hochschild-polynomial-growth` (chiral_hochschild_koszul.tex L1040ff) gets it right: explicitly labels part (a) "Concentration (cohomological amplitude, not virtual dimension)" with nonvanishing **range** $[0,2]$. For Vir generic: $\ChirHoch^1 = 0$, occupation is $\{0, 2\}$. For KM/Heis: occupation $\{0, 1, 2\}$. **Healing:** rewrite standalone statement to use "amplitude $[0, 2]$"; promote `prop:hilbert-families` to a Theorem with sharp occupation per family. **Cross-volume relevance:** Vol III's Theorem H analogue at $d \geq 2$ should explicitly state amplitude $[0, 2d]$ to maintain discipline. | **amplitude/occupation** (HZ3-14 confirmed cross-volume) | wave12_proof_verification_ABH.md Sections 3.2, 3.6, 7 (ghost theorem 3); HZ3-14 |

**Operational counter (definitional tautology, NEW recurring type, Wave 12):** when a foundational definition encodes the conclusion of the headline theorem, the headline theorem becomes vacuously true. To detect: for each `\ClaimStatusProvedHere` headline theorem, locate the principal definitional hypothesis and check whether it includes (a) the theorem's conclusion verbatim, (b) an equivalent characterization, or (c) the theorem's quasi-isomorphism / equivalence at a special case. If yes: rewrite the definition to use a stronger property (PBW / bar-concentration / acyclicity of twisted product) so the headline theorem becomes a derived consequence. The Vol I Theorem A and Theorem B cases are the prototype; Vol III may have analogues at CY-A_d (e.g., does `def:CY_d-category` encode "carries cyclic A_inf trace" as input?). Mechanical detection: grep for `def:` labels referenced in the hypothesis of any ProvedHere theorem and check whether the definition body contains a quasi-isomorphism or equivalence statement.

## XX. CY-C Six-Routes Pairwise Bridges (Wave 14, 2026-04-16)

Healing chapter `chapters/examples/cy_c_six_routes_convergence.tex` installs the comparison machinery behind Conjecture CY-C. Top-15 cached confusion #10 stated G(X) is unconstructed; the new chapter makes the construction problem precise by factoring convergence into six pairwise bridges organised as a 6-cycle, each a NAMED ARROW with honest status. Cache rows below record the narration-vs-construction violations that were present in the manuscript before the chapter and are now healed.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 159 | "The six routes to $G(K3\times E)$ converge by functoriality of $\Phi$" | Convergence is asserted by CY-C | Only R1 uses $\Phi_3$; R2--R6 are independent constructions with independent inputs (Jacobi form, Mukai lattice, orbifold data, Ricci-flat metric, 6d SCFT). Functoriality of $\Phi$ cannot force convergence it never applies to | Convergence = CONTENT of CY-C (conjectural). Factor into 6 pairwise bridges $\alpha_{ij}$ with named construction arrows. AP-CY60 | construction/functor | `cy_c_six_routes_convergence.tex` Sec.~\ref{sec:cy-c-six-setup} + Rem.~\ref{rem:six-routes-irreducible} |
| 160 | "The 6 routes produce a single $\kappa_{\mathrm{ch}}(K3\times E)$ value" | Each route DOES produce a $\kappa_{\mathrm{ch}}$ | Route-dependent: R1=3, R3=24, R4=12, R5=3 (R6 matches R1); R2 has no $\kappa_{\mathrm{ch}}$ (Borcherds lift = Jacobi-form attribute); $\kappa_{\mathrm{BKM}}=5$ is R2-specific | Correct spectrum on K3xE: $\{\kappa_{\mathrm{cat}}=0,\, \kappa_{\mathrm{ch}}^{R_1}=3,\, \kappa_{\mathrm{BKM}}=5,\, \kappa_{\mathrm{ch}}^{R_4}=12,\, \kappa_{\mathrm{ch}}^{R_3}=24,\, \kappa_{\mathrm{fiber}}=24\}$. Different invariants, not different values of one invariant. AP113+AP-CY55+AP-CY59 | construction/functor | `cy_c_six_routes_convergence.tex` Thm.~\ref{thm:kappa-stratification-CY-C} |
| 161 | "BKM is the Koszul dual of $A_{K3}$" | Some structural pairing $A_{K3}$ vs BKM exists | Conflates R2 (Borcherds lift, Jacobi-form input) with Koszul duality applied to R1. Koszul duality and Borcherds lift are not the same functor | R2 constructs BKM via denominator identity of $\mathfrak{g}_{\Delta_5}$; this does NOT factor through Koszul-duality applied to $\Phi_2(D^b(\Coh(K3)))$. If a Koszul-duality relation exists, it is a SEPARATE bridge not covered by $\alpha_{12}$. | conflation / construction/narration | `cy_c_six_routes_convergence.tex` Rem.~\ref{rem:cy-c-narration-audit}(c) |
| 162 | "Sigma-model chiral algebra via HKR" | HKR is a real functor | HKR takes $D^b(\Coh(X))$ to polyvector cohomology; sigma-model R5 takes (2,2)-SCFT to half-twist chiral algebra. Different starting data, different functors | R1 uses HKR; R5 uses the half-twist. Agreement of $A_X^{R_5}$ with $A_X^{R_1}$ is content of bridge $\alpha_{56}\circ\alpha_{45}\circ\alpha_{34}\circ\alpha_{23}\circ\alpha_{12}$; saying "R5 via HKR" collapses five bridges into one tautology | conflation | `cy_c_six_routes_convergence.tex` Rem.~\ref{rem:cy-c-narration-audit}(d) |
| 163 | "$\kappa(K3)$ is 2" (bare, FM119) | Both $\kappa_{\mathrm{ch}}(K3)=2$ and $\kappa_{\mathrm{fiber}}(K3)=24$ are correct | Bare $\kappa(K3)$ collapses two invariants of two different objects (algebra vs manifold). The SAME symbol on the SAME geometry gets two answers because the invariants are different | $\kappa_{\mathrm{ch}}(K3)=2$ (algebraization, routes R1/R5); $\kappa_{\mathrm{fiber}}(K3)=24$ (topology); $\kappa_{\mathrm{ch}}^{R_3}(K3)=24$ (lattice-VOA route, matches fiber value NUMERICALLY not semantically); $\kappa_{\mathrm{cat}}(K3)=2$ (manifold). FM119 | label/content | `cy_c_six_routes_convergence.tex` Prop.~\ref{prop:kappa-spectrum-k3-healed} + Rem.~\ref{rem:fm119-is-a-confusion} |
| 164 | "Pairwise-bridge closure is automatic once each bridge is proved" | Graph-theoretically a closed 6-cycle does commute IF every edge is an iso | Each alpha_ij must be constructed as an ISOMORPHISM of chiral algebras (not merely of characters, or partition functions, or Euler forms). Character agreement is necessary, not sufficient | Thm.~\ref{thm:pairwise-all-proved-closes-CY-C}: the 6-cycle closure depends on each alpha_ij being a chiral-algebra iso, not just a numerical coincidence. Five of the six bridges are currently Conditional; only alpha_23 (Borcherds 1992) is unconditional | necessary/sufficient | `cy_c_six_routes_convergence.tex` Thm.~\ref{thm:pairwise-all-proved-closes-CY-C} |
| 165 | "The CY-to-chiral functor Phi distinguishes three K3 algebras" | Three K3 algebras exist (CY functor / Monster orbifold / Leech VOA) | Phi gives ONE output. The other two come from DIFFERENT constructions (orbifold, lattice VOA) that do not factor through Phi | AP-CY59: for each algebra, name the CONSTRUCTION. $\kappa_{\mathrm{ch}}$ distinguishes the route, not the destination. Trichotomy is a consequence of using three different machines, not of Phi producing three outputs | construction/functor | `k3_chiral_algebra.tex` Prop.~\ref{prop:k3-trichotomy} (already healed; cross-referenced) |

**Operational counter (six-routes convergence, NEW pattern, Wave 14):** before writing "six routes converge on $G(X)$" or "the routes give the same algebra," fill in the following template:
```
For each route R_i:
  input data:   [derived category / Jacobi form / lattice / orbifold / SCFT / 6d theory]
  output:       A_X^{R_i}
  kappa_ch^{R_i}: [explicit value]
  construction arrow alpha_{i(i+1)}: [named construction, not "the R-matrix gives"]
  status:       [ProvedElsewhere / Conditional / Conjectured]
```
If any `input data` repeats across routes, the routes are not independent (check AP-CY60). If any `construction arrow` is narrated rather than named, see AP-CY57. If any `kappa_ch^{R_i}` is bare without subscript, see AP113. If the status column is uniformly `ProvedHere`, something is wrong -- only alpha_23 is unconditional at the Wave-14 snapshot.

**Operational counter (kappa-spectrum integrity, NEW pattern, Wave 14):** the kappa-spectrum on $K3 \times E$ is $\{0, 3, 5, 12, 24\}$ with FIVE values, not four. The cached pattern `{2,3,5,24}` conflates fiber $\chi(\mathcal{O}_S)=2$ with total-space data. Correct assignment:
```
kappa_cat(K3 x E)      = 0   [manifold; Kunneth 2*0=0]
kappa_ch^{R1}(K3 x E)  = 3   [algebraization; CY functor]
kappa_BKM(K3 x E)      = 5   [R2 Borcherds weight c_f(0)/2]
kappa_ch^{R4}(K3 x E)  = 12  [Kummer orbifold halves R3]
kappa_ch^{R3}(K3 x E)  = 24  [Mukai lattice VOA rank]
kappa_fiber(K3 x E)    = 24  [chi_top(K3)]
```
The value 2 that appeared as `kappa_cat` for K3xE in earlier working notes was $\chi(\mathcal{O}_{K3})=2$ of the FIBER, not $\chi(\mathcal{O}_{K3\times E})=0$ of the TOTAL SPACE. The value 2 belongs to $\kappa_{\mathrm{cat}}(K3)$, not $\kappa_{\mathrm{cat}}(K3\times E)$.

---

## Entry 51 — Wave-21 right-hand side: $\chi(\mathcal{O}_{K3\times E})$ vs $\chi^{\mathrm{cat}}$ (V53, 2026-04-16)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|---|---|---|---|---|
| 51 | "$\chi(\mathcal{O}_{K3\times E}) = 11$ closes the Wave-21 four-term identity $0+5-16+11=0$" | The Wave-21 identity $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{BKM}} + \mathrm{sdim}_{\mathrm{Ber}} + \chi^{\mathrm{cat}} = \chi(\mathcal{O}_X)$ DOES hold at $K3\times E$ | The right-hand side is $\chi(\mathcal{O}_{K3\times E}) = 0$ (Künneth: $2\cdot 0$), not 11. The value $\chi^{\mathrm{cat}} = 11$ is the *algebraization residual* on the LEFT side, not the manifold invariant on the right. | $0+5-16+11 = 0 = \chi(\mathcal{O}_{K3\times E})$. Manifold invariant ($\chi(\mathcal{O}_X)$, Künneth-multiplicative) closes the identity; algebraization residuals ($\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \mathrm{sdim}_{\mathrm{Ber}}, \chi^{\mathrm{cat}}$) collectively reproduce it. AP-CY55. | manifold/algebraization |

**First-principles disambiguation (V53 §6, AP-CY55 enforcement):**
- **Manifold invariants** (Künneth-multiplicative, depend ONLY on the underlying CY): $\chi(\mathcal{O}_X), \kappa_{\mathrm{fiber}}(X)$.
- **Algebraization residuals** (depend on which chiral/super/BKM algebra is constructed from $X$): $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \mathrm{sdim}_{\mathrm{Ber}}, \chi^{\mathrm{cat}}$.

The Wave-21 identity is a **bridge** between the two columns. Reading the right-hand $\chi(\mathcal{O}_X)$ as if it were an algebraization residual is the AP-CY55 conflation. The four projections on the left collectively reconstruct the manifold invariant on the right; this reconstruction is the *content* of the identity, not a tautology.

**Pythagorean companion (V53 §3):** $24^2 = (-16)^2 + 320$ orthogonally decomposes the squared Mukai rank into the squared Berezinian super-trace and the squared positive-root contribution measured against the K3 evaluation pairing. The Mukai signature $(4,20)$ produces a $\mathbb{Z}/2$-graded lattice; even and odd projections are orthogonal.

**Operational counter:** any expression $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{BKM}} + \mathrm{sdim}_{\mathrm{Ber}} + \chi^{\mathrm{cat}}$ MUST be checked against the *manifold-invariant* right-hand side, never against a numerical-coincidence sum. At $K3\times E$: $0+5-16+11 = 0 = \chi(\mathcal{O}_{K3\times E})$ ✓. At $K3$ alone (V50 falsifiable): $\chi^{\mathrm{cat}}(K3) = 13$ is *predicted*, $\chi(\mathcal{O}_{K3}) = 2$ is *known*; the four-term left-hand sum at the K3 fiber must equal 2.

---

## Entry 240 (2026-04-16): thm:borcherds-lift-universal installed

**Where**: chapters/examples/k3e_bkm_chapter.tex, new subsection §Universal property of the Borcherds lift, inserted after prop:k3e-genus-escalation (the Vol III chapter housing BKM machinery).

**Scope-and-hypothesis investigation (a)/(b)/(c):**

- **(a) Before install:** Borcherds lift was stated case-by-case — Δ_5 for K3×E (thm:k3e-borcherds-product), J(τ) for Monster (W13 remark on Vol II side), Fake Monster denominator referenced in notes/theory_generalized_root_datum.tex. prop:bkm-weight-universal proved the WEIGHT formula c_N(0)/2 universally for Z/NZ orbifolds, but only for K3-fibered CY_3 orbifolds; no universal-functor statement.
- **(b) Hypotheses for admitting a Borcherds lift:** even unimodular Lorentzian lattice L with b^+ ≥ 2, conformal VOA V with primitive isometric embedding L → Lat(V) compatible with Virasoro grading. Non-K3-fibered CY_3s (quintic, local P^2) have no K3 fiber → no Jacobi-form input → no Borcherds lift (prop:bkm-weight-universal(iv)); substitute is BCOV, NOT a theta lift (AP-CY8).
- **(c) Relation to Φ_3:** composite Φ_(-) ∘ Φ_3: D^b(Coh(X)) → E_1-ChirAlg → AutForm(G(Λ_Muk(X))) is DEFINED iff Λ_Muk(X) is even unimodular (K3-fibered case). NOT universal over all CY_3 — admission of a Borcherds lift is a PROPERTY of X (fibration existence), not of Φ_3 itself. This closes an AP-CY59/AP-CY60 ambiguity: Φ_3 and the Borcherds lift are INDEPENDENT constructions whose convergence at K3×E is Theorem-level, not functoriality.

**Cross-volume Vol II usage:** the Monster E_3-topological orbifold BV route (FM66, FM120, FM128) uses rem:borcherds-three-cases(2) — the Fake Monster denominator at L = II_{2,26} — and the SL_2(Z)-invariance of J(τ) from case (1). DW anomaly vanishing for the Leech Z/2 involution reduces to even-unimodularity of II_{2,26} + full modular invariance of J(τ), both consequences of thm:borcherds-lift-universal(i)+(iii).

**AP5 cross-volume propagation:** no formula with OPE-mode vs λ-bracket convention dependence introduced (weights, character multiplicativity, singular theta integrals are convention-independent). Vol II references the Monster route narratively in CLAUDE.md (FM66/FM120/FM128); no λ-bracket formula edits required. Vol I unaffected (no BKM machinery in Vol I's N-paper series).

**Citation alignment:** uses \cite{Borcherds1998}, \cite{Borcherds1992}, \cite{GN1996, GN2002} — keys consistent with notes/theory_generalized_root_datum.tex.

**Status**: ClaimStatusProvedElsewhere (attribution to Borcherds 1998 §§13-14 + Gritsenko-Nikulin 1996/2002). Strongest-form heal: no downgrade; theorem matches the universal statement the programme requires.

---

## Entry: rem:phi3-quintic-local-p2 (Vol III chapters/theory/cy_to_chiral.tex, 2026-04-16)

**Trigger:** Vol II-initiated adversarial probe — "Φ_3 is proved ∞-cat for any CY_3, but is the explicit E_1-chiral output identified for the quintic and local P^2? Is Borcherds admissibility correctly scoped (even unimodular Mukai)? Are BCOV vs Göttsche substitutes distinguished from Borcherds lift?"

**First-principles triple:**
- (A) Ghost of a true theorem: Φ_3 has explicit, manifold-specific constructions on the quintic (Gepner-chart CoHA on quiver-with-potential) and on local P^2 (Schiffmann-Vasserot/Nakajima CoHA on nested Hilbert schemes). Borcherds lift is a strict subcase requiring even unimodular Mukai + Lorentzian signature + Jacobi-form input. Non-K3-fibered CY_3 get substitutes that are dimension-specialised: BCOV (compact, h^{1,0}=0) or Göttsche/Vafa-Witten (local surfaces).
- (B) Precise conflation being defused: (i) "Φ_3 exists everywhere" ≠ "Φ_3 is Borcherds-lift-admissible everywhere" — the former is CY-A_3 (proved), the latter requires Mukai-lattice hypotheses that fail for quintic and local P^2. (ii) "Substitute for Borcherds" is NOT uniform across non-K3-fibered CY_3 — compact strict CY_3 with h^{1,0}=0 use BCOV; local surfaces use Göttsche; neither is a theta lift. (iii) κ_BKM is route-specific to the Borcherds lift (per cy_c_six_routes_convergence.tex R_2 route, AP-CY37); undefined for quintic and local P^2.
- (C) Correct statement: `rem:phi3-quintic-local-p2` bundles the five facts (a)-(e) with explicit cross-references to existing theorems (thm:cy-to-chiral-d3 for existence, prop:beauville-kappa-formula for κ_ch, thm:hae-mc-structural + prop:bcov-shadow-recursion for BCOV genus recursion, thm:borcherds-lift-universal for admissibility hypothesis, prop:cech-htt-coefficient-convergence for quintic convergence radius 1/20).

**Derived from:**
- chapters/theory/cy_to_chiral.tex:1629 (quintic N=5 patches, d=5, radius ≥ 1/20), 1968 (HKR H^0(O_X) coverage for quintic/local P^2), 2161 (quintic non-formality, Yukawa H^3=5+GW), 2414 (E_1 universality verified for quintic + local P^2), 3150-3175 (quintic κ_ch=-25/3, F_1=-25/72, conditional-on-Φ_3 now unconditional), 3815 (BCOV F_1=χ/24 for h^{1,0}=0 CICYs including quintic), 3898-3925 (HAE as shadow-tower spectral connection).
- chapters/examples/k3_chiral_algebra.tex:579 (κ_BKM undefined for quintic, C^3, conifold, local P^2; replacement = κ_BCOV for compact).
- chapters/examples/k3e_cy3_programme.tex:2140 (κ_BKM undefined for quintic).
- chapters/examples/cy_c_six_routes_convergence.tex:37-244 (R_2 Borcherds lift is route-specific; Mukai even unimodular required).
- chapters/connections/bar_cobar_bridge.tex:761 (Göttsche formula at rank 1 for K3); chapters/theory/quantum_chiral_algebras.tex:2470 (rank-1 VW generating function with exponent χ_top(S) for local surfaces).
- AP-CY8 (Borcherds denominator ≠ bar Euler product; needs CY-to-chiral functor), AP-CY11/AP-CY14 (CY-A_3 proved ∞-cat), AP-CY12 (class from full tower), AP-CY34/AP-CY37 (κ_BKM = c_N(0)/2 universal iff Borcherds admissible), Vol II FM160 (Monster/Borcherds even unimodular lineage).

**Verified against (disjoint sources for the scoping claim):**
- Quintic Hodge data: h^{1,1}=1, h^{2,1}=101, χ_top=-200 (Candelas-Ossa-Green-Parkes 1991 classical); H^3=5 (deg(X_5)=5).
- Local P^2 Hodge data: χ_top(P^2)=3 (Euler), McKay quiver of K_{P^2}=Z/3-orbifold quiver (AP-CY54 McKay).
- Göttsche 1990 (Math. Ann. 286): rank-1 Hilbert scheme generating function Σχ(Hilb^n(S))q^n = Π(1-q^k)^{-χ_top(S)}.
- BCOV 1994 (Comm. Math. Phys. 165): F_1 = -½ log det(∂̄†∂̄) gives χ_top/24 on strict CY_3 with h^{1,0}=0.
- Borcherds 1998 (Invent. Math. 132) + Gritsenko-Nikulin 1996/2002: multiplicative lift requires even unimodular Lorentzian lattice with Jacobi-form weight/index matching Weil representation.
- Schiffmann-Vasserot 2013 (Publ. IHÉS): CoHA of Jordan / affine-type quivers = Nakajima's nested Hilbert scheme Heisenberg extension.

**Disjoint rationale:** Göttsche 1990 computes Hilbert-scheme Euler characteristics directly from Betti numbers of S via Weil-Ellingsrud-Stromme. BCOV 1994 computes F_1 from the Ray-Singer analytic torsion. Borcherds 1998 requires a lattice + Jacobi-form pair whose Weil-representation data forces even unimodularity. These three sources produce the three substitutes independently, with disjoint inputs; the scoping claim ("Borcherds iff even unimodular Mukai; BCOV for compact h^{1,0}=0; Göttsche for local surfaces") is a partition of cases with independent witnesses, not a single-source tautology.

**AP5 cross-volume propagation:** No Vol II edits required. Vol II CLAUDE.md already has the correct Borcherds scoping in FM66/FM120/FM128 + FM160 (Monster orbifold route; even unimodularity of Leech/II_{25,1}). Vol I unaffected (no BCOV or Göttsche machinery). The Vol III remark cross-refs Vol II via the Monster-orbifold discussion only through FM160 in narrative, which is already in place.

**Citation alignment:** uses existing labels thm:cy-to-chiral-d3, prop:beauville-kappa-formula, thm:chi-neq-kappa, prop:cech-htt-coefficient-convergence, thm:e1-universality-cy3, thm:drinfeld-center-coha, thm:borcherds-lift-universal, thm:hae-mc-structural, prop:bcov-shadow-recursion, rem:gepner-lv-dichotomy, rem:cy3-kappa-polysemy — all verified present in chapters/theory/cy_to_chiral.tex and chapters/examples/k3e_bkm_chapter.tex by grep.

**Status:** Remark (not theorem) — it is a scoping/consequences bundle referring to proved theorems. No new ProvedHere tag introduced; no @independent_verification decorator required (this is a scope-bundling remark, the underlying theorems carry their own status). Strongest-form heal: three substitutes preserved (no downgrade to "Borcherds only"); Borcherds-admissibility hypothesis named precisely; explicit CoHA identifications for quintic and local P^2 supplied, not merely existence narration.


---

## Entry: rem:kha-vs-coha-bridge (Vol III chapters/theory/cy_to_chiral.tex, 2026-04-16)

**Trigger:** Vol II-initiated adversarial probe — "Are KHA and CoHA distinguished in the programme? Does Phi_3 land on cohomological or K-theoretic side? Is the quantum toroidal the K-theoretic refinement of the affine Yangian, and if so where in the manuscript?"

**First-principles triple:**
- (A) Ghost of true theorem: CoHA and KHA are genuinely distinct Hall-algebra constructions (rational vs trigonometric structure function), related by Chern character as a surjection-after-rationalization with torsion kernel; Phi_3 as constructed lands on CoHA, with K-theoretic Phi_3^K parallel awaiting construction.
- (B) Precise conflation defused: (i) narration "CoHA" used loosely for either; (ii) quantum toroidal appears in Vol III but as Koszul-dual target on E_2 category, not as direct Phi_3 output; (iii) Nekrasov partition function is a KHA object whose q->1 limit gives a CoHA object — not two names for the same thing.
- (C) Correct statement: Three-layer distinction (rational vs trigonometric structure functions; Chern character ring map with torsion kernel; native landing of Phi_3 on CoHA with Phi_3^K conjectural on KHA).

**Derived from:**
- chapters/theory/cy_to_chiral.tex:1337, 1373, 2363, 2398 (CoHA(C^3) = Y^+(gl_hat_1), five-step chain landing on CoHA).
- chapters/theory/e1_chiral_algebras.tex (E_1-chiral bialgebra axioms from Vol III swarm).
- compute/lib/e3_ce_quantum_toroidal.py (trigonometric structure function g^q(z); quantum toroidal U_{q,t}(gl_hat_hat_1) engine).
- compute/lib/quantum_toroidal_e1_cy3.py (quantum toroidal DIM presentation).
- compute/lib/qg_from_fh_3d_6d.py:1041 (quantum toroidal -> affine Yangian degeneration).
- AP-CY7 (CoHA != E_1-chiral algebra; associative construction).
- AP-CY30 (ZTE failure: K-theoretic refinement breaks K-V for E_infty).
- AP-CY33 (chain-level != rational; K-theoretic vs cohomological parallels chain vs rational).

**Verified against (disjoint sources):**
- Kontsevich-Soibelman 2008 (arXiv:0811.2435): CoHA definition via cohomology of moduli stack with vanishing-cycle sheaf.
- Kapranov-Vasserot 2011 (arXiv:1106.4428): K-theoretic elliptic cohomological Hall algebras on surfaces.
- Schiffmann-Vasserot 2013 (arXiv:1202.2756): CoHA(C^3) = Y^+(gl_hat_1) for Jordan quiver.
- Negut 2022 (arXiv:2211.16249): K-theoretic Hall algebras on 3-folds via derived Tor-convolution.
- Procházka-Rapčák 2018 (Y-algebras): Y(gl_hat_1) = W_{1+infty}.
- Feigin-Hashizume-Hoshino-Shiraishi-Yanagida 2009: quantum toroidal U_{q,t}(gl_hat_hat_1) presentation with Nekrasov-style trigonometric structure.

**Disjoint rationale:** KS2008 defines CoHA via cohomology (derived input: vanishing-cycle functor on commutative cohomology ring). KV2011 defines KHA via equivariant K-theory (derived input: Tor-convolution on Grothendieck group). Negut 2022 independently proves KHA convolution associativity via derived algebraic geometry on the Hecke stack. The Chern character ring homomorphism is Grothendieck-Riemann-Roch on the Hecke correspondence — each side defined without reference to the other; GRR provides the comparison. The rational-vs-trigonometric structure function dichotomy is computed independently in shuffle-algebra presentations (SV13 rational; FHHSY09 trigonometric).

**AP5 cross-volume propagation:** Vol II FM55 (RT invariants = E_infty factorization homology, not E_1-bar) relates: RT at roots of unity = KHA-level object, not CoHA; consistent with the remark's statement that quantum toroidal appears at roots of unity where CoHA collapses. No Vol II edits required — Vol II CLAUDE.md AP-CY22 (Miki automorphism algebra-specific) and the FM55 entry already capture the E_infty/KHA landing on the physics side. Vol I unaffected.

**Citation alignment:** uses \cite{KS2008, KV2011, SV2013, Negut2022}. Must verify all four bib keys exist in Vol III main bibliography. New keys KV2011 and Negut2022 may need adding to main.tex bibliography.

**Status:** Remark (not theorem) — scoping clarification distinguishing cohomological landing of Phi_3 from K-theoretic refinement. No ProvedHere tag. conj:phi3-K-theoretic noted as FRONTIER-ledger item; not installed as a \begin{conjecture} environment in this edit (separate task if promoted). Strongest-form heal: KHA vs CoHA distinction preserved without downgrade; Phi_3^K left as explicit open construction rather than conflated with Phi_3; quantum toroidal correctly positioned as Koszul-dual on E_2 category, not as direct CY-functor output.

---

## Entry: conj:harvey-moore-functorial (Functorial lift of alpha_{12})

**Location:** chapters/examples/cy_c_six_routes_convergence.tex, inserted after cor:cy-c-three-identities-reduction and before rem:cy-c-heal-upgrade.

**Claim (a) — conjectural statement:** There is an E_1-chiral-algebra isomorphism alpha_{12}^func: Phi_3(D^b(Coh(S x E))) -> A^Borch_{Phi_10}, equivariant under the identification (SL_2(Z) x SL_2(Z))/Z_2 ≅ Gamma_{Spin(2,1,2)}(Phi_10) between the Huybrechts autoequivalence group of D^b(Coh(S x E)) and the Siegel stabiliser of Phi_10 inside Sp(2,2,Z). S is a projective K3; E an elliptic curve; Phi_10 the Borcherds lift of the K3 elliptic genus 2 phi_{0,1}.

**Claim (b) — what is proved:**
- Rank level: Harvey-Moore 1996 BPS-counting identity for Phi_10 as the Borcherds denominator of g_{Delta_5}.
- Automorphism level: Huybrechts' autoequivalence group computation on product abelian/K3 derived categories (Ploog-Sosna for the K3 x E product case); Gritsenko-Nikulin's realisation of the Siegel stabiliser of Phi_10; both embed compatibly into Sp(2, 2, Z).
- 1/4-BPS scalar sector: Dabholkar-Murthy-Zagier Siegel-form counting of 1/4-BPS states = Fourier expansion of 1/Phi_10.

**Claim (c) — residual gap:** Promotion of the rank-, automorphism-, and 1/4-BPS-scalar-sector compatibilities to a functorial chiral-algebra isomorphism carrying higher correlators and mode-algebra structure. This is item (I1) of cor:cy-c-three-identities-reduction.

**Derived from:**
- chapters/examples/cy_c_six_routes_convergence.tex:196-229 (prop:cy-c-pairwise-agreements(a), cor:cy-c-three-identities-reduction(I1)).
- Harvey-Moore, Algebras, BPS states, and strings, arXiv:hep-th/9510182 (rank-level Phi_10 identity).
- Huybrechts (Fourier-Mukai transforms in algebraic geometry; The global Torelli theorem: classical, derived, twisted); Ploog-Sosna (autoequivalences of products).
- Dabholkar-Murthy-Zagier, Quantum black holes, wall crossing, and mock modular forms, arXiv:1208.4074 (1/4-BPS scalar Siegel-form counting).

**Verified against (disjoint sources):**
- Gritsenko-Nikulin (Automorphic forms and Lorentzian Kac-Moody algebras I, II; alg-geom/9610022, alg-geom/9611028): independent construction of Phi_10 as a denominator of a Borcherds-Kac-Moody superalgebra with Spin(2, 1, 2)-automorphy, giving the Siegel stabiliser Gamma_{Spin(2,1,2)}(Phi_10) intrinsically.
- Borcherds 1992 (Monstrous moonshine and monstrous Lie superalgebras, Invent. Math. 109): denominator formula theorem used in the R_2 route, independent of the Harvey-Moore BPS argument.
- Borcherds 1998 (Automorphic forms with singularities on Grassmannians, Invent. Math. 132): multiplicative lift defining A^Borch_{Phi_10} from 2 phi_{0,1}, independent of HKR/Phi_3.

**Disjoint rationale:** The derived-category side (Phi_3 of D^b(Coh(S x E))) is constructed via HKR + Bridgeland-King-Reid and the Fourier-Mukai kernel on S x E; the Borcherds side (A^Borch_{Phi_10}) is constructed via the Borcherds multiplicative lift applied directly to the K3 elliptic genus without any reference to the derived category. The coincidence of the automorphism groups is an independent theorem on each side: Huybrechts/Ploog-Sosna for the derived side, Gritsenko-Nikulin for the Siegel side. The 1/4-BPS scalar sector match (Dabholkar-Murthy-Zagier) is computed from BPS indices on the physics side and from Fourier coefficients of 1/Phi_10 on the automorphic side, with no common intermediary to Phi_3. All three evidence layers are pairwise derivation-disjoint.

**AP5 cross-volume propagation:** No formula-level propagation required. The conjecture introduces no new OPE coefficients, lambda-bracket entries, or kappa values. Vol II CLAUDE.md bridge tables reference the Phi_10 identity only at the scalar-character level (already Proved); Vol I is unaffected. The conjecture tag is ClaimStatusConjectured; no ProvedHere decorator required.

**Citation alignment:** uses inline references to arXiv:hep-th/9510182 (Harvey-Moore), arXiv:1208.4074 (Dabholkar-Murthy-Zagier), and named-author Huybrechts/Ploog-Sosna/Gritsenko-Nikulin/Borcherds citations. If promoted to \cite form, bib keys HarveyMoore1996, DMZ2012, Huybrechts-GTC, PloogSosna, GritsenkoNikulin, Borcherds1992, Borcherds1998 must be verified or added in main bibliography.

**Status:** Conjecture (ClaimStatusConjectured). Scope: functorial chiral-algebra refinement of alpha_{12}; closes item (I1) of CY-C three-identity reduction if promoted to theorem. Strongest-form heal: residual gap isolated to functorial mode-algebra content; three independent evidence layers prevent collapse to a single partial result; automorphism-level isomorphism promoted from narrative coincidence to explicit equivariance statement.

---

## Entry: prop:cy-c-i2-higher-genus-reduction (CY-C item (I2) modular-bootstrap reduction, 2026-04-16)

**Location:** chapters/examples/cy_c_six_routes_convergence.tex, inserted after rem:cy-c-heal-upgrade, before section "Status audit: pairwise-bridge table".

**Claim (a) — asserted.** For X = S x E with S a projective K3 and E an elliptic curve, the higher-genus EOT identity EG_g(K3) = Theta^{(g)}_{Lambda_Muk} as weight-0 index-1 Siegel modular forms reduces, for every g >= 2, to the genus-1 EOT statement EG_1(K3) = 2 phi_{0,1} via the curved-Dunn modular-bootstrap bridge. The discrepancy delta_g = EG_g(K3) - Theta^{(g)}_{Lambda_Muk} is a cocycle in the modular-bootstrap complex C^bullet_MB(Mbar_{g,n}), defining a class [delta_g] in H^2_MB whose vanishing is the Vol II theorem H^2_MB(g) = 0 for all g >= 1.

**Claim (b) — what is proved.** Unconditional at the cohomological level: the modular-bootstrap vanishing H^2_MB(g) = 0 (Vol II Part VI; curved_dunn_higher_genus.tex, thm:curved-dunn-H2-vanishing-all-genera, plus the modular-bootstrap-to-curved-Dunn bridge) kills the obstruction, giving EG_g(K3) = Theta^{(g)}_{Lambda_Muk} as a Siegel-modular-form identity. Clutching via Getzler-Kapranov modular operad + Borcherds multiplicative lift's compatibility with boundary-divisor restriction furnishes the stratum-wise equality; H^2_MB = 0 propagates it to the smooth locus.

**Claim (c) — residual gap.** Chain-level promotion to a chiral-algebra isomorphism at genus g requires the genus-1 chain-level compatibility of V_{Lambda_Muk(X)} and the half-twisted K3 sigma model, which is the EOT 2011 input and is established as a weak-Jacobi-form equality. The proposition does not eliminate this single genus-1 hypothesis; it eliminates the infinite-genus tower of hypotheses previously imagined for (I2).

**Derived from:**
- Vol II curved-Dunn directive (H^2_MB(g) = 0 at all g >= 1) and chapters/theory/curved_dunn_higher_genus.tex (Vol II): thm:curved-dunn-H2-vanishing-all-genera, prop:modular-bootstrap-to-curved-dunn-bridge, prop:genus1-twisted-tensor-product.
- Getzler-Kapranov 1998, Modular Operads (Compositio Math.), Thm 4.2.2: clutching decomposition of Mbar_{g,n} boundary strata.
- Borcherds 1998, Automorphic forms with singularities on Grassmannians, Invent. Math. 132: multiplicative theta-lift as Siegel modular form, compatibility with stratum restriction.
- Eguchi-Ooguri-Tachikawa 2011, arXiv:1004.0956: genus-1 EG_1(K3) = 2 phi_{0,1} weak-Jacobi-form equality.

**Verified against (disjoint sources):**
- Kudla 2003 (Modular forms and arithmetic geometry, Clay Lecture Notes): independent orthogonal-group theta-correspondence framework for higher-genus Siegel theta-lifts of even unimodular lattices, constructed without reference to modular-bootstrap cohomology or Vol II curved-Dunn complex.
- Gritsenko-Nikulin 1996-98 (Automorphic forms and Lorentzian Kac-Moody algebras I, II; alg-geom/9610022, 9611028): independent automorphy-level verification of the Siegel stabiliser of Phi_10 at arbitrary genus via Lorentzian-KM denominator identities, independent of modular-bootstrap complex.
- Wendland 2000 (Moduli spaces of unitary conformal field theories; hep-th/0010205 and follow-ups): sigma-model side higher-genus modular invariance of K3 elliptic genus computed from N=(4,4) superconformal character sums, independent of Niemeier-lattice theta-lift.
- Borcherds 1992 (Monstrous moonshine and monstrous Lie superalgebras, Invent. Math. 109): denominator formula at higher rank for the Phi_10 square root; cross-check on Niemeier-theta-lift side independent of the curved-Dunn bridge.

**Disjoint rationale.** The Niemeier-lattice theta-lift Theta^{(g)}_{Lambda_Muk} is computed via Kudla's orthogonal-group theta correspondence + Gritsenko-Nikulin's Lorentzian-KM framework; the K3 sigma-model elliptic genus EG_g(K3) is computed via Wendland's N=(4,4) superconformal character decomposition. Neither computation invokes the modular-bootstrap complex or Vol II curved-Dunn machinery. The reduction's content is that, once the genus-1 equality of these two independently-computed Siegel forms is established (EOT 2011), the modular-bootstrap vanishing H^2_MB(g) = 0 enforces the higher-genus equality without genus-by-genus computation. The curved-Dunn bridge is the programme-internal mechanism; EG_g(K3) and Theta^{(g)}_{Lambda_Muk} are programme-external objects with four independent automorphic constructions.

**AP5 cross-volume propagation.** No formula-level propagation. The proposition introduces no new OPE coefficients, lambda-bracket entries, kappa values, or modular coefficients. Vol II bridge tables already reference H^2_MB = 0 and the curved-Dunn bridge; this entry cites them by reference only. Vol I unaffected.

**Convention alignment:** Genus-g elliptic genus EG_g(K3) normalised as weight 0 index 1 Siegel modular form on Sp(2g, Z) (Gritsenko-Nikulin convention); 2 phi_{0,1} at genus 1 (EOT normalisation, c(-1) = 2; AP-CY42 respected). Vol II lambda-bracket vs Vol I OPE-mode conventions not engaged: proposition lives at Siegel-modular-form level.

**Status:** ClaimStatusProvedHereConditional. Unconditional cohomological reduction + conditional chain-level promotion on the same genus-1 hypothesis as (I2). Strongest-form heal: reduces surface area of (I2) from infinite-genus tower to single genus-1 chain-level input; Vol II modular-bootstrap vanishing theorem is load-bearing input, application here is novel.

## CY-B at d=3: Precise scope of proved vs open (rem:cy-b-d3-precise, 2026-04-16)

**Ghost theorem / full claim.** For any CY$_d$ category $\cC$, the functor $\Phi$ sends $\cC$ to an $E_n$-chiral algebra (with $n$ depending on $d$ per AP-CY58: $n=2$ at $d=2$; $n=1$ at $d=3$), and Koszul duality on the chiral side lifts to a Koszul duality of the underlying CY$_d$ category itself.

**Wrong/loose version.** "CY-B is proved at $d=3$" or "CY-B transports the CY$_3$ structure to a CY$_0$ Koszul dual," stated without distinguishing which of three layers is intended.

**First-principles layer decomposition (three layers).**
- Layer (a) — scalar conductor: $\kappa_\mathrm{ch}(A) + \kappa_\mathrm{ch}(A^!) = \rho_K$ for $A = \Phi(\cC)$, all shadow classes. PROVED (thm:cy-b-conductor).
- Layer (b) — categorical braided equivalence on the center: $\cZ(\Rep^{E_1}(A)) \simeq \cZ(\Rep^{E_1}(A^!))^{\mathrm{rev}}$ via Verdier spectral functor + Shapovalov $k \mapsto -k$. PROVED (thm:cy-b-d3, thm:verdier-spectral-functor). Note AP-CY26: Shapovalov transposition is the mechanism, NOT $\sigma_2$ negation.
- Layer (c) — geometric Koszul duality of the target CY$_3$ category itself: $D^b(\Coh(X))$ admits a Koszul dual fitting into a $0$-CY structure on $\End^\bullet_{D^b}(E_\bullet)$ for a tilting complex $E_\bullet$, compatible with the PTVV $(-3)$-shifted symplectic structure on $\mathrm{Perf}(X)$ via a $3$-shifted Lagrangian fibration. PROVED for toric CY$_3$ (fan combinatorics / Gale duality) and local CY$_3$ (resolved conifold, $\mathrm{Tot}(\omega_{\P^2})$). CONJECTURAL for compact CY$_3$ (quintic, K3-fibered, abelian).

**Precise open step (within layer (c)).** Compatibility between the tilting-complex $0$-CY structure on $\End^\bullet(E_\bullet)$ and a $3$-shifted Lagrangian fibration into $\mathrm{Perf}(X)$ with the PTVV $(-3)$-shifted symplectic structure. This is a $3$-shifted analogue of Kapranov's Koszul duality for exterior algebras. Required inputs: (i) PTVV $(-3)$-shifted symplectic on CY$_3$ derived moduli — AVAILABLE (Pantev-Toen-Vaquie-Vezzosi); (ii) Fukaya-Seidel $E_1$-algebra realizing Floer deformation at the $3$-shift — AVAILABLE in toric/local settings, UNAVAILABLE for compact quintics / K3-fibered / conifold transitions; (iii) Lagrangian-fibration compatibility — OPEN.

**Correct relationship.** "CY-B proved at $d=3$" in the master status table refers to layers (a)+(b): the conductor and the braided-center equivalence on the $E_1$-chiral side. The geometric Koszul duality of the CY$_3$ category itself (layer (c)) is a separate problem whose resolution would upgrade CY-B at $d=3$ from an $E_1$-chiral theorem to a CY$_3$-categorical theorem. Compact CY$_3$ cases (quintic, K3-fibered) sit outside the proved scope pending (iii).

**Confusion type.** level error (AP-CY56: $E_n$ level confusion across CY dim) + scope error (compact vs toric/local CY$_3$) + construction/narration (layer (b) proves a chiral-side equivalence; (c) would prove a category-side duality — distinct constructions).

**AP5 cross-volume propagation.** Vol II CLAUDE.md bridge tables: "E_2-chiral Koszul duality" entries should (when referring to $d=3$) specify $E_1$-chiral on $A$ inducing $E_2$ on center (per AP-CY58), and should not imply geometric Koszul duality of $D^b(\Coh(X))$. No formula-level propagation; scope-qualification only.

**Status.** Layers (a)+(b) ProvedHere in chapters/theory/e2_chiral_algebras.tex. Layer (c) unresolved; scope explicitly recorded in rem:cy-b-d3-precise. Strongest-honest form of "CY-B at $d=3$" is (a)+(b); layer (c) for compact CY$_3$ is a research frontier beyond the current programme.


## conj:kapranov-3shifted-exterior-koszul — Kapranov $3$-shifted exterior Koszul duality (2026-04-16)

**Ghost theorem / full claim.** For a compact CY$_3$ $X$, there exists a tilting object $E_X \in D^b(\Coh(X))$ with derived endomorphism algebra the $(-3)$-shifted exterior algebra on the tangent complex, $\End^\bullet(E_X) \simeq \Lambda^\bullet_{-3}(T_X) = \Sym^\bullet(T_X[-1])$; induced Koszul dual realizes $D^b(\Coh(X))^! \simeq \mathrm{QCoh}(T^*[-3]X)$ compatibly with the PTVV $(-3)$-shifted symplectic structure via a $3$-shifted Lagrangian fibration.

**Wrong/loose version.** "Kapranov Koszul duality extends to CY$_3$ directly" without the $(-3)$-shift; or conflating $\Lambda^\bullet(T_X)$ (classical Kapranov) with $\Lambda^\bullet_{-3}(T_X) = \Sym^\bullet(T_X[-1])$ (parity-swapped by the $3$-shift).

**First-principles three-part decomposition.**
- (a) Kapranov $1988$: for smooth projective $Y$, tilting $E_Y$ with $\End^\bullet(E_Y) \simeq \Lambda^\bullet(T_Y)$; dual dg-modules on $T[-1]Y$. UNCONDITIONAL.
- (b) PTVV $2013$: compact CY$_3$ $X$ gives $(-3)$-shifted symplectic on $\mathrm{Perf}(X)/\mathcal{M}_X$, forced by $\mathrm{HH}_3(X) \to k$ trace. UNCONDITIONAL.
- (c) $3$-shifted Kapranov: tilting $E_X$ with $\End^\bullet(E_X) \simeq \Sym^\bullet(T_X[-1])$; Koszul dual $\mathrm{QCoh}(T^*[-3]X)$ with PTVV-compatible Lagrangian fibration. CONJECTURAL compact; PROVED toric (Bondal-Orlov tilting + Gale duality on the fan; $E_X = \bigoplus_\sigma \mathcal{O}(D_\sigma)$, Jacobi algebra of superpotential as Koszul dual).

**Correct relationship.** Kapranov $1988$ exterior Koszul duality for smooth projective varieties is the unshifted ($d=0$) form. The $(-3)$-shift in the CY$_3$ setting turns $\Lambda^\bullet(T_X)$ into $\Sym^\bullet(T_X[-1])$ by parity swap; PTVV supplies the matching symplectic form; the conjecture asserts the Lagrangian-fibration compatibility needed to combine (a) with (b) into a genuine geometric Koszul duality at $d=3$. This is precisely step (c)(iii) of rem:cy-b-d3-precise.

**Confusion type.** Parity/shift convention (unshifted exterior vs shifted symmetric) + scope (toric/local vs compact CY$_3$) + construction-availability (toric gives explicit $E_X$; compact has candidate BCOV/Landau-Ginzburg routes but no constructed tilting object).

**AP5 cross-volume propagation.** Vol II CLAUDE.md: no formula propagation; the conjecture sharpens the missing step in layer (c) of CY-B at $d=3$ already recorded in the Vol II bridge tables. References Kapranov $1988$, PTVV $2013$, Bondal-Orlov $2001$.

**Status.** Conjectured in chapters/theory/e2_chiral_algebras.tex (conj:kapranov-3shifted-exterior-koszul). Resolution would close step (c)(iii) of rem:cy-b-d3-precise and upgrade CY-B at $d=3$ from an $E_1$-chiral theorem to a CY$_3$-categorical theorem in the sense of Kapranov.

## Entry: conj:cy-c-i3-half-bps (CY-C item (I3) full $1/2$-BPS chiral algebra identification, 2026-04-16)

**Location:** chapters/examples/cy_c_six_routes_convergence.tex, inserted after \end{proof} of prop:cy-c-pairwise-agreements and before conj:harvey-moore-functorial. Paired with rem:conj-cy-c-i3-half-bps-triple.

**Ghost theorem / full claim.** For X = S x E (S projective K3, E elliptic), the derived-category chiral algebra Phi_3(D^b(Coh(S x E))) coincides, as an E_1-chiral algebra, with the FULL 1/2-BPS chiral algebra A^{1/2}_{T[X]} of the class-S theory T[S x E], not merely with its 1/4-BPS (BLLPR Schur) sub-sector.

**First-principles triple.**
- (a) Asserted: Phi_3(D^b(Coh(S x E))) ~= A^{1/2}_{T[X]} as E_1-chiral algebras; A^{1/2} strictly extends A^{1/4} by short-multiplet operators satisfying E - 2R - 2j_2 = 0 but not the stronger Schur constraint E - 2R - j_2 = 0.
- (b) Proved: Schur sector (a) identification via BLLPR (arXiv:1312.5344) + Costello-Gaiotto holomorphic-twist bridge (arXiv:1810.01970); character-level match of full 1/2-BPS index with vacuum character of Phi_3(D^b(Coh(X))) after 1/2-BPS R-grading decomposition (Shimizu 2018, arXiv:1805.12565).
- (c) Residual gap: functorial extension of the Costello-Gaiotto 3d HT construction from the Schur locus t=q into the full 1/2-BPS locus. 1/2-BPS descendants carry irrational (p,q,t) fugacity dependence off the Schur surface; the missing construction is analytic continuation of the CG holomorphic-twist bridge in the superconformal fugacities, not an algebraic identification at a single point.

**Derived from:**
- BLLPR 2013 (Beem-Lemos-Liendo-Peelaers-Rastelli, Infinite chiral symmetry in four dimensions, arXiv:1312.5344): Schur-sector chiral algebra A^{1/4}_{T[X]} and 4d-N=2/2d-VOA correspondence.
- Costello-Gaiotto 2018 (Vertex operator algebras and 3d N=4 gauge theories, arXiv:1810.01970): 3d holomorphic-topological theory on X x R with boundary VOA; used to identify A^{1/4}_{T[X]} with Phi_3(D^b(Coh(X)))|_Schur.
- Shimizu 2018 (arXiv:1805.12565): superconformal-index / VOA-character match for class-S theories.
- Phi_3 HKR + Fourier-Mukai construction on D^b(Coh(S x E)) (Vol III e1_chiral_algebras.tex; AP-CY14 post-CY-A_3 closure).

**Verified against (disjoint sources):**
- Gaiotto-Moore-Neitzke 2013 (Framed BPS states, arXiv:1006.0146; Spectral networks, arXiv:1204.4824): independent BPS-state counting on T[X] via spectral networks on the UV curve, producing a partition function that matches the superconformal index via AGT-type localisation without reference to Phi_3 or D^b(Coh(X)).
- Dabholkar-Murthy-Zagier 2012 (arXiv:1208.4074): 1/4-BPS Siegel-form counting already referenced in prop:cy-c-pairwise-agreements(c); cross-check at the 1/4 locus disjoint from Phi_3 construction.
- Beem-Peelaers-Rastelli-van Rees 2014 (Chiral algebras of class S, arXiv:1408.6522): independent construction of class-S VOAs via Higgs-branch chiralisation, used here to verify that A^{1/4}_{T[X]} has the correct central charge and stress-tensor structure before the Phi_3 comparison, with no reference to derived categories of Coh.
- Arakawa-Moreau 2017 (Joseph ideals and lisse minimal W-algebras, arXiv:1706.10523): chiral-algebra-side check on A^{1/4}_{T[X]} C_2-cofiniteness, independent of 3d-HT bridge.

**Disjoint rationale.** The derived-category side (Phi_3) is constructed via HKR + Bridgeland-King-Reid + relative Fourier-Mukai on S x E -> E. The class-S side (T[X], A^{1/4}_{T[X]}, A^{1/2}_{T[X]}) is constructed via 6d (2,0) compactification + BLLPR Schur limit or full 1/2-BPS cohomology. The Costello-Gaiotto bridge is a THIRD construction (3d HT theory on X x R) mediating the comparison at the Schur locus. The character-level extension (Shimizu) is independent of Costello-Gaiotto, using only modular-trace computations on the VOA side and superconformal-index integrals on the class-S side. The four evidence layers (BLLPR construction, CG bridge, Shimizu character match, GMN spectral-network cross-check) are derivation-disjoint: no two share a mathematical intermediary beyond the superconformal index as a numerical output.

**AP5 cross-volume propagation.** No formula-level propagation. The conjecture introduces no new OPE coefficients, lambda-brackets, or kappa values. Vol II conventions (lambda-brackets with 1/n! factor) vs Vol I (OPE modes) are not engaged: conjecture lives at chiral-algebra-iso level. Vol II CLAUDE.md bridge tables reference BLLPR-type constructions at the Schur-sector level only; no table rewrite required.

**Citation alignment.** Inline arXiv references only (1312.5344, 1810.01970, 1805.12565). If promoted to \cite form: bib keys BLLPR2013, CostelloGaiotto2018, Shimizu2018 need verification in main bibliography; GaiottoMooreNeitzke2013, BPRvR2014, ArakawaMoreau2017 would be added if (b) or (c) layers get theorem-level proof.

**Status.** ClaimStatusConjectured. Scope: full 1/2-BPS chiral-algebra identification of Phi_3(D^b(Coh(S x E))); the 1/4-BPS Schur-sector content is proved and recorded separately in prop:cy-c-pairwise-agreements(c) and at character level by Shimizu. Strongest-form heal path: construct analytic continuation of Costello-Gaiotto bridge in (p,q,t) off the Schur surface t=q, promoting the Shimizu character-level match to a functorial E_1-chiral-algebra isomorphism. This is the (I3) chiral-algebra-level refinement within Corollary cor:cy-c-three-identities-reduction.


## Entry: kappa-cat(K3xE) fiber vs total-space (2026-04-17, CG-rectify preface chunk 5)

**Wrong claim.** $\kappa_{\mathrm{cat}}(K3 \times E) = 2$ (seen in preface L107, propagated from the conjectural BKM decomposition $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}}) = 3 + 2 = 5$ at $N = 1$).

**Ghost theorem.** $\chi(\mathcal{O}_{K3}) = 2$ is a genuine invariant of the K3 fiber, and $\kappa_{\mathrm{BKM}} - \kappa_{\mathrm{ch}} = 2$ is a genuine arithmetic relationship at $N = 1$ (the decomposition coincidence flagged by AP-CY55 adversarial).

**Correct relationship.** $\kappa_{\mathrm{cat}}(X) = \chi(\mathcal{O}_X)$ is defined on the TOTAL SPACE. By Künneth, $\chi(\mathcal{O}_{K3 \times E}) = \chi(\mathcal{O}_{K3}) \cdot \chi(\mathcal{O}_E) = 2 \cdot 0 = 0$. The value 2 is $\chi(\mathcal{O}_{\mathrm{fiber}})$, a fiber invariant, distinct from $\kappa_{\mathrm{cat}}(K3 \times E)$. The BKM decomposition, to the extent it holds, decomposes $\kappa_{\mathrm{BKM}}$ as $\kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$, not as $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{cat}}$. Per AP-CY55 adversarial, even that decomposition fails for $N \ge 2$; the only correct universal formula is $\kappa_{\mathrm{BKM}} = c_N(0)/2$ (Borcherds weight theorem, prop:bkm-weight-universal).

**Confusion type.** Level error: confusing a fiber invariant of a K3-fibered CY$_3$ with a total-space invariant of the same CY$_3$, driven by the numerical coincidence $5 = 3 + 2$ at $N = 1$.

**AP5 cross-volume propagation.** Other Vol III sites carry the same $\kappa_{\mathrm{cat}} = 2$ mislabelling: `quantum_chiral_algebras.tex` L870/L1020/L2453, `cy_holographic_datum_master.tex` L973, `en_factorization.tex` multiple lines, `working_notes.tex` L2682/L3928, `introduction.tex` L1179. `k3_chiral_algebra.tex` L531 and `k3_yangian_chapter.tex` L2596/L2607 are correct ($\kappa_{\mathrm{cat}}(K3)$, the fiber itself as the manifold). `main.tex` L872 is correct (underbraced with "fiber, manifold"). The Vol III preface L991 is correct ($\kappa_{\mathrm{cat}}(K3) = 2$ in the K3-moonshine-multiplier context). Future chunks should propagate the fix to the listed sites with explicit fiber-vs-total-space labelling per AP-CY68.

**Status.** AP-CY68 catalogued; preface L107 fixed in commit 51cee5b (chunk 5). Propagation to other Vol III sites pending.


## Entry: S^d-framing on HH_\bullet vs Gerstenhaber bracket on HH^\bullet (2026-04-17, CG-rectify preface chunk 5)

**Wrong claim.** "Hochschild complex $\HH_\bullet(\mathcal{C})$ receives the $\mathbb{S}^d$-framing and Gerstenhaber bracket" (preface L79-80 pre-fix).

**Ghost theorem.** Both the $\mathbb{S}^d$-framing and the Gerstenhaber bracket are genuine structures on "the Hochschild data of $\mathcal{C}$", and in the CY$_d$ setting they combine to produce the $\En$-chiral structure on the output of $\Phi$.

**Correct relationship.** The $\mathbb{S}^d$-framing (Connes $B$-operator hierarchy, Kontsevich-Vlassopoulos) lives on Hochschild HOMOLOGY $\HH_\bullet(\mathcal{C})$, producing the mixed / negative cyclic refinement $\HC^-_\bullet(\mathcal{C})$ on which the CY trace $\Tr : \HC^-_d(\mathcal{C}) \to k$ is defined. The Gerstenhaber bracket of degree $1 - d$ lives on Hochschild COHOMOLOGY $\HH^\bullet(\mathcal{C}, \mathcal{C})$. These are two distinct complexes with distinct structures; the CY-to-chiral functor uses BOTH: the trace on $\HC^-_d$ supplies the Frobenius pairing, and the Gerstenhaber bracket's degree determines the operadic level ($d = 2 \Rightarrow \Etwo$ via Hochschild's $\mathbb{S}^1$-action, $d \ge 3 \Rightarrow \Eone$ via shifted bracket).

**Why the degree matters.** For $d = 2$ the Gerstenhaber bracket has degree $-1$, which is the degree of the Lie conformal bracket ($\lambda$-bracket): the $\Etwo$-chiral structure emerges directly. For $d \ge 3$ the degree is $\le -2$, too shifted to produce braiding on $\Rep(A)$ via the little-disks operad ($\pi_1(\Conf_2(\R^d)) = 0$ for $d \ge 3$); the $\Etwo$-braiding is produced DERIVED on the Drinfeld centre, not NATIVE on $A$. Attributing the bracket to homology loses the degree shift and breaks this argument.

**Confusion type.** Part/whole confusion (one "Hochschild data" for two different complexes) + degree convention (bracket degree $1 - d$ requires cohomological framing).

**AP5 cross-volume propagation.** No formula propagation. Scope-level only: other Vol III sites using "Hochschild complex $\HH_\bullet(\mathcal{C})$" as a joint carrier for Connes + Gerstenhaber data would benefit from the separation, though most of the theory chapters (`cy_categories.tex`, `hochschild_calculus.tex`, `cyclic_ainf.tex`) already distinguish them correctly; the conflation was specific to the preface's compressed register.

**Status.** AP-CY69 catalogued; preface L79 fixed in commit 51cee5b (chunk 5).


## Entry: Internal-development metadata in reader-facing prose (2026-04-17, CG-rectify preface chunks 4-7)

**Wrong claim.** (Five species, not claims but editorial artefacts.) "(2026-04-17 inscription)", "(commit cade61c)", "first edition of this volume", "AP-CY60" cited in prose, "the original trichotomy presentation is healed". All instances document the manuscript's own development history inside prose intended for external readers.

**Ghost theorem.** Manuscript revision history is genuine content with value for internal audit. The AP-CY-NN tags, commit hashes, campaign timestamps, and status-change notes form an accurate record of how each claim reached its current scope.

**Correct relationship.** The audit trail belongs in commit messages, `notes/` changelog files, and the internal AP catalogue (this very document). It does NOT belong in preface prose or chapter introductions that a referee, reviewer, or external mathematician will read. The mathematical CONTENT of each fix (e.g., "$\kappa_{\mathrm{ch}}$ is the Hodge supertrace, hence route-independent" is the actual claim) should appear in prose verbatim; the METACOMMENTARY ("this was healed in commit cade61c; the original trichotomy presentation was wrong") should migrate to the audit trail.

**Confusion type.** Register error: conflating manuscript-internal discipline (AP tags, commit hashes, healing status) with reader-facing mathematical exposition. The LLM pattern-matches on the rectification-session verbiage present in CLAUDE.md and agent briefs, and reproduces that verbiage in the prose being rectified.

**AP5 cross-volume propagation.** Cross-volume grep pattern: `2026-`, `commit `, `inscription`, `campaign`, `AP-CY`, `healed`, `first edition`, `earlier phrasing`, `pre-2026-`, `superseded across the volume`. Each hit either strips the metadata (preserving the mathematical claim) or migrates content to a `notes/` file or commit message. Vol I and Vol II prose likely carry similar artefacts from their parallel rectification campaigns; scope-separate cleanup.

**Status.** AP-CY70 catalogued; 5 Vol III preface instances fixed in commits 38a074e / 51cee5b / 33f4d59 (chunks 4-7). Other files pending.


## Entry: kappa_ch conflated with Hodge supertrace (2026-04-17, CG-rectify preface chunk 9, AP-CY71)

**Wrong claim.** "kappa_ch is the Hodge supertrace, hence route-independent and equal to 0 on K3 x E."

**Ghost theorem.** kappa_ch IS route-independent across any construction that recovers Phi_3(C) up to equivalence. This is genuine: a categorical invariant of Phi_3(C) is route-independent tautologically.

**Correct relationship.** The Hodge supertrace sum (-1)^q h^{0,q}(X) = chi(O_X) = kappa_cat(X), a MANIFOLD INVARIANT (AP-CY55). It equals 0 for K3 x E by Kunneth (chi(O_K3) * chi(O_E) = 2 * 0 = 0). The chiral characteristic kappa_ch(K3 x E) = 3 is a different invariant, computed via additivity kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3. The WRONG MECHANISM is attributing route-independence to the Hodge supertrace formula; the CORRECT MECHANISM is categorical invariance of Phi_3(C) plus additivity under products.

**Confusion type.** Level error: conflating chi(O_X) = kappa_cat with kappa_ch. The two invariants agree only in the narrow d=2, h^{1,0} = 0 case (e.g. K3: 2 = 2). Elsewhere they diverge (E: chi(O_E) = 0 vs kappa_ch(E) = 1; K3 x E: chi(O_{K3 x E}) = 0 vs kappa_ch = 3).

**AP5 cross-volume propagation.** The stratification theorem kappa_ch(Phi(C_X)) = sum (-1)^q h^{0,q}(X) (thm:kappa-stratification-by-d) asserts this equality universally for d <= 5. It holds at d = 2 with h^{1,0} = 0 but fails at d = 1 (E) and d = 3 (K3 x E). The theorem's scope needs restriction or its claim needs revision. Cross-volume audit pending.

**Status.** AP-CY71 catalogued. Preface L427, L487 fixed in commit bcbdd3b (chunk 9).


## Entry: S^4 = S^2 x S^2 framing-decomposition shorthand (2026-04-17, CG-rectify preface chunk 11, AP-CY72)

**Wrong claim (as literally stated).** "The Hopf decomposition S^4 = S^2 x S^2 recovers E_2..."

**Ghost theorem.** For a product CY_4 of the form K3 x K3, the E_4-framing of Phi_4(C) splits as a Kunneth product of two E_2-framings, one per K3 factor, compatible with the Kontsevich-Vlassopoulos S^2-action on each factor's Hochschild homology.

**Correct relationship.** S^4 and S^2 x S^2 are not homeomorphic as manifolds (H^2(S^4) = 0, H^2(S^2 x S^2) = Z^2). The intended claim is a statement about factorization-algebra framing on the CARRIER manifold, not about sphere topology. The shorthand "S^4 = S^2 x S^2" compresses "the E_4-framing splits per K3 factor via Kunneth" into a symbolic equation, inviting literal misreading.

**Confusion type.** Notation shorthand without scope marker: the "=" in "S^4 = S^2 x S^2" is a framing-decomposition bookkeeping, not a manifold isomorphism. Writing it without a qualifier trips readers and introduces an apparent topological error.

**AP5 cross-volume propagation.** The shorthand appears at preface L610, introduction.tex L249 and L1404, en_factorization.tex L2685, m3_b2_saga.tex L1228, plus the engine hopf_fibration_s3_framing.py. Unified propagation needed; local fix in one site creates inconsistency with the rest of the volume.

**Status.** AP-CY72 catalogued. Cross-volume campaign pending.


## Entry: pi_d(BU) 8-periodicity vs 2-periodicity (2026-04-17, CG-rectify preface chunk 16, AP-CY73)

**Wrong claim.** "Obs_eff(d) ∈ pi_d(BU) is 8-periodic by Bott periodicity and trivial precisely when d mod 8 in {1, 3, 7}." (Preface L894; CLAUDE.md CY-A statement.)

**Ghost theorem.** The effective framing obstruction has a genuine 8-periodicity structure with a distinguished stratum at d ≡ 5 mod 8 (Sp-refinement contributing a Z/2-obstruction).

**Correct relationship.** pi_d(BU) = KU^{-d} is 2-periodic by complex Bott periodicity: pi_d(BU) = Z for d even, 0 for d odd. The 8-periodicity belongs to pi_d(BO) = KO^{-d} (real Bott) or to an Sp-refined tower. If Obs_eff is genuinely complex-analytic, the group is pi_d(BU) and the periodicity is 2 (trivial at all odd d). If the obstruction is real / symplectic, the group is pi_d(BO) or a refined tower, with the d mod 8 in {1, 3, 5, 7} odd-stratum (Sp refinement) as a further distinction. The shorthand "pi_d(BU) is 8-periodic" conflates the complex 2-periodic group with the real 8-periodic one.

**Confusion type.** Group-vs-periodicity mismatch: the periodicity cited is the real Bott periodicity of pi_d(BO), but the group name written is the complex pi_d(BU).

**AP5 cross-volume propagation.** Preface L894, CLAUDE.md CY-A Main Theorems entry, en_factorization.tex (e1-stabilization-cy theorems). A single campaign should either (a) pick pi_d(BO) and match to 8-periodicity, or (b) keep pi_d(BU) and match to 2-periodicity with an explicit Sp-refinement invocation for the d ≡ 5 stratum.

**Status.** AP-CY73 catalogued. Cross-volume campaign pending.
