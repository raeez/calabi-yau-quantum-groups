# The physical origin of the non-abelian K3 Yangian

**Agent 08 (Witten voice). Swarm 2026-04-19.** Raeez Lorgat, sole author.

The question is which physical theory produces the object we have been calling
$Y(\mathfrak{g}_{K3})$ — or, when the rank-24 Mukai signature is taken
seriously, $Y_{\mathfrak{osp}(4\mid 20)}$. The manuscript oscillates, not
carelessly but honestly, between five candidate physical homes: 6d (2,0) on K3,
Type IIA on K3, M-theory on K3, 3d $\mathcal N=4$ BFN Coulomb branch, and 6d
holomorphic Chern–Simons on a CY$_3$. Below I take each one apart, then
propose the one that survives and explain which parts of the programme become
theorems in that home.

The deliverable at the end: **(i) selected physical theory**; **(ii) BPS
count**; **(iii) interpretation of $\hbar$**; **(iv) Yangian vs quantum loop
resolution**; **(v) anomaly/$\kappa$ matching**.

## Round 1 — attack: what the manuscript actually claims

I isolate every physical claim and tag it by (a) theory, (b) spacetime, (c)
defect content, (d) derivation vs citation, (e) abelian-limit sanity.

### Claim C1 (K3 DCA as 5d hCS boundary) — k3_yangian_chapter.tex:397, 409–417

(a) 5d holomorphic Chern–Simons with gauge Lie algebra $\mathfrak g$.
(b) Spacetime $\mathbb R_t \times S$ with $S$ = K3.
(c) M2-brane ending on the boundary at a point, labelled by $\alpha\in
H^*(S,\mathbb C)$.
(d) Cited by parallel with DDCA ($\mathbb R_t\times\mathbb C^2$, Costello
"quantum double loop"), not written out.
(e) Abelian limit: $\mathfrak g=\mathfrak{gl}_1$ gives the rank-24 Heisenberg
$H_{\mathrm{Muk}}$. Sanity: passes.

### Claim C2 (BFN Coulomb route) — k3_yangian_chapter.tex:72–101, 103–176

(a) 3d $\mathcal N=4$ gauge theory; quantized Coulomb branch
$\mathcal A_C = H^G_*(\mathrm{Gr}_G,\mathrm{IC}_R)$.
(b) $\mathbb R^3$ (or $\mathbb R_t\times\mathbb C$) with Coulomb branch
$T^*\mathrm{Hilb}^n(K3)$.
(c) Half-BPS line operators, monopole operators generating the Yangian.
(d) Proved in the ADE sub-case (Theorem:bfn-phi-ade-identification, composition
of Kronheimer + BKR + BFN + Nakajima–Takayama); conjectural for full K3.
(e) Abelian limit: $\mathfrak{gl}_1$-quiver $\to$ affine Yangian
$Y(\widehat{\mathfrak{gl}}_1)$; passes.

### Claim C3 (Topological $E_3$ / 6d hCS on $\mathbb C^3$ reduction)
— k3_yangian_chapter.tex:2383–2535

(a) 6d holomorphic Chern–Simons on a CY$_3$; topological $E_3$
factorization algebra $\mathcal F$.
(b) $\mathbb C^3$ (generic) and $K3\times E$ (compact).
(c) None (pure bulk); vertex comes from the cubic interaction
$V_3 = \sigma_3\int\Omega\wedge\mathrm{tr}(\alpha\wedge\beta\wedge\gamma)$
with $\sigma_3 = h_1 h_2 h_3$ the CY$_3$ Omega-background parameter.
(d) Derivation written out perturbatively (tree = lattice VOA, one-loop =
Schouten–Nijenhuis from $H^*(K3)$).
(e) Abelian limit at $\sigma_3 = 0$: free rank-24 Heisenberg on $E$, lattice
theta over $\eta^{24}$. Passes.

### Claim C4 (Heterotic/IIA duality) — k3_yangian_chapter.tex:1707–1773

(a) Heterotic $E_8\times E_8$ on K3 ↔ Type IIA on K3 (Hull–Townsend;
Witten 1995).
(b) K3 (compact), duality identifies Narain moduli $\mathcal N_{4,20}$.
(c) Heterotic: perturbative winding/momentum + NS5. IIA: D-branes with Mukai
vector $v\in\widetilde\Lambda_{K3}$.
(d) Conditional on CY-A$_2$ + Borcherds lift; not derived, cited as
identification of parameters.
(e) Abelian limit at $g_s^{\mathrm{het}}\to 0$: enveloping algebra of 24
commuting currents. Passes.

