# Vertex-Enriched Scattering Diagrams as the Combinatorial Datum

## Research note for Volume III (Calabi-Yau Quantum Groups)
## Raeez Lorgat, 2 April 2026

---

## 0. Summary of the Proposal

The combinatorial datum of the quantum vertex chiral group G(X) is a
**vertex-enriched scattering diagram**: a scattering diagram
(Gross-Siebert / Kontsevich-Soibelman) in a real vector space, with the
additional structure of a **local vertex algebra** (an intertwiner of the
quantum vertex chiral group) attached to each vertex (codimension-2
intersection of walls).

- For toric CY3: the scattering diagram is the toric fan, the local vertex
  algebras are the topological vertex C_{lam,mu,nu}(q) viewed as
  intertwiners of Y(gl-hat_1).

- For non-toric CY3: the scattering diagram is the tropicalization of the
  CY geometry (Gross-Siebert mirror construction).

- For K3 x E: the scattering diagram lives in the Mukai lattice.

- For Higgs(C): the scattering diagram is the spectral network of
  Gaiotto-Moore-Neitzke.

The consistency condition (trivial monodromy around loops) is identified
with the Maurer-Cartan equation D*Theta + 1/2[Theta,Theta] = 0.

---

## 1. Scattering Diagrams: Foundations

### 1.1 Definition (Kontsevich-Soibelman 2004, Gross-Siebert 2006)

A **scattering diagram** D in a real vector space M_R (typically
M_R = Hom(N, R) for a lattice N) consists of:

- A collection of **walls** (d_i, f_i), where each d_i is a
  codimension-1 rational polyhedral cone in M_R and f_i is a formal
  automorphism of the algebraic torus T_N = Spec(k[N]).

- The wall-crossing automorphism attached to a wall d with primitive
  normal vector n_0 in N has the form

      theta_{d,f} : z^m |-> z^m * f(z^{n_0})^{<m, n_0>}

  where f is a formal power series with f(0) = 1.

The **consistency condition**: for any loop gamma in M_R \ (union of
codimension-2 strata), the ordered composition of wall-crossing
automorphisms encountered along gamma is the identity.

### 1.2 Key references and developments

**Kontsevich-Soibelman (2004, arXiv:math/0406564; 2008, arXiv:0811.2435)**:
Introduced scattering diagrams in the context of the wall-crossing formula
for Donaldson-Thomas invariants. Their key insight: the BPS automorphisms
K_gamma for different charges gamma compose to a consistent scattering
diagram if and only if the wall-crossing formula holds. The consistency is
a formal consequence of the motivic Hall algebra structure on the CY3
category.

**Gross-Siebert (2006, arXiv:math/0609514; 2011, arXiv:0809.4846; 2016,
arXiv:1512.08586; 2022, "Intrinsic mirror symmetry")**:
Developed scattering diagrams as the key tool in their mirror symmetry
programme. For a toric degeneration X -> Delta, the scattering diagram
lives on the base B of the dual intersection complex, encoding tropical
disk counts. Their main theorems:

- (GS Reconstruction): A consistent scattering diagram determines a
  mirror family, reconstructing the B-model from tropical A-model data.

- (GS Consistency = enumerative): The consistency condition for the
  scattering diagram is equivalent to the WDVV equations for the
  genus-0 Gromov-Witten theory (or their tropical analogues).

- (GS 2022, Intrinsic mirror symmetry): For a log CY pair (X, D), the
  scattering diagram is defined intrinsically (not requiring a toric
  degeneration) using punctured log Gromov-Witten invariants.

**Gross-Hacking-Keel-Kontsevich (2018, arXiv:1411.1394)**:
For cluster varieties and log CY surfaces, scattering diagrams govern
the canonical basis (theta functions). Walls correspond to broken lines
(tropical analogues of holomorphic disks), and vertices correspond to
singularities of the affine structure on the base.

**Bridgeland (2017, arXiv:1611.03697; 2019, arXiv:1906.02317)**:
Reinterpreted scattering diagrams in terms of Stokes data for the
Riemann-Hilbert problem associated to a BPS structure. Key contribution:
a scattering diagram is the Stokes data of a connection on the punctured
complex plane C*, where the walls are Stokes rays and the automorphisms
are Stokes factors. The consistency condition (trivial monodromy) is
then a standard result in the theory of irregular singularities.

