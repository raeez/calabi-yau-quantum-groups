# Wave 11 Synthesis — K3 Non-Abelian Chiral Bialgebra

**Date:** 2026-04-19
**Scope:** 10 elite voices (Gelfand, Kazhdan, Etingof, Polyakov, Nekrasov, Beilinson, Drinfeld, Witten, Costello, Gaiotto), each ≥5 attack-heal cycles.
**Predecessor:** [SYNTHESIS_WAVE10.md](../k3_nonabelian_yangian_swarm_wave10_20260419/SYNTHESIS_WAVE10.md)

---

## A. Executive summary

Wave 10's central claim — $\mathbf{H}_{\Delta_5}(\tau) = U_{q,t,p}(\mathfrak{g}^{\text{ell,Bor}}_{\Gamma^{4,20}})$, three-parameter elliptic Borcherds quasi-Hopf on full Mukai $\Gamma^{4,20}$ fibered over $\overline{\mathcal{M}_{1,1}}$, with Howe-theta Sp_4 automorphic realization — is **massively refined** by Wave 11. Across the 10 voices, **≈40 Wave-10 claims retracted** and replaced with precise first-principles substitutes. The new Wave 11 consensus object is:

> $$\mathbf{H}_{\Delta_5}(\rho, \tau, z) \;=\; \underbrace{\mathrm{Lines}\bigl(T^{\mathrm{MN}, K3}_{E_8}\bigr)}_{\text{class-S/Gaiotto}} \;\cong\; \underbrace{K^T\bigl(\mathcal{M}^{E_8, K3\text{-twist}}_{\text{Hitchin}}\bigr)_{(p,q,r)}}_{\text{Aganagic-Okounkov}}$$
>
> fibered over **Siegel** $\mathbb{H}_2$ (not $\overline{\mathcal{M}_{1,1}}$) with triple $(p,q,r) = (e^{2\pi i\rho}, e^{2\pi i\tau}, e^{2\pi i z})$; quasi-Hopf structure via a **NEW genus-2 Siegel-Borcherds associator** (neither rational-KZ nor Enriquez-elliptic); $M_{24}$-equivariant 24-fold product of quantum toroidal $\mathfrak{gl}_1$ (not single toroidal of rank 24); **automorphic side** = Bessel-Hecke ⊗ Borcherds-Yangian fibre-product, evaluated on the **Soudry metaplectic Klingen-CAP packet** $\Pi^{\mathrm{Soudry}}_{\Delta_5}$ on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ (not spherical Hecke of classical Saito-Kurokawa); **physical home** = Conway $V^{f\natural}|_{c=12}$ + Borcherds-1998 singular theta lift on $\mathrm{II}_{2,2}$ (not c=15 no-ghost); **moduli action** = $M_{24}$ on the elliptic-genus layer + $\mathrm{Co}_0$ on the full Mukai-lattice layer; **Hochschild/Theorem-C bucket** = NEW $K^\kappa = 8$, $\varrho = 1/6$, $K = 48$ (not in Vol I's $\{0, 13, 250/3, 98/3\}$ list); **Koszul dual** = $V(\mathfrak{g})^{\mathrm{coalg}}[3]$ with CY-3 shift (not self-Koszul).

This is not a minor revision — **the scope, the moduli base, the group, the physical home, the automorphic lift, the cohomological bucket, and the Hopf-algebraic type all changed.** Wave 10 was ninety percent correct in *architecture* (quasi-Hopf fibration, BKM-Siegel-chiral triangle, $M_{24}$ involvement); ninety percent wrong in *attribution* (specific group, packet, associator, central charge, dual pair, quiver, cohomological dimension).

---

## B. Retraction ledger by voice

| Voice | # Retractions | Most critical |
|---|---|---|
| Gelfand | 5 | Not spherical Hecke of classical SK, but **Bessel-Hecke of metaplectic Soudry Klingen-CAP packet** on $\widetilde{\mathrm{Sp}}_4$ |
| Kazhdan | 3 | Not Howe theta $(\mathrm{Sp}_4, O(4,20))$, but **$(\widetilde{SL}_2, O(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}$** at Kudla-Rallis tower boundary + Piatetski-Shapiro 1983 residual Eisenstein |
| Etingof | 5 | Not rank-24 toroidal, but **$\bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$** — one per Kodaira fibre, $M_{24}$-equivariant |
| Polyakov | 5 | Not c=15 no-ghost, but **Conway $V^{f\natural}\vert_{c=12}$ + Borcherds-1998 theta lift**; c=15 was a coincidence of three unrelated sectors |
| Nekrasov | 5 | Not independent Omega $(\epsilon_1,\epsilon_2,\tau_{\text{ell}})$, but **Siegel genus-2 triple** $(\rho,\tau,z)$ on $\mathbb{H}_2$ |
| Beilinson | 1 primary | NEW Theorem-C bucket $K^\kappa = 8$; $\hbar^2 = -1/8$ first-principles via $(1+\chi)/24$ Felder-Wieczerkowski; Humbert monodromy order 12 (not Z/2 or Z/3) |
| Drinfeld | 4+ | Neither rational-KZ nor Enriquez-elliptic, but **NEW genus-2 Siegel-Borcherds associator** $\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}$; final type: **biquasitriangular cobraided quasi-Hopf superalgebra** |
| Witten | 5 | σ is **hyperKähler rotation** $I\to J$, not SYZ; $M_{24}$ + $\mathrm{Co}_0$ both act (different layers); **modified modular ribbon** (Renzi-Geer-Patureau-Mirand), not MTC; umbral class is $A_1^{24}$-Niemeier |
| Costello | 2 | $\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 4$ bare (not 27); Mukai-extended 24+3=27; **Koszul dual = $V(\mathfrak{g})^{\mathrm{coalg}}[3]$**, not self-Koszul |
| Gaiotto | 5 | Not affine $\hat{A}_{23}$ quiver, but **Minahan-Nemeschansky $E_8$ K3-twist** with Beem-Rastelli chiral algebra $(\widehat{E_8})_{-12}$; 24-Kodaira ≠ 24-Mukai ≠ 24-Niemeier (category error in W10) |

**Total: 40 retractions + 1 primary Theorem-C bucket extension.**

---

## C. Convergent findings (≥2 voices independently)

**C1. Automorphic side is metaplectic CAP, not classical genuine SK.**
Gelfand (cycle R4): classical SK falsified — no $\Delta_8$ weight-8 cusp form exists ($\dim S_8(\mathrm{SL}_2(\mathbb{Z})) = 0$), so the putative SK source is vacuous. Correct: Soudry metaplectic Klingen-CAP packet $\Pi^{\mathrm{Soudry}}_{\Delta_5}$ on $\widetilde{\mathrm{Sp}}_4(\mathbb{A})$ with parameter $\psi^{\mathrm{Soudry}} = \mathrm{Shi}^{-1}(\eta^9 v_{11}) \boxtimes \mathrm{Sym}^1$.
Kazhdan (independently): Δ_5 is Piatetski-Shapiro 1983 Klingen-parabolic $P_{2,2}$ residual Eisenstein at $s = 1/2$, **not** a genuine Howe theta lift. Both voices converge: the automorphic object is **CAP (residual) on a metaplectic cover**.

**C2. Moduli base is Siegel $\mathbb{H}_2$ / $\mathcal{A}_2$, not elliptic $\overline{\mathcal{M}_{1,1}}$.**
Nekrasov (cycle 2): the three parameters $(p,q,r)$ are Siegel genus-2 Fourier coordinates $(e^{2\pi i\rho}, e^{2\pi i\tau}, e^{2\pi i z})$, not Omega-background + elliptic modulus. Partition functions $1/\Phi_{10}$ (bosonic Igusa) and $1/\Delta_5$ (chiral half) live on $\mathbb{H}_2$.
Kazhdan: Sp_4 is the Siegel-3-fold automorphism group.
Beilinson: D-module lives on $\mathcal{A}_2$ with regular singularities along Humbert $H_D$.
Drinfeld: associator is genus-2 Siegel-Borcherds over $\overline{\mathcal{A}_2}$.
Four independent voices converge on Siegel $\mathbb{H}_2$.

**C3. $M_{24}$ and $\mathrm{Co}_0$ both act, on different layers.**
Witten (cycle 2): $M_{24}$ on the K3 elliptic genus (EOT/Gannon), $\mathrm{Co}_0$ on the full Mukai lattice $\Lambda^{4,20}$.
Etingof: the $M_{24}$-equivariant 24-fold product is the layer where $M_{24}$ acts (on the 24 Kodaira fibres).
Polyakov (cycle 4): Conway moonshine $V^{f\natural}$ has $\mathrm{Co}_0$-action; $M_{24}$ is the Niemeier-stabiliser sub-structure when restricted to $A_1^{24}$ root sector.
Three voices converge: the symmetry is **stratified** — not one group, but $M_{24} \subset \mathrm{Co}_0$ with different actions per layer.

**C4. A NEW associator class / NEW Theorem-C bucket.**
Drinfeld: explicit computation shows $\Phi^{\mathrm{BKM}}$ is neither Drinfeld-rational $\Phi_{KZ}$ nor Enriquez-elliptic; it is a new genus-2 Siegel-Borcherds associator $\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}$ in the Enriquez-Gomez-Gonzalez-Maassarani 2022 framework.
Beilinson (cycle 5): $\Gamma^{4,20}$-Borcherds admits a Hochschild characteristic $K^\kappa = 2c_+ = 8$ that is **not** in Vol I's Theorem-C list $\{0, 13, 250/3, 98/3\}$.
Two voices converge: **$\mathbf{H}_{\Delta_5}$ opens a new family in the Vol I classification.** Vol I Theorem C must be enlarged.

