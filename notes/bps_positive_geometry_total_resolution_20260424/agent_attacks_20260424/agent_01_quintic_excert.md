# Agent 01 -- Quintic ExCert adversarial report

## claim attacked

The attacked claim is the quintic lane of the chambered BPS positive
geometry closure:

1. The manuscript proposition says that, for the quintic threefold
   \(X_5\subset \mathbb P^4\), the named-example theorem is the
   certificate
   \[
   \operatorname{ExCert}(X_5;\sigma,Q,S,o,T_{\mathrm{eq}},\Mot),
   \]
   and that this is equivalent to supplying actual
   Bridgeland/support/HN data compatible with PTVV and orientation.

2. The derived-zero-locus theorem says that the quintic residual problem
   is the equation \(o_{\mathrm{Ex}}=0\) inside the residual solution
   stack \(\Sol^{\BPS}\).

3. The executable oracle constructs a `quintic_excert` factor whose
   certificate is non-exact, but whose obstruction vector is nevertheless
   set to zero, and then reports the aggregate
   `derived_solution_stack_certificate` as exact.

## strongest failure mode

The strongest attack is not that the manuscript lacks a definition.
The manuscript definition is sharp enough: it says the quintic object is
an `ExCert`, not an already-realized chamber. The strongest failure is
that the executable model can turn a missing witness into a zero
coordinate.

Concretely, `quintic_excert_surface_certificate()` explicitly states
that the quintic certificate is not an unconditional realization:
the Bridgeland/support/HN slot remains a named input. Yet
`derived_solution_stack_factors()` installs

```text
names=("sigma_support_HN", "orientation_output", "motivic_target")
values=(0, 0, 0)
```

for the quintic factor. Since `SolutionStackFactor.solved` only tests
`certificate.passed and obstruction.vanishes`, the quintic factor is
formally solved even though its certificate has `exact=False`.

This is a real semantic bug. The absence of a discrepancy is being used
as if it were the presence of a point.

The mathematical obstruction is classical and local in the repository:
PTVV supplies the shifted symplectic form on \(\Perf(X_5)\), and HKR
supplies the Hochschild dimension vector
\((1,0,101,4,101,0,1)\), total \(208\). These are necessary surfaces of
the problem. They do not construct a Bridgeland stability condition on
\(D^b\mathrm{Coh}(X_5)\), a support quadratic form, an HN sector atlas,
or the required compact Hall orientation/motivic package.

The nearby false theorem to keep out of the closure is the older
large-volume chart assertion that
\(\oplus_{i=0}^4\mathcal O_{X_5}(i)\) is a tilting generator and that
the quintic hocolim has no obstruction. That story collides with the
newer compact CY3 obstruction surface: the large-volume chart has
Serre-dual higher Ext and cannot supply the strict toric-style tilting
input.

## fatal/nonfatal verdict

Verdict: fatal for the executable "exact derived solution stack"
interpretation; nonfatal for the manuscript theorem if read literally.

Nonfatal component. The manuscript proposition is mathematically honest
at the quintic line. It says that the exact theorem is
`ExCert`, and the proof explicitly says that PTVV and HKR do not by
themselves construct a Bridgeland chamber.

Fatal component. The executable aggregate is too strong as presently
typed. A non-exact certificate with a manually zeroed obstruction vector
is not an exact point-construction. The aggregate certificate cannot
have `exact=True` for all residual factors while the quintic factor has
`exact=False`. The correct exact object is a derived fiber over the
space of supplied witnesses, not an oracle point with zero coordinates
inserted before those witnesses exist.

## exact repair/heal theorem statement

The healed theorem should be strictly stronger because it separates the
geometry of the solution stack from the existence of a point.

**Theorem (quintic ExCert as a witness-fiber, exact form).**
Let \(X_5\subset \mathbb P^4\) be a smooth quintic threefold. Let
\(\mathfrak W_{X_5,\le N,\le R}\) be the finite witness functor whose
points are tuples
\[
(\sigma,Q,S,o,T_{\mathrm{eq}},\Mot,\mathcal A_{\HN})
\]
where:

1. \(\sigma=(Z,\mathcal P)\) is a Bridgeland stability condition on
   \(D^b\mathrm{Coh}(X_5)\);
2. \(Q\) is a support form for \(\sigma\);
3. \(S\) is a strict sector with no active boundary ray;
4. \(\mathcal A_{\HN}\) is the finite HN sector atlas on
   \(\Gamma_{S,\le N,\le R}\);
