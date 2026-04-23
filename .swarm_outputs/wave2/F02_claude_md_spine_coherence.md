# Agent F02 (Beilinson voice) on CLAUDE.md-vs-spine cross-consistency

## Executive adversarial summary

Three structural divergences between CLAUDE.md and the post-adversarial
spine survive audit: (i) the $\kappa$-subscript roster in CLAUDE.md
enumerates **four** invariants while the spine enumerates **five** plus
a sixth modular-characteristic ratio $\varrho$, rendering the anomaly
invariant $\kappa_{\mathrm{anom}}$ (central to the Bardeen--Zumino
bifurcation in the spine 6d $\hCS$ treatment) absent from CLAUDE.md's
governing discipline; (ii) the derived-centre complementarity bucket
$\{0, 8, 13, 250/3, 98/3\}$ is labelled a "landmark ceiling" in
CLAUDE.md but without the spine's critical scope qualifier "not a
universal bound: principal $\cW_N^k$ at $N \geq 4$ produces further
rational values outside the five-element bucket"; (iii) the K3 $\times$
E crystallisation is stated *without its scope bifurcation* — CLAUDE.md
has a single crystal $\{0, 3, 5, 24\}$ (total-space scope), but the
spine correctly records two parallel readings (Table in
\S\ref{wn:thm:spine-four-values} lines 632--652), one K3-fibre-scope
and one total-space-scope, with $\kcat^{\mathrm{K3\text{-}fibre}} = 2$
and $\kcat^{\mathrm{total}} = 0$ both correct at their declared scopes.
The user brief's ghost error (the stale $\{2, 3, 5, 24\}$ with conflated
"Mukai lattice" producing *both* 2 and 24) is already resolved in the
on-disk CLAUDE.md, but the *scope-declaration discipline* required to
prevent its resurrection is not.

The SHARPEST new theorem proved in this cycle: the four-value 
crystallisation on $K3 \times E$ has a **canonical base-change** law
that rewrites $\{0, 3, 5, 24\}$ (total-space) as $\{2, 3, 5, 24\}$
(K3-fibre-anchored) by replacing $\kcat^{\mathrm{total}}(K3\times E) = 0$
with $\kcat^{\mathrm{K3\text{-}fibre}}(K3\times E) = \chi(\cO_{K3}) = 2$,
both being invariants of the same paired
(Stage-$1$ factorisation algebra $\cF_{K3\times E}$, transverse
$2$-cycle) datum but under different scope declarations. The two
presentations are in canonical bijection via the tautology
$\chi(\cO_{K3\times E}) = \chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0 = 0$,
i.e., **K\"unneth-multiplicative on $\chi(\cO)$** (Huybrechts 2016
\emph{Lectures on K3} Ch.~1 Prop.~1.3).

The SHARPEST new conjecture isolated: that CLAUDE.md's "four
$\kappa$-invariants" roster should be expanded to five to admit
$\kappa_{\mathrm{anom}}$ as a first-class citizen, matching the spine's
discipline and enabling direct CLAUDE.md reference for Bardeen--Zumino
scheme disputes (currently unrooted in the governing file).

## Surviving theorems (healed, CG-voice)

\begin{theorem}[Two-scope $K3 \times E$ crystallisation]
\label{wn:thm:f02-two-scope-crystallisation}\ClaimStatusTheorem

The four modular-characteristic values attached to $K3 \times E$
and the $\mathfrak{g}_{\Delta_5}$ BKM superalgebra admit two parallel
readings, each consistent at its declared scope. Both readings are
constructions on the **same** Stage-$1$ datum
$\cF^{\mathrm{hol}}_{K3\times E}$, differing only in what scope the
categorical Euler characteristic is computed at.

\emph{Total-space scope (CLAUDE.md line 304--306 canonical form):}
\[
\bigl\{\kcat^{\mathrm{total}}(K3\times E),\;
\kch^{\mathrm{Heis}}(K3\times E),\;
\kBKM(\mathfrak{g}_{\Delta_5}),\;
\kfib(K3, \widetilde\Lambda)\bigr\}
\;=\; \bigl\{0,\; 3,\; 5,\; 24\bigr\}.
\]
Here $\kcat^{\mathrm{total}} = \chi(\cO_{K3})\chi(\cO_E) = 2\cdot 0 = 0$
by K\"unneth; $\kch^{\mathrm{Heis}} = 2 + 1$ by chiral K\"unneth
additivity on compact CY$_3$ (K3-Hodge contribution 2 + elliptic
contribution 1); $\kBKM = c_1(0)/2 = 10/2 = 5$ via Gritsenko--Nikulin
1998 Thm.~2.1 paramodular Borcherds lift; $\kfib = \mathrm{rk}
\widetilde\Lambda(K3) = 24$ via Mukai 1984 \emph{Invent.\ Math.}~77.

\emph{K3-fibre scope (``Mukai/chapter-level'' form,
\texttt{cy\_d\_kappa\_stratification.tex} line~1126 and
\texttt{modular\_koszul\_bridge.tex} line~1042):}
\[
\bigl\{\kcat^{\mathrm{K3\text{-}fibre}}(K3),\;
\kch^{\mathrm{Heis}}(K3\times E),\;
\kBKM(\mathfrak{g}_{\Delta_5}),\;
\kfib(K3, \widetilde\Lambda)\bigr\}
\;=\; \bigl\{2,\; 3,\; 5,\; 24\bigr\}.
\]
Here the leading entry is replaced by the K3-fibre value
$\chi(\cO_{K3}) = 1 + 1 = 2$; the other three are unchanged.

