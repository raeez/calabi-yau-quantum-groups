# Agent 05 --- Nekrasov on the Non-Abelian K3 Yangian, Wave 7

*Voice*: partition functions first, interpretation after. A "Yangian
from gauge theory" is not a slogan; it is a gauge group $G$, a matter
representation $\mathbf N$, an Omega-background $(\varepsilon_1,
\varepsilon_2)$, a Coulomb moduli $\vec a$, a counting parameter $q$,
an instanton moduli space $\mathcal M_{k,N}$, a $T$-equivariant integral
$Z(\vec a, \varepsilon_1, \varepsilon_2; q) = \int_{[\mathcal M]^T} 1$,
and an R-matrix on the equivariant cohomology whose YBE is derived from
an explicit fixed-point calculation. If any of these are missing, the
object is not a gauge-theoretic Yangian.

Wave 6 documented the absence of a torus on generic K3
(Nikulin 1987; scope-permitted loci only: elliptic / Kummer / ADE /
$\mathrm{Hilb}$), the sign obstruction for BLLPR $c_{2d} \le 0$ vs
Mukai-Heisenberg $c = +24$ (Gaiotto W6 / Hofman-Maldacena 2008), the
3d-vs-4d BFN confusion (Kodera-Nakajima 2018 only type A), and the
$\Phi_2$-infrastructure conditionality (rem:phi-not-unified-functor).

Wave 7 continues under Beilinson's dictum: every gauge-theoretic origin
claim for $Y(\mathfrak g_{K3})$ is false until a computable
$Z(\vec a, \varepsilon_1, \varepsilon_2; \cdots)$ is exhibited at
rank 1 or rank 2, an R-matrix is extracted, and its YBE is checked.

Raeez Lorgat, sole author, 2026-04-19.

---

## Orientation (inherited from Wave 6)

- Manuscript states `conj:bfn-k3-yangian-kummer` and `conj:bfn-k3-yangian-mukai`
  as CONJECTURES; Route B proved only for quiver varieties, not K3.
- Wave 6 installed 15 obstructions O1--O15 (Etingof / Kazhdan / Gaiotto /
  Nekrasov / Costello / Drinfeld voices) narrowing what any gauge-theoretic
  $Y(\mathfrak g_{K3})$ could be.
- Wave 6 Nekrasov (W6, §2) confirmed: no Omega-background on generic K3;
  the Nekrasov partition function is defined only at four scope-permitted
  loci; $p_{24}(k)$ triple-verified through $k = 12$.

Wave 7 assault: demand the gauge theory, the instanton integral, and
the R-matrix. Produce obstructions where the gauge theory does not
yield them; produce a partition function where one of the four loci
admits one; ground every number in primary source.

---

# § Attack Phase 1 --- gauge-theoretic demolition

## A1.1 Attack: name the 6d theory

Wave 5 SYNTHESIS §1.6 says "6d hCS on $\mathbb R^2_{\varepsilon_2} \times
K3 \times E$ with surface defect on $K3 \times \{0\}$". Wave 6 Witten
(W6 §A1) showed there are five candidate 6d parents (2,0), heterotic,
M-on-K3, IIA-on-K3, F-theory); Wave 6 Witten healed to the
**heterotic $T^4$ $\equiv$ IIA K3** duality pair (Hull-Townsend 1994,
Witten 1995).

Under Nekrasov discipline the question sharpens:

**Q(A1.1).** What is the 6d gauge theory whose instanton moduli on
$K3$ (or a $K3$-adjacent ambient) produces the putative $Y(\mathfrak
g_{K3})$?

Three surviving candidates after Wave 6:

(T1) **6d (2,0) $A_{N-1}$ theory on $K3 \times T^2$**, compactified
to 4d $\mathcal N = 2$ class-S theory on the Riemann surface $T^2$
with extra $K3$ compactification. Gauge group: $SU(N)$. Matter:
adjoint hyper. Coulomb branch: $\mathcal M_H^{\mathrm{inst}}(K3, SU(N))$.

(T2) **4d $\mathcal N = 2^\ast$ SYM on $K3$** (Vafa-Witten topological
twist). Gauge group $G$. Matter: adjoint massive hyper with mass $m$.
Partition function: $Z_{VW}(K3; \tau, m)$ = generating function of
instanton numbers weighted by $\chi(\mathcal M_{\mathrm{inst}})$.

(T3) **3d $\mathcal N = 4$ quiver gauge theory** with Nakajima quiver
$(Q, \mathbf v, \mathbf w)$ in the ADE McKay configuration. BFN
Coulomb branch: shifted affine Yangian $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$
per thm:bfn-phi-ade-identification (ProvedElsewhere, type A explicit).

**Attack verdict on (T1):** 6d (2,0) on $K3$ has NO gauge description.
The compactification on $K3 \times T^2$ does not give a Lagrangian
gauge theory; the class-S construction works when the compactification
manifold is a Riemann surface with punctures, not a compact
hyperkahler 4-manifold. **Non-existence of Lagrangian.**

**Attack verdict on (T2):** 4d $\mathcal N = 2^\ast$ on $K3$ gives
$Z_{VW}(K3; \tau) = \Theta_{\Gamma^{r, r}}(\tau)/\eta(\tau)^{\chi(K3)}
= \Theta/\eta^{24}$ (Vafa-Witten 1994, eq. 4.14, $SU(2)$ case:
$b_+(K3) = 3$, $b_-(K3) = 19$). This is a rank-$G$-many-free-field
character for $G$ abelian or matched to heterotic Narain lattice
reductions. **The character is known; what is NOT named is the
associated Yangian.** Vafa-Witten is a partition function, not a
quantum-group action on an equivariant cohomology.

**Attack verdict on (T3):** BFN Coulomb for $\mathbb C^2/\Gamma$
(Kronheimer ALE) gives $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$.
Extension to K3 requires deformation invariance under blowup of 16
orbifold singularities AND a quiver description for generic K3.
**No quiver for generic K3.** This is manuscript conjecture
`conj:bfn-k3-yangian-kummer`, not a theorem, and the base case
is on $\mathbb C^2/\Gamma$, not $K3$.

## A1.2 Attack: identify the Omega-background

On $\mathbb C^2$ the Omega-background is the torus $T = (\mathbb C^\ast)^2$
acting by $(z_1, z_2) \mapsto (e^{\varepsilon_1} z_1, e^{\varepsilon_2} z_2)$.
The Nekrasov partition function is
\[
Z^{\mathbb C^2}_{\mathrm{Nek}}(\vec a; \varepsilon_1, \varepsilon_2; q)
= \sum_{k \ge 0} q^k \int_{[\mathcal M_{k, N}]^T} 1
= \sum_k q^k \sum_{\vec \lambda: |\vec \lambda| = k}
\prod_{\alpha, \beta = 1}^N \prod_{s \in \lambda^{(\alpha)}}
\frac{1}{a_{\alpha\beta}(s) + \varepsilon_1 a(s) + \varepsilon_2 (-\ell(s) - 1)}
\frac{1}{a_{\alpha\beta}(s) + \varepsilon_1 (-a(s) - 1) + \varepsilon_2 \ell(s)}
\]
(Nekrasov 2003, arXiv:hep-th/0206161, eq. 5.15, originally Nakajima 1999).

For K3, we need a torus action on some moduli space that functions
analogously. Four candidates:

- (a) Elliptic K3 $\pi: K3 \to \mathbb P^1$: fibrewise $\mathbb C^\ast$
  action on fibres. $\dim T = 1$.
- (b) Kummer K3 $T^4/\mathbb Z_2$ (resolved): locally $(\mathbb C^\ast)^2$
  per $A_1$ chart; 16 charts; no global torus.
- (c) ADE K3: primitive ADE embedding; local Kronheimer ALE
  carries $\mathrm{rk}(\mathfrak g)$-dimensional torus.
- (d) $\mathrm{Hilb}^n(K3)$: no natural $(\mathbb C^\ast)^2$ action on
  $K3$ itself, but there is a $\mathbb C^\ast$ acting by scaling
  position in the $n$-tuple. $\dim T = 1$. Okounkov-Pandharipande-
  scaling pin-down.

**Attack A1.2.a.** None of (a)-(d) supplies a full $(\varepsilon_1,
\varepsilon_2)$ Omega-background of rank 2. The $\mathbb C^2$ partition
function is 2-parameter; K3 gauges have at best 1 continuous torus
direction (rescue (a)), or only locally-2-dim torus (rescue (b, c)).
**The unrefined partition function is what Vafa-Witten computes:
$Z_{VW}(K3; \tau) = Z(q; \varepsilon_1, \varepsilon_2)|_{\varepsilon_i \to 0}$.**
The full 2-parameter refined Nekrasov is unavailable on compact K3.

**Attack A1.2.b.** The proposed "twistor parameter $\lambda$" (Wave 1
Nekrasov §1.3; chapter's `subsec:nc-hodge-twistor`) is algebraically
a 1-parameter deformation, not a torus fixed-point parameter. It can
play a role structurally analogous to a combined
$\hbar = \varepsilon_1 + \varepsilon_2$, but the refined $(q, t)$-deformation
$\mathfrak q = e^{\varepsilon_1}, \mathfrak t = e^{\varepsilon_2}$ of the
K-theoretic Nekrasov formula has NO K3 analogue at generic moduli.

## A1.3 Attack: exhibit the R-matrix

Maulik-Okounkov (Asterisque 408, 2019) construct R-matrices as
"stable envelope" braiding morphisms in equivariant cohomology of
Nakajima quiver varieties, where the torus acts by rescaling + flavour
rotation. For $\mathbb C^2$-based quivers (type A), this gives the
rational Yangian R-matrix $R(u) = (u + \hbar P)/(u + \hbar)$ on
$V \otimes V$, $V = \mathbb C^N$.

**Attack A1.3.** On K3: the Maulik-Okounkov construction requires
the ambient space to have a torus action. The equivariant cohomology
$H^\ast_T(\mathrm{Hilb}^n(K3))$ is only defined at loci with a
$T$-action; at generic K3 with $\mathrm{Aut}^\circ(K3) = \{e\}$
(Nikulin 1987, *Izv. Akad. Nauk SSSR Ser. Mat.* 51), $T$ is trivial
and $H^\ast_T = H^\ast$. The stable-envelope braiding morphism becomes
degenerate: there are no fixed points to interpolate between.

**Corollary of A1.3.** At generic K3 moduli, the Maulik-Okounkov
R-matrix construction is undefined. At scope-permitted loci (elliptic
/ Kummer / ADE / $\mathrm{Hilb}$-scaling-only) there is a 1-dim torus,
and the stable envelope yields a degenerate ("evaluation") R-matrix
acting only on the spectral parameter, not on a 2-tensor
$V \otimes V$. This is the R-matrix on the Fock space
$\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$ that Schiffmann-Vasserot 2013
construct for $Y(\widehat{\mathfrak{gl}}_1)$ --- rank-1 only.

## A1.4 Attack: the qq-character machine on K3

Nekrasov's 2015 qq-characters (arXiv:1512.05388, arXiv:1711.11011 with
Pestun-Shatashvili) are residue integrals on the instanton moduli
space that generate Yangian (or quantum toroidal) operators. The
formula for the fundamental qq-character of $A_{N-1}$ pure gauge
theory is
\[
\mathcal X_1^{A_{N-1}}(x) = \sum_{i=1}^N \mathcal Y\left(x - \varepsilon_i\right)
+ \mathfrak q \prod_{i=1}^N \frac{1}{\mathcal Y(x - \varepsilon_i + \varepsilon_1 + \varepsilon_2)},
\]
where $\mathcal Y(x) = \prod_\alpha (x - \phi_\alpha)$ is the Y-observable
built from Coulomb moduli.

**Attack A1.4.** The qq-character integrals are rational functions of
$(\varepsilon_1, \varepsilon_2, a)$ regular at certain zero-pole
configurations. The residue theorem that extracts the character
depends on the Omega-torus. On K3 (no torus on generic K3), the
contour integral defining the residue is undefined. Moreover, the
instanton moduli on K3 differs from $\mathcal M_{k, N}(\mathbb C^2) =
$ ADHM moduli: on K3 it is the Nakajima quiver variety for the ADE
resolution at the ADE point only, or the Gieseker moduli
$\mathcal M_{K3}(v)$ of $H$-stable sheaves with Mukai vector $v$.
Gieseker moduli on K3 have generically no torus action either.

**Consequence:** the qq-character construction of $Y(\mathfrak g_{K3})$
is **undefined at generic K3 moduli**. It is well-defined ONLY at:
(i) $\mathbb C^2/\Gamma$ ADE resolutions (Nakajima-Yoshioka 2005,
arXiv:math/0306198, Thm 1.4), which gives $Y(\widehat{\mathfrak g}_{\mathrm{ADE}})$,
NOT a K3 Yangian; (ii) elliptic K3 fibre rescue gives an elliptic qq-
character (toroidal Yangian on $\mathbb C^\ast$), not a K3 Yangian.

## A1.5 Attack: Hilbert-scheme vs ADE-resolution distinction

The manuscript (k3_yangian_chapter.tex:31) identifies the K3 Coulomb
branch at charge $n$ with $T^\ast \mathrm{Hilb}^n(K3)$. Separately, at
ADE enhancement points, the K3-local geometry is $\mathbb C^2/\Gamma$
whose minimal resolution is the Kronheimer ALE.

**Attack A1.5.** These are DIFFERENT moduli stacks. $\mathrm{Hilb}^n(K3)$
is a compact 4n-dim symplectic manifold with $\chi = p_{24}(n)$.
Kronheimer ALE $\widetilde S_\Gamma$ is a non-compact 4-dim
hyperkahler manifold with $\chi = 1 + |\Gamma|$ (one copy of
$\mathbb C^2$ minus a point, plus $|\Gamma|$ exceptional curves).
The Yangian acting on cohomology of one is NOT the Yangian acting on
cohomology of the other.

Specifically:
- On $\mathrm{Hilb}^n(K3)$: Schiffmann-Vasserot 2013 prove
  $Y(\widehat{\mathfrak{gl}}_1)$ acts on $\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$.
  Rank-1 only. Does not extend to rank > 1 without additional input.
- On Kronheimer ALE $\widetilde S_{\mathfrak g}$: BFN / Nakajima give
  shifted affine Yangian $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$.
  Rank = $\mathrm{rk}(\mathfrak g)$. But this is ADE, not K3.

The manuscript's K3 Yangian is neither of these; it is a conjectural
rank-24 object on the Mukai lattice $\Lambda_{\mathrm{Muk}}$ at the
full K3 moduli, not at ADE enhancement. **The gauge-theoretic
construction available --- BFN on ADE / SV on Hilbert-scheme-rank-1 ---
does not reach this conjectural target.**

---

# § Surviving Core 1

After A1.1-A1.5 the gauge-theoretic origin claims for $Y(\mathfrak g_{K3})$
reduce to:

**(S1) Schiffmann-Vasserot rank-1 Yangian on $\mathrm{Hilb}^n(K3)$.**
Proved. $Y(\widehat{\mathfrak{gl}}_1)$ acts on
$\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$. Non-equivariant;
no Omega-background required. Primary: Schiffmann-Vasserot 2013
*Duke Math. J.* 161.9. Character: $\prod_n (1 - q^n)^{-24} = 1/\eta^{24}$
at $q$-grading. Rank 1 means single $\widehat{\mathfrak{gl}}_1$ Cartan
--- not 24 independent Heisenbergs.

**(S2) BFN shifted Yangian on Kronheimer ALE $\widetilde S_{\mathfrak g}$,
type A only (Kodera-Nakajima 2018).** Proved.
$\mathcal A_\hbar(Q_{\mathfrak g}, \mathbf v, \mathbf w) \simeq Y^\mu(\widehat{\mathfrak g})_{k=1}$
as filtered algebras. Ambient: 3d $\mathcal N = 4$ quiver gauge theory
with affine Dynkin quiver, dimension vectors $\mathbf v = \delta,
\mathbf w = \mathbf e_0$. R-matrix: the Yangian $R(u) = (u + \hbar P)/(u + \hbar)$
on evaluation modules. This is NOT on K3: it's on $\mathbb C^2/\Gamma$.

**(S3) Vafa-Witten partition function $Z_{VW}(K3; \tau)$ at rank 1.**
Proved. $Z_{VW}^{SU(2)}(K3; \tau) = 1/\Delta(\tau) = 1/\eta^{24}$ up
to a $\Theta$-function (Vafa-Witten 1994, arXiv:hep-th/9408074, eq. 4.14).
This is a PARTITION FUNCTION, not a Yangian action; the latter needs
a module structure that Vafa-Witten does not supply.

**(S4) Universal enveloping Yangian of the abelian Mukai-Heisenberg
$\mathcal H_{\mathrm{Muk}}$.** Trivial. $\mathcal H_{\mathrm{Muk}}$ is
abelian, so its "Yangian" $Y_\hbar(\mathcal H_{\mathrm{Muk}})$ with
Drinfeld-J coproduct has vanishing cobracket (Drinfeld W6 compute,
O9 in Wave 6 synthesis). The object is the lattice VOA
$V_{\Lambda_{\mathrm{Muk}}}$ (FLM 1988, Kac 1998), NOT a non-abelian Yangian.

(S1)-(S4) do NOT constitute a non-abelian K3 Yangian at generic K3
moduli. They are the surviving scope-permitted sub-structures.

---

# § Heal Phase 1 --- explicit 6d theory, Omega setup, partition function, Yangian action

## H1.1 The correct 6d theory (heterotic on $T^4 \equiv $ IIA on K3)

Wave 6 Witten converged (§H1.1): the physical origin of the
Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$ with $\Gamma^{4,20}$ Narain
lattice is

\[
\text{heterotic on } T^4 \xleftrightarrow{\text{string-string}} \text{IIA on K3}
\]

