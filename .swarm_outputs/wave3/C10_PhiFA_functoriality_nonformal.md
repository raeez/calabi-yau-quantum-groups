# Agent C10 — $(\infty,1)$-functoriality of $\PhiFA_d$ on non-formal CY categories at $d \geq 3$

## Terminal state

**C (Frontier Declaration).**

The morphism-level $(\infty,1)$-functoriality of $\PhiFA_d$ on
non-formal cyclic $A_\infty$ CY$_d$ categories at $d \geq 3$ (local
$\mathbb{P}^2$, resolved non-Kaledin quintic Gepner point, Ginzburg
potential quivers with $m_3 \neq 0$) is **genuine frontier**. What is
missing is not a rewording of a finished proof but a primary-source
theorem that has not been written: a chain-level rigidification of
the Grothendieck–Teichmüller action on formality quasi-isomorphisms
of $E_3$-algebras enhanced with a non-degenerate cyclic pairing of
degree $-3$, and an accompanying homotopy-transfer formula that
extends Willwacher 2014 from the universal $E_d$-formality torsor
to the **morphism-lifting** torsor on categories whose minimal model
carries $m_k \neq 0$ for some $k \geq 3$.

Object-level Stage-1 canonicality holds on the non-formal locus
(Wave 1 A01 Theorem T1 rational lane, $d \geq 3$; Wave 1 A03 Theorem
A3.1 via Costello–Gwilliam factorisation envelope with
$\GRT_1(\mathbb{Q})$-torsor trivialisation contractible as an
$\infty$-groupoid). Morphism-level $(\infty,1)$-functoriality
degrades to an $(\infty,1)$-correspondence precisely because the
contractibility of the formality-trivialisation space is
object-pinned: two different CY categories $\mathcal{C}, \mathcal{C}'$
each receive a contractible space of $E_3$-trivialisations, but the
*compatibility* of a choice on $\mathcal{C}$ with a choice on
$\mathcal{C}'$ under a CY-morphism $f: \mathcal{C} \to \mathcal{C}'$
is controlled by a $\GRT_1$-torsor that is non-trivial whenever at
least one side is non-formal.

## Statement of the frontier declaration (at CG voice)

\begin{conjecture}[$(\infty,1)$-functoriality of $\PhiFA_d$ on non-formal
CY$_d$ categories]\ClaimStatusOpen
\label{c10:conj:phifa-functoriality-nonformal}

