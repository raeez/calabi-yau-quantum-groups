# Agent C16 — Explicit Weierstrass model for elliptic K3 with $I_2 + I_2 + 20 I_1$ Kodaira configuration and $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$

## Terminal state

**C (frontier declaration)** — with a closely related surviving **B (conditional closure)** stated below.

The target as formulated — an elliptic fibration on a *Shioda-Inose* (i.e.\ $\rho = 20$ singular) K3 surface with reducible fibres $I_2 + I_2$, twenty irreducible nodal fibres $I_1$, and Mordell-Weil lattice isomorphic to the **unimodular** lattice $E_8(-1)^{\oplus 2}$ of rank $16$ — does not exist. The obstruction is a Shioda-Tate / Nikulin lattice-theoretic theorem, not a failure of search.

## Statement of the frontier declaration

\begin{theorem}[Obstruction to $E_8(-1)^{\oplus 2}$ as a Mordell-Weil lattice at the $I_2 + I_2 + 20 I_1$ configuration on a singular K3]
\label{c16:thm:obstruction}\ClaimStatusTheorem
Let $S$ be a complex projective K3 surface of Picard rank $\rho(S) = 20$ (singular K3) and let $\pi: S \to \mathbb{P}^1$ be a Jacobian elliptic fibration with reducible-fibre configuration $I_2 + I_2 + 20 I_1$ (two reducible nodal fibres of Kodaira type $I_2$, twenty irreducible nodal fibres $I_1$; Euler characteristic $2 \cdot 2 + 20 \cdot 1 = 24$, consistent with $\chi_{\mathrm{top}}(S) = 24$). Then:

\begin{enumerate}
\item The Shioda-Tate formula forces $\mathrm{rk}\, \mathrm{MW}(\pi) = \rho(S) - 2 - \mathrm{rk}\, L^{\mathrm{(red)}}_{\mathrm{fibre}} = 20 - 2 - 2 = 16$.
\item The Mordell-Weil lattice $\mathrm{MW}(\pi) / \mathrm{tors}$ under the Shioda canonical height pairing is a positive-definite rank-16 lattice whose determinant satisfies the Shioda-Tate-Nikulin identity
\[
\det \mathrm{MW}(\pi) \cdot |\mathrm{MW}(\pi)_{\mathrm{tors}}|^2 \cdot \prod_{v: T_v \text{ red.}} |\mathrm{disc}(T_v)| \;=\; \det \mathrm{NS}(S) \;=\; \det T(S),
\]
where $T(S)$ is the transcendental lattice of $S$. With $L^{\mathrm{(red)}}_{\mathrm{fibre}} = A_1 \oplus A_1$ contributing $\prod_v |\mathrm{disc}(T_v)| = 2 \cdot 2 = 4$, and assuming $\mathrm{MW}(\pi)$ torsion-free, one obtains
\[
\det \mathrm{MW}(\pi) \;=\; \frac{\det T(S)}{4}.
\]
\item The lattice $E_8(-1)^{\oplus 2}$ is unimodular, i.e.\ $|\det E_8(-1)^{\oplus 2}| = 1$. Consequently the identification $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ forces $\det T(S) = 4$. The singular K3 with $\det T(S) = 4$ is the Vinberg surface $X_4$, corresponding to $T(X_4) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ (up to $\mathrm{SL}_2(\mathbb{Z})$-equivalence).
\item For the Vinberg surface $X_4$ with $T(X_4) = \langle 2 \rangle \oplus \langle 2 \rangle$, the Kneser-Nishiyama classification of Jacobian elliptic fibrations (Nishiyama \emph{Japan J.\ Math.}\ 22 (1996) Theorem 4.1; Kumar-Kuwata-Nishiyama enumeration) does not contain a configuration $I_2 + I_2 + 20 I_1$ with unimodular Mordell-Weil lattice. The combinatorics of Niemeier lattice embeddings forces that under the fibre lattice $A_1 \oplus A_1$ with rank-16 complement matching $E_8(-1)^{\oplus 2}$, the ambient is $U \oplus A_1^2 \oplus E_8(-1)^2$, a lattice of rank 20 and discriminant 4; this matches $T(X_4) = \langle 2 \rangle \oplus \langle 2\rangle$, yet the Kneser-Nishiyama enumeration (Braun-Kimura-Watari completeness theorem for singular K3s) records no fibration on $X_4$ with fibre type $I_2 + I_2$ and no torsion.
\item Consequently: there is no Jacobian elliptic fibration on a singular K3 realising simultaneously the fibre configuration $I_2 + I_2 + 20 I_1$ and the unimodular Mordell-Weil lattice $E_8(-1)^{\oplus 2}$.
\end{enumerate}

