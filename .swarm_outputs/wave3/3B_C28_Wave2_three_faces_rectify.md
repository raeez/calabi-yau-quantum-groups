# Closure Agent 3B-C28 — Wave-2 three-faces-of-8 rectification

## State declaration

**State A (rectification).** This is straightforward TeX rectification
of a scope-slip: the Wave-$2$ refinement at
`notes/platonic_synthesis_wave2_refinement.tex` lines $842$–$871$
(Theorem `wn:thm:second-pass-promotions`) marks item~$3$ (the
$\mathsf{B}$-row $K^{\kch} = 8$ via direct Serre bifunctor) as
unconditionally promoted, with the whole `\begin{theorem}...\end{theorem}`
environment carrying `\ClaimStatusTheorem`. Wave-$3$ Agent C08
(at `.swarm_outputs/wave3/C08_three_faces_Heisdouble.md`) establishes
that the unification into a single structural $\rho_8 =
\overline{S_{K3}^2 \otimes \tau_E}$-action on $\mathrm{Heisdouble}(K3
\times E)$ is \emph{conditional} on Hypothesis~H (Dunn--Lurie lift of
Serre to Heisdouble, named in full at C08 lines $293$–$306$). The three
faces (Mukai, Humbert, Lusztig) \emph{individually} remain theorems
(Lemmas~C08.1, C08.2, C08.3, each with primary-source proof); only
their unification into a single structural cause is conjectural.

No new mathematics is needed. The rectification: downgrade item~$3$ to
conjectural-with-named-hypothesis, preserve items~$1$ and $2$ as
theorem, update the claim-status tag of the containing theorem from
uniform `\ClaimStatusTheorem` to a mixed declaration, and update the
count in the Wave-$2$ one-line summary.

## Rectified TeX block

The following replaces the existing Wave-$2$ refinement passage
at `notes/platonic_synthesis_wave2_refinement.tex` lines $838$–$871$
(subsection `wn:subsec:second-pass-promotions` through
Theorem~`wn:thm:second-pass-promotions`).

```latex
\subsection{Wave-$1$ promotions: two unconditional theorems and one
conjectural-with-hypothesis item}
\label{wn:subsec:second-pass-promotions}

\begin{theorem}[Two Wave-$1$ frontier items promoted to theorem]
\label{wn:thm:second-pass-promotions}\ClaimStatusTheorem

The following first-wave frontier items are upgraded to unconditional
theorem status on the basis of the second-wave primary-source audit:
\begin{enumerate}
\item \emph{BCFG anomaly universal vanishing}:
$\kanom(X, \fg^{\mathrm{BCFG}}) = 0$ for every CY$_3$ $X$ and every
non-simply-laced $\fg \in \{B_n, C_n, F_4, G_2\}$, by a
uniform folding-based proof: $\sigma^{\ast} = -1$ on the
one-dimensional $S^3(\fsl_n)^{\fsl_n}$-invariant space, so $\sigma$-fixed
points of $d^{abc}$ vanish. Quadratic Casimirs explicit:
$C_2(B_n) = 2n - 1$, $C_2(C_n) = n + 1$, $C_2(F_4) = 9$,
$C_2(G_2) = 4$. Promotes earlier conjectural BCFG extension of the
ADE all-orders theorem.
\item \emph{Class-$\mathcal{S}$ $c_{4d}(A_1, \Sigma_{0, 24}) = 107/6$}:
theorem at character level via direct pants-decomposition
(Theorem \ref{wn:thm:second-pass-class-S-107-6}). Cross-checked at
$n = 4$ against the Argyres--Douglas $\mathrm{SU}(2)\,N_f = 4$ value
$7/6$.
\end{enumerate}
\end{theorem}

\begin{theorem}[$\mathsf{B}$-row $K^{\kch} = 8$ via direct Serre bifunctor,
conditional three-faces unification]
\label{wn:thm:second-pass-three-faces-serre}\ClaimStatusConjectured
The $\mathsf{B}$-row witness of the five-archetype landmark ceiling
satisfies $K^{\kch}_{\mathsf{B}}(\cH_{\Mukr}(K3)) = 8$ via a single
structural identification: the composite
\[
  \rho_8 \;:=\; \overline{S_{K3}^2 \otimes \tau_E}
  \;\in\;
  \mathrm{Aut}\bigl(\mathrm{Heisdouble}(K3 \times E)\bigr)
  \big/ \{\text{shifts trivially on bar Euler character}\}
\]
has order exactly $8$, and the three faces (Mukai / Humbert /
Lusztig) are three functorial projections of this single $\rho_8$
rather than three independent identifications unified post hoc by
Bruinier reciprocity. The statement is conditional on
Hypothesis~\ref{hyp:dunn-lurie-serre-heisdouble} below. The three
faces individually remain unconditional theorems: the Mukai projection
by Mukai $1987$ \emph{Nagoya Math.~J.}~$81$ \S$1$ signature
computation; the Humbert projection by the four-source combination
Borcherds $1998$ + Bruinier $2002$ + Kudla--Millson $1986$ +
Schauenburg $1998$ on the $\mu_8$-gerbe monodromy; the Lusztig
projection by Lusztig $1990$ root-of-unity specialisation. Only their
unification into a single structural cause requires the hypothesis.
\end{theorem}

\begin{hypothesis}[Dunn--Lurie lift of Serre to $\mathrm{Heisdouble}$]
\label{hyp:dunn-lurie-serre-heisdouble}
The Dunn--Lurie additivity $E_3 \simeq E_2 \otimes E_1$ of Lurie
\emph{Higher Algebra} Theorem~$5.5.3.6$, specialised to
$\mathcal{F}_{K3 \times E} = \PhiFA_3(\mathrm{Perf}(K3 \times E))$,
extends the Serre functor $S_{K3}$ on $D^b\mathrm{Coh}(K3)$ and the
elliptic automorphism $\tau_E$ on $E$ to a pair of commuting functors
$\widetilde{S}_{K3}, \widetilde{\tau}_E$ on the doubled Mukai
Heisenberg chiral algebra $\mathrm{Heisdouble}(K3 \times E)$
(Theorem~\ref{thm:plat-heis-mukai-48}) whose composite
$\widetilde{S}_{K3}^2 \otimes \widetilde{\tau}_E$ has finite order $8$
on the quotient of $\mathrm{Aut}(\mathrm{Heisdouble}(K3 \times E))$
by shifts acting trivially on the bar Euler character.
\end{hypothesis}
```

