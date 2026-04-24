# Agent 05 Report: hCS-to-Hall Localization

## Scope

Exclusive write scope:
`notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_05_hcs_hall_localization.md`.

No code or TeX files were edited.

The attacked obligation is the compact CY3 hCS-to-Hall localization
arrow

```tex
\Theta^{o}_{\hCS\to\Hall}:
\Obs^{q}_{\hCS}(-,\frakg)
\longrightarrow
\CoHA^{\Mot,o}_{\mathrm{crit}}(-)
```

as it appears in `chapters/theory/bps_positive_geometry_closure.tex:334`.
The live closure statement is already the correct conditional form: the
seven DWR/Ran classes are descent obstructions only after a
gauge-fixed anomaly-cancelled all-scale hCS package, an oriented
critical Hall target, compact-support/completion conventions, and
chartwise stationary-phase quasi-isomorphisms have been supplied
(`chapters/theory/bps_positive_geometry_closure.tex:337`).

## Verdict

Fatal for any unconditional compact-CY3 construction theorem obtained
from local `C3` or `K3 x E` evidence.

Nonfatal for the present closure theorem if read literally as a
conditional descent theorem.  The theorem must remain a two-level
criterion:

1. primitive source/target/chartwise construction;
2. DWR/Ran descent of the supplied chartwise maps.

The finite oracle is aligned with this reading: the hCS factor is a
defined zero-fiber equation, not a solved point
(`compute/lib/bps_positive_truncation.py:765`,
`compute/lib/bps_positive_truncation.py:967`).

## ATTACK 1 -> HEAL 1: QME, anomaly, and gauge fixing

**Attack.**  The phrase "hCS observables" is not a primitive object on a
compact CY3.  In the chain-level bridge it is the Costello-Gwilliam
renormalized BV complex with effective interaction, heat-kernel BV
Laplacian, and the quantum master equation as part of the
anomaly-cancellation hypothesis
(`chapters/theory/cy3_chain_level_bridge.tex:76`).  Therefore a local
or abelian `C3` computation cannot certify compact all-scale QME,
counterterms, RG compatibility, or gauge-fixing independence.

The strongest illegal globalization is:

```text
fixed abelian C3 chart + CY volume form => compact hCS source exists.
```

This fails.  The `C3` fixed sector has zero differential only after
projection to positive torus-fixed abelian modes
(`compute/lib/c3_hcs_hall_theta.py:1`, `compute/lib/c3_hcs_hall_theta.py:137`).
It does not construct the renormalized compact observable factorization
algebra.

**Heal.**  The source side must contribute three primitive coordinates:

```tex
(\omega_{\mathrm{QME}},
 \omega_{\mathrm{anom}},
 \omega_{\mathrm{gf}}).
```

Here `omega_QME` is square-zero all-scale BV, `omega_anom` is the
Costello-Li anomaly/trivialization class, and `omega_gf` is
gauge-fixing independence for propagator and harmonic projection.  The
compact theorem begins only after these three vanish.  Local `C3`
evidence is admissible as a projected test for a chart, never as the
compact source construction.

## ATTACK 2 -> HEAL 2: DWR source/target and oriented critical atlas

**Attack.**  A compact hCS-to-Hall arrow is not a map between two
ordinary algebras on one open set.  The comparison datum in the chain
chapter is an object on the DWR/Ran nerve with hCS products on all
simplices, Hall charge/HN completions, vanishing cycles, orientation
systems, shifts, Tate twists, and Hall correspondences
(`chapters/theory/cy3_chain_level_bridge.tex:522`).

The Hall target is not automatic from local PTVV Darboux charts.  The
gluing chapter isolates the compact oriented critical Hall datum and
its four obstruction classes: critical atlas, orientation branch,
Harder-Narasimhan completion, and Thom-Sebastiani coherence
(`chapters/theory/gluing/sec_9_obstructions.tex:1257`).  Its theorem
explicitly constructs only the compact oriented critical Hall cosheaf,
not the hCS-to-Hall morphism
(`chapters/theory/gluing/sec_9_obstructions.tex:1323`).

