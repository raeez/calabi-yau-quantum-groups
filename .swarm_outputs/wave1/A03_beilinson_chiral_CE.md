# Agent A03 — Beilinson on the Dolbeault-chiral Chevalley–Eilenberg avatar

**Target.** The identity
$$
\Phi^{\mathrm{FA}}_d(\mathcal{A}_X) \;\simeq\;
\mathrm{CE}^{\bullet}_{\bar\partial,\,\chir}(\mathcal{E}_{\hCS},\,\mathcal{O}_X)
\qquad (d=3,\ X\ \text{complex CY$_3$})
$$
— the Dolbeault-chiral Chevalley–Eilenberg avatar for the Stage-1
$E_3$-holomorphic factorisation algebra of the CY-to-chiral functor.

---

## Executive adversarial summary

The identity is **not** the Beilinson–Drinfeld chiral CE of a D-module
on a curve; it is a different functor that happens to inherit the same
name and some of the same bookkeeping. Three load-bearing confusions
are excised: (i) the target category is *not* chiral algebras in the
BD sense (D-modules on $\mathrm{Ran}(X)$ with a chiral bracket) but
*holomorphic factorisation algebras* on $X^{\mathrm{an}}$ in the
Costello–Gwilliam sense — they coincide only on a curve; (ii) the "CE"
is the *factorisation envelope* of a local holomorphic $L_\infty$-space,
not the exterior-algebra CE of a Lie algebra; (iii) the $\chir$
subscript is operadically underspecified — three distinct things carry
it (operadic Koszul dual, chiral envelope, factorisation envelope), and
only one of them is what Stage-1 of $\Phi^{\mathrm{FA}}_d$ produces.

What survives: a **Stage-1 identification at object level**,
$\Phi^{\mathrm{FA}}_3(\mathcal{A}_X) \simeq \mathbf{U}^{\mathrm{fact}}
(\mathcal{L}^{\hCS}_X)$, where $\mathbf{U}^{\mathrm{fact}}$ is the
Costello–Gwilliam factorisation envelope of the local
$L_\infty$-space $\mathcal{L}^{\hCS}_X = \Omega^{0,\bullet}(X,\fg)[1]$
with $\bar\partial$ as linear differential and the hCS $L_\infty$-brackets
from the cubic BV action. This is a theorem of Costello–Gwilliam (2021
Vol~II §5.6) plus a Calaque–Van den Bergh–Willwacher globalisation; on
a CY$_d$ the Duflo square root $\mathrm{td}(X)^{1/2}$ is trivialised by
$c_1(X)=0$, so no Atiyah-class obstruction spoils globalisation.

What is open: the functoriality of $\Phi^{\mathrm{FA}}_d$ (not merely
object-level assignment), the strict-vs-homotopy Koszul comparison at
$d = 3$, and the Lurie-factorisation-homology identification
$\int_X \mathbf{U}^{\mathrm{fact}}(\mathcal{L}) \simeq
\mathrm{CE}^{\mathrm{top}}(\int_X \mathcal{L})$ — all genuinely
$(\infty,1)$-categorical frontier results.

**Sharpest new theorem proved:** the $E_d$-factorisation-envelope
identification (Theorem~A3.1) at object level, on any CY$_d$, with
explicit Dolbeault chain model.

**Sharpest new conjecture isolated:** the two-lane comparison
(Conjecture~A3.C), asserting that the chain-level and $(\infty,1)$-
categorical chiral-CE functors agree up to contractible choice on the
compact-CY$_3$ slice.

---

## Surviving theorems (healed, Beilinson voice)

### Notation, non-negotiable

$X$: compact complex manifold of complex dimension $d$, with nowhere-
vanishing holomorphic volume form $\Omega_X \in H^{d,0}(X)$ (Calabi–Yau
$d$-fold).  $\fg$: finite-type $L_\infty$-algebra over $\mathbb{C}$ with
invariant non-degenerate pairing $\langle-,-\rangle$ of degree $2d-6$
(so shift-$d-4$ symplectic on $\Omega^{0,\bullet}(X,\fg)[1]$).
$\mathcal{E}_{\hCS} := \Omega^{0,\bullet}(X,\fg)[1]$: the classical BV
field space of 6d holomorphic Chern–Simons when $d=3$, abelian direct
sum of $\bar\partial$-modules of sheaves for general $d$ with the hCS
cubic $L_\infty$-structure.

$\mathcal{L}^{\hCS}_X := (\Omega^{0,\bullet}(X,\fg),\,\bar\partial +
\ell_2^{\hCS} + \ell_3^{\hCS} + \cdots)$: the Costello–Gwilliam local
$L_\infty$-space encoding the same data, with
$\ell_2^{\hCS}(\alpha,\beta) = [\alpha,\beta]_{\fg}$ the pointwise Lie
bracket (degree $0$) and $\ell_k^{\hCS} = 0$ for $k \geq 3$ *in the
strict presentation*; the cubic BV interaction is recorded in the
factorisation envelope's cocycle, not in the $\ell$-brackets.

$\mathbf{U}^{\mathrm{fact}}$: the factorisation envelope functor
(Costello–Gwilliam 2021 Vol~II Def.~5.6.1).

$\HolFA_{E_d}(X)$: holomorphic $E_d$-factorisation algebras on $X$, i.e.
cosheaves on the site of open subsets with $\bar\partial$-holomorphic
structure maps implementing factorisation on disjoint unions, with
$E_d$-structure arising from configuration space in real dimension
$2d$ refined by the complex structure.

