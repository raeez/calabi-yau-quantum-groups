# Research Note: The Decorated CW-Complex as Core Combinatorial Datum

## 1. Statement of the Proposal

The proposal identifies the core combinatorial datum of a CY3 quantum vertex
chiral group G(X) as a **decorated CW-complex** (or simplicial/polyhedral
complex) of dimension at most 3, where:

- **0-cells (vertices)** carry local vertex algebras (intertwiners)
- **1-cells (edges)** carry spectral parameters / gluings (tensor products of root data)
- **2-cells (faces)** carry "automorphic corrections" (Borcherds lifts, genus contributions)
- **3-cells** carry "modular data" (higher-genus amplitudes, the full shadow obstruction tower)

The proposal further specifies:

- **Toric CY3**: the CW-complex is the toric web diagram (planar graph = a 2-complex with no 3-cells, since toric CY3 has no compact 3-cycles).
- **K3 x E**: the CW-complex has vertices from the K3 lattice, edges from the root system, faces from K3 geometry (22 = h^{1,1}(K3) divisor classes), plus the elliptic fiber as a 1-cell with modular parameter tau.
- **General CY3**: the CW-complex is the dual intersection complex of a degeneration X -> Delta, as in the Gross-Siebert programme.

The key question: the tree-level topological vertex gives the 0- and 1-skeleton;
the Borcherds lift adds the 2-skeleton; **what adds the 3-skeleton?**

---

## 2. Evidence From the Codebase

### 2.1. The Toric Case: 0-Skeleton and 1-Skeleton Are Precise

The topological vertex formalism (AKMV) as developed in
`notes/physics_topological_strings.tex` (Section 4) makes the 0-cell and 1-cell
assignments precise:

**0-cells = topological vertices.** Each trivalent vertex v of the toric web
diagram carries the local quantum vertex chiral group G(C^3) = Y(gl_1-hat) =
W_{1+infty} (Construction 4.6 in the topological strings note). The vertex
amplitude C_{lambda,mu,nu}(q) is the matrix element of the chiral intertwiner
(Conjecture 4.12). The local root datum at each vertex has:
- Lattice: Lambda_v = Z (the dimension vector)
- Root multiplicities: mult_v(n) = p(n) (partitions of n)
- Denominator identity: MacMahon function M(q) = prod (1-q^n)^{-n}

**1-cells = Kahler parameters / propagators.** Each internal edge e carries:
- The Kahler parameter Q_e = exp(-t_e)
- The propagator (-Q_e)^{|lambda_e|} f_{lambda_e}(q) implementing the Fock-space
  contraction F^(v)_{lambda_e} tensor (F^(w)_{lambda_e})* -> C
- The gluing is a tensor product pairing of the Fock representations of the
  two adjacent vertex groups G_v and G_w (Construction 4.8)

The factorization formula Z(X) = sum_{lambda_e} prod_v C_{lmn}(q) prod_e
(-Q_e)^{|lambda|} f_lambda(q) is literally the partition function computed by
summing over 1-cell labelings with fixed 0-cell amplitudes.

This matches the proposal exactly: toric CY3s (which have no compact 4-cycles,
hence no compact 3-cycles) produce a planar graph with no 3-cells.

**What about 2-cells for toric CY3?** The toric web diagram is planar, so it
bounds faces. For toric CY3 without compact divisors (e.g., C^3, conifold),
these faces correspond to non-compact divisors and carry no additional data.
For toric CY3 with compact divisors (e.g., local P^2 has h^{1,1} = 1 compact
divisor), the faces carry the DT invariants of curves within the compact
divisor. The root datum of the toric CY3 (`notes/theory_generalized_root_datum.tex`,
Construction 7.1) identifies:
- Real roots = vertices of the toric diagram (compact divisors)
- Imaginary roots = dimension vectors with nonzero DT invariant
- mult(d) = DT_d(X)

So the 2-cells, when present, carry the imaginary root data. This is consistent
with the proposal that 2-cells carry "automorphic corrections."

### 2.2. The K3 x E Case: 0-Skeleton Through 2-Skeleton Are Precise

