# Agent C15 — Mordell-Weil sections $\leftrightarrow$ real simple roots of $\mathfrak{g}_{\Delta_5}$

## Terminal state

C (FRONTIER DECLARATION)

The item as posed is genuine frontier. Three distinct lattices of incompatible signature are being compared, no primitive sublattice embedding is possible between them, and the surviving candidate --- a correspondence between the two GBKM algebras via a common ambient Mukai lattice through *orthogonal projection along different idempotent datums* --- is not established in any primary source. A weaker, conditional form (state B) is available and stated at the end for completeness, but it does not close the commensurability question as the brief frames it.

## Statement of the frontier

\begin{frontier}[Mordell-Weil $\leftrightarrow$ real-simple-root correspondence for $(\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1},\, \mathfrak{g}_{\Delta_5})$]
\label{frontier:MW-delta5-real-roots}
\ClaimStatusOpen

Let $\pi: \mathcal{E} \to \mathbb{P}^1$ be a Jacobian elliptic fibration on a Shioda-Inose K3 surface $S$ of Picard rank $\rho(S) = 20$, with reducible-fibre configuration $I_2 + I_2 + 20\, I_1$. By the Shioda-Tate formula (F03 Wave 2, healed),
\[
 \mathrm{rk}\,\mathrm{MW}(\pi) \;=\; 20 - 2 - \mathrm{rk}\,L_{\mathrm{fibre}}^{(\mathrm{red})} \;=\; 20 - 2 - 2 \;=\; 16,
\]
and under the Shioda canonical height pairing rescaled by $\chi(\mathcal{O}_S)^{-1} = 1/2$, the Mordell-Weil lattice is isomorphic to $E_8(-1)^{\oplus 2}$ as a rank-$16$ negative-definite lattice (conditions (1)--(3) of Wave~2 F03 Theorem~\ref{f03w2:thm:MW-E8E8}; realisation on specific $T = \mathrm{diag}(2,6)$-locus Nishiyama-Kuwata fibrations, Nishiyama 1996 \emph{Japan J.\ Math.}~22 Thm.~4.1; Kumar 2008 \emph{Int.\ Math.\ Res.\ Not.}). Let $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ denote the conjectural generalised Kac-Moody algebra attached to the Stage-$2$ specialisation $(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ of the $E_3^{\mathrm{hol}}$-factorisation algebra $\mathcal{F}_{K3 \times E}$ (Conjecture~\ref{wn:conj:gkm-on-P1}; conditional on Borcherds 1998 Thm.~13.3 on signature $(2, n)$ applied at $n = 16$ or $n = 18$).

Let $\mathfrak{g}_{\Delta_5}$ denote the generalised Kac-Moody superalgebra of Gritsenko-Nikulin 1998 with denominator the Igusa paramodular cusp form $\Delta_5 \in M^!_5(\mathrm{Sp}_4(\mathbb{Z})^{\mathrm{para}})$, whose real-root Cartan is the rank-$3$ hyperbolic lattice $\Lambda^{2,1}_{II} \simeq \Lambda^{(1,1)} \oplus \langle 2 \rangle$ of signature $(2, 1)$, with three real simple roots $\{\delta_1, \delta_2, \delta_3\}$ having Gram matrix
\[
 G_{\Delta_5} \;=\; \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix} \;=\; 4I - 2\mathbf{1}\mathbf{1}^\top,
\]
eigenvalues $\{-2, 4, 4\}$, Weyl vector $\rho = \tfrac{1}{2}(\delta_1 + \delta_2 + \delta_3)$ with $(\rho, \rho) = -3/2$ (Section~\ref{sec:k3e-reflections} of \texttt{chapters/examples/k3e\_bkm\_chapter.tex}; Gritsenko-Nikulin 1998 \S 2--3).

Then the following three statements are jointly open.

\emph{(F1) Correspondence existence.}
There exists an explicit matching $\sigma \mapsto \delta_\sigma$ from a distinguished triple of Mordell-Weil sections $\{\sigma_1, \sigma_2, \sigma_3\} \subset \mathrm{MW}(\pi)$ to the three real simple roots $\{\delta_1, \delta_2, \delta_3\}$ of $\mathfrak{g}_{\Delta_5}$ such that the Shioda canonical height of $\sigma_i$ (rescaled by $\chi(\mathcal{O}_S)^{-1}$) equals $(\delta_i, \delta_i) = 2$, and such that the pairing matrix $\bigl(\langle\sigma_i, \sigma_j\rangle_{\mathrm{height, resc}}\bigr)_{i,j}$ equals $G_{\Delta_5}$.

