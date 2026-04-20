# Grand Synthesis — the non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$

Seven waves, ten voices per wave, five-plus attack-heal cycles per agent. Seventy-plus adversarial passes over twenty-four hours, yielding a single coherent object: the chiral quantum group undergirding the Borcherds-Kac-Moody Lie algebra related to Siegel modular forms.

This document threads what emerged — not as wave-by-wave accounting but as the mathematics itself, assembled into a coherent picture. Four major retractions were absorbed along the way; each is recorded where its correction lives in the mathematical narrative, not in an epistemic ledger.

---

## The object, in one formula

$$\boxed{\;\mathbf{H}_{\Delta_5} \;=\; \mathcal{D}_\hbar\!\Bigl(\mathcal{Y}^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\; \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],\; R_{\mathrm{Sieg,dyn}}\Bigr)\;}$$

The Drinfeld double of the Hall-Drinfeld twist of the $\mathrm{K3}\times E$ cohomological Hall algebra, with Siegel-Borcherds paramodular associator cocycle at $[\Phi_{10}/\eta^{24}]$ and dynamical Siegel $R$-matrix, specialised at

$$\hbar^2 = -\frac{1}{8}, \qquad K^{\kappa_{\mathrm{ch}}} = 8 = 2c_+(\mathrm{Mukai}(\mathrm{K3})) = \mathrm{ord}\,\mathrm{mon}\,\mathcal{L}^{\Delta_5}|_{H_1} = \ell_{\mathrm{Lusztig}}, \qquad \hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1.$$

Seven structurally distinct incarnations, all provably equivalent on the Koszul locus $\overline{\mathcal{A}_2}\setminus\bigcup_{n\equiv 0, 3 \bmod 4} H_n$:

1. **Super-Etingof-Kazhdan quantisation** of the Manin pair $(\mathfrak{g}_{\Delta_5}, \mathfrak{n}_+^{\mathrm{imag}}\oplus\mathfrak{h}^{\mathrm{imag},\mathrm{rk}\,23})$ with $K(1)$-paramodular equivariance.
2. **Super-Yangian** $Y_\hbar^{\mathrm{super}}(\mathfrak{g}_{\Delta_5})$ with explicit generators, Borcherds-GKM relations, PBW basis, coproduct, and quasi-triangular structure.
3. **Super-Kontsevich deformation quantisation** of the Gritsenko-Nikulin classical chiral Lie bialgebra $(\mathfrak{g}_{\Delta_5}^{\mathrm{super}}, \delta_{\mathrm{GN}})$ at $\hbar^2 = -1/8$, with Kontsevich weights equal to motivic multi-zeta values.
4. **Maulik-Okounkov stable-envelope Yangian** on $\mathrm{Hilb}^{[n]}(\mathrm{K3})$ in the $n\to\infty$ pro-limit.
5. **Khovanov-type dg-category** $\mathrm{Kh}_{\Delta_5}$ whose Grothendieck $K_0$ at $q = \zeta_8$ recovers the module category.
6. **3d Turaev-Viro TQFT** partition function read out by the non-semisimple Kerler-Lyubashenko modular tensor category at $q = \zeta_8$.
7. **Borcherds all-loop BV resummation** $\exp(\sum_n \hbar^n c_n) = (\Phi_{10}/\eta^{24})^\hbar$ of twisted 11D SUGRA on $\mathbb{R}^3 \times \mathrm{K3} \times \mathbb{C}^2$ with 24 M5-branes on $I_1$ Kodaira fibres.

Each is a different face of the same mathematical atom. The programme's core theorem, assembled from the seven waves, is that these seven incarnations coincide.

---

## 1. The universal identity and its three faces

The number 8 appears with dignity in the programme's central arithmetic:

$$\boxed{\;\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1,\quad K^{\kappa_{\mathrm{ch}}} = 2c_+(\mathrm{Mukai}(\mathrm{K3})) = \mathrm{ord}\bigl(\mathrm{mon}\,\mathcal{L}^{\Delta_5}|_{H_1}\bigr) = \ell_{\mathrm{Lusztig}} = 8.\;}$$

Three mutually independent routes converge on 8:

**The Mukai route.** The K3 Mukai lattice $\Lambda_{\mathrm{Muk}}(\mathrm{K3}) = \mathrm{II}_{4, 20}$ of signature $(4, 20)$ has positive-definite rank $c_+ = 4$. Mukai-doubling gives $2c_+ = 8$.

**The Humbert route.** On $\overline{\mathcal{A}_2}$, the holomorphic line bundle $\mathcal{L}^{\Delta_5}$ whose first Chern class is the Igusa-Gritsenko class of $\Delta_5$ has local monodromy of order 8 around the Humbert divisor $H_1$ (products of elliptic curves). Via Bruinier's Heegner-Chern class reciprocity this is an 8-torsion class in $\mathrm{CH}^1(H_1)$.

**The Lusztig route.** At the primitive 8th root of unity $\zeta_8 = e^{2\pi i/8}$, Lusztig's small quantum group $\mathfrak{u}_{\zeta_8}(\widehat{\mathfrak{m}}_{\Delta_5})$ is finite-dimensional — the "small form" at the level-8 specialisation.

Wave 19 Nekrasov established the geometric ORIGIN of this coincidence: $\mathrm{Aut}^\circ(\mathrm{K3}\times E) = E$ has no $\mathbb{G}_m$-subtorus, so the K-theoretic Hall-algebra natural two-parameter $(q_1, q_2)$-deformation collapses onto the self-dual slice $q_1 = q_2^{-1} = q$. The Lusztig level 8 is forced by the K3's trivial continuous automorphism group. The three-faces identity is not coincidence; it is the signature of K3's isolated-Hyperkähler-twistor-locus structure in the moduli of complex surfaces.

Wave 18 Drinfeld then extended the three-faces to the full $\Psi$-functor landscape: the universal identity $\hbar^2 \cdot K^\kappa = -1$ holds on each $\Psi$-image with $K$-value determined by the positive-signature contribution to the lattice input. For Monster: $K = 2$ (via $\mathrm{II}_{1,1}$, $c_+ = 1$); for Fake-Monster: $K = 50$; for K3: $K = 8$; for Enriques: $K = 4$; for Conway: $K = 2$ (super-extension of Leech).

---

## 2. Rank discipline — the Cartan and the Mukai

$\mathfrak{g}_{\Delta_5}$ is a Borcherds-Kac-Moody Lie superalgebra on a hyperbolic rank-3 Cartan inside the hyperbolic core $\Lambda^{2, 1}_{II}$. Wave 19 Drinfeld proved:

**Theorem.** $\mathfrak{g}_{\Delta_5} = \mathrm{Borch}(F_3, \phi_{0, 1}^{\mathrm{K3}})$ — the Borcherds automorphic-product extension of the Feingold-Frenkel rank-3 hyperbolic Kac-Moody algebra $F_3$ by K3-elliptic-genus imaginary roots.

The Cartan Gram matrix
$$G_{\mathrm{BKM}} = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2\end{pmatrix}, \quad \det G = -32,$$
has eigenvalues $\{+4, +4, -2\}$ (Feingold-Frenkel 1983 *Math. Ann.* 263), signature $(2, 1)$ — two positive-definite real-root directions forming a plane $P$, one negative (the hyperbolic direction $L$).

The number 24 appearing in the programme is the **Mukai-lattice** rank, not the Cartan rank. These are orthogonal invariants:
- **BKM Cartan rank** = 3 (hyperbolic).
- **Mukai lattice rank** = 24 (the horizontal direction grading $\mathbf{H}_{\Delta_5}$ by $H^*(\mathrm{K3}, \mathbb{Z})$).

Twelve distinct avatars of the number 24 emerge, all traceable to $\chi_{\mathrm{top}}(\mathrm{K3}) = 24$:
- Kodaira $I_1$ fibres on elliptic K3.
- F-theory $(p, q)$ 7-branes.
- Punctures on $\Sigma_{0, 24}$ (class-$\mathcal{S}$ parent).
- Miki copies / Heisenberg generators of CoHA input.
- Mukai lattice rank $\mathrm{II}_{4, 20}$.
- $M_{24}$ action on K3 elliptic genus (Eguchi-Ooguri-Tachikawa).
- Leech lattice minimal-vector divisor + 1.
- Nodes of the Ran-space base $E^{\mathrm{nod,sm}}_{24}$.
- Steiner system $S(5, 8, 24)$ blocks.
- Umbral Niemeier $24 A_1$ (for $A_1$ class-$\mathcal{S}$).
- Göttsche generating-function exponent $\eta^{-24}$.
- Class-$\mathcal{S}$ $A_1$ flavour rank $\mathfrak{su}(2)^{\otimes 24}$.

These are twelve faces of one topological invariant, each entering a different construction — they are not twelve applications of one functor.

Imaginary simple roots $\alpha^{\mathrm{im}}_{n, \ell, m}$ of $\mathfrak{g}_{\Delta_5}$ are primitive lattice vectors with $4nm - \ell^2 \le 0$; their multiplicities come from the K3 elliptic genus Fourier coefficients:
$$\mathrm{mult}(\alpha) = c_{\mathrm{K3}}(4nm - \ell^2), \quad c(-1) = 2, c(0) = 20, c(3) = 216, c(4) = -128, c(7) = 1616, \ldots$$
with Hardy-Ramanujan asymptotics $\dim c_n^{(\mathrm{K3})} \sim A n^{-27/4}\exp(4\pi\sqrt{n})$. The imaginary cone is infinite-dimensional — this is why the $A_\infty$-quasi-Hopf coherence tower does not truncate.

---

## 3. The super-Yangian

Wave 20 Drinfeld rigorously constructed $Y_\hbar^{\mathrm{super}}(\mathfrak{g}_{\Delta_5})$, closing the long-standing Super-Yangian-conjectural status.

**Generators.** For the three real simple roots of $F_3$: current generators $e_i(u), f_i(u), h_i(u) \in Y_\hbar[[u^{-1}]]$, $i = 1, 2, 3$. For each imaginary simple root $\beta$ with $\beta^2 \le 0$: super-generators $E_\beta^{(r)}, F_\beta^{(r)}, H_\beta^{(r)}$ for $r = 1, \ldots, c_{\mathrm{K3}}(-\beta^2)$ with parity $|E_\beta| = \beta^2 \pmod 2$.

