# Agent 03: K3 x E Hall-Borcherds Radical Execution

## Claim Under Attack

The point-construction obligation is the raw unquotiented Hall-BKM bridge
for the compact Calabi-Yau threefold \(X=K3\times E\):

```tex
\CoHA^{\Mot,o}_{\mathrm{crit}}(X)^\wedge_S
\stackrel{?}{\cong}
\widehat U(\mathfrak g_{\Delta_5}^+).
```

The theorem-grade result already available is the quotient statement

```tex
\CoHA^{\Mot,o}_{\mathrm{crit}}(X)^\wedge_S/
\operatorname{Rad}_{\Aut}
\cong
\widehat U(\mathfrak g_{\Delta_5}^+),
```

where the Igusa denominator determines the automorphic target and the
closed Hall ideal \(\operatorname{Rad}_{\Aut}\) is the kernel invisible to
the automorphic denominator, orientation character, protected
integration, bracket comparison, Serre ideal, Hopf pairing, and
completion. The raw point exists exactly when the full seven-coordinate
radical vanishes in a cofinal tower of finite sectorial HN/Hall
quotients. A Gram-nullity check is only the first coordinate.

## Theorem-Grade Quotient

Let

```tex
\phi_{0,1}=\sum f(n,l)q^nr^l,
\qquad
f(0,0)=10,
\qquad
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}.
```

The Igusa normalization gives

```tex
\kappa_{\mathrm{BKM}}(\Delta_5)=f(0,0)/2=5,
\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})
=64^{-1}\Delta_5(2Z),
\qquad
\Delta_{10}=\Delta_5^2.
```

In the Oberdieck-Pandharipande/Igusa normalization,

```tex
Z^{K3\times E}_{\mathrm{OP}}=-4096\,\Delta_5^{-2};
```

in the normalized \(\Phi_{10}\) convention this is the same scalar square
statement \(Z^{\mathrm{red}}_{\mathrm{DT}}=-\Phi_{10}^{-1}\). The four
\(\kappa_\bullet\)-lanes are separated:

```tex
(\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
 \kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}})
=(0,3,5,24).
```

These formulas construct the denominator algebra
\(\mathfrak g_{\Delta_5}\), its multiplier \(\nu_{\Delta_5}\), and the
character-level quotient target. They do not construct the compact Hall
source or remove the radical.

## Raw Iff Theorem

Fix a stability condition \(\sigma\), a strict sector \(S\), and the
\(h_S\)-adic finite Hall quotient

```tex
\mathsf F_R\Hall^{or}_{\sigma,S}
=\Hall^{or}_{\sigma,S}/\Hall^{>R}_{\sigma,S},
\qquad
h_S(\gamma)=\Re(e^{-i\vartheta}Z_\sigma(\gamma))>0.
```

Assume support property, local finiteness, HN existence, an oriented
critical Hall atlas, compact-support vanishing-cycle pull-push
correspondences, and transition maps by closed Hall ideals. For each
finite quotient define

```tex
o_{\mathrm{rad},R}
=
(o_{\mathrm{pair}},o_{\mathrm{or}},o_{\mathrm{int}},
  o_{\mathrm{br}},o_{\mathrm{Serre}},
  o_{\mathrm{copair}},o_{\mathrm{comp}})_R.
```

Then the raw Hall-BKM point exists iff

```tex
o_{\mathrm{rad},R}=0\quad\text{for every cofinal finite quotient }R,
\qquad
\operatorname{Rad}_{\Aut}
=\varprojlim_R \operatorname{Rad}_{\Aut,R}
\quad\text{and the completion is separated.}
```

This is strictly stronger than the quotient theorem. It keeps the
Igusa/Borcherds algebra as a theorem and converts the raw compact
statement into seven explicit zero coordinates.

## Attack-Heal Cycles

### 1. Denominator Character Is Not a Hall Algebra

**Attack.** The identities

```tex
\operatorname{Borch}(\phi_{0,1})=\Delta_5,
\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)
```

determine a BKM denominator and signed root supermultiplicities. They do
not construct a compact oriented critical CoHA, a Hall convolution, a
primitive projection, a negative half, or a Hall-Drinfeld double.

