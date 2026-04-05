# Tropical CY Geometry and the Gross-Siebert Programme as Source of the Core Combinatorial Datum

## 1. The Gross-Siebert Programme (2006-2024): Summary

The Gross-Siebert programme reconstructs a Calabi-Yau manifold X from a purely combinatorial/tropical skeleton. The pipeline is:

1. **Toric degeneration**: Start with a maximal degeneration X -> Delta (a family over a disk whose central fiber X_0 is a union of toric varieties glued along toric strata).

2. **Dual intersection complex**: Extract the dual intersection complex B of X_0. This is an integral affine manifold with singularities --- a "tropical CY". The integral affine structure records the toric data of the components, and the singularities (the discriminant locus Delta_B in B) record where the toric description breaks down.

3. **Scattering diagram**: Equip B with a "consistent scattering diagram" D --- a collection of codimension-1 walls in B, each decorated with an automorphism of a formal power series ring (the "wall-crossing automorphism"). The consistency condition is that the ordered product of wall-crossing automorphisms around any loop is trivial.

4. **Reconstruction theorem** (Gross-Siebert 2006, culminating in Gross-Siebert 2021 "Intrinsic mirror symmetry"): The consistent scattering diagram D determines X up to deformation equivalence. More precisely, from D one constructs:
   - The canonical algebra: a ring built from "broken lines" (piecewise-linear paths in B that bend at walls of D)
   - The mirror family: a deformation of X_0 over Spec of the canonical algebra
   - Theta functions: a canonical basis for sections of line bundles on X, indexed by integral points of B

Key references:
- Gross-Siebert, "From real affine geometry to complex geometry" (2006, 2011)
- Gross-Hacking-Keel-Kontsevich, "Canonical bases for cluster algebras" (2018)
- Gross-Siebert, "Intrinsic mirror symmetry and punctured GW invariants" (2021)
- Gross-Pandharipande-Siebert, "The tropical vertex" (2010) --- already cited in the monograph

## 2. The Integral Affine Manifold B for Each Geometry

### 2a. Toric CY3

For a toric CY3 X (e.g., C^3, resolved conifold, local P^2), the toric degeneration is trivial and B = R^3 / lattice. The fan of the toric variety IS the scattering diagram in a trivial sense: the walls are the codimension-1 cones of the fan, and the wall-crossing automorphisms are trivial (identity). The interesting scattering diagram arises when one considers the "quantum" (i.e., corrected) version:

- The initial scattering diagram D_0 has walls corresponding to the rays of the toric fan.
- Consistency requires adding new walls: these are determined by the tropical vertex algorithm (Gross-Pandharipande-Siebert 2010).
- The added walls encode genus-0 GW invariants / DT invariants.
- The broken lines compute these invariants combinatorially.

**Connection to the monograph**: The toric diagram that determines the quiver Q_X (and hence the CoHA / affine super Yangian via RSYZ) is precisely the initial data of the scattering diagram. The corrections added by the tropical vertex algorithm correspond to the imaginary root contributions --- the non-perturbative BPS states. This is already implicit in the monograph's identification of toric data -> root datum (notes/VISION.md), but the scattering diagram makes the "correction" procedure algorithmic and combinatorial.

### 2b. K3 x E

For K3 x E, the tropical geometry factors:

- **Tropical K3**: The K3 surface S admits an elliptic fibration pi: S -> P^1. A maximal degeneration produces B_S = S^2 with 24 singular points (corresponding to the 24 nodal fibers of the elliptic fibration). The integral affine structure on S^2 \ {24 points} has monodromy conjugate to ((1,1),(0,1)) around each singular point.

- **Tropical E**: The elliptic curve E degenerates to a cycle of P^1s; its dual intersection complex is B_E = S^1.

- **Tropical K3 x E**: B = B_S x B_E = (S^2 with 24 singularities) x S^1.

The scattering diagram on B encodes the K3 lattice data. Specifically:
- The 24 singular points of B_S correspond to the 24 singular fibers of the elliptic K3.
- The monodromy of the affine structure around these points encodes the intersection form on H^2(S, Z).
- The Mukai lattice Lambda^{3,2} and the sublattice Lambda^{2,1}_{II} (the hyperbolic lattice of the BKM root datum) are recovered from the integral affine structure.
- The scattering diagram on B encodes phi_{0,1}: the corrections to the initial diagram are controlled by the K3 elliptic genus.

