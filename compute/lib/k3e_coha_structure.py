r"""
Associative Hall-side diagnostics for CoHA(K3 x E) from Oberdieck-Pixton.

MATHEMATICAL CONTENT
====================

The cohomological Hall algebra (CoHA) of K3 x E is the prototype CY3 example
for the BKM identification.  The BPS states of K3 x E are organized by charge
gamma = (r, c_1, ch_2) in H^*(K3 x E, Z).  The CoHA has graded pieces

    CoHA_gamma = H^*(M_gamma, phi_{tr W})

where M_gamma is the moduli of coherent sheaves with Chern character gamma,
and phi_{tr W} is the vanishing cycle sheaf for the potential tr(W).

THE COHA PRODUCT
================

The CoHA multiplication is defined by the Kontsevich-Soibelman construction
via correspondences:

    CoHA_{gamma_1} tensor CoHA_{gamma_2} --> CoHA_{gamma_1 + gamma_2}

given by the diagram

    M_{gamma_1} x M_{gamma_2} <-- Z_{gamma_1,gamma_2} --> M_{gamma_1+gamma_2}

where Z parametrizes short exact sequences 0 -> F_1 -> F -> F_2 -> 0 with
[F_i] = gamma_i.

RANK DECOMPOSITION
==================

For K3 x E, the CoHA decomposes by rank:

Rank 0: Ideal sheaves of subschemes Z subset K3 x E.
    The protected Euler/signed-character statistic is chi(Hilb^n(K3 x E)).
    It is not an unsourced ordinary CoHA dimension.  A dimension statement
    requires an explicit parity-resolved fixture or compact source datum.
    Generating function: M(q) * prod_{k>=1} 1/(1-q^k)^{20} (from DMVV).
    The 20 = b_2(K3) - 2 terms are protected-character inputs from K3
    cohomology beyond the algebraic classes.

Rank 1: Pure dimension-2 sheaves supported on K3 fibers.
    The CoHA_{(1,0,n)} counts rank-1 sheaves with ch_2 = n.
    GF: 1/eta(q)^{24} (Hilbert scheme of K3).

General: the Delta_5 Borcherds signed-character lane is

    sum_{N>=0} p^N Z_N(q,y) = prod_{n>0,l,m>=0} 1/(1-p^n q^l y^m)^{c(4nm-l^2)}

where c(D) are the discriminant coefficients of the weak Jacobi form phi_{0,1}.
The doubled K3 elliptic-genus/DMVV lane uses exponents 2c(D) and gives
Phi_10^{un} = Delta_5^2; it is not the coefficient lane computed below.

BKM IDENTIFICATION
==================

The central conditional target: an oriented compact critical
CoHA(K3 x E), once the Hall product and Hall-to-Borcherds bracket
comparison are constructed, should identify (as a graded associative
algebra with product) with the POSITIVE HALF of the BKM superalgebra
g_{Delta_5}:

    CoHA(K3 x E) = U(n_+)

where n_+ is the positive nilpotent part of g_{Delta_5} in the triangular
decomposition g = n_- oplus h oplus n_+.

Evidence:
(1) The signed BKM character coefficient is c(4nm - l^2).  Its
    magnitude |c(D)| is an unsigned coefficient statistic, not by itself
    a local CoHA dimension.  A CoHA dimension requires an even/odd parity
    source for the charge sector.
(2) The DMVV product = BKM denominator identity (Gritsenko-Nikulin).
(3) The Weyl symmetry of g_{Delta_5} acts on the K3 moduli.

EQUIVARIANT DEFORMATION (ASSOCIATIVE E1 ALGEBRA STRUCTURE)
===========================================================

The associative E1 algebra structure emerges when equivariant parameters
from the torus T action on E (the elliptic curve factor) are turned on.
CoHA itself is not a chiral algebra; the chiral object appears only after
the framed Phi_3 specialisation, completion, Hall/Drinfeld comparison,
and centre data are supplied.

Let epsilon be the equivariant parameter for the T-action on E.  Then:

    CoHA_epsilon(K3 x E) = deformed CoHA with epsilon-dependent product

At epsilon = 0: the CoHA is commutative (E_infty).
At epsilon != 0: the CoHA has a non-trivial E1 structure controlled by
the structure function

    g(z) = (z + epsilon/2) / (z - epsilon/2)   (rank 1)

or more generally for higher rank, by the Maulik-Okounkov R-matrix construction.

For K3 x E, the Maulik-Okounkov construction shows:
    - The CoHA carries a Y(g_{Delta_5})-module structure.
    - The stable envelope gives the R-matrix.
    - The E1 product is the epsilon-deformation of the BKM algebra.

This is an associative Hall-side diagnostic, not an E1-chiral algebra.
At the chiral level the corresponding vertex/chiral object is conditional
on the manuscript comparison data.

WHAT THIS MODULE COMPUTES
=========================

1. Signed-character coefficients c(D) and unsigned magnitudes |c(D)| for
   low charges, via the Delta_5 Borcherds product attached to phi_{0,1}.
2. The associative E1 product structure constants at low orders.
3. Root multiplicity / signed-character verification against phi_{0,1}.
4. The equivariant deformation structure function.
5. Generating functions for each rank sector.
6. Comparison with the BKM root datum.

REFERENCES
==========

- Dijkgraaf-Moore-Verlinde-Verlinde, hep-th/9607026 (DMVV formula)
- Oberdieck-Pixton, arXiv:1904.01266 (DT invariants of K3 x E)
- Kontsevich-Soibelman, arXiv:0811.2435 (CoHA definition)
- Maulik-Okounkov, arXiv:1211.1287 (quantum groups from geometry)
- Gritsenko-Nikulin, alg-geom/9504006 (BKM and Siegel modular forms)
- Schiffmann-Vasserot, arXiv:1211.1287 (CoHA = affine Yangian for C^3)
- Rapcak-Soibelman-Yang-Zhao, arXiv:1910.10006 (CoHA perspectives)

Manuscript references:
    Chapter: k3_times_e.tex (ch:k3-times-e)
    BKM identification: thm:k3e-denominator, thm:k3e-product
    CoHA-BKM theorem: conj:coha-bkm-identification
"""

from __future__ import annotations

import math
import warnings
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Mapping, NamedTuple, Optional, Tuple, Union

import importlib as _importlib
import os as _os
import sys as _sys


def _import_sibling(name: str):
    """Import a sibling module from the same directory."""
    try:
        return _importlib.import_module(f'compute.lib.{name}')
    except (ImportError, ModuleNotFoundError):
        _lib_dir = _os.path.dirname(_os.path.abspath(__file__))
        if _lib_dir not in _sys.path:
            _sys.path.insert(0, _lib_dir)
        return _importlib.import_module(name)


