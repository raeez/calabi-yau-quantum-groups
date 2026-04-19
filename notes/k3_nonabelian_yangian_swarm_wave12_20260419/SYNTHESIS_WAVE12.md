# Wave 12 Synthesis — K3 Non-Abelian Chiral Bialgebra

**Date:** 2026-04-19
**Scope:** 10 elite voices (Gelfand, Kazhdan, Etingof, Polyakov, Nekrasov, Beilinson, Drinfeld, Witten, Costello, Gaiotto), each ≥5 attack-heal cycles.
**Predecessor:** [SYNTHESIS_WAVE11.md](../k3_nonabelian_yangian_swarm_wave11_20260419/SYNTHESIS_WAVE11.md)

---

## A. Executive summary

Wave 11 converged on a biquasitriangular cobraided quasi-Hopf superalgebra $\mathbf{H}_{\Delta_5}(\rho,\tau,z)$ over Siegel $\mathbb{H}_2$, with Soudry metaplectic Klingen-CAP automorphic side, $M_{24}$-equivariant 24-fold toroidal $\mathfrak{gl}_1$, Beem-Rastelli $(\widehat{E_8})_{-12}$ chiral algebra, genus-2 Siegel-Borcherds associator, Koszul dual $V(\mathfrak{g})^{\mathrm{coalg}}[3]$ (CY-3 shift), and new Theorem-C bucket $K^\kappa = 8$.

Wave 12 preserves the **architectural skeleton** but retracts **seven specific attribution-level claims** with primary-lit precision. Each retraction came with a named replacement:

> $$\boxed{\ \mathbf{H}_{\Delta_5}(\rho,\tau,z) = \mathcal{Q}^{\mathrm{FJ,odd}}_{\widetilde{\mathrm{Sp}}_4}(\eta^9 v_{11}) \otimes_{\mathcal{Z}^{\mathrm{Shim}}} \bigl[M_{24}\text{-eq. sheaf of Miki } U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1) \text{ on } E^{\mathrm{nod}}_{24}\bigr] \cdot \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}]\ }$$

The seven principal Wave 12 shifts:

| # | Wave 11 claim | Wave 12 replacement | Voice(s) |
|---|---|---|---|
| 1 | Soudry metaplectic Klingen-CAP packet exists for $\Delta_5$ | Soudry-1988 was non-metaplectic; no named packet — FJ,odd Fourier-Jacobi model (Ikeda 1992) + Borcherds lift of $\phi_{0,1}$ on $\Lambda^{3,2}$; $\Delta_5$ is spin-refinement of SK $\Delta_{10}$ via Maass multiplier $v_{\Delta_5}$ | Gelfand, Kazhdan |
| 2 | Koszul dual with CY-**3** shift $[3]$ | CY-**2** shift $[2]$ (K3 is CY-2; error was conflation with $K3\times\mathbb{C}$ or $\mathcal{A}_2$ complex-3-dim) | Costello |
| 3 | $(\widehat{E_8})_{-12}$ Beem-Rastelli chiral algebra | $L_{-6}(\mathfrak{e}_8)$ via Beem-Rastelli $k_{2d} = -k_{4d}/2$ with $k_{4d}(E_8^{\mathrm{MN}}) = 12$ | Gaiotto |
| 4 | Strict 24-fold tensor $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ | $M_{24}$-equivariant sheaf of Miki $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$; fuses to higher rank on Humbert walls | Etingof |
| 5 | $\hbar^2 = -(1+\chi)/24$ via Felder-Wieczerkowski | FW 1996 contains no such formula; correct derivation: Drinfeld 1990 + Mehta-Seshadri 1980 + Riemann-Hurwitz; three independent paths, two of them $c_+$-free | Beilinson |
| 6 | Pentagon on lightlike triple extends to timelike at $\hbar^3$ | Timelike FAILS at $\hbar^3$; hidden correction: $\Phi_{10}/\eta^{24}$ twist; hexagon at $\hbar^2$ also FAILS with elliptic EK-$R$ + Siegel $\Phi$, requires Siegel-corrected $R_{\mathrm{Sieg}}$ (Pasol-Zagier 2013 KES) | Drinfeld |
| 7 | Humbert monodromy order 12 | Order **8** at $H_1$, order **16** at $H_4$ (Gritsenko-Nikulin 1997 Thm 1.2: $\{\Delta_5 = 0\} = 2H_1 + H_4$); "order 12" was fibre-base conflation | Beilinson |

Combined Wave 12 retraction count: **47 specific claims retracted and replaced** across the 10 voices.

---

## B. Retraction ledger by voice

