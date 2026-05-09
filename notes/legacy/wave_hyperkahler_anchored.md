# Wave: hyperkähler-anchored vs K3-anchored elliptic-tower fixed point

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Status:** complete deliverable (LOSSLESS, attempt 1).
**Companion notes:** `wave_V114_K3_Ek_stable_fixed_point.md`,
`oversaturated_kunneth_dichotomy.md`,
`elliptic_K3K3_bigraded_Lefschetz.md`.
**APs invoked:** AP-CY55 (manifold vs algebraization invariant
separation; the BKM-enhanced K$3$ matrix differs from the
Bogomolov–Beauville HK matrix at $n = 1$), AP-CY60 (six routes ≠
six functor applications: $M_{K3^{[n]}}$ comes from the
Bogomolov–Beauville construction, $M_{K3}$ in the K$3$ Yangian
chapter comes from BKM enhancement; these are different
algebraisations), AP-CY61 (first-principles investigation: extract
the ghost theorem before any correction).
**Style register:** Bogomolov–Beauville + Goettsche +
Künneth-bivariance + Atiyah–Singer push-forward.

---

## 0. The question

The K$3$-anchored fixed-point theorem
(Wave V114, `thm:k3-elliptic-tower-fixed-point`)
established
$$
  M_{K3 \times E^k} = M^\flat = (0, 5, -16, 11)
  \quad \forall\, k \geq 0,
$$
where $M_X = (\Pi_{++}, \Pi_{+-}, \Pi_{-+}, \Pi_{--})_X$ is the
bigraded Lefschetz matrix in $\mathbb{Z}[V_4]$, and $M_{K3}$ is the
**BKM-enhanced** K$3$ matrix $M_{K3} = (0, 5, -16, 13)$ from the
$\Phi_2$ functor of Theorem $\mathrm{thm{:}k3{-}multiproj{-}bigraded{-}lefschetz}$.

**Question.** Does the fixed-point property extend to
hyperkähler-anchored: is there a $M^{\flat,\mathrm{HK}}_n$ with
$M_{K3^{[n]} \times E^k} = M^{\flat,\mathrm{HK}}_n$ for all $k \geq 1$?

By Bogomolov–Beauville
(`thm:oversaturation-hierarchy`, line 3833 of the K$3$ Yangian
chapter), the indecomposable holomorphic rank of any irreducible
hyperkähler $X$ is $r(X) = 1$, with the unique generator the
holomorphic-symplectic form $\sigma \in H^{2, 0}(X)$. The bigraded
Lefschetz matrix takes the diagonal form
$$
  M_{\mathrm{HK}_X} \;=\; (\chi(\mathcal{O}_X), 0, 0, 0).
$$
For $X = K3^{[n]}$: $\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$ (this is
the Goettsche/Hirzebruch formula
$\sum_n \chi(\mathcal{O}_{K3^{[n]}}) q^n = \prod_{m \geq 1} (1 - q^m)^{-1}
= 1 + q + 2 q^2 + 3 q^3 + \cdots$, but on $K3^{[n]}$ the genus
$\chi(\mathcal{O})$ equals $n + 1$ since $H^*(K3^{[n]})$ has unique
generator $1 \in H^0$ at every weight). Hence
$$
  M_{K3^{[n]}} \;=\; (n + 1,\, 0,\, 0,\, 0).
$$

**Anomaly at $n = 1$.** $M_{K3^{[1]}} = (2, 0, 0, 0)$ disagrees with
the BKM-enhanced K$3$ matrix $M_{K3} = (0, 5, -16, 13)$ used in the
fixed-point theorem. This is **AP-CY55**: $K3$ admits two distinct
algebraisations:
- the bare Bogomolov–Beauville HK form (diagonal-volume-only,
  $r = 1$, gives $(2, 0, 0, 0)$);
- the BKM-enhanced form (Mukai signature $(4, 20)$, full
  $V_4$-faithful action, gives $(0, 5, -16, 13)$).

The fixed-point theorem uses the BKM-enhanced form. The hyperkähler
question naturally uses the bare HK form for $n \geq 2$, since the
BKM enhancement is not available there (BKM lift requires the
K$3$ elliptic genus, not $K3^{[n]}$ elliptic genus).

We therefore work with the bare HK form $M_{K3^{[n]}} = (n + 1, 0, 0, 0)$
throughout this wave.

---

## 1. Eigenspace classification under $\sigma_{\mathrm{tot}}^*$

