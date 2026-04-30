# FRONTIER - Vol III Open Research Directions

## Frontier Synthesis

The CY-to-chiral frontier has five cross-sections: the CY-A/B/C/D/H framework, the universal Borcherds weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$, structural conjectures around the K3 Hall-Drinfeld/BKM lane, the compact 6d hCS problem, and cross-volume bridges to Booth--Lazarev and the iterated-Sugawara ladder. The document records mathematical state, corrected statements, and open proof obligations. It does not record project chronology.

Five single-sentence targets carry the frontier:

1. **Chain-level $\mathrm{Sp}^{\mathrm{ch}}_{K3, E}$ on $\mathrm{Ran}(E)$ closing the witnessed CY-A$_3$ stratum.** Write the factorisation-homology equation on $\mathrm{Ran}(E)$ that realises
   \[
   \mathrm{Sp}^{\mathrm{ch}}_{K3, E}(\Phi^{\mathrm{FA}}_3(K3 \times E))
   \simeq U^{\mathrm{ch}}(\mathfrak{heis}_{\mathrm{Muk}})
   \otimes U^{\mathrm{ch}}(\mathfrak{g}^{\mathrm{BPS}}_{K3})
   \]
   beyond a single reference curve, pulling back the K3-factor Maulik--Okounkov stable envelope through $\int_{K3} E_3 \simeq E_1$ along the global critical-chart hypothesis.

2. **Sharpened Lorgat 2020 Conjecture 1.** Promote the structural identification
   \[
   \mathrm{Sp}^{\mathrm{ch}}_{K3, E}(\Phi^{\mathrm{FA}}_3(\mathcal{F}_{K3 \times E}))
   \simeq \mathbf{H}_{\Delta_5}
   \]
   to a chiral-bialgebra isomorphism on $E$ with character $\Delta_5^{-2}$ and root multiplicities equal to $g_N$-twisted-twined K3 elliptic genera, with proof obligations at the twisted-dimension calculation, the corrected $c_{2d}$ value, Oberdieck--Pixton beyond primitive $N=1$ K3 classes, the BKM-denominator comparison beyond Clery--Gritsenko automorphy, and the proof of $H^3(\widetilde{M}_{24}, U(1)) = \mathbb{Z}/12 \oplus \mathbb{Z}/2$.

3. **Booth--Lazarev chiral instantiation for Vol I/III concordance.** Instantiate the Booth--Lazarev curved $A_\infty$ Quillen equivalence in the chiral lane on $\overline{M}_{g, n}$ at compact CY$_d$ with $\kappa_{\mathrm{ch}} \neq 0$, closing the Vol I $\mathsf{B}$-row $K^{\kappa_{\mathrm{ch}}} = 8$ through the $\mathcal{B}$-family Heisenberg on $K3 \times E$.

4. **Explicit Fake Monster $\Phi^{\mathrm{FA}}_5$ on $K3 \times K3 \times E$ yielding $\kappa_{\mathrm{BKM}}(\Phi_{\mathrm{FM}}) = 12$.** Construct the chain-level $\Phi^{\mathrm{FA}}_5$-image on $K3 \times K3 \times E$ realising the $E_5$-Poisson bracket on the degree-$(4,20)$ sublattice of $\widetilde H^*(K3 \times K3) \oplus H^1(E)$ that hosts the rank-$24$ Leech lattice.

5. **Non-abelian $\mathrm{Obs}^{\mathrm{q}, E}_{\mathrm{hCS}}(K3 \times E, \mathfrak{g}) \simeq \mathfrak{g}_{\Delta_5}$.** Compute the non-abelian Costello--Gwilliam quantum-observable pushforward of 6d hCS on $K3 \times E$ along the $E$-projection and identify it with the Lorgat--Gritsenko GKM superalgebra $\mathfrak{g}_{\Delta_5}$ as a chiral algebra on $E$.

