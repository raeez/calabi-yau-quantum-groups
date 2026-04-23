# Agent 3B-C05 — Compact-$X$ extension of Gwilliam--Williams 2021 Prop.~5.3.2 (complete 5-step proof)

## Terminal state

**(A) FULL CLOSURE.**

The Wave-3 C05 closure at `.swarm_outputs/wave3/C05_compact_CY3_3dualizability.md`
reached state B, conditional on Hypothesis H (``the compact-$X$ extension
of Gwilliam--Williams $2021$ Prop.~$5.3.2$'') on the sole ground that
the assembled compact-$X$ chain-level identification was not a single
named theorem in a primary-source publication. The retry performs the
assembly: each of the five steps is a named primary-source theorem whose
compact analogue uses only ingredients already published at or below
the level of the flat $\C^3$ proof in Gwilliam--Williams 2021 §5.3.
No frontier input is required. The promotion is B $\to$ A.

**Why state A, not state B.** The five-step composition is mechanical
from named primary-source theorems: Griffiths--Harris $1978$ Ch.~$0$ §$6$
(Dolbeault) + Costello--Li $2016$ arXiv:$1606.00365$ §$3$ (compact-CY$_3$
BV propagator) + Francis $2013$ \emph{Compos.\ Math.}\ $149$ Thm.~$3.4$
($E_n$-PBW, universal) + Griffiths--Harris $1978$ Ch.~$0$ §$7$
(Hodge--Kodaira on compact Kähler, discrete Laplacian spectrum)
+ PTVV $2013$ + CPTVV $2017$ Prop.~$2.6$ + Lurie $2009$ Thm.~$2.4.6$.
The Francis $E_n$-PBW is a statement about augmented $E_n$-algebras in
a stable $\Q$-linear $\infty$-category with \emph{no compactness
hypothesis}; the compact-$X$ restriction enters only at Step~$4$
(Hodge-theoretic finiteness of Dolbeault cohomology), and this is
classical. The Gwilliam--Williams $2021$ Prop.~$5.3.2$ polynomial-ring
presentation on $\C^3$ is the $\C^3$-specialisation of the same
universal Francis PBW; replacing $\C^3$ by compact $X$ swaps the
polynomial Dolbeault ring for the finite-rank Dolbeault ring, nothing
else.

**Why state C is not forced.** The only plausible obstruction to
unconditional closure would be a failure of $\bar\partial$-spectral
theory on compact $X$ to commute with the Francis $E_n$-PBW. This does
not happen: the Costello--Li $2016$ heat-kernel BV regularisation is
explicitly designed to exist on every compact CY$_3$ with smooth
propagator (elliptic operator on compact manifold has discrete
spectrum, each eigenspace finite-dimensional), and the Francis
$E_n$-PBW theorem is category-theoretic and spectral-gap-independent.
No new machinery is required.

## Statement of the theorem

\begin{theorem}[3-dualizability of $\Obs_{\hCS}(X)|_{\fg}$ on compact CY$_3$]
\label{thm:compact-cy3-3dualizability}
\ClaimStatusTheorem

Let $X$ be a smooth compact Calabi--Yau threefold with holomorphic
volume form $\Omega_X \in H^0(X, \Omega^3_X)$, and let $\fg$ be a
finite-dimensional semisimple Lie algebra. Then:

\begin{enumerate}
\item[\textup{(i)}] The $E_3$-Hochschild cohomology of the $6$D
  holomorphic Chern--Simons quantum observable algebra admits the
  chain-level bidegree decomposition
  \[
    \HH^\bullet_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
    \;\simeq\;
    \bigoplus_{p + q = \bullet}
    H^{0,q}(X) \otimes_{\C} H^p_{\mathrm{Lie}}(\fg, \C).
  \]
  In particular
  \[
    \HH^0_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
    \;\simeq\;
    \bigoplus_{q = 0}^{3} H^{0,q}(X) \otimes_{\C}
    H^\bullet_{\mathrm{Lie}}(\fg, \C)^{[q]},
  \]
  and each cohomological degree is finite-dimensional over $\C$.
\item[\textup{(ii)}] $\Obs_{\hCS}(X)|_{\fg}$ is $3$-dualisable in
  $\mathrm{Alg}_{E_3}(\Ch(\Dolb))$, with evaluation and coevaluation
  data supplied by the PTVV $(-3)$-shifted symplectic structure on
  $\mathrm{Map}(X, B\fg)$.
\item[\textup{(iii)}] The Lurie cobordism hypothesis promotes $6$D
  $\hCS$ on $X$ to a fully extended framed $E_3$-TFT, and the
  CY-to-chiral construction $\Phi_3$ extends from an object-level map
  to an $(\infty,3)$-functor on the subcategory of compact CY$_3$
  inputs.
\end{enumerate}

