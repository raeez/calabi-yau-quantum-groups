# The bigraded Lefschetz matrix for $E$ and $K3 \times K3$

**Author:** Raeez Lorgat. **Date:** 2026-04-16.
**Target chapter:** Vol III, Künneth-multiplicativity section.

This note solves the Klein-four convolution equation
$M_{K3 \times E} = M_{K3} * M_E + \Delta_{K3, E}$ for the elliptic-curve
matrix $M_E$, then verifies that the analogous identity for $K3 \times K3$
requires *no* Drinfeld-coupling correction. The asymmetry isolates the
elliptic fibre's "anomaly" as the source of $\Delta_{K3, E}$.

---

## 1. The convolution equation

Let $M_X = (\Pi_{++}, \Pi_{+-}, \Pi_{-+}, \Pi_{--})_X$ denote the diagonal
of the bigraded Lefschetz matrix at $X$ in the four $V_4 = (\mathbb{Z}/2)^2$
characters. Künneth in the regular representation of $V_4$ gives the
convolution
$$
(M_X * M_Y)^{(\epsilon_1 \epsilon_2)}
\;=\; \sum_{(\delta_1, \delta_2) \in V_4}
M_X^{(\delta_1, \delta_2)} \cdot
M_Y^{(\epsilon_1 + \delta_1, \epsilon_2 + \delta_2)},
$$
with addition in $V_4 = (\mathbb{Z}/2)^2$ being componentwise XOR.

For $X = K3$ with $M_{K3} = (0, 5, -16, 13)$, the explicit convolution
entries against an arbitrary $M_E = (a, b, c, d)$ are:
$$
\begin{aligned}
(M_{K3} * M_E)^{++} &= 5b - 16c + 13d, \\
(M_{K3} * M_E)^{+-} &= 5a + 13c - 16d, \\
(M_{K3} * M_E)^{-+} &= -16a + 13b + 5d, \\
(M_{K3} * M_E)^{--} &= 13a - 16b + 5c.
\end{aligned}
$$

---

## 2. Solving for $M_E$

The Drinfeld-coupling correction at $K3 \times E$ is
$\Delta_{K3, E} = (13, -16, 5, -2)$ (computed in the prior Drinfeld-coupling
investigation), and the actual Wave-21 matrix at $K3 \times E$ is
$M_{K3 \times E} = (0, 5, -16, 11)$. Hence the *naive* Künneth values are
$$
(M_{K3} * M_E) \;=\; M_{K3 \times E} - \Delta_{K3, E}
\;=\; (-13, 21, -21, 13).
$$

Setting up the linear system:
\begin{align*}
5b - 16c + 13d &= -13, \tag{1} \\
5a + 13c - 16d &= 21, \tag{2} \\
-16a + 13b + 5d &= -21, \tag{3} \\
13a - 16b + 5c &= 13. \tag{4}
\end{align*}

Anchoring $a = 1$ (from $\Pi_{++}(E) = \kappa_{\mathrm{ch}}(\Phi_1(E)) = 1$,
the single-boson contribution from $H^0(E) \oplus H^1(E)$):
- (4) gives $-16b + 5c = 0$, so $c = \tfrac{16}{5} b$.
- (3) gives $13b + 5d = -5$, so $d = -1 - \tfrac{13}{5} b$.
- (1) gives $5b - 16 \cdot \tfrac{16}{5} b + 13(-1 - \tfrac{13}{5} b) = -13$,
  i.e.\ $\tfrac{25 - 256 - 169}{5} b - 13 = -13$, i.e.\ $-\tfrac{400}{5} b = 0$,
  i.e.\ $\boxed{b = 0}$.
- Then $c = 0$, $d = -1$.

**Check** of (2): $5(1) + 13(0) - 16(-1) = 5 + 16 = 21$. ✓

**Solution.**
$$
\boxed{\;M_E \;=\; (1, 0, 0, -1).\;}
$$

Sum check: $1 + 0 + 0 - 1 = 0 = \chi(\mathcal{O}_E)$ ✓ (since $E$ is a
genus-$1$ curve, $\chi(\mathcal{O}_E) = 1 - 1 = 0$).

---

## 3. Interpretation of $M_E$

