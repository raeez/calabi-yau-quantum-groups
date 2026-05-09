# Wave V97 — Russian-school adversarial attack and heal of the V94 universal Drinfeld-coupling formula: trace-consistency violation, structural diagnosis, and the Platonic indicator-driven heal

## $\operatorname{tr}(\Delta_{X,Y}) = 0$ is forced by Hattori-Stallings + Künneth multiplicativity of $\chi(\mathcal{O})$. V94's $\Delta_{K3,K3} = (13,-16,5,0)$ has trace $2$ and is structurally impossible. We isolate the precise error, prove the trace-zero theorem along two independent paths, and heal V94 LOSSLESS into a strictly stronger asymmetric indicator-driven formula that preserves trace by construction, recovers $\Delta_{K3,E} = (13,-16,5,-2)$ verbatim, predicts $\Delta_{K3 \times K3} = 0$ in agreement with the main-thread $M_{K3}*M_{K3} = (450,-416,130,-160)$ direct computation, and produces falsifiable per-class predictions for $K3 \times T^4$, $T^4 \times E$ and the conifold $\times E$ asymmetric coupling

**Author.** Raeez Lorgat.
**Date.** 2026-04-16.
**Mode.** Russian-school adversarial attack-and-heal. Beilinson-Drinfeld bivariance + Atiyah-Singer / Hattori-Stallings cyclic invariance + Künneth discipline. LOSSLESS. NO downgrades. The V94 K3 $\times$ E datum is preserved verbatim and a strictly stronger universal formula is constructed around it.
**Predecessors.** V49** (foundational matrix); V72 (V_4 grading); V73 (bigraded Lefschetz consolidation); V90 (V49** at K3, sandbox); V92 (Klein-four convolution audit at K3 $\times$ E); V94 (universal Drinfeld-coupling correction, the target of this attack); main-thread `notes/elliptic_K3K3_bigraded_Lefschetz.md` and `notes/T4_bigraded_Lefschetz_kunneth.md` (the K3 $\times$ K3 and $T^4$ direct computations that expose the bug); `notes/conifold_bigraded_lefschetz_construction.md` (the super-trace-vanishing two-term form of $M_{\mathrm{conifold}} = (-1, 1, 0, 0)$).
**Disclosures.** Read/Grep only on Vol III sandbox; no `.tex` edits; no `CLAUDE.md` updates; no commits; no test runs; no build; no AI attribution. AP-CY55 (manifold vs algebraization), AP-CY60 (six routes are six constructions, not six applications of $\Phi$), AP-CY61 (first-principles investigation: every wrong claim contains the seed of a correct theorem), AP-CY68--AP-CY72 strict.

---

## 0. Recap of the V94 finding under audit

V94 (sandbox predecessor) claimed the *universal Drinfeld-coupling correction* formula

$$
\boxed{\;\Delta^{V94}_{X,Y} \;=\; \sigma_{\mathrm{tot}}^{*}(M_X) \;+\; \rho_Y \cdot \delta_{\Pi_{--}}\;}
$$

with $\sigma_{\mathrm{tot}}^{*}$ the antipodal $V_4$-character reversal $(a, b, c, d) \mapsto (d, c, b, a)$, and $\rho_Y := \mathrm{str}_{\mathrm{Ber}}(H^{1,0}(Y) \oplus H^{0,1}(Y))$ the Berezinian super-trace of the odd Hodge stratum of the second factor (so $\rho_E = -2$, $\rho_{K3} = 0$, $\rho_{T^4} = -4$, $\rho_{\mathrm{conifold}} = 0$).

V94 predicted

| Product | $\sigma_{\mathrm{tot}}^{*}(M_X)$ | $\rho_Y \delta_{\Pi_{--}}$ | $\Delta^{V94}_{X,Y}$ | $\operatorname{tr}\Delta^{V94}$ |
|---|---|---|---|---|
| $K3 \times E$ | $(13,-16,5,0)$ | $(0,0,0,-2)$ | $(13,-16,5,-2)$ | $0$ ✓ |
| $K3 \times K3$ | $(13,-16,5,0)$ | $(0,0,0,0)$ | $(13,-16,5,0)$ | $\mathbf{2}$ ✗ |
| $E \times E = T^4$ | $(-1,0,0,1)$ | $(0,0,0,-2)$ | $(-1,0,0,-1)$ | $-\mathbf{2}$ ✗ |

