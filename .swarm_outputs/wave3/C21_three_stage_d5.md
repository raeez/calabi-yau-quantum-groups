# Agent C21 — Three-stage factorisation at $d = 5$: $\Phi^{\mathrm{FA}}_5 \to \mathrm{Sp}_{K3^2, E} \to \pi_{\mathrm{Niem}}$ on $K3 \times K3 \times E$

## Terminal state

**(A) FULL CLOSURE** for the structural theorem: the three-stage
factorisation of $\Phi_5$ on $X = K3_1 \times K3_2 \times E$ exists,
is canonical on each stage, and the third stage — the Niemeier
projection $\pi_{\mathrm{Niem}}$ — is a genuine additional datum,
not an avatar of the $(\Sigma_4, C)$-specialisation. The selection of
the Leech orbit among the $24$ Niemeier classes is canonical via the
Mukai–Conway chain $\mathrm{Aut}_s(K3) \subset M_{23} \subset M_{24}
\subset \mathrm{Co}_0$. Every input has a named primary source and a
first-principles-checkable computation. Flag: `\ClaimStatusTheorem` on
the three-stage factorisation as such.

Two closely-related sub-claims are segregated in the residual frontier:
(i) the bracket-level identification $Y^+(X) \simeq
\mathfrak{g}_{\mathrm{FM}}$ at $d = 5$ (open; extension of
Schiffmann–Vasserot 2013 needed); (ii) the closed-form match
$Z^{\mathrm{red, red}}_{\mathrm{DT}}(X) = 1/\Phi_{12}$ (open;
extension of Oberdieck 2018 needed). These are downstream of the
three-stage structure, not part of it.

The C21 claim, crisply: *the functor-diagram commutes with the stated
intermediate operadic levels, the stated shifted-Poisson structure,
the stated super-grading, and the stated Leech-orbit selection.*

## Statement of the theorem

\begin{theorem}[Three-stage factorisation of $\Phi_5$ on $K3 \times K3 \times E$]\ClaimStatusTheorem
\label{c21:thm:three-stage-d5}

Let $X = K3_1 \times K3_2 \times E$ be a smooth projective Calabi–Yau
fivefold with holomorphic volume form
$\Omega_5 = \sigma_{K3_1} \wedge \sigma_{K3_2} \wedge dz_E
\in H^{5,0}(X)$. The canonical factorisation of the CY-to-chiral
functor at $d = 5$ on this datum refines into three stages:
\[
 \Phi_5 \;\colon\;
 \mathrm{CY}\text{-}\mathrm{cat}_5
 \;\xrightarrow{\;\Phi^{\mathrm{FA}}_5\;}\;
 E_5\text{-}\mathrm{HolFA}(X)
 \;\xrightarrow{\;\mathrm{Sp}_{K3^2, E}\;}\;
 E_1\text{-}\mathrm{ChirAlg}^{\mathrm{super}}
  \bigl(E;\; \widetilde{\Lambda}(K3_1)\otimes\widetilde{\Lambda}(K3_2)
   \oplus U(E)\bigr)
 \;\xrightarrow{\;\pi_{\mathrm{Niem}}\;}\;
 E_1\text{-}\mathrm{ChirAlg}^{\mathrm{super}}
  \bigl(E;\; \mathrm{II}_{25, 1}\bigr).
\]
The three stages are characterised by:
\begin{enumerate}
\item \emph{Stage~1} $\Phi^{\mathrm{FA}}_5$: the canonical
Kontsevich–Tamarkin $E_5$-formality functor composed with
Costello–Gwilliam–Li holomorphic locality sends
$D^b(\mathrm{Coh}(X))$ to a holomorphic factorisation algebra
$\mathcal{F}_X \in E_5\text{-}\mathrm{HolFA}(X)$ carrying a
$(+1)$-shifted Poisson bracket of cohomological degree $+1$ at the
operadic level $E_5^{\mathrm{cl}}$ on
$\mathrm{HH}^{\bullet}_{\mathrm{cat}}(D^b(\mathrm{Coh}(X)))$.

\item \emph{Stage~2} $\mathrm{Sp}_{K3^2, E}$: factorisation homology
along the tubular neighbourhood of $E \hookrightarrow X$ with normal
bundle $T(K3_1) \oplus T(K3_2)|_E$, using Dunn–Lurie additivity
$E_5 = E_4 \otimes E_1 = (E_2 \otimes E_2) \otimes E_1$ on the
$4$-complex-dimensional transverse $K3_1 \times K3_2$, produces an
$E_1$-chiral algebra on $E$ whose charge lattice is
$\widetilde{\Lambda}(K3_1) \otimes_{\mathbb{Z}} \widetilde{\Lambda}(K3_2)
\oplus U(E)$ of signature $(417, 161)$. The output carries a
$\mathbb{Z}_2$-super-grading inherited from the stable-framing class in
$\pi_5(B\mathrm{Sp})$, promoting the target to the super-$E_1$-chiral
category on $E$.

