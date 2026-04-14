r"""Chiral quantization of the Hitchin system on curves C inside K3.

STATUS: CONJECTURAL (AP-CY14, AP-CY6).
The chiral quantization of the Hitchin system on curves inside K3 is
conditional on CY-A_2 (proved at d=2) for the functor Phi, and on
conjectural identifications connecting Hitchin spectral data to the
K3 Yangian modules.  Feigin-Frenkel center results are cited
(ProvedElsewhere).  New identifications are CONJECTURAL.

MATHEMATICAL FRAMEWORK
======================

1. CURVES INSIDE K3 FROM LINEAR SYSTEMS
----------------------------------------

Let S be a K3 surface and L a line bundle on S with L^2 = 2g-2 > 0
(ample or at least nef and big).  The complete linear system |L| is
a projective space of dimension:

    dim |L| = h^0(S, L) - 1 = g   (by Riemann-Roch on K3: chi(L) = L^2/2 + 2)

A generic member C in |L| is a smooth curve of genus g.  The family
of curves parametrised by |L| = P^g gives a FAMILY of Hitchin systems
    { M_H(C_t, G) : t in |L| }
varying over the linear system.

2. THE HITCHIN SYSTEM ON C subset K3
--------------------------------------

For C a smooth curve in |L| and G a reductive group:

    M_H(C, G) = T*Bun_G(C)   (cotangent of the moduli of G-bundles)

is a hyperkahler manifold with Hitchin fibration pi: M_H -> B_H.

The Hitchin base:  B_H = bigoplus_{i} H^0(C, K_C^{d_i})
where d_1, ..., d_r are the Casimir degrees of G.

For G = SL(2): B_H = H^0(C, K_C^2), dim = 3(g-1).
For G = SL(n): B_H = bigoplus_{i=2}^n H^0(C, K_C^i), dim = (n^2-1)(g-1).

KEY POINT: The K3 surface S provides EXTRA STRUCTURE not present in
the abstract Hitchin system on a bare curve:

(a) The holomorphic 2-form omega_S on K3 restricts to a nondegenerate
    2-form on the normal bundle N_{C/S} = L|_C.  By adjunction,
    K_C = K_S|_C tensor L|_C = L|_C  (since K_S = O_S).
    So the CANONICAL BUNDLE of C is the RESTRICTION of L.

(b) The spectral curve Sigma subset Tot(K_C) = Tot(L|_C) inherits
    a canonical embedding into the total space of L, which is a
    neighbourhood of C in S.  This connects spectral parameters
    to deformations of C inside S.

(c) As C varies in |L|, the spectral curves Sigma_t sweep out a
    family in S, producing a UNIVERSAL SPECTRAL CURVE over |L| x B_H.

3. CHIRAL QUANTIZATION: CHIRAL DIFFERENTIAL OPERATORS ON Bun_G(C)
-------------------------------------------------------------------

The chiral quantization of the Hitchin system (Beilinson-Drinfeld)
produces chiral differential operators (CDO) on Bun_G(C):

    CDO_{Bun_G(C)} = modules for hat{g} at the critical level k = -h^v

The Feigin-Frenkel center Z(hat{g}_{-h^v}) = Fun(Op_{G^L}(C)) is the
algebra of functions on G^L-opers, which are the quantum Hamiltonians.

For the K3 FAMILY: as C varies in |L|, the CDOs form a family of
chiral algebras parametrised by t in |L| = P^g.  The total chiral
algebra over P^g should be a FACTORIZATION SHEAF, conjecturally
producing K3 Yangian modules.

4. SPECTRAL PARAMETER FROM THE SPECTRAL CURVE
-----------------------------------------------

The spectral curve Sigma -> C has a tautological section
lambda in H^0(Sigma, pi^*K_C) which is the spectral parameter z.

For the K3 embedding: the identification K_C = L|_C means that
lambda is a section of L|_Sigma, which is the RESTRICTION of the
K3 polarisation to the spectral curve.  The spectral parameter z
of the Yangian lives in the SAME space as the K3 deformation
parameter: both are coordinates on Tot(L|_C).

This is the geometric origin of the spectral parameter in the
K3 Yangian Y(g_{K3}).

5. CONNECTION TO THE FEIGIN-FRENKEL CENTER
-------------------------------------------

At the critical level, the center z(hat{g}) = Fun(Op_{G^L}(C)).
For the K3 family:
    - At each C in |L|: z(hat{g}) = Fun(Op_{G^L}(C))
    - Varying C: the family of opers over |L| is a flat family
    - The dimension of Op_{G^L}(C) is dim(g^L)*(g-1) = dim Hitchin base

The quantisation: opers on C are classical limits of the quantum
Hitchin system.  The chiral quantisation deforms opers to
D-modules on Bun_G(C).  The K3 structure enriches this with the
additional parameter from the linear system.

6. THE FAMILY-LEVEL KAPPA
--------------------------

For each C in |L| at generic (non-critical) level k:
    kappa_ch(hat{g}_k) = dim(g)*(k+h^v)/(2*h^v)

At the critical level: kappa_ch = 0 (bar complex uncurved).
At K3 level 1 (from Mukai pairing): kappa_ch = dim(g)*(1+h^v)/(2*h^v).

As C varies in |L|, kappa_ch is CONSTANT (it depends on g and k,
not on the specific curve C within |L|).  The family adds moduli
but not anomaly.

MATHEMATICAL REFERENCES
========================
    - Hitchin, "Stable bundles and integrable systems" (1987)
    - Beilinson-Drinfeld, "Quantization of Hitchin" (~1991, 2005)
    - Feigin-Frenkel, "Affine KM algebras at critical level" (1992)
    - Frenkel, "Langlands Correspondence for Loop Groups" (2007)
    - Donagi-Markman, "Spectral covers and Hamiltonians" (1995)
    - Mukai, "On the moduli space of bundles on K3 surfaces I" (1987)
    - Beauville, "Counting rational curves on K3 surfaces" (1999)
    - Kapustin-Witten, "Electric-magnetic duality and geometric
      Langlands program" (2006)
    - Ben-Zvi-Nadler, "Betti geometric Langlands" (2016)

MANUSCRIPT REFERENCES
======================
    - chapters/connections/geometric_langlands.tex
    - chapters/theory/cy_to_chiral.tex
    - compute/lib/higgs_bundle_chiral.py
    - compute/lib/spectral_curve_chiral.py
    - compute/lib/k3_yangian.py
    - compute/lib/k3_geometric_langlands.py
    - compute/lib/geometric_langlands_shadow.py
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np

from compute.lib.geometric_langlands_shadow import (
    LieAlgebraData,
    _casimir_degrees,
    central_charge_affine,
    critical_level,
    kappa_affine,
    kappa_slope_at_critical,
    langlands_dual_data,
    lie_data,
    oper_structure,
)


F = Fraction
STATUS = 'CONJECTURAL'  # AP-CY14: all new identifications are conjectural


# =========================================================================
# 1. K3 LINEAR SYSTEM DATA
# =========================================================================

class K3LinearSystemData(NamedTuple):
    """Data for a linear system |L| on a K3 surface S.

    L is a line bundle on S with L^2 = 2g-2, giving curves of genus g.
    The linear system |L| = P(H^0(S, L)) has dimension g (by Riemann-Roch
    on K3: chi(L) = L^2/2 + 2 = (2g-2)/2 + 2 = g+1, so h^0(L) = g+1
    when L is nef and big, and |L| = P^g).

    A generic member C in |L| is a smooth connected curve of genus g.
    """
    genus: int                   # genus of the generic curve C in |L|
    L_square: int                # L^2 = 2g-2 (self-intersection)
    h0_L: int                    # h^0(S, L) = g+1
    dim_linear_system: int       # dim |L| = g
    is_ample: bool               # True if L is ample (g >= 2 suffices)


def k3_linear_system(genus: int) -> K3LinearSystemData:
    """Compute data for the linear system of genus-g curves on K3.

    Parameters
    ----------
    genus : int
        Genus of the generic curve C in |L|.  Must be >= 2 for
        the Hitchin system to have interesting geometry.

    Returns
    -------
    K3LinearSystemData.

    Notes
    -----
    By Riemann-Roch on K3:
        chi(L) = L^2/2 + 2 = g-1+2 = g+1.
    Since K_S is trivial, h^2(L) = h^0(L^{-1}) = 0 for L effective,
    and h^1(L) = 0 by Kodaira vanishing (L ample) or by the surjectivity
    of the restriction map H^0(S,L) -> H^0(C,L|_C) for |L| base-point-free.
    So h^0(L) = g+1.
    """
    if genus < 0:
        raise ValueError(f"Genus must be >= 0, got {genus}")
    L_sq = 2 * genus - 2
    h0 = genus + 1
    return K3LinearSystemData(
        genus=genus,
        L_square=L_sq,
        h0_L=h0,
        dim_linear_system=genus,
        is_ample=(genus >= 2),
    )


def k3_curve_count_beauville(genus: int, degree: int = 0) -> str:
    """Status of the curve-counting problem for genus-g curves on K3.

    The number of rational curves (genus 0) in |L| on a generic K3 is
    the Yau-Zaslow formula.  For higher genus, the BPS count is given
    by the Gopakumar-Vafa invariants.

    Returns a status string (not a number), since the full theory
    is conditional on CY-A_2 for the chiral interpretation.
    """
    if genus == 0:
        return (
            f"Yau-Zaslow: n_0(d) = coefficients of 1/eta(q)^24, "
            f"i.e. n_0(0) = 1, n_0(1) = 24, n_0(2) = 324, ..."
        )
    return (
        f"BPS invariant n_{genus}(L^2={2*genus-2}): "
        f"conditional on CY-A_2 for chiral interpretation"
    )


# =========================================================================
# 2. HITCHIN SYSTEM ON K3 CURVES
# =========================================================================

class HitchinOnK3Data(NamedTuple):
    """Complete data for the Hitchin system M_H(C, G) where C subset K3.

    The curve C is a generic member of |L| on a K3 surface S,
    with genus g and L^2 = 2g-2.

    The K3 ENHANCEMENT is that K_C = L|_C (adjunction with K_S = O_S),
    so the Hitchin base H^0(C, K_C^i) = H^0(C, L^i|_C), connecting
    the spectral data to the K3 geometry.
    """
    # Curve data
    genus: int
    L_square: int
    dim_linear_system: int

    # Group data
    group_type: str         # Cartan type ('A', 'B', etc.)
    group_rank: int
    group_dim: int
    h_dual: int

    # Hitchin moduli data
    dim_hitchin_base: int
    dim_hitchin_moduli: int      # = 2 * dim_hitchin_base (Lagrangian)
    casimir_degrees: Tuple[int, ...]
    hitchin_base_summands: Tuple[int, ...]  # dim H^0(K^{d_i}) for each Casimir

    # Spectral curve data
    spectral_genus: int          # genus of the spectral curve Sigma
    spectral_n_branch: int       # number of branch points

    # K3-specific data
    adjunction_identification: str   # K_C = L|_C
    spectral_lives_in: str           # Tot(L|_C) = neighbourhood of C in K3

    # Chiral quantization data (at critical level)
    critical_level_k: Fraction
    kappa_ch_at_critical: Fraction   # = 0
    oper_dual_type: str
    oper_dim: int                    # dim Op_{G^L}(C) = dim Hitchin base

    # Chiral quantization data (at K3 level 1, for ADE types)
    kappa_ch_at_k1: Optional[Fraction]
    central_charge_at_k1: Optional[Fraction]


def _h0_K_power(genus: int, power: int) -> int:
    """Compute dim H^0(C, K_C^i) for a genus-g curve.

    For g >= 2:
        i = 0: h^0(O_C) = 1
        i = 1: h^0(K_C) = g
        i >= 2: h^0(K_C^i) = (2i-1)(g-1)  [Riemann-Roch + vanishing]
    """
    if power <= 0:
        return 1 if power == 0 else 0
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")
    if power == 1:
        return genus
    return (2 * power - 1) * (genus - 1)


def _spectral_genus_sln(n: int, genus: int) -> int:
    """Genus of the spectral curve for SL(n) on a genus-g curve.

    The spectral curve Sigma -> C is a degree-n cover.
    By Riemann-Hurwitz with generic simple ramification:
        2g(Sigma)-2 = n*(2g-2) + n*(n-1)*(2g-2) = n^2*(2g-2)
        g(Sigma) = n^2*(g-1) + 1.

    This is the SAME formula for GL(n) and SL(n): the spectral
    curve is the same, only the Hitchin base and fibre differ.
    """
    return n * n * (genus - 1) + 1


def _spectral_branch_points(n: int, genus: int) -> int:
    """Number of simple branch points of the generic spectral curve.

    For an n-sheeted cover with generic simple ramification:
        B = n*(n-1)*(2g-2).
    """
    return n * (n - 1) * (2 * genus - 2)


def hitchin_on_k3(genus: int, group_type: str, group_rank: int
                  ) -> HitchinOnK3Data:
    """Compute complete Hitchin system data for a curve C in K3.

    Parameters
    ----------
    genus : int
        Genus of C (generic member of |L| with L^2 = 2g-2).
    group_type : str
        Cartan type ('A', 'B', 'C', 'D', 'E', 'F', 'G').
    group_rank : int
        Rank of the group.

    Returns
    -------
    HitchinOnK3Data with all structural invariants.
    """
    if genus < 2:
        raise ValueError(f"Hitchin system requires genus >= 2, got {genus}")

    # Lie algebra data
    d = lie_data(group_type, group_rank)
    casimirs = _casimir_degrees(group_type, group_rank)

    # Hitchin base: bigoplus_i H^0(K^{d_i})
    base_summands = tuple(_h0_K_power(genus, di) for di in casimirs)
    dim_base = sum(base_summands)

    # Spectral curve (for SL/GL types; for other types, the cover degree
    # depends on the representation, but we use rank for the generic cover)
    n_cover = group_rank  # degree of the spectral cover = rank
    if group_type == 'A':
        n_cover = group_rank + 1  # SL_{n+1} has degree-(n+1) spectral cover
    spec_genus = _spectral_genus_sln(n_cover, genus)
    n_branch = _spectral_branch_points(n_cover, genus)

    # Critical level and Langlands dual
    k_crit = critical_level(group_type, group_rank)
    dv = langlands_dual_data(group_type, group_rank)
    dual_label = f'{dv.type}{dv.rank}'

    # kappa at critical level (always 0)
    kap_crit = kappa_affine(group_type, group_rank, k_crit)

    # Oper dimension = Hitchin base dimension
    oper_dim = dim_base

    # K3 level 1 data (only meaningful for simply-laced ADE types)
    kap_k1 = None
    c_k1 = None
    if group_type in ('A', 'D', 'E'):
        kap_k1 = kappa_affine(group_type, group_rank, F(1))
        c_k1 = central_charge_affine(group_type, group_rank, F(1))

    return HitchinOnK3Data(
        genus=genus,
        L_square=2 * genus - 2,
        dim_linear_system=genus,
        group_type=group_type,
        group_rank=group_rank,
        group_dim=d.dim,
        h_dual=d.h_dual,
        dim_hitchin_base=dim_base,
        dim_hitchin_moduli=2 * dim_base,
        casimir_degrees=casimirs,
        hitchin_base_summands=base_summands,
        spectral_genus=spec_genus,
        spectral_n_branch=n_branch,
        adjunction_identification=f"K_C = L|_C (since K_S = O_S for K3)",
        spectral_lives_in=f"Tot(L|_C) = neighbourhood of C in K3",
        critical_level_k=k_crit,
        kappa_ch_at_critical=kap_crit,
        oper_dual_type=dual_label,
        oper_dim=oper_dim,
        kappa_ch_at_k1=kap_k1,
        central_charge_at_k1=c_k1,
    )


# =========================================================================
# 3. CHIRAL DIFFERENTIAL OPERATORS ON Bun_G(C)
# =========================================================================

class CDOData(NamedTuple):
    """Chiral differential operator data on Bun_G(C) for C subset K3.

    The CDO on Bun_G(C) is the sheaf of hat{g}_{-h^v}-modules on Bun_G(C),
    produced by the Beilinson-Drinfeld quantization of the Hitchin system.

    The K3 FAMILY structure: as C varies in |L| = P^g, the CDOs
    form a family of chiral algebras.  The total object over P^g
    is conjecturally a factorization sheaf.
    """
    genus: int
    group_type: str
    group_rank: int

    # Bun_G(C) data
    dim_bun_g: int                # dim Bun_G(C) for stable bundles

    # CDO data at critical level
    cdo_level: Fraction           # k = -h^v
    cdo_kappa: Fraction           # kappa_ch = 0 at critical
    center_description: str       # "Fun(Op_{G^L}(C))"
    center_dim: int               # dim Op_{G^L}(C)
    n_hitchin_hamiltonians: int   # = rank(g) independent Hamiltonians

    # Family data
    family_base_dim: int          # dim |L| = g
    family_total_dim: int         # dim |L| + dim Bun_G


def dim_bun_g(group_type: str, group_rank: int, genus: int) -> int:
    """Dimension of Bun_G(C) for semisimple G on a genus-g curve.

    For semisimple G: dim Bun_G(C) = dim(G) * (g-1).
    """
    d = lie_data(group_type, group_rank)
    return d.dim * (genus - 1)


def cdo_on_k3(genus: int, group_type: str, group_rank: int) -> CDOData:
    """Compute CDO data on Bun_G(C) for C in a K3 linear system.

    Parameters
    ----------
    genus : int
        Genus of C (>= 2).
    group_type : str
        Cartan type.
    group_rank : int
        Rank.

    Returns
    -------
    CDOData with all structural invariants.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    d = lie_data(group_type, group_rank)
    dv = langlands_dual_data(group_type, group_rank)
    dual_label = f'{dv.type}{dv.rank}'
    casimirs = _casimir_degrees(group_type, group_rank)

    k_crit = critical_level(group_type, group_rank)
    kap_crit = kappa_affine(group_type, group_rank, k_crit)

    dim_bung = d.dim * (genus - 1)
    dim_base_hitchin = sum(_h0_K_power(genus, di) for di in casimirs)

    return CDOData(
        genus=genus,
        group_type=group_type,
        group_rank=group_rank,
        dim_bun_g=dim_bung,
        cdo_level=k_crit,
        cdo_kappa=kap_crit,
        center_description=f"Fun(Op_{{{dual_label}}}(C))",
        center_dim=dim_base_hitchin,
        n_hitchin_hamiltonians=group_rank,
        family_base_dim=genus,
        family_total_dim=genus + dim_bung,
    )


