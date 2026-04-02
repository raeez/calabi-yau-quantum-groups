# Synthesis: The CY Combinatorial Datum

## Raeez Lorgat, 2 April 2026

### Status of the COMB agent notes

No research notes from agents COMB-1 through COMB-9 were found. This synthesis
is therefore written from the existing theory notes
(theory_generalized_root_datum.tex, theory_automorphic_shadow.tex,
theory_cy2_cy3_fibration.tex, theory_coha_e1_sector.tex,
theory_higgs_cy2_qvcg.tex), the VISION.md document, the working_notes.tex,
and the compute modules, together with the mathematical literature on each
candidate.

---

## 1. Evaluation of the nine candidates

### Candidate 1: Decorated bipartite graphs / brane tilings

**What it is.** A bipartite graph on a torus T^2 (a "dimer model") encoding the
quiver with potential (Q, W) of a toric CY3. Vertices are black/white (gauge
groups), edges are bifundamental fields, faces are terms of the superpotential.

**Toric CY3 (topological vertex)?** YES -- this is the native habitat. The
dimer model is the combinatorial dual of the toric diagram. For C^3 it gives
the hexagonal dimer; for the conifold, the square dimer. Perfect matchings
biject with lattice points of the toric diagram. The topological vertex
computation factorizes over vertices of the brane tiling.

**K3 x E (BKM / Delta_5)?** NO -- brane tilings are intrinsically toric and
periodic. K3 x E is not toric; there is no natural bipartite graph on a torus
encoding the K3 lattice Lambda^{2,1}_{II}. One could attempt to use an orbifold
approximation, but the data of root multiplicities from phi_{0,1} has no known
dimer encoding.

**Higgs(C) (Yangian / elliptic Hall)?** PARTIAL -- for C = T^2 (genus 1),
the Higgs moduli space of rank-1 sheaves on T^* T^2 can be described via a
dimer on T^2, giving the elliptic Hall algebra multiplication. For general
curves: no.

**Tree-level data?** YES -- vertices are intertwiners, edges are gluings.
This is exactly the RSYZ gluing of affine Yangians along bimodules.

**Loop-level data?** PARTIAL -- faces carry superpotential terms (tree-level
F-terms). The torus periodicity encodes the compactness of the base, but the
automorphic correction (imaginary roots from the Borcherds lift) is not visible
in the dimer.

**Computable?** YES -- mature algorithms (zigzag paths, Kasteleyn matrix,
perfect matching enumeration). Already have compute/lib/topological_vertex.py.

**Presentable?** YES -- clean combinatorial definition.

**Verdict:** Strong for toric CY3 (Level 1 data), fails for K3 x E and
higher-genus Higgs. A Level 1 object, not the full datum.

---

### Candidate 2: Vertex-enriched scattering diagrams

**What it is.** A scattering diagram in the sense of Kontsevich-Soibelman and
Gross-Siebert: a collection of walls (codimension-1 cones in a real vector
space) carrying automorphisms of a formal torus algebra, together with a
consistency condition (the composition of wall-crossing automorphisms around any
loop is trivial). "Vertex-enriched" means the data at vertices (intersections
of walls) is promoted from a simple product to a decorated intertwiner (a
higher operation in the factorization algebra).

**Toric CY3?** YES -- the Kontsevich-Soibelman scattering diagram for the
quiver (Q, W) of a toric CY3 encodes the DT invariants. The walls are in the
space of stability conditions; the wall-crossing automorphisms are the KS
factors. For C^3, this reduces to the single wall carrying the MacMahon
function.

**K3 x E?** YES, in principle -- the scattering diagram for K3 x E lives in
the space R^{2,1} (the hyperbolic space of Lambda^{2,1}_{II}). The walls are
the hyperplanes orthogonal to real roots delta_i, and the imaginary root
contributions are encoded in the wall-crossing automorphisms. The Borcherds
product formula IS the consistent scattering diagram. However: this
identification has not been made explicit in the literature.

**Higgs(C)?** YES -- Bridgeland's scattering diagrams for stability conditions
on D^b(Coh(T^*C)) recover the Yangian (genus 0) and elliptic Hall (genus 1)
R-matrices. The walls are the walls of marginal stability in the space of
Bridgeland stability conditions.

**Tree-level data?** YES -- the initial scattering diagram (before
consistency/completion) consists of the walls from real simple roots. These are
the tree-level data: the r-matrix poles.

**Loop-level data?** YES -- the consistency algorithm GENERATES new walls,
which are exactly the imaginary root contributions. The completed scattering
diagram IS the automorphic correction. Each new wall corresponds to an imaginary
root, and its attached automorphism encodes mult(alpha). The completion
algorithm IS the shadow tower: the n-th step of the completion adds walls
corresponding to arity-n roots.

**Computable?** YES -- the KS completion algorithm is iterative and
termination is guaranteed order-by-order. Already have the WKB denominator
module (compute/lib/wkb_denominator.py) and the BKM shadow tower module
(compute/lib/bkm_shadow_tower.py), which are essentially computing scattering
diagram completions.

**Presentable?** YES -- scattering diagrams have a clean axiomatic definition
(Gross-Siebert, KS). The enrichment at vertices needs specification.