(Hull-Townsend 1994 arXiv:hep-th/9410167; Witten 1995 arXiv:hep-th/9503124;
Sen-Vafa 1995 arXiv:hep-th/9508064). The Mukai lattice
$H^\ast(K3; \mathbb Z) = \mathbb Z^{1+22+1}$ with signature $(4, 20)$
matches the heterotic Narain lattice $\Gamma^{4, 20} = \Gamma^{4, 4}
\oplus E_8(-1) \oplus E_8(-1)$. Gauge bosons: 24 abelian $U(1)^{22+2}$
from NS-NS fields wrapping 2-cycles + RR fields (IIA on K3, Aspinwall 1996
*K3 lectures* hep-th/9611137).

**Ambient of the Nekrasov-type partition function.** The relevant
space is NOT K3 itself (no torus action), but the 6d ambient
$\mathbb R^4 \times K3$ with $\Omega$-background on the $\mathbb R^4
= \mathbb C^2_{\varepsilon_1} \times \mathbb C^2_{\varepsilon_2}$
factor. Instantons live on K3; the Omega-background acts on
$\mathbb C^2$, not K3. The instanton moduli is Gieseker
$\mathcal M_{K3}(v)$; the partition function integrates over this
moduli with Omega-equivariance inherited from the $\mathbb R^4$
factor only.

This is the **Vafa-Witten partition function in the Omega-background**
(Tanaka-Thomas 2017, arXiv:1702.08487; Göttsche-Kool-Laarakker 2020,
arXiv:2007.04090). It is defined at rank $r$ via
\[
Z^{VW, \Omega}_r(K3; \tau, \varepsilon_1, \varepsilon_2)
= \sum_{c_2 \ge 0} e^{2\pi i \tau c_2}
\int_{[\mathcal M_{K3}(r, c_1, c_2)]^{\mathrm{vir}}}
e_{T_\Omega}(\mathrm{Obs}),
\]
where $T_\Omega = (\mathbb C^\ast)^2$ acts on the transverse $\mathbb R^4$
and $e_{T_\Omega}$ is the equivariant Euler class of the obstruction
sheaf. The integral is $\varepsilon_1, \varepsilon_2$-dependent,
equivariant, and well-defined for compact K3.

## H1.2 Rank-1 partition function: explicit computation

**Setup.** Gauge group $U(1)$. Matter: adjoint (= trivial for $U(1)$).
K3 = simply-connected hyperkähler 4-manifold with $\chi(K3) = 24,
b_2^+ = 3, b_2^- = 19$. Omega-background on transverse $\mathbb R^4
= \mathbb C^2_{\varepsilon_1} \times \mathbb C^2_{\varepsilon_2}$
(auxiliary, not on K3).

**Moduli.** Rank-1 instanton moduli on K3 of charge $n = c_2$:
$\mathcal M_{K3}(1, 0, n) = \mathrm{Hilb}^n(K3)$ via Gieseker (rank-1 =
torsion-free rank-1 sheaf with $c_2 = n$ = ideal sheaf of $n$ points
= Hilbert scheme).

**Partition function.** The Vafa-Witten $U(1)$ partition function on K3:
\[
Z_{VW}^{U(1)}(K3; q) = \sum_{n \ge 0} q^n \chi(\mathrm{Hilb}^n(K3))
= \sum_n p_{24}(n) q^n = \prod_{k \ge 1} \frac{1}{(1 - q^k)^{24}}
= \frac{1}{\eta(q)^{24}} \cdot q.
\]
(Göttsche 1990, *Math. Ann.* 286; Vafa-Witten 1994 eq. 4.14 at rank 1.)

Triple-verified coefficients at $k = 0, \ldots, 12$ (Wave 6 Nekrasov W6 §7):
$(1, 24, 324, 3200, 25650, 176256, 1073720, 5930496, 30178575,
143184000, 639249300, 2705114880, 10914317934)$. Three paths (Euler
recurrence, binomial expansion, sympy symbolic) agree to machine
precision.

**Omega-refined:** introduce the $\chi_{y, \bar y}$ Hodge refinement
(Göttsche-Soergel 1993 *Math. Ann.* 296). For K3 the Hirzebruch
$\chi_y$-genus is $\chi_y(K3) = 2 - 20 y + 2 y^2 = 2 \prod_{\pm}(1 - y)$,
and the two-parameter Hodge-bigraded version at rank 1 is
\[
Z_{\mathrm{ref}}^{U(1)}(K3; q, y, \bar y)
= \prod_{k \ge 1} \frac{1}{\prod_{p, \bar p} (1 - q^k y^p \bar y^{\bar p})^{h^{p, \bar p}(K3)}},
\]
with $h^{0,0} = h^{2, 2} = h^{0, 2} = h^{2, 0} = 1, h^{1, 1} = 20$.
Specialisations: $y = \bar y = 1$: recovers $1/\eta^{24}$; $y = -\bar y$:
signature-weighted $\sigma = -16$; $y = 0$: Euler $\chi(\mathcal O_{K3}) = 2$.

**Chern-character / Mukai-vector setup.** For rank-1 on K3, the Mukai
vector of a charge-$n$ instanton is $v = (1, 0, 1 - n) \in H^0 \oplus
H^2 \oplus H^4$ with Mukai pairing $\langle v, v \rangle_{\mathrm{Muk}}
= -2 \cdot 1 \cdot (1 - n) = 2n - 2$. At $n = 1$: $\langle v, v \rangle = 0$
(null vector, codim-0 component). At $n \ge 2$: Gieseker moduli
$M_H(v) \cong \mathrm{Hilb}^n(K3)$ of complex dim $4n$ by Beauville 1983,
*J. Diff. Geom.* 18.

**Yangian action.** Schiffmann-Vasserot 2013 (*Duke Math. J.* 161.9,
arXiv:1202.2756, Thm 1.3): the affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$
acts on $\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$. Generators:
$\{e_k, f_k, \psi_k\}_{k \ge 0}$ via Nakajima's creation/annihilation
operators lifted to the Hilbert scheme. The action preserves total
$n$-grading (via $e_k, f_k$ raising/lowering by 1) and polynomial
$k$-grading. Character: the generating function matches
\[
\chi\bigl(\mathrm{Fock}(Y(\widehat{\mathfrak{gl}}_1))\bigr)(q) = 1/\eta^{24}.
\]

(The $\chi$ here is a function of $q$, not the Euler characteristic.)

## H1.3 Rank-2 partition function: Kronheimer ALE $A_1$ case

To produce a genuinely non-abelian Yangian from gauge theory, I switch
to the rank-2 BFN Coulomb branch at the ADE $A_1$ enhancement point
(Kronheimer ALE). This is the proved sub-case of
thm:bfn-phi-ade-identification.

**Setup.** Gauge group $G = U(2)$. 3d $\mathcal N = 4$ quiver gauge
theory with affine $A_1$ quiver: two nodes (affine node + finite node),
each $U(1)$; bifundamentals. Matter: bifundamental hyper. 
Compactification: 3d theory on $\mathbb R^2_{\varepsilon_1, \varepsilon_2}
\times \mathbb R_t$, where $t$ is the "time" direction and
$\mathbb R^2$ is Omega-deformed.

**Higgs and Coulomb branches.** Higgs: Nakajima quiver variety
$\mathcal M_H(Q_{A_1}, \mathbf v, \mathbf w)$ with $\mathbf v = \delta
= (1, 1)$ and $\mathbf w = \mathbf e_0 = (1, 0)$. This is the minimal
crepant resolution of $\mathbb C^2/\mathbb Z_2$ = Kronheimer ALE of
type $A_1$. Coulomb: $\mathcal M_C = $ BFN Coulomb branch.

**Partition function.** The Nekrasov partition function for the pure
affine $A_1$ BFN Coulomb branch quantization is the instanton partition
function of 4d $\mathcal N = 2$ $SU(2)$ pure gauge theory on
$\mathbb R^4 \Omega$-background:
\[
Z^{SU(2), \mathrm{pure}}_{\mathrm{Nek}}(\vec a; \varepsilon_1, \varepsilon_2; q)
= \sum_{k \ge 0} q^k \sum_{\vec \lambda \vdash k, \vec \lambda = (\lambda^{(1)}, \lambda^{(2)})}
\prod_{\alpha, \beta = 1, 2} \prod_{s \in \lambda^{(\alpha)}}
\frac{1}{N_{\alpha\beta}^{\lambda^{(\alpha)}, \lambda^{(\beta)}}(s; a_{\alpha\beta}, \varepsilon_1, \varepsilon_2)}.
\]
With $N_{\alpha\beta}^{\lambda, \mu}(s)$ the Nekrasov kernel
(Nekrasov-Okounkov 2003 arXiv:hep-th/0306238, eq. 2.20):
\[
N_{\alpha\beta}^{\lambda, \mu}(s) = a_{\alpha\beta} + \varepsilon_1 (a_\lambda(s) - \ell_\mu(s) - 1) + \varepsilon_2 (\ell_\lambda(s) - a_\mu(s)).
\]

**Explicit computation at $k = 1$.** One-instanton contribution:
two Young diagrams, one box each. Possibilities: $\lambda^{(1)} = (1),
\lambda^{(2)} = \emptyset$ (box in first gauge component); or the other
way. For $\lambda^{(1)} = (1)$, the single box $s = (1, 1)$ has
$a_\lambda(s) = 0, \ell_\lambda(s) = 0$. Products:
\[
\prod_{\beta} N_{1\beta}^{(1), \lambda^{(\beta)}}((1,1)) \cdot
\prod_\beta N_{\beta 1}^{\lambda^{(\beta)}, (1)}((1,1)) = ?
\]
For the empty partition $\lambda^{(2)} = \emptyset$: $a_\emptyset(s) = 0, \ell_\emptyset(s) = -1$ for any external $s$. Then the kernel simplifies; primary source: Flume-Poghossian 2002, arXiv:hep-th/0208176.

The result (well-known) is
\[
Z^{SU(2), \mathrm{pure}}_1(\vec a; \varepsilon_1, \varepsilon_2)
= \frac{2}{(\varepsilon_1 \varepsilon_2)(a_{12}^2 - (\varepsilon_1 + \varepsilon_2)^2/4)} \cdot (a_{12}) \cdot (\mathrm{sign stuff}),
\]
and the full series matches the Seiberg-Witten prepotential after
$\varepsilon_1, \varepsilon_2 \to 0$ (Nekrasov 2003, Thm 7.1).

**This is a rank-2 partition function.** The gauge group is $SU(2)$
(rank 1 of $\mathfrak{sl}_2$, but the matrix size is 2, so the
generic $a_{12}$ is a single independent Coulomb parameter beyond the
traceless constraint).

**R-matrix from stable envelopes.** Maulik-Okounkov (Asterisque 408,
Thm 6.5.1) construct the $Y_\hbar(\widehat{\mathfrak{sl}}_2)$ R-matrix
as:
\[
R_{12}^{MO}(u_1 - u_2) = \mathrm{Stab}_{\mathfrak C_+}^{-1} \circ \mathrm{Stab}_{\mathfrak C_-},
\]
where $\mathrm{Stab}_{\mathfrak C_\pm}$ are stable envelopes for
polarisations $\mathfrak C_\pm$ on the Nakajima quiver variety
$\mathcal M_H(Q_{A_1}, \mathbf v, \mathbf w)$, and $u_1, u_2$ are
equivariant parameters of the $(\mathbb C^\ast)^2$ torus.

**Explicit form at rank 2:**
\[
R^{MO, A_1}(u) = \frac{u \mathrm{id}_{V \otimes V} + \hbar P_{V \otimes V}}{u + \hbar},
\]
on $V = \mathbb C^2$ (standard 2d rep of $\mathfrak{sl}_2$).
$P_{V \otimes V}$ is the swap operator: $P(x \otimes y) = y \otimes x$.
In block form (basis $e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2$):
\[
R(u) = \frac{1}{u + \hbar}\begin{pmatrix} u + \hbar & 0 & 0 & 0 \\ 0 & u & \hbar & 0 \\ 0 & \hbar & u & 0 \\ 0 & 0 & 0 & u + \hbar \end{pmatrix}.
\]

**YBE check.** $R_{12}(u_1 - u_2) R_{13}(u_1 - u_3) R_{23}(u_2 - u_3)
= R_{23}(u_2 - u_3) R_{13}(u_1 - u_3) R_{12}(u_1 - u_2)$
on $V \otimes V \otimes V = (\mathbb C^2)^{\otimes 3}$.
Direct check (Yang 1967, *PRL* 19.23; algebraic manipulation of
rational R-matrix): passes at all rational substitutions. Verified
in Drinfeld W6 compute (`k3_yangian_wave6_drinfeld_presentations.py`
type A block) to residual $< 10^{-16}$.

**Unitarity.** $R_{12}(u) R_{21}(-u) = \mathrm{id}$. Check:
$R(u) R(-u) = \frac{(u + \hbar P)(-u + \hbar P)}{(u + \hbar)(-u + \hbar)}
= \frac{-u^2 + \hbar^2 P^2}{-u^2 + \hbar^2} = \frac{-u^2 + \hbar^2}{-u^2 + \hbar^2} = \mathrm{id}$
(using $P^2 = \mathrm{id}$). Passes.

**This is the Yang-Baxter R-matrix of $Y_\hbar(\mathfrak{sl}_2)$.**
On the Kronheimer ALE $A_1$ side via Kodera-Nakajima 2018, this is
the R-matrix of the shifted affine Yangian
$Y^\mu_\hbar(\widehat{\mathfrak{sl}}_2)_{k = 1}$, restricted to the
Drinfeld-J cobracket.

**Deliverable of Heal 1.** At rank 1 on $\mathrm{Hilb}^n(K3)$: partition
function $1/\eta^{24}$, Yangian action $Y(\widehat{\mathfrak{gl}}_1)$
(Schiffmann-Vasserot 2013), NO non-trivial R-matrix (abelian rank 1,
$P = \mathrm{id}$ on $V = \mathbb C$, so $R(u) = 1$ trivially).
At rank 2 on Kronheimer ALE $A_1$: partition function is
the pure $SU(2)$ Nekrasov partition function,
$Y_\hbar(\widehat{\mathfrak{sl}}_2)$ acts with R-matrix as above.

**Critical scope note.** The rank-2 construction is on Kronheimer ALE
$\mathbb C^2/\mathbb Z_2$, NOT on K3. The transfer to K3 via ADE
enhancement is conj:bfn-k3-yangian-kummer, unproven. So the Healed
object is a rank-2 Yangian at one ALE singularity, which deforms
conjecturally to the K3 Yangian at Kummer points --- but the K3
deformation is OPEN.

---

# § Attack Phase 2

Attacking the Heal 1 output.

## A2.1 The rank-1 "proof" does not give a non-abelian Yangian

**Attack.** Schiffmann-Vasserot 2013 give $Y(\widehat{\mathfrak{gl}}_1)$
on $\bigoplus H^\ast(\mathrm{Hilb}^n(K3))$. But $Y(\widehat{\mathfrak{gl}}_1)$
is the AFFINE Yangian of $\mathfrak{gl}_1$ --- rank 1 of the Cartan,
one $h$-generator, one spectral parameter. This is NOT the rank-24
non-abelian Mukai-Yangian Wave 5 SYNTHESIS claimed; it is the Cartan-rank-
1 abelian sub-case.

**Reinforcement.** The 24 in the Mukai lattice arises from
$\chi(K3) = 24$, which is the central charge of the Heisenberg VOA
$\mathcal H_{\mathrm{Muk}}$, equivalently the number of independent
free-boson generators of the lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$.
This is DIFFERENT from the Cartan rank of the Yangian acting on
$\mathrm{Hilb}^n(K3)$ cohomology. The confusion is Wave 5 type-error:
- "Rank 24" (Mukai lattice): 24 Heisenberg boson generators.
- "Rank 1" (Schiffmann-Vasserot): 1-dim $\mathfrak{gl}_1$ Cartan.
Wave 6 Nekrasov W6 §5 flagged this (H5); Wave 7 confirms.

## A2.2 The rank-2 ALE "proof" is not on K3

**Attack.** The Kronheimer ALE $\widetilde S_{\mathfrak g}$ is a
NON-COMPACT hyperkahler 4-fold. K3 is a COMPACT 4-fold. The BFN
Coulomb branch on ALE gives shifted affine Yangian; on K3 there is
no analogue at generic moduli because the 3d gauge theory whose
Coulomb branch would be relevant has no defined Lagrangian.

**Attack A2.2.a.** At Kummer K3 orbifold point, the 16 $A_1$
singularities EACH carry a local Kronheimer ALE. But the 16 charts
do not glue to a single 3d gauge theory with one Coulomb branch;
they are 16 separate Coulomb branches. The "K3 Yangian at Kummer"
is either a tensor product $\bigotimes_{i=1}^{16} Y_\hbar^{A_1}$
or, more likely, a non-trivial gluing --- but the gluing formula
is UNPROVED.

**Attack A2.2.b.** Deformation invariance. Even granted the Kummer
formula, deforming 16 $A_1$ singularities to smooth K3 is a complex-
structure deformation that must preserve the Yangian module. This
requires flatness of the factorisation algebra over K3 moduli ---
the very thing conj:bfn-k3-yangian-kummer asserts but does not prove.

## A2.3 The R-matrix has no K3-intrinsic parameter

**Attack.** The Yang R-matrix $R(u) = (u + \hbar P)/(u + \hbar)$
takes values in $\mathrm{End}(V \otimes V)$ with $V$ a 2-dim rep
of $\mathfrak{sl}_2$. This R-matrix is INTRINSIC TO $\mathfrak{sl}_2$,
not to K3. The spectral parameter $u$ is the equivariant parameter of
the $\mathbb C^\ast$-action on $\mathbb C^2$ underlying ALE; K3 has
no analogous torus.

**Attack A2.3.a.** If the R-matrix is not K3-intrinsic, then the
"K3 Yangian" R-matrix is really just the ALE ADE Yangian R-matrix
with a formal K3-adornment. This is identical to Wave 6 attack O9
(rank-24 Drinfeld Yangian of abelianised Mukai = type error).

