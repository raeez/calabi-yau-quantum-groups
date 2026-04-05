# The Core Combinatorial Datum: Scattering Diagrams with Coefficients

## The Question

What is the combinatorial object R such that:
- For toric CY3: R encodes the toric diagram / fan / web diagram
- For K3 x E: R encodes the lattice Lambda^{3,2} + Weyl data + phi_{0,1}
- For Higgs(C): R encodes the curve C + gauge group G + spectral data
- For general CY3: R classifies the geometry up to derived equivalence

## Executive Summary

**The answer is (f): consistent scattering diagrams on the BPS charge lattice, enriched with automorphic coefficients.** More precisely:

> **R(X) is a consistent scattering diagram D on Gamma_R (the real charge lattice), whose walls are decorated by elements of the quantum torus algebra, satisfying the Kontsevich-Soibelman consistency condition, together with a coefficient system valued in (weak) Jacobi forms that controls the wall-decorations.**

This is not a naive scattering diagram but a **scattering diagram with automorphic coefficients** --- what the Volume III framework calls the "tropical MC datum" of the quantum vertex chiral group. The consistency condition is exactly the MC equation d Theta + (1/2)[Theta, Theta] + ... = 0 in the L-infinity algebra controlling wall-crossing.

The key insight: a scattering diagram is not merely a tropical/combinatorial gadget. When equipped with a coefficient system (the Jacobi form phi controlling root multiplicities), it simultaneously encodes:
1. The combinatorial skeleton (the fan/lattice/toric diagram),
2. The automorphic data (the denominator identity / BPS spectrum),
3. The wall-crossing structure (gauge equivalence of MC elements),
4. The quantum group braiding (the R-matrix from the KS product).

Below I analyze each candidate in detail, then explain why (f) subsumes the others and satisfies all requirements.

---

## Assessment of Each Candidate

### (a) Decorated bipartite graphs on surfaces (brane tilings / dimer models)

**What it is.** A bipartite graph G on a torus T^2 (or more generally on a surface Sigma_g) whose faces, edges, and vertices encode a quiver with potential (Q, W). Faces --> vertices of Q, edges --> arrows of Q, elementary cycles --> terms of W. The Jacobian algebra Jac(Q, W) recovers the coordinate ring of the CY3.

**Toric CY3:** Excellent. The brane tiling is THE standard construction (theory_coha_e1_sector.tex, Construction 6.1): the toric diagram determines the dimer model on T^2, hence the quiver with potential, hence the CoHA = Y^+(g-hat_{Q_X}). The tiling lives on T^2 because toric CY3s have a (C*)^3 action; the T^2 is the real torus quotient.

**K3 x E:** Problematic. K3 is not toric (signature (3,19), not convex rational fan). The K3 lattice has 22 directions, of which only a 2- or 3-dimensional hyperbolic sublattice Lambda^{2,1} participates in the real root system. There is no natural embedding of the K3 data into a bipartite graph on a surface. One could try a dimer model on a higher-genus surface (the K3 fiber is an "internal face"), but:
  - The K3 is not a torus; its fundamental group is trivial.
  - The Borcherds lift structure (phi_{0,1} --> Delta_5) has no natural dimer interpretation.
  - The imaginary root multiplicities from the K3 elliptic genus are not captured by face/edge counts.

**Higgs(C):** Partially relevant for genus 0 and 1 (where the Higgs moduli has toric-like structure), but for g >= 2 the Hitchin system is intrinsically non-toric. The spectral curve geometry does not admit a dimer model description.

**General CY3:** Fails. Brane tilings are inherently toric --- they encode the (C*)^3 action. Non-toric CY3s (quintic, general complete intersections, K3 fibrations) have no brane tiling.

**Verdict: Too restrictive. Captures toric CY3 perfectly but breaks outside the toric world. Score: 3/10 for universality.**

---

### (b) Generalized fans/polyhedra (secondary fans, tropical geometry)

**What it is.** Replace the toric fan Sigma in Z^3 with a more general polyhedral/tropical object: a secondary fan (GKZ decomposition), a tropical variety, or a polyhedral complex in a real vector space.

**Toric CY3:** By definition, the toric fan is the datum. The secondary fan parametrizes the different triangulations of the toric diagram, hence the different crepant resolutions (related by flops).

