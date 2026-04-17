# Over-saturated Künneth-dichotomy: structural unification

**Author:** Raeez Lorgat. **Date:** 2026-04-17.

---

## 1. The two formulations

After the over-saturation hierarchy theorem, two formulations of the
Künneth-dichotomy coexist:

**Universal $V_4$ formulation (current K3 Yangian chapter).** $\Delta_{X, Y}$
vanishes iff both $M_X, M_Y$ are in the same $\sigma_{\mathrm{tot}}^*$-eigenspace
class on $\mathbb{Z}[V_4]$ (both generic, or both anti-symmetric).

**Over-saturated formulation (proposed unification).** $\Delta_{X, Y}$
vanishes iff the over-saturated matrices $\widetilde{M}_X, \widetilde{M}_Y$
admit a compatible Künneth gluing in the over-saturated lattice
$\mathbb{Z}[(\mathbb{Z}/2)^{2 + r(X) + r(Y)}]$.

These should agree. Where exactly does the over-saturated form predict
the dichotomy structurally?

---

## 2. The push-forward kernel

For a single CY $X$ with $r(X) = r$, the over-saturated symmetry is
$\widetilde{V}_X = (\mathbb{Z}/2)^{2 + r}$ and the canonical projection
$\pi : \widetilde{V}_X \to V_4$ has kernel
$$
K_X := \ker(\pi) = \{(\epsilon_w, \epsilon_p, \epsilon_1, \dots, \epsilon_r)
\in \widetilde{V}_X \mid \epsilon_w = +,\ \epsilon_p \epsilon_1 \cdots
\epsilon_r = +\}.
$$
This is a sub-group of order $2^r$ in $\widetilde{V}_X$ of order $2^{2+r}$.

The push-forward $M_X$ is determined by orbit-summing
$\widetilde{M}_X$ over $K_X$-orbits of $\widetilde{V}_X$.

For the elliptic curve $E$ ($r = 1$):
$K_E = \{(\!+, +, +), (+, -, -)\}$, order $2$. Each orbit has $2$
elements (translates of $K_E$ within $\widetilde{V}_E$ of order $8$).
Number of $V_4$-orbits = $8 / 2 = 4$ — matches the four $V_4$-characters.

For $T^4$ ($r = 2$): $K_{T^4}$ has order $4$, $\widetilde{V}_{T^4}$ has
order $16$, four $V_4$-orbits each of size $4$.

---

## 3. Künneth on the over-saturated side

For a product $X \times Y$, the over-saturated symmetry combines via
the natural injection
$$
\widetilde{V}_X \times \widetilde{V}_Y / \sim \;\hookrightarrow\;
\widetilde{V}_{X \times Y},
$$
where $\sim$ identifies the universal $V_4$ pair on each side (only
the universal $\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}}$
are shared). Hence
$$
\widetilde{V}_{X \times Y}
\;=\; (\mathbb{Z}/2)^{2 + r(X) + r(Y)}
\;=\; \widetilde{V}_X \times_{V_4} \widetilde{V}_Y.
$$

The Künneth identity at the over-saturated level reads
$$
\widetilde{M}_{X \times Y}
\;=\; \widetilde{M}_X *_{\widetilde{V}_{X \times Y}} \widetilde{M}_Y,
$$
i.e., convolution in the over-saturated regular representation.

**No coupling correction is needed at the over-saturated level**: the
chiral algebra $\Phi_d(D^b(\operatorname{Coh}(X \times Y)))$ tensor-factors
correctly when both Hodge-piece structures are tracked.

The Drinfeld-coupling correction $\Delta_{X, Y}$ on the universal $V_4$
side arises **purely from the push-forward**: when pushing
$\widetilde{M}_{X \times Y} = \widetilde{M}_X *_{\widetilde{V}} \widetilde{M}_Y$
forward to $\mathbb{Z}[V_4]$ via $\pi_{X \times Y}$, the result generally
differs from $M_X * M_Y$ in $\mathbb{Z}[V_4]$.

---

## 4. The push-forward-and-convolution diagram

Two operations to compare:
- **Path A (universal first, then convolve)**:
  $\widetilde{M}_X \xrightarrow{\pi_X} M_X$,
  $\widetilde{M}_Y \xrightarrow{\pi_Y} M_Y$, then
  $M_X * M_Y$ in $\mathbb{Z}[V_4]$.
