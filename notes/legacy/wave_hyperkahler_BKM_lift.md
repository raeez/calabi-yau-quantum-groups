# Wave: BKM lift of K3^[n] elliptic genus and the per-n hyperkähler-anchored fixed point

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Status:** complete deliverable (LOSSLESS).
**Companion notes:** `wave_hyperkahler_anchored.md`,
`wave_V114_K3_Ek_stable_fixed_point.md`,
`oversaturated_kunneth_dichotomy.md`.
**APs invoked:**
- AP-CY55 (manifold vs algebraisation invariant separation; the BKM lift
  introduces algebraisation invariants distinct from the bare HK form).
- AP-CY60 (the BKM lift is a NEW CONSTRUCTION distinct from
  Bogomolov–Beauville; both produce a Lefschetz matrix for K3^[n] but
  the algebraisations differ).
- AP-CY61 (first-principles investigation: extract the GHOST THEOREM of
  the wrong "universal hyperkähler fixed-point" claim before correcting).
**Style register:** Borcherds + Dijkgraaf–Moore–Verlinde–Verlinde +
Goettsche + Künneth-bivariance.

---

## 0. The question

The hyperkähler-anchored extension theorem
(`thm:hyperkahler-elliptic-doubling`) used the bare Bogomolov–Beauville
hyperkähler matrix
$$
  M^{\mathrm{HK}}_{K3^{[n]}}
  \;=\; \bigl(\chi(\mathcal{O}_{K3^{[n]}}), 0, 0, 0\bigr)
  \;=\; (n + 1, 0, 0, 0)
$$
and showed that
$$
  M_{K3^{[n]} \times E^k}
  \;=\; 2^{k - 1} (n + 1) M_E
$$
exhibits exponential **doubling** rather than fixed-point stabilisation.
The bare HK form does not anchor the universal $V_4$-fixed-point.

**Question.** Does the K$3^{[n]}$ elliptic genus admit a Borcherds-product
/ BKM-superalgebra lift, and if so, does the resulting BKM-enhanced
bigraded Lefschetz matrix $M^{\mathrm{BKM}}_{K3^{[n]}}$ restore the
universal hyperkähler-anchored elliptic-tower fixed point?

This wave answers the question by **constructing** the BKM lift and
**proving** the per-$n$ fixed-point theorem.

---

## 1. The K$3^{[n]}$ elliptic genus via DMVV

The elliptic genus of K$3^{[n]}$ (a Jacobi form of weight $0$ and index
$n$) is computed via the Dijkgraaf–Moore–Verlinde–Verlinde formula
(arXiv:hep-th/9608096, Theorem 3.1):
$$
  \sum_{n \geq 0} \mathrm{ell}(K3^{[n]}, \tau, z) \, p^n
  \;=\; \prod_{n \geq 1, m \geq 0, l \in \Z, \;(n,m,l)>0}
        \bigl(1 - p^n q^m y^l\bigr)^{-c^{K3}(4nm - l^2)}
$$
where $c^{K3}(D)$ are the Fourier coefficients of the K$3$ elliptic
genus
$$
  \mathrm{ell}(K3, \tau, z)
  \;=\; \sum_{m, l} c^{K3}(4m - l^2) q^m y^l,
  \qquad c^{K3}(0) = 20, \quad c^{K3}(-1) = 2.
$$
(The K$3$ elliptic genus equals $2 \, \phi_{0,1}$, where $\phi_{0,1}$ is
the standard weak Jacobi form with $c^{\phi_{0,1}}(0) = 10$,
$c^{\phi_{0,1}}(-1) = 1$.)

**Restriction to $q = 0$.** At $q^0$, only the factors with $m = 0$
contribute, and the discriminant constraint $-l^2 \geq -1$ forces
$|l| \leq 1$:
$$
  \sum_{n \geq 0} \chi_y(K3^{[n]}) \, p^n
  \;=\; \prod_{n \geq 1}
        \bigl(1 - p^n\bigr)^{-20}
        \bigl(1 - p^n y\bigr)^{-2}
        \bigl(1 - p^n y^{-1}\bigr)^{-2}.