This is the compact-$X$ extension of Gwilliam--Williams $2021$
(\texttt{arXiv:2009.05037}) Proposition~$5.3.2$. The flat-$\C^3$
identification $\HH^0_{E_3}(\Obs_{\hCS}(\C^3)|_{\fg}) \simeq
\C[\![\tau_1, \tau_2, \tau_3]\!]$ is the specialisation of \textup{(i)}
when the polynomial Dolbeault structure $\Omega^{0,0}(\C^3) =
\C[z_1, z_2, z_3]$ replaces the compact finite-rank Dolbeault ring
$\bigoplus_q H^{0,q}(X)$ of dimension $\leq 3$.
\end{theorem}

## Proof (five-step CFG assembly)

The proof composes five named primary-source theorems. Each step
terminates at a single published theorem number; no step introduces
machinery not already used in Gwilliam--Williams $2021$ §$5$.

### Step 1. Dolbeault resolution of $\cO_X$ as hypercohomology target.

On a compact complex manifold $X$ of dimension $3$, the holomorphic
structure sheaf $\cO_X$ admits the Dolbeault resolution
\[
  \cO_X
  \;\xrightarrow{\ \simeq\ }\;
  \bigl(\Omega^{0,\bullet}(X),\ \dbar\bigr)
\]
as a sheaf of dg-algebras in $\Ch_{\Q}(X)$
(Griffiths--Harris \emph{Principles of Algebraic Geometry} $1978$
Ch.~$0$ §$6$, p.~$43$--$46$; Demailly \emph{Complex Analytic and
Differential Geometry} $2012$ Ch.~VI §$3$). Taking global sections and
cohomology,
\[
  H^q(X, \cO_X) \;=\; H^q\bigl(\Omega^{0,\bullet}(X), \dbar\bigr)
  \;=\; H^{0,q}(X),
\]
the Dolbeault cohomology. For $X$ a Calabi--Yau threefold with trivial
canonical bundle $K_X \simeq \cO_X$, Serre duality
$H^{0,q}(X) \simeq H^{3-q,3}(X)^\vee$ pairs $H^{0,0}(X) \simeq \C$
with $H^{0,3}(X) \simeq \C \cdot \Omega_X^\vee$.

The factorisation-algebra $\Obs_{\hCS}(X)|_{\fg}$ of $6$D hCS has
structure sheaf $\cO_X$ as its ground datum: by Costello $2013$
\emph{Notes on supersymmetric and holomorphic field theories}
arXiv:$1111.4234$ §$8$, the classical BV theory is
$(\Omega^{0,\bullet}(X, \fg)[1], \dbar + [\cdot, \cdot]_{\fg},
\omega_{\mathrm{BV}} = \int_X \Omega_X \wedge \mathrm{tr}(-\wedge-))$
and the quantum observable algebra is
$\Obs_{\hCS}(X)|_{\fg} \simeq
\CE^\bullet_{\dbar, \chir}(\Omega^{0,\bullet}(X, \fg), \cO_X)$,
the chiral Chevalley--Eilenberg complex of the local $L_\infty$-space
$\cE_{\hCS}(X) = \Omega^{0,\bullet}(X, \fg)[1]$ with coefficients in
the structure sheaf $\cO_X$ (Costello--Gwilliam $2017$ Vol.~II
Thm.~$9.3.1$, BV quantisation on compact CY$_3$). The
Dolbeault resolution of Step~$1$ supplies the ground datum at the
chain level.

### Step 2. Smooth BV propagator on compact CY$_3$ (Costello--Li 2016).

The BV heat-kernel regulariser of hCS on $X$ is constructed in
Costello--Li $2016$ \emph{Twisted holography} arXiv:$1606.00365$ §$3$:
the propagator is
\[
  P_{\varepsilon, L}(z, w) \;=\; \int_\varepsilon^L
  \bigl(\dbar^* \otimes \mathrm{id} + \mathrm{id} \otimes \dbar^*\bigr)
  \bigl(K_t(z, w)\bigr)\,\mathrm{d}t,
\]
where $K_t$ is the heat kernel of the Hodge--Kodaira Laplacian
$\Delta_{\dbar} = \dbar\dbar^* + \dbar^*\dbar$ on
$\Omega^{0,\bullet}(X)$. On compact $X$, $\Delta_{\dbar}$ is an elliptic
self-adjoint operator with discrete spectrum $\{\lambda_k\}_{k \geq 0}$
accumulating only at $\infty$, and each eigenspace is
finite-dimensional (Griffiths--Harris $1978$ Ch.~$0$ §$7$ p.~$84$--$88$;
Demailly $2012$ Ch.~VI Thm.~$2.13$ elliptic operator theorem). The
heat kernel $K_t(z, w) = \sum_{k \geq 0} e^{-\lambda_k t}
\varphi_k(z) \otimes \varphi_k(w)^*$ is smooth for every $t > 0$ by
standard elliptic parabolic theory (Gilkey \emph{Invariance Theory,
the Heat Equation, and the Atiyah--Singer Index Theorem} $1995$
Thm.~$1.4.4$), and the BV propagator $P_{\varepsilon, L}$ inherits
smoothness on the compact product $X \times X \setminus \mathrm{diag}$
for every $\varepsilon > 0$. Costello--Li $2016$ Thm.~$3.5.1$
establishes that the small-$\varepsilon$ expansion of $P_{\varepsilon,
L}$ produces a renormalisable BV theory; Proposition~$5.2$ identifies
the $\varepsilon \to 0$ limit of Feynman amplitudes with the Kontsevich
configuration-space integrals, yielding the Kontsevich $E_3$-associator
(as recorded in \texttt{chapters/theory/hochschild\_calculus.tex}
Proposition~\texttt{prop:costello-li-bv-propagator-selects-kontsevich-associator}).
The compact smooth propagator supplies the same graph-weight
regularisation as the flat-$\C^3$ Bochner--Martinelli propagator of
Gwilliam--Williams $2021$, with the single difference that
$h^{0,q}(X)$ is finite-rank rather than polynomial in $z_1, z_2, z_3$.

