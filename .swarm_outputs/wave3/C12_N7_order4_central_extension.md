# Agent C12 — Non-CHL $N=7$ order-$4$ central extension of $\mathrm{Mp}_4$ by $\mu_4$

## Terminal state
**C (FRONTIER DECLARATION)**

The claim rests on three primary-source gaps that are not bridged by
any published theorem. Attempting to close at state B would require
naming one specific published theorem as the missing hypothesis; no
single theorem carries the weight. The mathematics is genuine
frontier: the $\mu_4$-central-extension structure, the weight-$7/4$
elliptic seed, and the Niwa-compatible $g_7 \in S_1(\Gamma_0(28),
\chi_7)$ target all require new construction, not the invocation of
an extension of published machinery.

## Statement of the frontier declaration

\begin{frontier}[Non-CHL $N=7$ order-$4$ central extension of $\mathrm{Mp}_4$ by $\mu_4$]\ClaimStatusOpen
\label{frontier:N7-mu4-central-extension}

Let $G^{(7)}$ denote the automorphic home of the would-be quarter-weight
Siegel paramodular form $\Delta_{1/4}^{(7)}$ advertised on the
simplest-divisor paramodular family at level $K(7) \subset \mathrm{Sp}_4(\mathbb{Q})$.
The non-CHL sector at $N = 7$ ($\varphi(7) = 6 \nmid 2$ excludes
Nikulin-admissibility, so no free $\mathbb{Z}/7$-quotient of $K3 \times E$
exists) would place $G^{(7)}$ as a central extension
\[
1 \;\longrightarrow\; \mu_4 \;\longrightarrow\; G^{(7)}
\;\longrightarrow\; \mathrm{Mp}_4(\mathbb{Z}) \;\longrightarrow\; 1
\]
with $\mu_4$ acting by a primitive quartic character on the paramodular
involution $V_7 \in K(7)$ and trivially elsewhere. The proposed identification
$(Z^{X_7}_{L,1})^{-1/8} \cdot \varepsilon_7(L) = \Delta_{1/4}^{(7)}$
would read the Borcherds singular-theta lift on the cover $G^{(7)}$
with multiplier $\chi_7^{\otimes 2}$ and weak-Jacobi input whose constant
Fourier coefficient $c_7(0) = 1/2$ forces $\kappa_{\mathrm{BKM}}(\Phi_7) = 1/4$.

The construction is genuine frontier: no published theorem establishes
existence of $G^{(7)}$, of the weight-$7/4$ elliptic seed
$g_7 \in M_{7/4}(\Gamma_0(7), \chi_7)$, or of a weight-$1$ Niwa preimage
$g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$. The Shimura 1975
cohomology computation $H^2(\mathrm{Sp}_4(\mathbb{Z}), \mathbb{Z}/4) \simeq
\mathbb{Z}/2$ obstructs a non-split $\mu_4$-extension of
$\mathrm{Sp}_4(\mathbb{Z})$; any $G^{(7)}$ must therefore be a further
$\mathbb{Z}/2$-extension of $\mathrm{Mp}_4$, not a $\mu_4$-extension of
$\mathrm{Sp}_4$. The additional extension class lies in
$H^2(\mathrm{Mp}_4(\mathbb{Z}), \mathbb{Z}/2)$, whose cohomology is not
computed in the literature at level $K(7)$.

\end{frontier}

## Primary-source gap

**The gap is threefold**, and each sub-gap requires a distinct primary-source
extension. Wave 2's retraction of "order-4 Cheeger-Simons gerbe" to
"order-4 central extension of $\mathrm{Mp}_4$ by $\mu_4$" changed the
framing from geometric to automorphic but did not close any of the
three underlying gaps.

### Gap 1. Existence of the seed weight-$7/4$ cusp form

**Missing**: a theorem establishing that
$\dim_{\mathbb{C}} M_{7/4}(\Gamma_0(7), \chi_7) \geq 1$ on the spin double
cover $\widetilde{\mathrm{SL}_2}(\mathbb{Z})$, producing a non-zero
Hecke eigenform $g_7$.

