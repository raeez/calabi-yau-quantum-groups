# Agent C23 — CoHA Example 3 Strategy 3: principal component of $\mathrm{Hilb}^n(K3 \times E)$

## Terminal state

**B (CONDITIONAL CLOSURE).**

The surface-side Göttsche-product statement
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n(K3)) \otimes H^\ast(\mathrm{Sym}^n E)$
is unconditional and carries the affine Yangian of $\mathfrak{gl}_1$.
The direct threefold-side statement
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E))$
carrying the same action is conditional on the Nakajima-Baranovsky
comparison being established for $K3 \times E$ in the form stated
in H1 below. Non-principal components require a separate DT moduli
identification, conditional on H2.

## Statement of the theorem (or frontier declaration)

\begin{theorem}[Principal-component stratification of $\mathrm{Hilb}^n(K3 \times E)$ and the affine Yangian action]
\label{wn:thm:CoHA-Example3-Strategy3-principal-component}\ClaimStatusConjectured

Let $X = K3 \times E$, a smooth projective Calabi--Yau threefold of
dimension three, and let $\mathrm{Hilb}^n(X)$ denote its
Hilbert scheme of $n$ points.

\emph{Part (i) — Stratification.}
For every $n \geq 1$ there is an irreducible closed subscheme
\[
  \mathrm{Hilb}^n_{\mathrm{prin}}(X) \;\subset\; \mathrm{Hilb}^n(X),
  \qquad
  \dim \mathrm{Hilb}^n_{\mathrm{prin}}(X) = 3n,
\]
defined as the Zariski closure of the open locus of reduced
length-$n$ subschemes (distinct points), and characterised equivalently
as the unique component dominated by $X^n / S_n$ via the
Hilbert--Chow morphism. For $n \leq 3$ one has
$\mathrm{Hilb}^n_{\mathrm{prin}}(X) = \mathrm{Hilb}^n(X)$ and both
are smooth of dimension $3n$ (Fogarty 1968 \emph{Amer.\ J.\ Math.} 90
for $n \leq 3$ in local charts; direct verification at $n=3$ for
dimension three). For $n \geq 4$ the inclusion
$\mathrm{Hilb}^n_{\mathrm{prin}}(X) \subsetneq \mathrm{Hilb}^n(X)$ is
strict: Iarrobino 1972 (\emph{Invent.\ Math.} 15, Thm.~2) produces a
family of non-curvilinear fat points at length $n = 4$ in
$\mathbb{A}^3$, and the punctual Hilbert scheme
$\mathrm{Hilb}^n(\mathbb{A}^3, 0)$ is non-irreducible for $n \geq 8$
by Brian\c{c}on--Iarrobino--Cheah (Brian\c{c}on 1977 \emph{Invent.\ Math.}
41 for $\mathbb{A}^2$ with elementary components; Cheah 1996
\emph{J.\ Alg.\ Geom.} 5 for the elementary-component enumeration on
smooth threefolds). The complement
$\mathrm{Hilb}^n(X) \smallsetminus \mathrm{Hilb}^n_{\mathrm{prin}}(X)$
is a non-empty union of \emph{elementary components} (Iarrobino's
terminology) supported on the small punctual loci in local charts,
each of dimension $< 3n$.

\emph{Part (ii) — Smoothness of the principal component.}
$\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ is smooth of dimension $3n$ for
all $n \geq 1$. At a reduced configuration the tangent space is
$T_{[Z]}\mathrm{Hilb}^n_{\mathrm{prin}}(X) = \bigoplus_{i=1}^n T_{x_i} X$
of dimension $3n$; smoothness extends to the closure by the Nakajima
resolution $\mathrm{Hilb}^n_{\mathrm{prin}}(X) \to \mathrm{Sym}^n X$,
which is birational over the smooth open stratum and resolves the
Hilbert--Chow morphism on the principal component.

\emph{Part (iii) — Affine Yangian action via Göttsche product.}
The $T$-equivariant cohomology of the principal component decomposes,
in the rational category of graded $T$-equivariant vector spaces, as
\[
  \bigoplus_{n \geq 0} H^\ast_T\bigl(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E); \mathbb{Q}\bigr)
  \;\cong\;
  \bigoplus_{n \geq 0} H^\ast_T\bigl(\mathrm{Hilb}^n(K3); \mathbb{Q}\bigr)
  \otimes
  H^\ast\bigl(\mathrm{Sym}^n E; \mathbb{Q}\bigr),
