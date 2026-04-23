# Agent 3B-C04 (retry) — Manes--Stora--Zumino descent on the Dolbeault bicomplex for 6d $\hCS$ on CY$_3$

## Terminal state

**C — FRONTIER DECLARATION (with partial B for the abelian fragment).**

The naive Dolbeault lift of the real-de-Rham Manes--Stora--Zumino 1985
*Commun.\ Math.\ Phys.*~102 Thm.~2 descent, starting from
$\mathrm{tr}(F^3)$ on a CY$_3$, **does not work** as stated in the Wave-3
state-B hypothesis. The obstruction is not Bott vanishing but the more
primitive fact that $F(\cA) = \bar\partial\cA + \tfrac12[\cA,\cA] \in
\Omega^{0,2}(X,\fg)$, so $\mathrm{tr}(F^3) \in \Omega^{0,6}(X)$ which
vanishes identically on any CY$_3$ by dimension. The holomorphic-twist
descent ladder therefore cannot start from the Chern--Weil $(2k, 2k)$-form
$\mathrm{tr}(F^3)$ in the way real-form MSZ starts from
$\mathrm{tr}(F_{\mathrm{real}}^3) \in \Omega^{6}_{\mathrm{dR}}$ of a
six-real-dimensional base.

What survives: a reformulated descent that **starts one step lower**, at
the $Q_{\mathrm{BRST}}$-level, from the universal one-loop BV integrand
$\mathrm{tr}(\cA \bar\partial\cA \bar\partial\cA) \cdot \Omega_X \in
\Omega^{3,2}(X)$ (the Costello--Li hCS kinetic density extended cubically).
This yields the correct chain-level primitive $Q^{(0)}_{5,\mathrm{hol}}$ and
descends correctly **in the abelian case $\fg = \fu(1)$**. In the
non-abelian case the descent stalls at the need for a scheme-compatible
BV extension (the Wave-3 hypothesis
\texttt{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}) that
is not supplied by the real-form MSZ functor. The hypothesis is
genuinely a frontier-research item, not a bookkeeping extension.

Flag: \texttt{\textbackslash ClaimStatusOpen} for the non-abelian
descent; \texttt{\textbackslash ClaimStatusProvedHere} for the abelian
fragment (six-vertex identity).

## The Hodge-bidegree obstruction (why the naive lift fails)

On a complex $n$-fold the Dolbeault bicomplex is $\Omega^{p,q}$,
$0 \leq p, q \leq n$. For $n = 3$ we have $(p, q) \in \{0,1,2,3\}^2$.
For a holomorphic $\fg$-bundle with Dolbeault connection
$\cA \in \Omega^{0,1}(X, \fg)$, the curvature is the **$(0,2)$-component**
\[
  F(\cA) \;=\; \bar\partial\cA + \tfrac{1}{2}[\cA, \cA]
  \;\in\; \Omega^{0,2}(X, \fg).
\]
(Equivalently: the $(1,1)$-component $F^{1,1}$ and $(2,0)$-component
$F^{2,0}$ vanish because $\cA$ has only a $(0,1)$-part; this is the
standard convention for the holomorphic-twist gauge theory of
Costello 2013, Costello--Li 2016, Costello--Gwilliam 2017 Vol~II~\S 11.)
Taking cubes,
\[
  \mathrm{tr}(F^3)\;\in\;\Omega^{0,6}(X)\;=\;0
  \qquad (\dim_{\bar\partial} X = 3).
\]
Likewise $\Omega_X \wedge \mathrm{tr}(F^3) \in \Omega^{3,6}(X) = 0$.
The Chern--Weil starting point of the real-de-Rham MSZ descent — a
nonzero closed form of top bidegree — simply is not available on the
Dolbeault bicomplex of a CY$_3$ at cubic order in the curvature.

**Wrong claim in the Wave-3 brief:** "$\mathrm{tr}(F^3)_{3,3} \in
\Omega^{3,3}$". Parsing attempts:

- If $\mathrm{tr}(F^3)_{3,3}$ means the $(3,3)$-Hodge component of a
  cubic trace of the real curvature $F_{\mathrm{real}} \in
  \Omega^{1,1} \oplus \Omega^{2,0} \oplus \Omega^{0,2}$, then yes,
  $(F_{\mathrm{real}})^3$ has components in bidegrees summing to six
  including $(3,3)$. But $(F_{\mathrm{real}})^3$ descending to $Q_5$
  is **real-form MSZ**, not holomorphic twist. The holomorphic twist
  replaces $F_{\mathrm{real}}$ by $F(\cA) \in \Omega^{0,2}$, losing
  the $(1,1)$ and $(2,0)$ components, losing the $(3,3)$ output.

