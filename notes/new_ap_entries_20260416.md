# Proposed New AP-CY Entries from 2026-04-16 Vol I Adversarial Swarm

**Date:** 2026-04-16
**Coverage:** Waves 1–5 complete + wave 6 running. ~16 agent reports.
**Status:** Proposed entries. NOT yet inserted into CLAUDE.md (per user "don't edit the file"). To be reviewed and merged.

The existing Vol III AP catalogue ends at AP-CY67. New entries continue from AP-CY68. Entries are organized by theme. Each carries:
- The wrong-claim template (so future authors recognize it)
- The ghost theorem (the strongest correct statement)
- Counter-template (decision rule for new content)
- Worked instance(s) from the swarm with file:line citations

---

## Theme A — Function-value vs principal-value at poles

### AP-CY68. Principal-value mean of a divergent function is not a function value
- **Wrong claim template.** "The function f at the fixed point z₀ of an involution σ takes the symmetric mean value `(f(z₀⁺) + f(z₀⁻))/2`" — when f has a pole at z₀.
- **Ghost theorem.** The polynomial / rational identity `f(z) + f(σ(z)) ≡ K` (constant) is structural and TRUE; it implies that `f − K/2` is odd in a centered variable. The fixed point is the LOCATION of a pole, not the SITE of a value.
- **Worked instance.** `kappa(BP_{−3}) = 49/3` in `bp_self_duality.tex` (Prop 4.7 acknowledges, dropped in `five_theorems_modular_koszul.tex` L2551–2554, `koszulness_fourteen_characterizations.tex` L1315–1316). The correct theorem is `c(BP_k) + c(BP_{−k−6}) ≡ 196`; equivalently, in `u = k+3`, `c − 98 = −24u − 96/u` is odd. Sympy-verified 2026-04-16.
- **Counter-template.** Before writing "the value at the fixed point is X", evaluate the limit from both sides. If the limits differ (or diverge), the value does not exist. Restate as a polynomial-identity theorem of the conductor `K = f(z) + f(σ(z))`.

### AP-CY69. Critical level coincides with involution fixed points
- **Wrong claim template.** Writing kappa formulas as `c/n` (Heisenberg n=1, Vir n=2, BP n=6, ...) without a remark on critical-level singularities.
- **Ghost theorem.** The critical level k = −h^v of an affine Lie algebra is the Sugawara denominator pole; for any DS reduction (W_n, BP, ...) the critical level inherits divergent behaviour. Where an involution `k ↔ −k − 2h^v` exists, k = −h^v is its fixed point — and is also where every `c/n` formula diverges.
- **Counter-template.** Document the critical-level singularity ONCE per family with an explicit remark: "kappa(family_k) is undefined at k = −h^v(g); the conductor `K = kappa(k) + kappa(−k − 2h^v)` is a polynomial identity in k that remains finite as k → −h^v."

---

## Theme B — Independence and bundling

### AP-CY70. False independence: two proofs sharing a load-bearing input lemma
- **Wrong claim template.** "We give two independent proofs of Theorem T" — when both proofs invoke the same lemma L as input.
- **Ghost theorem.** The two proofs are independent POST-INPUT but share input L; the theorem is proved CONDITIONALLY on L by two independent reductions.
- **Worked instance.** T4 in `five_theorems_modular_koszul.tex`: Proof A (GRR/Arakelov–Faltings) and Proof B (clutching) both take `[B^(g)_scalar(A)]^vir = κ·[E]` as input. The remark "the two proofs have no logical dependency on each other" is overstated.
- **Counter-template.** Before writing "two independent proofs", list the lemmas used in each. Lemmas in the intersection are "shared inputs" — state explicitly whether the theorem is proved (a) unconditionally by both, (b) conditionally on shared lemma L by both, (c) one unconditionally and one conditionally.

### AP-CY71. Theorem-bundling under one ProvedHere
- **Wrong claim template.** Statement T = "T1 and T2 and T3" tagged with one `\ClaimStatusProvedHere`, but the proof only addresses T1 directly; T2, T3 are invoked as known.
- **Ghost theorem.** The bundled statement is provable iff each component is. Bundling under one tag obscures which is actually proved here.
- **Worked instance.** T1 in `five_theorems_modular_koszul.tex` L684–697: bar-cobar adjunction + Verdier intertwining + Koszul-conditional iso bundled as one ProvedHere. Step 3 uses FG12 chiral Koszul duality at cohomology presupposing the Koszul condition; `A^!_∞` named twice but never constructed.
- **Counter-template.** Before writing a ProvedHere theorem with multiple conjuncts, split into atomic lemmas, prove each, then assemble. Bundling is fine ONLY if each conjunct is independently established with citation.