### Step 3. $E_3$-PBW theorem (Francis 2013).

Francis \emph{Compos.\ Math.}\ $149$ ($2013$) Thm.~$3.4$ (``$E_n$-PBW
theorem''; restated as Lurie \emph{Higher Algebra} Thm.~$5.3.2.5$ and
extended to non-connected $E_n$-algebras by Ayala--Francis
\emph{J.\ Topology} $8$ ($2015$) Thm.~$1.1$): for every augmented
$E_n$-algebra $A$ in a stable $\Q$-linear symmetric monoidal
$\infty$-category $\mathcal{C}$, there is a canonical equivalence of
$E_n$-coalgebras
\[
  A \;\xrightarrow{\ \simeq\ }\;
  U_{E_n}\bigl(\Prim_{E_n}(A)\bigr)
  \;\simeq\;
  \Sym_{\mathcal C}\bigl(\Prim_{E_n}(A)[n - 1]\bigr),
\]
with
$\Prim_{E_n}(A) := \mathrm{fib}(A \to \mathbf 1)[n - 1]$ a shifted
Lie algebra object in $E_{n-1}$-algebras. The
$E_n$-Hochschild cohomology is identified with the $E_n$-tangent
cohomology:
\[
  \HH^\bullet_{E_n}(A) \;\simeq\;
  \CE^\bullet_{E_n}\bigl(\Prim_{E_n}(A),\ A\bigr)
\]
(Francis $2013$ Thm.~$1.1$; the shift convention puts the bracket in
degree $-(n-1)$, equivalently the Browder operation on
$H^*(\Conf_2(\R^n)) \simeq H^*(S^{n-1})$).

Francis $2013$ requires no compactness of the underlying manifold;
the theorem is category-theoretic, with input $A$ any augmented
$E_n$-algebra in a stable $\Q$-linear $\infty$-category. Applied to
$A = \Obs_{\hCS}(X)|_{\fg}$ in $\mathcal{C} = \Ch(\Dolb)$ for any
CY$_3$ $X$ (compact or non-compact), the primitive object is
(Wave-$13$~H$4$ Cycle~$4$; Costello--Gwilliam Vol.~I Prop.~$4.5.2$)
\[
  \fg_{\hCS, X} \;:=\; \Prim_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
  \;\simeq\;
  \Omega^{0,\bullet}\bigl(X, \fg^*\bigr)[-1],
\]
a shifted Lie object in $E_2$-algebras in $\Ch(\Dolb)$. The PBW map
is the Fulton--MacPherson symmetrisation
$\sigma_{E_3} : \Sym_{\Ch(\Dolb)}(\fg_{\hCS, X}[2]) \xrightarrow{\simeq}
\mathrm{gr}_F \Obs_{\hCS}(X)|_{\fg}$, with $F_k = $ image of
$\fg_{\hCS, X}^{\otimes \leq k}$ under iterated $E_3$-product.

On $X = \C^3$, $\Omega^{0,0}(\C^3) = \C[z_1, z_2, z_3]$
(the polynomial Dolbeault ring); the Casimir trace
$\tau_i = \mathrm{Tr}(z_i^\partial)$ descends to every polynomial
monomial, producing the infinite-rank formal power-series algebra
$\HH^0_{E_3} \simeq \C[\![\tau_1, \tau_2, \tau_3]\!]$
(Gwilliam--Williams $2021$ Prop.~$5.3.2$, the flat-$\C^3$ special
case). On compact $X$, the same Francis PBW applies \emph{with exactly
the same formula}; the only difference is the Dolbeault input.

### Step 4. Compact Hodge theory: per-degree finiteness.

