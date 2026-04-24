# Agent 06 Integration Execution Attack, Wave 3

Date: 2026-04-24.

Scope read: `chapters/theory/bps_positive_geometry_closure.tex`,
`compute/lib/bps_positive_truncation.py`,
`compute/tests/test_bps_positive_truncation.py`, `main.tex`,
`compute/lib/hall_borcherds_gate.py`,
`compute/lib/cy3_dwr_descent_gate.py`, the wave-2 reports, and the
BPS-positive synthesis notes.  Write scope honored: only this report was
changed.

Verdict: the source object is now stable.  The remaining execution
problem is stricter: the oracle must expose witness objects for the five
named closed substacks without converting any uncomputed coordinate into
a point.  The next increase in strength is a finite witness-checker
layer, not another status sentence.

## Verification Commands Run

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py \
  compute/tests/test_cy3_dwr_descent_gate.py \
  compute/tests/test_hall_borcherds_gate.py \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_orbit_table_has_expected_seed_orbits

73 passed in 2.00s
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile \
  compute/lib/bps_positive_truncation.py \
  compute/lib/cy3_dwr_descent_gate.py \
  compute/lib/hall_borcherds_gate.py

passed
```

```text
derived True True
seven True False
constructed False False 5
compact_nontoric_bms cert_exact=True computed=True solved=True coords=3
quintic_excert cert_exact=False computed=False solved=False coords=3
schoen_banana_gluing cert_exact=False computed=False solved=False coords=6
k3e_raw_radical cert_exact=False computed=False solved=False coords=7
theta_comparison cert_exact=False computed=False solved=False coords=9
hcs_named_zero_fiber cert_exact=False computed=False solved=False coords=14
```

Hygiene scans:

```text
rg -n -P '\\kappa(?!_)|bare kappa|bare \\kappa' \
  chapters/theory/bps_positive_geometry_closure.tex \
  compute/lib/bps_positive_truncation.py \
  compute/tests/test_bps_positive_truncation.py \
  main.tex \
  notes/bps_positive_geometry_total_resolution_20260424/platonic_closure_20260424.md \
  notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md

no hits
```

```text
rg -n '\b(Wave|round|batch|AP-CY|Pattern|cache entry|notably|crucially|moreover|furthermore|let us now|we now turn|having established)\b' \
  chapters/theory/bps_positive_geometry_closure.tex

no hits
```

`make fast` was not run in this lane because the assigned write scope is
a note and the build writes shared auxiliary/PDF surfaces during
concurrent work.  The inclusion remains source-visible at `main.tex:1821`.

## ATTACK 1 -> HEAL 1: the point gate is correct, but the witness layer is missing

Defect.  `constructed_named_points_certificate()` correctly fails with
five unresolved factors, and `SolutionStackFactor.solved` requires
`certificate.exact`, `certificate.passed`, and computed vanishing
obstructions.  But there is no executable object a future worker can
fill in to convert a closed substack into a point.  The only available
objects are coarse ledgers:

- `compute/lib/bps_positive_truncation.py:967`: residual factors.
- `compute/lib/bps_positive_truncation.py:1097`: constructed-points gate.
- `compute/tests/test_bps_positive_truncation.py:448`: unresolved factors
  are asserted only by name.

Heal.  Add a witness-checker layer without changing the truth value of
any current example:

```python
@dataclass(frozen=True)
class NamedPointWitness:
    name: str
    certificate: Certificate
    obstruction: ObstructionVector
    transition: Certificate | None = None

def named_point_certificate(witness: NamedPointWitness) -> Certificate:
    ...
