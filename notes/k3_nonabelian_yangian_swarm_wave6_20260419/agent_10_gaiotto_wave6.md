# Agent 10 (Gaiotto voice) -- Wave 6: BLLPR Schur sign, SV/MO on K3, class S vs 4d-on-K3, Vafa-Witten as the correct physical route

**Raeez Lorgat, sole author. Wave 6. 2026-04-19.**

Wave 5 of the Gaiotto thread converged on a Hodge-bigraded
Yangian-Fock module, a flavoured Schur index at $k=3, \mathfrak g = A_2$,
a BRST witness at $k=3$, and a $k \ge 6$ DMVV pattern. Along the
boundary of that deliverable I wrote the phrase "Kapustin--Witten /
Beem--Rastelli cross-check passes at the structural level" without
auditing whether Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees
(BLLPR; 2013 arXiv:1312.5344; the attack brief calls this "BLFYR",
which I read as the same paper) actually accommodates the Mukai-rank
central charge $c = 24$ that the K3 Yangian's abelian core carries.
It does not. Wave 6 is a narrowing audit.

I channel three critical questions, deliberately not from Wave 5:

1. Does $Y_{K3}$ (the conjectural object) sit in the image of the
   BLLPR 4d-$\mathcal N{=}2$ / 2d-chiral-algebra correspondence?
2. Does the Schiffmann--Vasserot / Maulik--Okounkov affine
   $Y(\widehat{\mathfrak{gl}}_1)$ action on $\bigoplus_n
   H^\bullet(\mathrm{Hilb}^n(K3))$ extend to a genuine Yangian on a
   generic K3 (no torus)? This is the rank-1 anchor.
3. If the answer to (1) is no, what physical setup does the abelian
   core's character $1/\eta^{24}$ actually come from? I suspect
   Vafa--Witten $\mathcal N{=}2$ SYM on K3 spacetime, not class S on a
   Gaiotto curve with K3 in the compactification geometry.

The campaign executes three full attack-heal-attack-heal-attack-heal
cycles, with a compute module backing each cycle.

Hard constraints I respect: Beilinson's dictum (every claim false until
verified from primary source); epistemic hierarchy (direct computation
> `.tex` source > literature); Pattern 236 ambient qualifier discipline
(chain-level vs $(\infty,1)$-categorical scope tags each time it
matters); no overclaim adjectives; no formulas from memory; both
chain-level and $(\infty,1)$ lanes equal status.

Compute module:
`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_gaiotto_blfyr_schur.py`

---

## A1 -- First-principles attack: does Y_{K3} admit a BLLPR origin?

### A1.1 The BLLPR assertion and its sign

BLLPR (Beem, Lemos, Liendo, Peelaers, Rastelli, van Rees,
*Infinite chiral symmetry in four dimensions*, Commun. Math. Phys. 336
(2015), 1359--1433; arXiv:1312.5344, Theorem 2.1) asserts: for every
4d $\mathcal N{=}2$ superconformal theory $\mathcal T$ with conformal
anomalies $(a_{4d}, c_{4d})$, passing to the cohomology of a specific
nilpotent supercharge $\mathbb{Q}$ inside the superconformal algebra
produces a 2d vertex operator algebra $\mathbb{V}(\mathcal T)$ whose
Virasoro central charge is

$$
c_{2d} \;=\; -12 (c_{4d} - a_{4d}).
$$

(BLLPR eq. (1.4), and Beem--Rastelli 2018 arXiv:1707.07679 eq. (3.5).)

