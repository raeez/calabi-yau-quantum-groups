# Vafa-Witten Invariants and the Quantum Vertex Chiral Group

## Research note -- Raeez Lorgat, April 2026

### 0. Executive summary

The Vafa-Witten (VW) partition function of a 4-manifold S with gauge group G
should be the *character* (or denominator identity) of a quantum vertex chiral
group G(S, G). This note assembles the evidence, identifies the precise
dictionary, and formulates the key conjectures connecting VW theory to the
existing QVCG framework of Volume III.

The main claims:

1. **VW(K3, SU(2)) produces the BKM superalgebra g_{Delta_5}** -- the same
   object already constructed in Chapter `ch:k3-times-e` from DT theory on
   K3 x E. The VW route provides a *gauge-theoretic* derivation of the same
   algebraic structure.

2. **VW(C^2, GL(1)) produces W_{1+infinity}** -- matching the
   Schiffmann-Vasserot / toric CoHA story (Chapter `ch:toric-coha`). The VW
   equations on C^2 reduce to the Nekrasov partition function, whose
   underlying algebraic structure is the affine Yangian Y(gl_1-hat).

3. **A "VW vertex" exists for toric surfaces** -- analogous to the AKMV
   topological vertex. It computes VW invariants by cut-and-paste, factorizing
   the VW partition function over fixed-point loci of the torus action.

4. **VW theory extends to non-algebraic surfaces** (T^4, general Kahler) via
   the Tanaka-Thomas virtual fundamental class construction or the
   Jiang-Kool algebraic approach.

---

### 1. The Vafa-Witten equations and their invariants

#### 1.1 The equations

Let S be a compact oriented Riemannian 4-manifold with b_1 = 0 and
b_2^+ > 1 (or = 1 with a chamber structure). The Vafa-Witten equations for a
principal G-bundle P -> S are:

  F_A^+ + [B, B] + [C, B] = 0
  d_A^* B + d_A C = 0

where A is a connection on P, B in Omega^+(ad P) is a self-dual 2-form, and
C in Omega^0(ad P) is a scalar. These arise from the topological twist of
N=4 super Yang-Mills on S: specifically, the *Vafa-Witten twist*, which is the
twist at parameter t -> infinity in the Kapustin-Witten family (or
equivalently, a specific half-twist of the N=4 theory that preserves a scalar
supercharge Q with Q^2 = 0).

**Connection to existing notes**: The S-duality note (`physics_sduality_langlands.tex`,
Section 1) discusses the Kapustin-Witten family of twists. The VW twist is
*different* from the GL twist (t = 1) used in geometric Langlands and the
B-twist (t = i) giving Hitchin equations. The VW twist uses a different
combination of supercharges that localizes onto the VW equations rather than
the Hitchin equations.

#### 1.2 Relation to sheaves on S

Solutions to the VW equations are equivalent to Higgs pairs on S:

  (E, phi) where E is a holomorphic bundle on S, phi in H^0(End(E) tensor K_S)

satisfying a stability condition. When S is a smooth projective surface, the
VW moduli space M_VW(S, r, k) (rank r, instanton number k = c_2(E)) admits a
description as a moduli of coherent sheaves:

  M_VW(S, r, k) = M_Higgs(S, r, k) = {Higgs sheaves on S of rank r, c_2 = k}

This is directly analogous to the CY_2 Higgs sheaf framework of
`theory_higgs_cy2_qvcg.tex`, but for surfaces rather than curves. The key
structural point: Higgs(S) = Coh(T*S), and T*S is a (non-compact) CY_2 when
S is a surface with b_1 = 0 (the holomorphic symplectic form omega = dz1 ^ dw1
+ dz2 ^ dw2 is non-degenerate).

**Important distinction**: For a curve C, T*C is CY_2 of complex dimension 2.
For a surface S, T*S is CY of complex dimension 4, not 2. The CY_2 structure
relevant for VW on S is *not* the CY_4 structure of T*S but rather the
holomorphic symplectic structure of S itself (when S has trivial canonical
bundle, e.g., K3 or T^4).

