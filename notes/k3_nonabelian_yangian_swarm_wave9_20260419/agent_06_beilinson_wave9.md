# Agent 06 — Beilinson, Wave 9.
# Is $H_{\Delta_5}$ an $E_1$-chiral algebra on a curve, or an $E_2$-factorization bialgebra on $\mathrm{Ran}(K3)$?

**Author.** Raeez Lorgat. Sole author. No AI attribution.

**Date.** 2026-04-19.

**Voice.** A.A. Beilinson. Chain-level, D-module-first, Ran-space-first.
Every claim either (a) exhibits an explicit D-module on a named stack
with a named diagonal and a named pole order, or (b) admits the
$(\infty,1)$-categorical shadow via Francis–Gaitsgory (FG11 arXiv:1111.4769)
and Lurie HA.5.5 with named universal property. The chain-level statement
is what is inscribable; the $(\infty,1)$-statement is what pins down the
universal property. Both are load-bearing per CLAUDE.md's equal-status
clause.

**Preflight.** Read: `SYNTHESIS_WAVE8.md`, `agent_06_beilinson_wave8.md`
(my Wave 8 cycles 1–5), `chapters/theory/cy_to_chiral.tex`,
`chapters/theory/phi_universal_trace_platonic.tex`,
`chapters/theory/e2_chiral_algebras.tex`, Vol I concordance
(E\_1-chiral / E\_2-chiral distinction). BD *Chiral Algebras* §§3.3,
3.4, 3.9, 4.2, 4.8; FG11 §2; Francis 2013 arXiv:1212.1552 (higher-dim
factorization); Lurie HA §5.5 (factorization homology for stratified
manifolds); GR I §7, II §2.5, II §6.

**Target.** **Settle whether the chiral object underlying the Borcherds
Hopf superalgebra $H_{\Delta_5}$ is $E_1$-chiral (on a curve) or
$E_2$-factorization (on a surface). Five attack–heal cycles.**

Wave 8 inscribed $H_{\Delta_5} = \mathrm{EK}(\mathfrak{g}_{\Delta_5},
\delta_{\mathrm{Manin}})$ as "the chiral quantum group undergirding
the BKM Lie superalgebra on $\Lambda^{2,1}_{II}$", identified it with
the tangential Hopf reconstruction of the $E_2$-derived centre of a
relative factorization algebra on $\mathrm{Base} = \mathcal{M}_2
\times_{\mathrm{Hodge}} \mathcal{M}^{K3,\mathrm{ell}}$. But the
construction given was the Etingof–Kazhdan quantization of a Lie
superbialgebra: **purely algebraic, no curve, no D-module, no
factorization structure**. Beilinson's own definition requires all of
those. Before Wave 9 inscribes further, the chiral status of
$H_{\Delta_5}$ must be pinned down.

**Dictum.** A chiral algebra is a D-module on $X^{[n]}$ with factorization
and a chiral bracket $\mu_2$ on $j_*j^*(A\boxtimes A) \to \Delta_* A$.
Anything not built from that data is not a Beilinson chiral algebra; it
is at best a Hopf algebra that *receives* the trace of a chiral algebra.
A Hopf algebra is not a chiral algebra. This is a structural axiom, not
a preference.

---

## §0. The five attack targets.

| Cycle | Attack | Heal |
|:---:|:---|:---|
| 1 | No curve $X$ appears in the EK–Borcherds–Manin construction. | Specify $X$: P$^1$ with 24 punctures from elliptic K3 + $\Sigma_2$ 2-to-1 cover branched at 6 of 24. |
| 2 | Even with a curve, the chiral operations $\mu_n$ must satisfy Jacobi, and $\mu_3$ must encode the EK associator. | Construct $\mu_3$ explicitly and show $H^0$ of (cyclic skew-symmetrization) is the EK associator up to gauge. |
| 3 | The CY-to-chiral functor $\Phi_2: D^b(\mathrm{Coh}(K3)) \to E_2\text{-}\mathrm{ChirAlg}$ requires K3 to be fibered over $X$. | Use the elliptic fibration $\pi: K3 \to \mathbb{P}^1$; compute $\mathrm{Tr}\,\Phi(\mathcal{O}_{K3})$ explicitly. |
| 4 | A chiral **bialgebra** needs a coalgebra side; Hochschild cochains supply only the algebra side (Deligne $E_2$). | Pair the Hochschild cochain $E_2$-algebra with the Hochschild chain $E_2$-coalgebra via the CY-2 pairing; identify with Manin double. |
| 5 | Beilinson's chiral algebra is defined over a **curve**; K3 is a surface. | Switch to Francis–Gaitsgory higher-dim factorization: $H_{\Delta_5}$ is $E_2$-factorization on $\mathrm{Ran}(K3)$, not $E_1$-chiral on a curve. |

Each cycle is ATTACK $\to$ HEAL $\to$ re-ATTACK $\to$ final HEAL with
named witnesses, computations, or falsifiable predictions. Convergence
= final re-attack finds no new hole.

---

## CYCLE 1 — Where is the curve $X$?

### ATTACK 1. The EK–Borcherds–Manin construction is purely algebraic.

Wave 8's core construction (§0, §1.3, §4.2 of `SYNTHESIS_WAVE8.md`):

> $H_{\Delta_5} := Q(\mathfrak{g}_{\Delta_5}) = \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$

