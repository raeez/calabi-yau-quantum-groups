r"""K3 geometric Langlands: from ADE-enhanced K3 chiral algebras to opers.

STATUS: CONJECTURAL (AP-CY14, AP-CY6).
All results connecting the K3 chiral algebra to geometric Langlands
are conditional on CY-A_2 (proved at d=2) for the functor Phi, and
on CY-A_3 (programme) for any d=3 extension.  Results about opers
and the Feigin-Frenkel center are cited from the literature
(ProvedElsewhere).  New identifications are CONJECTURAL.

MATHEMATICAL CONTENT
====================

1. ADE ENHANCEMENT ON K3 AND THE CHIRAL SUBALGEBRA

   At an ADE singularity of type g on K3, the derived category D^b(Coh(K3))
   acquires an exceptional collection whose endomorphism algebra is the
   path algebra of the ADE quiver.  Under the CY-to-chiral functor Phi
   (CY-A_2, proved at d=2), the chiral algebra A_{K3} contains g_hat_1
   (affine Kac-Moody at level 1) as a subalgebra.

   The level-1 embedding is forced: the Mukai pairing on H^*(K3, Z) restricts
   to the Cartan matrix of g on the ADE sublattice, giving the OPE
   J^a(z) J^b(w) ~ delta^{ab} / (z-w)^2 at level k=1.

2. FEIGIN-FRENKEL CENTER AT CRITICAL LEVEL

   The center z(g_hat) = Z(V_{-h^v}(g)) is isomorphic to Fun(Op_{G^L}(D))
   (Feigin-Frenkel 1992).  For the level-1 subalgebra of the K3 chiral
   algebra, the critical-level deformation k: 1 -> -h^v is a 1-parameter
   family in the Kac-Moody moduli.

   For sl_2 at level 1 on K3:
     - Level 1: kappa_ch = 3*3/(2*2*2) = 9/4
     - Critical level k = -2: kappa_ch = 0
     - The center z(sl_2_hat) = Fun(Op_{PGL_2}(D))
     - PGL_2 opers on D = Spec C[[t]]: projective connections d^2/dt^2 + q(t)

3. OPERS FROM K3 GEOMETRY

   An oper for G^L on D is a G^L-connection with Borel reduction and
   transversality.  For G = SL_2, G^L = PGL_2, an oper is a
   Sturm-Liouville operator d^2/dt^2 + q(t).

   The K3 connection: at the ADE enhancement, the exceptional fibre
   of the resolution pi: K3 -> K3_sing produces classes in H^2(K3, Z)
   whose periods determine the oper parameter q.

   For each ADE type g with rank r:
     - dim(Cartan of g^L) = r = rank(g)
     - Number of oper parameters on D = r (Casimir parametrization)
     - The K3 Mukai lattice embeds r parameters into its (4,20) signature

4. K3 YANGIAN AND LANGLANDS DUAL

   The K3 Yangian Y(g_{K3}) (CONJECTURAL, AP-CY14) at the abelian
   (gl_1) level is parametrised by h_1,...,h_24 with sum h_i = 0.

   For the ADE subalgebra at level k:
     - Yangian Y(g_hat_k) has spectral parameter u
     - Langlands dual level: k^L = -k - h^v (quantum geometric Langlands)
     - At k=1 for sl_2: k^L = -1 - 2 = -3 (note: k^L != critical level -2)
     - At the QGL dual level, kappa(sl_2, -3) = 3*(-3+2)/(2*2) = -3/4

   The QGL correspondence: Cat O_k(g_hat) <--> Cat O_{k^L}(g^L_hat)
   where k^L = -k - h^v for simply-laced types.

5. K3 x E ELLIPTIC FAMILY AND D-MODULES

   For an elliptically fibered K3 surface pi: S -> P^1 with section,
   the product K3 x E gives a family of chiral algebras parametrised
   by E.  The resulting object over E is a FACTORIZATION SHEAF, not
   simply a D-module.  The question of whether it is a Hecke eigensheaf
   passes through the Feigin-Frenkel localization functor Delta_X.

   For the level-1 subalgebra: the family V_1(g)(z) over z in E
   produces, upon localization, a D-module on Bun_G(E).  Since E
   is an elliptic curve, Bun_G(E) has a simple description:
     - For G = SL_2: Bun_{SL_2}(E) has two components (trivial and
       nontrivial bundles), with the trivial component isomorphic
       to E / (Z/2Z) (the Kummer quotient of the dual elliptic curve).

6. SHADOW TOWER AND LANGLANDS PARAMETER TYPE

   The G/L/C/M classification of the shadow tower (Vol I) maps
   conjecturally to the type of Langlands parameter:

     Class G (finite tower, r=2): polynomial QGL -> UNRAMIFIED parameters
     Class L (r=3, KM generic): rational QGL -> TAMELY RAMIFIED parameters
     Class C (r=4, beta-gamma): convergent QGL -> WILDLY RAMIFIED (regular)
     Class M (r=inf, Virasoro/W): Gevrey-1 QGL -> IRREGULAR parameters

   This is Conjecture shadow-convergence-qgl of geometric_langlands.tex.

CONVENTIONS
===========
  - kappa subscripts per AP113: kappa_ch only.
  - AP-CY14: all new results CONJECTURAL.
  - AP-CY6: CY-A_3 objects NEVER assumed to exist.
  - AP-CY11: conditionality propagates.
  - AP-CY5: root of unity vs generic q distinction maintained.

REFERENCES
==========
  - geometric_langlands_shadow.py (critical level, FF duality, opers)
  - k3_yangian.py (K3 Yangian structure function)
  - ade_yangian_level1.py (ADE enhancement on K3)
  - drinfeld_center_k3_heisenberg.py (braided structure)
  - Feigin-Frenkel, "Affine KM algebras at critical level" (1992)
  - Frenkel, "Langlands Correspondence for Loop Groups" (2007)
  - Frenkel-Gaitsgory, "D-modules on Bun_G" (2006)
  - Aganagic-Frenkel-Okounkov, "Quantum q-Langlands" (2017)
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
    central_charge_residue,
    critical_level,
    ff_dual_level,
    is_self_dual,
    kappa_affine,
    kappa_slope_at_critical,
    kapustin_witten_psi_exact,
    langlands_dual_data,
    lie_data,
    oper_structure,
    quantum_langlands_levels,
)


F = Fraction
STATUS = 'CONJECTURAL'  # AP-CY14


# =========================================================================
# 1. ADE ENHANCEMENT ON K3: LEVEL-1 SUBALGEBRA DATA
# =========================================================================

class ADEEnhancementData(NamedTuple):
    """Data for an ADE enhancement on K3 at level 1.

    At an ADE singularity of type g on K3, the chiral algebra Phi(D^b(Coh(K3)))
    contains g_hat_1 as a subalgebra (conditional on CY-A_2, proved at d=2).

    The level k=1 is forced by the Mukai pairing: the intersection form on
    the exceptional divisors of the resolution gives the Cartan matrix,
    normalised so that long roots have length^2 = 2, which is level 1.
    """
    g_type: str             # 'A', 'D', or 'E'
    g_rank: int             # rank of g
    g_label: str            # e.g. 'A1', 'D4', 'E8'
    g_dim: int              # dim(g)
    h_dual: int             # dual Coxeter number h^v
    level: Fraction         # k = 1 (forced by Mukai pairing)
    kappa_ch_level1: Fraction  # kappa_ch at level 1
    central_charge_level1: Fraction  # Sugawara c at level 1
    num_mukai_directions: int  # = rank(g), embedded in the Mukai lattice
    remaining_mukai_rank: int  # = 24 - rank(g)


def ade_enhancement(g_type: str, g_rank: int) -> ADEEnhancementData:
    """Compute ADE enhancement data for K3.

    The ADE singularity of type g embeds the root lattice Lambda_g
    into the Mukai lattice Lambda_Muk of K3 (signature (4,20), rank 24).

    Parameters
    ----------
    g_type : str
        Must be 'A', 'D', or 'E' (ADE types only for du Val singularities).
    g_rank : int
        Rank of the Lie algebra.

    Returns
    -------
    ADEEnhancementData with level-1 invariants.

    Raises
    ------
    ValueError if not an ADE type or rank exceeds Mukai bound.
    """
    if g_type not in ('A', 'D', 'E'):
        raise ValueError(
            f"ADE enhancement requires type A, D, or E, got {g_type}"
        )
    d = lie_data(g_type, g_rank)
    if d.rank > 20:
        raise ValueError(
            f"rank({g_type}{g_rank}) = {d.rank} exceeds the 20 negative "
            f"directions of the Mukai lattice (cannot embed ADE root lattice)"
        )

    k = F(1)
    kap = kappa_affine(g_type, g_rank, k)
    c = central_charge_affine(g_type, g_rank, k)
    assert c is not None, "level 1 is not critical for ADE types"

    return ADEEnhancementData(
        g_type=g_type,
        g_rank=g_rank,
        g_label=f'{g_type}{g_rank}',
        g_dim=d.dim,
        h_dual=d.h_dual,
        level=k,
        kappa_ch_level1=kap,
        central_charge_level1=c,
        num_mukai_directions=d.rank,
        remaining_mukai_rank=24 - d.rank,
    )


def all_ade_enhancements() -> Dict[str, ADEEnhancementData]:
    """Compute ADE enhancement data for all standard ADE types on K3.

    The ADE types that can enhance K3 are constrained by rank <= 20
    (embedding in the negative-definite part of the Mukai lattice).
    In practice, the du Val singularities on K3 surfaces have type
    A_n (n >= 1), D_n (n >= 4), E_6, E_7, E_8.

    Returns dict keyed by label (e.g. 'A1', 'D4', 'E8').
    """
    types = [
        ('A', 1), ('A', 2), ('A', 3), ('A', 4),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    result = {}
    for t, r in types:
        enh = ade_enhancement(t, r)
        result[enh.g_label] = enh
    return result


# =========================================================================
# 2. FEIGIN-FRENKEL CENTER FROM K3 ADE ENHANCEMENT
# =========================================================================

class FFCenterFromK3(NamedTuple):
    """Feigin-Frenkel center data arising from K3 ADE enhancement.

    At the critical level k = -h^v, the center Z(V_{-h^v}(g)) = Fun(Op_{G^L}(D)).
    The K3 ADE enhancement gives g_hat_1; the critical-level deformation
    is a 1-parameter family in the Kac-Moody moduli.

    STATUS: The FF theorem is ProvedElsewhere (Feigin-Frenkel 1992).
    The identification of the K3 ADE subalgebra with g_hat_1 is
    conditional on CY-A_2 (proved at d=2).
    """
    g_label: str
    h_dual: int
    critical_level: Fraction       # k_crit = -h^v
    kappa_ch_at_k1: Fraction       # kappa_ch at the K3 level k=1
    kappa_ch_at_critical: Fraction  # = 0
    langlands_dual_label: str      # G^L type
    oper_description: str
    casimir_degrees: Tuple[int, ...]
    sugawara_residue: Fraction     # Res_{k=-h^v}(c(k)) = -dim(g)*h^v
    kappa_slope: Fraction          # d(kappa_ch)/dk at critical


def ff_center_from_k3(g_type: str, g_rank: int) -> FFCenterFromK3:
    """Compute the Feigin-Frenkel center data for a K3 ADE enhancement.

    The FF center z(g_hat) = Fun(Op_{G^L}(D)) is a theorem of
    Feigin-Frenkel (1992).  The K3 connection is that the ADE
    enhancement provides a natural level-1 starting point, and the
    critical-level limit k -> -h^v produces the FF center.

    Parameters
    ----------
    g_type, g_rank : ADE type and rank.

    Returns
    -------
    FFCenterFromK3 with all relevant invariants.
    """
    d = lie_data(g_type, g_rank)
    dv = langlands_dual_data(g_type, g_rank)

    k_crit = critical_level(g_type, g_rank)
    kap_k1 = kappa_affine(g_type, g_rank, F(1))
    kap_crit = kappa_affine(g_type, g_rank, k_crit)
    assert kap_crit == 0, "kappa must vanish at critical level"

    casimirs = _casimir_degrees(dv.type, dv.rank)
    residue = central_charge_residue(g_type, g_rank)
    slope = kappa_slope_at_critical(g_type, g_rank)

    # Oper description
    dual_label = f'{dv.type}{dv.rank}'
    if dv.type == 'A' and dv.rank == 1:
        oper_desc = (
            f"Op_{{PGL_2}}(D): projective connections d^2/dt^2 + q(t) "
            f"on the formal disk D = Spec C[[t]]. "
            f"Single Casimir of degree 2."
        )
    else:
        oper_desc = (
            f"Op_{{{dual_label}}}(D): {dual_label}-opers on D = Spec C[[t]]. "
            f"Casimir degrees {casimirs}, rank {dv.rank}."
        )

    return FFCenterFromK3(
        g_label=f'{g_type}{g_rank}',
        h_dual=d.h_dual,
        critical_level=k_crit,
        kappa_ch_at_k1=kap_k1,
        kappa_ch_at_critical=kap_crit,
        langlands_dual_label=dual_label,
        oper_description=oper_desc,
        casimir_degrees=casimirs,
        sugawara_residue=residue,
        kappa_slope=slope,
    )


def ff_center_all_ade() -> Dict[str, FFCenterFromK3]:
    """Compute FF center data for all standard ADE types."""
    types = [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    return {f'{t}{r}': ff_center_from_k3(t, r) for t, r in types}


# =========================================================================
# 3. OPERS FOR sl_2 AT LEVEL 1 ON K3
# =========================================================================

class OperFromK3(NamedTuple):
    """Oper data arising from K3 ADE enhancement at sl_2.

    For g = sl_2, G^L = PGL_2, an oper on the formal disk D is a
    projective connection: a second-order ODE d^2/dt^2 + q(t).

    The K3 geometry determines q through the periods of the
    exceptional divisor class in H^2(K3, Z).
    """
    g_label: str
    langlands_dual: str
    oper_order: int                # = max Casimir degree
    num_oper_params_genus_g: Dict[int, int]  # genus -> dim of oper space
    k3_period_constraint: str      # description of the K3 constraint
    critical_kappa: Fraction       # = 0
    level1_kappa: Fraction


def opers_from_k3_sl2() -> OperFromK3:
    """Compute oper data for sl_2 at level 1 on K3.

    An SL_2 oper on a genus-g curve X is a projective connection on X.
    The space of projective connections on X has dimension:
      dim H^0(X, K_X^2) = 3(g-1) for g >= 2.

    For K3: the relevant curve is NOT the K3 surface itself (which is
    a surface, not a curve), but rather a curve C embedded in K3.
    The natural choice is a curve in the linear system |L| for a
    polarisation L on K3.  For a K3 of degree 2g-2 (the intersection
    number L^2 = 2g-2), the generic curve C in |L| has genus g.

    The oper parameters are determined by the restriction of the
    K3 periods to the curve C.
    """
    d = lie_data('A', 1)
    kap_k1 = kappa_affine('A', 1, F(1))
    kap_crit = F(0)

    genus_dims = {}
    for g in range(2, 6):
        # dim H^0(C_g, K^2) = 3(g-1) for projective connections
        genus_dims[g] = 3 * (g - 1)

    return OperFromK3(
        g_label='A1',
        langlands_dual='A1',  # SL_2 is self-dual (A_1 = A_1^L)
        oper_order=2,  # Casimir degree 2 for sl_2
        num_oper_params_genus_g=genus_dims,
        k3_period_constraint=(
            "The oper parameter q(t) is constrained by the K3 periods: "
            "for a curve C of genus g in the linear system |L| on K3, "
            "the restriction of the holomorphic 2-form omega_K3 to a "
            "tubular neighbourhood of C determines a quadratic differential "
            "on C, hence an oper.  This is conditional on the identification "
            "of the K3 period map with the oper moduli (CONJECTURAL)."
        ),
        critical_kappa=kap_crit,
        level1_kappa=kap_k1,
    )


def opers_from_k3_general(g_type: str, g_rank: int, genus: int) -> Dict[str, Any]:
    """Compute oper data for general ADE type on K3 at a given genus.

    For G^L on a genus-g curve:
      - Number of oper parameters = dim(G^L) * (g-1)
      - Graded by Casimir degrees d_1,...,d_r:
        dim H^0(C, K^{d_i}) = (2*d_i - 1)(g-1)

    Parameters
    ----------
    g_type, g_rank : ADE type.
    genus : genus of the curve C embedded in K3.

    Returns
    -------
    Dict with oper dimensions and Casimir grading.
    """
    if genus < 2:
        return {
            'g_label': f'{g_type}{g_rank}',
            'genus': genus,
            'error': 'genus must be >= 2 for nontrivial oper space',
        }

    dv = langlands_dual_data(g_type, g_rank)
    casimirs = _casimir_degrees(dv.type, dv.rank)
    total_dim = dv.dim * (genus - 1)

    # Use a list of (degree, dim) pairs because Casimir degrees can repeat
    # (e.g. D_4 has degrees (2, 4, 6, 4) with degree 4 appearing twice).
    # A dict would lose the multiplicity.
    graded = [(deg, (2 * deg - 1) * (genus - 1)) for deg in casimirs]
    graded_sum = sum(dim for _, dim in graded)

    return {
        'g_label': f'{g_type}{g_rank}',
        'langlands_dual': f'{dv.type}{dv.rank}',
        'genus': genus,
        'total_oper_dim': total_dim,
        'casimir_degrees': casimirs,
        'graded_dimensions': graded,
        'graded_sum_check': graded_sum,
        'matches_total': (graded_sum == total_dim),
    }


# =========================================================================
# 4. K3 YANGIAN LANGLANDS DUAL
# =========================================================================

class YangianLanglandsDual(NamedTuple):
    """Langlands dual data for the K3 Yangian at ADE enhancement.

    For the ADE subalgebra g_hat_k of the K3 chiral algebra:
    - Yangian Y(g_hat_k) at level k
    - QGL dual level: k^L = -k - h^v (for simply-laced ADE)
    - kappa_ch at level k and at k^L

    The QGL correspondence:
      Cat O_k(g_hat) <--> Cat O_{k^L}(g^L_hat)

    STATUS: CONJECTURAL for the K3-specific identification.
    The QGL correspondence itself is part of the Frenkel-Gaitsgory programme.
    """
    g_label: str
    k: Fraction                    # original level
    k_langlands: Fraction          # QGL dual level k^L = -k - h^v
    h_dual: int
    kappa_ch_k: Fraction           # kappa_ch at level k
    kappa_ch_kL: Fraction          # kappa_ch at dual level k^L
    kappa_sum: Fraction            # kappa(k) + kappa(k^L) -- NOT zero in general
    psi_k: Optional[Fraction]      # KW parameter at k
    psi_kL: Optional[Fraction]     # KW parameter at k^L
    psi_product: Optional[Fraction]  # should be 1 for QGL duality
    is_critical_dual: bool         # whether k^L = -h^v


def yangian_langlands_dual(g_type: str, g_rank: int,
                           k: Fraction = F(1)) -> YangianLanglandsDual:
    """Compute Langlands dual data for the K3 Yangian at ADE enhancement.

    For simply-laced types (ADE), the QGL dual level is k^L = -k - h^v.
    This maps:
      k = 1 -> k^L = -1 - h^v
      k = -h^v (critical) -> k^L = h^v - h^v = 0 (classical limit)
      k = 0 -> k^L = -h^v (critical of dual)

    The KW parameter Psi = k/(k + h^v) satisfies:
      Psi(k) * Psi(k^L) = k*k^L / ((k+h^v)(k^L+h^v))

    For the QGL dual k^L = -k - h^v:
      k^L + h^v = -k, so Psi(k^L) = k^L / (k^L + h^v) = (-k-h^v)/(-k) = (k+h^v)/k
      Psi(k) * Psi(k^L) = (k/(k+h^v)) * ((k+h^v)/k) = 1. Correct!

    Parameters
    ----------
    g_type, g_rank : ADE type.
    k : level (default 1, the K3 ADE enhancement level).

    Returns
    -------
    YangianLanglandsDual with all QGL dual data.
    """
    d = lie_data(g_type, g_rank)
    k_crit = critical_level(g_type, g_rank)

    # QGL dual level for simply-laced types
    k_L = -k - d.h_dual

    kap_k = kappa_affine(g_type, g_rank, k)
    kap_kL = kappa_affine(g_type, g_rank, k_L)

    psi_k = kapustin_witten_psi_exact(g_type, g_rank, k)
    psi_kL = kapustin_witten_psi_exact(g_type, g_rank, k_L)

    psi_prod = None
    if psi_k is not None and psi_kL is not None:
        psi_prod = psi_k * psi_kL

    return YangianLanglandsDual(
        g_label=f'{g_type}{g_rank}',
        k=k,
        k_langlands=k_L,
        h_dual=d.h_dual,
        kappa_ch_k=kap_k,
        kappa_ch_kL=kap_kL,
        kappa_sum=kap_k + kap_kL,
        psi_k=psi_k,
        psi_kL=psi_kL,
        psi_product=psi_prod,
        is_critical_dual=(k_L == k_crit),
    )


def yangian_langlands_dual_table(g_type: str, g_rank: int,
                                 levels: Optional[List[Fraction]] = None
                                 ) -> List[YangianLanglandsDual]:
    """Table of QGL dual data at multiple levels."""
    if levels is None:
        levels = [F(n) for n in [1, 2, 3, 5, 10]]
    return [yangian_langlands_dual(g_type, g_rank, k) for k in levels]


def sl2_langlands_dual_at_level1() -> Dict[str, Any]:
    """Detailed Langlands dual analysis for sl_2 at level 1 on K3.

    sl_2: h^v = 2.
    At k = 1: k^L = -1 - 2 = -3.
    kappa_ch(sl_2, 1) = 3*3/(2*2) = 9/4.
    kappa_ch(sl_2, -3) = 3*(-3+2)/(2*2) = 3*(-1)/4 = -3/4.
    kappa_sum = 9/4 + (-3/4) = 6/4 = 3/2.

    Note: kappa_sum != 0 for the QGL dual (it equals 0 for the FF dual).
    The FF dual of k=1 is k' = -1 - 2*2 = -5, and
    kappa(1) + kappa(-5) = 9/4 + 3*(-5+2)/4 = 9/4 - 9/4 = 0.

    The QGL dual and FF dual are DIFFERENT involutions:
      QGL: k -> -k - h^v  (Psi -> 1/Psi, duality of Cat O)
      FF:  k -> -k - 2*h^v (kappa -> -kappa, Koszul duality)
    """
    d = yangian_langlands_dual('A', 1, F(1))

    # Also compute the FF dual for comparison
    k_ff = ff_dual_level('A', 1, F(1))
    kap_ff = kappa_affine('A', 1, k_ff)

    return {
        'qgl_data': d,
        'ff_dual_level': k_ff,
        'kappa_ff_dual': kap_ff,
        'kappa_ff_sum': d.kappa_ch_k + kap_ff,
        'ff_sum_is_zero': (d.kappa_ch_k + kap_ff == 0),
        'qgl_vs_ff': (
            f"QGL dual of k=1: k^L = {d.k_langlands} (Psi -> 1/Psi). "
            f"FF dual of k=1: k' = {k_ff} (kappa -> -kappa). "
            f"These are DIFFERENT involutions on the level space."
        ),
    }


# =========================================================================
# 5. K3 x E ELLIPTIC FAMILY
# =========================================================================

class K3xEFamilyData(NamedTuple):
    """Data for the chiral algebra family over E from K3 x E.

    For an elliptic fibration pi: K3 -> P^1 and the product K3 x E,
    the chiral algebra Phi(D^b(Coh(K3))) restricted to E gives
    a family of chiral algebras parametrised by z in E.

    STATUS: CONJECTURAL.  Conditional on CY-A_2 (proved at d=2)
    for the K3 factor, and on the factorization structure of
    the product K3 x E (which is CY_3, hence conditional on CY-A_3).
    """
    g_label: str
    elliptic_curve_modulus: str  # tau (modular parameter of E)
    bun_g_description: str
    hecke_eigensheaf_status: str
    kappa_ch_k3: Fraction
    kappa_ch_k3xe: str  # description (kappa for K3xE is in the d=3 regime)


def k3xe_family_sl2() -> K3xEFamilyData:
    r"""K3 x E family data for the sl_2 enhancement.

    Bun_{SL_2}(E): For an elliptic curve E, the moduli of
    semi-stable SL_2-bundles on E is:
      Bun_{SL_2}(E) = E / (Z/2Z)  (Kummer of the dual curve)
    which is isomorphic to P^1 (the Kummer quotient of an elliptic curve).

    The Hecke eigensheaf question: the D-module on Bun_{SL_2}(E)
    arising from localisation of the K3 x E chiral algebra should
    be a Hecke eigensheaf for the PGL_2-local system on E determined
    by the K3 periods.

    STATUS: CONJECTURAL.  The K3 x E product is a CY 3-fold,
    so the chiral algebra Phi(D^b(Coh(K3 x E))) passes through
    CY-A_3 (programme).  However, the factored structure
    Phi(K3) tensor Phi(E) may be accessible via CY-A_2 alone
    for each factor separately.
    """
    kap_k3 = kappa_affine('A', 1, F(1))

    return K3xEFamilyData(
        g_label='A1',
        elliptic_curve_modulus='tau',
        bun_g_description=(
            "Bun_{SL_2}(E) = E/(Z/2Z) = P^1.  "
            "Two connected components: trivial bundle (generic point) "
            "and non-trivial (4 fixed points of the Z/2Z action = "
            "the 2-torsion points of E)."
        ),
        hecke_eigensheaf_status=(
            "CONJECTURAL.  The localisation of the K3 x E chiral algebra "
            "to Bun_{SL_2}(E) should produce a Hecke eigensheaf.  "
            "This passes through CY-A_3 for the product K3 x E.  "
            "The factored approach Phi(K3) x Phi(E) may avoid CY-A_3 "
            "by using CY-A_2 for each factor, but the tensor product "
            "structure of chiral algebras over Ran(E) is not proven "
            "to factorise in this way."
        ),
        kappa_ch_k3=kap_k3,
        kappa_ch_k3xe=(
            "kappa_ch for K3 x E is in the d=3 regime (CY-A_3 programme).  "
            "For the K3 factor alone: kappa_ch = 9/4 at level 1 for sl_2.  "
            "The product formula kappa_ch(K3 x E) is UNDEFINED until "
            "CY-A_3 is resolved."
        ),
    )


def bun_g_elliptic(g_type: str, g_rank: int) -> Dict[str, Any]:
    """Describe Bun_G(E) for an elliptic curve E.

    For a reductive group G, the moduli stack Bun_G(E) of
    semi-stable G-bundles on an elliptic curve E has a simple
    structure related to the Weyl group:

      Bun_G(E) = (E tensor Lambda_cochar) / W

    where Lambda_cochar is the cocharacter lattice and W is the Weyl group.
    For simply-laced types, this simplifies to E^r / W.

    For SL_2: Bun_{SL_2}(E) = E / (Z/2Z) = P^1.
    For SL_3: Bun_{SL_3}(E) = (E x E) / S_3 (the symmetric group).
    """
    d = lie_data(g_type, g_rank)

    # Weyl group order for ADE types
    weyl_orders = {
        ('A', 1): 2, ('A', 2): 6, ('A', 3): 24, ('A', 4): 120,
        ('D', 4): 192, ('D', 5): 1920,
        ('E', 6): 51840, ('E', 7): 2903040, ('E', 8): 696729600,
    }
    w_order = weyl_orders.get((g_type, g_rank), None)

    # Dimension of Bun_G(E)
    # For E: genus 1, so dim Bun_G(E) = dim(G) * (g-1) = 0.
    # But as a stack, Bun_G(E) has nontrivial structure.
    # The coarse moduli space is (E^r / W), dimension = r.
    dim_coarse = d.rank

    return {
        'g_label': f'{g_type}{g_rank}',
        'rank': d.rank,
        'weyl_order': w_order,
        'dim_coarse_moduli': dim_coarse,
        'structure': f'(E^{d.rank}) / W(g)',
        'description': (
            f"Bun_{{{g_type}{g_rank}}}(E) = "
            f"(E^{d.rank}) / W({g_type}{g_rank}), "
            f"coarse moduli of dimension {dim_coarse}.  "
            f"Weyl group |W| = {w_order}."
        ),
    }


# =========================================================================
# 6. SHADOW TOWER AND LANGLANDS PARAMETER TYPE
# =========================================================================

# Shadow class -> Langlands parameter type (CONJECTURAL, conj:shadow-convergence-qgl)
SHADOW_LANGLANDS_MAP = {
    'G': {
        'shadow_depth': 2,
        'qgl_analytic_type': 'polynomial',
        'langlands_parameter': 'unramified',
        'description': (
            'Class G: finite shadow tower (depth 2). QGL series is polynomial '
            'in kappa_QGL, terminating at degree 1. Corresponds to unramified '
            'Langlands parameters (trivial monodromy).'
        ),
    },
    'L': {
        'shadow_depth': 3,
        'qgl_analytic_type': 'rational',
        'langlands_parameter': 'tamely ramified',
        'description': (
            'Class L: KM generic (depth 3, cubic shadow nonzero). QGL series '
            'is rational in kappa_QGL with poles at roots of the Kac determinant. '
            'Corresponds to tamely ramified Langlands parameters.'
        ),
    },
    'C': {
        'shadow_depth': 4,
        'qgl_analytic_type': 'convergent',
        'langlands_parameter': 'wildly ramified (regular)',
        'description': (
            'Class C: beta-gamma type (depth 4). QGL series converges in a '
            'disk |kappa_QGL| < R_C. Corresponds to regular wildly ramified '
            'Langlands parameters.'
        ),
    },
    'M': {
        'shadow_depth': float('inf'),
        'qgl_analytic_type': 'Gevrey-1 divergent',
        'langlands_parameter': 'irregular',
        'description': (
            'Class M: Virasoro/W type (infinite depth). QGL series is Gevrey-1 '
            'divergent, requires Borel resummation. Stokes data encodes the '
            'shadow tower. Corresponds to irregular Langlands parameters.'
        ),
    },
}


def shadow_to_langlands(shadow_class: str) -> Dict[str, Any]:
    """Map a shadow class to the conjectured Langlands parameter type.

    Parameters
    ----------
    shadow_class : str
        One of 'G', 'L', 'C', 'M'.

    Returns
    -------
    Dict with the conjectured Langlands parameter type and QGL analytic type.

    Raises
    ------
    ValueError if shadow_class not in {G, L, C, M}.
    """
    if shadow_class not in SHADOW_LANGLANDS_MAP:
        raise ValueError(
            f"Unknown shadow class '{shadow_class}'. Must be G, L, C, or M."
        )
    data = SHADOW_LANGLANDS_MAP[shadow_class].copy()
    data['shadow_class'] = shadow_class
    data['status'] = 'CONJECTURAL (conj:shadow-convergence-qgl)'
    return data


def k3_ade_shadow_classes() -> Dict[str, Dict[str, Any]]:
    """Shadow classes for K3 ADE-enhanced chiral algebras.

    At ADE enhancement on K3, the level-1 Kac-Moody subalgebra
    g_hat_1 has shadow class L (shadow depth 3 for KM generic).

    The FULL K3 chiral algebra has a more complex shadow structure:
    - The Heisenberg part (24 free bosons) is class G (depth 2).
    - The interacting part (from the CY structure) may elevate to L or C.
    - For the generic K3 (no ADE enhancement): class G (free-field).
    - For ADE-enhanced K3: class L (from the KM subalgebra).

    STATUS: CONJECTURAL for the full K3 chiral algebra classification.
    The KM subalgebra classification is ProvedElsewhere (Vol I).
    """
    result = {}
    for label, enh in all_ade_enhancements().items():
        km_class = shadow_to_langlands('L')
        km_class['g_label'] = label
        km_class['kappa_ch_level1'] = float(enh.kappa_ch_level1)
        km_class['note'] = (
            f"KM subalgebra g_hat_1 for g = {label} is class L "
            f"(proved, Vol I). Full K3 chiral algebra classification "
            f"is conjectural."
        )
        result[label] = km_class
    return result


# =========================================================================
# 7. KAPPA SPECTRUM AT ADE ENHANCEMENT
# =========================================================================

def kappa_spectrum_ade(g_type: str, g_rank: int) -> Dict[str, Fraction]:
    """The four kappa values at an ADE enhancement point on K3.

    Per AP113, bare kappa is FORBIDDEN. The kappa-spectrum:
      kappa_ch:    from the chiral algebra Phi(K3) via the KM subalgebra
      kappa_BKM:   from the Borcherds-Kac-Moody algebra (if applicable)
      kappa_cat:   from holomorphic Euler characteristic chi(O_{K3}) = 2
      kappa_fiber: from the Mukai lattice rank = 24

    The kappa_ch value depends on the ADE type and level:
      kappa_ch(g_hat_1) = dim(g) * (1 + h^v) / (2 * h^v)

    For sl_2: kappa_ch = 3 * 3 / 4 = 9/4.
    For E_8: kappa_ch = 248 * 31 / 60 = 7688/60 = 1922/15.
    """
    d = lie_data(g_type, g_rank)
    kap_ch = kappa_affine(g_type, g_rank, F(1))

    return {
        'kappa_ch': kap_ch,
        'kappa_cat': F(2),   # chi(O_{K3}) = 2 for all K3
        'kappa_fiber': F(24),  # Mukai lattice rank
        # kappa_BKM depends on the specific Borcherds-Kac-Moody algebra,
        # which is not determined by the ADE type alone.
        # For the generic K3 without enhancement: kappa_BKM = 5 (weight of Delta_5).
    }


# =========================================================================
# 8. COMPREHENSIVE VERIFICATION
# =========================================================================

def verify_all() -> Dict[str, Any]:
    """Run all verification checks for the K3 geometric Langlands engine."""
    results = {}

    # 1. ADE enhancements
    enhancements = all_ade_enhancements()
    results['num_ade_types'] = len(enhancements)
    for label, enh in enhancements.items():
        results[f'ade_{label}_kappa'] = float(enh.kappa_ch_level1)
        results[f'ade_{label}_c'] = float(enh.central_charge_level1)

    # 2. FF centers
    ff_centers = ff_center_all_ade()
    for label, ff in ff_centers.items():
        results[f'ff_{label}_critical'] = float(ff.kappa_ch_at_critical)
        results[f'ff_{label}_residue'] = float(ff.sugawara_residue)

    # 3. QGL duality: Psi * Psi^L = 1
    for label in ['A1', 'A2', 'D4', 'E8']:
        t, r = label[0], int(label[1:])
        yd = yangian_langlands_dual(t, r, F(1))
        results[f'qgl_{label}_psi_product'] = (
            float(yd.psi_product) if yd.psi_product is not None else None
        )

    # 4. sl_2 detailed
    sl2_detail = sl2_langlands_dual_at_level1()
    results['sl2_ff_sum_zero'] = sl2_detail['ff_sum_is_zero']

    # 5. Shadow-Langlands map
    for cls in ['G', 'L', 'C', 'M']:
        data = shadow_to_langlands(cls)
        results[f'shadow_{cls}_type'] = data['langlands_parameter']

    return results


def full_computation() -> Dict[str, Any]:
    """Full computation suite."""
    return {
        'verification': verify_all(),
        'all_ade_enhancements': {
            k: v._asdict() for k, v in all_ade_enhancements().items()
        },
        'all_ff_centers': {
            k: v._asdict() for k, v in ff_center_all_ade().items()
        },
        'sl2_opers': opers_from_k3_sl2()._asdict(),
        'sl2_langlands_dual': sl2_langlands_dual_at_level1(),
        'k3xe_family': k3xe_family_sl2()._asdict(),
        'shadow_langlands': {
            cls: shadow_to_langlands(cls) for cls in ['G', 'L', 'C', 'M']
        },
        'oper_genus2_A1': opers_from_k3_general('A', 1, 2),
        'oper_genus2_D4': opers_from_k3_general('D', 4, 2),
        'oper_genus2_E8': opers_from_k3_general('E', 8, 2),
        'bun_sl2_E': bun_g_elliptic('A', 1),
        'bun_sl3_E': bun_g_elliptic('A', 2),
        'bun_e8_E': bun_g_elliptic('E', 8),
    }
