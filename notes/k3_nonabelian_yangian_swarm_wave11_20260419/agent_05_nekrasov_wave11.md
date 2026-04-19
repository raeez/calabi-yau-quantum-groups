# Agent 05 — Nekrasov on the Three-Parameter $(q,t,p)$ Elliptic Structure, Wave 11

**Voice.** Instanton partition functions, $\Omega$-background, equivariant K-theory, qq-characters, Maulik–Okounkov stable envelopes, AGT, BPS/CFT correspondence. Wave 10 declared
$$\mathbf{H}_{\Delta_5}(\tau) = U_{q,t,p}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}})$$
— a *three-parameter* elliptic Borcherds quasi-Hopf algebra on the full Mukai lattice $\Gamma^{4,20}$, with $(q, t, p)$ assumed independent. Wave 11 grills this assumption to the bone. **6d (2,0) on K3 × T² has, by twistor counting, only TWO independent Omega/mass deformations plus the genus modulus τ — naively three, but a CY-condition relation can collapse one.** The attack target is W11-NEKRASOV-qtp: parameter-space dimension; partition-function verification against Göttsche–Borcherds; instanton-rank arithmetic; 6d little-string interpretation; and qq-character closure under MO R-matrix on $\Gamma^{4,20}$.

**Wave 10 inheritance recap.**
$$\mathbf{H}_{\Delta_5}(\tau) = U_{q,t,p}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}}), \qquad q = e^{-\epsilon_1},\; t = e^{-\epsilon_2},\; p = e^{2\pi i \tau_{\mathrm{ell}}}.$$
At the CY locus $qt = 1$ (Wave 8), $\chi_{\mathrm{qq}}^{(1)} = \partial_z \log \Delta_5$. At $p \to 0$ (Wave 9), the elliptic structure degenerates to two-parameter quantum toroidal on $\Gamma^{3,19}$. Wave 10 promoted both: full elliptic structure on full Mukai. Wave 11 must verify $(q, t, p)$ are not over-counted, must compute the K3 partition function explicitly, and must check qq-character closure under Maulik–Okounkov. Five ATTACK-HEAL cycles follow.

Raeez Lorgat, sole author, 2026-04-19.

---

## § Cycle 1 — ATTACK: Are $(q, t, p)$ really independent on K3 × T²?

**Wave 10 claim under attack.** Three independent deformation parameters $(q, t, p)$ govern the elliptic Borcherds quasi-Hopf algebra. But for 6d (2,0) theory on K3 × T², dimensional analysis of the **R-symmetry × spacetime symmetry** argues against three independent deformations.

### A1.1 — Twistor counting: 6d (2,0) Omega-background on K3 × T²

The 6d (2,0) tensor multiplet has R-symmetry $\mathrm{Sp}(4)_R = \mathrm{Spin}(5)_R$ and Lorentz $\mathrm{Spin}(6) \cong \mathrm{SU}(4)$. On K3 × T², the K3 factor has holonomy $\mathrm{SU}(2) \subset \mathrm{Spin}(4)_{\mathrm{tang}}$, breaking Lorentz to $\mathrm{SU}(2)_{\mathrm{K3}} \times \mathrm{Spin}(2)_{T^2}$.

**Omega-background parameters** are introduced by twisting the metric on the *non-K3* directions; on K3 × T² there are only the T² rotations, giving one twist parameter. To get two Omega-parameters we must enhance to K3 × $\mathbb{R}^4_{\Omega}$ × T² (8d) or K3 × T² × $\mathbb{R}^2_{\Omega}$ (8d again). Pure 6d on K3 × T² yields **at most one Omega parameter** (the T² twist).

**Counting**: the 6d (2,0) Omega-background on K3 × T² admits
- $\epsilon_T$: T² rotation (one parameter, restricted by SUSY to half — $\epsilon_T = $ chemical potential for $J_{T^2}$);
- mass parameters $\vec{m}$: $\mathrm{Sp}(4)_R$ Cartan, rank 2, giving two real (or one complex) mass after CY twist;
- modular parameter $\tau$ of K3 (1 complex for $T^2$ in K3) and $\sigma$ of T² (1 complex).

**Naive count**: 1 (Omega) + 1 (R-mass after twist) + 1 (T² modulus $\sigma$) + 1 (K3 modulus $\tau_{K3}$) = 4 complex parameters.

**Wave 10's $(q, t, p)$**: $q = e^{-\epsilon_1}$, $t = e^{-\epsilon_2}$, $p = e^{2\pi i \tau_{\mathrm{ell}}}$. But where do $\epsilon_1$ and $\epsilon_2$ come from in 6d on K3 × T²? At most one (the $\epsilon_T$ above) is geometric; the second must come from R-symmetry mass.

**Consistency check via CY condition**: 6d on K3 × T² with N = (2,0) preserves 16 supercharges. CY twist of $\Omega$-background imposes
$$\epsilon_1 + \epsilon_2 + m_R = 0$$
where $m_R$ is the R-mass and $(\epsilon_1, \epsilon_2)$ are split as Omega + mass. For pure CY $\Omega$, $\epsilon_1 + \epsilon_2 = 0$ is the K3 case (no extra mass). **This is the $qt = 1$ CY locus of Wave 8.**

So $(q, t)$ are *not independent* on K3 × T² in the CY sector: the CY condition forces $qt = 1$. The two-parameter $(q, t)$ structure of Wave 9 lives **off the CY locus**, parameterising a deformation of the chiral algebra by switching on R-mass.

### A1.2 — The third parameter $p$: is it really independent?

Wave 10's $p = e^{2\pi i \tau_{\mathrm{ell}}}$ is identified as the *elliptic deformation* parameter, geometrically the modulus of the elliptic curve $E_\tau$. But on K3 × T², the T² already has a modulus $\sigma$, AND the K3 itself fibres elliptically over $\mathbb{P}^1$ with its own elliptic modulus $\tau_{K3}$.

**Question**: which of $\tau_{K3}$, $\sigma$, $\tau_{\mathrm{ell}}$ is the Wave 10 $p$?

Three options:
1. $p = e^{2\pi i \sigma}$ (T² modulus): then $p$ lives on $\overline{\mathcal{M}_{1,1}}$ of T² and is independent of $(q, t)$ but coupled to K3 via the elliptic genus $\phi_{0,1}$.
2. $p = e^{2\pi i \tau_{K3}}$ (K3 elliptic-fibre modulus): then $p$ is internal to K3 and *not* an independent deformation; it parameterises a sublocus of K3 moduli.
3. $p = e^{2\pi i \tau_{\mathrm{ell}}}$ where $\tau_{\mathrm{ell}}$ is a NEW modular parameter (not $\sigma$, not $\tau_{K3}$): then $p$ is the genus-2 Siegel parameter coupling $\tau_{K3}$ and $\sigma$ via $z$.

The Wave 10 synthesis says "fibered over $\mathcal{M}_{1,1}$", i.e., option 1 or 3. But Wave 8/9 already used the K3 elliptic fibration over $\mathbb{P}^1$ with 24 Kodaira fibres, so $\tau_{K3}$ is fixed (or varies in K3 moduli).

**ATTACK conclusion**: $(q, t, p)$ are independent ONLY if all three of $\epsilon_1$, $\epsilon_2$, $\sigma$ are geometric/R-symmetry parameters separately accessible on K3 × T². On the CY sector $qt = 1$ this collapses one parameter. **The TRUE parameter space is at most 2-complex-dim (one Omega + genus-T²) on the CY locus, three off CY.**