- If $\mathrm{tr}(F^3)_{3,3}$ means $\Omega_X \wedge \mathrm{tr}(F^3)$
  after "projecting" to $(3,3)$ via the Calabi--Yau pairing, this is
  $0$ by dimension as above.

- If one means the Atiyah--Chern--Weil cocycle of the holomorphic
  tangent bundle $\mathrm{td}_3(T_X) \in H^{3,3}(X, \C)$ or
  $\mathrm{ch}_3(T_X)$, this is a scalar on a CY$_3$ (a number times
  the fundamental class), not a form descending to $Q_5^{\mathrm{hol}}$.

None of these give the Chern--Weil-to-Chern--Simons descent of real-form
MSZ. The Dolbeault bicomplex does not admit the real-form MSZ lift by
functorial substitution $d \rightsquigarrow \bar\partial$, $F \rightsquigarrow F(\cA)$.

## The corrected starting point: the hCS kinetic density

The correct bidegree arithmetic on a CY$_3$ is to start from the
holomorphic Chern--Simons classical action density, **not from a
Chern--Weil top form**. The Costello--Li 2016 \S 2 holomorphic
Chern--Simons action
\begin{equation}
\label{eq:hCS-action}
  S_{\hCS}^{\mathrm{cl}}(\cA)
  \;=\;
  \frac{1}{(2\pi i)^3}\,\int_X \Omega_X \wedge
  \mathrm{tr}\!\left(
    \tfrac{1}{2}\, \cA \wedge \bar\partial\cA
    \;+\; \tfrac{1}{6}\, \cA \wedge \cA \wedge \cA
  \right),
\end{equation}
has integrand a $(3,3)$-form:
$\Omega_X \in \Omega^{3,0}$, $\cA \in \Omega^{0,1}$, $\bar\partial\cA \in
\Omega^{0,2}$, so $\Omega_X \wedge \cA \wedge \bar\partial\cA \in
\Omega^{3, 1+2} = \Omega^{3,3}$, a top form on the real six-manifold $X$
as required for integration. The cubic term $\Omega_X \wedge \cA^3 \in
\Omega^{3,3}$ likewise. This is the actual $(3,3)$-receptacle on a
CY$_3$.

**Observation (bidegree accounting).** The hCS Lagrangian density is
**already** one degree below the Chern--Weil form that descends to it
in the real-form setup. Real-form CS: $\mathrm{tr}(F^3) = d Q_5$, so
$Q_5 \in \Omega^{5}_{\mathrm{dR}}$ is one form-degree below
$\mathrm{tr}(F^3) \in \Omega^{6}_{\mathrm{dR}}$. Holomorphic twist:
on a CY$_3$, the top form in $\Omega^{3,3}$ is **already** $\bar\partial
Q^{(0)}$ for a form $Q^{(0)}$ of bidegree $(3,2)$, not of bidegree
$(3,3)$. The descent ladder is therefore shifted:
\[
  \underbrace{\Omega_X \wedge \mathrm{tr}(F^3)}_{\Omega^{3,6} = 0
  \text{, not the starting point}}
  \;\neq\;
  \bar\partial\bigl(\Omega_X \wedge \mathrm{tr}(\cdots)\bigr)
  \qquad\text{on CY}_3.
\]
The correct ladder descends from the **kinetic density** of the hCS
one-loop anomaly integrand, not from a Chern--Weil top form.

## Step 1 — The hCS BV integrand at cubic order.

