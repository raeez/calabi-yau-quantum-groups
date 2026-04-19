# Agent 06 — Beilinson Audit: Non-Abelian K3 Yangian

Author: Raeez Lorgat.
Date: 2026-04-19.
Mode: Beilinson-voice adversarial audit of Vol III's "non-abelian K3 Yangian."
Posture: read-only; no .tex edits, no commits. Sole output is this memorandum.

Epistemic frame (Beilinson). What limits forward progress is not the lack
of genius but the inability to dismiss false ideas. The non-abelian K3
Yangian is the crown-jewel claim of Vol III; per the preface
(`chapters/frame/preface.tex:593-598`) the "naive six-way isomorphism of
the original CY-C" is already declared FALSIFIED at generator level, with
a "pentagon" surviving among five routes and the Borcherds branch R_2
demoted to a source, not a node. The task of this audit is to ask, for
every surviving claim the chapter makes: (i) what is being asserted, (ii)
what is being proved, (iii) what is being assumed, (iv) whether the
proved content supports the asserted content, and (v) whether the
asserted content is a genuine advance or a renaming.

Target files audited:
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex` (7078 lines)
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex` (2081 lines)
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex` (405 lines)
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_k3_nonabelian_all_ade.py` (1196 lines)
- `/Users/raeez/calabi-yau-quantum-groups/notes/wave_V110_attack_heal_Y_sln_Pentagon.md` (404 lines)

---

## (ii) The one-sentence strongest-honest-form

> **The "non-abelian K3 Yangian" is, at present, the rank-24
> indefinite-signature Heisenberg Yangian (Drinfeld 1985 / Chari–Pressley
> 1995, at signature (4,20) with the CY_2 constraint Σ h_i = 0),
> extended at ADE enhancement points by a standard level-one
> shifted affine Yangian Y^μ(ĝ_{ADE})_{k=1} (Theorem 108,
> `k3_yangian_chapter.tex:108-132`, the _only_ Proved-Here-or-Elsewhere
> non-abelian statement in the chapter). Every wider non-abelian claim
> — an osp(4|20) super-Yangian, a global non-abelian Mukai Yangian on
> generic K3 moduli, a Y(g_{Δ_5}) carrying all BKM imaginary-root
> generators, a Y(g_{K3}) satisfying Conjecture CY-C in its
> six-route form — is a labelled conjecture, not a theorem, and the
> programme's unique first-principles contribution beyond the
> classical Drinfeld / Chari–Pressley / BFN / Maulik–Okounkov /
> Etingof–Kazhdan / Tarasov–Varchenko layers is the V_4-Künneth
> character bookkeeping (Sec. 3179–5388) and a Pentagon-at-E_1
> cocycle class in (Z/2)^2 (Theorem 5502) — both of which are
> down-stream reorganisations of existing material, not a
> construction of the algebra Y(g_{K3}) as a new mathematical
> object.**

This is Beilinson's smaller true theorem. Everything larger that the
chapter advertises is either proved only for what was already proved
elsewhere, or conjectural.

---

## (i) Survive / Falsify / Qualify Punchlist

Punchlist ordered by file:line. I mark each claim with:
- **S** = survives adversarial attack in the strongest honest form below
- **Q** = survives with a qualifier that is missing or understated
- **F** = falsified or overstated; a narrower form is what actually holds
- **R** = renaming / reformulation — no new mathematical content

### A. Abelian (gl_1) layer

**A1.** `k3_yangian_chapter.tex:877-1001` —
**Theorem (Abelian K3 Yangian presentation).** `ClaimStatusProvedHere`.
Statement: rank-24 Heisenberg Yangian with structure function
g_{K3}(u) = ∏(u - h_i)/(u + h_i), unitarity, Koszul dual, bar Euler
η^{24}/q.
- **R**: at `rem:k3-abelian-yangian-classical` (1067) the author
  himself admits, "The programme's contribution is _not_ the
  presentation but its realisation as the Drinfeld double of the
  E_1-chiral Mukai Heisenberg algebra." Every structural piece is
  attributed to Drinfeld 1985, Chari–Pressley 1995, FRT 1989, or
  Frenkel–Jing 1988.
- **Beilinson verdict**: survives _as_ a specialisation; the new
  content is bookkeeping (the "CY_2 constraint" = trace condition
  on a rank-24 lattice).
- **Strongest honest form**: "At signature (4,20), rank 24, with
  Σh_i = 0 and unitarity g(u)g(-u)=1, the Heisenberg Yangian of
  Chari–Pressley (1995) admits the stated FRT/Miura presentation."

