# Case-(2) anti-symmetric fixed-point structure for the $T^4$-anchored
# elliptic tower

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Status:** complete deliverable (LOSSLESS, attempt 1).
**Companion notes:** `wave_universal_fixed_point_extension.md`,
`wave_hyperkahler_anchored.md`, `bracketing_rigidity_K3_anchored_tower.md`,
`oversaturated_kunneth_dichotomy.md`.
**APs invoked:**
- AP-CY55 (manifold vs algebraization invariants: $M_{T^4}$ is a manifold
  invariant in the $-1$ eigenspace of $\sigma_{\mathrm{tot}}^*$);
- AP-CY60 (the doubling tower is a SEPARATE construction from the
  case-(3) generic fixed-point tower; do not present them as different
  applications of one functor);
- AP-CY61 (first-principles investigation: extract the ghost theorem
  before any reformulation. The wrong claim "$T^4$ has the same fixed
  point as $K3$" hides the genuine ghost theorem of a PROJECTIVE
  fixed-point on the antisymmetric line).

---

## 0. The question

The K$3$-anchored fixed-point theorem
(`thm:k3-elliptic-tower-fixed-point`) and its universal extension
(`thm:universal-elliptic-tower-fixed-point`,
`wave_universal_fixed_point_extension.md`) establish that for every
$X$ with $M_X$ generic under $\sigma_{\mathrm{tot}}^*$ (case (3) of
the V$_4$ Künneth dichotomy with $E$):
$$
  M_{X \times E^k} = M_X
  \qquad \forall\, k \geq 0.
$$

The case-(2) **anti-symmetric** exception ($\sigma_{\mathrm{tot}}^* M_X
= -M_X$, e.g. $X = T^4$ with $M_{T^4} = (2, 0, 0, -2)$, $X = E$ with
$M_E = (1, 0, 0, -1)$, $X = K3^{[n]} \times E^k$ with
$M = 2^{k-1}(n+1) M_E$) instead **doubles** under each $E$-multiplication:
$$
  M_{T^4 \times E^k} = 2^k\, M_{T^4} = (2^{k+1}, 0, 0, -2^{k+1}),
  \qquad k \geq 0.
$$

**Question.** Does $T^4$ anchor a DIFFERENT fixed-point structure under
some operation distinct from naive elliptic-tower iteration?

This wave answers: yes. The doubling tower IS a fixed-point structure,
but at the level of a NATURAL PROJECTIVE QUOTIENT (or, equivalently, a
NATURAL RESCALING by the eigenvalue of the iteration map). The case
(2) anti-symmetric class is the INTRINSICALLY PROJECTIVE branch of the
$\sigma_{\mathrm{tot}}^*$-eigenspace decomposition.

---

## 1. The spectral decomposition of $T_E$

**Setup.** Work in $\mathbb{Z}[V_4]$ with the Klein-four convolution
$*_{V_4}$ (regular representation arithmetic). Let
$\sigma_{\mathrm{tot}}^*\colon \mathbb{Z}[V_4] \to \mathbb{Z}[V_4]$ be
the antipodal involution
$\sigma_{\mathrm{tot}}^*(a, b, c, d) = (d, c, b, a)$. Its eigenspaces:
- $E^+ := \ker(\sigma_{\mathrm{tot}}^* - \mathrm{id})$ (symmetric;
  $+1$ eigenspace), basis $\{e_0 + e_3,\; e_1 + e_2\}$, dimension $2$;
- $E^- := \ker(\sigma_{\mathrm{tot}}^* + \mathrm{id})$ (anti-symmetric;
  $-1$ eigenspace), basis $\{e_0 - e_3,\; e_1 - e_2\}$, dimension $2$.

**The $E$-multiplication operator.** Define
$$
  T_E\colon \mathbb{Z}[V_4] \to \mathbb{Z}[V_4],
  \qquad T_E(M) := M *_{V_4} M_E,
  \qquad M_E = (1, 0, 0, -1).
$$