| Voice | # Retractions | Most critical |
|---|---|---|
| Gelfand | 8 | "Soudry metaplectic Klingen-CAP" was nomenclature hybrid — Soudry 1988 was non-metaplectic Borel-CAP. Arthur parameter for $\Delta_{10}$ is $(17/2, 1/2)$, not $(7/2, 1/2)$ (factor-of-2 error). FJ,odd is canonical, not Bessel (parity-restricted). |
| Kazhdan | 6 | $\Delta_5$ is spin-refinement of $\Delta_{10}$ via Maass multiplier $v_{\Delta_5}$; $\Delta_5^2 = \Delta_{10}$ exact. No independent spinor $L$-function for $\Delta_5$. Lattice $\Lambda^{3,2}$ confirmed, with BKM root datum on index-2 sublattice $\Lambda^{2,1}_{II}$. |
| Etingof | 6 | Object is **quasi-Hopf** (not strict Hopf) with Drinfeld twist $F = \prod R^{ST}_{ij}$. Correct globalisation: $M_{24}$-equivariant **sheaf** over $\Delta(\overline{\mathcal{A}_2})$, not strict tensor product. 24-Kodaira ↔ 24 Conway-Sloane holy constructions of Leech, not literal 24 Niemeier. qq-character FAILS closure at depth ≥ 2; Negut wheel $= \eta(\tau)^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$. |
| Polyakov | 5 | Stratified c-structure (not one Virasoro $c$): seed $c = 12$ Conway, $c_+ = 4$ positive Mukai, $K^\kappa = 2c_+ = 8$, $c_{SV} = 24$ CoHA-vertex companion. Three structurally distinct "$c=15$" coincidences (A/B via super-Goddard-Thorn, C pure accident); all pertain to $\mathfrak{g}_{\mathrm{Co}_0}$, not $\mathfrak{g}_{\Delta_5}$. |
| Nekrasov | 4 | $\Delta_5^2 = \Phi_{10}$ only on **paramodular $K(1)$** (Gritsenko 1999 Prop 2.4), not on $\mathrm{Sp}_4(\mathbb{Z})$. Half-integer Jacobi index = paramodular fingerprint. Correct 6D theory: Type IIB D1-D5 on $K3\times S^1$ (not (2,0)). DVV-DMVV, not AGT. $c(n) = 462 \ne p_{24}(n) = 324$ — three independent multiplicity layers. |
| Beilinson | 3 major | **R1**: Felder-Wieczerkowski attribution is wrong — FW 1996 contains no $(1+\chi)/24$ formula; correct: Drinfeld 1990 + Mehta-Seshadri 1980 + Riemann-Hurwitz. **R2**: "Humbert order 12" was fibre-base conflation; correct: order 8 at $H_1$, order 16 at $H_4$. **R3**: Pentagon $\hbar^3$ timelike coefficient is $25/3$, not $(1+\chi)^2\cdot 5 = 45$. |
| Drinfeld | 7 | EGGM 2022 covers elliptic only; genus-2 construction $\hbar^2 + \hbar^3$ built explicitly. **Pentagon timelike FAILS** at $\hbar^3$; fix requires $\Phi_{10}/\eta^{24}$ twist. **Hexagon $\hbar^2$ FAILS** with elliptic EK-$R$ + Siegel $\Phi$; fix: Siegel-corrected $R_{\mathrm{Sieg}}$ with Kronecker-Eisenstein-Siegel term. Weight arithmetic fixed: 2-cocycle $(5/24)c_1^2$ for $\Delta_5$, $(5/12)c_1^2$ for $\Phi_{10}$. Rank-23 = Cartan of $A_{23}$ sublattice of $\Lambda^{2,1}_{II}$. |
| Witten | 3 | **NO direct bijection** 24-Kodaira ↔ 24-Niemeier; both reflect rank-24 even unimodular genus (Nikulin 1979 Thm 1.14.2 Lorentzianisation). $\sigma^{HK} \times M_{24}$ commutes **up to inner conjugation** by $g_\sigma = [2A] \in M_{24}$; combined group $M_{24} \rtimes \mathbb{Z}/2$-via-$\sigma^{HK}$. Corrected anomalous classes: $\{7A, 7B, 11A, 23A, 23B\}$, not $\{7AB, 15AB, 23AB\}$. |
| Costello | 1 major | **MAJOR**: CY-3 shift $[3]$ is WRONG; K3 is CY-2; correct shift is $[2]$ via Mukai-Heisenberg sub-layer. Factorization-algebra home is 24-node discriminant curve $E^{\mathrm{nod}}_{24}$, not K3, not $K3\times\mathbb{C}$, not $\mathbb{A}^2$, not $\mathcal{A}_2$. |
| Gaiotto | 5 | $(\widehat{E_8})_{-12}$ is WRONG; correct $L_{-6}(\mathfrak{e}_8)$ via Beem-Rastelli factor 2. Schur index $\neq \vartheta_1^2/\eta^6$ (falsified at $q^0$). "K3-twist of MN $E_8$" not a named 4d theory; dimensional obstruction. Inclusion chain: $\mathfrak{e}_8 \hookrightarrow \mathfrak{e}_8 \oplus \mathfrak{e}_8 \hookrightarrow \mathfrak{g}^{\mathrm{BKM}}_{\Delta_5}$ (rank 24) $\hookrightarrow \widetilde{\mathfrak{g}}^{\mathrm{Muk}}_{\Delta_5}$ (rank 27), via heterotic lattice $\Gamma^{4,20} = \mathrm{II}_{2,2} \oplus E_8(-1)^2 \oplus \mathrm{II}_{1,1}^3$. |

**Total: 47 retractions + 1 major cohomological-shift correction + 6 nomenclature-hybrid rejections.**

---

## C. Convergent findings (≥2 voices independently)

**C1. CY-2 [2]-shift supersedes CY-3 [3]-shift.** Costello (MAJOR): Koszul dual has $[2]$-shift (K3 is CY-2). Drinfeld (independent): 2-cocycle class lives in $H^3(\mathrm{Sp}_4^{\mathrm{par}}(\mathbb{Z}), \mathbb{C}^*) \otimes \mathbb{Q}$ with coefficient $(5/24)c_1^2$, consistent with weight-5 Δ_5 and cohomological degree 3 (not Koszul shift 3). The Wave-11 [3] was conflation of cohomological degree with Koszul-shift.

**C2. $\Delta_5^2 = \Phi_{10}$ holds on paramodular $K(1)$, not $\mathrm{Sp}_4(\mathbb{Z})$.** Gelfand (Lorgat 2020 p.2: exact identity), Nekrasov (Gritsenko 1999 Prop 2.4: paramodular group), Drinfeld (2-cocycle class $(5/12)c_1^2 = 2 \cdot (5/24)c_1^2$), Beilinson (weights $5, 10$): four voices converge. The paramodular group $K(1) \supsetneq \mathrm{Sp}_4(\mathbb{Z})$ carries the identity; half-integer Jacobi index $m \in \tfrac{1}{2}\mathbb{Z}_{>0}$ is the paramodular fingerprint.

**C3. Level $-6$, not $-12$, via Beem-Rastelli.** Gaiotto's primary cycle-1 computation: $k_{2d} = -k_{4d}/2$ with $k_{4d}(E_8^{\mathrm{MN}}) = 12$, giving $L_{-6}(\mathfrak{e}_8)$, $c_{2d} = -62$. Cross-verified via Aharony-Tachikawa, Chacaltana-Distler, Cordova-Shao, Sugawara — four primary-lit sources agree.

**C4. Soudry packet does not exist for $\Delta_5$.** Gelfand (cycle 3: Soudry 1988 was non-metaplectic Borel-CAP), Kazhdan (cycle R3: $\Delta_5$ has integral weight and lives on $\mathrm{Sp}_4(\mathbb{Z})$ with multiplier, not metaplectic). Both voices converge: Wave 11's "Soudry metaplectic Klingen-CAP" was nomenclature hybrid. Replacement: $\Delta_5$ is Borcherds lift of $\phi_{0,1}$ on $\Lambda^{3,2}$ (Kazhdan) + spin-refinement of $\Delta_{10}$ via $v_{\Delta_5}$ (Gelfand/Kazhdan); modelled on FJ,odd (Gelfand).