**Heal.** The theorem-grade object is the quotient
\(\CoHA/\operatorname{Rad}_{\Aut}\). The raw theorem is not asserted
from the denominator; it is the finite radical-zero criterion above.
The Hall-Borcherds gate correctly reports `OPEN_TYPED_GATE` when only
`denominator_normalization=True`.

### 2. Raw Igusa Lower Sets Are Not Finite Hall Quotients

**Attack.** A finite lower set in the raw product cone
\(\Gamma_{\mathrm{eff}}\) cannot contain an interior charge such as
\((1,0,1)\). For every \(a\in\mathbb Z\),

```tex
(1,0,1)=(1,a,0)+(0,-a,1),
```

and both summands lie in the raw effective cone. Raw lower closure is
infinite.

**Heal.** Finite-first means HN-first. The finite quotient is the
\(h_S\)-adic sector quotient by charges of \(h_S\)-height \(>R\), with
finiteness supplied by the support property and local finiteness. Thus
the completion coordinate \(o_{\mathrm{comp}}\) must include HN
finiteness, closed transition ideals, and separated inverse limit.

### 3. Pairing Kernel Is Only One Coordinate

**Attack.** The certificate
`radical_non_degeneracy_certificate(name, gram)` computes only the kernel
of a finite automorphic Gram matrix. A full-rank Gram matrix does not
prove orientation equality, protected integration, bracket equality,
Borcherds-Serre relations, Hopf compatibility, or pro-separatedness.

**Heal.** The pairing coordinate is

```tex
o_{\mathrm{pair},R}=\ker G_{\Aut,R}.
```

It is useful as an exact subroutine but not as the raw theorem. The live
oracle records this separation: `full_hall_borcherds_radical_certificate`
is `exact=False`, while a singular toy Gram matrix produces the exact
discrepancy `{"check": "Rad_Aut=0", "nullity": 1}`.

### 4. Orientation Character Must Equal the Igusa Multiplier

**Attack.** A Joyce/PTVV orientation branch gives signs for
vanishing-cycle Hall multiplication. It need not induce the Maass
character \(\nu_{\Delta_5}\). A wrong boundary character preserves many
dimensions and still changes the supercommutator signs.

**Heal.** The orientation coordinate is

```tex
o_{\mathrm{or},R}
=\epsilon_{o,R}-\nu_{\Delta_5}|_{\Gamma_R}.
```

It includes Cech square-root coherence, Thom-Sebastiani transport on
extension stacks, \(E\)-equivariance for the reduced quotient, and
compatibility with transition maps.

### 5. Protected Integration Must Be a Hall Character on States

**Attack.** The scalar identity

```tex
Z^{K3\times E}_{\mathrm{OP}}=-4096\,\Delta_5^{-2}
```

is a decategorified determinant. It does not identify state spaces and
does not show that protected integration is multiplicative for Hall
pull-push.

**Heal.** The protected integration coordinate is

```tex
o_{\mathrm{int},R}(\gamma)
=I^{\mathrm{prot}}_{\Aut,R}
  (\Prim_{\mathrm{prot},\gamma})
  - f(nm,l),
```

together with

```tex
I^{\mathrm{prot}}_{\Aut,R}(a*b)
=I^{\mathrm{prot}}_{\Aut,R}(a)I^{\mathrm{prot}}_{\Aut,R}(b)
```

for every retained product. Vanishing says the Igusa coefficient oracle
is realized by the compact Hall object, not merely by a scalar shadow.

### 6. Primitive Bracket and Serre Relations Are Independent Data

**Attack.** The product

```tex
64^{-1}\Delta_5(2Z)
=e^{-2\pi i(\rho,z)}
\prod_\alpha (1-e^{-2\pi i(\alpha,z)})^{\operatorname{sdim}\mathfrak g_\alpha}
```

determines signed integers. It does not determine the parity dimensions
separately and does not determine the structure constants
\([\mathfrak g_\alpha,\mathfrak g_\beta]\to\mathfrak g_{\alpha+\beta}\).

**Heal.** The bracket coordinate is

```tex
o_{\mathrm{br},R}(\alpha,\beta;\gamma)
=
[\Pi_Rx_\alpha,\Pi_Rx_\beta]^{\gamma}_{\Hall}
-\Pi_R([e_\alpha,e_\beta]^{\gamma}_{\Delta_5}),
```

and the Serre coordinate is