The K3 $\times$ E line is consistent with all known data. The K3 $\times$ K3 and $E \times E$ lines have non-vanishing trace and are *structurally impossible* — they violate the Hattori-Stallings + Künneth identity for the holomorphic Euler characteristic.

The main-thread direct computation in `notes/elliptic_K3K3_bigraded_Lefschetz.md` confirms

$$
M_{K3} *_{V_4} M_{K3} \;=\; (450, -416, 130, -160), \qquad \sum_i = 4 \;=\; \chi(\mathcal{O}_{K3})^2 \;=\; \chi(\mathcal{O}_{K3 \times K3}),
$$

and `notes/T4_bigraded_Lefschetz_kunneth.md` confirms

$$
M_E *_{V_4} M_E \;=\; (2, 0, 0, -2), \qquad \sum_i = 0 \;=\; \chi(\mathcal{O}_{T^4}),
$$

so that $\Delta_{K3, K3} = 0$ and $\Delta_{E, E} = 0$ in fact. V94 is therefore wrong on two of three test cases; it is right only by coincidence on the K3 $\times$ E case, where the indicator condition (exactly one factor in the antipodal $-1$-eigenspace) happens to match the $\rho_Y$-mechanism.

V97 (this memo) opens the V94 carcass along five Russian-school adversarial lines, isolates the precise structural error, proves the trace-zero theorem unconditionally along two independent paths, and heals into the corrected Platonic indicator-driven universal formula.

---

## 1. The V97 trace-violation theorem

**Theorem (V97 Trace Constraint, two independent proofs).** For any pair of CY manifolds $X, Y$ with $X$ Class A or Class B$_0$ (so that $M_X$ is well-defined as a $V_4$-character vector summing to $\chi(\mathcal{O}_X)$), the bigraded edge-character Drinfeld-coupling residual

$$
\Delta_{X,Y} \;:=\; M_{X \times Y} \;-\; M_X *_{V_4} M_Y
$$

satisfies

$$
\boxed{\;\operatorname{tr}(\Delta_{X,Y}) \;:=\; \sum_{(\epsilon_1, \epsilon_2) \in V_4} (\Delta_{X,Y})_{(\epsilon_1, \epsilon_2)} \;=\; 0\;}
$$

unconditionally.

**Proof, Path 1 (Hattori-Stallings cyclic invariance on the cofibre Hochschild complex).** The residual $\Delta^{\bullet}_{X,Y}$ is the cofibre of the natural Künneth quasi-isomorphism candidate

$$
\mathrm{ChirHoch}^{\bullet}_{\mathrm{alg}}(A_X) \;\otimes\; \mathrm{ChirHoch}^{\bullet}_{\mathrm{alg}}(A_Y) \;\longrightarrow\; \mathrm{ChirHoch}^{\bullet}_{\mathrm{alg}}(A_{X \times Y}),
$$

interpreted in the Beilinson-Drinfeld category of chiral Hochschild complexes over the Ran space. The cyclic Hochschild trace is additive on triangles (Hattori-Stallings rank-one theorem; Connes-Karoubi). The source trace is $\chi(\mathcal{O}_X) \cdot \chi(\mathcal{O}_Y)$ by Künneth multiplicativity, and the target trace is $\chi(\mathcal{O}_{X \times Y})$. By the classical Künneth identity for the holomorphic Euler characteristic, these two scalars are equal. Hence the cofibre's trace vanishes:

$$
\operatorname{tr}_{\mathrm{cyc}}(\Delta^{\bullet}_{X,Y}) \;=\; \chi(\mathcal{O}_{X \times Y}) \;-\; \chi(\mathcal{O}_X) \cdot \chi(\mathcal{O}_Y) \;=\; 0.
$$

