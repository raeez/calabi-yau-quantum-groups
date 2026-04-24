# Agent 04 -- Etingof axis: PBW / integrality / representation category

Date: 2026-04-24.

Scope contract: read-only on manuscript files.  This note is the only owned output:
`notes/adversarial_bps_positive_geometry_20260424/agent_04_etingof_pbw.md`.

## Files and anchors read

- `CLAUDE.md:1-502`, `AGENTS.md:1-498`.
- `chapters/theory/quantum_groups_foundations.tex:15-127`: effective BPS positive geometry, conditional Drinfeld double.
- `chapters/theory/quantum_groups_foundations.tex:530-537`: CY-C at `d=3` remains conjectural except the local `C^3` positive-half case.
- `chapters/theory/quantum_groups_foundations.tex:1014-1185`: root-of-unity BKM small-form/MTC claims.
- `chapters/theory/quantum_groups_foundations.tex:6147-6234`: generalized CY3 root datum and automorphic multiplicities.
- `chapters/examples/coha_wall_crossing_platonic.tex:12-72`: algebra/coalgebra, positive half/full Yangian, motivic/numerical split.
- `chapters/examples/coha_wall_crossing_platonic.tex:111-140`, `143-203`: CoHA has no internal differential; bar complex is separate.
- `chapters/examples/coha_wall_crossing_platonic.tex:298-360`: positive-half embedding and PBW decomposition.
- `chapters/examples/coha_wall_crossing_platonic.tex:414-700`: KS motivic/classical Hall dgLAs.
- `chapters/examples/coha_wall_crossing_platonic.tex:2403-2437`: KS sign conventions.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:337-355`: K3 x E shuffle-presentation claim.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:2964-3028`: `zeta_8` PBW trichotomy and tilting quotient.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:5181-5225`: super-Yangian PBW proposition.
- `chapters/examples/toric_cy3_coha.tex:2136-2170`, `2173-2188`: compact-CY3 extension and K3 x E Hall-Drinfeld double claim.
- `notes/adversarial_architecture_swarm_20260424/agent_05_k3e_bkm_yangian.md:63-93` and `agent_06_coha_positive_half.md:235-281`: prior local guardrails.
- `compute/lib/k3_yangian_adversarial.py:42-52`, `379-428`: compute-side finite-generator/bar-multiplicity separation.

Primary-source obligations checked externally: Davison--Meinhardt, *Cohomological Donaldson--Thomas theory of a quiver with potential and quantum enveloping algebras*, arXiv:1601.02479 / Invent. Math. 221 (2020), proves the Hodge-theoretic integrality and wall-crossing categorification and realizes the isomorphisms as PBW isomorphisms for the CoHA.  Davison, *The critical CoHA of a quiver with potential*, arXiv:1311.7172 / QJM 68 (2017), builds the coproduct and dimensional-reduction machinery for quivers with potential.  The local citation `Davison 2017 arXiv:1512.04179` should be checked: the primary critical-CoHA arXiv number is `1311.7172`; `1512.08898` is Davison--Meinhardt on homological dimension one with potential.

## Verdict

The clean theorem is a positive-half PBW theorem under explicit Hall hypotheses.  It does not, by itself, construct the Drinfeld double, a braided representation category, a K3 x E Hall--Borcherds comparison, or a root-of-unity modular tensor category.  The manuscript has good local caveats at `quantum_groups_foundations.tex:96-126` and `coha_wall_crossing_platonic.tex:1513-1514`, but other anchors promote the same input too far.

## ATTACK 1 -- PBW integrality promoted to a quantum group

Attack.  `quantum_groups_foundations.tex:96-126` assumes Davison--Meinhardt PBW integrality and then defines a Drinfeld double.  The danger is to read the PBW theorem as constructing the whole `G_sigma(X)`.

Failure mode.  PBW is a filtered vector-space / algebra statement for the positive CoHA.  The double also needs a Serre-duality Hall pairing, non-degeneracy, a Cartan completion, and compatibility of the coproduct with the chosen completion.

Heal.  Keep the theorem exactly conditional:

```tex
\begin{theorem}[PBW positive half, admissible Hall datum]
Let $(\mathcal C,\sigma)$ be a CY_3 Hall datum with orientation data,
an oriented critical atlas on semistable stacks, a strict-sector
completion of the effective charge monoid, and a Davison--Meinhardt
PBW filtration on each fixed-slope critical CoHA.  Then
\[
  \operatorname{gr}_F \mathcal H_{\sigma,\mu}^{crit}
  \cong
  \operatorname{Sym}_{super}
  \bigl(\operatorname{BPS}_{\sigma,\mu}\otimes H^\bullet(B\mathbb C^*)\bigr)
\]
as graded supercommutative objects, and ordered PBW monomials give a
basis of the completed positive half
$Y^+_\sigma(X)=\widehat{\bigoplus_\mu \mathcal H_{\sigma,\mu}^{crit}}$.
If, in addition, a non-degenerate Hall pairing with the Serre-dual
opposite half and a Cartan completion are supplied, the Drinfeld double
$D(Y^+_\sigma(X))$ is defined.
\end{theorem}
```

Boundary.  PBW proves `Y^+`, not `D(Y^+)`; `D(Y^+)` begins only after the pairing/completion hypotheses.

## ATTACK 2 -- Davison--Meinhardt input overextended to K3 x E

Attack.  `k3_chiral_bialgebra_platonic.tex:337-344` says the K3 x E CoHA admits a shuffle presentation through Schiffmann--Vasserot, Davison--Meinhardt, and Davison 2017.  `toric_cy3_coha.tex:2179-2188` similarly moves from Davison integrality to a non-toric Hall--Drinfeld double.

Failure mode.  Davison--Meinhardt proves the PBW/integrality theorem for quivers with potential / Jacobi algebras under its hypotheses.  K3 x E is compact and non-toric; `toric_cy3_coha.tex:2136-2170` itself says equivariant localization and chain-level explicit constructions are unavailable for compact CY3s and remain open.

Heal.  The K3 x E statement should be split:

- The reduced DT / Igusa character identity is theorem-grade where proved by the cited K3 x E DT literature.
- The Hall--Drinfeld double
  `D_hbar(Y_hbar^Hall(CoHA_{K3 x E}))` is conditional until the oriented critical atlas, local-to-global Hall comparison, pairing/completion, and Hall--Borcherds comparison are constructed.
- A rank-24 shuffle kernel is evidence/model data unless a primary theorem proves exactly that K3 x E CoHA has that shuffle presentation.

Boundary.  Davison--Meinhardt supplies the PBW theorem for the admissible critical CoHA input; it does not supply the compact K3 x E atlas, the global shuffle kernel, or the BKM double.

## ATTACK 3 -- Super sign and PBW parity

Attack.  The BKM and super-Yangian PBW claims risk treating signed denominator coefficients as ordinary positive dimensions.  `quantum_groups_foundations.tex:928-939` correctly says the denominator multiplicity is signed, while `k3_chiral_bialgebra_platonic.tex:5199-5204` imposes exterior powers for fermionic generators.

Failure mode.  Root multiplicity in a BKM superalgebra is a superdimension
`mult = mult_even - mult_odd`.  PBW must be
`Sym(V_even) tensor Lambda(V_odd)`, with Koszul signs and the Borcherds sign bicharacter.  A raw absolute value `|mult|` loses the denominator identity.

Heal.  State parity before PBW:

```tex
V_\alpha = V_{\alpha,\bar 0}\oplus V_{\alpha,\bar 1},\qquad
\operatorname{sdim} V_\alpha =
\dim V_{\alpha,\bar 0}-\dim V_{\alpha,\bar 1}=c_\varphi(\alpha).
```

Then the PBW monomials use arbitrary powers on even generators and exponents `0,1` on odd generators.  The KS pentagon convention must also be fixed: `coha_wall_crossing_platonic.tex:2406-2437` separates Reineke `Omega=+1` from the fermionic `Omega=-1` convention.

Boundary.  Super PBW is valid only after parity and sign cocycle are part of the datum; signed automorphic multiplicities cannot be replaced by raw BPS dimensions.

## ATTACK 4 -- Motivic and numerical integration conflated

Attack.  `quantum_groups_foundations.tex:61-64` allows motivic or numerical integration.  `coha_wall_crossing_platonic.tex:414-700` then has to repair the distinction between `g_KS^mot` and `g_KS^cl`.

Failure mode.  The motivic Hall algebra carries the `L^{1/2}` quantum torus and the nontrivial quantum dilogarithm; the numerical specialization is an Euler-characteristic shadow.  Dropping `L^{1/2}` collapses the quantum cocycle and changes the pentagon.

Heal.  Every PBW statement must name its ambient:

- Motivic / monodromic mixed-Hodge PBW: coefficients in the motivic or Hodge-theoretic realization; quantum torus and `q`-commutator retained.
- Numerical PBW shadow: Euler-characteristic specialization; classical Poisson torus; less information.

Boundary.  Numerical CoHA data cannot reconstruct refined/motivic root multiplicities or K-theoretic Hall parameters without an additional lift.

## ATTACK 5 -- Representation-category consequences overclaimed

Attack.  `quantum_groups_foundations.tex:1106-1185` claims a non-semisimple MTC and semisimple quotient at `zeta_8`.  But `k3_chiral_bialgebra_platonic.tex:2966-2988` says the full `u_{zeta_8}(H_{Delta_5})` is infinite-dimensional before the tilting quotient, and `quantum_groups_foundations.tex:1053-1097` contains incompatible counts: statement `8^129`, proof line `8^255`, and then an unspecified effective count.

Failure mode.  PBW flatness gives a basis and filtered control.  It does not imply finite tensor category, rigidity, braiding, ribbon element, nondegenerate Lyubashenko pairing, or semisimple MTC.  The full BKM imaginary sector is not finite-dimensional; bosonic imaginary divided powers survive unless a quotient kills them.

Heal.  Separate three objects:

1. Real-root truncated small form: finite only after exact real-root subsystem and truncation index are proved.
2. Full BKM root-of-unity object: infinite-dimensional if bosonic imaginary divided powers remain.
3. Tilting / negligible quotient: finite-rank category only after the trace-radical quotient and braiding data are constructed.

Boundary.  Representation-category claims are conditional past the real-root finite-type reduction.  PBW is a prerequisite, not an MTC theorem.

## ATTACK 6 -- Root multiplicities identified too early with BPS invariants

Attack.  The text moves among three quantities: Davison--Meinhardt BPS cohomology generators, KS wall-crossing invariants `Omega_sigma(gamma)`, and BKM automorphic root multiplicities from Jacobi coefficients.

Failure mode.  These are not the same object.  `quantum_groups_foundations.tex:6147-6234` defines CY3 root multiplicities from a Jacobi-type form and an automorphic denominator.  `coha_wall_crossing_platonic.tex:2362-2363` allows chamber multiplicities to reshuffle under gauge transformation.  The compute guardrail `k3_yangian_adversarial.py:42-52`, `379-428` keeps BKM multiplicities as bar/denominator data, not standard Yangian generators.

Heal.  Use a three-level ledger:

- `BPS_{sigma,mu}`: cohomological generators in the Davison--Meinhardt PBW theorem.
- `Omega_sigma(gamma)`: motivic or numerical wall-crossing coefficient, chamber-dependent.
- `mult_BKM(alpha)`: signed automorphic root multiplicity in the Borcherds denominator.

The equality `BPS/CoHA data = BKM multiplicities` is a theorem only after a Hall--Borcherds comparison identifies the character/denominator and respects parity.  Until then it is a source obligation.

Boundary.  Character agreement is not algebra agreement; denominator multiplicities do not define a Hall--Drinfeld double without the comparison functor.

## Clean theorem skeleton for manuscript repair

The safe inscription target is:

```tex
\begin{theorem}[PBW integrality for the admissible positive Hall half]
\ClaimStatusProvedElsewhere\ on Davison--Meinhardt quiver-with-potential
loci; \ClaimStatusConditional\ for compact non-toric CY_3 categories.
Let $(\mathcal C,\sigma)$ be an oriented CY_3 Hall datum whose fixed-slope
semistable stacks are covered by critical quiver-with-potential charts
to which the Davison--Meinhardt theorem applies, and assume the resulting
critical CoHA is locally finite after strict-sector completion.  Then the
positive half $Y^+_\sigma(X)$ has a PBW filtration whose associated graded
is the free supercommutative algebra on the BPS cohomology.  The parity is
the vanishing-cycle/Koszul parity, and numerical DT invariants are obtained
only after Euler-characteristic specialization.