Fix $d \geq 3$ and let $\CYcat_d^{\mathrm{nf}}$ denote the $(\infty,1)$-
category of cyclic $A_\infty$ CY$_d$ categories whose minimal model on
$\Ext^\bullet(\mathcal{E},\mathcal{E})$ carries some $m_k \neq 0$ for
$k \geq 3$. Let $\HolFA_{E_d}^{(\infty,1)}(\mathrm{CY}_d\text{-varieties})$
denote the $(\infty,1)$-category of holomorphic $E_d$-factorisation
algebras on complex $d$-folds in the Costello–Gwilliam sense. Then
the Stage-1 construction
\[
 \PhiFA_d \colon
 \CYcat_d^{\mathrm{nf}} \longrightarrow
 \HolFA_{E_d}^{(\infty,1)}(\mathrm{CY}_d\text{-varieties}),
\]
whose object-level restriction is canonical up to contractible choice
by Theorem~T1 of Wave~1~A01 and Theorem~A3.1 of Wave~1~A03, lifts to
an $(\infty,1)$-functor on morphisms. Equivalently: the obstruction
class to $(\infty,1)$-functoriality, lying in
\[
 \mathrm{Ob}_{\mathrm{mor}}(\PhiFA_d;\,\mathcal{C},\mathcal{C}';\,f)
 \;\in\;
 H^1\!\left(\mathfrak{grt}_1;\,
  \mathrm{Map}_{\EdHolFA(X)}^{\mathrm{cyc}}
  \bigl(\PhiFA_d(\mathcal{C}),\PhiFA_d(\mathcal{C}')\bigr)\right),
\]
vanishes for every cyclic $A_\infty$-morphism
$f: \mathcal{C} \to \mathcal{C}'$ and every pair
$(\mathcal{C},\mathcal{C}') \in \CYcat_d^{\mathrm{nf}}$. On local
$\mathbb{P}^2$ ($X = \mathrm{Tot}(\mathcal{O}(-3) \to \mathbb{P}^2)$,
McKay $\mathbb{Z}_3$-quiver with Ginzburg cubic potential
$W = x_{01}y_{12}z_{20} - x_{02}y_{21}z_{10}$ and
$m_3(x_{01},y_{12},z_{20}) = e_0$), the class is conjecturally measured
by a pairing between the Kontsevich wheel-class
$\mathrm{wh}_3 \in \mathfrak{grt}_1$ and the Atiyah class
$\At(T_X) \in H^1(X,\Omega^1_X \otimes \End T_X)$, non-trivial because
local $\mathbb{P}^2$ is not HKR-formal.
\end{conjecture}

\begin{remark}[On the failure of object-contractibility to imply
morphism-functoriality]
\label{c10:rem:object-vs-morphism}
Wave~1 A01 Theorem~T2 part~(4) made the structural point explicit:
contractibility of the object-level formality trivialisation space
(an honest theorem over $\mathbb{Q}$ for prounipotent
$\GRT_1(\mathbb{Q})$, by Willwacher 2014) does not imply
contractibility of the morphism-lifting space. Two homotopic
CY-morphisms $f_0 \simeq f_1: \mathcal{C} \to \mathcal{C}'$ lift to
homotopic $\PhiFA_d$-morphisms only up to a twist by $\GRT_1$,
trivial on formal objects (where both sides admit a canonical
formality quasi-isomorphism identifying the transferred $E_d$-structure
with the strict $E_d$-operad on Hochschild cohomology), genuinely
non-trivial on non-formal objects such as local $\mathbb{P}^2$ where
$m_3 \neq 0$ sources a chain-level wheel-class pairing against the
Atiyah cocycle.
\end{remark}

## Primary-source gap

**Gap 1 (identification of the obstruction class).** No published
theorem identifies
$\mathrm{Ob}_{\mathrm{mor}}(\PhiFA_d;\,\mathcal{C},\mathcal{C}';\,f)$
as a class in $H^1(\mathfrak{grt}_1;\,\cdot)$ with a primary-source
cocycle formula. The closest existing machinery is **Willwacher
2014** (*Invent. Math.* 200, arXiv:1009.1654), which proves:

> (Willwacher 2014 Theorem 1.1). The Grothendieck–Teichmüller Lie
> algebra $\mathfrak{grt}_1$ acts on the Kontsevich graph complex
> $\mathrm{GC}_d$ through a quasi-isomorphism
> $H^0(\mathrm{GC}_d) \cong \mathfrak{grt}_1$ for $d \geq 2$, and
> this action controls the set of $E_d$-formality quasi-isomorphisms
> as a torsor.

Willwacher's theorem is *object-level*: it parametrises the space of
formality quasi-isomorphisms on a fixed Hochschild cochain complex.
The extension to cyclic morphisms — an equivariance statement under
pullback along cyclic $A_\infty$-functors $f: \mathcal{C} \to
\mathcal{C}'$ compatible with a degree $-d$ Serre pairing — is not
proved.

**What would close Gap 1.** A theorem of the form:

> **Conjectured extension of Willwacher 2014 to cyclic morphisms.**
> For each cyclic $A_\infty$-functor
> $f: \mathcal{C} \to \mathcal{C}'$ between CY$_d$ categories with
> $d \geq 3$, the map on $E_d$-formality quasi-isomorphisms induced
> by $f$ is $\GRT_1$-equivariant; the obstruction to equivariance
> lies in $H^1(\mathfrak{grt}_1; \mathrm{Map}^{\mathrm{cyc}}_{E_d}(\cdot,\cdot))$
> and vanishes when both $\mathcal{C}, \mathcal{C}'$ are
> $A_\infty$-formal.

This would be the direct $E_d$-enhanced analogue of the Tamarkin 2007
theorem for associators on $E_n$ — which does not, in its 2007
incarnation, address morphism-level equivariance under a cyclic
pairing of negative degree.

**Gap 2 (chain-level homotopy transfer on non-formal CY$_3$
categories).** The Kajiura–Merkulov tree formula
(Kontsevich–Soibelman 2001, arXiv:math/0011041) transfers an
$A_\infty$-structure along a strong-deformation retract; when $X$ is
flat $\mathbb{C}^3$ (trivial $\At(T_X)$), the transfer is finite at
each order and terminates by the Dolbeault degree count (Wave~2 A06
Theorem 1). When $X$ is compact and non-flat CY$_3$, the transfer
is a formal-power series in propagators whose convergence requires
the $\GRT$-resummation of Willwacher 2014. For a *morphism*
$f: \mathcal{C} \to \mathcal{C}'$ between non-formal CY$_3$ categories
— e.g., a mutation between derived categories of two different toric
local CY$_3$ quiver algebras, or a Fourier–Mukai transform between
local $\mathbb{P}^2$ and local $\mathbb{P}^1 \times \mathbb{P}^1$ —
the homotopy transfer of $f_*$ along matched retracts is *not*
compatible with the wheel-graph resummation without a non-trivial
$\GRT_1$-compensation. The primary-source gap is the explicit chain-
level control on this compensation.

**What would close Gap 2.** An extension of **Costello–Gwilliam 2021
Vol II §7** (minimal models of holomorphic factorisation algebras,
specifically the Fedosov-resolution construction on compact CY$_d$
with $d \geq 2$) to morphism-level homotopy transfer, with explicit
wheel-diagram $\GRT_1$-counterterms cancelling the
wheel-class/Atiyah-class pairing on each side. The 2021 CG machinery
handles objects on fixed $X$; it does not (and was not intended to)
handle cyclic morphisms between two different CY$_3$ varieties.

**Gap 3 (derived mapping space interpretation).** The proposer's
question asks whether the obstruction is measurable as a class in
some derived moduli, perhaps in $\pi_0$ of the mapping space between
hCS observables on distinct CY categories. The precise statement
that would close this: the obstruction is a class in the homotopy
groups of the mapping space
\[
 \mathrm{Map}_{\EdHolFA}^{\mathrm{der}}
 \bigl(\PhiFA_d(\mathcal{C}),\PhiFA_d(\mathcal{C}')\bigr),
\]
specifically a class in $\pi_{-1}$ (or, equivalently, $\pi_0$ of the
loop space of the mapping space around a chosen basepoint). On flat
$\mathbb{C}^3$ this would reduce to a $\GRT_1$-invariant of the
Maurer–Cartan fibre — computable, finite-rank, vanishing by the
Dolbeault degree count when both categories are formal. On compact
non-formal CY$_3$ (local $\mathbb{P}^2$, quintic) this would require
a chain-level model of the non-formal Stage-1 output on each side
plus a chain-level representative for $f_*$, both of which exist
abstractly via Costello–Gwilliam Fedosov globalisation but neither
of which has been computed explicitly. **No published theorem
identifies $\pi_0$ of this mapping space with a $\mathfrak{grt}_1$-
cohomology group.**

**What would close Gap 3.** A theorem of the form:

> **Conjectured derived-mapping interpretation.** For $d \geq 3$ and
> $\mathcal{C},\mathcal{C}' \in \CYcat_d^{\mathrm{nf}}$, the
> $(\infty,1)$-functoriality obstruction class of
> Conjecture~\ref{c10:conj:phifa-functoriality-nonformal} is
> represented in
> $\pi_0 \mathrm{Map}_{\EdHolFA}^{\mathrm{der}}
> (\PhiFA_d(\mathcal{C}),\PhiFA_d(\mathcal{C}'))$ by the difference
> of the naive morphism $\PhiFA_d(f)$ computed in two different
> chain-level formality trivialisations, up to $\GRT_1$-twist.

This is neither proved nor disproved in the primary literature.

## Why existing machinery is insufficient

**Kontsevich 1999** formality theorem gives an $L_\infty$-quasi-
isomorphism between Schouten–Nijenhuis and Hochschild cochains;
**Tamarkin 2007** enhances this to $E_n$; **Willwacher 2014**
identifies the torsor of such trivialisations with $B\GRT_1$. All
three theorems are object-level: they concern the structure on a
fixed algebra, not the functoriality of $\PhiFA_d$ on Hom-sets.

**Costello–Gwilliam 2017/2021 Vol I and Vol II** produce the
factorisation-envelope functor $\mathbf{U}^{\mathrm{fact}}$ as a
chain-level functor from local $L_\infty$-algebras on $X$ to
factorisation algebras on $X$; functoriality holds at chain level
but requires a fixed $X$ and fixed chain-level presentation of each
side. Transferring this to the $(\infty,1)$-category of CY$_d$
categories with cyclic-$A_\infty$-morphisms requires descent along
Morita equivalences, and the Morita-invariance of
$\mathbf{U}^{\mathrm{fact}}$ at non-formal $d = 3$ input is not in
primary literature.

**Fresse 2017 Vol II** (*Homotopy of Operads and Grothendieck–
Teichmüller Groups*) establishes Thm.~12.3.A and Thm.~17.2.5
identifying the classifying space $B\mathrm{Isom}(E_d)$ with
$B\GRT_1$ rationally. This is the deepest object-level input and it
**stops** at objects. Fresse notes explicitly (Vol II §17.2, p.~465)
that morphism-level statements between distinct $E_d$-algebras
require new coherence data that he does not pursue.

**Kajiura–Merkulov / Kontsevich–Soibelman 2001** tree-transfer
formula gives the minimal $A_\infty$-model on $H^\bullet$ of a
DG-algebra. On a CY-morphism $f$, the induced minimal-model map
$f^{\min}$ is determined by tree summation involving propagators of
**both sides simultaneously**; when both sides are non-formal, the
tree sum is an infinite series whose convergence depends on matched
resummation of wheel graphs — the precise compensation controlled
by $\GRT_1$. This compensation is not constructed in the primary
literature at full generality.

The sum of these four gaps is the Tier-III-loose character of this
item: it is not solvable by applying a single named lemma; it
requires new machinery — specifically, a cyclic-$A_\infty$-enhanced
version of Willwacher 2014 with explicit chain-level compensation
for the morphism-level $\GRT_1$-action.

## Measurability of the obstruction in derived moduli

Tracking the proposer's sub-question: yes, *conjecturally*, the
obstruction admits a derived-moduli interpretation, though not in
the shape that first comes to mind.

Let $X, X'$ be two compact CY$_3$ varieties with CY$_3$-categorical
inputs $\mathcal{C} = \mathrm{Perf}(X)$, $\mathcal{C}' =
\mathrm{Perf}(X')$. A non-formal example is $X = \mathrm{local}\,
\mathbb{P}^2$, $X' = \mathrm{local}\,\mathbb{P}^1 \times \mathbb{P}^1$;
a mutation-induced derived equivalence $f: D^b(X) \simeq D^b(X')$
exists (Bridgeland 2002; Kawamata 2002) with explicit presentation.
Each side produces a hCS observable factorisation algebra
$\Obs_{\hCS}(X), \Obs_{\hCS}(X')$ on the respective variety; the
functoriality question is whether the $(\infty,1)$-mapping space
\[
 \mathrm{Map}_{\EdHolFA}(\Obs_{\hCS}(X),\Obs_{\hCS}(X'))
\]
contains a preferred point representing $\PhiFA_3(f)$, canonical up
to contractible choice. The obstruction, conjecturally, lives in
$\pi_0$ of this mapping space (more precisely, in the homotopy fibre
over a chosen base-point formality trivialisation) as a class
controlled by $\GRT_1$.

**Concrete test.** The simplest non-trivial case is $X = X' =
\mathrm{local}\,\mathbb{P}^2$ with $f$ the mutation generating
$\mathrm{Aut}(D^b(X))/\mathbb{Z}$ (the quiver mutation group of the
$\mathbb{Z}_3$-McKay quiver modulo global translation). On the
Hochschild side, $f$ acts on $\HH^\bullet(\mathrm{Perf}(\mathrm{local}\,
\mathbb{P}^2))$ by an explicit automorphism (the Seidel–Thomas
spherical twist associated to $\mathcal{O}_{\mathbb{P}^2}(-1)[1]$).
The conjecture predicts that $\PhiFA_3(f)$ is well-defined up to a
$\GRT_1$-twist that does not vanish on local $\mathbb{P}^2$ because
the minimal-model $m_3 \neq 0$.

**Status of this test case.** Computed on objects (Theorem~A3.1);
*not* computed on morphisms at the chain level. The needed
computation: (a) chain-level spherical-twist lift through Kapranov's
Dolbeault polyvector $L_\infty$-structure on $X$; (b) chain-level
wheel-graph correction on $\PhiFA_3(f)$ from the Willwacher
compensation mechanism; (c) comparison of the two sides. None of
(a)–(c) has been done in published literature.

## Cross-volume and cross-programme coordinates

**Vol I** (Bar–cobar programme). The formal-category locus — where
Conjecture~\ref{c10:conj:phifa-functoriality-nonformal} trivialises
— matches exactly the Vol I locus on which Theorem A (Koszul
reflection $\Omega \dashv \bar{B}$) and Theorem C (derived-centre
complementarity) are unconditional theorems. Vol I's
$\kappa^\kappa_\kappa = 8$ Mukai-enhancement theorem (three-faces-
of-$8$) uses the formal K3-Serre-bifunctor route, which does not
engage the non-formal morphism torsor; hence Vol I is insensitive to
the C10 obstruction.

**Vol II** (Chiral QFT / 3D HT). Vol II's functoriality on $A_X$ as
a functor from CY$_d$-categories with $d \leq 2$ to 3D holomorphic-
topological QFTs uses a different argument (the $S^2$-framed E_2
structure at $d = 2$ is genuinely functorial because the Drinfeld-
centre enhancement is an $(\infty, 2)$-adjoint at $d = 2$). At
$d = 3$, Vol II inherits the C10 open status; the
$(\infty,1)$-functoriality of the 3D HT construction on non-formal
CY$_3$ sources is conditional on the same primary-source extension.

**Vol III** (this programme). C10 is the sharp form of the
manuscript's own acknowledgement at
\texttt{chapters/theory/cy\_to\_chiral.tex}:248:
"\ClaimStatusProvedHere (on objects, per $d$; functoriality on
morphisms is Conjecture~\ref{conj:phi-d-functoriality})" and at
\texttt{chapters/theory/cy\_to\_chiral.tex}:306-314
(Conjecture~\ref{conj:phi-d-functoriality} unpacked). The present
declaration upgrades that conjecture's wording from a generic
"functoriality on morphisms" to the precise formulation as a
$\GRT_1$-torsor trivialisation problem, naming the primary-source
extensions that would close the gap.

## Inscription-ready TeX block

```tex
\begin{conjecture}[$(\infty,1)$-functoriality of $\PhiFA_d$ on
non-formal CY$_d$ categories at $d \geq 3$]
\label{c10:conj:phifa-functoriality-nonformal}
\ClaimStatusOpen

Fix $d \geq 3$. Let $\CYcat_d^{\mathrm{nf}}$ denote the $(\infty,1)$-
category of cyclic $\Ainf$ CY$_d$ categories whose minimal model on
$\Ext^\bullet(\cE, \cE)$ carries some $m_k \neq 0$ for $k \geq 3$
\textup{(}non-formal sources: local~$\bP^2$, quintic, Gepner points,
generic Ginzburg potential quivers\textup{).} The Stage-1 construction
$\PhiFA_d$ of Theorem~\ref{thm:phi-platonic}, object-level canonical
up to contractible choice by Willwacher 2014 Theorem~1.1 applied to
each object, lifts to an $(\infty,1)$-functor
\[
 \PhiFA_d \colon \CYcat_d^{\mathrm{nf}}
 \longrightarrow \HolFA_{E_d}^{(\infty,1)}\bigl(\mathrm{CY}_d\text{-varieties}\bigr).
\]
Equivalently, for every cyclic $\Ainf$-functor
$f \colon \cC \to \cC'$ between non-formal CY$_d$ categories, the
obstruction class
\[
 \mathrm{Ob}_{\mathrm{mor}}(\PhiFA_d;\, \cC, \cC';\, f)
 \;\in\;
 H^1\!\left(\mathfrak{grt}_1;\,
 \mathrm{Map}^{\mathrm{cyc}}_{\EdHolFA(X)}\!\bigl(
 \PhiFA_d(\cC), \PhiFA_d(\cC')\bigr)\right)
\]
vanishes. On local~$\bP^2$ with $m_3(x_{01}, y_{12}, z_{20}) = e_0$
\textup{(}Ginzburg cubic potential\textup{),} this class is
conjecturally represented by a pairing of the Kontsevich wheel-class
$\mathrm{wh}_3 \in \mathfrak{grt}_1$ against the Atiyah class
$\At(T_X) \in H^1(X, \Omega^1_X \otimes \End T_X)$.
\end{conjecture}

\begin{remark}[Primary-source gap and sufficient-conditions scope]
\label{c10:rem:phifa-functoriality-gap}
The object-level contractibility of $E_d$-formality trivialisations
\textup{(}Willwacher 2014, Fresse 2017 Vol.~II Thm.~17.2.5\textup{)}
does not imply morphism-level contractibility:
Conjecture~\ref{c10:conj:phifa-functoriality-nonformal} would follow
from a cyclic-$\Ainf$-enhanced extension of Willwacher 2014 with
explicit chain-level compensation of the $\GRT_1$-action on morphism
lifts. No such extension is in the primary literature. The nearest
partial results are: \textup{(a)} Fresse 2017 Vol.~II \S17.2 p.~465
notes that morphism-level coherences are outside the scope of the
Grothendieck--Teichm\"uller / $E_d$-formality package developed there;
\textup{(b)} Costello--Gwilliam 2021 Vol.~II \S7 establishes the
factorisation-envelope functor as chain-level-functorial on a fixed
$L_\infty$-space, but not on morphisms between distinct CY$_d$
categories with non-formal minimal models; \textup{(c)}
Kontsevich--Soibelman 2001 tree-transfer formula gives an infinite
formal series on non-formal sources, convergence of which under
matched-propagator morphism lifts requires a $\GRT_1$-compensation
not presently constructed. On $\Ainf$-formal CY$_d$ categories
\textup{(}flat $\C^3$, resolved conifold Kaledin-formal, K3 twisted-
HKR formal\textup{),} the obstruction class trivialises and
$\PhiFA_d$ is an $(\infty,1)$-functor on the formal sublocus.
\end{remark}
```

## Cross-consistency notes

**Against the Wave-1 spine
(\texttt{platonic\_synthesis\_post\_adversarial.tex}).** C10
sharpens Wave~1~A01 Theorem~T1 "rational lane, $d \geq 3$" scope
clause: the object-level correspondence is proved; the morphism-
level lift is precisely the open question. The $\GRT_1$-torsor
nomenclature of T2 part~(4) is inherited verbatim; the addition is
naming local $\mathbb{P}^2$ explicitly as the first non-trivial
test case and factoring the gap into the three named primary-source
extensions above.

**Against the Wave-2 refinement
(\texttt{platonic\_synthesis\_wave2\_refinement.tex}).** C10
matches the residual-frontier Tier-III classification assigned to
F8 ($(\infty,1)$-functoriality of $\PhiFA_d$ at $d \geq 3$) in
F05 §F8: "Remain open. Morphism functoriality requires formality
on morphisms, which is strictly weaker than integral formality of
$E_d$ but still open at $d \geq 3$ for non-formal sources." The
present declaration instantiates F8 with explicit non-formal
witnesses (local $\mathbb{P}^2$ with $m_3 = e_0$), a named
obstruction-class target ($H^1(\mathfrak{grt}_1; \cdot)$), and
three closure paths mapping to three named primary-source
extensions.

**Against the CoHA treatise
(\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}).** The
$\mathbb{C}^3$ case (abelian Jordan triple loop quiver) is
$A_\infty$-formal and does not engage the C10 obstruction. The
resolved conifold is Kaledin-formal and likewise unaffected. Local
$\mathbb{P}^2$ in the treatise appears (e.g., in the $\kch = 3/2$
computation) but the treatise does not address morphism-level
$\PhiFA_d$-functoriality; C10 is orthogonal and complementary.
$K3 \times E$ is product-formal via Căldăraru–Huybrechts on K3
(HKR-formal) tensor $E$ (trivially formal); hence C10 also does not
engage on $K3 \times E$ — the six-route multiplicity there is a
Stage-2 phenomenon (Theorem T4 of Wave 1 A01) and not a Stage-1
functoriality question.

**Against CLAUDE.md charter.** The programme's core assertion "$\Phi$
gives ONE output per category; different $\kappa$ values come from
DIFFERENT constructions, NOT six $\Phi$ applications to one object"
is insensitive to the C10 obstruction because multiplicity of
shadows on $K3 \times E$ is Stage-2 (six distinct specialisation
cycles), not Stage-1 (six different $\PhiFA_3$-outputs from one
category). C10 is the Stage-1 morphism-functoriality question at
$d \geq 3$ on non-formal sources, a separate issue.

**Against the $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal
identity.** The Borcherds-weight identity is a Stage-2 statement on
compact $K3 \times E$ across $N \in \{1,2,3,4,6\}$; the Stage-1
$\PhiFA_3$ output is fixed, and the specialisation cycles
$\Sigma_2^{(N)}$ vary. C10 does not engage this identity: the
Stage-1 output on the formal $K3 \times E$ is uniquely pinned
object-wise, and the universal identity concerns Stage-2
measurements, not Stage-1 functoriality under CY-morphisms.

**$\kappa$-subscript discipline.** $\kappa_{\mathrm{ch}}$ and
$\kappa_{\mathrm{cat}}$ appear only in the cross-consistency
discussion, never in the conjecture statement; bare $\kappa$ does
not appear. The obstruction class is named
$\mathrm{Ob}_{\mathrm{mor}}$, not conflated with any $\kappa$.

## Summary

**Terminal state: C (frontier).** The $(\infty,1)$-functoriality of
$\PhiFA_d$ at $d \geq 3$ on non-formal CY categories is genuine
open research, not a shortfall of proof-writing. Closure requires a
cyclic-$A_\infty$-enhanced version of Willwacher 2014 (Gap 1), its
chain-level morphism-transfer instantiation in the
Costello–Gwilliam Vol~II machinery (Gap 2), and a derived-mapping-
space identification of the resulting obstruction class (Gap 3).
Local $\mathbb{P}^2$ (with $m_3 \neq 0$ sourced from the Ginzburg
cubic potential) is the sharpest concrete test case.

*End of report.*