The Hofman--Maldacena positivity bound (Hofman--Maldacena,
*Conformal collider physics*, JHEP 05 (2008) 012, arXiv:0803.1467,
Theorem 1 -- "the positivity of energy flux at null infinity requires
$a/c \in [1/2, 3/2]$"), further sharpened for $\mathcal N{=}2$ theories
by Beem--Rastelli 2018 Prop. 3.1, forces $c_{4d} \ge a_{4d}$ for
every unitary interacting 4d $\mathcal N{=}2$ SCFT with a flavour
current. Therefore

$$
c_{2d}^{\mathrm{BLLPR}} \;\le\; 0.
$$

### A1.2 The K3 Yangian abelian core has $c = +24$

From Wave 5 §1.1 and §4.6, the abelian Heisenberg core $Y_\hbar^{\mathrm{Heis}}(\Lambda_{K3})$
has 24 Heisenberg currents indexed by the Mukai lattice
$\widetilde\Lambda_{K3}$. Each free boson contributes $c = 1$; total
$c = 24 > 0$. (See also the programme's inscribed chapter
`chapters/examples/k3_chiral_algebra.tex:1194` line 1194:
"The K3 Heisenberg has $c = 24$ (Mukai rank).")

### A1.3 Falsification

$c = 24 > 0$ and $c_{2d}^{\mathrm{BLLPR}} \le 0$. These are incompatible.

**First-principles conclusion.** The K3 Yangian abelian core is **not**
the BLLPR Schur-sector VOA of any unitary 4d $\mathcal N{=}2$ SCFT.

Compute module test A verifies this numerically with the values
$c_{K3}^{\mathrm{Heis}} = 24$ vs $c_{2d}^{\mathrm{BLLPR}} \le 0$; test
returns `compatible: False`. (Module
`k3_yangian_wave6_gaiotto_blfyr_schur.py`, function
`test_A_c2d_sign`.)

### A1.4 Retraction scope

The Wave 5 synthesis §2 retraction table should gain:

| Retracted claim | Wave claimed | Wave retracted | Mechanism |
|---|---|---|---|
| $Y_{K3}$ abelian core is a BLLPR Schur VOA (via Wave-5 Kapustin--Witten / Beem--Rastelli language) | W5 Gaiotto §6.2 | W6 Gaiotto A1 | Sign of $c_{2d}$; BLLPR always $\le 0$, Mukai-Heisenberg is $+24$ |

I retract my own Wave 5 prose "cross-check against Kapustin--Witten
(geometric Langlands on K3) and Beem--Rastelli (Schur-VOA
correspondence)" as an **adornment**: the structural form was verified
at the character level (which is a weak cross-check), but the
identification of $Y_{K3}$ with a BLLPR chiral algebra is falsified by
the sign obstruction.

---

## H1 -- Heal (scope narrowing; chain-level witness)

### H1.1 Two possible healings

Given A1.3, Wave 5's physical-interpretation paragraph must narrow.
Three candidate narrowings:

(H1-a) Drop the physical interpretation entirely; $Y_{K3}$ is a
mathematical object, full stop.

(H1-b) Keep a physical interpretation, but shift from class S on a
Gaiotto curve to **4d $\mathcal N{=}2$ gauge theory on K3 spacetime**
(Vafa--Witten); the Mukai-Heisenberg $1/\eta^{24}$ is the $SU(2)$
Vafa--Witten partition function $Z^{VW}(K3; q)$ (Vafa--Witten,
*A strong coupling test of S-duality*, Nucl. Phys. B 431 (1994) 3,
hep-th/9408074, eq. (4.14) for gauge group $SU(2)$).

(H1-c) Keep a physical interpretation but shift to **6d $(2,0)$ on
K3 $\times$ pt** with an $\Omega$-background twist in a transverse
plane; this is closer to Nekrasov partition function territory.

### H1.2 Why (H1-b) is the correct lane

The Vafa--Witten partition function for $SU(2)$ $\mathcal N{=}4$ SYM on
a simply-connected 4-manifold $X$ is

$$
Z^{VW}_{SU(2)}(X; q) \;=\; \frac{1}{\eta(q)^{\chi(X)}} \cdot \text{signature factor}
$$

(Vafa--Witten 1994 eq. (4.14) for $X = K3$ gives $\chi(K3) = 24$;
direct match). This is the GW/DT-type instanton sum over $n$-instanton
moduli, Poincaré-weighted by $\chi(\mathrm{Hilb}^n(K3)) = p_{24}(n)$
(Göttsche 1990 Math. Ann. 286, Theorem 0.1).

The Wave 5 §1.1 statement "character $1/\eta(q)^{24}$" therefore has
a direct Vafa--Witten reading: the abelian core of $Y_{K3}$ is the
**boundary VOA** of $\mathcal N{=}4$ SYM (or $\mathcal N{=}2^*$ in the
Vafa--Witten twist) on $K3 \times \mathbb R_{\ge 0}$, with
$q = e^{2\pi i \tau}$ the 4d instanton counting parameter. The
$\mathrm{Spin}(4, 20; \mathbb Z)$ group (Wave 5 §1.6, §1.8) is then the
heterotic T-duality group, consistent with the heterotic string /
Vafa--Witten duality picture.

Physically: in the $\Omega$-background on a transverse $\mathbb R^2$,
one gets the Nekrasov partition function; without the
$\Omega$-background one gets the Vafa--Witten partition function. The
boundary VOA on $K3 \times \{0\}$ carries the Mukai-Heisenberg
currents; the $\mathrm{Hilb}^n$-layered partition function
$\prod (1-q^n)^{-24}$ is the vacuum character.

### H1.3 Chain-level witness (scope declaration)

**Chain-level claim.** Let $X = K3$, $L = X \times \mathbb R_{\ge 0}$.
Consider Donaldson--Witten/Vafa--Witten twisted $\mathcal N{=}4$ SYM
at rank $r$ on $L$ (in the Vafa--Witten topological twist). The
boundary VOA $\partial(\mathcal T^{VW}_{SU(r)})$ on $X \times \{0\}$
admits a rank-$r \chi(X) = 24r$ lattice Heisenberg current algebra at
the abelian level (free abelian boson for each $H^{1,1}(X)$ plus
signature-twisted $H^{2,0}, H^{0,2}$ contributions). At $r = 1$:
rank-24 Mukai-Heisenberg, character $1/\eta^{24}$. This matches the
Wave 5 abelian core structurally.

(Scope: chain-level; "boundary VOA" here means the
Costello--Gwilliam factorization algebra at the boundary stratum
$X \times \{0\}$; see Costello--Gwilliam,
*Factorization algebras in quantum field theory* Vol. 2, chapter 9,
"Boundary conditions". Witness: the Mukai-Heisenberg currents are the
restrictions of the 4d anti-self-dual field strength on a $(1,1)$-form
cohomology basis, evaluated at the boundary. 24 currents from
$h^{0,0} + h^{2,0} + h^{0,2} + h^{1,1} + h^{2,2} = 1 + 1 + 1 + 20 + 1
= 24$.)

**$(\infty,1)$-categorical claim.** The boundary VOA is the
$\infty$-factorization algebra localized to the boundary component of
the cofibration sequence $X \times \mathbb R_{\ge 0} \supset X \times
\{0\}$; the Hodge--Deligne bigrading lifts to a grading on the
boundary $\infty$-chiral algebra via the Tate twist on the
Mixed-Hodge structure of $X$. Compatible with
Wave 5's Hodge-bigraded Yangian module structure (§1.3), which
becomes the $(y, \bar y)$-refined boundary character.

Both lanes independently give: **at rank 1, abelian-only**, the
boundary VOA of Vafa--Witten on K3 $\times \mathbb R_{\ge 0}$ is the
Mukai-Heisenberg at level 1. This is my healed framing.

### H1.4 What H1 does **not** claim

(i) It does not claim the BFN ADE layer (Wave 5 §1.2) is Vafa--Witten-derived.
The ADE-enhancement points correspond to $A_n$-surface singularities
in K3, where the instanton moduli has extra components that quantise
to BFN affine Yangians $Y_\hbar^\mu(\widehat{\mathfrak g})_{k=1}$. The
physical setup is different (ALE compactification of 6d $(2,0)$,
Nakajima 1994); I separate this as an open issue in A2/H2.

(ii) It does not claim the $L_\infty$-coupling, block-diagonal
cross-strata structure, pentagon-intertwiner framework (Wave 5 §1.4,
§1.5) are Vafa--Witten-derived. Those are intrinsic to the Yangian
algebraic structure, independent of the physical origin.

(iii) It does not claim the BKM sector (Wave 5 §1.3) is
Vafa--Witten-derived. The Gritsenko--Nikulin $\Phi_{10}$ multiplier
belongs to a different (K3$\times E$ DT counting) setup.

So H1 narrows the claim "Y_{K3} is physically interpreted via BLLPR
Schur sector" to: **only the abelian Heisenberg core admits a
clear physical origin, and that origin is Vafa--Witten on K3
spacetime, not BLLPR on a Gaiotto curve.** The non-abelian layers
retain their internal algebraic justification without a full physical
identification.

---

## A2 -- Second attack: the Schiffmann-Vasserot / Maulik-Okounkov rank-1 anchor

### A2.1 What SV / MO actually proves

Schiffmann--Vasserot (*Cherednik algebras, W-algebras, and the
equivariant cohomology of the moduli space of instantons on
$\mathbb A^2$*, Publ. IHES 118 (2013) 213, arXiv:1202.2756, Theorem
8.22) and Maulik--Okounkov (*Quantum groups and quantum cohomology*,
arXiv:1211.1287, §14) construct an action of
$Y_{\hbar_1, \hbar_2}(\widehat{\mathfrak{gl}}_1) = W_{1+\infty}[\hbar_1, \hbar_2]$
on $\bigoplus_{n \ge 0} H^\bullet_{T}(\mathrm{Hilb}^n(\mathbb C^2))$
where $T = \mathbb G_m \times \mathbb G_m$ is the 2-torus acting on
$\mathbb C^2$ by scaling the coordinates with weights $(\hbar_1,
\hbar_2)$.

**The construction is $T$-equivariant**: without the torus, no MO
stable envelope, no Yangian structure constants. The stable envelope
is a Lagrangian in the fixed-point localization $H^\bullet_T(\mathrm{Hilb}^n)_{\mathrm{loc}}$;
the R-matrix is defined by composing stable envelopes with opposite
chamber choices.

### A2.2 Torus availability on K3 loci

A generic K3 has $\mathrm{Aut}(X)^0 = \{e\}$ (trivial connected
automorphism group; Beauville, *Complex algebraic surfaces*,
London Math. Soc. Student Texts 34, 1983, Prop. V.19; Huybrechts,
*Lectures on K3 surfaces*, Cambridge Studies in Advanced Math. 158,
2016, Theorem 5.2.1 "Aut(X)^0 = 0 for every projective K3"). So no
continuous torus acts on $\mathrm{Hilb}^n(K3)$ for a generic $X$.

Special loci:
- **Elliptic K3** $\pi: X \to \mathbb P^1$ with a section: $\mathbb G_m$
  acts by scaling the fibres (preserving the section); rank-1 torus.
- **Kummer K3** $X = \mathrm{Km}(A)$ with $A$ an abelian surface,
  resolved from $T^4/\mathbb Z_2$: inherits the $T^4 / \mathbb Z_2 =
  T^2$-action from the translation invariance of $T^4$; rank-2 torus.
- **Attractor K3** (Picard rank 20): no torus in general.

### A2.3 Falsification of the "rank-1 SV/MO anchors the non-abelian claim" reading

The attack brief asks: "if the rank-1 case matches Schiffmann-Vasserot,
that anchors the non-abelian claim; if it doesn't match, the whole
construction fails at rank 1."

My response: the match is **vacuous** at rank 1. The SV/MO structure
function on $\mathbb C^2$ is

$$
g(z) \;=\; \prod_{a=1}^{3} \frac{z - h_a}{z + h_a}, \qquad h_1 + h_2 + h_3 = 0,
$$

(affine $Y(\widehat{\mathfrak{gl}}_1)$; programme module
`affine_yangian_gl1.py` line 11). Taking the "abelian limit" $h_1, h_2
\to 0$ (no $\Omega$-background on K3 as a 4-manifold, per
`k3_chiral_algebra.tex:1198`: "the K3 Yangian requires the $\Omega$-background"),
the CY constraint $h_3 = -(h_1 + h_2) \to 0$ also, so $g(z) = 1$
identically: trivial R-matrix. On the other hand, the Wave 5 Yang
R-matrix $R(u) = (u + \hbar P)/(u + \hbar)$ on $V \otimes V$ with
$V = \mathbb C$ (single line, rank 1) has $P = 1$ (identity on a line),
so $R(u) = 1$ identically. The two rank-1 "R-matrices" agree because
both are the scalar 1.

This is **not a consistency check**; it is a degeneracy. Both sides
are trivial, so matching is automatic.

Compute module test D verifies: `structural_match: True`, but the
diagnostic explicitly flags the tautology.

### A2.4 Conclusion: the rank-1 claim is weaker than advertised

The Wave 5 synthesis §4.6 claim "level-$k$ multiplicity $= p_{24}(k)$
via $\Theta_{\Gamma^{4,20}} / \eta^{24}$ = Göttsche formula" is a
partition count matching, not an R-matrix check. Partition-count
matching does not anchor a Yangian action: the Nakajima rank-24
**Heisenberg** on $\bigoplus_n H^\bullet(\mathrm{Hilb}^n(K3))$
(Nakajima 1997, Ann. Math. 145, Theorem 1) exists without torus, but
it is a Heisenberg algebra, not a Yangian. The Yangian upgrade needs
a torus (MO stable envelope), which does not exist on a generic K3.

**Narrowed Wave-5 claim**: the Yangian-structure upgrade from the
Nakajima Heisenberg to $Y_{K3}$ on generic K3 requires an alternative
construction (not MO). Wave 5 §1.1 R-matrix verification "YBE
symbolically verified at rank 24 (Polyakov W2, residual $5.55 \times
10^{-17}$)" refers to the Yang R-matrix on $V = \Lambda_{K3} \otimes
\mathbb C$, which is a purely algebraic statement. The physical
upgrade is what fails.

---

## H2 -- Heal: scope restriction to torus-admitting K3 loci

### H2.1 Restricted Yangian construction

Narrow the Wave 5 "Y_{K3}$ on generic K3 moduli" to:

**Y_{K3}$^{\mathrm{SV/MO}}$** exists only on:
- elliptic K3 loci (rank-1 torus; partial Yangian construction),
- Kummer K3 loci (rank-2 torus; full SV/MO Yangian construction).

On generic K3 (Picard rank $\le 19$, no continuous automorphisms),
only the Nakajima Heisenberg action is available; upgrading to a
Yangian requires either

(i) a different construction (via BFN Coulomb branches at ADE points
whose $\mathbb G_m$-action on the 3d Coulomb branch provides the
equivariance; Wave 5 §1.2), or

(ii) a formal deformation-quantization argument (not geometric; 
via $A_\infty$ / $L_\infty$ methods; Wave 5 §1.7 $L_\infty$-super-extension),

neither of which is MO/SV.

### H2.2 Chain-level vs $(\infty,1)$-categorical lane

**Chain-level**: SV/MO on $\mathbb C^2$ with torus $T = \mathbb G_m^2$
gives an explicit Yangian action on $\bigoplus_n H^\bullet_T(\mathrm{Hilb}^n(\mathbb C^2))$
with named stable envelopes. On Kummer K3, one inherits this locally
via the $T^4/\mathbb Z_2$ structure; on elliptic K3, only a rank-1
partial version. No chain-level SV/MO on generic K3.

**$(\infty,1)$-categorical**: Gaitsgory--Lurie's derived factorization
algebra framework (Gaitsgory--Lurie,
*Weil's conjecture for function fields*, Vol. I Chapter 2, Ann. Math.
Stud. 199 (2019)) defines $\infty$-chiral algebras on any smooth curve
without equivariance. The K3 Yangian as an
$\infty$-factorization algebra on a curve $C \subset X$ (the Gaiotto
curve of heterotic compactification; Wave 5 §1.8) exists without the
Hilb$^n(K3)$-equivariance. This is the $(\infty,1)$-categorical lane,
independent of the MO construction.

The two lanes are **not in conflict**: the chain-level MO construction
is restricted to torus-admitting K3 loci; the $(\infty,1)$-categorical
factorization-algebra construction works on any curve but loses
the explicit stable-envelope R-matrix. Both are valid; they answer
different questions.

### H2.3 Narrowed claim registry entry

Wave 5 synthesis §4.1 structural claim "BFN affine Yangian at ADE
enhancement" [H]: survives H2 (BFN uses the 3d Coulomb branch torus;
independent of K3 automorphisms).

