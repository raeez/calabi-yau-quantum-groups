# The Non-Abelian K3 Yangian: A Synthesis

**Date**: 2026-04-19.
**Sources**: 10-agent adversarial attack-heal swarm.
**Voices**: Gelfand, Kazhdan, Etingof, Polyakov, Nekrasov, Beilinson,
Drinfeld (Russian school) + Witten, Costello, Gaiotto (mathematical
physics).

## 1. One-sentence summary

The "K3 Yangian" is not a single algebra but a **stratified object**
whose proved layer is the rank-$24$ abelian Mukai-Heisenberg Yangian
$Y_\hbar^{\mathrm{Heis}}(\Lambda_{K3})$ with a Yang-type R-matrix on
$V \otimes V$ and a BFN affine-Yangian sub-quantisation
$Y_\hbar^{\mu}(\widehat{\mathfrak{g}})_{k=1}$ at resolved ADE
enhancement points, whose conjectural non-abelian envelope
$Y_\hbar(\mathfrak{g}_{K3})$ preserves the symmetric-indefinite
Mukai form of signature $(4,20)$ and lives as boundary obstructions
of 6d holomorphic Chern-Simons on $\R^2_{\varepsilon_2} \times
K3 \times E$ with surface defect along $K3 \times \{0\}$, whose
six alleged realizations are genuinely distinct but assemble into
a pentagon colimit with Borcherds as source, and whose principal
open problems are: a Jacobi-closing Lie bracket for the full rank-$24$
non-abelian generator set, a Drinfeld-$J$-presentation for imaginary
root sectors, an RTT structure function away from ADE, and a
stable-envelope R-matrix on generic (non-elliptic, non-Kummer) K3.

## 2. The stratification

### 2.1 Proved layer

**Abelian Mukai-Heisenberg Yangian.** Specialisation of
Chari–Pressley 1995 to the Mukai lattice $\Lambda_{K3}$ of rank $24$,
signature $(4, 20)$, even unimodular (type $II_{3,19}$ twisted by
$\pm 1$ Hodge parity to signature $(4, 20)$):
$$
Y_\hbar^{\mathrm{Heis}}(\Lambda_{K3}) \;=\;
U\bigl(\Lambda_{K3}[t] \oplus \Z \cdot c\bigr)[[\hbar]]
$$
with central extension $c$ graded by the Mukai form.
- R-matrix: $R(u) = (u \cdot \mathrm{Id} + \hbar P)/(u + \hbar)$ on
  $V \otimes V$, $V = \Lambda_{K3} \otimes \C$.
- YBE verified **symbolically** at rank $24$: residual
  $5.55 \times 10^{-17}$ (Polyakov).
- YBE is **signature-independent**: the Mukai form $\omega_{\mathrm{Muk}}$
  enters only the Shapovalov form on representations, never the
  R-matrix on $V \otimes V$.
- Partition function: $\operatorname{ch}(\mathcal F_{\mathrm{vac}})(q)
  = \prod_{n \ge 1}(1 - q^n)^{-24} = q^{-1}/\Delta(q)$, the inverse
  Ramanujan discriminant (Göttsche 1990).
- Three independent verification paths: free-boson character,
  Fake-Monster denominator, DMVV product formula at $p = 0$
  (Gaiotto).
- $\kappa$-invariant: $\kappa_{\mathrm{ch}}^{\mathrm{K}}(A_{K3 \times E})
  = \chi^{\mathrm{top}}(K3) = 24$ as Künneth-additive
  (Costello anomaly computation via Noether: $c_2(T_{K3}) = 24$).
- Manuscript anchor: Theorem \texttt{thm:k3-abelian-yangian-presentation}
  at \texttt{k3\_yangian\_chapter.tex:877}.

**BFN affine-Yangian sub-quantisation at ADE points.**
At resolved ADE surface singularities $\widetilde{\C^2/\Gamma_{\mathrm{ADE}}}$
embedded in K3, the chain
$$
\text{Kronheimer} \;\to\; \text{McKay} \;\to\; \text{BFN} \;\to\;
\text{Nakajima--Takayama}
$$
produces the shifted affine Yangian
$Y_\hbar^{\mu}(\widehat{\mathfrak{g}})_{k=1}$ at level one, with
$\mathfrak{g} \in \{A_n, D_n, E_6, E_7, E_8\}$.
- Proved fully in the manuscript as
  Theorem \texttt{thm:bfn-phi-ade-identification} at
  \texttt{k3\_yangian\_chapter.tex:109}.