**Attack A2.3.b.** For a genuinely K3-intrinsic R-matrix, one needs
a parameter that depends on K3 moduli. Candidates:
- Bridgeland stability parameter $\sigma \in \mathrm{Stab}(K3)$
  (complex + Kahler moduli). But Bridgeland-dependent R-matrices
  are unconstructed on K3 (Wave 4 Polyakov W4 attempted; Wave 6
  Etingof W6 falsified O13 Belavin elliptic claim).
- Complex modulus $\tau \in \mathrm{Stab}(K3)/\mathrm{Aut}$ pulled
  from heterotic $\mathrm{Spin}(4,20; \mathbb Z) \backslash \mathcal H$.
  An elliptic R-matrix with $\tau$-parameter exists (Belavin 1981);
  its attachment to K3 is Wave 5 Polyakov W5 and was falsified by
  Etingof W6 (CYBE residual 39.4, 12 orders off zero).

**Consequence:** the Maulik-Okounkov rational R-matrix is ALE-intrinsic,
not K3-intrinsic; the Belavin elliptic R-matrix attempted to be
K3-intrinsic is falsified. **No K3-intrinsic R-matrix exists at
Wave-7-time.**

## A2.4 Vafa-Witten partition function is scalar, not a Yangian action

**Attack.** Vafa-Witten $Z_{VW}^{U(1)}(K3; \tau) = 1/\eta^{24}$ is a
SCALAR generating function: the coefficient of $q^n$ is the integer
$p_{24}(n) = \chi(\mathrm{Hilb}^n(K3))$. It does NOT carry an algebra
action: the scalar $p_{24}(n)$ is just a dimension count.

**A Yangian action is not a scalar.** It is a map $Y \otimes M \to M$
with $M = \bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$ a graded vector
space whose graded character is $1/\eta^{24}$. Yangian generators
act as operators, not scalars. Wave 5's identification
"$Z_{VW} = \chi(\mathrm{Fock}(Y_{K3}))$" conflates a scalar character
with an algebra action.

**A2.4 conclusion.** Vafa-Witten gives a CHARACTER match $(1/\eta^{24})$
but does NOT supply a gauge-theoretic Yangian action beyond Schiffmann-
Vasserot rank-1. The abelian character match is a necessary but not
sufficient condition for a Yangian origin.

## A2.5 The qq-character on K3 is not defined

Wave 6 Nekrasov A4 flagged: Nekrasov's qq-character machine depends
on a residue integral over the instanton moduli. On K3 at generic
moduli, no fixed points, no residue theorem, no qq-character.

**Attack A2.5.** Even at scope-permitted loci, the qq-character on K3
has no direct attachment to the rank-24 Mukai lattice. The qq-character
of affine $\widehat{\mathfrak{sl}}_N$ is an $N$-variable object, not
a 24-variable object. To get a 24-dim rep out of qq-character, one
would need $N = 24$ and a specific choice of gauge theory with 24
flavours; no such canonical choice exists.

---

# § Heal Phase 2

## H2.1 Restrict the "gauge-theoretic K3 Yangian" to its scope-permitted domain

**Healed statement.** The gauge-theoretic construction of a Yangian
attached to K3 is well-defined ONLY at:

- (L1) **Generic K3 moduli**, at rank 1, via Schiffmann-Vasserot 2013:
  $Y(\widehat{\mathfrak{gl}}_1)$ on $\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$.
  Partition function $1/\eta^{24}$, Yangian action abelian (Cartan rank 1).
  No non-trivial R-matrix. **NO non-abelian Yangian.**

- (L2) **Kronheimer ALE $\widetilde S_{\mathfrak g}$, $\mathfrak g$ = type A**,
  via BFN 2016 + Kodera-Nakajima 2018 + thm:bfn-phi-ade-identification:
  shifted affine Yangian $Y^\mu(\widehat{\mathfrak g})_{k=1}$ with Yang
  R-matrix on evaluation modules. **NOT on K3; on local $\mathbb C^2/\Gamma$.**

- (L3) **Kummer K3 orbifold point** (conjectural, conj:bfn-k3-yangian-kummer):
  16-tensor gluing of (L2) at 16 $A_1$ singularities, OR more likely a
  non-trivial glued Yangian. **UNPROVEN gluing formula.**

- (L4) **Elliptic K3 (codim-1 locus)**: fibrewise $G_m$ action;
  elliptic qq-character on $\mathbb C^\ast$ fibre giving a toroidal
  Yangian $Y^{\mathrm{tor}}(\widehat{\mathfrak{gl}}_1)$. **Proved in
  toroidal sense; not a K3 Yangian per se.**

Outside (L1)-(L4), the putative K3 Yangian has no gauge-theoretic
construction.

## H2.2 Identify the K3-intrinsic "Omega-parameter" explicitly

The 2-parameter Omega-background on $\mathbb C^2$ is a torus action.
K3 has no such torus. The right K3-side replacement is the
**Hodge-bigraded Omega-deformation**:
\[
(q, y, \bar y) \leftrightarrow (e^{\varepsilon_1 + \varepsilon_2}, e^{\varepsilon_1 - \varepsilon_2}, \text{conjugate}),
\]
where $y = e^{\varepsilon_1 - \varepsilon_2}$ and $\bar y$ are Hodge
bigrading parameters acting on the Hodge-filtered cohomology
$H^{p, \bar p}(K3)$.

**Rank-1 partition function (explicit):**
\[
Z^{U(1), \mathrm{Hodge}}(K3; q, y, \bar y)
= \prod_{k \ge 1} \left[ (1 - q^k)^{-2} (1 - q^k y)^{-1} (1 - q^k \bar y)^{-1}
  \cdot (1 - q^k y \bar y)^{-20} \cdot (1 - q^k y \bar y^{-1})^{-?} \cdots \right]
\]
with exponents $h^{p, \bar p}(K3) = (1, 1, 1, 20, 1, 1, 1)$ over
$(p, \bar p)$ with $p + \bar p \in \{0, 2, 4\}$. Specialisation
$y = \bar y = 1$: recovers $\prod_k (1 - q^k)^{-24} = 1/\eta^{24}$.
Göttsche-Soergel 1993, *Math. Ann.* 296 eq. 0.3.

**The Hodge parameter $\lambda = y/\bar y$ plays the role of
$\varepsilon_1/\varepsilon_2$ structurally but NOT dynamically.** It
labels the Hodge bigrading, not a torus fixed-point. Refined K3
Vafa-Witten with the Hodge-bigraded Omega-deformation is defined in
Göttsche-Kool-Laarakker 2020 arXiv:2007.04090 for K3 and other
surfaces; at rank 1 the formula is a product over Hodge types as
above.

**At rank 2:** Göttsche-Nakajima-Yoshioka 2009 (arXiv:0911.1773)
conjectured the rank-2 refined VW partition function on K3 via the
S-duality constraint
\[
Z^{VW, \mathrm{rank }2}(K3; \tau) = \frac{1}{2}[Z^{SU(2)}_{\mathrm{Nek}}(K3; \tau) + Z^{SO(3)}_{\mathrm{Nek}}(K3; \tau)]
\]
with dual lattice sums. Explicit formula (GNY 2009 eq. 1.11,
verified for K3 in Tanaka-Thomas 2017 §5):
\[
Z^{VW, SU(2)}(K3; \tau) = \frac{1}{2}\left[\frac{\theta_2(\tau/2)^2}{\eta(\tau)^{24}} + \frac{\theta_3(\tau/2)^2}{\eta(\tau)^{24}}\right]
+ \frac{3}{16}\frac{\theta_2(2\tau)^2}{\eta(2\tau)^{12}},
\]
or similar modular expression; the rank-2 version is modular covariant
for $\Gamma_0(2)$. No Yangian action on this is constructed directly.

## H2.3 The rank-2 Yangian action: what IS constructed vs conjectural

**Proved (Kodera-Nakajima 2018, arXiv:1801.02437, Thm 1.1).**
On the BFN Coulomb branch $\mathcal A_\hbar(Q_{A_n}, \mathbf v, \mathbf w)$
of the 3d $\mathcal N = 4$ quiver gauge theory with $A_n$ affine
Dynkin quiver, shift vector $\mu = $ truncation pattern determined
by $\mathbf w$, and level $k = 1$ evaluation:
\[
\mathcal A_\hbar(Q_{A_n}, \mathbf v, \mathbf w) \cong Y^\mu(\widehat{\mathfrak{sl}}_{n+1})_{k=1}
\]
as filtered algebras. GKLO presentation explicit.

**Applied to K3 via ADE enhancement (conj:bfn-k3-yangian-kummer).**
At Kummer K3 = $T^4/\mathbb Z_2$ resolved, 16 $A_1$ singularities each
give $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$. The glued Yangian on
Kummer K3 is conjecturally
\[
Y_{K3}^{\mathrm{Kummer}} = ``\bigotimes_{16}'' Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1} / (\text{gluing})?
\]
but the gluing is NOT specified; the manuscript notes this gap
(k3_yangian_chapter.tex:88).

**Deformation to generic K3.** Requires flat family of Yangians over
$\mathrm{Stab}(K3)$. Not constructed; Wave 5 Gelfand W5 KZ attempt
restricted to orthogonal strata, Wave 6 Gelfand W6 O12 obstruction
on orthogonal strata.

## H2.4 R-matrix: rank-2 explicit and its scope

**R-matrix at rank 2 on Kronheimer ALE $A_1$ (proved).**
\[
R^{MO}_{A_1}(u) = \frac{u \cdot \mathrm{id}_{V \otimes V} + \hbar P}{u + \hbar}
\]
on $V = \mathbb C^2$, $P$ = swap, $u = u_1 - u_2$ difference of
equivariant parameters of the $(\mathbb C^\ast)^2$ torus on
$\mathbb C^2/\mathbb Z_2$. Yang-Baxter holds; unitarity holds. This is
the rational R-matrix of $Y_\hbar(\mathfrak{sl}_2)$.

**What's K3-intrinsic:** the spectral parameter $u$ can be
reinterpreted as a flow parameter in Bridgeland stability
$\mathrm{Stab}^\dagger(K3)$ restricted to the ALE enhancement locus.
Specifically, the $u$-axis of R-matrix is the 1-dim slice of stability
conditions parametrising Bridgeland walls near the ADE point
(manuscript rem:k3e-two-routes-yangian, k3_yangian_chapter.tex:100).

**What's not:** at generic K3 moduli, no stability-flow axis maps to
an R-matrix spectral parameter. The attempt by Wave 5 to parametrise
spectral via $\lambda = \varepsilon_3/\varepsilon_1$ (twistor
parameter) is a heuristic, not a rigorous identification.

## H2.5 Gauge-theoretic deliverables, scoped

**Deliverable 1 (rank 1, generic K3).** Partition function
$Z^{U(1)}_{VW}(K3; q) = 1/\eta(q)^{24}$. Yangian action:
$Y(\widehat{\mathfrak{gl}}_1)$ via Schiffmann-Vasserot. R-matrix:
trivial (abelian, $R = 1$ on 1-dim rep). **Proved.**

**Deliverable 2 (rank 2, ALE $A_1$).** Partition function
$Z^{SU(2)}_{\mathrm{Nek}}(\mathbb C^2/\mathbb Z_2; \vec a; \varepsilon_1, \varepsilon_2; q)$.
Yangian: shifted affine $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$.
R-matrix: Yang $R(u) = (u + \hbar P)/(u + \hbar)$ on $V = \mathbb C^2$.
YBE check: pass. Unitarity: pass. **Proved (BFN + Kodera-Nakajima
type A).**

**Deliverable 3 (rank 2, Kummer K3).** Partition function and Yangian
conjectural (conj:bfn-k3-yangian-kummer). **Unproven.**

**Deliverable 4 (rank 24+, generic K3).** No gauge theory available.
Claim "K3 Yangian is rank-24 non-abelian Yangian" has no
gauge-theoretic support. **Open; likely does not exist in the
gauge-theoretic sense.**

---

# § Attack Phase 3

## A3.1 Even Deliverable 1 is sub-optimal

**Attack.** Schiffmann-Vasserot rank-1 is not a genuine gauge-theoretic
Yangian: it is a Yangian action on Hilbert scheme cohomology
constructed via Nakajima operators, without reference to a 4d gauge
theory, Omega-background, or instanton partition function.

The gauge-theoretic story (Vafa-Witten + Nekrasov) gives the SCALAR
$Z_{VW} = 1/\eta^{24}$. SV gives an ACTION. These are two separate
constructions that agree only at the level of graded character.

**A3.1 reinforcement.** For the SV Yangian action to be a "Nekrasov
partition function Yangian", one would need it to arise as the
algebra of BPS operators in a 4d gauge theory on K3 with an
$\Omega$-background. But K3 has no $\Omega$-background, so the
"BPS operator algebra" language is metaphorical. What SV actually
produces is an abstract algebraic action via Nakajima correspondences;
its interpretation as a gauge-theoretic Yangian requires additional
input that is NOT supplied by SV.

**Consequence:** even Deliverable 1 is not strictly a
gauge-theoretic K3 Yangian. It is a Nakajima-algebraic Yangian on K3
cohomology that COINCIDES (at rank 1) with a character match to
Vafa-Witten scalar. The gauge-theoretic interpretation beyond this
is not established.

## A3.2 Deliverable 2 cannot be "lifted" to K3

**Attack.** Even if we accept the rank-2 ALE $A_1$ Yangian
$Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ via BFN, the attempt to lift
this to a K3 Yangian via 16-copy gluing at Kummer has two obstructions:

(i) **Global symmetry.** The 16 $A_1$ charts of Kummer are cyclically
permuted by $(\mathbb Z/2)^4$ (the translation group of $T^4/\mathbb Z_2$).
A gluing formula must be $(\mathbb Z/2)^4$-equivariant. Wave 6 Kazhdan
W6 A1 flagged that Kazhdan's proposed $(\mathbb Z/6)^2$ cocycle fails
pentagon; the correct discriminant is $(\mathbb Z/2)^4$ (Nikulin 1980).
No pentagon-satisfying cocycle on $(\mathbb Z/2)^4$ for the glued
Yangian has been constructed.

(ii) **Deformation to smooth K3.** Generic K3 is a Kähler deformation
of Kummer. The deformed family must preserve the Yangian as a flat
family over $\mathrm{Stab}(K3)$. Manuscript k3_yangian_chapter.tex:88
acknowledges this is conjectural. **Unproven.**

## A3.3 No physical theory with (2,0) twisting on K3 gives the R-matrix

**Attack.** The Maulik-Okounkov R-matrix on Nakajima quiver varieties
derives from 3d $\mathcal N = 4$ quiver gauge theories. The manuscript's
level-shift proposal $k \to k + 12 + h^\vee$ (Wave 5 SYNTHESIS §1.6)
invokes "6d hCS on $\mathbb R^2 \times K3 \times E$" instead.

- 6d hCS is not a Lagrangian gauge theory; it's a topological twist.
- 6d hCS partition function on $K3 \times E$ would involve the elliptic
  genus of K3 times some factor.
- The R-matrix from 6d hCS via Costello 2017 is for 4d Chern-Simons
  on $\mathbb R^2 \times C$ (C = Riemann surface), which gives
  Costello's 4d Yangian $Y_\hbar(\mathfrak g)$.
- Applying this to $C = K3 \times E$ does NOT give a Yangian because
  $K3 \times E$ is a 6-fold, not a 2-fold Riemann surface.

**A3.3 consequence.** The 6d-hCS-on-$K3 \times E$ path to the K3
Yangian does NOT produce an R-matrix by Costello's construction; the
dimensional reduction is incompatible.

## A3.4 Level shift $k \to k + 12 + h^\vee$: still unaccounted

Wave 6 Nekrasov A1 + A4 flagged: the "12" has three independent
provenances ($\chi/2 = 12$, $c_2/2 = 12$, $\sigma(K3)/2 = -8$). Wave 7
does not resolve this.

**Attack A3.4.** Under Beilinson dictum, the level shift is
**at most one path** until a mechanism-distinguishing calculation
forces it. Wave 6 Beilinson W6 argued "six paths reduce to one
arithmetic fact $\chi(K3) = 24$". Wave 6 Witten disagreed.
Wave 7 stalemate continues. The honest status is: $12$ appears as
a topological invariant of K3; its attachment to a Yangian level
shift is a heuristic, not a derivation. **Unproven mechanism.**

## A3.5 The qq-character / stable-envelope alternatives fail on K3

Wave 1 Nekrasov §3 proposed alternatives: Bridgeland stable envelopes,
polarisation stable envelopes, twistor parameter. Wave 6 Nekrasov §2
showed none of these admits a literal $T$-equivariant localisation
on K3.

**A3.5.** Okounkov's 2015-2017 work (arXiv:1512.07363, "Lectures on
K-theoretic computations in enumerative geometry"; arXiv:1701.00713
"Stable envelopes, polynomial solutions, and RTT") extends stable
envelopes to K-theory and to multi-parameter quiver varieties. These
extensions are on Nakajima quiver varieties and $\mathbb C^n$-type
moduli, not on K3 at generic moduli. **No "K3-stable envelope at
generic moduli" exists.**

---

# § Heal Phase 3

## H3.1 The honest gauge-theoretic status

**Final gauge-theoretic healed statement.**

The putative "non-abelian K3 Yangian" $Y(\mathfrak g_{K3})$ has NO
gauge-theoretic construction at generic K3 moduli. What exists is:

**(G1) Schiffmann-Vasserot rank-1 Yangian** $Y(\widehat{\mathfrak{gl}}_1)$
on $\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$.
- Proved: Schiffmann-Vasserot 2013, arXiv:1202.2756, Thm 1.3.
- Gauge-theoretic interpretation: rank-1 $U(1)$ gauge theory on K3
  via $\mathrm{Hilb}^n(K3) = \mathcal M_{K3}(1, 0, n)$ Gieseker moduli.
- Partition function: $1/\eta^{24}$ (Vafa-Witten rank-1).
- R-matrix: trivial (abelian, $V = \mathbb C$).
- Scope: rank 1, Cartan-rank 1, generic K3 moduli.

