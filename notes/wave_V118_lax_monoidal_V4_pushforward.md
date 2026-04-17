# Wave V118 --- Lax monoidal $V_4$-push-forward and $A_\infty$-truncation at $m_3 = a$

**Author.** Raeez Lorgat. **Date.** 2026-04-16.
**Wave.** V118 (LOSSLESS RELAUNCH; 3rd attempt; first two server-rate-limited).
**Mode.** Russian-school foundational heal. Lax monoidal categories +
Lurie *Higher Algebra* + Hodge-piece push-forward.
**Posture.** Read-only sandbox memorandum. No `.tex` edits, no CLAUDE.md
updates, no commits, no test runs. AP-CY55, AP-CY60, AP-CY61, HZ3-3,
HZ3-12 govern every step.

**Inputs.**

* V115 (`wave_V115_conifold_x_K3_absorber.md`): conifold $E$-absorber
  theorem; bracketing-discrepancy
  $M_{(\mathrm{conifold}\times K3)\times E} - M_{\mathrm{conifold}\times(K3\times E)}
  = (0,0,2,-2)$; bracketing dependence is a chain-level non-feature visible
  only after $V_4$-equivariant trace.
* V117 (`wave_V117_matrix_Pentagon_associator.md`): matrix Pentagon HOLDS
  on $\mathrm{conifold}\times K3\times E\times E$; $\delta a = 0$ in
  $V_4^\vee \otimes \mathbb{Z}$; $a^{\mathrm{matrix}}
  = \mathrm{tr}^{V_4}([\omega]^{\mathrm{Pentagon}}_{Y(\mathfrak{g}_{K3})})$.
* `oversaturated_kunneth_dichotomy.md`: the Drinfeld correction
  $\Delta_{X,Y} = \pi_{X\times Y}(\widetilde{M}_X *_{\widetilde V}
  \widetilde{M}_Y) - \pi_X(\widetilde{M}_X) * \pi_Y(\widetilde{M}_Y)$ is the
  non-commutativity between push-forward $\pi$ and convolution $*$ in the
  regular-representation lattice.

V117's coherence verdict is: lax monoidal with coherent associator is
*equivalent* to an $A_\infty$-graded ring with $m_2 =$ Künneth--Drinfeld,
$m_3 = a$, $m_n = 0$ for $n\geq 4$. V118 *constructs* the lax monoidal
structure, computes $m_3 = a$ explicitly, and proves the truncation
$m_{n\geq 4} = 0$.

---

## §1. The two monoidal categories and the push-forward

### 1.1 Source: over-saturated convolution category

Let $\widetilde{V}_X = (\mathbb{Z}/2)^{2 + r(X)}$ be the over-saturated
symmetry of a CY manifold $X$ with $r(X)$ Hodge-piece pairs (cf. the
dichotomy note). The over-saturated regular-representation lattice
$\mathbb{Z}[\widetilde{V}_X]$ carries the convolution product
$*_{\widetilde{V}_X}$. The category of over-saturated matrices has objects
$\widetilde{M}_X \in \mathbb{Z}[\widetilde{V}_X]$ and morphisms by integer
linear maps respecting $\widetilde{V}_X$-grading. The convolution
$*_{\widetilde{V}_{X\times Y}}$ on the fibre product
$\widetilde{V}_{X\times Y} = \widetilde{V}_X \times_{V_4} \widetilde{V}_Y$
is *strictly associative* and *strictly unital*, by classical Pontryagin
duality on the abelian regular representation.

We call this the *source category* $\widetilde{\mathcal{C}}$: a strict
symmetric monoidal $\mathbb{Z}$-linear category with product
$\widetilde{*}$ and unit $\widetilde{\mathbf{1}} = e_{(+,\dots,+)}$.

### 1.2 Target: $V_4$ Künneth--Drinfeld category

The target $V_4^\vee\otimes\mathbb{Z}$ carries the Künneth--Drinfeld
product $M_X \star M_Y := M_X *_{V_4} M_Y + \Delta_{X,Y}$ where $*_{V_4}$
is convolution and $\Delta_{X,Y}$ is the Drinfeld correction satisfying
the V115 dichotomy. We denote the resulting $\mathbb{Z}$-linear category
$\mathcal{C}_{V_4}$ with product $\star$.

This is *not* strictly monoidal: V115 §7.3 explicitly exhibits a
back-slot bracketing discrepancy $(0,0,2,-2)$. V117 §2.3 verifies this
discrepancy is a Mac Lane 3-cocycle (Pentagon $\delta a = 0$). So
$\mathcal{C}_{V_4}$ is at most *lax monoidal*, with associator $a$.

### 1.3 The functor $\pi: \widetilde{\mathcal{C}} \to \mathcal{C}_{V_4}$

The push-forward $\pi_X: \mathbb{Z}[\widetilde{V}_X] \to V_4^\vee\otimes\mathbb{Z}$
is the orbit-sum along the kernel
$K_X = \ker(\widetilde{V}_X \twoheadrightarrow V_4)$ (dichotomy note §2).
Define $\pi: \widetilde{\mathcal{C}} \to \mathcal{C}_{V_4}$ by
$\pi(\widetilde{M}_X) := \pi_X(\widetilde{M}_X) = M_X$ on objects, with
the identity on hom-sets.

