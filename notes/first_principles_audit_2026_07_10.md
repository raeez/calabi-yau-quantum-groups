# First-Principles Audit of the Mathematics and Physics — Vol III

**Date:** 2026-07-10.
**State audited:** HEAD `c44a491` ("release pdf", 2026-06-18) plus the
working tree (323 files modified vs HEAD; concurrent editing observed —
one stale citation in the audit brief had already moved). Line numbers
are as of this read.
**Method:** two independent adversarial deep reads — (i) the two-stage
CY-to-chiral functor Φ_d, the shift law, the chain-fusion conjecture,
the 6d hCS anomaly, and the κ-table; (ii) the quantum-group/BKM lane
(Y⁺(X), Drinfeld double, g_{Δ₅}, Fake Monster, κ_BKM ladder) — with
status macros distrusted and proof bodies refereed directly.
Load-bearing findings independently confirmed at the main line are
marked ✓M. Companion audits in the four sibling repos and
`~/ecosystem/swarm-reports/`.

---

## 1. Executive verdict

**Overall grade: C+. A serious, self-aware research programme wearing
a theorem's clothing.** The fine print is repeatedly honest — typed
hypothesis packages, explicit open problems, correct CoHA/W_{1+∞}
discipline, MA-8 operationalized into a checkable six-obstruction
theorem — but the headline theorem environments and CLAUDE.md assert
what the bodies retract, the 6d anomaly section imports a 4d
computation, and the numerical layer of the BKM lane cannot currently
be trusted without independent recomputation (three of five κ_BKM
ladder entries misattributed, one arithmetic error, one circular
verification engine).

## 2. Independently verified at the main line (✓M)

1. K3×E κ-row: κ_cat = χ(𝒪_{K3})·χ(𝒪_E) = 2·0 = 0 (Künneth);
   κ_BKM(Δ₅) = c(0)/2 = 5 with my own from-scratch theta computation
   of φ₀,₁ = (y⁻¹+10+y) + q(10y⁻²−64y⁻¹+108−64y+10y⁻²) + …, c(0,0) = 10;
   Ell(K3) = 2φ₀,₁ → weight 10 (χ₁₀ = Δ₅²); κ_fiber = 24 = Mukai rank.
2. dim S_k(Sp₄(ℤ)) = 0 for k ≤ 4 (first scalar cusp forms χ₁₀, χ₁₂;
   weight 5 exists only with character, as χ₅) — so "integer-weight
   Sp₄(ℤ) cusp forms of weights (5,4,3,2,1)" is impossible as stated.
3. rk(II₂₅,₁) = 26; η⁻²⁴ = q⁻¹(1 + 24q + 324q² + 3200q³ + …) — the
   fake-monster data used in the manuscript (weight 12, c(0) = 24,
   mult p₂₄(1−n)) are correct where stated.
4. The quartic-Casimir safe lists genuinely differ: d^{abc} = 0
   exactly for non-A_{n≥2}; no primitive quartic Casimir exactly for
   {A₁, A₂, G₂, F₄, E₆, E₇, E₈} (exponent lists contain no 4). They
   disagree on B_n, C_n, D_n, A₂ — so no reinterpretation rescues a
   classification based on the wrong tensor (see F-III.4).

## 3. Pillar-by-pillar findings

### 3.1 The two-stage functor Φ_d — grade **C+**

Locations: headline `chapters/theory/cy_to_chiral.tex:4–66`;
Stage-1/2 definitions :495–519, 568–582, 978–1015; morphism kernel
conditional :1097–1121; shift law :16–21, 559–566, 1132–1134, 718,
3587–3590; chain fusion :3453–3530, 3555–3562; envelope theorem
`chapters/theory/cy3_chain_level_bridge.tex:3481–3548`; hCS–Hall open
problem `cy3_chain_level_bridge.tex:1940–1989`.

- **F-III.1 (Stage-1 is a citation assembly; the glue functor is
  named, not constructed).** Φ_d^{FA} is *defined as* the conjunction
  of Kontsevich E_d-formality + Tamarkin + Costello–Gwilliam–Li
  holomorphic locality (:495–503). Arrows (a),(b) are genuine
  literature. The hard glue (c) — "Hol_{X,Ω_X}", transporting a
  factorization algebra on ℝ³ to a *holomorphic* FA on the
  6-real-dimensional X "by replacing the de Rham resolution with
  Ω^{0,•}(X)" (bridge:3536–3540) — is a redefinition, not a functor:
  no comparison map, no quasi-isomorphism; no such theorem exists in
  Costello–Li. Morphism functoriality is a Conjecture at every d
  (:3555–3562). **Internal contradiction (✓ referee-quoted twice):**
  d = 2 functoriality claimed proved at :400–402, :3595–3598, :1156,
  and simultaneously "pending a direct chain-level verification"
  inside the conjecture at :3446, :3561. The body's own fine print is
  honest ("assignment", "the map on Hom-sets must be verified",
  "no functoriality on arbitrary morphisms is asserted", :11, 3447,
  342); the theorem headlines and CLAUDE.md ("canonical functor")
  assert more. "Canonical up to a GRT₁(ℚ)-torsor" is self-cancelling
  phrasing the manuscript itself disavows at :486–489.