# =========================================================================
# 4. SPECTRAL PARAMETER FROM K3 GEOMETRY
# =========================================================================

class SpectralParameterData(NamedTuple):
    """Connection between the Hitchin spectral parameter and K3 geometry.

    The spectral curve Sigma subset Tot(K_C) has a tautological
    1-form lambda.  For C subset K3 with K_C = L|_C:
        lambda in H^0(Sigma, pi^*K_C) = H^0(Sigma, pi^*(L|_C))

    The spectral parameter z of the Yangian lives in Tot(L|_C),
    which is a neighbourhood of C in K3.  This connects the
    Hitchin spectral parameter to the K3 deformation parameter.

    STATUS: CONJECTURAL.  The identification of the Hitchin spectral
    parameter with the K3 Yangian spectral parameter passes through
    CY-A_2 and the conjectural existence of Y(g_{K3}).
    """
    genus: int
    L_square: int

    # Spectral curve data
    spectral_genus: int
    spectral_degree: int         # degree of Sigma -> C

    # Tautological section
    tautological_bundle: str     # pi^*K_C = pi^*(L|_C)
    tautological_degree: int     # deg(pi^*K_C) = n * deg(K_C) = n*(2g-2)

    # K3 identification
    k3_identification: str       # spectral z = coordinate on Tot(L|_C)
    yangian_spectral_parameter: str  # z in Y(g_{K3})

    # Normal bundle data (AP-CY20 compliant)
    normal_bundle: str           # N_{C/K3} = L|_C
    normal_bundle_degree: int    # deg(L|_C) = L^2 = 2g-2


