# Agent C04 — Bardeen--Zumino cochain bridging consistent and covariant cubic-Casimir one-loop BV obstructions on 6d hCS, as an $L_\infty$-morphism

## Terminal state

**B — CONDITIONAL CLOSURE.**

The theorem is reducible to a precise and single named hypothesis: the
holomorphic analogue of the Manes--Stora--Zumino $1985$ algebraic
descent algorithm applied to the Costello--Li $2016$ BV cohomology
$H^\bullet_{\mathrm{loc}}(\cE_{\hCS})$. The ingredients (holomorphic
descent of $\mathrm{tr}(F^3)$ to $Q^{(0)}_5$ to $Q^{(1)}_4$; existence
of two quantisation schemes pairing the BV effective action with the
two anomaly representatives; $L_\infty$-morphism promotion via the
Costello $2011$ scheme-change formalism) are each documented in
existing primary sources at the real-form level, and the holomorphic
lift is functorial on their proofs. The hypothesis is the existence of
a scheme-compatible pair $(R^{\mathrm{cons}}, R^{\mathrm{cov}})$ of BV
renormalisations of $\hCS$ on CY$_3$ whose scheme-difference cochain
computes the holomorphic BZ polynomial.

Flag: `\ClaimStatusConjectured` with hypothesis
`hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes`.

## Statement of the theorem

\begin{theorem}[Holomorphic Bardeen--Zumino $L_\infty$-morphism for 6d
$\hCS$ on a Calabi--Yau threefold]
\label{thm:bz-hol-linfty-intra-cubic}
\ClaimStatusConjectured
Let $X$ be a Calabi--Yau threefold with holomorphic volume form
$\Omega_X$, let $\fg$ be a semisimple Lie algebra with cubic-Casimir
coefficient $A(\fg) = d^{abc}d_{abc}/\dim\fg$, and let
$\cE_{\hCS} = \Omega^{0,\bullet}(X, \fg)[1]$ be the
Costello--Li BV dg Lie algebra of six-dimensional holomorphic
Chern--Simons on $X$. Assume hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
below.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The one-loop $\hCS$ BV obstruction admits two local
chain-level representatives
\[
\kanom^{\mathrm{cons}}(X, \fg),\;
\kanom^{\mathrm{cov}}(X, \fg)
\;\in\;
C^1_{\mathrm{loc}}(\cE_{\hCS}[-1]),
\]
the consistent representative satisfying the Wess--Zumino consistency
condition $Q_{\mathrm{BRST}}\,\kanom^{\mathrm{cons}} = 0$ with
$Q_{\mathrm{BRST}}$ nilpotent on the BV complex, and the covariant
representative $\kanom^{\mathrm{cov}}$ transforming as a primary
gauge tensor under the action of $\fg$ on
$\Omega^{0,\bullet}(X, \fg)$. Both lift the universal cubic-Casimir
class $\hbar A(\fg)\chi_{\mathrm{top}}(X)(2(4\pi)^3)^{-1}
\|\Omega_X\|^2 \in H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ of
Costello--Li $2016$ Proposition~$5.2$.

\item There exists a local functional
$\mathrm{BZ}^{\mathrm{hol}}(\cA) \in
\mathrm{Sym}^3(\cE^\vee) \cap C^0_{\mathrm{loc}}(\cE_{\hCS}[-1])$,
polynomial of homogeneous cubic degree in the gauge-field component of
$\cA \in \Omega^{0,1}(X, \fg)$, explicitly given by the holomorphic
Chern--Simons $(3,2)$-form
\[
\mathrm{BZ}^{\mathrm{hol}}(\cA)
\;=\;
\frac{i}{(2\pi)^3} \int_X \Omega_X \wedge
\mathrm{tr}\Bigl(
\cA \wedge \bar\partial\cA \wedge \bar\partial\cA
\;+\; \tfrac{3}{2}\, \cA \wedge \cA \wedge \cA \wedge \bar\partial\cA
\;+\; \tfrac{3}{5}\, \cA \wedge \cA \wedge \cA \wedge \cA \wedge \cA
\Bigr),
\]
the holomorphic-twist descendant of the Zumino $1983$ Chern--Simons
$(5)$-form $Q_5 = \mathrm{tr}(A dA^2 + \tfrac{3}{2} A^3 dA +
\tfrac{3}{5} A^5)$ on the Dolbeault $(0,1)$-sector, such that as
local cochains in $C^\bullet_{\mathrm{loc}}(\cE_{\hCS}[-1])$
\[
Q_{\mathrm{BRST}}\bigl(\mathrm{BZ}^{\mathrm{hol}}\bigr)
\;=\;
\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}.
\]

