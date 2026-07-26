"""Tests for the Arthur-Hecke eigenvalue compute module (Wave 15 closure)."""
# Raeez Lorgat -- Wave 15 compute tests for the Saito-Kurokawa / Ikeda
# lift of the weight-18 elliptic newform to Delta_10.

from __future__ import annotations

import pytest

from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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
# Primary-source reproduction: first-principles a_p from E_6 * Delta
# ----------------------------------------------------------------------


@pytest.mark.parametrize("p", PRIMES)
def test_first_principles_matches_table(p: int) -> None:
    """a_p in the table matches the first-principles E_6 * Delta computation."""
    assert DELTA_E6_AP[p] == first_principles_a_p(p)


@pytest.mark.parametrize("p", PRIMES)
def test_deligne_bound(p: int) -> None:
    """|a_p| <= 2 p^{17/2} for all tabulated primes."""
    a_p = DELTA_E6_AP[p]
    assert abs(a_p) <= 2 * p ** (17 / 2)


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

    def _sigma5(k: int) -> int:
        s = 0
        for d in range(1, k + 1):
            if k % d == 0:
                s += d ** 5
        return s

    e6 = [0] * (N + 1)
    e6[0] = 1
    for k in range(1, N + 1):
        e6[k] = -504 * _sigma5(k)

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

    f18 = [0] * (N + 1)
    for i in range(N + 1):
        if e6[i] == 0:
            continue
        for j in range(N + 1 - i):
            f18[i + j] += e6[i] * delta[j]

    assert f18[m * n] == f18[m] * f18[n]


def test_hecke_recursion_p_equals_2() -> None:
    """a_{p^2} = a_p^2 - p^{17} at p = 2.

    (-528)^2 - 2^17 = 278784 - 131072 = 147712.
    """
    from math import comb

    N = 5

    def _sigma5(k: int) -> int:
        s = 0
        for d in range(1, k + 1):
            if k % d == 0:
                s += d ** 5
        return s

    e6 = [0] * (N + 1)
    e6[0] = 1
    for k in range(1, N + 1):
        e6[k] = -504 * _sigma5(k)

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

    f18 = [0] * (N + 1)
    for i in range(N + 1):
        if e6[i] == 0:
            continue
        for j in range(N + 1 - i):
            f18[i + j] += e6[i] * delta[j]

    # a_2^2 - 2^17 = a_4
    assert DELTA_E6_AP[2] ** 2 - 2 ** 17 == f18[4]
    assert f18[2] == DELTA_E6_AP[2]


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
    """Weissauer 2009 RP: |lambda_p - p^8 - p^9| <= 2 p^{17/2}."""
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
    """Reciprocal roots alpha, beta of 1 - a_p x + p^{17} x^2 have |alpha beta| = p^{17}."""
    a_p = DELTA_E6_AP[p]
    alpha, beta = spinor_satake_roots(p, a_p)
    # Product of reciprocal roots = p^{17} (Vieta's)
    prod = alpha * beta
    assert abs(prod.real - p ** 17) < 1e-3 * p ** 17
    assert abs(prod.imag) < 1e-3 * p ** 17


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
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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
    """|a_p| <= 2 p^{17/2} for all Wave 17 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
    )

    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        bound = 2 * (p ** 8.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(17/2) = {bound}"
        )


def test_w17_satake_cosine_in_unitary_range() -> None:
    """Satake parameter 2 cos(theta_p) is in [-2, 2] for all Wave 17 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W17,
        PRIMES_W17,
        lambda_p_from_delta_e6,
    )

    expected = {
        41: 384231010625364,
        43: 423260837896600,
        47: 1093636765488480,
        53: 3384963735409260,
        59: 8842521346989240,
        61: 10577567550962044,
        67: 32808745935835720,
        71: 42784764372282384,
        73: 63080419768434580,
        79: 123735238733833120,
    }
    for p in PRIMES_W17:
        a_p = DELTA_E6_AP_W17[p]
        lam = lambda_p_from_delta_e6(p, a_p)
        assert lam == expected[p], (
            f"SK eigenvalue mismatch at p = {p}: {lam} != {expected[p]}"
        )