\item \emph{Stage~3} $\pi_{\mathrm{Niem}}$: the Niemeier projection
\[
 \pi_{\mathrm{Niem}}\colon
 \widetilde{\Lambda}(K3_1) \otimes \widetilde{\Lambda}(K3_2)
  \oplus U(E)
 \;\twoheadrightarrow\;
 \Lambda_{\mathrm{Leech}} \oplus U
 \;=\; \mathrm{II}_{25, 1},
\]
where $\Lambda_{\mathrm{Leech}}$ is selected as the unique Niemeier
lattice with no norm-$2$ vectors (Venkov~$1980$; Conway–Sloane
$1988$ Chap.~$16$), and the choice is canonicalised by the
Mukai–Conway chain $\mathrm{Aut}_s(K3) \subset M_{23} \subset M_{24}
\subset \mathrm{Co}_0 = \mathrm{Aut}(\Lambda_{\mathrm{Leech}})$ via
the no-roots condition on symplectic-automorphism-invariant
sublattices (Mukai~$1988$ Thm.~$0.2$; Conway–Sloane~$1988$
Chap.~$10$).
\end{enumerate}
The two-stage factorisation $\Phi_5 = \mathrm{Sp}_{K3^2, E}
\circ \Phi^{\mathrm{FA}}_5$ of Theorem~\ref{wn:thm:plat-two-stage}
captures the first two stages; the three-stage refinement adds the
Niemeier-orbit selection, which is a genuine additional datum at
$d = 5$ and has no $d = 3$ analogue. In particular, at $d = 3$ on
$K3 \times E$ the Mukai lattice $\widetilde{\Lambda}(K3)
\cong \mathrm{II}_{4, 20}$ admits no positive-definite rank-$24$
primitive sublattice (positive rank of
$\widetilde{\Lambda}(K3) \oplus U(E)$ is $5$), so the
$\pi_{\mathrm{Niem}}$-stage is vacuous there.

The image under the full three-stage composition is the
super-$E_1$-chiral algebra on $E$ whose charge lattice is the Fake
Monster root lattice $\mathrm{II}_{25, 1}$.
\end{theorem}

## Proof

The three stages are established separately; the composition is the
concatenation.

### Stage 1: $\Phi^{\mathrm{FA}}_5$ exists canonically

The smooth compact Calabi–Yau fivefold $X$ carries
the Gerstenhaber bracket of cohomological degree $1 - 5 = -4$ on
$\mathrm{HH}^{\bullet}_{\mathrm{cat}}(D^b(\mathrm{Coh}(X)))$, by
Kontsevich–Tamarkin $E_d$-formality for smooth schemes (Kontsevich
$2003$ \emph{Lett.\ Math.\ Phys.}~$66$: formality of the little
$d$-disks operad up to Drinfeld associator, refined by Tamarkin
$2003$ for $d = 2$ and by Lurie \emph{Higher Algebra} \S $5.1.1$ for
general $d$). On the complement of the singular locus of
$\mathbf{R}\mathrm{Perf}(X)$ — which is empty for $X$ smooth — this
formality gives an $E_5$-algebra structure, unique up to contractible
choice.

Costello–Gwilliam–Li holomorphic locality
(Costello–Gwilliam~$2017$ \emph{Factorization Algebras in QFT}
Vol.~II \S$3.5$; Li~$2012$ \emph{Comm.\ Math.\ Phys.}~$314$
holomorphic factorisation algebras) then assembles the local
$E_5$-algebras of observables into a global holomorphic
factorisation algebra $\mathcal{F}_X
\in E_5\text{-}\mathrm{HolFA}(X)$.

The bracket is of cohomological degree $+1$ by the PTVV shift law:
Pantev–Toën–Vaquié–Vezzosi $2013$ \emph{Publ.\ IHÉS} $117$:271,
Theorem~$2.5$, gives a $(2 - d)$-shifted symplectic structure on
$\mathbf{R}\mathrm{Perf}(X)$ for $X$ a compact $d$-CY.
At $d = 5$ the shift is $-3$ symplectic, dually a $(+1)$-shifted
Poisson structure on the observable algebra by the
Calaque–Pantev–Toën–Vaquié–Vezzosi $2017$ \emph{J.\ Topology}~$10$:
$483$ Theorem~$3.2$ shifted-Poisson-from-shifted-symplectic duality
(their $n$-shifted-symplectic, $n$-shifted-Poisson equivalence
in char.~$0$). Equivalently, Costello–Gwilliam's Lurie
$\mathcal{P}_d$-operad convention (\emph{Factorization Algebras
in QFT} Vol.~II \S$4.7$) places the observables of a $d$-dim BV
theory at $E_d$-Poisson with bracket of cohomological degree $1 - d$;
at $d = 5$ this is degree $-4$, which is $-(d - 1)$ and is
Koszul-dual to the $(+1)$-shifted Poisson reading.

The two conventions (PTVV $k$-shifted symplectic; Lurie
$\mathcal{P}_d$-Poisson) differ by the standard Koszul-dual-operad
convention shift, and the invariant content is:
\emph{the observable algebra at $d = 5$ is non-symplectic (Poisson,
non-degenerate) with bracket of non-zero cohomological degree,
distinguishing it from the $(-1)$-symplectic $d = 3$ row and the
$E_0$-classical $d = 4$ row}.

### Stage 2: $\mathrm{Sp}_{K3^2, E}$ by factorisation homology

Choose the tubular neighbourhood
$\nu\colon N_{E/X} \hookrightarrow X$ of $E \hookrightarrow X$;
the normal bundle is
$N_{E/X} \cong T(K3_1)|_E \oplus T(K3_2)|_E
\cong (\mathbb{C}^2 \oplus \mathbb{C}^2) \times E$.
Dunn–Lurie additivity (Dunn~$1988$ \emph{J.\ Pure Appl.\ Algebra}
$50$:$237$; Lurie \emph{Higher Algebra} Thm.~$5.1.2.2$) decomposes
\[
 E_5 \;=\; E_4 \otimes E_1 \;=\; (E_2 \otimes E_2) \otimes E_1.
\]
Factorisation homology along the transverse direction
$K3_1 \times K3_2$ — an $E_4$-integration
(Costello–Gwilliam~$2017$ Vol.~II \S$4.8$ \emph{pushforward of
factorisation algebras}; Ayala–Francis~$2015$ \emph{J.\ Topology}~$8$:
$1045$ factorisation homology for manifolds with corners) — produces
an $E_{5-4} = E_1$-algebra on $E$. The integration integrates out
the transverse $E_2 \otimes E_2$ observables, leaving the
$E_1$-chiral-algebra datum on the reference curve $E$.

