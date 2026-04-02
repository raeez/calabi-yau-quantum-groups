# BPS Graphs and Spectral Networks as the Core Combinatorial Datum

## Research note — 2 April 2026

### Overview

This note investigates the proposal that the **spectral network** (in the sense
of Gaiotto--Moore--Neitzke, 2009--2013) is the core combinatorial datum
underlying the quantum vertex chiral group G(X) of a CY3 threefold X.

A spectral network on a surface C is a collection of oriented curves (walls) on
C, labeled by roots of a Lie algebra g, satisfying specific differential
equations (the WKB flow equations). At each point of C, the network encodes the
BPS spectrum of the 4d N=2 theory obtained by compactifying the 6d (2,0) theory
of type g on C. The spectral network depends on a phase parameter — a stability
condition — and undergoes combinatorial mutations (flips) as the phase varies.

The spectral network sits at the intersection of:
- The Hitchin system (it lives on the base of the Hitchin fibration)
- Wall-crossing (flips are the GMN/KS wall-crossing formula)
- Tropical/combinatorial geometry (the WKB curves are the tropical limits of
  the spectral curves)
- Cluster algebras (the Fock--Goncharov coordinates are parametrized by
  spectral networks)

**Verdict**: The spectral network is an extremely compelling candidate for the
combinatorial datum. It naturally encodes the MC element Theta_A, its
dependence on stability conditions, and the wall-crossing = gauge equivalence
structure. However, it applies most naturally to *local* CY3 geometries
(class S theories from Hitchin systems), and the extension to compact CY3s
(especially K3 x E) requires significant new ideas.

---

## 1. Definition and basic structure

### 1.1. The GMN spectral network

**Setup.** Let C be a Riemann surface, G = SL(N), and (E, phi) a point of the
Hitchin base A_H. The spectral curve Sigma_a -> C is an N-fold branched
covering. Fix a phase theta in R/2piZ (equivalently, a ray in the Z-plane).

**Definition (GMN).** The spectral network W(phi, theta) is the collection of
all curves w on C satisfying:

    (lambda_i - lambda_j)(dw/dt) in e^{i*theta} * R_{>0}

where lambda_i, lambda_j are distinct sheets of the spectral cover above w, and
t is the parameter along the curve. In other words: the walls of the spectral
network are the integral curves of the foliation on C defined by the condition
that the *difference* of the SW differential lambda_SW = p dx restricted to two
sheets has constant phase theta along the curve.

Each wall is labeled by a pair (ij) of sheets — equivalently, by a root
alpha_{ij} of gl(N). At branch points of Sigma -> C (where two sheets collide),
new walls are born. The walls propagate across C, possibly colliding at
*joints* (codimension-2 loci) where three or more walls meet.

### 1.2. Dependence on the phase theta

As theta varies continuously, the spectral network W(phi, theta) changes
continuously *most of the time*, but at discrete critical phases theta_c, the
topology changes by a **flip**: a wall either appears, disappears, or passes
through a joint. These critical phases are precisely the phases
theta_c = arg Z_gamma(u) of BPS central charges.

This is the GMN wall-crossing formula in the spectral network language:
- Between critical phases: the network is stable (no BPS decays)
- At a critical phase: a wall of type gamma passes through a joint,
  encoding the existence of a BPS state of charge gamma
- The flip relation is equivalent to the KS wall-crossing formula

### 1.3. The spectral network as tropical datum

The spectral network is the **tropical limit** of the spectral curve.
More precisely:

- The spectral curve Sigma_a in T*C is a complex algebraic curve
- The spectral network W(phi, theta) is the image under the WKB approximation
  (hbar -> 0) of the anti-Stokes lines of the quantum curve
  det(hbar d/dx - phi(x)) psi = 0
- In the tropical limit, the spectral curve degenerates to a tropical curve
  (a metric graph) on C, and the spectral network IS this tropical curve

This connects directly to the scattering diagram / tropical MC interpretation
already developed in the codebase (physics_wall_crossing_mc.tex, Sec. 4.3):

    Spectral network walls <--> Scattering diagram rays
    Wall labels (roots)    <--> Scattering diagram automorphisms K_gamma
    Joints                 <--> Codimension-2 intersections (MC equation)
    Flip = wall-crossing   <--> Gauge transformation of Theta_A

---

## 2. The five questions

### Q1. K3 x E: spectral network on the base of the K3 fibration