**Status of the asserted citation**:
Files `wave19_z2_N7_order4_gerbe.tex` (line 43) and
`wave19_z4_N578_joint_automorphic.tex` (line 109) cite "Freitag--Hermann
1985 §II.5 Tab. 7.2" for the existence of $g_7 \in M_{7/4}(\Gamma_0(7),
\chi_7)$. Freitag--Hermann 1985 *Analytische Automorphieformen* §II.5
classifies the genus-two spin double cover
$\widetilde{\mathrm{Mp}}_4 \to \mathrm{Mp}_4$ (quarter-integer
weights on the genus-2 Siegel domain $\mathbb{H}_2$); §II.5 does not
tabulate weight-$7/4$ elliptic forms on $\Gamma_0(7)$. The primary-source
citation does not bear the object.

**What would close this gap**: a construction of a non-zero
$g_7 \in M_{7/4}(\Gamma_0(7), \chi_7)$ by explicit $\eta$-product,
theta-series, or Maass lift. Candidates: a rational combination of
$\eta(\tau)^{a}\eta(7\tau)^{b}$ at $(a, b)$ with $a + b = 7/2$ (requires
both $a, b \in \tfrac{1}{2}\mathbb{Z}$, giving candidates like
$\eta(\tau)^{3/2}\eta(7\tau)^{2}$ or $\eta(\tau)^{1/2}\eta(7\tau)^3$),
but no such object appears in Yang 2004 (*Trans.\ AMS* 356)
classification of $\eta$-quotients or in the Ligozat 1975 level-$N$
tables. The object remains a candidate, not a theorem.

### Gap 2. Existence of the $\mu_4$-central extension $G^{(7)}$

**Missing**: a theorem constructing the central extension
\[
1 \longrightarrow \mu_4 \longrightarrow G^{(7)} \longrightarrow
\mathrm{Mp}_4(\mathbb{Z}) \longrightarrow 1
\]
classifying the weight-$1/4$ automorphic line bundle on
$G^{(7)} \backslash \mathbb{H}_2$.

**Shimura 1975 obstruction** (`wave15_a3_lorgat_conj1_N5_metaplectic_etingof.tex`
Cycle 2, `.swarm_outputs/wave2/A09_shimura_weil_theta_direction.md` Cycle 3):
$H^2(\mathrm{Sp}_4(\mathbb{Z}), \mathbb{Z}/4) \simeq \mathbb{Z}/2$
(Shimura 1975 *Ann. Math.* 102 Prop. 1.5); the kernel of the classical
Shimura-Weil metaplectic extension is $\mathbb{Z}/2$, not $\mathbb{Z}/4$.
A non-split $\mu_4$-central extension of $\mathrm{Sp}_4(\mathbb{Z})$ does
not exist in the Shimura-Weil framework.

**Residual candidate**: $G^{(7)}$ as a further $\mathbb{Z}/2$-extension
of $\mathrm{Mp}_4(\mathbb{Z})$. The extension class lives in
$H^2(\mathrm{Mp}_4(\mathbb{Z}), \mathbb{Z}/2)$, whose full computation
is not published; the local class at $K(7)$ would arise from the
Freitag-Hermann spin double cover
$\widetilde{\mathrm{Mp}}_4 \to \mathrm{Mp}_4$, but the compatibility
with the paramodular $V_7$-twist and the $\chi_7^{\otimes 2}$-character
has not been established.

**What would close this gap**: either
(a) an explicit cocycle computation
$c \in Z^2(\widetilde{\mathrm{Mp}}_4(\mathbb{Z}) \cap K(7), \mu_4)$
with primitive order-$4$ restriction to $\langle V_7 \rangle$, or
(b) an extension of Brylinski 1987 (*Invent.\ Math.*\ 89, on the
non-triviality of the central extension of
$\mathrm{Sp}_{2n}(\mathbb{A})$ by $\mathrm{K}_2$) to the paramodular
genus-two setting at level $K(7)$.

### Gap 3. Existence of the Niwa-preimage $g_7 \in S_1(\Gamma_0(28), \chi_7)$