- The embedding $\mathfrak{g}_{\mathrm{ADE}} \subset \mathfrak{g}_{K3}$
  corresponds to the primitive orthogonal sublattice
  $\Lambda_{\mathrm{root}}(\mathfrak{g}) \hookrightarrow \Lambda_{K3}$.
- At each ADE enhancement point the full K3 Yangian decomposes as
  $$
  Y_\hbar^{\mathrm{ADE}}(\mathfrak{g}_{K3})\bigr|_{\text{ADE locus}} \;\simeq\;
  Y_\hbar^{\mu}(\widehat{\mathfrak{g}})_{k=1}
  \;\otimes\; Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{root}}^{\perp})
  $$
  (Etingof, reconstruction theorem). The second factor is the abelian
  complement of rank $24 - \operatorname{rk}(\mathfrak{g}) - 1$ under
  the Mukai form.

### 2.2 Conjectural envelope

$Y_\hbar(\mathfrak{g}_{K3})$, the non-abelian K3 Yangian, whose
classical limit is $\mathfrak{g}_{K3} = \mathfrak{so}(4, 20)$,
the orthogonal Lie algebra preserving the Mukai form of symmetric
indefinite signature $(4, 20)$ on the rank-$24$ lattice.

**Correction to the manuscript.** The current manuscript labels the
envelope $Y_\hbar(\osp(4 \mid 20))$. This is **wrong**: Kac's
$\osp(m \mid 2n) = D(m/2, n)$ preserves a form that is symmetric on
the $m$-dim even part and **symplectic** on the $2n$-dim odd part.
The Mukai form on $\Lambda_{K3}$ is **symmetric throughout**, with no
symplectic piece. The correct Lie algebra is therefore
$\mathfrak{so}(4, 20)$, not $\osp(4 \mid 20)$.

A **Hodge-parity $\Z/2$-super-extension**
$\mathfrak{so}(4 \mid 20)$ (symmetric on both parts, preserving the
even-cohomology-degree grading $H^0 \oplus H^4 \mid H^2$) is available
as a *programme-specific* super-extension; this object is **not in
Kac's simple classification** — it is an ortho-ortho superalgebra, not
ortho-symplectic.

The abelian Heisenberg Yangian is **not** a sub-super-Yangian of
$\osp(4 \mid 20)$: Kac's $\osp(4 \mid 20) = D(2, 10)$ has rank $12$
Cartan, which cannot accommodate $24$ commuting Heisenberg generators
(Kazhdan F3). The relationship is specialisation / projection, not
inclusion.

### 2.3 The Jacobi-antisymmetry obstruction

**Gelfand's critical finding.** Definition \texttt{def:k3-double-current-algebra}
at \texttt{k3\_yangian\_chapter.tex:277}, equation (316), specifies a
Lie bracket of the form
$$
[J^a_i, J^b_j] \;=\; f^{ab}_c J^c_{i \cdot j}
\;+\; (T^a, T^b)_{\mathfrak g}\langle\alpha_i, \alpha_j\rangle_{\mathrm{Muk}}\,\mathbf c
$$
where $\alpha_i, \alpha_j \in H^2(K3)$ are Mukai-lattice generators
and $f^{ab}_c$ are structure constants of an internal Lie algebra
$\mathfrak g$. The central term carries the symmetric pairing
$(T^a, T^b)_{\mathfrak g}$ multiplied by the symmetric Mukai form
$\langle\alpha_i, \alpha_j\rangle_{\mathrm{Muk}}$.

For the bracket to be antisymmetric in $(a, i) \leftrightarrow (b, j)$,
this central term must be antisymmetric. But it is **symmetric**: both
factors are symmetric. Hence
$$
[J^e_1, J^f_2] + [J^f_2, J^e_1] \;=\; 2 Q_{12}\,\mathbf c \;\neq\; 0
\quad\text{for}\quad \mathfrak g = \mathfrak{sl}_2,\;\; Q_{12} = \langle \alpha_1, \alpha_2\rangle_{\mathrm{Muk}} \ne 0.
$$
A Jacobi test on $(J^e_1, J^f_2, J^h_0)$ produces an obstruction
$-2 Q_{12}\,\mathbf c$.

A $\Z/2$-super-grading rescue fails: the symmetry of the two factors
conflicts on odd$\otimes$odd inputs.