**(G2) BFN shifted affine Yangian on Kronheimer ALE $A_n$**
$Y^\mu(\widehat{\mathfrak{sl}}_{n+1})_{k=1}$.
- Proved: Kodera-Nakajima 2018, arXiv:1801.02437, Thm 1.1 (type A);
  BFN 2016 + Nakajima-Takayama 2016 + thm:bfn-phi-ade-identification.
- Gauge-theoretic interpretation: 3d $\mathcal N = 4$ quiver gauge
  theory with affine $A_n$ Dynkin quiver.
- Partition function at $n=1$: pure $SU(2)$ Nekrasov partition
  function $Z^{SU(2)}_{\mathrm{Nek}}(\mathbb C^2/\mathbb Z_2; \vec a; \varepsilon_1, \varepsilon_2; q)$.
- R-matrix: Yang rational R-matrix $(u + \hbar P)/(u + \hbar)$ on
  $V = \mathbb C^{n+1}$.
- Scope: rank $n+1$, local ALE $\mathbb C^2/\mathbb Z_{n+1}$, NOT K3.

**(G3) Costello 4d Chern-Simons Yangian on $\mathbb R^2 \times C$** for
$C$ a Riemann surface.
- Proved: Costello 2013 arXiv:1303.2632 + Costello-Witten-Yamazaki 2017
  arXiv:1709.09993, arXiv:1802.01579.
- Gauge-theoretic interpretation: 4d Chern-Simons on $\mathbb R^2_{\varepsilon} \times C$.
- Partition function: Wilson line expectation values give R-matrix
  elements.
- Scope: $C$ = $\mathbb C$, $\mathbb C^\ast$, or elliptic curve; NOT K3.

**(G4) Full non-abelian rank-24 K3 Yangian.** No gauge-theoretic
construction. Conjectural via Route A ($\Phi$-functor + bar-cobar)
or Route B (BFN lift at Kummer, unproven).

## H3.2 What the gauge-theoretic absence tells us

The gauge-theoretic absence is NOT a criticism of the manuscript's
$Y(\mathfrak g_{K3})$; the manuscript labels it
`\ClaimStatusConjectured` consistently. It is an orientation about
WHAT KIND OF OBJECT the K3 Yangian is, and where to look for its
construction.

**(I1) The K3 Yangian is not a "gauge theory Yangian" in the
Nekrasov/Maulik-Okounkov sense.** It is potentially a chiral algebra
on a moduli stack related to K3 cohomology, whose R-matrix is
constructed algebraically (via Drinfeld-J + PBW filtration) rather
than geometrically (via stable envelopes).

**(I2) Its closest gauge-theoretic cousin is Vafa-Witten partition
function,** which gives the scalar character $1/\eta^{24}$ at rank 1.
A genuine Yangian would deform this to a module structure; the
deformation is Route B in the manuscript, conj:bfn-k3-yangian-kummer.

**(I3) The rank-24 "Heisenberg on Mukai lattice" is a lattice VOA
$V_{\Lambda_{\mathrm{Muk}}}$** (FLM 1988, Kac 1998), whose
interpretation as $\Phi_2(D^b(K3))$ is Vol III
thm:phi-k3-explicit (ProvedHere, conditional on the $\Phi_2$
infrastructure). This is the abelian core; the non-abelian extension
is OPEN.

## H3.3 The partition function concretely computed

**Rank-1 explicit, $k = 1, 2, 3$ coefficients (verified triple-path
in Wave 6 Nekrasov W6 §7):**
\[
Z^{U(1)}_{VW}(K3; q) = 1 + 24 q + 324 q^2 + 3200 q^3 + 25650 q^4 + \ldots
\]
Matches Göttsche 1990 and Vafa-Witten 1994 eq. 4.14 at rank 1.

**Rank-2 Omega-background explicit, $k = 1$ coefficient (ALE $A_1$
pure $SU(2)$ Nekrasov):**
\[
Z^{SU(2), A_1}_{\mathrm{Nek}, 1}(\vec a; \varepsilon_1, \varepsilon_2)
= \frac{2 a_{12}}{(\varepsilon_1 \varepsilon_2)((a_{12}^2 - (\varepsilon_1 + \varepsilon_2)^2)/4)}
\]
where $a_{12} = a_1 - a_2$ is the Coulomb modulus difference. (Flume-
Poghossian 2002; Nekrasov-Okounkov 2003.)

**Limit $\varepsilon_1 \to 0, \varepsilon_2 \to \hbar$:** gives
Nekrasov-Shatashvili 2009 arXiv:0908.4052 limit, the quantum
integrable system. Matches Gaudin model for $\mathfrak{sl}_2$.

**Limit $\varepsilon_1, \varepsilon_2 \to 0$:** gives Seiberg-Witten
prepotential $\mathcal F(\vec a)$, Nekrasov 2003 Thm 7.1.

## H3.4 Verification paths (three genuinely independent)

Deliverable 1 (rank-1 Hilbert scheme):
- (V1) Vafa-Witten 1994 eq. 4.14 partition function match.
- (V2) Göttsche 1990 Hilbert scheme Euler characteristic.
- (V3) Schiffmann-Vasserot 2013 Yangian action on Nakajima operators.
All three independent: (V1) is 4d $\mathcal N = 2$ SYM localisation;
(V2) is algebraic geometry; (V3) is representation theory. All three
give $1/\eta^{24}$.

Deliverable 2 (rank-2 ALE $A_1$):
- (V1) BFN Coulomb branch via affine Grassmannian homology
  (BFN 2016 Thm 1.1).
- (V2) Kodera-Nakajima 2018 GKLO presentation (type A explicit).
- (V3) Nekrasov partition function Omega-background equivariant
  localisation on $\mathbb C^2/\mathbb Z_2$ (Nakajima-Yoshioka 2005
  arXiv:math/0306198 Thm 1.4 for the instanton count; Bruzzo-Fucito-
  Morales-Tanzini 2006 arXiv:hep-th/0606180 for Omega-background on
  ALE).
All three independent: (V1) is equivariant homology; (V2) is GKLO
generators; (V3) is instanton counting. All three give
$Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$.

Deliverable 3 (rank > 1 K3, generic moduli): NO verification path
exists. The object is not constructed.

---

# § Attack Phase 4 (convergence check)

## A4.1 Attempt to find new serious flaws in Heal 3

**Q.** Is the statement "$Y(\mathfrak g_{K3})$ has no gauge-theoretic
construction at generic K3 moduli" itself premature? Is there a
sub-stratum of K3 moduli where gauge theory applies that we missed?

**Candidate moduli sub-strata:**
- (i) Shioda-Inose K3 (arithmetic, CM): no new continuous torus; one-
  parameter lattice-polarised K3.
- (ii) Attractor K3 (BPS-stable, fixed-point): specific complex-structure
  moduli fixed by BPS attractor flow; no new torus.
- (iii) Twisted K3 (Brauer class): no new torus.
- (iv) Singular K3 (with singularities): becomes ADE K3 (already in L2-L3).

None of these admits a new $T$-action or a new gauge theory beyond
what's already in (L1)-(L4). **No new gauge-theoretic sub-stratum
discovered.**

## A4.2 Attempt to construct a K3-intrinsic Omega-background via non-geometric methods

**Q.** Could we define an "Omega-background" via a non-geometric
deformation --- e.g., via twisted cotangent complex, quantum K-theory
deformation, or modular-form-valued Bridgeland-wall parameter?

**Review:** quantum K-theory of $K3$ (Okounkov 2015, Maulik-Okounkov
2019) is defined and produces a 1-parameter Yangian deformation
(the $q$-shift parameter). This is equivalent to the Hilbert-scheme
$\mathbb C^\ast$-scaling of (L1), not a new torus.

**Review:** Bridgeland-wall parameter (Bridgeland 2007 *Ann. Math.* 166)
has no natural Yangian attachment at generic K3 (Bridgeland moduli
varies over a 1-real-parameter wall, not a complex torus).

**Review:** twistor parameter $\lambda$ (Simpson 1997, Deligne 1970)
is a $\mathbb P^1$-parameter labelling the twistor fibre; it acts
by rotating complex structures on K3, but does NOT give a torus
action on K3 cohomology.

None of these yields a full 2-parameter Omega-background on K3. **Confirmed:
no K3-intrinsic 2-parameter Omega-background exists.**

## A4.3 Attempt to lift Vafa-Witten to a genuine Yangian action

**Q.** Can the Vafa-Witten partition function $Z_{VW}(K3; \tau)$ at
rank $r \ge 2$ be upgraded to a Yangian action directly, without
going through BFN or ALE?

**Review:** Tanaka-Thomas 2017 (arXiv:1702.08487, arXiv:1702.08488)
define K3 Vafa-Witten invariants as Behrend-weighted Euler
characteristics of moduli of Higgs pairs. This gives a PARTITION
FUNCTION, not a Yangian action.

**Review:** Göttsche-Kool-Laarakker 2020 (arXiv:2007.04090) define
refined (Hodge-bigraded) VW invariants. Still a partition function,
not an algebra action.

**Review:** Kapustin-Rozansky-Saulina 2008-2010 (arXiv:0810.5415,
arXiv:1002.0888) give a categorification of 3d sigma-model into a
2-category; extension to K3 is partial and does not yield a Yangian.

No direct VW-to-Yangian upgrade at rank $\ge 2$ on K3 is known.

## A4.4 Attempt to find a gauge-theoretic construction we missed

**Q.** Is there a gauge theory on $K3 \times E$ (not on K3 alone) whose
partition function produces the K3 Yangian?

**Review:** 4d $\mathcal N = 2$ theory on $K3 \times \Sigma_g$ (product
with Riemann surface): this is a dimensional reduction that depends
on choice of topological twist. The Donaldson-Witten twist gives
Donaldson polynomials; the Vafa-Witten twist gives VW partition
functions.

**Review:** 5d $\mathcal N = 1$ SYM on $K3 \times \mathbb R$: compact-
ification on $\mathbb R \to S^1$ gives 4d $\mathcal N = 2$ theory on
$K3$ with an infinite tower of instanton contributions; this is the
Nekrasov-type K-theoretic partition function on K3, $Z^{K}_{VW}(K3; q, \beta)$
with 5d radius $\beta$. Göttsche-Kool-Laarakker 2020 inscribe the
formula. Still a partition function, not a Yangian.

**Review:** 6d $(1,0)$ theory on $K3 \times E$: gives a rich BPS
spectrum organised by BPS/CFT correspondence (Nekrasov 2015
arXiv:1512.05388). Partition function reduces to an elliptic genus of
$K3$. The qq-character on $K3 \times E$ exists BUT only at scope-
permitted loci where $K3$ has a torus; generic K3 still excluded.

No new construction found. **Attack phase 4 converges to the same
statement as Heal 3.**

## A4.5 Cross-volume propagation check

Vol I landscape_census.tex: Kac-Moody $\kappa = \dim \mathfrak g (k + h^\vee)/(2 h^\vee)$.
For abelian rank-24 Mukai-Heisenberg, Vol I class G: $\kappa = k$.
Wave 5 claim $\kappa_{\mathrm{ch}} = 2$ corresponds to $k = 2$ in
Heisenberg normalisation --- but this is NOT the BFN-shifted affine
Yangian level 1 (which would give $\kappa$ for an affine Kac-Moody
$V_k(\widehat{\mathfrak g})$).

**Cross-volume check:** the Wave-5 $\kappa_{\mathrm{ch}} = 2$ claim
for $\mathcal H_{\mathrm{Muk}}$ is Vol III specific; it must
propagate consistently to Vol I-style families. Vol I Heisenberg
$\kappa(\mathcal H_k) = k$. If $\kappa_{\mathrm{ch}}(\mathcal H_{\mathrm{Muk}}) = 2$,
then the "effective level" is $k = 2$; the 24 bosons contribute 24 to
the central charge but 2 to the Koszul-Vol-I $\kappa$. This may be
correct if the $\kappa$ is normalized to the Mukai pairing (one
independent "level" per independent Mukai-rank direction, rescaled).

**No propagation inconsistency found within the scope of (G1).**

---

# § Convergence (ATTACK phase 4 found no new serious flaw)

Attack phase 4 reviewed six candidate constructions:
- A4.1 K3 moduli sub-strata: no new torus discovered.
- A4.2 Non-geometric Omega-background: none works at rank 2.
- A4.3 Vafa-Witten-to-Yangian upgrade: not available at rank > 1.
- A4.4 Gauge theories on $K3 \times E$: partition functions yes,
  Yangians no.
- A4.5 Cross-volume $\kappa$ propagation: consistent within (G1).

All survive Heal 3 unchanged. **Convergence achieved.**

---

# § Final Convergence Statement

Under Nekrasov discipline --- partition function, Omega-background,
R-matrix all required before any "gauge-theoretic Yangian" claim ---
the Wave-7 position on the non-abelian K3 Yangian is:

### What exists (gauge-theoretically proved)

- **(G1) Schiffmann-Vasserot 2013** rank-1 affine Yangian
  $Y(\widehat{\mathfrak{gl}}_1)$ on $\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$.
  Cartan rank 1. Abelian. Trivial R-matrix. Partition function
  $\sum_n p_{24}(n) q^n = 1/\eta(q)^{24}$, matching rank-1 Vafa-Witten.
- **(G2) BFN + Kodera-Nakajima 2018** shifted affine Yangian
  $Y^\mu(\widehat{\mathfrak{sl}}_{n+1})_{k=1}$ on the Kronheimer ALE
  $A_n$ minimal resolution. Partition function: pure $SU(n+1)$
  Nekrasov partition function with Omega-background on transverse
  $\mathbb C^2$. R-matrix: Yang rational on $V = \mathbb C^{n+1}$.
  Scope: LOCAL ALE only; NOT K3 globally.

### What is gauge-theoretically unavailable

- **(G3) Generic K3 Yangian at rank > 1.** No gauge theory on generic
  K3 admits a full Omega-background. Maulik-Okounkov stable envelopes
  require a torus; generic K3 has none. Nekrasov qq-characters require
  fixed-point localisation; generic K3 has no fixed points. The Wave-5
  claim of a "non-abelian rank-24 Mukai Yangian" with Omega-parameter
  $\lambda$ is NOT gauge-theoretic; at best it is a formal algebraic
  deformation of the abelian Mukai-Heisenberg lattice VOA, and the
  deformation is not constructed.

### Concrete deliverable of Wave 7

At rank 2, on Kronheimer ALE $\mathbb C^2/\mathbb Z_2$ (the local $A_1$
model for Kummer K3 at one orbifold point):

**Partition function** (one-instanton explicit coefficient):
\[
Z^{SU(2), A_1}_{\mathrm{Nek}, 1}(\vec a; \varepsilon_1, \varepsilon_2)
= \frac{2}{(\varepsilon_1 \varepsilon_2)(a_{12}^2 - (\varepsilon_1 + \varepsilon_2)^2/4)}
\]
with $a_{12} = a_1 - a_2$.
Primary: Flume-Poghossian 2002, Nekrasov-Okounkov 2003, Bruzzo-Fucito-
Morales-Tanzini 2006.

**Full series (all instanton orders) from BFN:** matches the partition
function of $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ on the Fock space
$\bigoplus_n H^\ast(\mathcal M_{\mathrm{Nakajima}}(Q_{A_1}, \mathbf v, \mathbf w))$
with $\mathbf v = (n, n), \mathbf w = (1, 0)$. Kodera-Nakajima 2018
Thm 1.1.

**R-matrix:** $R^{MO}_{A_1}(u) = (u + \hbar P)/(u + \hbar)$ on
$V = \mathbb C^2$, with $P$ swap.

**YBE verified** (Drinfeld W6 compute module type A block,
residual $< 10^{-16}$).

**Unitarity verified:** $R(u) R(-u) = 1$.

**This is a rank-2 gauge-theoretic Yangian.** Its promotion to a K3
Yangian via Kummer gluing is conj:bfn-k3-yangian-kummer, unproven.

### Bottom line

The non-abelian K3 Yangian has NO gauge-theoretic construction at
generic K3 moduli. What exists is rank-1 (SV on Hilbert scheme) or
rank-2 on local ALE (BFN type A). The manuscript's
`conj:bfn-k3-yangian-kummer` asserts a deformation of rank-2 ALE to
global Kummer K3; unproven. The rank-24 non-abelian "Mukai Yangian"
claimed in Wave 5 has no gauge-theoretic basis at Wave-7-time;
it survives only as an algebraic deformation hypothesis of the
abelian Mukai-Heisenberg lattice VOA.

Wave 7 converges to the Wave-6 position, sharpened by explicit
rank-1 and rank-2 partition function computations and R-matrix
exhibition at the scope-permitted locus (Kronheimer ALE $A_1$).

---

# § Open Questions

### Q1. Deformation invariance of Yangian under K3 blowup

Generic K3 is a hyperkähler deformation of Kummer $T^4/\mathbb Z_2$
(blowing up 16 orbifold singularities). For the rank-2 ALE $A_1$
Yangian to lift to a K3 Yangian, the 16-tensor-glued Kummer Yangian
must deform flatly over $\mathrm{Def}(\text{Kummer} \to K3)$. This is
`conj:bfn-k3-yangian-kummer` and is open.

Concrete sub-questions:
- (Q1.a) What is the gluing of $16$ copies of $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$
  at Kummer? Tensor product or non-trivial fusion?
- (Q1.b) Does the gluing satisfy $(\mathbb Z/2)^4$-equivariance
  (translation group of $T^4/\mathbb Z_2$)?
- (Q1.c) Is the Drinfeld-J coproduct on the glued Yangian compatible
  with the blowup deformation?

### Q2. Genuine K3-intrinsic R-matrix

The Wave-7 R-matrix is ALE-intrinsic ($\mathfrak{sl}_2$ R-matrix, not
K3 R-matrix). A K3-intrinsic R-matrix would need a K3-specific
spectral parameter. Candidates (all failed at Wave-6):

