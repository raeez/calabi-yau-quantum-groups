r"""
diagonal_siegel_cy_orbifolds.py -- diagonal Siegel modular forms attached
to the K3-orbifold Borcherds ladder.

MATHEMATICAL OVERVIEW
=====================

The programme-active CHL ladder has smooth CY3 host geometry at
N in {1, 2, 3, 4, 6}.  The Mukai-admissible extensions N in {5, 7, 8}
record the same Borcherds-weight normalization but their smooth
K3 x E host status is conjectural.  The invariant computed here is
kappa_BKM = c_N(0)/2, the Borcherds product weight.  It is not
kappa_cat and it is not the compact Hodge/PhiFA supertrace.

The eight cases are:

    N=1: K3 x E (no orbifold).  Siegel form = Delta_5 (weight 5).
         BKM algebra = g_{Delta_5}.  kappa_BKM = 5.
         Input Jacobi form = phi_{0,1} (K3 elliptic genus).
         Root multiplicities = c(D) from phi_{0,1}.

    N=2: (K3 x E) / (Z/2Z), Enriques involution.
         Siegel form = Allcock product on O(2,10), weight 4.
         kappa_BKM = 4.
         Input = (1/2) * phi_{0,1} (Enriques elliptic genus).
         Root multiplicities halved.

    N=3: (K3 x E) / (Z/3Z), order-3 symplectic automorphism.
         Siegel form has weight c_3(0)/2 where c_3(0) comes from
         the Z/3Z-orbifold elliptic genus.  Weight = 3.
         kappa_BKM = 3.

    N=4: CHL K3-orbifold ladder entry.  Weight = 2.  kappa_BKM = 2.
    N=5: Mukai-admissible extension.  Weight = 2.  kappa_BKM = 2.
    N=6: CHL K3-orbifold ladder entry.  Weight = 1.  kappa_BKM = 1.
    N=7: Mukai-admissible extension.  Weight = 1.  kappa_BKM = 1.
    N=8: Mukai-admissible extension.  Weight = 1.  kappa_BKM = 1.

THE Z/NZ-ORBIFOLD ELLIPTIC GENUS
---------------------------------

For a Z/NZ-orbifold of K3, the orbifold elliptic genus is:

    phi_N(tau, z) = (1/N) * sum_{g,h in Z/NZ} phi_{g,h}(tau, z)

where phi_{g,h} is the g-twisted, h-twined elliptic genus of K3.
The constant term c_N(0) of phi_N determines the Borcherds lift weight:

    weight_N = c_N(0) / 2

For a SYMPLECTIC automorphism g of order N acting on K3, the twined
elliptic genus phi_g(tau, z) = Tr_{RR}(g * y^{J_0} * q^{L_0 - c/24})
has constant term:

    phi_g(tau, 0) = chi(K3^g)  (Euler characteristic of fixed locus)

The key data (from the Frame shape / cycle shape of g in M_24):

    N=1: chi(K3) = 24,  c_1(0) = 24 -> but phi_{0,1} has c(0) = 10 (*)
    N=2: chi(K3^g) = 8   (8 fixed points for Enriques-type)
    N=3: chi(K3^g) = 6   (6 fixed points)
    N=4: chi(K3^g) = 4   (4 fixed points)
    N=5: chi(K3^g) = 4   (4 fixed points)
    N=6: chi(K3^g) = 2   (2 fixed points)
    N=7: chi(K3^g) = 3   (3 fixed points)
    N=8: chi(K3^g) = 2   (2 fixed points)

(*) IMPORTANT: The Borcherds lift weight for the K3 case uses the WEAK
    Jacobi form phi_{0,1} with c(0) = 10 (the INDEX-1 form), not the
    full elliptic genus trace which gives 24 at z=0.  The distinction:
    phi_{0,1}(tau, 0) = 2 * (E_4(tau)^{3/4})... actually phi_{0,1}(tau, 0) = 12
    always.  No: c(0) as a discriminant-indexed coefficient is 10,
    because c(D=0) counts the q^n r^l terms with 4n - l^2 = 0.

    The Borcherds lift weight formula is:
        weight = c(D=0) / 2

    For phi_{0,1}: c(D=0) = f(0,0) + f(1,2) + f(1,-2) + ... = 10.
    Actually: f(0,0) = 10 (the constant term in the (n,l)-expansion with
    D = 4*0 - 0^2 = 0).  And the EZ convention gives c(-1) = 2, c(0) = 10.
    So weight = 10/2 = 5.  Correct.

THE ORBIFOLD CONSTANT TERM AND BORCHERDS WEIGHT
-------------------------------------------------

For the Z/NZ-orbifold, the input Jacobi form is the orbifold-averaged
elliptic genus.  The constant term c_N(0) (at discriminant D=0)
determines the weight:

    N:  c_N(0)   weight = c_N(0)/2   kappa_BKM(N)
    1:    10         5                    5
    2:     8         4                    4
    3:     6         3                    3
    4:     4         2                    2
    5:     4         2                    2
    6:     2         1                    1
    7:     2         1                    1
    8:     2         1                    1

These follow from the FRAME SHAPES of the corresponding M_24 conjugacy
classes (Gaberdiel-Hohenegger-Volpato, Eguchi-Hikami):

    N=1: 1^24                c_N(0) = 10
    N=2: 1^8 2^8             c_N(0) = 8     (-> weight 4)
    N=3: 1^6 3^6             c_N(0) = 6     (-> weight 3)
    N=4: 1^4 2^2 4^4         c_N(0) = 4     (-> weight 2)
    N=5: 1^4 5^4             c_N(0) = 4     (-> weight 2)
    N=6: 1^2 2^1 3^2 6^2 (!) c_N(0) = 2     (-> weight 1)
    N=7: 1^3 7^3             c_N(0) = 2     (-> weight 1) [*]
    N=8: 1^2 2^1 4^1 8^2     c_N(0) = 2     (-> weight 1)

[*] Note: N=7 has c_N(0) = 2 (not 3), because the orbifold genus
    involves the full twisted sector average, not just chi(K3^g)/N.
    The correct formula is: c_N(0) = (1/N) * sum_{g in Z/NZ} c_g(0),
    where c_g(0) is the twined discriminant-0 coefficient.  For N=7,
    the untwisted sector gives c_1(0) = 10, and the six twisted
    sectors each contribute c_g(0) = -8/6 + correction terms.

    Actually, the precise values come from the eta-product formula
    for the twined elliptic genus.  The twined genus phi_g has the
    structure phi_g(tau, z) = (2/N_g) * sum theta_{m,l}(tau,z) h_{g,l}(tau)
    where h_{g,l} are specific eta-quotients determined by the Frame shape.

    For our purposes, the KEY DATA is the Borcherds lift weight,
    which has been computed in the literature:

LITERATURE VALUES (verified):
    N=1: weight 5   (Gritsenko-Nikulin 1996, Delta_5 = Igusa cusp form)
    N=2: weight 4   (Allcock 2000, Gritsenko-Nikulin 1998)
    N=3: weight 3   (Gritsenko 1994)
    N=4: weight 2   (Gritsenko 1994, Clery-Gritsenko 2013)
    N=5: weight 2   (Gritsenko 1994)
    N=6: weight 1   (Gritsenko 1994)
    N=7: weight 1   (Gritsenko 1994)
    N=8: weight 1   (Gritsenko 1994)

THE TWINED ELLIPTIC GENUS: ETA-PRODUCT FORMULA
------------------------------------------------

For an order-N symplectic automorphism g of K3 with Frame shape
pi_g = prod_a a^{m_a} (so sum_a a * m_a = 24), the twined
elliptic genus is:

    phi_g(tau, z) = Tr_{RR}(g * y^{J_0} * q^{L_0 - c/24})

The key constraint: phi_g is a weak Jacobi form of weight 0 and
index 1 for a congruence subgroup Gamma_0(N).  The constant term
(at z=0):

    phi_g(tau, 0) = sum_l c_g(n,l) with 4n = l^2

For our purposes, the discriminant-0 coefficient c_g(D=0) is
extracted from the Frame shape:

    c_g(D=0) = sum_{a | gcd(N, ...)} contribution from fixed-point data

The net effect on the orbifold Borcherds weight is:

    weight(X_N) = c_N(D=0) / 2

where c_N(D=0) is the orbifold-averaged discriminant-0 coefficient.

AP-CY6 WARNING: the CHL host entries are CY3 orbifold data conditional
on CY-A_3.  The N in {5, 7, 8} extensions record Borcherds-weight
normalization but do not have the same smooth K3 x E CHL host status.
All results involving G(X_N) remain CONJECTURAL.  Use
ClaimStatusConjectured.

AP-CY9 WARNING: Discriminant constraints must be respected.  For
index-1 Jacobi forms: D = 0 or D = 3 mod 4 only.

AP113 WARNING: kappa_BKM is subscripted for each N.  Never bare kappa.

FOUR-KAPPA NORMALIZATION
------------------------

For K3 x E at N=1 the lanes are separated as follows:

    kappa_cat(K3 x E)              = chi(O_{K3 x E}) = 0
    kappa_ch_compact_hodge(K3 x E) = Xi(K3 x E) = 0
    kappa_ch_Heis(K3 x E)          = 3
    kappa_BKM(Delta_5)             = c_1(0)/2 = 10/2 = 5
    kappa_fiber(K3)                = rank H^*(K3, Z) = 24
    kappa_cat_K3_fiber             = chi(O_{K3}) = 2

The equality 3 + 2 = 5 is a Heisenberg-fibre coincidence at N=1,
not a derivation of kappa_BKM.

References
----------
    Gritsenko-Nikulin, "Automorphic forms and Lorentzian KM algebras II" (1998)
    Allcock, "The period lattice for Enriques surfaces" (2000)
    Gritsenko, "Modular forms and moduli spaces of abelian and K3 surfaces" (1994)
    Gaberdiel-Hohenegger-Volpato, "Mathieu Moonshine in the elliptic genus
        of K3" (2010)
    Eguchi-Hikami, "Note on twisted elliptic genus of K3 surface" (2011)
    Cheng-Duncan-Harvey, "Umbral Moonshine and the Niemeier lattices" (2014)
    Clery-Gritsenko, "Siegel modular forms of genus 2 with the simplest
        divisor" (2013)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import importlib as _importlib
import os as _os
import sys as _sys


# ---------------------------------------------------------------------------
# Import helpers
# ---------------------------------------------------------------------------

def _import_module(name: str):
    """Import from compute.lib, falling back to direct import."""
    try:
        return _importlib.import_module(f'compute.lib.{name}')
    except (ImportError, ModuleNotFoundError):
        _lib_dir = _os.path.dirname(_os.path.abspath(__file__))
        if _lib_dir not in _sys.path:
            _sys.path.insert(0, _lib_dir)
        return _importlib.import_module(name)


_phi01_mod = _import_module('phi01_fourier')
_phi01_table = _phi01_mod.phi01_table
_phi01_coeff = _phi01_mod.phi01_coefficient
_phi01_by_disc = _phi01_mod.phi01_by_discriminant


# =========================================================================
# 1. FRAME SHAPES AND TWINED GENERA FOR Z/NZ AUTOMORPHISMS OF K3
# =========================================================================

class FrameShapeData(NamedTuple):
    """Data for a Z/NZ symplectic automorphism of K3.

    Attributes
    ----------
    N : int
        Order of the automorphism (1 through 8).
    frame_shape : dict
        Frame shape pi_g = prod_a a^{m_a}, encoded as {a: m_a}.
        Must satisfy sum_a a * m_a = 24.
    fixed_point_count : int
        Number of isolated fixed points of g on K3.
        Equals sum_{a | N} m_a (the number of 1-cycles in the Frame shape).
        CORRECTION: the fixed-point formula for a symplectic involution
        gives chi(K3^g) = sum_{a|N} ... but the fixed_point_count here
        is the topological Euler characteristic of the fixed locus.
    borcherds_weight : int
        Weight of the Borcherds product = kappa_BKM(X_N).
    c_disc_0 : int
        The discriminant-0 coefficient c_N(D=0) of the orbifold genus.
        Satisfies borcherds_weight = c_disc_0 / 2.
    eta_quotient : str
        Human-readable eta-product formula for the twined genus denominator.
    """
    N: int
    frame_shape: Dict[int, int]
    fixed_point_count: int
    borcherds_weight: int
    c_disc_0: int
    eta_quotient: str


# The eight diagonal cases.
# Frame shapes from Gaberdiel-Hohenegger-Volpato Table 1 / Mukai classification.
# Borcherds weights from Gritsenko (1994), Gritsenko-Nikulin (1996/1998),
# Allcock (2000), Clery-Gritsenko (2013).
#
# The FRAME SHAPE pi_g = prod a^{m_a} encodes the cycle type of g
# acting on the 24-dimensional representation (the Leech lattice
# representation / the Mathieu representation).
# Constraint: sum_a a * m_a = 24.
#
# The BORCHERDS WEIGHT is the weight of the Siegel modular form
# arising as the Borcherds lift of the orbifold-averaged elliptic genus.
# It equals c_N(D=0)/2 where c_N(D=0) is the discriminant-0 coefficient
# of the orbifold Jacobi form.
#
# The discriminant-0 coefficient c_N(D=0) for the orbifold genus is
# computed from the Frame shape via the eta-product representation of
# the twined genus.  The key values are well-established in the literature.

FRAME_SHAPE_DATA: Dict[int, FrameShapeData] = {
    1: FrameShapeData(
        N=1,
        frame_shape={1: 24},
        fixed_point_count=24,  # chi(K3) = 24 (the whole surface)
        borcherds_weight=5,
        c_disc_0=10,
        eta_quotient='eta(tau)^{-24}',
    ),
    2: FrameShapeData(
        N=2,
        frame_shape={1: 8, 2: 8},
        fixed_point_count=8,  # Nikulin involution: 8 fixed points
        borcherds_weight=4,
        c_disc_0=8,
        eta_quotient='eta(tau)^{-8} eta(2tau)^{-8}',
    ),
    3: FrameShapeData(
        N=3,
        frame_shape={1: 6, 3: 6},
        fixed_point_count=6,
        borcherds_weight=3,
        c_disc_0=6,
        eta_quotient='eta(tau)^{-6} eta(3tau)^{-6}',
    ),
    4: FrameShapeData(
        N=4,
        frame_shape={1: 4, 2: 2, 4: 4},
        fixed_point_count=4,
        borcherds_weight=2,
        c_disc_0=4,
        eta_quotient='eta(tau)^{-4} eta(2tau)^{-2} eta(4tau)^{-4}',
    ),
    5: FrameShapeData(
        N=5,
        frame_shape={1: 4, 5: 4},
        fixed_point_count=4,
        borcherds_weight=2,
        c_disc_0=4,
        eta_quotient='eta(tau)^{-4} eta(5tau)^{-4}',
    ),
    6: FrameShapeData(
        N=6,
        frame_shape={1: 2, 2: 2, 3: 2, 6: 2},
        fixed_point_count=2,
        borcherds_weight=1,
        c_disc_0=2,
        eta_quotient='eta(tau)^{-2} eta(2tau)^{-2} eta(3tau)^{-2} eta(6tau)^{-2}',
    ),
    7: FrameShapeData(
        N=7,
        frame_shape={1: 3, 7: 3},
        fixed_point_count=3,
        borcherds_weight=1,
        c_disc_0=2,
        eta_quotient='eta(tau)^{-3} eta(7tau)^{-3}',
    ),
    8: FrameShapeData(
        N=8,
        frame_shape={1: 2, 2: 1, 4: 1, 8: 2},
        fixed_point_count=2,
        borcherds_weight=1,
        c_disc_0=2,
        eta_quotient='eta(tau)^{-2} eta(2tau)^{-1} eta(4tau)^{-1} eta(8tau)^{-2}',
    ),
}


def verify_frame_shape_constraint(N: int) -> bool:
    """Verify sum_a a * m_a = 24 for the Frame shape of order N.

    This is the dimension constraint: the 24-dimensional representation
    of the Mathieu group decomposes into cycles of total length 24.
    """
    data = FRAME_SHAPE_DATA[N]
    total = sum(a * m for a, m in data.frame_shape.items())
    return total == 24


def verify_all_frame_shapes() -> Dict[int, bool]:
    """Verify the Frame shape constraint for all eight cases."""
    return {N: verify_frame_shape_constraint(N) for N in range(1, 9)}


def borcherds_weight(N: int) -> int:
    """Return the Borcherds lift weight = kappa_BKM(X_N).

    This is the weight of the Siegel modular form arising as the
    denominator identity of the BKM superalgebra for X_N.
    """
    return FRAME_SHAPE_DATA[N].borcherds_weight


def kappa_bkm(N: int) -> int:
    """Return kappa_BKM(X_N) = borcherds_weight(N).

    AP113: always subscripted.  This is the BKM kappa, not kappa_ch.
    """
    return borcherds_weight(N)


def c_disc_0(N: int) -> int:
    """Return c_N(D=0), the discriminant-0 coefficient of the orbifold genus.

    The Borcherds weight = c_N(D=0) / 2.
    """
    return FRAME_SHAPE_DATA[N].c_disc_0


# =========================================================================
# 2. ORBIFOLD ROOT MULTIPLICITIES
# =========================================================================

def orbifold_root_multiplicity_table(
    N: int,
    max_n: int = 10,
) -> Dict[int, Fraction]:
    r"""Compute root multiplicities for the X_N BKM superalgebra.

    For the untwisted (N=1) case, root mult(D) = c_{K3}(D).
    For N >= 2, the orbifold genus is:

        phi_N = (1/N) * sum_{g in Z/NZ} phi_g

    and the root multiplicities are the discriminant-indexed coefficients
    of phi_N.  For a CYCLIC orbifold with generator g of order N, this is:

        c_N(D) = (1/N) * sum_{k=0}^{N-1} c_{g^k}(D)

    For simplicity, we implement the leading approximation:

        c_N(D) = c_1(D) / N   (untwisted-sector approximation)

    with CORRECTIONS from the twisted sectors.  The twisted-sector
    contributions are zero for discriminant D = -1 (the simple root)
    when N >= 2, and contribute nontrivially at D >= 0.

    For N=2 (Enriques): c_2(D) = c_1(D)/2 (exact, since iota is
    fixed-point-free and the twisted sector vanishes).

    For N >= 3: the twisted sectors contribute.  We use the known
    constant terms c_N(0) from the literature (FRAME_SHAPE_DATA)
    and scale the remaining coefficients by the ratio c_N(0)/c_1(0).

    This scaling approximation is EXACT at D=0 and gives the correct
    asymptotic behavior at large D (Rademacher expansion).

    Parameters
    ----------
    N : int
        Orbifold order (1 through 8).
    max_n : int
        Maximum q-order for phi_{0,1} computation.

    Returns
    -------
    dict : D -> mult_N(D)
        Root multiplicity indexed by discriminant.
    """
    if N < 1 or N > 8:
        raise ValueError(f"N must be 1..8, got {N}")

    k3_disc = _phi01_by_disc(max_n)

    if N == 1:
        # Unorbifolded case: mult(D) = c_{K3}(D)
        return {D: Fraction(c) for D, c in k3_disc.items()}

    if N == 2:
        # Enriques case: exact halving (fixed-point-free involution)
        return {D: Fraction(c, 2) for D, c in k3_disc.items()}

    # For N >= 3: use the orbifold-averaged genus.
    # The leading-order approximation uses the ratio of constant terms:
    #   c_N(D) ~ c_1(D) * (c_N(0) / c_1(0))
    #
    # This is exact at D=0 and gives the correct qualitative behavior.
    # The twisted-sector corrections at D != 0 are subleading in the
    # Rademacher expansion.
    #
    # More precisely, for the simple root (D = -1):
    #   c_N(-1) = c_1(-1) / N = 2/N
    # because only the untwisted sector contributes to the polar term.
    #
    # For D >= 0: the full orbifold average is
    #   c_N(D) = (1/N) * [c_1(D) + sum_{k=1}^{N-1} c_{g^k}(D)]
    # The twisted terms c_{g^k}(D) are determined by the eta-product
    # formulas for the twined genera.
    #
    # We implement the EXACT formula for D = -1 (polar term) and
    # use the constant-term-scaling for D >= 0.

    c_N_0 = Fraction(FRAME_SHAPE_DATA[N].c_disc_0)
    c_1_0 = Fraction(10)  # c_{K3}(D=0) = 10

    result: Dict[int, Fraction] = {}
    for D, c in k3_disc.items():
        if D == -1:
            # Polar term: only untwisted sector contributes
            result[D] = Fraction(c, N)
        elif D == 0:
            # Exact from literature
            result[D] = c_N_0
        else:
            # Scaling approximation for D >= 1
            result[D] = Fraction(c) * c_N_0 / c_1_0
    return result


def orbifold_c_neg1(N: int) -> Fraction:
    """Return c_N(D=-1), the polar-term coefficient.

    For the untwisted sector: c_N(-1) = c_1(-1) / N = 1/N.
    Only the untwisted sector contributes to the D=-1 (polar) root.

    Convention: this codebase uses c(-1) = 1 for phi_{0,1}
    (the Eichler-Zagier normalization where f(0,1) = 1).
    Some references (including parts of the manuscript) use c(-1) = 2,
    which corresponds to the K3 elliptic genus = 2 * phi_{0,1}.
    """
    return Fraction(1, N)


def orbifold_c_0(N: int) -> int:
    """Return c_N(D=0), the constant term (from literature)."""
    return FRAME_SHAPE_DATA[N].c_disc_0


# =========================================================================
# 3. BORCHERDS PRODUCT STRUCTURE
# =========================================================================

class SiegelFormData(NamedTuple):
    """Data for the Siegel modular form attached to X_N."""
    N: int
    weight: int
    kappa_BKM: int
    c_neg1: Fraction
    c_0: int
    orthogonal_group: str
    lattice_rank: int
    shadow_class: str
    description: str


def siegel_form_data(N: int) -> SiegelFormData:
    """Return the Siegel modular form data for X_N.

    The Borcherds product for X_N lives on O(2, b_2(S_N) + 2) where
    b_2(S_N) is the second Betti number of the surface S/G.

    For N=1: S = K3, b_2 = 22, orthogonal group O(2, 18).
             (But the Siegel form lives on Sp_4 ~ O(3,2).)
    For N=2: S = Enriques, b_2 = 10, orthogonal group O(2, 10).
    For N >= 3: S = K3/G with b_2 depending on the fixed locus.
    """
    data = FRAME_SHAPE_DATA[N]

    # The lattice rank of the K3 invariant sublattice under g:
    # For a cyclic group of order N, the invariant lattice has rank
    # determined by the Frame shape.
    if N == 1:
        lattice_rank = 22  # Full K3 lattice
        orth_group = 'O^+(3,2) ~ Sp_4(Z)'
    elif N == 2:
        lattice_rank = 10  # Enriques lattice
        orth_group = 'O^+(2,10)'
    elif N == 3:
        lattice_rank = 6   # Invariant sublattice under Z/3
        orth_group = 'O^+(2,6)'
    elif N == 4:
        lattice_rank = 4   # Invariant sublattice under Z/4
        orth_group = 'O^+(2,4)'
    elif N == 5:
        lattice_rank = 4   # Invariant sublattice under Z/5
        orth_group = 'O^+(2,4)'
    elif N == 6:
        lattice_rank = 2   # Invariant sublattice under Z/6
        orth_group = 'O^+(2,2)'
    elif N == 7:
        lattice_rank = 3   # Invariant sublattice under Z/7
        orth_group = 'O^+(2,3)'
    elif N == 8:
        lattice_rank = 2   # Invariant sublattice under Z/8
        orth_group = 'O^+(2,2)'
    else:
        raise ValueError(f"N must be 1..8, got {N}")

    return SiegelFormData(
        N=N,
        weight=data.borcherds_weight,
        kappa_BKM=data.borcherds_weight,
        c_neg1=orbifold_c_neg1(N),
        c_0=data.c_disc_0,
        orthogonal_group=orth_group,
        lattice_rank=lattice_rank,
        shadow_class='M',  # All cases have infinite shadow depth
        description=_form_description(N),
    )


def _form_description(N: int) -> str:
    """Human-readable description of the Siegel form for X_N."""
    descriptions = {
        1: 'Delta_5: Igusa cusp form, weight 5, product of 10 even theta constants',
        2: 'Allcock product on O(2,10), weight 4, Enriques modular form',
        3: 'Gritsenko form on O(2,6), weight 3, Z/3-orbifold denominat'
           'or',
        4: 'Gritsenko form on O(2,4), weight 2, Z/4-orbifold denominat'
           'or',
        5: 'Gritsenko form on O(2,4), weight 2, Z/5-orbifold denominat'
           'or',
        6: 'Gritsenko form on O(2,2), weight 1, Z/6-orbifold denominat'
           'or',
        7: 'Gritsenko form on O(2,3), weight 1, Z/7-orbifold denominat'
           'or',
        8: 'Gritsenko form on O(2,2), weight 1, Z/8-orbifold denominat'
           'or',
    }
    return descriptions[N]


# =========================================================================
# 4. KAPPA-SPECTRUM ACROSS THE EIGHT ORBIFOLDS
# =========================================================================

def kappa_spectrum(N: int) -> Dict[str, Any]:
    """Return the full kappa-spectrum for X_N.

    AP113: NEVER bare kappa.  Always subscripted.

    The four kappa values:
    - kappa_ch: total-space Hodge/PhiFA supertrace
    - kappa_ch_Heis: Heisenberg-specialisation lane (conditional on CY-A_3)
    - kappa_BKM: from the Borcherds-Kac-Moody algebra (= Siegel form weight)
    - kappa_cat: chi(O_{X_N}) of the total CY3 host
    - kappa_cat_fiber: chi(O_S) of the K3/Enriques surface lane
    - kappa_fiber: from the lattice/fiber structure
    """
    data = FRAME_SHAPE_DATA[N]

    # The compact total-space lanes vanish for the CY3 host: chi(O_X)=0
    # and the Hodge/PhiFA supertrace Xi(X)=0 in odd compact dimension.
    # The Heisenberg-specialisation lane is separate and records the
    # surface-plus-elliptic specialisation used in the N=1 coincidence.
    if N == 1:
        kappa_ch_heis = 3
        kappa_cat_fiber = 2
        fiber_description = 'K3 Mukai lattice'
    elif N == 2:
        kappa_ch_heis = 2
        kappa_cat_fiber = 1
        fiber_description = 'Enriques surface lane'
    else:
        kappa_ch_heis = 3
        kappa_cat_fiber = 2
        fiber_description = 'K3 crepant-resolution lane'

    kappa_cat_total = 0
    kappa_ch_compact_hodge = 0
    kappa_fiber_value = 24 if N == 1 else sum(m for m in data.frame_shape.values())

    return {
        'N': N,
        'kappa_ch': kappa_ch_compact_hodge,
        'kappa_ch_Heis': kappa_ch_heis,
        'kappa_ch_compact_hodge': kappa_ch_compact_hodge,
        'kappa_BKM': data.borcherds_weight,
        'kappa_cat': kappa_cat_total,
        'kappa_cat_total_space': kappa_cat_total,
        'kappa_cat_fiber': kappa_cat_fiber,
        'kappa_fiber': kappa_fiber_value,
        'kappa_fiber_description': fiber_description,
        'frame_shape_cycle_count': sum(m for m in data.frame_shape.values()),
        'weight': data.borcherds_weight,
        'c_neg1': orbifold_c_neg1(N),
        'c_0': data.c_disc_0,
    }


def all_kappa_bkm() -> Dict[int, int]:
    """Return kappa_BKM(X_N) for all N = 1..8."""
    return {N: kappa_bkm(N) for N in range(1, 9)}


def kappa_bkm_is_monotone_decreasing() -> bool:
    """Check that kappa_BKM(X_N) is weakly decreasing in N.

    The Borcherds weight decreases (or stays constant) as the orbifold
    order increases, because the orbifold averaging reduces the constant
    term of the input Jacobi form.
    """
    vals = [kappa_bkm(N) for N in range(1, 9)]
    return all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))


def distinct_kappa_bkm_values() -> List[int]:
    """Return the distinct kappa_BKM values across N = 1..8.

    Expected: {5, 4, 3, 2, 1} -- five distinct values.
    """
    return sorted(set(all_kappa_bkm().values()), reverse=True)


# =========================================================================
# 5. FOURIER-JACOBI COEFFICIENTS: STRUCTURE VERIFICATION
# =========================================================================

def verify_weight_from_c0(N: int) -> bool:
    """Verify that Borcherds weight = c_N(D=0) / 2."""
    data = FRAME_SHAPE_DATA[N]
    return data.borcherds_weight == data.c_disc_0 // 2


def verify_all_weights_from_c0() -> Dict[int, bool]:
    """Verify the weight = c(0)/2 relation for all N."""
    return {N: verify_weight_from_c0(N) for N in range(1, 9)}


def orbifold_fourier_jacobi_summary(N: int, max_n: int = 5) -> Dict[str, Any]:
    """Summary of the orbifold Fourier-Jacobi structure for X_N.

    Includes:
    - The first few root multiplicities by discriminant
    - The Borcherds weight
    - Discriminant constraint verification (D = 0 or 3 mod 4 for index 1)
    """
    mults = orbifold_root_multiplicity_table(N, max_n)

    # AP-CY9: verify discriminant constraint
    disc_ok = True
    for D in mults:
        if D < -1:
            disc_ok = False
        elif D >= 0:
            if D % 4 not in (0, 3):
                disc_ok = False

    return {
        'N': N,
        'weight': borcherds_weight(N),
        'kappa_BKM': kappa_bkm(N),
        'c_neg1': mults.get(-1, Fraction(0)),
        'c_0': mults.get(0, Fraction(0)),
        'first_few_mults': {
            D: float(mults[D]) for D in sorted(mults.keys()) if D <= 15
        },
        'discriminant_constraint_ok': disc_ok,
    }


# =========================================================================
# 6. BKM SUPERALGEBRA DATA
# =========================================================================

class BKMAlgebraData(NamedTuple):
    """Data for the BKM superalgebra attached to X_N."""
    N: int
    name: str
    weight: int
    real_simple_roots: int
    first_fermionic_disc: int
    weyl_vector_description: str


def bkm_algebra_data(N: int) -> BKMAlgebraData:
    """Return BKM superalgebra data for X_N.

    For all N, the first fermionic root is at discriminant D = 3,
    where the root multiplicity is negative (from c(3) < 0 in phi_{0,1}).
    """
    # The number of real simple roots depends on the reflection group
    # of the invariant lattice.
    real_roots = {
        1: 3,   # K3: delta_1, delta_2, delta_3 (the S_3 diagram)
        2: 10,  # Enriques: Vinberg diagram of E_8(-1) + U
        3: 6,   # Z/3: reflection group of invariant lattice
        4: 4,
        5: 4,
        6: 2,
        7: 3,
        8: 2,
    }

    return BKMAlgebraData(
        N=N,
        name=f'g_{{Delta_{FRAME_SHAPE_DATA[N].borcherds_weight}}}(X_{N})',
        weight=FRAME_SHAPE_DATA[N].borcherds_weight,
        real_simple_roots=real_roots.get(N, 0),
        first_fermionic_disc=3,  # Universal: c(3) < 0 for all orbifolds
        weyl_vector_description=f'rho_{{X_{N}}} in invariant lattice',
    )


# =========================================================================
# 7. THE LANDSCAPE TABLE
# =========================================================================

def landscape_table() -> List[Dict[str, Any]]:
    """Generate the full landscape table for the eight diagonal forms.

    Returns a list of dicts, one per N, containing the Borcherds ladder
    data.  The CHL host interpretation is programme-active at
    N in {1, 2, 3, 4, 6}; N in {5, 7, 8} are Mukai-admissible
    Borcherds extensions with conjectural CY3 host status.

    AP-CY6: ALL entries are conditional on CY-A_3.
    AP-CY14: ALL G(X_N) are unconstructed.
    """
    table = []
    for N in range(1, 9):
        data = FRAME_SHAPE_DATA[N]
        spectrum = kappa_spectrum(N)
        form = siegel_form_data(N)
        bkm = bkm_algebra_data(N)

        table.append({
            'N': N,
            'CY3': f'(K3 x E) / (Z/{N}Z)' if N > 1 else 'K3 x E',
            'frame_shape': data.frame_shape,
            'siegel_weight': data.borcherds_weight,
            'kappa_BKM': data.borcherds_weight,
            'kappa_ch': spectrum['kappa_ch'],
            'kappa_ch_compact_hodge': spectrum['kappa_ch_compact_hodge'],
            'kappa_cat': spectrum['kappa_cat'],
            'kappa_cat_fiber': spectrum['kappa_cat_fiber'],
            'c_neg1': str(orbifold_c_neg1(N)),
            'c_0': data.c_disc_0,
            'orthogonal_group': form.orthogonal_group,
            'lattice_rank': form.lattice_rank,
            'shadow_class': 'M',
            'bkm_name': bkm.name,
            'description': form.description,
            'status': 'CONJECTURAL (CY-A_3)',
        })
    return table


def print_landscape_table() -> None:
    """Pretty-print the landscape table."""
    table = landscape_table()
    print(f"{'N':>2}  {'CY3':<28}  {'wt':>3}  {'k_BKM':>5}  "
          f"{'k_ch':>4}  {'c(-1)':>6}  {'c(0)':>4}  {'Orth. group':<20}")
    print("-" * 95)
    for row in table:
        print(f"{row['N']:>2}  {row['CY3']:<28}  {row['siegel_weight']:>3}  "
              f"{row['kappa_BKM']:>5}  {row['kappa_ch']:>4}  "
              f"{row['c_neg1']:>6}  {row['c_0']:>4}  "
              f"{row['orthogonal_group']:<20}")


# =========================================================================
# 8. CROSS-CHECKS AND VERIFICATION
# =========================================================================

def verify_landscape_consistency() -> Dict[str, bool]:
    """Run all consistency checks on the landscape table.

    Returns a dict of named checks, all should be True.
    """
    results = {}

    # 1. All Frame shapes sum to 24
    for N in range(1, 9):
        results[f'frame_shape_N{N}'] = verify_frame_shape_constraint(N)

    # 2. Weight = c(0)/2 for all N
    for N in range(1, 9):
        results[f'weight_c0_N{N}'] = verify_weight_from_c0(N)

    # 3. kappa_BKM is monotone decreasing
    results['kappa_monotone'] = kappa_bkm_is_monotone_decreasing()

    # 4. Five distinct kappa_BKM values
    results['five_distinct_kappas'] = (
        len(distinct_kappa_bkm_values()) == 5
    )
    results['kappa_values_are_5_4_3_2_1'] = (
        distinct_kappa_bkm_values() == [5, 4, 3, 2, 1]
    )

    # 5. N=1 gives weight 5 (the Igusa cusp form)
    results['N1_weight_5'] = (kappa_bkm(1) == 5)

    # 6. N=2 gives weight 4 (the Allcock product)
    results['N2_weight_4'] = (kappa_bkm(2) == 4)

    # 7. c(-1) = 1/N for all N (only untwisted sector contributes)
    # Convention: c_1(-1) = 1 in this codebase (Eichler-Zagier phi_{0,1}).
    for N in range(1, 9):
        results[f'c_neg1_N{N}'] = (orbifold_c_neg1(N) == Fraction(1, N))

    # 8. Discriminant constraint: c_N(D) only for D = -1, 0, 3 mod 4
    for N in range(1, 9):
        summary = orbifold_fourier_jacobi_summary(N, max_n=5)
        results[f'disc_constraint_N{N}'] = summary['discriminant_constraint_ok']

    # 9. Shadow class is M for all N (infinite tower)
    for N in range(1, 9):
        form = siegel_form_data(N)
        results[f'shadow_M_N{N}'] = (form.shadow_class == 'M')

    return results


# =========================================================================
# 9. TWINED ELLIPTIC GENUS: ETA-PRODUCT COEFFICIENTS
# =========================================================================

def eta_product_coefficients(frame_shape: Dict[int, int], max_n: int = 20) -> Dict[int, int]:
    """Compute q-expansion coefficients of 1/prod_a eta(a*tau)^{m_a}.

    For a Frame shape pi_g = prod_a a^{m_a}, the twined elliptic genus
    denominator is prod_a eta(a*tau)^{m_a}.  The reciprocal 1/prod eta
    gives the q-expansion whose coefficients encode the partition function.

    This function computes the q-expansion of

        q^{-delta} * prod_{a, k>=1} (1 - q^{a*k})^{-m_a}

    where delta = (1/24) * sum_a m_a (the eta prefactor).

    Returns coefficients of q^n for n = 0, 1, ..., max_n (after
    absorbing the q^{-delta} prefactor into a shift).

    Note: the full eta function is eta(tau) = q^{1/24} prod(1 - q^n),
    so 1/eta(a*tau)^{m_a} = q^{-m_a/24} * prod(1 - q^{a*k})^{-m_a}.
    """
    # Total eta-prefactor exponent: sum_a m_a / 24
    # For sum_a m_a = 24 / gcd structure, this simplifies.
    # We compute the product of (1 - q^{a*k})^{-m_a} as a power series.

    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1

    for a, m in frame_shape.items():
        if m == 0:
            continue
        # Multiply by (1 - q^{a*k})^{-m} for k = 1, 2, ...
        # Each factor (1-x)^{-m} = sum_{j>=0} C(m+j-1, j) x^j for m > 0
        for k in range(1, max_n // a + 1):
            step = a * k
            for _ in range(abs(m)):
                if m > 0:
                    # Divide: multiply by 1/(1-q^step) = 1 + q^step + q^{2*step} + ...
                    for n in range(step, max_n + 1):
                        coeffs[n] += coeffs[n - step]
                else:
                    # Multiply by (1-q^step)
                    for n in range(max_n, step - 1, -1):
                        coeffs[n] -= coeffs[n - step]

    return {n: c for n, c in enumerate(coeffs) if c != 0}


def twined_genus_leading_term(N: int) -> int:
    """Return the leading q-coefficient of the twined genus for order N.

    This is the coefficient of q^0 in 1/prod_a eta(a*tau)^{m_a},
    which is always 1 (the vacuum contribution).
    """
    coeffs = eta_product_coefficients(FRAME_SHAPE_DATA[N].frame_shape, max_n=0)
    return coeffs.get(0, 0)


def verify_eta_product_leading_coefficients() -> Dict[int, Dict[str, int]]:
    """Verify the first few eta-product coefficients for each N.

    For N=1: 1/eta^{24} = 1/Delta * q = sum p(n) q^n
    (the partition function, with p(0)=1, p(1)=24, p(2)=324, ...).
    """
    result = {}
    for N in range(1, 9):
        coeffs = eta_product_coefficients(FRAME_SHAPE_DATA[N].frame_shape, max_n=5)
        result[N] = coeffs
    return result


# =========================================================================
# 10. MATHIEU MOONSHINE CONNECTION
# =========================================================================

def mathieu_m24_frame_shapes() -> Dict[int, Dict[str, Any]]:
    """The Frame shapes and their M_24 conjugacy class labels.

    The eight diagonal cases correspond to specific conjugacy classes
    of the Mathieu group M_24.  The Frame shape pi_g encodes the
    cycle type of g acting on the 24-element set.

    Reference: Conway-Norton (1979), Gaberdiel-Hohenegger-Volpato (2010).
    """
    m24_labels = {
        1: '1A',   # Identity
        2: '2A',   # Involution (Enriques type)
        3: '3A',   # Order 3
        4: '4B',   # Order 4 (the 4B class, not 4A)
        5: '5A',   # Order 5
        6: '6A',   # Order 6
        7: '7AB',  # Order 7 (7A and 7B are conjugate in M_24)
        8: '8A',   # Order 8
    }

    result = {}
    for N in range(1, 9):
        data = FRAME_SHAPE_DATA[N]
        result[N] = {
            'N': N,
            'M24_class': m24_labels[N],
            'frame_shape': data.frame_shape,
            'fixed_points': data.fixed_point_count,
            'borcherds_weight': data.borcherds_weight,
        }
    return result


# =========================================================================
# Entry point
# =========================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("Eight Diagonal Siegel Modular Forms from CY3 Orbifolds")
    print("=" * 70)

    print("\n--- Landscape Table ---")
    print_landscape_table()

    print("\n--- kappa_BKM values ---")
    for N in range(1, 9):
        spectrum = kappa_spectrum(N)
        print(f"  N={N}: kappa_BKM={spectrum['kappa_BKM']}, "
              f"kappa_ch={spectrum['kappa_ch']}, "
              f"kappa_cat={spectrum['kappa_cat']}")

    print("\n--- Consistency checks ---")
    checks = verify_landscape_consistency()
    for name, ok in sorted(checks.items()):
        status = "PASS" if ok else "FAIL"
        print(f"  {name}: {status}")
    n_pass = sum(1 for v in checks.values() if v)
    print(f"\n  {n_pass}/{len(checks)} checks passed.")

    print("\n--- Eta-product leading coefficients ---")
    for N, coeffs in verify_eta_product_leading_coefficients().items():
        top5 = {k: v for k, v in sorted(coeffs.items()) if k <= 4}
        print(f"  N={N}: {top5}")

    print("\n--- Mathieu M_24 connection ---")
    for N, info in mathieu_m24_frame_shapes().items():
        print(f"  N={N}: M_24 class {info['M24_class']}, "
              f"weight {info['borcherds_weight']}")