**Verdict:** The strongest single candidate. Carries both tree-level and
loop-level data. Specializes to all three test geometries. The completion
algorithm = shadow tower. But: it is a Level 1+2 object (lattice + scattering
walls + corrections), not the full modular/genus data.

---

### Candidate 3: Decorated CW-complexes

**What it is.** A CW-complex (or more precisely, a CW-structure on a
topological space) where cells carry algebraic decorations: 0-cells = lattice
points (charge vectors), 1-cells = morphisms (gluings/intertwiners), 2-cells =
relations (automorphic corrections), 3-cells = syzygies (higher-genus data).

**Toric CY3?** YES -- the moment polytope of a toric CY3 is a 3-dimensional
polytope, and its face structure is a CW-complex. Vertices = fixed points,
edges = T-invariant curves, faces = T-invariant divisors, 3-cell = the open
orbit.

**K3 x E?** PARTIAL -- there is no canonical CW structure on the moduli
space. One could use the Voronoi decomposition of the hyperbolic space
H^{s-1} with respect to the Weyl group, but this is more naturally a scattering
diagram.

**Higgs(C)?** PARTIAL -- the Hitchin base has a natural stratification (the
Hitchin discriminant), but promoting this to a decorated CW-complex requires
additional choices.

**Tree / Loop / Computable / Presentable?** The CW-complex is too general --
it is a language rather than a structure. Any of the other candidates can be
described as a decorated CW-complex. The question is what the specific
decorations ARE, and those are determined by the other candidates.

**Verdict:** Framework, not a specific proposal. The hierarchy of cells
(0/1/2/3) does map to the hierarchy of levels (lattice/tree/surface/volume),
confirming the multi-level structure. But the CW-complex is the CONTAINER, not
the CONTENT.

---

### Candidate 4: Quivers with enriched potential

**What it is.** A quiver Q = (Q_0, Q_1) with a potential W in CQ/[CQ, CQ],
enriched by additional data: a grading on the lattice Z^{Q_0}, stability
conditions, and a "higher potential" encoding the automorphic correction.

**Toric CY3?** YES -- native habitat. The quiver with potential (Q, W) encodes
the CY3 category as Rep(Q, dW = 0). For C^3: Jordan quiver with cubic
potential. For conifold: Klebanov-Witten quiver. Already have the construction
in theory_generalized_root_datum.tex, Section "The toric case."

**K3 x E?** NO for a naive quiver -- K3 x E does not arise from a quiver with
potential in the classical sense. However: the BKM Lie superalgebra g_{Delta_5}
HAS a presentation by generators and relations, and the Gram matrix
((2,-2,-2),(-2,2,-2),(-2,-2,2)) can be viewed as the "adjacency matrix" of a
generalized quiver with 3 vertices and negative edge weights. The "enriched
potential" would need to encode the imaginary root multiplicities from
phi_{0,1}, which goes beyond the classical quiver-with-potential framework.

**Higgs(C)?** PARTIAL -- the preprojective algebra of a quiver is the special
case W = sum [a, a*]. For genus 0 (Higgs on P^1), quivers suffice. For genus 1,
one needs the "elliptic" quiver (a quiver on a torus), which is essentially a
brane tiling.

**Tree-level data?** YES -- the quiver IS the tree-level data (vertices =
intertwiners, arrows = gluings).

**Loop-level data?** PARTIAL -- the potential W encodes tree-level (F-term)
relations. The "enriched" part would need to include the automorphic correction.
The natural enrichment: promote W to a curved A-infinity structure, where the
curvature terms encode imaginary roots. This is exactly the bar-cobar machine
of Volume I.

**Computable?** YES -- quiver representation theory is highly algorithmic.

**Presentable?** YES -- clean definition.

**Verdict:** The quiver is Level 1 data. The potential is the beginning of
Level 2. The "enrichment" (curving the A-infinity structure) is the shadow
tower. This candidate is correct but incomplete -- it needs the full
A-infinity/BKM enrichment to capture the automorphic correction.

---

### Candidate 5: BPS graphs / spectral networks

**What it is.** A spectral network (Gaiotto-Moore-Neitzke) on a surface C:
a collection of walls on C emanating from branch points of a spectral cover
Sigma -> C, carrying BPS state data. BPS graphs are the degenerate limits
(maximal degeneration) where the network forms a graph.

**Toric CY3?** PARTIAL -- spectral networks are native to 4d N=2 theories
from compactification on a Riemann surface, i.e., to the Hitchin system on C.
A toric CY3 does not directly produce a spectral network (no canonical surface
C). However, for toric CY3 geometries that arise as local curves (e.g., the
resolved conifold = local P^1), there IS a spectral network on P^1.

**K3 x E?** NO directly -- K3 x E does not produce a 4d N=2 theory on a
surface. The BKM structure of g_{Delta_5} is not naturally a spectral network.

**Higgs(C)?** YES -- this is the native habitat. The spectral network on C
encodes the BPS spectrum of the Hitchin system, which is exactly the root
multiplicity data of the quantum vertex chiral group G_2(Higgs(C)). For C = P^1
with regular singularities: finite BPS spectrum, Yangian. For C = E: the
spectral network degenerates to a lattice, elliptic Hall algebra.

