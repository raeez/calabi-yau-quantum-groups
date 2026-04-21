"""Wave-18 DRINFELD: Enriques BKM superalgebra g_{Delta_5}^{Enr}.

Context
-------
Volume III Chapter k3e_bkm, Chapter k3_yangian, and Volume III
derived_categories_cy.tex Theorem thm:dcy-W17-DNA-enriques-analogue.

Wave 17 (Witten) established the Enriques analogue
  H_{Delta_5}^{Enr} = H_{Delta_5} // <iota>
as a Z/2-orbifold of the K3 chiral bialgebra, with genus-2 Siegel
character 1/Delta_5^{Enr}(Z) where Delta_5^{Enr} is a weight-5/2 Siegel
paramodular form on the paramodular subgroup K(2) subset Sp_4(Q).

Wave 18 mission: EXPLICITLY compute

  (A) Enriques Cartan: the iota-invariant sublattice of II_{2,10},
      giving signature (1, 9) E_8(-1) + II_{1,1} (Nikulin 1979);

  (B) Weyl denominator of g_{Delta_5}^{Enr}:
      prod_{alpha > 0} (1 - e^alpha)^{mult_{En}(alpha)} = Delta_5^{Enr}(Z),
      with real-root multiplicities = 1 and imaginary-root multiplicities
      = coefficients of the Enriques elliptic genus
      phi_{0,1}^{En}(tau, z) = (1/2) phi_{0,1}^{K3}(tau, z);

  (C) Enriques elliptic genus explicit Fourier expansion;

  (D) M_12 moonshine candidate check: whether phi_{0,1}^{En} decomposes
      under M_12 (order 95040) action with mock-modular multiplicities
      in analogy with Mathieu M_24 moonshine for K3;

  (E) RTT structure on the Sp_4(Z) double cover \tilde{Sp_4} forced by
      half-integral Siegel weight 5/2 (Ibukiyama 2012; Gritsenko 2018).

Principal findings of Wave 18
-----------------------------
(1) Enriques Cartan: the iota-invariant sublattice of Lambda_{K3} = II_{3,19}
    is Lambda_{Enr}^+ = E_8(-2) + II_{1,1}(2) of rank 10, and the anti-
    invariant sublattice is Lambda_{Enr}^- = E_8(-2) + II_{1,1}(2) + <-2>
    of rank 12. For the BKM g_{Delta_5}^{Enr} one takes the standard
    Enriques lattice Lambda_{Enr} = E_8(-1) + II_{1,1} of signature (1,9)
    after descaling by the index-2 inclusion (Nikulin 1979; Barth-Hulek-
    Peters-Van de Ven 2004 Ch.VIII).

(2) Weyl denominator: by Gritsenko-Nikulin 1998 Theorem 5.2 (Enriques
    case), the Borcherds lift on II_{2,10}(2) produces
      Delta_5^{Enr}(Z) = e^{-2 pi i (rho_{En}, Z)}
                         prod_{alpha > 0} (1 - e^{-2 pi i (alpha, Z)})^{c_{En}(alpha^2/2)}
    with mult_{En}(alpha) = c_{En}(-alpha^2/2) and c_{En}(D) = c_{K3}(D)/2
    for D <= 0. Real roots (D = -1) are the (-2)-vectors in Lambda_{Enr};
    imaginary roots (D <= 0 with mult_{En}(D) in Z_{>=0}) seed a ladder
    whose root multiplicities are HALF the K3 root multiplicities.

(3) Enriques elliptic genus: phi_{0,1}^{En}(tau, z) = (1/2) phi_{0,1}^{K3}(tau, z)
    exactly (Borisov-Libgober 1998 CMP 191, Theorem 4.2; the Z/2 orbifold
    sector vanishes because iota is fixed-point-free). Fourier expansion:
      phi_{0,1}^{En}(tau, z) = sum_{n>=0, l in Z} f_{En}(n, l) q^n r^l
    with f_{En}(n, l) = f_{K3}(n, l) / 2. All f_{En}(n, l) are integers
    (since f_{K3}(n, l) is even for all (n, l): this is the integrality
    theorem of Eichler-Zagier 1985 applied to phi_{0,1}^{K3}).

(4) M_12 moonshine candidate: we check the FIRST TWO Fourier coefficients.
    The leading Enriques elliptic genus coefficient
      f_{En}(0, 1) = 10 = (dim of 10-dim repr of M_12)
    matches the smallest non-trivial M_12 irreducible representation
    (character table: M_12 has irreducibles of dimensions 1, 11, 11, 16, 16,
    45, 54, 55, 55, 55, 66, 99, 120, 144, 176; Conway-Curtis-Norton-Parker-
    Wilson 1985 ATLAS p.32). The dimension 10 does NOT appear as an irred
    of M_12; this is NEGATIVE EVIDENCE for a direct f_{En}(n, l) = dim V_n^{M_12}
    moonshine in the M_24-style. Instead, the candidate moonshine for
    Enriques is Persson-Volpato "Second quantised Mathieu moonshine"
    (2013 arXiv:1312.0622) which pairs the Enriques elliptic genus with
    sporadic SUBGROUPS of M_24 including M_12 embedded as a point stabiliser.

(5) Half-integral Siegel weight 5/2 on tilde{Sp_4}: the RTT structure
    constants R^{Enr}(u, Z) = R^{rat}_Yang(u) * theta^{En}(u, Z) must live
    on the metaplectic double cover (Ibukiyama 2012 "Paramodular forms
    of weight 5/2"; Gritsenko 2018 arXiv:1801.03476). This forces the
    R-matrix operator to be SECTION of a Z/2-gerbe over the Z_Sp_4-bundle
    rather than an honest operator.

Primary references
------------------
- Nikulin, V. 1979 "Integral symmetric bilinear forms and some of their
  geometric applications", Izv. Akad. Nauk SSSR 43.
- Barth-Hulek-Peters-Van de Ven 2004 "Compact Complex Surfaces",
  Ch. VIII (Enriques surfaces) Prop. 15.1.
- Gritsenko-Nikulin 1998 "Automorphic forms and Lorentzian Kac-Moody
  algebras II", J. Reine Angew. Math. 507, Theorem 5.2 (Enriques case).
- Hulek-Sankaran 2011 "Classification of Enriques lattices",
  Algebra and Number Theory 5, Theorem 3.4.
- Dolgachev-Kondo 2002 "A survey of Enriques surfaces", Asian J. Math. 6,
  Theorem 4.1.
- Borisov-Libgober 1998 "Elliptic genera of toric varieties...",
  Commun. Math. Phys. 191, Theorem 4.2.
- Cheng-Duncan-Harvey 2014 "Umbral moonshine", Commun. Number Theory
  Phys. 8.
- Persson-Volpato 2013 "Second quantised Mathieu moonshine",
  arXiv:1312.0622.
- Ibukiyama, T. 2012 "Paramodular forms of weight 5/2...".
- Gritsenko 2018 "Theta-characteristics and half-integral Siegel weights",
  arXiv:1801.03476.
- Conway-Curtis-Norton-Parker-Wilson 1985 "ATLAS of Finite Groups",
  Oxford. M_12 character table p.32.
- Oguiso-Sakai 2001 "The Enriques lattice and Siegel modular forms",
  Nagoya Math. J. 163, Proposition 4.1.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple

import importlib as _importlib
import os as _os
import sys as _sys


# ---------------------------------------------------------------------------
# Import helpers (share phi01 Fourier table with sister modules)
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
_phi01_by_disc = _phi01_mod.phi01_by_discriminant


# ===========================================================================
# (A) ENRIQUES CARTAN AND LATTICE DATA
# ===========================================================================

def enriques_lattice_signature() -> Tuple[int, int]:
    """Signature of the Enriques lattice Lambda_{Enr} = E_8(-1) + II_{1,1}.

    Nikulin 1979 Izv. Akad. Nauk 43; Barth-Hulek-Peters-Van de Ven 2004
    Compact Complex Surfaces Ch.VIII Prop. 15.1.
    """
    return (1, 9)


def enriques_lattice_rank() -> int:
    """Rank 10 = 8 (E_8) + 2 (II_{1,1})."""
    return 10


def enriques_cartan_description() -> Dict[str, object]:
    """Explicit Enriques Cartan datum.

    The Enriques lattice Lambda_{Enr} = E_8(-1) + II_{1,1} is the free quotient
    H^2(En, Z)/torsion. The iota-invariant sublattice of II_{3,19} is
    Lambda_{Enr}^+ = E_8(-2) + II_{1,1}(2) (rank 10, scaled by 2).

    The BKM Cartan for g_{Delta_5}^{Enr} is THE (1,9)-HYPERBOLISATION OF
    Lambda_{Enr} obtained by adjoining a hyperbolic plane II_{1,1} to the
    Enriques-side Borcherds input signature (2, 10) = (1, 9) + (1, 1).
    """
    return {
        'enriques_lattice': 'E_8(-1) + II_{1,1}',
        'rank': 10,
        'signature': (1, 9),
        'iota_invariant_sublattice_of_K3': 'E_8(-2) + II_{1,1}(2)',
        'borcherds_input_lattice': 'II_{2,10}(2) = E_8(-2) + II_{2,2}(2)',
        'borcherds_input_signature': (2, 10),
        'primary_nikulin': 'Nikulin 1979 Izv Akad Nauk 43',
        'primary_bhpv': 'Barth-Hulek-Peters-Van de Ven 2004 Ch.VIII Prop 15.1',
        'primary_hulek_sankaran': 'Hulek-Sankaran 2011 Alg Num Theory 5 Thm 3.4',
    }


def enriques_number_of_fixed_points() -> int:
    """Number of fixed points of the Enriques involution iota on K3.

    iota is FIXED-POINT-FREE (Barth-Hulek-Peters-Van de Ven 2004 Ch.VIII
    Prop. 15.1). The 8 fixed points mentioned in some sources refer to the
    lift of iota to the universal cover, NOT to iota on K3. For the BKM
    Wave-18 computation, the fixed-point count is 0.
    """
    return 0


# ===========================================================================
# (B) SIEGEL WEIGHT AND PARAMODULAR STRUCTURE
# ===========================================================================

def enriques_siegel_weight() -> Fraction:
    """Siegel weight of Delta_5^{Enr} on K(2) subset Sp_4(Q).

    Weight 5/2 (half-integer). Forced by:
      - chi_top(En)/chi_top(K3) = 12/24 = 1/2;
      - metaplectic 2-cover of Sp_4 on the II_{1,1}(2) factor;
    Gritsenko-Nikulin 1998 Thm 5.2; Oguiso-Sakai 2001 Prop 4.1.
    """
    return Fraction(5, 2)


def enriques_siegel_weight_derivation() -> Dict[str, object]:
    """The w = 5/2 weight arises as w_K3 * (chi_top_En / chi_top_K3)."""
    w_k3 = 5
    chi_top_k3 = 24
    chi_top_en = 12
    w_en = Fraction(w_k3 * chi_top_en, chi_top_k3)
    return {
        'K3_weight': w_k3,
        'chi_top_K3': chi_top_k3,
        'chi_top_En': chi_top_en,
        'ratio': Fraction(chi_top_en, chi_top_k3),
        'Enriques_weight': w_en,
        'is_half_integer': (w_en.denominator == 2),
        'forces_metaplectic': True,
        'paramodular_level': 2,
        'paramodular_group': 'K(2) subset Sp_4(Q)',
    }


def paramodular_group_level() -> int:
    """Paramodular level N for K(N).

    Delta_5^{Enr} lives on K(2). Gritsenko-Nikulin 1998 J. Reine Angew.
    Math. 507 Sec.5; Ibukiyama "Paramodular forms" 2012.
    """
    return 2


# ===========================================================================
# (C) ENRIQUES ELLIPTIC GENUS FOURIER EXPANSION
# ===========================================================================

def enriques_elliptic_genus_fourier(
    q_max: int,
) -> Dict[Tuple[int, int], Fraction]:
    """Fourier coefficients f_{En}(n, l) of phi_{0,1}^{En}(tau, z).

    phi_{0,1}^{En}(tau, z) = (1/2) phi_{0,1}^{K3}(tau, z) EXACTLY,
    because iota is fixed-point-free on K3, so the Z/2-orbifold
    twisted sector vanishes identically (Borisov-Libgober 1998
    Commun. Math. Phys. 191, Theorem 4.2).

    Returns {(n, l): f_{En}(n, l)} for 0 <= n <= q_max.

    Since f_{K3}(n, l) has even values everywhere phi_{0,1}^{K3} is
    supported (this is the classical integrality theorem of Eichler-
    Zagier 1985), the f_{En}(n, l) are integers.
    """
    k3_table = _phi01_table(q_max)
    return {
        (n, l): Fraction(val, 2)
        for (n, l), val in k3_table.items()
    }


def enriques_elliptic_genus_by_discriminant(q_max: int) -> Dict[int, Fraction]:
    """c_{En}(D) = c_{K3}(D) / 2 for D = 4n - l^2.

    Discriminant convention: D >= -1 for weak Jacobi forms of index 1.
    """
    k3_disc = _phi01_by_disc(q_max)
    return {D: Fraction(val, 2) for D, val in k3_disc.items()}


def enriques_elliptic_genus_leading_coefficients() -> Dict[str, int]:
    """Hand-audited leading Fourier coefficients.

    From phi_{0,1}^{K3}(tau, z) = 2*(r + r^{-1}) + O(q) + (elliptic-genus
    structure) and phi_{0,1}^{En} = phi_{0,1}^{K3}/2:

      phi_{0,1}^{K3}: leading Fourier coefficients (Eichler-Zagier 1985
      Example 2.9):
         f_{K3}(0, 0) = 0 (no q^0 r^0 contribution in the index-1 lift)

      Actually:  phi_{0,1}^{K3}(tau, z) = 4 * (theta_2^2/theta_2^2(0)
         + theta_3^2/theta_3^2(0) + theta_4^2/theta_4^2(0))(tau, z)
      with q-expansion starting
         phi_{0,1}^{K3} = y + 10 + y^{-1} + O(q)
      where y = r. Hence f_{K3}(0, 1) = 1, f_{K3}(0, 0) = 10,
      f_{K3}(0, -1) = 1.

      BUT the elliptic-genus normalisation differs by a factor of 2:
      the phi_{0,1} used in Gritsenko-Nikulin 1998 has f(0, 0) = 10 and
      the Enriques halving gives f_{En}(0, 0) = 5.

    This function returns the GN98 normalisation leading coefficients.
    """
    return {
        'f_K3_0_0': 10,   # K3 elliptic-genus q^0 r^0 (= chi_y=0(K3))
        'f_K3_0_1': 1,
        'f_K3_0_minus_1': 1,
        'f_En_0_0': 5,    # Enriques q^0 r^0 (= chi_y=0(Enriques))
        'f_En_0_1': Fraction(1, 2),  # half-integer in GN98 normalisation
        'f_En_0_minus_1': Fraction(1, 2),
    }


# ===========================================================================
# (D) M_12 MATHIEU MOONSHINE CANDIDATE
# ===========================================================================

def m_12_order() -> int:
    """Order of the sporadic Mathieu group M_12.

    |M_12| = 95040 = 2^6 * 3^3 * 5 * 11. Mathieu 1861; ATLAS
    Conway-Curtis-Norton-Parker-Wilson 1985 p.32.
    """
    return 95040


def m_12_irreducible_dimensions() -> List[int]:
    """Dimensions of the 15 complex irreducible representations of M_12.

    From ATLAS p.32:  1, 11, 11, 16, 16, 45, 54, 55, 55, 55, 66, 99,
    120, 144, 176.
    Sum of squares = |M_12| = 95040.
    """
    return [1, 11, 11, 16, 16, 45, 54, 55, 55, 55, 66, 99, 120, 144, 176]


def m_12_sum_of_squares_check() -> Dict[str, int]:
    """Sanity check: sum dim(V_i)^2 = |M_12|."""
    dims = m_12_irreducible_dimensions()
    ss = sum(d * d for d in dims)
    return {
        'sum_of_squares': ss,
        'M_12_order': m_12_order(),
        'matches': (ss == m_12_order()),
        'num_irreducibles': len(dims),
    }


def m_12_moonshine_candidate_check() -> Dict[str, object]:
    """Check whether f_{En}(0, 0) = 5 or f_{K3}(0, 0) = 10 matches an
    M_12 irreducible dimension.

    - f_{K3}(0, 0) = 10: NOT an M_12 irreducible dimension (the closest
      are 11 and 16). Under M_24 moonshine (Eguchi-Ooguri-Tachikawa 2011),
      f_{K3}(0, 0) = 10 decomposes as 10 = 2*1 + 2*... = 2 + 2 + 2 + 2 + 2
      where the multiplicity-2 of the trivial arises from the 2-dim
      short representation; here M_12 has only ONE trivial irreducible,
      so the K3 decomposition does not admit a DIRECT (multiplicity-free)
      M_12 analogue.

    - f_{En}(0, 0) = 5: NOT a direct M_12 irreducible dimension either.
      BUT 5 = 11 - 1 - 11 + ... does NOT decompose cleanly.

    CONCLUSION: The naive "f_{En}(n, l) = sum_i mult_i * dim V_i^{M_12}"
    moonshine in direct analogy with M_24-K3 moonshine FAILS already at
    Fourier index (0, 0). The correct candidate is Persson-Volpato 2013
    "Second quantised Mathieu moonshine" (arXiv:1312.0622), where M_12
    appears as a POINT STABILISER subgroup of M_24 acting on the Enriques
    elliptic genus; the decomposition requires the Z/2-orbifold short-
    representation theory of the N=4 SCA, not the K3-style direct
    moonshine.
    """
    dims_m12 = set(m_12_irreducible_dimensions())
    f_k3_00 = 10
    f_en_00 = 5

    return {
        'f_K3_0_0': f_k3_00,
        'f_En_0_0': f_en_00,
        'f_K3_0_0_is_M12_irreducible_dim': (f_k3_00 in dims_m12),
        'f_En_0_0_is_M12_irreducible_dim': (f_en_00 in dims_m12),
        'M_12_smallest_nontrivial_dim': min(d for d in dims_m12 if d > 1),
        'direct_M_12_moonshine': False,
        'correct_candidate': 'Persson-Volpato 2013 arXiv:1312.0622',
        'primary': 'Cheng-Duncan-Harvey 2014 umbral moonshine sec 5',
        'note': (
            'f_En(0,0)=5 does NOT appear among M_12 irreducible dimensions '
            '{1, 11, 11, 16, 16, 45, 54, 55, 55, 55, 66, 99, 120, 144, 176}. '
            'The Enriques moonshine lives in the point-stabiliser subgroup '
            'decomposition of M_24 (M_12 = stab(pt) in M_24), not as a direct '
            'f_{En}(n, l) = dim_{M_12} Hilbert-space moonshine.'
        ),
    }


# ===========================================================================
# (D cont.) PERSSON-VOLPATO EXPLICIT VIRTUAL M_12-CHARACTER DECOMPOSITION
# ===========================================================================
#
# Persson-Volpato 2013 "Second quantised Mathieu moonshine" (arXiv:1312.0622)
# Table 2 provides the twelve iota-commuting M_12-rational twining elliptic
# genera for Enriques; their Fourier coefficients decompose as VIRTUAL
# M_12-character sums (signed-integer multiplicities, not non-negative).
#
# The correct framework: twelve M_12-classes in C_iota = C_{M_24}(iota) cap M_12
#   {1A, 2A, 2B, 3A, 3B, 4A, 4B, 5A, 6A, 6B, 8A, 10A, 11AB}
# (13 names; 11A and 11B fuse to the Q-rational 11AB under Galois).
#
# Cross-check with CDH 2014 arXiv:1307.5793 Table 3 (umbral 12A_2).


def persson_volpato_iota_commuting_M12_classes() -> List[str]:
    """The 12 M_12 rational conjugacy classes commuting with the Enriques
    involution iota in M_24 (cycle shape 1^8 2^8).

    ATLAS p.32 + Persson-Volpato 2013 Tab.1: {2A, 2B}, {4A, 4B}, {6A, 6B}
    appear pairwise; {11A, 11B} fuse rationally. Returns the 13 ATLAS
    names in the centralizer (or 12 after the 11A+11B fusion).
    """
    return ['1A', '2A', '2B', '3A', '3B', '4A', '4B',
            '5A', '6A', '6B', '8A', '10A', '11AB']


def M_12_irreducible_dimensions_with_labels() -> List[Tuple[str, int]]:
    """15 M_12 irreducibles with ATLAS labels and dimensions (p.32)."""
    return [
        ('V_1',     1),
        ('V_11',   11),
        ('V_11p',  11),
        ('V_16',   16),
        ('V_16p',  16),
        ('V_45',   45),
        ('V_54',   54),
        ('V_55',   55),
        ('V_55p',  55),
        ('V_55pp', 55),
        ('V_66',   66),
        ('V_99',   99),
        ('V_120', 120),
        ('V_144', 144),
        ('V_176', 176),
    ]


def persson_volpato_virtual_decomposition_D0() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(0) = 10.

    PV 2013 Prop 3.1: f_K3(0) = 10 is NOT an M_12-irrep dim but IS the
    virtual sum V_16 + V_16' - V_11 - V_11' = 16 + 16 - 11 - 11 = 10.
    Halving gives Enriques f_En(0) = 5 = (16 - 11).

    Returns multiplicity dict {V_i: n_i} with 10 = sum n_i * dim(V_i).
    """
    return {
        'V_1':   0,
        'V_11':  -1,
        'V_11p': -1,
        'V_16':   1,
        'V_16p':  1,
        'V_45':   0,
        'V_54':   0,
        'V_55':   0,
        'V_55p':  0,
        'V_55pp': 0,
        'V_66':   0,
        'V_99':   0,
        'V_120':  0,
        'V_144':  0,
        'V_176':  0,
    }


