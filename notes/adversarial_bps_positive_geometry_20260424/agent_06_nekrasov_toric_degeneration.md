# Agent 06: Nekrasov Toric Degeneration Report

Scope: toric degeneration and enumerative computation for the effective
BPS positive geometry.  Owned file only.

Target degeneration:

\[
\Gamma^+_{\mathrm{eff},\sigma}(X_\Sigma)=\mathbb Z_{\ge 0}^{Q_0},\qquad
\mathcal M^+_{\mathrm{eff},\sigma}(X_\Sigma)
=\coprod_{\mathbf d\in\mathbb Z_{\ge 0}^{Q_0}}
[\mathrm{Crit}(W_{\mathbf d})/G_{\mathbf d}],
\qquad
G_{\mathbf d}=\prod_{i\in Q_0}\mathrm{GL}(d_i).
\]

The positive half is
\[
Y^+_\sigma(X_\Sigma)
=H^\bullet_{\mathrm{eq}}\bigl(\mathcal M^+_{\mathrm{eff},\sigma},
\phi_W\bigr)
=\mathrm{CoHA}(Q_\Sigma,W_\Sigma),
\]
with the Hall product.  The Drinfeld double is extra data.

Local manuscript anchors read:

- `chapters/theory/quantum_groups_foundations.tex:129-170`:
  toric effective geometry, \(\mathbb Z_{\ge0}^{Q_0}\), quotient critical
  stacks, positive-half CoHA.
- `chapters/examples/toric_cy3_coha.tex:74-88`: critical CoHA definition,
  dimension vectors, vanishing cycles, Hall multiplication.
- `chapters/examples/coha_wall_crossing_platonic.tex:84-123` and
  `:212-268`: quiver/potential ledger; CoHA is an associative graded
  algebra, not a dg object.
- `chapters/theory/quantum_groups_foundations.tex:545-568` and
  `chapters/examples/toric_cy3_coha.tex:169-253`: \(Y^+\) versus full
  Yangian versus \(\mathcal W_{1+\infty}\).

## ATTACK/HEAL 1: effective monoid indexed by vertices

Attack.  A toric degeneration formula using arrows, roots, toric cones, or
Mori curve generators instead of \(Q_0\) has the wrong grading.  It would give
\(\mathbb Z_{\ge0}^{Q_1}\) for the Klebanov--Witten conifold or
\(\mathbb Z_{\ge0}^{9}\) for local \(\mathbb P^2\), contradicting the CoHA
dimension-vector grading.

Heal.  The effective monoid is the monoid of dimension vectors:
\[
\mathbf d=(d_i)_{i\in Q_0},\qquad
\Gamma^+_{\mathrm{eff},\sigma}=\mathbb Z_{\ge0}^{Q_0}.
\]
Concrete checks:

- \(\mathbb C^3\): \(Q_0=\{*\}\), so \(\Gamma^+=\mathbb Z_{\ge0}\).
- Conifold: \(Q_0=\{0,1\}\), so \(\Gamma^+=\mathbb Z_{\ge0}^2\).
- Local \(\mathbb P^2\): McKay \(\mathbb Z_3\) quiver has \(3\) vertices
  and \(9\) arrows, so \(\Gamma^+=\mathbb Z_{\ge0}^3\), not
  \(\mathbb Z_{\ge0}^9\).

Computation run:

```text
LocalP2 quiver vertices/arrows/potential_terms = 3, 9, 6
Conifold generator counts = 2, 3 across the two chamber subalgebras
```

Test to add: `test_toric_effective_monoid_rank_by_vertices`, asserting
`len(Gamma_eff_basis) == len(Q0)` for the Jordan, Klebanov--Witten, and
McKay \(\mathbb Z_3\) quivers, and explicitly rejecting `len(Q1)`.

Source obligations: Kontsevich--Soibelman 2008, Section 2.3
(`https://arxiv.org/abs/0811.2435`); Kontsevich--Soibelman 2010 CoHA
construction (`https://arxiv.org/abs/1006.2706`); Davison--Meinhardt
PBW/integrality (`https://arxiv.org/abs/1601.02479`).

## ATTACK/HEAL 2: critical stacks are quotient stacks, not raw critical loci