**K3 x E:** The hyperbolic sublattice Lambda^{2,1} has a fundamental polyhedron P_{II} in the hyperbolic space H^1 (the upper sheet of the hyperboloid). This polyhedron has 3 faces (bounded by the 3 real simple roots delta_1, delta_2, delta_3). The polyhedron IS a "generalized fan" in the sense that the Weyl chambers tile the hyperbolic space. But:
  - The polyhedron captures only the REAL root data (the "tree-level" / "E_1-sector").
  - The imaginary roots (from phi_{0,1}) are NOT encoded in the fan.
  - The automorphic form Delta_5 is not a fan invariant.

**Higgs(C):** No natural fan structure. The charge lattice Z^2 = (rank, degree) has a trivial fan (no walls for g = 0; a single wall for g = 1; a complicated picture for g >= 2 involving the Harder-Narasimhan stratification, but this is a stability condition, not a fan).

**General CY3:** The Kahler cone and its subdivisions provide a fan-like structure, but this captures only h^{1,1} directions and misses the BPS spectrum entirely.

**Verdict: Captures the "skeleton" but not the "flesh." The fan/polyhedron is the Weyl chamber structure, which is the E_1-sector / tree-level data. It cannot encode root multiplicities. Score: 4/10.**

---

### (c) Quivers with potential (Ginzburg dg-algebras)

**What it is.** A quiver Q = (Q_0, Q_1) with a potential W in CQ/[CQ, CQ]. The Ginzburg dg-algebra Gamma(Q, W) is a 3-CY dg-algebra whose derived category D(Gamma) is a CY3 category. Every CY3 category "of finite type" is derived equivalent to D(Gamma) for some (Q, W).

**Toric CY3:** Excellent. The brane tiling produces (Q, W), and CoHA(Q, W) = Y^+(g-hat_{Q_X}) (RSYZ theorem, thm:rsyz in theory_coha_e1_sector.tex).

**K3 x E:** This is more subtle. The derived category D^b(Coh(K3 x E)) is not equivalent to D(Gamma) for any finite quiver with potential (K3 has infinite-dimensional Ext groups in the relevant range). However, one can consider:
  - A sequence of finite approximations (tilting to an exceptional collection on a blow-up);
  - The "categorical" quiver with potential obtained from the heart of a bounded t-structure.
  
  The BKM superalgebra g_{Delta_5} is NOT a quiver Lie algebra in the usual sense: it has infinitely many simple roots (the imaginary simple roots), and its Gram matrix is of indefinite type. The quiver-with-potential framework does not naturally accommodate:
  - The Borcherds lift (the passage from phi_{0,1} to Delta_5);
  - The automorphic correction (adding imaginary roots);
  - The Sp_4(Z) symmetry (which is not a quiver automorphism).

**Higgs(C):** Yes, for formal reasons: Coh(T*C) is a CY2 category, and one can embed it into a CY3 via the cotangent construction. But the quiver with potential for Higgs sheaves on a curve of genus g >= 2 is not known explicitly, and the spectral curve data (the Hitchin fibration) has no quiver interpretation.

**General CY3:** In principle, every CY3 category arises from a (possibly infinite) quiver with potential. The Bridgeland-Smith theorem shows that finite-type BPS spectra correspond to finite quivers. But:
  - The quiver is NOT unique (it depends on a stability condition / t-structure);
  - Mutations change (Q, W) while preserving D(Gamma);
  - The "right" quiver is only well-defined up to mutation equivalence.

**This is the key weakness: the quiver with potential is not a combinatorial INVARIANT --- it is a PRESENTATION. Different stability conditions give different quivers, related by mutations. The invariant is the mutation class, not the individual quiver.**

**Verdict: Too presentation-dependent. The quiver changes under wall-crossing; the invariant data is the mutation class + DT invariants, which is exactly the scattering diagram. Score: 6/10.**

---

### (d) Lattice-polarized K3 data

**What it is.** A lattice L (a primitive sublattice of the K3 lattice Lambda_K3 = U^3 + E_8(-1)^2 of signature (3,19)) together with a weak Jacobi form phi of weight 0 and index 1 for a congruence subgroup of SL_2(Z). The pair (L, phi) determines a CY3 root datum via the fibration construction (theory_generalized_root_datum.tex, Construction 5.5).