**Key observation**: The Borcherds multiplicative lift phi_{0,1} -> Delta_5 (notes/theory_cy2_cy3_fibration.tex) should have a tropical interpretation: it corresponds to taking the product B_S x B_E and building the scattering diagram on the product from the scattering diagram on B_S, with the S^1 direction providing the additional "modular" parameter sigma. The Fourier-Jacobi expansion of Delta_5 corresponds to a Fourier decomposition of the scattering diagram along the S^1 factor.

### 2c. Hitchin moduli (Higgs(C, G))

The Hitchin moduli space M_H(C, G) is a completely integrable system with Hitchin fibration h: M_H -> A_H (Section 4 of physics_hitchin_langlands.tex, Section 5 of physics_4d_n2_hitchin.tex). In the tropical/Gross-Siebert framework:

- B = the Hitchin base A_H (or a compactification thereof).
- The discriminant locus Delta in A_H (where the spectral curve is singular) is the singular set of B.
- Over A_H \ Delta, the Hitchin fibration is a smooth torus fibration (the SYZ fibration in the mirror symmetry context), providing the integral affine structure.
- The monodromy around Delta encodes the spectral curve degenerations.
- The scattering diagram on A_H is precisely the system of BPS rays / spectral networks of Gaiotto-Moore-Neitzke (already noted in rem:scattering-diagrams of physics_4d_n2_hitchin.tex, line 473).

**The Gaiotto-Moore-Neitzke spectral network IS a scattering diagram**: The "BPS rays" of GMN, emanating from the origin in the Z-plane with wall-crossing automorphisms K_gamma^{Omega(gamma)}, form a scattering diagram in the Kontsevich-Soibelman sense. The consistency condition (trivial monodromy) is the KS wall-crossing formula. This is already noted in the monograph (physics_wall_crossing_mc.tex, Section 5.5).

### 2d. General CY3

For a general CY3 X (e.g., the quintic, complete intersections), the tropical skeleton is:

- B = the dual intersection complex of a maximal degeneration of X.
- dim(B) = 3 (real dimension).
- The singular locus Delta_B has codimension 2 (a graph embedded in B).
- The scattering diagram D on B is the Gross-Siebert canonical scattering diagram, which encodes all genus-0 GW invariants of X.

This is the most general case and the one where the tropical approach provides genuinely new access to the combinatorics. For the quintic, the maximal degeneration is the large complex structure limit (= the point at the tip of the Kahler cone in the mirror picture), and B is a 3-sphere with a trivalent graph of singularities.

## 3. The Thesis: Consistent Scattering Diagram + Vertex Algebra Data = QVCG

### 3a. Statement

The core combinatorial datum of the quantum vertex chiral group G(X) is a **consistent scattering diagram D on the integral affine manifold B**, enriched with vertex algebra data at each singular point of B. Specifically:

**(i) The lattice Lambda(X)**: Read off from the integral affine structure of B. The lattice of integral tangent vectors at a smooth point of B is Lambda(X) (or rather, the local model for it).

**(ii) The real roots Delta^{re}**: Correspond to the singular points (or singular strata) of B. Each singular point p in Delta_B has a local monodromy in SL(3, Z), and the monodromy matrices determine the real simple roots.

**(iii) The imaginary root multiplicities**: Read off from the wall-crossing automorphisms of D. Each wall w of D labeled by gamma with automorphism (1 - x^gamma)^{Omega(gamma)} contributes Omega(gamma) to mult(gamma). The consistency of D is the MC equation d Theta + (1/2)[Theta, Theta] = 0 (this is already noted in physics_wall_crossing_mc.tex, Section 5.5 and physics_bps_root_multiplicities.tex, Section 6.1).

**(iv) The Weyl group W(X)**: Corresponds to the symmetry group of (B, D). For K3 x E, this is the reflection group W^{(2)}(Lambda^{2,1}_{II}); tropically, it acts by piecewise-linear transformations of B.

**(v) The Weyl vector rho**: Determined by the "initial" scattering diagram D_0 (before corrections) via the normalization (rho, alpha_i) = -(alpha_i, alpha_i)/2.

**(vi) The denominator identity**: The "canonical function" on B constructed from broken lines (the Gross-Siebert theta function) IS the denominator identity of the BKM superalgebra.

### 3b. The broken lines = scattering amplitudes = root multiplicities

A broken line in the Gross-Siebert framework is a piecewise-linear path in B that:
- Starts at a point p in B, traveling in a direction m in Lambda.
- Bends each time it crosses a wall of D, picking up a monomial from the wall-crossing automorphism.
- Ends at a point q.

