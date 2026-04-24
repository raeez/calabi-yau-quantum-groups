# Agent 02 Wave 2: Schoen/Banana Compact Gluing

## Claim Attacked

The remaining Schoen obligation is the assertion that local banana BPS
geometry can be promoted to an actual compact non-toric point of the
chambered effective BPS positive geometry.  In the present manuscript this
is deliberately encoded as

```tex
X_{\mathrm{Sch}}\quad\Longleftrightarrow\quad o_{\mathrm{glue}}=0
```

inside the residual solution stack, not as an already constructed point.
The attack is therefore against the possible stronger misreading:

```tex
S_4^{\mathrm{inst}}=-44,\quad r_{\max}=-1
  \quad\Rightarrow\quad
\operatorname{ExCert}(X_{\mathrm{Sch}};\sigma,Q,S,o,T_{\mathrm{eq}},\Mot).
```

That implication is false.  The local banana calculation is a local
shadow input; it does not construct compact-support Hall gluing, Cech
descent of chambers, orientation descent, HN compatibility, or
wall-crossing transport on the compact Schoen derived moduli stack.

## Local Surface Read

- `chapters/theory/bps_positive_geometry_closure.tex:51` requires finite
  saturated Hall-lower subsets and closed Hall ideals, not raw rectangular
  charge truncations.
- `chapters/theory/bps_positive_geometry_closure.tex:231` defines
  `ExCert` as the full compact chamber existence package.
- `chapters/theory/bps_positive_geometry_closure.tex:249` states the
  Schoen certificate as compact-support HN-compatible gluing of local
  banana Hall charts.
- `chapters/theory/bps_positive_geometry_closure.tex:259` records
  `S_4^{inst}=-44` and `r_max=-1` as local banana shadow input.
- `chapters/theory/bps_positive_geometry_closure.tex:530` defines the
  finite data space containing compact-support Hall correspondences.
- `chapters/theory/bps_positive_geometry_closure.tex:558` identifies
  `o_glue` as the compact Hall Cech gluing defect.
- `chapters/theory/bps_positive_geometry_closure.tex:600` makes the
  residual solution stack an exact zero-fiber schema.
- `chapters/theory/bps_positive_geometry_closure.tex:619` says the BMS
  compact non-toric class is an actual point while Schoen is a closed
  substack until its named obstruction vector is computed and vanishes.
- `compute/lib/bps_positive_truncation.py:692` implements the
  Schoen/banana certificate by checking local banana shadow values.
- `compute/lib/bps_positive_truncation.py:707` marks this certificate
  `exact=False`.
- `compute/lib/bps_positive_truncation.py:910` installs the current
  Schoen obstruction coordinates
  `charge_pushforward`, `compact_support_BC`, `overlap_orientation`,
  `HN_overlap`, `motivic_overlap`, `pro_continuity`, with
  `computed=False`.
- `compute/tests/test_bps_positive_truncation.py:217` checks that the
  Schoen local ledger passes but is not exact.
- `compute/tests/test_bps_positive_truncation.py:318` checks that Schoen
  is a defined zero fiber but not solved.
- `compute/tests/test_bps_positive_truncation.py:346` records Schoen
  among the unresolved named point-construction obligations.
- `compute/lib/banana_shadow.py:498` computes the local banana shadow
  tower; `compute/lib/banana_shadow.py:553` returns class `M`,
  `S_4^{inst}=-44`, and `r_max=-1`.
- `compute/lib/banana_shadow.py:776` records the degenerate local banana
  intersection matrix with null fiber direction.
- `compute/lib/cy3_grand_atlas.py:702` separates the compact Schoen
  threefold from the local banana curve sector.
- `chapters/theory/gluing/sec_10_unifying.tex:528` gives the template for
  compact Hall construction data on a DWR/Cech/Ran nerve.
- `chapters/theory/gluing/sec_10_unifying.tex:660` names the cosheaf
  axioms for refinement and Hall convolution.
- `chapters/theory/gluing/sec_10_unifying.tex:697` states finite
  wall-transport compatibility with motivic integration and KS
  conjugation.
- `chapters/theory/gluing/sec_10_unifying.tex:992` warns that Schoen-type
  partial-fibration examples do not carry the full `K3 x E` cell-15
  cocycle.
- `chapters/theory/gluing/sec_10_unifying.tex:1697` separates the
  Cech--Ran Hall-cosheaf layer from the decategorified positive-cone
  layer.

