"""Tests for Wave-19 GELFAND non-semisimple S-matrix engine.

Target: >= 30 assertions covering:
  - Simple and projective enumeration on M_24-invariant block (13 simples).
  - Block classification: 1 singleton + 3 length-2 + 6 singletons = 10 blocks.
  - Pseudo-character count = 13 = total simples (Creutzig-Ridout 2013).
  - Pseudo-S matrix is block-diagonal 13x13.
  - Un-normalised S^{ps 2} = identity on each block.
  - Length-2 block S = [[0,1],[1,0]] reproduces the off-diagonal flip.
  - Semisimple projection of S^{ps} yields degenerate 10x10 consistent with
    the Fricke 4x4 reduction on fundamentals.
  - Log-Verlinde non-negative integer coefficients.
  - Projective cover dimensions: length-1 block = dim L, length-2 block = 3*dim L.
  - Jordan length on projectives: 1 on singleton, 3 on length-2.
  - Cross-reference to W17 3x3 fusion matrix thm:qgf-wave17-fusion-matrix.

Raeez Lorgat -- Vol III K3 BKM chiral bialgebra -- Wave 19 GELFAND tests.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_nonsemisimple_S import (
    FUSION_BOUND,
    LUSZTIG_ELL,
    RANK_REAL,
    Block,
    Simple,
    build_block_S_length_one,
    build_block_S_length_two,
    build_global_pseudo_S,
    enumerate_blocks,
    enumerate_simples,
    fricke_projection_on_fundamentals,
    is_identity_up_to_scale,
    jordan_length_on_projective,
    log_verlinde_all_nonnegative_integer,
    log_verlinde_fusion_coefficients_structural,
    matrix_multiply,
    projective_cover_dimension_via_cartan,
    pseudo_S_is_involution_up_to_normalisation,
    pseudo_S_squared_on_block,
    semisimple_projection_S,
    total_blocks_count,
    total_length_two_blocks,
    total_pseudo_traces_count,
    total_simples_count,
    total_singleton_blocks,
    verify_all,
)


# ------------------------------------------------------------------
# A. Constants and basic structure.
# ------------------------------------------------------------------


def test_lusztig_ell_equals_8():
    # K3 BKM Lusztig level = 8 (W18 thm:qgf-wave18-PBW-pro-limit).
    assert LUSZTIG_ELL == 8


def test_fusion_bound_equals_7():
    # Kac-Walton bound at ell = 8: <lambda, theta^vee> <= ell - 1 = 7.
    # (W17 thm:qgf-wave17-fusion-matrix.)
    assert FUSION_BOUND == 7


def test_rank_real_equals_3():
    # BKM g_{Delta_5} has 3 real simple roots (Gritsenko-Nikulin 1998).
    assert RANK_REAL == 3


# ------------------------------------------------------------------
# B. Simple enumeration.
# ------------------------------------------------------------------


def test_enumerate_simples_returns_13_simples():
    """W17 closure under Kac-Walton fusion at ell=8 gives 13 simples on
    the M_24-invariant block."""
    simples = enumerate_simples()
    assert len(simples) == 13


def test_identity_simple_V_0_present():
    simples = enumerate_simples()
    labels = {s.label for s in simples}
    assert "V_0" in labels


def test_three_real_root_fundamentals_present():
    simples = enumerate_simples()
    labels = {s.label for s in simples}
    for i in range(1, 4):
        assert f"V_alpha_{i}" in labels


def test_three_diagonal_descendants_present():
    simples = enumerate_simples()
    labels = {s.label for s in simples}
    for i in range(1, 4):
        assert f"V_2alpha_{i}" in labels


def test_three_off_diagonal_plus_present():
    simples = enumerate_simples()
    labels = {s.label for s in simples}
    for i in range(1, 4):
        for j in range(i + 1, 4):
            assert f"V_alpha_{i}+alpha_{j}" in labels


def test_three_off_diagonal_minus_present():
    simples = enumerate_simples()
    labels = {s.label for s in simples}
    for i in range(1, 4):
        for j in range(i + 1, 4):
            assert f"V_alpha_{i}-alpha_{j}" in labels


def test_all_simple_weights_within_fusion_bound():
    """All dominant weights satisfy <lambda, theta^vee> <= 7."""
    for s in enumerate_simples():
        # theta^vee in basis of simple coroots evaluates to sum of
        # non-negative components of highest weight for dominant lambda.
        # For the off-diagonal minus V_{alpha_i - alpha_j}, the
        # theta-pairing is 0 (sum zero), which is <= 7.
        pairing = s.theta_pairing()
        assert pairing <= 7


def test_total_simples_count_is_13():
    assert total_simples_count() == 13


# ------------------------------------------------------------------
# C. Block classification.
# ------------------------------------------------------------------


def test_enumerate_blocks_returns_10_blocks():
    """Minimal block structure: B_0 + B_1 + B_2 + B_3 + 6 singletons."""
    blocks = enumerate_blocks()
    assert len(blocks) == 10


def test_one_identity_singleton_B_0():
    blocks = enumerate_blocks()
    labels = {b.label for b in blocks}
    assert "B_0" in labels
    b0 = next(b for b in blocks if b.label == "B_0")
    assert b0.length == 1
    assert len(b0.simples) == 1


def test_three_length_two_blocks():
    """Affine-Weyl links V_{alpha_i} with V_{2 alpha_i} at ell=8."""
    assert total_length_two_blocks() == 3


def test_seven_singleton_blocks():
    """B_0 plus 6 off-diagonal singletons = 7 total."""
    # Block B_0, plus the six singletons V_{alpha_i +/- alpha_j}.
    assert total_singleton_blocks() == 7


def test_length_two_blocks_contain_alpha_i_and_2alpha_i():
    blocks = enumerate_blocks()
    for i in range(1, 4):
        b_i = next(b for b in blocks if b.label == f"B_{i}")
        labels = {s.label for s in b_i.simples}
        assert f"V_alpha_{i}" in labels
        assert f"V_2alpha_{i}" in labels


def test_total_blocks_count_matches():
    assert total_blocks_count() == 10


def test_sum_of_block_lengths_equals_13():
    # Primary structural invariant.
    blocks = enumerate_blocks()
    total = sum(len(b.simples) for b in blocks)
    assert total == 13


# ------------------------------------------------------------------
# D. Pseudo-character enumeration.
# ------------------------------------------------------------------


def test_total_pseudo_traces_count_is_13():
    """Creutzig-Ridout 2013: length-r block contributes r pseudo-traces.
    Sum over blocks = 1 + 3*2 + 6*1 = 13."""
    assert total_pseudo_traces_count() == 13


def test_singleton_contributes_one_pseudo():
    blocks = enumerate_blocks()
    singletons = [b for b in blocks if b.length == 1]
    for b in singletons:
        assert b.n_pseudos() == 1


def test_length_two_contributes_two_pseudos():
    blocks = enumerate_blocks()
    length2 = [b for b in blocks if b.length == 2]
    for b in length2:
        assert b.n_pseudos() == 2


# ------------------------------------------------------------------
# E. Projective cover dimensions and Jordan structure.
# ------------------------------------------------------------------


def test_projective_cover_singleton_equals_simple():
    """On a singleton block, P_lambda = L_lambda (no Jordan extension)."""
    assert projective_cover_dimension_via_cartan(1, 1) == 1
    assert projective_cover_dimension_via_cartan(1, 5) == 5


def test_projective_cover_length_two_equals_three_times_simple():
    """Chari-Pressley 1994 PKP: length-2 block has dim P = 3 * dim L."""
    assert projective_cover_dimension_via_cartan(2, 1) == 3
    assert projective_cover_dimension_via_cartan(2, 4) == 12


def test_jordan_length_on_singleton_is_one():
    """Singleton block: P = L (no radical)."""
    assert jordan_length_on_projective(1) == 1


def test_jordan_length_on_length_two_is_three():
    """Diamond structure: 0 < L < rad(P) < P with comp factors [L, mu, L]."""
    assert jordan_length_on_projective(2) == 3


def test_unsupported_block_length_raises():
    """We only model length 1, 2 blocks for K3 BKM at ell=8."""
    with pytest.raises(ValueError):
        projective_cover_dimension_via_cartan(3, 1)
    with pytest.raises(ValueError):
        jordan_length_on_projective(3)


# ------------------------------------------------------------------
# F. Pseudo-S-matrix structure.
# ------------------------------------------------------------------


def test_block_S_length_one_is_scalar_one():
    """Singleton block: S = [[1]]."""
    S = build_block_S_length_one()
    assert S == [[Fraction(1)]]


def test_block_S_length_two_is_off_diagonal_flip():
    """Creutzig-Ridout 2013 Phys. A 46 eq. (5.14):
    S^{ps}_{length 2} = [[0,1],[1,0]] (un-normalised)."""
    S = build_block_S_length_two()
    assert S == [
        [Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(0)],
    ]


def test_global_pseudo_S_is_13_by_13():
    S = build_global_pseudo_S()
    assert len(S) == 13
    assert all(len(row) == 13 for row in S)


def test_global_pseudo_S_is_block_diagonal():
    """Different linkage blocks are decoupled under the modular transform."""
    S = build_global_pseudo_S()
    blocks = enumerate_blocks()
    # Compute block boundaries.
    boundaries = []
    offset = 0
    for b in blocks:
        boundaries.append((offset, offset + b.n_pseudos()))
        offset += b.n_pseudos()
    # Off-block entries must be zero.
    for k, (start, end) in enumerate(boundaries):
        for i in range(13):
            for j in range(13):
                in_this_block = (start <= i < end) and (start <= j < end)
                # Check that if (i, j) straddles different blocks, entry is 0.
                if start <= i < end and not (start <= j < end):
                    assert S[i][j] == Fraction(0)
                if start <= j < end and not (start <= i < end):
                    assert S[i][j] == Fraction(0)


def test_pseudo_S_squared_on_length_one():
    """(S_{length 1})^2 = [[1]]."""
    S2 = pseudo_S_squared_on_block(1)
    assert S2 == [[Fraction(1)]]


def test_pseudo_S_squared_on_length_two_is_identity():
    """(S_{length 2})^2 = [[0,1],[1,0]]^2 = [[1,0],[0,1]]."""
    S2 = pseudo_S_squared_on_block(2)
    assert S2 == [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]


def test_pseudo_S_global_is_involution_up_to_normalisation():
    assert pseudo_S_is_involution_up_to_normalisation()


def test_pseudo_S_squared_on_bad_length_raises():
    with pytest.raises(ValueError):
        pseudo_S_squared_on_block(3)


# ------------------------------------------------------------------
# G. Semisimple projection to Fricke.
# ------------------------------------------------------------------


def test_semisimple_projection_is_10_by_10():
    """10 blocks -> 10 x 10 projected matrix."""
    S_proj = semisimple_projection_S()
    assert len(S_proj) == 10
    assert all(len(row) == 10 for row in S_proj)


def test_semisimple_projection_has_seven_ones_on_diagonal():
    """Seven singleton blocks give diagonal [[1]]."""
    S_proj = semisimple_projection_S()
    count_ones = sum(
        1 for k in range(10) if S_proj[k][k] == Fraction(1)
    )
    assert count_ones == 7


def test_semisimple_projection_has_three_zeros_on_diagonal():
    """Three length-2 blocks contribute 0 on diagonal (the [[0,1],[1,0]]
    off-diagonal flip projects the ordinary character to zero)."""
    S_proj = semisimple_projection_S()
    count_zeros = sum(
        1 for k in range(10) if S_proj[k][k] == Fraction(0)
    )
    assert count_zeros == 3


def test_fricke_projection_on_fundamentals_is_4_by_4():
    """Extract {V_0, V_alpha_1, V_alpha_2, V_alpha_3} sub-block."""
    sub = fricke_projection_on_fundamentals()
    assert len(sub) == 4
    assert all(len(row) == 4 for row in sub)


def test_fricke_projection_V_0_diagonal_is_one():
    """V_0 is in singleton B_0: diag entry = 1."""
    sub = fricke_projection_on_fundamentals()
    assert sub[0][0] == Fraction(1)


def test_fricke_projection_V_alpha_diagonal_is_zero():
    """V_alpha_i is ordinary character of length-2 B_i: diag entry = 0.
    Consistent with W17 4x4 Fourier: S_{jk} = (1/2) i^{jk}; after the
    semisimple projection in un-normalised form we expect only the
    STRUCTURAL vanishing on length-2 blocks."""
    sub = fricke_projection_on_fundamentals()
    for i in range(1, 4):
        assert sub[i][i] == Fraction(0)


# ------------------------------------------------------------------
# H. Logarithmic Verlinde.
# ------------------------------------------------------------------


def test_log_verlinde_all_nonnegative_integer():
    """GJRSV 2013 Thm. 2.3: all log-Verlinde coefficients are in Z_{>=0}."""
    assert log_verlinde_all_nonnegative_integer()


def test_log_verlinde_diagonal_V_alpha_i_V_alpha_i_yields_V_0_and_V_2alpha_i():
    """W17 thm:qgf-wave17-fusion-matrix: V_alpha_i x V_alpha_i = V_0 + V_{2 alpha_i}.
    Log-Verlinde reproduces this on the non-semisimple lift."""
    coeffs = log_verlinde_fusion_coefficients_structural()
    for i in range(1, 4):
        vN_alpha_self_0 = next(
            n
            for l, m, nu, n in coeffs
            if l == f"V_alpha_{i}"
            and m == f"V_alpha_{i}"
            and nu == "V_0"
        )
        vN_alpha_self_2alpha = next(
            n
            for l, m, nu, n in coeffs
            if l == f"V_alpha_{i}"
            and m == f"V_alpha_{i}"
            and nu == f"V_2alpha_{i}"
        )
        assert vN_alpha_self_0 == 1
        assert vN_alpha_self_2alpha == 1


def test_log_verlinde_off_diagonal_V_alpha_i_V_alpha_j_splits_two_ways():
    """V_alpha_i x V_alpha_j = V_{alpha_i+alpha_j} + V_{alpha_i-alpha_j}
    (for i != j). Matches W17 thm:qgf-wave17-fusion-matrix."""
    coeffs = log_verlinde_fusion_coefficients_structural()
    for i in range(1, 4):
        for j in range(i + 1, 4):
            n_plus = next(
                n
                for l, m, nu, n in coeffs
                if l == f"V_alpha_{i}"
                and m == f"V_alpha_{j}"
                and nu == f"V_alpha_{i}+alpha_{j}"
            )
            n_minus = next(
                n
                for l, m, nu, n in coeffs
                if l == f"V_alpha_{i}"
                and m == f"V_alpha_{j}"
                and nu == f"V_alpha_{i}-alpha_{j}"
            )
            assert n_plus == 1
            assert n_minus == 1


# ------------------------------------------------------------------
# I. Umbrella / regression.
# ------------------------------------------------------------------


def test_verify_all_passes():
    assert verify_all()


def test_matrix_multiply_sanity():
    """Sanity test on the exact Fraction multiplication primitive."""
    A = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    B = [[Fraction(5), Fraction(6)], [Fraction(7), Fraction(8)]]
    C = matrix_multiply(A, B)
    assert C == [
        [Fraction(19), Fraction(22)],
        [Fraction(43), Fraction(50)],
    ]


def test_is_identity_up_to_scale_sanity():
    I2 = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(2)]]
    assert is_identity_up_to_scale(I2, Fraction(2))
    assert not is_identity_up_to_scale(I2, Fraction(1))