The count of broken lines with given initial and final data computes the structure coefficients of the canonical algebra --- which are genus-0 GW invariants (or equivalently, genus-0 DT invariants). In the QVCG framework, these are the tree-level OPE coefficients, i.e., the structure constants of the E_1-sector (the CoHA).

The higher-genus corrections (beyond genus 0) are not captured by the classical Gross-Siebert scattering diagram. They require "punctured log GW invariants" (Gross-Siebert 2021). In the QVCG language, the genus-g corrections are the arity-(2g+2) shadow obstruction tower components Theta^{(2g+2)}_A. The full MC element Theta_A requires the "quantum" scattering diagram, which incorporates all genera.

### 3c. Consistency = MC equation

The consistency condition for the scattering diagram D (trivial monodromy around every codimension-2 stratum) is equivalent to the Maurer-Cartan equation in the tropical L-infinity algebra obtained from the modular convolution algebra g^{mod}_A by tropicalization. This is already noted in the monograph (physics_wall_crossing_mc.tex, lines 466-496):

- Each wall in D labeled by gamma with automorphism K_gamma^{Omega(gamma)} corresponds to a summand Omega(gamma) * Theta_gamma^{prim} * x^gamma in the MC element.
- The consistency condition is the MC equation.
- The L-infinity brackets l_n correspond to higher-codimension joints where n walls meet.

The tropical L-infinity algebra is the tropicalization of the modular convolution algebra: it is obtained by replacing moduli spaces of curves M_{g,n} by their dual intersection complexes (tropical moduli spaces). This is a precise implementation of the general principle that "tropical geometry is the combinatorial skeleton of algebraic geometry."

## 4. Reading the BKM Superalgebra from B + D

### 4a. The algorithm

Given (B, D), construct the BKM superalgebra g_X as follows:

**Step 1** (Lattice): Extract the lattice Lambda from the integral affine structure. At a smooth point b in B, the lattice of integral tangent vectors is Lambda_b. The global lattice Lambda(X) is the monodromy-invariant sublattice (or the full lattice if B is simply connected after removing singularities).

**Step 2** (Bilinear form): The integral affine structure determines a bilinear form on Lambda via the symplectic form on the total space of the SYZ fibration. For a CY3, this gives a symmetric bilinear form of signature (b_2 + 1, 1) on the Mukai lattice.

**Step 3** (Real roots): Each irreducible component of the singular locus Delta_B contributes real simple roots. The local monodromy around a component Delta_i determines the root alpha_i via the Picard-Lefschetz formula: the monodromy is T_{alpha_i}(v) = v + (v, alpha_i) alpha_i. The Gram matrix A_{ij} = (alpha_i, alpha_j) is computed from the intersection pattern of the singular components.

**Step 4** (Imaginary roots): Run the Gross-Siebert algorithm to construct the consistent completion of D. Each new wall added in the process contributes imaginary roots with multiplicities determined by the wall-crossing automorphisms:
- A wall with automorphism (1 - x^gamma)^{+m} (m > 0) contributes an even imaginary root of multiplicity m (bosonic).
- A wall with automorphism (1 + x^gamma)^{|m|} (m < 0 in the BPS index) contributes an odd imaginary root of multiplicity |m| (fermionic).

**Step 5** (Weyl group and Weyl vector): The Weyl group is the group generated by reflections s_{alpha_i} for real simple roots. The Weyl vector rho is determined by (rho, alpha_i) = -(alpha_i, alpha_i)/2.

**Step 6** (Denominator identity): The denominator identity is the product formula
  Phi_X = e^{-2pi i (rho, z)} * prod_{alpha in Delta_+} (1 - e^{-2pi i (alpha, z)})^{mult(alpha)}
which is the Gross-Siebert "canonical theta function" on B (or rather, its Fourier transform).

### 4b. Verification for the known cases

**K3 x E**: 
- B = S^2(24 sing.) x S^1. 
- Lambda = Lambda^{3,2}. 
- Real simple roots: 3 roots from Lambda^{2,1}_{II} with Gram matrix ((2,-2,-2),(-2,2,-2),(-2,-2,2)).
- Imaginary root multiplicities: f(nm, l) from phi_{0,1}. 
- Denominator identity: (1/64) Delta_5.
- The Gross-Siebert scattering diagram on B recovers phi_{0,1} as the genus-0 correction, and the Borcherds lift produces Delta_5. CHECK.

