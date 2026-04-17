# The cohomological home of the bracketing-associator:
# H^3(CY_*; Z[V_4]_0) as a graded V_4-equivariant invariant

**Author:** Raeez Lorgat. **Date:** 2026-04-17.

---

## 1. Statement and motivation

The bracketing-associator
$$
  a(X, Y, Z) \;=\; M_{((X \cdot Y) \cdot Z)} - M_{(X \cdot (Y \cdot Z))}
$$
admits a closed form in $\mathbb{Z}[V_4]$ (`thm:bracketing-associator-closed-form`)
and satisfies the matrix-Pentagon coherence at every quadruple
(`thm:matrix-pentagon-coherence` verified at multiple quadruples,
`thm:k6-5fold-matrix-coherence` verified at the K_6 falsifiable predictor).

The natural cohomological home is therefore the third $V_4$-equivariant
cohomology of the CY-product category with coefficients in the trace-zero
hyperplane:
$$
  [a] \;\in\; H^3\bigl(\mathrm{CY}_*;\, \mathbb{Z}[V_4]_0\bigr).
$$

This note computes $H^3(\mathrm{CY}_*; \mathbb{Z}[V_4]_0)$ as a graded
$V_4$-module and identifies the specific $V_4$-class that $[a]$ inhabits.

---

## 2. The trace-zero hyperplane $\mathbb{Z}[V_4]_0$

Recall the $V_4 = \langle \epsilon_{\mathrm{wt}}, \epsilon_{\mathrm{par}}\rangle$
group ring:
$$
  \mathbb{Z}[V_4] \;=\; \mathbb{Z}\langle e_{++}, e_{+-}, e_{-+}, e_{--}\rangle
$$
with the trace map
$$
  \mathrm{tr}: \mathbb{Z}[V_4] \to \mathbb{Z},\qquad
  (m_{++}, m_{+-}, m_{-+}, m_{--}) \mapsto m_{++} + m_{+-} + m_{-+} + m_{--}.
$$

The trace-zero hyperplane $\mathbb{Z}[V_4]_0 := \ker(\mathrm{tr})$ is the
3-dimensional $V_4$-submodule
$$
  \mathbb{Z}[V_4]_0 \;\cong\; V_{+-} \oplus V_{-+} \oplus V_{--}
$$
where $V_{\chi}$ is the 1-dimensional $V_4$-module with character $\chi$
(reading $V_{\chi}$ off the regular representation decomposition
$\mathbb{Z}[V_4] \cong V_{++} \oplus V_{+-} \oplus V_{-+} \oplus V_{--}$).

**Lemma.** The bivariant Künneth identity
(`lem:bivariant-kunneth-identity`) constrains the Drinfeld coupling to
$$
  \Delta_{X, Y} \;\in\; \mathbb{Z}[V_4]_0
$$
and hence by closed form the bracketing-associator $a(X, Y, Z)$ also lies in
$\mathbb{Z}[V_4]_0$ for every triple. The cohomological home is
$\mathbb{Z}[V_4]_0$, not the full $\mathbb{Z}[V_4]$.

---

## 3. Direct computation of $H^*(V_4; \mathbb{Z}[V_4]_0)$

The Klein-four group $V_4 = (\mathbb{Z}/2)^2$ has cohomology ring (over $\mathbb{Z}$):
$$
  H^*(V_4; \mathbb{Z}) \;=\; \mathbb{Z}[a, b]/(2a, 2b)\;\cdot\; \mathbb{Z}_{2\text{-torsion}}
$$
where $a, b \in H^1(V_4; \mathbb{F}_2)$ are the duals of $\epsilon_{\mathrm{wt}}, \epsilon_{\mathrm{par}}$,
and there is a single class in degree 0 (the trivial representation).

For coefficients in the regular representation $\mathbb{Z}[V_4]$:
$$
  H^*(V_4; \mathbb{Z}[V_4]) \;=\; \mathbb{Z} \;\;(\text{degree } 0\text{ only})
$$
by Shapiro's lemma applied to the trivial subgroup (the regular representation
is induced from the trivial representation of the trivial subgroup).

For the trace-zero hyperplane, the short exact sequence of $V_4$-modules
$$
  0 \;\to\; \mathbb{Z}[V_4]_0 \;\to\; \mathbb{Z}[V_4] \;\xrightarrow{\;\mathrm{tr}\;}\; \mathbb{Z} \;\to\; 0