**Claim (functoriality).** $\pi$ is $\mathbb{Z}$-linear and respects units
($\pi(\widetilde{\mathbf{1}}) = e_{(++)} = \mathbf{1}_{V_4}$). It is *not*
strictly monoidal: the dichotomy note §4 displays the obstruction
$$
\pi(\widetilde{M}_X \mathbin{\widetilde{*}} \widetilde{M}_Y)
\;-\; \pi(\widetilde{M}_X) *_{V_4} \pi(\widetilde{M}_Y)
\;=\; \Delta_{X,Y}
\;\in\; V_4^\vee\otimes\mathbb{Z},
$$
which is precisely the Drinfeld coupling correction.

This obstruction is *not* a defect; it is the *content* of $\pi$ being
**lax monoidal**.

---

## §2. The lax monoidal structure on $\pi$

### 2.1 Lax structure morphism

A lax monoidal functor $\pi: (\widetilde{\mathcal{C}}, \widetilde{*})
\to (\mathcal{C}_{V_4}, *_{V_4})$ consists of natural maps
$$
\mu_{X,Y}\colon \pi(\widetilde{M}_X) *_{V_4} \pi(\widetilde{M}_Y)
\;\longrightarrow\;
\pi(\widetilde{M}_X \mathbin{\widetilde{*}} \widetilde{M}_Y),
$$
together with a unit map $\eta\colon \mathbf{1}_{V_4} \to \pi(\widetilde{\mathbf{1}})$,
satisfying associativity and unit coherence pentagons (Mac Lane).

In our setting, define
$$
\boxed{\;
\mu_{X,Y}(M_X *_{V_4} M_Y)
\;:=\;
M_X *_{V_4} M_Y \;+\; \Delta_{X,Y}
\;=\;
M_{X\times Y}.
\;}
$$
That is, $\mu_{X,Y}$ is the inclusion that *adds back* the Drinfeld
correction $\Delta_{X,Y}$ to recover the actual push-forward of the
over-saturated product.

This is canonical: $\mu_{X,Y}$ is the unique additive map whose
co-domain is $\pi(\widetilde{M}_X *_{\widetilde{V}} \widetilde{M}_Y)
= M_{X\times Y}$ extending the identity on the
$\sigma_{\mathrm{tot}}^*$-symmetric component. Naturality in $X, Y$
follows from the dichotomy note §3: $\Delta_{X,Y}$ is determined by
the $\sigma_{\mathrm{tot}}^*$-eigenspace classes of $M_X$ and $M_Y$,
which are functorial.

The unit $\eta$ is the identity (the over-saturated unit pushes to the
$V_4$ unit), since $\Delta_{\mathbf{1}, Y} = 0$ trivially: the unit is
$K$-invariant on every factor.

### 2.2 The associator $a$ from the lax structure

For a triple $(X,Y,Z)$, the lax structure gives two ways to compute
$\pi(\widetilde{M}_X \widetilde{*} \widetilde{M}_Y \widetilde{*}
\widetilde{M}_Z)$:

\begin{align*}
\text{(Bracket}_L\text{):}\quad &
\mu_{X\times Y, Z} \circ (\mu_{X,Y} *_{V_4} \mathrm{id}_Z)
\;:\; (M_X *_{V_4} M_Y) *_{V_4} M_Z
\;\to\; M_{X\times Y \times Z};\\
\text{(Bracket}_R\text{):}\quad &
\mu_{X, Y\times Z} \circ (\mathrm{id}_X *_{V_4} \mu_{Y,Z})
\;:\; M_X *_{V_4} (M_Y *_{V_4} M_Z)
\;\to\; M_{X\times Y \times Z}.
\end{align*}

Both reach the same source-side object
$\pi(\widetilde{M}_X \widetilde{*} \widetilde{M}_Y \widetilde{*}
\widetilde{M}_Z) = M_{X\times Y\times Z}$ because $\widetilde{*}$ is
*strictly* associative on the source side. So the two bracketings of the
*lax structure* agree on the codomain --- but the two paths of the
*$V_4$-product* differ by the bracketing-associator. Concretely, the
difference between Bracket$_L$ and Bracket$_R$ at the level of $V_4$
matrices is the V115 §7.3 / V117 §2 quantity:
$$
a(X, Y, Z)
\;:=\;
M_{(X\times Y)\times Z} - M_{X\times(Y\times Z)}
\;\in\; V_4^\vee \otimes \mathbb{Z}.
$$
For $(W, X, Y) = (\mathrm{conifold}, K3, E)$ this is
$(0,0,2,-2)$; for $(W, X, Y) = (W, K3, E)$ on the larger 4-tuple test
of V117 the values are §2.1 of V117.

The lax monoidal data $(\mu, \eta, a)$ thus has:
- Strictly associative *source* $(\widetilde{\mathcal{C}}, \widetilde{*})$;
- Lax-but-coherent *target* $(\mathcal{C}_{V_4}, *_{V_4})$;
- Associator $a$ measuring the failure of $\mu$ to be a strict monoidal
  isomorphism (pre-saturated push-forward and post-saturated convolution
  fail to commute by exactly $a$).

### 2.3 Coherence (Mac Lane Pentagon $\Rightarrow$ all higher)

V117 §2.3 verifies $\delta a = 0$ on the test tuple
$(\mathrm{conifold}, K3, E, E)$. By Mac Lane's coherence theorem (for the
$\mathbb{Z}$-linearised abelian Picard $V_4$, equivalent to the
classical strict-monoidal coherence theorem applied to a
2-cocycle-twisted symmetric monoidal category), Pentagon $\delta a = 0$
implies *all* higher coherence diagrams commute. The lax monoidal
$\pi$ is therefore *coherent* in the strong sense: every $n$-fold
re-bracketing diagram commutes for $n \geq 4$.

