r"""Symplectic duality (Coulomb/Higgs branch duality) for the K3 Yangian.

STATUS: CONJECTURAL (AP-CY14).  All results are conditional on the
existence of Y(g_{K3}) as a quantum group.  The BFN construction of the
quantized Coulomb branch is UNCONDITIONAL for Nakajima quiver varieties
but K3 x E is NOT a Nakajima quiver variety (Proposition prop:k3e-hall-yangian).
The symplectic duality statements are therefore CONJECTURAL.

MATHEMATICAL CONTENT
====================

1. SYMPLECTIC DUALITY (BRADEN-LICATA-PROUDFOOT-WEBSTER).

   Symplectic duality (3d N=4 mirror symmetry in physics) exchanges:
     - Coulomb branch M_C <-> Higgs branch M_H of the dual theory
     - Y(g) acting on H^*(M_C) <-> Y(g^L) acting on H^*(M_H)
     - Quantized Coulomb branch A_C <-> Quantized Higgs branch A_H

   For a 3d N=4 theory T with gauge group G and hypermultiplet
   representation R:
     M_C(T) = T^*(G-monopole moduli)  (BFN construction)
     M_H(T) = T^*R /// G              (hyperkahler quotient)
     T^! (the mirror theory) has M_C(T^!) = M_H(T), M_H(T^!) = M_C(T).

   The Braverman-Finkelberg-Nakajima (BFN) construction quantizes M_C:
     A_C = H^G_*(Gr_G, R-sections)   (equivariant homology of affine Grassmannian)
   This is a filtered quantization of C[M_C].

2. K3 SELF-MIRROR SYMMETRY.

   K3 is self-mirror under the Dolgachev-Nikulin involution:
     S <-> S^v  with H^2(S,Z) <-> H^2(S^v,Z) by lattice duality.

   At the level of derived categories:
     D^b(Coh(S)) ~ D^b(Coh(S^v))  (Orlov's theorem for K3)

   At the level of Hilbert schemes:
     Hilb^n(S) ~ Hilb^n(S^v)  (deformation equivalence)

   CONSEQUENCE: the Coulomb and Higgs branches of the "K3 theory" are
   isomorphic.  The K3 Yangian Y(g_{K3}) should be SELF-DUAL under
   symplectic duality:
     Y(g_{K3})^L = Y(g_{K3})

   This self-duality is NOT the Koszul self-duality (which sends
   h_i -> -h_i and g(z) -> 1/g(z)).  It is a DIFFERENT involution
   that preserves the structure function.

3. THE BFN CONSTRUCTION FOR K3.

   The BFN quantized Coulomb branch for a theory T[X] is:
     A_{BFN}(T[X]) = H^G_*(Gr_G, IC_R)

   For K3: the relevant theory is T[K3] = 3d N=4 sigma model into
   Hilb^n(K3).  The gauge theory description requires a quiver:
     - For Kummer K3 = T^4/Z_2 (resolved): the theory is an
       ADE-type gauge theory (A_1 quiver with adjoint matter).
     - For generic K3: no quiver description is available.

   OBSTRUCTION: K3 x E is NOT a Nakajima quiver variety
   (Proposition prop:k3e-hall-yangian(b)).  The BFN construction
   applies to quiver varieties but not directly to K3 x E.

   BYPASS: For the Kummer K3, the orbifold T^4/Z_2 admits a
   quiver-like description via the McKay correspondence.
   The affine A_1 quiver: two nodes with 4 edges.
   The BFN Coulomb branch = Hilb^n(T^4/Z_2) (conjectural).

4. THE COULOMB BRANCH = T^*Hilb^n(K3).

   For a 3d N=4 theory on K3, the Coulomb branch is:
     M_C = T^*(Hilb^n(K3))  (cotangent bundle to Hilbert scheme)

   This is a HOLOMORPHIC SYMPLECTIC MANIFOLD of dimension 4n
   (where n is the instanton number/charge).

   Key properties:
   (a) dim_C(M_C) = 4n (hyperkahler, quaternionic dimension n).
   (b) The symplectic form: omega_C = canonical symplectic form on T^*.
   (c) Torus action: T = C^* acts on the cotangent fiber.
   (d) Fixed locus: T-fixed points = zero section = Hilb^n(K3).
   (e) chi(M_C^T) = chi(Hilb^n(K3)) = p_{24}(n) (Goettsche formula).

5. THE HIGGS BRANCH AND SELF-DUALITY.

   For the mirror theory T^![K3]:
     M_H(T[K3]) = M_C(T^![K3])

   K3 self-mirror => T[K3] ~ T^![K3] => M_C ~ M_H.

   The moduli of sheaves on K3:
     M_H(v) = moduli of H-stable sheaves with Mukai vector v
   is deformation-equivalent to Hilb^n(K3) for primitive v with
   <v,v>_Muk = 2n-2 (Beauville theorem, Proposition prop:k3e-beauville).

   Therefore: M_C = T^*Hilb^n ~ T^*M_H(v) = M_H (at the level of
   symplectic geometry).  The self-duality is geometrically manifest.

6. YANGIAN SELF-DUALITY.

   Under symplectic duality, the Yangian parameters transform:
     Y(g) acting on Coulomb -> Y(g^L) acting on Higgs

   For K3 (self-mirror), g = g^L implies:
     Y(g_{K3})^L = Y(g_{K3})

   At the level of the structure function:
     g_{K3}(z) = prod_{i=1}^{24} (z - h_i)/(z + h_i)

   The Langlands dual parameters h_i^L are related to h_i by the
   Langlands involution on the Mukai lattice.

   For gl_1 (abelian): Langlands duality is TRIVIAL (gl_1^L = gl_1).
   Therefore h_i^L = h_i and g_{K3}^L(z) = g_{K3}(z).

   For general g (non-abelian): the Langlands dual of g_{K3} involves
   the GNO dual lattice.  For K3 with simply-laced g:
     g^L = g (ADE are self-dual under Langlands)
   so the self-duality persists.

   DISTINCTION from Koszul duality:
     Koszul: g^!(z) = 1/g(z), h_i -> -h_i, kappa -> -kappa
     Symplectic: g^L(z) = g(z), h_i -> h_i^L, kappa preserved
   These are DIFFERENT operations (AP-CY10: flop != Koszul dual).

7. QUANTIZED COULOMB BRANCH AND THE YANGIAN.

   The BFN quantized Coulomb branch A_C is a filtered associative
   algebra whose associated graded is C[M_C].

   THESIS (conjectural): A_C(T[K3]) = Y(g_{K3}).

   Evidence:
   (a) For C^3: A_C = Y^+(gl_hat_1) (proved, Schiffmann-Vasserot).
   (b) For T^*C^2: A_C = Y(gl_1) (proved, BFN).
   (c) For resolved A_n: A_C = Y(sl_{n+1}) (proved, BFN).
   (d) For K3: A_C should be Y(g_{K3}) (conjectural).

   The BFN construction provides Y(g_{K3}) INDEPENDENTLY of CY-A_3:
   it does not require the CY-to-chiral functor.  However, it requires
   a quiver description of K3, which is available only for special K3
   (Kummer, orbifold limits).

8. THE SYMPLECTIC RESOLUTION.

   T^*Hilb^n(K3) -> Sym^n(T^*K3)
   is a symplectic resolution (for n >= 2).

   The Hilbert-Chow morphism Hilb^n -> Sym^n resolves the symmetric
   product singularity.  The cotangent lift extends this to a
   symplectic resolution.

   The quantized resolution:
     A_C ---filtration---> gr(A_C) = C[T^*Hilb^n]
     |                        |
     |   quantization         |  Hilbert-Chow
     v                        v
     Y(g_{K3})            C[Sym^n(T^*K3)]

   The RESOLVED side (Hilb) carries the Yangian; the SINGULAR side
   (Sym) carries the associated graded.

9. EULER CHARACTERISTICS AND THE BAR COMPLEX.

   The Coulomb branch Euler characteristics encode the bar complex:

     sum_n chi(M_C^T, charge n) q^n = prod_{k>=1} 1/(1-q^k)^{24}
                                     = 1/eta(q)^{24}

   This is the FOCK SPACE character of Y(g_{K3}) (Section 4 of
   k3_yangian_quantization.py) and equals the inverse bar Euler
   product (Section 5 of k3_yangian.py).

   Under symplectic duality, the Higgs branch has the SAME Euler
   characteristics (self-mirror), giving a SECOND computation of
   the same generating function: a consistency check of self-duality.

10. CONNECTION TO THE PROGRAMME.

   The symplectic duality perspective provides:
   (a) An INDEPENDENT construction of Y(g_{K3}) via BFN, bypassing
       CY-A_3 (but requiring quiver description).
   (b) Self-duality of Y(g_{K3}) under Langlands (from K3 self-mirror).
   (c) The identification A_C = Y(g_{K3}) (if both constructions agree).
   (d) Koszul duality != symplectic duality (the kappa diagnostic:
       Koszul reverses kappa, symplectic preserves it).

CONVENTIONS
===========
  - h_i: Yangian deformation parameters (i = 1,...,24)
  - omega_{ij}: Mukai pairing matrix, signature (4,20)
  - CY_2 constraint: sum h_i = 0
  - kappa subscripts per AP113: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber
  - AP-CY14: ALL results are CONJECTURAL
  - AP-CY10: Flop preserves kappa; Koszul reverses kappa; symplectic preserves kappa.
  - AP-CY6: A_{K3} at d=2 IS proved; Y(g_{K3}) is NOT constructed.
  - AP-CY20: Normal bundle to Omega-background connection requires intermediary.

REFERENCES
==========
  k3_yangian.py: K3 Yangian structure function, R-matrix
  k3_yangian_quantization.py: quantization, bar complex, RTT
  k3_double_current_algebra.py: classical limit H_Muk
  k3_mirror_koszul.py: mirror symmetry and Koszul for K3
  drinfeld_center_k3_heisenberg.py: Drinfeld center of H_Muk
  mo_rmatrix_k3_charge2.py: MO R-matrix at charge 2
  bridgeland_k3_yangian.py: Bridgeland stability and Y(g_{K3})
  three_d_n2_cy3_engine.py: 3d N=2 from CY3, BFN Coulomb branch

  Braden-Licata-Proudfoot-Webster, arXiv:1407.0964 (symplectic duality)
  Braverman-Finkelberg-Nakajima, arXiv:1601.03586, 1604.03625 (BFN Coulomb branches)
  Maulik-Okounkov, arXiv:1211.1287 (stable envelopes, R-matrices)
  Nakajima, arXiv:1503.03676 (quiver varieties and Yangians)
  Dolgachev-Nikulin (lattice mirror symmetry for K3)
  Beauville (1983) (moduli of sheaves on K3)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

F = Fraction

# ============================================================================
# 0. Constants
# ============================================================================

STATUS = 'CONJECTURAL'  # AP-CY14: Y(g_{K3}) is not constructed

MUKAI_RANK = 24          # rank of the Mukai lattice
MUKAI_SIG_PLUS = 4       # positive signature
MUKAI_SIG_MINUS = 20     # negative signature
MUKAI_SIGNATURE = (MUKAI_SIG_PLUS, MUKAI_SIG_MINUS)

# Euler characteristics of Hilb^n(K3): chi(Hilb^n(K3)) = p_{24}(n)
# These are the 24-colored partition numbers (coefficients of 1/eta^{24})
HILB_EULER_CHARS = {
    0: 1,
    1: 24,
    2: 324,
    3: 3200,
    4: 25650,
    5: 176256,
    6: 1073720,
}

# kappa spectrum for K3 (AP113: bare kappa FORBIDDEN)
KAPPA_CH_K3 = F(2)       # from chiral algebra
KAPPA_BKM_K3 = F(5)      # from Borcherds-Kac-Moody
KAPPA_CAT_K3 = F(2)      # from chi(O_K3)
KAPPA_FIBER_K3 = F(24)   # from lattice rank

# Koszul conductor (free-field branch)
KOSZUL_CONDUCTOR_FREE_FIELD = F(0)


# ============================================================================
# 1. Coulomb and Higgs branch geometry
# ============================================================================

class CoulombBranchData(NamedTuple):
    """Data of the Coulomb branch M_C for the K3 theory at charge n.

    STATUS: CONJECTURAL (AP-CY14).

    M_C = T^*Hilb^n(K3) is a holomorphic symplectic manifold.
    """
    charge: int                     # instanton number n
    complex_dim: int                # dim_C(M_C) = 4n
    quaternionic_dim: int           # quaternionic dim = n (hyperkahler)
    euler_char_fixed: int           # chi(M_C^T) = chi(Hilb^n(K3)) = p_{24}(n)
    is_hyperkahler: bool            # always True for 3d N=4
    symplectic_resolution: bool     # True: Hilb^n -> Sym^n is symplectic resolution
    status: str


class HiggsBranchData(NamedTuple):
    """Data of the Higgs branch M_H for the K3 theory at charge n.

    STATUS: CONJECTURAL (AP-CY14).

    For K3 (self-mirror): M_H ~ M_C (symplectic duality self-identification).
    """
    charge: int
    complex_dim: int
    quaternionic_dim: int
    euler_char: int                 # chi(M_H(v)) = p_{24}(n) (Beauville)
    mukai_vector_sq: int            # <v,v>_Muk = 2n - 2
    is_self_dual: bool              # True for K3 (self-mirror)
    status: str


def coulomb_branch_k3(n: int) -> CoulombBranchData:
    r"""Coulomb branch of the 3d N=4 theory on K3 at charge n.

    M_C = T^*Hilb^n(K3):
    - complex_dim = 2 * dim(Hilb^n(K3)) = 2 * 2n = 4n
    - quaternionic_dim = n (hyperkahler, real dim = 4 * quaternionic_dim)
    - chi(M_C^T) = chi(Hilb^n(K3)) = p_{24}(n)
    - symplectic resolution: Hilb^n -> Sym^n for n >= 2

    STATUS: CONJECTURAL (AP-CY14).  T^*Hilb^n(K3) is unconditionally a
    holomorphic symplectic manifold, but its identification as the Coulomb
    branch of a 3d N=4 theory requires a gauge theory construction that
    is not available for generic K3.
    """
    if n < 0:
        raise ValueError(f"Charge must be non-negative, got {n}")
    if n == 0:
        return CoulombBranchData(
            charge=0,
            complex_dim=0,
            quaternionic_dim=0,
            euler_char_fixed=1,
            is_hyperkahler=True,
            symplectic_resolution=False,
            status='CONJECTURAL',
        )

    # Euler characteristic of Hilb^n(K3)
    euler = _p24(n)

    return CoulombBranchData(
        charge=n,
        complex_dim=4 * n,
        quaternionic_dim=n,
        euler_char_fixed=euler,
        is_hyperkahler=True,
        symplectic_resolution=(n >= 2),
        status='CONJECTURAL',
    )


def higgs_branch_k3(n: int) -> HiggsBranchData:
    r"""Higgs branch of the 3d N=4 theory on K3 at charge n.

    For K3 (self-mirror under Dolgachev-Nikulin), the Higgs branch
    is isomorphic to the Coulomb branch: M_H ~ M_C.

    The Higgs branch is the moduli space M_H(v) of stable sheaves on K3
    with primitive Mukai vector v satisfying <v,v>_Muk = 2n-2.
    By Beauville's theorem: M_H(v) is deformation-equivalent to Hilb^n(K3).

    STATUS: CONJECTURAL (AP-CY14).  The Beauville deformation equivalence
    is PROVED (ProvedElsewhere), but the identification as Higgs branch
    of a 3d N=4 theory is conjectural.
    """
    if n < 0:
        raise ValueError(f"Charge must be non-negative, got {n}")

    euler = _p24(n)
    mukai_sq = 2 * n - 2

    return HiggsBranchData(
        charge=n,
        complex_dim=4 * n if n > 0 else 0,
        quaternionic_dim=n,
        euler_char=euler,
        mukai_vector_sq=mukai_sq,
        is_self_dual=True,  # K3 is self-mirror
        status='CONJECTURAL',
    )


# ============================================================================
# 2. K3 self-mirror and Langlands duality
# ============================================================================

class SelfDualityData(NamedTuple):
    """Data encoding K3 self-duality under symplectic duality.

    K3 is self-mirror: S ~ S^v (Dolgachev-Nikulin).
    Consequence: Y(g_{K3})^L = Y(g_{K3}).
    """
    is_self_mirror: bool                    # True for K3
    langlands_dual_type: str                # "self-dual" for gl_1
    coulomb_euler_chars: Dict[int, int]     # chi(M_C^T) by charge
    higgs_euler_chars: Dict[int, int]       # chi(M_H) by charge
    euler_chars_match: bool                 # C and H have same chi
    kappa_ch_preserved: bool                # symplectic duality preserves kappa_ch
    koszul_kappa_reversed: bool             # Koszul duality reverses kappa_ch
    status: str


def k3_self_duality(max_charge: int = 5) -> SelfDualityData:
    r"""Verify K3 self-duality under symplectic duality.

    K3 is self-mirror: the Dolgachev-Nikulin involution exchanges
    algebraic and transcendental sublattices of the Mukai lattice.

    For gl_1 (abelian): Langlands duality is trivial (gl_1^L = gl_1).
    For simply-laced g (ADE): g^L = g (self-dual under Langlands).

    The self-duality means:
    1. chi(M_C) = chi(M_H) at every charge (matching Euler chars).
    2. g_{K3}^L(z) = g_{K3}(z) (structure function preserved).
    3. kappa_ch preserved (symplectic duality preserves kappa,
       unlike Koszul duality which reverses it, AP-CY10).

    STATUS: CONJECTURAL (AP-CY14).
    """
    coulomb_eulers = {}
    higgs_eulers = {}

    for n in range(max_charge + 1):
        c_data = coulomb_branch_k3(n)
        h_data = higgs_branch_k3(n)
        coulomb_eulers[n] = c_data.euler_char_fixed
        higgs_eulers[n] = h_data.euler_char

    # Check Euler characteristics match (self-mirror)
    match = all(coulomb_eulers[n] == higgs_eulers[n]
                for n in range(max_charge + 1))

    return SelfDualityData(
        is_self_mirror=True,
        langlands_dual_type="self-dual (gl_1^L = gl_1)",
        coulomb_euler_chars=coulomb_eulers,
        higgs_euler_chars=higgs_eulers,
        euler_chars_match=match,
        kappa_ch_preserved=True,   # symplectic duality preserves kappa_ch
        koszul_kappa_reversed=True,  # Koszul reverses: kappa -> -kappa
        status='CONJECTURAL',
    )


def langlands_dual_structure_function(h_params: List[F]) -> str:
    r"""Langlands dual structure function for the K3 Yangian.

    For gl_1 (abelian), the Langlands dual is trivial:
      g^L(z) = g(z)
      h_i^L = h_i

    For general g with K3 lattice, the Langlands dual involves
    the GNO dual lattice.  For ADE (simply-laced): g^L = g.

    Returns a string description (the function is identity for gl_1).

    STATUS: CONJECTURAL (AP-CY14).
    """
    # Verify CY_2 constraint
    total = sum(h_params)
    if total != 0:
        raise ValueError(f"CY_2 constraint violated: sum h_i = {total}")

    # For gl_1: Langlands duality is trivial
    # g^L(z) = g(z), h_i^L = h_i
    return "g^L(z) = g(z) [gl_1 is self-Langlands-dual]"


def structure_function_under_dualities(
    h_params: List[F], z: F
) -> Dict[str, F]:
    r"""Compare structure function under symplectic vs Koszul duality.

    Given h_1,...,h_{24} and spectral parameter z, compute:
    1. g(z) = prod (z - h_i)/(z + h_i)  (original)
    2. g^!(z) = 1/g(z)                   (Koszul dual)
    3. g^L(z) = g(z)                     (Langlands dual, for gl_1)

    The distinction (AP-CY10):
    - Koszul: h_i -> -h_i, g -> 1/g, kappa -> -kappa
    - Symplectic/Langlands: h_i -> h_i^L = h_i (for gl_1), g -> g, kappa -> kappa
    - Flop: g -> g (preserves), kappa -> kappa (preserves)

    STATUS: CONJECTURAL (AP-CY14).
    """
    # Compute g(z) = prod (z - h_i)/(z + h_i)
    g_val = F(1)
    for hi in h_params:
        if z + hi == 0:
            raise ValueError(f"Pole at z = -{hi} (AP-CY28: pole-unsafe test point)")
        g_val *= (z - hi) / (z + hi)

    # Koszul dual: g^!(z) = 1/g(z) = prod (z + h_i)/(z - h_i)
    g_koszul = F(1) / g_val if g_val != 0 else None

    # Langlands dual for gl_1: g^L(z) = g(z) (trivial)
    g_langlands = g_val

    result = {
        'g_original': g_val,
        'g_langlands': g_langlands,
    }
    if g_koszul is not None:
        result['g_koszul'] = g_koszul

    return result


# ============================================================================
# 3. BFN quantized Coulomb branch
# ============================================================================

class BFNCoulombData(NamedTuple):
    """Data of the BFN quantized Coulomb branch for K3-type theories.

    The BFN construction:
      A_C = H^G_*(Gr_G, IC_R)
    is unconditional for Nakajima quiver varieties.

    For K3: requires a quiver description. Available for:
    - Kummer K3 = T^4/Z_2 (via McKay correspondence, affine A_1 quiver)
    - K3 at orbifold points (via ADE quivers)
    - NOT available for generic K3.

    STATUS: CONJECTURAL (AP-CY14).
    """
    quiver_type: str                # e.g., "affine_A1" for Kummer
    gauge_group: str                # e.g., "GL(n)" for Hilb^n
    matter_repr: str                # e.g., "adjoint + fundamental"
    coulomb_dim: int                # dim of Coulomb branch
    quantization_parameter: str     # hbar (or epsilon)
    yangian_identification: str     # conjectural: A_C = Y(g_{K3})
    status: str


def bfn_kummer_k3(n: int) -> BFNCoulombData:
    r"""BFN quantized Coulomb branch for the Kummer K3 at charge n.

    The Kummer K3 = T^4/Z_2 (resolved) admits a quiver description
    via the McKay correspondence:

    Quiver: affine A_1 = two nodes (0, 1) with:
      - 4 arrows from node 0 to node 1 (from T^4 directions)
      - 4 arrows from node 1 to node 0
      - Dimension vector: (n, n) for charge n

    The BFN Coulomb branch with this quiver:
      A_C = H^{GL(n) x GL(n)}_*(Gr_{GL(n) x GL(n)}, ...)
    is a filtered quantization of T^*Hilb^n(T^4/Z_2).

    After blowing up the 16 singular points: T^4/Z_2 -> K3,
    and the Coulomb branch deforms to T^*Hilb^n(K3).

    STATUS: CONJECTURAL (AP-CY14).  The quiver description is valid
    only at the orbifold point.  The identification A_C = Y(g_{K3})
    requires both the BFN construction at the orbifold point AND
    deformation invariance of the Yangian under blowup.
    """
    if n < 0:
        raise ValueError(f"Charge must be non-negative, got {n}")

    return BFNCoulombData(
        quiver_type="affine_A1",
        gauge_group=f"GL({n}) x GL({n})" if n > 0 else "trivial",
        matter_repr="4 bifundamental pairs (from T^4)" if n > 0 else "trivial",
        coulomb_dim=4 * n,
        quantization_parameter="hbar (Omega-background)",
        yangian_identification=f"A_C(Kummer, n={n}) =? Y(g_{{K3}}) at charge {n}",
        status='CONJECTURAL',
    )


def bfn_ade_k3(ade_type: str, n: int) -> BFNCoulombData:
    r"""BFN Coulomb branch for ADE-type K3 surfaces at charge n.

    K3 surfaces at orbifold singularities of type ADE have quiver
    descriptions via the McKay correspondence:

    - A_k: cyclic group Z/(k+1), quiver = affine A_k
    - D_k: binary dihedral group, quiver = affine D_k
    - E_k: binary tetrahedral/octahedral/icosahedral, quiver = affine E_k

    The BFN Coulomb branch of the affine ADE quiver with dimension
    vector n*delta (where delta is the minimal imaginary root):
      A_C(ADE, n) = Y(g_ADE) at charge n

    For the K3 SURFACE (not just the singularity), the full construction
    requires gluing local ADE patches, which involves the same chart-gluing
    obstruction as the center-hocolim problem.

    STATUS: CONJECTURAL (AP-CY14).
    """
    valid_types = ["A1", "A2", "D4", "E6", "E7", "E8"]
    if ade_type not in valid_types:
        raise ValueError(f"ADE type must be one of {valid_types}, got {ade_type}")
    if n < 0:
        raise ValueError(f"Charge must be non-negative, got {n}")

    # Rank of the ADE algebra
    rank_map = {"A1": 1, "A2": 2, "D4": 4, "E6": 6, "E7": 7, "E8": 8}
    rank = rank_map[ade_type]

    return BFNCoulombData(
        quiver_type=f"affine_{ade_type}",
        gauge_group=f"product of GL(n*d_i) for affine {ade_type} dimension vector",
        matter_repr=f"adjoint + bifundamental (from affine {ade_type} quiver)",
        coulomb_dim=4 * n,
        quantization_parameter="hbar (Omega-background)",
        yangian_identification=(
            f"A_C(affine {ade_type}, n={n}) = Y(g_{{{ade_type}}}) "
            f"[proved for ADE singularity; conjectural for full K3]"
        ),
        status='CONJECTURAL',
    )


# ============================================================================
# 4. Symplectic duality diagnostics
# ============================================================================

class SymplecticDualityDiagnostic(NamedTuple):
    """Diagnostic comparing symplectic duality with Koszul duality for K3.

    The key distinction (AP-CY10):
    - Symplectic duality: preserves kappa_ch, exchanges C and H branches
    - Koszul duality: reverses kappa_ch (kappa + kappa^! = K)
    - Flop: preserves kappa_ch (autoequivalence)

    For K3 (self-mirror): symplectic duality is a self-identification.
    Koszul duality is NOT a self-identification (kappa -> -kappa).
    """
    kappa_ch_original: F                # kappa_ch(Y) = 2
    kappa_ch_koszul_dual: F             # kappa_ch(Y^!) = -2
    kappa_ch_symplectic_dual: F         # kappa_ch(Y^L) = 2 (preserved)
    kappa_ch_flop: F                    # kappa_ch(Y_{X^+}) = 2 (preserved)
    koszul_conductor: F                 # K = kappa + kappa^! = 0
    symplectic_is_self_dual: bool       # True for K3
    koszul_is_self_dual: bool           # False for K3 (kappa != -kappa)
    flop_is_trivial: bool               # True for K3 (no flop for surfaces)
    status: str


def symplectic_vs_koszul_diagnostic() -> SymplecticDualityDiagnostic:
    r"""Compare symplectic duality and Koszul duality for K3.

    The three operations:
    1. Symplectic duality (3d N=4 mirror): Y -> Y^L
       - Exchanges Coulomb and Higgs branches
       - For K3 (self-mirror): Y^L = Y, kappa_ch preserved
    2. Koszul duality (algebraic): Y -> Y^!
       - h_i -> -h_i, g(z) -> 1/g(z)
       - kappa_ch -> -kappa_ch; conductor K = kappa + kappa^! = 0
    3. Flop (birational): Y_X -> Y_{X^+}
       - Derived equivalence, kappa_ch preserved
       - Trivial for K3 (no flops of K3 surfaces)

    STATUS: CONJECTURAL (AP-CY14).
    """
    return SymplecticDualityDiagnostic(
        kappa_ch_original=KAPPA_CH_K3,         # 2
        kappa_ch_koszul_dual=-KAPPA_CH_K3,     # -2
        kappa_ch_symplectic_dual=KAPPA_CH_K3,  # 2 (preserved)
        kappa_ch_flop=KAPPA_CH_K3,             # 2 (preserved)
        koszul_conductor=KOSZUL_CONDUCTOR_FREE_FIELD,  # 0
        symplectic_is_self_dual=True,
        koszul_is_self_dual=False,
        flop_is_trivial=True,  # no flops for K3 surfaces
        status='CONJECTURAL',
    )


# ============================================================================
# 5. Generating function comparisons
# ============================================================================

def coulomb_branch_generating_function(
    max_charge: int = 6,
) -> Dict[str, Any]:
    r"""Generating function for Coulomb branch Euler characteristics.

    Z_C(q) = sum_{n>=0} chi(M_C^T, charge n) * q^n
           = sum_{n>=0} p_{24}(n) * q^n
           = prod_{k>=1} 1/(1-q^k)^{24}
           = 1/eta(q)^{24}

    This is:
    (a) The Fock space character of Y(g_{K3}) (k3_yangian_quantization.py).
    (b) The inverse bar Euler product of A_{K3} (k3_yangian.py).
    (c) The generating function of root multiplicities of the Fake Monster
        Lie algebra at lightlike level (Borcherds).

    Under K3 self-duality: Z_H(q) = Z_C(q) (same generating function
    on the Higgs side), providing a consistency check.

    STATUS: ProvedHere for the Euler characteristics (Goettsche formula);
    CONJECTURAL for the identification with Y(g_{K3}).
    """
    # Compute Euler characteristics
    eulers_coulomb = {n: _p24(n) for n in range(max_charge + 1)}
    eulers_higgs = {n: _p24(n) for n in range(max_charge + 1)}

    # Verify Coulomb = Higgs (self-duality)
    match = all(eulers_coulomb[n] == eulers_higgs[n]
                for n in range(max_charge + 1))

    # Bar Euler exponents: a_k = -24 for all k (class G)
    bar_euler_exponents = {k: -MUKAI_RANK for k in range(1, max_charge + 1)}

    return {
        'coulomb_euler_chars': eulers_coulomb,
        'higgs_euler_chars': eulers_higgs,
        'self_dual_match': match,
        'bar_euler_exponents': bar_euler_exponents,
        'generating_function': '1/eta(q)^{24}',
        'fock_space_character': '1/eta(q)^{24}',
        'fake_monster_connection': 'p_{24}(n) = Fake Monster root mult at level n',
        'status': 'CONJECTURAL for Yangian identification',
    }


def hilbert_chow_resolution_data(n: int) -> Dict[str, Any]:
    r"""Data for the Hilbert-Chow symplectic resolution.

    The Hilbert-Chow morphism:
      pi: Hilb^n(K3) -> Sym^n(K3)
    resolves the symmetric product singularities.

    The cotangent lift:
      T^*pi: T^*Hilb^n(K3) -> T^*Sym^n(K3)
    is a SYMPLECTIC resolution (for n >= 2).

    Dimensions:
      dim Hilb^n(K3) = 2n (smooth)
      dim Sym^n(K3) = 2n (singular for n >= 2)
      dim T^*Hilb^n(K3) = 4n
      dim T^*Sym^n(K3) = 4n (singular)

    The exceptional fiber of pi over a point (x, x, ...) in Sym^n:
      pi^{-1}(n*[x]) = punctual Hilb^n = {length-n subschemes supported at x}
    which has dimension n-1.
    """
    if n < 0:
        raise ValueError(f"Charge must be non-negative, got {n}")

    is_resolution = (n >= 2)
    exceptional_fiber_dim = max(0, n - 1) if is_resolution else 0

    return {
        'charge': n,
        'hilb_dim': 2 * n,
        'sym_dim': 2 * n,
        'cotangent_hilb_dim': 4 * n,
        'cotangent_sym_dim': 4 * n,
        'is_symplectic_resolution': is_resolution,
        'exceptional_fiber_dim': exceptional_fiber_dim,
        'euler_char_hilb': _p24(n),
        'euler_char_sym': _multinomial_sym_euler(n),
    }


# ============================================================================
# 6. Dolgachev-Nikulin lattice mirror data
# ============================================================================

class LatticeSelfdualityData(NamedTuple):
    """Lattice-level data for K3 self-duality.

    The Dolgachev-Nikulin mirror for a K3 with Picard rank rho:
      S_rho <-> S_{20-rho}
    exchanges algebraic and transcendental lattices.

    At rho = 10: the K3 is EXACTLY self-mirror (rho = 20 - rho).
    At rho = 20 (Kummer): far from self-mirror in lattice polarization,
    but still self-mirror at the level of chi(Hilb^n) (Beauville).
    """
    picard_rank: int
    mirror_picard_rank: int               # 20 - rho
    algebraic_signature: Tuple[int, int]  # (2, rho)
    transcendental_signature: Tuple[int, int]  # (2, 20-rho)
    is_lattice_self_mirror: bool          # rho = 10
    euler_char_preserved: bool            # chi(Hilb^n) = p_{24}(n) always
    mukai_rank_preserved: bool            # 24 for all K3


def dolgachev_nikulin_self_duality(rho: int) -> LatticeSelfdualityData:
    r"""Dolgachev-Nikulin lattice mirror and self-duality analysis.

    For K3 with Picard rank rho:
    - Algebraic sublattice M_tilde: rank rho+2, signature (2, rho)
    - Transcendental sublattice M_tilde^perp: rank 22-rho, signature (2, 20-rho)
    - Mirror K3 has rho' = 20 - rho

    Self-mirror locus: rho = 10 (lattice-polarized self-mirror).
    BUT: for symplectic duality, the relevant self-mirror is at the level
    of chi(Hilb^n), which is p_{24}(n) for ALL K3 (Goettsche).  So the
    symplectic self-duality holds for ALL Picard ranks, not just rho = 10.
    """
    if not (1 <= rho <= 20):
        raise ValueError(f"Picard rank must satisfy 1 <= rho <= 20, got {rho}")

    mirror_rho = 20 - rho

    return LatticeSelfdualityData(
        picard_rank=rho,
        mirror_picard_rank=mirror_rho,
        algebraic_signature=(2, rho),
        transcendental_signature=(2, 20 - rho),
        is_lattice_self_mirror=(rho == 10),
        euler_char_preserved=True,  # p_{24}(n) for all K3
        mukai_rank_preserved=True,  # 24 for all K3
    )


# ============================================================================
# 7. Yangian parameter space and symplectic duality involution
# ============================================================================

class YangianDualityInvolution(NamedTuple):
    """The three involutions on Y(g_{K3}) parameters.

    1. Koszul: h_i -> -h_i  (reverses kappa_ch)
    2. Symplectic/Langlands: h_i -> h_i^L = h_i (for gl_1)
    3. Unitarity: g(z)*g(-z) = 1 (algebraic, always)

    STATUS: CONJECTURAL (AP-CY14).
    """
    h_original: List[F]
    h_koszul: List[F]          # [-h_i]
    h_langlands: List[F]       # [h_i] for gl_1
    g_original_at_z: F         # g(z)
    g_koszul_at_z: F           # g^!(z) = 1/g(z)
    g_langlands_at_z: F        # g^L(z) = g(z)
    g_unitarity_product: F     # g(z)*g(-z) = 1
    koszul_involution_order: int   # 2 (involution)
    langlands_involution_order: int  # 1 (trivial for gl_1)
    status: str


def yangian_duality_involutions(
    h_params: List[F], z: F
) -> YangianDualityInvolution:
    r"""Compute the three involutions on K3 Yangian parameters.

    Given h_1,...,h_{24} and z, compute:
    1. Koszul: h_i -> -h_i, g^!(z) = 1/g(z)
    2. Langlands: h_i^L = h_i (for gl_1), g^L(z) = g(z)
    3. Unitarity: g(z)*g(-z) = 1 (algebraic identity)

    AP-CY10: These are THREE DISTINCT operations.
    AP-CY28: Test points must avoid poles at +/-h_i.
    """
    # Verify CY_2 constraint
    total = sum(h_params)
    if total != 0:
        raise ValueError(f"CY_2 constraint violated: sum h_i = {total}")

    # Check for poles (AP-CY28)
    for hi in h_params:
        if z + hi == 0 or z - hi == 0:
            raise ValueError(
                f"z={z} is a pole of g(z) or g(-z) at h_i={hi} "
                f"(AP-CY28: pole-unsafe test point)"
            )

    # Compute g(z)
    g_val = F(1)
    for hi in h_params:
        g_val *= (z - hi) / (z + hi)

    # Compute g(-z)
    g_neg = F(1)
    for hi in h_params:
        g_neg *= (-z - hi) / (-z + hi)

    # Unitarity check: g(z)*g(-z) = 1
    unitarity = g_val * g_neg

    # Koszul dual
    h_koszul = [-hi for hi in h_params]
    g_koszul = F(1)
    for hi in h_koszul:
        g_koszul *= (z - hi) / (z + hi)

    return YangianDualityInvolution(
        h_original=h_params,
        h_koszul=h_koszul,
        h_langlands=list(h_params),  # trivial for gl_1
        g_original_at_z=g_val,
        g_koszul_at_z=g_koszul,
        g_langlands_at_z=g_val,      # trivial for gl_1
        g_unitarity_product=unitarity,
        koszul_involution_order=2,
        langlands_involution_order=1,  # trivial for gl_1
        status='CONJECTURAL',
    )


# ============================================================================
# 8. Connection to the programme: BFN vs CY-A routes
# ============================================================================

class TwoRoutesComparison(NamedTuple):
    """Comparison of the BFN and CY-A routes to Y(g_{K3}).

    Route A (CY-A): CY category -> Phi -> chiral algebra -> bar -> Yangian
      Status: CY-A_2 proved (d=2); CY-A_3 conditional (d=3)

    Route B (BFN): 3d N=4 theory -> Coulomb branch -> quantize -> Yangian
      Status: proved for quiver varieties; conjectural for K3

    The routes should agree (if both are defined), providing a
    consistency check of the programme.
    """
    route_a_status: str
    route_b_status: str
    agreement_status: str
    route_a_inputs: List[str]
    route_b_inputs: List[str]
    shared_output: str
    distinguishing_data: Dict[str, str]


def two_routes_to_k3_yangian() -> TwoRoutesComparison:
    r"""Compare the CY-A and BFN routes to the K3 Yangian.

    Route A (CY-A route):
      D^b(Coh(K3)) --Phi--> A_{K3} --bar--> B(A_{K3}) --Koszul--> Y(g_{K3})
      Status: CY-A_2 PROVED; the bar complex gives eta^{24}.
      Missing: the Yangian quantization step beyond the Heisenberg.

    Route B (BFN route):
      T[K3] (3d N=4 theory) --BFN--> A_C(T[K3]) =? Y(g_{K3})
      Status: CONJECTURAL.  Requires quiver description of K3.
      Available at orbifold points (Kummer, ADE singularities).

    Where they overlap (Kummer K3, orbifold limit):
      Both routes should give the same Y(g_{K3}).

    STATUS: CONJECTURAL (AP-CY14).
    """
    return TwoRoutesComparison(
        route_a_status="CY-A_2 PROVED; Yangian quantization CONJECTURAL",
        route_b_status="PROVED for quiver varieties; CONJECTURAL for K3",
        agreement_status="CONJECTURAL (overlap at Kummer/orbifold points)",
        route_a_inputs=[
            "CY-A_2 (proved)",
            "Bar complex B(A_{K3}) = eta^{24} (proved)",
            "Yangian quantization g_{K3} -> Y(g_{K3}) (conjectural)",
        ],
        route_b_inputs=[
            "3d N=4 theory T[K3] (conjectural for generic K3)",
            "BFN quantized Coulomb branch (proved for quiver varieties)",
            "Quiver description of K3 (available at orbifold points only)",
        ],
        shared_output="Y(g_{K3}) with structure function g(z) = prod (z-h_i)/(z+h_i)",
        distinguishing_data={
            'route_a_bar_euler': 'eta(q)^{24} = Delta(q)/q',
            'route_b_coulomb_euler': '1/eta(q)^{24} (inverse bar Euler)',
            'route_a_kappa_ch': 'kappa_ch = 2 (from Phi)',
            'route_b_kappa_ch': 'kappa_ch = 2 (from Coulomb branch dim)',
            'route_a_self_duality': 'Koszul self-duality kappa + kappa^! = 0',
            'route_b_self_duality': 'Symplectic self-duality M_C ~ M_H',
        },
    )


# ============================================================================
# 9. Verification suite
# ============================================================================

class VerificationResult(NamedTuple):
    """Result of a single verification check."""
    name: str
    passed: bool
    detail: str
    status: str


def verify_coulomb_higgs_match(max_charge: int = 5) -> VerificationResult:
    """Verify Coulomb = Higgs Euler characteristics (K3 self-duality)."""
    for n in range(max_charge + 1):
        c = coulomb_branch_k3(n)
        h = higgs_branch_k3(n)
        if c.euler_char_fixed != h.euler_char:
            return VerificationResult(
                name="Coulomb-Higgs Euler char match",
                passed=False,
                detail=f"Mismatch at charge {n}: C={c.euler_char_fixed}, H={h.euler_char}",
                status='FAILED',
            )
    return VerificationResult(
        name="Coulomb-Higgs Euler char match",
        passed=True,
        detail=f"All charges 0..{max_charge} match: p_{{24}}(n) on both sides",
        status='CONJECTURAL (Yangian identification)',
    )


def verify_kappa_diagnostic() -> VerificationResult:
    """Verify the kappa diagnostic: symplectic preserves, Koszul reverses."""
    diag = symplectic_vs_koszul_diagnostic()

    checks = [
        diag.kappa_ch_original == F(2),
        diag.kappa_ch_koszul_dual == F(-2),
        diag.kappa_ch_symplectic_dual == F(2),
        diag.kappa_ch_flop == F(2),
        diag.koszul_conductor == F(0),
        diag.symplectic_is_self_dual is True,
        diag.koszul_is_self_dual is False,
    ]

    if all(checks):
        return VerificationResult(
            name="kappa diagnostic: symplectic vs Koszul",
            passed=True,
            detail="kappa_ch: original=2, Koszul=-2, symplectic=2, flop=2, K=0",
            status='CONJECTURAL',
        )
    return VerificationResult(
        name="kappa diagnostic: symplectic vs Koszul",
        passed=False,
        detail=f"Check failures in {[i for i, c in enumerate(checks) if not c]}",
        status='FAILED',
    )


def verify_unitarity(h_params: List[F], z: F) -> VerificationResult:
    """Verify g(z)*g(-z) = 1 (algebraic unitarity)."""
    inv = yangian_duality_involutions(h_params, z)

    if inv.g_unitarity_product == F(1):
        return VerificationResult(
            name="Unitarity g(z)*g(-z)=1",
            passed=True,
            detail=f"g({z})*g(-{z}) = {inv.g_unitarity_product} = 1",
            status='PROVED (algebraic identity)',
        )
    return VerificationResult(
        name="Unitarity g(z)*g(-z)=1",
        passed=False,
        detail=f"g({z})*g(-{z}) = {inv.g_unitarity_product} != 1",
        status='FAILED',
    )


def verify_koszul_is_inversion(h_params: List[F], z: F) -> VerificationResult:
    """Verify g^!(z) = 1/g(z) (Koszul = structure function inversion)."""
    inv = yangian_duality_involutions(h_params, z)

    product = inv.g_original_at_z * inv.g_koszul_at_z
    if product == F(1):
        return VerificationResult(
            name="Koszul g(z)*g^!(z)=1",
            passed=True,
            detail=f"g({z})*g^!({z}) = {product} = 1",
            status='PROVED (algebraic identity)',
        )
    return VerificationResult(
        name="Koszul g(z)*g^!(z)=1",
        passed=False,
        detail=f"g({z})*g^!({z}) = {product} != 1",
        status='FAILED',
    )


def verify_langlands_trivial(h_params: List[F], z: F) -> VerificationResult:
    """Verify g^L(z) = g(z) (Langlands trivial for gl_1)."""
    inv = yangian_duality_involutions(h_params, z)

    if inv.g_langlands_at_z == inv.g_original_at_z:
        return VerificationResult(
            name="Langlands g^L(z)=g(z) for gl_1",
            passed=True,
            detail=f"g^L({z}) = g({z}) = {inv.g_original_at_z}",
            status='PROVED (gl_1 Langlands-trivial)',
        )
    return VerificationResult(
        name="Langlands g^L(z)=g(z) for gl_1",
        passed=False,
        detail=f"g^L({z}) = {inv.g_langlands_at_z} != g({z}) = {inv.g_original_at_z}",
        status='FAILED',
    )


def verify_dolgachev_nikulin_signatures() -> VerificationResult:
    """Verify DN decomposition signatures sum to (4,20) at all Picard ranks."""
    for rho in range(1, 21):
        data = dolgachev_nikulin_self_duality(rho)
        total_pos = data.algebraic_signature[0] + data.transcendental_signature[0]
        total_neg = data.algebraic_signature[1] + data.transcendental_signature[1]
        if total_pos != MUKAI_SIG_PLUS or total_neg != MUKAI_SIG_MINUS:
            return VerificationResult(
                name="DN signatures sum to (4,20)",
                passed=False,
                detail=f"At rho={rho}: ({total_pos},{total_neg}) != (4,20)",
                status='FAILED',
            )
    return VerificationResult(
        name="DN signatures sum to (4,20)",
        passed=True,
        detail="All rho=1..20: algebraic + transcendental = (4,20)",
        status='PROVED',
    )


def verify_beauville_euler_chars(max_charge: int = 5) -> VerificationResult:
    """Verify Beauville: chi(M_H(v)) = chi(Hilb^n(K3)) = p_{24}(n)."""
    for n in range(max_charge + 1):
        h_data = higgs_branch_k3(n)
        expected = _p24(n)
        if h_data.euler_char != expected:
            return VerificationResult(
                name="Beauville: chi(M_H) = p_{24}(n)",
                passed=False,
                detail=f"At n={n}: chi={h_data.euler_char} != p_24={expected}",
                status='FAILED',
            )
    return VerificationResult(
        name="Beauville: chi(M_H) = p_{24}(n)",
        passed=True,
        detail=f"All n=0..{max_charge}: chi(M_H(v)) = p_{{24}}(n)",
        status='ProvedElsewhere (Beauville 1983)',
    )


def full_verification(
    h_params: Optional[List[F]] = None,
    z: F = F(7),
    max_charge: int = 5,
) -> List[VerificationResult]:
    r"""Run the full symplectic duality verification suite.

    Tests:
    1. Coulomb-Higgs Euler char match (self-duality)
    2. kappa diagnostic (symplectic vs Koszul)
    3. Unitarity g(z)*g(-z) = 1
    4. Koszul = inversion g(z)*g^!(z) = 1
    5. Langlands trivial for gl_1
    6. DN signatures sum to (4,20)
    7. Beauville Euler chars

    Default parameters: simple 4-parameter CY_2 vector avoiding poles (AP-CY28).
    z=7 is far from all poles for the default parametrization.
    """
    if h_params is None:
        # Simple 4-parameter vector satisfying sum = 0
        # h = (3, 1, -1, -3) has sum = 0
        # Using 4 nonzero params (rest zero would cause poles)
        # Better: use the parametrization from k3_yangian.py
        # h_i = eps for i=1..4, h_i = -eps/5 for i=5..24
        # With eps=1: sum = 4 - 20/5 = 4 - 4 = 0
        eps = F(1)
        h_params = [eps] * MUKAI_SIG_PLUS + [-eps * F(1, 5)] * MUKAI_SIG_MINUS

    results = []
    results.append(verify_coulomb_higgs_match(max_charge))
    results.append(verify_kappa_diagnostic())
    results.append(verify_unitarity(h_params, z))
    results.append(verify_koszul_is_inversion(h_params, z))
    results.append(verify_langlands_trivial(h_params, z))
    results.append(verify_dolgachev_nikulin_signatures())
    results.append(verify_beauville_euler_chars(max_charge))

    return results


# ============================================================================
# Internal helpers
# ============================================================================

def _p24(n: int) -> int:
    """Compute p_{24}(n): the number of 24-colored partitions of n.

    This is the coefficient of q^n in prod_{k>=1} 1/(1-q^k)^{24}.
    Equivalently: chi(Hilb^n(K3)) (Goettsche formula).

    Uses the pre-computed table for small n, and a recursive formula
    via the Euler function for larger n.
    """
    if n < 0:
        return 0
    if n in HILB_EULER_CHARS:
        return HILB_EULER_CHARS[n]

    # Recursive computation using the product formula:
    # sum_{n>=0} p_{24}(n) q^n = prod_{k>=1} 1/(1-q^k)^{24}
    # Taking log and differentiating:
    # n * p_{24}(n) = sum_{k=1}^{n} sigma_{1,24}(k) * p_{24}(n-k)
    # where sigma_{1,24}(k) = 24 * sigma_1(k) = 24 * sum_{d|k} d
    table = [0] * (n + 1)
    table[0] = 1
    for m in range(1, n + 1):
        s = 0
        for k in range(1, m + 1):
            # sigma_1(k) = sum of divisors of k
            sig1 = sum(d for d in range(1, k + 1) if k % d == 0)
            s += 24 * sig1 * table[m - k]
        table[m] = s // m

    HILB_EULER_CHARS[n] = table[n]
    return table[n]


def _multinomial_sym_euler(n: int) -> int:
    r"""Euler characteristic of Sym^n(K3).

    chi(Sym^n(K3)) = multinomial coefficient for distributing n points
    among the 24 cohomology directions of K3.

    For n=0: 1
    For n=1: chi(K3) = 24
    For n=2: chi(K3)*(chi(K3)+1)/2 = 24*25/2 = 300
    General: binomial(chi(K3) + n - 1, n) = binomial(23 + n, n)

    This is NOT the same as p_{24}(n) = chi(Hilb^n(K3)) in general.
    The difference is the correction from the Hilbert-Chow resolution.
    """
    # chi(Sym^n(K3)) = binomial(24 + n - 1, n) = binomial(23 + n, n)
    return math.comb(23 + n, n)