**Heal.**  The source/target preparation must contribute two more
primitive coordinates:

```tex
(\omega_{\mathrm{DWR}},\omega_{\mathrm{crit}}).
```

`omega_DWR=0` says both the hCS source and Hall target satisfy the
chosen DWR/Weiss descent in the completed category.  `omega_crit=0`
says the Hall target has compatible oriented critical charts, not only
local Darboux presentations.  These coordinates absorb the compact
Hall-cosheaf criterion into the hCS-to-Hall problem without conflating
it with the comparison map.

## ATTACK 3 -> HEAL 3: stationary phase and vertex quasi-isomorphism

**Attack.**  The known fixed abelian `C3` map sends positive hCS modes
to the Schiffmann-Vasserot shuffle algebra
(`compute/lib/c3_hcs_hall_theta.py:22`, `compute/lib/c3_hcs_hall_theta.py:89`).
It proves an algebraic finite-mode localization witness.  It does not
construct full stationary-phase maps

```tex
\theta_{\sigma,\gamma}:
\Obs^q_{\hCS}(\sigma,\mathfrak g)
\to
\CoHA^{or}_{crit}(\sigma)_\gamma
```

on every compact DWR/Ran simplex, nor does it prove those maps are
quasi-isomorphisms in the completed shifted/Tate/oriented category.
The Costello note makes the same separation: the `C3` chain closes
perturbatively to `Y^+`, while the full algebra passes through
Drinfeld doubling; there is no direct `C3` production of
`\mathcal W_{1+\infty}`
(`notes/wave12_a13_costello_5_routes_6d_hCS.tex:135`,
`notes/wave12_a13_costello_5_routes_6d_hCS.tex:151`).

**Heal.**  Add the chartwise comparison coordinates:

```tex
(\omega_{\mathrm{sp}},\omega_{\mathrm{vqis}}).
```

`omega_sp=0` means the stationary-phase family exists on the full
renormalized hCS source and critical Hall target.  `omega_vqis=0`
means the vertex maps are quasi-isomorphisms after the prescribed
orientation, shift, Tate twist, and completions.  The finite `C3`
shuffle map kills only the projected positive finite-mode component of
this pair.

## ATTACK 4 -> HEAL 4: seven DWR/Ran descent classes

**Attack.**  The seven classes are not construction classes.  They are
descent classes for maps that already exist.  The chain-level descent
definition first builds the complete Cech convolution dg Lie algebra
of continuous maps
(`chapters/theory/cy3_chain_level_bridge.tex:1110`) and then defines
the Maurer-Cartan, orientation, grading, Thom-Sebastiani, and
factorization obstruction tuple
(`chapters/theory/cy3_chain_level_bridge.tex:1129`).  The later closure
chapter correctly strengthens this five-class tuple by adding
compact-support Beck-Chevalley and completion defects
(`chapters/theory/bps_positive_geometry_closure.tex:353`).

The failure mode is:

```text
seven DWR/Ran classes vanish => compact hCS-to-Hall map exists.
```

This is false unless the primitive source, target, and chartwise maps
have already been supplied.

**Heal.**  The conditional descent theorem is:

```tex
(\omega_{\mathrm{QME}},\omega_{\mathrm{anom}},\omega_{\mathrm{gf}},
 \omega_{\mathrm{DWR}},\omega_{\mathrm{crit}},
 \omega_{\mathrm{sp}},\omega_{\mathrm{vqis}})=0
```

defines the arena in which the seven descent coordinates are meaningful,
and then

```tex
o_{\MC}=o_{\mathrm{or}}=o_{\mathrm{gr}}=o_{\mathrm{TS}}
=o_{\mathrm{fact}}=o_{\mathrm{cs}}=o_{\wedge}=0
```

is necessary and sufficient for global DWR/Ran descent
(`chapters/theory/bps_positive_geometry_closure.tex:369`).  This is not
a downgrade; it is the stronger typed theorem, because it forbids a
descent equation from pretending to construct its source.

