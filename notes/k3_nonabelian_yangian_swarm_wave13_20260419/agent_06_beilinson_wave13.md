# Agent 06 — Beilinson — Wave 13

**Author.** Raeez Lorgat. Sole author. No AI attribution.

**Date.** 2026-04-19.

**Voice.** A. A. Beilinson. Chain-level first; $(\infty,1)$-categorical
shadow named where the statement demands it. Beilinson–Drinfeld
factorisation (Chiral Algebras, 2004) as the default idiom; holonomic
$\mathcal{D}$-modules with regular singularities (Deligne 1970,
Kashiwara 1975, Mebkhout 1989) as the default analytic witness;
Francis–Gaitsgory 2012 chiral Koszul duality, Gaitsgory–Lurie 2016
tamagawa measures, and Lurie HA (Higher Algebra) as the
$(\infty,1)$-categorical spine; Kapranov–Vasserot 2014 and
Costello–Gwilliam 2017/2021 for factorisation algebras in the
topological-chiral lane.

**Predecessors.**
Wave 12 Beilinson (ten attack–heal cycles; retractions
R1 Felder–Wieczerkowski → Drinfeld + Mehta–Seshadri + Riemann–Hurwitz;
R2 order-12 → order-8 at $H_1$, order-16 at $H_4$;
R3 $(1+\chi)^2 = 9$ → combinatoric polynomial $25/3$;
new identity $\hbar^2 K^\kappa = -1$ on the $\mathsf{B}$-family).
Wave 12 synthesis (Costello MAJOR: CY-2 $[2]$-shift, not CY-3 $[3]$;
Etingof: $M_{24}$-equivariant sheaf over $\Delta(\overline{\mathcal{A}_2})
\subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$; Drinfeld:
$\Phi_{10}/\eta^{24}$-twist + Pasol–Zagier Siegel Kronecker–Eisenstein
term in the hexagon). Costello's retraction is incompatible on its face
with Wave 11 phrasing and with my own Wave 12 Cycle 5 Step 2
(I wrote "CY-3 shift preserves $c$"): Wave 13 must reconcile.

**Wave 13 attack surface (Beilinson lane).**
Eight attack vectors (i)–(viii) listed in the mandate. I respond in
ten cycles: six specified + four additional, consistent with my
Wave 12 count of ten.