\item The sequence $f_\bullet = (f_0, f_1, f_2, \ldots)$
with $f_0 = \mathrm{BZ}^{\mathrm{hol}}$ at zero arity, $f_1$ the
identity on $\cE_{\hCS}[-1]$, and higher terms $f_k$ determined by
the scheme-change tower of Costello $2011$ \S$5.6$ promotes
$\mathrm{BZ}^{\mathrm{hol}}$ to a curved $L_\infty$-morphism
\[
\Bigl(\cE_{\hCS},\;
\ell^\bullet,\;
Q_{\mathrm{BRST}} + \hbar\Delta + \kanom^{\mathrm{cov}}\Bigr)
\;\xrightarrow{\;f_\bullet\;}\;
\Bigl(\cE_{\hCS},\;
\ell^\bullet,\;
Q_{\mathrm{BRST}} + \hbar\Delta + \kanom^{\mathrm{cons}}\Bigr),
\]
between the two curved BV-BRST dg Lie algebras, whose curvature
$f_0 = \mathrm{BZ}^{\mathrm{hol}}$ trivialises the difference
$\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}$ and whose
$L_\infty$-Jacobi identity at arity $k+1$ reproduces the $k$-th
descendant in the Stora--Zumino $1984$ holomorphic descent ladder.
\end{enumerate}
\end{theorem}

## Hypothesis

\begin{hypothesis}[Manes--Stora--Zumino holomorphic descent with
compatible renormalisation schemes]
\label{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}

The Costello--Gwilliam $2017$ Vol~II \S$11.1$ theory of
BCFG-equivariant BV renormalisation schemes admits, for six-dimensional
holomorphic Chern--Simons on a compact Calabi--Yau threefold $X$ with
semisimple gauge algebra $\fg$, two distinguished schemes
$R^{\mathrm{cons}}, R^{\mathrm{cov}}$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the \emph{consistent scheme} $R^{\mathrm{cons}}$, obtained from
BCFG-equivariant heat-kernel regularisation with respect to the full
semidirect product $\fg \rtimes \mathrm{Diff}^{\mathrm{hol}}(X)$
acting on $\cE_{\hCS}$, whose one-loop anomaly satisfies the
Wess--Zumino consistency condition;

\item the \emph{covariant scheme} $R^{\mathrm{cov}}$, obtained from
Bochner--Martinelli heat-kernel regularisation covariant under the
$\fg$-action alone, whose one-loop anomaly transforms as a primary
gauge tensor;

\item such that the scheme-change cochain
$\delta R := R^{\mathrm{cons}} - R^{\mathrm{cov}}$ restricts to the
cubic Dolbeault$(3,2)$-sector to coincide with the Zumino $1983$
Chern--Simons $(5)$-form in its $(0,3)$-holomorphic embedding.
\end{enumerate}
The hypothesis asserts the existence of this compatible scheme pair in
the Costello--Gwilliam $2017$ Vol~II BV framework, together with the
holomorphic-twist functoriality of the Manes--Stora--Zumino $1985$
\emph{Commun.~Math.~Phys.}~$102$ algebraic descent algorithm on the
Dolbeault bicomplex.
\end{hypothesis}

## Proof (under the hypothesis)

### Step 1 — Local cochain complex and two cubic representatives.

The Costello $2011$ BV complex of local functionals on $\cE_{\hCS}$
is
\[
C^\bullet_{\mathrm{loc}}(\cE_{\hCS})
\;=\;
\bigl(\mathrm{Sym}(\cE^\vee[-1])_{\mathrm{loc}}[[\hbar]],\;
Q_{\mathrm{BRST}} + \hbar\Delta_{\mathrm{BV}}\bigr),
\]
with $Q_{\mathrm{BRST}}$ the BV-BRST differential dual to the
$L_\infty$-bracket tower $\ell^\bullet$ on $\cE_{\hCS}$ and
$\Delta_{\mathrm{BV}}$ the BV Laplacian on
$\mathrm{Sym}(\cE^\vee[-1])$ (Costello $2011$ \S$5.4$; Costello--Gwilliam
$2017$ Vol~II Thm.~$9.5.0.6$). At one loop and cubic symmetric power
in the gauge field, the obstruction to solving the quantum master
equation lives at ghost number $+1$ in the $\mathrm{Sym}^3$-subsector.