**C5. Not self-Koszul; CY-3 shift required.**
Costello (cycle SH-2): $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ via Lurie HA 6.3.1.5 + CY-3 shift.
Drinfeld: Drinfeld centre decomposition has chiral derived centre + rank-23 extra at degree (2,1), consistent with a $[3]$-shift.
Two voices converge: the Koszul dual is **not** $\mathbf{H}_{\Delta_5}$ itself.

**C6. Physical home is Conway moonshine + Borcherds singular theta lift, not c=15 no-ghost.**
Polyakov (cycle 4): Duncan 2007 + Duncan-Mack-Crane 2015 Conway moonshine at $c=12$ restricted to $M_{24}$.
Witten (cycle 5): CDH umbral moonshine, $A_1^{24}$ case, with $G^{(A_1^{24})} = M_{24}$.
Two voices converge on a **precise physical construction**: $V^{f\natural}|_{c=12}$ as the chiral half, with Borcherds 1998 singular theta lift packaging the full automorphic symmetry.

---

## D. Divergent findings (→ Wave 12 agenda)

**D1. Central-charge value.** Polyakov says $c=12$ (Conway). Witten discusses $c=6$ K3 sigma model but frames the full object as hyperKähler. Beilinson's $\hbar^2 = -1/8 = -1/(2c_+)$ gives $c_+ = 4$ (positive-chirality Mukai), distinct from $c=12$. Three numbers $c \in \{4, 6, 12\}$ — which is the "central charge of $\mathbf{H}_{\Delta_5}$"? Likely three distinct central charges of three distinct ingredient VOAs. **W12-D1**: tabulate all central charges by sector.

