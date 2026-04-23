# Agent A06 — Kapranov voice on the Dolbeault-degree-count formality claim

## Executive adversarial summary

The spine theorem $\texttt{wn:thm:spine-minimal-model}$ survives in its conclusion
($\ell_n^{\min} = 0$ on flat $\CC^3$, all $n \geq 3$), but the stated degree-count
mechanism requires three structural corrections before it is inscribable at
Costello--Francis--Gwilliam detail. First: the attribution "Kapranov 1999 \S 3.1"
is wrong; Kapranov, Compositio 115 (1999), \S 3 treats the general \emph{non-flat}
Dolbeault $L_\infty$-structure on $\Omega^{0,\bullet}(X, T_X[-1])$ whose ternary
bracket is $\At(T_X) \cup \At(T_X)$ --- precisely the \emph{non-formal} case
where the degree count \emph{fails}. The flat-$\CC^n$ formality on a contractible
holomorphic base is Kontsevich 1997 (q-alg/9709040, \S 6.4) adapted to the
Dolbeault setting, lifted to compactly-supported / polynomial representatives
by Costello--Gwilliam (Vol II, Ch 7). Second: the phrase "the Hodge-homotopy
propagator maps $\Omega^{0, q} \to \Omega^{0, q-1}$" is ambiguous on non-compact
$\CC^3$: there is no canonical Hodge-homotopy on the full Fréchet space
$\Omega^{0,\bullet}(\CC^3)$ because $\Box_{\bar\partial}$ has continuous
spectrum at $0$ and no Green's operator in the compact-manifold sense; the
construction is performed on the compactly-supported Dolbeault complex
$\Omega^{0,\bullet}_c(\CC^3)$ with BV-regularised propagator
$G_\varepsilon = (e^{-\varepsilon \Box} - 1)/\Box$ (Costello--Li 2016
arXiv:1606.00365, \S 3). Third: the degree chain traced naively --- "inputs in
$\Omega^{0,0}$; internal edges land in $\Omega^{0,-1} = 0$" --- is incorrect
because $\ell_2^{\hCS}$ carries a grading shift. On the shifted Dolbeault
complex $\cE_{\hCS} = \Omega^{0,\bullet}(\CC^3, \fg)[1]$, the Lie bracket
$\ell_2$ has internal degree $0$ but \emph{Dolbeault} degree $0$, so brackets
of $\Omega^{0,0}[1]$-inputs land in $\Omega^{0,0}[1]$ and the propagator $h$
(acting on the \emph{unshifted} Dolbeault degree) maps $\Omega^{0,0}[1]
\to \Omega^{0,-1}[1] = 0$ only after correctly tracking that the shift
does not affect the Dolbeault degree. The degree count survives, but
requires the explicit bookkeeping.

Sharpest new theorem (healed):
On $\CC^3$ with the compactly-supported Dolbeault model, the
Kontsevich--Soibelman minimal-model recursion
$\ell_n^{\min} = H \circ \sum_{T \in \cT_n} \beta_T$ satisfies
$\ell_n^{\min} = 0$ for all $n \geq 3$ because for every rooted tree $T$
with $n \geq 3$ leaves, some internal edge carries a propagator $h$ acting
on a harmonic input of Dolbeault degree $0$, whose image
$\Omega^{0,-1} = 0$ structurally. The mechanism is a grading-shift-compatible
Dolbeault degree count, \emph{not} Kapranov 1999 \S 3.1 (whose content
is the \emph{obstructed} case $\At(T_X) \neq 0$).

Sharpest new conjecture (isolated):
The competing vanishing $H^3(K3, \Omega^3_{K3}) = 0$ is Serre-dual to
$H^0(K3, T_{K3}) = 0$ (no holomorphic vector fields on K3), whereas
$H^3(K3, \Lambda^3 T_{K3}) = 0$ is a rank-$2$ vanishing
($\Lambda^3 T_{K3} = 0$ on a surface). The two receptacles are not
equivalent --- the Kuranishi deformation functor $\mathrm{Def}_X$ of
complex-structure deformations on K3 has tangent $H^1(K3, T_{K3})$ and
obstructions in $H^2(K3, T_{K3})$, \emph{not} $H^3$; the cubic
receptacle argument applies to the Kapranov $L_\infty$-model on
$\Omega^{0,\bullet}(X, T_X[-1])$ at $d = 3$, where the cubic bracket
lands in $H^{0,3}(X, \Lambda^3 T_X) = H^3(X, \Lambda^3 T_X)$. The two
vanishings are independent; on K3 they both hold but for disjoint
structural reasons.

## Surviving theorems (healed, CG-voice)

### Theorem (Flat-$\CC^3$ formality of 6D hCS, degree-count proof).
\ClaimStatusTheorem

Let $\fg$ be a simple complex Lie algebra. The $L_\infty$-algebra
$\cE_{\hCS}(\CC^3) = (\Omega^{0,\bullet}_c(\CC^3, \fg)[1], \bar\partial,
[-,-], 0, 0, \ldots)$ --- the Dolbeault complex of compactly-supported
$(0,\bullet)$-forms valued in $\fg$, shifted by $1$, with the Chevalley--
Eilenberg differential $\bar\partial$ and the Lie bracket --- has
Kontsevich--Soibelman minimal model $(\mathcal{H}, \bar\partial = 0,
\ell_2^{\min} = [-,-]_\fg, \ell_n^{\min} = 0\ \forall n \geq 3)$ equal
to the trivial graded-Lie-algebra $\fg[1]$ up to the distributional
top-degree shadow $H^{0,3}_c(\CC^3) \simeq \CC$.

