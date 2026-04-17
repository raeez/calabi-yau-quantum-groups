# Birational invariance of CY-A functor Φ at d=3: attack and heal

**Question.** For birational CY_3 varieties X and X' (chain of flops), does the programme's functor Φ: CY_3 → E_1-chiral-algebra (Vol III Thm cy-to-chiral-d3) send them to the same object? If so, at what equivalence level?

Bridgeland 2002 proved D^b(Coh(X)) ≃ D^b(Coh(X')) for flop-equivalent CY_3 as a derived equivalence (an exact equivalence of triangulated categories, refined by Keller-Yang/Bridgeland-Maciocia to an A_∞-quasi-equivalence of dg-enhancements). Kawamata 2002 conjectured (and proved in many cases) the sharper statement that two K-equivalent smooth varieties are D-equivalent. The programme's Φ — bar-cobar-of-(Ginzburg-dg-algebra-of-D^b(Coh(X))) — inherits this structure, but the inheritance level requires care.

---

## Three-step protocol

### (a) What the claim Φ(X) ≃ Φ(X') gets RIGHT

Exactly the ghost theorem extracted from the Bondal-Orlov / Bridgeland input, restricted to the invariants Φ sees:

1. **Same CoHA up to E_1-quasi-isomorphism.** prop:mutation-e1-equivalence (cy_to_chiral.tex:2695; 155 tests in test_mutation_e1_equivalence.py) proves that every Fomin-Zelevinsky mutation μ_k corresponding to a crossing of a flop wall in Stab(D^b(X)) induces an E_1-algebra quasi-isomorphism μ_k^*: CoHA(Q,W) →^{≃_{E_1}} CoHA(Q',W'). Keller-Yang 2011 delivers the underlying derived equivalence; cyclic A_∞-preservation is the extra content.

2. **Same κ_ch.** prop:flop-koszul-duality(iii) (cy_to_chiral.tex:2727): κ_ch is a derived invariant, and the flop is a derived equivalence, so κ_ch(A_X) = κ_ch(A_{X^+}). This is locked down by the categorical Euler characteristic computation (Shklyarov): κ_ch reads only HH-data of the dg-enhancement.

3. **Same shadow class and same κ_BKM.** Shadow class (G/L/C/M) is a derived invariant because it is computed from bar H^*(A_X); bar cohomology depends on A_X only up to E_1-quasi-isomorphism. κ_BKM = c_N(0)/2 depends only on the structure function, hence only on Mukai-lattice-level data (AP-CY37) — preserved by any derived autoequivalence.

4. **Same DT generating function up to chamber relabeling.** Kontsevich-Soibelman wall-crossing implies Z_DT is chamber-independent; the flop relabels chambers but preserves Z_DT (conifold: Z_DT(Q) = Z_DT(Q^{-1}) after factoring M(q)^2, dt_flop_formula in flop_koszul_duality.py:874). Atkin-Lehner for local P^1 × P^1.

### (b) What the claim gets WRONG

Five precise conflations to block:

1. **"Isomorphism" vs. "quasi-isomorphism" vs. "equivalence-in-E_1-ChirAlg-∞-category".** Φ(X) and Φ(X') are NOT isomorphic as dg-E_1-chiral-algebras on the nose — they are chart-indexed hocolims from distinct atlases. They ARE quasi-isomorphic via an explicit zigzag of mutations. The correct language is "equivalent in E_1-ChirAlg_∞", not "equal". The conifold atlases {K_2, K_2^op} for X and {K_2^op, K_2} for X^+ differ as ordered tuples.

2. **"Flop is Koszul duality" (AP-CY10 — PROSCRIBED).** cy_to_chiral.tex:2735 carries a RECTIFICATION-FLAG deletion of the prior prop:flop-e1-koszul — Koszul duality sends κ → −κ (or κ + κ^! = ρ_K for a conductor), while the flop preserves κ. Different operations: flops exchange chambers in Mukai motion; Koszul exchanges algebra and coalgebra. CLAUDE.md:254-256 enforces this.

3. **Atlas invariance vs. "flop-invariance as a canonical definition".** Φ depends on a choice of atlas {(Q_α, W_α)} of stability chambers. Atlas-independence of A_X = hocolim_α CoHA(Q_α, W_α) is proved for toric CY_3 via thm:toric-chart-gluing (cy_to_chiral.tex:2628), using that (i) mutations are E_1-quasi-isos, (ii) the hocolim is well-defined, (iii) κ_ch is a derived invariant. For NON-toric birational-equivalent CY_3 (e.g. compact quintic with node resolutions), atlas existence itself is conjectural (def:quiver-chart-atlas is ClaimStatusConjectured at :2554).

4. **Spectral R-matrix identification.** R-matrices R_α(z), R_β(z) on the two sides are only gauge-equivalent, not equal: R_β(z) = (g_{αβ} ⊗ g_{αβ}) R_α(z) (g_{αβ}^{-1} ⊗ g_{αβ}^{-1}) (cy_to_chiral.tex:2680). The E_2 braiding on the Drinfeld center Z(Rep^{E_1}(A)) is preserved up to gauge conjugation — this is what one would naively call "the R-matrix is flop-invariant", but the gauge transformation is nontrivial and visible in the RTT presentation.

5. **Compact-case conjecturality.** For a compact quintic X_5 ⊂ P^4, the quiver-chart atlas at large volume uses the Beilinson tilting bundle restriction; at the Gepner point one has MF(W_Fermat), which is NOT a quiver chart (rem:gepner-lv-dichotomy, cy_to_chiral.tex:3458). Flop-invariance for compact quintics at a nodal/small-resolution transition is therefore conditional on (i) the conjectural atlas, (ii) the Kapranov-tilting conjecture (wave_compact_CY_B_d3_quintic.md), (iii) finiteness of the atlas across the node.

### (c) Correct relationship

The precise statement, healed to strongest honest form:

> **Theorem candidate (Φ-flop-invariance for CY_3).** Let X, X' be smooth CY_3 varieties that are birationally equivalent via a chain of (−1,−1)-curve flops (equivalently: K-equivalent via flops, in the sense of Kawamata 2002). Assume either (a) both X, X' are toric CY_3, or (b) both are local (noncompact) CY_3 admitting finite quiver-chart atlases, or (c) CY-A_3 holds (cy-to-chiral-d3) with atlas-existence. Then:
>
> 1. **E_1-equivalence.** Φ(X) ≃ Φ(X') as objects of the ∞-category E_1-ChirAlg, via a zigzag of mutation-induced quasi-isomorphisms indexed by the flop chain.
>
> 2. **Invariants.** κ_ch(Φ(X)) = κ_ch(Φ(X')); shadow class coincides; κ_BKM coincides; κ_fiber = rank(Mukai lattice) coincides (AP-CY55).
>
> 3. **Gauge-equivalent R-matrices.** The spectral R-matrices R_{Φ(X)}(z), R_{Φ(X')}(z) on eval-module cores of the Drinfeld centers Z(Rep^{E_1}(Φ(X))), Z(Rep^{E_1}(Φ(X'))) are Maulik-Okounkov-gauge conjugate; the induced E_2 braidings on Mod_{Φ(X)} and Mod_{Φ(X')} are equivalent as braided monoidal (∞,1)-categories.
>
> 4. **NOT an isomorphism.** Φ(X) and Φ(X') are not in general strictly isomorphic as dg-E_1-chiral-algebras, even for the conifold. The two atlases {(Q_α, W_α)} differ as ordered tuples; the quasi-inverse direction of the mutation zigzag is only defined up to homotopy.
>
> 5. **Distinction from Koszul duality.** Φ(X^+) ≠ Φ(X)^! (AP-CY10). Koszul duality X → X^! corresponds to a CY transition (resolved ↔ deformed conifold, with κ → −κ), not to a flop.
>
> **Status.** (1)–(4) are PROVED for the resolved conifold (134 tests in test_flop_koszul_duality.py). Proved for local P^1 × P^1 (Atkin-Lehner), local del Pezzo dP_n for n ≤ 5 (mutation of exceptional collection). CONDITIONAL on CY-A_3 for smooth noncompact toric CY_3 via thm:toric-chart-gluing. CONDITIONAL on the atlas-existence conjecture for birational non-toric CY_3 (e.g. compact quintic with node resolutions). (5) is the AP-CY10 guard.

### Conifold explicit Φ-analysis

Let X = Tot(O(−1) ⊕ O(−1) → P^1), X^+ = flop. Both have chi(X) = chi(X^+) = 2, κ_ch = 1, shadow class G, depth 2.

- **Atlases.** Atlas(X) = {σ_I = K_2 with arrows 1→2 twice, σ_II = K_2^op with arrows 2→1 twice}. Atlas(X^+) = {σ_I' = K_2^op, σ_II' = K_2} — chart labels swapped.
- **Φ(X), Φ(X^+) as hocolims.** Both equal the hocolim over their 2-chart diagrams of the Klebanov-Witten CoHAs. The underlying dg-E_1-chiral-algebras are DIFFERENT presentations (different chart orderings) of the SAME homotopy type. The mutation μ_1: (K_2, 0) → (K_2^op, 0) is an E_1-quasi-isomorphism (prop:mutation-e1-equivalence; Seiberg duality on Klebanov-Witten).
- **Flop functor.** On K-theory, F = [[0,1],[1,0]] exchanges simples S_1 ↔ S_2. F is Fourier-Mukai with kernel O_Z where Z = X ×_{X_0} X^+ (Bondal-Orlov / Bridgeland). F^2 = id on K-theory.
- **Verdict.** Φ(X) ≃ Φ(X^+) in E_1-ChirAlg_∞, NOT Φ(X) = Φ(X^+).

### Compact quintic explicit Φ-analysis

Let X ⊂ P^4 be a smooth quintic with 2-parameter family degenerating to X_0 with isolated node(s). Small resolutions X, X^+ (when a node admits two crepant resolutions of P^1 type) are flop-equivalent. For a quintic, the number of nodes that admit small resolutions constraints h^{1,1} change: standard example 16-node quintic (h^{1,1} jumps from 1 to 17).

- **Atlas.** Two charts (cy_to_chiral.tex:3458): (i) large-volume Beilinson-type tilting chart, (ii) Gepner MF(W_{Fermat}) chart — NOT a quiver chart. Flop-invariance at the nodal transition is NOT treated as a pure quiver-chart mutation in the manuscript.
- **Invariants.** κ_ch(A_{quintic}) = −25/3 (cy_to_chiral.tex:3452); same for X, X^+ by PTVV + derived invariance of Shklyarov pairing. κ_top(X) = κ_top(X^+) = −200 (NOT true in general for node resolutions with h^{1,1} jump; the h^{2,1} change offsets); shadow class M (r_max = ∞).
- **Status.** Φ(X) ≃ Φ(X^+) is CONDITIONAL on (a) CY-A_3, (b) atlas existence for compact quintic (Kapranov tilting conjecture, wave_compact_CY_B_d3_quintic.md point 5: refuted in strict sense, open with derived tilting), (c) extension of prop:flop-koszul-duality to small-resolution transitions where h^{1,1} jumps. The toric toolkit (thm:toric-chart-gluing) does NOT apply.

### Universality: when is Φ(X) = Φ(X')?

The sharp formulation of (3) from the brief:

> **Universality reformulation.** For smooth projective CY_3 X, X' with CY-A_3 (providing Φ), the following are equivalent in the programme:
> (α) Φ(X) ≃ Φ(X') in E_1-ChirAlg_∞;
> (β) There is an A_∞-quasi-equivalence D^b(Coh(X)) ≃ D^b(Coh(X')) that preserves the CY_3 cyclic structure (the Shklyarov trace);
> (γ) On the Mukai-lattice level, (H^*(X,Z), (,)_Muk) ≃ (H^*(X',Z), (,)_Muk) as Mukai lattices, AND the derived equivalence is bounded-t-exact-up-to-shift on heart filtrations.

Flops are the tautological case: Bondal-Orlov produces (β), which implies (α). Kawamata 2002 shows birational CY_3 are K-equivalent ⇒ D-equivalent ⇒ Φ-equivalent in the programme. The converse "Φ(X) ≃ Φ(X') ⇒ X birational to X'" is FALSE in general (Mukai's Abelian/K3-surface examples give D-equivalent non-birational varieties in d = 2, expected in d = 3: Namikawa's hyperkähler twins, Borisov-Căldăraru-Perry).

So the correct universal statement is:

> **Birational ⇒ Φ-equivalent, NOT ⇐.** For smooth CY_3, X and X' birational (equivalently: K-equivalent) implies Φ(X) ≃ Φ(X') (Bridgeland + cyclic-A_∞-preservation + hocolim). The converse fails because derived equivalence is strictly weaker than birational equivalence on smooth CY_3.

---

## Verdict

**Φ(flop) ≃ Φ, NOT Φ(flop) = Φ.** E_1-equivalence in E_1-ChirAlg_∞, via an explicit mutation zigzag. κ_ch, κ_BKM, κ_fiber, shadow class preserved. R-matrices gauge-equivalent (Maulik-Okounkov). Proved for conifold/toric/local dP_n; conditional for compact quintic (CY-A_3 + atlas existence). NEVER an isomorphism of dg-E_1-chiral-algebras; NEVER a Koszul duality (AP-CY10). Birational ⇒ Φ-equivalent; converse fails.