- **F-III.2 (shift law: one of five values derived).** Granting the
  internal convention, Dunn factorisation with ∫_{Σ_{d−1}} consuming
  E_{d−1} yields n = 1 for every d — so d = 3 → E₁ is sound (with the
  correct π₁(Conf₂(ℝ³)) = 0 braiding remark at :7380–7381), and the
  d = 2 → E₂, d = 1 → E_∞ entries are *enhancements* justified by
  arguments that fail: `prop:native-en-level`'s bracket-degree
  reasoning is d-independent (applied uniformly it would contradict
  n(3) = 1), and its Serre-duality antisymmetry clause is false at
  even d (χ(E,F) = +χ(F,E) at d = 4, conceded at :718). The
  d = 1 → E_∞ claim infers chain-level E_∞ from cohomological bracket
  vanishing (a shadow≠object move by the repo's own standards) and is
  contradicted by its own output — the rank-2 Heisenberg on H¹(E)
  with nondegenerate pairing (:3589) has singular OPE, hence is not
  commutative. d ≥ 4 is "an explicit hypothesis" (:523). CLAUDE.md's
  "shift law n = ∞,2,1,1,1" presents one derived value and four
  hypotheses as a law.
- **F-III.3 (chain fusion "verified" is a mislabel).** The body says
  it plainly (:3495–3498): three "constructed local comparison
  models" + one conditional case. The ℂ³ case dissolves: the Stage-2
  side is only the Hall-shadow normal form, with the hCS↔Hall
  identification deferred to Open Problem
  `op:cy3-hcs-hall-comparison` (bridge:1940–1989, seven unresolved
  conditions), and the boundary side End(𝟙) ≃ Y⁺(ĝl₁) is a
  type-slippage (literal End(𝒪_{ℂ³}) = ℂ[z₁,z₂,z₃]; the Y⁺ reading
  needs the critical-CoHA category, and the conjecture admits the
  canonical boundary vacuum "has no construction in the literature
  beyond these local models", :3524–3526). Local ℙ² and conifold are
  literature-correct identifications of the Hall side only. Zero
  end-to-end verifications. The label `rem:chain-fusion-verified-cases`
  and CLAUDE.md's "verified at ℂ³, local ℙ², conifold, K3×E"
  overstate the body.
- **F-III.4 (6d anomaly: type-correct functional, unsound
  derivation, unreliable classification).** Positives: the anomaly
  functional ∫_X Ω_X ∧ Tr_ad(A F_A³) is well-typed ((3,3)-form,
  ghost number +1; :2244–2269) and the "not the 3d CS cubic vertex"
  disclaimer (:2257–2259) is right. Negatives: the coefficient
  equation A_anom = d^{abc}d_{abc}/(2π)³ is diagrammatically
  malformed (a one-loop wheel produces one invariant tensor
  contracted with external legs, not a scalar times an independently
  traced functional), and the proof's group factor
  ⟨T^a{T^b,T^c}⟩ = d^{abc} (:2346–2348) is the 4d **triangle**
  tensor. For holomorphic theories on ℂ^d the one-loop anomaly is
  supported on (d+1)-vertex wheels (sanity anchor: d = 1 gives the
  2-vertex wheel = Kac–Moody level); at d = 3 this is a 4-vertex
  **box** with a symmetrized quartic adjoint trace. Since the
  d^{abc} = 0 list and the no-quartic-Casimir list provably differ
  (✓M §2.4), the "admissible gauge algebra" classification lemma
  (:2271–2307 — correct Lie theory about the wrong tensor) is
  unreliable. Note the constellation's own MA-9 slogan (quartic
  obstruction, not cubic Casimir) is violated by this derivation.
- **F-III.5 (κ-table: compact rows sound; noncompact κ_cat
  ill-defined).** K3×E row verified (✓M). Local ℙ²
  κ_ch = 3/2 = χ_top(ℙ²)/2 coherent with the stated
  compactly-supported-supertrace convention (:3209–3212). But
  κ_cat on noncompact rows is "n/a" at :3147 and "0" at :3171 under
  a header definition (ordinary χ(𝒪_X)) that is ill-defined
  (infinite-dimensional H⁰) on ℂ³/local ℙ²/conifold; the 0 is
  backfilled from the ghost-balance identity (:3193–3195) — a
  different definition than the column header. The refutation of
  κ_BKM = κ^Hodge + χ(𝒪_fib) (:220–233 of
  `cy_d_kappa_stratification.tex`) is correct discipline.

### 3.2 The quantum-group / BKM lane — grade **C+**

Locations: Hall datum + Y⁺ definition
`chapters/theory/quantum_groups_foundations.tex:21, 152`; conditional
double :202–253; CoHA(ℂ³) chain :692–772; K3×E Hall–BKM comparison
:4330–4693; g_{Δ₅} recognition `cy_to_chiral.tex:2011–2091`; K3
Yangian `examples/k3_yangian_chapter.tex`; Fake Monster
`cy_to_chiral.tex:3258–3332`.

- **Sound and best-in-constellation:** Y⁺(X) defined at
  Davison-school precision with the full datum (σ, S, o, Q, T_eq,
  oriented critical atlas); the forbidden slogan CoHA(ℂ³) = W_{1+∞}
  is *negated* repo-wide with the correct three-arrow chain
  (CoHA → Hopf double → vertex evaluation image;
  qgf:696–705, 4719); MA-8 is operationalized into a six-obstruction
  finite-height iff-theorem with ML descent (qgf:4571–4693); the
  genuinely open K3×E realization is respected ("do not by themselves
  identify the compact Hall source", cy_to_chiral:2032); the
  elliptic-partial/toroidal-absent boundary is honored. **Best proved
  theorem of the lane:** the Mukai super-Yangian ≄ BKM Hall double
  non-isomorphism (`k3_yangian_chapter.tex:2337–2381`) — separation
  by Cartan rank, root-multiplicity growth (polynomial vs
  Rademacher), and imaginary-simple-root existence; unconditionally
  correct.
- **F-III.6 (κ_BKM ladder: misattributed and mixed-convention;
  engine circular).** The inscribed "geometric CHL ladder" — weights
  (5,4,3,2,1), c_N(0) = (10,8,6,4,2) at N = (1,2,3,4,6)
  (`gluing/sec_7_lattice_automorphic.tex:390`,
  `phi_universal_trace_platonic.tex:82`, `introduction.tex:3914`,
  `compute/lib/k3_yangian_borcherds_weight_theta_refinement.py:35–140`,
  `modular_koszul_bridge.tex:835`) — carries three mutually
  incompatible in-repo descriptions, each wrong: (i) "integer-weight
  Sp₄(ℤ) Siegel cusp forms of weights (5,4,3,2,1)" is impossible
  (✓M §2.2); (ii) "exp-lifts of index-1 level-N Jacobi forms on
  paramodular Γ_N⁺" mispairs Γ_t with level-N index-1 forms and
  cites Eichler–Zagier 1985 Table 1, which cannot contain twined
  forms; (iii) attributions to Govindarajan–Krishna clash with GK's
  actual square-root weights (5, 3, 2, 3/2, 1) and Jatkar–Sen full
  weights (10, 6, 4, 3, 2). **Cross-repo adjudication (with the
  igusa-cusp-form audit):** the values (8,6,4,2) at N ≥ 2 do exist —
  they are the constants of the *Mathieu-twined* family
  (Cheng–Harrison Table 2; frame shapes 1⁸2⁸, 1⁶3⁶, 1⁴2²4⁴, 1²2²3²6²
  with a₁ = 8,6,4,2), while the N = 1 column (c = 10 → weight 5)
  is the *square-root* normalization of φ₀,₁ — a mixed-convention
  ladder that no single literature family matches. The compute
  "verification" is circular: the engine stores c_N(0), defines
  A_N := (T − c)/2, then "verifies" c = T − 2A
  (engine:155–166); no q-expansion is ever computed. The universal
  identity κ_BKM(Φ) = c(0)/2 itself is true (Borcherds Invent. Math.
  132 Thm 13.3) and correctly cited. **Repair:** recompute N ≥ 2 rows
  from actual twined q-expansions, pick one family and one
  normalization (declare the N = 1 column's convention), rebuild the
  engine to compute rather than store.
- **F-III.7 (local errors in the moonshine-adjacent claims).**
  `quantum_chiral_algebras.tex:3818, 3910`: "25/3 = rk(II₂₅,₁)/3" —
  the rank is 26 (✓M); the pentagon theorem at :3884–3911 also
  asserts "the three coboundaries are linearly independent in H³" (a
  category error — coboundaries vanish in cohomology) and uses the
  modular function Φ₁₀^{un}/η²⁴ as a scalar coefficient in a
  constant-coefficient CE complex. `hochschild_calculus.tex:3802`
  calls g_{Δ₅} "the Fake Monster Lie superalgebra", contradicting
  `cy_to_chiral.tex:3332` (rank 3 vs rank 26, distinct — the latter
  is right; also the fake monster is bosonic, as
  `introduction.tex:1189` correctly says against
  `cy_to_chiral.tex:3261`). qgf:5872 claims BKM algebras are
  "finitely presented" — false (infinitely many imaginary simple
  roots). `introduction.tex:1164–1174` asserts monstrous moonshine
  as an equality V^♮ = Sp^{ch}(Φ₃^{FA}(X_B)) with a 24-real-torus in
  a complex-surface slot — contradicted in-repo by
  `cy_holographic_datum_master.tex:1947–1953` ("none is used here").
- **F-III.8 (citation rot).** Gritsenko–Nikulin's one theorem is
  cited as AJM 120 (1998), Duke 119 (1997), Duke 94 (1998), and
  "alg-geom/9504006 = Part II" across four files; "Kapranov–Vasserot
  CoHA" for ℂ³ (KV is a surface construction); SV Publ. IHÉS 118
  used as the direct source for CoHA(ℂ³) = Y⁺ without the
  dimensional-reduction step (covered correctly elsewhere by RSYZ);
  φ₀,₁ repeatedly glossed as "the K3 elliptic genus" (it is half of
  it — ✓M, my theta computation).

## 4. Systemic diagnosis

Vol III's fine print is the most honest in the constellation about
what is conjectural — and its headlines are the least faithful to
that fine print. The recurring move is **assembly-by-citation
presented as construction** (Stage-1; the ladder attributions; the
"verified" fusion cases), compounded by a numerical layer whose
verification engine stores instead of computes. The lane-specific
repairs are finite and identified; the programme itself (per-d
correspondence, Hall-side identifications, recognition criteria,
negative theorems) is genuine mathematics.

## 5. Triage (ordered)

1. Rename and re-scope the fusion cases: "Model cases" everywhere
   (the body's own phrase); fix CLAUDE.md "verified at ℂ³, …".
2. Redo the 6d anomaly coefficient with the 4-vertex wheel and the
   quartic adjoint trace; re-derive the admissible-algebra list from
   the quartic Casimir; reconcile with MA-9.
3. Rebuild the κ_BKM ladder (F-III.6): one family, one convention,
   computed q-expansions; fix the Sp₄(ℤ)/EZ/GK attributions.
4. Resolve the d = 2 functoriality contradiction (:400 vs :3446);
   restate the shift law as {derived: d = 3} ∪ {hypotheses: d = 1, 2,
   4, 5}; repair or delete the d = 1 E_∞/Heisenberg inconsistency.
5. Fix local errors: rk(II₂₅,₁) = 26; pentagon coboundary category
   error; g_{Δ₅}/Fake-Monster naming collision; "finitely presented";
   V^♮ overclaim; κ_cat noncompact column (define it as the
   ghost-balance value or mark n/a consistently); GN citation
   unification.

**Provenance.** ✓M = verified by my own computation or reading at the
main line (theta/Jacobi expansions from scratch; Sp₄ dimensions;
lattice ranks; Casimir exponent lists; K3×E row). Remaining findings
are referee reports with decisive quotes; where two referees
overlapped (κ_BKM ladder), their tension is adjudicated in F-III.6.

---

# Part II — Mathematical yield (fresh-eyes pass, same date)

Stricter second pass: referee forbidden from reading CLAUDE.md,
FRONTIER.md, notes/, status appendices, or Part I; graded only
**true + proved + new**; hypothesis-contains-conclusion = zero.

**Yield grade: D.** True+proved+new mathematics found at the stated
bar: none. One proved-labelled computation is outright false.

1. **FALSE, numerically refuted: the elliptic "Fay identity" and
   d² = 0** (`examples/toroidal_elliptic.tex:556–641`). `thm:fay`
   asserts the *bilinear* three-term identity
   θ(u₁−u₂)θ(u₃−u₄) − θ(u₁−u₃)θ(u₂−u₄) + θ(u₁−u₄)θ(u₂−u₃) = 0;
   `prop:fay-implies-d-squared` derives an "elliptic Arnold relation"
   and d² = 0 for the elliptic bar differential from it. Both false.
   Referee computation at 30 digits: relative residual 2.17 at
   generic points; the sine degeneration passes exactly (the claimed
   identity is the Ptolemy identity — true only in the trigonometric
   limit; the genuine genus-1 Fay trisecant needs four-fold theta
   products). Independently reproduced at the main line (✓M): my own
   mpmath run gives bilinear residual 1.7×10⁻³ (relative) with sine
   limit exactly 0. The wedge-sum S = Σ_cyc ζ(a)ζ(b) (a+b+c = 0) is
   nonzero and point-dependent, so the elliptic Arnold relation
   fails; the classical identity is (ζ(a)+ζ(b)+ζ(c))² = ℘(a)+℘(b)+℘(c)
   — the square of the sum, which is exactly why the KZB/dynamical
   (Felder) correction is *necessary*, as the same file correctly
   explains at :486–493. Load-bearing: cited at :329, :444, :539 and
   by `thm:elliptic-vs-rational` (:674–844), whose "elliptic bar
   complex" is therefore not known to be a complex.
2. **The non-isomorphism theorem (Part I's "best proved theorem")
   is unproved as written.** `k3_yangian_chapter.tex:2337–2381`:
   line 2367–2369 takes the classical limit of the Yangian
   Y_ħ(so(4,20)) to be the *finite* orthogonal Lie algebra — false;
   the ħ→0 limit of a Yangian is U(g[t]), whose PBW growth is
   partition-type e^{c√n}, not polynomial, killing the growth
   separation as written; and the hypothesis gives only *containment*
   of g_{Δ₅} in the double's semiclassical limit, while the proof
   compares invariants as if the Lie bialgebras were equal. Fixable
   (g_{Δ₅} contains free Lie subalgebras by Borcherds–Jurisich;
   so₂₄(A) is Lie-PI by Amitsur–Levitzki; hence no embedding), but
   that argument is not in the text — and the corrected statement is
   NEW-BUT-TRIVIAL (no one has proposed the isomorphism).
   **This overturns Part I's assessment of the theorem.**
3. **The six-obstruction iff-theorem is a definition-chase.**
   Necessity is invariance-under-isomorphism; sufficiency is four
   lines of assertion; the obstructions are defined as the failures
   of the required maps, and the quantified objects don't exist (the
   same volume: the compact K3×E construction "has not been carried
   out", `k3_yangian_chapter.tex:2437–2438`). Symptom: "the
   following five maps" followed by six items (qgf:4585).
4. **The d = 3 E₁ argument**: the individually complete steps
   (π₁(Conf₂(ℝ³)) = 0; CY₃ Serre antisymmetry; g(z)g(−z) = 1) are
   textbook; the theorem's H4 assumes the chain-level framing
   trivialization, Costello correction, and Hochschild comparison —
   the hard content. KS-folklore, zero yield.
5. Verified-correct but classical or trivial: the Kummer structure
   function coefficients (Newton-identity arithmetic; the chapter's
   own remark concedes classicality); `thm:plat-Miki-S3` proves only
   ε-relabelling symmetry of the shuffle kernel (mislabelled as
   Miki's theorem — Miki 2007 is the nontrivial horizontal/vertical
   exchange); fake-monster chapter is Borcherds-1990 imports.

**Consequences for Part I:** F-III.6 (κ_BKM ladder) and the local
errors stand. Part I §3.2's "best proved theorem" is overturned
(item 2). New top-priority triage: excise or repair
`thm:fay`/`prop:fay-implies-d-squared` and everything downstream in
the elliptic bar section (`thm:elliptic-vs-rational`); repair the
Yangian classical limit (U(g[t])) and supply the free-Lie/Lie-PI
embedding obstruction; downgrade `thm:plat-Miki-S3`'s name.

---

# Part III — Healing ledger (2026-07-10, same date)

All six ledger items executed. Every inscribed identity was verified
numerically at 25–30 digits before inscription
(scratchpad `fay_heal_check.py`, `fay_heal_check2.py`,
`dybe_fv_check.py`, `dybe_entry_check.py`); the rebuilt compute engine
passes 51 tests. Concurrent-session drift was merged semantically
(several audit line numbers had moved; two sites were found already
part-healed and were completed, not clobbered).

## 1. Elliptic Fay section (excision of a proved-labelled falsehood; new true theorems)

- `chapters/examples/toroidal_elliptic.tex:556–641` (old numbering) —
  **excision + new true theorem.** The false bilinear `thm:fay`
  replaced by the true genus-1 Fay trisecant identity (same label),
  stated in kernel form (Kronecker–Eisenstein
  F(z₁,λ₁)F(z₂,λ₂) = F(z₁,λ₁+λ₂)F(z₂−z₁,λ₂) + F(z₂,λ₁+λ₂)F(z₁−z₂,λ₁))
  and quartic theta/sigma form, with full proof (degree-0 line-bundle
  argument; denominator-clearing + affine substitution; sigma-form
  exponential cancellation). New `lem:no-bilinear-fay`: the bilinear
  three-term expression vanishes identically for NO τ (Vandermonde in
  B-cycle multipliers); Ptolemy survives only trigonometrically.
- **New true theorems replacing `prop:fay-implies-d-squared`
  (label retired):** `prop:zeta-square` ((Σζ)² = Σ℘ at a+b+c=0, proof
  from the two addition theorems); `thm:elliptic-arnold-fails` (wedge
  sum = S_τ·da∧db; exact defect 2S_τ = Σ(℘ − ζ_τ²); S_τ nonconstant
  for every τ via the B-cycle monodromy ζ_τ(z+τ) = ζ_τ(z) − 2πi;
  collision limit 6η₁ = π²E₂(τ); trigonometric defect ≡ π²; rational
  0); `cor:elliptic-bar-dynamical` (naive d² ≠ 0; central absorption
  for Heisenberg targets = the file's own curvature m₀ ∝ E₂;
  dynamical correction forced for general targets).
- **DYBE block corrected (numerically false displays excised).** The
  file's R-matrix entries and eq:dybe-11/eq:dybe-12-reduced failed
  at 30 digits. `def:elliptic-r` replaced by the verified
  Felder–Varchenko matrix (α = θ(u)θ(λ+γ)/(θ(u−γ)θ(λ)),
  β = −θ(u+λ)θ(γ)/(θ(u−γ)θ(λ)), unit corners; β is a multiple of the
  Kronecker kernel); `def:dybe` re-stated in the FV form with γ-scaled
  shifts (verified as an 8×8 matrix identity at 26 digits);
  `comp:dybe-matrix-entries` rebuilt with the verified off-diagonal
  entry and its reduction to the cleared-kernel Fay identity at
  (z₁,z₂,λ₁,λ₂) = (u+v, v, −γ, γ−λ); `prop:dybe-reduces-to-fay`
  re-proved on that basis (Felder cited for the remaining entries);
  RLL shifts in `def:elliptic-quantum` γ-scaled.
- **Split per operating rules:** old `prop:dybe-bar-nilpotency`
  (proof used the false elliptic Arnold relation) split into the
  proved parts (DYBE holds; naive d² ≠ 0; monodromy match) recorded in
  `rem:dynamical-bar-status`, plus the named
  `conj:dynamical-bar-nilpotency` (construction of the λ-extended
  dynamical bar complex; d_λ² = 0 ⟺ DYBE).
- **Downstream (re-scope):** `thm:elliptic-vs-rational` now carries
  the explicit nilpotency hypothesis (H_nil) with the named supply
  routes (curved twist / dynamical extension) and a scope-remark
  clause; intro narrative, `rem:arnold-fay-generalization`,
  `constr:elliptic-shadow-data`(i–iii), `rem:toroidal-koszul-evidence`
  :329, `rem:toroidal-three-theorems` :444, `rem:elliptic-qg-bar`(iii)
  :539, shuffle ξ–kernel anchor and shuffle-associativity remark,
  comparison table rows (Arnold/d²/R-matrix; trig column made honest:
  Arnold holds in w-coordinates, π² defect for πcot), bridge/summary
  passages all rewritten to the failure + dynamical-correction truth.
  External: `cy_holographic_datum_master.tex:1830` (Face 6) retargeted
  from the dead label to `prop:dybe-reduces-to-fay` + conjecture;
  `k3_quantum_toroidal_chapter.tex:83` rewritten. Bibliography:
  added Felder94, FelderVarchenko96, WW27, BrownLevin11.

## 2. Yangian ≄ BKM non-isomorphism (corrected proof; now genuinely proved)

- `chapters/examples/k3_yangian_chapter.tex:2337–2381` —
  **corrected proof.** Statement re-scoped to "contains g_{Δ₅} as a
  Lie sub-superalgebra"; classical limit corrected to U(so(4,20)[u])
  (cross-ref to the file's own `thm:r10-classical-limit-ch`; partition
  growth e^{c√n} noted, killing the old polynomial-growth line);
  Arrow 2 transports the containment to an embedding
  ι: g_{Δ₅} ↪ so₂₄(ℂ[u]); Arrow 3 produces a free Lie algebra on two
  even generators from two generators in the D = 4 imaginary-simple
  sector (sdim E_α = c(4) = 108 > 0, per-repo
  `cor:g-delta5-fk-closure`; Jurisich structure theorem + retraction
  onto a free generating subset); Arrow 4 the degree-count
  contradiction (n-fold brackets of matrix polynomials span ≤
  576(nd₀+1) dimensions — linear — against Witt-exponential growth),
  with the Amitsur–Levitzki/Lie-PI formulation cited as the classical
  companion. Old rank/multiplicity comparisons moved to
  `rem:k3yang-nonisom-corroboration`, correctly scoped as
  corroboration that cannot alone rule out an embedding. Chapter
  intro parenthetical (:21) fixed. Bibliography: added
  AmitsurLevitzki50, Bahturin87, Jurisich96, Jurisich98.

## 3. 6d hCS anomaly (wrong tensor → box wheel + quartic Casimir)

- `chapters/theory/cy_to_chiral.tex:2244–2373` (old numbering) —
  **corrected derivation.** eq:6d-hcs-anomaly-decomposition rewritten:
  anomalous wheel = (d+1)-vertex wheel (d = 1 anchor: 2-vertex wheel =
  Kac–Moody level; d = 3: 4-vertex box); malformed scalar
  d^{abc}d_{abc}/(2π)³ excised; new `eq:quartic-box-tensor`
  q^{abcd} = tr_adj(T^{(a}T^bT^cT^{d)}) identified as the tensor
  content of Θ_anom (Bose symmetry + cyclicity); scalar box
  normalisation explicitly Conditional with the wheel-integral
  obligation named.
- **New true classification.** `lem:quartic-casimir-classification`
  (no primitive quartic Casimir ⟺ 3 not an exponent ⟺
  {A₁, A₂, G₂, F₄, E₆, E₇, E₈}; exponent-table proof); the correct
  cubic lemma retained for its genuine 5d (holomorphic dimension 2)
  role, with the two-list disagreement stated. New
  `def:6d-admissible-gauge-algebra`: (i) primitive-part vanishing
  (list, or the so(8) degeneration tr_adj X⁴ = (n−8)tr_V X⁴ +
  3(tr_V X²)² at n = 8), (ii) Green–Schwarz cancellation of the
  (C₂)²-part (Costello–Li 2019 anchor; bib entry added).
  `thm:6d-hcs-qme-one-loop-k3xe` hypotheses + proof rewritten
  accordingly (box bullet replaces the triangle bullet).
- **Downstream:** admissibility refs at the local pre-FA definition
  and Weiss-descent theorem repointed to the new definition; the (L2)
  survey item rewritten (quartic condition); 5d-vs-6d passages at
  :1977/:1981 corrected (cubic tensor = 3-wheel of the 5d theory; 6d
  condition quartic); `quantum_chiral_algebras.tex:732–758`
  (g_{Δ₅}^re anomaly split) rewritten to the box/quartic form with
  per-block A₁ primitive-vanishing + χ_top = 0 integrated
  cancellation, cross-block couplings delegated to the existing open
  problem; drafting-history phrasing at the (already-quartic) later
  theorem replaced by direct mathematics.

## 4. κ_BKM ladder rebuild (one family per ladder; impossible claims deleted)

- **Two honest ladders inscribed everywhere the mixed
  (5,4,3,2,1)/(10,8,6,4,2) chimera stood:** the Govindarajan–Krishna
  square-root ladder, weights (5, 3, 2, 3/2, 1) (square roots of the
  Jatkar–Sen dyon forms (10, 6, 4, 3, 2); N = 1 member Δ₅ from the
  half-genus, c₁(0) = 10), and the Mathieu-twined ladder, weights
  (10, 4, 3, 2, 1) with c_N(0) = (20, 8, 6, 4, 2) (frame shapes 1²⁴,
  1⁸2⁸, 1⁶3⁶, 1⁴2²4⁴, 1²2²3²6²; N = 1 member χ₁₀ = Δ₅², not Δ₅).
  Sites: `introduction.tex` (4 sites incl. :237, :904, :1916, :3905);
  `phi_universal_trace_platonic.tex:70, 82`;
  `gluing/sec_7_lattice_automorphic.tex:219–224, 390` (the
  impossible "integer-weight Sp₄(ℤ) cusp forms of weights (5,4,3,2,1)"
  deleted with the dim S_k(Sp₄(ℤ)) = 0 (k ≤ 4) fact inscribed; Γ_t ↔
  index-t pairing stated; GN citation corrected);
  `modular_koszul_bridge.tex:831–840` (GK misattribution of twined
  values removed); `cy_c_beyond_k3e_existence_obstruction.tex`
  (9 sites: eq:…-phi-N-weight, the N=1 doubling sentence, DT/BOP
  passage, Nikulin remark incl. the engineered "T − 2A" table
  deleted, N ∈ {5,7,8} values corrected to (2, 3/2, 1), CRC passages);
  `cy_holographic_datum_master.tex:125–151` (the third variant
  (5,2,1,1,1)/(10,4,2,2,2) excised); `k3_chiral_algebra.tex`
  (adversarial additivity table rebuilt with both honest columns and
  the two GK accidents 5 = 3+2, 3 = 2+1 marked as accidents;
  `prop:bkm-weight-universal` statement + proof rewritten,
  N = 5..8 chimera rows dropped);
  `cy_d_kappa_stratification.tex` (12 sites:
  `thm:borcherds-weight-kappa-BKM-universal` statement + proof,
  `cor:borcherds-weight-full-8form-scope` (twined 8-order values
  (10,4,3,2,2,1,3/2,1); 7A corrected to a₁ = 3, weight 3/2),
  Scope (A) opener, `lem:c-N-zero-closed-form` retitled and
  re-valued, three-paths remark, GC-vs-CHL comparisons, T−2A recipe
  replaced by the ones-exponent statement).
- **Compute engine rebuilt** (was circular: stored c, defined
  A := (T−c)/2, verified c = T−2A).
  `compute/lib/k3_yangian_borcherds_weight_theta_refinement.py`: now
  hard-codes ONLY the frame shapes, the K3 Hodge diamond, the two GK
  composite weights, and Igusa's dim S_k(Sp₄(ℤ)) facts; computes a₁,
  frame dimensions, power-map closure ((4B)² = 2A, (6A)² = 3A,
  (6A)³ = 2A, (8A)² = 4B, (8A)⁴ = 2A), c₁(0) = 20 from χ_{−y}(K3)
  (hence 10 for the half-genus/Δ₅), the twining-genus q⁰ rows
  (2y⁻¹ + (a₁−4) + 2y, with the a₁-vs-(a₁−4) distinction documented),
  prime Jatkar–Sen weights 24/(N+1) − 2 cross-checked against
  a₁ − 2, GK = JS/2, and both ladders; enforces the negative results
  (mixed tuple matches no family; no Sp₄(ℤ) cusp forms of weight
  ≤ 4). `compute/tests/test_k3_yangian_borcherds_weight_theta_refinement.py`
  rewritten to match; 51 tests pass.

## 5. Local errors

- (a) `quantum_chiral_algebras.tex` pentagon cluster: 25/3 → 26/3 =
  rk(II₂₅,₁)/3 at three sites (rank 26); "three coboundaries linearly
  independent in H³" category error restated at the cochain level
  (independent in B³ ⊂ C³; coboundaries vanish in cohomology);
  Φ₁₀^un/η²⁴ re-typed as a modular function on the period domain —
  CE with 𝒪(𝔻)-coefficients, scalar = chamber evaluation.
- (b) `hochschild_calculus.tex:3551, 3585` — g_{Δ₅} de-conflated from
  the Fake Monster (rank 3 GN BKM superalgebra vs rank-26 purely
  bosonic Fake Monster); `cy_to_chiral.tex:3384` "superalgebra" for
  the fake monster → "purely bosonic … Lie algebra".
- (c) `quantum_groups_foundations.tex:5881–5886` — "all are finitely
  presented" excised: BKM algebras with imaginary simple roots have
  infinitely many generators (Rademacher-growing multiplicities); the
  obstruction re-stated as 1-truncatedness.
- (d) `introduction.tex:1163–1174` — the monstrous-moonshine equality
  V^♮ = Sp^{ch}(Φ₃^FA(X_B)) with the 24-real-torus in the
  complex-surface slot downgraded to the honest conjecture consistent
  with `cy_holographic_datum_master.tex` (no CY₃ realisation used;
  what stands unconditionally listed).
- (e) `cy_d_kappa_stratification.tex:3168–3195` — noncompact κ_cat
  column renamed κ_cat^gb and DEFINED as the ghost-balance value
  κ_ch + κ_chBV (ordinary χ(𝒪_X) ill-defined, matching the compact
  table's n/a); the ghost-balance identity marked definitional on
  that table.
- (f) GN citation unified to Amer. J. Math. 119 (1997) 181–224 /
  Internat. J. Math. 9 (1998) 201–275 at: hochschild (2 sites, incl.
  the "AJM 120" rot), k3_chiral_algebra (16 "Duke Math. J. 94"
  instances batch-fixed), sec_7 (2 sites), beyond_k3e (Duke 119 →
  AJM 119), plus every site touched in item 4.
- (g) `k3_quantum_toroidal_chapter.tex:209–240` —
  `thm:plat-Miki-S3` renamed to "ε-relabelling S₃-equivariance…" (it
  proves relabelling symmetry of the shuffle kernel); new
  `rem:plat-miki-vs-relabelling` distinguishing Miki 2007's
  horizontal–vertical exchange (not a relabelling of manifest
  parameters) from the rational parameter-action shadow.

## 6. Headline honesty

- (a) d = 2 functoriality contradiction resolved by DOWNGRADE (the
  decision rule was applied: `thm:phi-k3-explicit` was read and is an
  object-level evaluation — no morphism-level Mukai proof exists).
  Three "proved functorial" sites re-scoped to "proved object-level
  construction" with the Mukai model explicitly pending chain-level
  verification inside `conj:phi-d-functoriality`
  (`cy_to_chiral.tex` :400-region, thm:cy-a-d2 preamble,
  kernel-transform theorem :1163-region).
- (b) "verified at ℂ³, local ℙ², conifold, K3×E" phrasing renamed to
  model-case language at: Vol III `CLAUDE.md` (chain-fusion bullet,
  now naming the hCS↔Hall open problem and "no end-to-end
  verification exists"); `k3_chiral_algebra.tex:18–23`;
  `k3_chiral_bialgebra_platonic.tex:33–36`.
  (`rem:chain-fusion-verified-cases` body and
  `the_bulk_three_faces.tex` model-cases proposition were found
  already healed by a concurrent session; titles/labels left stable.)
- (c) Shift law restated at every headline: n(3) = 1 derived (Dunn +
  π₁(Conf₂(ℝ³)) = 0); n(2) = 2 and n(1) = ∞ conditional enhancements
  with the gaps named. `prop:native-en-level` rewritten (three-part
  scope: chain-level S²-action; the d = 1 E∞ claim blocked by the
  rank-2 Heisenberg output's singular OPE — the target is NOT
  commutative, E₁ with central extension, commutativity only on the
  uncharged associated-graded; the bracket-degree argument and the
  even-d Serre clause (χ(E,F) = +χ(F,E) at d = 4) disqualified as
  mechanisms). `cor:phi-d1-evaluation` and (U3) fixed; headline
  theorem display annotated; Vol III `CLAUDE.md` shift-law line
  rewritten.

## Not completed (explicit reasons)

1. **Sibling compute engines still carry the mixed ladder:**
   `compute/lib/diagonal_siegel_cy_orbifolds.py` (N = 1 row (10, 5)
   square-root-labeled inside an otherwise twined table; N = 7 row
   carries the JS value where the twined value is (3, 3/2) — its
   int-typed weight field cannot hold 3/2 without a type change),
   `compute/lib/cy3_platonic_bridge.py`, `compute/lib/bps_entropy_shadow.py`,
   `compute/tests/test_diagonal_siegel_cy_orbifolds.py`,
   `compute/tests/test_cy_d_kappa_stratification.py`. Reason: the
   ledger mandated the theta-refinement engine + its test; the
   siblings need a coordinated NamedTuple/type change and test sweep
   — a contained follow-up, now unambiguous against the rebuilt
   canonical engine.
2. **Bare mixed-tuple echoes in files outside the ledger's named
   sites:** `chapters/frame/preface.tex`,
   `chapters/scalar/borcherds_terminus.tex`,
   `chapters/examples/k3e_bkm_chapter.tex`, `toric_cy3_coha.tex`,
   `k3e_cy3_programme.tex`, `cy_c_six_routes_convergence.tex`,
   `fake_monster_chapter.tex`, `gluing/sec_3_mckay_orbifold.tex`,
   `k3_yangian_chapter.tex` (ladder mentions outside the repaired
   theorem), `main.tex`, `standalone/*_vol3.tex`,
   `appendices/first_principles_cache.md`, `working_notes.tex`.
   Reason: session scope; the canonical statements these echo are now
   healed, so the remaining propagation is mechanical relabelling to
   one of the two declared ladders.
3. **`rem:bkm-weight-universal-proof-source` and the three-paths
   remarks** in `k3_chiral_algebra.tex`/`cy_d_kappa_stratification.tex`
   still describe "independent path" architectures whose Path-C
   fixed-point route now needs the N = 1 caveat added in item 4;
   values were corrected, the prose architecture of the paths was not
   re-audited.
4. **`def:theta` in `toroidal_elliptic.tex`** retains the
   multiplicative (non-odd) triple-product normalisation while the
   healed section works with the odd θ₁ (declared at each use). A
   one-line convention remark tying the two would remove residual
   friction; not done (outside ledger scope).
5. **The `.swarm_outputs/`, `notes/`, `FRONTIER.md` working notebooks**
   were not swept for the retired claims (primary-wins-on-conflict
   discipline applies).
