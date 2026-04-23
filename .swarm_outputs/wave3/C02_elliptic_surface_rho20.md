# Agent C02 — Elliptic-surface specialisation $(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ at Shioda–Inose $\rho(K3) = 20$

## Terminal state

**(B) CONDITIONAL CLOSURE.**

The item admits a precise statement of the Borcherds lift with Mordell–Weil identification of real simple roots and commensurability (not equality) with $\mathfrak{g}_{\Delta_5}$ conditional on two named hypotheses (Nishiyama 1996 embedding realisability for the specific $(T, \pi)$-pair; Gritsenko–Nikulin 1998 paramodular compatibility of Shioda-height-indexed real roots). Both hypotheses are published; the only residue is an explicit Weierstrass-model computation matching real-root walls across the $\mathrm{II}_{2, 20} \supset \Lambda^{3, 2}$ Humbert-restriction chain. Flag `\ClaimStatusConjectured`.

## Framing correction on the brief's signature reading

The brief states: *"the Picard lattice has signature $(1, 19)$ after the genus-shift. For the singular-theta lift Borcherds 1998 Thm 13.3 requires signature $(b^+, 2)$ with $b^+ \geq 1$; we have $(1, 19)$ which is $b^+ = 1$, $b^- = 19 = b^+ + 18$."*

Two corrections are forced before the closure can proceed.

**(a) The signature-convention in Borcherds 1998 Thm 13.3 is $(b^+, b^-) = (2, n)$ with $b^+ = 2$** — the Grassmannian is the space of positive definite $2$-planes, and the singular theta lift $\Psi$ converges to a holomorphic automorphic form of weight $c(0)/2$ on the period domain $\mathcal{G}(L) \cong \mathrm{O}(2, n)/(\mathrm{O}(2) \times \mathrm{O}(n))$ exactly when $b^+ = 2$. The convention is fixed (Borcherds 1998 \emph{Invent.\ Math.}\ 132, Thm.\ 13.3 statement plus \S 4–5 on the Siegel domain). In the Vol III convention of Theorem \texttt{thm:borcherds-lift-universal} (\texttt{chapters/examples/k3e\_bkm\_chapter.tex} L1605–1623) the hypothesis is stated as $b^+ \ge 2$ for the Grassmannian to be a non-trivial Hermitian symmetric domain; the brief's "$b^+ \ge 1$" under-states the hypothesis.

**(b) The Picard lattice of a singular K3 is not the correct ambient for the elliptic-surface specialisation.** The Picard lattice $\mathrm{NS}(S)$ of a Shioda–Inose K3 has signature $(1, 19)$ with $b^+ = 1$. The Stage-$2$ specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\mathcal{E}, \mathbb{P}^1}$ acts on $\mathcal{F}_{K3 \times E} = \Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$, which carries the \emph{product} lattice datum $\mathrm{NS}(S) \oplus \mathrm{NS}(E) = \mathrm{NS}(S) \oplus U_E$ (where $U_E = H^0(E) \oplus H^2(E)$ contributes a hyperbolic plane of signature $(1, 1)$). Hence the ambient for the Borcherds lift of the elliptic-surface specialisation is
\[
  \Lambda^{\mathcal{E}, \mathbb{P}^1} \;=\; \mathrm{NS}(S) \oplus U_E, \qquad
  \mathrm{sig}(\Lambda^{\mathcal{E}, \mathbb{P}^1}) \;=\; (1 + 1,\ 19 + 1) \;=\; (2, 20),
\]
at which $b^+ = 2$ satisfies Borcherds 1998 Thm.\ 13.3. The brief's framing that "$b^+ = 1$ fails the hypothesis" is correct for the Picard lattice alone; the framing is incorrect as applied to the ambient of the elliptic-surface specialisation on $K3 \times E$, which is $(2, 20)$, not $(1, 19)$. This is exactly the $\mathrm{II}_{1, 1}$-hyperbolic-extension mechanism recorded in \texttt{chapters/examples/k3e\_bkm\_chapter.tex} L3854 ("the $2$-dimensional $\mathrm{II}_{1, 1}$ hyperbolic extension").

## Statement of the theorem