\emph{(F2) Primitive sublattice embedding.}
The lattice $\Lambda^{2,1}_{II}$ embeds primitively (or as a finite-index sublattice of the saturation of) a rank-$3$ sub-lattice of $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ spanned by $\{\sigma_1, \sigma_2, \sigma_3\}$ in a manner compatible with (F1).

\emph{(F3) Commensurability of the GBKM algebras.}
The GBKM algebras $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ (constructed via the Stage-$2$ Borcherds lift on an ambient lattice of signature $(2, 18)$ or $(2, 16)$ --- see (G1) below) and $\mathfrak{g}_{\Delta_5}$ are commensurable in the sense that they share a common subalgebra of finite codimension on both sides, equivalently that they arise as distinct primitive restrictions of a common ambient Borcherds lift on $\mathrm{II}_{2,18}$ or $\mathrm{II}_{4,20}$.
\end{frontier}

\emph{Status of (F2) alone, on lattice-theoretic grounds.} (F2) is \textbf{false as stated}: no such embedding can exist, because $\Lambda^{2,1}_{II}$ is indefinite (signature $(2,1)$) whereas $E_8(-1)^{\oplus 2}$ is negative-definite (signature $(0, 16)$). An indefinite lattice does not embed isometrically into any definite lattice: the pairing on any rank-$2$ hyperbolic sublattice of the image would inherit an indefinite restriction, contradicting definiteness of the ambient. This is elementary linear algebra and is already recorded in \texttt{chapters/examples/k3e\_bkm\_chapter.tex} Remark~\ref{rem:k3ebkm-k3-monster-distinct} (``no rank-$3$ hyperbolic lattice embeds in rank-$2$ $\mathrm{II}_{1,1}$''; the same signature obstruction applies to embeddings into definite lattices).

\emph{Status of (F1) alone.} (F1) is \textbf{false as stated}: a rank-$3$ sub-lattice of $E_8(-1)^{\oplus 2}$ with the proposed Gram matrix $G_{\Delta_5}$ cannot exist because $G_{\Delta_5}$ has signature $(2, 1)$ while $E_8(-1)^{\oplus 2}$ has signature $(0, 16)$; the quadratic form $G_{\Delta_5}$ is not represented by the quadratic form of any rank-$3$ sub-lattice of $E_8(-1)^{\oplus 2}$.

\emph{Status of (F3) --- the genuine frontier.} (F3) is open. The two GBKM algebras live on incommensurable Cartan data (rank 3 hyperbolic $\Lambda^{2,1}_{II}$ for $\mathfrak{g}_{\Delta_5}$; conjecturally rank $16 + 2 = 18$ on $\mathrm{II}_{2, 16}$ or rank $2 + 2 = 4$ on a suitable ambient for $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ --- the exact Cartan of the elliptic-surface GBKM has not been pinned down in primary source). A commensurability in the classical sense of subgroup lattices admits no direct construction from Shioda height data; what the brief calls ``commensurability via some finite-index relation'' dissolves into: a conjectural common ambient Borcherds lift on the Mukai lattice $\widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$ of signature $(4, 20)$ whose two orthogonal-projection restrictions yield, respectively, $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ along the elliptic-fibration polarisation, and $\mathfrak{g}_{\Delta_5}$ along the Humbert divisor $H_1 \subset \mathcal{A}_2$ (Bruinier Heegner Chern-class reciprocity, \texttt{chapters/examples/k3\_chiral\_algebra.tex} line 3314).

## Primary-source gap

Three gaps must be closed simultaneously for any form of (F3) to become a theorem.

\textbf{(G1) The elliptic-surface GBKM Cartan, signature, and existence.}

Primary source needed: a theorem of the form