```tex
o_{\mathrm{Serre},R}
=I^{\Hall}_{\mathrm{prim},R}/I^{\mathrm{Borcherds-Serre}}_{\Delta_5,R}.
```

The raw bridge requires real-root Serre relations, imaginary-root
parities, multiplicity relations, and orthogonality relations in the
Hall primitive algebra itself.

### 7. Hopf Pairing and Separated Completion Close the Double

**Attack.** A positive-half map
\(\widehat{\CoHA}^{+}\to \widehat U(\mathfrak g_{\Delta_5}^{+})\) does
not construct a Drinfeld double. The double needs a negative half, Cartan
part, coproduct, continuous Hopf pairing, radical quotient, and a
separated completion.

**Heal.** The Hopf coordinate is

```tex
o_{\mathrm{copair},R}
=
(\langle a*b,c\rangle-\langle a\otimes b,\Delta c\rangle,
 \langle a,b*c\rangle-\langle\Delta a,b\otimes c\rangle,
 \ker\langle-,-\rangle_R).
```

The completion coordinate is

```tex
o_{\mathrm{comp}}
=
(\mathrm{HN\ finite\ quotient},\mathrm{closed\ transition\ ideals},
 \varprojlim\nolimits^1\operatorname{Rad}_{\Aut,R},
 \bigcap_k F^k\widehat\Hall).
```

Vanishing says the finite radical-zero statements assemble into an
actual completed Hall-Drinfeld double with no hidden pro-radical.

## Exact Gate and Witness Signatures

The current executable gate has the coarse implication signature

```python
HallBorcherdsWitnesses(
    oriented_critical_coha: bool,
    hopf_pairing: bool,
    drinfeld_double: bool,
    denominator_normalization: bool,
    root_multiplicity_map: bool,
    k3xe_spectrum_separated: bool,
    coha_positive_half_not_w: bool,
    bkm_object_not_yangian: bool,
)
```

The raw radical point needs the refined witness signature:

```python
K3EHallBorcherdsRadicalWitness(
    quotient,                    # finite HN/Hall quotient F_R Hall
    automorphic_pairing_matrix,   # o_pair
    hall_orientation_character,   # o_or source
    nu_delta5_character,          # o_or target
    protected_integration,        # o_int source
    phi01_coefficient_oracle,      # o_int target
    primitive_projection,
    hall_bracket_tensor,          # o_br source
    bkm_bracket_tensor,           # o_br target
    hall_primitive_relation_ideal, # o_Serre source
    bkm_serre_ideal,              # o_Serre target
    hall_coproduct,
    negative_half,
    cartan_completion,
    hopf_pairing_matrix,          # o_copair
    transition_maps,
    closed_transition_ideals,
    separated_completion_check,   # o_comp
)
```

The returned exact obstruction vector is

```python
(
    pairing_kernel,
    orientation_character,
    protected_integration,
    primitive_bracket,
    Serre_imaginary_relations,
    Hopf_pairing,
    completion_separatedness,
)
```

The current live `k3e_raw_radical` factor has exactly these seven names,
is `zero_fiber_defined=True`, and is not solved because
`computed=False`.

## File Anchors

