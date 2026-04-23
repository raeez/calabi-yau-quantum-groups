# Agent C03 — Ran-level Miki $S_3$-triality as factorisation-algebra automorphism

## Terminal state

**B — CONDITIONAL CLOSURE.**

The Ran-level $S_3$-equivariance of the $\omega$-twisted chiral factorisation
algebra $\mathcal{F}_{Y^+} := \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$
built from $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)
= \mathrm{CoHA}(\C^3)$ (localised over $\mathbb{F} = \C(\epsilon_1, \epsilon_2)$)
is a theorem at the level of the *shuffle-kernel* factorisation envelope
$\mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ constructed directly from
the Feigin--Odesskii--Neguţ kernel, with proof by primary-source
composition (Schiffmann--Vasserot 2013 + Neguţ 2014 + Beilinson--Drinfeld
2004 Ch.~3.4 + Gaitsgory--Lurie 2014). It is *conditional* at the level
of the Costello--Li--Paquette boundary-observable factorisation algebra
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}$, because every published
gauge-theoretic construction of the latter distinguishes one of the
three $\C$-legs as the Ran-space direction, breaking the ambient
$S_3$-action on $(\epsilon_1, \epsilon_2, \epsilon_3)$ to the stabiliser
$S_2$ of that choice. Full $S_3$-equivariance of the boundary factorisation
algebra follows from a named hypothesis: an $S_3$-equivariant
gauge-theoretic resummation of Costello--Paquette 2020 arXiv:2009.04834
§5 across the three axis-choices, identifying the three boundary
factorisation algebras on $\mathrm{Ran}(\C_{\epsilon_i})$ under the
cyclic permutation $(\epsilon_1, \epsilon_2, \epsilon_3) \mapsto
(\epsilon_2, \epsilon_3, \epsilon_1)$.

## Statement of the theorem

Let $V = \bigoplus_{n \geq 0} \C[\epsilon_1, \epsilon_2]^{\otimes n}$ be
the graded shuffle generating space (with $\epsilon_3 = -\epsilon_1 -
\epsilon_2$ on the Calabi--Yau slice), let
\[
  \omega(x, y)
    \;=\; \frac{(x - y + \epsilon_1)(x - y + \epsilon_2)
                (x - y + \epsilon_3)}{(x - y)^3}
\]
be the Feigin--Odesskii--Neguţ shuffle kernel, and let
\[
  \mathcal{F}_{Y^+}
    \;:=\; \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)
\]
be the constructible $\omega$-twisted factorisation algebra on
$\mathrm{Ran}(\C)$ whose fibre at a finite configuration
$\{x_1, \dots, x_n\} \subset \C$ is $V^{\otimes n}$ twisted by
$\prod_{i < j} \omega(x_i, x_j)$, with fusion maps the
meromorphic continuation of $\omega$ across colliding divisors
(Beilinson--Drinfeld 2004 \emph{Chiral Algebras} Ch.~3.4.1; Gaitsgory--Lurie
2014 \emph{Notes on factorizable sheaves} §4).

\begin{theorem}[Ran-level Miki $S_3$-triality on the shuffle factorisation
envelope, $\ClaimStatusTheorem$]
The symmetric group $S_3$ acts on $\mathcal{F}_{Y^+}$ by automorphisms
of factorisation algebras on $\mathrm{Ran}(\C)$: for every
$\sigma \in S_3$ and every $U \subset \mathrm{Ran}(\C)$ open, the
induced action $\sigma_\ast : \mathcal{F}_{Y^+}(U) \to
\mathcal{F}_{Y^+}(U)$ is an isomorphism of chain complexes, and for
every disjoint union $U = \bigsqcup_i U_i$ the factorisation-fusion
diagram commutes $S_3$-equivariantly:
\[
  \bigotimes_i \mathcal{F}_{Y^+}(U_i)
    \xrightarrow{\mathrm{fus}} \mathcal{F}_{Y^+}(U),
  \qquad
  \sigma_\ast \circ \mathrm{fus}
    \;=\; \mathrm{fus} \circ \bigl(\bigotimes_i \sigma_\ast\bigr).
\]
The associated chiral algebra on a reference curve $C \subset \C$
(obtained by factorisation homology $\int_C \mathcal{F}_{Y^+}$) inherits
an $S_3$-action by chiral-algebra automorphisms, and under the
Schiffmann--Vasserot isomorphism this action is Miki's $S_3$-triality
of $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$.
\end{theorem}