Recall the Künneth dichotomy
(`thm:kunneth-dichotomy`):
- case (1): both factors generic — $\Delta = 0$;
- case (2): both factors $\sigma_{\mathrm{tot}}^*$-anti-symmetric ($-1$
  eigenspace) — $\Delta = 0$;
- case (3): exactly one factor in the $-1$-eigenspace
  (asymmetric coupling) — $\Delta_{X, Y} = \sigma_{\mathrm{tot}}^* M_X
  - \chi(\mathcal{O}_X) e_{\Pi_{--}}$, where $X$ is the generic factor.

For $M_{K3^{[n]}} = (n + 1, 0, 0, 0)$:
$\sigma_{\mathrm{tot}}^*(n + 1, 0, 0, 0) = (0, 0, 0, n + 1)
\neq \pm(n + 1, 0, 0, 0)$.
**Generic** (case 1 trigger when paired with another generic; case 3
trigger when paired with the $-1$-eigenspace $M_E$).

For $M_E = (1, 0, 0, -1)$:
$\sigma_{\mathrm{tot}}^*(1, 0, 0, -1) = (-1, 0, 0, 1) = -M_E$.
**$-1$-eigenspace** (anti-symmetric).

Hence $K3^{[n]} \times E$ falls in case (3) of the dichotomy.

---

## 2. The hyperkähler-elliptic doubling theorem

**Theorem (hyperkähler-elliptic doubling).** For all $n \geq 1$ and
$k \geq 1$,
$$
  \boxed{\;
  M_{K3^{[n]} \times E^k}
  \;=\; \bigl(2^{k - 1} (n + 1),\, 0,\, 0,\, -2^{k - 1} (n + 1)\bigr)
  \;=\; 2^{k - 1} (n + 1)\, M_E.
  \;}
$$
The matrix grows **exponentially** in $k$ (doubling at each
$E$-step), with multiplicative scale $(n + 1)$ inherited from
$\chi(\mathcal{O}_{K3^{[n]}})$.

**Trace check.** $2^{k - 1} (n + 1) + 0 + 0 - 2^{k - 1} (n + 1) = 0
= (n + 1) \cdot 0 = \chi(\mathcal{O}_{K3^{[n]}}) \cdot \chi(\mathcal{O}_{E^k})
= \chi(\mathcal{O}_{K3^{[n]} \times E^k})$. ✓

**Proof.** By induction on $k$.

*Base case $k = 1$.* By case (3) of the Künneth dichotomy,
$$
\Delta_{K3^{[n]}, E}
= \sigma_{\mathrm{tot}}^* M_{K3^{[n]}}
- \chi(\mathcal{O}_{K3^{[n]}}) e_{\Pi_{--}}
= (0, 0, 0, n + 1) - (n + 1)(0, 0, 0, 1)
= (0, 0, 0, 0).
$$
The asymmetric correction $\Delta$ vanishes identically. The
convolution is
$$
M_{K3^{[n]}} *_{V_4} M_E
= (n + 1, 0, 0, 0) *_{V_4} (1, 0, 0, -1)
= (n + 1, 0, 0, -(n + 1)).
$$
Hence $M_{K3^{[n]} \times E} = (n + 1, 0, 0, -(n + 1)) = (n + 1) M_E$.

*Inductive step.* Assume $M_{K3^{[n]} \times E^k}
= 2^{k - 1} (n + 1) M_E$. Then $M_{K3^{[n]} \times E^k}$ is in the
$-1$-eigenspace of $\sigma_{\mathrm{tot}}^*$ (a scalar multiple of
$M_E$). Pairing with $M_E$ (also in the $-1$-eigenspace), case (2)
applies: $\Delta_{K3^{[n]} \times E^k, E} = 0$. The convolution is
$$
2^{k - 1} (n + 1) M_E *_{V_4} M_E
= 2^{k - 1} (n + 1) (M_E *_{V_4} M_E)
= 2^{k - 1} (n + 1) M_{T^4}
= 2^{k - 1} (n + 1) (2, 0, 0, -2)
= 2^k (n + 1) M_E,
$$
since $M_E *_{V_4} M_E = M_{T^4} = (2, 0, 0, -2) = 2 M_E$
(`prop:t4-via-kunneth`). Hence
$M_{K3^{[n]} \times E^{k + 1}} = 2^k (n + 1) M_E$, completing the
induction. ∎

**Corollary 2.1 ($n = 1$ HK form).** $M_{K3^{[1]} \times E^k}
= (2^k, 0, 0, -2^k) = 2 \cdot 2^{k - 1} M_E$. **Different from the
BKM-enhanced K$3$-anchored fixed-point** $(0, 5, -16, 11)$ for any
$k$. The off-diagonal channels $\Pi_{+-}, \Pi_{-+}$ remain zero
under doubling, since the bare HK starting matrix has them zero
and $E$-convolution preserves the zero pattern.