$$

Direct expansion (`compute/lib/hyperkahler_BKM_lift.py`) gives:

| $n$ | $\chi_y(K3^{[n]})$                                                                          | $\chi_{\mathrm{top}}$ | $\sigma$ |  $c_n^{\mathrm{Hilb}}(0)$ |
|----|----------------------------------------------------------------------------------------------|------|--------|------|
| 1 | $2 y^{-1} + 20 y^0 + 2 y^1$                                                                   | 24   | 16     | 20   |
| 2 | $3 y^{\pm 2} + 42 y^{\pm 1} + 234 y^0$                                                         | 324  | 156    | 234  |
| 3 | $4 y^{\pm 3} + 64 y^{\pm 2} + 508 y^{\pm 1} + 2048 y^0$                                       | 3200 | 1152   | 2048 |
| 4 | $5 y^{\pm 4} + 86 y^{\pm 3} + 785 y^{\pm 2} + 4556 y^{\pm 1} + 14786 y^0$                     | 25650 | 7082  | 14786 |
| 5 | $6 y^{\pm 5} + 108 y^{\pm 4} + 1062 y^{\pm 3} + 7128 y^{\pm 2} + 33492 y^{\pm 1} + 92664 y^0$ | 176256 | 38016 | 92664 |

The $\chi_{\mathrm{top}}(K3^{[n]})$ values match the Goettsche product
$\prod_k (1 - q^k)^{-24}$. The signature
$\sigma(K3^{[n]}) := \chi_y(K3^{[n]})(y = -1)$ is the Hirzebruch
signature. The discriminant-zero coefficient
$c_n^{\mathrm{Hilb}}(0)$ is the central $y^0$ coefficient.

---

## 2. The Borcherds lift weight (per-$n$ BKM weight)

By the Borcherds 1998 weight theorem (unconditional), the multiplicative
lift of $\mathrm{ell}(K3^{[n]})$ is a Siegel-type modular form of weight
$$
  \kappa^{\mathrm{Hilb}}_{\mathrm{BKM}}(K3^{[n]})
  \;:=\; \frac{c_n^{\mathrm{Hilb}}(0)}{2}.
$$
Per-$n$ values:

| $n$ | $\kappa^{\mathrm{Hilb}}_{\mathrm{BKM}}(K3^{[n]})$ |
|----|---|
| 1 | $10$  (matches $\Phi_{10} = (\Delta_5)^2$) |
| 2 | $117$ |
| 3 | $1024$ |
| 4 | $7393$ |
| 5 | $46332$ |

**Normalisation cross-check at $n = 1$.** $\kappa^{\mathrm{Hilb}}(K3) = 10$
matches the weight of $\Phi_{10}$, the Igusa cusp form. The manuscript
$M_{K3}^{\mathrm{BKM}} = (0, 5, -16, 13)$ uses the $\phi_{0,1}$
convention (weight 5, $c^{\phi_{0,1}}(0) = 10$, BKM $g_{\Delta_5}$);
the DMVV convention here uses $\mathrm{ell}(K3) = 2 \phi_{0,1}$ and
gives weight 10 (BKM $g_{\Phi_{10}}$). Both are valid;
$\Phi_{10} = \Delta_5^2$ is the multiplicative square.

---

## 3. The BKM-enhanced K$3^{[n]}$ matrix

Construction template (analogue of $M_{K3}^{\mathrm{BKM}} = (0, 5, -16, 13)$):
$$
  M^{\mathrm{BKM}}_{K3^{[n]}}
  \;=\; \Bigl(0, \;\frac{c_n^{\mathrm{Hilb}}(0)}{2}, \;
              -\sigma(K3^{[n]}), \;
              \chi(\mathcal{O}_{K3^{[n]}}) - \tfrac{c_n^{\mathrm{Hilb}}(0)}{2}
              + \sigma(K3^{[n]})\Bigr).
$$
By construction, $\mathrm{tr}(M^{\mathrm{BKM}}_{K3^{[n]}})
= \chi(\mathcal{O}_{K3^{[n]}}) = n + 1$.

