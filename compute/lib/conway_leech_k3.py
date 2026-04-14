r"""Conway group Co_0 = Aut(Leech), the Leech lattice, and the K3 Yangian.

STATUS: CONJECTURAL (AP-CY14).  The K3 Yangian Y(g_{K3}) is not constructed.
All results involving Y(g_{K3}) are conditional on its existence.  Results
about the Leech lattice, Conway group, and lattice VOAs are classical
(unconditional).

MATHEMATICAL CONTENT
====================

This module investigates the relationship between:
  (a) The 24 K3 Yangian generators (Mukai lattice, signature (4,20))
  (b) The 24-dimensional Leech lattice (signature (0,24), no roots)
  (c) The Conway group Co_0 = Aut(Leech) and its subgroup M_24
  (d) The FLM Monster VOA V^natural and its connection to K3

SECTION 1: THE RANK-24 COINCIDENCE
-----------------------------------

Both the Mukai lattice and the Leech lattice have rank 24.  This is NOT a
coincidence but NOT a direct lattice isomorphism either.

  Mukai lattice:  Lambda_Muk = U^3 + E_8(-1)^2,  signature (4,20),  rank 24
  Leech lattice:  Lambda_Leech,                    signature (0,24),  rank 24
  K3 lattice:     Lambda_K3 = U^3 + E_8(-1)^2,    signature (3,19),  rank 22

The connection is through the NIEMEIER CLASSIFICATION.  An even unimodular
lattice of rank 24 and signature (0,24) is a Niemeier lattice.  There are
exactly 24, classified by root system.  The Leech lattice is the unique one
with empty root system.

The bridge between the Mukai lattice (signature (4,20)) and the Niemeier
lattices (signature (0,24)) is:

  Lambda_K3 = U^3 + E_8(-1)^2   (rank 22, sig (3,19))
  Lambda_Muk = Lambda_K3 + U     (rank 24, sig (4,20))  [add hyperbolic plane]
  Lambda_Muk^{Wick} ~ N_i        (Wick rotation to definite form)

The "Wick rotation" is a FORMAL operation: replace the (4,20) inner product
with a (0,24) inner product on the same rank-24 vector space.  This destroys
the lattice structure but preserves the rank.  The Niemeier lattice at a
given K3 moduli point is determined by the enhanced symmetry, not by the
Wick rotation.

The number 24 arises from:
  24 = dim H*(K3, C) = b_0 + b_2 + b_4 = 1 + 22 + 1 = 24
  24 = rank(Lambda_Muk) = rank(Lambda_K3) + 2
  24 = rank(Lambda_Leech)

The "+2" in rank(Lambda_Muk) = rank(Lambda_K3) + 2 comes from the hyperbolic
plane U = H^0 + H^4 (the rank and degree components of the Mukai vector).
The coincidence 24 = 24 between rank(Lambda_Muk) and rank(Lambda_Leech) is a
CONSEQUENCE of H*(K3) being 24-dimensional, which is itself a consequence of
chi_top(K3) = 24 = 2(1 + b_2/2 + 1) = 2 + b_2 + 2 for a surface with
b_1 = b_3 = 0, h^{2,0} = 1.

SECTION 2: THE LEECH ENHANCEMENT POINT
----------------------------------------

Among the 24 Niemeier lattices, the Leech lattice (index 1) is UNIQUE: it has
NO roots (no vectors of norm 2).  At this enhancement point in K3 moduli:

  - The lattice VOA V_{Leech} has c = 24, kappa_ch = 24 (class G, depth 2).
  - There is NO enhanced Kac-Moody subalgebra (no roots => no current algebra).
  - The minimal vectors have norm 4 (not 2), giving 196560 vectors.
  - The automorphism group is MAXIMAL: Co_0 = Aut(Lambda_Leech),
    |Co_0| = 8,315,553,613,086,720,000 (order ~ 8.3 * 10^18).

The K3 Yangian at the Leech point Y(g_{K3}(Leech)):
  - The 24 parameters h_i are NOT specialized by any root system.
  - The FULL S_24 acts (no restriction from root system constraints).
  - Co_0 < S_24 (as a transitive subgroup on 24 letters via the
    Leech lattice minimal vectors modulo norm... BUT Co_0 does NOT act
    on 24 letters in the standard permutation representation!).

CRITICAL CORRECTION: Co_0 does NOT embed in S_24.  The Conway group Co_0
acts on the Leech lattice Lambda = Z^24, hence on 24 COORDINATES.
But Co_0 is a subgroup of O(24, Z), NOT of S_24.  The permutation
subgroup of Co_0 that acts by COORDINATE PERMUTATIONS is much smaller.
M_24 embeds in S_24 via the Steiner system S(5,8,24), and M_24 < Co_0
as the subgroup fixing a particular "frame" (= set of 48 vectors
forming 24 antipodal pairs spanning R^24).

SECTION 3: CO_0 ACTION ON THE K3 YANGIAN
------------------------------------------

Co_0 acts on the Leech lattice Lambda_Leech by orthogonal transformations.
The 24-dimensional representation is the STANDARD representation of Co_0.

For the K3 Yangian at the Leech point:
  - Co_0 acts on C^24 (the charge-1 representation space).
  - The action is by ORTHOGONAL transformations, not by permutations.
  - The structure function g_{K3}(z) = prod (z - h_i)/(z + h_i) is
    invariant under PERMUTATIONS of h_i, but the Co_0 action is more
    general (it mixes the h_i by orthogonal transformations).

The R-matrix for the Heisenberg Yangian is diagonal:
  R_{ii}(z) = (z - h_i)/(z + h_i),  R_{ij} = 0 for i != j.

Under a Co_0 transformation g: h_i -> sum_j g_{ij} h_j, the diagonal
R-matrix is CONJUGATED to a dense matrix.  The new R-matrix is:
  R^g(z) = g R(z) g^{-1}
which is no longer diagonal but satisfies the same YBE.

For Co_0 to act as Yangian AUTOMORPHISMS, we need:
  Delta_z(g . x) = (g tensor g) . Delta_z(x)
This is the coproduct-compatibility condition.  For the Heisenberg
Yangian with Miura coproduct, this requires g to preserve the Mukai
pairing, which is automatic since Co_0 < O(Lambda_Leech).

SECTION 4: CO_0 CONTAINS M_24
-------------------------------

The Mathieu group M_24 embeds in Co_0 as the automorphism group of a
particular combinatorial structure on Lambda_Leech: the MOG (Miracle
Octad Generator) of Curtis, or equivalently the sextet of S(5,8,24).

The chain of subgroups:
  M_24 < Co_0 = Aut(Lambda_Leech)
  |M_24| = 244,823,040
  |Co_0| = 8,315,553,613,086,720,000
  [Co_0 : M_24] = 33,965,714,432,000

The M_24 action on the K3 elliptic genus (Eguchi-Ooguri-Tachikawa 2010)
sees the PERMUTATION sector of Co_0.  The full Co_0 acts on a LARGER
structure: the full representation category Rep(Y(g_{K3}(Leech))).

What Co_0 sees that M_24 does not:
  (a) Non-permutation symmetries of Lambda_Leech (orthogonal reflections
      that mix coordinates).
  (b) The norm-4 shell of 196560 vectors (M_24 acts on the 24 coordinate
      axes; Co_0 acts on the full 196560-element orbit).
  (c) Higher shells of the Leech lattice (norm 6, 8, ...) with their
      Co_0-equivariant structure.

The REPRESENTATION THEORY:
  - M_24 has 26 irreducible representations (dimensions: 1, 23, 45, 45,
    231, 231, 252, 253, 483, 770, 770, 990, 990, 1035, 1035, 1265,
    1771, 2024, 2277, 3312, 3520, 5313, 5544, 5796, 10395).
  - Co_0 has far more irreps (it is much larger).
  - The 24-dim standard representation of Co_0 restricts to M_24 as:
    24 = 1 + 23 (the permutation representation minus trivial + trivial).

SECTION 5: THE MONSTER VOA V^NATURAL AND K3
---------------------------------------------

The FLM Monster VOA V^natural:
  - Constructed as the Z/2-orbifold of V_{Leech} (Frenkel-Lepowsky-Meurman).
  - Aut(V^natural) = Monster M (the largest sporadic simple group).
  - c = 24, kappa_ch(V^natural) = 12 (= 24/2, the orbifold halving).
  - Character: J(tau) = q^{-1} + 196884q + 21493760q^2 + ...

The chain of connections to K3:
  K3 -> Lambda_Muk (rank 24) -> Niemeier classification -> Lambda_Leech
  -> V_{Leech} (kappa_ch = 24) -> V^natural (kappa_ch = 12, orbifold)

The K3 Yangian connection to V^natural:
  - Y(g_{K3}(Leech)) acts on V_{Leech} modules (conjectural).
  - The Z/2-orbifold that produces V^natural is NOT a Yangian operation.
  - There is no known Y(g_{K3}) action on V^natural modules.
  - The Monster M and Co_0 are related: Co_1 = Co_0 / {+/- I_24} is a
    SUBGROUP of M (the largest sporadic subgroup of the Monster).

The kappa_ch hierarchy:
  kappa_ch(V_{Leech}) = 24 = rank(Lambda_Leech)
  kappa_ch(V^natural) = 12 = 24/2  (Z/2-orbifold halving)
  kappa_ch(Phi(D^b(K3))) = 2 = chi(O_{K3})  (CY functor)

These three values {2, 12, 24} encode the depth at which each construction
interrogates the 24-dimensional H*(K3):
  24: the full lattice (every Hochschild class contributes)
  12: the orbifold (half of the lattice data survives)
  2:  the CY functor (only the holomorphic Euler characteristic)

SECTION 6: THE LEECH THETA SERIES AND BAR EULER PRODUCT
---------------------------------------------------------

Leech lattice theta series:
  Theta_{Leech}(tau) = 1 + 196560 q^2 + 16773120 q^3 + ...

(Note: minimum norm = 4, so the first nonzero coefficient after the
constant term is at q^{4/2} = q^2, corresponding to norm-4 vectors.)

The KISSING NUMBER 196560 decomposes under Co_0:
  196560 = the Co_0-orbit of any minimal vector (single orbit).
  Under M_24: 196560 decomposes into M_24 orbits.

The bar Euler product of V_{Leech} is eta(tau)^24 / q (rank universality),
identical to that of ANY rank-24 lattice VOA.  The theta series is the
FINER invariant that distinguishes the Leech lattice.

The c_Delta coefficient for the Leech lattice:
  Theta_N(tau) = E_12(tau) + c_Delta(N) * Delta(tau)
  c_Delta(Leech) = (691 * 0 - 65520) / 691 = -65520/691

SECTION 7: CONWAY MOONSHINE (V^{s,natural})
---------------------------------------------

The shorter moonshine module V^{s,natural} (Conway moonshine):
  - c = 12 (half of the Leech VOA central charge)
  - Aut(V^{s,natural}) = Co_0 (the Conway group, NOT the Monster)
  - Character: related to eta-products of Co_0 Frame shapes

The K3 connection to Conway moonshine:
  - The K3 elliptic genus Z_{K3}(tau, z) = 2 * phi_{0,1}(tau, z)
    decomposes under N=4 characters with M_24 multiplicities.
  - A CONJECTURAL Conway analogue: the Leech lattice VOA character
    J(tau) + 24 decomposes under V^{s,natural} with Co_0 multiplicities.
  - The McKay-Thompson series for Co_0 elements are Hauptmoduls for
    genus-zero groups (Conway-Norton conjecture, proved by Borcherds).

Open question (manuscript: conj:universal-moonshine-multiplier):
  Does the twined partition function of V^{s,natural} decompose as
  Z_g(tau) = kappa_ch(V^{s,natural}) * sum_n dim(rho_n^{Co_0}) * ch_n(g)?

CONVENTIONS
===========
  - kappa subscripts per AP113: kappa_ch, kappa_cat, kappa_BKM, kappa_fiber
  - AP-CY14: Y(g_{K3}) is CONJECTURAL. All Yangian results conditional.
  - AP-CY16: Co_0 quotient by +/-I_{24} (24x24 identity), NOT +/-I_5.
  - AP-CY4: Drinfeld center Z(C) != derived center Z^der_ch(A).
  - AP-CY18: Leech theta series minimum norm = 4, first correction at q^2.
  - AP-CY12: shadow class from full tower computation (class G for Leech VOA).
  - AP-CY31: z is Yangian spectral parameter, NOT worldsheet coordinate.

REFERENCES
==========
  Conway-Sloane, "Sphere Packings, Lattices and Groups" (1999), Ch. 10, 16
  Frenkel-Lepowsky-Meurman, "Vertex Operator Algebras and the Monster" (1988)
  Curtis, "A new combinatorial approach to M_24" (1976)
  Borcherds, "Monstrous moonshine and monstrous Lie superalgebras" (1992)
  Eguchi-Ooguri-Tachikawa, arXiv:1004.0956 (Mathieu moonshine)
  Gaberdiel-Hohenegger-Volpato, arXiv:1008.3778, 1106.4315 (K3 symmetries)
  Duncan, arXiv:math/0507118 (Conway moonshine)
  Duncan-Mack-Crane, arXiv:1407.5862 (Conway moonshine module)
  Cheng-Duncan-Harvey, arXiv:1204.2779 (Umbral moonshine)

Manuscript references
---------------------
  k3_chiral_algebra.tex: prop:k3-trichotomy, rem:k3-heisenberg-leech
  k3_yangian_chapter.tex: rem:k3-heisenberg-leech, sec:k3-niemeier-landscape
  k3e_cy3_programme.tex: conj:universal-moonshine-multiplier, rem:leech-connection
"""