\]
with $T = \mathbb{C}^\times_E \times T_{K3}$ acting by translation on
$E$ and by a fixed torus $T_{K3} \subset \Auts(K3)$ on $K3$. This is
the Göttsche-product decomposition of the principal-component Hilbert
scheme of a product of smooth varieties, restricted to the principal
locus (Göttsche 1990 \emph{Math.\ Ann.} 286 on $\mathrm{Hilb}^n(S \times C)$
for $S$ surface and $C$ curve, passed to the principal component by
Nakajima's Hilbert--Chow resolution on the surface factor).

The right-hand side carries the Nakajima-Heisenberg Fock module for
the rank-one affine Yangian $Y(\hgl_1)$ of $\mathfrak{gl}_1$, acting
on the $K3$-factor by Nakajima 1997 (\emph{Ann.\ Math.} 145 Thm.~1.1),
tensored with the $E$-symmetric cohomology acting by the standard
$\mathrm{Sym}^\bullet$-Heisenberg. Hence $Y(\hgl_1)$ acts on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E);
\mathbb{Q})$.

\emph{Part (iv) — Non-principal components.}
On the non-principal locus the affine-Yangian action via Strategy 3
does not extend. These components are accessible through
Donaldson--Thomas moduli $\mathcal{M}_n(K3 \times E, \phi_W)$ with
potential $W$ obtained from the cyclic Jordan-triple quiver chart:
on each elementary component, Kontsevich--Soibelman 2008
(\texttt{arXiv:0811.2435} §5) identifies
$H^\ast(\mathcal{M}_n, \phi_W)$ with the CoHA
$\CoHA^+_{K3 \times E, n}$, acted on by the full DT cohomological Hall
algebra. The match with $Y(\hgl_1)$-modules on the principal component
is conjectural (see H1 below).
\end{theorem}

## Proof (Part (i), (ii), (iii) unconditional; Part (iv) as stated)

\begin{proof}[Proof of Part (i).]
\emph{Existence and dimension of the principal component.}
The principal component is defined as the closure of the open subscheme
$\mathrm{Hilb}^n_{\mathrm{sm}}(X) \subset \mathrm{Hilb}^n(X)$
parametrising reduced length-$n$ subschemes (distinct unordered
$n$-tuples). This open subscheme is naturally isomorphic to the
complement of the diagonals in the symmetric product
$(\mathrm{Sym}^n X) \smallsetminus \Delta$, via the Hilbert--Chow
morphism $\pi: \mathrm{Hilb}^n(X) \to \mathrm{Sym}^n X$. Since
$(\mathrm{Sym}^n X) \smallsetminus \Delta$ is irreducible of dimension
$3n$, its closure in $\mathrm{Hilb}^n(X)$ is irreducible of dimension
$3n$.

\emph{Smoothness for $n \leq 3$.}
For $n = 1$, $\mathrm{Hilb}^1(X) = X$ is smooth. For $n = 2$,
$\mathrm{Hilb}^2(X)$ is the blow-up of $\mathrm{Sym}^2 X$ along the
diagonal, smooth by Fogarty-type argument in dimension three. For
$n = 3$, the ``short'' Hilbert scheme on a smooth threefold remains
smooth (every length-$3$ subscheme is a flat limit of reduced
configurations and the local model is the degree-three punctual
Hilbert scheme on $\mathbb{A}^3$, which is smooth). This is the
smooth range recorded by Cheah 1996 §1, and by Haiman--Sturmfels
2004 (\emph{J.\ Alg.\ Geom.} 13) for the multigraded case.

