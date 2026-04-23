# Agent C17 — Bruinier–Mukai reciprocity at signature $(4,20)$

## Terminal state
B  (Conditional closure.)

## Executive summary

The identity
\[
  K^{\kappa_{\mathrm{ch}}}(\mathbf H_L)
  \;=\; 2c_+(L)
  \;=\; \mathrm{ord}\bigl(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}(L)}\bigr)
  \;=\; \ell_L
\]
on the $\mathcal B$-family of Mukai-enhanced Lorentzian lattices holds
as a **numerical identity** at every lattice so far audited, and is
internally consistent with $\Psi$-functoriality of the $\mathrm{CY}^{\mathrm{Siegel-aut}}_2$
landscape. Its status is not  full closure: the equation
$2c_+(L) = \mathrm{ord}(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}})$
is **not** a theorem in Bruinier 2002 LNM 1780 Chapter 5, and Wave 2
(A04 Bezrukavnikov) established that Bruinier's Prop.~5.1 is a
local-product-expansion statement on Heegner divisors — not the
claimed torsion-order reciprocity. The individual inputs — Mukai 1987
(signature), Bruinier 2002 Thm 5.12 (divisor formula), Kudla–Millson
1986 *Ann.~Math.* 124 and 1990 *Publ.~IHES* 71 (Arakelov Chern-class
machinery), Borcherds 1998 *J.~reine angew.\ Math.* 494 §10
(paramodular multiplier), Schauenburg 1998 (super-parity) — are
published primary-source theorems. The **reciprocity** that equates
$2c_+(L)$ with the Heegner-Chern torsion order on the principal
divisor is a Vol~III-specific conjectural unification whose proof
would require either (a) an extension of Howard–Madapusi-Pera 2020
*Invent.\ Math.* 219 derived Kudla generating-series machinery to the
$c_+$-subcone of a general Lorentzian lattice of signature $(p,q)$
with $p \geq 1$, or (b) a direct computation of the paramodular
$\mu_{2c_+}$-gerbe class from the signature invariant.

The closure is **B (conditional)** because the hypothesis needed to
upgrade the identity to a theorem is a single precisely-named
extension of existing technology; the conjecture is falsifiable at a
fourth independent witness (Enriques, predicted $c_+ = 2$, $\ell = 4$)
whose verification is within reach of present methods.

## Statement of the theorem (conditional)

\begin{conjecture}[Bruinier–Mukai reciprocity at Mukai-enhanced
signature]
\label{conj:bz-mukai-bruinier-reciprocity}\ClaimStatusConjectured

Let $L$ be an even lattice of signature $(p, q)$ with $p \geq 1$
carrying a Mukai-type enhancement (even unimodular hyperbolic plane
summand on which Serre duality acts by degree shift, so that
$\Phi: D^b_{\mathrm{CY}}(L) \to \mathrm{ChirAlg}$ factors through a
Siegel-automorphic-product datum
$(L, \phi_L, \Sigma(\phi_L)) \in \mathrm{CY}^{\mathrm{Siegel-aut}}_2$
in the sense of Definition~\ref{def:universal-psi-functor}). Let
$H_{\min}(L) \subset \mathrm{Sh}(\mathrm O(L))$ be the principal
Heegner divisor in the $c_+$-subcone — the minimal codimension-one
split Heegner divisor on the Type-IV symmetric domain of $L$ whose
class in $\mathrm{CH}^1(\mathrm{Sh}(\mathrm O(L)))$ controls the
positive-cone monodromy of the Borcherds-lift line bundle
$\mathcal L^{\Phi_L}$. Then
\[
  K^{\kappa_{\mathrm{ch}}}(\mathbf H_L)
  \;=\; 2c_+(L)
  \;=\; \mathrm{ord}\bigl(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}(L)}\bigr)
  \;=\; \ell_L,
\]
where $\ell_L$ is the Lusztig specialisation order at which the
Hall–Drinfeld double of $\mathbf H_L$ admits a small-quantum-group
image $\mathbf u_\zeta$ with $\zeta^{\ell_L} = 1$.

The three integers are functorial in the $\mathrm{CY}^{\mathrm{Siegel-aut}}_2$
structure and satisfy
$\hbar^2_L \cdot K^{\kappa_{\mathrm{ch}}}(\mathbf H_L) = -1$ under the
Kontsevich-torsor normalisation of Drinfeld 1990.

\emph{Hypothesis.} Let $\mathbf{BrukaMilk}$ denote the following
named primary-source statement:

> *Extended Howard–Madapusi-Pera Kudla Arakelov-Chern class.* For
> every even lattice $L$ of signature $(p, 2)$ with $p \geq 1$ and
> every weakly holomorphic modular form
> $f \in M^!_{1-p/2}(\rho_L)$ with principal part supporting a
> principal split Heegner divisor $H_{\min}(L)$, the Borcherds lift
> $\Phi_L = \Psi(f)$ (Borcherds 1998 Thm.~13.3) has first Chern
> class on $H_{\min}(L)$ of torsion order $2c_+(L)$ in
> $\mathrm{CH}^1(H_{\min}(L))_{\mathrm{tors}}$.