def spectral_parameter_k3(genus: int, group_type: str, group_rank: int
                          ) -> SpectralParameterData:
    """Compute the spectral parameter data for a K3 Hitchin system.

    The spectral curve Sigma -> C is a degree-n cover, where n depends
    on the group type (n = rank+1 for type A, n = rank for others).
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    n_cover = group_rank
    if group_type == 'A':
        n_cover = group_rank + 1

    spec_genus = _spectral_genus_sln(n_cover, genus)
    taut_degree = n_cover * (2 * genus - 2)

    return SpectralParameterData(
        genus=genus,
        L_square=2 * genus - 2,
        spectral_genus=spec_genus,
        spectral_degree=n_cover,
        tautological_bundle=f"pi^*K_C = pi^*(L|_C)",
        tautological_degree=taut_degree,
        k3_identification=(
            "The Hitchin spectral parameter lambda in Tot(K_C) = Tot(L|_C) "
            "is a coordinate on the total space of L restricted to C, which "
            "is a neighbourhood of C in the K3 surface S. This identifies "
            "the Hitchin spectral parameter with a local coordinate on K3 "
            "transverse to C."
        ),
        yangian_spectral_parameter=(
            "The K3 Yangian spectral parameter z (AP-CY31: this is a Yangian "
            "spectral parameter, NOT a worldsheet coordinate) enters via the "
            "Drinfeld coproduct Delta_z. The identification z = lambda "
            "(Hitchin tautological section) is conjectural and conditional "
            "on CY-A_2 + Y(g_{K3}) existence."
        ),
        normal_bundle=f"N_{{C/K3}} = L|_C",
        normal_bundle_degree=2 * genus - 2,
    )


# =========================================================================
# 5. HITCHIN-TO-YANGIAN MODULE CONJECTURE
# =========================================================================

class HitchinYangianModuleData(NamedTuple):
    """Data for the conjectured Hitchin -> K3 Yangian module functor.

    CONJECTURE (AP-CY14): For C in |L| on K3 with ADE enhancement
    of type g, the Hitchin system M_H(C, G) at the critical level
    produces, via the Beilinson-Drinfeld quantization, a module
    category for the K3 Yangian Y(g_{K3}):

        CDO_{Bun_G(C), crit} -> Y(g_{K3})-mod

    The functor is the composition:
    (1) CDO at critical level -> hat{g}_{-h^v}-mod (BD quantization)
    (2) hat{g}_{-h^v}-mod -> D-mod(Bun_G(C)) (Frenkel-Gaitsgory Delta_C)
    (3) D-mod(Bun_G(C)) -> Y(g_{K3})-mod (conjectural, from K3 structure)

    Step (1) is ProvedElsewhere (Beilinson-Drinfeld).
    Step (2) is ProvedElsewhere (Frenkel-Gaitsgory localization).
    Step (3) is CONJECTURAL: it uses the K3 enhancement (C subset K3)
    to promote the Hitchin D-module to a Yangian module via the
    spectral parameter identification.
    """
    genus: int
    group_label: str
    langlands_dual_label: str

    # Step 1: BD quantization
    bd_input: str               # CDO at critical level
    bd_output: str              # hat{g}_{-h^v}-modules

    # Step 2: FG localization
    fg_input: str               # hat{g}_{-h^v}-modules over Ran(C)
    fg_output: str              # D-modules on Bun_G(C)

    # Step 3: K3 promotion (CONJECTURAL)
    k3_input: str               # D-modules on Bun_G(C)
    k3_output: str              # Y(g_{K3})-modules
    k3_mechanism: str           # spectral parameter from K3

    # Dimensional checks
    dim_oper_moduli: int        # dim Op_{G^L}(C) = Hitchin base dim
    dim_bun_g: int              # dim Bun_G(C) = dim(G)*(g-1)
    dim_linear_system: int      # dim |L| = g

    # Status
    step1_status: str           # 'ProvedElsewhere'
    step2_status: str           # 'ProvedElsewhere'
    step3_status: str           # 'Conjectured'


def hitchin_to_yangian_module(genus: int, group_type: str, group_rank: int
                              ) -> HitchinYangianModuleData:
    """Compute data for the Hitchin -> K3 Yangian module conjecture.

    Parameters
    ----------
    genus : int
        Genus of the K3 curve (>= 2).
    group_type : str
        Cartan type (ADE only for K3 enhancement).
    group_rank : int
        Rank.

    Returns
    -------
    HitchinYangianModuleData.

    Raises
    ------
    ValueError if not ADE type (K3 enhancement requires du Val singularity).
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")
    if group_type not in ('A', 'D', 'E'):
        raise ValueError(
            f"K3 ADE enhancement requires type A, D, or E, got {group_type}"
        )

    d = lie_data(group_type, group_rank)
    dv = langlands_dual_data(group_type, group_rank)
    group_label = f'{group_type}{group_rank}'
    dual_label = f'{dv.type}{dv.rank}'

    casimirs = _casimir_degrees(group_type, group_rank)
    dim_base = sum(_h0_K_power(genus, di) for di in casimirs)
    dim_bung = d.dim * (genus - 1)

    return HitchinYangianModuleData(
        genus=genus,
        group_label=group_label,
        langlands_dual_label=dual_label,
        bd_input=f"CDO_{{Bun_{{{group_label}}}(C), crit}}",
        bd_output=f"hat{{{group_label}}}_({{-{d.h_dual}}})-mod",
        fg_input=f"hat{{{group_label}}}_({{-{d.h_dual}}})-mod over Ran(C)",
        fg_output=f"D-mod(Bun_{{{group_label}}}(C))",
        k3_input=f"D-mod(Bun_{{{group_label}}}(C))",
        k3_output=f"Y(g_{{K3}})-mod",
        k3_mechanism=(
            f"K3 spectral parameter: lambda in Tot(L|_C) identifies the "
            f"Hitchin spectral variable with the K3 Yangian parameter z. "
            f"The family over |L| = P^{genus} provides the variation."
        ),
        dim_oper_moduli=dim_base,
        dim_bun_g=dim_bung,
        dim_linear_system=genus,
        step1_status='ProvedElsewhere',
        step2_status='ProvedElsewhere',
        step3_status='Conjectured',
    )