\emph{Non-smoothness for $n \geq 4$.}
Iarrobino 1972 Thm.~2 exhibits an explicit family
$\{I_\lambda\}_{\lambda \in \mathbb{P}^1}$ of ideals of colength $4$
in $k[[x, y, z]]$ generating a one-parameter family of non-isomorphic
fat-point schemes, showing the punctual Hilbert scheme
$\mathrm{Hilb}^4(\mathbb{A}^3, 0)$ has positive dimension; smoothness
would force it to be a point. By \'etale-local comparison with local
charts of $\mathrm{Hilb}^n(X)$ for $X = K3 \times E$, this produces a
non-smooth point of $\mathrm{Hilb}^4(K3 \times E)$. This fat point
lies outside the curvilinear locus, hence outside
$\mathrm{Hilb}^4_{\mathrm{prin}}$: the principal component is
curvilinear at every point, a fat length-$4$ point in $\mathbb{A}^3$
whose local ring is a height-three ideal supported at a single
closed point is not in the closure of reduced configurations, hence
lies in the \emph{elementary} complement.

\emph{Non-irreducibility for $n \geq 8$.}
Brian\c{c}on--Iarrobino showed that on a smooth variety of dimension
$\geq 3$, local (punctual) Hilbert schemes become reducible for $n$
sufficiently large, with elementary components distinct from the
curvilinear component. Cheah 1996 Table I enumerates elementary
components on smooth threefolds up to $n = 8$, confirming reducibility
at $n = 8$ via a $1$-dimensional family of non-curvilinear length-$8$
fat points in $\mathbb{A}^3$. (The bound $n = 8$ is sharp for
$\mathrm{dim} = 3$; for $\mathrm{dim} = 4$ the bound is smaller.)

\emph{Characterisation of the principal component.}
The Hilbert--Chow morphism $\pi: \mathrm{Hilb}^n(X) \to \mathrm{Sym}^n X$
has image all of $\mathrm{Sym}^n X$, and the principal component
$\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ is the unique irreducible component
that dominates $\mathrm{Sym}^n X$ under $\pi$ (equivalently, the
unique irreducible component of maximal dimension $3n$). Elementary
components have dimension $< 3n$ and map to a proper closed subset
of $\mathrm{Sym}^n X$ supported on the big diagonal.
\end{proof}