**Toric CY3:** Does not apply directly. Toric CY3s do not have K3 fibers (unless they are K3-fibered toric varieties, which are very special). One would need to extend the notion of "lattice polarization" beyond the K3 setting.

**K3 x E:** This IS the paradigmatic case. The datum is (Lambda^{2,1}_{II}, phi_{0,1}, N) where N is the level of the torsion point on E. The fibration functor Fib(R_S, E) produces the CY3 root datum R(K3 x E). This captures everything: the lattice, the real roots, the imaginary roots (via the Borcherds lift of phi_{0,1}), the Weyl group, the Weyl vector, and the denominator identity Delta_5.

**Higgs(C):** Not directly applicable. The Higgs moduli is CY2, not K3-fibered CY3. One can connect via the "dimensional oxidation" T*C x E --> CY3 (theory_higgs_cy2_qvcg.tex, Proposition 7.2), but the lattice-polarized K3 datum does not encode the curve C or its Hitchin system.

**General CY3:** Only applies to K3-fibered CY3s. The quintic (h^{1,1} = 1, h^{2,1} = 101) has no K3 fibration and no natural lattice polarization in this sense. The Gritsenko-Nikulin classification covers many examples but not all CY3s.

**Verdict: Perfect for the K3 x E tower but not universal. Score: 5/10 (for universality; 10/10 for the K3 case).**

---

### (e) Spectral networks (Gaiotto-Moore-Neitzke)

**What it is.** A spectral network W on a Riemann surface C is a collection of trajectories (walls) of the differential lambda^2 (where lambda is the Seiberg-Witten differential on the spectral curve Sigma --> C), together with soliton data at each trajectory. The spectral network encodes the BPS spectrum of the 4d N=2 theory and determines the Darboux coordinates on the Hitchin moduli space.

**Toric CY3:** Spectral networks apply to the 4d N=2 theory engineered by the CY3 (the type IIA compactification). For toric CY3, the spectral network lives on the "mirror curve" (the thickened toric diagram). The BPS states are the finite webs. This works, but the spectral network is a DERIVED object --- it requires choosing a phase (an angle in the central charge plane), and different phases give different networks.

**K3 x E:** The 4d N=2 theory from K3 x E is a CHL string. Spectral networks have not been developed for this case (the spectral curve is on the K3 fiber, not on a curve). The BPS spectrum is encoded by phi_{0,1} and the Borcherds lift, which predates the GMN formalism.

**Higgs(C):** Excellent. The Hitchin system on C IS the physical system for which spectral networks were designed. The spectral curve Sigma_b --> C and its WKB triangulation are exactly the data of the spectral network. For g >= 2, the spectral network captures:
  - The BPS spectrum (soliton data at walls);
  - The wall-crossing (as the phase rotates, walls collide and split);
  - The Stokes data (monodromy of flat connections).

**General CY3:** Spectral networks apply to any CY3 that engineers a 4d N=2 theory (i.e., essentially all CY3s via type IIB). But the spectral network lives on a 2d surface (the "UV curve" of the 4d theory), so it is a 2d object encoding a 3d invariant. This dimensional reduction loses information for CY3s without a natural surface.

**Verdict: Excellent for Higgs/Hitchin, good for toric, incomplete for K3 x E. The spectral network is a phase-dependent presentation of the scattering diagram. Score: 7/10.**

---

### (f) Scattering diagrams (Gross-Siebert / Kontsevich-Soibelman)

**What it is.** A scattering diagram D on a real vector space Gamma_R (the "charge lattice tensored with R") consists of:
  - Walls: codimension-1 cones (rays in 2d, hyperplanes in higher dimensions)
  - Decorations: each wall d is labelled by a charge gamma in Gamma and decorated with an automorphism K_gamma^{Omega(gamma)} of the quantum torus algebra C[Gamma]
  - Consistency: the monodromy around any joint (codimension-2 locus where walls intersect) is trivial

The consistency condition is equivalent to the MC equation d Theta + (1/2)[Theta, Theta] + ... = 0 in the L-infinity algebra controlling wall-crossing (physics_wall_crossing_mc.tex, Section 5.2).

**I now argue that this is the correct answer, but with a critical enhancement: the scattering diagram must be equipped with an automorphic coefficient system.**

---

## The Enhanced Scattering Diagram: R(X) = (Gamma, D, phi)