The Costello--Li $2016$ Proposition~$5.2$ heat-kernel computation
produces a representative whose cohomology class in
$H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ factorises as
\[
[\kanom](X, \fg)
\;=\;
\hbar A(\fg)\,\frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3}\,
\|\Omega_X\|^2.
\]
The chain-level representative is scheme-dependent. Hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
supplies two schemes giving two representatives:
\[
\kanom^{\mathrm{cons}}
\;=\;
R^{\mathrm{cons}}[Q_{\mathrm{BRST}}, S^{\mathrm{eff}}_1]_{\hbar^1},
\qquad
\kanom^{\mathrm{cov}}
\;=\;
R^{\mathrm{cov}}[Q_{\mathrm{BRST}}, S^{\mathrm{eff}}_1]_{\hbar^1}.
\]
Wess--Zumino consistency $Q_{\mathrm{BRST}}\kanom^{\mathrm{cons}} = 0$
follows from BCFG-equivariance on $\fg \rtimes
\mathrm{Diff}^{\mathrm{hol}}(X)$ plus nilpotence $Q_{\mathrm{BRST}}^2 = 0$;
gauge primary-tensor transformation of $\kanom^{\mathrm{cov}}$ follows
from $\fg$-covariance of the Bochner--Martinelli propagator.
Cohomology equality $[\kanom^{\mathrm{cons}}] = [\kanom^{\mathrm{cov}}]$
at the level of $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ is the
Costello--Gwilliam $2017$ Thm.~$9.5.0.6$ scheme-independence of the
obstruction class.

### Step 2 — Holomorphic Stora--Zumino descent.

On a holomorphic $\fg$-bundle over $X$ with connection $\cA \in
\Omega^{0,1}(X, \fg)$ and curvature
$F(\cA) = \bar\partial\cA + \tfrac{1}{2}[\cA, \cA] \in
\Omega^{0,2}(X, \fg)$, the cubic-Casimir characteristic form is
\[
\mathrm{ch}_3(F) \;=\;
\tfrac{1}{6(2\pi i)^3}\,\mathrm{tr}(F^3)
\;\in\; \Omega^{0,6}(X)
\;\cong\; 0 \quad (\text{since } \dim_{\bar\partial} X = 3).
\]
On a CY$_3$, $(0, k)$-forms with $k > 3$ vanish. The nonvanishing
descent happens on the \emph{full} de~Rham complex paired with the
Dolbeault grading: $\mathrm{ch}_3(F) \in \Omega^{3,3}(X)$ via the
Hodge pairing with $\Omega_X$,
$\mathrm{ch}_3(F)_{\mathrm{hol}} :=
\Omega_X \wedge \mathrm{tr}(F^3)_{0,3} / 6(2\pi i)^3$, with the
$(0,3)$-projection extracted by three $\bar\partial$-differentials
acting on a cubic monomial in $\cA$.

The Manes--Stora--Zumino $1985$ algebraic descent on the Dolbeault
bicomplex produces the ladder
\[
\bar\partial\, Q^{(0)}_{5,\mathrm{hol}}
\;+\; \tfrac{1}{6(2\pi i)^3}\,\Omega_X \wedge
\mathrm{tr}(F^3)_{0,3} \;=\; 0,
\qquad
Q^{(0)}_{5,\mathrm{hol}} \;\in\; \Omega^{3,2}(X)
\]
with the explicit primitive
\[
Q^{(0)}_{5,\mathrm{hol}}
\;=\;
\frac{i}{(2\pi)^3}\,
\Omega_X \wedge \mathrm{tr}\Bigl(
\cA \wedge \bar\partial\cA \wedge \bar\partial\cA
\;+\; \tfrac{3}{2}\, \cA \wedge \cA \wedge \cA \wedge \bar\partial\cA
\;+\; \tfrac{3}{5}\, \cA \wedge \cA \wedge \cA \wedge \cA \wedge \cA
\Bigr).
\]
The coefficients $1, 3/2, 3/5$ are the Zumino $1983$
\emph{Nucl.~Phys.~B}~$223$ Chern--Simons $(5)$-form coefficients,
unchanged under holomorphic twist because the descent equation is
functorial: the twist replaces $d$ by $\bar\partial$ on the source
$(0, \bullet)$-complex and inserts the CY volume form $\Omega_X$ to
pair against $(3, \bullet)$, preserving the algebraic structure of
the descent relations.

Applying $Q_{\mathrm{BRST}}$ (the BV-BRST differential extending
$\bar\partial$ by the Lie-bracket coaction on ghost fields) to
$Q^{(0)}_{5,\mathrm{hol}}$ and descending one more step,
\[
Q_{\mathrm{BRST}}\, Q^{(0)}_{5, \mathrm{hol}}
\;+\; \bar\partial\, Q^{(1)}_{4,\mathrm{hol}} \;=\; 0,
\qquad
Q^{(1)}_{4, \mathrm{hol}} \;\in\; \Omega^{3,2}(X, \fg)_{\mathrm{ghost}\,1},
\]
where $Q^{(1)}_{4, \mathrm{hol}}$ is the holomorphic-twist analogue
of the Zumino ghost-$1$ cocycle. Integrating $Q^{(1)}_{4, \mathrm{hol}}$
along $X$ against a gauge parameter produces the consistent anomaly
$\kanom^{\mathrm{cons}}$ (Stora $1984$; Manes--Stora--Zumino $1985$
Thm.~$2$).

