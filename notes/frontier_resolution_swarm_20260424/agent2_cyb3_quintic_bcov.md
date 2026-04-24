# Agent 2 report: CY-B3 tier III and quintic BCOV obstruction

Date: 2026-04-24.

## Verdict

No chain-level orthogonal/Hilbert Shimura pairing was found for the
non-K3-fibred CY-B3 tier-III case. I did not promote the tier-III claim.
The manuscript now records the exact missing datum: a chain map/pairing
from
`B^{E_1}(Phi_3^{(Sigma_2,C)}(Perf X))`
to chains on the orthogonal Shimura target
`SO(2,2h11)/(SO(2)SO(2h11))/Gamma`, with lattice, arithmetic group,
automorphic line, and Verdier/Koszul compatibility fixed.

For the quintic, the leading LCS BCOV sign check works:

```text
kappa_BCOV(Q) = -25/3
S4_1^inst(Q) = 2875 / (-25/3) = -345
kappa_BCOV(Q)^3 * S4_1^inst(Q) > 0
```

This is not a vanishing proof for `O_3^{BL}`. The missing lemma is the
full BCOV Borel sign/nuclear-convergence statement for the entire sewing
defect, not just the first coefficient.

## Anchors Changed

- `chapters/connections/bar_cobar_bridge.tex`
  - `prop:cy-b3-tieriii-quintic-bl-obstruction`
  - Pins the tier-III orthogonal/Hilbert pairing datum and the residual
    quintic complexes
    `O_1^{BL} in H^1(Ran(C), Aut_tensor(Gen_BL)) ~= lim^1_n I_n`
    and
    `O_3^{BL} in lim^1_g A^{sew,g}`.
- `chapters/examples/cy_d_kappa_stratification.tex`
  - Adds the guardrail that BCOV class-M promotion is not a chiral
    Booth--Lazarev vanishing theorem.
- `compute/tests/test_quintic_shadow_tower.py`
  - Adds tests for the leading LCS Borel sign and for the absence of a
    full strict/framing/BKM witness.

## Obstruction Theorem Proposal

For compact non-K3-fibred CY3 with `h11 >= 3`, CY-B3 tier III remains
conditional until one constructs the orthogonal/Hilbert pairing

```text
< -, - >_X^orth:
  B^{E_1}(Phi_3^{(Sigma_2,C)}(Perf X))
  tensor C_*(D_X, L_X^{w_X})
  -> C
```

as a chain map compatible with sewing and Verdier/Koszul reflection.
BCOV/GW/PT coefficients on the Kahler lattice are evidence, not a
replacement for this map.

For the quintic, the residual BL representatives are pinned as:

```text
O_1^{BL}: Smith-recognition Cech class
  [j^*_{n,m} I_{n+m} - I_n box I_m] in lim^1_n I_n.

O_3^{BL}: sewing Mittag-Leffler defect
  [sigma_sew] in lim^1_g A^{sew,g}.
```

Vanishing requires actual nullhomotopies in these complexes.

## Tests Run

```bash
python3 -m pytest \
  compute/tests/test_quintic_shadow_tower.py \
  compute/tests/test_quintic_shadow_obstruction.py \
  compute/tests/test_cy_b_d3_proof.py \
  compute/tests/test_cy_b_toward_proof.py
```

Result: `421 passed in 2.39s`.

Also ran:

```bash
git diff --check -- \
  chapters/connections/bar_cobar_bridge.tex \
  chapters/examples/cy_d_kappa_stratification.tex \
  compute/tests/test_quintic_shadow_tower.py \
  notes/frontier_resolution_swarm_20260424/agent2_cyb3_quintic_bcov.md
```

Result: no whitespace errors.

## Remaining Open Questions

1. Construct or falsify the tier-III orthogonal/Hilbert pairing for a
   concrete non-K3-fibred `h11 >= 3` compact CY3.
2. Produce a Cech `0`-cochain killing the Ran-space Smith cocycle for
   `O_1^{BL}`, or prove no such cochain exists on the chosen curve.
3. Prove the full BCOV Borel sign lemma for the quintic sewing defect:
   analyticity of the Borel transform on the positive ray plus nuclear
   convergence of `sigma_sew^{(N)}`.
4. Reconcile the older residual notes that use `kappa_ch(Q)=1`; the
   live scoped files now keep the Hodge supertrace `0` separate from the
   BCOV shadow scalar `-25/3`.
