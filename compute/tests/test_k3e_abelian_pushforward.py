"""Tests for k3e_abelian_pushforward.py.

Multi-path verification of the abelian (2,0) pushforward analysis:
- Shadow tower of the K3 sigma model (class M)
- Free-field shadow tower (class G, terminates)
- BKM root multiplicity constancy (sum = 24 at each level)
- Interior cancellation from modular constancy of phi_{0,1}
"""

import math
from fractions import Fraction

import pytest

from compute.lib.k3e_abelian_pushforward import (
    F,
    KAPPA_SIGMA,
    S3_SIGMA,
    S4_SIGMA,
    DELTA_SIGMA,
    PHI01_DISCRIMINANT,
    bkm_boundary_mult_at_level,
    bkm_interior_mult_at_level,
    bkm_positive_roots_at_level,
    bkm_total_mult_at_level,
    free_field_shadow_tower,
    kappa_collapse_data,
    level_has_complete_data,
    max_discriminant_at_level,
    mc_recursion,
    phi01_coeff,
    phi01_coeff_D,
    root_mult_constancy_verification,
    sigma_model_shadow_tower,
)


# =========================================================================
# Section 1: phi_{0,1} Fourier data
# =========================================================================

class TestPhi01:
    """Verify phi_{0,1} coefficients from Eichler-Zagier (1985, p. 108)."""

    def test_constancy_n0(self):
        """phi_{0,1}(tau, 0) = 12: sum_l c(0, l) = sum_l c(-l^2) = 12."""
        total = 0
        for l in range(-5, 6):
            total += phi01_coeff(0, l)
        assert total == 12, f"phi01(tau, 0) = {total}, expected 12"

    def test_constancy_n1(self):
        """q^1 coefficient of phi_{0,1}(tau, 0) vanishes: sum_l c(1, l) = 0."""
        total = 0
        for l in range(-5, 6):
            total += phi01_coeff(1, l)
        assert total == 0, f"q^1 sum = {total}, expected 0"

    def test_constancy_n2(self):
        """q^2 coefficient vanishes."""
        total = sum(phi01_coeff(2, l) for l in range(-10, 11))
        assert total == 0

    def test_constancy_n3(self):
        """q^3 coefficient vanishes."""
        total = sum(phi01_coeff(3, l) for l in range(-12, 13))
        assert total == 0

    def test_known_coefficients(self):
        """Spot-check Eichler-Zagier table values."""
        assert phi01_coeff_D(-1) == 1
        assert phi01_coeff_D(0) == 10
        assert phi01_coeff_D(3) == -64
        assert phi01_coeff_D(4) == 108
        assert phi01_coeff_D(7) == -513
        assert phi01_coeff_D(8) == 808


# =========================================================================
# Section 2: Shadow tower of K3 sigma model (class M)
# =========================================================================

class TestSigmaModelShadow:
    """Verify shadow tower of the N=4 SCA at c=6."""

    def test_initial_data(self):
        assert KAPPA_SIGMA == F(2)
        assert S3_SIGMA == F(2)
        assert S4_SIGMA == F(5, 156)

    def test_critical_discriminant(self):
        assert DELTA_SIGMA == F(20, 39)
        assert DELTA_SIGMA != 0, "Delta = 0 would mean class G, not M"

    def test_shadow_tower_values(self):
        """MC recursion produces known values."""
        S = sigma_model_shadow_tower(max_r=12)
        assert S[2] == F(2)
        assert S[3] == F(2)
        assert S[4] == F(5, 156)
        assert S[5] == F(-1, 26)
        assert S[6] == F(3485, 73008)

    def test_sign_alternation(self):
        """Signs alternate from r=5 onward."""
        S = sigma_model_shadow_tower(max_r=12)
        for r in range(5, 13):
            expected_sign = (-1) ** (r - 4)
            actual_sign = 1 if S[r] > 0 else -1
            assert actual_sign == expected_sign, f"S_{r} sign wrong"

    def test_nonzero_at_all_arities(self):
        """Class M: all S_r nonzero for r >= 2."""
        S = sigma_model_shadow_tower(max_r=20)
        for r in range(2, 21):
            assert S[r] != 0, f"S_{r} = 0, contradicts class M"

    def test_quartic_formula(self):
        """Q^contact = 10/(c(5c+22)) at c=6."""
        c = 6
        Q = F(10, c * (5 * c + 22))
        assert Q == F(10, 312)
        assert Q == F(5, 156)
        assert Q == S4_SIGMA


# =========================================================================
# Section 3: Free-field pushforward (class G)
# =========================================================================

class TestFreeFieldShadow:
    """Verify that free-field pushforward terminates at arity 2."""

    def test_class_g_rank20(self):
        S = free_field_shadow_tower(F(20), max_r=10)
        assert S[2] == F(20)
        for r in range(3, 11):
            assert S[r] == F(0), f"S_{r} nonzero for class G"

    def test_class_g_rank24(self):
        S = free_field_shadow_tower(F(24), max_r=10)
        assert S[2] == F(24)
        for r in range(3, 11):
            assert S[r] == F(0)