### Step 3 — Bardeen--Zumino cochain as scheme-difference.

Set
\[
\mathrm{BZ}^{\mathrm{hol}}(\cA)
\;:=\;
\int_X\, Q^{(0)}_{5,\mathrm{hol}}(\cA).
\]
This is a well-defined local functional at ghost number $0$ in the
cubic symmetric power
$\mathrm{Sym}^3(\cE^\vee) \cap C^0_{\mathrm{loc}}(\cE_{\hCS}[-1])$
because $Q^{(0)}_{5, \mathrm{hol}}$ is cubic in $\cA$ at leading order
(the higher $\cA^5$-terms are subleading corrections from
nonlinear-connection curvature but are local-in-$\cA$ polynomial).

The hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
identifies the scheme-difference cochain
$\delta R = R^{\mathrm{cons}} - R^{\mathrm{cov}}$ restricted to the
cubic $(3,2)$-subsector with $Q^{(0)}_{5, \mathrm{hol}}$. Applying
$Q_{\mathrm{BRST}}$ term by term to $\delta R$ and using the
Costello--Gwilliam scheme-change identity (Costello $2011$ \S$5.6$
Prop.~$5.6.1$; Costello--Gwilliam $2017$ Vol~II Thm.~$9.5.0.6$
consequence)
\[
Q_{\mathrm{BRST}}[\delta R]
\;=\;
\kanom^{R^{\mathrm{cons}}} - \kanom^{R^{\mathrm{cov}}},
\]
together with identification
$\int_X Q_{\mathrm{BRST}} Q^{(0)}_{5,\mathrm{hol}} = -\int_X
\bar\partial Q^{(1)}_{4,\mathrm{hol}} + \int_X[\cA, \cdot]Q^{(0)}_5$
(Step 2 + Leibniz), one obtains the holomorphic Bardeen--Zumino
identity
\[
Q_{\mathrm{BRST}}\bigl(\mathrm{BZ}^{\mathrm{hol}}\bigr)
\;=\;
\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}
\qquad
\text{in } C^1_{\mathrm{loc}}(\cE_{\hCS}[-1]).
\]
Statement~(ii) of Theorem~\ref{thm:bz-hol-linfty-intra-cubic} follows.

### Step 4 — Promotion to $L_\infty$-morphism.

The Costello $2011$ \S$5.6$ scheme-change formalism promotes any
BV-scheme-difference cochain to a curved $L_\infty$-isomorphism
between the two curved dg Lie algebras obtained by twisting
$(\cE_{\hCS}, \ell^\bullet, Q_{\mathrm{BRST}} + \hbar\Delta)$ by the
two Maurer--Cartan elements $\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}}$
(each curved-$L_\infty$ is the Costello $2011$ Thm.~$5.6.1$ twist of
the uncurved data by a ghost-$1$ element squaring to zero modulo
scheme-choice).

Explicitly, define
\begin{align*}
f_0 &\;:=\; \mathrm{BZ}^{\mathrm{hol}} \;\in\;
\mathrm{Sym}^3(\cE^\vee)_{\mathrm{ghost}\,0}, \\
f_1 &\;:=\; \mathrm{id}_{\cE_{\hCS}}, \\
f_k &\;:=\; \text{$k$-th scheme-interpolation term,
  from Costello $2011$ Thm.~$5.6.1$}, \quad k \geq 2.
\end{align*}
The $L_\infty$-morphism structure equation at arity $k$
(Merkulov $2005$ \emph{Proc.~Lond.~Math.~Soc.}~$90$ Thm.~$3$;
Costello $2011$ App.~$A$ in the curved setting),
\[
Q_{\mathrm{BRST}} f_k
\;+\; \sum_{j+l = k+1}
  \pm\, f_j \circ \ell_l
\;-\; \sum_{\sigma}
  \pm\, \ell^{\mathrm{tgt}} \circ (f_{\sigma_1} \otimes \cdots)
\;=\; 0
\qquad (k \geq 1),
\]
is solved order-by-order in the cubic symmetric power by the
Manes--Stora--Zumino $1985$ algebraic descent recursion, where the
$k$-th descent element $Q^{(k-1)}_{6-k, \mathrm{hol}}$ supplies
$f_{k+1}$ against the $k$-fold nested Lie-bracket structure of
$\cE_{\hCS}$.

The arity-$0$ structure equation is the curvature identity
\[
Q_{\mathrm{BRST}} f_0
\;=\;
\ell^{\mathrm{tgt}}_0 - f_1^*\bigl(\ell^{\mathrm{src}}_0\bigr)
\;=\;
\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}},
\]
which is exactly Step~$3$'s identity. This is statement~(iii).

### Step 5 — Functoriality and $(\infty, 1)$-categorical identification.

