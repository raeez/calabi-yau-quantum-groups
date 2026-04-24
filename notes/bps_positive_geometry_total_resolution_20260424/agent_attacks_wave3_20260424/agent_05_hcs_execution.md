# Agent 05 Report: hCS-to-Hall Fourteen-Coordinate Execution

## Scope

Exclusive write scope:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_05_hcs_execution.md
```

No code, TeX, git state, or other notes were edited.

The attacked obligation is the compact CY3 hCS-to-Hall point condition
inside the BPS-positive residual solution stack:

```tex
\Omega_{\hCS,\Hall}=0.
```

The current manuscript gives the correct typed surface.  The descent
theorem starts at
`chapters/theory/bps_positive_geometry_closure.tex:334`; the seven
descent classes are named at
`chapters/theory/bps_positive_geometry_closure.tex:350`; the primitive
source/target vector is required at
`chapters/theory/bps_positive_geometry_closure.tex:359`; and the proof
explicitly says that without the primitive vector there is no source,
target, or chartwise map to descend
(`chapters/theory/bps_positive_geometry_closure.tex:385`).

## Verdict

The hCS-to-Hall obligation remains a point-construction problem, not a
missing foundation.  The surviving object is the fourteen-coordinate
derived zero fiber

```tex
\Omega_{\hCS,\Hall}
=
(\omega_{\mathrm{QME}},\omega_{\mathrm{anom}},
 \omega_{\mathrm{gf}},\omega_{\mathrm{DWR}},\omega_{\mathrm{crit}},
 \omega_{\mathrm{sp}},\omega_{\mathrm{vqis}},
 o_{\MC},o_{\mathrm{or}}^{\mathrm{rel}},o_{\mathrm{gr}},o_{\mathrm{TS}},
 o_{\mathrm{fact}},o_{\mathrm{cs}},o_{\wedge}),