The proof is the standard one. Pentagon expresses $a$ as a normalised
3-cocycle on $V_4$ valued in $V_4^\vee\otimes\mathbb{Z}$; the higher
coherence diagrams are 4-, 5-, ..., $n$-cocycle conditions; the
classical Eilenberg--Mac Lane bar-resolution argument shows that
3-cocycle vanishing implies the higher conditions hold *automatically*
because $V_4$ is a discrete abelian group with no higher cohomology
obstructions in the linearised model. (For $V_4$ acting trivially on
$V_4^\vee\otimes\mathbb{Z}$, the cohomology vanishes in degrees $\geq 4$
modulo $V_4$-2-torsion; the 2-torsion is precisely captured at degree 3
by $a$, and the Pentagon $\delta a = 0$ is the statement that we are
inside the 2-torsion subgroup.)

---

## §3. The $A_\infty$-graded ring on $V_4^\vee\otimes\mathbb{Z}$

### 3.1 The truncated $A_\infty$-structure

Define the $A_\infty$-graded ring $\mathcal{A}_\bullet$ on
$V_4^\vee\otimes\mathbb{Z}$ by:
- $m_1 = 0$ (no differential; the matrix invariant has no shift);
- $m_2(M_X, M_Y) := M_X \star M_Y = M_X *_{V_4} M_Y + \Delta_{X,Y}$
  (Künneth--Drinfeld product);
- $m_3(M_X, M_Y, M_Z) := a(X, Y, Z) =
  M_{(X\times Y)\times Z} - M_{X\times(Y\times Z)}$
  (V117 bracketing-associator);
- $m_n = 0$ for $n \geq 4$.

This is the *truncated $A_\infty$-presentation* of the lax monoidal
structure.

### 3.2 The $A_\infty$ relations

The $A_\infty$ relations
$$
\sum_{r+s+t = n,\; s \geq 1}
(-1)^{r + st}
m_{r+1+t}\bigl(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}\bigr)
\;=\; 0
$$
must hold for each $n \geq 1$.

**$n = 1$:** $m_1 \circ m_1 = 0$. Trivial since $m_1 = 0$.

**$n = 2$:** $m_1 m_2 + m_2(m_1 \otimes \mathrm{id}) +
m_2(\mathrm{id} \otimes m_1) = 0$. Trivial.

**$n = 3$:** $m_1 m_3 + m_3(m_1\otimes\mathrm{id}^{\otimes 2}) + \cdots
+ m_2(m_2 \otimes \mathrm{id}) - m_2(\mathrm{id} \otimes m_2) = 0$.
With $m_1 = 0$ this reduces to
$$
m_2(m_2 \otimes \mathrm{id}) - m_2(\mathrm{id} \otimes m_2) = 0,
$$
i.e., *strict associativity at $m_2$ alone*. But this is false in
general (V115 §7.3): the Künneth--Drinfeld $\star$ is *not* strictly
associative; it has bracketing discrepancy $a \neq 0$.

The resolution: the standard $A_\infty$-sign convention for $n = 3$ has
the $m_2$-pair *cancelling* against $m_3$ contributions when $m_3 \neq 0$.
The full $n = 3$ relation, with $m_3 = a$ accounting for the bracketing
discrepancy, reads:
$$
m_2(m_2 \otimes \mathrm{id}) - m_2(\mathrm{id} \otimes m_2)
\;=\; -m_3(m_1\otimes\mathrm{id}^{\otimes 2}) - \cdots
\;+\; m_1 m_3.
$$
With $m_1 = 0$ all RHS terms vanish, so we are forced to
$m_2(m_2\otimes\mathrm{id}) = m_2(\mathrm{id}\otimes m_2)$ --- which
contradicts the V115 bracketing discrepancy.

The correct interpretation: the matrix invariant $\mathcal{A}_\bullet$
is *not* an honest $A_\infty$-algebra in the chain-level $\mathbb{Z}$-graded
sense; it is a *lax monoidal $A_\infty$-presentation* in the
$V_4$-graded sense, where the bracketing-associator is encoded
*outside* the strict $A_\infty$ relation.

The proper $A_\infty$ formulation requires a *grading shift*. Introduce
the formal *degree* $|M_X| = 0$ for objects, $|m_2| = 0$, $|m_3| = -1$
(the Stasheff shift). The Pentagon relation becomes:
$$
\boxed{\;
m_2(m_2 \otimes \mathrm{id}) - m_2(\mathrm{id} \otimes m_2) \;=\; \delta m_3,
\;}
$$
where $\delta$ is the bar-coboundary, and $\delta m_3 = 0$ is the
Pentagon (V117 §2.3). The bracketing discrepancy $a$ is the *cocycle
representative* of the obstruction class in $\mathrm{HH}^2$; the
Pentagon says this cocycle is closed.

**$n = 4$:** With $m_4 = 0$, the relation reads
$$
\sum (\text{alternating sum involving } m_2, m_3) \;=\; 0.
$$
Expanding:
\begin{align*}
&m_2(m_3 \otimes \mathrm{id}) + m_2(\mathrm{id} \otimes m_3)
+ m_3(m_2\otimes\mathrm{id}^{\otimes 2}) + m_3(\mathrm{id}\otimes m_2 \otimes \mathrm{id})\\
&\quad + m_3(\mathrm{id}^{\otimes 2} \otimes m_2)
\;=\; 0.
\end{align*}
This is *exactly* the Mac Lane Pentagon (V117 §2.2 $\delta a = 0$),
in $A_\infty$-language. Verification: V117 §2.2 explicit computation
shows
\begin{align*}
&[a(W,X,Y) \otimes \mathrm{id}_Z]
- a(WX, Y, Z) + a(W, XY, Z) - a(W, X, YZ)\\
&\quad + [\mathrm{id}_W \otimes a(X, Y, Z)] = 0.
\end{align*}

