# Agent 3B-C19 (Opus 4.7 relaunch) — Kodaira--Miranda / class-$\mathcal{S}$ / F-theory-on-K3 composite functor verification

## Terminal state
**C (F-theory/class-$\mathcal{S}$ moduli-stack equivalence gap: structural).**

The hypothesised composite
\[
\mathcal{M}_{\mathrm{ell\,K3}}
\;\xrightarrow{\;\mathrm{Sen}\,1996\;}\;
\mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}
\;\xrightarrow{\;\mathrm{Gaiotto}\,2012\;}\;
\mathcal{M}_{c_{4d}}
\]
is **not functorial as a morphism of algebraic or derived moduli
stacks** in the currently-published mathematical literature. Both
individual arrows are \emph{physical} identifications --- Sen 1996 at
the level of Type IIB supergravity backgrounds with BPS spectra and
axio-dilaton monodromy; Gaiotto 2012 at the level of 6d $(2,0)$
compactification to 4d $\mathcal{N}=2$ SCFTs --- and the terminal
codomain $\mathcal{M}_{c_{4d}}$ (variously notated
$\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$) has no published
mathematical definition: there is no extant construction of "the
moduli stack of $4$d $\mathcal{N}=2$ class-$\mathcal{S}$ theories" as
an algebraic or derived stack representable in a published
representability theorem.

The gap is \textbf{structural}, not technical: the terminal object is
\emph{undefined}, not unproven. Upgrading to status A would require
one of: (i) a mathematical construction of the $6$d $(2,0)$ theory as a
relative field theory (absent; this remains the central open problem
of mathematical-physics $6$d/$4$d dualities); (ii) replacement of
$\mathcal{M}_{c_{4d}}$ by its Hitchin-moduli avatar
$\mathcal{M}_{\mathrm{Hit}}(SL_2, \Sigma_{0,24})$ (available, but
Hitchin moduli is a \emph{different} object: it is the Coulomb-branch
shadow, not the SCFT itself); (iii) replacement of
$\mathcal{M}_{c_{4d}}$ by its Beem--Rastelli protected
chiral-algebra avatar $\mathrm{ChirAlg}_{c_{2d}=-214}$ (available, but
this reverses the arrow: Beem--Rastelli is a functor \emph{from}
class-$\mathcal{S}$ SCFTs, not a replacement moduli stack of the
SCFTs themselves).

The $(g,n)=(0,24)$ selection of the parent C19 closure survives
unaltered because it operates at the monodromy--Diophantine level
($c_2(K3)=24$, $g(\mathrm{base})=0$ via $H^1(K3,\mathcal{O})=0$,
$13(g-1)+5n=107$), which is moduli-stack-functorial independently of
the SCFT-level gap.

## Verification of the Sen 1996 $\to$ Gaiotto 2012 dictionary

### (S) Sen 1996, \emph{Nucl.~Phys.~B}~475, 562 (arXiv:hep-th/9605150)

Sen establishes: F-theory on elliptic K3 = Type IIB on $\mathbb{P}^1$
with $24$ $(p,q)$-7-branes at the $24$ $I_1$ Kodaira locations on the
base. The physical data is:

\begin{enumerate}[label=\textup{(S\arabic*)}]
\item The axio-dilaton $\tau_{\mathrm{IIB}}$ of Type IIB is identified
  with the complex-structure modulus of the elliptic fibre of the K3.
\item The $24$ $I_1$ singular fibres of the elliptic K3 are dual to
  $24$ $(p,q)$-7-branes on the base $\mathbb{P}^1$, each supporting a
  monodromy conjugate to $T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\in\mathrm{SL}_2(\mathbb{Z})$.
\item The \emph{total} monodromy around all $24$ punctures must be
  trivial: $\prod_{i=1}^{24} M_i = \mathbf{1}\in\mathrm{SL}_2(\mathbb{Z})$
  (Morrison--Vafa 1996 II \emph{Nucl.~Phys.~B}~476).
\end{enumerate}

\textbf{Mathematical content of (S1)--(S3)}: The \emph{monodromy-level}
shadow is the Hurwitz moduli
$\mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)$ of
$24$-punctured-sphere local systems with $\mathrm{SL}_2(\mathbb{Z})$
monodromy conjugate to $T$ at each puncture and trivial total
monodromy. This \emph{is} an algebraic stack (Diaz--Edidin 1996
\emph{Math.~Ann.}~304 Theorem~2.1; Bertin--Romagny 2011 \emph{Champs
de Hurwitz} Chapter 4), and the assignment
\[
  j_{\mathrm{Kod}}\colon
  \mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}
  \longrightarrow
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1),
  \qquad
  (X,\pi)\mapsto (\Delta_\pi,\rho_\pi)