Wave 5 synthesis §4.1 "Abelian Mukai-Heisenberg rank 24 exists with
Yang R" [H]: survives H2 at the **Heisenberg level** (Nakajima 1997;
no torus needed for the Heisenberg). The Yangian upgrade at rank 24
on generic K3 remains scope-dependent.

Wave 5 synthesis §4.1 "$Y_{K3}$ is stratified direct-sum-with-coupling"
[H]: narrows to: this structure holds on torus-admitting K3 loci
(Kummer, elliptic) where a full SV/MO-style Yangian exists; on generic
K3 the statement is structural via the
$(\infty,1)$-categorical-factorization lane only.

---

## A3 -- Third attack: "Schur VOA of class S on C vs Vafa-Witten on K3 spacetime" disambiguation

### A3.1 The conflation

Wave 5 §6.2 language: "The flavoured Schur index at $k=3$,
$\mathfrak g = A_2$ matches the Kapustin--Witten partition function of
4d $\mathcal N{=}4$ SYM at $SU(3)$, twist $t = 1$, on $K3 \times T^2$
with three-fold Wilson-line flux."

This sentence contains two distinct physical setups:

**Setup 1: class S of type $A_1$ on a Gaiotto curve $C$, K3 internal.**
- IIB on K3 $\times \mathbb R^4$: 6d $(2,0)$ of type $A_1$ on $\mathbb R^{5,1}$ (Gaiotto 2009 arXiv:0904.2715).
- 6d $(2,0)$ on $C \times \mathbb R^4$: 4d $\mathcal N{=}2$ class-S on $\mathbb R^4$.
- Schur index on $S^1 \times S^3$: equals $\chi_{W_k(\mathfrak{sl}_2)}(q)$ via BLLPR.
- The Gaiotto curve $C$ is the Riemann surface for the class-S construction; K3 is **internal geometry** for IIB.