\begin{hypothesis}[G1-target: Shioda-Tate GBKM construction]
Let $\pi: \mathcal{E} \to \mathbb{P}^1$ be a Jacobian elliptic fibration on a K3 of Picard rank $20$ with fibre configuration $I_2 + I_2 + 20 I_1$. There exists a generalised Kac-Moody algebra $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ on an ambient lattice $L_{\mathcal{E}}$ of signature $(2, n_{\mathcal{E}})$, $n_{\mathcal{E}} \in \{16, 18\}$, whose real-root Cartan is the hyperbolic plane $\mathrm{II}_{1,1}$ tensored with $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ after Shioda-height rescaling, and whose denominator function $\Phi^{\mathcal{E}}$ is a Borcherds product of weight $n_{\mathcal{E}}/2$ on $L_{\mathcal{E}}$.
\end{hypothesis}

This hypothesis does not appear in Shioda 1990 \emph{J.\ Math.\ Soc.\ Japan}~39 (which proves the height-pairing formula but no Borcherds-lift construction), Nishiyama 1996 \emph{Japan J.\ Math.}~22 (which classifies MW-lattices via Kneser embeddings but does not construct GBKMs), or Scheithauer 2006 \emph{Invent.\ Math.}~164 (which classifies holomorphic reflective automorphic products of singular weight on prime-level lattices, not necessarily associated to elliptic-surface Shioda-Tate data). Borcherds 1998 Thm.~13.3 provides a construction apparatus (singular theta correspondence on $\mathrm{O}(2, n)$) but requires as input a weakly-holomorphic modular form of specific weight and Weil-representation type whose existence on the elliptic-surface-indexed lattice has not been established.

\textbf{(G2) Scheithauer 2006 scope and its (non-)applicability.}

Scheithauer 2006 \emph{Invent.\ Math.}~164, ``Generalized Kac-Moody algebras, automorphic forms and Conway's group,'' classifies \emph{holomorphic reflective automorphic products of singular weight} on even lattices of prime level and signature $(2, n)$ with $n \geq 3$. The classification (Theorem~3.1, extended by Dittmann-Ma-Scheithauer 2021 \emph{Adv.\ Math.}~386 to finiteness in each genus, and by Scheithauer 2017 \texttt{arXiv:1706.02546} Thm.~1.1 to a uniform singular-theta-correspondence description) produces exactly four such products on signature-$(2, n)$ lattices at $n \geq 3$: the K3 lift $\Delta_5$ on $\Lambda^{3,2}$ (signature $(2, 3)$); the Enriques half-lift $\Delta_{5/2}^{\mathrm{Enr}}$ on $\mathrm{II}_{1,1}(2) \oplus E_8$ (signature $(2, 9)$); the Monster $J$-face on $\mathrm{II}_{2,1}$ (signature $(2, 1)$, singular weight $0$); the Fake-Monster $\Phi_{12}$ on $\mathrm{II}_{2, 26}$ (signature $(2, 26)$, singular weight $12$). See \texttt{chapters/examples/k3e\_bkm\_chapter.tex} Remark~\ref{rem:bkm-scheithauer-primary-scope}, lines 8205--8264.

\emph{Observation.} The elliptic-surface candidate signature $(2, 16)$ or $(2, 18)$ is \emph{not} among the four Scheithauer-classified singular-weight holomorphic reflective products. Either the hypothetical $\Phi^{\mathcal{E}}$ is not of singular weight (it is of weight $< n_{\mathcal{E}}/2$, in which case it is not holomorphic reflective in the sense of Scheithauer and the GBKM construction of Borcherds 1998 Thm.~13.3 applies but yields a \emph{non-reflective} GBKM, distinct from $\mathfrak{g}_{\Delta_5}$), or it is the restriction of $\Phi_{12}$ along a primitive sublattice embedding $\mathrm{II}_{2, 16 \text{ or } 18} \hookrightarrow \mathrm{II}_{2, 26}$ (which reduces (F3) to an explicit Borcherds-pullback computation not performed in primary source).

\textbf{(G3) The common-ambient-lift conjecture.}

The form of (F3) that survives lattice-theoretic obstructions is the following.