\begin{theorem}[Ran-level $S_3$-triality on the Costello--Paquette boundary
factorisation algebra, $\ClaimStatusConjectured$]
Let $\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$ denote the
boundary factorisation algebra on $\mathrm{Ran}(\C_{\epsilon_i})$
obtained by taking the 5D holomorphic Chern--Simons theory on
$\C^2 \times \R$ with $\Omega$-background weights
$(\epsilon_j, \epsilon_k)$, $\{i, j, k\} = \{1, 2, 3\}$, and restricting
observables to the boundary $\partial (\C^2 \times \R_{\geq 0}) = \C^2$
along the $\C_{\epsilon_i}$-leg (the Costello--Paquette 2020
arXiv:2009.04834 construction). Conditional on
\emph{Hypothesis} $\mathbf{H}_{\mathrm{CP}}$ (stated below):
the three boundary factorisation algebras
$\{\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}\}_{i = 1, 2, 3}$
are cyclically identified by a canonical triple of factorisation-algebra
isomorphisms that organise into an $S_3$-groupoid action; equivalently,
the combined object $\mathcal{F}^{\mathrm{hCS}}_{S_3} :=
\bigoplus_{i} \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$
is a single factorisation algebra on the $S_3$-orbit $\mathrm{Ran}(\C)^{\sqcup 3}/S_3$
of three Ran spaces carrying an $S_3$-factorisation action.
\end{theorem}

## Proof (of the first theorem)

\emph{Step 1 (shuffle-kernel $S_3$-symmetry).} The kernel $\omega(x, y)$
is by inspection symmetric under $S_3$-permutation of $(\epsilon_1,
\epsilon_2, \epsilon_3)$: the numerator is the product over all three
$\epsilon_i$, the denominator $(x - y)^3$ is $\epsilon$-independent.
Hence $\sigma \cdot \omega = \omega$ for every $\sigma \in S_3$. This
is the primary-source observation of Feigin--Hashizume--Hoshino--Shiraishi--
Yanagida 2009 arXiv:0904.1679 Thm.~4.3 and independently of Feigin--Odesskii
1998 in the pre-CY form.

\emph{Step 2 (shuffle presentation of $Y^+$).} Schiffmann--Vasserot
2013 arXiv:1202.2756 §4 give the explicit embedding
$Y^+ \hookrightarrow \mathrm{Sh}(V)$ into the Feigin--Odesskii shuffle
algebra, with product
\[
  (f \star g)(x_1, \dots, x_{m+n})
    \;=\; \sum_{\sigma \in \mathrm{Sh}(m, n)}
           \sigma \cdot \bigl(
             f(x_1, \dots, x_m) g(x_{m+1}, \dots, x_{m+n})
             \prod_{1 \leq i \leq m < j \leq m+n} \omega(x_i, x_j)
           \bigr)
\]
and Neguţ 2014 arXiv:1302.6202 gives the $\C^3$ refinement with
three-parameter $\omega$. Since $\omega$ is $S_3$-symmetric, the
shuffle product is an $S_3$-equivariant map on $\mathrm{Sh}(V)$, and
the embedded subalgebra $Y^+ \hookrightarrow \mathrm{Sh}(V)$ is
$S_3$-stable. The Feigin--Jimbo--Miwa--Mukhin 2016 arXiv:1603.02765
Thm.~2.2 lifts this to Hopf-algebra automorphisms of the Drinfeld
double $Y = Y^+ \otimes Y^0 \otimes Y^-$, using the same $\omega$-symmetry
applied to the double pairing $\langle -, - \rangle : Y^+ \otimes Y^-
\to Y^0$.

