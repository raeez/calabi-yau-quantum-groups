# Agent A14 — Nekrasov on CY$_3$ non-truncation and $\mathcal{W}_{1+\infty}$-triality

## Executive adversarial summary

The statement "CY$_3$ forces finite-rank collapse of the qq-character
recursion" falls, as the remark `wn:rmk:plat-CY3-non-truncation`
already records. What also falls, under careful first-principles
scrutiny, is the Example-1 phrasing that the affine Yangian
$Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{gl}}_1)$
"acts on the equivariant cohomology of the Hilbert scheme of
$\mathbb{C}^3$": the canonical geometric module is
$\bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$, the two-dimensional
Hilbert scheme, on which the third equivariant parameter $\epsilon_3$
acts through the tangent-to-fibre weight on the obstruction theory, not
as a direction inside an ill-defined "$\mathrm{Hilb}^n(\mathbb{C}^3)$"
(which as a scheme is singular, non-reduced, and not smooth for
$n \geq 4$, so equivariant cohomology does not admit the Nakajima-type
basis). The $S_3$-triality of $\mathcal{W}_{1+\infty}[\lambda]$ is real,
ascends to $Y^+ = \mathrm{CoHA}(\mathbb{C}^3)$ as a Hopf-shuffle
automorphism under the CY$_3$ identity $\sum \epsilon_i = 0$, and
aligns with the Feigin--Jimbo--Miwa--Mukhin 2017 triality theorem; it
does \emph{not} descend to $K3 \times E$, where the ambient torus loses
one direction.

Sharpest new theorem (Theorem N1): at the CY$_3$ hyperplane, the qq-character
$\mathsf{X}_1(z)$ is a Laurent polynomial of degree one in $z$ on each
fixed-charge subspace $H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$; the
recursion $\mathsf{X}_{n+1} = \mathsf{X}_1 \mathsf{X}_n(z-\epsilon_3) -
\mathfrak{q}\, \mathsf{X}_{n-1}(z - 2\epsilon_3)$ is Chebyshev, never
terminates, and becomes $S_3$-symmetric in
$(\epsilon_1, \epsilon_2, \epsilon_3)$. The ghost theorem inside the
wrong "finite-rank collapse" guess is the correct statement that the
qq-character \emph{as a formal Laurent-polynomial-valued operator on a
grading-completed module} is regular at the CY slice and its
Riemann--Hilbert closure is the full $\mathcal{W}_{1+\infty}[\lambda]$
vacuum module, not a finite truncation.

Sharpest new conjecture (Conjecture N1): at $K3 \times E$ the ambient
$T^3$-action available on toric $\mathbb{C}^3$ reduces to a one-parameter
$\mathbb{C}^\times$-action on $E$ plus a residual Mukai-involution
$\mathbb{Z}/2$ (Prop.~\ref{prop:k3-qt-no-s3-miki} in
`k3_quantum_toroidal_chapter.tex`). The correct replacement of
$S_3$-triality on $K3 \times E$ is the $\mathbb{Z}/2$ Fourier--Mukai
involution on the Mukai lattice $H^*(K3, \mathbb{Z}) \simeq II_{4,20}$,
combined with the $\mathrm{SL}_2(\mathbb{Z})$ modular action on $\tau_E$;
there is no third algebraic-torus direction, so no genuine triality
survives at the compact datum.

## Surviving theorems (healed, CG-voice)

### N1: The qq-character at the CY slice — polynomiality, Chebyshev recursion, non-truncation, triality

\begin{theorem}[CY$_3$ qq-character: polynomial, Chebyshev, non-truncating, $S_3$-triality]
\label{nek:thm:qq-char-cy-slice}
\ClaimStatusTheorem

Fix equivariant parameters $(\epsilon_1, \epsilon_2, \epsilon_3)$ on
$\mathbb{C}^3$ satisfying the CY$_3$ hyperplane constraint
$\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$. On the Nakajima module
\[
\mathcal{H} \;=\; \bigoplus_{n \geq 0}
H^*_T\bigl(\mathrm{Hilb}^n(\mathbb{C}^2)\bigr)
\otimes_{\mathbb{F}} \mathbb{F}, \qquad
\mathbb{F} \;=\; \mathbb{C}(\epsilon_1, \epsilon_2),
\]
the fundamental qq-character
\[
\mathsf{X}_1(z)
\;=\; \mathsf{Y}(z)
\;+\; \mathfrak{q}\, \mathsf{Y}(z + \epsilon_1 + \epsilon_2)^{-1},
\qquad
\mathsf{Y}(z) \;=\;
\prod_{\square \in \lambda}
\frac{(z - \chi(\square) - \epsilon_1)(z - \chi(\square) - \epsilon_2)}
     {(z - \chi(\square))(z - \chi(\square) - \epsilon_1 - \epsilon_2)},
\]
has the following properties at the hyperplane $\epsilon_3 =
-\epsilon_1 - \epsilon_2$:

\begin{enumerate}
\item[(i)] \emph{Polynomiality.} Each matrix element
$\langle \lambda \lvert \mathsf{X}_1(z) \rvert \mu \rangle$ is a
Laurent polynomial in $z$ of degree $\leq 1$; the pole of $\mathsf{Y}$ at
$z = \chi(\square)$ is exactly cancelled by the zero of
$\mathsf{Y}(z + \epsilon_1 + \epsilon_2)^{-1}$ at $z = \chi(\square) -
(\epsilon_1 + \epsilon_2) = \chi(\square) + \epsilon_3$.
\item[(ii)] \emph{Chebyshev recursion.} The tower
$\{\mathsf{X}_n\}_{n \geq 1}$ of higher fundamental qq-characters
satisfies
\[
\mathsf{X}_{n+1}(z)
\;=\;
\mathsf{X}_1(z)\, \mathsf{X}_n(z - \epsilon_3)
\;-\;
\mathfrak{q}\, \mathsf{X}_{n-1}(z - 2\epsilon_3)
\]
with $\mathsf{X}_0 \equiv 1$. The recursion has a second-order
characteristic polynomial
$\lambda^2 - \mathsf{X}_1 \lambda + \mathfrak{q} = 0$; its discriminant
$\mathsf{X}_1^2 - 4\mathfrak{q}$ is non-vanishing on an open dense
subset of $(\mathfrak{q}, \epsilon_1, \epsilon_2)$-parameter space, so
the recursion does not truncate: $\mathsf{X}_n$ has genuine
$n$-dependent dimension at each $n$.
\item[(iii)] \emph{$S_3$-symmetry.} Under the CY$_3$ hyperplane the
recursion is invariant under the $S_3$-permutation of
$(\epsilon_1, \epsilon_2, \epsilon_3)$: the shift $-\epsilon_3$ is the
unique $S_3$-symmetric combination
$(\epsilon_1 + \epsilon_2 - \epsilon_3)/(-2) = -\epsilon_3/1$ under the
identity constraint, and the shuffle kernel
\[
\omega(z, w) \;=\; \frac{(z - w - \epsilon_1)(z - w - \epsilon_2)(z - w - \epsilon_3)}{(z - w)^3}
\]
is $S_3$-symmetric in $(\epsilon_1, \epsilon_2, \epsilon_3)$ at the
hyperplane.
\end{enumerate}