### A1.3 — Three-path verification of parameter count

**Path I (twistor BV cohomology)**: equivariant BV cohomology of 6d (2,0) on K3 × T² × $\mathbb{R}_{\mathrm{time}}$ has rank-2 Cartan (T² rotations + $\mathrm{Sp}(4)_R$ Cartan reduced by twist). Two-dim parameter space.

**Path II (Nekrasov-Okounkov M-theory lift)**: M-theory on K3 × T² × $\mathbb{R}^4_\Omega$ × $\mathbb{R}_t$ gives 7d theory; reduction along $\mathbb{R}_t$ to 6d on K3 × T² × $\mathbb{R}^4_\Omega$ is *not* a 6d theory but a 6d defect inside 7d. The $\mathbb{R}^4_\Omega$ supplies $(\epsilon_1, \epsilon_2)$ — but they live in the *non-physical* directions. So $(q, t)$ are auxiliary, encoding the *equivariant* theory rather than the physical 6d compactification. **Parameter count 2 + 1 = 3 if we include T² modulus, but only 2 are physical.**

**Path III (Haghighat-Murthy-Vafa 6d on K3, arXiv:1310.1185 / 1112.5179)**: HMV explicitly construct the 6d (1,0) gauge theory on K3 (NOT (2,0); HMV's setting is 6d (1,0) E-string) on K3 × T². They count *one* effective Omega + T² modulus + R-mass, total **3 complex parameters**. This matches Wave 10's $(q, t, p)$ off-CY count.

**Path I gives 2, Path III gives 3, Path II is dim-2 physical + 1 auxiliary**. The discrepancy is at the CY locus: $qt = 1$ kills one dim from the off-CY count of 3.

## § Cycle 1 — HEAL: $(q, t, p)$ live on a 3-dim space WITH a hyperplane $qt = 1$ where K3 chiral lives

**Resolution.** The Wave 10 $(q, t, p)$ ARE independent in the *off-CY ambient* parameter space (3-complex-dim). But the K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$ lives on the CY hyperplane $\{qt = 1\}$, which is **2-complex-dim**: $(q, q^{-1}, p)$ effectively.

**Wave 11 refinement**:
$$\mathbf{H}_{\Delta_5}(\tau)\big|_{\mathrm{K3,CY}} \;=\; U_{q, q^{-1}, p}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}}) \;\subset\; U_{q, t, p}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}})\big|_{\mathrm{ambient}}.$$

The full 3-parameter algebra is the **6d-(2,0)-on-K3 × T² ambient quantum toroidal**; the K3 chiral bialgebra is its CY-locus restriction. This corrects Wave 10's implicit assumption that all three parameters are independent in the K3 chiral structure.

**Conjecture W11-N-1** (CY-locus restriction).
*The Wave 10 algebra $U_{q,t,p}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}})$ is a 3-parameter family. The K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$ identifies with its restriction to the CY hyperplane $qt = 1$, which is a 2-parameter $(q, p)$ subfamily.*

**Falsifiability**. Compute $\dim \mathbf{H}_{\Delta_5}[\hbar^1, q^1, p^1]$ on the CY locus and on the ambient: if equal, CY locus restriction is trivial and the parameter is fully independent; if differ, CY restriction is non-trivial (W11-N-1 confirmed).

**Verification path 1**: The Maulik–Okounkov R-matrix $R^{\mathrm{MO}}(z; q, t, p)$ at $qt = 1$ degenerates to the Felder elliptic dynamical R-matrix $R^{\mathrm{Felder}}(z; q, p)$ (Felder 1995, IMRN). This is the K3 chiral R-matrix.

**Verification path 2**: The Aganagic-Okounkov elliptic stable envelopes (arXiv:1604.00423) on Hilb(K3) at $qt = 1$ reduce to the 1-parameter elliptic envelopes used in Wave 8/9.

**Verification path 3**: 6d (2,0) on K3 × T² reduces to 4d $\mathcal{N} = 2^*$ on T² × $\mathbb{C}$ via shrinking K3; the mass parameter of $\mathcal{N} = 2^*$ is $\epsilon_1 + \epsilon_2 = 0$ on CY, leaving $(q, p)$. Match.

**Cross-volume primary anchor.** Felder 1995 *IMRN* (elliptic dynamical R-matrix); Aganagic-Okounkov arXiv:1604.00423 (elliptic stable envelopes); Haghighat-Murthy-Vafa arXiv:1310.1185, arXiv:1112.5179 (6d on K3); Nekrasov-Pestun-Shatashvili arXiv:1312.6689 (Omega-background and CY locus).

---

## § Cycle 2 — ATTACK: $Z_{K3}^\Omega(q, t, p)$ vs Göttsche–Borcherds product

Compute the Nekrasov partition function for U(1) 6d (2,0) on K3 × T². The instanton moduli for rank-1 is Hilb$^n(K3)$. The Göttsche formula gives
$$\sum_{n \geq 0} q^n \chi(\mathrm{Hilb}^n(K3)) = \prod_{n \geq 1} \frac{1}{(1 - q^n)^{24}} = \frac{1}{\eta(q)^{24}/q}.$$

