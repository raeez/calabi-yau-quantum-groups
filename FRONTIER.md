# FRONTIER — Vol III Open Research Directions

This file lists the open research frontiers of Vol III under the three-axis (level / chart / ambient) scope discipline. Each frontier carries explicit coordinates, a hypothesis package, a target reconstruction theorem, and a heal path. The reader-facing inscription lives in `chapters/frontier/open_frontiers.tex` (Chapter `ch:open-frontiers`); the operating discipline is named in `chapters/frontier/scope_discipline_remark.tex` and detailed in `appendices/three_axis_scope_discipline.tex` (`app:three-axis-scope-discipline`). This document is the bookkeeping mirror.

## Operating discipline

> Every theorem in the programme declares its $(\text{level}, \text{chart}, \text{ambient})$ coordinates. Promotion across coordinates requires the named comparison arrow, constructed under the named hypotheses. No claim is permitted to be promoted from one coordinate to another by elision.

The vertical axis is the universal arrow with five levels: 0 primitive (CY$_d$-categories), 1 Stage-1 native ($\Phi^{\mathrm{FA}}_d$), 2 Stage-2 chart shadow ($\Phi^{(\Sigma_{d-1}, C)}_d$), 3 centre ($Z^{\mathrm{der}}_{\mathrm{ch}}$, $Y^+(X)$, $G(X)$), 4 scalar ($\kappa_{\mathrm{BKM}}$). The horizontal axis is the chart datum (equivariance stratum × $(\Sigma_{d-1}, C)$ × boundary vacuum × admissibility window). The ambient axis names the depth context (ordinary / weight-completed / pro / J-adic / HS-sewing / formal-local / global-with-descent / derived $\infty$-categorical).

The chain-level lane and the $(\infty, 1)$-categorical lane are equally load-bearing. State each theorem in the lane in which its proof actually works.

## Open frontiers

### F1. Chain fusion conjecture in general $d$

- **Coordinates.** Level 2 (Stage-2 chiral algebra equals open-side boundary algebra). Chart $(\Sigma_{d-1}, C, b, \mathrm{adm})$. Ambient: chain-level on verified loci; $(\infty, 1)$-categorical for the general statement.
- **Reconstruction theorem.** $A_X = \Phi^{(\Sigma_{d-1}, C)}_d(\mathcal{C}_X) = A_{b(X, \Sigma, C)}$ for canonical boundary vacuum $b(X, \Sigma, C)$ in an open factorisation dg-category on $(C, D_C, \tau_C)$.
- **Verified loci.** $\mathbb{C}^3$, local $\mathbb{P}^2$, resolved conifold, $K3 \times E$.
- **Heal path.** Boundary-vacuum existence stratum-by-stratum (toric / reduced+Aut / orbifold inertia / lattice-polarised); Stage-2 = boundary algebra via swiss-cheese pair; CY-A$_3$ chain-level closure feeds compact non-toric.
- **Residue.** Compact non-toric without global Lagrangian boundary brane is unresolved.

### F2. $G(X) = D(Y^+(X))$ for compact non-toric CY$_3$

- **Coordinates.** Level 3 (positive half $\to$ Drinfeld double). Chart: compact non-toric reduced $\mathbb{C}^\times +$ Aut or lattice-polarised. Ambient: chain-level with inverse-limit / pro-completion.
- **Reconstruction theorem.** $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$ exists chain-level; $G(X) = D(Y^+(X))$ is Hopf; $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X) \simeq \mathfrak{z}(G(X))$.
- **Verified loci.** Toric ($\mathbb{C}^3$, local $\mathbb{P}^2$, conifold), orbifold inertia $\mathbb{C}^3 / \Gamma$ (Bridgeland--King--Reid).
- **Seven gates.** Compact critical CoHA, Hall--Drinfeld doubling, radical descent, PBW with no extra relations, parity, Green-adjoint coproduct, primitive-centre reduction, associator cohomology, completion / inverse-limit Mittag--Leffler, Heegner comparison.
- **Heal path.** Fermat quintic $\mathbb{Z}_5^5$-equivariant test family; Heegner-comparison gate as cleanest single criterion; stage from $K3 \times E$ via Schoen elliptic fibration.
- **Residue.** Mittag--Leffler at compactness gate is the deepest; $K3 \times E$ centre-hocolim obstruction (>92% of global Drinfeld centre invisible to local chart data) suggests global Maulik--Okounkov stable-envelope data required.