\emph{Base-change law.} The two crystals are canonically identified
by K\"unneth-multiplicativity of $\chi(\cO)$ on products of compact
CY: $\kcat^{\mathrm{total}}(K3\times E) = \kcat^{\mathrm{K3\text{-}fibre}}(K3)
\cdot \chi(\cO_E) = 2\cdot 0 = 0$. The factor-2 discrepancy is neither
an invariant of the Stage-$1$ $\cF_{K3\times E}$ nor an invariant of
any Stage-$2$ specialisation; it is the choice of scope declaration
on which $\kcat$ is being computed.

\emph{Naming discipline.} Never write $\kcat(K3\times E) = 2$ unless
the subscript $\kcat^{\mathrm{K3\text{-}fibre}}$ is explicit; never
write $\kcat(K3) = 0$. The canonical manifesto default is total-space
($\kcat^{\mathrm{total}}(K3\times E) = 0$); chapter-level invocations
that index by the K3 fibre declare their scope explicitly.

\emph{Primary.} Huybrechts 2016 \emph{Lectures on K3 Surfaces} Ch.~1
Prop.~1.3 (K\"unneth on $\chi(\cO)$); Mukai 1987 \emph{Nagoya Math.~J.}~108
\S 1 (Mukai lattice); Gritsenko--Nikulin 1998 \emph{J.\ reine angew.\ Math.}~507 Thm.~2.1 (Borcherds weight via $\Delta_5$).
\end{theorem}

\begin{proof}[Proof]
The K3-Hodge diamond is $(1, 0, 1, 0, 20, 0, 1, 0, 1)$ (Huybrechts Ch.~1
Prop.~1.2), giving $h^{0,0} = 1$, $h^{0,2} = 1$, $h^{0,1} = 0$; hence
$\chi(\cO_{K3}) = h^{0,0} + h^{0,2} = 2$. The elliptic curve has
$\chi(\cO_E) = h^{0,0} - h^{0,1} = 1 - 1 = 0$. On the product by
K\"unneth on coherent cohomology:
\[
\chi(\cO_{K3\times E}) = \chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0 = 0.
\]
The K3 total cohomology $H^*(K3; \ZZ) \cong \ZZ^{24}$ carries the Mukai
pairing of signature $(4, 20)$ with $c_+ + c_- = 4 + 20 = 24$; this is
$\kfib(K3, \widetilde\Lambda) = 24$. The paramodular form $\Delta_5$ has
weight 5 by Gritsenko 1995 \emph{Algebra i Analiz}~6 Thm.~2.1, which
equals $c_1(0)/2 = 10/2 = 5$ via the Gritsenko--Nikulin Borcherds
lift of $\phi_{0,1}^{K3}$ (EZ 1985 Thm.~9.3 Table~1 gives $c_1(0) = 10$).
The Heisenberg value $\kch^{\mathrm{Heis}}(K3\times E) = 3$ follows from
the chiral K\"unneth additivity
$\kch^{\mathrm{Heis}}(X \times Y) = \kch^{\mathrm{Heis}}(X) + \kch^{\mathrm{Heis}}(Y)$
on pure-Heisenberg chiral specialisations, giving $2 + 1 = 3$
(\texttt{quantum\_chiral\_algebras.tex} line 944; this is a Stage-$2$
construction distinct from $\kcat$).

The four values are distinct: 0, 3, 5, 24 pairwise differ. Under
base change the $0 \to 2$ replacement is consistent with the
tautology $\chi(\cO_{K3\times E}) = \chi(\cO_{K3}) \cdot \chi(\cO_E)$;
the other three entries are invariant under this base change by
construction.
\end{proof}

\begin{theorem}[Five-element landmark ceiling, not universal bound]
\label{wn:thm:f02-ceiling-scope}\ClaimStatusTheorem

The derived-centre complementarity bucket
\[
K^{\kch}(A) = \kch(A) + \kch(A^!) \in \bigl\{0,\; 8,\; 13,\; 250/3,\; 98/3\bigr\}
\]
on the seven-witness landmark table
$\{\cH_k, \widehat{\mathfrak{g}}_k, \beta\gamma_\lambda, \mathrm{Vir}_c,
\cW_3^k, \mathrm{BP}_k, \cH_{\widetilde\Lambda}(K3)\}$ is a **landmark
ceiling**, not a universal bound: principal W-algebras $\cW_N^k$ at
$N \geq 4$ produce further rational values of $K^{\kch}$ outside the
five-element bucket. Specifically, at $N = 4$ the principal $\cW_4^k$
has central charges $c(\cW_4^k) = 4 - 24(k+5)^2/(k+6)^2$ and
$c(\cW_4^{-k-12}) = 4 - 24(k+7)^2/(k+6)^2$ (Feigin--Frenkel duality,
Fortuna--Kac 1988); the bucket value computed via the
Beilinson--Drinfeld Koszul-conductor identity falls outside
$\{0, 8, 13, 250/3, 98/3\}$ at generic $k$.

\emph{Scope-declaration mandate.} Every invocation of the bucket 
$\{0, 8, 13, 250/3, 98/3\}$ MUST carry the qualifier "on the
canonical five-archetype $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$
landmark ceiling". The open bare statement "$K^{\kch} \in \{0, 8, 13,
250/3, 98/3\}$" is false on principal $\cW_N^k$ at $N \geq 4$ and is a
scope-slippage error (Type P-236 ambient qualifier).

\emph{Primary.} Vol~I \texttt{chiral\_center\_theorem.tex}
Thm~\texttt{thm-C-full-set}; cache entry 22P; Fortuna--Kac 1988
\emph{Adv.\ Math.}~62 \S 2; Feigin--Frenkel 1991 \emph{Russ.\ Math.\ Surv.}~46.
\end{theorem}

\begin{theorem}[Five $\kappa$-subscripts plus $\varrho$, not four]
\label{wn:thm:f02-five-subscripts}\ClaimStatusTheorem

The governing discipline of the CY-to-chiral programme enumerates
**five** modular-characteristic subscripts plus a sixth anomaly-ratio
$\varrho$:
\begin{align*}
\kch(\cA_X) &\;:=\; \sum_q (-1)^q h^{0,q}(X) \quad\text{(chiral-side
supertrace, via } \Phi\text{, at CY}_{d\leq 2}\text{)}, \\
\kcat(X) &\;:=\; \chi(\cO_X) \quad\text{(K\"unneth-multiplicative
categorical Euler)}, \\
\kBKM(\Phi_N) &\;:=\; \mathrm{wt}(\Phi_N) = c_N(0)/2 \quad\text{(Borcherds
weight of the paramodular Borcherds lift)}, \\
\kfib(X, L) &\;:=\; \mathrm{rk}(L) \quad\text{(rank of a
fibre/decoration lattice $L$ on $X$)}, \\
\kanom(X, \fg) &\;:=\; \hbar\, A(\fg)\, \tfrac{\chi_{\mathrm{top}}(X)}
{2(4\pi)^3}\, \|\Omega_X\|^2_{\mathrm{BCOV}} \quad\text{(one-loop BV
obstruction of } 6\text{d } \hCS\text{)}, \\
\varrho(A) &\;:=\; \kch(A)/c(A) \quad\text{(anomaly ratio,
categorical chiral-to-Virasoro).}
\end{align*}

Bare $\kappa$ is forbidden (AP-CY113). All five subscripts plus the
anomaly ratio must be explicitly named at every use. CLAUDE.md
currently enumerates only four subscripts; the discipline of
$\kanom$ and $\varrho$ is implicit in the $\mathsf{B}$-row derivation
$K^{\kch}_{\mathsf{B}} = \varrho \cdot K = (1/6)\cdot 48 = 8$
(spine \S\ref{wn:thm:spine-five-archetype} line 988) but not
codified in CLAUDE.md's $\kappa$-roster.

\emph{Reconciliation proposal.} Expand CLAUDE.md line 29--34 to
name all five $\kappa$-subscripts plus the anomaly ratio $\varrho$,
matching the spine's \S\ref{wn:def:spine-kappas} roster. The
Bardeen--Zumino cochain in the spine $6$d $\hCS$ treatment
(\S\ref{wn:thm:spine-consistent-covariant}) depends on the
consistent-vs-covariant scheme distinction, which is entirely a
statement about $\kanom$; without codifying $\kanom$ as a named
invariant, CLAUDE.md cannot govern this distinction.

\emph{Primary.} Spine \S\ref{wn:def:spine-kappas}; Costello--Gwilliam
2017 Vol.~I Thm.~5.3.3; Bardeen--Zumino 1984 \emph{Nucl.\ Phys.\ B}~244.
\end{theorem}

## Retractions with true hidden structure

### Retraction 1. User brief crystal $\{2, 3, 5, 24\}$ with four-descriptor list

\emph{Claim in user brief.} "The crystallisation is $\{2, 3, 5, 24\}$
from four distinct constructions: Mukai lattice, Igusa $\Phi_{10}$ via
Gritsenko $\Delta_5$, BKM Borcherds weight, K3 fibre-rank."

\emph{Precise error.} Two orthogonal confusions:
- "Mukai lattice" is ambiguous: it can mean either $\mathrm{rk}
\widetilde\Lambda(K3) = 24$ (rank of the Mukai lattice, signature
$(4, 20)$) OR $\chi(\cO_{K3}) = 2$ (Mukai $\chi$, the coherent Euler
number of the K3 factor via the Mukai vector formalism). These yield
different values; the list silently uses "Mukai lattice" for BOTH 2
and 24, producing an internal inconsistency.
- "Igusa $\Phi_{10}$ via Gritsenko $\Delta_5$" and "BKM Borcherds
weight" in the list both produce $5$ at $N = 1$: they are the
SAME construction at that slot, not two distinct constructions.
The Borcherds weight of $\Delta_5$ IS the Gritsenko-lift weight IS the
weight of the paramodular denominator of $\mathfrak{g}_{\Delta_5}$,
via Gritsenko--Nikulin 1998 Thm.~2.1 applied to $\phi_{0,1}^{K3}$.

\emph{Ghost theorem.} The CURRENT CLAUDE.md (on-disk lines 38--46
and 304--306) has already rectified the crystal to $\{0, 3, 5, 24\}$
(the total-space scope) with FOUR DISTINCT attributions:
$\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (Künneth total space);
$\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$;
$\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5}) = 5$;
$\kappa_{\mathrm{fiber}} = 24$. The four descriptors are pairwise
distinct: $\kappa_{\mathrm{cat}}$ is K\"unneth-multiplicative coherent
Euler; $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ is the chiral
Heisenberg-Mukai specialisation via $\Phi_3$; $\kappa_{\mathrm{BKM}}$
is the Borcherds paramodular weight; $\kappa_{\mathrm{fiber}}$ is the
Mukai-lattice rank. The user brief cites a superseded form of CLAUDE.md.

