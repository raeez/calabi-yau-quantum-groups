# Agent 05 --- Nekrasov on the Non-Abelian K3 Yangian, Wave 6

*Voice*: partition functions first, interpretation second. Wave 5
concluded the Yangian was a stratified-coupled $L_\infty$-quasi-Hopf
object with level shift $k \to k + 12 + h^\vee$. Wave 6 attacks the
level shift at its root (the integer 12), re-opens the Omega-background
question, audits the BFN reduction, and sets one concrete
falsification (OEIS-tail regression) as a matter of record.

*Raeez Lorgat, sole author.*

---

## 0. Audit findings before the attacks begin

Before any attack-heal cycle, two structural audit findings are
recorded and will not be revisited further in this document:

1. **Wave 4 Nekrasov file is absent from disk.** The directory
   `notes/k3_nonabelian_yangian_swarm_wave4_20260419/` contains
   agents 01, 02, 03, 04, 06, 08, 09, 10 but is missing
   `agent_05_nekrasov_wave4.md` (and also agents 07 Drinfeld and 05
   Nekrasov for wave4). The Wave 5 Nekrasov file at
   `notes/k3_nonabelian_yangian_swarm_wave5_20260419/agent_05_nekrasov_wave5.md`
   references Wave-4 Nekrasov claims as though they existed on disk
   ("Wave 4 verified the third grading $p$ at $k=3,4,5$"). There is
   therefore a single-source provenance gap: Wave-5's extension of
   Wave-4 claims has no disk-witnessed Wave-4 statement to fall back
   on. Either Wave 4 Nekrasov was delivered orally in the Wave-5
   synthesis stream and never inscribed, or the file was lost.
   **Orientation for Wave 6:** treat the Wave-5 synthesis as Wave-5-
   inscribed only, not as Wave-4-corroborated. This flags the Wave-5
   `[H]` confidence tags on the Hodge-bigraded $\chi_{y,\bar y}$
   partition function and the OEIS-A006922 sequence as
   single-wave-sourced rather than two-wave-corroborated.

2. **OEIS A006922 tail regression.** Wave-5 Nekrasov W5 §3.5 verified
   $p_{24}(6), p_{24}(7), p_{24}(8) = (1\,073\,720, 5\,930\,496,
   30\,178\,575)$ via three paths and correctly falsified a prompt
   error. Wave-6 this agent re-computed $p_{24}(k)$ for $k \le 12$
   via three independent paths (Euler recurrence, direct
   $\prod(1-q^n)^{-24}$ multiplication with binomial expansion, sympy
   symbolic). All three paths agree on
   $(p_{24}(10), p_{24}(11), p_{24}(12)) = (639\,249\,300,
   2\,705\,114\,880, 10\,914\,317\,934)$.
   See `compute/lib/k3_yangian_wave6_nekrasov_level_shift.py`.
   The prompt of the current Wave-6 task cites Wave-5 SYNTHESIS which
   extends the sequence beyond $n = 9$; the extension carries a
   single-path memory attribution that disagrees at $n = 10$ with
   three-path computation by the values $(648\,454\,899,
   2\,825\,116\,440, 11\,867\,256\,960)$. Those three numbers are
   **not** $p_{24}(k)$ at $k = 10, 11, 12$, and I do not know what
   sequence they are.

   This is small in magnitude (one OEIS tail) but large in discipline:
   *memory-sourced "OEIS lookups" should not count as independent
   verification paths*. A genuine verification path for $p_{24}(k)$ at
   $k = 10, 11, 12$ is one of:
   (a) direct expansion; (b) Euler recurrence; (c) Nakajima's
   Fock-space character formula specialised to $\chi(\mathcal O_{K3})
   = 2, \chi(K3) = 24$; or (d) a published table in a paper I can
   cite. Memory of an OEIS tail is *not* one of these.

Both findings are documented with the audit finding tag in the
confidence table at §6.

---

## 1. Round A1 --- Attack the level shift $k \to k + 12 + h^\vee$

### 1.1 The attack

Wave 5 SYNTHESIS §1.6 claims six cross-checks support the **additive**
level shift $k \to k + 12 + h^\vee$ with the integer $12$ asserted as
$\chi(K3)/2$.

The integer $12$ has at least **three independent provenances** in K3
topology, and Wave 5 conflates them:

| Candidate | Value | Invariant | Role |
|:---|:---:|:---|:---|
| $\chi^{\text{top}}(K3) / 2$ | $12$ | Euler characteristic half | one-loop supertrace; elliptic-genus $z=0$ coefficient |
| $c_2(K3) / 2$ | $12$ | second Chern class half | index of Atiyah-Singer on the tangent bundle |
| $\sigma(K3)$ | $-16$ | signature (L-genus) | self-dual minus anti-self-dual 2-form count |
| $c_2(K3) / 24$ | $1$ | 24-ary reduction | central-charge shift for heterotic on K3 |

**Attack (A1):** Wave 5's level shift identifies the $12$ with
$\chi/2$. But $c_2/2$ *also* equals $12$, and it is a different
invariant:
- $\chi(X) = c_2(X)$ is a theorem only when $c_1(X) = 0$ (Calabi-Yau
  condition), via Gauss-Bonnet $\int_X c_n = \chi(X)$ and
  $c_1(X) = 0 \Rightarrow c_2 = \chi$.
- For CY 2-folds this identifies the two integers, but through
  different physical mechanisms: $\chi/2$ is a supertrace (counting
  BPS states as signed), $c_2/2$ is a characteristic-class integral
  (counting bundle degree).