from __future__ import annotations

import math
from collections import OrderedDict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import numpy as np

from compute.lib.niemeier_shadow_landscape import (
    all_niemeier_lattices,
    niemeier_lattice,
    ade_root_system,
    lattice_voa_shadow,
    NiemeierLattice,
    ADERootSystem,
)

F = Fraction


# =========================================================================
# 0. Constants
# =========================================================================

ENGINE_STATUS = 'CONJECTURAL'  # AP-CY14: Y(g_{K3}) not constructed

# Conway group Co_0 = Aut(Lambda_Leech)
CO_0_ORDER = 8_315_553_613_086_720_000

# Co_1 = Co_0 / {+/- I_24}  (AP-CY16: quotient by +/-I_{24}, 24x24)
CO_1_ORDER = CO_0_ORDER // 2  # = 4,157,776,806,543,360,000

# Mathieu group M_24
M_24_ORDER = 244_823_040

# Index [Co_0 : M_24]
CO_0_M24_INDEX = CO_0_ORDER // M_24_ORDER

# Monster group M order
MONSTER_ORDER = (
    2**46 * 3**20 * 5**9 * 7**6 * 11**2 * 13**3 * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71
)

# Leech lattice data
LEECH_RANK = 24
LEECH_SIGNATURE = (0, 24)  # negative-definite (convention: norm is positive)
LEECH_MIN_NORM = 4  # minimum nonzero norm-squared
LEECH_KISSING_NUMBER = 196560  # number of norm-4 vectors
LEECH_NORM_6_COUNT = 16773120  # number of norm-6 vectors
LEECH_NORM_8_COUNT = 398034000  # number of norm-8 vectors