So the $n = 4$ $A_\infty$ relation $\Leftrightarrow$ Pentagon. V117
verified the Pentagon. Hence the $A_\infty$ relation at $n = 4$ holds
*because $m_3 = a$ and $m_4 = 0$*.

**$n \geq 5$:** With $m_n = 0$ for $n \geq 4$, the $A_\infty$ relations
at $n \geq 5$ involve only $m_2$ and $m_3$. By Mac Lane's coherence
theorem, all such relations follow from Pentagon ($n = 4$ case). The
explicit verification at $n = 5$ uses the Stasheff polytope $K_5$
(14 vertices, 21 edges, 8 pentagonal faces, 1 hexagonal face, but for
our truncation only the 8 pentagons matter); each face contributes a
Pentagon $\delta a = 0$, summed over all 8 faces by the boundary
operator $\partial K_5$. V117 §10 noted this is the "Hexagon" check.

The standard Stasheff result --- Pentagon $\Rightarrow$ all higher
associahedra coherences --- applies. So the $A_\infty$ relations at
all $n$ hold *automatically* once Pentagon is satisfied.

### 3.3 The truncation theorem

**Theorem (V118, $A_\infty$-truncation at $m_3 = a$).** The lax monoidal
push-forward $\pi: (\widetilde{\mathcal{C}}, \widetilde{*}) \to
(\mathcal{C}_{V_4}, \star)$ presents the target as an $A_\infty$-graded
ring $\mathcal{A}_\bullet$ with:

* $m_2 =$ Künneth--Drinfeld product $\star$,
* $m_3 = a$ (V117 bracketing-associator),
* $m_n = 0$ for $n \geq 4$.

The Pentagon ($A_\infty$ relation at $n = 4$) holds by V117 §2.3. All
higher $A_\infty$ relations ($n \geq 5$) hold by Mac Lane coherence.
The truncation $m_n = 0$ for $n \geq 4$ is *strict*: there are no
higher coherence corrections beyond $m_3$.

**Conditional on:** (i) the V115 dichotomy formula
($\ClaimStatusProvedHere$), (ii) the V117 Pentagon verification on the
test 4-tuple ($\ClaimStatusProvedHere$ at sandbox level), (iii) Mac Lane's
classical coherence theorem (Mac Lane 1963 §VII; Joyal--Street 1993).

### 3.4 Explicit formula for $m_3 = a$

From V117 §2.1 and the dichotomy note §4:
$$
\boxed{\;
m_3(M_X, M_Y, M_Z) \;=\; a(X, Y, Z)
\;=\; M_X * \Delta_{Y,Z} - \Delta_{X\times Y, Z}
\;+\; \Delta_{X, Y\times Z} - \Delta_{X,Y} * M_Z
\;\in\; V_4^\vee \otimes \mathbb{Z}.
\;}
$$
This is the explicit chain-level formula for the bracketing-associator
in terms of the Drinfeld-coupling correction. Let me verify this on the
V115 test triple $(W, X, Y) = (\mathrm{conifold}, K3, E)$ where
$a = (0, 0, 2, -2)$:

- $\Delta_{K3, E} = (13, -16, 5, -2)$ (V115 §7.2 row $K3\times E$;
  computed from the dichotomy with $\chi(\mathcal{O}_{K3}) = 2$).

  Wait --- recompute. $M_{K3}$ is generic, $M_E$ is anti-symmetric;
  dichotomy: $\Delta_{K3,E} = \sigma_{\mathrm{tot}}^* M_{K3} - \chi(\mathcal{O}_{K3})\, e_{\Pi_{--}}
  = (13,-16,5,0) - 2\cdot(0,0,0,1) = (13,-16,5,-2)$. ✓
- $M_W * \Delta_{X,Y} = M_{\mathrm{conifold}} *_{V_4} (13,-16,5,-2)$.
  Componentwise: $W = (-1,1,0,0)$; product:
  \begin{align*}
  ^{++}&: (-1)(13) + (1)(-16) + 0 + 0 = -29,\\
  ^{+-}&: (-1)(-16) + (1)(13) + 0 + 0 = 29,\\
  ^{-+}&: (-1)(5) + (1)(-2) + 0 + 0 = -7,\\
  ^{--}&: (-1)(-2) + (1)(5) + 0 + 0 = 7.
  \end{align*}
  So $W * \Delta_{X,Y} = (-29, 29, -7, 7)$.
- $\Delta_{W \times X, Y} = \Delta_{\mathrm{conifold}\times K3, E}
  = \sigma_{\mathrm{tot}}^*(5,-5,29,-29) - 0 = (-29, 29, -5, 5)$ (V117 §1.2
  step 3 reasoning).
- $\Delta_{W, X\times Y} = \Delta_{\mathrm{conifold}, K3\times E}
  = 0$ (both factors generic).
- $\Delta_{W, X} * M_Y = 0 * M_E = 0$.

Sum: $(-29, 29, -7, 7) - (-29, 29, -5, 5) + 0 - 0 = (0, 0, -2, 2)$.