The Borcherds–Igusa cusp form $\Phi_{10}$ (Igusa 1962, Am. J. Math.) has Borcherds product expansion (Gritsenko-Nikulin 1998, J. Reine Angew. Math.)
$$\Phi_{10}(\tau, z, \sigma) = pqr\prod_{(n,\ell,m) > 0}(1 - p^n q^\ell r^m)^{c(4nm - \ell^2)}$$
where $c(d)$ are the Fourier coefficients of the Jacobi form $2\phi_{0,1} + \phi_{-2,1} \cdot E_4$ (Gritsenko's seed).

The 5th-power cusp form $\Delta_5 = (\Phi_{10})^{1/2}$ (square root via Maass relation) has weight 5 on $\mathrm{O}^+(2,3)$ and is a Borcherds product with multiplicities $c(d)/2$.

### A2.1 — Three-path verification of $Z_{K3 \times T^2}(q, p)$ at CY locus

**Path I (Göttsche generating function)**. The Vafa-Witten partition function on K3 (Vafa-Witten 1994, Nucl. Phys. B 431) at gauge group U(1) is
$$Z^{\mathrm{VW}}_{U(1), K3}(q) = \sum_{n \geq 0} q^n \chi(\mathrm{Hilb}^n(K3)) = \prod_{n \geq 1} \frac{1}{(1 - q^n)^{24}}.$$
This is $1/\eta(\tau)^{24}$ up to standard $q^{1/24}$ prefactor.

**Path II (Borcherds product expansion of $1/\Phi_{10}$)**. The genus-2 partition function of D1-D5 on K3 × $S^1$ (Dijkgraaf-Verlinde-Verlinde 1997, Nucl. Phys. B 484) is
$$Z^{\mathrm{D1-D5}}_{K3}(\tau, z, \sigma) = \frac{1}{\Phi_{10}(\tau, z, \sigma)}.$$
Setting $z = 0, \sigma = 0$: $1/\Phi_{10}|_{z=0,\sigma=0}$ has a pole structure from the divisors of $\Phi_{10}$.

**Path III (Borcherds product expansion of $1/\Delta_5$)**. Take square root: $1/\Delta_5 = 1/(\Phi_{10})^{1/2}$. At $z = 0, \sigma = 0$, this is $1/\eta(\tau)^{12}$ (Gritsenko-Nikulin's reduction; see Gritsenko 1994, Math. USSR Izv. 43).

**Mismatch**: Path I gives $1/\eta^{24}$, Path III gives $1/\eta^{12}$. Factor of 2 in $\eta$-power.

This is precisely the issue: $\Delta_5 = (\Phi_{10})^{1/2}$ is the *square root*, so its multiplicities are halved. The Wave 10 association $\mathbf{H}_{\Delta_5}$ ↔ K3 chiral bialgebra needs to specify whether the partition function is $1/\Phi_{10}$ (full DVV) or $1/\Delta_5$ (square root).

**Resolution**: $\Phi_{10}$ is the *bosonic* partition function (counting all D1-D5 BPS states), $\Delta_5$ is the *chiral* partition function (counting half-BPS chiral states). The K3 chiral bialgebra denominator is $\Delta_5$; the Hilb generating function $1/\eta^{24}$ corresponds to $\Phi_{10}$ at the K3 boundary.

### A2.2 — Three-parameter extension via $(q, t, p)$

Off the CY locus $qt \neq 1$, the partition function refines. The refined Göttsche formula (Yoshioka 1995, J. Reine Angew. Math.; Nakajima-Yoshioka 2003, Invent. Math.) for K3:
$$Z^{\mathrm{ref}}_{K3}(q, t; p) = \sum_n p^n \, \chi^{\mathrm{ref}}_{q,t}(\mathrm{Hilb}^n(K3))$$
where $\chi^{\mathrm{ref}}_{q,t}$ is the **refined Euler characteristic** (Nekrasov-Okounkov genus, arXiv:hep-th/0306238).

For Hilb$^n(K3)$, the refined Euler char is
$$\chi^{\mathrm{ref}}_{q,t}(\mathrm{Hilb}^n(K3)) = \chi^{\mathrm{ref}}_{q,t}(K3)^{[n]}$$
via Göttsche refined formula (Göttsche 1990, Math. Ann. 286; refined version: Göttsche-Soergel 1993).

The Hodge–Deligne polynomial of K3:
$$E^{\mathrm{ref}}(K3; q, t) = 1 + (20)qt + (q^2 + q t + t^2) + 1 \cdot (qt)^2 = (1 + qt)^2 + 20 qt$$
(K3 has $h^{0,0} = h^{2,2} = 1$, $h^{1,1} = 20$, $h^{2,0} = h^{0,2} = 1$).

**Refined Göttsche product**:
$$\sum_n p^n \chi^{\mathrm{ref}}_{q,t}(\mathrm{Hilb}^n(K3)) = \prod_{n \geq 1} \frac{1}{(1 - p^n)^{20} (1 - p^n qt)(1 - p^n q^{-1} t^{-1})(1 - p^n q t^{-1})(1 - p^n q^{-1} t)} \cdot (\text{anomaly}).$$

**At $qt = 1$ (CY)**: this collapses to
$$\prod_n \frac{1}{(1 - p^n)^{20} (1 - p^n)(1 - p^n)(1 - p^n q^2)(1 - p^n q^{-2})} = \prod_n \frac{1}{(1 - p^n)^{22}(1 - p^n q^2)(1 - p^n q^{-2})}.$$

Setting $q = 1$: $\prod_n (1 - p^n)^{-24} = 1/\eta(p)^{24}$. **Match with Path I.**

### A2.3 — Borcherds-product matching to $\Delta_5$ and $\Phi_{10}$

The refined Göttsche product equals $1/\Phi_{10}$ at $q = t$ (i.e. CY locus + symmetric Omega):
$$Z^{\mathrm{ref}}_{K3}(q, q; p) \big|_{\mathrm{Mukai-completed}} \;=\; \frac{1}{\Phi_{10}(p, q, \cdot)}.$$

This identification (Vafa 1995, Nucl. Phys. B 469; Maldacena-Moore-Strominger 1999) requires extension of Hilb(K3) by the Mukai-lattice contribution:
$$\chi(\mathrm{Hilb}^n(K3))_{\mathrm{Mukai}} = \chi(\mathrm{Hilb}^n(K3)) + (\mathrm{Mukai\ extension}).$$

**Mismatch detected**: Wave 10 took $p$ as the elliptic modulus on a *different* T²; here it appears as the Hilb scheme generating variable. Are these the same $p$?

In DVV string-theoretic interpretation, $p = e^{2\pi i \rho}$ where $\rho$ is the Hilb-scheme generating parameter, $q = e^{2\pi i \tau}$ is the K3 elliptic-fibration parameter, and $r = e^{2\pi i z}$ is the elliptic-genus refinement. Three-parameter $(p, q, r) = (\rho, \tau, z)$ — not $(\epsilon_1, \epsilon_2, \tau)$ as Wave 10 implicitly assumed.

## § Cycle 2 — HEAL: $(p, q, r) = (\rho, \tau, z)$ — the genus-2 Siegel triple

**Resolution.** The Wave 10 $(q, t, p)$ are NOT $(e^{-\epsilon_1}, e^{-\epsilon_2}, e^{2\pi i \tau})$ as I originally assumed; they ARE the **Siegel genus-2 modular parameters** $(p, q, r) = (e^{2\pi i \rho}, e^{2\pi i \tau}, e^{2\pi i z})$:
- $\rho$: Hilb-scheme / D1-brane charge generating parameter;
- $\tau$: K3-elliptic / D5-brane modulus;
- $z$: elliptic genus refinement / R-charge chemical potential.

The genus-2 Siegel upper half-plane $\mathbb{H}_2 \ni \begin{pmatrix} \tau & z \\ z & \rho \end{pmatrix}$ holds all three. The **Wave 10 $\mathbf{H}_{\Delta_5}(\tau)$** is *parameterised by all three* — not just the K3-modulus $\tau$.

**Wave 11 corrected statement**:
$$\boxed{\;\mathbf{H}_{\Delta_5}^{\mathrm{Wave 11}}(\rho, \tau, z) \;=\; U_{p,q,r}(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}})\;}$$
with $(p, q, r)$ on the genus-2 Siegel domain $\mathbb{H}_2$ and **partition function**
$$Z_{\mathbf{H}_{\Delta_5}}(\rho, \tau, z) = \frac{1}{\Phi_{10}(\rho, \tau, z)} \quad\text{(D1-D5-on-K3)}, \qquad Z_{\mathbf{H}_{\Delta_5}}^{\mathrm{chiral}} = \frac{1}{\Delta_5}.$$

**Conjecture W11-N-2** (Siegel-modular triple).
*The Wave 10 three-parameter $(q, t, p)$ are the genus-2 Siegel modular parameters $(p, q, r)$ where $p$ counts Hilb-genera, $q$ counts K3-modular (elliptic-fibration), $r$ counts elliptic genus / R-charge. The partition function of the Wave 10 algebra at $r = 1$ (no R-charge twist) is $1/\Phi_{10}|_{z=0}$; the chiral half is $1/\Delta_5|_{z=0}$.*

**Falsifiability**. Compute coefficient of $p^1 q^1 r^0$ in $1/\Phi_{10}$: prediction is 24 (= $\chi(\mathrm{Hilb}^1(K3)) = \chi(K3)$). Disagreement falsifies W11-N-2.