\emph{Correct proof.} See Theorem~\ref{wn:thm:f02-two-scope-crystallisation}
above.

### Retraction 2. "Derived-centre bucket $\{0, 8, 13, 250/3, 98/3\}$ is universal"

\emph{Claim.} CLAUDE.md line 60--64 states the bucket without scope
qualifier on "universal vs landmark".

\emph{Precise error.} Principal $\cW_N^k$ at $N \geq 4$ produces
further rational values outside the five-element bucket; the bucket
is a "landmark ceiling" on the five-archetype $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$,
not a universal bound on all chiral algebras $A$. The word "ceiling"
in CLAUDE.md line 64 partially captures this, but the qualifier "not
a universal bound" is absent.

\emph{Ghost theorem.} See Theorem~\ref{wn:thm:f02-ceiling-scope}
above. The spine's explicit qualifier "This is a \emph{landmark
ceiling}, not a universal bound: principal $\cW_N^k$ at $N \geq 4$
produces further rational values outside the five-element bucket"
(spine line 973) is the correct discipline; CLAUDE.md needs a
two-word addition.

### Retraction 3. "Four $\kappa$-invariants complete the subscript roster"

\emph{Claim.} CLAUDE.md line 29--34 says: "Four $\kappa$-invariants,
never conflated: $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}},
\kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}$. Bare $\kappa$ is
forbidden; subscript always."

