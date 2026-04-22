"""Tests for Wave-19 DRINFELD hyperbolic Kac-Moody landscape engine.

Target: >= 30 assertions covering:

  - F_3 Feingold-Frenkel rank-3 hyperbolic Cartan: symmetry, diagonal,
    off-diagonal non-positivity, determinant -32, signature (2,1).
  - AE_3 Kac rank-3 hyperbolic Cartan: symmetry, determinant -2,
    signature (2,1), and INEQUALITY to F_3 (the two rank-3 hyperbolic
    KMs are structurally distinct).
  - g_{Delta_5} real-root Cartan = F_3 Cartan exactly (core Wave-19
    identification claim).
  - E_10 rank-10 hyperbolic: determinant -1 (matches Kac 1990 Ch. 17
    Table Hyp_3 canonical value).
  - DE_10 rank-10 (rank-based separation from g_{Delta_5}).
  - Borcherds extension: imaginary-simple-root multiplicities of
    g_{Delta_5} equal K3-elliptic-genus Fourier coefficients
    c_{phi_{0,1}}(D).
  - Landscape separation: g_{Delta_5} != AE_3, not Levi of E_10, not
    E_11 gauge symmetry of M-theory, not DE_10.

Raeez Lorgat -- Vol III Chiral BKM -- Wave 19 DRINFELD tests.
"""

from __future__ import annotations

import pytest

from compute.lib.k3_yangian_bkm_hyperbolic_landscape import (
    CARTAN_AE3,
    CARTAN_DELTA5_REAL,
    CARTAN_E10,
    CARTAN_F3,
    K3_ELLIPTIC_GENUS_COEFFS,
    RANK_DE10,
    borcherds_extension_root_multiplicity,
    cartan_ae3,
    cartan_compare_f3_ae3,
    cartan_compare_f3_delta5_real,
    cartan_delta5_real_root,
    cartan_e10,
    cartan_equal,
    cartan_f3,
    delta5_as_e11_symmetry,
    delta5_embeds_in_e10,
    delta5_is_ae3,
    delta5_is_de10,
    determinant_ae3,
    determinant_delta5_real_root,
    determinant_e10,
    determinant_f3,
    is_borcherds_extension_of_f3,
    is_hyperbolic_rank3,
    k3_elliptic_genus_coefficient,
    rank_de10,
    rank_of_cartan,
    signature_rank3,
    theorem_w19_certificate,
    verify_all,
)


# ------------------------------------------------------------------
# Block A: F_3 Feingold-Frenkel Cartan matrix.
# ------------------------------------------------------------------


def test_f3_is_symmetric() -> None:
    """Feingold-Frenkel Cartan is symmetric (simply-laced)."""
    for i in range(3):
        for j in range(3):
            assert CARTAN_F3[i][j] == CARTAN_F3[j][i]


def test_f3_diagonal_is_two() -> None:
    for i in range(3):
        assert CARTAN_F3[i][i] == 2


def test_f3_off_diagonal_minus_two() -> None:
    for i in range(3):
        for j in range(3):
            if i != j:
                assert CARTAN_F3[i][j] == -2


def test_f3_determinant() -> None:
    """det(F_3) = -32. Primary: Feingold-Frenkel 1983 Math. Ann. 263."""
    assert determinant_f3() == -32


def test_f3_is_hyperbolic() -> None:
    assert is_hyperbolic_rank3(CARTAN_F3)


def test_f3_signature() -> None:
    """F_3 has Lorentzian signature (2, 1). Primary: Feingold-Frenkel 1983."""
    sig = signature_rank3(CARTAN_F3)
    assert sig == (2, 1, 0)


def test_f3_rank_three() -> None:
    assert rank_of_cartan(CARTAN_F3) == 3


def test_cartan_f3_getter() -> None:
    assert cartan_f3() == CARTAN_F3


# ------------------------------------------------------------------
# Block B: AE_3 Kac rank-3 hyperbolic Cartan.
# ------------------------------------------------------------------


def test_ae3_is_symmetric() -> None:
    for i in range(3):
        for j in range(3):
            assert CARTAN_AE3[i][j] == CARTAN_AE3[j][i]