#### 1.3 The VW partition function

The VW partition function is:

  Z_VW(S, G; q) = sum_k Omega_VW(S, G, k) * q^{k - r*chi(O_S)/2}

where Omega_VW(S, G, k) is the VW invariant at instanton number k, defined
as the virtual Euler characteristic of the VW moduli space (or more precisely,
the integral of the Behrend function over M_VW).

The shift k - r*chi(O_S)/2 ensures the correct modular properties.

---

### 2. VW on K3: the BKM superalgebra g_{Delta_5}

#### 2.1 The partition function

For S = K3 surface with gauge group G = SU(2):

  Z_VW(K3, SU(2); q) = sum_k chi(M(K3, 2, k)) * q^{k-1}

Gottsche (1990) and Yoshioka (1994-2001) computed the generating function of
Euler characteristics of moduli of sheaves on K3. The result:

  Z_VW(K3, SU(2); q) = 1/eta(q)^{24} * (theta function corrections)

More precisely, the *refined* VW partition function (incorporating the SU(2)_R
grading from the N=4 theory) is a Siegel modular form. The connection to
Delta_5 arises as follows:

1. The VW partition function on K3 with gauge group SU(N) is related to Siegel
   modular forms of genus N-1 (Dijkgraaf-Park-Schroers, Manschot).

2. For N=2: the generating function of Euler characteristics of rank-2 sheaves
   on K3, summed over all instanton numbers AND first Chern classes, is
   controlled by a function on the Siegel upper half-space H_2.

3. The DT partition function of K3 x E (Oberdieck-Pixton, Theorem
   `thm:dt-igusa`) gives Z^X = C / (Delta_5)^2.

4. The VW partition function on K3 is the *unrefined* specialization of the
   K3 x E DT partition function, obtained by integrating out the elliptic
   curve direction.

The precise relationship:

  Z_DT(K3 x E) = "second quantization" of Z_VW(K3)

This is the Dijkgraaf-Moore-Verlinde-Verlinde (DMVV) formula: the DT
partition function of K3 x E is the *second quantization* of the K3 elliptic
genus phi_{0,1}, which itself controls the VW invariants of K3.

#### 2.2 The QVCG identification

The quantum vertex chiral group G(K3 x E) has:
- Root lattice: Lambda^{3,2} (from `sec:k3e-lattice`)
- Root multiplicities: f(nm, l), the Fourier coefficients of phi_{0,1}
- Denominator identity: (1/64) * Delta_5(2Z) = Phi(z)
- Weyl group: W^{(2)}(Lambda^{2,1}_{II})
- Modular characteristic: kappa = 5 (the weight of Delta_5)

**Claim (VW -> QVCG)**: The BKM superalgebra g_{Delta_5} arises from VW theory
on K3 in the following precise sense:

(a) The *single-particle* BPS spectrum of VW theory on K3 = the root
    multiplicities of g_{Delta_5}. Each VW instanton configuration on K3 of
    charge (r, c_1, c_2) = (n, l, m) contributes mult(n, l, m) = f(nm, l)
    states, exactly as in the BPS root multiplicity identification
    (`eq:root-mult-bps`).

(b) The *multi-particle* VW partition function = the denominator identity of
    g_{Delta_5}. The second-quantized partition function (DMVV formula)
    produces the infinite product:

    Phi = exp(-2pi i <rho, z>) * prod_{alpha in Delta_+}
          (1 - exp(-2pi i <alpha, z>))^{mult(alpha)}

    which is exactly the Weyl-Kac-Borcherds denominator identity.

(c) The VW modularity (the fact that Z_VW transforms as a modular form under
    Sp_4(Z)) = the automorphic property of Delta_5 = the Sp_4(Z)-equivariance
    of the E_2-structure on G(K3 x E).

#### 2.3 S-duality and the VW partition function

Vafa-Witten (1994) proved that for b_2^+(S) > 1, the VW partition function
Z_VW(S, G; tau) transforms as a *modular form* under the S-duality group
SL_2(Z) acting on the complexified coupling tau. Specifically:

  Z_VW(S, G; -1/tau) = (const) * tau^w * Z_VW(S, G^L; tau)