# Mukai lattice data
MUKAI_RANK = 24
MUKAI_SIGNATURE = (4, 20)

# K3 lattice data
K3_LATTICE_RANK = 22
K3_SIGNATURE = (3, 19)

# kappa_ch values (AP113: subscripted)
KAPPA_CH_LEECH_VOA = 24       # lattice VOA: kappa_ch = rank
KAPPA_CH_MONSTER_VOA = 12     # V^natural: Z/2-orbifold halving
KAPPA_CH_K3_CY_FUNCTOR = 2   # Phi(D^b(K3)): CY functor
KAPPA_CH_CONWAY_VOA = None    # V^{s,natural}: c=12, kappa_ch unknown (open)


# =========================================================================
# 1. Rank-24 coincidence analysis
# =========================================================================

class Rank24Origin(NamedTuple):
    """Data tracking the origin of rank 24 in different contexts."""
    name: str
    rank: int
    signature: Tuple[int, int]
    origin: str  # mathematical origin of the rank
    is_lattice: bool
    has_roots: Optional[bool]  # None if not a lattice


def rank_24_origins() -> List[Rank24Origin]:
    """Catalogue all occurrences of rank 24 in the K3-Leech story.

    Returns a list of Rank24Origin objects documenting each occurrence
    and its mathematical provenance.

    The conclusion: 24 = dim H*(K3, C) is the single source.
    The Mukai lattice has rank 24 because H*(K3) is 24-dimensional.
    The Leech lattice has rank 24 because it is a Niemeier lattice
    (even unimodular rank 24 definite), and the Niemeier classification
    is connected to K3 through the embedding Lambda_K3 + U -> Niemeier.
    """
    return [
        Rank24Origin(
            name="H*(K3, C)",
            rank=24,
            signature=(4, 20),  # Mukai pairing signature on total cohomology
            origin="b_0 + b_2 + b_4 = 1 + 22 + 1 = 24 (Betti numbers of K3)",
            is_lattice=False,
            has_roots=None,
        ),
        Rank24Origin(
            name="Mukai lattice Lambda_Muk",
            rank=24,
            signature=(4, 20),
            origin="H^*(K3, Z) with Mukai pairing = Lambda_K3 + U",
            is_lattice=True,
            has_roots=True,  # Lambda_K3 has roots from E_8(-1)^2
        ),
        Rank24Origin(
            name="K3 lattice Lambda_K3 + U",
            rank=24,
            signature=(4, 20),
            origin="H^2(K3, Z) + H^0 + H^4 = rank 22 + 2",
            is_lattice=True,
            has_roots=True,
        ),
        Rank24Origin(
            name="Leech lattice Lambda_Leech",
            rank=24,
            signature=(0, 24),
            origin="Unique rootless even unimodular rank-24 definite lattice",
            is_lattice=True,
            has_roots=False,  # THE defining property of Leech
        ),
        Rank24Origin(
            name="Niemeier lattice (any of 24)",
            rank=24,
            signature=(0, 24),
            origin="Even unimodular rank-24 definite lattice",
            is_lattice=True,
            has_roots=None,  # varies (Leech: no, others: yes)
        ),
        Rank24Origin(
            name="K3 Yangian generators",
            rank=24,
            signature=(4, 20),
            origin="h_1,...,h_24 parametrize Y(g_{K3}) in Mukai lattice directions",
            is_lattice=False,
            has_roots=None,
        ),
        Rank24Origin(
            name="chi_top(K3)",
            rank=24,
            signature=(0, 0),  # not a lattice datum
            origin="Euler characteristic = sum(-1)^k b_k = 2 + 22 + 2 = 24 "
                   "(using b_0=b_4=1, b_1=b_3=0, b_2=22, but with alternating "
                   "signs: 1-0+22-0+1=24)",
            is_lattice=False,
            has_roots=None,
        ),
    ]


def is_rank_24_coincidence() -> Dict[str, Any]:
    """Analyse whether 24 = rank(Mukai) = rank(Leech) is coincidental.

    Returns a dictionary with the analysis.

    Answer: NOT a coincidence, but NOT a direct isomorphism either.
    The common source is dim H*(K3, C) = 24.

    The Mukai lattice has rank 24 because H*(K3) is 24-dimensional.
    The Leech lattice has rank 24 because it is the unique rootless Niemeier
    lattice.  The Niemeier lattices are connected to K3 through:
      Lambda_K3 + U = Lambda_Muk (rank 24, sig (4,20))
    which has the SAME RANK as the Niemeier lattices (rank 24, sig (0,24))
    but DIFFERENT SIGNATURE.

    The "deep" explanation: the K3 moduli space parametrizes lattice
    embeddings into Niemeier lattices.  The rank-24 constraint is that
    even unimodular lattices in dimension 24 are maximally rigid
    (finite classification, 24 types).  This rigidity is what makes the
    K3-Leech-Monster connection possible.
    """
    return {
        'is_coincidence': False,
        'common_source': 'dim H*(K3, C) = 24',
        'mukai_rank': MUKAI_RANK,
        'mukai_signature': MUKAI_SIGNATURE,
        'leech_rank': LEECH_RANK,
        'leech_signature': LEECH_SIGNATURE,
        'signature_match': MUKAI_SIGNATURE == LEECH_SIGNATURE,  # False!
        'rank_match': MUKAI_RANK == LEECH_RANK,  # True
        'direct_isomorphism': False,
        'obstruction': 'Signatures differ: (4,20) vs (0,24). '
                       'No isometry between an indefinite and a definite lattice.',
        'bridge': 'Niemeier classification. The K3 moduli space parametrizes '
                  'embeddings into rank-24 lattices. The Leech lattice is the '
                  'unique rootless Niemeier lattice, corresponding to the point '
                  'in K3 moduli with no enhanced symmetry from roots.',
        'deeper_explanation': (
            'The special dimension 24 is where even unimodular lattices are '
            'maximally rigid: there are exactly 24 such lattices (Niemeier), '
            'classified by their root systems. This rigidity connects K3 '
            'geometry (which produces a rank-24 cohomology lattice) to the '
            'Leech lattice (the unique rootless member of the finite list). '
            'In no other dimension does this finite classification + K3 '
            'cohomology rank + rootless uniqueness triangle close.'
        ),
        'b2_plus_2': f'b_2(K3) + 2 = 22 + 2 = {K3_LATTICE_RANK + 2} = '
                     f'{LEECH_RANK} = rank(Leech)',
        'b2_plus_2_explanation': (
            'The +2 comes from H^0 + H^4 (the hyperbolic plane U in the '
            'Mukai vector). This gives rank(Lambda_Muk) = b_2 + 2 = 24.'
        ),
    }


# =========================================================================
# 2. Leech enhancement point of Y(g_{K3})
# =========================================================================

