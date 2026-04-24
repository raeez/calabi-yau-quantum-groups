# Agent 04: theta package attack and heal

## Claim Attacked

The theta-enhancement lane for non-toric BPS-positive chambers has two
separate layers:

1. the intrinsic finite Hall theta package
   `theta_p^{lambda,c}=Phi_KS(b->c)(x_p)`;
2. comparison with external broken-line, GHKK, GMN, or framed Hall
   factorization packages.

The first layer survives as a finite theorem.  The second layer is not a
single scalar obstruction.  It is a package-indexed zero-fiber problem.

Local anchors:

- `chapters/theory/bps_positive_geometry_closure.tex:388-421` proves the
  intrinsic Hall theta package from finite KS transport and identity
  joint holonomy.
- `chapters/theory/bps_positive_geometry_closure.tex:424-435` states the
  comparison corollary with broken-line, GHKK, and GMN package
  obstruction vectors.
- `chapters/theory/bps_positive_geometry_closure.tex:566-567` inserts
  `o_theta^{pkg}` into the residual obstruction map.
- `chapters/theory/bps_positive_geometry_closure.tex:638-646` identifies
  the theta coordinate as the package-indexed existence and comparison
  vector, and says actual points require computed vanishing.
- `compute/lib/bps_positive_truncation.py:732-757` implements the finite
  Hall theta certificate.  It is a passed but non-exact comparison
  ledger.
- `compute/lib/bps_positive_truncation.py:943-960` encodes the theta
  zero-fiber factor by nine uncomputed coordinates.
- `compute/lib/scattering_diagram_e1_mc.py:1145-1185` computes theta
  functions from an MC scattering solution in finite local models.
- `compute/lib/c3_hcs_hall_theta.py:120-147` gives the abelian torus-fixed
  `C^3` hCS-Hall-theta finite-mode witness.

## Package-Indexed Obstruction Vector

The current correct top-level finite vector is

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

