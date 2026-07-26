r"""
k3_yangian_borcherds_weight_theta_refinement.py -- The two honest
kappa_BKM ladders on the CHL slice N in {1, 2, 3, 4, 6}, computed from
primary data.

PROVENANCE (honest)
===================

Primary hard-coded data, with sources:

1. M_24 frame shapes of the Nikulin-symplectic classes
   (Gaberdiel-Hohenegger-Volpato 2010; Mukai 1988):
       1A: 1^24, 2A: 1^8 2^8, 3A: 1^6 3^6, 4B: 1^4 2^2 4^4,
       5A: 1^4 5^4, 6A: 1^2 2^2 3^2 6^2, 7A: 1^3 7^3, 8A: 1^2 2 4 8^2.
2. The K3 Hodge diamond (h^{0,0} = h^{2,0} = h^{0,2} = h^{2,2} = 1,
   h^{1,1} = 20, odd rows zero).
3. Jatkar-Sen composite-level dyon-form weights k(4) = 3, k(6) = 2
   (Govindarajan-Krishna 2010 JHEP 05.014 Table 1; the prime-level
   values are COMPUTED below from 24/(N+1) - 2 and cross-checked
   against a_1 - 2).
4. dim S_k(Sp_4(Z)) = 0 for k <= 4; the first scalar Siegel cusp
   forms are chi_10, chi_12; weight 5 exists only with character
   (Igusa 1962/1964).

Everything else is computed:

* a_1(g) (ones-exponent) and the frame dimension sum a*m_a = 24 from
  the frame shapes; power-map frame shapes by cycle arithmetic.
* c_1(0) = 20, the q^0 y^0 coefficient of Ell(K3) = 2 phi_{0,1},
  computed from the Hodge diamond via
  Ell(K3)|_{q^0} = y^{-1} chi_{-y}(K3) = 2y^{-1} + 20 + 2y.
  The half-genus phi_{0,1} has c(0,0) = 10: this is the Borcherds
  input of Delta_5 (weight 5).
* The Mathieu-twined ladder (Cheng; Cheng-Harrison; Eguchi-Hikami
  2011 at N = 2): weight k_N = c_N(0)/2 with c_N(0) = a_1(g_N) for
  N >= 2 and c_1(0) = 20, giving weights (10, 4, 3, 2, 1). The
  twining-genus q^0 row itself is
  2y^{-1} + (a_1 - 4) + 2y (computed below via the equivariant
  chi_{-y}); the constant a_1 entering the twined SIEGEL-form weight
  completes this row through the twisted sectors of the
  second-quantized lift, and is taken from the frame shape as the
  Cheng-Harrison attribution.
* The Jatkar-Sen dyon-form ladder: weights (10, 6, 4, 3, 2) at
  N = (1, 2, 3, 4, 6); prime-level values computed as 24/(N+1) - 2
  and cross-checked against the frame-shape identity
  k = a_1(g_N) - 2 (prime N).
* The Govindarajan-Krishna square-root ladder: weights
  (5, 3, 2, 3/2, 1) = (Jatkar-Sen)/2; the N = 1 member is Delta_5,
  the Borcherds lift of the half-genus with c(0,0) = 10.

NEGATIVE RESULTS enforced by tests:

* The mixed tuple (5, 4, 3, 2, 1) -- square-root value at N = 1
  glued to twined values at N >= 2 -- matches NO single family.
* "Integer-weight Sp_4(Z) cusp forms of weights (5, 4, 3, 2, 1)" is
  impossible: dim S_k(Sp_4(Z)) = 0 for k <= 4.

The universal identity kappa_BKM(Phi) = c(0)/2 is Borcherds
(Invent. Math. 132 (1998), Thm 13.3) and holds per declared input.

References
----------
    Borcherds, "Automorphic forms with singularities on Grassmannians",
       Invent. Math. 132 (1998) 491-562, Thm 13.3
    Gritsenko-Nikulin, "Siegel automorphic form corrections of some
       Lorentzian Kac-Moody Lie algebras", Amer. J. Math. 119 (1997)
       181-224 (arXiv:alg-geom/9504006); "Automorphic forms and
       Lorentzian Kac-Moody algebras II", Internat. J. Math. 9 (1998)
       201-275
    Eguchi-Hikami, "Note on twisted elliptic genus of K3 surface",
       Phys. Lett. B 694 (2011) 446-455
    Cheng, "K3 surfaces, N=4 dyons, and the Mathieu group M24",
       Commun. Number Theory Phys. 4 (2010) 623-657
    Gaberdiel-Hohenegger-Volpato, "Mathieu twining characters for K3",
       JHEP 09 (2010) 058
    Jatkar-Sen, "Dyon spectrum in CHL models", JHEP 04 (2006) 018
    Govindarajan-Krishna, "BKM Lie superalgebras from dyon spectra in
       Z_N-CHL orbifolds for composite N", JHEP 05 (2010) 014
    Igusa, "On Siegel modular forms of genus two", Amer. J. Math. 84
       (1962) 175-200; 86 (1964) 392-412 (ring structure: first cusp
       forms chi_10, chi_12; chi_5 has a character)
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# Primary datum 1: frame shapes {cycle_length: multiplicity}.
# ---------------------------------------------------------------------------

FRAME_SHAPES: Dict[int, Dict[int, int]] = {
    1: {1: 24},
    2: {1: 8, 2: 8},
    3: {1: 6, 3: 6},
    4: {1: 4, 2: 2, 4: 4},
    5: {1: 4, 5: 4},
    6: {1: 2, 2: 2, 3: 2, 6: 2},
    7: {1: 3, 7: 3},
    8: {1: 2, 2: 1, 4: 1, 8: 2},
}

CHL_SLICE: List[int] = [1, 2, 3, 4, 6]
ALL_ORDERS: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

# Primary datum 2: K3 Hodge diamond h[p][q].
K3_HODGE: Dict[int, Dict[int, int]] = {
    0: {0: 1, 1: 0, 2: 1},
    1: {0: 0, 1: 20, 2: 0},
    2: {0: 1, 1: 0, 2: 1},
}

# Primary datum 3: Jatkar-Sen composite-level weights (GK 2010 Table 1).
JS_COMPOSITE_WEIGHTS: Dict[int, int] = {4: 3, 6: 2}

# Primary datum 4: dim S_k(Sp_4(Z)) for k <= 5 (Igusa).
DIM_SIEGEL_CUSP_SP4Z: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
# weight 5: only with character (chi_5); no cusp form with trivial
# multiplier below weight 10 (chi_10).


# ---------------------------------------------------------------------------
# Computations from the frame shapes.
# ---------------------------------------------------------------------------

def frame_dimension(N: int) -> int:
    """sum_a a * m_a (must be 24 on the Mukai 24-dim representation)."""
    return sum(a * m for a, m in FRAME_SHAPES[N].items())


def a1(N: int) -> int:
    """Ones-exponent a_1 = number of fixed points of g_N on the 24-dim rep."""
    return FRAME_SHAPES[N].get(1, 0)


def frame_power(shape: Dict[int, int], s: int) -> Dict[int, int]:
    """Frame shape of g^s from the frame shape of g, by cycle arithmetic:
    an a-cycle raised to the s-th power splits into gcd(a, s) cycles of
    length a/gcd(a, s)."""
    out: Dict[int, int] = {}
    for a, m in shape.items():
        g = gcd(a, s)
        length = a // g
        out[length] = out.get(length, 0) + m * g
    return out


def chi_minus_y_K3() -> Dict[int, int]:
    """chi_{-y}(K3) = sum_p (-y)^p sum_q (-1)^q h^{p,q}, as {power: coeff}."""
    out: Dict[int, int] = {}
    for p in range(3):
        col = sum((-1) ** q * K3_HODGE[p][q] for q in range(3))
        # (-y)^p contributes (-1)^p to the coefficient of y^p
        out[p] = out.get(p, 0) + (-1) ** p * col
    return out


def ell_genus_q0_row() -> Dict[int, int]:
    """q^0 row of Ell(K3) as {y-power: coeff}: y^{-1} chi_{-y}(K3)."""
    chi = chi_minus_y_K3()
    return {p - 1: c for p, c in chi.items()}


def twining_genus_q0_row(N: int) -> Dict[int, int]:
    """q^0 row of the g_N-twining genus via the equivariant chi_{-y}:
    the four corner Hodge classes are g-invariant (symplectic action),
    the H^{1,1}-trace is a_1 - 4. Row: 2 y^{-1} + (a_1 - 4) + 2 y."""
    t11 = a1(N) - 4
    return {-1: 2, 0: t11, 1: 2}


# ---------------------------------------------------------------------------
# The three honest ladders.
# ---------------------------------------------------------------------------

def twined_c0(N: int) -> int:
    """Constant c_N(0) of the Mathieu-twined family: the q^0 y^0
    coefficient 20 of Ell(K3) at N = 1 (computed from the Hodge
    diamond); the frame-shape ones-exponent a_1 at N >= 2
    (Cheng-Harrison attribution; the twisted-sector completion of the
    twining-genus row)."""
    if N == 1:
        return ell_genus_q0_row()[0]
    return a1(N)


def twined_weight(N: int) -> Fraction:
    """Mathieu-twined Borcherds weight = c_N(0)/2."""
    return Fraction(twined_c0(N), 2)


def js_weight(N: int) -> int:
    """Jatkar-Sen dyon-form weight: 24/(N+1) - 2 at prime N and N = 1
    (computed; requires (N+1) | 24), Govindarajan-Krishna Table 1 at
    composite N in the CHL slice."""
    if N in JS_COMPOSITE_WEIGHTS:
        return JS_COMPOSITE_WEIGHTS[N]
    assert 24 % (N + 1) == 0, f"24/(N+1) not integral at N={N}"
    return 24 // (N + 1) - 2


def gk_sqrt_weight(N: int) -> Fraction:
    """Govindarajan-Krishna square-root weight = (Jatkar-Sen)/2."""
    return Fraction(js_weight(N), 2)


def delta5_c0() -> int:
    """c(0,0) of the half-genus phi_{0,1} = Ell(K3)/2: the Borcherds
    input of Delta_5. Computed: 20/2 = 10; weight 5 = 10/2."""
    c = ell_genus_q0_row()[0]
    assert c % 2 == 0
    return c // 2


# ---------------------------------------------------------------------------
# Ladder tables and negative results.
# ---------------------------------------------------------------------------

def twined_ladder() -> List[Tuple[int, int, Fraction]]:
    """(N, c_N(0), weight) for the twined family on the CHL slice."""
    return [(N, twined_c0(N), twined_weight(N)) for N in CHL_SLICE]


def gk_ladder() -> List[Tuple[int, Fraction]]:
    """(N, weight) for the square-root family on the CHL slice."""
    return [(N, gk_sqrt_weight(N)) for N in CHL_SLICE]


def js_ladder() -> List[Tuple[int, int]]:
    """(N, weight) for the Jatkar-Sen dyon forms on the CHL slice."""
    return [(N, js_weight(N)) for N in CHL_SLICE]


MIXED_TUPLE = (Fraction(5), Fraction(4), Fraction(3), Fraction(2), Fraction(1))


def mixed_tuple_matches_no_family() -> bool:
    """The historically inscribed tuple (5, 4, 3, 2, 1) pairs the
    square-root value at N = 1 with twined values at N >= 2; it must
    differ from each honest ladder."""
    tw = tuple(twined_weight(N) for N in CHL_SLICE)
    gk = tuple(gk_sqrt_weight(N) for N in CHL_SLICE)
    js = tuple(Fraction(js_weight(N)) for N in CHL_SLICE)
    return MIXED_TUPLE not in (tw, gk, js)


def sp4z_integer_weight_claim_impossible() -> bool:
    """No integer-weight Sp_4(Z) cusp forms of weights 4, 3, 2, 1
    exist: dim S_k(Sp_4(Z)) = 0 for k <= 4 (Igusa)."""
    return all(DIM_SIEGEL_CUSP_SP4Z[k] == 0 for k in (1, 2, 3, 4))


# ---------------------------------------------------------------------------
# Verification paths (non-circular).
# ---------------------------------------------------------------------------

def verify_frame_dimensions() -> bool:
    """Path 1: every frame shape has total dimension 24."""
    return all(frame_dimension(N) == 24 for N in ALL_ORDERS)


def verify_power_map_closure() -> bool:
    """Path 2: frame shapes close under power maps within the M_24
    Nikulin list: (2A)^1, (3A)^1, (4B)^2 = 2A, (6A)^2 = 3A,
    (6A)^3 = 2A, (8A)^2 = 4B, (8A)^4 = 2A."""
    checks = [
        (frame_power(FRAME_SHAPES[4], 2), FRAME_SHAPES[2]),
        (frame_power(FRAME_SHAPES[6], 2), FRAME_SHAPES[3]),
        (frame_power(FRAME_SHAPES[6], 3), FRAME_SHAPES[2]),
        (frame_power(FRAME_SHAPES[8], 2), FRAME_SHAPES[4]),
        (frame_power(FRAME_SHAPES[8], 4), FRAME_SHAPES[2]),
    ]
    return all(got == want for got, want in checks)


def verify_ell_genus_row() -> bool:
    """Path 3: Ell(K3) q^0 row computed from the Hodge diamond is
    2 y^{-1} + 20 + 2 y (so c(0,0) = 20; half-genus 10)."""
    return ell_genus_q0_row() == {-1: 2, 0: 20, 1: 2} and delta5_c0() == 10


def verify_js_prime_frame_identity() -> bool:
    """Path 4: at prime N in the slice, the computed Jatkar-Sen weight
    24/(N+1) - 2 equals the frame-shape identity a_1(g_N) - 2."""
    return all(js_weight(N) == a1(N) - 2 for N in (2, 3))


def verify_ladders() -> bool:
    """Path 5: the three ladders take their literature values."""
    tw = [twined_weight(N) for N in CHL_SLICE]
    gk = [gk_sqrt_weight(N) for N in CHL_SLICE]
    js = [js_weight(N) for N in CHL_SLICE]
    return (
        tw == [Fraction(10), Fraction(4), Fraction(3), Fraction(2), Fraction(1)]
        and gk == [Fraction(5), Fraction(3), Fraction(2), Fraction(3, 2), Fraction(1)]
        and js == [10, 6, 4, 3, 2]
    )


def verify_squaring_relation() -> bool:
    """Path 6: GK squares to JS (Delta_{k/2}^2 = Phi_k), and at N = 1
    the twined member equals the JS member (chi_10 = Delta_5^2)."""
    gk_doubles = all(2 * gk_sqrt_weight(N) == js_weight(N) for N in CHL_SLICE)
    n1 = twined_weight(1) == Fraction(js_weight(1)) == 2 * gk_sqrt_weight(1)
    return gk_doubles and n1


def _self_check() -> None:
    assert verify_frame_dimensions(), "frame dimension != 24"
    assert verify_power_map_closure(), "power-map closure fails"
    assert verify_ell_genus_row(), "Ell(K3) q^0 row computation fails"
    assert verify_js_prime_frame_identity(), "JS prime/frame identity fails"
    assert verify_ladders(), "ladder values fail"
    assert verify_squaring_relation(), "squaring relation fails"
    assert mixed_tuple_matches_no_family(), "mixed tuple matches a family"
    assert sp4z_integer_weight_claim_impossible(), "Sp4(Z) dims wrong"


_self_check()
