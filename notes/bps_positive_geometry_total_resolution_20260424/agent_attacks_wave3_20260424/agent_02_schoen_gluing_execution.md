# Agent 02 Wave 3: Schoen/Banana Compact Gluing Execution

## Scope

Assigned write scope only:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_02_schoen_gluing_execution.md
```

No code, TeX, git state, or other notes were edited.

## Claim Attacked

The remaining Schoen point obligation is not the local banana theorem.
The false implication to destroy is:

```text
local banana shadow data pass
and X_Sch has compact Hodge type chi=0
and schoen_banana_gluing_certificate().passed
=> ExCert(X_Sch; sigma,Q,S,o,T_eq,Mot).
```

This implication is false.  The current local certificate checks only the
banana shadow input.  It is deliberately `exact=False`, and the derived
factor is a zero-fiber substack, not a constructed point.

The healed problem is stronger and sharper: construct a point of the
Schoen closed substack by computing and vanishing the full nine-coordinate
finite compact-gluing vector.

## File Anchors Read

- `chapters/theory/bps_positive_geometry_closure.tex:43`: finite visible
  charge set and saturated Hall-lower quotient.
- `chapters/theory/bps_positive_geometry_closure.tex:50`: the complement
  must generate a closed two-sided Hall ideal.
- `chapters/theory/bps_positive_geometry_closure.tex:104`: finite-first
  theorem assumes a cofinal Mittag--Leffler tower of finite saturated
  Hall-lower sets and Hall-admissible extension correspondences.
- `chapters/theory/bps_positive_geometry_closure.tex:231`: `ExCert`
  includes compact stability, support, HN, orientation, motivic, finite
  control, integration, and realization data.
- `chapters/theory/bps_positive_geometry_closure.tex:249`: Schoen lane is
  compact banana Hall gluing, not local banana data alone.
- `chapters/theory/bps_positive_geometry_closure.tex:252`: quintic and
  Schoen named-example theorem is the exact certificate `ExCert`.
- `chapters/theory/bps_positive_geometry_closure.tex:259`: Schoen requires
  compact-support HN-compatible correspondences.
- `chapters/theory/bps_positive_geometry_closure.tex:263`: local banana
  input records `S_4^{inst}=-44` and `r_max=-1`.
- `chapters/theory/bps_positive_geometry_closure.tex:552`: derived
  solution stack starts.
- `chapters/theory/bps_positive_geometry_closure.tex:562`: finite data
  space contains chamber data, orientation, motivic coefficients, wall
  transport, compact-support Hall correspondences, and automorphic pairing.
- `chapters/theory/bps_positive_geometry_closure.tex:588`: `o_Ex` records
  compact chamber data; `o_glue` records compact Hall Cech gluing.
- `chapters/theory/bps_positive_geometry_closure.tex:632`: points of the
  residual stack are complete solutions only after named obstruction
  coordinates are computed and vanish.
- `chapters/theory/bps_positive_geometry_closure.tex:651`: BMS gives an
  actual compact non-toric point; Schoen remains a closed substack.
- `compute/lib/bps_positive_truncation.py:692`: local Schoen certificate.
- `compute/lib/bps_positive_truncation.py:705`: certificate is returned.
- `compute/lib/bps_positive_truncation.py:707`: certificate is `exact=False`.
- `compute/lib/bps_positive_truncation.py:708`: theorem target is compact
  Schoen `ExCert` iff local banana charts glue by compact-support
  HN-compatible correspondences.
- `compute/lib/bps_positive_truncation.py:967`: derived solution factors.
- `compute/lib/bps_positive_truncation.py:988`: Schoen factor.
- `compute/lib/bps_positive_truncation.py:991`: current executable
  obstruction vector.
- `compute/lib/bps_positive_truncation.py:993`: current names start with
  `charge_pushforward`.
- `compute/lib/bps_positive_truncation.py:1001`: Schoen obstruction vector
  is `computed=False`.
- `compute/tests/test_bps_positive_truncation.py:301`: local certificate
  test.
- `compute/tests/test_bps_positive_truncation.py:420`: derived factors are
  zero fibers, not solved points.
- `compute/tests/test_bps_positive_truncation.py:448`: constructed points
  certificate records Schoen as unresolved.
- `compute/lib/banana_shadow.py:498`: banana shadow tower.
- `compute/lib/banana_shadow.py:557`: `S_4^{inst}=-44`.
- `compute/lib/banana_shadow.py:558`: shadow class is `M`.
- `compute/lib/banana_shadow.py:559`: `r_max=-1`.
- `compute/lib/banana_shadow.py:749`: banana quasi-Jacobi data.
- `compute/lib/banana_shadow.py:776`: local banana intersection matrix.
- `compute/lib/banana_shadow.py:789`: determinant of that matrix.
- `compute/lib/cy3_grand_atlas.py:702`: compact Schoen/banana family.
- `compute/lib/cy3_grand_atlas.py:723`: compact Schoen Hodge numbers
  `h11=h21=19`, `chi=0`.
- `chapters/theory/gluing/sec_10_unifying.tex:531`: compact Hall
  construction datum on a chamber.
- `chapters/theory/gluing/sec_10_unifying.tex:660`: Cech/Ran cosheaf
  axioms.
- `chapters/theory/gluing/sec_10_unifying.tex:698`: finite wall transport
  must become KS conjugation after motivic integration.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_02_schoen_banana_gluing.md:249`:
  wave-2 healed Schoen theorem.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_02_schoen_banana_gluing.md:305`:
  wave-2 oracle verdict.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_02_schoen_banana_gluing.md:422`:
  wave-2 remaining obligations.