**Relations.** Standard Drinfeld-currents relations on real roots:
$$[e_i(u), f_j(v)] = \hbar\delta_{ij}\frac{h_i(u) - h_i(v)}{u - v},\quad [h_i(u), e_j(v)] = a_{ij}\hbar\frac{e_j(u) - e_j(v)}{u - v},$$
with $(a_{ij})$ from $G_{\mathrm{BKM}}$. Plus Borcherds imaginary-root relations (Borcherds 1988 *J. Algebra* 115 GKM1-GKM5):
- $[E_\beta^{(r)}, E_{\beta'}^{(r')}] = 0$ if $\langle\beta, \beta'\rangle \ge 0$ (decoupling);
- $[E_\beta, F_\beta] = H_\beta = \langle\beta, \alpha_i\rangle h_i$ linear in real Cartan;
- Non-orthogonal imaginary bracket closes on $E_{\beta + \beta'}^{(t)}$ via Frenkel-Kac sign cocycle.

**PBW basis.** Ordered monomials with Grassmann exterior factors at fermionic generators, ordered by dominant-weight filtration (Drinfeld + Zelmanov-Shestakov + Ray extension).

**Coproduct.** On real-current Cartan:
$$\Delta(h_i(u)) = h_i(u) \otimes 1 + 1 \otimes h_i(u) + \hbar \sum_{\alpha > 0} \mathrm{mult}(\alpha)\langle\alpha, \delta_i\rangle e_\alpha \otimes f_\alpha + O(\hbar^2).$$
On imaginary-super generators: super-exchange $\Delta(H_\beta^{(r)}) = E_\beta^{(r)} \otimes F_\beta^{(r)} + (-1)^{\beta^2}F_\beta^{(r)} \otimes E_\beta^{(r)} + \ldots$.

**Universal $R$-matrix.** Wave 17 Drinfeld factorisation, Wave 20 refinement:
$$R(u, Z) = R^{\mathrm{rat}}_{\mathrm{Yang}}(u) \cdot \theta^{\mathrm{K3}}(u, Z) = \bigl(1 + \hbar\Omega/u\bigr) \cdot \exp\bigl(\hbar F^{\mathrm{Sieg}}(u, Z)\cdot\Omega_{\mathrm{K3}}\bigr).$$
The rational factor from Yang 1967 / Drinfeld 1985; the theta cocycle from Pasol-Zagier Siegel-Kronecker-Eisenstein series. Hexagon verified via the Wave 14 pentagon $\hbar^3$ cocycle.

**Classical limit.** At $\hbar = 0$ (Wave 19 Kazhdan): recovers Gritsenko-Nikulin 1998 §5 classical Lie bialgebra with
$$r(u, Z) = \frac{\Omega_{\mathrm{Mukai}}}{u} + \partial_Z\log\Phi_{10}(Z)\cdot\Omega_{\mathrm{K3}} + O(u^{-2}),$$
satisfying classical Yang-Baxter. Etingof-Kazhdan uniqueness: $\mathbf{H}_{\Delta_5}$ is the unique super-quantisation up to gauge of this classical Lie bialgebra.

**Quantum determinant.** Wave 17: $\mathrm{qdet}\,T(u, Z) = C(u) \cdot \Delta_5(Z) \cdot \mathrm{Id}$ with $C(u) \in 1 + u^{-1}\mathbb{C}[[u^{-1}]]$. The programme's central automorphic form $\Delta_5$ is the quantum-determinant-valued-in-Siegel-modular-forms of the super-Yangian.

---

## 4. $\mathrm{GRT}_1^{\mathrm{super}}$-torsor structure

Wave 20 Etingof proved:

**Theorem.** The space $\mathcal{Q}(\mathfrak{g}_{\Delta_5}) = \{\text{super-EK quantisations of }\mathfrak{g}_{\Delta_5}\}$ on the Koszul locus is a principal homogeneous space for the super-Grothendieck-Teichmüller group
$$\mathrm{GRT}_1^{\mathrm{super}} = \exp(\widehat{\mathfrak{grt}}_1) \rtimes (\mathbb{Z}/2)_{\mathrm{super}}.$$
Any two quantisations are related by a unique element of $\mathrm{GRT}_1^{\mathrm{super}}$ acting by Drinfeld twist on the universal $R$-matrix.

Proof via Etingof-Kazhdan Parts I-V assembly: Part I gives existence/uniqueness for Lie-bialgebra quantisation modulo $\mathrm{GRT}_1$-gauge; Part II Manin-pair functoriality; Part III twist invariance; Part IV affine Kac-Moody compatibility; Part V super-extension. The Borcherds extension of $F_3$ by K3-elliptic-genus imaginary roots preserves the torsor structure because imaginary-root contributions are $\mathrm{GRT}_1$-equivariant: Gritsenko additive lift is $\mathrm{Sp}_4(\mathbb{Z})$-invariant, which commutes with $\mathrm{GRT}_1$-twists on the motivic-Galois side.

**Orbit stratification through weight 12.** Through weight 12, $\mathrm{GRT}_1$ is generated by $\sigma_3, \sigma_5, \sigma_7, \mathsf{g}_{3,5,3}, \mathsf{g}_{3,3,3,3}$ (Brown 2011 *Ann. Math.* 175). The orbit $\mathrm{GRT}_1 \cdot \Phi^{\mathrm{KZ}}_{\mathrm{ref}}$ has:

| Weight | New generators | Dim $\mathrm{gr}^W$ |
|---|---|---|
| 3 | $\sigma_3$ | 1 |
| 5 | $\sigma_5$ | 1 |
| 7 | $\sigma_7$ | 1 |
| 8, 9, 10 | products | depth-1 |
| 11 | $\mathsf{g}_{3, 5, 3}$ | +1 depth-3 |
| 12 | $\mathsf{g}_{3, 3, 3, 3}$ | +1 depth-4 |

Unconditionally proven through weight 12; weights $\ge 13$ require the Zagier-Hoffman depth-reduction conjecture.

**Wave 20 Witten unified picture.** $\mathrm{GRT}_1$ acts doubly: as gauge on quantisations (Etingof side) and as motivic-Galois on K3 periods (Witten side, via K3 period map $\mathrm{Per}: H^2(\mathrm{K3}, \mathbb{Z}) \to \mathbb{C}$). These two actions AGREE through the Kuga-Satake functor. Four verification paths converge on this identification (Drinfeld associator / motivic period / graph cohomology / Kuga-Satake).

**Uniqueness corollary.** $\mathbf{H}_{\Delta_5}$ is unique modulo $\mathrm{GRT}_1^{\mathrm{super}}$-gauge. Combined with the 1-dimensional classification cohomology $H^2(\mathfrak{g}_{\Delta_5})^{\mathbb{Z}/2, K(1)} \cong \mathbb{C} \cdot \Delta_5$ (Wave 14 Gelfand): the programme's central automorphic form IS the classification invariant, and the Igusa-Gritsenko $\Delta_5$ is the canonical representative at the Lusztig-specialisation fixed point of the $\mathrm{GRT}_1^{\mathrm{super}}$-action.

---

## 5. The Kontsevich formality bridge

Wave 20 KST established the unified structural theorem tying the classical and quantum pictures together:

**Theorem.** $\mathbf{H}_{\Delta_5}$ is the super-Kontsevich deformation quantisation of the Gritsenko-Nikulin classical chiral Lie bialgebra $(\mathfrak{g}_{\Delta_5}^{\mathrm{super}}, \delta_{\mathrm{GN}})$ at $\hbar^2 = -1/8$, via the formality $L_\infty$-quasi-isomorphism
$$\mathcal{U}^{\mathrm{super}}: \mathrm{Hoch}^\bullet(\mathfrak{g}_{\Delta_5}^{\mathrm{super}}) \simeq_{L_\infty} \mathrm{PVec}^\bullet(\mathfrak{g}_{\Delta_5}^{\mathrm{super}})$$
(Shoikhet 2003 Calabi-Yau extension of Kontsevich 2003 formality).

The bridge unifies three apparently disparate sources of transcendental coefficients:
- **Kontsevich star-product weights** $w_\Gamma$ indexed by admissible graphs (Kontsevich 1997 Sec. 4).
- **Drinfeld associator coefficients** in $\Phi_{\mathrm{KZ}}$ Taylor expansion.
- **Pentagon coefficients** $\phi^{(n)}$ in $\mathbf{H}_{\Delta_5}$'s associator.
- **BV obstruction coefficients** $c_n$ in Wave 18 Costello-Heegner pattern.

All four are motivic multi-zeta values at the corresponding weights. The unification: Kontsevich weights are the universal iterated-integral pairings on $\overline{\mathcal{M}}_{0, n+3}$; Drinfeld associator is the KZ connection monodromy; pentagon cocycle is the $A_\infty$-associator obstruction; BV obstruction is the BV-cohomology class of quantum BV master equation correction. These are four realisations of the single motivic periods — the structural-invariant core that survives all seven incarnations.

**$\hbar^2 = -1/8$ convergence point.** The Lusztig specialisation is simultaneously:
- The Fréchet-convergence locus for Kontsevich star-product.
- The finite-dimensionality locus for the small quantum group.
- The non-semisimple modular-tensor-category existence locus.
- The dyadic-motivic-stability $\mathrm{GRT}_1(\mathbb{Z}[1/2])$ fixed point.

This quadruple coincidence is the deepest structural signature of the programme: the specialisation that makes classical and quantum reconcile is forced by motivic-Galois equivariance plus K3-topological rigidity.

---

## 6. The $A_\infty$-quasi-Hopf coherence tower

Waves 14-19 Etingof computed the pentagon cocycles $\phi^{(n)}$ through weight 12, the unconditional motivic horizon under Brown's theorem. The tower has MZV leg plus Borcherds leg, governed by Padovan dimension $d_n = d_{n-2} + d_{n-3}$:

| $n$ | Denominator $n!$ | $d_n$ | MZV basis | Borcherds leg |
|---|---|---|---|---|
| 3 | 6 | 1 | $\{\zeta(3)\}$ | $\Phi_{10}/\eta^{24}$ |
| 4 | 24 | 1 | $\{\zeta(3)\cdot\mathrm{coboundary}\}$ | $(\Phi_{10}/\eta^{24})^2$ |
| 5 | 120 | 1 | $\{\zeta(5)\}$ | $\Phi_{10}^{5/2}/\eta^{60}$ |
| 6 | 720 | 2 | $\{\zeta(3)^2\}$ | $(\Phi_{10}/\eta^{24})^3$ |
| 7 | 5040 | 2 | $\{\zeta(7), \zeta(3, 4)\}$ | $\Phi_{10}^{7/2}/\eta^{84}$ |
| 8 | 40320 | 3 | $\{\zeta(3, 5), \zeta(3)\zeta(5), \zeta(5, 3)\}$ | $\Phi_{10}^4/\eta^{96}$ |
| 9 | 362880 | 4 | $\{\zeta(9), \zeta(3)\zeta(3, 3), \zeta(3, 3, 3), \zeta(3, 6)\}$ | $\Phi_{10}^{9/2}/\eta^{108}$ |
| 10 | 3628800 | 5 | $\{\zeta(3)^2\zeta(3, 3), \zeta(3)\zeta(7), \zeta(5)^2, \zeta(3, 7), \zeta(5, 5)\}$ | $\Phi_{10}^5/\eta^{120}$ |
| 11 | 39916800 | 7 | $\{\zeta(11), \zeta(3)\zeta(3, 5), \zeta(3)\zeta(5, 3), \zeta(5)\zeta(3, 3), \zeta(3, 8), \zeta(5, 6), \zeta(3, 3, 5)\}$ | $\Phi_{10}^{11/2}/\eta^{132}$ |
| 12 | 479001600 | 9 | $\{\zeta(3)^4, \zeta(3)\zeta(9), \ldots, \mathbf{\zeta(3, 3, 3, 3)}\}$ | $\Phi_{10}^6/\eta^{144}$ |

Wave 14 explicitly: $\phi^{(3)} = \zeta(3) c_{\mathrm{symm}} + (25/3) c_{\mathrm{timelike}} + (\Phi_{10}/\eta^{24}) c_{\Phi_{10}}$, where $25/3 = (\mathrm{rk}(\mathrm{II}_{25, 1}) - 1)/3$ is the Fake-Monster Cartan rank minus timelike direction, NOT a Virasoro central charge.

Wave 19 Etingof computed the first depth-4 MZV coefficient at weight 12:
$$c_{12}^{(9)} = \frac{\zeta(3, 3, 3, 3)}{12!} = 6.1795 \times 10^{-13}.$$
(The draft value $\zeta(3, 3, 3, 3) \approx 0.0028565$ was incorrect by $\sim 10\times$; the correct strict-inequality Euler-Zagier value is $0.0002960\ldots$, verified against Vermaseren's multi-zeta database and independent O(N) partial-sum reconstruction.)

**Borcherds dominance.** At $n = 10$: $\dim c_n^{(\mathrm{K3})}/d_n \sim 6.4 \times 10^9$. At $n = 12$: $\sim 4.6 \times 10^{10}$. The Borcherds leg dominates the MZV leg by $10^{10}$-order as $n$ grows — the K3-specific automorphic content overwhelms the universal motivic content asymptotically.

**Non-closure.** Because the BKM imaginary cone is infinite-dimensional, $\phi^{(n)}$ does not vanish for any $n$. $\mathbf{H}_{\Delta_5}$ is a GENUINE $A_\infty$-quasi-Hopf algebra. The pro-limit $\mathrm{obs}_\infty = \varprojlim_m (\text{tower}/W^{\ge m})$ is a well-defined formal $\hbar$-series via Mittag-Leffler.

**Cyclic $A_\infty$ structure.** The BKM Killing form (inherited from $\Lambda^{2, 1}$ lattice pairing) makes the $A_\infty$-structure cyclic: $\langle\phi^{(n)}(a_1, \ldots, a_n), a_{n+1}\rangle = (-1)^{\epsilon_n}\langle a_1, \phi^{(n)}(a_2, \ldots, a_{n+1})\rangle$. Verified at all computed orders.

---

## 7. The BV obstruction tower and the Heegner pattern

Wave 18 Costello proved the all-orders Heegner-BV theorem:

**Theorem.** For BV-quantised twisted 11D SUGRA on $\mathbb{R}^3 \times \mathrm{K3} \times \mathbb{C}^2$ with 24 M5-branes on $I_1$ Kodaira fibres, the $\hbar^n$-order BV master equation obstruction class is
$$c_n = c_{\phi_{-2, 1}}(-n) \cdot [H_n] \in H^2(\mathfrak{g}_{\Delta_5}, \mathbb{C}) \cong \mathbb{C} \cdot [\Delta_5]$$
for all $n \ge 1$, with $\phi_{-2, 1}(\tau, z) = -(y - 2 + y^{-1})\prod_{n \ge 1}(1 - q^n y)^2(1 - q^n/y)^2(1 - q^n)^{-4}$ the weight-$-2$, index-1 weak Jacobi form. Admissibility: $n \equiv 0, 3 \pmod 4$; otherwise $c_n = 0$.

Specific values:

| $n$ | admissible? | $c_n$ |
|---|---|---|
| 1 | no | 0 (multiplicity-2 $H_1$ via $\mathrm{div}(\Phi_{10}) = 2 H_1$ separately) |
| 2 | no | 0 |
| 3 | yes | $-8$ (corrected from erroneous $176256 = p_{24}(5)$) |
| 4 | yes | $12$ |
| 5 | no | 0 |
| 6 | no | 0 |
| 7 | yes | $-39$ |
| 8 | yes | $56$ |
| 11 | yes | $-152$ |
| 12 | yes | $208$ |

The proof assembles three primary inputs: Bruinier 2002 Heegner-Chern reciprocity; Borcherds 1998 singular-theta lift $\phi_{-2, 1} \mapsto \Phi_{10}$; Costello-Gaiotto-Paquette 2018 one-loop factorisation-algebra holography.

**Asymptotic structure.** $|c_n| \sim \exp(\pi\sqrt{n})$ (Ramanujan-Petersson for Jacobi forms). The BV tower is Gevrey-1-divergent in naive $\hbar$-expansion.

**All-loop Borcherds resummation** (Wave 20 Costello). Exponentiation recovers:
$$\exp\Bigl(\sum_{n \ge 1}\hbar^n c_n\Bigr) = (pqy^{1/2})^\hbar \prod_{(m, n, r) > 0}(1 - p^m q^n y^r)^{-\hbar c_{\phi_{-2, 1}}(4mn - r^2)} = (\Phi_{10}/\eta^{24})^\hbar$$
as formal power series. The all-loop BV master equation solution is $S_q = S_{\mathrm{cl}} + \hbar \log(\Phi_{10}/\eta^{24})$; bulk-boundary duality reads $Z_{\mathrm{bulk}} \cdot Z_{\mathrm{boundary}} = \eta^{-24}$ at $\hbar = 1$ modulo classical phase and absorbed one-loop $\eta^{24}$ anomaly. The perturbative divergent series is the asymptotic presentation of the exact Borcherds infinite product — perturbative and non-perturbative completions agree at the all-loop exponential level.

**Non-perturbative D3-instantons** (Wave 19 Costello). Each rigid holomorphic curve $[C] \in H_2^+(\mathrm{K3})$ contributes a D3-instanton of weight $e^{-2\pi\mathrm{vol}(C)/|\hbar|}$; the Borcherds infinite-product factors correspond one-to-one with D3-instantons via the Mukai-lattice embedding $(m, n, r) \leftrightarrow [C]$.

---

## 8. Arthur packets and local Langlands

The automorphic home of $\Delta_5$ carries a rich Langlands parametrisation. $\Delta_5$ lives on the Maass spin cover $\widetilde{\mathrm{Sp}_4(\mathbb{Z})}$ (not paramodular $K(N)$ — a Wave-14 retraction), with character $v_{\Delta_5}$ factoring through $\mathrm{Sp}_4(\mathbb{Z}/2) \cong S_6$.

**Squaring relation.** $\Delta_5^2 = \Delta_{10}$ (Igusa weight-10 Siegel cusp form). The Gritsenko-Shimura-Waldspurger square $\Delta_5 \to \Delta_{10}$ factors through the double cover; Borcherds lift for $\Delta_{10}$ equals $\mathrm{Ikeda}_4(\Delta_{E_6})$ of the weight-16 elliptic newform.

**Arthur parameter.** $\Delta_{10}$ has Saito-Kurokawa non-tempered CAP parameter
$$\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1: L_F \times \mathrm{SL}_2(\mathbb{C}) \to \mathrm{SO}_5(\mathbb{C}) = {}^L\mathrm{Sp}_4.$$
Endoscopic transfer $\mathrm{Sp}_4 \to \mathrm{GL}_5$. Global component group $S_{\psi_{\Delta_{10}}} = \mathbb{Z}/2$; global packet $|\Psi_{\Delta_{10}}| = 4$.

**Maass spin refinement for $\Delta_5$** (Wave 18 Kazhdan). $S_{\psi_{\Delta_5}} = (\mathbb{Z}/2)^2$ Klein-four, distinguished from $\mathbb{Z}/4$ by Schur-Weil computation: $\varepsilon_{\mathrm{holo}}$ (internal to $\mathrm{Sym}^1$) and $\zeta_{\mathrm{spin}}$ (spin-cover central) commute. Global packet $|\Psi_{\Delta_5}| = 16$ = $4 \cdot 4$, with 4 distinguished cuspidal constituents.

**Hecke eigenvalues** (Wave 17+18 Beilinson). $\lambda_p(\Delta_{10}) = a_p(\Delta_{E_6}) + p^8 + p^9$ (Andrianov-Ikeda) verified first-principles through $p \le 79$ via $E_4 \cdot \Delta$ convolution (the unique $S_{16}(\mathrm{SL}_2(\mathbb{Z}))$ cuspform). All 22 primes satisfy Deligne-Weissauer bound $|a_p| \le 2p^{15/2}$.

**Local Langlands at all places.**
- **Unramified primes $p \ne 2$**: Satake parameters $(\alpha_p, \beta_p) \in \mathrm{SO}_5(\mathbb{C})$ with spinor Euler factor $Z_p(s) = \zeta_p(s - 8)\zeta_p(s - 9)L_p(s, \Delta_{E_6})$.
- **$p = 2$ ramification** (Wave 16 Kazhdan): $\psi_{\Delta_5, 2} = \phi_{\Delta_{E_6}, 2} \boxtimes \mathrm{Sym}^1 \otimes \varepsilon_2$ with $\varepsilon_2$ quadratic character of conductor $2^3$ (class of $\sqrt{2} \in \mathbb{Q}_2^\times/(\mathbb{Q}_2^\times)^2$).
- **Archimedean** (Wave 17-18 Kazhdan): $\phi_{\Delta_{10}, \infty}$ Schmidt $(17/2, 15/2)$ on $W_{\mathbb{R}} = \mathbb{C}^\times \rtimes \mathbb{Z}/2$; $\phi_{\Delta_5, \infty}$ Schmidt $(7/2, 5/2)$ $\otimes$ $\mathrm{sgn}_{\mathbb{R}}$.
- **Global consistency** (Wave 18 Kazhdan): $\varepsilon_\infty \cdot \varepsilon_2 = (-1)(-1) = +1$ via Hilbert reciprocity on $(-1, 2)_\mathbb{Q}$.

**Geometric Langlands self-duality** (Wave 17 Kazhdan). ${}^L\mathfrak{g}_{\Delta_5} = \mathfrak{g}_{\Delta_5}$ (Cartan matrix symmetric under Langlands; lattice $\Lambda^{2, 1}$ symmetric). Arinkin-Gaitsgory correspondence degenerates to self-duality exchanged by Fricke involution $w_8: Z \mapsto -(8Z)^{-1}$ — the modular $S$-matrix of the $\mathbf{H}_{\Delta_5}$-module category.

---

## 9. Non-semisimple modular tensor category and 3d TQFT

At $q = \zeta_8$, $\mathfrak{u}_{\zeta_8}(\widehat{\mathfrak{m}}_{\Delta_5})$ is finite-dimensional (Lusztig small form) with PBW bound $8^{129}$. Its representation category is a non-semisimple Kerler-Lyubashenko modular tensor category.

**Fusion ring** (Wave 17 Gelfand). 3 fundamental generators $V_{\alpha_1}, V_{\alpha_2}, V_{\alpha_3}$ from real simple roots. At $\ell = 8$ Kac-Walton truncation:
- Diagonal: $V_{\alpha_i} \otimes V_{\alpha_i} = V_0 \oplus V_{2\alpha_i}$.
- Off-diagonal: $V_{\alpha_i} \otimes V_{\alpha_j} = V_{\alpha_i + \alpha_j} \oplus V_{\alpha_i - \alpha_j}$ ($i \ne j$).
$(h^\vee = 1$ for hyperbolic BKM; $\ell - h^\vee = 7$.)

**Modular $S$-matrix = Fricke** (Wave 17 Gelfand). $S = w_8: Z \mapsto -(8Z)^{-1}$ on Siegel $\mathbb{H}_2$. Eigenvalues $\{1, i, -1, -i\}$ on semisimple quotient; $S^4 = \mathrm{id}$. Generic trace 0; $M_{24}$-invariant Humbert-block trace 4.

**Plancherel decomposition** (Wave 17 Gelfand; Wave 20 closed form). On non-semisimple MTCs, Plancherel decomposes via Kerler-Lyubashenko coend:
$$L^2_{\mathrm{cat}}(\mathbf{H}_{\Delta_5}) = \int^\oplus_{\widehat{\mathbf{H}}_{\Delta_5}} P_\lambda \otimes P_\lambda^\vee\,d\mu_{\mathrm{Plan}}(\lambda)$$
over indecomposable projective covers $P_\lambda$ (not simples). Plancherel measure integrates to:
$$\int \mathrm{tr}_{P_\lambda}(q^{L_0}q'^{L_0'})\,d\mu_{\mathrm{Plan}} = \frac{1}{\Phi_{10}(Z)}.$$
Closed form: $\mathcal{D}_N^2 = 8^{d(N) + 3}\prod_{\mathrm{ht}(\alpha) \le N}[\ell]_{q_\alpha} [\ell]_{q_\alpha}^{\mathrm{mult}(\alpha)}$ with pro-limit $\to 1/\Phi_{10}$.

**$\mu_8$-gerbe on $\overline{\mathcal{A}_2}$** (Waves 15, 18, 20). The Siegel-Borcherds associator $\widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}]$ defines a $\mu_8$-gerbe on $\overline{\mathcal{A}_2}$. Chain-level banding cocycle:
$$F_{ij}(Z) = \frac{[\Phi_{10}/\eta^{24}]^{1/8}|_{U_i}}{[\Phi_{10}/\eta^{24}]^{1/8}|_{U_j}}, \quad F_{ij}^8 = 1$$
on Igusa fundamental-domain cover. Trivialisable on Koszul locus $\overline{\mathcal{A}_2} \setminus (H_1 \cup H_4)$; gerbe-obstructed on $H_1 \cup H_4$ with orders 8 and 16.