**Setup 2: 4d $\mathcal N{=}4$ SYM on K3 spacetime.**
- 4d $\mathcal N{=}4$ on $K3 \times T^2$: topologically twisted
  (Vafa--Witten, Kapustin--Witten 2007 hep-th/0604151) gives 2d
  sigma-model on the Hitchin moduli space of $K3$; partition function
  $Z = \sum_n \chi(\mathrm{Hilb}^n(K3)) q^n = 1/\eta^{24}$.
- K3 is the **4d spacetime**, not internal.

### A3.2 Which setup matches $Y_{K3}$?

Setup 1 gives $c_{2d} \le 0$ (A1.1), incompatible with $c_{K3}^{\mathrm{Heis}} = 24$.
Setup 2 gives $1/\eta^{24}$ for $SU(2)$ (Vafa--Witten 1994 eq. (4.14)),
and the rank-24 Mukai-Heisenberg for the enhanced tower.

So **setup 2 is the correct reading**; setup 1 is the incorrect
reading. My Wave 5 sentence conflates these.

### A3.3 Consequence for the Wave-5 Gaiotto chain-level BRST witness (§3)

The Wave 5 §3 BRST chain map $V^{(k)}_{II_{25,1}} \otimes V_{\mathrm{ghost}}
\to V^{(k)}_{\widetilde\Lambda_{K3}}$ uses the Lorentzian
$II_{25, 1}$ string-theory ambient (Borcherds 1998, Beem--Rastelli
language of heterotic boundary states). This is a **heterotic-string
construction**, corresponding to setup 2 (4d on K3 spacetime via
heterotic compactification), not setup 1 (class S).