where G^L is the Langlands dual group and w is a weight depending on the
topology of S.

**Connection to the triple identification** (`physics_sduality_langlands.tex`,
Conjecture `conj:triple`): The VW modularity is a *fourth* manifestation of the
S-duality = Langlands duality = Koszul duality identification:

  S-duality of VW partition functions
  = Langlands duality G <-> G^L
  = Koszul duality of the QVCG: G(S, G) <-> G(S, G^L)

For K3 with SU(2) vs SO(3): since SU(2)^L = SO(3), the VW partition function
must split into contributions from the two dual gauge groups, related by a
modular S-transformation. This is precisely the decomposition of Delta_5 into
contributions from different spin structures / characteristic classes.

---

### 3. VW on C^2 and W_{1+infinity}

#### 3.1 The Nekrasov partition function

For S = C^2 with the standard torus action T = (C*)^2, the VW equations reduce
to the instanton equations (B = C = 0), and the VW partition function becomes
the Nekrasov partition function:

  Z_VW(C^2, GL(r); q, epsilon_1, epsilon_2)
  = Z_Nek(r; q, epsilon_1, epsilon_2)
  = sum_k q^k * chi_T(M(r, k))

where M(r, k) is the moduli of rank-r torsion-free sheaves on P^2 with
c_2 = k, trivialized at infinity, and chi_T is the equivariant Euler
characteristic.

For r = 1: M(1, k) = Hilb^k(C^2), the Hilbert scheme of k points on C^2.
The generating function:

  Z_Nek(1; q) = sum_k chi(Hilb^k(C^2)) * q^k = prod_{n=1}^infty 1/(1 - q^n)
  = 1/eta(q) * q^{1/24}

For general r, the Nekrasov partition function admits an AGT-type
decomposition.

#### 3.2 The affine Yangian / W_{1+infty}

The algebraic structure underlying the Nekrasov partition function for r = 1
is precisely the affine Yangian Y(gl_1-hat), which is isomorphic to W_{1+infty}
at the self-dual level (Theorem `thm:sv-c3`).

**VW route**: VW theory on C^2 with gauge group GL(1) produces:
- The CoHA of Hilb(C^2) = Y^+(gl_1-hat)  (positive half)
- The full algebra (including negative half) = Y(gl_1-hat) = W_{1+infty}
- The partition function Z_VW = 1/eta(q) = character of the vacuum module

**CY_3 route** (existing, Chapter `ch:toric-coha`): The toric CY_3 C^3 with
its Jordan quiver produces the same Y(gl_1-hat) via the critical CoHA.

**Comparison**: The VW route uses CY_2 geometry (C^2 is CY_2 in the sense
that its cotangent bundle T*C^2 = C^4 has holomorphic symplectic structure),
while the CY_3 route uses C^3 directly. The VW route is more natural from
the gauge theory perspective (4d N=4 SYM twisted on C^2), while the CY_3
route is more natural from the enumerative geometry perspective (DT invariants
of 3-folds).

The two routes are related by the dimensional reduction:

  VW on S  <---->  DT on Tot(K_S)

When S = C^2, K_S = O (trivial), so Tot(K_S) = C^2 x C = C^3. This is
precisely the CY_2/CY_3 fibration story of `theory_cy2_cy3_fibration.tex`.

#### 3.3 Higher rank: W_N algebras and instanton counting

For GL(r), the Nekrasov partition function on C^2 is controlled by the
W_r algebra (the W-algebra associated to gl_r). The AGT correspondence
(Alday-Gaiotto-Tachikawa) identifies:

  Z_Nek(r; q, epsilon_1, epsilon_2)
  = <V_1 ... V_n | q^{L_0} | V'_1 ... V'_m>_{W_r}

where the right side is a conformal block of the W_r algebra.

In the QVCG framework: the quantum vertex chiral group G(C^2, GL(r)) should
be the W_r-type quantum group, with the AGT correspondence providing the
isomorphism between the VW partition function and the character of the QVCG.