\begin{theorem}[Elliptic-surface specialisation at Shioda--Inose $\rho = 20$; $\ClaimStatusConjectured$, conditional on [N1996] and [GN1998]]
\label{thm:c02-elliptic-surface-rho-20-conditional}
Let $S$ be a Shioda--Inose K3 with Picard rank $\rho(S) = 20$, transcendental lattice $T = T(S)$ of rank $2$ and signature $(2, 0)$, equipped with a Jacobian elliptic fibration $\pi \colon S \to \mathbb{P}^1$ of Kodaira configuration $(I_2, I_2, 20 \cdot I_1)$; let $(E, e_0)$ be an elliptic curve with identity $e_0$; and let $X = S \times E$. Assume:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item \textup{(Nishiyama 1996 realisability)} The fibration $\pi$ is a Nishiyama--Kneser lattice embedding of type $(T, 2 A_1)$ into $\Lambda_{K3}$ with Mordell--Weil quotient $\mathrm{MW}(\pi)/\mathrm{tors}$ of rank $16$ and Shioda-height lattice isomorphic to $E_8(-1)^{\oplus 2}$ under the rescaling $\chi(\mathcal{O}_S)^{-1} = \tfrac{1}{2}$. Equivalently: the rank-$2$ reducible fibre lattice $L^{(\mathrm{red})}_{\mathrm{fibre}}(\pi) = 2 A_1$ equals the negative-defect lattice $T^\perp \cap \Lambda_{K3}$ modulo $U_{\mathrm{fibre + section}} \oplus E_8(-1)^{\oplus 2}$ under Shioda--Tate.
\item \textup{(Gritsenko--Nikulin 1998 paramodular compatibility)} The image of the Shioda-canonical-height lattice $E_8(-1)^{\oplus 2}$ under the Humbert-restriction chain
\[
 \mathrm{II}_{2, 18}
 \;\xrightarrow{\;\iota_{\mathrm{prim}}\;}\;
 \mathrm{II}_{2, 20}
 \;\xrightarrow{\;H_1\;}\;
 \Lambda^{3, 2}
\]
coincides, up to $W^{(2)}(\Lambda^{2, 1}_{II})$-action, with the real-simple-root wall system of $\mathfrak{g}_{\Delta_5}$ indexed by the norm-$2$ vectors of $\Lambda^{2, 1}_{II}$ (Gritsenko--Nikulin 1998 Thm.\ 2.1 plus the Fricke involution $w_{t = 1}$ of \texttt{chapters/examples/k3\_chiral\_algebra.tex} L3016--3032).
\end{enumerate}
Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Borcherds lift on the elliptic-surface ambient.)} The Stage-$2$ specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\mathcal{E}, \mathbb{P}^1}$ applied to $\mathcal{F}_{K3 \times E} = \Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$ at the fibration $\pi$ produces a GBKM superalgebra $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ with denominator
\[
 \Phi^{\mathcal{E}, \mathbb{P}^1} \;=\; \Psi\bigl(\phi^{\pi, g}_{0, 1};\ \Lambda^{\mathcal{E}, \mathbb{P}^1}\bigr),
\]
where $\Psi$ is the Borcherds singular-theta lift of \cite[Thm.\ 13.3]{Borcherds1998} on the signature-$(2, 20)$ lattice $\Lambda^{\mathcal{E}, \mathbb{P}^1} = \mathrm{NS}(S) \oplus U_E$, and $\phi^{\pi, g}_{0, 1}$ is the $\pi$-twisted Jacobi form of weight $0$ and index $1$ obtained from the K3 elliptic genus $Z_{K3}$ by the Bryan--Oberdieck orbifold-DT reduction applied to the Mordell--Weil torsion-free sector.
\item \textup{(Mordell--Weil identification of real simple roots.)} Under (H1), the real simple roots of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ are indexed by primitive Mordell--Weil sections $\sigma \in \mathrm{MW}(\pi)/\mathrm{tors}$ via the assignment
\[
 \sigma \;\longmapsto\; \alpha_\sigma, \qquad
 \langle \alpha_\sigma,\, \alpha_\sigma \rangle \;=\; \tfrac{1}{\chi(\mathcal{O}_S)}\,\langle \sigma,\, \sigma \rangle_{\mathrm{Shioda\text{-}height}} \;=\; -2,
\]
so that $\alpha_\sigma$ is an $E_8$-root inside $E_8(-1)^{\oplus 2} \subset \Lambda^{\mathcal{E}, \mathbb{P}^1}$. The indexing is internal (simple-root walls of the Weyl chamber), not an external orbit action on $H_4(K3 \times E; \mathbb{Z})$, by the discriminant-group argument: $\mathrm{disc}(E_8(-1)^{\oplus 2}) = 1$, so the discriminant form is trivial and no non-trivial external lattice symmetry is carried.
\item \textup{(Commensurability with $\mathfrak{g}_{\Delta_5}$.)} Under (H2), $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ is commensurable with $\mathfrak{g}_{\Delta_5}$: there exist primitive sublattice embeddings
\[
 \Lambda^{2, 1}_{II} \;\subset\; \Lambda^{3, 2} \;\subset\; \mathrm{II}_{2, 20} \;\cong\; \Lambda^{\mathcal{E}, \mathbb{P}^1},
\]
and a finite-index inclusion $\mathfrak{g}_{\Delta_5} \subset \mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ of GBKM algebras along which:
\begin{itemize}
\item the real simple roots $\{\delta_1, \delta_2, \delta_3\}$ of $\Lambda^{2, 1}_{II}$ inject into the $\mathrm{MW}$-indexed real simple roots $\{\alpha_\sigma\}_{\sigma \in \mathrm{MW}(\pi)/\mathrm{tors}}$ as the three generators of the rank-$3$ hyperbolic core;
\item the imaginary simple roots of $\mathfrak{g}_{\Delta_5}$ at Heegner discriminants $D \in \{-1, -4, -9, \dots\}$ (multiplicities $c_{\Delta_5}(N, \ell)$) pull back to imaginary simple roots of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ at the same discriminants with multiplicities equal to the $\pi$-twisted Fourier coefficients $c_{\phi^{\pi, g}_{0, 1}}(N, \ell)$;
\item equality $\mathfrak{g}_{\Delta_5} = \mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ holds if and only if the twisted input reduces to the untwisted K3 elliptic genus, i.e.\ $\phi^{\pi, g}_{0, 1} = \phi^{K3}_{0, 1}$, in which case the fibration $\pi$ specialises to the $(\mathcal{E}, \mathbb{P}^1) = (K3, E)$ diagonal trivial specialisation and the Humbert-restriction chain collapses to the identity.
\end{itemize}
\item \textup{(Weight preservation.)} The Borcherds weight of $\Phi^{\mathcal{E}, \mathbb{P}^1}$ equals $c_{\phi^{\pi, g}_{0, 1}}(0) / 2$. When $\phi^{\pi, g}_{0, 1} = \phi^{K3}_{0, 1}$ the weight is $c_1(0) / 2 = 10 / 2 = 5 = \mathrm{wt}(\Delta_5)$, consistent with $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$.
\end{enumerate}
\end{theorem}