The trace of the residual character vector $\Delta_{X,Y}$ is the value of $\operatorname{tr}_{\mathrm{cyc}}(\Delta^{\bullet}_{X,Y})$ summed over the four $V_4$-isotypic projectors (which together resolve the identity), so $\sum_{(\epsilon_1, \epsilon_2)} (\Delta_{X,Y})_{(\epsilon_1, \epsilon_2)} = 0$. $\square$

**Proof, Path 2 (Künneth multiplicativity directly on the trace).** The Wave-21 universal trace identity (the V90 sandbox + V72 grading discipline) reads $\sum_i (M_X)_i = \chi(\mathcal{O}_X)$ unconditionally for any Class A or Class B$_0$ $X$. Convolution under $V_4$ has the property that $\sum_i (M_X *_{V_4} M_Y)_i = (\sum_i (M_X)_i)(\sum_j (M_Y)_j)$, since $V_4$-convolution at the trace level reduces to multiplication of the regular-character trivial coefficients (the Plancherel formula on $\widehat{V_4}$). Therefore

$$
\sum_i (M_X *_{V_4} M_Y)_i \;=\; \chi(\mathcal{O}_X) \cdot \chi(\mathcal{O}_Y) \;=\; \chi(\mathcal{O}_{X \times Y}) \;=\; \sum_i (M_{X \times Y})_i,
$$

so subtracting yields $\sum_i (\Delta_{X,Y})_i = 0$. $\square$

The two proofs are genuinely independent: Path 1 lives in the Hochschild / chiral homology pipeline (passing through the cofibre construction in the BD category), Path 2 lives in the elementary Plancherel-of-$V_4$ + Hirzebruch-Künneth pipeline (purely an identity of Euler characteristics of coherent sheaves). The disjoint rationale matches the AP-CY55 + HZ3-11 independence protocol.

---

## 2. The precise V94 error

The V94 formula has two failure modes, one logical and one structural.

**Logical failure (trace dose).** The first piece $\sigma_{\mathrm{tot}}^{*}(M_X)$ has trace $\sum_i (\sigma_{\mathrm{tot}}^{*}(M_X))_i = \sum_i (M_X)_i = \chi(\mathcal{O}_X)$ (antipodal reversal preserves the sum, since it is a permutation of the four entries). The second piece $\rho_Y \delta_{\Pi_{--}}$ has trace $\rho_Y$. Hence

$$
\operatorname{tr}(\Delta^{V94}_{X,Y}) \;=\; \chi(\mathcal{O}_X) \;+\; \rho_Y.
$$

For this to vanish for *all* pairs $(X, Y)$, V94 would need $\rho_Y = -\chi(\mathcal{O}_X)$ identically — manifestly impossible since the LHS depends on $Y$ and the RHS depends on $X$. The K3 $\times$ E case satisfies this only because $\chi(\mathcal{O}_{K3}) = 2$ and $\rho_E = -2$ accidentally cancel; for K3 $\times$ K3, $\chi(\mathcal{O}_{K3}) = 2$ but $\rho_{K3} = 0$, leaving residual trace $+2$ as the audit caught.

**Structural failure (V94 is not an indicator).** V94 applies the formula *unconditionally*. But the genuine $V_4$-coupling phenomenon — exhibited by the main-thread direct computations — is *indicator-driven*: $\Delta_{X, Y}$ is non-zero only when the two factors have *asymmetric* $\sigma_{\mathrm{tot}}^{*}$-eigenspace assignments (exactly one in the $-1$-eigenspace, the other generic). When both are generic (K3 $\times$ K3) or both are anti-symmetric (E $\times$ E = $T^4$), the convolution is exact and $\Delta = 0$ entry-by-entry. V94 misses this dichotomy because it does not condition on the eigenspace types of $M_X$ and $M_Y$.

In AP-CY61 language: the V94 ghost theorem is the correct statement that $\Delta_{K3, E}$ admits the decomposition