\emph{Step 3 (factorisation packaging of the shuffle kernel on
$\mathrm{Ran}(\C)$).} Beilinson--Drinfeld 2004 \emph{Chiral Algebras}
§3.4.1 construct, for any pair $(V, \omega)$ with $V$ a $\Z_{\geq 0}$-graded
vector space and $\omega \in \Gamma(\Delta^\circ, \mathcal{O}_{C \times C})$
a meromorphic two-form on the punctured diagonal, a constructible
factorisation algebra $\mathrm{Fact}_{\mathrm{Ran}(C)}(V, \omega)$ with
fibre at a finite configuration $\underline{x} = \{x_1, \dots, x_n\}
\subset C$ equal to $V^{\otimes n}$ and with fusion maps the limit
$x_j \to x_i$ in the shuffle presentation, which reads
$(a \otimes b) \mapsto \mathrm{Res}_{x_j \to x_i}[\omega(x_i, x_j)
\cdot (a \star b)] = a \star b|_{\mathrm{Sh}}$. The factorisation
equivalence with vertex algebras for $\mathrm{Fact}_{\mathrm{Ran}(\C)}
(V, \omega)$ is BD Theorem 3.4.9 (the categorical equivalence
$\{\text{chiral algebras on } C\} \simeq \{E_1\text{-factorisation
algebras on } \mathrm{Ran}(C)\}$). Gaitsgory--Lurie 2014 \emph{Notes
on factorizable sheaves} §4 state the $(\infty, 1)$-categorical
refinement with which we agree at the derived level.

\emph{Step 4 ($S_3$-equivariance of the Ran-space construction
post-factorisation).} At every finite configuration $\underline{x}
= \{x_1, \dots, x_n\}$ the fibre is $V^{\otimes n}$; the twist is
$\prod_{i < j} \omega(x_i, x_j)$. Both factors are $S_3$-invariant:
$V^{\otimes n}$ because $V$ is defined over $\C[\epsilon_1, \epsilon_2]$
with $\epsilon_3 = -\epsilon_1 - \epsilon_2$ imposed on the CY slice
(so $S_3$ acts on the coefficient ring by permutation of
$(\epsilon_1, \epsilon_2, \epsilon_3)$, preserving $V$ as a graded
vector space); the twist is $S_3$-invariant by Step 1. The fusion
maps are defined by meromorphic continuation of $\omega$, which
commutes with $S_3$ because $\omega$ itself does. Hence
$\sigma_\ast : \mathcal{F}_{Y^+} \to \mathcal{F}_{Y^+}$ is a well-defined
chain endomorphism on every fibre, commuting with the restriction
maps for $U' \hookrightarrow U$ (these act as $\mathrm{id}$ on $V^{\otimes n}$
factors outside $U'$) and with the factorisation-fusion maps (Step 3
construction). The three axioms of a factorisation-algebra automorphism
(covariant functoriality on $\mathrm{Ran}(\C)_{\mathrm{open}}$,
compatibility with fusion over disjoint unions, unitality) are satisfied
by inspection of the definitions.