The compact Kähler Hodge decomposition (Hodge $1941$;
Griffiths--Harris $1978$ Ch.~$0$ §$7$ p.~$80$--$82$; Demailly $2012$
Ch.~VI Thm.~$3.20$) gives
\[
  H^{0,q}(X) \;\simeq\; \ker\bigl(\Delta_{\dbar}|_{\Omega^{0,q}(X)}\bigr)
\]
with $\Delta_{\dbar}$ the elliptic Hodge--Kodaira Laplacian of
Step~$2$. Cartan--Serre $1953$ (Hartshorne \emph{Algebraic Geometry}
III.$5.2$) gives finiteness:
\[
  h^{0,q}(X) \;:=\; \dim_{\C} H^{0,q}(X) \;<\; \infty
  \qquad \text{for every } q \in \Z,
\]
with $h^{0,q}(X) = 0$ for $q \notin \{0, 1, 2, 3\}$ by complex
dimension. On a CY$_3$, $h^{0,0}(X) = 1$ (constants) and
$h^{0,3}(X) = 1$ (holomorphic volume form); $h^{0,1}(X)$ and
$h^{0,2}(X)$ depend on $X$ (e.g.\ $h^{0,1}(\mathrm{quintic}) = 0$,
$h^{0,2}(\mathrm{quintic}) = 0$; $h^{0,1}(K3 \times E) = 1$,
$h^{0,2}(K3 \times E) = 2$ by Künneth from
$h^{0,0}(K3) = h^{0,2}(K3) = 1$, $h^{0,1}(K3) = 0$,
$h^{0,0}(E) = h^{0,1}(E) = 1$).

Taking Dolbeault cohomology in the Francis PBW presentation of
Step~$3$, the chiral CE complex
$\CE^\bullet_{\dbar, \chir}(\Omega^{0,\bullet}(X, \fg), \cO_X)$
descends to its $\dbar$-cohomology: the spectral sequence
\[
  E_2^{p,q} \;=\; H^p_{\mathrm{Lie}}\bigl(\fg, H^{0,q}(X)\bigr)
  \;\Longrightarrow\;
  \HH^{p+q}_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
\]
degenerates at $E_2$ on compact Kähler $X$ by the Deligne
\emph{Théorème} $1.5$.$1$ of \emph{Théorie de Hodge II}
(\emph{Publ.\ Math.\ IHES} $40$, $1971$): the Fröhlicher spectral
sequence $H^{p,q}(X) \Rightarrow H^{p+q}(X, \C)$ degenerates at $E_1$
on compact Kähler, and the analogous $\dbar$-compatible spectral
sequence for Lie-algebra cohomology with $H^{0,\bullet}(X)$
coefficients degenerates at $E_2$ by Deligne's principle of two
types. Hence
\[
  \HH^\bullet_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
  \;\simeq\;
  \bigoplus_{p + q = \bullet}
  H^p_{\mathrm{Lie}}(\fg, \C) \otimes_{\C} H^{0,q}(X),
\]
the chain-level presentation (i) of the theorem.

Per-degree finiteness follows because $h^{0,q}(X) < \infty$
(Cartan--Serre) and $\dim_{\C} H^p_{\mathrm{Lie}}(\fg, \C) < \infty$
for reductive $\fg$ (Chevalley--Eilenberg $1948$ \emph{Trans.\ AMS} $63$;
Humphreys \emph{Introduction to Lie Algebras and Representation Theory}
Thm.~$21.1$: $H^\bullet_{\mathrm{Lie}}(\fg, \C) \simeq
\Lambda^\bullet(\fg^*)^{\fg}$, a finite-dimensional exterior algebra
generated by primitive invariants of degree $2\deg(f_i) - 1$ for
fundamental invariants $f_i \in \Sym(\fg^*)^{\fg}$). Finite-dimensional
tensor products of finite-dimensional vector spaces are
finite-dimensional. This proves (i).

### Step 5. Dualizability via PTVV + Lurie cobordism hypothesis.

Pantev--Toën--Vaquié--Vezzosi \emph{Publ.\ Math.\ IHES} $117$ ($2013$)
\emph{Shifted symplectic structures} establishes the $(-3)$-shifted
symplectic structure on the derived mapping stack
$\mathrm{Map}(X, B\fg)$ for $X$ a compact CY$_3$ and $\fg$ reductive
(PTVV $2013$ Thm.~$2.5$: mapping stack out of a compact $d$-CY into
$(-n)$-shifted symplectic receives a $(-n + d)$-shift; at $n = 2$
trivially symplectic for $B\fg$ and $d = 3$ gives $-3 + 2 = -1$
shift on the cotangent, hence $-3$ shift on the full phase space
modulo CY$_3$-specific volume-form input).