### Definition

The core combinatorial datum of a CY3 X is:

> R(X) = (Gamma, <,>, D, phi)

where:
1. **Gamma** is the charge lattice (a free Z-module of finite rank with a skew-symmetric pairing <,>: Gamma x Gamma --> Z, the Dirac-Schwinger-Zwanziger pairing / Euler form).
2. **D** is a consistent scattering diagram on Gamma_R, encoding the BPS spectrum via wall-decorations.
3. **phi** is a coefficient system: a (weak) Jacobi form (or quasi-modular form, or mock modular form) of weight 0 that controls the wall-decoration data.

The relationship between D and phi: the wall decoration for a wall of charge gamma is

    K_gamma^{Omega(gamma)} where Omega(gamma) = c_phi(gamma^2/2, ell(gamma))

i.e., the BPS index Omega(gamma) is a Fourier coefficient of phi.

The **consistency condition** on D (trivial monodromy around joints) is equivalent to:
- The MC equation for the universal MC element Theta_A in the Volume I sense;
- The Kontsevich-Soibelman wall-crossing formula;
- The convergence of the Borcherds product to an automorphic form (axiom CY5).

### Specialization to each case

**(i) Toric CY3.** 
- Gamma = Z^{Q_0} (dimension vectors of the quiver), <,> = antisymmetrized Euler-Ringel form.
- D = the scattering diagram dual to the toric fan. For C^3: a single wall at the origin (no wall-crossing). For the conifold: two chambers separated by a wall at Im(Z(gamma)) = 0.
- phi = the "motivic DT generating function" = product of (1-q^n)^{DT_n} factors.
- The consistency of D is the integrality and wall-crossing of DT invariants.
- The toric diagram is recovered as the DUAL of D: the fan generators are the asymptotic directions of the walls.
- The brane tiling/dimer model is recovered as the periodic tiling dual to D on the universal cover of the T^2 on which the scattering diagram lives.

**(ii) K3 x E.**
- Gamma = Lambda^{3,2} = Lambda^{2,1}_{II} + Lambda^{1,1}, <,> from the Mukai pairing.
- D = the scattering diagram on Lambda^{2,1}_R whose walls are the hyperplanes orthogonal to roots. The real root walls (delta_i^perp) are the Weyl chamber walls; the imaginary root walls arise from the BPS states.
- phi = phi_{0,1} (the K3 elliptic genus), weight 0, index 1.
- The consistency of D is EXACTLY the statement that the Borcherds product (1/64) Delta_5 converges to an automorphic form for O(Lambda^{3,2})_+.
- The Weyl chambers of W^{(2)}(Lambda^{2,1}) are the "BPS chambers" of D.
- The imaginary roots add walls INSIDE the Weyl chambers (the "quantum corrections" / "automorphic correction" / higher-arity shadows).

The identification is precise: the scattering diagram D encodes BOTH the real root datum (Weyl chambers = the tree-level / E_1-sector) AND the automorphic correction (imaginary root walls = the shadow obstruction tower / higher-arity data).

**(iii) Higgs(C).**
- Gamma = Z^2 = (rank, degree), <,> = r_1 d_2 - r_2 d_1 (the antisymmetric part of the Euler form).
- D = the scattering diagram on R^2 encoding the BPS spectrum of the Hitchin system. The walls are the "BPS rays" emanating from the origin at angles arg(Z(gamma)) where Z is the central charge.
- phi depends on genus:
  - g = 0: trivial (finite number of BPS states, finitely many walls).
  - g = 1: essentially 1/eta(tau)^2 (partition multiplicities), reflecting the SL_2(Z) symmetry.
  - g >= 2: a new "Hitchin modular form" whose Fourier coefficients are Betti numbers of semistable Higgs moduli.
- The spectral curve data is encoded in the REFINED scattering diagram: each wall carries not just an integer Omega(gamma) but the full motivic DT invariant Omega^{mot}(gamma), which remembers the cohomology of the Hitchin fiber.
- Spectral networks (candidate (e)) are the PHASE SLICES of D: fixing a phase theta, the spectral network W_theta is the intersection of D with the half-plane at angle theta. Rotating theta gives the full scattering diagram by sweeping through all phases.

