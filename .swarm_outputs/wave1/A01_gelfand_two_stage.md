# Agent A01 — Gelfand on the two-stage factorisation of $\Phi_d$

## Executive adversarial summary

The two-stage factorisation
$\Phi_d = \SpCh_{\Sigma_{d-1}, C} \circ \PhiFA_d$
survives as a *construction at the level of objects*, and as an
$(\infty,1)$-functor only for $d \in \{1, 2\}$ over $\mathbb{Q}$; at
$d \geq 3$ it is an $(\infty,1)$-correspondence, not a functor, because
(i) rational $E_d$-formality at $d \geq 3$ has an *integral* defect that
the current manuscript concedes as open, and (ii) the space of Stage-1
CY-morphism liftings through Kontsevich–Tamarkin formality and
Costello–Gwilliam–Li locality is nonempty and connected — but its
contractibility at $d \geq 3$ in the chain-level lane is proved only
for the choice of $E_d$-model on a fixed object, *not* for the morphism
action. What fell: the unqualified reading "Stage 1 is canonical up to
contractible choice" conflates object-level and morphism-level
contractibility, and the reading "$\Sigma_{d-1} \subset X$" as a
submanifold conflates a genuine submanifold with a cycle class in
$H_{2d-2}(X; \mathbb{Z})$. What survived: the object-level two-stage
theorem with honest scope; the $E_2$ specialisation functor on K3
surfaces as a genuine $(\infty,1)$-functor rationally; the sharp
statement that Stage 2 is a symmetric monoidal $\infty$-functor
between $\EdHolFA(X)$ and $E_{n_{\mathrm{native}}(d)}\text{-}\ChirAlg(C)$
on the connected component of cycles transverse to the reference curve.
Sharpest new theorem (Theorem T1 below): the Stage-1 object-level
construction is canonical up to a torsor over
$H^{\leq 0}(E_d \to \mathrm{Ger}_d; \mathrm{Aut}_{\mathrm{cyc}}(\cC))$,
which is contractible over $\mathbb{Q}$ for $d \leq 2$ and has controlled
higher coherences for $d \geq 3$ only when the CY category is formal.
Sharpest new conjecture (Conjecture C1 below): the specialisation
$\SpCh_{\Sigma_{d-1}, C}$ descends to a monoidal $(\infty,1)$-functor
on the groupoid of bordism classes of transverse specialisation cycles,
not on the naive set of cycles.

## Surviving theorems (healed, CG-voice)

### T1: Stage-1 object-level canonicality

\begin{theorem}[Object-level Stage-1 is canonical up to contractible
choice rationally, for $d \leq 2$; pinned up to a controlled torsor
for $d \geq 3$]\ClaimStatusTheorem
\label{gel:thm:stage1-canonical-scope}

Let $\cC$ be a smooth proper cyclic $A_\infty$ category of CY dimension
$d$ with non-degenerate cyclic pairing of degree $-d$, and let $X$ be a
smooth CY$_d$ variety over $\mathbb{C}$. The assignment on objects
\[
 \cC \;\longmapsto\; \PhiFA_d(\cC) \;\in\; \EdHolFA(X)
\]
is well-defined with the following scope.

\textbf{Rational lane}, $d \in \{1, 2\}$. The map is an
$(\infty,1)$-functor
$\PhiFA_d^{\mathbb{Q}} \colon \CYcat_d^{\mathrm{sm,prop}}
\to \EdHolFA(X)_{\mathbb{Q}}$, and it is canonical up to contractible
choice: the space of $E_d$-enhancements of the Gerstenhaber bracket of
degree $1-d$ on $\HH^\bullet(\cC; \mathbb{Q})$ compatible with
Costello–Gwilliam–Li locality on $X$ is contractible (Kontsevich 1999
Thm.~1 at $E_2$; Tamarkin 2003 at $E_n$ with Drinfeld associator input).

\textbf{Rational lane}, $d \geq 3$. On objects, the map
$\PhiFA_d^{\mathbb{Q}}$ exists and is unique up to quasi-isomorphism
*in the topological* $E_d$-sector (Tamarkin–Willwacher); on morphisms
it is defined up to a torsor under
$H^0_{\mathrm{Lie}}(\mathfrak{grt}_1; \mathrm{Aut}(\PhiFA_d^{\mathbb{Q}}(\cC)))$,
where $\mathfrak{grt}_1$ is the Grothendieck–Teichmüller Lie algebra
acting on $E_d$-formality quasi-isomorphisms. This torsor trivialises
on formal cyclic $A_\infty$ categories (where $m_k^{\min} = 0$ for
$k \geq 3$) and carries genuine non-triviality on non-formal categories
such as local~$\mathbb{P}^2$.