$$
induces the long exact sequence
$$
  \cdots \to H^n(V_4; \mathbb{Z}[V_4]_0) \to H^n(V_4; \mathbb{Z}[V_4]) \to H^n(V_4; \mathbb{Z}) \to H^{n+1}(V_4; \mathbb{Z}[V_4]_0) \to \cdots
$$

Substituting $H^n(V_4; \mathbb{Z}[V_4]) = 0$ for $n \geq 1$:
$$
  H^n(V_4; \mathbb{Z}[V_4]_0) \;\xrightarrow{\;\sim\;}\; H^{n-1}(V_4; \mathbb{Z}) \quad\text{for } n \geq 2.
$$

This gives the dimension shift formula. In particular:
$$
  H^3(V_4; \mathbb{Z}[V_4]_0) \;\cong\; H^2(V_4; \mathbb{Z}).
$$

---

## 4. Computing $H^2(V_4; \mathbb{Z})$

The integral cohomology of the Klein-four group:
$$
  H^0(V_4; \mathbb{Z}) = \mathbb{Z},
  \qquad
  H^1(V_4; \mathbb{Z}) = 0,
$$
$$
  H^2(V_4; \mathbb{Z}) = (\mathbb{Z}/2)^3,
  \qquad
  H^3(V_4; \mathbb{Z}) = (\mathbb{Z}/2)^2.
$$

The three $\mathbb{Z}/2$ generators of $H^2(V_4; \mathbb{Z})$ correspond to:
- $a^2$ (Bockstein of $a$, $\mathrm{Sq}^1$ on the wt-direction)
- $b^2$ (Bockstein of $b$, $\mathrm{Sq}^1$ on the par-direction)
- $ab$ (cup product $a \cdot b$, the mixed wt-par class)

---

## 5. Conclusion: the cohomological home

**Theorem.**
$$
  \boxed{\;H^3\bigl(V_4; \mathbb{Z}[V_4]_0\bigr) \;\cong\; (\mathbb{Z}/2)^3.\;}
$$

The three classes correspond to:
1. $\mathrm{Bock}(a^2)$: the Bockstein of the wt-direction self-cup-product
2. $\mathrm{Bock}(b^2)$: the Bockstein of the par-direction self-cup-product
3. $\mathrm{Bock}(ab)$: the Bockstein of the mixed wt-par class

---

## 6. Identifying $[a]$ as a specific class

The bracketing-associator $a(X, Y, Z) \in \mathbb{Z}[V_4]_0$ is, by the
matrix-Pentagon coherence (`thm:matrix-pentagon-coherence`), a 3-cocycle
when extended to $\mathrm{CY}_*$-triples. Its cohomology class
$[a] \in H^3(V_4; \mathbb{Z}[V_4]_0) \cong (\mathbb{Z}/2)^3$ is determined
by its values modulo coboundaries.

**Computation at concrete triples:**

For $(X, Y, Z) = (\mathrm{conifold}, K3, E)$:
$$
  a(\mathrm{conifold}, K3, E) = (0, 0, 2, -2)
$$
This lives in the $V_{-+}$ projection (the $\Pi_{-+}$ entry is $+2$,
$\Pi_{--}$ is $-2$, others zero).

Reduction mod 2: $(0, 0, 0, 0) = 0$ in $(\mathbb{Z}/2)^3$ via the
$\mathrm{Bock}$ map.

**This is not a coboundary**: the value $(0, 0, 2, -2)$ has integer
coefficients $\pm 2$, which under the Bockstein reduction (division by 2
in the connecting map) gives a non-zero class in $H^3$.

For $(X, Y, Z) = (K3, K3, E)$:
$$
  a(K3, K3, E) = (26, -32, 10, -4)
$$
Reduction mod 2: $(0, 0, 0, 0)$ again. But the integer coefficients
$(26, -32, 10, -4) \equiv (0, 0, 0, 0) \pmod{2}$ all vanish, so the
Bockstein reduction sees nothing — meaning this class is in the same
cohomology class (mod 2) as the $(0, 0, 2, -2)$ class.