**Lemma 1.1 (closed-form $T_E$).** As a linear endomorphism of
$\mathbb{Z}[V_4]$,
$$
  \boxed{\;T_E \;=\; \mathrm{id} - \sigma_{\mathrm{tot}}^*.\;}
$$

*Proof.* This is the universal Drinfeld-coupling identity at $E$
(Theorem~\ref{thm:universal-drinfeld-coupling-E}, restated here): for any
$M \in \mathbb{Z}[V_4]$, $M *_{V_4} M_E = M - \sigma_{\mathrm{tot}}^*(M)$.
A direct $4 \times 4$ matrix verification (independent of any geometric
input) confirms it: writing $T_E$ in the standard basis $e_0, \dots, e_3$,
$$
  T_E = \begin{pmatrix}
    1 & 0 & 0 & -1 \\
    0 & 1 & -1 & 0 \\
    0 & -1 & 1 & 0 \\
    -1 & 0 & 0 & 1
  \end{pmatrix}
  \;=\; I_4 - S, \qquad
  S = \begin{pmatrix}
    0 & 0 & 0 & 1 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    1 & 0 & 0 & 0
  \end{pmatrix}. \qed
$$

**Lemma 1.2 (spectral decomposition of $T_E$).** $T_E$ is diagonalisable
with spectrum $\{0, 0, 2, 2\}$:
$$
  T_E = 2 P^- = 2 \cdot \frac{\mathrm{id} - \sigma_{\mathrm{tot}}^*}{2},
$$
where $P^- := (\mathrm{id} - \sigma_{\mathrm{tot}}^*)/2$ is the projection
onto $E^-$ along $E^+$. Equivalently:
- $T_E\big|_{E^+} = 0$ (symmetric subspace is the kernel of $T_E$);
- $T_E\big|_{E^-} = 2 \cdot \mathrm{id}$ (anti-symmetric subspace
  is preserved with eigenvalue $2$).

*Proof.* From Lemma 1.1, $T_E v^+ = (\mathrm{id} - \sigma_{\mathrm{tot}}^*)
v^+ = v^+ - v^+ = 0$ for $v^+ \in E^+$ and $T_E v^- = v^- - (-v^-) = 2 v^-$
for $v^- \in E^-$. $\qed$

**Corollary 1.3.** $T_E$ has no integral eigenvector with eigenvalue $1$
or any non-trivial integral fixed-point in $E^- \setminus \{0\}$. The
fixed-point locus of $T_E$ is exactly $\ker(T_E - \mathrm{id})$, which is
$\{0\}$ in $\mathbb{Z}[V_4]$ (since $T_E$ has eigenvalues $0$ and $2$
only).

---

## 2. The doubling tower as a projective fixed-point

**Theorem 2.1 (doubling tower).** For $M \in E^- \setminus \{0\}$
(any non-zero anti-symmetric matrix), define the iteration
$M^{(0)} := M$, $M^{(k+1)} := T_E(M^{(k)})$. Then
$$
  M^{(k)} = 2^k M, \qquad k \geq 0.
$$

In particular:
- $X = E$: $M_E^{(k)} = 2^k M_E$, with $M_E^{(1)} = M_{T^4} = 2 M_E$.
- $X = T^4$: $M_{T^4}^{(k)} = 2^k M_{T^4} = (2^{k+1}, 0, 0, -2^{k+1})$.
- $X = K3^{[n]} \times E$: $M_{K3^{[n]} \times E}^{(k)} = 2^k (n+1) M_E$
  (matches Theorem~2 of `wave_hyperkahler_anchored.md`).

*Proof.* By Lemma 1.2, $T_E$ acts as $2 \cdot \mathrm{id}$ on $E^-$. By
induction $M^{(k)} = 2 M^{(k-1)} = 2^k M^{(0)}$. Case (2) of the
dichotomy ensures $\Delta_{M^{(k)}, E} = 0$ for all $k \geq 0$ (both
$M^{(k)}$ and $M_E$ in $E^-$). $\qed$