## ATTACK 5 -> HEAL 5: compact CY3 hypotheses and local evidence

**Attack.**  The compact named cases are not obtained by transporting
the local toric theorem.  `C3` is Stein, affine, toric, and in the
executable witness abelian and fixed-mode.  `K3 x E` has special product
geometry and useful anomaly/cosection features, but its local
preparations still do not provide the relative comparison orientation,
all higher-simplex maps, compact-support Beck-Chevalley compatibility,
or completion continuity.  The DWR gate oracle explicitly rejects the
shortcuts:

- fixed `C3` chart kills only `o_theta^{fp,+}`;
- `CoHA(C3)=Y^+` is Hall-side cohomology, not an hCS-to-Hall map;
- Hall-side orientation triviality is not relative comparison
  orientation;
- Hall-side Thom-Sebastiani associativity is not comparison
  Thom-Sebastiani coherence
  (`compute/lib/cy3_dwr_descent_gate.py:61`).

**Heal.**  A compact CY3 point of the hCS-to-Hall zero fiber must be a
named geometry plus a computed vanishing certificate for all fourteen
coordinates below.  Local evidence is allowed only as a coordinate-level
input:

- `C3` fixed chart: evidence for a projected finite-mode piece of
  `omega_sp` and the MC/multiplicativity part after projection;
- Costello-Li/Costello-Gwilliam source theory: evidence for the form of
  `omega_QME`, `omega_anom`, and `omega_gf`;
- compact oriented Hall-cosheaf criterion: evidence for
  `omega_crit`, `o_or`, `o_TS`, and completion/HN pieces;
- K3 x E product geometry: a serious test case, not a global theorem.

## Healed theorem

Let `X` be a compact smooth CY3, `U` a DWR-good cover, `g` a metric
gauge Lie algebra, `Gamma` a charge monoid, and `sigma` a stability
sector.  Fix compact-support, orientation, shift, Tate, charge/HN,
equivariant, and completion conventions.  Let

```tex
\Omega_{\hCS,\Hall}(X,U,g)
=
(\omega_{\mathrm{QME}},
 \omega_{\mathrm{anom}},
 \omega_{\mathrm{gf}},
 \omega_{\mathrm{DWR}},
 \omega_{\mathrm{crit}},
 \omega_{\mathrm{sp}},
 \omega_{\mathrm{vqis}},
 o_{\MC},o_{\mathrm{or}},o_{\mathrm{gr}},o_{\mathrm{TS}},
 o_{\mathrm{fact}},o_{\mathrm{cs}},o_{\wedge}).
```

Then a global oriented hCS-to-Hall localization morphism exists on the
chosen DWR/Ran nerve and is vertexwise quasi-isomorphic in the completed
oriented Hall category if and only if

```tex
\Omega_{\hCS,\Hall}(X,U,g)=0.
```

After the first seven primitive coordinates vanish, this theorem reduces
exactly to the seven-class descent criterion in
`chapters/theory/bps_positive_geometry_closure.tex:334`.  Before the
first seven vanish, the seven DWR/Ran classes are not well-typed as a
complete construction theorem.

Equivalently, the primitive witness package of the chain-level bridge
is the descent-theoretic normal form:

```tex
(\theta^{(0)},\eta_{\mathrm{MC}},
 \lambda_{\mathrm{or}},\eta_{\mathrm{gr}},
 H_{\mathrm{TS}},H_{\mathrm{fact}},Q)
```

with the Maurer-Cartan correction, orientation primitive,
grading/Tate primitive, Thom-Sebastiani homotopy, factorization
homotopy, and quasi-isomorphism certificate as in
`chapters/theory/cy3_chain_level_bridge.tex:1213` and
`chapters/theory/cy3_chain_level_bridge.tex:1290`.

## Fourteen-coordinate obstruction vector