\begin{hypothesis}[G3-target: common ambient]
There exists an automorphic form $\Phi^{\mathrm{amb}}$ on a signature-$(2, n_{\mathrm{amb}})$ Siegel or Mukai-degenerate ambient lattice $L^{\mathrm{amb}}$, $n_{\mathrm{amb}} \in \{18, 20, 26\}$, together with two primitive sublattice embeddings
\[
 L_{\mathcal{E}} \;\hookrightarrow\; L^{\mathrm{amb}} \;\hookleftarrow\; \Lambda^{3,2},
\]
such that
(i) the Borcherds lift of $\Phi^{\mathrm{amb}}$ along the first embedding (with appropriate theta-pairing against the orthogonal complement) yields $\Phi^{\mathcal{E}}$ and hence $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$;
(ii) along the second embedding yields $\Delta_5$ and hence $\mathfrak{g}_{\Delta_5}$;
(iii) the two restrictions are exchanged by a finite-index lattice automorphism of $L^{\mathrm{amb}}$ preserving $\Phi^{\mathrm{amb}}$ up to a meromorphic factor.
\end{hypothesis}

Candidate $L^{\mathrm{amb}} = \widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$ of signature $(4, 20)$: this is the Mukai lattice of K3, containing both the signature-$(3, 2)$ Humbert-divisor stratum (hosting $\Delta_5$ after Gritsenko-Nikulin 1998 and Bruinier 2002 Heegner Chern-class reciprocity, see \texttt{chapters/examples/k3\_chiral\_algebra.tex} line 3314) and the signature-$(2, 16)$ elliptic-fibration stratum (hosting the conjectural $\Phi^{\mathcal{E}}$). The two strata intersect at the codimension-two locus $H_1 \cap \{\pi\text{-fibration}\}$ inside $\mathcal{A}_2$-moduli. Whether this intersection produces the claimed commensurability via pullback-along-intersection is open.

The G3-hypothesis does not appear in primary source. Borcherds 1998 Thm.~14.3 asserts \emph{some} compatibility of Borcherds products under primitive sublattice embeddings (singular-theta compatibility), but does not establish the two-embedding-commensurability form above. Gritsenko-Nikulin 1998 Prop.~2.5 records lattice-embedding obstructions for specific pairs (K3 Mukai $\mathrm{II}_{4, 20}$ does not primitively embed in $\Lambda_{24} \oplus \mathrm{II}_{1,1}$), the logic of which suggests the present G3-compatibility requires a fresh enumeration of primitive rank-$16$ sublattices of $\widetilde{\Lambda}_{K3}$ commensurable with $E_8(-1)^{\oplus 2}$ under the Shioda-height metric.

## Why existing machinery is insufficient

\emph{(I1) Signature-incompatible direct sublattice embedding is impossible.}
Independent of any moduli or automorphic input, the signature mismatch between $\Lambda^{2,1}_{II}$ (signature $(2,1)$) and $E_8(-1)^{\oplus 2}$ (signature $(0, 16)$) forbids any isometric embedding of the first into the second. Finite-index relations (commensurability as subgroup lattices) also fail for the same signature reason: a finite-index sublattice of $E_8(-1)^{\oplus 2}$ remains definite.

\emph{(I2) Shioda height pairing produces definite lattice.}
Shioda's canonical-height pairing on $\mathrm{MW}(\pi)/\mathrm{tors}$ is a positive-definite $\mathbb{Q}$-valued pairing (Shioda 1990 Thm.~8.6; Sch\"utt-Shioda 2019 \emph{Mordell-Weil Lattices} Prop.~6.36). Under the rescaling by $\chi(\mathcal{O}_S) = 2$ it takes integer values on appropriate sub-lattices (Wave~2 F03 Thm.~\ref{f03w2:thm:MW-E8E8}), but definiteness is preserved. Real simple roots of $\mathfrak{g}_{\Delta_5}$ have norm $+2$ in the ambient $\Lambda^{2,1}_{II}$, matching $E_8$-norm; this creates \emph{numerical but not structural coincidence}. Numerically, three sections with pairwise height $-2$ would give the $\Delta_5$ Gram matrix up to the factor $-1$, but no such triple exists in a definite lattice: three vectors of pairwise inner product $-2$ in a definite lattice with self-pairing $+2$ must be linearly dependent (Cauchy-Schwarz bound).

