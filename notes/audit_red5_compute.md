# RED5 Compute Module Audit

Adversarial audit of `compute/lib/` modules and their tests. Focus: cross-module
consistency, wrong values, silent failures, tautological tests.

Date: 2026-04-02

---

## FINDING 1 (CRITICAL): bkm_shadow_tower.py hardcoded phi_{0,1} table is WRONG

**Severity: HIGH. The entire shadow tower quantitative computation uses wrong data.**

The function `phi01_coefficients()` in `bkm_shadow_tower.py` returns a hardcoded
table that is NOT the Fourier coefficients of the weak Jacobi form phi_{0,1}.

Evidence:

| (n, l) | phi01_fourier (exact) | bkm_shadow_tower | wkb_denominator |
|--------|----------------------|------------------|-----------------|
| (0, 0) | 10                   | 20               | 10              |
| (0, 1) | 1                    | 2                | 1               |
| (1, 0) | 108                  | -252             | 108             |
| (1, 1) | -64                  | -128             | -64             |
| (1, 2) | 10                   | -2               | 10              |
| (2, 0) | 808                  | 4096             | 808             |

The n=0 row is 2x the correct value (DVV vs Eichler-Zagier normalization), but
for n >= 1, the values are COMPLETELY DIFFERENT -- not a constant multiple.

**Proof the bkm table is wrong**: phi_{0,1} coefficients f(n,l) depend only on
the discriminant D = 4n - l^2 (fundamental property of weak Jacobi forms).
The bkm table VIOLATES this:
- D=0: f(0,0)=20 but f(1,2)=-2 (should be equal)
- D=3: f(1,1)=-128 but f(3,3)=-252 (should be equal)
- D=4: f(1,0)=-252 but f(2,2)=216 (should be equal)

**Row sum test**: phi_{0,1}(tau, 0) = const, so sum_l f(n,l) = 0 for n >= 1.
The bkm table gives row sums: n=0: 24, n=1: -512, n=2: 10608, n=3: -162986.
Nonzero row sums for n >= 1 are IMPOSSIBLE for phi_{0,1}.

**What the bkm table actually contains**: Unknown. Possibly garbled Delta_5
Fourier-Jacobi coefficients mixed with phi_{0,1} values. The n=0 row matches
2 * phi_{0,1}^{EZ} (the K3 elliptic genus at the chi=24 normalization).

**Impact on the shadow tower**:
- `root_multiplicity(n, l, m)` returns `get_f(n*m, l)` using the wrong table
- All shadow tower projections (arity 2/3/4) use wrong root multiplicities
- `denominator_product_numerical` and `denominator_product_truncated` give wrong results
- The QUALITATIVE structure (real vs imaginary classification) is unaffected
  since it depends only on 4nm - l^2, not on the actual coefficient values

**Why tests pass**: Tests only compare bkm internal data to itself. No cross-validation
against phi01_fourier.py, wkb_denominator.py, or igusa_product_formula.py.

**Fix**: Replace `phi01_coefficients()` with exact values from `phi01_fourier.py`,
or import from that module. Choose one normalization (EZ with phi(tau,0)=12 is standard).

---

## FINDING 2 (MODERATE): wkb_denominator.py has wrong hardcoded values at n=6

**Severity: MODERATE. Affects high-order product formula terms.**

The `PHI01_TABLE` in `wkb_denominator.py` has incorrect entries at n=6:

| (n, l) | Exact (phi01_fourier) | wkb_denominator | Error |
|--------|----------------------|-----------------|-------|
| (6, -1) | -141826 | -141824 | off by 2 |
| (6, 0)  | 188304  | 186186  | off by 2118 |
| (6, 1)  | -141826 | -141824 | off by 2 |

Equivalently, at discriminant level:
- c(D=23): exact = -141826, wkb = -141824
- c(D=24): exact = 188304, wkb = 186186

**Proof**: The exact row sum for n=6 is 0 (as required by phi_{0,1}(tau,0) = const).
The wkb row sum for n=6 is -2114. The phi01_fourier.py computation uses exact
rational arithmetic (Fraction type) and satisfies the row sum constraint.

**Also**: `igusa_product_formula.py` numerical computation (via mpmath DFT) gives
f(5,0) = 58641 (should be 58640, off by 1) and f(6,0) = -98445 (completely wrong,
should be 188304). The numerical extraction loses precision at higher orders.