### AP-CY72. Tautological "two independent methods" for a numerical value
- **Wrong claim template.** "We verify shadow value S_n by two independent methods M1 and M2" — when M1 and M2 are algebraic restatements of the same recursion.
- **Ghost theorem.** Two methods are independent verification only if they invoke different algorithmic / mathematical content. Same recursion in different syntax is one method.
- **Worked instance.** Vol I `compute/lib/shadow_tower_ope_recursion.py`: `mc_recursion_rational` and `sqrt_ql_rational` are algebraically identical (both restate `H² = t⁴ Q`).
- **Counter-template.** Before claiming independent methods, name a primitive that one uses and the other does not. Genuinely independent verification: e.g., direct 5-point Wick contraction giving `m_5 = 775/5184` (Vol III analog) vs MC recursion (Vol I currently lacks).

---

## Theme C — Convention & label hygiene (extending AP126/AP141/AP151)

### AP-CY73. Bridge identity between two conventions of an algebraic object
- **Wrong claim template.** Equating expressions in two different conventions (trace `r = kΩ/z` vs KZ `r = Ω/((k+h^v)z)`) without rescaling.
- **Ghost theorem.** The two conventions are RELATED by an explicit rescaling of generators and z; they are not equal but isomorphic-after-rescaling.
- **Worked instance.** `chiral_chern_weil.tex:458` and `holographic_datum.tex:635`: `k Ω_trace = Ω/(k+h^v)`. At k=0 LHS=0, RHS≠0; at k=−h^v LHS finite, RHS diverges. They cannot be equal at any k.
- **Counter-template.** Before writing a "bridge identity", verify at boundary cases (k=0, k=−h^v, c=0). Boundary disagreement means the identity is false — provide the rescaling instead.

### AP-CY74. Convention clash within a single family of papers
- **Wrong claim template.** Different files in the same chapter use different conventions for the same symbol without a bridge.
- **Ghost theorem.** Two conventions are intertranslatable but produce different formulas at face value.
- **Worked instances.**
  - `drinfeld_kohno_bridge.tex` (Drinfeld `q = exp(πi/(k+h^v))`) vs `en_koszul_duality.tex` (Kazhdan `q = exp(2πi/(k+h^v))`). They differ by a SQUARE.
  - `three_parameter_hbar.tex`, `garland_lepowsky.tex`, one occurrence in `virasoro_r_matrix.tex`: KZ-form r = Ω/((k+h^v)z); other files: trace r = kΩ/z. `three_parameter_hbar.tex:173` derives κ_cl in trace-form from a KZ-form r without rescaling.
  - Heisenberg ordered bar in `chapters/` + 5 standalones uses curved with R(z) = exp(kℏ/z); `e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex` use linear with r(z) = k/z and no curvature.
- **Counter-template.** A "Conventions" appendix per topic naming canonical convention with bridge identities. Before any cross-file derivation, state convention in force.

### AP-CY75. Operator-exponential factor cannot be absorbed into "contour normalization"
- **Wrong claim template.** `R = e^{2πi · Ω/(k+h^v)}` written equal to `e^{Ω/(k+h^v)}` "after absorbing the 2πi into contour normalization."
- **Ghost theorem.** Constants of the EXPONENT of an operator exponential cannot be absorbed into contour normalization — only contour-rescalings of MULTIPLICATIVE prefactors of the integral can. The Kazhdan–Lusztig R-matrix is `R = q^Ω` with `q = exp(2πi/(k+h^v))`; the 2πi is real content.
- **Worked instance.** `drinfeld_kohno_bridge.tex` L602–606 (and recurrence in sl_2 matrix display L1568–1581).
- **Counter-template.** When simplifying an operator exponent, verify that the absorbed factor is a scalar prefactor of the integral, not a coefficient of the operator in the exponent.