**Tree-level data?** YES -- the saddle connections (finite-length trajectories)
are the tree-level data: they correspond to hypermultiplets (bifundamental
matter), i.e., real roots.

**Loop-level data?** PARTIAL -- the spectral network captures the wall-crossing
data (the KS automorphisms), but the full automorphic correction (Borcherds
lift) is not directly visible. The spectral network is a 2d object; the
Borcherds lift requires a 3d perspective.

**Computable?** YES -- algorithms for computing spectral networks exist
(Neitzke et al.), though they are computationally intensive.

**Presentable?** YES -- clean definition (differential equation on C).

**Verdict:** Excellent for Higgs(C) / CY2, partial for CY3. The spectral
network is a Level 1+2 object for the CY2 case. For CY3, it captures a
2-dimensional slice of the full data. It should be understood as the
restriction of the scattering diagram to a surface.

---

### Candidate 6: Tropical CY geometry (Gross-Siebert)

**What it is.** The Gross-Siebert programme: a tropical/combinatorial approach
to mirror symmetry, where a CY manifold is encoded by an integral affine
manifold B with singularities, together with a polyhedral decomposition P of B
and a collection of "slab functions" (tropical analogues of holomorphic discs).

**Toric CY3?** YES -- the moment polytope of a toric CY3 IS the tropical
CY (the integral affine manifold B = moment polytope, P = the fan, slab
functions = 1 (no corrections for toric varieties)). The topological vertex
computation is the tropical vertex computation.

**K3 x E?** YES, in principle -- Gross-Siebert's programme applies to K3
surfaces (the tropical K3 is an integral affine S^2 with 24 singular points).
The product K3 x E has a tropical description as the product of the tropical K3
and a tropical circle. However: extracting the BKM root datum (the Gram matrix,
Weyl group, root multiplicities) from the tropical data requires the scattering
diagram on B, which is a major open problem in the Gross-Siebert programme for
non-toric cases.

**Higgs(C)?** PARTIAL -- the Hitchin base is an affine space, and the
Hitchin fibration has a natural tropical/integrable system structure (the
SYZ fibration). The tropical data encodes the Lagrangian torus fibration,
but the quantum corrections (disc counting = scattering diagram completion)
are the hard part.

**Tree-level data?** YES -- the polyhedral decomposition P of B gives vertices
(toric charts), edges (gluings), faces (relations).

**Loop-level data?** YES, in principle -- the slab functions and the
scattering diagram on B encode the quantum corrections. But: computing these
corrections is the central difficulty of the Gross-Siebert programme.

**Computable?** PARTIALLY -- for toric: fully computable. For general CY3:
the scattering diagram completion is the bottleneck (same as Candidate 2, since
tropical = scattering diagram in the Gross-Siebert framework).

**Presentable?** YES -- the Gross-Siebert axioms are clean.

**Verdict:** The tropical CY is the GEOMETRIC realization of the scattering
diagram (Candidate 2). It provides the base manifold B on which the scattering
diagram lives. For toric CY3, it reduces to the moment polytope. For general
CY3, it is conjecturally equivalent to the scattering diagram but harder to
compute. It is Level 0+1+2 data (lattice + fan + corrections).

---

### Candidate 7: Motivic Hall algebras

**What it is.** The Hall algebra H(C) of a CY3 category C, defined using
motivic integration on the stack of objects M(C). The product is the "extension
product": [E] * [F] = sum of [G] over extensions 0 -> F -> G -> E -> 0,
weighted by motives of Ext groups.

**Toric CY3?** YES -- the motivic Hall algebra of Coh(X) for a toric CY3 X
is directly related to the CoHA (the critical CoHA is a cohomological shadow of
the motivic Hall algebra). The CoHA = positive half of the affine super Yangian
(RSYZ), which is already established in our framework.

**K3 x E?** YES, in principle -- the motivic Hall algebra of Coh(K3 x E)
exists and its numerical shadow should recover the root multiplicities of
g_{Delta_5}. However: the motivic Hall algebra of a non-toric CY3 is not well
understood (no explicit generators-and-relations presentation). The DT
invariants (= motivic DT invariants after taking the motivic weight) DO give
the root multiplicities, but the algebraic structure of the Hall algebra has
not been worked out for K3 x E.

**Higgs(C)?** YES -- the motivic Hall algebra of Coh(T^*C) is Schiffmann-
Vasserot's elliptic Hall algebra (for C = E). For C = P^1: the Hall algebra of
Higgs sheaves is related to the Yangian Y(gl_2).

**Tree-level data?** PARTIAL -- the Hall algebra is the FULL algebra, not
decomposed into tree/loop levels. The tree-level data (the quiver) is encoded
in the "semisimple locus" of the Hall algebra.

**Loop-level data?** YES -- the Hall algebra encodes ALL the BPS data
(tree-level AND loop-level), since it works with the full moduli stack. The
automorphic correction is built into the motivic integration.

**Computable?** PARTIALLY -- motivic Hall algebras are notoriously hard to
compute. For toric CY3, the CoHA gives a computable shadow. For general CY3,
the computation is a major open problem.