**Impact**: Product formula verification at moderate Im(Z) points may have slightly
degraded accuracy. The exponential suppression factor exp(-12*pi*Im(tau)) for n=6
terms means the error is ~1e-16 at the deep cusp test point (Im(tau)=2), so
existing tests still pass. But the hardcoded table is nonetheless wrong.

**Why tests miss this**: Cross-validation in `test_wkb_denominator.py` only checks
through n=4. The `verify_phi01_sum_rule` only checks n=0.

**Fix**: Replace PHI01_TABLE entries at n=6 with exact values. Better: generate
the table from phi01_fourier.py at import time (or cache the result).

---

## FINDING 3 (MODERATE): BKM identity in phi01_fourier.py is FALSE as stated

**Severity: MODERATE. The identity claim is wrong; the test documents the failure
as expected behavior.**

The function `verify_bkm_identity()` in `phi01_fourier.py` claims to verify:

    1 + (1/64) * sum_{t >= 0} f(1+2t, 1) * q^t = prod_{k >= 1} (1-q^k)^9

where f(n, l) are Fourier coefficients of phi_{0,1}. This identity is FALSE.
`verify_bkm_identity(20)` returns `False`.

At q^0: LHS = 1 + f(1,1)/64 = 1 + (-64)/64 = 0. RHS = 1. Already fails.

The test `test_bkm_identity_q0` in `test_phi01.py` documents this:
```python
lhs_q0 = 1 + f11 / 64
assert lhs_q0 == 0  # documents the actual value
```
This is a TEST THAT PASSES FOR THE WRONG REASON: it asserts the LHS is 0
(documenting the failure) without flagging that the identity itself is false.

**The correct identity**: The eta^9 identity involves Fourier-Jacobi coefficients
of Delta_5, NOT phi_{0,1}. The `igusa_product_formula.py` module correctly tests
the numerical version by extracting the (l=1, m=1) sector of Delta_5 via genus-2
theta constants and comparing with eta^9. That test PASSES.

**Fix**: Either remove `verify_bkm_identity` (since it tests a false statement) or
correct the docstring to explain that the identity requires Delta_5 coefficients.
Fix the test to not silently document a mathematical failure as expected behavior.

---

## FINDING 4 (LOW): Shadow tower truncation test is TAUTOLOGICAL

**Severity: LOW. Tests provide false confidence.**

`verify_truncation_agreement()` in `bkm_shadow_tower.py` compares:
1. `product_log_coefficient(r, max_coord, data)` -- the truncated product at order r
2. `shadow_tower_projection(r, max_coord, data)['log_coefficients']` -- which
   ALSO calls `product_log_coefficient(r, max_coord, data)`

Since both sides call the same function with the same arguments, the test is
comparing A == A. It ALWAYS passes regardless of whether the mathematical content
is correct. All four truncation agreement tests (order 2-5) are vacuous.

**Fix**: The shadow tower projection should be computed independently -- either
analytically from the Weyl orbit sum structure, or by constructing the tower from
a different mathematical characterization (e.g., the recursive structure of the
correction terms S_im from the Borcherds denominator formula).

---

## FINDING 5 (INFORMATIONAL): Igusa product formula sign is -1 (not a bug)

The ratio (1/64)*Delta_5(Z) / Borcherds_product(Z) = -1 (not +1) at all test
points, verified to 13+ digit precision. This is correctly documented in the
module docstring as arising from the branch of log for the (n=0, l=-1, m=0)
factor in the Borcherds product. The test `test_product_consistent_sign` explicitly
verifies `abs(ratio + 1) < 1e-8`.

This is NOT a bug. The sign comes from the GKM superalgebra structure and is a
well-known feature of Borcherds products for superalgebras. The previous C5 agent
report was correct to identify the sign but incorrect to call it an error.

---

## FINDING 6 (INFORMATIONAL): cy_euler kappa = h^{1,1}(K3)/4 = 5

The claim kappa(A_{K3 x E}) = 5 = h^{1,1}(K3)/4 is algebraically correct.
The chain of reasoning:
1. Borcherds product weight formula: weight = c_f(0)/2
2. c_f(0) = f(0,0) = 10 [in EZ normalization] = h^{1,1}(K3)/2 = 20/2
3. weight = 10/2 = 5
4. kappa = weight = h^{1,1}/4 = 20/4 = 5

The code tests a THEOREM (the Borcherds weight formula), not just an empirical
observation. The proof that c_f(0) = h^{1,1}/2 comes from the identification
f(0,0) with the number of K3 Ramond-Ramond ground states at (h,l) = (0,0),
which equals h^{1,1}(K3)/2 by the decomposition of the Witten index.