If a Serre-dual opposite half, non-degenerate completed Hall pairing, Cartan
completion, and compatible coproduct are also constructed, the Drinfeld
double $D(Y^+_\sigma(X))$ exists.  Any braided representation category,
root-of-unity quotient, or BKM denominator identification is additional
structure, not a consequence of PBW alone.
\end{theorem}
```

## Exact failure boundaries

- Proved elsewhere: Davison--Meinhardt PBW/integrality for quiver-with-potential CoHAs; KS/Joyce--Song/Bridgeland wall-crossing in their stated motivic or numerical Hall ambients; `CoHA(C^3)=Y^+(glhat_1)` as positive half.
- Conditional: `G_sigma(X)=D(Y^+_sigma(X))` outside explicit Hall-pairing loci; compact K3 x E structural CoHA/double; toric no-compact-4-cycle affine-super-Yangian identification beyond its published hypotheses.
- Conjectural/source-obligation: Hall--Borcherds comparison for K3 x E; rank-24 global shuffle kernel for K3 x E; full nonabelian BKM/Yangian/Hall comparison; finite MTC quotient from the BKM root-of-unity object.
- False shortcut: PBW integrality implies full quantum group; motivic integration equals numerical integration; signed BKM multiplicity equals raw BPS dimension; `CoHA = W_{1+infty}`; BKM side is a standard Drinfeld Yangian.

## Verification

- `python -m pytest compute/tests/test_k3_yangian_adversarial.py -q` failed because `python` is not on PATH.
- `python3 -m pytest compute/tests/test_k3_yangian_adversarial.py -q` passed: `31 passed in 0.33s`.

No manuscript files were edited.