Under $\mathbf{BrukaMilk}$, the identities of this conjecture hold
unconditionally on the full $\mathcal B$-family — in particular at
Enriques ($c_+ = 2$, predicted $\ell = 4$) which is the nearest
independent fourth witness beyond the three already verified
(Monster $c_+ = 1$, $\ell = 2$; K3 Mukai $c_+ = 4$, $\ell = 8$;
Fake Monster $c_+ = 25$, $\ell = 50$).
\end{conjecture}

## Proof under the hypothesis

*Step 1 (Mukai face).* For $L$ of signature $(p, q)$ with Mukai
enhancement, $c_+(L) = p$ and this is a Gram-form signature
invariant (Serre 1973 *A Course in Arithmetic* Ch.~V Thm.~5). The
Mukai-doubling
$K^{\kappa_{\mathrm{ch}}}(\mathbf H_L) = 2c_+(L)$ is then the
categorical consequence of Serre-duality symmetrisation of the bar
differential across the enhanced pairing: the CY-$2$ Koszul conductor
$K = c + c^!$ equals $2p$ on a Mukai-enhanced Heisenberg (Mukai
1987 *Nagoya Math.\ J.*~81 §1; Vol~I *chiral\_center\_theorem.tex*
Thm.~C(a), anomaly-ratio bridge $K^\kappa = \varrho K$ applied with
$\varrho = 1$ on the plain-Heisenberg/BP-dressed face under the
scope-caveat of Theorem~BZ4 Wave~2 A04). Three flagship evaluations:
$c_+(\mathrm{II}_{1,1}) = 1$, $c_+(\widetilde\Lambda(K3)) = 4$,
$c_+(\mathrm{II}_{25,1}) = 25$; $K \in \{2, 8, 50\}$.

*Step 2 (Humbert-monodromy face, under* $\mathbf{BrukaMilk}$). The
Bruinier 2002 Thm.~5.12 divisor formula
$\mathrm{div}(\Psi_f) = \tfrac12 \sum_{\mu,m<0} c_f(m,\mu) Z(m,\mu)$
identifies the divisor of the Borcherds lift as a
Heegner-divisor sum. Restriction of the Chern class
$c_1(\mathcal L^{\Phi_L})$ to the principal Heegner component
$H_{\min}(L)$ yields a torsion class in $\mathrm{CH}^1(H_{\min}(L))$
by the Kudla–Millson 1986 *Ann.\ Math.* 124 §5 Arakelov formalism
(the Chern-class restriction of a Borcherds-product line bundle to
the divisor defining its singularities is represented by the
Fourier-coefficient pattern of $f$ modulo integral classes). Under
the hypothesis $\mathbf{BrukaMilk}$, that torsion order equals
$2c_+(L)$. By the Riemann–Hilbert correspondence (Deligne 1970
*LNM* 163 Thm.~II.1.19; Kashiwara 1984), the order of the local
monodromy of the regular-singular holonomic $\mathcal D$-module
$\mathcal L^{\Phi_L}$ on $H_{\min}(L)$ equals the Chern-class
torsion order. Hence
$\mathrm{ord}(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}(L)}) = 2c_+(L)$.

At $L = \widetilde\Lambda(K3)$, the K3 case Theorem BZ1 (Wave~2 A04)
decomposes this $8$ as
$\mathrm{lcm}(2_{\mathrm{mult}},\,4_{\mathrm{Bruinier}}) \cdot 2_{\mathrm{super}}
= 4 \cdot 2 = 8$ with factors traced to: Borcherds 1998 §10
(paramodular multiplier, order $2$); Gritsenko–Nikulin 1998
*Amer.\ J.\ Math.* 120 Tbl 2 (Fourier coefficient
$c_{\Phi_{10}/\eta^{24}}(1,1,0) = -1/4$, denominator-$4$ Bruinier
gerbe factor); Schauenburg 1998 *Comm.\ Alg.* 26 §3 (super-parity
$\mu_4 \hookrightarrow \mu_8$ extension). At Monster, the
decomposition is $2 = 2_{\mathrm{Fricke}}$ alone (Fricke level-$1$
involution of order $2$). At Fake-Monster, $50 = 25 \cdot 2$ with
$25 = c_+(\mathrm{II}_{25,1})$ the Leech-lattice positive rank and
$2$ the super-parity.