Bridgeland's "BPS structures" formalism: a BPS structure on a lattice
Gamma is exactly the data needed to define a consistent scattering
diagram. The space of BPS structures with fixed lattice Gamma is the
space of Bridgeland stability conditions Stab(C) for an appropriate
CY3 category C.

### 1.3 The L-infinity perspective (existing in the monograph)

As developed in `physics_wall_crossing_mc.tex` (Section 4.2), the
scattering diagram admits an L-infinity interpretation:

- The tropical L-infinity algebra is obtained from the modular
  convolution algebra g^mod_A by tropicalization (replacing moduli of
  curves by dual intersection complexes).

- Each wall labeled gamma with automorphism K_gamma^{Omega(gamma)}
  corresponds to a summand Omega(gamma) * Theta_gamma^prim * x^gamma
  in the MC element Theta_A.

- The consistency condition (trivial monodromy around joints) IS the
  MC equation: d*Theta + 1/2[Theta, Theta] + ... = 0.

This identification is already present in the monograph's framework.
What the vertex-enriched proposal adds is the DATA AT THE VERTICES.

---

## 2. Toric Scattering Diagrams and the Topological Vertex

### 2.1 The toric CY3 scattering diagram

For a toric CY3 X_Sigma determined by a fan Sigma in Z^3, the toric
diagram is a trivalent planar graph Gamma_X (the dual of the toric
polygon). This graph IS the scattering diagram:

- **Vertices** of Gamma_X (trivalent) = C^3 patches.
- **Edges** (internal) = C^2 patches = gluing strips.
- **External legs** = non-compact divisors.

The toric fan imposes the consistency condition automatically: the
scattering diagram is "trivially consistent" because the fan is
complete and the automorphisms along the three walls meeting at each
vertex compose to the identity. This is equivalent to the SL(3,Z)
condition on the fan.

### 2.2 The topological vertex as local vertex algebra

The AKMV topological vertex C_{lam,mu,nu}(q) (as developed in
`physics_topological_strings.tex`, Section 4) is:

    C_{lam,mu,nu}(q) = q^{kappa_mu/2} s_{nu^t}(q^rho)
        * sum_eta s_{lam^t/eta}(q^{nu+rho}) s_{mu/eta}(q^{nu^t+rho})

The key identification (Conjecture 4.8 in `physics_topological_strings.tex`):
C_{lam,mu,nu}(q) IS the matrix element of an E_2-chiral intertwiner of
G(C^3) = Y(gl-hat_1) = W_{1+infinity}:

    C_{lam,mu,nu}(q) = <lam| Phi^{E_2}_{A_{C^3}}(z_1,z_2,z_3) |mu,nu>

where Phi^{E_2} is the genus-0, 3-point amplitude and F_lam are
Fock-space basis elements of B(A_{C^3}).

**This IS the vertex enrichment**: at each trivalent vertex v of the
toric scattering diagram, the local vertex algebra is
G_v = G(C^3) = Y(gl-hat_1), and the topological vertex C_{lam,mu,nu}(q)
is the intertwiner (= the vertex algebra datum) attached to v.

### 2.3 Gluing = factorization product

The AKMV factorization formula

    Z(X) = sum_{lam_e} prod_v C_{lam_{e1},lam_{e2},lam_{e3}}(q)
            * prod_e (-Q_e)^{|lam_e|} f_{lam_e}(q)

is exactly the factorization product of the vertex-enriched scattering
diagram:

- The sum over partitions lam_e on each internal edge is the "path
  integral over internal degrees of freedom" = the trace over edge
  Fock spaces.

- The vertex amplitudes C_{...}(q) are the local vertex algebra
  contributions.

- The edge weights (-Q_e)^{|lam_e|} f_{lam_e}(q) are the wall-crossing
  automorphisms (= the propagators/Stokes data) on each wall.

**Conclusion**: For toric CY3, the vertex-enriched scattering diagram
framework is literally the AKMV topological vertex formalism, repackaged
in the language of scattering diagrams. The proposal is not new content
for the toric case; it is a reformulation that GENERALIZES to the
non-toric case.

### 2.4 The crystal melting / 3D partition interpretation

The crystal melting picture (Okounkov-Reshetikhin-Vafa) provides the
combinatorial model: 3D partitions label states in the Fock space F of
Y(gl-hat_1), the topological vertex is a vertex operator creating/
annihilating boxes, and Z(X) counts weighted crystal configurations.