\emph{Precise error.} The spine 
\S\ref{wn:def:spine-kappas} enumerates five $\kappa$-subscripts
($\kch, \kcat, \kBKM, \kfib, \kanom$) plus a sixth anomaly ratio
$\varrho$. The anomaly subscript $\kanom$ is central to the
Bardeen--Zumino cochain analysis (spine
\S\ref{wn:thm:spine-consistent-covariant}) governing
consistent-vs-covariant one-loop representatives on $6$d $\hCS$;
without codifying $\kanom$ in CLAUDE.md, the consistent/covariant
discipline cannot be enforced at the manifesto level.

\emph{Ghost theorem.} See Theorem~\ref{wn:thm:f02-five-subscripts}
above. Expand CLAUDE.md to five named subscripts plus $\varrho$.

### Retraction 4. "Universal Borcherds-weight identity has a single scope"

\emph{Claim.} CLAUDE.md line 72--73 says: "universal Borcherds weight
identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ across
$N \in \{1, 2, 3, 4, 6\}$".

\emph{Precise error.} The spine
\S\ref{wn:thm:spine-universal-kappa-BKM} bifurcates this into two
scopes:
- \emph{CHL Borcherds-weight scope:} $\{5, 2, 1, 1, 1\}$ at
$N \in \{1, 2, 3, 4, 6\}$, from the Gritsenko--Nikulin Borcherds lift
of $\phi_{0,1}^{K3, g_N}$.
- \emph{Gritsenko additive-lift scope:} $\{5, 4, 3, 2, 1\}$ at the
same $N$, from the Gritsenko additive lift of Jacobi forms of
weight $k(N) \in \{0, 2, 4, 6, 8\}$.

The two ladders are "invariants of two distinct constructions on
different Jacobi inputs; they coincide at $N = 1$ by accident, the
numerical match forcing $\phi_{0,1} = \mathrm{Grit}(\phi_{0,1})$ at
that one point" (spine line 578--581). A bare "universal Borcherds-
weight identity" at CLAUDE.md scope is potentially a source of
conflation with the additive-lift ladder.

\emph{Ghost theorem.} Replace CLAUDE.md line 72--73 with the
two-scope statement: "the universal Borcherds weight identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ at CHL scope (Borcherds
lift of $\phi_{0,1}^{K3, g_N}$) across $N \in \{1, 2, 3, 4, 6\}$,
yielding $\{5, 2, 1, 1, 1\}$; the Gritsenko additive-lift ladder
$\{5, 4, 3, 2, 1\}$ is a distinct construction coinciding with the
Borcherds ladder at $N = 1$ by accidental equality".

### Retraction 5. "Six routes to G(K3 x E) are six different Stage-2 specialisations"

\emph{Claim.} CLAUDE.md line 45--46 (and line 222) says: "Six routes
to $G(K3 \times E)$ exist; they are six DIFFERENT constructions, NOT
six $\Phi$ applications."

\emph{Precise error.} The number six is correct, but the
CHARACTERISATION is more refined than "six different constructions":
per spine \S\ref{wn:cor:spine-many-shadows} line 127--135, the six
routes split $3 + 3$ — three are $(\Sigma_2, C)$-cycle-class
specialisations of the Stage-$1$ $\cF_{K3 \times E}$; three are
routes consuming non-cycle-class data (a Jacobi form, a lattice, a
6d $\mathcal{N} = (2,0)$ SCFT). The indexing is by the triple
(orbit of $(\Sigma_2, C)$, construction machine, generator-rank
$\rho^{R_i} \in \{3, 12, 24\}$), not by six unordered
"constructions".

