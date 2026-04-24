# Agent 03: K3 x E Full Hall-BKM Radical

## Attacked Claim

The attacked point-construction obligation is the raw unquotiented
`K3 x E` Hall-BKM bridge:

```tex
\CoHA^{Mot,o}_{crit}(K3\times E)^\wedge_S
\stackrel{?}{\cong}
\widehat U(\mathfrak g_{\Delta_5}^+).
```

The current theorem surface correctly states only the quotient theorem:

```tex
\CoHA^{Mot,o}_{crit}(K3\times E)^\wedge_S/Rad_{Aut}
\cong
\widehat U(\mathfrak g_{\Delta_5}^+),
```

with raw equality equivalent to `Rad_{Aut,<=N,<=R}=0` in every finite
quotient.  A finite Gram/nullity check is only the pairing coordinate of
this radical, not the full radical.

## Five Attack-Heal Cycles

### 1. Character theorem versus Hall theorem

**Attack.**  `Delta_5` fixes the automorphic denominator, not the
compact Hall algebra.  The character-level identities

```tex
AutBorch^{den}(\phi_{0,1})
=(\Delta_5,\nu_{\Delta_5},64^{-1}\Delta_5(2Z)),
\qquad
\kappa_{BKM}(\Delta_5)=f(0,0)/2=10/2=5,
```

determine the BKM denominator and its multiplier.  They do not construct
the compact oriented critical CoHA, the Hall commutator, the negative
half, the Hopf pairing, or the separated completion.

**Heal.**  The surviving theorem is the quotient theorem plus the raw
finite-radical criterion:

```tex
raw Hall-BKM(K3\times E)
\Longleftrightarrow
o_{rad}(N,R)=0 \text{ for all saturated finite Hall-lower } (N,R)
\text{ and the inverse-limit radical is separated.}
```

This strictly strengthens the earlier Gram test by replacing one matrix
kernel with the full Hall-Borcherds radical vector.

### 2. Hall bracket obstruction

**Attack.**  Sending a Hall fundamental class to
`c_{\phi_{0,1}}(-(\gamma,\gamma)/2,\ell_\gamma)e_\gamma` compares charge
labels and multiplicities.  It does not prove that the Hall
super-commutator on protected primitives equals the Borcherds bracket.
Two Lie superalgebras can have the same graded superdimension and
different structure constants.

**Heal.**  The bracket coordinate is the finite tensor residual

```tex
o_{br,N,R}(\alpha,\beta;\gamma)
 =
[\Pi_N x_\alpha,\Pi_N x_\beta]_{Hall}^{\gamma}
-
\Pi_N([e_{\alpha},e_{\beta}]_{\Delta_5}^{\gamma}).
```

The raw bridge requires `o_br,N,R=0` for every retained primitive pair,
not merely matching root multiplicities.

### 3. Protected integration obstruction

**Attack.**  The reduced DT character

```tex
Z^{red}_{DT}(K3\times E)=-\Phi_{10}^{-1}=-\Delta_5^{-2}
```

is a theorem-grade numerical shadow, but the protected integration map
may still fail to be a Hall character on the compact oriented critical
source.  It may kill extension data, see only Euler characteristics, or
fail compatibility with primitive/imprimitive splitting.

**Heal.**  The protected integration coordinate is the finite residual

```tex
o_{int,N,R}(\gamma)
= I^{prot}_{Aut,N,R}([\mathcal M_\gamma])
  - c_{\phi_{0,1}}(-(\gamma,\gamma)/2,\ell_\gamma),
```

together with the multiplicativity condition

```tex
I^{prot}_{Aut,N,R}(a*b)
= I^{prot}_{Aut,N,R}(a)I^{prot}_{Aut,N,R}(b)
```

on all retained Hall products.  The DT denominator closes only the
decategorified shadow; the Hall theorem needs this map on states.

### 4. Orientation character obstruction

**Attack.**  The Hall orientation branch may define a quadratic
refinement whose character differs from the automorphic multiplier
`\nu_{\Delta_5}`.  A correct denominator with a wrong orientation
character gives the wrong signed supermultiplicities and the wrong
super-commutator signs.