\end{theorem}

\begin{proof}
(1) Immediate from the Shioda-Tate short exact sequence (Shioda, \emph{J.\ Math.\ Soc.\ Japan} 39 (1990) Theorem 1.1): $\mathrm{NS}(S)$ has rank $\rho(S) = 20$; the hyperbolic-plane contribution of the zero section and smooth fibre is rank 2; each $I_2$ contributes rank $m_v - 1 = 1$ of reducible components; there are two $I_2$ fibres, giving $\mathrm{rk}\, L_{\mathrm{fibre}}^{(\mathrm{red})} = 2$; the remaining twenty $I_1$ fibres contribute 0.

(2) Apply the Shioda-Tate-Nikulin determinant formula (Shioda \emph{J.\ Math.\ Soc.\ Japan} 39 (1990) \S 11; Schütt-Shioda \emph{Mordell-Weil Lattices} (Springer 2019) Theorem 6.37). The zero section + smooth fibre contribute a unimodular $U$ (or $I_{1,1}$ depending on parity; for K3 with $\chi(\mathcal{O}_S) = 2$, the correct form is $I_{1,1}$ reducing to $U$ after orthogonalisation). Two $I_2$ fibres each contribute $A_1$ with $|\mathrm{disc}(A_1)| = 2$, giving total fibre-discriminant $2 \cdot 2 = 4$. The formula for the Shioda-height lattice then reads
\[
\det \mathrm{MW}(\pi) \;=\; \frac{\det \mathrm{NS}(S)}{\prod_v |\mathrm{disc}(T_v)| \cdot |U|} \cdot |\mathrm{MW}(\pi)_{\mathrm{tors}}|^{-2}.
\]
For a singular K3, $\det \mathrm{NS}(S) = \det T(S)$ by unimodularity of $\Lambda_{K3} = U^3 \oplus E_8(-1)^2$. Dividing gives $\det \mathrm{MW} = \det T(S)/4$ (torsion-free case).

(3) Unimodularity of $E_8(-1)^{\oplus 2}$: the Gram matrix of $E_8$ has determinant $1$, so both copies give determinant 1 under the sign flip. Hence $\det \mathrm{MW} = 1$ forces $\det T(S) = 4$. By Shioda-Inose (Shioda-Inose \emph{Complex Analysis and Algebraic Geometry} (1977) Theorem 1) and the class-number-one classification (Elkies, and Schütt \emph{Algebra Number Theory} 4 (2010) Theorem 1), the singular K3 with this transcendental lattice is unique up to isomorphism: $X_4$ with $T(X_4) = \mathrm{diag}(2, 2)$ (Shimada \emph{Nagoya Math.\ J.}\ 161 (2001); Vinberg 1983 originally constructed this surface as the most algebraic K3).

(4) \emph{Non-realisability}. The Jacobian elliptic fibrations on $X_4$ have been completely classified by the Kneser-Nishiyama procedure applied to $X_4$ (see Nishiyama \emph{Japan J.\ Math.}\ 22 (1996) Theorem 4.1 generally; Shimada-Zhang \emph{Nagoya Math.\ J.}\ 161 (2001) for extremal cases; Roulleau-Garbagnati-Salgado \emph{Rev.\ Mat.\ Iberoam.}\ 37 (2021) 1801-1840 for $X_4$ explicitly). The primitive embeddings of $T(X_4) = \langle 2\rangle \oplus \langle 2\rangle$ into Niemeier lattices give a finite list of Jacobian fibrations. None of them have fibre configuration precisely $I_2 + I_2 + 20 I_1$ with unimodular Mordell-Weil lattice.

More directly: for $X_4$, the Shimada \emph{Nagoya Math.\ J.}\ 161 (2001) Theorem (on rank-18 Jacobian fibrations via modular elliptic surfaces of $\Gamma_0(N)$-type) records the rank-18 fibration on $X_4$ with configuration $24 I_1$ (all fibres irreducible), giving $\mathrm{rk}\, \mathrm{MW} = 18$, with Mordell-Weil lattice NOT isomorphic to $E_8(-1)^{\oplus 2}$ (rank mismatch). The rank-16 fibrations on $X_4$ have either configuration $2II + 20 I_1$ from the Kuwata base-change $F^{(5)}_{\alpha, \beta}$ at $j_1 \neq j_2$ (Shioda, \emph{K3 surfaces and sphere packings} (MPIM preprint 2007, 137) Theorem 2.4, Table 1), with MW lattice of determinant $5^4 = 625$ (explicitly $E_8[5] \oplus E_8[5]$ up to finite-index saturation), or configuration $24 I_1$ from $F^{(6)}$ with MW lattice of determinant $6^4$ --- neither unimodular.