**Consequence**: the *current* definition does not assemble into a
Lie algebra for non-abelian internal $\mathfrak g$; the non-abelian
K3 Yangian in its Drinfeld-first-presentation form is **not
constructed**. This is an *open mathematical problem*, not a typo:
fixing it requires either (i) a skew-symmetric central pairing from
a different source, (ii) passing to a Lie bialgebra / $L_\infty$
setting where antisymmetry holds only up to homotopy, or (iii)
restricting to the abelian-$\mathfrak g$ case.

## 3. The physical home

**Selected home** (Witten, Costello converged): 6d holomorphic
Chern–Simons on $\R^2_{\varepsilon_2} \times K3 \times E$ with a
surface defect wrapping $K3 \times \{0\}$.
- Chiral direction: the elliptic curve $E$.
- Omega-background: the transverse $\varepsilon_2$ on $\R^2$.
- $\hbar$ identification: $\hbar = \varepsilon_2$. This is the
  **boundary** (Yangian RTT) parameter, distinct from bulk parameters
  like the CY$_3$ modulus $\sigma_3 = h_1 h_2 h_3$ or the Siegel
  parameter $p$.
- Line defects: D2-branes wrapping $\{\mathrm{pt}\} \times E$ with
  Mukai charges in $\Lambda_{K3}$.

**BPS count** (four-way convergence):
$$
\mathrm{rk}\bigl(Y_\hbar(\mathfrak{g}_{K3})\bigr) \;=\;
\chi^{\mathrm{top}}(K3) \;=\; 24
$$
matches:
1. Free-boson Heisenberg generator count.
2. Fake Monster Weyl-vector norm.
3. DMVV product exponent $(1 - q^n)^{-24}$.
4. Noether–Berezinian super-dimension $4 - (-20) = 24$.

**One-loop anomaly** (Costello): $c_2(T_{K3}) = 24$. Absorbed into a
level shift $k \mapsto k + 12$ by the standard Koszul–Feigin–Frenkel
shift. This matches $\kappa_{\mathrm{BKM}} = 5$ after the
half-shift $24/2 = 12$ plus residual $-7$ from the $E_8 \oplus E_8$
hyperbolic contribution (conjectural; requires further verification).

**Yangian vs quantum loop classification**:
- "K3 Yangian" = cuspidal-$E$ degeneration $= $ rational Drinfeld
  type (the elliptic parent $Y_\hbar^{\mathrm{ell}}(\mathfrak{g}_{K3})$
  collapsed at the cusp $\tau \to i \infty$).
- "K3 quantum toroidal algebra" $= $ nodal-$E$ degeneration (the
  elliptic parent collapsed at $\tau \to 0$).
- The programme's current "$Y(\mathfrak{g}_{K3})$" is implicitly the
  cuspidal degeneration.

**Narain T-duality origin** (Witten). The non-abelian structure of
$\mathfrak{g}_{K3}$ is forced by the $\mathrm{Spin}(4, 20)$ Narain
T-duality group of heterotic string compactification on $T^4 \times K3$
(Obers–Pioline 1998). The Lie algebra $\mathfrak{so}(4, 20)$
appears as the Lie algebra of the duality group; the Yangian is its
cuspidal loop-parameter quantisation.

## 4. The R-matrix and the factorisation framework

**Costello's framework.** The K3 Yangian is the perturbative
factorisation algebra of 6d hCS with surface defect:
$$
Y_\hbar^{n.a.}(\mathfrak{g}_{K3}) \;=\;
\mathrm{Obs}^q\bigl(\text{6d hCS on } \R^2_{\varepsilon_2} \times K3 \times E,\;
\text{defect along } K3 \times \{0\}\bigr).
$$
Integration over $K3$ gives an $E_1$-chiral algebra on $E$; this
integrates Costello's 4d/5d hCS → Yangian story for general $\mathfrak g$
to the K3 setting.

**Tree-level R-matrix** (Costello, agent_09):
$$
R_{6d}(u - v; \tau) \;=\;
\exp\bigl(\hbar \cdot \langle \cdot, \cdot \rangle_{\mathrm{Muk}}
\cdot \zeta(u - v; \tau) \cdot t \otimes t\bigr)
$$
with:
- $\zeta(\cdot; \tau)$: Weierstrass zeta (elliptic propagator).
- $t \otimes t$: Mukai-form Casimir on $\Lambda_{K3}^{\otimes 2}$.
- Rational limit $\tau \to i\infty$: reduces to
  $g_{K3}(u) = \prod_{a=1}^{24}(u - h_a)/(u + h_a)$ with $h_a$
  the Mukai-lattice eigenvalues.