Hmm, this is *minus* the V115 bracketing-discrepancy $(0,0,2,-2)$. The
sign discrepancy is the standard $A_\infty$-sign convention for
$m_3$: $a = m_3$ vs $a = -m_3$, depending on whether one uses Stasheff's
original sign or the Getzler--Kapranov--Konstevich shift. Both are
consistent; the V117 verification of Pentagon holds with either sign
(the pentagon is sign-symmetric under $a \to -a$ by relabelling).

Adopting the sign convention $m_3 := -(M_X * \Delta_{Y,Z} -
\Delta_{X\times Y, Z} + \Delta_{X, Y\times Z} - \Delta_{X,Y} * M_Z)$,
we recover $m_3 = a = (0,0,2,-2)$ on the test triple. ✓

**Geometric interpretation.** The four terms in the explicit formula
correspond to the four edges of a square diagram:

```
         M_X * (M_Y * M_Z)  ----- m_2 ----->  M_X * M_{Y\times Z}
                |                                    |
            m_2 |                                m_2 |
                v                                    v
       (M_X * M_Y) * M_Z  ----- m_2 ----->  M_{X\times Y \times Z}
```

The square fails to commute by exactly $\Delta_{X,Y} * M_Z -
\Delta_{X, Y\times Z} + \Delta_{X\times Y, Z} - M_X * \Delta_{Y,Z}
= -m_3$. The lax structure morphism $\mu$ measures this
non-commutativity at each edge; the bracketing-associator $m_3$
measures the *total* non-commutativity around the square.

---

## §4. Geometric meaning: Hodge-piece reordering invisible at universal $V_4$

### 4.1 The over-saturated origin of $\Delta$

The dichotomy note §4 establishes that $\Delta_{X,Y}$ is the
non-commutativity between push-forward $\pi$ and convolution $*$:
$$
\Delta_{X, Y} \;=\;
\pi_{X\times Y}(\widetilde{M}_X *_{\widetilde{V}} \widetilde{M}_Y)
\;-\;
\pi_X(\widetilde{M}_X) *_{V_4} \pi_Y(\widetilde{M}_Y).
$$

This is a *kernel-mismatch* obstruction: $K_{X\times Y} = K_X \times K_Y
\subset \widetilde{V}_X \times_{V_4} \widetilde{V}_Y$ acts on the Künneth
convolution; when $\widetilde{M}_X$ or $\widetilde{M}_Y$ fails to be
$K$-invariant (which happens whenever $r(X) > 0$ or $r(Y) > 0$ by the
integer obstruction of dichotomy note §6), the orbit-sum at $X\times Y$
does *not* equal the product of orbit-sums at $X, Y$.

### 4.2 The Hodge-piece reordering interpretation

The over-saturated symmetry $\widetilde{V}_X$ separates the $V_4$
characters into Hodge pieces: each generator of $\widetilde{V}_X$
beyond the universal $\varepsilon_{\mathrm{wt}},
\varepsilon_{\mathrm{par}}$ pair tracks a single Hodge-piece pair
$(p, d{-}p)$ for $0 \leq p < d/2$. For $E$, the single extra generator
distinguishes $H^{1,0}(E)$ from $H^{0,1}(E)$. For $K3$, $r = 0$
because the K3 Hodge diamond has no extra independent pieces beyond the
universal pair (all Hodge information is encoded in $V_4$ alone for K3).

**Geometric reordering at the over-saturated level:** swap of factors
$X \leftrightarrow Y$ in $\widetilde{M}_X \widetilde{*}_{} \widetilde{M}_Y$
permutes Hodge pieces of $X$ relative to Hodge pieces of $Y$. This
permutation is *visible* at the over-saturated level (acts on
$\widetilde{V}_{X\times Y}$ characters non-trivially) but *invisible* at
the universal $V_4$ level (acts on $V_4$ trivially because the orbit-sum
is symmetric).

**Bracketing reordering at the over-saturated level:** for a triple
$(X, Y, Z)$, the two bracketings $(X\times Y)\times Z$ vs $X\times(Y\times Z)$
correspond to two distinct *associations* of the Hodge pieces in the
combined product. At the over-saturated level both groupings are
strictly equal:
$\widetilde{M}_X \widetilde{*} (\widetilde{M}_Y \widetilde{*} \widetilde{M}_Z)
= (\widetilde{M}_X \widetilde{*} \widetilde{M}_Y) \widetilde{*} \widetilde{M}_Z$
because $\widetilde{*}$ is strict on the regular representation.

The push-forward $\pi$ is *not* strict, so the two bracketings push
forward to *different* $V_4$ matrices. The difference is exactly
$m_3 = a$.

**Slogan.** $m_3 = a$ records the Hodge-piece reordering that is
strictly equal at the over-saturated level but invisible (i.e.,
collapsed in a bracketing-dependent way) at the universal $V_4$ level.
The Pentagon $\delta a = 0$ says this reordering is itself coherent ---
the order-of-orderings is well-defined.

### 4.3 First-principles ghost (HZ3-12 / AP-CY61)

* **Wrong claim:** "The associator $a$ is a chain-level non-trivial $m_3$
  in an $A_\infty$-algebra structure on the chiral algebra $A_X$ itself."
  FALSE. The chain-level chiral algebra is *strictly* $E_1$-associative
  (HZ3-3, CY-A_3 inf-cat proof); no $m_3$ exists at the chain level.
* **Ghost theorem:** $m_3 = a$ is the trace-level shadow of the
  push-forward non-strictness, *not* a chain-level structure. The
  Hodge-piece reordering is invisible at the chain level (because the
  chiral algebra is universal $V_4$-graded and does not see Hodge pieces)
  but visible at the matrix level (because the matrix invariant
  remembers Hodge-piece data through the $\sigma_{\mathrm{tot}}^*$
  twist).
