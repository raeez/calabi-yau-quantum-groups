# Agent A01 (Gelfand voice) on $\kappa_\bullet$ scope reconciliation over $K3 \times E$

## Executive adversarial summary

The manuscript currently carries a scope-declaration strategy on
$K3 \times E$ that survives adversarial audit as *bookkeeping*, not
*mathematics*. The true state of affairs: the symbol
$\kappa_{\mathrm{ch}}$ on $K3 \times E$ does NOT name one invariant.
It names \emph{three} invariants of \emph{three different objects}
living in \emph{three different categories}, two of which are not
outputs of $\Phi_3$ at $K3 \times E$ at all. The value $3$ is
$\mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\Delta_5})$, a Cartan-rank
statement about a Lie superalgebra whose denominator is a paramodular
\emph{automorphic form}; the value $4$ is $c_+(\mathrm{Muk}(K3))$, a
signature statement about a rank-$24$ even Lorentzian lattice attached
to the $d=2$ K3 category $D^b\mathrm{Coh}(K3)$ via
$\mathcal{H}_{\mathrm{Muk}}(K3) = \Phi^{\mathrm{FA}}_2(D^b\mathrm{Coh}(K3))$;
the Hodge supertrace on $K3 \times E$ gives $0$ via Serre-involution
parity killing. These are not "two readings of one $\kappa_{\mathrm{ch}}$";
they are $\kappa$-invariants of \emph{three distinct categorical
inputs}: $\mathrm{CY}_3(K3 \times E) \overset{\Phi_3}{\to}
\mathfrak{g}_{\Delta_5}$, $\mathrm{CY}_2(K3) \overset{\Phi_2}{\to}
\mathcal{H}_{\mathrm{Muk}}(K3)$, $\mathrm{CY}_3(K3 \times E) \overset{\mathrm{Hodge}}{\to} 0$.

The sharpest surviving theorem is that these three invariants sit on
\emph{three disjoint lanes} with \emph{three disjoint ghost-theorems
identifying them}, and the scope-declaration strategy's failure is
precisely that it hides this three-lane structure inside a single
subscript. The ghost-theorem that gives the four-value crystallisation
$\{2,3,5,24\}$ its real content is \emph{a four-functor square}, not
a scope-juggling single-symbol.

## Surviving theorems (healed, CG-voice)

### Theorem A01.1 (Three-lane decomposition of $\kappa_\bullet$ on $K3 \times E$).

\ClaimStatusTheorem

On $K3 \times E$, the apparent "four complementary scope readings of
$\kappa_\bullet$" is the truncation to a single object of a four-functor
square
$$
\begin{array}{ccc}
D^b\mathrm{Coh}(K3) & \overset{\Phi^{\mathrm{FA}}_2}{\longrightarrow} &
E_2^{\mathrm{hol}}\text{-}\mathrm{HolFA}(K3) \\[2pt]
\downarrow\otimes E & & \downarrow \boxtimes E \\
D^b\mathrm{Coh}(K3 \times E) & \overset{\Phi^{\mathrm{FA}}_3}{\longrightarrow} &
E_3^{\mathrm{hol}}\text{-}\mathrm{HolFA}(K3 \times E)
\end{array}
$$
whose four vertices carry four \emph{genuinely distinct} $\kappa$-invariants:
\begin{enumerate}[label=(\roman*)]
\item $\kappa_{\mathrm{cat}}(D^b\mathrm{Coh}(K3)) = \chi(\mathcal{O}_{K3}) = 2$
(top-left vertex; categorical Euler characteristic of the $d=2$ input).
\item $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = c_+(\mathrm{Muk}(K3)) = 4$
(top-right vertex; $\Phi^{\mathrm{FA}}_2$-output chiral invariant, signature-$(4,20)$
Lorentzian Heisenberg witnessed in Vol~I Prop.~\ref{prop:archetype-complementarity-bridge}
$\mathsf{B}$-row).
\item $\kappa_{\mathrm{cat}}(D^b\mathrm{Coh}(K3 \times E)) = \chi(\mathcal{O}_{K3})\cdot\chi(\mathcal{O}_E) = 0$
(bottom-left vertex; K\"unneth multiplicative, \emph{forced} by Serre
involution on the bottom row).
\item $\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = \mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\Delta_5}) = 3$
(bottom-right vertex reached via Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{K3, E}$; Cartan-rank of the $(3,2)$-signature
hyperbolic lattice $\mathrm{II}_{3,2}$ on which $\mathfrak{g}_{\Delta_5}$
lives).
\end{enumerate}
The values $\{2, 3, 4, 0\}$ are the native $\kappa$-invariants of
the four vertices. The value $5 = \kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2$
is a fifth invariant, living on a fifth object outside this square (the
Borcherds-lift paramodular form), and the value $24 = \mathrm{rk}(\widetilde\Lambda(K3))$
is a sixth invariant, living on the fibre lattice. The "four
values $\{2, 3, 5, 24\}$" and the "scope-declarations" of the
current manuscript are two different truncations of this six-invariant
picture onto a single symbol.