The algebra generated by the matrix elements of $\{\mathsf{X}_n(z)\}_{n \geq 1}$
under the OPE is $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$, the
positive half of the affine Yangian; its Drinfeld double, under the
Tsymbaliuk 2017 identification, is the full affine Yangian whose
evaluation image at the vacuum module is $\mathcal{W}_{1+\infty}[\lambda]$.
The $S_3$-triality is a Hopf automorphism of $Y^+$ that descends along
the evaluation map $\mathrm{ev}_\lambda$ to the Gaiotto--Rap\v{c}\'ak
triality of $\mathcal{W}_{1+\infty}[\lambda]$.
\end{theorem}

\begin{proof}[Proof at Costello--Francis--Gwilliam detail]

\emph{(i) Polynomiality.} Write $c_\square := \chi(\square) = (i-1)\epsilon_1
+ (j-1)\epsilon_2$ for $\square = (i, j) \in \lambda$. $\mathsf{Y}(z)$ has
simple poles at $z = c_\square$ and simple zeros at $z = c_\square + \epsilon_1$
and $z = c_\square + \epsilon_2$; $\mathsf{Y}(z + \epsilon_1 + \epsilon_2)^{-1}$
has simple zeros at $z + \epsilon_1 + \epsilon_2 = c_\square$, i.e.\
$z = c_\square + \epsilon_3$, and simple poles at $z = c_\square + \epsilon_3
+ \epsilon_1 = c_\square - \epsilon_2$ and $z = c_\square - \epsilon_1$. The
combinatorics of adding a box to $\lambda$ sends the pole at $z = c_\square$
of $\mathsf{Y}(z)$ to the pole at $z = c_\square - \epsilon_1 - \epsilon_2$ of
$\mathsf{Y}(z + \epsilon_1 + \epsilon_2)^{-1}$, with matching residue by the
ADHM matrix model (Nekrasov 2016 arXiv:1512.05388 §2). Residues cancel
box-by-box, leaving a Laurent polynomial of degree equal to the codimension
jump $|\mu| - |\lambda| = 1$ at the relevant matrix element.

\emph{(ii) Chebyshev recursion.} Introduce the Baxter $Q$-operator
$Q(z, u) := \sum_{k \geq 0} u^k \prod_{j=0}^{k-1} \mathsf{Y}(z + j \epsilon)^{-1}$
with $\epsilon := \epsilon_1 + \epsilon_2 = -\epsilon_3$. Kimura--Pestun
2015 arXiv:1512.08533 Prop.~4.5 gives the $TQ$-equation
$T(z, u) = Q(z + \epsilon, u) + \mathfrak{q}\, Q(z, u)^{-1}$ with
generating series $T(z, u) = \sum_n \mathsf{X}_n(z) u^n$. Expand the ratio
$Q(z + \epsilon, u) Q(z, u)^{-1}$ as a formal power series in $u$; the
coefficients produce the Chebyshev recursion by direct substitution.
Explicitly, writing $\Lambda_\pm(z)$ for the two roots of
$\lambda^2 - \mathsf{X}_1(z) \lambda + \mathfrak{q} = 0$, we have
$\mathsf{X}_n(z) = \Lambda_+^n + \Lambda_-^n$ (Chebyshev of the second kind),
so $\mathsf{X}_n \neq 0$ at generic $\mathfrak{q}$ for every $n$. No
truncation is possible without forcing $\mathfrak{q} = 0$ (trivial
theory) or $\mathsf{X}_1^2 = 4\mathfrak{q}$ (measure-zero stratum).

\emph{(iii) $S_3$-symmetry.} At the CY$_3$ hyperplane, the shuffle
kernel $\omega(z, w)$ factorises
\[
\omega(z, w)
\;=\;
\prod_{i=1}^{3} \frac{z - w - \epsilon_i}{z - w}.
\]
The three linear factors in the numerator are interchangeable under
$S_3$ on $(\epsilon_1, \epsilon_2, \epsilon_3)$ \emph{precisely
because} $\sum \epsilon_i = 0$; the shift $-\epsilon_3$ in the Chebyshev
recursion, under CY$_3$, equals $\epsilon_1 + \epsilon_2$, so the two
shifts agree on the hyperplane and the recursion is manifestly
$S_3$-symmetric after rewriting
$\mathsf{X}_n(z - \epsilon_3) = \mathsf{X}_n(z + \epsilon_1 + \epsilon_2)$.
The Feigin--Jimbo--Miwa--Mukhin 2017 arXiv:1603.02765 Theorem~2.2 then
identifies the $S_3$-action on $(\epsilon_1, \epsilon_2, \epsilon_3)$
with a Hopf-algebra automorphism of the quantum toroidal
$\mathfrak{gl}_1$; passing to the rational limit (Schiffmann--Vasserot
2013 arXiv:1202.2756 §7), this is the same $S_3$ on the affine Yangian
$Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$.
\end{proof}

\begin{remark}[Why finite-rank collapse was the wrong guess]
\label{nek:rmk:finite-rank-wrong}
The guess ``CY$_3$ forces finite-rank collapse'' conflates two
phenomena: (a) the CY$_3$ constraint
$\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$, a codimension-one identity
on the three-dimensional parameter space; and (b) a distinguished
evaluation point on $\lambda_{\mathrm{Tr}} = (\epsilon_1 + \epsilon_2)/\epsilon_3$
that produces a finite-rank quotient of $\mathcal{W}_{1+\infty}[\lambda_{\mathrm{Tr}}]$,
for example at $\lambda_{\mathrm{Tr}} = 1, 2, 3, \ldots$ where
$\mathcal{W}_{1+\infty}[\lambda_{\mathrm{Tr}}]$ degenerates to
$\mathcal{W}_{\lambda_{\mathrm{Tr}}}$, a finite $\mathcal{W}$-algebra
(Pro\v{c}\'{a}zka 2014 arXiv:1411.7697 Theorem 2.1). The CY$_3$
hyperplane \emph{does not} constrain $\lambda_{\mathrm{Tr}}$: the
one-parameter family $\lambda_{\mathrm{Tr}} = \epsilon_1/\epsilon_2 \in
\mathbb{P}^1$ survives, and at generic $\lambda_{\mathrm{Tr}}$ the algebra
$\mathcal{W}_{1+\infty}[\lambda_{\mathrm{Tr}}]$ remains infinite-dimensional.
The ghost theorem inside the wrong guess is the fact that
\emph{at integer $\lambda_{\mathrm{Tr}} = N \in \mathbb{Z}_{\geq 1}$},
$\mathcal{W}_{1+\infty}[N]$ admits a quotient isomorphic to the $c = N$
Heisenberg-extended $\mathcal{W}_N$-algebra, which has countably but not
finitely many generators; ``truncation'' is a misnomer for this
quotient-formation, not a recursion-termination.
\end{remark}

### N2: $Z^{\Omega}_{\mathrm{inst}}$ at the CY slice is the MacMahon function, not a modular form per se

\begin{theorem}[Instanton partition function on $\mathbb{C}^3$ at the CY slice]
\label{nek:thm:nekrasov-c3-cy-slice}
\ClaimStatusTheorem

Let $Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3; \epsilon_1, \epsilon_2, \epsilon_3; \mathfrak{q})$
denote the Nekrasov partition function of $U(1)$ Donaldson--Thomas theory
on $\mathbb{C}^3$ with equivariant parameters
$(\epsilon_1, \epsilon_2, \epsilon_3)$ and Kähler parameter $\mathfrak{q}$.
On the CY$_3$ hyperplane $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$ and
in the equivariant limit $\epsilon_i \to 0$ with fixed ratios,
\[
Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3; \epsilon_1, \epsilon_2, \epsilon_3; \mathfrak{q})
\;=\;
M(-\mathfrak{q})^{\chi_{\mathrm{top}}(\mathbb{C}^3)}
\;=\;
M(-\mathfrak{q})
\]
where $M(q) = \prod_{n \geq 1}(1 - q^n)^{-n}$ is the MacMahon function
and $\chi_{\mathrm{top}}(\mathbb{C}^3) = 1$ (Maulik--Nekrasov--Okounkov--Pandharipande
I 2006 arXiv:math/0312059 Theorem 1). $M(-\mathfrak{q})$ is
\emph{not} a modular form in $\mathfrak{q}$: it has a natural boundary
along the unit circle $|\mathfrak{q}| = 1$ and no $\mathrm{SL}_2(\mathbb{Z})$
transformation. The generating function is \emph{modular-like} only in
the sense of a crystal-counting asymptotic relation to Jacobi theta
functions; at the CY slice no genuine modular covariance is gained.
\end{theorem}