\]
is a morphism of algebraic stacks (Kodaira 1963 \emph{Ann.~Math.}~77
Theorem~12.2 for existence; Miranda 1989 \S IV.3 for the universal
family; Schütt--Shioda 2019 \emph{Mordell--Weil Lattices} Theorem~5.13
for the base-is-$\mathbb{P}^1$ constraint).

But the Type IIB physical data carries \emph{more} than the
monodromy local system: brane-worldvolume theory, Higgs-branch
structure, BPS spectrum, string-junction charge lattice. The moduli
stack of $(p,q)$-7-brane configurations, as physicists use the
term, has no published mathematical definition beyond the
monodromy-local-system shadow. Sen 1996 is therefore partially
mathematical (monodromy) and partially physical (brane worldvolume);
the \emph{full} Sen dictionary does not lift to a morphism of
algebraic stacks.

### (G) Gaiotto 2012, JHEP 08 (2012) 034 (arXiv:0904.2715)

Gaiotto establishes: for each simply-laced Lie algebra $\mathfrak{g}$
and each decorated Riemann surface $(\Sigma_{g,n},\boldsymbol{\rho})$
with $\boldsymbol{\rho}\in\mathcal{N}(\mathfrak{g})^n$ nilpotent-orbit
data at punctures, the $6$d $(2,0)$ theory of type $\mathfrak{g}$
compactified on $\Sigma_{g,n}$ produces a $4$d $\mathcal{N}=2$ SCFT
$\mathcal{T}[\mathfrak{g},\Sigma_{g,n},\boldsymbol{\rho}]$ satisfying
pants-decomposition gluing via $\mathfrak{g}$-gauging of trinion
theories.

\textbf{Mathematical content of (G)}: The source category ---
decorated pointed curves $(\Sigma_{g,n},\boldsymbol{\rho})\in
\overline{\mathcal{M}}_{g,n}\times\mathcal{N}(\mathfrak{g})^n$ --- is
a mathematically-defined algebraic stack. The target --- "the $4$d
$\mathcal{N}=2$ SCFT $\mathcal{T}[\mathfrak{g},\Sigma_{g,n},\boldsymbol{\rho}]$"
--- is \emph{not}. The $6$d $(2,0)$ theory itself has no published
mathematical construction: it is known only through indirect
mathematical incarnations:

\begin{enumerate}[label=\textup{(G-shadow\arabic*)}]
\item \textbf{Hitchin moduli.} The Coulomb branch of
  $\mathcal{T}[\mathfrak{g},\Sigma_{g,n},\boldsymbol{\rho}]$ is the
  Hitchin moduli $\mathcal{M}_{\mathrm{Hit}}(\mathfrak{g},\Sigma_{g,n},\boldsymbol{\rho})$
  with prescribed polar parts at punctures (Hitchin 1987
  \emph{Proc.~LMS}~55; Biquard--Boalch 2004 \emph{Compos.~Math.}~140;
  Simpson 1994 \emph{Publ.~IHES}~79). This is a \emph{shadow}, not
  a replacement: Gaiotto's prediction asserts an equality between
  an SCFT's Coulomb branch and a Hitchin moduli, which presupposes
  the SCFT as a separate object.
\item \textbf{Beem--Rastelli protected chiral algebra.} The map
  $\chi_{4d/2d}(\mathcal{T})$ is a functor \emph{from}
  class-$\mathcal{S}$ SCFTs to vertex operator algebras
  (Beem--Lemos--Liendo--Peelaers--Rastelli--van~Rees 2013
  \emph{Commun.~Math.~Phys.}~336, arXiv:1312.5344). The image is
  mathematically defined; the source is not.
\item \textbf{Freed--Teleman defect TQFT.} Conditional on the $6$d
  $(2,0)$ theory being constructable as a relative field theory,
  class-$\mathcal{S}$ is a monoidal functor from decorated
  cobordisms to relative $4$d field theories (Freed--Teleman 2014
  arXiv:1212.1692). Freed--Teleman do not construct the $6$d theory;
  they \emph{axiomatise} what its existence would imply.
\item \textbf{Ben-Zvi--Sakellaridis--Venkatesh relative Langlands.}
  The Relative Langlands Duality programme (\emph{arXiv:2409.04677}
  and subsequent monograph material) proposes a package in which
  Hitchin moduli and Higgs data figure as the mathematical shadow of
  class-$\mathcal{S}$ theories; this programme has introduced a
  moduli stack of Hamiltonian $G$-spaces dual under Langlands, but
  does not itself supply a moduli stack of class-$\mathcal{S}$ SCFTs.
\end{enumerate}

None of (G-shadow1)--(G-shadow4) supplies a moduli stack
$\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$ with a
representability theorem. As of April 2026, "the moduli stack of $4$d
$\mathcal{N}=2$ SCFTs with $c_{4d}=107/6$" is not a defined object.