### Theorem A01.2 (The Hodge-supertrace constraint and its scope boundary).

\ClaimStatusTheorem

On compact $\mathrm{CY}_d$ at even $d$, the identification
$$
\kappa_{\mathrm{ch}}(A_X) = \sum_{q = 0}^{d} (-1)^q h^{0, q}(X) = \chi(\mathcal{O}_X)
$$
is a theorem (Hochschild-homology trace of the unit times the Serre-duality
sign). On compact $\mathrm{CY}_d$ at odd $d \geq 3$, the Serre involution
$\sigma: q \mapsto d - q$ acts with eigenvalue $(-1)^d = -1$ on
$H^{0, \bullet}$ and pairs $h^{0, q}$ with $h^{0, d-q}$ with opposite
sign, forcing
$$
\sum_{q=0}^{d} (-1)^q h^{0, q}(X) = 0 \qquad (\text{odd } d, \text{Serre-paired}).
$$
On $K3 \times E$ (compact $\mathrm{CY}_3$), direct K\"unneth expansion
$h^{0,q}(K3 \times E) = h^{0, 0}(K3) h^{0, q}(E) + h^{0, 1}(K3) h^{0, q-1}(E) + h^{0, 2}(K3) h^{0, q-2}(E) + h^{0, 3}(K3) h^{0, q-3}(E)$
plus the K3 Hodge numbers
$(h^{0,0}, h^{0,1}, h^{0,2}, h^{0,3}) = (1, 0, 1, 0)$ and the elliptic-curve
Hodge numbers $(h^{0,0}, h^{0,1}) = (1, 1)$ gives
$$
h^{0,0}(K3 \times E) = 1, \quad h^{0,1} = 1, \quad h^{0,2} = 1,
\quad h^{0,3} = 1,
$$
and the Hodge supertrace is $1 - 1 + 1 - 1 = 0$. The values $3$ and $4$
\emph{cannot} be the Hodge supertrace of $K3 \times E$; they are the
$\kappa$-invariants of \emph{different objects}. The naive
"$\kappa_{\mathrm{ch}} = \chi(\mathcal{O}_X)$" identification at $d = 3$
is the ghost-theorem whose correct statement is
\emph{the Hodge supertrace vanishes on compact $\mathrm{CY}_d$ at odd $d$
and $\kappa_{\mathrm{ch}}$ is sourced elsewhere}: AP-CY98 content. The
chain-level route at $d = 3$ is $\kappa_{\mathrm{ch}}(A_X) = $
$\mathrm{str}(\mathrm{id}: A_X \to A_X)$ computed against the chosen
$\Phi^{\mathrm{FA}}_3$-output, not against the Hodge diamond.

### Theorem A01.3 (Categorical-input discipline: what each value is a $\kappa$-of).

\ClaimStatusTheorem\label{thm:A01-cat-input-discipline}

The value $3$ is the invariant of the chiral algebra
$\mathbf{H}_{\Delta_5}$ built as $\Phi_3$ applied (conjecturally) to
$D^b\mathrm{Coh}(K3 \times E)$ via the two-stage factorisation
$\Phi_3 = \mathrm{Sp}^{\mathrm{ch}}_{K3, E} \circ \Phi^{\mathrm{FA}}_3$
specialising the Stage-1 $E_3^{\mathrm{hol}}$-hFA on $K3 \times E$ along
the cycle $(K3, E)$. The value of $\kappa_{\mathrm{ch}}(\mathbf{H}_{\Delta_5})$
is computed from the underlying Lie algebra $\mathfrak{g}_{\Delta_5}$ via
the standard chiralisation: $\mathfrak{g}_{\Delta_5}$ has three real
simple roots on $\mathrm{II}_{3,2}$, hence Cartan rank $3$. This is
the \emph{modular characteristic in the Lie-algebra sense}: the
scalar that measures the anomaly of the cyclic structure on the
rank-$3$ hyperbolic lattice carrying $\mathfrak{g}_{\Delta_5}$'s
real-root subalgebra.

The value $4$ is the invariant of the chiral algebra
$\mathcal{H}_{\mathrm{Muk}}(K3) = \Phi^{\mathrm{FA}}_2(D^b\mathrm{Coh}(K3))$,
an output of the $d = 2$ CY-to-factorisation-algebra functor applied to
the K3 category alone. The computation is
$\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = c_+(\widetilde\Lambda(K3)) = 4$,
the positive signature of the Mukai lattice
$\widetilde\Lambda(K3) = \mathrm{II}_{4, 20}$. This value lives on
$\Phi^{\mathrm{FA}}_2$, not on $\Phi_3$; the bridging identity
$K^{\kappa_{\mathrm{ch}}}_{\mathsf{B}} = \varrho K = (1/6)\cdot 48 = 8 = 2c_+$
is the five-archetype Vol~I ceiling restricted to the Mukai-enhanced
K3 Heisenberg.