### AP-CY76. Wrong central charge formula
- **Wrong claim template.** Writing a central-charge formula by analogy that disagrees with the literature value at admissible level.
- **Ghost theorem.** The FKR formula for BP central charge is `c(BP_k) = 2 − 24(k+1)²/(k+3)`. At k=−3/2 this gives c=−2 (the triplet value).
- **Worked instance.** `koszulness_fourteen_characterizations.tex` L1298: `c(k) = (k−1)(6k+1)/(k+3)` gives c(−3/2)=40/3, contradicting c=−2.
- **Counter-template.** Verify central-charge formulas at admissible level (the smallest non-trivial k value of the family). Mismatch with the literature value flags the formula.

---

## Theme D — Native vs derived structure (extending AP-CY3, AP-CY56, AP153, AP154)

### AP-CY77. AP154 in Vol I: algebraic vs topological E_3 universally conflated
- **Wrong claim template.** Tagging the output of HDC (Higher Deligne Conjecture / Kontsevich) as "topological E_3" when HDC produces ALGEBRAIC E_3.
- **Ghost theorem.** Two distinct E_3 structures: (a) algebraic E_3 from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3 from Sugawara topologisation, requires a conformal vector at non-critical level. These agree on cohomology under topologisation but not at chain level.
- **Worked instances.** `en_chiral_operadic_circle.tex` L1973–L1983 ("eq. 6.1" cascade) tags arrow 4 output as "E_3-top"; `chapters/theory/en_koszul_duality.tex` and `derived_langlands.tex` likely repeat. The topologisation step (Thm 5.1/5.5 of operadic_circle) is the additional structure required to pass from algebraic to topological.
- **Counter-template.** Always tag E_3 as `E_3^{alg}` (Deligne) or `E_3^{top}` (topologisation, requires conformal vector). State whether formality is assumed.

### AP-CY78. Operadic-circle confabulation (E_3 → E_2 → E_1 → E_2 → E_3)
- **Wrong claim template.** Presenting a closed circle of E_n structures as "the operadic circle" when only some arrows are theorems.
- **Ghost theorem.** A 6-arrow zigzag of constructions: B^ord → Comod → Drinfeld center Z → End-of-id = chiral Hochschild → ... — with each arrow tagged Theorem / Definition / Conjecture.
- **Worked instance.** `en_chiral_operadic_circle.tex` Eq. 6.1 (L1973–L1983): 5 arrows. Arrow 1 (restriction) is a definition; arrow 4 (HDC) is scope-inflated (AP153); arrow 5 (closing) is conjectural. Only 2/5 are theorems. The "closed circle" is rhetorical packaging.
- **Counter-template.** For any E_n cascade claim: list each arrow with status (Thm/Def/Conj), the ambient category at each node, and whether the cascade closes or zigzags.

### AP-CY79. Vir has no Yangian; "Y(Vir_c)" is confabulation
- **Wrong claim template.** Naming a structure "Y(Vir_c)" or "Gravitational Yangian Y(Vir_{13})" — Virasoro has no construction-of-record as a Yangian in the literature.
- **Ghost theorem.** The shadow obstruction tower at c=13 is an infinite sequence of conserved-charge invariants with special symmetry structure. It HAS Yangian-like RTT structure asymptotically; whether this lifts to a presentation Y(Vir_c) is open.
- **Worked instance.** `three_dimensional_quantum_gravity.tex` sec:gravitational-yangian L2645–2798.
- **Counter-template.** Before naming a structure "Y(g)" or "Y(...)", verify the Yangian has been constructed in the literature for that g, or explicitly mark the construction as conjectural.

### AP-CY80. Coupling-inversion mislabel of additive symmetry
- **Wrong claim template.** Calling the additive central-charge reflection `c ↔ K − c` (Feigin–Fuchs / Verdier) "S-duality" — S-duality is coupling INVERSION (g ↔ 1/g).
- **Ghost theorem.** The Feigin–Fuchs reflection is a real involution on the Vir bar coalgebra. The shift K is the bc-ghost central charge (K=26 for the standard bosonic string). It is ADDITIVE, not multiplicative.
- **Worked instance.** `three_dimensional_quantum_gravity.tex` abstract L75; `thm:vir-koszul` L998.
- **Counter-template.** Before naming a symmetry "S-duality" / "T-duality" / "modular invariance", check the form of the action. Additive shifts are reflections; multiplicative inversions are dualities.