**Toric CY3 (C^3)**:
- B = R^3 (trivial). 
- Lambda = Z^3 (the Jordan quiver lattice). 
- No real roots (the toric fan has no codimension-2 singularities in the relevant sense).
- The scattering diagram is the tropical vertex of GPS (2010). 
- The wall-crossing automorphisms encode the DT partition function M(q)^{chi(C^3)}. 
- The QVCG is Y(gl_hat_1) = W_{1+infty}. CHECK.

**Hitchin (SL_2, g=2)**:
- B = A_H = C^3 (the Hitchin base). 
- Delta = discriminant divisor.
- The scattering diagram is the GMN spectral network.
- The root datum R(C, SL_2) from physics_hitchin_langlands.tex Section 4 matches.
- Imaginary root multiplicities from the spectral generating function. CHECK.

### 4c. The vertex algebra enrichment

At each singular point p of B, the Gross-Siebert theory associates a "slab function" (the wall-crossing automorphism of the wall passing through p). In the QVCG framework, this should be upgraded to vertex algebra data:

- At each singular point p, there is a local CY category C_p (the "vanishing cycles" category at the corresponding singular fiber of the degeneration).
- The vertex algebra V_p associated to C_p via the CY-to-chiral functor Phi (Theorem CY-A) is the local vertex algebra datum.
- The global chiral algebra A_X is assembled from the local data {V_p} by a "factorization" construction along B, controlled by the scattering diagram D.

This is the vertex algebra enrichment of the Gross-Siebert framework. The scattering diagram D tells you how to glue the local vertex algebras, and the consistency of D is the MC equation for the resulting global chiral algebra.

## 5. New Insights and Gaps

### 5a. What tropical geometry adds to the programme

1. **Computability**: The Gross-Siebert scattering diagram is algorithmically computable. For the monograph, this means that the root datum R(X) (at least at genus 0) can be computed by a finite tropical algorithm. This addresses Open Problem OP1 (non-toric CY3) from physics_4d_n2_hitchin.tex: for the quintic, the dual intersection complex B is a 3-sphere with a trivalent graph, and the tropical vertex algorithm gives the root multiplicities.

2. **Universality**: The framework applies uniformly to all CY3s (toric, K3 x E, compact, non-compact), unifying the ad hoc constructions for each case. The monograph currently treats toric CY3 and K3 x E as separate examples; the Gross-Siebert viewpoint provides a single framework.