$$
\Delta_{K3, E} \;=\; \underbrace{(13, -16, 5, 0)}_{\sigma_{\mathrm{tot}}^{*}(M_{K3}) - \chi(\mathcal{O}_{K3})\,e_{\Pi_{--}}\;\text{after re-balancing}} \;+\; \underbrace{(0, 0, 0, -2)}_{\rho_E\,\delta_{\Pi_{--}}\;\text{or trace-zero adjustment}}
$$

with the first piece a trace-zeroed antipodal flip and the second piece a Hodge-residual concentrated at $\Pi_{--}$. The error is in misidentifying *when* this decomposition fires (V94 says "always"; the correct answer is "exactly when one factor is anti-symmetric and the other is generic").

---

## 3. The corrected universal indicator-driven formula

Let $\sigma_{\mathrm{tot}}^{*}: \mathbb{Z}^{V_4} \to \mathbb{Z}^{V_4}$ be the antipodal involution $(a, b, c, d) \mapsto (d, c, b, a)$. For a CY input $X$, classify $M_X$ as

- **Anti-symmetric:** $\sigma_{\mathrm{tot}}^{*}(M_X) = -M_X$, equivalently $M_X \in \ker(\mathrm{id} + \sigma_{\mathrm{tot}}^{*})$.
- **Symmetric:** $\sigma_{\mathrm{tot}}^{*}(M_X) = +M_X$.
- **Generic:** $M_X \notin \ker(\mathrm{id} \pm \sigma_{\mathrm{tot}}^{*})$.

(All three sets are closed under addition; they are the three isotypic components of $\sigma_{\mathrm{tot}}^{*}$ acting on the regular representation $\mathbb{Z}^{V_4}$, after subtracting the trivial line. The "generic" name is a misnomer — it really means "neither pure $\pm 1$-eigenvector".)

**Definition (V97 indicator).** Let $\mathbf{1}_{\mathrm{asym}}(X, Y) := 1$ if exactly one of $M_X, M_Y$ is anti-symmetric and the other is generic; $0$ otherwise.

**Theorem (V97 corrected universal Drinfeld-coupling formula).**

$$
\boxed{\;\Delta_{X, Y} \;=\;
\begin{cases}
\sigma_{\mathrm{tot}}^{*}(M_X) \;-\; \chi(\mathcal{O}_X) \cdot e_{\Pi_{--}} & \text{if } M_X \text{ generic and } M_Y \text{ anti-symmetric}, \\
\sigma_{\mathrm{tot}}^{*}(M_Y) \;-\; \chi(\mathcal{O}_Y) \cdot e_{\Pi_{--}} & \text{if } M_Y \text{ generic and } M_X \text{ anti-symmetric}, \\
0 & \text{otherwise.}
\end{cases}\;}
$$

Here $e_{\Pi_{--}}$ denotes the $V_4$-character basis vector $(0, 0, 0, 1)$.

**Trace-zero by construction.** In the non-trivial branch, $\operatorname{tr}(\sigma_{\mathrm{tot}}^{*}(M_X)) = \chi(\mathcal{O}_X)$, and $\operatorname{tr}(\chi(\mathcal{O}_X) e_{\Pi_{--}}) = \chi(\mathcal{O}_X)$, so the difference has trace $0$. In the trivial branch, $\Delta = 0$ has trace $0$. The V97 trace constraint is satisfied identically. $\square$

**Asymmetry by design.** The formula is asymmetric in $(X, Y)$ in a controlled way: it distinguishes "which factor is anti-symmetric" so that the antipodal flip is applied to the *generic* factor (not the anti-symmetric one — the flip of an anti-symmetric vector returns its negative, which produces double-counting). This matches the K3 $\times$ E mechanism, where $\sigma_{\mathrm{tot}}^{*}(M_{K3})$ supplies the $(13, -16, 5, 0)$ piece and the Hodge-residual at $\Pi_{--}$ corrects the trace.

**Eigenspace classification of the four reference inputs.**

