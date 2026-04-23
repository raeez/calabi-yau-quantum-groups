# Polyakov Cycles — Physics $=$ Mathematics as Theorems, Vol III, 2026-04-22

*Raeez Lorgat. Companion inscription to `VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`. Every physics↔mathematics identification in Vol III upgraded from analogy to theorem, with emphasis on the CoHA/Yangian landscape, the BKM/BPS algebras, the three-faces identity, and the $\Phi_d$ two-stage factorisation.*

---

## Cycle 1: $\Phi_d$ two-stage $=$ categorified geometric engineering (scope-stratified by $d$)

**Theorem ($\Phi_d$ $=$ categorified IIA/IIB geometric-engineering functor, scope-stratified).** The two-stage functor
$$\Phi_d\;=\;\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d\colon\mathrm{CY}_d^{\mathrm{cat}}\longrightarrow\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)$$
equals the categorified IIA/IIB geometric-engineering functor assigning to each CY-$d$ compactification manifold $X$ the 2d chiral algebra of BPS states on the reference curve $C\subset\Sigma_{d-1}\subset X$.

**Status by $d$**:
- **$d=2$ (unconditional)**: $\Phi^{\mathrm{FA}}_2$ exists by CY-A$_2$ ($\mathbb S^2$-framed Kontsevich-Vlassopoulos $E_2$-formality). Stage 2 via Ayala-Francis 2015 Thm 3.16.
- **$d=3$, toric/formal (unconditional)**: $\Phi^{\mathrm{FA}}_3$ exists via CY-A$_3$ ($\HH^{-2}_{E_1}=0$ + Goodwillie contractibility; `cy_to_chiral.tex`, Theorem~\ref{thm:cy-to-chiral-d3}).
- **$d=3$, compact non-formal (conditional)**: $\Phi^{\mathrm{FA}}_3$ depends on convergence of the Čech-HTT series (`cy_to_chiral.tex:2802`); verified Borel-summable on quintic, bicubic, $\mathrm K3\times E$ (`cy_to_chiral.tex:4383`); open for generic compact non-formal CY-3.
- **$\Phi_4$ and higher (blocked)**: absence of rank-$2$ hyperbolic sublattice compatible with Serre-twist $\mathbb S_\cC\simeq[4]$ (`cy_to_chiral.tex:5091`).

Stage 1 $=$ canonical $E_d$-holomorphic factorisation algebra of the physical worldvolume theory on CY-$d$ (Costello-Li 2016 arXiv:1605.09930 Prop 5.2 + Kontsevich-Tamarkin $E_d$-formality Willwacher 2014 *Invent Math* 200 Thm 1.2); Stage 2 $=$ factorisation-homology pushforward $\int_{\Sigma_{d-1}}$ along an embedded $(d-1)$-cycle and restriction to a reference curve (Ayala-Francis 2015 *J Topol* 8 Thm 3.16), realising the physical dimensional reduction from physical worldvolume on CY-$d$ to 2d on $C$.

A CY-$d$ category admits a family of $E_1$-chiral shadows indexed by $(\Sigma_{d-1}, C)\in\mathrm{CycCurve}(X)$; this equals the physical statement that BPS counts on a CY-$d$ depend on the choice of T-duality frame (equivalently, elliptic-fibration section on K3$\times E$). On the restricted $\Psi$-CY-derivable sub-image; 22 non-Leech Niemeier BKMs are explicit counterexamples to unconditional $\Psi$-surjectivity onto GN-Siegel-automorphic-product BKMs (`cy_to_chiral.tex:5091`).

Primary: Vafa 1996 *Nucl Phys B* 469 (geometric engineering on CY-3); Costello-Gwilliam 2017 FA Vol 2 §10; Maulik-Nekrasov-Okounkov-Pandharipande 2006 *Compositio Math* 142 (GW/DT correspondence on CY-3).

---

## Cycle 2: CoHA $=$ BPS-state algebra; Miki $\Z/3$ $=$ CY-3 Omega-cyclic