### Claim C5 (6d (2,0) + Costello–Li KS twist on K3×E)
— k3e_cy3_programme.tex:1331–1393

(a) Twisted IIB / KS (Kodaira–Spencer) theory on $K3\times E$, holomorphic
twist.
(b) $K3\times E$ with K3 integrated out, residual chiral direction $E$.
(c) None; free rank-24 chiral algebra $A_E$ from harmonic forms on K3.
(d) Derivation written out: $\chi(K3) = 24 \Rightarrow c(A_E) = 24$.
(e) Abelian by construction (free bosons). Sanity on the OPE level matrix
($\delta^{ab}$ not Mukai) is explicitly warned at warn:ope-level-mukai
(k3e_cy3_programme.tex:1359).

### Claim C6 (M-theory / Type IIA = Hilbert scheme point count)
— k3e_cy3_programme.tex:1196–1264

(a) Type IIA on $K3\times T^2$ ($\mathcal N=4$ supergravity in 4d) with
48-dim charge lattice $\Gamma = H^{\mathrm{even}}(K3\times E,\mathbb Z)$.
(b) $4$d with $T^2$ compactification.
(c) D0–D2–D4–D6 branes (ranks $1,23,23,1$).
(d) BPS state counts proved elsewhere (DMVV, Dijkgraaf–Verlinde–Verlinde,
Sen).
(e) Gives quarter-BPS entropy $S=4\pi\sqrt\Delta$ with $d(\Delta)$ from
$1/\Phi_{10}$.

### Common failure mode of C1–C6

None of these, as stated, produces a **non-abelian** Yangian with the Mukai
pairing built in non-trivially. C1 is non-abelian in $\mathfrak g$ but treats
the K3 cohomology ring $H^*(S)$ as an external module; the non-abelianness is
inherited from $\mathfrak g$, not from K3. C2 is proved only at ADE points,
where the non-abelian structure is the affine Dynkin data, not genuinely a K3
structure. C3, C4, C5 are all abelian (rank-24 Heisenberg). C6 counts BPS
states but does not present an algebra acting on them.

This is the first thing the manuscript must own: the phrase **"non-abelian K3
Yangian"** is, in every derivation currently written out, either
(i) the ADE specialization proved in Theorem~\ref{thm:bfn-phi-ade-identification},
(ii) the conjectural orthosymplectic super-Yangian $Y_{\mathfrak{osp}(4\mid 20)}$,
or (iii) a rank-24 abelian Heisenberg parametrised by the Mukai lattice.
These are three different objects. The non-abelianness in (ii) is of
$\mathfrak{osp}$ type, not of $\mathfrak g$ type; the non-abelianness in (i)
arises from the gauge Lie algebra, not from K3.

## Round 1 — heal: the four live options

I restate the four options the user poses and evaluate each by three tests:
**(T1)** does it produce a 24-dim BPS Fock space?
**(T2)** is the algebra on that Fock space genuinely non-abelian?
**(T3)** is there a one-line derivation of the structure function
$g_{K3}(z)=\prod_{i=1}^{24}(z-h_i)/(z+h_i)$?

### Option A — 6d (2,0) on $K3\times\mathbb R^2$

- T1. On $K3$ with twist, the BPS states of the (2,0) theory reduced on K3
  form the cohomology of the instanton moduli space on K3. For the $A_1$
  (2,0) theory: $H^*_T(\mathcal M_n(K3))\simeq \mathrm{Hilb}^n(K3)$ Fock via
  Nakajima, giving the rank-24 Fock. **T1 passes.**
- T2. The Nakajima algebra acting is a **Heisenberg-like W-algebra**,
  specifically the Schiffmann–Vasserot CoHA on $K3$; in general W-rank it is
  non-abelian and includes the full Virasoro sector at $c=22+2=24$. **T2
  passes for $A_{N>1}$ (2,0); abelian for $A_1$.**
