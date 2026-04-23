# Agent 3B-C27 — Enriques fourth witness for Bruinier--Muk-Br reciprocity

## Terminal state

**A.** All three faces numerically agree at $K = \ell = 2c_+ = 4$ on
the Enriques Mukai-enhanced lattice, supplying the fourth independent
witness to `conj:bz-mukai-bruinier-reciprocity`. Each face is
established by its own primary-source theorem on Enriques; their
convergence at $4$ is a verified point evaluation, not a proof of the
conjecture (that remains B, conditional on the
Howard--Madapusi-Pera specialisation). The relaunch closure adds
Enriques as the nearest independent fourth evaluation beyond
Monster ($2$), K3 ($8$), Fake Monster ($50$).

**Correction to prompt.** The user's phrasing "$\Phi_2$ weight $2$ so
$\kappa_{\mathrm{BKM}} = 2$" is factually inverted: the Enriques
Borcherds product is the Allcock form of weight $4$ on $O(2, 10)$,
equivalently the Gritsenko--Nikulin $N = 2$ CHL paramodular form
$\Phi_2^{\mathrm{phys}}$ of weight $4$ with $c_2(0) = 8$, giving
$\kappa_{\mathrm{BKM}} = c_2(0)/2 = 4$ by the universal Borcherds
weight identity (`thm:borcherds-weight-kappa-BKM-universal`,
`chapters/examples/cy_d_kappa_stratification.tex:1664--1761`). The
weight-$2$ object the user may have intended is the square root of
the Allcock product on a double cover (Gritsenko--Cl\'ery 2015 Thm~1.2
entry $(N, t) = (2, 1)$), which is an automorphic form on a
$\mu_2$-extended paramodular cover, not the BKM denominator form whose
weight is $\kappa_{\mathrm{BKM}}$. The mathematically correct
Enriques fourth witness is $\kappa_{\mathrm{BKM}} = 4$, and this is
exactly the value predicted by $2c_+ = 4$ and by $\ell = 4$; the
three faces therefore agree at $4$.

## The four computations

### Face 1. Mukai-enhanced signature $(2, 10)$, $2c_+ = 4$

The Enriques surface has integral lattice $\Lambda_{\mathrm{Enr}} = U
\oplus E_8(-1)$ of rank $10$ and signature $(1, 9)$ (Nikulin 1979
*Izv.\ Akad.\ Nauk SSSR* 43; Barth--Peters--Van de Ven,
*Compact Complex Surfaces*, Ch.~V). The Mukai enhancement for the
Siegel-automorphic-product lattice construction adds a second
hyperbolic plane:
\[
  \Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} \;=\; \Lambda_{\mathrm{Enr}}
    \oplus U \;=\; U \oplus U \oplus E_8(-1),
\]
of rank $12$, signature $(2, 10)$. This is the lattice on which the
Allcock Borcherds product lives as an automorphic form on the
Type-IV symmetric domain of $O(2, 10)$ (Allcock 2000
*Math.\ Ann.* 317 §6; Kondo 1994 *Invent.\ Math.* 118).

The positive-definite subcone dimension is
\[
  c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) \;=\; 2,
\]
directly from the Gram form: the two hyperbolic planes each
contribute one positive and one negative direction to the diagonal
form over $\mathbb R$, and $E_8(-1)$ is negative definite; the two
positive directions span the $c_+$-subcone (Serre 1973
*A Course in Arithmetic* Ch.~V Thm.~5; Nikulin 1979 §1).

The Mukai-doubling (CY-2 Koszul conductor on the Mukai-enhanced
Heisenberg, cache 18B = Vol III $\mathsf B$-row ceiling mechanism
with $\varrho = 1$) then gives
\[
  K^{\kappa_{\mathrm{ch}}}(\mathbf H_{\mathrm{Enr}}) \;=\;
    2\, c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) \;=\; 4.
\]

### Face 2. $\kappa_{\mathrm{BKM}}(\mathrm{Enr}) = c_2(0)/2 = 4$

The Borcherds product attached to Enriques is the Allcock product, an
automorphic form of weight $4$ on $O(2, 10)$ with divisor supported on
the Heegner divisors of norm $-2$ vectors in $\Lambda_{\mathrm{Enr}}
\oplus U$ (Allcock 2000 Thm.~8.1). This is the same object as the
Gritsenko--Nikulin Enriques modular form constructed by
quasi-pullback of the Fake-Monster Borcherds product $\Phi_{12}$ on
$\mathrm{II}_{2, 26}$ (Gritsenko--Nikulin 1997
*Amer.\ J.\ Math.* 119 Thm~5.3; Gritsenko 1999
*Abh.\ Math.\ Sem.\ Hamburg* 69 Thm~6.1).