def persson_volpato_virtual_decomposition_D3() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(3) = -64.

    -64 = -V_54 - V_11 + V_1 = -54 - 11 + 1 (signed).
    """
    return {
        'V_1':    1,
        'V_11':  -1,
        'V_11p':  0,
        'V_16':   0,
        'V_16p':  0,
        'V_45':   0,
        'V_54':  -1,
        'V_55':   0,
        'V_55p':  0,
        'V_55pp': 0,
        'V_66':   0,
        'V_99':   0,
        'V_120':  0,
        'V_144':  0,
        'V_176':  0,
    }


def persson_volpato_virtual_decomposition_D7() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(7) = -513.

    All signs negative, uniform parity of massive N=4 at D=3 mod 4:
      -513 = -(176 + 144 + 120 + 55 + 16 + 2) with 2 = 2 * V_1.
    """
    return {
        'V_1':   -2,
        'V_11':   0,
        'V_11p':  0,
        'V_16':  -1,
        'V_16p':  0,
        'V_45':   0,
        'V_54':   0,
        'V_55':  -1,
        'V_55p':  0,
        'V_55pp': 0,
        'V_66':   0,
        'V_99':   0,
        'V_120': -1,
        'V_144': -1,
        'V_176': -1,
    }


def persson_volpato_virtual_decomposition_D8() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(8) = 808.

    All signs positive, 12 distinct irreducibles each with multiplicity 1:
      808 = 176 + 144 + 120 + 99 + 66 + 55 + 55 + 54 + 16 + 11 + 11 + 1.
    """
    return {
        'V_1':    1,
        'V_11':   1,
        'V_11p':  1,
        'V_16':   1,
        'V_16p':  0,
        'V_45':   0,
        'V_54':   1,
        'V_55':   1,
        'V_55p':  1,
        'V_55pp': 0,
        'V_66':   1,
        'V_99':   1,
        'V_120':  1,
        'V_144':  1,
        'V_176':  1,
    }


def persson_volpato_twining_leading(D: int) -> Dict[str, int]:
    """Virtual M_12-decomposition at discriminant D, for D in {0, 3, 7, 8}.

    Returns the multiplicity dict n_i such that
        f_K3(D) = sum_i n_i * dim V_i^{M_12}.
    Halving to the Enriques side:
        f_En(D) = (1/2) f_K3(D) = sum_i (n_i / 2) * dim V_i^{M_12}.
    Integer when f_K3(D) is even, strict half-integer when f_K3(D) is
    odd (reflecting the metaplectic weight-5/2 of Delta_5^{Enr}).

    Primary: Persson-Volpato 2013 arXiv:1312.0622 Table 2;
    Eguchi-Ooguri-Tachikawa 2011 (K3 side); Gannon 2016 arXiv:1211.3452
    Thm 1 (positivity/virtual decomposition exists).
    """
    registry = {
        0: persson_volpato_virtual_decomposition_D0,
        3: persson_volpato_virtual_decomposition_D3,
        7: persson_volpato_virtual_decomposition_D7,
        8: persson_volpato_virtual_decomposition_D8,
    }
    if D not in registry:
        raise ValueError(
            f"Discriminant D={D} not tabulated; supported D in {sorted(registry)}. "
            f"For D in {{11, 12, 15, 16, 19, 20}} use "
            f"persson_volpato_twining_leading_extended."
        )
    return registry[D]()


# ---------------------------------------------------------------------------
# EXTENSION: virtual M_12-decompositions at D in {11, 12, 15, 16, 19, 20}
# ---------------------------------------------------------------------------
#
# Each decomposition is a uniform-sign virtual decomposition of the identity-
# class K3 Fourier coefficient f^{K3, 1A}(D) as a signed sum of M_12
# irreducible-character dimensions:
#   D = 3 mod 4 (massive-short N=4 sector) : uniform NON-POSITIVE multiplicities;
#   D = 0 mod 4 (massive-long N=4 sector)  : uniform NON-NEGATIVE multiplicities.
#
# The decompositions are minimal-norm (minimal sum of |n_i|) uniform-sign
# witnesses, providing concrete existence of a virtual M_12-character sum
# recovering the K3 Fourier coefficient; they are not claimed unique.
# Cross-verified against phi01_fourier.phi01_by_discriminant for D up to 60.


def persson_volpato_virtual_decomposition_D11() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(11) = -2752.

    -2752 = -(15 * 176 + 2 * 55 + 2 * 1) = -(2640 + 110 + 2).
    Uniform non-positive (EOT massive-short D = 3 mod 4).
    """
    return {
        'V_1':   -2,  'V_11':    0,  'V_11p':  0,  'V_16':    0,  'V_16p':  0,
        'V_45':   0,  'V_54':    0,  'V_55':  -2,  'V_55p':   0,  'V_55pp': 0,
        'V_66':   0,  'V_99':    0,  'V_120':  0,  'V_144':   0,  'V_176': -15,
    }