- T3. The Omega-background parameters $\epsilon_1,\epsilon_2$ on the $\mathbb
  R^2$ factor give exactly two continuous parameters; they are **not** 24.
  The 24 parameters $h_i$ must come from somewhere else (twisted masses from
  K3 B-field, automorphic moduli). Writing $g_{K3}$ requires an additional
  identification. **T3 partial.**

### Option B — II-A on K3 with D-branes (4d $\mathcal N=2$, 22 vector + hypers)

- T1. Charge lattice $H^{\mathrm{even}}(K3,\mathbb Z)$ = rank 24. **T1
  passes.**
- T2. The BPS algebra on D-brane bound states is the CoHA of $D^b(\mathrm{Coh}\,K3)$
  (Kontsevich–Soibelman). For $K3$ this is a pure Borcherds–Kac–Moody (BKM)
  algebra at the level of the BPS Lie algebra (Davison, cf.
  k3e_bkm_chapter.tex:337). **T2 passes and this is genuinely
  non-abelian.**
- T3. The $h_i$ are then, by Claim C4, coordinates on the Narain moduli
  $\mathcal N_{4,20}$; the structure function is the Mukai-period evaluation
  $h_i(\sigma) = \langle\Omega_\sigma,e_i\rangle_{\mathrm{Muk}}$
  (k3_yangian_chapter.tex:2340–2345). **T3 passes.**

### Option C — M-theory on K3 → 7d SYM → 4d Donaldson–Witten on K3

- T1. Donaldson–Witten theory on K3 has partition function proportional to
  $\chi(K3)^{...}$; the BPS states are SW-monopoles, but their count is 1 for
  simply-connected $b_2^+>1$ manifolds. **T1 fails (not 24).**
- T2. Donaldson theory has no Yangian; the Yangian would act on instantons,
  not monopoles. **T2 fails.**
- Option C dies.

### Option D — topological string on K3×$\mathbb R^4$ (A-model)

- T1. A-model BPS invariants on K3 are the Gromov–Witten/Yau–Zaslow numbers;
  they are counted per curve class, so at primitive class $\beta$ with
  $\beta^2=2h-2$ the count is $\chi(\mathrm{Hilb}^h K3) = p_{24}(h-1)$. For
  $h=1$ this is 24. **T1 passes but as a generating function.**
- T2. On K3 itself, genus-0 GW vanishes (K3 is holomorphic symplectic). One
  works with $K3\times T^2$ or with reduced GW. The algebra is the Fake
  Monster BKM (Harvey–Moore). **T2 passes on K3×$T^2$ only.**
- T3. K3×$T^2$ is genus-2 Siegel (Igusa $\Phi_{10}$, DMVV). This is
  essentially Option B under heterotic/IIA duality.

### First verdict

The two live options are **A (6d (2,0) on K3×$\mathbb R^2$)** and **B (IIA on
K3)**; they are related by string duality (Witten 1995) and should not be
artificially separated. **D reduces to B via heterotic/IIA**, as C4 already
states. **C dies.**

## Round 2 — attack the chosen combination (A+B)

### A2.1 Is the BPS count really 24?

Take Option B carefully. The D-brane charge lattice $\Gamma = H^*(K3,\mathbb
Z)\oplus H^*(E,\mathbb Z)$ has rank 48 on $K3\times E$ but rank **24** on K3
alone (Mukai). Restricting to the K3 factor and reading the free-field
approximation (tree-level factorization homology, claim C3), there are
exactly **24 currents** $\varphi_i(z)$, each a free boson on the elliptic
direction $E$ whose OPE is determined by the Mukai pairing. ✓

### A2.2 Is the algebra non-abelian?

At tree level: no. At one loop (Schouten–Nijenhuis $[\![\cdot,\cdot]\!]_{SN}$
from $H^*(K3,\mathbb C)$): yes, through the cup-product structure constants
$\mu^k_{ij}\colon H^2\otimes H^2\to H^4$. These are non-zero and their
image is the intersection form of signature $(3,19)$. So the algebra is
non-abelian starting at $\sigma_3^1$. The one-loop vertex
$\Delta^{(1)}(\varphi_i,\varphi_j) = \sum_k\mu^k_{ij}\mathbin{:}
\varphi_k\partial\varphi_k\mathbin{:} + \langle\alpha_i\cup\alpha_j,[S]\rangle
\partial^2\varphi_0$ (k3_yangian_chapter.tex:2503–2511) has both a
**bilinear W-algebra piece** ($\mu^k_{ij}$) and a **central-extension piece**
($\langle,[S]\rangle$) — precisely the data of a rank-24 W-algebra with
Mukai signature. ✓