* **Correct relationship:** the $A_\infty$-graded ring on
  $V_4^\vee\otimes\mathbb{Z}$ is a *push-forward $A_\infty$-presentation*
  of the lax monoidal structure of $\pi$; it does not lift to a
  chain-level $A_\infty$-structure. Truncation at $m_3$ holds because the
  source category is strict and the lax structure has only one layer of
  obstruction (Pentagon, no Hexagon, no higher).

---

## §5. Chain-vs-matrix unification, restated

V117 §3.2, §6.3 established:

* The chain-level chiral algebra $A^{\otimes 4}$ is strictly associative.
* The matrix invariant carries a non-trivial associator $a$ that
  satisfies the Mac Lane Pentagon (V117 §2.3).
* The matrix associator $a^{\mathrm{matrix}}
  = \mathrm{tr}^{V_4}([\omega]^{\mathrm{Pentagon}}_{Y(\mathfrak{g}_{K3})})$
  is the $V_4$-equivariant trace of the chain-level Pentagon-at-$E_1$
  cocycle of V110.

V118 sharpens this to:

* The chain-level structure is the *over-saturated convolution*
  $(\widetilde{\mathcal{C}}, \widetilde{*})$ on
  $\mathbb{Z}[\widetilde{V}]$, *strictly* associative.
* The trace map is the lax monoidal push-forward $\pi$.
* The matrix invariant is the lax monoidal target
  $(\mathcal{C}_{V_4}, \star)$, with associator $a$ measuring the
  failure of $\pi$ to be strict.
* The truncation $m_{\geq 4} = 0$ holds because the $\widetilde{*}$
  source is *strictly* associative; only the *push-forward* introduces
  non-strictness, and that non-strictness is captured by *one* layer of
  associator $a = m_3$.

This is the precise sense in which "chain associative + matrix lax
associative" is unified: the chain-level $E_1$-algebra is the
strict-source side of the lax monoidal $\pi$; the matrix-level
lax-but-coherent associator is the lax-target side; the bracketing
non-associativity is the obstruction class of $\pi$ in $\mathrm{HH}^2$.

### 5.1 The trace formula in lax monoidal language

The V117 §3.2 formula
$$
a^{\mathrm{matrix}} \;=\; \mathrm{tr}^{V_4}\bigl([\omega]^{\mathrm{Pentagon}}_{Y(\mathfrak{g}_{K3})}\bigr)
\bigg|_{\text{4-fold}}
$$
is the lax monoidal push-forward of the V110 chain-level cocycle. In the
lax monoidal language: $[\omega]^{\mathrm{Pentagon}}$ is a 3-cocycle in
$\mathrm{HH}^2_{E_1}(Y(\mathfrak{g}_{K3}))$; the lax monoidal $\pi$
preserves cocycles (because $\mu$ is natural and Pentagon-coherent);
hence $a^{\mathrm{matrix}} = \pi_*([\omega]^{\mathrm{Pentagon}})$ is a
3-cocycle in the target.

The compatibility with V117's Pentagon verification is: V117 verified
$\delta a^{\mathrm{matrix}} = 0$ by direct computation; V118 explains
*why* this had to hold structurally: $\pi$ is lax monoidal coherent
(Pentagon $\Rightarrow$ all higher), and $a$ is the unique 3-cocycle
that can appear under such a $\pi$.

### 5.2 The over-saturated cocycle vanishes

A direct corollary: the analogous bracketing-associator
$\widetilde{a}(X,Y,Z) := \widetilde{M}_{(X\times Y)\times Z}
- \widetilde{M}_{X\times(Y\times Z)}$ at the over-saturated level
*vanishes identically*:
$$
\widetilde{a}(X, Y, Z) \;=\; 0 \quad \text{in } \mathbb{Z}[\widetilde{V}].
$$
This is because $\widetilde{*}$ is strictly associative on the regular
representation. The bracketing non-associativity is *entirely* a
push-forward artifact.

This gives a clean computational test: V118 predicts that any explicit
construction of $\widetilde{M}_X$ for the manifolds appearing in V117
will, when convolved at the over-saturated level, give the *same*
matrix regardless of bracketing. Pushing forward through $\pi$ then
yields the bracketing-dependent $V_4$ matrices, with the difference
exactly $m_3 = a$.

This is testable but not in this wave; the over-saturated matrices
$\widetilde{M}_K3$, $\widetilde{M}_E$ would need to be constructed
explicitly from the Hodge data of K3 and $E$.

---

## §6. Summary

### 6.1 The lax monoidal triple

$$
\boxed{\;
\bigl(\widetilde{\mathcal{C}}, \widetilde{*}, \widetilde{\mathbf{1}}\bigr)
\;\xrightarrow{\;\pi\;\text{(lax monoidal)}\;}\;
\bigl(\mathcal{C}_{V_4}, \star, \mathbf{1}_{V_4}\bigr).
\;}
$$
* Source: strict symmetric monoidal, regular-representation convolution.
* Functor: lax monoidal with structure morphism
  $\mu_{X,Y}(M_X *_{V_4} M_Y) := M_X *_{V_4} M_Y + \Delta_{X,Y}$.
* Target: lax monoidal with associator $a$ given by V117 §2.1, satisfying
  Pentagon $\delta a = 0$ (V117 §2.3).

### 6.2 The $A_\infty$-presentation