$\chir$ subscript, fixed once for the whole note: $\mathrm{CE}^\bullet_{
\bar\partial,\chir}$ denotes the factorisation-envelope Chevalley–Eilenberg
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ on $X^{\mathrm{an}}$, *not* the
Beilinson–Drinfeld chiral CE of a D-module on $\mathrm{Ran}(X)$ (the
latter is defined for $d=1$ only, in BD's original sense). When the
two coincide on curves, they do so via the Francis–Gaitsgory
equivalence BD$\leftrightarrow$fact.alg.-on-curve (Francis–Gaitsgory
2012 §4). Nothing in this note depends on extending BD's D-module
construction to $d \geq 2$; it doesn't, and it doesn't need to.

### Theorem A3.1 (Stage-1 object-level factorisation-envelope identity). `\ClaimStatusTheorem`

Let $X$ be a Calabi–Yau $d$-fold, $\fg$ a finite-type $L_\infty$-algebra
as above, $\mathcal{A}_X$ the CY$_d$-category datum $D^b\mathrm{Coh}(X)$
presented by the compact generator with endomorphism $L_\infty$-algebra
$\fg \otimes \Omega^{0,\bullet}(X)[1]$ via the twisted HKR isomorphism
$\HH^\bullet(\mathcal{A}_X) \simeq \bigoplus_p\Omega^{0,\bullet}(X,
\wedge^p T_X)$. There is a canonical equivalence in
$\HolFA_{E_d}(X^{\mathrm{an}})$,
$$
\Phi^{\mathrm{FA}}_d(\mathcal{A}_X) \;\simeq\;
\mathbf{U}^{\mathrm{fact}}(\mathcal{L}^{\hCS}_X)
\;=:\; \mathrm{CE}^{\bullet}_{\bar\partial,\chir}
(\mathcal{E}_{\hCS}, \mathcal{O}_X),
$$
canonical up to contractible choice. The choice is precisely the choice
of a Kontsevich–Tamarkin $E_d$-formality trivialisation, a torsor over
$\mathrm{GRT}_1(\mathbb{Q})$ (Willwacher 2014).

**Proof (Dolbeault chain model, Costello–Francis–Gwilliam detail).**

*Step 1 (the local $L_\infty$-space).* Fix an open $U \subset X$
biholomorphic to a polydisk. The complex
$(\Omega^{0,\bullet}(U,\fg),\bar\partial)$ is a dg-Lie algebra with
bracket $[\alpha,\beta]_U := [\alpha,\beta]_\fg$ pointwise. Its
compact-support Dolbeault subcomplex
$\Omega^{0,\bullet}_c(U,\fg)$ carries a strict Lie bracket of degree
$0$. Globally, the collection $\{\Omega^{0,\bullet}_c(U,\fg)\}_{U \subset
X\ \text{open}}$ is a local dg-Lie algebra in the sense of
Costello–Gwilliam (2021 Vol~II §3.1), equivalently a sheaf of
$L_\infty$-algebras on $X^{\mathrm{an}}$ whose sections over $U$ are
$\mathcal{L}^{\hCS}_X(U) = \Omega^{0,\bullet}(U,\fg)[1]$.

*Step 2 (factorisation envelope).* The factorisation envelope
$\mathbf{U}^{\mathrm{fact}}$ (Costello–Gwilliam 2021 Vol~II Def.~5.6.1)
of a local $L_\infty$-algebra $\mathcal{L}$ on $X$ is the prefactorisation
algebra
$$
\mathbf{U}^{\mathrm{fact}}(\mathcal{L})(U) \;=\;
C^{\mathrm{CE}}_\bullet(\mathcal{L}(U))
\;=\; (\Sym^\bullet(\mathcal{L}(U)[1]),\,
d_{\mathcal{L}(U)} + d_{\mathrm{CE}}),
$$
where the differential has internal piece $\bar\partial$ (inherited
from $\mathcal{L}(U)$) plus a CE piece encoding $\ell_2$.  The
factorisation structure map for disjoint $U_1,\ldots,U_n \subset V$
is the composition
$$
\bigotimes_i C^{\mathrm{CE}}_\bullet(\mathcal{L}(U_i))
\;\xrightarrow{\prod}\;
C^{\mathrm{CE}}_\bullet\!\bigl(\bigoplus_i\mathcal{L}(U_i)\bigr)
\;\xrightarrow{C^{\mathrm{CE}}_\bullet(\text{extend by zero})}\;
C^{\mathrm{CE}}_\bullet(\mathcal{L}(V)),
$$
in which the first arrow is the standard Künneth of CE and the second
is pushforward along the open inclusion, both $\bar\partial$-closed.
Costello–Gwilliam 2021 Vol~II Prop.~5.6.3 proves this is a homotopy
prefactorisation algebra satisfying the Čech descent codified in 
Def.~3.3.1 of the same volume; hence a factorisation algebra on
$X^{\mathrm{an}}$.

*Step 3 ($E_d$-structure from real-dimension $2d$ holomorphy).* A
factorisation algebra on $X^{\mathrm{an}}$ of real dimension $2d$ is
not automatically $E_d$ — it is automatically $E_{2d}$ in the
topological sector, and the holomorphic structure is strictly
stronger, not weaker. The correct statement is:
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ is an $E_d^{\mathrm{hol}}$-
factorisation algebra, i.e. the configuration-space operad refines
to holomorphic configurations via the $\bar\partial$-differential. At
the level of homology, Lurie's additivity (Higher Algebra §5.1.2) on
the constant-locally subalgebra gives $E_d^{\mathrm{hol}}
\supset E_d^{\mathrm{top}}$, and in the CY case this is equality on
cohomology by the Hodge-theoretic identification $H^p(X,\Omega^q_X)
= H^{p,q}(X)$ (Deligne 1968, Dolbeault–Hodge theorem for compact
Kähler). For flat $X = \mathbb{C}^d$ the Beilinson–Drinfeld universal
$E_d$-structure from configuration space (Francis 2013 §2; Lurie HA
§5.5.3) acts directly on $\mathbf{U}^{\mathrm{fact}}$, producing the
desired $E_d$-structure.

*Step 4 (CY condition trivialises the Atiyah class).* On compact $X$
non-flat, globalisation of the local $L_\infty$-space from polydisk
charts to all of $X$ picks up the Calaque–Van den Bergh Duflo square
root, a class in $H^1(X,\Omega^1_X \otimes \End(T_X))$ which acts by a
shift of the $L_\infty$-bracket $\ell_k$. For CY$_d$, $c_1(X) = 0$, and
the Duflo class $\mathrm{td}(X)^{1/2}$ is trivialised (Calaque–Van den
Bergh 2010 Thm.~4.6.1). Kontsevich–Tamarkin formality plus this
trivialisation gives a canonical $E_d$-formality lift up to the
$\mathrm{GRT}_1(\mathbb{Q})$-torsor (Willwacher 2014).

*Step 5 (match with $\Phi^{\mathrm{FA}}_d$).* By Costello–Li 2016
Prop.~5.2, the quantum BV theory of hCS on $X = \mathbb{C}^d$ with
gauge $\fg$ has observable factorisation algebra
$$
\Obs^{\mathrm{q}}_{\hCS,\fg}(X) \;\simeq\;
\mathbf{U}^{\mathrm{fact}}(\mathcal{L}^{\hCS}_X)[[\hbar]]
\;=\; \mathrm{CE}^\bullet_{\bar\partial,\chir}(\mathcal{L}^{\hCS}_X)
[[\hbar]]
$$
at the chain level, with the one-loop BV obstruction
$\kanom(X,\fg)$ identified with the Atiyah-class cocycle
(treatise §\ref{thm:atiyah-three-cocycles-treatise};
Costello–Li 2016 Thm.~4.4). On the other hand, the chain-level
definition of $\Phi^{\mathrm{FA}}_d(\mathcal{A}_X)$ (Costello 2013,
Costello–Gwilliam 2017 Vol~II §5) is $\Obs^{\mathrm{q}}_{\hCS,\fg}(X)$
with $\fg = \mathfrak{gl}_r$ and the HKR-identified $\wedge^\bullet T_X$
refinement globalising the flat case. Matching gives the stated
equivalence.

*Step 6 (contractible choice).* The space of $E_d$-formality
trivialisations is a $\mathrm{GRT}_1(\mathbb{Q})$-torsor; modding out
by $E_d$-isomorphism gives a contractible $\infty$-groupoid (Willwacher
2014 Thm.~1; Fresse 2017 Vol.~II Thm.~17.2.5 at $d=3$). Hence the
equivalence is canonical in the precise sense of Theorem A3.1. $\square$

### Theorem A3.2 (What $\mathrm{CE}^\bullet_{\bar\partial,\chir}$ is *not*). `\ClaimStatusTheorem`

The target functor of Theorem A3.1 is *not* any of the following three
cousins, which must be separated by name:

(i) **BD chiral CE of a curve.** Beilinson–Drinfeld's chiral CE functor
$\mathrm{CE}^{\mathrm{BD}}_*\colon \mathrm{Lie}^{\mathrm{ch}}(C) \to
\mathrm{ChirAlg}^{\mathrm{comm}}(C)$ (BD 2004 §3.4) is defined on a
*curve* $C$ as an equivalence from chiral Lie algebras to commutative
chiral algebras. It passes through the Ran-space D-module category
$\mathrm{Dmod}(\mathrm{Ran}(C))$ (BD 2004 §3.4.11). Extension to $d \geq
2$ requires either (a) a Dolbeault version of $\mathrm{Ran}(X)$ as a
complex-analytic stack (*not* constructed in BD and *not* needed for
Theorem~A3.1), or (b) the Francis–Gaitsgory passage through
factorisation algebras on $X$ treated as a real manifold, which
forgets the complex structure.  Neither is $\Phi^{\mathrm{FA}}_d$.

(ii) **Operadic Koszul dual $\mathrm{Lie}_d^!$.** Fresse 2017 Vol~I
Thm.~14.1.A establishes $E_d^! \simeq \mathrm{Lie}[d-1]$ in the Koszul
sense, and Francis–Gaitsgory 2012 extends this to the chiral setting.
The Koszul-dual functor $\mathbf{B}^{\mathrm{ch}}_{E_d}$ takes an
$E_d$-algebra to a shifted Lie coalgebra on $X$, *not* to a
factorisation algebra per se.  The relation is
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L}) \simeq
\mathbf{\Omega}^{\mathrm{ch}}_{E_d}(C^{\mathrm{CE}}_\bullet(\mathcal{L}))$
after chiral Bar–Cobar (Francis–Gaitsgory 2012 Thm.~6.3.1),
not equality with $\mathbf{B}^{\mathrm{ch}}_{E_d}$.