In the scattering diagram language: the crystal is the "tropical curve"
in the fan Sigma, the 3D partition is the tropical disk, and the
topological vertex is the contribution from each vertex of the tropical
curve where three walls meet.

---

## 3. K3 x E: The Scattering Diagram from the Mukai Lattice

### 3.1 What is the scattering diagram for K3 x E?

For X = K3 x E (or more generally (S x E)/(Z/NZ)), the geometry is
NOT toric. The scattering diagram must be constructed differently.

**The lattice**: The charge lattice is Gamma = H_even(X, Z) which,
via the Kunneth decomposition, is

    Gamma = H^*(K3, Z) tensor H^*(E, Z)

The Mukai lattice of K3 is Lambda_S = U^3 + E_8(-1)^2 (signature (4,20)).
The full lattice has the sublattice Lambda^{3,2} = Lambda^{1,1} +
Lambda^{1,1} + [2] of signature (3,2) that governs the BKM algebra
g_{Delta_5} (as in Chapter ch:k3-times-e of the monograph).

**The base space**: The scattering diagram lives in

    M_R = Lambda^{3,2} tensor R

which is a real 5-dimensional space of signature (3,2). The relevant
"positive cone" is the tube domain in Lambda^{3,2} tensor C, which
identifies with the Siegel upper half-space H_2 via the isomorphism
Sp_4(Z)/{+/- I} = SO_+(Lambda^{3,2}).

### 3.2 Walls from the Weyl group

The **walls** of the K3 x E scattering diagram are:

(a) **Real root walls**: For each real simple root delta_i (i=1,2,3)
    with (delta_i, delta_i) = 2, the hyperplane delta_i^perp in
    Lambda^{3,2} tensor R is a wall. The associated automorphism is
    the Weyl reflection s_{delta_i}. These are the "hard" walls --
    they are always present and do not depend on the stability condition.

(b) **Imaginary root walls**: For each imaginary root alpha with
    mult(alpha) = f(nm, l) (Fourier coefficient of phi_{0,1}), the
    hyperplane alpha^perp is a wall carrying the KS automorphism
    K_alpha^{f(nm,l)}. These are the "soft" walls -- their arrangement
    depends on the stability condition (= the choice of point in H_2).

The **vertices** (codimension-2 intersections of walls) in the K3 x E
case correspond to joints where two walls meet. At each such joint,
the consistency condition is the MC equation restricted to that
codimension-2 stratum.

### 3.3 The Mukai lattice as the scattering lattice

**YES, the scattering diagram is directly related to the Mukai lattice.**

The Mukai lattice Lambda^{Muk}(K3) = U^3 + E_8(-1)^2 determines the
scattering lattice. More precisely:

- The scattering diagram lives in M_R = N_R, where N is the lattice
  dual to the Mukai lattice (or, in the self-dual case of K3, the
  Mukai lattice itself, since U^3 + E_8(-1)^2 is unimodular).

- The walls are indexed by roots alpha in Lambda^{Muk}, with the
  wall being alpha^perp and the automorphism determined by
  mult(alpha) = c_{phi_{0,1}}((alpha,alpha)/2, l(alpha)).

- The fundamental domain for the Weyl group W^{(2)}(Lambda^{2,1}_{II})
  is the fundamental polyhedron P_{II} of the hyperbolic reflection
  group.

The **Borcherds product** Delta_5 = e^{-2*pi*i*(rho,z)} * prod_{alpha}
(1 - e^{-2*pi*i*(alpha,z)})^{mult(alpha)} is then the "partition
function" of the scattering diagram: the product over all walls of
the wall-crossing automorphisms, evaluated on the tube domain.

### 3.4 Local vertex algebras for K3 x E

What are the local vertex algebras at the vertices of the K3 x E
scattering diagram?

**Key difference from the toric case**: the K3 x E geometry does not
have isolated C^3 patches (it is not toric), so there is no a priori
reason to expect the local vertex algebra to be Y(gl-hat_1).

**Proposal**: At a vertex where walls delta_1^perp and delta_2^perp
intersect (a codimension-2 joint in the hyperbolic lattice):

- The local vertex algebra is a **module over the BKM superalgebra
  g_{Delta_5}**, specifically the intertwiner space

      Hom_{g_{Delta_5}}(V_{delta_1} tensor V_{delta_2}, V_{delta_1+delta_2})

  where V_alpha are the root space representations.

