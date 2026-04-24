# hCS-to-Hall Seven-Obstruction Attack

## claim attacked

The attacked claim is the compact-CY3 theorem
`chapters/theory/bps_positive_geometry_closure.tex:305-341`:

```tex
\Theta^{o}_{\hCS\to\Hall}:
\Obs^{q}_{\hCS}(-,\frakg)
\longrightarrow
\CoHA^{\Mot,o}_{\mathrm{crit}}(-)
```

exists in oriented Ran/Dolbeault--Weiss factorization cosheaves if and
only if

```tex
o_{\MC}=o_{\mathrm{or}}=o_{\mathrm{gr}}=o_{\mathrm{TS}}
=o_{\mathrm{fact}}=o_{\mathrm{cs}}=o_{\wedge}=0.
```

The same seven coordinates are then inserted into the derived zero
locus in `chapters/theory/bps_positive_geometry_closure.tex:471-578`.
The proof line under attack is the sentence
`Local stationary phase gives the chartwise map...`; that sentence
contains the construction of the map, the all-scale BV quantization,
and the comparison with vanishing cycles.

## strongest failure mode

The seven classes are descent obstructions for an already constructed
source, target, and chartwise comparison.  They are not, by themselves,
the construction of those data.

The manuscript already contains the sharper source-side conditions:

- `chapters/theory/cy3_chain_level_bridge.tex:76-101` defines
  quantum hCS observables only as a Costello--Gwilliam renormalized BV
  complex with effective interaction, heat-kernel BV Laplacian, and QME.
- `chapters/theory/cy3_chain_level_bridge.tex:294-361` makes the
  BV/bar comparison conditional on six inputs: Stage-1 formality,
  renormalization datum, quartic anomaly cancellation, strict nuclear
  completions, BV-to-bar transfer, and square-zero quantum bar
  coderivations.
- `chapters/theory/cy3_chain_level_bridge.tex:790-817` identifies the
  genuine CY3 local anomaly slot as the degree-4 Costello--Li invariant
  polynomial; this is not the lower-dimensional cubic slot.
- `chapters/theory/cy3_chain_level_bridge.tex:522-649` defines the
  oriented hCS--Hall comparison datum only after fixing anomaly-cancelled
  hCS, a DWR-good cover, charge monoid, stability, equivariant
  parameters, Hall orientation, shifts, Tate twists, completions, and
  simplexwise maps.
- `chapters/theory/cy3_chain_level_bridge.tex:654-704` proves a clean
  theorem: a supplied quasi-isomorphic oriented comparison datum gives
  the DWR/Ran morphism.  It explicitly states that it constructs no such
  datum.
- `chapters/theory/cy3_chain_level_bridge.tex:1042-1096` names the
  construction of the comparison as the first missing lemma.
- `chapters/theory/cy3_chain_level_bridge.tex:1100-1210` gives a
  five-class descent obstruction after source, target, compact-support
  convention, local normalisation, and chartwise maps have been fixed.

The closure chapter enlarges the five descent classes by adding
compact-support Beck--Chevalley and completion defects.  That is a
useful strengthening, but it still leaves four primitive construction
layers outside the seven-class tuple:

1. the all-scale gauge-fixed hCS package
   `(P_L, I[L], counterterms, RG flow, QME)`;
2. the Costello--Li anomaly trivialization, including the degree-4
   invariant-polynomial class and the gauge algebra hypothesis;
3. the oriented critical Hall atlas with compactly supported
   semistable moduli, vanishing cycles, orientation square roots,
   shifts, Tate twists, and completions;
4. the chartwise stationary-phase calibration maps and vertex
   quasi-isomorphism tests.

The compute surface confirms the same separation.  In
`compute/lib/bps_positive_truncation.py:750-770`,
`hcs_named_obstruction_certificate()` is explicitly `exact=False` and
has no derived geometry in its data.  In
`compute/lib/bps_positive_truncation.py:829-925`, the hCS factor in the
derived solution stack is an exact zero vector inserted by construction:

```python
names=("o_MC", "o_or", "o_gr", "o_TS", "o_fact", "o_cs", "o_wedge"),
values=(zero, zero, zero, zero, zero, zero, zero),
```

This proves the formal zero-fiber API, not the vanishing of obstruction
classes computed from a named compact CY3 geometry.

## fatal/nonfatal verdict

Fatal for the literal theorem if it is read as a construction theorem
for named compact CY3 geometries.

Nonfatal for the correct strengthened theorem.  The seven classes are
necessary and sufficient for DWR/Ran descent after the hCS source, Hall
target, compact-support convention, completion category, and chartwise
comparison maps have been constructed.  They are not sufficient for the
existence of those objects from first principles.