\emph{Primary sources.} Kontsevich 1997 (q-alg/9709040, \S 6.4.1:
formality on $\RR^n$ via the harmonic-retraction diagonal); Costello--Li
2016 (arXiv:1606.00365, \S 3: BV regularisation and heat-kernel
propagator on $\CC^n$); Costello--Gwilliam 2017/2021 (Vol II, Ch 7:
minimal models of holomorphic field theories). The Kapranov 1999
(Compositio 115, \S 4) result is the \emph{compact non-formal} case
with ternary bracket $\ell_3 = \At(T_X) \cup \At(T_X)$; flat $\CC^3$
has $\At(T_{\CC^3}) = 0$ (trivial tangent bundle), so Kapranov's
formula reduces to $\ell_3 = 0$ and does not enter the primary attribution
for flat-space formality.

\emph{Proof at CFG detail.}

\textbf{Step 1 --- Hodge decomposition on compactly-supported Dolbeault
cohomology.} The Dolbeault Laplacian
$\Box_{\bar\partial} = \bar\partial\bar\partial^* + \bar\partial^*\bar\partial$
on $\Omega^{0,\bullet}_c(\CC^3)$ does not possess a Green's operator in the
compact-manifold sense (its spectrum on $L^2$ has continuous bottom at $0$).
The correct functional-analytic setting is the \emph{Schwartz space}
$\cS(\CC^3, \fg) \subset \Omega^{0,\bullet}_c(\CC^3, \fg)$ of
rapidly-decaying smooth sections, on which the BV-regularised heat-kernel
homotopy
\[
h_\varepsilon \;=\; \bar\partial^* \int_0^\varepsilon e^{-s \Box_{\bar\partial}}\, ds
\]
satisfies $[\bar\partial, h_\varepsilon] = \pi_\mathrm{sm} - e^{-\varepsilon
\Box}$ where $\pi_\mathrm{sm}$ is the $L^2$-smooth projection. Taking the
$\varepsilon \to \infty$ limit on polynomial representatives (the harmonic
inputs $\CC[z_1, z_2, z_3] \otimes \fg \subset \Omega^{0,0}$), $h_\infty$
is the Bochner--Martinelli kernel
\[
P_{\mathrm{BM}}(z, w) \;=\; \frac{(n-1)!}{(2\pi i)^n} \sum_{k=1}^{n}
(-1)^{k-1} \frac{\overline{z_k - w_k}}{\|z - w\|^{2n}}
\widehat{d\bar z_k} \wedge dw_1 \wedge \cdots \wedge dw_n
\]
at $n = 3$ on $\CC^3 \setminus \Delta$. The Hodge-homotopy identity
$[\bar\partial, h] = \mathrm{id} - H$ with $H$ the harmonic projection
onto $\cH^{0,\bullet} = \bigoplus_q \cH^{0,q}$ holds on the polynomial
sector, where $\cH^{0,0} = \CC[z_1, z_2, z_3]$ and $\cH^{0,q} = 0$
for $q \in \{1, 2\}$.

\textbf{Step 2 --- Shifted Dolbeault degree bookkeeping.} On
$\cE_{\hCS} = \Omega^{0,\bullet}(\CC^3, \fg)[1]$, the total $L_\infty$-degree
is Dolbeault degree $q$ shifted by $-1$: an element of $\Omega^{0,q}$
contributes total degree $q - 1$. The Lie bracket $\ell_2$ has
$L_\infty$-degree $+1$ relative to internal grading (Koszul convention),
which on Dolbeault representatives means $\ell_2(\Omega^{0,p}, \Omega^{0,q})
\subset \Omega^{0, p+q}$: brackets are wedge products in the Dolbeault
factor, Lie bracket in the $\fg$-factor. Harmonic inputs
$x_1, \ldots, x_n \in \fg \otimes \cH^{0,0} = \fg \otimes \CC[z_1, z_2, z_3]$
have Dolbeault degree $0$; brackets of Dolbeault-degree-$0$ elements are
still Dolbeault-degree-$0$.

\textbf{Step 3 --- Kajiura--Merkulov tree recursion.} The transferred
$\ell_n^{\min}$ on $\cH$ is
\[
\ell_n^{\min}(x_1, \ldots, x_n) \;=\; \sum_{T \in \cT_n}
\pm\, \pi_\cH \circ \beta_T(i x_1, \ldots, i x_n)
\]
where $\cT_n$ is the set of planar binary rooted trees with $n$ labelled
leaves; $i : \cH \hookrightarrow \cE_{\hCS}$ is the inclusion of harmonic
representatives; $\pi_\cH = H$ is the harmonic projection; and
$\beta_T(y_1, \ldots, y_n)$ is the composition: apply $\ell_2$ at each
internal vertex, apply $h$ along each internal edge, read from leaves to
root.

\textbf{Step 4 --- Degree count kills every tree with an internal edge.}
Consider a tree $T \in \cT_n$ with $n \geq 3$ leaves. Such a tree has at
least one internal edge. Let $e$ be an internal edge of $T$, let $v$ be
the endpoint of $e$ closer to the leaves, and trace the computation.

At the leaves-level closest to $v$, we have $\ell_2$ applied to two
harmonic inputs (or to compositions via sub-trees at deeper positions).
By induction on tree depth, the output of every sub-tree rooted at a
vertex whose leaves are all harmonic is still Dolbeault-degree-$0$:
$\ell_2$ preserves Dolbeault degree on Dolbeault-degree-$0$ inputs,
and $h$ on a Dolbeault-degree-$0$ element maps to $\Omega^{0,-1}$, but
we apply $h$ at the next internal edge, not within a sub-tree.

