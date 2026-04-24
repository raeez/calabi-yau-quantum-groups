# Two-loop hCS counterterm: Feynman/RG obstruction note

Date: 2026-04-24.

Owned scope: `compute/lib/k3_hcs_6d_twoloop.py`,
`compute/tests/test_k3_hcs_6d_twoloop.py`.

## Claim attacked

For 6d hCS on `K3 x E` with a surface defect, the remaining primitive was:
derive the two-loop hbar^4 counterterm from the Feynman/RG local graph
calculus and match the Yang-normalised counterterm produced by the exact
algebraic YBE oracle.

Conventions:

- `a = chi(K3)/2 + c_v/2 = 12 + c_v/2`.
- `A2 = a^2 - c_v^2/12`.
- Rational Yang normal form after the one-loop repair:
  `R(u; h_eff) = I + h_eff (P-I)/u`.
- Test normalisation: `sl_2`, `c_v = 2`, `dim_g = 3`,
  `(u, v) = (23/10, 17/10)`, hence `A2 = 506/3`.

## Result

The present executable witness obstructs the full Feynman/RG derivation.

The exact algebraic oracle gives the hbar^4 Yang-normalised family

```text
CT_2,ij = b (P_ij - I) / u_ij - Q_2,ij^legacy.
```

A local two-loop sunset/RG subtraction has the pole order of the two-loop
graph it subtracts. In this model it lies in the span of `I/u_ij^4` and
`P_ij/u_ij^4`. It can therefore recover the singular projection
`-Q_2^legacy`, but it does not fix the simple-pole tangent term
`b(P_ij-I)/u_ij`.

At the `sl_2` test point, the local Feynman/RG subtraction in slot `12` is

```text
I   : -632500/729
P12 :  158125/243
```

The default algebraic Yang-normalised counterterm with `b = A2 = 506/3`
is

```text
I   : -837430/729
P12 :  226435/243
```

The missing piece is exactly the finite tangent renormalisation

```text
b(P12-I)/(u-v),  b = 506/3:
I   : -2530/9
P12 :  2530/9
```

Thus the Feynman/RG local graph data matches the `b = 0` member of the
Yang-normalised family. It does not derive the default `b = A2` member
without an additional finite scheme condition or Ward identity.

## Executable anchors

- `twoloop_yang_normalization_condition`: exact group-algebra YBE oracle.
- `feynman_rg_locality_obstruction_exact`: no-go witness comparing the
  local pole-four Feynman/RG subtraction against the Yang-normalised
  counterterm family.
- `test_feynman_rg_locality_obstructs_default_yang_counterterm_derivation`:
  verifies the exact fractions above.
- `test_zero_tangent_yang_oracle_is_the_local_feynman_rg_case`: verifies
  that `b = 0` is precisely the local Feynman/RG case.

## Remaining primitive obligation

To turn the obstruction into a derivation, one must supply a genuine 6d
hCS finite-renormalisation principle fixing `b`. Acceptable inputs would be
one of:

- a Costello factorisation/RG Ward identity forcing the tangent
  `b(P-I)/u`;
- a defect-level BRST cohomology computation showing that the simple-pole
  tangent representative is cohomologous to the local sunset subtraction
  after descent;
- a scheme-normalisation condition tied to the algebraic Yang coupling,
  proved independently of the YBE oracle.

Until one of these is supplied, the theorem-grade statement is negative:
the local Feynman/RG route reaches the pole-four subtraction and stops
short of the default Yang-normalised counterterm.