**(iv) General CY3.**
- Gamma = K_0(X) with the Euler form (or the charge lattice of the associated 4d N=2 theory for non-compact X, or the Mukai lattice for compact X).
- D = the scattering diagram on Gamma_R, consistent by the KS wall-crossing formula.
- phi = the "BPS generating function," which is:
  - A Jacobi form for K3-fibered CY3s (by the Borcherds lift);
  - Related to the topological vertex for toric CY3s;
  - Conjecturally a mock modular or higher-depth modular form for general CY3s (e.g., the quintic --- open problem P2 of theory_generalized_root_datum.tex).
- The derived equivalence class of X is determined by the mutation class of D (i.e., D modulo gauge equivalence of the MC element).

---

## Why the Scattering Diagram Subsumes the Other Candidates

### (f) subsumes (a): brane tilings are scattering diagrams on T^2

For a toric CY3, the scattering diagram D on R^2 (the "tropical" plane) is periodic under the lattice translations of the toric fan. The periodic scattering diagram on R^2/Z^2 = T^2 IS the dimer model / brane tiling (dual graph). The walls of D become the edges of the bipartite graph; the chambers become the faces. Consistency of D = the matching condition of the dimer. The brane tiling is the scattering diagram for the special case of toric CY3.

### (f) subsumes (b): fans are the tree-level / real-root part of D

The toric fan (or the Weyl chamber decomposition, for K3 x E) is the "real root" part of the scattering diagram: the walls corresponding to real roots alpha with (alpha, alpha) = 2. The imaginary root walls are the "quantum corrections." The fan is D restricted to the real root walls --- the tree-level data. The full D adds all imaginary root walls, which is the automorphic correction.

### (f) subsumes (c): quivers with potential are scattering diagrams in a chamber

A quiver with potential (Q, W) determines a specific "BPS chamber" of the scattering diagram: the region in stability space where all BPS states have positive central charge. Different chambers give different quivers, related by mutations. The scattering diagram D is the MUTATION-INVARIANT object: it records ALL chambers simultaneously, with walls marking the transitions between them. The quiver (Q, W) is D restricted to a single chamber.

### (f) subsumes (d): lattice-polarized K3 data enters through the coefficient system

The lattice Lambda^{2,1}_{II} determines the real root walls of D. The Jacobi form phi_{0,1} IS the coefficient system phi. The Borcherds lift is the passage from the coefficient system to the full scattering diagram: Borch(phi) = Phi_{R(X)} is the "sum over all walls" that produces the automorphic form. The fibration construction Fib(R_S, E) of theory_generalized_root_datum.tex is exactly the construction of D from (Gamma, phi) via the Borcherds lift.

### (f) subsumes (e): spectral networks are phase slices of D

A spectral network W_theta (at phase theta) is the intersection of the scattering diagram D with the half-plane {gamma in Gamma_R : arg(Z(gamma)) = theta}. Rotating theta traces out the full scattering diagram. The soliton data at each trajectory of W_theta is the wall-decoration data of D. The "wall-crossing" of spectral networks (as theta crosses a BPS ray) is the monodromy of D around a joint.

---

## The Three Layers of R(X)

The enhanced scattering diagram R(X) = (Gamma, D, phi) has three layers, corresponding to the three levels of structure in the quantum vertex chiral group:

### Layer 1: The lattice Gamma with pairing <,> (the "skeleton")
- This is the K-theory / charge lattice.
- For toric CY3: Z^{Q_0} with Euler-Ringel form.
- For K3 x E: Lambda^{3,2} with Mukai pairing.
- For Higgs(C): Z^2 = (rank, degree) with Euler form.
- This layer determines the quantum torus C[Gamma] and hence the "target" of the wall-decorations.

### Layer 2: The coefficient system phi (the "flesh")
- This is the BPS counting function / Jacobi form.
- For toric CY3: the DT partition function (related to the topological vertex).
- For K3 x E: phi_{0,1} (the K3 elliptic genus).
- For Higgs(C): genus-dependent --- trivial (g=0), 1/eta^2 (g=1), Hitchin modular form (g>=2).
- This layer determines the root multiplicities: mult(alpha) = c_phi(alpha^2/2, ell(alpha)).
- CRUCIALLY: phi is a modular object (Jacobi form, mock modular, etc.), which is the "automorphic" part of the data.

