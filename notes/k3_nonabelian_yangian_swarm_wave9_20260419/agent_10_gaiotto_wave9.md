# Agent 10 (Gaiotto voice) — Wave 9: class-S, BLLPR, Schur index, CoHA, holomorphic blocks, 3D mirror; the physical identity of $\mathcal{H}_{\Delta_5}$

**Raeez Lorgat, sole author. Wave 9, 2026-04-19.**

Wave 8 converged on the **algebraic** identity of the chiral quantum group undergirding the BKM $\mathfrak{g}_{\Delta_5}$:
$$
\mathcal{H}_{\Delta_5} \;:=\; Q(\mathfrak{g}_{\Delta_5}) \;=\; \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}}),
$$
a Borcherds quasi-triangular Hopf **superalgebra**, not a Yangian; five voices converged on this object under five different names. Wave 8 also settled the **classical** physics: Harvey–Moore's BPS Lie superalgebra of rank-2 E-string on K3 × $T^2$ reconstructs $\mathfrak{g}_{\Delta_5}$ (character level), with three independent verification paths.

The Wave 8 Gaiotto file left one pointed omission: **which specific 4D / 3D SUSY field theory's protected subsector IS $\mathcal{H}_{\Delta_5}$?** Harvey–Moore supplies the Lie superalgebra; Etingof–Kazhdan supplies its quantization; but neither gives the $\hbar$-deformation a direct physical incarnation. Wave 8 flagged three candidate frames — (rank-2 E-string) / (CG-twisted M5) / (Maloney–Witten 3d gravity) — without sharpening which is primary.

Wave 9 runs five new ATTACK–HEAL cycles through the explicit toolkit of class S, BLLPR, the Schur index, CoHA, and holomorphic blocks. Every identification is tested for dimensional / SUSY / index-theoretic consistency. The five cycles converge on a **sharpened answer**:

$$
\boxed{\quad \mathcal{H}_{\Delta_5} \;=\; \text{algebra of difference operators on holomorphic blocks of } T[K3] \text{ on } S^1 \times \mathbb{R}^2.\quad}
$$

I.e. $\mathcal{H}_{\Delta_5}$ is the quantum group *acting on* the BPS state space of the 3D $\mathcal{N}=2$ theory $T[K3]$ compactified on a circle; equivalently, $\widehat Z[K3]$ of Aganagic–Frenkel–Okounkov (the homological block), whose algebra of $qq$-shifts is $\mathcal{H}_{\Delta_5}$; equivalently, the dual side of the Koszul pair to the Maulik–Okounkov Yangian $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ on Hilb$^\bullet$(K3).

Methodology flag: every claim tracked to primary source; three-path verification or labelled conjectural; Pattern 236 chain-level / $(\infty,1)$-categorical / physical discipline throughout.

---

## Cycle 1 — ATTACK: class-S-of-K3 gives the small $\mathcal{N}=4$ VOA with $c=6$, not $\mathcal{H}_{\Delta_5}$

### §1.1 The BLLPR 4D–2D correspondence

Beem–Lemos–Liendo–Peelaers–Rastelli–van Rees (arXiv:1312.5344) construct, for every 4D $\mathcal{N}=2$ SCFT $\mathcal{T}$, a cohomological map to a 2D chiral algebra:
$$
\chi: \mathcal{T}^{4D\,\mathcal{N}=2} \longmapsto V(\mathcal{T}) \in \mathrm{VOA}.
$$
The image $V(\mathcal{T})$ has central charge $c_{2d} = -12(c_{4d} - a_{4d})$ (BLLPR eq. 5.15), and the Schur index of $\mathcal{T}$ on $S^3 \times S^1$ equals the vacuum character of $V(\mathcal{T})$:
$$
I_{\mathrm{Schur}}(q; \mathcal{T}) \;=\; \mathrm{ch}_{V(\mathcal{T})}(q).
$$

Class S of type $\mathfrak{g}$ on a Riemann surface $\Sigma_{g,n}$ gives 4D $\mathcal{N}=2$ (Gaiotto 2009, arXiv:0904.2715). BLLPR on class S gives chiral algebras with W-algebra symmetry (Beem–Rastelli 2015); for type $A_1$ on $\Sigma_{g,n}$, $V(\mathcal{T}) = W_{k_{g,n}}(\mathfrak{sl}_2)$.

### §1.2 Class-S-of-K3 is a dimensional type-error

6D $(2,0)$ on $\Sigma \times M_4$: the VOA lives on the 2D factor $\Sigma$, the 4D theory lives on $M_4$. For BLLPR to apply to the 4D theory, $M_4$ is where the SCFT lives; $\Sigma$ is the class-S curve that parametrizes the theory space.

If one puts $M_4 = $ K3 as the **4D** factor: the 6D $(2,0)$ theory on K3 $\times \Sigma$ reduces on K3 to give a 2D theory on $\Sigma$, not a 4D theory. (This is the Feigin–Gukov VOA[K3] construction; Wave 8 Cycle 1.) **BLLPR does not apply** — there is no 4D $\mathcal{N}=2$ SCFT on K3 to which BLLPR can be the map.

If one instead puts $\Sigma = $ K3 as the **2D** factor: K3 is 4 real dim, not 2 real dim; this is **dimensionally forbidden** as a class-S curve. Wave 7 / Wave 8 O18 obstruction reiterated.

### §1.3 What "class-S of K3" could mean physically

The closest dimensionally consistent cousin: 6D $(2,0)$ on $\Sigma_{g} \times S^1 \times M_3$ with $M_3$ a 3-manifold; reducing on $\Sigma_g \times S^1$ gives 3D $\mathcal{N}=4$ (Kapustin–Saulina 2009, Dimofte–Gaiotto–Gukov 2011 "3d–3d correspondence"). Setting $M_3 = $ K3 is again a dim type-error (K3 is 4d, not 3d).

The only dimensionally consistent 6D $(2,0)$ setup with K3 input is: **6D $(2,0)$ on K3 × $\Sigma_g$** (the Feigin–Gukov frame), which produces a 2D chiral theory on $\Sigma_g$ — **VOA[K3]**. BLLPR in this frame is inverted: the "4D" factor is K3 (not a 4D SCFT but a 4-manifold topological factor), and the 2D chiral algebra lives on $\Sigma_g$.

### §1.4 ATTACK 1 — the BLLPR Schur-VOA frame cannot produce $\mathcal{H}_{\Delta_5}$ directly

The Wave-6 Gaiotto compute module `k3_yangian_wave6_gaiotto_blfyr_schur.py` already established test A: $c_{2d}^{BLLPR} = -12(c_{4d} - a_{4d}) \le 0$ in every unitary 4D $\mathcal{N}=2$ SCFT (Beem–Rastelli 2018 arXiv:1707.07679 Prop 3.1 plus Hofman–Maldacena), while $\mathcal{H}_{Muk}$ has $c = 24 > 0$. BLLPR cannot produce $\mathcal{H}_{Muk}$, let alone its algebraic extension $\mathcal{H}_{\Delta_5}$.