```

recorded in the manuscript at
`chapters/theory/bps_positive_geometry_closure.tex:601` and in the
oracle as

```text
omega_QME
omega_anom
omega_gauge_fixing
omega_DWR_source_target
omega_critical_atlas
omega_stationary_phase
omega_vertex_quasi_iso
o_MC
o_or_rel
o_gr
o_TS
o_fact
o_cs
o_wedge
```

at `compute/lib/bps_positive_truncation.py:772`.  The live test at
`compute/tests/test_bps_positive_truncation.py:336` enforces the
relative orientation name: `o_or_rel` is present and stale scalar
`o_or` is absent.

## ATTACK 1 -> HEAL 1: fixed C3 chart is not compact hCS

**Attack.**  The executable `C3` witness is finite, abelian,
torus-fixed, and positive-mode.  Its module docstring states this
scope at `compute/lib/c3_hcs_hall_theta.py:1`; the shuffle product is
the local Schiffmann-Vasserot algebraic witness at
`compute/lib/c3_hcs_hall_theta.py:89`; and the differential is zero
only in this projected sector at `compute/lib/c3_hcs_hall_theta.py:137`.

The false implication is:

```text
fixed abelian C3 shuffle localization
=> compact all-scale hCS source exists.
```

It fails because compact hCS requires the Costello-Gwilliam all-scale
BV package: QME, anomaly trivialization, propagator/RG compatibility,
and gauge-fixing independence.

**Heal.**  The `C3` chart is coordinate evidence for a projected piece
of `omega_stationary_phase` and for finite multiplicativity after
projection.  It is not evidence for

```text
omega_QME = omega_anom = omega_gauge_fixing = 0
```

on a named compact CY3.  The compact source side is solved only by an
all-scale package whose BV differential squares to zero and whose
renormalized observables are independent of gauge-fixing choices.

## ATTACK 2 -> HEAL 2: Hall orientation is not relative orientation

**Attack.**  The dangerous orientation shortcut is:

```text
Hall-side orientation triviality
=> o_or_rel = 0.
```

The gate oracle rejects this explicitly.  `Gate.RELATIVE_ORIENTATION_COCYCLE_ZERO`
is a required descent gate at `compute/lib/cy3_dwr_descent_gate.py:33`
and `compute/lib/cy3_dwr_descent_gate.py:43`; the shortcut reason
"Hall-side orientation triviality is not relative comparison
orientation" is registered at `compute/lib/cy3_dwr_descent_gate.py:61`;
and `test_hall_side_orientation_is_not_relative_orientation` checks
the failure at `compute/tests/test_cy3_dwr_descent_gate.py:60`.

The chain-level K3 x E discussion has the same shape.  The Hall
orientation torsor is prepared, but the relative comparison class can
still survive until the comparison cochain is chosen
(`chapters/theory/cy3_chain_level_bridge.tex:3686`).

**Heal.**  The relative orientation coordinate is:

```text
o_or_rel = delta(lambda_or)
```

where `lambda_or` compares the determinant transport from the hCS BV
side with the Joyce-Kontsevich-Song orientation local system on the
Hall side on every DWR/Cech/Ran simplex.  A Hall-side square root is
only the target half of this equation.  Vanishing means that a
comparison orientation cochain exists and is compatible with faces,
degeneracies, refinements, direct sums, and transition maps.

## ATTACK 3 -> HEAL 3: descent gates are not the whole point

**Attack.**  The DWR gate oracle has twelve gates
(`compute/lib/cy3_dwr_descent_gate.py:43`), while the residual
solution stack has fourteen hCS coordinates
(`compute/lib/bps_positive_truncation.py:772`).  Treating this as a
mismatch creates the false implication:

```text
complete_descent_state()
=> compact hCS-to-Hall point.
```

This is false.  The descent gates assume the primitive arena: DWR-good
cover, full renormalized chart maps, maps on all simplices, vertex
quasi-isomorphisms, and the comparison normalizations.  They do not
construct the compact quantum hCS package or the oriented critical Hall
target from nothing.

**Heal.**  The correct factorization is two-level.

Primitive construction coordinates:

```text
omega_QME
omega_anom
omega_gauge_fixing
omega_DWR_source_target
omega_critical_atlas
omega_stationary_phase
omega_vertex_quasi_iso
```

Relative descent coordinates:

```text
o_MC
o_or_rel
o_gr
o_TS
o_fact
o_cs
o_wedge
```

The twelve finite gates are a checkable normal form for the second
level plus the typing requirements that make the second level
meaningful.  The fourteen-coordinate vector is the point condition in
the residual solution stack.

## ATTACK 4 -> HEAL 4: compact Hall cosheaf is not the comparison map

**Attack.**  The compact oriented critical Hall datum is a target
construction.  It begins at
`chapters/theory/gluing/sec_9_obstructions.tex:1257`; its criterion
begins at `chapters/theory/gluing/sec_9_obstructions.tex:1323`; and
the text states that it does not construct
`\Theta_{\hCS\to\Hall}^{or}` at
`chapters/theory/gluing/sec_9_obstructions.tex:1346`.

The false implication is:

```text
compact oriented critical Hall cosheaf exists
=> hCS-to-Hall localization exists.
```

It fails because the comparison requires continuous chartwise maps from
renormalized hCS observables to oriented critical Hall complexes, and
these maps must satisfy DWR/Ran naturality, product, bracket,
Thom-Sebastiani, shift/Tate, orientation, and completion conditions.

**Heal.**  The Hall cosheaf vanishing vector supplies the target
component of `omega_critical_atlas` and part of
`omega_DWR_source_target`.  The comparison map still requires

```text
omega_stationary_phase = 0
omega_vertex_quasi_iso = 0
```

and the seven descent coordinates.  Target construction is a necessary
input, not a theorem about the arrow.

## ATTACK 5 -> HEAL 5: finite K3 x E evidence is not completed descent

**Attack.**  The finite K3 x E comparison theorem starts at
`chapters/theory/cy3_chain_level_bridge.tex:3554`.  It is a finite
theorem: finite holomorphic-jet order, finite renormalization order,
finite charge bound, and finite Ran arity bound.  The theorem itself
names the remaining global condition as compatibility under the four
transition systems at
`chapters/theory/cy3_chain_level_bridge.tex:3633`.

The false implication is:

```text
finite DWR/Ran oriented comparison at fixed (N,r,L,m)
=> completed compact hCS-to-Hall point.
```

It fails by the usual inverse-limit obstruction: the finite primitive
packages must be compatible under `N`, `r`, charge, and Ran-arity
transitions.  The residual pro-class is a lim^1 obstruction, not a
finite-stage decoration.

**Heal.**  Finite K3 x E supplies the right finite normal form.  A
completed point additionally requires pro-compatible primitive
packages:

```text
N+1 -> N
r+1 -> r
Gamma_{<=L+1} -> Gamma_{<=L}
Nerve_{<=m+1} -> Nerve_{<=m}
```

and vanishing of the corresponding transition obstruction.  In the
BPS-positive oracle this lives in the same "computed zero" discipline
as the other named point obligations: a finite ledger is not a point
until the compatible inverse system is constructed.

## ATTACK 6 -> HEAL 6: seven descent classes are not construction classes

**Attack.**  The seven DWR/Ran classes are often read as if their
vanishing alone constructs the morphism.  The chain-level bridge
forbids this reading.  The oriented comparison datum is defined at
`chapters/theory/cy3_chain_level_bridge.tex:522`; the theorem from a
DWR/Ran datum states that it constructs no such datum at
`chapters/theory/cy3_chain_level_bridge.tex:670`; the simplexwise
witnessed complete bridge starts at
`chapters/theory/cy3_chain_level_bridge.tex:1903`.

The false implication is:

```text
o_MC = o_or_rel = o_gr = o_TS = o_fact = o_cs = o_wedge = 0
=> compact comparison map exists.
```

It fails unless the local maps, source, target, and quasi-isomorphism
data have already been supplied.

**Heal.**  The seven classes are nullhomotopy obstructions inside the
Cech/Ran convolution dg Lie algebra of a supplied comparison datum.
The point theorem is:

```text
primitive arena exists
and
seven relative descent coordinates vanish
and
transition/pro-completion coordinates vanish.
```

This is stronger than an unconditional local-to-compact statement: it
names every object the theorem must construct and blocks every
shortcut.

## Healed theorem

Let `X` be a compact smooth CY3, `U` a DWR-good cover, `g` a metric
gauge Lie algebra, `Gamma` a charge monoid, and `sigma` a stability
sector.  Fix compact-support, orientation, shift, Tate, HN/charge,
equivariant, and completion conventions.

A compact oriented hCS-to-Hall localization point consists of:

```text
Q_hCS:
  all-scale anomaly-free quantum hCS package