The K3 x E tower (`chapters/examples/k3_times_e.tex`,
`notes/theory_cy2_cy3_fibration.tex`) provides the most detailed instantiation.

**0-cells: real simple roots.** The three real simple roots delta_1, delta_2,
delta_3 with Gram matrix ((2,-2,-2),(-2,2,-2),(-2,-2,2)) are the vertices of
the fundamental polyhedron P_{II} in hyperbolic space H^1. These correspond
to (-2)-curves in the K3 surface -- the vertices of the CW-complex.

**1-cells: edges of the Gram matrix.** The off-diagonal entries (delta_i, delta_j)
= -2 encode the 1-skeleton. Each pair of real simple roots connected by a
nonzero inner product corresponds to an edge. The elliptic fiber adds one
more 1-cell with modular parameter tau (the new lattice direction
Lambda_E^vee from the fibration construction, contributing the variable
sigma to the Siegel upper half-space H_2).

**2-cells: the Borcherds lift / automorphic correction.** The passage from the
CY2 root datum to the CY3 root datum via the Borcherds multiplicative lift
(`notes/theory_cy2_cy3_fibration.tex`, Construction 3.4) is precisely the
addition of the 2-skeleton. The Borcherds lift takes:
- Input: phi_{0,1} (K3 elliptic genus, a weak Jacobi form)
- Output: Delta_5 (Igusa cusp form, a Siegel modular form)

The 2-cells carry the imaginary root multiplicities mult_3(n,l,m) = f(nm,l).
In the shadow obstruction tower language (`notes/theory_automorphic_shadow.tex`), this is:
- Arity 2 captures the real roots (0-skeleton + 1-skeleton)
- Arity 3 captures depth-1 imaginary roots (first layer of 2-cells)
- Arity r captures depth <= r-2 roots (progressive filling of 2-cells)

The 22 = h^{1,1}(K3) divisor classes provide a natural count of independent
2-cells: these are the 22 directions in H^{1,1}(S) that govern the
K3 lattice structure, and the isotropic imaginary roots at multiplicity 20
(= f(0,0) = 20 from phi_{0,1}, corresponding to the 20 transverse directions
in H^{1,1}(S) after fixing the Kahler class) confirm this numerology.

### 2.3. The Shadow Tower Provides a Natural Filtration By Skeleton

The identification "automorphic correction = shadow obstruction tower"
(`notes/theory_automorphic_shadow.tex`, Theorem 1.1) provides a natural
stratification that aligns with the CW-complex skeletal filtration:

| Shadow arity | Root depth | CW skeleton | Data |
|---|---|---|---|
| r = 2 (kappa) | Real roots (depth 0) | 0-skeleton + 1-skeleton | Gram matrix, Weyl vector |
| r = 3 (cubic C) | Depth 1 imaginary | First 2-cells | First Borcherds correction |
| r = 4 (quartic Q) | Depth 2 imaginary | More 2-cells | Higher Borcherds corrections |
| r -> infinity | All imaginary roots | Full 2-skeleton | Complete automorphic form |
| genus g >= 1 | Higher-genus data | 3-cells (?) | Modular amplitudes |

The first four rows are rigorously established in the codebase. The last row
is the open question.

### 2.4. The Scattering Diagram Connection (Gross-Siebert)

The wall-crossing note (`notes/physics_wall_crossing_mc.tex`, Section 5.2)
explicitly identifies the Kontsevich-Soibelman scattering diagram -- the
central object of the Gross-Siebert programme -- with a **tropical
L-infinity algebra** obtained from the modular convolution algebra by
tropicalization (replacing moduli of curves by their dual intersection
complexes). Specifically:

- Each wall in the scattering diagram labeled by gamma corresponds to a
  summand Omega(gamma) * Theta_gamma^prim * x^gamma in the MC element.
- The consistency condition (trivial monodromy around codimension-2 joints)
  IS the MC equation.
- Higher L-infinity terms l_n correspond to higher-codimension joints
  where n walls meet.

This directly connects the proposal's "CW-complex = dual intersection complex
of a degeneration" to the existing framework. The Gross-Siebert reconstruction
theorem says the CY3 is determined by tropical data (the CW-complex +
decorations), and the MC equation of the shadow obstruction tower is precisely the
consistency condition for these tropical data.