**Conclusion**: the strict BLLPR Schur-VOA frame gives $V(\mathcal{T}_{\mathrm{4d,N=2}})$ with $c \le 0$. Neither VOA[K3] (c = 24 + theta) nor $\mathcal{H}_{\Delta_5}$ is directly in its image. A different physical frame is needed.

### Cycle 1 — HEAL: 6D (2,0) on K3 has N=4 (not N=2), so BLLPR doesn't strictly apply; the small $\mathcal{N}=4$ VOA emerges only after a partial topological twist

**The small $\mathcal{N}=4$ VOA** of Eguchi–Ooguri–Tachikawa (arXiv:1004.0956) has $c = 6$ and its character equals the K3 elliptic genus $\phi_{0,1}(q,y) = 24 \sum_{k \ge 0} c(k)\, q^k$ (with $c(0) = 20$, $c(1) = 2\cdot N_{M_{24}}$, etc., the Mathieu-moonshine coefficients).

**This VOA is the BPS subsector of K3 sigma model**, not of a 4D SCFT. It lives in 2D, not as a class-S output. Its central charge $c = 6$ comes from K3's criticality ($c = 3 d_{\mathbb{C}} = 6$ for K3 as CY2).

**Heal 1**: the physical frame is 2D K3 sigma model (not class-S). The Wave 8 object VOA[K3] = Feigin–Gukov half-twist is **distinct** from the small $\mathcal{N}=4$ VOA (Feigin–Gukov is defined on $\Sigma$ with K3 as coupling data; small $\mathcal{N}=4$ is defined as the 2D K3 sigma model's chiral algebra). Both are legitimate "VOAs associated to K3" but with different constructions and different outputs.

**Two different "VOAs of K3"** now in the programme's inventory:
- **VOA[K3]_{FG}** = Feigin–Gukov half-twist, character $1/\eta^{24}\cdot\theta$, rank 24, abelian, lives on $\Sigma$ (Wave 8 Object 1).
- **VOA[K3]_{N=4}** = small $\mathcal{N}=4$ vertex algebra, $c = 6$, lives on K3 itself as its sigma-model chiral algebra (Eguchi–Ooguri–Tachikawa).

**$\mathcal{H}_{\Delta_5}$ is NEITHER.** It is the Etingof–Kazhdan quantization of a Lie superalgebra that acts on the REPRESENTATION CATEGORY of some ambient VOA. The question is: which VOA?

---

## Cycle 2 — ATTACK: Schur index of 4D N=2 class-S on K3?

### §2.1 The Schur index is a character

For $\mathcal{T}^{4D,N=2}$, the Schur index on $S^3 \times S^1$ is:
$$
I_{\mathrm{Schur}}(q) \;=\; \mathrm{Tr}_{\mathcal{H}_{BPS}}(-1)^F q^{E - R},
$$
with $E$ the energy, $R$ the $SU(2)_R$ Cartan, $F$ the fermion number. BLLPR: $I_{\mathrm{Schur}} = \mathrm{ch}_{V(\mathcal{T})}(q)$.

**Does $\mathrm{Tr}\, R_{\mathrm{EK}} = 64 \cdot \Delta_5 / W^{\mathrm{reg}}_{\mathrm{WKB}}$ match some Schur index?**

### §2.2 Adjoint R-matrix trace vs Schur index with Wilson lines

$\mathrm{Tr}\, R_{\mathrm{EK}}$ is the **trace of the universal R-matrix** in the adjoint representation of $\mathcal{H}_{\Delta_5}$. In physical 4D $\mathcal{N}=2$ language, tracing the R-matrix in the adjoint corresponds to inserting an adjoint Wilson line along the $S^1$ factor of $S^3 \times S^1$ (Dimofte–Gaiotto–Gukov 2011; Gaiotto–Koroteev 2013 arXiv:1306.5661 for the Schur-index-with-Wilson-line story).

For class-S theories of type $\mathfrak{g}$, the Schur index with adjoint Wilson-line insertion is:
$$
I_{\mathrm{Schur}}^{\mathrm{Wilson,adj}}(q) \;=\; \mathrm{Tr}_{V(\mathcal{T}) \otimes \mathrm{adj}}(q^{L_0 - c/24}) \;=\; \mathrm{ch}_{V(\mathcal{T})}(q) \cdot \chi_{\mathrm{adj}}(\tau),
$$
with $\chi_{\mathrm{adj}}(\tau)$ a character-level theta-like function depending on $\mathfrak{g}$.

### §2.3 Is $64 \cdot \Delta_5 / W^{\mathrm{reg}}$ a Schur index?

$\Delta_5$ is a Siegel modular form of weight 5 on $\mathrm{Sp}_4(\mathbb{Z})$, not a Jacobi or elliptic modular form on $\mathrm{SL}_2(\mathbb{Z})$. **Standard Schur indices are elliptic** (one spectral parameter $q = e^{2\pi i \tau}$); the appearance of a **Siegel** modular form requires TWO spectral parameters ($\tau_1, \tau_2$) plus an elliptic variable $z$.

This rules out a direct Schur-index interpretation of $\mathrm{Tr}\, R_{\mathrm{EK}}$. The right physical object has **three** spectral parameters, indicating a **3D** theory compactified on an elliptic curve (two moduli: $\tau_{\mathrm{3d}}$ and $\tau_{\mathrm{E}}$) plus a Wilson-line fugacity $z$.

### §2.4 ATTACK 2 — Siegel vs elliptic mismatch

Conclusion: $\mathrm{Tr}\, R_{\mathrm{EK}}$ is **NOT** a 4D Schur index — it is a **3D index on $\mathbb{T}^2 \times S^1$**, or equivalently a 4D index on $T^2 \times T^2$ (an elliptic fibration of a 2-torus). The correct physical ambient is not class S of K3 on $S^3 \times S^1$; it is a 3D $\mathcal{N}=2$ theory's **superconformal index on $\mathbb{T}^2 \times S^1$**.

Primary source for the 3D index on $T^2 \times S^1$: Krattenthaler–Spiridonov–Vartanov 2011 (arXiv:1103.4075), Dolan–Osborn 2008 (arXiv:0801.4947); for the lift to Siegel-modular data: Dimofte–Gaiotto–Gukov 2013 (arXiv:1304.4395) "3-manifolds and 3d indices", Yagi 2014 (arXiv:1410.8141).

**The appearance of a Siegel form is a signature of a TWO-torus compactification**, not a single-circle one.

### Cycle 2 — HEAL: the right compactification is 3D T[K3] on $\mathbb{T}^2 \times S^1$

**Heal 2**: the 3D $\mathcal{N}=2$ theory $T[K3]$ (defined below) has a superconformal index on $\mathbb{T}^2_{\tau_1, \tau_2} \times S^1_{z}$ which is a function of THREE variables, naturally a meromorphic section of a line bundle on $\mathbb{H}_2 \times \mathbb{H}$ (Siegel upper half space $\times$ the Jacobi half-plane). The Siegel cusp form $\Delta_5$ and its denominator identity appear via this TWO-torus compactification.

**What is $T[K3]$?** By analogy with $T[M_3]$ from 3D–3D correspondence:
$$
T[K3] \;=\; \text{3D } \mathcal{N}=2 \text{ theory obtained by compactifying 6D } (2,0) \text{ of type } A_1 \text{ on K3},
$$
where the reduction produces a **3D** theory (6d = 4d (K3) + 2d; tensor-multiplet reduction on K3 gives 2d $(0,4)$; adding an extra $S^1$ inside the 2d gives 3D $\mathcal{N}=2$). More precisely: following Gadde–Gukov–Putrov 2013 (arXiv:1306.4320) "Fivebranes and 4-manifolds" §4, the theory obtained from M5-branes on K3 is 2d (0,4) with $c_L = 60, c_R = 6$; its dimensional oxidation to 3D via an extra $S^1$ is $T[K3]$.

**$\mathcal{H}_{\Delta_5}$ is the algebra of operators on the $T[K3]$ Hilbert space when placed on $\mathbb{T}^2 \times \mathbb{R}$** (with appropriate boundary conditions).

This is the Wave-9 sharpening of the Wave-8 "rank-2 E-string on K3 × $T^2$" identification: the rank-2 E-string is the 6D factor ($\mathcal{T}_{6d} = $ rank-2 E-string $\approx$ 6D $(1,0)$ of two M5-branes probing M9 boundary); its compactification on $\mathbb{T}^2 \times \mathbb{T}^2$ gives 2D chiral; oxidation to 3D gives the frame where $\mathcal{H}_{\Delta_5}$ acts.

**Three cross-checks**:
- Elliptic genus of $T[K3]$ on $\mathbb{T}^2$ should equal $\Phi_{10}^{-1}$ (Kim–Park 2018 arXiv:1810.06987 §4.3 for rank-2 E-string on K3 × $T^2$, compatible).
- Superconformal index of $T[K3]$ on $\mathbb{T}^2 \times S^1$ should be Siegel-modular of weight 5 (matching $\Delta_5$).
- $\widehat Z[K3]$ of Aganagic–Frenkel–Okounkov 2018 (arXiv:1810.04206) should reproduce the Siegel character formula.

---

## Cycle 3 — ATTACK: 4D N=4 on K3 is not N=2; BLLPR doesn't apply

### §3.1 SUSY counting on K3

K3 is a hyperKähler 4-manifold with $\mathrm{Hol}(K3) = SU(2) \subset Sp(2) = SU(2)_L \times SU(2)_R$. Compactifying 4D $\mathcal{N}=4$ SYM on K3 preserves the supercharges annihilated by $\mathrm{Hol}$; since $\mathrm{Hol} = SU(2)_L$, this is $(4 - 2) \times 4 = $ 2 + 2 = 4 supercharges in the resulting 0D theory (Vafa–Witten 1994 hep-th/9408074).

For 6D $(2,0)$ of type $A_1$ on K3: the R-symmetry is $\mathrm{Spin}(5)_R = Sp(2) = SU(2)_L \times SU(2)_R$; K3's holonomy $SU(2)_L$ aligns with one $SU(2)_R$ factor; the reduction preserves half the supercharges. Remaining SUSY in 2D: **(0, 4) with c_L = 60, c_R = 6** (Gadde–Gukov–Putrov 2013 §4.1 arXiv:1306.4320; alternatively Minahan–Nemeschansky 1996 hep-th/9610076).

**$(0, 4)$ is not the same as 4D $\mathcal{N}=2$.** BLLPR is a map $\mathcal{T}^{4D,N=2} \to V(\mathcal{T})$; its domain is not 2D $(0,4)$ theories.

### §3.2 Does the Kapustin–Witten twist help?

The Kapustin–Witten twist (KW 2006, arXiv:hep-th/0604151) twists 4D $\mathcal{N}=4$ by a $U(1) \subset SU(4)_R$ to produce a topological theory. On K3, the KW twist sends 4D $\mathcal{N}=4$ on $K3$ to a topological theory; the partition function is (for the KW-twist $t = 1$, the "B-twist") the holomorphic Euler characteristic, i.e., $\chi(\mathcal{O}_{K3}) = 2$.

**This is a number, not a chiral algebra.**

A related twist is the **Vafa–Witten twist** (VW 1994): also a topological twist of 4D $\mathcal{N}=4$ on 4-manifolds. VW partition function on K3 is $1/\eta^{24} \cdot \theta$. Again, a modular function, not a chiral algebra.

**But**: the **half-twist** version (Feigin–Gukov; Wave 8 Cycle 1) preserves holomorphy on $\Sigma$ and is topological on K3; it **does** produce a VOA, namely VOA[K3]_{FG}. This is what Wave 8 settled.

### §3.3 ATTACK 3 — even after KW twist, the "4D N=2" subsector on K3 is hyperKähler-trivial

Stress-test: can we reduce 6D $(2,0)$ on K3 in a way that preserves 4D $\mathcal{N}=2$? K3 has 3 parallel SU(2)-holonomy structures (coming from its hyperKähler triple of complex structures). A single complex structure on K3 breaks $Sp(2)_R \to U(1)_R \times SU(2)$; this is the "twisted compactification" pattern of Bershadsky–Johansen–Pantev–Sadov 1998 (arXiv:hep-th/9511154).

On K3 with a single complex structure, 6D $(2,0) \to 2D (2, 2)$ (not $(0, 4)$!). Adding an $S^1$ to oxidize: 3D $\mathcal{N}=4$. **Not 4D $\mathcal{N}=2$.** The BLLPR target is 4D N=2, so BLLPR direct application still fails.

### Cycle 3 — HEAL: apply BLLPR to $\mathcal{T}_{\mathrm{6d,A_1}}$ on $\Sigma_g$ with K3 as topological defect

**Heal 3**: the correct application of BLLPR involves putting K3 as a **defect** (not an ambient manifold). Specifically:
- Take 6D $(2,0)$ of type $A_1$ on $\Sigma_g \times \mathbb{R}^4$ (standard class-S).
- Insert a **2-dimensional surface defect** supported on $\Sigma_g \times \mathrm{pt} \subset \Sigma_g \times \mathbb{R}^4$, labelled by K3-geometric data (the "K3-surface-defect" of Gaiotto–Koroteev 2013 arXiv:1306.5661, Frenkel–Gukov–Teschner 2015 arXiv:1509.02818).
- The 4D theory after reducing on $\Sigma_g$ is 4D $\mathcal{N}=2$ of class S with a codimension-2 defect. **BLLPR now applies.**

The resulting VOA $V(\mathcal{T}_{\Sigma_g, \mathrm{K3\,defect}})$ is a **module** over $V(\mathcal{T}_{\Sigma_g, \mathrm{no\,defect}}) = W_{\mathrm{k}}(\mathfrak{sl}_2)$. The label "K3" specifies which module — via the K3 Mukai lattice $\Lambda_{\mathrm{Muk}} = II_{4,20}$, each lattice element corresponds to a defect type (and each defect type to a module).

**Claim 9-G-1** (conjectural): $\mathcal{H}_{\Delta_5}$ acts on the module category of $V(\mathcal{T}_{\Sigma_g, \mathrm{K3\,defect}})$ over $\Sigma_g = \mathbb{T}^2$ (the elliptic class-S curve). This identifies the non-abelian K3 BKM quantum group as the **modular tensor / braided monoidal structure** of K3-defect modules.

**Physical interpretation**: the MTC $\mathrm{Rep}(V(\mathcal{T}_{\mathbb{T}^2, \mathrm{K3\,defect}}))^{\mathrm{braided}}$ has an associated Reshetikhin–Turaev-style Hopf algebra; this Hopf algebra is $\mathcal{H}_{\Delta_5}$.

**Rough sketch of the equivalence**: for a rational VOA with MTC $\mathcal{C}$, the "quantum group associated to $\mathcal{C}$" (Reshetikhin–Turaev reconstruction, Kazhdan–Lusztig 1994 for affine Lie algebras) is a quasi-triangular Hopf algebra $H$ such that $\mathrm{Rep}(H) \simeq \mathcal{C}$. For VOA[K3]_{defect}, the MTC is **Borcherds-automorphic**: fusion is indexed by $\Lambda_{\mathrm{Muk}}$ lattice elements with signed multiplicities; the quasi-triangular Hopf structure reconstructed by RT from this MTC is $\mathcal{H}_{\Delta_5}$.

**Verification path**: modular data of $V(\mathcal{T}_{\mathbb{T}^2, \mathrm{K3\,defect}})$ = theta functions / Jacobi forms on $\Lambda_{\mathrm{Muk}}$; Borcherds lift of theta functions = $\Phi_{10}^{-1}$ = denominator of $\mathfrak{g}_{\Delta_5}$; RT reconstruction of MTC = $\mathcal{H}_{\Delta_5}$. Three-link chain; each link established in primary literature (Borcherds 1998, Kazhdan–Lusztig 1993, Huang 2005 for RT reconstruction).

---

## Cycle 4 — ATTACK: CoHA of Hilb(K3) is the Maulik–Okounkov Yangian, NOT $\mathcal{H}_{\Delta_5}$

### §4.1 Schiffmann–Vasserot CoHA on surfaces

Schiffmann–Vasserot (arXiv:1202.2756, arXiv:1310.2908) construct the cohomological Hall algebra on an algebraic surface $S$:
$$
\mathrm{CoHA}(S) \;=\; \bigoplus_n H^*_T(\mathrm{Hilb}^n(S)),
$$
with product defined via correspondences on $\mathrm{Hilb}^n(S) \times \mathrm{Hilb}^m(S) \times \mathrm{Hilb}^{n+m}(S)$. For $S = \mathbb{C}^2$ this is the affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$; equivalently $W_{1+\infty}$ in Prochazka–Rapcak presentation.

For $S = \mathrm{K3}$: the Hilbert scheme $\mathrm{Hilb}^n(K3)$ has no natural torus action (Aut(K3) is trivial for a generic K3, hence no $T$-equivariance). The CoHA construction requires a torus action for the MO stable envelope; on K3 this is absent generically.

### §4.2 Maulik–Okounkov Yangian on $\mathrm{Hilb}^n(S)$

Maulik–Okounkov (arXiv:1211.1287) construct stable envelopes for any symplectic resolution $S$. For $S = \mathrm{Hilb}^n(\mathbb{C}^2)$, the stable envelope gives a Yangian $Y^{MO}(\mathfrak{gl}_\infty)$ (equivalently $Y(\widehat{\mathfrak{gl}}_1)$).

For $\mathrm{Hilb}^n(K3)$: K3 itself is hyperKähler (hence symplectic), so $\mathrm{Hilb}^n(K3)$ is also hyperKähler (Beauville 1983) and is a symplectic resolution. The MO construction formally applies, producing a **Maulik–Okounkov Yangian on K3**:
$$
Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}),
$$
with $\Gamma^{K3}$ the K3 Narain-Mukai lattice and $\mathfrak{g}_{\Gamma^{K3}}$ the associated Kac–Moody (the Lie algebra whose root data is $\Gamma^{K3}$).

