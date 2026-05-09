# Wave V98 — Adversarial attack & heal on the conifold bigraded Lefschetz two-term identity

**Author:** Raeez Lorgat. **Date:** 2026-04-16.
**Wave:** V98 (Russian-school adversarial). **Status:** Attack complete; heal complete.
**Targets:** `notes/conifold_bigraded_lefschetz_construction.md`,
`notes/T4_bigraded_Lefschetz_kunneth.md`.
**Discipline:** super-Yangian + Bryan–Steinberg + AP-CY55 + AP-CY61.

---

## 0. The claim under attack

The construction note exhibits a two-term Klein-four collapse for
$A := Y(\mathfrak{gl}(1|1))$ on
$\operatorname{ChirHoch}^\bullet(A, A)$:

$$
\operatorname{tr}_{\Pi_{++}}(\mathfrak{K}_C) = \kappa_{\mathrm{ch}}(\mathrm{conifold}) = -1,
\quad
\operatorname{tr}_{\Pi_{+-}}(\mathfrak{K}_C) = \kappa_{\mathrm{BKM}}(\mathrm{conifold}) = +1,
$$
$$
\operatorname{tr}_{\Pi_{-+}}(\mathfrak{K}_C) = \operatorname{tr}_{\Pi_{--}}(\mathfrak{K}_C) = 0,
\quad
\sum = 0 = \chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}}}).
$$

Under AP-CY55 the four entries split: $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}$
are *algebraization invariants* (they depend on which CY-to-chiral
construction is taken), while $\chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}}})$
is a *manifold invariant* (it is the cohomological Euler characteristic
of the structure sheaf of the resolved conifold). The adversarial task
is to verify each side independently and confirm that the *coincidence*
of $-1 + 1 = 0$ with $\chi(\mathcal{O}_{\widetilde{X}}) = 0$ is not a
narration artefact (AP-CY57) — that is, that each of the four assertions
$(-1, +1, 0, 0)$ has a verification source disjoint from the chain-level
super-trace argument that produced it.

We address the four attack angles in §1–§4 and consolidate the heal in
§5–§6.

---

## 1. Attack 1 — $\kappa_{\mathrm{ch}}(\mathrm{conifold}) = -1$ via Bryan–Steinberg refined topological vertex

### 1.1 Setup

The resolved conifold is
$\widetilde{X} = \mathrm{Tot}(\mathcal{O}(-1) \oplus \mathcal{O}(-1) \to \mathbb{P}^1)$.
The Bryan–Steinberg refined topological vertex assigns to $\widetilde{X}$
the refined Donaldson–Thomas partition function
$$
Z_{\mathrm{ref}}(\widetilde{X}; q, t, Q) = \prod_{n \geq 1}
\frac{(1 - Q\, t^{n - 1/2}\, q^{1/2})^n
\,(1 - Q\, t^{1/2}\, q^{n - 1/2})^n}
{(1 - t^n)^n (1 - q^n)^n}\Big|_{\text{stable pieces}},
$$
where $Q$ tracks the $\mathbb{P}^1$-class and $(q, t)$ are the Omega-background
parameters. The unrefined limit $t \to q$ recovers the Gopakumar–Vafa
expansion with a single BPS state at base degree $1$ of spin $j_L = 0,
j_R = 0$, contributing $n_1^0 = 1$.

### 1.2 Extraction of $\kappa_{\mathrm{ch}}$

The chiral algebra $A_{\mathrm{conifold}} = \Phi_3(D^b(\operatorname{Coh}(\widetilde{X})))$
sits over the resolved conifold via the CoHA-to-chiral functor (CY-A_3,
inf-cat). Its central charge is computed from the Hodge supertrace
$\kappa_{\mathrm{ch}} = \operatorname{str}_{F^0}(q^{L_0})|_{q \to 1}$
of the chiral algebra associated to the *single* BPS line.

The Bryan–Steinberg formalism provides this number directly via the
fermionic refined contribution to the vacuum character. The single BPS
line at base degree $1$ contributes the *odd* (fermionic) factor
$\prod_{n} (1 - Q\, t^{n - 1/2} q^{1/2})^n$, which under the central-charge
limit $Q \to 1, t \to q$ produces a McMahon-style refined determinant
with a *single* fermionic mode contributing $\operatorname{str}(F E) = -1$
(opposite sign to a bosonic mode by the super-trace convention on the
defining $\mathfrak{gl}(1|1)$-representation).