Attack.  Writing only \(\mathrm{Crit}(W_{\mathbf d})\) suppresses the gauge
group \(G_{\mathbf d}\) and loses stack stabilisers.  Writing only
\(\mathrm{Rep}(Q,\mathbf d)\) with \(\phi_{W_{\mathbf d}}\) suppresses the
critical support.  Both errors can produce correct-looking characters while
breaking Hall correspondences and orientation data.

Heal.  The toric terminal fibre is the disjoint union of quotient critical
stacks
\[
\coprod_{\mathbf d\in\mathbb Z_{\ge0}^{Q_0}}
[\mathrm{Crit}(W_{\mathbf d})/G_{\mathbf d}],
\qquad
G_{\mathbf d}=\prod_i \mathrm{GL}(d_i),
\]
with vanishing-cycle sheaf \(\phi_{W_{\mathbf d}}\).  Equivalent shorthand
\[
H^\bullet_{G_{\mathbf d}}\bigl(\mathrm{Rep}(Q,\mathbf d),\phi_{W_{\mathbf d}}\bigr)
\]
is acceptable only when the quotient-stack and vanishing-cycle conventions
are stated.

Concrete cases:

- \(\mathbb C^3\): one vertex, \(G_n=\mathrm{GL}_n\),
  \(W_n=\mathrm{Tr}(X[Y,Z])\), and \(\mathrm{Crit}(W_n)\) is the commuting
  triple locus \([X,Y]=[Y,Z]=[Z,X]=0\).  Torus-fixed ideals are plane
  partitions.
- Conifold: \(G_{(d_0,d_1)}=\mathrm{GL}_{d_0}\times\mathrm{GL}_{d_1}\),
  \(W=\mathrm{Tr}(a_1b_1a_2b_2-a_1b_2a_2b_1)\), with KW F-term critical
  equations.
- Local \(\mathbb P^2\): \(G_{\mathbf d}=\prod_{i=0}^2\mathrm{GL}_{d_i}\)
  and the McKay potential is
  \[
  W=\sum_{i\in\mathbb Z/3}\mathrm{Tr}
  (X_iY_{i+1}Z_{i+2}-X_iZ_{i+1}Y_{i+2}).
  \]

Test to add: `test_critical_stack_group_is_product_gl`, building the three
example quivers and checking the displayed \(G_{\mathbf d}\), the number of
potential terms, and the quotient-stack notation.  A companion parser test
should ensure future prose never states the toric degeneration as raw
`\mathrm{Crit}(W_{\mathbf d})` without `/G_{\mathbf d}` nearby.

Source obligations: Ginzburg 2006, Proposition 5.1.9 for the dg algebra
attached to \((Q,W)\); Davison--Meinhardt 2016/2020 for critical CoHA and PBW;
Szendroi conifold NCCR (`https://arxiv.org/abs/0705.3419`).

## ATTACK/HEAL 3: shuffle basis is a toric terminal basis, not a universal basis

Attack.  The phrase "the theta basis becomes the shuffle/plane-partition
basis" can be over-read as a universal basis for all BPS positive geometries.
That is false.  It holds in the toric terminal degeneration, where the chamber
complex is rational polyhedral and the CoHA has a shuffle presentation.

Heal.  State the degeneration precisely:
\[
\Theta^{\mathrm{BPS}}_\sigma
\rightsquigarrow
\{\text{shuffle monomials indexed by dimension vectors and fixed points}\}.
\]
For \(\mathbb C^3\), the fixed-point basis of
\(\mathrm{Hilb}^n(\mathbb C^3)\) is indexed by plane partitions of \(n\).
For conifold and local \(\mathbb P^2\), the basis is coloured by the vertex
set and chamber data; it is not a single uncoloured plane-partition set.

Concrete computation:

```text
C3 plane partitions p(0..10) =
[1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
C3 Yangian/CoHA dimension match =
dimensions_match_pp_counts: True
character_equals_macmahon: True
```

Test to add: `test_shuffle_basis_terminal_degeneration`, asserting:

- for \(Q_0=\{*\}\), basis counts equal MacMahon coefficients;
- for conifold \(Q_0=\{0,1\}\), chamber subalgebra bar counts are
  \(2^k\) and \(3^k\), not MacMahon;
- for local \(\mathbb P^2\), the first coefficients are the
  \(\mathbb Z_3\)-coloured/McKay equaliser coefficients, not the bare
  one-vertex sequence.