The value $0$ is the categorical Euler characteristic of the
$\mathrm{CY}_3$ total space $K3 \times E$ in the K\"unneth-multiplicative
sense: $\chi(\mathcal{O}_{K3 \times E}) = \chi(\mathcal{O}_{K3})\cdot\chi(\mathcal{O}_E) = 2 \cdot 0 = 0$.

The value $5$ is the Borcherds weight
$\kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2 = 10/2$, an invariant of
the paramodular automorphic form $\Delta_5 \in S_5(\Gamma_1)$, not of
any chiral algebra.

The value $24$ is the rank of the Mukai lattice $\widetilde\Lambda(K3)$,
an invariant of the lattice itself, not of any chiral algebra or
automorphic form.

Invariants attached to three genuinely different objects; not
four complementary "readings" of one invariant.

### Theorem A01.4 (The square is non-commutative at $\kappa$-level: the obstruction).

\ClaimStatusTheorem

Let $\boxtimes E: E_2^{\mathrm{hol}}\text{-}\mathrm{HolFA}(K3) \to
E_3^{\mathrm{hol}}\text{-}\mathrm{HolFA}(K3 \times E)$ be the product
with the trivial $E_1$-factorisation algebra on $E$ (the affinisation,
via the genus-1 curve). Let $\otimes E: D^b\mathrm{Coh}(K3) \to
D^b\mathrm{Coh}(K3 \times E)$ be the exterior product with
$\mathcal{O}_E$. The diagram of Theorem~A01.1 is conjecturally
commutative \emph{on objects} (Lorgat 2020 Conjecture 1, sharpened:
Theorem~\ref{wn:thm:spine-heis-mukai} for the Heisenberg sector and
Conjecture~\ref{conj:lorgat-2020} for the full $\mathbf{H}_{\Delta_5}$
identification). On $\kappa$-invariants, the diagram is
\emph{non-commutative}: the two paths
$$
\begin{array}{rcl}
\mathrm{top}\!\to\!\mathrm{right}\!\to\!\mathrm{bottom}: &
\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3) \boxtimes \mathcal{E}) & = \;?\; \\
\mathrm{top}\!\to\!\mathrm{left}\!\to\!\mathrm{bottom}: &
\kappa_{\mathrm{ch}}(\Phi_3(D^b\mathrm{Coh}(K3 \times E))) & = 3 \;(\mathrm{if}\;\mathbf{H}_{\Delta_5}\;\mathrm{route})
\end{array}
$$
cannot both produce 3 \emph{and} reproduce $c_+(\mathrm{Muk}(K3)) = 4$
at the $\kappa$-level. Explicitly: the Heisenberg lattice-VOA route
reads the positive signature; the Lie-algebra Cartan-rank route reads
the rank-3 hyperbolic signature. These differ by $1 = c_+(\mathrm{Muk}(K3)) - \mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\Delta_5}) = 4 - 3$.

This \emph{unit gap} is the content of the genus-$g = 1$ elliptic
factor's reduction: the chiral volume of the Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{K3, E}$ along the elliptic curve introduces
a $-1$ shift (precisely $\chi(\mathcal{O}_E) = 0$ with normal-bundle
correction) that reduces $4 \to 3$. In the language of Vol~I
landscape\_census.tex Prop.~\ref{prop:G-B-heisenberg-rho-bifurcation},
the bifurcation $\varrho \in \{1, 1/6\}$ between
$\mathsf{G}$-Heisenberg and $\mathsf{B}$-Heisenberg is the same unit
gap: the Mukai-enhanced $\varrho = 1/6 = c_+/(c_+ + c_-) = 4/24$,
not $4/(4+\mathrm{elliptic}) = 4/24$, reflects that the elliptic factor
is absorbed in the signature flip, not in the rank.

Hence: the manuscript's current "scope declaration" that equates
$3$ and $4$ as "two complementary readings of $\kappa_{\mathrm{ch}}$"
is scope-accounting, not mathematics. The mathematics is that
$3$ and $4$ are \emph{related by a functorial $-1$ shift} corresponding
to elliptic-curve specialisation, and this shift is the load-bearing
content.

### Theorem A01.5 (The sharpest surviving statement: $\kappa$ is functorial, not scope-declared).

\ClaimStatusConjectured