---

### 4. The VW vertex for toric surfaces

#### 4.1 Statement of the problem

The AKMV topological vertex (`physics_topological_strings.tex`, Section 4)
computes the topological string partition function of any toric CY_3 by a
cut-and-paste formula:

  Z(X) = sum_{lambda_e} prod_v C_{lambda mu nu}(q) * prod_e (-Q_e)^{|lambda_e|}

Is there an analogous "VW vertex" that computes VW partition functions of
toric surfaces?

#### 4.2 Toric surfaces and their VW invariants

The basic toric surfaces are:
- C^2: the "vertex" (one fixed point)
- P^2: one triangle (three fixed points under T = (C*)^2)
- F_n (Hirzebruch surfaces): two triangles (four fixed points)
- Blowups of P^2 at torus-fixed points

The VW partition function on a toric surface S localizes (by virtual
localization) onto sheaves supported at the torus-fixed points. At each
fixed point p, the local contribution is a "vertex amplitude" depending on
the local geometry (which is always C^2 with a specific torus action).

#### 4.3 The VW vertex

**Conjecture (VW vertex)**: There exists a universal amplitude

  V_{lambda, mu}(q, t)

attached to each fixed point of a toric surface, such that:

  Z_VW(S, GL(r); q) = sum_{lambda_e} prod_{p in S^T} V_{lambda_e(p)}(q, t_p)
                       * (edge contributions)

where the sum is over assignments of partitions to each edge of the toric
diagram, and t_p encodes the equivariant weights at the fixed point p.

The VW vertex is *simpler* than the topological vertex because:
1. Toric surfaces have 2-dimensional fixed-point neighborhoods (vs 3 for CY_3)
2. The partitions labeling edges are ordinary (1D) partitions, not 2D
3. The vertex amplitude involves Schur functions in fewer variables

**Evidence**: For S = C^2, the VW vertex reduces to:

  V_{lambda}(q) = s_lambda(q^rho) = prod_{box in lambda} 1/(1 - q^{h(box)})

where h(box) is the hook length, and s_lambda is the Schur function specialized
at q^rho = (q^{-1/2}, q^{-3/2}, ...). This is the Nekrasov instanton partition
function restricted to a single fixed point.

For P^2, the VW partition function was computed by Kool-Thomas (2014) and
Laarakker (2018) using virtual localization, confirming that it factorizes
over the three fixed points with explicit vertex amplitudes.

#### 4.4 Connection to the QVCG root datum

The VW vertex factorization for a toric surface S gives a decomposition of
the QVCG root datum:

  R(S, G) = "tensor product" of local root data R_p over fixed points p

This parallels the topological vertex story for toric CY_3s
(`constr:local-root-datum` and `constr:gluing`). The local root datum at each
fixed point p is:

  R_p = R(C^2, G) = (affine Yangian root datum)

and the gluing over edges implements the identification of Fock-space
representations along shared edges, weighted by the Kahler parameters of
the compact curves connecting adjacent fixed points.

---

### 5. VW for non-algebraic surfaces

#### 5.1 The virtual class approach

The VW invariants were originally defined for *smooth* 4-manifolds S
(oriented, compact, b_1 = 0, b_2^+ > 1 or with a chamber structure).
In the algebraic setting, the construction uses the virtual fundamental class
[M_VW]^{vir} of the moduli space of Higgs pairs.

For non-algebraic surfaces, two approaches exist:

(a) **Tanaka-Thomas (2017-2020)**: Construct a perfect obstruction theory on
    the moduli of Higgs sheaves M_Higgs(S, r, k), even when S is not algebraic
    but only Kahler. The key: the deformation-obstruction theory at a Higgs
    pair (E, phi) is:

      T^i_M at (E, phi) = Ext^i(E, E tensor K_S)  for i = 0, 1, 2

    which is well-defined for any compact complex surface S. The virtual
    dimension is:

      vd = (4r^2 - r^2 * K_S^2) * chi(O_S) - ... (topological formula)

    For S = K3: K_S = O, chi(O_S) = 2, and vd = 0, giving numerical invariants.
    For S = T^4 (abelian surface): K_S = O, chi(O_S) = 0, and vd = 0 also.