def test_w17_sk_euler_factor_at_nine_and_half_is_finite_nonzero() -> None:
    """Z_p(s=9.5) is finite and non-zero at all Wave 17 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
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


# ----------------------------------------------------------------------
# Wave 18 extension: primes in {83, 89, 97, 101, 103, 107, 109, 113}
# ----------------------------------------------------------------------


def test_w18_primes_first_principles_match() -> None:
    """First-principles a_p at p in [83, 113] matches hardcoded table."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W18,
        W18_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    for p in W18_ADDITIONAL_PRIMES:
        computed = first_principles_a_p(p)
        expected = DELTA_E6_AP_W18[p]
        assert computed == expected, (
            f"Wave 18 first-principles mismatch at p = {p}: "
            f"computed {computed}, tabulated {expected}"
        )


def test_w18_deligne_bound() -> None:
    """|a_p| <= 2 p^{17/2} for all Wave 18 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W18,
        W18_ADDITIONAL_PRIMES,
    )

    for p in W18_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W18[p]
        bound = 2 * (p ** 8.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(17/2) = {bound}"
        )


# ----------------------------------------------------------------------
# Wave 20 extension: primes in {127, 131, ..., 199}. Three independent
# verification paths per prime:
#   (i) binomial eta^24 convolution (first_principles_a_p);
#   (ii) Jacobi pentagonal raised to the 24th power
#        (first_principles_a_p_jacobi);
#   (iii) Deligne bound |a_p| <= 2 p^{17/2};
# plus Hecke multiplicativity a_2 * a_p = a_{2p} and the
# Saito-Kurokawa identity lambda_p = a_p + p^8 + p^9
# agreeing with the Chenevier determinant component Sigma_1(T_p).
# ----------------------------------------------------------------------


def test_w20_primes_first_principles_match() -> None:
    """Binomial first-principles a_p at p in [127, 199] matches hardcoded table."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    for p in W20_ADDITIONAL_PRIMES:
        computed = first_principles_a_p(p)
        expected = DELTA_E6_AP_W20[p]
        assert computed == expected, (
            f"Wave 20 first-principles mismatch at p = {p}: "
            f"computed {computed}, tabulated {expected}"
        )


def test_w20_primes_jacobi_agrees() -> None:
    """Jacobi pentagonal path agrees with binomial path at every W20 prime.

    Two arithmetically independent q-series expansions produce the
    same a_p -- this is verification path (ii) in the W20 inscription.
    """
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        first_principles_a_p_jacobi,
    )

    for p in W20_ADDITIONAL_PRIMES:
        jacobi = first_principles_a_p_jacobi(p)
        expected = DELTA_E6_AP_W20[p]
        assert jacobi == expected, (
            f"Wave 20 Jacobi pentagonal mismatch at p = {p}: "
            f"jacobi {jacobi}, tabulated {expected}"
        )


def test_w20_deligne_bound() -> None:
    """|a_p| <= 2 p^{17/2} for all Wave 20 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
    )

    for p in W20_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W20[p]
        bound = 2 * (p ** 8.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(17/2) = {bound}"
        )


def test_w20_satake_cosine_in_unitary_range() -> None:
    """Satake parameter 2 cos(theta_p) is in [-2, 2] for all Wave 20 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        satake_cosine,
    )

    for p in W20_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W20[p]
        cos2 = satake_cosine(p, a_p)
        assert -2.0 <= cos2 <= 2.0, (
            f"Satake parameter out of unitary range at p = {p}: {cos2}"
        )


def test_w20_saito_kurokawa_eigenvalues() -> None:
    """lambda_p(Delta_10) = a_p + p^8 + p^9 at Wave 20 primes.

    The SK eigenvalue is identical to the Chenevier determinant value
    Sigma_1(T_p) = a_p(f_18) + p^8 + p^9 (Andrianov 1974; Ikeda 2001
    Cor. 16.2; Chenevier 2014 Section 1.2). Strict positivity at every
    prime witnesses p^9-dominance over |a_p| (Deligne).
    """
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        lambda_p_from_delta_e6,
    )

    for p in W20_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W20[p]
        lam = lambda_p_from_delta_e6(p, a_p)
        assert lam == a_p + p ** 8 + p ** 9
        assert lam > 0, f"SK eigenvalue not strictly positive at p = {p}: {lam}"