H_crit:
  oriented critical Hall target on the DWR/Cech/Ran nerve

Theta_sigma:
  continuous degree-zero stationary-phase maps on every retained simplex

Q_v:
  vertexwise quasi-isomorphism certificates after all normalizations

h_desc:
  nullhomotopies for MC, relative orientation, grading/Tate,
  Thom-Sebastiani, disjoint factorization, compact-support
  Beck-Chevalley, and completion defects

P_pro:
  compatible transition system in jet, RG, charge, and Ran-arity bounds
```

Such a point exists if and only if the fourteen-coordinate obstruction
vector `Omega_{hCS,Hall}` is computed from these named data and all
coordinates vanish.  Local `C3` and finite K3 x E statements are
admissible evidence for individual coordinates; they are not a compact
point until the full vector and transition system are computed.

## Exact witness and gate signatures

The next executable witness should be typed as:

```text
HCSHallLocalizationWitness:
  source_qme_certificate
  anomaly_trivialization_certificate
  gauge_fixing_homotopy_certificate
  dwr_source_target_certificate
  critical_atlas_certificate
  stationary_phase_family_certificate
  vertex_quasi_isomorphism_certificate
  descent_gate_state
  relative_orientation_cochain
  compact_support_bc_certificate
  completion_transition_certificate
  fourteen_coordinate_vector
```

The solved predicate must be:

```text
source certificates exact
and descent_gate_state.has_descent()
and relative_orientation_cochain kills o_or_rel
and pro-transition certificate exact
and fourteen_coordinate_vector.computed
and every coordinate is zero.
```

The present oracle already enforces the essential safety condition:
`hcs_named_zero_fiber` is zero-fiber-defined but not solved.  The
certificate is created at `compute/lib/bps_positive_truncation.py:772`;
the derived factor is created at
`compute/lib/bps_positive_truncation.py:1010`; and the residual
solution stack test checks unsolved zero-fiber status at
`compute/tests/test_bps_positive_truncation.py:420`.

## Available executable evidence

The targeted test slice was run with Python bytecode and pytest cache
writes disabled:

```text
PYTHONDONTWRITEBYTECODE=1 PYTEST_ADDOPTS='-p no:cacheprovider' pytest -q \
  compute/tests/test_cy3_dwr_descent_gate.py \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_bps_positive_truncation.py::test_hcs_named_obstruction_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points
```

Result:

```text
30 passed in 1.66s
```

Additional oracle probe:

```text
complete {'has_descent': True, 'missing_descent_gates': (), ...}
fixed {'has_descent': False,
       'missing_descent_gates': (..., 'relative_orientation_cocycle_zero', ...),
       'shortcut_reasons': ('fixed C3 chart kills only o_theta^{fp,+}, not descent',
                            'CoHA(C3)=Y^+ is Hall-side cohomology, not an hCS-to-Hall map',
                            'direct CoHA(C3)->W shortcut is forbidden')}
relative_orientation_shortcut {'has_descent': False,
                               'missing_descent_gates': ('relative_orientation_cocycle_zero',),
                               'shortcut_reasons': ('Hall-side orientation triviality is not relative comparison orientation',)}
hcs_certificate hcs_named_obstructions True False 14
hcs_factor hcs_named_zero_fiber True False False (...)
```

The probe confirms the three decisive facts:

1. complete gates pass only as descent data;
2. fixed `C3` and Hall-side orientation do not imply compact descent;
3. the hCS residual factor is a defined zero fiber and not a solved
   point.

## File anchors

- `chapters/theory/bps_positive_geometry_closure.tex:334`: conditional
  hCS-to-Hall descent theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:350`: seven
  relative DWR/Ran descent classes.
- `chapters/theory/bps_positive_geometry_closure.tex:359`: primitive
  source/target vector.