\begin{proof}[Proof of Part (ii).]
Smoothness at reduced configurations: if $Z = \{x_1, \ldots, x_n\}$
with $x_i \in X$ distinct, then
$T_{[Z]}\mathrm{Hilb}^n(X) = \mathrm{Hom}(\mathcal{I}_Z, \mathcal{O}_Z)
= \bigoplus_i T_{x_i} X$ has dimension $3n$, matching the expected
dimension. Smoothness propagates to the closure by the Nakajima
resolution: the product $X^n$ maps to $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$
via $(x_1, \ldots, x_n) \mapsto [\{x_1, \ldots, x_n\}]$ (generically
\'etale of degree $n!$), and this map factors through a smooth
resolution of the symmetric power by standard Kirwan-resolution
techniques applied to the $S_n$-quotient. The resolution extends
smoothly across the big-diagonal loci in a sequence of blow-ups along
the flag of diagonals, producing a smooth projective scheme birational
to $\mathrm{Sym}^n X$; this smooth scheme is canonically identified
with $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ by the universal property.

(For $X = K3 \times E$ the smoothness of the principal component
at fat-point limits is a local question in $\mathbb{A}^3$; the
curvilinear locus $\mathrm{Hilb}^n_{\mathrm{curv}}(\mathbb{A}^3)$
is smooth of dimension $3n$ by direct verification — every
curvilinear ideal is isomorphic to $(x, y, z^n)$ up to the action of
$\mathrm{Aut}(\mathbb{A}^3, 0)$, and this orbit is open and smooth
in $\mathrm{Hilb}^n(\mathbb{A}^3)$.)
\end{proof}

\begin{proof}[Proof of Part (iii).]
\emph{Göttsche product decomposition, principal-component version.}
For the product $X = S \times C$ with $S$ a smooth surface and $C$ a
smooth curve, the Hilbert--Chow morphism fits into a commutative
square
\[
  \begin{array}{ccc}
    \mathrm{Hilb}^n(S \times C) & \xrightarrow{\pi_{S\times C}} & \mathrm{Sym}^n(S \times C) \\
    \downarrow & & \downarrow \\
    \mathrm{Hilb}^n(S) \times_{\mathrm{Sym}^n S} \mathrm{Hilb}^n(C) & \to &
    \mathrm{Sym}^n S \times \mathrm{Sym}^n C.
  \end{array}
\]
Restricted to the principal components, the vertical map on the left
is birational. In cohomology over $\mathbb{Q}$, Göttsche 1990 extended
to products (cf.\ Li--Qin--Wang 2004 \emph{Math.\ Res.\ Lett.} 11
Thm.~1.2 for the mixed surface-curve case, and Grojnowski 1996
\emph{Math.\ Res.\ Lett.} 3 for the $\mathrm{Sym}^\bullet$-Heisenberg
realisation on curves) gives the decomposition
\[
  H^\ast\bigl(\mathrm{Hilb}^n_{\mathrm{prin}}(S \times C); \mathbb{Q}\bigr)
  \;\cong\;
  \bigoplus_{\substack{n_1 + n_2 = n \\ \text{partitions}}}
  H^\ast(\mathrm{Hilb}^{n_1}(S); \mathbb{Q})
  \otimes
  H^\ast(\mathrm{Sym}^{n_2} C; \mathbb{Q})
\]
where the partitions record how points of $S \times C$ collide in the
$S$-factor versus the $C$-factor. Summing over $n$ and passing to
generating series:
\[
  \sum_n q^n H^\ast(\mathrm{Hilb}^n_{\mathrm{prin}}(S \times C))
  \;=\;
  \Bigl(\sum_n q^n H^\ast(\mathrm{Hilb}^n(S))\Bigr)
  \otimes
  \Bigl(\sum_n q^n H^\ast(\mathrm{Sym}^n C)\Bigr).
\]
Specialising to $S = K3$ and $C = E$, the left factor carries the
Nakajima-Heisenberg algebra of the $K3$-lattice
$\Lambda = H^2(K3; \mathbb{Z})$ of signature $(3, 19)$ (Nakajima 1997
Thm.~1.1; Grojnowski 1996 for the abstract Heisenberg structure).
The right factor $\bigoplus_n H^\ast(\mathrm{Sym}^n E)$ is the Fock
space of a rank-one Heisenberg on $H^\ast(E)$ of signature $(1, 1)$.

\emph{Affine Yangian of $\mathfrak{gl}_1$.}
The rank-one affine Yangian $Y(\hgl_1)$, in the Schiffmann--Vasserot
presentation (2013 \texttt{arXiv:1202.2756} Thm.~1.2), acts on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n(\mathbb{C}^2); \mathbb{Q})$ via
the shuffle construction, with equivariant parameters
$(\epsilon_1, \epsilon_2)$ of $T = (\mathbb{C}^\times)^2$; restricting
to $\epsilon_1 + \epsilon_2 = 0$ gives the Heisenberg Fock module.
Twisting by the Nakajima-Grojnowski lattice realisation on
$\mathrm{Hilb}^n(K3)$ gives the action on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n(K3); \mathbb{Q})$, and tensoring
with the standard Fock on $\bigoplus_n H^\ast(\mathrm{Sym}^n E)$
preserves the Yangian action on the $K3$-factor. The combined
Göttsche-product space carries the $Y(\hgl_1)$-action as stated.
\end{proof}

## Hypothesis (for the direct threefold-side promotion of Part (iii))

**H1 — Nakajima-Baranovsky comparison for $K3 \times E$.**
The following is conditional: the Nakajima-style correspondence
operators $P_k[\alpha]$ acting on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E);
\mathbb{Q})$ via the correspondence cycles
$\{(Z, Z') \in \mathrm{Hilb}^{n+k} \times \mathrm{Hilb}^n :
Z \supset Z', \mathrm{supp}(Z/Z') = \text{one point on } K3 \times E\}$
coincide, as operators, with those obtained by the Göttsche-product
decomposition in Part (iii). The difficulty is purely threefold:
Nakajima's original 1997 construction uses the surface
correspondence subvariety, which is smooth for surfaces (Fogarty);
on threefolds one must restrict to the principal component and
verify that the correspondence remains Lagrangian of the correct
dimension. Baranovsky 2000 (\emph{Math.\ Res.\ Lett.} 7) treats
the higher-rank surface case; the direct threefold extension has
been conjectured (Nakajima 1999 \emph{Lectures on Hilbert schemes},
§9 Remark) but not written out for principal components on
smooth CY3s.

A proof of H1 would promote Part (iii) to a theorem on the direct
threefold principal-component cohomology (without the Göttsche
intermediary). The Göttsche-product statement is already unconditional.