## Present Oracle Verdict

The live oracle correctly prevents the local banana ledger from becoming
a false compact point:

```text
schoen_cert: passed=True, exact=False, checked_items=4
factor: solved=False, zero_fiber_defined=True, computed=False
constructed_named_points: passed=False, exact=False
```

But the live Schoen obstruction vector still has only six names:

```text
charge_pushforward
compact_support_BC
overlap_orientation
HN_overlap
motivic_overlap
pro_continuity
```

For the platonic point obligation this is too small.  The required finite
vector has nine coordinates:

```text
semistable_restriction
charge_pushforward_null_fiber
beck_chevalley
relative_orientation
HN_overlap
motivic_overlap
hall_lower_saturation
KS_monodromy
pro_continuity
```

Thus the strongest current defect is not a false solved claim.  The false
solved claim is blocked.  The surviving defect is that the executable
Schoen signature has not yet been refined to the full nine-coordinate
point-construction vector.

## Attack -> Heal Cycles

### Cycle 1: Semistable Restriction

**Attack.**  A semistable Schoen degeneration with banana local charts
does not determine a compact Bridgeland or Hall stability datum.  Local
curve sectors can be visible while compact objects crossing the same
central-charge sector have no certified HN filtration in the retained
finite quotient.

**Strongest failure mode.**  One can pass the local banana shadow checks
and still have no table proving

```text
HN_X(j_{a,!}E) = j_{a,!}HN_a(E)
```

for every retained local semistable object and every overlap.

**Heal.**  Split off the coordinate
`semistable_restriction`.  It vanishes precisely when a compact chamber
`(sigma,Q,S)` is supplied and each local banana semistable chart is the
restriction of that compact chamber on the finite Hall-lower set.

### Cycle 2: Charge Pushforward and Null-Fiber Quotient

**Attack.**  The local banana rank-two intersection matrix has determinant
zero.  Its null fiber direction cannot be silently identified with a
nondegenerate compact numerical lattice.  Local quasi-Jacobi index data
do not define the compact support map on `K_num(X_Sch)`.

**Strongest failure mode.**  The current name `charge_pushforward` hides
two separate requirements:

```text
j_{a,!}: Gamma_{a,L} -> Gamma_{X,L}
and
Gamma_{a,L}/<null fiber> -> image(j_{a,!}).
```

The first is functorial compact-support pushforward.  The second is the
quotient or transport of the local null fiber direction.

**Heal.**  Replace the coordinate by
`charge_pushforward_null_fiber`.  It vanishes exactly when every local
charge pushforward matrix is supplied, sends retained local charges into
the compact retained set, and has the declared null-fiber quotient as its
kernel on the local banana curve sector.

### Cycle 3: Compact-Support Beck-Chevalley

**Attack.**  Cech restriction is not Hall convolution.  The compact Hall
product is a pull-push along extension stacks.  Compact-support extension
by zero changes variance and can break the base-change square.

**Strongest failure mode.**  The desired identity

```text
j_! q_{a,!} p_a^*
=
q_{X,!} p_X^*(j_! x j_!)
```

can fail on a finite retained pair even if both local products and compact
products are separately associative.

**Heal.**  The coordinate `beck_chevalley` is the finite list of
compact-support Hall extension squares.  It vanishes precisely when every
retained local product transported by `j_!` agrees with the compact Hall
product after projecting to the saturated Hall-lower quotient.

### Cycle 4: Relative Orientation and Motivic Overlap

**Attack.**  Local orientation square roots do not automatically descend.
The obstruction is relative: a local orientation need not equal the
restriction of the chosen compact Hall orientation output.  Even after
orientation descent, motivic integration can disagree by half-Tate or
vanishing-cycle factors on overlaps.