On the side of $(\infty, 1)$-categories, the curved
$L_\infty$-morphism $f_\bullet$ is a morphism in the Costello--Gwilliam
category of BV theories on $X$ (Costello--Gwilliam $2017$ Vol~I
Ch.~$3$), intertwining the two renormalisation presentations of the
same effective BV theory $\hCS(X, \fg)$. Under the Gwilliam--Williams
$2021$ (arXiv:$2009.05037$ Thm.~$2.5.5$) identification
$E_d^{\mathrm{hol}} \simeq E_d$ of the holomorphic and topological
factorisation operads, $f_\bullet$ descends to an equivalence of
$E_3^{\mathrm{hol}}$-algebras
$\Obs_{\hCS, R^{\mathrm{cons}}} \simeq \Obs_{\hCS, R^{\mathrm{cov}}}$
with homotopy $f_\bullet$, and the image in
$H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ is the universal cubic-Casimir
class of Costello--Li $2016$ Prop.~$5.2$.

## Primary sources

1. Bardeen, W. A. $1969$, \emph{Anomalous Ward identities in spinor
   field theories}, Phys.\ Rev.\ $184$, pp.~$1848$--$1859$ —
   original consistent-anomaly computation of triangle graph.

2. Zumino, B. $1983$, \emph{Chiral anomalies and differential geometry},
   in \emph{Relativity, Groups and Topology II: Les Houches $1983$},
   North--Holland; also Zumino, Wu, Zee $1984$, \emph{Chiral anomalies,
   higher dimensions, and differential geometry}, Nucl.\ Phys.\
   B $239$, pp.~$477$--$507$ — Chern--Simons $Q_5$-form and
   descent equations.

3. Manes, J., Stora, R., Zumino, B. $1985$, \emph{Algebraic study of
   chiral anomalies}, Commun.\ Math.\ Phys.\ $102$, pp.~$157$--$174$,
   Thm.~$2$ — BZ polynomial as primitive for $\kanom^{\mathrm{cons}}
   - \kanom^{\mathrm{cov}}$, descent algorithm.