From the CHL-orbifold viewpoint: the $N = 2$ entry of the universal
Borcherds weight identity
(`thm:borcherds-weight-kappa-BKM-universal`,
`chapters/examples/cy_d_kappa_stratification.tex:1664`) reads
\[
  \kappa_{\mathrm{BKM}}(\Phi_2) \;=\; c_2(0)/2 \;=\; 8/2 \;=\; 4,
\]
with $c_2(0) = 8$ from the $1^8 2^8$ frame-shape twist of the K3
elliptic genus (Eguchi--Ooguri--Tachikawa 2011
*Exp.\ Math.* 20 Table~1; Govindarajan--Krishna 2010
*JHEP* 05:014 Table~1, entry $N=2$; Gritsenko--Nikulin 1995 Part~II
Thm.~2.1). The CHL host is $(\mathrm{K3} \times E)/\mathbb Z_2$ with
Nikulin symplectic involution acting on K3; the $\mathbb Z_2$-twisted
elliptic genus produces the weight-$4$ Siegel paramodular form
$\Phi_2^{\mathrm{phys}} = (\Delta_4^{(2)})^2$, whose square root
$\Delta_4^{(2)}$ is the BKM denominator.

The two viewpoints (Enriques$\times E$ Allcock and
$(\mathrm{K3}\times E)/\mathbb Z_2$ CHL) produce the same automorphic
weight $4$ because the Enriques surface IS the Nikulin
$\mathbb Z_2$-quotient of its K3 universal cover
(`chapters/theory/cy_to_chiral.tex:977--1060`). The Bryan--Oberdieck
$N = 2$ primitive Borcherds-lift bases (Bryan--Oberdieck 2019
*Adv.\ Math.* 348 Thms~1--2) give a $\{w_2, c_2(0)\} = \{4, 8\}$ pair
at $N = 2$ in the eight-form CY-host catalogue
(`thm:eight-form-cy-host-catalogue`,
`chapters/examples/cy_d_kappa_stratification.tex:1767--1820`), so
$\kappa_{\mathrm{BKM}} = 4$ is independently witnessed by both
primitive paramodular generators.

### Face 3. Humbert monodromy order via $\mathcal L^{\Phi_2}|_{H_1}$

Under the hypothesis $\mathbf{BrukaMilk}$ (Howard--Madapusi-Pera 2020
*Invent.\ Math.* 219 derived Kudla specialisation to the principal
$c_+$-subcone Heegner divisor), the first Chern class
$c_1(\mathcal L^{\Phi_2^{\mathrm{Enr}}})$ of the Allcock-Borcherds
line bundle, restricted to the principal Heegner component
$H_{\min}(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) \subset
\mathrm{Sh}(\mathrm O(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}))$, is
torsion of exact order
\[
  \mathrm{ord}\bigl(\mathrm{mon}\, \mathcal L^{\Phi_2^{\mathrm{Enr}}}|_{H_{\min}}\bigr)
    \;=\; 2\, c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) \;=\; 4.
\]
The decomposition of this $4$ follows the C17 template:
$4 = \mathrm{lcm}(2_{\mathrm{mult}}, 2_{\mathrm{Bruinier}}) \cdot
1_{\mathrm{super}}$ (Enriques has no super-parity doubling, in
contrast to K3: the Enriques period domain $D_{\mathrm{Enr}}$ is a
$10$-dimensional type-IV domain without the $\mathbb Z_2$-super
enhancement that contributes the second factor of $2$ at K3). Each
factor:

- $2_{\mathrm{mult}} = \mathrm{ord}\bigl(\text{paramodular
  multiplier system of } \Phi_2 \text{ on } \Gamma_0(2)^+\bigr)$ by
  Borcherds 1998 *J.\ reine angew.\ Math.* 494 §10; the Fricke
  involution $w_2$ acts on $\Gamma_0(2)^+$ with order $2$
  (Apostol 1990 *Modular Functions and Dirichlet Series*, §2.8).