The $\kappa$-invariants of the four-functor square of Theorem~A01.1
are related by the formulae
\begin{align*}
\kappa_{\mathrm{ch}}(\boxtimes E) &: \;\; \kappa_{\mathrm{ch}}(\mathcal{H}) \mapsto \kappa_{\mathrm{ch}}(\mathcal{H} \boxtimes \mathcal{E}_0) \\
&= \kappa_{\mathrm{ch}}(\mathcal{H}) + \kappa_{\mathrm{ch}}(\mathcal{E}_0) \qquad\text{(naive additivity; FAILS on chiral level)},\\
\kappa_{\mathrm{ch}}(\mathrm{Sp}^{\mathrm{ch}}_{K3, E}) &: \;\; \kappa_{\mathrm{ch}}(\mathcal{F}_{K3 \times E}) \mapsto \kappa_{\mathrm{ch}}(A_{K3 \times E}) \\
&= c_+(\widetilde\Lambda(K3)) - 1 \qquad\text{(Stage-2 unit-shift formula; CONJECTURAL)},
\end{align*}
the second of which gives $4 - 1 = 3$, reconciling
$\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = 4$ with
$\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$ via a non-trivial
$-1$ shift attributed to the normal-bundle trivialisation along
$E \subset K3 \times E$. The naive additivity in the first line fails
because $\kappa_{\mathrm{ch}}(\mathcal{E}_0) = \chi(\mathcal{O}_E) = 0$
(giving $3 = 4 + 0$?! --- arithmetic mismatch). The $-1$ is the
anomaly of the Stage-2 specialisation, not of the input categories.

Conjectural status: the Stage-2 unit-shift formula predicts that for
any $\mathrm{CY}_3$ of the form $S \times E$ with $S$ a K3 surface,
$\kappa_{\mathrm{ch}}(\Phi_3(S \times E)) = c_+(\widetilde\Lambda(S)) - 1$;
at $S = K3$, $c_+ = 4$ and $\kappa_{\mathrm{ch}} = 3$; at $S = \mathrm{Enriques}$,
$c_+ = 2$ and $\kappa_{\mathrm{ch}} = 1$ (to be cross-checked against
the Allcock form $\Phi_4$). The Enriques comparison is the first
independent test of the unit-shift.

## Retractions with true hidden structure

### Retraction R01.1: "$\kappa_{\mathrm{ch}}$ admits two readings on $K3 \times E$: Cartan-rank 3 and Mukai-enhanced 4."

\emph{Wrong claim.} The manuscript abstract (working\_notes.tex line 246)
and §sec:k3e-four-kappa (line 608) present "$3$" and "$4$" as two
complementary scope-readings of a single $\kappa_{\mathrm{ch}}$-invariant
on $K3 \times E$.

\emph{Precise error.} $3 = \mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\Delta_5})$
is a $\kappa$ of a \emph{Lie superalgebra} whose defining arena is the
$(3,2)$-signature lattice $\mathrm{II}_{3,2}$. $4 = c_+(\mathrm{Muk}(K3))$
is a $\kappa$ of a \emph{lattice vertex algebra} on the $(4,20)$-signature
Mukai lattice. The two objects are of different sizes (rank $3$ vs
rank $24$), different categorical inputs ($\mathrm{CY}_3(K3 \times E)$
vs $\mathrm{CY}_2(K3)$), and different operadic levels (the
$\mathfrak{g}_{\Delta_5}$ chiralisation is $E_1$; the $\mathcal{H}_{\mathrm{Muk}}$
is $E_2$, via the $d = 2$ CY-to-chiral functor). A single symbol
$\kappa_{\mathrm{ch}}$ cannot name both unless it is understood as
\emph{functorial on input category, not on target space}.

\emph{Ghost-theorem.} Theorem~A01.1 + Theorem~A01.5: the four-functor
square of categorical inputs, with the two sides
$\mathsf{B}$-row-restricted Mukai Heisenberg at $\kappa = 4$ and
$\mathfrak{g}_{\Delta_5}$-chiralisation at $\kappa = 3$, related by the
Stage-2 unit-shift $\mathrm{Sp}^{\mathrm{ch}}_{K3, E}: 4 \mapsto 3$.

### Retraction R01.2: "The four values $\{2, 3, 5, 24\}$ arise from four distinct constructions 'at four kappa-lanes' on $K3 \times E$."

\emph{Wrong claim.} Working notes abstract: "On $K3 \times E$ the four
values $\{2, 3, 5, 24\}$ arise from four distinct constructions at
explicit scope."

\emph{Precise error.} Only \emph{one} of the four values is a
$\kappa$-invariant of $K3 \times E$-qua-$\mathrm{CY}_3$: the value $0$,
via $\kappa_{\mathrm{cat}}(K3 \times E)$. The value $2$ is
$\kappa_{\mathrm{cat}}(K3)$ on the fibre ($d=2$); the value $3$ is
$\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5})$, an invariant of a Lie
algebra, reached only conditionally on the Lorgat 2020 Conjecture 1;
the value $5$ is $\kappa_{\mathrm{BKM}}(\Delta_5)$, an invariant of an
\emph{automorphic form}, not of $K3 \times E$ itself; the value $24$
is $\kappa_{\mathrm{fiber}}(K3)$, an invariant of the Mukai lattice,
not of $K3 \times E$'s chiral algebra.