**Presentable?** PARTIALLY -- the definition is clean, but the resulting
algebra is typically infinite-dimensional with no known explicit presentation
(except for toric/Higgs cases).

**Verdict:** The motivic Hall algebra is the ALGEBRAIC incarnation of the
full CY combinatorial datum. It carries all levels of data. But it is an
algebraic object, not a combinatorial datum -- it is what the combinatorial
datum should PRODUCE, not the datum itself. The relationship: the CY
combinatorial datum is the ROOT DATUM of the motivic Hall algebra.

---

### Candidate 8: Lattice VOAs from K-theory

**What it is.** A vertex (operator) algebra V_Lambda constructed from a lattice
Lambda with bilinear form, via the Frenkel-Kac-Segal construction: start with
the Heisenberg VOA Heis(Lambda tensor R), then extend by vertex operators
e^alpha for alpha in Lambda.

**Toric CY3?** PARTIAL -- for C^3, the relevant VOA is W_{1+infinity} (the
affine Yangian of gl_1), which is NOT a lattice VOA but rather a W-algebra.
The lattice K_0(C^3) = Z is rank 1 with trivial form; the lattice VOA is just
the Heisenberg, which misses the W_{1+infinity} structure.

**K3 x E?** YES -- the lattice Lambda^{3,2} determines a lattice-type VOA,
and the BKM superalgebra g_{Delta_5} is constructed from this lattice data
via the Borcherds construction. The denominator identity Delta_5 is the
character of a module of this VOA.

**Higgs(C)?** PARTIAL -- the lattice of the Hitchin system (the charge
lattice) determines a Heisenberg sub-VOA, but the full quantum vertex chiral
group is a W-algebra extension, not just the lattice VOA.

**Tree-level data?** YES -- the lattice Lambda and the bilinear form (,) are
the tree-level data. Vertex operators e^alpha for real roots are the
intertwiners.

**Loop-level data?** PARTIAL -- the lattice VOA by itself does not encode the
automorphic correction. One needs the Borcherds construction (adding imaginary
root generators) to get the full BKM algebra. The lattice VOA is the INPUT to
the Borcherds construction, not the output.

**Computable?** YES -- lattice VOAs are highly computable (character formulas,
correlation functions).

**Presentable?** YES -- the Frenkel-Kac-Segal construction is clean.

**Verdict:** The lattice VOA is Level 0 data (the lattice and form). It needs
the Borcherds automorphic correction (= shadow tower = scattering diagram
completion) to become the full quantum vertex chiral group. This is exactly
the "CY1 axiom" part of the CY root datum: the starting data before the
BPS spectrum is included.

---

### Candidate 9: Vafa-Witten theory

**What it is.** The partition function Z_{VW}(S) of the topologically twisted
N=4 SYM on a 4-manifold S (Vafa-Witten 1994), which for S = K3 is a modular
form. More precisely, Z_{VW}(K3; G) is a vector-valued modular form for
SL_2(Z) valued in the discriminant form of the gauge group lattice.

**Toric CY3?** NO directly -- Vafa-Witten theory is a 4d theory on a
4-manifold. A toric CY3 is 6-dimensional. However: dimensional reduction
VW on S to 2d gives a theory on E (when S = K3, the 2d theory on E produces
the denominator identity). So VW on K3 is related to CY3 = K3 x E, but the
relationship is indirect.

**K3 x E?** YES -- this is the main success story. VW on K3 with gauge group
SU(N) produces modular forms whose generating series is related to the Igusa
cusp form. Specifically: Z_{VW}(K3; SU(N)) is a Jacobi form, and the
Borcherds lift of the N=1 partition function (= phi_{0,1}, the K3 elliptic
genus) gives Delta_5. The root multiplicities of g_{Delta_5} are the VW
invariants.

**Higgs(C)?** PARTIAL -- VW theory on C x T^2 (where C is a Riemann surface)
produces a theory on T^2 whose Hilbert space is the Hitchin moduli space
Higgs(C). So VW connects to Higgs, but indirectly (via dimensional reduction).

**Tree-level data?** PARTIAL -- the VW partition function at one-instanton
level gives the tree-level data (real roots = one-instanton contributions).

**Loop-level data?** YES -- the full VW partition function includes all
instanton numbers, hence all imaginary root contributions. The modularity of
Z_{VW} IS the automorphic property of the denominator identity.

**Computable?** PARTIALLY -- VW partition functions are computable for K3 and
ALE spaces (via localization / blowup formulas). For general 4-manifolds, the
computation is difficult.

**Presentable?** PARTIALLY -- the physical definition is clean; the
mathematical definition (via the moduli space of solutions to the VW equations)
requires care with compactifications.

**Verdict:** VW theory provides the PHYSICAL origin of the Level 2 data
(automorphic forms). It is not a combinatorial datum per se, but rather the
physical theory that produces the automorphic correction. For K3 x E, VW on K3
= Borcherds lift = shadow tower completion.

---

## 2. The hierarchy is real

The evaluation confirms the suspicion stated in the task: **no single candidate
captures all the data.** Instead, each candidate captures data at specific
levels of a hierarchy. The hierarchy is:

### Level 0 -- The lattice

**Data:** An even lattice Lambda with symmetric bilinear form (,) of indefinite
signature (p, q) with p >= 2, q in {1, 2}. Extracted from K_0(C) with the
Euler form, or from H^*(X, Z) with the Mukai pairing.

**Axioms:** CY1 (lattice structure) and CY7 (integrality) of the generalized
root datum.

**Candidates that carry it:** Lattice VOA (Candidate 8), quiver lattice
(Candidate 4), toric fan (Candidate 6), all others implicitly.

**Examples:**
- Toric CY3: Z^{Q_0} with symmetrized Euler-Ringel form.
- K3 x E: Lambda^{2,1}_{II} + Lambda^{1,1}, signature (3,2).
- Higgs(C): the charge lattice of the Hitchin system (rank + degree).

### Level 1 -- The tree (scattering diagram skeleton)

**Data:** On the lattice Lambda, a finite set of real simple roots
Pi^{re} = {alpha_1, ..., alpha_n} in Lambda^{hyp} with (alpha_i, alpha_i) = 2,
together with the Gram matrix A_{ij} = (alpha_i, alpha_j) and the Weyl group
W = <s_{alpha_i}>. This is the "skeleton" of the scattering diagram: the
initial walls before completion.

**Axioms:** CY2 (real root constraints) and CY4 (Weyl group).

**Algebraic incarnation:** The Kac-Moody algebra g(A) with Cartan matrix A
(BEFORE adding imaginary roots). The collision r-matrix r(z). The positive half
U(n_+) at tree level.

**Candidates that carry it:** Brane tilings (Candidate 1) for toric CY3,
quivers (Candidate 4), scattering diagram initial data (Candidate 2),
toric fan (Candidate 6), spectral networks at generic phase (Candidate 5).

**Examples:**
- C^3: no real roots (degenerate). g = Heisenberg.
- Conifold: two real roots, A = ((2,-2),(-2,2)) (affine A_1). g = sl_2-hat.
- K3 x E: three real roots, A = ((2,-2,-2),(-2,2,-2),(-2,-2,2)). g = hyperbolic KM.
- Higgs(P^1): real roots from the curve P^1 (semisimple locus of Hitchin base).

### Level 2 -- The surface (automorphic correction)

**Data:** A multiplicity function mult: Delta^{im} -> Z_{!= 0} on imaginary
roots, controlled by a Jacobi-type form phi of weight 0, together with the
Weyl vector rho. Equivalently: the completed scattering diagram, where each
new wall carries mult(alpha). Equivalently: the Borcherds multiplicative lift
of phi.

**Axioms:** CY3 (imaginary root multiplicities from Jacobi form), CY5
(automorphic denominator identity), CY6 (Serre relations).

**Algebraic incarnation:** The full BKM superalgebra g_R (after adding
imaginary roots). The completed shadow tower Theta_A = sum_{r >= 2} Theta^{(r)}.
The denominator identity Phi_R.

**Connection to shadow tower:** Arity r of the shadow tower captures roots
up to complexity r. Arity 2 = Weyl vector (kappa). Arity 3 = first imaginary
roots. The completion algorithm (adding walls until consistency) IS the shadow
tower construction (solving the MC equation order by order in arity).

**Candidates that carry it:** Scattering diagrams (Candidate 2 -- the completed
diagram), tropical CY with slab functions (Candidate 6), Vafa-Witten theory
(Candidate 9 -- as the physical origin), motivic Hall algebra (Candidate 7 --
algebraic incarnation).

**Examples:**
- C^3: mult(n) = p(n) (partitions). Phi = MacMahon function M(q).
- K3 x E: mult(alpha) = c_{phi_{0,1}}(nm, l). Phi = (1/64) Delta_5.
- Higgs(E): mult from the elliptic Hall algebra character. Phi = eta-products.

### Level 3 -- The volume (full modular / higher-genus data)

**Data:** The genus-g amplitudes obs_g = kappa * lambda_g, encoding the full
modular structure. For CY3: the BCOV theory, the topological string partition
function F_g(t), the Gromov-Witten invariants at all genera. The E_2-chiral
structure (braided monoidal category Rep^{E_2}(G(X))).

**Axioms:** No axiom yet -- this level is not captured by the CY root datum
axioms (CY1)-(CY7). It requires the FULL quantum vertex chiral group G(X),
not just the root datum R(X).

**Algebraic incarnation:** The quantum vertex chiral algebra A(X) with its
E_2-chiral structure. The braided monoidal category Rep^{E_2}(G(X)). The
genus-g modular forms (Siegel modular forms on H_g for the K3 x E tower).

**Connection to the programme:** This is what Vol I's Theta_A produces at
the topological level. The full partition function Z(A) = sum_g hbar^{2g-2}
F_g is the "volume" data. The E_2 braiding is the genus-1 enhancement
(quantization of the Poisson bracket coming from the symplectic structure
on the moduli space).

**Candidates that carry it:** The motivic Hall algebra (Candidate 7) carries
it in principle (all of the BPS data is there). VW theory (Candidate 9) gives
the physical computation. No purely combinatorial candidate captures this level
completely -- it requires the full algebraic structure.