\emph{(I3) Scheithauer 2006 classification limits the candidates.}
The ``four-is-all'' classification of holomorphic reflective automorphic products of singular weight on signature-$(2, n)$ at $n \geq 3$ (Scheithauer 2006 + Scheithauer 2017 + Dittmann-Ma-Scheithauer 2021) does not produce a signature-$(2, 16)$ or $(2, 18)$ candidate. Any $\Phi^{\mathcal{E}}$ underlying $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ must therefore be either non-singular-weight (in which case the GBKM is non-reflective, and Gritsenko-Nikulin 1998 Thm.~5.2 excludes reflective-GN compatibility with $\mathfrak{g}_{\Delta_5}$), or a restriction of the Fake-Monster $\Phi_{12}$ along a primitive sub-lattice embedding $\mathrm{II}_{2, 16 \text{ or } 18} \hookrightarrow \mathrm{II}_{2, 26}$, which is a non-trivial Borcherds-pullback computation that has not been performed.

\emph{(I4) Bruinier Heegner Chern-class reciprocity is divisor-level, not algebra-level.}
The Bruinier 2002 \emph{Lecture Notes Math.}~1780 Prop.~5.1 identity --- $[\Delta_5] \in \mathrm{CH}^1(\mathcal{A}_2^*)$ has multiplicity $2$ along $H_1$ and no other Heegner support at discriminant $\leq 4$ (cf.\ \texttt{chapters/examples/k3\_chiral\_algebra.tex} line 3314) --- pins the divisor class of $\Delta_5$ uniquely but does not transport GBKM structure from $\mathfrak{g}_{\Delta_5}$ to any elliptic-fibration GBKM. The Wang-Williams 2023 pullback rigidity of $\Phi_{12}$ (Vol.\ III spine, \texttt{working\_notes.tex}) addresses the Fake-Monster lift but similarly does not produce a GBKM commensurability.

\emph{(I5) Conway-row analogy breaks at positive-definite rank.}
Scheithauer 2006 Ex.~7.3 constructs a super-character-normalised Borcherds lift on $\Lambda_{24}$ (Leech, signature $(24, 0)$) via the metaplectic extension $\Psi^{\mathrm{metap}}$, producing the Conway moonshine module $\mathbf{H}_{\mathrm{Conway}}$ (see \texttt{chapters/examples/k3e\_bkm\_chapter.tex} Theorem~\ref{thm:bkm-vs-natural-equals-psi-super}, line 8401; Duncan 2007 \texttt{arXiv:math/0502267}). This metaplectic route accepts positive-definite lattices as input but produces an \emph{independent} Borcherds algebra, not a commensurability with $\mathfrak{g}_{\Delta_5}$. The rank-$16$ positive-definite $E_8(-1)^{\oplus 2}$ could in principle serve as a metaplectic-$\Psi$ input (analogous to Scheithauer 2006 Ex.~7.3 on $\Lambda_{24}$), yielding a distinct Borcherds algebra $\mathbf{H}_{E_8 \oplus E_8}$; but (a) no explicit theta input $\Theta_{E_8 \oplus E_8}/\eta^?$ of the right weight on $\widetilde{\mathrm{SL}}_2$ has been identified, and (b) the resulting Borcherds algebra would be structurally analogous to Conway, not commensurable with $\mathfrak{g}_{\Delta_5}$.

## Hypothesis (weaker state-B form)

A weaker conditional closure is available. Adding the G3-hypothesis, one obtains the following.

\begin{theorem}[Conditional: restriction-compatibility of a common ambient Borcherds lift]
\label{thm:C15-conditional-ambient}
\ClaimStatusConjectured

Assume the G3-hypothesis (``common ambient'') with $L^{\mathrm{amb}} = \widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$, and an automorphic form $\Phi^{\mathrm{amb}}$ of weight $10$ on $L^{\mathrm{amb}}$ whose divisor on $\mathcal{D}_{\widetilde{\Lambda}_{K3}} / \mathrm{O}^+(\widetilde{\Lambda}_{K3})$ is the union of two Heegner-like components: (i) the codimension-two Humbert locus $H_1$ intersected with the elliptic-fibration polarisation $\mathrm{Pic}_{\mathcal{E}} \otimes \mathbb{Q}$ and (ii) the codimension-one divisor of $\Delta_5$ after pullback along the signature-$(3,2)$ Humbert-stratum embedding.

