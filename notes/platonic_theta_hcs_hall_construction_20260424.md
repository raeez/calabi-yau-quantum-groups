# Platonic theta hCS--Hall construction note

Date: 2026-04-24.

Owned scope: this note only.  The executable `C^3` files were read as a local
chart witness and left unchanged.

## Claim attacked

The attacked claim is the strongest possible reading of the existing
hCS--Hall criterion:

```text
The criterion plus the finite torus-fixed C^3 shuffle witness constructs the
global compact arrow

  Theta^{or}_{hCS->Hall} :
    Obs^q_hCS(-,g) -> CoHA^{or}_{crit}(-)

on K3 x E.
```

This claim is false.  The criterion is exact, but it is a criterion.  The
finite `C^3` witness constructs only the positive torus-fixed abelian
projection of the local chart map.  It does not produce the renormalised
hCS-to-Hall map, the DWR/Ran higher-simplex data, or the compact orientation,
grading, Thom--Sebastiani, factorisation, and quasi-isomorphism primitives.

## Source anchors

- `chapters/theory/cy3_chain_level_bridge.tex:1039` states the hCS--Hall
  comparison as an open problem.
- `chapters/theory/cy3_chain_level_bridge.tex:1099` defines the mapping dg
  Lie algebra and the obstruction tuple
  `(o_MC,o_or,o_gr,o_TS,o_fact)`.
- `chapters/theory/cy3_chain_level_bridge.tex:1152` proves the descent
  criterion: chartwise quasi-isomorphisms extend globally iff the obstruction
  tuple vanishes and the MC element is invertible on the DWR nerve.
- `chapters/theory/cy3_chain_level_bridge.tex:1903` defines the
  simplex-by-simplex witness maps and five nullhomotopies.
- `chapters/theory/cy3_chain_level_bridge.tex:2630` constructs only the
  compact open--closed source bridge and explicitly does not construct the
  Hall-valued comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:2867` makes the `C^3` five-way
  normal form conditional on a supplied chartwise hCS--Hall map.
- `chapters/theory/cy3_chain_level_bridge.tex:3264` says the fixed
  finite-mode chart kills only the projected fixed abelian piece and makes no
  claim about analytic extension or descent.
- `compute/lib/c3_hcs_hall_theta.py:1` records the local finite-mode scope.
- `compute/lib/c3_hcs_hall_theta.py:120` implements
  `theta_c3_fixed_modes`, the actual constructed fixed-sector map.
- `compute/lib/cy3_renormalised_extension_gate.py:32` lists the extra local
  gates from finite fixed chart to renormalised local chart and then DWR
  descent.
- `compute/lib/cy3_bridge_normal_form.py:1` says the bridge module records
  gates and does not construct the missing hCS-to-Hall map.

## Constructed component

The only genuine construction currently available is

```text
theta^{fp,+}_{C3}: Obs^{q,fp,+}_{hCS}(C^3; ghat) -> Y_T^+(ghat),
theta^{fp,+}_{C3}(J_m) = z_1^m,
```

extended multiplicatively by the Schiffmann--Vasserot shuffle kernel

```text
phi_SV(delta) =
 ((delta+eps_1)(delta+eps_2)(delta+eps_3))
 /(delta(delta+eps_1+eps_2)(delta+eps_2+eps_3)),
 eps_1+eps_2+eps_3 = 0.