Source obligations: Schiffmann--Vasserot 2013 positive-half result
(`https://arxiv.org/abs/1202.2756`); Rapcak--Soibelman--Yang--Zhao 2018
for CoHA/double actions and toric extension scope
(`https://arxiv.org/abs/1810.10402`).

## ATTACK/HEAL 4: \(\mathbb C^3\) is \(Y^+\), not \(\mathcal W_{1+\infty}\)

Attack.  The MacMahon character, the affine Yangian, and the VOA evaluation
chain can be collapsed into a false identity
\[
\mathrm{CoHA}(\mathbb C^3)=\mathcal W_{1+\infty}.
\]
The character equality does not supply the negative half, Cartan, OPE
locality, or vertex algebra structure.

Heal.  The correct chain is
\[
\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
\hookrightarrow
Y(\widehat{\mathfrak{gl}}_1)
\xrightarrow{\mathrm{ev}_\lambda}
\mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac}).
\]
The first equality is associative \(E_1\)-Hall.  The second step is a
Drinfeld-double embedding.  The last step is an evaluation representation,
not an isomorphism of CoHA with a VOA.

Concrete computation:

```text
Z^{DT}_{C3}(q)=M(-q):
q^0..q^8 = 1, -1, 3, -6, 13, -24, 48, -86, 160
MacMahon two-method match through order 15 = True
```

Test to add: `test_c3_positive_half_evaluation_chain`, using existing
`compute/tests/test_coha_wall_crossing_platonic.py` structure to require:
`Y_plus_modes < Y_full_modes`, `Y_minus_modes` disjoint from `Y_plus_modes`,
and MacMahon character equality stated only for \(Y^+\).

Source obligations: local anchors `quantum_groups_foundations.tex:550-568`,
`toric_cy3_coha.tex:221-253`, and `coha_wall_crossing_platonic.tex:29-38`.
Primary: Schiffmann--Vasserot 2013; Kapranov--Vasserot 2018; Gaiotto--Rapcak
2017 for the VOA target.

## ATTACK/HEAL 5: conifold chamber subalgebras are not two different ambient CoHAs

Attack.  The conifold data can be misread as saying the ambient CoHA changes
from a \(2\)-generator algebra to a \(3\)-generator algebra across the wall.
That is false.  The two counts belong to chamber-specific Hall subalgebras
inside one chamber-independent critical CoHA.

Heal.  Keep the three levels separate:
\[
\mathcal H_{\mathrm I},\mathcal H_{\mathrm {II}}
\subset
\mathcal H(Q_{\mathrm{con}},W_{\mathrm{con}}).
\]
The bar dimensions are
\[
\dim B^k(\mathcal H_{\mathrm I})=2^k,\qquad
\dim B^k(\mathcal H_{\mathrm {II}})=3^k,
\]
but Davison--Meinhardt PBW/integrality identifies the ambient algebra as a
single stability-independent object after the BPS filtration is accounted for.

Concrete computation:

```text
Conifold B^k totals I  = {1: 2, 2: 4, 3: 8, 4: 16}
Conifold B^k totals II = {1: 3, 2: 9, 3: 27, 4: 81}
Gauge match at (1,0), (0,1), (1,1) = True, True, True
Conifold GV d=1..5 = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0}
Reduced Q^1 coefficients q^0..q^6 = 0, -1, -2, -3, -4, -5, -6
```

The wall-crossing gauge series computed in the existing engine starts
\[
e^{\mathrm{ad}_\alpha}\Theta_{\mathrm I}
=-e_{10}-e_{01}-e_{11}
-\frac12 e_{21}-\frac16 e_{31}-\frac1{24}e_{41}-\cdots .
\]

Test to add: `test_conifold_ambient_coha_fixed_chamber_subalgebras_vary`,
asserting the \(2^k/3^k\) chamber counts, primitive-charge agreement, and the
single ambient `H(Q_con,W_con)` label.  Also add a string-guard test rejecting
"conifold is local surface"; the conifold is
\(\mathrm{Tot}(\mathcal O(-1)^{\oplus2}\to\mathbb P^1)\), not
\(\mathrm{Tot}(K_{\mathbb P^1})\).