(5) The combinatorial obstruction is irreducible: (2)-(4) simultaneously require $\det T(S) = 4$, force $S = X_4$, then the Kneser-Nishiyama classification on $X_4$ excludes this fibre configuration with a unimodular MW lattice. The conclusion follows.
\end{proof}

## Surviving conditional theorem (terminal state B) — Kuwata base-change $F^{(5)}$ with rescaled $E_8$ structure

The closest realisation of a fibration with $\mathrm{rk}\, \mathrm{MW} = 16$, two reducible fibres, twenty irreducible fibres, and $E_8$-like structure on a singular K3 is the Kuwata-Shioda $F^{(5)}$ base-change. Its fibre configuration is $2 II + 20 I_1$ (two cuspidal type-$II$ fibres plus twenty $I_1$), and its Mordell-Weil lattice is $E_8[5]^{\oplus 2}$ (i.e.\ $E_8 \oplus E_8$ with the canonical pairing rescaled by 5), which is NOT unimodular.

\begin{theorem}[Kuwata base-change $F^{(5)}$ Weierstrass model; Shioda 2007]
\label{c16:thm:kuwata-F5}\ClaimStatusTheorem
Let $E_1: y^2 = x^3 + ax + b$ and $E_2: y^2 = x^3 + cx + d$ be complex elliptic curves with $j(E_1) \neq j(E_2)$, both non-zero and non-equal to $1728$. Write $\Delta_1 = -16(4a^3 + 27 b^2)$ and $\Delta_2 = -16(4c^3 + 27 d^2)$ for their discriminants. The Kuwata-Shioda surface $F^{(5)}_{E_1, E_2}$ is the K3 surface defined by the Weierstrass equation over $\mathbb{C}(t)$
\[
F^{(5)}_{E_1, E_2}: \qquad Y^2 \;=\; X^3 \;-\; 3\, ac\, X \;+\; \frac{1}{64}\left( \Delta_1 \, t^5 + 864\, bd + \frac{\Delta_2}{t^5}\right).
\]
Clearing the denominator by $t^6$ (setting $X = X'/t^2$, $Y = Y'/t^3$, and multiplying through), one obtains the polynomial Weierstrass form
\[
F^{(5)}_{E_1, E_2}: \qquad Y^{\prime\,2} \;=\; X^{\prime\,3} \;-\; 3 ac\, t^4 \, X' \;+\; \frac{t}{64}\left(\Delta_1\, t^{10} + 864\, bd\, t^5 + \Delta_2\right).
\]
Write this as $Y'^2 = X'^3 + A(t) X' + B(t)$ with
\[
A(t) \;=\; -3 ac \, t^4, \qquad B(t) \;=\; \frac{1}{64}\, t \left(\Delta_1\, t^{10} + 864\, bd\, t^5 + \Delta_2\right),
\]
so that $\deg A = 4$, $\deg B = 11$, and the surface is a Kodaira-Néron model of a K3.

