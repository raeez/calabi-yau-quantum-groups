# Agent 03 -- Drinfeld/Kazhdan axis

Scope: chambered effective BPS positive geometry.  Claim attacked:
\[
  G_\sigma(X)=D\bigl(Y^+_\sigma(X)\bigr).
\]

Manuscript surface read:
`CLAUDE.md`, `AGENTS.md`,
`chapters/theory/quantum_groups_foundations.tex`,
`chapters/examples/coha_wall_crossing_platonic.tex`,
`chapters/examples/toric_cy3_coha.tex`.

Local anchors:
- `quantum_groups_foundations.tex:80--124` defines
  \(Y^+_\sigma(X)\), \(Y^0_\sigma(X)\), \(Y^-_\sigma(X)\), and the
  conditional positive-geometry Drinfeld double.
- `quantum_groups_foundations.tex:545--571` fixes the
  \(\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\) chain.
- `coha_wall_crossing_platonic.tex:1346--1432` separates positive half
  from full Yangian.
- `toric_cy3_coha.tex:1616--1815` assembles the toric chiral quantum
  group datum.
- `toric_cy3_coha.tex:984--1198` gives the conifold super-shuffle,
  bialgebra, and double discipline.
- `quantum_groups_foundations.tex:4445--4620` gives the conditional
  \(K3\times E\) Hall--BKM comparison.

## Verdict

The raw formula is not a theorem without extra data.  The correct
statement is a completed, chambered, paired, Cartan-enriched double:
\[
  G_{\sigma,S}^{\mathrm{Hall}}(X)
  :=
  D_{\sigma,S}\!\left(
    \widehat{Y^+_{\sigma,S}}(X),
    Y^0_\sigma(X),
    \langle-,-\rangle_{\sigma,S}
  \right)
  =
  \widehat{Y^-_{\sigma,S}}(X)\,\widehat{\bowtie}\,
  Y^0_\sigma(X)\,\widehat{\bowtie}\,
  \widehat{Y^+_{\sigma,S}}(X),
\]
where \(S\subset \mathbb C\) is a strict central-charge sector,
\(\widehat{Y^\pm_{\sigma,S}}\) are charge-sector completions, \(Y^0\)
is specified independently, and \(\langle-,-\rangle_{\sigma,S}\) is a
non-degenerate continuous Hopf pairing.  Without these hypotheses the
right hand side is at best notation.

Status by geometry:
- \(\mathbb C^3\): theorem-grade after completion:
  \[
    Y^+_\sigma(\mathbb C^3)=\CoHA(\mathbb C^3)
    =Y^+(\widehat{\mathfrak{gl}}_1),\qquad
    D(Y^+)=Y(\widehat{\mathfrak{gl}}_1).
  \]
  The \(\mathcal W_{1+\infty}\) object is reached only by an evaluation
  representation of the full double.
- Conifold: positive half theorem-grade at the Klebanov--Witten
  super-shuffle level; full quasi-triangular object is the Drinfeld
  double after the \(\mathbb Z_2\)-graded Hopf pairing:
  \[
    Y^+=\CoHA(Q_{\mathrm{con}},W_{\mathrm{con}})
    \simeq
    Y^+(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}},
    \qquad
    D(Y^+)=Y(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}.
  \]
- Exotic toric / compact-4-cycle toric: conditional.  The positive
  CoHA may exist, but the non-degenerate Hopf pairing, completion, and
  named Yangian identification must be proved separately.
- \(K3\times E\): character theorem-grade, algebra comparison
  conditional.  The equality
  \[
    \chi_{\mathrm{gr}}(\CoHA_{K3\times E})=\frac{1}{\Phi_{10}(\Omega)}
  \]
  does not construct the Hall pairing, negative half, Cartan, or full
  double.  The expected comparison
  \[
    \CoHA(K3\times E)\simeq
    U\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)_{\mathrm{num}},
    \qquad
    D\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)
    =
    U_q(\mathfrak g_{\Delta_5})^{\mathrm{Hall}}
  \]
  remains conditional on the motivic Hall lift, Hall--BKM positive-half
  comparison, and framed CY-C comparison.

## Healed Conditional Theorem

Let \(\mathcal C\) be a CY\(_3\) category with support \(X\), numerical
charge lattice \(\Gamma_X\), stability chamber \(\sigma\), orientation
data, and oriented critical semistable stacks
\(\mathcal M_\sigma(\gamma)\).  Fix a strict sector \(S\) in the
central-charge plane and set
\[
  \widehat{Y^+_{\sigma,S}}(X)
  =
  \prod_{\gamma\in \Gamma_{\mathrm{eff},\sigma}\cap S}
  H^\bullet_{\mathrm{eq}}\bigl(\mathcal M_\sigma(\gamma),\phi_W\bigr).
  \tag{1}
\]
Assume:

1. the Hall product and continuous coproduct make
   \(\widehat{Y^+_{\sigma,S}}\) a complete topological Hopf algebra, or
   a connected topological bialgebra with a proved continuous antipode;
2. Davison--Meinhardt PBW integrality holds in this sector;
3. the Serre-dual opposite half
   \[
     \widehat{Y^-_{\sigma,S}}(X)
     \simeq
     \widehat{Y^+_{\sigma,S}}(X)^{\vee,\mathrm{op}}
   \]
   is constructed as the opposite Hall algebra;
4. the continuous Hall pairing
   \[
     \langle \alpha,\beta\rangle_{\sigma,\gamma}
     =
     \int_{\mathcal M_\sigma(\gamma)}
       \alpha\cup \mathbb D_{\mathrm{Serre}}(\beta)\cap \phi_W
     \in k((\hbar))
     \tag{2}
   \]
   is non-degenerate after quotienting any radical and completing;
5. the Cartan half is fixed as the completed twisted group algebra
   \[
     Y^0_\sigma(X)=k((\hbar))[[\Gamma_X]]_\chi,\qquad
     K_\gamma K_\delta
     =
     (-\mathbb L^{1/2})^{\langle\gamma,\delta\rangle}
     K_{\gamma+\delta},
     \tag{3}
   \]
   acting by
   \[
     K_\gamma\, y_\delta\, K_\gamma^{-1}
     =
     q^{\langle\gamma,\delta\rangle} y_\delta .
     \tag{4}
   \]

Then the chambered BPS quantum group is the completed Hall--Drinfeld
double
\[
  G_{\sigma,S}^{\mathrm{Hall}}(X)
  =
  \widehat{Y^-_{\sigma,S}}(X)
  \widehat{\bowtie}
  Y^0_\sigma(X)
  \widehat{\bowtie}
  \widehat{Y^+_{\sigma,S}}(X),
  \tag{5}
\]
with cross-relations determined by (2).  In the convention where
\(\Delta^2(a)=a_{(1)}\otimes a_{(2)}\otimes a_{(3)}\) for
\(a\in Y^+\) and \(\Delta^2(b)=b_{(1)}\otimes b_{(2)}\otimes b_{(3)}\)
for \(b\in Y^-\),
\[
  b\,a
  =
  \sum
  \langle a_{(1)},b_{(1)}\rangle\,
  a_{(2)} b_{(2)}\,
  \langle a_{(3)},S^{-1}b_{(3)}\rangle .
  \tag{6}
\]
The universal \(R\)-matrix and quasi-triangularity live on (5), not on
\(Y^+\) alone.

## Attack/Heal Cycles

### 1. Non-degenerate Hall pairing

ATTACK.  \(Y^+_\sigma(X)\) is an associative Hall algebra.  A Drinfeld
double needs a non-degenerate Hopf pairing between positive and
negative halves.  Character identities and PBW integrality do not
produce such a pairing.  At root of unity or after numerical
specialisation, radicals can appear.

HEAL.  State non-degeneracy as a hypothesis and quotient by the radical
before doubling.  Formula (2) is the required pairing.  It is
theorem-grade for \(\mathbb C^3\); proved or locally verified for the
conifold super-Hopf presentation under the cited KW pairing; conditional
for exotic toric compact-4-cycle cases and \(K3\times E\).

Manuscript recommendation.  In
`coha_wall_crossing_platonic.tex:1419--1432`, replace "the abstract
double is always available" by "the formal tensor product is available;
the Drinfeld double is available only after a continuous non-degenerate
Hopf pairing, or after quotienting its radical."

### 2. Completion and local finiteness

ATTACK.  The BPS charge monoid is usually infinite.  Products in
wall-crossing and Hall integration are completed sector products, not
ordinary tensor products.  The formula \(D(Y^+_\sigma(X))\) suppresses
the completion and can be undefined.

HEAL.  Work in a strict sector \(S\) and use (1).  Wall-crossing then
acts by continuous automorphisms of completed quantum tori.  The full
object is a pro-object or sectorial local system, not a single algebra
unless sector gluing is proved.

Example check.  For \(\mathbb C^3\), completion is the plane-partition
/ MacMahon completion.  For \(K3\times E\), the infinite product
\(1/\Phi_{10}\) is character-level evidence for the completion, not a
construction of the completed algebra.