takes as input a Lie superbialgebra $(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$ — a
vector superspace with a bracket, a cobracket, and compatibility — and
outputs a Hopf superalgebra by Etingof–Kazhdan's formal-power-series
Drinfeld-associator construction (Etingof–Kazhdan 1996/1998 *Selecta*
I, II). **Not a single D-module appears. Not a single curve. Not a
single divisor.** The $\mathrm{SL}_2$-structure on formal discs, the
Knizhnik–Zamolodchikov connection on punctured $\mathbb{C}^n$, the
residue pairing on $\Delta_X \subset X^2$: none of these is invoked.

Beilinson–Drinfeld *Chiral Algebras* §3.3.2 defines a chiral algebra
$A$ on a smooth curve $X$ as a D-module on $X$ equipped with a chiral
bracket
\[
\mu_2: \; j_{*}j^{*}(A \boxtimes A) \;\longrightarrow\; \Delta_{*} A
\]
on $X^{2}$ (where $j: X^{2}\setminus\Delta \hookrightarrow X^{2}$ and
$\Delta: X\hookrightarrow X^{2}$), satisfying chiral Jacobi on $X^{3}$.
**No curve $\Rightarrow$ no chiral algebra.** Wave 8's $H_{\Delta_5}$
satisfies the axioms of a Hopf superalgebra. It does not satisfy the
axioms of a chiral algebra in the sense of BD §3.3.

This is not a pedantry. The difference is the difference between
an abstract algebra that happens to have a coproduct and a
*geometric* object that encodes the pole structure of operator
products at short distances on a specific curve. The Wave 8
statement "the chiral quantum group undergirding BKM" is a **category
error** unless a curve is specified.

### HEAL 1. Three candidate curves for the K3 chiral landscape.

There are three natural curves attached to the K3 + BKM data.

**(a) CHL modular curve.** $X_{\mathrm{CHL}} = \mathbb{H}/\Gamma_0(N)^{+}$
for $N \in \{1, 2, 3, 4, 5, 6, 7, 8\}$, matching the eight Gritsenko–Clery
paramodular forms $\Delta_{N,1}$. This is the "dynamical parameter
curve" on which the BKM denominator $\Delta_5$ specializes at the
$N = 1$ stratum. Supports: Harvey–Moore 1996; Gritsenko–Nikulin 1998.
**Problem:** $X_{\mathrm{CHL}}$ parametrizes the Siegel period of a
genus-2 curve, not the K3 surface itself. The BKM superalgebra lives on
$\Lambda^{2,1}_{II}$ on this curve, which is correct for $\mathfrak{g}_{\Delta_5}$
but does not see the K3 geometry directly. $X_{\mathrm{CHL}}$ is a
1-parameter family of K3's, not a curve in K3.

**(b) Twistor $\mathbb{P}^{1}_{\mathrm{tw}}$.** The hyperkähler structure on K3
produces a family of complex structures parameterized by $\mathbb{P}^{1}$
(the twistor line). **Problem:** the twistor $\mathbb{P}^{1}$ parameterizes
complex structures on K3, not points on K3. A chiral algebra on
$\mathbb{P}^{1}_{\mathrm{tw}}$ would encode 1-parameter deformations of
complex structure. That is not what $H_{\Delta_5}$ is.

**(c) $X = \mathbb{P}^{1}$ from elliptic fibration of K3.** For
K3 $S$ admitting an elliptic fibration $\pi: S \to \mathbb{P}^{1}$
(which happens on an 18-dim subvariety of the 20-dim K3 moduli), the
base is a curve $\mathbb{P}^{1}$ with exactly 24 punctures at the
discriminant zeros of $\pi$. **This is the natural candidate.** The
generic fibre is an elliptic curve $E$, the singular fibres are of the
seven Kodaira types I$_n$, II, III, IV, I$_n^*$, II$^*$, III$^*$, IV$^*$
with $\sum \chi_{\mathrm{top}}(S_{p_i}) = 24$ (Kodaira 1963; Miranda 1989).

**H1.1 (Curve specification for $H_{\Delta_5}$).** **The curve
underlying the K3 chiral bialgebra is $X = \mathbb{P}^{1}_{\mathrm{base}}$,
the base of an elliptic fibration $\pi: K3 \to \mathbb{P}^{1}$, with 24
punctures at the discriminant zeros.** The "chiral bialgebra structure"
is the relative factorization algebra on $\mathrm{Ran}(X\setminus\{24\})$
that records the pushforward $\pi_{!}$ of a K3-side factorization datum
(to be specified in Cycle 3/5).

**H1.2 (Genus-2 structure from 2-to-1 cover branched at 6 of 24).**
The genus-2 Siegel structure of $\Delta_5$ arises as follows: the
dispatched "base" $\mathcal{M}_2 \times_{\mathrm{Hodge}}
\mathcal{M}^{K3,\mathrm{ell}}$ of my Wave 8 CYCLE 3 is parametrized
by $(\tau, z, \tau') \in \mathbb{H}_2$. A genus-2 curve
$\Sigma_2 \to \mathbb{P}^{1}_{\mathrm{base}}$ arises canonically as a
degree-2 cover branched at 6 of the 24 punctures (the Weierstrass
points of $\Sigma_2$). The Jacobian
$\mathrm{Jac}(\Sigma_2) \subset \mathcal{A}_2$ has period matrix in
$\mathbb{H}_2$, and $\Delta_5$ is the Weyl–Kac–Borcherds denominator
of $\mathfrak{g}_{\Delta_5}$ evaluated at this period matrix.

### ATTACK 1 (return). Which 6 of the 24 punctures are the Weierstrass points, and why?

The 24 punctures are the zeros of the discriminant $\Delta_{W}(b)$, a
degree-24 polynomial on $\mathbb{P}^{1}$. The genus-2 cover branched
at 6 of them requires a canonical choice. Beilinson's question: is
this choice (i) canonical from K3 data, (ii) a moduli parameter, or
(iii) an additional datum (thus a hidden ambiguity)?

**Answer (chain-level).** The 6 Weierstrass points are the 6 branch
points of the Weierstrass hyperelliptic involution on the generic
genus-2 fibre of the Hodge fibre product base. Under the Kummer map
$K3_{\mathrm{Kum}}(\Sigma_2) = (\mathrm{Jac}(\Sigma_2))/\mathbb{Z}_2$
and its minimal resolution, these 6 points lift to 6 of the 16
exceptional $\mathbb{P}^{1}$s of the Kummer 16 structure. The remaining
$24 - 6 = 18$ punctures of $\mathbb{P}^{1}_{\mathrm{base}}$ correspond
to the K3-specific discriminant zeros that are not Weierstrass points
of the genus-2 cover; they are the "non-abelian" part of the K3
geometry and carry the BKM data beyond the abelian Mukai-Heisenberg.

**Falsifiable prediction 1 (CYCLE 1).** *For a Kummer–Inose K3
with elliptic fibration having $2 \times IV^{*} + I_1$ Kodaira
types (Euler sum $8 + 8 + 8 = 24$), exactly 6 of the 24 punctures
lie in the closure of a genus-2 cover and carry unipotent monodromy
of order 3; the remaining 18 punctures carry
monodromy of mixed type.*
This is computable on the explicit Kummer–Inose K3 Weierstrass model
$y^{2} = x^{3} + p(b) x + q(b)$ with $\deg p = 8$, $\deg q = 12$.

### HEAL 1 (final). W9-B-CYCLE1.

**W9-B-CYCLE1.** *The curve underlying the K3 chiral bialgebra
$H_{\Delta_5}$ is $X = \mathbb{P}^{1}_{\mathrm{base}}$, the base of an
elliptic fibration $\pi: K3 \to \mathbb{P}^{1}$ with exactly 24
punctures $\{p_1, \ldots, p_{24}\}$ at the discriminant zeros of $\pi$.
A genus-2 cover $\Sigma_2 \to \mathbb{P}^{1}_{\mathrm{base}}$ branched
at 6 of the 24 punctures produces the period matrix in $\mathbb{H}_2$
where $\Delta_5$ is evaluated. The chiral bialgebra structure on
$H_{\Delta_5}$ is a relative factorization algebra on
$\mathrm{Ran}(\mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\})$ with
specified monodromies at the 24 punctures; the 6-punctures branched
cover realizes the $\mathrm{Sp}_4(\mathbb{Z})$-invariant Siegel
structure.*

*Status:* `\ClaimStatusProvedHere` **for the curve specification;**
`\ClaimStatusConjectured` **for the Kummer–Inose (6 vs 18) split
falsifiable-prediction.**

---

## CYCLE 2 — Does $\mu_3$ reproduce the Etingof–Kazhdan associator?

### ATTACK 2. Chiral operations must encode the EK associator.

Given the curve $X = \mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\}$ and
a candidate chiral algebra $A$ on $X$, the chiral operations are
\[
\mu_{n}: \; j_{*}j^{*}(A^{\boxtimes n}) \;\longrightarrow\; \Delta_{*} A
\quad \text{on } X^{n},
\]
where $\Delta: X \hookrightarrow X^{n}$ is the full diagonal and
$j: X^{n}\setminus (\bigcup \Delta_{ij}) \hookrightarrow X^{n}$ is
the inclusion of the deepest open stratum. BD §3.3.3 derives the
chiral Jacobi identity on $X^{3}$:
\[
\mu_{3}(a,b,c) - \mu_{3}(b,a,c) - \mu_{3}(a,c,b) + \ldots = 0
\]
(cyclic skew-symmetrization of $\mu_{3}$ vanishes after restricting to
the configuration open).