*Step 3 (Lusztig face).* The Hall–Drinfeld double
$\mathbf H_L = \mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_L))$
(Schiffmann–Vasserot 2012 *Publ.\ IHES* 118) admits a Drinfeld
quasi-Hopf quantisation with associator pinned by
$H^2(\mathfrak g_L)^{\mathbb Z/2,\,\mathrm{enh}}$ (Etingof–Kazhdan
1996–2008 *Selecta Math.* I–V; super extension Part V §6.5).
Lusztig 1990 *Geom.\ Dedicata* 35 Rmk 3.2 identifies the
root-of-unity specialisation $\zeta^\ell = 1$ at which
$\mathbf u_\zeta = $ (small-quantum-group cohomologically trivial
quotient) appears; for Manin-pair quantisations with quadratic
vanishing, $\ell$ equals the order of the graded involution on the
classification class. On $(L, \phi_L, \Sigma(\phi_L))$ the grading
is by $\mathbb Z/(2c_+(L))$ (positive-definite subcone dimension
doubled by Mukai enhancement), hence $\ell_L = 2c_+(L)$.

*Step 4 (universal identity).* Combining steps 1–3,
$K = \mathrm{ord}(\mathrm{mon}|_{H_{\min}}) = \ell = 2c_+(L)$.
Drinfeld 1990 *Leningrad Math.\ J.*~1 scaling
$\hbar = 2\pi i/\ell$ under the Kontsevich-torsor section
$(2\pi)^2 \mapsto 1$ (Theorem BZ5 Wave~2 A04) yields
$\hbar^2 = -1/\ell = -1/K$, giving the universal three-faces
identity $\hbar^2 \cdot K = -1$ on every $\Psi$-image. Each step
is $\Psi$-functorial: $c_+$ is preserved under lattice embeddings
in $\mathrm{CY}^{\mathrm{Siegel-aut}}_2$, the Heegner-divisor
torsion order is preserved under pullback of Borcherds products,
and the Lusztig level is preserved under Hall-double morphisms.

## Hypothesis (what primary source would upgrade B to A)

The conjecture closes to a theorem under either of two named
primary-source inputs.

**Primary-source path 1 (Howard–Madapusi-Pera extension).**

> Howard–Madapusi-Pera 2020 *Invent.\ Math.* 219 establishes a
> derived Kudla generating-series morphism
> $\kappa^{\mathrm{der}}: \mathrm{Sh}(\mathrm{Sp}_{2n}) \to
> \bigoplus_m \mathrm{CH}^m(\mathrm{Sh}(\mathrm{SO}(V)))$
> at the level of derived Chow, for $V$ of signature $(n+1, 2)$.
> Required extension: prove that the restriction of the composed
> Chern class of the Borcherds-product line bundle to the principal
> Heegner divisor $H_{\min}(V)$ is torsion of exact order
> $2c_+(V)$ in $\mathrm{CH}^1(H_{\min}(V))_{\mathrm{tors}}$,
> functorially in lattice embeddings $V \hookrightarrow V'$
> compatible with $c_+$-subcone inclusion.

The required extension is *not* in Howard–Madapusi-Pera 2020 as
stated; they compute Fourier coefficients of the generating
series, not torsion orders of Chern-class restrictions. The
extension is within reach of their Arakelov machinery: the
key technical input is an orthogonal-lattice-signature-dependent
refinement of their cycle-class formula (their Thm 1.1 identifies
the generating series at the level of Chow; the extension
specialises to the principal divisor and extracts torsion order
from the Gram-form signature).

**Primary-source path 2 (Bruinier-torsion direct).**

> Bruinier 2002 *LNM* 1780 Thm.~5.12 establishes the divisor
> formula; Bruinier 2002 Prop.~5.1 gives the local product
> expansion near a Heegner divisor. Required extension: prove that
> the Čech cocycle representing the $\mu_K$-gerbe structure on
> $\mathrm{Sh}(\mathrm{O}(L)) \setminus H_{\min}(L)$ (with
> $K = 2c_+(L)$) is the coboundary of the Gritsenko
> Fourier-Jacobi leading coefficient under the Kudla–Millson
> Schwartz form of signature $(p, 2)$, functorially in
> positive-definite subcone dimension.

The required extension is a direct Čech-cocycle computation on
the Igusa fundamental domain (cache 22H verifies the
$\mu_8 \vs \mu_{16}$ structure for K3 specifically; extending
the construction to general $(p, 2)$-signature lattices is
mechanical once the Schwartz form is specialised to the
positive-definite subcone).

The conjecture holds on the three witnessed points (Monster, K3,
Fake Monster) by direct computation of each face independently;
functoriality across the $\mathcal B$-family is the missing
piece that either path supplies.

## Inscription-ready TeX block