# =========================================================================
# Section 4: Root multiplicity constancy (Theorem in working_notes.tex)
# =========================================================================

class TestRootMultConstancy:
    """sum mult(alpha) at level L = 24 = chi(K3) for all L >= 1."""

    def test_boundary_is_24(self):
        """Boundary roots (n=0 or m=0) sum to 24 at each level."""
        for lev in range(1, 7):
            assert bkm_boundary_mult_at_level(lev) == 24

    def test_interior_cancellation(self):
        """Interior roots (n>0, m>0) sum to 0 at levels with complete data."""
        for lev in range(1, 7):
            if level_has_complete_data(lev):
                interior = bkm_interior_mult_at_level(lev)
                assert interior == 0, f"Interior sum at level {lev} = {interior}"

    def test_total_is_24(self):
        """Total multiplicity at each level is 24."""
        for lev in range(1, 7):
            if level_has_complete_data(lev):
                assert bkm_total_mult_at_level(lev) == 24

    def test_level2_interior_detail(self):
        """Explicit cancellation: 108 - 128 + 20 = 0 at level 2."""
        # Interior roots at level 2: (1, l, 1) for various l
        c4 = phi01_coeff_D(4)    # D=4, l=0
        c3 = phi01_coeff_D(3)    # D=3, l=+/-1
        c0 = phi01_coeff_D(0)    # D=0, l=+/-2
        assert c4 == 108
        assert c3 == -64
        assert c0 == 10
        interior = c4 + 2 * c3 + 2 * c0
        assert interior == 0, f"Level 2 interior: {interior}"

    def test_data_completeness(self):
        """Levels 1-6 have complete data; level 7+ may not."""
        for lev in range(1, 7):
            assert level_has_complete_data(lev), f"Level {lev} incomplete"
        # Level 7 needs max D = 4*3*4 = 48 > 36 (table max)
        assert not level_has_complete_data(7)


# =========================================================================
# Section 5: Level 1 root structure
# =========================================================================

class TestLevel1:
    """Detailed verification of level-1 root structure."""

    def test_level1_roots(self):
        roots = bkm_positive_roots_at_level(1)
        assert len(roots) == 6

    def test_level1_mults(self):
        """6 roots: 2 with mult 10 (D=0) and 4 with mult 1 (D=-1)."""
        roots = bkm_positive_roots_at_level(1)
        mults = sorted([m for _, _, m in roots])
        assert mults == [1, 1, 1, 1, 10, 10]
        assert sum(mults) == 24


# =========================================================================
# Section 6: Kappa-collapse
# =========================================================================

class TestKappaCollapse:
    """The structural gap between free-field and sigma model."""

    def test_kappa_values(self):
        data = kappa_collapse_data()
        assert data['kappa_sigma'] == F(2)
        # AP113: kappa_BKM (not kappa_BPS -- BPS not in approved subscript set)
        assert data['kappa_bkm'] == F(5)

    def test_not_perturbative(self):
        """Collapse ratio > 10: not a small correction."""
        data = kappa_collapse_data()
        assert data['collapse_ratio_lower'] >= 10

    def test_second_quantization_ratio(self):
        """kappa_BKM / kappa_ch = 5/3.

        AP113: approved subscripts {ch, cat, BKM, fiber}.
        kappa_ch(K3 x E) = 3 (proved, chiral de Rham).
        kappa_BKM(K3 x E) = 5 (conjectural, Borcherds weight).
        """
        # kappa_ch(K3 x E) = kappa(K3) + kappa(E) = 2 + 1 = 3
        kappa_ch = KAPPA_SIGMA + F(1)  # +1 for E
        assert kappa_ch == F(3)
        assert F(5) / kappa_ch == F(5, 3)


# =========================================================================
# Section 7: Full verification suite
# =========================================================================

class TestFullVerification:
    """Cross-path consistency checks."""

    def test_constancy_all_levels(self):
        """Root mult constancy verified at all complete levels."""
        results = root_mult_constancy_verification(max_level=6)
        for lev, data in results.items():
            if data['data_complete']:
                assert data['correct'], f"Level {lev} failed"

    def test_max_discriminant_formula(self):
        """max D at level L = 4 * floor(L/2) * ceil(L/2)."""
        assert max_discriminant_at_level(2) == 4   # 4*1*1
        assert max_discriminant_at_level(3) == 8   # 4*1*2
        assert max_discriminant_at_level(4) == 16  # 4*2*2
        assert max_discriminant_at_level(5) == 24  # 4*2*3
        assert max_discriminant_at_level(6) == 36  # 4*3*3
        assert max_discriminant_at_level(7) == 48  # 4*3*4