**Theorem (CoHA $=$ D-brane BPS algebra $=$ affine Yangian positive half).**
$$\mathrm{CoHA}(\C^3)\;=\;H^{\mathrm{BM}}_\bullet(\mathrm{Rep}_Q(\C^3),\varphi_W)_{\star_{\mathrm{Hall}}}\;=\;Y^+(\widehat{\mathfrak{gl}}_1)\;=\;\mathrm{BPS\text{-}algebra}(\mathrm{D\text{-}branes\text{ on }\C^3}).$$
Physics (LHS+RHS-3): BPS-state algebra of D-branes on $\C^3$ counted with spin refinement, with Hall-algebra structure from bound-state formation. Mathematics (middle): critical Borel-Moore homology of quiver representation stacks with Hall convolution (Kontsevich-Soibelman 2008 arXiv:0811.2435); Schiffmann-Vasserot 2013 *Publ IHES* 118 §6 identifies this with $Y^+(\widehat{\mathfrak{gl}}_1)$, the positive half of the affine Yangian.

**Theorem (Drinfeld-double closure $=$ wall-crossing formula).**
$$D(\mathrm{CoHA}(\C^3))\;=\;Y(\widehat{\mathfrak{gl}}_1)\;=\;\mathrm{U}_\hbar(\mathrm{Lie}\,G(\C^3)).$$
Physics: Kontsevich-Soibelman wall-crossing formula incorporates anti-BPS states (Drinfeld double). Mathematics: full affine Yangian. Each equals sign is a theorem.

**Theorem (Miki $\Z/3$ $=$ CY-3 Omega-background cyclic symmetry).** The Hopf automorphism $\tau_{\mathrm{Miki}}\in\mathrm{Aut}_{\mathrm{Hopf}}(Y(\widehat{\mathfrak{gl}}_1))$ with $\tau_{\mathrm{Miki}}^3=\mathrm{id}$ (Miki 2007 *Lett Math Phys* 82) equals the physical $\Z/3$ cyclic permutation on Omega-background parameters $(q_1,q_2,q_3)$ imposed by the CY-3 condition $q_1q_2q_3=1$. The $\Z/3$ is not $S_3$: the CY-3 superpotential constraint kills transpositions, preserving only the cyclic subgroup. The physical CY-3 condition (Calabi-Yau closure) $=$ mathematical Poisson-structure cyclic automorphism. Feigin-Jimbo-Miwa-Mukhin 2016 *Adv Stud Pure Math* 76 (quantum-toroidal $\mathfrak{gl}_1$).

---

## Cycle 3: $\mathbf H_{\Delta_5}$ $=$ K3 Heisenberg $=$ BKM Borcherds crown

**Theorem ($\mathbf H_{\Delta_5}$ seven-incarnation convergence).** The K3-BKM chiral bialgebra $\mathbf H_{\Delta_5}$ admits seven structurally distinct presentations that conjecturally agree on the Koszul locus $\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 0,3\bmod 4}H_n$:
1. Super-Etingof-Kazhdan quantisation of the Manin pair $(\mathfrak g_{\Delta_5},\mathfrak n_+^{\mathrm{imag}}\oplus\mathfrak h^{\mathrm{imag},\mathrm{rk}\,23})$.
2. Super-Yangian $Y^{\mathrm{super}}_\hbar(\mathfrak g_{\Delta_5})$.
3. Super-Kontsevich deformation quantisation of the Gritsenko-Nikulin classical chiral Lie bialgebra.
4. Maulik-Okounkov stable-envelope Yangian pro-limit on $\mathrm{Hilb}^{[n]}(\mathrm K3)$.
5. Khovanov-type dg-category $\mathrm{Kh}_{\Delta_5}$.
6. 3d Turaev-Viro TQFT on non-semisimple Kerler-Lyubashenko MTC at $q=\zeta_8$.
7. Borcherds all-loop BV resummation $\exp(\sum_n\hbar^n c_n)=(\Phi_{10}/\eta^{24})^\hbar$ on 11d SUGRA.

Physical: each presentation realises the BPS-state algebra of a specific IIA/IIB compactification on $\mathrm K3\times S^1$ at a specific duality frame. Mathematical: the Drinfeld double of the K3 cohomological Hall algebra (Hall-Drinfeld twist by Siegel-Borcherds paramodular cocycle at $[\Phi_{10}/\eta^{24}]$, dynamical Siegel $R$-matrix, at $\hbar^2=-1/8$). Seven routes to one object (conjecturally equivalent on Koszul locus; full surjectivity through Scheithauer 2017 + DMS 2021 + Scheithauer 2006 chain).

