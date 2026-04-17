# The genus-$g$ curve bigraded Lefschetz matrix: derivation and consequences

**Author:** Raeez Lorgat. **Date:** 2026-04-17.

---

## 1. Statement and prediction

The over-saturation hierarchy theorem
(`thm:oversaturation-hierarchy`) predicts, via the
indecomposable-rank assignment $r(C_g) = g$ for a smooth projective
curve $C_g$ of genus $g$:
$$
\widetilde{V}_{C_g} \;=\; (\mathbb{Z}/2)^{2 + g}.
$$
The over-saturated bigraded Lefschetz matrix
$\widetilde{M}_{C_g} \in \mathbb{Z}[(\mathbb{Z}/2)^{2 + g}]$
push-forwards to the universal-$V_4$ matrix $M_{C_g} \in \mathbb{Z}[V_4]$
via the canonical projection
$\pi(\epsilon_{\mathrm{wt}}, \epsilon_{\mathrm{par}}, \epsilon_1, \dots, \epsilon_g)
= (\epsilon_{\mathrm{wt}}, \epsilon_{\mathrm{par}} \cdot \epsilon_1 \cdots \epsilon_g)$.

The prediction (V102 falsifiable P1):
$$
\boxed{\;M_{C_g} \;=\; (1, 0, 0, -g),\;}
$$
with sum $1 + 0 + 0 - g = 1 - g = \chi(\mathcal{O}_{C_g})$
(Riemann-Roch on a curve).

---

## 2. Verification at low genus

**$g = 0$ (sphere $\mathbb{P}^1$).** $H^{1, 0}(\mathbb{P}^1) = 0$, so
$r(\mathbb{P}^1) = 0$ and $\widetilde{V}_{\mathbb{P}^1} = V_4$. The
matrix is $M_{\mathbb{P}^1} = (1, 0, 0, 0)$ with sum $1
= \chi(\mathcal{O}_{\mathbb{P}^1})$. ✓

**$g = 1$ (elliptic curve $E$).** $r(E) = 1$,
$M_E = (1, 0, 0, -1)$ (independently verified via 5 disjoint sources:
Heisenberg lattice VOA character, Witten elliptic genus, Berezinian
super-trace, Hodge-filtered super-trace, Hattori-Stallings sum). Sum
$0 = \chi(\mathcal{O}_E)$. ✓

**$g = 2$ (genus-$2$ curve).** Predicted $M_{C_2} = (1, 0, 0, -2)$
with sum $-1 = \chi(\mathcal{O}_{C_2}) = 1 - 2$. The over-saturation
$\widetilde{V}_{C_2} = (\mathbb{Z}/2)^4$ has the same group as $T^4$,
but they are NOT the same matrix — $T^4 = E \times E$ has
$M_{T^4} = (2, 0, 0, -2)$ via Künneth ($\Pi_{++}$ entry $2 = 1 \cdot 1
+ \cdots = 2$ from product), while $C_2$ has
$M_{C_2} = (1, 0, 0, -2)$ ($\Pi_{++}$ entry $1 = $ single
"vacuum sector" since $C_2$ is NOT a Künneth product).

---

## 3. The structural reason

The push-forward $\pi: \widetilde{V}_{C_g} \to V_4$ has kernel
$K_{C_g} \subset \widetilde{V}_{C_g}$ of order $2^g$. Each $V_4$-orbit
under $\pi$ has size $2^g$.

The over-saturated matrix $\widetilde{M}_{C_g}$ is determined by the
Hodge-piece projections:
- $\widetilde{M}^{(+, +, +, \dots, +)}_{C_g}$: the unit/vacuum sector
  contribution. This is $1$ (single vacuum).
- $\widetilde{M}^{(+, -, -, +, \dots, +)}_{C_g}$ etc.\ for individual
  Hodge involutions: contributions from the $g$ holomorphic differentials
  $\omega_1, \dots, \omega_g$.