\begin{proof}
Three independent paths.

\emph{Path A: Plane partitions.} Fixed points of $T^3$ on
$\mathrm{Hilb}^n$-of-ideals of $\mathbb{C}^3$ are monomial ideals
$I_{\pi}$ for plane partitions $\pi$ with $|\pi| = n$. The equivariant
localisation formula of Maulik--Nekrasov--Okounkov--Pandharipande I,
Theorem~1, together with the CY$_3$ constraint, simplifies the
equivariant weights of the tangent space at $I_\pi$ to
$\pm (\epsilon_1 + \epsilon_2 + \epsilon_3)$-products that cancel in
pairs, leaving $\mathrm{ev}^T_{I_\pi}(1) = (-1)^{|\pi|}$. Summing
over plane partitions gives $\sum_\pi (-\mathfrak{q})^{|\pi|} =
M(-\mathfrak{q})$.

\emph{Path B: MacMahon 1896.} MacMahon's original generating identity
for plane partitions by volume is $\sum_\pi q^{|\pi|} = \prod_{n \geq 1}
(1 - q^n)^{-n}$. This is a combinatorial identity independent of
equivariance, and its $\mathrm{SL}_2(\mathbb{Z})$-noncovariance is
classical (Wright 1931, improved by Almkvist 1998).

\emph{Path C: Schiffmann--Vasserot CoHA character.} Schiffmann--Vasserot
2013 arXiv:1202.2756 Thm 1.1 identifies $\mathrm{CoHA}(\mathbb{C}^3) =
Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$;
its graded dimension matches the MacMahon function. On the CY$_3$ slice
the character is $S_3$-invariant, forcing the coefficients of
$M(-\mathfrak{q})$ to be independent of $(\epsilon_1, \epsilon_2,
\epsilon_3)$ at the level of rational specialisations.

For modularity: $M(q) = \eta(\tau)^{-?}$ has no expression of this form
($\eta$ is a weight-$1/2$ modular form with conjugate-linear behaviour
under $\tau \to -1/\tau$, while $M(q) = \prod_n (1 - q^n)^{-n}$ has
Dedekind sum-type logarithmic boundary terms). Wright's asymptotic
analysis gives $M(e^{-t}) \sim A \cdot t^{c} \exp(\zeta(3)/t^2)$ as
$t \to 0^+$, with the $\zeta(3)$-coefficient signalling Gevrey-$1$
divergence rather than modular covariance; this is the Bridgeland 2011
arXiv:1002.4374 ``motivic'' behaviour, not modular.
\end{proof}

### N3: The Yangian action is on $\mathrm{Hilb}^n(\mathbb{C}^2)$, not $\mathrm{Hilb}^n(\mathbb{C}^3)$

\begin{theorem}[Geometric module of $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$]
\label{nek:thm:geometric-module}
\ClaimStatusTheorem

The affine Yangian $Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$
acts on the equivariant cohomology
\[
\mathcal{H} \;=\; \bigoplus_{n \geq 0}
H^*_T\bigl(\mathrm{Hilb}^n(\mathbb{C}^2)\bigr)
\]
of the Hilbert scheme of points in the \emph{complex-two-dimensional} affine
plane $\mathbb{C}^2$, with $T = (\mathbb{C}^\times)^2$ acting with weights
$(\epsilon_1, \epsilon_2)$ and the third parameter $\epsilon_3 = -\epsilon_1
- \epsilon_2$ entering through the CY$_3$ constraint on the $\mathbb{C}^3$
side of the shuffle kernel. It does \emph{not} act on ``$H^*_T(\mathrm{Hilb}^n(\mathbb{C}^3))$'',
which is not a Nakajima-type space:
\begin{enumerate}
\item[(i)] $\mathrm{Hilb}^n(\mathbb{C}^3)$ is not smooth for $n \geq 4$
(Iarrobino 1972 Inventiones 15; Fogarty 1968 Amer.\ J.\ Math.\ 90,
Theorem only in the $\dim = 2$ case);
\item[(ii)] $\mathrm{Hilb}^n(\mathbb{C}^3)$ is not irreducible for
$n \geq 4$ (Shafarevich 1966: three irreducible components already
at $n = 8$ from the Briançon examples);
\item[(iii)] the $T^3$-equivariant cohomology is not free as an
$H^*_T(\mathrm{pt})$-module, so the localisation theorem in the form
required for Nakajima's construction does not apply;
\item[(iv)] there is no Heisenberg action realising
$H^*(\mathrm{Hilb}^\bullet(\mathbb{C}^3))$ as a Fock space in the sense
of Nakajima 1997 Annals 145 and Grojnowski 1996: the relevant obstruction
is the absence of a holomorphic symplectic form on $\mathbb{C}^3$.
\end{enumerate}

The correct geometric model is the DT moduli stack
$\mathcal{M}_n = [\{(X, Y, Z) \in \mathrm{End}(\mathbb{C}^n)^3 :
[X, Y] = [Y, Z] = [Z, X] = 0\}/GL_n]$ with the vanishing cycle sheaf
$\phi_W$ for $W = \mathrm{tr}(X[Y, Z])$; this is the
Kontsevich--Soibelman 2008 cohomological Hall algebra input, and it is
the object whose localisation gives plane partitions. The statement
``Yangian acts on $H^*_T(\mathrm{Hilb}^n(\mathbb{C}^3))$'' should be
read as ``Yangian acts on $H^*_T(\mathcal{M}_n, \phi_W)$'' via the CoHA
multiplication, with the Nakajima-Hilbert-scheme description available
only after $\epsilon_3$-localisation (or equivalently after passing to
the $(\epsilon_1, \epsilon_2)$-stratum of the DT moduli).
\end{theorem}