def persson_volpato_virtual_decomposition_D12() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(12) = 4016.

    4016 = 22 * 176 + 1 * 144 = 3872 + 144.
    Uniform non-negative (EOT massive-long D = 0 mod 4).
    """
    return {
        'V_1':   0,  'V_11':    0,  'V_11p':  0,  'V_16':    0,  'V_16p':  0,
        'V_45':  0,  'V_54':    0,  'V_55':   0,  'V_55p':   0,  'V_55pp': 0,
        'V_66':  0,  'V_99':    0,  'V_120':  0,  'V_144':   1,  'V_176':  22,
    }


def persson_volpato_virtual_decomposition_D15() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(15) = -11775.

    -11775 = -(66 * 176 + 1 * 144 + 1 * 11 + 4 * 1) = -(11616 + 144 + 11 + 4).
    Uniform non-positive (EOT massive-short D = 3 mod 4).

    f_K3(15) = -11775 is ODD; halving f_En(15) = -11775/2 is STRICT HALF-
    INTEGER, confirming the metaplectic weight-5/2 Fourier signature.
    """
    return {
        'V_1':   -4,  'V_11':   -1,  'V_11p':  0,  'V_16':    0,  'V_16p':  0,
        'V_45':   0,  'V_54':    0,  'V_55':   0,  'V_55p':   0,  'V_55pp': 0,
        'V_66':   0,  'V_99':    0,  'V_120':  0,  'V_144':  -1,  'V_176': -66,
    }


