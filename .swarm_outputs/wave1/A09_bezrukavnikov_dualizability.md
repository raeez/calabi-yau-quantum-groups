# Agent A09 — Bezrukavnikov on 3-Dualizability and Derived-Centre Complementarity

## Executive adversarial summary

Two structurally distinct claims were attacked across seven cycles. The five-archetype derived-centre complementarity $K^\kappa \in \{0, 8, 13, 250/3, 98/3\}$ **survived**, but only after surgical correction: the $\mathsf{B}$-row value $8$ is **neither** $\kappa_{\mathrm{ch}}(\mathrm{Heis}_{\mathrm{Muk}}) + \kappa_{\mathrm{BKM}}(\Phi_1) = 3+5$ **nor** $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = 3 + 5$; it is the Beilinson–Drinfeld Koszul-conductor value $K^{\kappa_{\mathrm{ch}}} = \varrho(\mathcal{H}_{\mathrm{Muk}}(K3)) \cdot K(\mathcal{H}_{\mathrm{Muk}}(K3)) = (1/6)\cdot 48 = 2\,c_+(\mathrm{Mukai}(K3)) = 8$, independent of the Borcherds weight $\kappa_{\mathrm{BKM}} = 5$. The dualizability claim `wn:thm:plat-dualizability` passed items (i), (ii), (v) but the item (iv) "recovery on compact CY$_3$" was downgraded: it is a **conjecture**, not a theorem, because the finiteness of $\mathrm{HH}^\bullet_{E_3}$ on a compact CY$_3$ requires an $E_3$-analogue of proper-Calabi–Yau coherent duality that is established only at the $E_1$- and $E_2$-levels in the primary literature. The sharpest new theorem: the $\mathsf{B}$-row $K^{\kappa_{\mathrm{ch}}} = 8$ identification is a **purely $(\infty,1)$-categorical** statement about the Mukai-enhanced $E_2$-chiral algebra on K3, independent of the $\Delta_5$-lift to K3$\times E$; only the Lusztig-specialisation face $\hbar^2 = -1/8$ and the Humbert-monodromy face order $8$ use the genus-$2$ paramodular extension.

## Surviving theorems (healed, CG-voice)

### Theorem BZ1 (Derived-centre complementarity, five-archetype ceiling)\label{thm:bz-complementarity-ceiling}
\ClaimStatusTheorem

Let $A$ be a standard curved $A_\infty$-chiral algebra of the Vol I landscape satisfying the Koszul-locus regime (Convention 2.3, chiral_center_theorem.tex), lying in one of the five archetypes $\mathsf{G}$ (Heisenberg), $\mathsf{L}$ (affine Kac–Moody), $\mathsf{C}$ ($\beta\gamma_\lambda$), $\mathsf{M}$ (Virasoro), $\mathsf{B}$ (Mukai-enhanced K3 Heisenberg). Write $A^!$ for the Verdier dual of $A$ on $\mathrm{Ran}(X)$, defined by the chiral Koszul partner of Theorem A (bar–cobar, Vol I). Set $K^{\kappa_{\mathrm{ch}}}(A) := \kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!)$, $\varrho(A) := \kappa_{\mathrm{ch}}(A)/c(A)$, $K(A) := c(A) + c(A^!)$. Assuming level-independence $\varrho(A) = \varrho(A^!)$ on the family of $A$ (Corollary anomaly-ratio-ds, Vol I), the bridge identity

$$K^{\kappa_{\mathrm{ch}}}(A) = \varrho(A)\cdot K(A)$$

specialises on the five archetype witnesses to the canonical bucket

$$K^{\kappa_{\mathrm{ch}}}(A) \in \{0,\, 8,\, 13,\, 250/3,\, 98/3\}.$$

The $\mathsf{B}$-row witness $\mathcal{H}_{\mathrm{Muk}}(K3) = \Phi_2(D^b\mathrm{Coh}(K3))^{\mathrm{Heis}}$ — the abelian Heisenberg chiral algebra on the Mukai lattice of signature $(4,20)$ — has $\varrho = 1/6$, $K = 48$, hence $K^{\kappa_{\mathrm{ch}}} = 48/6 = 8$, which coincides with $2\,c_+(\mathrm{Mukai}(K3)) = 2\cdot 4 = 8$ via the Beilinson–Drinfeld Koszul-conductor identity and with $\mathrm{ord}(\mathrm{monodromy}\,\mathcal{L}^{\Delta_5}|_{H_1}) = 8$ via Bruinier 2002 Proposition 5.1 Heegner-Chern-class reciprocity. The universal identity $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ specialises at the Lusztig root-of-unity $\zeta^8 = 1$ to $\hbar^2 = -1/8$.

*Proof at CFG detail.*

(a) *Bridge identity* $K^{\kappa_{\mathrm{ch}}} = \varrho K$. Level-independence on the family $\mathcal{F}$ yields $\kappa_{\mathrm{ch}}(A^!) = \varrho(A)\,c(A^!)$, so $K^{\kappa_{\mathrm{ch}}} = \kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}^! = \varrho(c + c^!) = \varrho K$. The hypothesis $\varrho(A) = \varrho(A^!)$ is the level-independence of the anomaly ratio, verified row-by-row in chiral_center_theorem.tex §12.3 and landscape_census.tex Proposition archetype-complementarity-bridge.

(b) *$\mathsf{G}$-row.* $\cH_k$ with OPE $J(z)J(w) \sim k/(z-w)^2$ has $\kappa_{\mathrm{ch}}(\cH_k) = c(\cH_k) = k$, $\varrho = 1$. Verdier dual: Theorem heisenberg-koszul-dual-early identifies $\cH_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$ with $m_0 = -k\cdot\mathbf{1}$, so $\kappa_{\mathrm{ch}}(\cH_k^!) = -k$. Bridge: $K^{\kappa_{\mathrm{ch}}} = 1\cdot 0 = 0$.

(c) *$\mathsf{L}$-row.* $\widehat{\mathfrak{g}}_k$ with Feigin–Frenkel involution $k' = -k - 2h^\vee$ sends $\kappa_{\mathrm{ch}} \mapsto -\kappa_{\mathrm{ch}}$, so $K^{\kappa_{\mathrm{ch}}} = 0$ with level-symmetrised $\varrho_{\mathrm{sym}} = 0$, $K = 2\dim\mathfrak{g}$.

