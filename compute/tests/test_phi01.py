"""
Tests for the Fourier coefficients of the weak Jacobi form phi_{0,1}.

Verifies against known values from Eichler--Zagier tables and structural
properties of weak Jacobi forms of weight 0 and index 1.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.phi01_fourier import (
    phi01_coefficient,
    phi01_table,
    phi01_by_discriminant,
    verify_bkm_identity,
    verify_row_sum,
    verify_symmetry,
    verify_discriminant_dependence,
)


# -----------------------------------------------------------------------
# Known Fourier coefficients f(n, l)
# From Eichler--Zagier, Table 1 (p. 37) and standard references.
# -----------------------------------------------------------------------

KNOWN_COEFFICIENTS = {
    # n=0 row:  phi_{0,1} = (r^{-1} + 10 + r) + O(q)
    (0, -1): 1,
    (0, 0): 10,
    (0, 1): 1,
    # n=1 row:  + q * (10 r^{-2} - 64 r^{-1} + 108 - 64 r + 10 r^2)
    (1, -2): 10,
    (1, -1): -64,
    (1, 0): 108,
    (1, 1): -64,
    (1, 2): 10,
    # n=2 row
    (2, -3): 1,
    (2, -2): 108,
    (2, -1): -513,
    (2, 0): 808,
    (2, 1): -513,
    (2, 2): 108,
    (2, 3): 1,
    # n=3 row
    (3, -3): -64,
    (3, -2): 808,
    (3, -1): -2752,
    (3, 0): 4016,
    (3, 1): -2752,
    (3, 2): 808,
    (3, 3): -64,
    # n=4 row
    (4, -4): 10,
    (4, -3): -513,
    (4, -2): 4016,
    (4, -1): -11775,
    (4, 0): 16524,
    (4, 1): -11775,
    (4, 2): 4016,
    (4, 3): -513,
    (4, 4): 10,
}


# -----------------------------------------------------------------------
# Known discriminant-indexed coefficients c(D) where f(n,l) = c(4n - l^2)
# -----------------------------------------------------------------------

KNOWN_C_BY_DISC = {
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
    19: -43200,
    20: 58640,
}


class TestKnownCoefficients:
    """Test individual Fourier coefficients against known values."""

    @pytest.mark.parametrize("n,l,expected", [
        (n, l, v) for (n, l), v in sorted(KNOWN_COEFFICIENTS.items())
    ])
    def test_known_f(self, n, l, expected):
        assert phi01_coefficient(n, l) == expected

    def test_table_matches_known(self):
        table = phi01_table(4)
        for (n, l), expected in KNOWN_COEFFICIENTS.items():
            assert table.get((n, l), 0) == expected, f"Mismatch at f({n}, {l})"


class TestDiscriminantCoefficients:
    """Test the discriminant-indexed coefficients c(D)."""

    def test_known_c_values(self):
        by_disc = phi01_by_discriminant(5)
        for D, expected in KNOWN_C_BY_DISC.items():
            assert by_disc.get(D, None) == expected, f"Mismatch at c({D})"


class TestStructuralProperties:
    """Structural properties of phi_{0,1} as a weak Jacobi form."""

    def test_symmetry_f_n_l_equals_f_n_minus_l(self):
        """f(n, l) = f(n, -l) by the evenness of phi_{0,1} in z."""
        assert verify_symmetry(6)

    def test_row_sum_is_12_then_zero(self):
        """
        sum_l f(n, l) = 12 if n=0, and 0 if n >= 1.

        This follows from phi_{0,1}(tau, 0) = 12 (a constant, since weight = 0
        and the Jacobi form at z=0 is a modular form of weight 0, hence constant).
        """
        assert verify_row_sum(6)

    def test_discriminant_dependence(self):
        """f(n, l) depends only on D = 4n - l^2 (not on n and l separately)."""
        assert verify_discriminant_dependence(6)

    def test_vanishing_for_negative_discriminant_bound(self):
        """f(n, l) = 0 when 4n - l^2 < -1 (outside the fundamental domain)."""
        table = phi01_table(5)
        for (n, l), v in table.items():
            assert 4 * n - l * l >= -1, f"f({n},{l}) nonzero with D = {4*n-l*l}"

    def test_f_at_boundary_D_minus_1(self):
        """At D = 4n - l^2 = -1, the coefficient is c(-1) = 1."""
        table = phi01_table(6)
        for (n, l), v in table.items():
            if 4 * n - l * l == -1:
                assert v == 1, f"f({n},{l}) = {v}, expected 1 for D = -1"


class TestSpecialValues:
    """Special evaluations of phi_{0,1}."""

    def test_phi01_at_z_equals_zero(self):
        """phi_{0,1}(tau, 0) = 12 identically."""
        table = phi01_table(8)
        for n in range(9):
            row_sum = sum(v for (nn, l), v in table.items() if nn == n)
            expected = 12 if n == 0 else 0
            assert row_sum == expected, f"Row sum at n={n}: {row_sum} != {expected}"

    def test_leading_term(self):
        """The q^0 term of phi_{0,1} is r^{-1} + 10 + r."""
        table = phi01_table(0)
        assert table == {(0, -1): 1, (0, 0): 10, (0, 1): 1}

    def test_n_equals_1_term(self):
        """The q^1 term is 10*r^{-2} - 64*r^{-1} + 108 - 64*r + 10*r^2."""
        table = phi01_table(1)
        q1 = {l: v for (n, l), v in table.items() if n == 1}
        assert q1 == {-2: 10, -1: -64, 0: 108, 1: -64, 2: 10}


class TestEdgeCases:
    """Edge cases and error handling."""

    def test_negative_n_raises(self):
        with pytest.raises(ValueError):
            phi01_coefficient(-1, 0)

    def test_vanishing_outside_lattice(self):
        """f(n, l) = 0 when 4n - l^2 < 0 and not equal to -1."""
        assert phi01_coefficient(0, 3) == 0
        assert phi01_coefficient(1, 3) == 0
        assert phi01_coefficient(0, 2) == 0

    def test_large_l_vanishes(self):
        """f(n, l) = 0 for l^2 > 4n + 1."""
        assert phi01_coefficient(2, 4) == 0
        assert phi01_coefficient(3, 4) == 0  # 4*3 - 16 = -4 < -1

    def test_max_n_parameter(self):
        """The max_n parameter controls truncation without affecting lower-order terms."""
        val_default = phi01_coefficient(2, 1)
        val_explicit = phi01_coefficient(2, 1, max_n=5)
        assert val_default == val_explicit == -513


class TestBKMIdentity:
    """
    The eta^9 identity

        1 + (1/64) * sum_{t >= 0} f(1 + 2t, 1) * q^t  =  prod_{k >= 1} (1 - q^k)^9

    is FALSE for phi_{0,1} Fourier coefficients.  The correct identity
    involves Fourier-Jacobi coefficients of the Igusa cusp form Delta_5,
    not those of phi_{0,1}.  See igusa_product_formula.py for the valid test.

    These tests document the FAILURE, confirming the identity is false.
    """

    def test_bkm_identity_is_false(self):
        """The identity is false for phi_{0,1}: verify_bkm_identity returns False."""
        assert verify_bkm_identity(10) is False

    def test_bkm_identity_fails_at_q0(self):
        """The identity fails at q^0: LHS = 0 but RHS = 1."""
        f11 = phi01_coefficient(1, 1)
        assert f11 == -64
        lhs_q0 = 1 + f11 / 64
        assert lhs_q0 == 0  # LHS is 0, but RHS is 1 => identity is false

    def test_f_odd_n_l1_divisible_by_64(self):
        """f(2t+1, 1) is divisible by 64 for all t >= 0 (BKM structure)."""
        table = phi01_table(11)
        for t in range(6):
            n = 1 + 2 * t
            f_val = table.get((n, 1), 0)
            assert f_val % 64 == 0, f"f({n}, 1) = {f_val} not divisible by 64"

    def test_f_odd_n_l1_over_64_values(self):
        """Known values of f(2t+1, 1) / 64."""
        table = phi01_table(11)
        expected = {
            0: -1,       # f(1,1)/64
            1: -43,      # f(3,1)/64
            2: -675,     # f(5,1)/64
            3: -6676,    # f(7,1)/64
            4: -49830,   # f(9,1)/64
            5: -305883,  # f(11,1)/64
        }
        for t, exp_val in expected.items():
            n = 1 + 2 * t
            f_val = table.get((n, 1), 0)
            assert f_val // 64 == exp_val, f"f({n},1)/64 = {f_val//64}, expected {exp_val}"


class TestConsistency:
    """Cross-checks between different computation methods."""

    def test_table_vs_individual(self):
        """phi01_table and phi01_coefficient agree."""
        table = phi01_table(4)
        for (n, l), v in table.items():
            assert phi01_coefficient(n, l) == v

    def test_discriminant_vs_table(self):
        """phi01_by_discriminant consistent with phi01_table."""
        table = phi01_table(5)
        by_disc = phi01_by_discriminant(5)
        for (n, l), v in table.items():
            D = 4 * n - l * l
            assert by_disc[D] == v

    def test_c_of_D_equals_3_mod_4_or_0_mod_4(self):
        """
        Nonzero c(D) occur only for D = -1, or D >= 0 with D equiv 0 or 3 (mod 4).

        This is because D = 4n - l^2, and l^2 mod 4 is either 0 or 1.
        """
        by_disc = phi01_by_discriminant(8)
        for D in by_disc:
            if D == -1:
                continue
            assert D >= 0
            assert D % 4 in (0, 3), f"c({D}) nonzero but D mod 4 = {D % 4}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