### AP-CY81. Module element treated as Maurer–Cartan element
- **Wrong claim template.** Stating a Cardy state (boundary state in a CFT, an element of a module M) as a Maurer–Cartan element of the underlying chiral algebra A.
- **Ghost theorem.** Cardy states satisfy `q^{L_0} |C> ∝ S |C>` (a module-level identity). MC elements satisfy the master equation in A. The two are DIFFERENT objects in DIFFERENT spaces with DIFFERENT equations.
- **Worked instance.** `three_dimensional_quantum_gravity.tex` thm:btz-mc.
- **Counter-template.** Before invoking MC equation for an element, verify it lives in the algebra not in a module. A module element can satisfy an analogous equation in End(M), not in A.

### AP-CY82. Algebraic identity as physical theorem
- **Wrong claim template.** Stating an algebraic identity (e.g. crossing time = X) as if it were the physical Page curve / RT formula / QES proposal.
- **Ghost theorem.** The algebraic identity is true and useful; the physical theorem it suggests is conjectural and requires identifying the algebraic objects with their physical referents (von Neumann entropy, area operator, ...).
- **Worked instance.** `three_dimensional_quantum_gravity.tex` thm:page-curve. `entanglement_modular_koszul.tex` already downgrades QES, Page curve, RT corrections to `\begin{conjecture}` honestly — the 3DQG paper should mirror.
- **Counter-template.** Theorems are mathematical; physical interpretations are conjectural until the identification is rigorous. Use `\begin{theorem}` for the algebraic statement and `\begin{conjecture}[Physical interpretation]` for the physics.

---

## Theme E — Within-volume contradictions

### AP-CY83. Standalone drops a caveat present in the chapter
- **Wrong claim template.** Same theorem in standalone and chapter, but the standalone omits a critical "this fails when X" warning.
- **Ghost theorem.** The chapter is correct; the standalone is a strict overclaim. The single-source-of-truth principle requires they agree.
- **Worked instances.**
  - BP self-dual point: `bp_self_duality.tex` Prop 4.7 acknowledges the pole; cross-references in `five_theorems_modular_koszul.tex` L2551–2554 and `koszulness_fourteen_characterizations.tex` L1315–1316 drop the warning.
  - L^sh Eisenstein poles: `chapters/connections/arithmetic_shadows.tex` L3458–L3495 explicitly disclaims; `standalone/arithmetic_shadows.tex` L639–L663 commits the disclaimed error.
- **Counter-template.** When migrating content to a standalone, port every warning. After any standalone edit, diff against the chapter version for caveats present-then-absent.

### AP-CY84. Occupation pattern misstated as amplitude bound (or vice versa)
- **Wrong claim template.** "ChirHoch^•(Vir_c) is concentrated in {0, 1, 2}" stated as occupation (H^i = 0 for i not in set).
- **Ghost theorem.** Distinguish AMPLITUDE bound (H^i = 0 for i > N) from OCCUPATION pattern (H^i = 0 for i not in S). For Vir_c, ChirHoch is amplitude-bounded by 2 and occupation = {0, 2} (i.e., H^1 = 0).
- **Worked instance.** `en_chiral_operadic_circle.tex` Thm 3.6 + Prop 10.4 says "{0, 1, 2}" (amplitude); `chiral_center_theorem.tex` L2025–L2041 says concentrated in {0, 2} with H^1 = 0 (occupation). The standalone confuses the two.
- **Counter-template.** State explicitly: "H^i = 0 for i > N" (amplitude bound) or "H^i = 0 for i ∉ S" (occupation pattern). Mixing them is a category error.

### AP-CY85. Within-volume Dirichlet-series / generating-function conflation
- **Wrong claim template.** Two distinct generating functions `D_2(s) = Σ a_n n^{−s}` (Fourier-coefficient series) and `L^sh(s)` (constant-term series) treated as the same object; properties of one (Eisenstein poles, Euler product, Selberg-class membership) ascribed to the other.
- **Ghost theorem.** The Fourier-coefficient series factors as `−24κ ζ(s) ζ(s−1)` for class G (Eisenstein, has poles at s=1, 2). The constant-term series `L^sh(s) = Σ S_r r^{−s}` is entire (two-term polynomial in 2^{−s} for class G; three terms class L; four terms class C; convergent in a half-plane class M). They are DIFFERENT objects.
- **Worked instance.** Cache entry 144 (wave 4): `arithmetic_shadows.tex` L639–L663 vs chapter version L3458–L3495.
- **Counter-template.** Before claiming "L-function" structural properties (Euler product, functional equation, poles, Selberg class), verify the series in question CARRIES those properties. Two series with the same coefficients can have very different analytic structure.