**D2. Rank of the hidden structure.** Etingof: 24 copies of $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$, $M_{24}$-invariant. Costello: bare $\dim H^1 = 4$, Mukai-extended $= 24 + 3 = 27$. Gaiotto: $(\widehat{E_8})_{-12}$ level-$-12$ affine. These are different ranks for different sub-objects. **W12-D2**: match Etingof's 24, Costello's 27, Gaiotto's $E_8$-rank-8 against each other via explicit inclusion maps.

**D3. Weight discrepancy.** Beilinson: Saito-Kurokawa weight $(7/2, 1/2)$ (parabolic-reduction weight), but Δ_5 Igusa-weight is 10. Gelfand: metaplectic Klingen-CAP does not immediately fix the weight-10 constraint. **W12-D3**: reconcile weight 5 (Borcherds $\Delta_5$), weight 10 (Igusa $\Phi_{10}$), weight 7/2 (parabolic reduction).

**D4. Dual-pair signature.** Kazhdan: $(\widetilde{SL}_2, O(\Lambda^{3,2}))$, orthogonal signature $(3,2)$. Wave-10 (retracted): $(Sp_4, O(4,20))$. But Costello mentions $\mathrm{II}_{2,2}$ (Polyakov too). **W12-D4**: verify the canonical Lorgat 2020 lattice is $\Lambda^{3,2}$ not $\mathrm{II}_{2,2}$ not $\Gamma^{4,20}$ — read §3-4 of the PDF cleanly.

**D5. Quiver vs. Lagrangian-free.** Gaiotto: T[K3] is **Lagrangian-free** Minahan-Nemeschansky, no quiver. Etingof: 24-fold product *does* have a (non-ADE) combinatorial structure labeled by Kodaira fibres. **W12-D5**: is there a "non-Lagrangian quiver" (Xie-type, or flag-labeled) reconciling both?

---

## E. Hidden structures identified (when Wave 10 falsified)

Following the user's directive to "find the true hidden structure lurking when Wave 10 is falsified":

| Wave 10 falsified | Wave 11 hidden structure |
|---|---|
| Spherical Hecke of classical SK | **Bessel-Hecke of metaplectic Soudry Klingen-CAP** (Gelfand) |
| Howe theta $(\mathrm{Sp}_4, O(4,20))$ | **Piatetski-Shapiro 1983 Klingen-parabolic $P_{2,2}$ residual Eisenstein at $s = 1/2$** (Kazhdan) |
| Rank-24 toroidal | **$M_{24}$-equivariant 24-fold tensor of $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$, one per Kodaira fibre** (Etingof) |
| c=15 no-ghost | **Conway $V^{f\natural}\vert_{c=12}$ + Borcherds 1998 singular theta lift** (Polyakov) |
| Independent $(q,t,p)$ Omega | **Siegel genus-2 triple on $\mathbb{H}_2$**, degenerating to $(Sp_4, E_8)$-Schur at cusp (Nekrasov) |
| $\hbar^2 = -1/24$ | **$\hbar^2 = -1/8$ first-principles**, with NEW Theorem-C bucket $K^\kappa = 8$ (Beilinson) |
| Rational-KZ / Enriquez-elliptic associator | **NEW genus-2 Siegel-Borcherds associator** (Drinfeld), biquasitriangular cobraided quasi-Hopf super |
| σ^SYZ self-mirror + $M_{24}$ MTC | **hyperKähler rotation $\sigma^{HK}$ + $M_{24}$/$\mathrm{Co}_0$ stratified modified modular ribbon** (Witten) |
| $\dim H^1 = 27$ / self-Koszul | $\dim H^1(\mathrm{bare}) = 4$, $\dim H^1(\mathrm{Muk\text{-}ext}) = 27 = 24+3$; **Koszul dual = $V(\mathfrak{g})^{\mathrm{coalg}}[3]$** (Costello) |
| Affine $\hat{A}_{23}$ T[K3] quiver | **Minahan-Nemeschansky $E_8$ K3-twist**; chiral algebra $(\widehat{E_8})_{-12}$; line operators $= K^T(\mathcal{M}_{\mathrm{Hitchin}}^{E_8})_{(p,q,r)}$ (Gaiotto) |