## Five Attack-Heal Cycles

### Cycle 1: Semistable Degeneration

**Attack.**  A semistable degeneration containing banana fibers does not
itself produce a Bridgeland or Hall stability datum on
`\Perf(X_{\mathrm{Sch}})`.  The degeneration identifies local curve
sectors and their DT shadows; it does not decide which compact objects
are semistable in a strict sector, nor does it prove the support property
for the compact numerical charge lattice.

**Failure mode.**  The false proof forgets the order:

```tex
degeneration data
  \not\Rightarrow
(\sigma,Q,\mathrm{HN}_{fin})
```

and therefore cannot build the finite Hall quotients required by
`thm:bps-positive-finite-first-existence`.

**Heal.**  The true theorem is an iff certificate.  For every finite
saturated Hall-lower set `L_{\le N,\le R}`, a Schoen truncation exists
only after a named compact chamber datum
`(\sigma,Q,S,\mathrm{HN}_{fin})` is supplied on the compact category and
the banana local sectors are restrictions of that datum.  The
semistable degeneration is an input to constructing the local charts,
not the chamber itself.

### Cycle 2: Banana Curve Local Model

**Attack.**  The local banana model has a rank-two curve sector with
degenerate intersection form

```text
((-2, 2), (2, -2)), determinant 0,
```

and null fiber direction `C_1+C_2`.  The compact Schoen threefold has
`h11=h21=19`.  Identifying these charge geometries without an explicit
compact-support pushforward destroys the null direction and can turn a
local Jacobi index into a compact charge pairing by fiat.

**Failure mode.**  The local facts

```text
S_4^{inst}=-44,
banana_genus0_gv_total(3)=-44,
Jacobi index ((2,-2),(-2,2)),
intersection determinant 0
```

prove non-toric higher-shadow input, not compact charge gluing.

**Heal.**  The Schoen point requires a finite charge map

```tex
j_{a,!}:\Gamma_{a,L}\longrightarrow \Gamma_{X,L}
```

for every banana chart `U_a`, induced by compact-support extension by
zero.  The map must quotient or transport the null fiber direction
before comparison with `K_num(X_{\mathrm{Sch}})`.  Its defect is the
first coordinate `o_charge`.

### Cycle 3: Compact Support and Gluing Exactness

**Attack.**  Ordinary Cech restriction does not imply Hall gluing.  Hall
product is pull-push along extension stacks; compact-support extension
changes variance and can break Beck--Chevalley.

**Failure mode.**  The equality

```tex
j_{!} q_{a,!}p_a^*
 =
q_{X,!}p_X^*(j_{!}\times j_{!})
```

is a theorem to prove, not a formal property of local DT invariants.
If it fails, local banana multiplication does not land in the compact
Schoen Hall product.

**Heal.**  Add the compact-support Beck--Chevalley coordinate `o_BC`.
It vanishes exactly when the local extension-stack convolution commutes
with compact-support pushforward in the retained finite quotient.  This
is the Schoen analogue of the compact-support obstruction named in
`notes/bps_positive_geometry_total_resolution_20260424/agent_05_hcs_hall_dwr_ran.md:205`
and `:354`.

### Cycle 4: Hall-Lower Saturation Under Extensions

**Attack.**  A bound `h(\gamma)\le N`, `|Z(\gamma)|\le R` is not
automatically a Hall quotient.  If `\alpha+\beta` is retained but one HN
factor lies outside the visible rectangle, the quotient kills data needed
for associativity.

**Failure mode.**  The compact gluing map can pass local checks but fail
when an overlap extension produces an HN factor outside the chosen
rectangular bound.  Then the complement is not a two-sided Hall ideal.

**Heal.**  Use the saturated Hall-lower closure
`L_{\le N,\le R}` and add the coordinate `o_lower`.  It vanishes exactly
when every retained compact Schoen extension has all HN factors retained
and the complement generates a closed two-sided Hall ideal.  This
preserves the finite-first theorem instead of weakening it.

### Cycle 5: Cech Descent of Chambers and Orientations

**Attack.**  Local chambers and local orientation square roots need not
descend.  A sign chosen on each banana chart can fail the triple-overlap
condition; local HN phase order can also fail on overlaps.

**Failure mode.**  The finite oracle can record zero placeholder values
for `overlap_orientation` and `HN_overlap` without computing the
orientation Cech cocycle or the HN overlap table.