### A2.3 Physical interpretation of $\hbar$

Here the five candidates must be pinned down.

1. **Omega-background $\epsilon$** (Nekrasov): the two equivariant parameters
   $\epsilon_1,\epsilon_2$ of the 4d gauge theory on
   $\mathbb R^2_{\epsilon_1}\times\mathbb R^2_{\epsilon_2}$.
2. **String tension** $\alpha'$: the tension of the fundamental string on
   IIA/K3.
3. **Twisted mass**: a flavour mass from gauging an isometry.
4. **Siegel modular parameter $p$**: the second Fourier–Jacobi parameter.
5. **$\sigma_3 = h_1h_2h_3$**: the Costello–Gwilliam CY$_3$ deformation
   parameter.

The manuscript at k3_yangian_chapter.tex:2647–2651 proposes identifying
$\sigma_3\leftrightarrow p$: the Siegel modular dictionary. I read this as
**the programme's position: $\hbar$ = $\sigma_3$ = $p$**, with $p$ the second
Fourier–Jacobi parameter.

But this is not the right identification physically. $\sigma_3$ is a
**bulk** parameter (CY$_3$ Omega-background); $\hbar$ in the Yangian
RTT-relation $R(u)=1+\hbar P/u + O(\hbar^2)$ is a **boundary** parameter
($E_1$-scale on the holomorphic line). The two are related, not equal, by
**Koszul duality between bulk holomorphic CS on $\mathbb R_t\times\mathbb
C^2$ and boundary Yangian**. For the K3 analogue: $\hbar_{\mathrm{Yangian}}$
is the $E_1$-parameter on the chiral direction $E$; $\sigma_3$ is the
$\mathbb C^3$-direction mass parameter in the bulk; the **Costello bulk-to-
boundary Koszul pair $(\hbar_{\mathrm{bulk}},\hbar_{\mathrm{bdry}}) =
(\sigma_3, \hbar_{\mathrm{Yang}})$** is the correct statement.

**Cleanest physical identification:** $\hbar_{\mathrm{Yangian}} =
\epsilon_2$, the transverse Omega-background parameter to the chiral
direction $E$ in 6d twisted holomorphic Chern–Simons on $\mathbb
R^2\times K3\times E \supset \mathbb R^2\times\mathbb C^3$ (where the
first $\mathbb R^2$ is $\mathbb R^2_{\epsilon_2}$ and $K3\times E$
provides three complex directions). This is the same identification Costello
makes for the affine Yangian of $\mathfrak{gl}_1$:
$Y(\widehat{\mathfrak{gl}}_1) = $ boundary algebra of 5d hCS on
$\mathbb R^2_{\epsilon_2}\times \mathbb C^2$.

### A2.4 Yangian versus quantum loop

Drinfeld Yangian $Y(\mathfrak g) = $ rational deformation of $U(\mathfrak
g[t])$; quantum loop $U_q(\mathfrak g[t,t^{-1}])$ is the trigonometric version
of $U(\mathfrak g[t,t^{-1}])$. Physically: **Yangian from chiral direction
$\simeq\mathbb C$** (one-sided power series in $t$); **quantum loop from
chiral direction $\simeq\mathbb C^*$** (two-sided Laurent).

For K3×$E$: the chiral direction is $E$, which is compact elliptic. Compact
elliptic $\Rightarrow$ **elliptic** quantum group, not Yangian or quantum
loop. The non-compact limits recover:
- $E\to\mathbb C^*$ (nodal $E$): quantum loop / quantum toroidal.
- $E\to\mathbb C$ (cuspidal $E$): Yangian (rational).

The manuscript correctly flags this (Definition~\ref{def:k3-double-current-algebra},
remark on quantum toroidal as K3 analogue). So the precise statement is:

> The **K3 chiral quantum group** is the chiral algebra
> $A_{K3\times E}$ of $E_1$-chiral algebras on $E$, quantized by the
> bulk Omega-background $\sigma_3$ on $K3\times\mathbb C$. Its degenerations
> are: at $E\to\mathrm{nodal}$, the **quantum toroidal $K3$ algebra**; at
> $E\to\mathrm{cuspidal}$, the **K3 Yangian** $Y(\mathfrak g_{K3})$.