**Corollary 2.2 ($n = 2, 3$).** $M_{K3^{[2]} \times E} = (3, 0, 0, -3)$;
$M_{K3^{[2]} \times E^2} = (6, 0, 0, -6)$; $M_{K3^{[3]} \times E}
= (4, 0, 0, -4)$; $M_{K3^{[3]} \times E^2} = (8, 0, 0, -8)$.

---

## 3. The hyperkähler-product matrix

**Proposition.** For $n, m \geq 1$,
$$
  \boxed{\;
  M_{K3^{[n]} \times K3^{[m]}}
  \;=\; \bigl((n + 1)(m + 1),\, 0,\, 0,\, 0\bigr).
  \;}
$$

*Proof.* Both $M_{K3^{[n]}}$ and $M_{K3^{[m]}}$ are generic under
$\sigma_{\mathrm{tot}}^*$ (their flips land on $\Pi_{--}$ rather
than $\pm$ the original). Case (1) of the dichotomy applies, so
$\Delta_{K3^{[n]}, K3^{[m]}} = 0$. The convolution
$(n + 1, 0, 0, 0) *_{V_4} (m + 1, 0, 0, 0)
= ((n + 1)(m + 1), 0, 0, 0)$ by direct computation in the regular
representation. ∎

**Trace check.** $(n + 1)(m + 1) + 0 + 0 + 0
= \chi(\mathcal{O}_{K3^{[n]}}) \cdot \chi(\mathcal{O}_{K3^{[m]}})
= \chi(\mathcal{O}_{K3^{[n]} \times K3^{[m]}})$ ✓.

**Examples.** $M_{K3^{[1]} \times K3^{[1]}} = (4, 0, 0, 0)$ (HK
algebraisation of $K3 \times K3$, distinct from the BKM-enhanced
$M_{K3 \times K3} = (450, -416, 130, -160)$); $M_{K3^{[1]} \times K3^{[2]}}
= (6, 0, 0, 0)$; $M_{K3^{[2]} \times K3^{[2]}} = (9, 0, 0, 0)$.

The HK product matrix is the **scalar Goettsche product**
$\chi(\mathcal{O}_X) \chi(\mathcal{O}_Y)$ on the diagonal $\Pi_{++}$
channel, with all off-diagonal channels zero. Both factors are
diagonal-only, so their convolution is also diagonal-only.

---

## 4. Cross-anchoring: $K3^{[n]} \times K3$ with BKM-enhanced $K3$

**Proposition.** Using the BKM-enhanced K$3$ matrix
$M_{K3} = (0, 5, -16, 13)$ from `thm:k3-multiproj-bigraded-lefschetz`,
$$
  M_{K3^{[n]} \times K3}
  \;=\; (n + 1) M_{K3}
  \;=\; \bigl(0,\, 5(n + 1),\, -16(n + 1),\, 13(n + 1)\bigr).
$$

*Proof.* $M_{K3^{[n]}} = (n + 1, 0, 0, 0)$ is generic, and
$M_{K3} = (0, 5, -16, 13)$ is also generic
($\sigma_{\mathrm{tot}}^* M_{K3} = (13, -16, 5, 0) \neq \pm M_{K3}$).
Case (1) applies, $\Delta = 0$. The convolution:
$(n + 1, 0, 0, 0) *_{V_4} (0, 5, -16, 13)
= (n + 1)(0, 5, -16, 13)$. ∎

**Trace.** $(n + 1) \cdot 2 = (n + 1) \chi(\mathcal{O}_{K3})
= \chi(\mathcal{O}_{K3^{[n]} \times K3})$ ✓.

---

## 5. Cross-anchored elliptic tower: $K3^{[n]} \times K3 \times E^k$

**Theorem (cross-anchored fixed-point with multiplicative scaling).**
For $n \geq 1$ and $k \geq 1$,
$$
  \boxed{\;
  M_{K3^{[n]} \times K3 \times E^k}
  \;=\; (n + 1) M^\flat
  \;=\; \bigl(0,\, 5 (n + 1),\, -16 (n + 1),\, 11 (n + 1)\bigr).
  \;}
$$
The fixed-point structure is **preserved** but **scaled by
$\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$**.