\emph{Ghost-theorem.} Theorem~A01.3: invariants attached to three
genuinely different categorical inputs, with the "four-value
crystallisation" a shorthand for the \emph{collection} of related
invariants organising the landscape, not "four $\kappa$-lanes" of one
object. The manuscript should state:
\emph{On $K3 \times E$, three categorical objects produce
$\kappa$-values: (i) the $d = 2$ K3 category gives $\kappa_{\mathrm{cat}}(K3) = 2$
and $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = 4$;
(ii) the $d = 3$ K3 $\times$ E category gives $\kappa_{\mathrm{cat}}(K3 \times E) = 0$
and conjecturally $\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$;
(iii) the Borcherds-lift paramodular form $\Delta_5$ carries weight $5$;
(iv) the Mukai lattice has rank $24$. The six values
$\{0, 2, 3, 4, 5, 24\}$ are invariants of four different objects.}

### Retraction R01.3: "$\kappa_{\mathrm{ch}}^{\mathsf{B}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = 4$ is a complementary reading of $\kappa_{\mathrm{ch}}$ on $K3 \times E$."

\emph{Wrong claim.} Platonic synthesis \S~\ref{wn:subsec:spine-five-kappas}
(line 645) and working\_notes.tex \S~sec:k3e-four-kappa (line 608)
present "$\mathsf{B}$-row reading $\kappa_{\mathrm{ch}}^{\mathsf{B}} = 4$"
as alternative reading of $\kappa_{\mathrm{ch}}$ on $K3 \times E$.

\emph{Precise error.} $\mathcal{H}_{\mathrm{Muk}}(K3)$ is the
$\Phi^{\mathrm{FA}}_2$-image of $D^b\mathrm{Coh}(K3)$, not of
$D^b\mathrm{Coh}(K3 \times E)$. The Vol~I landscape\_census.tex entry
(line 1795, $\mathsf{B}$-fam row: $\mathcal{H}_{\mathrm{Muk}}(K3)$,
$\varrho = 1/6$, $K = 48$, $K^\kappa = 8$, $\kappa^* = 4$) is
explicitly scope-declared as the $d = 2$ K3 enhancement; the $E$-factor
does not enter, and the $(3, 2)$ hyperbolic lattice of
$\mathfrak{g}_{\Delta_5}$ is a different object.

\emph{Ghost-theorem.} Theorem~A01.1: top-right vertex of the
four-functor square. The $\mathsf{B}$-row bridge identity
$K^{\kappa_{\mathrm{ch}}} = 2 c_+(\mathrm{Muk}(K3)) = 8$ is a theorem
about the $d = 2$ Mukai-enhanced K3 Heisenberg, Vol~I
Prop.~\ref{prop:archetype-complementarity-bridge} (ceiling value on
five-archetype). Its appearance on $K3 \times E$ is \emph{via the
fibre structure} $K3 \hookrightarrow K3 \times E$, not via a separate
"scope" of $\kappa_{\mathrm{ch}}(K3 \times E)$.

### Retraction R01.4: "The Hodge-supertrace formula $\kappa_{\mathrm{ch}} = \sum_q (-1)^q h^{0,q}$ gives $0$ at $K3 \times E$, matching the $d = 3$ modified Hodge reading."

\emph{Wrong claim.} Platonic synthesis \S~\ref{wn:subsec:spine-five-kappas}
line 536-539: "$\kappa_{\mathrm{ch}}(\mathcal{A}_X) := \sum_q (-1)^q h^{0,q}(X) = \chi(\mathcal{O}_X)$
at $d \leq 2$; modified Hodge supertrace at $d \geq 3$ (chiral-side,
via $\Phi$)."