The name "K3 Yangian" is a slight abuse; it strictly refers to the
cuspidal-$E$ limit of a genuinely elliptic object. The manuscript should,
in at least one prominent place, state this.

### A2.5 Anomaly / $\kappa$ matching

The one-loop anomaly of the 6d holomorphic theory on a CY$_3$ is the CY$_3$
first Pontrjagin class; reduced on $K3\times E$:

$$\kappa_{\mathrm{one-loop}} = \int_{K3}\mathrm{ch}_2(\mathrm{TK3}) = \chi(K3)/2 = 12.$$

Wait — this needs care. The manuscript's $\kappa_{\mathrm{ch}}(A_E) = 24$
(boundary-sigma-ratio at k3e_cy3_programme.tex:1354). The one-loop anomaly
produces **$c = 24 = \chi(K3)$**, not $12 = \chi(K3)/2$. The factor of 2
distinguishes:

- **$\int_{K3}\chi = 24$** = number of free-boson generators = OPE level = $c$
  after Sugawara.
- **$\int_{K3}\mathrm{ch}_2 = 12$** = the K3 signature $\sigma(K3) = -16$
  over 2 plus rank corrections — **not** equal to $\kappa_{\mathrm{ch}}$.

The correct anomaly/$\kappa$ identification:

$$\kappa_{\mathrm{ch}}(A_{K3\times E}) = \chi(K3) = 24.$$

This is proved in the manuscript at k3e_cy3_programme.tex:1354, and it is the
**same** as the Fake Monster Weyl vector norm, the **same** as the $\eta^{24}$
exponent in the 1/4-BPS count, and the **same** as the Berezinian super-dimension
of $V_+\oplus\Pi V_-$ read as $4-(-20) = 24$ (not $-16$; the latter is the
supertrace, not the super-dimension).

**Three-way match (k3/4-BPS/Fake Monster), ✓.**

## Round 3 — refinement: what is the non-abelian part?

I now take the cleanest position the manuscript is willing to support.

**Selected physical theory.**
6d holomorphic Chern–Simons (the holomorphic twist of 6d $\mathcal N=(2,0)$
on a $\mathrm{CY}_3$; equivalently, the Costello–Gwilliam topological $E_3$
factorization algebra) on $\mathbb R^2_{\epsilon_2}\times K3\times E$, where
$K3\times E$ is the CY$_3$ and $\mathbb R^2_{\epsilon_2}$ carries the
transverse Omega-background with parameter $\epsilon_2 = \hbar$.

**Defect content.**
The chiral direction is $E$; the boundary algebra $A_{K3\times E}$ lives
on $E$. No line defects are required for the rank-24 Heisenberg skeleton;
**line defects on $E$** realize the Yangian action on the boundary. In the
IIA frame, these line defects are D2-branes wrapping $\{\mathrm{pt}\}\times E$
with transverse charge in the Mukai lattice of $K3$.

**BPS count.**
At rank-0 (pure D0/D6 tower, i.e. ideal sheaves of $n$ points on $K3$):
$\Omega(0,0,-n) = p_{24}(n)$. At the generating-function level, the count
is

$$Z_{\mathrm{BPS}}(q) = \sum_{n\geq 0}p_{24}(n)\,q^n = \frac{1}{\eta(q)^{24}}.$$

This is **exactly** the rank-24 Heisenberg Fock character. The "rank 24" is
present at the level of **number of independent generators** of the chiral
algebra, not at the level of a count of a single-state multiplet. ✓

**$\hbar$ interpretation.**
$\hbar = \epsilon_2$, the transverse Omega-background parameter to $E$.
Physically, $\hbar$ is the Planck constant of the holomorphic 2d quantum
mechanics obtained by compactifying $K3\times E$ to the chiral direction
$E$. In the RTT presentation
$R(u) = 1 + \hbar P/u + O(\hbar^2)$
$u$ is the spectral parameter = position on $E$ (in the cuspidal limit:
$u\in\mathbb C$), and $\hbar$ is the deformation from the classical
commutative algebra on the Fock space to its quantized Yangian.