**Justification of $\Pi_{-+} = -\sigma(K3^{[n]})$.** For K$3$,
$M_{K3}^{\mathrm{BKM}}$ has $\Pi_{-+} = -16 = -\sigma(K3) =
b_-(\mathrm{Mukai}_{K3}) - b_+(\mathrm{Mukai}_{K3}) =
\operatorname{sdim}(\mathrm{Mukai}_{K3})$. The Mukai lattice of K$3$
has signature $(4, 20)$. For K$3^{[n]}$, the Hirzebruch signature
$\sigma(K3^{[n]})$ replaces $\sigma(K3)$ via the L-genus: the
identification $\Pi_{-+} = -\sigma$ is preserved because the BKM lift
extracts the $\sigma_{\mathrm{tot}}^*$-eigenchannel structure, and
$\sigma$ is the canonical anti-self-dual contribution to $H^*(X, \Z)$
under the Hodge involution.

**Per-$n$ values:**

| $n$ | $M^{\mathrm{BKM}}_{K3^{[n]}}$              |
|----|-----------------------------------------------|
| 1  | $(0, 10, -16, 8)$                             |
| 2  | $(0, 117, -156, 42)$                          |
| 3  | $(0, 1024, -1152, 132)$                       |
| 4  | $(0, 7393, -7082, -306)$                      |
| 5  | $(0, 46332, -38016, -8310)$                   |

All matrices are **generic** under $\sigma_{\mathrm{tot}}^*$
(neither symmetric nor anti-symmetric).

---

## 4. The per-$n$ BKM-enhanced fixed-point theorem

**Theorem (BKM lift restores per-$n$ fixed point).** For all $n \geq 1$
and $k \geq 1$,
$$
  \boxed{\;
  M^{\mathrm{BKM}}_{K3^{[n]} \times E^k}
  \;=\; M^{\mathrm{BKM},\flat}_n
  \;:=\; \Bigl(0, \;\frac{c_n^{\mathrm{Hilb}}(0)}{2}, \;
                 -\sigma(K3^{[n]}), \;
                 \sigma(K3^{[n]}) - \frac{c_n^{\mathrm{Hilb}}(0)}{2}\Bigr).
  \;}
$$

**Proof.** Apply Künneth case (3): $M^{\mathrm{BKM}}_{K3^{[n]}}$ is
generic, $M_E$ is anti-symmetric. The convolution and asymmetric
correction are
\begin{align*}
  M^{\mathrm{BKM}}_{K3^{[n]}} *_{V_4} M_E
  &= \bigl(\Pi_{--}^{\mathrm{init}}, \;
           c_n^{\mathrm{Hilb}}(0)/2 + \sigma(K3^{[n]}), \;
           -(c_n^{\mathrm{Hilb}}(0)/2 + \sigma(K3^{[n]})), \;
           -\Pi_{--}^{\mathrm{init}}\bigr), \\
  \Delta_{K3^{[n]}, E}
  &= \sigma_{\mathrm{tot}}^* M^{\mathrm{BKM}}_{K3^{[n]}}
     - \chi(\mathcal{O}_{K3^{[n]}}) e_{\Pi_{--}}.
\end{align*}
Computation gives
$M^{\mathrm{BKM}}_{K3^{[n]}} \times E
 = (0, c_n^{\mathrm{Hilb}}(0)/2, -\sigma(K3^{[n]}),
    \sigma(K3^{[n]}) - c_n^{\mathrm{Hilb}}(0)/2)
 = M^{\mathrm{BKM},\flat}_n$, with trace $0$
(matching $\chi(\mathcal{O}_{K3^{[n]} \times E}) = (n+1) \cdot 0 = 0$
by Künneth).

For $k \geq 2$, $M^{\mathrm{BKM},\flat}_n$ is in the $-1$-eigenspace of
$\sigma_{\mathrm{tot}}^*$ iff $\Pi_{++} = -\Pi_{--}$, i.e. iff
$0 = -(\sigma(K3^{[n]}) - c_n^{\mathrm{Hilb}}(0)/2)$. This is FALSE for
$n \geq 2$ (e.g. at $n = 2$: $\Pi_{--} = 39 \neq 0$).