The sharp repair is therefore not a downgrade.  It replaces the
ambiguous seven-class statement by a stronger two-level theorem:

1. a primitive construction theorem for the hCS source, Hall target, and
   chartwise stationary-phase maps;
2. a descent theorem saying that the seven DWR/Ran classes are exactly
   the remaining obstruction to gluing those maps into
   `\Theta_{\hCS\to\Hall}^{\mathrm{or}}`.

## exact repair/heal theorem statement

### Theorem. Total hCS-to-Hall obstruction package

Let `X` be a compact smooth CY3 with holomorphic volume form
`\Omega_X`, and let `\mathfrak U` be a DWR-good cover.  Fix a metric
gauge Lie algebra `\mathfrak g`, a charge monoid `\Gamma`, a stability
sector, and equivariant parameters.  Let

```tex
\mathcal Q_{\hCS}(X,\mathfrak g)
=
(P_L,I[L],C[L],\mathrm{RG},\mathrm{QME},a_{\mathrm{anom}},
  e_c,\widehat{\otimes})
```

be the all-scale hCS package consisting of a gauge-fixing propagator,
effective interactions, counterterms, RG semigroup, QME solution,
Costello--Li anomaly trivialization, compact-support extension maps,
and completed tensor products.  Let

```tex
\mathcal H^{\mathrm{or},\wedge}_{\crit}(X)
```

be an oriented critical Hall atlas: PTVV `(-1)`-shifted symplectic
local Darboux charts, vanishing-cycle Borel--Moore complexes, KS/Joyce
orientation square roots, shifts `s(P,\gamma)`, Tate twists
`t(P,\gamma)`, Hall extension correspondences, and
charge/HN/equivariant completions.  Let

```tex
\theta=\{\theta_{\sigma,\gamma}\}
```

be a simplexwise stationary-phase family from hCS observables to the
oriented critical Hall complexes.

Define the total obstruction vector