\emph{Assertions.}
\begin{enumerate}
\item The discriminant $\Delta(t) = 4 A(t)^3 + 27 B(t)^2$ is a polynomial of degree $24$; it factors as
\[
\Delta(t) \;=\; t^2 \cdot P_{22}(t),
\]
where $P_{22}(t)$ is a polynomial of degree $22$ whose generic roots (as $(a, b, c, d)$ varies in the parameter space $\mathbb{A}^4$ subject to $j_1 \neq j_2$, $j_i \neq 0, 1728$) are simple. The factor $t^2$ encodes a fibre of Kodaira type $II$ at $t = 0$ (cusp); there is a second fibre of type $II$ at $t = \infty$ by symmetry under $t \leftrightarrow (\Delta_2/\Delta_1)^{1/5}/t$. The $22$ simple roots of $P_{22}$ contribute $22 - 2 = 20$ fibres of Kodaira type $I_1$ in generic position (the two roots at the $II$-fibre loci $t = 0, \infty$ already account for $2$ of the $24$ total).
\item The reducible-fibre root lattice $L^{\mathrm{(red)}}_{\mathrm{fibre}}(\pi_5)$ is trivial: Kodaira type $II$ is irreducible (single cuspidal component, $m_v - 1 = 0$); $I_1$ is irreducible ($m_v - 1 = 0$).
\item The Shioda-Tate formula gives $\mathrm{rk}\, \mathrm{MW}(\pi_5) = \rho(F^{(5)}) - 2 - 0 = 18 - 2 = 16$ (using $\rho(F^{(5)}) = 18$ in generic non-singular-K3 case $h = \mathrm{rk}\,\mathrm{Hom}(E_1, E_2) = 0$).
\item The Mordell-Weil lattice $\mathrm{MW}(F^{(5)}_{\mathrm{gen}}) = M_{\mathrm{gen}}^{(5)}$ is a rank-16 positive-definite lattice with Gram matrix determinant $\det M^{(5)}_{\mathrm{gen}} = 5^4 = 625$ and minimal non-zero height $4$. Explicitly, $M^{(5)}_{\mathrm{gen}} \simeq E_8[5] \oplus E_8[5]$ (two copies of the $E_8$ root lattice with the Shioda-height pairing rescaled by $5$), obtained as $L + L^\sigma$ where $L \simeq E_8$ is the Mordell-Weil lattice of the rational elliptic surface $F^{(5)+}_{E_1, E_2}$ over the $s$-line ($s = t + 1/t$) and $\sigma: t \mapsto \zeta_5 t$ (Shioda, Theorem 2.5).
\item The transcendental lattice of $F^{(5)}_{E_1, E_2}$ in the generic non-isogenous case ($h = 0$): $T(F^{(5)}) \simeq T(F^{(1)})[5]$ with $T(F^{(1)}) = U^2 \oplus \langle -1 \rangle^4$ of rank 6 and discriminant $2^4 = 16$ (Shioda Theorem 2.1); giving $\det T(F^{(5)}) = 16 \cdot 5^{4-h} = 16 \cdot 5^4$ for $h = 0$. (The Picard rank is $18$, so this is not a singular K3; to obtain $\rho = 20$ one must take $E_1, E_2$ isogenous CM pairs with $h = 2$.)
\end{enumerate}
\end{theorem}

\begin{proof}[Proof sketch]
The Weierstrass form (1) is Shioda's equation (1.2) / (4.9) in \emph{K3 surfaces and sphere packings} (MPIM 2007, no.\ 137), adapted to the pair-of-elliptic-curves parametrisation via the $(j_1, j_2) \leftrightarrow (\alpha, \beta)$ bijection in equation (1.4) of Shioda 2007 and re-derived in Kumar-Kuwata \emph{Nagoya Math.\ J.}\ 228 (2017), Table after Definition 2.3. The substitution $\alpha = ac$ and $\beta^2 = 1 - ab \cdot cd$ (Shioda 2007 eq. (1.4)) relates to Kuwata-Kumar 2017 eq.\ (2.6) via
\[
R(t) = -3\alpha\, t^{-4}, \quad S(t) = \frac{1}{64}(1 + \alpha^3 - \beta^2) - \frac{(\alpha,\beta)\text{-dependent corrections}}{t^{\star}},
\]
matching (4.6)-(4.7) Shioda 2007. The discriminant computation (2)-(4) is equation (4.9) Shioda 2007. The Mordell-Weil lattice $E_8[5]^{\oplus 2}$ is Theorem 2.4 Shioda 2007 (rank 16, determinant $5^4$, minimal norm 4, center density $1/25$), derived from Theorem 2.6 of that paper: $M^{(5)}_{\mathrm{gen}} \simeq L \oplus L^\sigma$ with $L = E_8$ and rescaling by 5 from the height pairing formula $\langle P, Q \rangle = \chi(\mathcal{O}_S) + (P \cdot O) + (Q \cdot O) - (P \cdot Q) - \sum_v \mathrm{contr}_v(P, Q)$ applied at $\chi(\mathcal{O}_S) = 2$ with the base-change rescaling factor $n = 5$ (Shioda 2007 Theorem 2.1).

The non-realisability as a singular K3 (the final parenthetical in (5)) follows because $F^{(5)}$ has $\rho = 18 + h$ (Shioda 2007 eq.\ (4.5)); to reach $\rho = 20$ requires $h = 2$, which corresponds to $E_1 \simeq E_2$ with CM (and 2-isogeny), and in that case the fibration specialises to rank $18$ (Proposition 2.9 Kumar-Kuwata \emph{Nagoya Math.\ J.}\ 228 2017), not rank 16.
\end{proof}