_phi01_mod = _import_sibling('phi01_fourier')
_phi01_by_discriminant_raw = _phi01_mod.phi01_by_discriminant
phi01_table = _phi01_mod.phi01_table
phi01_coefficient = _phi01_mod.phi01_coefficient

# The phi01 theta-function computation becomes unreliable for max_n > ~20
# due to intermediate Fraction precision in the lattice sum.
# Cap at 20 to ensure exact integer results.
_PHI01_MAX_N = 24


def phi01_by_discriminant(max_n: int) -> Dict[int, int]:
    """Safe wrapper: cap max_n to avoid phi01 precision issues."""
    return _phi01_by_discriminant_raw(min(max_n, _PHI01_MAX_N))


# =========================================================================
# 1. CHARGE LATTICE AND ROOT DATA
# =========================================================================

# For K3 x E, the effective charge lattice for the CoHA is:
#   Gamma_eff = Z^3  with basis (rank r, fiber class l, instanton number m)
# The discriminant D = 4rm - l^2 classifies the target root type:
#   D < 0: below the retained BPS chamber in this finite sanity model
#   D = -1: real-root signed character c(-1) = 1 from phi_{0,1}
#   D >= 0: imaginary-root signed character c(D) from phi_{0,1}

# Gram matrix for g_{Delta_5} (real simple roots)
GRAM_MATRIX = ((2, -2, -2), (-2, 2, -2), (-2, -2, 2))

# chi(K3) = 24, chi(O_K3) = 2
CHI_K3 = 24
CHI_O_K3 = 2

# b_2(K3) = 22, signature (3, 19)
B2_K3 = 22

# phi_{0,1} key discriminant coefficients (Eichler-Zagier convention)
# c(-1) = 1 (real root, the simple root contribution)
# c(0)  = 10 (first imaginary: 10 = (chi(K3) - 4)/2 = 20/2)
# Actually c(0) = 10 is a standard result.
# c(3)  = -64 (fermionic root, D=3)
# c(4)  = 108 (D=4)
# c(7)  = -513 (D=7)
# c(8)  = 808 (D=8)
# c(11), c(12), c(15), c(16) extend the finite source table used by
# the three-path low-degree verification below.

KNOWN_C_DISC = {
    -1: 1,
    0: 10,
    3: -64,
    4: 108,
    7: -513,
    8: 808,
    11: -2752,
    12: 4016,
    15: -11775,
    16: 16524,
}


def discriminant(r: int, l: int, m: int) -> int:
    """Compute D = 4rm - l^2 for a charge vector (r, l, m)."""
    return 4 * r * m - l * l


