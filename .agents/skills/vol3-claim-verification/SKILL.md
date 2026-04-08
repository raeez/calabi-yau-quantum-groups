---
name: vol3-claim-verification
description: Use when verifying a formula, invariant, example, theorem statement, literature comparison, or compute-backed claim in the Calabi-Yau Quantum Groups repository, especially when multi-path verification, source normalization, or Vol I/II/III convention conversion matters.
---

# Vol III Claim Verification

Read `AGENTS.md` first.

## Required workflow

1. State the exact claim and the exact object.
2. State the convention and parameter regime.
3. Verify by at least three genuinely independent paths when the claim is numerical or computational.
4. Record source and normalization for any literature constant.
5. If the claim crosses volumes, convert conventions explicitly before comparing.

## Mandatory Vol III checks

- `AP-CY1`: CY dimension versus complex dimension
- `AP-CY2`: negative cyclic refinement of the CY trace
- `AP-CY5`: root-of-unity versus generic `q`
- `AP-CY6`: CY3 chiral algebra existence
- `AP-CY7`: CoHA versus `E_1`-chiral conflation
- `AP-CY8`: denominator identity versus bar Euler product
- `AP49`: OPE, lambda-bracket, and motivic/categorical convention conversion

## Compute discipline

- If the formula enters the manuscript and is computationally meaningful, look for or add a corresponding compute/test witness.
- Tests that merely restate the same derivation are not enough.
