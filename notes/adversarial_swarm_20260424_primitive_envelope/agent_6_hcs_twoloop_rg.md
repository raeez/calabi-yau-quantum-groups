# 6d hCS Two-Loop RG Attack Report

## Attacked claim

Claim attacked: the universal primitive envelope for
`chapters/theory/cy3_chain_level_bridge.tex` has effectively resolved the
6d hCS two-loop counterterm gate by deriving the Yang-normalised
`CT_2` from the actual Costello-Gwilliam/Costello-Li factorisation-RG
or Feynman calculation.

Verdict: **not derived**. The algebraic Yang-normalised `CT_2` is proved
as a rational Yang-Baxter normal form. The actual 6d hCS
Feynman/RG local functional producing the same counterterm remains the
missing analytic primitive.

## Failure mode

The manuscript is mostly honest about the boundary:

- `chapters/theory/cy3_chain_level_bridge.tex:1536` states the two-loop
  result as algebraic YBE normal form and explicitly says the hCS RG
  derivation is not asserted.
- `chapters/theory/cy3_chain_level_bridge.tex:2062` defines the relevant
  complex as
  `Loc_hCS^(2) -> T_YBE^(hbar^5)`.
- `chapters/theory/cy3_chain_level_bridge.tex:2070` says the algebraic
  oracle identifies the target `CT_2`, but does not derive it from the
  6d hCS factorisation-RG integral.
- `chapters/theory/cy3_chain_level_bridge.tex:2075` names the missing
  obstruction class:
  `[rho_YBE(CT_2^{Feyn/RG}) - CT_2^{Yang}]`.
- `chapters/theory/cy3_chain_level_bridge.tex:2199` lists the
  6d hCS Feynman/RG derivation of `CT_2^{Yang}` as the remaining
  geometric/analytic realisation condition.

The executable surface agrees:

- `compute/lib/k3_hcs_6d_twoloop.py:28` says the constructed repair is
  a two-loop Yang-normalisation, not a first-principles hCS Feynman
  counterterm.
- `compute/lib/k3_hcs_6d_twoloop.py:531` says
  `twoloop_yang_normalization_condition` proves the group-algebra YBE
  normal form and deliberately does not claim the hCS RG calculation has
  produced it.
- `compute/lib/cy3_platonic_bridge.py:110` records the global witness
  requirement as exactly the `6d hCS factorisation-RG derivation of the
  algebraic Yang-normalised CT2`.
- `compute/lib/cy3_platonic_bridge.py:593` implements the two-loop
  witness by importing `twoloop_yang_normalization_condition`; it does
  not construct a local hCS functional.
- `compute/lib/cy3_platonic_bridge.py:828` returns no unconditional
  global theorem claims.

The dangerous stale surface is `compute/lib/k3_hcs_6d_twoloop.py:108`,
where the old docstring still has a section titled "Extraction of CT_2
from axiom" and displays a counterterm at lines 113-116. That prose is
not supported by the current executable proof and is contradicted by the
module's adversarial status and by `twoloop_yang_normalization_condition`.

## Exact algebraic facts preserved

For `sl_2`, with `c_v=2`, `dim_g=3`, `u=2.3`, `v=1.7`:

- One-loop coefficient: `a = 13`.
- Naive one-loop obstruction:
  `{'P12P23': '6500/1173', 'P23P12': '-6500/1173'}`.
- Legacy sunset after `CT_1` still has nonzero order-`hbar^5`
  obstruction:
  `{'P12P23': '-22209137500/210517137',
  'P23P12': '22209137500/210517137'}`.
- `A_2 = 506/3`.
- Yang-normalised slot-12 counterterm:
  `{'I': '-837430/729', 'P12': '226435/243'}`.
- Repaired algebraic obstruction is `{}`.

Thus the legacy sunset `hbar^5` repair is false and must remain false.
The algebraic Yang-normalisation repairs the YBE tangent only.

## Strict closure criterion