**A2.** `k3_yangian_chapter.tex:859-875` (rem:k3-yangian-lattice-scope).
- **S**: _correctly_ scoped. The author acknowledges that the
  "K3" label is cosmetic — the same algebra arises from Leech,
  Niemeier, E_8(-1)^3 — "the mathematical object is the rank-24
  indefinite-signature Heisenberg Yangian with integral Mukai
  pairing." This is the one place the chapter does not
  overclaim.

**A3.** `k3_yangian_chapter.tex:713-846` — Proposition
`prop:mukai-indefinite-yangian`. ClaimStatusProvedHere.
- **S** with **Q**: the indefinite-signature statement survives as
  a property of _abelian_ gl_1 Yangians (direct product of 24
  rank-1 Yangians with prescribed signs). The proof (i)–(vii)
  uses only that the cross-sector commutator vanishes, which is
  immediate for gl_1.
- **Missing qualifier**: the theorem advertises "indefinite
  signature poses no obstruction" without scoping to gl_1. A line
  after (vii) needs "for non-abelian g, indefiniteness is
  obstructed exactly by the omega-twisted permutation
  P_ω^2 = ω ⊗ ω with 160/576 eigenvalues -1; see Remark
  1441/A1 below." The author's own Remark 1441-A1 admits the
  obstruction is non-trivial precisely in the non-abelian regime
  — the proposition title should be narrowed.

### B. BFN / ADE layer

**B1.** `k3_yangian_chapter.tex:108-132` — **Theorem
`thm:bfn-phi-ade-identification`.** ClaimStatusProvedElsewhere.
Statement: Φ(T*S̃_g) ≃ A_ℏ(Q_g, v, w) ≃ Y^μ(ĝ)_{k=1}.
- **S**: this is the _only_ non-abelian Yangian statement in the
  chapter carrying ProvedElsewhere. The three steps (McKay +
  Kronheimer, BKR + Kapranov–Vasserot, BFN 2016 + Nakajima–
  Takayama) are each published theorems. Step 4
  (Φ-compatibility) uses CY-A_2, which is claimed proved at d=2.
- **Q**: Remark `rem:bfn-ade-input-dependency` (136-158) correctly
  points out that V1 and V3 both depend on Kronheimer; only V2
  is truly input-disjoint. The "three independent paths" should
  be read as "two input-disjoint paths (V2 vs. V1+V3)."
  _Commendable_: the self-correcting remark already exists.
- **Scope reminder**: this theorem is about _ADE surface
  singularities on K3_, not about K3 itself as a global space.
  At generic K3 moduli the BFN route fails because K3 is not a
  Nakajima quiver variety (cf. `rem:k3e-two-routes-yangian`,
  line 91-101, and Conj. `conj:bfn-k3-yangian-kummer` 81-89).

**B2.** `k3_yangian_chapter.tex:81-89` — **Conjecture
`conj:bfn-k3-yangian-kummer`.** Kummer-orbifold identification
A_C(Kummer, n) = Y(g_{K3})|_charge n.
- **S**: correctly labelled Conjecture. `rem:bfn-kummer-reduces-to-a1`
  (178) reduces it to the A_1 instance of B1 _plus_ deformation
  invariance under blowup of 16 orbifold singularities — an
  extra, unverified deformation-invariance statement. The
  conjecture is honest about what remains open.

### C. Six-route / CY-C layer

**C1.** `k3_yangian_chapter.tex:353-364` — Three-route identification
`D(Y^+(g_{K3}))` via Chiral, BFN, MO routes (mirrored in
`quantum_groups_foundations.tex:355-364`).
- **F → S** after restriction: the Chiral route depends on CY-A_2
  (OK at d=2) but then requires a _Yangian quantisation step_
  which the author himself admits is "open" (`rem:k3-yangian-obstruction`
  line 639-652). The BFN route is conjectural for generic K3
  (Conj. `conj:bfn-k3-yangian-kummer`). The MO route is
  scope-restricted to the ADE/Kummer locus via Lemmas
  `lem:mo-bypass-local-to-global` and `lem:no-Gm-on-E` — K3 has
  no global torus action, so the MO stable envelope cannot be
  constructed on all of K3 moduli.
- **Beilinson verdict**: the chapter correctly, if verbosely,
  admits the three routes are three conjectures with different
  scope-gaps. But the language "three independent constructions
  [that] approach the same algebra" in `quantum_groups_foundations.tex:337`
  overstates the convergence — none of the three actually
  constructs the non-abelian Y(g_{K3}); they conjecture
  targets that should agree.