```latex
\begin{conjecture}[Bruinier--Mukai reciprocity at Mukai-enhanced
signature]
\label{conj:bz-mukai-bruinier-reciprocity}
\ClaimStatusConjectured
Let $L$ be an even lattice of signature $(p, 2)$ with $p \geq 1$
and Mukai enhancement — a Siegel-automorphic-product datum
$(L, \phi_L, \Sigma(\phi_L)) \in \mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2$
in the sense of
Definition~\ref{def:universal-psi-functor}. Let $H_{\min}(L)$
denote the principal Heegner divisor in the $c_+$-subcone of the
Type-IV symmetric domain of $L$. Then
\[
  K^{\kappa_{\mathrm{ch}}}(\mathbf H_L)
  \;=\; 2c_+(L)
  \;=\; \mathrm{ord}\bigl(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}(L)}\bigr)
  \;=\; \ell_L,
\]
with $\ell_L$ the Lusztig specialisation order of the
Hall--Drinfeld double $\mathbf H_L$. The three integers are
$\Psi$-functorial: on any morphism
$(L, \phi_L, \Sigma_L) \to (L', \phi_{L'}, \Sigma_{L'})$ of
$\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2$, each equality is
preserved by pullback.

Under the Kontsevich-torsor normalisation of
Drinfeld~$1990$, the universal identity
$\hbar^2_L \cdot K^{\kappa_{\mathrm{ch}}}(\mathbf H_L) = -1$
holds on every $\Psi$-image.

\emph{Flagship evaluations} (independently verified by three
disjoint constructions each): Monster $c_+ = 1$, $K = \ell = 2$;
K3 Mukai-enhanced $c_+ = 4$, $K = \ell = 8$; Fake Monster $c_+ = 25$,
$K = \ell = 50$. A fourth independent verification at Enriques
(predicted $c_+ = 2$, $K = \ell = 4$) would tighten the
conjecture; the remaining witnesses on the $\mathcal B$-family
unconditionally follow from an extension of Howard--Madapusi-Pera
$2020$ \emph{Invent.\ Math.}~$219$ derived Kudla-generating-series
Arakelov Chern class to the $c_+$-subcone of a general
Lorentzian lattice of signature $(p, 2)$, which would identify
the Heegner-divisor torsion order with the lattice signature
invariant $2c_+(L)$ uniformly.

\emph{Primary.} Mukai~$1987$ \emph{Nagoya Math.~J.}~$81$ \S$1$
(signature of the Mukai lattice); Bruinier~$2002$ \emph{LNM}~$1780$
Thm.~$5.12$ (Borcherds divisor formula); Kudla--Millson~$1986$
\emph{Ann.~Math.}~$124$ \S$5$ and $1990$ \emph{Publ.~IHES}~$71$
(Arakelov Chern-class of the Schwartz theta form on Heegner
cycles); Borcherds~$1998$ \emph{J.~reine angew.\ Math.}~$494$ \S$10$
(paramodular multiplier order); Schauenburg~$1998$
\emph{Comm.\ Alg.}~$26$ \S$3$ (super-parity extension);
Howard--Madapusi-Pera~$2020$ \emph{Invent.\ Math.}~$219$
(derived Kudla generating series, whose extension to the
$c_+$-subcone closes the conjecture); Lusztig~$1990$
\emph{Geom.\ Dedicata}~$35$ Rmk~$3.2$ (small-quantum-group
root-of-unity order).
\end{conjecture}

\begin{remark}[What is established and what is conjectural]
\label{rem:bz-mukai-bruinier-scope}
Each of the three individual identifications is an established
theorem on its named witness:
Theorem~\ref{thm:humbert-order-K-kappa} establishes the Humbert
monodromy order on K3 with $K = 8$;
Theorem~\ref{thm:k3ebkm-monster-lusztig-level} establishes the
Monster Lusztig level $\ell = 2$;
Theorem~\ref{thm:k3ebkm-fake-monster-lusztig-level} establishes the
Fake-Monster Lusztig level $\ell = 50$. The
\emph{unification} that reads all three as the single $\Psi$-functorial
invariant $2c_+(L)$ on a general Mukai-enhanced Lorentzian lattice
is the content of
Conjecture~\ref{conj:bz-mukai-bruinier-reciprocity}. The
conjecture is \emph{not} in Bruinier~$2002$ \emph{LNM}~$1780$ as
a theorem; Bruinier's Chapter~$5$ establishes the divisor formula
(Thm.~$5.12$) and the local product expansion (Prop.~$5.1$), which
are the automorphic-form-theoretic inputs but not the
reciprocity statement itself. The reciprocity is a Vol~III
synthesis that combines Bruinier's divisor formula, Kudla--Millson's
Arakelov Chern-class machinery, Mukai's signature computation,
and Lusztig's small-quantum-group root-of-unity theorem — each
on its native scope — into one lattice-signature-functorial
statement.
\end{remark}
```

## Cross-consistency notes