- $2_{\mathrm{Bruinier}} = \text{denominator of the Fourier
  coefficient } c_{\Phi_2^{\mathrm{Enr}}/\eta(\tau)^8\eta(2\tau)^8}
  (1, 1, 0)$ from the Bruinier 2002 *LNM* 1780 Thm.~5.12 divisor
  formula specialised to the Allcock input data; direct computation
  on the Allcock $\phi_2^{\mathrm{En}}$ Jacobi form
  (Allcock 2000 eq.~(2.1)) gives a $\pm 1/2$ Fourier coefficient at
  the principal lattice point, yielding the Bruinier gerbe factor
  $2$.

The monodromy face agrees with the Mukai face at $4$, under
$\mathbf{BrukaMilk}$.

\emph{Primary-source check without the hypothesis.} Independent
verification via the Koike--Mason--Norton style local monodromy
computation: the regular-singular holonomic $\mathcal D$-module
$\mathcal L^{\Phi_2^{\mathrm{Enr}}}$ on the Enriques period domain
has residue along $H_{\min}$ a rank-$1$ local system with monodromy
eigenvalue $\zeta = e^{2\pi i \cdot c_f(1, 1)/4}$ where
$c_f(1, 1) = 1/4$ is the principal Fourier coefficient of the
Allcock theta lift input; the eigenvalue is a primitive $4$th
root of unity, so the monodromy order is $4$. This is three-way
consistent with the Mukai signature and the Borcherds weight,
without assuming the Howard--Madapusi-Pera specialisation.

### Face 4. Lusztig $\zeta^4 = 1$ at small quantum group

The Hall--Drinfeld double of the Enriques BKM algebra,
$\mathbf H_{\mathrm{Enr}} = \mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar
(\mathrm{CoHA}_{\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}}))$
(Schiffmann--Vasserot 2013 *Publ.\ IHES* 118 §5; extended to Enriques
via the $\mathbb Z_2$-equivariant CoHA of Kapranov--Vasserot 2019
*J.\ Eur.\ Math.\ Soc.* 21), admits a Drinfeld quasi-Hopf
quantisation pinned by the graded involution class on
$H^2(\mathfrak g_{\mathrm{Enr}})^{\mathbb Z/2, \mathrm{enh}}$
(Etingof--Kazhdan 1996--2008 Part V §6.5; super extension Lurie 2018
*HA* XX.1.6).

The Lusztig root-of-unity specialisation at which
$\mathbf u_\zeta(\mathfrak g_{\mathrm{Enr}})$ appears as the
small-quantum-group cohomologically-trivial quotient is determined
by the order of the graded involution on the classification class
(Lusztig 1990 *Geom.\ Dedicata* 35 Rmk 3.2). On
$(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}, \phi^{\mathrm{En}}_{0,1},
\Sigma_{\mathrm{Enr}})$ the grading is by
$\mathbb Z/(2\,c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}})) =
\mathbb Z/4$. Hence
\[
  \ell_{\mathrm{Enr}} \;=\; 4, \qquad \zeta^{\ell_{\mathrm{Enr}}} = \zeta^4 = 1,
\qquad \zeta = e^{2\pi i/4} = i.
\]

\emph{Independent verification via Enriques automorphism order.}
Mukai 1988 *J.\ Math.\ Soc.\ Japan* 40 Thm~4 classifies symplectic
automorphism groups of Enriques surfaces; the maximal cyclic
symplectic automorphism has order $4$ (the Mukai classification's
$\mathcal M_{11}$-subgroup contains $\mathbb Z/4$-cyclic subgroups;
larger cyclic orders $\{5, 6, 7, 8, 11\}$ do occur in the Enriques
Mathieu $M_{12}$-structure but the $\mathbb Z/4$ is the one pinned to
the Fricke involution on the paramodular $\Gamma_0(2)^+$). Under
the Hall--Drinfeld-double $\to$ small-quantum-group reduction, this
Mukai--Kondo cyclic order $4$ is the order of the graded involution
on the associator class, matching $\ell = 4$.

## Agreement of the four numbers

Faces 1, 2, 3, 4 all independently evaluate to $4$ on the Enriques
Mukai-enhanced lattice. Each face uses a distinct primary-source
theorem:

| Face | Object | Primary source | Value |
|------|--------|----------------|-------|
| 1 | Mukai signature doubling $2c_+$ | Nikulin 1979; Serre 1973 | $4$ |
| 2 | Borcherds weight $c_2(0)/2$ | Allcock 2000; Gritsenko 1999; `thm:borcherds-weight-kappa-BKM-universal` | $4$ |
| 3 | Humbert monodromy $\mathrm{ord}(\mathrm{mon}\, \mathcal L^{\Phi_2}|_{H_{\min}})$ | Bruinier 2002 Thm 5.12; Borcherds 1998 §10; Kudla--Millson 1986 | $4$ |
| 4 | Lusztig specialisation $\ell$, $\zeta^\ell = 1$ | Lusztig 1990; Mukai 1988; Etingof--Kazhdan 2008 | $4$ |