**Heal.**  Split the Cech defect into two coordinates:

```tex
o_{\mathrm{or}}\in \check H^2(\mathfrak U_L,\mathbb Z/2),
\qquad
o_{\mathrm{HN}}\in \check C^1(\mathfrak U_L,\mathrm{PhaseOrd}).
```

The first is computed by determinant-line square-root transports as in
`notes/bps_positive_geometry_total_resolution_20260424/agent_02_orientation_oracle.md:826`.
The second vanishes when

```tex
\mathrm{HN}_{X}(j_{a,!}E)=j_{a,!}\mathrm{HN}_{a}(E)
```

and no active ray lands on the boundary of the strict sector after
transition.  Nonzero `o_or` does not kill the positive geometry; it
upgrades the output to the corresponding gerbe-twisted oriented motivic
positive geometry, as in the orientation oracle.

### Cycle 6: Monodromy and Wall Crossing

**Attack.**  A Schoen fibration has monodromy around singular fibers.
Even if local Hall charts glue on overlaps, transporting around a loop
can act by a nontrivial KS wall-crossing automorphism.  The compact
positive geometry needs this monodromy to agree with motivic integration
and sector transport.

**Failure mode.**  The local banana quasi-Jacobi data may be correct but
the compact wall transport can fail:

```tex
\Int^{\Mot}_{N,R}\circ T^{DWR}_{\wp,N,R}
 \ne
\operatorname{Ad}_{KS_{\wp,N,R}}\circ \Int^{\Mot}_{N,R}.
```

This is precisely the finite wall-transport equation visible in the
compact Hall construction package.

**Heal.**  Add `o_KS`, the finite monodromy/wall-transport coordinate.
It vanishes exactly when compact Schoen Cech transport, motivic
integration, and KS wall-crossing agree in every finite saturated
Hall-lower quotient and are compatible under the inverse-limit tower.

## Healed Schoen Point Theorem

Let `X_Sch` be a Schoen-type compact Calabi-Yau threefold with banana
local charts `U_a` over the singular fibers, and fix a realized strict
sector `S`.  For a finite saturated Hall-lower quotient `L=L_{\le N,\le R}`,
define the finite Schoen banana gluing vector

```tex
o_{\mathrm{Sch,ban},L}
=
(
o_{\mathrm{ssdeg}},
o_{\mathrm{charge}},
o_{\mathrm{BC}},
o_{\mathrm{or}},
o_{\mathrm{HN}},
o_{\mathrm{Mot}},
o_{\mathrm{lower}},
o_{\mathrm{KS}},
o_{\mathrm{pro}}
).
```

The coordinates are:

```text
o_ssdeg   : semistable degeneration does not restrict from a compact chamber;
o_charge  : compact-support charge pushforward / null-fiber quotient defect;
o_BC      : compact-support Beck--Chevalley defect for Hall extension stacks;
o_or      : determinant-line orientation Cech defect;
o_HN      : HN sector-order descent defect on overlaps;
o_Mot     : motivic integration, half-Tate, and orientation overlap defect;
o_lower   : failure of finite Hall-lower saturation under extensions;
o_KS      : monodromy / wall-crossing transport mismatch;
o_pro     : incompatibility under transition from larger finite quotients.
```

Then the finite compact Schoen Hall quotient is constructed if and only if

```tex
o_{\mathrm{Sch,ban},L}=0.
```

The compact Schoen point

```tex
\operatorname{ExCert}(X_{\mathrm{Sch}};\sigma,Q,S,o,T_{\mathrm{eq}},\Mot)
```

exists if and only if these finite vanishing statements hold on a
cofinal Mittag--Leffler tower of saturated Hall-lower sets and the
transition maps preserve the glued compact-support Hall correspondences.
This is stronger than the local banana theorem: the local theorem
survives as the construction of the chart input, while the compact point
is the simultaneous vanishing of the global gluing vector.

## Present Oracle Verdict

The current oracle now distinguishes the closed substack from the point.
The executed finite probe returned:

```text
certificate True False 4 ()
tower BananaShadowTower(... S4_instanton=Fraction(-44, 1),
                        shadow_class='M', r_max=-1, ...)
gv_total_3 -44
jacobi QuasiJacobiData(rank=2, weight=-2,
                       index_matrix=((2, -2), (-2, 2)),
                       is_meromorphic=True)
intersection ((-2, 2), (2, -2)) det 0
factor False True False
       ('charge_pushforward', 'compact_support_BC',
        'overlap_orientation', 'HN_overlap',
        'motivic_overlap', 'pro_continuity')
       False
```