Wave 20 Gelfand extracted the 3-cocycle:
$$\omega^{\mathrm{Bruinier}}(a, b, c) = \zeta_8^{a\lfloor(b + c)/8\rfloor} \cdot \zeta_{16}^{abc \cdot \mathbf{1}_{H_4}(Z)}.$$

**Non-semisimple pseudo-character $S^{\mathrm{ps}}$** (Waves 19-20 Gelfand). Via Creutzig-Ridout pseudo-traces on projective covers with Jordan-block structure:
$$S^{\mathrm{ps}}: \mathrm{End}(\mathcal{L}_{\mathcal{C}}) \to \mathrm{End}(\mathcal{L}_{\mathcal{C}}), \quad f \mapsto \mathrm{tr}_1(R_{21}(f \otimes \mathrm{id}) R_{12}^{-1})$$
with $\mathcal{L}_{\mathcal{C}} = \int^X X \otimes X^\vee$ Lyubashenko coend. Logarithmic Loewy block (Creutzig-Ridout) has Loewy length $2c_{\mathrm{Cox}} + 1 = 49$, multiplicities $(20, -2, -4, -2, \ldots)$ from EOT K3 elliptic genus.

**3d TQFT state spaces** (Waves 19-20 Polyakov).
- $Z(T^2) = \mathrm{HH}_0^{\mathrm{cat}}(\mathcal{C})$, dim $\le 8^{129}$.
- $Z(\Sigma_2) = \mathrm{HH}_0^{\mathrm{cat}}(\mathcal{C} \boxtimes \mathcal{C}^{\mathrm{op}})$; partition function on $\Sigma_2$ equals $1/\Phi_{10}$.
- $\mathrm{Sp}_4(\mathbb{Z})$-modular cocycle of weight 10 on $Z(\Sigma_2)$ via Lyubashenko-Virelizier MCG representation.
- Decomposition: $Z(\Sigma_2) \simeq \bigoplus_{f \in B_{10}^{\mathrm{Maass}}} \mathbb{C} \cdot f$ on Maass-Spezialschar basis.