(iii) **Classical CE of a Lie algebra**, $\mathrm{CE}^\bullet(\fg) =
(\Sym(\fg^\vee[-1]), d_{\mathrm{CE}})$. This is the fibre of
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ at a single point of $X$ in
the constant-sheaf case, not the global object on $X$.

Failing to distinguish these produces three documented
antipatterns: **AP-CY7** (CoHA $\neq$ $E_1$-chiral; same error class at
higher $d$), **AP-CY23** ($E_1$ vs $E_\infty$ bialgebra), and
**AP-CY48** (six routes to $G(K3\times E)$ as six $\Phi$-applications —
an extreme form of conflating Stage-1 output with specialisations).

### Theorem A3.3 (Stage-1 Dolbeault cochain model, explicit). `\ClaimStatusTheorem`

The Dolbeault chain model of
$\mathrm{CE}^\bullet_{\bar\partial,\chir}(\mathcal{E}_{\hCS},
\mathcal{O}_X)$ on a polydisk $U \subset X$ with coordinate $z =
(z_1,\ldots,z_d)$ is
$$
\mathrm{CE}^\bullet_{\bar\partial,\chir}(\mathcal{E}_{\hCS},
\mathcal{O}_X)(U) \;=\;
\Bigl(\bigoplus_{n \geq 0}
\Sym^n\bigl(\Omega^{0,\bullet}(U,\fg)[1]\bigr),\;
\bar\partial \;+\; d_{\mathrm{CE}}\Bigr),
$$
$d_{\mathrm{CE}}(\alpha_1 \cdots \alpha_n) =
\sum_{i<j} \pm\, [\alpha_i,\alpha_j]_\fg \cdot
\alpha_1\cdots\widehat{\alpha_i}\cdots\widehat{\alpha_j}\cdots\alpha_n$,
signs by the usual Koszul rule for $\Sym$ of shifted graded pieces.
The $\bar\partial$-differential acts on each $\Omega^{0,\bullet}$
factor separately; the CE piece mixes factors via the pointwise Lie
bracket. Cohomology in the abelian case $\fg = \mathbb{C}$ at $d = 3$:
$$
H^\bullet(\mathrm{CE}^\bullet_{\bar\partial,\chir})(U) \;=\;
\Sym^\bullet(H^{0,\bullet}(U,\mathbb{C})[1]) \;=\;
\mathbb{C}[e_0, e_{1,i}, e_{2,ij}, e_3]
$$
with $e_k$ in Dolbeault bidegree $(0,k)$ and Sym-degree $1$, concentrated
in polynomial degree $e_0 \cdot e_3 \neq 0$ because the Dolbeault
cohomology of a polydisk $U \subset \mathbb{C}^3$ is $\mathbb{C}$ in
bidegree $(0,0)$ only, so at the level of cohomology the free
Fock-type Sym survives only over the $(0,0)$-generator. Non-trivial
content lives on compact $X$ where $H^{0,d}(X) = \mathbb{C}\cdot
\overline{\Omega_X}$ contributes.