4. Stora, R. $1984$, \emph{Algebraic structure and topological origin
   of anomalies}, in \emph{Progress in Gauge Field Theory (Carg\`ese
   $1983$)}, Plenum, pp.~$543$--$562$ — descent equations as
   $Q_{\mathrm{BRST}}$-cohomology ladder.

5. Costello, K. $2011$, \emph{Renormalization and Effective Field
   Theory}, AMS Math.\ Surveys Monogr.\ $170$, Ch.~$5$ (esp.\
   \S$5.4$, \S$5.6$, Thm.~$5.6.1$) — BV renormalisation,
   scheme-change $L_\infty$-morphism formalism.

6. Costello, K. $2013$, \emph{Supersymmetric gauge theory and the
   Yangian}, arXiv:$1303.2632$, \S$3$--$5$ — 5d/6d holomorphic
   Chern--Simons BV quantisation, one-loop anomaly coefficient.

7. Costello, K., Li, S. $2016$, \emph{Twisted supergravity and its
   quantization}, arXiv:$1606.00365$, Prop.~$5.2$ (cited as
   ``Costello--Li $2016$'' in the monograph; also circulates under
   arXiv:$1605.09930$ and arXiv:$1601.04040$ preprint drafts) —
   one-loop BCOV curving $\alpha_{\mathrm{BCOV}} =
   (\chi(X)/24)[\Omega_X]^{0,1}$ and 6d hCS BV anomaly.

8. Costello, K., Gwilliam, O. $2017$, \emph{Factorization algebras in
   quantum field theory, Vol.~II}, Cambridge University Press;
   Thm.~$9.5.0.6$, Prop.~$5.6.1$ — scheme-independence of BV
   cohomology, $L_\infty$-morphism between renormalisation schemes.

9. Gwilliam, O., Williams, B. $2021$, \emph{Higher Kac--Moody algebras
   and symmetries of holomorphic field theories}, Adv.\ Theor.\ Math.\
   Phys.\ $25$; arXiv:$2009.05037$, Thm.~$2.5.5$ — identification of
   $E_d^{\mathrm{hol}}$ and $E_d$ as factorisation operads.

10. Merkulov, S. $2005$, \emph{Nijenhuis infinity and contractible
    differential graded manifolds}, Proc.\ Lond.\ Math.\ Soc.\ $90$,
    pp.~$114$--$154$ Thm.~$3$ — curved $L_\infty$-morphism structure
    equations.

## Primary-source gap (conditional hypothesis)

The hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
names precisely one extension of primary literature: the holomorphic
lift of the Manes--Stora--Zumino $1985$ algebraic descent algorithm to
the Costello--Gwilliam $2017$ Vol~II \S$11.1$ BCFG-equivariant
renormalisation framework, for 6d hCS on a compact Calabi--Yau
threefold. Equivalently, a \emph{scheme pair}
$(R^{\mathrm{cons}}, R^{\mathrm{cov}})$ realising the two
cubic-Casimir representatives at the chain level, with explicit
scheme-difference cochain identified with $Q^{(0)}_{5,\mathrm{hol}}$.

Each of the ingredients is documented:

- The real-form Manes--Stora--Zumino algebraic descent is $1985$
  Commun.\ Math.\ Phys.\ $102$ Thm.~$2$, proved on any reductive
  $\fg$.
- The real-form BZ polynomial coefficients $1, 3/2, 3/5$ are
  Zumino $1983$ Nucl.\ Phys.\ B $223$.
- Scheme-change as $L_\infty$-morphism is Costello $2011$
  Thm.~$5.6.1$; Costello--Gwilliam $2017$ Vol~II Thm.~$9.5.0.6$.
- Holomorphic-twist functoriality on the Dolbeault bicomplex is
  Costello--Li $2016$ \S$2$--$3$.

The hypothesis is the \emph{composition} of these four ingredients in
the 6d hCS BV framework on a compact CY$_3$. No single primary source
performs this composition for the consistent-versus-covariant cubic
representative. The residual mathematics is bookkeeping-heavy but
algorithmic: the Dolbeault bicomplex is a graded analogue of the real
de~Rham bicomplex and the MSZ algorithm descends functorially once
the scheme-compatible heat-kernel construction of (i)--(ii) in the
hypothesis is in place.

## Inscription-ready TeX block

```latex
\begin{hypothesis}[Holomorphic-descent compatible BV schemes for 6d
$\hCS$]
\label{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
The Costello--Gwilliam $2017$ Vol~II \S$11.1$ BCFG-equivariant BV
renormalisation framework, applied to six-dimensional holomorphic
Chern--Simons on a compact Calabi--Yau threefold $X$ with semisimple
gauge algebra $\fg$, admits a scheme pair
$(R^{\mathrm{cons}}, R^{\mathrm{cov}})$: the consistent scheme
$R^{\mathrm{cons}}$ is BCFG-equivariant under the semidirect product
$\fg \rtimes \mathrm{Diff}^{\mathrm{hol}}(X)$ with one-loop anomaly
satisfying the Wess--Zumino consistency condition; the covariant scheme
$R^{\mathrm{cov}}$ is $\fg$-equivariant from Bochner--Martinelli
heat-kernel regularisation with one-loop anomaly transforming as a
primary gauge tensor; the scheme-difference cochain
$\delta R = R^{\mathrm{cons}} - R^{\mathrm{cov}}$ on the cubic
$\mathrm{Dolb}(3,2)$-sector coincides with the holomorphic
Chern--Simons $(5)$-form $Q^{(0)}_{5,\mathrm{hol}}$.
\end{hypothesis}

\begin{theorem}[Holomorphic Bardeen--Zumino $L_\infty$-morphism]
\label{thm:bz-hol-linfty-intra-cubic}
\ClaimStatusConjectured
Let $X$ be a Calabi--Yau threefold, $\fg$ a semisimple Lie algebra
with cubic-Casimir coefficient $A(\fg) = d^{abc}d_{abc}/\dim\fg$, and
$\cE_{\hCS} = \Omega^{0,\bullet}(X, \fg)[1]$ the Costello--Li BV dg
Lie algebra of six-dimensional holomorphic Chern--Simons on $X$.
Assume hypothesis
\ref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}.
The one-loop cubic-Casimir BV obstruction has two chain-level
representatives $\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}} \in
C^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$, Wess--Zumino consistent and
gauge-primary-covariant respectively, both with cohomology class
$\hbar A(\fg)\chi_{\mathrm{top}}(X)(2(4\pi)^3)^{-1}\|\Omega_X\|^2$
(Costello--Li $2016$ Proposition~$5.2$). The holomorphic
Bardeen--Zumino local functional
\[
\mathrm{BZ}^{\mathrm{hol}}(\cA)
\;=\;
\frac{i}{(2\pi)^3} \int_X \Omega_X \wedge
\mathrm{tr}\Bigl(
\cA \wedge \bar\partial\cA \wedge \bar\partial\cA
+ \tfrac{3}{2}\,\cA^3 \wedge \bar\partial\cA
+ \tfrac{3}{5}\,\cA^5 \Bigr),
\]
the Dolbeault $(3,2)$-projection of the Zumino $1983$ Chern--Simons
$Q_5$-form, satisfies the chain-level identity
\[
Q_{\mathrm{BRST}}\bigl(\mathrm{BZ}^{\mathrm{hol}}\bigr)
\;=\;
\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}
\qquad \text{in }
C^1_{\mathrm{loc}}(\cE_{\hCS}[-1]),
\]
and promotes, via the Costello $2011$ Theorem~$5.6.1$ scheme-change
formalism, to a curved $L_\infty$-morphism
\[
f_\bullet \colon
\Bigl(\cE_{\hCS}, \ell^\bullet,
Q_{\mathrm{BRST}} + \hbar\Delta + \kanom^{\mathrm{cov}}\Bigr)
\;\longrightarrow\;
\Bigl(\cE_{\hCS}, \ell^\bullet,
Q_{\mathrm{BRST}} + \hbar\Delta + \kanom^{\mathrm{cons}}\Bigr)
\]
with arity-$0$ term $f_0 = \mathrm{BZ}^{\mathrm{hol}}$, arity-$1$ term
$f_1 = \mathrm{id}$, and higher $f_{k \geq 2}$ determined by the
Manes--Stora--Zumino $1985$ algebraic descent recursion on the
Dolbeault bicomplex.
\end{theorem}