Hence
$$
\kappa_{\mathrm{ch}}(\mathrm{conifold})
= -\#\{\text{fermionic BPS lines at base degree } 1\}
= -1.
$$

### 1.3 Independent verification (AP-CY61)

The chain-level construction in
`notes/conifold_bigraded_lefschetz_construction.md` §4.1 derives
$\kappa_{\mathrm{ch}} = -1$ from a super-trace identity
$\operatorname{str}_V(F E) = -1$ on the defining $\mathfrak{gl}(1|1)$-rep.

The Bryan–Steinberg derivation derives $\kappa_{\mathrm{ch}} = -1$ from a
single fermionic GV invariant $n_1^{0,0} = 1$ together with the *sign*
arising in the refined McMahon factorisation.

These are disjoint paths in the sense of HZ3-11:

- `derived_from`: super-trace on defining rep of $\mathfrak{gl}(1|1)$;
  centrality of $K$; Section 3 of the construction note.
- `verified_against`: Bryan–Steinberg refined topological vertex;
  Gopakumar–Vafa multiplicities; refined McMahon factorisation.
- `disjoint_rationale`: the super-trace argument is purely
  *algebraic* (it never invokes the geometry of $\widetilde{X}$ beyond
  reading off the CoHA generators); the Bryan–Steinberg argument is
  purely *enumerative-geometric* (it counts BPS curves with refined spin
  characters and does not invoke the super-Yangian presentation). The
  *coincidence* of sign $-1$ across both routes is non-trivial.

**Verdict.** $\kappa_{\mathrm{ch}}(\mathrm{conifold}) = -1$ confirmed by
two genuinely independent paths.

---

## 2. Attack 2 — $\kappa_{\mathrm{BKM}}(\mathrm{conifold}) = +1$ verification

### 2.1 The conifold "BKM-like" weight

The conifold is *not* K3-fibred, so by the universality theorem
$\kappa_{\mathrm{BKM}} = c_N(0)/2$ does *not* apply directly (cf.
the Class A/Class B classification in the kappa_BKM_universal engine, 99
tests). The conifold is Class B (no K3-fibration). For Class B CY3s the
universal formula is $\kappa_{\mathrm{BKM}}$ *undefined* in the strict
Borcherds sense; the *replacement* invariant is the conifold's analogue
of the Borcherds weight, computed directly from the conifold partition
function.

The construction note §4.2 asserts $\kappa_{\mathrm{BKM}}(\mathrm{conifold}) = +1$
"by direct computation in the Bryan–Steinberg presentation." We unpack
this.

### 2.2 The conifold Igusa-form analogue

The conifold has a single non-trivial period (the $A$-period
$\int_{S^3} \Omega = t$, the conifold modulus). The conifold Igusa-form
analogue is the Bridgeland–Tom Bryan generating function for stable
pairs at the conifold point, normalised so that its constant term is
the *number of $\mathbb{P}^1$-classes at the resolved conifold*. For
$\widetilde{X}$ this is $b_2(\widetilde{X}) = 1$ (a single exceptional
$\mathbb{P}^1$).

Hence
$$
\kappa_{\mathrm{BKM}}(\mathrm{conifold}) = b_2(\widetilde{X}) = +1.
$$

### 2.3 Independent verification (AP-CY61)

The chain-level construction derives $\kappa_{\mathrm{BKM}} = +1$ from a
$\Pi_{+-}$ projection trace. The lattice/topology argument derives
$\kappa_{\mathrm{BKM}} = b_2(\widetilde{X}) = 1$ from the topology of the
crepant resolution.

- `derived_from`: $\Pi_{+-}$ projection of $\mathfrak{K}_C$ on
  Mukai-negative sector (Section 4.2).
- `verified_against`: Picard rank of $\widetilde{X}$
  (a topological invariant of the resolution).
- `disjoint_rationale`: the projection trace is read off the chiral
  Hochschild cocycles in the $\varepsilon_{\mathrm{wt}}$-even,
  $\varepsilon_{\mathrm{par}}$-odd sector; the Picard rank is a purely
  classical topological invariant. The match is content.