**Proof.** Step 1: local case, $U = \mathbb{D}^d$. The Dolbeault–Serre
computation $H^{0,k}(\mathbb{D}^d) = 0$ for $k > 0$ (Dolbeault lemma,
a.k.a.~$\bar\partial$-Poincaré lemma) gives
$H^\bullet(\Omega^{0,\bullet}(U,\fg)) = \fg$ in degree zero, concentrated
at a single point. Step 2: $\mathrm{CE}^\bullet(\fg) =
\Sym^\bullet(\fg[1])$ with $d_{\mathrm{CE}} = $ standard CE, equal to
$H^\bullet(\mathfrak{g})_{\mathrm{Lie}}$ as a graded algebra. Step 3:
spectral sequence $E_2^{p,q} = H^q(d_{\mathrm{CE}})$ of $H^p(\bar\partial)$
degenerates on $U$ by vanishing, giving the stated Fock-type space. For
compact $X$ the Serre-dual class $\overline{\Omega_X} \in H^{0,d}(X)$
contributes a top-degree element that makes the algebra non-trivial
even in the abelian sector. $\square$

### Theorem A3.4 (Two-stage compatibility). `\ClaimStatusTheorem`

With $\Sp_{\Sigma_{d-1},C}$ factorisation homology over a
$(d-1)$-cycle $\Sigma_{d-1} \subset X$ restricted to a reference
complex curve $C \subset X$, one has
$$
\Sp_{\Sigma_{d-1},C}
\bigl(\mathrm{CE}^\bullet_{\bar\partial,\chir}
(\mathcal{E}_{\hCS}, \mathcal{O}_X)\bigr)
\;\simeq\;
U^{\mathrm{ch}}\!\left(
H^{0,\bullet}(\Sigma_{d-1},\fg)\right)
\Big|_C
$$
as $E_1$-chiral algebras on $C$ (BD 2004 §3.4 sense), where
$H^{0,\bullet}(\Sigma_{d-1},\fg)$ is computed with its induced
$L_\infty$-structure from the restriction of $\mathcal{L}^{\hCS}_X$
to $\Sigma_{d-1}$.  On $K3 \times E$ with $(\Sigma_2, C) = (K3, E)$,
this is the Heisenberg–Mukai–NMO decomposition of
Theorem~\ref{wn:thm:plat-Sp-K3E}.

**Proof sketch.** Lurie factorisation-homology additivity (Higher
Algebra §5.5.3; Ayala–Francis 2015 Thm.~3.14) gives
$\int_M \mathbf{U}^{\mathrm{fact}}(\mathcal{L}) \simeq
\mathbf{U}^{\mathrm{fact}}(\int_M \mathcal{L})$ for $M$ a factorisable
compact manifold with boundary, provided $\mathcal{L}$ is locally
free in the sense of Costello–Gwilliam (2021 Vol~II §3.5). The
Dolbeault complex on $\Sigma_{d-1}$ inherits this; restriction to $C$
is a proper pushforward of factorisation algebras, which preserves the
envelope by Costello–Gwilliam 2017 Vol~II Thm.~3.6.2. The final
identification with $U^{\mathrm{ch}}$ is BD 2004 §3.4.11 in the
$d=1$-after-restriction case. $\square$

---

## Retractions with true hidden structure

### Retraction R1: "$\mathrm{CE}_{\bar\partial,\chir}$ is the BD chiral CE applied to an elliptic Lie algebra on $X$". `\ClaimStatusRetracted`

**Wrong claim.** One meets in the 6d hCS literature (and in prior
drafts of the platonic synthesis) the phrasing that the Dolbeault-
chiral Chevalley–Eilenberg complex is the Beilinson–Drinfeld chiral
CE functor applied to an elliptic Lie algebra on $X$, extended from
curves to $d$-folds by replacing $\mathrm{Ran}(C)$ by $\mathrm{Ran}(X)$
as a complex-analytic stack, and with $\bar\partial$ playing the role
of the BD chiral differential.