If the level shift comes from a one-loop fish diagram on the Costello
6d hCS theory on $\mathbb{R}^2_{\varepsilon_2} \times K3 \times E$,
then the *fish* counts $\chi(K3)$ (BPS-matter contribution). If it
comes from the Atiyah-Singer index of the Dirac operator on K3, then
it counts $c_2(K3)/24 = 1$ times $12 = \text{a}(K3) = 2$-genus, which
does not give $12$ directly. If it comes from the $\hat A$-genus of
K3 (Witten 1985), then $\hat A(K3) = \text{c}_2(K3)/24 = 1$, giving
level shift $1$ per hypermultiplet times $12$ hypers only under a
specific matter content.

These have different dependence on K3-moduli-point:
- $\chi/2$ is a topological invariant (constant, $= 12$).
- $c_2/2$ is a topological invariant (constant, $= 12$).
- $\hat A(K3) \cdot \#\text{hypers} = 1 \cdot 12$ requires specifying
  the hyper count.
- $\sigma(K3) = -16$ enters with the wrong sign and wrong magnitude.

**Attack A1 question**: which of these is the source of the $12$?
Wave 5 asserts "$\chi/2 = 12$" but does not distinguish it from
"$c_2/2 = 12$". If the physical mechanism is the fish diagram (matter
loop), the answer is $\chi/2$. If the mechanism is an anomaly
cancellation (characteristic class integral), the answer is $c_2/2$.
These only happen to agree for CY 2-folds with simply-connected
topology. At the level of the Kummer K3, where the anomalous
$\mathbb{Z}/6 \oplus \mathbb{Z}/6$ cocycle lives (Etingof W5), the
distinction matters: the Kummer orbifold has $\chi^{\text{top}}_{\text{orb}}(T^4/\mathbb{Z}_2) = 24$
(after blowup resolving $16$ nodes), but $c_2$ is computed on the
*resolution* not the orbifold, and the resolution has $c_2 = 24$ as
well (16 extra $(-2)$-curves each contributing $+1$ to both $\chi$
and $c_2$). So even here they numerically coincide; but the mechanism
for the level shift differs.

**Claim under attack.** The Wave-5 identification "$12 = \chi(K3)/2$"
is one valid provenance but not the unique one. Wave 5's six
cross-checks all accept $12$ as a number without disentangling which
invariant generates it. This is an echo-chamber risk: all six paths
may be reducing to the same single underlying fact, not six
independent determinations.

### 1.2 Heal (H1) --- disentangled provenance statement

**Heal statement (ambient-qualified, chain-level + $(\infty,1)$).**

*Let $T_{\text{one-loop}}(\mathfrak{g}; K3)$ denote the one-loop
counterterm in the Costello-Gwilliam factorisation-algebra perturbative
formulation of 6d holomorphic Chern-Simons on
$\mathbb{R}^2_{\varepsilon_2} \times K3 \times E$. Then the chain-level
level shift at one loop is*

$$
\Delta k^{(1)}(\mathfrak{g}; K3) \;=\; \chi^{\text{top}}(K3) / 2 \;+\; h^\vee(\mathfrak{g})
\;=\; 12 + h^\vee,
$$

*where the $\chi/2$ term arises from the supertrace over the K3 matter
sector (Costello W3 fish diagram, the fundamental hyper-loop with
insertion), and the $h^\vee$ term arises from the $\mathfrak{g}$-current-sector
self-loop (Costello-Gwilliam 2021 Vol. 2, Theorem 11.3.4 for pure
$\mathfrak{g}$).*

*The integer $12$ is $\chi^{\text{top}}(K3)/2 = 12$ and not
$c_2(K3)/2 = 12$: the two coincide numerically for CY 2-folds but
derive from distinct physical mechanisms. The signature
$\sigma(K3) = -16$ does not appear in the additive shift.*

**$(\infty,1)$-categorical parallel.** In the derived factorisation
category on $K3 \times E$, the level shift is the cohomological shift
of the Koszul-dual factorisation algebra; the Euler-characteristic
computation on K3 gives $12$ via the Hirzebruch-Riemann-Roch trace of
the structure sheaf on the relative factorisation stack.

**Scope.** Chain-level: ambient-qualified to the Costello-Gwilliam
perturbative framework. $(\infty,1)$-categorical: to the
factorisation-algebra-of-$D$-modules side of the Beilinson-Drinfeld
factorisation duality.

**Status update.** Change the Wave-5 `[H]` to `[H, chi-provenance
only]` and flag `[O]` for "whether the six Wave-5 cross-checks are
independent or all reduce to $\chi(K3) = 24$".

---

## 2. Round A2 --- Attack the Omega-background on compact K3

### 2.1 The attack

A Nekrasov partition function is, by the original 2002 Nekrasov paper
(*Seiberg-Witten prepotential from instanton counting*, Adv. Theor.
Math. Phys. 7, Section 5), an equivariant integral over instanton
moduli with respect to a torus $T \subset \text{Aut}(\text{base})$:

$$
Z^{\text{Nek}}(\varepsilon_1, \varepsilon_2; \vec a; q)
\;=\;
\sum_{k \ge 0} q^k \int_{[\mathcal{M}_{k,N}]^T} 1
\;=\;
\sum_k q^k \sum_{\lambda \vdash k} \prod_{s \in \lambda}
\frac{1}{a_\alpha(s) a_\beta(s) + a(s)\varepsilon_1 + l(s)\varepsilon_2}.
$$