### F3. $W_\infty[\lambda] \Rightarrow E_\infty$ outside the admissible window

- **Coordinates.** Level 3 endpoint at $\lambda$-chart. Ambient: four-condition admissibility window.
- **Reconstruction theorem (target).** Identify the obstruction (which condition fails) and the next admissible window outside Pro\v{c}\'azka / Creutzig--Kanade--Linshaw / Pope--Romans--Shen / Yamada.
- **Verified subwindow.** Spin $\leq 8$ Pope--Romans--Shen quadratic.
- **Heal path.** Yamada full weight spectrum; Costello--Gaiotto holomorphic factor past spin 8; sharp $W_\infty$-cohomological obstruction at window boundary.
- **Residue.** Chain-level statement in ordinary complexes (versus weight-completed) is open and may genuinely fail; $E_\infty$-convention equivalences (operadic / simplicial) must be named.

### F4. Modularity compatibility under chain fusion

- **Coordinates.** Level 4 (scalar) versus level 3 (operator algebra) under chain fusion at level 2. Chart: $\Phi_N$ (CY-side) and clutching torus (open-side). Ambient: HS-sewing (open) / period-domain (CY).
- **Reconstruction theorem (target).** Open-side trace + clutching scalar at level 4 equals CY-side $\kappa_{\mathrm{BKM}}(\Phi_N)$ for matching chart input.
- **Verified loci.** $K3 \times E$ at $\Delta_5$ (BKM weight 5 = K3 elliptic genus open-side); Borcherds Monster at $d = 3$.
- **Heal path.** Identify open-side modular trace as bulk-side scalar via swiss-cheese pair; apply Borcherds-product identity; reduce to Petersson pairing between Igusa form (CY-side) and Borcherds-lifted Jacobi form (open-side).
- **Residue.** Orientation gerbe sign on open-side and Borcherds-product sign on CY-side must be matched chart-by-chart; CHL ladder $N \in \{1, 2, 3, 4, 6\}$ signs determined by $\varphi(N) \mid 2$.

### F5. Universal Borcherds-weight identity as fusion consequence

- **Coordinates.** Level 4 from level 3 via trace pairing on chiral centre. Chart: $\Phi_N$. Ambient: chain-level / pro-completion.
- **Reconstruction theorem (target).** $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is the trace of an explicit operator on $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X)$ at chart $\Phi_N$.
- **Verified loci.** $\Delta_5$ at $K3 \times E$ (trace of Cartan generator = 5); $\Phi_{12}$ at $K3 \times K3 \times E$ (trace = 12).
- **Heal path.** Construct $Z^{\mathrm{der}}_{\mathrm{ch}}(A_X)$ on four equivariance strata; compute Cartan trace via equivariant cohomology of $Y^+(X)$; Bruinier Heegner Chern-class reciprocity for lattice-polarised case.
- **Residue.** Universal Borcherds-weight identity may be level-4-internal (Borcherds 1995, Gritsenko 1999), independent of chain fusion. The fusion-consequence statement is stronger; the level-4-internal identity is unconditional.

### F6. The $d \geq 4$ stratum