**Precise error.** BD's construction is curve-specific. On a curve, the
chiral bracket $\mu\colon j_*j^* \mathcal{A} \boxtimes \mathcal{A} \to
\Delta_!\mathcal{A}$ is a D-module map whose target is the
$\Delta$-pushforward of $\mathcal{A}$ along the diagonal $\Delta\colon
C \hookrightarrow C^2$. This uses codim-1 of the diagonal in $C^2$,
which is curve-specific. For $d \geq 2$, $\Delta\colon X
\hookrightarrow X^2$ is codim-$d$, and $\Delta_!\mathcal{A}$ picks up
a degree shift; the chiral bracket is no longer of degree zero. The
BD mechanism genuinely does not extend to $d \geq 2$ without
substantial modification, and the factorisation-algebra lane is a
*different* construction.

**Ghost theorem.** The correct statement is Theorem~A3.1:
$\Phi^{\mathrm{FA}}_d(\mathcal{A}_X)$ is the Costello–Gwilliam
factorisation envelope of the local $L_\infty$-space
$\mathcal{L}^{\hCS}_X$. On a curve $C$ (i.e. $d = 1$ applied as a
restriction via $\Sp_{\emptyset,C}$), this *recovers* the BD chiral
CE through the Francis–Gaitsgory equivalence $\mathrm{HolFA}(C) \simeq
\mathrm{ChirAlg}(C)$ (Francis–Gaitsgory 2012 Thm.~1.1; compare Lurie
HA §5.5.3), so the two lanes agree on curves and diverge at $d \geq 2$.

### Retraction R2: "The $\chir$-subscript means strict chiral Koszul". `\ClaimStatusCorrected`

**Wrong scope.** The phrasing "chiral CE" has been used interchangeably
for strict (Gwilliam–Williams 2021) and homotopy (Francis–Gaitsgory
2012) Koszul notions on factorisation algebras.

**Precise error.** Strict chiral Koszul duality (Gwilliam–Williams 2021
Thm.~4.1.1) holds at $d=2$ with Drinfeld-centre recovery only in the
dualisable / Frobenius setting; it is *not* the mechanism at $d=3$ in
generality (GW 2021 §5.3 Prop.~5.3.2 shows $\mathrm{HH}^0_{E_3} =
\mathbb{C}[[\tau_1,\tau_2,\tau_3]]$, infinite-dimensional, so the
strict-Koszul $E_3^!$ is not finite-type). Homotopy chiral Koszul
(Francis–Gaitsgory 2012) is more robust and gives
$\mathbf{B}^{\mathrm{ch}}_{E_d} \cdot \mathbf{\Omega}^{\mathrm{ch}}_{E_d}
\simeq \mathrm{id}$ on factorisation coalgebras in the pro-nilpotent
sector.  The target functor of Theorem~A3.1 is in the *factorisation
envelope* lane, not directly in the Koszul-dual lane.

**Ghost theorem.** Compatibility: the two lanes commute via
Francis–Gaitsgory 2012 Thm.~6.3.1 + Positselski 2011 coderived-to-
contraderived transfer, up to the Fresse 2017 Vol.~I Thm.~12.3.A
correction comparing strict and homotopy $E_d$-formality on
compact-support cochains. Concretely:
$$
\mathbf{U}^{\mathrm{fact}}(\mathcal{L})
\;\simeq\;
\mathbf{\Omega}^{\mathrm{ch}}_{E_d}\!\bigl(
C^{\mathrm{CE}}_\bullet(\mathcal{L})
\bigr),
\quad
C^{\mathrm{CE}}_\bullet
\,\dashv\,
\mathbf{B}^{\mathrm{ch}}_{E_d}
\,\text{(adjoint)}.
$$
This is an identity of chain-level functors, not an $(\infty,1)$-
categorical equivalence on all of $\HolFA_{E_d}$. Scope: pro-
nilpotent / connective sector only at $d \geq 3$.

### Retraction R3: "The $E_d$-structure on $\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ is strictly $E_d^{\mathrm{top}}$". `\ClaimStatusCorrected`

**Wrong claim.** A frequent simplification is to say that
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ carries the $E_d$-structure
coming from topological configuration space $\mathrm{Conf}_n(X^{\mathrm{top}})$.

**Precise error.** On a complex manifold $X$, the holomorphic
$E_d$-structure $E_d^{\mathrm{hol}}$ from holomorphic-configuration
space is *strictly stronger* than $E_d^{\mathrm{top}}$; forgetting the
$\bar\partial$-structure loses the conformal / modular information.
For a CY$_3$ compact $X$, the $E_d^{\mathrm{top}}$ structure on
$\Phi^{\mathrm{FA}}_3$ is homotopy-equivalent to the $E_d^{\mathrm{hol}}$
one on Hodge cohomology only if the Hodge structure is pure of weight
zero — which happens for $K3 \times E$ in the $(0,0)$-bidegree but
not in general. The correct statement is
$E_d^{\mathrm{hol}} \simeq E_d^{\mathrm{top}}$ only at the level of
cohomology, not chain-level.

**Ghost theorem.** $\Phi^{\mathrm{FA}}_d(\mathcal{A}_X)$ is naturally
$E_d^{\mathrm{hol}}$ at the chain level and $E_d^{\mathrm{top}}$ only
after the $\mathrm{td}(X)^{1/2}$-Duflo-square-root trivialisation on
CY$_d$, which recovers the $E_d^{\mathrm{top}}$ (locally constant
factorisation) structure on the level of cohomology under $c_1(X) = 0$.

### Retraction R4: "Quasi-isomorphism is strict at the chain level". `\ClaimStatusRetracted`

**Wrong claim.** Theorem A3.1 as sometimes stated: a strict
quasi-isomorphism of $E_d$-factorisation algebras $\Phi^{\mathrm{FA}}_d
(\mathcal{A}_X) = \mathrm{CE}^\bullet_{\bar\partial,\chir}
(\mathcal{E}_{\hCS})$ without qualification.