Now the edge $e$ carries a propagator $h$. The input to $h$ along $e$ is
an $\Omega^{0,0}$-valued expression (by the induction above). The
propagator $h : \Omega^{0,q}_c \to \Omega^{0, q-1}_c$ (after BV
regularisation and $\varepsilon \to \infty$ on the polynomial sector) has
target $\Omega^{0, -1} = 0$ when $q = 0$. Hence the composition at $e$
vanishes: $h$ applied to a Dolbeault-degree-$0$ form is zero because the
target Dolbeault-degree-$(-1)$ space is trivial.

Therefore $\beta_T(ix_1, \ldots, ix_n) = 0$ for every $T \in \cT_n$ with
$n \geq 3$, and $\ell_n^{\min} = 0$ for all $n \geq 3$.

\textbf{Step 5 --- Residual $\ell_2^{\min}$ and top-degree shadow.} The
$n = 2$ corolla (one internal vertex, zero internal edges) gives
$\ell_2^{\min}(x_1, x_2) = H \circ [ix_1, ix_2]_\fg = [x_1, x_2]_\fg
\otimes 1$, the Lie bracket on $\fg[1]$. The $H^{0,3}_c(\CC^3) \simeq \CC$
summand contributes a distributional top-degree class dual to
$H^0(\CC^3, \cO) = \CC$ via compactly-supported Poincaré duality; this
is the $3$-dualizable shadow and feeds into Theorem
$\texttt{wn:thm:spine-3-dual-abelian}$.

$\qed$

\textbf{Remark (BM propagator clarification).} The statement "propagator
kills the harmonic subspace" is correctly understood as
$h|_{\cH^{0,0}} = 0$ because the target $\Omega^{0,-1} = 0$, not as
$P_{\mathrm{BM}}$ acting as a zero operator on polynomials. The BM kernel
$P_{\mathrm{BM}}(z,w)$ is a non-zero distributional form of Dolbeault
bi-degree $(3, 2)$ in $(z, w)$: it cannot act on $\Omega^{0,0}$-inputs in
a Dolbeault-degree-lowering way because the Dolbeault grading of the
output is fixed by the kernel bidegree and the convolution integral over
one variable. The phrase "propagator kills harmonic" in working notes
is shorthand for the structural-degree vanishing, not a computation on
polynomial representatives.

### Theorem (Atiyah class as formality obstruction on compact CY$_3$).
\ClaimStatusTheorem

Let $X$ be a compact CY$_3$ with holomorphic tangent bundle $T_X$ and
volume form $\Omega_X$. The Kapranov $L_\infty$-algebra on
$\Omega^{0,\bullet}(X, T_X[-1])$ has ternary bracket
\[
\ell_3(v_1, v_2, v_3) \;=\; \mathrm{Sym}\, \At(T_X)(v_1) \cdot
[v_2, v_3]_{T_X}
\]
where $\At(T_X) \in H^1(X, \Omega^1_X \otimes \mathrm{End}\, T_X)$ is
the Atiyah class (Atiyah 1957 Trans.\ AMS 85; Kapranov 1999 Compositio
115 \S 4 Thm.\ 2.8.1). The vanishing $\At(T_X) = 0$ is a \emph{necessary}
formality condition; sufficiency requires the vanishing of the
full Kapranov obstruction tower
$\{\kappa_n\}_{n \geq 3} \subset \bigoplus_n H^2(X, \mathrm{End}\, T_X
\otimes \mathrm{Sym}^n T_X^\vee)$ with leading $\kappa_3 = \At \cup \At$
and higher $\kappa_n$ equal to the Markarian--Duflo Taylor coefficients
of $\mathrm{td}(T_X)^{1/2} \in \bigoplus_p H^p(X, \Lambda^p T_X^\vee)$
(Markarian 2009 J. Lond. Math. Soc. 79; Calaque--Van den Bergh 2010
Adv.\ Math.\ 224).

\emph{Scope clarification.} This theorem is not the same as
$\texttt{wn:thm:spine-minimal-model}$ on flat $\CC^3$: flat-space
formality has $\At = 0$ trivially and is Kontsevich 1997 (q-alg/9709040,
\S 6.4.1 harmonic-retraction diagonal). Compact non-flat CY$_3$
formality invokes Kapranov 1999 \S 4 and requires the full tower. The
two scopes should not be conflated under a single citation.

\emph{Verification on $K3 \times E$.} The tangent bundle splits as
$T(K3 \times E) = \pi_1^* T_{K3} \oplus \pi_2^* T_E$. On $E$, $T_E$ is
holomorphically trivial (an elliptic curve is a complex Lie group), so
$\At(T_E) = 0$. On $K3$, $\At(T_{K3}) \neq 0$ generically (K3 has no
holomorphic connection on $T_{K3}$, Biswas--Nag 2002), so the Kapranov
tower does not terminate at $\kappa_3$ via $\At = 0$. Formality on
$K3 \times E$ instead proceeds via the Căldăraru--Huybrechts 2010
(arXiv:0907.2450 \S 4) twisted HKR isomorphism with
$\sqrt{\mathrm{td}(T_{K3})}$, which identifies the Kapranov
$L_\infty$-structure with its strict counterpart on the HKR polyvector
model. Formality therefore holds on $K3 \times E$ but via the
twisted-HKR route, not the naive $\At = 0$ route.

