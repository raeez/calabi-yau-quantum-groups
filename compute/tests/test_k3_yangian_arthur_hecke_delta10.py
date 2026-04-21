"""Tests for the Arthur-Hecke eigenvalue compute module (Wave 15 closure)."""
# Raeez Lorgat -- Wave 15 compute tests for the Saito-Kurokawa / Ikeda
# lift of the weight-16 elliptic newform to Delta_10.

from __future__ import annotations

import pytest

from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
    DELTA_E6_AP,
    PRIMES,
    delta_e6_coefficients,
    first_principles_a_p,
    hecke_eigenvalues,
    lambda_p_from_delta_e6,
    ramanujan_petersson_check,
    spinor_euler_factor,
    spinor_satake_roots,
    verify_andrianov_spinor_factorisation,
)


# ----------------------------------------------------------------------
# Primary-source reproduction: first-principles a_p from E_4 * Delta
# ----------------------------------------------------------------------


@pytest.mark.parametrize("p", PRIMES)
def test_first_principles_matches_table(p: int) -> None:
    """a_p in the table matches the first-principles E_4 * Delta computation."""
    assert DELTA_E6_AP[p] == first_principles_a_p(p)


@pytest.mark.parametrize("p", PRIMES)
def test_deligne_bound(p: int) -> None:
    """|a_p| <= 2 p^{15/2} for all tabulated primes."""
    a_p = DELTA_E6_AP[p]
    assert abs(a_p) <= 2 * p ** (15 / 2)


# ----------------------------------------------------------------------
# Hecke structure: multiplicativity and recursion
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "m,n",
    [(2, 3), (2, 5), (3, 5), (2, 7), (3, 7), (2, 11), (5, 7), (3, 11)],
)
def test_hecke_multiplicativity(m: int, n: int) -> None:
    """a_m * a_n = a_{mn} for coprime m, n.

    We verify using a first-principles computation of a_{mn} to order mn.
    """
    from math import comb

    N = m * n + 1

    def _sigma3(k: int) -> int:
        s = 0
        for d in range(1, k + 1):
            if k % d == 0:
                s += d ** 3
        return s

    e4 = [0] * (N + 1)
    e4[0] = 1
    for k in range(1, N + 1):
        e4[k] = 240 * _sigma3(k)

    eta24 = [0] * (N + 1)
    eta24[0] = 1
    for k in range(1, N + 1):
        factor = [0] * (N + 1)
        for j in range(0, 25):
            if k * j <= N:
                factor[k * j] = comb(24, j) * ((-1) ** j)
        new = [0] * (N + 1)
        for i in range(N + 1):
            if eta24[i] == 0:
                continue
            for jj in range(N + 1 - i):
                if factor[jj] == 0:
                    continue
                new[i + jj] += eta24[i] * factor[jj]
        eta24 = new

    delta = [0] * (N + 1)
    for i in range(N):
        delta[i + 1] = eta24[i]

    f16 = [0] * (N + 1)
    for i in range(N + 1):
        if e4[i] == 0:
            continue
        for j in range(N + 1 - i):
            f16[i + j] += e4[i] * delta[j]

    assert f16[m * n] == f16[m] * f16[n]


def test_hecke_recursion_p_equals_2() -> None:
    """a_{p^2} = a_p^2 - p^{15} at p = 2.

    216^2 - 2^15 = 46656 - 32768 = 13888.
    """
    from math import comb

    N = 5

    def _sigma3(k: int) -> int:
        s = 0
        for d in range(1, k + 1):
            if k % d == 0:
                s += d ** 3
        return s

    e4 = [0] * (N + 1)
    e4[0] = 1
    for k in range(1, N + 1):
        e4[k] = 240 * _sigma3(k)

    eta24 = [0] * (N + 1)
    eta24[0] = 1
    for k in range(1, N + 1):
        factor = [0] * (N + 1)
        for j in range(0, 25):
            if k * j <= N:
                factor[k * j] = comb(24, j) * ((-1) ** j)
        new = [0] * (N + 1)
        for i in range(N + 1):
            if eta24[i] == 0:
                continue
            for jj in range(N + 1 - i):
                if factor[jj] == 0:
                    continue
                new[i + jj] += eta24[i] * factor[jj]
        eta24 = new

    delta = [0] * (N + 1)
    for i in range(N):
        delta[i + 1] = eta24[i]

    f16 = [0] * (N + 1)
    for i in range(N + 1):
        if e4[i] == 0:
            continue
        for j in range(N + 1 - i):
            f16[i + j] += e4[i] * delta[j]

    # a_2^2 - 2^15 = a_4
    assert DELTA_E6_AP[2] ** 2 - 2 ** 15 == f16[4]
    assert f16[2] == DELTA_E6_AP[2]


# ----------------------------------------------------------------------
# Saito-Kurokawa: lambda_p = a_p + p^8 + p^9
# ----------------------------------------------------------------------


@pytest.mark.parametrize("p", PRIMES)
def test_saito_kurokawa_formula(p: int) -> None:
    """lambda_p(Delta_10) = a_p(Delta_E6) + p^8 + p^9."""
    a_p = DELTA_E6_AP[p]
    lam = lambda_p_from_delta_e6(p, a_p)
    assert lam == a_p + p ** 8 + p ** 9


@pytest.mark.parametrize("p", PRIMES)
def test_weissauer_ramanujan_petersson(p: int) -> None:
    """Weissauer 2009 RP: |lambda_p - p^8 - p^9| <= 2 p^{15/2}."""
    a_p = DELTA_E6_AP[p]
    lam = lambda_p_from_delta_e6(p, a_p)
    assert ramanujan_petersson_check(p, lam, a_p)


# ----------------------------------------------------------------------
# Spinor Euler factor: Andrianov factorisation
# ----------------------------------------------------------------------