- For the three real simple roots, the local vertex algebras at the
  three pairwise intersections delta_i^perp cap delta_j^perp should be
  related to the structure constants of the BKM superalgebra.

**This is genuinely new structure that the vertex-enriched framework
would need to provide for the K3 x E case.** In the toric case, all
local vertex algebras are copies of Y(gl-hat_1); in the K3 x E case,
the local vertex algebras are more complex objects determined by the
BKM superalgebra structure.

---

## 4. Higgs(C): Spectral Networks as Scattering Diagrams

### 4.1 The Gaiotto-Moore-Neitzke spectral network

For a 4d N=2 theory of class S[G, C] (compactification of the 6d (2,0)
theory of type g = Lie(G) on a curve C with defects D), Gaiotto-Moore-
Neitzke introduced **spectral networks** (arXiv:1204.4824, 1301.6169):

A spectral network W(zeta) on C (for a fixed phase zeta in S^1) is a
collection of paths ("walls") on C, satisfying:

(a) Each path is labeled by a root alpha_{ij} of g (a "sheet crossing"
    datum, specifying which two sheets i,j of the spectral cover
    Sigma -> C are involved).

(b) The paths satisfy a differential equation: at each point p on the
    path labeled alpha_{ij}, the tangent vector v satisfies

        <lambda_{SW}^{(i)}(p) - lambda_{SW}^{(j)}(p), v> / |v| = zeta

    i.e., the paths are "WKB trajectories" for the Schrodinger equation
    with potential given by the SW differential.

(c) At branch points of Sigma -> C (where two sheets coincide), paths
    emanate. At junctions where three paths meet (labeled alpha_{ij},
    alpha_{jk}, alpha_{ik}), the labels satisfy the triangle relation.

(d) The **spectral network datum** is the collection of Stokes factors
    (formal automorphisms) carried by each path, satisfying a
    consistency condition identical to the KS wall-crossing formula.

### 4.2 Spectral networks ARE scattering diagrams

The identification is:

| Spectral network (GMN) | Scattering diagram (GS/KS) |
|------------------------|---------------------------|
| Curve C (UV curve) | Base of scattering diagram |
| Paths on C (WKB trajectories) | Walls |
| Root labels alpha_{ij} | Wall labels (charge vectors) |
| Stokes factors | Wall-crossing automorphisms |
| Branch points | Codimension-2 joints |
| Junction conditions | Consistency (trivial monodromy) |
| Phase zeta | Choice of half-plane for ordering |

This identification was observed by Bridgeland (2017) and made precise
in the work of Bridgeland-Smith (arXiv:1302.7030): for a meromorphic
quadratic differential phi_2 on C (the SU(2) case), the spectral network
is the WKB triangulation, and the scattering diagram is the exchange graph
of the associated cluster algebra (= the Bridgeland stability space
Stab(C) for the CY3 category associated to the quadratic differential).

### 4.3 Vertex algebras at the junctions

The **vertex enrichment** for the Higgs(C) case:

At each junction of the spectral network (where three paths labeled
alpha_{ij}, alpha_{jk}, alpha_{ik} meet), the local vertex algebra is:

- For G = SL(2): the junction is a branch point, and the local vertex
  algebra is the **free boson** vertex algebra (equivalently, the
  Heisenberg VOA), reflecting the fact that the Hitchin system near a
  simple branch point is locally a free field.

- For G = SL(N): the junctions are more complex. The local vertex
  algebra at a junction where N sheets meet is related to the **W_N
  algebra** (the Casimir W-algebra of sl_N). More precisely, the
  intertwiner at a junction is a screened vertex operator in the
  W_N-algebra Coulomb gas realization.

- For general G: the local vertex algebra is the **principal W-algebra
  W(g)**, and the junction intertwiner is a Wakimoto-type vertex
  operator.

**This is consistent with the AGT correspondence**: for the class S
theory on C, the partition function is computed by conformal blocks
of W(g) on C (Alday-Gaiotto-Tachikawa for G = SL(2), its extension
to SL(N) by Wyllard, and the general case by Braverman-Feigin-Finkelberg-
Nakajima). The conformal blocks ARE the compositions of intertwiners
at the junctions of the spectral network.