Then there is a bi-restriction diagram
\[
 \Phi^{\mathcal{E}} \;\xleftarrow{\pi_{\mathcal{E},*}}\; \Phi^{\mathrm{amb}} \;\xrightarrow{\pi_{H_1, *}}\; \Delta_5,
\]
where $\pi_{\mathcal{E}, *}$ and $\pi_{H_1, *}$ are orthogonal-projection pullbacks onto sub-locus lattices $L_{\mathcal{E}} \subset L^{\mathrm{amb}}$ and $\Lambda^{3,2} \subset L^{\mathrm{amb}}$ respectively. The two GBKM algebras $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ and $\mathfrak{g}_{\Delta_5}$ are both sub-GBKMs of a common $\mathfrak{g}_{\mathrm{amb}}$ attached to $\Phi^{\mathrm{amb}}$, with the inclusions induced by the orthogonal-projection primitive embeddings.

\emph{Commensurability qualifier.} In this conditional form, the commensurability of the two GBKMs is \emph{ambient-derived}, not direct: they are sub-algebras of a common $\mathfrak{g}_{\mathrm{amb}}$ rather than finite-index relatives of each other. The real-root Cartan $\Lambda^{2,1}_{II}$ of $\mathfrak{g}_{\Delta_5}$ embeds primitively into $\widetilde{\Lambda}_{K3}$ along $\Lambda^{3,2}$ (of signature $(3,2)$); the Mordell-Weil lattice $E_8(-1)^{\oplus 2}$ embeds primitively into $\widetilde{\Lambda}_{K3}$ along the orthogonal complement of the elliptic-fibration hyperbolic plane $\langle F, S_0\rangle = U$ inside $\mathrm{NS}(S)$. The two primitive embeddings have non-trivial but non-primitive intersection in $\widetilde{\Lambda}_{K3}$, realising the conditional commensurability.
\end{theorem}

The G3-hypothesis is not established: no automorphic form $\Phi^{\mathrm{amb}}$ on $\mathrm{O}(4, 20)$-Mukai domain $\mathcal{D}_{\widetilde{\Lambda}_{K3}}$ satisfying (i) and (ii) is known. The candidate construction via Borcherds 1998 Thm.~13.3 applied on $\widetilde{\Lambda}_{K3}$ --- signature $(4, 20)$, non-reflective, non-singular-weight --- produces Borcherds products that are not classified by Scheithauer 2006 / Scheithauer 2017 / Dittmann-Ma-Scheithauer 2021 (whose scope is signature-$(2, n)$). Extending the singular-theta correspondence to $(p, q)$ with $p \geq 3$ is a genuine frontier; it would additionally require identifying which Jacobi-form input on the $\mathrm{O}(4, 20)$ Weil representation pulls back along both embeddings with the prescribed divisor structure.

## Inscription-ready TeX block