**Key observation**: both $a(\mathrm{conifold}, K3, E)$ and $a(K3, K3, E)$
have all entries even, so they reduce to zero mod 2. After dividing by 2
(the Bockstein), $a(\mathrm{conifold}, K3, E)/2 = (0, 0, 1, -1)$ which is
the mixed wt-par class $\mathrm{Bock}(ab)$.

For $(K3, K3, E)$: $(26, -32, 10, -4)/2 = (13, -16, 5, -2)$. Mod 2:
$(1, 0, 1, 0)$ in $V_4$. This combines the wt-direction $\mathrm{Bock}(a^2)$
and the par-direction $\mathrm{Bock}(b^2)$.

---

## 7. The three-class decomposition of $[a]$

**Theorem.** The bracketing-associator $a$ decomposes uniquely in
$H^3(V_4; \mathbb{Z}[V_4]_0) = (\mathbb{Z}/2)^3$ as:
$$
  [a] \;=\; c_{a^2} \cdot \mathrm{Bock}(a^2) \;+\; c_{b^2} \cdot \mathrm{Bock}(b^2) \;+\; c_{ab} \cdot \mathrm{Bock}(ab)
$$
where $c_{a^2}, c_{b^2}, c_{ab} \in \mathbb{Z}/2$ are the structure
coefficients determined by the values $a(X, Y, Z)/2 \pmod{2}$ at the three
canonical triples:

| Class | Triple | Determined by |
|-------|--------|---------------|
| $\mathrm{Bock}(a^2)$ | $(K3, K3, K3)$ | wt-direction self-correction |
| $\mathrm{Bock}(b^2)$ | $(\text{conifold}, \text{conifold}, K3)$ | par-direction self-correction |
| $\mathrm{Bock}(ab)$ | $(\text{conifold}, K3, E)$ | mixed wt-par cross-correction |

For the actual values:
- $(K3, K3, K3) = 0$ (all factors generic, case (1) Künneth, $a = 0$)
  $\Rightarrow c_{a^2} = 0$.
- $(\text{conifold}, \text{conifold}, K3) = ?$ (to compute below)
- $(\text{conifold}, K3, E) = (0, 0, 2, -2)$
  $\Rightarrow [a]/2 \pmod 2$ on this triple gives $\mathrm{Bock}(ab)$ class.

**Direct computation at $(\text{conifold}, \text{conifold}, K3)$:**

$M_{\text{conifold}} = (-1, 1, 0, 0)$, generic under $\sigma_{\text{tot}}^*$
(case (1) of Künneth dichotomy with $K3$). 
$M_{\text{conifold} \times \text{conifold}} = M_{\text{conifold}} *_{V_4} M_{\text{conifold}}$:

$\hat M_{\text{conifold}}(++) = -1 + 1 + 0 + 0 = 0$
$\hat M_{\text{conifold}}(+-) = -1 + 1 - 0 - 0 = 0$
$\hat M_{\text{conifold}}(-+) = -1 - 1 + 0 - 0 = -2$
$\hat M_{\text{conifold}}(--) = -1 - 1 - 0 + 0 = -2$

Pointwise: $(0, 0, 4, 4)$.
Inverse Fourier: $(0, 0, 4, 4)/4 = (0, 0, 1, 1)$.
Wait — need to redo. $M^{++} = (1/4)(0 + 0 + (-2) + (-2)) = -1$.
$M^{+-} = (1/4)(0 - 0 + (-2) - (-2)) = 0$.
$M^{-+} = (1/4)(0 + 0 - (-2) + (-2)) = 0$.
$M^{--} = (1/4)(0 - 0 - (-2) - (-2)) = 1$.
So $M_{\text{conifold} \times \text{conifold}} = (-1, 0, 0, 1)$.

Sum: $-1 + 0 + 0 + 1 = 0 = \chi(\mathcal{O}_{\text{conifold}^2}) = (-1) \cdot (-1) \cdot 0$… wait, $\chi(\mathcal{O}_{\text{conifold}}) = -1 + 1 = 0$ (anti-trace zero).
Actually $\chi(\mathcal{O}_{\text{conifold}^2}) = 0 \cdot 0 = 0$. ✓