The coordinates expand as follows when a package is supplied:

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
)
```

where the terms mean finite local wall support, identity joint holonomy,
strict height growth, finite bending, orientation and half-Tate
compatibility, triangular leading monomial, and saturated theta labels.

```text
Ob_GHKK =
(
  o_atlas,
  o_scatter,
  o_EGM,
  o_upper,
  o_orient,
  o_mut,
  o_comp
)
```

where the terms mean a cluster seed atlas, Hall-cluster scattering
identification, enough-global-monomials or stronger basis hypothesis,
the correct upper/regular algebra target, orientation and skew-form
match, mutation compatibility, and completion compatibility.

```text
Ob_GMN =
(
  o_cover,
  o_period,
  o_sector,
  o_detour,
  o_2d4d,
  o_halo,
  o_framed,
  o_spin,
  o_abel,
  o_OPE,
  o_comp
)
```

where the terms mean spectral cover, central-charge period equality,
sector dependence, finite detour sums, 2d-4d wall crossing, halo/Hall
identification, enough framed lines, spin/orientation match,
abelianization descent, OPE closure, and completion compatibility.

```text
Ob_Hall-fr =
(
  o_fr,
  o_crit_fr,
  o_or_fr,
  o_act,
  o_finite_fr,
  o_tri_fr,
  o_OPE,
  o_real_fr
)
```

where the terms mean framed objects, framed critical stacks, orientation
transport, framed Hall action, finite truncation, triangularity, OPE/Hall
compatibility, and realization compatibility.

The package-to-Hall comparison vector is

```text
Ob_cmp(T,Hall) =
(
  o_core,
  o_wall,
  o_orient,
  o_Tate,
  o_loc,
  o_mult,
  o_pro
).
```

## Attack -> Heal Cycles

### Cycle 1: broken-line existence

Attack.  A Hall scattering diagram does not automatically give a
broken-line basis.  Local finiteness, finite bending, strict height
growth, and triangularity are extra conditions; without them, broken
lines can accumulate, fail to terminate in a finite quotient, or lose
the leading monomial needed for a basis.

Heal.  In a finite saturated Hall-lower quotient, broken-line theta
functions are theorem-grade only on the zero fiber of `Ob_bl`.  Then
finite nilpotence bounds wall factors, strict height prevents infinite
descent, and triangularity gives a basis by induction on height.  The
intrinsic Hall theta package supplies the KS transport; the broken-line
package supplies the geometric expansion model.

### Cycle 2: GHKK package hypotheses

Attack.  GHKK theta functions require a cluster or cluster-like atlas,
scattering diagram, theta-basis hypothesis, and an algebra target.  None
of those follows from an arbitrary compact CY3 Hall chamber.

Heal.  GHKK comparison is valid on the zero fiber of `Ob_GHKK` plus
`Ob_cmp(GHKK,Hall)`.  A seed atlas identifies a primitive charge
sublattice with the Hall lattice, `Psi_Hall-cl` identifies wall
functions and skew forms, EGM or a stronger basis hypothesis gives the
GHKK theta basis, and completion compatibility passes the equality to
the inverse limit.

### Cycle 3: GMN/Riemann-Hilbert package

Attack.  A GMN package is not just KS wall crossing.  It needs a
spectral cover, central-charge periods, spectral networks, detours,
2d-4d wall crossing, halo rules, framed line defects, spin refinements,
abelianization, OPE, and completion.  A compact CY3 chamber need not
come from class-S or from a known Hitchin system.

Heal.  The GMN theorem target is conditional but sharp: if `Ob_GMN=0`
and `Ob_cmp(GMN,Hall)=0`, framed line generating functions are theta
functions in the same finite motivic quantum torus and jump by the same
Hall KS automorphisms.  This converts the GMN Riemann-Hilbert package
into a genuine point of the theta zero fiber, not an analogy.

### Cycle 4: intrinsic Hall factorization

Attack.  The formula `Phi_KS(b->c)(x_p)` gives a transported monomial
basis in a finite quantum torus.  It does not by itself construct
framed Hall modules, defect OPE, or a geometric factorization theta
basis.

Heal.  Separate the thin intrinsic transport theorem from the framed
Hall-factorization theorem.  The thin theorem is already proved by
finite Hall associativity, sector descent, and identity joint holonomy.
The framed theorem is a stronger point-construction problem with
obstruction vector `Ob_Hall-fr`; vanishing constructs theta functions as
framed motivic Hall characters and multiplication as framed OPE.

### Cycle 5: wall-function identification

Attack.  Equality of theta packages can fail even when two scattering
diagrams have the same support.  Wall functions may differ by motivic
normalization, Euler specialization, BCH approximation, sign, or
half-Tate convention.  The local scattering engines explicitly warn
that BCH forced multiplicities are not DT invariants at higher heights.

Heal.  Comparison must include `o_wall`, `o_orient`, and `o_Tate`.
The finite Hall comparison uses motivic quantum dilogarithm wall factors
and the orientation cocycle from the Hall product; external packages
must identify their wall factors with these after the chosen realization
and normalization.  BCH or local toy multiplicities are evidence only
for qualitative walls unless lifted to the motivic quantum torus.

### Cycle 6: multiplication and pro-saturation

Attack.  Matching individual theta functions does not prove equality of
theta algebras.  Multiplication can leave the label set, sector
restriction can drop cores, and inverse-limit transition maps can fail
to preserve package data.

Heal.  Add `o_mult` and `o_pro`.  A package comparison is an algebra
isomorphism only when pair-of-pants, broken-line pairs, cluster
multiplication, or framed OPE correspondences match Hall convolution and
when the theta labels form a saturated finite lower set under
multiplication.  Pro-comparison is the inverse limit of these finite
algebra comparisons, not a formal completion of a single quotient.

## Strongest Surviving Theorem

Finite intrinsic theorem.  In a finite saturated Hall-lower quotient
with support property, Hall associativity, HN sector descent, compatible
orientation, and identity KS holonomy around every retained joint, the
elements

```text
theta_p^{lambda,c} = Phi_KS(b->c)(x_p)
```

are path-independent and multiply by the oriented Hall quantum-torus
rule.  This is the strongest unconditional theorem currently supported
by the oracle.

External comparison theorem.  Let
`T in {bl, GHKK, GMN, Hall-fr}` be an external theta package over the
same finite chamber datum.  Then

```text
Theta_T^{lambda,b} = Theta_Hall^{lambda,b}
```

as finite theta algebras if and only if the package-existence vector
`Ob_T` vanishes and the comparison vector `Ob_cmp(T,Hall)` vanishes.
The completed comparison exists if these finite equalities are natural
under the saturated Hall-lower transition maps.  A non-toric compact
theta enhancement is therefore an actual point of this zero fiber.

## Exact Finite Oracle Encoding

The current oracle correctly records:

- `theta_comparison_certificate(bound)` as a passed, non-exact finite
  Hall theta and comparison-slot ledger;
- `derived_solution_stack_factors(bound)["theta_comparison"]` with the
  nine-coordinate top-level vector above;
- `ObstructionVector.vanishes` as false when the vector is uncomputed,
  even if all placeholder values are zero;
- `constructed_named_points_certificate(bound)` as failing until the
  theta package obstruction coordinates are computed and vanish.

The exact next oracle upgrade is not a new scalar test.  It is a family

```text
theta_package_obstruction_certificate(package, bound)
```

returning `Ob_bl`, `Ob_GHKK`, `Ob_GMN`, or `Ob_Hall-fr`, together with

```text
theta_package_comparison_certificate(package, bound)
```

returning `Ob_cmp(package,Hall)`.  The top-level
`theta_comparison` factor should pass as a constructed point only after
one package certificate and its comparison certificate are exact,
computed, and zero in every retained finite quotient.

## Computational Checks Available Now

Commands run:

```bash
python3 - <<'PY'
from compute.lib.bps_positive_truncation import TruncationBound, derived_solution_stack_factors, theta_comparison_certificate, obstruction_zero_certificate
b = TruncationBound(5, 6, 1)
c = theta_comparison_certificate(b)
print(c.name, c.passed, c.exact, c.checked_items, c.discrepancies)
for f in derived_solution_stack_factors(b):
    if f.name == 'theta_comparison':
        print(f.obstruction.names)
        print(f.obstruction.computed, f.obstruction.vanishes)
        print(obstruction_zero_certificate('theta_comparison', f.obstruction).discrepancies)