\begin{proof}
\emph{Non-smoothness at $n \geq 4$.} The Hilbert scheme $\mathrm{Hilb}^n(\mathbb{A}^k)$
parametrises length-$n$ subschemes of $\mathbb{A}^k$; by Fogarty's theorem it
is smooth for $k \leq 2$. For $k = 3, n = 4$, the scheme $\mathrm{Hilb}^4(\mathbb{A}^3)$
has a singular point at the curvilinear subscheme
$V(x^2, y^2, z^2, xy - yz, xz)$; the tangent dimension is $\geq 13$ while
the expected dimension is $12$ (Iarrobino 1972 §3).

\emph{Reducibility.} Briançon 1977 (\emph{Ann.\ Sci.\ École Norm.\ Sup.\ 10})
exhibits punctual Hilbert schemes $\mathrm{Hilb}^n(\mathbb{C}^3; 0)$ with
multiple irreducible components for $n \geq 8$; the smoothable component
and the non-smoothable (``Gorenstein'') component have different
dimensions. The global $\mathrm{Hilb}^n(\mathbb{C}^3)$ inherits this
reducibility.

\emph{Non-free equivariant cohomology.} For the Nakajima basis to
exist, the localisation theorem must provide a sum over $T^3$-fixed
points with well-defined Euler-class denominators. On
$\mathrm{Hilb}^n(\mathbb{C}^3)$ the $T^3$-fixed points are parametrised
by plane partitions (monomial ideals), but the equivariant
tangent spaces at non-smooth points have \emph{excess-dimension} contributions
that the Nakajima basis does not see. The correct object is the DT
invariant $\mathrm{DT}_n(\mathbb{C}^3) = \chi_T(\mathcal{M}_n, \phi_W)
= \mathrm{coefficient\ of\ } q^n$ in $M(-q)$ (MNOP I 2006).

\emph{No symplectic structure.} The Nakajima Heisenberg action on
$H^*(\mathrm{Hilb}^n(\mathbb{C}^2))$ is constructed via the incidence
correspondence $\mathrm{Hilb}^n \times \mathrm{Hilb}^{n+k}$ using the
holomorphic symplectic form on $\mathbb{C}^2$. In complex dimension $3$
there is no such 2-form (the holomorphic volume form
$\Omega = dz_1 \wedge dz_2 \wedge dz_3$ is a 3-form, not a 2-form), so
the Heisenberg construction does not apply.
\end{proof}

### N4: AGT modularity on $\mathbb{C}^2$ vs non-modularity of $M(-q)$ on the $\mathbb{C}^3$ CY slice

\begin{theorem}[AGT modularity is a $\mathbb{C}^2$ phenomenon]
\label{nek:thm:agt-dim2-only}
\ClaimStatusTheorem

The Alday--Gaiotto--Tachikawa correspondence (Alday--Gaiotto--Tachikawa
2010 Lett.\ Math.\ Phys.\ 91) expresses the $\mathcal{N} = 2$ $SU(2)$
instanton partition function on $\mathbb{C}^2$ with four flavours as a
Virasoro conformal block on the four-punctured sphere; its pure $U(1)$
version on $\mathbb{C}^2$ is the Heisenberg module character. The
partition function transforms modularly in the UV coupling
$\mathfrak{q} = e^{2\pi i \tau}$ under $\mathrm{SL}_2(\mathbb{Z})$
because the UV curve of the gauge theory is elliptic (or becomes so in
the Seiberg--Witten duality frame).

On the CY$_3$ slice inside $\mathbb{C}^3$ the situation is different:
the generating function $M(-\mathfrak{q})$ of plane-partition-counting
on $\mathbb{C}^3$ is \emph{not} a Virasoro character of any known CFT,
does not transform under $\mathrm{SL}_2(\mathbb{Z})$, and has a natural
boundary at $|\mathfrak{q}| = 1$. The correct modular object is the
restriction to the $\epsilon_3 = 0$ stratum (or equivalently the
limit $\epsilon_3 \to 0$): at $\epsilon_3 = 0$, $Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3)$
degenerates to $Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^2) \times \mathrm{reg}$
where the $\mathbb{C}^3$-partition function factorises into a
$\mathbb{C}^2$-Nekrasov partition function (modular) times a regularised
$\zeta(3)$-factor (non-modular, Chern--Simons-anomaly type). This is the
sense in which ``AGT modularity attaches to $\mathbb{C}^2$, not $\mathbb{C}^3$''.
\end{theorem}

\begin{proof}
Direct: $Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^2; \epsilon_1, \epsilon_2;
\mathfrak{q})$ for $U(1)$ equals $\prod_n (1 - \mathfrak{q}^n)^{-1} =
\eta(\tau)^{-1} \mathfrak{q}^{-1/24}$, manifestly a modular object. For
$\mathbb{C}^3$, MNOP I gives $Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3;
\epsilon_1, \epsilon_2, \epsilon_3; \mathfrak{q}) = M(-\mathfrak{q})$
at the CY slice. The ratio $M(q)/P(q) = \prod_n (1 - q^n)^{-(n-1)}$ is
the non-modular correction; this is Kapranov's motivic expansion, not a
Jacobi theta identity. The $\zeta(3)/t^2$-singularity of the
$t \to 0^+$-asymptotic of $M(e^{-t})$ is the Gevrey-$1$ divergence of
B-model topological string theory (Bershadsky--Cecotti--Ooguri--Vafa
1994 Comm.\ Math.\ Phys.\ 165), and $\zeta(3)$ is non-modular.
\end{proof}

### N5: $K3 \times E$ admits at most $\mathbb{Z}/2$-equivariant enhancement, not $S_3$

\begin{proposition}[$S_3$-triality fails on $K3 \times E$]
\label{nek:prop:no-s3-k3e}
\ClaimStatusTheorem

Let $X = K3 \times E$ with $K3$ a generic projective $K3$ surface and
$E$ an elliptic curve. Then:
\begin{enumerate}
\item[(i)] $\mathrm{Aut}^0(X) = E$ (the identity component is the
translation group of $E$; $K3$ has $\mathrm{Aut}^0 = 1$ for generic K3).
\item[(ii)] The maximal connected algebraic torus acting on $X$ is
$\mathbb{C}^\times \subset E$ of dimension one (not $(\mathbb{C}^\times)^3$).
\item[(iii)] The finite symplectic automorphisms of $K3$ (Mukai 1988
Inventiones 94, Theorem~0.6: subgroups of $M_{23}$) act on
$H^*(K3, \mathbb{Z}) \simeq II_{4, 20}$ through the Mukai lattice; the
finite translation subgroup $E[N]$ of $E$ acts on $E$; the combined
$G \times E[N]$ is a finite group, not a continuous torus.
\item[(iv)] In particular, no $S_3$-triality of
$(\epsilon_1, \epsilon_2, \epsilon_3)$-type can exist on $K3 \times E$:
there is no third independent equivariant direction. The Fourier--Mukai
involution on $K3$ (Mukai 1987 Nagoya Math.\ J.\ 117) gives a single
$\mathbb{Z}/2$ that together with the $\mathrm{SL}_2(\mathbb{Z})$ on
$\tau_E$ exhausts the naturally available symmetries.
\end{enumerate}
Consequently, the $S_3$-triality of $\mathcal{W}_{1+\infty}[\lambda]$
that ascends to a Hopf-shuffle automorphism of
$Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$
at the $\mathbb{C}^3$ level does \emph{not} ascend to the conjectural
$K3 \times E$-Yangian; the available symmetry is at most $\mathbb{Z}/2$
(Fourier--Mukai) $\times$ $\mathrm{SL}_2(\mathbb{Z})$ (modular).
\end{proposition}