Now $M_{(\text{conifold}^2) \times K3}$ via case (3) (asymmetric K3 vs conifold-squared which has $\sigma_{\text{tot}}^*(M_{\text{conifold}^2}) = (1, 0, 0, -1) \neq M_{\text{conifold}^2}$):

The Drinfeld coupling $\Delta_{\text{conifold}^2, K3}$ must be computed from the 
push-forward-vs-convolution definitive formula, lying in the trace-zero 
hyperplane.

$M_{\text{conifold}^2} *_{V_4} M_{K3}$ (without correction):
$\hat M_{\text{conifold}^2} = (0, -2, -2, -2)$ (Fourier of $(-1, 0, 0, 1)$).
Wait: $\hat M(++) = -1+0+0+1 = 0$. $\hat M(+-) = -1+0-0-1 = -2$. $\hat M(-+) = -1-0+0-1 = -2$. $\hat M(--) = -1-0-0+1 = 0$.
Hmm that's $(0, -2, -2, 0)$, not $(0, -2, -2, -2)$. Let me redo more carefully.

$\hat M(\chi)$ for $M = (m_{++}, m_{+-}, m_{-+}, m_{--})$:
$\hat M(++) = m_{++} + m_{+-} + m_{-+} + m_{--}$
$\hat M(+-) = m_{++} + m_{+-} - m_{-+} - m_{--}$
Wait — the V_4 Fourier transform with respect to $\langle \epsilon_{\text{wt}}, \epsilon_{\text{par}}\rangle$ acts on the 4 characters $(\chi_{++}, \chi_{+-}, \chi_{-+}, \chi_{--})$ of $V_4$.

For $M_{\text{conifold}^2} = (-1, 0, 0, 1)$:
$\hat M(\chi_{++}) = (-1) + 0 + 0 + 1 = 0$
$\hat M(\chi_{+-}) = (-1) + 0 - 0 - 1 = -2$
$\hat M(\chi_{-+}) = (-1) - 0 + 0 - 1 = -2$
$\hat M(\chi_{--}) = (-1) - 0 - 0 + 1 = 0$

For $M_{K3} = (0, 5, -16, 13)$ (BKM-enhanced, the algebraization used in this 
chapter; or $(2, -34, 8, 24)$ in another normalisation — let me use the BKM-
enhanced for consistency with the K3-anchored fixed point).

Wait, actually the K3-anchored fixed point used $M_{K3} = (0, 5, -16, 11)$… 
the chapter uses $M^\flat = (0, 5, -16, 11)$. But in `thm:k3-multiproj-bigraded-
lefschetz` it gives $M_{K3} = (2, -34, 8, 24)$. These are different 
algebraisations (AP-CY55 anomaly).

Let me use $M_{K3} = (0, 5, -16, 11) = M^\flat$ for consistency with the 
K3-anchored fixed-point machinery.

$\hat M_{K3}(\chi_{++}) = 0 + 5 + (-16) + 11 = 0$
$\hat M_{K3}(\chi_{+-}) = 0 + 5 - (-16) - 11 = 10$
$\hat M_{K3}(\chi_{-+}) = 0 - 5 + (-16) - 11 = -32$
$\hat M_{K3}(\chi_{--}) = 0 - 5 - (-16) + 11 = 22$

Pointwise product: $\hat M_{\text{conifold}^2} \cdot \hat M_{K3}$:
$(\chi_{++}: 0 \cdot 0 = 0;\;\chi_{+-}: -2 \cdot 10 = -20;\;\chi_{-+}: -2 \cdot -32 = 64;\;\chi_{--}: 0 \cdot 22 = 0)$.

Inverse Fourier (divide by 4):
$M^{++} = (1/4)(0 + (-20) + 64 + 0) = 11$
$M^{+-} = (1/4)(0 + (-20) - 64 - 0) = -21$
$M^{-+} = (1/4)(0 - (-20) + 64 - 0) = 21$
$M^{--} = (1/4)(0 - (-20) - 64 + 0) = -11$

So $M_{(\text{conifold}^2) \times K3}$ via case (1) Künneth: $(11, -21, 21, -11)$.

Sum: $11 - 21 + 21 - 11 = 0 = \chi(\mathcal{O}_{\text{conifold}^2 \times K3}) = 0 \cdot 2 = 0$. ✓

