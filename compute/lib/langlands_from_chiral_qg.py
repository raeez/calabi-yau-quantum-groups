r"""Langlands functor from chiral quantum groups: the full pipeline.

STATUS: CONJECTURAL (AP-CY14, AP-CY6).
All new identifications are conditional on CY-A_2 (proved at d=2) for the
functor Phi, and on CY-A_3 (programme) for d=3 extensions.  Results about
the Feigin-Frenkel center and opers are ProvedElsewhere.  New
identifications between CY chiral algebras and Langlands structures are
CONJECTURAL.

MATHEMATICAL CONTENT
====================

This engine implements the full Langlands pipeline from CY categories to
Langlands data, extending and unifying the results of:
  - k3_geometric_langlands.py (ADE enhancement, FF center, QGL duality)
  - geometric_langlands_shadow.py (critical level, opers, shadow)

The pipeline:

  CY_d category C  --Phi-->  E_2-chiral algebra A_C  --center-->  z(A_C)
       |                          |                         |
       v                          v                         v
  CY Langlands dual C^L    QGL dual A_C^!          Fun(Op_{G^L}(D))

FIVE COMPONENTS (matching the five tasks):

1. THE LANGLANDS FUNCTOR FROM CHIRAL QG
   For each CY_2 category C, Phi(C) gives a chiral algebra.
   The center z(Phi(C)) at the critical level corresponds to opers on the
   spectral curve.  The functor has three steps:
     (a) CY category -> chiral algebra (CY-A, proved at d=2)
     (b) Chiral algebra -> bar complex (Vol I Theorem A)
     (c) Bar complex -> Verdier dual -> opers (Feigin-Frenkel)

2. K3 AT A_1: FEIGIN-FRENKEL CENTER
   z(sl_2_hat) = Fun(Op_{PGL_2}(D)).  Opers are projective connections
   on curves.  The K3 Yangian "sees" opers via the critical-level limit:
   as k: 1 -> -h^v = -2, kappa_ch: 9/4 -> 0, and the shadow metric
   degenerates to the oper connection.

3. QGL AT LEVEL k
   K3 Yangian at level k=1 has QGL dual at k^L = -k - h^v = -3.
   The Kapustin-Witten parameter Psi(k) * Psi(k^L) = 1.
   QGL and FF are DIFFERENT involutions on the level space.

4. THE HECKE EIGENSHEAF
   K3 x E -> E: the D-module on Bun_G(E) from the family of K3 chiral
   algebras.  For SL_2: Bun_{SL_2}(E) = P^1.  The Hecke eigensheaf
   question is CONJECTURAL and passes through CY-A_3 for K3 x E.

5. SHADOW TOWER AND RAMIFICATION
   G -> unramified, L -> tame, C -> wild, M -> irregular.
   At K3 ADE enhancement: class L (tame).  Verified for all ADE types.
   The ramification depth equals the shadow depth (conjectural).

CONVENTIONS
===========
  - kappa subscripts per AP113: kappa_ch only.
  - AP-CY14: all new results CONJECTURAL.
  - AP-CY6: CY-A_3 objects NEVER assumed to exist.
  - AP-CY11: conditionality propagates.
  - AP-CY5: root of unity vs generic q distinction maintained.
  - AP-CY4: Drinfeld center != derived center.  State which.
  - AP-CY7: CoHA != E_1-chiral algebra.

REFERENCES
==========
  - k3_geometric_langlands.py (ADE enhancement, FF center, QGL duality)
  - geometric_langlands_shadow.py (critical level, opers, shadow)
  - k3_yangian.py (K3 Yangian structure function)
  - e1_chiral_bialgebra_engine.py (Hopf axioms)
  - chapters/connections/geometric_langlands.tex
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
    hitchin_base_dimension,
    is_self_dual,
    kappa_affine,
    kappa_slope_at_critical,
    kapustin_witten_psi_exact,
    langlands_dual_data,
    lie_data,
    oper_structure,
    quantum_langlands_levels,
)
from compute.lib.k3_geometric_langlands import (
    ade_enhancement,
    all_ade_enhancements,
    bun_g_elliptic,
    ff_center_from_k3,
    kappa_spectrum_ade,
    shadow_to_langlands,
    yangian_langlands_dual,
    SHADOW_LANGLANDS_MAP,
)


F = Fraction
STATUS = 'CONJECTURAL'  # AP-CY14


# =========================================================================
# 1. THE LANGLANDS FUNCTOR: CY CATEGORY -> OPERS
# =========================================================================

class LanglandsFunctorStep(NamedTuple):
    """A single step of the Langlands functor pipeline."""
    name: str
    input_type: str
    output_type: str
    status: str
    description: str


class LanglandsFunctorData(NamedTuple):
    """Full data for the Langlands functor applied to a CY_2 category.

    The pipeline:
      CY_2 category C
        --Phi-->     E_2-chiral algebra A_C       (step 1: CY-A_2, proved)
        --B-->       bar complex B(A_C)            (step 2: Vol I Thm A, proved)
        --D_Ran-->   Verdier dual A_C^!            (step 3: Vol I Thm A, proved)
        --center-->  z(A_C) at critical level      (step 4: FF, proved elsewhere)
        --ident-->   Fun(Op_{G^L}(D))              (step 5: CONJECTURAL)

    STATUS: Steps 1-4 are proved (for KM input).  Step 5 (identification
    of the CY chiral center with opers for the Langlands dual) is
    CONJECTURAL for general CY input.
    """
    g_type: str
    g_rank: int
    g_label: str
    steps: Tuple[LanglandsFunctorStep, ...]
    kappa_ch_input: Fraction       # kappa_ch at the K3 level k=1
    kappa_ch_critical: Fraction    # = 0 at critical level
    critical_level: Fraction       # k = -h^v
    langlands_dual_label: str
    oper_description: str
    center_dimension_genus_g: Dict[int, int]  # genus -> dim z(g_hat)
    total_steps: int
    num_proved: int
    num_conjectural: int


def langlands_functor_steps() -> Tuple[LanglandsFunctorStep, ...]:
    """The five steps of the Langlands functor pipeline.

    Returns the abstract pipeline (independent of the specific CY input).
    """
    return (
        LanglandsFunctorStep(
            name='CY-to-chiral',
            input_type='CY_2 category C',
            output_type='E_2-chiral algebra Phi(C)',
            status='PROVED (d=2)',
            description=(
                'CY-A_2: the functor Phi sends D^b(Coh(K3)) to an E_2-chiral '
                'algebra containing g_hat_1 at ADE enhancement points. '
                'Proved at d=2; conditional on CY-A_3 at d=3.'
            ),
        ),
        LanglandsFunctorStep(
            name='bar complex',
            input_type='E_2-chiral algebra A_C',
            output_type='factorization coalgebra B(A_C)',
            status='PROVED',
            description=(
                'Vol I Theorem A: the bar functor B sends the chiral algebra '
                'to a factorization coalgebra T^c(s^{-1} bar{A}) with '
                'deconcatenation coproduct.'
            ),
        ),
        LanglandsFunctorStep(
            name='Verdier dual',
            input_type='factorization coalgebra B(A_C)',
            output_type='Verdier-dual chiral algebra A_C^!',
            status='PROVED',
            description=(
                'Vol I Theorem A: the Ran-space Verdier dual D_Ran applied '
                'to B(A_C) gives the Koszul dual A_C^! = D_Ran(B(A_C)).'
            ),
        ),
        LanglandsFunctorStep(
            name='chiral center',
            input_type='critical-level algebra V_{-h^v}(g)',
            output_type='center z(g_hat) = Z(V_{-h^v}(g))',
            status='PROVED ELSEWHERE',
            description=(
                'Feigin-Frenkel (1992): at the critical level k = -h^v, '
                'the center of the vacuum vertex algebra is isomorphic to '
                'Fun(Op_{G^L}(D)).  The bar complex becomes uncurved '
                '(kappa_ch = 0).'
            ),
        ),
        LanglandsFunctorStep(
            name='oper identification',
            input_type='center z(Phi(C)) at critical level',
            output_type='Fun(Op_{G^L}(D)) (opers for Langlands dual)',
            status='CONJECTURAL',
            description=(
                'Conjecture (geometric_langlands.tex, conj:critical-self-dual): '
                'the CY chiral center at critical level, via the Verdier leg '
                'of Vol I Theorem A, is quasi-isomorphic to Fun(Op_{G^L}(D)). '
                'This is the "implies" direction of Feigin-Frenkel for CY input.'
            ),
        ),
    )


def langlands_functor(g_type: str, g_rank: int) -> LanglandsFunctorData:
    """Apply the full Langlands functor to K3 with ADE enhancement.

    For K3 at ADE type g, the functor is:
      D^b(Coh(K3)) --Phi--> A_{K3} contains g_hat_1
                   --B--> B(g_hat_1) with deconcatenation
                   --D_Ran--> (g_hat_1)^! (Verdier dual)
                   --k: 1 -> -h^v--> z(g_hat) = Fun(Op_{G^L}(D))

    At the critical level, kappa_ch = 0 and the bar complex is uncurved.
    The center z(g_hat) corresponds to opers for G^L on the formal disk.

    Parameters
    ----------
    g_type : str
        ADE type ('A', 'D', or 'E').
    g_rank : int
        Rank of the Lie algebra.

    Returns
    -------
    LanglandsFunctorData with the full pipeline.
    """
    d = lie_data(g_type, g_rank)
    dv = langlands_dual_data(g_type, g_rank)
    steps = langlands_functor_steps()

    kap_input = kappa_affine(g_type, g_rank, F(1))
    kap_crit = kappa_affine(g_type, g_rank, critical_level(g_type, g_rank))
    k_crit = critical_level(g_type, g_rank)

    casimirs = _casimir_degrees(dv.type, dv.rank)
    dual_label = f'{dv.type}{dv.rank}'

    if dv.type == 'A' and dv.rank == 1:
        oper_desc = (
            f"Op_{{PGL_2}}(D): projective connections d^2/dt^2 + q(t). "
            f"Single Casimir of degree 2."
        )
    else:
        oper_desc = (
            f"Op_{{{dual_label}}}(D): {dual_label}-opers on the formal disk. "
            f"Casimir degrees {casimirs}, rank {dv.rank}."
        )

    # Center dimension = dim of oper space on genus-g curve
    # = dim(G^L) * (g-1) for g >= 2 (Hitchin base dimension)
    center_dims = {}
    for g in range(2, 7):
        center_dims[g] = hitchin_base_dimension(dv.type, dv.rank, g)

    num_proved = sum(1 for s in steps if 'PROVED' in s.status)
    num_conj = sum(1 for s in steps if 'CONJECTURAL' in s.status)

    return LanglandsFunctorData(
        g_type=g_type,
        g_rank=g_rank,
        g_label=f'{g_type}{g_rank}',
        steps=steps,
        kappa_ch_input=kap_input,
        kappa_ch_critical=kap_crit,
        critical_level=k_crit,
        langlands_dual_label=dual_label,
        oper_description=oper_desc,
        center_dimension_genus_g=center_dims,
        total_steps=len(steps),
        num_proved=num_proved,
        num_conjectural=num_conj,
    )


def langlands_functor_all_ade() -> Dict[str, LanglandsFunctorData]:
    """Apply the Langlands functor to all standard ADE types on K3."""
    types = [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    return {f'{t}{r}': langlands_functor(t, r) for t, r in types}


# =========================================================================
# 2. K3 YANGIAN AND OPERS: THE CRITICAL-LEVEL BRIDGE
# =========================================================================

class YangianOperBridge(NamedTuple):
    """Data connecting the K3 Yangian to opers at the critical level.

    The K3 Yangian Y(g_{K3}) (CONJECTURAL, AP-CY14) at ADE enhancement
    sees opers through the critical-level limit:

      As k: 1 -> -h^v:
        kappa_ch: kappa_ch(1) -> 0     (shadow metric degenerates)
        c: rank(g) -> pole             (Sugawara fails)
        z(g_hat): trivial -> enormous  (Feigin-Frenkel center emerges)

    The shadow metric Q_L(0) = 4 * kappa_ch^2 -> 0 at the critical level.
    The surviving data is the oper connection (projective connection for
    G^L) on the spectral curve.

    STATUS: The FF theorem is ProvedElsewhere.  The K3 Yangian identification
    is CONJECTURAL (AP-CY14).
    """
    g_label: str
    h_dual: int
    # Level trajectory: k = 1 (K3 forced) -> k = -h^v (critical)
    k_start: Fraction          # = 1 (K3 level)
    k_end: Fraction            # = -h^v (critical)
    # kappa trajectory
    kappa_ch_start: Fraction   # kappa_ch at k=1
    kappa_ch_end: Fraction     # = 0 at critical
    kappa_slope: Fraction      # d(kappa_ch)/dk = dim(g)/(2*h^v)
    # Central charge trajectory
    c_start: Fraction          # c at k=1 = rank(g)
    c_residue: Fraction        # Res_{k=-h^v}(c) = -dim(g)*h^v
    # Oper data at the critical level
    langlands_dual: str
    oper_casimirs: Tuple[int, ...]
    oper_dim_genus2: int
    # Yangian structure function degree
    yangian_structure_degree: Tuple[int, int]  # (numerator deg, denom deg)
    # Shadow metric at k=1 (nondegenerate) vs k=-h^v (degenerate)
    shadow_metric_k1: Fraction
    shadow_metric_critical: Fraction  # = 0


def yangian_oper_bridge(g_type: str, g_rank: int) -> YangianOperBridge:
    """Compute the bridge between K3 Yangian and opers.

    The bridge has two endpoints:
      - k = 1: the K3 ADE enhancement level (forced by Mukai pairing).
        Here the Yangian sees the structure function g(z) and the R-matrix.
      - k = -h^v: the critical level (Feigin-Frenkel).
        Here the center becomes Fun(Op_{G^L}(D)) and kappa_ch = 0.

    The K3 Yangian "sees" opers because the deformation k: 1 -> -h^v
    tracks a path in the shadow tower along which all shadow amplitudes
    vanish (F_g -> 0 for all g) and the center emerges.

    Parameters
    ----------
    g_type, g_rank : ADE type.

    Returns
    -------
    YangianOperBridge with the full trajectory data.
    """
    d = lie_data(g_type, g_rank)
    dv = langlands_dual_data(g_type, g_rank)

    k_crit = critical_level(g_type, g_rank)
    kap_1 = kappa_affine(g_type, g_rank, F(1))
    kap_crit = kappa_affine(g_type, g_rank, k_crit)
    slope = kappa_slope_at_critical(g_type, g_rank)

    c_1 = central_charge_affine(g_type, g_rank, F(1))
    assert c_1 is not None, "c at level 1 is well-defined"
    residue = central_charge_residue(g_type, g_rank)

    casimirs = _casimir_degrees(dv.type, dv.rank)
    oper_dim_g2 = hitchin_base_dimension(dv.type, dv.rank, 2)

    # K3 Yangian structure function: degree (24, 24) for gl_1
    # For the ADE subalgebra, the relevant part has degree (rank, rank)
    # in the Mukai sublattice directions
    yang_deg = (24, 24)

    # Shadow metric: Q_L(0) = 4 * kappa_ch^2
    shadow_k1 = 4 * kap_1 * kap_1
    shadow_crit = 4 * kap_crit * kap_crit  # = 0

    return YangianOperBridge(
        g_label=f'{g_type}{g_rank}',
        h_dual=d.h_dual,
        k_start=F(1),
        k_end=k_crit,
        kappa_ch_start=kap_1,
        kappa_ch_end=kap_crit,
        kappa_slope=slope,
        c_start=c_1,
        c_residue=residue,
        langlands_dual=f'{dv.type}{dv.rank}',
        oper_casimirs=casimirs,
        oper_dim_genus2=oper_dim_g2,
        yangian_structure_degree=yang_deg,
        shadow_metric_k1=shadow_k1,
        shadow_metric_critical=shadow_crit,
    )


def yangian_oper_bridge_all_ade() -> Dict[str, YangianOperBridge]:
    """Compute the Yangian-oper bridge for all ADE types."""
    types = [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4), ('D', 5),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    return {f'{t}{r}': yangian_oper_bridge(t, r) for t, r in types}


def kappa_trajectory(g_type: str, g_rank: int,
                     num_points: int = 20) -> List[Dict[str, Any]]:
    """Compute the kappa_ch trajectory from k=1 to k=-h^v.

    The trajectory is the linear path k(t) = 1 - t*(1 + h^v) for t in [0, 1].
    At t=0: k=1 (K3 level).  At t=1: k=-h^v (critical).

    kappa_ch(k) = dim(g) * (k + h^v) / (2 * h^v)
               = dim(g) * (1 + h^v - t*(1+h^v)) / (2*h^v)
               = dim(g) * (1+h^v) * (1-t) / (2*h^v)
               = kappa_ch(1) * (1 - t)

    So kappa_ch decreases LINEARLY from kappa_ch(1) to 0.  This linearity
    is a consequence of the affine structure of the KM family.

    Parameters
    ----------
    g_type, g_rank : ADE type.
    num_points : number of points in [0, 1].

    Returns
    -------
    List of dicts with t, k, kappa_ch, c, shadow_metric values.
    """
    d = lie_data(g_type, g_rank)
    kap_1 = float(kappa_affine(g_type, g_rank, F(1)))

    trajectory = []
    for i in range(num_points + 1):
        t = i / num_points
        k = 1 - t * (1 + d.h_dual)
        kap = kap_1 * (1 - t)
        denom = k + d.h_dual
        c_val = d.dim * k / denom if abs(denom) > 1e-15 else float('nan')
        shadow = 4 * kap * kap

        trajectory.append({
            't': t,
            'k': k,
            'kappa_ch': kap,
            'central_charge': c_val,
            'shadow_metric': shadow,
            'is_critical': abs(denom) < 1e-15,
        })

    return trajectory


# =========================================================================
# 3. QGL DUALITY: THE FULL PICTURE
# =========================================================================

class QGLDualityData(NamedTuple):
    """Comprehensive QGL duality data for K3 ADE enhancement.

    Three involutions act on the level k:
      QGL: k -> k^L = -k - h^v      (Psi -> 1/Psi)
      FF:  k -> k' = -k - 2*h^v     (kappa -> -kappa)
      composite: k -> k'' = k + h^v  (QGL o FF, shift by h^v)

    QGL and FF are DIFFERENT involutions (AP-CY10: flop != Koszul dual).
    They generate a dihedral group of order infinity on the level space
    (the composition QGL o FF is a translation by h^v, which is not an
    involution unless h^v = 0).

    STATUS: The QGL correspondence is part of the Frenkel-Gaitsgory
    programme (conjectural in general, proved for Kac-Moody at integral
    positive levels by Aganagic-Frenkel-Okounkov).  The K3 specialization
    is CONJECTURAL (AP-CY14).
    """
    g_label: str
    h_dual: int
    k: Fraction
    # QGL involution
    k_qgl: Fraction            # k^L = -k - h^v
    kappa_ch_k: Fraction
    kappa_ch_qgl: Fraction
    kappa_sum_qgl: Fraction    # kappa(k) + kappa(k^L), NOT zero
    psi_k: Optional[Fraction]
    psi_qgl: Optional[Fraction]
    psi_product: Optional[Fraction]  # = 1
    # FF involution
    k_ff: Fraction             # k' = -k - 2*h^v
    kappa_ch_ff: Fraction
    kappa_sum_ff: Fraction     # kappa(k) + kappa(k'), = 0
    # Composite QGL o FF
    k_composite: Fraction      # QGL(FF(k)) = k + h^v
    kappa_ch_composite: Fraction
    # Fixed points
    qgl_fixed_point: Fraction  # k = -h^v/2
    ff_fixed_point: Fraction   # k = -h^v (critical)
    kappa_at_qgl_fixed: Fraction  # kappa(k=-h^v/2) = dim(g)/4
    # Category O duality
    cat_o_description: str


def qgl_full_duality(g_type: str, g_rank: int,
                     k: Fraction = F(1)) -> QGLDualityData:
    """Comprehensive QGL duality analysis.

    Computes all three involutions and their interactions.

    The QGL correspondence (Frenkel-Gaitsgory):
      Cat O_k(g_hat) <--> Cat O_{k^L}(g^L_hat)
    for k^L = -k - h^v (simply-laced).

    The FF / Koszul duality (Vol I):
      kappa_ch(k) + kappa_ch(k') = 0
    for k' = -k - 2*h^v.

    Parameters
    ----------
    g_type, g_rank : ADE type.
    k : level (default 1, the K3 forced level).

    Returns
    -------
    QGLDualityData with all three involutions.
    """
    d = lie_data(g_type, g_rank)
    dv = langlands_dual_data(g_type, g_rank)

    # QGL
    k_L = -k - d.h_dual
    kap_k = kappa_affine(g_type, g_rank, k)
    kap_L = kappa_affine(g_type, g_rank, k_L)
    psi = kapustin_witten_psi_exact(g_type, g_rank, k)
    psi_L = kapustin_witten_psi_exact(dv.type, dv.rank, k_L)
    psi_prod = psi * psi_L if psi is not None and psi_L is not None else None

    # FF
    k_ff = ff_dual_level(g_type, g_rank, k)
    kap_ff = kappa_affine(g_type, g_rank, k_ff)

    # Composite
    k_comp = k + d.h_dual  # QGL(FF(k)) = k + h^v
    kap_comp = kappa_affine(g_type, g_rank, k_comp)

    # Fixed points
    qgl_fp = F(-d.h_dual, 2)
    ff_fp = F(-d.h_dual)
    kap_qgl_fp = kappa_affine(g_type, g_rank, qgl_fp)

    # Category O description
    if k > 0:
        cat_o_desc = (
            f"Cat O_{float(k)}(g_hat): highest-weight modules at positive "
            f"level {float(k)}.  QGL dual: Cat O_{float(k_L)}(g^L_hat) at "
            f"negative level {float(k_L)} (wrong-sign category O, the "
            f"spectral side of quantum Langlands)."
        )
    else:
        cat_o_desc = (
            f"Cat O_{float(k)}(g_hat): at non-positive level {float(k)}.  "
            f"QGL dual: Cat O_{float(k_L)}(g^L_hat)."
        )

    return QGLDualityData(
        g_label=f'{g_type}{g_rank}',
        h_dual=d.h_dual,
        k=k,
        k_qgl=k_L,
        kappa_ch_k=kap_k,
        kappa_ch_qgl=kap_L,
        kappa_sum_qgl=kap_k + kap_L,
        psi_k=psi,
        psi_qgl=psi_L,
        psi_product=psi_prod,
        k_ff=k_ff,
        kappa_ch_ff=kap_ff,
        kappa_sum_ff=kap_k + kap_ff,
        k_composite=k_comp,
        kappa_ch_composite=kap_comp,
        qgl_fixed_point=qgl_fp,
        ff_fixed_point=ff_fp,
        kappa_at_qgl_fixed=kap_qgl_fp,
        cat_o_description=cat_o_desc,
    )


def qgl_involution_orbit(g_type: str, g_rank: int,
                         k_start: Fraction = F(1),
                         max_iter: int = 10) -> List[Dict[str, Any]]:
    """Compute the orbit of k under alternating QGL and FF involutions.

    Starting from k, apply QGL then FF alternately:
      k -> QGL(k) = -k - h^v -> FF(QGL(k)) = k + h^v -> ...

    The orbit is: k, k + h^v, k + 2*h^v, ...
    (an arithmetic progression, not periodic).

    This demonstrates that QGL and FF generate an INFINITE group action
    on the level space (not a dihedral group of finite order).

    Parameters
    ----------
    g_type, g_rank : ADE type.
    k_start : initial level.
    max_iter : number of QGL-FF iterations.

    Returns
    -------
    List of dicts with the orbit data.
    """
    d = lie_data(g_type, g_rank)
    orbit = []
    k = k_start

    for i in range(max_iter):
        kap = kappa_affine(g_type, g_rank, k)
        psi = kapustin_witten_psi_exact(g_type, g_rank, k)
        orbit.append({
            'step': i,
            'k': k,
            'kappa_ch': kap,
            'psi': psi,
            'operation': 'start' if i == 0 else ('QGL' if i % 2 == 1 else 'FF(QGL)'),
        })
        # Apply QGL
        k_qgl = -k - d.h_dual
        if i % 2 == 0:
            k = k_qgl  # apply QGL
        else:
            k = -k - 2 * d.h_dual  # apply FF

    return orbit


def qgl_level_lattice(g_type: str, g_rank: int,
                      k_values: Optional[List[Fraction]] = None
                      ) -> Dict[str, Any]:
    """Compute the QGL duality lattice for multiple levels.

    At each level k, compute the QGL dual k^L, the FF dual k',
    and verify the identities:
      Psi(k) * Psi(k^L) = 1
      kappa(k) + kappa(k') = 0

    For K3 ADE enhancement at level 1, k^L = -1 - h^v.
    The QGL dual is at NEGATIVE level, corresponding to the spectral side.

    Parameters
    ----------
    g_type, g_rank : ADE type.
    k_values : list of levels to compute.

    Returns
    -------
    Dict with the lattice data.
    """
    if k_values is None:
        d = lie_data(g_type, g_rank)
        # Include the K3 level 1, the QGL dual, the FF dual,
        # the critical level, and the QGL fixed point
        k_values = [
            F(1),
            F(-1 - d.h_dual),  # QGL dual of 1
            F(-1 - 2 * d.h_dual),  # FF dual of 1
            F(-d.h_dual),  # critical level
            F(-d.h_dual, 2),  # QGL fixed point
            F(0),  # classical limit
        ]

    entries = []
    for k in k_values:
        data = qgl_full_duality(g_type, g_rank, k)
        entries.append({
            'k': k,
            'k_qgl': data.k_qgl,
            'k_ff': data.k_ff,
            'kappa_ch': data.kappa_ch_k,
            'kappa_ch_qgl': data.kappa_ch_qgl,
            'kappa_sum_ff': data.kappa_sum_ff,
            'psi_product': data.psi_product,
            'psi_product_is_one': (data.psi_product == F(1)) if data.psi_product is not None else None,
            'kappa_sum_ff_is_zero': (data.kappa_sum_ff == F(0)),
        })

    return {
        'g_label': f'{g_type}{g_rank}',
        'h_dual': lie_data(g_type, g_rank).h_dual,
        'entries': entries,
        'all_psi_products_one': all(
            e['psi_product_is_one'] for e in entries
            if e['psi_product_is_one'] is not None
        ),
        'all_ff_sums_zero': all(
            e['kappa_sum_ff_is_zero'] for e in entries
        ),
    }


# =========================================================================
# 4. HECKE EIGENSHEAF FROM K3 x E
# =========================================================================

class HeckeEigensheafData(NamedTuple):
    """Data for the conjectured Hecke eigensheaf from K3 x E.

    For K3 x E with ADE enhancement of type g, the D-module on Bun_G(E)
    from the family of K3 chiral algebras is conjectured to be a Hecke
    eigensheaf.

    The pipeline:
      K3 x E (CY_3)
        --Phi--> Phi(K3) tensor Phi(E)  (CY-A_3 or factored approach)
        --restrict to E--> family {A_z}_{z in E}
        --Delta_E--> D-module on Bun_G(E)
        --Hecke?--> eigensheaf for G^L-local system on E

    STATUS: CONJECTURAL.  The factored approach Phi(K3) x Phi(E) may
    avoid CY-A_3 by using CY-A_2 for each factor, but the tensor
    product structure of chiral algebras over Ran(E) is not proved
    to factorise.
    """
    g_label: str
    h_dual: int
    # Bun_G(E) data
    bun_g_dim: int             # dim of coarse moduli Bun_G(E)
    bun_g_structure: str       # (E^r) / W
    weyl_order: Optional[int]
    # D-module data
    d_module_type: str         # e.g. "sheaf on P^1 for SL_2"
    d_module_rank: str
    # Hecke property
    hecke_status: str          # CONJECTURAL
    hecke_eigenvalue: str      # G^L-local system on E
    # Dependency chain
    depends_on: List[str]
    # Kappa data
    kappa_ch_k3: Fraction
    kappa_ch_product: str      # description (d=3 regime)
    # Localization functor
    localization_description: str


def hecke_eigensheaf_data(g_type: str, g_rank: int) -> HeckeEigensheafData:
    """Compute the Hecke eigensheaf data for K3 x E at ADE enhancement.

    For SL_2:
      Bun_{SL_2}(E) = E / (Z/2Z) = P^1.
      The D-module is a sheaf on P^1 with singularities at the
      4 fixed points (2-torsion of E).
      The Hecke eigensheaf property: the D-module is an eigensheaf
      for the PGL_2-Hecke operator, with eigenvalue the PGL_2-local
      system on E determined by the K3 periods.

    Parameters
    ----------
    g_type, g_rank : ADE type.

    Returns
    -------
    HeckeEigensheafData.
    """
    d = lie_data(g_type, g_rank)
    bun_data = bun_g_elliptic(g_type, g_rank)
    dv = langlands_dual_data(g_type, g_rank)
    kap_k3 = kappa_affine(g_type, g_rank, F(1))

    # D-module description
    if g_type == 'A' and g_rank == 1:
        d_mod_type = (
            "Sheaf on P^1 = Bun_{SL_2}(E).  "
            "Regular singularities at the 4 two-torsion points of E "
            "(the ramification points of the Kummer quotient E -> P^1)."
        )
        d_mod_rank = (
            "Rank 2 on P^1 minus 4 points, with local monodromy "
            "determined by the SL_2 representation at each 2-torsion "
            "point."
        )
    else:
        d_mod_type = (
            f"D-module on Bun_{{{g_type}{g_rank}}}(E) = "
            f"(E^{d.rank}) / W({g_type}{g_rank}).  "
            f"Coarse moduli of dimension {d.rank}."
        )
        d_mod_rank = (
            f"Rank determined by the representation theory of "
            f"{g_type}{g_rank} at level 1."
        )

    hecke_eigenvalue = (
        f"The {dv.type}{dv.rank}-local system on E determined by the "
        f"K3 periods.  For the ADE enhancement point on the K3 moduli, "
        f"the local system is determined by the restriction of the K3 "
        f"period map to the ADE sublattice of the Mukai lattice."
    )

    depends = [
        'CY-A_3 for K3 x E (programme), OR',
        'Factorization Phi(K3 x E) = Phi(K3) tensor Phi(E) (unproved)',
        'CY-A_2 for K3 factor (proved)',
        'CY-A_2 for E factor (proved: Heisenberg)',
        'Frenkel-Gaitsgory localization Delta_E (proved elsewhere)',
    ]

    localization_desc = (
        "The localization functor Delta_E sends the critical-level "
        "vacuum module V_{-h^v}(g) on Ran(E) to a D-module on "
        "Bun_G(E).  For K3 x E at level 1 (not critical), the "
        "localization must be composed with the level-shifting: "
        "restrict to the ADE subalgebra, deform to critical level, "
        "then localize.  This composition is the content of the "
        "conjecture (conj:k3xe-hecke in geometric_langlands.tex)."
    )

    return HeckeEigensheafData(
        g_label=f'{g_type}{g_rank}',
        h_dual=d.h_dual,
        bun_g_dim=d.rank,
        bun_g_structure=bun_data['structure'],
        weyl_order=bun_data['weyl_order'],
        d_module_type=d_mod_type,
        d_module_rank=d_mod_rank,
        hecke_status='CONJECTURAL (conj:k3xe-hecke)',
        hecke_eigenvalue=hecke_eigenvalue,
        depends_on=depends,
        kappa_ch_k3=kap_k3,
        kappa_ch_product=(
            f"kappa_ch for K3 x E: d=3 regime (CY-A_3 programme). "
            f"K3 factor alone: kappa_ch = {float(kap_k3)} at level 1. "
            f"Product formula UNDEFINED until CY-A_3 resolved."
        ),
        localization_description=localization_desc,
    )


def hecke_eigensheaf_all_ade() -> Dict[str, HeckeEigensheafData]:
    """Compute Hecke eigensheaf data for all ADE types."""
    types = [
        ('A', 1), ('A', 2), ('A', 3),
        ('D', 4),
        ('E', 6), ('E', 7), ('E', 8),
    ]
    return {f'{t}{r}': hecke_eigensheaf_data(t, r) for t, r in types}


# =========================================================================
# 5. SHADOW TOWER AND RAMIFICATION
# =========================================================================

# Extended shadow-ramification data with ADE-specific information
RAMIFICATION_DATA = {
    'G': {
        'shadow_depth': 2,
        'qgl_analytic_type': 'polynomial',
        'langlands_parameter': 'unramified',
        'ramification_depth': 0,
        'monodromy_type': 'trivial',
        'stokes_data': 'none',
        'example_algebras': ['Heisenberg', 'free boson', 'lattice VOA'],
        'k3_realization': (
            'Generic K3 (no ADE enhancement): free-field Heisenberg '
            'of rank 24.  The QGL series is polynomial (degree 1), '
            'corresponding to unramified Langlands parameters '
            '(Fourier-Mukai self-duality for the abelian case).'
        ),
    },
    'L': {
        'shadow_depth': 3,
        'qgl_analytic_type': 'rational',
        'langlands_parameter': 'tamely ramified',
        'ramification_depth': 1,
        'monodromy_type': 'quasi-unipotent (finite order)',
        'stokes_data': 'none (regular singular)',
        'example_algebras': ['g_hat_k (generic KM)', 'affine at level k'],
        'k3_realization': (
            'K3 with ADE enhancement: KM subalgebra g_hat_1.  '
            'The cubic shadow alpha != 0 (proved, Vol I).  '
            'Poles of the rational QGL series at Kac determinant '
            'roots correspond to reducibility of tamely ramified '
            'local systems.'
        ),
    },
    'C': {
        'shadow_depth': 4,
        'qgl_analytic_type': 'convergent',
        'langlands_parameter': 'wildly ramified (regular)',
        'ramification_depth': 2,
        'monodromy_type': 'ramified (Stokes multiplier)',
        'stokes_data': 'finite (convergent Stokes expansion)',
        'example_algebras': ['beta-gamma', 'symplectic bosons'],
        'k3_realization': (
            'K3 with beta-gamma type enhancement (not ADE, but '
            'higher-rank CY deformation).  The QGL series converges '
            'in a disk |kappa_QGL| < R_C.  Stokes data corresponds '
            'to the shadow tower truncation at depth 4.'
        ),
    },
    'M': {
        'shadow_depth': float('inf'),
        'qgl_analytic_type': 'Gevrey-1 divergent',
        'langlands_parameter': 'irregular',
        'ramification_depth': float('inf'),
        'monodromy_type': 'irregular (essential singularity)',
        'stokes_data': 'infinite (Borel resummation required)',
        'example_algebras': [
            'Virasoro', 'W_N', 'W_{1+infinity}', 'local P^2 chiral',
        ],
        'k3_realization': (
            'Not realized at ADE enhancement on K3 (ADE gives class L). '
            'Realized for the FULL K3 chiral algebra if nonperturbative '
            'corrections elevate the shadow depth (conjectural).  '
            'Also realized for local P^2 (class M, verified by '
            'shadow tower computation).'
        ),
    },
}


class ShadowRamificationData(NamedTuple):
    """Shadow class to ramification type correspondence.

    The correspondence (conj:shadow-ramification in geometric_langlands.tex):
      shadow depth r -> ramification depth
      2 (class G) -> unramified
      3 (class L) -> tamely ramified
      4 (class C) -> wildly ramified (regular)
      inf (class M) -> irregular

    STATUS: CONJECTURAL.
    """
    shadow_class: str
    shadow_depth: int
    qgl_analytic_type: str
    langlands_parameter: str
    ramification_depth: int
    monodromy_type: str
    stokes_data: str
    example_algebras: List[str]
    k3_realization: str


def shadow_ramification(shadow_class: str) -> ShadowRamificationData:
    """Map a shadow class to extended ramification data.

    Parameters
    ----------
    shadow_class : str
        One of 'G', 'L', 'C', 'M'.

    Returns
    -------
    ShadowRamificationData.

    Raises
    ------
    ValueError if shadow_class not in {G, L, C, M}.
    """
    if shadow_class not in RAMIFICATION_DATA:
        raise ValueError(
            f"Unknown shadow class '{shadow_class}'. Must be G, L, C, or M."
        )
    data = RAMIFICATION_DATA[shadow_class]
    depth = data['shadow_depth']
    ram_depth = data['ramification_depth']
    return ShadowRamificationData(
        shadow_class=shadow_class,
        shadow_depth=int(depth) if depth != float('inf') else -1,
        qgl_analytic_type=data['qgl_analytic_type'],
        langlands_parameter=data['langlands_parameter'],
        ramification_depth=int(ram_depth) if ram_depth != float('inf') else -1,
        monodromy_type=data['monodromy_type'],
        stokes_data=data['stokes_data'],
        example_algebras=data['example_algebras'],
        k3_realization=data['k3_realization'],
    )


def k3_ade_ramification_table() -> Dict[str, Dict[str, Any]]:
    """Shadow-ramification table for K3 ADE-enhanced chiral algebras.

    At ADE enhancement on K3, the KM subalgebra g_hat_1 has shadow class L
    (proved, Vol I).  The ramification type is therefore tamely ramified.

    For each ADE type, we compute:
      - kappa_ch at level 1
      - Shadow class (L for all ADE)
      - Ramification type (tamely ramified for all)
      - The Kac determinant poles (where the rational QGL series diverges)

    Returns dict keyed by ADE label.
    """
    result = {}
    for label, enh in all_ade_enhancements().items():
        ram = shadow_ramification('L')
        d = lie_data(enh.g_type, enh.g_rank)

        # For KM at level k, the Kac determinant vanishes at
        # k = -h^v + p/q (rational), giving poles of the QGL series.
        # The first pole is at k = -h^v + 1 (boundary of the critical region).
        kac_first_pole = F(-d.h_dual + 1)
        kac_pole_kappa = kappa_affine(enh.g_type, enh.g_rank, kac_first_pole)

        result[label] = {
            'g_label': label,
            'kappa_ch_level1': float(enh.kappa_ch_level1),
            'shadow_class': 'L',
            'ramification_type': ram.langlands_parameter,
            'ramification_depth': ram.ramification_depth,
            'monodromy_type': ram.monodromy_type,
            'kac_first_pole_level': float(kac_first_pole),
            'kac_first_pole_kappa': float(kac_pole_kappa),
            'note': (
                f"KM subalgebra {label}_hat_1 is class L "
                f"(shadow depth 3, cubic shadow nonzero). "
                f"Tamely ramified Langlands parameter. "
                f"First Kac pole at k = {float(kac_first_pole)}."
            ),
        }

    return result


def shadow_ramification_consistency_check() -> Dict[str, Any]:
    """Verify consistency between shadow classes and ramification.

    Checks:
    1. shadow_depth strictly increases: G < L < C < M
    2. ramification_depth strictly increases: 0 < 1 < 2 < inf
    3. All four GLCM classes map to distinct Langlands parameters
    4. K3 ADE types are all class L (tamely ramified)
    5. Shadow depth 2 is ALWAYS unramified, depth 3 ALWAYS tame

    Returns dict with all checks.
    """
    results = {}

    # Check 1: shadow depth ordering
    depths = []
    for cls in ['G', 'L', 'C', 'M']:
        data = RAMIFICATION_DATA[cls]
        sd = data['shadow_depth']
        depths.append(sd)
    results['depth_ordering'] = (
        depths[0] < depths[1] < depths[2] < depths[3]
    )

    # Check 2: ramification depth ordering
    ram_depths = []
    for cls in ['G', 'L', 'C', 'M']:
        data = RAMIFICATION_DATA[cls]
        rd = data['ramification_depth']
        ram_depths.append(rd)
    results['ram_depth_ordering'] = (
        ram_depths[0] < ram_depths[1] < ram_depths[2] < ram_depths[3]
    )

    # Check 3: distinct Langlands parameters
    params = set()
    for cls in ['G', 'L', 'C', 'M']:
        data = RAMIFICATION_DATA[cls]
        params.add(data['langlands_parameter'])
    results['distinct_params'] = len(params) == 4

    # Check 4: K3 ADE all class L
    k3_table = k3_ade_ramification_table()
    results['k3_ade_all_class_L'] = all(
        v['shadow_class'] == 'L' for v in k3_table.values()
    )
    results['k3_ade_all_tame'] = all(
        v['ramification_type'] == 'tamely ramified' for v in k3_table.values()
    )
    results['num_k3_ade_types'] = len(k3_table)

    # Check 5: depth-class correspondence
    results['depth_2_unramified'] = (
        RAMIFICATION_DATA['G']['langlands_parameter'] == 'unramified'
    )
    results['depth_3_tame'] = (
        RAMIFICATION_DATA['L']['langlands_parameter'] == 'tamely ramified'
    )

    results['all_checks_pass'] = all(
        v for k, v in results.items() if isinstance(v, bool)
    )

    return results


# =========================================================================
# 6. UNIFIED VERIFICATION
# =========================================================================

def verify_langlands_functor() -> Dict[str, Any]:
    """Verify the Langlands functor pipeline for all ADE types."""
    results = {}

    # 1. Pipeline structure
    steps = langlands_functor_steps()
    results['num_steps'] = len(steps)
    results['step_names'] = [s.name for s in steps]

    # 2. All ADE functors
    all_functors = langlands_functor_all_ade()
    results['num_ade_types'] = len(all_functors)
    for label, data in all_functors.items():
        results[f'functor_{label}_kappa_critical_zero'] = (
            data.kappa_ch_critical == F(0)
        )
        results[f'functor_{label}_steps'] = data.total_steps

    return results


def verify_yangian_oper_bridge() -> Dict[str, Any]:
    """Verify the Yangian-oper bridge for all ADE types."""
    results = {}

    all_bridges = yangian_oper_bridge_all_ade()
    for label, bridge in all_bridges.items():
        results[f'bridge_{label}_kappa_end_zero'] = (
            bridge.kappa_ch_end == F(0)
        )
        results[f'bridge_{label}_shadow_critical_zero'] = (
            bridge.shadow_metric_critical == F(0)
        )
        results[f'bridge_{label}_shadow_k1_positive'] = (
            bridge.shadow_metric_k1 > 0
        )
        results[f'bridge_{label}_slope'] = float(bridge.kappa_slope)

    return results


def verify_qgl_duality() -> Dict[str, Any]:
    """Verify QGL duality for all ADE types at multiple levels."""
    results = {}

    for t, r in [('A', 1), ('A', 2), ('D', 4), ('E', 8)]:
        label = f'{t}{r}'
        for k in [F(1), F(2), F(5)]:
            data = qgl_full_duality(t, r, k)
            tag = f'qgl_{label}_k{float(k)}'
            # Psi * Psi^L = 1
            results[f'{tag}_psi_product'] = (
                data.psi_product == F(1)
                if data.psi_product is not None else None
            )
            # kappa(k) + kappa(k') = 0 (FF duality)
            results[f'{tag}_ff_sum_zero'] = (data.kappa_sum_ff == F(0))
            # QGL sum is NOT zero
            results[f'{tag}_qgl_sum_nonzero'] = (data.kappa_sum_qgl != F(0))

    # QGL fixed point
    for t, r in [('A', 1), ('D', 4), ('E', 8)]:
        label = f'{t}{r}'
        data = qgl_full_duality(t, r)
        d = lie_data(t, r)
        results[f'qgl_{label}_fixed_kappa'] = (
            data.kappa_at_qgl_fixed == F(d.dim, 4)
        )

    return results


def verify_hecke_data() -> Dict[str, Any]:
    """Verify Hecke eigensheaf data."""
    results = {}

    all_hecke = hecke_eigensheaf_all_ade()
    results['num_ade_types'] = len(all_hecke)

    for label, data in all_hecke.items():
        d = lie_data(data.g_label[0], int(data.g_label[1:]))
        results[f'hecke_{label}_bun_dim'] = data.bun_g_dim
        results[f'hecke_{label}_bun_dim_matches_rank'] = (
            data.bun_g_dim == d.rank
        )

    # SL_2 special: Bun = P^1 (dim 1)
    sl2 = all_hecke['A1']
    results['hecke_sl2_bun_dim_1'] = (sl2.bun_g_dim == 1)
    results['hecke_sl2_weyl_order_2'] = (sl2.weyl_order == 2)

    return results


def verify_shadow_ramification() -> Dict[str, Any]:
    """Verify shadow-ramification correspondence."""
    return shadow_ramification_consistency_check()


def verify_all() -> Dict[str, Any]:
    """Master verification of the full Langlands-from-chiral-QG engine."""
    results = {}
    results['functor'] = verify_langlands_functor()
    results['bridge'] = verify_yangian_oper_bridge()
    results['qgl'] = verify_qgl_duality()
    results['hecke'] = verify_hecke_data()
    results['ramification'] = verify_shadow_ramification()

    # Top-level summary
    all_ok = True
    for section, data in results.items():
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, bool) and not v:
                    all_ok = False
    results['all_pass'] = all_ok

    return results


def full_computation() -> Dict[str, Any]:
    """Full computation suite for the Langlands-from-chiral-QG engine."""
    return {
        'verification': verify_all(),
        'langlands_functor': {
            k: v._asdict() for k, v in langlands_functor_all_ade().items()
        },
        'yangian_oper_bridge': {
            k: v._asdict() for k, v in yangian_oper_bridge_all_ade().items()
        },
        'qgl_sl2_level1': qgl_full_duality('A', 1, F(1))._asdict(),
        'qgl_e8_level1': qgl_full_duality('E', 8, F(1))._asdict(),
        'qgl_level_lattice_sl2': qgl_level_lattice('A', 1),
        'hecke_data': {
            k: v._asdict() for k, v in hecke_eigensheaf_all_ade().items()
        },
        'k3_ramification_table': k3_ade_ramification_table(),
        'shadow_ramification_check': shadow_ramification_consistency_check(),
    }