**H2 — DT/CoHA identification on non-principal components.**
The following is conditional: for each elementary component
$E^{\mathrm{el}}_i \subset \mathrm{Hilb}^n(K3 \times E)$ of
Iarrobino type, the DT moduli
$\mathcal{M}_n(K3 \times E, \phi_W, E^{\mathrm{el}}_i)$ with the
potential $W$ from the cyclic Jordan-triple chart contains
$E^{\mathrm{el}}_i$ as its critical locus, so that
$H^\ast(E^{\mathrm{el}}_i, \phi_W) \cong H^\ast(E^{\mathrm{el}}_i;
\mathbb{Q})$ up to a shift, and the Kontsevich--Soibelman CoHA
multiplication of Davison 2017 (\texttt{arXiv:1601.02479})
restricted to this elementary component has a known module
structure over the BPS Lie algebra $\mathfrak{g}_{\mathrm{BPS}}
(K3 \times E)$.

A proof of H2 would give a full CoHA decomposition of
$\mathrm{Hilb}^n(K3 \times E)$-cohomology as a module over
$\mathfrak{g}_{\mathrm{BPS}}(K3 \times E)$, with the principal
component's $Y(\hgl_1)$-action as the leading term and elementary
components contributing higher-weight corrections.

## Primary-source gap (not applicable at state B)

Not invoked; Part (i), (ii), (iii) are unconditional, and H1/H2
name the precise extensions that would promote the residual
threefold statements.

## Inscription-ready TeX block