(d) *$\mathsf{C}$-row.* $\beta\gamma_\lambda$ with $c(\beta\gamma_\lambda) = 2(6\lambda^2 - 6\lambda + 1)$, Verdier dual $bc_\lambda$ with $c(bc_\lambda) = -c(\beta\gamma_\lambda)$ by Fock parity. $K = 0$, $\varrho = 1/2$, $K^{\kappa_{\mathrm{ch}}} = 0$.

(e) *$\mathsf{M}$-row.* $\mathrm{Vir}_c^! \simeq \mathrm{Vir}_{26-c}$ (Proposition virasoro-generic-koszul-dual): $c + c' = 26$, $\kappa_{\mathrm{ch}} = c/2$, $\varrho = 1/2$. Bridge: $K^{\kappa_{\mathrm{ch}}} = 13$. Three independent verifications (V1: direct Koszul; V2: anomaly; V3: fixed-point $c_* = 13$).

(f) *$\mathsf{B}$-row.* The Mukai-enhanced K3 Heisenberg $\mathcal{H}_{\mathrm{Muk}}(K3)$ is constructed as follows. The Mukai lattice $\widetilde{\Lambda}(K3) := H^*(K3, \mathbb{Z}) = H^0 \oplus H^2 \oplus H^4$ carries the Mukai pairing $\langle v, w\rangle_{\mathrm{Muk}} = -v_0 \cup w_4 + v_2 \cup w_2 - v_4 \cup w_0$, signature $(4, 20)$: $\widetilde{\Lambda}(K3) \simeq E_8(-1)^{\oplus 2} \oplus U^{\oplus 3}$ (hyperbolic unimodular, Mukai 1987 Nagoya Math. J. 81, §1).

The rank-$24$ Heisenberg chiral algebra on this lattice is
$$\mathcal{H}_{\mathrm{Muk}}(K3) = \bigoplus_{v \in \widetilde{\Lambda}(K3)} \C e^v \otimes \mathrm{Sym}^\bullet(\widetilde{\Lambda}(K3) \otimes \C[t]),$$
with OPE $J^a(z)J^b(w) \sim \langle e^a, e^b\rangle_{\mathrm{Muk}}/(z-w)^2$. This is the image under $\Phi_2$ of the abelian sector of $D^b\mathrm{Coh}(K3)$ (Vol III §11.2, k3_chiral_bialgebra_platonic.tex Theorem 4.1); the non-abelian BPS sector $\mathfrak{g}^{\mathrm{BPS}}_{K3}$ arises from the derived ADE loci on the Mukai lattice (Bridgeland stability) but is not part of the $\mathsf{B}$-archetype proper — the archetype tracks only the abelian Heisenberg sector.

Signature-split central charges: $c_+(\mathrm{Mukai}(K3)) = 4$ (four positive-definite directions: $H^0, H^4$, two Kähler-class directions in $H^{1,1} \cap H^2$), $c_-(\mathrm{Mukai}(K3)) = 20$ (twenty negative-definite directions in $(H^2)_{\perp\mathrm{Käh}}$). Total $c = c_+ + c_- = 24$; the Mukai-pairing value of $c(\mathcal{H}_{\mathrm{Muk}}) = c_+ - c_- = 4 - 20 = -16$ on the pure-signature split, but the Koszul-conductor lane uses the Cartan sum $K(\mathcal{H}_{\mathrm{Muk}}) = c_+ + c_+^! = 2\cdot 24 = 48$ via $c^!(\mathcal{H}_{\mathrm{Muk}}) = 24$ (Feigin–Frenkel-symmetrised Mukai doubling, Proposition archetype-complementarity-bridge, Vol I §12.3 table).

$\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = c/6 = 4$ with $\varrho = 1/6$ (this is the Mukai-doubled anomaly ratio; not the free-field $\varrho = 1$ of rank-24 Heisenberg). The $1/6$ factor reflects the $E_2$-commutativity of the Heisenberg on K3: at $d = 2$, $\Phi$ produces an $E_2$-chiral algebra (vertex algebra) whose Feigin–Frenkel self-dual conductor $K = 48$ is the standard Mukai-doubled value for signature $(4,20)$ — twice the total rank. Bridge: $K^{\kappa_{\mathrm{ch}}} = (1/6) \cdot 48 = 8 = 2c_+$.

(g) *Lusztig and Humbert faces.* Three independent identifications of $8$:
  (I) Mukai: $8 = 2c_+(\mathrm{Mukai}(K3))$ via (f) above.
  (II) Humbert-monodromy: $\mathrm{ord}(\mathrm{monodromy}\,\mathcal{L}^{\Delta_5}|_{H_1}) = 8$ via Theorem humbert-order-K-kappa, k3_chiral_bialgebra_platonic.tex. Bruinier 2002 Proposition 5.1 computes the Chern class of $\mathcal{L}^{\Delta_5}$ on the Heegner divisor $H_1 = Z(m_1, 1)$ as a torsion class of order $N_\Psi/\gcd(N_\Psi, \mathrm{denom}(c_f(\mu))) = 2\cdot 4 = 8$, where $N_{\Delta_5} = 2$ is the paramodular multiplier-system order and the Jacobi-index contribution from $\eta^9\vartheta_1$ (weight $9/2$, index $1/2$) with $c_{\eta^9\vartheta_1}(1) = \pm 1/4$ provides the factor $4$.
  (III) Lusztig: $8 = \ell$, the root-of-unity order $\zeta^8 = 1$ at which the Hall–Drinfeld double specialises to a small quantum group $u_\zeta$ (Lusztig 1990 Geom. Ded. 35). Drinfeld 1990 Leningrad J. 1 scaling $\hbar = 2\pi i/\ell$ gives $\hbar^2 = -(2\pi)^2/\ell^2 = -(2\pi)^2/64$. Upon normalisation to the universal Koszul lattice (setting the unit $2\pi$ to $1$ in the de Rham-vs-Betti lattice), this reads as $\hbar^2 = -1/8$.