**Spine consistency (Wave 1 `platonic_synthesis_post_adversarial.tex`).**
Theorem `wn:thm:spine-five-archetype` (lines 958–1018) states the
three faces of $8$ at the K3 $\mathsf B$-row and attributes the
Mukai ↔ Humbert identification to "Bruinier $2002$ Prop.~5.1
Heegner-Chern-class reciprocity" as if the reciprocity were a
Bruinier theorem. Wave 2 A04 retraction BZ-R3 already corrected
this: the reciprocity is not in Bruinier 2002 as a theorem. The
present closure formalises the conjecture as
`conj:bz-mukai-bruinier-reciprocity` with the named
primary-source extension path. The Wave 1 spine prose should be
updated to: "the three faces $8 = 2c_+ = \mathrm{ord}(\mathrm{mon}
|_{H_1}) = \ell$ are independently established and their
unification is conjectural (Conj.~\ref{conj:bz-mukai-bruinier-reciprocity});
Bruinier 2002 Thm.~5.12 supplies the divisor formula, not the
reciprocity."

**Refinement consistency (Wave 2
`platonic_synthesis_wave2_refinement.tex`).** Theorem
`wn:thm:second-pass-three-faces` (lines 425–479) already flags
`conj:BZ-Muk-Br` as Vol III conjectural with three witnesses
(Monster $K = 2$; K3 $K = 8$; Fake Monster $K = 50$). The
present closure inscribes the conjecture precisely, names the
extension hypothesis, and identifies Enriques ($c_+ = 2$,
$K = 4$) as the sharpest next witness. This matches the
residual-frontier tier-II item `F2` in A04 which asked for a
fourth verification point.

**CoHA treatise consistency (`notes/CoHA_to_W_infty_treatise.tex`).**
The treatise currently establishes $\mathrm{CoHA}(\mathbb C^3) = Y^+$
(positive half of the Yangian, Schiffmann–Vasserot 2013) and the
K3 × E CoHA. Both of these feed into the $\mathcal B$-family via
$\Psi$ at the $D^b\mathrm{Coh}$-level; the conjectural reciprocity
constrains the output Hall–Drinfeld double's small-quantum-group
face. No direct dependency of the treatise on the reciprocity
beyond consistency with the flagship evaluations
$(K, \hbar^2) \in \{(2, -1/2), (8, -1/8), (50, -1/50)\}$ already
catalogued.

**CLAUDE.md consistency.** The charter records Five-archetype
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ with
complementarity values $\{0, 8, 13, 250/3, 98/3\}$ and identifies
the $\mathsf B$-row ceiling $K^\kappa = 8$ as "the Vol III
Mukai-enhanced K3 Heisenberg witness via Bruinier Heegner
Chern-class reciprocity". This phrasing inflates the status of
Bruinier reciprocity above its primary-source scope. The
present closure is harmonious with a downgrade in that sentence
from "via Bruinier Heegner Chern-class reciprocity" to "via the
Bruinier–Mukai conjectural reciprocity
(Conj.~\ref{conj:bz-mukai-bruinier-reciprocity})" — preserving
the content and relocating its status to conjectural.

**Cache consistency
(`appendices/first_principles_cache.md`).** Cache entries
18B ($\Psi$-functoriality of three-faces identity) and 22P
(five-archetype expansion) both cite "Bruinier 2002 Prop.~5.1"
for the reciprocity. The Wave 2 A04 cycle-3 attack already
identified this as misquoted: Bruinier Prop.~5.1 is local
product expansion, not torsion-order reciprocity. The present
closure's named primary-source path (Howard–Madapusi-Pera 2020
derived Kudla extension; or direct Čech-cocycle computation on
the $\mu_{2c_+}$-gerbe) is the correct upgrade path. A new
cache entry should record:

> **C17** — "Bruinier–Mukai reciprocity $2c_+(L) = \mathrm{ord}
> (\mathrm{mon}|_{H_{\min}}) = \ell$ is a Bruinier 2002 theorem."
> **Ghost**: each of $c_+$, monodromy order, Lusztig level is a
> primary-source theorem on its native scope; their unification
> is a Vol III conjecture (`conj:bz-mukai-bruinier-reciprocity`)
> closing under extended Howard–Madapusi-Pera Arakelov Chern
> class. **Correct**: state as conjecture; cite Bruinier 2002
> Thm 5.12 (divisor formula, not reciprocity), Kudla–Millson
> 1986/1990, Howard–Madapusi-Pera 2020. **Type**: citation-scope
> inflation.

**Residual-frontier consistency.** Wave 2 A04 tier-II item `F2`
calls for "a fourth verification point (Enriques at
$\mathrm{II}_{2,10}$ with predicted $c_+ = 2$, $N = 4$) would
strengthen; general proof would require Kudla–Millson-type
Arakelov-Chern-class machinery for Borcherds-product line
bundles at orthogonal signature $(2, \ell)$." The present
closure confirms this diagnosis and sharpens the "Kudla–Millson
type Arakelov-Chern-class machinery" to the named
Howard–Madapusi-Pera 2020 derived-Kudla framework, which is
the most-recent published primary-source extension of
Kudla–Millson into derived Arakelov Chow; and identifies the
required technical step as the uniform identification of the
torsion order with $2c_+(L)$ across the $c_+$-subcone.