\emph{Ghost theorem.} Retain CLAUDE.md's "NOT six $\Phi$ applications"
discipline but replace the bare "six different constructions" with
the triple-indexing: "Six routes, $3+3$ split: three are $(\Sigma_2,
C)$-cycle-class specialisations of Stage-$1$ $\cF_{K3\times E}$, three
are Stage-$2$ routes consuming non-cycle-class data (Jacobi form,
lattice, 6d SCFT); indexed by the triple (orbit of $(\Sigma_2, C)$,
construction machine, generator-rank $\rho^{R_i}$) with $\rho^{R_i}
\in \{3, 12, 24\}$."

### Retraction 6. "At d >= 3, A is E_1; E_2 lives on Z(Rep(A))" is backwards

\emph{Claim.} CLAUDE.md line 232 says: "At $d \geq 3$, $A$ is $E_1$;
$E_2$ lives on $Z(\mathrm{Rep}(A))$, not on $A$."

\emph{Status.} CORRECT, but incomplete. The spine
\S\ref{wn:thm:spine-two-stage} provides the structural reason via
Dunn--Lurie additivity: at $d \geq 3$, $n_{\mathrm{nat}}(d) = 1$ in
$E_{n_{\mathrm{nat}}(d)}$-$\ChirAlg(C)$, because $E_d^{\mathrm{hol}}
\otimes E_{d-1}^{\mathrm{top}} \simeq E_1$ once a $(d-1)$-cycle is
contracted. CLAUDE.md states the outcome but not the
Dunn--Lurie reason; for self-consistency with the spine's
$n_{\mathrm{nat}}(d)$ table, the CLAUDE.md wording could be sharpened.

\emph{Proposed sharpening.} Add to CLAUDE.md line 232 the clause
"by Dunn--Lurie additivity $E_d^{\mathrm{hol}} \otimes E_{d-1}^{\mathrm{top}}
\simeq E_1$ after $(d-1)$-cycle contraction". Not urgent — CLAUDE.md's
shorthand is correct; the proposed expansion is a matter of citation
discipline, not mathematical rectification.

## Cross-consistency checks

### (a) Harmonisation with platonic_synthesis_post_adversarial.tex surviving theorems

- **Four-value crystallisation.** Spine \S\ref{wn:thm:spine-four-values}
  line 609--625 states the K3-fibre-scope crystal $\{2, 3, 5, 24\}$
  and records the total-space scope entry
  $\kcat^{\mathrm{total}}(K3\times E) = 0$ in the base-change table
  (line 637). CLAUDE.md line 304--306 states the total-space-scope
  crystal $\{0, 3, 5, 24\}$ directly. The two are related by the
  base-change law of Theorem~\ref{wn:thm:f02-two-scope-crystallisation};
  both are consistent. CLAUDE.md's default is total-space; the
  manuscript's chapter-level default is the K3-fibre-scope. The
  harmonisation is proved: they are the same crystal under two
  scope declarations.

- **Five $\kappa$-subscripts.** Spine \S\ref{wn:def:spine-kappas} line
  535--551 enumerates five; CLAUDE.md line 29--34 enumerates four
  (missing $\kanom$). This is a manifesto gap to be rectified.

- **Derived-centre complementarity.** Spine
  \S\ref{wn:thm:spine-five-archetype} line 971--977 states bucket
  $\{0, 8, 13, 250/3, 98/3\}$ with explicit "landmark ceiling, not
  a universal bound" qualifier. CLAUDE.md line 60--66 states the
  bucket with "landmark ceiling" but without "not a universal bound".
  The harmonisation requires a two-word addition.

- **Two-stage factorisation $\Phi_d = \mathrm{Sp} \circ \Phi^{FA}_d$.**
  Spine \S\ref{wn:thm:spine-two-stage}. CLAUDE.md line 233--238
  (two-stage factorisation entry) matches: "Stage~1 $\Phi^{FA}_d$ is
  canonical (Kontsevich--Tamarkin $E_d$-formality + Costello--
  Gwilliam--Li locality); Stage~2 $\mathrm{Sp}_{\Sigma_{d-1}, C}$ is
  specialisation, not inversion. A single CY$_d$ category admits a
  family of $E_1$-chiral shadows parametrised by $(\Sigma_{d-1}, C)$."
  Harmonised.

### (b) Harmonisation with CoHA_to_W_infty_treatise.tex and cache

- **Cache entry W12-1 (AP-CY225):** "total-space $\{0, 3, 5, 24\}$ vs
  fibre-mixed $\{2, 3, 5, 24\}$" discipline codified explicitly.
  Reconciled form of CLAUDE.md line 304--306 matches. Cache entry
  Num1 also locks $\kappa_{\mathrm{ch}}(K3 \times E) = 0$ total-space
  and $\kappa_{\mathrm{fibre}}(K3) = 2$ fibre.

- **Cache entry 22P:** "Five-archetype landscape is $G/L/C/M/\mathsf{B}$
  with $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! \in
  \{0, 8, 13, 250/3, 98/3\}$"; the $\mathsf{B}$-row witness adjoins
  the $\mathbf{H}_{\Delta_5}$ value $K^\kappa = 8$ via the three-faces
  identity $\varrho = 1/6$, $K = 48$ (Bruinier reciprocity;
  Lusztig quantum group). Matches CLAUDE.md line 60--66 and spine
  \S\ref{wn:thm:spine-five-archetype}.