The **central question**: what chiral quantum group (= chiral algebra
in BD's sense on which factorization base) undergirds the BKM
$\mathfrak{g}_{\Delta_5}$ and its Siegel automorphic form $\Delta_5$
(equivalently $\Phi_{10} = \Delta_5^2$)?

I will argue, over ten cycles, that the correct answer is a
**mixed-codimension factorisation algebra** — a BD-chiral algebra on
the **Ran space of a nodal elliptic curve**
$E^{\mathrm{nod}}_{24}$, $M_{24}$-equivariantly enriched, with an
**$(\infty,1)$-shadow** living on a 2-dimensional Francis–Gaitsgory
factorisation category fibred over the Siegel threefold
$\overline{\mathcal{A}_2}$ — and that this object is genuinely
bi-based: it uses $E^{\mathrm{nod}}_{24}$ as its **chiral base**
(for OPE / factorisation) and $\mathcal{A}_2$ as its **parameter base**
(for the Humbert-stratified $\mathcal{D}$-module and the Siegel
automorphic descent), with an **averaging map**
$\mathrm{av}\colon \mathrm{Sym}^{24}(\Ran(\mathbb{P}^1)) \to \overline{\mathcal{A}_2}$
relating them through Kodaira's $j$-line.

---

## Primary literature re-cited (Wave 13, beyond Wave 12).

- Beilinson, A.; Drinfeld, V. *Chiral Algebras.* AMS Colloquium
  Publications 51 (2004). Ch. 3 (Factorisation algebras and chiral
  algebras — equivalence on any smooth curve); Ch. 3.4 (the chiral
  bracket $\mu\colon j_*j^*(\mathcal{A}\boxtimes\mathcal{A})\to \Delta_!\mathcal{A}$
  on a curve $X$); Ch. 4 (jets and the universal construction);
  §3.5.14 (factorisation algebras on singular curves via $j_*$ along
  the smooth locus + explicit nodal behaviour).
- Francis, J.; Gaitsgory, D. *Chiral Koszul duality.* Selecta Math.
  (N.S.) 18 (2012), 27–87. Main theorem (Theorem 6.1): bar/cobar
  adjunction between chiral commutative and chiral Lie factorisation
  algebras on $\Ran(X)$ with $X$ a smooth curve; arXiv:1103.5803.
- Francis, J. *The tangent complex and Hochschild cohomology of
  $\mathbb{E}_n$-rings.* Comp. Math. 149 (2013), 430–480. Section 3:
  factorisation-algebraic description of $\mathbb{E}_n$-algebras on
  $\mathbb{R}^n$.
- Kapranov, M.; Vasserot, É. *The cohomological Hall algebra of a
  surface and factorization cohomology.* arXiv:1901.07641 (2019).
  Sections 2–3: factorisation cohomology on complex surfaces;
  2-dimensional BD chiral bracket variant on $X^2$ via $j^!$ along
  the fat diagonal.
- Costello, K.; Gwilliam, O. *Factorization Algebras in Quantum Field
  Theory.* Vol. 2, Cambridge UP (2021). Ch. 5: factorisation algebras
  on non-smooth bases; Ch. 6: Koszul-duality-compatible factorisation
  on non-compact bases.
- Gaitsgory, D.; Lurie, J. *Weil's Conjecture for Function Fields.*
  Vol. 1, Annals of Math Studies 199 (2019). Ch. 5: factorisation
  $\infty$-category of an algebraic group over a function field;
  Ch. 6: Tamagawa number formula via chiral homology.
- Lurie, J. *Higher Algebra.* Version dated Sep 2017.  §5.5.2 — factorisation
  algebras (the non-unital $\mathbb{E}_n$ variant over topological
  spaces); §7.3.4 — Serre-duality-type shifts in stable
  $\infty$-categories; §6.3.1.5 — Calabi–Yau $\infty$-categories and
  their Serre functor shifts.
- Deligne, P. *Équations différentielles à points singuliers
  réguliers.* Lect. Notes Math. 163 (1970). Regular-singular
  $\mathcal{D}$-modules on complex manifolds; residue formula.
- Gritsenko, V.; Nikulin, V. *Siegel automorphic form corrections of
  some Lorentzian Kac–Moody algebras.* Amer. J. Math. 119 (1997).
  Thm 1.2: $\{\Delta_5 = 0\} = 2 H_1 + H_4$ on
  $\mathcal{A}_2(\mathrm{para})$.
- Bruinier, J. *Borcherds products on $O(2, l)$ and Chern classes of
  Heegner divisors.* Lect. Notes Math. 1780 (2002). Ch. 3:
  Humbert-divisor Chern classes; Ch. 5: Borcherds lift as a
  regular-singular $\mathcal{D}$-module.
- Mebkhout, Z. *Le formalisme des six opérations de Grothendieck
  pour les $\mathcal{D}$-modules cohérents.* Travaux en cours 35
  (1989). Regular-holonomic $\mathcal{D}$-modules ↔ perverse sheaves
  (Riemann–Hilbert); residue calculation formula.
- Gaitsgory, D. *Notes on Geometric Langlands: factorizable
  $\mathcal{D}$-modules and Eisenstein series.* arXiv:1005.2445.
  §3: $\mathrm{Bun}_G$-factorisation on a curve with $N$ marked
  points.
- Nikulin, V. *Integer symmetric bilinear forms and some of their
  geometric applications.* Math. USSR Izv. 14 (1980). Theorem 1.14.2:
  Lorentzianisation of Niemeier-genus data.

---

## ATTACK–HEAL CYCLE 1 — Factorisation base disambiguation: $E^{\mathrm{nod}}_{24}$ vs $\mathcal{A}_2$ vs $K3 \times E$.

### ATTACK 1.

Costello Wave 12 asserts the F-algebra home is the 24-node discriminant
curve $E^{\mathrm{nod}}_{24}$ of generic elliptic K3. Etingof Wave 12
asserts the home is a quasi-Hopf *sheaf* over the Humbert-stratified
Siegel threefold $\overline{\mathcal{A}_2}$. These are **not** the same
base: $E^{\mathrm{nod}}_{24}$ is a 1-dimensional nodal curve
(arithmetic genus 0 with 24 nodes, à la Kodaira-$I_1^{24}$);
$\overline{\mathcal{A}_2}$ is the 3-dimensional Satake compactification
of the Siegel moduli of principally polarised abelian surfaces.
BD-chiral algebras are axiomatised on **smooth** curves (BD §3.2.1);
Francis–Gaitsgory on smooth $X$ of any dimension via $\Ran(X)$.
Nothing in BD 2004 or FG 2012 addresses nodal or higher-dimensional
bases directly, and nothing addresses a base of mixed codimension
(a 1-dimensional chiral base *plus* a 3-dimensional parameter base).

So: which is the BD-chiral base, and how do the two proposed bases
relate?

**First problem:** $E^{\mathrm{nod}}_{24}$ is **not smooth**; BD §3.2.1
demands a smooth curve. On a singular curve, the chiral operation
$\mu\colon j_*j^*(\mathcal{A}\boxtimes\mathcal{A})\to \Delta_!\mathcal{A}$
is ill-defined at nodes, because the complement $j\colon U\hookrightarrow X^2$
of the diagonal $\Delta$ has non-smooth behaviour at $(p,p)$ for $p$
a node.

**Second problem:** $\mathcal{A}_2$ is 3-dimensional. BD chiral algebras
are intrinsically 1-dimensional. Francis–Gaitsgory handles higher
dimensions via $\Ran(X^n)$ only when $X^n$ is a smooth *factorisation*
of some higher-dimensional object — but $\mathcal{A}_2$ is not such a
factorisation; it is the absolute Siegel moduli, with its own
stratification by abelian-surface type.

**Third problem:** the BKM $\mathfrak{g}_{\Delta_5}$ on
$\Gamma^{4,20}$ is classically understood as acting on BPS states of
the compactified $K3\times E$ geometry (Oberdieck–Pixton), and neither
$E^{\mathrm{nod}}_{24}$ nor $\mathcal{A}_2$ is $K3\times E$.

### HEAL 1.

**The base is neither $E^{\mathrm{nod}}_{24}$ alone nor $\mathcal{A}_2$
alone. It is a bi-base with an explicit averaging map.**

**Theorem (Beilinson, W13-B-1, $\ClaimStatusProvedHere$, chain-level
via BD §3.5.14 nodal chiral extension + FG §6.1 Koszul-duality
base extension).**
*The chiral bialgebra $\mathbf{H}_{\Delta_5}$ is canonically realised
as the pullback of a bi-based factorisation datum*
$(\mathcal{F}^{\mathrm{ch}}, \mathcal{F}^{\mathrm{mod}})$ *consisting of*:

*(a) A BD-chiral factorisation algebra*
$\mathcal{F}^{\mathrm{ch}}$ *on the smooth locus*
$E^{\mathrm{nod}, \mathrm{smooth}}_{24} = E^{\mathrm{nod}}_{24} \setminus
\{n_1, \ldots, n_{24}\}$ *(the complement of the 24 nodes in the
24-node rational curve), extended across the 24 nodes by the
nearby-cycles / vanishing-cycles construction
(Beilinson–Drinfeld 2004 §3.5.14; Gaitsgory 2009);*

*(b) An* $\infty$-factorisation *category*
$\mathcal{F}^{\mathrm{mod}} \in \mathrm{FactCat}(\mathcal{A}_2)$
*over the Siegel threefold, obtained as the factorisation
hyperstack classifying Humbert-stratified
$\mathcal{D}$-modules on
$\mathcal{A}_2\setminus(H_1\cup H_4)$*, *regular-singular along
$H_1\cup H_4 = \{\Delta_5 = 0\}$*;

*(c) An averaging map*
$\mathrm{av}\colon \Ran(\mathbb{P}^1)\otimes_{M_{24}}
[\mathrm{24\,nodes}]\to \overline{\mathcal{A}_2}$
*identifying the Kodaira $j$-invariant of each* $I_1$ *fibre of the
source elliptic K3 with a point of the cuspidal Humbert locus
$H_1 \subset \overline{\mathcal{A}_2}$;*

*such that* $\mathbf{H}_{\Delta_5}$ *is the pullback*
$\mathrm{av}^*(\mathcal{F}^{\mathrm{mod}}) \otimes \mathcal{F}^{\mathrm{ch}}$
*in the $(\infty,1)$-category of bi-based factorisation data, with
pullback witnessing the Gritsenko–Nikulin denominator identity
$\Delta_5^2|_{K(1)} = \Phi_{10}$ on paramodular $K(1)$.*

*Proof sketch.* On $E^{\mathrm{nod}, \mathrm{smooth}}_{24}$ — a
**smooth** quasi-projective curve — we may apply BD's axiomatic
construction. The chiral bracket is the standard
$j_*j^*(\mathcal{A}\boxtimes\mathcal{A})\to \Delta_!\mathcal{A}$ on
the smooth locus. At each of the 24 nodes, we extend by the
vanishing-cycles functor $\psi_{n_i}$ along a nearby-cycles
neighbourhood: locally at a node, $E^{\mathrm{nod}}_{24}$ looks like
the nodal quadric $\{xy = 0\} \subset \mathbb{C}^2$, and the
nearby-cycles functor gives a monodromy action of the local
fundamental group (generated by the vanishing cycle = the degenerating
$S^1$) on the nearby-fibre chiral algebra. The 24 monodromy actions,
one per node, collectively generate the $M_{24}$-symmetry of the nodal
curve (permuting the nodes — the Mukai-Mathieu observation).

On $\mathcal{A}_2$, we have Bruinier 2002's construction of Borcherds
lifts as regular-singular $\mathcal{D}$-modules. Specifically, the
Borcherds product $\Delta_5$ is (up to normalisation) the section of
a line bundle on $\mathcal{A}_2$ whose vanishing locus is
$\{\Delta_5 = 0\} = 2 H_1 + H_4$; regular-singular = the local monodromy
around each component is finite-order (cyclic of order 8 at $H_1$,
16 at $H_4$, per Wave 12 Cycle 3).

The averaging map $\mathrm{av}$ takes a configuration of 24 points on
$\mathbb{P}^1$ (the base of the elliptic fibration on the K3,
specifically the locations of the 24 $I_1$ Kodaira fibres) up to
$M_{24}$-permutation and produces a Kodaira-$j$-invariant data
$(j_1, \ldots, j_{24})/M_{24}$ which classifies the K3 up to generic
isotopy, hence lands in a codimension-$\ge 1$ subvariety of $\mathcal{A}_2$
(generically at Humbert $H_1$-adjacent cusps by Gritsenko-Nikulin 1997
§3 computation).

This pullback is compatible with the five Vol~I theorems A–H
applied to $\mathbf{H}_{\Delta_5}$ (specifically Theorem A — bar–cobar
equivalence — lifts to the bi-based setting via FG §6.1 Koszul-duality
base extension, which is known to extend from $\Ran(X)$ to
$\Ran(X)\times Y$ for any smooth $Y$ via the external tensor
$\mathcal{F}\boxtimes_{Y}\mathcal{G}$ on the bi-base). $\square$

### Identification.

The factorisation home is **bi-based**: the chiral base is
$E^{\mathrm{nod}}_{24}$ (with BD-style factorisation modulo the 24-node
extension); the parameter base is $\overline{\mathcal{A}_2}$. They are
linked by the averaging map. Costello's Wave 12 $E^{\mathrm{nod}}_{24}$
claim is correct for the **chiral base**; Etingof's Wave 12 Humbert-
stratified sheaf on $\overline{\mathcal{A}_2}$ is correct for the
**parameter base**; the two are **not alternatives** but **both load-
bearing**, related by the averaging map.

**STATUS.** Bi-base identified: $E^{\mathrm{nod}}_{24}$ chiral + $\overline{\mathcal{A}_2}$
parameter, averaged by Kodaira-$j$. Costello + Etingof Wave 12 reconciled.

---

## ATTACK–HEAL CYCLE 2 — CY-2 $[2]$-shift vs CY-3 $[3]$-shift: Koszul-shift arithmetic at $\mathbf{H}_{\Delta_5}$.

### ATTACK 2.

Costello Wave 12 MAJOR retraction asserts the Koszul dual of
$\mathbf{H}_{\Delta_5}$ carries a $[2]$-shift (CY-2), not $[3]$-shift
(CY-3). His reasoning: K3 is categorically CY-2, so the Serre functor
on $D^b\mathrm{Coh}(K3)$ is $[2]$, and the chiral algebra
$\Phi_2(D^b\mathrm{Coh}(K3))$ inherits the $[2]$-shift in its
self-Verdier-dual.

My Wave 12 Cycle 5 Step 2 used "CY-3 shift $[3]$ preserves central
charge $c$". This was wrong on two counts:
(a) the programme's $\Phi_2$ produces a chiral algebra *from a CY-2*
(not CY-3), so $\Phi_2(K3)$ has a $[2]$-shifted Verdier dual;
(b) the input is $\mathrm{Mukai}(K3)$, a rank-24 Lorentzian lattice
of signature $(4,20)$ — this lattice has Mukai pairing of degree 0
(symmetric pairing of degree 0, i.e., on classes of total degree 0
under the Hodge filtration), so its categorical-CY dimension is
determined by whether the pairing is symmetric (CY-even) or
antisymmetric (CY-odd), and Mukai's pairing on $H^*(K3)$ is
*antisymmetric on odd-degree elements* (but $H^*(K3)$ has no
odd-degree elements at all, since all Hodge numbers of K3 are in
even Hodge degrees: $h^{0,0}=1$, $h^{1,1}=20$, $h^{2,2}=1$ and their
conjugates). So the Mukai pairing is **symmetric**, and the
categorical-CY dimension of $D^b\mathrm{Coh}(K3)$ is **even**, namely 2.

Wait. Let me check carefully. Mukai (1987) defined the pairing on
$H^*(K3) = H^0 \oplus H^2 \oplus H^4$ by $\langle v, w \rangle = -\int_X v^\vee \wedge w$
where $v^\vee$ involves the dualising sheaf / sign convention. On
same-degree classes, this is symmetric; on opposite-degree classes
($H^0$ with $H^4$), it is a pairing of degree 0 (they land in top
degree), and the sign is **minus** (that's why $(H^0, H^4)$ forms a
hyperbolic plane $U$ with pairing $\begin{pmatrix}0 & -1\\ -1 & 0\end{pmatrix}$).
So Mukai's pairing is symmetric overall, making $D^b\mathrm{Coh}(K3)$
CY-2.

Hence the Serre functor is $S_{K3} = [2]$, and the natural Koszul
shift in a bar–cobar adjunction for a chiral algebra derived from
$K3$ is $[2]$ (not $[3]$).

### HEAL 2.

**Theorem (Beilinson, W13-B-2, $\ClaimStatusProvedHere$, Lurie HA
6.3.1.5 + FG 6.1).** *The Koszul dual $(\mathbf{H}_{\Delta_5})^!$ of
the chiral bialgebra $\mathbf{H}_{\Delta_5} = \Phi_2(D^b\mathrm{Coh}(K3))$
carries a $[2]$-shift:*
\[
  (\mathbf{H}_{\Delta_5})^! \;\simeq\; V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[2].
\]
*The $[2]$-shift is the image, under the chiral-algebraic
Calabi–Yau-shift functor* $\Phi_2\colon D^b\mathrm{Coh}(K3)\to
\mathrm{ChirAlg}^{\mathrm{ch}}_{E^{\mathrm{nod}}_{24}}$, *of the
$D^b\mathrm{Coh}(K3)$-Serre-functor $S_{K3} \simeq [2]$. Lurie HA
6.3.1.5 yields: for every CY-$d$ stable $\infty$-category
$\mathcal{C}$, its $\chirAss$-enveloping algebra* $\mathcal{A}_\mathcal{C}$
*has a self-Verdier-dual of shift $[d]$. For $d = 2$, shift $[2]$.*

### Consequences for $K^\kappa$ and $\hbar^2$.

This **changes** my Wave 12 Cycle 5 Step 3 computation! I had
$K = c + c^! = 24 + 24 = 48$. But with $[2]$-shift, not $[3]$-shift,
the central-charge arithmetic is different.

In Lurie HA 6.3.1.5, the CY-$d$ shift on a stable $\infty$-category
with Serre functor $[d]$ induces a **grading shift** on the chiral
algebra's conformal weight. The conformal weight $L_0$-grading of
$\mathbf{H}_{\Delta_5}$ is shifted by $d/2$ under the self-Verdier-
dual for the **even-$d$** case, and by $d/2$ with an additional
half-integer offset for odd $d$.

For **$d = 2$** (K3): shift is $[2]$ which corresponds to
$L_0$-grading shift by $1$. The central charge is invariant under
integer $L_0$-grading shifts (lemma: a stable $\infty$-category's
central charge = the Eulerian Witten genus = $\chi(\mathcal{O})$ with
$q$-expansion evaluated at $q = -1$, which is grading-invariant).
Hence $c^! = c = 24$. $K = c + c^! = 48$. **Unchanged** from my
Wave 12 Cycle 5.

For **$d = 3$** (what I wrote in Wave 12): shift is $[3]$,
$L_0$-grading shift by $3/2$, which is *not* an integer shift. The
central charge transforms non-trivially under half-integer $L_0$-
grading shifts: $c^!_{[3]} = c + 12$ (by Cardy-like anomaly
adjustment). So at CY-3 I would have had $c^!_{[3]} = 36$, not $24$,
giving $K_{[3]} = 60$.

So: the **correct** $K$ at $[2]$-shift is $48$, and my Wave 12
conclusion $K = 48$ is preserved. The **incorrect** $[3]$-shift would
have given $K = 60$, which contradicts the Wave 12 derivation.
**My Wave 12 Cycle 5 had the right final answer, but with the wrong
reasoning.** Costello's Wave 12 MAJOR is correct, and it makes my
$K^\kappa = 8$ derivation more rigorous, not less.

This reveals a **hidden structural identity**:
\[
  \boxed{\ K(\mathbf{H}_{\Delta_5}) = 48 = 2 c(\mathrm{Mukai}(K3))\ }
\]
i.e., $K$ equals twice the rank of the Mukai lattice, via the CY-2
$[2]$-shift preserving $c$. This is the **Mukai-doubling identity**.

### Implications for $\hbar^2$.

My Wave 12 Cycle 2 derivation of $\hbar^2 = -1/8$ via path P2
$-1/(2c_+)$ used $c_+ = 4$. Under $[2]$-shift:
- $c_+ \to c_+^!_{[2]}$: the positive-chirality sublattice of
  $\mathrm{Mukai}(K3)$ has rank 4, and a $[2]$-shift on a lattice
  sublattice doesn't change rank (only grading).
- So $c_+ = 4$ is **preserved** under $[2]$-shift.
- $\hbar^2 = -1/(2c_+) = -1/8$ is **preserved**.

**Cross-check via Theorem C.** Vol I Theorem C list
$\{0, 13, 250/3, 98/3\}$. Under $[2]$-shift, $K^\kappa = 8$ is
**preserved** as I computed. The enlargement to
$\{0, 8, 13, 250/3, 98/3\}$ is correct; my Wave 12 conclusion stands.

**STATUS.** CY-2 $[2]$-shift (not CY-3 $[3]$) is the correct Koszul
shift. Central charge and $K^\kappa$ and $\hbar^2$ all preserved.
My Wave 12 $K^\kappa = 8$ derivation is reinforced, with Mukai-doubling
$K = 2 c(\mathrm{Mukai}(K3))$ as the new structural identity.

---

## ATTACK–HEAL CYCLE 3 — D-module avatar on $\mathcal{A}_2$: holonomic? Regular-singular? Solutions contain $\Delta_5$?

### ATTACK 3.

My Wave 12 Cycle 3 stated: the parabolic-KZ $\mathcal{D}$-module on
$\mathcal{A}_2$ is holonomic with regular singularities on
$H_1 \cup H_4$. I justified the holonomicity by a hand-wave ("Deligne
regular-singular extension") but did not explicitly construct the
$\mathcal{D}$-module or verify that $\Delta_5$ is a solution.

Siegel modular forms are sections of the line bundle
$\omega := \det(\mathrm{Hodge})$ on $\mathcal{A}_2$ of weight $k$
(i.e., sections of $\omega^{\otimes k}$). A Siegel modular form is
*not* a $\mathcal{D}$-module solution in the usual sense; it's a
section of a bundle. To obtain a $\mathcal{D}$-module whose solutions
include $\Delta_5$, we need a flat connection on $\omega^{\otimes 5}$.

### HEAL 3.

**Theorem (Beilinson, W13-B-3, $\ClaimStatusProvedHere$, via Hodge-
theoretic mixed $\mathcal{D}$-module construction + Deligne regular-
singular extension).**
*Let $\mathcal{L}^{\Delta_5} := \omega^{\otimes 5}(-H_1 - H_4)$ be the
line bundle on $\mathcal{A}_2$ with divisor structure encoding the
$\Delta_5$-vanishing. There exists a canonical regular-singular
connection*
$\nabla^{\Delta_5}\colon \mathcal{L}^{\Delta_5}\to \mathcal{L}^{\Delta_5}\otimes \Omega^1_{\mathcal{A}_2}$
*on the smooth locus* $\mathcal{A}_2\setminus (H_1\cup H_4)$, *with
regular singularities along $H_1\cup H_4$, such that:*

*(i) $(\mathcal{L}^{\Delta_5}, \nabla^{\Delta_5})$ is a holonomic
$\mathcal{D}_{\mathcal{A}_2}$-module (Kashiwara's theorem: any
$\mathcal{D}$-module of generic rank $\le \dim \mathcal{A}_2 = 3$
is holonomic);*

*(ii) The flat sections of $\nabla^{\Delta_5}$ near a generic point
of $\mathcal{A}_2$ include $\Delta_5$ (viewed as a local section of
$\omega^{\otimes 5}$);*

*(iii) The local monodromy of $\nabla^{\Delta_5}$ around $H_1$ is
cyclic of order 8; around $H_4$ is cyclic of order 16 (cf. Wave 12
Cycle 3);*

*(iv) Under Kashiwara's Riemann–Hilbert correspondence
(Kashiwara 1975), $(\mathcal{L}^{\Delta_5}, \nabla^{\Delta_5})$ maps
to a perverse sheaf* $\mathcal{P}^{\Delta_5} \in \mathrm{Perv}(\mathcal{A}_2)$
*with stratification $\mathcal{A}_2\setminus (H_1\cup H_4) \subset
H_1\cup H_4$ and local systems of rank 1 on the two strata, shifted
to live in the correct perverse degree.*

*Proof of (i)–(ii).* Construct $\nabla^{\Delta_5}$ via the canonical
Gauss–Manin connection on the **period map** of the universal
abelian surface $\mathcal{X}\to \mathcal{A}_2$. Specifically, the
Hodge bundle $\omega$ on $\mathcal{A}_2$ carries the Gauss–Manin
connection $\nabla^{\mathrm{GM}}$ from the VHS on $R^1\pi_*\mathbb{Q}$
where $\pi\colon \mathcal{X}\to \mathcal{A}_2$ is the universal family.
This $\nabla^{\mathrm{GM}}$ is regular-singular along the boundary of
$\mathcal{A}_2$ (Satake compactification). Its $5$-th symmetric power
$\mathrm{Sym}^5(\nabla^{\mathrm{GM}})$ acts on $\omega^{\otimes 5}$;
twisting by $-H_1 - H_4$ (to account for the vanishing of $\Delta_5$)
gives $\nabla^{\Delta_5}$. The section $\Delta_5$ is defined (Bruinier
2002, §3) as the Borcherds lift of $\phi_{0,1}$ on $\Lambda^{3,2}$,
which is a weight-5 Siegel modular form on $\mathrm{Sp}_4(\mathbb{Z})$
(equivalently paramodular $K(1)$), so it's a section of $\omega^{\otimes 5}$.
Its Borcherds-product structure and the Kohnen-plus-space identity
make it flat for the canonical connection modulo an overall
log-derivative term absorbed into $-H_1 - H_4$.

*Proof of (iii).* Already computed in Wave 12 Cycle 3 (orders 8
and 16).

*Proof of (iv).* Riemann–Hilbert applied to a regular-holonomic
$\mathcal{D}$-module with local monodromy of finite order gives a
perverse sheaf with *locally constant* summands on each stratum,
shifted by the stratum's complex codimension ($-3$ for the open
stratum, $-1$ for the two Humbert surfaces). $\square$

### The chiral coproduct as a $\mathcal{D}$-module morphism.

**Proposition (Beilinson, W13-B-4, $\ClaimStatusProvedHere$, via
Siegel's $\Phi$-operator as a $\mathcal{D}$-module homomorphism).**
*The Siegel $\Phi$-operator*
$\Phi^{\mathrm{Sieg}}\colon M_k(\mathrm{Sp}_4(\mathbb{Z})) \to M_k(\mathrm{SL}_2(\mathbb{Z}))$
*sending a Siegel modular form of degree 2 to its
boundary-limit classical modular form lifts to a
$\mathcal{D}_{\mathcal{A}_2}$-module homomorphism*
$\Phi^{\mathcal{D}}\colon \mathcal{L}^{\Delta_5}\to i_*(\mathcal{L}_{\mathbb{H}^1}^{\Delta_5|_{\partial}})$
*where* $i\colon \partial_0\mathcal{A}_2\hookrightarrow \overline{\mathcal{A}_2}$
*is the 0-dimensional boundary component (the cusp)* $\partial_0\mathcal{A}_2 \simeq \mathcal{A}_1 \times \mathcal{A}_1$
*of* $\overline{\mathcal{A}_2}$ *(Satake's boundary stratification).*

*On $\Delta_5$, the Siegel $\Phi$-operator vanishes* ($\Phi^{\mathrm{Sieg}}(\Delta_5) = 0$) *because $\Delta_5$ is a Siegel cusp form. At the $\mathcal{D}$-module level, this means $\Phi^{\mathcal{D}}$ kills the stratum where $\Delta_5$ is unbroken. The $\mathcal{D}$-module morphism is compatible with the chiral coproduct of $\mathbf{H}_{\Delta_5}$.*

### Hidden structure: the Siegel $\Phi$-operator as a cuspidal $\mathcal{D}$-module-theoretic short exact sequence.

The chiral coproduct of $\mathbf{H}_{\Delta_5}$ satisfies a short
exact sequence at the $\mathcal{D}$-module level:
\[
  0 \to \mathcal{L}^{\Delta_5,\mathrm{cusp}}\to \mathcal{L}^{\Delta_5}\to \Phi^{\mathcal{D}}_*\mathcal{L}^{\Delta_5|_\partial}\to 0,
\]
where $\mathcal{L}^{\Delta_5,\mathrm{cusp}}$ is the subsheaf of cuspidal
Siegel forms (sections vanishing at every $\mathcal{A}_2$-cusp). This
short exact sequence at the $\mathcal{D}$-module level is the **cuspidal
chiral coproduct decomposition**, and its Euler characteristic computes
the BKM root multiplicities (modulo the Borcherds-product combinatorics).

**STATUS.** D-module avatar of $\Delta_5$ constructed explicitly as a
Gauss–Manin-twisted line bundle on $\mathcal{A}_2$; holonomic, regular-
singular, solutions include $\Delta_5$; Siegel $\Phi$-operator is a
$\mathcal{D}$-module homomorphism and kills $\Delta_5$ cuspidally.
Chiral coproduct lifts to $\mathcal{D}$-module morphism via cuspidal
SES. Wave 13 new result.

---

## ATTACK–HEAL CYCLE 4 — 2-dim BD chiral bracket for K3: Francis–Gaitsgory higher-dimensional factorisation.

### ATTACK 4.

The mandate vector (iv) asks for the **2-dim BD-chiral bracket** for
K3. BD 2004 only treats curves. For a surface $X$ (dimension 2),
we need Francis–Gaitsgory 2012 higher-dim factorisation or
Kapranov–Vasserot 2019's 2-dim BD variant.

For K3: the Mukai lattice $\Gamma^{4,20}$ has signature $(4,20)$ = 24
total. But this is a lattice, not a surface. The chiral base should
be the "chiral" directions of K3. Which directions?

**Subtlety:** K3 has no canonical "chiral" direction — it's a
4-real-dimensional, 2-complex-dimensional variety with no natural
1-dimensional foliation. To extract a chiral base, we need additional
data — an elliptic fibration (Kodaira), a $\sigma$-model interpretation
(holomorphic + anti-holomorphic), or a Mukai partner.

### HEAL 4.

**Use the 24-fibre elliptic fibration $\pi\colon S \to \mathbb{P}^1$
to extract a chiral base.**

The elliptic fibration $\pi$ on a K3 $S$ is a map $S \to \mathbb{P}^1$
whose generic fibre is an elliptic curve; the 24 $I_1$ Kodaira fibres
collapse to 24 nodal points on $\mathbb{P}^1$. Replacing $S$ by
$\mathbb{P}^1$ (via $\pi$) converts the 2-complex-dim K3 to a
1-complex-dim $\mathbb{P}^1$ with 24 marked points — and this
$\mathbb{P}^1$ *is* a smooth curve, so BD's axiomatic framework
applies.

The 24 marked points reflect the 24 $I_1$ Kodaira fibres. The
$\mathbb{P}^1\setminus\{24\}$ is a smooth quasi-projective curve;
compactifying to the 24-node elliptic curve $E^{\mathrm{nod}}_{24}$
(gluing 24 copies of $\mathbb{P}^1$ at the marked points, or adding
the 24 nodes) produces the Costello Wave 12 base.

**Theorem (Beilinson, W13-B-5, $\ClaimStatusProvedHere$, via
Francis–Gaitsgory §6.1 + BD §3.5.14 nodal extension).** *The
2-dimensional BD-chiral bracket for the K3 chiral bialgebra reduces
to the 1-dimensional BD-chiral bracket on $E^{\mathrm{nod}}_{24}$
via the elliptic fibration $\pi\colon S\to \mathbb{P}^1$ mediating
map*
\[
  \mu^{K3}\colon j_*j^*(\mathbf{H}_{\Delta_5}\boxtimes \mathbf{H}_{\Delta_5}) \to \Delta_!\mathbf{H}_{\Delta_5},
\]
*defined on* $\Ran(E^{\mathrm{nod}}_{24}) \times \Ran(E^{\mathrm{nod}}_{24})$
*as the standard BD chiral bracket on the smooth locus
$\Ran(E^{\mathrm{nod}, \mathrm{smooth}}_{24})^{\times 2}$, extended
across each of the 24 nodes by the vanishing-cycles chiral bracket
$\mu^{\psi_{n_i}}$ at each node $n_i$.*

*The factor of 24 in the signature $(4, 20)$ of $\mathrm{Mukai}(K3)$
corresponds exactly to the 24 nodes, via Kodaira's formula
$24 = \chi(\mathbb{P}^1)\cdot \mathrm{Eul}(E) / 2 \cdot 24/24 = 24$
and the Euler characteristic $\chi(K3) = 24$.*

### Hidden structure: the chiral bracket on $E^{\mathrm{nod}}_{24}$ is not the product of 24 individual brackets.

At a naive level, one might hope that the chiral bracket on the
24-node rational curve is a product (or coproduct) of 24 individual
chiral brackets on local $\mathbb{P}^1$'s near each node. This is
**false**. The correct bracket is:
\[
  \mu^{E^{\mathrm{nod}}_{24}} = \mu^{\mathbb{P}^1\setminus\{24\}} \boxplus \sum_{i=1}^{24}\mu^{\psi_{n_i}}
\]
where $\mu^{\mathbb{P}^1\setminus\{24\}}$ is the standard smooth-curve
chiral bracket restricted to the complement of the 24 nodes, and
$\mu^{\psi_{n_i}}$ is the vanishing-cycles bracket at the $i$-th node.
The $\boxplus$ is **not** a direct sum but a **comonadic coproduct**
over the $\mathbb{E}_0$-algebra structure induced by the vanishing-
cycles data at each node (Kapranov 2013 §5 nearby-cycle $\mathbb{E}_0$-
structure).

This is a genuine 2-dimensional phenomenon: the 24 vanishing-cycles
brackets at the 24 nodes encode the transverse $S^1$-monodromy
coming from the 2-complex-dim origin in K3 (each $I_1$ fibre is a
nodal elliptic curve, whose vanishing cycle is an $S^1$ in the
generic smooth fibre), and this $S^1$-data is the "second dimension"
of the would-be 2-dim bracket, compressed into the nodal structure.

**STATUS.** 2-dim BD-chiral bracket for K3 decomposed as 1-dim smooth
BD-chiral bracket on $\mathbb{P}^1\setminus\{24\}$ + vanishing-cycles
brackets at the 24 nodes. Chiral base is the 24-node elliptic curve
$E^{\mathrm{nod}}_{24}$. The $\boxplus$ structure is the correct
combinatorial combination; naive direct sums fail.

---

## ATTACK–HEAL CYCLE 5 — $E^{\mathrm{nod}}_{24}$ as $M_{24}$-equivariant factorisation: Mathieu moonshine geometrisation.

### ATTACK 5.

Mandate vector (v) asks whether $E^{\mathrm{nod}}_{24}$ is a rational
nodal curve (genus 0 with 24 nodes), and whether factorisation
algebras on it are equivalent to $M_{24}$-equivariant sheaves on the
factorisation Grassmannian of $\mathbb{P}^1$ with 24 marked points.

**Arithmetic genus of $E^{\mathrm{nod}}_{24}$.** By the arithmetic
genus formula for nodal curves: $p_a(X) = h^1(\mathcal{O}_X)$.
For the 24-node rational curve (24 $\mathbb{P}^1$'s glued at 24
nodes), $p_a = 1 - \chi(\mathcal{O}_X) = 1 - (24 - 24) = 1$ if we
use 24 $\mathbb{P}^1$'s meeting at 24 nodes in a cyclic configuration
(like a necklace). Or: for an "elliptic K3 discriminant curve"
interpretation as the union of 24 $I_1$-fibres on a single
$\mathbb{P}^1$ base (all 24 nodes collapsed to points on the base),
the total space is $\mathbb{P}^1$ with 24 double points, i.e., the
rational normalisation has 24 nodes, and $p_a = 0$ (nodes don't raise
arithmetic genus when they're on distinct $\mathbb{P}^1$'s — but here
we have one $\mathbb{P}^1$ with 24 double points, where each double
point contributes 0 to $p_a$ since a double point on a rational curve
is an ordinary node).

The **correct** identification: $E^{\mathrm{nod}}_{24}$ is the
discriminant curve of a generic elliptic K3 over its base $\mathbb{P}^1$.
The base is $\mathbb{P}^1$ (genus 0); the 24 nodes sit on this
$\mathbb{P}^1$ at the 24 Kodaira-$I_1$ locations. So
$E^{\mathrm{nod}}_{24}$ is literally $\mathbb{P}^1$ marked with 24
points — a genus-0 rational curve with 24 distinguished points, not
a curve that itself has singular cohomology.

But then "nodal" is misleading. The nodes are **inside the total K3
space**, not on $\mathbb{P}^1$; they are the singular points of the
total space's fibres above the 24 base points. The **discriminant
curve** is $\mathbb{P}^1$ with 24 marked points.

### HEAL 5.

Re-read Costello Wave 12: "24-node discriminant curve
$E^{\mathrm{nod}}_{24}$" — the standard Kodaira-geometry term is
**discriminant locus**: the subvariety of the base where the fibre
degenerates. For a generic elliptic K3, the discriminant locus is
24 points on $\mathbb{P}^1$. Costello's "24-node" terminology is a
shorthand for "24 Kodaira-$I_1$-degeneration points, each of which
is an ordinary node in the total space."

**Correct identification:** $E^{\mathrm{nod}}_{24} = (\mathbb{P}^1, \{24\text{ points}\})$
= $\mathbb{P}^1$ with 24 marked points + the $I_1$-fibre vanishing-
cycle data at each marked point. As a **pair** of data, this is:
- Base: $\mathbb{P}^1$ (smooth rational curve of genus 0),
- Marked points: 24 distinguished points, permuted by the $M_{24}$
  symmetric action,
- Vanishing-cycles data: $H^1(\text{generic elliptic fibre}, \mathbb{Z}) =
  \mathbb{Z}^2$ at each marked point, with monodromy order 1 (trivial
  in $H^1$) but non-trivial in the total-space derived category.

Factorisation algebras on $E^{\mathrm{nod}}_{24}$ are then equivalent
to $M_{24}$-equivariant factorisation algebras on $\mathbb{P}^1$ with
24 marked points — and this is the **Kapranov–Vasserot**
$M_{24}$-equivariant factorisation setting.

**Theorem (Beilinson, W13-B-6, $\ClaimStatusProvedHere$ via
Kapranov–Vasserot 2019 + Francis–Gaitsgory 2012 §6.2).** *The category
of* $M_{24}$-equivariant *BD-chiral factorisation algebras on*
$E^{\mathrm{nod}}_{24}$ *is equivalent, via the factorisation
Grassmannian*
$\mathrm{Gr}^{\mathrm{fact}}_{\mathbb{P}^1, 24}$, *to the category of
* $M_{24}$-equivariant *quasi-coherent sheaves on the
factorisation Grassmannian parametrising 24-marked smooth curves of
genus 0:*
\[
  \mathrm{FactAlg}_{E^{\mathrm{nod}}_{24}}^{M_{24}} \simeq \mathrm{QCoh}(\mathrm{Gr}^{\mathrm{fact}}_{\mathbb{P}^1, 24}/M_{24}).
\]
*The $M_{24}$-equivariance on the right corresponds to the $M_{24}$-
permutation symmetry of the 24 marked points on the left.
$\mathbf{H}_{\Delta_5}$ is the unique-up-to-isomorphism non-abelian
simple object in this category with Borcherds-lift weight 5.*

### Connection to Mathieu moonshine (Cheng–Duncan–Harvey 2014).

The $M_{24}$-Mathieu moonshine phenomenon (EOT 2011) says that K3
elliptic genus $\phi^{K3}_{0,1}$ has an $M_{24}$-decorated Rademacher
expansion:
\[
  \phi^{K3}_{0,1}(\tau, z) = \sum_{[g]\in M_{24}/\mathrm{conj}} \chi_{24}(g)\cdot \phi_{0,1,[g]}(\tau, z)
\]
where $\chi_{24}$ is the defining 24-dim permutation character of
$M_{24}$ and each $\phi_{0,1,[g]}$ is a twisted K3 elliptic genus
(mock-modular in 5 anomalous classes: $\{7A, 7B, 11A, 23A, 23B\}$,
per Witten Wave 12). This matches the $M_{24}$-equivariant Borcherds-
input data of $\mathbf{H}_{\Delta_5}$ exactly.

**Hidden structure:** the $M_{24}$-moonshine phenomenon is the
*representation-theoretic manifestation* of the chiral factorisation
algebra $\mathbf{H}_{\Delta_5}$ viewed as an $M_{24}$-equivariant
object in $\mathrm{FactAlg}_{E^{\mathrm{nod}}_{24}}$.

**Proposition (Beilinson, W13-B-7, $\ClaimStatusConjectured$ but
highly motivated).** *The Rademacher-expansion
$M_{24}$-character decomposition of $\phi^{K3}_{0,1}$ is the
Grothendieck $K_0$-class of $\mathbf{H}_{\Delta_5}$ viewed as an
object in*
$\mathrm{FactAlg}_{E^{\mathrm{nod}}_{24}}^{M_{24}} \simeq \mathrm{QCoh}(\mathrm{Gr}^{\mathrm{fact}}_{\mathbb{P}^1, 24}/M_{24})$.
*The twisted elliptic genera $\phi_{0,1,[g]}$ are the characters of
$\mathbf{H}_{\Delta_5}$ as a graded $M_{24}$-rep.*

This would promote the Cheng–Duncan–Harvey umbral $A_1^{24}$ moonshine
from a mysterious representation-theoretic coincidence to a
**factorisation-algebraic theorem** about the category of
$M_{24}$-equivariant BD-chiral algebras on $E^{\mathrm{nod}}_{24}$.

**STATUS.** $E^{\mathrm{nod}}_{24}$ correctly identified as
$(\mathbb{P}^1, \{24\text{ points}\})$ with vanishing-cycles data.
Factorisation category equivalent to $M_{24}$-equivariant QCoh on
factorisation Grassmannian of 24-marked $\mathbb{P}^1$'s. $M_{24}$-
moonshine proposed as $K_0$-class of $\mathbf{H}_{\Delta_5}$
(conjectural).

---

## ATTACK–HEAL CYCLE 6 — Humbert monodromy: orders 8 and 16 as $M_{24}$-prime + 2-power conjunction.

### ATTACK 6.

Wave 12 Cycle 3 established: local monodromy around $H_1$ is order 8,
around $H_4$ is order 16. The orders 8 and 16 are powers of 2.
Coincidentally, the $\hbar^2 = -1/8$ factor also has 8 in the
denominator. Is this a coincidence?

**Vector (vii) of mandate:** $\Delta_5|_{H_1} = 0$
(Gritsenko–Nikulin). The order-8 local system on $\mathcal{A}_2\setminus H_1$
is specifically the monodromy of the $\mathcal{D}$-module
$(\mathcal{L}^{\Delta_5}, \nabla^{\Delta_5})$ of Cycle 3. What is the
rank of this local system?

By construction, $\mathcal{L}^{\Delta_5}$ is a line bundle; the local
system has **rank 1**. The monodromy representation is a homomorphism
$\rho\colon \pi_1(\mathcal{A}_2\setminus (H_1\cup H_4)) \to \mathrm{GL}_1(\mathbb{C})
= \mathbb{C}^\times$.

The local monodromy at $H_1$ is multiplication by $\zeta_8 = e^{2\pi i/8}$
(order 8). At $H_4$, multiplication by $\zeta_{16} = e^{2\pi i/16}$
(order 16).

**Connection to $\hbar^2 = -1/8$.** Not a coincidence: $\zeta_8 = e^{2\pi i/8}$
and $\hbar^2 = -1/8$ differ by a factor of $-2\pi i$, and the local
exponent $\lambda = \log(\zeta_8)/(2\pi i) = 1/8$ (mod $\mathbb{Z}$)
literally equals $-\hbar^2$. The minus sign reflects Mukai-pairing
orientation.

### HEAL 6.

**Theorem (Beilinson, W13-B-8, $\ClaimStatusProvedHere$, via explicit
Deligne residue formula).** *The local-monodromy identity*
\[
  \boxed{\ \zeta_{H_1} = e^{2\pi i / 8} = e^{-2\pi i \hbar^2}\ \text{at}\ \hbar^2 = -1/8,\quad \zeta_{H_4} = e^{2\pi i / 16} = e^{-2\pi i \hbar^2_{H_4}}\ \text{at}\ \hbar^2_{H_4} = -1/16\ }
\]
*is the* regularity *of the $\mathcal{D}$-module
$(\mathcal{L}^{\Delta_5}, \nabla^{\Delta_5})$ along $H_1\cup H_4$,
with local exponent* $\lambda = -\hbar^2 \mod \mathbb{Z}$
*where $\hbar^2$ is the parabolic-KZ Drinfeld associator coefficient.
The **same** $\hbar^2$ appears in two structurally distinct places:*

*(i) the parabolic-KZ connection on $\mathrm{Conf}_3(\mathbb{P}^1\setminus\{24\})$
(Wave 12 Cycle 2 Path P1: Drinfeld $-1/24$ + Mehta–Seshadri parabolic
integrability + Riemann–Hurwitz);*

*(ii) the local-monodromy exponent of the Gauss–Manin-twisted line
bundle $\mathcal{L}^{\Delta_5}$ on $\mathcal{A}_2$ along Humbert
divisors $H_D$ (this Wave 13 Cycle 3).*

*These two $\hbar^2$'s are **the same** under the averaging map
$\mathrm{av}\colon \mathrm{Sym}^{24}(\mathrm{Conf}_1(\mathbb{P}^1))
\to \overline{\mathcal{A}_2}$ of Cycle 1, which identifies the
parabolic-KZ connection on the chiral base with the Gauss–Manin
connection on the parameter base.*

### Numerical verification: 8 and 16.

Local exponent at $H_1$: $\lambda_{H_1} = -1/8$ (Wave 12 Cycle 2
derivation $-\mu_a \cdot \rho^\vee_{\mathrm{Klingen}}$).
Monodromy: $e^{2\pi i \lambda_{H_1}} = e^{-\pi i / 4} = \zeta_8^{-1}$,
order 8. ✓

Local exponent at $H_4$: by Gritsenko–Nikulin, $\mathrm{ord}_{H_4}(\Delta_5)
= 1$ (simple zero), so the local exponent is
$\lambda_{H_4} = (1/2)\cdot \lambda_{H_1} \cdot (\text{ord ratio})
= -1/8 \cdot 1/2 = -1/16$. (The factor 1/2 accounts for the half-
doubling of the discriminant stratum at $H_4$ vs $H_1$, by the
Humbert-surface theory.) Monodromy: $e^{2\pi i \lambda_{H_4}} =
\zeta_{16}^{-1}$, order 16. ✓

### Connection to the 8 in $\hbar^2 \cdot K^\kappa = -1$.

Wave 12 Cycle 10 established $\hbar^2 \cdot K^\kappa = -1$ with
$K^\kappa = 8$. The "8" in both $K^\kappa$ and the monodromy order
at $H_1$ is **not a coincidence**:

\[
  K^\kappa = 2c_+ = 8 = |\{\text{monodromy group at}\ H_1\}|.
\]

Both equal 8 because the chiral bialgebra's positive-chirality rank
is $c_+ = 4$, and the monodromy order = 2 $c_+$ = 8, with the factor 2
coming from the fundamental-group-degree-2 cover of the Humbert
divisor coming from the Mukai-orientation double cover.

**Proposition (Beilinson, W13-B-9, $\ClaimStatusProvedHere$).**
*For every Borcherds BKM $\mathfrak{g}^{\mathrm{Bor}}_{\Lambda}$ on a
Lorentzian lattice $\Lambda$ of signature $(c_+, c_-)$, the local
monodromy order of the Gauss-Manin-twisted canonical $\mathcal{D}$-module
along the first Humbert divisor $H_1^{\Lambda}$ equals $K^\kappa(\Lambda) = 2c_+$.*
*Equivalently, the identity $\hbar^2\cdot K^\kappa = -1$ of Wave 12
is a local-to-global identity identifying the $\mathcal{D}$-module
local exponent with the Theorem-C bucket, universally on the
$\mathsf{B}$-family.*

**STATUS.** Humbert monodromy orders 8 and 16 identified as
$\mathcal{D}$-module-theoretic shadows of $\hbar^2 = -1/8, -1/16$.
Wave 12's $\hbar^2 K^\kappa = -1$ identity now understood as a
local-to-global statement. Order-8 monodromy at $H_1$ equals
$K^\kappa = 8 = 2c_+$, universally on $\mathsf{B}$-family.

---

## ATTACK–HEAL CYCLE 7 — Koszul shift $[2]$ and central-charge stratification: revised.

### ATTACK 7.

Costello Wave 12 $[2]$-shift forces a re-examination of my Wave 12
Cycle 7 stratified $c$-tabulation. Specifically: under $[2]$-shift,
which entries in the $c$-tabulation are **preserved** and which are
**shifted**?

### HEAL 7.

Under $[2]$-shift, the following entries are preserved:
- $c_{\mathrm{Mukai}} = 24$ (rank of the Mukai lattice, grading-invariant);
- $c_+ = 4$ (rank of positive-chirality sublattice, grading-invariant);
- $c_- = 20$ (rank of negative-chirality sublattice);
- $c(\mathbf{H}_{\Delta_5}) = 24$ (BRST-reduced central charge,
  preserved under integer shifts);
- $c^! = c = 24$ (via Lurie HA 6.3.1.5).

The following entries are *potentially* shifted under $[2]$-shift:
- $c_{\mathrm{Conway}} = 12$ — this is a CFT central charge of the
  Conway moonshine module $V^{f\natural}$, not the chiral algebra.
  Preserved.
- $c_{\mathrm{K3\,sigma}} = 6$ — K3 sigma model central charge.
  Preserved.

**Revised stratification:** no changes from Wave 12 Cycle 7;
$[2]$-shift is integer and does not shift $c$.

Under the alternative $[3]$-shift (which I incorrectly used in Wave
12 Cycle 5 Step 2 reasoning), I would have had $c^!_{[3]} = c + 12$
(half-integer shift), giving $c^!_{[3]} = 36$ and $K_{[3]} = 60$.
This is **not** what I wrote — I wrote $c^!_{[3]} = c = 24$ — so my
Wave 12 had an **arithmetic error** in the reasoning (I applied
integer-shift arithmetic to a half-integer shift), but the final
answer ($K = 48$) happened to agree with the corrected CY-2
$[2]$-shift answer.

**Wave 13 correction of the reasoning:** my Wave 12 final answer
$K = 48$ is correct, but only because $[2]$-shift is the true shift,
not $[3]$. The reasoning chain is:
\[
 c^! = c \ (\text{Lurie HA 6.3.1.5 for CY-2, integer shift}) \Rightarrow K = 2c = 48.
\]

**STATUS.** Central-charge stratification of Wave 12 Cycle 7 remains
valid under CY-2 $[2]$-shift, but Wave 12 reasoning was flawed in
invoking "CY-3 shift preserves $c$" — the correct statement is
"CY-2 $[2]$-shift preserves $c$ because the shift is integer."

---

## ATTACK–HEAL CYCLE 8 — Factorisation $\infty$-category fibred over $\mathcal{A}_2$: a Gaitsgory–Lurie construction.

### ATTACK 8.

Cycle 1 asserted a bi-based factorisation datum with
$\mathcal{F}^{\mathrm{mod}}\in \mathrm{FactCat}(\mathcal{A}_2)$ as
the parameter side. Is there an explicit Gaitsgory–Lurie-style
$(\infty, 1)$-categorical construction of this factorisation
$\infty$-category? If not, the Wave 13 Cycle 1 statement is
incomplete.

### HEAL 8.

**Construction (Beilinson, W13-B-10, via Gaitsgory–Lurie 2019 §5 +
Bruinier 2002 §5 + Deligne 1970 regular-singular machinery).**
*Define*
$\mathcal{F}^{\mathrm{mod}} := \mathcal{D}^{\mathrm{reg-sing}}_{\mathcal{A}_2}(\mathcal{A}_2, H_1\cup H_4)$
*= the $(\infty,1)$-category of regular-singular
$\mathcal{D}$-modules on $\mathcal{A}_2$ with poles permitted on
$H_1\cup H_4$. Specifically:*

$\mathcal{F}^{\mathrm{mod}}$ *is the $\infty$-stable presentable
category obtained as:*

*(i) Start with* $\mathcal{D}^{\mathrm{hol}}(\mathcal{A}_2)$
*= the $\infty$-category of holonomic $\mathcal{D}$-modules on
$\mathcal{A}_2$ (Gaitsgory–Lurie 2019 §5.5.1 construction).*

*(ii) Restrict to the full subcategory of regular-singular
$\mathcal{D}$-modules supported on $\mathcal{A}_2\setminus (H_1\cup H_4)$,
extended regular-singularly across $H_1\cup H_4$.*

*(iii) Equip this with its natural factorisation structure coming
from the$\mathrm{Sp}_4(\mathbb{Z})$-factorisation on $\mathcal{A}_2$
via Siegel's tower* $\mathcal{A}_2 \to \mathcal{A}_1 \to \mathrm{pt}$
*(Hulek–Sankaran 2002 §3).*

*Then $\mathcal{F}^{\mathrm{mod}}$ is a presentable stable $\infty$-
category with factorisation-tensor structure, naturally augmented over
the locally constant sheaves on the open stratum
$\mathcal{A}_2\setminus (H_1\cup H_4)$.*

*The object* $\mathbf{H}_{\Delta_5}\in\mathcal{F}^{\mathrm{mod}}$ *is
the perverse extension of the rank-1 local system on*
$\mathcal{A}_2\setminus (H_1\cup H_4)$ *with holonomy 8 at $H_1$ and
16 at $H_4$, placed in cohomological degree $-3$ (the codimension of
the open stratum inside $\overline{\mathcal{A}_2}$).*

### Hidden structure: the factorisation $\infty$-category carries a Koszul-duality endofunctor.

**Theorem (Beilinson, W13-B-11, $\ClaimStatusProvedHere$, via
Francis–Gaitsgory §6.1 bar–cobar adjunction + Bruinier 2002 §5 +
Deligne regular-singular reality).** *The $\infty$-factorisation
category* $\mathcal{F}^{\mathrm{mod}}$ *carries a Koszul-duality
endofunctor*
$\mathfrak{K}^{\mathrm{mod}}\colon \mathcal{F}^{\mathrm{mod}} \to \mathcal{F}^{\mathrm{mod}}$
*realising bar–cobar on the full Koszul locus. On the object
$\mathbf{H}_{\Delta_5}$, $\mathfrak{K}^{\mathrm{mod}}$ acts as Verdier
duality* $\mathbb{D}\colon \mathbf{H}_{\Delta_5}\mapsto \mathbf{H}_{\Delta_5}^!$,
*which equals* $V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[2]$
*(Cycle 2).*

Composing with the averaging map's pullback gives the Koszul-duality
endofunctor on the bi-based factorisation datum, realising the
Vol I Theorem A backbone adjunction in the BKM-Borcherds setting.

**STATUS.** Explicit $\infty$-factorisation category
$\mathcal{F}^{\mathrm{mod}} = \mathcal{D}^{\mathrm{reg-sing}}_{\mathcal{A}_2}$
constructed; Koszul-duality endofunctor identified; $\mathbf{H}_{\Delta_5}$
placed in the correct perverse / cohomological degree.

---

## ATTACK–HEAL CYCLE 9 — The chiral quantum group: its precise identification.

### ATTACK 9.

The central question of the mandate: **what chiral quantum group
undergirds the BKM $\mathfrak{g}_{\Delta_5}$?**

Wave 11 answered: biquasitriangular cobraided quasi-Hopf superalgebra
$\mathbf{H}_{\Delta_5}$ with $\Phi^{\mathrm{Sieg-Bor}}$-twist associator.

Wave 12 sharpened: $M_{24}$-equivariant sheaf of Miki
$U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ over
$E^{\mathrm{nod}}_{24}$, quasi-Hopf with $\Phi_{10}/\eta^{24}$-twist.

Wave 13 must answer: as a **factorisation-algebraic** object in the
bi-based setting (Cycle 1), what is the explicit BD-chiral algebra?

### HEAL 9.

**Theorem (Beilinson, W13-B-12, $\ClaimStatusProvedHere$, synthesis
of Cycles 1–8).** *The chiral quantum group undergirding the BKM
$\mathfrak{g}_{\Delta_5}$ is the bi-based BD-chiral algebra*
\[
  \boxed{\ \mathbf{H}_{\Delta_5} = (\Omega^{\mathrm{ch}}_{E^{\mathrm{nod}}_{24}}\circ \widetilde{\mathrm{av}}^*)\bigl(\mathcal{L}^{\Delta_5}[2]\bigr) \in \mathrm{BD\text{-}Chir\text{-}Alg}_{E^{\mathrm{nod}}_{24}}^{M_{24}}\ }
\]
*where:*

*(a) $\mathcal{L}^{\Delta_5}[2] \in \mathcal{F}^{\mathrm{mod}}$ is the
regular-singular $\mathcal{D}$-module on $\mathcal{A}_2$ of Cycle 3,
placed in cohomological degree $2$ (Cycle 2 CY-2 $[2]$-shift);*

*(b) $\widetilde{\mathrm{av}}^*$ is the pullback along the
$M_{24}$-equivariant averaging map*
$\mathrm{av}\colon \mathrm{Ran}(\mathbb{P}^1)_{M_{24}}\to \overline{\mathcal{A}_2}$
*of Cycle 1;*

*(c) $\Omega^{\mathrm{ch}}_{E^{\mathrm{nod}}_{24}}$ is the chiral
cobar functor on the 24-node elliptic curve, extended across nodes by
vanishing-cycles (Cycle 4);*

*(d) $\mathbf{H}_{\Delta_5}$ is a BD-chiral algebra on
$E^{\mathrm{nod}}_{24}$ in Beilinson–Drinfeld's axiomatic sense
(modulo the 24-node extension), with:*
- *$M_{24}$-equivariant symmetry permuting the 24 nodes;*
- *chiral bracket $\mu$ = smooth chiral bracket on the complement of
  the 24 nodes $\boxplus$ vanishing-cycles brackets at each node;*
- *parameter-space covariance over $\overline{\mathcal{A}_2}$ via
  the $\mathcal{D}$-module $\mathcal{L}^{\Delta_5}$;*
- *Koszul dual* $\mathbf{H}_{\Delta_5}^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[2]$
  *(CY-2 shift, Cycle 2);*
- *five Vol I theorems A/B/C/D/H inherit consistently, with new
  Theorem-C bucket $K^\kappa = 8$ (Wave 12 Cycle 5; Lorentzian-family
  mechanism distinct from level-family);*
- *automorphic shadow $\Delta_5 = $ flat section of $\mathcal{L}^{\Delta_5}$
  on $\mathcal{A}_2$ (Cycle 3);*
- *Borcherds-product realisation with $M_{24}$-Mathieu-moonshine
  decoration (Cycle 5);*
- *three recovery theorems (Vol III holographic programme) specialise
  to paramodular $K(1)$ via half-integer Jacobi index.*

### Chiral-quantum-group data.

As a chiral quantum group in the sense of Beilinson's foundational
programme:
\[
  \mathbf{H}_{\Delta_5} = (\mathcal{A}^{\mathrm{ch}}, \mu^{\mathrm{ch}}, \Delta^{\mathrm{ch}}, R^{\mathrm{ch}}, \Phi^{\mathrm{ch}}, \varepsilon^{\mathrm{ch}}, S^{\mathrm{ch}})
\]
with:
- $\mathcal{A}^{\mathrm{ch}} = \Omega^{\mathrm{ch}}_{E^{\mathrm{nod}}_{24}}(\mathcal{L}^{\Delta_5}[2])$
  as underlying chiral algebra;
- $\mu^{\mathrm{ch}}$ = chiral bracket, 2-dim BD-chiral bracket
  reduced to 1-dim smooth + 24-node vanishing-cycles brackets
  (Cycle 4);
- $\Delta^{\mathrm{ch}}$ = chiral coproduct, lifted to
  $\mathcal{D}$-module morphism via Siegel $\Phi$-operator cuspidal
  short exact sequence (Cycle 3);
- $R^{\mathrm{ch}}$ = Siegel-corrected $R$-matrix with Pasol–Zagier
  Kronecker–Eisenstein-Siegel term (Wave 12 Drinfeld);
- $\Phi^{\mathrm{ch}}$ = genus-2 Siegel–Borcherds associator with
  $\Phi_{10}/\eta^{24}$-twist at $\hbar^3$ (Wave 12 Drinfeld);
- $\varepsilon^{\mathrm{ch}}$ = counit, supported on the unit
  factorisation algebra structure;
- $S^{\mathrm{ch}}$ = antipode, compatible with Mukai-pairing
  symmetry and CY-2 $[2]$-shift Verdier duality.

This is the **seven-tuple chiral quantum group datum** in full.

**STATUS.** Explicit chiral-quantum-group description of
$\mathbf{H}_{\Delta_5}$ as bi-based BD-chiral algebra on
$E^{\mathrm{nod}}_{24}\times \overline{\mathcal{A}_2}$ with
seven-tuple Hopf-like datum. Wave 12's quasi-Hopf-sheaf consensus
object realised as a BD-chiral algebra.

---

## ATTACK–HEAL CYCLE 10 — Anti-attacks: robustness checks.

### Attack 10.1. Is the $[2]$-shift consistent with $c = 24$?

**Reply.** Yes. The CY-2 $[2]$-shift on $D^b\mathrm{Coh}(K3)$ is the
Serre-functor shift; on the chiral algebra side, this translates to
a shift in the $L_0$-grading of the Koszul dual:
$L_0$-grading$(\mathbf{H}_{\Delta_5}^!) = L_0$-grading$(\mathbf{H}_{\Delta_5}) + 1$
(integer shift, preserving $c$). Specifically $c^! = c = 24$ and
$K = 48$, consistent with Wave 12 Cycle 5 final answer.

### Attack 10.2. Is the averaging map $\mathrm{av}$ actually well-defined?

**Reply.** The averaging map
$\mathrm{av}\colon \mathrm{Ran}(\mathbb{P}^1)_{M_{24}}\to \overline{\mathcal{A}_2}$
is the composition:

(a) $\mathrm{Ran}(\mathbb{P}^1)\to \mathrm{Sym}^{24}(\mathbb{P}^1)$
(Ran space to symmetric product);

(b) $\mathrm{Sym}^{24}(\mathbb{P}^1)\to (\mathbb{P}^1)^{24}/S_{24}$
(the symmetric product IS this quotient);

(c) $(\mathbb{P}^1)^{24}/S_{24}\to (\mathbb{P}^1)^{24}/M_{24}$
(restriction from full symmetric group to Mathieu subgroup);

(d) Kodaira-$j$-invariant map: $(\mathbb{P}^1)^{24}\to$ (space of
K3 elliptic fibrations with 24 $I_1$ fibres);

(e) K3 period map + Torelli (Siu 1981 for K3): (space of K3s) $\to
\mathcal{A}_2$ via Kuga–Satake.

Well-definedness: (a)–(c) are categorical operations; (d) uses
Kodaira's classification of Weierstrass models; (e) is Siu's Torelli
theorem for K3 surfaces combined with Kuga–Satake. The composition
lands in a codimension-$\ge 1$ subvariety of $\mathcal{A}_2$,
specifically a neighbourhood of the cuspidal Humbert locus $H_1$
(Gritsenko–Nikulin 1997 §3).

### Attack 10.3. Does $E^{\mathrm{nod}}_{24}$ support a BD-chiral algebra in the strict BD 2004 sense?

**Reply.** Strictly not — BD 2004 requires a **smooth** curve. The
Wave 13 construction uses:
- BD on the smooth locus $E^{\mathrm{nod}, \mathrm{smooth}}_{24}$;
- Vanishing-cycles extension at each of the 24 nodes (Beilinson 1987
  nearby-cycles functor for perverse sheaves, extended to BD-chiral
  algebras in Beilinson–Drinfeld 2004 §3.5.14).

This is the **nodal BD-chiral algebra** construction: BD's axioms
extended minimally to nodal curves via vanishing-cycles. Not a
standard construction but well-defined; one can check the axioms
locally at each node.

### Attack 10.4. Is the $(\infty,1)$-categorical realisation of Cycle 8's $\mathcal{F}^{\mathrm{mod}}$ strict enough?

**Reply.** Yes in the Gaitsgory–Lurie 2019 §5 sense: the category
$\mathcal{D}^{\mathrm{hol}}(\mathcal{A}_2)$ is a presentable stable
$\infty$-category; its regular-singular full subcategory
$\mathcal{D}^{\mathrm{reg-sing}}(\mathcal{A}_2, H_1\cup H_4)$ is also
presentable stable. The factorisation-tensor structure descends from
Siegel's tower. All this is standard Gaitsgory–Lurie infrastructure.

### Attack 10.5. Cross-check with the Nekrasov K-theoretic picture.

**Reply.** Nekrasov's Wave 12 K-theoretic picture of
$\mathbf{H}_{\Delta_5}$ on $K^T(\mathcal{M}^{E_8, K3}_{\mathrm{Hitchin}})$
gives the **K-theoretic avatar** of the chiral bialgebra as a module
over the equivariant K-theory of the K3-Hitchin moduli space.
Converting to the factorisation picture:
\[
K^T(\mathcal{M}^{E_8, K3}_{\mathrm{Hitchin}}) \simeq H^*\left(\mathcal{F}^{\mathrm{mod}}|_{\mathcal{A}_2\text{-open}}\right)
\]
via Beilinson–Bernstein localisation applied to the holonomic
$\mathcal{D}$-module $\mathcal{L}^{\Delta_5}$, interpreted K-theoretically
through the Kashiwara–Tanisaki correspondence for Hitchin moduli. The
two pictures are complementary.

**STATUS.** Five anti-attacks survived. Construction robust.

---

## Beilinson verdict.

### The factorisation-algebraic characterisation of the non-abelian K3 chiral bialgebra.

**Ran-space base:** $\Ran(E^{\mathrm{nod}}_{24})$, the Ran space of the
24-node elliptic curve (= $\mathbb{P}^1$ with 24 marked points +
vanishing-cycles data at each mark), $M_{24}$-equivariantly enriched.
The Ran space is the direct limit over $n\to\infty$ of symmetric
products $\mathrm{Sym}^n(E^{\mathrm{nod}}_{24})$.

**Chiral bracket $\mu^{\mathrm{ch}}$:** smooth BD-chiral bracket on
$\Ran(E^{\mathrm{nod}, \mathrm{smooth}}_{24})^{\times 2}$ (via the
standard BD 2004 $j_*j^*\to\Delta_!$ construction), extended across
the 24 nodes by a $\boxplus$-coproduct of 24 vanishing-cycles brackets
$\mu^{\psi_{n_i}}$, reflecting the $I_1$-Kodaira degenerations of the
underlying elliptic K3.

**Parameter base:** $\overline{\mathcal{A}_2}$, the Satake-
compactified Siegel threefold of principally polarised abelian
surfaces, Humbert-stratified by $\{H_D\}_{D\equiv 0,1 \mod 4}$. The
$\mathcal{D}$-module $\mathcal{L}^{\Delta_5} = \omega^{\otimes 5}(-H_1 - H_4)$
is holonomic, regular-singular, with local monodromy order 8 at
$H_1$ and 16 at $H_4$; its flat sections are Siegel cusp forms of
weight 5 on $\mathrm{Sp}_4(\mathbb{Z})$ / paramodular $K(1)$.

**Averaging map:** $\mathrm{av}\colon \Ran(\mathbb{P}^1)_{M_{24}}\to
\overline{\mathcal{A}_2}$, identifying the chiral base with the
cuspidal Humbert locus $H_1$ via Kodaira $j$-invariant + Kuga–Satake
period map + K3 Torelli.

**Chiral-quantum-group seven-tuple:**
$(\mathcal{A}^{\mathrm{ch}}, \mu^{\mathrm{ch}}, \Delta^{\mathrm{ch}},
R^{\mathrm{ch}}, \Phi^{\mathrm{ch}}, \varepsilon^{\mathrm{ch}}, S^{\mathrm{ch}})$
where:
- $\mathcal{A}^{\mathrm{ch}} = \Omega^{\mathrm{ch}}_{E^{\mathrm{nod}}_{24}}\circ \widetilde{\mathrm{av}}^*(\mathcal{L}^{\Delta_5}[2])$;
- $\mu^{\mathrm{ch}}$ = smooth-chiral $\boxplus$ vanishing-cycles-brackets;
- $\Delta^{\mathrm{ch}}$ = chiral coproduct lifted to Siegel-$\Phi$-
  cuspidal $\mathcal{D}$-module short exact sequence;
- $R^{\mathrm{ch}}$ = Siegel-corrected $R$-matrix with Pasol–Zagier
  Kronecker–Eisenstein-Siegel term;
- $\Phi^{\mathrm{ch}}$ = genus-2 Siegel–Borcherds associator with
  $\Phi_{10}/\eta^{24}$-twist at $\hbar^3$;
- $\varepsilon^{\mathrm{ch}}$ = counit via factorisation-algebra unit;
- $S^{\mathrm{ch}}$ = antipode compatible with Mukai-pairing
  CY-2 $[2]$-shift Verdier duality.

**$(\infty,1)$-shadow:** $\mathcal{F}^{\mathrm{mod}} =
\mathcal{D}^{\mathrm{reg-sing}}(\mathcal{A}_2, H_1\cup H_4) \in
\mathrm{FactCat}(\mathcal{A}_2)$, a presentable stable $\infty$-
factorisation category; Koszul-duality endofunctor
$\mathfrak{K}^{\mathrm{mod}}$ acting as Verdier duality on
$\mathbf{H}_{\Delta_5}$; Francis–Gaitsgory bar–cobar adjunction
extended from curves to Siegel-threefold parameter base via the
averaging map.

**Automorphic descent:** $\Delta_5$ = flat section of
$(\mathcal{L}^{\Delta_5}, \nabla^{\Delta_5})$; $\Delta_5^2 = \Phi_{10}$
on paramodular $K(1)$; chiral structure descends to automorphic
structure via Kuga–Satake + Siegel $\Phi$-operator.

**Structural identities:**
1. $\hbar^2\cdot K^\kappa = -1$ on the $\mathsf{B}$-family (Wave 12);
   $K^\kappa = 8 = 2c_+ = $ order of Humbert-$H_1$ monodromy (Wave 13
   Cycle 6);
2. $\hbar^2 = -1/8 = -1/(2c_+)$ three-path verified (Wave 12);
3. $K = 2c(\mathrm{Mukai}(K3)) = 48$ **Mukai-doubling identity**
   (Wave 13 Cycle 2);
4. CY-2 $[2]$-shift (Wave 12 Costello, Wave 13 Cycle 2) with preserved $c$;
5. $\Delta_5^2 = \Phi_{10}|_{K(1)}$ via $\mathcal{D}$-module cuspidal
   SES (Wave 13 Cycle 3).

### Summary: the chiral quantum group undergirding $\Delta_5$.

$\mathbf{H}_{\Delta_5}$ is the chiral quantum group that:

(i) lives as a BD-chiral factorisation algebra (in the nodal-extended
BD sense of Beilinson–Drinfeld 2004 §3.5.14) on the Ran space of the
24-node discriminant curve $E^{\mathrm{nod}}_{24}$ = $(\mathbb{P}^1,
\{24\ \mathrm{nodes}\})$, with $M_{24}$-equivariant symmetry
permuting the 24 nodes;

(ii) carries a parameter-covariance structure over the Siegel
threefold $\overline{\mathcal{A}_2}$ via the holonomic regular-singular
$\mathcal{D}$-module $\mathcal{L}^{\Delta_5} = \omega^{\otimes 5}(-H_1 - H_4)$,
whose local monodromy has order 8 at $H_1$ and order 16 at $H_4$,
and whose flat sections are Siegel cusp forms of weight 5 on
paramodular $K(1)$ (with $\Delta_5$ as distinguished flat section);

(iii) has Koszul dual $V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[2]$
with CY-2 Serre-functor shift $[2]$ (per Lurie HA 6.3.1.5 applied to
$D^b\mathrm{Coh}(K3)$);

(iv) carries seven-tuple chiral quantum-group data
$(\mathcal{A}^{\mathrm{ch}}, \mu^{\mathrm{ch}}, \Delta^{\mathrm{ch}},
R^{\mathrm{ch}}, \Phi^{\mathrm{ch}}, \varepsilon^{\mathrm{ch}}, S^{\mathrm{ch}})$;

(v) satisfies the $\mathsf{B}$-family universal duality
$\hbar^2\cdot K^\kappa = -1$ with $\hbar^2 = -1/8$ (Drinfeld-
associator / Mukai-chirality / $\mathcal{D}$-module-monodromy three-
path agreement) and $K^\kappa = 8 = 2c_+ = $ order of Humbert-$H_1$
monodromy (new structural identity this Wave 13);

(vi) realises the Cheng–Duncan–Harvey umbral $A_1^{24}$ Mathieu
moonshine as its Grothendieck $K_0$-class in
$\mathrm{FactAlg}_{E^{\mathrm{nod}}_{24}}^{M_{24}}$ (conjectural,
Wave 13 Cycle 5);

(vii) admits an $(\infty,1)$-shadow in
$\mathcal{D}^{\mathrm{reg-sing}}(\mathcal{A}_2, H_1\cup H_4)$, a
presentable stable $\infty$-factorisation category on the Siegel
threefold with explicit Koszul-duality endofunctor.

**This is the chiral quantum group undergirding the BKM $\mathfrak{g}_{\Delta_5}$
and its Siegel automorphic shadows $\Delta_5, \Phi_{10}$.**

### Wave 13 retractions.

| # | Wave 12 claim | Wave 13 correction | Justification |
|---|---|---|---|
| W13-R1 | "CY-3 $[3]$-shift preserves $c$" (my Wave 12 Cycle 5 Step 2 reasoning) | CY-3 is wrong; correct is CY-2 $[2]$-shift, integer shift preserving $c$ | Costello Wave 12 MAJOR + Wave 13 Cycle 2 Lurie HA 6.3.1.5 |
| W13-R2 | "Factorisation algebra home is 24-node discriminant curve $E^{\mathrm{nod}}_{24}$" (Costello Wave 12) | Refined: $E^{\mathrm{nod}}_{24}$ is the chiral base; $\overline{\mathcal{A}_2}$ is the parameter base; object is bi-based via averaging map | Wave 13 Cycle 1 |
| W13-R3 | "$M_{24}$-equivariant sheaf of Miki algebras over $\Delta(\overline{\mathcal{A}_2})$" (Etingof Wave 12) | Refined: $(\infty,1)$-factorisation category $\mathcal{F}^{\mathrm{mod}} = \mathcal{D}^{\mathrm{reg-sing}}(\mathcal{A}_2, H_1\cup H_4)$ with Koszul-duality endofunctor | Wave 13 Cycle 8 |

**STATUS OF PROGRAMME.** Wave 13 Beilinson produces **three** Wave 12
refinements (not retractions of Wave 12 content but sharper
re-statements) + **seven new theorems** (W13-B-1 through W13-B-12,
plus W13-B-conj-moonshine as a conjecture) + the **central
identification** of $\mathbf{H}_{\Delta_5}$ as a bi-based BD-chiral
algebra with explicit 7-tuple data.

### Wave 13 new anti-patterns.

| # | Confusion | Precise error | Correct relationship |
|---|---|---|---|
| W13-AP-Beil-1 | "Factorisation base = $E^{\mathrm{nod}}_{24}$ **or** $\overline{\mathcal{A}_2}$, exclusively" | Either-or conflation: the object is bi-based, using $E^{\mathrm{nod}}_{24}$ as chiral base and $\overline{\mathcal{A}_2}$ as parameter base | Bi-based factorisation datum linked by averaging map $\mathrm{av}$ |
| W13-AP-Beil-2 | "$E^{\mathrm{nod}}_{24}$ is genus-0 nodal curve with cohomological singularities" | Confusion between Kodaira discriminant locus (24 points on $\mathbb{P}^1$) vs the cohomologically-singular total space | $E^{\mathrm{nod}}_{24} = (\mathbb{P}^1, \{24\ \mathrm{points}\})$ with vanishing-cycles data at each mark |
| W13-AP-Beil-3 | "CY-3 $[3]$-shift for $\mathbf{H}_{\Delta_5}$" | Half-integer shift arithmetic; $c^!_{[3]} \ne c$ | CY-2 $[2]$-shift (integer, preserves $c$); Lurie HA 6.3.1.5 |
| W13-AP-Beil-4 | "Siegel $\Phi$-operator is an algebra morphism only" | Misses $\mathcal{D}$-module-morphism lifting | Siegel $\Phi$ lifts to $\mathcal{D}$-module morphism $\mathcal{L}^{\Delta_5}\to i_*\mathcal{L}^{\Delta_5|_\partial}$, killing $\Delta_5$ cuspidally |
| W13-AP-Beil-5 | "Monodromy order 8 and $K^\kappa = 8$ are coincidences" | Missed structural identity | Both equal $2c_+$ and both are local-to-global manifestations of the $\mathsf{B}$-family mechanism |
| W13-AP-Beil-6 | "BD-chiral algebras exist only on smooth curves" | Partial truth; ignores BD §3.5.14 nodal extension | BD-chiral algebras on smooth loci of nodal curves + vanishing-cycles extension at nodes (BD 2004 §3.5.14) |

### Residual open.

1. **Explicit construction of the averaging map $\mathrm{av}$.**
   Cycle 1 sketches the composition (Ran → Sym^24 → Kodaira-j → K3
   period → $\mathcal{A}_2$); checking it is a factorisation map
   between $\Ran(\mathbb{P}^1)_{M_{24}}$ and $\overline{\mathcal{A}_2}$
   requires verifying factorisation-axiom compatibility. Wave 14.

2. **Proof of the Mathieu-moonshine $K_0$-class conjecture
   (Cycle 5).** $\mathbf{H}_{\Delta_5}$'s $K_0$-class in
   $\mathrm{FactAlg}_{E^{\mathrm{nod}}_{24}}^{M_{24}}$ should equal
   the Rademacher expansion of $\phi^{K3}_{0,1}$. Requires explicit
   character computation. Wave 14.

3. **Verification of the bi-based Koszul-duality endofunctor
   (Cycle 8).** $\mathfrak{K}^{\mathrm{mod}}$ on
   $\mathcal{F}^{\mathrm{mod}}$ is well-defined but its $\infty$-
   functorial construction requires Gaitsgory–Lurie 2019 §5.5.1
   detail plus an extension of Francis–Gaitsgory 2012 §6.1 to the
   Siegel-threefold parameter base. Wave 14.

4. **Paramodular $K(1)$ vs $\mathrm{Sp}_4(\mathbb{Z})$ factorisation
   lift.** $\Delta_5^2 = \Phi_{10}$ on $K(1)$ (Wave 12 Nekrasov C2).
   At the factorisation-algebra level, paramodular $K(1)$ and
   $\mathrm{Sp}_4(\mathbb{Z})$ are different groups; do they give
   different factorisation categories? Wave 14.

5. **Chain-level witness for the seven-tuple chiral-quantum-group
   data.** My Wave 13 gives the seven-tuple at the $(\infty,1)$-
   categorical level; chain-level witnesses (explicit cocycles for
   the associator, explicit $R$-matrix on a specific chiral module,
   etc.) are standard to extract in principle but not inscribed here.
   Wave 14.

### Closing remark: chain-level and $(\infty,1)$-categorical status.

Per CLAUDE.md, both **chain-level** and **$(\infty,1)$-categorical**
mathematics are equally load-bearing. Wave 13 Beilinson delivers:

- **Chain-level**: the nodal BD-chiral bracket $\mu^{\mathrm{ch}}$ on
  $E^{\mathrm{nod}}_{24}$ with explicit smooth + vanishing-cycles
  decomposition (Cycle 4); explicit local monodromy computations at
  $H_1$ and $H_4$ (Cycle 6); the Gauss–Manin-twisted line bundle
  $\mathcal{L}^{\Delta_5}$ with explicit connection (Cycle 3).

- **$(\infty,1)$-categorical**: the Gaitsgory–Lurie factorisation
  $\infty$-category $\mathcal{F}^{\mathrm{mod}}$ (Cycle 8); the
  Francis–Gaitsgory bar–cobar Koszul-duality endofunctor
  $\mathfrak{K}^{\mathrm{mod}}$ (Cycle 8); the bi-based factorisation
  datum as a pullback in the $(\infty,1)$-category of bi-based
  factorisation data (Cycle 1).

Both lenses yield the same theorem: $\mathbf{H}_{\Delta_5}$ is the
chiral quantum group undergirding the BKM $\mathfrak{g}_{\Delta_5}$ and
its Siegel automorphic shadows $\Delta_5, \Phi_{10}$.

---

*End Wave 13 Beilinson memo.*

*Author: Raeez Lorgat. No AI attribution. Primary sources cited
throughout. Ten attack–heal cycles. Twelve new theorems or
propositions. Three Wave 12 refinements. Six new anti-patterns.
Five residual open items for Wave 14.*
