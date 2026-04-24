# Agent 09: Gaiotto--Moore Axis

Scope: spectral networks, class S, BPS categories, and their relation to positive BPS bases.  Owned file only:
`notes/adversarial_bps_positive_geometry_20260424/agent_09_gaiotto_spectral_networks.md`.

No manuscript files were edited.

## Anchor Ledger

- `chapters/theory/quantum_groups_foundations.tex:15` defines the current universal positive-geometry tuple
  \[
  \mathfrak P^{BPS}_\sigma(X)=
  (\Gamma_X,\Gamma^+_{\mathrm{eff},\sigma},\mathcal M^+_{\mathrm{eff},\sigma},
  \phi_W,\Omega_\sigma,\mathfrak D^{KS}_\sigma,\Theta^{BPS}_\sigma).
  \]
- `chapters/theory/quantum_groups_foundations.tex:65` writes the KS factor as
  \[
  \mathbb S_{\ell,\sigma}=
  \prod_{\gamma:Z_\sigma(\gamma)\in \ell}
  \exp\bigl(\Omega_\sigma(\gamma)\operatorname{Li}_2(e_\gamma)\bigr),
  \]
  and `:73` already limits theta-basis theorem status to cluster/toric charts while leaving compact CY3 generality conjectural.
- `chapters/theory/quantum_groups_foundations.tex:80` defines the positive half
  \[
  Y^+_\sigma(X):=H^\bullet_{\mathrm{eq}}
  (\mathcal M^+_{\mathrm{eff},\sigma},\phi_W),
  \]
  with Hall product only when the critical correspondence is constructed.