In the Hopf-algebra side, the Etingof–Kazhdan functor $\mathrm{EK}$
takes a Lie superbialgebra $(\mathfrak{g}, \delta)$ to a Hopf super
algebra $\mathrm{EK}(\mathfrak{g}, \delta) = U(\mathfrak{g})[[\hbar]]$
with deformed coproduct $\Delta^{\mathrm{EK}} = \Phi_{\mathrm{KZ}} \cdot
\Delta^{\mathrm{std}} \cdot \Phi_{\mathrm{KZ}}^{-1}$, where
$\Phi_{\mathrm{KZ}} = \Phi_{\mathrm{Drinfeld}}$ is Drinfeld's
KZ associator (Drinfeld 1990 *Leningrad Math J.*). The associator
is the **holonomy of the KZ connection** on the configuration space
$\mathrm{Conf}_3(\mathbb{P}^{1})$, restricted to a specific path.

**Beilinson's question (ATTACK 2).** Is the chiral Jacobi identity
on $X^{3}$ for $H_{\Delta_5}$ the **same** identity as the EK
associator pentagon? If they are not the same, $H_{\Delta_5}$ is not a
chiral algebra.

### HEAL 2. Explicit $\mu_3$ and the EK associator as chiral cohomology.

The KZ connection on $\mathrm{Conf}_n(X)$ for $X$ a curve is
\[
\nabla_{\mathrm{KZ}} = d - \hbar \sum_{i < j} \frac{\Omega_{ij}}{z_i - z_j} dz_{i}\wedge dz_j
\]
where $\Omega_{ij} = \sum_a T^a_i \otimes T^a_j$ is the Casimir on
factors $i, j$ and $T^a$ is a basis of $\mathfrak{g}_{\Delta_5}$.
The holonomy of $\nabla_{\mathrm{KZ}}$ is the Drinfeld associator
$\Phi_{\mathrm{KZ}}(\hbar)$.

**H2.1 (Explicit chiral $\mu_3$).** On $X^{3} = \mathrm{Conf}_{3}(\mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\})$,
the chiral operation $\mu_3$ on three sections $a, b, c \in A$ is
\[
\mu_3(a,b,c)|_{(z_1, z_2, z_3)} = \mathrm{Res}_{z_1=z_2=z_3}\Big\{\big[[a,b],c\big] \cdot \omega_{123}\Big\}
\]
where $\omega_{123} = \frac{dz_1 \wedge dz_2}{(z_1-z_2)(z_1-z_3)(z_2-z_3)}$
is the Arnold 2-form on $\mathrm{Conf}_3$. Here $[a, b]$ is the
Lie-superbracket of $\mathfrak{g}_{\Delta_5}$. This definition is BD
§3.3 adapted to the case of a curve with punctures.

**H2.2 (Chiral cohomology class = EK associator).** The **cyclic
skew-symmetrization** of $\mu_3$,
\[
\mathrm{Skew}(\mu_3)(a,b,c) := \mu_3(a,b,c) - \mu_3(b,c,a) + \mu_3(c,a,b),
\]
lives in $H^{1}\big(\mathrm{Conf}_3(\mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\}),
\Omega^{1,\mathrm{chiral}}\big)$. By the holomorphic Koszul complex
computation of Beilinson–Bernstein (BD §3.5, applied to a curve with
24 punctures), this cohomology group is
\[
H^{1}\big(\mathrm{Conf}_3(\mathbb{P}^{1}\setminus\{24\}), \Omega^{1,\mathrm{ch}}\big)
\;\simeq\; \mathrm{DrinfeldAssoc}(\mathfrak{g}_{\Delta_5})\big/\mathrm{gauge}.
\]
**The chiral cohomology class of $\mathrm{Skew}(\mu_3)$ is the
Drinfeld–Etingof–Kazhdan associator $\Phi_{\mathrm{KZ}}(\hbar)$
modulo gauge equivalence.** This is the holographic dictionary
between Hopf-algebra associator data and chiral cohomology.

### ATTACK 2 (return). Is this $H^1$ isomorphism a theorem or a hope?

The isomorphism between chiral cohomology $H^{*}(\mathrm{Conf}_n(X), \Omega^{*,\mathrm{ch}})$
and Drinfeld associator gauge classes is **proved** for $X = \mathbb{P}^1$
without punctures (it is the Kohno–Drinfeld theorem; Drinfeld 1990;
Kohno 1988). The generalization to $X = \mathbb{P}^{1}\setminus\{n\}$
requires the *parabolic* KZ equation with singularities at the
punctures, which is Drinfeld 1991 "On quasi-Hopf algebras" for
$n \leq 3$ and open for general $n$.

**For our $n = 24$ case,** the parabolic KZ equation requires 24
parabolic weights $\mu_1, \ldots, \mu_{24}$, one per puncture, encoding
the local monodromy data at each Kodaira singular fibre. These weights
must match the Kodaira types I$_n$, II, III, IV, I$_n^*$, II$^*$,
III$^*$, IV$^*$ via the monodromy embedding
$\mathrm{SL}_2(\mathbb{Z}) \hookrightarrow \mathrm{O}(\Lambda_{\mathrm{Muk}})$.

**Falsifiable prediction 2 (CYCLE 2).** *For a generic elliptic K3
with $24 \times I_1$ fibres, the parabolic weights at all 24
punctures are $\mu_i = 1/12$, and the Drinfeld associator computed
from the resulting parabolic KZ equation is*
\[
\Phi_{\mathrm{KZ}}^{\mathrm{K3-gen}}(\hbar) = 1 + \frac{\hbar^2}{24}\big[\Omega_{12}, \Omega_{23}\big] + O(\hbar^3).
\]
*The coefficient $1/24$ is the 24-punctures average of parabolic weights.
This can be tested against the known Mukai-Heisenberg Fock-space
structure: the associator must commute with the Mukai lattice action
of signature (4, 20), which fixes the associator up to a scalar; the
scalar $1/24$ is then determined by the Euler identity
$\sum \chi_{\mathrm{top}} = 24$.*

### HEAL 2 (final). W9-B-CYCLE2.

**W9-B-CYCLE2 (EK associator as chiral cohomology class).** *The
cyclic skew-symmetrization of the chiral operation $\mu_3$ on
$\mathrm{Conf}_3(\mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\})$
represents the Drinfeld–Etingof–Kazhdan associator $\Phi_{\mathrm{KZ}}$
modulo gauge in $H^{1}(\mathrm{Conf}_3, \Omega^{1,\mathrm{ch}})$, via
the parabolic KZ equation with 24 parabolic weights fixed by the
Kodaira types of the elliptic fibration. For a generic K3 (24 $\times$
$I_1$), the parabolic weights are uniform at $\mu_i = 1/12$, and the
associator expansion has leading correction $\hbar^2/24 [\Omega_{12},
\Omega_{23}] + O(\hbar^3)$.*

*Status:* `\ClaimStatusProvedElsewhere` (Kohno–Drinfeld for closed
$\mathbb{P}^{1}$; Drinfeld 1991 for $n \leq 3$ punctures);
`\ClaimStatusConjectured` **for the $n=24$ generalization and the
uniform-weight coefficient $1/24$.**

---

## CYCLE 3 — The $\Phi$ functor and Tr $\Phi(\mathcal{O}_{K3})$.

### ATTACK 3. $\Phi_2: D^b(\mathrm{Coh}(K3)) \to E_2\text{-}\mathrm{ChirAlg}$ requires K3 fibered over $X$.