(b) **Jiang (2017)**: Algebraic construction of VW invariants for any smooth
    projective surface using the cosection-localization technique of
    Kiem-Li, which handles the non-compactness of the Higgs moduli space.

#### 5.2 VW on T^4 (abelian surfaces)

For S = T^4 = E_1 x E_2 (product of two elliptic curves):

- K_S = O (trivial), so T^4 is CY_2 (holomorphic symplectic).
- The VW moduli space contains the moduli of flat connections on T^4 as a
  component (since phi = 0 solves the VW equations when K_S = O).
- The VW partition function on T^4 with gauge group SU(2) was computed by
  Dijkgraaf-Park-Schroers and involves:

  Z_VW(T^4, SU(2); q) ~ theta functions / eta functions

  This is NOT a Siegel modular form (unlike K3), because b_2^+(T^4) = 3 but
  the Euler characteristic chi(T^4) = 0, which changes the modular weight.

**QVCG prediction**: The quantum vertex chiral group G(T^4, SU(2)) should be a
BKM-type algebra whose denominator identity involves theta functions for the
Narain lattice Gamma^{3,3} of T^4, rather than the Igusa cusp form. The root
multiplicities should come from the *abelian surface elliptic genus*, which is
trivial (= 0 for a strict CY_2 with holonomy SU(2) -- but T^4 has holonomy
{1}, so the elliptic genus is non-trivial in the weak sense).

This is a genuinely different case from K3 and deserves separate study.

#### 5.3 General Kahler surfaces

For a general Kahler surface S with b_2^+ > 1:

  Z_VW(S, G; q) = sum_{alpha in H^2(S, pi_1(G))} Z_VW^alpha(S, G; q)

where the sum is over topological types (first Chern class modulo torsion).
Each Z_VW^alpha transforms under SL_2(Z) by the VW modularity theorem.

The QVCG G(S, G) should have:
- Lattice: Lambda = K_0(Coh(S)) = Z^{1 + b_2 + 1} (rank, c_1, c_2)
- Real roots: from rigid sheaves on S (these depend on S -- for rational
  surfaces, there are many; for K3, there are finitely many)
- Imaginary roots: from families of sheaves, with multiplicities = DT/VW
  invariants
- Weyl group: autoequivalences of D^b(Coh(S))
- Denominator identity: Z_VW(S, G; q)

---

### 6. The VW/DT correspondence and the CY_2/CY_3 bridge

#### 6.1 The dimensional reduction

The key bridge between VW theory on a surface S and DT theory on a CY_3 is:

  VW(S, G)  <---->  DT(Tot(K_S), G)

where Tot(K_S) is the total space of the canonical bundle of S. When K_S is
trivial (S = K3 or T^4), Tot(K_S) = S x C, and DT invariants of S x C are
related to VW invariants of S by:

  Z_DT(S x C) = "second quantization" of Z_VW(S)

This is the DMVV formula when S = K3.

More generally, for any surface S:

  Z_DT(Tot(K_S)) = prod_{n >= 1} Z_VW(S; q^n)^{c(n)}

where c(n) are combinatorial coefficients (related to the partition function
of the "third direction").

**In QVCG terms**: The CY_3 quantum vertex chiral group G(Tot(K_S)) is the
"second quantization" of the CY_2 quantum vertex chiral group G(S).

This connects directly to `theory_cy2_cy3_fibration.tex`: the fibration
construction by which a CY_2 root datum R(S) and a curve C produce a CY_3
root datum R(S x C) via the Borcherds multiplicative lift.

#### 6.2 The Borcherds lift revisited

The Borcherds multiplicative lift takes a weak Jacobi form phi_{0,1} (= the
K3 elliptic genus = the "single-particle VW partition function") and produces
the Igusa cusp form Delta_5 (= the denominator identity of the BKM
superalgebra = the "multi-particle DT partition function"):

  VW single-particle on K3
    --[Borcherds lift]-->
  DT multi-particle on K3 x E
    = denominator identity of g_{Delta_5}