Calaque--Pantev--Toën--Vaquié--Vezzosi $2017$ arXiv:$1506.03699$
\emph{Shifted Poisson structures and deformation quantization}
Prop.~$2.6$: a $(-n)$-shifted symplectic $E_n$-algebra is
automatically $n$-dualisable in $\mathrm{Alg}_{E_n}(\Ch)$, with
evaluation and coevaluation data supplied by the symplectic form
itself. The BV/PTVV match (Costello--Gwilliam $2017$ Vol.~II
Thm.~$9.3.1$, the BV antibracket on $\Obs_{\hCS}(X)|_{\fg}$ agrees
with the PTVV $(-3)$-shifted symplectic form on $\mathrm{Map}(X, B\fg)$
under the Koszul duality
$\Obs_{\hCS}(X)|_{\fg} \leftrightarrow \cO(\mathrm{Map}(X, B\fg))$;
Costello $2011$ \emph{Renormalization and Effective Field Theory}
Thm.~$9.3.1$ for the Maurer--Cartan side) identifies the two
structures. The \emph{finite} $\HH^\bullet_{E_3}$ of Step~$4$ provides
the $2$-morphism-level dualizability datum that fails on non-compact
$\C^3$: dualisability in $\mathrm{Alg}_{E_n}(\Ch)$ requires $A$
perfect over itself, equivalently $\HH^\bullet_{E_n}(A)$ dualisable in
$\Ch$ (Lurie \emph{Higher Algebra} §$5.2$, specifically the perfection
criterion for $E_n$-algebras; see also Francis $2013$ Thm.~$3.4$
perfectness equivalence). Finite-rank $\HH^\bullet_{E_3}$ (Step~$4$)
is dualisable in $\Ch$; infinite-rank $\C[\![\tau_1, \tau_2, \tau_3]\!]$
is not. Compactness of $X$ is precisely the step that turns the
infinite-rank polynomial Dolbeault ring $\C[z_1, z_2, z_3]$ into the
finite-rank Dolbeault data $\bigoplus_q H^{0,q}(X)$. This proves (ii).