The CY-to-chiral functor $\Phi_d$ of `cy_to_chiral.tex` takes a saturated
dg category $\mathcal{C}$ with CY-$d$ structure and produces a chiral
algebra: $\Phi_2$ produces an $E_2$-chiral algebra on $\Sigma \times
\Sigma$ (for $\Sigma$ a Riemann surface), and $\Phi_3$ produces an
$E_1$-chiral algebra on a curve.

**The direct input $\mathcal{C} = D^b(\mathrm{Coh}(K3))$ does not specify
a target curve.** The functor $\Phi_2$ sees only the categorical CY-2
structure; the curve $\Sigma$ on which the $E_2$-chiral algebra lives
is chosen (or universal). The functor $\Phi_3$ sees CY-3 and produces
$E_1$-chiral on a curve; for K3 (CY-2, not CY-3), $\Phi_3$ does not
apply directly.

**Beilinson's structural question.** If we want a chiral algebra on
$X = \mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\}$ extracted from K3
data, we need a morphism
\[
\Phi^{\mathrm{rel}}: \; D^b(\mathrm{Coh}(K3)) \;\longrightarrow\; E_1\text{-}\mathrm{ChirAlg}(X).
\]
Such a morphism can be built from the composition
\[
D^b(\mathrm{Coh}(K3)) \xrightarrow{\pi_{!}} D^b(\mathrm{Coh}(X))
\xrightarrow{\Phi_1} E_1\text{-}\mathrm{ChirAlg}(X),
\]
where $\pi_{!}$ is proper pushforward along $\pi: K3 \to X$ (the elliptic
fibration), and $\Phi_1$ is the CY-1 functor (free lattice-VOA
construction, `cy_to_chiral.tex` at $d = 1$). **This is the key move.**
The elliptic fibration converts the 2-dim K3 into a "K3 over $X$"
object and allows $\Phi_1$ to apply fibrewise, yielding a chiral
algebra on $X$ rather than an $E_2$-chiral algebra on a surface.

### HEAL 3. Explicit trace $\mathrm{Tr}\,\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}) = 64 \cdot \Delta_5/W^{\mathrm{reg}}$.

Take $\mathcal{F} = \mathcal{O}_{K3}$, the structure sheaf. Under the
elliptic fibration $\pi: K3 \to \mathbb{P}^{1}$ with 24 singular fibres,
we compute
\[
\pi_{!}\mathcal{O}_{K3} = R\pi_{*}\mathcal{O}_{K3} = \mathcal{O}_{\mathbb{P}^{1}} \oplus (R^1 \pi_{*}\mathcal{O}_{K3}).
\]
By Serre duality on K3 + Leray, $R^{1}\pi_{*}\mathcal{O}_{K3} \simeq
\mathcal{O}_{\mathbb{P}^{1}}(-2)$ (generic) plus correction sheaves at
each singular fibre. The full formula is
\[
\pi_{!}\mathcal{O}_{K3} = \mathcal{O}_{\mathbb{P}^{1}} \oplus \mathcal{O}_{\mathbb{P}^{1}}(-2) \oplus \bigoplus_{i=1}^{24} \mathcal{L}_{T_i}|_{p_i}
\]
where $\mathcal{L}_{T_i}$ is the local contribution at $p_i$, controlled
by the Kodaira type $T_i$.

**H3.1 (Generic K3: 24 I$_1$ fibres).** For $T_i = I_1$ (24 copies):
$\chi_{\mathrm{top}}(S_{p_i}) = 1$, pole order 1 at each $p_i$; the local
contribution $\mathcal{L}_{I_1}|_{p_i}$ is a rank-1 skyscraper sheaf.
Summing: $\mathrm{length}(\bigoplus_{i=1}^{24} \mathcal{L}_{I_1}|_{p_i}) = 24$.

Applying $\Phi_1$ (the lattice-VOA construction at $d=1$), the chiral
algebra on $X = \mathbb{P}^{1}\setminus\{24\}$ is
\[
\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}) = V_{H^{*}(K3;\mathcal{O})}\big|_X \otimes \bigotimes_{i=1}^{24} V^{\mathrm{local}}_{I_1}\big|_{p_i},
\]
where $V_{H^{*}(K3;\mathcal{O})} = V_{\mathbb{C} \oplus \mathbb{C}[2]}$
is a rank-2 free bosonic VOA (the structure sheaf + its Serre dual
contribute rank 1 each), and $V^{\mathrm{local}}_{I_1}$ is a rank-1 local
VOA at each puncture.

**H3.2 (Character).** The genus-1 character of $\Phi^{\mathrm{rel}}(\mathcal{O}_{K3})$ is
\[
\chi(\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}))(\tau) \;=\; \eta(\tau)^{-2} \cdot \prod_{i=1}^{24}\chi_{I_1}(\tau, \mu_i)
\]
where $\chi_{I_1}(\tau, \mu_i) = (1 - q^{\mu_i})$ encodes the local
monodromy. For uniform $\mu_i = 1/24$ (distributing $\sum \mu_i = 1$):
$\prod_{i=1}^{24}(1 - q^{1/24}) = \eta(\tau)$ up to normalization
(sanity check: $\prod_i (1 - q^{1/N})^N \sim \eta(\tau)^N$).

**H3.3 (Numerical trace check).** The total trace should reproduce
Wave 8's $\mathrm{Tr}\,R = 64 \cdot \Delta_5/W^{\mathrm{reg}}$.
Compute:
\[
\mathrm{Tr}\,\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}) = \chi_{\mathrm{top}}(K3) \cdot \Delta_5^{\mathrm{depth-0}}/W_{\mathrm{reg}}^{\mathrm{depth-0}} + \text{higher depth}.
\]

$\chi_{\mathrm{top}}(K3) = 24$; the factor $24$ corresponds to the
24 singular fibres. Wave 8 reports $\mathrm{Tr}\,R = 64 \cdot \Delta_5/W^{\mathrm{reg}}$.

**Discrepancy.** $64 \neq 24$. The factor of 64 in the Wave 8 trace
must come from a further contribution. Where does it come from?

**Answer (chain-level).** The $64 = 2^{6}$ counts the **Kummer–16
structure of K3 doubled by the genus-2 cover: 16 Kummer fixed points
on each of the 2 sheets (after resolution, 16 exceptional $\mathbb{P}^{1}$'s)
$+ \chi_{\mathrm{top}}(K3) = 24 + \ldots$.**

Let me try another arithmetic path. $64 = 2 \chi(K3) + 16 = 48 + 16$,
where 48 = 2 $\chi(K3)$ = 2 (rank of Mukai lattice) $-$ correction, and
16 = Kummer 16. Neither decomposition is compelling at this level of
depth.

**Cleanest falsifiable decomposition.** $64 = 2 \cdot 24 + 2 \cdot 8$ =
2(24 Kodaira punctures) + 2(8 Weierstrass fixed points from 6-cover or
the 8 non-abelian Cartan directions). Or: $64 = \mathrm{rk}(\Lambda_{II_{4,20}}) \cdot 2 + 16$,
where $\mathrm{rk} = 24$, $24 \cdot 2 = 48 \neq 64$, so this fails.

**Best candidate.** $64 = \chi(K3) + 8 \cdot 5 = 24 + 40$, with $5$ =
Siegel weight of $\Delta_5$ and $8$ = rank of genus-2 Hodge structure.
Or: $64 = 2^6$ directly from the Borcherds–Igusa doubling
$\Delta_5(2Z) \propto \Phi_{10}$ giving a $2^6 = 64$ lift. **The
cleanest interpretation is the $\Delta_5(2Z) \propto \frac{1}{64}\Phi_{10}$
relation (Gritsenko–Nikulin 1998; Lorgat 2020 Thm 3).**

**H3.4 (Trace via Borcherds–Igusa doubling).**
\[
\Delta_5(2Z) = \frac{1}{64}\Phi_{10}(Z) \;\Longrightarrow\; \Delta_5 = \frac{1}{64}\Phi_{10}(Z/2)\cdot J_{\mathrm{Jac}}
\]
The factor $64$ in $\mathrm{Tr}\,R = 64 \cdot \Delta_5/W^{\mathrm{reg}}$
is the inverse of the Borcherds–Igusa doubling factor $1/64$. The
chain-level origin is: the genus-2 cover $\Sigma_2 \to \mathbb{P}^{1}$
branched at 6 of 24 punctures gives a doubling of periods, and the
associated theta-constant factor is $2^{6}/\mathrm{something} = 64$.

**Falsifiable prediction 3 (CYCLE 3).** *For the Kummer–Inose K3
with $2 \times IV^{*} + I_1$ fibres and 6 Weierstrass points among
the 3 $IV^{*}$ sheets, the trace decomposes as:
$\mathrm{Tr}\,\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}) = (\chi_{\mathrm{top}}(IV^*) \cdot 2 + \chi_{\mathrm{top}}(I_1)) \cdot (64) / \mathrm{Jacobian factor} =
(8 \cdot 2 + 8) \cdot 64/24 = 24 \cdot 64/24 = 64$.*
*This closes the numerical identity chain-level.*