**Strongest failure mode.**  A scalar orientation sign check is too weak.
The true check is a Cech comparison of determinant-line square-root
transports relative to the compact orientation output, followed by
compatibility of the motivic integration maps on double and triple
overlaps.

**Heal.**  Keep two coordinates:

```text
relative_orientation
motivic_overlap
```

The first vanishes when the local determinant-line square roots glue to
the compact orientation output.  The second vanishes when the motivic
integration maps agree on overlaps with the same orientation and
half-Tate normalization.

### Cycle 5: HN Overlap and Hall-Lower Saturation

**Attack.**  HN overlap compatibility and Hall-lower saturation are
independent.  A chart can preserve phase order on overlaps while the
finite set is still not closed under HN factors of compact extensions.
Conversely, a Hall-lower set can be saturated while the chart transition
changes sector order.

**Strongest failure mode.**  The current oracle has `HN_overlap` but no
`hall_lower_saturation`.  Therefore a future implementation could pass
overlap tables while silently using a non-ideal finite quotient.

**Heal.**  Require both coordinates:

```text
HN_overlap
hall_lower_saturation
```

`HN_overlap` vanishes when strict-sector phase order is preserved on all
overlaps and no active ray lands on the boundary after transition.
`hall_lower_saturation` vanishes when every retained compact extension
has all HN factors retained and the complement is a closed two-sided Hall
ideal.

### Cycle 6: KS Monodromy and Pro-Continuity

**Attack.**  Schoen singular fibers carry wall transport.  Finite local
gluing can pass on every chosen chart and still fail around a loop if the
DWR/Cech transport is not carried by motivic integration to KS
conjugation.  Passing one finite level also does not prove compatibility
under the inverse tower.

**Strongest failure mode.**  The equation

```text
Int^Mot_{N,R} T^{DWR}_{wp,N,R}
=
Ad_{KS_{wp,N,R}} Int^Mot_{N,R}
```

can fail at a retained wall path, or it can hold at level `(N,R)` and
fail after transition from a larger quotient.

**Heal.**  Require two coordinates:

```text
KS_monodromy
pro_continuity
```

`KS_monodromy` vanishes when every retained admissible wall loop has the
finite DWR/KS compatibility above.  `pro_continuity` vanishes when all
nine coordinates commute with the quotient transition maps in a cofinal
Mittag--Leffler tower.

## Healed Iff Theorem

Let `X_Sch` be a compact Schoen Calabi-Yau threefold with banana local
charts `{U_a}` over the singular fibers.  Fix a strict sector `S` and a
finite saturated Hall-lower set `L=L_{<=N,<=R}`.

Define the finite Schoen gluing vector

```text
o_Sch,L =
(
  o_ss,
  o_ch,
  o_BC,
  o_or_rel,
  o_HN,
  o_Mot,
  o_lower,
  o_KS,
  o_pro
)
```

with coordinates:

```text
o_ss     = semistable_restriction
o_ch     = charge_pushforward_null_fiber
o_BC     = beck_chevalley
o_or_rel = relative_orientation
o_HN     = HN_overlap
o_Mot    = motivic_overlap
o_lower  = hall_lower_saturation
o_KS     = KS_monodromy
o_pro    = pro_continuity
```

Then the finite compact Schoen Hall gluing datum exists if and only if

```text
o_Sch,L = 0.
```

The compact Schoen point

```text
ExCert(X_Sch; sigma,Q,S,o,T_eq,Mot)
```

exists if and only if `o_Sch,L=0` on a cofinal Mittag--Leffler tower and
the transition maps preserve the compact-support Hall correspondences,
orientations, motivic integrations, HN overlap tables, Hall-lower ideals,
and KS wall transports.

This theorem is strictly stronger than the current local ledger.  The
local banana theorem supplies chart input; the compact point is the
simultaneous vanishing of the nine global gluing coordinates.

## Exact Certificate Signatures

When code scope opens, the executable interface should separate the
nine coordinates instead of hiding them inside six names.

```python
@dataclass(frozen=True)
class CompactSchoenBananaGluingDatum:
    semistable_restriction_table: tuple[tuple[str, str, str], ...]
    charge_pushforward_matrix: FiniteLinearMap
    local_null_fiber_basis: tuple[tuple[Fraction, ...], ...]
    beck_chevalley_squares: tuple[FiniteCommutativeSquare, ...]
    relative_orientation_cech_matrix_F2: tuple[tuple[int, ...], ...]
    hn_overlap_phase_table: tuple[tuple[str, str, str], ...]
    motivic_overlap_equalities: tuple[tuple[MotivicClass, MotivicClass], ...]
    hall_lower_witnesses: tuple[tuple[Charge, tuple[Charge, ...]], ...]
    ks_monodromy_transport_matrices: tuple[FiniteLinearMap, ...]
    pro_transition_commutators: tuple[FiniteCommutativeSquare, ...]
```