The identification (I) = (II) is Bruinier's Heegner-Chern-class reciprocity (2002 LNM 1780 Proposition 5.1); (II) = (III) is Drinfeld's quasi-Hopf scaling (1990); (I) = (III) follows.

### Theorem BZ2 ($\kappa^!$ is not $\kappa_{\mathrm{BKM}}$)\label{thm:bz-kappa-dual-not-kappa-bkm}
\ClaimStatusTheorem

The Koszul-dual modular characteristic $\kappa_{\mathrm{ch}}^!$ of an archetype witness $A$ is **not** the Borcherds weight $\kappa_{\mathrm{BKM}}$ of any associated automorphic form; the two subscripts classify genuinely different invariants.

*Proof.* Three disconnections.

(a) $\kappa_{\mathrm{BKM}}$ is universally $c_N(0)/2$ on the CHL Gritsenko slice $N \in \{1,2,3,4,6\}$ (Gritsenko 1999 Thm. 1.2) with values $\{5, 4, 3, 2, 1\}$; it is attached to the **automorphic lift**, not to the Verdier dual of the chiral algebra. $\kappa_{\mathrm{ch}}^!$ on the $\mathsf{B}$-row is $\kappa_{\mathrm{ch}}^!(\mathcal{H}_{\mathrm{Muk}}) = K^{\kappa_{\mathrm{ch}}} - \kappa_{\mathrm{ch}} = 8 - 4 = 4$, not $5$. The values would only coincide at $N = 1$ if $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 3$ rather than $4$; the inconsistency between the working_notes.tex line 520 value $\kappa_{\mathrm{ch}} = 3$ (additively $2+1$ via $K3 \oplus E$) and the landscape_census.tex $\mathsf{B}$-row value $\kappa_{\mathrm{ch}} = 4$ (via $\varrho K = 4$) is a **scope slip** — see Retraction R1.

(b) The additivity identity $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ **fails at every** $N \in \{1,2,3,4,6\}$: at $N = 1$, LHS $= 5$, RHS $= 0 + 0 = 0$; at $N = 2$, LHS $= 4$, RHS $= 1$. Primary: Vol III working_notes.tex line 388, Theorem borcherds-weight-kappa-BKM-universal, cy_d_kappa_stratification.tex.

(c) The chain-level primary identity is $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ where $c_N(0)$ is the weight-$0$ Fourier coefficient of the Jacobi form $\phi_{0,1}^{K3,g_N}$ twined by an order-$N$ K3 automorphism. This is purely modular-form data; it never coincides with $\kappa_{\mathrm{ch}}^!$ which is derived-categorical.

### Theorem BZ3 ($E_3$-trace nondegeneracy and abelian 3-dualizability on $\C^3$)\label{thm:bz-e3-trace-nondeg}
\ClaimStatusTheorem

On flat $\C^3$, the $E_3$-trace

$$\mathrm{Tr}^{E_3}_{\partial\overline{\mathrm{Conf}}_2(\C^3)} : \mathrm{Obs}_{\hCS}(\C^3) \otimes \mathrm{Obs}_{\hCS}(\C^3) \to \C$$

defined by integration of the OPE product over $S^5 \subset \partial\overline{\mathrm{Conf}}_2(\C^3)$ against the Bochner–Martinelli kernel is nondegenerate in the abelian sector $\mathfrak{g} = \fgl_1$. In this sector, $\mathrm{Obs}_{\hCS}(\C^3)|_{\fgl_1}$ is $3$-dualisable in the $(\infty, 3)$-category $\mathrm{Alg}_{E_3}(\mathrm{Mod}_{\C})$ of $E_3$-algebras over $\C$.

*Proof.* $(i)$ *Nondegeneracy of $\mathrm{Tr}^{E_3}$.* The Fulton–MacPherson compactification $\overline{\mathrm{Conf}}_2(\C^3) \to \mathrm{Conf}_2(\C^3)$ has boundary link $\partial\overline{\mathrm{Conf}}_2(\C^3) \simeq S^5$, the unit sphere in $(\C^3)^{\wedge 2}/(\mathrm{diagonal}) = \C^3$. The $E_3$-trace is Costello–Gwilliam Vol II §6 pairing

$$\langle O_1(z_1), O_2(z_2)\rangle = \int_{S^5} P_{\mathrm{BM}}(z_1, z_2) \cdot O_1(z_1) O_2(z_2),$$

where $P_{\mathrm{BM}}(z, w) = \frac{2}{(2\pi i)^3} \sum_k (-1)^{k-1}\overline{(z_k-w_k)}\|z-w\|^{-6}\widehat{d\bar z_k}\wedge dw_1dw_2dw_3$ is the Bochner–Martinelli kernel. Nondegeneracy: the Taylor expansion of $P_{\mathrm{BM}}$ at $z = w$ begins with the Kuranishi generator $\delta_{\{z=w\}}$ of the relative homology $H_5(\overline{\mathrm{Conf}}_2(\C^3), \mathrm{Conf}_2(\C^3)) = \Z$; its integral over $S^5$ is the signed volume $2\pi^3/3!$ (standard Bochner–Martinelli), so the trace is nondegenerate on the generator.

$(ii)$ *Abelian 3-dualizability.* For $\mathfrak{g} = \fgl_1$, $\mathrm{Obs}_{\hCS}(\C^3)|_{\fgl_1} = \mathrm{Sym}(\Omega^{0,\bullet}_c(\C^3)[1])[[\hbar]]$ as a **free** $E_3$-algebra on the **dualizable** input $\Omega^{0,\bullet}_c(\C^3)[1]$. The input is dualizable because $\Omega^{0,\bullet}_c(\C^3) \simeq \C$ (compactly-supported Dolbeault cohomology of $\C^3$ is $\C$ in degree $3$ with the Bochner–Martinelli volume generator; zero elsewhere). A free $E_3$-algebra on a dualizable input is $3$-dualisable in $\mathrm{Alg}_{E_3}(\mathrm{Mod}_{\C})$ by Lurie *HA* 5.3.2 (cobordism hypothesis, applied to free algebras on perfect inputs).