PY
```

Output:

```text
theta_comparison True False 318 ()
('hall_joint_holonomy', 'broken_line_package', 'GHKK_package', 'GMN_package', 'core_charge_identification', 'wall_function_identification', 'orientation_half_tate_match', 'multiplication_comparison', 'pro_saturation')
False False
({'obstruction': 'hall_joint_holonomy', 'value': 'uncomputed'}, {'obstruction': 'broken_line_package', 'value': 'uncomputed'}, {'obstruction': 'GHKK_package', 'value': 'uncomputed'}, {'obstruction': 'GMN_package', 'value': 'uncomputed'}, {'obstruction': 'core_charge_identification', 'value': 'uncomputed'}, {'obstruction': 'wall_function_identification', 'value': 'uncomputed'}, {'obstruction': 'orientation_half_tate_match', 'value': 'uncomputed'}, {'obstruction': 'multiplication_comparison', 'value': 'uncomputed'}, {'obstruction': 'pro_saturation', 'value': 'uncomputed'})
```

```bash
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_theta_comparison_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_orbit_table_has_expected_seed_orbits \
  compute/tests/test_c3_hcs_hall_theta.py
```

Result:

```text
12 passed in 0.90s
```

```bash
pytest -q \
  compute/tests/test_scattering_diagram_e1_mc.py::TestThetaFunctionsConifold \
  compute/tests/test_scattering_diagram_e1_mc.py::TestThetaFunctionsLocalP2
```

Result:

```text
9 passed in 0.74s
```

These checks prove finite Hall transport, rank-two scattering witnesses,
local theta leading terms/corrections, and abelian `C^3` hCS-Hall-theta
shuffle localization.  They do not construct a compact non-toric
broken-line/GHKK/GMN package point.

## Files Changed

Only this note:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_04_theta_package.md
```

No code or TeX files were edited.

## Remaining Point-Construction Obligations

The remaining theta obligation is exact:

1. choose a named non-toric BPS-positive chamber and a package
   `T in {bl, GHKK, GMN, Hall-fr}`;
2. construct the finite package data in every saturated Hall-lower
   quotient;
3. compute `Ob_T`;
4. construct the comparison datum to the intrinsic Hall package;
5. compute `Ob_cmp(T,Hall)`;
6. prove finite multiplication compatibility;
7. prove naturality under the pro-system.

The smallest fully executable compact target is likely the intrinsic
framed Hall package, because it does not require a cluster atlas or
spectral cover.  The smallest external comparison target remains a
cluster or spectral-network locus where the charge lattice, central
charge, wall functions, orientation character, half-Tate normalization,
and multiplication correspondences can be written explicitly.