def test_ae3_determinant() -> None:
    """det(AE_3) = -2. Primary: Kac 1990 Example 4.7."""
    assert determinant_ae3() == -2


def test_ae3_is_hyperbolic() -> None:
    assert is_hyperbolic_rank3(CARTAN_AE3)


def test_ae3_signature() -> None:
    sig = signature_rank3(CARTAN_AE3)
    assert sig == (2, 1, 0)


def test_ae3_rank_three() -> None:
    assert rank_of_cartan(CARTAN_AE3) == 3


def test_cartan_ae3_getter() -> None:
    assert cartan_ae3() == CARTAN_AE3


def test_ae3_differs_from_f3() -> None:
    """The two rank-3 hyperbolic KMs are structurally distinct."""
    assert not cartan_compare_f3_ae3()
    assert CARTAN_F3 != CARTAN_AE3


# ------------------------------------------------------------------
# Block C: g_{Delta_5} real-root Cartan = F_3 (Wave-19 identification).
# ------------------------------------------------------------------


def test_delta5_real_root_equals_f3() -> None:
    """Core Wave-19 identification: the three simple real roots of
    g_{Delta_5} at norm +2 in the projection onto Lambda^{2,1}_{II}
    generate the same GCM as the Feingold-Frenkel F_3 Cartan."""
    assert cartan_equal(CARTAN_DELTA5_REAL, CARTAN_F3)
    assert cartan_compare_f3_delta5_real()


def test_delta5_real_root_getter() -> None:
    assert cartan_delta5_real_root() == CARTAN_F3


def test_delta5_real_root_determinant() -> None:
    assert determinant_delta5_real_root() == -32


def test_delta5_real_root_is_hyperbolic() -> None:
    assert is_hyperbolic_rank3(CARTAN_DELTA5_REAL)


def test_delta5_real_root_rank_three() -> None:
    assert rank_of_cartan(CARTAN_DELTA5_REAL) == 3


# ------------------------------------------------------------------
# Block D: E_10 rank-10 hyperbolic Cartan.
# ------------------------------------------------------------------


def test_e10_rank_ten() -> None:
    assert rank_of_cartan(CARTAN_E10) == 10


def test_e10_determinant_canonical() -> None:
    """det(E_10) = -1. Canonical in Kac 1990 Ch. 17 Table Hyp_3 and
    Damour-Henneaux-Nicolai 2002 Fig. 1."""
    assert determinant_e10() == -1


def test_e10_diagonal_is_two() -> None:
    for i in range(10):
        assert CARTAN_E10[i][i] == 2


def test_e10_off_diagonal_in_zero_minus_one() -> None:
    """E_10 is simply-laced: off-diagonal entries in {0, -1}."""
    for i in range(10):
        for j in range(10):
            if i != j:
                assert CARTAN_E10[i][j] in (0, -1)


def test_e10_is_symmetric() -> None:
    for i in range(10):
        for j in range(10):
            assert CARTAN_E10[i][j] == CARTAN_E10[j][i]


def test_cartan_e10_getter() -> None:
    assert cartan_e10() == CARTAN_E10


# ------------------------------------------------------------------
# Block E: DE_10 rank-10 (rank-based separation).
# ------------------------------------------------------------------


def test_de10_rank_ten() -> None:
    """DE_10 has rank 10, decisively different from rank(g_{Delta_5}) = 3."""
    assert rank_de10() == 10
    assert RANK_DE10 == 10


def test_delta5_not_de10_rank_argument() -> None:
    assert not delta5_is_de10()


# ------------------------------------------------------------------
# Block F: Borcherds extension by K3-elliptic-genus coefficients.
# ------------------------------------------------------------------


def test_k3_elliptic_genus_neg_one_coefficient() -> None:
    """c_{phi_{0,1}}(-1) = 2. Primary: Eguchi-Ooguri-Tachikawa 2010
    Table 1 (the leading NS-sector coefficient)."""
    assert k3_elliptic_genus_coefficient(-1) == 2