These five targets are read against the spine below: target (1) belongs to the two-stage factorisation of $\Phi_d$; target (2) belongs to the 8-row Gritsenko--Clery catalogue at $N=1$, sharpened to bialgebra level; target (3) carries the Vol I $\mathsf{B}$-row bridge; target (4) extends the dimension-stratified sibling catalogue at the Fake Monster row; target (5) is the compact 6d hCS route to the K3 Hall-Drinfeld/BKM object.

---

## Programme Spine

### Two-stage factorisation of $\Phi_d$

\[
\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d .
\]

Stage 1 $\Phi^{\mathrm{FA}}_d \colon \mathrm{CY}\text{-cat}_d \to \mathrm{FA}^{E_d}(X)$ is canonical: Kontsevich--Tamarkin $E_d$-formality on the holomorphic factor and Costello--Gwilliam--Li locality produce an $E_d$-holomorphic factorisation algebra on the CY target $X$. Stage 2 $\mathrm{Sp}_{\Sigma_{d-1}, C} = \int_{\Sigma_{d-1}}$ is factorisation-homology specialisation along a $(d-1)$-dimensional slicing $\Sigma_{d-1}$ through $X$, landing on a chiral algebra on a curve $C$. Stage 2 is specialisation, not inversion: different $(\Sigma_{d-1}, C)$ choices for a single CY$_d$ category produce different $E_1$-chiral shadows.

For $d \geq 3$, the algebra $A$ on the chiral side is $E_1$. The $E_2$ structure lives on the centre, double, or representation category under named hypotheses. Any statement placing $E_2$ directly on $A$ at $d \geq 3$ must be replaced by this centre/double formulation.

### Universal positive-geometry grammar

\[
Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W),
\qquad
G(X) = D(Y^+(X)).
\]

The grammar covers CoHA on $\mathbb{C}^3$ and the resolved conifold, Nakajima stable envelopes on local $\mathbb{P}^2$, orbifold inertia $I(X/G)$ for Mathieu and McKay loci, and lattice-polarised period half-spaces for Borcherds lifts. The precise equivariant cohomology is fixed by the stratum: toric $T^d$; reduced $\mathbb{C}^\times+\mathrm{Aut}(X)$; orbifold inertia; or lattice-polarised period domain.

The toric affine space identity is
\[
\mathrm{CoHA}(\mathbb{C}^3) = Y^+.
\]
The full $\mathcal{W}_{1+\infty}$ object belongs to the double/dual side, not to the positive half $Y^+$.

The Maulik--Okounkov $R$-matrix reads as a gluing-cocycle residue across chamber walls:
\[
R^{MO}(u) = \mathrm{Res}_{u = u_\star}\phi^+_{\mathrm{UV}}(u).
\]
The Yang--Baxter plus unitarity axiom is the cocycle condition for $\phi^+_{\mathrm{UV}}$.

### Gritsenko--Clery catalogue and $\kappa_\bullet$ discipline

The universal Borcherds identity is
\[
\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2.
\]
For the eight Gritsenko--Clery forms, the weights are $(5,2,3,1,2,1/2,3/2,1)$ and the Fourier constants are $c_N(0) \in \{10,4,6,2,4,1,3,2\}$, so $\kappa_{\mathrm{BKM}} \in \{5,2,3,1,2,1/2,3/2,1\}$ row by row. The catalogue has no weight-$0$ row and no quarter-weight row.

For $K3 \times E$, the spectrum $\{0,3,5,24\}$ comes from four distinct constructions:

- $\kappa_{\mathrm{cat}}(K3 \times E)=0$, the compact total-space categorical trace.
- $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3$, the Heisenberg-Cartan Stage-2 shadow.
- $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5})=5$, the Borcherds weight.
- $\kappa_{\mathrm{fiber}}=24$, the Mukai-lattice rank of the K3 fibre.

