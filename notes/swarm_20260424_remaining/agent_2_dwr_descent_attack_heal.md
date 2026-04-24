# Agent 2 - DWR Descent Attack/Heal

Date: 2026-04-24.

Scope: residual obstruction \(o_\theta^{\mathrm{des}}\) in
`chapters/theory/cy3_chain_level_bridge.tex`, after the fixed abelian
\(\mathbb C^3\) hCS-to-Hall shuffle chart.  I did not edit the chapter.

## Verdict

The fixed abelian chart kills exactly
\[
  o_\theta^{\mathrm{fp},+}=0.
\]
It does not kill \(o_\theta^{\mathrm{ren}}\), and it does not kill
\(o_\theta^{\mathrm{des}}\).  A chartwise formula on \(\mathbb C^3\),
even the correct Schiffmann--Vasserot positive-half formula
\(\CoHA(\mathbb C^3)=Y^+\), is not a DWR descent datum.  The descent
problem starts only after full renormalised chart maps exist on the
objects of the chosen Dolbeault--Weiss--Ran nerve.

The strongest truthful theorem package is therefore conditional:
given a finite DWR-good cover, full renormalised hCS-to-Hall maps on
every relevant Cech/Ran simplex, and nullhomotopies for the five
obstruction components
\[
  (o_{\mathrm{MC}},o_{\mathrm{or}},o_{\mathrm{gr}},
    o_{\mathrm{TS}},o_{\mathrm{fact}}),
\]
Theorem `thm:hcs-hall-descent-criterion` gives the global
orientation-preserving morphism.  No shortcut from the fixed local
chart, Hall-side orientation, Hall-side Thom--Sebastiani associativity,
or \(\mathcal W_{1+\infty}\) character shadow supplies those data.

## Attacks

### 1. Overlap naturality

Attack: a family of maps \(\theta_i\) on charts \(U_i\simeq\mathbb C^3\)
does not define maps on \(U_{i_0}\cap\cdots\cap U_{i_p}\), nor does it
commute with face, degeneracy, or refinement maps.

Required healing datum: for every non-empty Cech/Ran simplex
\(\sigma\), a continuous degree-zero map
\[
  \Theta_\sigma:
  \Obs_{\hCS}^{q}(|\sigma|,\mathfrak g)\to
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(|\sigma|)
\]
compatible with all faces, degeneracies, refinements, and compact-support
extensions.

### 2. Cech/Ran Maurer--Cartan curvature

Attack: vertex quasi-isomorphisms do not solve the total Cech
Maurer--Cartan equation.  The Cech differential records overlap failure;
the convolution bracket records product failure.

Required healing datum:
\[
  \mathfrak M_{\hCS,\Hall}(\mathfrak U)
  =
  \Tot\,\Cech^\bullet(\mathfrak U,\mathcal M^\bullet),
  \qquad
  \mathcal M^q(U_I)=
  \Hom_{\mathrm{cont}}^q(\Obs_{\hCS}^q(U_I),\CoHA_{\mathrm{crit}}^{\mathrm{or}}(U_I)),
\]
completed in the \(\hbar\)-adic, strong-dual, charge/HN-adic, and
equivariant-localised topologies, together with
\[
  d\Theta+\frac12[\Theta,\Theta]=0.
\]
In the chapter convention the curvature class is
\[
  o_{\mathrm{MC}}\in H^1(\mathfrak M_{\hCS,\Hall}(\mathfrak U)).
\]
After shifting the deformation complex by one, the same obstruction is
the familiar \(H^2\) deformation class.

### 3. Orientation

Attack: a Hall-side KS/Joyce orientation trivialisation is not the
relative hCS-to-Hall orientation comparison.  It prepares the target; it
does not transport source and target determinant data through \(\Theta\).

Required healing datum: edge transports of determinant-line square
roots and orientation local systems, compatible with direct sums,
extensions, and restrictions.  On triple overlaps the residual
\(\mathbb Z/2\) cocycle must be explicitly nullhomotoped.  The gate is
\[
  o_{\mathrm{or}}=0,
\]
not merely "the Hall orientation torsor is trivial."

### 4. Grading and Tate twist

Attack: the fixed local functions \(s(U,\mathbf d)\) and
\(t(U,\mathbf d)\) on \(\mathbb C^3\) do not prove that the comparison is
degree-zero on all overlaps.  Coordinate changes and equivariant
localisations can shift conventions.

Required healing datum: a global convention for
\((s,t)\colon\mathsf{N}_{\mathsf{DWR}}(\mathfrak U)\times\Gamma\to
\mathbb Z\times\mathbb Z\) preserved by all restriction and refinement
maps, and by \(\Theta_\sigma\).  The gate is
\[
  o_{\mathrm{gr}}=0.
\]

### 5. Thom--Sebastiani coherence

Attack: strict associativity of Hall convolution on the CY locus is not
the comparison theorem.  The comparison must identify the two Hall
Thom--Sebastiani parenthesisations with the two hCS factorisation
products, including signs, Tate twists, and transported orientation
lines.

Required healing datum: coherent TS isomorphisms for every iterated
short-exact-sequence correspondence in the finite DWR/Ran truncation,
with the pentagon/associator defect killed:
\[
  o_{\mathrm{TS}}=0.
\]

### 6. Factorisation compatibility

Attack: multiplicativity on one affine chart does not imply disjoint
Ran multiplicativity.  Descent requires compatibility for disjoint
families of polydiscs and their refinements.

Required healing datum: for disjoint \(\sigma_1,\sigma_2\), the product
square
\[
  \Theta_{\sigma_1\sqcup\sigma_2}\circ\mu_{\BV}^{\mathrm{fact}}
  =
  \mu_{\Hall}^{\mathrm{TS},o}\circ
  (\Theta_{\sigma_1}\widehat\otimes\Theta_{\sigma_2})
\]
in completed complexes.  The gate is
\[
  o_{\mathrm{fact}}=0.
\]