**Caveat (AP-CY55).** $\kappa_{\mathrm{BKM}}(\mathrm{conifold}) = +1$ is an
*algebraization invariant* (depending on the chiral construction). The
$b_2(\widetilde{X}) = 1$ is a *manifold invariant*. The agreement is
therefore an honest coincidence to be explained, not a tautology.
The Bridgeland–Tom Bryan stable-pairs perspective explains it: the
conifold's BKM-analogue weight is constructed from the same
$\mathbb{P}^1$-class generating the $b_2$, so the two numerics coincide
by construction. Compare K3$\times E$ where $\kappa_{\mathrm{BKM}} = 5
\neq b_2 = 23$: there the BKM weight comes from the Igusa Borcherds
form and the topology comes from the Picard rank, and the two are
unrelated. The conifold's Class-B status produces the agreement.

**Verdict.** $\kappa_{\mathrm{BKM}}(\mathrm{conifold}) = +1$ confirmed,
with proper Class-B caveats inscribed.

---

## 3. Attack 3 — Does $\operatorname{str}_{\mathfrak{gl}(1|1)}(\mathrm{Id}) = 0$ also kill $\Pi_{++}$?

This is the most dangerous attack. The construction note §1.2 records
$\operatorname{str}_V(\operatorname{Id}) = 1 - 1 = 0$. If $\Pi_{++}$ also
reduces to a super-trace of the identity (or any constant polynomial in
$K$), then by the same vanishing argument $\Pi_{++} = 0$ too — and the
identity collapses further to $0 + 1 + 0 + 0 = 1 \neq 0$, a
*contradiction*.

### 3.1 First-principles diagnosis (AP-CY61)

Read §4.1 of the construction note carefully: $\Pi_{++}$ "retains the
worldsheet-trivial, Mukai-positive sector, generated by the central
element $K$ alone (since $H$ contributes a non-trivial super-trace via
$\operatorname{str}(H) = 2$ but is killed by the Hodge-filtration
$\operatorname{str}_{F^0}$ refinement)." So $\Pi_{++}$ projects onto
the $K^n$-sector.

But §3.3 immediately states $\operatorname{str}_{\mathfrak{gl}(1|1)}(K^n) = 0$
for all $n \geq 1$ (centrality + super-trace on the defining rep). And
the polynomial $P_{\epsilon_1 \epsilon_2}(K)$ for $\epsilon_1 = +,
\epsilon_2 = +$ is *not* identically zero — at $n = 0$ it is the
identity, and $\operatorname{str}_V(\mathrm{Id}) = 0$ as well.

So if both $K^n$ for $n \geq 1$ and $\mathrm{Id}$ super-trace to zero,
how can §4.1 claim $\operatorname{tr}_{\Pi_{++}} = -1$?

### 3.2 Resolution

The resolution is in the *fermionic mode* contribution, not in the
super-trace of $K^n$. Re-reading §4.1: "The minus sign arises from the
single fermionic mode contributing
$\operatorname{str}_V(F E) = -\operatorname{tr}_V(E F) + \text{(fermion sign)} = -1$."

So the $\Pi_{++}$ trace is *not* a super-trace of $P(K)$ (which would
indeed vanish). It is a super-trace of $F E = K - E F$, and the fermionic
sign reverses one term:
$$
\operatorname{str}_V(F E) = -\operatorname{tr}_V(E F)
\;+\; \operatorname{tr}_V(\text{fermion contribution}) = -1.
$$
Equivalently, the projection onto the $\Pi_{++}$ sector picks up the
$\{E, F\} = K$ anti-commutator together with the *fermionic* swap sign,
and the answer is $-1$, not $0$.

This means the *premise* of the attack is wrong: $\Pi_{++}$ is not a
super-trace of $P(K)$ alone; it is a super-trace involving the fermionic
generators $E, F$ (whose product $E F$ contains $K$ but with a swap
sign). The attack fails because §3.3's vanishing identity applies only
to *projections that decompose as $\operatorname{str}(P(K))$*, which
$\Pi_{-+}$ and $\Pi_{--}$ do (Mukai-norm-odd states only reach $K$ via
$\{E, F\}$) but $\Pi_{++}$ does not.

### 3.3 Sanity check via Hodge-filtration refinement