---

## 3. The CY combinatorial datum: definition

The hierarchy suggests the following definition:

**Definition (CY combinatorial datum).** A *CY combinatorial datum of
dimension 3* is a quadruple

    D = (R, S, Phi, E_2)

consisting of:

**(D0) The CY root datum** R = (Lambda, (,), Delta, mult, W, rho) satisfying
axioms (CY1)-(CY7) of theory_generalized_root_datum.tex.

This already packages Levels 0-2:
- Level 0 (lattice): Lambda with (,).
- Level 1 (tree): Delta^{re}, W, the Gram matrix A of simple roots.
- Level 2 (surface): mult: Delta^{im} -> Z, the Jacobi form phi, the Weyl
  vector rho.

**(D1) The scattering diagram** S = (B, P, D) where:
- B is an integral affine manifold (the "tropical base");
- P is a polyhedral decomposition of B compatible with the lattice Lambda;
- D is a consistent scattering diagram on (B, P): a collection of walls d_i
  (codimension-1 polyhedral subsets of B) carrying automorphisms
  theta_{d_i} in Aut(k[Lambda]) such that the product of wall-crossing
  automorphisms around any loop is the identity.

The scattering diagram S is *compatible with R* if:
- The initial walls of S correspond to the real simple roots Pi^{re}.
- The walls generated by the consistency algorithm correspond to the imaginary
  roots Delta^{im}, with the attached automorphisms encoding mult(alpha).

**(D2) The automorphic form** Phi = Phi_R, the denominator identity of R
viewed as an automorphic form for O(Lambda)_+. This is determined by (D0)
via the Borcherds product formula, but carrying it as separate data emphasizes
its role as a modular object.

Specifically, Phi satisfies:
- Phi is an automorphic form of weight k_R = (1/2) c_phi(0,0) on the
  orthogonal symmetric domain D(Lambda).
- The product expansion: Phi(z) = e^{-2 pi i (rho, z)} prod_{alpha in Delta_+}
  (1 - e^{-2 pi i (alpha, z)})^{mult(alpha)}.
- Phi = bar-complex Euler product chi(B(A_X)) of the quantum chiral algebra.

**(D3) The E_2 enhancement** E_2 = a braided monoidal structure on the
representation category Rep(g_R), specified by:
- An R-matrix R(z) in End(V tensor V)[[z]] solving the quantum Yang-Baxter
  equation (for the Yangian/quantum group case);
- Or: a modular functor structure on the category of g_R-modules, compatible
  with the modular group action on Phi (for the BKM/automorphic case);
- Or: an E_2-operad action on the factorization algebra Fact(A_X) on Ran(C)
  (for the chiral algebra case).

The E_2 enhancement is *compatible with the rest* if the monodromy of Phi
around the discriminant locus in D(Lambda) is given by the braiding in E_2.

---

## 4. The fibration structure

The most important structural operation: given a CY_2 datum and an elliptic
datum, produce a CY_3 datum.

**Construction (Fibration).** Given:
- A CY_2 root datum R_S = (Lambda_S, (,)_S, phi_S) (e.g., the K3 root datum
  with phi_S = phi_{0,1});
- An elliptic datum E = (Lambda_E, N);

the fibered CY_3 combinatorial datum D_3 = Fib(D_2, E) has:
- (D0): R_3 = Fib(R_S, E) as in theory_generalized_root_datum.tex
  Construction 5.1 (the fibration root datum).
- (D1): S_3 is the scattering diagram on B_3 = B_S x S^1, where B_S is the
  tropical base of S and S^1 is the tropical circle of E. The walls in S_3
  are "lifts" of walls in S_2 (the CY_2 scattering diagram), plus new walls
  generated by the Borcherds lift.
- (D2): Phi_3 = Borch(phi_S), the Borcherds multiplicative lift of the Jacobi
  form phi_S. For K3 x E: Phi_3 = (1/64) Delta_5.
- (D3): The E_2 structure comes from the modular parameter tau of E acting on
  the Jacobi form phi_S. Concretely: the Sp_4(Z) action on the Siegel
  upper half-space H_2 (which parametrizes genus-2 curves) provides the
  braiding.

This fibration identifies the "shadow tower as Borcherds lift" at every level:
- Level 0: Lambda_3 = Lambda^{hyp} + Lambda^{1,1} (lattice extension).
- Level 1: real roots of R_3 = real roots of the hyperbolic KM of Lambda^{hyp}.
- Level 2: imaginary roots of R_3 = Fourier coefficients of phi_S =
  automorphic correction = completed scattering diagram.
- Level 3: Phi_3 = Borch(phi_S) = the Siegel modular form.

---

## 5. Specialization to the three test geometries

### Test 1: Toric CY3 (topological vertex)

- Level 0: Lambda = Z^{Q_0}, (,) = symmetrized Euler-Ringel form of the
  quiver Q.
- Level 1: Real roots = standard basis vectors e_i with (e_i, e_i) = 2.
  The quiver Q and its brane tiling. The toric fan = the polyhedral
  decomposition P of B = moment polytope.