---

## Theme F — Inflated counts and rhetorical inflation

### AP-CY86. Inflated "N equivalent characterizations" / "M faces" count
- **Wrong claim template.** "Theorem: koszulness has 14 equivalent characterizations" / "Seven faces of r_CY(z)" — when several listed items are 1-way, conditional, or family-restricted.
- **Ghost theorem.** Compute the genuine ⇔ count. State 1-way arrows separately. Conditional / family-restricted versions get their own qualified theorem.
- **Worked instances.**
  - `koszulness_fourteen_characterizations.tex`: genuine unconditional ⇔ count is 10, not 14. Six are 1-way (v, xvi), conditional (xi simplicial dual; xv perfectness), or family-restricted (xiv affine KM only).
  - "Seven faces" of r_CY(z): 4 distinct objects in 7 presentations. F4↔F7 same data; F3↔F6 both E_∞ shadows. Cache entry 52.
  - "Three independent sources" of free-field exactness: ONE mechanism (block-diagonal propagator) projected three ways. Cache entry 52.
  - "Universal N-formula": EXACT only at N=3; LOWER BOUND at N≥4. Cache entry 52.
- **Counter-template.** Before writing "N equivalent characterizations", build the implication graph. State separately: unconditional ⇔, 1-way, conditional, family-restricted. Inflate counts only by enumerating presentations of the SAME object.

### AP-CY87. Tautological "characterizations equivalence"
- **Wrong claim template.** "Theorem G: characterization (i) ⇔ characterization (j)" — when the two are the same by definition.
- **Ghost theorem.** A tautological equivalence is a definition unfolding, not a theorem. The physical / structural identification (e.g., "Koszulness ⇔ exact bulk reconstruction") is a STRUCTURAL ANALOGY, not a theorem.
- **Worked instance.** `holographic_codes_koszul.tex` thm:hc-koszulness-exact-qec L339–421: characterization (iii) is silently DEFINED to be K4 (Koszulness), so (iii) ⇔ (i) is K4 ⇔ K4.
- **Counter-template.** Before writing a characterization-equivalence theorem, verify the characterizations are NOT definitionally equal. A definition-unfolding belongs in a remark, not a theorem.

---

## Theme G — Bar / cobar / homological discipline

### AP-CY88. Bar is multiplicative, not additive
- **Wrong claim template.** "barB is additive: barB(A ⊗ A') ≃ barB(A) ⊕ barB(A')."
- **Ghost theorem.** Bar is MULTIPLICATIVE (shuffle): `B(A ⊗ A') ≃ B(A) ⊗ B(A')` via the Eilenberg–Zilber shuffle map. ADDITIVE applies only to PRIMITIVES of the bar coalgebra (=indecomposables, the cotangent complex up to shift).
- **Worked instance.** `cobar_construction.tex` L1969.
- **Counter-template.** Bar(tensor product) → tensor product of bars (shuffle). Sum-of-bars only at the primitive / indecomposable level.

### AP-CY89. Graded-commutativity claim that trivializes the curvature being introduced
- **Wrong claim template.** "Chiral algebras are graded-commutative, so [μ_0, −]_{μ_2} = 0" — used to dismiss curvature obstructions.
- **Ghost theorem.** Graded-commutativity holds on the BD-COMMUTATIVE subclass (V2-AP5 strict subclass). Outside this subclass, [μ_0, −]_{μ_2} is the curvature obstruction being studied. Asserting it vanishes universally trivializes the very curvature being introduced.
- **Worked instances.** `bar_cobar_adjunction_curved.tex` L270; `filtered_curved.tex` L103.
- **Counter-template.** Before asserting graded-commutativity, scope to BD-commutative subclass (V2-AP5). For curved bar-cobar, the curvature obstruction is the OBJECT — do not assume it away.