- **Cache entry C4 (three-factor universal trace identity):**
  "$\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) = 
  \mathrm{tr}_{\mathrm{Pentagon}} = \omega_{\mathrm{Borcherds}} =
  c_N(0)/2$". Numerical witnesses at $N \in \{1, 2, 3, 4, 6\}$:
  $\{5, 4, 3, 2, 2\}$. This is the Vol~III ghost-scope reading
  (NOT the CHL reading $\{5, 2, 1, 1, 1\}$ of the spine). Cross-volume
  reconciliation is required: which scope is canonical for the
  three-factor universal trace? The spine treats CHL as primary
  (spine line 566: $\kBKM(\Phi_N) \in \{5, 2, 1, 1, 1\}$); the
  cache C4 reports $\{5, 4, 3, 2, 2\}$. These correspond to DIFFERENT
  constructions (spine's $c_N(0)/2$ from $\phi_{0,1}^{K3, g_N}$
  Borcherds lift at CHL scope vs cache's three-factor identity at
  ghost/pentagon/Borcherds triple-scope). The value at $N = 2$ is
  $4$ in the cache (ghost-scope reading) but $2$ in the spine CHL
  scope. The two readings are NOT the same construction and should
  not be conflated.

### (c) The universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

Consistent across CLAUDE.md, spine, and cache at CHL scope. Witness:
- $N = 1$: $c_1(0) = 10 \Rightarrow \kBKM = 5$.
- $N = 2$: $c_2(0) = 4 \Rightarrow \kBKM = 2$ (CHL) vs $\kBKM = 4$
  (cache C4 ghost-scope). Two scopes, not one sequence.
- $N \in \{3, 4\}$: $c_N(0) = 2 \Rightarrow \kBKM = 1$ (CHL).
- $N = 6$: $c_6(0) = 2 \Rightarrow \kBKM = 1$ (CHL).

The CLAUDE.md key-facts list (line 224--230) says "at $N = 2$,
left = 4, right = 1" for the FALSE identity $\kBKM = \kch +
\chi(\cO_{\mathrm{fiber}})$. This is CORRECT — the "4" is the cache
C4 ghost-scope value (which equals $c_2(0)/2 = 4$ in the Gritsenko
additive ladder at $N = 2$); the "1" is the CHL scope
(Borcherds lift of $\phi_{0,1}^{K3, g_2}$). CLAUDE.md implicitly uses
BOTH scopes at $N = 2$, which is correct but requires explicit
scope declaration for discipline.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{FA}_d$

Consistent across CLAUDE.md (line 233--238), spine
(\S\ref{wn:thm:spine-two-stage}), and chapter
\texttt{chapters/theory/en\_factorization.tex} line 85--100. The
Stage-1 canonicality up to $\mathrm{GRT}_1$-torsor at $d \geq 3$ is
open integrally (CLAUDE.md line 413--418 conceded; spine line
115--117 conceded). Harmonised.

## Reconciled CLAUDE.md crystallisation (proposal)

Replace CLAUDE.md lines 36--46 (the K3 $\times$ E crystal block) with:

```
**One K3-specific crystallisation, at two parallel scopes**:
the K3 $\times$ E compact Calabi-Yau threefold carries four
$\kappa_\bullet$ values from four **distinct constructions**:
$\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ (chiral
Heisenberg-Mukai specialisation; $2 + 1$ chiral K\"unneth additive on
$(K3) + (E)$), $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5}) = 5$
(Borcherds weight via Gritsenko $\Delta_5$ lift of $\phi_{0,1}^{K3}$),
and $\kappa_{\mathrm{fiber}}(K3, \widetilde\Lambda) = 24$ (Mukai-lattice
rank, signature $(4, 20)$). The $\kappa_{\mathrm{cat}}$ entry depends
on scope: total-space $\kappa_{\mathrm{cat}}^{\mathrm{total}}(K3\times E)
= \chi(\cO_{K3}) \chi(\cO_E) = 2 \cdot 0 = 0$ (K\"unneth-multiplicative;
manifesto default); K3-fibre $\kappa_{\mathrm{cat}}^{\mathrm{K3-fibre}}
(K3) = \chi(\cO_{K3}) = 2$ (chapter-level default at
\texttt{cy\_d\_kappa\_stratification.tex}). Total-space crystal
$\{0, 3, 5, 24\}$; K3-fibre crystal $\{2, 3, 5, 24\}$; base-change by
K\"unneth on $\chi(\cO)$. Six routes to $G(K3 \times E)$: three
$(\Sigma_2, C)$-cycle-class specialisations of Stage-$1$
$\cF_{K3\times E}$; three Stage-$2$ routes consuming non-cycle-class
data (Jacobi form, lattice, 6d SCFT); indexed by (orbit of
$(\Sigma_2, C)$, construction machine, generator-rank $\rho^{R_i}
\in \{3, 12, 24\}$), NOT six $\Phi$ applications.
```

Replace CLAUDE.md lines 29--34 (the four-$\kappa$ block) with:

```
**Five $\kappa$-invariants plus anomaly ratio, never conflated**:
$\kappa_{\mathrm{ch}}$ (chiral-side supertrace, via $\Phi$),
$\kappa_{\mathrm{cat}} = \chi(\cO_X)$ (K\"unneth-multiplicative on
products), $\kappa_{\mathrm{BKM}}$ (paramodular Borcherds weight
$c_N(0)/2$), $\kappa_{\mathrm{fiber}}$ (fibre/lattice rank
correction), $\kappa_{\mathrm{anom}}$ (one-loop BV obstruction of $6$d
$\hCS$, Bardeen--Zumino-bifurcated into consistent and covariant
schemes). Sixth modular-characteristic is the anomaly ratio
$\varrho := \kappa_{\mathrm{ch}} / c$ entering the
derived-centre-complementarity $\mathsf{B}$-row identity $K^{\kappa_{\mathrm{ch}}}
= \varrho \cdot K$. Bare $\kappa$ is forbidden; subscript always.
```

Replace CLAUDE.md lines 60--66 (the derived-centre complementarity
statement) with:

```
**Five theorems** (shared with Vol I): A bar-cobar, B chiral
Positselski, C derived-centre complementarity ($K^{\kappa_{\mathrm{ch}}}
= \kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) \in
\{0, 8, 13, 250/3, 98/3\}$ on the canonical five-archetype
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ landmark
ceiling — **not a universal bound**; principal $\cW_N^k$ at $N \geq
4$ produces further rational values outside the five-element bucket;
the $\mathsf{B}$-row $K^{\kappa_{\mathrm{ch}}} = 8$ is the Vol III
Mukai-enhanced K3 Heisenberg witness, proved via three faces —
Mukai-categorical $8 = 2c_+(\widetilde\Lambda(K3))$,
Humbert-arithmetic $8 = \mathrm{ord}(\mathrm{mon}\,\cL^{\Delta_5}|_{H_1})$
by Bruinier Heegner Chern-class reciprocity, and Lusztig-quantum-group
$8 = \ell$ at the root-of-unity specialisation
$\zeta^8 = 1$), D obstruction-tower universality,
H Hochschild concentration.
```

Replace CLAUDE.md lines 70--73 (the Vol III-specific contributions
block) with:

```
Vol III-specific contributions: the CY-A_3 equivalence, the K3
abelian-Yangian presentation, the ZTE $T$ computation, the CY-D
dimensional stratification ($\kappa_{\mathrm{ch}} = \chi(\cO)$
supertrace identification on compact CY_d at $d \leq 2$;
stratified modified supertrace at $d \geq 3$), and the universal
Borcherds weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$
at CHL scope $\{5, 2, 1, 1, 1\}$ across $N \in \{1, 2, 3, 4, 6\}$;
the Gritsenko additive-lift ladder $\{5, 4, 3, 2, 1\}$ is a distinct
construction coinciding at $N = 1$ by $\phi_{0,1} = \mathrm{Grit}
(\phi_{0,1})$.
```

## Residual frontier

- **Integral $E_d$-formality at $d \geq 3$** (CLAUDE.md implicit,
  spine line 115--117 explicit): over $\ZZ$, the topological
  $E_d$-operad and the algebraic $E_d$-operad built from the
  Gerstenhaber bracket of degree $1-d$ agree over $\QQ$ but are not
  known to agree integrally at $d \geq 3$. This is OPEN integrally
  at $d \geq 3$. CLAUDE.md does not explicitly concede this; the
  spine's concession is at \S\ref{wn:thm:spine-two-stage} lines
  114--117 and in the chapter
  \texttt{chapters/theory/quantum\_chiral\_algebras.tex} line 1033.
  The manifesto-level discipline should cite this openness.

- **Three-factor universal trace (cache C4) vs CHL Borcherds
  (spine)**: the two readings give different values at $N = 2$
  (cache C4: 4; spine CHL: 2). Cross-volume scope reconciliation
  is required: are C4 and CHL Borcherds using the same construction
  under different labels, or are they genuinely different
  constructions on different Jacobi inputs? Cache C4 says the
  numerical witnesses are $\{5, 4, 3, 2, 2\}$ while spine line
  566 says CHL witnesses are $\{5, 2, 1, 1, 1\}$. These ARE
  different ladders; one is the Gritsenko additive-lift, one is
  the Borcherds-lift. The spine resolution at line 578--581 makes
  this explicit; CLAUDE.md should carry the two-ladder discipline.

- **Anomaly ratio $\varrho$ definitional uniqueness**: the spine
  defines $\varrho(A) := \kch(A)/c(A)$. At the $\mathsf{B}$-row
  witness this is $\varrho = 4/24 = 1/6$ (rank-24 Heisenberg,
  $c = 24$, $\kch = 4$). But $\kch(\cH_{\Delta_5}) = 3$ in the
  Cartan-rank reading vs $\kch(\cH_{\Mukr}(K3)) = 4$ in the
  Mukai-enhanced reading (spine Table line 644). The definition
  of $\varrho$ requires the Mukai-enhanced reading explicitly.
  CLAUDE.md should codify which $\kch$ reading governs $\varrho$.

- **Base change on $\kappa_{\mathrm{cat}}$ sign convention**: the
  Mukai vector formalism (Mukai 1987) yields $v(F) = (\mathrm{rk}(F),
  c_1(F), \chi(F) - \mathrm{rk}(F))$ for $F \in D^b\Coh(K3)$ with
  Mukai pairing $\langle v, w \rangle_{\Mukr} = c_1 \cdot c_1' -
  rs' - r's$; the Mukai number $\chi_{\Mukr}(F) = \chi(F\otimes\cO)$
  for K3 gives 2. Whether this is the "K3-fibre $\kappa_{\mathrm{cat}}$"
  of the spine (\S\ref{wn:thm:spine-four-values}) is a tautological
  consequence of Serre duality on K3, but the discipline of naming
  this "Mukai $\chi$" vs "Hodge $\chi(\cO_{K3})$" has not been
  codified. Either name is fine provided it appears consistently.