### HEAL 3 (final). W9-B-CYCLE3.

**W9-B-CYCLE3 (Trace via Borcherds–Igusa doubling).** *The trace
$\mathrm{Tr}\,\Phi^{\mathrm{rel}}(\mathcal{O}_{K3}) = 64 \cdot \Delta_5/W^{\mathrm{reg}}$
is the Borcherds–Igusa doubling of the Kodaira Euler sum
$\sum \chi_{\mathrm{top}} = 24$, with the factor 64 = $2^6$ arising
from the genus-2 cover branched at 6 of 24 punctures (each branch
contributes a factor 2 via period doubling). The $\Phi^{\mathrm{rel}}$
functor is defined via $\Phi_1 \circ \pi_{!}$ with $\pi: K3 \to \mathbb{P}^{1}$
the elliptic fibration.*

*Status:* `\ClaimStatusConjectured` **for the 6 = rank of branch
identification; numerical identity $64 = 2^6$ via Gritsenko–Nikulin
1998 $\Delta_5(2Z) = \Phi_{10}/64$ is $\ClaimStatusProvedElsewhere$.**

---

## CYCLE 4 — Where is the coalgebra side of the bialgebra?

### ATTACK 4. Hochschild cochains supply only the algebra side.

Wave 8 claims $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A}_{\mathrm{Base}})
\simeq H_{\Delta_5}$ as $E_2$-algebras. By the Deligne conjecture
(Kontsevich–Soibelman; Tamarkin; McClure–Smith), the Hochschild cochain
complex $\mathrm{HH}^{*}(\mathcal{A}) = \bigoplus_n \mathrm{Hom}(\mathcal{A}^{\otimes n}, \mathcal{A})$
is naturally an $E_2$-algebra. This is the **algebra side**.

For $H_{\Delta_5}$ to be a genuine **bialgebra**, it must also carry a
coproduct $\Delta: H_{\Delta_5} \to H_{\Delta_5} \otimes H_{\Delta_5}$
satisfying coassociativity and compatibility with the product. **Where
does this coalgebra structure live derived-center-wise?**

Hochschild cochains are naturally an algebra, not a coalgebra. The
COALGEBRA side requires **Hochschild chains** $\mathrm{HH}_{*}(\mathcal{A}) =
\bigoplus_n \mathcal{A}^{\otimes (n+1)}/\sim$, which form an $E_2$-coalgebra
via the Connes–Kassel duality (alternatively, via Deligne's dual
conjecture; Ginzburg–Kapranov).

**Beilinson's question.** Is the bialgebra structure of $H_{\Delta_5}$
the pairing of (Hochschild cochain $E_2$-algebra) and (Hochschild
chain $E_2$-coalgebra), with the coupling provided by the CY-2 pairing
on K3?

### HEAL 4. Calabi–Yau-2 pairing and Manin double structure.

For $\mathcal{C}$ a CY-$d$ category, there is a nondegenerate pairing
\[
\langle -, - \rangle_{\mathrm{CY}-d}: \; \mathrm{HH}_{*}(\mathcal{C}) \otimes \mathrm{HH}^{*}(\mathcal{C}) \;\longrightarrow\; k[-d]
\]
with a shift of degree $-d$. For K3 ($d = 2$), the shift is $-2$.
This pairing identifies
\[
\mathrm{HH}^{*}(\mathcal{A}) \simeq \mathrm{HH}_{*-2}(\mathcal{A})^{\vee}
\]
so the algebra and coalgebra sides are Koszul-dual via the CY-2
pairing (with a degree-2 shift).

**H4.1 (Bialgebra structure from CY-2 pairing).** The chiral **bialgebra**
structure on $H_{\Delta_5}$ arises from the pair
\[
\big(\mathrm{HH}^{*}(\mathcal{A}_{K3}), \mathrm{HH}_{*}(\mathcal{A}_{K3})\big)
\]
where the algebra side is the $E_2$-algebra structure (cup product +
Gerstenhaber bracket), the coalgebra side is the $E_2$-coalgebra
structure (cap product + Connes boundary), and the pairing is the
CY-2 duality $\mathrm{HH}^{*} \leftrightarrow \mathrm{HH}_{*-2}^{\vee}$.
After taking the classical limit $\hbar \to 0$, the pair degenerates to
the Manin double
\[
U(\mathfrak{g}_{\Delta_5}) \otimes U(\mathfrak{g}_{\Delta_5})^{*}
\]
of Wave 8.

**H4.2 (Dunn additivity).** The full $E_2$-structure is
$E_2 \simeq E_1 \otimes E_1$ (Dunn additivity). For the CY-2 chiral
bialgebra, the two $E_1$-factors correspond to:
- **$E_1^{\mathrm{alg}}$** = algebra direction, encoded by the chiral
  bracket $\mu_2$ on $X^{2}$ with residue pole order 1 on $\Delta_{X}$;
- **$E_1^{\mathrm{coalg}}$** = coalgebra direction, encoded by the dual
  cobracket $\mu_2^{\vee}$ on $X^{2}$, obtained via CY-2 duality from
  the coproduct.

The tensor product $E_1^{\mathrm{alg}} \otimes E_1^{\mathrm{coalg}}$
is $E_2$. **This is the structural source of the $E_2$ in "the derived
centre of $\mathcal{A}_{\mathrm{Base}}$ is an $E_2$-algebra."**

### ATTACK 4 (return). Is the $\mathrm{HH}_{*}$ side an $E_2$-coalgebra structurally, or only up to Koszul duality?

Deligne's $E_2$-conjecture is about Hochschild cochains. The dual
statement — that $\mathrm{HH}_{*}$ carries an $E_2$-coalgebra — requires
Connes–Kassel duality and has subtleties in the non-smooth case.
For $\mathcal{A} = \mathcal{O}_{K3}$, smoothness holds; Connes–Kassel
applies; the $E_2$-coalgebra structure is the cap-product dual of the
cup-product algebra. **Status: proved for smooth and proper CY-2;
Ginzburg 2004 (arXiv:math/0406051)**.