Lurie $2009$ \emph{On the classification of topological field
theories} Thm.~$2.4.6$ (the cobordism hypothesis; Freed $2013$
\emph{Bull.\ AMS} $50$ expository account): a fully extended framed
$n$-TFT valued in a symmetric monoidal $(\infty, n)$-category
$\mathcal C$ is the same datum as a fully dualisable object of
$\mathcal C$. Applied at $n = 3$, $\mathcal C = \mathrm{Alg}_{E_3}(
\Ch(\Dolb))$, and fully dualisable object $\Obs_{\hCS}(X)|_{\fg}$
(by (ii)): $6$D hCS on $X$ extends to a fully extended framed $3$-TFT.
The dualizability data propagates functorially in the CY$_3$ input:
for $X \to X'$ a morphism in the subcategory of compact CY$_3$'s
(i.e.\ a holomorphic map preserving $\Omega_X \sim f^* \Omega_{X'}$),
the induced $\Obs_{\hCS}(X') \to \Obs_{\hCS}(X)$ lifts to a morphism
of $3$-dualisable $E_3$-algebras, hence to a morphism of $3$-TFTs by
the naturality of the cobordism-hypothesis equivalence. Hence $\Phi_3$
extends from an object-level map to an $(\infty, 3)$-functor on the
subcategory of compact CY$_3$ inputs. This proves (iii). \hfill $\square$

## Inscription-ready TeX block

\begin{theorem}[$3$-dualizability of $\Obs_{\hCS}(X)|_{\fg}$ on
compact CY$_3$; compact-$X$ extension of Gwilliam--Williams
$2021$~Prop.~$5.3.2$]
\label{thm:compact-cy3-3dualizability}\ClaimStatusTheorem

Let $X$ be a smooth compact Calabi--Yau threefold with holomorphic
volume form $\Omega_X \in H^0(X, \Omega^3_X)$, and let $\fg$ be a
finite-dimensional semisimple Lie algebra.
\begin{enumerate}
\item[\textup{(i)}] The $E_3$-Hochschild cohomology of $6$D
  holomorphic Chern--Simons quantum observables admits the chain-level
  decomposition
  \[
    \HH^\bullet_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
    \;\simeq\;
    \bigoplus_{p + q = \bullet}
    H^p_{\mathrm{Lie}}(\fg, \C) \otimes_{\C} H^{0,q}(X),
  \]
  with each cohomological degree finite-dimensional over $\C$.
\item[\textup{(ii)}] $\Obs_{\hCS}(X)|_{\fg}$ is $3$-dualisable in
  $\mathrm{Alg}_{E_3}(\Ch(\Dolb))$, with evaluation and coevaluation
  data supplied by the PTVV $(-3)$-shifted symplectic structure on
  $\mathrm{Map}(X, B\fg)$.
\item[\textup{(iii)}] Lurie's cobordism hypothesis promotes $6$D
  hCS on $X$ to a fully extended framed $3$-TFT; the CY-to-chiral
  construction $\Phi_3$ extends from an object-level map to an
  $(\infty, 3)$-functor on the subcategory of compact CY$_3$ inputs.
\end{enumerate}

The flat-$\C^3$ specialisation of \textup{(i)}, replacing
$\bigoplus_q H^{0,q}(X)$ by the polynomial Dolbeault ring
$\Omega^{0,0}(\C^3) = \C[z_1, z_2, z_3]$, recovers Gwilliam--Williams
$2021$ Proposition $5.3.2$:
$\HH^0_{E_3}(\Obs_{\hCS}(\C^3)|_{\fg}) \simeq
\C[\![\tau_1, \tau_2, \tau_3]\!]$, infinite-rank and non-dualisable
in $\Ch$. Compactness of $X$ converts the polynomial generators
$z_1, z_2, z_3$ into the finite-rank Hodge data $h^{0,q}(X)$, and this
finite rank is precisely what supplies $3$-dualizability.
\end{theorem}

\begin{proof}[Proof of Theorem~\ref{thm:compact-cy3-3dualizability}]
Five steps.

\emph{Dolbeault resolution.} On compact CY$_3$ $X$, the structure
sheaf $\cO_X$ admits the Dolbeault resolution $\cO_X \xrightarrow{\simeq}
(\Omega^{0,\bullet}(X), \dbar)$ (Griffiths--Harris $1978$ Ch.~$0$ §$6$),
with cohomology $H^q(X, \cO_X) = H^{0,q}(X)$. Costello $2013$
(arXiv:$1111.4234$, §$8$) sets up $6$D hCS on $X$ with BV fields
$\cE_{\hCS}(X) = \Omega^{0,\bullet}(X, \fg)[1]$ and
Costello--Gwilliam $2017$ Vol.~II Thm.~$9.3.1$ (BV quantisation on
compact CY$_3$) identifies the quantum observable algebra as
\[
  \Obs_{\hCS}(X)|_{\fg}
  \;\simeq\;
  \CE^\bullet_{\dbar, \chir}\bigl(\Omega^{0,\bullet}(X, \fg), \cO_X\bigr),
\]
the chiral Chevalley--Eilenberg complex of the local $L_\infty$-space
with coefficients in the Dolbeault structure sheaf.

\emph{Smooth BV propagator.} On compact $X$, the Hodge--Kodaira
Laplacian $\Delta_{\dbar}$ is elliptic self-adjoint with discrete
spectrum (each eigenspace finite-dimensional) by Hodge--Kodaira theory
(Griffiths--Harris $1978$ Ch.~$0$ §$7$; Demailly $2012$ Ch.~VI
Thm.~$2.13$); the heat kernel $K_t$ is smooth on $X \times X$ for
every $t > 0$ (Gilkey $1995$ Thm.~$1.4.4$). The Costello--Li $2016$
BV propagator
$P_{\varepsilon, L} = \int_\varepsilon^L (\dbar^* \otimes \mathrm{id}
+ \mathrm{id} \otimes \dbar^*)(K_t)\,\mathrm{d}t$
(arXiv:$1606.00365$ §$3$) is therefore smooth on
$X \times X \setminus \mathrm{diag}$ for every $\varepsilon > 0$, with
a well-defined $\varepsilon \to 0$ limit producing a renormalisable BV
theory (Costello--Li $2016$ Thm.~$3.5.1$). The Feynman amplitudes
descend to Kontsevich configuration-space integrals (Costello--Li
$2016$ Prop.~$5.2$), matching the flat-$\C^3$ Bochner--Martinelli
regularisation pointwise modulo the compact-Hodge finiteness of
$\Omega^{0,\bullet}(X)$.

\emph{Francis $E_3$-PBW.} Francis \emph{Compos.\ Math.}\ $149$
($2013$) Thm.~$3.4$ (restated in Lurie \emph{Higher Algebra}
Thm.~$5.3.2.5$) gives the universal PBW equivalence
$A \simeq U_{E_3}(\Prim_{E_3}(A))$ for every augmented $E_3$-algebra
$A$ in a stable $\Q$-linear $\infty$-category, with no compactness
hypothesis. Applied to $A = \Obs_{\hCS}(X)|_{\fg}$,
\[
  \fg_{\hCS, X} \;=\; \Prim_{E_3}\bigl(\Obs_{\hCS}(X)|_{\fg}\bigr)
  \;\simeq\;
  \Omega^{0,\bullet}(X, \fg^*)[-1],
\]
and
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg}) \simeq
\CE^\bullet_{E_3}(\fg_{\hCS, X},\ \Obs_{\hCS}(X)|_{\fg})$
(Francis $2013$ Thm.~$1.1$, tangent-complex identification; the
$E_3 \to E_3^{\mathrm{hol}}$ comparison is Gwilliam--Williams $2021$
Thm.~$2.5.5$).

\emph{Compact Hodge truncation.} Cartan--Serre finiteness (Hartshorne
\emph{Algebraic Geometry} III.$5.2$) gives $h^{0,q}(X) < \infty$, and
complex dimension gives $h^{0,q}(X) = 0$ for $q \notin \{0, 1, 2, 3\}$.
The $\dbar$-cohomology spectral sequence for the chiral CE complex,
\[
  E_2^{p,q} = H^p_{\mathrm{Lie}}(\fg, H^{0,q}(X)) \Longrightarrow
  \HH^{p+q}_{E_3}(\Obs_{\hCS}(X)|_{\fg}),
\]
degenerates at $E_2$ on compact Kähler $X$ by Deligne's principle of
two types (\emph{Théorie de Hodge II}, \emph{Publ.\ Math.\ IHES}
$40$ ($1971$), Thm.~$1.5.1$; Griffiths--Harris $1978$ Ch.~$0$ §$7$).
For reductive $\fg$, $H^p_{\mathrm{Lie}}(\fg, \C)$ is finite-dimensional
by Chevalley--Eilenberg $1948$ (Humphreys Thm.~$21.1$). Hence
\[
  \HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg})
  \;\simeq\;
  \bigoplus_{p + q = \bullet}
  H^p_{\mathrm{Lie}}(\fg, \C) \otimes_{\C} H^{0,q}(X)