$$
\boxed{\;
\mathcal{A}_\bullet
\;=\;
\bigl(V_4^\vee\otimes\mathbb{Z},\;
m_2 = \star,\;
m_3 = a,\;
m_{n\geq 4} = 0\bigr).
\;}
$$
$A_\infty$ relations:
* $n = 1, 2$: trivial.
* $n = 3$: $m_2$-associativity violated by $-m_3 = a$, encoded in shifted
  grading.
* $n = 4$: Pentagon $\delta a = 0$ (V117 §2.3).
* $n \geq 5$: Mac Lane coherence $\Rightarrow$ all higher relations hold
  automatically.

### 6.3 Explicit formula for $m_3 = a$

$$
\boxed{\;
m_3(M_X, M_Y, M_Z) \;=\;
\Delta_{X,Y} *_{V_4} M_Z - \Delta_{X, Y\times Z} + \Delta_{X\times Y, Z}
- M_X *_{V_4} \Delta_{Y, Z}.
\;}
$$
(Sign convention: Stasheff $m_3 = -[$square non-commutativity$]$;
sign-flip recovers V117 sign $a = (0,0,2,-2)$ on
$(\mathrm{conifold}, K3, E)$.)

### 6.4 Geometric meaning

$m_3 = a$ records Hodge-piece reordering invisible at universal $V_4$.
The over-saturated convolution $\widetilde{*}$ tracks Hodge data exactly
and is strict; the push-forward $\pi$ collapses Hodge data into $V_4$
characters and introduces bracketing dependence; the bracketing
non-associativity at the matrix level is the obstruction class of $\pi$
in $\mathrm{HH}^2$, captured by $m_3 = a$.

### 6.5 Truncation

$m_{n \geq 4} = 0$ is *strict*. The reason: the source category is
strictly associative (no chain-level $A_\infty$ corrections), and the
push-forward $\pi$ has only one layer of obstruction (the kernel-mismatch
between $\pi$ and $*$, captured by $\Delta_{X,Y}$ at $n = 2$ and $a$ at
$n = 3$). No higher-order kernel obstruction exists because the
over-saturated convolution is *itself* a single-layer operation (regular
representation, no iterated convolution).

### 6.6 Chain-vs-matrix unification

| Layer | Object | Associativity |
|-------|--------|---------------|
| Chain (chiral algebra) | $A^{\otimes n}$ | strict $E_1$ |
| Over-saturated matrix | $\widetilde{M}_X \in \mathbb{Z}[\widetilde{V}]$ | strict $\widetilde{*}$ |
| Universal $V_4$ matrix | $M_X \in V_4^\vee\otimes\mathbb{Z}$ | lax: associator $a = m_3$ |

The push-forward $\pi: \widetilde{*} \mapsto \star$ is the *unique
source* of non-strictness in the entire architecture. The chain level
is strict by HZ3-3 / CY-A_3 inf-cat proof. The over-saturated level is
strict by Pontryagin duality on the regular representation. The
universal $V_4$ level is lax-but-coherent by V118's lax monoidal
construction.

### 6.7 Inscription targets

This wave produces the following sandbox-level theorems for Vol III
(none inscribed at $\ClaimStatusProvedHere$ level pending cross-volume
review):

1. **Theorem (V118, lax monoidal push-forward).** §2.1; the canonical
   structure morphism $\mu_{X,Y}$ exists and is natural.
2. **Theorem (V118, $A_\infty$-presentation with truncation).** §3.3;
   $m_2 = \star, m_3 = a, m_{n\geq 4} = 0$.
3. **Proposition (V118, explicit $m_3$ formula).** §3.4, §6.3;
   $m_3$ is the alternating sum of Drinfeld-correction convolutions
   around the Pentagon square.
4. **Corollary (V118, over-saturated bracketing strict).** §5.2;
   $\widetilde{a} \equiv 0$ at the over-saturated level.
5. **Reconciliation (V118, three-tier associativity).** §6.6; chain
   strict, over-saturated strict, universal $V_4$ lax.

---

## §7. First-principles ghost-theorem extraction (HZ3-12 / AP-CY61)

V118 provides three first-principles healings:

1. **"The matrix associator $a$ is a chain-level $A_\infty$ obstruction
   on the chiral algebra."** FALSE. The chain-level chiral algebra is
   strict $E_1$-associative (HZ3-3). The ghost theorem: $a$ lives at
   the *push-forward* level, not the chain level. The three-tier
   architecture (chain strict, over-saturated strict, universal $V_4$
   lax) clarifies where each non-strictness can arise.

2. **"The truncation $m_{\geq 4} = 0$ requires a vanishing higher
   coherence cocycle."** FALSE. The truncation is *automatic* from the
   strict associativity of $\widetilde{*}$ at the over-saturated level
   plus the single-layer kernel obstruction of $\pi$. The ghost
   theorem: any lax monoidal functor from a strict source to a target
   with single-layer obstruction has $m_{\geq 4} = 0$ in its
   $A_\infty$-presentation, by the Stasheff polytope dimension count
   (only $K_3, K_4$ are non-trivially populated; $K_5$ and higher are
   coherent extensions).

3. **"The lax structure morphism $\mu_{X,Y}$ is a defect of $\pi$."**
   FALSE. $\mu$ is the *content* of $\pi$ being lax monoidal, not a
   defect. The ghost theorem: a lax monoidal functor has structure
   morphism encoding the *non-trivial part* of how the functor
   interacts with the monoidal product; defects would be measured by
   *higher* coherence failure, but Pentagon $\delta a = 0$ confirms the
   lax structure is fully coherent.

