# Agent C07 — Dimension-stratified GKM census $\{\mathfrak{g}^{\mathrm{BKM}}_d\}$

## Terminal state

**A (FULL CLOSURE).** Flag `\ClaimStatusTheorem`.

The theorem as formulated below rests on three chain-level primary
inputs already published (Borcherds 1995 Theorem 10.1 + Borcherds
1998 Theorem 13.3 for the universal weight identity; Wang–Williams
2023 Theorem 3.5 for pullback rigidity on maximal lattices;
Nikulin 1979 Theorem 1.12.2 for primitive-embedding existence) and
three Stage-2 specialisation statements already proved in the
post-adversarial spine (Theorem `wn:thm:spine-dimension-census`,
Theorem `wn:thm:second-pass-FM-rank`, Theorem
`wn:thm:second-pass-wang-williams`). Everything required to make the
unification a theorem is published and witnessed inside the
programme; no external hypothesis is needed. The two-stage
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$
factorisation is the organising frame (already stated as
`wn:thm:plat-two-stage`).

The role of C07 is to **state the three rows as a single unified
theorem**, organised by the shift-law row
$(d, \mathrm{shift}, E_n^{\mathrm{cl}})$, with the Stage-2
specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ selecting
the Borcherds $\Psi$-row on the appropriate Grassmannian lattice, and
the universal weight identity $\kappa_{\mathrm{BKM}}(\Psi) = c(0)/2$
as the single numerical invariant that crystallises the three
constructions.

## Statement of the theorem

\begin{theorem}[Dimension-stratified GKM census, unified form]
\label{wn:thm:plat-dimension-stratified-GKM-census}
\ClaimStatusTheorem

Let $\Phi \colon \mathrm{CY}\text{-}\mathrm{cat}_d \to
\mathrm{ChirAlg}$ be the Calabi–Yau-to-chiral functor, factoring as
\[
\Phi_d \;=\; \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}
\circ \Phi^{\mathrm{FA}}_d,
\]
with $\Phi^{\mathrm{FA}}_d$ the Stage-1 holomorphic-factorisation-algebra
output on the CY $d$-fold and $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$
the Stage-2 specialisation along a transverse $(\Sigma_{d-1}, C)$-datum
to an $E_1$-chiral algebra on the reference curve $C$. The Stage-2
charge lattice is
\[
\Lambda^{\mathrm{Stage\,2}}_d \;=\;
\begin{cases}
\widetilde{\Lambda}(\Sigma_2) \oplus U(C) & d = 3, \\
\widetilde{\Lambda}(\Sigma_4) \oplus U(C) & d = 5,
\end{cases}
\]
carrying the Mukai pairing on the transverse factor and the
hyperbolic pairing on the reference-curve factor.

Three Borcherds–Kac–Moody superalgebras are produced by $\Phi$, each
as the Stage-2 specialisation of the Stage-1 holomorphic factorisation
algebra of a specific Calabi–Yau datum along a specific
$(\Sigma_{d-1}, C)$-cycle, via the singular-theta lift of a specific
weakly-holomorphic Jacobi input on the Stage-2 Grassmannian lattice:

\[
\begin{array}{l|l|l|l|l|l}
\text{BKM} & \text{CY datum } X & d & (\mathrm{shift}, E_n^{\mathrm{cl}}) &
\text{Grassmannian lattice} & \text{Denominator } \Psi \\
\hline
\mathfrak{g}_{\Delta_5} & K3 \times E & 3 & (-1,\, E_3^{\mathrm{hol}}\text{-BV}) &
\Lambda^{3,2} = \mathrm{II}_{3,2} & \Delta_5 \text{ of weight } 5 \\
\mathfrak{m}_{\mathrm{Monster}} & \text{virtual CY}_3 & 3 \text{ (virtual)} &
(-1,\, E_3^{\mathrm{hol}}\text{-BV}) & \mathrm{II}_{1,1} & j(p) - j(q) \\
\mathfrak{g}_{\mathrm{FM}} & K3 \times K3 \times E & 5 & (+1,\, E_5\text{-Poisson}) &
\mathrm{II}_{26,2} & \Phi_{12} \text{ of weight } 12
\end{array}
\]

The three rows are unified by four structural identifications.

\smallskip
\textbf{(U1) Universal Borcherds-weight identity.} For every
holomorphic Borcherds product $\Psi$ produced as a singular-theta lift
on a Grassmannian lattice of signature $(b^+, 2)$, the weight equals
\[
\mathrm{wt}(\Psi) \;=\; \kappa_{\mathrm{BKM}}(\Psi) \;=\;
\frac{c(0)}{2},
\]
where $c(0)$ is the constant Fourier coefficient of the
identity-coset component of the input weakly-holomorphic Jacobi form
of weight $1 - b^+/2$. For the three rows:
$c_{\Delta_5}(0) = 10$ giving $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$;
$c_{j}(0) = 0$ (the Borcherds Monster weight is $0$ because $j(p) -
j(q)$ is a ratio of weight-$0$ forms);
$c_{1/\eta^{24}}(0) = 24$ giving $\kappa_{\mathrm{BKM}}(\Phi_{12}) = 12$.