- Level 2: mult(d) = DT_d(Q, W). The scattering diagram on the moment
  polytope, completed by the KS algorithm. For C^3: mult(n) = p(n),
  Phi = M(q).
- Level 3: The affine super Yangian Y(g-hat_{Q}). R-matrix from the Yang-Baxter
  equation. F_g(t) from the topological vertex at genus g.
- Computationally verified: compute/lib/topological_vertex.py,
  compute/lib/c3_dt_partition.py, compute/lib/affine_yangian_gl1.py.

### Test 2: K3 x E (BKM / Delta_5)

- Level 0: Lambda = Lambda^{2,1}_{II} + Lambda^{1,1}, signature (3,2).
- Level 1: Pi^{re} = {delta_1, delta_2, delta_3}, Gram matrix
  ((2,-2,-2),(-2,2,-2),(-2,-2,2)). W = W^{(2)}(Lambda^{2,1}_{II}).
- Level 2: phi = phi_{0,1} (K3 elliptic genus). mult(alpha) = f(nm, l).
  The Borcherds lift: Phi = (1/64) Delta_5. The automorphic correction adds
  all imaginary roots to the hyperbolic KM algebra.
- Level 3: g_{Delta_5} (the full BKM superalgebra). Sp_4(Z) acts on H_2 as
  the E_2 braiding. kappa(G(K3 x E)) = 5 = weight(Delta_5).
- Computationally verified: compute/lib/phi01_fourier.py,
  compute/lib/dd_modular_lattices.py, compute/lib/igusa_product_formula.py,
  compute/lib/bkm_shadow_tower.py.

### Test 3: Higgs(C) (Yangian / elliptic Hall)

- Level 0: Lambda = Z (rank) x Z (degree), (,) depends on genus.
- Level 1: For C = P^1: rational r-matrix, Yangian Y(gl_2). For C = E:
  elliptic r-matrix, one-loop scattering diagram on the Hitchin base.
- Level 2: For C = P^1: finite BPS spectrum, no automorphic correction needed.
  For C = E: the elliptic Hall algebra E_{q,t}, Phi = eta-products. For
  genus >= 2: "Hitchin Hall algebras" (new, conjectural).
- Level 3: E_2 structure from the braided monoidal category. For C = P^1:
  the quantum group Rep(Y(gl_2)). For C = E: the spherical DAHA category.
  For genus >= 2: unknown.
- Computationally verified: compute/lib/elliptic_hall.py,
  compute/lib/higgs_p1_coha.py.

---

## 6. The main conjecture

**Conjecture (CY Combinatorial Classification).**
Let X be a Calabi-Yau threefold (smooth, projective, or quasi-projective with
at worst Gorenstein singularities). Let C(X) denote the CY_3 category of X
(either D^b(Coh(X)) or the Fukaya category Fuk(X), related by HMS).

(I) *Extraction.* There is a canonical CY combinatorial datum D(X) extracted
from C(X):
- R(X) from K_0(C(X)) with the Euler form and DT invariants;
- S(X) from the Bridgeland stability manifold Stab(C(X));
- Phi(X) from the Borcherds product / DT partition function;
- E_2(X) from the S^2-framing of the CY_3 cyclic structure (via Dunn:
  S^3-framing -> E_3 -> E_2).