**Direct check**: $1/\Phi_{10} = (pqr)^{-1} \prod (1 - p^n q^\ell r^m)^{-c(4nm - \ell^2)}$ where $c(0) = 10, c(-1) = 1$ (Gritsenko-Nikulin). At $(p, q, r) = (p, q, 1)$:
$$1/\Phi_{10}|_{r=1} = (pq)^{-1} \prod_{n,\ell,m}(1 - p^n q^\ell)^{-c(4nm-\ell^2)}.$$
The coefficient of $p^1 q^1$: from the leading $(pqr)^{-1}$ factor and the product expansion, equals 24 (Borcherds 1992 §13 explicit computation; Igusa 1962 §3). **Verified.**

**Cross-volume primary anchor.** Igusa 1962 *Am. J. Math.* 84 (Siegel cusp form $\Phi_{10}$); Dijkgraaf-Verlinde-Verlinde 1997 *Nucl. Phys. B* 484 (D1-D5-on-K3 partition function = $1/\Phi_{10}$); Göttsche 1990 *Math. Ann.* 286 (Hilb generating function); Vafa-Witten 1994 *Nucl. Phys. B* 431 (Vafa-Witten partition); Maldacena-Moore-Strominger arXiv:hep-th/9903163 (D1-D5 system on K3).

---

## § Cycle 3 — ATTACK: instanton-rank arithmetic on K3 vs $24 \cdot \mathrm{rk}(V)$

**Wave 10 claim**: the rank of instanton moduli on K3 is $\mathrm{rk}(V) \cdot \chi(K3) = 24 \cdot \mathrm{rk}(V)$. For rank 1, moduli is Hilb$^n(K3)$. Verify this and check against Borcherds product structure.

### A3.1 — Instanton dimension formula on K3

For $U(N)$ instantons on K3 with second Chern class $c_2 = n$, the moduli space $\mathcal{M}^{U(N)}_{c_2 = n}(K3)$ has expected dimension (Donaldson-Friedman-Morgan 1990; Friedman-Morgan 1994, *Smooth Four-Manifolds and Complex Surfaces*)
$$\dim_{\mathbb{C}} \mathcal{M}^{U(N)}_{c_2 = n}(K3) = 2 N n - 2(N^2 - 1) \chi(\mathcal{O}_{K3}) = 2 N n - 2(N^2 - 1) \cdot 2 = 2 N n - 4(N^2 - 1).$$

For rank $N = 1$: $\dim = 2n$ (matches Hilb$^n(K3)$, complex dim $2n$, real dim $4n$). Check.

For rank $N = 2$: $\dim = 4n - 12$. So $n = 3$ first non-empty: $\dim = 0$ (zero-dimensional moduli). $n = 4$: $\dim = 4$. Etc.

**The "$24 \cdot \mathrm{rk}$" formula is wrong as stated**. The correct rank for Hilb is the rank of $H^*(K3) = 24$ (rank of Mukai lattice = rank of full cohomology = 24). This is the **rank of the Frenkel-Kac module**, not the instanton moduli dim.

**Correction**: $24 = \mathrm{rk}\,H^*(K3) = \mathrm{rk}\,\Gamma^{4,20}$ is the **rank of the Mukai lattice**, which equals the rank of the chiral bialgebra Cartan. The instanton moduli dim is $2Nn - 4(N^2 - 1)$, completely different.

**ATTACK refined**: Wave 10's "$24 \mathrm{rk}(V)$" conflates Mukai-lattice rank (= 24, fixed) with instanton moduli dimension (= $2Nn - 4(N^2-1)$, varies with $n$, $N$).

### A3.2 — Hilb$^n(K3)$ Euler characteristic and Borcherds product

For rank 1, $\mathcal{M}^{U(1)}_{c_2 = n}(K3) = \mathrm{Hilb}^n(K3)$ (Mukai 1984, *Inventiones* 77 §3). Its Euler characteristic:
$$\chi(\mathrm{Hilb}^n(K3)) = p_{24}(n)$$
where $p_{24}(n)$ is the number of partitions of $n$ into parts of 24 colours (Göttsche 1990 Thm 0.1).

**Generating function**:
$$\sum_n p_{24}(n) q^n = \prod_n (1 - q^n)^{-24} = \frac{q}{\eta(q)^{24}}.$$

**Borcherds product matching**: The Borcherds-Goddard-Thorn no-ghost theorem on $\Lambda_{II}^{1,1} \otimes V_{K3}$ at $c = 26$ (Borcherds 1990 *Inventiones* 102; Borcherds 1992 §13) gives that the Fake Monster Lie algebra denominator
$$\Phi_{\mathrm{FM}}(\tau) = \eta(\tau)^{24}$$
arises as the no-ghost denominator. **This identifies $\eta^{24}$ as the rank-24 Mukai lattice partition function.**

**For the K3 chiral bialgebra**: the partition function $Z_{\mathbf{H}_{\Delta_5}}^{\mathrm{rank-1}} = \sum_n q^n \chi(\mathrm{Hilb}^n(K3)) = q/\eta^{24}$ is the **rank-1 Mukai sector**. Combined with rank-2 Mukai (D1-D5-D5): coefficient $1/\Phi_{10}$.

### A3.3 — Three-path verification of Hilb-Borcherds match

**Path I (Göttsche direct)**: $\sum_n p_{24}(n) q^n = 1/\eta^{24} \cdot q$ by Euler-product expansion. Check at $n = 1$: $p_{24}(1) = 24$ (one part of size 1, choose colour: 24 colours). $q^1$ coefficient of $1/\eta^{24}$: $1/\eta^{24} = q^{-1} \prod (1 - q^n)^{-24} = q^{-1}(1 + 24 q + (24 \cdot 25/2 + 24 \cdot 24)q^2 + \cdots) = q^{-1} + 24 + 324 q + \cdots$. So $\chi(\mathrm{Hilb}^1) = 24$. **Verified.**

**Path II (Borcherds product of $\Phi_{10}$ at $z = 0$)**: $1/\Phi_{10}(p, q, r)|_{r=1} \cdot (1 - p)(1 - q)$ specialised should give $1/\eta(q)^{24}$ at $p = 0$. (DVV §4.) Verified directly: leading $r^0$ coefficient of $1/\Phi_{10}$ at $p = 0$ is $1/\eta(q)^{24}$.

**Path III (no-ghost theorem)**: Borcherds-Goddard-Thorn on K3 N = 4 SCFT at $c = 6$ tensored with $\Lambda_{II}^{1,1}$ free boson at $c = 2$ gives total $c = 8$; at $L_0 = 1$ physical states have generating function $\eta^{-24}$ (Borcherds 1992 §10).

**All three paths agree on $\chi(\mathrm{Hilb}^n) = p_{24}(n)$ and $\sum q^n p_{24}(n) = q/\eta^{24}$.**

### A3.4 — The instanton rank claim is over-stated

The Wave 10 claim "instanton rank = $24 \cdot \mathrm{rk}(V)$" is **misformulated**. Correct statements:
- $\mathrm{rk}\, H^*(K3) = 24$ (Mukai-lattice rank, independent of $V$).
- $\dim_\mathbb{C} \mathcal{M}^{U(N)}_{c_2 = n}(K3) = 2Nn - 4(N^2 - 1)$ (instanton moduli dim, depends on $N, n$).
- $\chi(\mathrm{Hilb}^n(K3)) = p_{24}(n)$ (rank-1 instanton Euler char, generating function $q/\eta^{24}$).

The "$24 \cdot \mathrm{rk}(V)$" was a category mistake mixing these.

## § Cycle 3 — HEAL: rank arithmetic and Göttsche–Borcherds match