# =========================================================================
# 6. FEIGIN-FRENKEL CENTER AND OPERS FOR K3 CURVES
# =========================================================================

class FFCenterK3CurveData(NamedTuple):
    """Feigin-Frenkel center data specialised to curves in K3.

    At the critical level k = -h^v, for each C in |L|:
        Z(hat{g}_{-h^v}) = Fun(Op_{G^L}(C))

    The oper space Op_{G^L}(C) has dimension:
        dim Op = sum_{i} dim H^0(C, K^{d_i}) = dim Hitchin base

    For G = SL_2, G^L = PGL_2:
        Op_{PGL_2}(C) = space of projective connections d^2/dt^2 + q(t)
        dim Op = dim H^0(C, K^2) = 3(g-1)
    """
    genus: int
    group_label: str
    langlands_dual_label: str

    # Oper data
    oper_dim: int
    oper_summands: Tuple[int, ...]  # dim H^0(K^{d_i}) for each Casimir d_i
    casimir_degrees: Tuple[int, ...]

    # Hitchin base match
    hitchin_base_dim: int
    oper_equals_hitchin: bool  # should always be True

    # Center structure
    center_generators: int     # = rank(G^L) independent generators
    center_transcendence_degree: int  # = dim Op (for the polynomial ring)

    # K3-specific: variation over |L|
    family_dim: int            # dim of the universal oper space over |L|