### AP-CY90. Three-bar discipline named but not enforced
- **Wrong claim template.** Citing V2-AP3 (B^FG, B^Sigma, B^ord distinct) as known, then writing every theorem with `barB` (defaults to B^Sigma) without explicit tag.
- **Ghost theorem.** Each theorem requires a specific bar; defaulting to B^Sigma is an implicit choice that must be stated.
- **Worked instance.** Vol I `chapters/theory/`: 92 hits for B^ord, 5 for B^FG, 4 for B^Sigma. All load-bearing theorems use untagged `barB`.
- **Counter-template.** Every theorem statement using "the bar complex" must specify B^FG / B^Sigma / B^ord (or `barB^X` macro). Apply by macro substitution + grep.

### AP-CY91. ProvedHere theorem mixing proved with conjectural clauses
- **Wrong claim template.** A 4-clause theorem with `\ClaimStatusProvedHere`, where clauses 1–3 are proved but clause 4 ("promotion to ordinary QI") is conjectural.
- **Ghost theorem.** Each clause must be tagged independently. Bundling proved with conjectural under one ProvedHere tag is the V2-AP31 violation at write time.
- **Worked instance.** `bar_cobar_adjunction_inversion.tex` thm:bar-cobar-inversion-qi.
- **Counter-template.** Split multi-clause theorems by status: B.1, B.2, B.3 ProvedHere; B.4 Conjectured. AP-CY71 + V2-AP31 enforcement.

### AP-CY92. Adjunction stated as theorem-of-the-unit
- **Wrong claim template.** `thm:bar-cobar-adjunction = thm:geom-unit` — labels the unit-as-QI as the adjunction itself.
- **Ghost theorem.** A Quillen adjunction requires (a) the adjoint pair, (b) a Quillen condition (left adjoint preserves cofibrations + acyclic cofibrations). Exhibiting the unit-as-QI is one half of the adjoint-equivalence, not the adjunction itself.
- **Worked instance.** `bar_cobar_adjunction.tex` (per wave 5).
- **Counter-template.** State the adjoint pair explicitly. Prove cofibration and weak-equivalence preservation. Then state the Quillen equivalence (= unit-and-counit are weak equivalences).

---

## Theme H — Eval-core qualifier and AP47 hygiene

### AP-CY93. AP47 by omission: theorem statement lacks eval-gen-core qualifier
- **Wrong claim template.** Theorem statement omits "(on the evaluation-generated core)", inheriting AP47 only via citation chain to Vol I Thm B.
- **Ghost theorem.** The theorem holds on the eval-gen-core; full-category extension is conjectural. Statement without qualifier overclaims.
- **Worked instances.** `drinfeld_kohno_bridge.tex` Thms 3.1, 3.2, 4.6, 6.4. `analytic_sewing.tex` thm:mc4-strong (per wave 3).
- **Counter-template.** Every theorem invoking MC3 or its descendants (MC4, DK chain) must state "on the eval-gen-core" in its hypotheses. Add a Remark on the conjectured full-category extension.

### AP-CY94. Misnamed file: N5_mc5_sewing.tex contains no MC5 theorem
- **Wrong claim template.** File named `N5_mc5_sewing.tex` (suggesting an MC5 theorem) but is the analytic sewing standalone with no MC5 proof.
- **Ghost theorem.** Either the file should be renamed (`N5_analytic_sewing.tex`) or the missing MC5 standalone should be written.
- **Counter-template.** File names that promise a theorem must contain it. Audit by `grep "thm:mc5\|MC5" filename` after creation.

---

## Theme I — Misapplied / hand-waved classical results

### AP-CY95. Misapplied Whitehead reduction
- **Wrong claim template.** Using Whitehead reduction (a topological tool for finite-dim simple g) to compute `H^*(g[t], C)` (loop algebra cohomology).
- **Ghost theorem.** The right tool is Garland–Lepowsky (Garland 1980, Lepowsky 1980). The Vol I standalone `garland_lepowsky.tex` exists but is not cited in the misapplication site.
- **Worked instance.** `drinfeld_kohno_bridge.tex` Thm 5.4.
- **Counter-template.** For loop algebra cohomology, cite Garland–Lepowsky. For finite-dim simple g cohomology, cite Whitehead.

