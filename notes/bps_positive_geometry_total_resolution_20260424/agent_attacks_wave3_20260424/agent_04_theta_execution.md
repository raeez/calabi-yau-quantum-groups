# Agent 04: theta package execution attack and heal

Date: 2026-04-24.

## Object Attacked

The remaining theta point obligation is not the intrinsic finite Hall
theta package.  That package is already a finite theorem in the current
closure:

```text
theta_p^{lambda,c} = Phi_KS(b->c)(x_p).
```

The remaining obligation is the construction of an actual external or
framed theta-package point over a named non-toric compact chamber.  The
top-level finite zero-fiber coordinate in the current oracle is

```text
o_theta^{pkg} =
(
  hall_joint_holonomy,
  broken_line_package,
  GHKK_package,
  GMN_package,
  core_charge_identification,
  wall_function_identification,
  orientation_half_tate_match,
  multiplication_comparison,
  pro_saturation
).
```

Local anchors:

- `chapters/theory/bps_positive_geometry_closure.tex:391` states the
  intrinsic Hall theta theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:427` states and
  proves the comparison iff corollary.
- `compute/lib/bps_positive_truncation.py:737` implements
  `theta_comparison_certificate(bound) -> Certificate`.
- `compute/lib/bps_positive_truncation.py:1021` records the
  `theta_comparison` solution-stack factor with nine uncomputed
  coordinates.
- `compute/lib/bps_positive_truncation.py:260` defines
  `ObstructionVector`.
- `compute/lib/bps_positive_truncation.py:290` defines
  `SolutionStackFactor`.
- `compute/lib/scattering_diagram_e1_mc.py:1145` computes local theta
  functions from an MC scattering solution.
- `compute/lib/c3_hcs_hall_theta.py:120` gives the abelian fixed
  `C^3` framed-Hall theta witness.
- `compute/lib/compact_hall_construction_package.py:156` records full
  nerve theta equations for the compact Hall construction package.

## Strongest Finite Intrinsic Theorem

Let `P_{<=N,<=R}` be a finite saturated Hall-lower quotient with support
property, exact oriented Hall product, HN sector descent, finite
motivic integration, and identity KS holonomy around every retained
codimension-two joint.  For a base chamber `b`, define

```text
theta_p^{lambda,c} = Phi_KS(b->c)(x_p).
```

Then the elements are path independent, form the transported Hall
monomial basis, and multiply in the base chamber by

```text
theta_p theta_q =
  L^{<p,q>/2} epsilon_o(p,q) theta_{p+q}