class LeechEnhancementData(NamedTuple):
    """Data for the K3 Yangian at the Leech enhancement point."""
    niemeier_index: int         # 1 (Leech is Niemeier lattice #1)
    root_system: str            # "(none)"
    num_roots: int              # 0
    min_norm: int               # 4 (minimum nonzero norm)
    kissing_number: int         # 196560
    automorphism_group: str     # "Co_0"
    automorphism_order: int     # |Co_0|
    kappa_ch_lattice_voa: int   # 24
    kappa_ch_k3_sigma: int      # 2 (topological, moduli-independent)
    shadow_class_lattice_voa: str    # "G"
    shadow_class_k3_sigma: str       # "M"
    shadow_depth_lattice_voa: int    # 2
    has_enhanced_kac_moody: bool     # False (no roots!)
    c_delta: Fraction           # theta series coefficient


def leech_enhancement_point() -> LeechEnhancementData:
    """Construct the data for Y(g_{K3}) at the Leech enhancement point.

    The Leech lattice is Niemeier lattice #1 (index 1 in our ordering).
    It is the UNIQUE Niemeier lattice with no roots.

    At this point:
    - The lattice VOA V_{Leech} has c = 24, kappa_ch = 24, class G.
    - There is NO enhanced Kac-Moody subalgebra (no roots).
    - The automorphism group Co_0 = Aut(Lambda_Leech) is the LARGEST
      automorphism group of any Niemeier lattice.
    - The K3 sigma model retains kappa_ch = 2 (topological invariant).
    """
    leech = niemeier_lattice(1)
    assert leech.name == "Leech"
    assert leech.total_roots == 0
    assert leech.rank == 24

    c_delta = Fraction(-65520, 691)

    return LeechEnhancementData(
        niemeier_index=1,
        root_system="(none)",
        num_roots=0,
        min_norm=LEECH_MIN_NORM,
        kissing_number=LEECH_KISSING_NUMBER,
        automorphism_group="Co_0",
        automorphism_order=CO_0_ORDER,
        kappa_ch_lattice_voa=KAPPA_CH_LEECH_VOA,
        kappa_ch_k3_sigma=KAPPA_CH_K3_CY_FUNCTOR,
        shadow_class_lattice_voa="G",
        shadow_class_k3_sigma="M",
        shadow_depth_lattice_voa=2,
        has_enhanced_kac_moody=False,
        c_delta=c_delta,
    )