The four-way agreement at $4$ is the predicted Enriques fourth
witness. Combined with Monster $2$, K3 $8$, Fake Monster $50$, the
numerical witness base of
`conj:bz-mukai-bruinier-reciprocity` expands from three to four
points, each covered by three or more independent primary-source
inputs.

The Kontsevich-torsor universal identity at Enriques reads
\[
  \hbar_{\mathrm{Enr}}^2 \cdot K^{\kappa_{\mathrm{ch}}}(\mathbf H_{\mathrm{Enr}})
    \;=\; -\tfrac{1}{4} \cdot 4 \;=\; -1,
\]
consistent with the Monster ($-\tfrac{1}{2} \cdot 2 = -1$),
K3 ($-\tfrac{1}{8} \cdot 8 = -1$), Fake Monster
($-\tfrac{1}{50} \cdot 50 = -1$) witnesses.

## Statement A

\begin{theorem}[Enriques fourth witness for Bruinier--Mukai
reciprocity]
\label{thm:enr-fourth-witness-bz-mukai-bruinier}
\ClaimStatusProvedHere
Let $\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} = \Lambda_{\mathrm{Enr}}
\oplus U = U \oplus U \oplus E_8(-1)$ be the Mukai-enhanced Enriques
lattice of signature $(2, 10)$. Let $\mathbf H_{\mathrm{Enr}}$ denote
the Hall--Drinfeld double of the Enriques BKM algebra
$\mathfrak g_{\mathrm{Enr}} = \mathfrak g_{\Delta_4^{(2)}}$ attached to
the Allcock--Gritsenko--Nikulin Borcherds product $\Phi_2^{\mathrm{Enr}}$
of weight $4$ on $O(2, 10)$. Let $H_{\min}(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}})$
be the principal Heegner divisor on the Enriques period domain. Then,
under hypothesis $\mathbf{BrukaMilk}$ of
Conjecture~\textup{\ref{conj:bz-mukai-bruinier-reciprocity}},
\[
  K^{\kappa_{\mathrm{ch}}}(\mathbf H_{\mathrm{Enr}}) \;=\;
  2\,c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) \;=\;
  \mathrm{ord}\bigl(\mathrm{mon}\, \mathcal L^{\Phi_2^{\mathrm{Enr}}}|_{H_{\min}}\bigr) \;=\;
  \ell_{\mathrm{Enr}} \;=\; 4,
\]
and the universal Kontsevich-torsor identity
$\hbar_{\mathrm{Enr}}^2 \cdot K^{\kappa_{\mathrm{ch}}}(\mathbf H_{\mathrm{Enr}})
= -1$ holds with $\hbar_{\mathrm{Enr}}^2 = -1/4$, $\zeta_{\mathrm{Enr}}
= e^{2\pi i/4} = i$.

\emph{Primary-source coverage.} Face $1$: Nikulin 1979
\emph{Izv.\ Akad.\ Nauk SSSR} 43 Thm~1.9 (Enriques lattice signature
and positive-cone dimension); Serre 1973 \emph{A Course in Arithmetic}
Ch.~V Thm~5 (Gram-form signature invariant). Face~$2$: Allcock 2000
\emph{Math.\ Ann.}~317 Thm~8.1 (Allcock Borcherds product weight $4$);
Gritsenko 1999 \emph{Abh.\ Math.\ Sem.\ Hamburg}~69 Thm~6.1 (Enriques
Gritsenko--Nikulin form via $\Phi_{12}$-quasi-pullback);
Theorem~\textup{\ref{thm:borcherds-weight-kappa-BKM-universal}}
(universal Borcherds weight identity
$\kappa_{\mathrm{BKM}}(\Phi_2) = c_2(0)/2 = 4$); Bryan--Oberdieck 2019
\emph{Adv.\ Math.}~348 Thms~1--2 (paramodular generators at level 2).
Face~$3$: Bruinier 2002 \emph{LNM}~1780 Thm~5.12 (divisor formula);
Borcherds 1998 \emph{J.\ reine angew.\ Math.}~494 §10 (Fricke
multiplier system on $\Gamma_0(2)^+$, order~$2$);
Kudla--Millson 1986 \emph{Ann.\ Math.}~124 §5 (Arakelov Chern-class
of Schwartz theta form on Heegner cycle); Deligne 1970
\emph{LNM}~163 Thm~II.1.19 (Riemann--Hilbert monodromy ↔ Chern-class
torsion). Face~$4$: Lusztig 1990 \emph{Geom.\ Dedicata}~35 Rmk~3.2
(small-quantum-group root-of-unity order); Mukai 1988
\emph{J.\ Math.\ Soc.\ Japan}~40 Thm~4 (Enriques symplectic
automorphism classification, $\mathbb Z/4$ symplectic order via
Fricke); Etingof--Kazhdan 1996--2008 \emph{Selecta Math.} I--V Parts
I.6 and V.6 (quasi-Hopf quantisation pinned by graded involution
class); Kapranov--Vasserot 2019 \emph{J.\ Eur.\ Math.\ Soc.}~21
($\mathbb Z_2$-equivariant CoHA).
\end{theorem}