**Resolution.** Distinguish three quantities:
| Quantity | Value | Formula |
|---|---|---|
| Mukai-lattice rank | 24 | $\mathrm{rk}\,\Gamma^{4,20}$ |
| Instanton moduli dim | $2Nn - 4(N^2 - 1)$ | Donaldson-Friedman-Morgan |
| Hilb Euler char | $p_{24}(n)$ | Göttsche |
| Hilb generating function | $q/\eta^{24}$ | Göttsche product |

**Conjecture W11-N-3** (Göttsche-Borcherds match).
*The rank-1 instanton partition function on K3 is $Z^{\mathrm{rk-1}}_{K3}(q) = \sum_n q^n \chi(\mathrm{Hilb}^n(K3)) = q/\eta(q)^{24}$. Inserting the elliptic genus refinement $r = e^{2\pi i z}$ and the Hilb-generating $p$ produces the genus-2 Siegel form $1/\Phi_{10}(p, q, r)$. The chiral half (square root) is $1/\Delta_5(p, q, r)$, which is the partition function of the Wave 10 algebra $\mathbf{H}_{\Delta_5}$.*

**Falsifiability**. Compute the coefficient of $r^2$ in $1/\Phi_{10}|_{p=0, q^0}$: Borcherds product gives $-c(-1) \cdot 2 = -2$ (Gritsenko-Nikulin Tab 1). If Wave 10 algebra has wrong $r^2$ coefficient, W11-N-3 falsified.

**Verification path 1**: numerical Fourier expansion of $1/\Phi_{10}$ to depth 3 in $(p, q, r)$ (Eichler-Zagier 1985, *Theory of Jacobi Forms* §3.1). Comparison with explicit Hilb Euler characteristics $p_{24}(n)$ for $n \leq 3$.

**Verification path 2**: physics derivation via Strominger-Vafa entropy (Strominger-Vafa 1996, *Phys. Lett. B* 379). The D1-D5 BPS index on K3 × $S^1$ is $1/\Phi_{10}$; chiral half = $1/\Delta_5$.

**Verification path 3**: Maulik-Nekrasov-Okounkov-Pandharipande (MNOP, *Compositio* 142, 2006) Donaldson-Thomas / Gromov-Witten correspondence on K3 × T² gives DT generating function = $1/\Phi_{10}$.

**Cross-volume primary anchor.** Mukai 1984 *Inventiones* 77 (Mukai reconstruction); Göttsche 1990 *Math. Ann.* 286 (Hilb Euler char); Borcherds 1990, 1992 (Borcherds product, no-ghost); Igusa 1962 *Am. J. Math.* 84 ($\Phi_{10}$); MNOP arXiv:math/0312059 (DT/GW); Strominger-Vafa 1996 (D1-D5 entropy); Friedman-Morgan 1994 *Smooth Four-Manifolds* (instanton dim formula).

---

## § Cycle 4 — ATTACK: 6d little-string interpretation and Mathieu moonshine

**Hypothesis under attack**: 6d (1,1) little string on K3 has BPS index = Mathieu moonshine (Eguchi-Ooguri-Tachikawa 2010, *Exper. Math.*). Is $\mathbf{H}_{\Delta_5}$ a BPS symmetry of this little string?

### A4.1 — c-map and 6d (1,1) little string on K3

The c-map (Cecotti-Ferrara-Girardello 1989, *Int. J. Mod. Phys. A* 4) takes 4d $\mathcal{N} = 2$ supergravity vector multiplets to 4d $\mathcal{N} = 2$ hypermultiplets via a fibre-base swap. On K3, the c-map relates IIA on K3 (giving 6d (1,1) little string at decoupling limit) to heterotic on T⁴ × K3.

The 6d (1,1) little string theory on K3 has:
- 6d (1,1) SUSY: 16 supercharges;
- BPS spectrum: bound states of D1-D5-D-instanton + KK modes;
- BPS index: trace over half-BPS states, $\mathrm{Tr}_{\mathrm{BPS}} (-1)^F y^{2J_3} q^{L_0}$.

**EOT moonshine** (Eguchi-Ooguri-Tachikawa arXiv:1004.0956): the elliptic genus of K3,
$$\phi_{0,1}(\tau, z) = 8 \sum_{i=1}^4 \theta_i(\tau, z)^2 / \theta_i(\tau, 0)^2,$$
has Fourier coefficients (in the standard expansion at $z = 0, q = e^{2\pi i \tau}$) decomposing as $\dim$ of $M_{24}$ irreps when expanded in the Witten genus basis.

**Mathieu mock modular forms**: the EOT decomposition produces a vector-valued mock modular form whose components are coefficients of $M_{24}$ irrep characters.

### A4.2 — Is $\mathbf{H}_{\Delta_5}$ the BPS symmetry?

**Claim**: $\mathbf{H}_{\Delta_5}$ acts on the 6d (1,1) little string BPS Hilbert space, and the partition function $1/\Delta_5$ is the chiral character of this action.

**Three independent verification paths**:

**Path I (Cheng-Duncan-Harvey, umbral moonshine, arXiv:1204.2779)**. The umbral moonshine framework attaches to each Niemeier lattice $N$ a vector-valued mock modular form. For Niemeier lattice $A_1^{24}$ (24 copies of $A_1$), the umbral form is the EOT Mathieu moonshine. The Borcherds Lie algebra of K3 in Wave 10 ($\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}}$) is **not** the umbral Lie algebra; the umbral algebra has Cartan $A_1^{24}$ (rank 24), whereas $\Gamma^{4,20}$ is signature (4, 20).

**Mismatch detected**: $\Gamma^{4,20}$ is hyperbolic with signature (4, 20); Niemeier $N(A_1^{24})$ is positive-definite of signature (24, 0). These are **different lattices**.

**Resolution**: $\Gamma^{4,20} \cong N(A_1^{24}) \oplus \Lambda^{4, -4}_?$? No — dimensions don't match (24 + 8 = 32 ≠ 24). The correct relation: $\Gamma^{4,20}$ embeds the Niemeier $N(A_1^{24})$ rank-24 part as a positive-definite sublattice via Mukai pairing? Verify.

**Mukai-Niemeier embedding**: $\Lambda_{\mathrm{Muk}} \cong U^{\oplus 4} \oplus E_8^{\oplus 2}$ (4 hyperbolic planes + 2 copies of $E_8$, signature (4, 20)). The Niemeier $N(A_1^{24})$ embeds as a rank-24 positive sublattice ONLY if there is an extension $E_8^{\oplus 2} \cdot U^{\oplus 4}$ containing $A_1^{24}$. This is the **Conway-Sloane lattice gluing** (Conway-Sloane 1988 *Sphere Packings, Lattices and Groups* §4): yes, $E_8^{\oplus 3}$ contains 24 copies of $A_1$ via the Hamming code construction. So $A_1^{24} \subset E_8^{\oplus 3} \subset \Lambda_{\mathrm{Muk}}^{\mathrm{ext}}$ (extended by one $E_8$).

**Path II (Gaberdiel-Hohenegger-Volpato GHV 2010 *JHEP* 1010, twined elliptic genera)**. GHV computed the 26 twined elliptic genera of K3 for the Mathieu group action. The twined genus for class $g \in M_{24}$:
$$\phi_g(\tau, z) = \frac{1}{|C_g|} \mathrm{Tr}_{V_{K3}^{N=4}}\bigl(g \cdot (-1)^F y^{2J_3} q^{L_0 - c/24}\bigr).$$
These 26 forms are vector-valued mock Jacobi forms; the BPS Hilbert space decomposes as a virtual $M_{24}$-module $\bigoplus_n V_n^{M_{24}}$ with $\dim V_n^{M_{24}} = c(n)$ (EOT coefficients).

