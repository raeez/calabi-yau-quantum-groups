# Agent 01 report: quintic ExCert point obligation

## Scope

Exclusive write scope: this file.

Object attacked: the residual point-construction obligation
`quintic_excert` for the chambered effective BPS positive geometry.

Local anchors read:

- `chapters/theory/bps_positive_geometry_closure.tex:26-78` defines chamber data and finite saturated Hall-lower quotients.
- `chapters/theory/bps_positive_geometry_closure.tex:206-228` proves compact non-toric existence only in the BMS data-realized class.
- `chapters/theory/bps_positive_geometry_closure.tex:231-247` defines `ExCert`.
- `chapters/theory/bps_positive_geometry_closure.tex:249-282` states the quintic certificate as an equivalence to supplied Bridgeland/support/HN, orientation, and motivic data.
- `chapters/theory/bps_positive_geometry_closure.tex:520-658` defines the residual zero-fiber stack and identifies the quintic equation with `o_Ex = 0`.
- `compute/lib/bps_positive_truncation.py:260-303` makes `computed=False` obstruction vectors non-vanishing and prevents schema-as-point collapse.
- `compute/lib/bps_positive_truncation.py:657-688` records the quintic certificate surface as `exact=False`.
- `compute/lib/bps_positive_truncation.py:913-920` records `quintic_excert` with uncomputed coordinates `sigma_support_HN`, `orientation_output`, `motivic_target`.
- `compute/lib/bps_positive_truncation.py:1031-1041` records unresolved named points when a factor is not solved.
- `compute/lib/compact_geometric_koszul_d3.py:279-347` supplies HKR and PTVV input for the quintic.
- `compute/lib/compact_geometric_koszul_d3.py:376-471` proves HKR/PTVV are not enough and names the open Bridgeland/Kapranov route.
- `compute/lib/A_BVDB_quintic_formality.py:361-425` proves the continuous torus route fails for the Fermat quintic.
- `compute/lib/compact_cy3_e1_chain.py:1680-1729` separates source-side open-closed closure from Hall-valued orientation/descent.

## Five attack -> heal cycles

### Cycle 1: Bridgeland/support/HN existence

Attack. The claim "compact non-toric existence" cannot be transported from the BMS class to the quintic. BMS gives actual stability/support data for abelian threefolds and certain quotients, not for `D^b Coh(X_5)`. The quintic has HKR/PTVV surfaces, but no constructed Bridgeland stability condition with support property and HN filtrations in the file anchors above.

Failure mode. Fatal for the assertion "the quintic point exists." Nonfatal for the theorem "the quintic closed zero-fiber substack is defined." The current code correctly keeps `quintic_excert_surface_certificate().exact == False`.

Heal. The surviving theorem is:

For a smooth quintic `X_5`, a strict sector `S`, and a cofinal tower of finite saturated Hall-lower subsets `L_i`, a point of the quintic component of `Sol^BPS` is equivalent to an inverse system of finite witnesses

`(Z_i, P_i, Q_i, HN_i, S_i, o_i, Mot_i, Int_i, Real_i)`

whose restrictions are Mittag-Leffler compatible and whose finite Hall products are quotient products by closed Hall ideals. This is stronger than a vague existence conjecture: it is a necessary-and-sufficient point criterion in finite verifiable coordinates.

### Cycle 2: toric weights and equivariant specialization

Attack. The quintic cannot inherit the toric effective positive geometry by retaining ambient `P^4` torus weights. The Fermat polynomial is preserved by only a finite fifth-root subgroup; the connected torus does not act on `X_5` (`A_BVDB_quintic_formality.py:361-425`). Therefore an oracle slot `T_eq` that secretly means torus localization is false for the quintic.

Failure mode. Fatal for any localization proof using continuous torus fixed weights on `X_5`. Nonfatal for a chambered Hall construction whose `T_eq` is trivial, finite-automorphism, or analytic/Gepner-phase specialization rather than toric localization.

Heal. The quintic ExCert must refine `T_eq` into a tagged finite witness:

`T_eq_mode in {"trivial", "finite_aut", "LG_Gepner", "analytic_period_sector"}`

with `continuous_torus_rank = 0` for the Fermat quintic. Any finite oracle that accepts a nonzero continuous torus-rank matrix for `X_5` must fail.

### Cycle 3: finite Hall-lower truncations

Attack. A rectangular `(N,R)` bound is not a Hall quotient by itself. Without an actual stability condition and HN filtration, the phrase "HN-bounded finite quotient" has no quintic content. A retained extension class may have HN factors outside the visible rectangle unless the retained set is saturated Hall-lower.