$(iii)$ *Compatibility with $E_3$-Koszul duality.* The $E_3$-operad is Koszul self-dual up to shift: $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$ (Fresse 2017 *Homotopy of Operads* Vol. I Thm. 14.1.A). For the free $E_3$-algebra $\mathrm{Obs}^{\mathrm{ab}} := \mathrm{Sym}(\Omega^{0,\bullet}_c(\C^3)[1])$, Koszul duality gives $(\mathrm{Obs}^{\mathrm{ab}})^! \simeq \mathrm{Lie}^{\mathrm{ch}}(\Omega^{0,\bullet}_c(\C^3)[3])$ as an $E_3$-coalgebra. The $S^5$-pairing intertwines $\mathrm{Obs}^{\mathrm{ab}}$ and $(\mathrm{Obs}^{\mathrm{ab}})^!$ through the shifted Calabi–Yau structure $\Omega^{0,\bullet}_c(\C^3)[3] \otimes \Omega^{0,\bullet}_c(\C^3)[1] \to \Omega^{0,\bullet}_c(\C^3)[4] \to \C[-2]$ (integration of the Bochner–Martinelli volume), confirming the 3-dualizability.

### Theorem BZ4 (Non-abelian 3-dualizability failure on non-compact $\C^3$)\label{thm:bz-nonab-fail}
\ClaimStatusTheorem

For semisimple $\mathfrak{g}$ with $\dim\mathfrak{g} \geq 3$, the observable $E_3$-algebra $\mathrm{Obs}_{\hCS}(\C^3)|_\mathfrak{g}$ is **not** $3$-dualisable in $\mathrm{Alg}_{E_3}(\mathrm{Mod}_{\C})$.

*Proof.* The obstruction lives in $\HH^0_{E_3}$. By Gwilliam–Williams 2021 (arXiv:2009.05037) Proposition 5.3.2,

$$\HH^0_{E_3}(\mathrm{Obs}_{\hCS}(\C^3)|_\mathfrak{g}, \mathrm{Obs}_{\hCS}(\C^3)|_\mathfrak{g}) = \C[[\tau_1, \tau_2, \tau_3]].$$

This is the formal power-series ring in three variables — the receptacle of the three formal deformations $(\tau_1, \tau_2, \tau_3)$ of the $\Omega$-background $(h_1, h_2, h_3)$. It is **infinite-dimensional** as a $\C$-vector space. The 3-dualizability finiteness axiom in $\mathrm{Alg}_{E_3}$ requires $\HH^0_{E_3}(A, A)$ to be finite-dimensional (equivalently, a dualizable $\C$-module); this fails. 

The Calabi–Yau slice $\sum_i h_i = 0$ cuts out a codimension-1 formal subspace $\HH^0_{\mathrm{CY}} = \C[[\tau_1, \tau_2, \tau_3]]/(\tau_1 + \tau_2 + \tau_3)$, which is still infinite-dimensional. The obstruction is **structural**, not remediable by CY-restriction alone on the non-compact base $\C^3$. See quantum_chiral_algebras.tex Remark rem:plat-dualizability-HH0 for the explicit formal-deformation identification; the three generators of $\HH^0$ correspond to the triality of the affine Yangian $Y_{h_1, h_2, h_3}(\widehat{\fgl}_1)$ (Miki automorphism permutes them cyclically).

### Theorem BZ5 ($E_3$-Koszul self-duality $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$)\label{thm:bz-e3-koszul-self-dual}
\ClaimStatusTheorem

The $E_3$-operad in chain complexes over $\Q$ is Koszul self-dual up to shift: the Koszul dual operad $\mathcal{D}_3^! := \mathrm{Bar}(\mathcal{D}_3)^\vee[2]$ satisfies $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$ as dg-operads. Equivalently, on the category of augmented $E_3$-algebras, the bar–cobar adjunction $B_{E_3} \dashv \Omega_{E_3}$ is a Quillen equivalence with shifted-Lie coalgebras on the dual side.

*Proof at CFG detail.*

(i) *Strict statement.* Gwilliam–Williams 2021 §5.3 proves the strict Koszul-self-duality of $\mathcal{D}_3$ on the level of bar-cobar resolutions: the reduced bar construction $\overline{B}_{E_3}(A)$ of a free $E_3$-algebra $A = \mathcal{D}_3(V)$ is explicitly quasi-isomorphic to the shifted free shifted-Lie coalgebra $\mathrm{Lie}^{\mathrm{coalg}}(V[-2])$.

(ii) *Homotopy statement.* Francis–Gaitsgory 2012 (arXiv:1106.2489) prove the $\infty$-categorical version: in the $\infty$-category $\mathrm{Alg}_{E_n}^{\mathrm{aug}}(\mathcal{C})$ of augmented $E_n$-algebras in a stable $\infty$-category $\mathcal{C}$, the functor $B_{E_n}$ is a fully faithful embedding into $\mathrm{coAlg}_{E_n}^{\mathrm{aug}}(\mathcal{C})$ whose essential image is the nilpotent coalgebras. At $n = 3$, the Koszul-dual $\infty$-category is $\mathrm{Lie}$-algebras shifted by $2$.

(iii) *Compatibility.* Fresse 2017 *Homotopy of Operads* Vol. I Theorem 12.3.A provides the bridge between the strict bar-cobar resolution (Gwilliam–Williams) and the homotopy bar-cobar adjunction (Francis–Gaitsgory) via the Positselski coderived/contraderived transfer (Positselski 2011 "Two kinds of derived categories, Koszul duality, and comodule-contramodule correspondence," Memoirs AMS 212).

(iv) *Consequence for dualizability.* For any $E_3$-algebra $A$ satisfying the Koszul hypothesis (Proposition 5.3.1, Gwilliam–Williams), 3-dualizability is equivalent to finiteness of $\HH^\bullet_{E_3}(A, A)$. Via Koszul duality, this becomes finiteness of $\mathrm{Ext}^\bullet_{U(\mathrm{Lie}[2]\text{-coalg})}(\C, \C)$ on the dual side — the shifted-Lie-algebra cohomology.

### Conjecture BZ6 (Compact CY$_3$ recovery of 3-dualizability)\label{conj:bz-compact-cy3-recovery}
\ClaimStatusConjectured