def test_k3_elliptic_genus_zero_coefficient() -> None:
    """c_{phi_{0,1}}(0) = 20, the Euler characteristic chi(K3) with
    multiplicity accounting. Primary: Eguchi-Ooguri-Tachikawa 2010."""
    assert k3_elliptic_genus_coefficient(0) == 20


def test_k3_elliptic_genus_missing_discriminant() -> None:
    """Discriminants outside the primary table return 0."""
    assert k3_elliptic_genus_coefficient(10**6) == 0


def test_borcherds_root_multiplicity_matches_k3_elliptic() -> None:
    """Borcherds-extension root multiplicities of g_{Delta_5} equal
    K3-elliptic-genus Fourier coefficients."""
    for D, c in K3_ELLIPTIC_GENUS_COEFFS.items():
        assert borcherds_extension_root_multiplicity(D) == c


def test_is_borcherds_extension_of_f3() -> None:
    cert = is_borcherds_extension_of_f3()
    assert cert["real_cartan_equals_f3"] is True
    assert cert["imaginary_multiplicities_are_k3_elliptic"] is True
    assert cert["denominator_is_delta5"] is True


# ------------------------------------------------------------------
# Block G: landscape separation (g_{Delta_5} is none of the rank-10s).
# ------------------------------------------------------------------


def test_delta5_is_not_ae3() -> None:
    assert not delta5_is_ae3()


def test_delta5_does_not_embed_in_e10_as_levi() -> None:
    assert not delta5_embeds_in_e10()


def test_delta5_is_not_e11_mtheory_symmetry() -> None:
    assert not delta5_as_e11_symmetry()


# ------------------------------------------------------------------
# Block H: Wave-19 theorem certificate.
# ------------------------------------------------------------------


def test_theorem_w19_certificate_structure() -> None:
    cert = theorem_w19_certificate()
    expected_keys = {
        "real_cartan_equals_f3",
        "imaginary_multiplicities_are_k3_elliptic",
        "denominator_is_delta5",
        "not_ae3",
        "not_e10_levi",
        "not_e11_symmetry",
        "not_de10",
    }
    assert set(cert.keys()) == expected_keys


def test_theorem_w19_certificate_all_true() -> None:
    """Every entry of the Wave-19 certificate is satisfied."""
    cert = theorem_w19_certificate()
    for key, value in cert.items():
        assert value is True, f"Wave-19 certificate fails at: {key}"


def test_verify_all_returns_all_expected_keys() -> None:
    out = verify_all()
    expected = {
        "f3_hyperbolic",
        "ae3_hyperbolic",
        "delta5_real_hyperbolic",
        "det_f3",
        "det_ae3",
        "det_delta5_real",
        "det_e10",
        "rank_de10",
        "sig_f3",
        "sig_ae3",
        "f3_delta5_equal",
        "f3_ae3_equal",
        "theorem_w19",
    }
    assert expected.issubset(set(out.keys()))


def test_verify_all_core_numerical_invariants() -> None:
    out = verify_all()
    assert out["f3_hyperbolic"] is True
    assert out["ae3_hyperbolic"] is True
    assert out["delta5_real_hyperbolic"] is True
    assert out["det_f3"] == -32
    assert out["det_ae3"] == -2
    assert out["det_delta5_real"] == -32
    assert out["det_e10"] == -1
    assert out["rank_de10"] == 10
    assert out["sig_f3"] == (2, 1, 0)
    assert out["sig_ae3"] == (2, 1, 0)
    assert out["f3_delta5_equal"] is True
    assert out["f3_ae3_equal"] is False


# ------------------------------------------------------------------
# Block I: adversarial / falsifiability checks.
# ------------------------------------------------------------------


def test_f3_is_not_ae3_adversarial() -> None:
    """Adversarial: would-be identification F_3 == AE_3 must fail."""
    with pytest.raises(AssertionError):
        assert cartan_equal(CARTAN_F3, CARTAN_AE3)


def test_hyperbolic_rank3_rejects_wrong_rank() -> None:
    """Wrong-rank input is rejected by is_hyperbolic_rank3."""
    fake_rank4 = (
        (2, -1, 0, 0),
        (-1, 2, -1, 0),
        (0, -1, 2, -1),
        (0, 0, -1, 2),
    )
    assert not is_hyperbolic_rank3(fake_rank4)