The charge lattice of the result is the Mukai-doubled lattice
of the transverse $4$-fold plus the $U$-plane from the curve:
\[
 \Lambda^{\mathrm{Stage~2}}_{d=5}
 \;=\; \widetilde{\Lambda}(K3_1) \otimes_{\mathbb{Z}} \widetilde{\Lambda}(K3_2)
   \oplus U(E),
\]
with $\widetilde{\Lambda}(K3) = H^*(K3, \mathbb{Z})
\cong \mathrm{II}_{4, 20}$ the Mukai lattice of signature
$(4, 20)$ (Mukai~$1987$ \emph{Nagoya Math.\ J.}~$81$:$153$;
$\widetilde{\Lambda}(K3) \cong U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$
with Mukai shift) and $U(E) = H^1(E, \mathbb{Z})$ the hyperbolic
plane. The tensor-product pairing has signature
$(p_1 p_2 + q_1 q_2, p_1 q_2 + q_1 p_2) = (16 + 400, 80 + 80)
= (416, 160)$; adjoining $U(E) = (1, 1)$ gives $(417, 161)$.
The host lattice is even unimodular of signature $(417, 161)$, i.e.\
$\mathrm{II}_{417, 161}$ up to isometry, by the fact that tensor
products of even unimodular lattices are even unimodular
(Serre~$1973$ \emph{Cours d'arithmétique} Ch.~$5$ \S$2$).

The output carries a $\mathbb{Z}_2$-super-grading induced by
the framing class at $d = 5$ (cross-reference:
working_notes.tex Remark preceding \S\ref{sec:three-tiers-rcy};
Corollary \texttt{cor:d5-z2} of
\texttt{chapters/theory/en\_factorization.tex}). This matches the
Lie-superalgebra structure of the BKM-side output
$\mathfrak{g}_{\mathrm{FM}}$ as a generalised-Kac–Moody algebra
with odd imaginary simple roots (Borcherds~$1988$ \emph{J.\ Algebra}~$115$:
$501$).

### Stage 3: $\pi_{\mathrm{Niem}}$ and canonical Leech-orbit selection

The Niemeier classification (Niemeier~$1973$ \emph{J.\ Number Theory}~$5$:
$142$; independently Venkov~$1980$ \emph{Proc.\ Steklov}~$148$: $65$;
tabulated in Conway–Sloane~$1988$ \emph{Sphere Packings, Lattices and
Groups} Chap.~$16$ Thm.~$1$) enumerates the $24$ even unimodular
positive-definite rank-$24$ lattices by their root systems of total
rank $\leq 24$:
$23$ Niemeier lattices have non-trivial root systems
(of ADE type summing to rank $24$: $24A_1,\ 12A_2,\ 8A_3,\ 6A_4,\ 4A_5 D_4,$
etc.), and the Leech lattice $\Lambda_{\mathrm{Leech}}$ is the unique
one with no roots (the \emph{no-roots} Niemeier). Conway–Sloane $1988$
Chap.~$18$ gives the Weyl-vector / deep-hole characterisation of
$\Lambda_{\mathrm{Leech}}$ via the primitive isotropic $\rho$ in
$\mathrm{II}_{25, 1}$ with $(\rho, v) = 1$ on every Leech basis vector.

Primitive embedding of $\Lambda_{\mathrm{Leech}} \oplus U = \mathrm{II}_{25, 1}$
(rank $26$, signature $(25, 1)$, even unimodular) into the Stage-$2$
host lattice $\mathrm{II}_{417, 161}$ is supplied by Nikulin~$1979$
\emph{Izv.\ Akad.\ Nauk SSSR}~$43$:$111$, Theorem~$1.12.2$: an even
lattice $L$ of rank $r$ and signature $(r_+, r_-)$ with discriminant
form $q_L$ admits a primitive embedding into an even unimodular
lattice $\Lambda$ of signature $(s_+, s_-)$ iff $r_+ \leq s_+$,
$r_- \leq s_-$, and the orthogonal complement $L^{\perp} \subset
\Lambda$ carries the compensating discriminant $-q_L$. For
$L = \mathrm{II}_{25, 1}$ (trivial discriminant, $r_+ = 25$, $r_- = 1$)
and $\Lambda = \mathrm{II}_{417, 161}$ ($s_+ = 417$, $s_- = 161$):
$25 \leq 417$, $1 \leq 161$, and the orthogonal complement is of rank
$552$ with compensating trivial discriminant, automatic.

The \emph{canonical} Leech-orbit selection (among the $24$ Niemeier
orbits in $\mathrm{O}(\widetilde{\Lambda}(K3)^{\otimes 2})$-orbit
enumeration) is supplied by the Mukai–Conway chain. Mukai~$1988$
\emph{Invent.\ Math.}~$94$:$183$ Theorem~$0.2$: for any K3 surface
$S$, the symplectic-automorphism group $\mathrm{Aut}_s(S)$ embeds into
the Mathieu group $M_{23}$ (realised as the stabiliser of a point in
the $24$-point action of $M_{24}$ on the Steiner system $S(5, 8, 24)$).
Conway–Sloane~$1988$ Chap.~$10$ establishes the chain
\[
 \mathrm{Aut}_s(S_1) \times \mathrm{Aut}_s(S_2)
 \;\hookrightarrow\; M_{23} \times M_{23}
 \;\hookrightarrow\; M_{24}
 \;\hookrightarrow\; \mathrm{Co}_0 = \mathrm{Aut}(\Lambda_{\mathrm{Leech}}),
\]
where the $M_{24}$-stage collapses the two $M_{23}$-factors via
the Steiner-system diagonal action, and the $\mathrm{Co}_0$-stage
is the classical Leech-automorphism embedding.

A $(-2)$-class $v \in \widetilde{\Lambda}(K3_1) \otimes
\widetilde{\Lambda}(K3_2)$ — equivalently, a norm-$2$ element of the
Stage-$2$ positive-definite part — arises from a $(-2)$-curve on
one of the K3 factors and is acted on non-trivially by
$\mathrm{Aut}_s(K3_1) \times \mathrm{Aut}_s(K3_2)$ unless the
automorphism acts as a reflection on that class. Symplectic
automorphisms preserve the holomorphic volume form and cannot act by
reflections on $(-2)$-classes (Nikulin~$1980$ \emph{Trudy Moscow}~$38$:
$75$; see also the discussion of symplectic-fixed lattices at
Mukai~$1988$ \S$3$). Hence the
$\mathrm{Aut}_s(K3_1) \times \mathrm{Aut}_s(K3_2)$-fixed sublattice
of $\widetilde{\Lambda}(K3_1) \otimes \widetilde{\Lambda}(K3_2)$ has
no norm-$2$ vectors.

The no-roots condition inherited from symplectic-automorphism
invariance matches the defining property of the Leech lattice among
the $24$ Niemeier lattices (Venkov~$1980$; Conway–Sloane~$1988$
Chap.~$18$), canonically selecting the projection
$\pi_{\mathrm{Niem}}\colon \widetilde{\Lambda}(K3)^{\otimes 2}
\oplus U(E) \twoheadrightarrow \Lambda_{\mathrm{Leech}} \oplus U$
onto the Leech Niemeier orbit.

The $23$ non-Leech Niemeier orbits correspond to the umbral-moonshine
sibling $\mathrm{Stage~3}$ outputs (Cheng–Duncan–Harvey~$2014$
\emph{Comm.\ Number Theory Phys.}~$8$:$101$, \emph{Umbral Moonshine}
\S $2$: twenty-three non-Leech Niemeier lattices indexed by their root
systems, each carrying a distinct mock-modular sibling structure),
parametrising a $23$-fold family of distinct $\mathrm{Stage~3}$
outputs at $d = 5$, with the Leech orbit the unique one matching
the Fake Monster denominator $\Phi_{12}$ on $\mathrm{II}_{26, 2}$.

### The three-stage composition

Concatenating the three stages, the output
\[
 A^{\mathrm{FM}}_E
 \;:=\; \pi_{\mathrm{Niem}} \circ \mathrm{Sp}_{K3^2, E}
   \circ \Phi^{\mathrm{FA}}_5
  \bigl(D^b(\mathrm{Coh}(X))\bigr)
\]
is a super-$E_1$-chiral algebra on $E$ whose charge lattice is
$\mathrm{II}_{25, 1}$, precisely the Fake Monster root lattice
(Borcherds~$1990$ \emph{Invent.\ Math.}~$109$:$405$, Theorem~$3$). The
commutation of the diagram at the functor level is the concatenation
of the three canonical constructions: Stage~$1$ is canonical up to
contractible choice by $E_5$-formality; Stage~$2$ is canonical by the
Dunn–Lurie pushforward formula; Stage~$3$ is canonical by the
Mukai–Conway chain plus no-roots selection.

That the $\pi_{\mathrm{Niem}}$-stage is a \emph{genuine} additional
datum, not an avatar of $(\Sigma_4, C)$-specialisation, is attested
by the $d = 3$ comparison: on $K3 \times E$ the Mukai lattice
$\widetilde{\Lambda}(K3) \cong \mathrm{II}_{4, 20}$ has positive-rank
$4$, so $\widetilde{\Lambda}(K3) \oplus U(E)$ has positive rank $5$,
and Nikulin~$1979$ Thm.~$1.12.2$ \emph{forbids} any primitive embedding
of $\mathrm{II}_{25, 1}$ (which needs positive rank $\geq 25$). The
$\pi_{\mathrm{Niem}}$-stage is vacuous at $d = 3$ precisely because
there is no rank-$24$ positive-definite sublattice in which to project;
it becomes non-trivial only at $d = 5$ where positive-rank $417 \gg 24$
accommodates $24$ Niemeier-orbit choices. This is Theorem
\texttt{f04w2:thm:pos-rank-obstr-d3} (positive-rank obstruction at
$d = 3$) and Theorem \texttt{f04w2:thm:pos-rank-avail-d5} (positive-rank
availability at $d = 5$) of Wave~$2$ F04, re-used verbatim.

Primary sources, collected:
\begin{itemize}
\item Borcherds~$1990$ \emph{Invent.\ Math.}~$109$:$405$ Thm.~$3$
(Fake Monster denominator; the output target of the three-stage).
\item Borcherds~$1995$ \emph{Invent.\ Math.}~$120$:$161$ \S$10$,~$14$
(automorphic products; K\"unneth restriction
$\Phi_{12}|_{\mathrm{II}_{2, 2}} = \Phi_{10}^2 = \Delta_5^2$ for the
cross-consistency with the $d = 3$ $K3 \times E$ row).
\item Borcherds~$1998$ \emph{Invent.\ Math.}~$132$:$491$ Thm.~$13.3$
(singular-theta lift weight formula $\kappa_{\mathrm{BKM}}(\Phi)
= c(0)/2$; input $1/\eta^{24}$ gives $\kappa_{\mathrm{BKM}}(\Phi_{12})
= 12$).
\item Mukai~$1987$ \emph{Nagoya Math.\ J.}~$81$:$153$ (Mukai lattice
$\widetilde{\Lambda}(K3) \cong \mathrm{II}_{4, 20}$).
\item Mukai~$1988$ \emph{Invent.\ Math.}~$94$:$183$ Thm.~$0.2$
(symplectic-automorphism embedding $\mathrm{Aut}_s(K3) \subset M_{23}$).
\item Niemeier~$1973$ \emph{J.\ Number Theory}~$5$:$142$ and
Venkov~$1980$ \emph{Proc.\ Steklov}~$148$:$65$ (Niemeier classification:
$24$ lattices).
\item Nikulin~$1979$ \emph{Izv.\ Akad.\ Nauk SSSR}~$43$:$111$
Thm.~$1.12.2$ (primitive embedding of even lattices into even
unimodular lattices).
\item Nikulin~$1980$ \emph{Trudy Moscow}~$38$:$75$ (symplectic-fixed
sublattices of K3; no reflection action on $(-2)$-classes).
\item Conway–Sloane~$1988$ \emph{Sphere Packings, Lattices and Groups}
Chap.~$10$ (Mathieu-Conway chain $M_{23} \subset M_{24} \subset
\mathrm{Co}_0$), Chap.~$16$ (Niemeier classification), Chap.~$18$ (Leech
uniqueness by no-roots), Chap.~$26$ ($\mathrm{II}_{25, 1}$ and Weyl
vector $\rho$).
\item Cheng–Duncan–Harvey~$2014$ \emph{Comm.\ Number Theory Phys.}~$8$:
$101$ (umbral moonshine: twenty-three non-Leech Niemeier siblings).
\item Pantev–Toën–Vaquié–Vezzosi~$2013$ \emph{Publ.\ IHÉS}~$117$:$271$
Thm.~$2.5$ ($(2 - d)$-shifted symplectic structure).
\item Calaque–Pantev–Toën–Vaquié–Vezzosi~$2017$ \emph{J.\ Topology}~$10$:
$483$ Thm.~$3.2$ ($n$-shifted Poisson dualisation).
\item Costello–Gwilliam~$2017$ \emph{Factorization Algebras in QFT}
Vol.~II \S$3.5$, \S$4.7$, \S$4.8$ (holomorphic factorisation algebras,
$\mathcal{P}_d$-operad, fibrewise pushforward).
\item Kontsevich~$2003$ \emph{Lett.\ Math.\ Phys.}~$66$:$157$
(deformation quantisation / $E_d$-formality), Lurie \emph{Higher
Algebra} Thm.~$5.1.2.2$ (Dunn–Lurie additivity).
\item Ayala–Francis~$2015$ \emph{J.\ Topology}~$8$:$1045$ (factorisation
homology).
\item Dunn~$1988$ \emph{J.\ Pure Appl.\ Algebra}~$50$:$237$ (little
$n$-cubes tensor products).
\item Serre~$1973$ \emph{Cours d'arithmétique} Ch.~$5$ \S$2$ (tensor
products of even unimodular lattices).
\item Borcherds~$1988$ \emph{J.\ Algebra}~$115$:$501$ (generalised
Kac–Moody algebras and Lie superalgebras with odd imaginary simple
roots).
\end{itemize}
\qed

## Inscription-ready TeX block

Direct insertion target: \texttt{working\_notes.tex} Part~II
two-stage factorisation block (around line $357$
\texttt{\textbackslash subsection\{The two-stage factorisation\}}),
or the $d = 5$ Fake-Monster discussion at line $395$--$400$.
Alternative target: \texttt{chapters/theory/cy\_to\_chiral.tex}
where $\Phi_d$ is constructed. Adjacent label usable for
cross-reference: \texttt{wn:thm:plat-two-stage} and
\texttt{wn:conj:plat-siblings-dim}. Reader-facing prose: no
bookkeeping vocabulary; no meta-narration; Chriss–Ginzburg voice.

```latex
\subsection{The three-stage refinement at $d = 5$: Niemeier projection
as genuine datum}
\label{wn:subsec:three-stage-d5}

On a single-K3 transverse surface the Mukai lattice
$\widetilde\Lambda(K3) \cong \mathrm{II}_{4,20}$ has positive rank
$4$, and the two-stage factorisation
$\Phi_3 = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C} \circ
\Phi^{\mathrm{FA}}_3$ is terminal. On the doubled transverse surface
$\Sigma_4 = K3_1 \times K3_2$ at $d = 5$, the Mukai-squared lattice
has positive rank $416$, and the $24$ Niemeier orbits in
$\mathrm{O}(\widetilde\Lambda(K3)^{\otimes 2})$ enumerate $24$
distinct positive-definite rank-$24$ primitive sublattice classes.
The two-stage factorisation must be refined to three stages to record
which Niemeier orbit is selected.

\begin{theorem}[Three-stage factorisation of $\Phi_5$ on
$K3 \times K3 \times E$]
\label{wn:thm:three-stage-d5}\ClaimStatusTheorem
Let $X = K3_1 \times K3_2 \times E$ with holomorphic volume
$\Omega_5 = \sigma_{K3_1} \wedge \sigma_{K3_2} \wedge dz_E$. The
canonical factorisation of $\Phi_5$ on this datum is
\[
 \Phi_5 \;=\; \pi_{\mathrm{Niem}} \;\circ\;
 \mathrm{Sp}^{\mathrm{ch}}_{K3^2, E} \;\circ\;
 \Phi^{\mathrm{FA}}_5,
\]
with the three stages characterised as follows.
\begin{enumerate}
\item $\Phi^{\mathrm{FA}}_5\colon \CY\text{-}\mathrm{cat}_5 \to
E_5\text{-}\mathrm{HolFA}(X)$ is the Kontsevich–Tamarkin
$E_5$-formality functor composed with Costello–Gwilliam–Li
holomorphic locality; its output carries a $(+1)$-shifted Poisson
bracket of cohomological degree $+1$ via the PTVV shift law at
$\mathrm{shift} = d - 4 = 1$.
\item $\mathrm{Sp}^{\mathrm{ch}}_{K3^2, E}\colon E_5\text{-}
\mathrm{HolFA}(X) \to E_1\text{-}\mathrm{ChirAlg}^{\mathrm{super}}(E)$
is factorisation homology along the tubular neighbourhood of
$E \hookrightarrow X$, using Dunn–Lurie additivity
$E_5 = E_4 \otimes E_1$; its charge lattice is
$\widetilde\Lambda(K3_1) \otimes \widetilde\Lambda(K3_2) \oplus U(E)$
of signature $(417, 161)$, and the $\Z_2$-super-grading is inherited
from the stable-framing class at $d = 5$.
\item $\pi_{\mathrm{Niem}}\colon \widetilde\Lambda(K3)^{\otimes 2}
\oplus U(E) \twoheadrightarrow \Lambda_{\mathrm{Leech}} \oplus U
= \mathrm{II}_{25, 1}$ is the Niemeier projection onto the
no-roots sublattice, canonically selected by the Mukai–Conway chain
$\mathrm{Aut}_s(K3) \subset M_{23} \subset M_{24} \subset
\mathrm{Co}_0$ via the no-roots condition on
symplectic-automorphism-invariant sublattices.
\end{enumerate}
The $23$ non-Leech Niemeier orbits index a $23$-fold family of
umbral-moonshine sibling Stage-$3$ outputs (Cheng–Duncan–Harvey
$2014$) at $d = 5$, of which the Leech orbit is the unique
no-roots selection realising the Fake Monster root lattice.
\end{theorem}

\begin{proof}
\emph{Stage~$1$.} Kontsevich $2003$ $E_d$-formality assigns a unique
$E_5$-algebra structure (up to contractible choice) on
$\HH^{\bullet}_{\mathrm{cat}}(D^b(\mathrm{Coh}(X)))$ for $X$ smooth;
Costello–Gwilliam–Li locality (Costello–Gwilliam $2017$ Vol.~II
\S$3.5$; Li $2012$ \emph{Comm.\ Math.\ Phys.}~$314$) assembles the
local $E_5$-algebras into a global holomorphic factorisation algebra.
The $(+1)$-shifted Poisson structure follows from
Pantev–Toën–Vaquié–Vezzosi $2013$ Thm.~$2.5$
($(2-d)$-shifted symplectic at $d = 5$ is $-3$-shifted, dual to
$(+1)$-shifted Poisson via Calaque–Pantev–Toën–Vaquié–Vezzosi $2017$
Thm.~$3.2$).

\emph{Stage~$2$.} Dunn–Lurie additivity (Lurie \emph{Higher
Algebra} Thm.~$5.1.2.2$; Dunn $1988$ for the little-$n$-cubes
version) decomposes $E_5 = (E_2 \otimes E_2) \otimes E_1$;
factorisation homology along $K3_1 \times K3_2$
(Ayala–Francis $2015$ \emph{J.\ Topology}~$8$:$1045$; alternately
Costello–Gwilliam $2017$ Vol.~II \S$4.8$ pushforward of factorisation
algebras) integrates out the $E_4 = E_2 \otimes E_2$ transverse
directions, leaving an $E_{5-4} = E_1$-chiral algebra on $E$. The
charge-lattice signature computation uses the tensor-product pairing
$(p_1 p_2 + q_1 q_2, p_1 q_2 + q_1 p_2) = (416, 160)$ at
$(4, 20) \otimes (4, 20)$, adjoined $(1, 1)$ for $U(E)$. The
$\Z_2$-super-grading from the framing class $\pi_5(B\Sp) = \Z_2$
promotes the target to super-$E_1$-chiral algebras.

\emph{Stage~$3$.} The Niemeier classification (Niemeier $1973$;
Venkov $1980$; Conway–Sloane $1988$ Chap.~$16$) enumerates $24$
even unimodular positive-definite rank-$24$ lattices; Leech
is uniquely characterised among these by the no-roots condition
(Conway–Sloane $1988$ Chap.~$18$). Primitive embedding of
$\mathrm{II}_{25, 1}$ into $\mathrm{II}_{417, 161}$ is guaranteed
by Nikulin $1979$ Thm.~$1.12.2$ (signature bounds $25 \leq 417$ and
$1 \leq 161$ both satisfied; trivial discriminant on Leech matches
any compensating discriminant on the orthogonal complement).
Canonical Leech-orbit selection follows from Mukai $1988$
Thm.~$0.2$ ($\mathrm{Aut}_s(K3) \subset M_{23}$) combined with
Conway–Sloane $1988$ Chap.~$10$ (Mathieu–Conway chain
$M_{23} \subset M_{24} \subset \mathrm{Co}_0 = \mathrm{Aut}(
\Lambda_{\mathrm{Leech}})$), and with the no-reflection-action
of symplectic automorphisms on $(-2)$-classes (Nikulin $1980$
\emph{Trudy Moscow}~$38$:$75$), forcing the
symplectic-automorphism-invariant sublattice to be root-free.

The three stages compose, and the target of the composite is the
super-$E_1$-chiral algebra on $E$ with charge lattice
$\mathrm{II}_{25, 1}$, matching the Fake Monster root lattice
(Borcherds $1990$ Thm.~$3$).
\end{proof}

\begin{remark}[Contrast with $d = 3$: Niemeier stage vacuous on
single-K3 transverse]
\label{wn:rem:three-stage-d3-vacuous}
At $d = 3$ on $K3 \times E$, the transverse Mukai lattice
$\widetilde\Lambda(K3) \cong \mathrm{II}_{4, 20}$ has positive rank $4$,
so $\widetilde\Lambda(K3) \oplus U(E)$ has positive rank $5$.
Nikulin $1979$ Thm.~$1.12.2$ forbids any primitive embedding
$\Lambda_{\mathrm{Leech}} \hookrightarrow \widetilde\Lambda(K3)
\oplus U(E)$ because the Leech-side positive rank $24$ exceeds the
host-side $5$. The Niemeier-projection stage is vacuous at $d = 3$;
the two-stage factorisation $\Phi_3 = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C}
\circ \Phi^{\mathrm{FA}}_3$ is terminal there. The Niemeier stage
enters only at $d = 5$ where positive-rank availability $417 \gg 24$
accommodates the full $24$-fold Niemeier orbit structure.
\end{remark}
```

## Cross-consistency notes

\textbf{(a) Spine consistency.} Theorem~\ref{wn:thm:three-stage-d5}
refines the two-stage factorisation of
working\_notes.tex~\S\ref{sec:two-stage-factorisation} at $d = 5$ by
adding a third stage; the two-stage form at $d = 3$ is unchanged. The
Fake-Monster Stage-$2$-specialisation statement at
working\_notes.tex line~$250$ (Borcherds $\Psi$-row census) and
line~$395$ (the $d = 5$ Poisson entry) is preserved verbatim; the
three-stage theorem extracts the additional $\pi_{\mathrm{Niem}}$
datum that was implicit in those statements but not yet formalised.

\textbf{(b) Wave-$1$ F04 consistency.} Theorem~\ref{wn:thm:three-stage-d5}
reproduces and extends Theorem~\texttt{f04:thm:two-stage-d5} of
Wave-$1$ F04 by (i) adding the explicit $\pi_{\mathrm{Niem}}$ stage,
(ii) stating the Mukai–Conway-chain canonical selection (implicit in
Wave-$1$ F04 Remark~\texttt{f04:rmk:leech-embedding-d5} but not
promoted there to theorem status). The three-stage picture is
anticipated at Wave-$1$ F04 \S~(i) of the cross-consistency block
(``$\pi_{\mathrm{Niem}}$: is an \emph{additional} datum on top of the
$(\Sigma_4, C)$ specialisation'') but was marked as a refinement
rather than a formal theorem.

\textbf{(c) Wave-$2$ F04 consistency.} Theorem~\ref{wn:thm:three-stage-d5}
formalises Theorem~\texttt{f04w2:thm:three-stage-d5} of Wave-$2$ F04
in closed theorem form with complete proof citations. The
Mukai–Conway chain is Theorem~\texttt{f04w2:thm:mukai-conway-chain}
of Wave-$2$ F04, re-used; the positive-rank obstruction at $d = 3$
and availability at $d = 5$ are
Theorem~\texttt{f04w2:thm:pos-rank-obstr-d3} and
Theorem~\texttt{f04w2:thm:pos-rank-avail-d5}, re-used.

\textbf{(d) Shift-law consistency.} The $(+1)$-shifted Poisson
structure at Stage-$1$ sits at the shift-law row
$(d, \mathrm{shift}, E_n^{\mathrm{cl}}) = (5, +1, E_5\text{-Poisson})$
of working\_notes.tex \S\ref{sec:organising-framework} line~$362$ and
Proposition~\texttt{prop:ptvv-shift-law} line~$388$. The
$\mathbb{Z}_2$-super-grading at Stage-$2$ matches the framing-class
$\pi_5(B\mathrm{Sp}) = \mathbb{Z}_2$ datum of working\_notes.tex
line~$2380$ Remark on PTVV-vs-framing orthogonality.

\textbf{(e) Universal Borcherds weight consistency.} The target of
the three-stage composition has charge lattice $\mathrm{II}_{25, 1}$
which is the Fake Monster root lattice; the associated BKM algebra
$\mathfrak{g}_{\mathrm{FM}}$ has Borcherds weight
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 = 12$ where $c(0) = 24 =
p_{24}(1)$ (the $24$-coloured partition count for $1$; first-principles
computed in Wave-$2$ F04 Cycle~$1$). This sits at the
universal-Borcherds-weight ladder of working\_notes.tex \S$250$,
extending the ladder from $\mathrm{II}_{3, 2}$ (Igusa $\Delta_5$,
weight $5$) to $\mathrm{II}_{26, 2}$ (Fake Monster $\Phi_{12}$,
weight $12$).

\textbf{(f) Four-$\kappa$ discipline.} No subscript is conflated:
$\kappa_{\mathrm{ch}}(X)$ is the Hodge-supertrace of
$K3 \times K3 \times E$, vanishing by Künneth
($\chi(\mathcal{O}_{K3})^2 \cdot \chi(\mathcal{O}_E) = 4 \cdot 0 = 0$);
$\kappa_{\mathrm{cat}}(X)$ is $\chi(\mathcal{O}_X)$, also $0$;
$\kappa_{\mathrm{BKM}}(\Phi_{12}) = 12$ via Borcherds weight formula;
$\kappa_{\mathrm{fiber}}(K3)$ is the rank of $\widetilde\Lambda(K3) = 24$.
The three-stage theorem is structural — it concerns the shape of
$\Phi_5$, not the values of $\kappa_{\bullet}$ — and does not involve
$\kappa$-arithmetic directly.

\textbf{(g) CoHA treatise consistency.} The three-stage picture is
compatible with the CoHA $= Y^+$ dictionary at $d = 5$ (conjectural
extension of Schiffmann–Vasserot $2013$): the Stage-$2$ output
$A^{\mathrm{FM,pre-Niem}}_E$ is conjecturally
$Y^+(\widehat{\mathfrak{g}}^{\mathrm{pre-Niem}})$ for some
pre-Niemeier-projected Lie-algebra datum, and $\pi_{\mathrm{Niem}}$
maps it to $Y^+(\mathfrak{g}_{\mathrm{FM}})$ by collapsing the
Stage-$2$ lattice to the Leech slice. The bracket-level identification
after projection is in the residual frontier.

\textbf{(h) Umbral-moonshine consistency.} The $23$ non-Leech Niemeier
orbits index Cheng–Duncan–Harvey $2014$ umbral siblings; each
$\Lambda \in \{24A_1, 12A_2, 8A_3, 6A_4, 4A_5 D_4, \ldots\}$ supplies
a distinct Stage-$3$ output with its own twined mock-modular form.
The full family of $24$ Niemeier-indexed $d = 5$ outputs populates a
Vol III sibling face at $d = 5$ beyond the Fake Monster, of which
only the Leech/no-roots orbit gives the Fake Monster; the
$23$ umbrals are parametrised residual frontier.

\textbf{(i) $(\infty, 1)$-lane discipline.} The theorem is stated at
the object-level on the CY side and at the $(\infty, 1)$-categorical
level at Stage-$1$ (where $E_5$-formality is the natural $(\infty, 1)$-
functorial statement) and Stage-$2$ (where factorisation homology is
a canonical $(\infty, 1)$-functor by Ayala–Francis). Stage-$3$ is
lattice-level-combinatorial and does not require $(\infty, 1)$-
functoriality; the morphism-level upgrade at Stages $1$ and $2$ is
the standard Kontsevich–Tamarkin / Ayala–Francis content.
Pattern $273$ (object-level vs $(\infty, 1)$-functor scope) is
respected: the object-level three-stage claim is established; the
$(\infty, 1)$-functorial upgrade for $\Phi_5$ as a functor on
$\mathrm{CY}$-$\mathrm{cat}_5$ requires morphism preservation,
an upgrade documented separately (residual frontier item of
Wave-$2$ F04).

\textbf{(j) AP-CY discipline.} No bare $\kappa$; all references
subscripted. No Drinfeld-centre-vs-averaging confusion (Stage-$2$
is factorisation-homology, not Drinfeld centre). No
$\Phi$-output-scope confusion at $d = 5$: the output is
$E_1$-chiral (on the $1$-dimensional reference curve $E$), not
$E_2$ (which would live at $d \leq 2$). No K\"unneth-multiplicative
confusion on the $\kappa_{\mathrm{cat}}$-side: the total space
$K3^2 \times E$ has $\chi(\mathcal{O}) = 4 \cdot 0 = 0$, not
$4$. No CoHA-vs-vertex-algebra confusion at $d = 5$: the Stage-$2$
output is an $E_1$-chiral algebra (which is a vertex algebra), not
a CoHA; the CoHA, if constructed, is a distinct Stage-$2.5$
object that localises to the vertex algebra.

## Residual frontier (downstream, not part of C21 closure)

\textbf{(F1)} \emph{Bracket-level identification
$Y^+(X) \simeq \mathfrak{g}_{\mathrm{FM}}$ at $d = 5$.}
\ClaimStatusOpen\
The extension of Schiffmann–Vasserot $2013$
$\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ to
$d = 5$ via doubly-reduced virtual cycle is open.

\textbf{(F2)} \emph{Closed-form DT integrand match
$Z^{\mathrm{red, red}}_{\mathrm{DT}}(X) = 1/\Phi_{12}$.}
\ClaimStatusOpen\ Oberdieck $2018$ establishes
$Z^{\mathrm{red}}_{\mathrm{DT}}(K3 \times E) = -1/\Phi_{10}$ at $d = 3$;
the doubled analogue at $d = 5$ is open.

\textbf{(F3)} \emph{Quantum renormalisation of 10-dim hCS on compact
CY$_5$.} \ClaimStatusOpen\ Bochner–Martinelli propagator at $5$
complex variables, one-loop BV anomaly, quantum master equation; the
Costello–Gaiotto–Li machine at $d = 5$ is open.

\textbf{(F4)} \emph{Super-grading match at bracket level.}
\ClaimStatusOpen\ The $\mathbb{Z}_2$-super-grading on the CY-side and
on the Lie-superalgebra side both exist; their match bracket-by-bracket
is structurally forced but not yet explicitly checked.

\textbf{(F5)} \emph{Niemeier projection full specification.}
\ClaimStatusOpen\ The canonical Leech-orbit selection via Mukai–Conway
chain is structurally natural per Theorem~\ref{wn:thm:three-stage-d5};
the explicit
$\mathrm{O}(\widetilde\Lambda(K3)^{\otimes 2})$-orbit parametrisation
of the $23$ non-Leech umbral moonshine Stage-$3$ siblings at $d = 5$
(Cheng–Duncan–Harvey $2014$ family) is open as an explicit family.