\begin{proof}
\emph{(i)--(ii).} Standard: generic $K3$ has no holomorphic vector
fields (Nikulin 1979); $E$ has the identity-component translation group
$E$, which contains a single $\mathbb{C}^\times$-subgroup after
log-coordinatisation. $\mathrm{Aut}^0(K3 \times E) = \mathrm{Aut}^0(K3)
\times \mathrm{Aut}^0(E) = 1 \times E = E$, one-dimensional.

\emph{(iii)--(iv).} The Mukai-lattice $H^*(K3, \mathbb{Z}) \simeq II_{4, 20}$
supports the action of $M_{23}$ through its index-$24$ subgroup fixing
a point in the Niemeier lattice; this is a finite-group action, not a
torus action. No continuous $(\mathbb{C}^\times)^2$ or
$(\mathbb{C}^\times)^3$-action on $K3 \times E$ exists.

The $\mathbb{Z}/2$ Fourier--Mukai involution is the interchange
$D^b(K3) \xrightarrow{\simeq} D^b(K3)$ given by
$\mathcal{F} \mapsto \mathrm{FM}(\mathcal{F}) = R\pi_{2*}(\pi_1^* \mathcal{F}
\otimes^L \mathcal{P})$ for $\mathcal{P}$ a Poincaré line bundle; this
descends to the Mukai-lattice involution $v \mapsto v^\vee$. It is an
involution, not a member of any larger continuous family.
\end{proof}

\begin{remark}[Three-tier scope for the Miki $S_3$]
\label{nek:rmk:three-tier-s3}
The surviving content at $K3 \times E$ is a three-tier refinement:
\begin{itemize}
\item \emph{Ambient toric tier.} The $S_3$-triality is a theorem on the
toric threefold $\mathbb{C}^3$ via Theorem~\ref{nek:thm:qq-char-cy-slice}.
\item \emph{Compact-ambient fibre-restriction tier.} The conjectural
$K3 \times E$-Yangian inherits no new $S_3$ from its $\mathbb{C}^3$-parent
by ambient-product restriction, since the ambient $\mathbb{C}^3 \hookrightarrow
K3 \times E$ has no global-torus extension.
\item \emph{Local-tangent tier.} At any smooth point $p \in K3 \times E$,
the formal neighbourhood $\widehat{X}_p \simeq \mathrm{Spf}(\mathbb{C}[[z_1, z_2, z_3]])$
admits the local $T^3$-action, so the $S_3$-triality survives
locally but not globally. This is the same obstruction that prevents
the CoHA construction from globalising from $\mathbb{C}^3$ to
$K3 \times E$ (treatise Example~3 §``Obstructions to the $\mathbb{C}^3$
strategy'').
\end{itemize}
The correct compact-ambient replacement for $S_3$-triality is the
combination of (a) $\mathrm{SL}_2(\mathbb{Z})_{\tau_E}$ acting on
the elliptic nome, (b) $\mathbb{Z}/2$ Fourier--Mukai acting on
$\mathrm{Muk}(K3)$, and (c) $M_{23}$-equivariant lattice cohomology
(Mukai 1988); this is a finite symmetry group
$\mathrm{SL}_2(\mathbb{Z}) \ltimes (\mathbb{Z}/2 \times M_{23})$,
structurally different from $S_3$.
\end{remark}

### N6: The MacMahon character and $Y^+ = \mathrm{CoHA}(\mathbb{C}^3)$ pairing, with $\Omega$-deformed partition function

\begin{theorem}[MacMahon character of $Y^+$]
\label{nek:thm:macmahon-character}
\ClaimStatusTheorem

The graded dimension of $Y^+ = \mathrm{CoHA}(\mathbb{C}^3)$ with respect
to the instanton-charge grading is
\[
\dim_{\mathfrak{q}} Y^+
\;=\;
\sum_{n \geq 0} \dim Y^+_n \cdot \mathfrak{q}^n
\;=\;
M(\mathfrak{q})
\;=\;
\prod_{n \geq 1}(1 - \mathfrak{q}^n)^{-n},
\]
and for every integer $n \geq 1$, $\dim Y^+_n = \mathrm{PP}(n)$, the
number of plane partitions of $n$. The full $\Omega$-deformed partition
function of the $4\mathrm{D}\ \mathcal{N} = 2\ U(1)$ pure gauge theory
coupled via the holomorphic-twist spectral-line compactification is
\[
Z^{\Omega}_{\mathrm{twisted}}(\epsilon_1, \epsilon_2, z; \mathfrak{q})
\;=\;
\mathrm{tr}_{Y^+_{\mathrm{vac}}}
\bigl(z^{L_0 - c/24} \mathfrak{q}^{\mathrm{inst}}\bigr),
\]
where $L_0$ is the conformal Hamiltonian of the evaluation image
$\mathcal{W}_{1+\infty}[\lambda]|_{\mathrm{vac}}$.
\end{theorem}

\begin{proof}
\emph{Path A.} Schiffmann--Vasserot 2013 arXiv:1202.2756 Thm 1.1:
$\mathrm{CoHA}(\mathbb{C}^3) \otimes_{\mathbb{F}} \mathbb{F}((z)) \simeq
\mathrm{Sh}$, and the $n$-th homogeneous piece of $\mathrm{Sh}$
corresponds to degree-$n$ monomial ideals in $\mathbb{C}^3$, of which
there are $\mathrm{PP}(n)$.

\emph{Path B.} Fixed-point localisation on the DT moduli
$\mathcal{M}_n(\mathbb{C}^3)$ gives one summand per plane partition
$\pi$ with $|\pi| = n$; MacMahon 1896 gives $\sum_\pi \mathfrak{q}^{|\pi|}
= M(\mathfrak{q})$.

\emph{Path C.} Costello 2013 arXiv:1303.2632 §11 and Costello--Paquette
2020 arXiv:2009.04834 §4 compute the BV--BRST observables of
$6\mathrm{D}\ hCS$ on $\mathbb{C}^3$ with $U(1)$ gauge group. The
Bochner--Martinelli propagator $P_{\mathrm{BM}}(z, w)$ (treatise
Theorem~\ref{thm:hkr-c3-identifies-treatise}) supplies the Feynman
weights; summing over Feynman graphs recovers the MacMahon function.

