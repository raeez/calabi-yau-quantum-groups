# Agent 01 wave 3: quintic ExCert execution

## Scope

Exclusive write scope: this file.

Object attacked: the remaining quintic point obligation inside the
residual chambered BPS-positive solution stack.

Current local anchors:

- `chapters/theory/bps_positive_geometry_closure.tex:206`: compact
  non-toric existence is proved only for the BMS data-realized class.
- `chapters/theory/bps_positive_geometry_closure.tex:231`: `ExCert` is
  the compact chamber existence package.
- `chapters/theory/bps_positive_geometry_closure.tex:249`: the quintic
  theorem is equivalent to supplying actual Bridgeland/support/HN data,
  orientation output, and motivic data.
- `chapters/theory/bps_positive_geometry_closure.tex:552`: the residual
  solution stack is a derived zero fiber.
- `chapters/theory/bps_positive_geometry_closure.tex:589`: the quintic
  coordinate is `o_Ex`.
- `compute/lib/bps_positive_truncation.py:664`: the quintic surface
  certificate is a ledger, not an unconditional realization.
- `compute/lib/bps_positive_truncation.py:973`: the `quintic_excert`
  factor uses the remaining-gate coordinate list and is `computed=False`.
- `compute/lib/bps_positive_remaining_gates.py:26`: the executable
  quintic gate has 13 required coordinates.
- `compute/tests/test_bps_positive_remaining_gates.py:31`: tests pin the
  13-coordinate quintic gate.
- `compute/lib/compact_geometric_koszul_d3.py:279`: HKR matching for
  the quintic is proved only as a necessary surface.
- `compute/lib/compact_geometric_koszul_d3.py:376`: HKR does not imply
  the compact chain-level/Kapranov/Bridgeland witness.
- `compute/lib/A_BVDB_quintic_formality.py:361`: the ambient torus of
  `P^4` does not preserve the Fermat quintic.
- `compute/lib/A_BVDB_quintic_formality.py:377`: the continuous
  automorphism torus rank of the Fermat quintic is zero.
- `chapters/theory/cy_to_chiral.tex:11959`: scalar quintic shadow
  calculations do not construct the quintic `Phi_3` output.

## Claim Attacked

The false claim to destroy is:

```text
PTVV + HKR + finite truncation data construct an actual quintic
ExCert point of Sol^BPS.
```

This claim is false.  PTVV gives the shifted symplectic surface on
`Perf(X_5)`.  HKR gives the Hochschild dimension vector
`(1, 0, 101, 4, 101, 0, 1)` and total `208`.  Neither datum constructs
a Bridgeland stability condition on `D^b Coh(X_5)`, a support form, HN
tables, active-ray isolation, orientation square roots, vanishing-cycle
Thom-Sebastiani motivic integration, or a cofinal Mittag-Leffler tower
of saturated Hall-lower quotients.

The current oracle correctly blocks the collapse: `quintic_excert` is a
closed zero-fiber component, not a solved point.

## Attack -> Heal Cycles

### Cycle 1: Bridgeland/support/HN witness

Attack.  BMS compact non-toric existence cannot be transported to the
quintic.  Bayer--Macri--Stellari supply stability/support in their
abelian-threefold and quotient class; the quintic line has no
constructed Bridgeland stability condition with support property and HN
filtrations in the local anchors.

Falsifier.  `quintic_excert_surface_certificate()` passes as a ledger
but has `exact=False`; `constructed_named_points_certificate()` records
`quintic_excert` as unresolved.

Heal.  The point statement is the finite witness theorem: a quintic
point is equivalent to a cofinal inverse system of finite witnesses
`(Z_i, P_i, Q_i, HN_i, S_i, o_i, Mot_i, Int_i, Real_i)` over saturated
Hall-lower sets, with transition maps preserving every coordinate.  No
single HKR/PTVV datum is allowed to stand in for this inverse system.

### Cycle 2: analytic period isolation

Attack.  A finite oracle cannot store an analytic Bridgeland central
charge as if it were an exact rational vector unless the required phase
inequalities have already been isolated.

Falsifier.  Central charges for a compact quintic chamber are period
data.  Exact arithmetic can verify the finite Hall algebra after the
period comparisons have been certified; it does not by itself prove the
sector is active-ray-free.