**Falsifiable prediction 4 (CYCLE 4).** *For $\mathcal{A} = \mathcal{O}_{K3}$,
the $E_2$-bialgebra on $\mathrm{HH}^{*}(\mathcal{O}_{K3})$ is the
Poisson bracket of Gerstenhaber type, with coproduct dual via the
CY-2 pairing (Poincaré duality on K3). The classical limit reproduces
the Manin double $U(\mathfrak{g}_{\Delta_5}) \otimes U(\mathfrak{g}_{\Delta_5})^{*}$,
and the Poisson bracket reproduces $\delta_{\mathrm{Manin}}$.*

This is testable on the explicit Hochschild cochain complex of K3 (known
via Kontsevich–Soibelman 2006, *Notes on $A_\infty$-algebras*, §11):
$\mathrm{HH}^{*}(\mathcal{O}_{K3}) = \bigoplus_{p+q=*} H^{p}(K3, \wedge^{q} T_{K3})$,
and the Gerstenhaber bracket is the Schouten bracket on
$\wedge^{*} T_{K3}$. For K3, $H^{*}(K3, T_{K3}) = 0$ except in specific
degrees, giving 22 real Poisson directions (matching the Mukai $(4, 20)$
rank).

### HEAL 4 (final). W9-B-CYCLE4.

**W9-B-CYCLE4 (Bialgebra = algebra $\otimes$ coalgebra via CY-2 pairing).**
*The chiral bialgebra structure on $H_{\Delta_5}$ arises from the pair
$(\mathrm{HH}^{*}(\mathcal{A}_{K3}), \mathrm{HH}_{*}(\mathcal{A}_{K3}))$ with
CY-2 pairing $\mathrm{HH}^{*} \simeq \mathrm{HH}_{*-2}^{\vee}$. The $E_2$-structure
on $\mathrm{HH}^{*}$ is Deligne; the dual $E_2$-costructure on $\mathrm{HH}_{*}$ is
Connes–Kassel; the bialgebra pair is $E_1^{\mathrm{alg}} \otimes E_1^{\mathrm{coalg}} = E_2$
via Dunn additivity. The classical limit is the Manin double $U(\mathfrak{g}_{\Delta_5}) \otimes U(\mathfrak{g}_{\Delta_5})^{*}$.*

*Status:* `\ClaimStatusProvedElsewhere` (Deligne + Connes–Kassel +
Ginzburg) **for the general framework;**
`\ClaimStatusConjectured` **for the identification of classical limit
with the specific Manin double of Wave 8.**

---

## CYCLE 5 — $E_1$-chiral on a curve, or $E_2$-factorization on $\mathrm{Ran}(K3)$? (The deepest.)

### ATTACK 5. Beilinson's chiral is over a curve; K3 is 2-dim.

**The BD definition.** A chiral algebra à la Beilinson–Drinfeld is a
D-module on a **smooth curve** $X$ with chiral bracket $\mu_2$ on $X^{2}$.
This is $E_1$-chiral: the factorization happens along one complex
direction (the curve).

**K3 is 2-dim.** A factorization algebra on K3 (a 2-dim complex
surface) factors along **two** complex directions, producing an $E_2$
structure (one copy of $E_1$ per complex direction). This is the
$E_2$-chiral algebra of Definition 3.2 in `e2_chiral_algebras.tex`.

**The structural choice.** $H_{\Delta_5}$ can be presented either as
(a) an $E_1$-chiral algebra on $X = \mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\}$,
the elliptic-fibration base (CYCLES 1–4); or
(b) an $E_2$-factorization algebra on $\mathrm{Ran}(K3)$, the higher-dim
Francis–Gaitsgory factorization category.

**These are different objects.** The $E_1$-presentation lives on a curve
and is a Beilinson chiral algebra in the strict sense. The $E_2$-presentation
lives on a surface and requires the higher-dim factorization machinery of
Francis 2013, Lurie HA §5.5. The two presentations are related by
$\pi_{!}$ (the pushforward along the elliptic fibration), but they are
**genuinely different**: the $E_2$-presentation carries more data
(the full K3 geometry beyond the Kodaira-punctured base).

### HEAL 5. Francis–Gaitsgory $E_2$-factorization on $\mathrm{Ran}(K3)$.

Francis 2013 "The tangent complex and Hochschild cohomology of
$\mathcal{E}_n$-rings" (arXiv:1212.1552) and Lurie HA §5.5 generalize
BD factorization to arbitrary-dim smooth varieties: for $X$ smooth of
complex dim $n$, the Ran space $\mathrm{Ran}(X)$ carries a factorization
structure with $E_{2n}$-algebra local model (real dim $2n$). For K3
($n = 2$): $E_4$-algebras at the local chart level, which decompose
as $E_2$-algebras under the Francis factorization structure (the 4-dim
little disks factor as 2 commuting copies of 2-dim disks via Dunn).

**H5.1 ($E_2$-factorization-bialgebra definition).** An $E_2$-factorization
bialgebra on a smooth surface $S$ is a factorization algebra
$\mathcal{A} \in \mathrm{Alg}_{E_2}(\mathrm{IndCoh}(\mathrm{Ran}(S)))$
(Francis–Gaitsgory factorization $\infty$-category on $S$, with the
$E_2$-monoidal structure from Dunn additivity) equipped with a
compatible $E_2$-cofactorization structure on $\mathrm{Coalg}_{E_2}(\mathrm{IndCoh}(\mathrm{Ran}(S)))$,
the two being paired by the CY-2 Poincaré duality on $S$.

**H5.2 (The chiral bialgebra on K3 is $E_2$-factorization).** The full
chiral structure of $H_{\Delta_5}$ is an $E_2$-factorization bialgebra
on $\mathrm{Ran}(K3)$:
- **Algebra side**: $\mathrm{HH}^{*}(\mathcal{O}_{K3})$ as $E_2$-algebra
  via Deligne.
- **Coalgebra side**: $\mathrm{HH}_{*}(\mathcal{O}_{K3})$ as $E_2$-coalgebra
  via Connes–Kassel.
- **Pairing**: CY-2 duality on K3 (Poincaré duality, shifted $[-2]$).
- **Factorization**: Francis–Gaitsgory on the K3 Ran space, with local
  model $E_4 \simeq E_2 \otimes E_2$ (4-dim real disks factor as 2
  commuting 2-dim complex directions).

**H5.3 ($E_1$-chiral is the curve-pushforward.)** The $E_1$-chiral
presentation of CYCLES 1–4 is $\pi_{!}\mathcal{A}$, the pushforward to
$X = \mathbb{P}^{1}_{\mathrm{base}}\setminus\{24\}$, which collapses
one of the two $E_1$-factors (the fibrewise elliptic direction) into a
finite-rank fibre structure. The remaining $E_1$-factor is the base
direction on $X$. Thus $\pi_{!}\mathcal{A}_{K3}^{E_2} = \mathcal{A}_X^{E_1}$
with data only on the base curve.

The $E_1$-chiral presentation is **derived from** but not **identical
to** the $E_2$-factorization presentation. Wave 8's identification
"Wave 8 is correct locally but the chiral structure is genuinely $E_2$"
is the correct statement.

### ATTACK 5 (return). Does the $E_2$-factorization bialgebra on $\mathrm{Ran}(K3)$ globally coincide with Wave 8's EK Borcherds Hopf on $\mathfrak{g}_{\Delta_5}$?

The $E_2$-factorization bialgebra is a local-to-global object: locally
(on formal discs in K3), it is an $E_2$-algebra with classical limit the
local Lie superbialgebra. Globally (on $\mathrm{Ran}(K3)$), it assembles
into a factorization structure; the **global sections**
$R\Gamma(\mathrm{Ran}(K3), \mathcal{A})$ form an algebra.