| coordinate | meaning | finite witness status |
|---|---|---|
| `omega_QME` | all-scale BV differential squares to zero | uncomputed for named compact CY3 |
| `omega_anom` | Costello-Li anomaly class/trivialization | uncomputed for named compact CY3 |
| `omega_gauge_fixing` | heat-kernel gauge-fixing independence | uncomputed |
| `omega_DWR_source_target` | source and target satisfy DWR/Weiss descent | uncomputed |
| `omega_critical_atlas` | compatible oriented critical Hall atlas | uncomputed |
| `omega_stationary_phase` | chartwise stationary-phase maps exist | uncomputed outside finite fixed `C3` projection |
| `omega_vertex_quasi_iso` | vertex maps are quasi-isomorphisms after all normalizations | uncomputed |
| `o_MC` | Cech/Ran Maurer-Cartan curvature | gate-defined, uncomputed for named compact CY3 |
| `o_or` | relative orientation square-root Cech class | gate-defined, uncomputed |
| `o_gr` | shift/Tate grading mismatch | gate-defined, uncomputed |
| `o_TS` | Thom-Sebastiani associator defect | gate-defined, uncomputed |
| `o_fact` | disjoint Ran factorization defect | gate-defined, uncomputed |
| `o_cs` | compact-support Beck-Chevalley defect | gate-defined, uncomputed |
| `o_wedge` | charge/HN/completion continuity defect | gate-defined, uncomputed |

The executable ledger names the same vector in
`compute/lib/bps_positive_truncation.py:768` and the zero-fiber factor
marks it `computed=False`, hence not solved.

## Finite executable oracle design

The present oracle should be read as three layers.

1. **Descent gate layer.**  `compute/lib/cy3_dwr_descent_gate.py:21`
   defines finite gates.  `REQUIRED_DESCENT_GATES` has twelve gates:
   DWR cover, full renormalized chart maps, all simplices, Cech MC zero,
   vertex quasi-isomorphisms, `H^0` invertibility, relative orientation,
   grading/Tate, Thom-Sebastiani, factorization, completions, and
   compact-support compatibility (`compute/lib/cy3_dwr_descent_gate.py:43`).

2. **Local finite-mode witness.**  `compute/lib/c3_hcs_hall_theta.py:1`
   proves only the abelian positive fixed `C3` shuffle-localization
   witness.  It should remain a source of coordinate evidence, not a
   constructor for compact `Theta`.

3. **Named zero-fiber layer.**  `hcs_named_obstruction_certificate()`
   names all fourteen coordinates and is `exact=False`
   (`compute/lib/bps_positive_truncation.py:765`).  The derived solution
   stack factor is zero-fiber-defined but not solved, because
   `obstruction.computed=False` for `hcs_named_zero_fiber`.

The next strict increase in oracle strength is a typed data structure
for

```text
HCSHallLocalizationWitness
```

with fields:

```text
source_qme_certificate
anomaly_trivialization_certificate
gauge_fixing_homotopy_certificate
dwr_source_target_certificate
critical_atlas_certificate
stationary_phase_family_certificate
vertex_quasi_isomorphism_certificate
descent_gate_state
fourteen_coordinate_vector
```

`solved` must be true only when every primitive certificate is exact,
`descent_gate_state.has_descent()` is true, the fourteen-coordinate
obstruction vector is computed, and every coordinate is zero.  The
current code already enforces the last distinction at the
`SolutionStackFactor` level.

## Exact anchors read