def test_w20_ramanujan_discriminant_negative() -> None:
    """Discriminant a_p^2 - 4 p^{17} < 0 (complex conjugate Satake pair)."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
    )

    for p in W20_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W20[p]
        disc = a_p * a_p - 4 * p ** 17
        assert disc < 0, (
            f"Ramanujan discriminant non-negative at p = {p}: {disc}"
        )


def test_w20_hecke_multiplicativity_a2_ap_bridge() -> None:
    """Bridge to the W15 table: a_2 * a_p = a_{2p} at all W20 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP,
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    a2 = DELTA_E6_AP[2]
    for p in W20_ADDITIONAL_PRIMES:
        ap = DELTA_E6_AP_W20[p]
        a2p = first_principles_a_p(2 * p, N=2 * p)
        assert a2 * ap == a2p, (
            f"Hecke multiplicativity failed at p = {p}: "
            f"a_2 * a_p = {a2 * ap}, a_{{2p}} = {a2p}"
        )


def test_w20_frenkel_reshetikhin_casimir_in_range() -> None:
    """C_2 Casimir eigenvalue = 2 cos(2 theta_p) is in [-2, 2]."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W20,
        W20_ADDITIONAL_PRIMES,
        frenkel_reshetikhin_c2_eigenvalue,
    )

    for p in W20_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W20[p]
        c2 = frenkel_reshetikhin_c2_eigenvalue(p, a_p)
        assert -2.0 <= c2 <= 2.0, (
            f"FR C_2 eigenvalue out of range at p = {p}: {c2}"
        )


def test_w20_target_primes_all_union_has_56_entries() -> None:
    """Union of W15 + W17 + W18 + W20 + W25 + W26 primes has 56 distinct entries."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        delta_e6_coefficients_all,
        target_primes_all,
    )

    all_primes = list(target_primes_all())
    assert len(all_primes) == 56
    assert len(set(all_primes)) == 56
    coeffs = delta_e6_coefficients_all()
    assert len(coeffs) == 56
    for p in all_primes:
        assert p in coeffs


# ----------------------------------------------------------------------
# Wave 25 extension: primes in {211, 223, 227, 229}. Same verification
# surface as W20: binomial + Jacobi + Deligne + Saito-Kurokawa.
# ----------------------------------------------------------------------


def test_w25_primes_first_principles_match() -> None:
    """Binomial first-principles a_p at p in [211, 229] matches the W25 table."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W25,
        W25_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    for p in W25_ADDITIONAL_PRIMES:
        computed = first_principles_a_p(p)
        expected = DELTA_E6_AP_W25[p]
        assert computed == expected, (
            f"Wave 25 first-principles mismatch at p = {p}: "
            f"computed {computed}, tabulated {expected}"
        )


def test_w25_deligne_bound() -> None:
    """|a_p| <= 2 p^{17/2} for all Wave 25 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W25,
        W25_ADDITIONAL_PRIMES,
    )

    for p in W25_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W25[p]
        bound = 2 * (p ** 8.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(17/2) = {bound}"
        )


# ----------------------------------------------------------------------
# Wave 26 extension: primes in {233, 239, 241, 251, 257, 263}.
# Five independent verification paths per prime:
#   (a) Binomial eta^24 convolution (first_principles_a_p);
#   (b) Jacobi pentagonal raised to the 24th power
#       (first_principles_a_p_jacobi);
#   (c) Ramanujan mod-691 congruence tau(p) == 1 + p^11 (mod 691)
#       on the driving tau coefficient;
#   (d) Deligne bound |a_p| <= 2 p^{17/2};
#   (e) Chenevier determinant Sigma_1(T_p) = a_p + p^8 + p^9 evaluated
#       integrally and equal to lambda_p(Delta_{10}).
# ----------------------------------------------------------------------


def test_w26_primes_first_principles_match() -> None:
    """Binomial first-principles a_p at p in [233, 263] matches the W26 table."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    for p in W26_ADDITIONAL_PRIMES:
        computed = first_principles_a_p(p)
        expected = DELTA_E6_AP_W26[p]
        assert computed == expected, (
            f"Wave 26 first-principles mismatch at p = {p}: "
            f"computed {computed}, tabulated {expected}"
        )


def test_w26_primes_jacobi_agrees() -> None:
    """Jacobi pentagonal path agrees with binomial path at every W26 prime."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        first_principles_a_p_jacobi,
    )

    for p in W26_ADDITIONAL_PRIMES:
        jacobi = first_principles_a_p_jacobi(p)
        expected = DELTA_E6_AP_W26[p]
        assert jacobi == expected, (
            f"Wave 26 Jacobi pentagonal mismatch at p = {p}: "
            f"jacobi {jacobi}, tabulated {expected}"
        )