\begin{frontier}[Mordell-Weil $\leftrightarrow$ $\mathfrak{g}_{\Delta_5}$ real-simple-root commensurability]
\label{frontier:C15-MW-delta5}
\ClaimStatusOpen
Let $\pi: \mathcal{E} \to \mathbb{P}^1$ be the Jacobian elliptic fibration on a Shioda--Inose K3 of Picard rank $20$ with fibre configuration $I_2 + I_2 + 20\, I_1$, realising $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ as a rank-$16$ negative-definite Shioda-height lattice after rescaling by $\chi(\mathcal{O}_S)^{-1} = 1/2$ (conditions of Shioda 1990 \emph{J.\ Math.\ Soc.\ Japan}~39 Thm.~8.6; Sch\"utt--Shioda 2019 \emph{Mordell--Weil Lattices} Prop.~6.36; Nishiyama 1996 \emph{Japan J.\ Math.}~22 Thm.~4.1 for realisability on specific $T = \mathrm{diag}(2, 6)$-locus fibrations).

Let $\mathfrak{g}_{\Delta_5}$ denote the Gritsenko--Nikulin generalised Kac--Moody superalgebra whose denominator is the Igusa paramodular cusp form $\Delta_5$, with real-root Cartan $\Lambda^{2,1}_{II}$ of signature $(2, 1)$ and three real simple roots $\{\delta_1, \delta_2, \delta_3\}$ with Gram matrix $4I - 2\mathbf{1}\mathbf{1}^\top$ and eigenvalues $\{-2, 4, 4\}$.

The question of whether there is a primitive sublattice commensurability
\[
 E_8(-1)^{\oplus 2} \supset \langle \sigma_1, \sigma_2, \sigma_3\rangle_{\mathbb{Z}} \;\stackrel{?}{\cong}\; \Lambda^{2,1}_{II}
\]
has a negative signature-obstruction answer: no rank-$3$ sublattice of a definite lattice can be isometric to an indefinite lattice of signature $(2, 1)$. The surviving frontier statement is the \emph{common-ambient commensurability}: do the two generalised Kac--Moody algebras $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ and $\mathfrak{g}_{\Delta_5}$ arise as primitive-restriction sub-algebras of a common Borcherds algebra $\mathfrak{g}_{\mathrm{amb}}$ on the Mukai signature-$(4, 20)$ lattice $\widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$, with the two primitive embeddings realising respectively $\Lambda^{3,2} \hookrightarrow \widetilde{\Lambda}_{K3}$ (Humbert-divisor stratum, hosting $\Delta_5$ via Bruinier 2002 \emph{Lecture Notes Math.}~1780 Prop.~5.1 Heegner reciprocity) and $\mathrm{MW}(\pi) \oplus U_{\mathrm{fibre}} \hookrightarrow \widetilde{\Lambda}_{K3}$ (elliptic-fibration stratum). The construction of such a common $\mathfrak{g}_{\mathrm{amb}}$ requires extending the Borcherds 1998 \emph{J.\ reine angew.\ Math.}~494 Thm.~13.3 singular-theta correspondence beyond the Scheithauer 2006 \emph{Invent.\ Math.}~164 ``singular-weight holomorphic reflective products on signature-$(2, n)$, $n \geq 3$'' classification, to a non-reflective automorphic form on $\mathrm{O}(4, 20)$ with prescribed bi-stratum Heegner divisor. No such construction is available in Borcherds 1998, Scheithauer 2006/2008/2017, Dittmann--Ma--Scheithauer 2021, Gritsenko--Nikulin 1998, or Bruinier 2002.
\end{frontier}

## Cross-consistency notes

\emph{Wave-1 spine (\texttt{notes/platonic\_synthesis\_post\_adversarial.tex}).}
The first-wave spine stated ``$\mathrm{MW}(\pi) = E_8 \oplus E_8$ indexes the real simple roots of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$, commensurable with $\mathfrak{g}_{\Delta_5}$.'' Wave~2 F03 corrected the MW rank claim (rank $16$ only at $I_2 + I_2 + 20 I_1$ configuration, rescaled Shioda height). The present closure C15 further records the signature obstruction that prevents any direct rank-$3$ primitive embedding of $\Lambda^{2,1}_{II}$ into $\mathrm{MW}(\pi)$, consistent with Wave~2 F03 Cycle~6 observation that ``the Inose pencil is \emph{not} the fibration that produces $\mathfrak{g}_{\Delta_5}$.''

\emph{Wave-2 refinement (\texttt{notes/platonic\_synthesis\_wave2\_refinement.tex}).}
The refinement records at line 524--531 that the MW lattice, at the $I_2 + I_2 + 20 I_1$ configuration with rescaling, indexes the \emph{internal} simple-root system of the Stage-$2$ GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ --- via unimodularity of $E_8(-1)^{\oplus 2}$ and discriminant-group triviality. C15 extends this by noting that the internal-indexing produces real simple roots of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ \emph{but not of $\mathfrak{g}_{\Delta_5}$}; the two sets of real simple roots are disjoint lattice objects, shared only conjecturally via a common ambient as in Theorem~\ref{thm:C15-conditional-ambient}. The refinement's Tier-I residual item ``Elliptic-surface specialisation $(\mathcal{E}, \mathbb{P}^1)$ at Shioda-Inose $\rho = 20$, primary-source gap: Borcherds 1998 Thm.~13.3 on signature $(2, 20)$'' is \emph{expanded} by C15: the gap is (G1) + (G2) + (G3), not Borcherds 1998 alone.

\emph{CoHA treatise (\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}).}
The treatise does not address the Shioda-Inose MW-to-$\mathfrak{g}_{\Delta_5}$ question directly (it concerns the $\mathbb{C}^3$ CoHA / $\mathcal{W}_{1+\infty}$ identification). No cross-consistency conflict; C15 is orthogonal.