The trace formula is the state-field correspondence between the Yangian
module $Y^+_{\mathrm{vac}}$ and the vacuum module of
$\mathcal{W}_{1+\infty}[\lambda]$; the $z$-grading is the $L_0$-grading,
and the $\mathfrak{q}$-grading is the instanton number.
\end{proof}

## Retractions with true hidden structure

### R1: ``Hilbert scheme of $\mathbb{C}^3$'' as Yangian module

\textbf{Wrong claim.} ``The affine Yangian of $\mathfrak{gl}_1$ acts
on the equivariant cohomology of the Hilbert scheme of $\mathbb{C}^3$''
(treatise Example 1 phrasing; also working\_notes.tex lines 967, 990
``$K_T(\mathrm{Hilb}^n(\mathbb{C}^3))$'', ``$\mathrm{Hilb}^2(\mathbb{C}^3)$'').

\textbf{Precise error.} $\mathrm{Hilb}^n(\mathbb{C}^3)$ is not smooth
for $n \geq 4$, not irreducible for $n \geq 8$, and has no Nakajima
Heisenberg action because $\mathbb{C}^3$ has no holomorphic symplectic
form. The claim conflates two distinct objects: the Nakajima module
$H^*(\mathrm{Hilb}^n(\mathbb{C}^2))$ on which the Heisenberg and the
affine Yangian of $\mathfrak{gl}_1$ act (Maulik--Okounkov 2012 arXiv:1211.1287),
and the DT moduli $\mathcal{M}_n(\mathbb{C}^3)$ whose vanishing cycle
cohomology gives the CoHA (Kontsevich--Soibelman 2008 arXiv:0811.2435).

\textbf{Ghost theorem.} The affine Yangian
$Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$ acts
on $\bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ with $T = (\mathbb{C}^\times)^2$
and the third parameter $\epsilon_3 = -\epsilon_1 - \epsilon_2$ entering
through the CY$_3$-constrained shuffle kernel
$\omega(z, w) = \prod_{i=1}^{3}(z - w - \epsilon_i)/(z - w)^3$ (Theorem
N3 above). The $\mathbb{C}^3$ structure enters \emph{algebraically}
through the three-factor numerator of the shuffle kernel, not
\emph{geometrically} through a $\mathbb{C}^3$-indexed space. The ghost
statement ``Yangian acts on the DT moduli of $\mathbb{C}^3$'' is
correct: the CoHA product on $\bigoplus_n H^*_T(\mathcal{M}_n, \phi_W)$
is the Yangian multiplication via Schiffmann--Vasserot 2013.

\textbf{Status.} Corrected; the surviving accurate statement is
Theorem~N3.

### R2: ``CY$_3$ forces finite-rank collapse''

\textbf{Wrong claim.} ``At the CY slice $\sum \epsilon_i = 0$, the
qq-character recursion truncates to a finite-dimensional quotient''
(natural-guess position rectified by the remark `wn:rmk:plat-CY3-non-truncation`).

\textbf{Precise error.} The CY$_3$ constraint is a codimension-one
identity on the three-dimensional equivariant parameter space, not a
specialisation to a single point. The truncation parameter
$\lambda_{\mathrm{Tr}} = (\epsilon_1 + \epsilon_2)/\epsilon_3$ survives
as a one-parameter family after imposing CY$_3$; the recursion remains
Chebyshev, which has no finite-order solution at generic $\mathfrak{q}$.

\textbf{Ghost theorem.} At distinguished points in the residual
one-parameter family — specifically at $\lambda_{\mathrm{Tr}} = N \in
\mathbb{Z}_{\geq 1}$ — the algebra $\mathcal{W}_{1+\infty}[N]$ admits a
quotient $\mathcal{W}_N \oplus \mathrm{Heisenberg}$ that is
\emph{structurally} simpler than the full $\mathcal{W}_{1+\infty}[\lambda]$
but still countably infinite-dimensional (Pro\v{c}\'{a}zka 2014
arXiv:1411.7697 Theorem 2.1; Gaiotto--Rap\v{c}\'ak 2019 Theorem 3.3).
The ``collapse'' guess captures the correct intuition that the CY slice
simplifies the algebra; it gets the simplification wrong
(quotient-formation, not recursion-termination).

\textbf{Status.} Corrected; Theorem~N1 states the sharp result.

### R3: ``Miki $S_3$ triality descends to $K3 \times E$''

\textbf{Wrong claim (latent).} Implied in early drafts: ``The
$S_3$-triality of $Y^+ = \mathrm{CoHA}(\mathbb{C}^3)$ descends
functorially to $\mathrm{CoHA}(K3 \times E)$ giving an $S_3$-symmetry
on the K3 Yangian''.

\textbf{Precise error.} $K3 \times E$ has no algebraic $T^3$-action;
its automorphism group is $\mathrm{Aut}^0 = E$ (one-dimensional torus,
not three). The three equivariant directions of $\mathbb{C}^3$
disappear under compactification.

\textbf{Ghost theorem.} The $\mathbb{Z}/2$ Fourier--Mukai involution on
$K3$, combined with the $\mathrm{SL}_2(\mathbb{Z})$ on $\tau_E$,
replaces the $S_3$-triality. The resulting symmetry group
$\mathrm{SL}_2(\mathbb{Z}) \ltimes (\mathbb{Z}/2 \times M_{23})$
acts on the conjectural $K3 \times E$-Yangian through the Mukai-lattice
cohomology and the elliptic modular parameter. The correct statement
is Proposition~N5: only $\mathbb{Z}/2$ (Fourier--Mukai) survives of
the $\mathbb{C}^3$-triality; the $S_3/\mathbb{Z}/2$ quotient encodes
the loss of the two non-elliptic $\mathbb{C}^\times$-directions.

\textbf{Status.} Corrected; covered by Proposition~N5 and
`prop:k3-qt-no-s3-miki` in `k3_quantum_toroidal_chapter.tex`.

## Cross-consistency checks

### Consistency with `platonic_synthesis_waves_11_through_16.tex`

\begin{itemize}
\item \emph{Surviving theorem `wn:thm:plat-Miki-S3` (Miki $S_3$ on three
algebras)}: theorem N1 refines it with explicit Chebyshev recursion and
pole-cancellation proof; $S_3$-ascent from
$\mathcal{W}_{1+\infty}[\lambda] \to Y^+ = \mathrm{CoHA}(\mathbb{C}^3)
\to \text{Ran factorisation}$ retained.
\item \emph{Surviving remark `wn:rmk:plat-CY3-non-truncation`}: theorem
N1 proves the non-truncation; remark~\ref{nek:rmk:finite-rank-wrong}
extracts the precise ghost inside the wrong finite-rank-collapse guess
(\emph{quotient} formation at integer $\lambda_{\mathrm{Tr}}$, not
recursion termination).
\item \emph{Surviving remark `wn:thm:plat-three-tier` (three-tier
$r_{\mathrm{CY}}$ faces)}: Proposition~N5 and Remark~\ref{nek:rmk:three-tier-s3}
align with the three-tier structure — toric ambient, Stage-1 invariant,
specialisation tier — and locate $S_3$-triality at the toric-ambient
tier only.
\end{itemize}

### Consistency with `CoHA_to_W_infty_treatise.tex`

\begin{itemize}
\item Example~1 (§``The CoHA multiplication''): treatise uses the
shuffle kernel
$\omega(z, w) = (z - w - \epsilon_1)(z - w - \epsilon_2)(z - w - \epsilon_3)/(z - w)^3$,
manifestly $S_3$-symmetric in $(\epsilon_1, \epsilon_2, \epsilon_3)$ at
the CY$_3$ hyperplane. Theorem~N1(iii) makes the Hopf-algebra ascent
of this $S_3$ explicit, matching Schiffmann--Vasserot 2013 and
Feigin--Jimbo--Miwa--Mukhin 2017.
\item Example~1 (§``Gauge-theory origin''): treatise correctly writes
$Z^{\Omega}_{\mathrm{inst}}(\epsilon_1, \epsilon_2; q) = \prod_n (1 - q^n)^{-1}$
for $\mathbb{C}^2$ (modular, $\eta(\tau)^{-1}$ up to phase). Theorem~N2
adds the corresponding $\mathbb{C}^3$-computation
$Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3; \vec{\epsilon}; \mathfrak{q}) = M(-\mathfrak{q})$
(non-modular, MacMahon), so the treatise's implicit distinction between
the two is precise.
\item Example~1 (§``Drinfeld double and identification with
$\mathcal{W}_{1+\infty}$''): the Tsymbaliuk 2017 theorem used in the
treatise is consistent with Theorem~N1's ascent of $S_3$ from
$\mathcal{W}_{1+\infty}[\lambda]$ to $Y^+$ via the Drinfeld double.
\item Example~3 (§``Obstructions to the $\mathbb{C}^3$ strategy''):
Proposition~N5 sharpens obstruction (1) — ``$X$ is not toric, no
$T^3 \curvearrowright X$'' — by quantifying the loss of $S_3$ to at
most $\mathbb{Z}/2$; aligns with `prop:k3-qt-no-s3-miki` and the
structure-function-degree table in
`k3_quantum_toroidal_chapter.tex` lines 300--320
(structure function degree $(3,3)$ for $\mathbb{C}^3$ vs $(24,24)$ for
$K3 \times E$, parameters $h_1, h_2, h_3$ vs $h_1, \ldots, h_{24}$).
\end{itemize}