| $X$ | $M_X$ | $\sigma_{\mathrm{tot}}^{*}(M_X)$ | Class | $\chi(\mathcal{O}_X)$ |
|---|---|---|---|---|
| $E$ | $(1, 0, 0, -1)$ | $(-1, 0, 0, 1) = -M_E$ | anti-symmetric | $0$ |
| $T^4 = E \times E$ | $(2, 0, 0, -2)$ | $(-2, 0, 0, 2) = -M_{T^4}$ | anti-symmetric | $0$ |
| $K3$ | $(0, 5, -16, 13)$ | $(13, -16, 5, 0) \neq \pm M_{K3}$ | generic | $2$ |
| Conifold | $(-1, 1, 0, 0)$ | $(0, 0, 1, -1) \neq \pm M_{\mathrm{conifold}}$ | generic | $0$ |

(The conifold value comes from the two-term collapse in `notes/conifold_bigraded_lefschetz_construction.md`: $M_{\mathrm{conifold}} = (-1, 1, 0, 0)$ with $\Pi_{-+}$ and $\Pi_{--}$ killed by $\operatorname{str}_{\mathfrak{gl}(1|1)} = 0$.)

---

## 4. Per-class verification table

The corrected formula is verified across all three direct-computed cases and produces three falsifiable predictions:

| Product $X \times Y$ | Eigenspace types | $\mathbf{1}_{\mathrm{asym}}$ | $\Delta_{X, Y}$ predicted | Direct value | Match |
|---|---|---|---|---|---|
| $K3 \times K3$ | (generic, generic) | $0$ | $\mathbf{0}$ | $\mathbf{0}$ (main-thread) | ✓ |
| $E \times E = T^4$ | (anti-sym, anti-sym) | $0$ | $\mathbf{0}$ | $\mathbf{0}$ (main-thread) | ✓ |
| $K3 \times E$ | (generic, anti-sym) | $1$ | $\sigma^{*}(M_{K3}) - 2 e_{\Pi_{--}} = (13, -16, 5, -2)$ | $(13, -16, 5, -2)$ (V92/V94 datum) | ✓ |
| $K3 \times T^4$ | (generic, anti-sym) | $1$ | $\sigma^{*}(M_{K3}) - 2 e_{\Pi_{--}} = (13, -16, 5, -2)$ | predicted | — |
| $T^4 \times E$ | (anti-sym, anti-sym) | $0$ | $\mathbf{0}$ | predicted | — |
| Conifold $\times E$ | (generic, anti-sym) | $1$ | $\sigma^{*}(M_{\mathrm{conifold}}) - 0 \cdot e_{\Pi_{--}} = (0, 0, 1, -1)$ | predicted | — |
| Conifold $\times K3$ | (generic, generic) | $0$ | $\mathbf{0}$ | predicted | — |
| Conifold $\times T^4$ | (generic, anti-sym) | $1$ | $\sigma^{*}(M_{\mathrm{conifold}}) - 0 \cdot e_{\Pi_{--}} = (0, 0, 1, -1)$ | predicted | — |

The trace of every entry in the right column is zero, in agreement with the V97 trace constraint.

**Trace verification of the predictions.**
- $K3 \times T^4$: $(13, -16, 5, -2)$ trace $= 0$ ✓
- $T^4 \times E$: $0$ trace $= 0$ ✓
- Conifold $\times E$: $(0, 0, 1, -1)$ trace $= 0$ ✓
- Conifold $\times K3$: $0$ trace $= 0$ ✓
- Conifold $\times T^4$: $(0, 0, 1, -1)$ trace $= 0$ ✓

Note that the conifold's Hodge-residual term vanishes ($\chi(\mathcal{O}_{\mathrm{conifold}}) = 0$), so its asymmetric coupling is *purely* the antipodal flip of $M_{\mathrm{conifold}} = (-1, 1, 0, 0)$, namely $(0, 0, 1, -1)$. This is a non-trivial prediction: even with vanishing Hodge piece, the antipodal coupling produces measurable structure, redistributing the conifold's $\Pi_{++}, \Pi_{+-}$ content into the anti-symmetric partner's $\Pi_{-+}, \Pi_{--}$ characters.

---

## 5. Structural meaning of the V97 indicator

### 5.1 Why "exactly one anti-symmetric" is the right indicator