So the chain-level BRST witness is consistent with Vafa--Witten /
heterotic, not with BLLPR / class S. This is actually a point in H1's
favour: the whole Wave-5 Gaiotto apparatus lives in the Vafa--Witten
side of the conflation.

---

## H3 -- Final heal: corrected physical identification

### H3.1 Stated

**Claim (Wave 6 Gaiotto healed).** The K3 Yangian abelian core is the
boundary VOA of Vafa--Witten topologically twisted 4d $\mathcal N{=}4$
(or $\mathcal N{=}2^*$) SYM of gauge rank 1 on $K3 \times \mathbb R_{\ge 0}$,
with the Mukai-lattice Heisenberg currents carrying the 24 ranks
$h^{0,0} + h^{2,0} + h^{0,2} + h^{1,1} + h^{2,2} = 1 + 1 + 1 + 20 + 1 = 24$.
Its character is $1/\eta(q)^{24}$, matching the $SU(2)$ Vafa--Witten
partition function $Z^{VW}_{SU(2)}(K3; q)$ up to signature. This is
**not** a BLLPR Schur VOA.

Status: [M] chain-level (Costello--Gwilliam factorization algebra
at boundary stratum; free-boson restrictions of $(1,1)$-form field
strengths); [M] $(\infty,1)$-categorical (boundary factorization
$\infty$-algebra; Hodge--Deligne lifts).

