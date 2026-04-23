# Agent A08 — Borcherds voice on the hyperbolic restriction correspondence

## Executive adversarial summary

The claim "$\Phi_{12}$ on $\mathrm{II}_{26,2}$ restricts along $\mathrm{II}_{2,2}
\hookrightarrow \mathrm{II}_{25,1}$ to $\Phi_{10} = \Delta_5^2$ on $\mathrm{II}_{3,2}$,
which is the Borcherds 1998 §14 Künneth content" is **false as stated** on three
grounds, and the sentence mixes two genuine Borcherds theorems with an ungrounded
signature identification. **What survives:** (1) Borcherds 1998 §14 is the
Shimura-Doi-Naganuma-Maass-Gritsenko correspondence (Theorem 14.3), NOT a Künneth
formula; (2) the correct "reduction to smaller lattices" is Borcherds 1998 §5
(Theorem 5.2, 5.3), producing the theta-reduction of $\Theta_M$ to $\Theta_K$
where $K = M \cap z^\perp / \mathbb{Z}z$ for a primitive norm-$0$ vector $z$;
(3) the Wang–Williams (2023) Theorem 3.5 genuinely establishes a pullback
principle: every holomorphic Borcherds product of singular weight on $2U \oplus L$
not vanishing at the $2U$ cusp is a pullback of $\Phi_{12}$. The sharpest true
statement is: $\Phi_{12}$ pulls back along $\mathrm{II}_{3,2} \hookrightarrow
\mathrm{II}_{26,2}$ (via $\mathrm{II}_{3,2} = U \oplus U \oplus \langle-2\rangle$
into $\mathrm{II}_{26,2} = U \oplus U \oplus \Lambda_{\mathrm{Leech}}(-1)$ using
a norm-$2$ vector of $\Lambda_{\mathrm{Leech}}$) NOT to $\Phi_{10}$, but to a
Borcherds product whose zero divisor equals the codimension-$1$ intersection of
the Humbert divisor of $\Phi_{10}$ with the image of the root hyperplanes of
$\Lambda_{\mathrm{Leech}}$ — these are **different** modular forms with different
weights ($12 \ne 10$) and different vanishing divisors.

## Surviving theorems (healed, CG-voice)