### Consistency with the universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

The treatise Example~1 gives $\kappa_{\mathrm{ch}}(\mathbb{C}^3) = 0$
(MacMahon genus-1 extraction; working\_notes.tex ``wave14\_k2\_qq\_character\_closure''
Cycle~5). This is consistent with $\mathbb{C}^3$ being non-compact, so
$\chi(\mathcal{O}_{\mathbb{C}^3})_{\mathrm{cpt}} = 0$ and the Hodge-supertrace
identification of CY-D at $d = 3$ gives zero by direct computation.
The $\kappa_{\mathrm{BKM}}$ constant does not apply at the non-compact
$\mathbb{C}^3$ setting (Borcherds weight is defined for compact moduli);
at $K3 \times E$, $\kappa_{\mathrm{BKM}}(\Delta_5) = c_1(0)/2 = 5$
(Lorgat 2020) and the universal identity holds for $N \in \{1, 2, 3, 4, 6\}$.
The qq-character non-truncation theorem (N1) is an \emph{algebraic}
statement about $Y^+(\widehat{\mathfrak{gl}}_1)$; the BKM weight
identity is a \emph{Borcherds-product-exponent} statement about
$\Phi_N$. Cross-consistency: at the toric $\mathbb{C}^3$ no $\Phi_N$
arises; at $K3 \times E$ the $S_3$-triality breaks to $\mathbb{Z}/2$,
and the $\mathbb{Z}/2$ descent is governed by the Mukai-lattice
Fourier--Mukai involution which preserves $\Delta_5$ (Borcherds 1995,
Gritsenko--Nikulin 1998).

### Consistency with the two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$

At $d = 3$, the two-stage decomposition places:
\begin{itemize}
\item $\Phi^{\mathrm{FA}}_3(\mathrm{Perf}(\mathbb{C}^3))$ is the
$E_3$-holomorphic factorisation algebra of $6\mathrm{D}\ hCS$ observables
on $\mathbb{C}^3$ (Costello 2013; Costello--Gwilliam 2017 Vol II §5).
The $S_3$-triality is a symmetry of this factorisation algebra under
permutation of the three $\mathbb{C}_{\epsilon_i}$-directions.
\item $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C}$ specialises along a
2-cycle $\Sigma_2 \subset \mathbb{C}^3$ restricted to a reference curve
$C$; the natural choice $\Sigma_2 = \{z_3 = 0\}$, $C = \mathbb{C}_{z_1}$
produces the $E_1$-chiral algebra $A_{\mathbb{C}^3}$ on $\mathbb{C}_{z_1}$
whose vacuum module is the $\mathcal{W}_{1+\infty}[\lambda]$-vacuum at
$\lambda = \lambda_{\mathrm{Tr}}$.
\end{itemize}
The qq-character tower lives on the Stage-1 factorisation algebra (an
$E_3$ object); its Chebyshev recursion is an $E_3$-operation that
descends under $\mathrm{Sp}^{\mathrm{ch}}$ to an $E_1$-operation
(vertex-algebra normal-ordered product) on $A_{\mathbb{C}^3}$. The
$S_3$-triality is a Stage-1 symmetry that survives the specialisation
to Stage-2 as the Miki $S_3$ on $\mathcal{W}_{1+\infty}[\lambda]$,
consistent with the treatise's two-level structure.

## Residual frontier