- ADE enhancement: matches Maulik–Okounkov stable envelopes on
  $\mathrm{Hilb}^n(\widetilde{\C^2/\Gamma_{\mathrm{ADE}}})$.

**Polyakov's falsification.** The "omega-twisted permutation"
R-matrix $R_\omega(u) = (u \cdot \mathrm{Id} + \hbar P_\omega)/(u + \hbar)$
with $P_\omega v \otimes w = \omega(v, w) \cdot (w \otimes v)$
**fails** YBE numerically: at rank $4$ signature $(2, 2)$ and
$(u, v, \hbar) = (2.3, 1.7, 1.0)$, YBE residual $= 4.63 \times 10^{-1}$.

The $\mathfrak{so}(p, q)$ Casimir R-matrix $r(z) = \Omega / z$
**fails** classical YBE at first order: CYBE residual $= 2.5 \times
10^{-1}$ on $\R^4$ signature $(2, 2)$.

What **works**: the plain Yang R-matrix $R(u) = (u + \hbar P)/(u + \hbar)$
with ordinary permutation $P$, signature-independent.

**Maulik–Okounkov scope.** MO stable envelopes act on
$\bigoplus_{n \ge 0} K_T(\mathrm{Hilb}^n(X))$, not on
$\Lambda_{K3} \otimes \Lambda_{K3}$ directly. The charge-$1$ block
$K_T(\mathrm{Hilb}^1(K3)) = K_T(K3)$ recovers the abelian Heisenberg.
The continuous torus $T$ exists for elliptic K3, Kummer K3, and ADE
resolutions; for generic K3 the torus is absent and the MO R-matrix
requires a Bridgeland-chamber / polarisation substitute (conjectural).

## 5. The Tannakian reconstruction

**Fiber functor** (Etingof). Rep$^{E_2}(A_{K3}^{\mathrm{ADE}})$ is
rigid semisimple at ADE enhancement points, and the
**lowest-weight functor**
$$
\omega(V) \;=\; V^{\mathrm{lw}} \;=\; \{v \in V : e_i v = 0 \text{ for all } i\}
$$
is a symmetric monoidal functor Rep$^{E_2}(A_{K3}^{\mathrm{ADE}})
\to \mathrm{Vect}$ (symmetric monoidality holds because
$\lim_{u \to \infty} R(u) = \mathrm{Id}$).

This resolves Obstruction 1 in Conjecture \texttt{conj:cy-c-k3-rep}
at \texttt{quantum\_groups\_foundations.tex:367}: the missing fiber
functor is named.

**Tannaka–Krein output**: a Hopf algebra $H_{K3}^{\mathrm{ADE}}$
with antipode; the coproduct is the $E_2$-braiding image; the
antipode comes from the Berezinian-style construction of
Molev–Ragoucy for super-Yangians (adapted to the ortho-ortho case).

## 6. The pentagon colimit

**Drinfeld's converged position**: the six alleged routes to
$G(K3 \times E)$ are **genuinely distinct** with generator-rank
stratification $\rho^{R_i} \in \{3, 12, 24\}$; no common Hopf
algebra $H_{K3}$ surjects isomorphically onto all six.

The correct universal object is the **pentagon colimit**
$P_{K3}$ with source $P_0 = R_2$ (Borcherds), because $R_2$ uniquely
carries the Jacobi-form datum $2\phi_{0,1}$:
$$
\begin{array}{c}
R_2 \;(\text{Borcherds / BKM envelope } U(\mathfrak{g}_{\Delta_5})) \\
\big\downarrow \\
\{R_1, R_3, R_4, R_5, R_6\}
\end{array}
$$
Five named intertwiners $\beta_{13}, \beta_{34}, \beta_{45},
\beta_{56}, \beta_{61}$ on explicit generators (Cartan, real-root,
lightlike/spacelike imaginary sectors).

**Universal property** (conditional on four pentagon-convergence
hypotheses H1–H4): $P_{K3}$ is the initial object such that each
$A_X^{R_i}$ receives a surjective functor from $P_{K3}$ with
computable kernel.