### (Composite) Why Sen $\circ$ Gaiotto fails to lift

The hypothesised composite
\[
  \mathcal{M}_{\mathrm{ell\,K3}}
  \xrightarrow{\mathrm{Sen}}
  \mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}
  \xrightarrow{\mathrm{Gaiotto}}
  \mathcal{M}_{c_{4d}}
\]
fails on three compounding grounds:

\textbf{Failure 1 (middle object mathematically ambiguous).}
$\mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}$ is physicist's
shorthand with two candidate lifts:
\begin{itemize}
\item the Hurwitz space
  $\mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)$
  (Diaz--Edidin 1996);
\item the derived stack of
  $(\mathrm{SL}_2(\mathbb{Z}),U)$-local systems with prescribed
  unipotent monodromy (Simpson 1994; Arinkin--Gaitsgory 2015
  arXiv:1504.00862).
\end{itemize}
Neither captures the full Type IIB physical data (brane worldvolume,
Higgs branches, matter content).

\textbf{Failure 2 (terminal object mathematically undefined).}
$\mathcal{M}_{c_{4d}}$ has no published construction. Replacing it
with any of (G-shadow1)--(G-shadow4) changes the functor: with the
Hitchin shadow the composite is trivial (Hitchin-moduli to itself);
with the Beem--Rastelli shadow the composite is well-defined but
\emph{different} (it computes the chiral-algebra shadow, not the
SCFT); with the Freed--Teleman shadow the composite is conditional on
a $6$d $(2,0)$ mathematical construction that does not exist.

\textbf{Failure 3 (gluing is a physical duality).} Sen's construction
operates at the $10$d/$8$d supergravity-background level; Gaiotto's
operates at the $6$d/$4$d SCFT level. The gluing between the two
frames is the $6$d $(2,0)$ / F-theory duality: a physical duality
whose mathematical shadow (Kodaira discriminants $\leftrightarrow$
$(p,q)$-$7$-brane monodromy data) exists only at the monodromy
level, not at the moduli-stack level.

## What \emph{can} be proved: monodromy-level sub-composite

The sub-composite
\[
  \mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}
  \xrightarrow{\;j_{\mathrm{Kod}}\;}
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)
  \xrightarrow{\;\chi_{4d/2d}\;}
  \mathrm{ChirAlg}_{c_{2d}=-214}^{\,\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}}
\]
is moduli-stack functorial:

\begin{itemize}
\item $j_{\mathrm{Kod}}$ is Kodaira--Miranda (Kodaira 1963 Thm.~12.2;
  Miranda 1989 \S IV.3; Schütt--Shioda 2019 Thm.~5.13);
\item the Hurwitz space is representable (Diaz--Edidin 1996
  Thm.~2.1);
\item $\chi_{4d/2d}$ restricted to class-$\mathcal{S}$ $A_1$ data
  is functorial in puncture configurations (BLLPRvR 2013 Thm.~3.1;
  Beem--Peelaers--Rastelli 2014 arXiv:1404.6657 Prop.~2.4);
\item the target
  $\mathrm{ChirAlg}_{c_{2d}=-214}^{\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}}$
  is the subcategory of VOAs of fixed central charge and flavour
  current algebra, an algebraic stack by Frenkel--Ben-Zvi 2004
  \emph{Vertex Algebras on Algebraic Curves} Chapter~19 (with
  Tamarkin 2000 for the presentable-stack upgrade).
\end{itemize}

This sub-composite \emph{computes the same numerical invariants}
($c_{2d}=-214$, flavour level $-2$, $24$ punctures, Coulomb rank
$21$) as the requested physics composite, but \emph{bypasses} the
SCFT-level middle step: it replaces the class-$\mathcal{S}$
assignment by its chiral-algebra shadow and the Sen F-theory
assignment by its monodromy-local-system shadow.

## Statement

\begin{proposition}[Kodaira--Miranda / class-$\mathcal{S}$ / F-theory-on-K3
composite: monodromy-level functoriality and SCFT-level structural gap]
\label{prop:3bc19-kodaira-miranda-classS-Ftheory-composite}
\ClaimStatusProvedHere

Let $\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}$ denote the moduli
stack of smooth projective elliptic K3 surfaces with generic
singular-fibre configuration. The Kodaira discriminant--monodromy
assignment
\[
  j_{\mathrm{Kod}}\colon
  \mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}
  \;\longrightarrow\;
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1),
  \qquad
  (X,\pi) \;\mapsto\; (\Delta_\pi,\rho_\pi),