**Heal.**  The orientation coordinate is

```tex
o_{or,N,R}=\epsilon_{o,N,R}-\nu_{\Delta_5}|_{\Gamma_{\leq N,\leq R}},
```

plus the Cech/quadratic-refinement equations on the same finite
Hall-lower set.  Vanishing means the PTVV/Joyce orientation output and
the Gritsenko-Nikulin multiplier are the same character on the retained
charge lattice.

### 5. Imaginary Serre and primitive-root obstruction

**Attack.**  Borcherds multiplicities `sdim g_{\Delta_5,\alpha}=f(nm,l)`
do not by themselves impose the real Serre relations, imaginary
simple-root parities, or the quotient by the Borcherds-Serre ideal.
The Hall kernel could contain extra primitive relations, or miss a
Borcherds relation, while preserving the denominator character.

**Heal.**  The Serre coordinate is the finite ideal residual

```tex
o_{Serre,N,R}
 =
\ker(\Pi_{prim,N,R})/I^{Borcherds-Serre}_{N,R},
```

where `I^{Borcherds-Serre}_{N,R}` includes the real simple root Serre
relations, imaginary-root parity, and the multiplicity relations cut out
by `f(nm,l)`.  The raw theorem requires equality of ideals, not only
equality of graded dimensions.

### 6. Hopf pairing obstruction

**Attack.**  A positive half is not a Hall-Drinfeld double.  The double
requires a negative half, a Cartan part, a continuous non-degenerate
Hopf pairing, and compatibility of product and coproduct.  The positive
map to `U(g_{\Delta_5}^+)` cannot supply those data retroactively.

**Heal.**  The Hopf coordinate is the finite pairing residual

```tex
o_{copair,N,R}
=
(\langle a*b,c\rangle
 - \langle a\otimes b,\Delta c\rangle,
  \langle a,b*c\rangle
 - \langle \Delta a,b\otimes c\rangle,
  \ker\langle-,-\rangle_{N,R}).
```

The coordinate vanishes exactly when the retained positive and negative
halves form a finite Manin/Hopf pair modulo the Borcherds Cartan
radical.

### 7. Completion separatedness obstruction

**Attack.**  Vanishing through a bound is not vanishing in the completed
Hall algebra.  A tower can have zero finite visible kernel at selected
levels but still acquire a closed pro-radical if the transition maps are
not Mittag-Leffler, if the finite subsets are not saturated Hall-lower
sets, or if the completion is not separated.

**Heal.**  The completion coordinate is

```tex
o_{comp}
=
(\text{saturated Hall-lower closure},
 \text{closed two-sided transition ideals},
 \varprojlim^1 Rad_{Aut,N,R},
 \bigcap_k F^k\widehat H).
```

It vanishes when finite radical-zero is cofinal, functorial under
restriction, and the completed radical is the inverse limit of finite
radicals with no hidden pro-kernel.

## Full Obstruction Vector

For every finite saturated Hall-lower quotient:

```tex
o_{rad,N,R}
=
(o_{pair},o_{or},o_{int},o_{br},o_{Serre},o_{copair},o_{comp})_{N,R}.
```

Coordinate meanings:

- `o_pair`: kernel of the automorphic denominator pairing; the old
  Gram/nullity test sees only this coordinate.
- `o_or`: equality of the Hall orientation character with
  `nu_{Delta_5}`.
- `o_int`: protected integration as a Hall character with the
  `phi_{0,1}` coefficient oracle.
- `o_br`: primitive Hall bracket equals the BKM bracket.
- `o_Serre`: Hall primitive ideal equals the Borcherds-Serre ideal,
  including imaginary-root parity and multiplicity.
- `o_copair`: non-degenerate continuous Hopf pairing and coproduct
  compatibility for the Hall-Drinfeld double.
- `o_comp`: separated, Mittag-Leffler, closed-ideal completion.

The raw point exists exactly when this vector is computed from the named
`K3 x E` compact Hall geometry and vanishes for all finite quotients.

## Finite Oracle Representation

A finite oracle for the raw bridge must store:

```python
HallBorcherdsRadicalOracle(
    charges=L_N_R,
    hall_product=mu_N_R,
    hall_coproduct=Delta_N_R,
    primitive_projection=Prim_N_R,
    orientation_character=epsilon_o,
    automorphic_character=nu_Delta5,
    protected_integration=I_Aut,
    phi01_coefficient=c_phi01,
    pairing_matrix=G_Aut,
    hopf_pairing_matrix=G_Hopf,
    bracket_tensor=B_Hall - B_Delta5,
    serre_residuals=S_Hall / S_Delta5,
    completion_transition=T_N_R_to_Np_Rp,
)
```

It returns the exact seven-vector above.  The existing
`radical_non_degeneracy_certificate` is useful only as the `o_pair`
subroutine.  The current `full_hall_borcherds_radical_certificate` is
correctly non-exact: it records the full vector but does not compute it.

## Strongest Surviving Algebraic Statement

**Theorem-grade.**  The Igusa/Borcherds boundary normalization is fixed:

```tex
\phi_{0,1}=\sum f(n,l)q^n r^l,\qquad
f(0,0)=10,\qquad
\kappa_{BKM}(\Delta_5)=5,
```

```tex
AutBorch^{den}(\phi_{0,1})
=(\Delta_5,\nu_{\Delta_5},64^{-1}\Delta_5(2Z)),
\qquad
\Phi_{10}=\Delta_5^2.
```

The numerical compact `K3 x E` reduced DT character is

```tex
Z^{red}_{DT}(K3\times E)=-\Phi_{10}^{-1}=-\Delta_5^{-2}.
```

The four invariant lanes remain separated:

```tex
(\kappa_{cat},\kappa_{ch}^{Heis},\kappa_{BKM},\kappa_{fiber})
=(0,3,5,24).
```

**Conditional theorem.**  Given a compact oriented critical Hall cosheaf
on `K3 x E`, a protected primitive integration map, the character
identity `epsilon_o=nu_Delta5`, a primitive Lie-superalgebra comparison,
the Borcherds-Serre ideal equality, a continuous Hopf pairing, and a
separated Hall-lower completion, the raw unquotiented Hall-BKM bridge is
equivalent to `o_rad,N,R=0` for all finite saturated Hall-lower
quotients.  Under these hypotheses the quotient comparison upgrades to
the raw positive Hall algebra theorem.

## File Anchors

- `chapters/theory/bps_positive_geometry_closure.tex:286`: Igusa
  quotient boundary theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:300`: quotient
  Hall-Borcherds theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:309`: raw theorem
  equals finite radical-zero in every quotient.
- `chapters/theory/bps_positive_geometry_closure.tex:560`: full
  seven-coordinate radical vector.
- `chapters/theory/bps_positive_geometry_closure.tex:634`: proof states
  Gram nondegeneracy is only the pairing coordinate.
- `compute/lib/bps_positive_truncation.py:716`: old unquotiented radical
  ledger remains non-exact.
- `compute/lib/bps_positive_truncation.py:832`: finite Gram/nullity
  certificate, exact only for `o_pair`.
- `compute/lib/bps_positive_truncation.py:856`: full Hall-Borcherds
  radical certificate, non-exact ledger.
- `compute/lib/bps_positive_truncation.py:926`: current `k3e_raw_radical`
  obstruction names.
- `compute/lib/hall_borcherds_gate.py:75`: gate witness fields for the
  Hall/Borcherds comparison.
- `compute/lib/hall_borcherds_gate.py:116`: typed gate remains open
  unless all witnesses are supplied.
- `chapters/examples/k3e_cy3_programme.tex:111`: hCS-Hall-Borcherds
  comparison maps.
- `chapters/examples/k3e_cy3_programme.tex:141`: coefficient projection
  only compares positive half before double/centre/envelope.
- `chapters/examples/k3e_bkm_chapter.tex:13872`: quasi-NCCR character
  `-Phi_10^{-1}=-Delta_5^{-2}`.
- `chapters/examples/k3e_bkm_chapter.tex:13945`: six-route convergence
  remains a Hopf-superalgebra conjecture.
- `chapters/examples/k3e_bkm_chapter.tex:13992`: character-level physics
  theorem is conditional as a compact-CoHA character.
