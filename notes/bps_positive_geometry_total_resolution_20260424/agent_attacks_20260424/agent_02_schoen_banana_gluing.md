# Agent 02: Schoen/Banana Compact Hall Gluing Attack

## Claim attacked

The current platonic-ideal resolution claims that the Schoen/banana
remaining problem is completely captured by the derived zero-fiber
coordinate

```tex
X_{\mathrm{Sch}} \quad \Longleftrightarrow \quad o_{\mathrm{glue}}=0,
```

with the local banana calculation supplying

```tex
S_4^{\mathrm{inst}}=-44,\qquad r_{\max}=-1.
```

The attacked claim is not the finite-first Hall-cosheaf framework.  The
attacked claim is the stronger reading that this zero-fiber treatment is
already a complete compact Schoen point construction.

## Strongest failure mode

The strongest failure is that the executable solution-stack factor marks
the Schoen/banana lane solved while its own certificate says the lane is
not exact.

Observed executable state:

```text
schoen_banana_gluing_certificate().passed = True
schoen_banana_gluing_certificate().exact = False
derived_solution_stack_factors(...).schoen_banana_gluing.obstruction.vanishes = True
derived_solution_stack_factors(...).schoen_banana_gluing.solved = True
```

This is not a harmless display issue.  The zero obstruction vector

```text
overlap_orientation = 0,
compact_support_BC = 0,
HN_overlap = 0,
motivic_overlap = 0
```

is inserted as data, not computed from a compact-support gluing
correspondence.  Hence the current finite oracle verifies local banana
numerics and then assumes the compact gluing obstructions vanish.

There is a second load-bearing under-specification.  The local banana
model and the compact Schoen container are distinct charge geometries.
Local banana data live on the two-curve sector with singular intersection
matrix

```text
((-2, 2), (2, -2)), determinant 0,
```

whereas the compact Schoen threefold has `h11=h21=19`.  A theorem must
therefore include the local-to-compact charge map, its null directions,
and the resulting compact support convention.  The current closure text
names compact-support Hall gluing but does not construct the charge map,
extension-by-zero functor, overlap Cech diagram, or motivic integration
compatibility that would make `o_glue` a computed class.

## Fatal/nonfatal verdict

Fatal for the claim "the Schoen/banana compact Hall gluing point has been
constructed."

Nonfatal for the stronger repaired programme: the lane is correctly
typed as a closed zero-fiber problem over the finite-first Hall cosheaf.
The repair is to make `o_glue` an explicit finite obstruction vector
computed from a compact-support local-to-global Hall diagram, and to make
the Schoen factor unsolved until those coordinates are produced by that
diagram.

## Exact repair/heal theorem statement

**Theorem (Schoen banana compact Hall gluing certificate).**
Let

```tex
\pi:X_{\mathrm{Sch}}\to \mathbb P^1
```

be a Schoen-type compact Calabi--Yau threefold and let
`U_a` be the formal or analytic neighborhoods of its banana singular
fibers, together with the complementary compact chart needed to cover the
compact derived critical stack.  Fix a finite charge bound `(N,R)`.
For each chart let

```tex
\mathcal H^{\mathrm{mot},o_a}_{a,\le N,\le R}
```

be the oriented local HN Hall quotient with local charge lattice
`\Gamma_a`.  A compact Schoen point

```tex
\operatorname{ExCert}(X_{\mathrm{Sch}};\sigma,Q,S,o,T_{\mathrm{eq}},\Mot)
```

exists in the finite quotient if and only if the following six pieces of
data exist and satisfy the stated equations.

1. **Compact-support charge pushforward.**  For every chart there is a
   charge map

   ```tex
   j_{a,!}:\Gamma_{a,\le N,\le R}\to \Gamma_{X,\le N,\le R}
   ```

   induced by extension by zero of objects with proper support in `U_a`.
   It identifies and quotients the null fiber directions of the banana
   intersection matrix before comparison with the compact charge lattice.

2. **Extension-stack Beck--Chevalley.**  For every retained pair
   `alpha,beta`, the square comparing local and compact exact-triangle
   stacks is Cartesian after compact-support pullback, and the Hall
   pushforward is proper on the retained HN quotient:

   ```tex
   j_{a,!} q_{a,!} p_a^* = q_{X,!} p_X^* (j_{a,!}\times j_{a,!}).
   ```