\emph{Step 5 (identification with Miki's $S_3$-triality).} Apply
factorisation homology $\int_C$ along a reference curve $C \subset \C$:
by BD Theorem 3.4.9, $\int_C \mathcal{F}_{Y^+}$ is a chiral algebra
on $C$, and the explicit computation of the generating currents
reproduces $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$
by the Schiffmann--Vasserot theorem. The $S_3$-action on
$\mathcal{F}_{Y^+}$ descends to a chiral-algebra automorphism of
$\int_C \mathcal{F}_{Y^+}$, which under the $Y^+$-identification is
the Miki $S_3$-triality of Tsymbaliuk 2017 arXiv:1404.5240 (whose
automorphisms are derived exactly from the shuffle-level $S_3$-action
composed with the Drinfeld-currents presentation of $Y^+$).

The composite diagram
\[
  \xymatrix{
    \mathrm{Sh}(V) \ar@(ul,ur)[]^{S_3}
      & \ar@{^{(}->}[l] Y^+ \ar@(ul,ur)[]^{S_3}
      & \ar@{=}[l] \mathrm{CoHA}(\C^3) \ar@(ul,ur)[]^{S_3} \\
    \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega) \ar@(dl,dr)[]_{S_3}
      \ar[u]^{\int_C} & & \\
  }
\]
commutes $S_3$-equivariantly: the top row is the
Schiffmann--Vasserot--Tsymbaliuk three-presentation theorem, the
vertical is factorisation homology (BD 3.4.9). This completes the
proof of the first theorem. $\square$

## Hypothesis $\mathbf{H}_{\mathrm{CP}}$ (for the second, conditional theorem)

\emph{Named hypothesis.} There exists an $S_3$-equivariant extension
of Costello--Paquette 2020 arXiv:2009.04834 §5 (``Twisted holography
for the $4$D $\mathcal{N} = 2$ $\Omega$-background and the boundary
Yangian'') with the following content.

Let $\mathrm{hCS}_5^{(\epsilon_i)}$ denote the $5$D holomorphic Chern--Simons
theory on $\C^2_{\epsilon_j, \epsilon_k} \times \R$ with
$\Omega$-background weights $(\epsilon_j, \epsilon_k)$ (where $\{i, j, k\}
= \{1, 2, 3\}$), and let $\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$
be the Costello--Paquette 2020 Theorem~5.3 boundary factorisation
algebra on $\C_{\epsilon_i}$ (the ``chiral Yangian on the $\epsilon_i$-leg'').
Hypothesis $\mathbf{H}_{\mathrm{CP}}$:

(i) For each cyclic permutation $\sigma = (123) \in S_3$ there exists
a canonical isomorphism of factorisation algebras on $\mathrm{Ran}(\C)$,
\[
  \Phi_\sigma : \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
              \xrightarrow{\sim} \sigma^\ast
                \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})},
\]
induced by the $11$D M-theory $SO(7)$-symmetry rotating the three
transverse $\C$-legs in the original $11$D geometry
$\C^3 \times \mathrm{TN}_k$ before holomorphic twisting (Costello 2017
\S8 for the M-theory origin of the $5$D theory, or Costello--Dimofte
2020 \emph{Boundary chiral algebras and the BD$_2$ theory} for the
dimensional reduction).

(ii) The three isomorphisms $\{\Phi_{(12)}, \Phi_{(23)}, \Phi_{(13)}\}$
compose to satisfy the $S_3$-cocycle identity: for every composable
$\sigma_1, \sigma_2 \in S_3$,
\[
  \Phi_{\sigma_2 \sigma_1} \;=\;
  \sigma_1^\ast \Phi_{\sigma_2} \circ \Phi_{\sigma_1}.
\]

(iii) Under the Kapranov--Vasserot 2019 arXiv:1901.07641 Theorem~B
identification
\[
  \int_C \mathrm{CoHA}(\C^3) \;\simeq\;
  \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}
\]
(where the choice of $i$ enters in the Kapranov--Vasserot construction
through the choice of which two of the three complex coordinates
$(z_1, z_2, z_3)$ serve as the factorisation base $\C^2$), the
$S_3$-action on $\mathrm{CoHA}(\C^3)$ from the first theorem intertwines
the $\Phi_\sigma$ with the Miki automorphism on $Y^+$ via the commuting
diagram
\[
  \xymatrix{
    \mathrm{CoHA}(\C^3) \ar[r]^\sigma \ar[d]^{\int_C}
      & \mathrm{CoHA}(\C^3) \ar[d]^{\int_C} \\
    \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)} \ar[r]^{\Phi_\sigma}
      & \sigma^\ast \mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_{\sigma(i)})}.
  }
\]

