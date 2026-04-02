r"""Hitchin moduli space M_H(C, SL_2) for genus-2 curve C.

DIMENSION ANALYSIS (CAREFUL)
=============================

    dim_C(M_H(C, G)) = 2*dim(G)*(g-1) = 2*3*1 = 6

for G = SL_2 (dim 3) and g = 2.

This is a holomorphic symplectic manifold of complex dimension 6 (real
dimension 12), with holonomy Sp(3) \subset SU(6).  The canonical bundle
is trivial (the top power of the holomorphic symplectic form trivializes
it), so M_H is Calabi-Yau in the sense of SU(n) holonomy, but of
COMPLEX DIMENSION 6 --- it is NOT literally a CY3 (which would require
complex dimension 3 and SU(3) holonomy).

The Hitchin fibration pi: M_H -> A_H = C^3 is a Lagrangian fibration
with generic fibre Prym(Sigma/C) ~ abelian 3-fold.  Both the base and
the fibre have complex dimension 3, and this "CY3 of fibration type"
structure is what the physics literature means by calling M_H a "CY3":
the effective 2d sigma model target arising from double compactification
of the 6d (2,0) theory on C x T^2 sees a CY3 geometry.

For the QVCG framework, M_H is treated as a CY category of the
appropriate dimension (d=6 literally, d=3 effectively via the
integrable system structure).  The Hitchin CY3 is the unique case
where dim(G)*(g-1) = 3, giving a 3-dimensional Hitchin base, hence
a Lagrangian fibration of "CY3 type" (base dim = fibre dim = 3).

WHAT WE COMPUTE
================

1. DIMENSIONS AND FIBRATION STRUCTURE
   - dim_R = 12, dim_C = 6 (holomorphic symplectic, Sp(3) holonomy)
   - Hitchin base A_H = H^0(C, K_C^2), dim = 3g-3 = 3
   - Generic Hitchin fibre: Prym(Sigma/C), dim = 3 (abelian 3-fold)
   - Spectral curve Sigma -> C: genus-5 double cover, branched at 4 points

2. SPECTRAL CURVE GEOMETRY
   - Sigma -> C is a degree-2 cover branched at zeros of a in H^0(K_C^2)
   - deg(K_C^2) = 2*(2g-2) = 4 for g=2: generic section has 4 simple zeros
   - Riemann-Hurwitz: 2g(Sigma)-2 = 2*(2g(C)-2) + 4 = 8, so g(Sigma) = 5
   - NOTE: The research note physics_hitchin_langlands.tex line 660 claims
     g(Sigma) = 3 for g=2. This is INCORRECT. The correct value is g(Sigma) = 5.
     (Riemann-Hurwitz applied to a degree-2 cover with 4 branch points gives
     2g(S)-2 = 2*(2*2-2) + 4 = 4+4 = 8, hence g(S)=5.)
   - Prym(Sigma/C) has dimension g(Sigma) - g(C) = 5 - 2 = 3

3. ROOT DATUM R(C, SL_2)
   - Lattice: Lambda = cochar(SL_2) tensor H_1(C, Z) enriched with bilinear form
   - Real roots: Phi(SL_2) = {+alpha, -alpha} (A_1 root system)
   - Imaginary roots: multiplicities = DT/BPS invariants of M_H
   - Weyl group: W(SL_2) x translations = Z/2Z x Z^4 (affine-type)

4. E-POLYNOMIAL AND EULER CHARACTERISTIC
   - M_H is non-compact (affine) hyperkahler, so chi_top = 0.
   - Hausel-Thaddeus (2003) E-polynomial (for odd degree twisted version):
     E(t) = ((1+t^3)^4 - (t+t^2)^4) / (1-t^4) = 1 + 4t^3 - 4t^5 - t^8
     chi = E(1) = 0.
   - The zero-section N_0 = Bun^s_{SL_2}(C, odd degree) is a smooth 3-fold
     isomorphic to a (2,2) complete intersection in P^5 (Desale-Ramanan).
     Betti numbers: b_0=1, b_1=0, b_2=1, b_3=4, b_4=1, b_5=0, b_6=1.
     chi(N_0) = 0.

5. CONNECTION TO K3 x E AND DELTA_5
   - Both M_H(g=2, SL_2) and K3 x E are CY3s.
   - Both involve Sp_4(Z) automorphic forms (genus-2 Siegel modular forms).
   - The K3 x E BKM superalgebra g_{Delta_5} has denominator = Delta_5.
   - SL_2 is self-dual (SL_2^v = PGL_2 ~ SL_2 at Lie algebra level).
   - CONJECTURE: the BKM of M_H(g=2, SL_2) is related to g_{Delta_5}.

6. EXPECTED KAPPA
   - If BKM = g_{Delta_5}: kappa = weight(Delta_5) = 5.
   - Self-duality: kappa + kappa' = kappa_crit with kappa = kappa'.
   - So kappa_crit = 2*5 = 10 = dim(Sp_4).

MATHEMATICAL REFERENCES
========================
  - Hitchin, "The self-duality equations on a Riemann surface" (1987)
  - Hitchin, "Stable bundles and integrable systems" (1987)
  - Desale-Ramanan, "Poincare polynomials of the variety of stable bundles" (1975)
  - Hausel-Thaddeus, "Mirror symmetry, Langlands duality, and the Hitchin system" (2003)
  - Hausel-Rodriguez-Villegas, "Mixed Hodge polynomials of character varieties" (2008)
  - Hausel, "Mirror symmetry, Langlands duality, and the Hitchin system" (2005)

MANUSCRIPT REFERENCES
======================
  - notes/physics_hitchin_langlands.tex: conj:langlands-koszul, rem:comparison-k3e
  - chapters/examples/k3_times_e.tex: Delta_5 BKM story
  - compute/lib/wkb_denominator.py: BKM product/sum verification
  - compute/lib/igusa_product_formula.py: Delta_5 as Borcherds product
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, NamedTuple, Optional, Tuple

import numpy as np


# =========================================================================
# 1. BASIC DIMENSIONS AND FIBRATION DATA
# =========================================================================

class HitchinData(NamedTuple):
    """Dimensional and structural data for M_H(C, G) with specified G, g."""
    group: str
    genus: int
    dim_group: int           # dim(G) as a variety
    rank_group: int          # rank(G)
    casimir_degrees: Tuple[int, ...]  # degrees of Casimir invariants
    dim_real: int            # real dimension of M_H
    dim_complex: int         # complex dimension of M_H (= 2*dim(G)*(g-1))
    dim_hitchin_base: int    # dimension of A_H (= dim(G)*(g-1) = dim_C / 2)
    is_lagrangian_cy3: bool  # whether the Hitchin fibration is "CY3 type"
                             # i.e. dim(base) = dim(fibre) = 3
                             # (requires dim(G)*(g-1) = 3, NOT dim_C = 3)
    dim_hitchin_fibre: int   # dim of generic Hitchin fibre (= dim base)


# Group data: (dim, rank, casimir_degrees)
GROUP_DATA: Dict[str, Tuple[int, int, Tuple[int, ...]]] = {
    'SL_2': (3, 1, (2,)),
    'PGL_2': (3, 1, (2,)),
    'GL_2': (4, 2, (1, 2)),
    'SL_3': (8, 2, (2, 3)),
    'PGL_3': (8, 2, (2, 3)),
    'GL_3': (9, 3, (1, 2, 3)),
    'SL_4': (15, 3, (2, 3, 4)),
    'Sp_4': (10, 2, (2, 4)),
    'SO_3': (3, 1, (2,)),
    'SO_5': (10, 2, (2, 4)),
    'G_2': (14, 2, (2, 6)),
    'E_6': (78, 6, (2, 5, 6, 8, 9, 12)),
    'E_7': (133, 7, (2, 6, 8, 10, 12, 14, 18)),
    'E_8': (248, 8, (2, 8, 12, 14, 18, 20, 24, 30)),
}


def hitchin_dimensions(group: str, genus: int) -> HitchinData:
    """Compute dimensional data for M_H(C, G).

    Parameters
    ----------
    group : str
        One of the keys in GROUP_DATA.
    genus : int
        Genus of the curve C (must be >= 2 for smooth M_H).

    Returns
    -------
    HitchinData with all dimensional invariants.
    """
    if genus < 2:
        raise ValueError(f"Hitchin moduli space requires genus >= 2, got {genus}")

    if group not in GROUP_DATA:
        raise ValueError(f"Unknown group {group}. Known: {sorted(GROUP_DATA.keys())}")

    dim_G, rank_G, casimirs = GROUP_DATA[group]

    dim_real = 4 * dim_G * (genus - 1)
    dim_complex = 2 * dim_G * (genus - 1)
    dim_base = sum((2 * d - 1) * (genus - 1) for d in casimirs)

    # Sanity: dim_base should equal dim_G * (genus - 1) = dim_complex / 2
    assert dim_base == dim_G * (genus - 1), \
        f"Hitchin base dimension {dim_base} != {dim_G * (genus - 1)}"

    return HitchinData(
        group=group,
        genus=genus,
        dim_group=dim_G,
        rank_group=rank_G,
        casimir_degrees=casimirs,
        dim_real=dim_real,
        dim_complex=dim_complex,
        dim_hitchin_base=dim_base,
        is_lagrangian_cy3=(dim_base == 3),
        dim_hitchin_fibre=dim_base,
    )


# The distinguished case: SL_2, genus 2
SL2_G2 = hitchin_dimensions('SL_2', 2)


def find_lagrangian_cy3_cases(max_genus: int = 10) -> List[HitchinData]:
    """Find all (G, g) pairs where the Hitchin fibration is "CY3 type".

    This means the Hitchin base has dimension 3, equivalently the generic
    Hitchin fibre is an abelian 3-fold: dim(G)*(g-1) = 3.

    WARNING: the total space M_H has complex dimension 2*3 = 6 in these
    cases, NOT 3.  The "CY3" designation refers to the Lagrangian fibration
    structure (base dim = fibre dim = 3), not the literal complex dimension.

    The ONLY solution for standard groups is dim(G) = 3, g = 2.
    Groups with dim(G)=3: SL_2, PGL_2, SO_3 (all locally isomorphic).
    """
    results = []
    for group in sorted(GROUP_DATA.keys()):
        for g in range(2, max_genus + 1):
            data = hitchin_dimensions(group, g)
            if data.is_lagrangian_cy3:
                results.append(data)
    return results


# =========================================================================
# 2. SPECTRAL CURVE GEOMETRY
# =========================================================================

class SpectralCurveData(NamedTuple):
    """Geometry of the spectral curve Sigma -> C for the SL_n Hitchin system."""
    degree_cover: int        # degree of Sigma -> C
    genus_base: int          # g(C)
    genus_spectral: int      # g(Sigma) by Riemann-Hurwitz
    n_branch_points: int     # number of branch points (generic)
    dim_prym: int            # dim Prym(Sigma/C) = dim Hitchin fibre
    dim_jacobian: int        # dim Jac(Sigma) = g(Sigma)


def spectral_curve_sl2(genus: int) -> SpectralCurveData:
    """Spectral curve data for the SL_2 Hitchin system on genus-g curve C.

    The spectral curve is eta^2 + a = 0 in Tot(K_C), where a in H^0(K_C^2).
    It is a degree-2 cover of C branched at the zeros of a.

    Branching: a generic section of K_C^2 has deg(K_C^2) = 2*(2g-2) = 4g-4
    simple zeros, giving B = 4g-4 branch points.

    Riemann-Hurwitz for a degree-n cover with B simple branch points:
        2g(Sigma)-2 = n*(2g(C)-2) + B

    For n=2, B=4g-4:
        2g(Sigma)-2 = 2*(2g-2) + (4g-4) = 4g-4 + 4g-4 = 8g-8
        g(Sigma) = 4g - 3.

    For g=2: g(Sigma) = 5, B = 4.
    Prym dimension: g(Sigma) - g(C) = (4g-3) - g = 3g - 3.
    For g=2: dim Prym = 3 (consistent with dim Hitchin fibre = dim(G)*(g-1) = 3).
    """
    B = 4 * genus - 4
    g_spectral = 4 * genus - 3
    dim_prym = g_spectral - genus  # = 3g - 3

    return SpectralCurveData(
        degree_cover=2,
        genus_base=genus,
        genus_spectral=g_spectral,
        n_branch_points=B,
        dim_prym=dim_prym,
        dim_jacobian=g_spectral,
    )


def spectral_curve_sln(n: int, genus: int) -> SpectralCurveData:
    """Spectral curve data for the SL_n Hitchin system on genus-g curve C.

    The spectral curve is det(eta*I - phi) = 0 in Tot(K_C),
    a degree-n cover of C.

    For SL_n, the Hitchin fibre is Prym(Sigma/C) of dimension (n^2-1)*(g-1).
    Hence g(Sigma) = dim Prym + g(C) = (n^2-1)(g-1) + g.

    Branch points by Riemann-Hurwitz:
        B = 2g(Sigma)-2 - n*(2g(C)-2)
          = 2*((n^2-1)(g-1)+g) - 2 - 2n*(g-1)
          = 2n(n-1)(g-1).
    """
    g_spectral = (n**2 - 1) * (genus - 1) + genus
    dim_prym = (n**2 - 1) * (genus - 1)
    B = 2 * n * (n - 1) * (genus - 1)

    return SpectralCurveData(
        degree_cover=n,
        genus_base=genus,
        genus_spectral=g_spectral,
        n_branch_points=B,
        dim_prym=dim_prym,
        dim_jacobian=g_spectral,
    )


# =========================================================================
# 3. ROOT DATUM R(C, SL_2)
# =========================================================================

class RootDatum(NamedTuple):
    """Generalized root datum for the QVCG G(C, G)."""
    lattice_rank: int               # rank of Lambda(C,G)
    real_roots: str                  # description of real root system
    n_real_positive: int             # number of positive real roots
    weyl_group: str                  # description of Weyl group
    weyl_group_order: str            # order (may be infinite)
    imaginary_root_source: str       # what controls imaginary multiplicities
    hitchin_base_dim: int            # dim of A_H (source of imaginary roots)
    langlands_dual: str              # G^v


def root_datum_sl2_genus2() -> RootDatum:
    r"""Root datum R(C, SL_2) for a genus-2 curve C.

    From physics_hitchin_langlands.tex, Construction constr:root-datum-hitchin:

    Lattice: Lambda(C, SL_2) = Lambda_cochar(SL_2) + H_1(C, Z)
             = Z (rank-1 cocharacter lattice) + Z^4 (H_1 of genus-2 surface)
             Total rank: 5.
    Bilinear form: combines Killing form on cochar with intersection form on H_1.

    Real roots: Phi(SL_2) = {+alpha, -alpha} (the A_1 root system).
    These have multiplicity 1 and generate the finite part of the Weyl group.

    Imaginary roots: from the Hitchin base A_H = H^0(K_C^2) = C^3.
    Multiplicities are DT/BPS invariants of M_H, controlled by an automorphic
    form for Sp_4(Z) (conjectured to be Delta_5 or a close relative).

    Weyl group: W(SL_2) x Lambda_cochar^{2g} = Z/2Z x Z^4.
    This is infinite (affine-type).

    Langlands dual: SL_2^v = PGL_2. At the Lie algebra level, sl_2 = pgl_2,
    so the root datum is self-dual. This means G(C, SL_2) should be self-Koszul-dual.
    """
    return RootDatum(
        lattice_rank=5,
        real_roots='A_1 = {+alpha, -alpha}',
        n_real_positive=1,
        weyl_group='W(SL_2) x Z^4 = Z/2Z x Z^4',
        weyl_group_order='infinite',
        imaginary_root_source='DT/BPS invariants of M_H, or automorphic form for Sp_4(Z)',
        hitchin_base_dim=3,
        langlands_dual='PGL_2 (isomorphic to SL_2 at Lie algebra level)',
    )


# =========================================================================
# 4. E-POLYNOMIAL AND EULER CHARACTERISTIC
# =========================================================================

def hausel_thaddeus_e_polynomial(genus: int) -> Dict[int, int]:
    """E-polynomial of M_B(SL_2, odd degree, genus g) via Hausel-Thaddeus.

    Formula (Hausel-Thaddeus 2003, Theorem 4.6):
        E(t) = ((1+t^3)^{2g} - (t+t^2)^{2g}) / (1-t^4)

    This is the virtual Poincare polynomial (E-polynomial evaluated at x=y=t).
    It CAN have negative coefficients (and does for g >= 2), reflecting the
    mixed Hodge structure on the character variety.

    Returns dict: degree -> coefficient.
    """
    max_deg = 12 * (genus - 1)

    # Expand (1+t^3)^{2g} by convolution
    a = np.array([1, 0, 0, 1], dtype=np.int64)  # 1 + t^3
    power_a = np.array([1], dtype=np.int64)
    for _ in range(2 * genus):
        power_a = np.convolve(power_a, a)

    # Expand (t+t^2)^{2g} by convolution
    b = np.array([0, 1, 1], dtype=np.int64)  # t + t^2
    power_b = np.array([1], dtype=np.int64)
    for _ in range(2 * genus):
        power_b = np.convolve(power_b, b)

    # Pad to same length
    L = max(len(power_a), len(power_b))
    pa = np.zeros(L, dtype=np.int64)
    pa[:len(power_a)] = power_a
    pb = np.zeros(L, dtype=np.int64)
    pb[:len(power_b)] = power_b

    numerator = pa - pb

    # Divide by (1-t^4) using formal power series: 1/(1-t^4) = sum t^{4k}
    result = np.zeros(max_deg + 1, dtype=np.int64)
    for m in range(max_deg + 1):
        s = 0
        for j in range(min(m + 1, len(numerator))):
            if (m - j) % 4 == 0:
                s += int(numerator[j])
        result[m] = s

    return {k: int(result[k]) for k in range(max_deg + 1) if result[k] != 0}


def euler_characteristic_from_e_poly(e_poly: Dict[int, int]) -> int:
    """Compute chi = E(1) = sum of all coefficients of the E-polynomial.

    For the E-polynomial E(x,y) evaluated at x=y=1, this gives the
    compactly-supported Euler characteristic chi_c.
    """
    return sum(e_poly.values())


def bun_sl2_genus2_betti() -> Dict[int, int]:
    """Betti numbers of Bun^s_{SL_2}(C, odd degree) for genus-2 curve C.

    This is the zero-section N_0 of the Hitchin fibration.
    By Desale-Ramanan (1975), for rank 2, odd degree, genus 2:
    N_0 is isomorphic to the intersection of two quadrics in P^5.
    This is a smooth projective 3-fold.

    Betti numbers (from the Lefschetz hyperplane theorem + explicit computation):
        b_0 = 1, b_1 = 0, b_2 = 1, b_3 = 4, b_4 = 1, b_5 = 0, b_6 = 1.

    The middle Betti number b_3 = 4 reflects the genus-2 curve:
    the (2,2) complete intersection in P^5 has H^3 = H^1(C)^2 = (Z^4)^2/...
    In fact b_3 = 2g = 4 where g is the genus of the associated curve
    (the Desale-Ramanan curve is intimately related to C).

    chi(N_0) = 1 - 0 + 1 - 4 + 1 - 0 + 1 = 0.
    """
    return {0: 1, 1: 0, 2: 1, 3: 4, 4: 1, 5: 0, 6: 1}


def euler_characteristic_from_betti(betti: Dict[int, int]) -> int:
    """Compute chi = sum (-1)^k * b_k."""
    return sum((-1)**k * b for k, b in betti.items())


# =========================================================================
# 5. HITCHIN FIBRE TOPOLOGY
# =========================================================================

def hitchin_fibre_topology_sl2_genus2() -> Dict[str, object]:
    """Topology of the generic Hitchin fibre for (SL_2, genus 2).

    Generic fibre = Prym(Sigma/C) where Sigma has genus 5 and C has genus 2.
    Prym(Sigma/C) is a principally polarized abelian variety of dimension 3
    (up to a shift in polarization type).

    As a real manifold, Prym ~ (S^1)^6 (a 6-torus), with:
        b_k = C(6, k) for 0 <= k <= 6.
        chi = 0 (as for any torus).

    The polarization type for the Prym of SL_2 spectral curves is (1,1,2),
    NOT principally polarized. The dual abelian variety (for PGL_2) has
    polarization type (1,2,2), and the two are Hausel-Thaddeus dual.
    """
    betti = {k: math.comb(6, k) for k in range(7)}
    return {
        'fibre_type': 'Prym(Sigma/C), abelian 3-fold',
        'real_dimension': 6,
        'complex_dimension': 3,
        'betti_numbers': betti,
        'euler_char': 0,
        'polarization_type': (1, 1, 2),
        'is_principally_polarized': False,
        'spectral_genus': 5,
        'base_genus': 2,
        'prym_dimension': 3,
    }


# =========================================================================
# 6. SYZ MIRROR SYMMETRY
# =========================================================================

def syz_data_sl2_genus2() -> Dict[str, object]:
    """SYZ mirror symmetry data for the Hitchin CY3.

    The Hitchin fibration pi: M_H -> A_H is a LAGRANGIAN torus fibration
    (with singular fibres over the discriminant locus).

    SYZ mirror symmetry predicts: the mirror CY3 is obtained by dualizing
    the torus fibres. For M_H(C, SL_2): the SYZ mirror is M_H(C, PGL_2).

    Since SL_2 ~ PGL_2 at the Lie algebra level, the mirror has the SAME
    underlying smooth manifold (diffeomorphic), but the COMPLEX STRUCTURE
    is different (the B-field/gerbe data differ by a Z/2 twist).

    This is the Hausel-Thaddeus mirror symmetry:
        M_H(C, SL_n) is SYZ mirror to M_H(C, PGL_n).
    For n = 2: the mirror is "almost" self-mirror.
    """
    return {
        'fibration': 'pi: M_H -> A_H = C^3',
        'generic_fibre': 'Prym(Sigma/C) ~ T^6 (Lagrangian 3-torus)',
        'discriminant_description': (
            'Delta = {a in C^3 : quadratic differential a has a repeated zero}, '
            'a hypersurface in A_H.'
        ),
        'syz_mirror': 'M_H(C, PGL_2)',
        'is_self_mirror_diffeo': True,
        'is_self_mirror_complex': False,
        'mirror_exchange': 'SL_2 <-> PGL_2 (Langlands duality)',
    }


# =========================================================================
# 7. CONNECTION TO K3 x E AND DELTA_5
# =========================================================================

def k3xe_comparison() -> Dict[str, object]:
    """Compare the Hitchin CY3 M_H(genus 2, SL_2) with K3 x E.

    Both are non-compact CY3s (though K3 x E is compact as a product but
    the BKM algebra is really associated to the DT theory, which sees the
    non-compactness of the moduli of sheaves). Both involve Sp_4(Z).

    Returns a dictionary of parallel structures.
    """
    hitchin = hitchin_dimensions('SL_2', 2)
    spectral = spectral_curve_sl2(2)

    return {
        # Dimensional data
        'hitchin_dim_C': hitchin.dim_complex,       # 6 (holomorphic symplectic)
        'hitchin_lagrangian_fibre_dim': 3,          # Hitchin fibre = abelian 3-fold
        'k3xe_dim_C': 3,                            # literal CY3 (K3 dim 2 + E dim 1)

        # Key distinction
        'hitchin_is_noncompact': True,
        'k3xe_is_compact': True,

        # Base/lattice structure
        'hitchin_base_dim': hitchin.dim_hitchin_base,  # 3
        'k3xe_bkm_lattice_rank': 3,                   # Lambda^{2,1} rank 3

        # Fibre structure
        'hitchin_fibre_dim': spectral.dim_prym,         # 3

        # Automorphic form
        'hitchin_automorphic': 'Sp_4(Z) modular form (genus-2 Siegel)',
        'k3xe_automorphic': 'Delta_5, Igusa cusp form, weight 5 for Sp_4(Z)',

        # Self-duality
        'hitchin_langlands_dual': 'SL_2^v = PGL_2 ~ SL_2 => self-dual at Lie algebra level',
        'k3xe_mirror_symmetry': 'K3 is self-mirror (T-duality), E is self-dual',

        # kappa
        'hitchin_expected_kappa': 5,   # if BKM = g_{Delta_5}
        'k3xe_kappa': 5,               # weight(Delta_5)

        # Sp_4 connection
        'sp4_from_hitchin': (
            'genus-2 curve C has Jac(C) = principally polarized abelian surface; '
            'Sp_4(Z) is the mapping class group of H_1(C, Z) preserving the '
            'intersection form. The Siegel upper half-space H_2 parametrizes '
            'genus-2 curves.'
        ),
        'sp4_from_k3xe': (
            'Lambda^{2,1} has signature (2,1), O^+(2,1) = PSL_2(R). '
            'But Delta_5 is a form for Sp_4(Z) on H_2, which arises from '
            'the embedding Lambda^{2,1} -> Lambda^{2,3} and O^+(2,3) = Sp_4(R).'
        ),

        # The conjecture
        'conjecture': (
            'The BKM superalgebra g_{R(C, SL_2)} for the Hitchin CY3 '
            'IS (or is closely related to) g_{Delta_5} from K3 x E. '
            'Evidence: (1) Both are CY3. (2) Both involve Sp_4(Z). '
            '(3) Both have 3-dimensional base/lattice. '
            '(4) SL_2 self-dual matches K3 x E self-mirror. '
            '(5) Expected kappa = 5 in both cases.'
        ),
    }


# =========================================================================
# 8. DISCRIMINANT LOCUS AND SINGULAR FIBRES
# =========================================================================

def discriminant_locus_sl2_genus2() -> Dict[str, object]:
    r"""The discriminant locus Delta in the Hitchin base A_H = H^0(C, K_C^2).

    For SL_2, the spectral curve is eta^2 + a = 0, a double cover of C
    branched at zeros of a in H^0(K_C^2).

    A generic a has 4 simple zeros (deg(K_C^2) = 2*(2g-2) = 4 for g=2).
    The spectral curve is SINGULAR when a has a repeated zero: a and da
    share a zero, i.e. a belongs to the discriminant divisor.

    The discriminant Delta in C^3 = H^0(K_C^2):
    - Is a hypersurface (codimension 1) in the 3-dimensional base.
    - Over Delta, the spectral curve acquires a node, and the Prym fibre
      degenerates (an abelian 3-fold degenerates to a semi-abelian variety).

    For the SL_2 Hitchin system, the discriminant is the locus where the
    quadratic differential a has a zero of multiplicity >= 2.

    The nilpotent cone N is the fibre pi^{-1}(0) over the origin 0 in A_H.
    For SL_2, g=2: N contains the zero-section Bun_{SL_2}(C) and additional
    components from nilpotent Higgs fields.

    The topology of the nilpotent cone determines the "most degenerate"
    BPS spectrum and contains the information needed for the geometric
    Satake correspondence.
    """
    return {
        'base_dimension': 3,
        'discriminant_codimension': 1,
        'discriminant_type': 'hypersurface in C^3',
        'singular_fibre_type': 'semi-abelian variety (nodal Prym)',
        'nilpotent_cone_description': (
            'pi^{-1}(0): union of components including Bun_{SL_2}(C) '
            'and closures of nilpotent orbits'
        ),
        'monodromy_group': (
            'Finite index subgroup of Sp_6(Z) (monodromy of the '
            'torus fibration around Delta)'
        ),
        'n_branch_points_generic': 4,
        'degeneration_type': 'A_1 singularity (node) when two branch points collide',
    }


# =========================================================================
# 9. SP_4(Z) AND THE SIEGEL MODULAR CONNECTION
# =========================================================================

def sp4_connection() -> Dict[str, object]:
    r"""The Sp_4(Z) connection: genus-2 curves, abelian surfaces, and Delta_5.

    A genus-2 curve C determines:
    (a) Its Jacobian Jac(C), a principally polarized abelian surface.
    (b) The period matrix tau in H_2 (Siegel upper half-space of degree 2),
        defined up to the action of Sp_4(Z).

    The moduli space A_2 = H_2/Sp_4(Z) of principally polarized abelian
    surfaces has dimension 3 (= dim(H_2) = g*(g+1)/2 for g=2).

    The Torelli map: M_2 -> A_2 (sending a curve to its Jacobian) is
    generically injective (Torelli's theorem) but NOT surjective: not every
    ppas is a Jacobian.  The image is the Torelli locus.

    Delta_5 (the Igusa cusp form of weight 5) is the UNIQUE Siegel modular
    form of smallest weight for Sp_4(Z).  It vanishes exactly on the locus
    of decomposable abelian surfaces (products E_1 x E_2), which is the
    boundary of the Torelli locus.

    Key formulas for Delta_5:
    - Weight 5, genus 2 Siegel modular form
    - Vanishes on the reducible locus (Humbert surface H_1)
    - Product formula: Delta_5(tau) = prod_{(c,d) even} theta_m(tau)
      (product over the 10 even theta characteristics, each of weight 1/2)
    - The BKM denominator for K3 x E IS Delta_5 (Gritsenko-Nikulin)

    For the Hitchin system on a FIXED genus-2 curve C:
    - The period matrix tau(C) is a POINT in H_2/Sp_4(Z)
    - The Hitchin base A_H = H^0(C, K_C^2) = C^3 depends on C
    - The spectral curves Sigma_a define a FAMILY of genus-5 curves
      parametrized by a in A_H
    - Each Prym(Sigma_a/C) is a ppav of dimension 3 (NOT 2)
    - But the Prym map induces a map to A_3 (the Siegel space for g=3)

    The Sp_4(Z) enters differently:
    (1) Through the genus-2 curve C itself (Torelli for C)
    (2) Through the BKM denomination (if g_{Delta_5} controls the QVCG)
    (3) Through the automorphic form for the denominator identity
    """
    return {
        'siegel_degree': 2,
        'siegel_half_space_dim': 3,  # g*(g+1)/2 = 2*3/2 = 3
        'torelli_map': 'M_2 -> A_2 = H_2/Sp_4(Z)',
        'torelli_injective': True,
        'torelli_surjective': False,
        'delta_5_weight': 5,
        'delta_5_vanishing_locus': 'reducible ppas (products E_1 x E_2)',
        'n_even_theta_characteristics': 10,
        'delta_5_as_product': 'prod_{m even} theta_m(tau)',
        'sp4_dim': 10,
        'sp4_rank': 2,
        'coincidence_base_dim_equals_siegel_dim': True,  # both = 3
        'a2_dim': 3,   # dim(A_2)
        'a_h_dim': 3,  # dim(Hitchin base)
        'prym_target': 'A_3 (NOT A_2; the Prym is 3-dimensional)',
    }


def genus2_hodge_data() -> Dict[str, object]:
    r"""Hodge-theoretic data for the genus-2 curve C and its Jacobian.

    C: smooth projective curve of genus 2.
    Hodge numbers of C: h^{0,0} = h^{1,1} = 1, h^{1,0} = h^{0,1} = 2.
    Hodge diamond of C:
            1
          2   2
            1

    Jac(C): abelian surface (complex dimension 2).
    Hodge numbers: h^{p,q}(Jac(C)) = C(2,p) * C(2,q).
    Hodge diamond of Jac(C):
            1
          2   2
        1   4   1
          2   2
            1

    chi_top(C) = 2 - 2*g = -2.
    chi_top(Jac(C)) = 0 (all abelian varieties have chi = 0).
    sigma(Jac(C)) = 0 (signature; abelian surfaces have zero signature).

    H^1(C, Z) = Z^4, with intersection form given by the symplectic matrix
    J = ((0, I_2), (-I_2, 0)).  This is the standard Sp_4(Z) form.
    """
    # Hodge numbers of C
    c_hodge = {(0, 0): 1, (1, 0): 2, (0, 1): 2, (1, 1): 1}

    # Hodge numbers of Jac(C) = abelian surface
    jac_hodge = {}
    for p in range(3):
        for q in range(3):
            jac_hodge[(p, q)] = math.comb(2, p) * math.comb(2, q)

    return {
        'curve_genus': 2,
        'curve_hodge': c_hodge,
        'curve_euler': -2,
        'jacobian_dim': 2,
        'jacobian_hodge': jac_hodge,
        'jacobian_euler': 0,
        'jacobian_signature': 0,
        'h1_rank': 4,
        'intersection_form': 'standard symplectic J_2 on Z^4',
        'automorphism_group': 'Sp_4(Z)',
    }


def hitchin_hodge_numbers_sl2_g2() -> Dict[str, object]:
    r"""Mixed Hodge structure data for M_H(SL_2, g=2).

    The character variety M_B(SL_2, g=2) = Hom(pi_1(C), SL_2)/SL_2 has
    a mixed Hodge structure (Hausel-Rodriguez-Villegas).

    The E-polynomial E(x,y) encodes the mixed Hodge numbers:
        E(x,y) = sum_{p,q} (-1)^{p+q} h^{p,q}_c * x^p * y^q

    where h^{p,q}_c are the compactly-supported mixed Hodge numbers.

    For the Dolbeault realization (Higgs bundles), the pure Hodge structure
    is controlled by the C*-action phi -> t*phi, which gives a Bialynicki-
    Birula decomposition.

    KNOWN RESULTS (Hausel-Thaddeus, Hausel-Rodriguez-Villegas):
    - The E-polynomial at y=x=t: E(t,t) = 1 + 4t^3 - 4t^5 - t^8.
    - The Poincare polynomial of M_B^{ss} (for twisted/odd degree case):
      P(t) = (1+t^3)^4 / (1-t^4) evaluated appropriately.
    - The pure part: H^*(M_H) in the Dolbeault realization.

    The mixed Hodge diamond is complicated because M_H is non-compact and
    the cohomology has non-trivial weight filtration.  The key features:

    - H^0 = C (connected)
    - H^1 = 0 (for the twisted version)
    - H^2 = 0 (for the twisted version)
    - H^3 = C^4 (from H^1(C)^2 contributions)
    - H^4 = 0
    - H^5 = C^4 (Poincare duality-like, but with signs from mixed structure)
    - H^6 through H^8: determined by E-polynomial

    The Euler characteristic vanishes: chi = 0.
    """
    e_poly = hausel_thaddeus_e_polynomial(2)

    return {
        'e_polynomial': e_poly,
        'euler_characteristic': sum(e_poly.values()),
        'e_poly_display': '1 + 4t^3 - 4t^5 - t^8',
        'poincare_virtual': 'P(t) ~ (1+t^3)^4 / (1-t^4)',
        'weight_filtration': 'non-trivial (mixed Hodge structure)',
        'pure_part_source': 'C*-action on Higgs field',
        'known_h_values': {
            'H^0': 1,
            'H^3_coefficient': 4,
            'H^5_coefficient': -4,
            'H^8_coefficient': -1,
        },
        'note': (
            'Negative coefficients in E-polynomial reflect the mixed '
            'Hodge structure: these are virtual dimensions (alternating '
            'sum of mixed Hodge numbers at given degree).'
        ),
    }


# =========================================================================
# 10. EXPECTED KAPPA
# =========================================================================

def expected_kappa_hitchin_sl2_g2() -> Dict[str, object]:
    """Expected modular characteristic kappa for the Hitchin CY3.

    From the K3 x E analogy and the Langlands = Koszul conjecture:

    If M_H(genus 2, SL_2) has BKM superalgebra related to g_{Delta_5}:
        kappa(G(C, SL_2)) = weight(Delta_5) = 5.

    Self-duality: SL_2^v = PGL_2 ~ SL_2 at Lie algebra level, so
    G(C, SL_2)^! ~ G(C, PGL_2) ~ G(C, SL_2).
    Complementarity: kappa + kappa' = kappa_crit.
    Since kappa = kappa': 2*kappa = kappa_crit = 10 = dim(Sp_4).

    The value dim(Sp_4) = 10 arises because Sp_4 is the automorphic group
    for genus-2 Siegel modular forms. The general pattern:
        kappa_crit = dim(G_aut) where G_aut is the Siegel-type group.
    """
    return {
        'expected_kappa': Fraction(5, 1),
        'source': 'weight of Delta_5 (if BKM ~ g_{Delta_5})',
        'self_dual': True,
        'kappa_crit': Fraction(10, 1),
        'kappa_crit_interpretation': 'dim(Sp_4) = 10',
        'cross_checks': {
            'k3xe_kappa': 5,
            'delta5_weight': 5,
            'sp4_dim': 10,
            'half_sp4_dim': 5,
        },
    }


# =========================================================================
# 9. COMPREHENSIVE COMPUTATION
# =========================================================================

def full_computation() -> Dict[str, object]:
    """Run the complete computation for M_H(genus 2, SL_2).

    Returns a comprehensive dictionary of all computed quantities.
    """
    hitchin = hitchin_dimensions('SL_2', 2)
    spectral = spectral_curve_sl2(2)
    root = root_datum_sl2_genus2()
    e_poly = hausel_thaddeus_e_polynomial(2)
    chi_e = euler_characteristic_from_e_poly(e_poly)
    bun_betti = bun_sl2_genus2_betti()
    chi_bun = euler_characteristic_from_betti(bun_betti)
    fibre = hitchin_fibre_topology_sl2_genus2()
    syz = syz_data_sl2_genus2()
    kappa = expected_kappa_hitchin_sl2_g2()
    comparison = k3xe_comparison()

    return {
        'hitchin_data': hitchin._asdict(),
        'spectral_curve': spectral._asdict(),
        'root_datum': root._asdict(),
        'e_polynomial': e_poly,
        'chi_e_polynomial': chi_e,
        'bun_betti_numbers': bun_betti,
        'chi_bun': chi_bun,
        'fibre_topology': fibre,
        'syz_mirror': syz,
        'discriminant_locus': discriminant_locus_sl2_genus2(),
        'sp4_connection': sp4_connection(),
        'genus2_hodge': genus2_hodge_data(),
        'hitchin_hodge': hitchin_hodge_numbers_sl2_g2(),
        'expected_kappa': kappa,
        'k3xe_comparison': comparison,
        'lagrangian_cy3_cases': find_lagrangian_cy3_cases(),
    }


# =========================================================================
# 10. VERIFICATION FUNCTIONS
# =========================================================================

def verify_dimensions() -> bool:
    """Verify dimensional data for M_H(SL_2, g=2)."""
    h = hitchin_dimensions('SL_2', 2)
    return all([
        h.dim_real == 12,
        h.dim_complex == 6,
        h.dim_hitchin_base == 3,
        h.dim_hitchin_fibre == 3,
        h.is_lagrangian_cy3,
        h.dim_group == 3,
        h.rank_group == 1,
        h.casimir_degrees == (2,),
    ])


def verify_spectral_curve() -> bool:
    """Verify spectral curve data for SL_2, genus 2.

    Key fact: g(Sigma) = 5 (NOT 3 as erroneously stated in the research note).
    """
    s = spectral_curve_sl2(2)
    return all([
        s.degree_cover == 2,
        s.genus_base == 2,
        s.genus_spectral == 5,
        s.n_branch_points == 4,
        s.dim_prym == 3,
        s.dim_jacobian == 5,
    ])


def verify_riemann_hurwitz() -> bool:
    """Cross-check spectral curve via Riemann-Hurwitz for multiple genera.

    Two independent computations:
    (a) g(Sigma) = 4g - 3 from the SL_2 formula.
    (b) g(Sigma) from dim Prym = (n^2-1)(g-1) (the SL_n formula with n=2).
    These must agree.

    Also check: dim Prym = dim Hitchin fibre = dim Hitchin base.
    """
    for genus in [2, 3, 4, 5]:
        s_sl2 = spectral_curve_sl2(genus)
        s_sln = spectral_curve_sln(2, genus)
        h = hitchin_dimensions('SL_2', genus)
        if s_sl2.genus_spectral != s_sln.genus_spectral:
            return False
        if s_sl2.dim_prym != s_sln.dim_prym:
            return False
        if s_sl2.dim_prym != h.dim_hitchin_base:
            return False
    return True


def verify_hitchin_base_is_half_dim() -> bool:
    """Verify dim(A_H) = (1/2) * dim_C(M_H) for all groups and genera.

    This is the fundamental property: the Hitchin fibration is a
    completely integrable system (Lagrangian fibration).
    """
    for group in ['SL_2', 'SL_3', 'GL_2', 'GL_3', 'Sp_4', 'E_8']:
        for genus in [2, 3, 4]:
            h = hitchin_dimensions(group, genus)
            if h.dim_hitchin_base != h.dim_complex // 2:
                return False
    return True


def verify_lagrangian_cy3_uniqueness() -> bool:
    """Verify (SL_2, g=2) is the unique Lagrangian-CY3 Hitchin system.

    Requires dim(G)*(g-1) = 3 (Hitchin base = fibre = 3-dimensional).
    Since g >= 2, g-1 >= 1.  dim(G) must divide 3 and be at least 1.
    dim(G) = 1 is impossible (no 1-dimensional reductive group in our list).
    dim(G) = 3, g = 2 is the only solution.

    The groups with dim(G)=3 are SL_2, PGL_2, SO_3 (all locally isomorphic).
    """
    cases = find_lagrangian_cy3_cases(max_genus=20)
    groups_found = set(c.group for c in cases)
    expected = {'SL_2', 'PGL_2', 'SO_3'}
    return groups_found == expected and all(c.genus == 2 for c in cases)


def verify_e_polynomial_genus2() -> bool:
    """Verify the E-polynomial for genus 2.

    The Hausel-Thaddeus formula gives:
        E(t) = 1 + 4t^3 - 4t^5 - t^8

    Properties:
    (a) E(1) = 1 + 4 - 4 - 1 = 0 (Euler characteristic).
    (b) The polynomial is a valid E-polynomial (not necessarily non-negative).
    (c) Highest-degree term is t^8 (< dim_R = 12 due to Artin vanishing
        for the affine character variety).
    """
    e_poly = hausel_thaddeus_e_polynomial(2)
    expected = {0: 1, 3: 4, 5: -4, 8: -1}
    if e_poly != expected:
        return False
    chi = euler_characteristic_from_e_poly(e_poly)
    return chi == 0


def verify_bun_betti() -> bool:
    """Verify Betti numbers of Bun^s_{SL_2}(C, odd degree) for genus 2.

    This is a (2,2) complete intersection in P^5 (Desale-Ramanan).
    Betti: 1, 0, 1, 4, 1, 0, 1. chi = 0.
    Poincare duality: b_k = b_{6-k} (smooth compact 6-manifold, real dim 6).
    """
    betti = bun_sl2_genus2_betti()
    # Check values
    expected = {0: 1, 1: 0, 2: 1, 3: 4, 4: 1, 5: 0, 6: 1}
    if betti != expected:
        return False
    # Poincare duality
    for k in range(4):
        if betti[k] != betti[6 - k]:
            return False
    # Euler characteristic
    chi = euler_characteristic_from_betti(betti)
    return chi == 0


def verify_fibre_betti() -> bool:
    """Verify Betti of generic Hitchin fibre (abelian 3-fold ~ T^6)."""
    fibre = hitchin_fibre_topology_sl2_genus2()
    betti = fibre['betti_numbers']
    for k in range(7):
        if betti[k] != math.comb(6, k):
            return False
    return fibre['euler_char'] == 0


def verify_casimir_sum_rule() -> bool:
    """Verify sum_{i=1}^r (2d_i - 1)(g-1) = dim(G)(g-1) for all groups.

    This is the fundamental identity ensuring dim(A_H) = dim(G)(g-1).
    """
    for group, (dim_G, rank_G, casimirs) in GROUP_DATA.items():
        lhs = sum(2 * d - 1 for d in casimirs)
        if lhs != dim_G:
            return False
    return True


def verify_all(verbose: bool = False) -> Dict[str, bool]:
    """Run all verification checks."""
    checks = {
        'dimensions': verify_dimensions(),
        'spectral_curve': verify_spectral_curve(),
        'riemann_hurwitz': verify_riemann_hurwitz(),
        'hitchin_base_half_dim': verify_hitchin_base_is_half_dim(),
        'lagrangian_cy3_uniqueness': verify_lagrangian_cy3_uniqueness(),
        'e_polynomial_genus2': verify_e_polynomial_genus2(),
        'bun_betti': verify_bun_betti(),
        'fibre_betti': verify_fibre_betti(),
        'casimir_sum_rule': verify_casimir_sum_rule(),
    }
    if verbose:
        for name, result in checks.items():
            print(f"  {name}: {'PASS' if result else 'FAIL'}")
    return checks


# =========================================================================
# CLI
# =========================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("M_H(genus 2, SL_2) -- the unique Hitchin Lagrangian CY3 fibration")
    print("(dim_C = 6, hol. sympl.; Hitchin base = fibre = 3-dimensional)")
    print("=" * 72)

    print("\n--- 1. Dimensions ---")
    h = SL2_G2
    print(f"  Group: {h.group}, Genus: {h.genus}")
    print(f"  dim(G) = {h.dim_group}, rank(G) = {h.rank_group}")
    print(f"  Casimir degrees: {h.casimir_degrees}")
    print(f"  dim_R(M_H) = {h.dim_real}")
    print(f"  dim_C(M_H) = {h.dim_complex}  (holomorphic symplectic, Sp(3) holonomy)")
    print(f"  dim(A_H) = {h.dim_hitchin_base}  (Hitchin base)")
    print(f"  dim(fibre) = {h.dim_hitchin_fibre}  (generic Hitchin fibre)")
    print(f"  Lagrangian CY3 fibration: {h.is_lagrangian_cy3}  (base=fibre=3)")

    print("\n--- 2. Spectral curve ---")
    s = spectral_curve_sl2(2)
    print(f"  Cover degree: {s.degree_cover}")
    print(f"  Genus(C) = {s.genus_base}")
    print(f"  Genus(Sigma) = {s.genus_spectral}  [NOTE: corrects g=3 error in research note]")
    print(f"  Branch points: {s.n_branch_points}")
    print(f"  dim(Prym) = {s.dim_prym}")
    print(f"  dim(Jac(Sigma)) = {s.dim_jacobian}")

    print("\n--- 3. Lagrangian CY3 uniqueness ---")
    cases = find_lagrangian_cy3_cases()
    for c in cases:
        print(f"  {c.group}, g={c.genus}: dim_C = {c.dim_complex}, base = fibre = {c.dim_hitchin_base}")
    print(f"  All locally isomorphic to SL_2. Unique Hitchin Lagrangian CY3.")

    print("\n--- 4. E-polynomial (Hausel-Thaddeus) ---")
    e_poly = hausel_thaddeus_e_polynomial(2)
    terms = [f"{c}*t^{k}" if c > 0 else f"({c})*t^{k}"
             for k, c in sorted(e_poly.items())]
    print(f"  E(t) = {' + '.join(terms)}")
    chi_e = euler_characteristic_from_e_poly(e_poly)
    print(f"  chi = E(1) = {chi_e}")

    print("\n--- 5. Zero-section Bun^s(SL_2) Betti numbers ---")
    bun_betti = bun_sl2_genus2_betti()
    print(f"  Betti: {[bun_betti[k] for k in range(7)]}")
    print(f"  chi(Bun) = {euler_characteristic_from_betti(bun_betti)}")
    print(f"  Desale-Ramanan: (2,2) CI in P^5, b_3 = 4 = 2*genus")

    print("\n--- 6. Root datum ---")
    rd = root_datum_sl2_genus2()
    print(f"  Lattice rank: {rd.lattice_rank}")
    print(f"  Real roots: {rd.real_roots}")
    print(f"  Imaginary root source: {rd.imaginary_root_source}")
    print(f"  Langlands dual: {rd.langlands_dual}")

    print("\n--- 7. Generic Hitchin fibre ---")
    fibre = hitchin_fibre_topology_sl2_genus2()
    betti_f = fibre['betti_numbers']
    print(f"  Type: {fibre['fibre_type']}")
    print(f"  Betti: {[betti_f[k] for k in range(7)]}")
    print(f"  chi(fibre) = {fibre['euler_char']}")
    print(f"  Polarization type: {fibre['polarization_type']}")

    print("\n--- 8. Expected kappa ---")
    kap = expected_kappa_hitchin_sl2_g2()
    print(f"  kappa = {kap['expected_kappa']}")
    print(f"  kappa_crit = {kap['kappa_crit']} = dim(Sp_4)")
    print(f"  Self-dual: {kap['self_dual']}")

    print("\n--- 9. K3 x E comparison ---")
    comp = k3xe_comparison()
    print(f"  Hitchin base dim = {comp['hitchin_base_dim']}")
    print(f"  K3xE lattice rank = {comp['k3xe_bkm_lattice_rank']}")
    print(f"  Both involve Sp_4(Z): YES")
    print(f"  Hitchin dim_C={comp['hitchin_dim_C']} (hol. sympl.), fibre dim={comp['hitchin_lagrangian_fibre_dim']}")
    print(f"  K3xE dim_C={comp['k3xe_dim_C']} (literal CY3)")
    print(f"  Expected kappa match: {comp['hitchin_expected_kappa']} = {comp['k3xe_kappa']}")

    print("\n--- 10. Verification ---")
    results = verify_all(verbose=True)
    n_pass = sum(1 for v in results.values() if v)
    print(f"\n  {n_pass}/{len(results)} checks passed.")