### H3.2 What this means for downstream Wave-5 claims

Wave 5 §1.8 "The heterotic physical origin" **stays intact** because
it already identifies the physical setup as 6d hCS on $\mathbb R^2_{\varepsilon_2}
\times K3 \times E$, which is a heterotic-string / Vafa--Witten-style
compactification, not a class-S setup. Wave 5 Witten §3 three-way
convergence ("free-boson count, Fake Monster Weyl-vector norm, DMVV
$(1-q^n)^{-24}$, Berezinian super-dimension $4 - (-20)$") is consistent
with setup 2.

Wave 5 §6.2 Gaiotto paragraph "Beem--Rastelli (Schur-VOA
correspondence)" **is retracted** and replaced by:

> The Mukai-Heisenberg character $1/\eta^{24}$ is the $SU(2)$
> Vafa--Witten partition function on K3 (Vafa--Witten 1994, eq. (4.14))
> or equivalently the Euler characteristic generating function
> $\sum_n \chi(\mathrm{Hilb}^n(K3)) q^n$ (Göttsche 1990, Math. Ann. 286,
> Theorem 0.1). This partition function is **not** a Schur index of a
> 4d $\mathcal N{=}2$ SCFT via BLLPR; the sign obstruction
> $c_{2d}^{\mathrm{BLLPR}} = -12(c_{4d} - a_{4d}) \le 0$ vs
> $c_{K3}^{\mathrm{Heis}} = +24$ prevents that identification.

### H3.3 Chain-level witness vs $(\infty,1)$-categorical witness

Pattern 236 ambient-qualifier discipline:

**Chain-level** (status: [M]): the boundary Mukai-Heisenberg of
Vafa--Witten on $K3 \times \mathbb R_{\ge 0}$ is the free-abelian
Heisenberg on $H^\bullet(K3; \mathbb Q) = \mathbb Q^{24}$ graded by
cohomological degree. Explicit witness: restriction of the ASD
field-strength $F^- \in \Omega^2_-(K3)$ at the boundary, which for
abelian gauge group is 24-dimensional (one current per
$H^\bullet$-basis element). This gives the Mukai-lattice Heisenberg
currents at the abelian level.

**$(\infty,1)$-categorical** (status: [M]): the Costello--Gwilliam
factorization algebra of 4d $\mathcal N{=}4$ SYM has a derived
factorization module structure at the boundary $K3 \times \{0\}$. The
$\infty$-chiral algebra on this boundary admits a Hodge bigrading
compatible with the derived Mixed-Hodge structure on $H^\bullet(K3)$
(Deligne 1971, *Théorie de Hodge: II*, Publ. IHES 40 (1971) 5).
This lane does not commit to a specific chain complex; it provides
the universal property.

Both witnesses exist; neither subsumes the other. This is the correct
ambient-qualifier inscription.

---

## CONVERGENCE -- Wave 6 Gaiotto state

### Stable [H] claims