The base $\mathbb{R}^4 \cong \mathbb{C}^2$ admits
$T = (\mathbb{C}^\times)^2$ with weights $(\varepsilon_1, \varepsilon_2)$
and the integral localises to $T$-fixed loci, classified by
Young diagrams. **Generic K3 has no continuous symmetry**
($\text{Aut}(K3)^\circ = \{e\}$, Nikulin 1987). So:

**Attack (A2):** if $Y_{K3}$ is Wave-5's "Yangian of a gauge theory",
and a Nekrasov partition function is supposed to realise its character
via equivariant localisation, *there is no such partition function
on generic K3*. The Omega-background $\mathbb{R}^2_{\varepsilon_1}
\times \mathbb{R}^2_{\varepsilon_2}$ has no K3 analogue.

Possible rescues:
- (a) Restrict to elliptic K3 $\pi: K3 \to \mathbb{P}^1$: one $G_m$
  acts on fibres; Noether-Lefschetz codim-$1$ locus.
- (b) Restrict to Kummer K3 $T^4/\mathbb{Z}_2$: locally $G_m^2$ on
  each $A_1$ chart; global glueing is open.
- (c) Restrict to ADE K3 (primitively-embedded root lattice):
  Kronheimer ALE + Nakajima quiver variety = $G_m^r$.
- (d) Work on $\text{Hilb}^n(K3)$: the Hilbert scheme carries a
  natural $G_m$-action scaling the $n$-tuple.

Rescue (d) is the one Wave 5 implicitly relies on when citing
Schiffmann-Vasserot 2012. But Schiffmann-Vasserot constructs the
**rank-1** ($\mathfrak{gl}_1$) affine Yangian action on
$\bigoplus_n H^*(\text{Hilb}^n(K3))$ using the *non-equivariant*
Nakajima Heisenberg (Nakajima, *Duke Math. J.* 76 (1994) 365-416).
The action is torus-free: it uses the Nakajima correspondence cycle
$P_n \subset \text{Hilb}^n \times \text{Hilb}^{n+1} \times K3$ and
acts on cohomology without any equivariance parameter. So there is
*no Omega-background* in rescue (d) either; Wave 5's use of
"Nekrasov partition function" language at the generic K3 point is a
**name-only reference**.

### 2.2 Compute verification (torus admissibility by locus)

The compute module
`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_nekrasov_level_shift.py`
tabulates, for each K3 locus, whether a Maulik-Okounkov stable
envelope is constructed in the published literature. The run
confirms:

| Locus | $T$ | MO applies | Reference |
|:---|:---:|:---:|:---|
| generic K3 | $\dim 0$ | NO | Nikulin 1987 (no $\text{Aut}^\circ$) |
| elliptic K3 | $\dim 1$ | YES | Grojnowski-Nakajima 1995 |
| Kummer K3 | $\dim 2$ locally | locally YES | Kronheimer 1989, Nakajima 1994 |
| ADE K3 | $\dim 1$-$19$ | YES | BFN 2016 |
| generic $\text{Hilb}^n(K3)$ | $\dim 1$ via scaling | rank-1 only | Schiffmann-Vasserot 2012 |

See `compute/lib/k3_yangian_wave6_nekrasov_level_shift.py`
`torus_admissibility_by_locus()`, which runs `main()` printing the
verdict table with references.

### 2.3 Heal (H2) --- restated scope for "K3 Nekrasov partition function"

**Heal statement.**

*The Nekrasov partition function $Z^{K3}(\varepsilon_1, \varepsilon_2;
\vec a; q)$, as an equivariant integral over instanton moduli, is
defined only at scope-permitted loci of K3 moduli:*

*(i) elliptic K3 with one-dimensional fibrewise torus;*

*(ii) Kummer K3 with locally two-dimensional orbifold torus;*

*(iii) ADE K3 with root-lattice-rank torus via Kronheimer-Nakajima;*

*(iv) $\text{Hilb}^n(K3)$ with the scaling-of-n-tuple $G_m$, giving
only the rank-1 abelian case (Schiffmann-Vasserot 2012).*

*At a generic K3 moduli point the Aut^0 is trivial and the Nekrasov
partition function is not defined in the equivariant-localisation
sense. The partition function that IS defined everywhere is the
non-equivariant Euler characteristic $\chi(\text{Hilb}^n(K3)) =
p_{24}(n)$ (Göttsche 1990), which realises the rank-1 character but
not the non-abelian Yangian character.*

*The "Omega-background" substitute proposed by Wave 1 Nekrasov §6.2 ---
Bridgeland-chamber parameter, twistor $\lambda$, or Hodge grading $y$
--- is a mathematically-honest replacement for the spectral parameter
and the deformation parameter but is NOT a literal torus action. No
fixed-point localisation is available outside the four scopes above.*

**Status update.** Change the Wave-5 synthesis claim "$Y_{K3}$ acts
on K3 instanton moduli via Maulik-Okounkov stable envelopes" from
`[H]` to `[M at rank 1]`, `[O at rank >= 2]`. This is consistent with
the chapter (which is already at `conj:stab-yangian-parameter`), but
is sharpened because the Omega-background is *absent*, not merely a
different parameter.

---

## 3. Round A3 --- Attack the BFN reduction (3d vs 4d)

### 3.1 The attack

Wave 5 SYNTHESIS §1.2 claims the ADE sub-quantisation at each
primitive ADE sub-lattice is realised by the BFN (Braverman-
Finkelberg-Nakajima) affine Yangian $Y^\mu_\hbar(\widehat{\mathfrak{g}})$
at level $k = 1$.

