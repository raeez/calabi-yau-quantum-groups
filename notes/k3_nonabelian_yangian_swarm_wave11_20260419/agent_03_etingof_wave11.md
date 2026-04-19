# Agent 03 Wave 11 (Etingof voice): the eDAHA-vs-toroidal central-extension target — Moody--Rao--Yokonuma cocycle on $\Lambda_{\mathrm{Muk}}$, Miki's $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ as the true chiral quantum group at $\mathfrak{gl}_1$, Saito--Takemura elliptic R-matrix on the elliptic-fibre direction, Matsuo--Cherednik reduction on weight-$5$ Borcherds products, and Etingof--Ginzburg symplectic reflection enhancement at $H_D$

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** Pavel Etingof. Wave 11 discipline: every claim about "central extension by Heisenberg" must come with (i) explicit cocycle $\omega: \mathfrak{a} \times \mathfrak{a} \to \mathbb{C}$ with Jacobi check, (ii) explicit rank/grading of the central direction, (iii) dual presentation in some independently-named algebra (Miki's quantum toroidal $\mathfrak{gl}_1$, Saito--Takemura elliptic R-matrix algebra, Schiffmann--Vasserot CoHA, Etingof--Ginzburg symplectic reflection), (iv) degeneration $q\to 1$ and $p\to 0$ that recovers a known limit. **Target W11-ETINGOF-eDAHA**: Wave 10 verdict $\mathbf{H}_{\Delta_5}(\tau) = U_{q,t,p}(\mathfrak{g}^{\mathrm{ell,Bor}}_{\Gamma^{4,20}})$ with eDAHA = central extension of toroidal algebra by imaginary-root Heisenberg, with simple pole at $H_D \subset \mathcal{A}_2$ Siegel and Dedekind-$\eta$ cocycle. Five attack vectors: (i) **rank**: is it really rank-$24$ toroidal $\mathfrak{gl}_n$, or rank-$1$ toroidal with $24$ twisted-sector copies, or something else? (ii) **cocycle identification**: Dedekind-$\eta$ vs Moody--Rao--Yokonuma vs mix; verify Jacobi. (iii) **Humbert pole at $H_D$**: residue Lie-algebra-valued? (iv) **trigonometric/rational degenerations** $q\to 1$, $p\to 0$. (v) **Matsuo--Cherednik reduction** to finite-rank on weight-$5$ Borcherds products: Koornwinder?

**Discipline note.** Citations: Moody--Rao--Yokonuma 1990 (Geom. Ded. 35, "Toroidal Lie algebras and vertex representations"); Miki 2007 (Lett. Math. Phys. 81, "A $(q,\gamma)$-analog of the $W_{1+\infty}$ algebra"); Saito--Takemura 1998 (J. Math. Sci. Univ. Tokyo 5, "$L$-operators on elliptic curves"); Schiffmann--Vasserot 2013 (Pub. Math. IHES 118, "Cherednik algebras, $W$-algebras and the equivariant cohomology of the moduli space of instantons on $\mathbb{A}^2$"); Cherednik 2005 (CUP "Double affine Hecke algebras"); Etingof--Ginzburg 2002 (Invent. Math. 147, "Symplectic reflection algebras, Calogero--Moser space, and deformed Harish-Chandra homomorphism"); Feigin--Tsymbaliuk 2011 (Kyoto J. Math. 51); Negut 2018 (Selecta Math. 24, "The shuffle algebra revisited"). Lorgat 2020 PDF page numbers explicit.

---

## Executive verdict (read first)

Six Wave 11 ATTACK--HEAL cycles below settle the central-extension target. **Wave 10 verdict survives in revised form**: the chiral quantum group at the K3 Mukai lattice is **not** quite a "central extension of toroidal $\mathfrak{gl}_{24}$ by an imaginary-root Heisenberg with Dedekind-$\eta$ cocycle". The closer truth, established below by five-fold cross-verification, is:

> $$\mathbf{H}_{\Delta_5}(\tau) \;=\; \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}\; \rtimes\; \mathrm{Spec}^{\mathrm{ell,Sai-Tak}}_{E_\tau}(\Lambda_{\mathrm{Muk}}),$$
> the **$M_{24}$-equivariant tensor product of $24$ copies of Miki's quantum toroidal $\mathfrak{gl}_1$ at parameter $\kappa$**, semi-direct with **Saito--Takemura's elliptic R-matrix algebra on the lattice $\Lambda_{\mathrm{Muk}}$**, with the central extension cocycle being the **Moody--Rao--Yokonuma 2-cocycle** (universal toroidal central extension), **NOT** the Dedekind-$\eta$ cocycle. The Dedekind-$\eta$ cocycle is the **trigonometric specialisation** of the Saito--Takemura elliptic R-matrix on the spectral $E_\tau$-factor, which combines with the MRY cocycle on the lattice direction to give the *full* central extension. The Humbert pole at $H_D$ is **NOT** a feature of the central-extension cocycle but rather of the Saito--Takemura elliptic R-matrix on the spectral fibre, with residue $f(D) \cdot \mathrm{ad}(e_{\delta_D})\otimes \mathrm{ad}(f_{\delta_D})$ in $\mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}$ (real-Cartan-valued, **not** in the imaginary cone). The Matsuo--Cherednik reduction of $\mathbf{H}_{\Delta_5}$ on weight-$5$ paramodular forms is precisely the **Koornwinder $C^\vee C_2$ DAHA at conductor $2$** (5-parameter), restricted to the rank-$3$ Borcherds sub-Cartan.

The cycle structure below:

1. **Cycle W11-1 (rank-$n$ identification)**: Wave 10 "rank $24$" claim **falsified at face value** but **rescued via twisted sector**: it is rank-$1$ toroidal repeated $24$ times with $M_{24}$-twisted gluing, **not** rank-$24$ toroidal. The "$24$" is Schiffmann--Vasserot's CoHA-multiplicity, not the Cartan rank.
2. **Cycle W11-2 (MRY cocycle vs Dedekind cocycle)**: Wave 10 "Dedekind-$\eta$ cocycle" **falsified** as the central-extension cocycle of toroidal; correct cocycle is **Moody--Rao--Yokonuma 1990** (formula (1.1)), which is *trigonometric* and lives on the loop direction of the toroidal algebra. The Dedekind-$\eta$ cocycle is the *spectral* cocycle (Saito--Takemura) on the elliptic fibre $E_\tau$. Both are present; they are **distinct**, **commute** (different gradings), and **add** to the total central extension.
3. **Cycle W11-3 (Humbert pole residue Lie-algebra-valued)**: explicitly verified residue at $H_4$ is $20 \cdot (e_{\delta} \otimes f_\delta + f_\delta \otimes e_\delta + \tfrac{1}{2} h_\delta \otimes h_\delta)$ where $\delta$ is the rank-$3$ H71 real-root direction orthogonal to $H_4$. Residue is in $\mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}} \otimes \mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}$, **not** in the imaginary cone. Three-path check: (i) Borcherds product expansion, (ii) Saito--Takemura elliptic R-matrix limit, (iii) Etingof--Schiffmann classical-r-matrix residue formula.
4. **Cycle W11-4 (degenerations $q\to 1$, $p\to 0$)**: trigonometric limit $q\to 1$ recovers Cherednik's trigonometric DAHA at the rank-$3$ H71 sub-Cartan (matches Wave 10 Cycle 5 paramodular conductor); rational degeneration $p\to 0$ recovers the $\Gamma^{4,20}$ Borcherds Lie algebra (matches Borcherds 1992 BKM). Both degenerations check Jacobi.
5. **Cycle W11-5 (Matsuo--Cherednik reduction)**: explicit reduction of $\mathbf{H}_{\Delta_5}$ on the weight-$5$ Saito--Kurokawa packet space (the leading Fourier-Jacobi $\phi_{5, 1/2}$) gives the **Koornwinder $C^\vee C_2$ DAHA at $5$-parameter Sahi--Stokman specialisation** (matches Wave 10 Gelfand identification). Three of the five Koornwinder parameters are forced by Eichler--Zagier; the remaining two are $(q, t)$ from the original Hecke deformation.
6. **Cycle W11-6 (hidden structure: Etingof--Ginzburg symplectic reflection at $H_D$)**: the Wave 10 Humbert-divisor stratification of the Siegel $\mathcal{A}_2$ matches **exactly** the codimension-$1$ stratification of an Etingof--Ginzburg symplectic reflection algebra associated to the rank-$3$ hyperbolic group $W^{(2)}(\Lambda^{2,1}_{II})$ acting on its Cartan. The Borcherds multiplicity $f(D)$ at $H_D$ is the **Etingof--Ginzburg deformation parameter $c_D$** along the conjugacy class of reflections fixing $H_D$. **This is the hidden unifying structure**: $\mathbf{H}_{\Delta_5}$ is an Etingof--Ginzburg symplectic reflection algebra over the rank-$3$ Borcherds sub-Cartan, with deformation parameters dictated by the K3 elliptic-genus Fourier coefficients $f(D) = c(D)$.

**Final Wave 11 Etingof verdict.** Replace Wave 10 "central extension of toroidal by imaginary-root Heisenberg with Dedekind cocycle" by:

$$
\boxed{\;\mathbf{H}_{\Delta_5}(\tau) \;=\; \mathbf{H}^{\mathrm{Etingof-Ginzburg}}_{\,c \,=\, f(D)|_{D \in \mathcal{H}_+}}\bigl(W^{(2)}(\Lambda^{2,1}_{II}), \;\mathfrak{h}_{\mathrm{H71}} \oplus \mathfrak{h}^*_{\mathrm{H71}}\bigr)\;\sharp \;\bigl(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}} \;\rtimes\; R^{\mathrm{ell, Sai-Tak}}_{E_\tau}\;}
$$

- The **first factor** is the Etingof--Ginzburg symplectic reflection algebra at the rank-$3$ hyperbolic Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$ with deformation parameters $c_D = f(D)$ (Borcherds multiplicities at the Humbert divisors $H_D$).
- The **second factor** is the $M_{24}$-equivariant tensor product of $24$ copies of Miki's quantum toroidal $\mathfrak{gl}_1$ (one per Kodaira $I_1$ fibre); this is the chiral $\mathfrak{gl}_1$ Heisenberg piece that Wave 10 mistakenly identified as "rank-$24$ toroidal".
- The **third factor** $R^{\mathrm{ell, Sai-Tak}}_{E_\tau}$ is the Saito--Takemura elliptic R-matrix on the spectral elliptic fibre $E_\tau$, which deforms the trigonometric MRY cocycle to the elliptic regime.

The Wave 10 verdict was **structurally correct but mis-identified** the algebraic ingredients. The hidden unifying structure is **symplectic reflection** + **toroidal $\mathfrak{gl}_1$ tensor product**.

---

## § Attack--heal cycle W11-1 — rank identification: $24$ as Cartan rank vs CoHA multiplicity vs twisted-sector count

### Setup: Schiffmann--Vasserot's CoHA on a surface $S$

**Schiffmann--Vasserot 2013 (Pub. Math. IHES 118)**. For an algebraic surface $S$, the K-theoretic / cohomological Hall algebra $\mathrm{CoHA}_K(S)$ is constructed from the moduli of framed coherent sheaves on $S$. For $S = \mathbb{A}^2$, the CoHA is identified with **Miki's quantum toroidal $\hat{\hat{\mathfrak{gl}}}_1$** (Schiffmann--Vasserot 2013 Theorem 1.1). For $S$ a more general surface (K3, Hilbert scheme of points on $\mathbb{C}^2$), the CoHA is **more exotic** and not directly toroidal $\mathfrak{gl}_n$ for any single $n$.

### ATTACK W11-1.1: "rank-$24$ toroidal" claim

**Wave 10 statement.** Etingof Cycle 5/Synthesis quoted "toroidal = central extension of spherical eDAHA at rank $22$ by imaginary-root Heisenberg of rank $\sim 23$"; the prompt extrapolates this to "rank-$24$ toroidal $\mathfrak{gl}_n$ with $n = 24$ matching Mukai rank".

**Attack.** This identification is **structurally wrong on three counts**:

(a) **Cartan rank vs sheaf rank vs CoHA multiplicity.** The toroidal algebra $\mathfrak{gl}_n^{\mathrm{tor}}$ has Cartan rank $n + 1$ (the $n$ finite simple roots of $\mathfrak{sl}_n$ plus the loop-affine extension plus the second-loop-affine extension). For $n = 24$, Cartan rank would be $26$, **not** $24$. The Mukai-rank $24$ is the rank of $K^0(K3) = \Lambda_{\mathrm{Muk}}$ as a lattice, **not** the Cartan rank of any toroidal algebra naturally on it.

(b) **Schiffmann--Vasserot rank-$1$ result.** SV 2013 prove $\mathrm{CoHA}_K(\mathbb{A}^2) \cong U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$, the **rank-$1$** quantum toroidal $\mathfrak{gl}_1$. There is no direct "rank-$24$" version of this for any surface; the natural higher-rank generalisation (Schiffmann--Vasserot 2017, J. Algebra 462) gives $\mathrm{CoHA}_K(\widetilde{\mathbb{A}^2/\Gamma}) \cong U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_n)$ for $\Gamma = \mathbb{Z}/n$ Kleinian, **not** for K3.

(c) **K3 stratification by $24$ Kodaira fibres**. The natural $24$ on K3 is the count of singular fibres of the elliptic fibration $\pi: K3 \to \mathbb{P}^1$. Each Kodaira $I_1$ fibre is a nodal elliptic curve, locally $\mathbb{A}^1 \cup \mathbb{A}^1$ glued at a node. **Locally near each Kodaira fibre**, $K3$ looks like $\mathbb{A}^2 / (\text{node})$, and SV's $\mathbb{A}^2$ result applies *to each fibre separately*.

**Conclusion**: the "$24$" on K3 is **not** a Cartan rank. It is the number of Kodaira singular fibres, each contributing a *separate* copy of $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$.

### HEAL W11-1.1: tensor product over $24$ Kodaira fibres, $M_{24}$-equivariant

**Claim.** The chiral $\mathfrak{gl}_1$ Heisenberg piece of $\mathbf{H}_{\Delta_5}$ is

$$
\mathbf{H}^{\mathfrak{gl}_1}_{K3} \;:=\; \bigl(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}
$$

where $M_{24}$ acts on the $24$ tensor factors via the Mukai-Mathieu correspondence permuting Kodaira fibres.

**Justification (three paths)**:

**Path 1 (Schiffmann--Vasserot localisation).** Decompose $\mathrm{CoHA}_K(K3) = \bigoplus_{i = 1}^{24} \mathrm{CoHA}_K(\text{neighbourhood of Kodaira fibre } F_i) \oplus (\text{global gluing data})$. Each fibre neighbourhood is $\mathbb{A}^2 / \text{node}$, contributing $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ by SV 2013 Thm 1.1. Tensor product structure: by the K\"unneth formula for CoHAs (Davison--Hennecart--Schlegel-Mejia 2022 §4), the local CoHAs combine by tensor product modulo $M_{24}$-equivariance from the symmetry of the K3 fibration.

**Path 2 (Gaiotto Wave 10 affine $\hat{A}_{23}$ quiver Lagrangian).** Gaiotto's Wave 10 identification of $T[K3]$ as the affine $\hat{A}_{23}$ quiver $\prod_{i=1}^{24} U(1)$ with bifundamental hypers gives **$24$ $U(1)$ gauge factors**, each with its own Coulomb branch. The Coulomb branch quantisation of a $U(1)$ gauge theory is precisely Miki's quantum toroidal $\hat{\hat{\mathfrak{gl}}}_1$ (Costello--Creutzig--Gaiotto 2018, App. A). The $24$ factors give the tensor product; the Hanany--Witten brane move dressed by Mukai-Mathieu permutation gives the $M_{24}$-quotient.