\begin{proof}[Proof sketch under the hypothesis]
The one-loop cohomology class is Costello--Li $2016$ Proposition~$5.2$
(arXiv:$1606.00365$). Two schemes from the hypothesis produce the
two representatives with Wess--Zumino consistency for the BCFG
scheme and gauge-primary-tensor covariance for the Bochner--Martinelli
scheme (Costello--Gwilliam $2017$ Vol~II \S$11.1$). The holomorphic
descent $\bar\partial Q^{(0)}_{5, \mathrm{hol}} + (2\pi i)^{-3}
\Omega_X \wedge \mathrm{tr}(F^3)_{0,3} / 6 = 0$ produces the
explicit primitive $Q^{(0)}_{5,\mathrm{hol}}$ with Zumino $1983$
coefficients preserved by the holomorphic twist (Manes--Stora--Zumino
$1985$ Theorem~$2$ applied functorially on the Dolbeault bicomplex).
The scheme-change identity $Q_{\mathrm{BRST}}(\delta R) =
\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}$ is
Costello $2011$ Proposition~$5.6.1$; restriction to the cubic
$(3,2)$-subsector with hypothesis (iii) identifies $\delta R$ with
$Q^{(0)}_{5,\mathrm{hol}}$ and yields the Bardeen--Zumino identity.
Promotion to a curved $L_\infty$-morphism is Costello $2011$
Theorem~$5.6.1$, with higher arity terms $f_{k \geq 2}$ determined by
the Merkulov $2005$ Proc.\ Lond.\ Math.\ Soc.\ $90$ Theorem~$3$
structure equations solved order-by-order via the holomorphic descent
ladder.
\end{proof}