Failure mode. Fatal for any finite oracle that stores only charges with `height <= N` and `radius <= R`. Nonfatal for the current manuscript, which now requires finite saturated Hall-lower subsets at `bps_positive_geometry_closure.tex:50-55`.

Heal. The quintic finite oracle should represent each finite stage by:

```text
QuinticFiniteStage {
  charges: finite list of numerical K-classes;
  euler_matrix: exact integer skew/symmetric CY3 Euler data;
  sector_order: rational interval certificate for phase order;
  support_form: exact rational matrix Q on the retained lattice;
  hall_lower_relation: table gamma -> tuple(HN factors);
  retained_is_saturated: boolean checked from the table;
  extension_pairs: finite table (alpha,beta,alpha+beta);
  quotient_ideal_closed: checked predicate;
}
```

Central charges of the quintic need not be rational numbers. The exact rational part is the combinatorial certificate after analytic phase-order comparisons have been isolated by rational intervals with positive separation.

### Cycle 4: PTVV/HKR data versus orientation output

Attack. HKR matching and PTVV shifted symplectic structure are not orientations, not vanishing-cycle data, and not motivic integration. The current local code imports a PTVV/HKR quintic surface, but the point obstruction also needs orientation output and motivic target. There is also a shift bookkeeping hazard: compact Hall moduli require the `(-1)`-shifted critical moduli orientation, while `compact_geometric_koszul_d3.py` records a categorical `(-3)` CY/shifted surface. These are related inputs, not the same coordinate.

Failure mode. Fatal for "PTVV implies oriented Hall integration on the quintic." Nonfatal for the current residual-stack theorem, because `orientation_output` and `motivic_target` remain uncomputed at `bps_positive_truncation.py:917-919`.

Heal. Split the quintic orientation coordinate into four finite oracle slots:

```text
ptvv_critical_shift_minus_one
orientation_square_root
critical_atlas_compatibility
vanishing_cycle_TS_motivic_target
```

The categorical `(-3)` CY trace/HKR surface may feed this package, but it cannot replace it.

### Cycle 5: schema as point

Attack. A derived zero-fiber stack can be exact while having no constructed named point. If the code treats a zero vector with `computed=False` as vanishing, the manuscript falsely solves the quintic.

Failure mode. This would be fatal, but the current implementation blocks it: `ObstructionVector.vanishes` requires both `computed=True` and all zero values (`bps_positive_truncation.py:272-274`), and `SolutionStackFactor.solved` also requires an exact certificate (`bps_positive_truncation.py:297-299`).

Heal. Keep the current schema/point separation. The exact quintic point predicate is:

```text
quintic_point :=
  certificate.name == "quintic_excert_surface"
  and certificate.exact
  and certificate.passed
  and obstruction.computed
  and obstruction.names refine the ExCert coordinates
  and all obstruction values vanish.
```

The present oracle correctly reports the quintic as a closed zero-fiber component, not as a solved point.

### Cycle 6: exact rational encoding of a compact analytic chamber

Attack. A genuine Bridgeland central charge for the quintic is expected to involve periods and wall data, not bare rational numbers. A purely rational matrix cannot honestly encode all analytic phase comparisons unless the analytic comparisons have already been certified.

Failure mode. Fatal for "exact rational oracle proves the quintic Bridgeland chamber." Nonfatal for a finite certifier whose rational layer checks algebraic closure after a separate period-comparison certificate supplies strict inequalities.

Heal. The finite oracle should use two layers:

1. Analytic isolation layer: rational rectangles or intervals isolating the finitely many central-charge values and proving no active ray lies on the sector boundary.
2. Exact Hall layer: integer charges, rational support matrix, orientation signs, motivic Laurent exponents, Hall-lower tables, and exact discrepancy vectors.

The point construction then reduces to finitely many strict inequalities and exact algebraic identities at each retained stage.

## Strongest surviving theorem

The strongest theorem currently supported is not "the quintic point is constructed." It is the following exact conditional theorem.

Let `X_5` be the smooth quintic. Suppose there exists a cofinal inverse system of finite witnesses over saturated Hall-lower subsets `L_i` containing:

- a Bridgeland or explicitly named Hall stability datum with support property;
- certified active-ray-free sector data and HN filtrations for all retained charges;
- quotient-closed Hall extension correspondences;
- the `(-1)`-shifted critical moduli atlas and orientation square-root data;
- a motivic coefficient target compatible with vanishing cycles and Thom-Sebastiani;
- compatible motivic integration and realization maps;
- transition maps preserving all obstruction coordinates.

Then these witnesses define an actual point of the quintic component of `Sol^BPS`; conversely, an actual point of that component restricts to such a witness at every finite Hall-lower stage. This is a strict equivalence between the point problem and finite ExCert data, not a status downgrade.