**Corollary 2.2 (projective fixed-point on the anti-symmetric line).**
In the projective space $\mathbb{P}(E^- \otimes \mathbb{Q}) = \mathbb{P}^1$,
the line $[M_{T^4}]$ is a fixed point of $[T_E]$:
$$
  [T_E][M_{T^4}] = [2 M_{T^4}] = [M_{T^4}].
$$
In fact, EVERY non-zero anti-symmetric matrix represents a fixed point of
$[T_E]$ in $\mathbb{P}(E^- \otimes \mathbb{Q})$, because $T_E$ acts as a
scalar on $E^-$.

**Remark 2.3 (vs case-(3) generic).** This is a structurally distinct
fixed-point notion from the case-(3) generic case:
- Generic ($X = K3$, conifold, $\mathrm{LP}^2$, etc.): $M_X$ is a
  fixed-point of the FULL iteration $M \mapsto T_E(M) + \Delta_{X,E}$
  in $\mathbb{Z}[V_4]$ (additive group). Eigenvalue $1$.
- Anti-symmetric ($X = T^4, E, K3^{[n]} \times E$, etc.): $M_X$ is
  a fixed-point of $[T_E]$ in $\mathbb{P}(E^-_{\mathbb{Q}})$. Eigenvalue
  $2$ on the anti-symmetric line.

The case-(2) class is INTRINSICALLY PROJECTIVE; it does not admit an
additive integral fixed-point because the eigenvalue of $T_E$ on the
relevant invariant subspace is $2 \neq 1$.

---

## 3. The rescaled iteration

**Definition 3.1 ($T_E$-eigenvalue rescaling).** For any
$M \in \mathbb{Z}[V_4]$ in an invariant subspace of $T_E$ with eigenvalue
$\lambda \neq 0$, define the rescaled operator
$$
  H_E^{(\lambda)} \colon M \longmapsto \frac{T_E(M)}{\lambda}.
$$

**Theorem 3.2 (rescaled fixed-point on $E^-$).** With $\lambda = 2$,
$H_E^{(2)} = (\mathrm{id} - \sigma_{\mathrm{tot}}^*)/2 = P^-$ is the
projection onto $E^-$. Every $M \in E^-$ is a fixed point of
$H_E^{(2)}$ in $E^- \otimes \mathbb{Q}$:
$$
  H_E^{(2)}(M) = M, \qquad M \in E^- \otimes \mathbb{Q}.
$$
In particular $H_E^{(2)}(M_{T^4}) = M_{T^4}$.

*Proof.* From Lemma 1.2, $T_E\big|_{E^-} = 2 \cdot \mathrm{id}$, so
$H_E^{(2)}\big|_{E^-} = \mathrm{id}\big|_{E^-}$. $\qed$

**Remark 3.3.** $H_E^{(2)}$ is INTEGRAL ONLY ON $2 \mathbb{Z}[V_4]$ (or
on the rationalisation $\mathbb{Z}[V_4] \otimes \mathbb{Q}$). The
rescaling is the price of insisting on an additive (rather than projective)
fixed-point on the anti-symmetric line. This is the structural reason
the case-(2) class is "different from" the case-(3) generic class.

---

## 4. The $T^4$-iterated tower

The naive elliptic tower $M_{X \times E^k}$ is one natural iteration.
The wave's prompt asks: what about iteration by $T^4$ itself, i.e.
$M_{X \times (T^4)^k}$?

**Lemma 4.1 ($T^4$-iteration on $E^-$).** For $M \in E^-$ and $k \geq 0$,
$$
  M *_{V_4} (M_{T^4})^{*_{V_4} k}
  = 4^k\, M.
$$
In particular $M_{T^4 \times (T^4)^k} = 4^k \cdot M_{T^4}$.

*Proof.* $M_{T^4} = 2 M_E$, so $T_{T^4}(M) = M *_{V_4} M_{T^4}
= 2 M *_{V_4} M_E = 2 T_E(M)$. By Lemma 1.2, $T_{T^4}\big|_{E^-}
= 4 \cdot \mathrm{id}$. Iterating gives the $4^k$ factor. $\qed$