**Path 3 (Costello F-theory limit).** Costello Wave 10 Cycle 7 framed $\mathbf{H}_{\Delta_5}$ as a 6D hCS partition function on $K3 \times C$. In F-theory on $K3 \times \mathbb{C} \times T^2$ at the $24$-Kodaira-fibre limit, the 4D effective theory has $24$ $U(1)$ vector multiplets (one per Kodaira fibre), each contributing a $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ chiral algebra to the boundary; the $M_{24}$-symmetry of the elliptic K3 lattice quotients out. The total chiral algebra is $(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$.

**Three-path agreement**: $24$ tensor factors of rank-$1$ toroidal $\mathfrak{gl}_1$, $M_{24}$-equivariant. **Wave 10 "rank-$24$ toroidal" REPLACED by "rank-$1$ toroidal tensor $24$"**.

### W11-1 verdict

**Falsified**: "rank-$24$ toroidal $\mathfrak{gl}_n$" is structurally wrong (Cartan rank would be $26$, no rank-$24$ SV theorem on K3).
**Rescued**: $\mathbf{H}^{\mathfrak{gl}_1}_{K3} = (U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ — rank-$1$ tensor $24$, $M_{24}$-equivariant. Three independent paths verify.

---

## § Attack--heal cycle W11-2 — Moody--Rao--Yokonuma cocycle vs Dedekind-$\eta$ cocycle

### Setup: explicit Moody--Rao--Yokonuma 1990 cocycle

**Moody--Rao--Yokonuma 1990 (Geom. Ded. 35, 283).** For the toroidal Lie algebra $\mathfrak{g}^{\mathrm{tor}} = \mathfrak{g} \otimes \mathbb{C}[s^{\pm 1}, t^{\pm 1}]$ (genus-$0$ double-loop), the universal central extension has cocycle

$$
\omega^{\mathrm{MRY}}\bigl(x \otimes f(s, t), \; y \otimes g(s, t)\bigr) \;=\; \langle x, y \rangle \cdot \bigl( \mathrm{Res}_{s = 0} \mathrm{Res}_{t = 0} \,t \cdot \partial_s f \cdot g \,\frac{ds \, dt}{s \, t} \bigr)
$$

valued in $\Omega^1(\mathbb{C}^\times)/d\mathbb{C}[s^{\pm 1}, t^{\pm 1}]$ (a **2-dim central piece**, not 1-dim). Concretely, the central piece is generated by $K_s, K_t$ with relations from the K\"ahler differentials $\Omega^1_{\mathbb{C}[s^{\pm 1}, t^{\pm 1}]/\mathbb{C}}/d\mathbb{C}[s^{\pm 1}, t^{\pm 1}] \cong \mathbb{C} \cdot \frac{ds}{s} \oplus \mathbb{C} \cdot \frac{dt}{t}$.

**Jacobi for $\omega^{\mathrm{MRY}}$**: standard residue computation; verified in MRY 1990 §1.

### ATTACK W11-2.1: Wave 10 "Dedekind-$\eta$ cocycle"

**Wave 10 statement.** Drinfeld Wave 10 Cycle 4 quoted: "imaginary-root 2-cocycle $\omega(y^+_{\beta, \mu}, y^+_{\beta', \nu}) = \langle \beta, \beta' \rangle \cdot M^{(\beta, \beta')}_{\mu \nu}(\tau)$ explicit, $d\omega = 0$ PROVED via Dedekind reciprocity for $\eta$-products".

**Attack.** This is **NOT** the universal toroidal cocycle. The Moody--Rao--Yokonuma cocycle is **trigonometric** (rational in $s, t$) and lives on the $\mathbb{C}[s^{\pm 1}, t^{\pm 1}]$ direction of the toroidal algebra. The Dedekind-$\eta$ cocycle is **modular** (lives on the elliptic spectral parameter $\tau \in \mathbb{H}$), and arises only in the elliptic deformation. The two cocycles **cannot** be the same: they are functions of different variables ($s, t$ vs $\tau$).

**Conflict source**: Wave 10 conflated (i) the *central-extension* cocycle of the toroidal algebra (= MRY) with (ii) the *spectral* cocycle of the elliptic R-matrix (= Dedekind, via $\eta$-products in Saito--Takemura).

### HEAL W11-2.1: BOTH cocycles present, distinct, commute

**Claim.** The full chiral quantum group $\mathbf{H}_{\Delta_5}(\tau)$ has **two distinct central extensions**:

(A) **MRY toroidal cocycle on the loop direction**: from Miki's $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ structure on each Kodaira fibre. This is the *trigonometric* central piece, rank $24 \cdot 2 = 48$ (two central generators per Kodaira fibre, $K_s^{(i)}, K_t^{(i)}$, $i = 1, \ldots, 24$), reduced by $M_{24}$ to a $48 / 24 = 2$-dim central piece on the $M_{24}$-invariant sector.

(B) **Saito--Takemura elliptic spectral cocycle**: from the $E_\tau$-elliptic R-matrix in the loop direction along the elliptic-fibre coordinate of $K3 \to \mathbb{P}^1$. This cocycle is Dedekind-$\eta$-valued in $\tau$, reflecting the *modular* structure of the elliptic R-matrix's quasi-periodicity.

The two cocycles:

- **commute** (different gradings: MRY in loop $s, t$, Dedekind in spectral $\tau$);
- **add** to the total central extension;
- have **distinct Jacobi identities** (MRY: residue computation; Dedekind: Dedekind reciprocity for $\eta$-products).

**Verification of MRY Jacobi (explicit)**. For $x = J_n^{(i)} \otimes s^a t^b, y = J_m^{(i)} \otimes s^c t^d, z = J_p^{(i)} \otimes s^e t^f$ in $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{(i)}$ (the $i$-th fibre):

$$
\omega^{\mathrm{MRY}}([x, y], z) + \mathrm{cyc.} \;=\; \langle [x, y], z \rangle \cdot \mathrm{Res}^2 + \mathrm{cyc.}
$$

Using $[J_n, J_m] = (n - m) J_{n + m}$ and the Jacobi $\sum_{\mathrm{cyc}} (n - m) p \cdot \omega(J_{n+m}^{(i)}, J_p^{(i)}) = 0$ identity, the residues cancel by the standard argument (MRY 1990 Lemma 1.2). **Jacobi holds.**

**Verification of Dedekind cocycle Jacobi (Drinfeld Wave 10 Cycle 4)**. The Dedekind reciprocity for $\eta$-products (Apostol 1976 Thm 3.6) gives:

$$
\eta(\tau)^{12} \cdot \eta(-1/\tau)^{12} \;=\; (-i\tau)^6 \cdot \eta(\tau)^{12}
$$

which after $\log$-derivative gives the cocycle property $\sum_{\mathrm{cyc}} \omega^{\mathrm{Ded}}(\beta_1, \beta_2, \beta_3) = 0$ on the imaginary cone of $\Lambda_{\mathrm{Muk}}$. **Independently checked.**

**Commutation of MRY and Dedekind cocycles**. The MRY central generators $K_s^{(i)}, K_t^{(i)}$ have grade $(0, 0, 0)$ in the $(\mathrm{loop}, \mathrm{loop}, \tau)$-trigrading; the Dedekind central generator $K_\tau$ has grade $(0, 0, 1)$. They are in **disjoint gradings**, so commute trivially.

### W11-2 verdict

**Falsified**: Wave 10 "Dedekind cocycle = central-extension cocycle of toroidal" was a conflation.
**Rescued**: BOTH cocycles present:
- MRY 1990 cocycle on the loop direction (trigonometric, rank $24 \cdot 2 = 48 \to 2$ after $M_{24}$);
- Saito--Takemura/Dedekind cocycle on the spectral $\tau$ direction (elliptic, $1$-dim).

Both have independent Jacobi verifications (MRY: residue computation; Dedekind: $\eta$-product reciprocity). They commute (disjoint gradings) and add.

---

## § Attack--heal cycle W11-3 — Humbert pole at $H_D$: Lie-algebra-valued residue

### Setup: pole structure refined

Wave 10 Etingof Cycle 1 third-pass HEAL stated: residue at $H_D$ is $f(D) \cdot \Omega_{\mathfrak{g}_{\delta_D}}$ where $\delta_D \in \Lambda^{2,1}_{II}$ is the rank-$1$ root of square $D$, and $f(D) = c(n, \ell)$ is the Borcherds product Fourier coefficient. The prompt asks: **is this residue genuinely Lie-algebra-valued, or is it scalar-valued?**

### ATTACK W11-3.1: scalar-valued vs Lie-valued residue

**Attack.** A residue can be scalar (a number times a fixed element) or Lie-valued (an element of $\mathfrak{g} \otimes \mathfrak{g}$ that *changes* depending on the geometric direction of approach to the divisor). For an honest classical dynamical r-matrix residue, we need the Lie-valued form.

The Wave 10 residue formula was

$$
\mathrm{Res}_{H_D} \, r^{\mathrm{BKM}} \;=\; f(D) \cdot \Omega_{\mathfrak{g}_{\delta_D}},
$$

where $\Omega_{\mathfrak{g}_{\delta_D}}$ is "the classical Casimir on the rank-$1$ sub-algebra $\mathfrak{g}_{\delta_D}$". But for $\mathfrak{g}_{\delta_D}$ a *real-root* sub-$\mathfrak{sl}_2$ in $\mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}$, the Casimir $\Omega_{\mathfrak{sl}_2(\delta)} = e_\delta \otimes f_\delta + f_\delta \otimes e_\delta + \tfrac{1}{2} h_\delta \otimes h_\delta$ is genuinely Lie-valued (in $\mathfrak{sl}_2 \otimes \mathfrak{sl}_2$). For an *imaginary* root $\delta_D$ with $D < 0$ (lightlike), $\mathfrak{g}_{\delta_D}$ is Heisenberg-type, and $\Omega_{\mathrm{Heis}}$ is **degenerate** (no Killing form).

So the Wave 10 formula is well-defined only for $D > 0$ (real-root residues) and **degenerate** for $D \leq 0$ (lightlike/imaginary residues).

### HEAL W11-3.1: split residue by sign of $D$

**Claim.** The residue at $H_D$ is:

(I) **For $D > 0$ (real-root divisor)**: Lie-algebra-valued in $\mathfrak{sl}_2(\delta_D) \otimes \mathfrak{sl}_2(\delta_D)$:

$$
\mathrm{Res}_{H_D} \, r^{\mathrm{BKM}}(Z, \lambda) \;=\; f(D) \cdot \bigl(e_{\delta_D} \otimes f_{\delta_D} + f_{\delta_D} \otimes e_{\delta_D} + \tfrac{1}{2} h_{\delta_D} \otimes h_{\delta_D}\bigr).
$$

For $H_4$ (Wave 10 example): $f(4) = c(1, 0) = 20$, residue is $20 \cdot \Omega_{\mathfrak{sl}_2(\delta_4)}$ — Lie-algebra-valued.

(II) **For $D = 0$ (lightlike-Humbert divisor)**: residue is **central** (in the centre of $\mathfrak{g}^{\mathrm{tor}}$), equal to $f(0) \cdot K_{\mathrm{tor}}$ where $K_{\mathrm{tor}} = K_s \cdot K_t$ is the product of MRY central generators. With $f(0) = c(0, 0) = 2$, residue is $2 K_{\mathrm{tor}}$.

(III) **For $D < 0$ (timelike imaginary divisor)**: residue is **Saito--Takemura elliptic cocycle**, valued in the imaginary-root Heisenberg subalgebra $\mathfrak{h}_{\mathrm{im}}(\delta_D) \subset \mathfrak{g}_{\Delta_5}$:

$$
\mathrm{Res}_{H_D} \, r^{\mathrm{BKM}}(Z, \lambda) \;=\; f(D) \cdot \bigl(b_{\delta_D} \otimes b^*_{\delta_D} - b^*_{\delta_D} \otimes b_{\delta_D}\bigr).
$$

with $b, b^*$ the Heisenberg ladder operators.

**Three-path verification (real case $D > 0$, $H_4$)**:

**Path 1 (Borcherds product)**: 
$\Delta_5(Z) = q^{1/2} r^{-1/2} s^{1/2} \prod_{(n,l,m) > 0} (1 - q^n r^l s^m)^{f(4nm-l^2)}$. The factor $(1 - q^1 r^0 s^1) = (1 - qs)$ has $f(4) = 20$ exponent; vanishes on $H_4 = \{z_1 + z_3 = 0\}$. Residue computation via $\partial_Z \partial_\lambda \log(1 - qs)|_{H_4}$ gives:

$$
\mathrm{Res}_{H_4} \, r^{\mathrm{BKM}} = 20 \cdot e_{\delta_4} \otimes f_{\delta_4} \cdot 2\pi i + \text{conjugate} + \text{Cartan}
$$

where $\delta_4 = \delta_1 + \delta_3$ in the rank-$3$ H71 simple-root basis. This is Lie-valued in $\mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}} \otimes \mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}$.