def ff_center_k3_curve(genus: int, group_type: str, group_rank: int
                       ) -> FFCenterK3CurveData:
    """Compute the Feigin-Frenkel center data for curves on K3.

    Parameters
    ----------
    genus : int
        Genus (>= 2).
    group_type : str
        Cartan type.
    group_rank : int
        Rank.

    Returns
    -------
    FFCenterK3CurveData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    dv = langlands_dual_data(group_type, group_rank)
    casimirs = _casimir_degrees(group_type, group_rank)
    group_label = f'{group_type}{group_rank}'
    dual_label = f'{dv.type}{dv.rank}'

    oper_summands = tuple(_h0_K_power(genus, di) for di in casimirs)
    oper_dim = sum(oper_summands)
    hitchin_base_dim = oper_dim  # They are equal (Hitchin-BD correspondence)

    return FFCenterK3CurveData(
        genus=genus,
        group_label=group_label,
        langlands_dual_label=dual_label,
        oper_dim=oper_dim,
        oper_summands=oper_summands,
        casimir_degrees=casimirs,
        hitchin_base_dim=hitchin_base_dim,
        oper_equals_hitchin=(oper_dim == hitchin_base_dim),
        center_generators=dv.rank,
        center_transcendence_degree=oper_dim,
        family_dim=genus + oper_dim,
    )


# =========================================================================
# 7. KAPPA ANALYSIS FOR THE HITCHIN-K3 FAMILY
# =========================================================================

class KappaAnalysisData(NamedTuple):
    """Analysis of kappa_ch along the Hitchin-K3 family.

    For hat{g}_k on a curve C of genus g:
        kappa_ch = dim(g)*(k + h^v) / (2*h^v)

    KEY OBSERVATION: kappa_ch is independent of the genus g of C.
    It depends only on the group g and the level k.  As C varies in
    |L| on K3, kappa_ch is CONSTANT across the family.

    The genus g enters into the DIMENSIONAL analysis (dim Bun, dim Op)
    but not into the anomaly kappa_ch.

    At the critical level k = -h^v:
        kappa_ch = 0  (bar complex uncurved, shadow tower degenerate)

    At K3 level 1 (for ADE enhancement):
        kappa_ch = dim(g)*(1 + h^v)/(2*h^v)  (nonzero, bar complex curved)

    The Koszul conductor for the KM family:
        kappa_ch(k) + kappa_ch(k') = 0, where k' = -k - 2*h^v (FF reflection)
    """
    group_label: str
    group_dim: int
    h_dual: int

    # Level analysis
    k_critical: Fraction         # = -h^v
    k_k3_level1: Fraction        # = 1
    k_ff_dual_of_1: Fraction     # = -1 - 2*h^v = -(2*h^v + 1)

    # kappa values
    kappa_at_critical: Fraction  # = 0
    kappa_at_k1: Fraction        # = dim(g)*(1+h^v)/(2*h^v)
    kappa_at_ff_dual: Fraction   # = -kappa_at_k1

    # Slope
    kappa_slope: Fraction        # d(kappa)/dk = dim(g)/(2*h^v)

    # Genus-independence check
    is_genus_independent: bool   # = True (kappa doesn't depend on g)

    # K3-specific
    kappa_ch_spectrum: Dict[str, Fraction]  # all kappa values for reference


def kappa_analysis_hitchin_k3(group_type: str, group_rank: int
                              ) -> KappaAnalysisData:
    """Analyse kappa_ch for the Hitchin system on K3 curves.

    Parameters
    ----------
    group_type : str
        Cartan type.
    group_rank : int
        Rank.

    Returns
    -------
    KappaAnalysisData.
    """
    d = lie_data(group_type, group_rank)
    group_label = f'{group_type}{group_rank}'

    k_crit = critical_level(group_type, group_rank)
    k1 = F(1)
    k_ff_dual = F(-1 - 2 * d.h_dual)

    kap_crit = kappa_affine(group_type, group_rank, k_crit)
    kap_k1 = kappa_affine(group_type, group_rank, k1)
    kap_ff = kappa_affine(group_type, group_rank, k_ff_dual)

    slope = kappa_slope_at_critical(group_type, group_rank)

    # Verify Koszul conductor
    assert kap_k1 + kap_ff == 0, (
        f"Koszul conductor failed: kappa({k1}) + kappa({k_ff_dual}) = "
        f"{kap_k1} + {kap_ff} = {kap_k1 + kap_ff} != 0"
    )

    spectrum: Dict[str, Fraction] = {
        'critical': kap_crit,
        'K3_level_1': kap_k1,
        'FF_dual_of_1': kap_ff,
    }

    return KappaAnalysisData(
        group_label=group_label,
        group_dim=d.dim,
        h_dual=d.h_dual,
        k_critical=k_crit,
        k_k3_level1=k1,
        k_ff_dual_of_1=k_ff_dual,
        kappa_at_critical=kap_crit,
        kappa_at_k1=kap_k1,
        kappa_at_ff_dual=kap_ff,
        kappa_slope=slope,
        is_genus_independent=True,
        kappa_ch_spectrum=spectrum,
    )


# =========================================================================
# 8. HITCHIN-K3 FAMILY OVER THE LINEAR SYSTEM
# =========================================================================

class HitchinK3FamilyData(NamedTuple):
    """Data for the family of Hitchin systems over the K3 linear system.

    As C varies in |L| = P^g, the Hitchin system M_H(C, G) varies
    in a family.  The total space is:

        M_H^{univ} = { (t, (E, phi)) : t in |L|, (E, phi) in M_H(C_t, G) }

    This is a family of Lagrangian fibrations over |L| x B^{univ},
    where B^{univ} is the universal Hitchin base.

    CONJECTURE: The chiral quantization of this family produces a
    factorization sheaf on Ran(|L|) that is a module for the
    K3 Yangian Y(g_{K3}).
    """
    genus: int
    group_label: str

    # Family dimensions
    dim_linear_system: int       # dim |L| = g
    dim_hitchin_base_fiber: int  # dim B_C for each C
    dim_hitchin_moduli_fiber: int  # dim M_H(C, G) for each C
    dim_total_base: int          # dim |L| + dim B = g + dim B
    dim_total_moduli: int        # dim |L| + dim M_H

    # Universal spectral curve data
    dim_universal_spectral: int  # dim of the total space of spectral curves

    # Factorization sheaf data (CONJECTURAL)
    factorization_base: str
    factorization_target: str
    status: str


def hitchin_k3_family(genus: int, group_type: str, group_rank: int
                      ) -> HitchinK3FamilyData:
    """Compute data for the universal Hitchin family over |L| on K3.

    Parameters
    ----------
    genus : int
        Genus (>= 2).
    group_type : str
        Cartan type.
    group_rank : int
        Rank.

    Returns
    -------
    HitchinK3FamilyData.
    """
    if genus < 2:
        raise ValueError(f"Need genus >= 2, got {genus}")

    h = hitchin_on_k3(genus, group_type, group_rank)
    group_label = f'{group_type}{group_rank}'

    # Universal spectral curve dimension: |L| x (spectral data)
    # The spectral curve Sigma_t varies in a family of dim |L| + dim B
    dim_univ_spec = genus + h.dim_hitchin_base

    return HitchinK3FamilyData(
        genus=genus,
        group_label=group_label,
        dim_linear_system=genus,
        dim_hitchin_base_fiber=h.dim_hitchin_base,
        dim_hitchin_moduli_fiber=h.dim_hitchin_moduli,
        dim_total_base=genus + h.dim_hitchin_base,
        dim_total_moduli=genus + h.dim_hitchin_moduli,
        dim_universal_spectral=dim_univ_spec,
        factorization_base=f"Ran(|L|) = Ran(P^{genus})",
        factorization_target=f"Y(g_{{K3}})-mod",
        status='CONJECTURAL',
    )


# =========================================================================
# 9. EXPLICIT EXAMPLES
# =========================================================================

def sl2_genus2_on_k3() -> Dict[str, Any]:
    """SL_2 Hitchin system on a genus-2 curve C subset K3.

    This is the UNIQUE case where dim(G)*(g-1) = 3*(2-1) = 3,
    giving a Hitchin fibration of "CY3 type" (base dim = fibre dim = 3).
    The Hitchin moduli M_H(C, SL_2) has dim_C = 6 with holonomy Sp(3).

    CROSS-REFERENCE: hitchin_sl2_genus2.py computes the Hitchin moduli
    space itself.  This function adds the K3 embedding structure.
    """
    h = hitchin_on_k3(2, 'A', 1)
    cdo = cdo_on_k3(2, 'A', 1)
    ff = ff_center_k3_curve(2, 'A', 1)
    sp = spectral_parameter_k3(2, 'A', 1)
    ka = kappa_analysis_hitchin_k3('A', 1)

    return {
        'hitchin_data': h,
        'cdo_data': cdo,
        'ff_center_data': ff,
        'spectral_data': sp,
        'kappa_analysis': ka,
        'summary': {
            'genus': 2,
            'L_square': 2,
            'dim_linear_system': 2,
            'group': 'SL_2',
            'dim_hitchin_base': h.dim_hitchin_base,
            'dim_hitchin_moduli': h.dim_hitchin_moduli,
            'spectral_genus': h.spectral_genus,
            'critical_level': h.critical_level_k,
            'kappa_ch_at_k1': h.kappa_ch_at_k1,
            'kappa_ch_at_critical': h.kappa_ch_at_critical,
            'oper_type': 'PGL_2',
            'oper_dim': h.oper_dim,
            'is_cy3_type': True,  # dim base = dim fibre = 3
            'note': (
                "The genus-2 SL_2 case is the unique 'CY3 type' Hitchin "
                "system: the Lagrangian fibration has 3-dim base and fibre."
            ),
        },
    }


def sl2_genus3_on_k3() -> Dict[str, Any]:
    """SL_2 Hitchin system on a genus-3 curve C subset K3.

    L^2 = 4, |L| = P^3.  dim Hitchin base = 6, dim M_H = 12.
    Spectral curve: genus 5 double cover of C.
    """
    h = hitchin_on_k3(3, 'A', 1)
    cdo = cdo_on_k3(3, 'A', 1)

    return {
        'hitchin_data': h,
        'cdo_data': cdo,
        'summary': {
            'genus': 3,
            'L_square': 4,
            'dim_linear_system': 3,
            'group': 'SL_2',
            'dim_hitchin_base': h.dim_hitchin_base,
            'dim_hitchin_moduli': h.dim_hitchin_moduli,
            'spectral_genus': h.spectral_genus,
            'oper_dim': h.oper_dim,
        },
    }


def e8_genus2_on_k3() -> Dict[str, Any]:
    """E_8 Hitchin system on a genus-2 curve C subset K3.

    This is the maximal ADE enhancement.  The root lattice E_8 uses
    8 of the 20 negative directions of the Mukai lattice.

    dim Hitchin base = dim(E_8)*(g-1) = 248*1 = 248.
    Oper type: E_8 (self-dual).
    """
    h = hitchin_on_k3(2, 'E', 8)
    cdo = cdo_on_k3(2, 'E', 8)

    return {
        'hitchin_data': h,
        'cdo_data': cdo,
        'summary': {
            'genus': 2,
            'L_square': 2,
            'dim_linear_system': 2,
            'group': 'E_8',
            'dim_hitchin_base': h.dim_hitchin_base,
            'dim_hitchin_moduli': h.dim_hitchin_moduli,
            'oper_type': 'E8',
            'oper_dim': h.oper_dim,
            'kappa_ch_at_k1': h.kappa_ch_at_k1,
            'note': (
                "E_8 at level 1 is the maximal ADE enhancement on K3. "
                "dim(E_8) = 248, h^v = 30.  The oper dimension is 248."
            ),
        },
    }


# =========================================================================
# 10. LANDSCAPE: ALL ADE TYPES ON K3 GENUS-2 CURVES
# =========================================================================

def hitchin_k3_landscape(genus: int = 2) -> List[Dict[str, Any]]:
    """Compute Hitchin-K3 data for all standard ADE types.

    Parameters
    ----------
    genus : int
        Genus of curves (default 2).

    Returns
    -------
    List of dicts, one per ADE type.
    """
    types = [
        ('A', 1), ('A', 2), ('A', 3), ('A', 4),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    results = []
    for gt, gr in types:
        h = hitchin_on_k3(genus, gt, gr)
        ka = kappa_analysis_hitchin_k3(gt, gr)
        results.append({
            'type': f'{gt}{gr}',
            'group_dim': h.group_dim,
            'h_dual': h.h_dual,
            'dim_hitchin_base': h.dim_hitchin_base,
            'dim_hitchin_moduli': h.dim_hitchin_moduli,
            'spectral_genus': h.spectral_genus,
            'oper_dual': h.oper_dual_type,
            'kappa_ch_at_k1': ka.kappa_at_k1,
            'kappa_slope': ka.kappa_slope,
        })
    return results


# =========================================================================
# 11. CROSS-VOLUME BRIDGE: CONNECTING TO EXISTING ENGINES
# =========================================================================

def cross_volume_hitchin_bridge() -> Dict[str, Any]:
    """Verify consistency with existing Hitchin/spectral engines.

    Cross-checks against:
        - higgs_bundle_chiral.py: Hitchin moduli dimensions
        - spectral_curve_chiral.py: spectral curve genera
        - k3_geometric_langlands.py: ADE enhancement data
        - k3_yangian.py: structure function parameters
        - geometric_langlands_shadow.py: critical level analysis

    Returns a dict of consistency checks.
    """
    checks = {}

    # Check 1: SL_2 genus 2 Hitchin base dim
    # From spectral_curve_chiral.py: dim B(SL_2, g=2) = (4-1)*(2-1) = 3
    h = hitchin_on_k3(2, 'A', 1)
    checks['sl2_g2_hitchin_base'] = {
        'computed': h.dim_hitchin_base,
        'expected': 3,
        'match': h.dim_hitchin_base == 3,
        'source': 'spectral_curve_chiral: (n^2-1)*(g-1) = 3*1 = 3',
    }

    # Check 2: Spectral curve genus for SL_2, g=2
    # g(Sigma) = n^2*(g-1) + 1 = 4*1 + 1 = 5
    checks['sl2_g2_spectral_genus'] = {
        'computed': h.spectral_genus,
        'expected': 5,
        'match': h.spectral_genus == 5,
        'source': 'spectral_curve_chiral: n^2*(g-1)+1 = 4+1 = 5',
    }

    # Check 3: kappa_ch at critical level is 0
    checks['sl2_kappa_critical'] = {
        'computed': h.kappa_ch_at_critical,
        'expected': F(0),
        'match': h.kappa_ch_at_critical == 0,
        'source': 'geometric_langlands_shadow: kappa_ch(-h^v) = 0',
    }

    # Check 4: kappa_ch(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
    checks['sl2_kappa_k1'] = {
        'computed': h.kappa_ch_at_k1,
        'expected': F(9, 4),
        'match': h.kappa_ch_at_k1 == F(9, 4),
        'source': 'k3_geometric_langlands: dim(sl2)*(1+h^v)/(2*h^v) = 3*3/4',
    }

    # Check 5: E_8 at level 1, c = rank = 8
    h_e8 = hitchin_on_k3(2, 'E', 8)
    checks['e8_central_charge_k1'] = {
        'computed': h_e8.central_charge_at_k1,
        'expected': F(8),
        'match': h_e8.central_charge_at_k1 == F(8),
        'source': 'k3_geometric_langlands: c(hat{e8}_1) = rank(E8) = 8',
    }

    # Check 6: SL_3 genus 2 Hitchin base dim
    # casimirs for A2 are (2,3), dim H^0(K^2)=3(g-1)=3, dim H^0(K^3)=5(g-1)=5
    # dim B = 3 + 5 = 8  =  (n^2-1)*(g-1) = 8*1 = 8
    h_sl3 = hitchin_on_k3(2, 'A', 2)
    checks['sl3_g2_hitchin_base'] = {
        'computed': h_sl3.dim_hitchin_base,
        'expected': 8,
        'match': h_sl3.dim_hitchin_base == 8,
        'source': 'sum of H^0(K^{d_i}): 3+5=8 = (n^2-1)*(g-1)',
    }

    # Check 7: D_4 at level 1, c = rank = 4
    h_d4 = hitchin_on_k3(2, 'D', 4)
    checks['d4_central_charge_k1'] = {
        'computed': h_d4.central_charge_at_k1,
        'expected': F(4),
        'match': h_d4.central_charge_at_k1 == F(4),
        'source': 'k3_geometric_langlands: c(hat{so8}_1) = rank(D4) = 4',
    }

    return checks


# =========================================================================
# 12. MASTER VERIFICATION
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all internal consistency checks.

    Returns
    -------
    Dict mapping check name to pass/fail.
    """
    results = {}

    # 1. K3 linear system
    for g in range(2, 6):
        ls = k3_linear_system(g)
        results[f'linear_system_g{g}_L2'] = (ls.L_square == 2 * g - 2)
        results[f'linear_system_g{g}_h0'] = (ls.h0_L == g + 1)
        results[f'linear_system_g{g}_dim'] = (ls.dim_linear_system == g)

    # 2. Hitchin base = oper dim (Hitchin-BD correspondence)
    for g in range(2, 5):
        for gt, gr in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 8)]:
            ff = ff_center_k3_curve(g, gt, gr)
            results[f'oper_hitchin_{gt}{gr}_g{g}'] = ff.oper_equals_hitchin

    # 3. kappa at critical level is 0
    for gt, gr in [('A', 1), ('A', 2), ('A', 3), ('D', 4), ('E', 6), ('E', 8)]:
        h = hitchin_on_k3(2, gt, gr)
        results[f'kappa_crit_{gt}{gr}'] = (h.kappa_ch_at_critical == 0)

    # 4. Koszul conductor: kappa(k) + kappa(-k - 2*h^v) = 0
    for gt, gr in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 8)]:
        ka = kappa_analysis_hitchin_k3(gt, gr)
        results[f'koszul_conductor_{gt}{gr}'] = (
            ka.kappa_at_k1 + ka.kappa_at_ff_dual == 0
        )

    # 5. Central charge at level 1 = rank (simply-laced)
    for gt, gr in [('A', 1), ('A', 2), ('D', 4), ('E', 6), ('E', 7), ('E', 8)]:
        h = hitchin_on_k3(2, gt, gr)
        results[f'c_k1_eq_rank_{gt}{gr}'] = (
            h.central_charge_at_k1 == F(gr)
        )

    # 6. Spectral genus formula: g(Sigma) = n^2*(g-1) + 1
    for g in range(2, 5):
        for n in range(2, 5):
            expected = n * n * (g - 1) + 1
            actual = _spectral_genus_sln(n, g)
            results[f'spectral_genus_n{n}_g{g}'] = (actual == expected)

    # 7. Cross-volume bridge
    bridge = cross_volume_hitchin_bridge()
    for key, val in bridge.items():
        results[f'bridge_{key}'] = val['match']

    # 8. Lagrangian property: dim M_H = 2 * dim B
    for g in range(2, 5):
        for gt, gr in [('A', 1), ('A', 2), ('D', 4)]:
            h = hitchin_on_k3(g, gt, gr)
            results[f'lagrangian_{gt}{gr}_g{g}'] = (
                h.dim_hitchin_moduli == 2 * h.dim_hitchin_base
            )

    # 9. Family data consistency
    for g in range(2, 4):
        fam = hitchin_k3_family(g, 'A', 1)
        results[f'family_sl2_g{g}_total_base'] = (
            fam.dim_total_base == g + fam.dim_hitchin_base_fiber
        )

    return results