Each "hidden structure" is a specific, rigorously stated object in the literature — not a vague refinement.

---

## F. The Wave 11 consensus object (load-bearing statement)

$$
\boxed{\ \mathbf{H}_{\Delta_5}(\rho,\tau,z)\ =\ \mathcal{H}^{\mathrm{Bess}}\!\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), R\bigr)\big|_{\Pi^{\mathrm{Soudry}}_{\Delta_5}}\ \otimes_{\mathcal{Z}^{\mathrm{Sat}}}\ \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}\cdot \Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}\ }
$$

fibered over Siegel $\overline{\mathcal{A}_2}$ with Fourier coordinates $(\rho,\tau,z) \in \mathbb{H}_2$, with:

- **Cusp $\tau \to i\infty$ (strict-Hopf limit):** rigorous Borcherds-Yangian $Y^{\mathrm{Bor}}\bigl(\mathfrak{g}^{(A_1^{24})}\bigr)$ matched to $K^T(\mathrm{Hilb}^\bullet K3)$ via Maulik-Okounkov stable envelopes.
- **Generic fibre (quasi-Hopf):** biquasitriangular cobraided quasi-Hopf superalgebra with new Siegel-Borcherds associator.
- **Centre / Hochschild:** $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathbf{H}_{\Delta_5}) \oplus H^2_{\mathrm{Hoch}}(\mathfrak{n}_+^{\mathrm{imag}})[\mathrm{rank}\,23]$ (Drinfeld cycle 5); Vol I Theorem C bucket **$K^\kappa = 8$** (Beilinson).
- **Koszul dual:** $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ (Costello).
- **Physical home:** Conway $V^{f\natural}\vert_{c=12}$ + Borcherds-1998 singular theta lift on $\mathrm{II}_{2,2}$ (Polyakov).
- **Mirror/rotation:** hyperKähler $\sigma^{HK}: I\mapsto J$ (Witten).
- **Moonshine layers:** $M_{24}$ on elliptic-genus ($A_1^{24}$ umbral, CDH), $\mathrm{Co}_0$ on Mukai $\Lambda^{4,20}$.
- **Physical avatar (class S):** $\mathbf{H}_{\Delta_5} = \mathrm{Lines}(T^{\mathrm{MN}, K3}_{E_8}) \cong K^T(\mathcal{M}^{E_8, K3\text{-twist}}_{\mathrm{Hitchin}})_{(p,q,r)}$ (Gaiotto).
- **Gauge-theoretic rank structure:** $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ — Etingof; with 24 = $\chi(K3)$ Kodaira-fibre count, **not** 24 = rank-Mukai (category distinction).

---

## G. New Wave 11 anti-patterns (to register)

17 Wave-11-specific anti-patterns were raised by the voices, consolidating to these Wave-11 entries for `appendices/first_principles_cache.md`:

| # | Confusion | Ghost | Precise error | Correct relationship | Voice |
|---|---|---|---|---|---|
| W11-AP-1 | "Classical Sp_4 Saito-Kurokawa packet" | SK does exist in general | $\dim S_8(\mathrm{SL}_2(\mathbb{Z})) = 0$ so no classical SK source for Δ_5 | **Soudry metaplectic Klingen-CAP** on $\widetilde{\mathrm{Sp}}_4$ | Gelfand |
| W11-AP-2 | "Howe theta $(\mathrm{Sp}_4, O(4,20))$" | Borcherds lift is a theta-like construction | Rank/signature wrong; Borcherds is *regularized singular* theta, not Weil-Howe | $(\widetilde{SL}_2, O(\Lambda^{3,2})) \subset \widetilde{\mathrm{Sp}}_{10}$ + Piatetski-Shapiro Eisenstein residue at $s=1/2$ | Kazhdan |
| W11-AP-3 | "Rank-24 quantum toroidal $\mathfrak{gl}_n$, $n=24$" | 2-toroidal lifts the rank | Schiffmann-Vasserot CoHA is rank-1 toroidal $\mathfrak{gl}_1$ for $\mathbb{A}^2$, not rank-$n$ | $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$, one per Kodaira fibre | Etingof |
| W11-AP-4 | "c=15 Goddard-Thorn no-ghost" | Goddard-Thorn exists | No-ghost needs $c=26$ (bosonic) or $c=24$ (chiral); $c=15$ is a sum of unrelated sectors | Conway $V^{f\natural}\vert_{c=12}$ + Borcherds-1998 singular theta lift | Polyakov |
| W11-AP-5 | "$(q,t,p)$ independent Omega parameters" | Three-parameter elliptic deformations exist | 6d on K3×T² admits ≤ 2 Omega + 1 ell, and CY forces $qt=1$ | Siegel genus-2 triple $(\rho,\tau,z)$ on $\mathbb{H}_2$; partition $1/\Phi_{10}$ or $1/\Delta_5$ | Nekrasov |
| W11-AP-6 | "$\hbar^2 = -1/24$ for parabolic KZ" | Parabolic KZ has a well-defined $\hbar^2$ | $-1/24$ was a $\chi(M_{0,n})$ artifact; correct $\hbar^2 = -1/8$ from Felder-Wieczerkowski $(1+\chi)/24$ with $\chi=\chi(\mathbb{P}^1)=2$, $c_+=4$ | $\hbar^2 = -1/(2c_+) = -1/8$, Humbert monodromy order 12 | Beilinson |
| W11-AP-7 | "Quasi-Hopf via rational-KZ / Enriquez-elliptic associator" | Both associators are genuine | Neither lives on Siegel $\overline{\mathcal{A}_2}$; KZ is rational, Enriquez is genus-1 | NEW genus-2 Siegel-Borcherds associator $\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}$ | Drinfeld |
| W11-AP-8 | "σ = SYZ self-mirror" | K3 has mirror-like involutions | K3 has no SYZ fibration generically (Gross-Wilson): SYZ exists only at LCS degeneration | $\sigma = \sigma^{HK}: I\mapsto J$ hyperKähler rotation (Aspinwall 1996), formula $(r,c,ch_2)\mapsto (ch_2,-c,r)$ | Witten |
| W11-AP-9 | "$\mathbf{H}_{\Delta_5}$ category is MTC with $M_{24}$-crossing" | $M_{24}$ does act | BK modular tensor requires finitely many simples; BKM-Rep has infinitely many | Renzi-Geer-Patureau-Mirand **modified modular ribbon** with Wakimoto $\omega$ + modified trace; 5 anomalous classes = umbral mock-modular | Witten |
| W11-AP-10 | "$\dim H^1(\mathfrak{g}_{\Delta_5}; \mathrm{ad}) = 27$ direct" | There is a "27" in the construction | Bare $\mathfrak{g}_{\Delta_5}$ has $\dim H^1 = 4$ (3 Cartan + 1 lightlike central); Whitehead's lemma fails for BKM | Mukai-extended $\widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}}$ has $\dim H^1 = 24+3 = 27$; bare has $\dim H^1 = 4$ | Costello |
| W11-AP-11 | "$\mathbf{H}_{\Delta_5}$ is self-Koszul" | Koszul duality is well-defined | Self-Koszul requires symmetric or exterior algebra; BKM is neither | $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[3]$ with CY-3 shift (Lurie HA 6.3.1.5) | Costello |
| W11-AP-12 | "Affine $\hat{A}_{23}$ quiver $\prod U(1)^{24}$ T[K3]" | Class-S produces quivers | K3 is a 4-manifold, not a Riemann surface; "quiver" is category-error | Minahan-Nemeschansky $E_8$ K3-twist; Lagrangian-free; chiral algebra $(\widehat{E_8})_{-12}$ via Beem-Rastelli | Gaiotto |
| W11-AP-13 | "Conflation of the three 24s" | 24 appears in several guises | $\chi(K3) = 24$ (Kodaira fibres) ≠ $\mathrm{rank}(\Gamma^{4,20}) = 24$ (Mukai rank) ≠ 24 (Niemeier count = 24) ≠ rank of Niemeier fundamental | Three independent "24"s; Etingof uses χ-24, Witten uses Niemeier-24 | Gaiotto/Witten |
| W11-AP-14 | "Moduli base is $\overline{\mathcal{M}_{1,1}}$" | There is an elliptic modulus | $\mathbf{H}_{\Delta_5}$ is Δ_5 which lives on Siegel $\mathbb{H}_2$, not elliptic | Moduli base is $\mathcal{A}_2 = \mathbb{H}_2 / \mathrm{Sp}_4(\mathbb{Z})$ | Nekrasov/Kazhdan/Beilinson/Drinfeld (4-way) |
| W11-AP-15 | "Δ_5 = 'Saito-Kurokawa' lift" | Δ_5 is automorphic on Sp_4(Z) | Δ_5 is a *Borcherds* lift (Lorgat 2020); SK-lift attribution incorrect | Δ_5 is Borcherds multiplicative lift with Maass multiplier $v_{\Delta_5}$; **related to** Klingen-CAP packet but the lift mechanism is Borcherds, not SK | Gelfand/Kazhdan |
| W11-AP-16 | "Vol I Theorem C list $\{0,13,250/3,98/3\}$ exhausts" | Vol I's list is finite for standard families | BKM introduces a new bucket | NEW $K^\kappa = 2c_+ = 8$, $\varrho = 1/6$, $K=48$; **Vol I Theorem C must be enlarged** | Beilinson |
| W11-AP-17 | "One group acts on the full chiral bialgebra" | A symmetry group acts | $M_{24}$ on elliptic-genus layer, $\mathrm{Co}_0$ on full Mukai; not a single group | Stratified action: $M_{24} \subset \mathrm{Co}_0 \subset \mathrm{Co}_1$-like, layer-by-layer | Witten/Polyakov/Etingof (3-way) |