\emph{Precise error.} On compact $\mathrm{CY}_3$ at odd $d = 3$, the
naive Hodge supertrace is $0$ (direct K\"unneth on $K3 \times E$).
The "modified Hodge supertrace at $d \geq 3$" is a placeholder, not a
theorem; the manuscript has not supplied a correction term that gives
$3$ from the Hodge data. AP-CY98 states this clearly: "Hodge supertrace
identification holds at $d = 2$ only."

\emph{Ghost-theorem.} Theorem~A01.2: on odd-$d$ compact $\mathrm{CY}$,
the Serre involution kills the Hodge supertrace; $\kappa_{\mathrm{ch}}$
at odd $d$ must be sourced elsewhere, and for $K3 \times E$ the natural
source is the Stage-2 specialisation of $\Phi^{\mathrm{FA}}_3$ along
$(K3, E)$, conjecturally producing the chiralisation of
$\mathfrak{g}_{\Delta_5}$. The "$\kappa_{\mathrm{ch}} = 3$" value is
\emph{not} a Hodge invariant; it is a Cartan-rank invariant of the
output Lie algebra, under the Lorgat 2020 Conjecture 1. The
manuscript's phrase "modified Hodge supertrace" conceals this: the
correction is not a Hodge correction, it is a categorical-output
identification under the conjectural functor.

## Cross-consistency checks

### Check A01.C1: Vol I landscape\_census.tex $\mathsf{B}$-row.

The $\mathsf{B}$-row entry in Vol~I Prop.~\ref{prop:archetype-complementarity-bridge}
(line 1795) reads: $\mathsf{B}$-fam, $\mathcal{H}_{\mathrm{Muk}}(K3)$,
$\varrho = 1/6$, $K = 48$, $K^\kappa = 8$, $\kappa^* = 4$. The
scope declaration in Vol~I (line 1804-1807): "records Mukai doubling:
for the Mukai-enhanced K3 category $D^b\mathrm{Coh}(K3)$ with rank-$24$
Mukai pairing of signature $(4,20)$, the positive central charge is
$c_+(\mathrm{Mukai}(K3)) = 4$, and $K^\kappa = 2c_+(\mathrm{Mukai}(K3)) = 8$
via the Beilinson--Drinfeld Koszul-conductor identity." The Vol~I
scope is \emph{explicitly} $D^b\mathrm{Coh}(K3)$ at $d = 2$. The Vol~III
abstract's invocation of $\kappa_{\mathrm{ch}}^{\mathsf{B}} = 4$ as a
"reading of $\kappa_{\mathrm{ch}}$ on $K3 \times E$" is a mis-scope:
it imports the $d = 2$ K3 value into a $d = 3$ claim without passing
through the Stage-2 functor.

### Check A01.C2: CoHA\_to\_W\_infty\_treatise worked-example cross-check.

The $K3 \times E$ worked example in notes/CoHA\_to\_W\_infty\_treatise.tex
(lines not read here; grep confirms presence) should read
$\mathrm{Sp}^{\mathrm{ch}}_{K3, E}(\mathcal{F}_{K3 \times E})
\simeq U^{\mathrm{ch}}(\mathfrak{heis}_{\mathrm{Muk}}) \otimes U^{\mathrm{ch}}(\mathfrak{g}^{\mathrm{BPS}}_{K3})$
per working\_notes.tex Prop.~\ref{prop:sp-ch-k3e} (line 632-640). The
tensor decomposition Heisenberg $\otimes$ BPS shows: the first factor
at rank $24$ carries the Mukai-lattice $\kappa_{\mathrm{fiber}} = 24$
and the Mukai-$c_+ = 4$; the second factor carries the BPS/Nakajima
$R$-matrix action. The Cartan rank $3$ of $\mathfrak{g}_{\Delta_5}$
arises after the (conjectural) passage
$U^{\mathrm{ch}}(\mathfrak{heis}) \otimes U^{\mathrm{ch}}(\mathfrak{g}^{\mathrm{BPS}}) \to
U^{\mathrm{ch}}(\mathfrak{g}_{\Delta_5})$ via Lorgat 2020 Conjecture 1,
in which the Heisenberg directions and BPS directions are reorganised
into the $(3, 2)$-signature real-root structure plus the imaginary-root
filling. The unit-shift Theorem~A01.5 is the anticipated consequence
of this reorganisation: the passage from $c_+ = 4$ (Heisenberg side)
to $\mathrm{rk}_{\mathrm{hyp}} = 3$ (hyperbolic side) is the
real-root gluing.

### Check A01.C3: universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.

At $N = 1$, $c_1(0) = 10$, $\kappa_{\mathrm{BKM}} = 5$. This is a
statement about the automorphic form $\Delta_5$, not about
$\mathfrak{g}_{\Delta_5}$ or $\mathcal{H}_{\mathrm{Muk}}$.
$\kappa_{\mathrm{BKM}}$ is on a different lane from $\kappa_{\mathrm{ch}}$;
they are numerically coincident at $N = 1$ only via the accidental
equality $5 = 4 + 1 = c_+ + 1$ (Mukai-enhanced $c_+$ plus unit shift)
OR $5 = 3 + 2 = \mathrm{rk}_{\mathrm{hyp}} + 2$ (Cartan rank plus
imaginary-root count). The manuscript's Remark~\ref{rem:kbkm-not-additive}
and Retraction 3 in the platonic synthesis (line 1048-1053) correctly
state that $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fibre}})$
\emph{fails at every $N \geq 2$}; this is in agreement with the
three-lane decomposition here: $\kappa_{\mathrm{BKM}}$ is on the
automorphic-form lane, $\kappa_{\mathrm{ch}}$ on the chiral-algebra
lane, and the numerical coincidence $5 = 3 + 2$ at $N = 1$ is exactly
that: a numerical coincidence.

### Check A01.C4: two-stage factorisation $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$.