\emph{CLAUDE.md charter.}
The charter requires four-$\kappa$ discipline: $\kappa_{\mathrm{ch}}(K3 \times E) = 0$ (Hodge supertrace), $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (Künneth-multiplicative on total space), $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$ (Borcherds weight $c_1(0)/2$), $\kappa_{\mathrm{fiber}}(K3) = 24$. C15 addresses neither a $\kappa$-value correction nor a new $\kappa$-invariant claim; it clarifies the lattice-level incommensurability between $\mathrm{MW}(\pi)$ (rank $16$, $\kappa_{\mathrm{fiber}}$-adjacent: the rank of $\mathrm{NS}(S)$ minus the $\langle F, S_0\rangle$ bi-vector minus reducible fibres) and $\Lambda^{2,1}_{II}$ (rank $3$, $\kappa_{\mathrm{BKM}}$-associated: the Cartan of the Igusa $\Phi_1 = \Delta_5$ algebra).

\emph{\texttt{chapters/examples/k3e\_bkm\_chapter.tex}.}
The chapter at lines 623--688 records the three-real-simple-roots structure of $\mathfrak{g}_{\Delta_5}$, the signature $(2, 1)$ of $\Lambda^{2,1}_{II}$, and Remark~\ref{rem:k3e-ten-is-not-real-simples} at line 685 warning against conflating the integer $10$ (Fourier coefficient $c_{\phi_{0,1}}(0,0)$ and number of even theta constants on $\mathbb{H}_2$) with the number of real simple roots (which is $3$). C15 is consistent with this: the purported MW-to-real-root matching would require $16$ real simple roots on the $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ side, not $3$. No number of rank-$3$ sublattices of $\mathrm{MW}(\pi)$ can match the rank-$3$ Cartan of $\mathfrak{g}_{\Delta_5}$ up to isometry because of the signature obstruction.

\emph{\texttt{chapters/examples/cy\_c\_beyond\_k3e\_existence\_obstruction.tex}.}
The chapter at lines 5123--5130 records the Shioda height pairing $\langle s_j, s_k \rangle_{\mathrm{NS}} = \chi(\mathcal{O}_S) - \sum_v \mathrm{contr}_v(s_j, s_k) = 2 - 1 = 1$ for distinct torsion sections. C15 is consistent: torsion sections and free sections behave differently under Shioda height, with the torsion-case $\chi - \mathrm{contr}_v = 1$ applicable to the $g_N$-twisted orbifold-CY$_3$ construction, and the free-case applicable to the $E_8(-1)^{\oplus 2}$-MW-lattice question. The two pairings produce distinct lattice structures, neither of which embeds into $\Lambda^{2,1}_{II}$.

\emph{Lorgat 2020 \texttt{raeez.lorgat.automorphic-corrections.pdf}.}
The reference paper (cf.\ \texttt{memory/reference\_lorgat\_2020\_automorphic\_corrections.md}) constructs $\mathfrak{g}_{\Delta_5}$ as the Borcherds lift of $\phi_{0,1}$ on $\Lambda^{3,2}$, with real-root Cartan $\Lambda^{2,1}_{II}$ of Gram matrix $2$ on diag, $-2$ off-diag (matching the three-$\delta$ structure used throughout). Lorgat 2020 does not address the elliptic-surface GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ or its commensurability with $\mathfrak{g}_{\Delta_5}$. The Conjecture~1 of Lorgat 2020 (DT zeta $\leftrightarrow$ 8 Gritsenko-Cl\'ery forms $\leftrightarrow$ GKM denominators via twined elliptic genera) is a distinct statement about the $N \in \{1, \ldots, 8\}$ paramodular family, not about $\mathrm{MW}(\pi)$-indexed algebras. C15 is orthogonal to Lorgat 2020 Conjecture~1.

\emph{Adjudication Ledger W14-W19 (\texttt{memory/reference\_adjudication\_ledger\_w14\_w19.md}).}
The ledger's 32 verified facts, 6 corrected retractions, and 9 conjectures for $\mathbf{H}_{\Delta_5}$ do not include a MW-indexed real-root correspondence; C15's frontier declaration is consistent with the ledger's open status on structural extensions of $\mathfrak{g}_{\Delta_5}$.