### Layer 3: The scattering diagram D (the "structure")
- This is the combinatorial arrangement of walls in Gamma_R with their decorations.
- D is determined by Layers 1 and 2 (plus a "seed" --- the choice of initial scattering diagram, which is the tree-level / real root data) via the consistency condition (MC equation).
- The consistency condition is constructive: one builds D iteratively, adding walls to cancel monodromy, starting from the seed (real root walls) and progressively adding imaginary root walls. This is exactly the shadow obstruction tower construction of Volume I: Theta^{(2)} (arity 2, tree level) is the seed, and Theta^{(r)} (arity r) adds the walls at "distance r" from the seed.

The passage from (Gamma, phi) to D is the Borcherds lift / automorphic correction / shadow obstruction tower construction. The scattering diagram D encodes the FULL quantum vertex chiral group G(X), not just the positive half (CoHA).

---

## Classification Power: R(X) and Derived Equivalence

**Claim (conjectural).** Two CY3 threefolds X, X' have equivalent derived categories D^b(Coh(X)) ~ D^b(Coh(X')) if and only if their enhanced scattering diagrams R(X), R(X') are gauge-equivalent (i.e., the MC elements Theta_X, Theta_{X'} are L-infinity gauge equivalent).

**Evidence:**
1. For toric CY3: derived equivalence = mutation equivalence of quivers = same scattering diagram (different chambers).
2. For K3 x E: derived equivalence of K3 surfaces is controlled by the Mukai lattice and Hodge structure. The scattering diagram R(K3 x E) encodes the Mukai lattice (Layer 1) and the elliptic genus (Layer 2), which together with the Hodge structure determine the derived category.
3. For Higgs(C): derived equivalence of Coh(T*C) depends on C up to isomorphism (since T*C determines C). The scattering diagram encodes C through the Hitchin spectral data.
4. General: Bridgeland's work on stability conditions shows that the "space of stability conditions" Stab(D^b(X)) is a complex manifold whose fundamental group acts on the BPS spectrum by wall-crossing. The scattering diagram D is the universal cover of this action --- it records the BPS spectrum in all chambers simultaneously.

---

## Connection to the Topological Vertex and Internal Faces

The hint mentions the topological vertex factorization: the toric CY3 partition function factorizes into vertex contributions C_{lam,mu,nu}(q) (one per vertex of the toric diagram) and edge gluings (one per edge). Each vertex = an intertwiner of Y(gl-hat_1). This is TREE-LEVEL: no internal faces (the dual graph of the toric diagram is a tree for "strip geometries," and has loops = internal faces for compact 4-cycles).

### Internal faces in the scattering diagram framework

The generalization to internal faces corresponds to:

1. **Loops in the dual graph** = algebraic surface cycles = compact 4-cycles. In the scattering diagram, these correspond to CLOSED WALLS (walls that form loops in Gamma_R, not just rays). A closed wall encloses a "chamber" whose monodromy is nontrivial --- this is the "internal face" contribution.

2. **For K3 x E:** The K3 fiber IS an internal face. In the scattering diagram on Lambda^{2,1}_R (the 2-dimensional hyperbolic plane), the three Weyl chamber walls form a TRIANGLE (the fundamental domain P_{II}). This triangle is a "closed loop" in the wall structure. The interior of the triangle is the "internal face," and its contribution is the imaginary root spectrum from phi_{0,1}. The K3 elliptic genus controls what lives INSIDE the triangle.

3. **Escaping toric:** The scattering diagram on a hyperbolic space (signature (s,1) with s >= 2) is inherently non-toric: the walls are geodesics in H^{s-1}, not rays in R^2. The curvature of hyperbolic space = the non-convexity of the fan = the "escape from toric." The K3 lattice signature (3,19) gives walls on H^2 (the hyperbolic plane), which has negative curvature --- fundamentally different from the flat R^2 of toric scattering diagrams.

4. **Encoding the automorphic data:** The Borcherds lift is the mechanism by which the coefficient system phi (living on the internal faces) produces the full scattering diagram. The walls INSIDE the fundamental domain are generated by phi via the consistency condition. This is exactly the "automorphic correction = shadow obstruction tower" identification of VISION.md.

---

## Summary Table