The one-loop BV integrand for hCS at cubic order in $\cA$ is the
Costello--Li 2016 Proposition~5.2 heat-kernel expansion at order $\hbar$
and $\mathrm{Sym}^3(\cE^\vee)$. Extracting the cubic-Casimir
contribution and its BV-ghost extension gives a local density
\[
  \Lambda^{\mathrm{cons}}_3(\cA)
  \;=\;
  \frac{i}{(2\pi)^3}\,\Omega_X \wedge \mathrm{tr}\!\left(
    \cA \wedge \bar\partial\cA \wedge \bar\partial\cA
    + \tfrac{3}{2}\,\cA \wedge \cA \wedge \cA \wedge \bar\partial\cA
    + \tfrac{3}{5}\,\cA \wedge \cA \wedge \cA \wedge \cA \wedge \cA
  \right),
\]
with bidegree accounting
\begin{align*}
  \Omega_X \wedge \cA \wedge \bar\partial\cA \wedge \bar\partial\cA
  &\in \Omega^{3, 1+2+2} \;=\; \Omega^{3,5} \;=\; 0 \text{ on CY}_3, \\
  \Omega_X \wedge \cA^3 \wedge \bar\partial\cA
  &\in \Omega^{3, 3+2} \;=\; \Omega^{3,5} \;=\; 0 \text{ on CY}_3, \\
  \Omega_X \wedge \cA^5
  &\in \Omega^{3, 5} \;=\; 0 \text{ on CY}_3.
\end{align*}
**Every summand vanishes identically on a CY$_3$.** The Zumino 1983
$Q_5$-form written in the Dolbeault-twist incarnation is the zero form,
and $Q^{(0)}_{5,\mathrm{hol}}$ as literally written in the Wave-3
C04 state-B file (equations copied below for reference) is
identically zero on CY$_3$.

For reference, the Wave-3 C04 formula (verbatim):
\[
  Q^{(0)}_{5,\mathrm{hol}}
  \;=\;
  \frac{i}{(2\pi)^3}\,\Omega_X \wedge \mathrm{tr}\!\left(
    \cA \wedge \bar\partial\cA \wedge \bar\partial\cA
    + \tfrac{3}{2}\,\cA^3 \wedge \bar\partial\cA
    + \tfrac{3}{5}\,\cA^5
  \right)
  \;=\;\mathbf{0}\qquad\text{on any CY}_3.
\]

## Step 2 — What actually happens: the descent is truncated.

On a CY$_3$, the Dolbeault bicomplex supports nontrivial closed forms
only up to bidegree $(3,3)$. The hCS classical density is already a
$(3,3)$-form, and the cubic term $\Omega_X \wedge \cA^3 \in
\Omega^{3,3}$ is nonzero. The **truncated descent** is
\begin{align*}
  \bar\partial\bigl(\Omega_X \wedge \cA^3\bigr)
  &= \Omega_X \wedge \bar\partial(\cA^3)
   = \Omega_X \wedge 3\, \cA^2 \wedge \bar\partial\cA
   \in \Omega^{3, 1+1+2}
   \;=\; \Omega^{3,4}
   \;=\; 0
\end{align*}
i.e.\ $\Omega_X \wedge \cA^3$ is $\bar\partial$-closed for dimensional
reasons. There is no higher-bidegree form to descend into. The
quadratic term $\Omega_X \wedge \cA \wedge \bar\partial\cA \in
\Omega^{3,3}$ likewise is $\bar\partial$-closed
($\bar\partial(\Omega_X \wedge \cA \wedge \bar\partial\cA) = \Omega_X
\wedge \bar\partial\cA \wedge \bar\partial\cA \in \Omega^{3,5} = 0$).

**Conclusion.** The MSZ descent ladder on the Dolbeault bicomplex of a
CY$_3$ terminates at bidegree $(3,3)$ after $0$ steps (the top bidegree
is the kinetic density itself, already $\bar\partial$-closed mod top
forms). There is no analogue of the real-form chain
$\mathrm{tr}(F^3) \to Q^{(0)}_5 \to Q^{(1)}_4$ because the Dolbeault
bicomplex lacks the source $(3, 3+k)$-forms for $k \geq 1$.

## Step 3 — The actual source of $\kanom$ on CY$_3$ (Costello--Li 2016).

The one-loop anomaly is not computed by MSZ descent. Costello--Li
2016 Proposition~5.2 establishes
\[
  [\kanom] \;=\;
  \frac{\hbar\, A(\fg)\,\chi_{\mathrm{top}}(X)}{2(4\pi)^3}\,
  \|\Omega_X\|^2
  \;\in\;
  H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])