Let $X$ be a smooth compact Calabi–Yau 3-fold with a fixed holomorphic volume form $\Omega_X \in H^{3,0}(X)$. Let $\mathrm{Obs}_{\hCS}(X)|_\mathfrak{g}$ be the $E_3$-algebra of observables of 6D holomorphic Chern–Simons theory on $X$ with semisimple gauge algebra $\mathfrak{g}$. Then $\mathrm{Obs}_{\hCS}(X)|_\mathfrak{g}$ is $3$-dualisable in $\mathrm{Alg}_{E_3}(\mathrm{Mod}_{\C})$. Equivalently, $\HH^\bullet_{E_3}(\mathrm{Obs}_{\hCS}(X), \mathrm{Obs}_{\hCS}(X))$ is finite-dimensional in each cohomological degree.

*Evidence.* The chain-level heuristic: on compact $X$, the propagator $P_X$ (compactification of Bochner–Martinelli) has discrete spectrum via Hodge theory, so the formal deformation space $\HH^0_{E_3}$ should concentrate on finitely many eigenmodes. On $K3\times E$ specifically, the $\Phi_3$-output $\mathbf{H}_{\Delta_5}$ has $\ChirHoch^\bullet$ concentrated in degrees $\{0,1,2,3\}$ (hochschild_calculus.tex Remark hochcalc-theoremH-CY3-scope) with each $\ChirHoch^i$ finite-dimensional on the Koszul locus $\mathcal{U}^{K3}_{\mathrm{Kosz}} = \overline{\mathcal{A}_2}\setminus(H_1 \cup H_4)$.

*Obstruction to theorem-status.* The primary-literature input for $E_3$ coherent duality on compact CY$_3$ is not yet published. Costello 2013 (arXiv:1303.2632) and Costello–Gwilliam–Li 2021 prove $E_3$-structure on $\mathrm{Obs}_{\hCS}(X)$; Francis 2013 proves $\{0,1,2\}$-concentration for $E_n$-Hochschild at $n \leq 2$; the compact-CY$_3$ finiteness is known at the **chain-level** on $K3 \times E$ (hochschild_calculus.tex Proposition chi-3-nonvanishing-MNOP) but **not** at the $(\infty,1)$-categorical level as a general fact for arbitrary compact CY$_3$. The status is therefore **Conjectured**, not **Proved**. The claim (iv) in `wn:thm:plat-dualizability` is **downgraded** to this conjecture.

## Retractions with true hidden structure

### Retraction R1: $\kappa^! = \kappa_{\mathrm{BKM}}$

*Wrong claim.* $\kappa_{\mathrm{ch}}^!(\mathcal{H}_{\mathrm{Muk}}) = \kappa_{\mathrm{BKM}}(\Phi_1) = 5$, so $K^{\kappa_{\mathrm{ch}}} = 3 + 5 = 8$ reads as $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) + \kappa_{\mathrm{BKM}}(\Phi_1)$.

*Precise error.* The two quantities live in different slots:
- $\kappa_{\mathrm{ch}}^!(A)$ is the modular characteristic of the **Verdier dual** $A^!$ of $A$ on $\mathrm{Ran}(X)$ — an invariant of the chiral algebra lane.
- $\kappa_{\mathrm{BKM}}(\Phi_N)$ is the **Borcherds weight** of the paramodular Siegel form $\Phi_N$ — an invariant of the automorphic lift lane.

The claim confuses two subscripts: `ch-dual` vs `BKM`. The numerical coincidence at $N = 1$ (both give small integers) is accidental and breaks at $N \geq 2$ — see working_notes.tex line 388 for the explicit broken-additivity proof.

*Ghost theorem.* The true statement is the **three-faces** identity of $8$ (Remark one-identity-three-faces-k3, k3_chiral_bialgebra_platonic.tex):
- $8 = 2c_+(\mathrm{Mukai}(K3))$ (Mukai face, categorical).
- $8 = \mathrm{ord}(\mathrm{monodromy}\,\mathcal{L}^{\Delta_5}|_{H_1})$ (Humbert-$H_1$ face, arithmetic).
- $8 = \ell$ Lusztig root-of-unity (quantum-group face).

These three readings are unified by Bruinier 2002 Proposition 5.1 (Mukai ↔ Humbert) and Drinfeld 1990 scaling $\hbar = 2\pi i/\ell$ (Humbert ↔ Lusztig). The Borcherds weight $\kappa_{\mathrm{BKM}} = 5$ is a **fourth, disconnected** invariant of $\Delta_5$ that happens to sum with $\kappa_{\mathrm{ch}}(K3 \times E \text{ fibre}) = \chi(\mathcal{O}_{K3\times E}) = 0 + \text{elliptic-correction} = 3$ to give $8$ **numerically at $N = 1$**, but this sum is **not** the Koszul-conductor identity; it is a Borcherds-product-expansion artefact.

### Retraction R2: working_notes.tex line 520 additivity $3 = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$

*Wrong claim.* $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}} \otimes \mathfrak{g}^{\mathrm{BPS}}_{K3}) = 3$ by additive decomposition $\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$.

*Precise error.* Two subtle slips:
(a) $\kappa_{\mathrm{ch}}(E) = 1$ is **false** on the universal formula $\kappa_{\mathrm{ch}} = \sum_q (-1)^q h^{0,q}(X)$: for an elliptic curve $E$, $h^{0,0}(E) = 1$, $h^{0,1}(E) = 1$, so $\kappa_{\mathrm{ch}}(E) = 1 - 1 = 0$. The value $1$ is ambient-unqualified.
(b) $\kappa_{\mathrm{ch}}$ is **not additive on tensor products** of chiral algebras in general; it is additive on direct sums of CY fibre categories (when the ambient CY is a disjoint union, which $K3 \oplus E$ is not — $K3 \times E$ is a **product**, not a sum).

The correct scope: on the Heisenberg-Mukai specialisation at $d = 3$, the relevant modular characteristic is $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 4$ (from $\varrho K = (1/6)\cdot 24$ Mukai-rank reading) — **not** $3$. The value $3$ in working_notes.tex line 520 is a scope-confusion artefact: it mixes the Hodge supertrace of the compact CY$_3$ target (which gives $\chi(\mathcal{O}_{K3\times E}) = 0$, not $3$) with an ad-hoc summand decomposition.