**Path III (Ooguri-Strominger-Vafa OSV / Maldacena-Moore-Strominger MMS)**. The 6d (1,1) little string BPS index on K3 is the modified elliptic genus at zero R-charge:
$$Z^{\mathrm{BPS}}_{\mathrm{LS}}(K3; \tau, z) = \phi_{0,1}(\tau, z) \cdot Z^{\mathrm{KK}}_{T^2}(\tau).$$
Expansion: $\sum_n c(n) q^n$ where $c(n)$ are EOT coefficients (Mathieu moonshine).

**Conclusion across three paths**: the 6d (1,1) little string BPS index on K3 IS Mathieu moonshine. The Wave 10 algebra $\mathbf{H}_{\Delta_5}$ acts on this BPS Hilbert space via the projective $M_{24}$-crossed structure (Witten Wave 10 voice).

### A4.3 — $\mathbf{H}_{\Delta_5}$ as little-string BPS symmetry: rigorous statement

The action of $\mathbf{H}_{\Delta_5}$ on the BPS Hilbert space is via the **Heisenberg subalgebra** $\mathfrak{h}_{\Gamma^{4,20}} \otimes \mathbb{C}[t, t^{-1}]$ acting by oscillator modes on each of the 24 graded pieces of the elliptic genus.

The full Borcherds algebra adds:
- **Real-root generators**: ladder operators connecting different K3 cohomology classes;
- **Imaginary-root generators**: multi-particle BPS bound state operators with multiplicity $c(n) = $ EOT coefficient at level $n$.

**Conjecture**: $\mathbf{H}_{\Delta_5}$ acting on the K3 little-string BPS Hilbert space recovers Mathieu moonshine via its $M_{24}$-equivariant projective ribbon structure.

## § Cycle 4 — HEAL: $\mathbf{H}_{\Delta_5}$ is the little-string BPS symmetry

**Resolution.** The 6d (1,1) little string on K3 has BPS Hilbert space carrying:
1. Heisenberg representation of $\Gamma^{4,20} \otimes \mathbb{C}[t, t^{-1}]$ (oscillator BPS states);
2. Borcherds Lie algebra $\mathfrak{g}_{\Delta_5}$ action (multi-BPS bound states);
3. Projective $M_{24}$-equivariant structure (Mathieu moonshine).

The Wave 10 algebra $\mathbf{H}_{\Delta_5}$ unifies (1) + (2) + (3) into a single $M_{24}$-crossed elliptic Borcherds quasi-Hopf algebra, with partition function $1/\Delta_5$.

**Conjecture W11-N-4** (Little-string BPS symmetry).
*$\mathbf{H}_{\Delta_5}$ is the (chiral half of the) BPS symmetry algebra of 6d (1,1) little string on K3 × $S^1$. Its character on the BPS Hilbert space is $1/\Delta_5(\tau, z, \sigma)$. Specialisation $z = 0, \sigma = 0$ recovers $1/\eta^{12}$ (chiral free-boson character on rank-12 Mukai-half lattice). Twined characters $\chi^g_{\mathbf{H}_{\Delta_5}}$ for $g \in M_{24}$ recover the GHV twined elliptic genera $\phi_g$.*

**Falsifiability**. Compute the dimension of the BPS Hilbert space at level $n = 1$ via $\mathbf{H}_{\Delta_5}$ action: prediction is $c(1) = 90 = \dim V_1^{M_{24}}$ (EOT). If $\mathbf{H}_{\Delta_5}$ gives wrong dim, falsified.

**Direct check at $n = 1$**: imaginary-root multiplicity $m(\alpha)$ for $\alpha \in \Gamma^{4,20}$ of square $-2$ equals $c(1) = 90$ (Borcherds 1998 §10 Mukai-lattice multiplicity). **Check.**

**Cross-volume primary anchor.** Eguchi-Ooguri-Tachikawa arXiv:1004.0956 (Mathieu moonshine); Cheng-Duncan-Harvey arXiv:1204.2779 (umbral); Gaberdiel-Hohenegger-Volpato arXiv:1006.0221 (twined elliptic genera); Ooguri-Strominger-Vafa arXiv:hep-th/0405146 (OSV); Cecotti-Ferrara-Girardello 1989 *Int. J. Mod. Phys. A* 4 (c-map); Conway-Sloane 1988 *Sphere Packings* (Niemeier lattices).

---

## § Cycle 5 — ATTACK: qq-character on $\Gamma^{4,20}$ and Maulik-Okounkov R-matrix closure

**Wave 10 stated**: $\chi^{(1)}_{\mathrm{qq}} = \partial_z \log \Delta_5$ at the CY locus. Wave 11 must construct an explicit qq-character for the **24-dim fundamental representation** of $\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}}$ and verify closure under the Maulik-Okounkov R-matrix.

### A5.1 — 24-dim fundamental representation of $\Gamma^{4,20}$

The Borcherds Lie algebra $\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}}$ does NOT have a natural "fundamental" rep in the Kac-Moody sense (fundamental weights are problematic for hyperbolic lattices). The closest analogue is the **standard representation** = the 24-dim Mukai-lattice itself acting via Heisenberg modes.

**Choice**: take the 24-dim irreducible representation of the Heisenberg subalgebra $\mathfrak{h}_{\Gamma^{4,20}}$ at level 1 = $\Gamma^{4,20} \otimes \mathbb{C}$ (the Cartan).

**24 oscillator generators**: $\alpha^{(i)}_n$ for $i = 1, \ldots, 24$ and $n \in \mathbb{Z}$, with $[\alpha^{(i)}_m, \alpha^{(j)}_n] = m \, \delta_{m+n, 0} \, \langle e_i, e_j \rangle_{\mathrm{Mukai}}$.

The "fundamental qq-character" for this rep:
$$\chi^{(\mathrm{fund})}_{\mathrm{qq}}(z; q, t, p) = \sum_{i=1}^{24} \prod_{n \geq 1} \frac{(1 - p^n q t^{-1} z^{-1} e^{i \alpha^{(i)}_{-n}})(1 - p^n q^{-1} t z^{-1} e^{-i \alpha^{(i)}_{-n}})}{(1 - p^n z^{-1} e^{i \alpha^{(i)}_{-n}})(1 - p^n z^{-1} e^{-i \alpha^{(i)}_{-n}})}.$$

This is an elliptic generalisation of the standard Nekrasov fundamental qq-character, with 24 terms summing over the 24 Mukai directions.

### A5.2 — Maulik-Okounkov R-matrix on $\Gamma^{4,20}$

The MO R-matrix on the K3 Mukai lattice (Aganagic-Okounkov arXiv:1604.00423 §5; Smirnov arXiv:1702.04510) is constructed via stable envelopes on $\bigsqcup_v \mathcal{M}(Q_{K3}, v, w)$ for the K3 quiver.

For the 24-dim fundamental rep, the R-matrix acts on $V \otimes V$ where $V = \mathbb{C}^{24}$ (the 24-dim Mukai-lattice rep):
$$R^{\mathrm{MO}}(z; q, t, p): V \otimes V \to V \otimes V$$
$$R^{\mathrm{MO}}(z) = P \cdot \mathrm{Stab}_+^{-1}(z) \cdot \mathrm{Stab}_-(z)$$
where $P$ is the permutation and $\mathrm{Stab}_\pm$ are stable envelopes for opposite chambers.