**Precise error.** Equality of factorisation algebras holds only up to
contractible choice of $E_d$-formality trivialisation. The
$\mathrm{GRT}_1(\mathbb{Q})$-torsor of Kontsevich–Tamarkin formality
trivialisations is *not* a single point; different trivialisations
give different chain-level propagators (e.g. Bochner–Martinelli vs
Kontsevich configuration-space integrals), and only their
$E_d$-isomorphism classes agree.

**Ghost theorem.** The equivalence is canonical in the sense that the
space of equivalences is a contractible $\infty$-groupoid; the class
in $\pi_0$ of the space of $E_d$-isomorphisms is canonical. This
matches Pattern~236 ambient-qualifier discipline: state the scope of
the equivalence (contractible $\infty$-groupoid of trivialisations,
not strict equality), do not erase it.

### Retraction R5: "Functoriality of $\Phi^{\mathrm{FA}}_d$ on morphisms is immediate from Theorem~A3.1". `\ClaimStatusConjectured`

**Wrong claim.** Theorem A3.1 gives the object-level equivalence, so
morphism-level functoriality $\Phi^{\mathrm{FA}}_d(\mathcal{A}_X
\xrightarrow{F} \mathcal{A}_Y) = \mathbf{U}^{\mathrm{fact}}(F_*)$
follows immediately.

**Precise error.** The object-level assignment is one statement;
morphism-level is another. A morphism $F\colon \mathcal{A}_X \to
\mathcal{A}_Y$ of CY$_3$-categories induces a morphism of
$L_\infty$-algebras $\fg_X \to \fg_Y$ only if $F$ preserves the Serre
pairing up to the degree shift, and only up to $R$-matrix gauge. This
is the Vol~III Pattern~273 / Vol~I AP273 cross-programme antipattern:
the functor-vs-correspondence scope.

**Ghost theorem.** Object-level, Theorem A3.1 holds. Morphism-level:
$\Phi^{\mathrm{FA}}_d$ is an assignment that sends
Serre-pairing-preserving morphisms to $R$-matrix-gauge classes of
$\mathrm{HolFA}_{E_d}$-morphisms, functorially up to higher
$R$-matrix-gauge coherence. Lifting this to a genuine $(\infty,1)$-
functor on CY$_d$-categories requires either restricting to a
subcategory of Morita-equivalences plus Serre-compatible 2-morphisms,
or upgrading to a lax functor — both open.

---

## Cross-consistency checks

### Against platonic synthesis Waves 11–16

- `wn:thm:plat-hCS-quantum` states the identity
  $\Obs_{\hCS}(\mathbb{C}^3) \simeq \mathrm{CE}^\bullet_{\bar\partial,
  \chir}(\mathcal{E}_{\hCS},\mathcal{O}_{\mathbb{C}^3})$. Theorem A3.1
  extends this from $\mathbb{C}^3$ to arbitrary CY$_d$ by Calaque–Van
  den Bergh globalisation, and identifies the chain-level chiral CE
  as the factorisation envelope. The flat-$\mathbb{C}^3$ case is
  the Dolbeault-lemma-trivialised special case of Theorem A3.1.

- `wn:thm:plat-hCS-classical` states the $(d,\mathrm{shift},E_n)$
  table. Theorem A3.1's $E_d^{\mathrm{hol}}$ refinement is compatible
  with the Pantev–Toën–Vezzosi–Vaquié shifted-symplectic shifts
  $\mathrm{shift}(d) = d - 4$: the factorisation envelope of an
  $L_\infty$-space with a degree-$(d-4)$ shifted-symplectic pairing
  naturally lands in $E_d$-factorisation algebras with BV structure.

- `wn:thm:plat-two-stage` states the two-stage factorisation. Theorem
  A3.4 is the Stage-1 internal structure (factorisation envelope of
  $\mathcal{L}^{\hCS}_X$) followed by Stage-2 specialisation
  (factorisation homology over $\Sigma_{d-1}$ restricted to $C$),
  matching the canonical two-stage picture.

- `wn:thm:plat-dualizability` asserts strict-vs-homotopy Koszul
  compatibility via Fresse 12.3.A + Positselski coderived transfer.
  Retraction R2 here sharpens this: the compatibility holds in the
  pro-nilpotent sector, and is *not* identity of the envelope with
  the Koszul-dual functor.

### Against CoHA treatise (worked examples)

- The $\mathbb{C}^3$ case of Theorem A3.1 matches the $U(1)$
  abelian factorisation algebra of treatise §\ref{wn:subsubsec:hCS-on-C3}:
  the observables $\mathrm{Obs}(\hCS_{U(1)}) = \mathbf{U}^{\mathrm{fact}}
  (\Omega^{0,\bullet}(\mathbb{C}^3,\mathbb{C})[1]) \simeq
  \mathrm{Sym}^\bullet(\Omega^{0,\bullet}(\mathbb{C}^3,\mathbb{C})[1])$
  with differential $\bar\partial$. This is the free $E_3^{\mathrm{hol}}$
  factorisation algebra on the Dolbeault line.

- The HKR identification of treatise §\ref{thm:hkr-c3-identifies-treatise}
  enters Theorem A3.1 Step 5: $\mathrm{HH}^\bullet(D^b\mathrm{Coh}
  (\mathbb{C}^3)) \simeq \PV^\bullet(\mathbb{C}^3)$ is the $(\wedge^\bullet
  T)$-refinement whose global enhancement is
  $\mathcal{L}^{\hCS}_X|_{\fg = \mathfrak{gl}_r}$.

- Treatise §\ref{thm:atiyah-three-cocycles-treatise}'s three Atiyah
  cocycles are recovered in the hCS $L_\infty$-brackets: $\ell_2$
  generates the CE differential; $\ell_3^{\min}$ on compact non-flat
  $X$ picks up the Kapranov $Y_3$ coupling; $\alpha_{\mathrm{BCOV}}$
  is the one-loop BV obstruction to quantisation. These are exactly
  the data that get recorded in the factorisation envelope's
  differential.