3. **Orientation Cech and Thom--Sebastiani compatibility.**  The local
   orientation square roots `o_a` and the compact orientation `o` are
   related by transition cochains `q_ab` with `delta q=0`; under exact
   triangles the induced quadratic refinements agree with the compact
   Hall sign.

4. **HN local-to-global compatibility.**  For every retained object `E`
   with compact support in `U_a`, semistability and phase order are
   preserved by `j_{a,!}`.  Equivalently,

   ```tex
   HN_X(j_{a,!}E)=j_{a,!}HN_a(E)
   ```

   in the ordered strict sector, and no active ray lands on the sector
   boundary after pushforward.

5. **Motivic integration overlap compatibility.**  On every double and
   triple overlap,

   ```tex
   \Int_X^{\Mot}\circ j_{a,!}
     =
   J_{a,*}\circ \Int_a^{\Mot}
   ```

   in the completed motivic quantum torus, including the half-Tate and
   orientation factors.

6. **Finite quotient continuity.**  The five preceding structures commute
   with restriction from `(N',R')` to `(N,R)`.  The compact Schoen object
   is the inverse limit of these finite glued quotients.

Define

```tex
o_{\mathrm{Sch,ban},\le N,\le R}
 =
(o_{\mathrm{charge}},o_{\mathrm{BC}},o_{\mathrm{or}},
  o_{\mathrm{HN}},o_{\mathrm{mot}},o_{\mathrm{comp}}).
```

Then

```tex
o_{\mathrm{Sch,ban},\le N,\le R}=0
```

if and only if the local banana Hall charts glue to the compact Schoen
finite Hall quotient.  The full compact Schoen theorem is the assertion
that this equality holds for every `(N,R)`.

The local equalities

```tex
S_4^{\mathrm{inst}}=-44,\qquad r_{\max}=-1
```

are inputs to the local chart and prove non-toric higher-shadow
nontriviality.  They do not by themselves imply
`o_{\mathrm{Sch,ban},\le N,\le R}=0`.

## Local file anchors

- `chapters/theory/bps_positive_geometry_closure.tex:220` states the
  Schoen certificate and says the lane is equivalent to compact-support
  HN-compatible local banana Hall gluing.
- `chapters/theory/bps_positive_geometry_closure.tex:247` proves only
  the iff form: local Hall data become compact data precisely when the
  compact-support correspondences glue and preserve HN order.
- `chapters/theory/bps_positive_geometry_closure.tex:481` defines the
  residual data space with compact-support Hall correspondences, but the
  concrete Schoen compact-support diagram is not supplied.
- `chapters/theory/bps_positive_geometry_closure.tex:548` makes
  `X_{\mathrm{Sch}}` the equation `o_{\mathrm{glue}}=0`.
- `chapters/theory/bps_positive_geometry_closure.tex:569` identifies
  `o_{\mathrm{glue}}` with the compact Hall Cech defect, but does not
  construct its Cech coordinates.
- `compute/lib/bps_positive_truncation.py:682` implements
  `schoen_banana_gluing_certificate()` by checking local banana shadow
  values only.
- `compute/lib/bps_positive_truncation.py:697` marks that certificate
  `exact=False`.
- `compute/lib/bps_positive_truncation.py:849` constructs the
  Schoen solution-stack factor with four obstruction coordinates already
  set to zero.
- `compute/lib/bps_positive_truncation.py:291` defines `solved` as
  `certificate.passed and obstruction.vanishes`, so a non-exact passed
  ledger becomes solved when its placeholder obstruction vector is zero.
- `compute/lib/banana_shadow.py:498` computes the local banana shadow
  tower.
- `compute/lib/banana_shadow.py:553` returns `S4_instanton=-44`,
  `shadow_class="M"`, and `r_max=-1`.
- `compute/lib/banana_shadow.py:776` records the degenerate local banana
  intersection matrix and its null fiber class.