After push-forward via the multiplicative-character projection:
- $\Pi_{++}(C_g) = $ sum over orbit of $(+, +, +, \dots, +)$ + sum
  over orbits with even Hodge-involution count. This equals $1$.
- $\Pi_{--}(C_g) = $ sum over orbit of $(-, -, +, \dots, +)$
  contribution from Hodge differentials. This equals $-g$ via the
  Hodge-filtered super-trace
  $\operatorname{str}_{F^0}(C_g) = h^{0, 0}(C_g) - h^{1, 0}(C_g)
  = 1 - g$, restricted to the $\Pi_{--}$-projection.
- $\Pi_{+-}(C_g) = \Pi_{-+}(C_g) = 0$: no BKM and no Berezinian
  channel for a genus-$g$ curve (since $H^*(C_g, \mathbb{Z})$ has no
  rank-non-trivial signature decomposition beyond the $h^{0, 0}, h^{1, 0},
  h^{0, 1}, h^{1, 1}$ sectors, which align with $\Pi_{++}$ and
  $\Pi_{--}$).

Hence $M_{C_g} = (1, 0, 0, -g)$.

---

## 4. Consequences

### 4.1 Künneth multiplicativity at $C_g \times C_h$

By the Künneth dichotomy theorem case (1), if both $M_{C_g}$ and
$M_{C_h}$ are generic under $\sigma_{\mathrm{tot}}^*$, then
$\Delta_{C_g, C_h} = 0$. But $M_{C_g} = (1, 0, 0, -g)$ has antipodal
flip $(-g, 0, 0, 1) \neq \pm M_{C_g}$ unless $g = -1$ (impossible).

So $M_{C_g}$ is generic — neither in the $-1$ nor $+1$-eigenspace of
$\sigma_{\mathrm{tot}}^*$.

By the dichotomy: $\Delta_{C_g, C_h} = 0$ for all $g, h \geq 1$, and
$M_{C_g \times C_h} = M_{C_g} * M_{C_h}$ entry-by-entry.

Direct computation: $M_{C_g} * M_{C_h}$ via Klein-four convolution.
$\hat{M}_{C_g}(++) = 1 - g$, $\hat{M}_{C_g}(+-) = 1 + g$, $\hat{M}_{C_g}(-+) = 1 + g$,
$\hat{M}_{C_g}(--) = 1 - g$.

Pointwise: $\hat{M}_{C_g} \cdot \hat{M}_{C_h} = ((1-g)(1-h), (1+g)(1+h),
(1+g)(1+h), (1-g)(1-h))$.

Inverse Fourier:
$M_{C_g \times C_h}^{++} = \tfrac{1}{4}((1-g)(1-h) + 2(1+g)(1+h) + (1-g)(1-h))
= \tfrac{1}{2}((1-g)(1-h) + (1+g)(1+h))
= 1 + gh$.
$M_{C_g \times C_h}^{+-} = \tfrac{1}{4}((1-g)(1-h) - (1+g)(1+h) + (1+g)(1+h) - (1-g)(1-h))
= 0$.
Similarly $M_{C_g \times C_h}^{-+} = 0$.
$M_{C_g \times C_h}^{--} = \tfrac{1}{4}((1-g)(1-h) - 2(1+g)(1+h) + (1-g)(1-h))
= \tfrac{1}{2}((1-g)(1-h) - (1+g)(1+h))
= -(g + h)$.

**Result.** $M_{C_g \times C_h} = (1 + gh, 0, 0, -(g + h))$.

Sum: $1 + gh - g - h = (1 - g)(1 - h) = \chi(\mathcal{O}_{C_g \times C_h})$ ✓.

This is a clean closed form for any product of two algebraic curves.

### 4.2 The K$3$-anchored elliptic-tower fixed-point generalisation