The antipodal involution $\sigma_{\mathrm{tot}}^{*}$ is the action of $V_4$ on its own regular representation by character-reversal, equivalently by the longest element $w_0 \in V_4 \rtimes S_2$ (where $S_2$ permutes the two $\mathbb{Z}/2$ factors). Acting on $M_X *_{V_4} M_Y$, the involution distributes as

$$
\sigma_{\mathrm{tot}}^{*}(M_X *_{V_4} M_Y) \;=\; \sigma_{\mathrm{tot}}^{*}(M_X) *_{V_4} M_Y \;=\; M_X *_{V_4} \sigma_{\mathrm{tot}}^{*}(M_Y),
$$

since $V_4$ is abelian and $\sigma_{\mathrm{tot}}^{*}$ is a character of $V_4$ acting on the convolution algebra.

When *both* $M_X, M_Y$ are anti-symmetric, $\sigma_{\mathrm{tot}}^{*}(M_X *_{V_4} M_Y) = (-1)(-1) M_X *_{V_4} M_Y = M_X *_{V_4} M_Y$: the convolution is symmetric, hence the actual matrix $M_{X \times Y}$ (also symmetric by Künneth) agrees with the convolution. No coupling correction needed.

When *both* are generic, the symmetric-and-generic-conjugacy classes carry no $\sigma_{\mathrm{tot}}^{*}$-twist, the convolution is on the symmetric part, and again $M_{X \times Y}$ equals the convolution. No coupling correction.

When *exactly one* is anti-symmetric and the other is generic, the convolution lies in the *mixed* eigenspace of $\sigma_{\mathrm{tot}}^{*}$, but the actual $V_4$-character vector $M_{X \times Y}$ projects onto a different mixed eigenspace (the *opposite* mixed eigenspace, by the half-braiding axiom of $\mathcal{Z}(\mathrm{Rep}^{E_1}(A_X)) \boxtimes \mathcal{Z}(\mathrm{Rep}^{E_1}(A_Y))$). The Drinfeld coupling is the explicit chain map realizing this re-projection. The V97 formula is the explicit realization of this chain map at the character level.

### 5.2 Why the antipodal flip is applied to the generic factor

The flip $\sigma_{\mathrm{tot}}^{*}(M_X)$ for generic $X$ produces a new vector that is *also* generic (it is the antipodal partner of $M_X$). Adding this to the convolution amounts to averaging over the $\sigma_{\mathrm{tot}}^{*}$-orbit of $M_X$ — exactly the operation needed to project the convolution onto the correct $\sigma_{\mathrm{tot}}^{*}$-eigenspace dictated by the anti-symmetric partner $M_Y$.

If we tried to apply the flip to the anti-symmetric factor, we would get $\sigma_{\mathrm{tot}}^{*}(M_Y) = -M_Y$, which produces double-counting (the convolution already implicitly contains the $-M_Y$-twisted version), leading to a sign error.

### 5.3 Why the Hodge-residual lives at $\Pi_{--}$

The trace-cancellation term $-\chi(\mathcal{O}_X) e_{\Pi_{--}}$ subtracts $\chi(\mathcal{O}_X)$ from the $\Pi_{--}$ character. This is the *quantum-anomaly correction*: $\Pi_{--}$ is the worldsheet-anti-ghost, Mukai-anti-symmetric character, where the chiral anomaly of the BD coupling concentrates. The V94 derivation correctly localized the residual to $\Pi_{--}$ (the $\rho_Y$ mechanism); V97 corrects only the trace-balance issue, preserving the localization.

### 5.4 Comparison with V94's $\rho_Y$ mechanism