```

The certificate may pass only when every component certificate is exact,
the obstruction vector is computed, every coordinate is zero, and
transition/pro-completion compatibility passes.  Add a test that the
current five witness stubs fail and that the BMS data-realized witness is
the only solved point.

## ATTACK 2 -> HEAL 2: quintic and Schoen coordinates are still too coarse

Defect.  Wave-2 refined the quintic point into thirteen finite
coordinates and the Schoen point into nine compact gluing coordinates,
but the executable factors still expose only three and six:

- `compute/lib/bps_positive_truncation.py:979`: quintic names
  `sigma_support_HN`, `orientation_output`, `motivic_target`.
- `compute/lib/bps_positive_truncation.py:988`: Schoen names
  `charge_pushforward`, `compact_support_BC`, `overlap_orientation`,
  `HN_overlap`, `motivic_overlap`, `pro_continuity`.
- `agent_01_quintic_excert.md:151`: required quintic refinement.
- `agent_02_schoen_banana_gluing.md:272`: required Schoen refinement.

Heal.  Replace the coarse vectors by the refined finite obstruction
vectors while keeping `computed=False`.

Quintic vector:

```text
Z_period_isolation, support_Q, active_sector, HN_filtration_table,
hall_lower_saturation, extension_closed_ideal, ptvv_critical_atlas,
orientation_square_root, vanishing_cycle_TS, motivic_target,
realization_maps, ML_transition, T_eq_mode
```

Schoen vector:

```text
o_ssdeg, o_charge, o_BC, o_or, o_HN, o_Mot, o_lower, o_KS, o_pro
```

Concrete patches:

- Update `derived_solution_stack_factors()` coordinate names.
- Add tests asserting the exact coordinate tuples and `computed=False`.
- Add `quintic_excert_witness_certificate()` and
  `schoen_banana_constructed_point_certificate()` stubs that fail on
  missing coordinate data, not on vague non-existence.
- Update `chapters/theory/bps_positive_geometry_closure.tex:588` and
  `:590` to display the refined coordinate decompositions.

## ATTACK 3 -> HEAL 3: the raw K3 x E radical is not wired to its gate

Defect.  The BPS oracle uses the seven-coordinate raw radical vector,
which is correct:

- `compute/lib/bps_positive_truncation.py:1004`: `k3e_raw_radical`.
- `compute/lib/bps_positive_truncation.py:934`: full radical ledger.

But the separate Hall-Borcherds gate has different Boolean witnesses:

- `compute/lib/hall_borcherds_gate.py:75`: `HallBorcherdsWitnesses`.
- `compute/lib/hall_borcherds_gate.py:89`: eight required witnesses.
- `compute/tests/test_hall_borcherds_gate.py:36`: denominator weight does
  not close the typed gate.

There is no function mapping a closed gate to a computed
`ObstructionVector` for the BPS residual factor.  A future patch could
close one surface while leaving the other stale.

Heal.  Introduce a typed radical witness:

```python
@dataclass(frozen=True)
class HallBorcherdsRadicalWitness:
    pairing_kernel: Certificate
    orientation_character: Certificate
    protected_integration: Certificate
    primitive_bracket: Certificate
    serre_imaginary_relations: Certificate
    hopf_pairing: Certificate
    completion_separatedness: Certificate
```

Then add:

```python
def k3e_radical_witness_certificate(witness) -> Certificate
def k3e_radical_obstruction_vector(witness) -> ObstructionVector
```

The existing `HallBorcherdsWitnesses` gate can remain as an implication
guard, but the BPS point gate must read the seven radical coordinates
directly.  Add tests that denominator normalization plus root
multiplicity still leaves the BPS radical uncomputed, and that a toy
Gram certificate closes only `pairing_kernel`, never the raw theorem.

## ATTACK 4 -> HEAL 4: theta comparison has no package-indexed witness

Defect.  `theta_comparison_certificate()` proves the intrinsic finite
Hall theta package plus a comparison-slot ledger:

- `compute/lib/bps_positive_truncation.py:737`: theta certificate.
- `chapters/theory/bps_positive_geometry_closure.tex:391`: intrinsic Hall
  theta theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:427`: comparison
  corollary.

But the executable surface does not let a worker choose a package
`T in {broken_line, GHKK, GMN, Hall_fr}` and compute its existence and
comparison vectors.  The top-level nine-coordinate obstruction is useful
as a schema, but it is not a package witness.