```

This is exactly the finite torus-fixed abelian chart:

- source: positive fixed shuffle-normal-form quotient, not the full
  Costello--Gwilliam/Costello--Li renormalised observable complex;
- differential: zero on the selected fixed sector;
- target: the cohomological positive shuffle model `CoHA(C^3)=Y^+`, not
  the full oriented critical CoHA with shifts, Tate twists, and
  Thom--Sebastiani transport;
- topology: finite mode filtration by arity, mode weight, and pair-pole
  bound, not the nuclear LF/DFS source topology and charge/HN/equivariant
  completed Hall target.

Thus the available theorem proves

```text
o_theta^{fp,+} = 0.
```

It does not prove `o_theta^{ren}=0` or `o_theta^{des}=0`.

## Primitive-by-primitive attack

### 1. `theta^(0)`

`theta^(0)` for the criterion means 0-simplex maps

```text
theta_i : Obs^q_hCS(U_i,g) -> CoHA^{or}_{crit}(U_i)
```

on every DWR-good chart, with the fixed compact-support, orientation,
completion, shift, and Tate conventions.

The constructed `C^3` map gives only the boundary condition on the
projected fixed abelian quotient.  It does not give `theta_i` for the full
renormalised hCS source because no continuous transfer

```text
Theta_L^{ren} : Obs^q_hCS(C^3;ghat) -> CoHA^{or}_{crit}(C^3)
```

has been constructed that intertwines

```text
Q_hCS + {I[L],-}_{BV} + hbar Delta_L
```

with the Hall differential.  It also does not globalise to compact
`K3 x E`: the compact geometry has no global toric `T^3` fixed-point
presentation, and a DWR cover introduces overlap, orientation, grading,
and factorisation data absent from the one-chart fixed model.

Conclusion: constructed only as `theta^{fp,+}_{C3}`; obstructed as a full
`theta^(0)` by the unconstructed renormalised transfer and compact DWR
chart family.

### 2. `eta_MC`

The MC primitive must satisfy

```text
d eta_MC = d theta + (1/2)[theta,theta]
```

inside the completed Cech/Ran mapping dg Lie algebra
`Tot Cech^bullet(U,Hom_cont(Obs^q_hCS,CoHA^{or}_{crit}))`.

The finite `C^3` witness has no nontrivial Cech direction and no full
renormalised differential.  Therefore the MC residual on compact
`K3 x E` is not even a computed cochain until the maps `theta_i` and their
restrictions to all intersections are supplied.

Conclusion: no `eta_MC` is constructed.  The obstruction is not a proved
nonzero class; it is the absence of the cochain whose exactness could be
tested.

### 3. `lambda_or`

The orientation primitive must trivialise the relative square-root
mismatch between the hCS BV determinant transport and the
Kontsevich--Soibelman/Joyce orientation local system on the critical Hall
side.  It is not the Hall orientation notation alone.  It is a Cech
primitive for the relative `Z/2` cocycle on overlaps and triple overlaps.

The fixed `C^3` chart can use the standard toric orientation convention
inside a contractible affine model.  That supplies no compact square-root
transport on `K3 x E`, no comparison with the hCS determinant line, and no
triple-overlap cocycle trivialisation.

Conclusion: `lambda_or` remains open.  The first concrete target is a
relative determinant-line isomorphism on every overlap, compatible with
Hall extension correspondences.

### 4. `eta_gr`

The grading/Tate primitive must identify the hCS cohomological degree with
the perverse vanishing-cycle shift `s(U,d)` and Tate twist `t(U,d)` in the
local critical CoHA normalisation.

The executable `C^3` witness records only arity, mode weight, and
pair-pole bound.  Those are useful filtration metadata, but they are not
the perverse/Tate shifts of the oriented critical CoHA.  In compact
`K3 x E`, shifts must also be compatible with charge/HN completion,
equivariant localisation, and restriction to intersections.

Conclusion: no `eta_gr` is constructed.  The required object is an
integer/Tate Cech cochain whose coboundary is the shift mismatch.

### 5. `H_TS`

The Thom--Sebastiani primitive must compare the two parenthesisations of
iterated Hall extensions, including orientation local-system transport:

```text
((E_1 * E_2) * E_3)  versus  (E_1 * (E_2 * E_3)).
```

The `C^3` binary test checks the two-point shuffle/localisation formula.
It does not produce a chain homotopy for all iterated Hall
correspondences, nor does it include vanishing cycles with orientation
local systems.

Conclusion: no `H_TS` is constructed.  A binary shuffle formula is not a
Thom--Sebastiani associator homotopy on the compact Hall correspondence
stack.

### 6. `H_fact`

The factorisation primitive must prove compatibility with disjoint
Ran/DWR products:

```text
Theta_{sigma_1 sqcup sigma_2} mu_BV
  ~