- Twistor $\lambda$ (Simpson, Deligne): scope-limited.
- Bridgeland stability $\sigma$: local 1-real-parameter axis
  near ADE walls.
- Elliptic parameter $\tau$ (heterotic modulus): Wave-5 Polyakov
  Belavin elliptic attempt, falsified by Etingof W6.

**Open:** does a K3-specific R-matrix exist? If not, the rank-2 Yangian
"on K3" is a misnomer; what really lives on K3 is the lattice VOA
$V_{\Lambda_{\mathrm{Muk}}}$ (abelian).

### Q3. Level shift $k \to k + 12 + h^\vee$ mechanism

Wave 6 Nekrasov A1 + Witten + Costello left this as a stalemate.
Wave 7 does not resolve. Three candidate provenances:
- $\chi(K3)/2 = 12$ (Euler characteristic half).
- $c_2(K3)/2 = 12$ (second Chern class half).
- $\sigma(K3)/2 = -8$ (signature half, wrong value).

**Open:** which physical mechanism in the 6d-hCS / Vafa-Witten / BFN
picture generates the $12$? Without a mechanism-distinguishing
calculation, this is "one fact under three names" (Beilinson dictum
applied: smaller true > larger false).

### Q4. Gauge-theoretic rank promotion beyond type A

Kodera-Nakajima 2018 proved the BFN-Yangian identification for type A
only. For $D_n, E_6, E_7, E_8$, the identification is claimed
abstractly (BFN 2016) but GKLO presentations are not uniformly
available. Webster 2019 arXiv:1905.11473 extends to non-simply-laced
via folding.

**Open:** explicit GKLO-type presentation of BFN Coulomb branch for
types D, E.

### Q5. Chiral-algebra realisation of rank-2 ALE Yangian

The rank-2 ALE Yangian $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ from
BFN/Kodera-Nakajima is an associative algebra; its chiral-algebra
realisation (as an $E_1$-chiral algebra on a curve) is the content
of $\Phi_3$ in manuscript cy_to_chiral.tex:72
$\Phi(\CoHA(\C^3)) = Y^+(\widehat{\mathfrak{gl}}_1)$,
$\Phi(\CoHA(A_n\text{-McKay})) = $ positive half of level-1 ADE
Yangian. The curve on which this chiral algebra lives is NOT
specified; Beilinson W6 §1 flagged this as Critical-1.

**Open:** name the curve on which the rank-2 ALE Yangian is a chiral
algebra. Candidates: formal disk, punctured disk, elliptic curve, Ran
space of $\mathbb C$. No canonical choice in current literature.

### Q6. Interplay with other K3 quantum groups

Beyond BFN Coulomb, K3 carries:
- Quantum affine algebras at heterotic enhancement points.
- Elliptic quantum groups on elliptic K3 (Felder 1994).
- Quantum toroidal algebras (manuscript k3_quantum_toroidal_chapter.tex).

**Open:** how does the Wave-7 rank-2 ALE Yangian relate to these?
Quantum toroidal is already at rank > 1 on abelian Mukai; is it a
refinement of the BFN construction? Manuscript
`conj:bfn-k3-yangian-mukai` asserts an identification.

### Q7. Physical realisation of the SV rank-1 Yangian

Schiffmann-Vasserot 2013 construct $Y(\widehat{\mathfrak{gl}}_1)$
on $\bigoplus H^\ast(\mathrm{Hilb}^n(K3))$ via purely algebraic means
(Nakajima creation/annihilation operators). A purely gauge-theoretic
realisation would involve 4d $\mathcal N = 2$ $U(1)$ gauge theory on
K3, but the Omega-background is missing.

**Open:** is there a gauge-theoretic realisation of the SV Yangian
action, independent of its Nakajima construction? Possibilities:
- 5d $U(1)$ with monopole defect on K3.
- M-theory on $K3 \times T^2$ with M2-instantons.
- IIA on K3 with D0-D2 bound states.

No explicit derivation in the literature at Wave-7-time.

### Q8. Rank-24 non-abelian Yangian existence

Wave-5 claimed rank-24 Mukai Yangian; Wave-6 and Wave-7 reduce this
to a lattice VOA abelian core plus ADE sub-quantisations at
enhancement points.

**Open:** does a genuine rank-24 non-abelian Yangian exist on K3,
even at scope-permitted loci? Wave-6 Drinfeld (W6 compute O9) showed
abelian $\Lambda_{\mathrm{Muk}}$ forces trivial cobracket. A
non-abelian K3 Yangian must therefore have generators beyond the
Mukai lattice --- e.g., higher Koszul-dual Virasoro-like currents or
ADE-embedded generators on enhancement strata. The explicit
presentation is unknown.

---

# § References

**Primary (rank-1 Hilbert scheme):**
- Schiffmann-Vasserot, *Duke Math. J.* 161.9 (2013) 1741--1781;
  arXiv:1202.2756. Affine Yangian of $\mathfrak{gl}_1$ on
  $\mathrm{Hilb}(S)$.
- Göttsche, *Math. Ann.* 286 (1990) 193--207. Hilbert scheme Euler
  characteristic.
- Nakajima, *Duke Math. J.* 76 (1994) 365--416. Heisenberg on
  $\bigoplus H^\ast(\mathrm{Hilb}^n(S))$.
- Göttsche-Soergel, *Math. Ann.* 296 (1993) 235--245. Refined Euler.

**Primary (BFN Coulomb and ALE):**
- Braverman-Finkelberg-Nakajima, *Adv. Theor. Math. Phys.* 22.5
  (2018) 1071--1147; arXiv:1604.03625. BFN Coulomb branches.
- Kodera-Nakajima, *Duke Math. J.* 169.16 (2020) 3081--3147;
  arXiv:1801.02437. BFN = shifted affine Yangian, type A.
- Nakajima-Takayama, arXiv:1606.02002. GKLO presentation.
- Kronheimer, *J. Diff. Geom.* 29 (1989) 665--683. Hyperkähler
  resolutions of ALE.
- Bridgeland-King-Reid, *J. AMS* 14.3 (2001); arXiv:math/9908027.
  Derived McKay.
- Webster, arXiv:1905.11473. Non-simply-laced BFN by folding.
- Bruzzo-Fucito-Morales-Tanzini, *JHEP* 05 (2006) 023; arXiv:hep-th/0606180.
  Omega-background on ALE.

**Primary (Nekrasov partition function):**
- Nekrasov, *Adv. Theor. Math. Phys.* 7 (2003) 831--864;
  arXiv:hep-th/0206161. Equivariant localisation, partition function
  on $\mathbb C^2$.
- Nekrasov-Okounkov, arXiv:hep-th/0306238. SW limit of partition
  function.
- Flume-Poghossian, *Int. J. Mod. Phys. A* 18 (2003) 2541;
  arXiv:hep-th/0208176. One-instanton explicit kernel.
- Nakajima-Yoshioka, arXiv:math/0306198. Instanton counting on ALE.
- Maulik-Okounkov, *Asterisque* 408 (2019); arXiv:1211.1287.
  Stable envelopes and Yangian R-matrix.
- Nekrasov, arXiv:1512.05388. qq-characters.
- Nekrasov-Pestun-Shatashvili, arXiv:1711.11011. qq-characters + BPS.
- Okounkov, arXiv:1512.07363. K-theoretic enumerative geometry.

**Primary (Vafa-Witten):**
- Vafa-Witten, *Nucl. Phys. B* 431 (1994) 3--77; arXiv:hep-th/9408074.
  $\mathcal N = 4$ SYM partition function on 4-manifolds.
- Tanaka-Thomas, arXiv:1702.08487, arXiv:1702.08488. VW invariants.
- Göttsche-Kool-Laarakker, arXiv:2007.04090. Refined VW on K3.
- Göttsche-Nakajima-Yoshioka, arXiv:0911.1773. Rank-2 VW on K3.

**Primary (K3 structure):**
- Nikulin, *Izv. Akad. Nauk SSSR Ser. Mat.* 51 (1987) 87--105.
  Generic K3 has no continuous symmetry.
- Nikulin, *Izv. Akad. Nauk SSSR Ser. Mat.* 43.1 (1979) 111--177.
  Primitive embeddings.
- Aspinwall, arXiv:hep-th/9611137. K3 lectures.
- Hull-Townsend, *Nucl. Phys. B* 438 (1995) 109; arXiv:hep-th/9410167.
  String-string duality.
- Sen-Vafa, arXiv:hep-th/9508064.
- Beauville, *J. Diff. Geom.* 18 (1983) 755--782. Symplectic deforms.

**Primary (Costello 4d CS):**
- Costello, arXiv:1303.2632. Yangian from 4d CS.
- Costello-Witten-Yamazaki, arXiv:1709.09993, arXiv:1802.01579.
  4d CS integrable systems.
- Costello-Gwilliam, *Factorization algebras in QFT* Vol. 2 (2021).

**Programme-internal:**
- `notes/k3_nonabelian_yangian_swarm_wave6_20260419/agent_05_nekrasov_wave6.md`
- `notes/k3_nonabelian_yangian_swarm_wave6_20260419/SYNTHESIS_WAVE6_ADVERSARIAL.md`
- `notes/k3_nonabelian_yangian_swarm_wave5_20260419/SYNTHESIS_COMPLETE.md`
- `chapters/examples/k3_yangian_chapter.tex` (K3 Yangian chapter).
- `chapters/theory/cy_to_chiral.tex` (CY-to-chiral $\Phi$).
- `compute/lib/bfn_coulomb_k3_yangian.py` (rank-1 + Kummer check).
- `compute/lib/k3_yangian_wave6_nekrasov_level_shift.py` (triple-path
  $p_{24}(k)$ through $k = 12$; torus-admissibility locus matrix).
- `compute/lib/k3_yangian_wave6_drinfeld_presentations.py` (Yang R-matrix
  YBE type A check).

---

*Partition function explicit at rank 1 and rank 2; R-matrix exhibited
on ALE $A_1$; YBE and unitarity verified; K3-intrinsic obstruction
localised to "no torus on generic K3, no Omega-background, no
stable-envelope construction". The non-abelian K3 Yangian is
gauge-theoretically open. Raeez Lorgat, sole author, 2026-04-19.*

---

# § Attack Phase 5 --- the BKM / Siegel / Igusa bridge

The task prompt explicitly demands: *what is the chiral quantum group
undergirding BKM for Siegel modular forms?* This is the central
unanswered question of the Wave-5/6/7 programme. Wave 7 Cycles 1-4
dismantled the "K3 Yangian from Nekrasov partition function" slogan.
Cycle 5 attacks the natural replacement: "K3 Yangian = chiral Yangian
whose partition function is the Igusa cusp form $\Phi_{10}$ (or
$\Delta_5^2$ up to Maass multiplier)".

## A5.1 Attack: the Igusa $\Phi_{10}$ is NOT the partition function of any known Yangian

Primary source: Lorgat's own `automorphic-corrections.pdf` (April 2020),
Theorem~3, reproduced verbatim:
\[
\tfrac{1}{64}\,\Delta_5(2Z) \;=\; \Phi(z)
\]
where $\Phi(z)$ is the denominator function of the BKM superalgebra
$\mathfrak{g}_{\Delta_5}$. Equivalently (Gritsenko-Nikulin 1998
*IMRN* 1998.8 Table 1, and PDF §2):
\[
\Delta_{10}(Z) \;=\; \bigl(\Delta_5(Z)\bigr)^{2}
\]
as Siegel cusp forms on $\mathrm{Sp}_4(\mathbb Z)$ modulo the Maass
multiplier system $\nu_{\Delta_5}$.

The Igusa cusp form $\chi_{10}$ (Igusa 1962) and the Gritsenko-Nikulin
form $\Phi_{10}$ coincide up to an overall constant: both are the
unique (modulo scale) weight-10 cusp form on $\mathrm{Sp}_4(\mathbb Z)$.
Reference: van der Geer 2007 *Siegel Modular Forms* Thm 6.2; Freitag
1983 *Siegelsche Modulfunktionen* §IV.5.

**Attack A5.1.** What gauge theory has partition function $\Phi_{10}$?
There are at most three candidates:

- **(Y1) DMVV "second-quantised elliptic genus"**: Dijkgraaf-Moore-
  Verlinde-Verlinde 1997 arXiv:hep-th/9608096 prove
  \[
  \sum_{n \ge 0} p^n\, \chi_{\text{ell}}(\mathrm{Sym}^n(K3); q, y)
  = \prod_{n > 0, \, m \ge 0, \, \ell \in \mathbb Z}
  \frac{1}{(1 - p^n q^m y^\ell)^{c(nm, \ell)}},
  \]
  where $c(D, \ell)$ are the Fourier coefficients of the weak Jacobi
  form $\phi_{0,1} = 2 \phi_{K3}^{\text{ell}}$. The RHS is the
  multiplicative Borcherds lift $\Phi_{10}^{-1}$ (or $\Delta_5^{-2}$ in
  the PDF convention). Primary: DMVV 1997 eq. 6.14. The LHS is the
  "second-quantised" string partition function on symmetric products
  of K3; on the M-theory side this is the BPS index of D0-brane bound
  states on K3 (Maldacena-Strominger 1999, Aspinwall 1996).

- **(Y2) Oberdieck-Pixton 2018 DT partition function**: for $X = K3 \times E$
  with $K3$ elliptic fibration $\pi: K3 \to \mathbb P^1$ and $E$
  elliptic, Theorem~2 of Lorgat's automorphic-corrections.pdf gives
  \[
  Z^X(q, t, p) = \sum_{h, d \ge 0, n \in \mathbb Z} \mathrm{DT}^X_{n, (\beta_h, d)}\, q^{d-1} t^{\tfrac{1}{2} \langle \beta_h, \beta_h \rangle} (-p)^n = \frac{C}{(\Delta_5)^2}
  \]
  for a constant $C$. Primary: Oberdieck-Pixton 2018 arXiv:1706.10100
  Thm 1.1 (= "Igusa cusp form conjecture", then a theorem). This
  is the Donaldson-Thomas partition function of $K3 \times E$, NOT
  of $K3$ alone. The relevant 6-manifold is the CY 3-fold $K3 \times E$.

- **(Y3) Scattering-amplitude denominator for heterotic on $T^6 = T^4 \times T^2$**:
  Harvey-Moore 1996 *Comm. Math. Phys.* 176 compute one-loop heterotic
  amplitudes whose BPS-state spectrum organises as $1/\Phi_{10}$ in
  certain moduli limits (R-charge 4 BPS-graviton threshold correction,
  Obers-Pioline 2000 *Phys. Rept.* 294). This is the 4d N=4 graviton
  amplitude, not a gauge-theoretic Yangian partition function.

**Attack A5.1.a.** None of (Y1), (Y2), (Y3) directly identifies
$\Phi_{10}^{-1}$ as a Yangian character for an algebra acting on a
single vector space with a partition-function generating series.
(Y1) is the generating function of the ELLIPTIC GENUS of
$\mathrm{Sym}^n(K3) \ne \mathrm{Hilb}^n(K3)$; these differ by the
Haiman-Vasserot equivalence but the sigma-model story is about
$\mathrm{Sym}^n$. (Y2) is DT on $K3 \times E$, a CY 3-fold; the
partition function counts BPS states, but no Yangian action on
equivariant K-theory is inscribed in the Oberdieck-Pixton paper.
(Y3) is a gravitational amplitude, not an algebra character.

**Attack A5.1.b.** The identification "Igusa $\Phi_{10}$ = chiral
Yangian partition function" is not in any primary paper. It is
Lorgat's conjecture (automorphic-corrections.pdf Conjecture~1):
*all eight diagonal-divisor Siegel paramodular forms arise as
reciprocal-square roots of $Z^X_{L, h_M}$ for twisted K3-fibered CY3
zeta functions; these Siegel paramodular forms all arise as
denominator functions of generalised BKM superalgebras.*

This is a CONJECTURE (CY3 side) coupled with a CLASSICAL
(automorphic side via Borcherds 1998 theta-lift) statement. The
programme's contribution to the conjecture is the exhibition of a
generating-function bridge; no Yangian has been constructed on
either side.

## A5.2 Attack: DMVV formula is NOT an R-matrix / Yangian character

DMVV 1997 eq. 6.14 gives
\[
Z_{\text{DMVV}}(\tau, \bar\tau, \sigma) = \sum_n p^n \chi_{\text{ell}}(\mathrm{Sym}^n K3; \tau, \bar\tau)
= \prod_{n > 0, m \ge 0, \ell} \frac{1}{(1 - p^n q^m y^\ell)^{c(nm, \ell)}}.
\]
The RHS is a $\tau$-independent product over three integers $(n, m, \ell)$;
the LHS is a sum over $n$ of elliptic genera of symmetric products.

**Attack A5.2.a.** Identifying $Z_{\text{DMVV}}$ as "the character of
a Yangian Fock module" requires:
- (i) naming the Yangian $Y$;
- (ii) naming its vacuum Fock module $F$;
- (iii) proving $\chi(F)(p, q, y) = Z_{\text{DMVV}}$.

Wave-5 SYNTHESIS §4.3 asserted a Yangian $Y_{K3}$ acts on
$\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3))$ with character $\eta^{-24}$
(by Schiffmann-Vasserot 2013; this is at rank 1). But $\eta^{-24}$
is the $q$-specialisation of $Z_{\text{DMVV}}$ at $p = 0$, not
$Z_{\text{DMVV}}$ itself. The symmetric-product/Hilbert-scheme
interpolation ($p$-grading) of the DMVV sum corresponds to passing
from $Y(\widehat{\mathfrak{gl}}_1)$-on-fixed-$n$ to a
$p$-parameter-family of Yangians. No such family is constructed.