The K3 fibre value $\chi(\mathcal O_{K3})=2$ is a fibre witness, not the total-space entry. The formula $\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})$ is false on the CHL rows; the corrected formula is $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$.

### Compact CY$_3$ and CY-A$_3$

The compact CY-A$_3$ functorial theorem is not unconditional for every smooth proper non-formal CY$_3$. The infinity-categorical obstruction analysis removes one obstruction after the data are fixed, and coefficient convergence gives a finite-cover analytic estimate. The chain-level compact closure remains conditional on a corrected TCFT package: an $E_3$-formality point, an $A_\infty$-compatible $S^3$-framing homotopy on $HC^-_3(C)$, anomaly cancellation, analytic completion, and an admissible Stage-2 specialisation.

For compact CY$_3$, the total-space value
\[
\kappa_{\mathrm{ch}}(A_X)=\sum_q(-1)^q h^{0,q}(X)=0
\]
by Serre duality. Thus $K3 \times E$ has total-space $\kappa_{\mathrm{ch}}=0$; the numbers $2$, $3$, and $24$ near this geometry are fibre, Stage-2/Heisenberg-Cartan, or Mukai-rank data.

### K3 Hall-Drinfeld/BKM object

The BKM-side K3 object is the K3 chiral Hall-Drinfeld double $\mathbf{H}_{\Delta_5}$. It is separate from the Mukai self-mirror Yangian branch. The BKM lane carries the bi-based Ran/$\overline{\mathcal A_2}$ architecture, CY-2 $[2]$ shift, class-$\mathcal S$ parent $\mathcal T[A_1,\Sigma_{0,24}]$, and $\Delta_5$ as a one-loop output. The Yangian lane carries the Mukai form, the abelian K3 presentation, and the orthogonal target $Y_\hbar(\mathfrak{so}(4,20))$, with a possible non-Kac Hodge-parity refinement $Y_\hbar(\mathfrak{so}(4|20))$.

At Lie/Hopf level, the K3 Hall-Drinfeld presentation is abelian up to the 24 Heisenberg/Miki copies. Non-abelian BKM structure enters after vertex-operator closure on the K3 Fock module.

### 6d hCS and the all-orders 5d theorem

$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{hCS}_6}$ is an $E_3$-algebra on $\mathbb{C}^3$: the Bochner--Martinelli propagator and shuffle sums realise the $E_3$ product, and the BV anomaly vanishes on $\mathbb{C}^3$ and on the K3-fibred loci under the named compactness hypotheses. Non-abelian 5d holomorphic Chern--Simons on $\mathbb{R}\times\mathbb{C}^2$ for simply-laced $\mathfrak g$ quantises to the affine Yangian VOA $Y_\hbar(\widehat{\mathfrak g})$ to all orders in $\hbar$. Non-simply-laced types require a twisted Yangian construction.

### Three-tier hierarchy on the seven faces of $r_{\mathrm{CY}}$

Every face of $r_{\mathrm{CY}}$ belongs to one of three tiers:

1. CY-datum intrinsics: Mukai pairing, Hodge supertrace, categorical Euler $\kappa_{\mathrm{cat}}$.
2. Stage-1 invariants of $\Phi^{\mathrm{FA}}_d$: $\kappa_{\mathrm{ch}}$, $E_d$-centre, Kontsevich--Tamarkin formality class.
3. $(\Sigma_2,C)$ specialisations: $\kappa_{\mathrm{BKM}}$ at the chosen Siegel cusp, Maulik--Okounkov residue, Borcherds lift.

The three-factor trace identity on the CHL scope $N \in \{1,2,3,4,6\}$ is
\[
\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2)
= \mathrm{tr}_{\mathrm{Pentagon}}
= \omega_{\mathrm{Borcherds}}
= c_N(0)/2.
\]
The CHL row values are $\{5,4,3,2,1\}$ and are distinct from the eight-form Gritsenko--Clery list $\{5,2,3,1,2,1/2,3/2,1\}$.