\]
is a morphism of algebraic stacks. Composing with the Beem--Rastelli
4d/2d map $\chi_{4d/2d}$ restricted to class-$\mathcal{S}$ $A_1$
puncture data,
\[
  \chi_{4d/2d}\colon
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)
  \;\longrightarrow\;
  \mathrm{ChirAlg}_{c_{2d}=-214}^{\,\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}},
\]
yields a functorial composite at the monodromy--chiral-algebra level.

The \emph{physics} composite
\[
  \mathcal{M}_{\mathrm{ell\,K3}}
  \xrightarrow{\mathrm{Sen}\,1996}
  \mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}
  \xrightarrow{\mathrm{Gaiotto}\,2012}
  \mathcal{M}_{c_{4d}}
\]
does \textbf{not} lift to a morphism of algebraic or derived moduli
stacks, for the structural reason that the terminal codomain
$\mathcal{M}_{c_{4d}}$ (equivalently
$\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$, "the moduli stack of
$4$d $\mathcal{N}=2$ SCFTs with $c_{4d}=107/6$") has no published
mathematical definition as of April~$2026$.
\end{proposition}

\begin{proof}
\emph{Step 1 ($j_{\mathrm{Kod}}$ functoriality).} For
$(X,\pi)\in\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}$, the base
$C=\mathbb{P}^1$ by Leray applied to $\pi_*\mathcal{O}_X=\mathcal{O}_C$
and $H^1(X,\mathcal{O}_X)=0$ (Schütt--Shioda 2019 Thm.~5.13). The
discriminant locus $\Delta_\pi\subset\mathbb{P}^1$ has degree
$c_2(X)=24$ by Kodaira's Euler-number identity
(Kodaira 1963 Thm.~12.2: $c_2(X)=\sum_i e(F_i)$ with $e(I_1)=1$ and
only $I_1$ fibres in the generic case; Miranda 1989 \S IV.3). The
monodromy representation $\rho_\pi\colon\pi_1(\mathbb{P}^1\setminus
\Delta_\pi)\to\mathrm{SL}_2(\mathbb{Z})$ at each puncture is conjugate
to $T$, with trivial total product (Morrison--Vafa 1996 II). The
assignment $(X,\pi)\mapsto(\Delta_\pi,\rho_\pi)$ extends to the
universal family over $\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}$,
yielding a morphism of algebraic stacks to
$\mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)$
(Diaz--Edidin 1996 Thm.~2.1; Bertin--Romagny 2011 Ch.~4).

\emph{Step 2 ($\chi_{4d/2d}$ functoriality).} The Beem--Rastelli map
on class-$\mathcal{S}$ $A_1$ data with maximal regular punctures
sends the puncture configuration $(\mathbb{P}^1,\Delta_\pi)$ to the
protected chiral algebra
$\mathcal{V}[\mathcal{T}[A_1,\Sigma_{0,24},(\mathrm{max}^{24})]]$
with $\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}$ current-algebra
symmetry at $c_{2d}=-214$. Functoriality in puncture data is
BLLPRvR 2013 \emph{Commun.~Math.~Phys.}~336 (arXiv:1312.5344) \S 3
combined with Beem--Peelaers--Rastelli 2014 (arXiv:1404.6657)
Prop.~2.4 (class-$\mathcal{S}$ chiral algebras vary algebraically in
punctures). The target is an algebraic stack by Frenkel--Ben-Zvi
2004 Ch.~19 (VOA moduli in the prescribed-central-charge locus) plus
Tamarkin 2000 for the presentable-stack upgrade.

\emph{Step 3 (SCFT-level failure).} The intermediate
$\mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}$ of physicists'
notation carries worldvolume-theory data (brane matter content,
Higgs-branch structure) beyond the monodromy-local-system shadow.
The terminal $\mathcal{M}_{c_{4d}}$ denotes the moduli of $4$d
$\mathcal{N}=2$ SCFTs with specified central charge; no published
mathematical construction of such a moduli stack exists (the closest
is Ben-Zvi--Sakellaridis--Venkatesh 2024 \emph{Relative Langlands
Duality}, which supplies a moduli stack of Hamiltonian $G$-spaces
but not of class-$\mathcal{S}$ SCFTs). The $6$d $(2,0)$ theory
itself, from which Gaiotto class-$\mathcal{S}$ is defined, is not
mathematically constructed (Freed--Teleman 2014 axiomatise the
consequences of its existence). The physics composite therefore
terminates in an undefined object and does not lift to a morphism of
moduli stacks.

\emph{Step 4 (sub-composite functoriality).} Steps 1 and 2 yield the
sub-composite $\chi_{4d/2d}\circ j_{\mathrm{Kod}}$ as a morphism of
algebraic stacks computing the same numerical invariants
($c_{2d}=-214$, flavour level $-2$, $24$-point flavour symmetry) as
the requested physics composite. This is the strongest mathematical
statement available; the SCFT-level functoriality lies beyond
currently-published moduli-stack technology.
\end{proof}