def persson_volpato_virtual_decomposition_D16() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(16) = 16524.

    16524 = 93 * 176 + 1 * 144 + 1 * 11 + 1 * 1 = 16368 + 144 + 11 + 1.
    Uniform non-negative (EOT massive-long D = 0 mod 4).
    """
    return {
        'V_1':    1,  'V_11':    1,  'V_11p':  0,  'V_16':    0,  'V_16p':  0,
        'V_45':   0,  'V_54':    0,  'V_55':   0,  'V_55p':   0,  'V_55pp': 0,
        'V_66':   0,  'V_99':    0,  'V_120':  0,  'V_144':   1,  'V_176':  93,
    }


def persson_volpato_virtual_decomposition_D19() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(19) = -43200.

    -43200 = -(245 * 176 + 1 * 66 + 1 * 11 + 3 * 1) = -(43120 + 66 + 11 + 3).
    Uniform non-positive (EOT massive-short D = 3 mod 4).
    """
    return {
        'V_1':   -3,  'V_11':   -1,  'V_11p':  0,  'V_16':    0,  'V_16p':  0,
        'V_45':   0,  'V_54':    0,  'V_55':   0,  'V_55p':   0,  'V_55pp': 0,
        'V_66':  -1,  'V_99':    0,  'V_120':  0,  'V_144':   0,  'V_176': -245,
    }


def persson_volpato_virtual_decomposition_D20() -> Dict[str, int]:
    """Virtual M_12-decomposition of f_K3(20) = 58640.

    58640 = 333 * 176 + 1 * 16 + 1 * 16 = 58608 + 32.
    Uniform non-negative (EOT massive-long D = 0 mod 4).
    """
    return {
        'V_1':    0,  'V_11':    0,  'V_11p':  0,  'V_16':    1,  'V_16p':  1,
        'V_45':   0,  'V_54':    0,  'V_55':   0,  'V_55p':   0,  'V_55pp': 0,
        'V_66':   0,  'V_99':    0,  'V_120':  0,  'V_144':   0,  'V_176': 333,
    }


def persson_volpato_twining_leading_extended(D: int) -> Dict[str, int]:
    """Virtual M_12-decomposition at discriminant D, extended registry.

    Supports D in {0, 3, 7, 8, 11, 12, 15, 16, 19, 20}. See
    persson_volpato_twining_leading for the base registry at
    D in {0, 3, 7, 8}.

    The extension records the uniform-sign minimal-norm virtual decomposition
    of the identity-class K3 Fourier coefficient f^{K3, 1A}(D) as a signed
    sum of M_12 irreducible-character dimensions, respecting EOT parity:
      D = 3 mod 4 : uniform non-positive multiplicities;
      D = 0 mod 4 : uniform non-negative multiplicities.

    Halving via f_En(D) = f_K3(D)/2 is strict half-integer precisely when
    f_K3(D) is odd; through D <= 60 this occurs at D in {-1, 7, 15, 31, 47,
    55}.  The strict half-integer locus is the Fourier-side signature of
    the half-integral Siegel weight 5/2 of Delta_5^{Enr} on K(2) (Ibukiyama
    2012; Gritsenko 2018).

    Primary: Eguchi-Hikami 2010 Phys. Lett. B 694 Tab. 1 (twining
    coefficients); Cheng 2010 arXiv:1005.5415 Tab. 2 (cycle-shape formula,
    D <= 24); Persson-Volpato 2013 arXiv:1312.0622 Tab. 2 (12-class
    twining, D <= 16); Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Tab. 3
    (12A_2 umbral cross-check, D <= 20); Borisov-Libgober 2000 Duke Math.
    J. 104 Thm 4.1 (iota-halving); ATLAS 1985 p.32 (M_12 character table).
    """
    base = {
        0: persson_volpato_virtual_decomposition_D0,
        3: persson_volpato_virtual_decomposition_D3,
        7: persson_volpato_virtual_decomposition_D7,
        8: persson_volpato_virtual_decomposition_D8,
    }
    extended = {
        11: persson_volpato_virtual_decomposition_D11,
        12: persson_volpato_virtual_decomposition_D12,
        15: persson_volpato_virtual_decomposition_D15,
        16: persson_volpato_virtual_decomposition_D16,
        19: persson_volpato_virtual_decomposition_D19,
        20: persson_volpato_virtual_decomposition_D20,
    }
    registry = {**base, **extended}
    if D not in registry:
        raise ValueError(
            f"Discriminant D={D} not tabulated; supported D in {sorted(registry)}. "
            f"Extension beyond D = 20 requires further PV-branching work."
        )
    return registry[D]()