- **Coordinates.** Level 0--4 at $d \in \{4, 5\}$. Chart: PT$_4$ at $d = 4$; Fake Monster at $d = 5$. Ambient: $E_5$-Poisson at $d = 5$.
- **Reconstruction theorem (target).** Two-stage factorisation extends to $d = 4, 5$ with shift law forcing $E_0$ at $d = 4$ and $E_5$-Poisson at $d = 5$. Fake Monster $\mathfrak{g}_{\Phi_{12}}$ on $\mathrm{II}_{25, 1}$ is Stage-2 image of $\Phi^{(\Sigma_4, C)}_5$ on $D^b\mathrm{Coh}(K3 \times K3 \times E)$.
- **Verified loci.** PT$_4$ at $d = 4$ for local $\mathbb{P}^2 \times \mathbb{P}^1$ (Cao--Maulik--Toda). $K3 \times K3 \times E$ Hodge diamond $(1, 1, 2, 2, 1, 1)$ admits K\"unneth Stage-1 datum.
- **Heal path.** Verify $E_5 \simeq E_2 \otimes E_2 \otimes E_1$ via Dunn--Lurie additivity ($E_2$ on each K3, $E_1$ on E); construct $b(K3 \times K3 \times E, \Sigma_4, C)$ on lattice-polarised period domain $\Omega^+(\mathrm{II}_{26, 2}) / O^+(\mathrm{II}_{25, 1})$; verify $\kappa_{\mathrm{BKM}}(\Phi_{12}) = 12$.
- **Residue.** Signature $(25, 1)$ forces Fake Monster to $d = 5$, not $d = 3$; rank obstruction is dimension-stratification, not duality. Conway / Leech is the $d = 4$ bridge (Leech embeds in $\mathrm{II}_{25, 1}$).

### F7. Higher-$n$ bar = twisting at $E_n$ for $n \geq 2$

- **Coordinates.** Level 2 (bar/twisting) at $E_n$ for $n \geq 2$. Chart: $E_n$-cooperad / cobar duality. Ambient: $(\infty, 1)$-categorical bar/cobar.
- **Reconstruction theorem (target).** $B_n(A)$ computes twisting/coupling data; $\Omega_n B_n(A) \simeq A$ in appropriate ambient.
- **Verified loci.** $n = 1$ classical; $n = 2$ Francis--Gaitsgory.
- **Heal path.** Francis--Gaitsgory factorisation cooperad at $n = 2$; Lurie higher centralizer $\mathfrak{Z}_{E_n}(A)$ at $n \geq 3$ via HA 5.3.1; Koszul self-duality of $E_n$ for $n \geq 1$ (Fresse).
- **Residue.** Chain-level identification at $n \geq 2$ requires Beilinson--Drinfeld $\Ran(X)$-realisation.

### F8. CY-B$_3$ Koszul, CY-C non-abelian Yangian, CY-D dimensional stratification at odd $d$

- **CY-B$_3$ Koszul.** Coordinates: level 3 at $d = 3$. Target: $A^! \simeq A$ at Stage-1 chiral level. Heal: Beilinson--Ginzburg--Soergel framework + CY trace pairing; verify on Fermat quintic with $\mathbb{Z}_5^5$-equivariance.
- **CY-C non-abelian Yangian.** Coordinates: level 3 at $d = 3$ on $K3 \times E$. Target: matrix Miura presentation, $\mathfrak{sl}_2$-Serre $P_2 = 0$ exact at $D = 3$. Heal: Molev reflection-algebra computation on $(4, 20)$-signature Mukai datum; Arnaudon--Cramp\'e--Doikou--Frappat--Ragoucy reflection equation. Target: $Y_\hbar(\mathfrak{so}(4, 20))$ ungraded; non-Kac super-extension $Y_\hbar(\mathfrak{so}(4 \mid 20))$ when Hodge $\mathbb{Z}/2$-super imposed; never $\mathfrak{osp}(4 \mid 20)$.
- **CY-D dimensional stratification at odd $d$.** Coordinates: level 2 at odd $d$. Target: $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}(A_X) = -\kappa_{\mathrm{BKM}}(\Phi_N)$ modulo explicit shift correction. $d = 3$ verified at K3 $\times E$; $d = 5$ requires Fake Monster Stage-2 (F6).

### F9. Non-abelian K3 Yangian for non-simply-laced $\mathfrak{g}_{K3}$

- **Coordinates.** Level 3 at $d = 2$ on K3 Mukai self-mirror branch with non-simply-laced $\mathfrak{g}_{K3}$. Chart: K3 with non-simply-laced ADE-like structure on Mukai lattice. Ambient: chain-level Yangian.
- **Reconstruction theorem (target).** Twisted Yangian $Y^{\mathrm{tw}}_\hbar(\mathfrak{g}_{K3})$ on K3 chiral algebra at level 3, quantising 5d hCS in twisted sector.
- **Verified loci.** Simply-laced $\mathfrak{g}$ via Costello--Gaiotto--Yagi all-orders.
- **Heal path.** Identify non-simply-laced ADE-like structure on $H^{\mathrm{ev}}(K3, \mathbb{Z})$ via Eichler--Zagier; Molev twisted-Yangian construction with Chevalley involution; extend 5d hCS BV propagator to twisted sector.
- **Residue.** $d^{abc} \neq 0$ at non-simply-laced may require twisted-construction obstruction analysis distinct from simply-laced unobstructed.

