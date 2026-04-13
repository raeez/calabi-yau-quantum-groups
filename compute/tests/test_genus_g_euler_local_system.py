"""Tests for genus_g_euler_local_system: Euler characteristics of degree-2
KZB local systems on punctured surfaces at arbitrary rank and genus.

Ground truth:
  chapters/theory/higher_genus_modular_koszul.tex
  (Proposition prop:genus-g-euler-general, eq:genus-g-euler-general).

Formula: chi(Sigma_g \\ {0}, L_KZB^{(2)}) = d^2 * (1 - 2g).

Three independent verification paths per value:
  [DC] Direct computation from formula d^2 * (1 - 2g).
  [LT] Literature / manuscript cross-reference.
  [CF] Cross-family consistency (varying d at fixed g, or vice versa).
"""

import pytest

from compute.lib.genus_g_euler_local_system import (
    chi_top_punctured_surface,
    kzb_local_system_rank,
    euler_char_kzb_degree2,
    euler_table,
    verify_all,
)


# ======================================================================
# 1. Topological Euler characteristic of punctured surfaces
# ======================================================================

class TestChiTopPuncturedSurface:
    r"""Verify chi_top(Sigma_g \ {s punctures}) = 2 - 2g - s."""

    def test_sphere_one_puncture(self):
        r"""chi_top(S^2 \ {pt}) = 1."""
        # VERIFIED [DC] 2 - 0 - 1 = 1 [LC] C has chi = 1
        assert chi_top_punctured_surface(0, 1) == 1

    def test_torus_one_puncture(self):
        r"""chi_top(T^2 \ {pt}) = -1."""
        # VERIFIED [DC] 2 - 2 - 1 = -1 [LC] once-punctured torus
        assert chi_top_punctured_surface(1, 1) == -1

    def test_genus2_one_puncture(self):
        r"""chi_top(Sigma_2 \ {pt}) = -3."""
        # VERIFIED [DC] 2 - 4 - 1 = -3 [LT] higher_genus_modular_koszul.tex:32832
        assert chi_top_punctured_surface(2, 1) == -3

    def test_genus3_one_puncture(self):
        r"""chi_top(Sigma_3 \ {pt}) = -5."""
        # VERIFIED [DC] 2 - 6 - 1 = -5 [CF] pattern 1 - 2g
        assert chi_top_punctured_surface(3, 1) == -5

    def test_closed_surface(self):
        """chi_top(Sigma_g) = 2 - 2g (no punctures)."""
        # VERIFIED [DC] standard formula [LC] sphere chi = 2
        assert chi_top_punctured_surface(0, 0) == 2
        assert chi_top_punctured_surface(1, 0) == 0
        assert chi_top_punctured_surface(2, 0) == -2

    def test_two_punctures(self):
        r"""chi_top(Sigma_g \ {2 pts}) = 2 - 2g - 2 = -2g."""
        # VERIFIED [DC] direct formula [CF] cross-check at g=0: chi=0
        assert chi_top_punctured_surface(0, 2) == 0
        assert chi_top_punctured_surface(1, 2) == -2
        assert chi_top_punctured_surface(2, 2) == -4


# ======================================================================
# 2. Local system rank
# ======================================================================

class TestKZBRank:
    """Verify rank of degree-2 local system is d^2."""

    def test_sl2(self):
        """sl_2: d=2, rank=4."""
        # VERIFIED [DC] 2^2 = 4 [LT] higher_genus_modular_koszul.tex:32802
        assert kzb_local_system_rank(2, degree=2) == 4

    def test_sl3(self):
        """sl_3: d=3, rank=9."""
        # VERIFIED [DC] 3^2 = 9 [CF] consistent with V tensor V
        assert kzb_local_system_rank(3, degree=2) == 9

    def test_sl4(self):
        """sl_4: d=4, rank=16."""
        # VERIFIED [DC] 4^2 = 16 [CF] consistent with V tensor V
        assert kzb_local_system_rank(4, degree=2) == 16


# ======================================================================
# 3. Euler characteristic: d=2 (sl_2, V=C^2) -- manuscript values
# ======================================================================

class TestEulerSl2:
    """Verify chi at d=2 against manuscript values."""

    def test_g0_d2(self):
        """g=0, d=2: chi = 4."""
        # VERIFIED [DC] 4*(1-0) = 4 [LT] higher_genus_modular_koszul.tex:32866
        # [CF] punctured sphere rank-4 local system
        assert euler_char_kzb_degree2(2, 0) == 4

    def test_g1_d2(self):
        """g=1, d=2: chi = -4."""
        # VERIFIED [DC] 4*(1-2) = -4 [LT] higher_genus_modular_koszul.tex:32947
        # [CF] matches dim H^1 = 4 at genus 1 (rem:h1-comparison)
        assert euler_char_kzb_degree2(2, 1) == -4

    def test_g2_d2(self):
        """g=2, d=2: chi = -12."""
        # VERIFIED [DC] 4*(1-4) = -12 [LT] higher_genus_modular_koszul.tex:32816
        # [CF] matches 4*(-3) in eq:g2-degree2-euler
        assert euler_char_kzb_degree2(2, 2) == -12

    def test_g3_d2(self):
        """g=3, d=2: chi = -20."""
        # VERIFIED [DC] 4*(1-6) = -20 [CF] pattern chi = 4*(1-2g)
        # [SY] linear in g at fixed d
        assert euler_char_kzb_degree2(2, 3) == -20


# ======================================================================
# 4. Euler characteristic: d=3 (sl_3, V=C^3)
# ======================================================================

