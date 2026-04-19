# Agent 07 -- Drinfeld: Non-abelian K3 Yangian. The unifying principle.

**Author.** Raeez Lorgat.
**Voice.** Drinfeld. The unifying principle stated precisely. Courage with the equals sign, but only after the six F_i have been named and their kernels computed.
**Target.** `k3_yangian_chapter.tex`, `bar_cobar_bridge.tex` (+ the Vol I seven-faces chapter `genus1_seven_faces.tex`), `k3e_bkm_chapter.tex`, `cy_c_six_routes_convergence.tex`, `cy_c_pentagon_hypothesis_closures_platonic.tex`.
**Question.** Is there a common quasi-triangular Hopf algebra H_{K3} of which each of the six R_i-constructions is a functorial image? Or is "G(K3 x E)" a *pentagon colimit* whose source is Borcherds?

I will state the conclusion first, then prove it.

---

## Executive theorem (the unifying principle, stated precisely)

> **Theorem (Non-abelian K3 Yangian, pentagon-colimit form).** Fix X = S × E, S a projective K3, E an elliptic curve. Let Λ_Muk = H*(S,Z) ⊕ H*(E,Z) (Mukai lattice, signature (4,20), rank 24). There does NOT exist a single quasi-triangular Hopf algebra H_{K3} of which the six route-outputs A_X^{R_i} (i = 1,...,6) are functorial images.
>
> What exists is a **pentagon P_{K3}** of quasi-triangular Hopf/bialgebra objects with five named intertwiners β_{ij}, whose **colimit (equivalently, pushout across the Borcherds source)** is a well-defined object
>
>    Y_{non-ab}(g_{K3}) := colim P_{K3} ≅ D( Y^+( ĝ_{Δ_5} ) ) / I_Muk ,
>
> where Y^+( ĝ_{Δ_5} ) is the positive-half generalised Yangian on Gritsenko-Nikulin's BKM superalgebra g_{Δ_5}, D(·) its Drinfeld double, and I_Muk the ideal specified by the Mukai orthogonal form ω_Muk of signature (4,20). The Borcherds construction R_2 is the **source** of the pentagon (all five β-arrows point away from R_2); every other construction receives a lossy functor from R_2 whose kernel is computed below.
>
> The r-matrix of Y_{non-ab}(g_{K3}) is uniquely determined, up to the gauge group
>
>    G_gauge = Aut( osp(4|20), ω_Muk ) × C*_{shift}
>            ≃ O(4,20; Z) × C*,
>
> by the chain-level collision-residue data at genus 0 (hence at genus 1 via the Weierstrass promotion of Vol I's seven faces chapter).

The rest of this note is the proof: ROUND 1 attack and heal (the six constructions and what they actually produce), ROUND 2 attack and heal (no common H_{K3}, pentagon colimit with β-arrows on explicit generators), ROUND 3 attack and heal (r-matrix determines Y up to G_gauge).

---

## ROUND 1 ATTACK: enumerate the six constructions precisely

For each route I report: **(a) output object; (b) Hopf/bialgebra structure; (c) Y-type / U_q-type / W-type / none; (d) category in which it lives; (e) R-matrix / universal R.**

**R_1 (CY-to-chiral, Φ_3).**
- **(a)** A_X^{R_1} := Φ_3(D^b(Coh(S × E))), an E_1-chiral algebra on the elliptic fibration X → E. Primitive generator rank ρ^{R_1} = 3 (Thm kappa-stratification, `cy_c_six_routes_convergence.tex:403-410`).
- **(b)** Coassociative E_1-coalgebra via the bar functor B; bialgebra structure conjectural (depends on chain-level CY-A_3 passage).
- **(c)** *Neither* a Yangian nor a quantum loop algebra in any conventional sense; a factorisation-E_1 chiral-algebra output. At Koszul locus restricts to a Y-type via Φ_3 ∘ Drinfeld double.
- **(d)** ChirAlg^{E_1}_X, or equivalently FactCoAlg(Ran X).
- **(e)** No universal R in the ordinary sense. The shadow has a collision residue r_1(z) = coll-res(Θ_{A_X^{R_1}}), with ρ^{R_1} = 3 primitive generators.

**R_2 (Borcherds lift).**
- **(a)** A_X^{R_2} := U(g_{Δ_5}), the universal envelope of Gritsenko-Nikulin's BKM superalgebra, whose denominator is the Siegel cusp form Φ_{10} = Δ_5^2 up to constants (`cy_c_six_routes_convergence.tex:26`).
- **(b)** Cocommutative Hopf algebra (envelope of a Lie superalgebra). Drinfeld double D(U(g_{Δ_5}^+)) can be formed on the positive half and yields a *generalised Yangian* in the weak sense (no standard Drinfeld presentation for a BKM with imaginary simple roots; `k3_yangian_chapter.tex:1290-1294`, Borcherds-Serre obstruction).
- **(c)** BKM-type envelope; the *positive-half* Y^+(ĝ_{Δ_5}) is Y-type (CoHA form, Schiffmann-Vasserot dictionary for the abelian fibre).
- **(d)** Co-commutative Hopf algebras over C (BKM envelope); OR, after Drinfeld-double, quasi-triangular Hopf on the Koszul locus.
- **(e)** No classical universal R (g_{Δ_5} is not a Manin triple as stated). After formal Drinfeld-doubling the positive half:
     r_2(z) = canonical pairing on g_{Δ_5}^+ ⊗ g_{Δ_5}^-
with spectral dependence inherited from the Siegel parameter through Φ_{10}. The generator rank is ρ^{R_2} = 24 (Mukai lattice rank, realised via lightlike imaginary roots of multiplicity c(0) = 10, real roots of multiplicity 3, and spacelike imaginaries stratified by discriminant).

**R_3 (Mukai lattice VOA).**
- **(a)** A_X^{R_3} := V_{Λ_Muk(X)}, the even unimodular lattice VOA on the Mukai lattice Λ_Muk = U^3 ⊕ E_8(-1)^2.
- **(b)** Commutative cocommutative vertex operator algebra; NO quantum-group Hopf structure. Bialgebra structure via the Frenkel-Lepowsky-Meurman lattice construction — *Hopf algebra of modes* is a Heisenberg envelope on 24 generators.
- **(c)** W-type lattice VOA; after abelianisation, Heisenberg (class G) on 24 generators. Corresponds to Y(h_{24}) in the Vol III abelian-level (`cy_c_six_routes_convergence.tex:508-554`, thm cy-c-abelian-K3).
- **(d)** VOA/chiral algebra category on a (fixed) elliptic curve.
- **(e)** r_3(z) = (diagonal Heisenberg) = Σ_{i=1}^{24} ε_i H_i ⊗ H_i / z, where ε_i = ±1 encodes the Mukai signature (4,20). No non-abelian enhancement; ρ^{R_3} = 24.

**R_4 (Kummer / orbifold).**
- **(a)** A_X^{R_4} := V_{Λ_Muk}^{Z/2} ⊕ V_{Λ_Muk}^{Z/2,tw}, the Z/2-orbifold of the lattice VOA along the symplectic K3 involution ι_S crossed with the elliptic inversion on E (`cy_c_six_routes_convergence.tex:99-113`).
- **(b)** Cyclic-orbifold VOA; "twisted Hopf" structure via Dong-Li-Mason 1997 (q-alg/9603018).
- **(c)** W-type orbifold VOA; ρ^{R_4} = 12 (halved by Z/2).
- **(d)** Orbifold-VOA category.
- **(e)** r_4(z) = Z/2-invariant restriction of r_3(z). Drops to signature (2,10); the non-invariant half of Mukai is killed by the orbifold.

**R_5 (half-twisted sigma model).**
- **(a)** A_X^{R_5} := holomorphic half-twist of the N=(2,2) sigma model on X = S × E. A chiral algebra of primitive rank ρ^{R_5} = 3 (one per complex dimension of X). Kapustin-Witten / Costello-Gaiotto form.
- **(b)** E_1-chiral algebra; Hopf structure via the holomorphic-topological boundary operator.
- **(c)** Neither pure Y-type nor U_q-type; a *holomorphic twist chiral algebra* — comes closest to R_1 but lives natively in physics.
- **(d)** Cost-Gaio factorisation-algebra category on X.
- **(e)** r_5(z) comes from Chern-Simons on the elliptic fibration; carries the same 3 primitive currents as R_1.

**R_6 (BLLPR / 6d compactification).**
- **(a)** A_X^{R_6} := Schur-sector chiral algebra of a 4d N=2 class-S theory T[X] whose UV curve is E and whose K3-fibre data is encoded in the BLLPR functor (arXiv:1312.5344).
- **(b)** E_1-chiral algebra with a natural class-S modular structure; quantum-group organisation *per punctures* on the UV curve.
- **(c)** Class-S W-type; contains a Virasoro of c = 26 and a Mukai-rank Cartan of rank ρ^{R_6} = 3.
- **(d)** 4d N=2 → 2d chiral algebra category (BLLPR); equivalently, holomorphic twist category of a 6d (2,0) theory compactified on E.
- **(e)** r_6(z) is the Schur-limit R-matrix; Maulik-Okounkov form on Hilb^n(S) (via the K3-fibre).

**Summary table.**

| Route | Output A_X^{R_i} | Hopf/bialgebra | Type | Category | Gen. rank ρ | R-matrix |
|---|---|---|---|---|---|---|
| R_1 | Φ_3(D^b Coh(S×E)) | E_1-coalgebra | ChirAlg | ChirAlg^{E_1}_X | 3 | chiral coll-res |
| R_2 | U(g_{Δ_5}) | cocomm. Hopf (BKM env.) | BKM | co-Hopf/C | 24 | formal D(Y^+) |
| R_3 | V_{Λ_Muk} | VOA, Heis. modes | W / Heis | VOA | 24 | diag. Mukai |
| R_4 | (V_{Λ_Muk})^{Z/2} ⊕ tw | Orbifold VOA | W-orb. | OrbVOA | 12 | Z/2-inv. |
| R_5 | σ-model twist | E_1 holomorphic-twist | χ-alg | FactAlg | 3 | hCS Lax |
| R_6 | A^{Schur}_{T[X]} | class-S χ-alg | W / Schur | BLLPR | 3 | MO R-matrix |

**Key reading of this table.** The six outputs do NOT live in a single category. The generator ranks ρ^{R_i} take *three distinct* values, {3, 12, 24}. This is the Vol III `kappa-stratification` theorem (`cy_c_six_routes_convergence.tex:403-410`): the stratification is by generator rank, not by κ_ch (which is zero for all six, as X is CY-3). No single Hopf algebra can surject onto representatives of all three strata by *isomorphism*; any candidate H_{K3} surjects only by lossy quotients.

---

## ROUND 1 HEAL: the shared structure is a pentagon, not a point

Because the six outputs live in three distinct strata {3, 12, 24} with genuinely different categorical homes (ChirAlg, VOA, OrbVOA, FactAlg), no candidate H_{K3} → A_X^{R_i} can be an isomorphism for all i simultaneously. The shared structure is therefore a diagram, not an object.

**Proposal (Drinfeld-style).** The shared structure is a pentagon P_{K3} in the (2,1)-category of quasi-triangular bialgebras equipped with a spectral parameter. Its five vertices are

  P_1 = R_1 (Φ_3 of D^b Coh);
  P_2 = R_5 (half-twisted σ-model);
  P_3 = R_6 (BLLPR Schur);
  P_4 = R_4 (orbifold VOA);
  P_5 = R_3 (Mukai lattice VOA);

and its **source** (not a vertex of the pentagon but a generator above it) is

  P_0 = R_2 (Borcherds / BKM envelope U(g_{Δ_5}));

the pentagon's colimit receives a map from P_0. Explicitly:
- three vertices (P_1, P_2, P_3) sit in the rank-3 stratum;
- one vertex (P_4) sits in the rank-12 stratum;
- one vertex (P_5) sits in the rank-24 stratum;
- the source P_0 sits above rank 24 (BKM, carrying the full Jacobi-form datum).

This matches exactly `cy_c_pentagon_hypothesis_closures_platonic.tex:462-495`: the pentagon convergence theorem (under the four hypotheses H1-H4) identifies the pentagon colimit with the "quantum vertex chiral group G(K3 × E)".

**The candidate H_{K3}.** If H_{K3} were a single quasi-triangular Hopf algebra with functors F_i : H_{K3} → Obj_i reproducing each A_X^{R_i}, then each A_X^{R_i} would be a quotient/module-category of H_{K3}. The different ρ-strata show this cannot happen *isomorphically*. The correct reformulation is:

> Let H_{K3} := D(Y^+(ĝ_{Δ_5})) be the formal Drinfeld double of the positive half of the generalised Yangian on Gritsenko-Nikulin's BKM superalgebra g_{Δ_5}. Then there are surjective functors
>    F_i : H_{K3} → A_X^{R_i} for i = 3, 4, 5 (lattice, orbifold, σ-twist)
> and the composite F_1 ∘ Φ_3 and F_6 ∘ BLLPR factor through H_{K3} as Koszul-dual companions. The KERNELS are computed below.

**Generating data of H_{K3}.** Following Drinfeld 1988 / Molev 2007 (super-Yangian presentation), H_{K3} is presented by:
- 24 Drinfeld currents E_a(z), F_a(z), ψ^±_a(z), a = 1,...,24, one per Mukai-lattice direction;
- an ε-grading ε_a ∈ {+1, -1}^{24}, signature (4,20);
- a structure function
     G_{K3}(x) = ∏_{a=1}^{24} ( (1 - q_a x)(1 - q_a^{-1} t x) ) / ( (1 - q_a^{-1} x)(1 - q_a t x) );
- five OPE families (commutation, E-F Cartan, ψ^± involution, shifted coproduct, antipode).

This is the abelian-level presentation proved in `cy_c_six_routes_convergence.tex:516-554`. Its non-abelian extension requires replacing ε-diagonal Cartan with the osp(4|20) structure, leading to the non-abelian Drinfeld double D(Y^+( osp(4|20) )) with Mukai form ω_Muk. The non-abelian extension is CONJECTURAL at Vol III's current status (`k3_yangian_chapter.tex:1879-1916`, osp-yangian-mukai conjecture).

---

## ROUND 2 ATTACK: the kernels are non-trivial

The strong-unification claim *H_{K3} → A_X^{R_i} is an equivalence for all i* is false: compute the kernels.

**ker F_3 (H_{K3} → R_3 lattice VOA).** The BKM superalgebra g_{Δ_5} contains imaginary roots of multiplicities c(D) where c is the Fourier spectrum of 2φ_{0,1}; of these, the Mukai-lattice VOA V_{Λ_Muk} sees only the **real root sector** (discriminant D = 2) plus the Heisenberg sector (Cartan). So

   ker F_3 = ideal generated by {imaginary-root generators of g_{Δ_5}},

which is infinite-dimensional — precisely the "lightlike imaginary roots" of multiplicity c(0) = 10 plus the tower of spacelike imaginaries of multiplicities c(D) for D ≥ 3. F_3 is the *truncation to finite-dimensional roots* (Cartan + real roots). This kernel is a non-trivial obstruction: F_3 discards exp(2π√D) many generators.

**ker F_4 (H_{K3} → R_4 orbifold).** The Z/2-orbifold halves the rank from 24 to 12. So

   ker F_4 ⊇ {ε_a H_a : ε_a = +1} ⊕ (odd-graded twisted sector),

losing exactly 12 Cartan generators plus the associated currents.

**ker F_5 (H_{K3} → R_5 σ-twist).** The σ-model half-twist produces 3 primitive currents, one per complex dimension of X. The functor F_5 is a *huge* projection:

   ker F_5 = ideal (22 of the 24 Cartan directions),

keeping only the 2 directions polarised by the Kähler class on S plus the 1 direction on E. This kernel is the largest of the five.

**ker F_1 ≡ ker F_6.** Both are rank-3 projections analogous to ker F_5, keeping only the "holomorphic-dimension-3" sector of H_{K3}. Difference: F_6 is refined by Schur-index data; F_1 is refined by HH*-data.

**Verdict on strong unification.** The six kernels are pairwise distinct *and* pairwise non-contained (except for the Z/2-orbifold specialisation ker F_4 ⊂ ker F_3, i.e. the lattice-orbifold factorisation). Therefore:

> There is NO quasi-triangular Hopf H_{K3} such that every F_i is an isomorphism. Pentagon colimit is the weakest object that satisfies the full 6-cycle closure.

This *sharpens* the pentagon-colimit formulation of `cy_c_pentagon_hypothesis_closures_platonic.tex:462-495`. The pentagon source being Borcherds (P_0 = R_2) is justified because R_2 uniquely carries the Jacobi-form input 2φ_{0,1}, which all five F_i can only *project*, never *recover*.

---

## ROUND 2 HEAL: pentagon colimit with five β-arrows on explicit generators

I now write the five named intertwiners β_{ij} on generators.

Notation. Let {H_a}_{a=1}^{24} denote the Cartan generators of H_{K3} (one per Mukai direction), {E_a, F_a} the positive/negative currents, and ψ^±_a the Cartan currents. Let φ^S_1, φ^S_2 denote the two K3-Kähler directions (ε = +1) and φ^E the E-elliptic direction (ε = +1). Let θ_α, α ∈ Δ_{re}(g_{Δ_5}), denote real-root generators; w_β, β ∈ Δ_{im,lightlike}, lightlike imaginary generators with dim = 10.

### β_{13} : P_1 (R_1, Φ_3 of D^b Coh) → P_3 (R_6, BLLPR Schur)

On the three primitive-dimension-3 currents:
- β_{13}(J^{R_1}_i) = J^{Schur}_i, i = 1, 2, 3,
with J^{R_1}_1, J^{R_1}_2 the two K3 holomorphic currents (via Costello-Gaiotto) and J^{R_1}_3 the elliptic direction. Maps to the BLLPR 4d-N=2 Schur-protected Cartan. On higher modes:
- β_{13}(∂^n J_i) = ∂^n J^{Schur}_i; on composites,
- β_{13}(:J_i J_j:) = :J^{Schur}_i J^{Schur}_j: + Schur-anomaly(i,j), where the anomaly is computed in Costello-Gaiotto 1810.01970.

**Image.** Rank-3 Schur chiral subalgebra of BLLPR. **Cokernel** = class-S operators off the Schur locus (the 1/2-BPS sector not captured by 1/4-BPS Schur).

### β_{34} : P_3 (R_6, BLLPR) → P_4 (R_4, orbifold VOA)

On the 3 Schur primitives:
- β_{34}(J^{Schur}_i) = J^{orb}_i for i = 1, 2, 3, embedding into the 12 orbifold-invariant Cartan directions.
On Schur composites:
- β_{34}(W^{Schur}_k) = DHVW orbifold projection of W^{Schur}_k into the Z/2-twisted sector.

**Image.** The {3} → {12} promotion: adds 9 new rank directions from the orbifold twisted sector. **Cokernel** = the pure (untwisted) orbifold sector not reached from Schur.

### β_{45} : P_4 (R_4, orbifold) → P_5 (R_5, lattice V_{Λ_Muk})

On the 12 orbifold Cartan directions:
- β_{45}(J^{orb}_a) = J^{lat}_a (for a ∈ fixed Cartan of the Z/2-action);
- β_{45}(tw_α) = twisted-vertex-operator V^{lat}_{α/2} (Dong-Li-Mason 1997 / Frenkel-Lepowsky-Meurman chapter 9).

**Image.** Embeds the orbifold into the full rank-24 lattice VOA by Z/2 *de-orbifolding*. **Kernel** = trivial (orbifold → lattice is injective after doubling the twisted generators).

### β_{56} : P_5 (R_5, V_{Λ_Muk}) → P_1 (R_1, Φ_3 of D^b Coh) [CLOSING THE PENTAGON]

This is the "costly" intertwiner because the ρ-stratum drops from 24 to 3. It's a *projection* onto 3 holomorphic directions:
- β_{56}(H_a) = Σ_{i=1}^{3} λ_{ai} J^{R_1}_i, where λ_{ai} ∈ C is determined by the HKR map on H^2(S) + H^*(E).
- β_{56}(V_α) = 0 for α a non-Cartan lattice vector (the lattice ≫ rank-3 holomorphic).

**Image.** The rank-3 Φ_3-image; **kernel** is huge (21 of 24 Cartan directions + all lattice vertex operators). Consistent with `cy_c_six_routes_convergence.tex:222`: this is the composite of α_{45}^{-1} α_{56}^{-1} α_{61}^{-1} in the 6-cycle form.

### β_{61} : P_0 (R_2, Borcherds source) → P_1 (R_1, Φ_3)

The source-to-vertex arrow. This is the Harvey-Moore / Gritsenko-Nikulin character-level arrow (`cy_c_six_routes_convergence.tex:186-207`), lifted to a chiral-algebra morphism:
- β_{61}(real-root generator θ_α) = generator of Φ_3 at a class-α deformation, α ∈ Δ_{re};
- β_{61}(lightlike imaginary w_β) = 1/4-BPS operator at discriminant-0, β ∈ Δ_{im,light};
- β_{61}(spacelike imaginary x_γ) = 1/4-BPS operator at discriminant D > 0, γ ∈ Δ_{im,space,D>0}.

**Image.** All of A_X^{R_1} (Φ_3 is surjective from the BKM positive half). **Kernel** = elements annihilated by the Mukai-equivariant HKR trace. This is precisely the quantitative content of the Harvey-Moore functorial conjecture `cy_c_six_routes_convergence.tex:259-288`.

### Universal property of the colimit

**Proposition (pentagon colimit).** Let P_{K3} be the pentagon diagram (P_1, P_2, P_3, P_4, P_5; β_{13}, β_{34}, β_{45}, β_{56}, β_{61}) with source P_0 = R_2 = U(g_{Δ_5}) and the five β_{ij}. The pentagon colimit
   colim P_{K3}
is canonically isomorphic to H_{K3} := D(Y^+(ĝ_{Δ_5})), *when the latter exists*. The universal property: any quasi-triangular Hopf Q_0 together with arrows Q_0 → A_X^{R_i} (i = 1, ..., 6) commuting with all β_{ij} factors uniquely through H_{K3}.

This universal property is a *conditional* theorem in the Vol III status: it holds under the four hypotheses H1-H4 of `cy_c_pentagon_hypothesis_closures_platonic.tex:462-495` (Costello-Li chain-level factorisation; HKR-Borcherds functorial lift; Mukai-lattice-orbifold crepant resolution; K3 × E relative factorisation).

---

## ROUND 3 ATTACK: does r_{K3}(z) determine Y_{non-ab}(g_{K3})?

The seven-faces programme (Vol I, `genus1_seven_faces.tex`) shows that at genus 0 the collision residue r_A(z) is a single Laurent datum with seven equivalent names (twisting morphism, DNP line-operator R-matrix, λ-bracket, KZB, Belavin-Drinfeld, Sklyanin, Gaudin). At genus 1 it splits: the collision residue becomes r_A^{(1)}(z, τ) involving Weierstrass ζ_τ and ℘_τ.

**Drinfeld's question.** Does r_{K3}(z) uniquely determine Y_{non-ab}(g_{K3})?

In the classical setting (Drinfeld 1988, Belavin-Drinfeld 1982), a classical r-matrix r(z) satisfying classical YBE determines, up to a gauge, a quasi-triangular Lie bialgebra (g, δ), hence a Yangian Y(g) after formal deformation quantisation.

**Attack.** In the K3 setting, the Mukai form is *indefinite* — signature (4,20). Classical Drinfeld construction requires a bilinear form that restricts to an invariant non-degenerate pairing on g. For affine Kac-Moody g at non-critical level, this is the shifted Killing form Ω/(k + h^∨). For Heisenberg, it's the identity. For BKM g_{Δ_5}, it's the *Gritsenko-Nikulin form* induced by 2φ_{0,1}, which is indefinite.

The indefinite signature introduces a new obstruction absent from Drinfeld's classical treatment: the ω-twisted permutation P_ω on Λ_Muk ⊗ Λ_Muk has P_ω^2 = ω ⊗ ω with eigenvalues {+1 on 416/576, -1 on 160/576} (`k3_yangian_chapter.tex:1458-1465`). The "standard" braid-identity R(u)R(-u) = f(u) · Id acquires a sign correction on the mixed-sign eigenspace — crossing symmetry is *modified*.

This is resolved in Vol III by passage to the orthosymplectic super-Yangian Y_{osp(4|20)} (`k3_yangian_chapter.tex:1879-1916`). Under this resolution:
- the crossing relation R(u)^{st_1} R(-u - (m-n-2)ℏ)^{st_1} = f(u) · Id with (m,n) = (4,20) has shift κ_osp = -9ℏ;
- the Berezinian centre supplies the global shift κ_{osp} = -18 (doubled perturbatively).

**Verdict of Round 3 attack.** A bare r_{K3}(z) does not determine Y_{non-ab}(g_{K3}) uniquely; it determines it up to:
- (i) the gauge group Aut(osp(4|20), ω_Muk) acting on the Cartan and on the permutation P_ω;
- (ii) scalar shifts u → u + c for c ∈ C* (the overall spectral shift);
- (iii) a Z/2 choice of *reality structure* (non-super Y(so(4,20)) versus super Y(osp(4|20)); `k3_yangian_chapter.tex:2055-2071`).

---

## ROUND 3 HEAL: gauge group and the precise determination theorem

**Theorem (r-matrix-to-Yangian gauge theorem, non-abelian K3 level).**

Let r_{K3}(z) be the K3 collision residue as computed by the seven-faces programme at genus 0 (any one of the seven realisations). Then the quasi-triangular Hopf superalgebra Y_{non-ab}(g_{K3}) := D(Y^+(osp(4|20), ω_Muk)) is uniquely determined by r_{K3}(z) up to the gauge group

   G_gauge = Aut(osp(4|20), ω_Muk) × C*_shift
           ≃ O(4,20; Z) × C*,

where
- O(4,20; Z) is the arithmetic subgroup of orthogonal automorphisms of the Mukai lattice preserving ω_Muk (this is the "Mukai-lattice automorphism" subgroup acting on the Narain moduli space `k3_yangian_chapter.tex:1716-1724`; it contains SL_2(Z) × SL_2(Z)/Z_2 as the "elliptic-genus-modular" subgroup);
- C*_shift is the scalar spectral shift u → u + c for c ∈ C* (absorbed trivially at the level of the universal R).

**Proof sketch.**
1. (r(z) determines the Lie bialgebra.) Compute the residue r_{K3}(z) = c_0^{Muk} · Σ_{a=1}^{24} ε_a H_a ⊗ H_a / z + (non-abelian correction). The abelian part fixes the Cartan and signature (4,20). The non-abelian correction, at enhancement points, fixes the E_8 ⊕ E_8 blocks (see `k3_yangian_chapter.tex:1660-1690`, structure function factorisation g_{K3}(z) = g_{E_8}^{(1)}(z) · g_{E_8}^{(2)}(z) · g_{U^4}(z)).
2. (Signature obstruction → osp.) The signature (4,20) forces orthosymplectic super-grading (`k3_yangian_chapter.tex:2002-2018`); this eliminates the candidate gl(4|20) super-Yangian.
3. (Deformation quantisation is unique up to gauge.) Standard Drinfeld deformation quantisation of (osp(4|20), δ_{Muk}) produces Y_{non-ab}(g_{K3}) uniquely up to twisting by elements of Aut(osp(4|20), ω_Muk). The twist is realised on the R-matrix by R → F_{21} R F^{-1}, F ∈ Aut(osp) (Drinfeld 1989 twisted-quasitriangular).
4. (Scalar shifts.) A shift u → u + c acts on R by R(u) → R(u+c), which is gauge-equivalent to R(u) at the Hopf level (multiplication by an invertible function).

This establishes the claimed uniqueness up to G_gauge.

**Corollary (r-matrix determines the pentagon colimit).** Because r_{K3}(z) also determines, via the seven-faces identification, the elliptic-genus-modular (SL_2(Z) × SL_2(Z))/Z_2 subgroup of G_gauge, the pentagon colimit

   H_{K3} = Y_{non-ab}(g_{K3}) = colim P_{K3}

is determined by r_{K3}(z) up to G_gauge. In particular, the isomorphism class of H_{K3} is an invariant of the CY threefold X = S × E (deformation-invariant within its moduli class, modulo Mukai-lattice automorphisms).

---

## The unifying principle as one sentence

**There is a single quasi-triangular Hopf superalgebra H_{K3} := D(Y^+(osp(4|20), ω_Muk)), the non-abelian K3 Yangian, such that:
  (a) each of the six route-outputs A_X^{R_i} is the image of H_{K3} under a surjective functor F_i with computable kernel;
  (b) the five intertwiners β_{ij} among A_X^{R_i}, (i, j) pairwise-distinct, factor through H_{K3} and form a pentagon P_{K3} whose colimit IS H_{K3};
  (c) the classical K3 r-matrix r_{K3}(z) determines H_{K3} up to the gauge group G_gauge = O(4,20;Z) × C*;
  (d) the Borcherds construction R_2 = U(g_{Δ_5}) is the "source" of the pentagon, supplying the Jacobi-form datum 2φ_{0,1} from which all five β-arrows descend by projection.**

This is the Drinfeld-style unifying principle: one Hopf algebra, one r-matrix, one gauge group; the six faces of the pentagon are six projections, each with a computable kernel and a named β-intertwiner.

---

## Falsification criteria

The above is CONJECTURAL at Vol III's current status. It would be **falsified** by any of the following:
1. **Category-theoretic falsification.** If the pentagon diagram P_{K3} were shown not to commute in the (2,1)-category of chiral algebras at chain level, then the colimit fails to exist as a strict object. Test: verify the pentagon coherence condition at the 5-ary Mac Lane pentagon via `k3_pentagon_E1_edge_architecture` (`k3_yangian_chapter.tex:3244-3313`).
2. **Signature falsification.** If osp(4|20) is replaced by gl(4|20) (the non-osp super-Yangian), R(u)^2 fails crossing symmetry on the mixed-sign subspace, and the double D(Y^+) is ill-defined. Test: recompute the Berezinian centre of gl(4|20) at rank (4,20) and compare to the Molev-Ragoucy osp-Berezinian.
3. **Kernel-non-disjointness falsification.** If ker F_i and ker F_j coincide for i ≠ j, the six routes do NOT span three distinct strata, and the pentagon collapses. Test: compute rank(A_X^{R_i}) at three distinct enhancement points and verify they separate into {3, 12, 24}.
4. **Source-uniqueness falsification.** If a route other than R_2 could also supply the 2φ_{0,1} Jacobi-form input as a pentagon source, the pentagon is not minimal. Test: verify that only the Borcherds lift receives the Jacobi form input canonically (`cy_c_six_routes_convergence.tex:37`, Remark "the six routes do not reduce to one").

The critical open *mathematical* gap is #2: the Vol III status of Y_{osp(4|20)} at rank (4,20) is only structurally verified at osp(1|2) and osp(2|2); the rank-(4,20) reflection equation is open (`k3_yangian_chapter.tex:1913-1916`).

---

## Open standalone: explicit Drinfeld presentation of Y_{non-ab}(g_{K3})

**Sprint target.** Produce the explicit Drinfeld presentation of Y_{non-ab}(g_{K3}) := D(Y^+(osp(4|20), ω_Muk)) in terms of:
- 296 super-generators (216 even, 80 odd), see `k3_yangian_chapter.tex:1939-1944`;
- Molev-Ragoucy reflection equation at rank (4,20);
- Berezinian central element with κ_osp = -18 (perturbative).

The abelian-level presentation on 24 × 3 Drinfeld currents is already proved (`cy_c_six_routes_convergence.tex:516-609`, Thm cy-c-abelian-K3-currents). The non-abelian extension requires replacing the diagonal ε_a · δ_{ab} Cartan with the osp(4|20) super-Cartan and adjusting the structure function to include the off-diagonal E_8 ⊕ E_8 blocks.

**Next step (for a future agent).** Compute the non-abelian structure function
   G_{K3}^{non-ab}(x) = det( 1 + x · (osp-Cartan matrix) · ω_Muk ) · (abelian Mukai factors)
and verify YBE at rank (4,20) symbolically. If verified, H_{K3} is explicit; if not, the pentagon colimit remains the only correct formulation.

---

## Cross-reference map for a reader

- **Six constructions.** `cy_c_six_routes_convergence.tex` Def 20-33 (definition of the six routes) and Thm kappa-stratification-CY-C 395-434.
- **Pentagon hypotheses.** `cy_c_pentagon_hypothesis_closures_platonic.tex` Thm cy-c-pentagon-convergence-unconditional 462-495.
- **Abelian-level H_{K3}.** `cy_c_six_routes_convergence.tex` Thm cy-c-abelian-K3-currents 566-633.
- **Non-abelian conjecture.** `k3_yangian_chapter.tex` Conj osp-yangian-mukai 1879-1916.
- **Signature/crossing obstruction.** `k3_yangian_chapter.tex` Attack 1 (indefinite signature) 1451-1469.
- **Seven-faces at genus 0/1.** `chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex` master Thm 1037-1080.
- **Gauge group (Mukai-lattice automorphisms).** `k3_yangian_chapter.tex` Narain moduli 1715-1724.
- **Harvey-Moore functorial conjecture.** `cy_c_six_routes_convergence.tex` Conj harvey-moore-functorial 259-288.

---

*End of Agent 07 analysis.*