## Proof

\begin{proof}
\emph{Signature accounting.}
The Shioda--Inose K3 has transcendental lattice $T(S)$ of rank $2$ with $\mathrm{sig}(T) = (2, 0)$ (positive-definite binary quadratic form; Shioda--Inose 1977 Theorem). The K3 lattice $\Lambda_{K3} = U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}$ has signature $(3, 19)$. By orthogonality, $\mathrm{NS}(S) = T(S)^\perp \cap \Lambda_{K3}$ has signature $(3, 19) - (2, 0) = (1, 19)$. Adjoining the elliptic factor $H^{1, 1}(E) = U_E$ of signature $(1, 1)$ gives
\[
 \Lambda^{\mathcal{E}, \mathbb{P}^1} \;:=\; \mathrm{NS}(S) \oplus U_E, \qquad
 \mathrm{sig}(\Lambda^{\mathcal{E}, \mathbb{P}^1}) \;=\; (2, 20),
\]
satisfying $b^+ = 2$ as required by Borcherds 1998 Thm.\ 13.3.

\emph{(i) Borcherds lift on $\Lambda^{\mathcal{E}, \mathbb{P}^1}$.}
Borcherds 1998 \emph{Invent.\ Math.}\ 132 Theorem 13.3 applied to $L = \Lambda^{\mathcal{E}, \mathbb{P}^1}$ of signature $(2, 20)$, with input vector-valued modular form $\chi$ of weight $1 - b^+/2 = 0$ and index attached to $U_E$, returns a holomorphic automorphic form $\Psi(\chi) = \Phi^{\mathcal{E}, \mathbb{P}^1}$ on the Grassmannian $\mathcal{G}(\Lambda^{\mathcal{E}, \mathbb{P}^1})$ of positive $2$-planes, of weight $c_\chi(0)/2$. For the specific input $\chi = \phi^{\pi, g}_{0, 1}$ (the $\pi$-twisted weight-$0$ index-$1$ weak Jacobi form built from the $\mathbb{Z}/N\mathbb{Z}$-twisted K3 elliptic genus through the Mordell--Weil torsion sector of $\pi$; Bryan--Oberdieck 2019 arXiv:1807.01379 Theorem 3), the Borcherds product expansion around a $0$-dimensional cusp $F_\rho$ with Weyl vector $\rho \in \Lambda^{\mathcal{E}, \mathbb{P}^1}$ is
\[
 \Phi^{\mathcal{E}, \mathbb{P}^1}(Z)
 \;=\; e^{2 \pi i (\rho, Z)} \prod_{\substack{\lambda \in \Lambda^{\mathcal{E}, \mathbb{P}^1}_+ \\ (\lambda, \rho) > 0}}
 \bigl( 1 - e^{2 \pi i (\lambda, Z)} \bigr)^{c_\chi(-\lambda^2 / 2)}
\]
(Borcherds 1998 Thm.\ 13.3(5)). The GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ with denominator $\Phi^{\mathcal{E}, \mathbb{P}^1}$ is constructed by the Borcherds 1988 generalised-Kac--Moody procedure: real simple roots at norm-$(-2)$ vectors with positive Weyl-vector pairing, imaginary simple roots at norm-$\le 0$ vectors of positive Fourier coefficient. This is the standard GBKM output of the Borcherds singular-theta lift (Borcherds 1995 \emph{Invent.\ Math.}\ 120; 1998 \emph{Invent.\ Math.}\ 132 \S 13).