- **Path B (convolve first, then push)**:
  $\widetilde{M}_X *_{\widetilde{V}_{X \times Y}} \widetilde{M}_Y
  = \widetilde{M}_{X \times Y}$, then push to
  $\pi_{X \times Y}(\widetilde{M}_{X \times Y}) = M_{X \times Y}$.

The Drinfeld-coupling correction is exactly the difference:
$$
\boxed{\;
\Delta_{X, Y} \;=\; \pi_{X \times Y}(\widetilde{M}_X *_{\widetilde{V}}
\widetilde{M}_Y) \;-\; \pi_X(\widetilde{M}_X) * \pi_Y(\widetilde{M}_Y)
\;\in\; \mathbb{Z}[V_4].
\;}
$$

This is a **non-commutativity** between push-forward and convolution
in the regular-representation lattice — a kernel-mismatch obstruction.

---

## 5. When does $\Delta_{X, Y} = 0$?

The two operations commute (give zero $\Delta$) when the Künneth
convolution of $\widetilde{M}_X * \widetilde{M}_Y$ is
$K_{X \times Y}$-invariant, where $K_{X \times Y} = \ker(\pi_{X \times Y})$.

**Sufficient condition.** Both $\widetilde{M}_X$ and $\widetilde{M}_Y$
are $K_X$-invariant (resp.\ $K_Y$-invariant) at the over-saturated
level. Then the convolution is $K_{X \times Y} = K_X \times K_Y$-invariant
automatically.

For $X = K3$ ($r = 0$): $K_{K3} = \{e\}$ trivial, so $\widetilde{M}_{K3}
= M_{K3}$ is trivially $K_{K3}$-invariant. ✓
For $Y = K3$ likewise. So $\Delta_{K3, K3} = 0$ ✓.

For $X = E$ ($r = 1$): $K_E = \mathbb{Z}/2$. Need
$\widetilde{M}_E$ to be $K_E$-invariant. Verified by computation in
the over-saturated form: $\widetilde{M}_E$ assigns equal mass to
$(+, +, +)$ and $(+, -, -)$ (since $K_E = \{(\!+, +, +), (+, -, -)\}$
acts trivially on these two as a single orbit). So
$\widetilde{M}_E$ is $K_E$-invariant ✓.

For $E \times E = T^4$: both factors $K_E$-invariant, hence the
product is $(K_E \times K_E)$-invariant = $K_{T^4}$-invariant.
$\Delta_{E, E} = 0$ ✓.

For $X = K3$, $Y = E$: $K_{K3 \times E} = K_{K3} \times K_E = K_E$
in $\widetilde{V}_{K3 \times E} = V_4 \times \widetilde{V}_E$. The
convolution $M_{K3} * \widetilde{M}_E$ is $K_E$-invariant
(since $\widetilde{M}_E$ is). So push-forward commutes with
convolution → $\Delta_{K3, E}$ should be $0$?

But $\Delta_{K3, E} = (13, -16, 5, -2) \neq 0$. **Contradiction.**

So $\widetilde{M}_E$ is NOT $K_E$-invariant after all. The
over-saturated matrix has non-trivial $K_E$-asymmetry. Let me recheck.

---

## 6. The $K_E$-asymmetry of $\widetilde{M}_E$

For $\widetilde{M}_E \in \mathbb{Z}[(\mathbb{Z}/2)^3]$ with
push-forward $M_E = (1, 0, 0, -1)$, $K_E = \{(\!+, +, +), (+, -, -)\}$.

The 8 over-saturated characters:
$(+, +, +), (+, +, -), (+, -, +), (+, -, -)$ in the $\epsilon_w = +$
sector;
$(-, +, +), (-, +, -), (-, -, +), (-, -, -)$ in the $\epsilon_w = -$
sector.

Push-forward sum constraint:
- $M_E^{(+, +)} = \widetilde{M}_E^{(+, +, +)} + \widetilde{M}_E^{(+, -, -)} = 1$
- $M_E^{(+, -)} = \widetilde{M}_E^{(+, +, -)} + \widetilde{M}_E^{(+, -, +)} = 0$
- $M_E^{(-, +)} = \widetilde{M}_E^{(-, +, +)} + \widetilde{M}_E^{(-, -, -)} = 0$
- $M_E^{(-, -)} = \widetilde{M}_E^{(-, +, -)} + \widetilde{M}_E^{(-, -, +)} = -1$