### F10. CY-A$_3$ chain-level compact closure

- **Coordinates.** Level 1 (Stage-1 chain-level) at $d = 3$ for compact non-formal CY$_3$. Chart: quintic / generic Schoen. Ambient: chain-level with $\Ainf$-compatible $S^3$-framing on $HC^-_3(C)$, $J$-adic / pro-object on raw bar complex.
- **Reconstruction theorem (target).** Chain-level $\Ainf$ two-stage factorisation extends to compact non-formal CY$_3$.
- **Verified loci.** Witnessed loci ($\mathbb{C}^3$, local $\mathbb{P}^2$, conifold, $K3 \times E$).
- **Heal path.** $\Ainf$-compatible $S^3$-framing on Fermat quintic via $\mathbb{Z}_5^5$-equivariant cover; Costello--Gwilliam--Li one-loop BV anomaly cancellation; J-adic completion through non-formal locus.
- **Residue.** Strict formality of $A_{\mathrm{BVDB}} = \mathrm{End}^\bullet(\bigoplus_{i=0}^4 \mathcal{O}_{X_5}(i))$ on quintic refuted ($Y_3 = H^3 = 5$ is non-zero $m_3$); correct is curved formality with Yukawa as BCOV datum. Number 204 is Hodge total $1+101+101+1$, not $\mathbb{Z}_5^5$-invariant-sector dimension.

### F11. Stage-1 four-physical-lane completeness

- **Coordinates.** Level 1 (Stage-1 physical realisations) at $d \in \{2, 3\}$. Chart: 5d hCS / 6d hCS / mixed-HT-strings local model / Costello--Gwilliam--Li perturbative. Ambient: BV cohomology + holomorphic locality.
- **Reconstruction theorem (target).** Four physical lanes produce equivalent $E_d$-holomorphic factorisation algebras at verified loci. Compact non-toric extension lives along holomorphic de Rham class on mixed-HT lane.
- **Verified loci.** 5d hCS Yangian VOA all-orders simply-laced; 6d hCS $\mathfrak{sl}_2$ unobstructed; resolved conifold finite-Rees with anomaly-free quantum lift; mixed-HT toric loci.
- **Heal path.** Twisted Yangian for non-simply-laced $\mathfrak{g}$ in 5d hCS (F9); compact $K3 \times E$ Hall double via 6d hCS (F2 + F10); mixed-HT holomorphic de Rham obstruction on compact non-toric via Costello--Li one-loop BV residue.
- **Residue.** 6d hCS $\neq$ 3d Chern--Simons; one-loop quartic in fields. $A_{\mathrm{w.f.}} = -C_2 / (2\pi)^3 = -2 h^\vee / (2\pi)^3$ scheme-dependent BV-trivial counter-term + cohomological piece sourced by $d^{abc}$. Miki $S_3$ torus-Weyl has no K3 torus-action input on $K3 \times E$; only elliptic $\mathrm{SL}_2(\mathbb{Z})$ survives.

## Scope-determination obligations carried by other parts

The discipline applied to the body of the volume surfaces a finite list of scope-determination obligations: theorem statements in other parts that have at least one axis underdeclared. Each obligation is a target for the next rectification cycle, not a frontier in the research-direction sense.