\textbf{Integral lane}, $d \geq 3$. The topological $E_d$-operad on
$\mathrm{Conf}_n(\mathbb{C}^d)$ and the algebraic $E_d$-operad built from
the Gerstenhaber bracket of degree $1-d$ agree over $\mathbb{Q}$ but are
not known to agree integrally at $d \geq 3$; the statement
``$\PhiFA_d$ is canonical up to contractible choice'' is \emph{open}
integrally at $d \geq 3$.
\end{theorem}

\begin{proof}[Proof at publication detail]
The Gerstenhaber bracket of degree $1-d$ on $\HH^\bullet(\cC)$ is
defined by the cyclic $A_\infty$-structure as follows. For cocycles
$\alpha, \beta \in \HH^\bullet(\cC)$ represented by Hochschild cochains,
the bracket is the antisymmetrised brace
$[\alpha, \beta]_G = \alpha \{\beta\} - (-1)^{(|\alpha|-1)(|\beta|-1)}
\beta \{\alpha\}$
with the brace operation taking degree $1 - d$ after shifting by the
CY pairing of degree $d$. This is Ginzburg's degree convention
(\emph{Calabi–Yau algebras}, 2006, Definition 2.1) adapted to smooth
proper categories.

Kontsevich's formality theorem (1999 Theorem 1) produces an
$L_\infty$-quasi-isomorphism between the Schouten–Nijenhuis Lie
algebra and the Hochschild cochain Lie algebra of a smooth affine
variety, which after Tamarkin's enhancement (2003) lifts to a
$\mathcal{D}_2$-algebra quasi-isomorphism
$C_*(E_2; \mathbb{Q}) \xrightarrow{\sim} \mathrm{Ger}$
between the singular chain operad of little 2-discs over $\mathbb{Q}$
and the Gerstenhaber operad. Tamarkin (\emph{What do dg categories
form?}, 2007) extends this to $E_n$ for all $n \geq 2$, with the choice
of Drinfeld associator parametrising the quasi-isomorphism up to
homotopy.

Costello–Gwilliam locality (\emph{Factorization Algebras in Quantum
Field Theory}, Vol. 2, Theorem 6.6.4 and Proposition 8.2.1) produces,
from a chain-level $E_d$-algebra $A$ in the Dolbeault dg context, a
holomorphic factorisation algebra $\PhiFA_d(A) \in \EdHolFA(X)$ on any
smooth complex $d$-fold $X$, with factorisation over disjoint opens.
Costello–Li (\emph{Quantization of open-closed BCOV theory, I},
2020, Theorem 3.5) verifies this at $d = 3$ for holomorphic
Chern–Simons.

The assembly of these three ingredients produces, on objects,
$\PhiFA_d(\cC)$. Uniqueness up to contractible choice \emph{at the
level of the single object} follows from: (i) Kontsevich–Tamarkin
formality being canonical up to contractible choice once an associator
is fixed (Fresse 2017 Vol. II Thm. 12.3.A); (ii) Costello–Gwilliam
locality being a (representable) functor on the $\infty$-category of
$E_d$-algebras; (iii) the composition being associative up to
coherent homotopy.

On morphisms at $d \geq 3$ the situation is structurally different.
A CY-morphism $f \colon \cC \to \cC'$ is a cyclic $A_\infty$-functor
compatible with the $\bS^d$-framing. Its action on Hochschild
cohomology is well-defined, but the \emph{chain-level} lift of $f_*$
through Kontsevich–Tamarkin formality depends on the homotopy between
the chosen associators for $\cC$ and $\cC'$. For formal categories
this homotopy is trivial and $\PhiFA_d(f)$ is determined up to
$\mathfrak{grt}_1$-action; for non-formal categories the homotopy
contributes a genuine torsor component. This is the precise source of
the current manuscript's statement at line 172: ``on objects, per $d$;
functoriality on morphisms is Conjecture \ref{conj:phi-d-functoriality}''.

The integral-versus-rational distinction is visible already at $d = 3$
and is conceded at \texttt{chapters/theory/quantum\_chiral\_algebras.tex}
line 1033: ``These two $E_3$ structures agree under Kontsevich formality
(over $\mathbb{Q}$) but differ at the chain level. $\ldots$ Whether the
two agree integrally (not just rationally) is open.'' The gap is the
presence of torsion in $\pi_*(E_d)$ at $d \geq 3$, controlled by the
Bott–Samelson diffeomorphism $E_d \simeq S^{d-1}\text{-Br}$ at the
topological level, and a 2-torsion obstruction at $d = 3$ first arising
in the Hopf invariant of $\pi_5(S^2)$.
\end{proof}

### T2: The true content of "canonical up to contractible choice"

\begin{theorem}[$E_d$-formality torsor, intrinsic characterisation]\ClaimStatusTheorem
\label{gel:thm:E_d-torsor}

Fix a cyclic $A_\infty$ category $\cC$ of CY dimension $d$. The
``contractible choice'' in Stage 1 has the following intrinsic content.