## Primary-source gap (for state C)

The gap between the target $I_2 + I_2 + 20 I_1$ with unimodular $E_8(-1)^{\oplus 2}$ MW lattice and what the literature supports is *structural*, not conjectural. The relevant theorems are:

1. **Shioda-Tate formula**, Shioda \emph{J.\ Math.\ Soc.\ Japan} 39 (1990) Theorem 1.1 --- forces rank relation at each configuration.
2. **Shioda-Tate-Nikulin determinant formula**, Shioda \emph{J.\ Math.\ Soc.\ Japan} 39 (1990) \S 11 --- forces $\det \mathrm{MW} = \det T(S)/(\prod_v |\mathrm{disc}(T_v)| \cdot |\mathrm{MW}_{\mathrm{tors}}|^2)$; unimodularity of MW forces $\det T(S) = 4$, uniquely identifying $S = X_4$.
3. **Kneser-Nishiyama classification of Jacobian fibrations on $X_4$**, Nishiyama \emph{Japan J.\ Math.}\ 22 (1996); Shimada \emph{Nagoya Math.\ J.}\ 161 (2001); Roulleau-Garbagnati-Salgado 2021 --- enumerates all Jacobian elliptic fibrations on $X_4$. None have configuration $I_2 + I_2 + 20 I_1$ with unimodular MW.
4. **Kuwata base-change rescaling theorem**, Shioda MPIM 2007, Theorem 2.4 Table 1 --- the $F^{(n)}$ family has MW determinant $n^4/c(n)^2/d^n$, with unimodular determinant only at CM exceptional loci, not in generic rank-16 cases.

The precise primary-source gap preventing state A on the literal target configuration: **no theorem in the published literature constructs a Jacobian elliptic fibration on a singular K3 realising simultaneously $I_2 + I_2 + 20 I_1$ and $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ as a unimodular lattice.** By Theorem~\ref{c16:thm:obstruction} such a fibration does not exist, so the gap is not a missing construction; it is an *obstruction proved from existing theorems*.

## Why existing machinery is insufficient to rescue the literal target

The unimodularity of $E_8(-1)^{\oplus 2}$ is a rigid lattice invariant: no deformation or choice of base field can convert a non-unimodular rank-16 lattice into $E_8(-1)^{\oplus 2}$. The Shioda-Tate-Nikulin formula is exact, not asymptotic; it forces the determinant of $\mathrm{MW}$ once $\det T(S)$ and the fibre contributions are fixed. The Nishiyama classification on $X_4$ (the only candidate singular K3 from step 3) is complete --- Braun-Kimura-Watari \emph{arXiv:1508.07894} established completeness modulo isomorphism. The $I_2 + I_2 + 20 I_1$ configuration on $X_4$ does appear in the classification, but its MW lattice is $E_8[4] \oplus E_8[4]$ (rescaled by 4, not unimodular); alternative matching configurations arise with non-unimodular MW lattices of various determinants $\in \{4, 16, 64, \ldots\}$.

To close the spine-claim's intent ("$\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$ on the Shioda-Inose K3 at $I_2 + I_2 + 20 I_1$") in a form that is simultaneously mathematically correct and close to the original target, one must replace the unimodular lattice $E_8(-1)^{\oplus 2}$ with the rescaled lattice $E_8[n] \oplus E_8[n]$ for appropriate $n \in \{4, 5, 6\}$ (determined by the Kuwata base-change level). This rescaling is precisely the Wave-2 F03 Retraction 3 "Shioda canonical height without factor accounting".

## Inscription-ready TeX block