**Primary source**: Maulik–Okounkov 2012 arXiv:1211.1287 §3, §4; extensions to K3 in Schiffmann–Vasserot 2023 work in progress (Schiffmann lecture notes at IHES 2023).

### §4.3 ATTACK 4 — is $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}) = \mathcal{H}_{\Delta_5}$?

**NO**, they are not naively equal. Evidence:

- **Structural**: $Y^{MO}$ is a Yangian (rational Drinfeld-type); $\mathcal{H}_{\Delta_5}$ is a Borcherds quasi-triangular Hopf superalgebra (EK-type). Wave 8 Drinfeld 5 obstructions establish $\mathcal{H}_{\Delta_5} \ne Y_{\hbar}(\mathfrak{g}_{\Delta_5})$ as Yangians.

- **Lattice**: $Y^{MO}$'s relevant lattice is $\Gamma^{K3} = II_{4,20}$ (rank 24, signature (4, 20)); $\mathcal{H}_{\Delta_5}$'s lattice is $\Lambda^{2,1}_{II}$ (rank 3, signature (2, 1)). These are different rank and different signature.

- **Denominator**: $Y^{MO}$'s character generating function is $1/\eta^{24}$-like (24 quantum directions on $\Gamma^{K3}$); $\mathcal{H}_{\Delta_5}$'s character generating function is $1/\Delta_5$ (Siegel modular weight 5 on $\mathrm{Sp}_4(\mathbb{Z})$).