---

## 3. Analysis of the Key Question: What Adds the 3-Skeleton?

### 3.1. The Dimensional Argument

For a CY3 X, the relevant homology is:
- H_0(X) ~ Z: one point (controls nothing, or rather the overall normalization)
- H_2(X) ~ Z^{h^{1,1}}: curve classes, controlled by Kahler parameters (1-cells)
- H_4(X) ~ Z^{h^{1,1}}: divisor classes, dual to curves (2-cells)
- H_6(X) ~ Z: the fundamental class
- H_3(X) ~ Z^{2h^{2,1}+2}: the intermediate Jacobian (3-cycles)

The 3-cycles (H_3) are where the B-model complex structure moduli live.
The complex structure moduli space M_cpx of dimension h^{2,1} carries the
special Kahler geometry and the period map. These are precisely the data
NOT captured by the tree-level (genus-0) topological vertex.

### 3.2. What Data Lives on 3-Cells?

Examining the codebase structures:

**(A) Higher-genus amplitudes.** The genus-g free energy F_g
(`notes/physics_topological_strings.tex`) contains data beyond the root
multiplicities. The GV invariants n^g_beta for g > 0 are the "genus-g
refinements of the root multiplicity" (Remark 2.5 of that note). These
are not captured by any finite arity of the shadow obstruction tower -- they require
the full modular structure. The BCOV holomorphic anomaly equation
(Section 3.2) shows that F_g for g >= 1 involves anti-holomorphic data
from the B-model complex structure moduli, which are controlled by
3-cycles.

**(B) The modular convolution algebra.** The L-infinity algebra
g^mod_A has operations l_n coming from boundary strata of M-bar_{g,n}
(`notes/physics_wall_crossing_mc.tex`, Section 2.2). The genus-g
contributions to the MC element Theta_A involve sections over M-bar_{g,n},
which for g >= 1 introduce genuinely new data (the Hodge bundle, lambda
classes). These are the genus-g obstructions obs_g(A_X) = kappa * lambda_g
on the uniform-weight lane, with higher terms from shadow corrections.

**(C) The B-model period data.** The special geometry of the CY moduli
space (`notes/physics_topological_strings.tex`, Section 3.1) involves:
- Period matrix tau_{ij}
- Propagator S^{ij} (the genus-1 annulus amplitude)
- Yukawa coupling C_{ijk} (genus-0 3-point function)

The propagator and the Yukawa coupling are the homotopy transfer data for
the Hodge-to-de Rham spectral sequence on PV^{*,*}. The propagator
specifically mediates degeneration of genus-g surfaces into lower genera
by pinching a cycle -- this is precisely the data that relates different
genera, and it comes from the 3-cycle structure of X.

### 3.3. The Answer: 3-Cells Carry the Full Modular/Higher-Genus Data

The evidence supports the following precise identification:

**The 3-skeleton is added by the genus expansion (higher-genus amplitudes).**

More specifically:

1. The **0-skeleton** is the tree-level data at genus 0: local vertex algebras,
   the collision r-matrix, the Weyl vector. This is the arity-2 shadow obstruction tower.

2. The **1-skeleton** is the gluing data: Kahler parameters, edge propagators,
   tensor product pairings. This is still arity-2 but encodes the combinatorial
   connectivity.

3. The **2-skeleton** is the automorphic correction: imaginary root
   multiplicities from the Borcherds lift (for K3 x E) or DT invariants (for
   toric CY3). This is the arity >= 3 part of the shadow obstruction tower at genus 0.
   For a toric CY3 with no compact 3-cycles, this is the full story.

4. The **3-skeleton** is the higher-genus data: the genus-g free energies F_g
   for g >= 1, the BCOV propagator, the modular completion. This corresponds to:
   - The genus expansion of the shadow obstruction tower Theta_{A_X} = sum_g hbar^{2g-2} Theta^(g)
   - The B-model complex structure moduli (periods of 3-forms)
   - The non-holomorphic completion required by the holomorphic anomaly

**The genus-0 shadow obstruction tower (all arities, genus 0) gives the 2-skeleton.
The genus >= 1 shadow obstruction tower gives the 3-skeleton.**