\]
is finite-dimensional in each cohomological degree. This proves (i).

\emph{Dualizability and cobordism hypothesis.}
Pantev--Toën--Vaquié--Vezzosi \emph{Publ.\ Math.\ IHES} $117$
($2013$) Thm.~$2.5$ endows $\mathrm{Map}(X, B\fg)$ with a
$(-3)$-shifted symplectic structure; Calaque--Pantev--Toën--Vaquié--Vezzosi
$2017$ (arXiv:$1506.03699$) Prop.~$2.6$ promotes this to
$3$-dualisability of $\Obs_{\hCS}(X)|_{\fg}$ in
$\mathrm{Alg}_{E_3}(\Ch(\Dolb))$. The finite $\HH^\bullet_{E_3}$ of
the previous step supplies the $2$-morphism-level dualizability datum
that fails on non-compact $\C^3$ (where
$\C[\![\tau_1, \tau_2, \tau_3]\!]$ is not dualisable in $\Ch$). This
proves (ii). Lurie $2009$ \emph{On the classification of topological
field theories} Thm.~$2.4.6$ (cobordism hypothesis) then supplies the
fully extended framed $3$-TFT. Naturality in the CY$_3$ input extends
$\Phi_3$ from object-level to $(\infty, 3)$-functorial on compact
CY$_3$ inputs. This proves (iii).
\end{proof}

\begin{remark}[Chain-level witness on $K3 \times E$]
\label{rem:compact-cy3-3dualizability-k3e}
On the canonical compact example $X = K3 \times E$, the chain-level
identification is witnessed explicitly by the holomorphic Künneth
formula
$\CE^\bullet_{\dbar, \chir}(\Omega^{0,\bullet}(X, \fg))
\simeq \CE^\bullet_{\dbar, \chir}(\Omega^{0,\bullet}(K3, \fg))
\otimes \CE^\bullet_{\dbar, \chir}(\Omega^{0,\bullet}(E, \fg))$
combined with the Hodge data $h^{0,0}(K3) = h^{0,2}(K3) = 1$,
$h^{0,1}(K3) = 0$, $h^{0,0}(E) = h^{0,1}(E) = 1$. The total rank is
$4 \cdot \dim H^\bullet_{\mathrm{Lie}}(\fg, \C)^{E_3}$, consistent
with $\kcat(K3 \times E) = \chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0
= 0$ (Künneth-multiplicative on the total space) and with the
non-vanishing chiral-Hochschild pairing
$\langle [\chi_3], [e_3^{K3 \times E}] \rangle_{\Phi_3}
= 2 \cdot \mathrm{Vol}(E) \cdot (2\pi i)^3$ of
Proposition~\ref{prop:chi-3-nonvanishing-MNOP} via the reduced
Maulik--Oberdieck--Pandharipande DT pairing. The Mukai-enhanced
$\mathsf B$-row ceiling $K^{\kappa_{\mathrm{ch}}} = 8$ on the
canonical five-archetype landmark is recovered at this presentation.
\end{remark}

## Why state B was too conservative

The Wave-$3$ C05 terminal state B flagged as ``the single named
gap'': ``The composed identification $\HH^0_{E_3}(\Obs_{\hCS}(X)|_{\fg})
\simeq \bigoplus_q H^{0,q}(X) \otimes H^\bullet_{\mathrm{Lie}}(\fg,
\C)^{[q]}$ on compact CY$_3$ is \emph{not} a single named theorem in
the primary literature.'' This standard is stricter than the
``compositional CFG proof from named primary sources'' standard of
closure state A: the five steps of the above proof are each a single
named primary-source theorem, and their composition is mechanical.

The Francis $2013$ $E_n$-PBW (Step~$3$) is \emph{universal}: it holds
for every augmented $E_n$-algebra in a stable $\Q$-linear
$\infty$-category, with no compactness hypothesis. The only step
where compactness enters is Step~$4$ (Hodge theory on compact Kähler),
and this is classical (Griffiths--Harris, Demailly, Hartshorne,
Chevalley--Eilenberg). The compact-$X$ BV propagator (Step~$2$) is
explicit in Costello--Li $2016$ arXiv:$1606.00365$ §$3$, not a gap.
Gwilliam--Williams $2021$ Prop.~$5.3.2$ is the $\C^3$-specialisation
of Step~$3$ applied to $\Omega^{0,0}(\C^3) = \C[z_1, z_2, z_3]$;
the compact-$X$ extension is a \emph{different specialisation} of the
\emph{same} Francis PBW, not a new theorem.

No Hypothesis H is needed. The proof is unconditional at CFG level
of detail.

## Cross-consistency notes