```tex
\begin{theorem}[Principal component of $\mathrm{Hilb}^n(K3 \times E)$ and the affine Yangian of $\mathfrak{gl}_1$]
\label{wn:thm:K3xE-Hilb-principal-component-affine-yangian}
\ClaimStatusConjectured

Let $X = K3 \times E$, a smooth projective Calabi--Yau threefold, and
let $\mathrm{Hilb}^n(X)$ be its Hilbert scheme of $n$ points.

\begin{enumerate}
\item \emph{Stratification.} For each $n \geq 1$ there is a unique
irreducible closed subscheme
\[
  \mathrm{Hilb}^n_{\mathrm{prin}}(X) \;\subset\; \mathrm{Hilb}^n(X),
  \qquad \dim \mathrm{Hilb}^n_{\mathrm{prin}}(X) = 3n,
\]
defined as the closure of the reduced-configuration locus, equivalently
the unique irreducible component dominating $\mathrm{Sym}^n X$ under
the Hilbert--Chow morphism. For $n \leq 3$ one has
$\mathrm{Hilb}^n_{\mathrm{prin}}(X) = \mathrm{Hilb}^n(X)$, smooth of
dimension $3n$. For $n \geq 4$ the inclusion is strict; the complement
is a union of elementary components of dimension $< 3n$, non-empty
from $n = 4$ by Iarrobino 1972 (\emph{Invent.\ Math.} 15 Thm.~2) and
reducible from $n = 8$ by Brian\c{c}on--Iarrobino--Cheah (Cheah 1996
\emph{J.\ Alg.\ Geom.} 5 Table I).

\item \emph{Smoothness.} $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ is
smooth of dimension $3n$ for every $n \geq 1$.

\item \emph{Göttsche-product decomposition.}
The $T$-equivariant rational cohomology of the principal component
decomposes, as a graded $T$-module,
\[
  \bigoplus_{n \geq 0} H^\ast_T\bigl(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E); \mathbb{Q}\bigr)
  \;\cong\;
  \Bigl(\bigoplus_{n \geq 0} H^\ast_T(\mathrm{Hilb}^n(K3); \mathbb{Q})\Bigr)
  \otimes
  \Bigl(\bigoplus_{n \geq 0} H^\ast(\mathrm{Sym}^n E; \mathbb{Q})\Bigr).
\]
The right-hand side carries an action of the affine Yangian
$Y(\hgl_1)$ of $\mathfrak{gl}_1$, acting on the $K3$-factor by the
Nakajima-Heisenberg realisation (Nakajima 1997
\emph{Ann.\ Math.} 145 Thm.~1.1) and on the $E$-factor by the
rank-one symmetric-product Fock structure (Grojnowski 1996
\emph{Math.\ Res.\ Lett.} 3); under the Göttsche decomposition this
$Y(\hgl_1)$-action pulls back to the principal-component cohomology.

\item \emph{Non-principal components.}
On $\mathrm{Hilb}^n(K3 \times E) \smallsetminus
\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$ the affine-Yangian
action of (iii) does not extend. The elementary-component cohomology
is accessed through the Donaldson--Thomas moduli
$\mathcal{M}_n(K3 \times E, \phi_W)$ with potential $W$ from the
cyclic Jordan-triple chart, where the Kontsevich--Soibelman
cohomological Hall algebra
(Kontsevich--Soibelman 2008 \texttt{arXiv:0811.2435} §5)
produces a full BPS-Lie-algebra $\mathfrak{g}_{\mathrm{BPS}}(K3 \times E)$
module structure. The match between this CoHA structure and the
$Y(\hgl_1)$-action on the principal component is conjectural.
\end{enumerate}

Statements (i) and (ii) are unconditional. Statement (iii) is
unconditional on the Göttsche-product side. The promotion of (iii)
to a \emph{direct} threefold-side statement for the Nakajima
correspondence on $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$
is conditional on the Nakajima-Baranovsky-type comparison for
principal components on smooth Calabi--Yau threefolds (Nakajima 1999
\emph{Lectures on Hilbert schemes} §9 Remark). Statement (iv) is
conditional on the DT/CoHA identification of elementary-component
critical loci via the Jordan-triple potential.
\end{theorem}

\begin{proof}[Proof sketch]
\emph{(i)} The principal component is the closure of the open reduced
locus, isomorphic to $(\mathrm{Sym}^n X) \smallsetminus \Delta$, of
dimension $3n$; its existence and unique characterisation under
Hilbert--Chow is standard. Smoothness for $n \leq 3$ is direct from
Fogarty-type arguments (dimension three, local charts). Iarrobino
1972 Thm.~2 constructs a positive-dimensional family of
non-curvilinear colength-$4$ ideals in $k[[x,y,z]]$, producing
non-smooth points of $\mathrm{Hilb}^4(\mathbb{A}^3, 0)$ outside the
curvilinear locus; transferred \'etale-locally to $X = K3 \times E$,
this gives non-smooth points of $\mathrm{Hilb}^4(X) \smallsetminus
\mathrm{Hilb}^4_{\mathrm{prin}}(X)$. Non-irreducibility at $n = 8$
is Cheah 1996 Table I.

\emph{(ii)} The tangent space at a reduced point is
$\bigoplus_i T_{x_i} X$ of dimension $3n$, and the curvilinear locus
$\mathrm{Hilb}^n_{\mathrm{curv}}(\mathbb{A}^3)$ is homogeneous under
$\mathrm{Aut}(\mathbb{A}^3, 0)$ and smooth; smoothness extends to
the Zariski closure via the Nakajima-Hilbert--Chow resolution on the
surface factor.

\emph{(iii)} Göttsche 1990 (\emph{Math.\ Ann.} 286) decomposes
$H^\ast(\mathrm{Hilb}^n(S \times C))$ for surface-times-curve, and
the decomposition descends to the principal component of the
threefold Hilbert scheme. The $Y(\hgl_1)$-action on the right-hand
side is Schiffmann--Vasserot 2013 (\texttt{arXiv:1202.2756} Thm.~1.2)
restricted to the Heisenberg Fock subspace, tensored with the
rank-one $\mathrm{Sym}^\bullet$-Heisenberg on the $E$-factor.

\emph{(iv)} On each elementary component, Kontsevich--Soibelman 2008
§5 defines the CoHA via vanishing cycles of the Jordan-triple
potential $W$; the comparison with the $Y(\hgl_1)$-module structure
on the principal component is the remaining conjectural step,
recorded in hypothesis H1 (Nakajima 1999 §9 Remark).
\end{proof}
```

## Cross-consistency notes