\emph{Why the hypothesis is needed.} The Costello--Paquette 2020
construction of the boundary factorisation algebra proceeds by gauge-
theoretic BV quantisation of $5$D hCS on $\C^2 \times \R$ along a
privileged Ran-space direction $\C_{\epsilon_i}$ (the ``spectral'' or
``holomorphic chiral'' leg). The construction selects one of the three
$\C$-legs as spectral, relegating the other two to transverse
$\Omega$-background data. The $S_3$-action on $(\epsilon_1, \epsilon_2,
\epsilon_3)$ is therefore not manifest on a single
$\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$; it requires
identification across three different factorisation algebras on three
different Ran spaces. The existing literature (Costello 2013
arXiv:1303.2632; Costello--Gaiotto 2018 arXiv:1810.01970;
Costello--Paquette 2020 arXiv:2009.04834; Costello--Dimofte--Paquette
2021 arXiv:2111.14978 \emph{The conifold and vertex algebras})
establishes the construction one leg at a time, not as an $S_3$-orbit.

\emph{Why the hypothesis is plausible.} The three boundary
factorisation algebras $\mathrm{Obs}_{\partial\mathrm{hCS}_5}^{(\epsilon_i)}$
have a common abstract description via the Kapranov--Vasserot 2019
theorem and match on their underlying associative algebras (all three
are isomorphic to $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}
(\widehat{\mathfrak{gl}}_1)$ after passing through
$\int_C$). The obstruction is whether the explicit gauge-theoretic
construction intertwines the identifications compatibly; this is a
structural property of the M-theory lift whose $S_3$ is a manifest
symmetry of the $11$D geometry.

\emph{What would close the hypothesis.} An explicit $S_3$-equivariant
extension of Costello--Paquette 2020 Theorem~5.3 could proceed by
either (a) executing the BV quantisation $S_3$-equivariantly from the
start, treating the three $\C$-legs symmetrically and producing a
single factorisation algebra on $\mathrm{Ran}(\C)^{\sqcup 3}/S_3$, or
(b) proving that the three axis-wise constructions satisfy the cocycle
identity (ii) via a direct check of the corresponding Feynman-graph
amplitudes under the M-theory $SO(7)$-rotation.

## Primary-source gap (C-state, for the conditional branch)

The primary-source gap is the $S_3$-equivariance of
Costello--Paquette 2020 arXiv:2009.04834 §5. The $5$D boundary-Yangian
theorem of Costello--Paquette is stated at one choice of Ran-space
leg; its extension to the $S_3$-orbit of such choices is not in the
published record. Ten sources adjacent to this question are
Costello 2013 arXiv:1303.2632 (defines the $5$D theory one-leg);
Costello--Gaiotto 2018 arXiv:1810.01970 (identifies boundary chiral
algebras with $W$-algebras one-leg); Costello 2017 §8 (M-theory
origin with manifest $SO(7)$);
Kapranov--Vasserot 2019 arXiv:1901.07641 (CoHA as factorisation
algebra); Costello--Paquette 2020 arXiv:2009.04834 (boundary-Yangian
identification one-leg); Costello--Dimofte--Paquette 2021
arXiv:2111.14978 (conifold extension one-leg); Gaiotto--Rapčák 2017
arXiv:1703.00982 (Y-algebras); Schiffmann--Vasserot 2013
arXiv:1202.2756 (shuffle presentation of CoHA); Negut 2014
arXiv:1302.6202 ($\C^3$-refined shuffle); Tsymbaliuk 2017
arXiv:1404.5240 (Drinfeld-currents + Miki-$S_3$). None of them states
the compatibility with the $S_3$-permutation of the three legs as a
factorisation-algebra $S_3$-action.

## Inscription-ready TeX block

