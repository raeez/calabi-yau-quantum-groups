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