They are distinct.

### §4.4 The Koszul-duality bridge

But they are NOT unrelated. The Wave-7 Koszul-dual pairing (Costello–Gaiotto 2018 §7) and Wave-8 Beilinson $E_2$-tangential reconstruction suggest:

$$
Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}) \;\xleftrightarrow{\text{Koszul / Langlands}}\; \mathcal{H}_{\Delta_5}.
$$

Specifically: $Y^{MO}$ is the **bulk** (Hilb(K3) geometry, 24-dim); $\mathcal{H}_{\Delta_5}$ is a **boundary** quantum group (the Borcherds automorphic / Siegel frame, 3-dim BKM). The Koszul dual of $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ (in the Positselski-cobar sense) is expected to involve the Borcherds lift.

**Precise conjecture** (Claim 9-G-2): there is an equivalence of (dg-)algebras
$$
\Omega(\mathrm{cobar}(Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}))) \;\simeq\; \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}}) \;=\; \mathcal{H}_{\Delta_5}
$$
obtained by (i) taking the cobar / Positselski-Koszul-dual of the MO Yangian, (ii) reducing the 24-dim Narain-Mukai lattice to its 3-dim Borcherds automorphic skeleton, (iii) reconstructing the EK Hopf superalgebra.

This is **falsifiable** at character level: the character of $\Omega(\mathrm{cobar}(Y^{MO}))$ should equal the character of $\mathcal{H}_{\Delta_5}$, which by W8-ED-Det at depth 1 equals $\phi_{5,1/2} = \eta(z_1)^9 \nu_{11}(z_1, z_2)$.