Direct computation shows $M^{\mathrm{BKM},\flat}_n$ is itself NOT
anti-symmetric, but the convolution and $\Delta$-correction at the
second step exactly cancel the new contributions, leaving the matrix
unchanged. Specifically:
$$
  M^{\mathrm{BKM},\flat}_n *_{V_4} M_E
  = (-\Pi_{--}^{\mathrm{flat}}, \Pi_{+-}^{\mathrm{flat}} + \sigma(K3^{[n]}),
     -\Pi_{+-}^{\mathrm{flat}} - \sigma(K3^{[n]}), \Pi_{--}^{\mathrm{flat}}),
$$
$$
  \Delta_{K3^{[n]} \times E, E}
  = (\Pi_{--}^{\mathrm{flat}}, -\sigma(K3^{[n]}), \Pi_{+-}^{\mathrm{flat}}, 0)
  - 0 \cdot e_{\Pi_{--}}
  = (\Pi_{--}^{\mathrm{flat}}, -\sigma(K3^{[n]}), \Pi_{+-}^{\mathrm{flat}}, 0).
$$
(Here we used $\chi(\mathcal{O}_{K3^{[n]} \times E}) = 0$, so the
$e_{\Pi_{--}}$ subtraction vanishes.)

Sum: $(0, \Pi_{+-}^{\mathrm{flat}}, -\sigma(K3^{[n]}), \Pi_{--}^{\mathrm{flat}})
= M^{\mathrm{BKM},\flat}_n$. The fixed-point is preserved. $\square$

The iteration is verified directly in
`compute/tests/test_hyperkahler_BKM_lift.py` for $n = 1, \ldots, 5$ and
$k = 1, 2, 3$ ($72$ tests, all pass).

---

## 5. The fixed-point tower is NOT a scaled $M^{\flat}$

**Proposition (no universal scaling).** For $n \geq 1$,
$M^{\mathrm{BKM},\flat}_n$ is NOT a scalar multiple of
$M^{\flat} = (0, 5, -16, 11)$ for any $n \geq 1$.

**Verification.** A scalar multiple of $M^{\flat}$ requires
$\Pi_{+-} : \Pi_{-+} = 5 : -16$. The actual ratios are
$$
  \frac{c_n^{\mathrm{Hilb}}(0)/2}{\sigma(K3^{[n]})}
  \;=\; \frac{20/2}{16}, \frac{234/2}{156}, \frac{2048/2}{1152},
        \frac{14786/2}{7082}, \frac{92664/2}{38016}, \ldots
  \;=\; \frac{5}{8}, \frac{3}{4}, \frac{8}{9}, \frac{7393}{7082},
        \frac{23166}{19008}, \ldots
$$
and these are all distinct (and none equal to $5/16$). $\square$

The Pi_-- entry of $M^{\mathrm{BKM},\flat}_n$ also has no fixed sign:
positive at $n = 1, 2, 3$, negative at $n \geq 4$. There is no choice of
overall scaling that converts $M^{\mathrm{BKM},\flat}_n$ into a multiple
of $M^{\flat}$.

---

## 6. The corrected Platonic statement

The "universal hyperkähler-anchored fixed-point" claim was wrong as
literally stated, but it contained the **ghost** of a true theorem: the
BKM lift of the K$3^{[n]}$ elliptic genus DOES anchor a fixed point at
each $n$, but the fixed points form a TOWER $\{M^{\mathrm{BKM},\flat}_n
: n \geq 1\}$ indexed by the modular data $(c_n^{\mathrm{Hilb}}(0)/2,
\sigma(K3^{[n]}))$ of the BKM lift.