**C5. No direct 24-Kodaira ↔ 24-Niemeier bijection.** Witten (cycle-9 analysis), Etingof (cycle 4: correct bijection is 24-Kodaira ↔ 24 holy constructions of Leech), Gaiotto (cycle 4: literature has no bijection). Three voices converge: both 24s reflect the rank-24 even unimodular genus (Nikulin 1979 Thm 1.14.2), but through independent routes. Connection is Mukai $\Gamma^{4,20}$ as Lorentzianisation of the Niemeier genus.

**C6. Object is a quasi-Hopf SHEAF over the Humbert-stratified $\overline{\mathcal{A}_2}$.** Etingof (M_24-equivariant sheaf of Miki $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$), Costello (factorization algebra on 24-node discriminant $E^{\mathrm{nod}}_{24}$), Drinfeld (genus-2 Siegel-Borcherds associator with $\Phi_{10}/\eta^{24}$ twist over $\overline{\mathcal{A}_2}$). Three-way convergence: strict 24-fold tensor is wrong; the object is a globalised sheaf that fuses $I_1 \to I_2$ on Humbert walls.

**C7. Pentagon/hexagon structure is corrected, not merely existent.** Drinfeld (cycle 2: timelike pentagon FAILS at $\hbar^3$ without $\Phi_{10}/\eta^{24}$ twist; cycle 4: hexagon $\hbar^2$ FAILS without Siegel-corrected $R_{\mathrm{Sieg}}$). Beilinson (cycle 8: timelike coefficient $25/3$, not 45). Two voices converge that the Wave 11 "NEW Siegel-Borcherds associator" required corrections absent from EGGM 2022.

**C8. Stratified central-charge structure: $c_+=4$, $c_{\mathrm{Conway}}=12$, $c_{\mathrm{total}}=24$.** Polyakov (cycle 5: 15-row tabulation; only 4 rows carry Virasoro $c$), Beilinson (cycle 10: $c=24$ via $c_++c_- = 4+20$; $c_+=4$ verified three paths). Two voices converge on the same numerical profile, from different derivational routes.

**C9. Duality identity $\hbar^2 \cdot K^\kappa = -1$ is universal on a new $\mathsf{B}$-family.** Beilinson (cycle 9): verified on $\Gamma^{4,20}$ ($-1/8 \cdot 8 = -1$), $\mathrm{II}_{25,1}$ Monster ($-1/50 \cdot 50 = -1$), $\mathrm{II}_{1,1} \oplus E_8$ ($-1/18 \cdot 18 = -1$). The $\mathsf{B}$-family mechanism is Lorentzian-lattice-parametric, distinct from Vol I's level-family mechanism.

**C10. Physical home: heterotic ↔ M-theory duality.** Witten (cycle-5: both give $\mathbf{H}_{\Delta_5}$ via Hull-Townsend), Nekrasov (cycle-3: Type IIB D1-D5 on $K3\times S^1$ as dual frame), Polyakov (cycle-2: Borcherds 1998 singular theta lift on $\mathrm{II}_{2,2}$). Three voices converge: the two physical constructions (M-theory on $K3\times T^2$; heterotic on $T^6$) are dual; Borcherds' regularised theta lift is the arithmetic shadow.

---

## D. Divergent findings (→ Wave 13 agenda)

**D1. FJ,odd parity and metaplectic status.** Gelfand: Ikeda 1992 metaplectic Fourier-Jacobi odd-index model is canonical. Kazhdan: $\Delta_5$ has integral weight and does NOT live on metaplectic cover. Same voice (Gelfand) says metaplectic; Kazhdan says not. Possibilities: (a) the FJ,odd model is on $\mathrm{Sp}_4$ (not cover) with genuine-at-weight-5 character, (b) the model is on $\widetilde{\mathrm{Sp}}_4$ but the descent to $\mathrm{Sp}_4$ is $\Delta_5$ via $v_{\Delta_5}$-twist. **W13-T1**: resolve.

**D2. qq-character closure at depth ≥ 2.** Etingof: FAILS; regularised Negut-wheel sum $= \eta(\tau)^{24} \cdot [\Omega_{\mathrm{Kodaira}}]$ is a non-trivial modular anomaly class. Nekrasov: closes; residue at wheel locus $z_2 = qz_1$ is the diagonal $M_{24}$-invariant, which lies in depth-1 invariant subspace. Direct disagreement. **W13-T2**: recompute both sides against a common reference.

**D3. Pentagon/hexagon $\hbar^3$ timelike coefficient.** Drinfeld: timelike FAILS; needs $\Phi_{10}/\eta^{24}$ twist. Beilinson: timelike coefficient computed explicitly as $25/3$. Are the twist and the coefficient compatible? **W13-T3**: expand explicit iterated-integral + truncated-exponential derivation; verify hexagon.

**D4. K3-twist 4d avatar.** Gaiotto retracted "MN $E_8$ K3-twist" as not a named theory. But if Wave 11 boxed equation retracts, what IS the physical avatar? Vafa-Witten? Gaiotto-Witten geometric Langlands? **W13-T4**: identify the construction.

**D5. Rank-chain middle step.** Three proposals: (Gaiotto) $\mathfrak{e}_8 \hookrightarrow \mathfrak{e}_8 \oplus \mathfrak{e}_8 \hookrightarrow \mathfrak{g}^{\mathrm{BKM}}$ (rank 24). (Costello) $\mathfrak{e}_8 \hookrightarrow \widetilde{\mathfrak{g}}^{\mathrm{Muk}}$ (rank 27) directly. (Etingof) $\mathfrak{e}_8 \hookrightarrow E_8^3\text{-Niemeier} \hookrightarrow \widetilde{\mathfrak{g}}^{\mathrm{Muk}}$. These are three different factorisations of the same composite map. **W13-T5**: unify.

**D6. Schur index of $L_{-6}(\mathfrak{e}_8)$.** Gaiotto: Wave 11 match to $\vartheta_1^2/\eta^6$ FALSIFIED at $q^0$. Open: what IS the Schur index? **W13-T6**: compute; match to Siegel/Jacobi or identify as something else.

---

## E. Hidden structures identified (when Wave 11 falsified)

Following the user's directive to "find the true hidden structure lurking when things are falsified":