\]
via a **heat-kernel regularisation argument**: the short-time asymptotic
expansion of the $\bar\partial$-Laplacian heat kernel, paired against
the ghost-field action, produces the Atiyah--Singer index density
$\chi_{\mathrm{top}}(X)/24$ on the geometric factor and $A(\fg)$ on the
Lie-algebra factor. The descent equations (Wess--Zumino consistency,
ghost-$1$ cocycle) are satisfied **by the cohomology class**, not by a
chain-level Dolbeault ladder. At chain level, the BV anomaly is
localised on the diagonal of $X \times X$ via the heat-kernel
singularity, with $Q_{\mathrm{BRST}}$ closure a consequence of the
Stokes theorem for the regularised heat kernel (Costello--Gwilliam
2017 Vol~II Thm.~9.5.0.6), not of MSZ descent.

## Step 4 — What remains: the Bardeen--Zumino difference at the abelian level.

For $\fg = \fu(1)$ (abelian), the cubic-Casimir $A(\fu(1)) = 0$
(there is no $d^{abc}$ for an abelian algebra), so the cubic
contribution vanishes on the nose. The quadratic contribution is
(tree-level) the kinetic density $\Omega_X \wedge \cA \bar\partial\cA
\in \Omega^{3,3}$, and a **holomorphic Bardeen--Zumino identity** does
hold at this order as a consequence of the six-vertex/Wick identity
for the free $\bar\partial$-propagator. Explicitly:

\begin{proposition}[Abelian holomorphic Bardeen--Zumino identity]
\label{prop:abelian-bz-hol}
\ClaimStatusProvedHere
For $\fg = \fu(1)$ on a compact CY$_3$ $X$, the local functional
\[
  \mathrm{BZ}^{\mathrm{hol,\,ab}}(\cA)
  \;:=\;
  \frac{1}{(2\pi i)^3}\,\int_X\, \Omega_X \wedge
  \tfrac{1}{2}\, \cA \wedge \bar\partial\cA
  \;\in\;
  \mathrm{Sym}^2(\cE^\vee)_{\mathrm{ghost}\,0}
\]
is $Q_{\mathrm{BRST}}$-closed modulo the equations of motion $\bar\partial\cA = 0$
and satisfies
\[
  Q_{\mathrm{BRST}}\bigl(\mathrm{BZ}^{\mathrm{hol,\,ab}}\bigr)
  \;=\;
  \kanom^{\mathrm{cons},\,\mathrm{ab}} - \kanom^{\mathrm{cov},\,\mathrm{ab}}
  \;=\;0\quad\text{identically}
\]
because both abelian representatives vanish (no $d^{abc}$, no
cubic-Casimir contribution). The identity is trivially true and
carries no information beyond the vanishing of abelian hCS anomalies.
\end{proposition}

\begin{proof}
In the abelian case $\fg = \fu(1)$ the gauge algebra is one-dimensional
with trivial bracket $[\cdot, \cdot] = 0$. The curvature reduces to
$F(\cA) = \bar\partial\cA \in \Omega^{0,2}(X)$, the cubic-Casimir
coefficient $A(\fu(1)) = 0$, and the one-loop BV anomaly
$\kanom(X, \fu(1)) = 0$ by Theorem~\ref{thm:plat-anomaly}
(\texttt{quantum\_chiral\_algebras.tex} §\texttt{subsec:hcs-anomaly},
lines 3448--3488). Both scheme-specific representatives
$\kanom^{\mathrm{cons},\mathrm{ab}}, \kanom^{\mathrm{cov},\mathrm{ab}}$
vanish on the nose, so their difference vanishes, and
$Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol,\,ab}}) = 0$ trivially.
\end{proof}

This abelian fragment is the only piece of the Wave-3 state-B statement
that survives the Dolbeault-bicomplex bidegree analysis. It is honest
but empty: it says $0 = 0$.

## Step 5 — The genuine frontier: what primary source is missing.

What the Wave-3 state-B hypothesis
\texttt{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
needs to establish, to promote the abelian fragment to a non-abelian
theorem, is **not** a holomorphic lift of MSZ 1985 (which cannot be
lifted by the bidegree obstruction above). What is needed is:

\begin{frontier}[Holomorphic descent from Atiyah classes, not from
Chern--Weil top forms]
\label{frontier:holomorphic-descent-atiyah}
\ClaimStatusOpen
Construct a pair of chain-level representatives
$\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}} \in
C^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ for the Costello--Li 2016
Proposition~5.2 one-loop anomaly class, differing by
$Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}})$ where
$\mathrm{BZ}^{\mathrm{hol}}$ is a local functional polynomial in $\cA$
of cubic degree, via a descent ladder on the Dolbeault bicomplex
starting not from $\mathrm{tr}(F^3)$ but from the Atiyah class
$\mathrm{At}(T_X) \in H^{1,1}(X, \End T_X)$ of the tangent bundle,
coupled to the cubic-Casimir class $d^{abc}$ of the gauge algebra.
\end{frontier}

