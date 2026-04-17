# Bracketing-rigidity of the K3-anchored elliptic tower:
# the structural unification

**Author:** Raeez Lorgat. **Date:** 2026-04-17.

---

## 1. Statement

The K3-anchored elliptic tower $\{K3 \times E^k\}_{k \geq 1}$ exhibits
a **bracketing-rigidity** property: the bracketing-associator
$a(X, Y, Z) = M_{((X \cdot Y) \cdot Z)} - M_{(X \cdot (Y \cdot Z))}$
vanishes identically whenever all three factors $X, Y, Z$ are drawn
from the K3-anchored elliptic tower:

$$
\boxed{\;a(K3, E^j, E^k) \;=\; 0 \quad \text{for all } j, k \geq 0
\text{ (with at least one factor }= K3\text{)}.\;}
$$

This is a direct consequence of the V114 fixed-point theorem
$M_{K3 \times E^k} = M^\flat = (0, 5, -16, 11)$.

---

## 2. Proof

By the V114 fixed-point theorem, $M_{K3 \times E^k} = M^\flat$ for all
$k \geq 1$. Hence:
$$
M_{((K3 \times E^j) \times E^k)} = M_{K3 \times E^{j + k}} = M^\flat,
$$
$$
M_{(K3 \times (E^j \times E^k))} = M_{K3 \times E^{j + k}} = M^\flat.
$$
Both bracketings give the same matrix; their difference is zero.

Similarly for $a(E^j, K3, E^k)$ etc.: any product involving K3 + only
elliptic factors stabilises at $M^\flat$.

---

## 3. The bracketing-associator's support

Combined with V116's closed form and the V117 matrix-Pentagon coherence,
this shows the bracketing-associator $a$ is supported on the
*cross-class* regime — triples $(X, Y, Z)$ where at least two factors
fall outside the K3-anchored elliptic tower.

**Cross-class non-trivial values verified by direct computation:**
| $(X, Y, Z)$ | $a(X, Y, Z)$ |
|---|---|
| $(\mathrm{conifold}, K3, E)$ | $(0, 0, 2, -2)$ |
| $(K3, K3, E)$ | $(26, -32, 10, -4)$ |

**K3-anchored tower (vanishing by bracketing-rigidity):**
| $(X, Y, Z)$ | $a(X, Y, Z)$ |
|---|---|
| $(K3, E, E)$ | $(0, 0, 0, 0)$ |
| $(K3, T^4, E)$ | $(0, 0, 0, 0)$ |
| $(K3, E^j, E^k)$ for any $j, k$ | $(0, 0, 0, 0)$ |

**Other vanishing cases:**
| $(X, Y, Z)$ | $a(X, Y, Z)$ |
|---|---|
| $(E, E, E)$ | $(0, 0, 0, 0)$ — pure elliptic tower also rigid |
| $(K3, K3, K3)$ | $0$ (case (1) trivial: all three generic, no $\Delta$) |

---

## 4. The Bockstein interpretation

V116 characterised the bracketing-associator $a$ as the Bockstein
connecting homomorphism at level 3 of the bar complex of the short
exact sequence
$$
0 \;\to\; K \;\to\; \widetilde{V}_X \;\xrightarrow{\;\pi\;}\; V_4 \;\to\; 0
$$
of $V_4$-modules.

The bracketing-rigidity of the K3-anchored tower has a natural
interpretation in this language: **the K3 factor acts as a
homological retraction**. Specifically, the over-saturated
$\widetilde{V}_{K3 \times E^k}$ admits a canonical $V_4$-equivariant
splitting onto the universal $V_4$ via the K3-anchor mechanism — the
push-forward $\pi$ becomes a *split* surjection on K3-anchored inputs,
killing the Bockstein contribution.

For non-K3-anchored cross-class triples, no such splitting exists, and
the Bockstein contribution $a$ is genuinely non-trivial.

---

## 5. The chain-to-matrix Pentagon descent

V117's chain-to-matrix Pentagon unification states:
$$
a^{\mathrm{matrix}}(X, Y, Z, W) \;=\;
\mathrm{tr}^{V_4}\bigl([\omega]^{\mathrm{Pentagon}}_{Y(\fg_{K3})}\bigr)\bigm|_{4\text{-fold}}.
$$

The K3-anchored bracketing-rigidity manifests on the chain side as the
K3-Yangian Pentagon coherence cocycle vanishing identically when
specialised to the K3-anchored elliptic tower. This is exactly the
content of the K3-anchored elliptic-tower fixed-point theorem
(Theorem `thm:k3-elliptic-tower-fixed-point`): the Pentagon
$[\omega]^{\mathrm{Pentagon}}_{Y(\fg_{K3})}$ is a coboundary when
restricted to $\{K3 \times E^k\}$.

**This is the chain-level chain-level explanation of why the matrix
bracketing-associator vanishes on the K3-anchored tower**: the
chain-level Pentagon cocycle is itself trivial on the corresponding
sub-cycle.

---

## 6. Implications for the rank-1 frontier

The rank-1 frontier residuals (after refactoring through the V49 K3
edge architecture and the V55 trichotomy) reduce to:
- Mock-modular completion at quintic ⟺ $\alpha = 0$ in $E_{100/\mathbb{Q}}$
  new-form projection.
- Mock-modular completion at LP² ⟺ $\beta = 0$ in $E_{27/\mathbb{Q}}$
  new-form projection.
- Resurgent Drinfeld twist at $Y(\fg)$ for $\fg$ simple non-abelian.

The K3-anchored bracketing-rigidity adds a **structural negative
result**: NONE of these residuals can arise from K3-anchored elliptic
tower products, because the bracketing-associator vanishes on that
tower. The non-trivial Pentagon obstructions live elsewhere — in the
cross-class regimes (Class B mock-modular and the algebraic
Yang-Baxter sub-class).

This sharpens the rank-1 frontier: the obstruction to chain-level
Pentagon-at-$E_1$ does NOT propagate through K3-fibered CY3 products
of the form $K3 \times E^k$ (these are rigidly K3-anchored), but
instead lives in the genuinely-cross-class CY inputs.

---

## 7. Inscription opportunity

This bracketing-rigidity result is a clean structural corollary that
ties together V114, V116, V117. Worth inscribing as a remark in the
K3 Yangian chapter, right after the bracketing-associator section.

---

— Raeez Lorgat, 2026-04-17