### 7. Completion and continuity

Attack: algebraic shuffle multiplication is finite-mode.  The global
comparison lives in completed topological complexes.  HN/charge
completion, equivariant localisation, continuous duals, and
\(\hbar\)-adic completion must be compared before descent is typed.

Required healing datum: every \(\Theta_\sigma\) is continuous for the
four named topologies and commutes with completion before taking
homotopy colimits.

### 8. Fixed chart, positive half, and \(\mathcal W_{1+\infty}\)

Attack: \(\CoHA(\mathbb C^3)=Y^+\) does not imply
\(\CoHA(\mathbb C^3)=\mathcal W_{1+\infty}\), and neither statement is a
DWR descent proof.  The \(\mathcal W_{1+\infty}\) object appears only
after
\[
  Y^+\to \mathcal D(Y^+)\to \mathcal W_{1+\infty}
\]
and a Fock/evaluation representation.

Required healing datum: keep the descent theorem separate from the
double/Fock shadow.  The latter is a typed representation-theoretic
passage, not a replacement for \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\).

## Healed Theorem Package

### Definition: finite DWR descent gate

Fix a finite DWR-good cover \(\mathfrak U\), a finite charge bound
\(\Gamma_{\leq N}\), and a finite Ran arity bound \(r\).  The finite
descent gate consists of:

1. a refinement-closed DWR/Ran nerve in the chosen bounds;
2. full renormalised chart maps on every simplex, not only the fixed
   \(\mathbb C^3\) finite-mode projection;
3. a complete filtered total Cech/Ran convolution dg Lie algebra
   \(\mathfrak M_{\hCS,\Hall}^{\leq N,\leq r}(\mathfrak U)\);
4. a degree-zero element \(\Theta\) satisfying the Maurer--Cartan
   equation;
5. vertex quasi-isomorphisms and \(H^0\)-invertibility on every object
   of the finite nerve;
6. vanishing relative orientation, grading/Tate,
   Thom--Sebastiani, and disjoint-union factorisation classes;
7. continuity for all completions and compact-support refinement maps.

The unbounded theorem is the inverse limit over \(N,r\) after the
completion maps are proved continuous and Mittag--Leffler/exact enough
for the chosen homotopy limit.

### Theorem: conditional finite descent

Let the finite DWR descent gate vanish in the sense above.  Then the
simplexwise maps \(\Theta_\sigma\) define a morphism
\[
  \Theta_{\hCS\to\Hall}^{\mathrm{or},\leq N,\leq r}:
  \Obs_{\hCS}^{q}(-,\mathfrak g)_{\leq N,\leq r}
  \to
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)_{\leq N,\leq r}
\]
in the completed Hall-valued factorisation-cosheaf category on that
finite nerve.  If the vertex maps are quasi-isomorphisms and
\(H^0\)-invertible throughout the nerve, the induced map on finite
DWR/Ran descent is a quasi-isomorphism.

Proof: this is exactly Theorem `thm:hcs-hall-descent-criterion` applied
to the finite completed total Cech/Ran dg Lie algebra.  The five
obstruction components are the five forgotten structures of a morphism
in `def:hall-valued-factorisation-cosheaf-target`.  Their nullhomotopies
restore naturality, orientation, degree, TS associativity, and disjoint
Ran multiplicativity.  Homotopy colimits over a finite nerve preserve
the resulting quasi-isomorphisms.

### Corollary: fixed chart residual

The fixed abelian \(\mathbb C^3\) chart supplies one input to the finite
gate only after it has been extended to the full renormalised chart
complex.  Before that extension, it proves only
\[
  o_\theta^{\mathrm{fp},+}=0.
\]
The residual \(o_\theta^{\mathrm{des}}\) is the conjunction of:
all-simplex maps, Cech/Ran Maurer--Cartan vanishing, relative
orientation, grading/Tate, Thom--Sebastiani, factorisation, completion,
and compact-support refinement compatibility.

## Minimal Compute Witness

I added `compute/lib/cy3_dwr_descent_gate.py` and
`compute/tests/test_cy3_dwr_descent_gate.py`.

The witness records the finite gate implication lattice:

- all required DWR descent gates imply descent;
- deleting any single required gate prevents descent;
- the fixed \(\mathbb C^3\) chart does not imply descent;
- vertex quasi-isomorphisms without all-simplex maps and MC vanishing do
  not descend;
- Hall-side orientation triviality does not imply relative orientation;
- Hall-side TS associativity does not imply comparison TS coherence;
- \(\CoHA(\mathbb C^3)=Y^+\) does not give a direct
  \(\mathcal W_{1+\infty}\) shortcut.

This is an executable sanity check for integration.  It is not a proof
of \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\).

## Integration Recommendation

Integrate the theorem package only as a conditional descent criterion.
Do not inscribe "DWR descent solved" unless the integration agent has
actual simplexwise maps and nullhomotopies for all five obstruction
components.  The chapter can safely say:

1. `thm:c3-fixed-abelian-chart-map` kills \(o_\theta^{\mathrm{fp},+}\);
2. \(o_\theta^{\mathrm{ren}}\) remains the full renormalised extension;
3. \(o_\theta^{\mathrm{des}}\) is killed exactly by the finite DWR gate
   above, then by the completed inverse-limit theorem if the topology
   hypotheses are proved;
4. the \(\mathcal W_{1+\infty}\) passage remains only
   \(Y^+\to\mathcal D(Y^+)\to\) Fock/evaluation, never a direct CoHA
   identification.