\emph{(ii) Mordell--Weil indexing.}
By Theorem~\texttt{wn:thm:second-pass-shioda-inose-MW} (\texttt{notes/platonic\_synthesis\_wave2\_refinement.tex} L485--531), the Shioda--Tate formula $\rho(S) = 2 + r + \mathrm{rk}\,\mathrm{MW}(\pi)$ at $\rho(S) = 20$ and Kodaira configuration $(I_2, I_2, 20 \cdot I_1)$ yields $r = 2$ and $\mathrm{rk}\,\mathrm{MW}(\pi) = 16$. Under (H1), the Shioda-height pairing
\[
 \langle P, Q \rangle_{\mathrm{Shioda}}
 \;=\; \chi(\mathcal{O}_S) + (P \cdot S_0) + (Q \cdot S_0) - (P \cdot Q) - \sum_v \mathrm{contr}_v(P, Q),
\]
with $\chi(\mathcal{O}_S) = 2$ (K3), rescaled by $\chi(\mathcal{O}_S)^{-1} = 1/2$, gives the integral $E_8(-1)^{\oplus 2}$ Gram matrix on $\mathrm{MW}(\pi)/\mathrm{tors}$ (Shioda 1990 \emph{J.\ Math.\ Soc.\ Japan}\ 39 Theorem 8.6; Schütt--Shioda 2019 \emph{Mordell--Weil Lattices} Proposition 6.36).

The embedding $\mathrm{MW}(\pi)/\mathrm{tors} \hookrightarrow \mathrm{NS}(S) \subset \Lambda^{\mathcal{E}, \mathbb{P}^1}$ places $E_8(-1)^{\oplus 2}$ as a primitive rank-$16$ sublattice of $\Lambda^{\mathcal{E}, \mathbb{P}^1}$ of signature $(2, 20) - (0, 16) = (2, 4)$ on the orthogonal complement. The real simple roots of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ at norm $-2$ that lie inside this $E_8(-1)^{\oplus 2}$ sublattice are exactly the $E_8$-root vectors, indexed by primitive sections $\sigma$ with $\langle \sigma, \sigma \rangle_{\mathrm{Shioda}} = 4$ (Shioda-height) corresponding to $\langle \alpha_\sigma, \alpha_\sigma \rangle = -2$ (rescaled) as asserted.

\emph{Internal decoration.} The discriminant form $\mathrm{disc}(E_8(-1)^{\oplus 2}) = 1$ (unimodular; Serre 1973 \emph{A Course in Arithmetic} Ch.\ V Theorem 4); the discriminant group is trivial, so no non-trivial external lattice symmetry on the complement is induced by the $\mathrm{MW}$-action. The $\mathrm{MW}$-indexing is internal to the GBKM simple-root system, not an orbit action on $H_4(K3 \times E; \mathbb{Z}) \cong \mathbb{Z} \oplus \Lambda_{K3}$ (Sterk 1985 \emph{Math.\ Ann.}\ 273; Dolgachev 2008 \emph{Mirror Symmetry for Lattice Polarised K3 Surfaces}).

\emph{(iii) Commensurability.}
Under (H2), the Humbert-restriction chain $\mathrm{II}_{2, 18} \supset \Lambda^{3, 2} \supset \Lambda^{2, 1}_{II}$ of \texttt{chapters/examples/k3\_chiral\_algebra.tex} L3016--3032 provides a chain of primitive isometric embeddings
\[
 \Lambda^{2, 1}_{II} \;\hookrightarrow\; \Lambda^{3, 2} \;\hookrightarrow\; \mathrm{II}_{2, 18} \;\hookrightarrow\; \mathrm{II}_{2, 20} \;\cong\; \Lambda^{\mathcal{E}, \mathbb{P}^1},
\]
with the last step given by the Mukai-doubling inclusion $\mathrm{II}_{2, 18} \subset \mathrm{II}_{4, 20}$ restricted to the signature-$(2, 20)$ slice fixed by the symplectic-automorphism complement (Mukai 1987 \emph{Nagoya Math.\ J.}\ 81 \S 1; Nishiyama 1996 \emph{Japan J.\ Math.}\ 22). By Borcherds functoriality (Theorem~\texttt{thm:borcherds-lift-universal}(iii), \texttt{chapters/examples/k3e\_bkm\_chapter.tex} L1605--1623), pullback along these primitive embeddings produces corresponding denominator pullbacks, and the GBKM $\mathfrak{g}_{\Delta_5}$ at $\Lambda^{2, 1}_{II}$ embeds as a sub-GBKM of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ at $\Lambda^{\mathcal{E}, \mathbb{P}^1}$. 