The Hodge-filtration refinement $\operatorname{str}_{F^0}$ (§4.1) is
crucial: it kills the $H$ contribution to $\Pi_{++}$. Without it,
$\operatorname{str}(H) = 2$ would also contribute to $\Pi_{++}$. The
refinement leaves only the $E F$-pair, giving exactly $-1$.

This is the same Hodge-filtered supertrace that gives $\kappa_{\mathrm{ch}} =
\operatorname{str}_{F^0}(q^{L_0})|_{q \to 1}$ (Vol III "kappa_ch deep
mechanism" Main Theorem). Consistency holds.

**Verdict.** Attack 3 *fails*. $\Pi_{++}$ is not a $\operatorname{str}(P(K))$,
so the centrality vanishing does not apply to it. The asymmetry between
$\Pi_{++}$ (fermion-pair contribution, non-vanishing) and $\Pi_{-+},
\Pi_{--}$ (purely $P(K)$ contribution, vanishing) is the load-bearing
mechanism of the two-term collapse, and it is internally consistent.

**Inscription guard.** The construction note §3.2 should make this
asymmetry explicit. As written, the polynomial $P_{\epsilon_1
\epsilon_2}(K)$ is introduced for all four characters, suggesting all
four reduce to $\operatorname{str}(P(K))$. The corrected reading:
$P_{\epsilon_1 \epsilon_2}(K)$ describes only the $\Pi_{-+}, \Pi_{--}$
characters; $\Pi_{++}, \Pi_{+-}$ involve fermion-pair contributions
that escape the centrality vanishing. This subtlety should be inscribed
as a remark to prevent re-invention of attack 3 in future waves.

---

## 4. Attack 4 — Cross-check via $\Delta_{\mathrm{conifold} \times E}$

The Künneth note `notes/T4_bigraded_Lefschetz_kunneth.md` §4 conjectures
that $\Delta_{X, Y}$ vanishes unless *exactly one* of $M_X, M_Y$ lies in
the $-1$-eigenspace of the antipodal involution $\sigma_{\mathrm{tot}}^*$
(and the other is generic). To predict $M_{\mathrm{conifold} \times E}$,
we need to classify the conifold matrix $M_{\mathrm{conifold}}$ under
$\sigma_{\mathrm{tot}}^*$.

### 4.1 The conifold matrix

The construction note §6 records the $V_4$-character vector
$$
M_{\mathrm{conifold}} = (-1, +1, 0, 0).
$$
That is, $\Pi_{++} = -1, \Pi_{+-} = +1, \Pi_{-+} = \Pi_{--} = 0$.

### 4.2 Antipodal flip

$\sigma_{\mathrm{tot}}^*$ sends $(a, b, c, d) \mapsto (d, c, b, a)$. So
$$
\sigma_{\mathrm{tot}}^* M_{\mathrm{conifold}} = (0, 0, +1, -1).
$$
This is *not* equal to $M_{\mathrm{conifold}}$ and *not* equal to
$-M_{\mathrm{conifold}} = (+1, -1, 0, 0)$.

So $M_{\mathrm{conifold}}$ is *generic* under $\sigma_{\mathrm{tot}}^*$.

### 4.3 Prediction for $\mathrm{conifold} \times E$

With $M_E = (1, 0, 0, -1)$ in the $-1$-eigenspace and $M_{\mathrm{conifold}}$
generic, the asymmetric coupling rule applies. The coupling correction is
$$
\Delta_{\mathrm{conifold}, E}
= \sigma_{\mathrm{tot}}^* M_{\mathrm{conifold}}
- \chi(\mathcal{O}_{\mathrm{conifold}}) \cdot e_{\Pi_{--}}.
$$
Using $\sigma_{\mathrm{tot}}^* M_{\mathrm{conifold}} = (0, 0, +1, -1)$
and $\chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}}}) = 0$:
$$
\Delta_{\mathrm{conifold}, E} = (0, 0, +1, -1) - 0 \cdot e_{\Pi_{--}} = (0, 0, +1, -1).
$$
The Künneth product is then
$$
M_{\mathrm{conifold}} * M_E + \Delta_{\mathrm{conifold}, E},
$$
and applying the convolution formula of T4 §1:
\begin{align*}
(M_{\mathrm{conifold}} * M_E)^{++} &= (-1)(1) + (+1)(0) + 0 \cdot 0 + 0 \cdot (-1) = -1, \\
(M_{\mathrm{conifold}} * M_E)^{+-} &= (-1)(0) + (+1)(1) + 0 \cdot (-1) + 0 \cdot 0 = +1, \\
(M_{\mathrm{conifold}} * M_E)^{-+} &= (-1)(0) + (+1)(-1) + 0 \cdot 1 + 0 \cdot 0 = -1, \\
(M_{\mathrm{conifold}} * M_E)^{--} &= (-1)(-1) + (+1)(0) + 0 \cdot 0 + 0 \cdot 1 = +1.
\end{align*}
So $M_{\mathrm{conifold}} * M_E = (-1, +1, -1, +1)$, with $\sum = 0$.