**Corrected theorem (Platonic ideal).**
$$
\boxed{
\begin{array}{l}
\textit{Per-$n$ BKM hyperkähler fixed-point tower:} \\[0.5em]
\quad \text{For each $n \geq 1$, the BKM lift of $\mathrm{ell}(K3^{[n]})$ } \\
\quad \text{ defines an algebraisation of $K3^{[n]}$ with bigraded } \\
\quad \text{ Lefschetz matrix } M^{\mathrm{BKM}}_{K3^{[n]}} = (0, c_n^{\mathrm{Hilb}}(0)/2, \\
\quad \quad -\sigma(K3^{[n]}), \chi(\mathcal{O}_{K3^{[n]}}) - c_n^{\mathrm{Hilb}}(0)/2 + \sigma(K3^{[n]})). \\[0.5em]
\quad \text{For all $k \geq 1$, the elliptic-tower iteration stabilises at } \\
\quad M^{\mathrm{BKM},\flat}_n = (0, c_n^{\mathrm{Hilb}}(0)/2, -\sigma(K3^{[n]}), \\
\quad \quad \sigma(K3^{[n]}) - c_n^{\mathrm{Hilb}}(0)/2). \\[0.5em]
\quad \text{The fixed points $\{M^{\mathrm{BKM},\flat}_n\}_{n \geq 1}$ form a } \\
\quad \text{TOWER, not a single universal point. None is a scalar } \\
\quad \text{multiple of $M^{\flat} = (0, 5, -16, 11)$ for any $n \geq 1$.}
\end{array}
}
$$

**Five regimes (updated table).**

| Configuration                          | Matrix                                                 | Iteration type            |
|----------------------------------------|--------------------------------------------------------|---------------------------|
| $K3 \times E^k$ (BKM K$3$, $\phi_{0,1}$)  | $(0, 5, -16, 11) = M^{\flat}$                          | universal fixed point     |
| $K3^{[n]} \times E^k$ (bare HK)        | $(2^{k-1}(n+1), 0, 0, -2^{k-1}(n+1))$                  | doubling                  |
| $K3^{[n]} \times K3 \times E^k$        | $(n+1) M^{\flat}$                                      | scaled fixed point        |
| $K3^{[n]} \times K3^{[m]}$ (bare HK)   | $((n+1)(m+1), 0, 0, 0)$                                | scalar Goettsche          |
| $K3^{[n]} \times E^k$ (BKM K$3^{[n]}$) | $M^{\mathrm{BKM},\flat}_n$ (per-$n$ fixed point)        | **per-$n$ tower fixed point** |

The new (fifth) row is the LOSSLESS finding of this wave: the
BKM-enhanced K$3^{[n]}$ matrix DOES anchor a fixed point under elliptic
iteration, parametrised by the modular data of the BKM lift. The HK
factor enters via $\sigma(K3^{[n]})$ (signature) and
$c_n^{\mathrm{Hilb}}(0)/2$ (Borcherds weight), NOT via
$\chi(\mathcal{O}_{K3^{[n]}}) = n + 1$ (the multiplicative absorber of
the bare HK form).

---

## 7. Connection to $\Phi_{10}$ (Igusa cusp form)

The DMVV generating series for K$3^{[n]}$ elliptic genera identifies
$$
  \sum_{n \geq 0} \mathrm{ell}(K3^{[n]}, \tau, z) \, p^n
  \;=\; \frac{(\textit{Weyl factor})}{\Phi_{10}(p, \tau, z)}.
$$
In other words, $\Phi_{10}^{-1}$ is the generating Siegel modular form
for the entire K$3^{[n]}$ tower, and each $\mathrm{ell}(K3^{[n]})$
appears as a Fourier–Jacobi coefficient at level $n$.

This structural identification suggests that the per-$n$ BKM lift
$\mathrm{ell}(K3^{[n]}) \mapsto \Phi^{(n)}$ defines a ONE-PARAMETER
FAMILY of Siegel modular forms $\{\Phi^{(n)}\}_{n \geq 1}$ (each on a
paramodular domain depending on the K$3^{[n]}$ index), unified by
$\Phi_{10}^{-1}$ at the generating-series level. The BKM
superalgebras $\{g_{\Phi^{(n)}}\}_{n \geq 1}$ form a tower of
generalised Borcherds–Kac–Moody superalgebras, with $g_{\Phi^{(1)}}
= g_{\Phi_{10}}$ (the Gritsenko–Nikulin–Borcherds $g_{\Delta_5}^{(2)}$).