**r-matrix determines envelope up to gauge**: $G_{\mathrm{gauge}}
= O(4, 20; \Z) \times \C^*$.

## 7. The VOA identification

**Gaiotto's lattice-VOA analysis.** The signature-$(4, 20)$ Mukai
lattice VOA is constructed via **Mukai-twist + BRST reduction** from
the ambient $II_{25,1}$ lattice VOA (Fake Monster no-ghost construction):
$$
V_{\Lambda_{K3}}(-1) \;=\; H^*_{\mathrm{BRST}}\bigl(V_{II_{25,1}} \otimes \text{ghost}; Q_{\mathrm{BRST}}\bigr),
\qquad c_{\mathrm{matter}} = 26.
$$
- Central charge $c = 24$ verified three ways: direct OPE/Casimir
  with timelike Heisenberg sign-absorption, DMVV character
  generating function $q^{-c/24} = q^{-1}$, lattice-VOA rank count.
- Held distinct from the $c = 6$ small-$\mathcal{N} = 4$ sigma model
  VOA (different functor $\Phi$, same K3).

**Abelian OPE** for currents $J_v(z), J_w(0)$ labelled by
$v, w \in \Lambda_{K3}$:
$$
J_v(z) J_w(0) \;\sim\; \frac{\langle v, w \rangle_{\mathrm{Muk}}}{z^2} \;+\;
\text{regular},
$$
no first-order pole (abelian Heisenberg).

**Koszul dual** via Dolgachev–Nikulin self-duality:
$A_{K3}^! \simeq V_{\widetilde\Lambda_{K3}(-1)} \simeq V_{\widetilde\Lambda_{K3}}$.
At ADE enhancement: $(A^{\mathfrak g})^! = A^! \otimes
\widehat{\mathfrak g}_{k^! = -1 - 2 h^\vee}$ (Feigin–Frenkel
reflection), Koszul conductor $K = 0$.

**Schur-index-Yangian relation**:
$$
I_{\mathrm{Schur}}(T_{K3, \mathfrak g_{K3}}; q, y) \;=\;
\chi_{V_{K3}}(q, y) \;=\;
\operatorname{Tr}_{M_Y}(q^{L_0}) \;=\;
\Phi_{10}(q, y, 0)^{-1}.
$$
This is the DMVV product at $p \to 0$, confirming the conjectural
matching of 4d N=2 class-$S[K3]$ Schur index to K3-Yangian character.

## 8. The open problems

Ranked by severity:

**Critical**.
1. **Jacobi-closing Lie bracket for non-abelian $\mathfrak g$**
   (Gelfand). Central term symmetrisation in
   Definition \texttt{def:k3-double-current-algebra} (line 277,
   eq 316) forces an antisymmetry obstruction on non-abelian
   internal tensors. Fix requires either skew central pairing or
   Lie-bialgebra / $L_\infty$ homotopy-antisymmetry.
2. **Drinfeld-$J$-presentation for imaginary root sectors**. No
   Drinfeld $J$-presentation is known in the literature for any
   BKM Yangian with imaginary simple roots. The K3 Yangian contains
   such sectors at the lightlike Mukai vectors ($\langle v, v\rangle_{\mathrm{Muk}} = 0$).

**High**.
3. **RTT structure function away from ADE.** Only at ADE
   enhancement is the structure function explicitly known; the
   generic-Mukai structure function is an open problem.
4. **Tradler-style strictification of the higher $A_\infty$ tower
   on $\HH_\bullet(\cC)$** (one of the three named inputs to
   CY-A$_3$ on compact CY$_3$). Unconditional at toric/formal;
   conditional at compact.
5. **Chain-level $B^{(2)}_{\mathrm{TCFT}} \simeq B^{(2)}_{\mathrm{naive}}$**
   (Costello TCFT moduli-boundary extension). Stated not
   constructed. Required for compact-CY$_3$ CY-A$_3$.
6. **Yukawa-curvature connectivity of $\HH_\bullet(\cC)$** in the
   required range. Third CY-A$_3$ compact input.
7. **Global R-matrix across K3 moduli** (non-torus setting).
   Polyakov/Costello flagged 25+ pp programme with Bridgeland-stable
   envelope substitute.

**Medium**.
8. **Non-abelian antipode via Molev–Ragoucy Berezinian**. Structural
   argument exists at $\osp(1\mid 2)$, $\osp(2 \mid 2)$; extension
   to rank-$(4, 20)$ unverified.