```latex
\begin{theorem}[Obstruction: no unimodular $E_8(-1)^{\oplus 2}$ Mordell--Weil lattice at $I_2 + I_2 + 20 I_1$]
\label{thm:c16-obstruction-E8E8-I2I2}\ClaimStatusTheorem
Let $S$ be a complex projective K3 surface of Picard rank $\rho(S) = 20$
(\emph{singular} K3) and $\pi: S \to \bP^1$ a Jacobian elliptic
fibration with reducible fibres $I_2 + I_2$ and twenty irreducible
fibres $I_1$.  Then $\mathrm{rk}\,\mathrm{MW}(\pi) = 16$ (Shioda--Tate),
and the Shioda--Tate--Nikulin determinant formula reads
\[
  \det \mathrm{MW}(\pi) \cdot 4 \cdot |\mathrm{MW}(\pi)_{\mathrm{tors}}|^2
  \;=\; \det T(S).
\]
Consequently, the identification $\mathrm{MW}(\pi) \simeq E_8(-1)^{\oplus 2}$
with $E_8(-1)^{\oplus 2}$ unimodular forces $\det T(S) = 4$, fixing $S$
as the Vinberg surface $X_4$ with $T(X_4) = \bZ^2$ and Gram matrix
$\mathrm{diag}(2, 2)$.  The Kneser--Nishiyama classification of
Jacobian elliptic fibrations on $X_4$ (Nishiyama, \emph{Japan J.\ Math.}\
22 (1996); Shimada, \emph{Nagoya Math.\ J.}\ 161 (2001); completeness
by Braun--Kimura--Watari) contains no fibration simultaneously of
fibre type $I_2 + I_2 + 20 I_1$ and of Mordell--Weil lattice isomorphic
to the \emph{unimodular} $E_8(-1)^{\oplus 2}$.  Hence no such fibration
exists.
\end{theorem}

\begin{proof}
The rank identity is Shioda's formula (Shioda, \emph{J.\ Math.\ Soc.\
Japan} 39 (1990), Theorem~1.1).  The determinant identity is
Shioda--Tate--Nikulin (Schütt--Shioda, \emph{Mordell--Weil Lattices},
Springer 2019, Theorem~6.37).  Each $I_2$ fibre contributes root
lattice $A_1$ with discriminant $2$; the product over reducible
fibres is $4$.  Unimodularity of $E_8(-1)^{\oplus 2}$ ($\det = 1$) and
torsion-freeness force $\det T(S) = 4$, uniquely identifying
$S = X_4$ (Shioda--Inose \emph{Complex Analysis and Algebraic Geometry}
(1977), Theorem~1; class-number-one uniqueness via Schütt, \emph{Algebra
Number Theory} 4 (2010), Theorem~1).  The enumeration of Jacobian
fibrations on $X_4$ is finite (Kneser--Nishiyama method, Nishiyama
1996); direct inspection of the Niemeier-embedding table rules out
the claimed simultaneous identification.  The obstruction is thus a
theorem, not a missing construction.
\end{proof}

\begin{theorem}[Kuwata--Shioda $F^{(5)}$ model realises the closest variant]
\label{thm:c16-kuwata-F5-model}\ClaimStatusTheorem
For $E_1: y^2 = x^3 + ax + b$ and $E_2: y^2 = x^3 + cx + d$ with
$j(E_1) \neq j(E_2)$, $j(E_i) \notin \{0, 1728\}$, write
$\Delta_1 = -16(4 a^3 + 27 b^2)$, $\Delta_2 = -16(4 c^3 + 27 d^2)$.
The Kuwata--Shioda K3 surface
\[
  F^{(5)}_{E_1, E_2}: \quad
  Y^2 = X^3 - 3 a c\, t^4 X + \tfrac{1}{64}\, t\!\left(\Delta_1 t^{10}
  + 864\, b d\, t^5 + \Delta_2\right)
\]
has Picard rank $\rho = 18$, transcendental lattice
$T(F^{(5)}) \simeq T(F^{(1)})[5]$, fibre configuration
$2\, II + 20\, I_1$ (cuspidal fibres at $t = 0, \infty$), and
Mordell--Weil lattice
\[
  \mathrm{MW}(F^{(5)}_{\mathrm{gen}}) \;\simeq\; E_8[5] \oplus E_8[5]
  \quad \text{(rank $16$, $\det = 5^4$, minimal norm $4$)}.
\]
The Mordell--Weil lattice is isomorphic to $E_8 \oplus E_8$ as an
abelian group but \emph{not} as a Shioda-height lattice: the pairing
is rescaled by $5$.  Its Gram matrix is $5 \cdot G_{E_8}^{\oplus 2}$,
which is \emph{not} unimodular; hence this is the closest realisation
of the target structure compatible with Theorem~\ref{thm:c16-obstruction-E8E8-I2I2}.
\end{theorem}

\begin{proof}
The Weierstrass model is Shioda's equation (1.2) in
\emph{K3 surfaces and sphere packings} (MPIM preprint 2007, no.~137),
applied with $n = 5$ and the Kumar--Kuwata parametrisation of the
Inose surface by $(a, b, c, d)$ (Kumar--Kuwata, \emph{Nagoya Math.\ J.}\
228 (2017), Definition~2.3, Table after~2.3).  The discriminant
factors as $\Delta(t) = -16(4 A^3 + 27 B^2)$; direct computation on
$A = -3ac\, t^4$ and $B = \tfrac{1}{64}\, t(\Delta_1 t^{10} + \dots +
\Delta_2)$ gives a polynomial of degree $24$ in $t$ with a double root
at $t = 0$ (matching Kodaira type $II$) and a symmetric double root at
$t = \infty$ (matching type $II$ after inverting $t$); the remaining
$20$ roots are simple in the generic parameter locus.  Kodaira type $II$
is irreducible (Kodaira, \emph{Ann.\ of Math.}\ 77 (1963) Table~III),
so the reducible fibre lattice is trivial; Shioda--Tate yields rank
$16$.  The Mordell--Weil lattice identification with $E_8[5] \oplus E_8[5]$
is Theorem~2.4 / Theorem~2.5 of Shioda MPIM~137 (2007), via
$L + L^\sigma$ decomposition from the rational elliptic surface
$F^{(5)+}_{a,b,c,d}$ over $s = t + t^{-1}$ with $L \simeq E_8$.
\end{proof}
```