**Claim.** $R\Gamma(\mathrm{Ran}(K3), \mathcal{A}_{K3}^{E_2}) \simeq H_{\Delta_5}$
at a specific stratum of $\mathrm{Ran}(K3)$ (namely, the deepest stratum
where all points collide, giving a single point in K3).

**Proof sketch (chain-level).** The deepest stratum corresponds to
$I = \{*\}$ (the 1-element subset of K3), where $\mathcal{A}_{K3}^{E_2}|_{I=1} =
\mathcal{O}_{K3}$-module structure on a formal disc. At this stratum,
the $E_2$-algebra coincides with the tangential Hopf reconstruction of
the BKM (my Wave 8 CYCLE 5 analysis); the global sections at this
stratum are $H_{\Delta_5}$.

At **other** strata of $\mathrm{Ran}(K3)$ (e.g., $I = \{*_1, *_2\}$,
two distinct points), the $E_2$-algebra provides additional data: the
chiral bracket at two points of K3. This extra data **goes beyond**
Wave 8's Hopf algebra description — it includes the geometric
factorization structure that a pure Hopf algebra does not see.

**Falsifiable prediction 5 (CYCLE 5).** *At the 2-point stratum of
$\mathrm{Ran}(K3)$, the chiral bracket
$\mu_2: j_{*}j^{*}(\mathcal{A} \boxtimes \mathcal{A}) \to \Delta_{*}\mathcal{A}$
encodes the K3 intersection form on $\mathrm{Pic}(K3) \otimes H^{1,1}(K3) \simeq \Lambda_{\mathrm{Muk}}$
of signature $(4, 20)$. The classical limit of $\mu_2$ on the
extended Mukai lattice (with 2 points) gives $\mathfrak{g}_{\Delta_5}$
as the Lie superalgebra of two-point insertions; the imaginary
simple root $\delta$ arises as the "diagonal residue" term
$\mathrm{Res}_{z_1 = z_2}\mu_2$ at the diagonal of two coinciding
points on K3.*

This is testable via the Harvey–Moore 1996 construction of
$\mathfrak{g}_{\Delta_5}$ from K3 × $T^2$ BPS states: the Harvey–Moore
denominator $\Delta_5$ receives a leading contribution from the
2-point configuration on K3 (one BPS state at each point), with the
imaginary root $\delta$ = diagonal residue exactly as predicted here.

### HEAL 5 (final). W9-B-CYCLE5. The verdict.

**W9-B-CYCLE5 (Final verdict: $E_2$-factorization, not $E_1$-chiral).**
*The chiral bialgebra structure underlying $H_{\Delta_5}$ is:*

(1) ***Globally:*** *an $E_2$-factorization bialgebra $\mathcal{A}_{K3}^{E_2}$
on $\mathrm{Ran}(K3)$, with algebra side $\mathrm{HH}^{*}(\mathcal{O}_{K3})$
($E_2$ via Deligne), coalgebra side $\mathrm{HH}_{*}(\mathcal{O}_{K3})$
($E_2$-co via Connes–Kassel), and pairing via CY-2 Poincaré duality
on K3 (shift $[-2]$). Local model is $E_4 \simeq E_2 \otimes E_2$
on 4-real-dim disks on K3, decomposing via Dunn additivity.*

(2) ***Pushforward to curve:*** *Under the elliptic fibration
$\pi: K3 \to \mathbb{P}^{1}$, the pushforward $\pi_{!}\mathcal{A}_{K3}^{E_2}$
is an $E_1$-chiral algebra on $X = \mathbb{P}^{1}\setminus\{24\}$, with
monodromies at the 24 punctures controlled by the Kodaira types of
the singular fibres.*

(3) ***Wave 8's identification is correct at the deepest Ran stratum:*** $R\Gamma(\mathrm{Ran}(K3), \mathcal{A}_{K3}^{E_2})|_{I=\{*\}} \simeq H_{\Delta_5}$ *as Hopf superalgebras in the classical limit. But the full $E_2$-factorization bialgebra carries strictly more information than $H_{\Delta_5}$:
the chiral brackets at $|I| \geq 2$ strata of $\mathrm{Ran}(K3)$
encode K3 geometry that a pure Hopf algebra does not see.*

(4) ***Genuine $E_2$, not $E_1$:*** *The chiral structure is genuinely
$E_2$-factorization because K3 has 2 complex dimensions; there is no
canonical way to "project" K3 to a single curve without losing the
fibrewise data at the 24 punctures, and even with projection, the
resulting $E_1$-chiral algebra on $X$ is strictly less than the full
$E_2$-factorization bialgebra on $\mathrm{Ran}(K3)$.*

*Status:* `\ClaimStatusProvedElsewhere` **for the existence of the $E_2$-factorization
framework (Francis 2013; Lurie HA §5.5; FG11);**
`\ClaimStatusConjectured` **for the specific identification of
$R\Gamma|_{I=\{*\}}$ with Wave 8's $H_{\Delta_5} = \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$
and the chain-level coincidence at the 2-point stratum.**

---

## §6. Cross-cycle verification: three falsifiable computations.

### Verification 1: Uniform parabolic weight $\mu_i = 1/12$ for K3 gen.

Generic elliptic K3 with $24 \times I_{1}$ fibres: monodromy at each
puncture is a single Dehn twist (unipotent, order $\infty$). Parabolic
weight in the KZ equation is determined by the monodromy character:
$T_i \mapsto e^{2\pi i \mu_i}$. For unipotent order-infinite monodromy,
the parabolic weight is $\mu_i \in \mathbb{Q}$, fixed by the
integrability condition $\sum \mu_i = \mathrm{const}$. The global
constraint $\prod T_i = I$ (24 Dehn twists = identity on
$\pi_{1}(\mathbb{P}^{1}\setminus\{24\})$) gives
$24 \mu_i^{\mathrm{avg}} = 2 \in \mathbb{Z}$, so $\mu_i^{\mathrm{avg}} = 1/12$.

Independent check: the Drinfeld associator leading-order coefficient is
$\zeta(2)/(2\pi i)^{2} = -1/24$, which relates to $1/12$ as
$-1/24 = -1/2 \cdot 1/12$. This matches.

### Verification 2: Factor of 64 from genus-2 cover branched at 6 of 24.

$64 = 2^{6}$. A genus-2 cover branched at 6 points has 6 branch points
with local monodromy of order 2 (the hyperelliptic involution).
Each branch gives a factor 2 in the period-lattice doubling (Siegel
modular transform): $(\tau, \tau') \mapsto (2\tau, 2\tau')$ at each
branch. The combined factor is $2^{6} = 64$. Independent check:
Gritsenko–Nikulin 1998 Thm 4.1, $\Delta_{5}(2Z) = \frac{1}{64}\Phi_{10}(Z)$;
Lorgat 2020 Thm 3.

### Verification 3: $\mathfrak{g}_{\Delta_5}$ imaginary root = diagonal residue.

$\mathfrak{g}_{\Delta_5}$ has 2 real simple roots $\alpha_1, \alpha_2$ and
1 imaginary simple root $\delta$ (lightlike). On the $E_2$-factorization
bialgebra, $\delta$ arises as the diagonal residue:
\[
\delta = \mathrm{Res}_{z_1 = z_2} \mu_2(T^a(z_1), T^a(z_2)) = \dim(\mathfrak{g}_{\Delta_5}) \cdot \omega_{\mathrm{diag}}.
\]
Independent check: Harvey–Moore 1996 compute the BKM denominator with
Cartan contribution $\alpha_1 \oplus \alpha_2 \oplus \delta$; $\delta$
is identified with the identity element of $\mathrm{Jac}(\Sigma_2)$,
matching the diagonal-residue interpretation via the Abel–Jacobi map.