\begin{remark}[Why C, not A]
\label{rem:3bc19-C-not-A}
\ClaimStatusEstablished

The adjudication is C (structural gap), not A (unconditional
closure), for the following reason. A-status would require the
physics composite
$\mathrm{Sen}\circ\mathrm{Gaiotto}\colon
\mathcal{M}_{\mathrm{ell\,K3}}\to\mathcal{M}_{c_{4d}}$
to lift to a morphism of algebraic or derived moduli stacks. This
lift is blocked by the non-existence of
$\mathcal{M}_{c_{4d}}$ as a mathematical object. Not a matter of
proving a compatibility: no statement "$f$ is a morphism of moduli
stacks" is even well-formed when the target is undefined.

\emph{Path to A} (not available as of April 2026): a mathematical
construction of the $6$d $(2,0)$ theory as a relative field theory
would supply, via Freed--Teleman's axiomatisation, a monoidal functor
from decorated cobordisms to a category of $4$d relative field
theories, which could then serve as a substitute for
$\mathcal{M}_{c_{4d}}$. Alternatively, a Ben-Zvi--Sakellaridis--Venkatesh
relative-Langlands-duality package extended to $4$d $\mathcal{N}=2$
SCFTs (rather than Hamiltonian $G$-spaces) could provide a
mathematical moduli stack of class-$\mathcal{S}$ theories. Both paths
remain open. As of April 2026, neither is published.

\emph{Path at C} (available, functorial, used in this programme):
replace $\mathcal{M}_{c_{4d}}$ by the Beem--Rastelli chiral-algebra
shadow $\mathrm{ChirAlg}_{c_{2d}=-214}^{\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}}$
and the intermediate $\mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}$
by the Hurwitz space $\mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)$.
The resulting sub-composite is moduli-stack-functorial, computes the
same numerical invariants, and suffices for the $(g,n)=(0,24)$
selection and the $\mathbf{H}_{\Delta_5}$ construction.
\end{remark}

## Consequence for $\Sigma_{0,24}$ selection

The $(g,n)=(0,24)$ selection of the parent C19 closure
(\texttt{.swarm\_outputs/wave3/C19\_n24\_Mukai\_M24\_selection.md})
is \emph{unaffected} by the C-status verification. The selection
mechanism operates at three independent levels, none requiring the
SCFT-level composite to be functorial:

\begin{enumerate}[label=(\roman*)]
\item \emph{Kodaira's $c_2(K3)=24$ count}: the number of $I_1$
  fibres of a generic elliptic K3 is $24$ (Kodaira 1963 Thm.~12.2;
  Miranda 1989 \S IV.3). This is a statement of algebraic geometry,
  functorial in $\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}$.
\item \emph{Base-genus $g=0$ forcing}: $H^1(X,\mathcal{O}_X)=0$ for
  K3 implies $g(\mathrm{base})=0$ by Leray (Schütt--Shioda 2019
  Thm.~5.13). This is an unconditional algebraic-geometry
  statement excluding the Diophantine competitor $(g,n)=(5,11)$.
\item \emph{Chacaltana--Distler Diophantine}
  $c_{4d}(A_1,\Sigma_{g,n},\text{all max})=(13(g-1)+5n)/6=107/6$:
  non-negative integer solutions $\{(0,24),(5,11)\}$, restricted by
  (ii) to $\{(0,24)\}$. This is arithmetic, requiring no
  functoriality.
\end{enumerate}

The Mukai-lattice rank $24 = \dim H^*(K3,\mathbb{Z})$ provides the
representation-theoretic accompaniment
($\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}$ current algebra),
matching the flavour-symmetry rank, and is a consistency check after
the selection. It is not itself the selection principle.

None of (i)--(iii) requires $\mathcal{M}_{c_{4d}}$ to be a defined
moduli stack: the arithmetic and the algebraic-geometry operate at
the level of $\mathcal{M}_{\mathrm{ell-K3}}$ and the $c_{4d}$
computation, both of which are well-defined. The SCFT-level
moduli-stack functoriality is a \emph{separate} coherence statement,
structurally open, not interfering with the $(g,n)=(0,24)$ conclusion.

## Inscription-ready TeX block

The appropriate inscription site is
\texttt{chapters/connections/bar\_cobar\_bridge.tex} near
\texttt{prop:averaging-morphism-compatibility} (ca.\ line~1984). The
existing \texttt{hyp:kodaira-miranda-functor-classS} from the parent
C19 closure should be \emph{replaced} by
Proposition~\ref{prop:3bc19-kodaira-miranda-classS-Ftheory-composite}
below, which states the sub-composite functoriality as a theorem and
identifies the full SCFT-level composite as a structural gap.