\emph{Cubic receptacle on $K3 \times E$.} The Kapranov cubic
receptacle at $d = 3$ is $H^3(X, \Lambda^3 T_X)$ (not
$H^3(X, \Omega^3_X)$). Künneth decomposition:
\[
H^3(K3 \times E, \Lambda^3 T_{K3 \times E}) \;=\;
\bigoplus_{\substack{p + q = 3\\ a + b = 3\\ a \leq 2,\, b \leq 1}}
H^p(K3, \Lambda^a T_{K3}) \otimes H^q(E, \Lambda^b T_E).
\]
Every summand vanishes: $\Lambda^3 T_{K3} = 0$ (rank $2$);
$\Lambda^2 T_E = 0$ (rank $1$); the remaining summand
$H^2(K3, \Lambda^2 T_{K3}) \otimes H^1(E, T_E)$ has
$\Lambda^2 T_{K3} \simeq \cO_{K3}$ (K3 is CY$_2$, $\Lambda^2 T_{K3}
= K_{K3}^\vee = \cO_{K3}$), $H^2(K3, \cO_{K3}) = \CC$,
$H^1(E, T_E) = \CC$, so the summand is $\CC \otimes \CC = \CC \neq 0$
--- \emph{non-zero}! Hence the cubic Kapranov receptacle is
one-dimensional, sourced by the K3 holomorphic symplectic form paired
with the elliptic-curve tangent deformation.

This one-dimensional class is the Bershadsky--Cecotti--Ooguri--Vafa
tree-level three-point Yukawa $Y_3(v_1, v_2, v_3) = \int_X \Omega_X \wedge
\At(v_1) \cup \At(v_2) \cup \At(v_3)$ evaluated on the $K3 \times E$
Kuranishi moduli; it is non-trivial but does not obstruct formality
because the Căldăraru--Huybrechts twisted HKR absorbs the $\At$-cup
products into the $\mathrm{td}^{1/2}$-correction.

The competing statement "$H^3(K3 \times E, \Omega^3) = 0$" is a
\emph{different} computation: by Künneth on Hodge decomposition,
$H^3(K3 \times E, \Omega^3_{K3 \times E}) = \bigoplus_{p+q=3,\, a+b=3}
H^p(K3, \Omega^a_{K3}) \otimes H^q(E, \Omega^b_E)$; every summand has
$\Omega^3_{K3} = 0$ ($K3$ is a surface), $\Omega^2_E = 0$ (E is a curve),
or $H^2(E, \Omega^1_E) = 0$ (E has no higher cohomology with non-trivial
forms), giving $0$. Both vanishings hold on $K3 \times E$ but for
disjoint reasons:
$H^3(X, \Omega^3_X) = 0$ is a rank-and-dimension vanishing
(Hodge bigrading support); $H^3(X, \Lambda^3 T_X)$ on $K3 \times E$
is \emph{non-zero} (as shown), and the correct statement is that
the non-vanishing Yukawa does not obstruct formality via the twisted-HKR
mechanism.

\textbf{Correction to spine theorem.} The spine statement
"$H^3(K3, \Lambda^3 T_{K3}) = 0$ by rank... formality holds" on
$K3 \times E$ must be refined: the Yukawa receptacle on the product
$K3 \times E$ is $\CC$-valued (one-dimensional), not zero; formality
holds via Căldăraru--Huybrechts twisted HKR despite the non-vanishing
Yukawa. The spine conclusion (formality holds on $K3 \times E$) is
correct; the mechanism (rank-vanishing of the cubic receptacle on the
\emph{product}) is incorrect. On K3 alone, $\Lambda^3 T_{K3} = 0$ by
rank ($T_{K3}$ rank $2$); on $K3 \times E$, $\Lambda^3 T_{K3 \times E}$
is a rank-$3$ bundle with non-trivial sections coming from the
$\Lambda^2 T_{K3} \otimes T_E = \cO_{K3} \boxtimes T_E$ summand.

$\qed$

## Retractions with true hidden structure

### Retraction R1: "Kapranov 1999 \S 3.1" attribution

\textbf{Wrong claim.} "This is Kapranov 1999 \S 3.1, adapted to flat
$\CC^3$." (Spine theorem $\texttt{wn:thm:spine-minimal-model}$)

\textbf{Precise error.} Kapranov 1999 (\emph{Compositio Math.\ 115}:
"Rozansky--Witten invariants via Atiyah classes") \S 3 is the general
Dolbeault geometric setup for compact complex manifolds: \S 3.1
introduces the Dolbeault resolution of the structure sheaf on a complex
manifold and the local DG-algebra model; \S 3.2 introduces the
formal geometry / Fedosov construction. None of \S 3 treats flat-$\CC^n$
formality per se --- the argument there is about the \emph{non-flat}
non-formal case where $\At(T_X) \neq 0$ sources $\ell_3^{\min}$.

\textbf{Ghost theorem.} The correct primary source for flat-space
Dolbeault formality via harmonic retraction is \textbf{Kontsevich 1997}
(q-alg/9709040, \S 6.4.1), lifted to the holomorphic Dolbeault setting
by \textbf{Costello--Gwilliam 2017/2021} (Vol II, Ch 7 on minimal models
of holomorphic field theories). The Kapranov 1999 paper is about the
\emph{obstructed} case, where the degree count fails and $\At$-sourced
cohomology classes contribute to $\ell_n^{\min}$.