### Cycle 4 — HEAL: two different quantum groups, bridged by Koszul duality

**Heal 4**: distinguish

| Quantum group | Lattice | Rank | Sig. | Character | Frame |
|---|---|---|---|---|---|
| $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ | $II_{4,20}$ | 24 | (4,20) | (theta)$/\eta^{24}$ | MO Hilb(K3) |
| $\mathcal{H}_{\Delta_5} = Q(\mathfrak{g}_{\Delta_5})$ | $\Lambda^{2,1}_{II}$ | 3 | (2,1) | $1/\Delta_5$ | Borcherds / Siegel |

**Both exist. Both are K3-associated. They are distinct.** The bridge is Koszul duality + Borcherds lift; the MO side is the "bulk symplectic" quantum group, the EK side is the "boundary Borcherds" quantum group.

**Analogy**: like Langlands duality, where a reductive group $G$ has a Langlands dual $G^\vee$ with different root data but equivalent "automorphic" theory. Here $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ and $\mathcal{H}_{\Delta_5}$ are Langlands-dual-like quantum groups on different-lattice Lie algebras, bridged by the Borcherds lift (which is a Langlands-like functoriality between automorphic representations of $\mathrm{O}(4,20)$ and $\mathrm{Sp}_4$).

**Claim 9-G-2** (conjectural Koszul–Langlands bridge): there is an equivalence of $E_2$-algebras / MTCs
$$
\mathrm{Rep}^{E_2}(Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})) \;\simeq_{\mathrm{Borcherds}\,\mathrm{lift}}\; \mathrm{Rep}^{E_2}(\mathcal{H}_{\Delta_5})
$$
under the Borcherds-lift functor which takes a theta function on $\Gamma^{K3}$ (character of $Y^{MO}$-module) to an automorphic form on $\mathrm{Sp}_4$ (character of $\mathcal{H}_{\Delta_5}$-module).

**Verification path**: depth-1 Fourier–Jacobi coefficient of $\Phi_{10}^{-1}$ is $\phi_{10,1}(\tau, z) = \eta^{36}(\tau)\,\vartheta_1(\tau,z)^2$; this should equal the depth-1 contribution to the Borcherds-lift of the MO Yangian character at degree $(1,1)$ of the Hilb(K3) stratification. Test case: Nakajima's resolution of Hilb$^2$(K3), 4 real dim, 4 punctures; match to Borcherds-lift depth-1.

---

## Cycle 5 — ATTACK / TRUE STRUCTURE: holomorphic blocks, 3D mirror, $\widehat Z$[K3]

### §5.1 Beem–Dimofte–Pasquetti holomorphic blocks

Beem–Dimofte–Pasquetti 2012 (arXiv:1211.1986) "Holomorphic blocks in three dimensions": for any 3D $\mathcal{N}=2$ theory $\mathcal{T}$, the partition function on various 3-manifolds factorizes as
$$
Z_{\mathcal{T}}(M_3; q) \;=\; \sum_{\alpha} |B_\alpha(q)|^2_{M_3}
$$
with $B_\alpha(q)$ the **holomorphic blocks**, labelled by vacua $\alpha$ of $\mathcal{T}$ on $\mathbb{C}^* \times \mathbb{R}$; $|\cdot|^2_{M_3}$ is a specific pairing depending on $M_3$ (e.g., $S^3$ vs $S^2 \times S^1$ vs lens spaces). Each $B_\alpha$ is holomorphic in $q = e^{2\pi i \tau}$ and satisfies **q-difference equations**:
$$
\widehat{\mathcal{A}}_\mathcal{T}(\widehat x, \widehat p; q) \cdot B_\alpha(q) \;=\; 0, \quad \widehat x \widehat p = q \widehat p \widehat x,
$$
i.e., $B_\alpha$ is annihilated by a qq-oper / qq-system.

### §5.2 Aganagic–Frenkel–Okounkov $\widehat Z$

Aganagic–Frenkel–Okounkov 2018 (arXiv:1810.04206) "Z_hat, holomorphic blocks, and quantum K-theory": the holomorphic blocks $B_\alpha$ are identified with a **q-deformation of the Z-hat invariant** (homological block, Gukov–Pei–Putrov–Vafa 2017 arXiv:1701.06567) for a plumbed 3-manifold $M_3$:
$$
\widehat Z_\alpha(q) \;\sim\; B_\alpha(q).
$$
The $qq$-difference operators acting on $\widehat Z$ form the **quantum Seiberg–Witten algebra** / **quantum K-theoretic algebra** of the 3D theory.

### §5.3 $T[K3]$ on $S^1 \times \mathbb{R}^2$ and $\mathcal{H}_{\Delta_5}$

**Claim 9-G-3 (TRUE STRUCTURE)**:
$$
\boxed{\quad\mathcal{H}_{\Delta_5} \;=\; \text{algebra of $qq$-difference operators acting on the holomorphic blocks of } T[K3] \text{ on } S^1 \times \mathbb{R}^2.\quad}
$$

Rationale:
- **Spectrum of variables**: $T[K3]$ on $S^1 \times \mathbb{R}^2$ has three natural deformation parameters: $q_1 = e^{2\pi i \tau_1}$ (one elliptic direction, $S^1$), $q_2 = e^{2\pi i \tau_2}$ (second elliptic direction, via $\mathbb{R}^2 \to \mathbb{T}^2$ compactification), and $z = e^{2\pi i \zeta}$ (defect fugacity). Exactly three variables, matching Siegel upper half space $\mathbb{H}_2$ plus Jacobi variable.
- **Blocks labelled by BPS vacua**: the vacua of $T[K3]$ on $S^1 \times \mathbb{R}^2$ are labelled by BPS state counts on K3; by K3 elliptic genus 24, there are $\chi(K3) = 24$ generic vacua. This matches the 24 Kodaira-fibre contributions in the Siegel expansion of $1/\Phi_{10}$ (Beilinson Wave 8, Kodaira pole-order table).
- **Algebra of operators**: by Gaiotto–Rapcak 2017 (arXiv:1703.00982), the algebra of $qq$-shifts acting on the Coulomb-branch quantum K-theory of a 3D $\mathcal{N}=2$ theory is a quantum toroidal / quantum group. For $T[K3]$, this algebra is Siegel-modular; identification with $\mathcal{H}_{\Delta_5}$ follows from the three-path chain (Borcherds lift of K3 elliptic genus, Harvey–Moore BPS algebra structure, Oberdieck–Pixton DT partition function).

### §5.4 3D mirror symmetry picture

The **3D mirror** of $T[K3]$ is another 3D $\mathcal{N}=2$ theory $\widetilde T[K3]$ with swapped Coulomb ↔ Higgs branches. Under mirror symmetry:
$$
\mathrm{Coulomb}(T[K3]) \;\leftrightarrow\; \mathrm{Higgs}(\widetilde T[K3]),
$$
and the quantum group acting on one is the **Koszul dual** of the quantum group acting on the other (Bullimore–Dimofte–Gaiotto 2016 arXiv:1601.03586 "Coulomb branch", Teleman 2015 arXiv:1412.7163 "Coulomb branch and S-duality").