- `chapters/examples/coha_wall_crossing_platonic.tex:428` gives the motivic quantum-torus bracket
  \[
  [e_\gamma,e_{\gamma'}]_q=
  \bigl({\mathbb L}^{\langle\gamma',\gamma\rangle/2}
  -{\mathbb L}^{-\langle\gamma',\gamma\rangle/2}\bigr)e_{\gamma+\gamma'},
  \]
  while `:441` gives the Euler-specialized classical bracket
  \[
  [e_\gamma,e_{\gamma'}]=
  (-1)^{\chi(\gamma,\gamma')}\chi(\gamma,\gamma')e_{\gamma+\gamma'}.
  \]
- `chapters/examples/coha_wall_crossing_platonic.tex:597` records the exact quantum pentagon
  \[
  \Psi(x_0)\Psi(x_1)=
  \Psi(x_1)\Psi(q^{-1/2}x_0x_1)\Psi(x_0),
  \]
  so motivic wall crossing is not merely the classical BCH logarithm.
- `chapters/examples/coha_wall_crossing_platonic.tex:1228` records the theorem-grade reduced K3xE DT identity
  \[
  Z^{\mathrm{DT,red}}_{K3\times E,\beta}
  =-\frac{C}{\Phi_{10}}=-\frac{C}{\Delta_5^2}.
  \]
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:1573` identifies the class-S parent as
  \(T[A_1,\Sigma_{0,24}]\), with GMN spectral networks computing BPS spectra on the UV curve \(\Sigma\).
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:1648` states the corrected class-S parent theorem:
  \[
  c_{4d}=\frac{107}{6},\qquad a_{4d}=\frac{403}{24},\qquad
  \operatorname{rk}_{\mathbb C}\mathcal B=21,\qquad c_{2d}=-214.
  \]
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:1935` states the necessary two-step composite
  \[
  I_{\mathrm{Schur}}[T[A_1,\Sigma_{0,24}]]
  \xrightarrow{\mathrm{av}_{M_{24}}}\phi^{K3}_{0,1}
  \xrightarrow{\mathrm{Borch}}\Delta_5,
  \]
  and explicitly rejects direct equality between the Schur index and \(1/\Delta_5\).
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:2175` labels the GMN-to-BKM root comparison as conjectural.
- `chapters/examples/k3e_cy3_programme.tex:4104` contains the corrected K3xE class-S shadow with
  \(22\) trinions, \(21\) tubes, \((n_v,n_h)=(63,88)\), \(c_{4d}=107/6\), \(c_{2d}=-214\).
- Neighboring swarm anchors: Agent 01 separates the BPS datum from theta enhancements; Agent 03 makes Drinfeld doubling conditional on sector completion and Hall pairing; Agent 05 fixes strict-sector KS scattering and broken-line positivity; Agent 06 confines toric shuffle bases to toric-degeneration chambers.

## Verdict

The spectral-network interpretation is theorem-grade in known class-S/Hitchin and cluster/toric situations.  It should not be promoted to a universal construction of \(\Theta^{BPS}\) for compact CY3 categories.  For \(K3\times E\), the correct scope is:

1. The reduced DT product \(-C/\Delta_{10}=-C/\Delta_5^2\) is theorem-grade.
2. The class-S parent \(T[A_1,\Sigma_{0,24}]\) is theorem-grade as a four-dimensional theory with corrected central charges.
3. The Schur-to-\(\Delta_5\) route is a two-step M24-average plus Borcherds lift.
4. A direct GMN spectral-network construction of the K3xE BPS positive basis is conjectural.
5. A direct identification of GMN saddle counts with \(\mathfrak g_{\Delta_5}\) imaginary-root multiplicities is conjectural until an explicit spectral-network count is supplied.

## ATTACK/HEAL 1: Universal Spectral-Network Basis

**Attack.**  The phrase "BPS positive basis via spectral networks" is false if read universally.  A GMN spectral network is defined for class-S/Hitchin data: a UV curve \(C\), a branched spectral cover \(\Sigma\to C\), Seiberg--Witten differential sheets \(\lambda_i\), and phase \(\vartheta\).  Its walls are trajectories
\[
\mathcal W_\vartheta(\phi)=
\left\{w\subset C:
(\lambda_i-\lambda_j)(\dot w(t))\in e^{i\vartheta}\mathbb R_{>0}
\right\}.
\]
The general CY3 BPS datum in `quantum_groups_foundations.tex` has a charge lattice, critical stacks, vanishing cycles, and KS scattering, but no UV curve or finite spectral cover.

**Heal.**  State spectral-network positivity as a theorem only in the known GMN/class-S setting and in the adjacent cluster/toric theta-basis setting.  For general compact CY3 categories, including \(K3\times E\), say:
\[
\Theta^{BPS}_{\sigma,\mathrm{SN}}(X)
\quad\text{is conjectural unless \(X\) is presented by a class-S/Hitchin or toric/cluster chart.}
\]
The manuscript should treat spectral networks as one geometric presentation of a KS scattering diagram, not as the definition of the universal BPS positive basis.

## ATTACK/HEAL 2: Phase-Independent Positivity

**Attack.**  A single spectral-network basis independent of phase is not a theorem.  GMN networks jump at critical phases; framed BPS degeneracies and line-operator expansions mutate under wall crossing.  The invariant object is the KS wall-crossing class, not a fixed list of paths.

**Heal.**  Use phase- and chamber-indexed notation:
\[
\Theta^{\mathrm{SN}}_\vartheta(C,\Sigma)
=\left\{F^\vartheta_\wp\right\}_{\wp},
\qquad
F^\vartheta_\wp
=\sum_{\tilde\gamma}
\underline{\Omega}^{\mathrm{fr}}_\vartheta(\wp,\tilde\gamma)X_{\tilde\gamma}.
\]
Across a wall,
\[
F^{\vartheta_+}_\wp
=\mathbb S_{\ell}^{-1}F^{\vartheta_-}_\wp\mathbb S_{\ell}
\]
in the appropriate completed torus or line-operator algebra.  This matches the strict-sector formulation already requested by Agents 01 and 05:
\[
A_V(Z)=
\prod_{\ell\subset V}^{\curvearrowright}
\prod_{Z(\gamma)\in\ell}
\mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}(\gamma)}.
\]
The positive basis is therefore chambered; only the KS transport law is chamber-independent.

## ATTACK/HEAL 3: Motivic Versus Numerical Counts

**Attack.**  GMN spectral-network counts are usually numerical or framed.  They do not automatically construct the motivic CoHA
\[
Y^+_\sigma(X)=H^\bullet_{\mathrm{eq}}
(\mathcal M^+_{\mathrm{eff},\sigma},\phi_W)
\]
or its refined motivic DT classes.  Replacing motivic vanishing-cycle cohomology by Euler-specialized saddle counts loses the \({\mathbb L}^{1/2}\)-quantum-torus structure and can erase signs, grading, and orientation-data dependence.

**Heal.**  Separate three levels:

- Numerical/classical:
  \[
  K_\gamma(X_\eta)
  =X_\eta(1-(-1)^{\langle\gamma,\eta\rangle}X_\gamma)^{
  \Omega^{\mathrm{cl}}(\gamma)\langle\gamma,\eta\rangle}.
  \]
- Motivic/refined:
  \[
  x_\alpha x_\beta
  ={\mathbb L}^{\langle\alpha,\beta\rangle/2}x_{\alpha+\beta},
  \qquad
  U^{\mathrm{mot}}_\gamma
  =\mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}(\gamma)}.
  \]
- CoHA:
  \[
  Y^+=H^\bullet_{\mathrm{eq}}(\mathcal M^{\mathrm{crit}},\phi_W)
  \]
  with Hall convolution.

In class-S examples, spectral networks compute the numerical/framed shadow and guide the wall-crossing operators.  In toric quiver-with-potential examples, the CoHA and refined quantum dilogarithm give theorem-grade motivic content.  For \(K3\times E\), the motivic spectral-network refinement is conjectural.

## ATTACK/HEAL 4: Class-S Parent Versus Chiral Base

**Attack.**  The UV curve \(\Sigma_{0,24}\), the Seiberg--Witten spectral curve, and the chiral curve/base cannot be conflated.  The local anchors explicitly reject using \(\Sigma_{0,24}\), \(X(1)\), or the Seiberg--Witten curve as the chiral factorization base.  A spectral network on \(\Sigma_{0,24}\) computes class-S BPS data, not directly the chiral algebra on the K3 elliptic base.

**Heal.**  Use the three-object distinction:

\[
\Sigma_{0,24}
\quad\text{class-S UV curve,}
\]
\[
\Sigma_{\mathrm{SW}}\to \Sigma_{0,24}
\quad\text{Hitchin spectral cover for GMN networks,}
\]
\[
E^{\mathrm{nod}}_{24}\ \text{or}\ E
\quad\text{chiral/factorization base in the K3/K3xE construction.}
\]

The class-S parent supplies a Schur-sector shadow, central charges, line defects, and BPS categories.  It does not replace the chiral factorization geometry.

## ATTACK/HEAL 5: Direct Schur/GMN Equality With \(\Delta_5\)

**Attack.**  A direct equality
\[
I_{\mathrm{Schur}}[T[A_1,\Sigma_{0,24}]]
=\frac{1}{\Delta_5}
\]
or a direct theorem equating all GMN saddle counts with BKM imaginary-root multiplicities is false at current manuscript status.  The local anchor already gives the obstruction: the class-S central charge is \(c_{2d}=-214\), while \(\Delta_5\) has weight \(5\), so a direct VOA-character equality has the wrong anomaly.

**Heal.**  Keep the two-step route:
\[
I_{\mathrm{Schur}}[T[A_1,\Sigma_{0,24}]](q;\mathbf z)
\xrightarrow{\mathrm{av}_{M_{24}}}
\phi^{K3}_{0,1}(q,y)
\xrightarrow{\mathrm{Borch}}
\Delta_5(\rho,\tau,z),
\]
with
\[
\Delta_5=e^{2\pi i(\rho+\tau+z)}
\prod_{(n,\ell,m)>0}
\left(1-e^{2\pi i(n\rho+\ell z+m\tau)}\right)^{
c(4nm-\ell^2)}.
\]
The theorem-grade statement is the M24-averaged Jacobi-form route and Borcherds lift.  The conjectural statement is:
\[
\Omega^{\mathrm{GMN}}_{\Sigma_{0,24}}(\gamma)
\stackrel{?}{=}
\operatorname{mult}_{\mathfrak g_{\Delta_5}}(\alpha_\gamma)
\quad\text{after M24 diagonal projection and chamber normalization.}
\]
The proof obligation is an explicit saddle/web count at a fixed Coulomb point, including wall-crossing normalization, and a match to the coefficients \(c(D)\) of \(\phi^{K3}_{0,1}\).

## ATTACK/HEAL 6: Strict GMN Network for \(K3\times E\)

**Attack.**  \(K3\times E\) is not automatically a class-S Hitchin system with a UV curve and GMN spectral networks.  The theorem-grade K3xE input is the reduced DT product
\[
Z^{\mathrm{DT,red}}_{K3\times E,\beta}
=-\frac{C}{\Delta_{10}}
=-\frac{C}{\Delta_5^2},
\]
not a spectral-network construction of the full motivic Hall algebra.  The manuscript also insists that \(\kappa_{\mathrm{cat}}(K3\times E)=0\) and that the CoHA/BKM comparison is conditional at algebra level.

**Heal.**  Use this scope:

- The K3xE numerical DT/Borcherds-product shadow is theorem-grade.
- The Hall--BKM positive-half comparison
  \[
  \mathrm{CoHA}(K3\times E)
  \simeq
  U\bigl(Y^+(\mathfrak g_{\Delta_5})\bigr)_{\mathrm{num}}
  \]
  is conditional/conjectural unless the orientation data, motivic lift, Hall pairing, and completion are supplied.
- A "spectral network" for K3xE should be called a class-S shadow or higher-dimensional Weyl/Humbert chamber analogue, not a GMN network, unless an actual \((C,\Sigma,\lambda)\) Hitchin presentation is built.

The clean conjectural bridge is:
\[
\Theta^{\mathrm{SN}}_\vartheta(T[A_1,\Sigma_{0,24}])
\xrightarrow{\mathrm{M24\ diagonal}}
\Theta^{\mathrm{Jac}}_{\phi_{0,1}}
\xrightarrow{\mathrm{Borcherds}}
\Theta^{\mathrm{BKM}}_{\Delta_5}
\dashrightarrow
\Theta^{BPS}_{K3\times E},
\]
where the dashed arrow is not yet a theorem.

## ATTACK/HEAL 7: Class-S Arithmetic Drift

**Attack.**  The local anchors contain arithmetic drift that would corrupt the spectral-network bridge if copied into a theorem:

- `k3_chiral_bialgebra_platonic.tex:1604` says the positive Coulomb dimension is \(23\), but the formula immediately below gives
  \[
  \operatorname{rk}_{\mathbb C}\mathcal B=3g-3+n=21.
  \]
- `k3_chiral_bialgebra_platonic.tex:1727` says \(k_{2d}^{\mathrm{flav}}=-1/2\) per puncture, but the theorem at `:1675` and BLLPR convention at `:2098` give
  \[
  k_{2d}^{\mathrm{flav}}=-\frac{k_{4d}^{\mathrm{flav}}}{2}
  =-\frac{4}{2}=-2.
  \]
- `k3e_cy3_programme.tex:3907` preserves the stale \(c_{4d}=26\), \(c_{2d}=-312\) class-S ansatz.

**Heal.**  Use the corrected class-S arithmetic everywhere:
\[
n_v=22\cdot 0+21\cdot 3=63,\qquad
n_h=22\cdot 4=88,
\]
\[
c_{4d}=\frac{2n_v+n_h}{12}
=\frac{126+88}{12}=\frac{107}{6},
\qquad
a_{4d}=\frac{5n_v+n_h}{24}
=\frac{315+88}{24}=\frac{403}{24},
\]
\[
c_{2d}=-12c_{4d}=-214,\qquad
k_{2d}^{\mathrm{flav}}=-2.
\]
Any insertion connecting GMN networks to the K3/K3xE story should quote these values, not the older \(26,-312\) values.

## Manuscript Insertions Recommended

1. In `chapters/theory/quantum_groups_foundations.tex`, after the KS/scattering component of Definition `def:universal-positive-geometry-grammar`, insert a scope sentence:

   > The notation \(\Theta^{BPS}_\sigma\) denotes a theta-basis enhancement, not part of the minimal BPS datum.  It is theorem-grade in toric quiver, cluster, and class-S/Hitchin charts where broken lines or GMN spectral networks construct the basis; for compact CY3 categories it is conjectural unless an oriented critical atlas, strict-sector KS scattering diagram, and theta construction are supplied.

2. Near `conj:effective-bps-cone-positive-basis`, add the spectral-network theorem/conjecture split:

   > In class-S examples \(T[\mathfrak g,C]\), a GMN spectral network \(\mathcal W_\vartheta(C,\Sigma)\) gives chambered framed-BPS line-operator expansions \(F^\vartheta_\wp\) and their KS mutation law.  This is a theorem in the standard GMN/Hitchin setting.  The use of these expansions as a compact-CY3 BPS positive basis is a conjectural bridge, not a definition.

3. In `chapters/examples/k3_chiral_bialgebra_platonic.tex`, correct the local arithmetic:

   - Replace the "positive Coulomb dimension 23" sentence by \(3g-3+n=21\).
   - Replace \(k_{2d}^{\mathrm{flav}}=-1/2\) per puncture by \(k_{2d}^{\mathrm{flav}}=-2\) per puncture.
   - Keep `thm:k3-GMN-BKM-roots` conjectural and add the proof obligation: explicit GMN saddle/web counts at a fixed Coulomb point must match the coefficients \(c(D)\) of \(\phi_{0,1}^{K3}\) after M24 diagonal projection.

4. In `chapters/examples/k3e_cy3_programme.tex`, remove or quarantine the stale \(c_{4d}=26\), \(c_{2d}=-312\) statement at the older class-S reminder and point to the corrected `rem:k3e-cy3-classs` values \(c_{4d}=107/6\), \(c_{2d}=-214\).

5. In `chapters/examples/coha_wall_crossing_platonic.tex`, any phrase "spectral R-matrix for \(K3\times E\)" should be explicitly scoped as a class-S shadow or higher Weyl/Humbert chamber analogue unless a genuine GMN datum \((C,\Sigma,\lambda)\) is constructed.

## Exact Scope Statement

Theorem-grade:

- GMN spectral networks compute framed BPS wall crossing and line-operator expansions in known class-S/Hitchin cases.
- Cluster/toric broken lines give positive theta bases under standard GHKK/toric hypotheses.
- The reduced \(K3\times E\) DT product is \(-C/\Delta_{10}=-C/\Delta_5^2\).
- The corrected \(T[A_1,\Sigma_{0,24}]\) class-S parent has
  \[
  (n_v,n_h)=(63,88),\quad c_{4d}=107/6,\quad a_{4d}=403/24,\quad
  c_{2d}=-214,\quad \operatorname{rk}_{\mathbb C}\mathcal B=21.
  \]

Conjectural bridge:

- Spectral-network positive bases for compact \(K3\times E\) BPS categories.
- Direct GMN saddle-count identification with \(\mathfrak g_{\Delta_5}\) imaginary roots.
- Motivic/refined spectral-network construction matching the CoHA positive half \(Y^+(K3\times E)\).
- The final identification of the class-S shadow with the Hall--Drinfeld/BKM object attached to \(K3\times E\).

Files changed: this note only.