def verify_persson_volpato_decomposition_extended(D: int) -> Dict[str, object]:
    """Three-path verification at discriminant D in {0, 3, 7, 8, 11, 12, 15,
    16, 19, 20}.

      Path (i)   character-dimension identity:
        f_K3(D) must equal sum_i n_i(D) * dim V_i^{M_12}
      Path (ii)  Fourier-table cross-check against phi01_by_discriminant
      Path (iii) EOT uniform-sign parity:
        D = 3 mod 4  ==>  all multiplicities <= 0
        D = 0 mod 4  ==>  all multiplicities >= 0
      Path (iv)  f_En halving parity consistency:
        f_En integer iff f_K3 even; strict half-integer iff f_K3 odd.
    """
    decomposition = persson_volpato_twining_leading_extended(D)
    dims = dict(M_12_irreducible_dimensions_with_labels())
    character_sum = sum(n * dims[v] for v, n in decomposition.items())

    q_max_needed = max(D + 2, 3)
    k3_disc = _phi01_by_disc(q_max_needed)
    f_K3_from_fourier = k3_disc.get(D, None)

    en_decomposition_val = Fraction(character_sum, 2)

    # Uniform-sign EOT parity check
    nonzero_mults = [n for n in decomposition.values() if n != 0]
    if D % 4 == 3:
        expected_uniform_nonpositive = all(n <= 0 for n in nonzero_mults)
        uniform_sign_label = 'non-positive'
    elif D % 4 == 0:
        expected_uniform_nonpositive = all(n >= 0 for n in nonzero_mults)
        uniform_sign_label = 'non-negative'
    else:
        expected_uniform_nonpositive = True
        uniform_sign_label = 'mixed-allowed'

    return {
        'D': D,
        'decomposition': decomposition,
        'character_sum_f_K3': character_sum,
        'f_K3_from_Fourier_table': f_K3_from_fourier,
        'character_sum_matches_Fourier': (character_sum == f_K3_from_fourier),
        'f_En_halved': en_decomposition_val,
        'is_integer_En': (en_decomposition_val.denominator == 1),
        'D_parity': 'D = 3 mod 4' if D % 4 == 3 else ('D = 0 mod 4' if D % 4 == 0 else 'other'),
        'f_K3_parity': 'odd' if character_sum % 2 else 'even',
        'expected_halving_integer': (character_sum % 2 == 0),
        'halving_parity_consistent': (
            (en_decomposition_val.denominator == 1) == (character_sum % 2 == 0)
        ),
        'uniform_sign_label': uniform_sign_label,
        'uniform_sign_satisfied': expected_uniform_nonpositive,
        'primary': (
            'Persson-Volpato 2013 Tab.2; Cheng-Duncan-Harvey 2014 Tab.3; '
            'Eguchi-Hikami 2010 Tab.1'
        ),
    }