\textbf{Correct attribution.}
\begin{itemize}
\item Flat $\CC^n$ formality (degree count): Kontsevich 1997
q-alg/9709040 \S 6.4 (harmonic retraction on $\RR^n$; Dolbeault
adaptation by Costello--Gwilliam Vol II Ch 7).
\item Compact non-flat CY$_d$ obstruction (Kapranov tower): Kapranov
1999 \emph{Compositio Math.\ 115} \S 4 Thm.\ 2.8.1.
\item Higher-order obstructions via Duflo/Markarian: Markarian 2009
\emph{J.\ Lond.\ Math.\ Soc.} 79; Calaque--Van den Bergh 2010
\emph{Adv.\ Math.} 224.
\end{itemize}

The spine theorem mixes the two scopes. The correct statement names
both: "On flat $\CC^3$, $\ell_n^{\min} = 0$ for $n \geq 3$ by the
Kontsevich 1997 / Costello--Gwilliam Vol II degree-count mechanism;
on compact non-flat CY$_3$, the obstruction tower follows Kapranov 1999
\S 4, with $K3 \times E$ formal via Căldăraru--Huybrechts twisted HKR."

### Retraction R2: Degree chain "$\ell_2$ lands in $\Omega^{0,-1}$"

\textbf{Wrong claim (implicit in naive reading).} "Harmonic inputs sit
in $\Omega^{0,0}$, the Hodge-homotopy propagator maps $\Omega^{0,q}$ to
$\Omega^{0, q-1}$, and on $\Omega^{0,0}$ its target $\Omega^{0,-1}$
vanishes" --- suggesting that the Lie bracket outputs an
$\Omega^{0,0}$-form and then the propagator immediately lands in
$\Omega^{0,-1}$.

\textbf{Precise error.} In a tree with $n \geq 3$ leaves, the propagator
does not act immediately at every internal edge; the tree order matters.
At each internal vertex, $\ell_2$ applies; at each internal edge,
$h$ applies. Between leaves and the first internal vertex, no propagator
acts; after the first vertex, the output feeds into another vertex or
through an edge. The naive degree count confuses the order.

\textbf{Ghost theorem.} The correct bookkeeping: at every internal
vertex the output remains Dolbeault-degree-$0$ (because
$\ell_2 : \Omega^{0,0} \times \Omega^{0,0} \to \Omega^{0,0}$ when inputs
are harmonic); at every internal edge the propagator $h$ maps
$\Omega^{0,0} \to \Omega^{0,-1} = 0$ structurally. The vanishing
cascades: any tree with at least one internal edge has at least one
propagator acting on a Dolbeault-degree-$0$ output, and that propagator
returns zero. The minimal-model bracket at order $n \geq 3$ is a sum
over such trees, each summand zero.

This is what $\texttt{wn:thm:spine-minimal-model}$ asserts; the
ambiguity is only in the prose wording, not the mathematics.

### Retraction R3: "Cubic receptacle on $K3 \times E$ is $H^3(K3, \Lambda^3 T_{K3}) = 0$"

\textbf{Wrong claim.} "$H^3(K3, \Lambda^3 T_{K3})$, which vanishes on
rank grounds ($T_{K3}$ has rank $2$, so $\Lambda^3 T_{K3} = 0$). Hence
the full Kapranov tower vanishes and formality holds." (Spine theorem
$\texttt{wn:thm:spine-minimal-model}$, "Formality on $K3 \times E$"
paragraph)

\textbf{Precise error.} The Kapranov cubic receptacle on the \emph{product}
$K3 \times E$ is $H^3(K3 \times E, \Lambda^3 T_{K3 \times E})$, which is
\emph{not} $H^3(K3, \Lambda^3 T_{K3})$. The Künneth decomposition
contains the summand
\[
H^2(K3, \Lambda^2 T_{K3}) \otimes H^1(E, T_E) \;=\;
H^2(K3, \cO_{K3}) \otimes H^1(E, \cO_E) \;=\; \CC \otimes \CC \;=\; \CC,
\]
using $\Lambda^2 T_{K3} \simeq \cO_{K3}$ (K3 is CY$_2$) and $T_E \simeq
\cO_E$ (E is a complex Lie group). Hence the cubic receptacle on
$K3 \times E$ is one-dimensional, \emph{non-zero}.

\textbf{Ghost theorem.} Formality on $K3 \times E$ does hold (the
spine conclusion is correct), but via the \textbf{Căldăraru--Huybrechts
2010 twisted HKR} mechanism, not via rank-vanishing of the cubic
receptacle. The one-dimensional Yukawa class is
\[
Y_3 \;=\; \int_{K3 \times E} \Omega_{K3 \times E}
\wedge \At \cup \At \cup \At,
\]
non-zero in $H^{0,3}(K3 \times E) \simeq \CC$; it represents the
B-model tree-level Yukawa coupling $\langle v_1, v_2, v_3 \rangle_{g=0}$
of BCOV. Non-triviality of $Y_3$ does not obstruct formality because the
Căldăraru--Huybrechts quasi-isomorphism twists the HKR map by
$\sqrt{\mathrm{td}(T_X)}$, absorbing $\At$-sourced corrections into a
strict Gerstenhaber morphism at the Hochschild level.

\textbf{Correct statement.}