### Dimension-stratified sibling catalogue

Monster $\mathbb M$ from $V^\natural$ and Igusa $\Phi_{10}$ via Gritsenko--Nikulin are the $d=3$ siblings of a universal construction. Borcherds' Fake Monster Lie algebra on $\mathrm{II}_{25,1}$ is the $d=5$ sibling; the rank-$24$ obstruction forces dimension $5$ rather than dimension $3$. The $d=4$ bridge is the Conway/Leech lattice datum. The catalogue is ordered by dimension rather than moonshine narrative.

### Corrected statements

1. $\widehat{\mathfrak{sl}_3}$ Gaiotto shadow is replaced by the $F_3$ Feingold--Frenkel real-root subalgebra of $\mathfrak{g}_{\Delta_5}$.
2. $L_{-6}(\mathfrak e_8)$ for $V_{24}$ is replaced by $V_{24}=H^0_{\mathrm{DS}}(L_{-2+1/22}(\mathfrak{sl}_2)^{\otimes 22})$.
3. $\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})$ is replaced by $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$.
4. Fake Monster at $d=3$ is replaced by the $d=5$ Fake Monster row.
5. The direct $\chi_{V_{24}}$ match is replaced by the Heisenberg--Mukai $\eta^{-48}$ identity.
6. The Gaiotto curve $\Sigma_{2,0}$ is replaced by $\Sigma_{0,24}$.
7. Native $E_n$-chiral output on a curve is replaced by the two-stage factorisation with Stage-2 specialisation.
8. A shifted-symplectic table ending at $d=4$ is replaced by a table containing the $d=5$ Poisson-$E_5$ row.
9. Uniform $H^3$-vanishing for $\widetilde M_{24}$ is replaced by class-dependent cohomology: 2A carries $\mathbb Z/2$, and 2B carries $\mathbb Z/4$.

---

## Open Frontier Register

### Core CY-to-chiral problems

**V3-F13. $E_1$-chiral bialgebra axiom completeness.** The remaining axiom work is H3 for composite channels at spin $s\geq4$, H3 entrywise for noncommutative RTT in $Y(\mathfrak{sl}_N)^{\mathrm{ch}}$ at $\hbar^2$, H5 for non-connected Yangians at $z\neq0$, and the single categorical proposition that $(Y(\mathfrak g)^{\mathrm{ch}},\mu,\Delta_z,\epsilon,\eta,S)$ satisfies (H1)-(H5).

**V3-F14. Zamolodchikov tetrahedron correction.** The explicit rational $T_{ijk}$ correction exists on the charge-2 surface. The charge-3 obstruction is the four-dimensional $\binom{4}{3}$ sector of $V^{\otimes4}$, where the current one-dimensional kernel correction does not close the equation. The missing theorem is the bridge from the ZTE obstruction at $O(\hbar^2)$ to the $A_\infty$ coproduct correction $\delta^{(3)}$.

**V3-F15. Universal coproduct residue.** The Miura cross-term formula proves the all-spin universal statement. The remaining finite task is entrywise $Y(\mathfrak{sl}_N)$ RTT verification at $\hbar^2$ using Molev's formulas. This is compute support for the theorem, not a new frontier theorem.

**V3-F16. Kummer collar transport.** Kummer steps through the excision surface reduce the problem to chain-level transport of the commutator pairing to the Mukai form of signature $(4,20)$. The open computation is the quadratic-form identification via collar-pairing, lattice-VOA transport, or the trace constraint for $\kappa_{\mathrm{ch}}$ on the K3 surface.

**V3-F17. $A_\infty$ coproduct and shadow tower.** The proved direction gives $\Delta^{A_\infty}=\Delta^{\mathrm{Yangian}}+\sum_{k\geq3}\hbar^{k-1}\delta^{(k)}$ with coefficients governed by shadow invariants. The missing theorem is the ZTE-to-$\delta^{(k)}$ bridge. The nontrivial biconditional is: $\Delta^{A_\infty}$ truncates after $\delta^{(2)}$ exactly when the shadow depth is finite on the relevant class. The class-L counterexample shows that shadow-tower truncation alone is weaker.