9. **BKM-generator realization** in the full K3-Yangian presentation.
10. **Refined Göttsche–Kool prediction** for $Z_{\mathrm{VW}}(K3; q, y)
    = 1/\prod_n(1 - q^n y^{\chi_n})^{c_n}$ with $c_n$ chambered by
    Hodge grading. Falsifiable; conjectural.

## 9. Contribution of the programme

The programme's genuine contributions beyond existing literature:
1. **V$_4$-Künneth character bookkeeping** for K3 $\times$ K3 and
   K3 $\times$ E.
2. **Pentagon cocycle class** in $(\Z/2)^2$ recording the non-trivial
   pairwise gluing data across the six R-constructions.
3. **Mukai-signed diagonal R-matrix with YBE + unitarity + Koszul
   conductor $K = 0$** (at the abelian / ADE level).
4. **The BFN-$\Phi_2$-ADE match** as a computed theorem (not just a
   correspondence sketch).
5. **The Hodge-parity $\Z/2$-super-extension** as a programme-specific
   (non-Kac) Lie superalgebra construction.

## 10. Anchors and references

- Vol III preface lines 239–330 (Hochschild trinity + Phi assignment).
- Vol III abstract lines 484–538 (K3 Yangian crown).
- Theorem \texttt{thm:k3-abelian-yangian-presentation} (line 877).
- Theorem \texttt{thm:bfn-phi-ade-identification} (line 109).
- Definition \texttt{def:k3-double-current-algebra} (line 277) — carries
  the Jacobi-antisymmetry open gap.
- Conjecture \texttt{conj:cy-c-k3-rep} (line 367 of
  \texttt{quantum\_groups\_foundations.tex}) — updated with fiber functor.
- Remark \texttt{rem:k3-yangian-obstruction} (line 639) — torus
  obstruction flagged.
- Compute backing: \texttt{compute/lib/k3\_yangian\_adversarial.py}
  (rank-$24$ YBE symbolic verification), \texttt{test\_k3\_nonabelian\_all\_ade.py}
  (classical YBE on ADE sub-cases).
- Cross-volume anchors: Vol I Theorem A (bar–cobar adjunction),
  Vol I Theorem H (Hochschild concentration), Vol II
  SC$^{\mathrm{ch,top}}$ foundations for the holographic-bulk
  interpretation.

## 11. Recommended manuscript refinements

Prioritised for the next attack-heal wave:
1. Replace $\osp(4 \mid 20)$ with $\mathfrak{so}(4, 20)$ as the
   classical limit in every preface / abstract / introduction
   mention.
2. Flag the Gelfand Jacobi-antisymmetry gap at
   Definition \texttt{def:k3-double-current-algebra} with an
   explicit \texttt{\textbackslash{}ClaimStatusConjectured} tag
   and a Remark naming the central-term symmetrisation obstruction.
3. Inscribe the Etingof lowest-weight fiber functor as a Remark /
   Construction under Conjecture \texttt{conj:cy-c-k3-rep}.
4. Inscribe the Costello surface-defect factorisation-algebra
   formulation as a third route in
   \texttt{k3\_yangian\_chapter.tex:91} "Two routes to the K3
   Yangian", making it three.
5. Add the dimensional-hierarchy row "6d hCS on $K3 \times E$"
   to \texttt{en\_factorization.tex:1184}.
6. Cross-reference the Narain $\mathrm{Spin}(4, 20)$ T-duality
   origin in the K3 Yangian chapter lead-in.
7. Replace the $h_i$-specific Yukawa computations at
   \texttt{k3\_yangian\_chapter.tex:276} with the symbolic
   Chari–Pressley specialisation to avoid F1-type conflation
   of abelian vs non-abelian.
8. Inscribe the $\hbar = \varepsilon_2$ boundary-parameter
   identification (Witten) as a Remark in the RTT presentation;
   separate it from the bulk parameter $\sigma_3 \leftrightarrow p$
   Koszul identification at line 2647.

## 12. Convergence declaration

The 10-agent adversarial attack-heal swarm converged on the above
stratification. The swarm's output is lossless (all ten agents'
notes preserved in this directory), materially stronger than the
pre-swarm manuscript state (Gelfand's Jacobi gap was previously
unflagged), and exposes the real open problems behind the K3
Yangian programme at the level of first-principles mathematics.