```tex
\Omega_{\hCS,\Hall}(X,\mathfrak U,\mathfrak g,\theta)
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

Here:

- `\omega_{\mathrm{QME}}` is the failure of the renormalized BV
  differential to square to zero at all scales;
- `\omega_{\mathrm{anom}}` is the Costello--Li degree-4 anomaly class,
  with its chosen counterterm or trivialization;
- `\omega_{\mathrm{gf}}` is the gauge-fixing independence class for the
  heat-kernel propagator and harmonic projection;
- `\omega_{\mathrm{DWR}}` is the failure of the hCS source and Hall
  target to satisfy Weiss/DWR descent in the selected completed category;
- `\omega_{\mathrm{crit}}` is the failure to present the Hall target by
  compatible oriented critical charts;
- `\omega_{\mathrm{sp}}` is the failure to construct the chartwise
  stationary-phase maps;
- `\omega_{\mathrm{vqis}}` is the failure of the vertex maps to be
  quasi-isomorphisms after the fixed shifts, Tate twists, orientation,
  and completions;
- the seven `o_*` are the DWR/Ran descent, orientation, grading,
  Thom--Sebastiani, factorization, compact-support, and completion
  classes.

Then a global oriented hCS-to-Hall localization morphism

```tex
\Theta_{\hCS\to\Hall}^{\mathrm{or}}:
\Obs_{\hCS}^{q}(-,\mathfrak g)
\longrightarrow
\CoHA_{\crit}^{\mathrm{or},\wedge}(-)
```

exists and is a quasi-isomorphism on DWR/Weiss descent if and only if

```tex
\Omega_{\hCS,\Hall}=0.
```

Moreover, after fixing an anomaly-free all-scale hCS package, an
oriented critical Hall atlas, compact-support and completion
conventions, and vertex quasi-isomorphic stationary-phase maps, the
total theorem reduces exactly to the seven-class criterion

```tex
o_{\MC}=o_{\mathrm{or}}=o_{\mathrm{gr}}=o_{\mathrm{TS}}
=o_{\mathrm{fact}}=o_{\mathrm{cs}}=o_{\wedge}=0.
```

The space of global maps is then the Maurer--Cartan gauge quotient of
the complete Cech convolution dg Lie algebra
`\mathfrak M_{\hCS,\Hall}(\mathfrak U)`, with residual automorphisms
controlled by `H^0` and obstructions by `H^1`.

### K3 x E refinement

For the Kummer product `K3 x E` with abelian gauge, the local anomaly
and Hall-side orientation preparations are strong but not final:

- `chapters/theory/cy3_chain_level_bridge.tex:3136-3162` proves
  chartwise abelian anomaly vanishing.
- `chapters/theory/cy3_chain_level_bridge.tex:3164-3200` trivializes
  the Hall-side orientation torsor while explicitly saying this does
  not kill the relative comparison class.
- `chapters/theory/cy3_chain_level_bridge.tex:3203-3264` gives
  preparatory grading, Thom--Sebastiani, and factorization data while
  explicitly saying a chartwise comparison map is still required.
- `chapters/theory/cy3_chain_level_bridge.tex:3266-3300` states the
  K3 x E result as conditional on supplied chartwise
  quasi-isomorphisms and vanishing relative classes.
- `chapters/theory/cy3_chain_level_bridge.tex:3338-3372` states that
  all seven conditions hold only after the comparison datum is supplied.

Thus the K3 x E lane is the first serious compact test, but its point
construction is still the chartwise comparison datum plus relative
zero-class verification.

## local file anchors

- `chapters/theory/bps_positive_geometry_closure.tex:303-341`:
  seven-class theorem and proof line asserting local stationary phase.
- `chapters/theory/bps_positive_geometry_closure.tex:471-578`:
  derived zero locus using the seven hCS coordinates.
- `chapters/theory/cy3_chain_level_bridge.tex:76-101`:
  quantum hCS observables require renormalized BV data and QME.
- `chapters/theory/cy3_chain_level_bridge.tex:294-361`:
  quantum BV/bar comparison is conditional on six analytic and
  homotopical inputs.
- `chapters/theory/cy3_chain_level_bridge.tex:522-649`:
  oriented hCS--Hall comparison datum on the full DWR/Ran nerve.
- `chapters/theory/cy3_chain_level_bridge.tex:654-704`:
  supplied datum gives the morphism; no datum is constructed.
- `chapters/theory/cy3_chain_level_bridge.tex:790-817`:
  quartic Costello--Li anomaly slot and distinction from bar shadow data.
- `chapters/theory/cy3_chain_level_bridge.tex:1042-1210`:
  first missing lemma and five-class descent criterion after maps are
  fixed.
- `chapters/theory/cy3_chain_level_bridge.tex:1284-1317`:
  complete CY3 bridge datum includes the all-scale hCS package,
  strictification, comparison map, and global coherence.
- `chapters/theory/cy3_chain_level_bridge.tex:3125-3395`:
  K3 x E compact chart analysis remains conditional on supplied
  comparison maps and relative obstruction vanishing.
- `compute/lib/bps_positive_truncation.py:750-770`:
  hCS named obstruction certificate is a ledger and is not exact.
- `compute/lib/bps_positive_truncation.py:829-925`:
  derived solution stack inserts the hCS zero vector by construction.
- `compute/lib/c3_hcs_hall_theta.py:1-5`:
  finite-mode witness is only torus-fixed abelian shuffle localization.
- `compute/lib/k3_hcs_6d_oneloop.py:298-366`:
  one-loop negative oracle and Yang-family repair.
- `compute/lib/k3_hcs_6d_twoloop.py:462-500`:
  legacy two-loop hbar^5 obstruction remains nonzero.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_05_costello_bv_hcs.md:203-325`:
  prior attack on CFG shortcut, anomaly, compactness, and compute
  overclaim.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_01_gelfand_formal_moduli.md:424-545`:
  prior attack on quantum deformation, anomaly transfer, and the open
  hCS-to-Hall map.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_05_hcs_hall_dwr_ran.md:322-389`:
  seven-class descent theorem in note form.
- `notes/bps_positive_geometry_total_resolution_20260424/agent_05_hcs_hall_dwr_ran.md:462-504`:
  ten constructive compact-CY3 obligations.

## primary/literature anchors if needed from existing bibliography or local notes

- Costello--Gwilliam, factorization algebras in QFT:
  `bibliography/references.tex:90-94` and
  `bibliography/references.tex:423-425`.
- Costello--Li, twisted supergravity and quantization:
  `bibliography/references.tex:427-433`; local use is the CY3 quartic
  anomaly slot in `chapters/theory/cy3_chain_level_bridge.tex:790-817`.
- Pantev--Toen--Vaquie--Vezzosi shifted symplectic structures:
  `bibliography/references.tex:342-343`; local use is the oriented
  critical Hall atlas.
- Kontsevich--Soibelman motivic DT and Hall formalism:
  `bibliography/references.tex:707-708`.
- Schiffmann--Vasserot local positive-half model:
  `bibliography/references.tex:269-270`.
- Joyce--Song orientation data:
  `bibliography/references.tex:865`.

## executable checks proposed or run

Run:

```bash
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    hcs_named_obstruction_certificate,
    derived_solution_stack_factors,
    seven_extension_resolution_certificate,
)
b=TruncationBound(N=4,R_num=4)
for c in [hcs_named_obstruction_certificate(), seven_extension_resolution_certificate(b)]:
    print(c.name, c.exact, c.checked_items, c.passed, c.discrepancies)
for f in derived_solution_stack_factors(b):
    if 'hcs' in f.name:
        print(f.name, f.certificate.exact, f.certificate.discrepancies, f.obstruction.nonzero_entries())
PY
```

Observed:

```text
hcs_named_obstructions exact=False checked=7 passed=True discrepancies=()
seven_extension_resolution exact=False checked=449 passed=True discrepancies=()
hcs_named_zero_fiber cert_exact=True cert_discrepancies=() obs_nonzero=()
```

Interpretation: the seven-class named certificate is not exact; the
exact hCS zero fiber is formal input data.

Run:

```bash
python3 - <<'PY'
from compute.lib.c3_hcs_hall_theta import (
    C3EquivariantParameters, hcs_mode, shuffle_product,
    direct_binary_localization, continuity_bound_for_modes,
)
params=C3EquivariantParameters(1,2,-3)
prod=shuffle_product(hcs_mode(0), hcs_mode(1), params)
print(prod.arity, prod.is_zero(), continuity_bound_for_modes((0,1)))
print((prod.expr-direct_binary_localization(0,1,params)).simplify()==0)
PY
```

Observed:

```text
c3 arity 2 is_zero False bound (2, 1, 1)
binary equals direct True
```

Interpretation: the C3 chart witness checks the abelian torus-fixed
shuffle localization; it does not construct compact hCS localization.

Run:

```bash
python3 - <<'PY'
from compute.lib.k3_hcs_6d_oneloop import ybe_at_order
from compute.lib.k3_hcs_6d_twoloop import (
    legacy_twoloop_hbar5_obstruction_exact,
    one_loop_normalization_condition,
)
r=ybe_at_order(N=2, c_v=2.0, hbar=0.01, u=2.3, v=1.7)
print(r['naive_fish_ybe_preserved_at_hbar3'])
print(r['renormalized_yang_exact_ybe'])
o=one_loop_normalization_condition(c_v=2.0,u=2.3,v=1.7)
print(o['naive_obstruction_vanishes'])
print(o['normalized_obstruction_vanishes'])
t=legacy_twoloop_hbar5_obstruction_exact(2,3)
print(t['legacy_hbar5_obstruction_vanishes'])
print(t['legacy_hbar5_obstruction'])
PY
```

Observed:

```text
naive fish preserved at hbar3: False
renormalized Yang exact YBE: True
one-loop naive obstruction vanishes: False
one-loop normalized obstruction vanishes: True
legacy two-loop hbar5 vanishes: False
legacy obstruction: {'P12P23': '-22209137500/210517137', 'P23P12': '22209137500/210517137'}
```

Interpretation: BV renormalization and counterterm choices are genuine
data; the hCS Feynman input is not automatically zero-class.

Run:

```bash
pytest -q \
  compute/tests/test_bps_positive_truncation.py \
  compute/tests/test_c3_hcs_hall_theta.py \
  compute/tests/test_k3_hcs_6d_oneloop.py \
  compute/tests/test_k3_hcs_6d_twoloop.py
```

Observed:

```text
52 passed in 4.97s
```

Interpretation: the current executable surface is internally
consistent with the healed theorem: finite zero-fiber certificates,
torus-fixed chart localization, and hCS renormalization probes pass.
None of these tests computes the compact-CY3 total obstruction vector.

## remaining point-construction obligation

For a named compact CY3 geometry, the remaining point-construction is:

1. choose a DWR-good cover and gauge datum;
2. construct `\mathcal Q_{\hCS}` at all scales, including gauge fixing,
   heat kernel, counterterms, QME, RG, anomaly trivialization, and
   compact-support extension on all higher intersections;
3. construct the oriented critical Hall atlas with PTVV Darboux charts,
   vanishing cycles, orientation square roots, shifts, Tate twists, and
   completions;
4. construct the simplexwise stationary-phase maps
   `\theta_{\sigma,\gamma}`;
5. prove the vertex maps are quasi-isomorphisms;
6. compute the total obstruction vector above and produce explicit
   null-homotopies for every non-primitive descent coordinate.

For `K3 x E` in the Kummer abelian sector, steps 2 and the Hall-side
orientation part have substantial local evidence, but the point is not
complete until the supplied comparison maps and the relative seven
classes are explicitly constructed on the DWR nerve.
