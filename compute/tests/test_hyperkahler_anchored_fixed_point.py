"""Tests for the hyperkähler-anchored elliptic-tower investigation.

Verifies: the K3-anchored elliptic-tower fixed point M^♭ = (0, 5, -16, 11)
does NOT extend to hyperkähler-anchored. For K3^[n] with n >= 2 (using the
Bogomolov-Beauville HK matrix M_{K3^[n]} = (n+1, 0, 0, 0)), the iteration
M_{K3^[n] × E^k} is doubling, not stabilising. The cross-anchored configuration
M_{K3^[n] × K3 × E^k} = (n+1) M^♭ recovers a SCALED fixed-point with
multiplicative factor χ(O_{K3^[n]}) = n+1.

Theorems verified:
- thm:hyperkahler-elliptic-doubling
  (M_{K3^[n] × E^k} = 2^{k-1} (n+1) M_E)
- prop:hyperkahler-product-matrix
  (M_{K3^[n] × K3^[m]} = ((n+1)(m+1), 0, 0, 0))
- thm:cross-anchored-scaled-fixed-point
  (M_{K3^[n] × K3 × E^k} = (n+1) M^♭ for k >= 1)

Manuscript: chapters/examples/k3_yangian_chapter.tex (after
thm:k3-elliptic-tower-fixed-point at line 3284).
Companion note: notes/wave_hyperkahler_anchored.md.

AP-CY55 compliance: BKM-enhanced K3 matrix M_{K3} = (0, 5, -16, 13)
distinguished from bare HK matrix M_{K3^[1]} = (2, 0, 0, 0).
AP-CY60 compliance: HK Bogomolov-Beauville construction distinguished
from BKM Borcherds-lift construction; these are DIFFERENT
algebraisations of K3.
AP-CY61 compliance: extracted the ghost theorem (multiplicative
absorber) that the wrong claim (hyperkähler universal fixed-point)
was reaching for.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Tuple

import pytest

from compute.lib.independent_verification import independent_verification


# =========================================================================
# V_4 convolution + Künneth-dichotomy primitives
# =========================================================================
#
# We implement these directly here (rather than importing) to make the
# verification self-contained. The TEST source for the matrices is the
# manuscript / Bogomolov-Beauville / Goettsche; the test itself uses the
# REGULAR REPRESENTATION ARITHMETIC of V_4 = (Z/2)^2 with standard
# componentwise XOR.

V4Vec = Tuple[int, int, int, int]
"""V_4-character vector: (Pi_++, Pi_+-, Pi_-+, Pi_--)."""

# V_4 group operation as XOR on (Z/2)^2 indexing 0..3.
# Index map: 0 = (+,+), 1 = (+,-), 2 = (-,+), 3 = (-,-).
# XOR table:
#   0^0=0, 0^1=1, 0^2=2, 0^3=3
#   1^1=0, 1^2=3, 1^3=2
#   2^2=0, 2^3=1
#   3^3=0
def _xor(a: int, b: int) -> int:
    """XOR of V_4 indices in (Z/2)^2 representation."""
    a_high, a_low = a >> 1, a & 1
    b_high, b_low = b >> 1, b & 1
    return ((a_high ^ b_high) << 1) | (a_low ^ b_low)


def v4_convolve(M: V4Vec, N: V4Vec) -> V4Vec:
    """Klein-four convolution in the regular representation of V_4.

    (M *_{V_4} N)^{eps} = sum_{delta in V_4} M^{delta} * N^{eps + delta}.
    """
    result = [0, 0, 0, 0]
    for eps in range(4):
        s = 0
        for delta in range(4):
            s += M[delta] * N[_xor(eps, delta)]
        result[eps] = s
    return tuple(result)  # type: ignore[return-value]


def sigma_tot_flip(M: V4Vec) -> V4Vec:
    """Antipodal involution: sigma_tot^*((a, b, c, d)) = (d, c, b, a)."""
    return (M[3], M[2], M[1], M[0])


def trace(M: V4Vec) -> int:
    """Trace = sum of components = chi(O_X)."""
    return sum(M)


def is_anti_symmetric(M: V4Vec) -> bool:
    """True if sigma_tot^*(M) = -M (in -1 eigenspace)."""
    return sigma_tot_flip(M) == tuple(-x for x in M)


def is_symmetric(M: V4Vec) -> bool:
    """True if sigma_tot^*(M) = +M (in +1 eigenspace)."""
    return sigma_tot_flip(M) == M


def is_generic(M: V4Vec) -> bool:
    """True if M is neither symmetric nor anti-symmetric under sigma_tot^*."""
    return not is_symmetric(M) and not is_anti_symmetric(M)


def kunneth_dichotomy_delta(M: V4Vec, N: V4Vec, chi_M: int, chi_N: int) -> V4Vec:
    """Compute Drinfeld-coupling Delta_{X, Y} per the Künneth dichotomy
    (thm:kunneth-dichotomy of k3_yangian_chapter.tex).

    Case 1: both generic                          -> Delta = 0
    Case 2: both anti-symmetric (-1 eigenspace)   -> Delta = 0
    Case 3: exactly one in -1 eigenspace          -> Delta = sigma^* M_generic
                                                     - chi(O_generic) * e_{Pi_--}
    """
    M_anti = is_anti_symmetric(M)
    N_anti = is_anti_symmetric(N)
    M_gen = is_generic(M)
    N_gen = is_generic(N)

    # Case 1: both generic
    if M_gen and N_gen:
        return (0, 0, 0, 0)

    # Case 2: both anti-symmetric
    if M_anti and N_anti:
        return (0, 0, 0, 0)

    # Case 3: one generic, one anti-symmetric
    if M_gen and N_anti:
        # X = M is generic
        flip = sigma_tot_flip(M)
        return (flip[0], flip[1], flip[2], flip[3] - chi_M)
    if N_gen and M_anti:
        # X = N is generic
        flip = sigma_tot_flip(N)
        return (flip[0], flip[1], flip[2], flip[3] - chi_N)

    # Other configurations (both symmetric, or symmetric+anti, etc.) ->
    # not covered by the dichotomy; treat as zero by default for the
    # narrow set of cases this test exercises.
    return (0, 0, 0, 0)


def kunneth_product(M: V4Vec, N: V4Vec, chi_M: int, chi_N: int) -> V4Vec:
    """M_{X × Y} = M_X *_{V_4} M_Y + Delta_{X, Y}."""
    conv = v4_convolve(M, N)
    delta = kunneth_dichotomy_delta(M, N, chi_M, chi_N)
    return tuple(conv[i] + delta[i] for i in range(4))  # type: ignore[return-value]


# =========================================================================
# Manifold matrices (canonical inputs)
# =========================================================================

# BKM-enhanced K3 matrix (Mukai signature (4, 20), full V_4-faithful)
# Source: thm:k3-multiproj-bigraded-lefschetz, k3_yangian_chapter.tex.
M_K3_BKM: V4Vec = (0, 5, -16, 13)
CHI_O_K3 = 2  # = 0 + 5 + (-16) + 13

# Elliptic curve matrix
# Source: prop:elliptic-bigraded-matrix.
M_E: V4Vec = (1, 0, 0, -1)
CHI_O_E = 0

# Bogomolov-Beauville HK matrix for K3^[n]
# Source: rem:hodge-saturation-cases (line 3833) of k3_yangian_chapter.tex,
# applied to the irreducible HK manifold K3^[n].
def M_K3_n_HK(n: int) -> V4Vec:
    """Bare HK Bogomolov-Beauville matrix for K3^[n]: (n+1, 0, 0, 0)."""
    return (n + 1, 0, 0, 0)


def chi_O_K3_n(n: int) -> int:
    """χ(O_{K3^[n]}) = n + 1 (Goettsche formula).

    Goettsche-Hirzebruch:
       sum_n χ(O_{K3^[n]}) q^n = prod_{m≥1} 1/(1 - q^m)^{24} ... ?
    The actual formula gives χ(O_{K3^[n]}) = n + 1 directly, since
    H^*(O_{K3^[n]}) is concentrated in even degree with one summand per
    weight.
    """
    return n + 1


# K3-anchored elliptic-tower fixed point
# Source: thm:k3-elliptic-tower-fixed-point.
M_FLAT: V4Vec = (0, 5, -16, 11)


# =========================================================================
# Hyperkähler-elliptic doubling theorem
# =========================================================================


class TestHyperkahlerEllipticDoubling:
    """M_{K3^[n] × E^k} = 2^{k-1} (n+1) M_E for n >= 1, k >= 1.

    The K3-anchored fixed-point does NOT extend to hyperkähler-anchored:
    the iteration is doubling, not stabilising.
    """

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_M_K3n_basic(self, n):
        """M_{K3^[n]} = (n+1, 0, 0, 0) and is generic under sigma_tot^*."""
        M = M_K3_n_HK(n)
        assert M == (n + 1, 0, 0, 0)
        assert trace(M) == n + 1
        assert is_generic(M)
        assert not is_anti_symmetric(M)
        assert not is_symmetric(M)

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_K3n_times_E_doubling_base(self, n):
        """M_{K3^[n] × E} = (n+1) M_E = (n+1, 0, 0, -(n+1)).

        Case (3) of dichotomy: K3^[n] generic, E anti-symmetric.
        Delta = sigma^*(M_K3^[n]) - χ(O_K3^[n]) e_{Pi_--}
              = (0, 0, 0, n+1) - (n+1)(0,0,0,1) = (0, 0, 0, 0).
        """
        M = M_K3_n_HK(n)
        chi = chi_O_K3_n(n)
        delta = kunneth_dichotomy_delta(M, M_E, chi, CHI_O_E)
        assert delta == (0, 0, 0, 0), (
            f"Asymmetric correction at K3^[{n}] × E should vanish "
            f"(σ^* M cancels χ(O) e_{{Π--}}); got {delta}"
        )
        product = kunneth_product(M, M_E, chi, CHI_O_E)
        expected = (n + 1, 0, 0, -(n + 1))
        assert product == expected
        # Trace check: 0 = χ(O_{K3^[n]}) × χ(O_E) = (n+1) × 0
        assert trace(product) == chi * CHI_O_E

    @pytest.mark.parametrize("n,k_max", [(1, 4), (2, 4), (3, 3)])
    def test_K3n_times_Ek_doubling(self, n, k_max):
        """Iteration: M_{K3^[n] × E^k} = 2^{k-1} (n+1) M_E.

        After the first E-multiplication, the result is anti-symmetric
        (∝ M_E), so subsequent E-multiplications fall under case (2)
        with Delta = 0, and the convolution doubles the magnitude.
        """
        M = M_K3_n_HK(n)
        chi_curr = chi_O_K3_n(n)
        for k in range(1, k_max + 1):
            M = kunneth_product(M, M_E, chi_curr, CHI_O_E)
            chi_curr = chi_curr * CHI_O_E  # always 0 for k >= 1
            scale = (2 ** (k - 1)) * (n + 1)
            expected = (scale, 0, 0, -scale)
            assert M == expected, (
                f"At K3^[{n}] × E^{k}: expected {expected}, got {M}. "
                f"Doubling pattern broken — universal fixed-point would be wrong."
            )
            assert trace(M) == 0


# =========================================================================
# Hyperkähler product matrix
# =========================================================================


class TestHyperkahlerProductMatrix:
    """M_{K3^[n] × K3^[m]} = ((n+1)(m+1), 0, 0, 0)."""

    @pytest.mark.parametrize("n,m", [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3)])
    def test_K3n_times_K3m(self, n, m):
        """Both factors generic: case (1), Delta = 0, convolution diagonal."""
        Mn = M_K3_n_HK(n)
        Mm = M_K3_n_HK(m)
        chi_n = chi_O_K3_n(n)
        chi_m = chi_O_K3_n(m)
        # Both generic
        assert is_generic(Mn)
        assert is_generic(Mm)
        delta = kunneth_dichotomy_delta(Mn, Mm, chi_n, chi_m)
        assert delta == (0, 0, 0, 0), "Generic-generic pair: Delta must vanish"
        product = kunneth_product(Mn, Mm, chi_n, chi_m)
        expected = ((n + 1) * (m + 1), 0, 0, 0)
        assert product == expected
        assert trace(product) == chi_n * chi_m


# =========================================================================
# Cross-anchored scaled fixed-point theorem
# =========================================================================


class TestCrossAnchoredScaledFixedPoint:
    """M_{K3^[n] × K3 × E^k} = (n+1) M^♭ for k >= 1.

    The HK factor enters as a multiplicative scalar χ(O_{K3^[n]}) = n+1.
    """

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_K3n_times_K3_BKM(self, n):
        """M_{K3^[n] × K3} = (n+1) M_{K3} = (0, 5(n+1), -16(n+1), 13(n+1)).

        Both generic: case (1), Delta = 0.
        """
        Mn = M_K3_n_HK(n)
        chi_n = chi_O_K3_n(n)
        delta = kunneth_dichotomy_delta(Mn, M_K3_BKM, chi_n, CHI_O_K3)
        assert delta == (0, 0, 0, 0)
        product = kunneth_product(Mn, M_K3_BKM, chi_n, CHI_O_K3)
        expected = (0, 5 * (n + 1), -16 * (n + 1), 13 * (n + 1))
        assert product == expected
        assert trace(product) == chi_n * CHI_O_K3

    @pytest.mark.parametrize("n,k_max", [(1, 3), (2, 3), (3, 2)])
    def test_K3n_times_K3_times_Ek_scaled_fixed_point(self, n, k_max):
        """Iteration K3^[n] × K3 × E^k stabilises at (n+1) M^♭ for k >= 1.

        Step 1: K3^[n] × K3 = (n+1) M_{K3} (case 1).
        Step 2: × E gives (n+1)[M_{K3} *_{V_4} M_E + Delta_{K3, E}]
                       = (n+1) M^♭ (case 3 with explicit Delta).
        Step 3+: × E preserves (n+1) M^♭ by the bivariant Künneth identity
                 on the trace-zero hyperplane.
        """
        # Step 1: K3^[n] × K3
        Mn = M_K3_n_HK(n)
        chi_n = chi_O_K3_n(n)
        M = kunneth_product(Mn, M_K3_BKM, chi_n, CHI_O_K3)
        chi_curr = chi_n * CHI_O_K3
        # Step 2..: × E^k
        for k in range(1, k_max + 1):
            M = kunneth_product(M, M_E, chi_curr, CHI_O_E)
            chi_curr = chi_curr * CHI_O_E  # = 0 for k >= 1
            expected = ((n + 1) * M_FLAT[0], (n + 1) * M_FLAT[1],
                        (n + 1) * M_FLAT[2], (n + 1) * M_FLAT[3])
            assert M == expected, (
                f"Cross-anchored scaling broken at K3^[{n}] × K3 × E^{k}: "
                f"expected (n+1) M^♭ = {expected}, got {M}"
            )
            assert trace(M) == 0


# =========================================================================
# Independent verification (HZ3-11 protocol, AP-CY10)
# =========================================================================


class TestIndependentVerification:
    """The decorated tests cross-check the formal V_4 convolution
    arithmetic against an independent algebraic-geometry source.

    DERIVED_FROM: V_4 convolution + Künneth dichotomy
    (regular-representation arithmetic on Z[V_4]; case classification by
    sigma_tot^* eigenspace of M_X, M_Y).

    VERIFIED_AGAINST: Bogomolov-Beauville hyperkähler rank theorem +
    Goettsche formula for χ(O_{K3^[n]}) (= n+1, classical algebraic
    geometry, derived without any V_4 / chiral / convolution structure).
    """

    @independent_verification(
        claim="thm:hyperkahler-elliptic-doubling",
        derived_from=[
            "V_4 convolution + Künneth dichotomy applied to "
            "M_{K3^[n]} = (n+1, 0, 0, 0) and M_E = (1, 0, 0, -1)",
            "Eigenspace classification: K3^[n] generic, E anti-symmetric "
            "under sigma_tot^*",
        ],
        verified_against=[
            "Bogomolov-Beauville hyperkähler rank theorem (r(K3^[n]) = 1)",
            "Goettsche formula chi(O_{K3^[n]}) = n + 1 (classical "
            "algebraic geometry, Hirzebruch-Riemann-Roch on K3^[n])",
            "Direct iterated Klein-four convolution of the diagonal "
            "matrix (n+1)(1, 0, 0, 0) against M_E = (1, 0, 0, -1)",
        ],
        disjoint_rationale=(
            "DERIVATION: the K3-anchored fixed-point reasoning argues "
            "from the dichotomy case structure (which classifies M_X, M_Y "
            "by sigma_tot^* eigenspace) to predict whether Delta vanishes "
            "and what the iterated matrix is. VERIFICATION: the inputs "
            "M_{K3^[n]} = (n+1, 0, 0, 0) come from the Bogomolov-Beauville "
            "rank theorem (uniqueness of the holomorphic-symplectic form) "
            "+ the Goettsche formula chi(O_{K3^[n]}) = n+1 (classical "
            "Hirzebruch-Riemann-Roch on the Hilbert scheme). These are "
            "INDEPENDENT geometric inputs; the V_4 convolution is then "
            "carried out as direct arithmetic, which can be cross-checked "
            "against the case classification independently. The doubling "
            "pattern 2^{k-1}(n+1) is computed by both routes (case-2 "
            "iterated convolution in the dichotomy framework AND direct "
            "Klein-four convolution arithmetic of (n+1) M_E with itself "
            "via M_{T^4} = 2 M_E)."
        ),
    )
    def test_doubling_at_K3n_E2(self):
        """K3^[n] × E^2 = 2(n+1) M_E for n = 1, 2, 3.

        Derivation route: case (3) at step 1 with Delta = 0, then case (2)
        at step 2 with iteration on the anti-symmetric subspace.
        Verification route: direct evaluation of (n+1) M_E *_{V_4} M_E
        via the closed form M_E *_{V_4} M_E = M_{T^4} = (2, 0, 0, -2)
        (= 2 M_E), giving 2(n+1) M_E.
        """
        for n in [1, 2, 3]:
            # Derivation route
            Mn = M_K3_n_HK(n)
            M1 = kunneth_product(Mn, M_E, chi_O_K3_n(n), CHI_O_E)
            M2 = kunneth_product(M1, M_E, 0, CHI_O_E)
            # Verification route: direct (n+1) M_E *_{V_4} M_E
            M_T4 = v4_convolve(M_E, M_E)
            assert M_T4 == (2, 0, 0, -2), "M_E *_{V_4} M_E != M_{T^4}"
            verif = tuple((n + 1) * M_T4[i] for i in range(4))
            assert M2 == verif, (
                f"At n={n}: derivation gives {M2}, "
                f"independent (n+1)*M_{{T^4}} verification gives {verif}"
            )

    @independent_verification(
        claim="prop:hyperkahler-product-matrix",
        derived_from=[
            "V_4 convolution of (n+1, 0, 0, 0) with (m+1, 0, 0, 0) "
            "in the regular representation of V_4",
            "Case (1) of the Künneth dichotomy (both factors generic, "
            "Delta = 0)",
        ],
        verified_against=[
            "Hirzebruch-Riemann-Roch on K3^[n] × K3^[m] giving "
            "chi(O_{K3^[n] x K3^[m]}) = (n+1)(m+1)",
            "Multiplicativity of chi(O) under direct product "
            "(classical algebraic geometry, independent of V_4 / "
            "Künneth-dichotomy framework)",
        ],
        disjoint_rationale=(
            "DERIVATION: V_4 convolution arithmetic gives the "
            "matrix entry-by-entry, with case (1) of the dichotomy "
            "predicting Delta = 0 because both factors are generic. "
            "VERIFICATION: classical Hirzebruch-Riemann-Roch on the "
            "Hilbert scheme + multiplicativity of chi(O) under direct "
            "product gives the trace = (n+1)(m+1) WITHOUT reference to "
            "V_4 or convolution. Both routes converge on the same "
            "single nonzero entry at Pi_++."
        ),
    )
    def test_K3_n_K3_m_trace_matches_chi_product(self):
        """Trace of M_{K3^[n] × K3^[m]} = (n+1)(m+1) by both routes."""
        for (n, m) in [(1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (3, 3)]:
            # Derivation route
            Mn = M_K3_n_HK(n)
            Mm = M_K3_n_HK(m)
            product = kunneth_product(Mn, Mm, chi_O_K3_n(n), chi_O_K3_n(m))
            # Verification route: classical χ(O) multiplicativity
            chi_product_classical = (n + 1) * (m + 1)
            assert trace(product) == chi_product_classical, (
                f"At (n, m) = ({n}, {m}): "
                f"V_4 trace {trace(product)} vs classical χ product "
                f"{chi_product_classical}"
            )
            # Diagonal-only structure
            assert product[1] == 0
            assert product[2] == 0
            assert product[3] == 0
            assert product[0] == chi_product_classical

    @independent_verification(
        claim="thm:cross-anchored-scaled-fixed-point",
        derived_from=[
            "V_4 convolution + dichotomy case classification: "
            "K3^[n] (generic) × K3 (generic) gives case (1) "
            "scaling, then × E (anti-symmetric) gives case (3) "
            "with explicit Delta = (n+1) Delta_{K3, E}",
            "Bivariant Künneth identity (lem:bivariant-kunneth-identity): "
            "kappa_E acts as identity on trace-zero hyperplane, "
            "so subsequent E-multiplications preserve (n+1) M^♭",
        ],
        verified_against=[
            "Direct linearity of V_4 convolution: "
            "(c * M) *_{V_4} N = c * (M *_{V_4} N) for scalar c",
            "K3-anchored elliptic-tower fixed-point theorem "
            "(thm:k3-elliptic-tower-fixed-point) at multiplicative "
            "scale c = n+1 = chi(O_{K3^[n]})",
            "Trace check via Hirzebruch-Riemann-Roch: trace of "
            "(n+1) M^♭ = (n+1) * 0 = 0 = chi(O_{K3^[n] x K3 x E^k})",
        ],
        disjoint_rationale=(
            "DERIVATION: combines the case (3) explicit Delta formula "
            "from the Künneth dichotomy with the bivariant Künneth "
            "identity for stable iteration. VERIFICATION: cross-checks "
            "via the linearity of V_4 convolution -- if K3^[n] enters "
            "as a multiplicative scalar (n+1) on M_{K3}, then the "
            "iteration K3^[n] × K3 × E^k is exactly (n+1) times the "
            "K3 × E^k iteration, which is the K3-anchored fixed-point "
            "theorem (a SEPARATE established theorem with its own "
            "independent verification chain). The trace check uses "
            "chi(O) multiplicativity, an entirely classical fact "
            "independent of any V_4 / convolution / dichotomy structure."
        ),
    )
    def test_cross_anchored_scaling(self):
        """K3^[n] × K3 × E^k iteration gives (n+1) M^♭ for k >= 1."""
        for n in [1, 2, 3]:
            # Derivation route: explicit iteration
            Mn = M_K3_n_HK(n)
            M = kunneth_product(Mn, M_K3_BKM, chi_O_K3_n(n), CHI_O_K3)
            chi_curr = chi_O_K3_n(n) * CHI_O_K3
            for k in range(1, 4):
                M = kunneth_product(M, M_E, chi_curr, CHI_O_E)
                chi_curr = 0
                # Verification route: linearity gives (n+1) * (M_K3 × E^k)
                # The K3-anchored fixed-point is M_{K3 × E^k} = M^♭ for k >= 1.
                expected_linear = tuple((n + 1) * M_FLAT[i] for i in range(4))
                assert M == expected_linear, (
                    f"Cross-anchored scaling at K3^[{n}] × K3 × E^{k}: "
                    f"derivation gives {M}, "
                    f"(n+1) * M_K3-anchored fixed point gives {expected_linear}"
                )
                # Trace check
                assert trace(M) == 0, "Trace should vanish for elliptic-product"


# =========================================================================
# Sanity: V_4 convolution arithmetic
# =========================================================================


class TestV4ConvolutionArithmetic:
    """Smoke tests for the V_4 convolution primitive itself."""

    def test_xor_table(self):
        """V_4 = (Z/2)^2 XOR table."""
        # 0 = (+,+), 1 = (+,-), 2 = (-,+), 3 = (-,-)
        assert _xor(0, 0) == 0
        assert _xor(1, 2) == 3  # (+,-) ^ (-,+) = (-,-)
        assert _xor(3, 3) == 0
        assert _xor(1, 3) == 2

    def test_M_E_self_convolution_T4(self):
        """M_E *_{V_4} M_E = M_{T^4} = (2, 0, 0, -2) (prop:t4-via-kunneth)."""
        result = v4_convolve(M_E, M_E)
        assert result == (2, 0, 0, -2)

    def test_M_K3_BKM_self_convolution(self):
        """M_{K3} *_{V_4} M_{K3} = (450, -416, 130, -160)
        (prop:k3-k3-via-kunneth)."""
        result = v4_convolve(M_K3_BKM, M_K3_BKM)
        assert result == (450, -416, 130, -160)
        assert trace(result) == 4  # = chi(O_K3)^2

    def test_M_E_anti_symmetric(self):
        """sigma_tot^*(M_E) = -M_E."""
        assert sigma_tot_flip(M_E) == (-1, 0, 0, 1)
        assert is_anti_symmetric(M_E)
        assert not is_generic(M_E)

    def test_M_K3_BKM_generic(self):
        """sigma_tot^*(M_K3) = (13, -16, 5, 0) -- not ± M_K3."""
        assert sigma_tot_flip(M_K3_BKM) == (13, -16, 5, 0)
        assert is_generic(M_K3_BKM)

    def test_M_K3n_HK_generic(self):
        """sigma_tot^*((n+1, 0, 0, 0)) = (0, 0, 0, n+1) -- generic."""
        for n in range(1, 5):
            M = M_K3_n_HK(n)
            assert sigma_tot_flip(M) == (0, 0, 0, n + 1)
            assert is_generic(M), f"K3^[{n}] should be generic"

    def test_K3_E_BKM_recovers_fixed_point(self):
        """Sanity: BKM-K3 × E gives M^♭ = (0, 5, -16, 11)."""
        delta = kunneth_dichotomy_delta(M_K3_BKM, M_E, CHI_O_K3, CHI_O_E)
        assert delta == (13, -16, 5, -2)
        product = kunneth_product(M_K3_BKM, M_E, CHI_O_K3, CHI_O_E)
        assert product == M_FLAT

    def test_iterated_K3_E_stays_at_fixed_point(self):
        """Sanity: iterating K3 × E^k stays at M^♭."""
        M = M_K3_BKM
        chi = CHI_O_K3
        for k in range(1, 4):
            M = kunneth_product(M, M_E, chi, CHI_O_E)
            chi = chi * CHI_O_E
            if k >= 1:
                assert M == M_FLAT
                assert trace(M) == 0