Heal.  Add the period-isolation layer to the finite witness.  For every
retained charge `gamma`, the witness supplies a rational box in `C`
containing `Z(gamma)`, disjoint from zero and from sector boundaries.
For each pair of retained active charges, rational interval separation
certifies the phase order.  The exact Hall layer starts only after
these analytic inequalities are certified.

### Cycle 3: continuous torus rank zero

Attack.  The quintic cannot be solved by importing the toric effective
positive geometry of the ambient `P^4`.  The ambient `(C^*)^4` action
does not preserve the Fermat equation except at fifth roots.

Falsifier.  `torus_action_preserves_quintic()` returns `False`;
`quintic_continuous_symmetry_group()` records
`max_torus_dim_acting = 0`; Calaque-Halbout-Felder formality does not
apply.

Heal.  The `T_eq_mode` coordinate is structured data:

```text
T_eq_mode = (mode, continuous_torus_rank, specialization_certificate)
mode in {"trivial", "finite_aut", "LG_Gepner", "analytic_period_sector"}
continuous_torus_rank = 0
```

Any proposed quintic ExCert with positive continuous torus rank fails
the finite gate.  This is stronger than saying "non-toric": it is an
executable exclusion of the toric degeneration proof.

### Cycle 4: Hall-lower saturation and quotient ideal

Attack.  A rectangular `(N,R)` truncation is not a Hall quotient.
If `gamma` is retained and has HN factors outside the retained set, the
finite Hall product is not closed.  If the omitted complement is not a
closed two-sided Hall ideal, quotient-zeroing can change associativity.

Falsifier.  The proof of the finite-first theorem uses saturated
Hall-lower subsets, not raw rectangles.  The current oracle contains
ambient-aware lower-set and quotient associativity checks; the quintic
point must supply the HN table those checks act on.

Heal.  The finite quintic stage includes:

```text
hn_factors: gamma -> tuple[gamma_j, ...]
hall_lower_saturation: every gamma_j lies in L_i
extension_pairs: finite table (alpha, beta, alpha + beta)
extension_closed_ideal: complement is a closed Hall ideal
```

The obstruction coordinates `HN_filtration_table`,
`hall_lower_saturation`, and `extension_closed_ideal` vanish only after
these tables are supplied and checked.

### Cycle 5: orientation square root

Attack.  PTVV shifted symplectic structure does not choose an
orientation.  The determinant-line square root and its Cech descent are
separate data, and a nontrivial but closed orientation gerbe must be
kept as coefficient data rather than erased.

Falsifier.  The current orientation oracle permits gerbe-twisted
orientation output.  The quintic point gate still records
`orientation_square_root` as uncomputed.

Heal.  The quintic orientation witness is:

```text
orientation_square_root:
  determinant_line = det REnd(E)
  local_square_roots: sqrt(det REnd(E)) on the critical atlas
  cech_cocycle: F_2-valued descent class
  quadratic_refinement: q(alpha + beta)
    = (-1)^{chi(alpha,beta)} q(alpha) q(beta)
```

The coordinate vanishes when the local roots glue, or when the
nontrivial closed gerbe is explicitly retained as the Hall coefficient
system and all products are computed in that twisted system.

### Cycle 6: motivic target and vanishing-cycle products

Attack.  HKR and PTVV do not define motivic integration.  A Hall product
requires vanishing cycles, orientation factors, and Thom-Sebastiani
compatibility over the retained critical atlas.

Falsifier.  The executable quintic factor has uncomputed
`vanishing_cycle_TS`, `motivic_target`, and `realization_maps`
coordinates.  The source-side compact CY3 open-closed bridge is not the
Hall-valued orientation/motivic comparison.

Heal.  The finite stage must supply a target `Mot_i`, a map
`Int_i` from oriented critical stacks to `Mot_i`, and realization maps
to Euler/Hodge/numerical shadows.  The multiplication certificate is the
commutative square expressing Thom-Sebastiani compatibility for every
retained extension pair.

### Cycle 7: Mittag-Leffler transitions

Attack.  Even if each finite stage passes, unrelated finite stages do
not define a completed quintic point.  The pro-object requires
transition compatibility and eventual stabilization of finite
coordinate images.