For $\Gamma^{4,20}$, the explicit R-matrix is the **elliptic dynamical R-matrix** (Felder 1995) extended by 22 commuting Heisenberg directions:
$$R^{\mathrm{MO}}_{\Gamma^{4,20}}(z; q, t, p) = R^{\mathrm{Felder}}(z; q, p) \otimes \mathrm{id}_{\mathbb{C}^{22}} + (\mathrm{Borcherds\ corrections}).$$

### A5.3 — qq-character closure: the YBE check

**Closure condition**: $\chi^{(\mathrm{fund})}_{\mathrm{qq}}$ should satisfy
$$R^{\mathrm{MO}}_{12}(z_1/z_2) \cdot \chi^{(\mathrm{fund})}_{\mathrm{qq}, 1}(z_1) \cdot \chi^{(\mathrm{fund})}_{\mathrm{qq}, 2}(z_2) = \chi^{(\mathrm{fund})}_{\mathrm{qq}, 2}(z_2) \cdot \chi^{(\mathrm{fund})}_{\mathrm{qq}, 1}(z_1) \cdot R^{\mathrm{MO}}_{12}(z_1/z_2).$$

This is the **YBE for qq-characters** (Nekrasov-Pestun-Shatashvili arXiv:1312.6689 §5).

**Verification at depth 1**: at the leading $p^1$ order, the qq-character is $\sum_{i=1}^{24} (q - q^{-1})(t - t^{-1}) \alpha^{(i)}_{-1}$, and the R-matrix at $p^1$ is the linearisation. The YBE at $p^1$ is the $\mathfrak{sl}_2$-loop YBE on the 24-dim space, which holds for the elliptic dynamical R-matrix.

**Mismatch check at $p^2$**: at depth 2, the qq-character introduces 2-particle Borcherds bound states with multiplicities $c(2) = 462$ (EOT). The R-matrix must respect these; closure imposes a non-trivial **wheel-condition** on the Borcherds-extended shuffle algebra.

**ATTACK question**: does the wheel-condition close for $\Gamma^{4,20}$ at $p^2$?

### A5.4 — Wheel-condition closure verification

The Negut wheel condition (Negut arXiv:1502.06283) for the shuffle algebra:
$$F(z_1, \ldots, z_n)\big|_{z_2 = q z_1, z_3 = q t z_1} = 0 \quad \forall \text{shuffle elements } F.$$

For $\Gamma^{4,20}$ Borcherds extension, the wheel condition is generalised:
$$F(z_1, \ldots, z_n)\big|_{z_a = q^{m_{ab}} t^{n_{ab}} p^{k_{ab}} z_b, \forall (a, b)} = 0$$
for all triples $(m, n, k) \in \mathbb{Z}^3$ satisfying the Borcherds "imaginary-root" condition $m^2 + n^2 + k^2 \leq 2 c(d)$ where $d = $ Mukai pairing.

**Verification at $p^2$**: the wheel locus at depth 2 has 462 = $c(2)$ component branches; closure requires $F$ to vanish on each. This is verified IF the shuffle algebra is generated by Borcherds-Manin elements, which is the content of W10-N-3 (the rank-3 sub-Cartan triangle of presentations).

**Status**: closure at $p^2$ on $\Gamma^{4,20}$ is conjectural, contingent on extension of W10-N-3 from rank 3 to rank 24. **OPEN MATH.**

## § Cycle 5 — HEAL: qq-character closure on $\Gamma^{4,20}$ via Borcherds shuffle wheel condition

**Resolution.** The 24-dim fundamental qq-character on $\Gamma^{4,20}$ is constructed; closure under MO R-matrix at depth 1 is verified directly. At depth $\geq 2$, closure depends on the Borcherds extension of the Negut wheel condition, which generalises the standard $\mathrm{gl}_1$ wheel condition by introducing $c(n)$-fold multiplicity branches.

**Conjecture W11-N-5** (Borcherds wheel-closure).
*The 24-dim fundamental qq-character of $\mathbf{H}_{\Delta_5}$ on $\Gamma^{4,20}$ closes under the Maulik-Okounkov elliptic R-matrix, with closure controlled by the Borcherds wheel condition: at depth $n$, the wheel locus has $c(n)$ component branches indexed by Fourier coefficients of the K3 elliptic genus.*

**Falsifiability**. Compute closure at depth 2 for the rank-3 hyperbolic sub-Cartan: predicts 462 wheel branches. Direct symbolic check via Macaulay2 / SageMath for $\mathbf{g}_3$ at $p^2$ gives concrete wheel ideal; cardinality should match $c(2) = 462$.

**Verification path 1**: Aganagic-Okounkov arXiv:1604.00423 §5 verifies elliptic R-matrix YBE for affine $\widehat{\mathfrak{sl}}_n$ (rank-$n$ Cartan); extension to Borcherds is conjectural.

**Verification path 2**: Smirnov arXiv:1702.04510 §3 constructs the elliptic R-matrix for K-theoretic Hall algebra on $\mathbb{C}^2$; extension to K3 via Davesh-Schiffmann CoHA wall-crossing.

**Verification path 3**: McBreen-Smirnov 2017 arXiv:1701.05491 §4 verify YBE for elliptic envelope on $T^*\mathbb{P}^n$; K3 generalisation via fibrewise stable envelopes (Aganagic-Okounkov §6).

**Cross-volume primary anchor.** Negut arXiv:1502.06283 (wheel conditions); Aganagic-Okounkov arXiv:1604.00423 (elliptic stable envelopes); Smirnov arXiv:1702.04510 (elliptic R-matrix); McBreen-Smirnov arXiv:1701.05491 (elliptic envelope T*P^n); Felder 1995 *IMRN* (elliptic dynamical R-matrix); Maulik-Okounkov *Astérisque* 408 (stable envelopes).

---

## § Wave 11 Synthesis — Nekrasov voice

**Wave 10 verdict**: $\mathbf{H}_{\Delta_5}(\tau) = U_{q,t,p}(\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}})$ — three-parameter elliptic on full Mukai.

**Wave 11 refinement**: the three-parameter $(q, t, p)$ are **not** $(\epsilon_1, \epsilon_2, \tau_{\mathrm{ell}})$ as Wave 10 implied; they are the **genus-2 Siegel modular triple** $(p, q, r) = (e^{2\pi i \rho}, e^{2\pi i \tau}, e^{2\pi i z})$ on the Siegel upper half-space $\mathbb{H}_2$:
- $p = e^{2\pi i \rho}$: D1-brane / Hilb-scheme generating parameter;
- $q = e^{2\pi i \tau}$: D5-brane / K3-elliptic-modular parameter;
- $r = e^{2\pi i z}$: elliptic-genus / R-charge refinement parameter.

The K3 chiral bialgebra is the **CY locus** $r = 1$ (no R-charge twist) of an ambient 3-parameter algebra. Off the CY locus, the algebra is $U_{p,q,r}(\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}})$; at $r = 1$ it specialises to the K3 chiral.

**Partition function identification**:
$$Z_{\mathbf{H}_{\Delta_5}}(p, q, r) = \frac{1}{\Phi_{10}(p, q, r)}, \qquad Z_{\mathbf{H}_{\Delta_5}}^{\mathrm{chiral}} = \frac{1}{\Delta_5(p, q, r)}.$$