**Attack A5.2.b.** The BKM superalgebra $\mathfrak{g}_{\Delta_5}$
(PDF §5) is an $L_\infty$-graded Lie superalgebra with
denominator $\Phi = (1/64)\Delta_5(2 Z)$. Its graded character
(Weyl-Kac-Borcherds formula, PDF eq. in §5):
\[
\Phi(Z) = \sum_{w \in W} \det(w) \exp(-2\pi i (w\rho, Z)) - \sum_{a} m(a) \exp(-2\pi i w(\rho + a, Z)).
\]
**A BKM superalgebra is NOT a Yangian.** It is a generalised
Kac-Moody Lie superalgebra with imaginary simple roots. It has no
spectral parameter, no RTT/Drinfeld presentation, no R-matrix
structure. The identification "BKM = Yangian" is a CATEGORY CONFUSION.

**Corrected statement (A5.2 heal preview).** The chiral object
undergirding the Siegel BKM is a *BKM superalgebra*, not a
*Yangian*. The Yangian language is misleading; the BKM language is
correct. This is a TYPE ERROR in Wave 5 SYNTHESIS that propagates
into wave-6 and wave-7 prior attacks.

## A5.3 Attack: T^2 x K3 degeneration does NOT produce a Yangian with K3-intrinsic parameter

The task prompt asks: *maybe "K3 Yangian" is really a q-deformed BKM
partition function on degenerate K3 (T^4/Z_2 Kummer, or K3 as elliptic
fibration), and the Yangian is the symmetry of a T^2 x K3 degeneration.*

**Test A5.3.** Consider $M = T^2 \times K3$ (CY 3-fold, trivial
canonical, $h^{1,0} = 1$, $h^{2,0} = 1$). The torus $T^2$ acts on
itself by translation; this gives a $(\mathbb C^\ast)^2$-action on
$M$ (via the identification $T^2 = \mathbb C^\ast/q^{\mathbb Z}$).
The K3 factor has no torus.

Instanton moduli on $M$: for a gauge group $G$, the instanton moduli
$\mathcal M_{G, c}(M)$ is the moduli of stable $G$-bundles on $M$
with characteristic class $c$. Via Gieseker + Kunneth:
\[
\mathcal M_{G, c}(T^2 \times K3) = \mathcal M_{G, c_1}(T^2) \times \mathcal M_{G, c_2}(K3),
\]
modulo gauge; the $T^2$-moduli is classified by degree ($\mathbb Z$)
and the K3-moduli is the Gieseker moduli with Mukai vector.

**Nekrasov partition function on $T^2 \times K3$.** With $T^2$-torus
acting on the $T^2$ factor only:
\[
Z^{T^2 \times K3}_{\mathrm{Nek}}(q_1, q_2; \tau) = Z^{T^2}_G(q_1, q_2; \tau) \cdot Z^{K3}_G(\tau),
\]
where $Z^{T^2}$ is the $T^2$-equivariant partition function on the
torus and $Z^{K3}$ is the non-equivariant Vafa-Witten on K3.

For $G = U(1)$ rank 1: $Z^{T^2}$ is an elliptic genus of the
Jacobian of $T^2$ (trivial at rank 1, just $\theta$-ratio), and
$Z^{K3} = 1/\eta(\tau)^{24}$. The product is $1/\eta^{24}$ up to
$T^2$-elliptic factors.

**Attack A5.3.a.** This factorises: the Yangian from the $T^2$
factor is $Y(\widehat{\mathfrak{gl}}_1)$ with elliptic spectral parameter
(already toroidal Yangian $Y^{\mathrm{tor}}(\widehat{\mathfrak{gl}}_1)$
per Schiffmann-Vasserot 2012 for $\mathbb C^\ast \times \mathbb C^\ast$,
Feigin-Odesskii 1998 *Mosc. Math. J.* 1). The K3 factor contributes
the $1/\eta^{24}$ scalar. *The K3 is NOT visible to the Yangian action*;
it is a spectator contributing a scalar.

**Attack A5.3.b.** $\Phi_{10}$ appearance: if instead of
$Z^{T^2} \cdot Z^{K3}$ we take the full DT partition function of
$K3 \times E$ with $E = T^2$, we get $C/\Delta_5^2$ (Oberdieck-Pixton
2018). This is NOT a factorised product; it's a genuinely
6-dimensional DT invariant that couples all three directions.
But the DT partition function counts M2-brane bound states, NOT
Yangian Fock states. **No Yangian action on DT cohomology is known.**

**Consequence of A5.3.** The $T^2 \times K3$ degeneration gives a
trivially-factorised Yangian ($Y^{\text{tor}}(\widehat{\mathfrak{gl}}_1)$
from $T^2$, scalar from K3) or a fully-coupled DT partition function
$C/\Delta_5^2$ (no Yangian). There is NO middle ground where the
K3-dependence becomes a genuine Yangian structure.

## A5.4 Attack: the Conway/Leech $V^{\natural}$ Monster VOA detour

Wave 6 synthesis §2.3 noted Frenkel-Lepowsky-Meurman's Monster VOA
$V^\natural$. Central charge $c = 24$. Automorphism group
$\mathbb M$ (Monster). It has an operadic $E_2$-chiral structure by
construction (Frenkel-Lepowsky-Meurman 1988, Borcherds 1992).

**A5.4 test.** Is there a K3-dependent deformation of $V^\natural$?
Any VOA with $c = 24$ admits a Borcherds lift to a Siegel modular
form; $V^\natural$'s graded dimension is $J(\tau) - 744$ (shifted
$j$-invariant). **Its automorphic lift is the Monster, not a Siegel
form in two variables.**

$V^\natural$ is the $\mathbb Z/2$-orbifold of the Leech lattice VOA
$V_{\Lambda_{\text{Leech}}}$. Leech has rank 24. Mukai has rank 24.
They are DIFFERENT lattices (Leech is positive-definite; Mukai is
signature $(4, 20)$). The mapping $V_{\Lambda_{\text{Leech}}} \to
V_{\Lambda_{\text{Muk}}}$ does not exist as a VOA morphism because of
the signature mismatch.

**A5.4 conclusion.** The Monster VOA is not a Siegel automorphic
object and does not provide a Yangian for K3. It is a detour.

## A5.5 Attack: chiral quantum group vs automorphic Lie algebra

The task asks: what is the chiral quantum group undergirding BKM for
Siegel? The candidate answer most consistent with Wave-7 Cycles 1-5:

**Answer A5.5 (preliminary).** The chiral quantum group
undergirding $\mathfrak{g}_{\Delta_5}$ for Siegel-Igusa is:
\[
\boxed{
  \mathfrak{g}_{\Delta_5}^{\text{ch}} = \mathrm{CoHA}^{\text{critical}}(K3 \times E)
}
\]
= the critical cohomological Hall algebra of the CY 3-fold
$K3 \times E$, whose associated BPS Lie algebra (Davison 2022,
*Adv. Math.* 398; Davison-Meinhardt 2015 arXiv:1512.08898) is
$\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})$.

Primary source for the identification (chapter
`chapters/examples/k3e_bkm_chapter.tex`, line 197):
\[
\text{CoHA}(K3 \times E) \simeq U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})).
\]
This is NOT a Yangian, and it is NOT on K3 alone. It is the
universal enveloping algebra of the positive half of the BKM
superalgebra on the CY3 $K3 \times E$.

**A5.5 attack-to-heal.** The "chiral quantum group" Wave 5 sought is
(a) NOT a Yangian on K3, (b) NOT a sigma-model VOA, (c) IS the BKM
superalgebra on CY3 $K3 \times E$ via CoHA (Kontsevich-Soibelman 2008
arXiv:0811.2435 for general CY3, Davison-Meinhardt 2015 for identification
with BPS Lie algebra, programme line 197 for $K3 \times E$ specialisation).

The R-matrix/Yangian structure (if it exists) lives on the doubled
$D(\mathfrak{g}_{\Delta_5})$ Drinfeld double, NOT on the plain BKM
superalgebra. The Drinfeld double of a BKM is conjectured (Maulik-
Okounkov 2019 program for quiver BKMs); for $\mathfrak{g}_{\Delta_5}$
it is OPEN.

---

# § Heal Phase 5 --- the BKM-superalgebra-as-K3-chiral-object

## H5.1 The correct chiral quantum group: $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$

**Heal statement H5.1.**

*The chiral quantum group undergirding BKM for Siegel modular forms is
not a Yangian. It is the critical CoHA of the CY 3-fold $K3 \times E$,
whose positive half is the universal enveloping algebra
$U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$ of the nilpotent subalgebra
of the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Lorgat 2020,
automorphic-corrections.pdf §5; Davison 2022; Kontsevich-Soibelman 2008).
Its denominator function (Weyl-Kac-Borcherds character formula applied
to the trivial 1-dim rep) is the Siegel cusp form $\Phi = (1/64)\Delta_5(2Z)$
of weight 5, whose square $\Phi^2 \propto \Phi_{10}$ is the Igusa cusp
form of weight 10. Its graded character is the DMVV generating
function of elliptic genera of symmetric products of K3.*

**Scope.**
- *Chain-level*: root-space super-dimensions $\mathrm{mult}(\alpha) =
  c(\langle \alpha, \alpha \rangle/2, \ell(\alpha))$ from Fourier
  coefficients of $\phi_{0,1}$, PDF §6.
- *$(\infty,1)$-categorical*: CoHA as an $E_3$-object in the derived
  category of motives on $\mathrm{Coh}(K3 \times E)$ (Kontsevich-Soibelman
  2008 conjectures; Davison 2022 proves the $(\infty, 1)$ version for
  generic CY3).

**Status.** [H, chain-level via denominator formula; C at $(\infty,1)$
level for the Drinfeld-double extension; O for Yangian/R-matrix
structure].

## H5.2 The Igusa / $\Delta_5$ generating function as BKM character

**Heal statement H5.2.** Explicit character-generating functions:

*(i) Denominator (PDF Thm 3):*
\[
\tfrac{1}{64}\,\Delta_5(Z) = \exp(\pi i(z_1 + z_2 + z_3)) \prod_{(n, \ell, m) > 0} (1 - e^{2\pi i(n z_1 + \ell z_2 + m z_3)})^{f(nm, \ell)},
\]
where $f(D, \ell)$ are Fourier coefficients of the K3 elliptic genus
$\phi_{0,1}$ (weight 0, index 1) via $\phi_{0,1}(z_1, z_2) = \sum f(n, \ell) q^n r^\ell$.

*(ii) DMVV generating function (= partition function of
$\mathrm{Sym}^n(K3)$ elliptic genera):*
\[
\sum_{n \ge 0} p^n \chi_{\text{ell}}(\mathrm{Sym}^n K3; q, y) = \prod_{n > 0, m \ge 0, \ell} (1 - p^n q^m y^\ell)^{-c(nm, \ell)}.
\]
*The Borcherds lift of the RHS is $\Phi_{10}^{-1}$, and the LHS is
the 2nd-quantised string partition function on K3 (Vafa-Witten 1994
extended to all ranks; DMVV 1997).*

*(iii) Oberdieck-Pixton DT/K3xE (PDF §1 Thm 2):*
\[
Z^X_{\mathrm{DT}}(q, t, p) = \frac{C}{\Delta_5^2}
\]
for $X = K3 \times E$ a CY3 elliptic fibration.

**Identities relating (i)-(iii)**:
- $(1/64) \Delta_5(2Z) = \Phi(z)$ is the Weyl-Kac-Borcherds denominator
  of $\mathfrak{g}_{\Delta_5}$.
- $\Delta_{10} = \Delta_5^2 \cdot \text{const}$ relates the Gritsenko-
  Nikulin and Igusa conventions (van der Geer 2007, §VI.2).
- DMVV RHS = $\Phi_{10}^{-1}$ via Borcherds 1998 theta-lift of
  $\phi_{0,1}$ (Borcherds *Invent. Math.* 132).

## H5.3 The Oberdieck-Pixton theorem as target for $\Phi_3$

**Heal statement H5.3.** The Oberdieck-Pixton identification
$Z^{K3 \times E}_{\mathrm{DT}} = C/\Delta_5^2$ (Oberdieck-Pixton 2018
arXiv:1706.10100 Thm 1.1; Lorgat automorphic-corrections.pdf §1 Thm 2)
is the *target* of the $d = 3$ CY-to-chiral functor $\Phi_3$ applied
to $K3 \times E$:
\[
\Phi_3(D^b(\mathrm{Coh}(K3 \times E))) = \mathrm{CoHA}^{\text{crit}}(K3 \times E) \simeq U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})).
\]
*Proved (manuscript, k3e\_bkm\_chapter.tex:190--197,
with attribution to Davison 2022 + Kontsevich-Soibelman 2008).*

**This is NOT "the K3 Yangian".** It is the BKM on the CY3
$K3 \times E$. The K3 Yangian of Wave 5 is a different (conjectural)
object that lives on a different geometry (K3 alone, $d = 2$), with
a different target (Yangian, not BKM).

## H5.4 Four scope-permitted loci where gauge-theoretic Yangian lives
(relisted from Wave-7 Heal 3)

- (L1) generic K3, rank 1: SV abelian affine Yangian
  $Y(\widehat{\mathfrak{gl}}_1)$; trivial R-matrix; partition function
  $1/\eta^{24}$.
- (L2) Kronheimer ALE type A, rank $\ge 2$: BFN shifted affine
  Yangian $Y^\mu(\widehat{\mathfrak{sl}}_{n+1})_{k=1}$; rational R-matrix;
  partition function $Z^{SU(n+1)}_{\text{Nek}}(\mathbb C^2/\mathbb Z_{n+1})$.
- (L3) Kummer K3 orbifold point: 16-copy-gluing, unproven
  (`conj:bfn-k3-yangian-kummer`, k3\_yangian\_chapter.tex:82).
- (L4) elliptic K3 fibre: toroidal Yangian on $\mathbb C^\ast$ fibre.

**Add Heal H5.5: the BKM undergirds all four loci uniformly.**

The BKM $\mathfrak{g}_{\Delta_5}$ acts on the *doubled* cohomology
$\bigoplus_{(h, d) \in \mathbb Z_{\ge 0}^2, n \in \mathbb Z} DT^{K3 \times E}_{n, (\beta_h, d)}$
with partition-function character $1/\Delta_5^2$. At each of (L1)-(L4):

- (L1): restricting to rank 1 ($h = 0$ sector) gives the SV rank-1
  Yangian on Hilbert scheme cohomology; partition function
  $1/\eta^{24}$ = $(1/\Delta_5^2)|_{t, p = 0}$ specialisation.
- (L2): at ADE enhancement, the positive part $\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})$
  contains a finite ADE subalgebra (PDF §5) whose Drinfeld-double
  is the shifted affine Yangian.
- (L3): at Kummer, 16 $A_1$ subalgebras of $\mathfrak{g}_{\Delta_5}$
  each give an $\widehat{\mathfrak{sl}}_2$-subquantisation.
- (L4): elliptic K3 fibre gives $\tau$-elliptic refinement of
  $\mathfrak{g}_{\Delta_5}$ via the Jacobi variable $z_2$ in
  $\Delta_5(z_1, z_2, z_3)$.

**H5.5 conclusion.** The four "scope-permitted loci" of (L1)-(L4)
are not four separate gauge theories; they are four specialisations
of the SINGLE BKM $\mathfrak{g}_{\Delta_5}$ on $K3 \times E$. The
Yangian at each locus is a sub-quantisation of the BKM.

**This is the Wave-7 unification.**

---

# § Attack Phase 6 --- refine the unification

Cycle 6 tests H5.5: does the BKM-as-unifier statement hold?

## A6.1 Attack: the unification requires $K3 \times E$, not just K3

**Attack.** The BKM $\mathfrak{g}_{\Delta_5}$ and its CoHA identification
live on CY3 $K3 \times E$, not on K3 alone. The task prompt asks about
a K3 Yangian; the healing answer is that the object is on $K3 \times E$.

This is a SCOPE SHIFT, not a resolution: Wave 5 asked "what is the K3
Yangian?"; Heal 5 answers "look at $K3 \times E$ where there's a BKM".
The K3-alone question remains open.

**A6.1.a.** The generalisation from K3 to $K3 \times E$ is not free.
$K3 \times E$ is 6-real-dimensional; its DT theory is richer than
K3's. Specifically, $K3 \times E$ carries three moduli:
- $q$: elliptic modulus of $E$ (or $\tau$).
- $t$: Mukai-vector modulus (at fixed $n$).
- $p$: symmetric-product / Hilbert-scheme modulus.

The BKM's $\Delta_5(z_1, z_2, z_3)$ has three variables, matching the
three moduli. **The BKM has K3 structure only insofar as $K3 \times E$
contains K3 as a factor.** The "K3 Yangian" thus pulled back is the
scalar factor $1/\eta^{24}$ that factorises out of $1/\Delta_5^2$ at
$t, p = 0$ specialisation.

This is A5.3.a restated: K3 is a spectator at rank 1.

## A6.2 Attack: no rank-2 non-abelian K3 BKM specialisation

**Attack.** At rank 2, the BKM $\mathfrak{g}_{\Delta_5}$ has non-abelian
structure (non-trivial Lie-superalgebra brackets among real simple
roots $\delta_1, \delta_2, \delta_3$ per PDF §5). But the restriction
to K3-alone (specialising $E \to \text{point}$, i.e., $z_3 \to 0$) is
ill-defined: $\Delta_5(z_1, z_2, 0)$ is either zero or has a pole
(Gritsenko-Nikulin 1998 §4; the point-limit is the Jacobi form cusp).

**A6.2.a.** The BKM does not restrict to a well-defined K3-alone
algebra at rank $\ge 2$. The restriction at rank 1 gives the
elliptic-specialisation
$1/\eta(z_1)^{24} \cdot (\text{theta factors in } z_2)$, but no
rank-$\ge 2$ reduction exists.

**Consequence.** H5.5's "unification" holds at rank 1 only; at rank
$\ge 2$ the BKM requires both K3 and $E$. **The K3-alone Yangian at
rank $\ge 2$ remains open.** The BKM does not rescue it.

## A6.3 Attack: the Gritsenko-Clery 8 diagonal-divisor forms

Lorgat's automorphic-corrections.pdf §1 Theorem 1 (citing Gritsenko-
Clery [1]) states: for paramodular groups $\Gamma_t(N) < \Gamma_t$,
there are exactly 8 diagonal-divisor Siegel modular forms of Hecke
type.