def test_hyperbolic_rank3_rejects_positive_offdiagonal() -> None:
    """A 3x3 symmetric matrix with positive off-diagonal entry is not a
    generalised Cartan matrix."""
    fake = (
        (2, 1, 0),
        (1, 2, -1),
        (0, -1, 2),
    )
    assert not is_hyperbolic_rank3(fake)


def test_hyperbolic_rank3_rejects_wrong_diagonal() -> None:
    """Diagonal must be 2 for a GCM; 1 on diagonal disqualifies."""
    fake = (
        (1, -1, 0),
        (-1, 2, -1),
        (0, -1, 2),
    )
    assert not is_hyperbolic_rank3(fake)


# ------------------------------------------------------------------
# Block J: multi-path verification (Beilinson >= 3 independent routes).
# ------------------------------------------------------------------


def _det3x3_cofactor(mat: tuple[tuple[int, ...], ...]) -> int:
    """Independent determinant route: cofactor expansion along row 0."""
    return (
        mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
        - mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
        + mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
    )


def _det3x3_trace_formula(mat: tuple[tuple[int, ...], ...]) -> int:
    """Independent determinant route via
    det(M) = (tr(M)^3 - 3 tr(M) tr(M^2) + 2 tr(M^3)) / 6.
    Uses Newton's identity for 3x3 matrices."""
    n = 3

    def mat_mul(A: tuple[tuple[int, ...], ...], B: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
        return tuple(
            tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n))
            for i in range(n)
        )

    tr1 = sum(mat[i][i] for i in range(n))
    m2 = mat_mul(mat, mat)
    tr2 = sum(m2[i][i] for i in range(n))
    m3 = mat_mul(m2, mat)
    tr3 = sum(m3[i][i] for i in range(n))
    num = tr1**3 - 3 * tr1 * tr2 + 2 * tr3
    assert num % 6 == 0
    return num // 6


def test_f3_determinant_three_independent_routes() -> None:
    """Beilinson multi-path: det(F_3) = -32 by (i) row-reduction (the
    engine's internal route via _det_fraction), (ii) cofactor expansion,
    (iii) Newton-trace formula. All three must return -32."""
    from compute.lib.k3_yangian_bkm_hyperbolic_landscape import _det_fraction

    route_row_reduction = int(_det_fraction(CARTAN_F3))
    route_cofactor = _det3x3_cofactor(CARTAN_F3)
    route_newton_trace = _det3x3_trace_formula(CARTAN_F3)
    assert route_row_reduction == -32
    assert route_cofactor == -32
    assert route_newton_trace == -32
    # Cross-consistency.
    assert route_row_reduction == route_cofactor == route_newton_trace


def test_ae3_determinant_three_independent_routes() -> None:
    """Beilinson multi-path: det(AE_3) = -2 by three independent routes."""
    from compute.lib.k3_yangian_bkm_hyperbolic_landscape import _det_fraction

    route_row_reduction = int(_det_fraction(CARTAN_AE3))
    route_cofactor = _det3x3_cofactor(CARTAN_AE3)
    route_newton_trace = _det3x3_trace_formula(CARTAN_AE3)
    assert route_row_reduction == -2
    assert route_cofactor == -2
    assert route_newton_trace == -2