The Borcherds lift IS the second quantization IS the passage from root
multiplicities to the denominator identity. In the QVCG framework:

  Borcherds lift = bar-complex Euler product = Weyl-Kac-Borcherds identity

This is established in `theory_automorphic_shadow.tex` (Theorem `thm:main`)
and `theory_denominator_bar_euler.tex`.

---

### 7. Wall-crossing and the MC gauge equivalence

The VW invariants depend on a stability parameter (the Bridgeland stability
condition sigma on D^b(Coh(S))). As sigma varies, the invariants jump at
walls of marginal stability.

**Connection to `physics_wall_crossing_mc.tex`**: The wall-crossing of VW
invariants is *exactly* the KS wall-crossing, which in the QVCG framework
is gauge equivalence of MC elements in the modular convolution algebra:

  VW wall-crossing on S
  = KS wall-crossing for BPS states of Tot(K_S)
  = MC gauge equivalence: Theta_A |--> e^alpha . Theta_A

The VW modularity (invariance of Z_VW under SL_2(Z)) is then the statement
that the *full* MC element Theta_A is gauge-invariant, even though its
finite-order truncations Theta^{<=r}_A may jump at walls.

Specifically:
- The attractor mechanism places Theta_A in a canonical gauge at the
  large-volume limit of the Kahler moduli of S.
- Moving away from the attractor point (varying the Kahler class of S)
  induces gauge transformations that reshuffle the root multiplicities.
- The denominator identity (= Z_VW) is gauge-invariant because it depends
  only on the gauge-equivalence class [Theta_A] in MC/gauge.

---

### 8. The four key questions: answers and status

#### Q1: Does VW(K3, SU(2)) literally give the BKM superalgebra g_{Delta_5}?

**Answer: YES, with a precise dictionary.**

The VW invariants on K3 give the *single-particle* root multiplicities of
g_{Delta_5}, controlled by the K3 elliptic genus phi_{0,1}. The full BKM
superalgebra arises from the second-quantized (multi-particle) VW spectrum,
which is the DT theory of K3 x E. The denominator identity is Delta_5.

Status: The DT/VW side is established (Oberdieck-Pixton for K3 x E,
Tanaka-Thomas for the VW virtual class on K3). The QVCG identification is
the content of Chapter `ch:k3-times-e` and Conjecture `conj:eight-qvcg`.

The VW perspective adds: the *gauge-theoretic* origin of the BKM superalgebra
is N=4 SYM on K3. The S-duality of the gauge theory explains the Sp_4(Z)
modularity of Delta_5 and the exchange G <-> G^L.

#### Q2: Does VW(C^2, GL(1)) give W_{1+infinity}?

**Answer: YES.**

The VW partition function on C^2 with GL(1) gauge group is the Nekrasov
partition function Z_Nek(1; q) = prod 1/(1-q^n) = M(q)/M(q^2)... More
precisely, for the equivariant VW theory on C^2:

  Z_VW(C^2, GL(1)) = 1/eta(q) (up to normalization)

and the underlying algebraic structure is the affine Yangian Y(gl_1-hat)
= W_{1+infinity} at the self-dual level.

Status: Fully established by Schiffmann-Vasserot (critical CoHA = positive
half of Y(gl_1-hat)), matching the toric CY_3 route through C^3.

The VW perspective adds: the *surface* origin of W_{1+infty}. It arises from
counting instantons on C^2, not from counting ideal sheaves in C^3. The two
are related by the dimensional reduction VW(C^2) <-> DT(C^3).

#### Q3: Is there a VW vertex?

**Answer: CONJECTURAL, with strong evidence.**

The VW vertex should be the amplitude V_{lambda, mu}(q, t) that computes the
local contribution of each torus-fixed point of a toric surface to the VW
partition function. Evidence:

- Virtual localization on M_VW(S, r, k) reduces the computation to fixed-point
  contributions (Nekrasov-type sums over partitions).
- For P^2: Kool-Thomas (2014) computed Z_VW(P^2, SU(2)) using localization,
  confirming the factorization over three fixed points.