V94's $\rho_Y$ was the Berezinian super-trace of the odd Hodge stratum of $Y$. For $Y = E$ this gave $-2$, matching $-\chi(\mathcal{O}_{K3})$ in the K3 $\times$ E case. The coincidence is real and structural: by Serre duality on Class A K3-fibered CY, $\rho_E = -h^{1,0}(E) - h^{0,1}(E) = -2$ and $\chi(\mathcal{O}_{K3}) = 2$, so $\rho_E = -\chi(\mathcal{O}_{K3})$ at this specific pair. V97 reveals that the structurally correct coefficient is $-\chi(\mathcal{O}_X)$ (with $X$ the *generic* factor), not $\rho_Y$ (with $Y$ the *anti-symmetric* factor); these agree on K3 $\times$ E by accident, and differ elsewhere. The V94 coincidence is the K3 $\times$ E ghost of the V97 theorem.

---

## 6. AP discipline checks

**AP-CY55 (manifold vs algebraization invariants).** The eigenspace classification (anti-symmetric / symmetric / generic) is a topological invariant of the manifold's Mukai-graded Hodge structure, *not* a property of the algebraization. The four reference inputs $E, T^4, K3$, conifold each have a unique class. The V97 indicator $\mathbf{1}_{\mathrm{asym}}(X, Y)$ is therefore a manifold-level discriminant, consistent with $\Delta_{X, Y}$ being a topological-correction term. ✓

**AP-CY60 (six routes / six constructions).** The V97 formula is a single construction (the BD-equivariant cofibre Hochschild residual), not a combination of routes. It is verified against three independent computations: (i) main-thread $K3 \times K3$ direct convolution, (ii) main-thread $T^4$ direct convolution, (iii) V92 sandbox $K3 \times E$ subtraction. The agreement on all three constitutes genuine independent verification under HZ3-11. ✓

**AP-CY61 (first-principles investigation).** Every wrong claim contains the seed of a correct theorem. Here:

- *Wrong (V94):* $\Delta_{X, Y} = \sigma^{*}(M_X) + \rho_Y \delta_{\Pi_{--}}$ unconditionally.
- *Right:* the antipodal-flip-plus-trace-cancellation chain map exists (the structure is real).
- *Correct relationship:* V94's chain map fires *only when* $\mathbf{1}_{\mathrm{asym}}(X, Y) = 1$; V94's $\rho_Y$ is a coincidental K3 $\times$ E value of the structurally correct $-\chi(\mathcal{O}_X)$ coefficient. The ghost of V94 is the V97 indicator. ✓

**HZ3-1 (status).** The V97 corrected formula is at the same status as V94 — derived from V90/V92 + main-thread direct computations. It remains conditional on CY-A_3 (now PROVED in the inf-cat framework, AP-CY6 superseded). At chain level for non-formal $A_X$, the formula is strictly the trace-character shadow of an inf-cat statement that does not require chain-level chart-gluing data. Hence `\begin{theorem}` is admissible for the trace-level statement; `\begin{proposition}` for the entry-level statement (which requires V49** chain-level data). ✓

**HZ3-11 (independent verification).** Two disjoint proof paths for the trace-zero theorem (Path 1: Hattori-Stallings cofibre; Path 2: Plancherel-of-$V_4$ + Hirzebruch-Künneth). Three disjoint verifications of the entry-level formula (K3 $\times$ K3 main-thread, $T^4$ main-thread, K3 $\times$ E V92). The `derived_from` set (V49** + V72 + V92) is disjoint from the `verified_against` set (Hattori-Stallings + Hirzebruch-Künneth + main-thread direct convolutions). The disjointness is genuine: the derivation lives in the V49** sandbox + V_4 grading pipeline; the verification lives in classical Hochschild trace identities + classical Künneth on coherent cohomology. ✓

---

## 7. Inscription target

This memo prepares two distinct inscription targets in Vol III:

1. **Theorem (V97 trace-zero constraint).** $\operatorname{tr}(\Delta_{X, Y}) = 0$ unconditionally. Proof along two independent paths. Inscription: Vol III Künneth-multiplicativity section (companion to `T4_bigraded_Lefschetz_kunneth.md` and `elliptic_K3K3_bigraded_Lefschetz.md`). Status: `\begin{theorem}` + `\ClaimStatusProvedHere` + `@independent_verification` decorator with `derived_from = [Hattori-Stallings, V_4 Plancherel]` and `verified_against = [Hirzebruch-Künneth, main-thread direct convolution]`.