The obstruction: no primary source in the literature performs this
descent. Real-form MSZ 1985 *Commun.\ Math.\ Phys.*~102 Thm.~2 starts
from Chern--Weil, not from Atiyah; the Costello--Li 2016 heat-kernel
derivation of $[\kanom]$ does not produce two distinct chain-level
representatives. The Costello 2011 \S 5.6 scheme-change formalism
promotes a difference cochain to an $L_\infty$-morphism *after* the
difference is constructed, but does not itself construct the two
representatives. Costello--Gwilliam 2017 Vol~II \S 11.1 describes
BCFG-equivariant renormalisation at the abstract level but does not
analyse the consistent-vs-covariant bifurcation for cubic anomalies
on holomorphic theories.

A first step (not yet a theorem): Kapranov 1999
*Compositio Math.*~115 \S 4 establishes a dg Lie structure on
$\Omega^{0,\bullet}(X, T_X)$ with $\ell_3$ bracket dual to the Atiyah
class cubed $\mathrm{At}^3 \in H^{3,3}(X, \Lambda^3 \End T_X)$. The
conjectural lift of MSZ descent would couple the gauge-bundle cubic
Casimir $d^{abc}$ to $\mathrm{At}^3$ via the Costello--Li index
formula to produce a pair $(\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}})$
whose difference is a descent of the **Kapranov cubic bracket**, not
of the Chern--Simons $Q_5$-form. This is genuinely new mathematics
and belongs to the programme, not to the closure wave.

## Cross-consistency notes

### With the Wave-3 C04 state-B file

The Wave-3 C04 state-B claim that
\[
  Q^{(0)}_{5,\mathrm{hol}}
  = \tfrac{i}{(2\pi)^3}\,\Omega_X\wedge
    \mathrm{tr}\!\left(\cA\bar\partial\cA\bar\partial\cA
      + \tfrac32\,\cA^3\bar\partial\cA + \tfrac35\,\cA^5\right)
\]
is written by functorially substituting $d \rightsquigarrow \bar\partial$,
$A_{\mathrm{real}} \rightsquigarrow \cA$, $F_{\mathrm{real}}
\rightsquigarrow F(\cA)$ in Zumino 1983 *Nucl.\ Phys.\ B*~223 $Q_5$.
The substitution is formally correct but produces the **zero form** on
a CY$_3$ by bidegree ($\Omega^{3, \geq 4} = 0$). The Wave-3 C04 file
does not flag this vanishing; the error is in Step~2 of its proof
("Holomorphic Stora--Zumino descent") where the statement
"$\bar\partial Q^{(0)}_{5,\mathrm{hol}} + (2\pi i)^{-3}/6\cdot\Omega_X
\wedge \mathrm{tr}(F^3)_{0,3} = 0$" is correct but uninformative: both
sides vanish identically ($\mathrm{tr}(F^3)_{0,3} = 0$ because
$F \in \Omega^{0,2}$, and the putative primitive is zero).

### With AP-CY 162 / BCOV curving vs Yukawa cubic (cache entry W14-A3)

AP-CY162 records: $\alpha_{\mathrm{BCOV}} \in H^{0,1}(X)$,
$Y_3 \in H^{0,3}(X) = H^3(X, \cO_X)$, three Atiyah-sourced cocycles in
distinct Hodge receptacles. The hCS cubic-Casimir anomaly of
Costello--Li 2016 Proposition~5.2 is **fourth Hodge-distinct** receptacle:
the cohomology class is $A(\fg)(\chi_{\mathrm{top}}/24)\|\Omega_X\|^2$,
a number times the volume form in $H^{3,3}(X) \otimes \C$ (integrating
to a scalar). The chain-level representative is not a Dolbeault
$(3,2)$-form; it is the heat-kernel short-time expansion coefficient
localised on the diagonal, supported in the full BV-complex
$C^\bullet_{\mathrm{loc}}(\cE_{\hCS}[-1])$. The Wave-3 state-B attempt
to place $\mathrm{BZ}^{\mathrm{hol}}$ in the Hodge receptacle
$\mathrm{Sym}^3(\cE^\vee) \otimes H^{3,2}(X)$ is bidegree-inconsistent:
the form to place there is zero on CY$_3$.