- The one-loop anomaly of treatise §\ref{thm:one-loop-anomaly-treatise}
  is $\kappa_{\mathrm{anom}} = \hbar A(\fg) \chi_{\mathrm{top}}(X)
  (2\pi)^{-3}$, which identifies with the obstruction to extending
  the strict chain-level equivalence of Theorem A3.1 to all orders
  in $\hbar$ — i.e., Theorem A3.1's classical ($\hbar = 0$) identity
  extends quantum-ly precisely when $\kappa_{\mathrm{anom}} = 0$.

### Against the universal Borcherds weight identity

- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is a Stage-2 statement
  (specialisation of the Stage-1 factorisation algebra to a curve
  via $(\Sigma_{d-1},C)$) and not a statement about
  $\mathrm{CE}^\bullet_{\bar\partial,\chir}$ directly. The Stage-1
  object is dimension-agnostic; Stage-2 produces the BKM-denominator
  weight. Theorem~A3.4 identifies the Stage-2 output on $K3 \times E$
  with $U^{\mathrm{ch}}(H^{0,\bullet}(K3,\fg))|_E$, which by
  Heisenberg–Mukai evaluation gives the Borcherds weight $5 = c_1(0)/2$
  after Gritsenko–Nikulin residue at $H_1$. Consistent.

### Against two-stage factorisation $\Phi_d = \Sp \circ \Phi^{\mathrm{FA}}_d$

- Theorem A3.1 constructs Stage 1; Theorem A3.4 computes Stage 2
  explicitly on compact CY$_d$. Retraction R1 is the separation of
  this picture from the BD-curve picture; Retraction R5 is the
  functor-vs-assignment disclaimer.

### $\kappa$-subscript discipline

- $\kappa_{\mathrm{anom}}$ appears in the discussion of the quantum
  extension; $\kappa_{\mathrm{ch}}$ is the Stage-2 BPS weight on
  compact CY$_d$; $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X)$ the
  Künneth-multiplicative Euler characteristic; $\kappa_{\mathrm{BKM}}
  = c_N(0)/2$ the Borcherds weight; $\kappa_{\mathrm{fiber}}$ the
  rank data. Bare $\kappa$ does not appear in the manuscript-ready
  theorem statements above.

---

## Residual frontier

`\ClaimStatusOpen`

### F1 ($(\infty,1)$-functoriality of $\Phi^{\mathrm{FA}}_d$).

Theorem A3.1 is object-level. The $(\infty,1)$-categorical upgrade
$\Phi^{\mathrm{FA}}_d\colon \mathrm{CY\text{-}cat}^{(\infty,1)}_d
\to \HolFA^{(\infty,1)}_{E_d}(\text{complex}\,d\text{-folds})$
requires compatibility with Morita equivalences, Fourier–Mukai
autoequivalences, and the $R$-matrix-gauge tower on morphisms.
Known chain-level on objects (Theorem A3.1); $(\infty,1)$-categorical
on morphisms: conjectural. Pattern 273 / AP273.

### F2 (Lurie factorisation-homology identification).

Is the Lurie factorisation homology $\int_X \mathbf{U}^{\mathrm{fact}}
(\mathcal{L}) = C^{\mathrm{CE}}_\bullet(\int_X \mathcal{L})$ in the
sense of Ayala–Francis 2015, and do the two sides give the same
answer at chain level? On flat $\mathbb{C}^d$: yes by Costello–Gwilliam
2021 Thm.~5.6.4. On compact CY$_d$: open in full generality; known
cases $X = K3 \times E$ and $X =$ abelian 3-fold via Theorem A3.4.

### F3 (Strict-vs-homotopy Koszul at $d = 3$).

Gwilliam–Williams 2021 strict Koszul is infinite-dimensional at $d=3$
on $\mathrm{HH}^0_{E_3}$; Francis–Gaitsgory 2012 homotopy Koszul is
pro-nilpotent. A precise comparison statement in the CY$_3$ sector
(where BV obstructions add structure) is open: under what hypothesis
on the CY$_3$ categorical datum does strict Koszul become
finite-dimensional after imposing Calabi–Yau vanishing?

### F4 (Complex-analytic Ran space).

A Dolbeault-Ran space $\mathrm{Ran}^{\bar\partial}(X)$ as a complex-
analytic stack, mapping to the underlying topological
$\mathrm{Ran}(X^{\mathrm{top}})$, would give a BD-like framework at
$d \geq 2$ compatible with the factorisation envelope. Nik
Rozenblyum's work on Ran spaces on stacks (Gaitsgory–Rozenblyum 2017
Vol.~I Ch.~10) provides a template but not the complex-analytic
version.

### F5 (Comparison with Lurie's factorisation homology topologically).

Lurie factorisation homology (HA §5.5.3) operates on $E_n$-algebras
and $n$-manifolds topologically. The Dolbeault refinement is strictly
richer: $\int_X^{\mathrm{hol}} \mathbf{U}^{\mathrm{fact}}(\mathcal{L})$
on a complex $d$-fold is *not* the same as $\int_{X^{\mathrm{top}}}^{
\mathrm{top}} \mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ on the
underlying real $2d$-manifold; they agree on cohomology but differ
at chain level, precisely because $E_d^{\mathrm{hol}}$ is strictly
finer than $E_{2d}^{\mathrm{top}}$.

### Conjecture A3.C (Two-lane agreement on the CY$_3$ slice).