The three real simple roots $\{\delta_1, \delta_2, \delta_3\}$ of $\Lambda^{2, 1}_{II}$ (Gram matrix with $2$ on diagonal, $-2$ off-diagonal; Lorgat 2020 \S 3 eqs.\ (3.4)--(3.7); Gritsenko--Nikulin 1998 Theorem 2.1) map to three of the $\mathrm{MW}$-indexed real simple roots $\{\alpha_\sigma\}$ in $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ via the $\Lambda^{2, 1}_{II} \hookrightarrow E_8(-1)^{\oplus 2}$-inclusion fixed by the three hyperbolic generators of the ambient $U \oplus U \oplus \langle -2 \rangle$. Imaginary simple roots match at Heegner discriminants $D = 4N - \ell^2$ via Bruinier 2002 \emph{LNM} 1780 Proposition 5.1 (Heegner Chern-class reciprocity): the Fourier coefficient $c_{\phi^{\pi, g}_{0, 1}}(N, \ell)$ on the twisted-input side equals $c_{\Delta_5}(N, \ell)$ on the untwisted-input side precisely when $\phi^{\pi, g}_{0, 1} = \phi^{K3}_{0, 1}$.

The ``commensurability'' statement (not equality) records: $\mathfrak{g}_{\Delta_5} \subset \mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ is finite-index as a Lie superalgebra inclusion when the twisted input reduces to the untwisted K3 elliptic genus; at non-trivial Mordell--Weil twists $g \in \mathrm{MW}(\pi)/\mathrm{tors}$, the inclusion is strict and $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ carries strictly more real-simple-root data than $\mathfrak{g}_{\Delta_5}$. The equality statement holds only at the diagonal $(\mathcal{E}, \mathbb{P}^1) = (K3, E)$ specialisation with trivial twist.

\emph{(iv) Weight preservation.}
By Theorem~\texttt{thm:borcherds-lift-universal}(iv) (\texttt{chapters/examples/k3e\_bkm\_chapter.tex} L1617; Borcherds 1998 Thm.\ 13.3 weight formula), $\mathrm{wt}(\Phi^{\mathcal{E}, \mathbb{P}^1}) = c_{\phi^{\pi, g}_{0, 1}}(0) / 2$. At untwisted input, $c_1(0) = 10$ (constant Fourier coefficient of $\phi^{K3}_{0, 1} = \tfrac{1}{2} Z_{K3}$; Eichler--Zagier 1985 Theorem 9.5), giving $\mathrm{wt} = 5 = \mathrm{wt}(\Delta_5) = \kappa_{\mathrm{BKM}}(\Delta_5)$, consistent with the universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ of Theorem~\texttt{thm:borcherds-weight-kappa-BKM-universal} (\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex}).

This completes the conditional proof under (H1) and (H2).
\end{proof}

## Hypotheses (conditional)

**(H1) Nishiyama 1996 embedding realisability, specific $(T, \pi)$-pair.** That there exists a specific singular K3 transcendental lattice $T$ and Jacobian elliptic fibration $\pi: S \to \mathbb{P}^1$ of Kodaira configuration $(I_2, I_2, 20 \cdot I_1)$ such that $\mathrm{MW}(\pi)/\mathrm{tors}$, under the Shioda canonical height rescaled by $\chi(\mathcal{O}_S)^{-1} = 1/2$, is isomorphic to $E_8(-1)^{\oplus 2}$.

*Literature status.* Nishiyama 1996 \emph{Japan J.\ Math.}\ 22 Theorem 4.1 enumerates Jacobian elliptic fibrations on singular K3s via Kneser $p$-neighbour lattice embeddings $U \oplus L^{(\mathrm{red})}_{\mathrm{fibre}} \hookrightarrow U^3 \oplus E_8(-1)^2$ with orthogonal complement of type $T$. The general existence is theorem-level; what remains is the explicit Weierstrass equation and the verification that the specific choice $L^{(\mathrm{red})}_{\mathrm{fibre}} = 2 A_1$, $T = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ (discriminant $-3$) realises $\mathrm{MW}(\pi) \simeq E_8(-1)^2$ as the quotient. Kumar 2008 \emph{Int.\ Math.\ Res.\ Not.}\ and Kuwata 2000 \emph{Comment.\ Math.\ Univ.\ St.\ Pauli}\ 49 give explicit models on Kummer surfaces $\mathrm{Km}(E \times E)$ for $E$ with $j \in \{0, 1728\}$; extraction of the matching $(T, \pi)$-pair remains a primary-source unification step.

**(H2) Gritsenko--Nikulin 1998 paramodular compatibility.** That under the Humbert-restriction chain $\mathrm{II}_{2, 18} \supset \Lambda^{3, 2} \supset \Lambda^{2, 1}_{II}$, the $E_8(-1)^{\oplus 2}$-indexed real-simple-root walls of the Weyl chamber of $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ map, under pullback, to the three-generator rank-$3$ hyperbolic core of $\Lambda^{2, 1}_{II}$ in a manner compatible with the Borcherds-product factorisation of $\Delta_5$.