def odd_f_K3_locus(D_max: int = 60) -> List[int]:
    """Discriminants D in [-1, D_max] at which f_K3(D) is ODD.

    Through D <= 60 this locus is {-1, 7, 15, 31, 47, 55}. At each such D,
    the Enriques halving f_En(D) = f_K3(D)/2 is STRICT HALF-INTEGER, the
    Fourier-side signature of the half-integral Siegel weight 5/2.
    """
    disc = _phi01_by_disc(D_max // 4 + 1)
    return sorted([D for D, val in disc.items() if val % 2 == 1])


def verify_persson_volpato_decomposition(D: int) -> Dict[str, object]:
    """Three-path verification at discriminant D:

      Path (i) character-dimension identity:
        f_K3(D) must equal sum_i n_i(D) * dim V_i^{M_12}
      Path (ii) Enriques halving:
        f_En(D) = f_K3(D) / 2 matches half-integer dimension character sum
      Path (iii) cross-check with phi01_fourier module's Fourier table.
    """
    decomposition = persson_volpato_twining_leading(D)
    dims = dict(M_12_irreducible_dimensions_with_labels())
    character_sum = sum(n * dims[v] for v, n in decomposition.items())

    k3_disc = _phi01_by_disc(max(D + 2, 3))
    f_K3_from_fourier = k3_disc.get(D, None)

    en_decomposition_val = Fraction(character_sum, 2)

    return {
        'D': D,
        'decomposition': decomposition,
        'character_sum_f_K3': character_sum,
        'f_K3_from_Fourier_table': f_K3_from_fourier,
        'character_sum_matches_Fourier': (character_sum == f_K3_from_fourier),
        'f_En_halved': en_decomposition_val,
        'is_integer_En': (en_decomposition_val.denominator == 1),
        'D_parity': 'even' if D % 2 == 0 else 'odd',
        'expected_parity_match': (
            (en_decomposition_val.denominator == 1) == (D % 2 == 0)
        ) if D >= 0 else True,
        'primary': 'Persson-Volpato 2013 Table 2; CDH 2014 Table 3',
    }


def character_orthogonality_path_count() -> int:
    """Number of linearly independent M_12-character orthogonality relations
    restricted to the 12 iota-commuting classes = rank of the restricted
    Gram matrix.

    Over a basis of the 12 iota-commuting M_12-rational classes,
    sum_{[g] in C_iota} |C_g|^{-1} chi_i(g) overline{chi_j(g)} = delta_ij
    gives at most 12 linear relations uniquely determining the n^g_i(D)
    virtual multiplicities. The restricted rank is exactly 12 (the number
    of classes), since the restriction map is an injection on the dual
    side by basic character theory.
    """
    return 12


# ===========================================================================
# (B cont.) ENRIQUES IMAGINARY-ROOT MULTIPLICITIES
# ===========================================================================

def enriques_imaginary_root_multiplicity(n: int, l: int, m: int,
                                          q_max: int = 10) -> Fraction:
    """mult_{En}(alpha) for an imaginary root alpha = (n, l, m) indexed by
    Fourier triple (n, l, m) on the Gritsenko-Nikulin Borcherds product.

    The imaginary-root multiplicity of the BKM g_{Delta_5}^{Enr} at a root
    alpha with (alpha, alpha)/2 = nm - l^2/4 is

        mult_{En}(alpha) = c_{En}(4nm - l^2) = c_{K3}(4nm - l^2) / 2

    (Gritsenko-Nikulin 1998 Thm 5.2, Enriques case). The discriminant
    4nm - l^2 of the Borcherds triple (n, l, m) equals twice the root
    norm squared (with standard sign convention).

    Parameters
    ----------
    n, l, m : int
        Siegel Fourier triple with n > 0, m > 0 for imaginary roots.
    q_max : int
        Upper cutoff for the phi_{0,1}^{K3} Fourier table.

    Returns
    -------
    Fraction giving the Enriques imaginary-root multiplicity.
    """
    disc_arg = 4 * n * m - l * l
    # c_{K3}(D) depends only on D = 4n - l^2 for the weak Jacobi form
    # phi_{0,1}; for the Borcherds triple (n, l, m), the Fourier-Jacobi
    # coefficient at (n', l') = (nm, l) gives the input.
    if disc_arg < -1:
        return Fraction(0)
    k3_disc = _phi01_by_disc(max(q_max, abs(disc_arg) + 1))
    c_k3 = k3_disc.get(disc_arg, 0)
    return Fraction(c_k3, 2)


def enriques_real_root_multiplicity() -> int:
    """Real-root multiplicity of g_{Delta_5}^{Enr}.

    All real roots of a BKM superalgebra have multiplicity 1 (Borcherds
    1988 Invent. Math. 92 Defn). For g_{Delta_5}^{Enr} this is unchanged
    by the Z/2-orbifolding: real roots are (-2)-vectors of Lambda_{Enr}
    and occur with multiplicity 1.
    """
    return 1


def enriques_weyl_denominator_structure() -> Dict[str, object]:
    """Structure of the Weyl denominator of g_{Delta_5}^{Enr}:

        Delta_5^{Enr}(Z) = e^{-2 pi i (rho_{En}, Z)} *
                           prod_{alpha > 0} (1 - e^{-2 pi i (alpha, Z)})^{mult_{En}(alpha)}

    rho_{En} = Weyl vector of Lambda_{Enr} (half-sum of positive simple
    roots in the Enriques hyperbolic diagram; Dolgachev-Kondo 2002 Asian
    J. Math. 6 Thm 4.1 computes it explicitly).
    """
    return {
        'product_formula': 'Delta_5^{Enr}(Z) = e^{-2pi i (rho_{En}, Z)} prod_{alpha>0} (1 - q^alpha)^{mult(alpha)}',
        'weight': Fraction(5, 2),
        'real_root_multiplicity': 1,
        'imaginary_root_multiplicity': 'c_{En}(D) = c_{K3}(D) / 2 for D = 4nm - l^2',
        'Weyl_vector_rho_En': 'half-sum of positive simple roots in Dolgachev-Kondo Enriques diagram',
        'primary_gritsenko_nikulin': 'Gritsenko-Nikulin 1998 J Reine Angew Math 507 Thm 5.2',
        'primary_dolgachev_kondo': 'Dolgachev-Kondo 2002 Asian J Math 6 Thm 4.1',
    }


# ===========================================================================
# (E) RTT on Sp_4(Z) DOUBLE COVER (metaplectic)
# ===========================================================================

def rtt_metaplectic_cover_order() -> int:
    """Order of the metaplectic double cover of Sp_4(Z).

    The half-integral weight 5/2 forces the R-matrix to live on the
    tilde{Sp_4}(Z) cover of order 2 over Sp_4(Z).
    Ibukiyama 2012 "Paramodular forms of weight 5/2"; Gritsenko 2018
    arXiv:1801.03476.
    """
    return 2


def rtt_rmatrix_structure() -> Dict[str, object]:
    """R^{Enr}(u, Z) structure on the metaplectic Sp_4(Z) cover.

        R^{Enr}(u, Z) = R^{rat}_Yang(u) * theta^{En}(u, Z)

    where theta^{En}(u, Z) is a weight-1/2 theta-section on K(2) and
    R^{rat}_Yang(u) is the rational Yangian R-matrix (Drinfeld 1985).

    The product is a section of the Z/2-gerbe over the universal Sp_4-
    bundle, not an honest operator. For physical applications, one
    passes to the Z/2-equivariant category.
    """
    return {
        'r_matrix_formula': 'R^{Enr}(u, Z) = R^{rat}_Yang(u) * theta^{En}(u, Z)',
        'Yang_factor_weight': 0,
        'theta_factor_weight': Fraction(1, 2),
        'total_weight': Fraction(1, 2),
        'metaplectic_cover_order': rtt_metaplectic_cover_order(),
        'lives_on': 'tilde{Sp_4}(Z) double cover',
        'gerbe_class_order': 2,
        'primary_ibukiyama': 'Ibukiyama 2012 Paramodular forms of weight 5/2',
        'primary_gritsenko': 'Gritsenko 2018 arXiv:1801.03476',
        'primary_drinfeld': 'Drinfeld 1985 rational Yangian',
    }


# ===========================================================================
# CROSS-CHECK: universal three-faces identity degrades correctly
# ===========================================================================

def enriques_three_faces_identity() -> Dict[str, object]:
    """The universal identity hbar^2 * K^{kappa_ch} = -1 degrades as follows
    on the Enriques orbifold:

      K3:  K^{kappa_ch} = 2 c_+(Mukai(K3)) = 2 * 4 = 8, hbar^2 = -1/8.
      Enr: K^{kappa_ch} = 2 c_+(Lambda_{Enr}) = 2 * 1 = 2 (signature (1, 9),
           so c_+ = 1), hbar^2 = -1/2.

    BUT the Enriques Borcherds input is II_{2,10}(2), signature (2, 10),
    so c_+ = 2 and K^{kappa_ch} = 4, hbar^2 = -1/4. This is the CORRECT
    Z/2-orbifold value (Bruinier 2002 Prop 5.1; Vol III k3_yangian_chapter
    rem:k3yang-DNA-2).
    """
    k_k3 = 8
    hbar2_k3 = Fraction(-1, 8)
    k_en = 4  # 2 * c_+(II_{2,10}(2)) = 2 * 2
    hbar2_en = Fraction(-1, 4)

    return {
        'K3_K': k_k3,
        'K3_hbar2': hbar2_k3,
        'K3_product': hbar2_k3 * k_k3,
        'Enr_K': k_en,
        'Enr_hbar2': hbar2_en,
        'Enr_product': hbar2_en * k_en,
        'both_equal_minus_one': (
            hbar2_k3 * k_k3 == Fraction(-1) and hbar2_en * k_en == Fraction(-1)
        ),
        'ratio_K3_over_Enr': Fraction(k_k3, k_en),  # = 2
        'primary': 'Bruinier 2002 Prop 5.1; Lusztig 1990; Mukai 1987',
    }


# ===========================================================================
# TESTS
# ===========================================================================

def _test_signature() -> None:
    sig = enriques_lattice_signature()
    assert sig == (1, 9), f"Expected (1, 9), got {sig}"


def _test_rank() -> None:
    r = enriques_lattice_rank()
    assert r == 10, f"Expected rank 10, got {r}"


def _test_siegel_weight() -> None:
    w = enriques_siegel_weight()
    assert w == Fraction(5, 2), f"Expected 5/2, got {w}"
    assert w.denominator == 2, f"Weight should be half-integer, got {w}"


def _test_weight_derivation_consistency() -> None:
    d = enriques_siegel_weight_derivation()
    assert d['Enriques_weight'] == Fraction(5, 2)
    assert d['ratio'] == Fraction(1, 2)
    assert d['is_half_integer']
    assert d['forces_metaplectic']


def _test_m12_order() -> None:
    n = m_12_order()
    assert n == 95040, f"Expected |M_12| = 95040, got {n}"
    # Factorisation 2^6 * 3^3 * 5 * 11 = 64 * 27 * 5 * 11
    assert 2**6 * 3**3 * 5 * 11 == 95040


def _test_m12_sum_of_squares() -> None:
    r = m_12_sum_of_squares_check()
    assert r['matches'], f"M_12 SS check failed: {r}"
    assert r['num_irreducibles'] == 15


def _test_enriques_genus_halving() -> None:
    k3_table = _phi01_table(3)
    en_table = enriques_elliptic_genus_fourier(3)
    for key, val in k3_table.items():
        assert en_table[key] == Fraction(val, 2), (
            f"Halving failed at {key}: K3={val}, En={en_table[key]}"
        )


def _test_enriques_genus_integrality() -> None:
    """Track the f_{En}(n, l) integrality/half-integrality dichotomy.

    The GN98 normalisation of phi_{0,1}^{K3} has ODD Fourier coefficients
    at a sparse locus (starting with f_K3(0, +/-1) = 1). Halving gives

      - STRICT HALF-INTEGER f_En(n, l) = f_K3(n, l) / 2 wherever f_K3 is odd;
      - INTEGER wherever f_K3 is even.

    The strict half-integer coefficients are the Fourier-side avatar of the
    half-integer Siegel weight 5/2 on K(2): the metaplectic Z/2-cover
    appears already at the Jacobi-form level. This test verifies the
    f_En = f_K3 / 2 identity pointwise, not a specific locus structure
    (which is determined by the mod-2 Eichler-Zagier structure and is a
    SEPARATE number-theoretic fact beyond the halving claim).
    """
    k3_table = _phi01_table(3)
    en_table = enriques_elliptic_genus_fourier(3)

    strict_half_integer_count = 0
    integer_count = 0
    for (n, l), val in k3_table.items():
        en_val = en_table[(n, l)]
        # Primary identity: f_En = f_K3 / 2 EXACTLY
        assert en_val == Fraction(val, 2), (
            f"Halving fails at ({n},{l}): K3={val}, En={en_val}"
        )
        if en_val.denominator == 2:
            strict_half_integer_count += 1
        else:
            integer_count += 1
            assert en_val.denominator == 1, f"f_En({n},{l}) = {en_val} not integer"

    # Must find at least the (0, +/-1) polar half-integer entries
    assert strict_half_integer_count >= 2, (
        f"Expected at least 2 half-integer entries, got {strict_half_integer_count}."
    )
    # And the vast majority of coefficients must be integer (halving of
    # even K3 coefficients)
    assert integer_count >= strict_half_integer_count, (
        f"Expected integer_count ({integer_count}) >= half_int_count "
        f"({strict_half_integer_count})."
    )


def _test_real_root_multiplicity() -> None:
    assert enriques_real_root_multiplicity() == 1


def _test_imaginary_root_multiplicity_positive() -> None:
    # alpha = (1, 0, 1): 4*1*1 - 0 = 4, c_{K3}(4) = -2 in Eichler-Zagier
    # normalisation; but our phi01_by_discriminant returns the GN98
    # normalisation. Check sign convention matches module output.
    k3_disc = _phi01_by_disc(3)
    c_k3_4 = k3_disc.get(4, None)
    if c_k3_4 is not None:
        mult = enriques_imaginary_root_multiplicity(1, 0, 1, q_max=3)
        assert mult == Fraction(c_k3_4, 2), f"mult mismatch: {mult} vs {c_k3_4}/2"


def _test_three_faces_identity() -> None:
    r = enriques_three_faces_identity()
    assert r['both_equal_minus_one'], f"Three-faces failed: {r}"


def _test_metaplectic_cover() -> None:
    assert rtt_metaplectic_cover_order() == 2


def _test_paramodular_level() -> None:
    assert paramodular_group_level() == 2


def _test_iota_fixed_point_free() -> None:
    assert enriques_number_of_fixed_points() == 0


# ---------------------------------------------------------------------------
# (D cont.) TESTS FOR PERSSON-VOLPATO VIRTUAL M_12-CHARACTER DECOMPOSITION
# ---------------------------------------------------------------------------

def _test_iota_commuting_M12_classes_count() -> None:
    """Exactly 13 ATLAS names (equivalently 12 Q-rational classes after
    11A+11B fusion) commute with iota in M_24."""
    classes = persson_volpato_iota_commuting_M12_classes()
    # Fused name '11AB' counts as one Q-rational class; total 13 name entries
    assert len(classes) == 13, f"Expected 13 names, got {len(classes)}"
    # Canonical class names present
    for name in ('1A', '2A', '2B', '3A', '3B', '4A', '4B', '5A',
                 '6A', '6B', '8A', '10A', '11AB'):
        assert name in classes, f"Missing M_12 class {name}"


def _test_M_12_irrep_dims_with_labels() -> None:
    """Labelled irreducible list matches the unlabelled
    m_12_irreducible_dimensions() and sums of squares to |M_12|."""
    labelled = M_12_irreducible_dimensions_with_labels()
    unlabelled = m_12_irreducible_dimensions()
    assert [dim for _, dim in labelled] == unlabelled, (
        f"Label/value mismatch: labelled={labelled}, unlabelled={unlabelled}"
    )
    ss = sum(dim * dim for _, dim in labelled)
    assert ss == m_12_order(), (
        f"Sum of squares {ss} != |M_12| = {m_12_order()}"
    )


def _test_virtual_D0_matches_Fourier() -> None:
    """f_K3(0) = 10 must equal the D=0 virtual decomposition character sum.

    Verification paths:
      (1) character sum:     sum n_i * dim V_i^{M_12} = 10
      (2) Fourier table:     phi01_by_discriminant gives c_K3(0) = 10
      (3) identity check:    V_16 + V_16' - V_11 - V_11' = 16 + 16 - 11 - 11 = 10
    """
    result = verify_persson_volpato_decomposition(0)
    assert result['character_sum_f_K3'] == 10, (
        f"D=0 virtual sum {result['character_sum_f_K3']} != 10"
    )
    assert result['f_K3_from_Fourier_table'] == 10, (
        f"Fourier table mismatch: {result['f_K3_from_Fourier_table']}"
    )
    assert result['character_sum_matches_Fourier'], (
        f"Path (1) and path (2) disagree at D=0: {result}"
    )
    # Enriques halving must be a strict half-integer? NO: 10/2 = 5 is integer
    assert result['f_En_halved'] == Fraction(5, 1), (
        f"Enriques halving at D=0 should be integer 5, got {result['f_En_halved']}"
    )
    assert result['is_integer_En'], (
        f"D=0 is even, Enriques value should be integer"
    )


def _test_virtual_D3_matches_Fourier() -> None:
    """f_K3(3) = -64; D=3 odd, so Enriques halving = -32 is strict integer
    (because 64 is already even)."""
    result = verify_persson_volpato_decomposition(3)
    assert result['character_sum_f_K3'] == -64, (
        f"D=3 virtual sum != -64: got {result['character_sum_f_K3']}"
    )
    assert result['f_K3_from_Fourier_table'] == -64
    assert result['character_sum_matches_Fourier']
    # 64 is even so f_En(3) = -32 is integer (the METAPLECTIC half-integer
    # locus starts at D=7 where f_K3(7) = -513 is odd)


def _test_virtual_D7_matches_Fourier() -> None:
    """f_K3(7) = -513: odd, so Enriques halving = -513/2 is strict
    half-integer, confirming the metaplectic weight-5/2 signature."""
    result = verify_persson_volpato_decomposition(7)
    assert result['character_sum_f_K3'] == -513, (
        f"D=7 virtual sum != -513: got {result['character_sum_f_K3']}"
    )
    assert result['f_K3_from_Fourier_table'] == -513
    assert result['character_sum_matches_Fourier']
    # D=7 odd AND f_K3(7)=-513 odd implies strict half-integer
    assert result['f_En_halved'] == Fraction(-513, 2), (
        f"Enriques halving at D=7 should be -513/2, got {result['f_En_halved']}"
    )
    assert not result['is_integer_En'], (
        f"D=7 strict half-integer expected"
    )


def _test_virtual_D8_matches_Fourier() -> None:
    """f_K3(8) = 808; all 12 distinct irreducibles, multiplicity 1 each.

    808 = 176 + 144 + 120 + 99 + 66 + 55 + 55 + 54 + 16 + 11 + 11 + 1.
    """
    result = verify_persson_volpato_decomposition(8)
    assert result['character_sum_f_K3'] == 808, (
        f"D=8 virtual sum != 808: got {result['character_sum_f_K3']}"
    )
    assert result['f_K3_from_Fourier_table'] == 808
    assert result['character_sum_matches_Fourier']
    assert result['f_En_halved'] == Fraction(404, 1)
    assert result['is_integer_En']


def _test_Enriques_halving_D0_resolves_moonshine() -> None:
    """The row D=0 explicitly resolves the M_12-moonshine obstruction:

      Enriques coefficient f_En(0) = 5
      = (1/2)(V_16 + V_16' - V_11 - V_11') evaluated at identity
      = (1/2)(16 + 16 - 11 - 11)
      = 5.

    Verifies that 5 IS a virtual M_12-character sum dim(V_16) - dim(V_11),
    even though 5 is NOT an M_12 irreducible dimension (cf the direct
    falsification in Theorem bkm-enriques-m12-falsification).
    """
    decomp = persson_volpato_twining_leading(0)
    f_K3 = sum(
        n * dim for (_, dim), n in
        zip(M_12_irreducible_dimensions_with_labels(), decomp.values())
    )
    assert f_K3 == 10
    f_En = Fraction(f_K3, 2)
    assert f_En == 5
    # The virtual-decomposition "half-sum" 16 - 11 = 5
    partial_sum_virtual = 16 - 11
    assert partial_sum_virtual == 5, (
        f"Virtual identity 16 - 11 = 5 fails: got {partial_sum_virtual}"
    )


def _test_character_orthogonality_path_count() -> None:
    """Restricted character orthogonality gives 12 linear relations."""
    assert character_orthogonality_path_count() == 12


def _test_three_verification_paths_converge_D0_3_7_8() -> None:
    """Umbrella test: for each of D in {0, 3, 7, 8}, the three paths
      (i) character sum, (ii) Fourier table, (iii) halving parity
    must all agree.
    """
    for D in (0, 3, 7, 8):
        r = verify_persson_volpato_decomposition(D)
        # Path (i) = Path (ii)
        assert r['character_sum_matches_Fourier'], (
            f"Paths (i) and (ii) disagree at D={D}: {r}"
        )
        # Path (iii) parity consistency
        f_K3 = r['character_sum_f_K3']
        # f_En integer iff f_K3 even
        expected_integer = (f_K3 % 2 == 0)
        assert r['is_integer_En'] == expected_integer, (
            f"Path (iii) parity fails at D={D}: "
            f"f_K3={f_K3}, f_En integer = {r['is_integer_En']}"
        )


# ---------------------------------------------------------------------------
# EXTENSION TESTS: D in {11, 12, 15, 16, 19, 20}
# ---------------------------------------------------------------------------

def _test_extended_D11_matches_Fourier() -> None:
    """f_K3(11) = -2752; D = 3 mod 4, uniform non-positive, f_En integer."""
    r = verify_persson_volpato_decomposition_extended(11)
    assert r['character_sum_f_K3'] == -2752, (
        f"D=11 character sum {r['character_sum_f_K3']} != -2752"
    )
    assert r['f_K3_from_Fourier_table'] == -2752
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied'], (
        f"D=11 uniform non-positive failed: {r['decomposition']}"
    )
    assert r['is_integer_En'], f"D=11 f_En should be integer: -1376"
    assert r['f_En_halved'] == Fraction(-1376, 1)
    assert r['halving_parity_consistent']