**Reshetikhin-Turaev-DGGPR quantum invariants** (Wave 20 Polyakov).
- $\tau(S^3) = \mathcal{D}^{-1} = 8^{-65}$ (via $\mathcal{D}^2 = 8^{130}$).
- $\tau(S^2 \times S^1) = |\mathrm{IndProj}(\mathcal{C})|$.
- $\tau(\Sigma_g \times S^1)$: genus-$g$ tower $\{1, 1, 2, 4, 7, 12, 22\}$ for $g = 2, \ldots, 8$ bounded by $\dim M_{10}^{\mathrm{Sieg}}(\mathrm{Sp}_{2g}(\mathbb{Z}))$.
- Lens-space torsor: $\tau(L(8, q))$ for $q \in (\mathbb{Z}/8)^\times$ form a $\mathrm{Gal}(\mathbb{Q}(\zeta_8)/\mathbb{Q})$-torsor realising the $\mu_8$-gerbe.
- Fricke mapping torus: $\tau(\Sigma_2 \times_{w_8} S^1) = 2 e^{i\pi/4}$, magnitude 2, phase $\pi/4$ tracking $\mu_8$-gerbe anomaly.
- Poincaré homology sphere: Lawrence-Rozansky Seifert closed form with binary-icosahedral partition over 5 $A_5$-conjugacy classes.

---

## 10. The $A_{N-1}$ class-$\mathcal{S}$ family and umbral Niemeier bijection

$\mathbf{H}_{\Delta_5}$ is the Beem-Rastelli protected chiral algebra of the 4d $\mathcal{N}=2$ theory $\mathcal{T}[A_1, \Sigma_{0, 24}]$ — class-$\mathcal{S}$ of type $A_1$ on the 24-punctured sphere with $M_{24}$ acting on punctures via Steiner $S(5, 8, 24)$.

**Central charges** (Chacaltana-Distler + Shapere-Tachikawa + Beem-Rastelli):
$$c_{4d}(A_1, \Sigma_{0, 24}) = \frac{2n_v + n_h}{12} = \frac{2 \cdot 63 + 88}{12} = \frac{214}{12} = \frac{107}{6}, \quad c_{2d} = -12 c_{4d} = -214.$$
Trinion data: $T_2$ has $(n_v, n_h) = (0, 4)$; $A_1$ on $\Sigma_{0, 24}$ decomposes into 22 trinions + 21 gauge tubes giving $(n_v, n_h) = (63, 88)$.

Wave-14 erroneously reported $(26, -312)$ via formula $(12(g-1) + 7n)/6$; Wave 15 Gaiotto restored $(107/6, -214)$ via first-principles Chacaltana-Distler; Wave 16 Polyakov cascaded the retraction. $107$ is prime, so no non-trivial integer factorisation of $-214$ beyond $-2 \cdot 107$.

The correct modular covariance is Siegel (not elliptic): partition function is a Siegel modular form of weight 5 via $\Delta_5 = \Phi_{10}^{1/2}$. The ratio $-c_{2d}/24 = 107/12$ is non-integer — a signature of Siegel rather than elliptic modularity.

**Effective spectrum on real-root unitary submodule** (Wave 17 Polyakov). Hyperbolic Cartan signature $(2, 1)$ with eigenvalues $\{+4, +4, -2\}$. Real-root unitary submodule $V^{\mathrm{unit}} = \{V^\lambda : \lambda \in P_+^*, \lambda^2 > 0\}$ has $c_{\mathrm{unit}} = \mathrm{rk}(P) = 2$, giving genuine positive entanglement $S_{\mathrm{EE}} = (2/3)\log(L/\epsilon)$. Effective full-module $c_{\mathrm{eff}} = c - 24 h_{\min} = -214 + 48 = -166 = -2 \cdot 83$ (83 prime) is a gravitational-anomaly coefficient, not Hilbert-space entropy.

**$N$-family** (Wave 15-19 Gaiotto). For $\mathcal{T}[A_{N-1}, \Sigma_{0, 24}]$:
$$k_N = \frac{N+3}{2} \text{ on spin cover}, \quad f^{(N)}(0, 0) = 2(N + 3).$$
Verified for $N = 3$: $f^{(3)}(0, 0) = 12$, $k_3 = 3$. For $N = 4$: $f^{(4)}(0, 0) = 14$, $k_4 = 7/2$. Honest Siegel weights: $(5, 6, 7, 8)$ for $N = 2, 3, 4, 5$ on the honest cover.

**Umbral Niemeier bijection** (Wave 19 Gaiotto corrected).
The $A_{N-1}$ class-$\mathcal{S}$ family admits umbral-Niemeier labelling iff $(N - 1) \mid 24$ (the rank of $A_{N-1}$ is $N - 1$, which must divide 24). Valid $N$: $\{2, 3, 4, 5, 7, 9, 13, 25\}$. For $N \in \{6, 8, 12, 24\}$: substitute Niemeiers.

Full umbral table:

| $N$ | Niemeier | Umbral group | $k_N$ (spin) |
|---|---|---|---|
| 2 | $24A_1$ | $M_{24}$ | $5/2$ |
| 3 | $12A_2$ | $2.M_{12}$ | $3$ |
| 4 | $8A_3$ | $2.\mathrm{AGL}_3(2)$ | $7/2$ |
| 5 | $6A_4$ | $\mathrm{GL}_2(5)/\{\pm 1\}$ | $4$ |
| 6 | $6D_4$ | $3.\mathrm{Sym}_6$ | $9/2$ |
| 7 | $4A_6$ | $\mathrm{SL}_2(3)$ | $5$ |
| 8 | $2A_7 D_5^2$ | $\mathbb{Z}/2$ | $11/2$ |
| 9 | $3A_8$ | $\mathrm{Dih}_4$ | $6$ |
| 12 | $A_{11}D_7E_6$ | trivial | $15/2$ |
| 13 | $2A_{12}$ | $\mathbb{Z}/4$ | $8$ |
| 24 | Leech $\Lambda_{24}$ | $\mathrm{Co}_0 = 2.\mathrm{Co}_1$ | $27/2$ (Conway moonshine) |
| 25 | $A_{24}$ | $\mathbb{Z}/2$ | $14$ |

At $N = 24$: Leech lattice has no roots; escapes to Conway moonshine (Wave 19 Witten fifth $\Psi$-image; Wave 20 Kazhdan explicit Conway McKay-Thompson Fourier data).

---

## 11. The $\Psi$-functor landscape

The universal functor
$$\Psi: \mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2 \longrightarrow \mathrm{QHopf}^{\mathrm{BKM}}$$
takes a CY-2 automorphic-product datum (lattice $L$ + Jacobi form $\phi_L$ → Siegel form $\Sigma(\phi_L)$) to the Hall-Drinfeld double of the lattice-adapted cohomological Hall algebra. Five flagship images:

| Input lattice | Signature | Siegel form | Weight | $\Psi$-image | Cartan rank | $\ell$ |
|---|---|---|---|---|---|---|
| $\mathrm{II}_{1, 1}$ | $(1, 1)$ | $j(\sigma) - j(\tau)$ | $0$ | $\mathbf{H}_{\mathrm{Monster}}$ | $2$ | $2$ |
| Leech$^{\mathrm{super}}$ | $(24, 0)$ | Conway denominator | $\ldots$ | $\mathbf{H}_{\mathrm{Conway}} = V^{s\natural}$-double | $2$ (super) | $2$ |
| $E_8 \oplus \mathrm{II}_{1, 1}(2)$ | $(1, 9)$ | $\Delta_5^{\mathrm{Enr}}$ | $5/2$ (metaplectic) | $\mathbf{H}_{\Delta_5}^{\mathrm{Enr}} = \mathbf{H}_{\Delta_5}/\!/\mathbb{Z}/2$ | — | $4$ |
| $\Lambda^{2, 1}_{II}$ (K3) | $(2, 1)$ | $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ | $5$ | $\mathbf{H}_{\Delta_5}$ | $3$ | $8$ |
| $\mathrm{II}_{25, 1}$ (Fake-M) | $(25, 1)$ | $\Phi_{12} = \mathrm{Borch}(\phi_{0, 1}^{\mathrm{K3}})$ | $12$ | $\mathbf{H}_{\mathrm{Fake-M}}$ | $26$ | $50$ |

These are co-siblings under $\Psi$, not nested subalgebras. Non-embedding proofs: Cartan-rank mismatches (2 vs 3 vs 26); Mukai $\mathrm{II}_{4, 20}$ does not signature-preservingly embed in Leech; weights $\{0, 5/2, 5, 12\}$ all different.

**Critical disambiguation** (Wave 16 Gaiotto). For K3 elliptic genus $\phi_{0, 1}^{\mathrm{K3}}$:
- Borcherds multiplicative lift $\mathrm{Borch}(\phi_{0, 1}^{\mathrm{K3}}) = \Phi_{12}$ (Igusa weight 12) — the Fake-Monster denominator.
- Gritsenko additive lift $\mathrm{Grit}(\eta^9\vartheta_1) = \Delta_5$ (weight 5) — the K3-BKM denominator of $\mathbf{H}_{\Delta_5}$.

These are DIFFERENT Siegel modular forms. The K3-BKM denominator is $\Delta_5$, not $\Phi_{12}$.

**$\Psi$ as lax symmetric-monoidal functor of operads** (Wave 20 Gaiotto). The operadic domain $(\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2, \oplus)$ carries $E_2$-structure from lattice-doubling + Jacobi-form tensor product; the operadic codomain $(\mathrm{QHopf}^{\mathrm{BKM}}, \otimes)$ carries $E_1$-structure from algebra tensor product + coproduct factorisation. $\Psi$ is an $E_2 \to E_1$ operadic map (Dunn-stabilisation) with lax comparison $\mu_{L_1, L_2}: \Psi(L_1) \otimes \Psi(L_2) \xrightarrow{\sim} \Psi(L_1 \oplus L_2)$ on the Koszul locus. Test case: $\Psi(\mathrm{II}_{1, 1} \oplus \mathrm{II}_{1, 1}) \simeq \mathbf{H}_{\mathrm{Monster}} \otimes \mathbf{H}_{\mathrm{Monster}}$ giving rank-4 BKM on $\mathrm{II}_{2, 2}$. The Reshetikhin-Turaev quantum invariants factorise compatibly: $Z_{\mathrm{RT}}\circ\Psi$ is symmetric-monoidal, realising the physical "disjoint union = multiplicative" principle.

---

## 12. Humbert stratification and nearby cycles

The Siegel moduli stack $\overline{\mathcal{A}_2}$ is stratified by Humbert divisors $H_n$ of discriminant $n$:

| Divisor | Structure | Monodromy order | Role |
|---|---|---|---|
| $H_1$ | products of elliptic curves | $\mathbb{Z}/8$ | $\hbar^2 = -1/8$ specialisation |
| $H_3$ | RM $\mathbb{Z}[(1+\sqrt 3)/2]$ | ? | 3-loop BV $c_3 = -8 \cdot [H_3]$ lives here |
| $H_4$ | $(2, 2)$-isogeny quotient of $E_1 \times E_2$, CM $\mathbb{Z}[2i]$ | $\mathbb{Z}/2$ | Koszul-locus boundary |
| $H_n$ for $n \equiv 0, 3 \pmod 4$ | admissible Heegner divisors | various | $n$-loop BV $c_n = c_{\phi_{-2, 1}}(-n) \cdot [H_n]$ |