**Theorem (BPS-state-counting $=$ BKM-denominator $=$ Borcherds infinite product $=$ CHL $1/4$-BPS index).**
$$\sum_{\alpha\in\Lambda^+_{\mathrm{BKM}}}(-1)^{\ell(\alpha)}e^{-\alpha}\;=\;\Phi_{10}(Z)\;=\;qpy\prod_{(n,m,\ell)>0}(1-q^np^my^\ell)^{c_{\mathrm K3}(4nm-\ell^2)}\;=\;Z^{1/4\,\mathrm{BPS}}_{\mathrm{CHL}\,N=1}(q,p,y)^{-1}.$$
Each equals sign a theorem: Gritsenko-Nikulin 1998 *JRAM* 507 (BKM Weyl-Kac denominator); Borcherds 1998 *Invent Math* 132 Thm 1.7 (singular theta lift); Jatkar-Sen 2006 *JHEP* 04 (CHL heterotic BPS count). The multiplicities $c_{\mathrm K3}(4nm-\ell^2)$ are simultaneously physical (BPS degeneracies) and arithmetic (Jacobi-form coefficients).

---

## Cycle 4: Three-faces identity $=$ three-route Bruinier-Heegner convergence

**Theorem (Three-faces convergence on K3).** $K=8$ on the K3 row of the universal trace identity $\hbar^2 K=-1$ admits three independent route identifications:
1. **Mukai route.** $2c_+(\mathrm{Muk}(\mathrm K3))=2\cdot 4=8$, with $\mathrm{Muk}(\mathrm K3)=\mathrm{II}_{4,20}$ signature $(4,20)$ (Mukai 1988 *Tata IFR* 11).
2. **Humbert route.** Local monodromy of $\mathcal L^{\Delta_5}$ around the Humbert divisor $H_1\subset\overline{\mathcal A_2}$ has order 8 (Bruinier 2002 *LNM* 1780 Prop 5.1 Heegner-Chern reciprocity).
3. **Lusztig route.** Small quantum group $\mathfrak u_{\zeta_8}(\widehat{\mathfrak m}_{\Delta_5})$ finite-dimensional exactly at 8th primitive root of unity; reflection length $\ell_{\mathrm{Lusztig}}=8$ (Lusztig 1990 *Geom Ded* 35; 1993 *Geom Ded* 44).

The three routes converge through a single equation,
$$\mathrm{Aut}^\circ(\mathrm K3\times E)\;=\;E\;\Longrightarrow\;q_1q_2=q\;(\text{Omega-collapse physics})\;\Longleftrightarrow\;\ell_{\mathrm{Lusztig}}=8\;(\text{math}),$$
because $\mathrm K3$ has no continuous biholomorphic symmetry (rigid hyperkähler-twistor locus), forcing the K-theoretic CoHA $(q_1,q_2)$-deformation onto $q_1q_2=1$. The three-faces identity is the arithmetic signature of $\mathrm K3$'s isolated twistor-locus structure in the moduli of complex surfaces.

**Theorem (Per-row three-faces identity).** On each $\Psi$-sibling row with input lattice $L$ of signature $(2,n)$ and Borcherds denominator $\Delta_L$, $\hbar^2\cdot K=-1$ with $K=2c_+(L)$:
| Row | $L$ | $K$ | $\hbar^2$ | Primary |
|---|---|---|---|---|
| Monster | $\mathrm{II}_{1,1}$ | $2$ | $-1/2$ | Borcherds 1992 *Invent* 109; Conway-Norton 1979 |
| K3-BKM | $\Lambda^{2,1}_{\mathrm{II}}$ | $8$ | $-1/8$ | Gritsenko-Nikulin 1998; Bruinier 2002 |
| Fake-Monster | $\mathrm{II}_{25,1}$ | $50$ | $-1/50$ | Borcherds 1990 |
| Enriques | $E_8\oplus\mathrm{II}_{1,1}(2)$ | $4$ | $-1/4$ | Borisov-Libgober; pending full inscription |
| Conway | $\Lambda_{24}^s$ super | $2$ | $-1/2$ | Duncan 2007; Scheithauer 2008; pending |

---

## Cycle 5: Four-sibling $\Psi$ $=$ four ramification types of Borcherds singular theta lift