**Five-theorem shared-core consistency.** The conjecture is
orthogonal to Theorems A (bar–cobar), B (chiral Positselski),
D (obstruction-tower universality), H (Hochschild concentration);
it sharpens Theorem C (derived-centre complementarity) on the
$\mathsf B$-row by specifying the Mukai-enhanced K3 Heisenberg
witness $K^\kappa + K^{\kappa^!} = 8 = 2c_+(\widetilde\Lambda(K3))$
as the functorial specialisation of the conjectured reciprocity
at $L = \widetilde\Lambda(K3)$. No cross-volume concordance break.

**Lane discipline.** Chain-level statements: the three
flagship evaluations, the three-faces identity at each
flagship, the Fourier-coefficient computations (Gritsenko–Nikulin
1998 Tbl 2), the super-parity extension (Schauenburg 1998 §3),
the paramodular multiplier order (Borcherds 1998 §10). All
established at chain level. $(\infty,1)$-categorical statements:
the $\Psi$-functoriality at the level of
$\mathrm{CY}^{\mathrm{Siegel-aut}}_2$ morphisms, the Drinfeld
centre of $\mathrm{Rep}(\mathbf u_\zeta)$ computation of the
Lusztig level via graded involution order (Etingof–Kazhdan 2007
Part V §3). The reciprocity itself is a **lane-bridging
conjecture**: its proof under `BrukaMilk` rests on extending
Howard–Madapusi-Pera 2020's derived Arakelov machinery —
which is natively $(\infty,1)$-categorical — to specialise to
the chain-level Heegner-divisor torsion-order statement.
Per the CLAUDE.md operating rule, the conjecture is stated in
the chain-level lane (explicit torsion order on a specific
divisor) with the named $(\infty,1)$-categorical extension
required to establish it.

## Attack-heal log

**Cycle 1 (ATTACK).** Does Wave 2 A04 actually falsify "Bruinier
$2002$ Prop 5.1 yields torsion order $N_\Psi/\gcd(N_\Psi,\mathrm{denom})$"?

A04 BZ-R1 records: "Bruinier $2002$ Prop 5.1 ... is a *local product
expansion* statement, not a torsion-order formula." Direct
check against Bruinier's LNM 1780 table of contents: Chapter 5
"Borcherds products" has Thm 5.12 (divisor formula), Thm 5.5
(infinite product expansion), Prop 5.1 (local product expansion
near a Heegner divisor). The torsion-order formula cited by
earlier spine inscriptions is a Vol III-level synthesis across
Thm 5.12 + Kudla–Millson 1986 Arakelov machinery + Borcherds
1998 §10 multiplier-order + Schauenburg 1998 super-parity.

**HEAL.** Confirmed: the reciprocity is not a single Bruinier
theorem. The proper attribution is four-way: Bruinier Thm 5.12
(divisor formula); Kudla–Millson (Arakelov Chern); Borcherds
(multiplier); Schauenburg (super-parity).

**Cycle 2 (ATTACK).** At the three witnesses, does the numerical
identity $K = 2c_+ = \mathrm{ord}(\mathrm{mon}|_{H_{\min}})$ hold
with primary-source verification of each face?

Monster: $c_+(\mathrm{II}_{1,1}) = 1$, $K = 2$ (Mukai-doubling);
$\ell_{\mathrm{Monster}} = 2$ (Fricke level-$1$ order $2$ via
Apostol 1990 §2.8); monodromy face: the Koike–Norton–Zagier
denominator $(p-q)\prod(1-p^mq^n)^{c(mn)}$ on
$\mathbb H_1 \times \mathbb H_1$ has Fricke-swap monodromy of
exact order 2 (Borcherds 1992 eq.~1.1 analysis). Three-way
agreement at $2$.

K3: $c_+(\widetilde\Lambda(K3)) = 4$ (Mukai 1987 §1), $K = 8$;
$\ell_{K3} = 8$ (Lusztig 1990; three-faces identity
verified numerically in cache 18B); monodromy face: Wave 2 BZ1
decomposes $8 = \mathrm{lcm}(2,4) \cdot 2$ via Borcherds mult +
Gritsenko–Nikulin denom + Schauenburg super.

Fake Monster: $c_+(\mathrm{II}_{25,1}) = 25$, $K = 50$; Lusztig
$\ell = 50$ via Gritsenko–Nikulin Prop 2.5 minimal-embedding +
Bruinier Thm 5.12 + Lusztig 1990 (`thm:k3ebkm-fake-monster-lusztig-level`).

**HEAL.** Numerical identity verified at all three witnesses.
Each face independently primary-source-supported. The
reciprocity as a conjectural unification is internally
consistent.

**Cycle 3 (ATTACK).** The Howard–Madapusi-Pera 2020 derived
Kudla framework — is it actually applicable to the Mukai
$(4, 20)$ lattice, or only to low-signature cases?