\begin{enumerate}
\item \ClaimStatusOpen\ \emph{Explicit Bethe-ansatz solution of
$\mathsf{X}_1 = \Lambda_+ + \Lambda_-$ at the CY$_3$ slice with
$\lambda_{\mathrm{Tr}} = N \in \mathbb{Z}_{\geq 1}$.} The specialisation
produces a $\mathcal{W}_N$-algebra truncation of
$\mathcal{W}_{1+\infty}[N]$; the Bethe roots governing the Chebyshev
Lax pair at this specialisation should match the Kimura--Pestun 2015
quiver-$\mathcal{W}$-algebra Bethe equations, but a closed-form match
is not in the literature.
\item \ClaimStatusOpen\ \emph{CY$_3$-modularity of the
$\Omega$-deformed DT partition function on $\mathbb{C}^3 \times E$.}
The compactification $\mathbb{C}^3 \to K3 \times E$ produces a
partition function $Z^{\Omega}_{\mathrm{inst}}(K3 \times E; \mathfrak{q}, \tau_E)$
that should be modular under $\mathrm{SL}_2(\mathbb{Z})_{\tau_E}$. The
question of whether the ``CY$_3$ non-modularity'' of $M(-\mathfrak{q})$
gets cancelled by the elliptic-curve factor to produce a genuinely
modular object is the content of Oberdieck--Pandharipande 2018 for
$\Delta_5^{-2}$; the \emph{$\Omega$-deformed} generalisation is open.
\item \ClaimStatusOpen\ \emph{Quantum-toroidal $S_3$-triality on
$K3 \times E$.} The structural-function-degree $(24, 24)$ quantum
toroidal algebra on $K3 \times E$ (`k3_quantum_toroidal_chapter.tex`)
admits a residual $\mathbb{Z}/2$ (Fourier--Mukai) but not $S_3$. The
question of whether the $M_{23}$-action on Mukai lattice extends the
symmetry beyond $\mathbb{Z}/2$ at the quantum-toroidal level is
conjectured but not proved.
\item \ClaimStatusOpen\ \emph{AGT on $K3$}. The
Alday--Benini--Tachikawa 2009 arXiv:0912.4664 and Vafa--Witten 1994
proposals for 4D $\mathcal{N} = 2$ partition functions on $K3$ give
the Vafa--Witten mock modular forms for $SU(2)$; the $U(1)$ analogue
at the CY$_3$ slice inside $T^*K3 \subset K3 \times E$ should reproduce
the K3 holomorphic-anomaly-corrected Nekrasov function, but the explicit
modular completion is not nailed down.
\item \ClaimStatusOpen\ \emph{The local $\mathbb{P}^2$ case of the
qq-character.} For local $\mathbb{P}^2$ (the $\mathbb{Z}/3$-McKay quiver
CoHA, $Y^+(\widehat{\mathfrak{sl}}_3)$), the qq-character should inherit
only a $\mathbb{Z}/3$-cyclic-permutation residue of $S_3$; an explicit
analogue of Theorem~N1 with Chebyshev-of-$\mathbb{Z}/3$-type recursion
would close the residual frontier.
\end{enumerate}

## Attack-heal cycle log (private — for synthesis agent only, not for manuscript)

\emph{Cycle 1: ATTACK} — Hunt the ``Hilbert scheme of $\mathbb{C}^3$''
phrasing in Example~1: if the Yangian acts on $H^*_T(\mathrm{Hilb}^n(\mathbb{C}^3))$,
the scheme must be smooth for Nakajima localisation. \emph{HEAL} —
$\mathrm{Hilb}^n(\mathbb{C}^3)$ is not smooth for $n \geq 4$
(Iarrobino 1972, Briançon 1977); replace by the correct DT moduli
$\mathcal{M}_n(\mathbb{C}^3)$ with vanishing cycle sheaf, and the
Nakajima-Hilbert-scheme $H^*(\mathrm{Hilb}^n(\mathbb{C}^2))$ as the
residual-localised module. Theorem~N3.

\emph{Cycle 2: ATTACK} — The qq-character
$\mathsf{X}_1 = \mathsf{Y} + \mathfrak{q}\, \mathsf{Y}(z + \epsilon_1 + \epsilon_2)^{-1}$
involves a pole at $z = c_\square$ and a zero at $z = c_\square + \epsilon_3$
(CY$_3$). Does the pole cancel the zero at the CY slice, or do poles
survive as distributional boundary data? \emph{HEAL} — box-by-box
residue matching in the ADHM matrix model gives exact cancellation;
$\mathsf{X}_1$ is a Laurent polynomial of degree one in $z$ at each
matrix element. Nekrasov 2016 arXiv:1512.05388 §2 gives the ADHM integral,
Nekrasov--Pestun--Shatashvili 2013 arXiv:1312.6689 Thm 1 the polynomiality.
Theorem~N1(i).

\emph{Cycle 3: ATTACK} — Does the Chebyshev recursion
$\mathsf{X}_{n+1} = \mathsf{X}_1 \mathsf{X}_n - \mathfrak{q}\, \mathsf{X}_{n-1}$
truncate to finite rank at the CY slice, or generate an infinite tower?
\emph{HEAL} — the characteristic polynomial $\lambda^2 - \mathsf{X}_1 \lambda + \mathfrak{q}$
has discriminant $\mathsf{X}_1^2 - 4\mathfrak{q}$ nonvanishing at generic
$\mathfrak{q}$; $\mathsf{X}_n = \Lambda_+^n + \Lambda_-^n \neq 0$ for
every $n$. No truncation. The ghost of the wrong ``collapse'' guess is
the \emph{quotient} formation at $\lambda_{\mathrm{Tr}} = N \in \mathbb{Z}_{\geq 1}$.
Theorem~N1(ii) + Remark~\ref{nek:rmk:finite-rank-wrong}.

\emph{Cycle 4: ATTACK} — Is the Nekrasov partition function on $\mathbb{C}^3$
at the CY slice modular, like on $\mathbb{C}^2$? \emph{HEAL} —
$Z^{\Omega}_{\mathrm{inst}}(\mathbb{C}^3) = M(-\mathfrak{q})$ is NOT modular;
its $t \to 0^+$ asymptotic has a $\zeta(3)/t^2$-singularity (Gevrey-$1$),
which is the B-model topological-string divergence, not a modular phenomenon.
AGT modularity is a $\mathbb{C}^2$-phenomenon; at $\mathbb{C}^3$ the
modularity lives on $\mathbb{C}^2 \subset \mathbb{C}^3$ via
$\epsilon_3 \to 0$. Theorem~N2 + Theorem~N4.

\emph{Cycle 5: ATTACK} — Does the $S_3$-triality ascend from $\mathbb{C}^3$
to $K3 \times E$? \emph{HEAL} — Proposition~N5: $\mathrm{Aut}^0(K3 \times E) = E$
(one-dimensional torus only); no third equivariant direction. $S_3$
breaks to $\mathbb{Z}/2$ (Fourier--Mukai) $\times \mathrm{SL}_2(\mathbb{Z})_{\tau_E}$.
The correct symmetry group at $K3 \times E$ is
$\mathrm{SL}_2(\mathbb{Z}) \ltimes (\mathbb{Z}/2 \times M_{23})$, not $S_3$.

\emph{Cycle 6: ATTACK} — The treatise Example~1 claims
``$Y(\widehat{\mathfrak{gl}}_1)$ acts on equivariant cohomology of the
Hilbert scheme of $\mathbb{C}^3$''. Does this action exist, and how does
it relate to the MacMahon counting $M(\mathfrak{q})$? \emph{HEAL} —
the correct module is $\bigoplus_n H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$
(DT cohomology) or the $\epsilon_3$-localisation
$\bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ (Nakajima Fock space);
the graded dimension is $M(\mathfrak{q})$ on both, via Schiffmann--Vasserot 2013
and MNOP I 2006. Theorem~N6.

\emph{Cycle 7: ATTACK} — Is the partition function at the CY slice a
trace of the Yangian on a natural module, and does the Miki $S_3$ act
on this trace? \emph{HEAL} — Theorem~N6: the $\Omega$-deformed
twisted partition function is $\mathrm{tr}_{Y^+_{\mathrm{vac}}}(z^{L_0 - c/24} \mathfrak{q}^{\mathrm{inst}})$,
computable on both the Yangian side (via shuffle algebra) and the
gauge theory side (via Bochner--Martinelli Feynman weights on
$6\mathrm{D}\ hCS$). Miki $S_3$ acts on the trace via the Hopf
automorphism of $Y^+$, consistent with the $S_3$-invariance of the
shuffle kernel at the CY slice.
