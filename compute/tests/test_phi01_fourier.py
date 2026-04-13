"""Tests for phi01_fourier: Fourier coefficients of the weak Jacobi form phi_{0,1}.

Claims tested:
1. Known discriminant coefficients: c(-1) = 1, c(0) = 10, c(3) = -64, c(4) = 108
2. Row sum: sum_l f(n, l) = 12 if n=0, else 0
3. Symmetry: f(n, l) = f(n, -l)
4. Discriminant dependence: f(n, l) depends only on D = 4n - l^2
5. BKM identity: the eta^9 identity is FALSE for phi_{0,1} coefficients
   (it requires Delta_5 FJ coefficients -- regression test)

Ground truth:
    Eichler-Zagier "The Theory of Jacobi Forms" (1985), Thm 9.3
    c(-1)=1 (AP-CY9: the unique root with D=-1)
    c(0)=10, c(3)=-64, c(4)=108, c(7)=-513, c(8)=808
"""

import pytest
from fractions import Fraction

from compute.lib.phi01_fourier import (
    phi01_coefficient,
    phi01_table,
    phi01_by_discriminant,
    verify_bkm_identity,
    verify_row_sum,
    verify_symmetry,
    verify_discriminant_dependence,
)


# ======================================================================
# 1. Known discriminant coefficients
# ======================================================================

class TestDiscriminantCoefficients:
    """Verify c(D) against Eichler-Zagier table."""

    @pytest.fixture(scope="class")
    def c_disc(self):
        return phi01_by_discriminant(8)

    def test_c_neg1(self, c_disc):
        """c(-1) = 1: the unique real simple root (AP-CY9 convention)."""
        # VERIFIED [DC] Jacobi form coefficient [LT] Eichler-Zagier table
        assert c_disc[-1] == 1

    def test_c_0(self, c_disc):
        """c(0) = 10: the 10 imaginary simple roots."""
        assert c_disc[0] == 10

    def test_c_3(self, c_disc):
        """c(3) = -64: fermionic (negative) root multiplicity."""
        assert c_disc[3] == -64

    def test_c_4(self, c_disc):
        """c(4) = 108: bosonic root multiplicity."""
        assert c_disc[4] == 108

    def test_c_7(self, c_disc):
        """c(7) = -513."""
        assert c_disc[7] == -513

    def test_c_8(self, c_disc):
        """c(8) = 808."""
        assert c_disc[8] == 808

    def test_c_neg1_from_coefficient_api(self):
        """phi01_coefficient(0, 1) = 1 (the f(0,1) entry giving D=-1)."""
        # Multi-path: two APIs give same answer
        assert phi01_coefficient(0, 1) == 1

    def test_c_0_from_coefficient_api(self):
        """phi01_coefficient(0, 0) = 10 (D=0 entry)."""
        assert phi01_coefficient(0, 0) == 10


# ======================================================================
# 2. Row sum identity
# ======================================================================

class TestRowSum:
    """Verify sum_l f(n, l) = 12 if n=0, 0 otherwise."""

    def test_row_sum_n5(self):
        """Row sum holds for n = 0..5."""
        # VERIFIED [DC] row sum identity [LT] Jacobi form theory
        assert verify_row_sum(5) is True

    def test_row_sum_n10(self):
        """Row sum holds for n = 0..10."""
        assert verify_row_sum(10) is True

    def test_row_0_explicit(self):
        """sum_l f(0, l) = 12 explicitly from table."""
        table = phi01_table(0)
        row_sum = sum(v for (n, l), v in table.items() if n == 0)
        assert row_sum == 12


# ======================================================================
# 3. Symmetry
# ======================================================================

class TestSymmetry:
    """Verify f(n, l) = f(n, -l) for all coefficients."""

    def test_symmetry_n5(self):
        """Symmetry holds for n = 0..5."""
        assert verify_symmetry(5) is True

    def test_symmetry_n10(self):
        """Symmetry holds for n = 0..10."""
        assert verify_symmetry(10) is True


# ======================================================================
# 4. Discriminant dependence
# ======================================================================

class TestDiscriminantDependence:
    """Verify f(n, l) depends only on D = 4n - l^2."""

    def test_discriminant_n5(self):
        """Discriminant dependence for n = 0..5."""
        assert verify_discriminant_dependence(5) is True

    def test_discriminant_n10(self):
        """Discriminant dependence for n = 0..10."""
        assert verify_discriminant_dependence(10) is True

    def test_same_D_same_value(self):
        """f(1, 1) = f(1, -1) and both have D = 3, so equal c(3)."""
        # Multi-path: direct coefficient and discriminant table agree
        val_pos = phi01_coefficient(1, 1)
        val_neg = phi01_coefficient(1, -1)
        c_disc = phi01_by_discriminant(3)
        assert val_pos == val_neg
        assert val_pos == c_disc[3]


# ======================================================================
# 5. BKM identity regression (expected FALSE for phi_{0,1})
# ======================================================================

class TestBKMIdentity:
    """The eta^9 identity does NOT hold for phi_{0,1} (regression test).

    It requires Delta_5 Fourier-Jacobi coefficients, not phi_{0,1} directly.
    """

    def test_bkm_identity_false(self):
        """verify_bkm_identity returns False (expected)."""
        # VERIFIED [DC] regression test [LT] igusa_product_formula.py
        assert verify_bkm_identity(10) is False


# ======================================================================
# 6. Discriminant constraint (AP-CY9)
# ======================================================================

class TestDiscriminantConstraint:
    """AP-CY9: only D with D >= -1 can appear; D = -1 mod 4 or D = 0 mod 4."""

    def test_no_coefficient_below_neg1(self):
        """No f(n, l) with 4n - l^2 < -1."""
        assert phi01_coefficient(0, 2) == 0  # D = 0 - 4 = -4

    def test_discriminant_range(self):
        """All D values in the table satisfy D >= -1."""
        c_disc = phi01_by_discriminant(8)
        for D in c_disc:
            assert D >= -1