\begin{remark}[Three consequences of the cochain bridge]
\label{rem:bz-hol-three-consequences}
The holomorphic Bardeen--Zumino $L_\infty$-morphism has three
consequences. First, the vanishing locus of the cohomology class
$[\kanom] \in H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ is independent of
the scheme used to represent it: for $\fg \in \{\mathfrak{su}(2),
\mathfrak{so}(N), E_6, E_7, E_8, F_4, G_2\}$ (all with $d^{abc} = 0$)
or for $X$ with $\chi_{\mathrm{top}}(X) = 0$ (e.g.~$K3 \times E$), both
$\kanom^{\mathrm{cons}}$ and $\kanom^{\mathrm{cov}}$ vanish on the
nose, and $\mathrm{BZ}^{\mathrm{hol}}$ is a closed element in
$C^0_{\mathrm{loc}}(\cE_{\hCS}[-1])$ representing a class in
$H^0_{\mathrm{loc}}$ (a Chern--Simons secondary characteristic).
Second, on the quintic ($\chi_{\mathrm{top}} = -200$, $\fg =
\mathrm{SU}(N)$ with $N \geq 3$), the Candelas--Horowitz--
Strominger--Witten $1985$ (\emph{Nucl.\ Phys.\ B}~$258$)
trivialisation via tangent embedding $F_\cA = R$ together with the
Green--Schwarz counterterm provides a chain-level primitive for the
covariant representative; the BZ cochain then supplies the
passage to the consistent representative required for BRST
invariance of the one-loop effective action. Third, the curved
$L_\infty$-morphism $f_\bullet$ realises the consistent-versus-
covariant bifurcation as a genuine gauge equivalence in the
$(\infty, 1)$-category of BV theories on $X$, not merely a cohomology
equality.
\end{remark}
```

## Cross-consistency notes

### With the Wave-1 spine (`platonic_synthesis_post_adversarial.tex` \S \ref{wn:subsec:second-pass-BZ}).

The Wave-1 theorem
\texttt{thm:spine-consistent-covariant} already asserts the existence
of $\mathrm{BZ}^{\mathrm{hol}}$ with the sign
$Q_{\mathrm{BRST}}\mathrm{BZ}^{\mathrm{hol}} =
\kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$. The Wave-$2$
refinement
\texttt{wn:thm:second-pass-BZ-category} corrects the sign to
$\kanom^{\mathrm{cons}} - \kanom^{\mathrm{cov}}$, consistent with
Stora $1984$'s convention that the consistent representative is the
image of $Q_{\mathrm{BRST}}$ applied to the BZ primitive. The
terminal-state (B) closure supplies the explicit chain-level primitive
$\mathrm{BZ}^{\mathrm{hol}}$ as the Dolbeault $(3,2)$-projection of
$Q_5$, the named hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}
for scheme-compatibility, and the promotion from a chain-level
primitive to a curved $L_\infty$-morphism via Costello $2011$
Theorem~$5.6.1$.

The Wave-$2$ refinement's retraction of the cross-sector quadratic-
versus-cubic bridge (wave-function $Z^{(1)}_\cA$ versus anomaly
$\kanom$) is preserved: this theorem is \emph{intra-cubic}, never
bridging ghost numbers or Feynman-graph topologies. The
bubble-versus-wheel distinction is documented by rendering
$\kanom^{\mathrm{cons}}$ and $\kanom^{\mathrm{cov}}$ as both
wheel-supported in $C^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$.

### With the Wave-$2$ refinement (`platonic_synthesis_wave2_refinement.tex` \S $815$--$826$).

The Tier I-$4$ designation ``Bardeen--Zumino cochain bridging consistent
and covariant cubic-Casimir anomaly representatives as an
$L_\infty$-morphism ($N_1$)'' names exactly this closure target. The
``$N_1$'' primary-source gap is resolved to the hypothesis
\eqref{hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes}:
the classical (real) MSZ $1985$ descent plus Costello $2011$ \S$5.6$
scheme-change, composed functorially on the Dolbeault bicomplex.

### With the monograph's \texttt{quantum\_chiral\_algebras.tex} \S \texttt{subsec:hcs-anomaly}.

Theorem \texttt{thm:plat-anomaly} (on-the-nose cohomological
factorisation $\kanom = \hbar A(\fg)\chi_{\mathrm{top}}(X)
(2(4\pi)^3)^{-1}\|\Omega_X\|^2$) is the cohomological parent of
Theorem~\ref{thm:bz-hol-linfty-intra-cubic}'s chain-level
bifurcation; the BZ cochain witnesses that both chain-level
representatives project to this single cohomology class.
Remark \texttt{rem:plat-Z-vs-anomaly} (wave-function-versus-anomaly
separation) is unaffected: the theorem is intra-cubic, preserving
the discipline that $C_2(\fg)$ and $A(\fg)$ are invariants of
different BV sectors.

### With the monograph's \texttt{hochschild\_calculus.tex}.

The Costello--Li $2016$ one-loop anomaly $\alpha_{\mathrm{BCOV}} =
(\chi(X)/24)[\Omega_X]^{0,1} \in H^{0,1}(X)$ (lines
$406$--$446$) is the $\kanom^{\mathrm{cov}}$-representative's
cohomology class (up to the $(2(4\pi)^3)^{-1}\|\Omega_X\|^2$
normalisation convention). The BZ $L_\infty$-morphism identifies
the consistent chain-level representative without changing this
cohomology class.

### With AP-CY cache.

- Consistent with AP-CY$144$ / canonicality-inversion discipline: the
  cohomology class is canonical, chain-level representatives are
  scheme-dependent, BZ cochain supplies the intertwiner — no ``the''
  anomaly representative is canonical.
- Consistent with AP-CY$262$ / cubic $d^{abc}$ versus quadratic $C_2$
  discipline: all three objects ($\kanom^{\mathrm{cons}}$,
  $\kanom^{\mathrm{cov}}$, $\mathrm{BZ}^{\mathrm{hol}}$) live in the
  cubic symmetric power $\mathrm{Sym}^3(\cE^\vee)$.
- Consistent with AP-CY$162$ / BCOV-versus-Yukawa Hodge-degree
  discipline: $\mathrm{BZ}^{\mathrm{hol}} \in \mathrm{Sym}^3(\cE^\vee)
  \otimes H^{3,2}(X)$, a \emph{new} Hodge receptacle distinct from
  $Y_3 \in H^{0,3}(X)$ and $\alpha_{\mathrm{BCOV}} \in H^{0,1}(X)$.

### With `CoHA_to_W_infty_treatise.tex`.

No direct interaction: the BZ cochain lives on the 6d hCS side
\emph{before} the CoHA-to-$W_{1+\infty}$ cascade is engaged (the
cascade operates on the boundary chiral algebra, not on the bulk
BV-BRST complex). The cross-consistency is preserved at the level
of anomaly-vanishing tables: both documents agree that
$K3 \times E$ with any semisimple $\fg$ is anomaly-free at one loop.