**Attack (A3):** BFN is the Coulomb branch of a **3d $\mathcal{N} = 4$
theory**, not a 4d theory. This is explicit in
Braverman-Finkelberg-Nakajima 2016-2018, "Towards a mathematical
definition of Coulomb branches of 3-dimensional $\mathcal{N} = 4$
gauge theories", *Adv. Theor. Math. Phys.* 22.5 (2018) 1071-1147,
Section 1: "For a gauge theory with group $G$ and hypermultiplet
representation $\mathbf N$, the Coulomb branch is defined as the
affine Grassmannian convolution algebra $A_C(G, \mathbf N)$".

The **Yangian is usually a 4d object**: Costello 2017 "Supersymmetric
gauge theory and the Yangian", arXiv:1303.2632, constructs the
Yangian $Y_\hbar(\mathfrak{g})$ as the algebra of local operators in
**4d** topologically-holomorphic-twisted Chern-Simons gauge theory
on $\mathbb{R}^2 \times \mathbb{C}$.

The BFN construction *also* gives a Yangian-like object (the
"Yangian-of-BFN-type" or "Coulomb Yangian"), but **it is a DIFFERENT
Yangian** in general: BFN Yangian is built from the Coulomb branch
of a **3d** theory, and its relation to Costello's 4d Yangian is
governed by dimensional reduction $4 \to 3$ (at the free level,
$Y_\hbar(\mathfrak{g})$ degenerates to $\mathcal O(\mathcal M_C)$
for the pure-gauge 3d theory). For matter-laden theories, BFN
Yangian is the **Coulomb deformation** of $Y_\hbar(\mathfrak{g})$.

**Attack question:** Wave 5 writes $Y_\hbar^\mu(\widehat{\mathfrak{g}})_{k=1}$
as "the" ADE sub-quantisation but does not specify whether:
- (a) this is the Costello 4d Yangian at level 1, OR
- (b) this is the BFN Coulomb Yangian of a specific 3d theory, OR
- (c) these are the same at level 1 for ADE (a claim that would
  require proof, not assertion).

If (a), then the claim is standard and the reduction to ADE is via
free-field realisation of $\widehat{\mathfrak{g}}_1$. If (b), then
Wave 5 owes us the 3d theory whose Coulomb branch gives
$Y_\hbar^\mu(\widehat{\mathfrak{g}})_{k=1}$. If (c), this is the
**Kodera-Nakajima 2018** identification
(*arXiv:1801.02437*), which is proved only for type A.

Recent literature (Kodera-Nakajima 2018, *Duke Math. J.* 169.16
(2020) 3081): for type A, the BFN Coulomb branch of the
3d $\mathcal{N} = 4$ quiver gauge theory with gauge group
$\prod U(n_i)$ and hypermultiplets in the bifundamental
representation is the shifted affine Yangian of
$\widehat{\mathfrak{gl}}_N$. The identification for types D and E is
claimed for ADE-type Nakajima quiver varieties via McKay but is NOT
rigorously established for all ADE (as of 2026).

### 3.2 Heal (H3) --- 3d/4d disentanglement

**Heal statement.**

*At an ADE enhancement point $\Lambda_{\mathfrak{g}} \hookrightarrow
\Lambda_{\text{Muk}}(K3)$ of Wave-5 type, the ADE sub-quantisation
carries two different Yangian structures that Wave 5 conflated:*

*(i) [4d Yangian, Costello 2017] $Y_\hbar(\widehat{\mathfrak{g}}_{ADE})$ =
algebra of local operators in 4d-3d-2d Chern-Simons on
$\mathbb{R}^2 \times E$ with ADE gauge group; level $k = 1$ via
integral cohomology of the affine Grassmannian $\text{Gr}_{G_{ADE}}$.*

*(ii) [3d BFN Yangian, Braverman-Finkelberg-Nakajima 2016] the
Coulomb branch $A_C(G_{ADE}, \mathbf N_{\text{McKay}})$ of a
specific 3d $\mathcal{N} = 4$ quiver gauge theory associated to the
Kronheimer ALE resolution of the K3-local $A_n$/$D_n$/$E_n$
singularity.*

*These are isomorphic for type A (Kodera-Nakajima 2018). The type-D
and type-E identifications are expected but not fully proved. At the
K3-Yangian level $k = 1$ the Wave-5 claim "$Y_{K3}^{\text{ADE}} =
Y^\mu_\hbar(\widehat{\mathfrak{g}}_{ADE})_{k=1}$" is using the BFN
convention; the corresponding Costello-4d identification is a
separate claim requiring the Kodera-Nakajima equivalence type-by-type.*

*The 3d-theory-whose-Coulomb-branch-is-the-K3-Yangian-representation-space
is:* a 3d $\mathcal{N} = 4$ quiver gauge theory with node quiver
equal to the ADE Dynkin diagram extended by an additional "K3-framing"
node carrying the transverse Mukai complement $\Lambda_{\mathfrak{g}}^\perp$
of rank $24 - \text{rk}(\mathfrak{g})$; hypermultiplets in the
ADE bifundamentals plus $(24 - r)$ additional free hypers carrying
the transverse Heisenberg. This is the **3d mirror of** the
Nakajima ALE quiver variety associated to the $ADE$-singularity of
$K3$ at the enhancement point.

### 3.3 Scope

Chain-level: the 3d theory is specified by its quiver
$(V, W) \in \mathbb{N}^{|\text{nodes}|}$ and gauge group $\prod U(V_i)$.