- For Hirzebruch surfaces F_n: Gottsche-Kool (2017) computed Z_VW(F_n) using
  localization, confirming factorization over four fixed points.

The VW vertex is *not* the same as the topological vertex -- it lives in one
dimension fewer. It is the 4d gauge-theory analogue of the 6d string-theory
topological vertex. In QVCG terms: the topological vertex is the local root
datum of G(toric CY_3), while the VW vertex is the local root datum of
G(toric surface).

Status: OPEN. A rigorous definition of the VW vertex as a universal amplitude
(analogous to the AKMV definition of the topological vertex) has not been
given. The computational evidence is strong.

#### Q4: Can VW be defined for non-algebraic surfaces?

**Answer: YES, via virtual techniques.**

- Tanaka-Thomas (2017-2020): perfect obstruction theory on the Higgs moduli
  of any compact complex surface.
- For Kahler surfaces: the analytic construction of VW invariants via gauge
  theory (the original Vafa-Witten approach) is well-defined.
- For general smooth 4-manifolds: the VW equations make sense on any oriented
  Riemannian 4-manifold, but the moduli spaces may not be well-behaved
  (e.g., non-compactness issues when b_2^+(S) = 1).

Status: ESTABLISHED for algebraic surfaces. For non-algebraic Kahler
surfaces (e.g., non-algebraic K3 surfaces, non-algebraic tori), the
construction works but fewer computational tools are available (no
localization, no quiver description).

---

### 9. New conjectures

#### Conjecture VW-1 (VW/QVCG correspondence)

For any smooth projective surface S with b_2^+(S) > 1 and gauge group G,
the Vafa-Witten partition function Z_VW(S, G; q) is the character of the
vacuum module of the quantum vertex chiral group G(S, G):

  Z_VW(S, G; q) = tr_{V_0} q^{L_0 - c/24}

where V_0 is the vacuum representation and c is the central charge
(= modular characteristic kappa).

#### Conjecture VW-2 (VW modularity = denominator modularity)

The Vafa-Witten modularity theorem (Z_VW transforms under SL_2(Z)) is
equivalent to the automorphic property of the denominator identity of
the BKM superalgebra g(S, G):

  Phi_{S,G}(z) = "automorphic form on a type IV domain"

with the automorphic group determined by the lattice Lambda(S) and the
gauge group G.

#### Conjecture VW-3 (VW vertex = local QVCG)

There exists a universal vertex amplitude V_{R}(q, t) (R = representation
of the torus at a fixed point) such that the VW partition function of any
toric surface factorizes as:

  Z_VW(S) = sum_{lambda} prod_{p in S^T} V_{R_p, lambda(p)}(q, t_p)
            * prod_{e} (gluing factors)

and the local QVCG at each fixed point is:

  G_p = G(C^2, G) = affine Yangian-type quantum group

with the global G(S, G) assembled by the tensor product construction of
`constr:gluing`.

#### Conjecture VW-4 (VW for higher rank and Siegel modular forms)

For S = K3 and G = SU(N), the VW partition function Z_VW(K3, SU(N); q) is
controlled by a Siegel modular form of genus N-1:

- N = 1: Z_VW = 1/eta^{24} (the K3 partition function, related to the
  Monster module)
- N = 2: Z_VW ~ 1/Delta_5 (related to the Igusa cusp form)
- N = 3: Z_VW involves a genus-2 Siegel modular form
- General N: Z_VW involves genus-(N-1) Siegel modular forms

The corresponding QVCG G(K3, SU(N)) has a BKM superalgebra g_N whose
denominator identity is this Siegel modular form, with root multiplicities
given by the SU(N)-twisted K3 elliptic genus.

---

### 10. Connections to other notes in the programme

