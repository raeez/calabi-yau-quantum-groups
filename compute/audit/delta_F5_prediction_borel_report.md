# Prediction of delta_F_5^cross(W_3) and Borel Analysis

## Source data

The cross-channel correction to the multi-weight genus expansion
F_g(W_3) = kappa * lambda_g^FP + delta_F_g^cross has been computed
at g = 2, 3, 4 (thm:multi-weight-genus-expansion). All formulas below
are for the W_3 algebra with generators T (weight 2) and W (weight 3),
kappa(W_3) = 5c/6.

```
delta_F_2 = (c + 204) / (16 c)
delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
delta_F_4 = (287c^4 + 268881c^3 + 115455816c^2
             + 29725133760c + 5594347866240) / (17418240 c^3)
```

Source: `multi_weight_genus_tower.py`, `theorem_delta_f3_universal_engine.py`,
`delta_fg_degree_pattern_engine.py` (all in ~/chiral-bar-cobar/compute/lib/).

---

## 1. Denominator factorization

```
D_2 = 16         = 2^4
D_3 = 138240     = 2^10 * 3^3 * 5
D_4 = 17418240   = 2^11 * 3^5 * 5 * 7
```

Ratios:
```
D_3 / D_2 = 8640  = 2^6 * 3^3 * 5
D_4 / D_3 = 126   = 2 * 3^2 * 7
```

The ratio D_{g+1}/D_g decreases dramatically: 8640, 126, ...

Prime support: {2}, {2,3,5}, {2,3,5,7}. The primes appearing are
exactly the primes up to 2g-1 (primes up to 3, 5, 7 for g = 2, 3, 4).

Key observation: D_3 = denom(a_1) * denom(a_2) = 24 * 5760, where
a_1 = 1/24 and a_2 = 7/5760 are the A-hat genus coefficients. This
factorization into A-hat denominators is exact but does not extend
cleanly to g = 4 (D_4 / denom(a_3) = 17418240 / 967680 = 18, not a
single A-hat denominator).

Connection to (2g)!:
```
D_3 / 6! = 192 = 2^6 * 3
D_4 / 8! = 432 = 2^4 * 3^3
```

Both (2g)! | D_g for g = 3, 4. The quotients D_g/(2g)! grow with
ratio 432/192 = 9/4.

---

## 2. Structural prediction for delta_F_5

### 2.1 Numerator degree

| g | deg(P_g) | g-1 | net degree e_g | # terms | status |
|---|----------|-----|----------------|---------|--------|
| 2 | 1        | 1   | 0              | 2       | PROVED |
| 3 | 3        | 2   | 1              | 4       | PROVED |
| 4 | 4        | 3   | 1              | 5       | PROVED |
| 5 | **5**    | 4   | **1**          | **6**   | PREDICTED |

Pattern: deg(P_g) = g for g >= 3; the net degree e_g = 1 stabilizes.
The number of terms is g+1 for g >= 3. All coefficients are strictly
positive (verified at g = 2, 3, 4).

### 2.2 Denominator D_5

Prime support: {2, 3, 5, 7} (since 2*5-1 = 9 is not prime, no new
prime enters at g = 5).

Geometric extrapolation from D_g/(2g)!: if D_5/10! = 432 * (9/4) = 972,
then D_5 = 972 * 3628800 = 3,527,193,600 = 2^10 * 3^9 * 5^2 * 7.

This estimate is speculative (two-point geometric extrapolation). The
true D_5 will be determined by the lcm of automorphism group orders
of the stable graphs of M-bar_{5,0} contributing to the mixed-channel
graph sum.

### 2.3 Predicted form

```
delta_F_5 = (a_5 c^5 + a_4 c^4 + a_3 c^3 + a_2 c^2 + a_1 c + a_0)
            / (D_5 * c^4)
```

Properties:
- 6 terms in numerator, all positive (prediction, not proof)
- Pole of order 4 at c = 0
- Large-c: delta_F_5 ~ E_5 * c (linear in c)
- P_5(c) irreducible over Q (predicted from P_2, P_3, P_4 all irreducible)
- delta_F_5 > 0 for all c > 0

Confidence: HIGH for the structural pattern (degree, pole order,
positivity, linearity at large c). LOW for the specific value of D_5
(only two-point extrapolation).

---

## 3. Leading coefficient E_5 prediction

### 3.1 Large-c asymptotics