The code in `decompose_weight_5()` contains extensive commentary exploring
multiple decomposition routes. The final answer kappa = (chi(K3) - 4)/4 is
equivalent and illuminating.

---

## FINDING 7: Cross-module consistency summary

| Module | Convention | f(0,0) | f(0,1) | f(1,0) | Row sums | Status |
|--------|-----------|--------|--------|--------|----------|--------|
| phi01_fourier.py | EZ | 10 | 1 | 108 | 12,0,0,... | CORRECT (exact) |
| igusa_product_formula.py | EZ | 10 | 1 | 108 | 12,0,0,... | CORRECT (numerical, precision loss at n>=5) |
| wkb_denominator.py | EZ | 10 | 1 | 108 | 12,0,...,-2114(n=6) | MOSTLY CORRECT (2 wrong entries at n=6) |
| dd_modular_lattices.py | N/A | N/A | N/A | N/A | N/A | CORRECT (lattice only) |
| bkm_shadow_tower.py | WRONG | 20 | 2 | -252 | 24,-512,10608,... | WRONG TABLE |

The lattice structures in dd_modular_lattices.py and wkb_denominator.py are
fully consistent: same Gram matrices, same Weyl vector, same simple roots,
same signatures, same embedding maps. This was verified by the existing
cross-validation tests in test_wkb_denominator.py (TestCrossValidationDD).

---

## Recommendations (priority-ordered)

1. **FIX bkm_shadow_tower.py**: Replace the hardcoded `phi01_coefficients()` with
   values imported from (or cross-checked against) `phi01_fourier.py`. This is
   the most impactful bug.

2. **FIX wkb_denominator.py**: Correct the three wrong entries in `PHI01_TABLE`
   at n=6: f(6,0) = 188304, f(6,+/-1) = -141826.

3. **FIX phi01_fourier.py**: Either delete `verify_bkm_identity()` or correct
   its docstring to explain that the identity requires Delta_5 Fourier-Jacobi
   coefficients, not phi_{0,1} coefficients.

4. **FIX test_phi01.py**: The `test_bkm_identity_q0` test should either be
   removed or rewritten to clearly state that the identity is false and why.

5. **ADD cross-validation tests**: Add tests in `test_bkm_shadow.py` that compare
   `bkm.get_f(n, l)` against `phi01_fourier.phi01_coefficient(n, l)` for n <= 5.

6. **ADD row sum tests**: Add `sum_l f(n, l) = 0` tests for n up to at least 6
   in all modules with hardcoded tables.

7. **REPLACE tautological test**: Rewrite `verify_truncation_agreement()` to
   compare against an independently computed quantity.

---

## FINDING 8 (INFORMATIONAL): Complexity function is well-defined but not unique

The complexity function `root_complexity(n, l, m)` assigns:
- complexity = 2 for all real roots (regardless of coordinates)
- complexity = 2 + (n + m) for imaginary roots

This is well-defined as a function on positive roots since the coordinates (n,l,m)
in the basis (f_2, f_3, f_{-2}) uniquely determine the root. Real roots at
arbitrary coordinates (e.g., (2,3,1) with n+m=3) all get complexity 2, which means
the arity-2 layer includes the ENTIRE Weyl orbit of the simple roots.

However, the choice of n+m as the grading for imaginary roots is not mathematically
unique. One could equally use root height, norm, or other filtrations. The paper
should state this as a physical motivation (BPS/D-brane charge) rather than implying
it is "the" natural filtration.

---

## FINDING 9 (INFORMATIONAL): Positive root ordering conventions differ

- `igusa_product_formula.py`: For n=m=0, takes l < 0 (Gritsenko-Nikulin convention)
- `wkb_denominator.py` and `bkm_shadow_tower.py`: For n=m=0, takes l > 0

Both produce the same product formula value since f(0,l) = f(0,-l) and the Weyl
vector prefactor compensates for the sign difference. Not a bug.

---

## Test run summary (all existing suites)

| Test file | Results |
|-----------|---------|
| test_phi01.py | 51/51 pass |
| test_bkm_shadow.py | 67/67 pass |
| test_dd_lattices.py | 65/65 pass |
| test_wkb_denominator.py | 86/86 pass |
| test_igusa_product.py | 22/22 pass |
| test_cy_euler.py | 85/85 pass |

All 376 tests pass. The critical issues (Findings 1-3) are not caught because:
- bkm_shadow tests only compare internal data to itself
- wkb_denominator cross-validation stops at n=4
- phi01_fourier BKM identity test documents failure as expected behavior