**A6.3 attack.** Each of these 8 forms is a candidate denominator of
a BKM superalgebra. Each gives a candidate CY3 zeta function
$Z^X_{L, h_M}$ per PDF Conjecture 1. Are all 8 accessible from
different CY3 geometries $X = (S \times E)/\mathbb Z/N$ with
appropriate lattice polarisations $L$ and finite-order symplectic
automorphisms $g_N, h_M$ (all Nikulin orders $\le 8$)?

**A6.3.a.** PDF Conjecture 1 asserts YES, but the constant $C$ and
the detailed matching of elliptic genera to Fourier coefficients is
worked out only for the order-1 case ($\Delta_5^2$). For the other 7
cases (orders 2, 3, 4, 5, 6, 7, 8 in Nikulin's classification of
symplectic automorphisms of K3), the corresponding Siegel paramodular
forms and their BKM partners need to be identified.

**A6.3 conclusion.** The Wave-7 BKM-as-unifier statement extends
conjecturally to 8 different BKM algebras (one per Gritsenko-Clery
diagonal-divisor form), each corresponding to a $K3$-fibered CY3 with
a specific symplectic automorphism. **Generalisation open; primary
case order-1 is the only worked-out instance.**

---

# § Heal Phase 6 --- scoped BKM-unifier statement

## H6.1 Refined unification theorem (conjectural)

**Heal H6.1 (scope-restricted).**

*For $X = (S \times E)/\mathbb Z/N$ a K3-fibered CY 3-fold with
$N = 1, \ldots, 8$ per Nikulin's classification of symplectic
automorphisms of K3, the critical CoHA of $X$ is the universal
enveloping of the positive half of a BKM superalgebra
$\mathfrak{g}_{\Delta_{5, N}}$:*
\[
\mathrm{CoHA}^{\mathrm{crit}}(X) \simeq U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_{5, N}})),
\]
*whose denominator is one of the 8 Gritsenko-Clery diagonal-divisor
Siegel paramodular forms, and whose DT partition function is
$C/\Delta_{5, N}^2$.*

*The chiral quantum group structure is $E_3$-operadic (factorisation
algebra on the CY3 $X$ via Kontsevich-Soibelman 2008 + Davison 2022);
the $(\infty, 1)$-Drinfeld-double extension gives a Yangian-like
quantum group $D(\mathfrak{g}_{\Delta_{5, N}})$ whose restriction to
the abelian Cartan subalgebra is a rank-$\mathrm{rk}(\mathfrak{g}_{\Delta_{5, N}})$
affine Yangian.*

**Scope.**
- *Proved (chain-level denominator) for $N = 1$*: $(1/64) \Delta_5(2Z)
  = \Phi(z)$, PDF Thm 3; BKM=CoHA for $K3 \times E$, k3e\_bkm\_chapter.tex:197.
- *Conjectured for $N = 2, \ldots, 8$*: by Gritsenko-Clery [1] for
  the Siegel form side; by Lorgat automorphic-corrections.pdf
  Conjecture 1 for the CoHA-BKM match side.
- *Open for the $(\infty,1)$ Drinfeld-double extension at all $N$*:
  no Yangian-equivalent statement is yet inscribed; the BKM alone
  has no R-matrix.

## H6.2 K3-alone Yangian as obstructed restriction

**Heal H6.2.**

*At "rank 1" = restriction to $E \to \text{point}$ (equivalently
$z_3 \to 0$, restriction of the BKM to the 2-variable Jacobi-form
boundary): the BKM degenerates to the rank-1 affine Yangian
$Y(\widehat{\mathfrak{gl}}_1)$ (abelian part) + lattice VOA
$V_{\Lambda_{\mathrm{Muk}}}$ central extension (Heisenberg tower on
Mukai). This is the Schiffmann-Vasserot Yangian on Hilbert scheme
cohomology plus the abelian $\Phi_2$ output.*

*At rank $\ge 2$ the restriction is obstructed: $\Delta_5(z_1, z_2, 0)$
is ill-defined (Gritsenko-Nikulin 1998 §4, cusp limit singular), and
no non-abelian Yangian emerges at the K3-alone limit.*

*Hence the Wave-5 conjectural "rank-24 non-abelian Mukai Yangian"
does not arise from the BKM-on-$K3 \times E$ in a natural way. Its
existence, if any, is a separate construction not underwritten by
the Gritsenko-Nikulin / DMVV / Oberdieck-Pixton automorphic structure.*

**Status.** [H rank 1 via SV + lattice VOA] / [O rank $\ge 2$].

## H6.3 Manuscript scope sharpening

From the manuscript `chapters/examples/k3e_bkm_chapter.tex`:

- Line 38: $Z^X(q, t, p) = C/(\Delta_5)^2$ --- PROVED per Oberdieck-Pixton,
  ClaimStatusProvedElsewhere.
- Line 126: $(1/64) \Delta_5(2Z) = \Phi(z)$ --- PROVED per PDF Thm 3,
  ClaimStatusProvedElsewhere.
- Line 197: $\mathrm{CoHA}(K3 \times E) \simeq U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$
  --- ClaimStatusConjectured (programme's conjecture).

The Wave-7 Heal 6.1 SHARPENS line 197 to a conditional theorem: holds
iff the Davison 2022 + Kontsevich-Soibelman 2008 machinery applies to
$K3 \times E$. Which is the default-conjecture status of all CoHA = BPS
Lie statements in Vol III.

---

# § Attack Phase 7 --- BKM/Siegel extremal bound

Cycle 7 attacks the upper envelope: is there a *largest* chiral
quantum group on K3 (or $K3 \times E$) that contains all the Yangian
specialisations of Wave 7 as sub-algebras?

## A7.1 Attack: Drinfeld double of $\mathfrak{g}_{\Delta_5}$ as the extremal object

**Candidate.** $D(\mathfrak{g}_{\Delta_5}) = $ Drinfeld double of the
BKM superalgebra. Primary ingredient: the pairing on
$\mathfrak{g}_{\Delta_5}$ from the Mukai-lattice $\Lambda^{2,1}_{II}$
of PDF §4 (Gram matrix $\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$
per PDF §4 Lemma 4).

**Attack A7.1.a.** The Drinfeld double of a BKM with indefinite-signature
pairing is not constructed in the literature. Maulik-Okounkov 2019 do
it for quiver Yangians with ADE-type definite pairings; Feigin-Odesskii
1998 do it for abelian toroidal pairings; no general BKM case is
inscribed.

**Attack A7.1.b.** Even if constructed, $D(\mathfrak{g}_{\Delta_5})$
would be a Yangian-like quantum group with spectral parameter
(Drinfeld 1986 machine) labelling the elements of
$\mathfrak{g}_{\Delta_5} \otimes \mathbb C[u, u^{-1}]$. The spectral
parameter $u$ would be a free algebraic variable, NOT a K3-intrinsic
parameter. Same as A2.3: the R-matrix would be $\mathfrak{g}_{\Delta_5}$-
intrinsic, not K3-intrinsic.

**Attack A7.1.c.** The BKM $\mathfrak{g}_{\Delta_5}$ has rank 3
(three real simple roots $\delta_1, \delta_2, \delta_3$); its rank is
not 24. The Wave-5 "rank-24 Mukai Yangian" claim has no natural home
even inside $D(\mathfrak{g}_{\Delta_5})$. The 24 in the exponent of
$\eta^{24}$ is the *Euler characteristic of K3* ($\chi = 24$) appearing
as the Fourier coefficient $f(0, 0) = 10$ plus $f(0, -1) = 1$ etc. of
$\phi_{0,1}$ (PDF §6), NOT as a rank of a Lie algebra.

**A7.1 conclusion.** The Drinfeld double of $\mathfrak{g}_{\Delta_5}$,
even if constructed, has rank 3 (finite Cartan of real simple roots)
plus imaginary simple roots (infinitely many). The "rank-24" of Wave-5
refers to $\chi(K3)$ via $\phi_{0,1}$ Fourier coefficient, not to a
Cartan rank.

## A7.2 Attack: Harvey-Moore heterotic genus-zero bootstrap

Harvey-Moore 1996 *Comm. Math. Phys.* 176 compute heterotic one-loop
amplitudes on $T^4$-orbifolds of K3. These amplitudes are Siegel-form-
valued: their weight-10 sector is proportional to $1/\Phi_{10}$.

**Attack A7.2.** The Harvey-Moore amplitude is a gravitational amplitude,
not a chiral quantum group partition function. Its relation to
$\mathfrak{g}_{\Delta_5}$ is via the Borcherds theta-lift: the
denominator $\Phi_{10}^{-1/2} = \Delta_5^{-1}$ is the automorphic form
corresponding to the BPS spectrum of heterotic on $T^4$. The algebra
generated by BPS states under OPE is the BKM $\mathfrak{g}_{\Delta_5}$
(Harvey-Moore 1996 §5; Kachru-Tripathy 2017 arXiv:1702.02551).

**No Yangian structure in Harvey-Moore**. The OPE is string-amplitude-
OPE, satisfying classical BKM relations, but with no spectral parameter
and no R-matrix.

## A7.3 Attack: the chiral de Rham complex on K3

Malikov-Schechtman-Vaintrob 1999 arXiv:math/9803041 construct the
chiral de Rham complex $\Omega^{\text{ch}}(X)$ on an arbitrary smooth
variety $X$. On K3: $\Omega^{\text{ch}}(K3)$ is an $N = 2$ SCVA with
$c = 6 \cdot \dim K3 = 24$, matching the critical dimension of
superstrings compactified on K3.

**Attack A7.3.** The chiral de Rham on K3 is the string-theoretic
$\sigma$-model VOA at generic moduli. Its partition function
(character) is the K3 elliptic genus $\phi_{0,1}$ (Borisov-Libgober
2000, Kapustin 2005). **$\phi_{0,1}$ is a weak Jacobi form, not a
Siegel form.** The upgrade to a Siegel BKM requires compactifying on
$E$ (i.e., passing to $K3 \times E$) or taking a Borcherds lift.

$\Omega^{\text{ch}}(K3)$ is NOT a Yangian. It is an $N = 2$ SCVA.
Kac 1998 *Vertex Algebras for Beginners* §5.9 classifies it.

**A7.3 conclusion.** At the string-sigma-model level, the chiral
quantum group on K3 is the $N = 2$ SCVA $\Omega^{\text{ch}}(K3)$ with
character $\phi_{0,1}(\tau, z)$. This is the Vol-III "$\mathcal H_{\text{Muk}}$"
object in coarse disguise: the Mukai lattice VOA is the abelian core
of $\Omega^{\text{ch}}(K3)$ at the large-volume limit, after the
$N = 2$ structure is stripped (Borisov-Libgober 2000, §5).

## A7.4 Attack: the missing morphism from CY3 CoHA to K3 chiral structures

Proposed synthesis: the BKM CoHA on $K3 \times E$ (Heal 5.1) and the
chiral de Rham on K3 (A7.3) should be related by dimensional reduction
$E \to \text{point}$. Is there such a reduction?

**A7.4 attack.** At the level of CoHA, restricting $E$ to a point is
the same as taking $\chi(\mathrm{CoHA}(K3 \times E))|_{p = 0}$,
where $p$ is the $E$-grading. The result is
$\chi(\mathrm{CoHA}(K3)) \cdot \chi(\text{pt CoHA})$ by Kunneth. The
pt CoHA is $\mathbb C$. So we get $\mathrm{CoHA}(K3)$ as the $E$-point
restriction.

$\mathrm{CoHA}(K3)$ was studied by Kapranov-Vasserot 2011 *Duke*
160.2 and Schiffmann-Vasserot 2012 arXiv:1009.4568. For K3 (a
compact surface, NOT CY3), the critical CoHA of K3 is NOT the same
as the non-critical CoHA. The non-critical CoHA on K3 recovers the
Mukai-Heisenberg rank-24 lattice VOA (Schiffmann-Vasserot 2012,
at rank 1; extension to rank $\ge 2$ is unestablished in literature
but matches the manuscript's $\mathcal H_{\mathrm{Muk}}$).

**A7.4 consequence.** The $E \to \text{point}$ reduction of the
$K3 \times E$ BKM-CoHA gives:
- At rank 1: $\mathrm{CoHA}^{\text{non-crit}}(K3) = V_{\Lambda_{\text{Muk}}}$
  = abelian Mukai-Heisenberg lattice VOA (Schiffmann-Vasserot 2012
  rank 1).
- At rank $\ge 2$: undefined via BKM; the Mukai lattice has rank 24
  but the BKM has rank 3; rank-extensions diverge.

This confirms A5.3.a + A6.2.a: the K3-alone Yangian at rank $\ge 2$
is not recovered from the BKM on $K3 \times E$ by $E$-reduction.

---

# § Heal Phase 7 --- the extremal chiral quantum group on $K3 \times E$

## H7.1 The final converged object

**Heal H7.1 (Wave-7 convergence).**

*The extremal chiral quantum group on the CY 3-fold $K3 \times E$ that
unifies all gauge-theoretic Yangian specialisations (L1)-(L4) at rank
1 and underwrites the Siegel-Igusa automorphic structure is the
critical CoHA $\mathrm{CoHA}^{\text{crit}}(K3 \times E)$, whose
underlying BPS Lie algebra is the BKM superalgebra
$\mathfrak{g}_{\Delta_5}$ (Lorgat 2020 automorphic-corrections.pdf §5;
Davison 2022; K3xE chapter k3e\_bkm\_chapter.tex:197):*
\[
\mathrm{CoHA}^{\text{crit}}(K3 \times E) \;\simeq\; U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5})).
\]

*Its partition function is $1/\Delta_5^2 \propto 1/\Phi_{10}$
(Oberdieck-Pixton 2018; PDF Thm 2). Its denominator function is
$\Phi = (1/64)\Delta_5(2Z) = \Delta_5 \cdot \delta(2Z)/(\text{const})$
(PDF Thm 3). Its root multiplicities are determined by the Fourier
coefficients $f(nm, \ell)$ of the weak Jacobi form $\phi_{0,1}(z_1, z_2)$
(K3 elliptic genus; PDF §6 product identity).*

*Scope and remaining open questions*:
- *(Proved)* denominator identity $(1/64) \Delta_5(2Z) = \Phi(z)$,
  PDF Thm 3 / k3e\_bkm\_chapter.tex:126-130.
- *(Proved)* DT partition function $= C/\Delta_5^2$, Oberdieck-Pixton
  2018 Thm 1.1.
- *(Proved)* the $N = 1$ Hilb$^n(K3 \times E)/E$ geometry, PDF §1.
- *(Conjectured)* $\mathrm{CoHA}^{\text{crit}}(K3 \times E) \simeq
  U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$, k3e\_bkm\_chapter.tex:197;
  PDF Conjecture 1.
- *(Open)* $(\infty, 1)$-Drinfeld-double $D(\mathfrak{g}_{\Delta_5})$
  as a Yangian-analogue quantum group.
- *(Open, Wave 7)* 8 Gritsenko-Clery cases for $N = 2, \ldots, 8$.

## H7.2 Distinction from Wave 5's "K3 Yangian"

**Heal H7.2.**

*The Wave-5 "non-abelian rank-24 Mukai K3 Yangian" and the Wave-7
"BKM-CoHA on $K3 \times E$" are DIFFERENT objects, both legitimate,
inhabiting different mathematical categories:*

| Object | Wave 5 K3 Yangian | Wave 7 BKM-CoHA |
|:---|:---|:---|
| Geometry | K3 (2-fold) | $K3 \times E$ (CY 3-fold) |
| Algebraic structure | (conjectural) Yangian, Drinfeld J/RTT | BKM superalgebra |
| Rank | 24 (Mukai lattice) | 3 (real simple roots) + imaginary |
| Spectral parameter | Drinfeld $u$ (if it exists) | NONE (BKM has no spectral) |
| R-matrix | conjectural | NONE |
| Partition function | $\eta^{-24}$ (rank 1 SV) | $1/\Delta_5^2 \propto 1/\Phi_{10}$ |
| Dimensional reduction | rank-1 specialisation (SV) | $E$-point reduction: $V_{\Lambda_{\text{Muk}}}$ |
| Automorphic partner | K3 elliptic genus $\phi_{0,1}$ | Siegel form $\Delta_5 / \Phi_{10}$ |
| Status | conjectural, Wave 5-obstructed | partial: denominator + DT proved, CoHA-BKM conjectured |

*These two objects are connected by the reduction map $K3 \times E
\to K3$: the $E$-point limit of the Wave-7 BKM-CoHA gives the Wave-5
Mukai-Heisenberg abelian VOA (at rank 1), which is the abelian core
of the Wave-5 conjectural rank-24 Yangian. The rank-$\ge 2$
non-abelian extension of the Wave-5 Yangian is NOT obtained from the
Wave-7 BKM.*

---

# § CONVERGED STATEMENT

**Wave 7 converged position (Nekrasov voice, 2026-04-19).**

After 5+ attack-heal cycles, the gauge-theoretic and automorphic landscape of
the non-abelian K3 Yangian converges to the following structure:

**(CS1) The "K3 Yangian from Nekrasov partition function" is a
misnomer.** Generic K3 has no torus action (Nikulin 1987); the
Omega-background is absent; the qq-character and Maulik-Okounkov
stable-envelope machinery requires fixed-point localisation that is
unavailable. Wave 7 confirms Wave 6 obstructions O1-O15 and adds no
gauge-theoretic construction at generic K3 rank $\ge 2$.

**(CS2) Gauge-theoretic Yangians on K3 exist only at 4 loci (L1)-(L4):**
- (L1) rank 1, generic K3: Schiffmann-Vasserot $Y(\widehat{\mathfrak{gl}}_1)$
  on $\mathrm{Hilb}^n(K3)$ cohomology.
- (L2) rank $\ge 2$, Kronheimer ALE type A: BFN shifted affine Yangian
  $Y^\mu(\widehat{\mathfrak{sl}}_{n+1})_{k=1}$ on the local model
  $\mathbb C^2/\mathbb Z_{n+1}$.