@pytest.mark.parametrize("p", PRIMES)
def test_spinor_euler_factor_at_centre(p: int) -> None:
    """Spinor Euler factor at s = 9.5 (centre of symmetry) is nonzero finite.

    Z_p(s, Delta_10) = zeta_p(s-8) zeta_p(s-9) L_p(s, Delta_E6).
    """
    import cmath

    a_p = DELTA_E6_AP[p]
    z = spinor_euler_factor(p, complex(9.5, 0.0), a_p)
    assert cmath.isfinite(z.real) and cmath.isfinite(z.imag)
    assert abs(z) > 0.0


@pytest.mark.parametrize("p", PRIMES)
def test_satake_roots_unitary(p: int) -> None:
    """Reciprocal roots alpha, beta of 1 - a_p x + p^{15} x^2 have |alpha beta| = p^{15}."""
    a_p = DELTA_E6_AP[p]
    alpha, beta = spinor_satake_roots(p, a_p)
    # Product of reciprocal roots = p^{15} (Vieta's)
    prod = alpha * beta
    assert abs(prod.real - p ** 15) < 1e-3 * p ** 15
    assert abs(prod.imag) < 1e-3 * p ** 15


# ----------------------------------------------------------------------
# Aggregated verification surface
# ----------------------------------------------------------------------


def test_full_verification_surface() -> None:
    """Full Wave 15 surface: all primes verified, all RP checks pass."""
    summary = verify_andrianov_spinor_factorisation()
    assert set(summary["primes"]) == set(PRIMES)
    # Every prime carries a verified a_p (no None entries)
    for p in PRIMES:
        assert summary["delta_e6_coefficients"][p] is not None
        assert summary["hecke_eigenvalues"][p] is not None
    # Every prime passes RP
    for p, rp in summary["ramanujan_petersson"].items():
        assert rp, f"RP failed at p = {p}"


# ----------------------------------------------------------------------
# Wave 17 extension: primes in {41, 43, 47, 53, 59, 61, 67, 71, 73, 79}
# ----------------------------------------------------------------------


def test_w17_primes_first_principles_match() -> None:
    """First-principles a_p at p in [41, 79] matches hardcoded table."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        first_principles_a_p,
    )

    for p in PRIMES_W17:
        computed = first_principles_a_p(p)
        expected = DELTA_E6_AP_W17[p]
        assert computed == expected, (
            f"Wave 17 first-principles mismatch at p = {p}: "
            f"computed {computed}, tabulated {expected}"
        )


def test_w17_deligne_bound() -> None:
    """|a_p| <= 2 p^{15/2} for all Wave 17 primes."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
    )

    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        bound = 2 * (p ** 7.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(15/2) = {bound}"
        )


def test_w17_satake_cosine_in_unitary_range() -> None:
    """Satake parameter 2 cos(theta_p) is in [-2, 2] for all Wave 17 primes."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        satake_cosine,
    )

    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        cos2 = satake_cosine(p, a_p)
        assert -2.0 <= cos2 <= 2.0, (
            f"Satake parameter out of unitary range at p = {p}: {cos2}"
        )


def test_w17_saito_kurokawa_eigenvalues() -> None:
    """lambda_p(Delta_10) = a_p + p^8 + p^9 at Wave 17 primes."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        lambda_p_from_delta_e6,
    )

    expected = {
        41: 337008833641284,
        43: 513788409105136,
        47: 1139531074811904,
        53: 3368820433869396,
        59: 8819685113074800,
        61: 11890785248458324,
        67: 27583764247226224,
        71: 46619304364609344,
        73: 59595875344648516,
        79: 121343291713830400,
    }
    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        lam = lambda_p_from_delta_e6(p, a_p)
        assert lam == expected[p], (
            f"SK eigenvalue mismatch at p = {p}: {lam} != {expected[p]}"
        )


def test_w17_sk_euler_factor_at_nine_and_half_is_finite_nonzero() -> None:
    """Z_p(s=9.5) is finite and non-zero at all Wave 17 primes."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        spinor_euler_factor,
    )

    import math

    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        Zp = spinor_euler_factor(p, 9.5, a_p)
        assert math.isfinite(Zp.real) and math.isfinite(Zp.imag), (
            f"Z_p(9.5) not finite at p = {p}: {Zp}"
        )
        assert abs(Zp) > 1e-12, (
            f"Z_p(9.5) vanishes at p = {p}: {Zp}"
        )


def test_w17_frenkel_reshetikhin_casimir_in_range() -> None:
    """C_2 Casimir eigenvalue = 2 cos(2 theta_p) is in [-2, 2]."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        frenkel_reshetikhin_c2_eigenvalue,
    )

    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        c2 = frenkel_reshetikhin_c2_eigenvalue(p, a_p)
        assert -2.0 <= c2 <= 2.0, (
            f"FR C_2 eigenvalue out of range at p = {p}: {c2}"
        )


def test_w17_hecke_multiplicativity_w14_w17_joined() -> None:
    """a_{p*q} = a_p * a_q for distinct primes with p*q <= 79 (bridges both waves)."""
    from compute.lib.k3_yangian_wave14_arthur_hecke_delta10 import (
        first_principles_a_p,
    )

    pairs = [
        (2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (2, 19),
        (3, 5), (3, 7), (3, 11), (3, 13), (3, 17), (3, 19), (3, 23),
        (5, 7), (5, 11), (5, 13), (7, 11),
    ]
    for p, q in pairs:
        lhs = first_principles_a_p(p) * first_principles_a_p(q)
        rhs = first_principles_a_p(p * q, N=p * q)
        assert lhs == rhs, (
            f"Hecke multiplicativity failed at ({p}, {q}): "
            f"{lhs} != {rhs}"
        )