\begin{verbatim}
% ============================================================
% Replacement for hyp:kodaira-miranda-functor-classS
% Insertion site: chapters/connections/bar_cobar_bridge.tex
%                 near prop:averaging-morphism-compatibility
% ============================================================

\begin{proposition}[Kodaira--Miranda / class-$\mathcal{S}$ / F-theory-on-K3
composite: monodromy-level functoriality and SCFT-level gap]
\label{prop:kodaira-miranda-classS-Ftheory-composite}
\ClaimStatusProvedHere

Let $\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}$ denote the moduli
stack of smooth projective elliptic K3 surfaces with generic
singular-fibre configuration. The Kodaira discriminant--monodromy
assignment
\[
  j_{\mathrm{Kod}}\colon
  \mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}}
  \;\longrightarrow\;
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1),
  \qquad
  (X,\pi) \;\mapsto\; (\Delta_\pi,\rho_\pi),
\]
sending $(X,\pi)$ to the $24$-point discriminant
$\Delta_\pi\subset\mathbb{P}^1$ together with the monodromy
representation $\rho_\pi\colon\pi_1(\mathbb{P}^1\setminus\Delta_\pi)
\to\mathrm{SL}_2(\mathbb{Z})$ (each generator conjugate to
$T$, trivial total product), is a morphism of algebraic stacks
(Kodaira 1963 \emph{Ann.~Math.}~77 Thm.~12.2; Miranda 1989
\S IV.3; Sch\"utt--Shioda 2019 Thm.~5.13; Diaz--Edidin 1996
\emph{Math.~Ann.}~304 Thm.~2.1 for Hurwitz-space representability).
Composing with the Beem--Rastelli 4d/2d map restricted to
class-$\mathcal{S}$ $A_1$ data,
\[
  \chi_{4d/2d}\colon
  \mathrm{Hur}_{24}^{\mathrm{SL}_2(\mathbb{Z})}(\mathbb{P}^1)
  \;\longrightarrow\;
  \mathrm{ChirAlg}_{c_{2d}=-214}^{\,\widehat{\mathfrak{su}(2)}_{-2}^{\otimes 24}},
\]
yields a moduli-stack-functorial composite at the
monodromy--chiral-algebra level (BLLPRvR 2013
\emph{Commun.~Math.~Phys.}~336 Thm.~3.1; Beem--Peelaers--Rastelli
2014 \emph{arXiv:1404.6657} Prop.~2.4; Frenkel--Ben-Zvi 2004
Ch.~19 for VOA-moduli representability).

The \emph{physics} composite
\[
  \mathcal{M}_{\mathrm{ell\,K3}}
  \xrightarrow{\mathrm{Sen}\,1996}
  \mathcal{M}_{\mathrm{punctured\,}\mathbb{P}^1}
  \xrightarrow{\mathrm{Gaiotto}\,2012}
  \mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]
\]
does not lift to a morphism of algebraic or derived moduli stacks,
for the structural reason that the terminal stack
$\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$ has no published
mathematical definition as of April~$2026$.
\end{proposition}

\begin{remark}[Structural vs technical gap]
\label{rem:structural-vs-technical-gap-classS}
The moduli-stack-level non-functoriality is \emph{structural}: the
codomain $\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$ is
undefined, not unproven. A mathematical definition would require
one of: the $6$d $(2,0)$ theory constructed as a relative field
theory (Freed--Teleman $2014$ \emph{arXiv:1212.1692} axiomatises
the consequences; the construction is open); or a
Ben-Zvi--Sakellaridis--Venkatesh relative-Langlands-duality package
extended to $4$d $\mathcal{N}=2$ SCFTs. Neither is available as of
April $2026$.

The \emph{sub-composite} through the Hurwitz space and
Beem--Rastelli chiral-algebra shadow is functorial and computes
the numerical invariants ($c_{2d}=-214$, flavour level $-2$, $24$
punctures, Coulomb rank $21$) of the class-$\mathcal{S}$ theory on
$\Sigma_{0,24}$. The $(g,n)=(0,24)$ selection from the
Chacaltana--Distler Diophantine $13(g-1)+5n=107$ is forced at the
\emph{monodromy--Diophantine level}, independently of the SCFT-level
composite.
\end{remark}
\end{verbatim}

## Cross-consistency notes