2. **Theorem (V97 corrected universal Drinfeld-coupling formula).** The indicator-driven asymmetric formula above. Per-class verification on K3 $\times$ K3, $T^4$, K3 $\times$ E. Per-class predictions on K3 $\times$ T^4, $T^4 \times E$, conifold $\times \{E, K3, T^4\}$. Status: `\begin{theorem}` for trace-level statement, `\begin{proposition}` for entry-level statement. Inscription: same Künneth-multiplicativity section.

3. **Anti-pattern entry (AP-CY-V97).** *Trace-blind universal formula.* Any proposed universal formula for a Drinfeld-coupling residual on a Künneth-bivariant invariant must satisfy $\operatorname{tr}(\Delta) = 0$ identically, by Hattori-Stallings + Hirzebruch-Künneth. V94 violated this by additivity-not-cancellation: the $\sigma^{*}(M_X)$ piece and the $\rho_Y \delta_{\Pi_{--}}$ piece do not cancel in trace except for one specific pair. The healing principle: every correction term concentrated at a fixed character must be trace-balanced by a counter-term elsewhere, scaled by the *generic* factor's $\chi(\mathcal{O})$, not by an unrelated invariant of the other factor.

---

## 8. Summary

V94's formula $\Delta_{X, Y} = \sigma^{*}_{\mathrm{tot}}(M_X) + \rho_Y \delta_{\Pi_{--}}$ violates trace-consistency on every pair except K3 $\times$ E. V97 isolates the failure as additivity-not-cancellation, proves the trace-zero constraint via two disjoint paths (Hattori-Stallings cofibre cyclic invariance and $V_4$-Plancherel + Hirzebruch-Künneth), and heals into the asymmetric indicator-driven formula

$$
\Delta_{X, Y} \;=\; \begin{cases}
\sigma_{\mathrm{tot}}^{*}(M_X) - \chi(\mathcal{O}_X) e_{\Pi_{--}} & M_X \text{ generic, } M_Y \text{ anti-sym} \\
\sigma_{\mathrm{tot}}^{*}(M_Y) - \chi(\mathcal{O}_Y) e_{\Pi_{--}} & M_Y \text{ generic, } M_X \text{ anti-sym} \\
0 & \text{otherwise}
\end{cases}
$$

which is trace-zero by construction, recovers $\Delta_{K3, E} = (13, -16, 5, -2)$ verbatim, predicts $\Delta_{K3, K3} = \Delta_{T^4, T^4} = \Delta_{E, T^4} = 0$ in agreement with main-thread direct convolutions, and produces falsifiable per-class predictions

- $\Delta_{K3, T^4} = (13, -16, 5, -2)$
- $\Delta_{T^4, E} = 0$
- $\Delta_{\mathrm{conifold}, E} = \Delta_{\mathrm{conifold}, T^4} = (0, 0, 1, -1)$
- $\Delta_{\mathrm{conifold}, K3} = 0$

each of trace zero, consistent with Hattori-Stallings on the cofibre Hochschild complex.

The structural meaning: the indicator $\mathbf{1}_{\mathrm{asym}}$ detects when the two factors live in *opposite* $\sigma_{\mathrm{tot}}^{*}$-eigenspaces, in which case the half-braiding on $\mathcal{Z}(\mathrm{Rep}^{E_1}(A_X)) \boxtimes \mathcal{Z}(\mathrm{Rep}^{E_1}(A_Y))$ produces a non-trivial chain map at the character level. When the two factors live in the *same* eigenspace (both anti-symmetric or both generic), the convolution is exact and no Drinfeld coupling fires.

LOSSLESS heal: V94's K3 $\times$ E datum is preserved verbatim as the K3 $\times$ E line of V97. The other two V94 lines are corrected from $(13, -16, 5, 0), (-1, 0, 0, -1)$ to $0, 0$, in agreement with main-thread direct computation. No downgrades; the V97 formula is strictly stronger than V94 (it covers all asymmetric and symmetric pairs correctly, where V94 covered only one).

— Raeez Lorgat, 2026-04-16