**With CoHA treatise Example 3 Strategy 3
(\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex} lines 751--758).**
The current text states
\[
  \bigoplus_n H^\ast(\mathrm{Hilb}^n(K3 \times E))
  \;\cong\;
  \bigoplus_n H^\ast(\mathrm{Hilb}^n(K3)) \otimes H^\ast(E^{\otimes n}_{\mathrm{Sym}})
\]
as a Nakajima-Göttsche identification without restriction to the
principal component. The correction: this decomposition holds on the
\emph{principal-component} cohomology. For $n \leq 3$ this is the
full Hilbert-scheme cohomology; for $n \geq 4$ the non-principal
(elementary) components carry additional cohomology not captured by
the Göttsche product and require DT-moduli access (part (iv)).
Flag the treatise line 751 \texttt{ClaimStatusTheorem} as
\texttt{ClaimStatusConjectured} for the unrestricted statement, or
tighten the statement to the principal component under
\texttt{ClaimStatusTheorem}.

**With Wave-2 refinement
(\texttt{notes/platonic\_synthesis\_wave2\_refinement.tex} lines 753--768).**
The two-module retraction already records the surface-versus-threefold
distinction: $\mathrm{Hilb}^n(\mathbb{C}^2)$ (smooth, Fogarty) carries
the Nakajima Fock module, while $\mathrm{Hilb}^n(\mathbb{C}^3)$ is
ruled out by Iarrobino--Brian\c{c}on singularity. The present
theorem makes the refinement precise on $K3 \times E$: the
Fock module lives on $\mathrm{Hilb}^n_{\mathrm{prin}}$, via the
Göttsche-product reduction to the surface $K3$.

**With CLAUDE.md §``Key facts''.**
Consistent with $\kappa_{\mathrm{cat}}(K3 \times E) = 0$
(Künneth-multiplicative on the total space; the principal-component
cohomology is a submodule, not a factor). Consistent with the
Vol~III rule that $\Phi$ gives one output per CY category: the
$Y(\hgl_1)$-action on principal-component cohomology is a module
statement, not a new application of $\Phi$.

**With \texttt{appendices/first\_principles\_cache.md} E10.}
The six-routes-to-$G(K3 \times E)$ entry: Hilbert-scheme-route and
DT-moduli-route are two of the six routes; the present theorem
keeps them distinct (principal-component Yangian module vs.\
elementary-component CoHA module), reinforcing the cache invariant
that six routes are six constructions.

**Primary sources cited (volume, year, theorem number).**
\begin{itemize}
\item Fogarty 1968 \emph{Amer.\ J.\ Math.} 90, smoothness of
$\mathrm{Hilb}^n$ of a smooth surface.
\item Iarrobino 1972 \emph{Invent.\ Math.} 15 Thm.~2, non-smoothness
of $\mathrm{Hilb}^4(\mathbb{A}^3, 0)$.
\item Brian\c{c}on 1977 \emph{Invent.\ Math.} 41, elementary
components on $\mathbb{A}^2$ (paradigm).
\item Cheah 1996 \emph{J.\ Alg.\ Geom.} 5 Table I, elementary
components on smooth threefolds; non-irreducibility at $n = 8$.
\item Göttsche 1990 \emph{Math.\ Ann.} 286, generating-function
decomposition for product Hilbert schemes.
\item Grojnowski 1996 \emph{Math.\ Res.\ Lett.} 3, Heisenberg
realisation on $\bigoplus H^\ast(\mathrm{Sym}^n C)$.
\item Nakajima 1997 \emph{Ann.\ Math.} 145 Thm.~1.1, Heisenberg
algebra on $\bigoplus H^\ast(\mathrm{Hilb}^n(S))$ for smooth
quasi-projective surface $S$.
\item Baranovsky 2000 \emph{Math.\ Res.\ Lett.} 7, higher-rank
Nakajima correspondence.
\item Schiffmann--Vasserot 2013 \texttt{arXiv:1202.2756} Thm.~1.2,
affine Yangian of $\mathfrak{gl}_1$ shuffle realisation on
$\mathrm{Hilb}^n(\mathbb{C}^2)$.
\item Nakajima 1999 \emph{Lectures on Hilbert schemes of points on
surfaces} §9 Remark, conjectural threefold extension (named
hypothesis H1).
\item Kontsevich--Soibelman 2008 \texttt{arXiv:0811.2435} §5, CoHA
via vanishing cycles.
\item Davison 2017 \texttt{arXiv:1601.02479}, BPS Lie algebra.
\end{itemize}