Thus the previous false state, in which placeholder zeroes made Schoen
look solved, has been healed.  The remaining improvement is not to mark
Schoen solved, but to refine the six current coordinates into the
nine-coordinate vector above and provide executable witnesses for each
coordinate.

## Proposed Executable Oracle Hooks

Add, when code scope opens, a `CompactSchoenBananaGluingDatum` with:

```python
charge_pushforward_matrix
local_null_fiber_basis
semistable_restriction_table
beck_chevalley_squares
orientation_cech_matrix_F2
HN_overlap_phase_table
motivic_overlap_equalities
hall_lower_closure_witnesses
ks_monodromy_transport_matrices
pro_transition_commutators
```

and certificates:

```python
schoen_semistable_degeneration_certificate(datum, bound)
schoen_charge_pushforward_certificate(datum, bound)
schoen_compact_support_bc_certificate(datum, bound)
schoen_orientation_cech_certificate(datum, bound)
schoen_hn_overlap_certificate(datum, bound)
schoen_motivic_overlap_certificate(datum, bound)
schoen_hall_lower_saturation_certificate(datum, bound)
schoen_wall_transport_certificate(datum, bound)
schoen_pro_continuity_certificate(datum, bound)
schoen_banana_constructed_point_certificate(datum, bound)
```

The last certificate may pass only when every preceding coordinate is
computed and vanishes.  It must fail on the current local-only input.

## Commands Run

```text
pytest -q \
  compute/tests/test_bps_positive_truncation.py::test_schoen_banana_gluing_certificate \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_banana_shadow.py::TestBananaShadowIV::test_banana_shadow_structure_from_disjoint_sources
```

Result:

```text
4 passed in 0.32s
```

Additional direct probe:

```text
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound, derived_solution_stack_factors,
    schoen_banana_gluing_certificate,
)
from compute.lib.banana_shadow import (
    banana_shadow_tower, banana_genus0_gv_total, banana_jacobi_data,
    intersection_matrix_banana, intersection_determinant,
)
bound = TruncationBound(4,4)
cert = schoen_banana_gluing_certificate()
print('certificate', cert.passed, cert.exact, cert.checked_items, cert.discrepancies)
print('tower', banana_shadow_tower())
print('gv_total_3', banana_genus0_gv_total(3))
print('jacobi', banana_jacobi_data())
print('intersection', intersection_matrix_banana(), 'det', intersection_determinant())
for factor in derived_solution_stack_factors(bound):
    if factor.name == 'schoen_banana_gluing':
        print('factor', factor.solved, factor.zero_fiber_defined,
              factor.obstruction.computed, factor.obstruction.names,
              factor.obstruction.vanishes)
PY
```

Result summarized in the oracle verdict above.

## Files Changed

Only this assigned note was changed:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_02_schoen_banana_gluing.md
```

No code or TeX was edited.

## Remaining Obligations

1. Construct an actual compact Schoen stability/HN datum whose
   restrictions recover the banana local sectors.
2. Construct the compact-support charge pushforward from local banana
   curve sectors to `K_num(X_Sch)`, including the null fiber direction.
3. Prove compact-support Beck--Chevalley for Hall extension stacks in
   every finite saturated Hall-lower quotient.
4. Compute the orientation Cech class and either trivialize it or retain
   the gerbe-twisted coefficient system.
5. Prove HN chamber descent on overlaps and exclude sector-boundary
   active rays after transition.
6. Prove motivic integration compatibility on double and triple overlaps,
   including half-Tate and orientation factors.
7. Prove finite Hall-lower saturation for the compact Schoen gluing tower.
8. Compute monodromy/wall-crossing around the Schoen singular fibers and
   verify finite KS conjugation after motivic integration.
9. Prove pro-continuity under the cofinal Mittag--Leffler tower.

When these nine obligations are supplied, the Schoen/banana closed
substack becomes an actual compact non-toric constructed point.  Until
then, the current manuscript/oracle is correctly stronger than an
unsupported example claim: it names the exact zero-fiber geometry and
prevents the local banana shadow from masquerading as compact Hall
gluing.