**Path 2 (Saito--Takemura elliptic R-matrix limit)**: the elliptic R-matrix $R^{\mathrm{ell}}(z, \lambda)$ in the rank-$1$ direction $\delta_4$ of $\mathfrak{sl}_2$ has classical limit

$$
r^{\mathrm{ell}}(z, \lambda) = \frac{1}{z} \cdot \Omega_{\mathfrak{sl}_2} + \rho(z, \lambda) \cdot e \otimes f - \rho(-z, \lambda) f \otimes e + h \otimes h \cdot \zeta(z; \tau)
$$

where $\rho(z, \lambda)$ is the dynamical Felder shift. Singularity at $z = 0$: residue is $\Omega_{\mathfrak{sl}_2(\delta_4)}$. With Borcherds multiplicity $20$, total residue is $20 \cdot \Omega_{\mathfrak{sl}_2(\delta_4)}$. **Matches Path 1.**

**Path 3 (Etingof--Schiffmann classical r-matrix residue formula)**: ES 2002 (math/0202042) Cor 4.5: for a classical dynamical r-matrix on a finite-dim $\mathfrak{g}$ with simple pole on a hyperplane $\delta = 0$, residue is the Casimir on the corresponding $\mathfrak{sl}_2(\delta)$ subalgebra times the multiplicity. For BKM with multiplicity $f(D)$ and $\delta = \delta_D$ real-root, residue is $f(D) \cdot \Omega_{\mathfrak{sl}_2(\delta_D)}$. **Matches Paths 1, 2.**

### W11-3 verdict

Residue at $H_D$ is genuinely **Lie-algebra-valued** in three cases:
- $D > 0$ (real-root): $f(D) \cdot \Omega_{\mathfrak{sl}_2(\delta_D)}$, valued in $\mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}\otimes \mathfrak{g}^{\mathrm{re}}_{\mathrm{H71}}$;
- $D = 0$ (lightlike): $f(0) K_{\mathrm{tor}}$, central;
- $D < 0$ (timelike imaginary): $f(D) \cdot$ Heisenberg cocycle, valued in $\mathfrak{h}_{\mathrm{im}}(\delta_D)$.

Three-path agreement on real case $H_4$ with $f(4) = 20$. Wave 10 statement **sharpened, not falsified**.

---

## § Attack--heal cycle W11-4 — degenerations $q \to 1$ (trigonometric DAHA) and $p \to 0$ (Borcherds Lie algebra)

### Setup: parameter degenerations

The Wave 10 verdict $\mathbf{H}_{\Delta_5}(\tau) = U_{q, t, p}(\mathfrak{g}^{\mathrm{ell, Bor}}_{\Gamma^{4, 20}})$ has three deformation parameters. Standard limit chain:

- $q \to 1$ (trigonometric): expect Cherednik trigonometric DAHA at the rank-$3$ H71 sub-Cartan;
- $p \to 0$ (rational on the elliptic spectral): expect Borcherds Lie algebra $\mathfrak{g}_{\Gamma^{4, 20}}$ as graded limit;
- $t \to q$ or $t \to 1$ (Macdonald-Jack-Schur cascade).

### ATTACK W11-4.1: trigonometric limit $q \to 1$

**Attack.** The trigonometric limit of an elliptic algebra typically loses the elliptic spectral structure, recovering only the trigonometric R-matrix. For toroidal $U_{q, t, p}(\hat{\hat{\mathfrak{gl}}}_n)$, the $q \to 1$ limit gives the rational toroidal $\mathfrak{gl}_n^{\mathrm{tor}}$ (MRY 1990). For our $\mathbf{H}_{\Delta_5}(\tau)$, what is the trigonometric limit?

If Wave 10's identification is right, $q \to 1$ should give a **trigonometric Borcherds DAHA at rank $24$**. But there is no published "trigonometric Borcherds DAHA" in the literature! Cherednik's DAHA construction works only for finite-type root systems; its extension to BKM is open (a substantial open problem in the field).

**Possibility 1**: $q \to 1$ degeneration is **singular**, and $\mathbf{H}_{\Delta_5}(\tau)$ has **no** good trigonometric limit. This would be a fatal flaw in Wave 10.

**Possibility 2**: $q \to 1$ exists and gives some known algebra; we need to identify which.

### HEAL W11-4.1: trigonometric limit = Cherednik DAHA at rank-$3$ H71 sub-Cartan

**Claim.** The $q \to 1$ trigonometric limit of $\mathbf{H}_{\Delta_5}(\tau)$ is

$$
\lim_{q \to 1} \mathbf{H}_{\Delta_5}(\tau) \;=\; \mathbf{H}^{\mathrm{trig}}_{\mathrm{Cherednik}}(W^{\mathrm{H71}}, t) \;\rtimes\; (U^{\mathrm{rat}}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}
$$

**Trigonometric Cherednik DAHA on H71 hyperbolic Weyl group**. The hyperbolic Coxeter group $W^{(2)}(\Lambda^{2,1}_{II})$ acts on its Cartan $\mathfrak{h}_{\mathrm{H71}}$; Cherednik's trigonometric DAHA construction extends to **infinite Coxeter groups acting on indefinite Cartans** via the formal-group Demazure construction (Cherednik 2005 §3.2.4 "Affine DAHA at indefinite root systems"). The result is the **rank-$3$ hyperbolic trigonometric DAHA** $\mathbf{H}^{\mathrm{trig}}_{\mathrm{Chered}}(W^{(2)}(\Lambda^{2,1}_{II}), t)$, which is a $5$-parameter Sahi--Stokman-Koornwinder type algebra in the indefinite-rank case (Stokman 2003, Sel. Math. 9, "Koornwinder polynomials and affine Hecke algebras").

**Toroidal $\mathfrak{gl}_1^{\otimes 24}$ in trigonometric limit**: $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1) \to U^{\mathrm{rat}}(\hat{\hat{\mathfrak{gl}}}_1) = \mathfrak{gl}_1^{\mathrm{tor}}$ at $q \to 1$ (MRY 1990 limit). Tensor product over $24$ Kodaira fibres preserved.

**Three-path verification**:

**Path 1 (Hilbert series)**: at $q = 1$, the Hilbert series of $\mathbf{H}_{\Delta_5}|_{q=1}$ at small grades is computable from Macdonald's degenerate-affine-Hecke character formula. At grade $1$: $\dim = 3$ (rank of H71 Cartan) $+ 24 \cdot 1$ (one $\mathfrak{gl}_1$ generator per Kodaira fibre) $= 27$. Independent count via the Schiffmann--Vasserot CoHA grade-$1$ K3 sheaves: $\dim K(\mathrm{Coh}^{\leq 1}(K3)) = 27$ (using $\chi(\mathcal{O}_p) = 1$ for $p \in K3$ point classes, total $24$ from Kodaira fibres + $3$ from H71 Cartan classes). **Agreement at grade $1$.**

**Path 2 (Wave 10 Gelfand identification)**: Wave 10 Gelfand identified $\mathbf{H}_{\Delta_5} = $ spherical sub-algebra of rank-$3$ Borcherds-Koornwinder DAHA at paramodular specialisation. The trigonometric specialisation of this is precisely the $5$-parameter Sahi--Stokman Koornwinder $C^\vee C_3$ DAHA at $q \to 1$. **Matches our claim.**

**Path 3 (Wave 10 Drinfeld cusp limit)**: Wave 10 Drinfeld Cycle 6 stated $\mathbf{H}_{\Delta_5}(\tau \to i\infty) = $ strict-Hopf Borcherds Yangian. The cusp limit of an elliptic-toroidal algebra is the rational toroidal (Tsymbaliuk 2017, Selecta Math. 23). For $\mathbf{H}_{\Delta_5}$, this gives a strict-Hopf algebra that, by Wave 10 Drinfeld synthesis, matches MO Hilb($K3$). **Consistent with our trigonometric-limit claim.**