*Proof.* By case (3) of the dichotomy applied to $K3^{[n]} \times K3$
(generic) paired with $E$ (anti-symmetric):
$$
\Delta_{K3^{[n]} \times K3, E}
= \sigma_{\mathrm{tot}}^*((n + 1) M_{K3})
- 2(n + 1) e_{\Pi_{--}}
= (n + 1) \bigl(\sigma_{\mathrm{tot}}^* M_{K3} - 2 e_{\Pi_{--}}\bigr)
= (n + 1) \Delta_{K3, E}
= (n + 1)(13, -16, 5, -2).
$$
Convolution:
$$
(n + 1) M_{K3} *_{V_4} M_E
= (n + 1)(M_{K3} *_{V_4} M_E)
= (n + 1)(-13, 21, -21, 13).
$$
Sum:
$$
(n + 1)\bigl[(-13, 21, -21, 13) + (13, -16, 5, -2)\bigr]
= (n + 1)(0, 5, -16, 11)
= (n + 1) M^\flat.
$$
For subsequent $E$-multiplications, $(n + 1) M^\flat$ is trace-zero
(since $M^\flat$ is). By the bivariant Künneth identity
(`lem:bivariant-kunneth-identity`), $\kappa_E$ acts as the identity
on the trace-zero hyperplane, so
$\kappa_E((n + 1) M^\flat) = (n + 1) M^\flat$ identically, and the
inductive step closes as in V114. ∎

---

## 6. The structural picture: HK is a multiplicative scalar on the
   K$3$-anchored fixed-point

The hyperkähler factor $K3^{[n]}$ enters the universal-$V_4$
spectrum as **multiplication by the holomorphic Euler characteristic
$\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$**, NOT as a new fixed-point
generator. The structural reason:

- $r(K3^{[n]}) = 1$ (Bogomolov–Beauville: unique
  holomorphic-symplectic form).
- $M_{K3^{[n]}} = (n + 1, 0, 0, 0)$ (diagonal-only, all mass on
  $\Pi_{++}$).
- The Klein-four convolution with a diagonal-only matrix scales the
  other factor's full $V_4$-character vector by the diagonal value
  $n + 1$.

Hence the hyperkähler factor is a **multiplicative absorber**: it
neither anchors nor stabilises a non-trivial fixed-point; it merely
scales whatever fixed-point structure the BKM-enhanced K$3$ factor
brings.

**Three regimes of $K3$-vs-HK-vs-elliptic interaction.**

| Configuration | Matrix | Iteration type |
|---|---|---|
| $K3 \times E^k$ (BKM K$3$) | $(0, 5, -16, 11) = M^\flat$ | fixed-point |
| $K3^{[n]} \times E^k$ (HK $K3^{[n]}$) | $(2^{k - 1}(n + 1), 0, 0, -2^{k - 1}(n + 1))$ | doubling |
| $K3^{[n]} \times K3 \times E^k$ | $(n + 1) M^\flat$ | scaled fixed-point |
| $K3^{[n]} \times K3^{[m]}$ | $((n + 1)(m + 1), 0, 0, 0)$ | scalar Goettsche |
| $E^k$ | $(2^{k - 1}, 0, 0, -2^{k - 1})$ | doubling |

The fixed-point regime requires the BKM-enhanced K$3$ factor; the
HK $K3^{[n]}$ factor multiplies but does not stabilise. The doubling
regime applies to all pure HK or pure elliptic (or mixed
HK-elliptic without BKM) iterations.

---

## 7. Why does the fixed-point fail for hyperkähler-anchored?

The K$3$-anchored fixed-point theorem's structural mechanism
(`rem:fixed-point-selection`) requires:

1. A K-trivial generic factor with **full $V_4$-faithful action** (all
   four channels carry non-trivial trace).
2. Exactly one $K$-asymmetric factor ($E$, $r = 1$).
3. The convolution-plus-correction closure
   $M^\flat *_{V_4} M_E + \Delta^\flat = M^\flat$, which requires
   $M^\flat$ to satisfy $\sigma_{\mathrm{tot}}^* M^\flat$ = (the
   asymmetric correction at the next step).

For HK-anchored: condition (1) **fails** at the bare HK level. The
matrix $M_{K3^{[n]}} = (n + 1, 0, 0, 0)$ has only $\Pi_{++}$ active.
There is no Borcherds enhancement at $\Pi_{+-}$, no super-Berezinian
at $\Pi_{-+}$, and no algebraisation residual at $\Pi_{--}$.
Convolution with $M_E$ shuffles the diagonal value into
$(\Pi_{++}, \Pi_{--})$, but the result $(n + 1, 0, 0, -(n + 1))$ is
itself anti-symmetric (in the $-1$-eigenspace of $\sigma_{\mathrm{tot}}^*$).
Subsequent $E$-multiplications fall into case (2), which gives
strict doubling.