### 3.4. Why Toric CY3 Has No 3-Cells

For a toric CY3 without compact 4-cycles:
- h^{2,1} = 0 (no complex structure deformations)
- There are no compact 3-cycles
- The B-model is trivial (no periods to compute)
- The BCOV equation degenerates: F_g for g >= 1 are determined entirely
  by genus-0 data via the propagator, which is algebraic (no non-holomorphic
  completion needed)
- The shadow obstruction tower at higher genus reduces to kappa * lambda_g (the
  uniform-weight lane), which is determined by kappa = chi(X)/2 alone

This is consistent with the proposal: toric CY3s are 2-complexes because
their topology has no room for 3-cells.

### 3.5. Why K3 x E Has (Implicit) 3-Cells

For K3 x E:
- h^{2,1} = 0 for the generic K3 x E (the product preserves h^{2,1}(K3) = 0,
  h^{2,1}(E) = 0, but the Kunneth formula gives h^{2,1}(K3 x E) = h^{1,1}(K3)
  * h^{0,1}(E) + h^{2,0}(K3) * h^{0,1}(E) = 20 * 1 + 1 * 1 = 21)
- Actually h^{2,1}(K3 x E) = 21, so there are 21 complex structure moduli
- The Siegel modular form Delta_5 lives on H_2, a genus-2 object
- The genus-2 structure IS the 3-cell data: it encodes the full modular
  information beyond the Borcherds lift

The Siegel upper half-space H_2 parameterized by Z = ((tau, z), (z, sigma))
has three complex dimensions. The genus-2 Siegel modular form Delta_5 is a
function on this 3-dimensional space. The three directions correspond to:
- tau (base moduli) -- from the 1-skeleton
- z (fiber moduli) -- from the elliptic variable  
- sigma (elliptic curve moduli) -- from the fibration

The 3-cell data is the full dependence on all three variables simultaneously,
which cannot be recovered from lower-dimensional projections. This is the
content of the Borcherds lift: it takes a function of two variables (the
Jacobi form phi_{0,1}(tau, z)) and produces a function of three variables
(Delta_5(tau, z, sigma)). The third direction (sigma) is added by the
fibration over E, which geometrically introduces a compact 3-cycle.

---

## 4. The Gross-Siebert Connection

### 4.1. The Dual Intersection Complex

For a general CY3, the proposal identifies the CW-complex with the dual
intersection complex of a maximal degeneration X -> Delta. This is the
central object of the Gross-Siebert programme:

- A large complex structure limit (LCSL) degeneration X -> Delta produces
  a singular central fiber X_0 with normal crossing singularities.
- The dual intersection complex B = B(X_0) is a real 3-dimensional topological
  space (for a CY3) with an integral affine structure on B \ Delta, where
  Delta is the discriminant locus.
- The Gross-Siebert reconstruction theorem says: X is determined (up to
  deformation equivalence) by the data (B, affine structure, scattering
  diagram on B).

### 4.2. The Scattering Diagram as MC Data

The codebase already identifies scattering diagrams with MC data
(`notes/physics_wall_crossing_mc.tex`, Section 5.2). The consistency
condition for scattering diagrams is the MC equation. This means:

- The **base** B of the SYZ fibration (the dual intersection complex)
  is the underlying CW-complex.
- The **affine structure** on B encodes the lattice Lambda(X) and the
  Kahler/complex structure moduli.
- The **scattering diagram** on B is the shadow obstruction tower Theta_A: its walls
  are codimension-1 strata decorated by BPS multiplicities (root data),
  and its consistency is the MC equation.

### 4.3. Stratification of the Dual Intersection Complex

For a CY3 degeneration, the dual intersection complex B has a natural
stratification:

- **Vertices** (0-cells) of B: triple points of X_0 (where three
  irreducible components meet). These correspond to local C^3 patches
  and carry the topological vertex data.
  
- **Edges** (1-cells) of B: double curves of X_0 (where two components
  meet). These carry the gluing data / propagators / Kahler parameters.
  