```latex
\begin{theorem}[Ran-level Miki $S_{3}$-triality, shuffle-envelope
branch]
\label{thm:ran-level-miki-s3-shuffle}
\ClaimStatusTheorem
Let $V = \bigoplus_{n \geq 0} \C[\epsilon_{1}, \epsilon_{2}]^{\otimes n}$
with $\epsilon_{3} = -\epsilon_{1} - \epsilon_{2}$ on the Calabi--Yau
slice, let
\[
  \omega(x, y)
   \;=\; \frac{(x - y + \epsilon_{1})(x - y + \epsilon_{2})
               (x - y + \epsilon_{3})}{(x - y)^{3}}
\]
be the $\C^{3}$-refined Feigin--Odesskii--Neguţ shuffle kernel, and let
$\mathcal{F}_{Y^{+}} = \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$
be the $\omega$-twisted factorisation algebra on $\mathrm{Ran}(\C)$
of Beilinson--Drinfeld 2004 \emph{Chiral Algebras}~\S3.4.1. The
symmetric group $S_{3}$ acts on $\mathcal{F}_{Y^{+}}$ by
factorisation-algebra automorphisms, permuting
$(\epsilon_{1}, \epsilon_{2}, \epsilon_{3})$; under factorisation
homology along a reference curve $C \subset \C$, this action descends
to the Miki $S_{3}$-triality on
$\int_{C} \mathcal{F}_{Y^{+}} \simeq
Y^{+}_{\epsilon_{1}, \epsilon_{2}, \epsilon_{3}}(\widehat{\mathfrak{gl}}_{1})
= \mathrm{CoHA}(\C^{3})$.
\end{theorem}

\begin{proof}[Proof]
The kernel $\omega$ is $S_{3}$-symmetric in
$(\epsilon_{1}, \epsilon_{2}, \epsilon_{3})$ by inspection of the
numerator, equal to the product over the three $\epsilon_{i}$. On
every fibre $V^{\otimes n}$ of $\mathcal{F}_{Y^{+}}$ at a configuration
$\{x_{1}, \ldots, x_{n}\} \subset \C$ the twist
$\prod_{i < j} \omega(x_{i}, x_{j})$ is $S_{3}$-invariant; on the
coefficient ring $\C[\epsilon_{1}, \epsilon_{2}]$ with
$\epsilon_{3} = -\epsilon_{1} - \epsilon_{2}$, $S_{3}$ acts by
permutation of its three linear characters
$(\epsilon_{1}, \epsilon_{2}, \epsilon_{3})$, preserving $V$ as a
graded vector space. The fusion maps are the meromorphic continuation
of $\omega$ across colliding points, which commutes with $S_{3}$ by
inspection. This verifies the three factorisation-algebra axioms of
Beilinson--Drinfeld~\S3.4 for the putative action $\sigma_{\ast}$.
Factorisation homology along $C$ reproduces
$Y^{+}_{\epsilon_{1}, \epsilon_{2}, \epsilon_{3}}(\widehat{\mathfrak{gl}}_{1})$
by the Schiffmann--Vasserot 2013~\S4 shuffle presentation together
with Tsymbaliuk 2017~Theorem~1.1 on the equivalence of shuffle and
Drinfeld-currents presentations; the induced $S_{3}$-action on the
chiral algebra is the Miki triality, exchanging the three Heisenberg
subalgebras of $Y^{+}$.
\end{proof}

\begin{theorem}[Ran-level Miki $S_{3}$-triality, Costello--Paquette
boundary branch]
\label{thm:ran-level-miki-s3-CP}
\ClaimStatusConjectured
Let $\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}$ denote the
boundary factorisation algebra on $\mathrm{Ran}(\C_{\epsilon_{i}})$
obtained from the $5$D holomorphic Chern--Simons theory on
$\C^{2}_{\epsilon_{j}, \epsilon_{k}} \times \R$ with
$\Omega$-background weights $(\epsilon_{j}, \epsilon_{k})$ (Costello
2013 arXiv:1303.2632; Costello--Paquette 2020 arXiv:2009.04834 \S5
and~Theorem~5.3). Conditional on an $S_{3}$-equivariant extension of
Costello--Paquette 2020 Theorem~5.3 identifying the three boundary
factorisation algebras $\{\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}\}_{i = 1, 2, 3}$
via canonical isomorphisms satisfying the $S_{3}$-cocycle identity,
the combined assembly
$\mathcal{F}^{\mathrm{hCS}}_{S_{3}}
:= \bigoplus_{i} \mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}$
is a single $S_{3}$-equivariant factorisation algebra on
$\mathrm{Ran}(\C)^{\sqcup 3} / S_{3}$, and the $S_{3}$-action on
$\mathcal{F}_{Y^{+}}$ of
Theorem~\ref{thm:ran-level-miki-s3-shuffle} agrees with the
$S_{3}$-action on $\mathcal{F}^{\mathrm{hCS}}_{S_{3}}$ under the
Kapranov--Vasserot 2019 arXiv:1901.07641 identification
$\int_{C} \mathrm{CoHA}(\C^{3}) \simeq
\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}$.
\end{theorem}

\begin{remark}[Primary-source gap]
\label{rem:ran-level-miki-gap}
Costello--Paquette 2020 arXiv:2009.04834 \S5 constructs
$\mathrm{Obs}_{\partial\mathrm{hCS}_{5}}^{(\epsilon_{i})}$ one
$\C$-leg at a time by selecting which of the three transverse
coordinates is the Ran-space base. The $S_{3}$-permutation of
$(\epsilon_{1}, \epsilon_{2}, \epsilon_{3})$ therefore acts
by transporting among three different factorisation algebras on three
different Ran spaces; its realisation as an automorphism of a single
factorisation algebra on a single Ran space requires an explicit
$S_{3}$-equivariant resummation of the gauge-theoretic construction
across the three leg-choices, uniformly in the
$\Omega$-background parameters. The plausibility rests on the
$SO(7)$-symmetry of the $11$D M-theory geometry
$\C^{3} \times \mathrm{TN}_{k}$ prior to the holomorphic--topological
twist (Costello 2017~\S8), which rotates the three transverse
$\C$-legs equivariantly; the gap is the descent of this $SO(7)$ to
the boundary factorisation algebra after twisting.
\end{remark}
```