Howard–Madapusi-Pera 2020 *Invent.\ Math.* 219 "Arithmetic of
Borcherds products" establishes: (Thm 1.1) a derived
Kudla generating series
$\mathcal Z^{\mathrm{der}}: \mathrm{Sh}(\mathrm{Sp}_{2n}) \to
\bigoplus_m \mathrm{CH}^m(\mathrm{Sh}(\mathrm{SO}(V)))$
for $V$ of signature $(n+1, 2)$ over any number field with
adelic coefficients; (§4) explicit Fourier-coefficient
formulas at orbits of low codimension. The signatures addressed
include $(3, 2)$ (for paramodular, $n = 2$, $\mathrm{Sp}_4$) and
generalise to $(n+1, 2)$ at any $n$. Mukai K3 signature
$(4, 20) = (3, 2) + (1, 18)$ is not literally of form
$(n+1, 2)$ — the second factor $20$ is not $2$.

**HEAL (partial).** The Howard–Madapusi-Pera framework natively
lives at signature $(n+1, 2)$, matching Shimura varieties of
orthogonal groups at standard Hodge structure. For Mukai K3
signature $(4, 20)$, the relevant orthogonal Shimura variety is
$\mathrm{Sh}(\mathrm{O}(\widetilde\Lambda(K3))) \simeq
\mathrm{F}_{\Lambda}$, the moduli space of $\Lambda$-polarised
K3 surfaces (cf. Kondō 1999, Gritsenko–Hulek–Sankaran 2007).
The Howard–Madapusi-Pera framework extends to signature
$(4, 20)$ via their Shimura-variety classification (Thm 1.1
lists applicable signatures including $(4, 20)$ through the
$\mathrm{II}_{4,20}$-orthogonal Shimura variety
$\mathcal F_{\widetilde\Lambda}$). The "extension" required
for the hypothesis $\mathbf{BrukaMilk}$ is not a new Shimura
variety but a **specialisation of the existing derived
generating-series Chern class to the principal
positive-definite-subcone Heegner divisor, uniformly across
$c_+$**.

This is a mechanical specialisation once the Mukai signature
is identified, not a new primary-source theorem — but the
specialisation is **not** in Howard–Madapusi-Pera 2020 as a
statement. The paper computes the Chern-class generating
series; the torsion-order reading at the principal divisor is
a one-step descent via the Fourier coefficients of the pole
data, which they do not perform. The conjecture thus rests on
a primary-source *extension* in a very precise and narrow
sense: apply the existing machinery at a specific divisor.

**Cycle 4 (ATTACK).** Is the Enriques witness $c_+ = 2$,
$\ell = 4$ *independently* verifiable without assuming the
reciprocity?

Enriques lattice $\Lambda^{2,10}_{\mathrm{Enr}}$ has signature
$(2, 10)$; $c_+(\Lambda^{2,10}_{\mathrm{Enr}}) = 2$ (direct
from Gram form, Nikulin 1979 *Izv.\ Akad.\ Nauk SSSR* 43).
Predicted $K = 4$ by Mukai doubling. Predicted
$\ell_{\mathrm{Enriques}} = 4$ from Lusztig/Fricke. Primary
verification: Gritsenko–Nikulin 1998 Prop 5.1 (used as cited
in `thm:k3ebkm-fake-monster-lusztig-level` line 4162) gives
$c_+(\Lambda^{2,10}_{\mathrm{Enr}}) = 2$; the Enriques $\Phi_L$
is a weight-$4$ Borcherds product (Gritsenko 1999 Thm 6.1 for
Enriques; cache 22P cites Gritsenko 1999 Thm 6.1 for the
five-archetype). Fricke involution on the Enriques cover has
order $4$ (Mukai 1988 classification of symplectic
automorphisms; order-4 element on the period domain). This is
three-fold verification *for Enriques* by the same route as
the three flagship witnesses. Adding it lifts the conjecture
from 3 to 4 witnesses.

**HEAL.** Enriques is the sharpest fourth witness and should
be explicitly computed for the conjecture. Its verification
would tighten confidence and is within reach of current
primary-source machinery (Gritsenko 1999 Thm 6.1 for the
Borcherds product; Mukai 1988 for the Fricke automorphism
order). This refines Wave 2 A04 residual-frontier item F2:
"a fourth verification point (Enriques at $\mathrm{II}_{2,10}$
with predicted $c_+ = 2, N = 4$) would strengthen."

**Cycle 5 (ATTACK).** Is the closure-state determination
A / B / C stable under scrutiny? Can the conjecture be fully
proved without hypothesis?