- `compute/lib/cy3_grand_atlas.py:702` distinguishes the compact Schoen
  threefold from the local banana curve sector.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_10_compact_examples_and_falsification.md:655`
  lists the exact missing compact realization data.
- `notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md:95`
  already states the correct warning: local curve data do not
  automatically glue to compact Hall correspondences.

## Primary/literature anchors

- Schoen 1988 is the local-note anchor for the compact fiber product
  construction and `h11=h21=19`; see
  `compute/tests/test_banana_shadow.py:691`.
- Bryan--Kool--Young / Bryan--Kool are the local-note anchors for
  banana GV/DT data and the quasi-Jacobi structure; see
  `compute/lib/banana_shadow.py:15`, `compute/lib/banana_shadow.py:97`,
  and `compute/tests/test_banana_shadow.py:736`.
- Oberdieck--Pixton is the local-note/bibliography anchor for elliptic
  fibration Jacobi-form and holomorphic-anomaly structure; see
  `compute/lib/banana_shadow.py:101` and
  `bibliography/references.tex:592`.
- Joyce--Upmeier / Kinjo--Park--Safronov are the local-note anchors for
  strong orientation as actual input; see
  `notes/bps_positive_geometry_total_resolution_20260424/agent_01_compact_cy3_construction.md:576`.
- Kontsevich--Soibelman/Joyce--Song provide the Hall wall-crossing and
  generalized DT background already present in the bibliography at
  `bibliography/references.tex:707` and `bibliography/references.tex:865`.

## Executable checks proposed or run

Run:

```text
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_schoen_banana_gluing_certificate \
  compute/tests/test_banana_shadow.py::TestBananaShadowIV::test_banana_shadow_structure_from_disjoint_sources
```

Result:

```text
2 passed in 0.18s
```

Run:

```text
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
    schoen_banana_gluing_certificate,
)
from compute.lib.banana_shadow import (
    banana_genus0_gv_total,
    banana_jacobi_data,
    banana_shadow_tower,
    intersection_determinant,
)
bound = TruncationBound(4,4)
cert = schoen_banana_gluing_certificate()
print(cert.passed, cert.exact)
print(banana_shadow_tower())
print(banana_genus0_gv_total(3))
print(banana_jacobi_data())
print(intersection_determinant())
for factor in derived_solution_stack_factors(bound):
    if factor.name == "schoen_banana_gluing":
        print(factor.solved, factor.obstruction)
PY
```

Observed facts:

```text
certificate.passed=True
certificate.exact=False
S4_instanton=-44
r_max=-1
banana_genus0_gv_total(3)=-44
banana Jacobi index matrix=((2,-2),(-2,2))
intersection determinant=0
schoen factor solved=True
```

Proposed executable additions:

1. A negative test:

   ```python
   assert not schoen_factor.solved
   ```

   unless the compact-support gluing witness object is supplied.

2. A `CompactHallGluingDatum` finite oracle containing:

   ```text
   charge_pushforward_matrix,
   compact_support_Beck_Chevalley_squares,
   orientation_Cech_cochains,
   HN_phase_order_table,
   motivic_overlap_equalities,
   transition_maps_for_(N,R).
   ```

3. A local/compact normalization test checking that the singular local
   banana rank-two charge sector is compared to the compact Schoen
   charge lattice through an explicit pushforward/quotient, not by
   identifying `(2,2)` local Hodge data with `(19,19)` compact Hodge
   data.

## Remaining point-construction obligation

Construct, for a Schoen fiber product, the actual compact-support
oriented Hall Cech diagram:

```tex
\{\mathcal H^{\mathrm{mot},o_a}_{a,\le N,\le R}\}_a
\rightrightarrows
\{\mathcal H^{\mathrm{mot},o_{ab}}_{ab,\le N,\le R}\}_{a,b}
\longrightarrow
\mathcal H^{\mathrm{mot},o}_{X_{\mathrm{Sch}},\le N,\le R}.
```

The construction must exhibit the local-to-compact charge map, prove
compact-support Beck--Chevalley for the extension stacks, prove
orientation Cech triviality or retain the gerbe twist, prove HN
compatibility under extension by zero, and prove motivic integration
commutes with the gluing diagram.  Only then does the Schoen/banana
zero-fiber equation produce an actual point rather than a correctly typed
closed substack.