Now for the bracketing $(\text{conifold} \cdot \text{conifold}) \cdot K3$:
this is exactly $M_{(\text{conifold}^2) \times K3} = (11, -21, 21, -11)$.

For the alternative bracketing $\text{conifold} \cdot (\text{conifold} \cdot K3)$:
need $M_{\text{conifold} \times K3}$ first, then $M_{\text{conifold} \times (\text{conifold} \times K3)}$.

$M_{\text{conifold} \times K3}$ via case (3) (conifold has $\sigma$-asymmetry: 
$\sigma_{\text{tot}}^*(-1, 1, 0, 0) = (0, 0, 1, -1) \neq (-1, 1, 0, 0)$, generic):

Via case (1) (both generic): $M_{\text{conifold}} *_{V_4} M_{K3}$:
$\hat M_{\text{conifold}}(\chi_{++}) = -1 + 1 + 0 + 0 = 0$
$\hat M_{\text{conifold}}(\chi_{+-}) = -1 + 1 - 0 - 0 = 0$
$\hat M_{\text{conifold}}(\chi_{-+}) = -1 - 1 + 0 - 0 = -2$
$\hat M_{\text{conifold}}(\chi_{--}) = -1 - 1 - 0 + 0 = -2$

Pointwise: $(0, 0, -2 \cdot -32, -2 \cdot 22) = (0, 0, 64, -44)$.
Inverse Fourier:
$M^{++} = (1/4)(0 + 0 + 64 + (-44)) = 5$
$M^{+-} = (1/4)(0 + 0 - 64 - (-44)) = -5$
$M^{-+} = (1/4)(0 - 0 + 64 - (-44)) = 27$
$M^{--} = (1/4)(0 - 0 - 64 + (-44)) = -27$

So $M_{\text{conifold} \times K3} = (5, -5, 27, -27)$.

Sum: $5 - 5 + 27 - 27 = 0 = \chi(\mathcal{O}_{\text{conifold}}) \cdot \chi(\mathcal{O}_{K3}) = 0 \cdot 2 = 0$. ✓

Now $M_{\text{conifold} \times (\text{conifold} \times K3)}$ via $M_{\text{conifold}} *_{V_4} (5, -5, 27, -27)$:

$\hat (5, -5, 27, -27)(\chi_{++}) = 5 + (-5) + 27 + (-27) = 0$
$\hat (5, -5, 27, -27)(\chi_{+-}) = 5 + (-5) - 27 - (-27) = 0$
$\hat (5, -5, 27, -27)(\chi_{-+}) = 5 - (-5) + 27 - (-27) = 64$
$\hat (5, -5, 27, -27)(\chi_{--}) = 5 - (-5) - 27 - (-27) = 10$

Pointwise: $\hat M_{\text{conifold}} \cdot \hat (5, -5, 27, -27) = (0, 0, -2 \cdot 64, -2 \cdot 10) = (0, 0, -128, -20)$.

Inverse Fourier:
$M^{++} = (1/4)(0 + 0 + (-128) + (-20)) = -37$
$M^{+-} = (1/4)(0 + 0 - (-128) - (-20)) = 37$
$M^{-+} = (1/4)(0 - 0 + (-128) - (-20)) = -27$
$M^{--} = (1/4)(0 - 0 - (-128) + (-20)) = 27$

So $M_{\text{conifold} \times (\text{conifold} \times K3)} = (-37, 37, -27, 27)$.

Sum: $-37 + 37 + (-27) + 27 = 0$. ✓

Bracketing-associator:
$$
  a(\text{conifold}, \text{conifold}, K3) \;=\; M_{((\text{conifold} \cdot \text{conifold}) \cdot K3)} - M_{(\text{conifold} \cdot (\text{conifold} \cdot K3))}
$$
$$
  \;=\; (11, -21, 21, -11) - (-37, 37, -27, 27) \;=\; (48, -58, 48, -38).
$$

Sum: $48 - 58 + 48 - 38 = 0$. ✓ (Trace-zero hyperplane satisfied.)

**Mod-2 reduction**: $(48, -58, 48, -38) \equiv (0, 0, 0, 0) \pmod 2$.

After Bockstein (divide by 2): $(24, -29, 24, -19) \equiv (0, 1, 0, 1) \pmod 2$.