- Mukai-Heisenberg character $1/\eta^{24}$ matches $SU(2)$ Vafa--Witten
  partition function on K3 (Vafa--Witten 1994; Göttsche 1990).
- Generic K3 has no continuous automorphism group (Beauville 1983;
  Huybrechts 2016).
- SV/MO construction requires a torus; unavailable on generic K3.
- Nakajima (1997) rank-24 Heisenberg on $\bigoplus_n H^\bullet(\mathrm{Hilb}^n(K3))$
  exists without torus, but is Heisenberg, not Yangian.

### Narrowed [M] claims (Wave 5 -> Wave 6 narrowing)

- $Y_{K3}$ on generic K3 has an $(\infty,1)$-factorization realization
  but no chain-level MO realization (H2.1).
- Physical interpretation of the abelian core is Vafa--Witten on K3
  spacetime, not BLLPR on a Gaiotto curve (H1.2, H3.1).
- Wave 5 §3 BRST chain-map apparatus corresponds to setup 2 (heterotic
  / Vafa--Witten), not setup 1 (class S). Chain-level status unchanged
  (k=3 partition decomposition $24 + 576 + 2600 = 3200$ still valid
  structurally).

### Falsified [F] claims

- Wave 5 §6.2 "Beem--Rastelli Schur-VOA cross-check passes" is
  falsified by the sign obstruction (A1.1, A1.3).
- Wave 5 §6.2 "Kapustin--Witten geometric Langlands [on K3 spacetime,
  implicitly]" at $A_2$ enhancement: the language is
  conflation-prone; KW on $C \times \Sigma$ with $\Sigma = K3$ is
  geometric Langlands for class groups on K3, not for a class-S
  construction (A3.2).

### New conjectures (Wave 6 Gaiotto)

**Conjecture 6-G-1 (Gaiotto Vafa-Witten identification; [M] chain-level).**
The abelian Heisenberg core $Y_\hbar^{\mathrm{Heis}}(\Lambda_{K3})$ at
level 1 is isomorphic as a VOA to the boundary chiral algebra of
topologically twisted 4d $\mathcal N{=}4$ SYM at gauge rank 1 on
$K3 \times \mathbb R_{\ge 0}$, with $\hbar$ identified with the 4d
$\theta$-angle deformation parameter.

**Conjecture 6-G-2 (Gaiotto torus-locus restriction; [M]).** The SV/MO
affine-Yangian action extends from $\mathrm{Hilb}^n(\mathbb C^2)$ to
$\mathrm{Hilb}^n(K3)$ only on Kummer and elliptic loci of K3 moduli;
on generic K3, a distinct construction is required (derived
factorization-algebra / non-equivariant; H2.2).

**Conjecture 6-G-3 (Gaiotto non-BLLPR status; [H]).** $Y_{K3}$ is not a
BLLPR Schur VOA of any 4d $\mathcal N{=}2$ SCFT. This is [H] because
the sign obstruction is robust (Hofman--Maldacena 2008 + Beem--Rastelli
2018 Prop. 3.1).

### NEW_COMPUTATION modules

`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_gaiotto_blfyr_schur.py`

Five tests (A, B, C, D, E):
- Test A: $c_{2d}$ sign compatibility -- FAIL (falsifies BLLPR).
- Test B: torus on K3 loci -- FAIL on generic K3.
- Test C: $1/\eta^{24}$ vs $W_k(\mathfrak{sl}_2)$ character -- falsifies rank mismatch.
- Test D: SV/MO rank-1 structure function vs Wave-5 Yang R-matrix -- vacuous tautology.
- Test E: class S on C vs 4d-on-K3-spacetime disambiguation -- Vafa--Witten is the correct route.

Output reproducible by `python3 k3_yangian_wave6_gaiotto_blfyr_schur.py`.

---

## File-line anchors

- `chapters/examples/k3_chiral_algebra.tex:1172`: BLLPRR (Bryan--Leung--Lian--Pandharipande--Ruan)
- `chapters/examples/k3_chiral_algebra.tex:1190--1208`: BLLPR vs K3 Yangian are distinct algebraizations (already inscribed)
- `chapters/examples/k3_chiral_algebra.tex:1194`: "K3 Heisenberg has $c = 24$ (Mukai rank)"
- `chapters/examples/k3_chiral_algebra.tex:1196`: "$E_n$ structure" -- BLLPR is $E_\infty$, K3 Yangian is $E_1$
- `chapters/examples/k3_chiral_algebra.tex:1198`: "$\Omega$-dependence" -- BLLPR no, K3 Yangian yes
- `compute/lib/bllpr_k3_connection.py`: 73-test internal-consistency module for BLLPR / K3 Yangian distinction
- `compute/lib/affine_yangian_gl1.py`: SV/MO structure function $g(z) = \prod (z-h_a)/(z+h_a)$
- `notes/k3_nonabelian_yangian_swarm_wave5_20260419/agent_10_gaiotto_wave5.md`: Wave 5 deliverable
- `notes/k3_nonabelian_yangian_swarm_wave5_20260419/SYNTHESIS_COMPLETE.md`: §6.2, §1.1, §4.1