Source obligations: Szendroi 2007 (`https://arxiv.org/abs/0705.3419`);
Nagao--Nakajima 2011; Davison--Meinhardt (`https://arxiv.org/abs/1601.02479`);
Bryan--Pandharipande for the conifold GV closed form.

## ATTACK/HEAL 6: local \(\mathbb P^2\) is a \(\mathbb Z_3\) McKay equaliser, not a conifold analogue

Attack.  Local \(\mathbb P^2\) can be flattened to "three copies of
\(\mathbb C^3\)" or confused with the conifold's two-chart KW gluing.  That
forgets the \(\mathbb Z_3\) McKay quotient, the three-vertex dimension-vector
grading, and the nontrivial triple-overlap/equaliser constraint.

Heal.  The local \(\mathbb P^2\) chart data is:
\[
K_{\mathbb P^2}\simeq [\mathbb C^3/\mathbb Z_3]^{\mathrm{res}},
\quad
Q_0=\{0,1,2\},\quad
|Q_1|=9,
\]
with three arrows \(i\to i+1\) for each coordinate direction and the cubic
\(\epsilon_{abc}\)-potential.  The CoHA is glued as an equaliser of three
\(\mathbb C^3\) positive halves over pairwise overlaps:
\[
\mathrm{CoHA}(K_{\mathbb P^2})
\simeq
\mathrm{eq}\Bigl(\prod_{i=0}^2Y^+(\widehat{\mathfrak{gl}}_1)
\rightrightarrows
\prod_{i<j}Y^+(\widehat{\mathfrak{sl}}_2)\Bigr)
\]
with \(\mathbb Z_3\)-equivariance.

Concrete computation:

```text
LocalP2 kappa_ch paths = 3/2, 3/2, 3/2, 3/2
CoHA vs MacMahon^3 through degree 4:
coefficients = [1, 3, 12, 37, 111], all_match = True
Z3 DT simples = 1, 1, 1
DT(1,1,1) = -3
GV d=1..4 = {1: 3, 2: -6, 3: 27, 4: -192}
```

Test to add: `test_local_p2_terminal_degen_mckay_equalizer`, asserting:

- \(Q_0=3\), \(Q_1=9\), six cubic potential terms;
- \(\Gamma^+=\mathbb Z_{\ge0}^3\);
- four independent computations give
  \(\kappa_{\mathrm{ch}}(K_{\mathbb P^2})=3/2\);
- degree \(0\ldots4\) coefficients match \(M(q)^3\), while the GV tower
  matches \(3,-6,27,-192\).

Source obligations: Bridgeland--King--Reid McKay correspondence
(`https://arxiv.org/abs/math/9908027`); AKMV topological vertex
(`https://arxiv.org/abs/hep-th/0305132`); Konishi toric GV integrality
(`https://arxiv.org/abs/math/0504188`).

## Test Run

Command:

```bash
pytest -q compute/tests/test_c3_dt_partition.py \
  compute/tests/test_conifold_bar_complex.py \
  compute/tests/test_local_p2_chart_gluing.py \
  compute/tests/test_toric_cy3_dt_engine.py \
  compute/tests/test_coha_wall_crossing_platonic.py
```

Result:

```text
379 passed in 0.48s
```

Additional direct computations were run from existing compute modules:
`compute.lib.c3_dt_partition`, `compute.lib.conifold_bar_complex`,
`compute.lib.local_p2_chart_gluing`, and `compute.lib.toric_cy3_dt_engine`.

## Verdict

CONVERGED for this axis.  The toric terminal degeneration must be stated
with vertex-indexed dimension vectors, quotient critical stacks, and the
positive-half CoHA.  The three example strata separate cleanly:

- \(\mathbb C^3\): one-vertex Jordan quiver, plane partitions, \(M(q)\),
  \(\mathrm{CoHA}=Y^+\), not \(\mathcal W_{1+\infty}\).
- Conifold: two-vertex KW quiver, \(\mathbb Z_{\ge0}^2\), chamber
  subalgebras \(2^k/3^k\), one ambient CoHA, \(\kappa_{\mathrm{ch}}=1\).
- Local \(\mathbb P^2\): three-vertex \(\mathbb Z_3\) McKay quiver,
  \(\mathbb Z_{\ge0}^3\), three-chart equaliser, \(M(q)^3\) low-degree
  check, \(\kappa_{\mathrm{ch}}=3/2\).

No manuscript files were edited.