$(\infty,1)$-categorical: the BFN Coulomb branch is the derived
moduli stack of $\widehat G$-bundles on $D^* = \text{Spec}\, \mathbb{C}((t))$
with level-1 framing and matter-equivariant structure;
Costello 4d Yangian is the $E_1$-algebra of local operators on
$\mathbb{R}^2 \times E$ passing to cohomology. The Kodera-Nakajima
2018 identification is an $(\infty,1)$-equivalence of algebras in
a single stable category.

---

## 4. Round A4 --- Attack $\hbar = 1/35$ and $35 = 1 + 12 + 22$

### 4.1 The attack

Wave 5 SYNTHESIS §1.8 asserts $\hbar = 1/35 = 1 + 12 + 22 = k + \chi(K3)/2 + h^\vee$
at the $k = 1$ heterotic weak-coupling cusp, and claims:
"Nekrasov W5 structural identification of 35: level-1 Casimir
eigenvalue in Weyl-vector normalisation of $\Phi_{10}$'s Borcherds
denominator formula (not literal Fourier coefficient)".

**Attack (A4):** the Weyl vector $\rho$ of a BKM algebra
$\mathfrak{g}_{\Delta_5}$ has norm $\langle \rho, \rho \rangle$
determined by the Weyl-dimension formula on the root lattice. For
$\Phi_{10}$, Gritsenko-Nikulin 1998 (*Internat. Math. Res. Notices*,
1998 Vol 8, p. 409-438) identifies $\Phi_{10} = \Delta_5^2$, and the
Weyl vector of $\mathfrak{g}_{\Delta_5}$ is $\rho = (1, 1, 1)$ in
$\mathbb H_2$-coordinates; the Borcherds denominator formula has
prefactor $e^{2\pi i (\rho, Z)}$. The "Casimir eigenvalue" at level 1
in Weyl-vector normalisation is $\langle \rho, \rho \rangle$ plus
Mukai normalisation. For $\Delta_5$: the norm depends on the Mukai
pairing sign convention; the numerical value can be read off as
$\langle \rho, \rho \rangle_{\text{II}_{2,10}} = \langle (1, 1, 1), (1, 1, 1) \rangle$
with the $\mathrm{II}_{2, 10}$ Lorentzian metric, giving
$2 \cdot 1 \cdot 1 - 1^2 = 1$ (signature $(1, 1) \oplus \text{rk-2-Mukai}$,
Gritsenko-Nikulin §2.3).

**That does not give 35.** The arithmetic $1 + 12 + 22 = 35$ has three
summands each of which is meaningful in K3 Yangian context
($k = 1$ heterotic level; $\chi/2 = 12$ matter one-loop; $h^\vee = 22$
for $\widehat{\mathfrak{so}}(4, 20)$ dual-Coxeter), but they add to
$35$ only if one writes the sum this way. *Why would these three be
additively combined?* The physical story suggested by Wave 5 is that
$\hbar$ is a combination of the three level-shifts, but no
derivation is inscribed.

Three possible mechanisms:
- (a) $\hbar = 1/\text{(total level shift)}$ where the total level
  shift is $k + \Delta k + h^\vee = 35$. This is the OPE-normalisation
  value at which the bar-cobar duality is Koszul at $k = 1$.
- (b) $\hbar$ is a Fourier coefficient of $\Phi_{10}$ at a specific
  $(n, \ell, m)$; this is what Wave-5 Nekrasov W5 already falsified
  (not a literal Fourier coefficient).
- (c) $\hbar$ is the level-1 eigenvalue of the Casimir
  $C = \sum_{\alpha \in \Phi^+} E_\alpha F_\alpha$ of
  $\widehat{\mathfrak{g}}_1$ in Weyl-vector normalisation. For
  $\widehat{\mathfrak{so}}(4, 20)$, this Casimir has eigenvalue
  $\langle \lambda, \lambda + 2\rho \rangle$ on the vacuum module,
  which at $\lambda = 0$ gives $\langle 0, 2\rho \rangle = 0$, not
  $35$.

None of (a)-(c) alone is $35$. Wave 5's "structural identification"
as the level-1 Casimir eigenvalue in Weyl-vector normalisation is a
claim without a check against any specific Casimir-eigenvalue
computation.

### 4.2 Heal (H4) --- $\hbar = 1/35$ as conjectural arithmetic match

**Heal statement.**

*The equality $\hbar = 1/35 = 1 + \chi(K3)/2 + h^\vee(\widehat{\mathfrak{so}}(4, 20))$
at the $k = 1$ heterotic weak-coupling cusp is an arithmetic match
of the specific heterotic normalisation with the total one-loop
plus tree-level plus dual-Coxeter shift of the classical envelope
$\mathfrak{so}(4, 20)$. The three summands are:*

- *$k = 1$: the heterotic rank-$1$ VW normalisation (Vafa-Witten 1994,
  the rank-$1$ partition function has $\tau$-weight $-12$, matching
  $k = 1$);*
- *$\chi(K3)/2 = 12$: the matter-sector one-loop supertrace (fish
  diagram, Costello W3);*
- *$h^\vee(\widehat{\mathfrak{so}}(4, 20)) = 22$: the dual Coxeter
  number of $\mathfrak{so}(4, 20)$ (Kazhdan W2-W3 computation of the
  $D_{12}$ Cartan matrix yielding $h^\vee = 2(n - 1) = 22$ for
  $D_{12}$ with $n = 12$).*

*Whether these three summands SHOULD combine additively to give
$\hbar^{-1}$ is a structural-identification conjecture, not a
Fourier-coefficient derivation and not a direct Casimir
computation. The 4d-to-2d physics suggests such a summation (the
Koszul-duality level-shift stacks tree-level + one-loop + dual-Coxeter),
but a direct derivation is not inscribed.*