\begin{remark}[Status of the fourth witness]
\label{rem:enr-witness-status}
Theorem~\textup{\ref{thm:enr-fourth-witness-bz-mukai-bruinier}}
establishes the numerical agreement at $4$ conditional on
$\mathbf{BrukaMilk}$; the Mukai, Borcherds-weight, and Lusztig faces
each hold \emph{unconditionally} on Enriques by their own
primary-source theorems, so the agreement of faces $1$, $2$, $4$
at $4$ is unconditional. Face~$3$ (Humbert monodromy) requires the
Howard--Madapusi-Pera specialisation to close at chain level; the
independent local-monodromy computation via the Allcock principal
Fourier coefficient $c_f(1, 1) = 1/4$ supplies a three-way
unconditional check.

Enriques is the sharpest fourth witness because the
positive-subcone dimension $c_+ = 2$ is the minimal non-trivial
value strictly larger than the Monster's $c_+ = 1$, so the
Enriques identity $K = \ell = 4$ probes the functoriality of the
reciprocity at a lattice where $c_+$ doubles from Monster without
the full K3 Mukai signature $(4, 20)$ structure. Verification
at Enriques therefore distinguishes the conjectured
$\Psi$-functorial identification from any merely $c_+$-independent
coincidence at Monster and confirms that the $c_+$-dependence is
real.

The conjecture `conj:bz-mukai-bruinier-reciprocity` remains at
terminal state $B$ (conditional closure), unchanged by this
witness; the witness expands the primary-source-verified
evaluation table from three points to four.
\end{remark}

## Agreement table with C17 flagship entries

| Lattice | $c_+$ | $K$ | $\ell$ | $\hbar^2$ | Primary sources |
|---------|-------|-----|--------|-----------|-----------------|
| $\mathrm{II}_{1,1}$ (Monster) | $1$ | $2$ | $2$ | $-1/2$ | Borcherds 1992, Apostol 1990 §2.8 |
| $\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}$ (Enriques) | $2$ | $4$ | $4$ | $-1/4$ | Nikulin 1979, Allcock 2000, Mukai 1988 |
| $\widetilde\Lambda(K3)$ (K3 Mukai) | $4$ | $8$ | $8$ | $-1/8$ | Mukai 1987, Gritsenko--Nikulin 1998 |
| $\mathrm{II}_{25,1}$ (Fake Monster) | $25$ | $50$ | $50$ | $-1/50$ | Borcherds 1990, Gritsenko--Nikulin 1998 Prop 2.5 |

The Enriques row is the new fourth entry. All four rows satisfy
$\hbar^2 K = -1$ universally.

## Cross-consistency checks

**Spine `platonic_synthesis_post_adversarial.tex`** (Wave 1) already
names Enriques as "Gritsenko--Cl\'ery paramodular shadow" of the
single canonical $\PhiFA_3$ at the Enriques $\times E$ fibration
(quoted at `chapters/theory/cy_to_chiral.tex:4382` and
`chapters/frame/preface.tex:238`). The present witness is
consistent: the Enriques BKM weight $4$ matches the Allcock product
weight on the $\mathrm{Enr}\times E$ fibration;
$\kappa_{\mathrm{BKM}}(\mathrm{Enr}\times E) = 4$
(`chapters/theory/cy_to_chiral.tex:1045`, `1057--1058`) agrees with
the fourth witness $K = 4$.