5. \(o\) is orientation output for the \((-1)\)-shifted critical Hall
   atlas induced from the PTVV \((-3)\)-shifted symplectic stack
   \(\Perf(X_5)\);
6. \(T_{\mathrm{eq}}\) and \(\Mot\) preserve the above finite Hall
   correspondences and vanishing-cycle Thom--Sebastiani products.

Then the finite quintic chambered BPS positive geometry is represented
by the derived zero fiber
\[
\operatorname{ExCert}_{X_5,\le N,\le R}
=
\mathfrak W_{X_5,\le N,\le R}
\times^h_{V_{\mathrm{Ex}}}\{0\}.
\]
For every field \(k\), the \(k\)-points of this derived fiber are
exactly the realized quintic chamber data over the retained charge set.
PTVV and HKR define canonical maps into the witness functor but do not
define a \(k\)-point of it. Therefore:

\[
\operatorname{ExCert}_{X_5,\le N,\le R}(k)\neq\varnothing
\quad\Longleftrightarrow\quad
\text{the quintic Bridgeland/support/HN/orientation/motivic witness exists.}
\]

The derived solution stack may contain the BMS compact non-toric point
unconditionally, but the quintic substack contains a point only after
the witness above is supplied. In executable terms, the exact solved
predicate for a factor must require

```text
certificate.exact and certificate.passed and obstruction.vanishes
```

or else must distinguish "formal zero fiber defined" from "point
constructed".

## local file anchors

- `chapters/theory/bps_positive_geometry_closure.tex:223`:
  the quintic theorem is phrased as `ExCert`.
- `chapters/theory/bps_positive_geometry_closure.tex:243`:
  PTVV and HKR are explicitly said not to construct a Bridgeland chamber.
- `chapters/theory/bps_positive_geometry_closure.tex:520`:
  the residual stack is defined as a derived zero fiber.
- `chapters/theory/bps_positive_geometry_closure.tex:547`:
  the quintic equation is \(o_{\mathrm{Ex}}=0\).
- `chapters/theory/bps_positive_geometry_closure.tex:556`:
  only the BMS class is asserted to give an actual point; quintic is a
  closed substack whose point-construction remains the named problem.
- `compute/lib/bps_positive_truncation.py:647`:
  `quintic_excert_surface_certificate()` correctly sets `exact=False`.
- `compute/lib/bps_positive_truncation.py:650`:
  the docstring says the certificate is not an unconditional
  realization.
- `compute/lib/bps_positive_truncation.py:841`:
  the executable factor installs zero values for the quintic witness
  coordinates.
- `compute/lib/bps_positive_truncation.py:291`:
  `SolutionStackFactor.solved` ignores the `exact` flag.
- `compute/lib/bps_positive_truncation.py:897`:
  the aggregate `derived_solution_stack_certificate()` returns
  `exact=True`.
- `compute/tests/test_bps_positive_truncation.py:198`:
  the test correctly asserts the quintic certificate is not exact.
- `compute/tests/test_bps_positive_truncation.py:292`:
  the derived-stack test asserts all obstruction vectors vanish,
  including the quintic vector.
- `compute/tests/test_bps_positive_truncation.py:307`:
  the aggregate derived-stack test asserts `certificate.exact`.
- `compute/lib/compact_geometric_koszul_d3.py:279`:
  HKR matching is proved as a necessary condition only.
- `compute/lib/compact_geometric_koszul_d3.py:375`:
  HKR matching implies Koszul duality is refuted.
- `compute/lib/compact_geometric_koszul_d3.py:430`:
  all three candidate tilting/Bridgeland routes remain open.
- `compute/lib/A_BVDB_quintic_formality.py:322`:
  the \(m_3\) obstruction is the Yukawa coupling.
- `compute/lib/A_BVDB_quintic_formality.py:439`:
  strict formality of the BVDB algebra is false.
- `compute/lib/quintic_chart_gluing.py:947`:
  an older hocolim construction claims the quintic \(E_1\) algebra is
  well-defined.
- `compute/lib/quintic_chart_gluing.py:1448`:
  an older tilting-generator function asserts that
  \(\oplus_{i=0}^4\mathcal O_{X_5}(i)\) is tilting.