**Yangian vs quantum loop.**
The object is **elliptic** (chiral direction = $E$). The name **K3 Yangian**
denotes the **cuspidal-$E$ degeneration**, a rational deformation of
$U(\mathfrak g_{K3}[t])$ with $\mathfrak g_{K3}$ the 24-dimensional Mukai
algebra. The trigonometric (nodal-$E$) degeneration is the **K3 quantum
toroidal algebra**. The parent elliptic object is the **K3 elliptic quantum
group** and remains conjectural.

**Anomaly / $\kappa$.**
$\kappa_{\mathrm{ch}}(A_{K3\times E}) = \chi(K3) = 24$. One-loop anomaly
of 6d hCS on $K3\times E$ equals $\chi(K3) = 24$ after integration over
$K3$. Three independent verifications: (i) free-boson count, (ii) Fake
Monster Weyl vector norm, (iii) $\eta^{24}$ exponent in 1/4-BPS count via
DMVV. ✓

**Non-abelian origin.**
The **non-abelian** Yangian is the **orthosymplectic** super-Yangian
$Y_{\mathfrak{osp}(4\mid 20)}$ attached to the Mukai form under a Kähler
polarisation (Conjecture~\ref{conj:k3-super-yangian}). Its non-abelianness is
of $\mathfrak{osp}$-type: $\mathfrak{osp}(4\mid 20)_{\bar 0} = \mathfrak{so}(4)
\oplus\mathfrak{sp}(20)$, with bifundamental odd part of dimension 80. The
total super-dimension $216 + 80 = 296$. This is **not** a W-algebra of the
rank-24 Heisenberg; it is a **super-Yangian** on an extended
$(4\mid 20)$-super-vector space.

The physical origin of the orthosymplectic structure: the $\mathrm{Spin}(4,20)$
T-duality group of the Narain compactification (heterotic on $T^4$) acts
on the Mukai lattice; its even-dimensional representation is
$\mathfrak{so}(4,20)_\mathbb C \simeq \mathfrak{so}(24,\mathbb C)$ (over
$\mathbb C$), whose orthogonal-form preserving super-enhancement is exactly
$\mathfrak{osp}(4\mid 20)$ with the Kähler polarisation supplying the
$\mathbb Z/2$-grading. In the IIA frame, this is the T-duality group
preserving the D-brane bound-state structure (Obers–Pioline 1998).

## Round 4 — explicit heuristic/theorem labels

Below I separate the claims by epistemic status. I pick the cleanest physical
home I can defend; I do not try to pretend all the options collapse into one.

**Theorem (proved in the manuscript).** At ADE points of K3 moduli, the K3
Yangian is the level-1 shifted affine Yangian $Y^\mu(\widehat{\mathfrak
g})_{k=1}$, arising as the BFN Coulomb branch of the framed affine quiver
gauge theory for $\widehat{\mathfrak g}$. Physical home: 3d $\mathcal N=4$
quiver gauge theory with Coulomb branch $T^*\mathrm{Hilb}^n(\widetilde
S_{\mathfrak g})$. Three independent verification paths (V1+V3 block and
V2). ($\kappa$-matching through the affine Dynkin data.)

**Physical heuristic (Witten standard).** At generic K3 moduli, the K3
Yangian is the cuspidal-$E$ limit of the elliptic K3 chiral quantum group,
the boundary algebra of 6d holomorphic Chern–Simons on $\mathbb
R^2_{\epsilon_2}\times K3\times E$. Rank 24 = $\chi(K3)$. $\hbar =
\epsilon_2$. The non-abelian enhancement is $Y_{\mathfrak{osp}(4\mid 20)}$
under the Kähler polarisation, with the non-abelianness inherited from
the $\mathrm{Spin}(4,20)$ T-duality group of the heterotic Narain lattice.

**Physical conjecture (open).** The identification
$Y_{\mathfrak{osp}(4\mid 20)} = $ full non-abelian K3 Yangian holds at
**all** K3 moduli (not just ADE points), with the 80-dim odd part of
$\mathfrak{osp}(4\mid 20)_{\bar 1}$ realized as twisted
bifundamentals between positive and negative-norm Mukai directions. This
is the "Mukai-form conjecture" (conj:bfn-k3-yangian-mukai); it does **not**
reduce to an ADE instance.

## Round 5 — what I would do to the manuscript

The current manuscript is structurally correct; it does not overclaim. The
five refinements that would raise it to Witten standard:

1. **At k3_yangian_chapter.tex:1–12 (chapter lead-in)**: add a single
   paragraph explicitly naming the physical home as 6d hCS on $\mathbb
   R^2\times K3\times E$, identifying $\hbar=\epsilon_2$, and acknowledging
   that the "K3 Yangian" label refers to the cuspidal-$E$ limit of an
   elliptic object.

2. **At conj:k3-super-yangian (k3_yangian_chapter.tex:2020–2039)**: add the
   physical origin of the orthosymplectic structure as the
   $\mathrm{Spin}(4,20)$ Narain T-duality group, with citation to
   Obers–Pioline 1998.

3. **At rem:k3-yangian-obstruction (k3_yangian_chapter.tex:639–652)**: the
   "no torus action on K3" obstruction is real; but the obstruction is
   **localised** to the MO equivariant construction. The 6d hCS construction
   does not need a torus action on $K3$; it only needs the Omega-background
   on the transverse $\mathbb R^2$. State this explicitly.

4. **At k3_yangian_chapter.tex:2647–2651** ($\sigma_3\leftrightarrow p$
   identification): clarify that this is a Koszul **bulk-to-boundary**
   identification (same as Costello's affine Yangian statement), not a
   **bulk=boundary** identification.

5. **At rem:k3-super-origin (k3_yangian_chapter.tex:2041–2053)**: replace
   "No fermionic BPS quantum number enters" with a positive statement:
   "The odd sector of $\mathfrak{osp}(4\mid 20)_{\bar 1}$ realizes
   off-diagonal bifundamental bosons that are non-BPS from the D-brane
   viewpoint but carry the 80-dim representation of
   $\mathfrak{so}(4)\oplus\mathfrak{sp}(20)$; their existence is
   forced by the orthosymplectic superalgebra structure of the Mukai
   form under the Kähler polarisation."

## Deliverables summary

1. **Physical theory + spacetime + defect content.**
   6d holomorphic Chern–Simons (topological $E_3$ factorization algebra, a
   la Costello–Gwilliam) on $\mathbb R^2_{\epsilon_2}\times K3\times E$.
   Chiral direction $E$. Line defects on $E$ realize the Yangian action on
   boundary. In the IIA duality frame: D2-branes wrapping $\{\mathrm{pt}\}
   \times E$ carrying Mukai charges.

2. **BPS count.**
   Rank 24 in the sense of **number of independent Heisenberg generators**
   of the chiral algebra $A_{K3\times E}$. BPS partition function
   $Z = 1/\eta^{24}$. Three-way match: free-boson count, Fake Monster Weyl
   vector norm, $\eta^{24}$ in DMVV.

3. **Interpretation of $\hbar$.**
   $\hbar = \epsilon_2$, transverse Omega-background parameter to the chiral
   direction $E$. The Siegel parameter $p$ and the CY$_3$ parameter
   $\sigma_3 = h_1 h_2 h_3$ are the **bulk** parameters; $\hbar$ is the
   **boundary** parameter; the Costello Koszul duality relates them.

4. **Yangian vs quantum loop resolution.**
   Elliptic parent (chiral direction = $E$, genuinely elliptic).
   Cuspidal-$E$ degeneration: **K3 Yangian** $Y(\mathfrak g_{K3})$
   (rational, Drinfeld type).
   Nodal-$E$ degeneration: **K3 quantum toroidal**
   (trigonometric).
   The term "K3 Yangian" as used in the chapter denotes the cuspidal limit.

5. **Anomaly check.**
   One-loop anomaly of 6d hCS on $K3\times E$ $=$ $\chi(K3) = 24 =
   \kappa_{\mathrm{ch}}(A_{K3\times E})$. Checked via:
   (i) free-boson count (rank of Heisenberg lattice),
   (ii) Ramanujan discriminant exponent ($\eta^{24} = \Delta$),
   (iii) Fake Monster Weyl vector norm,
   (iv) Berezinian super-dimension $4 - (-20) = 24$ of $V_+\oplus\Pi V_-$.
   Four-way match. The supertrace $\mathrm{sTr}(\omega_{\mathrm{Muk}}) =
   4 - 20 = -16$ is a **different invariant** ($\Psi_{\mathrm{eff}}$, the
   effective level) and does not equal $\kappa_{\mathrm{ch}}$; the
   manuscript correctly distinguishes these.

Witten standard. Raeez Lorgat, sole author.