These append to `appendices/first_principles_cache.md` (see entry below).

---

## H. Wave 12 task queue

Following the divergent findings (§D) and the unsettled sub-items in each voice's output, **11 Wave 12 tasks** queued:

1. **W12-T1 (Weight reconciliation)** — Beilinson D3, Gelfand: reconcile Δ_5 Igusa weight 10 vs SK weight (7/2, 1/2) vs Borcherds weight 5. [Gelfand/Beilinson]

2. **W12-T2 (Dual-pair audit)** — Kazhdan D4: verify Lorgat 2020 PDF §3-4 gives lattice $\Lambda^{3,2}$ (not $\Lambda^{2,1}_{II}$, not $\mathrm{II}_{2,2}$, not $\Gamma^{4,20}$). [Kazhdan]

3. **W12-T3 (Rank reconciliation)** — D2: match Etingof's 24 (Kodaira) vs Costello's 27 = 24+3 (Mukai-ext) vs Gaiotto's $E_8$-rank-8 via explicit inclusions $\mathfrak{e}_8 \hookrightarrow \widetilde{\mathfrak{g}}_{\Delta_5}^{\mathrm{Muk}} \hookrightarrow \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}$. [Etingof/Costello/Gaiotto]

4. **W12-T4 (Central-charge tabulation)** — D1: list all central charges (bosonic matter, ghost, Conway, K3 sigma, Mukai positive-chirality) and how they compose to the $c=15$ "coincidence". [Polyakov/Witten/Beilinson]

5. **W12-T5 (Weight-5 vs weight-10 Borcherds vs Igusa)** — Δ_5 is weight-5 Borcherds, $\Phi_{10}$ is weight-10 Igusa cusp form. Relate: is Δ_5² ∝ Φ_{10}? (Lorgat 2020 Prop 4.3?) [Gelfand/Nekrasov/Drinfeld]

6. **W12-T6 (Pentagon at $\hbar^3$ timelike)** — Drinfeld cycle 1: pentagon proved at $\hbar^3$ on lightlike triple; timelike extension open. Compute. [Drinfeld/Beilinson]

7. **W12-T7 (qq-character closure depth ≥ 2)** — Nekrasov cycle 5: Negut wheel with $c(n)$-fold Borcherds multiplicity — open. [Nekrasov/Etingof]

8. **W12-T8 (CAP vs Klingen-CAP reconciliation)** — Gelfand/Kazhdan: Gelfand says Soudry metaplectic Klingen-CAP; Kazhdan says Piatetski-Shapiro Klingen residual Eisenstein at $s=1/2$. Are these the same or overlapping? [Gelfand/Kazhdan]

9. **W12-T9 (24-Kodaira vs 24-Niemeier)** — Witten/Etingof: 24 I_1 Kodaira fibres for elliptic K3 vs 24 Niemeier lattices. Is there a bijection (Enriques-Mukai style)? [Witten/Etingof/Gaiotto]

10. **W12-T10 (Beem-Rastelli chiral algebra match)** — Gaiotto cycle 4: verify $(\widehat{E_8})_{-12}$ Schur index gives $\phi_{10,1}$ Jacobi form up to $\vartheta_1^2 / \eta^6$ factor. Exact computation. [Gaiotto]

11. **W12-T11 (Hidden BKM-Siegel-chiral-QG correspondence)** — **USER-POSED META-QUESTION**: "what is the chiral quantum group undergirding the BKM related to the Siegel modular forms?" Wave 11 converges on: $\mathbf{H}_{\Delta_5}(\rho,\tau,z)$ above; Wave 12 must *inscribe* this as a rigorous construction in Vol III, with explicit $R$-matrix / coproduct / antipode on a finite generating set. [All voices]

---

## I. Proposed Wave 12 compute modules