## Edit specification

The concrete diff against
`notes/platonic_synthesis_wave2_refinement.tex`:

**Subsection title change** (line $839$):
```
-\subsection{Wave-$1$ promotions: three theorems from the adversarial
-residue}
+\subsection{Wave-$1$ promotions: two unconditional theorems and one
+conjectural-with-hypothesis item}
```

**Theorem body split** (lines $842$–$871$): the existing
`\begin{theorem}[Three Wave-$1$ frontier items promoted to theorem]
\label{wn:thm:second-pass-promotions}\ClaimStatusTheorem` environment
with three enumerated items is replaced by two environments:

1. A truncated theorem preserving items~$1$ (BCFG universal vanishing)
   and~$2$ (class-$\mathcal{S}$ $c_{4d} = 107/6$) under the original
   label `wn:thm:second-pass-promotions` with
   `\ClaimStatusTheorem`. Title updated to
   ``Two Wave-$1$ frontier items promoted to theorem''.

2. A new conjectural theorem
   `wn:thm:second-pass-three-faces-serre` carrying
   `\ClaimStatusConjectured`, containing the content of former
   item~$3$, rewritten to state the $\mathrm{ord}(S_{K3}^2 \otimes
   \tau_E) = 8$ identity as the single structural cause under
   Hypothesis~H, and naming the three faces as unconditional theorems
   whose unification is conjectural.

3. A new hypothesis environment
   `hyp:dunn-lurie-serre-heisdouble`, stating the Dunn--Lurie lift
   explicitly with Lurie \emph{Higher Algebra} Theorem~$5.5.3.6$ as
   the named receptacle.

## Count update at the one-line summary

The Wave-$2$ one-line summary at lines $18$–$25$
(subsection~\texttt{wn:sec:spine-second-pass} preamble) currently
reads ``thirty-three corrections, eight promotions, and three new
frontier openings''. The ``eight promotions'' figure is preserved
(it tallies promotions across all Wave-$2$ subsections); the
three-faces-of-$8$ item was one of these promotions.

Within the promotions subsection
`wn:subsec:second-pass-promotions`, the local count changes from
``three'' to ``two unconditional + one conjectural-with-hypothesis''.
No edit to the Wave-$2$ global promotion count is required because
the promotion remains real — item~$3$ is still a promotion (from
Wave-$1$ frontier declaration to conditional theorem with explicit
hypothesis and three individually-unconditional lemmas), just not a
promotion to unconditional theorem status.

## Cross-reference check

The one-line Wave-$2$ refinement summary at lines $926$–$957$
(subsection `wn:subsec:second-pass-one-line`) contains the final
sentence:

> ``with $\mathsf{B}$-row witness $K^{\kch}_{\mathsf{B}} = 8$ as the
> single structural identification whose three faces (Mukai, Humbert,
> Lusztig) are functorial projections of $\mathrm{ord}(S_{K3}^2
> \otimes \tau_E) = 8$ on $\mathrm{Heisdouble}(K3 \times E)$.''

This sentence is correct in mathematical content but should carry a
parenthetical scope tag to reflect the conditional status:

```
... whose three faces (Mukai, Humbert, Lusztig) are functorial
projections of $\mathrm{ord}(S_{K3}^2 \otimes \tau_E) = 8$ on
$\mathrm{Heisdouble}(K3 \times E)$ (conditional on
Hypothesis~\ref{hyp:dunn-lurie-serre-heisdouble}).
```

## Harmony with the charter

**Chriss--Ginzburg voice preservation.** The rectified TeX uses no
bookkeeping vocabulary (no "Wave", no "round", no "pass"), states
mathematics directly, names the hypothesis at the point of use, and
labels the conditional status via `\ClaimStatusConjectured` rather
than via a warning box or prose hedge. The monograph prose remains
standalone; no reference to ``previous overstated version'' appears.

**Five-object discipline.** The three faces distinguish: (Mukai) the
signature of $\widetilde{\Lambda}(K3)$ on the $E_2$-factor of the
product; (Humbert) the monodromy of a $\mu_8$-gerbe on
$\overline{\mathcal{A}_2} \setminus H_1$; (Lusztig) the root-of-unity
order of $u_{\zeta_8}(\mathbf{H}_{\Delta_5})$. These live on three
different structures and are unified at $\mathrm{Heisdouble}(K3 \times
E)$ only under the hypothesis; this is Pattern~$273$ scope discipline
applied correctly.

**Honest scope.** The hypothesis is named, falsifiable, and assigned
the correct `\ClaimStatusConjectured` tag; the three underlying
lemmas keep their theorem status.

## Summary

One subsection title edit; one theorem environment split into two
(one theorem + one conjectural theorem) plus one hypothesis
environment; one parenthetical scope tag in the one-line summary.
All four tasks (i)--(iv) of the charge are discharged in the
concrete TeX block and the edit specification above.