The certificate functions should be:

```python
def schoen_semistable_restriction_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_charge_pushforward_null_fiber_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_beck_chevalley_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_relative_orientation_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_hn_overlap_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_motivic_overlap_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_hall_lower_saturation_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
    ambient_charges: tuple[Charge, ...],
) -> Certificate: ...

def schoen_ks_monodromy_certificate(
    datum: CompactSchoenBananaGluingDatum,
    truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_pro_continuity_certificate(
    small: CompactSchoenBananaGluingDatum,
    big: CompactSchoenBananaGluingDatum,
    small_truncation: FiniteHallTruncation,
    big_truncation: FiniteHallTruncation,
) -> Certificate: ...

def schoen_banana_constructed_point_certificate(
    tower: tuple[CompactSchoenBananaGluingDatum, ...],
    truncations: tuple[FiniteHallTruncation, ...],
) -> Certificate: ...
```

The aggregate obstruction vector should be exactly:

```python
ObstructionVector(
    names=(
        "semistable_restriction",
        "charge_pushforward_null_fiber",
        "beck_chevalley",
        "relative_orientation",
        "HN_overlap",
        "motivic_overlap",
        "hall_lower_saturation",
        "KS_monodromy",
        "pro_continuity",
    ),
    values=(0, 0, 0, 0, 0, 0, 0, 0, 0),
    computed=False,
)
```

The aggregate point certificate may pass only when every coordinate
certificate is exact, computed, and passed at every finite level, and the
transition certificates pass between levels.

## Minimal Executable Falsifiers

These are the smallest tests that should fail on bad future
implementations and pass only for the real nine-coordinate construction.

### Falsifier 1: Local Shadow Must Not Solve the Point

```python
def test_schoen_local_shadow_does_not_construct_point():
    cert = schoen_banana_gluing_certificate()
    factor = {
        f.name: f for f in derived_solution_stack_factors(TruncationBound(4, 4))
    }["schoen_banana_gluing"]

    assert cert.passed
    assert not cert.exact
    assert factor.zero_fiber_defined
    assert not factor.solved
    assert not factor.obstruction.computed
```

Current status: already passes in substance.

### Falsifier 2: Nine Coordinate Names Are Required

```python
def test_schoen_obstruction_vector_has_nine_coordinates():
    factor = {
        f.name: f for f in derived_solution_stack_factors(TruncationBound(4, 4))
    }["schoen_banana_gluing"]

    assert factor.obstruction.names == (
        "semistable_restriction",
        "charge_pushforward_null_fiber",
        "beck_chevalley",
        "relative_orientation",
        "HN_overlap",
        "motivic_overlap",
        "hall_lower_saturation",
        "KS_monodromy",
        "pro_continuity",
    )
```

Current status: would fail.  The live oracle has six names and is missing
`semistable_restriction`, `hall_lower_saturation`, and `KS_monodromy`;
it also needs to refine `charge_pushforward` and `overlap_orientation`.

### Falsifier 3: Null Fiber Cannot Be Injected Into Compact Charge

```python
def test_schoen_charge_pushforward_detects_unquotiented_null_fiber():
    datum = local_only_banana_datum_with_identity_charge_pushforward()
    cert = schoen_charge_pushforward_null_fiber_certificate(datum, truncation)

    assert not cert.passed
    assert {"check": "null_fiber_kernel"} in cert.discrepancies
```

This blocks the false identification of the degenerate local banana index
matrix with compact numerical charge geometry.

### Falsifier 4: HN Overlap Does Not Imply Hall-Lower Saturation

```python
def test_schoen_hn_overlap_without_hall_lower_saturation_fails():
    datum = datum_with_valid_phase_overlap_but_missing_extension_factor()

    assert schoen_hn_overlap_certificate(datum, truncation).passed
    assert not schoen_hall_lower_saturation_certificate(
        datum, truncation, ambient_charges
    ).passed
```

This guards the finite-first theorem: quotient associativity rests on the
closed Hall ideal condition, not on sector overlap alone.

### Falsifier 5: KS Loop Failure Blocks Compact Gluing