- **Faces** (2-cells) of B: irreducible components of X_0 (smooth
  surfaces). These carry the "automorphic corrections" -- the BPS data
  of curves within each component.
  
- **3-cells** of B: exist only when B is a genuine 3-manifold (not a
  2-complex). For a toric CY3, B is a 2-complex (the fan), so no 3-cells.
  For a compact CY3 with h^{2,1} > 0, B is a 3-manifold (typically S^3 or
  a connected sum), and the 3-cells carry the period data / complex
  structure moduli / higher-genus amplitudes.

### 4.4. The SYZ Picture

Under mirror symmetry / SYZ, the CY3 X admits a special Lagrangian
T^3 fibration X -> B. The base B is the dual intersection complex.
The fibers are T^3 tori, and:

- Over the smooth part of B: the fibers are smooth T^3
- Over the discriminant locus Delta in B: the fibers degenerate
- The period map (from H_3(X) to the intermediate Jacobian) is encoded
  in the affine structure of B

The 3-cells of B carry the data of how the T^3 fibers fit together
globally -- this is precisely the period/modular data of the CY3.

---

## 5. Precise Formulation of the Decorated CW-Complex

### 5.1. Definition

For a CY3 X with a chosen degeneration X -> Delta, define the
**decorated CW-complex** D(X) as follows:

**Underlying space**: B = B(X_0), the dual intersection complex of the
central fiber, with its integral affine structure on B \ Delta.

**0-cell decoration**: To each vertex v of B, attach the local quantum
vertex chiral group G_v = G(C^3) with:
- The affine Yangian Y(gl_1-hat) structure
- The topological vertex C_{lambda,mu,nu}(q) as intertwiner
- The MacMahon function M(q) as local denominator

**1-cell decoration**: To each edge e of B connecting vertices v, w, attach:
- The Kahler parameter Q_e = exp(-t_e) (area of the P^1 connecting the
  two C^3 patches)
- The propagator F^(v)_{lambda} tensor (F^(w)_{lambda})* -> C implementing
  the tensor product pairing
- For the K3 x E elliptic fiber: the modular parameter tau

**2-cell decoration**: To each face f of B, attach:
- The BPS multiplicities mult(alpha) for curves alpha within f
- The Borcherds lift data: the Jacobi form phi_{0,m} encoding the
  elliptic genus of the surface component
- The DT invariants of the corresponding surface class

**3-cell decoration**: To each 3-cell c of B (when B is a 3-manifold), attach:
- The period matrix of the CY3 restricted to the 3-cycles dual to c
- The genus-g free energies F_g for g >= 1, encoding higher-genus
  amplitudes
- The BCOV propagator S^{ij} and its modular completion
- The full shadow obstruction tower Theta_{A_X} beyond genus 0

### 5.2. Recovery of the Root Datum

The generalized CY3 root datum R(X) = (Lambda, Delta, mult, W, rho) is
recovered from D(X) as follows:

- **Lambda**: the lattice generated by 1-cells (Kahler classes) and
  extended by 2-cell data (divisor classes). For toric CY3: Lambda =
  Z^{Q_0} from the quiver. For K3 x E: Lambda = Lambda^{3,2}.

- **Delta^re**: the real simple roots correspond to 0-cells with
  self-intersection 2 (vertices of the polyhedron). The Gram matrix
  is read off from the 1-cell connectivity.

- **mult**: imaginary root multiplicities come from 2-cell decorations
  (BPS invariants / Fourier coefficients of the Jacobi form).

- **W**: the Weyl group is generated by reflections in the 0-cell data
  (symmetries of the polyhedron).

- **rho**: the Weyl vector is determined by the normalization condition
  (rho, delta_i) = -1 on real simple roots.

### 5.3. Recovery of the Shadow Tower

The shadow obstruction tower Theta_{A_X} is recovered from D(X) by progressive
assembly:

- **Arity 2** (0-skeleton + 1-skeleton): the collision r-matrix and kappa.
  This is the tree-level Kac-Moody algebra before automorphic correction.

- **Arity >= 3** (2-skeleton): the imaginary root corrections at genus 0.
  These come from 2-cell decorations via the Borcherds lift.