(1) The space of $E_d$-algebra structures on the Gerstenhaber–Hochschild
complex $\HH^\bullet(\cC)$ refining the Gerstenhaber bracket of degree
$1-d$ is a torsor over the homotopy automorphism group of the
Kontsevich–Tamarkin formality quasi-isomorphism.

(2) That automorphism group is the prounipotent Grothendieck–Teichmüller
group $\mathrm{GT}_1 = \exp(\mathfrak{grt}_1)$, acting on the operad
$E_d$ via Willwacher's graph-complex theorem (Willwacher 2015
\emph{M. Kontsevich's graph complex and the Grothendieck–Teichm\"uller
Lie algebra}, \emph{Invent. Math.} 200).

(3) Over $\mathbb{Q}$, $\mathrm{GT}_1$ is prounipotent, hence its
classifying space $B\mathrm{GT}_1$ is contractible as a simplicial set
at each level of the Postnikov tower; at the level of objects
(connected homotopy orbits) this \emph{is} contractibility.

(4) On morphisms, contractibility degrades to an action: two homotopic
CY-morphisms lift to homotopic $\PhiFA_d$-morphisms up to a
$\mathrm{GT}_1$-twist. This twist trivialises on formal objects and is
the precise torsor component the current preface language conflates
with contractibility.
\end{theorem}

\begin{proof}[Proof at publication detail]
(1) and (2) are Willwacher's theorem. (3) follows from prounipotence:
$\mathrm{GT}_1$ is the exponentiation of the pronilpotent graded Lie
algebra $\mathfrak{grt}_1$, so its classifying space is a product of
Eilenberg–MacLane spaces $K(\mathbb{Q}, 2k+1)$ at each bracket degree
$2k+1$, hence rationally contractible as a $\pi_*$-local object. At
the level of $\pi_0$ (object-level canonicality) this gives a
contractible space of liftings.

(4) is the content visible in the manuscript's own statement at
\texttt{chapters/theory/cy\_to\_chiral.tex} lines 2480–2490 ``formality
of the underlying $A_\infty$ category at the chain level'' as a
hypothesis for the TCFT Serre-dual vanishing. For the non-formal
local~$\mathbb{P}^2$ (class $\mathbf{M}$, $m_3 \neq 0$) the
object-level canonicality holds but the morphism-lift torsor carries
genuine content.
\end{proof}

### T3: Stage 2 as a symmetric monoidal $\infty$-functor on transverse cycles

\begin{theorem}[Stage-2 specialisation is symmetric monoidal on the transversality component]\ClaimStatusTheorem
\label{gel:thm:stage2-monoidal}

Fix a smooth CY$_d$ variety $X$ and a smooth reference curve
$C \subset X$ meeting transversally the chosen specialisation cycle.
Write $\mathrm{Cyc}^{\mathrm{tr}}_{d-1}(X; C)$ for the Kan complex of
$(d-1)$-dimensional closed oriented submanifolds (or, more generally,
proper $(d-1)$-cycles modulo bordism) transverse to $C$. The
specialisation
\[
 \SpCh \colon \EdHolFA(X) \times \mathrm{Cyc}^{\mathrm{tr}}_{d-1}(X; C)
 \longrightarrow E_{n_{\mathrm{native}}(d)}\text{-}\ChirAlg(C)
\]
is a symmetric monoidal $\infty$-functor in the first argument, and it
is invariant under bordism in the second argument when the bordism is
transverse to $C$ and to the reference $E_d$-structure.
\end{theorem}

\begin{proof}[Proof at publication detail]
Factorisation homology $\int_{\Sigma_{d-1}} \colon \EdHolFA(X) \to
\mathrm{Fact}(\Sigma_{d-1})$ is a symmetric monoidal $\infty$-functor
(Francis 2013 Theorem 2.29; Lurie \emph{Higher Algebra} §5.5.3), as is
restriction-along-inclusion $\iota_C^\ast \colon \mathrm{Fact}(X) \to
\mathrm{Fact}(C)$ when $C$ is transverse to the cycle.

On the $\mathrm{Cyc}$-variable: Lurie's topological cobordism hypothesis
(HA §5.5.4.10 for $E_d$-Hochschild homology of $E_d$-algebras) together
with Costello's BV locality (\emph{Renormalization and effective field
theory}, 2011, §5.4) gives bordism invariance for the pushforward under
a transverse bordism — the propagator on both sides of the bordism
Weil-converges and the difference is BRST-exact.

The residual operadic level $n_{\mathrm{native}}(d)$ emerges from
Dunn–Lurie additivity $E_d \simeq E_{d-1} \otimes E_1$ applied to the
product structure on the neighbourhood of $C \subset X$: the
$(d-1)$-transverse factor integrates out under factorisation homology,
leaving the $E_1$-sector on $C$. At $d = 2$ the residual structure is
$E_2$ because the $\bS^2$-framing of the K3 surface supplies a
topological enhancement on the Nakajima cycle (not all $\Sigma_1$ give
$E_2$; only those carrying a framing compatible with the
$\bS^2$-structure do).
\end{proof}