- **Strongest honest form**: "Three conjectural constructions of
  a Hopf object D(Y^+(g_{K3})): (A) CY-A_2 + Yangian
  quantisation (open); (B) BFN at Kummer (reduces to ADE+blowup
  deformation invariance, open); (C) MO/FRT at ADE/Kummer
  locus only (scope-restricted, no global extension). None
  constructs the algebra on all of K3 moduli."

**C2.** Preface `chapters/frame/preface.tex:593-598` — Explicit
falsification: "The naive six-way isomorphism of the original CY-C
is therefore _falsified_."
- **S**: correctly inscribed. This is the load-bearing honesty of
  Vol III. The surviving pentagon structure (R_1 → R_3 → R_4 →
  R_5 → R_6, with R_2 demoted to "source") is the genuine
  Beilinson move.
- **Beilinson commendation**: this is the only place in the
  manuscript that performs the expected epistemic surgery.
  Every downstream chapter must inherit it. The k3_yangian
  chapter does _not_ propagate this scope uniformly — see D1
  below.

**C3.** `k3_yangian_chapter.tex:2223-2295` — `conj:stable-yangian-module`,
Bridgeland stability as Yangian parameter space.
- **S** with **Q**: labelled Conjecture. The dimension
  reconciliation (23 Yangian dof vs. 24 = dim Stab) via
  Conj. `conj:stab-dimension-reconciliation` (2322) reads as
  an _ansatz_: the stated fibre dimension 2+ρ is asserted, not
  derived, and no author of the literature (Bridgeland,
  Kontsevich–Soibelman) is cited for the claimed
  $(M_X = \text{params} \times t\text{-structure data})$
  factorisation. This decomposition is not a theorem.

### D. Super-Yangian layer (orthosymplectic)

**D1.** `k3_yangian_chapter.tex:1879-2072` — `conj:osp-yangian-mukai`,
`def:osp-super-yangian-K3`, `conj:k3-super-yangian`.
- **F → Q**: Definition 1919 carries `ClaimStatusProvedElsewhere`
  — this is _misleading_. What is "proved elsewhere" is the
  _general (m,n)_ orthosymplectic Yangian construction of
  Arnaudon–Crampé–Doikou–Frappat–Ragoucy (2003) and Molev (2007);
  the chapter's own Conjecture 1913 admits: "Existence at rank
  (4,20) is verified only at the structural level (grading,
  reflection equation, braid identities at osp(1|2) and
  osp(2|2)). Rank-(4,20) verification of the full reflection
  equation is _open_." So the definition is populated by
  inference from classical osp(m|n) theory, _not_ by explicit
  construction at rank (4,20). The definition should carry
  `ClaimStatusConjectured` or at minimum a scope qualifier
  stating "(4,20) instantiation is conjectural at the reflection-
  equation level."
- **Scope gap**: `rem:so-4-20-alternative` (2056) notes a genuine
  second candidate Y(so(4,20)) distinct from Y_{osp(4|20)}.
  Which of the two is "the" non-abelian K3 Yangian is
  _not_ determined by the programme; the remark defers to "the
  N=(2,2) worldsheet boundary algebra of K3 at the ADE
  enhancement point" — i.e., to physics heuristics. Beilinson
  rejects this: the algebra is determined by its own universal
  property, not by a physics preference.
- **Strongest honest form**: "At signature (4,20), _both_
  Y(so(4,20)) and Y_{osp(4|20)} exist as general-rank
  abstractions of published constructions. Which realises the
  non-abelian K3 Yangian (in the sense of being the image of Φ_2
  at enhancement points) is open; the programme offers physics
  heuristics favouring osp but no mathematical selection
  principle."

**D2.** `k3_yangian_chapter.tex:2179-2192` — "ZTE obstruction
persists" at O(κ^2) for both gl-super and osp-super Yang R-matrices.
- **S**: correctly labels the ZTE obstruction as unresolved.
  Consistent with AP-CY30 (pairwise YBE ≠ tetrahedron).

### E. BKM / imaginary-root layer

**E1.** `k3_yangian_chapter.tex:1267-1317` — `conj:bkm-yangian-generators`,
stratification by discriminant D.
- **S**: correctly Conjecture. The remark
  `rem:borcherds-serre-obstruction` (1290) states: "No Drinfeld
  presentation for Y(g) exists for _any_ BKM algebra g with
  nontrivial imaginary simple roots." This is the key Beilinson
  admission: the object "non-abelian K3 Yangian" extended to
  BKM generators is not just unproved, it has no known framework.
- **Scope reminder**: `rem:bkm-yangian-coha` (1283) correctly
  scopes CoHA = U(n_+(g_{Δ_5})) as an associative algebra, _not_
  a chiral algebra. This addresses AP-CY7 (construction /
  identification).