mu_Hall^{TS,or}(Theta_{sigma_1} tensor Theta_{sigma_2}).
```

The fixed shuffle multiplication is an internal product of modes in one
affine chart.  It is not disjoint-polydisc factorisation, does not compare
restriction maps in a Weiss cover, and does not give the higher homotopies
for all Ran decompositions.

Conclusion: no `H_fact` is constructed.  It remains a separate DWR/Ran
factorisation problem.

### 7. `Q`

`Q` is the completed quasi-isomorphism certificate.  It must verify that
the vertexwise maps preserve the hbar-adic, charge/HN, equivariant,
orientation, shift, Tate, and compact-support conventions, and that they
are quasi-isomorphisms in the completed category.

The current tests verify the finite kernel, binary localisation, zero
fixed-sector differential, and filtration metadata.  They do not compare
the cohomology of the full renormalised hCS BV complex with the oriented
critical CoHA complex.

Conclusion: no `Q` is constructed.  A future `Q` must be an actual
quasi-isomorphism proof, not a gate label.

## Compact `K3 x E` verdict

The compact arrow is not solved.  The exact current state is:

```text
theta^{fp,+}_{C3} exists,
o_theta^{fp,+}=0,
o_theta^{ren} open,
o_theta^{des} open,
(eta_MC, lambda_or, eta_gr, H_TS, H_fact, Q) open.
```

For compact `K3 x E`, even a future renormalised `C^3` chart map would
still not imply the global arrow.  The DWR/Ran cover introduces the five
descent obstructions, and the compact Hall target introduces the oriented
critical atlas, HN completion, Thom--Sebastiani transport, and Joyce/KS
orientation branch.

This is a proof-grade obstruction to the inference

```text
finite C^3 fixed chart  =>  global Theta^{or}_{hCS->Hall}.
```

It is not a proof that the global compact arrow cannot exist.  The correct
mathematical status is conditional/open: construct the seven primitives
above, or compute a genuine nonzero obstruction class in the completed
DWR/Ran mapping complex.

## Narrow executable witness status

No compute edit was natural in this pass.  The existing executable surface
already states the needed separation:

- `compute/tests/test_c3_hcs_hall_theta.py` verifies the finite fixed
  `C^3` algebra witness.
- `compute/tests/test_cy3_renormalised_extension_gate.py` verifies that the
  fixed chart leaves `o_theta^{ren}` and `o_theta^{des}` open.
- `compute/tests/test_cy3_bridge_normal_form.py` verifies that even a
  local chart map does not close the global hCS--Hall target without DWR
  descent gates.

## Remaining primitive obligations

1. Build `Theta_L^{ren}` on the full `C^3` renormalised hCS observable
   complex and prove continuity into the oriented critical CoHA completion.
2. Prove differential compatibility with
   `Q_hCS + {I[L],-}_{BV} + hbar Delta_L`.
3. Lift the `Y^+` shuffle target to the oriented critical CoHA chain target
   with shifts, Tate twists, and Thom--Sebastiani data.
4. Produce the DWR/Ran chart family `theta_i` on a compact `K3 x E` cover.
5. Produce `eta_MC`, `lambda_or`, `eta_gr`, `H_TS`, and `H_fact` as actual
   cochains/homotopies on that nerve.
6. Produce `Q`, the completed quasi-isomorphism certificate.
7. Only after these six steps should the Hall--Borcherds and Drinfeld
   double layers be invoked for compact `K3 x E`.