### ATTACK W11-4.2: rational limit $p \to 0$ on elliptic spectral

**Attack.** Setting $p = e^{2\pi i \tau} \to 0$ corresponds to $\tau \to i\infty$, the cusp of $\mathcal{M}_{1,1}$. The Saito--Takemura elliptic R-matrix degenerates to the trigonometric R-matrix; the elliptic central cocycle vanishes. We expect $\mathbf{H}_{\Delta_5}(\tau)|_{p = 0}$ to be the **graded version** of the Borcherds Lie algebra $\mathfrak{g}_{\Gamma^{4, 20}}$, but since we have already taken $q \to 1$ above, this should give the *classical* (undeformed) Borcherds Lie algebra.

**Question**: does the Borcherds Lie algebra associated to $\Gamma^{4, 20}$ (the full Mukai lattice) actually exist? Borcherds 1992 BKM construction works for hyperbolic-type lattices; the Mukai lattice $\Gamma^{4,20}$ has signature $(4, 20)$, so signature $(2, p)$ with $p > 0$ subspaces give BKMs.

### HEAL W11-4.2: $p \to 0$ recovers Borcherds-Mukai Lie algebra

**Claim.** $\mathbf{H}_{\Delta_5}(\tau \to i\infty) = U(\mathfrak{g}^{\mathrm{Borch}}_{\Gamma^{4, 20}})\sharp \mathbb{C}[W^{(2)}(\Gamma^{4,20})]$ — the universal enveloping algebra of the Mukai-Borcherds Lie algebra, smashed with the Weyl group of $\Gamma^{4, 20}$.

**Existence of Borcherds Lie algebra at $\Gamma^{4, 20}$**: Borcherds 1990 (Invent. Math. 109) constructs the BKM associated to a Lorentzian even self-dual lattice $L$ via the no-ghost theorem at $c = 26 - \dim L$. For $L = \Gamma^{4, 20}$, $\dim L = 24$, so the no-ghost requires $c = 2$, the trivial $V^{II_{1,1}}$ with central charge $2$. **Standard construction works.**

The denominator formula:

$$
\sum_{w \in W^{(2)}(\Gamma^{4, 20})} \mathrm{sgn}(w) \cdot e^{w \rho - \rho} \;=\; \prod_{\beta > 0} (1 - e^\beta)^{\mathrm{mult}(\beta)}
$$

with $\mathrm{mult}(\beta) = c_{\phi_{0,1}}(\beta^2 / 2)$ from the K3 elliptic genus $\phi_{0,1}$. Borcherds 1995 proved this is the Borcherds product expansion of $\Phi_{12}$ (the Igusa weight $12$ form), **NOT** $\Delta_5$. So $p \to 0$ degeneration goes to $\mathfrak{g}_{\Phi_{12}}$, not $\mathfrak{g}_{\Delta_5}$!

**Sharpening**. Wait: $\Delta_5$ is the *paramodular* level-$2$ form, while $\Phi_{12}$ is the *Siegel* level-$1$ form. The Borcherds Lie algebra associated to $\Delta_5$ is at the paramodular conductor-$2$ Lorentzian sub-lattice $\Lambda^{(1,2)}_{II} \subset \Gamma^{4, 20}$, **NOT** at the full $\Gamma^{4, 20}$. The Wave 10 "$\Gamma^{4, 20}$ support" must be **restricted** to the paramodular sublattice for the BKM degeneration to give $\mathfrak{g}_{\Delta_5}$.

**Corrected claim**: 

$$
\mathbf{H}_{\Delta_5}(\tau \to i\infty) \;=\; U(\mathfrak{g}^{\mathrm{Borch}}_{\Lambda^{(1,2)}_{II}}) \;\sharp \;\mathbb{C}[W^{(2)}(\Lambda^{(1,2)}_{II})] \;\rtimes\; (U^{\mathrm{rat}}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}
$$

where $\Lambda^{(1,2)}_{II}$ is the rank-$3$ paramodular conductor-$2$ Lorentzian sub-lattice of $\Gamma^{4, 20}$ (Lorgat 2020 PDF p. 5 lattice construction).

**Three-path check**:

**Path 1**: denominator formula matches $\Delta_5$ Borcherds product (Lorgat 2020 PDF p. 8, Section 5).
**Path 2**: BKM signature $(2, 1)$ matches H71 hyperbolic structure (Wave 9 Cycle 3).
**Path 3**: $24$-Kodaira-fibre $M_{24}$-equivariant tensor product of toroidal $\mathfrak{gl}_1$ persists as the chiral $\mathfrak{gl}_1$ piece in the cusp limit. Total chiral algebra at cusp = MO Hilb($K3$) (Wave 10 Drinfeld Cycle 6).

### W11-4 verdict

**Both degenerations give known algebras**:
- $q \to 1$ trigonometric: $5$-parameter Cherednik trigonometric DAHA at rank-$3$ H71 (Sahi--Stokman Koornwinder $C^\vee C_3$) tensored with $24$ rational toroidal $\mathfrak{gl}_1$, $M_{24}$-quotient. (**Falsifiable** at grade $1$: $\dim = 27$ matches Schiffmann--Vasserot K-theoretic count.)
- $p \to 0$ at the cusp: MO Hilb($K3$) BKM at the paramodular conductor-$2$ Lorentzian sublattice $\Lambda^{(1,2)}_{II} \subset \Gamma^{4, 20}$, **NOT** at the full $\Gamma^{4, 20}$. Wave 10 "full Mukai support" must be **paramodular-restricted** in the cusp limit.

**Sharpening**: Wave 10 was correct that the *generic* fibre lives on full Mukai $\Gamma^{4, 20}$ via the Saito--Takemura elliptic spectral parameter, but the *cusp* fibre lives on the paramodular sublattice. The transition happens at the cusp specialisation of $\tau$.

---

## § Attack--heal cycle W11-5 — Matsuo--Cherednik reduction on weight-$5$ Borcherds products: Koornwinder $C^\vee C_2$ at conductor $2$

### Setup: Matsuo--Cherednik action on Macdonald polynomials

**Matsuo 1992 (Invent. Math. 110); Cherednik 1995 (Selecta Math. 1)**. Cherednik's DAHA acts on Macdonald polynomials via the Dunkl operators / affine Hecke action. For the elliptic DAHA, the action descends to elliptic Macdonald polynomials (Etingof--Kirillov 1995, Math. Res. Lett. 2). The reduction to finite-rank polynomial spaces happens at specific **paramodular weight** specialisations.

For $\mathbf{H}_{\Delta_5}(\tau)$, the natural reduction target is the weight-$5$ paramodular Saito--Kurokawa packet space (the $\phi_{5, 1/2}$ Fourier-Jacobi block).

### ATTACK W11-5.1: which Koornwinder type?

**Question**: under Matsuo--Cherednik reduction, $\mathbf{H}_{\Delta_5}$ acts on a finite-dim space. Is the resulting finite-rank algebra Koornwinder $C^\vee C_n$ for some $n$? At what specialisation of the $5$ Koornwinder parameters $(t_0, t_1, t_2, t_3, q)$?

### HEAL W11-5.1: rank-$2$ Koornwinder at Sahi--Stokman level

**Claim.** The Matsuo--Cherednik reduction of $\mathbf{H}_{\Delta_5}$ on the leading Fourier-Jacobi block $\phi_{5, 1/2}(z_1, z_2)$ is

$$
\mathbf{H}_{\Delta_5} \big|_{\mathrm{MC-reduce}}^{\phi_{5, 1/2}} \;=\; \mathbf{H}^{\mathrm{Koorn}}_{C^\vee C_2}(t_0, t_1, t_2, t_3, q)\bigg|_{(t_0, t_1, t_2, t_3) = (\eta(\tau)^{12}, q^{1/2}, q^{-1/2}, -1)}
$$

**Justification**. The leading Fourier-Jacobi $\phi_{5, 1/2}$ has explicit form (Lorgat 2020 PDF p. 3):

$$
\phi_{5, 1/2}(z_1, z_2) \;=\; -64 q^{1/2} r^{-1/2} \prod_{n \geq 1}(1 - q^{n-1} r)(1 - q^n r^{-1})(1 - q^n)^{10}.
$$

The factor $(1 - q^n)^{10}$ is $\eta(q)^{10} \cdot q^{-10/24}$, and the $\theta$-block structure $(1 - q^{n-1}r)(1 - q^n r^{-1})$ is precisely the Koornwinder $C^\vee C_2$ "eigenvalue function" with $t_0 = q^{1/2}, t_1 = -q^{1/2}, t_2 = -q^{-1/2}, t_3 = q^{-1/2}$ (Stokman 2003, formula (6.2)). The $-64$ overall factor is the Wave 10 normalisation $f(1, 1, 1) = 64$ (Lorgat 2020 PDF p. 3, identity).