- `chapters/theory/bps_positive_geometry_closure.tex:334`: seven-class
  hCS-Hall descent theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:357`: primitive
  source/target vector required for named compact CY3.
- `chapters/theory/bps_positive_geometry_closure.tex:369`: proof that
  seven classes are descent after the primitive vector exists.
- `chapters/theory/cy3_chain_level_bridge.tex:76`: quantum hCS
  observables as renormalized BV complex with QME.
- `chapters/theory/cy3_chain_level_bridge.tex:522`: oriented
  hCS-Hall comparison datum on the DWR/Ran nerve.
- `chapters/theory/cy3_chain_level_bridge.tex:654`: supplied DWR/Ran
  datum gives the comparison morphism; it constructs no such datum.
- `chapters/theory/cy3_chain_level_bridge.tex:1110`: Cech convolution
  dg Lie algebra controlling descent.
- `chapters/theory/cy3_chain_level_bridge.tex:1213`: primitive witness
  package.
- `chapters/theory/cy3_chain_level_bridge.tex:1290`: primitive package
  iff compact oriented comparison.
- `chapters/theory/gluing/sec_9_obstructions.tex:1257`: compact
  oriented critical Hall datum.
- `chapters/theory/gluing/sec_9_obstructions.tex:1323`: compact Hall
  cosheaf criterion does not construct hCS-to-Hall.
- `notes/wave12_a13_costello_5_routes_6d_hCS.tex:135`: Costello-Li
  nonperturbative/full-W shortcut attack.
- `notes/wave12_a13_costello_5_routes_6d_hCS.tex:151`: `C3` closes to
  `Y^+`, full algebra by Drinfeld doubling.
- `notes/wave12_a5_hCS_BV_BRST_explicit.tex:161`: local line-defect
  hCS evidence on `C3`.
- `compute/lib/cy3_dwr_descent_gate.py:21`: finite DWR gate enum.
- `compute/lib/cy3_dwr_descent_gate.py:43`: required descent gates.
- `compute/lib/cy3_dwr_descent_gate.py:61`: forbidden shortcut reasons.
- `compute/lib/c3_hcs_hall_theta.py:1`: fixed abelian `C3` finite-mode
  scope.
- `compute/lib/bps_positive_truncation.py:765`: fourteen-coordinate
  hCS named obstruction ledger.
- `compute/tests/test_cy3_dwr_descent_gate.py:17`: complete gate passes.
- `compute/tests/test_cy3_dwr_descent_gate.py:33`: fixed `C3` chart does
  not imply descent.
- `compute/tests/test_cy3_dwr_descent_gate.py:60`: Hall-side orientation
  is not relative orientation.
- `compute/tests/test_bps_positive_truncation.py:242`: hCS certificate
  checks fourteen coordinates.

## Commands run

```text
pytest -q compute/tests/test_cy3_dwr_descent_gate.py \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_bps_positive_truncation.py::test_hcs_named_obstruction_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points
```

Result:

```text
30 passed in 0.95s
```

Additional oracle probe:

```text
complete_dwr {'has_descent': True, 'missing_descent_gates': (), ...}
fixed_c3_shortcut {'has_descent': False, 'missing_descent_gates': (...), ...}
hcs_cert hcs_named_obstructions False True 14 ...
hcs_factor hcs_named_zero_fiber False True False (...)
```

One attempted probe called a nonexistent `Certificate.as_dict()` method
and failed before rerunning with direct field access.  It did not edit
files and did not affect the test surface.

## Files changed

Only this report:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_05_hcs_hall_localization.md
```

## Remaining obligations

The hCS-to-Hall point is now exact as a typed problem and unresolved as
a constructed named compact-CY3 point.  The remaining obligations are:

1. construct an all-scale compact hCS source with computed
   `omega_QME`, `omega_anom`, and `omega_gauge_fixing`;
2. construct the oriented critical Hall target on the DWR/Ran nerve with
   computed `omega_DWR_source_target` and `omega_critical_atlas`;
3. construct stationary-phase chart maps on every retained simplex and
   prove `omega_stationary_phase=0`;
4. prove vertex quasi-isomorphism after orientation, shift, Tate,
   compact-support, and completion normalizations;
5. compute the seven descent classes
   `(o_MC,o_or,o_gr,o_TS,o_fact,o_cs,o_wedge)` from the named compact
   geometry and prove that they vanish;
6. upgrade the finite oracle from a gate ledger to a witness-checker
   that refuses `solved=True` unless all fourteen coordinates are
   computed zero.

No weaker theorem is needed.  The platonic object is the fourteen
coordinate derived zero fiber; a compact hCS-to-Hall construction is a
point of that zero fiber, not a consequence of the local `C3` normal
form.