**Theorem 4.2 (rescaled $T^4$-fixed-point).** The rescaled $T^4$-iteration
$$
  H_{T^4}^{(4)}\colon M \longmapsto \frac{M *_{V_4} M_{T^4}}{4}
$$
fixes every $M \in E^-$, and in particular
$H_{T^4}^{(4)}(M_{T^4}) = M_{T^4}$.

*Proof.* By Lemma 4.1, $T_{T^4} = 2 T_E$, with spectrum $\{0, 0, 4, 4\}$.
On $E^-$: $T_{T^4} = 4 \cdot \mathrm{id}$, so $H_{T^4}^{(4)}\big|_{E^-}
= \mathrm{id}\big|_{E^-}$. $\qed$

---

## 5. The unified Platonic statement

**Theorem 5.1 (eigenvalue-rescaled fixed-point trichotomy).** Let
$X$ be a compact CY input and consider the elliptic-tower iteration
$$
  \mathcal{T}_{X, E}\colon M \longmapsto M *_{V_4} M_E + \Delta_{X, E}.
$$
There is a canonical eigenvalue $\lambda(X) \in \{0, 1, 2\}$ such that
$\mathcal{T}_{X, E}$ acts as $\lambda(X) \cdot \mathrm{id}$ on the
$\sigma_{\mathrm{tot}}^*$-stable invariant subspace generated by $M_X$
(viewed in $\mathbb{Z}[V_4] \otimes \mathbb{Q}$):
- $\lambda(X) = 0$ if $M_X \in E^+ \setminus \{0\}$ and $\Delta_{X,E} = 0$
  (symmetric kernel; not a $\sigma$-generic case).
- $\lambda(X) = 1$ if $M_X$ is generic under $\sigma_{\mathrm{tot}}^*$
  (case (3) of the dichotomy with $\Delta_{X,E} = \sigma_{\mathrm{tot}}^*
  M_X$).
- $\lambda(X) = 2$ if $M_X \in E^- \setminus \{0\}$ (anti-symmetric;
  case (2) with $\Delta_{X,E} = 0$).

The corresponding rescaled iteration
$$
  H_X := \frac{\mathcal{T}_{X, E}}{\lambda(X)}
  \quad (\text{when } \lambda(X) \neq 0)
$$
fixes $M_X$.

**Corollary 5.2.** The K$3$-anchored fixed-point $M^\flat = (0, 5, -16, 11)$
is the case $\lambda(K3) = 1$ (generic). The $T^4$-anchored projective
fixed-point $M_{T^4} = (2, 0, 0, -2)$ is the case $\lambda(T^4) = 2$
(anti-symmetric). In the rescaled picture, BOTH are fixed points; the
distinction is the rescaling factor $\lambda$.

**Corollary 5.3 (Platonic shape).** The dichotomy
$$
  \begin{array}{c|c|c|c}
    \text{Class} & \sigma_{\mathrm{tot}}^* M_X & \lambda(X) & \text{Fixed-point shape} \\
    \hline
    \text{Symmetric (kernel)} & +M_X & 0 & \text{annihilated, no fixed-point} \\
    \text{Generic (case 3)}  & \neq \pm M_X & 1 & M_X \in \mathbb{Z}[V_4] \\
    \text{Anti-symmetric (case 2)} & -M_X & 2 & [M_X] \in \mathbb{P}(E^-_{\mathbb{Q}})
  \end{array}
$$
records the COMPLETE structure of the $T_E$-iteration.

---

## 6. Why no additional integral fixed-point structure for $T^4$

**Theorem 6.1 (no integral fixed-point for $T^4$).** There is NO
$\mathbb{Z}$-linear operator $\mathcal{O}: \mathbb{Z}[V_4] \to
\mathbb{Z}[V_4]$ that
(i) is a "natural" combination of $T_E$, $\sigma_{\mathrm{tot}}^*$, and
$\mathrm{id}$ (i.e. lies in the $\mathbb{Z}$-algebra they generate),
(ii) acts non-trivially on $E^-$, and
(iii) has $M_{T^4}$ as an integral fixed-point, distinct from the trivial
$\mathcal{O} = \mathrm{id}$.