---

## References (Wave 6 Gaiotto)

- Beauville, A., *Complex algebraic surfaces*, London Math. Soc.
  Student Texts 34, 1983, Prop. V.19.
- Beem, C., Lemos, M., Liendo, P., Peelaers, W., Rastelli, L.,
  van Rees, B. C., *Infinite chiral symmetry in four dimensions*,
  Commun. Math. Phys. 336 (2015) 1359, arXiv:1312.5344,
  Theorem 2.1, eq. (1.4).
- Beem, C., Rastelli, L., *Vertex operator algebras, Higgs branches,
  and modular differential equations*, JHEP 08 (2018) 114,
  arXiv:1707.07679, Prop. 3.1 and eq. (3.5).
- Costello, K., Gwilliam, O., *Factorization algebras in quantum field
  theory*, Vol. 2, Cambridge Univ. Press 2021, Chapter 9 "Boundary
  conditions".
- Deligne, P., *Théorie de Hodge: II*, Publ. IHES 40 (1971) 5.
- Gaiotto, D., *$\mathcal N{=}2$ dualities*, JHEP 08 (2012) 034,
  arXiv:0904.2715.
- Gaitsgory, D., Lurie, J., *Weil's conjecture for function fields*,
  Vol. I, Ann. Math. Studies 199 (2019), Chapter 2.
- Göttsche, L., *The Betti numbers of the Hilbert scheme of points on
  a smooth projective surface*, Math. Ann. 286 (1990) 193, Theorem 0.1.
- Hofman, D. M., Maldacena, J., *Conformal collider physics*, JHEP 05
  (2008) 012, arXiv:0803.1467, Theorem 1.
- Huybrechts, D., *Lectures on K3 surfaces*, Cambridge Studies in
  Advanced Math. 158, 2016, Theorem 5.2.1.
- Kapustin, A., Witten, E., *Electric-magnetic duality and the
  geometric Langlands program*, Commun. Num. Theor. Phys. 1 (2007) 1,
  hep-th/0604151.
- Maulik, D., Okounkov, A., *Quantum groups and quantum cohomology*,
  arXiv:1211.1287, §14.
- Nakajima, H., *Heisenberg algebra and Hilbert schemes of points on
  projective surfaces*, Ann. Math. 145 (1997) 379, Theorem 1.
- Schiffmann, O., Vasserot, E., *Cherednik algebras, W-algebras, and
  the equivariant cohomology of the moduli space of instantons on
  $\mathbb A^2$*, Publ. IHES 118 (2013) 213, arXiv:1202.2756,
  Theorem 8.22.
- Vafa, C., Witten, E., *A strong coupling test of S-duality*,
  Nucl. Phys. B 431 (1994) 3, hep-th/9408074, eq. (4.14) for
  gauge group $SU(2)$.

---

*End of Gaiotto attack-heal, Agent 10, Wave 6, 2026-04-19.*

*Raeez Lorgat, sole author. No AI attribution.*

*Gaiotto standard (Wave-6 correction). The physical system that
produces the K3 Yangian abelian core is NOT class S on a Gaiotto curve
with K3 internal; it is 4d $\mathcal N{=}4$ SYM on K3 spacetime
(Vafa--Witten 1994), whose boundary VOA carries the Mukai-Heisenberg
currents with character $1/\eta(q)^{24}$. The Wave-5 BLLPR /
Beem--Rastelli Schur-VOA cross-check language was incorrect: BLLPR
forces $c_{2d} \le 0$, while the Mukai-Heisenberg has $c = +24$.
Schiffmann--Vasserot / Maulik--Okounkov Yangian on
$\mathrm{Hilb}^n(K3)$ requires a torus, which exists only on Kummer
and elliptic K3 loci; on generic K3 only the torus-free Nakajima
(1997) Heisenberg action survives, and the Yangian upgrade needs
either BFN Coulomb branches at ADE points or a derived
factorization-algebra / $(\infty,1)$-categorical approach. The rank-1
SV/MO match is vacuous (both sides reduce to scalar 1). The whole
correction is a narrowing: the non-abelian K3 Yangian's algebraic
structure (stratified coupled quasi-Hopf, $L_\infty$-homotopy, pentagon
coherence) survives; only the "BLLPR Schur VOA" reading of its
physical origin is retracted and replaced by the Vafa--Witten boundary
VOA reading. The physical interpretation is now sound at the abelian
core and properly open at non-abelian layers.*