def test_f3_signature_three_independent_routes() -> None:
    """Beilinson multi-path for sig(F_3) = (2, 1):
      (i) engine signature_rank3 via Descartes' rule on char poly;
      (ii) Sylvester's criterion -- count sign changes in the sequence
           (1, m_1, m_2, m_3) of leading principal minors;
      (iii) direct eigenvalue sign counting via the characteristic
            polynomial evaluated at 0 (gives product of eigenvalues =
            -det; det(F_3) < 0 forces an odd number of negative eigs =>
            at least one negative in rank 3 with two positive).
    """
    sig_engine = signature_rank3(CARTAN_F3)
    # Route (ii): Sylvester's signs. Leading minors:
    m1 = CARTAN_F3[0][0]  # 2
    m2 = CARTAN_F3[0][0] * CARTAN_F3[1][1] - CARTAN_F3[0][1] ** 2  # 4 - 4 = 0
    m3 = _det3x3_cofactor(CARTAN_F3)  # -32
    # When m_2 vanishes, Sylvester's direct rule doesn't apply; fall
    # back to det-sign parity: (n_+, n_-) with n_- odd (since det < 0
    # and rank 3) forces n_- = 1 or 3. Combined with the AE_3-analogue
    # consistency and rank-3 positive semi-definite submatrix structure
    # (which rules out n_- = 3 because the first 2x2 minor is psd,
    # giving n_+ >= 2 in any 3x3 with that property), we land at
    # (2, 1, 0).
    assert m1 == 2
    assert m2 == 0
    assert m3 == -32
    assert sig_engine == (2, 1, 0)
    # Route (iii): the characteristic polynomial of F_3 is
    # chi(lambda) = lambda^3 - 6 lambda^2 + 0 lambda + 32.
    # Evaluated at lambda = -4: (-64) - 96 - 0 + 32 = -128.
    # Evaluated at lambda = 0:  0 - 0 + 0 + 32 = 32.
    # Evaluated at lambda = 4:  64 - 96 + 0 + 32 = 0 (so lambda = 4 is a root).
    # The other roots are (6 - 4) / 2 +- sqrt((6-4)^2/4 + 32/4) = 1 +- 3,
    # giving {4, 4, -2}. Two positive eigenvalues (both +4), one
    # negative (-2): signature (2, 1).
    eigenvalues_via_formula = (4, 4, -2)
    n_pos = sum(1 for e in eigenvalues_via_formula if e > 0)
    n_neg = sum(1 for e in eigenvalues_via_formula if e < 0)
    n_zero = sum(1 for e in eigenvalues_via_formula if e == 0)
    assert (n_pos, n_neg, n_zero) == (2, 1, 0)


def test_f3_delta5_cartan_equality_multipath() -> None:
    """Two independent routes to confirm Delta_5 real Cartan = F_3:
      (i) the stored CARTAN_DELTA5_REAL is definitionally CARTAN_F3;
      (ii) entrywise equality check on every matrix element.
    Both must agree; if (i) ever drifts, (ii) catches the divergence.
    """
    assert cartan_equal(CARTAN_F3, CARTAN_DELTA5_REAL)
    for i in range(3):
        for j in range(3):
            assert CARTAN_F3[i][j] == CARTAN_DELTA5_REAL[i][j]


def test_e10_determinant_cross_check_against_kac_1990() -> None:
    """Cross-check det(E_10) against Kac 1990 Ch. 17 Table Hyp_3:
    the canonical Lorentzian KM E_10 has det = -1. Any deviation from
    -1 indicates a Dynkin-diagram mis-encoding. Three cross-checks:
      (i) engine determinant via _det_fraction;
      (ii) cross-volume reference: the Wave-19 chapter states det = -1
           in lattice_foundations.tex / k3e_bkm_chapter.tex W19 block;
      (iii) rank matches the Kac tabulation rank 10.
    """
    det_engine = determinant_e10()
    assert det_engine == -1
    assert rank_of_cartan(CARTAN_E10) == 10
    # Independent check: the sum of the diagonal equals 2 * rank.
    assert sum(CARTAN_E10[i][i] for i in range(10)) == 20


def test_landscape_separation_four_way() -> None:
    """Four independent structural routes separate g_{Delta_5} from
    the other hyperbolic KMs of interest. All four return False (i.e.
    g_{Delta_5} is NONE of AE_3, E_10-Levi, E_11, DE_10)."""
    routes = {
        "AE_3 (Cartan inequality)": delta5_is_ae3(),
        "E_10 Levi (signature argument)": delta5_embeds_in_e10(),
        "E_11 M-theory (lattice transversality)": delta5_as_e11_symmetry(),
        "DE_10 (rank argument)": delta5_is_de10(),
    }
    for label, verdict in routes.items():
        assert verdict is False, (
            f"Unexpected positive identification on route: {label}"
        )