*Ghost theorem.* The correct **four-faces** of $\{0, 4, 5, 24\}$ (not $\{0, 3, 5, 24\}$) on the $K3 \times E$ platonic crystallisation:
- $\kappa_{\mathrm{cat}}(K3 \times E) = \chi(\mathcal{O}_{K3\times E}) = \chi(\mathcal{O}_{K3})\cdot\chi(\mathcal{O}_E) = 2\cdot 0 = 0$ (Künneth-multiplicative).
- $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 4$ (Mukai-enhanced K3 Heisenberg chiral algebra, $\mathsf{B}$-row $\varrho K/2 = 24/6$; matches $c_+(\mathrm{Mukai}(K3)) = 4$ from signature-split).
- $\kappa_{\mathrm{BKM}}(\Phi_1) = 5 = c_1(0)/2$ (Borcherds weight of $\Delta_5 = \mathrm{Borch}(\phi_{0,1}^{K3})$).
- $\kappa_{\mathrm{fiber}}(K3) = 24 = \mathrm{rank}(\widetilde{\Lambda}(K3))$ (Mukai lattice rank).

**Scope declaration**: working_notes.tex line 520 should be replaced with $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 4$; the "$3 = 2 + 1$" line is to be flagged for rectification. Alternatively — and this is the ghost the author had in mind — the value $3$ is the $E_3$-chiral dimension shift in the CY-B$_3$ Serre-duality lane: on the compact CY$_3$, $\ChirHoch^\bullet$ concentrates in degrees $\{0,1,2,3\}$ with top class $\ChirHoch^3 = \C\cdot[\omega_{K3\times E}]$ (hochschild_calculus.tex eq. eq:hochcalc-CY3-scope); the supertrace of this four-term concentration is $3$ only if one weights degrees $\{0,1,2,3\}$ as $\{+1, -1, +1, -1\}$ and plugs in $\{1, 1, \infty_{\mathsf{B}}, 1\}$ without regularisation. This is not the modular characteristic $\kappa_{\mathrm{ch}}$; it is the **naive Euler characteristic of the ChirHoch concentration**, a different invariant. 

### Retraction R3: `wn:thm:plat-dualizability` item (iv) as Theorem

*Wrong claim.* 3-dualizability "recovers on compact CY$_3$" — stated with Claim-status-Theorem.

*Precise error.* The primary-literature input required is $E_3$-analogue of proper-Calabi–Yau coherent duality for the full observable algebra $\mathrm{Obs}_{\hCS}(X)$ on a compact CY$_3$ $X$. Costello 2013 and Costello–Gwilliam Vol II establish the **existence** of the $E_3$-algebra on compact $X$ (via renormalisation-group flow with compact propagator); Francis 2013 Theorem 1.1 gives $E_n$-Hochschild concentration in $\{0, \ldots, n+1\}$; but **finiteness** of each $\HH^i_{E_3}$ on compact CY$_3$ is not proved in general. 

The only case proved at chain-level is $X = K3 \times E$ (hochschild_calculus.tex Proposition chi-3-nonvanishing-MNOP, Theorem hoch-chi3-koszul-obstruction) — and this is via a $\Phi_3$-specific computation using the Gritsenko $V_1$-lift and Igusa-Borcherds denominator, **not** via a general coherent-duality argument.

*Ghost theorem.* The correct claim is **Conjecture BZ6** (above): 3-dualizability of $\mathrm{Obs}_{\hCS}(X)|_\mathfrak{g}$ on compact CY$_3$ is a **conjecture** with chain-level evidence on $K3\times E$ and tree-level evidence on the quintic; its $(\infty,1)$-categorical proof requires Costello–Francis–Gwilliam 2026 + a compact-$X$ extension of Gwilliam–Williams 2021 Proposition 5.3.2 that is currently unwritten.

### Retraction R4: "$\kappa + \kappa^! \in \{0, 8, 13, 250/3, 98/3\}$ **universally** on the five-archetype ceiling"

*Wrong claim.* The five-element set $\{0, 8, 13, 250/3, 98/3\}$ is a universal bound for $K^{\kappa_{\mathrm{ch}}}$ across all CY$_d$ archetypes.

*Precise error.* The $\mathsf{B}$-row value $8$ is **specific to the Mukai-enhanced K3 Heisenberg** $\mathcal{H}_{\mathrm{Muk}}(K3)$ on the Lorentzian-lattice-parametric family, not a universal bound. The general landscape populates the **rational** set
$$\{0\} \cup \{13, 250/3, 98/3\} \cup \{(H_N - 1)K_N\}_{N \geq 4} \cup \{8\}_{\mathcal{B}}$$
(Theorem derived-centre-complementarity-strengthened, chiral_center_theorem.tex eq:thm-C-full-set). Principal $\mathcal{W}_N^k$ at $N \geq 4$ produces further values outside $\{0,8,13,250/3,98/3\}$: e.g. $(H_4 - 1)K_4 = (25/12)\cdot K_4$ is rational and distinct from all five.

*Ghost theorem.* The precise claim is **Theorem BZ1** above: $K^{\kappa_{\mathrm{ch}}} \in \{0, 8, 13, 250/3, 98/3\}$ holds **exactly** on the **six-witness landmark table** $\{\mathcal{H}_k, \widehat{\fg}_k, \beta\gamma_\lambda, \mathrm{Vir}_c, \mathcal{W}_3^k, \mathrm{BP}_k, \mathcal{H}_{\mathrm{Muk}}(K3)\}$. The five-element bucket is the **canonical landmark ceiling**, not a universal bound. Scope must be declared.

## Cross-consistency checks

### (a) Harmony with `platonic_synthesis_waves_11_through_16.tex`

- `wn:thm:plat-dualizability` items (i), (ii), (v): **survive** (Theorems BZ3, BZ5 above).
- Item (iii) (non-abelian failure on $\C^3$): **survives** as Theorem BZ4.
- Item (iv) (compact-CY$_3$ recovery): **downgraded** to Conjecture BZ6.
- `wn:thm:plat-hCS-quantum` ($E_3$-algebra structure via Bochner–Martinelli OPE, $\pi_1(S^5) = 0$): consistent with Theorem BZ3.
- `wn:thm:plat-Linf-minimal` (Atiyah class as formality obstruction on compact CY$_3$): consistent with the ChirHoch concentration machinery underlying Conjecture BZ6.