## Exact obstruction coordinates to compute

Current coarse code coordinates:

- `sigma_support_HN`
- `orientation_output`
- `motivic_target`

Required refinement for the quintic point:

- `Z_period_isolation`: central charges for retained quintic classes isolated by certified rational intervals.
- `support_Q`: exact support form with support-property inequality on retained charges.
- `active_sector`: sector boundary contains no active ray.
- `HN_filtration_table`: HN factors supplied for retained classes.
- `hall_lower_saturation`: retained set is saturated under those HN factors.
- `extension_closed_ideal`: complement generates a closed two-sided Hall ideal.
- `ptvv_critical_atlas`: `(-1)`-shifted critical atlas for the relevant moduli chart.
- `orientation_square_root`: Joyce-Kontsevich orientation square roots.
- `vanishing_cycle_TS`: Thom-Sebastiani compatibility for vanishing cycles.
- `motivic_target`: target category/ring and integration map.
- `realization_maps`: Euler/Hodge/numerical realizations compatible with transition maps.
- `ML_transition`: cofinal Mittag-Leffler compatibility across finite stages.
- `T_eq_mode`: trivial/finite/analytic specialization, with continuous torus-rank zero for the Fermat quintic.

## Proposed finite oracle representation

```python
@dataclass(frozen=True)
class QuinticExCertStage:
    stage_id: tuple[int, int]
    charges: tuple[Charge, ...]
    euler_matrix: tuple[tuple[int, ...], ...]
    central_charge_boxes: tuple[tuple[Fraction, Fraction, Fraction, Fraction], ...]
    phase_order_certificate: tuple[tuple[int, int, str], ...]
    support_matrix: tuple[tuple[Fraction, ...], ...]
    sector: tuple[Fraction, Fraction]
    active_ray_free: bool
    hn_factors: dict[Charge, tuple[Charge, ...]]
    hall_lower_saturated: bool
    extension_pairs: tuple[tuple[Charge, Charge, Charge], ...]
    quotient_ideal_closed: bool
    ptvv_critical_shift_minus_one: bool
    orientation_square_root: bool
    critical_atlas_compatible: bool
    vanishing_cycle_TS: bool
    motivic_target: str
    realization_maps: tuple[str, ...]
    transition_parent: tuple[int, int] | None
    transition_compatible: bool
    T_eq_mode: str
    continuous_torus_rank: int
```

Predicate:

```text
quintic_stage_passes =
  active_ray_free
  and hall_lower_saturated
  and quotient_ideal_closed
  and ptvv_critical_shift_minus_one
  and orientation_square_root
  and critical_atlas_compatible
  and vanishing_cycle_TS
  and motivic_target != ""
  and transition_compatible
  and continuous_torus_rank == 0
```

The inverse system gives the point only when every cofinal stage passes and the transition maps are Mittag-Leffler compatible.

## Commands run

Targeted regression slice:

```text
pytest -q compute/tests/test_bps_positive_truncation.py::test_quintic_excert_surface_certificate \
  compute/tests/test_bps_positive_truncation.py::test_obstruction_zero_certificate_detects_uncomputed_coordinates \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_compact_cy3_e1_chain.py::TestCompactCY3OpenClosedBridge::test_quintic_source_bridge_closed_with_source_data \
  compute/tests/test_compact_cy3_e1_chain.py::TestCompactCY3OpenClosedBridge::test_quintic_missing_anomaly_cancellation_is_source_obstruction
```

Result:

```text
6 passed in 0.29s
```

Direct certificate inspection:

```text
quintic_excert_surface True False 5 ()
quintic_excert False True ('sigma_support_HN', 'orientation_output', 'motivic_target') False
uncomputed entries: sigma_support_HN, orientation_output, motivic_target
constructed_named_points: passed False, exact False; quintic_excert remains unresolved
```

## Files changed

- `notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_01_quintic_excert.md`

No code or TeX was edited.

## Remaining quintic point-construction obligations

The quintic closed substack is well-defined. The actual quintic point remains exactly the computation and gluing of:

1. a Bridgeland/support/HN finite-stage inverse system on `D^b Coh(X_5)`;
2. certified active-ray-free sectors and saturated Hall-lower truncations;
3. orientation square roots for the PTVV `(-1)`-shifted critical Hall moduli;
4. vanishing-cycle and Thom-Sebastiani compatible motivic integration;
5. a non-toric specialization mode with continuous torus rank zero;
6. cofinal Mittag-Leffler transition compatibility;
7. exact oracle discrepancies proving every refined coordinate above is computed and zero.