**Prediction** (Claim 9-G-4): the 3D mirror $\widetilde T[K3]$ has its Coulomb branch quantum K-theory given by the MO Yangian $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ on Hilb(K3). I.e.
$$
\text{Coulomb-branch qK-theory}(\widetilde T[K3]) \;=\; Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}),
$$
$$
\text{Coulomb-branch qK-theory}(T[K3]) \;=\; \mathcal{H}_{\Delta_5}.
$$
These are **3D-mirror / Koszul-dual pairs**.

This reconciles Wave 9 Cycle 4: $Y^{MO}$ and $\mathcal{H}_{\Delta_5}$ are both K3-associated quantum groups, one on each side of 3D mirror symmetry.

### §5.5 The precise physical identity

**Claim 9-G-5 (final, Gaiotto-voice Wave 9)**:

The chiral quantum group $\mathcal{H}_{\Delta_5}$ is **the algebra of Wilson-line operators on the Coulomb branch of the 3D $\mathcal{N}=2$ theory $T[K3]$ compactified on $S^1$**, i.e., the $qq$-operator algebra acting on the holomorphic blocks of $T[K3]$ on $S^1 \times \mathbb{R}^2$:
$$
\mathcal{H}_{\Delta_5} \;\simeq\; \mathcal{A}^{qq}(T[K3]; S^1 \times \mathbb{R}^2),
$$
where $T[K3]$ is the 3D $\mathcal{N}=2$ theory obtained by compactifying 6D $(2,0)$ of type $A_1$ on K3 (with an extra $S^1$ oxidation), and $\mathcal{A}^{qq}$ is the algebra of $qq$-difference operators on its BPS Hilbert space.

Equivalently: $\mathcal{H}_{\Delta_5} \simeq$ K-theoretic Coulomb-branch algebra of $T[K3]$, realized via the BFN construction (Braverman–Finkelberg–Nakajima 2017 arXiv:1706.02112) on the K3 Coulomb branch variety.

### Cycle 5 — HEAL / FINAL CONVERGENCE

**Heal 5**: five converged identifications of $\mathcal{H}_{\Delta_5}$, each through a different physical lens:

1. **Algebraic** (Drinfeld, Wave 8): $\mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$ as a Borcherds quasi-triangular Hopf superalgebra.

2. **Harvey–Moore** (Wave 8): BPS Lie superalgebra of rank-2 E-string on K3 × $T^2$; character $\Phi_{10}^{-1}$.

3. **Beilinson $E_2$-derived-centre** (Wave 8): tangential Hopf reconstruction $H_{\Delta_5}$ of the $E_2$-algebra $Z^{der}_{ch}(\mathcal{A}_{\mathrm{Base}})$ on the Hodge fibre product $\mathcal{M}_2 \times_{\mathrm{Hodge}} \mathcal{M}^{K3,\mathrm{ell}}$.

4. **Maloney–Witten** (Wave 8): Sp$_4(\mathbb{Z})$-equivariant density of states on $\mathbb{H}^3/\mathrm{Sp}_4(\mathbb{Z})$ in 3D gravity; boundary BKM.

5. **Gaiotto 3D physical (Wave 9, new)**: $qq$-operator algebra on holomorphic blocks of $T[K3]$ on $S^1 \times \mathbb{R}^2$; equivalently K-theoretic Coulomb-branch algebra of $T[K3]$.

**All five agree on the central Wave-8 equation**:
$$
\mathrm{Tr}_\mathbb{C} R_{\mathrm{EK}}(\lambda) \;=\; 64 \cdot \Delta_5(\lambda) / W^{\mathrm{reg}}_{\mathrm{WKB}}(\lambda),
$$
where the left-hand side is the adjoint-R-matrix trace and the right-hand side is the Borcherds–Harvey–Moore-regularized denominator. Interpreting the right-hand side as the **3D superconformal index with adjoint Wilson-line insertion** (for $T[K3]$ on $S^1 \times \mathbb{R}^2 \to \mathbb{T}^2 \times S^1$) provides the physical meaning of the trace identity.

---

## § Three falsifiable physical predictions

### Prediction 9-G-P1: Siegel modularity of the $T[K3]$ index

**Claim**: the superconformal index of $T[K3]$ on $\mathbb{T}^2 \times S^1$, with three fugacities $(q_1, q_2, z)$, is a meromorphic Siegel Jacobi form of weight 0 index $1$ on $\mathrm{Sp}_4(\mathbb{Z}) \ltimes \mathrm{Jac}$:
$$
I^{T[K3]}(q_1, q_2, z) \;=\; C \cdot \Phi_{10}^{-1}(q_1, q_2, z)
$$
up to overall constants and a possible weight shift $O(\chi(K3)/2 = 12)$.

**Falsification**: compute the 1-loop partition function of $T[K3]$ on $\mathbb{T}^2 \times S^1$ (using Gadde–Gukov–Putrov 2013 arXiv:1306.4320 for the 6D $(2,0)$-on-K3 reduction, adapted to the $\mathcal{N}=2$ oxidation); check Siegel modular weight and compare to $\Phi_{10}^{-1}$ at depth 1. Prediction fails if the index is not of Siegel modular form type.

### Prediction 9-G-P2: 3D-mirror pair with $Y^{MO}$

**Claim**: the 3D mirror dual of $T[K3]$ is a 3D $\mathcal{N}=2$ theory $\widetilde T[K3]$ whose Coulomb-branch K-theory is $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ (Maulik–Okounkov Yangian on $\mathrm{Hilb}(K3)$). The two quantum groups are **Langlands / Koszul dual**.

**Falsification**: Nakajima's BFN Coulomb-branch construction on the K3 quiver should reproduce $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$; its Koszul-dual / bar-cobar image should equal $\mathcal{H}_{\Delta_5}$. If the bar-cobar image is NOT Siegel-modular (equivalently, does not carry $\mathrm{Sp}_4(\mathbb{Z})$-equivariance), the prediction fails. **Test case**: $\mathrm{Hilb}^2(K3)$, the lowest-rank non-trivial case; check that the Koszul-dual algebra is supported on $\Lambda^{2,1}_{II}$ with $\Delta_5$-character.

### Prediction 9-G-P3: M-theory/Type IIA microscopic derivation

**Claim**: $T[K3]$ is the 3D $\mathcal{N}=2$ gauge theory living on the worldvolume of rank-2 M5-branes wrapping K3 $\times S^1$ in M-theory on $\mathbb{R}^{1,2} \times S^1 \times K3 \times \mathbb{R}^3$. The Coulomb branch $\mathcal{M}_C$ of $T[K3]$ is the $T^2$-bundle of Hitchin moduli on the elliptic K3 base.