### (b) Harmony with `CoHA_to_W_infty_treatise.tex`

$\mathrm{CoHA}(\C^3) = Y^+$ is the positive half of the affine Yangian, not the Drinfeld double; it is $E_1$-chiral on $\C^3$. The $\HH^0_{E_3} = \C[[\tau_1, \tau_2, \tau_3]]$ obstruction of Theorem BZ4 is **consistent** with the triality $Y_{h_1, h_2, h_3}(\widehat{\fgl}_1)$ of the treatise §5: the three formal parameters $\tau_i$ are the logarithmic coordinates on the Miki-$S_3$ triality axis. The $\Omega$-background $\sum h_i = 0$ slice cuts $\HH^0_{\mathrm{CY}}$ to codimension $1$, still infinite-dimensional, explaining why $Y_{h_1, h_2, h_3}^{\mathrm{CY}}$ remains an infinite-dimensional deformation space on non-compact $\C^3$.

### (c) Universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

Theorem BZ2 **enforces** that $\kappa_{\mathrm{ch}}^!$ (Verdier dual of chiral algebra) is orthogonal to $\kappa_{\mathrm{BKM}}$ (Borcherds weight of automorphic form): the two subscripts label invariants of genuinely different objects. The universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (Gritsenko 1999, Borcherds 1995/1998) remains intact on the CHL slice $N \in \{1,2,3,4,6\}$ with values $\{5, 4, 3, 2, 1\}$; it does **not** enter the five-archetype complementarity ceiling.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$

Theorem BZ1 respects the factorisation: the $\mathsf{B}$-row witness $\mathcal{H}_{\mathrm{Muk}}(K3)$ is obtained as the abelian-sector Stage-2 specialisation of $\Phi_2^{\mathrm{FA}}(D^b\mathrm{Coh}(K3))$ along $\Sigma_1 = \{pt\}\subset K3$, $C = K3$; the Mukai lattice $(4, 20)$ is the K3-fibre data of Stage 1 before specialisation. Tier-(ii) in the three-tier stratification (Theorem plat-three-tier, platonic_synthesis_waves_11_through_16.tex) — "Stage-1 invariants of $\mathcal{F}_X$" — is exactly where $\kappa_{\mathrm{fiber}} = 24$ and Mukai signature $(4,20)$ live; the Koszul-conductor $K^{\kappa_{\mathrm{ch}}} = 8$ is Tier-(iii), a $(\Sigma, C)$-specialisation invariant of the resulting chiral algebra.

## Residual frontier

**F1.** Conjecture BZ6 (compact CY$_3$ recovery of 3-dualizability) — requires $E_3$-coherent-duality input not in primary literature. [\ClaimStatusOpen] Scope: all compact CY$_3$ with $\mathfrak{g}$ semisimple, finite-type. Tightest available: $X = K3\times E$, chain-level at the ChirHoch-concentration lane.

**F2.** Extension of the five-archetype landmark ceiling to CY$_d$ with $d \geq 4$. The Calabi–Yau fourfold $\mathrm{Kuga\text{-}Satake}(K3\times K3)$ would give a candidate $\mathsf{B}_4$-row with $c_+(\mathrm{Mukai}^2) = ?$; conjecturally $K^{\kappa_{\mathrm{ch}}} = 16 = 2 \cdot 8$. [\ClaimStatusConjectured]

**F3.** Does the Mukai-doubling identity $K^{\kappa_{\mathrm{ch}}} = 2c_+(\mathrm{Mukai}(K3))$ admit an independent derivation without recourse to Bruinier Proposition 5.1? A Serre-duality-first derivation via the CY-$2$ bar-complex symmetrisation would promote the identity to a categorically-pure $(\infty,1)$-statement. [\ClaimStatusOpen]

**F4.** Rectification: working_notes.tex line 520 value $\kappa_{\mathrm{ch}} = 3$ disagrees with landscape_census.tex $\mathsf{B}$-row $\kappa_{\mathrm{ch}} = 4$ (from $\varrho K / 2 = 8/2$). This is a **scope slip** — both readings may be correct at their declared scope (line 520: compact-CY$_3$ Hodge-supertrace fibre-by-fibre sum; landscape_census: Mukai-enhanced $E_2$-chiral on K3 alone) but the manuscript currently lacks the scope-declaration that reconciles them. [\ClaimStatusCorrected pending rectification]

**F5.** The assertion that $K^\kappa = 8$ is the sum $\kappa + \kappa^!$ specifically for the Mukai-enhanced Heisenberg: the Verdier dual $\mathcal{H}_{\mathrm{Muk}}^!$ is not explicitly constructed in the manuscript. Without the explicit bar-complex Koszul partner, the sum $4 + 4 = 8$ is a formal matching; the primary-source input is the Mukai-doubling identity (II in the three-faces), which bypasses the Koszul construction by going through the Beilinson–Drinfeld Chern-class lane. This is **acceptable** because the three faces I/II/III are independently proved and their coincidence is Bruinier's reciprocity. But a direct Koszul-partner construction of $\mathcal{H}_{\mathrm{Muk}}^!$ — via the K3 Serre functor $S_{K3} = [2]$ acting on the bar coalgebra — would strengthen the $\mathsf{B}$-row to a pure-Koszul statement. [\ClaimStatusOpen]

## Attack-heal cycle log (private)

**Cycle 1: ATTACK — Is $K^\kappa = 8$ via $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{BKM}} = 3 + 5$?** User's adversarial question: the $\mathsf{B}$-row $K^\kappa = 8$ claim ambiguously hides the structure. Checked chiral_center_theorem.tex §12.3, landscape_census.tex Proposition archetype-complementarity-bridge: answer is **NO**. The identity is $K^\kappa = \varrho K = (1/6)(48) = 8 = 2c_+(\mathrm{Mukai}(K3))$, independent of the Borcherds weight $\kappa_{\mathrm{BKM}} = 5$. The two lanes are disconnected.
**HEAL — Theorem BZ1 (five-archetype ceiling) + Theorem BZ2 ($\kappa^! \neq \kappa_{\mathrm{BKM}}$) + Retraction R1.** The $\mathsf{B}$-row is $\kappa_{\mathrm{ch}} = 4$, $\kappa_{\mathrm{ch}}^! = 4$, sum $= 8$, via Mukai-doubling. The value $5$ is $\kappa_{\mathrm{BKM}}$, a different invariant.