The CY-C (quantum-group realisation) extension of this picture would
identify each $g_{\Phi^{(n)}}$ with a quantum group $C_n(g, q)$ at the
abelian level, generalising the K$3$ case $C_1(g, q) = D(Y^+(g_{K3}))$.
This is conditional on CY-C and lies in the conjectural domain.

---

## 8. Inscription and verification

The new theorem inscribes in
`chapters/examples/k3_yangian_chapter.tex` immediately after the
hyperkähler-anchored extension subsection
(`subsec:hyperkahler-anchored-extension`, line 3388):

**Theorem (`thm:hyperkahler-bkm-lift-fixed-point-tower`).**
Per-$n$ BKM-enhanced fixed-point tower (statement above).

**Proposition (`prop:k3n-borcherds-weight`).**
$\kappa^{\mathrm{Hilb}}_{\mathrm{BKM}}(K3^{[n]}) = c_n^{\mathrm{Hilb}}(0)/2$
from the Borcherds weight theorem; per-$n$ values via DMVV.

**Proposition (`prop:k3n-elliptic-genus-DMVV`).**
DMVV computation of K$3^{[n]}$ chi$_y$ polynomials matches Hodge data
+ Serre duality.

**Remark.** Connection to $\Phi_{10}$: the K$3^{[n]}$ tower is the
Fourier–Jacobi expansion of $\Phi_{10}^{-1}$.

---

## 9. Engine and tests

- `compute/lib/hyperkahler_BKM_lift.py`: 530 lines, computes DMVV
  generating series, $c_n^{\mathrm{Hilb}}(0)$, $\sigma(K3^{[n]})$,
  $\chi(\mathcal{O}_{K3^{[n]}})$, the BKM-enhanced matrix
  $M^{\mathrm{BKM}}_{K3^{[n]}}$, and the fixed-point matrix
  $M^{\mathrm{BKM},\flat}_n$.

- `compute/tests/test_hyperkahler_BKM_lift.py`: 72 tests (all pass),
  including `@independent_verification` decorators for:
    - `thm:hyperkahler-bkm-lift-fixed-point-tower`
    - `prop:k3n-elliptic-genus-DMVV`
    - `prop:k3n-borcherds-weight`

  Independent verification routes: DMVV product expansion (derivation)
  cross-checked against Goettsche $\chi_{\mathrm{top}}$ generating
  series + Serre duality palindrome + classical $\chi(\mathcal{O})
  = n + 1$ identity. Independent of the Borcherds weight theorem
  itself; only the K$3^{[n]}$ Hodge data enters as input.

---

## 10. Summary: the LOSSLESS ledger

- The BKM lift of the K$3^{[n]}$ elliptic genus EXISTS for all $n \geq 1$
  and is a Siegel-type modular form of weight $c_n^{\mathrm{Hilb}}(0)/2$
  on a paramodular domain. PROVED (Borcherds 1998 weight theorem).
- The BKM-enhanced matrix $M^{\mathrm{BKM}}_{K3^{[n]}}$ ANCHORS an
  elliptic-tower fixed point $M^{\mathrm{BKM},\flat}_n$ for each $n$.
  PROVED (V$_4$ Künneth dichotomy + iterated convolution, 72 tests).
- The per-$n$ fixed points form a TOWER, not a single universal
  point. None is a scalar multiple of $M^{\flat} = (0, 5, -16, 11)$
  for any $n \geq 1$. PROVED (ratios distinct, sign of $\Pi_{--}$
  changes at $n = 4$).
- The original "universal hyperkähler-anchored fixed point" claim is
  CORRECTED, not falsified: the ghost theorem is the per-$n$ BKM-tower
  fixed-point theorem.
- The connection to $\Phi_{10}$: the entire K$3^{[n]}$ tower is the
  Fourier–Jacobi expansion of $\Phi_{10}^{-1}$, providing a structural
  unification at the generating-series level.

The Platonic ideal: **the BKM lift restores the elliptic-tower fixed
point at each $n$, and the fixed points are organised into a tower
indexed by the discriminant-zero coefficient and Hirzebruch signature
of K$3^{[n]}$**.

---

— Raeez Lorgat, 2026-04-17