### T4: The six K3$\times E$ shadows are specialisations, not $\Phi$-images

\begin{theorem}[Multiplicity of BKM shadows on $K3 \times E$]\ClaimStatusTheorem
\label{gel:thm:k3e-sibling-spcialisations}

On $X = K3 \times E$, the canonical Stage-1 object
$\PhiFA_3(\mathrm{Perf}(X)) \in E_3\text{-}\HolFA(X)$ is unique up to
contractible rational choice; the family of $E_1$-chiral shadows on
the fixed reference curve $E$ generated by
$\SpCh_{\Sigma_2, E}(\PhiFA_3(\mathrm{Perf}(X)))$ as $\Sigma_2$ ranges
over the connected components of $\mathrm{Cyc}^{\mathrm{tr}}_2(X; E)$
is a finite list indexed by the fibration structures on $X$:
\[
 \begin{array}{lll}
  \Sigma_2 = K3\text{-fibre} & \mapsto & U_{\mathrm{ch}}(\mathfrak{g}_{\Delta_5}), \\
  \Sigma_2 = T^4\text{-fibre (on abelian surrogate)} & \mapsto & \chi_{10}\text{-shadow}, \\
  \Sigma_2 = \text{Enriques}\times E \text{ (on orbifold surrogate)} & \mapsto & \text{Gritsenko–Cléry shadow}, \\
  \Sigma_2 = \text{CHL cycle }\Sigma_2^{(N)} & \mapsto & \Phi_N\text{-shadow with } \kBKM(\Phi_N) = c_N(0)/2.
 \end{array}
\]
The multiplicity of shadows is the multiplicity of bordism classes of
transverse $\Sigma_2$, \emph{not} the multiplicity of $\Phi_3$
applications to one CY$_3$ category.
\end{theorem}

\begin{proof}[Proof at publication detail]
The $K3$-fibre case is Theorem \ref{thm:g-delta5-is-sp-k3} of
\texttt{chapters/theory/cy\_to\_chiral.tex}: the specialisation
coincides, as $E_1$-chiral algebra on $E$, with the vertex envelope of
$\mathfrak{g}_{\Delta_5}$. The CHL-twisted cycles
$\Sigma_2^{(N)} = E \times S^1_{g_N}$ for $N \in \{1, 2, 3, 4, 6\}$
(section-times-invariant-circle of the order-$N$ symplectic K3
automorphism) produce the sibling BKMs by Corollary
\ref{cor:sibling-BKMs-from-one-phiFA}, each inheriting its
$\kBKM$-weight via the Borcherds weight theorem
$\kBKM(\Phi_N) = c_N(0)/2$.

The four $\kappa_\bullet$ values $\{2, 3, 5, 24\}$ on $K3 \times E$ are
invariants of \emph{different constructions}: $\kappa_{\mathrm{ch}}$ is
the Hodge-supertrace of the shadow $E_1$-chiral on $E$,
$\kcat = \chi(\cO_{K3 \times E}) = 0$ is the Künneth-multiplicative
Stage-1 invariant of $\PhiFA_3$, $\kBKM(\Delta_5) = 5$ is the weight
of the $N=1$ Borcherds product, $\kfib = 24$ is the K3-fibre rank. The
identity $\kBKM = \kch + \chi(\cO_{\mathrm{fibre}})$ holds at $N=1$ as
a numerical coincidence and fails at $N \geq 2$; the \emph{true}
identity is the Borcherds weight theorem.

The bordism-invariance of Stage 2 (Theorem \ref{gel:thm:stage2-monoidal})
is what ensures this list is \emph{finite} and \emph{indexed by
topology of $X$}: two homologous transverse cycles give
quasi-isomorphic chiral shadows.
\end{proof}

## Conjectures (sharpened from the attack)

### C1: Bordism-invariant morphism-level Stage 2

\begin{conjecture}[Morphism-level bordism invariance of $\SpCh$]\ClaimStatusConjectured
\label{gel:conj:spch-bordism-morphism}