**V3-F18. CY-A$_3$ chain-level compact closure.** The compact non-formal CY$_3$ problem remains conditional outside witnessed loci. The Fermat quintic gives a tractable test locus, but the number $204$ is the Hodge-diamond total $1+101+101+1$, not a $\mathbb{Z}_5^5$-invariant-sector dimension. A proof must supply the TCFT/framing/anomaly/completion witnesses listed in the spine.

**V3-F19. K3 Hall-Drinfeld double and Mukai Yangian split.** The BKM branch is $\mathbf H_{\Delta_5}$, not a Yangian under another name. The Mukai branch has abelian Yangian data and the candidate orthogonal target $Y_\hbar(\mathfrak{so}(4,20))$. The open work is real-root completion, comparison with the BKM denominator, and reverse Tannakian reconstruction for $D^b(\mathrm{Coh}(K3))$.

**V3-F20. Mode-level Drinfeld centre.** The categorified centre statement is proved in the standard Lie landscape. The remaining mode-level problem compares $Z(U_A)$ with $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ under three obstructions: pointwise reduction for class $\mathbf M$, $A^!$ factorisation on the Ran space for classes $\mathbf C/\mathbf M$, and RHom compatibility beyond class $\mathbf G$.

**V3-F20h. Centre-hocolim obstruction for $K3\times E$.** More than 92 percent of the global Drinfeld centre is invisible to local chart data in the computed levels. Maulik--Okounkov stable envelopes bypass the obstruction globally. The open work is charge $\geq3$, a Verlinde-type formula for charge-graded dimensions, and the Mittag--Leffler condition for the inverse system $\{Z_N\}$.

**V3-F21. $\mathrm{Sp}_4(\mathbb Z)$ modularity.** The non-factorisation-homology ingredients are classical: $\Phi_{10}$ as the $K3\times E$ BKM denominator, the mapping-class quotient to $\mathrm{Sp}_4(\mathbb Z)$, and Humbert divisors. The remaining theorem identifies $\int_{\Sigma_2\times S^1}A_{K3\times E}$ with the Igusa/Borcherds tower and inherits the conditional CY-A$_3$ chain-level hypotheses.

**V3-F22. Class $\mathbf M$, logarithmic centres, and mock modularity.** Huang's logarithmic tensor category theorem together with EGNO gives the class-$\mathbf M$ logarithmic-centre implication under the required finiteness hypotheses. Mock modularity is a separate spectral-decomposition condition, present for K3 and open for $K3\times E$ and non-CY Monster/W$_N$ comparisons.

**V3-F23. Borcherds lift as resummation.** The perturbative expansion in $\sigma_3=h_1h_2h_3$ reproduces the Fourier--Jacobi expansion of $\Delta_5$. Additive Saito--Kurokawa data give the perturbative side, and the Borcherds product gives the non-perturbative side. The open statement is a Stokes automorphism controlled by BKM imaginary root multiplicities.