- `chapters/theory/bps_positive_geometry_closure.tex:385`: no primitive
  vector, no typed descent problem.
- `chapters/theory/bps_positive_geometry_closure.tex:601`: total
  fourteen-coordinate vector.
- `compute/lib/bps_positive_truncation.py:772`: hCS named obstruction
  certificate.
- `compute/lib/bps_positive_truncation.py:1010`: hCS zero-fiber factor.
- `compute/tests/test_bps_positive_truncation.py:336`: `o_or_rel`
  regression test.
- `compute/lib/cy3_dwr_descent_gate.py:43`: required DWR descent gates.
- `compute/lib/cy3_dwr_descent_gate.py:61`: forbidden shortcut reasons.
- `compute/tests/test_cy3_dwr_descent_gate.py:60`: Hall-side orientation
  is not relative orientation.
- `compute/lib/c3_hcs_hall_theta.py:1`: fixed abelian `C3` scope.
- `compute/tests/test_c3_hcs_hall_theta.py:75`: projected fixed-sector
  differential check.
- `chapters/theory/cy3_chain_level_bridge.tex:522`: oriented comparison
  datum on the DWR/Ran nerve.
- `chapters/theory/cy3_chain_level_bridge.tex:670`: datum theorem
  constructs no datum.
- `chapters/theory/cy3_chain_level_bridge.tex:3554`: finite K3 x E
  DWR/Ran comparison theorem.
- `chapters/theory/cy3_chain_level_bridge.tex:3633`: remaining
  transition/pro-descent condition.
- `chapters/theory/gluing/sec_9_obstructions.tex:1257`: compact
  oriented critical Hall datum.
- `chapters/theory/gluing/sec_9_obstructions.tex:1346`: compact Hall
  cosheaf does not construct the hCS-to-Hall arrow.

## Commands run

```text
sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md
sed -n '1,220p' .agents/skills/vol3-claim-verification/SKILL.md
sed -n '1,220p' .agents/skills/vol3-compute-engine/SKILL.md
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' AGENTS.md
sed -n '1,180p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,200p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
rg -n ... chapters/theory/bps_positive_geometry_closure.tex compute/lib/bps_positive_truncation.py compute/tests/test_bps_positive_truncation.py
sed -n '1,260p' compute/lib/cy3_dwr_descent_gate.py
sed -n '1,300p' compute/lib/c3_hcs_hall_theta.py
sed -n '1,260p' notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_05_hcs_hall_localization.md
sed -n '1,180p' compute/tests/test_cy3_dwr_descent_gate.py
sed -n '1,240p' compute/tests/test_c3_hcs_hall_theta.py
sed -n '520,700p' chapters/theory/cy3_chain_level_bridge.tex
sed -n '1898,1938p' chapters/theory/cy3_chain_level_bridge.tex
sed -n '3554,3690p' chapters/theory/cy3_chain_level_bridge.tex
sed -n '1250,1368p' chapters/theory/gluing/sec_9_obstructions.tex
PYTHONDONTWRITEBYTECODE=1 PYTEST_ADDOPTS='-p no:cacheprovider' pytest -q ...
PYTHONDONTWRITEBYTECODE=1 python3 -c "..."
mkdir -p notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424
```

One `rg` pattern containing TeX backslashes was malformed and returned
a regex parse error.  It was replaced by fixed-string `rg -F` searches.

No git commands were run.

## Files changed

Only the assigned report was added:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_05_hcs_execution.md
```

The target directory was absent and was created to hold the assigned
report.

## What remains

The remaining obligation is not to invent a new foundation.  It is to
construct an actual named compact-CY3 point of the already defined
zero fiber.

Concrete remaining work:

1. construct an all-scale compact hCS source and compute
   `omega_QME`, `omega_anom`, and `omega_gauge_fixing`;
2. construct the oriented critical Hall target on the DWR/Cech/Ran
   nerve and compute `omega_DWR_source_target` and
   `omega_critical_atlas`;
3. construct stationary-phase maps on every retained simplex and prove
   `omega_stationary_phase=0`;
4. prove vertex quasi-isomorphism after orientation, shift, Tate,
   compact-support, and completion normalizations;
5. construct the relative orientation cochain killing `o_or_rel`, not
   only the Hall-side orientation square root;
6. compute and kill
   `(o_MC,o_or_rel,o_gr,o_TS,o_fact,o_cs,o_wedge)`;
7. prove compatibility through the jet, RG, charge, and Ran-arity
   transition systems.

The strongest next theorem is a witness theorem for
`HCSHallLocalizationWitness`: solved exactly when the fourteen
coordinates are computed zero and the pro-transition certificate
vanishes.  The current manuscript and oracle already express the
correct zero-fiber; the next strict increase is to populate it with an
actual compact point.