### With AP-CY 264 / Atiyah K3xE block-diagonal truncation (cache entry W15-L2)

For $X = K3 \times E$, the Atiyah class decomposes
$\mathrm{At}(T_{K3\times E}) = p_1^*\mathrm{At}(T_{K3}) \oplus
p_2^*\mathrm{At}(T_E)$ with $\mathrm{At}(T_E) = 0$ on-the-nose. The
cubic Kapranov bracket $\ell_3$ for the Dolbeault algebra
$\Omega^{0,\bullet}(K3 \times E, T_{K3 \times E})$ truncates to
$\Omega^{0,\bullet}(K3, T_{K3})$ by Künneth. Any conjectural
holomorphic-descent construction via Kapranov's $\ell_3$ on $K3 \times E$
therefore reduces to the $K3$-side; but $\chi_{\mathrm{top}}(K3 \times E)
= 24 \cdot 0 = 0$, so the one-loop anomaly vanishes for this CY$_3$
regardless. This is consistent with
\texttt{quantum\_chiral\_algebras.tex} Theorem~\texttt{thm:plat-anomaly}(ii).

### With AP-CY 144 / canonicality-inversion discipline

The cohomology class $[\kanom] \in H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$
is canonical (Costello--Gwilliam 2017 Vol~II Thm.~9.5.0.6); chain-level
representatives are scheme-dependent. The Wave-3 state-B plan to
supply the BZ cochain as the **explicit intertwiner** between two
specific chain representatives is sound in principle. What the
Dolbeault-bicomplex analysis adds: the intertwiner cannot be the
holomorphic twist of Zumino's $Q_5$. It must be a new local functional
whose construction is a genuine frontier item.

### With the Wave-1 spine \texttt{thm:spine-consistent-covariant}

The Wave-1 spine asserts existence of $\mathrm{BZ}^{\mathrm{hol}}$ as a
local functional satisfying $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}})
= \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$. With the Dolbeault
bidegree analysis: the Wave-1 assertion is correct as a **cohomology-level
statement** (any two representatives of $[\kanom] = 0$ for anomaly-free
$(\fg, X)$ pairs differ by a coboundary), but the **explicit Zumino-$Q_5$
realisation is false** on the Dolbeault bicomplex. The Wave-1 spine
statement should be downgraded from "explicit $Q_5^{\mathrm{hol}}$
primitive" to "abstract coboundary primitive", or upgraded with the
Kapranov-Atiyah frontier construction (still open).

### With the Wave-2 refinement \texttt{wn:thm:second-pass-BZ-category}

The Wave-2 refinement corrected the sign convention to
$\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}$. The sign correction
is unaffected by the Dolbeault bidegree issue (the sign is a convention
in the real-form MSZ 1985 paper and transports verbatim to any
well-defined holomorphic realisation). But the existence of the
primitive in the stated form fails. Wave-2 should be further refined
to flag the bidegree obstruction.

### With the monograph \texttt{thm:plat-anomaly}

The monograph Theorem~\texttt{thm:plat-anomaly}
(\texttt{quantum\_chiral\_algebras.tex} line 3448) states the
cohomology class $[\kanom] = (\hbar A(\fg) \chi_{\mathrm{top}} /
2(4\pi)^3)\|\Omega_X\|^2$ and vanishes for the ADE-exceptional list
and for $K3 \times E$. This theorem is unaffected by the Dolbeault
descent obstruction: it is a cohomology-level statement proved by
the Costello 2015 heat-kernel calculation, not by MSZ descent.

## Frontier declaration (inscription-ready TeX)