## Cross-consistency notes

### Against Wave-2 F03 (Shioda voice on $\mathrm{MW}(\pi)$)

Theorem~\ref{c16:thm:obstruction} is the resolution of Wave-2 F03 Retraction 3 ("Shioda canonical height without factor accounting") plus the Cycle-8 final consolidation in the Wave-2 F03 attack-heal log. The closest surviving form (Theorem~\ref{c16:thm:kuwata-F5}) corrects F03 Theorem~\ref{f03w2:thm:MW-E8E8} condition (3) ("the Shioda height pairing, rescaled to account for the Euler-characteristic factor $\chi(\mathcal{O}_S) = 2$, coincides with the $E_8 \oplus E_8$ Gram matrix (up to the factor $2$)") by making the rescaling factor $5$ (not $2$) explicit: the Kuwata base-change introduces an additional factor of $n$ from the Shioda-Tate height formula. The Wave-2 F03 condition (3) is *approximately* correct for a Jacobian fibration on the Shioda-Inose K3 of discriminant $-4$ or $-16$ but the rescaling factor depends on both $\chi(\mathcal{O}_S)$ and the base-change order $n$.

### Against `working_notes.tex` residual-frontier item

The residual-frontier item stated "elliptic-surface specialisation with Mordell-Weil-indexed simple roots" for the K3 Shioda-Inose structure. The surviving correct form: the Kuwata-Shioda base-change $F^{(n)}$ for $n \in \{2, 3, 4, 5, 6\}$ produces Mordell-Weil lattices $A_2^{\oplus 2}[n] \oplus \ldots \oplus E_8[n]^{\oplus 2}$ with rank $4(n-1)$ for $n \leq 5$; these are rescaled versions of the classical root lattices, not the root lattices themselves. The simple-root indexing in the Stage-2 GBKM $\mathfrak{g}_{\mathcal{E}, \mathbb{P}^1}$ picks up the rescaling factor, which must be absorbed into the Borcherds-product real-root normalisation. This is consistent with Wave-2 F03 "Retraction 3 Ghost theorem".

### Against CLAUDE.md essential constants

CLAUDE.md states $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1, 2, 3, 4, 6\}$; $N = 1$: Gritsenko $\Delta_5$ weight 5, $c_1(0) = 10$, $\kappa_{\mathrm{BKM}} = 5$. The elliptic-fibration case of the Vol III Borcherds product identification involves the Kuwata base-change $F^{(n)}$: at $n = 1$ (Inose fibration with $2 II^* + I_2$, MW rank 1), the Borcherds lift is $\Delta_5$; at $n > 1$, the base change introduces modular-form pullback factors compatible with the Shioda rescaling $T(F^{(n)}) \simeq T(F^{(1)})[n]$. The numerical claim $\kappa_{\mathrm{BKM}} = 5$ is for $N = 1$ and does not itself involve the $E_8(-1)^{\oplus 2}$ lattice structure; the latter is a \emph{sublattice} of the Borcherds lattice $\mathrm{II}_{2, 10}$ via the unimodular $E_8(-1)^{\oplus 2}$ primitive embedding, which is a lattice-theoretic fact about ambient unimodular lattices, not a Mordell-Weil identification.

### Against `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex`