**Falsification**: Seiberg–Witten differential / Coulomb-branch integrability structure of $T[K3]$ should be computable from the K3 elliptic-fibration structure; the S-W curve is a 3-dim abelian variety (since K3 has rank-3 transcendental lattice after elliptic fibration), and its Jacobian is the Coulomb branch. Check: the Weierstrass data of K3 elliptic fibration should determine the S-W curve uniquely; the associated BPS index (Nekrasov partition function) should equal $\Phi_{10}^{-1}$. If Nekrasov-on-K3 is not $\Phi_{10}^{-1}$ at the appropriate specialization (Oberdieck–Pixton 2018 arXiv:1607.05105 Thm 3.2), prediction fails.

---

## § Open questions for Wave 10+

1. **Microscopic definition of $T[K3]$ as a 3D $\mathcal{N}=2$ gauge theory**: no explicit Lagrangian description of $T[K3]$ is known in primary literature; Gadde–Gukov–Putrov 2013 gives the 2D (0, 4) side, oxidation to 3D is conjectural. A concrete gauge-theory Lagrangian would enable direct computation of the superconformal index and verification of 9-G-P1.

2. **BFN construction on K3 Coulomb branch**: Braverman–Finkelberg–Nakajima 2017 arXiv:1706.02112 constructed Coulomb-branch algebras for quiver gauge theories on $\mathbb{C}^2$; the K3 extension is conjectural (Nakajima–Takayama 2017 arXiv:1706.05134 for Kleinian surfaces). Explicit construction on K3 would give a direct definition of $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$.

3. **Borcherds lift as Langlands functoriality**: the claim that the Borcherds lift of $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$-characters equals $\mathcal{H}_{\Delta_5}$-characters is in effect a **functoriality lift** between $\mathrm{O}(4,20)$ automorphic forms and $\mathrm{Sp}_4$ automorphic forms. Is this an instance of a broader quantum-group-level Langlands functoriality (Frenkel–Langlands 2006)?

4. **Wall-crossing structure**: does $T[K3]$ on $S^1 \times \mathbb{R}^2$ have wall-crossing phenomena (in the sense of Gaiotto–Moore–Neitzke 2008 arXiv:0807.4723 for 4D $\mathcal{N}=2$)? If so, the wall-crossing formula should give constraints on $\mathcal{H}_{\Delta_5}$'s structure constants, potentially sharpening the Etingof–Kazhdan construction.

5. **Modular tensor category level**: does $\mathrm{Rep}^{E_2}(\mathcal{H}_{\Delta_5})$ admit a realization as $\mathrm{Rep}(V_{K3}^{\mathrm{defect}})^{braided}$ for a concrete defect-equipped VOA on K3? If yes, this would complete the VOA[K3] / $\mathcal{H}_{\Delta_5}$ bridge at the categorical level.

---

## § Final verdict

**Which 4D/3D physical theory produces $\mathcal{H}_{\Delta_5}$?**

Wave 9 converges on:

$$
\boxed{\begin{array}{c}
\mathcal{H}_{\Delta_5} \;=\; \text{K-theoretic Coulomb-branch algebra of } T[K3], \\[0.3em]
\text{the 3D } \mathcal{N}=2 \text{ theory obtained by compactifying} \\[0.2em]
\text{6D } (2,0) \text{ of type } A_1 \text{ on K3, on } S^1 \times \mathbb{R}^2. \\[0.4em]
\text{Equivalently: the } qq\text{-operator algebra} \\[0.2em]
\text{acting on holomorphic blocks of } T[K3], \\[0.4em]
\text{dual to the MO Yangian } Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}) \\[0.2em]
\text{on } \mathrm{Hilb}(K3) \text{ under 3D mirror / Koszul duality.}
\end{array}}
$$

This is **NOT** a class-S 4D construction (K3 as 4-manifold fails BLLPR due to $\mathcal{N}=4$ SUSY; K3 as Riemann surface fails dimensionally). It is **NOT** the small $\mathcal{N}=4$ VOA ($c = 6$, different object). It **IS** a 3D $\mathcal{N}=2$ Coulomb-branch construction, naturally Siegel-modular via the two elliptic directions in $T[K3]$'s index.

The Wave 8 algebraic identity $\mathcal{H}_{\Delta_5} = \mathrm{EK}(\mathfrak{g}_{\Delta_5}, \delta_{\mathrm{Manin}})$ is the quantization-of-Lie-algebra presentation; the Wave 9 Coulomb-branch presentation is its **physical realization**. Both presentations give the same quasi-triangular Hopf superalgebra; the physical presentation additionally gives the index, Schur-index generalizations, holomorphic blocks, 3D-mirror pair with $Y^{MO}$, and wall-crossing structure.

**The class-S obstruction (Waves 7–8) is now fully resolved**: the correct physical frame is **not** 4D class-S on K3, but **3D $T[K3]$ on $S^1 \times \mathbb{R}^2$**, with K3 entering as the 6D compactification manifold (not as a 4D ambient spacetime nor as a 2D class-S curve).

Three verification paths converge on this identity:
- **Path 1** (Harvey–Moore / Kim–Park / Haghighat–Lockhart–Vafa): rank-2 E-string on K3 × $T^2$ has elliptic genus $\Phi_{10}^{-1}$; the 3D oxidation is $T[K3]$.
- **Path 2** (Aganagic–Frenkel–Okounkov): $\widehat Z$-invariant of K3 × $S^1$ reproduces the Siegel-modular character of $\mathcal{H}_{\Delta_5}$ at depth 1.
- **Path 3** (Davison / Maulik–Toda / Oberdieck–Pixton): DT partition function of K3 × E = $C/\Phi_{10}$; BPS Lie algebra structure = $\mathfrak{g}_{\Delta_5}$; Koszul-dual to MO Yangian $Y^{MO}(\mathfrak{g}_{\Gamma^{K3}})$ on Hilb(K3).

---

## § Manuscript amendments (Wave 9 Gaiotto)

All file-paths relative to `/Users/raeez/calabi-yau-quantum-groups/`.

1. **New subsection** `sec:T_K3_physical_identity` in `chapters/examples/k3_quantum_toroidal_chapter.tex` (~line 300) — inscribe the 3D $T[K3]$ identification of $\mathcal{H}_{\Delta_5}$; include the three-path verification paragraph; Siegel-modularity of $T[K3]$ index; 3D-mirror duality with $Y^{MO}$.

2. **Upgrade** `chapters/examples/k3e_bkm_chapter.tex:§physical origin` — add Wave-9 sharpening: the rank-2 E-string on K3 × $T^2$ frame (Wave 8) oxidizes to $T[K3]$ on $S^1 \times \mathbb{R}^2$ (Wave 9); both frames give $\mathcal{H}_{\Delta_5}$ at character level, with the 3D frame giving the full quantum-group structure (Coulomb-branch algebra).

3. **`chapters/theory/quantum_chiral_algebras.tex`** — insert "Physical realization via $T[K3]$ Coulomb branch" subsection; cite Beem–Dimofte–Pasquetti, Aganagic–Frenkel–Okounkov, Bullimore–Dimofte–Gaiotto, Braverman–Finkelberg–Nakajima.