```

when `p+q` is retained, and by zero otherwise.  Transport by
`Phi_KS` gives the same algebra in every chamber.  The completed
intrinsic Hall theta package is the inverse limit along the verified
Hall-lower transition maps.

This theorem is finite, intrinsic, and already represented by the
current executable oracle.  It does not require broken-line, GHKK, or
GMN input.

## External Comparison Iff Theorem

Let

```text
T in {broken_line, GHKK, GMN, Hall_framed}.
```

Assume `T` supplies finite basis labels, wall functions, transport,
orientation/half-Tate normalization, multiplication, and transition
maps over the same finite chamber datum.  Then

```text
Theta_T^{lambda,c} = Theta_Hall^{lambda,c}
```

as finite theta algebras if and only if

```text
Ob_T = 0
and
Ob_cmp(T,Hall) = 0.
```

The completed equality holds if and only if the finite equalities are
natural for every saturated Hall-lower transition.  The comparison
vector is

```text
Ob_cmp(T,Hall) =
(
  o_core,
  o_wall,
  o_orient,
  o_Tate,
  o_locality,
  o_multiplication,
  o_pro
).
```

The word "if" is construction: vanishing trivializes the ratio of
external transport to Hall KS transport and identifies basis,
orientation, wall factors, multiplication, and pro-system.  The word
"only if" is rigidity: equality of theta algebras forces the same
transport, wall factors, orientation twists, multiplication constants,
and transition maps, hence the obstruction vector is zero.

## Attack -> Heal Cycles

### Cycle 1: broken-line gate

Attack.  A finite Hall scattering diagram does not itself construct
broken lines.  Broken-line termination needs local finiteness, strict
height growth, finite bending, triangular leading monomials, label
saturation, and identity joint holonomy.  Without these hypotheses the
formula can accumulate or lose basis triangularity.

Heal.  The broken-line package is a point only on the zero fiber

```text
Ob_bl =
(
  o_locfin,
  o_joint,
  o_height,
  o_bend,
  o_orient,
  o_tri,
  o_sat
).
```

Vanishing gives finite inductive construction of broken-line theta
functions in each quotient; comparison with Hall is then governed by
`Ob_cmp(bl,Hall)`.

### Cycle 2: GHKK gate

Attack.  GHKK theta functions require cluster or cluster-like seeds,
mutation/scattering compatibility, enough global monomials or a stronger
basis theorem, an upper/regular algebra target, and completion control.
None follows formally from a compact CY3 Hall chamber.

Heal.  The GHKK package is a point only on the zero fiber

```text
Ob_GHKK =
(
  o_seed_atlas,
  o_scattering_identification,
  o_EGM_or_basis,
  o_upper_algebra_target,
  o_orientation_skew_form,
  o_mutation,
  o_completion
).
```

If these vanish, GHKK gives an external finite theta algebra.  It equals
the Hall theta algebra exactly when `Ob_cmp(GHKK,Hall)` vanishes.

### Cycle 3: GMN gate

Attack.  A GMN/Riemann-Hilbert package needs a spectral cover, central
charge periods, spectral-network sectors, detour sums, 2d-4d wall
crossing, halo/framed-line data, spin/orientation refinements,
abelianization, OPE closure, and completion.  KS wall crossing alone is
far too weak.

Heal.  The GMN package is a point only on the zero fiber

```text
Ob_GMN =
(
  o_cover,
  o_period,
  o_sector,
  o_detour,
  o_2d4d,
  o_halo,
  o_framed_lines,
  o_spin,
  o_abelianization,
  o_OPE,
  o_completion
).
```

Vanishing constructs a finite GMN theta algebra.  Equality with the
intrinsic Hall package is precisely `Ob_cmp(GMN,Hall)=0`.

### Cycle 4: Hall-framed gate

Attack.  The intrinsic formula `Phi_KS(b->c)(x_p)` gives transported
monomials in the Hall quantum torus.  It does not by itself construct
framed objects, framed critical stacks, framed Hall modules, or a defect
OPE.

Heal.  The framed Hall construction has its own zero fiber

```text
Ob_Hall_fr =
(
  o_framed_objects,
  o_framed_critical_stacks,
  o_orientation_transport,
  o_Hall_action,
  o_finite_truncation,
  o_triangularity,
  o_OPE_Hall,
  o_realization
).
```

This is the smallest plausible compact target because it stays inside
the Hall category.  It still requires proof of framed moduli, OPE/Hall
compatibility, and finite-to-pro continuity before it becomes an actual
point.

### Cycle 5: wall and core comparison gate

Attack.  Two packages can have the same wall support and still define
different theta algebras.  Wall functions can differ by motivic
normalization, Euler specialization, BCH approximation, sign,
orientation character, or half-Tate power.  The local scattering tests
explicitly record that BCH multiplicities are not exact DT invariants at
higher heights.

Heal.  Comparison requires

```text
(o_core, o_wall, o_orient, o_Tate) = 0.
```

`o_core` identifies the charge lattice and theta labels.
`o_wall` identifies external wall factors with motivic Hall quantum
dilogarithm factors.  `o_orient` identifies the orientation character.
`o_Tate` fixes the half-Tate grading normalization.

### Cycle 6: locality and multiplication gate

Attack.  Matching individual basis elements does not prove equality of
theta algebras.  Multiplication can leave the retained lower set,
pair-of-pants or broken-line multiplication can disagree with Hall
convolution, and framed OPE can violate the Hall product normalization.

Heal.  Comparison requires

```text
(o_locality, o_multiplication) = 0.
```

`o_locality` asserts that the construction is compatible with chamber
restriction, sector descent, and retained finite labels.  `o_multiplication`
asserts equality of structure constants with the oriented Hall product,
including zero boundary products when `p+q` leaves the quotient.

### Cycle 7: pro-saturation gate

Attack.  A comparison in one finite quotient is not a completed theta
package.  Transition maps can drop labels, fail lower-set closure, or
destroy wall-function normalization.

Heal.  The completed comparison requires

```text
o_pro = 0
```

in every finite quotient and naturality under the saturated Hall-lower
transition maps.  The pro-package is an inverse limit of finite algebra
comparisons, not a formal completion after a single check.

## Exact Dataclass And Certificate Signatures

Current executable signatures:

```python
@dataclass(frozen=True)
class Certificate:
    name: str
    exact: bool
    theorem_target: str
    normalization: str
    checked_items: int
    discrepancies: Tuple[Dict[str, object], ...]
    source_modules: Tuple[str, ...]

@dataclass(frozen=True)
class ObstructionVector:
    names: Tuple[str, ...]
    values: Tuple[Fraction, ...]
    computed: bool = True

@dataclass(frozen=True)
class SolutionStackFactor:
    name: str
    certificate: Certificate
    obstruction: ObstructionVector
```

Current theta certificate surface:

```python
theta_comparison_certificate(bound: TruncationBound) -> Certificate
derived_solution_stack_factors(bound: TruncationBound) -> Tuple[SolutionStackFactor, ...]
obstruction_zero_certificate(name: str, obstruction: ObstructionVector) -> Certificate
transition_certificate(small: BPSMotivicTruncation, big: BPSMotivicTruncation) -> Certificate
```

Next exact oracle surface, not yet implemented in this agent scope:

```python
ThetaPackage = Literal["broken_line", "GHKK", "GMN", "Hall_framed"]

theta_package_obstruction_certificate(
    package: ThetaPackage,
    bound: TruncationBound,
) -> tuple[Certificate, ObstructionVector]

theta_package_comparison_certificate(
    package: ThetaPackage,
    bound: TruncationBound,
) -> tuple[Certificate, ObstructionVector]