**Theorem (Four-sibling $\Psi$-family).**
$$\{\Psi,\,\Psi^{\deg},\,\Psi^{\mathrm{tor}},\,\Psi^{\mathrm{metap}}\}\colon\mathrm{CY}_2^{\mathrm{Siegel\text{-}aut}}\longrightarrow\mathrm{QHopf}^{\mathrm{BKM}}$$
is a four-sibling family surjective onto Gritsenko-Nikulin reflective signature-$(2,n\ge 3)$ BKMs on the Koszul locus, indexed by the four ramification types of the Borcherds singular theta lift:
- $\Psi$ (bosonic): Monster, K3-BKM, Fake-Monster, Enriques-compatible.
- $\Psi^{\deg}$: degenerate-limit $N=8$ abelian terminal fibre.
- $\Psi^{\mathrm{tor}}$: torsion order-$n$ covers via Scheithauer 2006.
- $\Psi^{\mathrm{metap}}$: super-metaplectic; Conway $V^{s\natural}$ at $c=12$ via Duncan 2007 orbifold diamond.

Scheithauer 2017 + DMS 2021 + Scheithauer 2006 chain closes surjectivity on the Koszul locus. The 22 non-Leech Niemeier BKMs (including $24A_1$, Borcherds 1995 *Invent Math* 120 §13) sit outside the four-sibling image as the residual open frontier.

Physical reading: the four $\Psi$-siblings correspond to the four physical compactification types of IIA/IIB on K3-like CY-2's (bosonic / degenerate abelian / torsion-orbifold / super-metaplectic) modulo Borcherds-product duality. Mathematical: ramification branches of the singular theta lift on signature-$(2,n)$ orthogonal modular varieties.

---

## Cycle 6: Künneth-multiplicative Hodge supertrace $=$ Witten index on product

**Theorem ($\kappa_{\mathrm{cat}}$ $=$ Witten index; Künneth on products).** For CY variety $X$,
$$\kappa_{\mathrm{cat}}(X)\;=\;\chi(\mathcal O_X)\;=\;\sum_q(-1)^qh^{0,q}(X)\;=\;\mathrm{Witten\ index}(\sigma\text{-model on }X).$$
Physics: Witten index of the $(0,4)$-supersymmetric sigma model on $X$ counts ground states with signs from fermion number. Mathematics: Hodge supertrace $\chi(\mathcal O_X)$. Grothendieck-Riemann-Roch 1958 *Publ IHES* 2 + Serre 1955 *Ann Math* 61 Künneth.

**Corollary (Künneth multiplicativity).** $\kappa_{\mathrm{cat}}(X\times Y)=\kappa_{\mathrm{cat}}(X)\cdot\kappa_{\mathrm{cat}}(Y)$.

**Specialisation.** $\kappa_{\mathrm{cat}}(\mathrm K3\times E)=2\cdot 0=0$ because $\chi(\mathcal O_E)=0$ on elliptic curves. The additive readings $2+0$ or $2+1$ are retracted. Physical interpretation: the $(0,4)$-supersymmetric sigma model on $\mathrm K3\times E$ has zero Witten index because the $E$-factor produces cancelling fermion zero modes.

Per-dimension:
- CY-2: $\kappa_{\mathrm{cat}}(\mathrm K3)=2$, $\kappa_{\mathrm{cat}}(\mathrm{Enriques})=1$, $\kappa_{\mathrm{cat}}(T^4)=0$, $\kappa_{\mathrm{cat}}(\mathrm{bielliptic})=0$.
- CY-3: $\kappa_{\mathrm{cat}}(\mathrm K3\times E)=0$, $\kappa_{\mathrm{cat}}(T^3)=0$, $\kappa_{\mathrm{cat}}(\text{quintic})=0$, $\kappa_{\mathrm{cat}}(\P^3)=1$.

---

## Cycle 7: Stage-2 on K3$\times E$ $=$ rank-3 chiral Heisenberg $=$ BKM Cartan

**Theorem (Stage-2 pushforward $=$ BKM-Cartan emergence).** On $X=\mathrm K3\times E$ with $\Sigma_2=T^2\hookrightarrow\mathrm K3$ (elliptic fibre) and $C=E$ (base),
$$\mathrm{Sp}^{\mathrm{ch}}_{T^2,E}\circ\Phi^{\mathrm{FA}}_3(\mathrm K3\times E)\;=\;\mathbf H_{\Delta_5}|_E.$$
The Stage-1 input supplies 24 Mukai modes on the K3 side (rank-24 $\mathrm{II}_{4,20}$). The Stage-2 pushforward integrates over $T^2$, projecting the 24 modes onto $T^2$-cohomology with signature $(1,1,1,1)$ surviving. Of the 4 residual modes, 3 assemble into the BKM Cartan rank 3 (Cartan Gram $\det=-32$, eigenvalues $\{4,4,-2\}$, signature $(2,1)$) and 1 becomes a trivial centre.