**Missing**: a weight-$1$ elliptic cusp form
$g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$ whose Niwa 1974
lift produces the weight-$1/2$ vector-valued elliptic shadow that
pulls back the weight-$1/4$ paramodular form through a Gritsenko
additive theta lift.

**Correct direction**: The question posed to this agent asserts
"$g_7 \in S_1(\Gamma_0(28), \chi_7)$ provides the Niwa/Shimura-correspondence
input". Wave 2 A09 (`.swarm_outputs/wave2/A09_shimura_weil_theta_direction.md`
Cycles 1, 5) establishes that the direction is:

- Niwa 1974: $S_{k - 1/2}(\Gamma_0(4N), \chi') \to S_{2k - 1}(\Gamma_0(2N), \chi)$,
  so at $k = 1$ the input has weight $1/2$ and output weight $1$;
- Shimura 1973: $S_{k + 1/2}(\Gamma_0(4N), \chi) \to S_{2k}(\Gamma_0(N^{\mathrm{desc}}), \chi^2)$,
  direction half-integer $\to$ integer.

At $N = 7$, the candidate diagram is:
\[
\underbrace{\phi_{1/2, 7}^{\mathrm{seed}} \in J_{1/2, 7}^{\mathrm{cusp}, \mathrm{Mp}_2}}_{\text{half-int Jacobi, index 7}}
\;\xrightarrow{\;\mathrm{Grit}^{\theta}_{\mathrm{add}}\;}\;
\underbrace{\Delta_{1/2}^{(7)?}}_{\text{half-int paramodular}}
\;\xrightarrow{?}\;
\underbrace{\Delta_{1/4}^{(7)?}}_{\text{quarter-int paramodular}}
\]
with elliptic shadow
\[
\phi_{1/2, 7}^{\mathrm{seed}}(\tau, 0) \in S_{1/2}^{\mathrm{Mp}_2}(\Gamma_0(28), \chi'_7)
\;\xrightarrow{\;\mathrm{Niwa 1974}\;}\;
g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7).
\]
The left arrow is conjectural (Gritsenko--Nikulin 2002 *Amer. J. Math.* 124
constructs the additive theta lift only at indices compatible with
$\mathcal{N} = (4, 4)$ CHL, not at $N = 7$); the "$?$" arrow from
weight $1/2$ to weight $1/4$ requires the $\mu_4$-central extension of
Gap 2; the Niwa 1974 arrow requires the seed $\phi_{1/2, 7}^{\mathrm{seed}}$
to be nonzero.

**Status of $g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$**:
$\dim_{\mathbb{C}} S_1(\Gamma_0(28), \chi_7)$ at a fixed
Dirichlet character $\chi_7$ of conductor $7$ is computable via
Cohen--Oesterlé dimension formulae (Cohen--Oesterlé 1977, *LNM* 627
\S 5.1); at level $28 = 4 \cdot 7$ with $\chi_7$ the Legendre character
modulo $7$, the dimension is small but positive (the LMFDB database at
level $28.1.c.a$ contains candidates, but the present agent does not
have verified LMFDB-access to pin down which one corresponds to
the required Niwa preimage). The existence of the specific Hecke
eigenform with Niwa-image of correct level and character is not
established.

**What would close this gap**: a computation of
$\dim_{\mathbb{C}} S_{1/2}^{\mathrm{Mp}_2}(\Gamma_0(28), \chi'_7)$ on the
Kohnen plus-space at weight $1/2$, verification that the Niwa lift is
non-zero on the target spin of the spectrum, and identification of
the weight-$1$ eigenform $g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$
by Atkin-Lehner newform extraction.

## Why existing machinery is insufficient

The object requires **three simultaneous novel constructions** at the
same point of the paramodular atlas. Each of the four candidate
machineries fails:

1. **Borcherds 1998 singular-theta lift** handles integer and
   half-integer weights on $\mathrm{Sp}_4$ and $\mathrm{Mp}_4$ respectively
   (Borcherds 1998 Thm. 10.1, 13.3; Bruinier 2002 *LNM* 1780 Prop. 5.1
   for the half-integer case). It does **not** extend to quarter-integer
   weights. Freitag-Hermann 1985 §II.5 establishes the spin double cover
   $\widetilde{\mathrm{Mp}}_4 \to \mathrm{Mp}_4$ but does not produce
   weight-$1/4$ Borcherds products on $K(N)$ for any $N$.

2. **Gritsenko-Nikulin 1998 additive theta lift** produces
   integer-weight paramodular forms from Jacobi cusp forms of integer
   weight (Gritsenko-Nikulin 1998 Part II Thm. 2.1). Its half-integer
   extension (Gritsenko-Nikulin 2002 Amer. J. Math. 124) covers the
   metaplectic $\mathrm{Mp}_4$ case but not a $\mu_4$-refinement.

3. **Cheng-Duncan-Harvey 2014 umbral moonshine** (arXiv:1204.2779
   Tab. 2) catalogues CHL admissibility $\varphi(N) \mid 2$; $N = 7$ sits
   outside by $\varphi(7) = 6$. No Mathieu-twining on a Niemeier
   $A_6^4$ lattice produces the required weight-$1/4$ shadow.

4. **Gan-Takeda 2011** (Ann. Math. 173) gives generic local Langlands
   for $\mathrm{GSp}_4$ via $(\mathrm{GSp}_4, \mathrm{GO}_{\mathrm{split}})$-Howe
   duality. It does **not** extend to $\mathrm{Mp}_4$ or to non-algebraic
   central extensions $G^{(7)}$. Roberts-Schmidt 2007 (*LNM* 1918)
   classifies local representations of $\mathrm{GSp}_4(F)$ via
   paramodular newforms; the $\mu_4$-refinement at level $K(7)$ would
   require a metaplectic extension of Roberts-Schmidt at the paramodular
   non-split torus, which is not in the published literature.

The "$\mu_4$-central extension" Wave 2 framing relocates the object from
geometry (a Cheeger-Simons gerbe on $X_7$) to automorphic forms
(an extension of $\mathrm{Mp}_4$); the three gaps above survive the
relocation. The Wave 2 refinement (`platonic_synthesis_wave2_refinement.tex`
line 846--856) itself places this item at **Tier III — loose (new machinery
required)**, consistent with the present closure at state C.

## Cross-consistency notes

### Spine consistency (Wave 1 `platonic_synthesis_post_adversarial.tex` line 583--593, 1333--1334)

The Wave 1 spine already records the retraction at line 591--593:

> "The '$1/4$' at $N = 7$ is a classification index of an order-$4$
> *central extension* of $\mathrm{Mp}_4$ by $\mu_4$, not a
> Chern-Simons gerbe class."

and the residual-frontier list at line 1333--1334:

> "Non-CHL $N = 7$: order-$4$ central extension of $\mathrm{Mp}_4$ by
> $\mu_4$ (not a Chern-Simons gerbe), open."

The present closure agrees with this "open" status and sharpens the
primary-source gap into three sub-gaps (Gaps 1, 2, 3 above) with
explicit remedies.

### Refinement consistency (Wave 2 `platonic_synthesis_wave2_refinement.tex` line 846--856)

The Wave 2 three-tier frontier stratification places the item at
**Tier III — loose (new machinery required)**. The present closure
agrees with Tier III and supplies the explicit primary-source gap
formulation as a State-C frontier declaration.

### Wave 2 A09 consistency (`.swarm_outputs/wave2/A09_shimura_weil_theta_direction.md`)

A09 Cycle 5 corrects the Shimura 1973 direction; the present closure
inherits A09's diagram (Niwa 1974 at input, Gritsenko additive at
output) and names all three sub-gaps — seed existence, $\mu_4$-extension
existence, Niwa-preimage existence — as unresolved. A09's statement at
line 526--534 about the $\mu_4$-extension (contingent on
$H^2(\mathrm{Mp}_4(\mathbb{A}), \mu_4) \supset \mathrm{Hom}(\{\pm 1\}, \mu_4)$)
is not a theorem; it is the structural-class location at which
the extension would live if constructed. The present closure treats this
as a frontier-gap location, not a surviving theorem.

### Gritsenko-Cléry 2008 atlas consistency

The actual Gritsenko-Cléry 2008 table (`wave13_a15_mathieu_conj1_segal.tex`
line 160--175, reading arXiv:0812.3962 Theorem 1.1) has 8 forms at
$(t, N) \in \{1,2,3,4\} \times \{1,2,3,4\}$ with weights
$(5, 2, 3, 1, 2, 1/2, 3/2, 1)$ — the sequence
$\{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$ attributed in `wave15_a12_half_integer_GC_witten.tex`,
`wave19_p5_synthesis_8_forms.tex`, and `wave19_z4_N578_joint_automorphic.tex`
re-indexes the atlas by a different variable $N \in \{1, \ldots, 8\}$
(Nikulin-Mukai K3 automorphism order), which does not match the
paramodular $(t, N_\Gamma)$ parameters of the primary Gritsenko-Cléry
atlas. The "$N = 7$" label therefore names a K3-automorphism-order
slot to which no Gritsenko-Cléry form is assigned in the primary source;
the would-be $\Delta_{1/4}^{(7)}$ is an object whose existence is
conjectural at the automorphic level.

### CoHA treatise consistency (`CoHA_to_W_infty_treatise.tex`)

Not directly relevant: the CoHA / $W_\infty$ triality on
$\mathbb{C}^3$ / resolved conifold / $K3 \times E$ concerns the CHL
slice $N \in \{1, 2, 3, 4, 6\}$. No conflict with the present frontier
declaration.

### CLAUDE.md invariants

The frontier declaration observes:
- Subscript discipline: $\kappa_{\mathrm{BKM}}$ is identified at its
  native scope as the Borcherds singular-theta weight; $\kappa_{\mathrm{ch}}$
  is undefined at $N = 7$ (no compact CY$_3$ host) and the CY-to-chiral
  functor $\Phi$ does not reach the non-CHL sector.
- Lane discipline: the frontier is chain-level automorphic; no
  $(\infty,1)$-categorical lane applies because the source category
  (compact CY$_3$) is absent at $N = 7$.
- Primary sources: all cited works carry volume/year/theorem numbers;
  the Freitag-Hermann 1985 §II.5 misattribution in wave19 files is flagged.

## Inscription-ready TeX block

```latex
\begin{frontier}[Non-CHL $N = 7$ order-$4$ central extension of
$\mathrm{Mp}_4$ by $\mu_4$]
\label{frontier:N7-mu4-central-extension}
\ClaimStatusOpen

The non-CHL entry at $N = 7$ places the would-be quarter-weight
paramodular form $\Delta_{1/4}^{(7)}$ on a conjectural order-$4$ central
extension
\[
1 \;\longrightarrow\; \mu_4 \;\longrightarrow\; G^{(7)}
\;\longrightarrow\; \mathrm{Mp}_4(\mathbb{Z}) \;\longrightarrow\; 1
\]
with $\mu_4$ acting primitively on the paramodular involution $V_7 \in K(7)$.
Three primary-source gaps separate this frontier from closure.

\emph{Gap 1 (automorphic seed).} Existence of a non-zero
$g_7 \in M_{7/4}(\Gamma_0(7), \chi_7)$ on the spin double cover of
$\Gamma_0(7)$ is not established; the Freitag--Hermann 1985
\emph{Analytische Automorphieformen} \S II.5 reference cited at
internal Wave-19 notes concerns the genus-two spin double cover
$\widetilde{\mathrm{Mp}}_4 \to \mathrm{Mp}_4$, not weight-$7/4$
elliptic forms on $\Gamma_0(7)$.

\emph{Gap 2 (group extension).} Shimura $1975$ (\emph{Ann.\ Math.}\ $102$
Prop.~$1.5$) computes $H^2(\mathrm{Sp}_4(\mathbb{Z}), \mathbb{Z}/4)
\simeq \mathbb{Z}/2$; no non-split $\mu_4$-central extension of
$\mathrm{Sp}_4(\mathbb{Z})$ exists in the Shimura-Weil framework.
The residual possibility, a further $\mathbb{Z}/2$-extension of
$\mathrm{Mp}_4(\mathbb{Z})$ classified by
$H^2(\mathrm{Mp}_4(\mathbb{Z}), \mathbb{Z}/2)$ at level $K(7)$, would
require an extension of Brylinski $1987$ (\emph{Invent.\ Math.}\ $89$,
central extensions of $\mathrm{Sp}_{2n}(\mathbb{A})$ by $\mathrm{K}_2$)
to paramodular genus-two at level $K(7)$; such an extension is not in
the published literature.

\emph{Gap 3 (Niwa preimage).} The weight-$1$ elliptic cusp form
$g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$ whose Niwa $1974$
(\emph{Nagoya Math.\ J.}\ $56$) lift produces the half-integer elliptic
shadow of the Gritsenko-Nikulin $2002$ additive theta seed of
$\Delta_{1/4}^{(7)}$ is conjectural; its Hecke-eigensystem identification
is not verified in the published literature.

The universal Borcherds-weight identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ of Theorem~\ref{prop:bkm-weight-universal}
extends to the non-CHL sector $N \in \{5, 7, 8\}$ under the Borcherds
singular-theta weight reading \emph{only} conditional on closure of
Gaps~$1$--$3$. At CHL-admissible $N \in \{1, 2, 3, 4, 6\}$, the identity
is a theorem via Gritsenko-Nikulin $1998$ Part~II Thm.~$2.1$ and
Borcherds $1998$ Thm.~$13.3$.

\emph{Primary sources.}
Borcherds $1998$ \emph{Invent.\ Math.}\ $132$ Thm.~$13.3$;
Shimura $1975$ \emph{Ann.\ Math.}\ $102$ Prop.~$1.5$;
Freitag-Hermann $1985$ \emph{Analytische Automorphieformen} \S II.5;
Bruinier $2002$ \emph{LNM}\ $1780$ Prop.~$5.1$;
Gritsenko-Nikulin $2002$ \emph{Amer.\ J.\ Math.}\ $124$;
Niwa $1974$ \emph{Nagoya Math.\ J.}\ $56$;
Brylinski $1987$ \emph{Invent.\ Math.}\ $89$;
Gan-Takeda $2011$ \emph{Ann.\ Math.}\ $173$;
Roberts-Schmidt $2007$ \emph{LNM}\ $1918$.

\end{frontier}
```

## What would convert state C to state B

A closure at conditional state B would require a single primary-source
hypothesis that subsumes Gaps 1--3 simultaneously. Candidate hypotheses:

- **(H1)** *Gritsenko-Clery 2018 extension to $(t, N) = (7, 1)$ paramodular.*
  The Gritsenko-Cléry 2008 atlas is extended to paramodular levels
  $K(t)$ at $t \geq 5$ with an eighth row at $(t, N_\Gamma) = (7, 1)$
  of weight $1/4$ and character $\nu^8$. Under H1, Gap 1 closes via the
  constructed Jacobi seed and Gap 2 closes via the atlas-prescribed
  cover, but Gap 3 (Niwa preimage $g_7^{\mathrm{Niwa}}$) remains open.

- **(H2)** *Extension of Brylinski 1987 to paramodular $K(7)$.*
  The central extensions of $\mathrm{Sp}_{2n}(\mathbb{A})$ by
  $\mathrm{K}_2$ are extended to the paramodular non-split torus at
  level $K(7)$, producing an explicit cocycle for $G^{(7)}$. Under H2,
  Gap 2 closes, but Gaps 1 and 3 remain open.

- **(H3)** *Explicit LMFDB / Sage computation of $\dim S_1(\Gamma_0(28),
  \chi_7)$ and identification of $g_7^{\mathrm{Niwa}}$.*
  A computer algebra computation identifies the Atkin-Lehner newform
  $g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28), \chi_7)$, verifies
  non-vanishing of its Niwa-lift to $S_{1/2}^{\mathrm{Mp}_2}(\Gamma_0(28),
  \chi'_7)$, and confirms Hecke eigenvalue agreement with a candidate
  Arthur parameter. Under H3, Gap 3 closes, but Gaps 1 and 2 remain open.

None of H1, H2, H3 alone closes all three gaps; the item requires all
three in combination, so no single-hypothesis state-B closure is currently
available. State C is the accurate reading.