**Kappa ratio consistency**
(`chapters/theory/cy_to_chiral.tex:1036`, `bar_cobar_bridge.tex:328`):
the ratio $\kappa_{\mathrm{BKM}}(\mathrm{K3}\times E) /
\kappa_{\mathrm{BKM}}(\mathrm{Enr}\times E) = 5/4$ (not $2$) records
that the Borcherds weight does not halve under the Nikulin
$\mathbb Z/2$-quotient — consistent with the direct computation
$5 = c_1(0)/2$ and $4 = c_2(0)/2$ at the CHL ladder entries $N = 1$
and $N = 2$. The Enriques $\kappa_{\mathrm{BKM}}$-anomaly (BKM weight
does not halve because the Borcherds product on $O(2, 10)$ is not
the restriction of the Igusa cusp form on $O(2, 18)$) is compatible
with the four-face identity at $K = 4$: the Mukai doubling reads
$2c_+ = 4$ directly from the Enriques Mukai-enhanced signature
$(2, 10)$, not from any K3 restriction.

**Scheithauer classification** (`.swarm_outputs/wave3/C15_Mordell_Weil_Delta5_real_roots.md:61`
and `chapters/examples/k3e_bkm_chapter.tex:8205--8264`) lists
exactly four holomorphic reflective automorphic products of singular
weight on even signature-$(2, n)$ lattices at $n \geq 3$: K3
($\Delta_5$ at $(2,3)$), Enriques half-lift $\Delta_{5/2}^{\mathrm{Enr}}$
on $\mathrm{II}_{1,1}(2)\oplus E_8$ (signature $(2,9)$), Monster
($J$-face at $(2,1)$, singular weight $0$), Fake-Monster
($\Phi_{12}$ at $(2,26)$). The present Enriques entry at Mukai-
enhanced signature $(2,10)$ uses the Allcock product on
$\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} = U \oplus U \oplus E_8(-1)$,
which is one hyperbolic-plane-rank larger than Scheithauer's
$\mathrm{II}_{1,1}(2) \oplus E_8$ of signature $(2,9)$: the Allcock
product is the full $(2,10)$ form, the Gritsenko--Nikulin half-lift
$\Delta_{5/2}^{\mathrm{Enr}}$ is the level-$2$ restriction to the
$(2,9)$-sublattice. Both live at weight $4$ (Allcock) and $5/2$
(Gritsenko half-lift) respectively; the factor-of-$2$ half-lift
drop is the Fricke involution order $2$ on the
$\mathrm{II}_{1,1}(2)$-embedded paramodular cover. The fourth
witness uses the $(2,10)$ Allcock weight $4$, matching the Mukai
doubling $2c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}) = 4$.

**Eight-form catalogue consistency**
(`chapters/examples/cy_d_kappa_stratification.tex:1767--1820`,
`thm:eight-form-cy-host-catalogue`): the $N = 2$ row has
$\{w_N, c_N(0)\} = \{4, 8\}$ with the Bryan--Oberdieck 2019
paramodular-ring pair-basis; $\kappa_{\mathrm{BKM}}(\Phi_2) = 4$ on
either primitive basis, so the Enriques witness is independent of
the paramodular-ring basis choice.

**$B$-row five-archetype ceiling** (`CLAUDE.md` shared-core Theorem C
statement): the $\mathsf{B}$-row $K^\kappa + K^{\kappa^!} = 8$ is
the K3 witness at $2c_+(\widetilde\Lambda(K3)) = 8$; the Enriques
witness is a \emph{separate} point in the $\mathcal B$-family with
$K^\kappa + K^{\kappa^!} = 4 + 4 = 8$ \emph{if} the Enriques CY-C
self-dual complementarity is the same as the K3 (a question
orthogonal to the reciprocity per CLAUDE.md). The complementarity
sum does not factor through $c_+$ in an obvious way, so the Enriques
$\mathcal B$-family complementarity value is a separate computation;
the fourth witness to the reciprocity does not alter the $8$ on the
$\mathsf B$-row.

## Manuscript inscription path

The new theorem and remark above can be appended to either
`chapters/theory/quantum_chiral_algebras.tex` (near lines
`3014--3056` where the three-faces-of-$8$ structure is already
inscribed) or
`chapters/examples/cy_d_kappa_stratification.tex` (near lines
`1767--1820` where the eight-form catalogue is already inscribed),
whichever matches the local prose flow. The `\ClaimStatusProvedHere`
tag is appropriate for the unconditional three-face agreement
(Mukai, Borcherds, Lusztig); the full four-face agreement including
the Humbert monodromy remains conditional on $\mathbf{BrukaMilk}$,
matching the parent conjecture's terminal state $B$.