def test_w26_tau_ramanujan_mod_691() -> None:
    """Ramanujan 1916 congruence tau(p) == 1 + p^11 (mod 691) at W26 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        TAU_W26,
        W26_ADDITIONAL_PRIMES,
    )

    for p in W26_ADDITIONAL_PRIMES:
        lhs = TAU_W26[p] % 691
        rhs = (1 + pow(p, 11, 691)) % 691  # sigma_11(p) for prime p
        assert lhs == rhs, (
            f"Ramanujan mod-691 congruence failed at p = {p}: "
            f"tau(p) mod 691 = {lhs}, sigma_11(p) mod 691 = {rhs}"
        )


def test_w26_deligne_bound() -> None:
    """|a_p| <= 2 p^{17/2} for all Wave 26 primes (weight 18)."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
    )

    for p in W26_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W26[p]
        bound = 2 * (p ** 8.5)
        assert abs(a_p) <= bound, (
            f"Deligne bound violated at p = {p}: "
            f"|a_p| = {abs(a_p)} > 2 p^(17/2) = {bound}"
        )


def test_w26_satake_cosine_in_unitary_range() -> None:
    """Satake parameter 2 cos(theta_p) is in [-2, 2] for all Wave 26 primes."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        satake_cosine,
    )

    for p in W26_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W26[p]
        cos2 = satake_cosine(p, a_p)
        assert -2.0 <= cos2 <= 2.0, (
            f"Satake parameter out of unitary range at p = {p}: {cos2}"
        )


def test_w26_chenevier_determinant_identity() -> None:
    """Chenevier determinant Sigma_1(T_p) = a_p(f_18) + p^8 + p^9 at W26 primes.

    Independent verification of the Saito-Kurokawa trace formula
    (Andrianov 1974 / Ikeda 2001) via the Chenevier determinant
    framework (Chenevier 2014 arXiv:1301.0635 Prop.~1.9), pinning
    the spinor trace of phi_{Delta_10}(Frob_p) on the Vol I
    determinant register.
    """
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        lambda_p_from_delta_e6,
    )

    # Chenevier Sigma_1(T_p) via the Satake factorisation
    # {p^8, p^9, alpha_p, beta_p}: first elementary symmetric function is
    # p^8 + p^9 + (alpha_p + beta_p) = p^8 + p^9 + a_p.
    for p in W26_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W26[p]
        sigma1 = a_p + p ** 8 + p ** 9
        lam = lambda_p_from_delta_e6(p, a_p)
        assert sigma1 == lam, (
            f"Chenevier Sigma_1 != SK lambda at p = {p}: {sigma1} != {lam}"
        )


def test_w26_hecke_multiplicativity_bridges_w14() -> None:
    """a_{2 p} = a_2 * a_p for every p in W26 primes (2 p <= 526 < 528)."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP,
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        first_principles_a_p,
    )

    a_2 = DELTA_E6_AP[2]
    for p in W26_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W26[p]
        a_2p = first_principles_a_p(2 * p, N=2 * p)
        assert a_2p == a_2 * a_p, (
            f"Hecke multiplicativity a_{{2p}} = a_2 a_p failed at p = {p}: "
            f"a_{{2p}} = {a_2p}, a_2 * a_p = {a_2 * a_p}"
        )


def test_w26_saito_kurokawa_eigenvalues_positive() -> None:
    """lambda_p(Delta_10) > 0 at all Wave 26 primes (p^9 dominates |a_p|)."""
    from compute.lib.k3_yangian_arthur_hecke_delta10 import (
        DELTA_E6_AP_W26,
        W26_ADDITIONAL_PRIMES,
        lambda_p_from_delta_e6,
    )

    for p in W26_ADDITIONAL_PRIMES:
        a_p = DELTA_E6_AP_W26[p]
        lam = lambda_p_from_delta_e6(p, a_p)
        assert lam > 0, (
            f"lambda_p not positive at p = {p}: lambda_p = {lam}"
        )