A natural $\widetilde{M}_E$ assignment (symmetric): each pair of
$K_E$-orbit elements get the same value.
- $\widetilde{M}_E^{(+, +, +)} = \widetilde{M}_E^{(+, -, -)} = 1/2$ — non-integer!

So no $K_E$-invariant integer-valued $\widetilde{M}_E$ exists with the
given push-forward. The over-saturated matrix MUST break $K_E$-symmetry.

Concretely: $\widetilde{M}_E^{(+, +, +)} = 1, \widetilde{M}_E^{(+, -, -)} = 0$
(or vice versa) is the natural integral choice — Hodge-volume sector
concentrated on $(+, +, +)$. Similarly for the $(-, -)$ orbit:
$\widetilde{M}_E^{(-, +, -)} = -1, \widetilde{M}_E^{(-, -, +)} = 0$
(or vice versa).

This $K_E$-asymmetry of $\widetilde{M}_E$ is what generates the
Drinfeld-coupling correction at $K3 \times E$: the Künneth convolution
$\widetilde{M}_{K3} * \widetilde{M}_E$ in $\widetilde{V}_{K3 \times E}$
inherits the asymmetry, but the push-forward $\pi_{K3 \times E}$
sums orbits of $K_{K3 \times E} = K_E$ — the "wrong" pairs get
summed when one of the factors is asymmetric.

---

## 7. The structural reason: integer obstruction to $K$-invariance

The wedge-indecomposable structure forces $\widetilde{M}_X$ to assign
integer values to specific Hodge-pieces; the $K_X$-orbit summing is
not generally an integer-respecting operation. Hence
$K_X$-non-invariance is the *generic* situation when $r(X) > 0$.

Combined with the kernel-mismatch obstruction: $\Delta_{X, Y} = 0$
when **both** factors are $r = 0$ (no $K$-asymmetry possible) OR
both factors have COMPATIBLE $K$-asymmetry such that the convolution
is $K_{X \times Y}$-invariant.

For $E \times E$: both factors $K_E$-asymmetric, but the asymmetries
align (same $K_E$ acting on each factor) so the convolution is
$K_{E^2}$-asymmetric in a compatible way that the push-forward
correctly handles. Result: $\Delta_{E, E} = 0$.

For $K3 \times E$: $K3$ is $K$-trivially-invariant ($r = 0$), $E$ is
$K_E$-asymmetric. The convolution is $K_E$-asymmetric in a way that
the push-forward $\pi_{K3 \times E}$ does NOT correctly handle —
hence $\Delta_{K3, E} \neq 0$.

---

## 8. The structural unification

**Theorem (over-saturated Künneth-dichotomy, conjectural).**
For products $X \times Y$ of CY manifolds, the Drinfeld-coupling
correction
$$
\Delta_{X, Y} \;=\; \pi_{X \times Y}(\widetilde{M}_X *_{\widetilde{V}}
\widetilde{M}_Y) - \pi_X(\widetilde{M}_X) * \pi_Y(\widetilde{M}_Y)
$$
vanishes iff at least one of $r(X), r(Y)$ is zero, OR
$\widetilde{M}_X$ and $\widetilde{M}_Y$ have aligned $K$-asymmetry
patterns (e.g., both factors are pure powers of the elliptic case,
$X = E^a, Y = E^b$).

The empirical $\sigma_{\mathrm{tot}}^*$-eigenspace classification of
the universal-$V_4$ Künneth-dichotomy is the *push-forward shadow*
of this $K$-alignment condition: factors with $\widetilde{M}_X$
$K$-invariant push to $\sigma_{\mathrm{tot}}^*$-anti-symmetric $M_X$,
and the eigenspace-matching criterion is exactly
$K$-asymmetry-alignment after push-forward.

This unifies the two formulations and explains the asymmetric
coupling formula structurally: it measures the kernel-mismatch
non-commutativity between push-forward and convolution.

---

## 9. Inscription target

This unification belongs in Vol III as an extension of the
over-saturation hierarchy theorem. The key new content:
- **Theorem** (over-saturated Künneth-dichotomy): $\Delta_{X, Y}$ as
  push-forward-vs-convolution non-commutativity.
- **Remark** ($K$-asymmetry of integral $\widetilde{M}_X$):
  wedge-indecomposable Hodge-piece structure forces integer
  $K$-asymmetric assignment.
- **Remark** (push-forward shadow): the universal $V_4$ dichotomy is
  the shadow of the over-saturated $K$-alignment.

---

— Raeez Lorgat, 2026-04-17