Falsifier.  The residual solution stack is completed as an inverse
limit.  A single finite witness cannot be promoted to `Sol^BPS` without
cofinal transition control.

Heal.  The `ML_transition` coordinate consists of transition maps
`r_{j,i}: L_j -> L_i` for `j >= i`, quotient maps by closed Hall ideals,
preservation of central-charge boxes, HN tables, orientation data,
motivic integration, and realization maps, plus the finite
Mittag-Leffler condition on the image of every coordinate set.

## Healed Theorem

Theorem.  Let `X_5` be a smooth quintic threefold.  Fix a strict sector
symbol `S` and a cofinal tower of finite saturated Hall-lower charge
sets `L_i`.  A point of the quintic component of `Sol^BPS` is
equivalent to a compatible inverse system of finite quintic ExCert
stages

```text
W_i =
(L_i, Z_i, phase_i, Q_i, HN_i, Hall_i, PTVV_i, orient_i,
 Mot_i, Int_i, Real_i, T_eq_i)
```

such that the 13-coordinate obstruction vector below is computed and
zero at every stage and is preserved by the transition maps.  Conversely,
any point of the quintic component restricts to such a finite witness at
every `L_i`.

This theorem is stronger than a status statement: it is a necessary and
sufficient finite point criterion.  It does not prove nonemptiness of
the quintic component; it makes nonemptiness equivalent to explicit
finite data whose coordinates are independently checkable.

Proof sketch.  The forward direction restricts a point of the derived
zero fiber to each finite Hall-lower quotient, giving chamber data,
orientation output, motivic coefficients, and compatible transition
maps.  Since the point lies over zero, each obstruction coordinate is
computed and vanishes.  The reverse direction forms the finite
chambered Hall cosheaf at each stage.  Hall-lower saturation and
closed-ideal quotienting give finite associativity.  Period isolation
gives active-ray-free sector order.  Orientation and Thom-Sebastiani
data give the motivic Hall product.  The Mittag-Leffler transition
coordinate identifies the inverse system, hence defines the completed
point in `Sol^BPS`.

## Exact Quintic Obstruction Vector

Current executable vector:

```text
QUINTIC_EXCERT_COORDINATES = (
  "Z_period_isolation",
  "support_Q",
  "active_sector",
  "HN_filtration_table",
  "hall_lower_saturation",
  "extension_closed_ideal",
  "ptvv_critical_atlas",
  "orientation_square_root",
  "vanishing_cycle_TS",
  "motivic_target",
  "realization_maps",
  "ML_transition",
  "T_eq_mode",
)
```

Coordinate meanings:

- `Z_period_isolation`: rational boxes for retained central charges.
- `support_Q`: exact support form and finite support inequality.
- `active_sector`: sector boundary avoids all retained active rays.
- `HN_filtration_table`: retained HN factors for every retained charge.
- `hall_lower_saturation`: retained set contains all HN factors.
- `extension_closed_ideal`: omitted complement is a closed Hall ideal.
- `ptvv_critical_atlas`: `(-1)`-shifted critical atlas for Hall moduli,
  derived from the `(-3)` CY/PTVV source with the correct moduli shift.
- `orientation_square_root`: determinant-line square-root or retained
  closed gerbe coefficient system.
- `vanishing_cycle_TS`: Thom-Sebastiani compatibility of vanishing cycles.
- `motivic_target`: target ring/category for motivic integration.
- `realization_maps`: Euler/Hodge/numerical realizations commute with
  finite products and transitions.
- `ML_transition`: cofinal transition and Mittag-Leffler compatibility.
- `T_eq_mode`: non-toric specialization tag; for Fermat quintic it
  includes continuous torus rank zero.

## Proposed Dataclass And Certificate Signatures