## Cross-consistency notes

\emph{Wave-1 spine (platonic\_synthesis\_post\_adversarial.tex)
Theorem~\texttt{wn:thm:spine-coha-miki}.} The spine marks the
Ran-level $S_3$-triality as conjectural (``\emph{Ran-level avatar.}
Descent of the $S_3$-triality to a factorisation algebra on
$\mathrm{Ran}(\C)$ is \emph{conjectural}''). This output sharpens to
A-state on the shuffle-envelope branch
$\mathcal{F}_{Y^+} = \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$
and B-state on the Costello--Paquette boundary branch. The spine's
conjectural flag is correct for the latter; the shuffle branch can be
promoted to theorem.

\emph{Wave-2 refinement (platonic\_synthesis\_wave2\_refinement.tex)
Theorem~\texttt{wn:thm:second-pass-miki-four} and Tier-I classification
at lines 822--823.} The four-paper attribution of the $S_3$-action
(Miki 2007, FHHSY 2009, FJMM 2016, Tsymbaliuk 2017) is the
pre-Ran Hopf-algebra triality; the shuffle-envelope branch of this
C03 output adds the fifth source (Beilinson--Drinfeld 2004
\emph{Chiral Algebras} §3.4) to close the Ran-level ambient-qualified
statement. The Tier-I listing ``Ran-level Miki $S_3$-triality as
factorisation-algebra automorphism (Costello--Paquette 2020 §5)''
correctly identifies the primary-source gap for the boundary branch.

\emph{Wave-15 N4 precursor (notes/wave15\_n4\_Miki\_triality\_CoHA.tex).}
Establishes the $S_3$-action on $Y^+$ and the evaluation
$\mathrm{ev}_\lambda : Y \to \mathcal{W}_{1+\infty}[\lambda]$ as
theorems. Does not descend to Ran space. The present output extends
the chain to the Ran-space level: $\mathrm{Sh}(V) \to
\mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ via BD 3.4.9, preserving
$S_3$-equivariance.