### AP-CY96. Chevalley-basis Casimir hand-wave
- **Wrong claim template.** "With the correct index placement the identity holds" — admitted in-source after a basis-dependent contraction gives the wrong number.
- **Ghost theorem.** The Casimir is basis-INDEPENDENT. Computing it in a fixed basis MUST give `C_2^{ad}`. Disagreement means the basis-dependent computation is wrong.
- **Worked instance.** `chiral_chern_weil.tex` L780–810: sl_2 contraction gives 5 instead of 4 = C_2^{ad}.
- **Counter-template.** Compute the contraction in a fixed Chevalley basis, identify the error, fix it. Do not admit "correct index placement" as a hand-wave.

---

## Theme J — Build / LaTeX hygiene

### AP-CY97. Malformed LaTeX masked by lenient parsing
- **Wrong claim template.** A line with stray `}` or missing opening delimiter (e.g. `divided-power convention} = \lambda^n/n!$)`) survives compilation and renders as garbage.
- **Worked instance.** `three_parameter_hbar.tex` L210.
- **Counter-template.** After every paragraph edit, build and visually inspect the rendered output (not just the log). Stray braces produce silent rendering artifacts.

### AP-CY98. Build-warning regression silently absorbed
- **Wrong claim template.** New "Undefined control sequence" warnings introduced by chapter migration are absorbed into the build log without action (V2-AP39 variant).
- **Counter-template.** After any cross-volume migration, grep build log for "Undefined control sequence" and add `\providecommand` for each. Run `make warnings` before commit.

---

## Theme K — Construction-vs-narration (extending AP-CY57)

### AP-CY99. "BBL triangle = single object viewed three ways" without functorial map
- **Wrong claim template.** "The BBL triangle is one object viewed three ways" — claimed without naming the functorial maps between presentations.
- **Ghost theorem.** Three distinct functorial outputs of the bar complex (chiral homology, K-theory class, motivic invariant) related by named natural transformations.
- **Worked instance.** `three_dimensional_quantum_gravity.tex` and 2 other locations (per wave 4).
- **Counter-template.** AP-CY57 enforcement: every "X is Y viewed differently" needs the explicit functor F: X → Y or the natural transformation η: X ⇒ Y. Name it.

### AP-CY100. Spectral coassociativity drops the Drinfeld associator Φ
- **Wrong claim template.** Spectral coassociativity stated as `(Δ ⊗ id) ∘ Δ = (id ⊗ Δ) ∘ Δ` — without the Drinfeld associator Φ.
- **Ghost theorem.** Quasi-coassociativity: `Φ_{12,3} ∘ (Δ ⊗ id) ∘ Δ = (id ⊗ Δ) ∘ Δ`. Φ is the KZ associator, satisfying the pentagon.
- **Worked instance.** `e1_primacy_ordered_bar.tex` Eq. 9.2.
- **Counter-template.** For E_1-chiral coalgebras, coassociativity is QUASI-coassociativity with Φ. Drop Φ only if A is E_inf (symmetric).

---

## Suggested AP-CY99/100 placement reconsider

AP-CY99 and AP-CY100 thematically duplicate AP-CY57 and AP-CY100 may belong in Vol I AP catalogue rather than Vol III. The user can decide placement.

---

## Cache entries to append (already in protocol; double-check coverage)

The agents have appended cache entries 51–54 and 138–144 across waves 1–4. Outstanding cache entries to add:
- BP arithmetic at fixed-point pole (AP-CY68 ghost)
- AP-CY70 false independence
- AP-CY78 operadic circle confabulation (already partial in entry 53)
- AP-CY83 standalone-drops-caveat (already partial in entries 140-144)
- AP-CY84 occupation vs amplitude (already partial in entry 54)
- AP-CY88 bar additive vs multiplicative
- AP-CY89 graded-commutativity trivializing curvature
- AP-CY94 misnamed file
- AP-CY97 malformed LaTeX

These cache appends should be done by a single follow-up pass to avoid agent races.

---

## Application instructions (when user is ready to merge)

1. Insert AP-CY68–AP-CY100 entries into Vol III CLAUDE.md at the end of the existing AP catalogue (before the Roadmap section).
2. For Vol I-specific entries (AP-CY76, AP-CY83 instances, AP-CY88 etc.) consider also adding to ~/chiral-bar-cobar/CLAUDE.md.
3. Update HZ3-12 (proposed in `notes/claudemd_improvement_suggestions_20260416.md`) to cross-link the new APs.
4. Run `make build && make test && make verify-independence` to confirm the AP additions don't break documentation builds.
5. NO AI attribution. All commits Raeez Lorgat.