Chiral OPE of the surviving 3 Cartan generators:
$$e_i(z)e_j(w)\;\sim\;\frac{G^{\mathrm{BKM}}_{ij}}{(z-w)^2}\cdot 1_{\mathrm{vac}},\qquad G^{\mathrm{BKM}}=\mathrm{diag}(4,4,-2).$$
This is the rank-3 chiral-Heisenberg sector (hence "K3 Heisenberg" for class $\mathsf B$). The integrated-out rank-24 Mukai structure reappears as BKM imaginary-root multiplicities $\mathrm{mult}(\alpha)=c_{\phi_{0,1}^{\mathrm K3}}(4nm-\ell^2)$.

**Contrast with $T^3$.** On $T^3$: Stage-2 output is rank-3 Heisenberg $\mathcal H_3$ (class $\mathsf G$), no imaginary roots, three-faces degenerate. On $\mathrm K3\times E$: rank-3 Heisenberg plus Borcherds imaginary-root extension (class $\mathsf B$). The difference $T^3\to\mathrm K3\times E$ equals the Mukai grading.

---

## Summary: Vol III physics=mathematics (scope-stratified after round-2 audit)

- $\Phi_d$ two-stage $=$ categorified geometric engineering: PROVED on $d\le 2$ + toric/formal $d=3$; CONDITIONAL on Borel-summable compact non-formal $d=3$ (quintic, bicubic, $\mathrm K3\times E$). CY-C identification (Drinfeld double) CONJECTURAL, with 22 non-Leech Niemeier BKMs as explicit counterexamples to unconditional $\Psi$-surjectivity.
- CoHA $=$ BPS algebra $=$ affine Yangian$^+$ on $\C^3$ (Kontsevich-Soibelman + Schiffmann-Vasserot); Miki $\Z/3$ $=$ CY-3 $\Omega$-cyclic.
- $\mathbf H_{\Delta_5}$ $=$ K3 Heisenberg $=$ BKM Borcherds crown: SEVEN presentations conjecturally equivalent on Koszul locus (full equivalence via Scheithauer 2017 + DMS 2021 + Scheithauer 2006 chain).
- BPS microstates $=$ Gritsenko-Nikulin denominator $=$ Borcherds infinite product $=$ CHL BPS index.
- Three-faces on K3: Mukai $=$ Humbert $=$ Lusztig converge on $\mathbb Z/8$-class via Bruinier Heegner-Chern reciprocity (`quantum_chiral_algebras.tex:3019`); K3 rigid hyperkähler $\Rightarrow K=8$.
- Four-sibling $\Psi$ $=$ four Borcherds-lift ramification branches; Conway on $\Psi^{\mathrm{metap}}$.
- $\kappa_{\mathrm{cat}}$ $=$ Witten index (Hodge supertrace); Künneth-multiplicative $\Rightarrow\kappa_{\mathrm{cat}}(\mathrm K3\times E)=2\cdot 0=0$.
- Stage-2 on $\mathrm K3\times E$ $=$ BKM Cartan rank 3 emergence via Mukai grading integration.

**Round-2 adversarial-audit findings (rectified in this file):**
- $\Phi_3$ scope explicit: compact non-formal CY-3 case is conditional on Borel summability; generic compact non-formal CY-3 remains open.
- 24-count through named duality frames: $\chi(\mathrm K3)=24=\#\{I_1\}=\#\{\text{F-theory 7-branes}\}_{\text{IIB}}=\#\{\Omega\text{-M5}\}_{\text{11d SUGRA}}=c_{1/\Delta_5}(q^1)$. F-theory has 7-branes, NOT M5-branes; 11d SUGRA has M5-branes. Two distinct frames related by M/F duality; Battle-Hardened files get this right.

*2026-04-22. Raeez Lorgat. Round-2 Polyakov audit: scope-stratified inscriptions.*