**Key insight**: The vertex-enriched scattering diagram for Higgs(C) is
nothing but the conformal block decomposition of the W-algebra on C,
viewed through the lens of spectral networks.

### 4.4 The CY_2 vs CY_3 perspective

As developed in `theory_higgs_cy2_qvcg.tex`, the Higgs moduli space
Higgs(C) = Coh(T*C) is a CY_2 category, and the E_2 structure arises
directly from the S^2-framing. The spectral network is the scattering
diagram for this CY_2 geometry, NOT a CY_3 scattering diagram.

The CY_2 scattering diagram is lower-dimensional: it lives on the
curve C itself (a real 2-manifold), rather than in a higher-dimensional
lattice space. The walls are 1-dimensional paths on C, and the vertices
are 0-dimensional points. This is the "surface operator" or "2d-4d"
version of the scattering diagram, related to the 4d KS scattering
diagram by the class S construction.

---

## 5. Reading off the BKM Root System from the Scattering Diagram

### 5.1 The dictionary

The BKM root system R(X) of the quantum vertex chiral group G(X)
can be read off from the scattering diagram D as follows:

| BKM root datum | Scattering diagram |
|----------------|-------------------|
| Root lattice Lambda | Lattice N underlying the scattering diagram |
| Real roots Delta^re | Walls with Weyl-reflection automorphisms (finite-order walls) |
| Imaginary roots Delta^im | Walls with non-Weyl automorphisms (infinite-order walls) |
| Root multiplicity mult(alpha) | Exponent of the wall-crossing automorphism on the wall alpha^perp |
| Weyl group W | Group generated by reflections in the real root walls |
| Weyl vector rho | The "initial scattering datum" (the seed of the iterative consistency algorithm) |
| Denominator identity Phi_X | The "partition function" of the scattering diagram |
| Simple roots Pi | Walls passing through the origin / initial walls |

### 5.2 The iterative consistency algorithm

The Gross-Siebert "consistent completion" algorithm provides a
constructive method for reading off the root system:

**Step 0**: Start with the initial scattering diagram D_0 consisting
of the simple root walls: for each simple root alpha_i in Pi, include
the wall alpha_i^perp with the automorphism determined by mult(alpha_i).

**Step 1**: Check consistency at each codimension-2 joint. Where the
monodromy is non-trivial, ADD new walls to restore consistency. The
new walls are indexed by "composite" charges gamma = n_1*alpha_1 +
n_2*alpha_2 + ..., and the multiplicity of the new wall is determined
by the BCH expansion of the monodromy.

**Step k**: Repeat. At each step, new walls of higher complexity are
added. The process converges (formally) to a consistent scattering
diagram D_infty.

**The root system is the limit**: The roots of g_X are exactly the
charges labeling the walls of D_infty. The imaginary roots are the
walls added in steps >= 1 (they are NOT present in the initial diagram
but are FORCED by the consistency condition). The multiplicities are
the exponents of the wall-crossing automorphisms.

### 5.3 The K3 x E example

For K3 x E, the initial scattering diagram D_0 has three real root
walls (delta_1^perp, delta_2^perp, delta_3^perp in Lambda^{2,1} tensor R).
The iterative completion adds imaginary root walls with multiplicities
f(nm, l) = Fourier coefficients of phi_{0,1}. The full consistent
scattering diagram D_infty has the property that its partition function
is the Igusa cusp form Delta_5.

**The Borcherds lift IS the consistent completion**: The passage from
the initial Kac-Moody data (the three simple roots) to the full BKM
superalgebra g_{Delta_5} (with all imaginary roots) is EXACTLY the
passage from D_0 to D_infty in the scattering diagram language. The
Borcherds multiplicative lift phi_{0,1} |-> Delta_5 is the analytic
incarnation of the iterative consistency algorithm.

### 5.4 Significance

This means that the BKM root system is NOT an independent datum: it is
DETERMINED by the scattering diagram (equivalently, by the MC element
Theta_A and its consistency). The root multiplicities are forced by the
consistency condition from the simple root data.

Conversely: the scattering diagram is DETERMINED by the root system
(since the walls are root hyperplanes and the automorphisms are
determined by multiplicities). So the two structures are equivalent.

**The vertex enrichment provides ADDITIONAL structure**: the local
vertex algebras at the vertices, which encode not just the
combinatorics (multiplicities) but the ALGEBRAIC structure (the OPE,
the intertwiner amplitudes, the genus-g corrections).