- `chapters/theory/bps_positive_geometry_closure.tex:286`: Igusa quotient
  boundary theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:300`: quotient
  Hall-Borcherds theorem.
- `chapters/theory/bps_positive_geometry_closure.tex:309`: raw theorem
  equals finite radical-zero.
- `chapters/theory/bps_positive_geometry_closure.tex:592`: full
  seven-coordinate Hall-Borcherds radical vector.
- `chapters/theory/bps_positive_geometry_closure.tex:667`: proof states
  Gram nondegeneracy is only the pairing coordinate.
- `compute/lib/bps_positive_truncation.py:716`: legacy unquotiented
  radical ledger, non-exact.
- `compute/lib/bps_positive_truncation.py:910`: finite Gram/nullity
  certificate for the pairing coordinate.
- `compute/lib/bps_positive_truncation.py:934`: full Hall-Borcherds
  radical certificate, non-exact.
- `compute/lib/bps_positive_truncation.py:1004`: `k3e_raw_radical`
  seven-coordinate obstruction vector.
- `compute/tests/test_bps_positive_truncation.py:318`: test that the full
  radical certificate is not Gram-only.
- `compute/tests/test_bps_positive_truncation.py:420`: zero-fiber tests
  enforce unresolved named factors.
- `compute/lib/hall_borcherds_gate.py:75`: coarse Hall-Borcherds witness
  dataclass.
- `compute/lib/hall_borcherds_gate.py:116`: gate evaluation remains open
  unless all witnesses are supplied.
- `chapters/examples/k3e_cy3_programme.tex:111`: K3 x E hCS-Hall-Borcherds
  comparison maps.
- `chapters/examples/k3e_cy3_programme.tex:141`: coefficient projection
  compares only the positive half before double/center/envelope.
- `chapters/examples/k3e_bkm_chapter.tex:13888`: four separated
  \(\kappa_\bullet\)-lanes on \(K3\times E\).
- `chapters/examples/k3e_bkm_chapter.tex:13926`: quasi-NCCR scalar
  character \(=-\Phi_{10}^{-1}=-\Delta_5^{-2}\).
- `chapters/examples/k3e_bkm_chapter.tex:14001`: six-route convergence is
  conditional on finite-height Hall-BKM package maps.
- `/Users/raeez/igusa-cusp-form/proj.tex:56`: OP/Igusa scalar square
  \(Z_{\mathrm{OP}}=-4096\Delta_5^{-2}\).
- `/Users/raeez/igusa-cusp-form/proj.tex:1397`: microscopic
  Hall-Drinfeld datum.
- `/Users/raeez/igusa-cusp-form/proj.tex:1423`: realization criterion for
  the protected Igusa BPS bracket.
- `/Users/raeez/igusa-cusp-form/proj.tex:1713`: denominator determines
  signed dimensions but not parity or structure constants.
- `/Users/raeez/igusa-cusp-form/proj.tex:2344`: two exponential
  normalizations, \(64^{-1}\Delta_5(2Z)\).
- `/Users/raeez/igusa-cusp-form/agent_material/08_compact_hall_factorization_object.tex:293`:
  Igusa Hall-Borcherds comparison datum.
- `/Users/raeez/igusa-cusp-form/agent_material/10_compact_hall_atlas_attack_heal.tex:105`:
  raw finite lower sets fail.
- `/Users/raeez/igusa-cusp-form/agent_material/11_compact_hall_finite_heart_and_hn.tex:293`:
  correct finite-first object is the \(h_S\)-adic HN quotient system.

## Commands Run

```bash
pytest -q \
  compute/tests/test_hall_borcherds_gate.py \
  compute/tests/test_bps_positive_truncation.py::test_k3e_unquotiented_radical_certificate \
  compute/tests/test_bps_positive_truncation.py::test_full_hall_borcherds_radical_certificate_is_not_gram_only \
  compute/tests/test_bps_positive_truncation.py::test_derived_solution_stack_factors_are_zero_fibers \
  compute/tests/test_bps_positive_truncation.py::test_constructed_named_points_certificate_records_remaining_points \
  compute/tests/test_igusa_product_formula.py::test_borcherds_product_matches_delta5_in_absolute_value
```

Result:

```text
13 passed in 0.45s
```

```bash
python3 - <<'PY'
from fractions import Fraction
from compute.lib.bps_positive_truncation import (
    TruncationBound, constructed_named_points_certificate,
    derived_solution_stack_factors, full_hall_borcherds_radical_certificate,
    k3e_unquotiented_radical_certificate, radical_non_degeneracy_certificate,
    FiniteLinearMap,
)
from compute.lib.hall_borcherds_gate import (
    DELTA5_DATUM, HallBorcherdsWitnesses, evaluate_gate,
    k3xe_spectrum_tuple, primitive_root_key, additive_claim_status,
)

bound = TruncationBound(N=4, R_num=4)
full = full_hall_borcherds_radical_certificate()
legacy = k3e_unquotiented_radical_certificate()
k3e = {f.name: f for f in derived_solution_stack_factors(bound)}["k3e_raw_radical"]
print("DELTA5 kappa_BKM", DELTA5_DATUM.kappa_BKM)
print("DELTA5 square_weight", DELTA5_DATUM.square_weight)
print("K3xE spectrum", tuple(str(x) for x in k3xe_spectrum_tuple()))
print("full radical", full.exact, full.passed, full.checked_items, full.normalization)
print("legacy radical", legacy.exact, legacy.passed, legacy.normalization)
print("k3e solved/zero_fiber/computed/vanishes",
      k3e.solved, k3e.zero_fiber_defined,
      k3e.obstruction.computed, k3e.obstruction.vanishes)