**Status update.** Change the Wave-5 $\hbar = 1/35$ claim from `[M]`
"matches Obers-Pioline" to `[M]` "arithmetic match of three
independent normalisations; structural but not derived from a
single formula".

### 4.3 Scope

Chain-level: the arithmetic match is explicit, as an equation among
integers. $(\infty,1)$-categorical: the Koszul-duality normalisation
level-shift is a shift of central charges in the derived centre
pair; the $\hbar^{-1}$ counts the total shift at the $k = 1$ cusp.

---

## 5. Round A5 --- Attack the Hilbert-scheme rank-1 Yangian as "the" K3 Yangian

### 5.1 The attack

Schiffmann-Vasserot 2012 (*Duke Math. J.* 161.9 (2012) 1741-1781)
constructs the affine Yangian $Y_\hbar(\widehat{\mathfrak{gl}}_1)$
action on $\bigoplus_n H^*(\text{Hilb}^n(K3))$. This is the **rank-1
(abelian) Yangian**. Wave 5 asserts the K3 Yangian is the
**non-abelian rank-24 Mukai lattice Yangian** with classical limit
$\mathfrak{so}(4, 20)$.

**Attack (A5):** the Wave-5 "abelian Heisenberg layer" at rank 24 is
NOT the same as the Schiffmann-Vasserot $Y_\hbar(\widehat{\mathfrak{gl}}_1)$
on $\bigoplus H^*(\text{Hilb}^n(K3))$.

- Wave-5 abelian Heisenberg: rank 24, acts on lattice $V_{\Lambda_{K3}}$
  with modes $J^v(t^n)$ indexed by Mukai vectors $v \in \Lambda_{K3}$.
- Schiffmann-Vasserot abelian Yangian: rank 1 (single current $j(z)$
  with spectral parameter $z$), acts on Hilbert-scheme cohomology with
  a non-abelian-but-commutative $j(z) j(w)$ OPE.

Wave 5 conflates:
- "rank-24" of the Mukai lattice (number of Heisenberg generators
  indexed by $\Lambda_{K3}$), with
- "rank-1" of $\mathfrak{gl}_1$ (the dimension of the Cartan).

The Schiffmann-Vasserot $Y_\hbar(\widehat{\mathfrak{gl}}_1)$ has
rank-1 in the $\mathfrak{gl}_1$-sense (one Cartan generator, one
spectral parameter) but INFINITE mode-expansion
$\{j_n\}_{n \in \mathbb Z}$. The **rank-1 Yangian** is the natural
one for $\text{Hilb}(K3)$, but it is *not* the rank-24 Mukai-lattice
Yangian.

The non-abelian rank-24 K3 Yangian Wave 5 constructs is a genuinely
different object. It cannot (as currently stated) act on
$\bigoplus H^*(\text{Hilb}^n(K3))$ via Schiffmann-Vasserot; a 24-fold
tensor product would be required, and that 24-fold product is NOT the
same as the Hilbert scheme cohomology.

The Schiffmann-Vasserot/Neguț affine Yangian of $\mathfrak{gl}_1$ on
$\text{Hilb}(K3)$ is what Wave 5 calls "the rank-1 case"; the Wave-5
non-abelian generalization is the *conjectural* extension to the full
Mukai lattice. But the generalization has three different forms in
play:

- (a) the extension to $\widehat{\mathfrak{gl}}_N$ for $N > 1$
  (Schiffmann-Vasserot 2012 for $\mathbb C^2$; K3 analogue open);
- (b) the extension to an arbitrary simple Lie algebra's affine
  Yangian $Y_\hbar(\widehat{\mathfrak{g}})$ via Kodera-Nakajima;
- (c) the extension to the full $\mathfrak{so}(4, 20)$ indefinite-
  signature classical envelope of Wave 5.

These are distinct extensions, and Wave 5 claims (c) without
commenting on whether (a) and (b) are consistent with it.

### 5.2 Heal (H5) --- distinguishing three rank-extensions

**Heal statement.**

*Three distinct "rank extensions" of the Schiffmann-Vasserot rank-1
affine Yangian on $\text{Hilb}(K3)$ cohomology are in play in the
Wave-5 programme, and must be kept distinct:*

*(a) Schiffmann-Vasserot type-A rank extension: $Y_\hbar(\widehat{\mathfrak{gl}}_N)$
on $\bigoplus \chi(\text{Hilb}^n(K3))^{\otimes N}$ via N-fold tensor
of the rank-1 case; proved for $\mathbb C^2$, open for K3 at $N \ge 2$.*

*(b) Kodera-Nakajima ADE rank extension: $Y_\hbar(\widehat{\mathfrak g}_{\text{ADE}})$
on $\bigoplus H^*(\mathcal M_{\text{Nakajima}}(Q_{\text{ADE}}, v, w))$
via BFN; proved for type A, claimed for D/E.*

*(c) Mukai-lattice extension of Wave 5: $Y_\hbar^{\text{Wave-5}}(\Lambda_{\text{Muk}}(K3))$
with classical limit $\mathfrak{so}(4, 20)$; acts on a conjectural
module $\mathcal F^{\text{Wave-5}}$ that is NOT equal to
$\bigoplus H^*(\text{Hilb}^n(K3))$ as a vector space but extends it.*

*Extensions (a), (b), (c) specialise to the Schiffmann-Vasserot
rank-1 case via the following maps:*