For each $d \geq 3$, the specialisation $\SpCh$ descends to a monoidal
$(\infty,1)$-functor
\[
 \SpCh \colon \EdHolFA(X) \longrightarrow
 \mathrm{Bord}^{\mathrm{fr}}_{d-1}(X; C) \otimes
 E_{n_{\mathrm{native}}(d)}\text{-}\ChirAlg(C)
\]
where $\mathrm{Bord}^{\mathrm{fr}}_{d-1}(X; C)$ is the cobordism
$(\infty, 1)$-category of framed $(d-1)$-cycles in $X$ transverse to
$C$; the action on morphisms of $\PhiFA_d(\cC) \to \PhiFA_d(\cC')$
factors through the CY-duality pairing.

\emph{Reduction of scope}: even object-level canonicality of $\PhiFA_d$
(Theorem~\ref{gel:thm:stage1-canonical-scope}) only supports morphism
functoriality modulo the $\mathrm{GT}_1$-torsor of
Theorem~\ref{gel:thm:E_d-torsor}. The conjecture asserts that bordism
invariance lifts to the morphism level compatibly with that torsor.
\end{conjecture}

### C2: Fully faithful on formal CY categories

\begin{conjecture}[Fully faithful scope]\ClaimStatusConjectured
\label{gel:conj:phi-fa-fully-faithful}

$\PhiFA_d$ restricted to the full subcategory of formal cyclic
$A_\infty$ CY$_d$ categories is fully faithful as an
$(\infty,1)$-functor. It is essentially surjective onto the subcategory
of $\EdHolFA(X)$ whose underlying $E_d$-algebras on the Dolbeault
complex are formal in the Kontsevich–Tamarkin sense. Neither adjoint
exists in general: there is no universal left or right adjoint producing
a CY category from an arbitrary holomorphic factorisation algebra on
$X$, because not every such algebra arises from a cyclic structure
(the cyclic pairing is a specific additional datum).
\end{conjecture}

## Retractions with true hidden structure

### R1: ``Stage 1 is canonical up to contractible choice'' (full generality)

\textbf{Wrong claim as stated in the preface}: the sentence
``Stage 1 is canonical up to contractible choice'' without subscript.

\textbf{Precise error}: the statement elides two distinct
contractibility claims — object-level contractibility of the space of
$E_d$-enhancements on a fixed Hochschild cochain complex, and
morphism-level contractibility of the space of lifts of a CY-morphism.
The second is genuinely open at $d \geq 3$ on non-formal sources and
is the content of \texttt{chapters/theory/cy\_to\_chiral.tex} line 172
(``functoriality on morphisms is Conjecture
\ref{conj:phi-d-functoriality}'').

\textbf{Ghost-theorem}: \emph{Stage 1 is canonical up to contractible
choice on objects; it is canonical up to a $\mathrm{GT}_1$-torsor on
morphisms, which trivialises on formal cyclic $A_\infty$ categories.}
This is Theorems~\ref{gel:thm:stage1-canonical-scope}
and~\ref{gel:thm:E_d-torsor} above.

### R2: ``$\Sigma_{d-1}$ is a closed cycle''

\textbf{Wrong reading of the current text}: $\Sigma_{d-1}$ taken as a
fixed submanifold, without transversality hypothesis on $C$, and
without specifying whether it is an oriented submanifold, a cycle
class in Borel–Moore homology, or an integration class.

\textbf{Precise error}: the specialisation
$\SpCh_{\Sigma_{d-1}, C}$ requires three separate pieces of data —
(i) an oriented proper $(d-1)$-submanifold $\Sigma_{d-1} \subset X$
with $\Sigma_{d-1} \cap C = \emptyset$ (or controlled intersection),
(ii) a framing of $\Sigma_{d-1}$ compatible with the holomorphic
factorisation structure, and (iii) a tubular neighbourhood of $C$ in
$X$ for the restriction operation. Conflating these reads
``fibration base'' as ``submanifold class''.

\textbf{Ghost-theorem}: \emph{$\SpCh$ is defined on the triple
$(\Sigma_{d-1}, \varphi, \nu)$ of oriented transverse cycle plus
framing plus tubular neighbourhood; bordism invariance holds only when
the bordism carries all three pieces of data.} This is
Theorem~\ref{gel:thm:stage2-monoidal} above.

### R3: ``$\Phi_d$ is a functor''

\textbf{Wrong phrasing}: the unqualified statement
``$\Phi_d \colon \CYcat_d \to E_1\text{-}\ChirAlg(C)$ is a functor''.

\textbf{Precise error}: the preface and \texttt{cy\_to\_chiral.tex}
line 172 already concede this: the construction is rigorous on
objects; functoriality on morphisms (property (U2)) is asserted as a
per-$d$ conjecture. But the phrase ``two-stage factorisation'' in the
preface carries connotations stronger than the manuscript supports.

\textbf{Ghost-theorem}: \emph{$\{\Phi_d\}_{d \geq 1}$ is a family of
object-level constructions, rigorous at $d \leq 2$ rationally as
$(\infty,1)$-functors, and at $d \geq 3$ as $(\infty,1)$-correspondences
admitting a groupoid of ambiguities that trivialises on formal CY
categories.} The manuscript's conclusion at line 242 (``the collection
$\{\Phi_d\}$ does not assemble into a functor in the standard
category-theoretic sense''; ``per-$d$ existence and uniqueness on the
smooth proper locus, with morphism action and compatibility under
CY-duality stated as per-$d$ conjectures'') is correct. The healed
prose should be propagated to every preface and summary passage.