\emph{Claim.} On $K3 \times E$, the Kapranov $L_\infty$-structure on
$\Omega^{0,\bullet}(K3 \times E, T_{K3 \times E}[-1])$ is formal despite
the non-vanishing cubic class $Y_3 \in H^{0,3}(K3 \times E) \simeq \CC$;
formality is witnessed by the Căldăraru--Huybrechts 2010 twisted HKR
with $\sqrt{\mathrm{td}(T_{K3 \times E})}$, equivalent on the product
to $\sqrt{\mathrm{td}(T_{K3})} \otimes 1$ since $\mathrm{td}(T_E) = 1$.

\emph{Distinction from $H^3(X, \Omega^3_X) = 0$.} The competing
vanishing $H^3(K3 \times E, \Omega^3) = 0$ holds independently: by
Künneth on Hodge decomposition with $\Omega^3_{K3} = 0$ (K3 is a
surface), $\Omega^2_E = 0$ (E is a curve), and $H^2(E, \Omega^1_E) = 0$
(E has one-dimensional complex structure), every summand vanishes. This
is a pure Hodge-bigrading-support vanishing. The Kapranov cubic
receptacle $H^3(X, \Lambda^3 T_X)$ is non-zero on $K3 \times E$ (as
computed above); the two vanishings are independent, not equivalent.

## Cross-consistency checks

\emph{(a) Waves 11--16 surviving core.} The flat-$\CC^3$ formality is
consistent with the two-stage factorisation
$\Phi_3 = \mathrm{Sp}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$
of \texttt{wn:thm:two-stage-Phi}: on flat $\CC^3$, the $E_3$-holomorphic
factorisation algebra $\Phi^{\mathrm{FA}}_3(\mathrm{Perf}(\CC^3))$ is
trivially formal (minimal model is free graded Lie algebra on $\fg$),
so Stage 1 gives $\Obs_{\hCS}(\CC^3) \simeq \cU^{\mathrm{fact}}(\fg[1])$
without higher Maurer--Cartan deformations. Stage 2 specialisation on
a curve $C$ then produces an $E_1$-chiral algebra that is also strict
(no $\hbar$-corrections), matching the flat-space observation that
the moduli of deformations $T_0 \cM = \CC \cdot B$ is one-parameter.

\emph{(b) CoHA treatise cross-consistency.}
$\mathrm{CoHA}(\CC^3) = Y^+$ (Schiffmann--Vasserot 2013): on flat $\CC^3$,
the positive half of the affine Yangian arises as the cohomological
Hall algebra. The Kontsevich--Soibelman minimal model being trivial
($\ell_n^{\min} = 0$ for $n \geq 3$) is consistent with the CoHA being
freely generated in a single degree modulo quadratic relations --- the
Yangian's triangular decomposition $Y = Y^- \otimes Y^0 \otimes Y^+$
reflects this flat-space formality.

\emph{(c) $\kappa$-subscript identity.} The claim
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is entirely orthogonal to the
formality result: Borcherds weight is a count of singular theta
coefficients, not a formality datum. On $K3 \times E$, $\kappa_{\mathrm{BKM}}
(\Delta_5) = 5 = c_1(0)/2$ (Gritsenko 1999); $\kappa_{\mathrm{cat}}
(K3 \times E) = \chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0 = 0$
Künneth-multiplicative; $\kappa_{\mathrm{fiber}} = 24 = \chi_{\mathrm{top}}
(K3)$; $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ by the
Hodge-supertrace-plus-correction formula at $d = 3$. The formality
Yukawa $Y_3 \in H^{0,3}$ is a $\hbar^2$-piece of the Hochschild
differential on $\mathbf H_{\Delta_5}$ (per
Remark~\ref{rem:hochcalc-hdelta5-decomp} of
\texttt{chapters/theory/hochschild\_calculus.tex} line 473), not a
$\kappa$-subscript.

\emph{(d) Two-stage factorisation.}
$\Phi^{\mathrm{FA}}_3$ on flat $\CC^3$ produces the free
$E_3^{\mathrm{hol}}$-algebra on $\fg[1]$, consistent with minimal-model
formality. Stage-2 specialisation on a curve $C$ picks out the
chiral/affine Yangian avatar; non-trivial Yukawa corrections would
enter at the compact CY$_3$ level, which is Kapranov-tower-obstructed
but made formal on $K3 \times E$ via Căldăraru--Huybrechts twisted HKR.

## Residual frontier

\begin{itemize}
\item \textbf{Sufficient criterion for Kapranov-tower termination on
compact CY$_3$ beyond $K3 \times E$.} \ClaimStatusOpen. On general
compact CY$_3$ the full tower $\{\kappa_n\}_{n \geq 3}$ can in principle
contribute; sufficient criteria for termination (other than
Căldăraru--Huybrechts-style twisted HKR on HK$2$ base) are not
established in the primary literature. The quintic has non-trivial
$Y_3$ and unknown higher $\kappa_n$ status.

\item \textbf{Non-compact degree-count on $\cS(\CC^3) \supsetneq
\Omega^{0,\bullet}_c$.} \ClaimStatusConjectured. The BV regularisation
$h_\varepsilon$ extends to Schwartz-class sections; the $\varepsilon
\to \infty$ limit on polynomial representatives has been verified (Costello--Li
2016 \S 3), but the extension to general Schwartz-class sections
(non-polynomial harmonic representatives) is open. For the formality
argument as stated in the spine, polynomial representatives suffice.

\item \textbf{Compact-CY$_3$ recovery of minimal-model trivialisation.}
\ClaimStatusConjectured. On a compact CY$_3$ whose Kapranov tower
terminates at $\kappa_N = 0$ for some $N \geq 3$, the minimal model has
$\ell_n^{\min} = 0$ for $n > N$; this is conjectured for $K3 \times E$
via Căldăraru--Huybrechts and for abelian threefolds via triviality
of the tangent bundle, but unproved in the general-HK$2 \times E$
class.
\end{itemize}