- `/Users/raeez/igusa-cusp-form/agent_material/10_chiral_koszul_construction_or_refusal.tex:84`:
  compact Hall enhancement requires orientation character, Hall double,
  and comparison maps.
- `/Users/raeez/igusa-cusp-form/agent_material/10_chiral_koszul_construction_or_refusal.tex:192`:
  scalar and denominator identities do not determine differential,
  product, Hall constants, or state comparison.
- `/Users/raeez/igusa-cusp-form/agent_material/07_chiral_koszul_factorization_boundary.tex:250`:
  normalization propagation does not construct the compact Hall cosheaf.

## Commands Run

```bash
pytest -q \
  compute/tests/test_hall_borcherds_gate.py \
  compute/tests/test_bps_positive_truncation.py::test_k3e_unquotiented_radical_certificate \
  compute/tests/test_bps_positive_truncation.py::test_radical_non_degeneracy_certificate_detects_kernel \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_igusa_product_formula.py::test_borcherds_product_matches_delta5_in_absolute_value
```

Result: `13 passed in 0.35s`.

```bash
python3 - <<'PY'
from compute.lib.bps_positive_truncation import (
    TruncationBound,
    constructed_named_points_certificate,
    derived_solution_stack_factors,
    full_hall_borcherds_radical_certificate,
)
from compute.lib.hall_borcherds_gate import (
    HallBorcherdsWitnesses,
    evaluate_gate,
    DELTA5_DATUM,
    k3xe_spectrum_tuple,
)

bound = TruncationBound(N=3, R_num=5)
cert = full_hall_borcherds_radical_certificate()
print(DELTA5_DATUM.kappa_BKM)
print(DELTA5_DATUM.square_weight)
print(k3xe_spectrum_tuple())
print(cert.exact, cert.passed)
print(evaluate_gate(HallBorcherdsWitnesses(
    denominator_normalization=True,
)).missing_witnesses)
print([
    (f.name, f.certificate.exact, f.obstruction.computed, f.obstruction.names)
    for f in derived_solution_stack_factors(bound)
    if f.name == "k3e_raw_radical"
])
print([d["factor"] for d in constructed_named_points_certificate(bound).discrepancies])
PY
```

Observed output:

```text
Delta5 kappa_BKM: 5
Phi10 square weight: 10
K3xE spectrum: ('0', '3', '5', '24')
full radical cert exact/passed: False True
open gate missing: ('oriented_critical_coha', 'hopf_pairing',
 'drinfeld_double', 'root_multiplicity_map', 'k3xe_spectrum_separated',
 'coha_positive_half_not_w', 'bkm_object_not_yangian')
k3e factor: [('k3e_raw_radical', False, False,
 ('pairing_kernel', 'orientation_character', 'protected_integration',
  'primitive_bracket', 'Serre_imaginary_relations', 'Hopf_pairing',
  'completion_separatedness'))]
constructed points unresolved: ['quintic_excert', 'schoen_banana_gluing',
 'k3e_raw_radical', 'theta_comparison', 'hcs_named_zero_fiber']
```

## Files Changed

Only this assigned report file was written:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_03_k3e_full_radical.md
```

No code or TeX files were edited.

## Remaining Obligations

1. Construct the compact oriented critical Hall cosheaf on `K3 x E` over
   a cofinal saturated Hall-lower tower.
2. Construct the protected integration map as a Hall character and prove
   its coefficient oracle is `c_{\phi_{0,1}}`.
3. Prove the orientation equality `epsilon_o=nu_Delta5` on the retained
   charge lattice and under transition maps.
4. Compute the primitive Hall bracket and prove equality with the
   Borcherds bracket of `g_{Delta5}`.
5. Prove equality of the Hall primitive relation ideal with the full
   Borcherds-Serre ideal, including imaginary roots and parity.
6. Construct the negative half, Cartan completion, continuous
   non-degenerate Hopf pairing, and coproduct compatibility.
7. Prove the Hall-lower completion is separated and that the inverse
   limit radical is exactly the inverse limit of finite radicals.

These are not downgrades.  They are the exact coordinates of the raw
`K3 x E` point-construction problem.