The missing primitive is an analytic/local-functional realisation of the
formal primitive `h_hCS_two_loop_counterterm_1`, with boundary
`rho_YBE(CT_2^{Feyn/RG}) - CT_2^{Yang}`.

To close the theorem, one must construct a genuine
`CT_2^{Feyn/RG} in Loc_hCS^(2)` from the two-loop Costello
homotopy-RG expansion:

```text
CT_2^{Feyn/RG}
= -Sing_{epsilon -> 0}
  [ W_2(P(epsilon,L), I_hCS)
    + W_1(P(epsilon,L), CT_1)
    + counterterm-insertion and BV-Laplacian subtraction terms
  ]_local,defect .
```

The derivation must include every two-loop local graph and subtraction
class relevant to the defect R-matrix: sunset, double-fish or iterated
fish, one-loop counterterm insertions, ghost/BRST terms, BV Laplacian
terms, heat-kernel subtraction terms, automorphism factors, and the
compact-support convention.

It must then prove:

1. `CT_2^{Feyn/RG}` is local, BRST/BV closed modulo exact terms, and
   compatible with factorisation products and RG scale homotopy.
2. The defect projection
   `rho_YBE: Loc_hCS^(2) -> T_YBE^(hbar^5)` is defined from the same
   renormalised factorisation product, not postulated from the R-matrix
   normal form.
3. After one-loop Yang normalisation,
   `rho_YBE(CT_2^{Feyn/RG}) = CT_2^{Yang}` modulo central scalar and
   BRST-exact terms.
4. The tangent coefficient is computed by the RG integral. If the
   current normalisation is retained, this means
   `b_RG = A_2 = (12 + h^vee/2)^2 - (h^vee)^2/12`; for `sl_2`,
   `b_RG = 506/3`. Since the algebraic YBE tangent also closes with
   `b=0`, YBE alone does not determine this coefficient.

## Recommended claim status

- `prop:k3-hcs-two-loop-yang-normalisation`: keep
  `ProvedHere` only for "algebraic YBE normal form; hCS RG derivation
  not asserted".
- `thm:cy3-universal-primitive-envelope`: keep
  `ProvedHere` only for formal obstruction resolution; analytic
  realisation remains the exact condition.
- Any sentence implying the actual 6d hCS Feynman/RG derivation of the
  Yang-normalised `CT_2` has already been done should be rejected or
  rewritten as the strict criterion above.
- The stale "Extraction of CT_2 from axiom" prose in
  `compute/lib/k3_hcs_6d_twoloop.py` should be treated as historical
  ansatz text, not theorem evidence.

## Tests and computations run

```bash
python3 -m pytest compute/tests/test_k3_hcs_6d_twoloop.py compute/tests/test_cy3_platonic_bridge.py -q
```

Result: `29 passed in 0.48s`.

Additional exact probe confirmed:

- `ybe_at_hbar5(..., hbar=1e-4)` reports
  `two_loop_verification_passed=False` and
  `residual_order_detected='hbar^3'`.
- `frontier_realisation_package().normal_form_status()['hCS_two_loop_counterterm']`
  is `proved_algebraic`.
- `remaining_analytic_global_obligations()['hCS_two_loop_counterterm']`
  is exactly
  `('6d hCS factorisation-RG derivation of the algebraic Yang-normalised CT2',)`.

## Files changed

- `notes/adversarial_swarm_20260424_primitive_envelope/agent_6_hcs_twoloop_rg.md`

## Remaining open questions

1. What is the full two-loop graph basis for the 6d hCS defect local
   functional on `K3 x E` after one-loop normalisation?
2. Does the RG integral produce the default tangent coefficient
   `b=A_2`, a different tangent coefficient, or only the non-tangent
   subtraction?
3. Are wheel-of-wheel/double-fish and `CT_1`-insertion terms exact,
   central, or part of the non-tangent cancellation?
4. Can the map `rho_YBE` be constructed directly from the renormalised
   factorisation product rather than imposed from the rational Yang
   R-matrix?