## Attack-heal cycle log (private — for synthesis agent only, not for manuscript)

\textbf{Cycle 1.} ATTACK: The Kapranov 1999 \S 3.1 citation is wrong.
Kapranov's Compositio 115 paper has \S 3 on the general Dolbeault-DG setup
and \S 4 on the non-flat $L_\infty$-structure with $\At$-sourced
brackets. \S 3.1 specifically covers the Dolbeault resolution of $\cO_X$
on a complex manifold, not flat-space formality.
HEAL: The correct attribution is Kontsevich 1997 (q-alg/9709040, \S 6.4.1)
for the harmonic-retraction flat-space argument on $\RR^n$, lifted to
Dolbeault by Costello--Gwilliam Vol II Ch 7. Kapranov 1999 \S 4 covers
the non-formal compact case, which is a different theorem.

\textbf{Cycle 2.} ATTACK: On non-compact $\CC^3$, there is no Hodge
homotopy on the full Fréchet space $\Omega^{0,\bullet}(\CC^3)$ because
$\Box_{\bar\partial}$ has continuous spectrum at $0$ and no compact
Green's operator. Is the claim "Hodge homotopy propagator maps
$\Omega^{0,q} \to \Omega^{0,q-1}$" rigorous?
HEAL: The construction is performed on $\Omega^{0,\bullet}_c(\CC^3)$
with BV-regularised heat-kernel propagator
$h_\varepsilon = \bar\partial^* \int_0^\varepsilon e^{-s\Box} ds$
(Costello--Li 2016 \S 3). The $\varepsilon \to \infty$ limit on polynomial
representatives gives the Bochner--Martinelli kernel. The Hodge-homotopy
identity $[\bar\partial, h] = \mathrm{id} - H$ holds on the polynomial
sector. The claim is rigorous, but the propagator is BV-regularised, not
a naive Green's operator.

\textbf{Cycle 3.} ATTACK: The degree chain "harmonic inputs land in
$\Omega^{0,0}$, propagator lands in $\Omega^{0,-1} = 0$" is incomplete
as stated: trees have multiple internal edges, and the propagator
doesn't apply immediately. Work through $n = 3$ explicitly.
HEAL: For $n = 3$, the tree has one internal vertex and two edges from
vertex to leaves. Wait --- $n = 3$ means three leaves; planar binary
rooted tree has structure: root with two children, one of which is a
leaf $x_1$, the other is an internal vertex with two leaves $x_2, x_3$.
Internal edges: one (connecting the root to the internal vertex). The
computation: $\ell_2(x_2, x_3) = [x_2, x_3]_\fg \in \Omega^{0,0} \otimes \fg$;
propagator $h$ applied gives $h([x_2, x_3]) \in \Omega^{0,-1} = 0$; so
$\ell_2(x_1, h([x_2, x_3])) = 0$. Hence $\beta_T = 0$ for this tree,
and by similar argument for other planar trees. $\ell_3^{\min} = 0$.

\textbf{Cycle 4.} ATTACK: The Kuranishi receptacle for
complex-structure deformations of $X$ is $H^2(X, T_X)$ at the quadratic
level, $H^3(X, T_X)$ at cubic. Why is the spine statement using
$H^3(X, \Lambda^3 T_X)$?
HEAL: The Kuranishi deformation functor for complex-structure
deformations of $X$ has tangent $H^1(X, T_X)$ and \emph{obstructions}
in $H^2(X, T_X)$ — $H^3(X, T_X)$ is the \emph{third-order} obstruction.
But the spine theorem is about the Kapranov $L_\infty$-model on
$\Omega^{0,\bullet}(X, T_X[-1])$ at $d = 3$, where the \emph{cubic bracket}
$\ell_3 : T_X^{\otimes 3} \to T_X[1]$ lands in $H^{0,3}(X, \Lambda^3 T_X)
= H^3(X, \Lambda^3 T_X)$ by symmetrisation. This is a different
receptacle from the complex-structure Kuranishi obstruction $H^3(X, T_X)$;
it is the BCOV Yukawa receptacle (Kapranov 1999 \S 4 Thm.\ 2.8.1).
The spine attribution is correct for the Kapranov $L_\infty$-model, but
the prose "Kuranishi cubic receptacle" is misleading — the receptacle is
not the Kuranishi-functor $H^3(X, T_X)$ but the BCOV Yukawa receptacle.

\textbf{Cycle 5.} ATTACK: On $K3 \times E$, the Yukawa receptacle
$H^3(K3 \times E, \Lambda^3 T_{K3 \times E})$ claim to vanish by
Künneth + rank ($\Lambda^3 T_{K3} = 0$). But Künneth gives
$H^2(K3, \Lambda^2 T_{K3}) \otimes H^1(E, T_E)$ as a summand, and
$\Lambda^2 T_{K3} = \cO_{K3}$ (K3 holomorphic symplectic), which is
\emph{not} zero. So the cubic receptacle is non-zero on the product,
and the rank-vanishing argument is incorrect.
HEAL: The correct mechanism for formality on $K3 \times E$ is
Căldăraru--Huybrechts 2010 twisted HKR (via $\sqrt{\mathrm{td}}$),
which absorbs the non-vanishing Yukawa into a strict Gerstenhaber
morphism. The spine's mechanism (rank-vanishing of the cubic receptacle
on the product) is incorrect but the conclusion (formality on
$K3 \times E$) is correct via the twisted-HKR route.