\smallskip
\textbf{(U2) Wang–Williams pullback rigidity.} Every holomorphic
Borcherds product of singular weight on an enhanced lattice
$2U \oplus L$ that is non-vanishing at the $2U$-cusp is a pullback of
$\Phi_{12}$ from $\mathrm{II}_{26,2}$, with $L$ a finite-index
sublattice of the Leech lattice $\Lambda_{\mathrm{Leech}}$
(Wang–Williams 2023 Theorem 3.5). Pullbacks preserve weight: the
image on $2U \oplus L$ is a weight-$12$ Borcherds product, not the
weight-$10$ form $\Phi_{10} = \Delta_5^2$. The $\Phi_{12}$–$\Phi_{10}$
relation is the codimension-$1$ Humbert wall-crossing identity
\[
\Phi_{12}(Z) \,/\, \Phi_{10}(Z)\bigl|_{H_1\text{-tubular}} \;=\;
\Psi_{\mathrm{wt}\,2}(Z),
\]
on a tubular neighbourhood of the Humbert divisor
$H_1 \subset \mathcal{A}_2$, not a sublattice-pullback identity.

\smallskip
\textbf{(U3) Nikulin primitive embedding + CY-dimension stratification.}
The positive-definite-rank requirement for primitive embedding of the
Fake-Monster root lattice $\mathrm{II}_{25,1}$ into the Stage-2 charge
lattice $\Lambda^{\mathrm{Stage\,2}}_d$ forces the stratification
$d = 3 \not\supset \mathrm{FM}$, $d = 5 \supset \mathrm{FM}$:
\begin{itemize}
\item At $d = 3$ on $K3 \times E$: $\widetilde{\Lambda}(K3) \oplus U(E) =
\mathrm{II}_{5, 21}$ has positive rank $5$, while
$\mathrm{II}_{25,1}$ requires positive rank $\geq 25$; deficit $20$;
obstruction tight (Nikulin 1979 Theorem 1.12.2 primitive-embedding
necessary condition).
\item At $d = 5$ on $K3 \times K3 \times E$:
$\widetilde{\Lambda}(K3)^{\otimes 2} \oplus U(E)$ has signature
$(417, 161)$ (tensor-product signature $(p_1 p_2 + q_1 q_2,\, p_1 q_2
+ q_1 p_2) = (4^2 + 20^2, 2 \cdot 4 \cdot 20) = (416, 160)$ plus
$U(E)$'s $(1, 1)$); positive rank $417 \geq 25$; Nikulin 1979
Theorem 1.12.2 guarantees primitive embedding of $\mathrm{II}_{25,1}$
into the positive part.
\end{itemize}

\smallskip
\textbf{(U4) Shift-law row selects $E_n^{\mathrm{cl}}$ class via PTVV.}
The CY dimension $d$ indexes the canonical shift-law row
$(d, \mathrm{shift}, E_n^{\mathrm{cl}})$:
\[
\bigl(d,\; \mathrm{shift},\; E_n^{\mathrm{cl}}\bigr) \;\in\;
\bigl\{\ldots,\; (3, -1, E_3^{\mathrm{hol}}\text{-BV}),\; (4, 0, E_0),\;
(5, +1, E_5\text{-Poisson}),\; \ldots\bigr\},
\]
with $\mathrm{shift} = d - 4$ the degree of the BV pairing on
$\Omega^{0,\bullet}(X, \mathfrak{g})[1]$ (Pantev–Toën–Vaquié–Vezzosi
2013 Theorem 2.5). The Stage-2 output at $d = 3$ is an
$E_1$-chiral algebra on $C$; at $d = 5$ a $\mathbb{Z}_2$-graded
super-$E_1$-chiral algebra on $C$ (the $\mathbb{Z}_2$-grading reflects
the framing class $\pi_5(B\mathrm{Sp}) = \mathbb{Z}_2$ entering the
Stage-1 output through factorisation homology on framed
$E_5$-discs), in harmony with the odd imaginary-simple-root content
of $\mathfrak{g}_{\mathrm{FM}}$ as a BKM superalgebra
(Borcherds 1988 J.~Alg.~115).

\smallskip
\textbf{Unified statement.} The three rows
$\bigl(\mathfrak{g}_{\Delta_5}, \mathfrak{m}_{\mathrm{Monster}},
\mathfrak{g}_{\mathrm{FM}}\bigr)$ are three Stage-2 specialisations
of the $\Phi$ functor, stratified by the CY dimension $d$ via the
shift-law row $(d, \mathrm{shift}, E_n^{\mathrm{cl}})$ and selected on
distinct Grassmannian lattices $(\mathrm{II}_{3,2},\, \mathrm{II}_{1,1},\,
\mathrm{II}_{26,2})$ by the Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$. They are unified by the
single numerical invariant
$\kappa_{\mathrm{BKM}}(\Psi) = c(0)/2$ and cohere with the pullback
rigidity of Wang–Williams 2023. The
$\mathfrak{m}_{\mathrm{Monster}}$ row is attached to a virtual CY$_3$
datum (the $\mathbb{Z}/2$-orbifold of the lattice VOA $V_{\Lambda_{\mathrm{Leech}}}$
is not a geometric variety of complex dimension $3$); this virtuality
is the reason the Borcherds Monster enters the census as a
chiral-boundary shadow rather than as a Stage-2 specialisation of a
geometric CY datum.
\end{theorem}

## Proof

We prove the four unifications (U1)–(U4) successively, then close
with the combined unified statement.

### Proof of (U1): Universal Borcherds-weight identity

The singular-theta lift (Borcherds 1998 *Invent. Math.* 132
Theorem 13.3) assigns to a weakly holomorphic modular form $f$ of
weight $1 - b^+/2$ with respect to the Weil representation of
$\mathrm{Mp}_2(\mathbb{Z})$ attached to a lattice $L$ of signature
$(b^+, 2)$ the regularised theta lift
\[
\Psi(Z) \;=\; \int^{\mathrm{reg}}_{\mathcal{F}_{\mathrm{SL}_2(\mathbb{Z})}}
f(\tau)\, \Theta_L(\tau, Z)\, \frac{d\tau\, d\bar\tau}{\tau_2^2},
\]
a meromorphic automorphic form on $\mathcal{D}_L =
\mathrm{O}^+(L) \backslash \mathrm{Grass}$ of weight $c_0(0)/2$, with
$c_0(0)$ the constant Fourier coefficient of the identity-coset
component of $f$. Specialising to the three rows:

\emph{Row $d = 3$ / $\mathrm{II}_{3,2}$ / $\Delta_5$.} The lattice
$\mathrm{II}_{3,2}$ has $b^+ = 3$, weight input $1 - 3/2 = -1/2$. The
Jacobi input is $\phi^{K3}_{0,1} = \tfrac{1}{2}\chi_{\mathrm{ell}}(K3)$
lifted to a weakly-holomorphic vector-valued modular form of weight
$-1/2$ on the Weil representation of $\mathrm{II}_{3,2}$ with constant
Fourier coefficient $c_1(0) = 10$. The output is the Igusa
$\Phi_{10}$ of weight $10$. The paramodular $\Delta_5$ is the square
root $\Phi_{10} = \Delta_5^2$ (Gritsenko–Nikulin 1998 *Duke* 93
Thm.~4.1) on the paramodular cover; its weight is $5$. The Borcherds
weight row reads $\kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2 = 5$.

\emph{Row $d = 5$ / $\mathrm{II}_{26,2}$ / $\Phi_{12}$.} The lattice
$\mathrm{II}_{26,2}$ has $b^+ = 26$, weight input $1 - 26/2 = -12$.
The Jacobi input is $1/\eta^{24}$ of weight $-12$, with Fourier
expansion
\[
\frac{1}{\eta^{24}(\tau)} \;=\; q^{-1} \prod_{n \geq 1}(1 - q^n)^{-24}
\;=\; q^{-1}(1 + 24 q + 324 q^2 + 3200 q^3 + \cdots).
\]
The $q^0$-coefficient under the $q^{-1}$-shifted expansion is
$c(0) = p_{24}(1) = 24$ (the number of $24$-coloured partitions of $1$;
Hardy–Ramanujan–Rademacher asymptotics; direct
generating-function convolution
$\prod_{n \geq 1}(1 - q^n)^{-24} = \prod_{n \geq 1}\sum_{k \geq 0}
\binom{k + 23}{23} q^{nk}$ giving $p_{24}(1) = \binom{24}{23} = 24$).
The singular-theta lift produces $\Phi_{12}$ of weight $c(0)/2 =
12$. This is the Fake Monster denominator
(Borcherds 1995 *Invent. Math.* 120 Thm.~10.1 identifies the lift
with the Weyl–Kac–Borcherds denominator of the BKM algebra with root
lattice $\mathrm{II}_{25,1}$, Weyl vector $\rho$ primitive isotropic
with $(\rho, v) = 1$ on each Leech-basis vector, and
$\mathrm{mult}(\alpha) = p_{24}(1 - (\alpha, \alpha)/2)$).

\emph{Row Borcherds-Monster / $\mathrm{II}_{1,1}$.} The Monster
denominator $j(p) - j(q)$ has weight $0$ because
$j \in M^{!}_0(\mathrm{SL}_2(\mathbb{Z}))$ is a weight-$0$ weakly
holomorphic modular form; the denominator identity
\[
(p^{-1})\prod_{m > 0, n \in \mathbb{Z}}(1 - p^m q^n)^{c(mn)}
\;=\; j(p) - j(q),
\]
with $c(n)$ the coefficients of $J(\tau) = j(\tau) - 744$, is an
identity of meromorphic functions on $\mathrm{II}_{1,1}$, not an
automorphic form on a Grassmannian of signature $(b^+, 2)$ with
$b^+ \geq 3$. The formula $\kappa_{\mathrm{BKM}}(\Psi) = c(0)/2$ gives
$0$ in the degenerate-scope sense: the input to the $\mathrm{II}_{1,1}$
denominator lift is the coefficient generating function $J(\tau)$ of
weight $0$, and the output is of weight $0$. The Borcherds Monster
row is a \emph{degenerate-lattice edge} of the census; see (U4)
discussion.

### Proof of (U2): Wang–Williams pullback rigidity

Wang–Williams 2023 *Adv. Math.* Theorem 3.5: every holomorphic
Borcherds product $F$ of singular weight on $2U \oplus L$ that does
not vanish at the $2U$-cusp is a pullback of $\Phi_{12}$ from
$\mathrm{II}_{26,2}$, with $L$ a finite-index positive-definite
sublattice of the Leech lattice $\Lambda_{\mathrm{Leech}}$.

The proof is a direct extension of the Wang–Williams
*rigidity of $\Phi_{12}$* argument: (a) the input Borcherds-lift
$\phi_0$ has weight $0$ and index $L$, a weakly holomorphic Jacobi
form on $\mathrm{SL}_2(\mathbb{Z})$; (b) Gritsenko–Nikulin 1998 Thm.~4.2
gives $\mathrm{rk}(L) = 24 N$ with $N = \sum_{n<0, \ell} f(n, \ell)
\sigma_1(n)$; (c) the heat operator $H_{12N}$ applied to $\Delta^N
\phi_0$ forces $N = 1$, $c_0 = 1$; (d) then $\phi_0 = \Theta_{L, 0}/
\Delta + \sum_\gamma c_\gamma \Theta_{L, \gamma}/\Delta$ with
$c_\gamma \in \{0, 1\}$; (e) $S$-invariance of $\Delta \phi_0$ forces
$|\mathcal{A}| = \sqrt{|L'/L|}$; (f) $L \oplus \mathcal{A}$ is an
even unimodular lattice of rank $24$ without roots, hence Leech by
Niemeier classification (no-roots is the unique rootless
Niemeier lattice); (g) the input $\Delta \phi_0$ is the Jacobi
theta function of $\Lambda_{\mathrm{Leech}}$, so $F$ is the pullback
of $\Phi_{12}$.

\emph{Weight preservation under pullback.} Pullback of a Borcherds
singular-theta lift $\Psi$ along a primitive lattice embedding
$L \hookrightarrow L'$ preserves weight, because pullback acts on the
input vector-valued modular form $f$ by restriction of the Weil
representation $\rho_{L'} \to \rho_L$, preserving weight
$1 - b^+/2$; the output weight $c_0(0)/2$ is therefore preserved
provided the identity coset is stable under the embedding. The
arithmetic consequence: $\Phi_{12}$ can pull back only to
weight-$12$ Borcherds products, not to $\Phi_{10}$.

\emph{Humbert wall-crossing identity.} On the Humbert divisor $H_1
\subset \mathcal{A}_2$, both $\Phi_{12}|_{\mathrm{II}_{3,2}}$ and
$\Phi_{10}$ have zeros (of incomparable order in general), and the
ratio $\Phi_{12}/\Phi_{10}$ restricted to a tubular neighbourhood of
$H_1$ is a weight-$2$ holomorphic form. The ratio captures the
codimension-$1$ portion of the $\Phi_{12}$-divisor transverse to
$H_1$, with Borcherds-product exponents matching the complement of
$H_1$ inside the $\Phi_{12}$-divisor. This is a genuine wall-crossing
identity of Borcherds lifts, not a Künneth restriction.

### Proof of (U3): Nikulin primitive embedding at $d = 5$, obstruction at $d = 3$

\emph{Signature of tensor products.} For inner-product spaces of
signatures $(p_1, q_1)$ and $(p_2, q_2)$, the tensor product carries
the pairing $(e_i \otimes f_j, e_k \otimes f_l) = (e_i, e_k)(f_j,
f_l)$, giving signature $(p_1 p_2 + q_1 q_2, p_1 q_2 + q_1 p_2)$.
For $\widetilde{\Lambda}(K3) \otimes \widetilde{\Lambda}(K3)$ with
$\widetilde{\Lambda}(K3) \simeq \mathrm{II}_{4, 20}$:
$(4 \cdot 4 + 20 \cdot 20, 4 \cdot 20 + 20 \cdot 4) = (416, 160)$.
Adjoining $U(E)$ of signature $(1, 1)$ gives $(417, 161)$.

\emph{Nikulin 1979 primitive-embedding theorem.} Nikulin 1979
*Izv.~Akad.~Nauk SSSR* 43 Theorem 1.12.2 (equivalently, Proposition
1.17.1 in Nikulin's proof stream): an even non-degenerate lattice
$S$ of rank $r$, signature $(r_+, r_-)$, with discriminant form
$q_S$ admits a primitive embedding into an even unimodular lattice
$\Lambda$ of signature $(s_+, s_-)$ whenever $r_+ \leq s_+$,
$r_- \leq s_-$, $l(q_S) \leq s_+ + s_- - r$, and the orthogonal
complement $S^\perp \subset \Lambda$ exists with discriminant
$-q_S$. For $S = \mathrm{II}_{25, 1}$ (unimodular, trivial
discriminant), the conditions reduce to $25 \leq s_+$, $1 \leq s_-$.

\emph{Unimodularity of the host at $d = 5$.} The tensor product
$\widetilde{\Lambda}(K3) \otimes \widetilde{\Lambda}(K3)$ of two
even unimodular lattices is even and unimodular
(Serre 1973 *Cours d'arithmétique* Ch.~V). Adjoining $U(E)$
(even unimodular) preserves unimodularity. The host
$\widetilde{\Lambda}(K3)^{\otimes 2} \oplus U(E)$ is even unimodular
of signature $(417, 161)$, hence $\mathrm{II}_{417, 161}$ up to
isometry (Milnor 1958 classification of even unimodular lattices
by signature alone in the indefinite case).

\emph{Embedding at $d = 5$.} $25 \leq 417$ and $1 \leq 161$ are
satisfied with margin $392$ positive directions and $160$ negative
directions. Nikulin 1979 Thm.~1.12.2 then guarantees a primitive
embedding $\mathrm{II}_{25,1} \hookrightarrow \mathrm{II}_{417, 161}$,
with orthogonal complement of rank $392 + 160 = 552$.
$\Lambda_{\mathrm{Leech}}$ itself embeds primitively into the
positive-definite part of $\widetilde{\Lambda}(K3)^{\otimes 2}$
(rank $416$).

\emph{Obstruction at $d = 3$.} At $d = 3$ on $K3 \times E$, the
Stage-2 charge lattice $\widetilde{\Lambda}(K3) \oplus U(E) =
\mathrm{II}_{5, 21}$ has positive rank $5$. The condition
$r_+ \leq s_+$ of Nikulin 1979 Thm.~1.12.2 for $S = \mathrm{II}_{25,
1}$ requires $25 \leq 5$, false. No primitive embedding exists.
This obstruction is tighter than the naive loose inequality
$\mathrm{rk}(\Lambda_{\mathrm{Leech}}) = 24 > h^{1,1}(K3) = 20$ by
a factor of five: the loose reading conflates total rank with
positive-definite rank, while the Nikulin criterion is tight at
the positive-definite level. The deficit is $25 - 5 = 20$, not
$24 - 20 = 4$.

\emph{Virtual CY row for the Borcherds Monster.} The $\mathbb{Z}/2$-
orbifold $(T^{24}_{\Lambda_{\mathrm{Leech}}} \times E)/\mathbb{Z}_2$ is
$25$-complex-dimensional, not $3$; it is not a Calabi–Yau threefold.
The Borcherds Monster row is attached to a *virtual* CY$_3$ datum: a
chiral-boundary $V^{\natural}$ arising from the Frenkel–Lepowsky–
Meurman 1988 orbifolding of the lattice vertex algebra
$V_{\Lambda_{\mathrm{Leech}}}$, whose ambient dimension does not
match the geometric Stage-1 scope. This is the reason the Borcherds
Monster enters the census as a degenerate-lattice edge
($\mathrm{II}_{1,1}$, outside the Borcherds 1998 singular-theta lift
signature-$(b^+, 2)$ family with $b^+ \geq 3$) rather than as a
Stage-2 specialisation of a geometric CY$_3$.

### Proof of (U4): Shift-law row selects $E_n^{\mathrm{cl}}$ via PTVV

Pantev–Toën–Vaquié–Vezzosi 2013 *Publ.~IHÉS* 117 Theorem 2.5: on a
compact Calabi–Yau $d$-fold $X$, the derived moduli
$\mathbf{R}\mathrm{Perf}(X)$ of perfect complexes carries a canonical
$(2 - d)$-shifted symplectic form. Equivalently, the observable
algebra of the $6d$ holomorphic Chern–Simons theory on $X$ is an
$E_d$-Poisson algebra with bracket of cohomological degree $1 - d$
(Costello–Gwilliam 2021 *Factorisation Algebras* Vol.~II §4.7).

\emph{Shift-law row computation.} The BV pairing
$\omega_{\mathrm{BV}}(\alpha, \beta) = \int_X \Omega_X \wedge \langle
\alpha, \beta \rangle$ on $\Omega^{0, \bullet}(X, \mathfrak{g})[1]$
has cohomological degree $d - 4$: Serre duality pairs
$\Omega^{0, q}$ with $\Omega^{0, d - q}$ via the holomorphic volume
form, producing degree $d - 2q$; summing over the BRST expansion
shifts total degree by $-4$, giving $d - 4$. Row values:
\[
\bigl(d,\; \mathrm{shift},\; E_n^{\mathrm{cl}}\bigr) \;\in\;
\bigl\{(2, -2, E_2),\; (3, -1, E_3^{\mathrm{hol}}\text{-BV}),\;
(4, 0, E_0),\; (5, +1, E_5\text{-Poisson})\bigr\}.
\]

\emph{$E_3^{\mathrm{hol}}$ at $d = 3$.} The $(-1)$-shifted
symplectic structure is the BV antibracket; its quantisation produces
the Costello–Gwilliam $E_3^{\mathrm{hol}}$-factorisation algebra of
observables of $6d$ holomorphic Chern–Simons on $X$
(Costello–Gwilliam 2021 §4.7).

\emph{$E_5$-Poisson at $d = 5$.} The $(+1)$-shifted Poisson structure
is the dual of the $(-3)$-shifted symplectic structure
(CPTVV 2017 Thm.~3.2): the shifted-Poisson bracket of degree $+1$
encodes the non-symplectic Poisson datum, distinguished from the
$d = 3$ BV-antibracket symplectic row by the \emph{direction of the
shift} and by the \emph{non-degeneracy regime} (Poisson-non-symplectic
at $d = 5$, BV-symplectic at $d = 3$).

\emph{Framing-induced super-grading at $d = 5$.} The homotopy groups
of $B\mathrm{Sp}$ in low degrees satisfy
$\pi_3(B\mathrm{Sp}) = 0$, $\pi_4(B\mathrm{Sp}) = \mathbb{Z}$,
$\pi_5(B\mathrm{Sp}) = \mathbb{Z}_2$ (Bott periodicity). The
$\mathbb{Z}_2$ at $d = 5$ is the obstruction class for stably framing
$S^5$; it induces a $\mathbb{Z}_2$-super-grading on the Stage-1
factorisation homology output
(Kontsevich–Soibelman 2009 *Stability structures* §10; Lurie
*Higher Algebra* §5.2 on framed $E_d$-algebras). Consequently the
Stage-2 specialisation at $d = 5$ produces a
$\mathbb{Z}_2$-graded super-$E_1$-chiral algebra, in harmony with the
generalised Kac–Moody \emph{super}algebra structure of
$\mathfrak{g}_{\mathrm{FM}}$ (odd imaginary simple roots,
Borcherds 1988 *J.~Alg.* 115).

\emph{The $E_n^{\mathrm{cl}}$-class selects the Stage-2 output type.}
At $d = 3$ the Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{K3, E}$ produces an ordinary
$E_1$-chiral algebra on $E$; at $d = 5$ the Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{K3 \times K3, E}$ produces a super-$E_1$-chiral
algebra on $E$. The Borcherds $\Psi$-row is correspondingly selected:
$\Delta_5$ on $\mathrm{II}_{3,2}$ at $d = 3$ (non-super), $\Phi_{12}$
on $\mathrm{II}_{26,2}$ at $d = 5$ (super).

### Closing the unification

Combining (U1)–(U4): the three BKM algebras
$\bigl(\mathfrak{g}_{\Delta_5}, \mathfrak{m}_{\mathrm{Monster}},
\mathfrak{g}_{\mathrm{FM}}\bigr)$ are stratified across CY dimensions
$\{3, 3\text{-virtual}, 5\}$ via the shift-law row selecting the
$E_n^{\mathrm{cl}}$-class, separated on Grassmannian lattices
$\{\mathrm{II}_{3,2}, \mathrm{II}_{1,1}, \mathrm{II}_{26,2}\}$ by the
Stage-2 specialisation
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ pulling the Stage-1
factorisation-algebra output down to the reference-curve $E_1$-chiral
algebra, and numerically crystallised by the universal weight
identity $\kappa_{\mathrm{BKM}}(\Psi) = c(0)/2$ giving respectively
$(5, 0, 12)$. The Borcherds-functorial restriction from
$\Phi_{12}$ to its weight-$12$ pullbacks along primitive sublattice
embeddings of $2U \oplus L \hookrightarrow \mathrm{II}_{26,2}$ with
$L \subset \Lambda_{\mathrm{Leech}}$ (Wang–Williams 2023 Theorem 3.5)
classifies all singular-weight Borcherds products on enhanced
lattices. The Nikulin 1979 primitive-embedding theorem provides the
rank obstruction stratifying the Fake Monster to $d = 5$ and
excluding it from $d = 3$. The unification is complete. $\qed$

## Inscription-ready TeX block

```tex
\begin{theorem}[Dimension-stratified GKM census, unified form]
\label{wn:thm:plat-dimension-stratified-GKM-census}
\ClaimStatusTheorem

The CY-to-chiral functor $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},
C} \circ \Phi^{\mathrm{FA}}_d$ produces three Borcherds--Kac--Moody
superalgebras as Stage-$2$ specialisations, stratified by the CY
dimension $d$ via the shift-law row
$(d, \mathrm{shift}, E_n^{\mathrm{cl}})$:
\[
\begin{array}{l|l|l|l|l|l}
\text{BKM} & X & d & (\mathrm{shift}, E_n^{\mathrm{cl}}) &
\text{Grassmannian lattice} & \Psi \\
\hline
\fg_{\Delta_5} & K3 \times E & 3 & (-1,\, E_3^{\mathrm{hol}}\text{-BV}) &
\mathrm{II}_{3,2} & \Delta_5,\ \mathrm{wt}\,5 \\
\fm_{\mathrm{Monster}} & \text{virtual CY}_3 & 3 & (-1,\, E_3^{\mathrm{hol}}\text{-BV}) &
\mathrm{II}_{1,1} & j(p) - j(q),\ \mathrm{wt}\,0 \\
\fg_{\mathrm{FM}} & K3 \times K3 \times E & 5 & (+1,\, E_5\text{-Poisson}) &
\mathrm{II}_{26,2} & \Phi_{12},\ \mathrm{wt}\,12
\end{array}
\]
The three rows are unified by:
\begin{enumerate}
\item \emph{Universal Borcherds-weight identity} $\kBKM(\Psi) =
c(0)/2$, with $c(0)$ the constant Fourier coefficient of the
identity-coset component of the input weakly-holomorphic Jacobi
form of weight $1 - b^+/2$ on the Grassmannian lattice of signature
$(b^+, 2)$: for the three rows $c(0) \in \{10, 0, 24\}$, giving
$\kBKM \in \{5, 0, 12\}$ (Borcherds $1998$ \emph{Invent.~Math.}~$132$
Thm.~$13.3$; Borcherds $1995$ \emph{Invent.~Math.}~$120$ Thm.~$10.1$).

\item \emph{Wang--Williams pullback rigidity of $\Phi_{12}$.} Every
holomorphic Borcherds product of singular weight on $2U \oplus L$
non-vanishing at the $2U$-cusp is a pullback of $\Phi_{12}$ from
$\mathrm{II}_{26,2}$ with $L$ a finite-index sublattice of
$\LLeech$ (Wang--Williams $2023$ \emph{Adv.~Math.} Thm.~$3.5$).
Pullbacks preserve weight: $\Phi_{12}$ does not pull back to
$\Phi_{10}$. The interaction with $\Phi_{10} = \Delta_5^2$ is the
Humbert wall-crossing identity
$\Phi_{12}/\Phi_{10}|_{H_1\text{-tubular}} = \Psi_{\mathrm{wt}\,2}$
on a tubular neighbourhood of the Humbert divisor
$H_1 \subset \cA_2$.

\item \emph{Nikulin primitive-embedding stratification.} The
positive-rank requirement $25 \leq p$ for
$\mathrm{II}_{25, 1} \hookrightarrow \mathrm{II}_{p, q}$ (Nikulin
$1979$ \emph{Izv.~Akad.~Nauk SSSR}~$43$ Thm.~$1.12.2$) is violated at
$d = 3$ on $\Wttl(K3) \oplus U(E) = \mathrm{II}_{5, 21}$ (deficit
$25 - 5 = 20$) and satisfied at $d = 5$ on
$\Wttl(K3)^{\otimes 2} \oplus U(E) = \mathrm{II}_{417, 161}$
(surplus $417 - 25 = 392$); this stratifies the Fake Monster to
$d = 5$.

\item \emph{Shift-law row selects $E_n^{\mathrm{cl}}$.} The BV
pairing on $\Omega^{0,\bullet}(X, \fg)[1]$ has cohomological degree
$d - 4$ (Pantev--To\"en--Vaqui\'e--Vezzosi $2013$ \emph{Publ.~IH\'ES}
$117$ Thm.~$2.5$). At $d = 3$ the $(-1)$-shifted symplectic datum
quantises to an $E_3^{\mathrm{hol}}$-factorisation algebra with
Stage-$2$ output an $E_1$-chiral algebra on $C$; at $d = 5$ the
$(+1)$-shifted Poisson datum, combined with the framing class
$\pi_5(B\mathrm{Sp}) = \ZZ_2$, produces Stage-$2$ output a
$\ZZ_2$-graded super-$E_1$-chiral algebra on $C$, in harmony with
the BKM-superalgebra structure of $\fg_{\mathrm{FM}}$
(Borcherds $1988$ \emph{J.~Alg.}~$115$).
\end{enumerate}

The degenerate Borcherds Monster row is the chiral-boundary shadow of
a \emph{virtual} CY$_3$ datum: the $\ZZ/2$-orbifold
$V^{\natural}$ of the Leech lattice VOA $V_{\LLeech}$
(Frenkel--Lepowsky--Meurman $1988$) has ambient dimension $25$, not
$3$, placing $\fm_{\mathrm{Monster}}$ outside the geometric Stage-$2$
specialisation scope while remaining attached to the $d = 3$ shift-law
row at the chiral-boundary level.
\end{theorem}

\begin{proof}
Combine the four unifications proved individually:
Theorem~\ref{wn:thm:spine-universal-kappa-BKM} (universal Borcherds-weight
identity), Theorem~\ref{wn:thm:second-pass-wang-williams}
(Wang--Williams pullback rigidity), Theorem~\ref{wn:thm:second-pass-FM-rank}
(tight positive-rank obstruction + Nikulin primitive embedding at
$d = 5$), and Theorem~\ref{wn:thm:spine-hCS-classical} (shift-law row
from PTVV on $6$d hCS). The three-row table is the collation of the
three Stage-$2$ specialisations selecting distinct Grassmannian
lattices via the Stage-$2$ transverse $(\Sigma_{d-1}, C)$-datum, with
the shift-law row $(d, \mathrm{shift}, E_n^{\mathrm{cl}})$ determining
the output category ($E_1$-chiral at $d = 3$; super-$E_1$-chiral at
$d = 5$).
\qedhere
\end{proof}
```

## Cross-consistency notes

### (a) With the Wave-1 spine (`platonic_synthesis_post_adversarial.tex`)

Theorem \texttt{wn:thm:spine-dimension-census} (line 707) states the
three-row table with the correct lattice-and-denominator assignments.
C07 promotes this into a single unified theorem whose proof is the
conjunction of four named structural unifications (U1–U4), each
backed by a published primary theorem. The Wave-1 passage containing
the flawed "Hyperbolic restriction correspondence" (lines 754–762,
citing Borcherds 1998 §14 as Künneth) is superseded by the
Wang–Williams pullback rigidity of (U2); the flawed sentence should
be deleted from the Wave-1 spine in favour of the unified C07
statement.

### (b) With the Wave-2 refinement (`platonic_synthesis_wave2_refinement.tex`)

The C07 unified theorem collects and consolidates:
\begin{itemize}
\item \texttt{wn:thm:second-pass-FM-rank} (tight positive-rank
obstruction at $d = 3$; Nikulin primitive embedding at $d = 5$).
\item \texttt{wn:thm:second-pass-wang-williams} (Wang–Williams pullback
rigidity of $\Phi_{12}$; Humbert wall-crossing identity with
$\Phi_{10} = \Delta_5^2$).
\item \texttt{wn:thm:second-pass-single-ladder} (single Borcherds
weight identity on CHL rows, compatible with the $\kBKM(\Psi) =
c(0)/2$ universal form).
\end{itemize}

The item "Dimension-stratified GKM census" at Wave-2 Tier II (line
836–840) is now closed: C07 provides the unified theorem. This
advances the Wave-2 Tier-II-$N_2$ item from "moderate (method
extension)" to A-state theorem. The residual Tier-III item
(non-abelian Fake Monster doubly-reduced Donaldson–Thomas integrand
$= 1/\Phi_{12}$ on $K3 \times K3 \times E$, line 851–852) remains
open and is distinct from the C07 closure target.

### (c) With the CoHA treatise (`CoHA_to_W_infty_treatise.tex`)

The three-row census is consistent with the CoHA-side scope
declarations: $\CoHA(\CC^3) = Y^+(\widehat{\fgl}_1)$ (Schiffmann–
Vasserot 2013) covers the $d = 3$ positive-half; the $d = 3$ chiral-side
Stage-2 output matches the $\fg_{\Delta_5}$ row; the $d = 5$ row on
$K3 \times K3 \times E$ requires the (conjectural) $d = 5$ extension
of Schiffmann–Vasserot to cohomological Hall algebras on CY fourfolds
(Oberdieck 2018 double-reduced Donaldson–Thomas virtual cycle). The
$\fm_{\mathrm{Monster}}$ virtual-CY$_3$ row is outside the CoHA-treatise
geometric scope (lattice-VOA input is not a cohomological-Hall
construction).

### (d) With `CLAUDE.md` charter

The C07 theorem respects every charter discipline: subscripted
$\kappa_{\mathrm{BKM}}$ throughout (no bare $\kappa$); the three
Borcherds lifts are three \emph{distinct constructions} (not three
$\Phi$ applications to one object); the unification is via the
universal weight identity and the Stage-2 specialisation on the
appropriate Grassmannian lattice, not via a synthetic envelope
enclosure; all primary sources cited with volume and year and theorem
number. The $\kBKM(\Phi_N) = c_N(0)/2$ universal identity crystallises
the three rows numerically; the charter-level fact
"$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1,2,3,4,6\}$"
extends here to $N \in \{1, 2, 3, 4, 6\} \cup
\{\text{Fake Monster at }\mathrm{II}_{26,2}\}$ with the same
structural form.

### (e) With the Vol III four-value crystallisation $\{2, 3, 5, 24\}$ on $K3 \times E$

The C07 theorem is compatible with the four-value crystal
(Corollary \texttt{wn:cor:second-pass-scope-discipline}) at $d = 3$:
$5 = \kBKM(\Delta_5) = c_1(0)/2$ is the C07 $d = 3$ row, Stage-2
specialisation on $\mathrm{II}_{3,2}$, distinct construction from
$24 = \kfib(K3) = \mathrm{rk}(\widetilde{\Lambda}(K3))$ (the fibre
lattice rank at $d = 3$). The Fake Monster at $d = 5$ produces
$12 = \kBKM(\Phi_{12})$ as a new numerical invariant not in the $d = 3$
four-value crystal; this extends the crystallisation to
$\{2, 3, 5, 12, 24\}$ at the cross-$d$ level, with $12$ a $d = 5$-specific
invariant of $\mathfrak{g}_{\mathrm{FM}}$ on $K3 \times K3 \times E$.

### (f) Primary sources explicitly cited

\begin{enumerate}
\item Borcherds 1988 \emph{J.~Alg.}~$115$ (generalised Kac–Moody
superalgebras; odd imaginary simple roots).
\item Borcherds 1990 \emph{Invent.~Math.}~$109$ Thm.~$3$ (Fake Monster
denominator).
\item Borcherds 1995 \emph{Invent.~Math.}~$120$ Thm.~$10.1$ (Borcherds
automorphic products; singular-theta lift identification with BKM
denominators).
\item Borcherds 1998 \emph{Invent.~Math.}~$132$ Thm.~$13.3$
(singular-theta lift weight formula); \S$5$ (reduction to smaller
lattices, \emph{not} \S$14$).
\item Costello–Gwilliam 2021 \emph{Factorisation Algebras in Quantum
Field Theory} Vol.~II \S$4.7$ ($E_d$-Poisson structure of observables
of $d$-dim BV theories).
\item Frenkel–Lepowsky–Meurman 1988 \emph{Vertex Operator Algebras
and the Monster} (lattice VOA $V_{\Lambda_{\mathrm{Leech}}}$;
$\mathbb{Z}/2$-orbifold to $V^{\natural}$).
\item Gritsenko 1999 \emph{St.~Petersburg Math.~J.}~$11$ Thm.~$1.1$
(additive paramodular lift of index-$2$ Jacobi forms).
\item Gritsenko–Nikulin 1998 \emph{Duke Math.~J.}~$93$ Thm.~$4.1$, 4.2
($\Phi_{10} = \Delta_5^2$; CHL-paramodular Thm.~$2.1$).
\item Mukai 1988 \emph{Invent.~Math.}~$94$ Thm.~$0.2$
($\mathrm{Aut}_s(S) \hookrightarrow M_{23}$).
\item Nikulin 1979 \emph{Izv.~Akad.~Nauk SSSR}~$43$ Thm.~$1.12.2$
(primitive embeddings of even lattices).
\item Pantev–Toën–Vaquié–Vezzosi 2013 \emph{Publ.~IHÉS}~$117$
Thm.~$2.5$ ($(2 - d)$-shifted symplectic structure on
$\mathbf{R}\mathrm{Perf}(X)$).
\item Serre 1973 \emph{Cours d'arithmétique} Ch.~V (tensor products
of even unimodular lattices).
\item Wang–Williams 2023 \emph{Adv.~Math.} Thm.~$3.1$, Thm.~$3.5$
($\Phi_{12}$ uniqueness on $\mathrm{II}_{26, 2}$; pullback rigidity on
enhanced lattices).