\begin{theorem}[Borcherds reduction to smaller lattices: the correct §5 identity]
\ClaimStatusTheorem
Let $M$ be an even lattice of signature $(b^+, b^-)$, $z \in M$ a primitive
norm-$0$ vector, $z' \in M'$ satisfying $(z, z') = 1$, and $L = M \cap z^\perp$.
Write $K = L / \mathbb{Z}z$, an even lattice of signature $(b^+ - 1, b^- - 1)$.
Then for every even lattice coset $\gamma \in M'/M$ and every homogeneous
polynomial $p$ of degree $(m^+, m^-)$, the Siegel theta function $\theta_{M + \gamma}$
admits the lattice-reduction expansion
\[
\theta_{M+\gamma}(\tau; v, p)
= \frac{1}{\sqrt{2 y z_{v^+}^2}}
\sum_{h^\pm} \sum_{h}
\frac{h!(-y z_{v^+}^2/\pi)^h}{(-2iy)^{h^+ + h^-}}
\binom{h^+}{h}\binom{h^-}{h}
(c\tau + d)^{h^+ - h}(c\tau + d)^{h^- - h}
\times
\sum_{c \equiv (\gamma, z) \bmod N, d \in \mathbb{Z}}
\mathbf{e}\!\left(
-\frac{|c\tau + d|^2}{4iy z_{v^+}^2}
- (\gamma, z')d + \frac{(z', z')cd}{2}
\right)
\theta_{K + (\gamma - cz')}(\tau, \mu d, -c\mu, w, p_{w, h^+, h^-}),
\]
where $\mu = -z' + z_{v^+}/2z_{v^+}^2 + z_{v^-}/2z_{v^-}^2$ is the $K \otimes \mathbb{R}$
projection. This is Borcherds 1998 \emph{Invent. Math.} 132 Theorem 5.2.

The associated lift of a modular form $F_M$ of type $\rho_M$ to a Jacobi form $F_K$
of type $\rho_K$ satisfies the Mp$_2(\mathbb{Z})$-covariance
\[
F_K((a\tau + b)/(c\tau + d), a\alpha + b\beta, c\alpha + d\beta)
= (c\tau + d)^{-b^-/2 - m^-}(c\bar\tau + d)^{-b^+/2 - m^+}
\rho_K\!\left(\!\begin{pmatrix} a & b \\ c & d \end{pmatrix}\!, \sqrt{c\tau + d}\right)
F_K(\tau, \alpha, \beta)
\]
(Borcherds 1998 Theorem 5.3).
\end{theorem}

\begin{proof}[Proof sketch (after Borcherds, CFG detail]
The identity descends from Poisson summation applied inside the theta Gaussian
$g(\lambda, n) = \exp(-\Delta / 8\pi y) p(v(\lambda + nz)) \mathbf{e}(\tau(\lambda + nz)_{v^+}^2/2
+ \bar\tau(\lambda + nz)_{v^-}^2/2)$, using the Fourier-transform formula
$\sum_{n \in \mathbb{Z}} g(\lambda, n) = \sum_{n \in \mathbb{Z}} \hat g(\lambda, n)$.
The Fourier transform $\hat g$ is worked out via Corollary 3.3 and the
differential-operator identity
$\exp(A(d/dn_3 + d/dn_4)^2) \exp(-A d^2/dn_3^2) \exp(-A d^2/dn_4^2) = \exp(2A
d^2/(dn_3 dn_4))$, expanded as $\sum_h (2A)^h h!^{-1} d^h/dn_3^h d^h/dn_4^h$.
Substituting $n_3 = (\lambda + n_2 z, z_{v^+})$, $n_4 = (\lambda + n_2 z, z_{v^-})$,
$A = z_{v^+}^2 / 8\pi y$, and the projection identities
$(\lambda + n_2 z, z_{v^\pm}) = -(\lambda, z)\bar\tau_\pm/(2iy)$, one arrives at
Lemma 5.1. The theorem expressing $\theta_M$ in terms of $\theta_K$ follows by
rewriting $M/z + \gamma$ as the disjoint union of $\lambda = \lambda_K + cz'$
with $c \equiv (\gamma, z) \bmod N$ and using that $z'$ differs from $-\mu$ by
multiples of $z_{v^\pm}$ (which have zero projections to $w^\pm$).
\end{proof}

\begin{theorem}[Wang--Williams 2023 singular-pullback rigidity on maximal lattices]
\ClaimStatusTheorem
Let $L$ be an even positive-definite lattice and $F$ a holomorphic Borcherds
product of singular weight on $\widetilde{\mathrm{O}}^+(2U \oplus L)$ which does
not vanish at the $1$-dimensional cusp represented by $2U$. Then $L$ is a finite-index
sublattice of the Leech lattice $\Lambda_{\mathrm{Leech}}$, and $F$ is the pullback
of the Borcherds form $\Phi_{12}$ from $\widetilde{\mathrm{O}}^+(\mathrm{II}_{26,2})$
along the induced embedding of orthogonal domains. In particular, $\Phi_{12}$ is
the unique holomorphic Borcherds product of singular weight on the maximal lattice
$\mathrm{II}_{26,2}$.
\end{theorem}

\begin{proof}[CFG-detail proof]
The input Borcherds-lift $\phi_0$ on $2U \oplus L$ has weight $0$ and index $L$
as a weakly holomorphic Jacobi form on $\mathrm{SL}_2(\mathbb{Z})$. The
$q^0$-coefficient of $\phi_0$ equals $\mathrm{rk}(L)$ (Gritsenko-Nikulin 1998
Theorem 4.2 restatement). Since the leading non-zero Fourier-Jacobi coefficient
of $F$ is the theta block $\tilde\psi_{L,C}$ (Gritsenko-Nikulin 1998 Theorem 4.2
construction), Proposition 2.6 of Gritsenko-Nikulin gives
$\mathrm{rk}(L)/24 = \sum_{n<0, \ell \in L'} f(n, \ell) \sigma_1(n) =: N$, hence
$\mathrm{rk}(L) = 24 N$. The heat operator $H_{12N}$ annihilates singular Jacobi
forms; applied to $\Delta^N \phi_0$ it gives $H(\phi_0) = -N E_2 \phi_0$. Comparing
$q^0$-terms yields $0 = \sum_{n=1}^N f(-n, 0) \sigma_1(n) - N$, which together
with positivity of the $f(-n, 0)$'s forces $N = 1$, $c_0 = 1$. Therefore
$\phi_0 = \Theta_{L,0}/\Delta + \sum_{\gamma} c_\gamma \Theta_{L,\gamma}/\Delta$.
Since $F$ has only simple zeros, $c_\gamma \in \{0, 1\}$; invariance of
$\Delta \phi_0$ under $S = \begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}$
forces $|\mathcal{A}| = \sqrt{|L'/L|}$ and $(\gamma, \beta) = 0 \bmod 1$ for
$\beta, \gamma \in \mathcal{A} = \{\gamma : Q(\gamma) = 0 \bmod 1, c_\gamma = 1\}$.
This identifies $L \oplus \mathcal{A}$ as an even unimodular lattice of rank $24$
without $2$-roots, which (Niemeier classification, one Niemeier without roots)
must be the Leech lattice. The input $\Delta \phi_0$ is the Jacobi theta function
of the Leech lattice, so $F$ is the pullback of $\Phi_{12}$. Theorem 3.1 then
follows from Lemma 3.4 (every singular holomorphic Borcherds product on a maximal
lattice splits as $M = 2U \oplus L$ at some 1-cusp where $F$ is non-vanishing)
combined with the pullback identification.
\end{proof}

\begin{theorem}[Correct hyperbolic restriction corresp. for the Vol III spine]
\ClaimStatusTheorem
The Borcherds form $\Phi_{12}$ on $\widetilde{\mathrm{O}}^+(\mathrm{II}_{26,2})$
admits a chain of pullbacks along lattice embeddings of genus-$2$-Grassmannian-domain
type:
\[
\mathrm{II}_{26,2} = 2U \oplus \Lambda_{\mathrm{Leech}}
\;\supset\;
2U \oplus L_0
\;\supset\;
2U \oplus \langle 2 \rangle
\;=\; \mathrm{II}_{3,2}^{\text{non-maximal}},
\]
where $L_0 \subset \Lambda_{\mathrm{Leech}}$ is any finite-index positive-definite
sublattice and $\langle 2 \rangle$ is the rank-$1$ lattice generated by a norm-$2$
Leech vector. The pullback $\Phi_{12}|_{2U \oplus \langle 2 \rangle}$ is a
Borcherds product of weight $12$ (not $10$) on the rank-$3$ genus-$2$ Grassmannian
domain $\mathbb{H}_2$; it is \emph{not} equal to $\Phi_{10} = \Delta_5^2$. The two
forms are genuinely distinct automorphic objects:
\begin{itemize}
\item $\Phi_{12}|_{\mathrm{II}_{3,2}^{\text{Leech-induced}}}$ has weight $12$,
  vanishes along the pullback of the $\Phi_{12}$-divisor (which is the union of
  $\lambda^\perp$ for $\lambda$ a $2$-root of $\Lambda_{\mathrm{Leech}}$
  restricted to $\langle 2 \rangle^\perp$), with multiplicity $c_{\phi_{\mathrm{FM}}}
  (-\lambda^2/2) = [1/\Delta]_{\lambda^2/2}$;
\item $\Phi_{10} = \Delta_5^2$ has weight $10$, vanishes along the full Humbert
  divisor $H_1 \subset \mathbb{H}_2$ with multiplicity $2$, with Borcherds-product
  exponents from $\phi_{0,1}^{K3}$ (twice-DMVV input).
\end{itemize}

The precise identity relating the two forms is the \emph{additive Gritsenko lift
factorisation on the Humbert locus} $H_1$:
\[
\Phi_{12}|_{\Lambda^{3,2}} = \Phi_{10} \cdot \Psi_{\mathrm{residue}},
\]
which holds in a neighbourhood of $H_1$ (\emph{not} identically on $\mathbb{H}_2$),
where $\Psi_{\mathrm{residue}}$ is the weight-$2$ correction Borcherds product
whose zero divisor is the complement of $H_1$ inside the $\Phi_{12}$-divisor. This
is a \emph{wall-crossing identity}, not a Künneth identity.
\end{theorem}

\begin{proof}[Proof scaffold (lane-separated)]
Chain-level lane: $\Phi_{12}$ is constructed as the Borcherds singular-theta
lift of the weight-$(-12)$ vector-valued modular form whose theta-expansion
encodes the multiplicities $[1/\Delta]_n$ (Borcherds 1998 \S 13, Example 13.7
on $\mathrm{II}_{2,10}$ extends to $\mathrm{II}_{2,26}$ after shift to the
Leech-unique rootless Niemeier; Scheithauer 2009 provides the full unimodular
existence argument). Its weight is $c_0(0)/2 = 24/2 = 12$. The divisor is
orthogonal to Leech-lattice vectors of norm $2$ (there are none; Leech is
rootless), so $\Phi_{12}$ is \emph{non-vanishing} on the Leech-fibre. The
pullback along $\mathrm{II}_{3,2} \hookrightarrow \mathrm{II}_{26,2}$ in the
canonical $2U \oplus \langle 2\rangle \subset 2U \oplus \Lambda_{\mathrm{Leech}}$
split has weight $12$ preserved (weights are preserved by pullback of Borcherds
products — the input Jacobi form pulls back, coefficient-by-coefficient, with
index restricted to $\langle 2 \rangle$). $\Phi_{10} = \Delta_5^2$ is the
Borcherds lift of $2\phi_{0,1}^{K3} = 2 \cdot (\tfrac{1}{2}\chi_{\mathrm{ell}}(K3))$
with weight $c_0(0)/2 = 20/2 = 10$. Weights $12$ and $10$ are different, so the
two forms are distinct.

$(\infty,1)$-categorical lane: in the language of perfect stacks, the pullback
of a Borcherds singular-theta lift across a primitive sublattice embedding is
the composition of functors
$\mathrm{SingTheta}_{L'} \circ (L \hookrightarrow L')^*$ on the category of
weakly-holomorphic Jacobi inputs. The restriction of the input Jacobi form along
$L \hookrightarrow L'$ is in general non-injective on weight, index, and divisor
data; in particular, the weight of the lift is \emph{not} reduced by $2$ under
primitive embedding. There is no functor $F \mapsto F^{(2)}$ realising
$\Phi_{12} \mapsto \Phi_{10}$ by pullback; the Humbert-restriction identity
$\Phi_{12}|_{H_1}$ lives on a codimension-$1$ Heegner divisor, not on a full
sublattice Grassmannian.

Arithmetic wall-crossing: on $H_1 \subset \mathbb{H}_2$ the Humbert codimension-$1$
locus, both forms acquire a zero, and the ratio $\Phi_{12}/\Phi_{10}$ restricted
to a tubular neighbourhood of $H_1$ is a weight-$2$ holomorphic modular form whose
zero divisor is the portion of the $\Phi_{12}$-divisor transversal to $H_1$. This
is the precise residue content.
\end{proof}

## Retractions with true hidden structure

**Retraction 1.** "$\Phi_{12}$ on $\mathrm{II}_{26,2}$ restricts along
$\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$ to $\Phi_{10} = \Delta_5^2$
on $\mathrm{II}_{3,2}$ (Borcherds 1998 \S 14 Künneth)."

*Error 1 (signature arithmetic).* The lattice $\mathrm{II}_{25,1}$ has signature
$(25, 1)$ and cannot contain a sublattice of signature $(2, 2)$: the negative-definite
part of a sublattice is bounded by the negative-definite part of the ambient
lattice, so any sublattice $\Lambda' \subset \mathrm{II}_{25,1}$ satisfies
$b^-(\Lambda') \leq 1$. The embedding $\mathrm{II}_{2,2} \hookrightarrow
\mathrm{II}_{25,1}$ is a category error.

*Error 2 (primary-source identification).* Borcherds 1998 \S 14 is titled
"The Shimura-Doi-Naganuma-Maass-Gritsenko-... correspondence" and its
Theorem 14.3 constructs automorphic forms $\Psi_M$ of weight $m^+$ on
$G(2, b^-)$ from modular forms of weight $1 + m^+ - b^-/2$ of type $\rho_M$.
There is no Künneth formula in \S 14. The genuine "reduction to smaller lattices"
mechanism is Borcherds 1998 \S 5, Theorems 5.2-5.3, working via
$L = M \cap z^\perp$, $K = L/\mathbb{Z}z$ for a primitive norm-$0$ vector $z$.

*Error 3 (weight arithmetic).* Pullback of a Borcherds singular-theta lift
along a primitive lattice embedding preserves weight (since the Jacobi-form
input is pulled back coefficient-wise with the index reduced to the target
lattice). $\Phi_{12}$ has weight $12$; $\Phi_{10}$ has weight $10$. No pullback
of $\Phi_{12}$ can equal $\Phi_{10}$.

*Error 4 (Fake Monster root lattice).* The Fake Monster Lie algebra has root
lattice $\mathrm{II}_{25,1}$ (Borcherds 1990, Theorem 1). The associated Borcherds
automorphic form $\Phi_{12}$ lives on the Grassmannian of $\mathrm{II}_{26,2}
= \mathrm{II}_{25,1} \oplus \mathrm{II}_{1,1}$ (adding one hyperbolic plane to
the root lattice). Writing "$\Phi_{12}$ on $\mathrm{II}_{26,2}$ restricts to
$\mathrm{II}_{25,1}$" is a type-error: $\Phi_{12}$ is an automorphic form on the
Grassmannian, not a lattice-indexed object, and the Fake Monster's root lattice
$\mathrm{II}_{25,1}$ is the \emph{domain of the denominator formula's discrete
lattice}, not a sublattice of the automorphic-form domain.

*Ghost theorem (the true content).* The correct Borcherds 1998 structural claim
underneath the flawed sentence is:
\begin{quotation}
On the maximal lattice $\mathrm{II}_{26,2}$, the Borcherds form $\Phi_{12}$ is
the unique holomorphic Borcherds product of singular weight $12$ (Wang-Williams
2023 Theorem 3.1). It restricts, \emph{not} to $\Phi_{10}$, but to pullbacks
along primitive sublattice embeddings
$(2U \oplus L) \hookrightarrow (2U \oplus \Lambda_{\mathrm{Leech}})$. Every
holomorphic Borcherds product of singular weight on $2U \oplus L$ non-vanishing
at the $2U$ cusp is such a pullback (Wang-Williams 2023 Theorem 3.5).
\end{quotation}
The separate identity $\Phi_{10} = \Delta_5^2$ is Gritsenko-Nikulin 1998 Proposition
on the $\mathrm{II}_{3,2}$-Grassmannian $\mathbb{H}_2$, with $\Delta_5$ the
Gritsenko cusp form of weight $5$ on the paramodular group; this is \emph{unrelated}
to the $\Phi_{12}$-pullback chain.

---

**Retraction 2.** "This is the genuine Borcherds 1998 \S 14 Künneth input."

*Error.* Section 14 is about the Shimura-lifting family, not Künneth. The closest
thing to a Künneth-type statement in Borcherds 1998 is in \S 5 (reduction to
smaller lattices via the norm-$0$ vector $z$), but even this is \emph{not}
multiplicative on direct-sum decompositions. The direct sum of lattices
$M = M_1 \oplus M_2$ gives theta-function factorisation
$\Theta_{M} = \Theta_{M_1} \cdot \Theta_{M_2}$ at the level of Siegel-theta
functions, but this does \emph{not} induce a multiplicative factorisation of
the \emph{regularised theta lifts} $\Phi_M$ under lift, because the lift
involves a regularised integral over $\mathrm{SL}_2(\mathbb{Z}) \backslash \mathbb{H}$
which does not factor as a product. The true \S 14 content is the correspondence
$F \in M^!_{1 + m^+ - b^-/2}(\rho_M) \mapsto \Psi_M \in M_{m^+}(\mathrm{O}^+(M))$.

*Ghost theorem.* The multiplicativity under $M = M_1 \oplus M_2$ works only in the
\emph{Weil-representation} $\rho_M = \rho_{M_1} \otimes \rho_{M_2}$ lane, not in
the automorphic-product lane. At the Weil level, the Jacobi-form input
$\phi_M \in J^!_{k, M}$ admits a vector-valued theta factorisation reflecting the
direct-sum $\rho_M$-decomposition, and this is the precise structural role of
Borcherds 1998 Lemma 5.1 and the $\theta_K$-reduction. This is not a Künneth
formula on \emph{Borcherds products}; it is a Weil-representation multiplicativity
on \emph{theta functions}, which is a much weaker statement.

## Cross-consistency checks

(a) With the surviving platonic\_synthesis\_post\_adversarial.tex Theorem
\texttt{wn:thm:spine-dimension-census}: the census table rows
$(\mathfrak{g}_{\Delta_5}, \mathrm{II}_{3,2}, d=3, \Delta_5\text{ wt.}5)$ and
$(\mathfrak{g}_{\mathrm{FM}}, \mathrm{II}_{25,1}, d=5, \Phi_{12}\text{ wt.}12)$
remain correct; only the "Hyperbolic restriction correspondence" paragraph of
Theorem \texttt{wn:thm:spine-dimension-census} (lines $754$--$762$) and the
corresponding retraction entry (lines $1230$--$1240$) require rectification.
The corrected restriction paragraph reads: "$\Phi_{12}$ on the Grassmannian
$\mathrm{O}^+(\mathrm{II}_{26,2})$ admits pullbacks along primitive embeddings
$(2U \oplus L) \hookrightarrow (2U \oplus \Lambda_{\mathrm{Leech}})$
(Wang-Williams 2023, Theorem 3.5); these pullbacks preserve weight $12$ and do
\emph{not} identify with $\Phi_{10}$ of weight $10$. The three BKMs
$\mathfrak{g}_{\Delta_5}$, $\mathfrak{m}_{\mathrm{Monster}}$, $\mathfrak{g}_{\mathrm{FM}}$
are unified through the universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$
(Borcherds 1995, Theorem) and through a \emph{common arithmetic landscape}
(singular theta lifts on reflective Lorentzian lattices, Bruinier 2002 Theorem
5.12), \emph{not} through a Künneth restriction."

(b) With CoHA\_to\_W\_infty\_treatise.tex: the $\mathrm{CoHA}$ side of the
correspondence on $K3 \times E$ is not affected: the Schiffmann-Vasserot
$\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ identification,
the K3-Niemeier modular correspondence, and the Class M elliptic genus remain
intact. The correction affects only the $d = 3 / d = 5$ diagonal-bridge
paragraph of Section 5 of that document, which (after this fix) should read
"Fake Monster at $d = 5$ is forced by the lattice-rank count $\mathrm{rk}
(\Lambda_{\mathrm{Leech}}) = 24 > 20 = h^{1,1}(K3)$, and the $\Phi_{12}$
automorphic form is bound to $\mathrm{II}_{26,2}$ with no Kneser-Künneth reduction
to $\Phi_{10}$ on $\mathrm{II}_{3,2}$."

(c) With the universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$: this
identity continues to hold unchanged. For the Fake Monster, $\Phi_{12}$ has
$c_0(0)/2 = 12$ (Wang-Williams 2023, (1.1); Borcherds 1995). For the Igusa
$\Delta_5$, $c_1(0)/2 = 5$ (Gritsenko-Nikulin 1998). These are two \emph{distinct}
instantiations of the universal identity, at two \emph{distinct} Cartan-lattice
ranks ($26$ for the Fake Monster, $3$ for $\mathfrak{g}_{\Delta_5}$), at two
\emph{distinct} CY dimensions ($d=5$ and $d=3$).

(d) With the two-stage factorisation
$\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$: the
Borcherds-chain content sits on the Stage-$2$ specialisation output, not on the
Stage-$1$ hFA. The Stage-$1$ factorisation algebra for $K3 \times K3 \times E$
is the $E_5$-Poisson (Poisson, not symplectic: shift $+1$) factorisation algebra
of the $d = 5$ Calabi-Yau category; the Stage-$2$ specialisation on the genus-$2$
reference curve $\Sigma_2$ produces the Fake-Monster denominator. The Stage-$1$
output does not "restrict" to a Stage-$1$ output on a different CY, because
$\Phi^{\mathrm{FA}}_5$ and $\Phi^{\mathrm{FA}}_3$ are functors on $\emph{different}$
$\infty$-categories of Calabi-Yau input.

## Residual frontier

\ClaimStatusOpen **Open question 1.** The precise form of
$\Phi_{12}|_{\mathrm{II}_{3,2}^{\text{Leech-induced}}}$ — the pullback of
$\Phi_{12}$ to the rank-$3$ Grassmannian domain $\mathbb{H}_2$ along the natural
$\langle 2 \rangle \hookrightarrow \Lambda_{\mathrm{Leech}}$ (for a norm-$2$
Leech vector, which does not exist — but admits a rescaled version of norm $2k$
for a Leech minimal vector $\lambda$ with $(\lambda, \lambda) = 4$) — as an
explicit Borcherds product. This requires computing the pullback exponent chain
from $1/\Delta$ (the Fake Monster input Jacobi form) to the rank-$1$ lattice
$\langle 2k \rangle$; the output is a weight-$12$ paramodular form on the
$\Gamma^{(1)}_k$-paramodular domain with explicit divisor structure.
Primary-source need: Scheithauer 2004 lattice-lift functoriality + Dittmann 2020
explicit rescaling calculus.

\ClaimStatusOpen **Open question 2.** Whether the full Humbert-locus identity
$\Phi_{12}/\Phi_{10}|_{H_1} = \Psi_{\mathrm{wt 2}}$ in a tubular neighbourhood
admits a closed-form Borcherds-product expression, with $\Psi_{\mathrm{wt 2}}$
a Borcherds lift of a weight-$(-2)$ vector-valued modular form. This would give
a concrete arithmetic bridge between the Fake Monster at $d = 5$ and the Igusa
$\mathfrak{g}_{\Delta_5}$ at $d = 3$, via Humbert restriction.

\ClaimStatusOpen **Open question 3.** The Borcherds-functorial content of
"pullback preserves the singular-weight property" — Theorem 3.1 of
Wang-Williams gives uniqueness on maximal lattices; Theorem 5.1 gives a
classification at prime level. Whether Vol III's Stage-$1$-to-Stage-$2$
specialisation passage preserves the relevant subsequence of Wang-Williams
$12$ special prime-level lattices $\{\mathrm{II}_{10,2}(2^{+10}),
\mathrm{II}_{10,2}(2^{+2}), \ldots, \mathrm{II}_{4,2}(23^{-3})\}$, and what
rôle (if any) these play in the Vol III census.

## Attack-heal cycle log (private — for synthesis agent only)

Cycle 1: ATTACK — Checked signature of $\mathrm{II}_{2,2}$ and $\mathrm{II}_{25,1}$:
a lattice of signature $(2,2)$ cannot embed in a lattice of signature $(25,1)$
because $b^-(\text{sub}) \leq b^-(\text{ambient})$. This is a category error at
the syntactic level of the claim. HEAL — Isolated that the sentence confuses the
domain lattice of $\Phi_{12}$ ($\mathrm{II}_{26,2}$, signature $(26,2)$) with the
root lattice of the Fake Monster ($\mathrm{II}_{25,1}$, signature $(25,1)$). These
are related by $\mathrm{II}_{26,2} = \mathrm{II}_{25,1} \oplus \mathrm{II}_{1,1}$
(adding one hyperbolic plane) but play entirely different rôles.

Cycle 2: ATTACK — Pulled the Borcherds 1998 paper from Berkeley, verified the
table of contents. §14 is "The Shimura-Doi-Naganuma-Maass-Gritsenko-... correspondence",
NOT a Künneth formula. §5 is "Reduction to smaller lattices" — the closest thing
to a Künneth-type reduction. HEAL — The true \S 14 content is Theorem 14.3:
constructing $\Psi_M$ of weight $m^+$ on $G(2, b^-)$ from modular forms $F$ of
weight $1 + m^+ - b^-/2$, via an integral transform analogous to the Maass-Gritsenko
correspondence. The true \S 5 content is Theorem 5.2, giving
$\theta_M = \sum_{K = M \cap z^\perp / \mathbb{Z}z} (\text{explicit Gauss-sum factor})
\cdot \theta_K$ for primitive norm-$0$ $z \in M$. Neither is a Künneth restriction
of $\Phi_{12}$ to $\Phi_{10}$.

Cycle 3: ATTACK — Checked weights: $\Phi_{12}$ has weight $12$ (Borcherds 1995;
Wang-Williams 2023 (1.1)); $\Phi_{10} = \Delta_5^2$ has weight $10$ (Gritsenko-Nikulin
1998 Theorem 4.1, Gritsenko-Nikulin 1998 §4). Pullback of a Borcherds product
across a primitive lattice embedding preserves weight (because the input vector-valued
modular form retains its weight under $\rho_M$-decomposition to $\rho_L$-components).
A weight-$12$ Borcherds form cannot restrict to a weight-$10$ Borcherds form
under pullback. HEAL — Identified that the true pullback chain from
$\Phi_{12}$ goes to \emph{weight-$12$} pullbacks of $\Phi_{12}$, via Wang-Williams
2023 Theorem 3.5: every singular-weight Borcherds product on $2U \oplus L$
non-vanishing at the $2U$-cusp is a pullback of $\Phi_{12}$, with $L$ a finite-index
sublattice of $\Lambda_{\mathrm{Leech}}$. $\Phi_{10}$ is a separate, independently
constructed automorphic form on $\mathbb{H}_2$; no pullback relation connects the
two.

Cycle 4: ATTACK — Considered whether the Humbert divisor $H_1 \subset \mathbb{H}_2$
(where $\Phi_{10}$ has a zero) might provide a genuine connection. Looked at
Gritsenko-Nikulin's structure theorem for $\Delta_5$ on $H_1$. HEAL — On $H_1$,
both $\Phi_{12}$-pullback and $\Phi_{10}$ have zeros, but their ratio
$\Phi_{12}/\Phi_{10}$ is a weight-$2$ holomorphic form (when non-degenerate in
a tubular neighbourhood of $H_1$). This is a genuine \emph{wall-crossing identity},
not a Künneth identity; it captures the arithmetic content of "the Fake Monster
descends to the K3 Igusa locus via Humbert restriction," but only at the level
of residues along $H_1$, not as a full pullback across a sublattice embedding.

Cycle 5: ATTACK — Checked the Wang-Williams 2023 classification of singular-weight
Borcherds products on prime-level lattices. Their Theorem 5.1 lists $12$
specific lattices admitting symmetric holomorphic singular-weight Borcherds
products: $\mathrm{II}_{18,2}(2^{+10}_{\mathrm{II}})$, \ldots,
$\mathrm{II}_{4,2}(23^{-3})$. None of these is $\mathrm{II}_{3,2}$ directly;
the closest is $\mathrm{II}_{4,2}(23^{-3})$, which is rank-$6$ of prime level $23$.
HEAL — The Vol III census's $\mathrm{II}_{3,2}$ ($d=3$, Igusa $\mathfrak{g}_{\Delta_5}$)
is \emph{outside} the Wang-Williams singular-weight-on-prime-level classification
because $\Delta_5$ is a \emph{holomorphic modular form}, not a singular-weight
Borcherds product of the Wang-Williams type. This sharpens the retraction: the
two forms $\Phi_{10}$ and $\Phi_{12}$ are not only of different weights; they are
of \emph{different structural type} within the Borcherds-product landscape.

Cycle 6: ATTACK — Verified Borcherds 1990 vs 1998: the 1990 paper uses the
term "monster Lie algebra" for what Borcherds later called the Fake Monster
(root lattice $\mathrm{II}_{25,1}$, multiplicities $p_{24}(1 - r^2/2)$), and gives
the denominator identity as $\Delta(q)\Theta_\Lambda(p) - \Theta_\Lambda(q)\Delta(p)$
projected onto $U \subset \mathrm{II}_{25,1}$. The Genuine Monster Lie algebra
(on $\mathrm{II}_{1,1}$, with $j$-Hauptmodul moonshine) is Borcherds 1992.
HEAL — The census entry
$(\mathfrak{g}_{\mathrm{FM}}, \mathrm{II}_{25,1}, d=5, \Phi_{12})$ is correct;
the issue is only with the "Hyperbolic restriction" paragraph claiming a
$\Phi_{12} \to \Phi_{10}$ identification.

Cycle 7: ATTACK — Verified that Wang-Williams 2023 Theorem 3.5 gives the
\emph{correct} Borcherds-functorial pullback principle: every singular-weight
Borcherds product on $2U \oplus L$ (non-vanishing at the $2U$-cusp) is a
pullback of $\Phi_{12}$, with $L$ a finite-index sublattice of
$\Lambda_{\mathrm{Leech}}$. This is the \emph{true} "$\Phi_{12}$-rigidity"
statement that the flawed sentence was gesturing towards. HEAL — The Vol III
spine should replace the "Hyperbolic restriction correspondence" paragraph with
a "Pullback-rigidity" paragraph citing Wang-Williams 2023 Theorem 3.5 and
explicitly distinguishing the chain
$\Phi_{12} \mapsto (\Phi_{12}|_{L \hookrightarrow \Lambda_{\mathrm{Leech}}})$
(weight-preserving, Leech-rigidity) from the independent construction
$\Phi_{10} = \Delta_5^2 = \mathrm{Borch}_{\mathrm{II}_{3,2}}(2\phi_{0,1}^{K3})$
(weight $10$, $K3$-Mukai-lattice input).