### R4: ``$\Sp_{\Sigma, C}$ preserves $E_1$-chiral structure by strict identification''

\textbf{Wrong reading}: $\SpCh$ producing a strictly identified
$E_1$-chiral algebra on $C$ (as if the factorisation homology sat on
$C$ literally, not up to quasi-isomorphism).

\textbf{Precise error}: factorisation homology
$\int_{\Sigma_{d-1}}(-)|_C$ is defined up to quasi-isomorphism in the
derived category of factorisation algebras; the strict product
structure fails already on the K3 surface because the Nakajima cycle
requires the Hilbert-scheme blowup of $\mathrm{Sym}^n K3$ to
rationalise, and strict identification would require the unproven
chain-level commutativity of factorisation homology with restriction.

\textbf{Ghost-theorem}: \emph{$\SpCh$ is defined up to quasi-isomorphism
in $E_{n_{\mathrm{native}}(d)}$-$\ChirAlg(C)$; strict identification
is available only on the formal sublocus and up to the
$\mathrm{GT}_1$-torsor of Theorem~\ref{gel:thm:E_d-torsor}.}

## Cross-consistency checks

### Against \texttt{notes/platonic\_synthesis\_waves\_11\_through\_16.tex}

Theorem \texttt{wn:thm:plat-two-stage} states: ``Stage 1 is canonical up
to contractible choice (Kontsevich–Tamarkin $E_d$-formality;
Costello–Gwilliam–Li locality). Stage 2 is a specialisation: factorisation
homology over a $(d-1)$-cycle $\Sigma_{d-1} \subset X$, restricted to a
reference curve $C \subset X$. Different $(\Sigma_{d-1}, C)$ produce
different $E_1$-chiral shadows.''

The healed Theorems T1–T4 agree at the object level and sharpen the
morphism-level scope to ``object level $(\infty,1)$-functor rationally
for $d \leq 2$; correspondence with $\mathrm{GT}_1$-torsor for
$d \geq 3$''. They are consistent with the swarm-synthesis claim, adding
only the honest scope that separates object-level from morphism-level
contractibility.

The \texttt{wn:cor:plat-many-bkms} corollary (``Borcherds Monster and
Igusa $\mathfrak{g}_{\Delta_5}$ are sibling $E_1$-specialisations'') is
preserved verbatim in Theorem \ref{gel:thm:k3e-sibling-spcialisations}.

### Against \texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}

The $\mathbb{C}^3$ example (Jordan triple loop quiver) computes
$\mathrm{CoHA}(\mathbb{C}^3) = Y^+$ with shuffle-product structure
function $g(z) = \prod_i(z+\epsilon_i)/z^3$. Under the two-stage
factorisation this is the specialisation
$\SpCh_{\{z_3 = 0\}, \mathbb{C}} \circ \PhiFA_3$: Stage 1 produces the
6D $\hCS$ factorisation algebra on $\mathbb{C}^3$ with
Bochner–Martinelli propagator, Stage 2 specialises along the plane
$z_3 = 0$ to the base $\mathbb{C}$. The Tsymbaliuk 2017 triangular
decomposition of $Y(\widehat{\mathfrak{gl}}_1)$ is precisely the
$E_1$-chiral image.

The $\mathcal{W}_{1+\infty}$ is the evaluation-module sector of $Y^+$
at specific $\epsilon_i$-values; it is \emph{not} the CoHA itself
(AP-CY cache rule: $\CoHA(\mathbb{C}^3) = Y^+ \neq \mathcal{W}_{1+\infty}$).

The conifold and $K3 \times E$ examples in the treatise are two-stage
specialisations at different $\Sigma_2$, consistent with
Theorem~\ref{gel:thm:k3e-sibling-spcialisations} and its application
to non-compact CY$_3$.

### Against the universal identity $\kBKM(\Phi_N) = c_N(0)/2$

At each $N \in \{1, 2, 3, 4, 6\}$, the specialisation
$\SpCh_{\Sigma_2^{(N)}, E}(\PhiFA_3(\mathrm{Perf}(K3 \times E)))$
yields a BKM superalgebra whose Borcherds weight satisfies the
universal identity. The proof is modular: Stage 1 furnishes the
canonical $E_3$-hFA whose factorisation-homology partition function on
$K3 \times E$ is $\Delta_5^{-2}$; Stage 2 over the CHL cycle rescales
the denominator to $\Phi_N$; the weight is then the Borcherds weight
of the resulting form, by Borcherds 1995 Theorem 10.1 and Gritsenko
1999 Theorem 1.2.

Consistency check: $\kcat(K3 \times E) = 0$ (Künneth on total space) as
Stage-1 invariant is \emph{independent of} $\Sigma_2^{(N)}$; the
stratification of the $\{2, 3, 5, 24\}$ spectrum of $K3 \times E$ by
Stage-1 vs Stage-2 vs fibre-rank-vs-Hodge-supertrace is consistent with
the survey remark \ref{rem:four-kappa-stage-assignment}.