- **Genus >= 1** (3-skeleton): the higher-genus shadow amplitudes.
  These come from 3-cell decorations encoding the modular/period data.

---

## 6. Critical Assessment

### 6.1. What Works Well

1. **Toric case is clean.** The identification 0-cells = topological vertices,
   1-cells = Kahler parameters, 2-cells = compact divisors is rigorous and
   matches the AKMV formalism exactly.

2. **K3 x E case is mostly clean.** The real simple roots (0-cells), Gram
   matrix (1-cells), and Borcherds lift (2-cells) fit naturally. The Siegel
   modular form Delta_5 living on H_2 (a 3-dimensional space) provides
   indirect evidence for 3-cells.

3. **Scattering diagram = MC equation** is already established in the
   codebase. This connects the Gross-Siebert programme directly to the
   shadow obstruction tower framework.

4. **The dimensional numerology works.** A CW-complex of dimension <= 3
   matches the dimension of CY3; the skeletal filtration matches the
   shadow obstruction tower arity filtration at genus 0 and extends to genus >= 1
   via 3-cells.

### 6.2. What Needs Work

1. **The 3-cell assignment is not as crisp as 0-1-2.** For 0-cells, 1-cells,
   and 2-cells, there are precise mathematical objects being attached. For
   3-cells, the assignment "higher-genus amplitudes / full modular data" is
   more diffuse. One needs a precise definition of what data decorates a
   3-cell.

2. **The Gross-Siebert reconstruction theorem** gives the CY3 from
   tropical data on a 3-manifold B, but the precise relationship between
   the scattering diagram consistency (MC equation on the tropical
   L-infinity algebra) and the shadow obstruction tower MC equation (on the modular
   convolution algebra) needs rigorous development. The codebase identifies
   these at the motivational level but flags this as needing "a rigorous
   proof at the chain level" (`notes/physics_4d_n2_hitchin.tex`, line 890).

3. **The K3 x E case obscures the 3-cell structure** because the Borcherds
   lift packages all the data into a single automorphic form (Delta_5). The
   separation of the 2-skeleton (imaginary roots at genus 0) from the
   3-skeleton (genus >= 1 corrections) is implicit in the genus expansion
   but not explicitly developed in the codebase.

4. **Non-fibered CY3s** (like the quintic) are acknowledged as problematic
   (`notes/theory_generalized_root_datum.tex`, Remark after Conjecture 7.4):
   "The truly non-trivial cases are compact CY3s with no elliptic fibration
   structure, such as the quintic threefold in P^4; for these, the root
   datum (if it exists in the BKM sense) is not well understood."

5. **The proposal conflates two notions of "CW-complex."** For toric CY3,
   it is the toric web diagram (a graph in R^2). For Gross-Siebert, it is
   the dual intersection complex (a topological space of real dimension
   dim_C(X) = 3). These are different objects with different dimensions.
   The reconciliation requires identifying the toric web diagram as a
   degenerate case of the Gross-Siebert dual complex (a 2-complex rather
   than a 3-manifold).

### 6.3. Conjectural Refinement

Based on the analysis, I propose the following refinement:

**Conjecture (Skeletal Shadow Correspondence).** Let X be a CY3 with dual
intersection complex B = B(X_0) from a maximal degeneration. Let
Theta_{A_X} = sum_{g,r} Theta^{(g,r)} be the bi-graded shadow obstruction tower
(by genus g and arity r). Then:

(a) The genus-0, arity-2 component Theta^{(0,2)} is determined by
    the 0-skeleton and 1-skeleton of B (vertices + edges + decorations).

(b) The genus-0, arity >= 3 components Theta^{(0,r)} for r >= 3 are
    determined by the 2-skeleton of B (faces + decorations), via the
    Borcherds lift when B arises from a K3 fibration.

(c) The genus >= 1 components Theta^{(g,*)} for g >= 1 are determined
    by the 3-skeleton of B (when B is a 3-manifold), via the BCOV
    propagator and modular completion.

(d) When B is a 2-complex (toric case, h^{2,1} = 0), the genus >= 1
    components are determined by genus 0 via the uniform-weight lane
    obs_g = kappa * lambda_g, and no 3-cells are needed.