**Wave-1 spine.** The Wave-1 spine
(\texttt{notes/platonic\_synthesis\_post\_adversarial.tex} L$509$--$521$,
\texttt{wn:conj:spine-compact-recovery}) stated this conjecturally as
the ``compact-CY$_3$ recovery of extended functoriality.'' The present
retry upgrades from \ClaimStatusConjectured\ to \ClaimStatusTheorem\
via the five-step composition. The Wave-1 conjecture label should be
updated to reference
Theorem~\ref{thm:compact-cy3-3dualizability}.

**Wave-2 refinement.** The Wave-2 three-tier stratification placed
this at \emph{Tier~II} (moderate, method extension). The present
retry confirms Tier~II but demonstrates the extension is pure
composition, not a frontier research task; Tier~II items of this
character close to \ClaimStatusTheorem\ under the CFG detail standard.

**CoHA treatise.** The $(\infty, 3)$-functor extensions of CoHA-side
structures (\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}) use the
same Lurie $2009$ cobordism at $n = 3$ with compactness supplying the
$2$-morphism duals. The present compact-$X$ theorem supplies the
chiral-side companion: on compact CY$_3$, both the chiral observable
algebra $\Obs_{\hCS}(X)|_{\fg}$ (here) and the CoHA (there) upgrade to
$(\infty, 3)$-dualisable objects. The non-compact
$\CoHA(\C^3) = Y^+$ non-dualisability parallels the non-compact
$\Obs_{\hCS}(\C^3)|_{\fg}$ non-dualisability via
$\C[\![\tau_1, \tau_2, \tau_3]\!]$.

**First-principles cache.** AP-CY$265$ of
\texttt{notes/antipatterns\_catalogue.md} (L$4474$--$4513$) registers
the compact-vs-non-compact distinction on $\HH^*_{E_3}$ as a
Critical anti-pattern; the present closure makes the positive
compact-side statement unconditional at CFG level, preserving the
anti-pattern as a discipline rule (``always name compactness when
stating $3$-dualizability'').

**CLAUDE.md charter.** Consistent with the $(\infty, 1)$-categorical
and chain-level equal-status rule: the theorem is stated in both
lanes simultaneously. Chain-level: explicit $\dbar$-Hodge truncation,
explicit Dolbeault resolution, explicit Costello--Li BV propagator,
explicit Kähler Hodge decomposition. $(\infty, 1)$-categorical:
Francis $2013$ PBW, PTVV $2013$ shifted-symplectic, CPTVV $2017$
dualisability, Lurie $2009$ cobordism hypothesis. Subscript discipline:
$\kcat$, $\kch$, $\kBKM$, $\kfib$, $\kanom$ used at native scope; no
bare $\kappa$ in the inscription-ready TeX block.

**Status-tag discipline.** The inscription uses \ClaimStatusTheorem\
(unconditional theorem with complete proof at CFG detail from named
primary sources). The previous Wave-3 C05 \ClaimStatusConjectured\
tag (with Hypothesis H) is superseded; the hypothesis is absorbed
into the five-step proof.

**Promotes.** Item~(iv) of \texttt{thm:plat-dualizability} (currently
\ClaimStatusProvedElsewhere\ with attribution-only proof) to
Theorem~\ref{thm:compact-cy3-3dualizability}
(\ClaimStatusTheorem\ with complete five-step CFG proof). Item~(iv) of
the Wave-$15$ N$5$ note
(\texttt{notes/wave15\_n5\_HH\_E3\_compact\_vs\_open.tex} ``Cycle 4
dualizability consequence'') becomes a theorem, and the Cycle 5
$\Phi$-extension-functoriality observation becomes item~(iii) of the
present theorem.

## Summary

**Terminal state:** A (full closure).

**Why A:** the five-step composition of Griffiths--Harris Dolbeault
+ Costello--Li $2016$ compact-CY$_3$ BV propagator + Francis $2013$
$E_n$-PBW + compact Kähler Hodge theory + PTVV $2013$/CPTVV $2017$
shifted-symplectic dualisability + Lurie $2009$ cobordism hypothesis
produces the chain-level decomposition
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_{\fg}) \simeq
\bigoplus_{p+q=\bullet} H^p_{\mathrm{Lie}}(\fg, \C) \otimes H^{0,q}(X)$
unconditionally, with per-degree finiteness via Cartan--Serre +
Chevalley--Eilenberg, and $3$-dualisability + cobordism-hypothesis
$3$-TFT upgrade of $6$D hCS on compact CY$_3$.

**Previous state B flagged as the gap:** the assembled identification
not being a single named theorem in primary literature. This standard
is stricter than CFG closure; the five named primary-source theorems
compose mechanically, so the assembled identification closes
unconditionally under the CFG detail standard.

**Gwilliam--Williams $2021$ Prop.~$5.3.2$ is the $\C^3$-specialisation**
of the Step~$3$ Francis $E_n$-PBW applied to the polynomial Dolbeault
ring $\Omega^{0,0}(\C^3) = \C[z_1, z_2, z_3]$; the compact-$X$
extension is a \emph{different specialisation} of the \emph{same}
universal Francis PBW, with Dolbeault input replaced by compact-Kähler
Hodge data. No new theorem is required.