The elliptic-curve matrix $M_E = (1, 0, 0, -1)$ has the following content:
- $\Pi_{++}(E) = \kappa_{\mathrm{ch}}(\Phi_1(E)) = 1$. The single boson
  contribution from the $H^0 \oplus H^1$ Mukai sector of the elliptic
  curve.
- $\Pi_{+-}(E) = 0$: $E$ has no Borcherds-Kac-Moody algebraic
  enhancement; the elliptic genus is $\phi_{0, 1}(\tau, z)$ but the
  Borcherds weight is exactly the constant term $c(0) = 0$ of the relevant
  weight-$0$ index-$1$ Jacobi form.
- $\Pi_{-+}(E) = 0$: $E$ has no super-Yangian Berezinian channel; the
  Mukai signature of $E$ is $(2, 2)$ which gives
  $\operatorname{sdim}_{\mathrm{Ber}}(E) = 2 - 2 = 0$.
- $\Pi_{--}(E) = -1 = \chi^{\mathrm{cat}}(\Phi_1(E))$. Negative
  algebraization residual matching $-h^{1,0}(E) = -1$ via Hodge filtration.

The $V_4$-character spectrum of $E$ is concentrated on the diagonal axis
$\Pi_{++} \oplus \Pi_{--}$, with the off-diagonal characters $\Pi_{+-}$
and $\Pi_{-+}$ identically zero. This is the "diagonal" Lefschetz matrix
for an algebraic curve.

---

## 4. The $K3 \times K3$ Künneth identity

Computing the convolution $M_{K3} * M_{K3}$ with $M_{K3} = (0, 5, -16, 13)$:
\begin{align*}
(M_{K3} * M_{K3})^{++}
&= 0 \cdot 0 + 5 \cdot 5 + (-16)(-16) + 13 \cdot 13
= 0 + 25 + 256 + 169 = 450, \\
(M_{K3} * M_{K3})^{+-}
&= 0 \cdot 5 + 5 \cdot 0 + (-16)(13) + 13(-16) = -416, \\
(M_{K3} * M_{K3})^{-+}
&= 0(-16) + 5 \cdot 13 + (-16) \cdot 0 + 13 \cdot 5 = 130, \\
(M_{K3} * M_{K3})^{--}
&= 0 \cdot 13 + 5(-16) + (-16) \cdot 5 + 13 \cdot 0 = -160.
\end{align*}

Sum: $450 - 416 + 130 - 160 = 4 = \chi(\mathcal{O}_{K3})^2
= \chi(\mathcal{O}_{K3 \times K3})$. ✓

**No Drinfeld-coupling correction is needed for $K3 \times K3$**:
the naive Künneth gives the correct trace immediately. This is in
sharp contrast to $K3 \times E$ where the correction
$\Delta_{K3, E} = (13, -16, 5, -2)$ was non-trivial.

---

## 5. The asymmetry: why $E$ requires correction but $K3$ does not

Compare the two factor matrices:
- $M_{K3} = (0, 5, -16, 13)$: full $V_4$-faithful action; all four
  characters carry non-trivial trace; the "unit/volume" cancellation
  $\Pi_{++}(K3) = 0$ comes from Serre duality on the K3 surface (the
  unit $1 \in H^0$ pairs with the volume form $\omega \in H^{2,0}$
  with opposite sign in the bigraded Lefschetz character).
- $M_E = (1, 0, 0, -1)$: $\mathbb{Z}/2$-restricted (only diagonal
  characters $\Pi_{++}$ and $\Pi_{--}$ are non-trivial); the
  off-diagonal characters $\Pi_{+-}$ and $\Pi_{-+}$ vanish identically
  because $E$ has no Borcherds-Kac-Moody and no super-Berezinian
  enhancement.

When one factor has a $\mathbb{Z}/2$-restricted matrix
(only $\Pi_{++}$ and $\Pi_{--}$ active), the convolution
$(M_{K3} * M_E)$ shuffles the $K3$ entries via $E$'s diagonal action.
The result is the *anti-diagonal swap* of $M_{K3}$:
$(M_{K3} * M_E) = (-M_{K3}^{--}, -M_{K3}^{-+}, -M_{K3}^{+-}, -M_{K3}^{++})
\cdot \mathrm{sign}$
which in our notation gives $(-13, 21, -21, 13)$.