**E2.** `k3_yangian_chapter.tex:1747-1759` — `conj:k3-dbrane-bkm`,
BPS D-brane ↔ imaginary-root dictionary. Specifically the claim
c(-1) = 2.
- **Q**: the EZ convention is cited and correctly flagged
  (matches AP-CY42: "phi_{0,1} c(-1)=1 vs c(-1)=2 factor of 2 =
  κ_ch(K3) propagated silently"). The convention is stated; good.
  But the three-verification-path requirement is not satisfied:
  the chapter gives one derivation (`conj:k3-c-minus-1` at 2664,
  "winding modes"), and the verification at line 2698 cites
  only the direct Fourier expansion of φ_{0,1}. The "topological
  protection" argument for c(-1) = 2 as an exact result is a
  heuristic, not a theorem.

### F. Pentagon / V_4 bigraded Lefschetz layer

**F1.** `k3_yangian_chapter.tex:3248-3309` — Theorem
`thm:k3-pentagon-E1-edge-architecture`. ClaimStatusProvedHere,
but with conditional: "conditional on FM164, FM161."
- **F → Q**: "ProvedHere" + "conditional on FM164, FM161" is
  mutually inconsistent. If the result depends on unproved
  Yangian pro-nilpotent bar-cobar completion (FM164) and
  Yangian Koszulness in the Positselski framework (FM161), it
  should be `ClaimStatusConditional`, not `ClaimStatusProvedHere`.
- **Beilinson correction**: downgrade to `ClaimStatusConditional`.
  The `\ClaimStatusProvedHere` tag is the wrong one; the
  conditional hypothesis is explicit in the theorem statement.

**F2.** `k3_yangian_chapter.tex:3246-3358` — The "edge-architecture"
proof via Φ_{Borch} + Φ_{EK} + Φ_{FH}, with the fifth edge
"closing by Pentagon coboundary (Mac Lane K_5)."
- **F**: this is a _presentation_ of a closure diagram, not a
  proof. Each of the three closure morphisms is (a) attributed to
  external literature (Borcherds theta lift, Etingof–Kazhdan
  quantisation, factorisation homology = mode-algebra Ext), and
  (b) the claim that the three together witness the same Pentagon
  class vanishing is asserted by construction, not proved. The
  cobounding argument for the fifth edge misuses Mac Lane's
  coherence: Mac Lane's theorem says _all_ diagrams commute
  given _all_ edges commute, not that any four commuting edges
  force the fifth to commute.
- **Beilinson verdict**: the theorem as stated is an _outline_
  or _scheme of proof_; it should carry `ClaimStatusConjectured`
  and restate the outline as "a proof strategy requires (a)
  the Borcherds singular theta lift adapted to (4,20), (b) the
  EK twist identification of g_{K3} with the K3 R-matrix, (c)
  the FH identification of factorisation homology on S^1 with
  the mode algebra. Subject to these three identifications, the
  Pentagon class vanishes; the fifth edge then follows by Mac
  Lane coherence."

**F3.** `k3_yangian_chapter.tex:3363-3424` — Theorem
`thm:k3-multiproj-bigraded-lefschetz`. ClaimStatusConditional.
- **S**: correctly Conditional. The conditions (Caldararu chiral
  HRR, Hodge–de Rham E_2-collapse) are named.

**F4.** `k3_yangian_chapter.tex:3699-3764` — Theorem
`thm:k3-elliptic-tower-fixed-point`. Statement: M_{K3×E^k} = M^♭
= (0, 5, -16, 11) for all k.
- **S**: this is the genuine computational theorem of the V_4
  section. The proof (inductive use of
  Theorem `thm:universal-drinfeld-coupling-E`) is explicit.
  The universal identity M *_{V_4} M_E = M - σ_tot*(M) (5399-5441)
  is a direct 4×4 Fourier computation.
- **Q**: the content is _V_4-character bookkeeping_. It does not
  construct the non-abelian K3 Yangian. It is a consistency
  theorem on what a hypothetical Y(g_{K3}) _would_ produce at
  the character level if it existed. The ambient-qualifier
  discipline should make this explicit.

**F5.** `k3_yangian_chapter.tex:5502-5529` — Theorem
`thm:bracketing-associator-cohomology-class`, [a] ∈ H^3(V_4; Z[V_4]_0) = (Z/2)^2 with c_α = 0, c_β = 1.
- **S** with **Q**: a computation at witness triples. The claim is
  that the Pentagon obstruction lives in a (Z/2)^2 group; that it
  _projects_ onto a specific 1-dimensional sub-class. This is a
  finite-abelian group-cohomology computation on the V_4-Fourier
  bookkeeping; the classification at the witness triples is
  verifiable. Survives as a theorem about V_4-character
  combinatorics — not as a theorem about Y(g_{K3}) itself.

**F6.** `k3_yangian_chapter.tex:5667-5687` — Theorem
`thm:chain-to-matrix-pentagon-unification`. ClaimStatusConditional.
- **S**: correctly Conditional, on (a) chain-level Pentagon at K3,
  (b) additivity of Pentagon cocycle under Yangian tensor
  products, (c) V_4-equivariant Lefschetz formula. The first of
  these is F1/F2 above (itself questionable); the second is
  unproved; the third is standard.
- **Q**: `rem:chain-to-matrix-pentagon-five-quadruples` (5689)
  flags ProvedHere for the _numerical verification_ at five
  quadruples. The verification is numerical and cluster-specific;
  it does not establish the universal statement.

### G. Wave V110 and the sl_n chain-level Pentagon cocycle

**G1.** `notes/wave_V110_attack_heal_Y_sln_Pentagon.md:39-68` —
Explicit closed-form Pentagon cocycle for Y(sl_n),
[ω]^{Pentagon} = Σ (α_i, α_i) [ω^{(2)}_i].
- **S** for sl_n, simply-laced. The derivation from the Cartan-pair
  projector P_i = h_{α_i} ⊗ h_{α_i} / (α_i, α_i) is explicit, and
  matches Drinfeld (1985) at n=2 and Etingof–Kazhdan (1996, §4.7,
  Thm 4.7) at n=3. These are literature-verifiable cross-checks.
- **Q**: the file is a note, not an inscription. Lives in `notes/`,
  so by CLAUDE.md epistemic hierarchy, counts as a _draft_ that
  has not been moved into chapters/**.tex with a `\begin{proof}...
  \end{proof}` body. Until inscribed, it is provisional.

**G2.** `wave_V110.md:136-221` — Tarasov–Varchenko non-degeneracy
det(1 - A^{(2)}) = n · 4^{-(n-1)} > 0 for all n ≥ 2.
- **Q**: the derivation contains a notable internal inconsistency
  flagged within the note itself (§4.3 vs. §4.4): the first
  computation gives det = (-1)^{n-1} D_{n-1} with D sequence
  periodic and _vanishing_ at n-1 ≡ 2, 5 (mod 6); the "healed
  normalisation" (§4.4) re-derives in a different convention and
  obtains det = n·4^{-(n-1)} > 0. The note explicitly
  acknowledges that the V105 normalisation differs from the
  V110 raw computation. Beilinson reads this as: the closed
  form is convention-dependent and the author has not pinned
  down which convention corresponds to the programme's intended
  Pentagon cocycle. A specific computation in one fixed
  convention (consistent with the chapter's Theorem
  `thm:k3-abelian-yangian-presentation` conventions) is owed
  before this can be upgraded to a theorem.

**G3.** `wave_V110.md:238-269` — Non-simply-laced extension
to B_n, C_n, F_4, G_2 via the (α_i, α_i)-weighted formula.
- **F**: the extension is stated without derivation. The note
  says "By direct construction, 1 - A^{(2)}_{B_n} is positive
  definite with det > 0 for all n ≥ 2 in the appropriate
  normalization (analogous to §4.4); the proof is the same
  Chebyshev-recurrence argument, with the recurrence
  coefficients now non-uniform." For G_2 the number 5/9 is
  asserted without showing the 2×2 matrix entries. "Analogous
  to §4.4" is not a proof when §4.4 itself has the
  normalisation ambiguity of G2.
- **Scope honest form**: "Simply-laced proved at rank ≤ 3 via
  Etingof–Kazhdan; non-simply-laced is stated as a structural
  prediction awaiting case-by-case computation of the
  corresponding Gram matrix."

### H. Tests — `test_k3_nonabelian_all_ade.py`

**H1.** File docstring lines 1-20: "STATUS: CONJECTURAL (AP-CY14).
All results conditional on Y(g_{K3}). The Lie algebra data and Yang
R-matrices are unconditional mathematical facts; the K3 embedding is
conditional on CY-A_2 (proved at d=2)."
- **S**: _commendable_. The file is self-aware that what it tests
  is ADE data and Yang R-matrices (unconditional classical
  objects) with _K3 interpretation_ conditional. This is
  exactly the discipline Beilinson requires.

**H2.** Tests 91-169 — off-diagonal counts
{A1: 48, A2: 144, D4: 294, D5: 510, E6: 810, E7: 1218, E8: 1764}
with closed form d(d-1)(26-d) + C(d,2)(C(d,2)-1) in the 324×324
charge-2 Fock space.
- **S**: these are classical Lie-algebra dimension arithmetic.
  The closed form matches N*(N-1) for the Yang R-matrix block
  plus combinatorial tail. Survives as bookkeeping.
- **Q**: the test labels these as "K3 offdiag_324" — but the 324
  is p_{24}(2) = dim Fock^2, which is a Mukai-rank-24
  consequence, not intrinsically K3. Per `rem:k3-yangian-lattice-scope`
  the number 324 holds uniformly for any rank-24 even
  unimodular lattice. Label hygiene: substitute "rank-24 Fock"
  for "K3".

**H3.** TestYBE lines 442-477 — YBE verified numerically for
A1, A2, D4, D5, E6; "guaranteed analytically" for E7, E8 because
matrix "too large."
- **F**: "guaranteed analytically" is _not_ a verification. The
  Yang R-matrix for any simply-laced g satisfies YBE by a
  general theorem (Yang 1967, Drinfeld 1985). The statement
  should be "YBE holds by Drinfeld 1985 for simply-laced
  Lie algebras," with direct computation at small rank as a
  sanity check. "Guaranteed analytically" glosses over the fact
  that the test does nothing at E7, E8.

**H4.** TestADEDeformationsMukaiIV (lines 1068-1196) — "disjoint
sources: Mukai 1984 + Frenkel-Kac + Borel–de Siebenthal + direct
dimension formula."
- **Q**: four "disjoint" paths _but_ paths (i) Bourbaki dimensions
  and (iv) direct dimension formula arithmetic are literally
  the same table. Three paths would be more accurate. Does not
  invalidate the tests; misclassifies the verification structure.

### I. Cross-reference to Preface

**I1.** Preface line 593-598 declares the naive six-way CY-C
falsified. The k3_yangian chapter does _not_ consistently
propagate this falsification:
- Line 96 (k3_yangian_chapter.tex): "The routes are
  complementary: Route (A) constructs the algebra from the CY
  category, Route (B) constructs it from the 3d N=4 gauge
  theory. Where both are defined (Kummer/orbifold K3), they
  should agree." This is the old pre-falsification language.
  After the preface's pentagon restructuring, "they should
  agree" carries a sharpened burden: they can only be proved to
  agree at the character level (ρ, κ_ch), not at generator
  level.
- **Fix**: line 96-101 should acknowledge that generator-level
  agreement between Route A and Route B is part of what was
  _falsified_, and that only character-level agreement
  (constant κ_ch and ρ-trace around the pentagon) survives.

---

## (iii) Top-10 Most Fragile Claims by Severity (with corrections)

Severity grading:
- **Critical** = claim labels misrepresented status; downgrade
  required to preserve manuscript honesty.
- **High** = scope gap; qualifier needed.
- **Medium** = reformulation / convention-clarification.

| # | Severity | File:line | Claim | Correction |
|---|----------|-----------|-------|-----------|
| 1 | Critical | `k3_yangian_chapter.tex:3249` | `thm:k3-pentagon-E1-edge-architecture` carries `\ClaimStatusProvedHere` despite explicit "conditional on FM164, FM161" in the statement. | Downgrade to `\ClaimStatusConditional`. |
| 2 | Critical | `k3_yangian_chapter.tex:1921` | `def:osp-super-yangian-K3` carries `\ClaimStatusProvedElsewhere` though Conj. 1879-1917 admits rank-(4,20) reflection equation "open." | Downgrade definition to a `Conjecture/Construction` pairing: the general (m,n) form is ProvedElsewhere; the (4,20) specialisation is Conjectured. |
| 3 | Critical | `k3_yangian_chapter.tex:5667` | `thm:chain-to-matrix-pentagon-unification` is Conditional on F1 which is Critically mislabelled. Transitive weakness. | Fix propagates from fix to #1. |
| 4 | High | `k3_yangian_chapter.tex:713-846` | `prop:mukai-indefinite-yangian` scopes only loosely to gl_1; title "Indefinite Mukai signature poses no obstruction" overclaims. | Retitle: "Indefinite Mukai signature poses no obstruction _at the abelian (gl_1) level_; at non-abelian level the ω-twisted permutation carries a non-trivial crossing obstruction (see Remark A1 of Section …)." |
| 5 | High | `k3_yangian_chapter.tex:355-364` (and mirror `quantum_groups_foundations.tex:337-364`) | "Three independent constructions [that] approach the same algebra Y(g_{K3})" | Rewrite: "Three _conjectural_ routes that _would_ target a non-abelian K3 Yangian, each with its own scope-gap: Route A (Chiral) pending Yangian quantisation; Route B (BFN) proved only for resolved ADE surfaces and conjectural for Kummer; Route C (MO) restricted to ADE/Kummer moduli locus, no global extension." |
| 6 | High | `k3_yangian_chapter.tex:96-101` | `rem:k3e-two-routes-yangian`: "Where both are defined (Kummer/orbifold K3), they should agree." | Sharpen to: "Where both are defined, they should agree at the character level (κ_ch = 2, ρ = 24); generator-level agreement is part of what the preface's falsified six-way CY-C addressed, and even the surviving pentagon does _not_ equate R_A and R_B at generator level." |
| 7 | High | `k3_yangian_chapter.tex:2280-2336` | `conj:stab-yangian-parameter`, `conj:stab-dimension-reconciliation` | Add remark naming the authors who _should_ have stated the Stab = params × t-structure decomposition and explicitly flag that no published source does so; this is a new conjecture, not a reformulation. |
| 8 | High | `compute/tests/test_k3_nonabelian_all_ade.py:463-477` | YBE "guaranteed analytically" for E7, E8 — this is a non-verification masquerading as a test. | Reword: "YBE holds by Drinfeld 1985 Theorem 1 (simply-laced general-rank result); the numerical test is skipped at E7, E8 owing to matrix size. The theoretical result is cited, not tested." Distinguish "citation-verified" from "numerical-verified" in the test harness. |
| 9 | Medium | `notes/wave_V110_attack_heal_Y_sln_Pentagon.md:140-225` | The Tarasov–Varchenko determinant has two inconsistent closed forms in §4.3 vs. §4.4; convention is not pinned down. | Either inscribe a single normalisation consistent with the chapter's Theorem 877 conventions, or drop the closed-form claim from the programme and retain only the non-degeneracy statement. |
| 10 | Medium | `k3_yangian_chapter.tex:1747-1759` | `conj:k3-dbrane-bkm` gives c(-1)=2 (EZ convention) but the three-path verification requirement is not met. | Add three independent derivations (one already exists: direct Fourier of φ_{0,1}); two more are (a) the Jacobi form weight (character of the K3 elliptic genus), (b) the Weyl-vector normalisation in the BKM denominator. |

---

## (iv) Adversarial interrogation of the "one-sentence honest form"

Round 2, attacked.

**(i) Does "Y(g_{K3}) exists" have content, or is it a renaming?**
At abelian level gl_1: _renaming_. The algebra is a rank-24
Heisenberg Yangian (Drinfeld 1985 / Chari–Pressley 1995) with a
CY_2 constraint. "K3" is a physics label attached to the Mukai
lattice structure; the author himself acknowledges this at
`rem:k3-yangian-lattice-scope` (859-875).

At non-abelian level at ADE enhancement points: _specialisation_
of a proved object (BFN's shifted Yangian) via `thm:bfn-phi-ade-identification`.
Has content in the sense that the compatibility with Φ_2 is the
new piece; this is one theorem's worth of content.

At generic non-abelian K3 moduli: the claim "Y(g_{K3}) exists" has
_no constructed object_ to refer to. There is a candidate (Y(so(4,20))
or Y_{osp(4|20)}), there are conjectures, there is bookkeeping.
There is no construction.

**(ii) Is Y(g_{K3}) a NEW object, or a specialisation of known ones?**
Abelian: specialisation of Chari–Pressley. ADE-enhancement: specialisation
of BFN Coulomb branch. Non-abelian generic: no object; so the question
is degenerate.

**(iii) What is the programme's contribution? Compute the delta.**
- ✓ The V_4-Künneth character bookkeeping (Sec. 3179–5388). This is
  a genuine reorganisation of trace invariants into the Klein-four
  regular representation. It is a new _expository_ contribution
  that makes the K3-anchored fixed-point M^♭ = (0, 5, -16, 11)
  visible.
- ✓ The Pentagon cocycle class computation (G1, Theorem 5502): a
  cohomology-class identification in H^3(V_4; Z[V_4]_0) = (Z/2)^2.
  Genuine computation, genuine content, but _about_ the V_4
  bookkeeping rather than about Y(g_{K3}) itself.
- ✓ Theorem `thm:bfn-phi-ade-identification` Step 4 (Φ_2-compatibility):
  the one proved-elsewhere non-abelian identification. Content is
  the glue between CY-A_2 and BFN, not a new Yangian.
- ✓ The scope-honest labelling in `rem:k3-yangian-lattice-scope`,
  `rem:k3-abelian-yangian-classical`, `rem:k3-serre-mixing-mechanism`.
  Beilinson-style distillation.

**(iv) Is the NEW material (V_4 + Pentagon cocycle) a genuine advance
or a reformulation?**
Reformulation of existing Drinfeld-Etingof-Kazhdan / Tarasov-Varchenko
material into the V_4 regular-representation bookkeeping, plus one
finite-group-cohomology computation over this bookkeeping. Not an
advance of the underlying mathematics of Yangians. An advance of the
manuscript's _organisation_, yes.

---

## Open problems, correctly flagged

The chapter does correctly flag a number of genuine open problems:

- `rem:k3-yangian-obstruction` (639-652): existence of Y(g_{K3})
  at non-abelian level is open.
- `rem:borcherds-serre-obstruction` (1290-1295): no Drinfeld
  presentation for any BKM Yangian with imaginary simple roots.
- Conj. `conj:osp-yangian-mukai` (1879): (4,20)-rank reflection
  equation verification open.
- `rem:k3-yangian-obstruction-tests` A1 (1451-1469): ω-twisted
  crossing symmetry obstruction for non-abelian case.
- `rem:k3-yangian-obstruction-tests` A5 (1513-1535): four-layer
  scoping, with layer (iii) requiring chain-level framing data and
  layer (iv) requiring the Vol I Borcherds-lift bridge.

## Open problems, incorrectly flagged as solved

- `thm:k3-pentagon-E1-edge-architecture` (3248): ProvedHere, but
  the statement itself is conditional on FM164, FM161 (see Fragile
  #1 above).
- `def:osp-super-yangian-K3` (1919): ProvedElsewhere, but rank-(4,20)
  reflection equation is open (see Fragile #2 above).
- `quantum_groups_foundations.tex:337` (rem:cy-c-three-routes):
  "Three independent constructions" of C(g_{K3}, q); none of the
  three actually constructs the algebra at generic K3 moduli (see
  Fragile #5).
- `rem:chain-to-matrix-pentagon-five-quadruples` (5689): ProvedHere
  for the numerical verification at five quadruples, but this is
  cluster-by-cluster arithmetic, not a universal proof.

---

## Summary punchlist (Beilinson-compressed)

**Falsified / overstated (F)**: 4 items (#1, #2, #3, #F2 edge-arch
"proof" treatment, `test_k3_nonabelian_all_ade.py` YBE "guaranteed
analytically").
**Missing scope qualifier (Q)**: 6 items (#4–#9 above).
**Renaming / no new content (R)**: at least 3 (abelian K3 Yangian
presentation; osp(4|20) definition inherits from AcdfR; three-route
convergence is a restatement of three attribution tables).

**Surviving theorems of the chapter** (genuine content that resists
attack):
1. `thm:bfn-phi-ade-identification` (108-132) — ADE resolved-surface
   case; ProvedElsewhere; honestly composed.
2. `thm:k3-abelian-yangian-presentation` (878-1001) — abelian
   presentation; ProvedHere but with `rem:k3-abelian-yangian-classical`
   correctly stating the content is "a recasting of classical Drinfeld
   / CP."
3. `thm:k3-elliptic-tower-fixed-point` (3700) — M_{K3×E^k} = M^♭;
   genuine finite computation in V_4-Fourier.
4. `thm:universal-drinfeld-coupling-E` (3811) — M *_V_4 M_E =
   M - σ*(M); direct Fourier identity.
5. `thm:bracketing-associator-cohomology-class` (5502) — cocycle class
   in H^3(V_4; Z[V_4]_0) = (Z/2)^2 with c_α = 0, c_β = 1.
6. `thm:k3-mock-modular-proof` (2845) — K3 mock-modular four-step at
   d = 2, via Gaberdiel + Huang + CGR + Zwegers + DMZ; cleanly
   composed, honestly scoped.

**Non-surviving as Yangian claims** (survive only as V_4 / lattice
/ character bookkeeping):
- Every theorem of Section 3179–7078 in the k3_yangian chapter is a
  V_4-character or finite-group-cohomology statement, not a
  theorem _about_ the non-abelian K3 Yangian.

**Final Beilinson verdict**: the chapter's "non-abelian K3 Yangian"
is simultaneously (i) an _honestly scoped abelian theorem_ via the
Heisenberg/signature(4,20)/CY_2 layer, (ii) an _honestly scoped ADE
specialisation_ via BFN, and (iii) a _large cloud of conjectures_ that
inherits the preface's falsification of six-way CY-C without uniformly
propagating it. The genuine advances are scope-honest remarks, the V_4
bookkeeping, and the Pentagon cocycle class computation; the rest is
reorganisation. A smaller true theorem beats a larger false one, and
that smaller true theorem is already in the chapter, under
`thm:k3-abelian-yangian-presentation` and `rem:k3-yangian-lattice-scope`.

— End of audit.