- `chapters/theory/cy_to_chiral.tex:6860`:
  the current cross-chapter statement says the large-volume quintic chart
  has no tilting generator and the explicit model remains conditional.

## primary/literature anchors if needed from existing bibliography or local notes

- `bibliography/references.tex:342`: PTVV 2013, shifted symplectic
  structures. Used only for the \((-3)\)-shifted symplectic structure on
  \(\Perf(X_5)\), not for Bridgeland stability.
- `bibliography/references.tex:375`: Caldararu 2003, Mukai pairing/HKR
  source used in the local HKR dimension computation.
- `bibliography/references.tex:357`: Voisin Hodge theory source for the
  quintic Hodge diamond.
- `bibliography/references.tex:683`: Bridgeland 2007, definition and
  general theory of stability conditions; it does not construct
  \(\Stab(D^b\mathrm{Coh}(X_5))\).
- `bibliography/references.tex:354`: Bayer--Macri--Toda 2014,
  threefold tilt-stability/BMT framework; local sources record that the
  compact quintic case is not uniformly closed.
- `bibliography/references.tex:391`: Bayer--Macri--Stellari 2016,
  existence for abelian threefolds and some CY3 quotient examples; this
  supplies the non-toric compact point used in the closure, not a quintic
  point.
- `bibliography/references.tex:245`: Sheridan 2015, HMS for compact
  CY hypersurfaces; the local obstruction file correctly records that
  HMS does not preserve the Kapranov property needed for this ExCert.

## executable checks proposed or run

Run:

```text
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_quintic_excert_surface_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_certificate
```

Result:

```text
3 passed
```

Direct probe run:

```text
quintic_cert_passed True
quintic_cert_exact False
hkr_match True [1, 0, 101, 4, 101, 0, 1]
ptvv_exists True
hkr_implies_koszul False
strict_formality False
torus_action_applicable False
route_BCOV OPEN
route_LG_mirror OPEN
route_Bridgeland_stability OPEN
derived_factor quintic_excert
certificate_passed True
certificate_exact False
obstruction_vanishes True
obstruction_names ('sigma_support_HN', 'orientation_output', 'motivic_target')
obstruction_values ['0', '0', '0']
```

The first direct probe initially used a wrong constructor keyword for
`TruncationBound`; rerun with `R_num=5` produced the displayed derived
factor output.

Proposed falsifying tests:

```python
def test_quintic_factor_is_not_solved_without_exact_certificate():
    factors = derived_solution_stack_factors(_bound())
    q = next(f for f in factors if f.name == "quintic_excert")
    assert q.certificate.passed
    assert not q.certificate.exact
    assert not q.solved


def test_derived_solution_stack_exactness_propagates_factor_exactness():
    certificate = derived_solution_stack_certificate(_bound())
    assert not certificate.exact
```

These tests should fail against the present oracle, which is precisely
the point: they force the executable layer to distinguish "zero fiber
defined" from "quintic point constructed".

## remaining point-construction obligation

The remaining quintic obligation is not to recompute PTVV, HKR, the
Hodge vector, or the Yukawa obstruction. Those are already sharp. The
remaining point-construction obligation is:

Construct a genuine tuple
\[
(\sigma,Q,S,o,T_{\mathrm{eq}},\Mot,\mathcal A_{\HN})
\]
on \(D^b\mathrm{Coh}(X_5)\) satisfying the support property, finite HN
sector descent on \(\Gamma_{S,\le N,\le R}\), compatibility with the
PTVV critical Hall atlas, orientation output, and motivic vanishing-cycle
Thom--Sebastiani product.

The strongest current route is not strict toric tilting. That route is
blocked by Serre-dual higher Ext, non-formality, and the Yukawa
\(m_3\) obstruction. The stronger surviving route is a curved
BCOV/Bridgeland witness:

1. construct or import a Bridgeland stability condition on
   \(D^b\mathrm{Coh}(X_5)\);
2. prove the support property for the retained charge lattice;
3. construct finite HN Hall atlases in strict sectors;
4. build orientation output for the \((-1)\)-shifted critical Hall
   atlas induced by PTVV;
5. express the non-formal Yukawa \(m_3\) as the BCOV curving rather than
   trying to erase it by strict formality;
6. prove the compact Hall pull-push and motivic realization maps commute
   with this curved witness.

Only after these six items are supplied may the executable quintic
coordinates be set to zero as values of a constructed point rather than
as placeholders.