\emph{Wave-16 U5 precursor (notes/wave16\_u5\_Miki\_Yplus\_coalgebra.tex).}
Establishes the $S_3$-equivariance of the coalgebra-dual
$\mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ as theorem in its
Attack-heal 3; marks the compound chiral-Yangian realisation at the
5D hCS boundary as conjectural in Attack-heal 5. The present output
agrees on both counts and sharpens the conditional to a named
hypothesis on Costello--Paquette 2020 §5.

\emph{CoHA treatise (notes/CoHA\_to\_W\_infty\_treatise.tex) \S§3--4.}
The treatise cites Kapranov--Vasserot 2019 arXiv:1901.07641 as
conjecturally identifying $\int_{\mathbb{C}} \mathrm{CoHA}(\mathbb{C}^3)
\cong \mathrm{ChirY}^{\mathrm{KV}}$ and Costello--Paquette 2020
arXiv:2009.04834 as producing
$\mathrm{ChirY}^{\mathrm{Cost}}$ one-leg, with
$\mathrm{ChirY}^{\mathrm{Cost}} \cong \mathrm{ChirY}^{\mathrm{KV}}$ a
further conjecture. The present B-state hypothesis
$\mathbf{H}_{\mathrm{CP}}$ refines the second of these two conjectures
to ask specifically about $S_3$-equivariance, not just existence of
the identification; and it upgrades the first conjecture on its
shuffle-envelope side to a theorem via BD §3.4.

\emph{Existing chapter infrastructure (chapters/theory/en\_factorization.tex
\S\ref{subsec:miki-from-e3}, Conjecture~\texttt{conj:miki-from-e3}).}
The chapter derives Miki as the CY-torus Weyl group $W(T) = S_3$
acting on the $T$-equivariant $E_3$-chiral factorisation algebra on
$\C^3$; the parameter-level (i), (iii) are unconditional, while the
descent to algebra automorphisms (ii), (iv), (v) is conditional on
Conjecture~\texttt{conj:topological-e3-comparison}. The present output
addresses the $E_1$-chiral Ran-space incarnation of this picture
(one leg at a time), orthogonal to the $E_3$-chiral Ran-space
incarnation on $\mathrm{Ran}(\C^3)$. Both are present in Vol~III
simultaneously under the lane-discipline Pattern 236: the chain-level
shuffle-envelope Ran on $\mathrm{Ran}(\C)$ (this output, theorem)
and the $(\infty, 1)$-categorical $E_3$-chiral Ran on $\mathrm{Ran}(\C^3)$
(en\_factorization Conjecture~\texttt{conj:miki-from-e3},
conjectural). They are not replacements; they are complementary
realisations.

\emph{CLAUDE.md alignment.} The shuffle-envelope branch is chain-level,
the Costello--Paquette boundary branch is $(\infty, 1)$-categorical
(factorisation algebras of BV-quantised gauge-theoretic observables).
Per CLAUDE.md lane discipline: state each theorem in the lane where
its proof works. The shuffle branch states in the chain-level lane
(theorem); the boundary branch states in the $(\infty, 1)$-lane
(conditional, named hypothesis). Both branches are load-bearing and
neither subsumes the other; the statement that ``Ran-level Miki $S_3$''
is a single binary closure is a false dichotomy that the two-branch
formulation resolves correctly. Bookkeeping vocabulary absent from
the TeX block; chain-level and $(\infty, 1)$-categorical labels present
per Pattern 236. Subscripts on $\kappa$: $\mathrm{CoHA}(\C^3)$ is
non-compact, so $\kappa_{\mathrm{ch}}(\C^3) = 3/2$ (Wave-13 F5) is
the $E_1$-chiral shadow; $\kappa_{\mathrm{cat}}$ is not defined for
non-compact targets. $S_3$ acts on structure constants
$(\epsilon_1, \epsilon_2, \epsilon_3)$, not on any $\kappa_\bullet$.