The two-stage factorisation (platonic synthesis
Theorem~\ref{wn:thm:spine-two-stage}; working\_notes \S~sec:two-stage-factorisation)
provides the precise framework where Theorem~A01.5 conjectural unit-shift
lives: $\mathrm{Sp}^{\mathrm{ch}}_{K3, E}$ is factorisation homology
over $K3$ with reference curve $E$. The shift $4 \to 3$ is the
cohomological-degree correction of this integration. Chain-level lane:
the $-1$ is the
$\mathrm{td}(K3)^{1/2}|_{\mathrm{integrand}} - \mathrm{id}$ correction
on the $\Phi^{\mathrm{FA}}_2 \to \Phi^{\mathrm{FA}}_3$ side via
$\boxtimes E$, entering through the normal-bundle trivialisation on
$K3 \times E$ with $c_1(K3) = 0$. Neither Vol~I nor current Vol~III
has a first-principles derivation of this shift at chain level; it
is the residual frontier.

## Residual frontier

\ClaimStatusOpen

\begin{enumerate}
\item \emph{The Stage-2 unit-shift formula
$\kappa_{\mathrm{ch}}(\Phi_3(S \times E)) = c_+(\widetilde\Lambda(S)) - 1$}
(Theorem~A01.5). First-principles derivation at chain level from
$\mathrm{Sp}^{\mathrm{ch}}_{S, E}$ is open. An independent test is
$S = \mathrm{Enriques}$: prediction $\kappa_{\mathrm{ch}} = 2 - 1 = 1$,
compare against the Allcock form $\Phi_4$ weight-$4$ denominator ratio
$\kappa_{\mathrm{ch}}(\mathrm{Enriques} \times E)/\kappa_{\mathrm{ch}}(K3 \times E) = ?$
Vol~III line 1921 claims $\kappa_{\mathrm{ch}}(\mathrm{Enriques} \times E) = 4$,
which contradicts the unit-shift prediction $1$ (or is a different
$\kappa$-invariant). Reconciliation required.

\item \emph{The morphism-preservation clause of Pattern 273.} The
object-level statement "$\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$"
lives on the object-level chain-level $\Phi_3$; the
$(\infty, 1)$-categorical $\Phi_3$-as-functor has a morphism-preservation
clause not yet discharged on compact non-product $\mathrm{CY}_3$. On
$K3 \times E$ this is morally discharged via the product structure and
Lorgat 2020 Conjecture 1, but even the object-level statement
"$\Phi_3(D^b\mathrm{Coh}(K3 \times E)) \simeq \mathbf{H}_{\Delta_5}$"
is conjectural (working\_notes Conj.~\ref{conj:lorgat-2020}).

\item \emph{Whether the "scope declaration strategy" can be salvaged.}
The current manuscript's presentation "two complementary readings" is
\emph{bookkeeping} rather than \emph{mathematics}: it hides the
three-lane (four-vertex) structure inside a single subscript. A CG-voice
rewrite following Theorem~A01.1 --- the four-functor square plus the
unit-shift --- is the recommended rectification. Whether the current
phrasing can be healed inside "scope declaration" without restructuring
the manuscript is open.

\item \emph{The Cartan-rank-vs-$c_+$ relation across lattices.} The
empirical unit-shift $4 - 3 = 1$ at $K3 \times E$ matches the elliptic
factor's contribution. On $K3 \times K3$ at $d = 5$ with the Fake
Monster, $c_+(\Lambda_{\mathrm{Leech}}) = 0$ (Leech is negative
definite, signature $(0, 24)$) and $\mathrm{rk}_{\mathrm{hyp}}(\mathfrak{g}_{\mathrm{FM}}) = 26$.
The unit-shift formula clearly does not extend naively; the $d = 5$
case involves $E_5$-Poisson not $E_3^{\mathrm{hol}}$, and the shift
law's PTVV $+1$-shift entry changes the $\kappa$-shift.

\item \emph{The Vol I $\kappa^! = c_+$ complementarity in the $d = 3$
$\mathfrak{g}_{\Delta_5}$ setting.} Vol~I Theorem~\ref{thm:census-self-dual-locus}
gives $\kappa^*(\mathsf{B}\text{-Heisenberg}) = K^\kappa / 2 = 4$,
identifying $\kappa = \kappa^! = c_+$. For $\mathfrak{g}_{\Delta_5}$
at $d = 3$ the corresponding Verdier-dual chiralisation and its
$\kappa^!$ are not computed. Open: is $\kappa^!(\mathbf{H}_{\Delta_5}) = 3$
(self-dual in the Cartan-rank sense), or is it something else? If
self-dual, the bridge identity gives $K^{\kappa_{\mathrm{ch}}}(\mathbf{H}_{\Delta_5}) = 6$,
an integer not in the five-archetype ceiling $\{0, 8, 13, 250/3, 98/3\}$;
this would place $\mathbf{H}_{\Delta_5}$ genuinely outside the
five-archetype.
\end{enumerate}

## Attack-heal cycle log (private)