```python
@dataclass(frozen=True)
class PeriodBox:
    charge: Charge
    real_min: Fraction
    real_max: Fraction
    imag_min: Fraction
    imag_max: Fraction
    avoids_zero: bool
    avoids_sector_boundary: bool


@dataclass(frozen=True)
class QuinticExCertStage:
    stage_id: tuple[int, int]
    charges: tuple[Charge, ...]
    euler_matrix: tuple[tuple[int, ...], ...]
    period_boxes: tuple[PeriodBox, ...]
    phase_order_certificate: tuple[tuple[Charge, Charge, Literal["<", ">"]], ...]
    support_matrix: tuple[tuple[Fraction, ...], ...]
    support_kernel_negative: bool
    active_sector: tuple[Fraction, Fraction]
    hn_factors: Mapping[Charge, tuple[Charge, ...]]
    extension_pairs: tuple[tuple[Charge, Charge, Charge], ...]
    ptvv_critical_atlas: bool
    orientation_square_root: bool
    orientation_gerbe_retained: bool
    vanishing_cycle_TS: bool
    motivic_target: str
    realization_maps: tuple[str, ...]
    transition_parent: tuple[int, int] | None
    transition_compatible: bool
    T_eq_mode: Literal["trivial", "finite_aut", "LG_Gepner", "analytic_period_sector"]
    continuous_torus_rank: int
```

```python
def quintic_period_isolation_certificate(stage: QuinticExCertStage) -> Certificate: ...
def quintic_support_hn_certificate(stage: QuinticExCertStage) -> Certificate: ...
def quintic_hall_lower_certificate(stage: QuinticExCertStage) -> Certificate: ...
def quintic_orientation_certificate(stage: QuinticExCertStage) -> Certificate: ...
def quintic_motivic_ts_certificate(stage: QuinticExCertStage) -> Certificate: ...
def quintic_transition_certificate(
    small: QuinticExCertStage,
    big: QuinticExCertStage,
) -> Certificate: ...
def quintic_excert_point_certificate(
    tower: tuple[QuinticExCertStage, ...],
) -> Certificate: ...
```

Acceptance predicate:

```text
quintic_excert_point_certificate(tower).passed
iff
  every stage computes all 13 coordinates,
  every coordinate vanishes at that stage,
  continuous_torus_rank = 0 at every quintic stage,
  transitions preserve all coordinates,
  the tower is cofinal and Mittag-Leffler.
```

## Commands Run

Targeted regression slice:

```text
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py::test_quintic_excert_surface_certificate \
  compute/tests/test_bps_positive_truncation.py::test_obstruction_zero_certificate_detects_uncomputed_coordinates \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_compact_cy3_e1_chain.py::TestCompactCY3OpenClosedBridge::test_quintic_source_bridge_closed_with_source_data \
  compute/tests/test_compact_cy3_e1_chain.py::TestCompactCY3OpenClosedBridge::test_quintic_missing_anomaly_cancellation_is_source_obstruction
```

Result:

```text
6 passed in 0.30s
```

Remaining-gate regression slice:

```text
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_remaining_gates.py \
  compute/tests/test_bps_positive_truncation.py::test_quintic_excert_surface_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points
```

Result:

```text
9 passed in 0.43s
```

Direct clean probe:

```text
quintic_surface True False 5 ()
quintic_factor False True
  ('Z_period_isolation', 'support_Q', 'active_sector',
   'HN_filtration_table', 'hall_lower_saturation',
   'extension_closed_ideal', 'ptvv_critical_atlas',
   'orientation_square_root', 'vanishing_cycle_TS', 'motivic_target',
   'realization_maps', 'ML_transition', 'T_eq_mode')
  computed=False
constructed_points False False ['quintic_excert']
hkr True [1, 0, 101, 4, 101, 0, 1] 208
ptvv True -3
hkr_implies_koszul False OPEN
routes {'route_BCOV': 'OPEN', 'route_LG_mirror': 'OPEN',
        'route_Bridgeland_stability': 'OPEN'}
torus False False 0
```

One preliminary direct probe exited with code `1` after printing the
same certificate data because it asked for stale formality keys.  The
clean probe above is the checkable run.

## Files Changed

- `notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_01_quintic_excert_execution.md`

No code, TeX, git state, or other notes were edited by this agent.

## What Remains

The quintic closed substack is exact.  The actual point remains the
construction of a cofinal tower of `QuinticExCertStage` witnesses whose
13 obstruction coordinates are computed and zero.  The mathematically
hard first coordinate is still the Bridgeland/support/HN chamber on
`D^b Coh(X_5)`, with analytic period isolation and support property.
After that, the remaining point obligations are Hall-lower saturation,
orientation square root or retained gerbe coefficients, motivic
Thom-Sebastiani integration, non-toric specialization with continuous
torus rank zero, and Mittag-Leffler transition compatibility.