The leading coefficient E_g = lc(P_g)/D_g governs the large-c behavior:
```
E_2 = 1/16                    = 6.250e-02   (net degree 0: constant)
E_3 = 5/138240  = 1/27648     = 3.617e-05   (net degree 1: coefficient of c)
E_4 = 287/17418240 = 41/2488320 = 1.648e-05 (net degree 1: coefficient of c)
```

Simplified denominators:
```
denom(E_3) = 27648  = 2^10 * 3^3
denom(E_4) = 2488320 = 2^11 * 3^5 * 5   (numerator 41, prime)
```

The single available ratio:
```
E_4 / E_3 = 41/90 = 0.4556
```

Note: 41 is prime. 287 = 7 * 41 (the leading numerator coefficient of P_4).
Also 90 = 9 * 10 = (2*4+1)(2*4+2)/2. And 5040 = 7! = 7 * 8 * 9 * 10.

### 3.2 Borel growth models

The series delta_F_g at fixed c is NOT homogeneous in c (g=2 is O(1),
g >= 3 is O(c)). This c-inhomogeneity means Borel analysis must be
performed either at fixed c or on the separated O(c) tower for g >= 3.

For the O(c) tower, the ansatz E_g ~ C * beta^g * Gamma(2g + b) gives
a one-parameter family in b, with beta determined from the single ratio:

```
E_4/E_3 = beta * Gamma(8+b)/Gamma(6+b) = beta * (6+b)(7+b)
```

| b   | (6+b)(7+b) | beta        | A = 1/beta | A/A_scalar | E_5 prediction |
|-----|------------|-------------|------------|------------|----------------|
| -1  | 30         | 41/2700     | 65.9       | 1.67       | 1.401e-05      |
| 0   | 42         | 41/3780     | 92.2       | 2.34       | 1.300e-05      |
| 1   | 56         | 41/5040     | 122.9      | 3.11       | 1.206e-05      |
| 2   | 72         | 41/6480     | 158.0      | 4.00       | 1.126e-05      |

where A_scalar = (2pi)^2 = 39.48.

The (2g)! model (b = 1) gives A_cross = 5040/41 = 7!/41 exactly.

### 3.3 E_5 prediction range

```
E_5 in [1.13e-05, 1.40e-05]   (from b in [-1, 2])
Central estimate (b=0): E_5 ~ 1.30e-05
```

This corresponds to 1/E_5 in [71000, 89000], constraining the
denominator of the reduced fraction to this range.

---

## 4. Borel analysis: instanton action

### 4.1 Large-c instanton action

At large c, the (2g)! model (the most natural from Weil-Petersson
volume asymptotics at graph vertices) gives:

```
A_cross(c -> infinity) = 5040/41 = 7!/41 = 122.93
                       = 3.114 * (2pi)^2
                       = 3.114 * A_scalar
```

The cross-channel instanton action is approximately 3x the scalar
instanton action. This means:
- Cross-channel non-perturbative effects exp(-A_cross/hbar^2)
  are exponentially suppressed relative to scalar effects
  exp(-A_scalar/hbar^2).
- The Borel plane singularity from the cross-channel sector is
  FURTHER from the origin than the scalar A-hat poles at (2pi*n)^2.

### 4.2 c-dependent instanton action

At fixed c, the effective instanton action A(c) computed from the
ratio dF_4/dF_3 via the (2g)! model:

| c    | R(4/3)  | beta     | A(c)   | A(c)/A_scalar |
|------|---------|----------|--------|---------------|
| 4    | 51.14   | 0.913    | 1.10   | 0.028         |
| 10   | 20.46   | 0.365    | 2.74   | 0.069         |
| 26   | 7.89    | 0.141    | 7.10   | 0.180         |
| 50   | 4.13    | 0.074    | 13.56  | 0.344         |
| 100  | 2.12    | 0.038    | 26.40  | 0.669         |
| 200  | 1.17    | 0.021    | 48.02  | 1.216         |
| 500  | 0.68    | 0.012    | 82.71  | 2.095         |
| 1000 | 0.55    | 0.010    | 101.43 | 2.569         |

Asymptotics:
- Large c: A(c) -> 5040/41 ~ 122.9.
- Small c: A(c) ~ 0.274 * c -> 0. The instanton action VANISHES
  at c = 0, consistent with the c^{-(g-1)} pole driving a more
  violent divergence at small c.

The crossover A(c) = A_scalar occurs near c ~ 180. For c > 180,
the cross-channel Borel singularity is further from the origin than
the scalar singularity. For c < 180, it is closer.