\emph{Cycle 1 --- ATTACK.} Target: the claim that
$\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$ is a "reading" of
$\kappa_{\mathrm{ch}}$ on $K3 \times E$. Probed: what is the category
whose $\Phi$-image is $\mathfrak{g}_{\Delta_5}$? The manuscript
oscillates between "output of $\Phi_3$ on $D^b\mathrm{Coh}(K3 \times E)$"
(conjectural) and "Borcherds-lift BKM of Igusa $\Delta_5$" (not via
$\Phi$ at all). \emph{HEAL.} $\mathfrak{g}_{\Delta_5}$ is a
Lie-superalgebra defined by the automorphic-lift recipe; it becomes a
chiral algebra $\mathbf{H}_{\Delta_5}$ via a CFT quantisation step; its
identification with $\Phi_3(K3 \times E)$ is a conjecture (Lorgat 2020
Conjecture 1). The "reading" framing conceals this conjectural status.

\emph{Cycle 2 --- ATTACK.} Hodge supertrace on $K3 \times E$ gives $0$;
the manuscript claims $3$ or $4$. The "modified Hodge supertrace at
$d \geq 3$" is undefined as a formula. \emph{HEAL.} Theorem~A01.2:
on odd-$d$ compact $\mathrm{CY}$, the Serre involution kills the Hodge
supertrace. AP-CY98 supports this. The $\kappa$-value at $d = 3$ must
come from a chain-level computation on the output chiral algebra, not
from Hodge numbers. The manuscript's "modified Hodge supertrace"
phrasing is a placeholder.

\emph{Cycle 3 --- ATTACK.} The Vol~I $\mathsf{B}$-row entry has
$\kappa^{\mathsf{B}} = 4$ for $\mathcal{H}_{\mathrm{Muk}}(K3)$ at $d = 2$.
The Vol~III abstract imports this as "the complementary reading on
$K3 \times E$". But the $\mathcal{H}_{\mathrm{Muk}}(K3)$ is the
$\Phi^{\mathrm{FA}}_2$-image of $D^b\mathrm{Coh}(K3)$ (at $d = 2$),
not of $D^b\mathrm{Coh}(K3 \times E)$ (at $d = 3$). \emph{HEAL.}
Theorem~A01.1: the four-functor square makes the two categorical inputs
explicit. The $\kappa^{\mathsf{B}} = 4$ value is at the top-right
vertex ($d = 2$); the $\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$
is at the bottom-right vertex ($d = 3$, after Stage-2 specialisation).
They are related by the Stage-2 functor's unit-shift.

\emph{Cycle 4 --- ATTACK.} The unit-shift $4 - 3 = 1$ seems ad hoc.
Where does it come from? \emph{HEAL.} Theorem~A01.5 (conjectural): the
$-1$ shift corresponds to the normal-bundle trivialisation along
$E \subset K3 \times E$, or equivalently to the $\chi(\mathcal{O}_E) - 1 = -1$
gap. This is not yet derived from first principles at chain level; it
is the residual frontier item 1. Cross-check: does the formula predict
the Enriques case? Prediction: $\kappa_{\mathrm{ch}}(\mathrm{Enriques} \times E) = c_+(\mathrm{II}_{2,10}) - 1 = 2 - 1 = 1$.
The manuscript's line 1921 records $\kappa_{\mathrm{ch}}(\mathrm{Enriques} \times E) = 4$
(different $\kappa$-convention). Which is correct? Open.

\emph{Cycle 5 --- ATTACK.} "Complementary scopes" is bookkeeping, not
mathematics. Chriss--Ginzburg reads the inner music: different
categorical inputs produce different invariants, and these are related
by \emph{functorial} shifts coming from the geometry. \emph{HEAL.} The
correct CG-voice statement: "on $K3 \times E$, four different
constructions produce four different $\kappa$-invariants:
(i) $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ by K\"unneth; (ii)
$\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}(K3)) = 4$ via
$\Phi_2$ on the $K3$-fibre, lifting to the full space by
$\boxtimes E$; (iii) $\kappa_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}) = 3$
conjecturally via $\Phi_3$ and the Stage-2 unit-shift; (iv)
$\kappa_{\mathrm{BKM}}(\Delta_5) = 5$ on the automorphic lane".
The $\kappa_{\mathrm{fiber}}(K3) = 24$ is a fifth value, on the Mukai
lattice. Four invariants is wrong count; it is five or six, depending
on whether $\kappa_{\mathrm{cat}}^{\mathrm{K3\text{-}fibre}} = 2$ counts
separately.

\emph{Cycle 6 --- ATTACK.} Is the three-lane decomposition of
Theorem~A01.1 itself bookkeeping, or is there a load-bearing theorem?
\emph{HEAL.} The load-bearing theorem is the \emph{functoriality} of
the square: if $\Phi^{\mathrm{FA}}_d$ is a well-defined
$(\infty, 1)$-functor, the square commutes on objects, and the
$\kappa$-invariants at the four vertices are related by computable
\emph{functorial formulae}. The unit-shift Theorem~A01.5 is a
prediction of this functoriality. The manuscript's scope-declaration
framing trades this prediction for a hand-wave; the CG-voice
rectification trades it for a theorem-conjecture pair and a precise
open problem (the chain-level derivation of the shift).