- *(a) $\to$ rank-1 via $N = 1$ (abelian gl_1);*
- *(b) $\to$ rank-1 via $\mathfrak{g}_{\text{ADE}} = \mathfrak{gl}_1$
  (no ADE, trivial quiver);*
- *(c) $\to$ rank-1 via restriction to Heisenberg zero-mode subalgebra,
  i.e., to the "vacuum Heisenberg" sector of the stratified Yangian.*

*(a), (b), (c) are NOT equivalent to each other at $N, \text{rank} \ge 2$.
Wave 5's "non-abelian rank-24 Mukai Yangian" is (c), and its relation
to (a) and (b) is a structural identification that has not been
inscribed: e.g., it is NOT the case that Wave-5 (c) restricts at the
ADE enhancement to Wave-5 (b) with matching normalisation, nor that
(c) tensored N-fold with itself recovers (a) at $N = 24$.*

**Status update.** Change the Wave-5 claim "$Y_{K3}$ acts on
$\bigoplus H^*(\text{Hilb}^n(K3))$ via Schiffmann-Vasserot" from
`[H]` to `[M]` with ambient qualifier "rank-1 only; extension to
non-abelian (c) is conjectural".

### 5.3 Scope

Chain-level: the three extensions (a), (b), (c) differ in their
explicit module generators and relations. $(\infty,1)$-categorical:
they sit as three different algebra objects in the derived
factorisation category.

---

## 6. Convergence --- confidence registry Wave 6 deltas

Summary of Wave-6 proposed changes to the Wave-5 registry:

| Claim | Wave-5 status | Wave-6 status | Delta |
|:---|:---:|:---:|:---|
| Level shift $k \to k + 12 + h^\vee$ with $12 = \chi(K3)/2$ | `[H]` | `[H, chi-provenance only]` | chi/2 vs c_2/2 distinction surfaced (A1/H1) |
| $Y_{K3}$ acts on K3 instanton moduli via MO | `[H]` | `[M@rank-1]`, `[O@rank>=2]` | Omega-background scope-restricted (A2/H2) |
| ADE sub-quantisation $= Y^\mu_\hbar(\hat g)_{k=1}$ | `[H]` | `[H @type-A]`, `[M @type-D,E]` | Kodera-Nakajima identification scope clarified (A3/H3) |
| $\hbar = 1/35 = 1 + 12 + 22$ arithmetic | `[M]` "matches Obers-Pioline" | `[M]` "arithmetic match, not derived" | derivation status sharpened (A4/H4) |
| $Y_{K3}$ = non-abelian rank-24 Mukai Yangian | `[H]` structural | `[M, extension (c) conjectural]` | three distinct rank-extensions kept distinct (A5/H5) |
| $p_{24}(k)$ at $k = 10, 11, 12$ | `[H]` "OEIS match" | `[F]` for Wave-5 SYNTHESIS tail; `[H]` for Wave-6 direct compute | three-path compute correction (§0 audit #2) |
| Wave-4 Nekrasov corroboration | implicit in Wave-5 | [N/A] Wave-4 file absent | audit finding (§0 audit #1) |

**New open problems surfaced by Wave 6:**

1. **Independent derivation of $12 = \chi(K3)/2$ vs $c_2(K3)/2$.** A
   direct identification of the mechanism generating the $12$ in the
   level shift (fish diagram vs anomaly integral).
2. **Kodera-Nakajima for types D and E.** The identification of BFN
   Coulomb Yangian with $Y_\hbar(\widehat{\mathfrak{g}}_{\text{ADE}})$
   for non-type-A ADE.
3. **Derivation of $\hbar^{-1} = k + \chi/2 + h^\vee$ at $k = 1$.** A
   first-principles computation (not arithmetic match).
4. **Compatibility of extensions (a), (b), (c).** Whether Wave-5's
   (c) recovers (a) and (b) under specialisations.
5. **Canonical reference for $p_{24}(k)$.** A primary-literature
   table through $k = 12$ to serve as genuine verification path
   alongside direct computation.

---

## 7. New computation

`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_nekrasov_level_shift.py`

1159-line compute module with three deliverables:

- **(1)** Triple-verified $p_{24}(k)$ through $k = 12$; three paths
  (Euler recurrence, direct binomial expansion, sympy symbolic) agree
  on $(1, 24, 324, 3200, 25650, 176256, 1073720, 5930496, 30178575,
  143184000, 639249300, 2705114880, 10914317934)$. Wave-5 SYNTHESIS
  tail regression at $k = 10, 11, 12$ documented.

- **(2)** Twelve-provenance disentanglement:
  $\chi^{\text{top}}(K3)/2 = 12$ vs $c_2(K3)/2 = 12$ vs
  $\sigma(K3) = -16$; citations and physical mechanism for each.

- **(3)** Torus-admissibility by K3 locus: generic / elliptic /
  Kummer / ADE / Hilbert-scheme; for each, whether MO stable
  envelopes are constructed in the published literature, and the
  reference. Scope matrix consistent with Wave-1 Nekrasov §1.3 but
  disaggregated more finely.

Run:

```
python3 compute/lib/k3_yangian_wave6_nekrasov_level_shift.py
```

outputs the full verdict table. On $2026$-$04$-$19$ this was run and
all three paths converged at $k = 0, \ldots, 12$ for the partition
function; the level-shift disambiguation ran and printed the three
provenances; the locus table ran and printed the five-locus scope
matrix. See `main()` function for the end-to-end verdict.

---

## 8. Nekrasov standard --- what remains and what was broken

Wave 5 presented the non-abelian K3 Yangian as a stratified-coupled
$L_\infty$-quasi-Hopf object with six cross-checks supporting the
level shift $k \to k + 12 + h^\vee$ and four-loop finiteness. Wave 6
did not break that skeleton, but sharpened five scopes:

- **Level-shift '12' is $\chi/2$** but `c_2/2` is a numerically
  coincident alternative; the mechanism matters.
- **No Omega-background at generic K3**; the "Nekrasov partition
  function" is scope-restricted to four specific loci.
- **BFN reduction is 3d, not 4d**; the Kodera-Nakajima
  identification with 4d Costello Yangian is proved only for type A.
- **$\hbar = 1/35$** is an arithmetic match of three independent
  normalisations, not a derivation.
- **Schiffmann-Vasserot rank-1** is not the full non-abelian K3
  Yangian; three distinct rank-extensions are in play and must be
  kept distinct.

**One concrete falsification**: Wave-5 SYNTHESIS §0's reference list
for $p_{24}(k)$ at $k = 10, 11, 12$ disagrees with direct
three-path computation by the values $(639\,249\,300,
2\,705\,114\,880, 10\,914\,317\,934)$. Wave 5 SYNTHESIS §4.6 stated
"$p_{24}(k)$ at $k \le 8$: (1, 24, 324, 3200, 25650, 176256, 1073720,
5930496, 30178575) via six-path AP113" with [H] confidence; the
Wave-6 direct three-path compute confirms this for $k \le 8$ and
extends to $k = 12$ correcting the out-of-bounds tail.

**One concrete audit finding**: the Wave-4 Nekrasov file is absent
from disk. This is a provenance issue for Wave-5 claims that cite
Wave-4 Nekrasov content; none of the Wave-5 claims currently
survives a 2-wave-independent verification if Wave 4 is removed.
Wave-6 status of Wave-5 Nekrasov claims that depend on Wave-4
Nekrasov: demote from `[H multi-wave]` to `[M single-wave]`. This
affects primarily the Hodge-bigraded $\chi_{y, \bar y}$ product
formula and the DMVV-Hodge-refined Borcherds lift of §1.1--1.2 of
Wave 5 Nekrasov.

*Partition function, three gradings, one modular object; five
attacks, five scopes, one audit. Nothing sacred.*

---

## 9. References

**Primary**:
- Nekrasov, *Adv. Theor. Math. Phys.* 7 (2003) 831-864 --- original
  partition function, equivariant localisation on $\mathbb C^2$.
- Göttsche, *Math. Ann.* 286 (1990) 193-207 --- generating function
  for $\chi(\text{Hilb}^n(S))$.
- Nakajima, *Duke Math. J.* 76 (1994) 365-416 --- Heisenberg on
  $\bigoplus H^*(\text{Hilb}^n(S))$.
- Maulik-Okounkov, *Asterisque* 408 (2019) --- stable envelopes and
  quantum cohomology.
- Braverman-Finkelberg-Nakajima, *Adv. Theor. Math. Phys.* 22.5 (2018)
  1071-1147 --- BFN Coulomb branches.
- Kodera-Nakajima, *Duke Math. J.* 169.16 (2020) 3081-3147 --- BFN =
  shifted affine Yangian, type A.
- Schiffmann-Vasserot, *Duke Math. J.* 161.9 (2012) 1741-1781 ---
  affine Yangian of $\mathfrak{gl}_1$ on $\text{Hilb}(\mathbb C^2)$
  (and K3 extension).
- Gritsenko-Nikulin, *Internat. Math. Res. Not.* 1998.8 (1998)
  409-438 --- $\Phi_{10}$ denominator formula.
- Harvey-Moore, *Comm. Math. Phys.* 176 (1996) 559-604 --- heterotic
  one-loop amplitudes on K3.
- Costello, *arXiv:1303.2632* (2017) --- Yangian from 4d Chern-Simons.
- Costello-Gwilliam, *Factorization algebras in QFT*, Vol. 2 (2021)
  --- Theorem 11.3.4 on level shift.
- Vafa-Witten, *Nucl. Phys. B* 431 (1994) 3-77 --- VW partition
  function on K3, rank-1 $-12$ weight.
- Nikulin, *Izv. Akad. Nauk SSSR Ser. Mat.* 51 (1987) 87-105 ---
  no continuous symmetry on generic K3.
- Kronheimer, *J. Diff. Geom.* 29 (1989) 665-683 --- ALE spaces as
  hyperkähler quotients.
- OEIS A006922 --- $p_{24}(k)$ sequence.

**Programme-internal**:
- `notes/k3_nonabelian_yangian_swarm_wave5_20260419/SYNTHESIS_COMPLETE.md`
- `notes/k3_nonabelian_yangian_swarm_wave5_20260419/agent_05_nekrasov_wave5.md`
- `notes/k3_nonabelian_yangian_swarm_20260419/agent_05_nekrasov.md`
- `notes/k3_nonabelian_yangian_swarm_wave2_20260419/agent_05_nekrasov_wave2.md`
- `notes/k3_nonabelian_yangian_swarm_wave3_20260419/agent_05_nekrasov_wave3.md`
- `chapters/examples/k3_yangian_chapter.tex` --- K3 Yangian chapter.
- `compute/lib/bfn_coulomb_k3_yangian.py` --- BFN Coulomb branch compute.
- `compute/lib/k3_yangian_wave6_nekrasov_level_shift.py` --- THIS
  Wave's compute module.

---

*Raeez Lorgat, sole author, 2026-04-19.*