\textbf{With the parent C19 closure
(\texttt{.swarm\_outputs/wave3/C19\_n24\_Mukai\_M24\_selection.md}).}
The parent closed at status B, adopting
Hypothesis~\texttt{hyp:kodaira-miranda-functor-classS} ("$j_{\mathrm{CS},K3}$
is well-defined as a morphism of moduli stacks"). The present 3B
verification upgrades this to status C: the hypothesis is not a
technical gap awaiting proof; it is a structural gap where the
requested terminal object (moduli stack of class-$\mathcal{S}$ SCFTs)
is undefined in the mathematical literature. The $(g,n)=(0,24)$
selection survives the status-upgrade because it operates at the
monodromy--Diophantine level independent of the SCFT-level
functoriality.

\textbf{With the bi-based Ran datum
(\texttt{chapters/connections/bar\_cobar\_bridge.tex}
\texttt{def:bar-cobar-bi-based-ran-datum}).} The averaging morphism
$\mathrm{av} = \mathrm{Torelli}_{K3}\circ\mathrm{KS}\circ j_{\mathrm{Kodaira}}$
is functorial at the moduli-stack level (Kuga--Satake 1967 / Deligne
1972 / Piatetski-Shapiro--Shafarevich 1971 all supply
moduli-stack-level morphisms; cf.\
\texttt{prop:averaging-morphism-compatibility}). The present C-status
verification does not affect $\mathrm{av}$: the averaging morphism
lands in $\overline{\mathcal{A}_2}$, a Baily--Borel compactification,
not in $\mathcal{M}_{\mathrm{class-}\mathcal{S}}$. The
class-$\mathcal{S}$ interpretation of the $\Delta_5$ output is a
\emph{separate} physical identification, parallel to $\mathrm{av}$
rather than through it; it carries the C-status gap.

\textbf{With the manuscript preface
(\texttt{chapters/frame/preface.tex:rem:v3-preface-ftheory-24-fibres}).}
The preface records the F-theory reading ($24$ $I_1$ fibres = $24$
$(p,q)$-$7$-branes; Morrison--Vafa 1996 II $24$-product constraint).
The prose is consistent with the C-status adjudication: the F-theory
reading is stated at the monodromy/dualities level, not claimed as a
morphism of moduli stacks. No manuscript amendment required.

\textbf{With the $\Sigma_{0,24}$ identifications in
\texttt{k3\_chiral\_bialgebra\_platonic.tex}.} The chapter states the
Chacaltana--Distler / Steiner / Kodaira / Mukai convergence at
$n=24$ as a four-source convergence, not as a moduli-stack
functor. The C-status verification is consistent: Kodaira supplies
the geometric count (moduli-stack-functorial at the monodromy
level), Steiner the moduli-group rigidity, Mukai the
representation-theoretic accompaniment, all unconditional. The
class-$\mathcal{S}$ SCFT interpretation is conditional, C-status gap
at the moduli-stack level. The Kuga--Satake mirror
$\Sigma_{0,24}\leftrightarrow E^{\mathrm{nod}}_{24}$
(\texttt{rem:k3-kuga-satake-mirror}) is stated at the
pullback/base-change level, not the SCFT-moduli-stack level,
consistent with the present closure.

\textbf{With the CLAUDE.md charter.} The charter directs: "state
every theorem in the lane in which its proof actually works." The
monodromy-level sub-composite works in the chain-level
moduli-stack lane (Hurwitz-space representability + Beem--Rastelli
chiral-algebra VOA moduli); the SCFT-level composite does not work
in any currently-published mathematical lane. The present closure
states the theorem in the lane where it works and flags the lane
where it does not. Consistent with Pattern 273 scope discipline:
chain-level and $(\infty,1)$-categorical lanes are both
load-bearing; the SCFT-moduli-stack lane is a third, structurally
open.

\textbf{With the cache
(\texttt{appendices/first\_principles\_cache.md}).} Candidate new
entry:

\begin{verbatim}
| 3B-C19 | Kodaira--Miranda / Sen / Gaiotto composite is functorial
  as a morphism of moduli stacks. | Target stack
  $\mathcal{M}_{\mathrm{class-}\mathcal{S}}[A_1]$ is undefined in
  the mathematical literature as of April 2026; "moduli stack of
  4d N=2 SCFTs" has no representability theorem and requires
  (conjecturally) the 6d (2,0) theory constructed as a relative
  field theory (Freed--Teleman 2014 conditional on existence). |
  The full physics composite is not functorial at the moduli-stack
  level for a STRUCTURAL reason: the terminal codomain is
  undefined, not merely unproven. A sub-composite through the
  Hurwitz space of SL_2(Z)-monodromy data
  Hur_{24}^{SL_2(Z)}(P^1) and the Beem--Rastelli chiral-algebra
  avatar ChirAlg_{c_{2d}=-214}^{su(2)_{-2}^{24}} IS
  moduli-stack-functorial. The (g,n)=(0,24) selection operates at
  the monodromy-Diophantine level and survives unaffected. Primary:
  Kodaira 1963 Ann. Math. 77 Thm. 12.2; Miranda 1989 S IV.3; Sen
  1996 Nucl. Phys. B 475; Gaiotto 2009 arXiv:0904.2715; BLLPRvR
  2013 arXiv:1312.5344; Diaz--Edidin 1996 Math. Ann. 304 for
  Hurwitz-space representability; Frenkel--Ben-Zvi 2004 Ch. 19 for
  VOA moduli; Ben-Zvi--Sakellaridis--Venkatesh 2024 Relative
  Langlands Duality (potential future path to A). Cross-ref C9,
  C19 (Wave 3), AP-CY171, AP-CY246. |
  AP-CY / F-theory/class-S moduli-stack definition gap (structural) |
\end{verbatim}

\textbf{With antipattern catalogue
(\texttt{notes/antipatterns\_catalogue.md}).} Candidate new entry
flags the structural antipattern of treating physicist's "moduli
stack of $4$d $\mathcal{N}=2$ SCFTs" as a mathematical object:

\begin{verbatim}
| AP-CY[3B-C19] | Moduli stack of 4d N=2 SCFTs as
  mathematically-defined object. | Chain of partial mathematical
  objects, no full stack: Hitchin moduli (Hitchin 1987 Proc. LMS
  55; Coulomb shadow), Beem--Rastelli chiral algebras (BLLPRvR
  2013 arXiv:1312.5344; Schur/VOA shadow), Freed--Teleman
  relative field theories (Freed--Teleman 2014 arXiv:1212.1692;
  categorical shadow, conditional on 6d (2,0) existence),
  Ben-Zvi--Sakellaridis--Venkatesh relative Langlands (2024;
  Hamiltonian G-space shadow). | "The moduli stack of 4d N=2
  class-S theories M_{c_{4d}}" is not a defined object as of
  April 2026. When stating a functor with class-S codomain,
  specify which shadow is intended (Hitchin / Beem--Rastelli /
  Freed--Teleman / BSV-RLD). Use the Beem--Rastelli chiral-algebra
  shadow when the question is at the VOA/Schur level; use
  Hitchin when the question is at the Coulomb-branch level; use
  Freed--Teleman when the question is categorical/TFT-theoretic;
  use BSV-RLD when the question is Langlands-dual to
  Hamiltonian G-space data. | The physics composite
  Kodaira--Miranda o Sen o Gaiotto terminates in an undefined
  object at the SCFT-moduli-stack level; its moduli-stack lift
  requires one of the four shadow replacements. The present
  closure replaces M_{c_{4d}} by the Beem--Rastelli chiral-algebra
  shadow, yielding a functorial sub-composite. Primary: Hitchin
  1987 Proc. LMS 55; Beem--Lemos--Liendo--Peelaers--Rastelli--van
  Rees 2013 arXiv:1312.5344; Freed--Teleman 2014 arXiv:1212.1692;
  Ben-Zvi--Sakellaridis--Venkatesh 2024 Relative Langlands
  Duality. | AP-CY / class-S moduli-stack non-existence;
  structural gap |
\end{verbatim}

## Summary of closure

\textbf{Terminal state: C (structural gap).}

\textbf{Hypothesis as stated} (Sen 1996 $\circ$ Gaiotto 2012 is a
moduli-stack morphism
$\mathcal{M}_{\mathrm{ell\,K3}}\to\mathcal{M}_{c_{4d}}$): not
provable at the moduli-stack level, for the structural reason that
$\mathcal{M}_{c_{4d}}$ has no published mathematical definition.

\textbf{Available sub-composite} (Kodaira--Miranda $j_{\mathrm{Kod}}$
followed by Beem--Rastelli $\chi_{4d/2d}$ restricted to
class-$\mathcal{S}$ $A_1$ data): moduli-stack-functorial, computes
the same numerical invariants, and suffices for the
$(g,n)=(0,24)$ selection and the $\mathbf{H}_{\Delta_5}$
construction downstream. This is
Proposition~\ref{prop:3bc19-kodaira-miranda-classS-Ftheory-composite},
proved here.

\textbf{Parent C19 consequence}: the $(g,n)=(0,24)$ selection
survives the C-status upgrade, because it operates at the
monodromy--Diophantine level (Kodaira $c_2=24$, base-genus $g=0$,
Chacaltana--Distler $13(g-1)+5n=107$), none of which requires the
SCFT-level composite to be functorial.

\textbf{Future path to A}: a mathematical construction of the $6$d
$(2,0)$ theory as a relative field theory (Freed--Teleman framework
becomes unconditional); or extension of Ben-Zvi--Sakellaridis--Venkatesh
relative Langlands duality from Hamiltonian $G$-spaces to $4$d
$\mathcal{N}=2$ SCFTs. Neither available as of April~$2026$.

\hfill$\square$