### 3. Cartan half is independent data

ATTACK.  \(D(Y^+)\) does not determine the Cartan half.  The Cartan is
rank \(1\) for \(\mathbb C^3\), rank \(2\) for the conifold, rank
\(\#Q_0\) for toric quivers, and imaginary rank \(23\) in the
\(K3\times E\) Hall--BKM picture.  Omitting \(Y^0\) collapses distinct
Manin data.

HEAL.  Use the enriched notation
\[
  D_{\sigma,S}\bigl(Y^+;Y^0,\langle-,-\rangle\bigr),
  \qquad
  Y^0=k((\hbar))[[\Gamma_X]]_\chi .
  \tag{7}
\]
For the conifold, retain the two-dimensional imaginary-root Cartan
\(\mathrm{span}(H_n,K_n)\) before any supertrace projection.  For
\(K3\times E\), do not replace the imaginary rank-\(23\) Cartan by a
toric charge lattice.

Manuscript recommendation.  In `toric_cy3_coha.tex:1687--1696`, append
"after choosing the Cartan twisted group algebra of the charge lattice"
to the Drinfeld-double component.  In \(K3\times E\) passages, keep the
rank-\(23\) imaginary Cartan explicit.

### 4. Negative half is not automatic

ATTACK.  The notation \(D(Y^+)\) silently identifies the graded dual of
the positive half with the negative half.  This fails unless the
opposite chamber/quiver, Serre duality, orientation data, and completed
graded dual all agree.

HEAL.  Require
\[
  Y^-_{\sigma,S}(X)
  =
  \bigl(Y^+_{\sigma,S}(X)\bigr)^{\vee,\mathrm{op}}
  \tag{8}
\]
as a theorem or hypothesis.  For \(\mathbb C^3\), this is the opposite
affine-Yangian Borel.  For the conifold, it is the opposite
Klebanov--Witten super-shuffle with the \(\mathbb Z_2\)-graded pairing.
For \(K3\times E\), the negative BKM cone is part of the conditional
Hall--BKM comparison, not a consequence of the DT character.

### 5. Topological bialgebra versus Hopf algebra

ATTACK.  A CoHA naturally has Hall multiplication.  Coproducts are often
coideal, localization, or topological coproducts.  A Drinfeld double in
the strict sense needs a Hopf algebra, or a specified weak/multiplier
substitute.  The \(R\)-matrix is not present on the positive half.

HEAL.  State the exact ambient structure.  For conifold:
\[
  \Delta(e^{(a)}(u))
  =
  e^{(a)}(u)\otimes 1
  +
  \psi^{(a)}(u)\otimes e^{(a)}(u),
  \tag{9}
\]
and connected super-bialgebra hypotheses give an antipode.  The
quasi-triangular structure appears only on
\[
  D(Y^+)=Y(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}.
  \tag{10}
\]
For general toric cases, say "coideal topological bialgebra" until the
Hopf upgrade is proved.

Manuscript recommendation.  Preserve the reconciliation ledger at
`coha_wall_crossing_platonic.tex:1460--1475`, and propagate its
"coideal-topological, not strict Hopf" reading back into
`toric_cy3_coha.tex:1650--1657`.

### 6. \(E_1\) versus \(E_2\)

ATTACK.  \(Y^+_\sigma(X)\) is an associative \(E_1\) Hall algebra.  The
full double is still algebraic/Hopf data.  The braided \(E_2\) structure
belongs to the Drinfeld centre of the \(E_1\)-representation category,
not to the positive half and not to the \(d=3\) chiral algebra itself.

HEAL.  The representation-level formula is
\[
  \mathcal Z\bigl(\Rep^{E_1}(Y^+_\sigma(X))\bigr)
  \simeq
  \Rep^{E_2}\bigl(G_{\sigma,S}^{\mathrm{Hall}}(X)\bigr),
  \tag{11}
\]
only where the centre comparison is proved.  For \(\mathbb C^3\) this
is the complete local case.  For general toric and \(K3\times E\), it
is CY-C input.

Manuscript recommendation.  In `quantum_groups_foundations.tex:96--124`
keep the theorem about the double conditional, and avoid wording that
identifies the double with the \(\Phi_3\) output.  The \(\Phi_3\) output
at \(d=3\) is \(E_1\)-chiral; \(E_2\) enters through (11).

### 7. Chamber dependence and wall-crossing

ATTACK.  The subscript \(\sigma\) matters.  Wall-crossing changes the
positive cone and the presentation.  A single equality
\(G(X)=D(Y^+(X))\) suppresses the KS gauge transformations.

HEAL.  Treat \(\{G_{\sigma,S}^{\mathrm{Hall}}(X)\}_\sigma\) as a
local system/groupoid over chambers.  Across a wall \(W\),
\[
  Y^+_{\sigma'}(X)=\mathrm{KS}_W\,Y^+_\sigma(X)\,\mathrm{KS}_W^{-1},
  \qquad
  R^{\sigma'}(u)
  =
  F_{\sigma\sigma'}\,R^\sigma(u)\,F_{\sigma\sigma'}^{-1}.
  \tag{12}
\]
The double is chamber-invariant only up to this gauge equivalence.

Manuscript recommendation.  `coha_wall_crossing_platonic.tex:1729--1819`
already has the right chamber-adapted statement for the K3 route.  The
universal positive-geometry theorem should cite that model and not
suggest chamber-independent equality before gauge descent.

## Exact Example Data

### \(\mathbb C^3\)

\[
  \CoHA(\mathbb C^3)
  =
  Y^+(\widehat{\mathfrak{gl}}_1),
  \qquad
  D(Y^+(\widehat{\mathfrak{gl}}_1))
  =
  Y(\widehat{\mathfrak{gl}}_1)
  =
  Y^-\otimes Y^0\otimes Y^+.
  \tag{13}
\]
The Schiffmann--Vasserot shuffle kernel is
\[
 \phi_{\mathrm{SV}}(u,v)=
 \frac{(u-v+\epsilon_1)(u-v+\epsilon_2)(u-v+\epsilon_3)}
 {(u-v)(u-v+\epsilon_1+\epsilon_2)(u-v+\epsilon_2+\epsilon_3)},
 \qquad
 \epsilon_1+\epsilon_2+\epsilon_3=0.
 \tag{14}
\]
The MO residue is
\[
  R^{\mathrm{MO}}(u)=\operatorname{Res}_{u=u_*}\phi^+_{\mathrm{UV}}(u).
  \tag{15}
\]
Do not identify \(Y^+\) with \(\mathcal W_{1+\infty}\).  The correct
chain is
\[
  \CoHA(\mathbb C^3)=Y^+
  \hookrightarrow
  Y(\widehat{\mathfrak{gl}}_1)
  \xrightarrow{\mathrm{ev}_\lambda}
  \mathrm{End}\bigl(\mathcal W_{1+\infty}[\lambda]\text{-vac}\bigr).
  \tag{16}
\]

### Conifold

\[
  W_{\mathrm{con}}
  =
  \operatorname{tr}(a_1b_1a_2b_2-a_1b_2a_2b_1).
  \tag{17}
\]
\[
  \CoHA(Q_{\mathrm{con}},W_{\mathrm{con}})
  \simeq
  Y^+\bigl(\widehat{\mathfrak{gl}}(1|1)\bigr)^{\mathrm{con}}.
  \tag{18}
\]
The KW super-shuffle bond factors are
\[
 \varphi^{0\Rightarrow0}=\varphi^{1\Rightarrow1}=1,\qquad
 \varphi^{0\Rightarrow1}(u)
 =
 \frac{(u+h_1)(u+h_2)}{u(u+h_1+h_2)},\qquad
 \varphi^{1\Rightarrow0}(u)=\varphi^{0\Rightarrow1}(-u).
 \tag{19}
\]
The imaginary-root coefficient is
\[
  \mathbf c^{\mathrm{KW}}_{(1,1)}
  =
  \frac{1}{h_1h_2}
  =
  (\varepsilon_1\varepsilon_2)^{-1}.
  \tag{20}
\]
Status: positive half and conifold bialgebra are theorem-grade at the
local KW/shuffle scope.  The universal \(R\)-matrix and
quasi-triangularity are double-level statements, not positive-half
statements.

### Exotic Toric

For toric CY\(_3\) without compact \(4\)-cycles:
\[
  \CoHA(Q_X,W_X)\simeq Y^+(\widehat{\mathfrak g}_{Q_X})
  \tag{21}
\]
is the RSYZ positive-half theorem at its stated scope.  The manuscript
also discusses compact-base/local-surface examples such as local
\(\mathbb P^2\), where
\[
  \kappa_{\mathrm{ch}}(K_{\mathbb P^2})=\frac{3}{2}.
  \tag{22}
\]
For compact-4-cycle or exotic quiver cases, the double
\[
  D\bigl(\CoHA(Q_X,W_X)\bigr)=Y(\widehat{\mathfrak g}_{Q_X})
  \tag{23}
\]
must remain conditional until the topological Hopf pairing,
completion, and named-Yangian identification are proved.  Do not import
the \(\mathbb C^3\) pairing proof by analogy.

### \(K3\times E\)

The theorem-grade statement is character-level:
\[
  Z_{\mathrm{DT}}^{\mathrm{red},\prime}(K3\times E)
  =
  \frac{1}{\Phi_{10}(\Omega)},
  \qquad
  \chi_{\mathrm{gr}}(\CoHA_{K3\times E})
  =
  \frac{1}{\Phi_{10}(\Omega)}.
  \tag{24}
\]
The expected positive-half comparison is
\[
  \operatorname{Poinc}\bigl(\CoHA(K3\times E)\bigr)
  =
  \frac{1}{\Delta_5(Z)^2}
  =
  \frac{1}{\Delta_{10}(Z)},
  \tag{25}
\]
\[
  \CoHA(K3\times E)
  \simeq
  U\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)_{\mathrm{num}},
  \qquad
  \operatorname{Lie}\CoHA(K3\times E)
  =
  Y^+(\mathfrak g_{\Delta_5}).
  \tag{26}
\]
The expected full double is
\[
  D\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)
  =
  U_q(\mathfrak g_{\Delta_5})^{\mathrm{Hall}},
  \qquad
  \mathfrak g_{\Delta_5}
  =
  Y^-\oplus\mathfrak h\oplus Y^+.
  \tag{27}
\]
Status: (24) is theorem-grade as a reduced DT/character identity in
the manuscript.  (25)--(27) are conditional Hall--BKM/CY-C statements.
Generic \(K3\times E\) is not MO-accessible by a rank-\(\ge 2\)
algebraic torus; ADE/Kummer loci have separate restricted MO evidence.

## Manuscript Recommendations

1. Keep Theorem `thm:quantum-group-as-positive-geometry-double`
   conditional, but strengthen its hypotheses by naming sector
   completion, continuous Hopf pairing, Cartan half, negative half, and
   radical quotient.
2. Replace every bare global reading of \(D(Y^+_\sigma(X))\) by
   \(D_{\sigma,S}(Y^+;Y^0,\langle-,-\rangle)\) when the theorem needs
   the actual double rather than slogan notation.
3. In `coha_wall_crossing_platonic.tex:1419--1432`, repair "abstract
   double is always available"; a formal dual tensor product is
   available, but the Drinfeld double requires a non-degenerate pairing
   and compatible topological Hopf structure.
4. In `toric_cy3_coha.tex:1634--1815`, split component (III): proved
   for \(\mathbb C^3\); proved/locally verified for conifold under the
   KW super-Hopf pairing; RSYZ-scope for standard no-compact-4-cycle
   toric; conditional for exotic compact-4-cycle toric.
5. In `quantum_groups_foundations.tex:714--800`, soften
   representability prose: it is an accessible-locus conditional
   corepresentability theorem, not a global construction of \(G(X)\).
   The same paragraph should not list conifold/local \(\mathbb P^2\)
   as beyond reach without specifying "global \(E_2\) centre comparison"
   rather than "positive-half CoHA".
6. In the \(K3\times E\) sections, keep the hierarchy:
   reduced DT/Igusa character identity proved; CoHA-to-BKM positive
   half conditional; Hall pairing/double conditional; framed
   \(\Phi_3\) algebra comparison conditional.
7. Preserve the rule: CoHA is \(E_1\)-associative.  The \(E_2\) braided
   object is
   \(\mathcal Z(\Rep^{E_1}(-))\), not \(Y^+\), not the raw CoHA, and not
   the \(d=3\) chiral algebra itself.

## Open Proof Obligations

1. Prove or cite a non-degenerate continuous Hopf pairing for every
   toric/exotic class where the manuscript names a full Yangian.
2. Construct the sector completion and prove wall-crossing continuity
   for \(Y^+_{\sigma,S}(X)\) beyond standard toric loci.
3. Construct the negative half by Serre-dual opposite Hall algebra, not
   by formal naming.
4. For \(K3\times E\), upgrade the character identity to an algebra
   identification only after constructing the motivic Hall lift,
   Hall--BKM pairing, and imaginary Cartan action.
5. Prove the Drinfeld-centre comparison separately from the Hall double;
   the former is representation-categorical \(E_2\) data, the latter is
   algebraic/Hopf data.