(e) The dimension of the space of 3-cell decorations equals h^{2,1}(X),
    the number of complex structure moduli.

---

## 7. Connections to Open Problems

### 7.1. Problem P2 (The Quintic Root Datum)

The quintic has h^{1,1} = 1, h^{2,1} = 101. In the decorated CW-complex
picture:
- The 0-skeleton has very few vertices (perhaps just one, from the
  unique Kahler class)
- The 1-skeleton is minimal
- The 2-skeleton encodes one compact divisor class
- The 3-skeleton must carry 101 complex structure parameters

This suggests the quintic's CW-complex is "mostly 3-cells" -- the dominant
contribution comes from the modular/period data, not from the tree-level
root datum. This is consistent with the difficulty of constructing the
quintic root datum: the interesting structure is in the 3-skeleton, which
is precisely the higher-genus data that is hardest to compute.

### 7.2. Problem P4 (Wall-Crossing as Weyl Chamber Crossing)

Wall-crossing changes the BPS spectrum as stability parameters vary. In
the CW-complex picture, this corresponds to a change of fundamental
polyhedron P -> P' within the same Weyl group W. The 0-skeleton and
1-skeleton change (different choice of real simple roots), but the
2-skeleton (total imaginary root content, measured by the denominator
identity) is gauge-invariant. The 3-skeleton (higher-genus amplitudes)
is gauge-invariant too (it depends only on the MC equivalence class).

This matches Proposition 3.5 in the wall-crossing note: the bar-complex
Euler product Phi_X depends only on the gauge equivalence class, not on
the representative.

### 7.3. Problem P6 (Higher CY Root Data)

For CY_d with d > 3, the CW-complex should have dimension <= d. The
pattern would be:
- 0-cells to (d-3)-cells: tree-level / genus-0 root datum
- (d-2)-cells: automorphic corrections (Borcherds lift)
- (d-1)-cells: one-loop corrections
- d-cells: full modular data

For CY4 (d = 4), the CW-complex has dimension <= 4, and the
"Borcherds lift" should be replaced by a lift from Siegel modular forms
to automorphic forms on a higher-dimensional domain.

---

## 8. Summary

The proposal that the core combinatorial datum is a decorated CW-complex
is well-supported by the existing codebase, with the following caveats:

1. **The 0-1-2 skeleton story is clean and rigorous** for both toric CY3s
   (via AKMV) and K3 x E (via Borcherds lift).

2. **The 3-skeleton story is conceptually correct but not yet rigorous.**
   The 3-cells carry higher-genus / modular / period data, and their
   existence is controlled by h^{2,1}(X). The precise decoration of a
   3-cell should be the BCOV propagator data restricted to the corresponding
   portion of the complex structure moduli space.

3. **The Gross-Siebert dual intersection complex** is the correct general
   framework, and the connection to the shadow obstruction tower MC equation (via
   tropicalization of the modular convolution algebra) is already
   anticipated in the codebase.

4. **The key open problem** is making the 3-cell decoration precise:
   what exactly decorates a 3-cell in a way that (a) recovers the
   BCOV holomorphic anomaly equation, (b) is compatible with the MC
   equation, and (c) reduces to the known data in the toric and K3 x E
   cases?

### Answer to the Key Question

> The tree-level topological vertex gives the 0- and 1-skeleton. The Borcherds
> lift adds the 2-skeleton. What adds the 3-skeleton?

**The 3-skeleton is added by the genus >= 1 shadow obstruction tower -- the BCOV
holomorphic anomaly / modular completion data.** Concretely:
- The BCOV propagator S^{ij} (genus-1 data) provides the basic 3-cell
  gluing.
- The higher-genus free energies F_g (computed recursively via BCOV)
  fill in the 3-cell decorations.
- The non-holomorphic completion (the anti-holomorphic dependence of F_g
  on complex structure moduli) is the genuinely new 3-cell datum that
  cannot be recovered from the 2-skeleton.
- The dimension of the 3-cell decoration space is h^{2,1}(X), matching
  the number of complex structure moduli.
- When h^{2,1} = 0 (toric CY3), there are no 3-cells and the higher-genus
  data is determined by genus 0, consistent with the proposal.
