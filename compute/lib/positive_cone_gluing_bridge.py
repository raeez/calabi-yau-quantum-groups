"""Exact witnesses for the homotopy-gluing / positive-cone bridge.

The module records the small piece of arithmetic that must be shared by
the DWR/Cech/Ran gluing story in Vol III and the Borcherds chamber story
in ``~/igusa-cusp-form``.

It does not construct the compact ``K3 x E`` Hall-Drinfeld double.  It
only verifies the common chamber data:

* the Igusa effective semigroup ``Gamma_eff``;
* the Lorentzian degree map ``alpha(n,l,m)``;
* the square-2 real-root walls of ``Poly_II``;
* the Weyl vector ``rho``;
* the ``kappa_BKM(Delta_5) = c_1(0)/2 = 5`` normalization.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Tuple


Vector3 = Tuple[Fraction, Fraction, Fraction]
Charge = Tuple[int, int, int]


F2: Vector3 = (Fraction(1), Fraction(0), Fraction(0))
F3: Vector3 = (Fraction(0), Fraction(1), Fraction(0))
FM2: Vector3 = (Fraction(0), Fraction(0), Fraction(1))

DELTA_1: Vector3 = (Fraction(2), Fraction(-1), Fraction(0))
DELTA_2: Vector3 = (Fraction(0), Fraction(-1), Fraction(2))
DELTA_3: Vector3 = F3
REAL_ROOTS: Tuple[Vector3, Vector3, Vector3] = (DELTA_1, DELTA_2, DELTA_3)

RHO: Vector3 = (Fraction(1), Fraction(-1, 2), Fraction(1))


def lorentz_pair(x: Vector3, y: Vector3) -> Fraction:
    """Pairing on ``Lambda^{2,1}`` in the basis ``(f_2, f_3, f_{-2})``.

    The matrix is

        [[0, 0, -1],
         [0, 2,  0],
         [-1, 0, 0]].

    This convention gives the simple-root Gram matrix used by the
    ``Delta_5`` denominator chamber.
    """

    return -x[0] * y[2] - x[2] * y[0] + 2 * x[1] * y[1]


def alpha(charge: Charge) -> Vector3:
    """Lorentzian degree of a BPS charge ``gamma=(n,l,m)``."""

    n, l, m = charge
    return (Fraction(2 * n), Fraction(-l), Fraction(2 * m))


def bps_pair(gamma: Charge, eta: Charge) -> int:
    """BPS pairing transported by the Lorentzian degree map."""

    n, l, m = gamma
    n2, l2, m2 = eta
    return 2 * (n * m2 + n2 * m) - l * l2


def alpha_pairing_identity(gamma: Charge, eta: Charge) -> bool:
    """Check ``(alpha(gamma), alpha(eta)) = -2 <gamma, eta>``."""

    return lorentz_pair(alpha(gamma), alpha(eta)) == -2 * bps_pair(gamma, eta)


def discriminant(charge: Charge) -> int:
    """Igusa discriminant ``4nm-l^2``."""

    n, l, m = charge
    return 4 * n * m - l * l


def in_igusa_effective_chamber(charge: Charge) -> bool:
    """The standard product chamber from the Igusa Borcherds product."""

    n, l, m = charge
    return (m > 0 and n >= 0) or (m == 0 and n > 0) or (
        m == 0 and n == 0 and l < 0
    )


def simple_root_gram() -> Tuple[Tuple[Fraction, ...], ...]:
    """Gram matrix of ``delta_1, delta_2, delta_3``."""

    return tuple(tuple(lorentz_pair(x, y) for y in REAL_ROOTS) for x in REAL_ROOTS)


def rho_wall_pairings() -> Tuple[Fraction, Fraction, Fraction]:
    """The Weyl-vector equations ``(rho, delta_i) = -1``."""

    return tuple(lorentz_pair(RHO, root) for root in REAL_ROOTS)


def chamber_wall_pairings(vector: Vector3) -> Tuple[Fraction, Fraction, Fraction]:
    """Pairings against the three walls of ``Poly_II``."""

    return tuple(lorentz_pair(vector, root) for root in REAL_ROOTS)


def in_closed_poly_ii(vector: Vector3) -> bool:
    """Closed chamber condition ``(x, delta_i) <= 0`` for all walls."""

    return all(pairing <= 0 for pairing in chamber_wall_pairings(vector))


def kappa_bkm_from_constant_term(c0: int) -> Fraction:
    """Borcherds weight formula ``kappa_BKM = c_0 / 2``."""

    return Fraction(c0, 2)


@dataclass(frozen=True)
class GluingPositiveConeDictionary:
    """The common data seen by homotopy gluing and the positive cone."""

    homotopy_gluing_object: str
    positive_cone_object: str
    chamber: str
    wall_transport: str
    orientation_character: str
    automorphic_boundary: str
    status: str


def bridge_dictionary() -> GluingPositiveConeDictionary:
    """Return the typed bridge without claiming the unbuilt double."""

    return GluingPositiveConeDictionary(
        homotopy_gluing_object=(
            "completed oriented critical Hall cosheaf on the DWR/Cech/Ran nerve"
        ),
        positive_cone_object=(
            "Igusa Lorentzian chamber Gamma_eff mapped by alpha into Poly_II"
        ),
        chamber="Harder-Narasimhan sector equals Borcherds product chamber",
        wall_transport="KS wall-crossing equals gauge transport in the completed Hall torus",
        orientation_character="determinant-line sign realized by nu_Delta_5",
        automorphic_boundary="AutBorch(phi_{0,1}) = Delta_5",
        status=(
            "proved for Igusa denominator arithmetic; conditional for compact "
            "K3 x E Hall-Drinfeld assembly"
        ),
    )


def all_alpha_identities(charges: Iterable[Charge]) -> bool:
    """Pairing identity on a finite charge sample."""

    charge_list = list(charges)
    return all(
        alpha_pairing_identity(gamma, eta)
        for gamma in charge_list
        for eta in charge_list
    )