theta_package_point_certificate(
    package: ThetaPackage,
    bound: TruncationBound,
) -> Certificate
```

The point certificate should pass only when both the package obstruction
and the comparison obstruction are exact, computed, zero, and compatible
with transitions for every retained finite quotient.

## Executable Pass/Fail Examples Available Now

Direct oracle query:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    derived_solution_stack_factors,
    obstruction_zero_certificate,
    theta_comparison_certificate,
)

b = TruncationBound(5, 6, 1)
c = theta_comparison_certificate(b)
print(c.name, c.passed, c.exact, c.checked_items, c.discrepancies)
for f in derived_solution_stack_factors(b):
    if f.name == "theta_comparison":
        print(f.name, f.zero_fiber_defined, f.solved)
        print(f.obstruction.names)
        print(f.obstruction.computed, f.obstruction.vanishes)
        print(obstruction_zero_certificate("theta_comparison", f.obstruction).discrepancies)
PY
```

Output:

```text
theta_comparison True False 16026 ()
theta_comparison True False
('hall_joint_holonomy', 'broken_line_package', 'GHKK_package', 'GMN_package', 'core_charge_identification', 'wall_function_identification', 'orientation_half_tate_match', 'multiplication_comparison', 'pro_saturation')
False False
({'obstruction': 'hall_joint_holonomy', 'value': 'uncomputed'}, {'obstruction': 'broken_line_package', 'value': 'uncomputed'}, {'obstruction': 'GHKK_package', 'value': 'uncomputed'}, {'obstruction': 'GMN_package', 'value': 'uncomputed'}, {'obstruction': 'core_charge_identification', 'value': 'uncomputed'}, {'obstruction': 'wall_function_identification', 'value': 'uncomputed'}, {'obstruction': 'orientation_half_tate_match', 'value': 'uncomputed'}, {'obstruction': 'multiplication_comparison', 'value': 'uncomputed'}, {'obstruction': 'pro_saturation', 'value': 'uncomputed'})
```

Synthetic zero-fiber pass/fail check:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction
from compute.lib.bps_positive_truncation import ObstructionVector, obstruction_zero_certificate

pass_vector = ObstructionVector(names=("o_core", "o_wall"), values=(Fraction(0), Fraction(0)), computed=True)
uncomputed_vector = ObstructionVector(names=("o_core", "o_wall"), values=(Fraction(0), Fraction(0)), computed=False)
fail_vector = ObstructionVector(names=("o_core", "o_wall"), values=(Fraction(0), Fraction(1)), computed=True)
for label, vector in (("pass", pass_vector), ("uncomputed", uncomputed_vector), ("nonzero", fail_vector)):
    cert = obstruction_zero_certificate(f"theta_{label}", vector)
    print(label, cert.passed, cert.exact, vector.vanishes, cert.discrepancies)
PY
```

Output:

```text
pass True True True ()
uncomputed False True False ({'obstruction': 'o_core', 'value': 'uncomputed'}, {'obstruction': 'o_wall', 'value': 'uncomputed'})
nonzero False True False ({'obstruction': 'o_wall', 'value': '1'},)
```

Targeted executable surface:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py::test_theta_comparison_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_bps_positive_truncation.py::test_finite_lower_set_certificate_for_rank2_model \
  compute/tests/test_bps_positive_truncation.py::test_finite_lower_set_certificate_detects_omitted_ambient_summands \
  compute/tests/test_bps_positive_truncation.py::test_transition_certificate_for_nested_rank2_quotients \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_orbit_table_has_expected_seed_orbits \
  compute/tests/test_scattering_diagram_e1_mc.py::TestThetaFunctionsConifold \
  compute/tests/test_scattering_diagram_e1_mc.py::TestThetaFunctionsLocalP2 \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_compact_hall_construction_package.py::test_full_nerve_theta_contains_all_commuting_equations \
  compute/tests/test_compact_hall_construction_package.py::test_wall_crossing_records_finite_first_limit_data
```

Result:

```text
26 passed in 1.79s
```

One stale selector was tried first:

```text
compute/tests/test_bps_positive_truncation.py::test_transition_certificate_for_nested_rank2_models
```

Pytest reported no such test; the live test name is
`test_transition_certificate_for_nested_rank2_quotients`.

## Files Changed

Only this note:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_04_theta_execution.md
```

No code, TeX, git state, or other notes were edited.

## What Remains

The theta obligation is now a strict point-construction problem:

1. choose a named compact non-toric chamber and one package
   `T in {broken_line, GHKK, GMN, Hall_framed}`;
2. construct the finite package data in every saturated Hall-lower
   quotient;
3. compute `Ob_T`;
4. construct the comparison map to intrinsic Hall theta;
5. compute `Ob_cmp(T,Hall)`;
6. prove finite multiplication equality, including quotient boundary
   zeroing;
7. prove transition naturality and pro-saturation.

The strongest executable route is the Hall-framed package.  It avoids a
cluster seed atlas and spectral cover, but it still demands framed
critical moduli, orientation transport, framed Hall action, OPE/Hall
multiplication, and transition compatibility.  Broken-line, GHKK, and
GMN comparisons remain strictly stronger external enhancements.