---

## 6. Consistency = MC Equation: The Precise Statement

### 6.1 The identification

The consistency condition for the scattering diagram (trivial monodromy
around every loop) IS the Maurer-Cartan equation

    D*Theta + 1/2[Theta, Theta] = 0

in the following precise sense:

**Theorem** (schematic; precise version in physics_wall_crossing_mc.tex,
Theorem 3.5). Let D be a scattering diagram on M_R = N tensor R with
wall data {(d_i, f_i)}. Define:

(a) The L-infinity algebra L_N associated to the lattice N with its
    skew-symmetric form <-,->.

(b) The MC element Theta_D = sum_i Omega_i * e_{n_i} in L_N, where
    n_i is the primitive normal to the wall d_i and Omega_i is the
    "multiplicity" extracted from f_i.

Then: D is consistent (trivial monodromy around all loops) if and only
if Theta_D satisfies the MC equation in L_N.

### 6.2 Codimension analysis

The MC equation has a filtration by codimension:

- **Codimension 0** (the walls themselves): The wall data f_i
  encodes the "linear" part d*Theta of the MC equation. A single
  wall is always consistent (no monodromy to check).

- **Codimension 1** (a generic point where two walls cross):
  The monodromy around the crossing point is the commutator
  [f_{i_1}, f_{i_2}], which contributes to 1/2[Theta, Theta].
  Consistency requires new walls carrying the commutator correction
  -- this is the l_2 bracket of the L-infinity algebra.

- **Codimension 2** (a point where three or more walls cross):
  Higher L-infinity operations l_3, l_4, ... contribute. The
  consistency at codimension-k joints requires the l_k operation
  of the L-infinity algebra.

**The full MC equation encodes consistency at ALL codimensions
simultaneously.**

### 6.3 The genus correction

The MC equation D*Theta + 1/2[Theta,Theta] = 0 is the GENUS-ZERO
consistency condition. The full modular MC equation (including
higher-genus corrections) is:

    sum_{n=0}^{infty} (1/n!) l_n(Theta, ..., Theta) = 0

where the l_n come from the modular convolution algebra g^mod_A.
The higher l_n encode:

- l_0 = curvature (genus-0 obstruction, the Weyl vector contribution)
- l_1 = differential (genus-0 deformation)
- l_2 = binary bracket (genus-0 bound states)
- l_3, l_4, ... = higher interactions (tropical limits of higher
  boundary strata of M-bar_{g,n})

The genus-g correction to the scattering diagram consistency comes
from the l_n operations involving genus-g moduli. In the shadow
tower language: the arity-r shadow Theta^{<= r}_A captures the
consistency condition truncated to interactions involving at most r
walls meeting at a joint.

### 6.4 Comparison with BCOV

As established in `physics_topological_strings.tex` (Section 3.2),
the BCOV holomorphic anomaly equation IS the MC equation projected
to genus g. So:

    Scattering diagram consistency (genus 0) = MC equation (genus 0)
    BCOV holomorphic anomaly = MC equation (genus g)
    Full consistency (all genera) = Full MC equation in g^mod_A

The vertex enrichment encodes the GENUS CORRECTIONS: the local
vertex algebra at each vertex captures not just the genus-0
intertwiner (the topological vertex) but the full genus expansion
of the local amplitude.

---

## 7. Non-Toric CY3: The Gross-Siebert Tropicalization

### 7.1 The tropical base

For a non-toric CY3 X, the scattering diagram is constructed via
the Gross-Siebert programme:

(a) Choose a **maximal degeneration** X -> Delta (a toric degeneration
    of X to a union of toric varieties X_0 = union_v X_v, glued along
    toric strata).

(b) The **dual intersection complex** B of X_0 is a topological
    manifold (typically a 3-sphere with an integral affine structure,
    minus a codimension-2 discriminant locus).

(c) The scattering diagram D lives on B, with walls given by tropical
    curves (images of holomorphic disks under the moment map).

(d) The vertex-enrichment: at each vertex v of the dual intersection
    complex (corresponding to a top-dimensional toric stratum X_v),
    the local vertex algebra is G(X_v) -- the quantum vertex chiral
    group of the local toric geometry.

### 7.2 Internal faces and genus contributions

For a non-toric CY3, the scattering diagram has **internal faces**
(codimension-1 strata of the dual intersection complex) corresponding
to compact divisors in X. These compact divisors contribute genus
corrections:

- An internal face dual to a compact divisor D with genus g(D)
  contributes an "automorphic correction" of genus g(D) to the
  scattering diagram consistency.

- In the shadow obstruction tower language: the genus-g correction obs_g(A_X)
  receives contributions from compact divisors of genus <= g.

This is the geometric origin of the imaginary root multiplicities
in the non-toric case: they come from tropical disk counts that
wrap around compact divisors.

### 7.3 The intrinsic mirror symmetry perspective

Gross-Siebert's "intrinsic mirror symmetry" (arXiv:1909.07649, 2022)
removes the need for a toric degeneration: the scattering diagram
is defined using punctured log Gromov-Witten invariants. In this
framework:

- The scattering diagram is determined by the CY category C = D^b(Coh(X))
  and a choice of "theta function" (= stability condition).

- The walls carry punctured log GW invariants (tropical counts of
  punctured curves).

- The consistency condition is the WDVV/MC equation for punctured
  invariants.

**This is the most natural framework for the vertex-enriched proposal
in the non-toric case**: the Gross-Siebert intrinsic scattering
diagram provides the combinatorial skeleton, and the vertex enrichment
adds the algebraic structure (local vertex algebras at vertices).

---

## 8. Assessment and Open Questions

### 8.1 Strengths of the proposal

(a) **Unifies toric and non-toric**: The topological vertex (toric)
    and the BKM root system (K3 x E) are both special cases of the
    vertex-enriched scattering diagram. The toric case is "trivially
    consistent" (the fan is complete); the K3 x E case requires
    non-trivial consistency (= the Borcherds lift).

(b) **The MC equation = consistency**: The central identification
    MC equation <-> scattering diagram consistency is clean and
    well-motivated from both the GS and KS perspectives.

(c) **Local vertex algebras provide new content**: The enrichment
    at vertices goes beyond the scattering diagram formalism
    (which only records the combinatorial/automorphism data) by
    attaching genuine algebraic structures (vertex algebras,
    intertwiners) that encode the full genus expansion.

(d) **Compatible with spectral networks**: For CY_2 geometries
    (Higgs moduli), the proposal reduces to the GMN spectral
    network formalism, which is well-developed and tested.

### 8.2 Genuine difficulties

(a) **Non-toric local vertex algebras are unknown**: For toric CY3,
    the local vertex algebra at each vertex is Y(gl-hat_1) -- a
    well-understood object. For non-toric CY3 (or for K3 x E), the
    local vertex algebras are NOT known. Defining them rigorously is
    a major open problem.

(b) **The scattering diagram for K3 x E is infinite-dimensional**:
    The Mukai lattice Lambda^{Muk}(K3) has rank 24. The scattering
    diagram in a 24-dimensional space is vastly more complex than the
    toric case (rank 2 or 3). No explicit construction exists.

(c) **Higher codimension is hard**: The L-infinity structure (higher
    l_n operations at higher-codimension joints) is not well-understood
    in the scattering diagram literature. The vertex enrichment
    proposal requires understanding the full L-infinity homotopy theory
    of the scattering diagram, not just the l_2 bracket.

(d) **Genus corrections are not tropicalized**: The full modular MC
    equation includes genus-g corrections. The tropical/scattering
    diagram framework is inherently genus-0 (or at best genus-0 +
    log corrections). Incorporating higher genera requires passing
    to the "quantum scattering diagram" of Mandel (2015) or the
    "theta function" approach of Gross-Siebert, but these are not
    fully developed.

### 8.3 Key open questions

(Q1) **What is the explicit scattering diagram for K3 x E?** Can the
Borcherds product Delta_5 be reconstructed from a finite initial
scattering diagram D_0 (the three real root walls) by the iterative
consistency algorithm? This would be a new proof of the Borcherds
lift that is purely combinatorial/tropical.

(Q2) **What are the local vertex algebras for K3 x E?** Are they
related to vertex algebras of the Mukai lattice (e.g., lattice vertex
algebras V_{Lambda_Muk})?

(Q3) **Can the BKM Gram matrix be read off from the scattering diagram
without knowing the BKM algebra first?** In other words: does the
scattering diagram provide an INDEPENDENT construction of the BKM
root system, or is it merely a reformulation?