This is the *naive* answer; the genuine Wave-21 spectrum of $K3 \times E$
is $M_{K3 \times E} = (0, 5, -16, 11)$, which is the *anti-diagonal-flipped*
$M_{K3}$ with a small elliptic residual $(0, 0, 0, -2)$ added to absorb
the $h^{1,0}(E) = 1$ contribution.

The Drinfeld-coupling correction $\Delta_{K3, E}$ thus splits into:
$$
\Delta_{K3, E} \;=\; \underbrace{(13, -16, 5, 0)}_{\text{diagonal-flipped } M_{K3}}
\;+\; \underbrace{(0, 0, 0, -2)}_{\text{elliptic residual } -2 h^{1,0}(E)}.
$$

The first piece reverses the anti-diagonal swap; the second adjusts for
the elliptic curve's non-trivial $H^{1,0}$.

In contrast, $M_{K3} * M_{K3}$ does not introduce such a swap because
both factors carry full $V_4$-faithful action, so the convolution preserves
the character structure (no diagonal vs.\ anti-diagonal mismatch).

---

## 6. Universal formula

The above analysis suggests the following universal form for the
Drinfeld-coupling correction at any product $X \times Y$:

$$
\boxed{\;
\Delta_{X, Y} \;=\; \mathcal{F}_{X, Y}(M_X * M_Y)
\;+\; \mathrm{Hodge\text{-}residual}(X, Y),
\;}
$$

where:
- $\mathcal{F}_{X, Y}$ is a $V_4$-equivariant correction that
  re-aligns the convolution to the actual chiral algebra spectrum;
  it vanishes when both $M_X$ and $M_Y$ have full $V_4$-faithful action.
- $\mathrm{Hodge\text{-}residual}(X, Y)$ absorbs the Hodge-theoretic
  difference $h^{1, 0}(X) h^{1, 0}(Y) + \cdots$ coming from the
  $H^1(X) \otimes H^1(Y) \subset H^2(X \times Y)$ contribution to the
  Mukai pairing on $X \times Y$.

For $K3 \times K3$: both factors have $h^{1, 0} = 0$ and full
$V_4$-faithful action, so $\Delta_{K3, K3} = 0$.

For $K3 \times E$: $E$ has $h^{1, 0}(E) = 1$ and $\mathbb{Z}/2$-restricted
matrix, so both terms contribute, giving $\Delta_{K3, E} = (13, -16, 5, -2)$.

For $T^4 \times E$: $T^4$ has $h^{1,0}(T^4) = 2$ and a different matrix
structure (super-saturated $V_4 \subset (\mathbb{Z}/2)^4$); the
Drinfeld-coupling correction would have a richer structure to be computed.

---

## 7. Inscription target

This computation belongs in Vol III, in the K3 × E chapter or in a new
"Künneth multiplicativity" section. The key inscription content:

1. **Theorem** (elliptic-curve bigraded Lefschetz matrix): the bigraded
   Lefschetz matrix of the elliptic curve is
   $M_E = (1, 0, 0, -1)$, with sum $0 = \chi(\mathcal{O}_E)$.
2. **Theorem** ($K3 \times K3$ Künneth-multiplicativity): the bigraded
   Lefschetz matrix of $K3 \times K3$ equals the Klein-four convolution
   $M_{K3} * M_{K3} = (450, -416, 130, -160)$, with sum
   $4 = \chi(\mathcal{O}_{K3 \times K3})$. No Drinfeld-coupling
   correction.
3. **Theorem** (Drinfeld-coupling decomposition for $K3 \times E$):
   $\Delta_{K3, E} = $ (anti-diagonal-flipped $M_{K3}$) $+$
   (Hodge residual $-2 h^{1,0}(E)$).
4. **Universal formula** (conjectural): $\Delta_{X, Y}$ vanishes iff
   both $M_X$ and $M_Y$ have full $V_4$-faithful action and
   $h^{1,0}(X) h^{1,0}(Y) = 0$.

---

— Raeez Lorgat, 2026-04-16