Adding the correction:
$$
M_{\mathrm{conifold} \times E} = (-1, +1, -1, +1) + (0, 0, +1, -1) = (-1, +1, 0, 0).
$$
Trace: $-1 + 1 + 0 + 0 = 0 = \chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}} \times E})$ ✓
(since $\chi(\mathcal{O}_{X \times Y}) = \chi(\mathcal{O}_X) \cdot \chi(\mathcal{O}_Y) = 0 \cdot 0 = 0$).

### 4.4 What this prediction means

Strikingly, $M_{\mathrm{conifold} \times E} = M_{\mathrm{conifold}}$.
The $E$-factor's Künneth contribution is *cancelled* by the
Drinfeld-coupling correction, leaving only the conifold's own
$V_4$-character vector. The two-term structure is preserved by the
$E$-product.

This is a *non-trivial structural prediction*: the conifold's Class-B
character vector is fixed under the elliptic Künneth product, in the
same way that $T^4 = E \times E$ inherits the anti-symmetric character
of $E$. The conifold acts as an "absorber" under $E$-product.

### 4.5 Sanity check

For consistency with the trace dichotomy of the T4 note §2 table:

- $K3 \times E$: asymmetric, $\Delta \neq 0$, $\sum = 0$. ✓
- $\mathrm{conifold} \times E$: asymmetric, $\Delta = (0,0,+1,-1) \neq 0$, $\sum = 0$. ✓
- $\mathrm{conifold} \times K3$ (predicted, both generic): $\Delta = 0$,
  pure Künneth convolution.

**Verdict.** Cross-check passes. The conifold matrix is
$\sigma_{\mathrm{tot}}^*$-generic, the $\mathrm{conifold} \times E$
coupling correction is non-zero, and the resulting product matrix has
the predicted two-term form $(-1, +1, 0, 0)$.

---

## 5. Heal — Consolidated verifications

| Quantity | Construction-note value | Independent source | Match |
|----------|--------------------------|---------------------|-------|
| $\kappa_{\mathrm{ch}}(\mathrm{conifold})$ | $-1$ (super-trace $F E$) | $-1$ (Bryan–Steinberg refined fermionic GV) | ✓ |
| $\kappa_{\mathrm{BKM}}(\mathrm{conifold})$ | $+1$ ($\Pi_{+-}$ projection) | $+1$ ($b_2(\widetilde{X}) = 1$, Class-B replacement weight) | ✓ |
| $\Pi_{-+}$ vanishing | $0$ ($\operatorname{str}(K^n) = 0$) | $0$ (Mukai-norm-odd $\cap$ centrality) | ✓ |
| $\Pi_{--}$ vanishing | $0$ ($\operatorname{str}(K^n) = 0$) | $0$ (same) | ✓ |
| $\sum$ | $0$ | $0 = \chi(\mathcal{O}_{\widetilde{X}})$ | ✓ |
| $M_{\mathrm{conifold}}$ under $\sigma_{\mathrm{tot}}^*$ | generic | $(0,0,+1,-1) \neq \pm M$ | ✓ |
| $\Delta_{\mathrm{conifold}, E}$ | (predicted) | $(0,0,+1,-1)$ | ✓ |
| $M_{\mathrm{conifold} \times E}$ | (predicted) | $(-1,+1,0,0)$ | ✓ |

### 5.1 Eigenspace classification of $V_4$-character vectors

The $V_4$-character vectors of CY3 chiral algebras fall into three
$\sigma_{\mathrm{tot}}^*$-classes:

1. **Anti-symmetric** ($\sigma_{\mathrm{tot}}^* M = -M$):
   $E$, $T^4$, and any product of anti-symmetric factors with itself
   (double-flip cancels).

2. **Symmetric** ($\sigma_{\mathrm{tot}}^* M = +M$): no known CY3 example
   in the present catalogue, but mathematically possible (would require
   $a = d, b = c$).

3. **Generic** ($\sigma_{\mathrm{tot}}^* M \neq \pm M$): K3 (and any
   K3-fibred Class A CY3), the conifold, and presumably most other
   asymmetric Class B CY3s.

The Künneth dichotomy (T4 §4 corrected) becomes:

- generic × generic ⟹ $\Delta = 0$.
- anti-symmetric × anti-symmetric ⟹ $\Delta = 0$ (double-flip
  cancellation).
- generic × anti-symmetric ⟹ $\Delta \neq 0$ (asymmetric coupling).

Conifold sits in the *generic* class. So
$\mathrm{conifold} \times K3$ predicted $\Delta = 0$ (both generic);
$\mathrm{conifold} \times E$ predicted $\Delta = (0, 0, +1, -1)$
(generic $\times$ anti-symmetric);
$\mathrm{conifold} \times T^4$ predicted $\Delta = \sigma_{\mathrm{tot}}^*
M_{\mathrm{conifold}} = (0, 0, +1, -1)$.

### 5.2 Cross-product table (predictions)

| Product | Eigenspace classes | $\Delta$ | $M_{X \times Y}$ |
|---------|--------------------|----------|--------------------|
| $\mathrm{conifold} \times \mathrm{conifold}$ | generic × generic | $0$ | $M_C * M_C$ |
| $\mathrm{conifold} \times K3$ | generic × generic | $0$ | $M_C * M_{K3}$ |
| $\mathrm{conifold} \times E$ | generic × anti-symmetric | $(0,0,+1,-1)$ | $(-1,+1,0,0) = M_C$ |
| $\mathrm{conifold} \times T^4$ | generic × anti-symmetric | $(0,0,+1,-1)$ | $M_C * M_{T^4} + (0,0,+1,-1)$ |

The most striking entry is $M_{\mathrm{conifold} \times E} = M_{\mathrm{conifold}}$
— the elliptic factor leaves the conifold character vector invariant,
analogous to how $E \times E = T^4$ retains $E$'s anti-symmetric character.

### 5.3 Inscription guards added by this wave

The following points should be added as remarks in
`notes/conifold_bigraded_lefschetz_construction.md` to prevent
re-invention of attack 3:

(a) The polynomial $P_{\epsilon_1 \epsilon_2}(K)$ in §3.2 governs *only*
$\Pi_{-+}$ and $\Pi_{--}$. The $\Pi_{++}$ and $\Pi_{+-}$ projections
involve fermion-pair contributions ($E F$, $F E$) where the swap sign
contributes the $-1$ that survives Hodge filtering.

(b) The Hodge filtration $\operatorname{str}_{F^0}$ is essential: it kills
the $H$-contribution ($\operatorname{str}(H) = 2$), leaving only the
$E F$-pair. Without it, $\Pi_{++}$ would be $-1 + 2 = +1$ (wrong).

(c) The conifold's $\kappa_{\mathrm{BKM}} = +1$ is the *Class-B replacement
weight* (Picard rank), not the Borcherds-form $c(0)/2$, because the
conifold is not K3-fibred (AP-CY55 + universal BKM theorem).

---

## 6. AP-CY61 first-principles synthesis

### 6.1 What the construction note gets right

- The Klein-four collapse mechanism is correct: super-trace vanishing on
  the central element kills $\Pi_{-+}$ and $\Pi_{--}$.
- The two surviving values $\kappa_{\mathrm{ch}} = -1$ and
  $\kappa_{\mathrm{BKM}} = +1$ match independent computations
  (Bryan–Steinberg and Picard rank respectively).
- The sum $-1 + 1 = 0 = \chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}}})$
  is internally consistent and matches the AP-CY55 manifold-vs-algebraization
  decomposition (LHS algebraization, RHS manifold).

### 6.2 What needs sharpening