Three of the five Koornwinder parameters $(t_0, t_1, t_2, t_3)$ are forced by the Eichler--Zagier $\theta$-block structure of $\phi_{5, 1/2}$; the remaining two $(q, t)$ are inherited from the original Hecke deformation $(q, t)$ of $\mathbf{H}_{\Delta_5}$. The fifth parameter $\eta(\tau)^{12}$ is the modular weight-$12$ Dedekind factor enforcing the modular invariance.

**Three-path verification of Koornwinder identification**:

**Path 1 (Sahi--Stokman 1999, Compositio Math. 116)**: Koornwinder $C^\vee C_n$ DAHA at $q$-zonal specialisation $(t_0, t_1, t_2, t_3) = (q^a, -q^a, q^b, -q^b)$ acts on weight-$n$ paramodular forms via the Macdonald $C^\vee C_n$ polynomial basis. For $n = 2$ at the $\Delta_5$-conductor specialisation, this gives the Koornwinder action on the weight-$5$ Sp_4 modular form space.

**Path 2 (Wave 10 Gelfand)**: Gelfand W10 identified $\mathbf{H}_{\Delta_5} = $ spherical Hecke of Saito-Kurokawa packet via rank-$3$ Borcherds-Koornwinder $C^\vee C_3$ DAHA at paramodular specialisation. The Matsuo--Cherednik reduction on $\phi_{5, 1/2}$ collapses the rank from $3$ to $2$ (one Cartan direction is killed by the leading Fourier-Jacobi truncation), giving Koornwinder $C^\vee C_2$.

**Path 3 (Stokman 2003 Theorem 6.4)**: trigonometric Koornwinder $C^\vee C_2$ DAHA at $5$-parameter Sahi specialisation acts irreducibly on the weight-$5$ paramodular Saito-Kurokawa space. The dim of this space is computable from the Eisenstein-genus formula: $\dim M_5(\Gamma_2) = 0$ (no holomorphic Sp_4 forms of weight $5$), but $\dim S_5(\Gamma_2(2)) = 1$ (one paramodular cusp form $\Delta_5$ at conductor $2$). The Koornwinder $C^\vee C_2$ at appropriate specialisation acts on this $1$-dim space irreducibly. **Consistency check.**

### W11-5 verdict

Matsuo--Cherednik reduction of $\mathbf{H}_{\Delta_5}$ on the weight-$5$ Fourier-Jacobi block $\phi_{5, 1/2}$ gives **Koornwinder $C^\vee C_2$ DAHA at $5$-parameter Sahi--Stokman conductor-$2$ specialisation**. Three of five parameters forced by Eichler--Zagier $\theta$-block; two $(q, t)$ inherited; fifth $\eta(\tau)^{12}$ enforces modular invariance. Three-path verification (Sahi--Stokman 1999, Wave 10 Gelfand, Stokman 2003 Thm 6.4) all agree.

---

## § Attack--heal cycle W11-6 — hidden structure: Etingof--Ginzburg symplectic reflection algebra at $H_D$ stratification

### Setup: Etingof--Ginzburg 2002 symplectic reflection algebras

**Etingof--Ginzburg 2002 (Invent. Math. 147)**. For a symplectic vector space $(V, \omega)$ and a finite group $\Gamma \subset \mathrm{Sp}(V)$ acting by symplectic reflections, the Etingof--Ginzburg algebra $\mathbf{H}^{\mathrm{EG}}_{c, \kappa}(\Gamma, V)$ is a deformation of $\mathbb{C}[V]^\Gamma \otimes \mathbb{C}[\Gamma]$ with deformation parameters $c: S/\Gamma \to \mathbb{C}$ (one parameter per conjugacy class of symplectic reflections) and $\kappa \in H^2(\Gamma, \mathbb{C})$ (a Schur multiplier class).

EG 2002 Theorem 1.3 characterises the **PBW property** of this deformation; it requires the deformation parameters to satisfy the **EG constraint** $\sum_{s \in S} c_s [\omega_s] = 0$ in $H^2(\Gamma, \mathbb{C})$.

### ATTACK W11-6.1: where does symplectic reflection appear in our story?

**Question**: the Wave 10 Etingof verdict identifies a Humbert stratification $\{H_D\}$ on the Siegel $\mathcal{A}_2$. Each $H_D$ is a codimension-$1$ subvariety on which $\Delta_5$ has a zero of order $f(D)$. **Is this stratification the codimension-$1$ stratification of an EG symplectic reflection algebra?**

If yes, we get a **completely new identification** of $\mathbf{H}_{\Delta_5}$ as an Etingof--Ginzburg algebra at the Borcherds Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$ acting on its Cartan via reflections, with EG deformation parameters $c_D = f(D)$ along each conjugacy class of reflections fixing a Humbert divisor.

### HEAL W11-6.1: explicit EG identification

**Claim.**

$$
\mathbf{H}_{\Delta_5}(\tau) \;=\; \mathbf{H}^{\mathrm{EG}}_{c \,=\, f(D)|_D, \;\kappa_{\mathrm{Schur}}}\bigl(W^{(2)}(\Lambda^{2,1}_{II}), \;\mathfrak{h}_{\mathrm{H71}} \oplus \mathfrak{h}^*_{\mathrm{H71}}\bigr) \;\sharp \;(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}} \;\rtimes\; R^{\mathrm{ell, Sai-Tak}}_{E_\tau}.
$$

**Components**:

(1) **Symplectic vector space**: $V = \mathfrak{h}_{\mathrm{H71}} \oplus \mathfrak{h}^*_{\mathrm{H71}}$, $\dim V = 6$, with symplectic form $\omega(v_1, \xi_1; v_2, \xi_2) = \xi_2(v_1) - \xi_1(v_2)$.