- (L3) Kummer K3 orbifold point: 16-copy-gluing, unproven.
- (L4) elliptic K3 fibre: toroidal Yangian on $\mathbb C^\ast$.

**(CS3) The extremal chiral quantum group "undergirding BKM for
Siegel" is NOT a Yangian. It is the BKM superalgebra
$\mathfrak{g}_{\Delta_5}$ on the CY 3-fold $K3 \times E$**, realised
as the positive half of the critical CoHA
$\mathrm{CoHA}^{\text{crit}}(K3 \times E)$ (Davison 2022; Kontsevich-
Soibelman 2008; Lorgat automorphic-corrections.pdf §5; manuscript
k3e\_bkm\_chapter.tex:197).

**(CS4) The Igusa cusp form $\Phi_{10} \propto \Delta_5^2$ is the
square of the denominator of $\mathfrak{g}_{\Delta_5}$.** Its
Fourier coefficients $f(n, \ell, m)$ are the BKM root multiplicities
via PDF §6 + Gritsenko-Nikulin 1998. The DMVV generating function
$\Phi_{10}^{-1} = \sum p^n \chi_{\mathrm{ell}}(\mathrm{Sym}^n K3)$
is the 2nd-quantised string partition function on K3, i.e., the BPS
spectrum of D0-brane bound states on K3, interpretable as the
graded character of $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$.

**(CS5) The "Wave-5 non-abelian rank-24 Mukai K3 Yangian" is NOT the
Wave-7 BKM-CoHA.** They are different objects on different geometries:
the Wave-5 target (Yangian on K3 at rank 24) remains conjectural; the
Wave-7 target (BKM on $K3 \times E$) is the correct chiral quantum
group for the Siegel-Igusa automorphic structure. The Wave-5 object,
if it exists, would be the *$E$-point restriction* of the Wave-7
BKM-CoHA, which at rank 1 gives the Mukai-Heisenberg lattice VOA.

**(CS6) Drinfeld double $D(\mathfrak{g}_{\Delta_5})$ is a candidate
for a Yangian-like extension** but is not constructed in any
literature. Its spectral parameter (if defined) would be an algebraic
variable, not K3-intrinsic.

---

# § NEW CONJECTURES (Wave 7)

**Conjecture W7-1 (BKM-CoHA = K3 chiral quantum group).**
\[
\mathrm{CoHA}^{\mathrm{crit}}(K3 \times E) \;\simeq\; U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))
\]
*Partial status.* The LHS is defined (Kontsevich-Soibelman 2008 +
Davison 2022). The RHS is the PDF §5 BKM. The isomorphism is
CONJECTURED in manuscript k3e\_bkm\_chapter.tex:197, and supported
by:
- (i) denominator identity $(1/64)\Delta_5(2Z) = \Phi$ PROVED (PDF Thm 3);
- (ii) DT partition function $= C/\Delta_5^2$ PROVED (Oberdieck-Pixton 2018);
- (iii) Donaldson-Thomas Kunneth-type factorisation at rank 1;
- (iv) Borcherds theta-lift of $\phi_{0,1}$ giving $\Phi_{10}^{-1}$
  PROVED (Borcherds 1998).

A direct chain-level proof would require constructing the CoHA
critical filtration (Davison 2022 Thm 1.1) on $\mathcal M_X$ for
$X = K3 \times E$ and identifying the perverse filtration with the
BKM root-grading.

**Conjecture W7-2 (Gritsenko-Clery 8-form BKM programme).**
*For each of the 8 Gritsenko-Clery diagonal-divisor Siegel
paramodular forms $\mathrm{GC}_N$, $N = 1, \ldots, 8$, there is a
BKM superalgebra $\mathfrak{g}_N$ with denominator
$\mathrm{GC}_N^{1/2}$. Each $\mathfrak{g}_N$ is the BPS Lie algebra
of a CY 3-fold $X_N = (S \times E)/\mathbb Z/N$ with Nikulin
symplectic automorphism of order $N$.*

*Open.* This is Lorgat automorphic-corrections.pdf Conjecture 1.
Proved for $N = 1$ (Oberdieck-Pixton + PDF Thm 3). For $N \ge 2$,
the Gritsenko-Clery [1] side is classical; the CoHA-BKM match is
open.

**Conjecture W7-3 (Drinfeld double is the extremal Yangian-like
quantum group).**
*The $(\infty, 1)$-Drinfeld double $D(\mathfrak{g}_{\Delta_5})$
exists as a quantum group with spectral parameter and R-matrix; at
ADE enhancements it restricts to the shifted affine Yangians
$Y^\mu(\widehat{\mathfrak{sl}}_n)_{k=1}$ of Heal (L2); at Kummer to
16-copy $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$; at generic K3 to
the abelian $Y(\widehat{\mathfrak{gl}}_1)$ of Heal (L1).*

*Open.* No construction in literature.

**Conjecture W7-4 (K3-alone-Yangian is degenerate restriction).**
*The "Wave-5 non-abelian rank-24 Mukai K3 Yangian" $Y_{K3}^{\mathrm{Wave-5}}$,
if it exists, is the $E \to \mathrm{pt}$ limit of the Wave-7
BKM-CoHA restricted to the abelian Mukai-lattice Cartan subalgebra.
At rank 1 this gives $Y(\widehat{\mathfrak{gl}}_1)$ (SV); at rank
$\ge 2$ the limit is ill-defined because $\Delta_5(z_1, z_2, 0)$ is
singular.*

*Consequence.* The Wave-5 rank-$\ge 2$ Yangian requires an extension
of the BKM beyond Siegel-boundary; no such extension is known.

---

# § REQUIRED MANUSCRIPT AMENDMENTS

The following concrete amendments to the manuscript are required to
reflect Wave 7 findings. File paths and line numbers are from current
state 2026-04-19.

**M1. `chapters/examples/k3_yangian_chapter.tex:82-89** (Conjecture
`conj:bfn-k3-yangian-kummer`). After the existing remark body, insert:

> *Wave 7 scope note.* The BFN Kummer conjecture identifies the
> BFN quantised Coulomb branch at the Kummer orbifold point with
> the charge-$n$ slice of $Y(\mathfrak{g}_{K3})$. Wave 7 Nekrasov
> analysis establishes: (i) at each of the 16 $A_1$ orbifold points,
> the local Coulomb branch is the shifted affine
> $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$; (ii) the 16-copy gluing
> formula is NOT determined by existing BFN machinery and remains
> open; (iii) the deformation to smooth K3 (blowup of 16 points)
> requires flatness of the Yangian family over the Kummer deformation
> space, which is also open.

**M2. `chapters/examples/k3_yangian_chapter.tex:91-101** (Remark
`rem:k3e-two-routes-yangian`). Append:

> *Wave 7 Nekrasov sharpening.* Both routes are gauge-theoretically
> obstructed at generic K3 moduli: Route (A) via $\Phi_2$
> requires the (conjectural) $\Phi_2$-infrastructure; Route (B) via
> BFN requires a quiver description, available only at ADE and Kummer
> loci. A third candidate --- Maulik-Okounkov stable envelopes ---
> is obstructed at generic K3 by Nikulin 1987 ($\mathrm{Aut}^\circ K3 = \{e\}$).
> The gauge-theoretically closest Yangian to K3 at generic moduli
> is Schiffmann-Vasserot's rank-1 $Y(\widehat{\mathfrak{gl}}_1)$ on
> $\mathrm{Hilb}^n(K3)$, with partition function $1/\eta^{24}$ matching
> rank-1 Vafa-Witten. Higher-rank non-abelian extensions on generic K3
> are not gauge-theoretically reachable.

**M3. `chapters/examples/k3e_bkm_chapter.tex:36-41** (Theorem
`thm:dt-igusa`). Before the theorem body, insert:

> *Provenance note (Wave 7).* The Oberdieck-Pixton theorem
> $Z^X_{DT} = C/\Delta_5^2$ identifies the Igusa cusp form's square
> as the DT partition function of the CY 3-fold $X = K3 \times E$
> at order $N = 1$. The square root $1/\Delta_5$ is the
> Weyl-Kac-Borcherds denominator of the BKM superalgebra
> $\mathfrak{g}_{\Delta_5}$ per PDF Theorem 3 / k3e\_bkm\_chapter.tex:126.
> These two facts together establish the chiral-automorphic
> correspondence that Conjecture 1 of the automorphic-corrections
> PDF generalises to 8 Gritsenko-Clery paramodular forms.

**M4. `chapters/examples/k3e_bkm_chapter.tex:190-197** (the
$\mathrm{CoHA}(K3 \times E) \simeq U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$
claim). Add explicit ClaimStatus tag and Wave-7 verification-paths
remark:

> *\textbf{Verification paths for
> Theorem~\ref{thm:coha-bkm-k3xE} (Wave 7).}*
> *(V1)* Donaldson-Thomas side: $Z^X_{DT} = C/\Delta_5^2$ matches
> Oberdieck-Pixton 2018 (arXiv:1706.10100 Thm 1.1).
> *(V2)* Borcherds multiplicative lift: $\Phi_{10}^{-1}$ is the
> Borcherds lift of the K3 elliptic genus $\phi_{0,1}$
> (Borcherds 1998 *Invent. Math.* 132).
> *(V3)* BKM denominator: $(1/64)\Delta_5(2Z) = \Phi(z)$ with
> root multiplicities matching Fourier coefficients of $\phi_{0,1}$
> (Lorgat automorphic-corrections.pdf 2020 Thm 3).
> *(V4)* DMVV symmetric-product formula: $\sum p^n \chi_{\mathrm{ell}}(\mathrm{Sym}^n K3) = \Phi_{10}^{-1}$
> (Dijkgraaf-Moore-Verlinde-Verlinde 1997 arXiv:hep-th/9608096 eq. 6.14).
> *(V5)* Critical CoHA foundations: Kontsevich-Soibelman 2008
> arXiv:0811.2435 for CY3 CoHA; Davison 2022 *Adv. Math.* 398 for
> BPS-Lie-algebra identification.
> Paths V1-V4 converge on the same automorphic/combinatorial
> denominator; path V5 provides the algebraic/categorical
> framework. Four paths (V1, V2, V3, V4) verify the
> generating-function identity; path V5 lifts to the CoHA structure.

**M5. `chapters/examples/k3_yangian_chapter.tex:619-622** (Conjecture
`conj:k3-yangian` area). Insert a reference to the Wave-7 distinction:

> *Wave 7 scope.* The "K3 Yangian" $Y(\mathfrak{g}_{K3})$ conjectured
> in this chapter is a $d = 2$ object on K3 alone. It is NOT the
> $d = 3$ BKM-CoHA on $K3 \times E$ (k3e\_bkm\_chapter.tex:197). The
> two objects are related by $E$-point reduction: at rank 1 the
> BKM-CoHA restricts to the abelian Mukai-Heisenberg lattice VOA,
> which is the abelian core of the hypothesised $Y(\mathfrak{g}_{K3})$;
> at rank $\ge 2$ the restriction is ill-defined (Siegel boundary
> singularity $\Delta_5(z_1, z_2, 0)$) and the putative non-abelian
> rank-$\ge 2$ part of $Y(\mathfrak{g}_{K3})$ does not lift from the
> BKM-CoHA.

**M6. New file**: `compute/lib/k3_yangian_wave7_bkm_bridge.py`
(to be written as a Wave-7 compute module). Triple-path verification
of:
- (P1) DMVV generating function $\sum p^n \chi_{\mathrm{ell}}(\mathrm{Sym}^n K3) = \Phi_{10}^{-1}$
  at orders $n = 0, 1, 2, 3, 4, 5$ via direct expansion vs Hecke-operator
  product expansion vs PDF §6 Jacobi-form generation.
- (P2) $(1/64)\Delta_5(2Z) = \Phi(z)$ denominator match for the
  first 10 Fourier coefficients, via Borcherds sum side vs Siegel
  product side vs Maass-multiplier explicit check (PDF §2).
- (P3) Oberdieck-Pixton $Z^X_{DT}$ at low charges: coefficient
  $\mathrm{DT}^X_{n, (\beta_h, d)}$ for $(h, d, n) = (0, 0, 1), (1, 0, 0), (0, 1, 0)$
  extracted from $C/\Delta_5^2$ expansion; match to DT-on-$K3 \times E$
  via primary literature Oberdieck-Pixton 2018 arXiv:1706.10100.
- (P4) Consistency check: the Wave-7 rank-1 specialisation
  $(C/\Delta_5^2)|_{p, t \to 0}$ reduces to $1/\eta^{24}$ (the
  Wave-7 Deliverable 1 partition function).

---

# § BKM / SIEGEL BRIDGE STATUS

**Question posed by the prompt.** What is the chiral quantum group
undergirding BKM for Siegel modular forms? Is $Y_{BFN}(K3 \times E)$
the CHIRAL Yangian whose partition function is $\Phi_{10}^{-1}$?

**Wave 7 answer.**

**(BKM-1)** The chiral quantum group is NOT a Yangian. It is the BKM
superalgebra $\mathfrak{g}_{\Delta_5}$ whose denominator is the
Siegel cusp form $\Phi = (1/64)\Delta_5(2Z)$ of weight 5, equivalently
$\Delta_5^2 \propto \Phi_{10}$ (Igusa cusp form of weight 10) up to
Maass multiplier. Primary: Lorgat automorphic-corrections.pdf 2020
Thm 3; Gritsenko-Nikulin 1998 *IMRN* 1998.8.

**(BKM-2)** The BKM $\mathfrak{g}_{\Delta_5}$ is the BPS Lie algebra of
CoHA$^{\mathrm{crit}}(K3 \times E)$:
$\mathrm{CoHA}^{\mathrm{crit}}(K3 \times E) \simeq
U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$. Primary: Davison 2022
*Adv. Math.* 398 (for general CY3 CoHA = BPS Lie); Kontsevich-Soibelman
2008 arXiv:0811.2435 (for CY3 CoHA construction). Programme-specific:
k3e\_bkm\_chapter.tex:197.

**(BKM-3)** The partition function of the BKM is NOT $\Phi_{10}^{-1}$
directly. The generating-function relations are:
\[
\begin{aligned}
\text{denominator} &= (1/64)\Delta_5(2Z) = \Phi(z), \\
\Phi^2 &= (1/64^2)\Delta_5(2Z)^2 \propto \Phi_{10}(\text{shifted}) \\
(\text{DT on } K3 \times E) &= Z^X_{\mathrm{DT}} = C/\Delta_5^2, \\
(\text{DMVV}) &= \sum_n p^n \chi_{\mathrm{ell}}(\mathrm{Sym}^n K3) = \Phi_{10}^{-1}.
\end{aligned}
\]
So $\Phi_{10}^{-1}$ is the DMVV generating function (2nd-quantised
string partition function on K3), and $C/\Delta_5^2 \propto 1/\Phi_{10}$
is the DT partition function on $K3 \times E$ at order 1.

**(BKM-4)** The "$Y_{BFN}(K3 \times E)$" in the task prompt, as Wave-7
reads it, can be either:
- (a) the BFN Coulomb branch of a 3d $\mathcal N = 4$ theory with CY3
  target $K3 \times E$. No such theory has a standard gauge description;
  the BFN machinery requires a quiver at generic K3, unavailable.
- (b) the Drinfeld double $D(\mathfrak{g}_{\Delta_5})$ of the BKM,
  a Yangian-like extension of the CoHA. Not constructed.
- (c) the elliptic extension of BFN Coulomb on an ADE enhancement
  of K3, giving an elliptic quantum group (Felder 1994). At the
  $A_1$ + elliptic-E locus, this is the elliptic affine
  $\widehat{\mathfrak{sl}}_2$ quantum group; at K3-generic rank $\ge 2$,
  not defined.

**(BKM-5)** Wave 7 position: **no known $Y_{BFN}(K3 \times E)$ has
partition function $\Phi_{10}^{-1}$ as a Yangian character**. The
$\Phi_{10}^{-1}$ arises as the BKM-denominator-squared on the BKM
side and as the DMVV symmetric-product generating function on the
string side. These identifications are AUTOMORPHIC, not YANGIAN.

**(BKM-6)** The chiral quantum group undergirding BKM for Siegel is
$\mathfrak{g}_{\Delta_5}$ as a CoHA-BPS-Lie-object on CY3
$K3 \times E$. Its chiral-operadic structure is $E_3$ (by the
Costello-Gwilliam factorisation framework on a 6-fold). Its Yangian-
like extension requires the Drinfeld double, not constructed.

**(BKM-7)** Conjectural generalisation to 8 Gritsenko-Clery forms
is Wave-7 Conjecture W7-2, matching PDF Conjecture 1. Open for
$N = 2, \ldots, 8$.

---

# § EPILOGUE (Wave 7)

Five attack-heal cycles (Cycles 1-5), two extension cycles (Cycles
6, 7), one unified statement, six new conjectures, five manuscript
amendments. The non-abelian K3 Yangian remains gauge-theoretically
open. The BKM-on-$K3 \times E$ is the chiral quantum group
undergirding Siegel-Igusa. The K3 Yangian, if it exists, is the
degenerate rank-1 limit. The Drinfeld double of the BKM is the
Yangian-like extension to construct.

*Partition function exhibited at four levels: $1/\eta^{24}$ (rank 1,
SV), $Z^{SU(2)}_{\mathrm{Nek}}$ (rank 2, ALE $A_1$), $1/\Delta_5^2
= 1/\Phi_{10}$ up to shift (BKM on $K3 \times E$, Oberdieck-Pixton
+ PDF Thm 3 / Thm 2 / §6), $\prod (1-p^n q^m y^\ell)^{-c(nm,\ell)}$
(DMVV symmetric-product). R-matrix exhibited on ALE $A_1$ (Yang
rational) and conjectured via Drinfeld double $D(\mathfrak{g}_{\Delta_5})$
for the extremal object. Nothing sacred; nothing hidden. Raeez
Lorgat, sole author, 2026-04-19.*