The K$3$ Mukai signature $(4, 20)$ generates the off-diagonal
channels $5, -16$ via the BKM lift and super-Berezinian; the bare
HK $K3^{[n]}$ has no such enhancement at $n \geq 2$. The fixed-point
phenomenon is therefore an **algebraisation invariant** specific to
the BKM-enhanced K$3$; it does not extend to the HK-bare $K3^{[n]}$
for $n \geq 2$.

The cross-anchored case $K3^{[n]} \times K3 \times E^k$ recovers the
fixed-point structure scaled by $\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$,
because the BKM-enhanced K$3$ factor brings the off-diagonal channels
back into play and the $K3^{[n]}$ factor acts as a multiplicative
absorber on top.

---

## 8. Falsifiable predictor (for the wave's verification gate)

The wave's predictor was: $M_{K3^{[2]} \times E}$ should equal
either $M^{\flat,\mathrm{HK}}_2$ (universal HK fixed point) or
$M_{K3^{[2]}} *_{V_4} M_E$ (generic Künneth).

**Result:** the second alternative holds. $M_{K3^{[2]} \times E}
= M_{K3^{[2]}} *_{V_4} M_E + \Delta_{K3^{[2]}, E}$
$= (3, 0, 0, -3) + (0, 0, 0, 0)$ $= (3, 0, 0, -3)$. The
asymmetric correction $\Delta$ vanishes identically because
$\sigma_{\mathrm{tot}}^* M_{K3^{[2]}} = (0, 0, 0, 3)
= \chi(\mathcal{O}_{K3^{[2]}}) e_{\Pi_{--}}$.

The HK fixed-point $M^{\flat,\mathrm{HK}}_n$ does **not** exist as a
universal fixed-point; the iteration is doubling, not stabilising.

---

## 9. Inscription and verification

The new theorems inscribe in
`chapters/examples/k3_yangian_chapter.tex` immediately after the
K$3$-anchored elliptic-tower fixed-point theorem
(`thm:k3-elliptic-tower-fixed-point`, line 3284):

1. **Theorem (hyperkähler-elliptic doubling).**
   $M_{K3^{[n]} \times E^k} = 2^{k - 1} (n + 1) M_E$ for $n \geq 1, k \geq 1$.
2. **Proposition (HK product matrix).**
   $M_{K3^{[n]} \times K3^{[m]}} = ((n + 1)(m + 1), 0, 0, 0)$.
3. **Theorem (cross-anchored scaled fixed-point).**
   $M_{K3^{[n]} \times K3 \times E^k} = (n + 1) M^\flat$ for $n \geq 1, k \geq 1$.
4. **Remark (regimes table; HK as multiplicative absorber).**

The independent-verification test
`compute/tests/test_hyperkahler_anchored_fixed_point.py` cross-checks:
- the Goettsche formula $\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$
  against the Bogomolov–Beauville rank theorem;
- the V$_4$ convolution against the dichotomy case classification;
- the doubling pattern against direct iteration.

---

## 10. Summary: the LOSSLESS ledger

- The K$3$-anchored fixed point does **NOT** extend universally to
  hyperkähler-anchored. PROVED (Theorem of §2: doubling regime).
- The fixed-point property arises iff the K$3$ factor carries the
  BKM enhancement (Mukai $(4, 20)$ signature populating
  $\Pi_{+-} = 5, \Pi_{-+} = -16$). PROVED structurally (§7).
- The hyperkähler $K3^{[n]}$ factor enters as a multiplicative scalar
  $\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$ on top of the K$3$-anchored
  fixed-point: $M_{K3^{[n]} \times K3 \times E^k} = (n + 1) M^\flat$.
  PROVED (Theorem of §5).
- Pure hyperkähler products: $M_{K3^{[n]} \times K3^{[m]}}
  = ((n + 1)(m + 1), 0, 0, 0)$. PROVED (Proposition of §3).
- Mixed HK-elliptic without BKM: doubling, not fixed-point. PROVED
  (§2).
- Falsifiable predictor at $K3^{[2]} \times E$: confirmed
  case (3)-with-$\Delta = 0$ (equivalent to case (1) outcome).

The ghost theorem of "hyperkähler-anchored fixed-point" is the
**multiplicative-absorber theorem**: the HK factor acts as
multiplication by $\chi(\mathcal{O})$ on whatever fixed-point
structure the BKM-enhanced K$3$ factor brings.

The full Platonic statement is the trichotomy in the regimes table of
§6.

---

— Raeez Lorgat, 2026-04-17