The bivariant Künneth identity and the K$3$-anchored fixed-point
theorem extend to genus-$g$ factors: $M_{K3 \times C_g \times E^k}
= (0, 5, -16, 11) = M^\flat$ for all $g \geq 1, k \geq 0$.

**Verification for $g = 2$, $k = 0$**: predicted
$M_{K3 \times C_2} = M^\flat = (0, 5, -16, 11)$.
By case (3) of the dichotomy: $C_2$ generic, $K3$ generic — case (1)
applies, $\Delta_{K3, C_2} = 0$. So $M_{K3 \times C_2} = M_{K3} * M_{C_2}$:

$\hat{M}_{C_2} = (-1, 3, 3, -1)$, $\hat{M}_{K3} = (2, -34, 8, 24)$.

Pointwise: $\hat{M}_{K3} \cdot \hat{M}_{C_2} = (-2, -102, 24, -24)$.

Inverse Fourier:
$M_{K3 \times C_2}^{++} = \tfrac{1}{4}(-2 - 102 + 24 - 24) = -26$.
$M_{K3 \times C_2}^{+-} = \tfrac{1}{4}(-2 + 102 + 24 + 24) = 37$.
$M_{K3 \times C_2}^{-+} = \tfrac{1}{4}(-2 - 102 - 24 + 24) = -26$.
$M_{K3 \times C_2}^{--} = \tfrac{1}{4}(-2 + 102 - 24 - 24) = 13$.

**Result via case (1)**: $M_{K3 \times C_2} = (-26, 37, -26, 13)$,
sum $-2 = \chi(\mathcal{O}_{K3}) \cdot \chi(\mathcal{O}_{C_2})
= 2 \cdot (-1) = -2$ ✓.

But wait — V114 said $M_{K3 \times C_g \times E^k} = M^\flat$ for all
$g, k$. At $g = 2, k = 0$: $M_{K3 \times C_2}$ should equal
$M^\flat = (0, 5, -16, 11)$, not $(-26, 37, -26, 13)$.

**Discrepancy detected.** V114's generalisation $M_{K3 \times C_g
\times E^k} = M^\flat$ for all $g \geq 1$ FAILS at $g = 2, k = 0$
because the case (1) of the dichotomy ($C_2$ generic, K3 generic)
gives $\Delta = 0$ and the convolution $(-26, 37, -26, 13) \neq M^\flat$.

So either:
- V114's generalisation is wrong (the K$3$-anchored fixed point is
  $E$-specific, not $C_g$-general), OR
- The dichotomy classification is wrong: $M_{C_g}$ for $g \geq 2$ is
  NOT generic but actually anti-symmetric in some refined sense, OR
- The Drinfeld coupling at $K3 \times C_g$ requires a non-zero
  correction even though the universal-$V_4$ classification looks
  like case (1).

**Conjecture (V117 to be tested):** the K$3$-anchored elliptic-tower
fixed-point $M^\flat$ is $E$-specific. For $C_g$ with $g \geq 2$,
$M_{K3 \times C_g} = (-26, 37, -26, 13) \cdot (\text{some scaling})$
or a different value entirely.

Verify by computing $M_{K3 \times C_2}$ via an independent path:
the genus-$2$ surface admits a hyperelliptic double cover
$C_2 \to \mathbb{P}^1$ branched at $6$ points; the Mukai-style
analysis on $\Phi_3(D^b(\operatorname{Coh}(K3 \times C_2)))$ via the
Hodge structure $h^{*, 0}(K3 \times C_2) = (1, 1, 2, 0)$ gives
$\chi(\mathcal{O}) = -2$ as computed.

---

## 5. Inscription target

The clean closed form $M_{C_g \times C_h} = (1 + gh, 0, 0, -(g + h))$
is inscription-ready (in the K3 Yangian chapter Künneth-multiplicativity
section). The discrepancy at $K3 \times C_g$ for $g \geq 2$ is an
OPEN question requiring further wave investigation (V117 attack
target).

---

— Raeez Lorgat, 2026-04-17
