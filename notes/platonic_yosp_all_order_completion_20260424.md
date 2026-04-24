# Platonic yosp All-Order Completion Attack, 2026-04-24

## Claim Attacked

The finite orthogonal/Hodge-parity boundary and the small-rank
super-RTT computations do not prove the completed Hall--Drinfeld
Super-Yangian
\[
  Y_\hbar^{\mathrm{super}}(\mathfrak g_{\Delta_5})
  \simeq D^\wedge_\hbar(\mathrm{CoHA}_{K3\times E}).
\]

The eight-condition criterion in
`chapters/examples/k3_chiral_bialgebra_platonic.tex` separates the
formal current algebra from the completed quasi-Hopf object. This note
attacks the six primitives that remain after the finite current and
reflection-equation boundary is isolated.

## Failure Mode

Finite-dimensional evidence proves only a boundary:

- \(\mathfrak{gl}(4\mid20)\): ambient RTT warm-up, dimension \(576\).
- Kac \(\mathfrak{osp}(4\mid20)\): comparison series, dimension \(296\).
- Hodge-parity \(\mathfrak{so}(4\mid20)\): finite theta-fixed envelope,
  dimension \(276\).
- Small-rank \(Y(\mathfrak{gl}(m\mid n))\) checks: graded signs,
  Yang--Baxter, unitarity, crossing.

None of these supplies the completed Hall primitive comparison, PBW
flatness after completion, continuous Hopf operations, universal
\(R\)-matrix convergence, all-order associator topology, denominator
central character, or the \(\zeta_8\) divided-power integral form.

## Executable Oracle

`compute/lib/k3_super_yangian.py` now contains
`super_yangian_completion_obstruction_oracle()`. It records six
obligations as unproved:

1. `completed_pbw_flatness`;
2. `coproduct_antipode_continuity`;
3. `universal_R_convergence`;
4. `all_order_associator_topology`;
5. `reflection_centre_delta5_match`;
6. `zeta8_divided_power_integral_form`.

The oracle is intentionally negative. It also records the positive
finite evidence so that tests can distinguish useful boundary checks
from the completed object.

## Tests Added

`compute/tests/test_k3_super_yangian.py` now enforces:

- exact six-primitive tracking after the criterion;
- every primitive remains unproved and non-all-order;
- dimension evidence \(576,296,276\) does not imply completion;
- PBW spanning is not PBW flatness;
- small-rank RTT coproduct intuition is not continuous completed Hopf
  structure;
- finite Yang--Baxter checks do not prove universal \(R\)-matrix
  convergence;
- an \(\hbar^3\) associator check is not all-order topology;
- the finite central series is not yet the \(\Delta_5\) denominator;
- \(8^{129}\) is only the real-root positive-Borel/projective-index
  count at \(\zeta_8\), not a full Hopf dimension.

## Verification

Command:

```bash
pytest compute/tests/test_k3_super_yangian.py
```

Result:

```text
73 passed in 0.74s
```

## Remaining Primitive Obligations

- Prove completed PBW flatness:
  \(\operatorname{gr}Y_\hbar^{\mathrm{super}}
  \cong U(\mathfrak g_{\Delta_5}[u])^\wedge\).
- Construct continuous coproduct and antipode compatible with the Hall
  pairing.
- Prove convergence of
  \(R^{\mathrm{rat}}_{\mathrm{Yang}}(u)\theta^{K3}(u,Z)\) in the joint
  \(\hbar\)-adic and positive-root-height topology.
- Lift the Siegel--Borcherds associator from the displayed
  \(\hbar^3\) check to an all-order completed associator.
- Match the reflection-equation centre with the Gritsenko--Borcherds
  denominator \(\Delta_5\).
- Construct the \(\zeta_8\) divided-power integral form for the same
  completed object, stable under coproduct, antipode, and \(R\).