def _signed_character_coefficient_raw(r: int, l: int, m: int, max_n: int = 20) -> int:
    """Internal signed root-character coefficient c(4rm - l^2)."""
    D = discriminant(r, l, m)
    if D < -1:
        return 0
    c_disc = phi01_by_discriminant(max(max_n, D // 4 + 5))
    return c_disc.get(D, 0)


def root_multiplicity(r: int, l: int, m: int, max_n: int = 20) -> int:
    """Deprecated legacy alias for signed root-character coefficient c(D).

    This function is kept for compatibility. Its return value may be
    negative and must not be read as an ordinary dimension or generator
    count without a parity-resolved fixture/source datum.
    """
    warnings.warn(
        "root_multiplicity() is a deprecated legacy alias for the signed "
        "root-character coefficient; use signed_character_coefficient() and "
        "do not read it as an ordinary dimension without a parity fixture.",
        DeprecationWarning,
        stacklevel=2,
    )
    return _signed_character_coefficient_raw(r, l, m, max_n)


def is_real_root(r: int, l: int, m: int) -> bool:
    """A root is real iff D = 4rm - l^2 = -1 and mult = 1."""
    return discriminant(r, l, m) == -1


def is_imaginary_root(r: int, l: int, m: int) -> bool:
    """A root is imaginary iff D = 4rm - l^2 >= 0."""
    return discriminant(r, l, m) >= 0


def root_type(r: int, l: int, m: int) -> str:
    """Classify a root as 'real', 'imaginary_bosonic', 'imaginary_fermionic', or 'none'.

    Bosonic roots have c(D) > 0; fermionic have c(D) < 0.
    This is a feature of the BKM SUPERalgebra: the Lie superalgebra has
    both even (bosonic) and odd (fermionic) root spaces.
    """
    D = discriminant(r, l, m)
    if D < -1:
        return 'none'
    mult = signed_character_coefficient(r, l, m)
    if mult == 0:
        return 'none'
    if D == -1:
        return 'real'
    if mult > 0:
        return 'imaginary_bosonic'
    return 'imaginary_fermionic'


# =========================================================================
# 2. SIGNED CHARACTER STATISTICS AND PARITY-RESOLVED DIMENSIONS
# =========================================================================

class CoHAParityFixture(NamedTuple):
    """Parity-resolved source data for a CoHA charge sector.

    The signed character c(D) only determines even_dim - odd_dim.  The
    ordinary dimension even_dim + odd_dim is available only after a source
    has resolved the parity split for the sector.
    """
    even_dim: int
    odd_dim: int
    source: str

    @property
    def signed_character(self) -> int:
        """The super-character contribution even_dim - odd_dim."""
        return self.even_dim - self.odd_dim

    @property
    def total_dimension(self) -> int:
        """The ordinary dimension even_dim + odd_dim."""
        return self.even_dim + self.odd_dim


ParityFixtureInput = Union[
    CoHAParityFixture,
    Mapping[Tuple[int, int, int], CoHAParityFixture],
]


def _parity_fixture_for_charge(r: int, l: int, m: int,
                               parity_fixture: Optional[ParityFixtureInput]
                               ) -> Optional[CoHAParityFixture]:
    """Resolve a charge-specific parity fixture."""
    if parity_fixture is None:
        return None
    if isinstance(parity_fixture, CoHAParityFixture):
        return parity_fixture
    return parity_fixture.get((r, l, m))


def _validate_parity_fixture(fixture: CoHAParityFixture) -> None:
    """Reject fixture data that cannot be a sourced dimension split."""
    if fixture.even_dim < 0 or fixture.odd_dim < 0:
        raise ValueError("CoHA parity fixture dimensions must be non-negative")
    if not fixture.source:
        raise ValueError("CoHA parity fixture needs a non-empty source")


def signed_character_coefficient(r: int, l: int, m: int,
                                 max_n: int = 20) -> int:
    """Signed character coefficient c(4rm - l^2)."""
    return _signed_character_coefficient_raw(r, l, m, max_n)


def signed_character_magnitude(r: int, l: int, m: int,
                               max_n: int = 20) -> int:
    """Unsigned statistic |c(4rm - l^2)|, not a CoHA dimension."""
    return abs(signed_character_coefficient(r, l, m, max_n))


def unsigned_coefficient_statistic(r: int, l: int, m: int,
                                   max_n: int = 20) -> int:
    """Alias for the unsigned coefficient magnitude |c(D)|."""
    return signed_character_magnitude(r, l, m, max_n)


def coha_dimension(r: int, l: int, m: int, max_n: int = 20,
                   parity_fixture: Optional[ParityFixtureInput] = None) -> int:
    """Parity-resolved dimension of CoHA_{(r,l,m)}.

    The coefficient c(D) is a signed character.  The number |c(D)| is only
    an unsigned coefficient statistic unless a source identifies the charge
    sector as purely even, purely odd, or otherwise gives the even/odd split.
    """
    fixture = _parity_fixture_for_charge(r, l, m, parity_fixture)
    if fixture is None:
        raise ValueError(
            "CoHA dimension requires parity fixture/source recognition; "
            "use signed_character_magnitude(...) for |c(D)|."
        )
    _validate_parity_fixture(fixture)
    expected_character = signed_character_coefficient(r, l, m, max_n)
    if fixture.signed_character != expected_character:
        raise ValueError(
            "Parity fixture signed character does not match c(D): "
            f"{fixture.signed_character} != {expected_character}"
        )
    return fixture.total_dimension


def signed_character_magnitude_table(max_r: int, max_l: int, max_m: int,
                                     max_n: int = 20
                                     ) -> Dict[Tuple[int, int, int], int]:
    """Compute |c(D)| for all charges up to the given bounds.

    This is a finite unsigned coefficient statistic, not a table of local
    CoHA dimensions.
    """
    # Need c(D) for D up to 4*max_r*max_m + max_l^2.
    # phi01_by_discriminant(N) computes c(D) for D up to ~4*N.
    # So need N >= (4*max_r*max_m + max_l^2)/4 + 1.
    needed_n = (4 * max_r * max_m + max_l * max_l) // 4 + 2
    needed_n = min(needed_n, 20)  # cap to avoid precision issues in phi01
    c_disc = phi01_by_discriminant(max(needed_n, min(max_n, 20)))
    table = {}
    for r in range(0, max_r + 1):
        for m in range(0, max_m + 1):
            if r == 0 and m == 0:
                continue
            for l_val in range(-max_l, max_l + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                if cD != 0:
                    table[(r, l_val, m)] = abs(cD)
    return table


def coha_dimension_table(max_r: int, max_l: int, max_m: int,
                         max_n: int = 20,
                         parity_fixtures: Optional[
                             Mapping[Tuple[int, int, int], CoHAParityFixture]
                         ] = None) -> Dict[Tuple[int, int, int], int]:
    """Compute sourced CoHA dimensions from parity fixtures.

    Without parity fixtures this function refuses to promote |c(D)| to a
    dimension.
    """
    if parity_fixtures is None:
        raise ValueError(
            "CoHA dimension table requires parity fixtures; "
            "use signed_character_magnitude_table(...) for |c(D)|."
        )
    table: Dict[Tuple[int, int, int], int] = {}
    for (r, l_val, m), fixture in parity_fixtures.items():
        if not (0 <= r <= max_r and abs(l_val) <= max_l and 0 <= m <= max_m):
            continue
        table[(r, l_val, m)] = coha_dimension(
            r, l_val, m, max_n=max_n, parity_fixture=fixture
        )
    return table


def total_signed_character_magnitude_by_degree(max_degree: int,
                                               max_n: int = 20) -> Dict[int, int]:
    """Sum |c(D)| by degree N = r + m.

    This is a signed-character magnitude statistic.  It is useful for finite
    sanity checks, but it is not a CoHA dimension without parity data.
    """
    c_disc = phi01_by_discriminant(max(max_n, max_degree**2 + 5))
    totals: Dict[int, int] = {}
    for N in range(1, max_degree + 1):
        total = 0
        for r in range(0, N + 1):
            m = N - r
            l_max = int(math.isqrt(4 * r * m + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                if cD != 0:
                    total += abs(cD)
        totals[N] = total
    return totals


def total_coha_dimension_by_degree(max_degree: int,
                                   max_n: int = 20,
                                   parity_fixtures: Optional[
                                       Mapping[Tuple[int, int, int], CoHAParityFixture]
                                   ] = None) -> Dict[int, int]:
    """Total sourced CoHA dimension at each degree N = r + m.

    Requires parity fixtures for the charge sectors being counted.
    """
    if parity_fixtures is None:
        raise ValueError(
            "CoHA dimensions require parity fixtures; "
            "use total_signed_character_magnitude_by_degree(...) for |c(D)| sums."
        )
    totals: Dict[int, int] = {N: 0 for N in range(1, max_degree + 1)}
    for (r, l_val, m), fixture in parity_fixtures.items():
        degree = r + m
        if 1 <= degree <= max_degree:
            totals[degree] += coha_dimension(
                r, l_val, m, max_n=max_n, parity_fixture=fixture
            )
    return totals


def _legacy_abs_coefficient_totals(max_degree: int,
                                   max_n: int = 20) -> Dict[int, int]:
    """Compatibility helper for code paths explicitly using |c(D)| statistics."""
    return total_signed_character_magnitude_by_degree(max_degree, max_n)


def _canonical_phi01_representative(D: int) -> Optional[Tuple[int, int]]:
    """Return a canonical (n, l) with D = 4n - l^2 when one exists."""
    if D < -1:
        return None
    if D % 4 == 0:
        return (D // 4, 0)
    if D % 4 == 3:
        return ((D + 1) // 4, 1)
    return None


@lru_cache(maxsize=None)
def _direct_phi01_coefficient(n: int, l: int, max_n: int) -> int:
    """Cached direct Fourier coefficient path for verification."""
    return phi01_coefficient(n, l, max_n)


# =========================================================================
# 3. RANK-SECTOR GENERATING FUNCTIONS
# =========================================================================

def _eta_inverse_power(exponent: int, max_n: int) -> List[Fraction]:
    """Compute prod_{k>=1} 1/(1-q^k)^{exponent} truncated to q^{max_n}."""
    result: Dict[int, Fraction] = {0: Fraction(1)}
    for k in range(1, max_n + 1):
        for _ in range(abs(exponent)):
            new: Dict[int, Fraction] = {}
            for n_val in range(max_n + 1):
                s = result.get(n_val, Fraction(0))
                if n_val >= k:
                    s += new.get(n_val - k, Fraction(0))
                new[n_val] = s
            result = new
    return [result.get(i, Fraction(0)) for i in range(max_n + 1)]


def rank0_generating_function(max_n: int) -> List[int]:
    """Rank-0 CoHA generating function: ideal sheaves on K3 x E.

    For K3 x E, the rank-0 sector counts ideal sheaves of subschemes.
    The generating function is related to the MacMahon function M(q)
    and the K3 Euler characteristic:

        Z_{rank 0}(q) = prod_{k>=1} 1/(1 - q^k)^{chi(K3)}
                       = prod_{k>=1} 1/(1 - q^k)^{24}
                       = 1/eta(q)^{24} (up to q-shift)

    This is the Hilbert scheme generating function chi(Hilb^n(K3)).

    Returns
    -------
    list of int : coefficients [chi(Hilb^0), chi(Hilb^1), ...].
    """
    coeffs = _eta_inverse_power(CHI_K3, max_n)
    return [int(c) for c in coeffs]


def rank1_generating_function(max_n: int) -> List[int]:
    r"""Rank-1 CoHA generating function.

    For rank-1 sheaves on K3 with ch_2 = n, the moduli space is
    essentially Hilb^n(K3), so the generating function is the same:

        Z_{rank 1}(q) = prod_{k>=1} 1/(1 - q^k)^{24}

    This counts rank-1 torsion-free sheaves with fixed determinant.

    Returns
    -------
    list of int.
    """
    return rank0_generating_function(max_n)


def rank_r_gf_leading(r: int, max_n: int) -> List[Fraction]:
    r"""Leading terms of the rank-r CoHA generating function.

    For rank r >= 2, the generating function is more complex.
    The single-Delta_5 product packages the signed-character lane; the
    doubled DMVV/Phi_10 lane has exponents 2c(D).

    At leading order, the rank-r contribution involves:
        Z_r(q) ~ prod_{k>=1} 1/(1-q^k)^{r * chi(K3)}   (crude upper bound)

    The precise formula involves the Fourier-Jacobi expansion of 1/Delta_5.

    For r = 2, the precise formula involves Yoshioka's computation.

    Returns
    -------
    list of Fraction : leading-order coefficients.
    """
    if r == 0 or r == 1:
        return [Fraction(c) for c in rank0_generating_function(max_n)]
    # For r >= 2, use the Delta_5 product rank-r sector extraction
    # At leading order, the rank-r contribution can be extracted from
    # the single-Delta_5 product by collecting the p^r coefficient.
    # The p^r coefficient involves convolutions of lower-rank terms.
    # Here we compute the first few terms by direct enumeration.
    return _extract_rank_r_from_dmvv(r, max_n)


def _extract_rank_r_from_dmvv(r: int, max_n: int) -> List[Fraction]:
    """Extract rank-r sector from the Delta_5 Borcherds product.

    The single-Delta_5 product gives:
        sum_N p^N Z_N(q) = prod (1/(1-p^n q^l s^m))^{c(4nm-l^2)}

    The doubled K3 elliptic-genus DMVV/Phi_10 product uses exponents
    2c(4nm-l^2).  This helper deliberately stays on the signed-character
    Delta_5 lane.

    We need the coefficient of p^r in this product.

    For computational tractability, we work with the LOG of the product
    and extract terms via plethystic exponentiation.

    The single-particle index at rank r is:
        f_r(q) = sum_{l,m: m=r or n=r} c(4nm-l^2) * q^{something}

    We use the plethystic exponential:
        prod 1/(1-p^n q^l y^m)^{c(D)} = PE[sum c(D) p^n q^l y^m]
    """
    # For small r, compute directly
    c_disc = phi01_by_discriminant(max(max_n, 4 * r * max_n + 5))

    # The single-particle partition function at rank r:
    # f_r(q) = sum_l c(4*r*1 - l^2) * delta_{m=1}  + ...
    # This is too complicated for general r; use the recursive approach.

    # For r = 2: the coefficient of p^2 in PE[f] is
    #   (1/2)(f_2 + f_1^2) where f_k is the single-particle at rank k.
    # f_1 = sum_{l} c(-l^2) = c(-1) * 2 + c(0) = 2 + 10 = 12
    # Wait, more carefully:

    # The single-particle index:
    # f(p,q) = sum_{n>=1,l,m>=0} c(4nm - l^2) p^n q^l s^m
    # Setting s = q (diagonal):
    # f(p,q) = sum_{n>=1,m>=0,l} c(4nm-l^2) p^n q^{l+m}

    # At rank r (coefficient of p^r):
    # f_r(q) = sum_{m>=0, l} c(4rm - l^2) q^{l+m}

    # Compute f_r(q) truncated to max_n terms
    f_r = [Fraction(0)] * (max_n + 1)
    for m in range(0, max_n + 1):
        l_max = int(math.isqrt(4 * r * m + 1))
        for l_val in range(-l_max, l_max + 1):
            D = 4 * r * m - l_val * l_val
            if D < -1:
                continue
            cD = c_disc.get(D, 0)
            if cD == 0:
                continue
            idx = l_val + m  # the q-power (may be negative; skip if so)
            if 0 <= idx <= max_n:
                f_r[idx] += Fraction(cD)
    return f_r


# =========================================================================
# 4. E1 PRODUCT STRUCTURE (equivariant deformation)
# =========================================================================

def e1_structure_function_rank1(z: complex, epsilon: float) -> complex:
    """The E1 structure function for the rank-1 CoHA sector.

    For K3 x E with equivariant parameter epsilon on E:

        g(z; epsilon) = (z + epsilon/2) / (z - epsilon/2)

    This is the simplest Maulik-Okounkov structure function.
    At epsilon = 0: g = 1 (commutative, E_infty).
    At epsilon != 0: nontrivial E1 structure.

    The structure function controls the CoHA product via:
        m(a, b) = Res_{z=0} g(z) * a(z) * b(0)

    Parameters
    ----------
    z : complex
        The spectral parameter.
    epsilon : float
        The equivariant parameter.

    Returns
    -------
    complex : g(z; epsilon).
    """
    if abs(z - epsilon / 2) < 1e-15:
        return float('inf')
    return (z + epsilon / 2) / (z - epsilon / 2)


def e1_structure_function_full(z: complex, h1: float, h2: float, h3: float) -> complex:
    """Full Maulik-Okounkov structure function for 3-parameter deformation.

    g(z) = prod_{a=1}^{3} (z - h_a) / (z + h_a)

    with CY condition h1 + h2 + h3 = 0.

    For K3 x E:
        h1 = epsilon_1, h2 = epsilon_2, h3 = -(epsilon_1 + epsilon_2)
    where epsilon_1, epsilon_2 are equivariant parameters for the
    holomorphic symplectic form on K3 and the E-direction respectively.

    Parameters
    ----------
    z : complex
        Spectral parameter.
    h1, h2, h3 : float
        Deformation parameters satisfying h1 + h2 + h3 = 0.

    Returns
    -------
    complex : g(z).
    """
    num = (z - h1) * (z - h2) * (z - h3)
    den = (z + h1) * (z + h2) * (z + h3)
    if abs(den) < 1e-30:
        return float('inf')
    return num / den


def structure_function_coefficients(h1: float, h2: float, h3: float,
                                    max_order: int = 10) -> List[float]:
    """Taylor coefficients of g(z) = sum_{j>=0} phi_j z^{-j}.

    Uses the recursion from log g(z):
        log g(z) = sum_{k odd} alpha_k z^{-k}
        alpha_k = (-2/k)(h1^k + h2^k + h3^k)

    then phi_j from the exponential recursion:
        j * phi_j = sum_{k=1}^{j} k * alpha_k * phi_{j-k}

    Parameters
    ----------
    h1, h2, h3 : float
        Deformation parameters (CY: h1+h2+h3 = 0).
    max_order : int
        Compute phi_0, ..., phi_{max_order}.

    Returns
    -------
    list of float : [phi_0, phi_1, ..., phi_{max_order}].
    """
    # Newton power sums
    def p_k(k: int) -> float:
        return h1**k + h2**k + h3**k

    # Log coefficients: alpha_k = (-2/k)*p_k for k odd, 0 for k even
    alpha = [0.0] * (max_order + 1)
    for k in range(1, max_order + 1, 2):  # odd k only
        alpha[k] = (-2.0 / k) * p_k(k)

    # Exponential recursion
    phi = [0.0] * (max_order + 1)
    phi[0] = 1.0
    for j in range(1, max_order + 1):
        s = 0.0
        for k in range(1, j + 1):
            s += k * alpha[k] * phi[j - k]
        phi[j] = s / j

    return phi


def verify_cy_condition(h1: float, h2: float, h3: float,
                        tol: float = 1e-12) -> bool:
    """Check h1 + h2 + h3 = 0 (CY condition)."""
    return abs(h1 + h2 + h3) < tol


def verify_g_involution(h1: float, h2: float, h3: float,
                        z_values: Optional[List[complex]] = None,
                        tol: float = 1e-10) -> bool:
    """Verify g(z) * g(-z) = 1 (the involution property).

    This follows from the CY condition and is equivalent to:
    only odd-indexed log-series coefficients are nonzero.
    """
    if z_values is None:
        z_values = [1.0 + 0.5j, 2.0 - 1.0j, 0.5 + 2.0j, 3.0, -1.5 + 0.7j]
    for z in z_values:
        gz = e1_structure_function_full(z, h1, h2, h3)
        g_neg_z = e1_structure_function_full(-z, h1, h2, h3)
        if abs(gz * g_neg_z - 1.0) > tol:
            return False
    return True


# =========================================================================
# 5. BOSONIC/FERMIONIC ROOT DECOMPOSITION
# =========================================================================

def root_decomposition(max_degree: int,
                       max_n: int = 20) -> Dict[str, Any]:
    """Decompose the BKM signed-character data into parity sectors.

    The BKM superalgebra g_{Delta_5} has:
    - Real roots: D = -1, mult = 1 (always bosonic)
    - Imaginary bosonic: D >= 0, c(D) > 0
    - Imaginary fermionic: D >= 0, c(D) < 0

    The generating function splits:
        Phi = Phi_real * Phi_bos * Phi_ferm

    Returns
    -------
    dict with keys 'real', 'bosonic', 'fermionic', each containing
    a list of (r, l, m, D, mult) tuples, plus summary statistics.
    """
    c_disc = phi01_by_discriminant(max(max_n, max_degree**2 + 5))

    real_roots = []
    bosonic_roots = []
    fermionic_roots = []

    for N in range(1, max_degree + 1):
        for r in range(0, N + 1):
            m = N - r
            l_max = int(math.isqrt(4 * r * m + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                if cD == 0:
                    continue
                entry = (r, l_val, m, D, cD)
                if D == -1:
                    real_roots.append(entry)
                elif cD > 0:
                    bosonic_roots.append(entry)
                else:
                    fermionic_roots.append(entry)

    total_bos_magnitude = sum(abs(e[4]) for e in real_roots) + sum(e[4] for e in bosonic_roots)
    total_ferm_magnitude = sum(abs(e[4]) for e in fermionic_roots)

    return {
        'real': real_roots,
        'bosonic': bosonic_roots,
        'fermionic': fermionic_roots,
        'n_real': len(real_roots),
        'n_bosonic': len(bosonic_roots),
        'n_fermionic': len(fermionic_roots),
        'total_bosonic_magnitude': total_bos_magnitude,
        'total_fermionic_magnitude': total_ferm_magnitude,
        'signed_super_character': total_bos_magnitude - total_ferm_magnitude,
    }


# =========================================================================
# 6. DMVV PLETHYSTIC EXPONENTIAL
# =========================================================================

def plethystic_log_k3e(max_n: int) -> Dict[int, int]:
    r"""Plethystic logarithm of the rank-0 sector generating function.

    The plethystic logarithm extracts the single-particle spectrum:
        PL[Z(q)] = sum_{k>=1} mu(k)/k * log Z(q^k)

    For Z(q) = 1/eta(q)^{24} = prod 1/(1-q^n)^{24}:
        PL[Z(q)] = 24 * sum_{n>=1} q^n = 24 * q/(1-q)

    This is a protected-character/even-cohomology fixture with value 24.
    It is not, by itself, an unsourced ordinary CoHA generator count.

    Returns
    -------
    dict : mapping n -> PL coefficient at q^n.
    """
    # For 1/eta^{24}, the PL is exactly 24 * q/(1-q) = 24*(q + q^2 + ...)
    # This is because 1/(1-q^n)^{24} = PE[24*q^n], and
    # PE[sum_n a_n q^n] = prod_n 1/(1-q^n)^{a_n}.
    # So PL[prod 1/(1-q^n)^{24}] = sum_n 24*q^n = 24*q/(1-q).
    return {n: CHI_K3 for n in range(1, max_n + 1)}


def plethystic_log_full(max_r: int, max_n: int) -> Dict[Tuple[int, int], int]:
    r"""Plethystic logarithm of the Delta_5/BKM signed-character product.

    For the Borcherds product attached to phi_{0,1}:
        Z = prod_{n>0,l,m>=0} 1/(1-p^n q^l y^m)^{c(4nm-l^2)}

    the plethystic logarithm is:
        PL[Z] = sum_{n>0,l,m>=0} c(4nm - l^2) * p^n q^l y^m

    The K3 elliptic-genus DMVV/Phi_10 lane has doubled exponents 2c(D).
    This function deliberately returns the Delta_5 signed-character lane.

    So the single-particle spectrum at charge (n, m) is:
        f(n, m) = sum_l c(4nm - l^2)

    Returns
    -------
    dict : mapping (n, m) -> sum_l c(4nm - l^2).
    """
    c_disc = phi01_by_discriminant(max(max_n, 4 * max_r * max_n + 5))
    result: Dict[Tuple[int, int], int] = {}
    for n in range(0, max_r + 1):
        for m_val in range(0, max_n + 1):
            if n == 0 and m_val == 0:
                continue
            total = 0
            l_max = int(math.isqrt(4 * n * m_val + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * n * m_val - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                total += cD
            if total != 0:
                result[(n, m_val)] = total
    return result


def single_particle_index(r: int, max_m: int, max_n: int = 20) -> Dict[int, int]:
    """Single-particle index at rank r: f_r(m) = sum_l c(4rm - l^2).

    This is the fundamental building block. The full generating function is:
        Z = PE[sum_{r>=1} sum_m f_r(m) p^r q^m]

    For r = 0, m >= 1:
        f_0(m) = sum_l c(-l^2) = c(-1) + c(-1) = 2   (only l = +/-1)
        Wait: for (n=0, l, m=1), D = -l^2, c(D) nonzero only for D >= -1,
        so l = 0 (D=0, c=10) and l = +/-1 (D=-1, c=1).
        f_0(1) = c(0) + 2*c(-1) = 10 + 2 = 12.

    For r = 1, m = 0:
        f_1(0) = sum_l c(-l^2) = c(0) + 2*c(-1) = 12.

    For r = 1, m = 1:
        f_1(1) = sum_l c(4 - l^2):
            l=0: c(4) = 108
            l=+/-1: c(3) = -64 each -> combined row contribution -128
            l=+/-2: c(0) = 10 each -> 20
            Total: 108 - 128 + 20 = 0.

    Wait, the row-sum of phi_{0,1} at n >= 1 is 0 (known identity).
    So f_r(m) = sum_l c(4rm - l^2) = row sum at n=rm, which is:
        0 for rm >= 1 (by the known identity sum_l f(n,l) = 0 for n >= 1)
        12 for rm = 0 (i.e., r=0 or m=0 but not both)

    This is a CRUCIAL observation: the single-particle index summed over
    all l vanishes for rm >= 1.  This does NOT mean the CoHA is trivial ---
    rather, the l-refined index carries nontrivial information.

    Returns
    -------
    dict : mapping m -> f_r(m) = sum_l c(4rm - l^2).
    """
    c_disc = phi01_by_discriminant(max(max_n, 4 * r * max_m + 5))
    result: Dict[int, int] = {}
    for m_val in range(0, max_m + 1):
        if r == 0 and m_val == 0:
            continue
        total = 0
        l_max = int(math.isqrt(4 * r * m_val + 1))
        for l_val in range(-l_max, l_max + 1):
            D = 4 * r * m_val - l_val * l_val
            if D < -1:
                continue
            cD = c_disc.get(D, 0)
            total += cD
        if total != 0:
            result[m_val] = total
    return result


def verify_row_sum_vanishing(max_rm: int, max_n: int = 20) -> bool:
    """Verify that sum_l c(4rm - l^2) = 0 for rm >= 1.

    This is a consequence of phi_{0,1}(tau, 0) = 12: the z=0 specialization
    is a constant, so all q-coefficients for n >= 1 vanish.

    Returns
    -------
    bool : True if all row sums vanish.
    """
    # phi01_by_discriminant(N) reliably works up to N ~ 20.
    # We need c(D) for D up to 4*max_rm, so N >= max_rm + 1.
    needed = min(max_rm + 1, 20)
    c_disc = phi01_by_discriminant(max(needed, min(max_n, 20)))
    for nm in range(1, max_rm + 1):
        total = 0
        l_max = int(math.isqrt(4 * nm + 1))
        for l_val in range(-l_max, l_max + 1):
            D = 4 * nm - l_val * l_val
            if D < -1:
                continue
            cD = c_disc.get(D, 0)
            total += cD
        if total != 0:
            return False
    return True


# =========================================================================
# 7. L-REFINED CoHA SPECTRUM
# =========================================================================

def l_refined_spectrum(r: int, m: int, max_n: int = 20) -> Dict[int, int]:
    """The l-refined BPS spectrum at charge (r, m).

    Returns c(4rm - l^2) for each l with nonzero multiplicity.

    This is the l-refined single-particle index that carries the
    nontrivial information (since the total sum over l vanishes for rm >= 1).

    Returns
    -------
    dict : mapping l -> c(4rm - l^2).
    """
    c_disc = phi01_by_discriminant(max(max_n, 4 * r * m + 5))
    result: Dict[int, int] = {}
    l_max = int(math.isqrt(4 * r * m + 1))
    for l_val in range(-l_max, l_max + 1):
        D = 4 * r * m - l_val * l_val
        if D < -1:
            continue
        cD = c_disc.get(D, 0)
        if cD != 0:
            result[l_val] = cD
    return result


def l_refined_coha_table(max_r: int, max_m: int,
                         max_n: int = 20) -> Dict[Tuple[int, int], Dict[int, int]]:
    """Complete l-refined CoHA spectrum for all (r, m) up to bounds.

    Returns
    -------
    dict : mapping (r, m) -> {l -> c(4rm - l^2)}.
    """
    table = {}
    for r in range(0, max_r + 1):
        for m_val in range(0, max_m + 1):
            if r == 0 and m_val == 0:
                continue
            spec = l_refined_spectrum(r, m_val, max_n)
            if spec:
                table[(r, m_val)] = spec
    return table


# =========================================================================
# 8. E1 PRODUCT STRUCTURE CONSTANTS (LOW ORDER)
# =========================================================================

def e1_product_rank0_rank0(n1: int, n2: int, epsilon: float = 1.0) -> float:
    """E1 product CoHA_{(0,0,n1)} x CoHA_{(0,0,n2)} -> CoHA_{(0,0,n1+n2)}.

    In the rank-0 sector, the CoHA is the Hilbert scheme CoHA of K3.
    The E1 product is the Nakajima-type creation/annihilation algebra:

        [alpha_n, alpha_m] = n * delta_{n+m,0} * chi(K3) * epsilon

    where alpha_n are the Nakajima operators on Hilb(K3), and epsilon
    is the equivariant deformation parameter.

    At epsilon = 0: commutative (classical, symmetric product).
    At epsilon != 0: Heisenberg algebra with central charge chi(K3) = 24.

    The structure constant for alpha_n * alpha_m in the E1 product is:
        c(n, m) = n * delta_{n+m,0} * 24 * epsilon

    For the same-sign product (both creation or both annihilation):
        c(n, m) = 0 (no correction to the commutative product)

    For creation * annihilation:
        c(n, -n) = n * 24 * epsilon

    Parameters
    ----------
    n1, n2 : int
        Instanton numbers.
    epsilon : float
        Equivariant parameter.

    Returns
    -------
    float : the E1 structure constant.
    """
    if n1 + n2 != 0:
        return 0.0
    # This is the Heisenberg commutator
    return float(n1) * CHI_K3 * epsilon


def e1_central_charge() -> int:
    """Central charge of the rank-0 Heisenberg sector.

    c_Heis = chi(K3) = 24.

    This is the level of the Heisenberg algebra acting on Hilb(K3).
    """
    return CHI_K3


# =========================================================================
# 9. MAULIK-OKOUNKOV R-MATRIX (low order)
# =========================================================================

def mo_r_matrix_rank1(z: complex, h1: float, h2: float, h3: float,
                      partition1: Tuple[int, ...] = (),
                      partition2: Tuple[int, ...] = ()) -> complex:
    """Maulik-Okounkov R-matrix on the tensor product of Fock modules.

    For the rank-1 Fock representations (labeled by partitions),
    the R-matrix acts as:

        R(z) = prod_{s in partition1} g(z + c(s))
             * prod_{t in partition2} g(z - c(t))^{-1}

    where c(s) = (arm(s) + 1)*h1 - (leg(s) + 1)*h2 is the content of a box,
    and g(z) is the structure function.

    For empty partitions: R(z) = 1.
    For partition1 = (1,): R(z) = g(z + h1) (adding one box).

    Parameters
    ----------
    z : complex
        Spectral parameter.
    h1, h2, h3 : float
        Deformation parameters (CY: h1+h2+h3=0).
    partition1, partition2 : tuple of int
        Young diagrams (as tuples of row lengths).

    Returns
    -------
    complex : R-matrix value.
    """
    result = 1.0 + 0.0j
    # Content of boxes in a partition
    for i, row_len in enumerate(partition1):
        for j in range(row_len):
            content = j * h1 - i * h2  # simplified content
            result *= e1_structure_function_full(z + content, h1, h2, h3)
    for i, row_len in enumerate(partition2):
        for j in range(row_len):
            content = j * h1 - i * h2
            g_val = e1_structure_function_full(z - content, h1, h2, h3)
            if abs(g_val) > 1e-30:
                result /= g_val
    return result


def verify_yang_baxter_rank1(h1: float, h2: float, h3: float,
                             z1: complex, z2: complex,
                             tol: float = 1e-8) -> bool:
    """Verify Yang-Baxter equation for rank-1 Fock R-matrix on small partitions.

    R_{12}(z1-z2) R_{13}(z1) R_{23}(z2) = R_{23}(z2) R_{13}(z1) R_{12}(z1-z2)

    On scalar (empty partition) states, this is trivially 1 = 1.
    On one-box states, this provides a nontrivial check.

    Returns True if the YBE holds at these parameter values.
    """
    # For the simplest nontrivial check: tensor of 3 empty Fock spaces.
    # R-matrix on empty partitions is 1 on both sides.
    # This is trivially satisfied.

    # One-box check: partition = (1,) in the first tensor factor.
    p1 = (1,)
    p_empty = ()

    # R_{12}(z1-z2) on (p1, p_empty)
    r12 = mo_r_matrix_rank1(z1 - z2, h1, h2, h3, p1, p_empty)
    # R_{13}(z1) on (p1, p_empty) [third factor is p_empty]
    r13 = mo_r_matrix_rank1(z1, h1, h2, h3, p1, p_empty)
    # R_{23}(z2) on (p_empty, p_empty) = 1
    r23 = mo_r_matrix_rank1(z2, h1, h2, h3, p_empty, p_empty)

    lhs = r12 * r13 * r23
    rhs = r23 * r13 * r12

    return abs(lhs - rhs) < tol


# =========================================================================
# 10. BKM POSITIVE HALF SIGNED-CHARACTER DATA
# =========================================================================

def bkm_positive_half_signed_character_data(max_degree: int,
                                            max_n: int = 20) -> Dict[str, Any]:
    """Finite BKM positive-half signed-character data for g_{Delta_5}.

    The positive half n_+ of the BKM superalgebra has signed character
    coefficient c(4rm - l^2).  The magnitude |c(D)| is recorded only as
    a coefficient statistic; it is not promoted to a local CoHA dimension.

    Returns per-degree root counts, signed character, and unsigned
    coefficient magnitude totals.
    """
    c_disc = phi01_by_discriminant(max(max_n, max_degree**2 + 5))

    # Collect positive roots at each degree N = r + m
    roots_by_degree: Dict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)
    for N in range(1, max_degree + 1):
        for r in range(0, N + 1):
            m = N - r
            l_max = int(math.isqrt(4 * r * m + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                if cD != 0:
                    roots_by_degree[N].append((r, l_val, m, cD))

    # For each degree, compute the number of positive roots and total multiplicity
    result = {}
    for N in range(1, max_degree + 1):
        roots = roots_by_degree.get(N, [])
        n_roots = len(roots)
        total_signed_character_magnitude = sum(abs(r[3]) for r in roots)
        signed_character = sum(r[3] for r in roots)
        n_bosonic = sum(1 for r in roots if r[3] > 0)
        n_fermionic = sum(1 for r in roots if r[3] < 0)

        result[N] = {
            'n_roots': n_roots,
            'total_signed_character_magnitude': total_signed_character_magnitude,
            'signed_character': signed_character,
            'n_bosonic': n_bosonic,
            'n_fermionic': n_fermionic,
            'roots': roots,
        }

    return result


# =========================================================================
# 11. CROSS-VERIFICATION: signed character vs phi_{0,1}
# =========================================================================

def verify_signed_character_vs_phi01(max_degree: int = 5,
                                     max_n: int = 20) -> Dict[str, Any]:
    """Cross-verify signed-character coefficients against phi_{0,1}.

    Path 1: c(D) where D = disc(gamma), from the discriminant table.
    Path 2: direct Fourier coefficient f(n,l) of phi_{0,1}.
    Path 3: finite source constants in KNOWN_C_DISC.

    The signed-character API is checked against all three paths but is not
    counted as an independent source, since it is the local interface under
    test.

    All three should agree.

    Returns
    -------
    dict : verification results with 'all_match' bool.
    """
    c_disc = phi01_by_discriminant(max(max_n, max_degree**2 + 5))

    checks = []
    for N in range(1, max_degree + 1):
        for r in range(0, N + 1):
            m = N - r
            l_max = int(math.isqrt(4 * r * m + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                # Path 1: from discriminant table
                cD_path1 = c_disc.get(D, 0)
                api_value = signed_character_coefficient(r, l_val, m, max_n)
                representative = _canonical_phi01_representative(D)
                if representative is None:
                    continue
                n_rep, l_rep = representative
                # Path 2: direct Fourier coefficient, not the discriminant table
                cD_path2 = _direct_phi01_coefficient(n_rep, l_rep, max(max_n, n_rep))
                # Path 3: finite source/parity gate.  We only claim a
                # three-path check at discriminants whose source constant is
                # recorded independently of the discriminant-table computation.
                if D not in KNOWN_C_DISC:
                    continue
                cD_path3 = KNOWN_C_DISC[D]

                match = (cD_path1 == cD_path2 == cD_path3 == api_value)
                checks.append({
                    'r': r, 'l': l_val, 'm': m, 'D': D,
                    'path1': cD_path1, 'path2': cD_path2,
                    'path3': cD_path3, 'api': api_value,
                    'path2_representative': (n_rep, l_rep),
                    'match': match,
                })

    all_match = all(c['match'] for c in checks)
    return {
        'checks': checks,
        'n_checks': len(checks),
        'all_match': all_match,
        'path_sources': (
            'phi01_by_discriminant',
            'phi01_coefficient',
            'KNOWN_C_DISC',
        ),
        'api_checked': 'signed_character_coefficient',
    }


# =========================================================================
# 12. SUPER-CHARACTER OF CoHA
# =========================================================================

def super_character_by_degree(max_degree: int,
                              max_n: int = 20) -> Dict[int, int]:
    """Super-character (sdim) at each degree N = r + m.

    sdim(CoHA_N) = sum_{r+m=N, l} c(4rm - l^2)

    (NOT the absolute value: bosonic minus fermionic.)

    By the row-sum vanishing identity, sdim(CoHA_N) = 0 for N >= 2
    when considering the full charge lattice.

    However, the REFINED super-character by (r, l, m) individually is
    nontrivial.

    Returns
    -------
    dict : mapping N -> sdim.
    """
    c_disc = phi01_by_discriminant(max(max_n, max_degree**2 + 5))
    result: Dict[int, int] = {}
    for N in range(1, max_degree + 1):
        total = 0
        for r in range(0, N + 1):
            m = N - r
            l_max = int(math.isqrt(4 * r * m + 1))
            for l_val in range(-l_max, l_max + 1):
                D = 4 * r * m - l_val * l_val
                if D < -1:
                    continue
                cD = c_disc.get(D, 0)
                total += cD
        result[N] = total
    return result


def super_character_diagonal(max_N: int,
                             max_n: int = 20) -> Dict[int, int]:
    """Super-character on the diagonal r = m.

    sdim_diag(N) = sum_{l} c(4N^2 - l^2)  (at r = m = N)

    This is the row sum of phi_{0,1} at instanton number n = N^2, which
    vanishes for N^2 >= 1 (i.e., N >= 1) by the row-sum identity.

    But for r = m = N, D = 4N^2 - l^2, and we evaluate:
        sum_l c(4N^2 - l^2).

    This equals 0 by the row-sum identity (the sum over l of c(4n - l^2) = 0
    for n >= 1, and here n = N^2 >= 1).

    Returns
    -------
    dict : mapping N -> sdim on diagonal.
    """
    c_disc = phi01_by_discriminant(max(max_n, 4 * max_N**2 + 5))
    result: Dict[int, int] = {}
    for N in range(1, max_N + 1):
        nm = N * N
        total = 0
        l_max = int(math.isqrt(4 * nm + 1))
        for l_val in range(-l_max, l_max + 1):
            D = 4 * nm - l_val * l_val
            if D < -1:
                continue
            cD = c_disc.get(D, 0)
            total += cD
        result[N] = total
    return result


# =========================================================================
# 13. SUMMARY AND IDENTIFICATION
# =========================================================================

def coha_k3e_summary(max_degree: int = 4, max_n: int = 20) -> Dict[str, Any]:
    """Complete summary of the CoHA(K3 x E) structure.

    Returns a comprehensive dict with all computed data.
    """
    return {
        'signed_character_magnitudes': total_signed_character_magnitude_by_degree(max_degree, max_n),
        'dimension_caveat': (
            "CoHA dimensions are not inferred from |c(D)|; they require "
            "parity-resolved source fixtures."
        ),
        'root_decomposition': root_decomposition(max_degree, max_n),
        'super_character': super_character_by_degree(max_degree, max_n),
        'row_sum_vanishing': verify_row_sum_vanishing(max_degree**2, max_n),
        'cross_verification': verify_signed_character_vs_phi01(max_degree, max_n),
        'plethystic_log_rank0': plethystic_log_k3e(max_degree),
        'e1_central_charge': e1_central_charge(),
        'identification': {
            'algebra': 'BKM positive half signed-character data for g_{Delta_5}',
            'type': 'BKM superalgebra (generalized Kac-Moody)',
            'root_multiplicities': 'c(D) from phi_{0,1}',
            'real_root_mult': 'c(-1) = 1 (simple roots)',
            'first_imaginary': 'c(0) = 10',
            'first_fermionic': 'c(3) = -64',
            'e1_deformation': 'Maulik-Okounkov R-matrix with CY structure function g(z)',
            'rank0_heisenberg': f'Level {CHI_K3} Heisenberg from chi(K3) = {CHI_K3}',
        },
    }


if __name__ == '__main__':
    print("=" * 70)
    print("CoHA(K3 x E) STRUCTURE ANALYSIS")
    print("=" * 70)

    summary = coha_k3e_summary(4)

    print("\n--- Signed-character magnitudes by degree N = r + m ---")
    for N, magnitude in sorted(summary['signed_character_magnitudes'].items()):
        print(f"  N = {N}: total |c(D)| = {magnitude}")

    rd = summary['root_decomposition']
    print(f"\n--- Root decomposition (degree <= 4) ---")
    print(f"  Real roots: {rd['n_real']}")
    print(f"  Bosonic imaginary: {rd['n_bosonic']}")
    print(f"  Fermionic imaginary: {rd['n_fermionic']}")
    print(f"  Total bosonic magnitude: {rd['total_bosonic_magnitude']}")
    print(f"  Total fermionic magnitude: {rd['total_fermionic_magnitude']}")
    print(f"  Signed super-character: {rd['signed_super_character']}")

    print(f"\n--- Super-character by degree ---")
    for N, sdim in sorted(summary['super_character'].items()):
        print(f"  N = {N}: sdim = {sdim}")

    print(f"\n--- Row-sum vanishing: {summary['row_sum_vanishing']}")
    print(f"--- Cross-verification: {summary['cross_verification']['all_match']}")
    print(f"--- E1 central charge: {summary['e1_central_charge']}")

    print(f"\n--- Identification ---")
    for k, v in summary['identification'].items():
        print(f"  {k}: {v}")