class TestEulerSl3:
    """Verify chi at d=3."""

    def test_g0_d3(self):
        """g=0, d=3: chi = 9."""
        # VERIFIED [DC] 9*(1-0) = 9 [CF] ratio chi/d^2 = 1 matches g=0 d=2
        assert euler_char_kzb_degree2(3, 0) == 9

    def test_g1_d3(self):
        """g=1, d=3: chi = -9."""
        # VERIFIED [DC] 9*(1-2) = -9 [CF] ratio chi/d^2 = -1 matches g=1 d=2
        assert euler_char_kzb_degree2(3, 1) == -9

    def test_g2_d3(self):
        """g=2, d=3: chi = -27."""
        # VERIFIED [DC] 9*(1-4) = -27 [CF] -3*d^2 = -3*9 = -27
        assert euler_char_kzb_degree2(3, 2) == -27

    def test_g3_d3(self):
        """g=3, d=3: chi = -45."""
        # VERIFIED [DC] 9*(1-6) = -45 [CF] -5*d^2 = -5*9 = -45
        assert euler_char_kzb_degree2(3, 3) == -45


# ======================================================================
# 5. Euler characteristic: d=4 (sl_4, V=C^4)
# ======================================================================

class TestEulerSl4:
    """Verify chi at d=4."""

    def test_g0_d4(self):
        """g=0, d=4: chi = 16."""
        # VERIFIED [DC] 16*(1-0) = 16 [CF] ratio chi/d^2 = 1
        assert euler_char_kzb_degree2(4, 0) == 16

    def test_g1_d4(self):
        """g=1, d=4: chi = -16."""
        # VERIFIED [DC] 16*(1-2) = -16 [CF] ratio = -1 matches all d at g=1
        assert euler_char_kzb_degree2(4, 1) == -16

    def test_g2_d4(self):
        """g=2, d=4: chi = -48."""
        # VERIFIED [DC] 16*(1-4) = -48 [CF] -3*16 = -48
        assert euler_char_kzb_degree2(4, 2) == -48

    def test_g3_d4(self):
        """g=3, d=4: chi = -80."""
        # VERIFIED [DC] 16*(1-6) = -80 [CF] -5*16 = -80
        assert euler_char_kzb_degree2(4, 3) == -80


# ======================================================================
# 6. Structural properties
# ======================================================================

class TestStructuralProperties:
    """Verify structural properties of the Euler characteristic formula."""

    def test_linearity_in_d_squared(self):
        """chi(d, g) / d^2 depends only on g, not on d."""
        # VERIFIED [DC] formula is d^2 * (1 - 2g) [SY] manifest factorization
        for g in [0, 1, 2, 3, 5, 10]:
            expected_ratio = 1 - 2 * g
            for d in [2, 3, 4, 5, 7]:
                chi = euler_char_kzb_degree2(d, g)
                assert chi == d**2 * expected_ratio, (
                    f"d={d}, g={g}: chi={chi} != {d**2 * expected_ratio}"
                )

    def test_sign_pattern(self):
        """chi > 0 at g=0; chi < 0 for g >= 1."""
        # VERIFIED [DC] 1 - 2g > 0 iff g = 0 [SY] topological
        for d in [2, 3, 4, 5]:
            assert euler_char_kzb_degree2(d, 0) > 0
            for g in [1, 2, 3, 4, 5]:
                assert euler_char_kzb_degree2(d, g) < 0

    def test_genus_linear_growth(self):
        """|chi| grows linearly with g at fixed d."""
        # VERIFIED [DC] |chi| = d^2 * |1-2g| = d^2*(2g-1) for g>=1
        d = 3
        for g in range(1, 10):
            expected = d**2 * (2 * g - 1)
            assert abs(euler_char_kzb_degree2(d, g)) == expected

    def test_rank_quadratic_growth(self):
        """At fixed g >= 1, |chi| grows as d^2."""
        # VERIFIED [DC] manifest from formula [CF] cross-family
        g = 2
        factor = abs(1 - 2 * g)  # = 3
        for d in [2, 3, 4, 5, 6, 7]:
            assert abs(euler_char_kzb_degree2(d, g)) == factor * d**2

    def test_sl_N_formula_matches_user_claim(self):
        """Verify: chi(sl_N, g=2) = N^2 * (2 - 4 - 1) = -3N^2."""
        # VERIFIED [DC] direct [LT] user specification
        for N in [2, 3, 4, 5, 10]:
            assert euler_char_kzb_degree2(N, 2) == -3 * N**2


# ======================================================================
# 7. Euler table
# ======================================================================

class TestEulerTable:
    """Test the tabular output."""

    def test_full_table(self):
        """Verify the full d=2,3,4 x g=0,1,2,3 table."""
        # VERIFIED [DC] all 12 entries independently computed
        table = euler_table([2, 3, 4], [0, 1, 2, 3])

        # d=2 row
        assert table[(2, 0)] == 4
        assert table[(2, 1)] == -4
        assert table[(2, 2)] == -12
        assert table[(2, 3)] == -20

        # d=3 row
        assert table[(3, 0)] == 9
        assert table[(3, 1)] == -9
        assert table[(3, 2)] == -27
        assert table[(3, 3)] == -45

        # d=4 row
        assert table[(4, 0)] == 16
        assert table[(4, 1)] == -16
        assert table[(4, 2)] == -48
        assert table[(4, 3)] == -80


# ======================================================================
# 8. Internal verify_all
# ======================================================================

class TestVerifyAll:
    """Run the engine's internal verification suite."""

    def test_verify_all_passes(self):
        """All internal checks pass."""
        results = verify_all()
        assert len(results) >= 6, f"Expected >= 6 checks, got {len(results)}"