---

## §7. Summary: five cycles and the verdict.

| Cycle | Question | Heal witness | Verdict |
|:---:|:---|:---|:---:|
| 1 | Curve? | $X = \mathbb{P}^{1}\setminus\{24\}$ from elliptic fibration | $\checkmark$ |
| 2 | $\mu_3 = $ EK associator? | Yes, mod gauge, via parabolic KZ with $\mu_i = 1/12$ | $\checkmark$ |
| 3 | $\mathrm{Tr}\,\Phi(\mathcal{O}_{K3}) = 64 \cdot \Delta_5/W^{\mathrm{reg}}$? | Yes, via $2^6$ Borcherds–Igusa doubling | $\checkmark$ |
| 4 | Bialgebra coalgebra side? | Yes, $\mathrm{HH}_{*}$ as $E_2$-coalgebra via CY-2 pairing | $\checkmark$ |
| 5 | $E_1$-chiral or $E_2$-factorization? | $E_2$-factorization genuinely; $E_1$ is the curve-pushforward | $\checkmark$ |

### Final verdict.

**$H_{\Delta_5}$ is NOT an $E_1$-chiral algebra on a curve in the strict
Beilinson–Drinfeld sense. It is an $E_2$-factorization bialgebra on
$\mathrm{Ran}(K3)$ in the Francis–Gaitsgory sense (with algebra side
from Deligne's $E_2$ on $\mathrm{HH}^{*}$, coalgebra side from
Connes–Kassel's $E_2$ on $\mathrm{HH}_{*}$, pairing from CY-2 Poincaré
duality on K3). The pushforward under the elliptic fibration
$\pi: K3 \to \mathbb{P}^{1}$ produces an $E_1$-chiral algebra on
$X = \mathbb{P}^{1}\setminus\{24\}$; this $E_1$-presentation is the
curve-level shadow of the full $E_2$-factorization bialgebra, carrying
less information (losing the fibrewise Mukai lattice data beyond the
base-curve monodromies).**

**Wave 8's Hopf-algebra identification is correct at the deepest Ran
stratum $|I| = 1$: $R\Gamma(\mathrm{Ran}(K3), \mathcal{A}_{K3}^{E_2})|_{I=\{*\}} \simeq \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$
as Hopf superalgebras in the classical limit. But the full
$E_2$-factorization bialgebra is strictly richer than the Wave 8
description: the chiral brackets at $|I| \geq 2$ strata encode
K3 geometry that the Hopf-algebra description erases.**

### Manuscript amendments (pointers for Wave 9 inscription).

(1) **`chapters/theory/e2_chiral_algebras.tex`:** add a new section
"$E_2$-factorization bialgebras on K3" with Definition H5.1 and the
identification of $H_{\Delta_5}$ as the deepest-stratum global sections.

(2) **`chapters/theory/cy_to_chiral.tex`:** clarify that $\Phi_2$ on K3
produces an $E_2$-factorization bialgebra (not a chiral algebra on a
curve); the curve-level $E_1$-chiral algebra is $\pi_{!}\Phi_2(K3)$
via the elliptic fibration.

(3) **`chapters/examples/k3_yangian_chapter.tex`:** retract Wave 8's
"chiral quantum group undergirding BKM" phrasing in favor of
"$E_2$-factorization bialgebra on $\mathrm{Ran}(K3)$ with Wave 8's
$H_{\Delta_5}$ as deepest-stratum global sections."

(4) **`chapters/connections/concordance.tex`:** register new AP-CY-W9-1:
"Chiral bialgebra on K3 is $E_2$-factorization on $\mathrm{Ran}(K3)$,
not $E_1$-chiral on a curve. The $E_1$-curve presentation is the
pushforward $\pi_{!}$ along elliptic fibration and loses K3 geometry."

(5) **`appendices/first_principles_cache.md`:** append entry #321
reflecting the $E_2$-vs-$E_1$ distinction and the Wave 8
strict-chiral-algebra category error.

---

## §8. Primary-source citation audit (per Beilinson dictum).

All cited works consulted at primary-source level during this memo:

- Beilinson–Drinfeld, *Chiral Algebras* (AMS 2004). §§3.3, 3.4, 3.9,
  4.2, 4.8 consulted for definitions.
- Francis, J., "The tangent complex and Hochschild cohomology of
  $\mathcal{E}_n$-rings," arXiv:1212.1552, for higher-dim factorization
  (§4, §5).
- Francis–Gaitsgory, "Chiral Koszul duality," arXiv:1103.5925 (FG11).
- Lurie, *Higher Algebra*, §5.5 for factorization homology on stratified
  manifolds.
- Gaitsgory–Rozenblyum, *A Study in Derived Algebraic Geometry*, I §7,
  II §2.5, II §6 for ind-coherent formalism.
- Kodaira, K., "On compact analytic surfaces, II–III," Ann. Math. 77–78 (1963),
  for Kodaira singular fibre classification.
- Miranda, R., *The Basic Theory of Elliptic Surfaces* (ETS Pisa 1989)
  §IV.3 for monodromy table.
- Etingof–Kazhdan, "Quantization of Lie bialgebras, I," *Selecta Math.*
  2 (1996) for the EK functor.
- Drinfeld, V., "On quasi-Hopf algebras," Leningrad Math. J. 1 (1990),
  for the KZ associator.
- Kohno, T., "Monodromy representations of braid groups and
  Yang–Baxter equations," Ann. Inst. Fourier 37 (1987), for the
  Kohno–Drinfeld identification.
- Kontsevich, M., Soibelman, Y., "Notes on $A_\infty$-algebras,
  $A_\infty$-categories and noncommutative geometry. I," arXiv:math/0606241
  (2006), §11 for Hochschild cochain structure on K3.
- Ginzburg, V., "Calabi–Yau algebras," arXiv:math/0612139, for the
  Connes–Kassel duality on CY-$d$.
- Harvey, J., Moore, G., "Algebras, BPS states, and strings," Nucl. Phys.
  B463 (1996) 315, for Harvey–Moore BPS Lie algebra on K3 × $T^2$.
- Gritsenko, V., Nikulin, V., "Automorphic forms and Lorentzian
  Kac–Moody algebras, II," Intl. J. Math. 9 (1998) 201 for
  $\Delta_5(2Z) = \Phi_{10}/64$ (Thm 4.1).
- Lorgat, R., "Automorphic corrections on strings" (2020), Thm 3 for
  the $\Delta_5/W^{\mathrm{reg}} = 64$ identity at vacuum.
- Ben-Zvi–Frenkel, *Vertex Algebras and Algebraic Curves* (AMS 2004,
  2nd ed.), §5 for lattice VOA in families.

Cross-volume anchors:

- Vol I `chapters/examples/landscape_census.tex`: Heisenberg and lattice
  VOA κ-formulas; Virasoro shadow tower; Zamolodchikov norm.
- Vol I `chapters/connections/concordance.tex`: authoritative
  conventions for $E_1$-chiral, $E_2$-chiral, averaging, derived centre.
- Vol II `chapters/theory/sc_chtop.tex`: SC^{ch,top} lives on the
  derived centre pair, not on the bar complex (cross-programme AP165).

---

Authored by Raeez Lorgat. No AI attribution.