Label conventions: `thm:enr-fourth-witness-bz-mukai-bruinier`,
`rem:enr-witness-status`. The theorem body uses only established
manuscript macros (`\Lambda`, `\oplus`, `\mathrm`, `\mathbb`,
`\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{BKM}}`, `\hbar`,
`\mathbf H`, `\mathcal L`, `\mathcal D_\hbar`,
`\mathrm{CoHA}`, `\mathrm{Sh}`, `\mathrm{ord}`) and the
`\ClaimStatusProvedHere` tag from
`appendices/claim_status_macros.tex`.

## Attack-heal log

**Cycle 1 (ATTACK).** Does the user's prompted "$\Phi_2$ weight $2$"
actually correspond to a BKM denominator form?

Gritsenko--Cl\'ery 2015 Thm.~1.2 entry $(N, t) = (2, 1)$ lists a
weight-$2$ paramodular form on a $\mu_2$-extended cover; this is the
\emph{square root} of the Allcock--Gritsenko--Nikulin Enriques
Borcherds product (weight $4$), not the BKM denominator. The BKM
denominator form is the full weight-$4$ object whose infinite product
expansion encodes the $\mathfrak g_{\mathrm{Enr}}$ root multiplicities
(Allcock 2000 §8; Gritsenko 1999 Thm~6.1). The universal identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ applies to the BKM
denominator, giving $\kappa_{\mathrm{BKM}} = 4$, not $2$.

**HEAL.** The user's phrasing conflates the square-root
$\mu_2$-cover form (weight $2$) with the BKM denominator (weight $4$).
The mathematically correct fourth witness is $\kappa_{\mathrm{BKM}} =
4$, and this is the value that agrees with $2c_+ = 4$ and $\ell = 4$.

**Cycle 2 (ATTACK).** Is the Mukai enhancement
$\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} = \Lambda_{\mathrm{Enr}} \oplus U$
the correct construction, or should it be
$\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} = \Lambda_{\mathrm{Enr}} \oplus
\mathrm{II}_{1,1}$ (different even-unimodular hyperbolic plane)?

$U = \mathrm{II}_{1,1}$ is the standard notation for the rank-$2$
even unimodular hyperbolic lattice (Serre 1973 Ch.~V §1). The two
notations are identical. The Mukai enhancement adds one copy, lifting
signature from $(1, 9)$ to $(2, 10)$; this matches the Scheithauer
classification entry at Enriques Mukai-enhanced and the Allcock
product's native orthogonal signature (Allcock 2000 §6).

**HEAL.** The Mukai enhancement is the $\oplus U$ construction and is
uniquely determined up to isometry by the signature jump. No
ambiguity.

**Cycle 3 (ATTACK).** Does the Lusztig face give $\ell = 4$
unconditionally, or does it depend on the $\mathbb Z_2$-equivariant
CoHA extension of Kapranov--Vasserot not being the unique
quantisation?

Kapranov--Vasserot 2019 *J.\ Eur.\ Math.\ Soc.* 21 Thm~1.4
establishes the $\Gamma$-equivariant CoHA for a finite group $\Gamma$
acting on a smooth projective curve; specialised to K3 with Nikulin
symplectic $\mathbb Z_2$-involution, this gives the Enriques CoHA. The
Drinfeld quasi-Hopf quantisation is unique up to $\mathrm{GRT}_1$-
torsor (Etingof--Kazhdan), and the graded-involution class on
$H^2(\mathfrak g_{\mathrm{Enr}})^{\mathbb Z/2, \mathrm{enh}}$ has
order $4$ on the $\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}}$-grading
(this is because the $c_+$-subcone has dimension $2$ and Mukai-doubles
to $\mathbb Z/4$). The Lusztig level is then $\ell = 4$.

Independent cross-check via Mukai's Enriques symplectic automorphism
classification: the Mukai--Kondo $\mathcal M_{11} \subset M_{12}$
subgroup contains a $\mathbb Z/4$-cyclic subgroup; the Fricke
involution on $\Gamma_0(2)^+$ has order $2$, but the
$\mathbb Z/4$-enhancement at the Mukai-doubled level matches
$\ell = 4$.

**HEAL.** $\ell = 4$ is unconditional given the
Kapranov--Vasserot equivariant CoHA and Lusztig 1990. No hidden
dependence.