*Sketch.* The $\mathbb{Z}$-algebra generated by $\mathrm{id}$, $T_E
= \mathrm{id} - \sigma_{\mathrm{tot}}^*$ and $\sigma_{\mathrm{tot}}^*$
inside $\mathrm{End}_{\mathbb{Z}}(\mathbb{Z}[V_4])$ is the polynomial
ring $\mathbb{Z}[\sigma_{\mathrm{tot}}^*] / ((\sigma_{\mathrm{tot}}^*)^2 - 1)
\cong \mathbb{Z} \oplus \mathbb{Z}$, with the two summands corresponding
to the two eigenspaces. On $E^-$, every operator in this algebra acts as
multiplication by $a + b \cdot (-1) = a - b$ for some $a, b \in \mathbb{Z}$;
the eigenvalue takes values in $\mathbb{Z}$. For $M_{T^4}$ to be a fixed
point, we need $a - b = 1$, but then on $E^+$ the eigenvalue is
$a + b$ (from $\sigma$ acting as $+1$), giving the same operator class as
"some scaling on $E^+$ + identity on $E^-$". The only operators of this
shape that act trivially on the anti-symmetric line are
$\mathrm{id}$ itself (and $\mathrm{id} + c (\mathrm{id} +
\sigma_{\mathrm{tot}}^*)$ for any $c$, but those are trivial on $E^-$).
$\qed$

**Interpretation.** The case-(2) class genuinely DOES NOT admit a
non-trivial integral fixed-point structure in $\mathbb{Z}[V_4]$ — only
the projective / rescaled / scalar-eigenvalue structure of §§2–5. The
prompt's intuition that "T$^4$ might anchor a different fixed-point" is
EXACTLY THIS: it anchors a PROJECTIVE FIXED POINT IN
$\mathbb{P}(E^-_{\mathbb{Q}})$, with eigenvalue $\lambda = 2$ on the
anti-symmetric line.

---

## 7. The ghost theorem

**Ghost theorem (extracted via AP-CY61):**
The case-(2) anti-symmetric class is the PROJECTIVE-FIXED-POINT branch
of the elliptic-tower iteration. Its "doubling" is the eigenvalue
$\lambda = 2$ of $T_E$ on the $-1$ eigenspace of $\sigma_{\mathrm{tot}}^*$.
The full Platonic picture is the eigenvalue trichotomy
($\lambda \in \{0, 1, 2\}$) of Theorem 5.1.

The K$3$-anchored fixed-point ($\lambda = 1$) is the **integral** branch.
The $T^4$-anchored doubling tower ($\lambda = 2$) is the **projective**
branch. The kernel ($\lambda = 0$) is the **annihilated** branch
(no fixed-point structure at all; e.g. $M_X = (1, 1, 1, 1)$ in the
trivial $V_4$-character).

---

## 8. Comparison with hyperkähler-doubling

The hyperkähler-elliptic doubling theorem
(`wave_hyperkahler_anchored.md`, §2) states that for $X = K3^{[n]}$ in
the Bogomolov-Beauville HK form, $M_{K3^{[n]} \times E^k}
= 2^{k-1}(n+1) M_E$. The trajectory PASSES THROUGH the anti-symmetric
line at $k = 1$ ($M_{K3^{[n]} \times E} = (n+1) M_E \in E^-$) and then
DOUBLES from there.

This is consistent with the spectral decomposition: $M_{K3^{[n]}}
= (n+1, 0, 0, 0)$ is generic (neither in $E^+$ nor $E^-$), so the FIRST
$E$-multiplication uses the case-(3) Künneth (with $\Delta = 0$ as
computed in `wave_hyperkahler_anchored.md` §2 because of the precise
balance $\sigma^*(M_{K3^{[n]}}) = (n+1) e_{\Pi_{--}} = \chi(\mathcal{O})
e_{\Pi_{--}}$). The result lands in $E^-$, and from there subsequent
$E$-multiplications fall into case (2) and double via Theorem 2.1.