```latex
\begin{remark}[Bidegree obstruction to Dolbeault MSZ descent]
\label{rem:bidegree-obstruction-MSZ-dolbeault}
\ClaimStatusProvedHere
On a Calabi--Yau threefold $X$, the Dolbeault curvature
$F(\cA) = \bar\partial\cA + \tfrac12[\cA, \cA] \in \Omega^{0,2}(X, \fg)$
has cube $\mathrm{tr}(F^3) \in \Omega^{0,6}(X) = 0$. Consequently the
formal holomorphic-twist substitution
$\mathrm{tr}(F^3_{\mathrm{real}}) \rightsquigarrow
\Omega_X \wedge \mathrm{tr}(F(\cA)^3)$ produces the zero form in
$\Omega^{3,6}(X) = 0$, and the Manes--Stora--Zumino $1985$
\emph{Commun.\ Math.\ Phys.}\ $102$ Thm.~$2$ descent ladder does not
lift to the Dolbeault bicomplex in the form
$\mathrm{tr}(F^3) \to Q^{(0)}_5 \to Q^{(1)}_4$. The real-form $Q_5$
primitive, when written with $d \rightsquigarrow \bar\partial$ and
$A \rightsquigarrow \cA$, evaluates to zero on CY$_3$ by bidegree
($\Omega^{3, \geq 4}(X) = 0$). The chain-level primitive witnessing
the scheme-difference of the cubic-Casimir one-loop anomaly of
Costello--Li $2016$ Prop.~$5.2$ is therefore not the holomorphic twist
of Zumino's $Q_5$ and must be constructed by a different mechanism,
coupling the gauge-bundle cubic Casimir $d^{abc}$ to the Kapranov
$1999$ Compositio Math.\ $115$ \S$4$ cubic $L_\infty$-bracket on
$\Omega^{0,\bullet}(X, T_X)$ via the Atiyah class $\mathrm{At}(T_X)
\in H^{1,1}(X, \End T_X)$ rather than the Chern--Weil cocycle
$\mathrm{tr}(F^3)$. This construction is an open item.
\end{remark}

\begin{frontier}[Holomorphic Bardeen--Zumino cochain via Atiyah--Kapranov
coupling]
\label{frontier:hol-BZ-atiyah-kapranov}
\ClaimStatusOpen
For $X$ a compact CY$_3$ and $\fg$ a semisimple Lie algebra with
$d^{abc} \neq 0$ (e.g.\ $\fg = \mathfrak{su}(N \geq 3)$), produce a
pair of local chain-level representatives
$\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}} \in
C^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ of the cubic-Casimir one-loop
anomaly of Costello--Li $2016$ Prop.~$5.2$, together with a local
functional $\mathrm{BZ}^{\mathrm{hol}} \in
C^0_{\mathrm{loc}}(\cE_{\hCS}[-1])$ satisfying
$Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}) = \kanom^{\mathrm{cons}}
- \kanom^{\mathrm{cov}}$, built from the cubic Kapranov bracket
$\ell_3 \colon \Omega^{0,\bullet}(X, T_X)^{\otimes 3} \to
\Omega^{0,\bullet+1}(X, T_X)$ (Kapranov $1999$ Compositio Math.\ $115$
\S$4$) coupled to $d^{abc}(\fg)$ via the Atiyah class
$\mathrm{At}(T_X)$. Existing primary sources provide:
\begin{itemize}
  \item the Kapranov bracket $\ell_3$ as dual to $\mathrm{At}^3$
  (Kapranov $1999$ Thm.~$4.2$);
  \item the Costello--Li heat-kernel anomaly class as the Atiyah--Singer
  index coupling of $d^{abc}$ and $\mathrm{At}^3$
  (Costello--Li $2016$ Prop.~$5.2$, arXiv:$1606.00365$);
  \item the Costello $2011$ \S$5.6$ scheme-change formalism promoting a
  chain-level difference cochain to an $L_\infty$-morphism;
\end{itemize}
but no primary source has performed the descent assembling these
ingredients into two distinct chain-level representatives and an
explicit intertwiner at cubic order. The bidegree obstruction
\eqref{rem:bidegree-obstruction-MSZ-dolbeault} rules out the
Zumino-$Q_5$ construction; an Atiyah--Kapranov-sourced construction is
conjectural.
\end{frontier}

\begin{proposition}[Abelian Bardeen--Zumino identity on CY$_3$]
\label{prop:abelian-bz-hol-cy3}
\ClaimStatusProvedHere
For $\fg = \fu(1)$ on a compact CY$_3$ $X$, both cubic-Casimir one-loop
anomaly representatives
$\kanom^{\mathrm{cons},\mathrm{ab}}, \kanom^{\mathrm{cov},\mathrm{ab}}
\in C^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ vanish on the nose (no $d^{abc}$
for abelian $\fg$), and the holomorphic Bardeen--Zumino local functional
$\mathrm{BZ}^{\mathrm{hol,\,ab}} = (2\pi i)^{-3}\int_X \Omega_X \wedge
\tfrac12 \cA \wedge \bar\partial\cA$ satisfies
$Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol,\,ab}}) =
\kanom^{\mathrm{cons},\mathrm{ab}} - \kanom^{\mathrm{cov},\mathrm{ab}}
= 0$ trivially. The identity carries no information beyond the
ADE-and-exceptional-plus-abelian vanishing list of
Theorem~\ref{thm:plat-anomaly}(i).
\end{proposition}
```