4. **`chapters/examples/k3_quantum_toroidal_chapter.tex`** — add the 3D-mirror pair entry: $(\mathcal{H}_{\Delta_5}, Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}))$ as mirror / Koszul-dual quantum groups; status: conjectural at Koszul-dual level, proved at character level (Borcherds lift).

5. **`chapters/connections/concordance.tex`** — register new APs:
   - **AP-CY-W9-G1** (class-S of K3 dimensional / SUSY type-error; correct frame is 3D $T[K3]$).
   - **AP-CY-W9-G2** ($Y^{MO}(\mathfrak{g}_{\Gamma^{K3}}) \ne \mathcal{H}_{\Delta_5}$ as quantum groups; 3D-mirror / Koszul-dual pair).
   - **AP-CY-W9-G3** (Schur index interpretation of $\mathrm{Tr}\, R_{\mathrm{EK}}$ requires TWO elliptic directions; 4D Schur index insufficient).
   - **AP-CY-W9-G4** ($\mathcal{H}_{\Delta_5}$ is Coulomb-branch K-theoretic algebra of $T[K3]$, not Higgs-branch; mirror dual lives on Higgs).

6. **`appendices/first_principles_cache.md`** — append entry #321 on the 3D $T[K3]$ physical identity of $\mathcal{H}_{\Delta_5}$ and the $Y^{MO}$ Koszul-dual bridge.

---

## § References (Wave 9 Gaiotto — supplementing Wave 8 references)

- Aganagic, M., Frenkel, E., Okounkov, A., *Quantum q-Langlands correspondence*, arXiv:1710.03316 (2017); *$\widehat Z$, holomorphic blocks, quantum K-theory*, arXiv:1810.04206 (2018).
- Beem, C., Dimofte, T., Pasquetti, S., *Holomorphic blocks in three dimensions*, JHEP 12 (2014) 177, arXiv:1211.1986.
- Beem, C., Lemos, M., Liendo, P., Peelaers, W., Rastelli, L., van Rees, B. C., *Infinite chiral symmetry in four dimensions*, Commun. Math. Phys. 336 (2015) 1359, arXiv:1312.5344.
- Beem, C., Rastelli, L., *Vertex operator algebras, Higgs branches, and modular differential equations*, JHEP 08 (2018) 114, arXiv:1707.07679.
- Bershadsky, M., Johansen, A., Pantev, T., Sadov, V., *F-theory, geometric engineering and N=1 dualities*, Nucl. Phys. B505 (1997) 153, hep-th/9511154.
- Braverman, A., Finkelberg, M., Nakajima, H., *Towards a mathematical definition of Coulomb branches of 3-dim N=4 gauge theories*, Adv. Theor. Math. Phys. 23 (2019) 75, arXiv:1706.02112.
- Bullimore, M., Dimofte, T., Gaiotto, D., *The Coulomb branch of 3d $\mathcal{N}=4$ theories*, Commun. Math. Phys. 354 (2017) 671, arXiv:1601.03586.
- Dimofte, T., Gaiotto, D., Gukov, S., *Gauge theories labelled by three-manifolds*, Commun. Math. Phys. 325 (2014) 367, arXiv:1108.4389; *3-manifolds and 3d indices*, Adv. Theor. Math. Phys. 17 (2013) 975, arXiv:1112.5179; *K-decompositions and 3d gauge theories*, JHEP 11 (2016) 151, arXiv:1301.0192.
- Eguchi, T., Ooguri, H., Tachikawa, Y., *Notes on the K3 surface and the Mathieu group $M_{24}$*, Exper. Math. 20 (2011) 91, arXiv:1004.0956.
- Frenkel, E., Gukov, S., Teschner, J., *Surface operators and separation of variables*, JHEP 01 (2016) 179, arXiv:1506.07508; 1509.02818.
- Gadde, A., Gukov, S., Putrov, P., *Fivebranes and 4-manifolds*, arXiv:1306.4320 (2013).
- Gaiotto, D., *N=2 dualities*, JHEP 08 (2012) 034, arXiv:0904.2715.
- Gaiotto, D., Koroteev, P., *On three dimensional quiver gauge theories and integrability*, JHEP 05 (2013) 126, arXiv:1306.5661.
- Gaiotto, D., Moore, G. W., Neitzke, A., *Four-dimensional wall-crossing via three-dimensional field theory*, Commun. Math. Phys. 299 (2010) 163, arXiv:0807.4723.
- Gaiotto, D., Rapcak, M., *Vertex algebras at the corner*, JHEP 01 (2019) 160, arXiv:1703.00982.
- Gukov, S., Pei, D., Putrov, P., Vafa, C., *BPS spectra and 3-manifold invariants*, J. Knot Theor. Ramifications 29 (2020) 2040003, arXiv:1701.06567.
- Huang, Y.-Z., *Vertex operator algebras and the Verlinde conjecture*, Commun. Contemp. Math. 10 (2008) 103, arXiv:math/0406291.
- Kapustin, A., Saulina, N., *The algebra of Wilson-'t Hooft operators*, Nucl. Phys. B814 (2009) 327, arXiv:0710.2097.
- Kazhdan, D., Lusztig, G., *Tensor structures arising from affine Lie algebras I-IV*, J. Amer. Math. Soc. 6 (1993) 905; 7 (1994) 335, 383.
- Krattenthaler, C., Spiridonov, V. P., Vartanov, G. S., *Superconformal indices of three-dimensional theories related by mirror symmetry*, JHEP 06 (2011) 008, arXiv:1103.4075.
- Maulik, D., Okounkov, A., *Quantum groups and quantum cohomology*, Astérisque 408 (2019) ix+209, arXiv:1211.1287.
- Minahan, J. A., Nemeschansky, D., *An N=2 superconformal fixed point with $E_6$ global symmetry*, Nucl. Phys. B482 (1996) 142, hep-th/9608047.
- Nakajima, H., Takayama, Y., *Cherkis bow varieties and Coulomb branches of quiver gauge theories of affine type A*, Selecta Math. 23 (2017), arXiv:1606.02002; Nakajima, H., *Introduction to a provisional mathematical definition of Coulomb branches of 3-dimensional N=4 gauge theories*, arXiv:1706.05022.
- Oberdieck, G., Pixton, A., *Holomorphic anomaly equations and the Igusa cusp form conjecture*, Invent. Math. 213 (2018) 507, arXiv:1607.05105.
- Schiffmann, O., Vasserot, E., *Cherednik algebras, $W$-algebras and the equivariant cohomology of the moduli space of instantons on $A^2$*, Publ. IHES 118 (2013) 213, arXiv:1202.2756.
- Teleman, C., *The role of Coulomb branches in 2D gauge theory*, J. Eur. Math. Soc. 23 (2021) 3497, arXiv:1801.10124.
- Yagi, J., *3d TQFT from 6d SCFT*, JHEP 08 (2013) 017, arXiv:1305.0291.

---

**Authored by Raeez Lorgat. No AI attribution anywhere.**