Heal.  Add package-indexed witness functions:

```python
ThetaPackage = Literal["broken_line", "GHKK", "GMN", "Hall_fr"]

def theta_package_existence_certificate(package: ThetaPackage, datum, bound) -> Certificate
def theta_package_comparison_certificate(package: ThetaPackage, datum, bound) -> Certificate
def theta_constructed_point_certificate(package: ThetaPackage, datum, bound) -> Certificate
```

The default datum should be an empty/uncomputed datum, so the new tests
can be implemented now:

- every package has a named coordinate vector;
- no package is solved from intrinsic Hall transport alone;
- `theta_comparison_certificate(bound).passed` does not imply
  `theta_constructed_point_certificate(...).passed`;
- the intrinsic finite Hall package remains exact on the current rank-two
  test quotient.

## ATTACK 5 -> HEAL 5: hCS has a descent gate and a 14-vector, but no witness bridge

Defect.  The hCS surface has two correct pieces:

- `compute/lib/cy3_dwr_descent_gate.py:43`: twelve required DWR/Ran gates.
- `compute/lib/bps_positive_truncation.py:765`: fourteen-coordinate hCS
  named obstruction ledger.

They are not connected.  A complete `DescentGateState` currently proves
only the descent gate surface, not the primitive seven source/target
coordinates, and the BPS factor remains an uncomputed ledger:

- `compute/lib/bps_positive_truncation.py:1040`: hCS residual factor.
- `compute/tests/test_cy3_dwr_descent_gate.py:17`: complete gate passes.
- `compute/tests/test_bps_positive_truncation.py:336`: fourteen names are
  counted, not witnessed.

There is also stale notation in the wave-2 report: `agent_05_hcs_hall_localization.md:290`
and `:446` still write `o_or` where the code and chapter now use
`o_or_rel`.

Heal.  Add:

```python
@dataclass(frozen=True)
class HCSHallLocalizationWitness:
    primitive_certificates: tuple[Certificate, ...]
    descent_state: DescentGateState
    obstruction: ObstructionVector

def hcs_hall_localization_point_certificate(witness) -> Certificate
```

The certificate passes only when all seven primitive certificates are
exact and pass, `descent_state.has_descent()` is true, the obstruction
vector is computed, and all fourteen coordinates vanish.  Add tests that
`complete_descent_state()` alone does not solve the BPS hCS factor.
Patch stale note notation from `o_or` to `o_or_rel` for consistency with
`chapters/theory/bps_positive_geometry_closure.tex:350` and
`compute/lib/bps_positive_truncation.py:1053`.

## ATTACK 6 -> HEAL 6: transition exactness is single-step, not a tower witness

Defect.  `transition_certificate()` is now non-tautological and catches
ambient lower-set failures:

- `compute/lib/bps_positive_truncation.py:853`: transition certificate.
- `compute/tests/test_bps_positive_truncation.py:148`: nested rank-two
  transition test.

But the point obligations require cofinal Mittag-Leffler towers and
coordinate restriction.  A single `N-1 -> N` rank-two transition does not
check:

- a chain of three or more finite stages;
- cofinality of the visible charge sets;
- preservation of obstruction coordinate names and computed flags;
- compatibility of theta/wall transport under restriction.

Heal.  Add:

```python
def pro_tower_certificate(stages: tuple[BPSMotivicTruncation, ...]) -> Certificate
def obstruction_tower_certificate(vectors: tuple[ObstructionVector, ...]) -> Certificate
```

Tests implementable now:

- a three-stage rank-two tower passes;
- a tower with a missing middle charge fails;
- an obstruction tower with changed coordinate names fails;
- an obstruction tower with an uncomputed top vector remains a
  zero-fiber schema, not a constructed point.

Update `chapters/theory/bps_positive_geometry_closure.tex:680` to cite
the tower certificate rather than only pairwise transition maps.

## ATTACK 7 -> HEAL 7: synthesis notes still over-advertise "solved by"