## Primary sources

1. Zumino, B.\ $1983$, *Chiral anomalies and differential geometry*,
   in *Relativity, Groups and Topology II (Les Houches $1983$)*,
   North--Holland — $Q_5$ Chern--Simons form coefficients $1, 3/2, 3/5$,
   applicable on six-real-dimensional de~Rham base.

2. Manes, J., Stora, R., Zumino, B.\ $1985$, *Algebraic study of chiral
   anomalies*, *Commun.\ Math.\ Phys.*\ $102$, pp.~$157$--$174$,
   Thm.~$2$ — real-form descent algorithm, does not lift functorially
   to Dolbeault bicomplex (bidegree obstruction).

3. Kapranov, M.\ $1999$, *Rozansky--Witten invariants via Atiyah
   classes*, *Compositio Math.*\ $115$, pp.~$71$--$113$, Thm.~$4.2$ —
   cubic bracket $\ell_3 \colon \Omega^{0,\bullet}(X, T_X)^{\otimes 3}
   \to \Omega^{0,\bullet+1}(X, T_X)$ dual to $\mathrm{At}^3$; the
   conjectural replacement-source for a holomorphic descent.

4. Costello, K.\ $2011$, *Renormalization and Effective Field Theory*,
   AMS Math.\ Surveys Monogr.\ $170$, Ch.~$5$ (\S$5.4$, \S$5.6$,
   Thm.~$5.6.1$) — scheme-change $L_\infty$-morphism formalism.

5. Costello, K., Li, S.\ $2016$, *Twisted supergravity and its
   quantization*, arXiv:$1606.00365$, Prop.~$5.2$ — one-loop BV anomaly
   class via heat-kernel.

6. Costello, K., Gwilliam, O.\ $2017$, *Factorization algebras in
   quantum field theory, Vol.~II*, CUP, Thm.~$9.5.0.6$ and \S$11.1$ —
   scheme-independence of BV cohomology; BCFG-equivariant BV
   renormalisation.

7. Atiyah, M.F.\ $1957$, *Complex analytic connections in fibre
   bundles*, *Trans.\ AMS*\ $85$, pp.~$181$--$207$, Thm.~$1$ —
   Atiyah class $\mathrm{At}(T_X) \in H^{1,1}(X, \End T_X)$.

## Summary

**Terminal state: C** (frontier declaration) for the non-abelian case;
**state A** (abelian, trivially) for the abelian fragment.

The Wave-3 C04 state-B hypothesis cannot be promoted to state A by
invoking MSZ 1985 on the Dolbeault bicomplex. The bidegree obstruction
is not Bott vanishing or heat-kernel subtlety — it is the elementary
fact that $F(\cA) \in \Omega^{0,2}$ makes $F^3 \in \Omega^{0,6} = 0$ on
CY$_3$, voiding the Chern--Weil source of the MSZ ladder. The
genuine construction requires Atiyah--Kapranov coupling not present in
any primary source; this is declared as
Frontier~\ref{frontier:hol-BZ-atiyah-kapranov}.

The downstream monograph statements (Theorem~\texttt{thm:plat-anomaly},
\texttt{thm:three-atiyah-cocycles-qca}) are unaffected: they address the
cohomology class $[\kanom]$, proved by Costello--Li heat-kernel, not by
MSZ descent. The Wave-1 spine and Wave-2 refinement assertions of an
explicit $\mathrm{BZ}^{\mathrm{hol}}$ primitive via holomorphic-twist
Zumino-$Q_5$ should be downgraded to abstract-coboundary statements
pending resolution of
Frontier~\ref{frontier:hol-BZ-atiyah-kapranov}.