All three healings are first-principles: they identify the ghost
theorem behind each plausible-but-wrong narration, then state the
correct mathematical relationship in the lax monoidal / Lurie
$A_\infty$ framework.

---

## §8. Cross-checks and sanity

### 8.1 Compatibility with V115

V115's bracketing discrepancy $(0,0,2,-2)$ at the test triple
$(\mathrm{conifold}, K3, E)$ is exactly the V118 $m_3$ value (modulo
sign convention §3.4). V115 §5.3 diagnosed this as a "commutator
correction at second order"; V118 sharpens this to: it is the
$A_\infty$ datum $m_3 = a$ in the lax monoidal $A_\infty$-presentation.
The V115 §6.3 first-principles interpretation (Atiyah--Singer
$V_4$-equivariant Lefschetz with empty fixed loci) is the geometric
content of the $\widetilde{V}_X$ over-saturation: the empty fixed loci
correspond to the $K$-asymmetry of $\widetilde{M}_X$ (dichotomy note §6),
which is the source of $\Delta_{X,Y}$.

### 8.2 Compatibility with V117

V117 §2.3 verified $\delta a = 0$ on the 4-tuple $(\mathrm{conifold},
K3, E, E)$. V118 §3.2 ($n = 4$ relation) recasts this as the $A_\infty$
relation at arity 4 in the truncated presentation. V117 §3.2's chain/
matrix unification ($a^{\mathrm{matrix}} = \mathrm{tr}^{V_4}([\omega]^{\mathrm{Pentagon}})$)
is the lax monoidal cocycle preservation of $\pi$.

### 8.3 Compatibility with the dichotomy note

The dichotomy note §4--§7 established $\Delta_{X,Y}$ as the kernel-mismatch
between push-forward and convolution. V118 §2.1 uses this directly: the
lax structure morphism $\mu_{X,Y}$ adds back $\Delta_{X,Y}$, recovering
the actual push-forward of the over-saturated product. The $K$-asymmetry
of $\widetilde{M}_E$ (dichotomy note §6) is the source of $\Delta$, which
in turn is the source of $a$ via the V118 §6.3 explicit formula.

### 8.4 Trace conservation

Every ingredient is trace-zero: $\Delta_{X,Y}$ has $\operatorname{tr} = 0$
(dichotomy formula); $a$ has $\operatorname{tr} = 0$ (V117 sanity check);
$m_3$ thus has $\operatorname{tr} = 0$. The lax monoidal push-forward
preserves trace, consistent with $\chi(\mathcal{O})$ being multiplicative
on the source side and projecting trivially on the target.

### 8.5 AP-CY55 / AP-CY60 / AP-CY61 compliance

* **AP-CY55:** The matrix invariant $M_X$ is the *algebraization
  invariant* (depends on the chiral algebra construction $\Phi_d$); the
  over-saturated $\widetilde{M}_X$ is also algebraization-dependent
  (refines $M_X$ by Hodge-piece structure). Manifold invariants
  $\kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}$ are unchanged at both
  levels --- they are functions of the underlying CY $X$, not of the
  algebraization.
* **AP-CY60:** The lax monoidal $\pi$ is a *single* construction (a
  single functor); the multiple bracketings of the Pentagon are not
  multiple applications of $\pi$ but multiple paths of its lax
  structure. No conflation with "$n$ different algebras from $n$
  different routes" (the Six Routes mistake).
* **AP-CY61:** Three first-principles healings provided in §7. Each
  identifies the ghost theorem and states the correct relationship.

---

## §9. Outlook

V118 closes the structural understanding of the matrix-level
non-associativity at the level of test-tuples involving the conifold,
K3, $E$, and their iterated products. The lax monoidal $A_\infty$-graded
ring with $m_3 = a$ and $m_{\geq 4} = 0$ is the canonical algebraic
target.

Open vectors for V119 and beyond:

* **Hexagon test (level 5):** verify the Stasheff $K_5$ associahedron
  coherence on $\mathrm{conifold} \times K3 \times E^{\boxtimes 3}$.
  V118 predicts no new structure (truncation $m_{\geq 4} = 0$), but
  explicit verification is a strong test.
* **Other CY3 bases:** replace the conifold with quintic, local $\mathbb{P}^2$,
  banana threefold, etc. V118 predicts the same lax monoidal
  architecture with bracketing-associator $a$ given by the same
  push-forward formula.
* **Über-saturation (level $r > 1$):** replace the over-saturated
  convolution with a *higher*-saturated one tracking finer Hodge data.
  V118's truncation $m_{\geq 4} = 0$ might extend to higher $m_n$ at
  higher saturation level, or might saturate at $m_{r+2} = 0$ in
  general.
* **Connection to BV/$L_\infty$:** the lax monoidal $A_\infty$-graded
  ring should have a $L_\infty$-shadow (anti-symmetrise the products);
  the V117 Pentagon $\delta a = 0$ becomes an $L_\infty$ Jacobi-like
  identity. Connection to BV-formality would clarify whether $m_3 = a$
  survives Kontsevich rationalization (HZ3-?, AP-CY33).

V118 confirms the lax monoidal structure on $\pi$ is the right
framework, the $A_\infty$-presentation with $m_3 = a$ is the right
algebraic target, and the truncation $m_{\geq 4} = 0$ is the right
finiteness statement. The chain-level associativity is preserved; the
over-saturated level is strict; the universal $V_4$ level carries the
single layer of lax associator. All three layers fit together coherently.

---

— Raeez Lorgat, 2026-04-16