**V3-F24. Non-abelian chiral quantum group at $E_3$.** The shuffle-algebra half reduces to Miki, Schiffmann--Vasserot, and Feigin--Hashizume technology. The open half is the two-parameter Kazhdan--Lusztig equivalence
\[
\mathrm{Rep}_{q,t}(U_{q,t}(\widehat{\widehat{\mathfrak{sl}_2}}))
\simeq \mathcal O_{k,k'}(\widehat{\widehat{\mathfrak{sl}_2}}).
\]
Exceptional BCFG types are obstructed by the absence of the relevant CY$_3$ orbifold source.

**V3-F25. Class $\mathbf M$ Borel summability and imaginary roots.** K3 Borel summability is supported by the K3 mock-modular theorem and the class-$\mathbf M$ Borel engine. The $K3\times E$ and non-K3 compact CY$_3$ cases remain conditional on CY-A$_3$. The W$(p)$ triplet family is logarithmic class $\mathbf M$, distinct from the K3 mock-modular mechanism.

**V3-F26. Orthogonal K3 Yangian.** The Mukai form fixes the ungraded target $Y_\hbar(\mathfrak{so}(4,20))$. The possible $4|20$ Hodge-parity refinement is non-Kac because both pieces inherit symmetric forms. The open construction is the rank-$(4,20)$ reflection-equation Shapovalov datum and its comparison with the Borcherds denominator.

**V3-F27. 6d hCS and K3 quantum toroidal.** The 5d Costello pipeline is verified through low charge. The $\mathbb C^3$ BV--BRST hCS avatar and the resolved-conifold two-chart descent are now constructed at classical/finite-Rees level, with an anomaly-free perturbative quantum lift on the resolved conifold. The compact $K3\times E$ Hall double and the K3 quantum-toroidal case remain gated on reduced compact Hall data, negative-half/pairing/radical recognition, and CY-A$_3$ chain-level input. The Miki $S_3$ torus-Weyl statement has no K3 torus-action input; only the elliptic-factor $\mathrm{SL}_2(\mathbb Z)$ survives.

### Secondary frontiers and cross-volume residues

**V3-F1. BV/BRST equals bar in the coderived category.** The genus-0 and genus-1 class $\mathbf G/\mathbf L/\mathbf C$ cases are proved, and the coderived identification covers class $\mathbf M$. The open problem is genus $\geq2$ class $\mathbf M$, where the full period matrix enters, and the physical selection principle for $D^{\mathrm{co}}$ over $D^b$.

**V3-F2. Non-principal Drinfeld--Sokolov reduction.** The first genuinely non-abelian nilpotent test is the $(3,2)$ partition in $\mathfrak{sl}_5$. The BRST ghost-ghost terms obstruct the abelian Kazhdan-filtration argument. A successful $E_1$ degeneration would cover all two-step type-A nilpotents; a failure would identify the obstruction.

**V3-F3. Genus-5 cross-channel computation.** The $W_3$ cross-channel values at genera $2,3,4$ do not determine the Gevrey shift. The genus-5 graph computation determines the cross-channel instanton action $A_{\mathrm{cross}}$, denominator support, and positivity pattern.

**V3-F4. Admissible $\mathfrak{sl}_3$ Koszulness.** The universal algebra is Koszul, and the simple $\mathfrak{sl}_2$ quotient is Koszul at admissible levels. The $\mathfrak{sl}_3$ quotient has multi-weight null vectors, so the Li-bar $E_2$ page at $k=-3/2$ is the first decisive computation.

**V3-F5. Restricted DK-4.** The evaluation-generated core satisfies the pointwise data. The missing step is the filtered-complete dg Lie identification between the abstract tangent Lie algebra and the dg-shifted Yangian.

**V3-F6. DK-5 categorical $E_1$ primacy.** The bridge criterion reduces the problem to full O-Koszulness beyond the evaluation core, tower completion with algebraic identification, and comparison with Latyntsev's spectral quantum group.

**V3-F7. Modular cumulant completion.** The two subproblems are cumulant recognition for the resonance-graded associated graded of the completed bar coalgebra and the jet principle extracting the Yangian $r$-matrix from reduced-weight windows.

**V3-F8. Analytic realisation.** Heisenberg and lattice sewing are established. The open layers are interacting sewing envelopes, conformally flat two-disk algebras with anomaly cancellation, and higher-genus coderived shadows.

**V3-F9. $E_1$ Verdier duality on ordered configurations.** Verdier/Ran duality controls the closed colour. The ordered bar lives on ordered configuration spaces, where the correct analogue is opposite-duality $B^{\mathrm{ord}}(A^{\mathrm{op}})=B^{\mathrm{ord}}(A)^{\mathrm{cop}}$. A ribbon Ran space or Verdier theory on ordered configurations would make the comparison intrinsic.

**V3-F10. Resurgence from genus 5.** The scalar instanton action is $(2\pi)^2$. The cross-channel action comes from multi-weight OPE structure and is bounded by the first three data points. The genus-5 computation fixes it.

**V3-F11. Cross-channel generating function.** No A-hat-type closed generating function is known for $\delta F_g^{\mathrm{cross}}$. A candidate must be bivariate in the central charge and $\hbar$, with inhomogeneous scaling and irreducible numerators.

**V3-F12. Scalar saturation beyond algebraic families.** Layer 1 holds for algebraic families with rational OPE coefficients, and the uniform-weight lane has scalar genus towers. Multi-weight families fail at genus $\geq2$. The open test families are non-GKO cosets, 4d $\mathcal N=2$ quiver VOAs, and admissible simple quotients in rank $\geq2$.

**V3-F28. Derived Satake for CY.** The $\mathbb C^3$ lane has Maulik--Okounkov charge-2 and Fock-dimension evidence, but the derived Satake equivalence remains conjectural. The K3 lane passes through the Hall-Drinfeld/BKM and Mukai-Yangian split.

**V3-F29. Tropical and cluster CY.** The residual content belongs to the upper-semicontinuity problem for shadow class over tropical or wall-crossing degenerations, with Gross--Siebert, GHKK, and Bridgeland as the appropriate comparison sources.

**V3-F30. Chiral Verlinde.** The class-stratified Verlinde polynomial family is assembled in Vol I and Vol III. The remaining Vol III problem is the chiral $S$-matrix for the root-of-unity truncation of $\Phi(K3\times E)$.

**V3-F31. Hitchin quantisation.** The SL$_2$, genus-2 case is accessible through Beilinson--Drinfeld, the Feigin--Frenkel centre, and the K3 abelian Yangian. The residual problem is the general ADE oper/Yangian Hamiltonian comparison.

**V3-F32. False-theta versus mock-modular mechanisms.** Bringmann--Lovejoy--Mahlburg--Rolen and Beem--Lemos--Liendo--Peelaers--Rastelli are distinct comparison families. W$(p)$ triplets are logarithmic/false-theta or quantum-modular examples; they are not K3 mock-modular examples.

**V3-F33. $p$-adic Langlands CY.** The K3 $d=2$ Fermat lane is accessible through Livne, Kuga--Satake, and the existing $p$-adic K3 engine. The rigid CY$_3$ quintic lane is conditional on CY-A$_3$ and is separate from Bernoulli/Kummer localisation.

**V3-F34. BFN Coulomb.** The ADE case is assembled from Braverman--Finkelberg--Nakajima, Nakajima--Takayama, and Webster. The frontier is non-quiver Coulomb branches for generic K3 and duplicate-label hygiene in the manuscript.

**V3-F35. Higher-genus chiral form factors.** Genus $0$ is covered by Vol II UCH and Vol III truncation by class. The open directions are $g\geq1$ punctured surfaces and a Smirnov/Babujian--Karowski axiom system for $\Phi(\mathrm{CY}_d)$.

**V3-F36. FH McKay naturality.** This is the same mathematical problem as V3-F16: Mukai-pairing collar transport and naturality for the ADE $d=2$ route. Generic orbifold and conifold phrasing should be replaced by the ADE scope.

**V3-F37. Mathieu moonshine.** Gannon and Eguchi--Ooguri--Tachikawa provide the moonshine theorem. The frame-shape equals twined-bar-Euler identity is cyclotomic. The remaining geometric problem is the sigma-model $M_{24}$ action for the non-surfing classes $\{7A,7B,15A,15B\}$, downstream of the K3 Yangian construction.