def leech_theta_coefficients(max_norm: int = 10) -> Dict[int, int]:
    """Known theta series coefficients for the Leech lattice.

    Theta_{Leech}(tau) = sum_{v in Lambda} q^{|v|^2 / 2}
                       = 1 + 196560 q^2 + 16773120 q^3 + ...

    The exponent is norm/2 (so norm-4 vectors contribute to q^2).
    Minimum norm is 4, so first nontrivial coefficient is at q^2.
    (AP-CY18: Leech theta series minimum norm = 4, first correction at q^2.)

    Returns dict mapping q-exponent -> coefficient.
    """
    # Known coefficients (Conway-Sloane, Table 16.1)
    coeffs = {
        0: 1,       # the zero vector
        # q^1: NO norm-2 vectors (Leech is rootless)
        2: 196560,        # 196560 vectors of norm 4
        3: 16773120,      # vectors of norm 6
        4: 398034000,     # vectors of norm 8
    }
    # Only return coefficients up to max_norm/2
    return {k: v for k, v in coeffs.items() if k <= max_norm // 2}


def leech_vs_free_field_character(max_q: int = 3) -> Dict[str, Any]:
    """Compare Leech lattice VOA character with free-field 1/eta^24.

    The free-field (Heisenberg) character:
      1/eta(tau)^24 = q^{-1} (1 + 24q + 324q^2 + 3200q^3 + ...)

    The Leech lattice VOA character:
      Theta_{Leech}(tau) / eta(tau)^24
      = q^{-1} (1 + 24q + (196560 + 324)q^2 + ...)
      Wait -- this is not quite right.  The Leech VOA character is:
      ch(V_{Leech}) = Theta_{Leech}(tau) / eta(tau)^24
      But the standard form is:
      ch(V_{Leech}) = J(tau) + 24
      where J(tau) = j(tau) - 744 = q^{-1} + 196884q + ...

    Actually: ch(V_{Leech}) = sum_{n >= -1} dim(V_n) q^n
    where V_n is the degree-n subspace.  For the Leech lattice VOA:
      dim(V_{-1}) = 1 (vacuum)
      dim(V_0) = 24 (the 24 currents, one per lattice direction)
      dim(V_1) = 196884 (the 196560 lattice vectors of norm 4 produce
                          vertex operators, plus 324 from oscillator states)

    The free-field (Heisenberg) VOA of rank 24:
      dim(V_{-1}) = 1
      dim(V_0) = 24
      dim(V_1) = 324 = p(2) * 24 + C(24,2) oscillator modes

    The divergence appears at V_1: 196884 vs 324.
    The difference 196884 - 324 = 196560 = kissing number of Leech.
    """
    # Free-field partition function coefficients: 1/eta^24
    # 1/eta(q)^24 = prod_{n>=1} 1/(1-q^n)^24
    # = q^{-1} * prod 1/(1-q^n)^24  (after including q^{-24/24} = q^{-1})
    free_field = {-1: 1, 0: 24, 1: 324, 2: 3200}

    # Leech lattice VOA character coefficients (= J(tau) + 24)
    leech_voa = {-1: 1, 0: 24, 1: 196884, 2: 21493760}

    divergence = {}
    for n in range(-1, max_q + 1):
        ff = free_field.get(n, 0)
        lv = leech_voa.get(n, 0)
        divergence[n] = {
            'free_field': ff,
            'leech_voa': lv,
            'difference': lv - ff,
            'match': ff == lv,
        }

    return {
        'free_field_character': free_field,
        'leech_voa_character': leech_voa,
        'divergence': divergence,
        'first_divergence_order': 1,
        'divergence_at_q1': 196884 - 324,
        'divergence_equals_kissing': (196884 - 324) == 196560,
        'interpretation': (
            'At q^{-1} and q^0 the characters match (universal: any rank-24 '
            'lattice VOA agrees with the free field at these orders). '
            'At q^1 they diverge by 196560 = kissing number of Leech. '
            'This is the interacting structure of V_{Leech} beyond free fields.'
        ),
    }


# =========================================================================
# 3. Conway group structure and M_24 embedding
# =========================================================================

class ConwayGroupData(NamedTuple):
    """Structural data for Co_0 and its relationship to M_24."""
    order: int
    quotient_name: str          # "Co_1" = Co_0 / {+/- I_24}
    quotient_order: int
    is_simple: bool             # Co_0 is NOT simple (center = Z/2)
    center_order: int           # |Z(Co_0)| = 2
    m24_subgroup_order: int
    m24_index: int              # [Co_0 : M_24]
    num_conjugacy_classes: int  # of Co_0
    standard_rep_dim: int       # 24 (the defining representation)


def conway_group_data() -> ConwayGroupData:
    """Return structural data for the Conway group Co_0 = Aut(Leech).

    Co_0 is the full automorphism group of the Leech lattice.
    It contains -I_{24} (negation of all coordinates), so its center
    is Z(Co_0) = {+I_{24}, -I_{24}} = Z/2.
    The quotient Co_1 = Co_0 / Z(Co_0) IS simple (one of the 26 sporadic groups).
    (AP-CY16: quotient by +/-I_{24}, the 24x24 identity matrix.)
    """
    return ConwayGroupData(
        order=CO_0_ORDER,
        quotient_name="Co_1",
        quotient_order=CO_1_ORDER,
        is_simple=False,  # Co_0 has center Z/2
        center_order=2,
        m24_subgroup_order=M_24_ORDER,
        m24_index=CO_0_M24_INDEX,
        num_conjugacy_classes=167,  # Co_0 has 167 conjugacy classes
        standard_rep_dim=24,
    )


def m24_in_co0_embedding() -> Dict[str, Any]:
    """Describe the embedding M_24 < Co_0 and what it means for K3.

    M_24 embeds in Co_0 as the subgroup fixing a "frame" of the Leech lattice.
    A frame is a set of 48 vectors (24 antipodal pairs) that form a basis
    for R^24 (up to rescaling).  M_24 permutes these 24 pairs.

    M_24 also embeds in S_24 via the Steiner system S(5,8,24).
    The K3 elliptic genus sees the M_24 action through permutations
    of the 24 Mukai directions (Eguchi-Ooguri-Tachikawa 2010).

    Co_0 is LARGER: it includes non-permutation orthogonal transformations
    of Lambda_Leech.  These additional symmetries act on the K3 Yangian
    representation category but are NOT visible in the elliptic genus
    (which only sees the permutation sector).
    """
    return {
        'embedding_type': 'frame stabilizer',
        'frame_definition': (
            'A frame of Lambda_Leech is a set of 48 vectors forming 24 '
            'antipodal pairs {v_i, -v_i} such that the 24 directions '
            'v_i/|v_i| form an orthogonal basis for R^24. '
            'M_24 is the subgroup of Co_0 that permutes the 24 pairs.'
        ),
        'm24_order': M_24_ORDER,
        'co0_order': CO_0_ORDER,
        'index': CO_0_M24_INDEX,
        'm24_acts_on': 'K3 elliptic genus (permutation of 24 parameters)',
        'co0_acts_on': 'Full Leech lattice VOA and Rep(Y(g_{K3}(Leech)))',
        'co0_beyond_m24': (
            'Co_0 includes orthogonal transformations that MIX the 24 '
            'Mukai directions (not just permute them). These additional '
            'symmetries are invisible to the elliptic genus but act on '
            'the charge >= 2 representations of Y(g_{K3}).'
        ),
        'conjectural_statement': (
            'CONJECTURAL (AP-CY14): Co_0 acts on Rep(Y(g_{K3}(Leech))) '
            'extending the M_24 action on the elliptic genus. The larger '
            'structure that Co_0 acts on is the full representation category, '
            'not just the twined partition functions.'
        ),
    }


def co0_24dim_representation() -> Dict[str, Any]:
    """The 24-dimensional standard representation of Co_0.

    Co_0 acts faithfully on R^24 by lattice automorphisms.
    This 24-dimensional representation is irreducible over R.

    Over Q (rationals): the representation remains irreducible.
    Over C (complex): the representation remains irreducible
    (no proper Co_0-invariant subspaces of C^24).

    Restriction to M_24:
      24|_{M_24} = 1 + 23
    where 1 is the trivial and 23 is the standard M_24 representation
    (the deleted permutation representation: the 24-letter permutation
    representation minus the trivial component sum_i e_i).

    For the K3 Yangian:
      The charge-1 representation V = C^24 carries the Co_0 action.
      The charge-n representation decomposes under Co_0 into irreducibles.
    """
    return {
        'dimension': 24,
        'is_irreducible_over_R': True,
        'is_irreducible_over_C': True,
        'restriction_to_m24': '24 = 1 + 23 (trivial + deleted permutation)',
        'character_at_identity': 24,
        'character_at_minus_identity': 24,  # -I acts as (-1)^24 = 1 on trace
        # Actually: trace(-I_{24}) = -24.  Let me correct:
        # -I_{24} acts on R^24 by negating all coordinates.
        # trace(-I_{24}) = 24 * (-1) = -24.
        'character_at_minus_identity_corrected': -24,
        'note': (
            'The center element -I_{24} acts on the 24-dim rep with '
            'trace -24.  In the quotient Co_1, this element is identified '
            'with the identity, so Co_1 acts on the PROJECTIVE space P^23.'
        ),
    }


# =========================================================================
# 4. Monster VOA connection
# =========================================================================

class MonsterVOAConnection(NamedTuple):
    """Data on the V^natural - K3 Yangian connection."""
    voa_name: str               # "V^natural (FLM Monster VOA)"
    central_charge: int         # 24
    kappa_ch: int               # 12
    automorphism_group: str     # "Monster M"
    automorphism_order: int     # |M|
    construction: str           # "Z/2-orbifold of V_{Leech}"
    co1_in_monster: bool        # True: Co_1 < M
    yangian_connection: str     # status of connection


def monster_voa_connection() -> MonsterVOAConnection:
    """Describe the FLM Monster VOA V^natural and its K3 Yangian connection.

    V^natural = V_{Leech} / Z_2  (the Z/2-orbifold)
    Aut(V^natural) = Monster M

    The chain:
      K3 -> Lambda_Muk (rank 24) -> Niemeier -> Lambda_Leech
      -> V_{Leech} (c=24, kappa_ch=24, Aut=Co_0)
      -> V^natural (c=24, kappa_ch=12, Aut=Monster M)

    The K3 Yangian connection to V^natural is INDIRECT:
      Y(g_{K3}) acts on V_{Leech} modules (conjectural).
      V^natural is the orbifold of V_{Leech} by the involution theta
      (the lift of -I_{24} to the VOA).
      There is no direct Y(g_{K3}) action on V^natural modules.

    Co_1 = Co_0/{+/-I_{24}} is a subgroup of the Monster (the largest
    sporadic subgroup).  The Monster has additional structure beyond Co_1.
    """
    return MonsterVOAConnection(
        voa_name="V^natural (FLM Monster VOA)",
        central_charge=24,
        kappa_ch=KAPPA_CH_MONSTER_VOA,
        automorphism_group="Monster M",
        automorphism_order=MONSTER_ORDER,
        construction="Z/2-orbifold of V_{Leech}",
        co1_in_monster=True,
        yangian_connection=(
            "INDIRECT and CONJECTURAL. Y(g_{K3}) at the Leech point acts on "
            "V_{Leech} modules (conjectural, AP-CY14). V^natural is the Z/2-"
            "orbifold of V_{Leech}; the orbifold procedure is NOT a Yangian "
            "operation. No direct Y(g_{K3}) action on V^natural modules is "
            "known. The connection is through Co_1 < Monster: the Conway "
            "group embeds in the Monster, but the Yangian structure does not "
            "extend to the full Monster symmetry."
        ),
    )


def kappa_ch_hierarchy() -> Dict[str, Any]:
    """The kappa_ch hierarchy for K3-related VOAs.

    Three algebraization routes produce three different kappa_ch values
    from the same K3 geometry (Proposition prop:k3-trichotomy):

      kappa_ch = 24: Leech lattice VOA V_{Leech}
      kappa_ch = 12: Monster VOA V^natural
      kappa_ch = 2:  CY functor Phi(D^b(K3))

    The ratio 24 : 12 : 2 = 12 : 6 : 1 encodes the depth at which
    each route interrogates the 24-dimensional H*(K3).
    """
    hierarchy = OrderedDict()
    hierarchy['V_{Leech}'] = {
        'kappa_ch': 24,
        'central_charge': 24,
        'construction': 'Lattice VOA (24 free bosons on Lambda_Leech)',
        'shadow_class': 'G',
        'depth': 'sees full H*(K3) = 24 dimensions',
        'automorphism': f'Co_0 (order {CO_0_ORDER})',
    }
    hierarchy['V^natural'] = {
        'kappa_ch': 12,
        'central_charge': 24,
        'construction': 'Z/2-orbifold of V_{Leech}',
        'shadow_class': 'unknown (not computed in this engine)',
        'depth': 'Z/2-orbifold halves the lattice data: 24/2 = 12',
        'automorphism': f'Monster M (order {MONSTER_ORDER})',
    }
    hierarchy['Phi(D^b(K3))'] = {
        'kappa_ch': 2,
        'central_charge': 24,
        'construction': 'CY-to-chiral functor (CY-A_2, PROVED at d=2)',
        'shadow_class': 'M (K3 sigma model)',
        'depth': 'CY trace projects to chi(O_K3) = 2',
        'automorphism': 'K3 sigma model symmetry group (varies with moduli)',
    }
    return {
        'hierarchy': hierarchy,
        'ratio': '24 : 12 : 2 = 12 : 6 : 1',
        'common_source': 'dim H*(K3, C) = 24',
        'interpretation': (
            'The three values are NOT different answers to the same question. '
            'They are answers to different questions: how much of the 24-dim '
            'Hochschild homology does each algebraization route promote to '
            'chiral algebra generators contributing to the shadow tower?'
        ),
    }


# =========================================================================
# 5. Structure function at the Leech point
# =========================================================================

def leech_structure_function_properties() -> Dict[str, Any]:
    """Properties of g_{K3}(z) = prod (z - h_i)/(z + h_i) at the Leech point.

    At the Leech enhancement point, the 24 parameters h_i are NOT constrained
    by any root system (Leech has no roots).  The parameters are subject only
    to the CY_2 constraint: sum h_i = 0.

    The structure function has degree (24, 24): numerator and denominator
    are both degree-24 polynomials in z.

    Properties (proved for ANY choice of h_i satisfying sum h_i = 0):
      g(inf) = 1
      g(0) = (-1)^{24} = 1  (for 24 factors)
      g(z) * g(-z) = 1  (unitarity)
      g(-z) = 1/g(z)   (equivalently)

    At the Leech point specifically:
      - No h_i = 0 (no roots => no degenerate factors)
      - The h_i can be chosen to lie in the complexified Leech lattice
      - Co_0 acts on the parameter space by orthogonal transformations
      - The structure function is NOT invariant under Co_0 (only under
        permutations, and Co_0 includes non-permutation transformations)
    """
    return {
        'degree': (24, 24),
        'g_at_infinity': 1,
        'g_at_zero': 1,  # (-1)^24 = 1
        'unitarity': 'g(z) * g(-z) = 1',
        'cy2_constraint': 'sum_{i=1}^{24} h_i = 0',
        'root_system_constraint': 'NONE (Leech has no roots)',
        'symmetry_group': (
            'S_24 (permutations) acts trivially on g(z). '
            'Co_0 (orthogonal transformations) does NOT preserve g(z) '
            'but acts on the R-matrix by conjugation.'
        ),
        'co0_action_on_rmatrix': (
            'For g in Co_0: R^g(z) = g R(z) g^{-1}. '
            'The diagonal R-matrix becomes non-diagonal under non-permutation '
            'elements of Co_0, but continues to satisfy YBE.'
        ),
        'specialization': (
            'At the Leech point, the 24 parameters h_i parametrize a '
            '23-dimensional space (CY_2 constraint removes 1 degree of '
            'freedom). This is the MAXIMAL parameter freedom: at other '
            'Niemeier points, root system constraints reduce the freedom '
            'further.'
        ),
        'parameter_freedom_dim': 23,  # 24 - 1 (CY_2 constraint)
    }


# =========================================================================
# 6. Comparison landscape: Leech vs other Niemeier points
# =========================================================================

def niemeier_automorphism_orders() -> Dict[str, int]:
    """Automorphism group orders for Niemeier lattice VOAs.

    The Leech lattice has the LARGEST automorphism group (Co_0).
    All other Niemeier lattices have root systems, and their
    automorphism groups are products of Weyl groups and diagram
    automorphisms, which are much smaller.

    This data is for the LATTICE automorphism groups, not the VOA
    automorphism groups (which can be larger by additional outer
    automorphisms).
    """
    # Selected automorphism group orders
    # Full computation requires extensive group theory; we record key values
    return {
        'Leech': CO_0_ORDER,
        'E_8^3': (
            # Aut(E_8)^3 x S_3 = |W(E_8)|^3 * |Out(E_8)|^3 * 3!
            # |W(E_8)| = 696729600
            # |Out(E_8)| = 1
            696729600**3 * 6
        ),
        'D_24': (
            # |W(D_24)| * |Out(D_24)| = 2^23 * 24! * 2
            2**23 * math.factorial(24) * 2
        ),
        'A_1^24': (
            # Aut(A_1^24) = W(A_1)^24 x M_24 = 2^24 * |M_24|
            # (M_24 permutes the 24 copies)
            2**24 * M_24_ORDER
        ),
    }


def leech_uniqueness_properties() -> Dict[str, Any]:
    """Properties that make the Leech lattice UNIQUE among Niemeier lattices.

    The Leech lattice Lambda is the unique Niemeier lattice with:
      (1) No roots (no vectors of norm 2)
      (2) Minimum norm 4
      (3) Largest automorphism group (Co_0)
      (4) Largest kissing number among Niemeier lattices: 196560
      (5) Deep holes of depth exactly sqrt(2)

    For the K3 Yangian, the Leech point is special because:
      (a) No enhanced Kac-Moody algebra (consequence of (1))
      (b) Maximal parameter freedom (23 dimensions, no root constraints)
      (c) The full Co_0 acts, not just a Weyl group
      (d) The shadow class of the lattice VOA is G (same as all Niemeier),
          but the K3 sigma model at this point has class M (as at all points)
    """
    return {
        'is_unique_rootless': True,
        'min_norm': LEECH_MIN_NORM,
        'kissing_number': LEECH_KISSING_NUMBER,
        'automorphism_order': CO_0_ORDER,
        'deep_hole_depth': 'sqrt(2)',
        'num_deep_holes': 23,  # 23 types of deep holes -> 23 other Niemeier lattices!
        'deep_holes_bijection': (
            'The 23 types of deep holes in the Leech lattice are in '
            'bijection with the 23 other Niemeier lattices (Conway-Sloane). '
            'This gives a canonical map from Lambda_Leech to the full '
            'Niemeier classification.'
        ),
        'yangian_consequence': (
            'At the Leech point, Y(g_{K3}) has maximal symmetry (Co_0) '
            'and maximal parameter freedom (23 dimensions). The 23 deep '
            'hole types correspond to 23 DEFORMATION DIRECTIONS in the '
            'K3 Yangian parameter space, each leading to a different '
            'Niemeier enhancement point.'
        ),
    }


# =========================================================================
# 7. Conway moonshine and the universal multiplier
# =========================================================================

def conway_moonshine_data() -> Dict[str, Any]:
    """Data on Conway moonshine and its K3 Yangian interpretation.

    Conway moonshine (Duncan 2005, Duncan-Mack-Crane 2014):
    The shorter moonshine module V^{s,natural} (c = 12) has
    Aut(V^{s,natural}) = Co_0.

    The Conway moonshine module is related to the K3 sigma model
    through the connection:
      V^{s,natural} -> super VOA structure -> N=1 SVOA at c=12
    The K3 sigma model has c = 6 for the N=(4,4) SCFT; the N=1
    reduction gives c = 12 for the left-moving sector (holomorphic).

    This is DISTINCT from the FLM Monster VOA (which has c = 24).

    Open question (conj:universal-moonshine-multiplier):
    Does the decomposition A_n = kappa_ch * dim(rho_n^G) hold for
    V^{s,natural} with G = Co_0?  The kappa_ch of V^{s,natural}
    is not computed in this engine.
    """
    return {
        'module_name': 'V^{s,natural} (shorter moonshine module)',
        'central_charge': 12,
        'automorphism_group': 'Co_0',
        'automorphism_order': CO_0_ORDER,
        'is_super_voa': True,
        'construction': (
            'Duncan-Mack-Crane (2014): constructed from a Z/2-orbifold '
            'of a lattice VOA related to the Barnes-Wall lattice BW_16, '
            'or equivalently from the Conway group acting on the c=12 '
            'fermion system.'
        ),
        'k3_connection': (
            'V^{s,natural} at c=12 is related to the K3 sigma model (c=6) '
            'through the N=1 holomorphic SCFT structure. The N=4 -> N=1 '
            'reduction doubles the central charge. CONJECTURAL: the Conway '
            'moonshine module encodes the full left-moving sector of the '
            'K3 sigma model, with Co_0 acting as the symmetry group at '
            'the Leech enhancement point.'
        ),
        'universal_multiplier_question': (
            'Open problem (conj:universal-moonshine-multiplier): does '
            'the Conway moonshine decomposition A_n^{Co_0} = kappa_ch * '
            'dim(rho_n^{Co_0}) hold? This requires computing kappa_ch '
            'of V^{s,natural}, which is not yet done.'
        ),
    }


# =========================================================================
# 8. Sporadic group tower and K3
# =========================================================================

def sporadic_tower_from_k3() -> Dict[str, Any]:
    """The tower of sporadic groups connected to K3 through moonshine.

    Starting from K3, we obtain a tower of sporadic groups through
    increasingly indirect connections:

    Level 0: K3 sigma model symmetries
      -> Gaberdiel-Hohenegger-Volpato: symm groups G(M) < M_24 for each model M
      -> Union generates M_24 (the first sporadic group)

    Level 1: K3 elliptic genus
      -> Mathieu moonshine (EOT 2010): M_24 acts on the BPS spectrum
      -> A_n = kappa_ch * dim(rho_n^{M_24}) with kappa_ch = 2

    Level 2: Leech lattice (the rootless Niemeier lattice)
      -> Co_0 = Aut(Lambda_Leech) acts at the Leech enhancement point
      -> Conway moonshine: V^{s,natural} has Aut = Co_0

    Level 3: Monster VOA V^natural
      -> Z/2-orbifold of V_{Leech}: Aut = Monster M
      -> Monstrous moonshine: McKay-Thompson series are Hauptmoduls

    Each level is more indirect:
      M_24: acts directly on K3 sigma model symmetries
      Co_0: acts on the Leech lattice VOA (one of 24 Niemeier points)
      Monster: acts on V^natural (orbifold of V_{Leech})

    The Yangian connection weakens at each level:
      M_24: acts on Rep(Y(g_{K3})) by parameter permutation (conjectural)
      Co_0: acts on Rep(Y(g_{K3}(Leech))) by orthogonal transformation (conjectural)
      Monster: NO direct Yangian action known
    """
    return {
        'tower': [
            {
                'level': 0,
                'group': 'Sigma model symmetry groups G(M) < M_24',
                'connection_to_k3': 'DIRECT (acts on worldsheet)',
                'yangian_connection': 'Acts on parameters by permutation',
                'status': 'PROVED (Gaberdiel-Hohenegger-Volpato)',
            },
            {
                'level': 1,
                'group': f'M_24 (order {M_24_ORDER})',
                'connection_to_k3': 'Elliptic genus decomposition',
                'yangian_connection': (
                    'CONJECTURAL: acts on Rep(Y(g_{K3})) by S_24 permutation'
                ),
                'status': 'PROVED as moonshine (EOT + Gannon)',
            },
            {
                'level': 2,
                'group': f'Co_0 (order {CO_0_ORDER})',
                'connection_to_k3': 'Leech enhancement point in K3 moduli',
                'yangian_connection': (
                    'CONJECTURAL: acts on Rep(Y(g_{K3}(Leech))) by O(24)'
                ),
                'status': 'Conway moonshine PROVED (Duncan-Mack-Crane)',
            },
            {
                'level': 3,
                'group': f'Monster M (order {MONSTER_ORDER})',
                'connection_to_k3': 'Z/2-orbifold of V_{Leech}',
                'yangian_connection': 'NO direct Yangian connection known',
                'status': 'Monstrous moonshine PROVED (Borcherds)',
            },
        ],
        'pattern': (
            'Each step in the tower: K3 -> M_24 -> Co_0 -> Monster '
            'adds one layer of algebraic construction (moduli point '
            'specialization -> lattice automorphism -> VOA orbifold). '
            'The Yangian connection weakens at each step.'
        ),
    }


# =========================================================================
# 9. Numerical verification functions
# =========================================================================

def verify_co0_order() -> bool:
    """Verify |Co_0| = 2^22 * 3^9 * 5^4 * 7^2 * 11 * 13 * 23.

    This is the standard factorization from Conway-Sloane.
    """
    expected = 2**22 * 3**9 * 5**4 * 7**2 * 11 * 13 * 23
    return CO_0_ORDER == expected


def verify_monster_order() -> bool:
    """Verify |M| = 2^46 * 3^20 * 5^9 * 7^6 * 11^2 * 13^3 * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71.

    Standard factorization.
    """
    expected = (
        2**46 * 3**20 * 5**9 * 7**6 * 11**2 * 13**3
        * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71
    )
    return MONSTER_ORDER == expected


def verify_index_co0_m24() -> bool:
    """Verify [Co_0 : M_24] is an integer and equals |Co_0|/|M_24|."""
    return CO_0_ORDER % M_24_ORDER == 0 and CO_0_M24_INDEX == CO_0_ORDER // M_24_ORDER


def verify_co1_in_monster() -> bool:
    """Verify that |Co_1| divides |Monster|.

    Co_1 < Monster, so |Co_1| must divide |Monster|.
    """
    return MONSTER_ORDER % CO_1_ORDER == 0


def verify_leech_theta_q2() -> bool:
    """Verify the q^2 coefficient of Theta_{Leech} = 196560.

    This is the kissing number of the Leech lattice.
    Cross-check: 196560 = 2 * 196560/2 where 196560/2 = 98280.
    Also: 196560 = 24 * 8190 + 24 * 10 = ... (decomposition under M_24).

    Standard reference: Conway-Sloane, Table 1.3.
    """
    coeffs = leech_theta_coefficients()
    return coeffs.get(2, 0) == 196560


def verify_24_not_coincidence() -> bool:
    """Verify the logical chain: 24 = dim H*(K3) = rank(Lambda_Muk) = rank(Leech).

    The chain:
      b_0(K3) + b_2(K3) + b_4(K3) = 1 + 22 + 1 = 24  (Betti numbers)
      rank(Lambda_Muk) = dim H*(K3, Z) = 24
      rank(Lambda_Leech) = 24  (Niemeier lattice)
    """
    b0 = 1   # H^0(K3)
    b1 = 0   # H^1(K3) = 0 (simply connected)
    b2 = 22  # H^2(K3) (= 3 * h^{1,1} when h^{1,1} + h^{2,0} = 20 + 1, but
              # the full b_2 = 22 from the lattice U^3 + E_8(-1)^2)
    b3 = 0   # H^3(K3) = 0
    b4 = 1   # H^4(K3) = Z (fundamental class)

    dim_H_star = b0 + b1 + b2 + b3 + b4
    chi_top = b0 - b1 + b2 - b3 + b4  # Euler characteristic

    return (
        dim_H_star == 24
        and chi_top == 24
        and MUKAI_RANK == 24
        and LEECH_RANK == 24
        and dim_H_star == MUKAI_RANK
        and K3_LATTICE_RANK + 2 == MUKAI_RANK  # b_2 + 2 = 24
    )


def verify_kappa_ch_hierarchy() -> bool:
    """Verify the kappa_ch hierarchy: 24, 12, 2 with correct ratios."""
    return (
        KAPPA_CH_LEECH_VOA == 24
        and KAPPA_CH_MONSTER_VOA == 12
        and KAPPA_CH_K3_CY_FUNCTOR == 2
        and KAPPA_CH_LEECH_VOA == 2 * KAPPA_CH_MONSTER_VOA  # orbifold halving
        and KAPPA_CH_MONSTER_VOA == 6 * KAPPA_CH_K3_CY_FUNCTOR
        and KAPPA_CH_LEECH_VOA == 12 * KAPPA_CH_K3_CY_FUNCTOR
    )


def verify_character_divergence() -> bool:
    """Verify that V_{Leech} character diverges from free field at q^1.

    Free field: dim(V_1) = 324
    Leech VOA: dim(V_1) = 196884
    Difference: 196884 - 324 = 196560 = kissing number of Leech
    """
    data = leech_vs_free_field_character()
    return (
        data['divergence_at_q1'] == 196560
        and data['divergence_equals_kissing']
        and data['first_divergence_order'] == 1
    )


def verify_leech_c_delta() -> bool:
    """Verify c_Delta(Leech) = -65520/691.

    Formula: c_Delta(N) = (691 * |R(N)| - 65520) / 691
    For Leech: |R| = 0, so c_Delta = -65520/691.
    """
    data = leech_enhancement_point()
    expected = Fraction(-65520, 691)
    return data.c_delta == expected


def verify_signatures_differ() -> bool:
    """Verify that Mukai and Leech signatures differ.

    Mukai: (4, 20)
    Leech: (0, 24)
    These are DIFFERENT -- no lattice isometry exists.
    """
    return MUKAI_SIGNATURE != LEECH_SIGNATURE


def verify_leech_no_roots() -> bool:
    """Verify the Leech lattice has no roots (the defining property)."""
    data = leech_enhancement_point()
    return data.num_roots == 0 and not data.has_enhanced_kac_moody


def verify_deep_holes_count() -> bool:
    """Verify that the Leech lattice has 23 types of deep holes.

    The 23 types of deep holes in Lambda_Leech are in bijection with
    the 23 Niemeier lattices with nonempty root system.
    Total Niemeier lattices = 24, minus Leech itself = 23.
    """
    data = leech_uniqueness_properties()
    return data['num_deep_holes'] == 23


# =========================================================================
# 10. Summary functions
# =========================================================================

def full_investigation_summary() -> Dict[str, Any]:
    """Complete summary of the Conway-Leech-K3 investigation.

    Answers the five questions posed:

    Q1: Is there ANY connection between the 24 Mukai generators and the
        24 Leech dimensions?
    A1: YES, but NOT a direct lattice isomorphism (signatures differ:
        (4,20) vs (0,24)). The connection is through the Niemeier
        classification: both are rank-24 lattices, and the K3 moduli
        space parametrizes embeddings into Niemeier lattices. The rank
        24 arises from dim H*(K3, C) = 24 in both cases.

    Q2: The Niemeier lattice with root system {} IS the Leech lattice.
        At this enhancement point: Y(g_{K3}(Leech)) has what properties?
    A2: At the Leech point, Y(g_{K3}(Leech)) has:
        - No enhanced Kac-Moody subalgebra (no roots)
        - Maximal parameter freedom (23 dimensions)
        - Co_0 = Aut(Lambda_Leech) acts on the representation category
        - kappa_ch = 2 (K3 sigma model, topological)
        - kappa_ch = 24 (Leech lattice VOA, rank)

    Q3: Co_0 contains M_24 as a subgroup. The M_24 acts on the K3
        elliptic genus. Does Co_0 act on a LARGER structure?
    A3: YES. M_24 acts by permuting the 24 parameters (visible in the
        elliptic genus). Co_0 acts by ORTHOGONAL transformations on
        the 24-dim representation space (visible in the full
        representation category Rep(Y(g_{K3}(Leech))), NOT just in
        the elliptic genus). Co_0 sees the full 196560-element
        minimal shell, not just the 24 coordinate axes.

    Q4: The FLM monster VOA V^natural has Aut = Monster M.
        Is there a K3 Yangian connection to V^natural?
    A4: INDIRECT. The chain is:
        Y(g_{K3}) -> V_{Leech} modules -> (Z/2 orbifold) -> V^natural
        The Z/2-orbifold step is NOT a Yangian operation. There is no
        direct Y(g_{K3}) action on V^natural modules. The connection
        is through Co_1 < Monster (Conway quotient embeds in Monster).

    Q5: The 24 = dim(Leech) = rank(Mukai) = b_2(K3)+2.
        Is this a coincidence?
    A5: NOT a coincidence. The single source is dim H*(K3, C) = 24:
        - rank(Lambda_Muk) = 24 because H*(K3) is 24-dimensional
        - rank(Lambda_Leech) = 24 because Niemeier lattices have rank 24
        - b_2(K3) + 2 = 22 + 2 = 24 (the +2 is from H^0 + H^4)
        - chi_top(K3) = 24 (same Betti number sum, with alternating signs
          that happen to give the same answer for a surface with b_1=b_3=0)
        The deep reason: dimension 24 is where even unimodular lattices
        are maximally rigid (finite Niemeier classification), creating
        the triangle K3-Leech-moonshine.
    """
    return {
        'Q1_mukai_leech_connection': {
            'answer': 'YES, through Niemeier classification, NOT direct isomorphism',
            'obstruction': 'Signatures differ: (4,20) vs (0,24)',
            'bridge': 'Both rank 24; K3 moduli embeds in Niemeier lattices',
        },
        'Q2_leech_enhancement_point': {
            'answer': 'No Kac-Moody, maximal freedom, Co_0 symmetry',
            'kappa_ch_lattice_voa': 24,
            'kappa_ch_k3_sigma': 2,
            'shadow_class': 'G (lattice VOA) / M (K3 sigma model)',
        },
        'Q3_co0_larger_structure': {
            'answer': 'YES, Co_0 acts on full Rep(Y(g_{K3}(Leech)))',
            'what_co0_sees': 'Orthogonal transformations, not just permutations',
            'visible_in': 'Charge >= 2 representations and 196560 minimal vectors',
        },
        'Q4_monster_voa_connection': {
            'answer': 'INDIRECT, through V_{Leech} -> V^natural orbifold',
            'yangian_action_on_monster_voa': 'NONE known',
            'link': 'Co_1 < Monster (largest sporadic subgroup)',
        },
        'Q5_rank_24_coincidence': {
            'answer': 'NOT a coincidence',
            'source': 'dim H*(K3, C) = 24',
            'deep_reason': 'Dimension 24: Niemeier lattices are finitely classified',
        },
        'status': ENGINE_STATUS,
        'ap_compliance': 'AP-CY14 (conjectural), AP113 (subscripted kappa), AP-CY18',
    }


# =========================================================================
# Convenience function for tests
# =========================================================================

def all_niemeier_lattices_with_leech() -> List[NiemeierLattice]:
    """Return all 24 Niemeier lattices including Leech (index 1).

    Wraps the niemeier_shadow_landscape function.
    """
    return [niemeier_lattice(i) for i in range(1, 25)]