(II) *Classification up to derived equivalence.* Two CY threefolds X, X' are
derived equivalent (D^b(Coh(X)) ~ D^b(Coh(X'))) if and only if their CY
combinatorial data are isomorphic: D(X) ~ D(X').

More precisely: the map X |-> D(X) descends to an injective map from the set
of derived equivalence classes of CY3 categories to the set of isomorphism
classes of CY combinatorial data. The image consists of the "geometric" CY
combinatorial data (those satisfying the Hodge-theoretic, mirror, and DT
integrality constraints of Proposition 7.2 in theory_generalized_root_datum.tex).

(III) *Determination of the quantum vertex chiral group.* The CY combinatorial
datum D(X) determines a quantum vertex chiral group G(X) whose:
- Root datum is R(X);
- BKM superalgebra is g_{R(X)};
- Chiral algebra A_X has bar complex B(A_X) graded by Lambda(X);
- Shadow tower Theta_{A_X} encodes the automorphic correction (Level 2);
- Denominator identity equals the automorphic form Phi(X);
- Representation category Rep^{E_2}(G(X)) is the braided monoidal category
  determined by E_2(X);
- Modular characteristic kappa(G(X)) = weight of Phi(X) = (1/2) chi(X).

(IV) *Compatibility with fibration.* If X = (S x E)/G for S a K3 surface
and E an elliptic curve, then D(X) = Fib(D_2(S), E_G), where D_2(S) is the
CY_2 datum of S and E_G is the elliptic datum (Lambda_E, |G|). The Borcherds
lift of the Jacobi form of S equals the denominator identity of G(X).

(V) *Computability.* Each level of the CY combinatorial datum is algorithmically
computable:
- Level 0: lattice arithmetic (reduction of intersection forms).
- Level 1: Vinberg's algorithm for the fundamental polyhedron; quiver mutation.
- Level 2: KS scattering diagram completion; Borcherds lift computation.
- Level 3: quantum group R-matrix from the RTT formalism; modular functor from
  the conformal blocks of the associated VOA.

---

## 7. Relationship to the shadow tower

The shadow tower of Volume I is the algebraic engine that builds the CY
combinatorial datum level by level:

| Shadow tower component | CY combinatorial level | Mathematical content |
|---|---|---|
| Theta^{(2)} = kappa | Level 1 -> Level 2 transition | Weyl vector, modular characteristic |
| Theta^{(3)} = C (cubic shadow) | First imaginary roots | First layer of Borcherds correction |
| Theta^{(r)} (arity r) | Roots at depth r-2 | Order-r scattering diagram walls |
| Theta = lim Theta^{(<=r)} | Full Level 2 data | Complete automorphic form Phi |
| MC equation dTheta + (1/2)[Theta, Theta] = 0 | Consistency of S | Scattering diagram consistency |
| Gauge equivalence of MC | Wall-crossing | KS wall-crossing formula |

The scattering diagram completion algorithm and the shadow tower Postnikov
filtration are THE SAME COMPUTATION carried out in different languages:
- Scattering diagram: add walls until the composition around every loop is
  trivial (geometric consistency).
- Shadow tower: solve the MC equation order by order in arity (algebraic
  consistency).

---

## 8. Which candidate "wins"?

None individually. The correct answer is:

**The CY combinatorial datum is a scattering diagram on a lattice, enriched
by an E_2 structure.**

This combines:
- Candidate 2 (scattering diagrams) for the core structure (Levels 1+2);
- Candidate 8 (lattice VOAs) for Level 0;
- Candidate 4 (quivers with enriched potential) as the local model at each
  vertex of the scattering diagram;
- Candidate 6 (tropical CY geometry) as the geometric realization of the base
  manifold;
- Candidate 7 (motivic Hall algebras) as the algebraic output;
- Candidate 5 (spectral networks) as the CY_2 restriction;
- Candidate 9 (VW theory) as the physical origin of Level 2;
- Candidate 1 (brane tilings) as the toric specialization of Level 1.

The scattering diagram is the UNIFYING framework because:
1. It naturally lives on the lattice Lambda (Level 0).
2. Its initial walls are the real roots (Level 1).
3. Its completion is the automorphic correction (Level 2).
4. The consistency condition = MC equation = shadow tower.
5. It specializes correctly to all three test geometries.
6. The Gross-Siebert programme provides the geometric foundation.
7. The KS framework provides the algebraic foundation.

The E_2 enrichment comes from promoting the formal automorphisms attached to
walls from elements of Aut(k[Lambda]) to R-matrices (solutions of the quantum
YBE). This is the passage from the "classical" scattering diagram (KS/GS) to
the "quantum" scattering diagram (the quantum vertex chiral group).

---

## 9. Proposed computation modules

To make this concrete, the following new compute modules should be developed:

1. **compute/lib/scattering_diagram.py**: Implement the KS scattering diagram
   completion algorithm for a lattice with Gram matrix and initial walls.
   Input: Gram matrix A, initial walls (real simple roots). Output: walls up
   to a given depth (= arity of the shadow tower), with attached automorphisms.
   Verify against bkm_shadow_tower.py for the K3 x E case.

2. **compute/lib/tropical_cy.py**: Implement the tropical CY base manifold
   for toric CY3s (moment polytope + fan). Verify against
   topological_vertex.py.

3. **compute/lib/cy_combinatorial_datum.py**: A master class CYDatum that
   packages (Lambda, A, mult, W, rho, Phi) and verifies axioms (CY1)-(CY7).
   Factory methods: from_quiver(Q, W), from_k3_fibration(Lambda_hyp, phi),
   from_higgs(C, G).

4. **compute/lib/e2_rmatrix.py**: Compute the R-matrix of the quantum vertex
   chiral group from the scattering diagram data. For toric CY3: recover the
   RSYZ R-matrix. For K3 x E: recover the BKM braiding.

---

## 10. Summary

The CY combinatorial datum is NOT a single combinatorial object but a
HIERARCHY of increasingly rich structures:

- Level 0: an even lattice Lambda with bilinear form -- the charge lattice.
- Level 1: a finite root system Delta^{re} in Lambda -- the tree-level data.
- Level 2: a scattering diagram on Lambda -- the automorphic correction.
- Level 3: an E_2-chiral structure -- the quantum group data.

Each level enriches the previous one, and the shadow tower is the tower of
these enrichments. The CY root datum (CY1)-(CY7) captures Levels 0-2. The full
quantum vertex chiral group G(X) captures all four levels.

The scattering diagram (Candidate 2), enriched with E_2 data and seated on a
lattice VOA (Candidate 8), is the optimal combinatorial incarnation. It
specializes correctly to toric CY3 (where it reduces to the brane
tiling/quiver), to K3 x E (where its completion is the Borcherds lift producing
Delta_5), and to Higgs(C) (where it reduces to the spectral network/Bridgeland
stability scattering diagram producing the Yangian/elliptic Hall R-matrix).

The main conjecture: this datum classifies CY3 categories up to derived
equivalence and determines the quantum vertex chiral group.