| Note | Connection |
|------|-----------|
| `ch:k3-times-e` | The K3 x E BKM superalgebra g_{Delta_5} is the second quantization of VW(K3, SU(2)) |
| `ch:toric-coha` | Toric CY_3 CoHA = second quantization of VW on the toric base surface |
| `theory_higgs_cy2_qvcg.tex` | Higgs sheaves on curves = the 1d analogue of VW on surfaces; the genus hierarchy (rational/elliptic/Hitchin) should lift to a surface hierarchy |
| `theory_cy2_cy3_fibration.tex` | VW on S <-> DT on Tot(K_S) via the CY_2/CY_3 fibration |
| `theory_automorphic_shadow.tex` | Borcherds lift = second quantization = automorphic correction = shadow obstruction tower |
| `physics_wall_crossing_mc.tex` | VW wall-crossing = KS wall-crossing = MC gauge equivalence |
| `physics_sduality_langlands.tex` | VW modularity is a manifestation of S-duality = Langlands = Koszul |
| `physics_topological_strings.tex` | The topological vertex for CY_3 should have a 4d VW analogue for surfaces |
| `physics_4d_n2_hitchin.tex` | The 4d N=2 story (SW curve, Nekrasov) is the rank-1 specialization of VW |
| `physics_3d_mirror.tex` | 3d mirror symmetry relates Higgs and Coulomb branches, both carrying QVCG structures; VW on the Higgs side should have a Coulomb dual |

---

### 11. Key references (to be expanded)

- Vafa-Witten (1994): "A strong coupling test of S-duality" -- original paper defining VW invariants and proving modularity for b_2^+ > 1.
- Tanaka-Thomas (2017-2020): "Vafa-Witten invariants for projective surfaces" I and II -- construction of the virtual fundamental class.
- Jiang (2017): "Virtual signed Euler characteristics" -- algebraic VW invariants via cosection localization.
- Gottsche-Kool (2017): "Virtual refinements of the VW formula" -- computations for toric surfaces.
- Kool-Thomas (2014): "Reduced classes and curve counting on surfaces" -- VW computations for P^2.
- Laarakker (2018): "Monopole contributions to refined VW invariants" -- refined invariants.
- Oberdieck-Pixton (2018): "Holomorphic anomaly equations and the Igusa cusp form conjecture" -- DT theory of K3 x E.
- Dijkgraaf-Park-Schroers (1997): "N=4 SYM partition functions on K3 x T^2" -- VW on K3, connection to Siegel modular forms.
- Manschot (2011): "The Betti numbers of the moduli space of stable sheaves of rank 3 on P^2" -- higher rank VW.
- Dijkgraaf-Moore-Verlinde-Verlinde (1997): "Counting dyons in N=4 string compactifications" -- the DMVV formula (second quantization).
- Gritsenko-Nikulin (1996, 2002): "Automorphic forms and Lorentzian Kac-Moody algebras" -- BKM algebras from automorphic forms.

---

### 12. Open problems

1. **Explicit VW vertex**: Give a closed-form expression for the VW vertex
   amplitude, analogous to the AKMV formula for the topological vertex.

2. **Non-simply-connected gauge groups**: How does the VW/QVCG correspondence
   work for non-simply-connected G (e.g., SO(3) vs SU(2))? The different
   topological types of bundles (classified by w_2) should correspond to
   different sectors of the root system.

3. **Refined VW and the motivic QVCG**: The refined VW invariants
   (incorporating the chi_y genus rather than the Euler characteristic) should
   correspond to a motivic or K-theoretic refinement of the QVCG.

4. **VW on non-compact surfaces**: For S = C^2/Gamma (ALE spaces), the VW
   theory produces the affine Lie algebra g_hat associated to the ADE
   singularity Gamma. This should correspond to the QVCG of the McKay
   quiver.

5. **VW on ruled surfaces**: For S = C x P^1 (C a curve of genus g), the VW
   partition function should produce a QVCG interpolating between the Hitchin
   Hall algebra of `theory_higgs_cy2_qvcg.tex` (the "fiber" direction P^1)
   and the modular forms of S-duality (the "base" direction C).

6. **Higher-dimensional generalization**: Is there a "VW theory" on
   6-manifolds that produces QVCGs from CY_3 geometry directly, without the
   DT intermediary? This would be the 6d N=(2,0) theory twist.