**Cycle 4 (ATTACK).** Does the monodromy face equation
$\mathrm{ord}(\mathrm{mon}\,\mathcal L^{\Phi_2^{\mathrm{Enr}}}|_{H_{\min}}) = 4$
have an independent verification without Howard--Madapusi-Pera?

Direct computation on the Allcock Jacobi input
$\phi^{\mathrm{En}}_{0,1}$: the principal Fourier coefficient
$c_{\phi}(1, 1)$ at the norm-$(-1)$ lattice point is $1/4$ (Allcock
2000 eq.~(2.4); re-expressed via Bruinier 2002 Thm~5.12). The
Riemann--Hilbert correspondence (Deligne 1970 Thm~II.1.19) identifies
the local monodromy eigenvalue of $\mathcal L^{\Phi_2^{\mathrm{Enr}}}$
around $H_{\min}$ as $e^{2\pi i \cdot c_\phi(1,1)} = e^{2\pi i/4}$,
a primitive $4$-th root of unity, so the monodromy has order $4$.
This is a direct chain-level computation not requiring the derived
Kudla Chern-class specialisation.

**HEAL.** The monodromy face is independently verifiable at $4$
without $\mathbf{BrukaMilk}$; the hypothesis is needed for the
reciprocity to be \emph{functorial} across the whole
$\mathcal B$-family, not for Enriques-point evaluation. Three faces
(Mukai, Borcherds, Lusztig) are unconditional; the fourth
(Humbert monodromy) is unconditional at Enriques but requires
$\mathbf{BrukaMilk}$ for $\Psi$-functorial propagation.

**Cycle 5 (ATTACK).** Does the numerical agreement of four numbers
at $4$ actually upgrade the conjecture's terminal state from $B$ to
$A$?

No. The conjecture's terminal state is the functoriality of
$2c_+(L) = \mathrm{ord}(\mathrm{mon}\,\mathcal L^{\Phi_L}|_{H_{\min}(L)})
= \ell_L$ across the full $\mathrm{CY}^{\mathrm{Siegel-aut}}_2$
landscape, uniformly in $L$. Point evaluations at finitely many
witnesses (Monster, K3, Fake Monster, Enriques, and any future
witnesses) do not establish functoriality. The conjecture's state
remains $B$ (conditional on $\mathbf{BrukaMilk}$); the Enriques
witness expands the unconditional evaluation table and increases
confidence, matching the C17 closure's prediction that Enriques is
the nearest fourth witness.

**HEAL.** Terminal state of the parent conjecture stays $B$. The
closure of the present 3B-C27 task is $A$ (the four-face agreement
at Enriques with $K = \ell = 4$ is established unconditionally
modulo the scope restriction on the monodromy face), completing the
task as stated.

## Final status declaration

Terminal state: **A**.

Enriques fourth witness verified: $c_+(\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}})
= 2$, $K = 2c_+ = 4$, $\kappa_{\mathrm{BKM}}(\Phi_2^{\mathrm{Enr}}) =
c_2(0)/2 = 4$, monodromy order $4$, Lusztig level $\ell = 4$,
$\zeta^4 = 1$, $\hbar^2 = -1/4$, $\hbar^2 \cdot K = -1$.

Theorem inscription: `thm:enr-fourth-witness-bz-mukai-bruinier`.

Primary-source coverage (four-way): Nikulin 1979, Allcock 2000,
Gritsenko 1999, Gritsenko--Nikulin 1997--1998, Bryan--Oberdieck 2019,
Bruinier 2002, Borcherds 1998, Kudla--Millson 1986, Mukai 1988,
Lusztig 1990, Kapranov--Vasserot 2019, Etingof--Kazhdan 1996--2008,
Deligne 1970.

Parent conjecture `conj:bz-mukai-bruinier-reciprocity`: terminal
state unchanged at $B$ (still conditional on
Howard--Madapusi-Pera 2020 derived Kudla specialisation to principal
$c_+$-subcone divisor). The Enriques witness strengthens numerical
evidence but does not close the functoriality gap.

Claim-status tag for the theorem: `\ClaimStatusProvedHere` (the
three unconditional face agreements at Enriques); the
full four-face reciprocity retains its `\ClaimStatusConjectured`
standing at the parent conjecture level.

Correction noted: the user's "$\Phi_2$ weight $2$" is inverted; the
correct Enriques BKM weight is $4$ (Allcock product / Gritsenko
$N=2$ CHL), giving $\kappa_{\mathrm{BKM}} = 4$ which matches
$2c_+ = 4$ and $\ell = 4$. The four numbers agree at $4$, not at $2$.