Defect.  The manuscript and code now separate schema from points, but the
current synthesis note still contains over-strong shorthand:

- `notes/bps_positive_geometry_total_resolution_20260424/platonic_closure_20260424.md:282`:
  "compact non-toric existence: solved by ..."
- `:286`: "K3 x E Hall--BKM: solved as ..."
- `:290`: "hCS-to-Hall: solved by ..."
- `:293`: "theta enhancement: solved by ..."

This conflicts with the executable verdict:

```text
constructed False False 5
```

Heal.  Replace that block by:

```text
compact non-toric existence:
  BMS data-realized compact point constructed;

K3 x E Hall--BKM:
  Igusa denominator quotient theorem proved; raw Hall point equals the
  seven-coordinate radical zero fiber;

hCS-to-Hall:
  fourteen-coordinate descent/construction zero fiber defined;

theta enhancement:
  intrinsic finite Hall theta package proved; external packages are
  package-indexed comparison zero fibers;

finite oracle:
  implemented as schema gate; named point witnesses remain to be filled.
```

Also update `platonic_closure_20260424.md:300` so the final remaining
list includes raw `K3 x E` and hCS, not only quintic, Schoen, theta, and
truncation-depth upgrades.

## Concrete Patch Queue for the Main Thread

1. Refine `derived_solution_stack_factors()` coordinate names for quintic
   and Schoen; add tests asserting the exact coordinate vectors.
2. Add the generic `NamedPointWitness` / `named_point_certificate()` gate.
3. Add `HallBorcherdsRadicalWitness` and wire it to the BPS
   `k3e_raw_radical` factor; keep `radical_non_degeneracy_certificate()`
   as a pairing-coordinate primitive only.
4. Add theta package witness functions for `broken_line`, `GHKK`, `GMN`,
   and `Hall_fr`, with default uncomputed stubs that fail as points.
5. Add `HCSHallLocalizationWitness` bridging the DWR gate to the
   fourteen-coordinate BPS obstruction vector.
6. Add `pro_tower_certificate()` and `obstruction_tower_certificate()`.
7. Patch `platonic_closure_20260424.md` solved-language and the stale
   `o_or` notation in `agent_05_hcs_hall_localization.md`.
8. Update the closure chapter's derived-stack proof to name the refined
   coordinate decompositions and tower certificate.

## Tests to Run After Those Patches

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile \
  compute/lib/bps_positive_truncation.py \
  compute/lib/cy3_dwr_descent_gate.py \
  compute/lib/hall_borcherds_gate.py

PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py \
  compute/tests/test_cy3_dwr_descent_gate.py \
  compute/tests/test_hall_borcherds_gate.py \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_seed_walls_and_first_symmetric_root \
  compute/tests/test_scattering_diagram.py::test_scattering_diagram_orbit_table_has_expected_seed_orbits
```

If TeX or `main.tex` is edited by the integration thread, run session-end:

```text
make fast
```

## Exact Remaining List After These Patches

No untyped foundational gap remains.  The exact point-construction
obligations will be:

1. Quintic point: compute the thirteen-coordinate ExCert witness over a
   cofinal saturated Hall-lower tower and prove every coordinate is zero.
2. Schoen point: compute the nine-coordinate compact banana gluing vector
   and prove pro-compatible vanishing.
3. Raw `K3 x E` point: compute the seven-coordinate Hall-Borcherds
   radical vector in every finite quotient and prove completion
   separatedness.
4. Theta point: choose one package
   `T in {broken_line, GHKK, GMN, Hall_fr}`, compute its existence and
   comparison vectors against intrinsic Hall theta, and prove
   pro-compatible vanishing.
5. hCS point: supply the seven primitive hCS source/target certificates,
   close the DWR/Ran descent gate, compute the fourteen-coordinate vector,
   and prove it vanishes.

The BMS compact non-toric data-realized class remains the actual compact
non-toric point already present in the source object.  The five items
above are stronger named points of the same derived solution stack.

## Files Changed

Only:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_06_integration_execution.md
```