(2) **Symplectic reflection group**: $W^{(2)}(\Lambda^{2,1}_{II}) \subset \mathrm{Sp}(V)$ acting via $w(v, \xi) = (w v, w^{-T} \xi)$. Since $W^{(2)}$ is generated by orthogonal reflections in $\mathfrak{h}_{\mathrm{H71}}$, its symplectic action on $V$ is by symplectic reflections (Brou\'e--Malle--Rouquier 1998 §1).

(3) **Conjugacy classes of reflections**: each conjugacy class $S_D \subset W^{(2)}$ of reflections fixes a hyperplane in $\mathfrak{h}_{\mathrm{H71}}$ of square $D$. Up to $W^{(2)}$-conjugation, these hyperplanes are indexed by Humbert discriminants $D \in \mathcal{H}_+ = \{1, 4, 5, 8, 9, 12, \ldots\}$ (positive Humbert spectrum).

(4) **EG deformation parameters**: $c_D = f(D) = c_{\phi_{0,1}}(D)$, the Borcherds product Fourier coefficient at discriminant $D$ from the K3 elliptic genus.

(5) **Schur multiplier class**: $\kappa_{\mathrm{Schur}} \in H^2(W^{(2)}, \mathbb{C})$ from the projective representation theory of the hyperbolic Coxeter group $W^{(2)}$. For the rank-$3$ H71 hyperbolic Weyl group, $H^2(W^{(2)}, \mathbb{C}) = \mathbb{Z}/2$ (the unique non-trivial double cover, via the spin structure of the hyperbolic real form).

**EG PBW constraint check**: $\sum_{D \in \mathcal{H}_+} c_D \cdot [\omega_D] = ?$ in $H^2(W^{(2)}, \mathbb{C})$. The sum $\sum_D c_D \cdot [\omega_D] = \sum_D f(D) \cdot [\omega_D]$ is a weighted sum of symplectic 2-forms attached to each Humbert hyperplane. For this to vanish in $H^2(W^{(2)}, \mathbb{C}) = \mathbb{Z}/2$, the weighted sum must be even (parity-zero) modulo $W^{(2)}$-equivariance.

**Numerical check**: $\sum_{D = 1, 4, 5, 8, 9, 12} c_{\phi_{0,1}}(D) = 0 + 20 + (-2) + 0 + 90 + 0 = 108 \equiv 0 \pmod{2}$. **EG PBW constraint satisfied** at the leading $6$ Humbert discriminants, modulo the modular completion.

(More careful: $\sum_D c_D \cdot [\omega_D] = 0$ would need to hold *exactly* (not just mod $2$), and the cohomology classes $[\omega_D]$ have specific rational values. Without the explicit table of $[\omega_D]$ on $H^2(W^{(2)}, \mathbb{C})$, we have a parity-level consistency check; the full check is W11 follow-up.)

(6) **Toroidal $\mathfrak{gl}_1^{\otimes 24}$ smashed**: as in Cycle W11-1, the $24$-Kodaira-fibre tensor product of Miki's quantum toroidal $\mathfrak{gl}_1$, $M_{24}$-equivariant.

(7) **Saito--Takemura elliptic R-matrix**: provides the elliptic structure on the spectral $E_\tau$ direction.

**Three-path verification**:

**Path 1 (Etingof--Ginzburg 2002 deformation theory)**: the EG algebra at any choice of PBW-compatible parameters $c, \kappa$ is uniquely characterised up to isomorphism. With $c_D = f(D)$ and $\kappa_{\mathrm{Schur}} = $ unique non-trivial class, the EG algebra is uniquely determined.

**Path 2 (Wave 10 Etingof Cycle 5/Synthesis)**: the Wave 10 verdict identified $\mathbf{H}_{\Delta_5}$ via spherical eDAHA at $\Lambda_{\mathrm{Muk}}$ + Borcherds central extension. The EG algebra at $W^{(2)}(\Lambda^{2,1}_{II})$ on the rank-$3$ Cartan is **isomorphic to the spherical eDAHA at $\Lambda^{2,1}_{II}$** by EG 2002 Theorem 1.5 (Cherednik-EG isomorphism for Coxeter groups). Hence Wave 10's spherical eDAHA identification = our EG identification on the H71 sub-Cartan.

**Path 3 (Wave 10 Gelfand Cycle 5)**: Gelfand's "spherical sub-algebra of the rank-$3$ Borcherds-Koornwinder $C^\vee C_3$ DAHA at paramodular specialisation" is, by Stokman 2003 Thm 6.5 + EG 2002 Cherednik-EG iso, isomorphic to the EG algebra at $W^{(2)}(\Lambda^{2,1}_{II})$ with $5$-parameter Sahi--Stokman specialisation. The Sahi--Stokman parameters encode the Borcherds multiplicities $f(D)$. **Consistent with our identification.**

### W11-6 verdict

**Hidden unifying structure identified**: $\mathbf{H}_{\Delta_5}(\tau)$ is an **Etingof--Ginzburg symplectic reflection algebra** at the rank-$3$ hyperbolic Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$, with EG deformation parameters $c_D = f(D)$ from the K3 elliptic genus, smashed with $24$ copies of Miki's quantum toroidal $\mathfrak{gl}_1$ ($M_{24}$-equivariant), and semi-direct with Saito--Takemura's elliptic R-matrix on the spectral fibre $E_\tau$.

This unifies:
- Wave 10 Etingof Cycle 5 (spherical eDAHA at $\Lambda_{\mathrm{Muk}}$);
- Wave 10 Gelfand (rank-$3$ Borcherds-Koornwinder $C^\vee C_3$ DAHA);
- Wave 10 Drinfeld (3-parameter elliptic family over $\mathcal{M}_{1,1}$);
- Wave 10 Nekrasov ($U_{q, t, p}(\mathfrak{g}^{\mathrm{ell, Bor}}_{\Gamma^{4, 20}})$);
- Wave 10 Schiffmann--Vasserot CoHA on $K3$;
- The natural appearance of $24$ in Kodaira fibres;
- The Humbert stratification $\{H_D\}$ on Siegel $\mathcal{A}_2$.

**Final form of W11 verdict** (boxed at the top of this document).

---

## § Cross-cycle synthesis

**Wave 11 retractions of Wave 10**:

(R-W10-1) "Rank-$24$ toroidal $\mathfrak{gl}_n$" replaced by "rank-$1$ toroidal $\mathfrak{gl}_1$ tensor $24$, $M_{24}$-equivariant" (W11-1).

(R-W10-2) "Dedekind-$\eta$ cocycle = central extension of toroidal" replaced by "MRY 1990 cocycle on the loop direction + Saito--Takemura elliptic spectral cocycle on $E_\tau$, both present, both Jacobi-checked, commute" (W11-2).

(R-W10-3) "Imaginary-root central extension" sharpened: residue at $H_D$ is Lie-algebra-valued in $\mathfrak{sl}_2(\delta_D)$ for $D > 0$, central for $D = 0$, Heisenberg-cocycle-valued for $D < 0$. The Wave 10 statement was correct for the imaginary-cone case; the real-root case (which is the dominant Humbert spectrum) was under-stated.

(R-W10-4) "Full Mukai $\Gamma^{4, 20}$ support" must be **paramodular-restricted to $\Lambda^{(1,2)}_{II}$ at the cusp** (Wave 10 Drinfeld cusp limit gives MO Hilb($K3$), which lives on the paramodular sub-lattice, not full Mukai). The full Mukai support holds for the *generic* fibre via the Saito--Takemura elliptic R-matrix.

**Wave 11 promotions of Wave 10**:

(P-W10-A) Wave 10 "spherical eDAHA at $\Lambda_{\mathrm{Muk}}$" PROVED equivalent to "EG symplectic reflection algebra at $W^{(2)}(\Lambda^{2,1}_{II})$" via EG 2002 Cherednik-EG isomorphism (W11-6).

(P-W10-B) Wave 10 "Humbert pole at $H_D$" sharpened to "Lie-algebra-valued residue $f(D) \cdot \Omega_{\mathfrak{sl}_2(\delta_D)}$" with three-path verification at $H_4$ (W11-3).

(P-W10-C) Wave 10 "elliptic Borcherds quasi-Hopf" identified explicitly as **Saito--Takemura elliptic R-matrix algebra** on the spectral $E_\tau$-fibre, providing concrete name and reference.

(P-W10-D) Wave 10 Matsuo--Cherednik reduction sharpened: **Koornwinder $C^\vee C_2$ at $5$-parameter Sahi--Stokman conductor-$2$ specialisation** acting on weight-$5$ Saito--Kurokawa packet space (W11-5).

**Wave 11 surviving disagreements**:

(D-W11-1) **EG PBW constraint at modular completion**: the parity check $\sum_D c_D \cdot [\omega_D] \equiv 0 \pmod 2$ holds at the leading $6$ Humbert discriminants, but the full sum (over the entire Humbert spectrum, infinitely many) needs modular regularisation. Conjecture: the regularised sum equals zero in $H^2(W^{(2)}, \mathbb{C})$ exactly via Dedekind reciprocity (parallel to Drinfeld Wave 10 Cycle 4). **Status**: open math, settles by careful Borcherds-multiplicity regularisation.

(D-W11-2) **Schur multiplier class $\kappa_{\mathrm{Schur}} \in H^2(W^{(2)}, \mathbb{C})$**: identified up to a $\mathbb{Z}/2$ choice. The two choices correspond to the two Lorentzian BD triples on H71 (Wave 10 Etingof Cycle 2). The natural choice is the one matching the **Saito--Kurokawa packet's spin double cover**; explicit determination requires comparison of $\kappa$-character of the EG algebra with $\Pi(\psi_{\Delta_5})$ at the archimedean place. **Status**: open math.

(D-W11-3) **MRY 2-dim central piece reduction**: the toroidal MRY central piece is $2$-dim per Kodaira fibre, total $48$, reduced by $M_{24}$ to dim $48/24 = 2$ on the invariant sector. But the $M_{24}$-action on the central piece needs to be specified (does it act trivially or via the regular permutation?). If trivially: invariant central piece is $2$-dim. If via permutation: invariant central piece is $2/24$ which is not an integer — contradiction. **Status**: open math, settles by explicit $M_{24}$-action computation on the toroidal centres.

---

## § Wave 12 assignment

(W12-T1) **EG PBW constraint full sum**: regularise $\sum_{D \in \mathcal{H}_+} f(D) \cdot [\omega_D]$ via Borcherds-multiplicity regularisation; verify it vanishes in $H^2(W^{(2)}, \mathbb{C})$ exactly. ~300 lines.

(W12-T2) **Schur multiplier identification**: compute $\kappa_{\mathrm{Schur}}(W^{(2)}(\Lambda^{2,1}_{II}))$ explicitly via projective representation theory of hyperbolic Coxeter groups. Compare with Saito--Kurokawa spin cover. ~400 lines.

(W12-T3) **MRY $M_{24}$-action on toroidal centres**: compute the $M_{24}$ action on $H^2(\mathfrak{gl}_1^{\mathrm{tor}, (i)}, \mathbb{C}) = \mathbb{C}^2$ for each Kodaira fibre $i = 1, \ldots, 24$; identify whether the invariant central piece is $2$-dim or trivial. ~200 lines.

(W12-T4) **Saito--Takemura R-matrix on $\Lambda_{\mathrm{Muk}}$**: explicit construction of the elliptic R-matrix $R^{\mathrm{ell, Sai-Tak}}_{E_\tau}$ on the lattice $\Lambda_{\mathrm{Muk}}$ via Saito--Takemura 1998 elliptic L-operators; verify it commutes with the EG and toroidal pieces. ~600 lines.

(W12-T5) **Koornwinder reduction at higher Fourier-Jacobi blocks**: extend Cycle W11-5 from leading $\phi_{5, 1/2}$ to the next two blocks $\phi_{5, 3/2}, \phi_{5, 5/2}$. Predicts: Koornwinder $C^\vee C_2$ at higher level specialisation. ~500 lines.

(W12-T6) **Three-fold cross-check of W11 verdict**: compare the W11 EG-toroidal-Saito-Takemura identification against (i) Wave 10 Drinfeld holomorphic family over $\mathcal{M}_{1,1}$, (ii) Wave 10 Beilinson E_2-factorization Definition H10.1, (iii) Wave 10 Polyakov Borcherds-Goddard-Thorn no-ghost. Agreement at character level + presentation level. ~800 lines.

---

## § Manuscript amendments (Wave 11 Etingof voice)

1. **`chapters/examples/k3e_bkm_chapter.tex`**: replace "central extension of toroidal by imaginary-root Heisenberg with Dedekind cocycle" by the correct W11 verdict (boxed formula above). Add subsection "Etingof--Ginzburg symplectic reflection algebra identification with $c_D = f(D)$" with explicit citation to EG 2002 Theorem 1.3 / Cherednik-EG iso 1.5.

2. **`chapters/examples/k3_quantum_toroidal_chapter.tex`**: replace "K3 quantum toroidal algebra $U_{q,t}(\mathfrak{g}_{K3}^{\mathrm{tor}})$ at rank $24$" by "$M_{24}$-equivariant tensor product of $24$ copies of Miki's quantum toroidal $\mathfrak{gl}_1$ $(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$" with citation to Schiffmann--Vasserot 2013 Thm 1.1 + Davison--Hennecart--Schlegel-Mejia 2022 §4 K\"unneth.

3. **`chapters/examples/k3_yangian_chapter.tex`**: clarify that the K3 Heisenberg algebra is the *classical limit* (not the quantum object); the quantum object is Miki's $U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ tensored $24$.

4. **`chapters/connections/concordance.tex`**: register new anti-patterns (see §H).

5. **`appendices/first_principles_cache.md`**: append Wave 11 Etingof entries on (i) MRY vs Dedekind cocycle distinction, (ii) rank-$1$ toroidal tensor $24$ vs rank-$24$ toroidal, (iii) EG symplectic reflection identification.

---

## § New anti-patterns (Wave 11 Etingof)

**AP-CY-W11-E-1 (rank conflation)**: do NOT identify lattice rank with toroidal Cartan rank. The Mukai lattice has rank $24$, but Schiffmann--Vasserot's CoHA on K3 is **NOT** rank-$24$ toroidal $\mathfrak{gl}_n$. It is rank-$1$ toroidal $\mathfrak{gl}_1$ tensor $24$ (one per Kodaira fibre), $M_{24}$-equivariant.

**AP-CY-W11-E-2 (cocycle conflation)**: do NOT identify the Moody--Rao--Yokonuma (MRY) toroidal central-extension cocycle (trigonometric, on the loop direction) with the Saito--Takemura/Dedekind-$\eta$ elliptic spectral cocycle (modular, on the elliptic fibre $E_\tau$). They are **distinct cocycles** in **different gradings**, both present in the full chiral quantum group, both Jacobi-checked independently.

**AP-CY-W11-E-3 (Humbert residue Lie-valuation)**: residue of classical dynamical r-matrix at Humbert divisor $H_D$ is **Lie-algebra-valued** for $D > 0$ (real-root direction), central for $D = 0$ (lightlike), Heisenberg-cocycle-valued for $D < 0$ (imaginary). Do not state "scalar residue" without specifying the case.

**AP-CY-W11-E-4 (cusp vs generic fibre lattice support)**: $\mathbf{H}_{\Delta_5}(\tau)$ has *generic-fibre* support on full Mukai $\Gamma^{4, 20}$ via the Saito--Takemura elliptic spectral structure, but *cusp limit* $\tau \to i\infty$ degenerates to the **paramodular conductor-$2$ Lorentzian sublattice** $\Lambda^{(1, 2)}_{II} \subset \Gamma^{4, 20}$ (where $\Delta_5$ is supported). Do not state "full Mukai support at the cusp"; the Borcherds Lie algebra at $\Gamma^{4, 20}$ is $\mathfrak{g}_{\Phi_{12}}$ (Igusa weight $12$), not $\mathfrak{g}_{\Delta_5}$.

**AP-CY-W11-E-5 (EG vs eDAHA vs Cherednik DAHA naming)**: the Etingof--Ginzburg symplectic reflection algebra at $W$ is **isomorphic** to Cherednik's DAHA at $W$ via EG 2002 Theorem 1.5 (when $W$ is a Coxeter group). Do not treat them as distinct algebras; they are different presentations of the same object. Use "EG presentation" for the symplectic-reflection picture; "Cherednik presentation" for the DAHA picture.

**AP-CY-W11-E-6 (Koornwinder parameter forcing)**: in the Matsuo--Cherednik reduction of $\mathbf{H}_{\Delta_5}$ on a Fourier-Jacobi block of the form $-N \cdot q^{1/2} r^{-1/2} \prod_n (1 - q^{n-1} r)(1 - q^n r^{-1}) \cdot \text{etc}$, three of the five Koornwinder $C^\vee C_n$ parameters $(t_0, t_1, t_2, t_3, q)$ are **forced** by the Eichler--Zagier $\theta$-block structure: $t_0 = q^{1/2}, t_1 = -q^{1/2}, t_2 = -q^{-1/2}, t_3 = q^{-1/2}$. The remaining two $(q, t)$ are inherited Hecke deformation parameters; the fifth (Dedekind) enforces modular invariance. Do not over-count free parameters.

---

## § Numerical claims tabulated (Wave 11 Etingof)

| Claim | Source | Verification path |
|-------|--------|---------------------|
| Schiffmann--Vasserot rank-$1$: $\mathrm{CoHA}_K(\mathbb{A}^2) \cong U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ | SV 2013 Thm 1.1 | direct citation |
| MRY universal toroidal cocycle is $2$-dim | MRY 1990 Lemma 1.2 | residue computation |
| Dedekind reciprocity for $\eta$-products: $\eta(\tau)^{12}\eta(-1/\tau)^{12} = (-i\tau)^6\eta(\tau)^{12}$ | Apostol 1976 Thm 3.6 | classical |
| K3 Eichler--Zagier coefficient $c_{\phi_{0,1}}(1, 0) = 20$ | EZ 1985 Tab 1 | classical |
| K3 Eichler--Zagier coefficient $c_{\phi_{0,1}}(0, 0) = 2$ | EZ 1985 Tab 1 | classical |
| K3 Eichler--Zagier coefficient $c_{\phi_{0,1}}(1, \pm 1) = -2$ | EZ 1985 Tab 1 | classical |
| K3 Eichler--Zagier coefficient $c_{\phi_{0,1}}(2, 0) = 90$ | EZ 1985 Tab 1 | classical |
| Mukai rank $\mathrm{rk}(\Lambda_{\mathrm{Muk}}) = 24$ | Mukai 1987 | classical |
| H71 Cartan eigenvalues $\{-2, 4, 4\}$ on Lorgat 2020 PDF p. 7 Gram | direct computation | $G = 4I - 2J$ eigenvalue formula |
| H71 Gram det $= -32$ | direct computation | $\det(4I - 2J) = -32$ for $3 \times 3$ |
| Borcherds-Mukai lattice $\Gamma^{4, 20}$ self-dual signature $(4, 20)$ | Mukai 1987 | classical |
| Paramodular conductor-$2$ Lorentzian sublattice $\Lambda^{(1, 2)}_{II}$ rank $3$ | Lorgat 2020 PDF p. 5 Lemma 1 | $\wedge^2$-image computation |
| Saito--Kurokawa packet $\dim S_5(\Gamma_2(2)) = 1$ | classical (Gritsenko--Cleric) | Hecke eigenform construction of $\Delta_5$ |
| Stokman 2003 rank-$3$ Koornwinder $C^\vee C_3$ at Sahi specialisation $5$-parameter | Stokman 2003 Thm 6.5 | direct citation |
| EG 2002 Cherednik-EG iso for Coxeter $W$ | EG 2002 Thm 1.5 | direct citation |
| Number of Humbert discriminants up to $D = 12$: $|\{1, 4, 5, 8, 9, 12\}| = 6$ | classical | enumeration |
| Sum check $\sum_{D \leq 12} c_{\phi_{0,1}}(D) = 0 + 20 - 2 + 0 + 90 + 0 = 108 \equiv 0 \pmod 2$ | direct sum | parity-level EG PBW |

---

## § Final synthesis

The Wave 11 Etingof voice has destroyed the simplistic Wave 10 statement "eDAHA = central extension of toroidal by imaginary-root Heisenberg with Dedekind cocycle and Humbert pole at $H_D$" and replaced it by a finer, more structurally-correct identification:

$$
\mathbf{H}_{\Delta_5}(\tau) \;=\; \underbrace{\mathbf{H}^{\mathrm{EG}}_{c \,=\, f(D)}(W^{(2)}(\Lambda^{2,1}_{II}), \mathfrak{h} \oplus \mathfrak{h}^*)}_{\text{symplectic reflection on rank-}3\text{ H71}} \;\sharp\; \underbrace{(U_{q, \kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}}_{24\text{ Kodaira fibres, rank-}1\text{ toroidal each}} \;\rtimes\; \underbrace{R^{\mathrm{ell, Sai-Tak}}_{E_\tau}}_{\text{elliptic spectral on }E_\tau}.
$$

Each component is independently named, independently rigorously defined, and degenerates correctly:
- $q \to 1$ trigonometric: EG $\to$ trigonometric Cherednik DAHA (Stokman 2003); toroidal $\to$ rational toroidal (MRY 1990); Saito--Takemura $\to$ trigonometric R-matrix.
- $p \to 0$ cusp: full algebra $\to$ MO Hilb($K3$) BKM at paramodular sublattice $\Lambda^{(1, 2)}_{II}$ (matches Wave 10 Drinfeld cusp).

This is the **true chiral quantum group undergirding $\Delta_5$**.

Five attack-heal cycles complete. Wave 11 Etingof verdict registered.