### Against the two-stage factorisation itself

Every healed theorem statement (T1–T4) uses the decomposition as
stated; no statement is made \emph{against} the decomposition. What
was attacked and what survived is the \emph{scope} of the uniqueness,
canonicality, and functoriality, not the decomposition itself.

## Residual frontier

\begin{itemize}
 \item \emph{Integral $E_d$-formality at $d \geq 3$} \ClaimStatusOpen.
 Whether the two-stage factorisation holds with strict identification
 (not merely up to rational quasi-isomorphism) is open. The
 2-torsion in $\pi_5(S^2)$ would be the first obstruction point at
 $d = 3$; whether it acts non-trivially on $\PhiFA_3(\cC)$ for any
 concrete CY$_3$ category is unexamined in the programme.

 \item \emph{Morphism-level conjecture (U2) at $d \geq 3$}
 \ClaimStatusOpen. Per-$d$ functoriality of $\Phi_d$ is conjectured
 (Conjecture~\ref{conj:phi-d-functoriality} in
 \texttt{cy\_to\_chiral.tex}); verified at $d = 2$ on Mukai transforms.
 At $d = 3$ the Borcherds–Monster orbifold on $(T^{24}/\mathbb{Z}_2)
 \times E$ would be the first target for direct chain-level
 verification.

 \item \emph{The $\mathrm{GT}_1$-torsor component}
 \ClaimStatusConjectured. On non-formal CY$_3$ categories such as
 local~$\mathbb{P}^2$, the $\mathrm{GT}_1$ action on $\PhiFA_3$-lifts
 of CY-morphisms should match the Kontsevich–Soibelman wall-crossing
 automorphism group; this is currently only observed at the level of
 characters.

 \item \emph{Essential surjectivity scope for
 Conjecture~\ref{gel:conj:phi-fa-fully-faithful}} \ClaimStatusOpen.
 Which $E_d$-holomorphic factorisation algebras arise from CY
 categories is a separate non-trivial question — the answer is
 conjecturally those with a negative cyclic CY class of degree $-d$,
 but this has not been verified on a single non-toy example.

 \item \emph{Bordism invariance with respect to transverse cycles}
 \ClaimStatusConjectured (Conjecture~\ref{gel:conj:spch-bordism-morphism}).
 At $d = 3$ the bordism class of a specialisation cycle
 $\Sigma_2 \subset K3 \times E$ determines the chiral shadow; whether
 this holds for a \emph{genuine} bordism (not a homology) is not
 established.
\end{itemize}

## Attack–heal cycle log (private, not for manuscript)

**Cycle 1** — ATTACK: Is Kontsevich–Tamarkin $E_d$-formality actually
available at the chain level for $d \geq 3$, integrally? The claim
``canonical up to contractible choice'' presumes an $\infty$-categorical
uniqueness that requires the formality morphism to be pinned down on
the chain level. HEAL: Found the answer in
\texttt{chapters/theory/quantum\_chiral\_algebras.tex}:1033 — the manuscript
itself concedes ``agree under Kontsevich formality (over $\mathbb{Q}$)
but differ at the chain level... Whether the two agree integrally
(not just rationally) is open.'' The healed scope is rational lane at
$d \leq 2$ plus Tamarkin–Willwacher $\mathrm{GT}_1$-torsor at $d \geq 3$.

**Cycle 2** — ATTACK: Is $\PhiFA_d$ an $(\infty,1)$-functor on
morphisms, or is it only defined on objects? The current manuscript
states an object-level theorem with a morphism-level conjecture, but
the two-stage phrasing in the preface suggests functoriality. HEAL:
\texttt{chapters/theory/cy\_to\_chiral.tex}:172 is explicit —
``ClaimStatusProvedHere (on objects, per $d$; functoriality on morphisms
is Conjecture \ref{conj:phi-d-functoriality})''. The preface language
must be tightened. Sharpened to Theorem T1: rational $(\infty,1)$-functor
at $d \leq 2$, object-level correspondence with $\mathrm{GT}_1$-torsor
at $d \geq 3$.

**Cycle 3** — ATTACK: What exactly is $\Sigma_{d-1}$? A submanifold, a
cycle class, a fibration base, an integration class? The
specialisation $\int_{\Sigma_{d-1}}(-)|_C$ makes sense only with
transversality + framing + tubular neighbourhood. HEAL: The cache
confirms at AP-CY144 that specialisation data is
$(\Sigma_{d-1}, \text{framing}, \text{tubular neighbourhood})$, not a
bare cycle. Theorem T3 makes this explicit and upgrades Stage 2 to a
symmetric monoidal $\infty$-functor on the Kan complex of transverse
oriented framed cycles with tubular neighbourhoods.