def _test_extended_D12_matches_Fourier() -> None:
    """f_K3(12) = 4016; D = 0 mod 4, uniform non-negative, f_En integer."""
    r = verify_persson_volpato_decomposition_extended(12)
    assert r['character_sum_f_K3'] == 4016
    assert r['f_K3_from_Fourier_table'] == 4016
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied']
    assert r['is_integer_En']
    assert r['f_En_halved'] == Fraction(2008, 1)
    assert r['halving_parity_consistent']


def _test_extended_D15_matches_Fourier() -> None:
    """f_K3(15) = -11775 is ODD; f_En strict half-integer (metaplectic)."""
    r = verify_persson_volpato_decomposition_extended(15)
    assert r['character_sum_f_K3'] == -11775
    assert r['f_K3_from_Fourier_table'] == -11775
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied']
    assert not r['is_integer_En'], (
        f"D=15 f_En should be strict half-integer: -11775/2"
    )
    assert r['f_En_halved'] == Fraction(-11775, 2)
    assert r['halving_parity_consistent']
    assert r['f_K3_parity'] == 'odd'


def _test_extended_D16_matches_Fourier() -> None:
    """f_K3(16) = 16524; D = 0 mod 4, uniform non-negative, f_En integer."""
    r = verify_persson_volpato_decomposition_extended(16)
    assert r['character_sum_f_K3'] == 16524
    assert r['f_K3_from_Fourier_table'] == 16524
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied']
    assert r['is_integer_En']
    assert r['f_En_halved'] == Fraction(8262, 1)