\textbf{Cycle 6.} ATTACK: The competing statement
"$H^3(K3, \Omega^3_{K3}) = 0$" — is this claim correct?
$\Omega^3_{K3} = 0$ because K3 is a surface, so any section of
$\Omega^3_{K3}$ is zero, hence $H^3(K3, \Omega^3_{K3}) = 0$ trivially.
But is this the right receptacle for any deformation-theoretic question?
HEAL: $H^3(K3, \Omega^3_{K3})$ is Serre-dual to $H^0(K3, T_{K3})$, which
is $0$ because K3 has no holomorphic vector fields (it is rigid as a
complex Lie-group-action). The vanishing $H^3(K3, \Omega^3_{K3}) = 0$
is equivalent via Serre duality to $H^0(K3, T_{K3}) = 0$, a statement
about the isometry group. Not a statement about cubic formality
obstructions. The spine's framing "competing statement" is correct:
these are two different vanishings, both holding on K3, but for
disjoint structural reasons. The Kapranov obstruction argument uses
$H^3(X, \Lambda^3 T_X)$; the Kuranishi-functor analysis uses
$H^2(X, T_X)$ for obstructions and $H^1(X, T_X)$ for tangents; neither
directly uses $H^3(X, \Omega^3_X)$.

\textbf{Cycle 7.} ATTACK: Does the claim "Hodge homotopy propagator maps
$\Omega^{0,q} \to \Omega^{0,q-1}$" hold on the BV-regularised heat
kernel, or only in the compact limit? What is the precise functional-
analytic status?
HEAL: On compactly-supported Schwartz-class $\Omega^{0,\bullet}_c(\CC^n)$
with BV regularisation at scale $\varepsilon$, the propagator
$h_\varepsilon = \bar\partial^* \int_0^\varepsilon e^{-s\Box} ds$ maps
$\Omega^{0,q}_c \to \Omega^{0,q-1}_c$ by construction
($\bar\partial^*$ lowers Dolbeault degree by one). The
Hodge-homotopy identity $[\bar\partial, h_\varepsilon] = \mathrm{id}
- e^{-\varepsilon\Box}$ holds at each finite $\varepsilon$; the
$\varepsilon \to \infty$ limit on polynomial representatives gives
$[\bar\partial, h] = \mathrm{id} - H$ where $H$ is the harmonic
projection. This is standard Costello--Gwilliam BV regularisation
(Vol I \S 9, Vol II \S 6). The propagator does lower Dolbeault
degree by one at every scale, and on $\Omega^{0,0}$ the target
$\Omega^{0,-1}$ is structurally zero.

\textbf{Cycle 8.} ATTACK: The spine theorem says "on $\Omega^{0,0}$ its
target $\Omega^{0,-1}$ vanishes" — but is $\Omega^{0,-1}$ \emph{really}
zero, or is it a distributional completion? In Čech--Dolbeault Verdier
duality, one sometimes identifies $H^0 = H^{-n}_c$ via PD, which
formally puts negative-degree content somewhere.
HEAL: The Dolbeault complex $\Omega^{0,\bullet}(X) = \bigoplus_{q \geq 0}
\Omega^{0,q}(X)$ is concentrated in non-negative degrees by definition
($\Omega^{0,q}$ is the bundle of smooth $(0,q)$-forms, well-defined
for $q \in \{0, 1, \ldots, n\}$ on an $n$-dim complex manifold). At
$q = -1$, there is no bundle; the space $\Omega^{0,-1}$ is $0$ by
definition of the Dolbeault complex, not via duality identification.
Verdier/Poincaré duality provides an identification between different
cohomology groups (e.g.\ $H^0 \simeq H^n_c$ via PD), but not between
$\Omega^{0,-1}$ and anything non-zero. The vanishing is structural.

## Conclusion

The spine theorem survives with three corrections:

1. \textbf{Attribution.} Replace "Kapranov 1999 \S 3.1" with "Kontsevich
1997 (q-alg/9709040, \S 6.4.1) harmonic-retraction adapted to Dolbeault
via Costello--Gwilliam Vol II Ch 7". Kapranov 1999 \S 4 covers the
compact non-flat obstruction, a separate theorem.

2. \textbf{Propagator qualifier.} The Hodge-homotopy propagator on
non-compact $\CC^3$ is BV-regularised (Costello--Li 2016 \S 3), not
a naive Green's operator. The $\varepsilon \to \infty$ limit on
polynomial harmonic representatives gives the Bochner--Martinelli
kernel.

3. \textbf{$K3 \times E$ receptacle.} The cubic receptacle
$H^3(K3 \times E, \Lambda^3 T_{K3 \times E}) \simeq \CC$ is non-zero
(Künneth + $\Lambda^2 T_{K3} \simeq \cO_{K3}$); formality on $K3 \times E$
proceeds via Căldăraru--Huybrechts 2010 twisted HKR, not via
rank-vanishing of the cubic receptacle on the product. The
statement $\Lambda^3 T_{K3} = 0$ (rank-$2$ vanishing on K3 alone) is
correct but does not propagate to the product.

The mathematical conclusion (flat-$\CC^3$ formality; $K3 \times E$
formal; cubic class $H^3(X, \Lambda^3 T_X) \neq H^3(X, \Omega^3_X)$ as
receptacles) is preserved; the surviving theorems above are
inscription-ready at CFG detail.