**Cycle 4** — ATTACK: Is the residual operadic level
$n_{\mathrm{native}}(d) = 1$ at $d \geq 3$ correct, or does it depend
on the $\Sigma_{d-1}$-framing? The Dunn–Lurie additivity
$E_d \simeq E_{d-1} \otimes E_1$ gives $E_1$ only when $\Sigma_{d-1}$
integrates out the $E_{d-1}$-factor cleanly. HEAL: Proposition
\ref{prop:native-en-level} is correct as stated for transverse
specialisation cycles; the $E_2$-enhancement at $d = 2$ on the
Nakajima cycle comes from the $\bS^2$-framing of K3 (not from every
$\Sigma_1$, only those carrying a framing). This becomes explicit in
Theorem T3. The residual operadic level is stable under bordism
(Theorem T3 part 3), but the $E_2$-enhancement at $d = 2$ is not: it
requires a framed cycle.

**Cycle 5** — ATTACK: Do the six (or infinitely many) specialisation
cycles $\Sigma_2$ on $K3 \times E$ produce genuinely distinct chiral
shadows, or are they equivalent under some larger automorphism? The
current manuscript says ``six different constructions, not six
applications of $\Phi_3$''. HEAL: The bordism-invariance content of
Theorem T3 implies the multiplicity is \emph{exactly} the number of
connected components of $\mathrm{Cyc}^{\mathrm{tr}}_2(K3 \times E; E)$
modulo bordism-through-transverse-cycles. The six constructions
correspond to six bordism classes: the K3-fibre (over a point of $E$),
the $T^4$-fibre (on the abelian-surrogate input, not on $K3 \times E$
itself), the Enriques-$\times E$ fibre, and three CHL-twisted cycles
$\Sigma_2^{(N)}$ for $N = 2, 3, 4, 6$. These are pairwise
non-bordant through transverse cycles (distinct invariants:
$\chi(K3) = 24$ vs $\chi(T^4) = 0$ vs $\chi(\text{Enriques}) = 12$).
Theorem T4 inscribes this scope.

**Cycle 6** — ATTACK: Does full faithfulness of $\PhiFA_d$ on formal
CY categories follow from Kontsevich–Tamarkin formality? What about
essential surjectivity? HEAL: Conjecture C2 states the expected scope:
$\PhiFA_d$ is fully faithful on formal CY categories (because formality
trivialises the $\mathrm{GT}_1$-torsor component on morphisms) but
\emph{not} essentially surjective in general (a generic
$E_d$-holomorphic factorisation algebra lacks the cyclic pairing in
degree $-d$ needed to come from a CY category). No adjoints exist.
This upgrades the current manuscript scope by tightening both the
scope of the functor and identifying the obstruction to its reversal.

**Cycle 7** — ATTACK (Gelfand-style surgical final check): Is the
two-stage factorisation the \emph{only} canonical presentation of
$\Phi_d$, or are there genuinely different factorisations? The naive
alternative would be a one-stage direct construction from the cyclic
$A_\infty$-structure to the $E_1$-chiral algebra on the curve (via the
five-step chain of Section~\ref{subsec:five-step-chain}), without the
intermediate $E_d$-holomorphic factorisation algebra. HEAL: The
four-step cyclic-to-chiral passage (line 148) is acknowledged as ``the
computational incarnation of $\SpCh_{\Sigma_{d-1}, C}$ composed with
the explicit realisation of $\PhiFA_d$''. The two-stage factorisation
is the canonical \emph{conceptual} presentation — what makes the
multiplicity of $E_1$-chiral shadows intelligible from a single source;
the five-step chain is its \emph{operational} presentation. Both are
correct; neither subsumes the other. This is the Gelfand insight:
strip every accidental choice (here, the choice of reference curve
$C$ and cycle $\Sigma_{d-1}$), and what remains is the $E_d$-hFA on $X$
itself — the platonic object.

## Verdict

The two-stage factorisation is \emph{mathematics}, not
meta-organisation. It survives the attack; what fell were imprecise
scope statements, not the factorisation itself. The programme's own
statement at \texttt{cy\_to\_chiral.tex}:172 is already honest; the
healed Theorems T1–T4 extract that honest scope into stand-alone
CG-voice theorems ready for inscription and propagation.

The sharpest structural insight: Stage 1 is the \emph{canonical object},
pinned by the CY datum alone. Stage 2 is the \emph{measurement}:
projecting the canonical object onto a reference curve through a choice
of cycle. The zoo of chiral algebras (Borcherds Monster, Igusa
$\mathfrak{g}_{\Delta_5}$, Fake Monster, Niemeier twists, CHL
descendants) is the zoo of measurements, not a zoo of underlying
objects. One CY$_d$ category, one $E_d$-hFA on $X$; many chiral shadows
on $C$. That is the two-stage factorisation reduced to its essence.

\emph{End of report.}