For X = K3 x E, the CY3 does *not* arise directly from a class S theory
(it is not a Hitchin system on a curve). However, there is a partial story:

**The K3 fibration perspective.** View K3 x E as an elliptic K3 fibered over
P^1, with a further E-fibration. The base of the K3 fibration is P^1. The
"walls" on P^1 are the singular fibers of the K3 elliptic fibration — 24
singular fibers (for a generic elliptic K3). But these are *not* spectral
network walls in the GMN sense — they are discriminant loci, not WKB curves.

**The Hitchin system connection.** A more promising route: the K3 x E BPS
spectrum is governed by the Mukai lattice Lambda = H^*(K3, Z) of signature
(4,20), and the BKM root system has three real simple roots with Gram matrix
((2,-2,-2),(-2,2,-2),(-2,-2,2)). The Weyl group W^{(2)}(Lambda^{2,1}_{II})
acts on the positive cone.

The spectral network, if it exists for K3 x E, should live on a
**2-dimensional** space (not a curve) because the "base" of the relevant
fibration is 2-dimensional. This is closer to a *spectral network on a surface*
in the sense of a higher-dimensional generalization. The walls would be
codimension-1 in the 2d base (i.e., curves in a surface), labeled by elements of
the root lattice Lambda^{2,1}_{II}.

**Proposed identification.** The Weyl chamber decomposition of the positive cone
C^+(Lambda^{2,1}_{II}) by the reflection hyperplanes of W^{(2)} IS the
analogue of the spectral network for K3 x E:
- The walls (reflection hyperplanes in the positive cone) correspond to real
  roots delta with (delta, delta) = 2
- The chambers correspond to different "stability conditions" (fundamental
  domains of the Weyl group)
- The Igusa cusp form Delta_5 is gauge-invariant across all chambers

This is consistent with the existing framework (physics_wall_crossing_mc.tex,
Sec. 7.2: "the imaginary root multiplicities f(nm,l) are gauge-dependent (they
depend on the choice of fundamental domain for W^{(2)}(Lambda^{2,1}_{II})), but
the sum formula (denominator identity Delta_5) is gauge-invariant").

**Assessment.** The spectral network for K3 x E is the Weyl chamber
decomposition, NOT a classical GMN spectral network on a curve. The W^{(2)}
reflection group plays the role of the wall-crossing groupoid. This is a
*higher-dimensional* analogue of the spectral network, appropriate for a CY3
that is not a local CY3 from a Hitchin system.

### Q2. Toric CY3: spectral network vs. toric web diagram

For a toric CY3 X_Sigma, the relevant combinatorial datum is the **toric web
diagram** (the trivalent planar graph dual to the toric polygon). The question
is: does the spectral network reduce to the toric web?

**The (p,q)-web connection.** For local CY3 geometries that also admit a
class S description, the answer is YES in a specific sense. Consider the
resolved conifold X = O(-1) + O(-1) -> P^1. This geometry:
- Has a toric diagram: two vertices joined by one edge
- Engineers pure SU(2) gauge theory
- The SW curve is a 2-fold cover of P^1 with 4 branch points
- The spectral network on P^1 at generic phase consists of WKB curves
  connecting the branch points

The toric web diagram encodes the **tropical limit** of the spectral network:
- The vertices of the web are the "frozen" data (the local root data
  G_v = G(C^3) at each vertex, as in physics_topological_strings.tex Sec. 4.3)
- The edges carry the propagator / edge weight Q_e = exp(-t_e)
- The trivalent structure is the tropical version of the topological vertex
  gluing

For more general toric CY3s:
- The toric web IS the tropical spectral network at a specific (maximally
  degenerate) phase
- At other phases, the spectral network has a richer topology, encoding
  the BPS states at that phase
- The flips of the spectral network correspond to flop transitions of the
  toric CY3 (wall-crossing between different Kahler chambers)

**Assessment.** The toric web diagram is the **tropical/degenerate limit** of
the spectral network. The spectral network is the richer object: it carries the
full BPS spectrum, while the toric web carries only the tree-level (topological
vertex) data. This is consistent with the VISION.md identification: the toric
web gives the local root data R_v, while the spectral network gives the
global root datum R(X) including the imaginary roots from bound states.

### Q3. Encoding the BKM root system

The spectral network encodes the BKM root system as follows:

**Walls = roots.** Each wall of the spectral network is labeled by a root
alpha in the root lattice Gamma. The wall label carries the charge of the
corresponding BPS state.

**Multiplicities = BPS degeneracies.** The number of distinct walls carrying
the same charge gamma (more precisely, the signed count with spin) gives the
BPS index Omega(gamma; u). In the BKM language, this is the root multiplicity
mult(gamma).

**Joints = bracket relations.** When two walls of types gamma_1 and gamma_2
collide at a joint, the consistency condition at the joint produces a new wall of
type gamma_1 + gamma_2. The consistency equation at the joint is:

    K_{gamma_1}^{Omega_1} K_{gamma_2}^{Omega_2}
    = K_{gamma_2}^{Omega_2'} K_{gamma_1+gamma_2}^{Omega_{12}'} ... K_{gamma_1}^{Omega_1'}

This is precisely the Lie bracket [e_{gamma_1}, e_{gamma_2}] = Omega_{12}
e_{gamma_1+gamma_2} in the BKM superalgebra, mediated by the L_infty structure
of the modular convolution algebra g^{mod}_A. The factorization at the joint
is the L_infty MC equation d Theta + (1/2)[Theta, Theta] + ... = 0.

**The denominator identity from the spectral network.** The generating function
of the spectral network (the partition function of all BPS states counted
by the network) is

    Phi_X = prod_{gamma in Gamma_+} (1 - x^gamma)^{(-1)^{|gamma|} mult(gamma)}

which is the bar-complex Euler product / BKM denominator identity. For K3 x E,
this gives (1/64) Delta_5. For toric CY3s, this gives the DT partition function.

**Assessment.** The spectral network does encode the BKM root system. More
precisely:
- At a FIXED phase theta: the network encodes the BPS spectrum at one stability
  condition (one chamber)
- The FULL collection of all networks {W(phi, theta)}_{theta} (varying over all
  phases) encodes the FULL root datum, including the wall-crossing data
- The gauge-invariant content (the denominator identity / automorphic form) is
  independent of the phase

This is exactly the MC gauge equivalence picture of
physics_wall_crossing_mc.tex: different phases give different gauges
(representatives of Theta_A), but the same MC moduli class [Theta_A].

### Q4. GMN wall-crossing = KS wall-crossing

**This is a theorem**, not a conjecture. The GMN spectral network wall-crossing
formula is equivalent to the KS wall-crossing formula. This was established in:

- Gaiotto--Moore--Neitzke, "Wall-crossing, Hitchin systems, and the WKB
  approximation" (Adv. Math. 234, 2013, 239-403): the spectral network
  formalism derives the KS wall-crossing formula for class S theories.

- The key mechanism: the spectral network provides a concrete realization of the
  KS product formula. At a critical phase theta_c = arg Z_gamma, a wall of type
  gamma undergoes a flip. The flip relation between the network before and after
  the flip is EXACTLY the KS relation

      prod_{gamma: arg Z_gamma = theta_c} K_gamma^{Omega(gamma)} = const

  ordered by the phase.

- Bridgeland (2019) made this precise in the mathematical framework: the space
  of stability conditions Stab(C) for the relevant CY3 category is identified
  with a space of irregular connections, and the KS wall-crossing formula
  becomes the isomonodromic deformation equation. The spectral network is the
  WKB approximation to these irregular connections.

**Therefore:** the spectral network encodes the MC gauge equivalence class
[Theta_A] in overline{MC}(g^{mod}_A). The flip/wall-crossing of the spectral
network IS the gauge transformation e^{alpha} . Theta_A of the MC element.

This directly confirms the existing framework in the codebase: the dictionary

    KS ordered product A_l(t) <--> bar-complex Euler product Phi_X
    KS invariance            <--> gauge invariance of Phi_X
    wall-crossing            <--> gauge transformation of Theta_A

(from physics_wall_crossing_mc.tex, Sec. 3.3 and physics_4d_n2_hitchin.tex,
Sec. 3.3) has the spectral network as its *concrete geometric realization*.

### Q5. Stability conditions and the MC moduli space

**The space of spectral networks IS (a piece of) the MC moduli space.**

More precisely, for a class S theory T[G, C]:

- The space of stability conditions is Stab(C_X), which contains the
  Hitchin base A_H as a subset (the "physical" slice)
- At each point (phi, theta) of A_H x (R/2piZ), we have a spectral network
  W(phi, theta) encoding the MC element Theta_A(phi, theta)
- Different phases theta give gauge-equivalent MC elements: Theta_A(phi, theta)
  and Theta_A(phi, theta') are related by a gauge transformation
- The MC moduli space overline{MC}(g^{mod}_A) is parametrized by the
  quotient A_H / (gauge), where the gauge group acts by varying theta

The full story is richer:

1. **The Bridgeland space.** The space Stab(C_X) of Bridgeland stability
   conditions is a complex manifold that maps to A_H (forgetting the heart of
   the t-structure). The fiber over each a in A_H is the space of compatible
   hearts — this is the "phase" degree of freedom that parametrizes different
   gauges.

2. **Autoequivalences and the mapping class group.** The autoequivalence group
   Aut(C_X) acts on Stab(C_X). For class S theories, this includes the mapping
   class group of C and the Weyl group. The quotient
   Stab(C_X) / Aut(C_X) is the "physical" moduli space.

3. **The attractor mechanism.** The attractor MC element Theta_A^* (the
   canonical gauge from physics_wall_crossing_mc.tex, Sec. 5) corresponds to a
   specific spectral network: the one at the phase theta_*(gamma) = arg Z_gamma
   at the attractor point. At this phase, the spectral network is "maximally
   degenerate" (all walls of a given charge are parallel), corresponding to the
   split BPS spectrum.

**Assessment.** The MC moduli space is parametrized by the space of stability
conditions modulo gauge (= modulo phase variation). The spectral network
provides the concrete geometric realization of this parametrization: each point
in the MC moduli space corresponds to a gauge equivalence class of spectral
networks.

---

## 3. The bridging role: from toric vertex to automorphic form

The proposal asks whether the spectral network bridges the tree-level (toric
vertex) and the full automorphic (K3 x E) cases. Here is the assessment:

### 3.1. What the spectral network provides for toric CY3

For a toric CY3 X with toric diagram Sigma:
- The toric web (tropical limit of the spectral network) gives the local root
  data R_v = R(C^3) at each vertex
- The topological vertex C_{lambda mu nu}(q) is the local intertwiner
  (physics_topological_strings.tex, Sec. 4.3)
- The gluing formula Z(X) = sum prod C . Q^|lambda| . f is the factorization
  product over the tropical spectral network
- The full (non-tropical) spectral network captures the BPS bound states that
  go beyond the topological vertex

### 3.2. What the spectral network provides for Hitchin systems

For a class S theory T[G, C]:
- The spectral network lives on C (the UV curve)
- It encodes the BPS spectrum of the 4d N=2 theory
- The flips encode wall-crossing
- The generating function is the DT partition function of the local CY3 X_{G,C}
- The AGT correspondence identifies this with a W-algebra conformal block

### 3.3. The gap: compact CY3s and K3 x E

For K3 x E, the spectral network in the strict GMN sense does NOT directly
apply, because K3 x E is not a class S theory (it is not obtained by
compactifying the 6d (2,0) theory on a curve). However:

**The 2d spectral network.** As argued in Q1 above, the analogue of the spectral
network for K3 x E is the Weyl chamber decomposition of the positive cone
C^+(Lambda^{2,1}_{II}) by the reflection hyperplanes of W^{(2)}. This is a
2-dimensional spectral network (walls are curves in a 2d space) rather than the
1-dimensional spectral networks on a Riemann surface.

**The Borcherds lift as fibered spectral network.** The CY2 -> CY3 fibration
(theory_cy2_cy3_fibration.tex) provides a different perspective: the spectral
network of K3 x E is obtained by "fibering" the K3 spectral data (the Mukai
lattice and its Hodge structure) over the elliptic curve E. The Borcherds
multiplicative lift phi_{0,1} -> Delta_5 is the operation that converts the
"fiber-wise" spectral data into the "total space" automorphic form. In this
picture:
- The K3 elliptic genus phi_{0,1} is the generating function of the 2d
  spectral network data on a single fiber
- The Borcherds lift assembles these into the Siegel modular form Delta_5
  by summing over the lattice of the total space

**Connecting to the Hitchin system.** There is a tantalizing connection via the
Hitchin moduli space M_H(C, G) for g(C) = 2, G = SL(2):
- dim M_H = 4 * 3 * 1 = 12 (real)
- The Hitchin base is A_H = H^0(C, K_C^2) = C^3 (a 3-dimensional space)
- The Hitchin fiber is a (generalized) abelian variety of dimension 3
- The total space is a non-compact CY (hyperkahler) 6-fold

The K3 x E denominator identity Delta_5 is a Siegel modular form for
Sp_4(Z) = SO_+(3,2), and the Hitchin base for g=2, G=SL(2) is 3-dimensional.
This suggests (as noted in physics_hitchin_langlands.tex) that the K3 x E
quantum vertex chiral group is related to the Hitchin system at genus 2. The
spectral network on the genus-2 curve C might encode the same BPS data as
the Weyl chamber decomposition of the K3 x E positive cone.

This is speculative but geometrically motivated. If true, it would mean:
- The spectral network on the genus-2 curve (1d network on a 2d surface)
  encodes the K3 x E BPS spectrum
- The Borcherds lift is the passage from the spectral network data to the
  automorphic form
- The spectral network provides the missing link between toric (local) and
  automorphic (global) CY3 data

### 3.4. Summary of the bridging role

| CY3 type | Spectral network lives on | Network type | Generating function |
|----------|--------------------------|-------------|-------------------|
| C^3 | point (trivial) | trivial | MacMahon M(q) |
| Resolved conifold | P^1 (2 branch pts) | finite graph | M(q)^2 * dilog |
| Local CY3 = T*C | curve C | GMN network | DT partition fn |
| K3 x E | P^1 (24 fibers) or genus-2 curve | Weyl chamber / higher network | Delta_5 |
| Compact CY3 (quintic) | ??? | ??? | Z^DT(quintic) |

The spectral network bridges the toric and automorphic cases *within the class S
realm* (i.e., for CY3s that are Hitchin systems). For K3 x E, it provides the
bridge *conjecturally*, via the genus-2 Hitchin connection. For general compact
CY3s, the spectral network picture is still missing — the "combinatorial datum"
would need to be defined intrinsically from the CY category, not from a Hitchin
system.

---

## 4. Synthesis with the existing framework

The spectral network proposal integrates cleanly with the existing codebase:

### 4.1. The MC element Theta_A (physics_wall_crossing_mc.tex)

The spectral network CONCRETIZES the MC element:
- Theta_A(t) = sum_gamma Omega(gamma; t) Theta_gamma^{prim} x^gamma
  (eq. 3.3 of physics_wall_crossing_mc.tex)
- The spectral network W(phi, theta) at stability condition (phi, theta)
  is the *geometric realization* of the MC element Theta_A(phi, theta)
- Each wall of type gamma with multiplicity Omega(gamma) in the network
  corresponds to the summand Omega(gamma) Theta_gamma^{prim} x^gamma in Theta_A
- The consistency condition at joints (trivial monodromy) is the MC equation

### 4.2. The scattering diagram (physics_wall_crossing_mc.tex, Sec. 4.3)

The scattering diagram and the spectral network are DUAL descriptions:
- The scattering diagram lives in the *charge lattice* Gamma_R
  (the Z-plane)
- The spectral network lives on the *curve* C (the UV curve)
- They encode the same data: the scattering diagram records
  which BPS states exist (their charges and multiplicities),
  while the spectral network records WHERE on C they are
  localized

The scattering diagram is the "momentum space" picture;
the spectral network is the "position space" picture.
This is a familiar Fourier duality.

### 4.3. The attractor mechanism (physics_wall_crossing_mc.tex, Sec. 5)

The attractor MC element Theta_A^* corresponds to a specific spectral network:
the one at the attractor phase theta_*(gamma) = arg Z_gamma(u_*). At this
phase, the network is "maximally simple" (no bound states), corresponding
to the split BPS spectrum with Omega(gamma) = Omega_*(gamma) (single-centered
invariants only).

### 4.4. The topological vertex (physics_topological_strings.tex, Sec. 4)

For toric CY3, the topological vertex factorization

    Z(X) = sum_{lambda_e} prod_v C_{lambda} prod_e (-Q_e)^{|lambda|}

is the *tropical limit* of the spectral network generating function.
The local root data R_v at each vertex is the data of the spectral
network restricted to a neighborhood of the corresponding branch point.

### 4.5. The shadow tower (physics_bps_root_multiplicities.tex, Sec. 5)

The shadow tower has a spectral network interpretation:
- Arity 2 (kappa): the "skeleton" of the spectral network (the walls
  originating from branch points, before any interactions)
- Arity 3: the first joints (where two walls collide, creating a new wall)
- Arity r: joints of order r (where r walls interact)
- Full tower: the complete spectral network with all interactions resolved

This is exactly the perturbative expansion of the spectral network:
the tree-level data (arity 2) gives the WKB approximation, and the
higher-order corrections (arity >= 3) give the exact (non-perturbative)
network.

---

## 5. Concrete programme for incorporation

### 5.1. For class S theories (immediate)

The spectral network is already implicit in the existing codebase
(physics_4d_n2_hitchin.tex, Remark 4.7 mentions it explicitly). To make it
central:

1. **Define** the spectral network W(phi, theta) as the concrete geometric
   realization of the MC element Theta_A at stability condition (phi, theta).

2. **Prove** that the spectral network consistency condition (trivial monodromy
   at joints) is equivalent to the MC equation for Theta_A.

3. **Identify** the spectral network flip (wall-crossing) with the gauge
   transformation e^{alpha} . Theta_A.

4. **Show** that the generating function of the spectral network is the
   bar-complex Euler product / denominator identity.

These are essentially repackaging of known results (GMN 2013, Bridgeland 2019)
in the Vol III language.

### 5.2. For K3 x E (conjectural)

1. **Formulate** the "higher spectral network" on the base of the K3 fibration
   (P^1) or on a genus-2 curve, encoding the K3 x E BPS spectrum.

2. **Identify** the walls with elements of the W^{(2)} reflection group, and
   the chambers with fundamental domains.

3. **Show** that the Borcherds lift phi_{0,1} -> Delta_5 is the passage from
   the fiber-wise spectral data to the total spectral network generating
   function.

4. **Connect** to the Hitchin system at genus 2 via the Sp_4(Z) = SO_+(3,2)
   symmetry group.

### 5.3. For general CY3 (speculative)

1. **Define** a "spectral network" intrinsically from the CY3 category C_X,
   without reference to a Hitchin system. The network would live on a
   suitable "base space" extracted from Stab(C_X).

2. **Show** that the consistency conditions of this abstract spectral network
   are equivalent to the MC equation for Theta_A in g^{mod}_A.

3. **Recover** the denominator identity as the generating function of the
   abstract spectral network.

---

## 6. Critical gaps and obstructions

### 6.1. Compact CY3s are not class S theories

The most serious obstacle: the spectral network is defined for class S theories
(4d N=2 theories from 6d (2,0) on a curve), which correspond to LOCAL CY3
geometries. For COMPACT CY3s (the quintic, K3 x E), there is no canonical
curve C on which to place the spectral network.

Possible resolutions:
- The "base" for the spectral network comes from the Hitchin system on the
  moduli of the CY itself (not a fixed curve C)
- The spectral network generalizes to a "spectral sheaf" on a higher-dimensional
  base
- The compact CY3 data is obtained by "compactifying" the spectral network
  data from a non-compact (local) limit

### 6.2. K3 x E: the Hitchin system at genus 2

The proposed connection between K3 x E and the genus-2 Hitchin system is
suggestive but not established. Key missing pieces:
- Is there a precise map from the K3 x E BPS spectrum to the genus-2 Hitchin
  BPS spectrum?
- Does the Sp_4(Z) symmetry of Delta_5 coincide with the modular group of the
  genus-2 Hitchin system?
- What is the role of the Narain lattice Lambda^{3,2} vs. the Hitchin lattice
  H_1(Sigma, Z)?

### 6.3. The refinement (motivic) structure

The spectral network as defined by GMN encodes the NUMERICAL BPS invariants
Omega(gamma). The REFINED (motivic) invariants Omega(gamma; y) require a
refined spectral network — this exists (the "motivic spectral network" of
GMN and Galakhov--Longhi--Moore) but is more complex. The motivic lift is
needed for the full root datum (including the grading by conformal weight,
as in physics_bps_root_multiplicities.tex, Sec. 6.2).

### 6.4. Uniqueness

Is the spectral network the UNIQUE combinatorial datum with these properties?
Other candidates include:
- The scattering diagram (tropical datum in the charge lattice — dual to
  the spectral network)
- The Bridgeland stability manifold Stab(C_X) (the ambient space, not the
  datum itself)
- The cluster variety (Fock--Goncharov coordinates)
- The BPS quiver (Alim--Cecotti--Cordova--Espahbodi--Vafa)

These are all EQUIVALENT encodings of the same data. The spectral network is
distinguished by being the most GEOMETRIC: it lives on a physical space (the
curve C), it has a natural topology (the wall structure), and it has a natural
evolution (the flow with theta). But it is not "more fundamental" than the
scattering diagram or the BPS quiver — they are Fourier/tropical duals of each
other.

---

## 7. Verdict

**The spectral network is a natural and powerful concrete realization of the
MC element Theta_A for class S theories.** It makes geometric the abstract
L_infty / MC gauge equivalence structure of the quantum vertex chiral group.

**Strengths:**
- Provides the concrete geometric realization of the MC element, scattering
  diagram, and wall-crossing formula
- The GMN = KS equivalence is a theorem, directly confirming the
  physics_wall_crossing_mc.tex framework
- Natural tropical/combinatorial structure that bridges tree-level (toric vertex)
  and full BPS data
- The spectral network is defined for any Hitchin system, covering all class S
  theories

**Limitations:**
- Defined only for class S theories (local CY3s from Hitchin systems), not for
  general compact CY3s
- The extension to K3 x E requires the (conjectural) genus-2 Hitchin connection
  or a higher-dimensional generalization
- Not "more fundamental" than the scattering diagram — it is a dual/equivalent
  description

**Recommendation for the programme:** The spectral network should be adopted as
the *preferred geometric realization* of the MC element Theta_A for class S
theories, alongside the scattering diagram as the dual *tropical realization*
in the charge lattice. The K3 x E case requires the Weyl chamber decomposition
/ genus-2 Hitchin generalization, which is a genuinely new construction that
could form the basis of a conjecture in the main text.

---

## References

- Gaiotto--Moore--Neitzke, "Wall-crossing, Hitchin systems, and the WKB
  approximation", Adv. Math. 234 (2013), 239-403. [The foundational paper]
- Gaiotto--Moore--Neitzke, "Spectral networks", Annales Henri Poincare 14
  (2013), 1643-1731. [The definition and basic properties]
- Gaiotto--Moore--Neitzke, "Spectral networks and snakes", Annales Henri
  Poincare 15 (2014), 61-141. [Rank-2 classification]
- Bridgeland, "Riemann-Hilbert problems from Donaldson-Thomas theory",
  Invent. Math. 216 (2019), 69-124. [Mathematical framework: Stab <-> connections]
- Kontsevich--Soibelman, "Stability structures, motivic DT invariants and
  cluster transformations" (2008). [The KS wall-crossing formula]
- Gross--Pandharipande--Siebert, "The tropical vertex", Duke Math. J. 153
  (2010), 297-362. [Tropical/scattering diagram framework]
- Fock--Goncharov, "Moduli spaces of local systems and higher Teichmuller
  theory", Publ. Math. IHES 103 (2006), 1-211. [Cluster coordinates
  parametrized by spectral networks]
- Galakhov--Longhi--Moore, "Spectral networks with spin", Commun. Math.
  Phys. 340 (2015), 171-232. [Refined/motivic spectral networks]

---

## Relevance to existing codebase files

- `notes/physics_wall_crossing_mc.tex`: The spectral network concretizes the
  scattering diagram / tropical MC interpretation (Sec. 4.3). The GMN reference
  is already cited ([10]). The spectral network should be incorporated as the
  geometric dual of the scattering diagram.

- `notes/physics_4d_n2_hitchin.tex`: Remark 4.7 already mentions spectral
  networks in connection with scattering diagrams. The spectral network should
  be promoted from a remark to a central construction, as the concrete
  realization of the MC element for class S theories.

- `notes/physics_3d_mirror.tex`: Item 8 of Sec. 7 mentions spectral networks
  explicitly ("recover the wall-crossing of spectral networks (GMN)"). The
  spectral network provides the link between the 3d mirror symmetry story and
  the 4d N=2 wall-crossing story.

- `notes/theory_cy2_cy3_fibration.tex`: The Borcherds lift phi_{0,1} -> Delta_5
  should be interpreted as the "fibered spectral network" construction: the
  fiber-wise spectral data (K3 elliptic genus) is assembled into the total
  automorphic form by summing over the lattice.

- `notes/physics_topological_strings.tex`: The topological vertex
  factorization is the tropical limit of the spectral network generating
  function for toric CY3s.