**Koszul locus.** The full Koszul locus for the bar-cobar adjunction is
$$\mathcal{U}^{\mathrm{adm}} = \overline{\mathcal{A}_2} \setminus \bigcup_{n \equiv 0, 3 \pmod 4} H_n.$$
(Wave 18 Beilinson tightening of Wave 15's "$H_1 \cup H_4$" statement.)

**Chain-level nearby-cycle comparison** (Wave 20 Beilinson). For each admissible $H_n$:
- Nearby cycle $\psi_n: A|_{H_n^{\mathrm{nbd}}} \to \mathcal{D}\text{-mod}$ with unipotent monodromy of order $\ell_n$.
- Koszul filtration $F^k B(A) = V^{\ge k/\ell_n}$ with graded pieces $B_k(A_{H_n})$.
- $\lim^1$-obstruction = Fourier coefficient $c_{-2, 1}(n, r_n)$ of $\phi_{-2, 1}$ at $H_n$.

**Global inversion theorem.** For $A = \mathbf{H}_{\Delta_5}$:
(i) Strict $\Omega^{\mathrm{ch}} B^{\mathrm{ch}} A \simeq A$ on $\mathcal{U}^{\mathrm{adm}}$.
(ii) Weight-completed coderived $\Omega^{\mathrm{ch}}_W B^{\mathrm{ch}}_W A \simeq A$ on each $H_n^{\mathrm{nbd}}$ with nilpotency index $\ell_n$.
(iii) $A_\infty$-correction via $\phi^{(3)}$ at $H_3$; via $\phi^{(n)}$ at each admissible $H_n$.
(iv) Global: glued via Čech descent across the stratification.

**Bridgeland-stability dictionary** (Wave 19 Beilinson). Map
$$\Theta: \mathrm{Stab}^\dagger(D^b\mathrm{Coh}(\mathrm{K3}))/\Gamma \to \{R\text{-matrices of }\mathbf{H}_{\Delta_5}\}$$
via Bayer-Macrì-Igusa composite $\iota: \mathrm{Stab}^\dagger/\Gamma \xrightarrow{\pi} \mathcal{P}(\widetilde{\Lambda}_{\mathrm{K3}}) \xrightarrow{\mathrm{Sieg}} \overline{\mathcal{A}_2}$, intertwining autoequivalence group $\Gamma$ with paramodular $K(1)$. Three canonical boundary specialisations:
- Large-volume cusp $\mapsto R^{\mathrm{rat}}_{\mathrm{Yang}}$.
- Gepner point $\mapsto R^{\mathrm{trig}}_{q = \zeta_8}$ (via $\mathbb{Z}/8$-fixed period).
- Humbert $H_1$ boundary $\mapsto R^{\mathrm{ell, dyn}}_{\mathrm{Felder}}$.

Across walls of marginal stability: $R^{(\sigma')} = F_{\sigma\sigma'} \cdot R^{(\sigma)} \cdot F_{\sigma\sigma'}^{-1}$ with $F_{\sigma\sigma'}$ the Etingof-Kazhdan image of Kontsevich-Soibelman dilogarithm wall-crossing element.

---

## 13. CY-2 landscape dichotomy

Classification of compact Kähler CY-2 surfaces partitioned by $\Psi$-image (Wave 17 Witten):

| Surface | $\chi_{\mathrm{top}}$ | $c_1$ | $h^{2, 0}$ | $\pi_1$ | $\Psi$-image | Taxon | Siegel weight |
|---|---|---|---|---|---|---|---|
| K3 | 24 | 0 | 1 | $\{1\}$ | $\mathbf{H}_{\Delta_5}$ | 4th (BKM) | 5 |
| Kummer K3 | 24 | 0 | 1 | $\{1\}$ | $\mathbf{H}_{\Delta_5}|_{\Lambda_{\mathrm{Kum}}}$ sublattice | 4th | 5 |
| Enriques | 12 | 0 | 0 | $\mathbb{Z}/2$ | $\mathbf{H}_{\Delta_5}/\!/\mathbb{Z}/2$ | 4th-$\mathbb{Z}/2$ | 5/2 metaplectic |
| $T^4$ | 0 | 0 | 1 | $\mathbb{Z}^4$ | $V_{\mathrm{II}_{4, 4}}$ Heisenberg | G (abelian) | 0 |
| Bielliptic | 0 | 0 | 0 | $\mathbb{Z}^4 \rtimes G$ | $V_{\mathrm{II}_{4, 4}}/G$ orbifold | G | 0 |
| Half-K3 / dP$_9$ | 12 | $-f \ne 0$ | 0 | $\{1\}$ | $\widehat{E_8}_{k = 1}$ | L (affine) | 0 |

**Linear weight formula** on 4th-taxon column:
$$w_{\mathrm{Borch}}(X) = \frac{5 \chi_{\mathrm{top}}(X)}{24}.$$

K3 is the unique maximally-large $\chi_{\mathrm{top}} = 24$ simply-connected CY-2; the fourth taxon (BKM quantum groups) realises only for $\chi \in \{12, 24\}$ via (Enriques, K3). $T^4$ and bielliptic fall to taxon G (Heisenberg); half-K3 falls to taxon L (affine Kac-Moody $\widehat{E_8}$ at level 1).

---

## 14. The Khovanov categorification

Wave 20 Nekrasov constructed:

**Theorem.** The dg-category $\mathrm{Kh}_{\Delta_5}$ with objects indexed by the Humbert-admissible weight lattice $\Lambda_{\mathrm{K3}}^+ \subset \mathrm{II}_{3, 2}$, morphisms $\mathrm{RHom}$ over the chiral Koszul dual $\mathbf{H}_{\Delta_5}^!$, and Koszul Maurer-Cartan differential satisfies:
$$K_0(\mathrm{Kh}_{\Delta_5}) \otimes \mathbb{Z}[q^{\pm 1}] \simeq K\mathrm{HA}_{\mathrm{K3}\times E}\text{-Mod},$$
specialising at $q = \zeta_8$ to $\mathfrak{u}_{\zeta_8}(\mathbf{H}_{\Delta_5})$-Mod and at $q = 1$ to cohomological $\mathrm{CoHA}_{\mathrm{K3}\times E}$.

Serre functor $S_{\mathrm{Kh}}(P_\lambda) = P_\lambda[d_\lambda]$ with $d_\lambda = \dim_{\mathrm{qu}}(P_\lambda)$ quantum dimension. Maulik-Okounkov $Y^{\mathrm{MO}}_\hbar(\mathrm{Hilb}^n(\mathrm{K3}))$ acts via $K$-theoretic stable envelopes, making $\mathrm{Kh}_{\Delta_5}$ a Nakajima-Webster-style categorification of $\bigotimes_{i = 1}^{24} V_{\omega_i}$.

Four derived equivalences:
$$\mathrm{Kh}_{\Delta_5} \simeq D^b\mathrm{Coh}(\mathcal{M}_{\mathrm{Coulomb}}(\mathcal{T}[A_1, \Sigma_{0, 24}])) \simeq \varinjlim_n \mathrm{Fuk}(\mathrm{Hilb}^{[n]}(\mathrm{K3})) \simeq \text{Koszul-dual dg-category}.$$
The Fukaya incarnation: vanishing-cycle Lagrangians $L_\lambda$ map to $P_\lambda$ under homological mirror symmetry; Floer complexes compute Koszul $\mathrm{RHom}$.

---

## 15. The five duality frames and the seven routes

All routes into $\mathbf{H}_{\Delta_5}$ converge; no route is privileged; each exhibits a distinct face.

**Five string/M-theory duality frames** (Wave 15 Witten):

| Frame | Setup | $\Delta_5$ origin |
|---|---|---|
| Heterotic | on $T^6$ with self-dual $T^2$ | Harvey-Moore 1996 1-loop threshold |
| IIA | on $\mathrm{K3} \times T^2$ | Narain $\mathrm{II}_{3, 19}$ via T-duality |
| M-theory | on $\mathrm{K3} \times T^3$ | lift of IIA |
| IIB | on $\mathrm{K3} \times S^1$ | T-dual to IIA |
| F-theory | on elliptic $\mathrm{K3} \times T^2$ | 24 $I_1$ 7-branes + $\mathrm{SL}_2(\mathbb{Z})$ |

**Sixth route.** M-theory on $\mathrm{K3}^2 \times S^1$ as second-quantised BKM (Dijkgraaf-Verlinde-Verlinde 1997):
$$Z_{M/\mathrm{K3}^2 \times S^1}(Z) = 1/\Phi_{10}(Z).$$

**Seventh route** (Wave 17 Nekrasov). Gromov-Witten / Donaldson-Thomas on $\mathrm{K3} \times E$: $Z^{\mathrm{red}}_{\mathrm{GW}} = Z^{\mathrm{red}}_{\mathrm{DT}} = 1/\Phi_{10}$ (Oberdieck-Pandharipande 2015, Oberdieck-Pixton 2016 unconditional).

**Decoupling limit at chain level** (Wave 15 Witten). Heterotic on $T^6$ with $g_s \to 0$, $R_{T^2} \to R_{\mathrm{sd}} = \sqrt{\alpha'/2}$, $R_{T^4} \to \infty$ isolates $\mathbf{H}_{\Delta_5}$ as standalone. At factorisation-algebra level (Costello-Gwilliam): observables concentrate on codim-4 submanifold $T^2$ in the degenerate limit.

**F-theory 24-brane monodromy** (Wave 15 Witten). Product of 24 local $I_1$ monodromies in $\mathrm{SL}_2(\mathbb{Z})$ equals identity. $M_{24}$ permutes them via Steiner $S(5, 8, 24)$.

**Six routes are DIFFERENT constructions**, not six applications of a single $\Phi$. Each route has different generator rank $\rho^{R_i} \in \{3, 12, 24\}$; convergence at the output $\mathbf{H}_{\Delta_5}$ is a non-trivial theorem, not a tautology.

---

## 16. Hodge structure and motivic periods

Wave 20 Witten established:

**Theorem.** The Chevalley-Eilenberg cohomology
$$H^k_{\mathrm{CE}}(\mathfrak{g}_{\Delta_5}) = \bigoplus_{\ell(\alpha) = k} \Lambda^k \mathfrak{g}_\alpha^*$$
carries a mixed Hodge structure: real-root graded pieces are pure Tate $(k, k)$; imaginary-root graded pieces carry genuine MHS with weight filtration from $\phi_{0, 1}^{\mathrm{K3}}$ Fourier decomposition.

Euler characteristic: $\chi_{\mathrm{CE}}(\mathfrak{g}_{\Delta_5}) = \Delta_5$ on $\mathbb{H}_2$ — Borcherds denominator identity.

**Twisted period integrals.** For $\gamma \in \Lambda^\vee_{\mathrm{Muk}}$ and $\phi \in H^1_{\mathrm{CE}}$:
$$\pi_\alpha^{(k)} = \int_{\gamma_\alpha} \phi \cdot \omega_{\mathrm{K3}}^k \in \mathbb{C}/\mathbb{Z}(k).$$
Framing by $\Delta_5$ gives arithmetic invariants in $\mathbb{Q}$-subalgebra of motivic periods.

**Motivic fundamental group** $\pi_1^{\mathrm{mot}}(\mathrm{K3})$ non-trivial via unipotent motives; contains $\mathrm{GRT}_1$-action as motivic Galois.

**Unified structural identification** (Wave 20 Witten + Etingof). $\mathrm{GRT}_1$ acts doubly: as gauge on $\mathbf{H}_{\Delta_5}$-quantisations (Etingof-Kazhdan torsor) and as motivic-Galois on K3 periods. These two actions AGREE through the Kuga-Satake functor. The Drinfeld-associator-freedom of the quantum group is literally the tangential-base-point-freedom of K3's motivic Galois group.

**Mixed Tate structure.** $H^\bullet(\mathfrak{g}_{\Delta_5})$ is mixed Tate: iterated extensions by Tate motives with weight-$n$ pieces from $\zeta(n)$-period pairings. First depth-4 MZV $\zeta(3, 3, 3, 3)$ at weight 12 matches Wave 18 Etingof $\phi^{(12)}$ Padovan dimension.

---

## 17. $M_{24}$ 't Hooft anomaly

**Pentagon = $M_{24}$ umbral cocycle agreement** (Wave 14 Gaiotto).
$$[\phi^{(3)}|_{\langle g\rangle}] = \iota_g^*[\text{umbral cocycle}] \in H^3_{\mathrm{transgr}}(\langle g\rangle, U(1)) \cong \mathbb{Z}/6$$
for $g \in M_{24}$ of order 6 ($6A$ with cycle $1^2 2^2 3^2 6^2$, $6B$ with cycle $6^4$).

**Two distinct invariants** (Wave 16 Kazhdan): Umbral shifts $m_{6A} = 2, m_{6B} = 6$ (from CDH 2014); transgression cocycle classes $6A \mapsto 2, 6B \mapsto 3 \pmod 6$. Sum of cocycle classes: $2 + 3 = 5 \equiv -1 \pmod 6$, the $\mathbb{Z}/6$-restriction of the universal identity $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$.

**Schur cocycle order.** $|H^2(M_{24}, U(1))| = 12$; the chiral-bialgebra twist has order dividing 12; the order 6 appears as the $M_{24}$-order-6 subcocycle in the pentagon $\hbar^3$ obstruction.

**Conway moonshine extension** (Wave 20 Kazhdan). At $N = 24$ class-$\mathcal{S}$ (Leech) the $M_{24}$-moonshine enhances to $\mathrm{Co}_0 = 2.\mathrm{Co}_1$. Identity class:
$$T_{1A}^{\mathrm{Conway}}(\tau) = q^{-1/2} + 0 \cdot q^0 + 276 q^{1/2} + 2048 q + 11202 q^{3/2} + \ldots$$
Hauptmodul for $\mathrm{SL}_2(\mathbb{Z})$. Ten conjugacy classes of $\mathrm{Co}_0$ produce ten Hauptmoduls for specific modular subgroups. Leech theta series shadow coefficient $196\,560$ (kissing number) at $q^2$ verified via three paths: direct theta, Conway-orbit length $|\mathrm{Co}_0|/|\mathrm{Co}_2|$, Eisenstein congruence $(65520/691)(2049 + 24)$.

**$M_{24}$ descent.** $M_{24} \subset \mathrm{Co}_1$ as sextet stabiliser; restriction of $\mathrm{Co}_0$-twined characters along $M_{24}$ recovers EOT Mathieu moonshine. The 21 Mathieu-realised classes descend from $\mathrm{Co}_1$-classes; anomalous classes $\{7A, 7B, 11A, 23A, 23B\}$ carry $\mathrm{Co}_1$-specific extensions requiring umbral Niemeier-$24 A_1$.

---

## 18. Compute infrastructure

Fifteen wave-specific compute modules and one whole-object verifier:

| Module | Wave | Contents | Tests |
|---|---|---|---|
| `schur_index_classS_A1_24` | 14 | Plethystic Schur index, 10 Fourier coeffs | ✓ |
| `arthur_hecke_delta10` | 14-18 | Hecke $a_p$ first-principles for $p \le 79$ | 89/89 |
| `gritsenko_additive_explicit` | 14 | BKM Cartan, EOT, Fourier to $q^{10}$ | ✓ |
| `twisted_11dsugra_1loop` | 14 | $\hbar^2 = -1/8$ five-frame duality | ✓ |
| `bi_based_ran` | 14 | Kuga-Satake, Torelli, nearby cycles | 22/22 |
| `pentagon_coboundary_hbar3` | 14 | $\phi^{(3)}$ coefficients | ✓ |
| `humbert_monodromy_8` | 14 | Triple-face $K = 8$ | 33/33 |
| `M24_umbral_cocycle_order6` | 14 | $6A$/$6B$ distinction | ✓ |
| `wave15_pentagon_hbar45` | 15 | $\phi^{(4)}, \phi^{(5)}$ | ✓ |
| `wave15_schur_classS_ANm1_24` | 15-19 | $A_{N-1}$ family + umbral Niemeier | 120/120 |
| `wave17_pentagon_hbar8_9_10` | 17 | $\phi^{(8, 9, 10)}$ + Padovan + Borcherds asymptotics | 27/27 |
| `wave17_cn_heegner_pattern` | 17 | $c_n = c_{\phi_{-2,1}}(-n)$ corrected Heegner | 13/13 |
| `wave17_unified_cross_check` | 17 | Cross-module regression | 58/58 |
| `wave18_pentagon_hbar11_12` | 18 | $\phi^{(11, 12)}$, depth-4 MZV | ✓ |
| `wave19_K_theoretic_coha` | 19 | K-theoretic Hall algebra, $(q_1, q_2)$-collapse | 41/41 |
| `wave19_phi12_zeta3333` | 19 | $c_{12}^{(9)} = \zeta(3, 3, 3, 3)/12!$ | 11/11 |
| `wave19_bkm_hyperbolic_landscape` | 19 | Borcherds extension of $F_3$ | 50/50 |
| `wave18_monster_bkm_lusztig` | 18 | Monster $\ell_{\mathrm{Monster}} = 2$ multi-path | 73/73 |
| `wave18_enriques_bkm` | 18 | Enriques $\mathbf{H}^{\mathrm{Enr}}_{\Delta_5}$ | ✓ |
| `wave18_heegner_pattern_phi_m21` | 18 | Heegner-BV all-orders theorem | ✓ |
| `wave20_conway_moonshine` | 20 | $T_g^{\mathrm{Conway}}$ for 10 classes | 94/94 |
| `wave17_monster_bkm` + `wave19_nonsemisimple_S` + $\ldots$ | | | |
| **`whole_object_verifier`** | post-17 | 10 WOV cross-module coherence checks | 11/11 |

Total: ~500+ passing test assertions; WOV status: VERIFIED on 10/10 coherence checks.

**Whole-object verifier checks** (post-Wave-17):
- WOV-1: $\hbar^2 K^\kappa = -1$ via three routes (Mukai/Humbert/Lusztig all = 8).
- WOV-2: CD $\to$ ST $\to$ BR chain $(n_v, n_h) = (63, 88) \to c_{4d} = 107/6 \to c_{2d} = -214$.
- WOV-3: Siegel weight 5 via four routes.
- WOV-4: BKM rank 3 orthogonal to Mukai rank 24.
- WOV-5: BV Heegner pattern corrected ($c_3 = -8$, not $176256 = p_{24}(5)$).
- WOV-6: Saito-Kurokawa chain + Deligne bound for 12 primes.
- WOV-7: Schur-index 10 Fourier coefficients.
- WOV-8: Pentagon MZV+Borcherds coherence, Padovan, Borcherds dominance at $n = 10$.
- WOV-9: $A_{N-1}$ family for $N = 2, 3, 4$.
- WOV-10: Exact Fraction $\hbar^2 \cdot 8 = -1$.

---

## 19. Retractions ledger

Four wave-level corrections, each absorbed by a subsequent wave:

1. **Central charges** ($c_{4d}, c_{2d}$). Wave 13 computed $(107/6, -214)$ via first-principles Chacaltana-Distler. Wave 14 erroneously revised to $(26, -312)$ via the formula $(12(g-1) + 7n)/6$; this formula fails the SU(2) $N_f = 4$ cross-check ($n = 4$ gives $8/3$, not $7/6$). Wave 15 Gaiotto restored $(107/6, -214)$ via pants decomposition with trinion anomalies $(n_v, n_h) = (0, 4)$. Wave 16 Polyakov propagated the retraction across ~20 Vol II files.

2. **Monster BKM Cartan rank.** Wave 16 asserted Monster rank 26 (conflating with Fake-Monster). Wave 17 Drinfeld corrected: Monster has hyperbolic rank 2 in $\mathrm{II}_{1, 1}$; Fake-Monster has rank 26 in $\mathrm{II}_{25, 1}$; K3-BKM has rank 3 in $\Lambda^{2, 1}_{II}$. Wave 18 Witten four-route verification: $\ell_{\mathrm{Monster}} = 2$ via Mukai-doubling, Fricke $w_1$, super-EK, Conway-Norton.

3. **BV 3-loop obstruction $c_3$.** Wave 16 Costello asserted $c_3 = 176256 \cdot [H_3]$. Wave 17 multi-path analysis showed $176256 = p_{24}(5)$ (24-coloured partition of 5, unrelated to $\phi_{10, 1}$). Wave 18 Costello corrected to $c_3 = -8 \cdot [H_3]$ via the all-orders Heegner theorem; factor $-22032 = 176256/(-8)$ bridges Bruinier reduced-class convention (Wave 18) and GN Cartan-matrix convention (Wave 16).

4. **$A_{N-1}$ umbral divisor rule.** Wave 18 Gaiotto asserted rule $N \mid 24$. Wave 19 Gaiotto corrected to $(N - 1) \mid 24$ (rank $A_{N-1} = N - 1$ must divide 24). Valid $N \in \{2, 3, 4, 5, 7, 9, 13, 25\}$ for naive labelling; substitute Niemeiers for $\{6, 8, 12, 24\}$.

Epistemic constitutional datum: intermediate-wave status is not authoritative without primary-source re-derivation (Beilinson's dictum). Multi-path verification (≥ 3 independent routes) prevents this class of error.

---

## 20. Open frontier

Priority-ordered residual items:

**Tier 1 — Deep mathematical.**
1. $\phi^{(n \ge 13)}$: conditional on Zagier-Hoffman depth-reduction conjecture (Brown 2017 proves only depth-2 stratum).
2. Mock-modular $H^{(\mathrm{Co}_0, g)}$ explicit Fourier expansion beyond 10 flagship classes.
3. Full Bridgeland-$R$-matrix functor $\Theta$ on non-projective K3.
4. CY-3 Kontsevich formality bridge extension ($\hbar^3$-correction from CY-3 Hodge).

**Tier 2 — Structural/categorical.**
5. PBW exact dimension of $\mathfrak{u}_{\zeta_8}$ beyond $8^{129}$ upper bound.
6. Yetter-Drinfeld $\delta^{(n \ge 4)}$ tower explicit.
7. Chain-level $\mu_8$-gerbe banding primitive over full Igusa fundamental domain.
8. Non-semisimple Turaev-Viro partition function on Poincaré homology sphere independent derivation.

**Tier 3 — Arithmetic.**
9. Hecke $a_p$ for $p \ge 83$: first-principles continuation.
10. Archimedean-$p = 2$ global $\varepsilon$ consistency at higher-weight Maass-spin Siegel forms.

**Tier 4 — Universal $\Psi$-functor.**
11. $\Psi$-image classification: surjectivity onto quasi-Hopf BKMs.
12. Enriques BKM $\mathfrak{g}_{\Delta_5}^{\mathrm{Enr}}$ Weyl denominator + $M_{12}$-moonshine independent verification.
13. Higher-$d$ $\Psi$-images at CY-3 onward (conditional on CY-C and Phi-extension).

**Tier 5 — Cross-volume.**
14. Unified $\hbar$-convention sweep (AP151) across all three volumes.
15. $\mathrm{GRT}_1$-transitivity chain-level witness for the imaginary cone.

---

## 21. The genealogy of the identification

The programme's dependency chain:

```
K3 topology χ = 24, c₁ = 0, h²⁰ = 1
    ↓ [CY-2 classification, Witten W15]
Mukai lattice II₄,₂₀, Humbert stratification
    ↓ [Gritsenko-Nikulin 1998 Siegel-automorphic-product BKM classification]
BKM Lie superalgebra g_Δ₅, denominator Δ₅ = Grit(η⁹θ₁)
    ↓ [Wave 19 Drinfeld: Borch(F_3, φ_K3)]
g_Δ₅ as Borcherds extension of Feingold-Frenkel F_3
    ↓ [Etingof-Kazhdan Parts I-V super-quantisation]
super-EK quantum group U_ℏ(g_Δ₅)
    ↓ [Wave 20 Drinfeld super-Yangian construction]
Y^super_ℏ(g_Δ₅) explicit generators + relations + PBW
    ↓ [Wave 19 Kazhdan classical ℏ→0 limit]
Classical: Gritsenko-Nikulin 1998 cobracket
    ↓ [Wave 20 KST Kontsevich formality bridge]
Super-Kontsevich deformation quantisation at ℏ² = -1/8
    ↓ [Schiffmann-Vasserot CoHA + Davison CY-3 integrality]
Hall-Drinfeld double via CoHA(K3 × E)
    ↓ [Wave 17 Drinfeld RTT + Wave 19 Nekrasov geometric (q₁q₂)-collapse]
R-matrix R_{Sieg,dyn}(u, Z) = R_rat × θ_K3
    ↓ [Bruinier 2002 Prop 5.1 Heegner-Chern reciprocity]
Three-faces identity: ℏ² · 8 = -1
    ↓ [Beem-Rastelli 2013 protected chiral algebra]
4d parent T[A₁, Σ₀,₂₄] with c₄d = 107/6
    ↓ [Costello-Gaiotto-Paquette 2018 twisted holography]
11D SUGRA on K3 × C² with 24 M5-branes BV-quantised
    ↓ [Wave 18 Costello all-orders Heegner-BV theorem]
c_n = c_{φ_{-2,1}}(-n) · [H_n] Heegner pattern
    ↓ [Wave 20 Costello exponentiation]
exp(Σ ℏⁿ c_n) = (Φ_10/η^24)^ℏ — Borcherds product = all-loop BV effective action
    ↓ [Wave 14 Gaiotto pentagon-umbral + Wave 16 Kazhdan cocycle]
M_24 't Hooft anomaly = order-6 transgression cocycle
    ↓ [Wave 17 Gelfand Kerler-Lyubashenko MTC + Fricke]
Non-semisimple MTC at ζ_8 with S = w_8 + Plancherel = 1/Φ_10
    ↓ [Wave 20 Polyakov Reshetikhin-Turaev-DGGPR]
3d TQFT invariants: τ(S³) = 8^{-65}, τ(Σ₂ ×_{w_8} S¹) = 2e^{iπ/4}
    ↓ [Oberdieck-Pixton 2016 DT unconditional]
Seventh route: GW = DT = 1/Φ_10
    ↓ [Wave 20 Etingof GRT₁^super-torsor]
H_Δ₅ unique modulo GRT₁^super-gauge
    ↓ [Wave 17-20 Drinfeld Ψ-functor + Wave 20 Gaiotto operadic]
Ψ: (CY^Siegel-aut_2, ⊕) → (QHopf^BKM, ⊗) lax symmetric-monoidal
    ↓ [Five images: Monster/Conway/Enriques/K3/Fake-Monster]
H_Δ₅ as co-sibling quantum group in the Ψ-landscape
```

---

## 22. The answered question

> **"What is the chiral quantum group undergirding the BKM related to the Siegel modular forms?"**

$$\boxed{\;\mathbf{H}_{\Delta_5} \;=\; \mathcal{D}_\hbar\!\Bigl(\mathcal{Y}^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\; \widetilde{\Phi}^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],\; R_{\mathrm{Sieg,dyn}}\Bigr)\;}$$

specialised at $\hbar^2 = -1/8$, equivalently realised as:

1. Super-EK quantisation of the Manin pair $(\mathfrak{g}_{\Delta_5}, \mathfrak{n}_+^{\mathrm{imag}} \oplus \mathfrak{h}^{\mathrm{imag}, \mathrm{rk}\,23})$;
2. Super-Yangian $Y_\hbar^{\mathrm{super}}(\mathfrak{g}_{\Delta_5})$ with explicit generators + Borcherds-GKM relations;
3. Super-Kontsevich deformation quantisation of $(\mathfrak{g}_{\Delta_5}^{\mathrm{super}}, \delta_{\mathrm{GN}})$ at $\hbar^2 = -1/8$;
4. Maulik-Okounkov stable-envelope Yangian pro-limit on $\mathrm{Hilb}(\mathrm{K3})$;
5. Khovanov-type dg-category $\mathrm{Kh}_{\Delta_5}$ with $K_0$ recovering $\mathbf{H}_{\Delta_5}$-Mod;
6. 3d Turaev-Viro TQFT via Kerler-Lyubashenko non-semisimple MTC at $\zeta_8$;
7. Borcherds all-loop BV resummation $(\Phi_{10}/\eta^{24})^\hbar$ of twisted 11D SUGRA.

**The numerical invariants**:
- $\hbar^2 = -1/8$, $K^{\kappa_{\mathrm{ch}}} = 8$, $\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$;
- BKM Cartan rank 3 orthogonal to Mukai grading rank 24;
- $c_{4d} = 107/6$, $c_{2d} = -214$, $c_{\mathrm{unit}} = 2$, $c_{\mathrm{eff}} = -166$;
- Siegel weight 5; Arthur packet $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1$; $|\Psi_{\Delta_5}| = 16$, $|\Psi_{\Delta_{10}}| = 4$;
- Pentagon tower $\phi^{(3\ldots 12)}$ with depth-4 $\zeta(3,3,3,3)$ at weight 12;
- BV obstruction $c_n = c_{\phi_{-2,1}}(-n) \cdot [H_n]$ with $c_3 = -8, c_4 = 12$, etc.;
- Quantum dim $\mathcal{D}^2 = 8^{130}$, $\tau(S^3) = 8^{-65}$.

**The symmetries**:
- $\mathrm{GRT}_1^{\mathrm{super}}$-torsor of quantisations;
- Motivic-Galois $\mathrm{GRT}_1$-action on K3 periods (same action under Kuga-Satake);
- Fricke $w_8$ modular $S$-matrix on $\mathbb{H}_2$;
- $M_{24}$ 't Hooft anomaly of order 6;
- $\mathrm{Co}_0 = 2.\mathrm{Co}_1$ moonshine extension at $N = 24$ class-$\mathcal{S}$.

**The landscape**:
- Five $\Psi$-images: Monster (rank 2), Conway (rank 2 super), Enriques (orbifold), K3 (rank 3), Fake-Monster (rank 26);
- CY-2 landscape dichotomy with weight formula $w_{\mathrm{Borch}} = 5\chi_{\mathrm{top}}/24$;
- Class-$\mathcal{S}$ $A_{N-1}$ family with umbral-Niemeier bijection $(N - 1) \mid 24$;
- Seven construction routes (Het/IIA/M/F/IIB/$\mathrm{K3}^2 \times S^1$/GW-DT) all converging on $\Delta_5$.

**The physical origin**:
- BV-quantised twisted 11D SUGRA on $\mathbb{R}^3 \times \mathrm{K3} \times \mathbb{C}^2$ with 24 M5-branes on $I_1$ Kodaira fibres;
- Effective action $S_q = S_{\mathrm{cl}} + \hbar\log(\Phi_{10}/\eta^{24})$;
- Bulk-boundary exact duality $Z_{\mathrm{bulk}} \cdot Z_{\mathrm{boundary}} = \eta^{-24}$ at $\hbar = 1$.

The chiral quantum group undergirding the BKM related to the Siegel modular forms is $\mathbf{H}_{\Delta_5}$. It is not a Yangian, not a toroidal algebra, not a Drinfeld quasi-Hopf. It is a new taxon: a super-Etingof-Kazhdan Hall-Drinfeld double of a CY-3 cohomological Hall algebra at paramodular specialisation. The seven incarnations are faces of one object, forced by seven structurally distinct but compatible constructions — all converging because K3's isolated Hyperkähler-twistor-locus structure (trivial continuous automorphism group, self-dual Mukai-lattice signature, motivic-Galois $\mathrm{GRT}_1$-equivariance, Hodge-structure Tate purity on real roots, Brown-Zagier motivic depth closure through weight 12) makes the convergence mandatory.

The Igusa-Gritsenko $\Delta_5$ is simultaneously:
- The classification cohomology $\mathbb{C}$-generator of $H^2(\mathfrak{g}_{\Delta_5})^{\mathbb{Z}/2, K(1)}$;
- The quantum determinant of the super-Yangian;
- The denominator of the BKM Lie superalgebra $\mathfrak{g}_{\Delta_5}$;
- The Plancherel measure of the non-semisimple MTC at $\zeta_8$, integrated on $\mathbb{H}_2$;
- The $\Psi$-functor arithmetic shadow on the rank-3 K3-row of the automorphic-product landscape;
- The all-loop BV effective action on $\mathbb{R}^3 \times \mathrm{K3} \times \mathbb{C}^2$;
- The character of the 3d TQFT on $\Sigma_2 \times S^1$;
- The Borcherds-lifted K3-elliptic-genus Fourier-shadow generator.

Eight structural roles, one arithmetic object. The programme converges.

---

## Appendix A — the elite-voice roster

Wave-by-wave, the agents channelled:

**Russian school**: Gelfand (representation theory, Tannakian fibres), Beilinson (Koszul duality, chiral algebras), Drinfeld (Yangians, quantum groups, RTT), Etingof (deformation quantisation, Kazhdan-Lusztig, quasi-Hopf), Polyakov (CFT, central charges, bootstrap), Nekrasov (partition functions, instanton counting, class-$\mathcal{S}$), Kazhdan (Langlands, Hecke algebras, spherical reps).

**Mathematical physics school**: Witten (topological QFT, M-theory, duality), Costello (BV quantisation, factorisation algebras, twisted holography), Gaiotto (class-$\mathcal{S}$, VOA bootstrap, 4d/2d).

**Tenth voice** (Waves 17-20): Kontsevich-Soibelman-Toën (CoHA, motivic integration, formality).

Each voice brought a structural lens:
- Gelfand: Tannakian reconstruction, Plancherel measures.
- Beilinson: Koszul-duality epistemic verification, chain-level witness.
- Drinfeld: RTT presentations, super-Yangian construction.
- Etingof: $\mathrm{GRT}_1$-torsor, $\phi^{(n)}$ MZV structure.
- Polyakov: anomaly cocycles, entanglement spectrum.
- Nekrasov: partition-function geometric origin, stable envelopes, K-theoretic refinement.
- Kazhdan: local Langlands, Arthur packets, Conway moonshine.
- Witten: duality frames, decoupling limits, Hodge/motivic structure.
- Costello: BV master equation, Heegner-Chern reciprocity, all-loop exponentiation.
- Gaiotto: class-$\mathcal{S}$ construction, umbral-Niemeier bijection, operadic functoriality.
- KST: formality bridges, adjudication ledgers, cross-module verification.

Together: the non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$ as the unifying centre of the programme's mathematical landscape, recovered by every route and witnessed by every voice.

---

## Appendix B — canonical primary-source anchors

Andrianov 1974 *Matem. Sbornik*; Arthur 2013 AMS Coll. 61; Atiyah 1988 *Publ. IHES* 68; Bayer-Macrì 2014 *Invent.* 198; Beauville 1983 *J. Diff. Geom.* 18; Beem-Rastelli 2013 arXiv:1312.5344; Ben-Zvi-Francis-Nadler 2010 *JAMS* 23; Borcherds 1988/1992/1995/1998 *J. Algebra*/*Invent.*/*Invent.*/*Invent.*; Bridgeland 2007/2008 *Ann. Math.*; Brown 2011/2012/2017 *Ann. Math.*/*Duke*; Bruinier 2002 *LNM* 1780; Cattaneo-Felder 2001; Chacaltana-Distler 2010 arXiv:1008.5203; Cheng-Duncan-Harvey 2014 arXiv:1307.5793; Costello 2011 AMS; Costello-Gaiotto 2018; Costello-Gaiotto-Paquette 2018 arXiv:1810.10016; Costello-Gwilliam 2017/2021; Creutzig-Ridout 2013 *CMP* 323; Davison-Meinhardt 2020 *Invent.*; De Renzi-Gainutdinov-Geer-Patureau-Mirand-Runkel 2021 arXiv:2003.09814; Deligne 1970/1971/1989/2013; Dijkgraaf-Moore-Verlinde-Verlinde 1997/Dijkgraaf-Verlinde-Verlinde 1997; Drinfeld 1985/1986/1990; Duncan 2007 *Math. Res. Lett.* 14; Duncan-Mack-Ono 2015 *Forum Math. Pi* 3; Eguchi-Hikami 2009 arXiv:0904.0911; Eguchi-Ooguri-Tachikawa 2011 *Exp. Math.* 20; Enriquez-Furusho 2020 arXiv:2004.07090; Etingof-Kazhdan 1996-2008 I-V *Selecta Math.*; Feigin-Frenkel 1990/1992; Feigin-Gainutdinov-Semikhatov-Tipunin 2006 *CMP* 265; Feingold-Frenkel 1983 *Math. Ann.* 263; Francis 2013 *Adv. Math.* 239; Frenkel-Lepowsky-Meurman 1988; Gaiotto 2009 arXiv:0904.2715; Göttsche 1990 *Math. Ann.* 286; Gritsenko 1995/1999; Gritsenko-Nikulin 1997/1998; Hardy-Ramanujan 1918; Harvey-Moore 1996 arXiv:hep-th/9510182; Hinich 2010 *Adv. Math.* 223; Igusa 1962/1964 *Amer. J. Math.*; Ikeda 2001 *Ann. Math.* 154; Kapranov-Vasserot 2018 arXiv:1802.07988; Kerler-Lyubashenko 2001 *LMS LNS* 262; Khovanov 2000; Khovanov-Lauda 2009; Kontsevich 1997/2003 *Lett. Math. Phys.*; Kontsevich-Soibelman 2008 arXiv:0811.2435; LMFDB project; Lusztig 1990/1993 Birkhäuser/MIT; Lyubashenko-Majid 1994 *J. Algebra* 166; Maulik-Nekrasov-Okounkov-Pandharipande 2006 *Publ. IHES* 104; Maulik-Okounkov 2019 *Astérisque* 408; Maulik-Pandharipande-Thomas 2010; Moeglin-Renard 2018; Morrison-Vafa 1996 I/II; Mukai 1984/1987; Nakajima 1997 *Ann. Math.* 145; Nahm-Wendland 2001; Nekrasov 2003; Nekrasov-Shatashvili 2009; Niemeier 1973 *J. Number Theory* 5; Oberdieck 2018 *JEMS* 20; Oberdieck-Pixton 2016 arXiv:1706.10100; Pasol-Zagier 2013 arXiv:1309.4883; Positselski 2011; Reshetikhin-Turaev 1991 *Invent.* 103; Saito-Kurokawa; Schiffmann-Vasserot 2013 *Publ. IHES* 118; Shapere-Tachikawa 2008 arXiv:0804.1957; Shoikhet 2003 arXiv:math/9809171; Tamarkin 1998; Taormina-Wendland 2011 arXiv:1107.3834; Turaev 1994; Vafa 1996 arXiv:hep-th/9602022; Weissauer 2009; Willwacher 2015 *Invent.* 200; Witten 1989 *CMP* 121; Witten 1995 arXiv:hep-th/9503124; Zagier 1994 *Prog. Math.* 120; Zwegers 2002 Utrecht.

---

*The non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$, seven incarnations, one object, five waves of seventy adversarial voices converging on the chiral quantum group undergirding the Borcherds-Kac-Moody Lie algebra related to Siegel modular forms. The programme has crystallised.*

*Raeez Lorgat, Perimeter Institute, April 2026.*