### 4.3 Can A_cross be computed from 3 data points?

Not uniquely from the leading coefficients alone. The ansatz
E_g ~ C * beta^g * Gamma(2g+b) has three parameters (C, beta, b),
requiring three data points (E_3, E_4, E_5). With only E_3 and E_4,
the Gevrey shift parameter b is undetermined, giving a one-parameter
family of models with A_cross in [66, 158].

The genus-5 computation delta_F_5^cross(W_3) is the critical
bottleneck: it would pin down b, hence beta, hence A_cross exactly
(within this ansatz). It would also test whether the factorial
growth is (2g)!, (2g-2)!, or intermediate.

---

## 5. Ratio to scalar part

The ratio delta_F_g / (kappa * lambda_g) at large c:

| g | ratio            | numerical |
|---|------------------|-----------|
| 2 | 18/c -> 0        | subdominant |
| 3 | 42/31            | 1.355     |
| 4 | 9184/381         | 24.10     |
| 5 | **predicted > 24** | super-linear growth continues |

The cross-channel correction dominates the scalar part for g >= 4
at large c. The ratio grows super-linearly, consistent with factorial
growth of the cross-channel tower versus the convergent (Gevrey-0)
scalar tower.

---

## 6. Summary of predictions for delta_F_5

| Property | Prediction | Confidence |
|----------|-----------|------------|
| deg(P_5) | 5 | HIGH |
| # terms | 6 (all positive) | HIGH |
| Net degree | 1 (linear in c) | HIGH |
| Pole order at c=0 | 4 | HIGH (= g-1) |
| P_5 irreducible over Q | yes | MEDIUM |
| D_5 prime support | {2, 3, 5, 7} | MEDIUM |
| D_5 value | ~ 3.5 * 10^9 | LOW (two-point extrap.) |
| E_5 = lc(P_5)/D_5 | [1.1e-5, 1.4e-5] | MEDIUM (one-param family) |
| A_cross (large c) | [66, 158] | MEDIUM (needs g=5 for b) |
| A_cross (large c, (2g)! model) | 5040/41 = 122.9 | CONDITIONAL on (2g)! |
| delta_F_5/F_5^scalar (large c) | >> 24 | HIGH |

---

## 7. What delta_F_5 would resolve

1. PIN DOWN THE GEVREY INDEX: three E_g values (g=3,4,5)
   uniquely determine (C, beta, b) in E_g ~ C * beta^g * Gamma(2g+b).
   This gives A_cross exactly within the factorial growth ansatz.

2. DISTINGUISH (2g)! FROM (2g-2)!: the predicted E_5 differs by
   a factor of 1.16 between the two models (1.21e-5 vs 1.40e-5).
   This is within computational reach if the genus-5 graph sum
   can be evaluated.

3. TEST THE DENOMINATOR PATTERN: D_5 determines whether the
   primes-up-to-2g-1 pattern and the D_g/(2g)! geometric growth
   persist.

4. CONSTRAIN THE BOREL PLANE: with 3 data points, a [2/1] Pade
   approximant of B_cross(t) in the variable u = t^2 becomes
   available, giving a sharper estimate of the singularity location.

---

## 8. Status

- delta_F_2, delta_F_3, delta_F_4: PROVED (ProvedHere), multi-path verified
- Structural pattern (degree, positivity, net degree): PROVED at g=2,3,4
- Structural prediction for g=5: PREDICTED (high confidence)
- E_5 range: ESTIMATED [1.1e-5, 1.4e-5] (medium confidence)
- A_cross at large c: ESTIMATED [66, 158] (medium, needs g=5)
- Specific (2g)! model A_cross = 7!/41: CONDITIONAL on growth type
- c-dependent A(c): COMPUTED from g=3->4 ratio (single-ratio estimate)
- Crossover c ~ 180 where A_cross = A_scalar: ESTIMATED

## References

- `delta_fg_degree_pattern_engine.py` (~/chiral-bar-cobar/compute/lib/)
- `theorem_multiweight_generating_function_engine.py` (~/chiral-bar-cobar/compute/lib/)
- `theorem_w3_stokes_resurgence_engine.py` (~/chiral-bar-cobar/compute/lib/)
- `resurgence_cross_channel_report.md` (~/chiral-bar-cobar/compute/audit/)
- `delta_F_cross_generating_function_report.md` (~/chiral-bar-cobar/compute/audit/)
- thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
- prop:cross-channel-growth (higher_genus_modular_koszul.tex)