```python
def test_schoen_ks_monodromy_mismatch_blocks_point():
    datum = datum_with_one_bad_wall_loop()
    cert = schoen_ks_monodromy_certificate(datum, truncation)

    assert not cert.passed
    assert {"check": "DWR_KS_wall_transport"} in cert.discrepancies
```

This makes the wall-transport identity executable.

### Pass Case: One-Triangle Toy Compact Gluing Datum

```python
def test_schoen_one_triangle_toy_gluing_passes():
    datum = toy_one_chart_one_overlap_datum_with_zero_all_obstructions()
    certs = schoen_all_coordinate_certificates(datum, truncation)

    assert all(c.exact and c.passed for c in certs)
    assert schoen_banana_constructed_point_certificate(
        (datum,), (truncation,)
    ).passed
```

This pass case is not a Schoen theorem.  It is a regression witness that
the nine certificate functions are not vacuous and can certify an
explicit finite gluing datum when supplied.

## Commands Run

```text
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_schoen_banana_gluing_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points
```

Result:

```text
3 passed in 0.33s
```

Direct oracle probe:

```text
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
    schoen_banana_gluing_certificate,
    constructed_named_points_certificate,
)
from compute.lib.banana_shadow import (
    banana_shadow_tower,
    banana_genus0_gv_total,
    banana_jacobi_data,
    intersection_matrix_banana,
    intersection_determinant,
)

bound = TruncationBound(4, 4)
cert = schoen_banana_gluing_certificate()
print("schoen_cert", cert.passed, cert.exact, cert.checked_items, cert.discrepancies)
print("tower_shadow_class", banana_shadow_tower().shadow_class)
print("tower_S4", banana_shadow_tower().S4_instanton)
print("tower_depth", banana_shadow_tower().r_max)
print("gv_total_3", banana_genus0_gv_total(3))
print("jacobi", banana_jacobi_data())
print("intersection", intersection_matrix_banana(), "det", intersection_determinant())
for factor in derived_solution_stack_factors(bound):
    if factor.name == "schoen_banana_gluing":
        print("factor", factor.name, factor.solved, factor.zero_fiber_defined, factor.obstruction.computed)
        print("names", factor.obstruction.names)
        print("nonzero", factor.obstruction.nonzero_entries())
point_cert = constructed_named_points_certificate(bound)
print("points_cert", point_cert.passed, point_cert.exact)
print("unresolved", [d["factor"] for d in point_cert.discrepancies])
PY
```

Result summarized:

```text
schoen_cert True False 4 ()
tower_shadow_class M
tower_S4 -44
tower_depth -1
gv_total_3 -44
intersection determinant 0
factor schoen_banana_gluing solved=False zero_fiber_defined=True computed=False
names = six-coordinate current vector
points_cert False False
unresolved includes schoen_banana_gluing
```

Additional local banana witnesses:

```text
pytest -q \
  compute/tests/test_banana_shadow.py::TestBananaShadowIV::test_banana_shadow_structure_from_disjoint_sources \
  compute/tests/test_banana_shadow.py::TestIntersectionJacobi::test_intersection_degenerate \
  compute/tests/test_banana_shadow.py::TestIntersectionJacobi::test_intersection_null_vector \
  compute/tests/test_bps_positive_truncation.py::test_schoen_banana_gluing_certificate
```

Result:

```text
4 passed in 0.14s
```

Compact Schoen atlas witnesses:

```text
pytest -q \
  compute/tests/test_cy3_grand_atlas.py::TestBanana::test_chi_zero \
  compute/tests/test_cy3_grand_atlas.py::TestBanana::test_shadow_depth_M
```

Result:

```text
2 passed in 0.05s
```

One stale selector was tried and rejected by pytest:

```text
compute/tests/test_cy3_grand_atlas.py::test_banana_manifold_family_b5_disambiguation
```

It is not a test name in the current suite; no mathematical inference was
taken from that selector failure.

## Files Changed

Only this assigned note was changed:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_02_schoen_gluing_execution.md
```

## What Remains

The remaining Schoen obligation is now exact:

1. Refine the live `schoen_banana_gluing` obstruction vector from six
   names to the nine-coordinate vector above.
2. Implement the nine coordinate certificates with nonvacuous falsifiers.
3. Construct an actual compact Schoen datum supplying the nine coordinate
   values on a finite saturated Hall-lower quotient.
4. Prove and compute vanishing on a cofinal Mittag--Leffler tower.
5. Only then promote the Schoen closed substack to an actual compact
   non-toric point of `Sol^BPS`.

This is a strict strengthening of the current state.  The local banana
shadow remains theorem-grade input; the compact Schoen point is the
vanishing of the full finite gluing vector, not a consequence of the
local shadow alone.