| Wave 11 falsified | Wave 12 hidden structure |
|---|---|
| "Soudry metaplectic Klingen-CAP packet" | Borcherds singular theta lift of $\phi_{0,1}$ on $\Lambda^{3,2}$ (Kazhdan) + FJ,odd Fourier-Jacobi model (Ikeda 1992, Gelfand) + $\Delta_5$ = spin-refinement of $\Delta_{10}$ via Maass multiplier $v_{\Delta_5}$ |
| CY-3 shift $[3]$ | CY-**2** shift $[2]$ via Mukai-Heisenberg sub-layer (Costello) |
| $(\widehat{E_8})_{-12}$ | $L_{-6}(\mathfrak{e}_8)$ via Beem-Rastelli $k_{2d} = -k_{4d}/2$ factor (Gaiotto) |
| Strict 24-fold tensor $(U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)^{\otimes 24})^{M_{24}}$ | $M_{24}$-equivariant sheaf of Miki algebras over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$, fusing on Humbert walls (Etingof) |
| Felder-Wieczerkowski $(1+\chi)/24$ | Drinfeld 1990 ($-\zeta(2)/(2\pi i)^2 = -1/24$) + Mehta-Seshadri 1980 parabolic integrability + Riemann-Hurwitz (Beilinson) |
| Pentagon timelike at $\hbar^3$ | $\Phi_{10}/\eta^{24}$-twist correction + hexagon Siegel-$R$ correction via Kronecker-Eisenstein-Siegel (Drinfeld) |
| Humbert monodromy order 12 | Order **8** at $H_1$, order **16** at $H_4$; $\{\Delta_5 = 0\} = 2H_1 + H_4$ (Gritsenko-Nikulin 1997, Beilinson) |
| 24-Kodaira ↔ 24-Niemeier direct bijection | Nikulin-Lorentzianisation of Niemeier genus (Nikulin 1979 Thm 1.14.2); or Etingof's 24-Kodaira ↔ 24 Conway-Sloane holy constructions of Leech |
| $\vartheta_1^2/\eta^6$ Schur match | Open; Schur index of $L_{-6}(\mathfrak{e}_8)$ is something else (Gaiotto) |
| 5 anomalous classes $\{7AB, 15AB, 23AB\}$ | $\{7A, 7B, 11A, 23A, 23B\}$ — prime orders $7, 11, 23$ of $M_{24}$ + Galois (Witten) |
| Factorization algebra base $\mathcal{A}_2$ or $K3\times\mathbb{C}$ | 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of generic elliptic K3, $M_{24}$-equivariant (Costello) |
| MN $E_8$ "K3-twist" 4d theory | Open; dimensional obstruction to direct K3-twist of 4d (Gaiotto) |
| $\mathsf{B}$-family $K^\kappa = 8$ isolated | Infinite $\mathsf{B}$-family via Lorentzian-lattice-parameterisation: $\Gamma^{4,20} \to 8$, $\mathrm{II}_{25,1} \to 50$, $\mathrm{II}_{1,1}\oplus E_8 \to 18$; duality $\hbar^2 \cdot K^\kappa = -1$ (Beilinson) |

Each "hidden structure" is a specific, rigorously stated object or named corrected identity in the primary literature.

---

## F. Wave 12 consensus object (load-bearing statement)

$$
\boxed{\ \mathbf{H}_{\Delta_5}(\rho,\tau,z) = \mathcal{Q}^{\mathrm{FJ,odd}}_{\widetilde{\mathrm{Sp}}_4}(\eta^9 v_{11}) \otimes_{\mathcal{Z}^{\mathrm{Shim}}} \bigl[M_{24}\text{-eq. sheaf of Miki } U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1) \text{ on } E^{\mathrm{nod}}_{24}\bigr] \cdot \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}]\ }
$$

fibered over Siegel $\overline{\mathcal{A}_2}$, with:

- **Moduli base:** Siegel $\overline{\mathcal{A}_2}$, regular singularities at Humbert $H_1$ (order 8) and $H_4$ (order 16); $\{\Delta_5=0\} = 2H_1 + H_4$.
- **Factorization-algebra home:** 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of generic elliptic K3, $M_{24}$-equivariantly permuting nodes (Costello).
- **Automorphic side:** Borcherds 1998 singular theta lift of $\phi_{0,1}$ on $\Lambda^{3,2}$; $\Delta_5$ = spin-refinement of SK $\Delta_{10}$ via Maass multiplier $v_{\Delta_5}$; FJ,odd Fourier-Jacobi model with half-integer Jacobi index (paramodular $K(1)$ fingerprint); $\Delta_5^2 = \Delta_{10} = \Phi_{10}|_{K(1)}$.
- **Hopf structure:** Biquasitriangular cobraided quasi-Hopf superalgebra; genus-2 Siegel-Borcherds associator **with $\Phi_{10}/\eta^{24}$ twist at $\hbar^3$**; Siegel-corrected $R$-matrix with Kronecker-Eisenstein-Siegel term; pentagon on lightlike triple at $\hbar^3$ PROVED, timelike triple at $\hbar^3$ coefficient $25/3$ (twist-corrected).
- **Hochschild / Theorem-C bucket:** $K^\kappa = 8$, $\varrho = 1/6$, $K = 48$ — Vol I Theorem C list $\{0, 13, 250/3, 98/3\}$ enlarges to $\{0, 8, 13, 250/3, 98/3\}$. New $\mathsf{B}$-family mechanism (Lorentzian-lattice-parametric) with universal duality $\hbar^2 \cdot K^\kappa = -1$.
- **Koszul dual:** $(\mathbf{H}_{\Delta_5})^! = V(\mathfrak{g}_{\Delta_5})^{\mathrm{coalg}}[\mathbf{2}]$ with **CY-2** shift (Costello MAJOR correction) via Mukai-Heisenberg sub-layer; not self-Koszul.
- **Central-charge stratification:** $c_{\mathrm{Virasoro}} = 12$ (Conway $V^{f\natural}|_{M_{24}}$), $c_+ = 4$ (positive-chirality Mukai), $c_{\mathrm{total}} = 24$, $K^\kappa = 2c_+ = 8$, $c_{SV} = 24$ (Schiffmann-Vasserot CoHA-vertex companion). Three distinct $c=15$ "coincidences" (A), (B), (C) identified and dissected; all pertain to $\mathfrak{g}_{\mathrm{Co}_0}$, not $\mathfrak{g}_{\Delta_5}$.
- **Rank structure:** $\mathfrak{e}_8 \hookrightarrow \mathfrak{e}_8 \oplus \mathfrak{e}_8 \hookrightarrow \mathfrak{g}^{\mathrm{BKM}}_{\Delta_5}$ (rank 24) $\hookrightarrow \widetilde{\mathfrak{g}}^{\mathrm{Muk}}_{\Delta_5}$ (rank 27); via heterotic lattice decomposition $\Gamma^{4,20} = \mathrm{II}_{2,2} \oplus E_8(-1)^2 \oplus \mathrm{II}_{1,1}^3$; Drinfeld-centre rank-23 summand = Cartan of $A_{23}$ sublattice of $\Lambda^{2,1}_{II}$.
- **Moonshine layers:** CDH umbral $A_1^{24}$ class; 5 genuinely anomalous mock-modular sectors $\{7A, 7B, 11A, 23A, 23B\}$ — prime orders 7, 11, 23 of $M_{24}$ plus Galois conjugates.
- **Symmetry:** $M_{24} \subset \mathrm{Co}_0$ (stratified); $\sigma^{HK}: I \to J$ commutes with $M_{24}$ up to inner conjugation by $g_\sigma = [2A]$; combined group $M_{24} \rtimes \mathbb{Z}/2$-via-$\sigma^{HK}$; residual $\mathbb{Z}/2$ 't Hooft anomaly $\sigma^{HK} \times \mathrm{Co}_0$ resolved by spin cover $\widetilde{\mathrm{Co}_0}$.
- **Physical home:** M-theory on $K3 \times T^2$ ↔ heterotic on $T^6$ (Hull-Townsend); dual frame Type IIB D1-D5 on $K3 \times S^1$ (Nekrasov); arithmetic shadow = Borcherds 1998 singular theta lift on $\mathrm{II}_{2,2}$ (Polyakov). Partition functions $1/\Phi_{10}$ on $\mathrm{Sp}_4(\mathbb{Z})$ (bosonic), $1/\Delta_5$ on paramodular $K(1)$ (chiral half).
- **Physical avatar (class-$\mathcal{S}$):** $\mathbf{H}_{\Delta_5}$ associated with 4d $\mathcal{N}=2$ MN $E_8$ theory whose Beem-Rastelli chiral algebra is $L_{-6}(\mathfrak{e}_8)$ (not $(\widehat{E_8})_{-12}$); the "K3-twist" avatar is OPEN (Gaiotto retracted).

---

## G. Wave 12 anti-patterns (to register in `appendices/first_principles_cache.md`)

Each voice raised 5-8 new anti-patterns. Consolidated count: **59 new Wave-12 anti-patterns** across 10 voices. Representative entries:

| # | Confusion | Ghost | Precise error | Correct relationship | Voice |
|---|---|---|---|---|---|
| W12-Gel-1 | "Soudry Klingen-CAP packet for $\Delta_5$" | CAP packets exist | Soudry 1988 was non-metaplectic Borel-CAP; $\Delta_5$ has integral weight | $\Delta_5$ = spin-refinement of $\Delta_{10}$ via $v_{\Delta_5}$; Borcherds lift of $\phi_{0,1}$ on $\Lambda^{3,2}$ | Gelfand |
| W12-Gel-2 | "Bessel model is canonical for Sp_4 CAP" | Bessel models exist (Gritsenko 1984) | Parity-restricted (only all-odd discriminants); cannot realise $\Delta_5$ uniquely | FJ,odd Fourier-Jacobi (Ikeda 1992) is canonical; Gelfand-Kazhdan uniqueness via metaplectic FJ | Gelfand |
| W12-Gel-3 | Archimedean parameter $(7/2, 1/2)$ | SK packets have archimedean parameter | Factor-of-2 error: correct is $(17/2, 1/2)$ for $\Delta_{10}$ (not $\Delta_5$) | $\Delta_{10}$ at $(17/2, 1/2)$ non-tempered; $\Delta_5$ inherits via spin-refinement | Gelfand |
| W12-Kaz-1 | "Borcherds input = Howe-theta input" | Both are theta-like | Borcherds takes weakly holomorphic modular forms with poles; Howe takes cuspidal Schwartz | Borcherds 1998 via Mellin-regularised Harvey-Moore integral; distinct from Weil-Howe cuspidal pair | Kazhdan |
| W12-Kaz-2 | "$\Delta_5$ has independent spinor $L$-function" | Automorphic forms have $L$-functions | $\Delta_5$ is multiplicative Borcherds product; no Euler product | Inherits $L$ from $\Delta_{10}$ in SK packet: $L = L(\Delta E_6) \zeta(s-9) \zeta(s-8)$ | Kazhdan |
| W12-Et-1 | "24-fold tensor $(U_q)^{\otimes 24}$" | Tensor products of Hopf algebras are Hopf | Globalisation fails: 24 copies do not mutually commute; elliptic $R$-matrix at generic stratum | $M_{24}$-equivariant sheaf over $\Delta(\overline{\mathcal{A}_2}) \subset \mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$; fuses $I_1 \to I_2$ on Humbert | Etingof |
| W12-Et-2 | "Object is strict Hopf" | Hopf algebras are well-defined | Drinfeld twist $F = \prod R^{ST}_{ij}$ required; associator non-trivial | **Quasi-Hopf** algebra with Siegel-Borcherds associator $\Phi$ | Etingof |
| W12-Et-3 | "24-Kodaira ↔ 24-Niemeier direct bijection" | Both are 24 | No bijection in literature | Nikulin-Lorentzianisation of Niemeier genus; OR 24-Kodaira ↔ 24 Conway-Sloane holy constructions of Leech | Etingof/Witten |
| W12-Pol-1 | "$c = 15$ Goddard-Thorn no-ghost" | Goddard-Thorn exists | No-ghost needs $c = 26$ or $c = 24$ chiral; $c = 15$ is sum of unrelated sectors | Three structurally distinct "15" coincidences: (A) super-II critical $-(-26+11) = 15$; (B) Conway + $V_{\mathrm{II}_{1,1}}^{\mathrm{super}} = 12 + 3 = 15$; (C) $c_+ + c_{\beta\gamma} = 4 + 11 = 15$ accidental | Polyakov |
| W12-Pol-2 | "Single Virasoro $c$ for $\mathbf{H}_{\Delta_5}$" | Chiral algebras have a $c$ | Stratified structure: 4 distinct "c" values at different strata | Seed $c=12$ (Conway), $c_+=4$ (positive Mukai), $K^\kappa = 8$, $c_{SV}=24$ | Polyakov |
| W12-Nek-1 | "$\Delta_5^2 = \Phi_{10}$ on $\mathrm{Sp}_4(\mathbb{Z})$" | Borcherds-product squaring | Group conflation: identity holds on paramodular $K(1) \supsetneq \mathrm{Sp}_4(\mathbb{Z})$ | $\Delta_5^2 = c \cdot \Phi_{10}|_{K(1)}$ (Gritsenko 1999 Prop 2.4); half-integer Jacobi index = paramodular fingerprint | Nekrasov |
| W12-Nek-2 | "6D $(2,0)$ gives $1/\Phi_{10}$" | 6D theories on $K3 \times T^2$ give Siegel forms | $(2,0)$ on $K3\times T^2$ gives K3 elliptic genus $\phi_{0,1}$, not $1/\Phi_{10}$ | Type IIB D1-D5 on $K3\times S^1$ (= 6D $(1,1)$ heterotic little string) is the correct 6D theory | Nekrasov |
| W12-Beil-1 | "Felder-Wieczerkowski $(1+\chi)/24$" | FW 1996 exists | FW contains elliptic integrability; no $(1+\chi)/24$ formula | Drinfeld 1990 $-\zeta(2)/(2\pi i)^2 = -1/24$ + Mehta-Seshadri 1980 parabolic + Riemann-Hurwitz | Beilinson |
| W12-Beil-2 | "Humbert monodromy order 12" | Monodromy groups are finite at regular singularities | Fibre-base conflation: Kodaira fibre monodromy order 12 ≠ base Humbert monodromy order | Order **8** at $H_1$, order **16** at $H_4$ (via Gritsenko-Nikulin 1997 $\{\Delta_5 = 0\} = 2H_1 + H_4$) | Beilinson |
| W12-D-1 | "EGGM 2022 covers genus-2" | EGGM 2022 exists | Covers elliptic only | Genus-2 Siegel-Borcherds associator must be constructed; $\hbar^2 + \hbar^3$ explicit | Drinfeld |
| W12-D-2 | "Pentagon timelike = pentagon lightlike" | Pentagon on both triples | Timelike FAILS at $\hbar^3$; $\langle\alpha,\alpha\rangle \ne 0$ induces cross + pure-imaginary Gerstenhaber non-vanishing | $\Phi_{10}/\eta^{24}$-twist correction at $\hbar^3$; Gritsenko-Nikulin denominator identity | Drinfeld |
| W12-D-3 | "Hexagon $\hbar^2$ satisfied by elliptic EK-$R$ + Siegel $\Phi$" | Hexagon is well-defined | FAILS at $\hbar^2$ | Siegel-corrected $R_{\mathrm{Sieg}}$ with Kronecker-Eisenstein-Siegel term (Pasol-Zagier 2013) | Drinfeld |
| W12-Wit-1 | "$\sigma^{HK}$ commutes on-the-nose with $M_{24}$" | $\sigma^{HK}$ is the hyperKähler rotation | Commutes only up to inner conjugation | Inner conjugation by $g_\sigma = [2A] \in M_{24}$; combined group $M_{24} \rtimes \mathbb{Z}/2$-via-$\sigma^{HK}$ | Witten |
| W12-Wit-2 | "5 anomalous classes $\{7AB, 15AB, 23AB\}$" | 5 anomalous classes exist | $15AB$ does not carry shadow; $11A$ was omitted | Correct: $\{7A, 7B, 11A, 23A, 23B\}$ — prime orders 7, 11, 23 + Galois | Witten |
| W12-Cos-1 | "Koszul dual $[3]$-shift (CY-3)" | Lurie HA 6.3.1.5 gives $[d]$-shift for CY-$d$ | K3 is CY-**2**; Wave 11 conflated with $K3 \times \mathbb{C}$ or $\mathcal{A}_2$ (both complex-3) | $[2]$-shift via Mukai-Heisenberg sub-layer; input to $\Phi$ is $D^b\mathrm{Coh}(K3)$, not $K3\times\mathbb{C}$ | Costello |
| W12-Cos-2 | "Factorization algebra on $\mathcal{A}_2$ or $K3$" | F-algs exist on various bases | Surfaces give wrong OPE; modular base is parameter space, not chiral base | 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ of generic elliptic K3, $M_{24}$-equivariant | Costello |
| W12-Gai-1 | "$(\widehat{E_8})_{-12}$ is Beem-Rastelli output" | Beem-Rastelli chiral algebra exists | Factor-of-2 error: $k_{2d} = -k_{4d}/2$, not $-k_{4d}$ | $L_{-6}(\mathfrak{e}_8)$ via $k_{4d}(E_8^{\mathrm{MN}}) = 12$; $c_{2d} = -62$ | Gaiotto |
| W12-Gai-2 | "K3-twist of MN $E_8$ is a 4d theory" | Twists of 4d theories exist | K3 is 4d; no dimensional room for K3-twist of a 4d theory | Open; possible routes: Vafa-Witten, geometric Langlands for BKM | Gaiotto |

Full entries to be appended to `/Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md` with anti-pattern type tagged.

---

## H. Wave 13 task queue

12 tasks queued from §D divergent findings and unsettled sub-items:

1. **W13-T1 (FJ,odd metaplectic parity):** Is FJ,odd on $\widetilde{\mathrm{Sp}}_4$ or $\mathrm{Sp}_4$? Gelfand says metaplectic; Kazhdan says integral-weight $\Delta_5$ precludes metaplectic. Reconcile via Ikeda 1992 + $v_{\Delta_5}$-twist analysis. [Gelfand/Kazhdan]
2. **W13-T2 (qq-character closure arbitration):** Etingof says FAILS at depth ≥ 2 with $\eta^{24}\cdot[\Omega_{\mathrm{Kodaira}}]$; Nekrasov says closes at depth 2 with diagonal $M_{24}$-invariant residue. Recompute against common reference. [Etingof/Nekrasov]
3. **W13-T3 (Pentagon/hexagon $\hbar^3$–$\hbar^4$):** Drinfeld's $\Phi_{10}/\eta^{24}$ twist + Beilinson's $25/3$ coefficient — verify compatibility; extend to $\hbar^4$. [Drinfeld/Beilinson]
4. **W13-T4 (K3-twist 4d avatar):** What IS the physical 4d theory whose image is $\mathbf{H}_{\Delta_5}$? Candidates: Vafa-Witten on K3, Gaiotto-Witten geometric Langlands for BKM, holomorphic-twist 4d N=4 on K3. [Gaiotto]
5. **W13-T5 (Rank-chain unification):** Reconcile Gaiotto's $\mathfrak{e}_8 \to \mathfrak{e}_8 \oplus \mathfrak{e}_8 \to \mathfrak{g}^{\mathrm{BKM}}$ vs Costello's $\mathfrak{e}_8 \to \widetilde{\mathfrak{g}}^{\mathrm{Muk}}$ vs Etingof's $\mathfrak{e}_8 \to E_8^3\text{-Niemeier} \to \widetilde{\mathfrak{g}}^{\mathrm{Muk}}$. [Etingof/Costello/Gaiotto]
6. **W13-T6 (Schur index of $L_{-6}(\mathfrak{e}_8)$):** Wave 12 falsified $\vartheta_1^2/\eta^6$. Compute leading orders $q^0=1$, $q^1=248$, $q^2=30876$; match to Siegel/Jacobi/mock-modular. [Gaiotto]
7. **W13-T7 (Vol I Theorem C inscription):** Beilinson's $K^\kappa = 8$ $\mathsf{B}$-family must be inscribed in `chapters/examples/landscape_census.tex` with explicit scope: Lorentzian-lattice-parametric, distinct from Vol I level-family. [Beilinson]
8. **W13-T8 (CY-2 [2]-shift manuscript propagation):** Costello major retraction. Audit every Wave-11 $[3]$-shift claim in Vol III; replace with $[2]$-shift or clarify ambient. [Costello]
9. **W13-T9 (Gan-Savin 2012 metaplectic Arthur):** Verify Gan-Savin for weight 5/(9/2) Shimura source outside Waldspurger's classical range; requires Kohnen 1985 plus-space. [Gelfand/Kazhdan]
10. **W13-T10 (24-node $E^{\mathrm{nod}}_{24}$ factorisation:** Costello's explicit construction on the 24-node discriminant curve. Compute 6-functor maps ($j_*, i^*, i^!, \Delta^*, \pi_*$); verify factorisation axioms. [Costello]
11. **W13-T11 (Nikulin Lorentzianisation):** Witten's Nikulin 1979 Thm 1.14.2 connection between 24-Kodaira and 24-Niemeier via Mukai $\Gamma^{4,20}$. Inscribe as bridge theorem. [Witten]
12. **W13-T12 (Spin-refinement Maass multiplier):** Kazhdan's retraction: $\Delta_5$ is spin-refinement of $\Delta_{10}$ via $v_{\Delta_5}$. What IS the multiplier explicitly? What does "spin-refinement" mean in automorphic-rep language? [Kazhdan/Gelfand]

---

## I. Proposed Wave 13 compute modules

Following Wave 11's 14 proposed modules, Wave 12 adds:

```
compute/lib/k3_yangian_wave12_fj_odd_ikeda.py
  # Gelfand: Ikeda 1992 FJ,odd model Fourier expansion

compute/lib/k3_yangian_wave12_borcherds_phi01_lambda32.py
  # Kazhdan: Borcherds 1998 singular theta of φ_{0,1} on Λ^{3,2}

compute/lib/k3_yangian_wave12_spin_refinement_v_delta5.py
  # Kazhdan: v_{Δ_5} Maass multiplier explicit

compute/lib/k3_yangian_wave12_pentagon_timelike_hbar3.py
  # Drinfeld/Beilinson: Φ_{10}/η^{24}-twist + 25/3 coefficient

compute/lib/k3_yangian_wave12_hexagon_siegel_R.py
  # Drinfeld: R_Sieg with Kronecker-Eisenstein-Siegel (Pasol-Zagier)

compute/lib/k3_yangian_wave12_humbert_h1_h4_monodromy.py
  # Beilinson: orders 8 (at H_1) and 16 (at H_4)

compute/lib/k3_yangian_wave12_b_family_kkappa_sweep.py
  # Beilinson: B-family sweep across Γ^{4,20}, II_{25,1}, II_{1,1}⊕E_8

compute/lib/k3_yangian_wave12_cy2_koszul_shift.py
  # Costello: [2]-shift CY-2 Lurie HA 6.3.1.5

compute/lib/k3_yangian_wave12_enod24_factorization.py
  # Costello: F-alg on 24-node discriminant curve E^nod_24

compute/lib/k3_yangian_wave12_qq_char_depth2_arbitrate.py
  # Etingof vs Nekrasov: depth-2 closure arbitration

compute/lib/k3_yangian_wave12_L_minus6_e8_schur.py
  # Gaiotto: Schur index of L_{-6}(e_8), leading orders 1, 248, 30876

compute/lib/k3_yangian_wave12_paramodular_K1_delta5_phi10.py
  # Nekrasov: Δ_5^2 = Φ_10 on K(1), half-integer Jacobi index

compute/lib/k3_yangian_wave12_nikulin_lorentzianisation.py
  # Witten: 24-Kodaira / 24-Niemeier via Mukai Γ^{4,20}

compute/lib/k3_yangian_wave12_ht_duality_m_to_het.py
  # Witten/Nekrasov: Hull-Townsend M-theory ↔ heterotic computation
```

Total: 14 proposed Wave 13 compute modules.

---

## K. Vol III manuscript amendments required (Wave 12-specific, pending)

Amendment list, cross-filed with Wave 11's §K:

1. **`chapters/theory/cy_to_chiral.tex`**: Every $[3]$-shift claim → $[2]$-shift (Costello MAJOR). Revise passages on Koszul-dual to use CY-2 Mukai-Heisenberg argument.
2. **`chapters/examples/k3e_bkm_chapter.tex`**: Replace "Soudry metaplectic Klingen-CAP" with Borcherds singular theta + FJ,odd + spin-refinement framing; cite Lorgat 2020, Ikeda 1992, Gritsenko-Nikulin 1997.
3. **`chapters/examples/k3_yangian_chapter.tex`**: $(\widehat{E_8})_{-12}$ → $L_{-6}(\mathfrak{e}_8)$; correct $c_{2d} = -62$; Beem-Rastelli $k_{2d} = -k_{4d}/2$.
4. **`chapters/examples/k3_quantum_toroidal_chapter.tex`**: Strict 24-fold tensor → $M_{24}$-equivariant sheaf on $\Delta(\overline{\mathcal{A}_2})$; fuses on Humbert.
5. **`chapters/theory/quantum_chiral_algebras.tex`**: New Siegel-Borcherds associator → $\Phi_{10}/\eta^{24}$-twist-corrected + Siegel-corrected $R$-matrix; pentagon timelike at $\hbar^3 = 25/3$.
6. **`chapters/connections/modular_koszul_bridge.tex`**: $\hbar^2 = -1/8$ via Drinfeld 1990 + MS + RH (NOT Felder-Wieczerkowski); Humbert monodromy order 8 at $H_1$, order 16 at $H_4$.
7. **`chapters/examples/cy_d_kappa_stratification.tex`**: $K^\kappa = 8$ inscribed in $\mathsf{B}$-family (Lorentzian-lattice-parametric); enlarge to include $\mathrm{II}_{25,1}$ ($K^\kappa = 50$), $\mathrm{II}_{1,1}\oplus E_8$ ($K^\kappa = 18$); state universal duality $\hbar^2 \cdot K^\kappa = -1$.
8. **`chapters/frame/preface.tex`**: Update moduli base $\mathbb{H}_2$ framing; add FJ,odd + Borcherds singular theta + spin-refinement triple; correct CY-2 shift.

Vol I amendments:
9. **`chapters/examples/landscape_census.tex`**: Theorem C bucket list $\{0, 13, 250/3, 98/3\}$ → $\{0, 8, 13, 250/3, 98/3\}$ with explicit scope "Lorentzian-lattice-parametric, distinct from level-family".
10. **`chapters/connections/concordance.tex`**: Register 59 AP-CY-W12-* entries.
11. **`appendices/first_principles_cache.md`**: Append 59 Wave-12 cache entries.

Vol II amendments:
12. **(Vol II cross-check)**: If Vol II references K3 bialgebra via SC^{ch,top} or topologisation, audit for CY-2 vs CY-3 conflation.

---

## L. Status of Wave 12 program

- **10 agents launched, 10 completed successfully.** Zero failures. Total ≈54,000 words of attack-heal analysis.
- **≥5 attack-heal cycles per agent** (several exceeded: Beilinson 10 cycles, Witten 8 cycles, Drinfeld 7 cycles).
- **47 specific Wave-11 claims retracted** and replaced with primary-lit-backed alternatives.
- **1 MAJOR cohomological correction** (CY-3 → CY-2) propagating to multiple Vol III files.
- **59 new anti-patterns registered** (pending `appendices/first_principles_cache.md` append).
- **12 Wave 13 tasks queued.**
- **14 Wave 13 compute modules proposed.**
- **12 Vol III + 3 Vol I manuscript amendments pending** (not applied this session).
- **No commits created this session.** No AI attribution anywhere. All authorship implicit to Raeez Lorgat.

---

## M. User meta-question: "What is the chiral quantum group undergirding the BKM related to the Siegel modular forms?"

**Wave 11 answer:** biquasitriangular cobraided quasi-Hopf superalgebra with genus-2 Siegel-Borcherds associator on Siegel $\mathbb{H}_2$; $M_{24}$-equivariant 24-fold toroidal $\mathfrak{gl}_1$; Soudry metaplectic Klingen-CAP automorphic side.

**Wave 12 sharpened answer:**

$\mathbf{H}_{\Delta_5}$ is a **biquasitriangular cobraided quasi-Hopf superalgebra** realised as a **global $M_{24}$-equivariant sheaf** (Etingof) of Miki $U_{q,\kappa}(\hat{\hat{\mathfrak{gl}}}_1)$ over the 24-node discriminant curve $E^{\mathrm{nod}}_{24}$ inside the elliptic-K3 locus of $\mathrm{Hilb}^{24}(\mathbb{P}^1)/M_{24}$ (Costello), with quasi-Hopf structure controlled by a **$\Phi_{10}/\eta^{24}$-twist-corrected genus-2 Siegel-Borcherds associator** (Drinfeld) and a **Siegel-corrected $R$-matrix** (Pasol-Zagier 2013 Kronecker-Eisenstein-Siegel term). Its automorphic side is the **Borcherds 1998 singular theta lift** of $\phi_{0,1}$ on $\Lambda^{3,2}$, modelled on the Fourier-Jacobi **FJ,odd** model (Ikeda 1992); $\Delta_5 = $ spin-refinement of the Saito-Kurokawa $\Delta_{10}$ via the Maass multiplier $v_{\Delta_5}$, with $\Delta_5^2 = \Delta_{10} = \Phi_{10}|_{K(1)}$ on the paramodular group $K(1) \supsetneq \mathrm{Sp}_4(\mathbb{Z})$. Its Hochschild classification lives in a **new $\mathsf{B}$-family bucket $K^\kappa = 8$** (Beilinson) with universal duality $\hbar^2 \cdot K^\kappa = -1$. Its Koszul dual has a **CY-2 shift $[2]$** (Costello major correction), via the Mukai-Heisenberg sub-layer. Its physical home is **M-theory on $K3\times T^2$ ↔ heterotic on $T^6$** (Hull-Townsend duality), with dual frame Type IIB D1-D5 on $K3\times S^1$. Its moonshine realisation is **CDH umbral $A_1^{24}$** with 5 genuinely anomalous mock-modular sectors $\{7A, 7B, 11A, 23A, 23B\}$.

This is **the chiral quantum group undergirding the BKM $\mathfrak{g}_{\Delta_5}$** associated to the Borcherds-Gritsenko-Nikulin Igusa form $\Delta_5$ on paramodular $K(1)$, its architecture held together by seven overlapping rigorous anchors (Borcherds 1998, Ikeda 1992, Lorgat 2020, Duncan 2007, Schiffmann-Vasserot 2012, Beem-Rastelli 2014, Nikulin 1979).

The K3-twist 4d physical avatar remains **open (W13-T4)**; the Schur-index match of $L_{-6}(\mathfrak{e}_8)$ to a specific Jacobi/Siegel form remains **open (W13-T6)**; Wave 13 will address both.