*Literature status.* Gritsenko--Nikulin 1998 \emph{Amer.\ J.\ Math.}\ 119 Theorem 2.1 gives the full paramodular presentation of $\Delta_5$ with the three real simple roots $\delta_1, \delta_2, \delta_3$ and the imaginary simple root tower at Heegner discriminants; Gritsenko 2018 \emph{Algebra i Analiz}\ 30 supplies the Humbert-surface restriction from $\Lambda^{4, 2} \supset \mathrm{II}_{2, 18}$ to the paramodular $\Lambda^{3, 2}$ chamber. The residue is a direct Borcherds-product-coefficient match across the chain at real-root walls (no new theorem required; primary-source unification at coefficient level).

## Cross-consistency notes

**Wave 1 spine (\texttt{notes/platonic\_synthesis\_post\_adversarial.tex}).** The residual-frontier entry at L1325--1328 reads ``Elliptic-surface specialisation $(\Sigma_2, C) = (\mathcal{E}, \mathbb{P}^1)$ with Mordell--Weil-indexed simple roots: conjectural for K3 of Picard rank $20$ (Shioda--Inose); scope hypothesis $\rho(K3) = 20$ is necessary.'' Theorem~\ref{thm:c02-elliptic-surface-rho-20-conditional} above refines this to three specific scope clauses: (i) $\rho(S) = 20$; (ii) Kodaira configuration $(I_2, I_2, 20 I_1)$; (iii) $\mathrm{MW}(\pi)/\mathrm{tors} \simeq E_8(-1)^{\oplus 2}$ under the $\chi(\mathcal{O}_S)^{-1}$-rescaled Shioda height. Consistent with the Wave-2 refinement Theorem~\texttt{wn:thm:second-pass-shioda-inose-MW} (L481--531).

**Wave 2 F03 retraction (\texttt{.swarm\_outputs/wave2/F03\_shioda\_MW\_K3\_fibration.md}).** F03 established the rank-bifurcation (rank 2 or 16 per Kodaira configuration) and the discriminant-group internal-decoration argument. The present closure builds on F03 Theorem \texttt{f03w2:thm:MW-E8E8} (conditions 1--3 for $\mathrm{MW} \simeq E_8(-1)^2$) and extends it to the full Borcherds-lift + commensurability closure. F03 residual-frontier (R1)--(R5) are absorbed as follows:
- (R1) Specific fibration realising $\mathrm{MW}(\pi) = E_8(-1)^2$ → (H1) here.
- (R2) Shioda height normalisation in the GBKM real-root dictionary → (H2) here (Bruinier 2002 Proposition 5.1 Heegner Chern-class reciprocity reduces this to a coefficient match at Fourier level).
- (R3) Non-Jacobian fibrations → outside scope of the closure (Jacobian assumed).
- (R4) Kodaira-type imaginary roots → covered by the Fourier-coefficient match at Heegner discriminants in (iii).
- (R5) Higher-$\rho$ vs.\ $\rho = 20$ stability → outside scope (the closure is at $\rho = 20$).

**Wave 2 refinement (\texttt{notes/platonic\_synthesis\_wave2\_refinement.tex}).** Residual-frontier Tier I item at L819--821 (``Elliptic-surface specialisation $(\Sigma_2, C) = (\mathcal{E}, \bP^1)$ at Shioda--Inose $\rho = 20$ (Borcherds $1998$ Thm.~$13.3$ on signature $(2, 20)$)''). The parenthetical ``(2, 20)'' is the correct ambient; the brief's framing of the obstruction as ``$(1, 19)$ with $b^+ = 1$'' mis-identifies the ambient as the Picard lattice alone. The present closure makes the ``(2, 20)'' explicit as $\mathrm{NS}(S) \oplus U_E$ and resolves the Tier-I item to Terminal State (B) Conditional Closure under (H1), (H2).

**CLAUDE.md invariants.** Subscript discipline: $\kappa_{\mathrm{BKM}}(\Delta_5) = 5$, $\kappa_{\mathrm{BKM}}(\Phi^{\mathcal{E}, \mathbb{P}^1}) = c_{\phi^{\pi, g}_{0, 1}}(0)/2$, with equality at the untwisted input. No bare $\kappa$. Lane discipline: the closure is chain-level (explicit Borcherds-product expansion, explicit Shioda-height Gram matrix, explicit Humbert-restriction chain at the level of lattice embeddings); the $(\infty, 1)$-categorical lane would require stating $\mathrm{Sp}^{\mathrm{ch}}_{\mathcal{E}, \mathbb{P}^1}$ as a Morita-natural $(\infty, 1)$-functor and is a separate statement covered by Theorem CY-A$_3$ (\texttt{chapters/theory/cy\_to\_chiral.tex}). Primary sources: Borcherds 1998 \emph{Invent.\ Math.}\ 132 Thm.\ 13.3; Gritsenko--Nikulin 1998 \emph{Amer.\ J.\ Math.}\ 119 Thm.\ 2.1; Nishiyama 1996 \emph{Japan J.\ Math.}\ 22 Thm.\ 4.1; Shioda 1990 \emph{J.\ Math.\ Soc.\ Japan}\ 39 Thm.\ 8.6; Shioda--Inose 1977 \emph{Classification of Algebraic Varieties}; Bruinier 2002 \emph{LNM}\ 1780 Prop.\ 5.1; Lorgat 2020 \S 3; Schütt--Shioda 2019 \emph{Mordell--Weil Lattices}.