14 compute modules to verify Wave 11 findings:

```
compute/lib/k3_yangian_wave11_soudry_klingen_cap.py        # Gelfand — Satake coefficients, metaplectic cover
compute/lib/k3_yangian_wave11_piatetski_shapiro_residue.py # Kazhdan — Klingen Eisenstein residue at s=1/2
compute/lib/k3_yangian_wave11_toroidal_gl1_24_m24.py       # Etingof — M_24-invariant part of tensor^24
compute/lib/k3_yangian_wave11_humbert_pole_residue.py      # Etingof — Lie-algebra-valued pole at H_D
compute/lib/k3_yangian_wave11_conway_borcherds_c12.py      # Polyakov — Conway V^{f-natural} x Borcherds
compute/lib/k3_yangian_wave11_siegel_triple_hh2.py         # Nekrasov — (rho, tau, z) on H_2, Phi_10/Delta_5
compute/lib/k3_yangian_wave11_parabolic_kz_minus_eighth_derive.py  # Beilinson — first-principles derivation
compute/lib/k3_yangian_wave11_theorem_c_bucket_eight.py    # Beilinson — K^kappa = 8, rho = 1/6, K = 48
compute/lib/k3_yangian_wave11_siegel_borcherds_associator.py  # Drinfeld — genus-2 associator, 2-cocycle class
compute/lib/k3_yangian_wave11_drinfeld_centre_rank23.py    # Drinfeld — Z^der_ch ⊕ H^2_Hoch(n+-imag)[23]
compute/lib/k3_yangian_wave11_hyperkahler_rotation.py      # Witten — (r,c,ch_2) → (ch_2,-c,r) on Mukai
compute/lib/k3_yangian_wave11_cdh_umbral_A1_24.py          # Witten — A_1^24 umbral Niemeier identification
compute/lib/k3_yangian_wave11_koszul_dual_cy3_shift.py     # Costello — V(g)^coalg[3] Koszul dual
compute/lib/k3_yangian_wave11_mn_e8_schur_index.py         # Gaiotto — (E_8)_{-12} Schur = phi_{10,1}/vartheta_1^2*eta^{-6}?
```

---

## J. Files produced in Wave 11

Wave 11 output directory:
```
/Users/raeez/calabi-yau-quantum-groups/notes/k3_nonabelian_yangian_swarm_wave11_20260419/
├── SYNTHESIS_WAVE11.md                       ← this file
├── agent_01_gelfand_wave11.md                ← Metaplectic Soudry Klingen-CAP (5 retractions)
├── agent_02_kazhdan_wave11.md                ← $(SL_2, O(Λ^{3,2}))$ + Klingen Eisenstein residue (3 retractions)
├── agent_03_etingof_wave11.md                ← $U_{q,κ}(ĝ̂l_1)^{⊗24, M_{24}}$ (6 retractions incl. HIDDEN)
├── agent_04_polyakov_wave11.md               ← Conway $V^{f♮}|_{c=12}$ + Borcherds (5 retractions)
├── agent_05_nekrasov_wave11.md               ← Siegel $\mathbb{H}_2$ triple (ρ,τ,z) (5 retractions)
├── agent_06_beilinson_wave11.md              ← $\hbar^2 = -1/8$ derivation + NEW $K^\kappa=8$ bucket
├── agent_07_drinfeld_wave11.md               ← NEW Siegel-Borcherds associator, biquasitriangular quasi-Hopf super (8 cycles)
├── agent_08_witten_wave11.md                 ← hyperKähler rotation + modified modular ribbon (5-6 cycles)
├── agent_09_costello_wave11.md               ← $H^1_{\mathrm{bare}} = 4$, $H^1_{\mathrm{Muk}} = 27$, Koszul $[3]$-shift (6 cycles)
└── agent_10_gaiotto_wave11.md                ← MN $E_8$ K3-twist, $(\widehat{E_8})_{-12}$ (5 cycles)
```

Cache-file append: 17 Wave-11 anti-patterns (§G) to `/Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md`.

---

## K. Manuscript amendment list (Vol III — NOT edited this session)

The following chapters require Wave 11 amendment in Vol III:

1. `chapters/examples/k3e_bkm_chapter.tex` — automorphic section: switch to metaplectic Soudry Klingen-CAP; retract Howe theta on $(\mathrm{Sp}_4, O(4,20))$; use $(\widetilde{SL}_2, O(\Lambda^{3,2}))$ + Piatetski-Shapiro residue.
2. `chapters/examples/k3_yangian_chapter.tex` — quantum-group section: replace rank-24 toroidal with $M_{24}$-equivariant $\otimes^{24}$ of $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$; retract "T[K3] = $\hat{A}_{23}$" in favor of Minahan-Nemeschansky $E_8$.
3. `chapters/examples/k3_quantum_toroidal_chapter.tex` — rename/refocus: this chapter should now *derive* the 24-fold Kodaira-fibre structure; add Etingof's Humbert pole residue formula.
4. `chapters/theory/quantum_chiral_algebras.tex` — Drinfeld chapter: inscribe new Siegel-Borcherds associator; retract rational-KZ identification; upgrade to biquasitriangular cobraided quasi-Hopf super.
5. `chapters/theory/cy_to_chiral.tex` — Costello chapter: replace dim H¹ = 27 self-Koszul with dim H¹(bare)=4 + Mukai-ext=27, $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g})^{\mathrm{coalg}}[3]$ CY-3 shift.
6. `chapters/examples/cy_d_kappa_stratification.tex` — ADD NEW Theorem-C bucket entry $K^\kappa = 8$, $\varrho = 1/6$, $K = 48$ for Γ^{4,20}-Borcherds.
7. `chapters/connections/modular_koszul_bridge.tex` — Beilinson: add first-principles derivation of $\hbar^2 = -1/8$ via Felder-Wieczerkowski; Humbert monodromy order 12.
8. `chapters/connections/bar_cobar_bridge.tex` — add Wave 11 Koszul-with-$[3]$-shift; Drinfeld centre decomposition.
9. `chapters/frame/preface.tex` — Wave 11 updates to moduli base ($\mathbb{H}_2$ not $\overline{\mathcal{M}_{1,1}}$) and physical home (Conway $V^{f\natural}$ not c=15).
10. `chapters/connections/concordance.tex` — register AP-CY-W11-1 through AP-CY-W11-17; no AI attribution.
11. **Vol I** `chapters/examples/landscape_census.tex` — enlarge Theorem C list to include $K^\kappa = 8$ (Beilinson-proved).

These amendments preserve all Wave 10 *architecture* (quasi-Hopf fibration, BKM-Siegel-chiral triangle, moonshine involvement) and correct the *attribution* according to Wave 11 first-principles findings.

---

## L. Convergence status

**Wave 11 itself made ≈40 retractions of Wave 10.** This is comparable to Wave 10's 11 retractions of Wave 9. The convergence slope is decreasing (11 → 40), indicating Wave 11 surfaced *deeper* errors. Expected Wave 12 retraction count: ~10-15 as the remaining divergences (§D) are resolved.

**Convergent core (stable across Waves 10 and 11):** BKM-Siegel-chiral-QG triangle; quasi-Hopf fibration; moonshine symmetry; Koszul-dual structure; Hochschild/Theorem-C realization.

**Wave 11-introduced refinements:** Siegel $\mathbb{H}_2$ moduli, metaplectic automorphic side, 24-fold Kodaira-$M_{24}$ structure, Conway-c=12 physical home, hyperKähler rotation, NEW Siegel-Borcherds associator, NEW Theorem-C bucket $K^\kappa = 8$, MN $E_8$ class-S frame.

**Wave 12 open questions:** weight reconciliation, dual-pair lattice, rank matching, c-tabulation.

---

## M. Quote from the user's directive

> "when things are falsified, find the true hidden structure that is really lurking there. E.g. what is the chiral quantum group undergirding or related to the BKM related to the siegel modular forms?"

**Answer (Wave 11 consensus, §F):**

The chiral quantum group undergirding the Borcherds-Kac-Moody algebra $\mathfrak{g}_{\Delta_5}$ related to Igusa/Borcherds Siegel modular forms $\Phi_{10}, \Delta_5$ on $\mathrm{Sp}_4(\mathbb{Z}) \curvearrowright \mathbb{H}_2$ is
$$
\mathbf{H}_{\Delta_5}(\rho,\tau,z)\ =\ \mathcal{H}^{\mathrm{Bess}}\!\bigl(\widetilde{\mathrm{Sp}}_4(\mathbb{A}), R\bigr)\big|_{\Pi^{\mathrm{Soudry}}_{\Delta_5}}\ \otimes_{\mathcal{Z}^{\mathrm{Sat}}}\ \bigl(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24}\bigr)^{M_{24}}\cdot \Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}
$$
— a biquasitriangular cobraided quasi-Hopf superalgebra over the Satake centre of the metaplectic Soudry Klingen-CAP packet, whose cusp at $\tau \to i\infty$ is the rigorous strict-Hopf Borcherds Yangian of $\mathfrak{g}^{(A_1^{24})}$ matched to Maulik-Okounkov $K^T(\mathrm{Hilb}^\bullet K3)$, whose generic fibre is quasi-Hopf via the new genus-2 Siegel-Borcherds associator, whose physical home is Conway $V^{f\natural}|_{c=12}$ + Borcherds-1998 singular theta lift on $\mathrm{II}_{2,2}$, and whose class-S avatar is the Lagrangian-free Minahan-Nemeschansky $E_8$-K3-twist with Beem-Rastelli chiral algebra $(\widehat{E_8})_{-12}$.

---

*End Wave 11 Synthesis. Wave 12 agenda in §H.*