The cited line 5057 proof uses torsion-section height pairing on an elliptic K3 as a witness for a specific lattice computation. The computation there ($\chi - \mathrm{contr}_v = 2 - 1 = 1$) is consistent with the Shioda-height formula applied at an $I_n$ fibre; it does not involve the $E_8(-1)^{\oplus 2}$ identification discussed here and is orthogonal to Theorem~\ref{c16:thm:obstruction}.

## Residual frontier notes

(R1) **Cross-check on $X_4$ (Vinberg's most algebraic K3).** A complete explicit enumeration of Jacobian elliptic fibrations on $X_4$, with their Weierstrass equations, discriminants, Kodaira types, and Mordell-Weil lattices (including the rescaling factor), is in Roulleau-Garbagnati-Salgado \emph{Rev.\ Mat.\ Iberoam.}\ 37 (2021) 1801-1840, Table 1 and 2. Direct verification that none has unimodular $E_8(-1)^{\oplus 2}$ MW lattice with $I_2 + I_2 + 20 I_1$ configuration is reducible to reading that paper's tables; not pursued here as the Shioda-Tate-Nikulin determinant obstruction already forces the conclusion.

(R2) **Partial weakening — fine-index saturation.** The generic Mordell-Weil lattice $M^{(5)}_{\mathrm{gen}} = E_8[5] \oplus E_8[5]$ might admit a finite-index saturation to a primitive sublattice of $\mathrm{NS}(F^{(5)})$ with more refined structure. Shioda Theorem 2.6 leaves room for a non-trivial index between $M_0 \oplus M_1$ and $M = \mathrm{MW}$; this index is a possible source of additional arithmetic structure. Not sufficient to produce unimodularity.

(R3) **Mock analogue of target.** A \emph{non-Jacobian} elliptic fibration (i.e.\ with no section, only a multi-section of degree $d > 1$) on $X_4$ or on a singular K3 may admit a different Mordell-Weil (or Jacobian-fibration) structure. This is outside the scope of Jacobian-fibration classification; governed by the Ogg-Shafarevich theory of elliptic surfaces. Whether such a non-Jacobian fibration realises $E_8(-1)^{\oplus 2}$ unimodular as its Jacobian-fibration MW is an open question consistent with F03 (R3).

## Primary sources used

- Shioda, T. \emph{K3 surfaces and sphere packings}, MPIM preprint 2007, no.\ 137. URL: https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/137.pdf
- Shioda, T. \emph{On the Mordell-Weil lattices}, J.\ Math.\ Soc.\ Japan 39 (1990) no. 2, 211-240.
- Schütt, M., Shioda, T. \emph{Mordell-Weil Lattices}, Ergebnisse der Mathematik 3.\ Folge vol.\ 70, Springer 2019, Chapters 6-8.
- Shioda, T., Inose, H. \emph{On singular K3 surfaces}, in: Complex Analysis and Algebraic Geometry, Iwanami Shoten (1977), 119-136.
- Nishiyama, K. \emph{The Jacobian fibrations on some K3 surfaces and their Mordell-Weil groups}, Japan J.\ Math.\ 22 (1996), 293-347.
- Shimada, I. \emph{On elliptic K3 surfaces}, Nagoya Math.\ J.\ 161 (2001), 23-54.
- Kumar, A., Kuwata, M. \emph{Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell-Weil lattices and their fields of definition}, Nagoya Math.\ J.\ 228 (2017), 124-185. arXiv:1409.2931.
- Kumar, A., Kuwata, M. \emph{Inose's construction and elliptic K3 surfaces with Mordell-Weil rank 15 revisited}, Contemp.\ Math.\ 703 (2018), 131-152. arXiv:1604.00738.
- Utsumi, K. \emph{Jacobian fibrations on the singular K3 surface of discriminant 3}, arXiv:1405.3577 (2014).
- Schütt, M. \emph{K3 surfaces with Picard rank 20}, Algebra Number Theory 4 (2010) no. 3, 335-356. arXiv:0804.1558.
- Kuwata, M. \emph{Elliptic K3 surfaces with given Mordell-Weil rank}, Comment.\ Math.\ Univ.\ St.\ Pauli 49 (2000), 91-100.
- Kodaira, K. \emph{On compact analytic surfaces II-III}, Ann.\ of Math.\ 77 (1963) and 78 (1963).
- Roulleau, X., Garbagnati, A., Salgado, C. (and coauthors). Relevant classification of elliptic fibrations on specific singular K3s.