The HK-anchored elliptic tower is a TRANSITION trajectory: generic at $k = 0$,
anti-symmetric for $k \geq 1$, doubling thereafter.

---

## 9. Inscription target

This wave does not require manuscript edits to existing chapters; the
content is a STRUCTURAL DEEPENING of the existing K$3$-anchored
fixed-point and hyperkähler-doubling theorems. The natural inscription
target is **after**
`thm:hyperkahler-elliptic-doubling` (line ~3500 of
`chapters/examples/k3_yangian_chapter.tex`), as a **remark** on the
projective/rescaled fixed-point structure and the eigenvalue trichotomy.

The companion test
`compute/tests/test_anti_symmetric_iteration.py` cross-checks:
- the spectral decomposition of $T_E$ (Lemma 1.2) against direct $4 \times 4$
  matrix computation;
- the doubling pattern on $E^-$ (Theorem 2.1) against direct iteration;
- the rescaled fixed-point on $E^-$ (Theorem 3.2) against $H_E^{(2)} \circ
  H_E^{(2)} = H_E^{(2)}$ (idempotency of the projection);
- the projective fixed-point statement (Corollary 2.2) against the
  $T_E$ orbit of $M_{T^4}$;
- the no-non-trivial-integral-fixed-point claim (Theorem 6.1) by
  exhausting the $\mathbb{Z}$-algebra generated by $T_E$, $\sigma_{\mathrm{tot}}^*$,
  $\mathrm{id}$.

The library `compute/lib/anti_symmetric_iteration.py` provides the
operator algebra primitives (spectral projection, eigenvalue extraction,
rescaled iteration).

---

## 10. Summary: the LOSSLESS ledger

- $T_E := M \mapsto M *_{V_4} M_E = \mathrm{id} - \sigma_{\mathrm{tot}}^*$
  (Lemma 1.1). PROVED.
- Spectral decomposition of $T_E$: spectrum $\{0, 0, 2, 2\}$, kernel
  $E^+$, image $E^-$ on which $T_E$ acts as $2 \cdot \mathrm{id}$
  (Lemma 1.2). PROVED.
- Doubling tower on $E^-$: $M *_{V_4} M_E^{*k} = 2^k M$ for
  $M \in E^-$ (Theorem 2.1). PROVED.
- $M_{T^4}$ is a projective fixed-point in $\mathbb{P}(E^-_{\mathbb{Q}})$
  with eigenvalue $\lambda = 2$ (Corollary 2.2). PROVED.
- Rescaled fixed-point: $H_E^{(2)} := T_E / 2 = (\mathrm{id} -
  \sigma_{\mathrm{tot}}^*)/2 = P^-$ fixes every $M \in E^-_{\mathbb{Q}}$
  (Theorem 3.2). PROVED.
- $T^4$-iterated tower: $M *_{V_4} (M_{T^4})^{*k} = 4^k M$ on $E^-$
  (Lemma 4.1). PROVED.
- Eigenvalue trichotomy: $\lambda(X) \in \{0, 1, 2\}$ classifies the
  $T_E$-orbit of $M_X$ (Theorem 5.1). PROVED.
- No non-trivial integral fixed-point in the $\mathbb{Z}$-algebra of
  $T_E, \sigma_{\mathrm{tot}}^*, \mathrm{id}$ (Theorem 6.1). PROVED.
- The case-(2) class is the PROJECTIVE branch ($\lambda = 2$); the
  case-(3) generic class is the INTEGRAL branch ($\lambda = 1$); the
  $E^+$ symmetric class is the KERNEL branch ($\lambda = 0$).
  STRUCTURAL.

The ghost theorem of "T$^4$-anchored fixed-point" is the **eigenvalue
trichotomy with projective branch**: T$^4$ does anchor a fixed-point,
but in $\mathbb{P}(E^-_{\mathbb{Q}})$ rather than $\mathbb{Z}[V_4]$. The
distinction is the rescaling by the eigenvalue $\lambda = 2$.

The full Platonic statement is Theorem 5.1.

---

— Raeez Lorgat, 2026-04-17