- **Stage-2 chart-internal disambiguation.** Six $(\Sigma_2, C)$-routes to $G(K3 \times E)$ in `chapters/examples/k3e_bkm_chapter.tex`: each route's chart-internal coordinates (boundary vacuum $b$, admissibility window) require explicit per-row labels.
- **Class $\mathcal{M}$ bar-tower ambient.** Cross-volume references inherit the Vol II weight-completed ambient; Vol III citations import the ambient qualifier explicitly.
- **Six routes versus six $\Phi$-applications.** The structural remark that the six K3 $\times E$ routes are six $(\Sigma_2, C)$-specialisations of one Stage-1 datum $\Phi^{\mathrm{FA}}_3(D^b\mathrm{Coh}(K3 \times E))$, not six $\Phi$-applications, must be inscribed at every row of the K3 $\times E$ catalogue.
- **$\kappa_{\mathrm{ch}}$ subscript discipline.** Bare $\kappa_{\mathrm{ch}}$ violates HZ-7. Subscripts in active use: $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}, \kappa_{\mathrm{ch}}^{\mathrm{Mukai}}, \kappa_{\mathrm{ch}}^{\mathrm{cpt}}, \kappa_{\mathrm{ch}}^{\mathrm{loc}}, \kappa_{\mathrm{ch}, \mathrm{BV}}$. Every body occurrence carries the relevant subscript.
- **Bare $\Phi$ specialisation.** Naked symbol $\Phi$ at body level decomposes as $\Phi^{(\Sigma_{d-1}, C)}_d$ (Stage-2) or $\Phi^{\mathrm{FA}}_d$ (Stage-1). Every occurrence carries the relevant superscript.
- **Bulk versus bar.** "The bulk" decomposes as $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ at level 3. The bar $B(A)$ at level 2 is twisting/coupling, not bulk; comparison $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \RHom(\Omega B(A), A)$ is the named arrow.

## Eight scope-omission collapse types (for attack-heal use)

The discipline catches scope-omission collapses by axis:

1. **Bar $\to$ bulk.** Level 2 asserted as level 3 without bar/cobar comparison. Heal: $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = \RHom(\Omega B(A), A)$.
2. **Stage $\to$ functor.** Stage-1 + Stage-2 asserted as single functor. Heal: $\Phi^{(\Sigma_{d-1}, C)}_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$, functoriality at Stage-1.
3. **Scalar $\to$ operator.** Level 4 asserted as level 3. Heal: scalar = trace of operator at named chart.
4. **Positive half $\to$ double.** $Y^+(X)$ asserted as $G(X)$ without doubling. Heal: $G(X) = D(Y^+(X))$, three arrows in CoHA evaluation chain.
5. **Chart-internal $\to$ universal.** Chart-specific identity asserted across chart space. Heal: name input chart, restrict universality.
6. **Equivariance stratum.** Toric statement asserted compact non-toric. Heal: name stratum, restrict, isolate obstruction.
7. **Ambient (chain-level / $(\infty, 1)$).** Weight-completed identity asserted in ordinary complexes. Heal: declare ambient and comparison arrow between ambients.
8. **Theory-import.** 6d hCS asserted as 3d CS; 5d hCS Yangian assumed for non-simply-laced without twisted construction. Heal: name source theory, target functor, obstruction.

## Cross-volume residues (referenced from this frontier)

- Vol III $\Delta_5$ / $\Phi_{10}$ / $\Phi_{12}$ references inherit the level-4 disclaimer at `~/igusa-cusp-form/main.tex:96`: scalar is not Hilbert space, not Hall pairing, not orientation, not BPS operator product. Level-3 promotion (compact Hall--Drinfeld--Pfaffian recognition) is research target (F2 + F4).
- Vol III mixed-HT-strings references inherit `~/mixed-holomorphic-topological-strings/main.tex:3207-3266` holomorphic de Rham obstruction discipline (F11).
- Vol III tangential log curve $(C, D_C, \tau_C)$ references inherit `~/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2062-2544` definition (F1).
- Vol III class $\mathcal{M}$ references inherit Vol II `weight_completed_topologization_class_m_platonic.tex` ambient discipline (F3, F8).

## Files

- `appendices/three_axis_scope_discipline.tex` — operating discipline named (`app:three-axis-scope-discipline`).
- `chapters/frontier/scope_discipline_remark.tex` — Part VII opening (`ch:operating-discipline`).
- `chapters/frontier/open_frontiers.tex` — eleven open frontiers with hypothesis package + reconstruction theorem + heal path (`ch:open-frontiers`).
- `notes/platonic_ideal_architecture_vol3.md` — six-movement platonic architecture (Part VII positioned as meta-axis).
- `notes/chatgpt_critique_consequence_map_adversarial_review.md` — May 2026 deep adversarial review installing the three-axis discipline.