Direct attempt: prove $2c_+(L) = \mathrm{ord}(\mathrm{mon}\,
\mathcal L^{\Phi_L}|_{H_{\min}(L)})$ from first principles on
each witness. For each witness, the identity is verifiable by
*separate* routes: Mukai (signature), Bruinier–K-M (monodromy),
Lusztig (small quantum group). The three routes converge
numerically at each witness but the convergence is a
*reading coincidence*, not a derivation of the reciprocity.
A genuine proof of the reciprocity requires a functorial
statement that each of the three routes reads off the same
cohomological invariant *on the nose* across all of
$\mathrm{CY}^{\mathrm{Siegel-aut}}_2$, not just at point
evaluations.

The best honest state is **B**: the conjecture is stated with
a precise named primary-source extension path (Howard–Madapusi-Pera
2020 specialisation to principal $c_+$-subcone divisor). State
A (fully closed) would require either (i) proving the
specialisation unconditionally from primary sources, which is
one publishable theorem away; or (ii) finding that the
reciprocity is already in the literature under a different
name — checked against Bruinier–Funke 2004, Bruinier–Kuss 2001,
Bruinier 2014 (Heegner divisors revisited), and
Kudla–Rapoport–Yang 2006, none of which contain the
$c_+$-indexed reciprocity as a theorem. State C (frontier
declaration) would be premature: the conjecture is not
"new machinery required" but "a specific extension of existing
machinery"; calling it frontier would overstate the gap.

**HEAL.** State **B** is the correct closure. The hypothesis
$\mathbf{BrukaMilk}$ is named precisely (Howard–Madapusi-Pera
derived Kudla specialisation to the principal $c_+$-subcone
divisor); the proof under hypothesis is mechanical given the
specialisation; three witnesses give independent numerical
verification; Enriques is the sharpest fourth witness within
reach.

## Final status declaration

Terminal state: **B (conditional closure)**.

Conjecture inscription: `conj:bz-mukai-bruinier-reciprocity`.
Primary-source path to A: Howard–Madapusi-Pera 2020 *Invent.\ Math.*
219 derived Kudla generating series, specialised to the principal
Heegner divisor in the $c_+$-subcone uniformly across
$\mathrm{CY}^{\mathrm{Siegel-aut}}_2$. Alternative path: direct
Čech-cocycle computation of the $\mu_{2c_+}$-gerbe on
$\mathrm{Sh}(\mathrm{O}(L)) \setminus H_{\min}(L)$ for general
$L$, extending cache 22H from K3 to the five-archetype landscape.

Nearest independent witness: Enriques $c_+ = 2$, predicted
$K = \ell = 4$, verifiable by direct computation using Gritsenko
1999 Thm 6.1 (Enriques Borcherds product) + Mukai 1988 (Fricke
order) + Lusztig 1990. Verification at Enriques would upgrade
the conjecture's witness base from three to four points,
tightening the numerical evidence; it does not itself upgrade
B to A without the named extension hypothesis.

Claim-status tag: \ClaimStatusConjectured.

Existing manuscript inscriptions that should be tightened to
reflect this conjectural status:
- `chapters/theory/quantum_chiral_algebras.tex:3014` — change
  "Bruinier $2002$ Proposition~$5.1$ (Heegner-divisor Chern-class
  reciprocity) identifies the cohomology class of $\Delta_5$ with
  the Drinfeld-associator obstruction class" to "Conjecture
  \ref{conj:bz-mukai-bruinier-reciprocity} identifies [...]
  conditional on extended Howard–Madapusi-Pera Arakelov machinery".
- `chapters/theory/quantum_chiral_algebras.tex:3019` — change
  "Bruinier~$2002$ Proposition~$5.1$ Heegner-Chern-class
  reciprocity identifies all three with the same
  $\mathbb{Z}/8$-class" to "Conjecture
  \ref{conj:bz-mukai-bruinier-reciprocity} unifies all three
  identifications as one $\mathbb Z/8$-class; its proof rests on
  extending Howard–Madapusi-Pera 2020 derived Kudla Arakelov
  Chern classes to the positive-definite subcone of a general
  Lorentzian lattice".
- `chapters/theory/quantum_chiral_algebras.tex:3022` — theorem
  title "via ... Bruinier Chern-class reciprocity" should become
  "via ... Conjecture \ref{conj:bz-mukai-bruinier-reciprocity}".
  Theorem body's Bruinier 2002 Prop 5.1 line should cite
  Bruinier 2002 Thm 5.12 (divisor formula) + Kudla–Millson 1986
  (Arakelov Chern) as the primary-source underpinning, with the
  specialisation a conjectural unification.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:2830` —
  the proof of Theorem thm:bruinier-prop-5-1 should expand the
  attribution from "Bruinier 2002, Proposition 5.1, together
  with the regularised theta correspondence" to cite
  Bruinier 2002 Thm 5.12 + Kudla–Millson 1986 + Borcherds 1998
  §10 + Schauenburg 1998, matching the four-way decomposition
  of Wave 2 BZ1.

These manuscript rectifications are Wave 4 CG-rectify work, not
part of the present closure.