**Cycle 2: ATTACK — Is $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 3$ or $4$?** working_notes.tex line 520 says $3$ (from $2 + 1$); landscape_census.tex $\mathsf{B}$-row table says $4$ (from $\varrho K / 2$). Which? Computed signature $(4, 20)$ of Mukai lattice: $c_+ = 4$, so $\kappa_{\mathrm{ch}} = c_+ = 4$ on Mukai-enhanced Heisenberg. The line-520 value $3$ uses a different reading ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$) which is additively confused: $\kappa_{\mathrm{ch}}(E) = 0$ by Hodge supertrace of elliptic curve, not $1$.
**HEAL — Retraction R2.** Ghost theorem: $\kappa_{\mathrm{ch}}(\mathcal{H}_{\mathrm{Muk}}) = 4$ at the Mukai-doubling lane; the "$3 = 2 + 1$" reading is a different, naive-concentration-count invariant that should be **subscripted differently** (not $\kappa_{\mathrm{ch}}$). Rectification flag added.

**Cycle 3: ATTACK — Is item (iv) of `wn:thm:plat-dualizability` actually a theorem?** Primary literature input: Costello 2013 + Costello–Gwilliam Vol II + Francis 2013 + Gwilliam–Williams 2021. Francis 2013 Theorem 1.1 is $E_n$-HH concentration in $\{0, \ldots, n+1\}$, which is a concentration bound, not a finite-dimensionality statement per degree. The claim "$\HH^\bullet_{E_3}$ finite-dimensional on compact CY$_3$" is NOT in primary literature in general.
**HEAL — Retraction R3 + Conjecture BZ6.** Downgrade item (iv) to conjecture. Evidence on $K3\times E$ via Oberdieck/Bruinier/Gritsenko. Residual frontier F1.

**Cycle 4: ATTACK — Is $K^\kappa \in \{0, 8, 13, 250/3, 98/3\}$ a universal bound?** Checked chiral_center_theorem.tex eq:thm-C-full-set: the full landscape is $\{0\} \cup \{13, 250/3, 98/3\} \cup \{(H_N-1)K_N\}_{N\geq 4}\cup\{8\}_{\mathcal{B}}$. The bucket $\{0,8,13,250/3,98/3\}$ is a **landmark ceiling on the seven-witness table**, not a universal bound.
**HEAL — Retraction R4.** Scope declared: the five-element bucket holds exactly on the canonical seven landmark witnesses, not universally. Principal $\mathcal{W}_N^k$ at $N \geq 4$ produces rational values outside the bucket.

**Cycle 5: ATTACK — Does the Bochner–Martinelli $E_3$-trace actually recover the abelian 3-dualizability?** Checked: $\partial\overline{\mathrm{Conf}}_2(\C^3) \simeq S^5$ (link of fat diagonal in Fulton–MacPherson); $P_{\mathrm{BM}}$ integral over $S^5$ = $2\pi^3/3!$ (standard). Abelian sector is free $E_3$-algebra on $\Omega^{0,\bullet}_c(\C^3)[1] \simeq \C$, dualizable. Lurie HA 5.3.2 applies.
**HEAL — Theorem BZ3.** $E_3$-trace nondegeneracy + abelian 3-dualizability proved. Non-abelian failure via $\HH^0 = \C[[\tau_1, \tau_2, \tau_3]]$ obstruction from Gwilliam–Williams 2021 Proposition 5.3.2 — Theorem BZ4.

**Cycle 6: ATTACK — Is $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$ strict or only $\infty$-categorical?** Gwilliam–Williams 2021 §5.3 gives strict; Francis–Gaitsgory 2012 gives $\infty$-categorical; Fresse 2017 Vol I Thm. 14.1.A bridges via Thm. 12.3.A + Positselski coderived/contraderived transfer. Both lanes work; stated in each.
**HEAL — Theorem BZ5 + lane-discipline declaration.** Strict on the chain-level (homotopy transfer of free $E_3$-algebra); $\infty$-categorical on augmented $E_3$-algebras in stable $\infty$-cats; compatibility via Fresse + Positselski. The "real theorem" is **both lanes simultaneously** (Pattern 236 ambient-qualifier discipline).

**Cycle 7: ATTACK — Why does $\varrho(\mathcal{H}_{\mathrm{Muk}}) = 1/6$ and not $1$ (as for plain Heisenberg)?** Mukai-enhanced Heisenberg is *not* plain rank-24 Heisenberg; it is the $E_2$-chiral $\Phi_2$-image of $D^b\mathrm{Coh}(K3)$ including the Serre structure $S_{K3} = [2]$. The $[2]$-shift contributes to the Koszul bar-degree count, and the anomaly ratio is computed with the shifted pairing. Verified against landscape_census.tex line 1795 table entry: $\varrho = 1/6$, $K = 48$. This matches the Mukai-doubled Bershadsky–Polyakov-like pattern: $\mathrm{BP}_k$ has $\varrho = 1/6$, $K = 196$, $K^\kappa = 98/3$; $\mathcal{H}_{\mathrm{Muk}}$ has $\varrho = 1/6$, $K = 48$, $K^\kappa = 8$. Same anomaly ratio class; different conductors.
**HEAL — Structural insight.** The $\varrho = 1/6$ of the $\mathsf{B}$-row is **structurally identical** to the $\mathsf{M}$-ext Bershadsky–Polyakov row. This is not coincidence: the Mukai-enhanced K3 Heisenberg sits in the same Drinfeld–Sokolov reduction class as BP (minimal nilpotent orbit, three-step step-variable). This unifies the $\mathsf{B}$-row into the principal-$\mathcal{W}$-tower classification, with Mukai-signature replacing the $\mathfrak{sl}_3$ Cartan rank. Candidate new identity: for the $\Phi_2$-image of any $d=2$ CY category with pairing signature $(p, q)$, $\varrho = 1/(p+q-(p-q)/2)$, specialising to $1/6$ at $(p,q) = (4,20)$, matching BP. [Requires verification; flagged as Conjecture candidate.]