print("k3e coordinates", k3e.obstruction.names)
print("open gate",
      evaluate_gate(HallBorcherdsWitnesses(denominator_normalization=True)).status,
      evaluate_gate(HallBorcherdsWitnesses(denominator_normalization=True)).missing_witnesses)
print("closed implication", evaluate_gate(HallBorcherdsWitnesses(
      oriented_critical_coha=True, hopf_pairing=True, drinfeld_double=True,
      denominator_normalization=True, root_multiplicity_map=True,
      k3xe_spectrum_separated=True, coha_positive_half_not_w=True,
      bkm_object_not_yangian=True)).closed)
print("primitive root key 1,1,1", primitive_root_key(1, 1, 1))
print("singular gram discrepancy",
      radical_non_degeneracy_certificate("toy",
      FiniteLinearMap(((Fraction(1), Fraction(1)), (Fraction(2), Fraction(2)))))
      .discrepancies)
print("unresolved factors",
      [d["factor"] for d in constructed_named_points_certificate(bound).discrepancies])
print("additive shortcut", additive_claim_status(
      kappa_ch_Heis=Fraction(3), kappa_fiber=Fraction(2),
      kappa_BKM=Fraction(5), universal_claim=True))
PY
```

Observed output:

```text
DELTA5 kappa_BKM 5
DELTA5 square_weight 10
K3xE spectrum ('0', '3', '5', '24')
full radical False True 8 pairing, orientation character, protected integration, bracket, Serre, Hopf pairing, and completion coordinates
legacy radical False True Igusa denominator fixes the quotient; finite Gram nondegeneracy is only the pairing coordinate
k3e solved/zero_fiber/computed/vanishes False True False False
k3e coordinates ('pairing_kernel', 'orientation_character', 'protected_integration', 'primitive_bracket', 'Serre_imaginary_relations', 'Hopf_pairing', 'completion_separatedness')
open gate OPEN_TYPED_GATE ('oriented_critical_coha', 'hopf_pairing', 'drinfeld_double', 'root_multiplicity_map', 'k3xe_spectrum_separated', 'coha_positive_half_not_w', 'bkm_object_not_yangian')
closed implication True
primitive root key 1,1,1 3
singular gram discrepancy ({'check': 'Rad_Aut=0', 'nullity': 1},)
unresolved factors ['quintic_excert', 'schoen_banana_gluing', 'k3e_raw_radical', 'theta_comparison', 'hcs_named_zero_fiber']
additive shortcut {'numeric_match': True, 'accepted_as_bridge_proof': False, 'universal_claim': True, 'reason': 'numeric coincidence only'}
```

## Files Changed

Only this assigned report was written:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave3_20260424/agent_03_k3e_radical_execution.md
```

No code, TeX, git state, or other note was edited.

## What Remains

The raw \(K3\times E\) point is the following exact construction problem.

1. Construct the compact oriented critical Hall atlas in a stability
   sector with support property, HN existence, compact-support
   vanishing-cycle correspondences, and finite \(h_S\)-adic quotient
   maps.
2. Compute \(o_{\mathrm{pair}}\): the automorphic pairing kernel in every
   finite quotient.
3. Compute \(o_{\mathrm{or}}\): prove the Hall orientation character is
   \(\nu_{\Delta_5}\) under transition.
4. Compute \(o_{\mathrm{int}}\): prove protected integration is a Hall
   character with coefficient oracle \(f(nm,l)\).
5. Compute \(o_{\mathrm{br}}\): identify the protected Hall primitive
   bracket with the Borcherds bracket.
6. Compute \(o_{\mathrm{Serre}}\): prove equality of Hall primitive
   relation ideal and Borcherds-Serre/imaginary relation ideal.
7. Compute \(o_{\mathrm{copair}}\) and \(o_{\mathrm{comp}}\): construct the
   negative half, Cartan completion, continuous Hopf pairing, closed
   transition ideals, Mittag-Leffler control, and separated completed
   radical.

These are not weaknesses of the quotient theorem. They are the exact
coordinates of the stronger raw Hall-BKM point.