| Feature | (a) Dimers | (b) Fans | (c) QwP | (d) K3-lat | (e) Spec.net | **(f) Scat.diag** |
|---------|-----------|---------|---------|-----------|-------------|-----------------|
| Toric CY3 | Yes | Yes | Yes | No | Yes | **Yes** |
| K3 x E | No | Partial | No | Yes | No | **Yes** |
| Higgs(C) | No | No | Partial | No | Yes | **Yes** |
| General CY3 | No | Partial | Partial | No | Partial | **Yes** |
| Encodes BPS spectrum | No | No | Partial | Yes | Yes | **Yes** |
| Encodes wall-crossing | No | No | Via mutation | No | Yes | **Yes** |
| Encodes automorphic form | No | No | No | Yes | No | **Yes** |
| Encodes R-matrix/braiding | No | No | Partial | No | Yes | **Yes** |
| Invariant (not presentation) | Yes | Yes | No | Yes | No | **Yes** (up to gauge) |
| Internal faces (loops) | Yes | No | Yes | Yes | Yes | **Yes** |

---

## Precise Conjecture

**Conjecture (Core Combinatorial Datum).** Let CY3Root denote the category of CY3 root data (Definition 2.3 of theory_generalized_root_datum.tex) and let ScatAut denote the category of consistent scattering diagrams with automorphic coefficients (scattering diagrams on even lattices Gamma with skew pairing, equipped with a weight-0 Jacobi-type form phi as coefficient system, and satisfying the KS consistency condition). Then:

(i) There is a fully faithful functor R: CY3Root --> ScatAut sending a CY3 root datum R = (Lambda, Delta, mult, W, rho) to the scattering diagram D(R) on Lambda^{hyp}_R with coefficient phi_R (the Jacobi form governing multiplicities).

(ii) The essential image of R consists of those scattering diagrams satisfying the CY axioms (CY1)-(CY7).

(iii) For a CY3 threefold X, the quantum vertex chiral group G(X) is recovered from D(R(X)) as follows:
  - The positive half (CoHA) = the algebra generated by wall-crossing automorphisms in a single chamber;
  - The full algebra (BKM superalgebra / affine super Yangian) = the algebra generated by ALL wall-crossing automorphisms across ALL chambers;
  - The R-matrix = the KS product along a path crossing a single wall;
  - The modular characteristic kappa = the weight of the automorphic form = (1/2) c_phi(0,0).

(iv) Two CY3 root data R, R' produce isomorphic quantum vertex chiral groups G(X) ~ G(X') if and only if their scattering diagrams D(R), D(R') are gauge-equivalent (L-infinity gauge equivalence of the MC elements Theta_R, Theta_{R'}).

---

## What Remains to Be Done

1. **Make the "automorphic coefficient" notion precise.** The coefficient system phi must be axiomatized: what class of modular forms is allowed? For K3 x E, phi_{0,1} is a weak Jacobi form. For toric CY3, the analogous object is the refined DT generating function. For general CY3, it may be a mock modular or higher-depth modular form (the quintic case is open).

2. **Prove the scattering diagram determines the QVCG.** The construction CoHA = single-chamber algebra is established (RSYZ for toric, Schiffmann-Vasserot for Higgs). The full algebra = all-chambers algebra requires the Drinfeld double construction, which is known for toric (affine super Yangian) and for K3 x E (BKM superalgebra) but not in general.

3. **Establish gauge equivalence = derived equivalence.** This would follow from Bridgeland's space of stability conditions being connected and the scattering diagram being the universal cover of the monodromy action.

4. **Handle the non-fibered case.** The fibration construction Fib(R_S, E) produces scattering diagrams from K3 data. For toric CY3, the construction comes from the brane tiling. For general CY3 (quintic, etc.), the construction of the scattering diagram from the geometry is the open problem --- it requires understanding the BPS spectrum of the quintic, which is unknown.

5. **Internal faces and higher genus.** The topological vertex analogy suggests that internal faces (compact 4-cycles) contribute "loop corrections" to the scattering diagram. Making this precise requires the "scattering diagram on a surface" generalization (Gross-Siebert for log CY surfaces), where the surface is the base of the CY3 fibration and internal faces are the compact fibers. This connects back to (a): the dimer model on a higher-genus surface IS the scattering diagram with internal faces, but only in the toric-like setting. The general case requires "scattering diagrams on hyperbolic surfaces," which is new territory.