(Q4) **What is the "quantum scattering diagram" that incorporates all
genera?** Is this the full modular convolution algebra g^mod_A viewed
through a tropical lens?

(Q5) **For the spectral network (Higgs(C)) case: is the vertex algebra
at each junction precisely the W-algebra W(g)?** This would connect
the vertex-enriched proposal to the AGT correspondence.

(Q6) **Is the refined topological vertex (Iqbal-Kozcaz-Vafa) the
"motivic" version of the vertex-enriched scattering diagram?** The
refinement epsilon_1 != -epsilon_2 breaks the unrefined symmetry; in
the scattering diagram language, this should correspond to a
"motivic" wall-crossing formula (Kontsevich-Soibelman motivic DT
invariants).

### 8.4 Relationship to existing monograph content

The vertex-enriched scattering diagram proposal is CONSISTENT with
and EXTENDS the existing framework in the following ways:

- `physics_wall_crossing_mc.tex` (Section 4.2): already identifies
  scattering diagram consistency with the MC equation. The vertex
  enrichment adds the local vertex algebra data.

- `physics_topological_strings.tex` (Section 4): already identifies
  the topological vertex as a "local root datum" and an intertwiner
  of Y(gl-hat_1). The vertex enrichment upgrades this to a systematic
  framework.

- `theory_generalized_root_datum.tex`: the CY root datum axioms
  (CY1-CY7) can be DERIVED from the vertex-enriched scattering
  diagram, rather than being postulated.

- `theory_automorphic_shadow.tex`: the automorphic correction =
  shadow obstruction tower identification is the analytic incarnation of the
  iterative consistency algorithm for the scattering diagram.

- `theory_cy2_cy3_fibration.tex`: the CY_2 -> CY_3 fibration via
  the Borcherds lift is the passage from a CY_2 scattering diagram
  (on a surface) to a CY_3 scattering diagram (in a 3d lattice),
  with the elliptic fiber providing the new "direction" for the lift.

---

## 9. Conclusion

The vertex-enriched scattering diagram is a compelling proposal for the
core combinatorial datum of the quantum vertex chiral group. Its main
virtues:

1. It provides a SINGLE framework that unifies the toric topological
   vertex (AKMV), the BKM root system (K3 x E, automorphic correction),
   the spectral network (Higgs moduli, class S theories), and the
   Gross-Siebert mirror symmetry programme.

2. The consistency condition = MC equation identification is natural
   and well-motivated from multiple perspectives (KS wall-crossing,
   GS tropical mirror symmetry, Bridgeland stability structures).

3. The vertex enrichment (local vertex algebras at joints) provides
   genuinely new structure beyond the bare scattering diagram, encoding
   the full genus expansion and the algebraic (non-combinatorial)
   content of the quantum vertex chiral group.

The main challenge is making this proposal precise for non-toric
geometries, where both the scattering diagram and the local vertex
algebras are much less understood than in the toric case. The K3 x E
case is the crucial test: can the Borcherds product be reconstructed
from a scattering diagram with explicit local vertex algebras?

---

## References (to be expanded)

- Gross-Siebert, "From real affine geometry to complex geometry" (2006)
- Gross-Siebert, "An invitation to toric degenerations" (2011)
- Gross-Siebert, "Intrinsic mirror symmetry" (2022)
- Gross-Hacking-Keel-Kontsevich, "Canonical bases for cluster algebras" (2018)
- Kontsevich-Soibelman, "Affine structures and non-archimedean..." (2004)
- Kontsevich-Soibelman, "Stability structures, motivic DT..." (2008)
- Bridgeland, "Scattering diagrams, Hall algebras, and stability..." (2017)
- Bridgeland-Smith, "Quadratic differentials as stability conditions" (2015)
- Gaiotto-Moore-Neitzke, "Spectral networks" (2013)
- Gaiotto-Moore-Neitzke, "Wall-crossing, Hitchin systems, and WKB" (2010)
- Aganagic-Klemm-Marino-Vafa, "The topological vertex" (2005)
- Okounkov-Reshetikhin-Vafa, "Quantum Calabi-Yau and classical crystals" (2003)
- Mandel, "Scattering diagrams, theta functions, and refined tropical curve counting" (2015)
- Borcherds, "Automorphic forms with singularities on Grassmannians" (1998)
- Gritsenko-Nikulin, "Siegel automorphic form corrections of some Lorentzian KM algebras" (1996)
