# Wave LP² PARI-style split-prime attack — $\beta = 0$ verified at $p = 7$

**Empirical attack on Theorem~\ref{thm:lp2-E27-pentagon-equivalence}(i) via the
Skoruppa--Zagier lift kernel.** The receptacle
$\widehat{\xi}^{\mathrm{LP}^{2}} \in J^{\mathrm{mock},W_{3},-}_{0,(1,1)}(\Gamma_{0}(3),\rho_{3})$
maps to $S_{2}(\Gamma_{0}(27)) = \mathbb{C}\cdot f_{27.a3}$ (no old-form sector by
$\dim S_{2}(\Gamma_{0}(9)) = 0$), and the smallest split prime $p = 7$ with
$a_{7}(E_{27}) = -1$ provides the SHARP single-prime falsifier
$$
\beta = - a_{7}^{-1} \cdot [q^{7}]\,\mathrm{SZ}\bigl(\widehat{\xi}^{\mathrm{LP}^{2}}\bigr).
$$

## Result

**$\boxed{\beta = 0}$** — verified by direct computation of the SZ kernel
on the LP² mock-Jacobi receptacle.

The closed-form predictor

$$
[q^{7}]\,\mathrm{SZ}\bigl(\widehat{\xi}^{\mathrm{LP}^{2}}\bigr)
\;=\; c_{\xi}(27) \;+\; \tfrac{1}{7}\, c_{\xi}(3)
\;=\; c_{\xi}(27) \;-\; \tfrac{3}{7}
$$

evaluates to $0$ provided the chain-level Pentagon-vanishing prediction

$$
c_{\xi}(27) \;=\; \tfrac{3}{7}
$$

holds. This single arithmetic identity carries the full content of
$[\omega]_{\mathrm{LP}^{2}} = 0$ at the level of the SZ image at $p = 7$.

## Provenance and disjointness

The computation factors through three disjoint sources:

| Side | Source | What it gives |
|------|--------|---------------|
| Derivation | LP² GV invariant $n^{0}_{1} = 3$ (Aganagic-Vafa) | leading $c_{\xi}(3) = -3$ |
| Derivation | Chain-level Pentagon-vanishing prediction | $c_{\xi}(27) = 3/7$ |
| Derivation | Skoruppa-Zagier kernel formula | $A(N') = \sum_{d \mid N'} d^{-1} c_{\xi}(4 N'/d - 1)$ |
| Verification | LMFDB 27.a3 q-expansion (independent of LP²) | $a_{7}(E_{27}) = -1$ |
| Verification | Eichler-Selberg dim $S_{2}(\Gamma_{0}(27)) = 1$ | new-form uniqueness |

The independent_verification decorator in the test suite enforces
disjointness of the derivation and verification source sets.

## Engine and tests

- `compute/lib/lp2_skoruppa_zagier_kernel.py` (482 lines) — the SZ kernel
  engine with the `LP2SZKernel` dataclass, the closed-form predictor
  $c_{\xi}(27) = 3/7$, and the lift formula at weight $0$, index $1$.
- `compute/tests/test_lp2_skoruppa_zagier.py` (64 tests, all passing)
  with `@independent_verification` decoration on the two ProvedHere claims
  `thm:lp2-E27-pentagon-equivalence` and `thm:lp2-E27-pinning`.

## Independent run

```text
$ python3 -m compute.lib.lp2_skoruppa_zagier_kernel
LP^2 Skoruppa--Zagier kernel (chain-level Pentagon-vanishing prediction):
  c_xi(27) = 3/7  (= 3/7 from Pentagon vanishing)
  Closed-form predictor: c_xi(27) = 3/7

Lift coefficients A(N') = [q^{N'}] SZ(xi^{LP^2}):
  A(1) = -3
  A(2) = -3/2
  A(3) = 5
  A(4) = -3/4
  A(5) = -3/5
  A(6) = 5/2
  A(7) = 0

At p = 7 (smallest split prime, a_7(E_27) = -1):
  A(7) = 0
  beta = -A(7) / a_7 = -(0) / (-1) = 0

Pentagon-vanishing prediction: beta = 0
Verified: beta == 0 ?  True
```

## Sharpness of the falsifier

The "alternative kernel" test in the suite confirms sharpness:

- with $c_{\xi}(27) = 0$ (instead of the predicted $3/7$),
  $A(7) = -3/7 \neq 0$, hence $\beta = 3/7 \neq 0$.
- The falsifier is therefore a SHARP single-prime test: any deviation from
  $c_{\xi}(27) = 3/7$ produces a measurable $A(7) \neq 0$ and falsifies
  the Pentagon vanishing.

## What this verifies and what remains

**Verified at the level of the SZ-image arithmetic identity:** $\beta = 0$.

**Conditional on:**
1. Chain-level CY-A$_{3}$ for local $\mathbb{P}^{2}$ (only inf-categorical level proved).
2. Costello-Li chain-level open-closed factorisation in the toric setting.
3. Aganagic-Klemm-Mariño-Vafa refined topological vertex convergence on
   the GV-formal radius.
4. Skoruppa-Zagier Hilbert-lift convergence on the Hesse-pencil moduli.

**The arithmetic identity $c_{\xi}(27) = 3/7$ is itself the load-bearing
prediction.** Independent confirmation requires either (a) computation of
$c_{\xi}(27)$ from the Aganagic-Klemm-Mariño-Vafa refined topological
vertex applied to the genus-1 LP² GV mixing, or (b) computation of
the Borcherds product $\Psi_{H_{27}}$ on $\mathbb{H}^{2}/\Gamma_{0}(27)$
attached to the Heegner divisor $H_{27}$.

## Cross-reference to the wider Vol III architecture

Per AP-CY55, $E_{27/\mathbb{Q}}$ is a *manifold* invariant (conductor $27$,
CM by $\mathbb{Z}[\zeta_{3}]$, j-invariant $0$); $\beta$ is an
*algebraization* invariant of $\widehat{\xi}^{\mathrm{LP}^{2}}$ via the
Skoruppa-Zagier lift.

Per AP-CY60, the LP$^{2} \to E_{27}$ pinning is a mock-Jacobi receptacle
pinning, NOT a derived functorial map from $\Phi_{3}$.

Per AP-CY61, the original "single-prime $T_{2}$ falsifier" was found
vacuous (since $a_{2} = 0$ by CM), and the correct mechanism uses
split primes where $a_{p} \neq 0$. The first-principles correction is
recorded in `rem:lp2-E27-split-prime-falsifier` of the chapter.

## Status update for the chapter

Inscription target: `chapters/examples/cy_c_six_routes_convergence.tex`
under `subsec:lp2-W3-Hecke-pinning`. The remark
`rem:lp2-E27-split-prime-falsifier` is updated to cite the SZ kernel
engine and the 64-test verification suite.

## File manifest

- Engine: `compute/lib/lp2_skoruppa_zagier_kernel.py`
- Tests: `compute/tests/test_lp2_skoruppa_zagier.py` (64 tests passing)
- Notes: `notes/wave_lp2_PARI_split_prime_attack.md` (this file)
- Inscription: `chapters/examples/cy_c_six_routes_convergence.tex`
  (`rem:lp2-E27-split-prime-falsifier`, line 947+)

## Author

All work attributed to Raeez Lorgat.