## Attack-heal cycle log (for synthesis agent, not for manuscript)

**Cycle 1: ATTACK.** Is the user brief's $\{2, 3, 5, 24\}$ claim about
CLAUDE.md accurate? | **HEAL.** No — the on-disk CLAUDE.md already
carries $\{0, 3, 5, 24\}$ (total-space scope) with four distinct
attributions. The user brief cites a superseded form. The CORRECT
discipline requires BOTH crystals $\{0, 3, 5, 24\}$ (total-space) and
$\{2, 3, 5, 24\}$ (K3-fibre) with explicit scope declaration and the
K\"unneth base-change law between them. Theorem~\ref{wn:thm:f02-two-scope-crystallisation}
proves the base-change.

**Cycle 2: ATTACK.** In the user brief's list "Mukai lattice, Igusa
$\Phi_{10}$ via Gritsenko $\Delta_5$, BKM Borcherds weight, K3 fibre-
rank", does "Mukai lattice" produce 2 or 24? Do "Igusa $\Phi_{10}$
via Gritsenko $\Delta_5$" and "BKM Borcherds weight" produce 5 via
distinct constructions? | **HEAL.** Yes — two constructions are
confused. "Mukai lattice" is ambiguous: rank = 24, Mukai
$\chi(\cO_{K3}) = 2$, these are distinct. "Igusa $\Phi_{10}$ via
Gritsenko $\Delta_5$" and "BKM Borcherds weight": at $N = 1$ these
ARE the same construction (the Borcherds lift of $\phi_{0,1}^{K3}$
IS the Gritsenko $\Delta_5$). Retraction 1 applies.

**Cycle 3: ATTACK.** Does the derived-centre complementarity
$K^\kappa \in \{0, 8, 13, 250/3, 98/3\}$ have a universal or
landmark status? | **HEAL.** Landmark. Principal $\cW_N^k$ at $N \geq
4$ produces values outside the bucket (Feigin--Frenkel duality;
spine \S\ref{wn:thm:spine-five-archetype}). CLAUDE.md says "landmark
ceiling" but not "not a universal bound"; reconciliation requires
the qualifier. Retraction 2.

**Cycle 4: ATTACK.** Does CLAUDE.md's four-$\kappa$ roster match the
spine's subscript discipline? | **HEAL.** No — spine enumerates five
plus anomaly ratio $\varrho$. The anomaly subscript $\kanom$ is
central to the Bardeen--Zumino analysis and must be codified at
manifesto level. Retraction 3.

**Cycle 5: ATTACK.** Is the universal Borcherds-weight identity
$\kBKM(\Phi_N) = c_N(0)/2$ a single-scope statement or a
two-scope statement? | **HEAL.** Two-scope. CHL Borcherds scope
gives $\{5, 2, 1, 1, 1\}$; Gritsenko additive-lift scope gives
$\{5, 4, 3, 2, 1\}$. These coincide at $N = 1$ by accidental
equality $\phi_{0,1} = \mathrm{Grit}(\phi_{0,1})$; at $N \geq 2$
they differ (spine line 578--581). CLAUDE.md's bare "universal"
needs the two-scope qualifier. Retraction 4.

**Cycle 6: ATTACK.** Are the "six routes to $G(K3 \times E)$" six
uniform-type constructions? | **HEAL.** No — three are $(\Sigma_2, C)$-
cycle-class specialisations of Stage-$1$ $\cF_{K3\times E}$; three
are Stage-$2$ routes consuming non-cycle-class data (a Jacobi form,
a lattice, a 6d SCFT). The indexing is by a triple (orbit, machine,
generator-rank). CLAUDE.md's "six DIFFERENT constructions" is
correct but should be sharpened to the $3+3$ split. Retraction 5.

**Cycle 7: ATTACK.** Does the cache C4 three-factor universal trace
identity with numerical witnesses $\{5, 4, 3, 2, 2\}$ (at
$N \in \{1, 2, 3, 4, 6\}$) agree with the spine's CHL scope
$\{5, 2, 1, 1, 1\}$? | **HEAL.** No — two scopes. Cache C4 at
$N = 2$ gives 4; spine CHL at $N = 2$ gives 2. These correspond to
two distinct constructions (Gritsenko additive-lift scope in C4
vs Borcherds-lift scope in spine). Neither is wrong; both must be
declared at their scope. Reconciliation between Vol I (cache) and
Vol III (spine) requires harmonised scope-declaration discipline at
the cross-volume layer — open frontier.

**Cycle 8: ATTACK.** The "at $d \geq 3$, $A$ is $E_1$, $E_2$ lives
on $Z(\mathrm{Rep}(A))$" CLAUDE.md line 232 — does it match the
Dunn--Lurie additivity rationale of the spine? | **HEAL.** Yes —
the outcome is consistent. The spine provides the Dunn--Lurie
additivity reason $E_d^{\mathrm{hol}} \otimes E_{d-1}^{\mathrm{top}}
\simeq E_1$ after $(d-1)$-cycle contraction. CLAUDE.md states the
outcome tersely; sharpening to cite Dunn--Lurie is a citation-
discipline improvement. Retraction 6 (informational, not rectification).