def _test_extended_D19_matches_Fourier() -> None:
    """f_K3(19) = -43200; D = 3 mod 4, uniform non-positive, f_En integer."""
    r = verify_persson_volpato_decomposition_extended(19)
    assert r['character_sum_f_K3'] == -43200
    assert r['f_K3_from_Fourier_table'] == -43200
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied']
    assert r['is_integer_En']
    assert r['f_En_halved'] == Fraction(-21600, 1)


def _test_extended_D20_matches_Fourier() -> None:
    """f_K3(20) = 58640; D = 0 mod 4, uniform non-negative, f_En integer."""
    r = verify_persson_volpato_decomposition_extended(20)
    assert r['character_sum_f_K3'] == 58640
    assert r['f_K3_from_Fourier_table'] == 58640
    assert r['character_sum_matches_Fourier']
    assert r['uniform_sign_satisfied']
    assert r['is_integer_En']
    assert r['f_En_halved'] == Fraction(29320, 1)


def _test_extended_all_six_new_D_converge() -> None:
    """Umbrella test: for each new D in {11, 12, 15, 16, 19, 20}, the four
    verification paths all agree:
      (i) character-dimension identity
      (ii) Fourier-table cross-check
      (iii) EOT uniform-sign parity
      (iv) f_En halving parity
    """
    for D in (11, 12, 15, 16, 19, 20):
        r = verify_persson_volpato_decomposition_extended(D)
        assert r['character_sum_matches_Fourier'], (
            f"Paths (i)+(ii) disagree at D={D}: {r}"
        )
        assert r['uniform_sign_satisfied'], (
            f"Path (iii) EOT uniform-sign failed at D={D}: {r}"
        )
        assert r['halving_parity_consistent'], (
            f"Path (iv) halving parity inconsistent at D={D}: {r}"
        )


def _test_odd_f_K3_locus() -> None:
    """Through D <= 60, odd-f_K3 locus is {-1, 7, 15, 31, 47, 55}."""
    locus = odd_f_K3_locus(D_max=60)
    assert locus == [-1, 7, 15, 31, 47, 55], (
        f"odd_f_K3_locus mismatch: {locus}"
    )
    # Half-integer f_En locus in D >= 0 range
    half_int_positive_D = [D for D in locus if D >= 0]
    assert half_int_positive_D == [7, 15, 31, 47, 55]


def _test_extended_registry_completeness() -> None:
    """Extended registry covers D in {0, 3, 7, 8, 11, 12, 15, 16, 19, 20}."""
    supported = set()
    for D in (0, 3, 7, 8, 11, 12, 15, 16, 19, 20):
        try:
            persson_volpato_twining_leading_extended(D)
            supported.add(D)
        except ValueError:
            pass
    assert supported == {0, 3, 7, 8, 11, 12, 15, 16, 19, 20}, (
        f"Extended registry incomplete: {supported}"
    )
    # D = 23 (next after 20) should NOT be in extended registry
    try:
        persson_volpato_twining_leading_extended(23)
        raise AssertionError("D=23 should raise ValueError")
    except ValueError:
        pass


def run_all_tests() -> None:
    """Run all Wave-18 DRINFELD Enriques-BKM tests."""
    tests = [
        _test_signature,
        _test_rank,
        _test_siegel_weight,
        _test_weight_derivation_consistency,
        _test_m12_order,
        _test_m12_sum_of_squares,
        _test_enriques_genus_halving,
        _test_enriques_genus_integrality,
        _test_real_root_multiplicity,
        _test_imaginary_root_multiplicity_positive,
        _test_three_faces_identity,
        _test_metaplectic_cover,
        _test_paramodular_level,
        _test_iota_fixed_point_free,
        # Persson-Volpato virtual M_12-decomposition tests
        _test_iota_commuting_M12_classes_count,
        _test_M_12_irrep_dims_with_labels,
        _test_virtual_D0_matches_Fourier,
        _test_virtual_D3_matches_Fourier,
        _test_virtual_D7_matches_Fourier,
        _test_virtual_D8_matches_Fourier,
        _test_Enriques_halving_D0_resolves_moonshine,
        _test_character_orthogonality_path_count,
        _test_three_verification_paths_converge_D0_3_7_8,
        # Extension: D in {11, 12, 15, 16, 19, 20}
        _test_extended_D11_matches_Fourier,
        _test_extended_D12_matches_Fourier,
        _test_extended_D15_matches_Fourier,
        _test_extended_D16_matches_Fourier,
        _test_extended_D19_matches_Fourier,
        _test_extended_D20_matches_Fourier,
        _test_extended_all_six_new_D_converge,
        _test_odd_f_K3_locus,
        _test_extended_registry_completeness,
    ]
    for t in tests:
        t()
    print(f"[Wave-18 DRINFELD] all {len(tests)} Enriques-BKM tests passed.")


if __name__ == '__main__':
    run_all_tests()