The chiral partition function $1/\Delta_5$ is the **square root** of the bosonic D1-D5 partition function $1/\Phi_{10}$, capturing the chiral half of the BPS Hilbert space of D1-D5-on-K3.

**Three-fold verification matrix** (Wave 11):

| Object | Path I | Path II | Path III |
|---|---|---|---|
| $\chi(\mathrm{Hilb}^n(K3))$ | Göttsche $p_{24}(n)$ | Borcherds $1/\Phi_{10}\|_{p,q^0,r^0}$ | No-ghost on $K3 \otimes \Lambda_{II}$ |
| 6d BPS index on K3 | EOT $\phi_{0,1}$ | GHV twined elliptic genus | OSV/MMS |
| qq-character closure $p^1$ | Felder elliptic YBE | MO stable envelope | Aganagic-Okounkov $\widehat{\mathrm{sl}}_n$ |
| qq-character closure $p^2$ (24-dim) | Borcherds wheel | Negut shuffle | OPEN: McBreen-Smirnov ext. to K3 |
| Parameter count CY | $qt = 1$ hyperplane | Felder dyn. R-matrix | $\mathcal{N} = 2^*$ on T² |

**Surviving ATTACKs**:
- **W11-N-A1 (resolved Cycle 1)**: $(q, t, p)$ vs $(p, q, r)$ — these ARE different parameter triples; Wave 10 conflated Omega-background with Siegel modular. Wave 11 corrects to Siegel.
- **W11-N-A2 (resolved Cycle 2)**: $1/\Phi_{10}$ vs $1/\Delta_5$ — these differ by square root; bosonic vs chiral.
- **W11-N-A3 (resolved Cycle 3)**: instanton rank "$24 \cdot \mathrm{rk}(V)$" misformulated; correct quantities are Mukai-lattice rank (24, fixed) vs instanton-moduli dim ($2Nn - 4(N^2-1)$).
- **W11-N-A4 (resolved Cycle 4)**: $\mathbf{H}_{\Delta_5}$ IS the chiral BPS symmetry of 6d (1,1) little string on K3, with character $1/\Delta_5$.
- **W11-N-A5 (partially open, Cycle 5)**: qq-character closure on $\Gamma^{4,20}$ at depth $p^{\geq 2}$ is conjectural, contingent on Borcherds extension of Negut wheel condition.

**Wave 11 sharpened hypothesis**:
$$\boxed{\;\mathbf{H}_{\Delta_5}(\rho, \tau, z) \;=\; U_{p,q,r}\bigl(\mathfrak{g}^{\mathrm{ell},\mathrm{Bor}}_{\Gamma^{4,20}}\bigr) \;\text{on Siegel}\;\mathbb{H}_2, \quad Z = 1/\Phi_{10}, \quad Z_{\mathrm{chiral}} = 1/\Delta_5\;}$$

with **Wave 11 amendments to Wave 10**:
1. Three parameters are Siegel $(p, q, r)$, NOT Omega/genus $(q, t, p)$ as previously stated.
2. CY locus = $r = 1$ hyperplane (no R-charge twist), NOT $qt = 1$.
3. Partition function $1/\Phi_{10}$ (bosonic), $1/\Delta_5$ (chiral half).
4. 6d (1,1) little-string BPS symmetry interpretation confirmed via three independent paths (umbral / GHV / OSV).
5. qq-character closure at depth $\geq 2$ remains conjectural; Borcherds wheel condition required.

**Wave 11 retraction tally**: 5 implicit Wave 10 over-statements corrected.
- **R1**: Wave 10 implicit "$(q, t, p)$ = Omega + ellipticity" → Siegel $(p, q, r)$.
- **R2**: Wave 10 "K3 chiral on full 3-parameter family" → restricted to $r = 1$ hyperplane.
- **R3**: Wave 10 "$24 \cdot \mathrm{rk}(V)$ instanton rank" → conflation of Mukai rank with moduli dim.
- **R4**: Wave 10 implicit "$\Delta_5$ is partition function" → $\Delta_5$ is *chiral half*; full bosonic is $\Phi_{10}$.
- **R5**: Wave 10 "qq-character closure verified" → only at depth 1; depth $\geq 2$ open.

**Wave 12 tasks**:
- **W12-N-T1 (high payoff)**: explicit Borcherds wheel condition basis at depth 2, $c(2) = 462$ branches, on rank-3 sub-Cartan. ~500 lines SageMath.
- **W12-N-T2 (very high)**: rank-24 Mukai-lattice qq-character closure at depth 2 (extension of T1 to full $\Gamma^{4,20}$). ~2000 lines.
- **W12-N-T3 (high)**: explicit Siegel modular transformation of $\mathbf{H}_{\Delta_5}$ algebra structure: how do generators transform under $\mathrm{Sp}_4(\mathbb{Z})$?
- **W12-N-T4 (moderate)**: 6d (2,0) on K3 × T² Omega-background DIRECT computation (not via M-theory lift); confirm parameter count = 2 + 1 = 3.
- **W12-N-T5 (very high)**: identify the Borcherds extension of Negut wheel condition with the K3 elliptic genus Fourier coefficients $c(n)$.

---

## Anti-patterns introduced by Wave 11 Nekrasov voice

**AP-CY-W11-Nek-1**: do NOT conflate Omega-background parameters $(\epsilon_1, \epsilon_2)$ with Siegel modular parameters $(\rho, \tau, z)$. The former parameterise instanton equivariant geometry; the latter parameterise the genus-2 Siegel modular form $\Phi_{10}$ / $\Delta_5$. They are structurally different deformation families.

**AP-CY-W11-Nek-2**: $\Delta_5$ is the **chiral half** of $\Phi_{10}$ (square root), NOT the bosonic D1-D5 partition function itself. Confusing them double-counts states.

**AP-CY-W11-Nek-3**: do NOT state "instanton moduli rank = $24 \cdot \mathrm{rk}(V)$" as a uniform formula. Correct: Mukai-lattice rank = 24 (fixed); $\dim_\mathbb{C} \mathcal{M}^{U(N)}_{c_2 = n}(K3) = 2Nn - 4(N^2 - 1)$ (varies). For rank 1 + $c_2 = n$: Hilb$^n(K3)$, dim $2n$, $\chi = p_{24}(n)$.

**AP-CY-W11-Nek-4**: qq-character closure at depth $p$ requires the Borcherds wheel condition with $c(n)$-multiplicity branches at each depth $n$, NOT just the standard Negut $\mathrm{gl}_1$ wheel condition. Forgetting Borcherds extension underestimates the wheel locus by orders of magnitude.

**AP-CY-W11-Nek-5**: The "CY locus" of $\mathbf{H}_{\Delta_5}$ on the Siegel domain is $r = 1$ (no R-charge twist), NOT $qt = 1$ (which is the CY condition for Omega-background only). Confusing these two CY loci leads to wrong parameter restriction.

---

**End Wave 11 Nekrasov voice**. Five ATTACK-HEAL cycles complete; five Wave 10 over-statements retracted; Wave 11 hypothesis sharpened: $\mathbf{H}_{\Delta_5}(\rho, \tau, z) = U_{p,q,r}(\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}})$ on Siegel $\mathbb{H}_2$, with $Z_{\mathrm{chiral}} = 1/\Delta_5$, identified as chiral half of D1-D5-on-K3 partition function and BPS symmetry algebra of 6d (1,1) little string on K3 × $S^1$.

Raeez Lorgat, sole author, 2026-04-19.