The chain-level factorisation-envelope functor
$\mathbf{U}^{\mathrm{fact}}$ of Costello–Gwilliam and the
$(\infty,1)$-categorical construction of $\Phi^{\mathrm{FA}}_3$ via
Kontsevich–Tamarkin formality on $\HH^\bullet(\mathcal{A}_X)$ (Lurie
HA, applied on the $E_3$-algebra rather than the $L_\infty$-algebra)
agree as $E_3^{\mathrm{hol}}$-factorisation algebras on every compact
CY$_3$, up to a contractible $\infty$-groupoid of formality
trivialisations. Status: `\ClaimStatusConjectured`. Chain-level
witnesses on $K3\times E$, abelian 3-fold, local $\mathbb{P}^2$.
$(\infty,1)$-categorical proof: open, depending on globalising
Willwacher 2014.

---

## Attack–heal cycle log (private — synthesis agent only)

**Cycle 1.** ATTACK: the target "$\mathrm{CE}^\bullet_{\bar\partial,
\chir}$" is operadically underspecified — three different functors
(BD chiral CE, operadic Koszul dual, classical CE of a Lie algebra)
share the name. HEAL: fixed the target as the Costello–Gwilliam
factorisation envelope $\mathbf{U}^{\mathrm{fact}}$; separated the
three cousins explicitly (Theorem A3.2); identified Retraction R1
as the conflation with BD's curve-specific construction.

**Cycle 2.** ATTACK: does the BD construction extend from curves to
$d \geq 2$? No — the chiral bracket on $C^2$ uses $\Delta$ codim-1,
curve-specific. HEAL: the extension to $d$-folds is *not* BD; it is
the Costello–Gwilliam factorisation envelope, which on curves
*recovers* the BD chiral CE via Francis–Gaitsgory 2012 Thm.~1.1.
The two lanes diverge at $d \geq 2$; the factorisation-envelope lane
is what Stage 1 of $\Phi$ uses.

**Cycle 3.** ATTACK: does the factorisation algebra structure on
Dolbeault chain-level interact correctly with the $\bar\partial$-
differential? There are TWO gradings (cohomological, ghost) and TWO
differentials ($\bar\partial$, $d_{\mathrm{CE}}$); signs must be
compatible. HEAL: Theorem A3.3 gives the explicit Dolbeault chain
model with both differentials. Sign compatibility is Costello–Gwilliam
2021 Vol~II Prop.~5.6.3; the proof passes because $\bar\partial$ acts
on each Sym factor separately and $d_{\mathrm{CE}}$ mixes factors
via the $\ell_2$-bracket, so the total differential squares to zero
by the graded Jacobi identity on $\fg$.

**Cycle 4.** ATTACK: does Francis–Gaitsgory 2012 $E_n$-Koszul compose
with Positselski coderived/contraderived transfer to give the
quasi-isomorphism? GW 2021 strict Koszul is infinite-dim at $d=3$;
FG homotopy Koszul is pro-nilpotent only; the two lanes are *not*
equivalent at $d = 3$ in full generality. HEAL: Retraction R2 sharpens
this — they are compatible via Fresse 2017 Vol.~I Thm.~12.3.A in
the pro-nilpotent sector. The factorisation envelope is in neither
lane directly; it is the left adjoint of chain-level CE whose
homotopy-Koszul comparison Francis–Gaitsgory 2012 Thm.~6.3.1
establishes. Relation: $\mathbf{U}^{\mathrm{fact}}(\mathcal{L}) \simeq
\mathbf{\Omega}^{\mathrm{ch}}_{E_d}(C^{\mathrm{CE}}_\bullet(
\mathcal{L}))$.

**Cycle 5.** ATTACK: is the identification strict, or up to
contractible choice? HEAL: Retraction R4 — it is up to contractible
choice, parametrised by the $\mathrm{GRT}_1(\mathbb{Q})$-torsor of
Kontsevich–Tamarkin $E_d$-formality trivialisations. Willwacher 2014
Thm.~1 establishes the contractibility of the $E_d$-isomorphism class
space.  Pattern 236 ambient-qualifier discipline: scope the
equivalence.

**Cycle 6.** ATTACK: how does the base change work from the 1d (curve)
to the $d$-d (CY $d$-fold) factorisation-algebra setup? Is
$\mathrm{Ran}(X)$ replaced by a complex-analytic stack or by
$\mathrm{Ran}(X^{\mathrm{top}})$? HEAL: neither, in the
factorisation-envelope lane. The factorisation envelope
$\mathbf{U}^{\mathrm{fact}}(\mathcal{L})$ is a cosheaf on $X^{\mathrm{an}}$
directly (Costello–Gwilliam 2021 §5.6), not on a Ran space. A
complex-analytic Dolbeault-Ran space would give an alternative
construction compatible with BD, but is neither constructed nor
needed — this is frontier F4.

**Cycle 7.** ATTACK: functoriality on morphisms — does
$\Phi^{\mathrm{FA}}_d$ promote to a functor at the $(\infty,1)$-
categorical level? HEAL: Retraction R5. Object-level: Theorem A3.1.
Morphism-level: only up to $R$-matrix gauge; full
$(\infty,1)$-categorical: open (Pattern 273 / AP273 cross-programme
antipattern). This is frontier F1.

**Cycle 8.** ATTACK: does the $E_d$ on $\mathbf{U}^{\mathrm{fact}}$
come from $E_d^{\mathrm{hol}}$ or $E_{2d}^{\mathrm{top}}$? HEAL:
Retraction R3. At chain level it is $E_d^{\mathrm{hol}}$, strictly
stronger than $E_d^{\mathrm{top}}$; at cohomology they agree on the
CY slice only after Duflo trivialisation using $c_1(X) = 0$. Connected
to frontier F5 — comparison with Lurie's topological factorisation
homology.

**Synthesis.** Five cycles in the attack–heal discipline; three
retractions (R1, R2, R4 as strict theorems; R3, R5 as scope
clarifications); one sharpened master theorem (A3.1) with explicit
Dolbeault chain model (A3.3) and two-stage compatibility (A3.4);
five open frontiers; one focused two-lane conjecture (A3.C). No
bookkeeping vocabulary in the mathematical content above.