3. **The mirror**: The Gross-Siebert programme constructs mirror symmetry as an involution on (B, D): the mirror manifold X' has the same B but the "dual" scattering diagram D'. In the QVCG language, this should be the Koszul duality of quantum vertex chiral groups: G(X)^! = G(X'). This connects to the Koszul duality programme (theory_qvcg_koszul.tex).

4. **The theta basis**: The Gross-Hacking-Keel-Kontsevich theta functions on the mirror form a canonical basis for sections of line bundles. In the QVCG language, these should be the canonical basis vectors of representations of G(X). The "positivity" of the structure constants (a key conjecture of GHKK) would correspond to unitarity of the representation.

### 5b. What is missing

1. **Higher genus**: The classical Gross-Siebert scattering diagram captures genus-0 data only. The full QVCG requires all genera. The "quantum scattering diagram" (incorporating punctured log GW invariants at all genera) is needed. This is the tropical version of the full shadow obstruction tower Theta_A, not just Theta^{<=2}_A.

2. **The superalgebra structure**: The Gross-Siebert framework works with commutative algebras (the canonical ring). The superalgebra structure of the BKM (fermionic roots from negative BPS indices) is not directly visible tropically. One would need a "super" or "derived" tropical geometry to capture the Z/2-grading.

3. **The E_2 structure**: The Gross-Siebert scattering diagram is an E_1 (associative) object: the walls are ordered by phase, and the product is taken in that order. The E_2 (braided) structure of the QVCG requires additional data --- specifically, the braiding should come from the monodromy of the integral affine structure around loops in B. This connects to the Sp_4(Z) action for K3 x E but needs to be developed in general.

4. **Chain-level refinement**: The scattering diagram records numerical invariants (DT numbers). The full QVCG requires the chain-level data (the motivic Hall algebra / categorified DT invariants). The tropical framework should be enhanced to a "derived tropical" or "motivic tropical" framework.

### 5c. The key conjecture

**Conjecture (Tropical reconstruction of the QVCG)**: For any CY3 X with maximal degeneration X -> Delta, let B be the dual intersection complex with its canonical scattering diagram D. Then:

(a) The genus-0 root multiplicities of G(X) are computed by the broken line counts in (B, D).

(b) The full root multiplicities (all genera) are computed by the "quantum broken line counts" incorporating punctured log GW invariants.

(c) The E_2-braiding of G(X) is determined by the monodromy representation pi_1(B \ Delta_B) -> Aut(Lambda).

(d) The denominator identity of G(X) is the theta function Theta_0 on B in the sense of GHKK.

This conjecture, if true, would provide an effective algorithm for computing the root datum of ANY CY3 quantum vertex chiral group, resolving Open Problem OP1 of physics_4d_n2_hitchin.tex.

## 6. Connections to Existing Monograph Content

| Monograph location | Tropical interpretation |
|---|---|
| physics_wall_crossing_mc.tex, Sec 5.5: scattering diagram as tropical MC | Direct match --- the scattering diagram IS the tropical MC element |
| physics_bps_root_multiplicities.tex, Sec 6.1: scattering diagram encodes wall-crossing | The Gross-Siebert consistency = KS trivial monodromy = MC equation |
| physics_4d_n2_hitchin.tex, Rem 5.3: scattering diagrams and tropical geometry | Brief remark; the full Gross-Siebert reconstruction theorem is much stronger |
| theory_cy2_cy3_fibration.tex: Borcherds lift | Tropically: the product B_S x B_E with scattering diagram D_S x D_E |
| physics_wall_crossing_mc.tex, Ref [5]: GPS "tropical vertex" | Already cited; the GPS paper is the genus-0 case of the general programme |
| notes/VISION.md: "toric diagram = root datum" | The toric fan is the initial scattering diagram D_0 |
| physics_4d_n2_hitchin.tex, OP1: non-toric CY3 root datum | Tropical geometry provides the answer via the dual intersection complex |
| physics_hitchin_langlands.tex: SYZ for Hitchin system | The smooth part of the Hitchin fibration = the integral affine structure on B |

## 7. Action Items for the Monograph

1. **Upgrade rem:scattering-diagrams** (physics_4d_n2_hitchin.tex, line 473) from a brief remark to a full section explaining the Gross-Siebert reconstruction theorem and its role as the source of the combinatorial datum.

2. **Write a new section in theory_generalized_root_datum.tex** explaining how the root datum R(X) is read off from (B, D). The algorithm in Section 4a above should be made into a Construction.

3. **State the Tropical Reconstruction Conjecture** (Section 5c above) as a formal conjecture, linking it to OP1.

4. **Develop the fibration story tropically** in theory_cy2_cy3_fibration.tex: the Borcherds lift phi_{0,1} -> Delta_5 should be reinterpreted as the passage from D_{B_S} to D_{B_S x B_E}.

5. **Connect the "quantum scattering diagram"** (incorporating all genera via punctured log GW invariants) to the full shadow obstruction tower Theta_A. This is the tropical version of the shadow obstruction tower completion.

6. **The vertex algebra enrichment** (Section 4c) should be developed as a new research direction: the Gross-Siebert framework provides the skeleton, and the QVCG programme adds the vertex algebra flesh. This is the natural meeting point of the two programmes.

## 8. Key References (not yet in the monograph bibliography)

- M. Gross and B. Siebert, "From real affine geometry to complex geometry," Ann. Math. 174 (2011) 1301-1428.
- M. Gross and B. Siebert, "Intrinsic mirror symmetry," arXiv:1909.07649 (2019).
- M. Gross, P. Hacking, S. Keel, and M. Kontsevich, "Canonical bases for cluster algebras," J. AMS 31 (2018) 497-608.
- M. Gross, P. Hacking, and S. Keel, "Mirror symmetry for log Calabi-Yau surfaces I," Publ. Math. IHES 122 (2015) 65-168.
- T. Mandel, "Scattering diagrams, theta functions, and refined tropical curve counting," J. London Math. Soc. 104 (2021) 2299-2334.
- M. Kontsevich and Y. Soibelman, "Affine structures and non-Archimedean analytic spaces," Prog. Math. 244 (2006) 321-385.
- H. Arguz and M. Gross, "The higher-dimensional tropical vertex," Geom. Topol. 26 (2022) 2135-2235.
- T. Bridgeland, "Scattering diagrams, Hall algebras and stability conditions," Alg. Geom. 4 (2017) 523-561.