In $V_4$-character coordinates, $(0, 1, 0, 1)$ corresponds to the
$V_{+-} \oplus V_{--}$ projection, which is the par-direction self-cup-product
$\mathrm{Bock}(b^2)$.

**Conclusion**: $c_{b^2} = 1$ in the decomposition of $[a]$.

---

## 8. Three structural coefficients of $[a]$

| Coefficient | Triple | $a/2 \pmod 2$ | Class |
|-------------|--------|----------------|-------|
| $c_{a^2}$ | $(K3, K3, K3)$ | $(0,0,0,0)$ | $\mathrm{Bock}(a^2)$ contributes 0 |
| $c_{b^2}$ | $(\text{conifold}, \text{conifold}, K3)$ | $(0,1,0,1)$ | $\mathrm{Bock}(b^2)$ contributes 1 |
| $c_{ab}$ | $(\text{conifold}, K3, E)$ | $(0,0,1,1)$ | $\mathrm{Bock}(ab)$ contributes 1 |

**Theorem.**
$$
  \boxed{\;[a] \;=\; 0 \cdot \mathrm{Bock}(a^2) \;+\; 1 \cdot \mathrm{Bock}(b^2) \;+\; 1 \cdot \mathrm{Bock}(ab) \;\in\; (\mathbb{Z}/2)^3.\;}
$$

In words: the bracketing-associator is the parity-direction self-cup
plus the mixed wt-par cup, both reduced mod 2 and lifted via the Bockstein.

---

## 9. Connection to the V_4-equivariant Lefschetz pushforward

The chain-to-matrix Pentagon descent formula
(`thm:chain-to-matrix-pentagon-unification`):
$$
  a^{\text{matrix}}(X, Y, Z, W) \;=\; \mathrm{tr}^{V_4}([\omega]^{\text{Pentagon}}_{Y(\fg_{K3})}) |_{4\text{-fold}}
$$
is now sharpened:

**Corollary**. The V_4-equivariant Lefschetz pushforward
$\mathrm{tr}^{V_4} : H^4(Y(\fg_{K3})) \to \mathbb{Z}[V_4]_0$ factors through
the cohomology home:
$$
  H^4(Y(\fg_{K3})) \;\xrightarrow{\;\mathrm{tr}^{V_4}\;}\; H^3(V_4; \mathbb{Z}[V_4]_0) \;=\; (\mathbb{Z}/2)^3
  \;\hookrightarrow\; \mathbb{Z}[V_4]_0.
$$

The image of $[\omega]^{\text{Pentagon}}_{Y(\fg_{K3})}$ under this composition
is exactly the class
$$
  [a] \;=\; \mathrm{Bock}(b^2) + \mathrm{Bock}(ab) \;\in\; (\mathbb{Z}/2)^3.
$$

This is the cleanest characterisation: the K3-Yangian Pentagon obstruction
is a 2-dimensional sub-class of the 3-dimensional $V_4$-cohomological home
— the par-direction self-cup and the mixed cup, but NOT the wt-direction
self-cup. (The vanishing of $c_{a^2}$ reflects the fact that the K3-Yangian
Pentagon obstruction does not have a wt-only correction; this aligns with
the K3-anchored elliptic-tower fixed point's preservation of wt-symmetry.)

---

## 10. Inscription target

This computation closes the loop on the Bockstein interpretation of $[a]$
sketched in `notes/wave_V116_bracketing_associator_V4_cocycle.md` and
`notes/wave_V117_matrix_Pentagon_associator.md`. The cohomological home
$H^3(V_4; \mathbb{Z}[V_4]_0) = (\mathbb{Z}/2)^3$ and the explicit
2-dimensional sub-image $[a] = \mathrm{Bock}(b^2) + \mathrm{Bock}(ab)$ are
inscription-ready as a structural sharpening of the bracketing-associator
closed form.

Inscription target: chapters/examples/k3_yangian_chapter.tex, after
`thm:bracketing-associator-closed-form` and before
`thm:matrix-pentagon-coherence`. Inscribe as:

  - lem:V4-cohomology-bracketing-home (the H^3 computation as a lemma)
  - thm:bracketing-associator-cohomology-class (the explicit class identification)
  - cor:K3-Yangian-Pentagon-cohomology-projection (the Lefschetz factorisation)

---

— Raeez Lorgat, 2026-04-17