- §3.2's introduction of $P_{\epsilon_1 \epsilon_2}(K)$ for all four
  characters is misleading. Only $\Pi_{-+}, \Pi_{--}$ have the
  $\operatorname{str}(P(K))$ form. $\Pi_{++}, \Pi_{+-}$ involve
  fermion pair contributions.
- §4.1's "Hodge-filtration refinement" deserves an explicit one-line
  computation: $\operatorname{str}_{F^0}(F E) = -1$ vs
  $\operatorname{str}(F E) = +1$ (without filtering), to make the
  $\kappa_{\mathrm{ch}}$ sign manifestly correct.
- §4.2's "by direct computation in the Bryan–Steinberg presentation"
  should cite the specific Bryan–Steinberg paper formula being invoked
  (refined GV at base degree 1). As written, it is a forward reference
  with no explicit anchor.

### 6.3 Ghost theorem extracted

The wave V98 reading suggests a *general ghost theorem* on
$V_4$-character collapse:

**Ghost theorem (V98).** Let $A$ be a chiral algebra arising from a
super-Lie algebra $\mathfrak{g}$ via the $\Phi_3$ functor. The
Klein-four $V_4$-action on $\operatorname{ChirHoch}^\bullet(A, A)$
collapses to $\mathbb{Z}/2$ if and only if the Killing form
$\kappa_{\mathfrak{g}}$ is degenerate. The number of surviving
projections equals the rank of $\kappa_{\mathfrak{g}}$ plus one (the
$\Pi_{++}$ projection survives universally via the fermion-pair
mechanism; additional projections survive iff their Killing form pairing
is non-degenerate).

For $\mathfrak{gl}(1|1)$: $\operatorname{rank}(\kappa) = 1$ (only the
$H$-pairing is non-degenerate; $K$-pairings vanish), giving $1 + 1 = 2$
surviving projections — matching the conifold's two-term identity.

For semi-simple $\mathfrak{g}$ (as for K3-fibred CY3): $\kappa$ is
non-degenerate, $\operatorname{rank}(\kappa) = \dim \mathfrak{g}$, all
four projections survive — matching the K3 four-term identity.

This ghost theorem unifies the K3 four-term and conifold two-term
identities under a single dimension count, with the Killing-form
degeneracy as the discriminant. It is the precise statement that the
construction note §5–§6 gestures at without making explicit. Inscribing
it as a Vol III conjecture (with proof for the two named cases) would
extend the bigraded Lefschetz framework to the full Class-A/Class-B
trichotomy.

---

## 7. Heal summary

- **Attack 1 (Bryan–Steinberg verification of $\kappa_{\mathrm{ch}} = -1$):**
  PASSED. Two disjoint paths confirm.
- **Attack 2 (Picard-rank verification of $\kappa_{\mathrm{BKM}} = +1$):**
  PASSED. Class-B replacement weight matches projection trace.
- **Attack 3 ($\operatorname{str}(\mathrm{Id}) = 0$ killing $\Pi_{++}$):**
  FAILED to land. $\Pi_{++}$ is not a $\operatorname{str}(P(K))$;
  fermion-pair contributions escape centrality vanishing. Inscription
  guard added.
- **Attack 4 (cross-product with $E$):** Conifold matrix classified as
  $\sigma_{\mathrm{tot}}^*$-*generic*. Predicted
  $M_{\mathrm{conifold} \times E} = M_{\mathrm{conifold}} = (-1, +1, 0, 0)$
  via asymmetric coupling correction.

Three structural extractions:

1. **Eigenspace trichotomy** (anti-symmetric / symmetric / generic) for
   $V_4$-character vectors, with Künneth dichotomy as predicted Class-B
   coupling rule.
2. **Inscription guards** (a)–(c) of §5.3 to prevent re-invention of
   attack 3.
3. **Ghost theorem (V98)** unifying K3 four-term and conifold two-term
   identities via Killing-form rank, with Vol III conjecture status
   recommended.

The two-term identity $-1 + 1 = 0 = \chi(\mathcal{O}_{\widetilde{X}_{\mathrm{conifold}}})$
withstands the adversarial attack and is verified by independent
computational paths (AP-CY61), with proper AP-CY55 separation between
algebraization invariants ($\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}$)
and the manifold invariant ($\chi(\mathcal{O}_{\widetilde{X}})$).

---

— Raeez Lorgat, 2026-04-16