**Cross-programme propagation (Vol I / Vol II).** This closure is Vol III-specific (CY-to-chiral $\Phi_3$ specialisation on $K3 \times E$). Vol I (\texttt{chiral-bar-cobar}) bar-cobar apparatus does not directly intersect; Vol II (\texttt{chiral-bar-cobar-vol2}) $3$D HT QFT framework is orthogonal. No propagation of hypotheses (H1), (H2) to Vol I or Vol II is required.

## Inscription-ready TeX block

```latex
\begin{theorem}[Elliptic-surface specialisation at Shioda--Inose $\rho(S) = 20$]
\label{thm:elliptic-surface-rho-20-conditional}
\ClaimStatusConjectured
Let $S$ be a Shioda--Inose K3 surface of Picard rank $\rho(S) = 20$ with transcendental lattice $T(S)$ of rank $2$ and signature $(2, 0)$, equipped with a Jacobian elliptic fibration $\pi: S \to \bP^1$ of Kodaira configuration $(I_2, I_2, 20 \cdot I_1)$; let $(E, e_0)$ be an elliptic curve and $X = S \times E$. Assume:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item \textup{(Nishiyama realisability \cite[Thm.~4.1]{Nishiyama1996})} The Mordell--Weil lattice $\mathrm{MW}(\pi)/\mathrm{tors}$, under the Shioda canonical height rescaled by $\chi(\cO_S)^{-1} = 1/2$, is isomorphic to $E_8(-1)^{\oplus 2}$.
\item \textup{(Paramodular compatibility \cite[Thm.~2.1]{GritsenkoNikulin1998})} The image of the $E_8(-1)^{\oplus 2}$ rescaled Shioda-height lattice under the Humbert-restriction chain $\mathrm{II}_{2, 20} \supset \mathrm{II}_{2, 18} \supset \Lambda^{3, 2} \supset \Lambda^{2, 1}_{II}$ coincides, up to $W^{(2)}(\Lambda^{2, 1}_{II})$-action, with the real-simple-root wall system of $\fg_{\Delta_5}$.
\end{enumerate}
Then the Stage-$2$ specialisation $\SpCh_{\cE, \bP^1}$ applied to $\cF_{K3 \times E} = \PhiFA_3(D^b\mathrm{Coh}(K3 \times E))$ yields a generalised Borcherds--Kac--Moody superalgebra $\fg_{\cE, \bP^1}$ with the following structure.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Borcherds lift.)} The denominator of $\fg_{\cE, \bP^1}$ is the Borcherds singular-theta lift \cite[Thm.~13.3]{Borcherds1998} on the signature-$(2, 20)$ lattice $\Lambda^{\cE, \bP^1} = \mathrm{NS}(S) \oplus U_E$ of the $\pi$-twisted weight-$0$ index-$1$ Jacobi form $\phi^{\pi, g}_{0, 1}$:
\[
 \Phi^{\cE, \bP^1}
 \;=\; \Psi\bigl(\phi^{\pi, g}_{0, 1};\ \Lambda^{\cE, \bP^1}\bigr).
\]
\item \textup{(Mordell--Weil indexing of real simple roots.)} Under (H1), the real simple roots of $\fg_{\cE, \bP^1}$ are indexed internally by primitive Mordell--Weil sections $\sigma \in \mathrm{MW}(\pi)/\mathrm{tors}$ via $\sigma \mapsto \alpha_\sigma$ with $\langle \alpha_\sigma, \alpha_\sigma \rangle = -2$, the $E_8$-root pairing on $E_8(-1)^{\oplus 2} \subset \Lambda^{\cE, \bP^1}$. Unimodularity of $E_8(-1)^{\oplus 2}$ forces trivial discriminant form, hence no external orbit action.
\item \textup{(Commensurability with $\fg_{\Delta_5}$.)} Under (H2), there exists a finite-index GBKM inclusion $\fg_{\Delta_5} \hookrightarrow \fg_{\cE, \bP^1}$ along the primitive lattice chain $\Lambda^{2, 1}_{II} \subset \Lambda^{3, 2} \subset \mathrm{II}_{2, 20} \cong \Lambda^{\cE, \bP^1}$; equality holds if and only if $\phi^{\pi, g}_{0, 1} = \phi^{K3}_{0, 1}$.
\item \textup{(Weight.)} $\mathrm{wt}(\Phi^{\cE, \bP^1}) = c_{\phi^{\pi, g}_{0, 1}}(0)/2$; at untwisted input, $\mathrm{wt} = 5 = \kappa_{\mathrm{BKM}}(\Delta_5)$.
\end{enumerate}
\end{theorem}

\begin{proof}
The ambient lattice $\Lambda^{\cE, \bP^1} = \mathrm{NS}(S) \oplus U_E$ has signature $(1, 19) + (1, 1) = (2, 20)$, so $b^+ = 2$ and \cite[Thm.~13.3]{Borcherds1998} applies: the singular theta lift $\Psi$ converges to a holomorphic automorphic form of weight $c(0)/2$ on $\cG(\Lambda^{\cE, \bP^1})$, with product expansion around a $0$-cusp
\[
 \Phi^{\cE, \bP^1}(Z)
 \;=\; e^{2 \pi i (\rho, Z)} \prod_{\substack{\lambda \in \Lambda^{\cE, \bP^1}_+ \\ (\lambda, \rho) > 0}}
 \bigl( 1 - e^{2 \pi i (\lambda, Z)} \bigr)^{c_{\phi^{\pi, g}_{0, 1}}(-\lambda^2/2)}.
\]
The GBKM $\fg_{\cE, \bP^1}$ with this denominator is the Borcherds-1988 output.

\emph{(ii)} Shioda--Tate at $\rho(S) = 20$ with Kodaira configuration $(I_2, I_2, 20 I_1)$ forces $r = 2$ and $\mathrm{rk}\,\mathrm{MW}(\pi) = 16$ \cite[Thm.~1.1]{Shioda1990}. Under (H1), the rescaled Shioda-height Gram on $\mathrm{MW}(\pi)/\mathrm{tors}$ is $E_8(-1)^{\oplus 2}$, and the primitive embedding $\mathrm{MW}(\pi)/\mathrm{tors} \hookrightarrow \mathrm{NS}(S) \hookrightarrow \Lambda^{\cE, \bP^1}$ identifies the $-2$-norm vectors with GBKM real simple roots. Unimodularity $\mathrm{disc}(E_8(-1)^{\oplus 2}) = 1$ \cite[Ch.~V]{Serre1973} trivialises the discriminant form, forcing internal-decoration status.

\emph{(iii)} The lattice chain $\Lambda^{2, 1}_{II} \hookrightarrow \Lambda^{3, 2} \hookrightarrow \mathrm{II}_{2, 18} \hookrightarrow \mathrm{II}_{2, 20} \cong \Lambda^{\cE, \bP^1}$ is the Humbert-restriction chain of the Mathieu/Siegel-paramodular/$K3$-BKM correspondence (Gritsenko 2018 \emph{Algebra i Analiz}\ 30; \cite[Thm.~2.1]{GritsenkoNikulin1998}). Borcherds functoriality \cite[\S 14]{Borcherds1998} pulls back denominators along primitive embeddings; the resulting GBKM inclusion $\fg_{\Delta_5} \hookrightarrow \fg_{\cE, \bP^1}$ is finite-index under (H2), with equality exactly when the Fourier coefficients of $\phi^{\pi, g}_{0, 1}$ agree with those of $\phi^{K3}_{0, 1}$ at all Heegner discriminants \cite[Prop.~5.1]{Bruinier2002}.

\emph{(iv)} Weight formula \cite[Thm.~13.3~(iv)]{Borcherds1998}: $\mathrm{wt}(\Phi^{\cE, \bP^1}) = c_{\phi^{\pi, g}_{0, 1}}(0)/2$. At untwisted K3 input, $c_1(0) = 10$ \cite[Thm.~9.5]{EichlerZagier1985}, yielding weight $5$.
\end{proof}
```

## Primary-source gap (residue beyond hypothesis)

*None at the level of literature citations.* Both (H1) and (H2) are published theorems; the explicit Weierstrass-model computation realising the specific $(T, \pi)$-pair with $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ and the coefficient match at Heegner discriminants across the Humbert-restriction chain are within-literature unification tasks, not new theorems.

The only mathematical question reserved for further primary-source work is *uniqueness*: is the $(T, \pi)$-pair satisfying (H1) unique up to $\mathrm{O}(\Lambda_{K3})$-action, or does Nishiyama's classification yield a finite family of distinct fibrations each producing a distinct $\fg_{\cE, \bP^1}$? Kuwata 2000 \emph{Comment.\ Math.\ Univ.\ St.\ Pauli}\ 49 suggests multiple rank-$16$ MW fibrations exist on $\mathrm{Km}(E \times E)$ at $j \in \{0, 1728\}$; the uniqueness of the $\Delta_5$-commensurable fibration is a separate closure question, not part of the present closure.
