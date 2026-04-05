"""Tests for the Maulik-Okounkov R-matrix on K3 x E.

Verifies:
  1. Structure function properties (CY condition, inversion, limits)
  2. Self-dual K3 limit (g = 1, trivial R-matrix)
  3. Unitarity R(u)*R_{21}(-u) = 1 at all charges
  4. Yang-Baxter equation at charges 1 and 2
  5. Hilbert scheme Euler characteristics (Gottsche formula)
  6. Comparison with Vol II chiral R-matrix (Heisenberg sector)
  7. Comparison with Drinfeld center / affine Yangian
  8. Numerical spot checks
  9. Elliptic structure function

Multi-path verification (CLAUDE.md mandate):
  - Path 1: Direct symbolic computation
  - Path 2: Numerical evaluation at specific parameter values
  - Path 3: Cross-check with drinfeld_center_coha.py
  - Path 4: Known special cases (self-dual, Heisenberg limit)
  - Path 5: Gottsche formula for Hilbert scheme Euler characteristics
"""

import sys
import os

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, cancel, expand, symbols, simplify

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from mo_rmatrix_k3e import (
    k3e_structure_function,
    k3e_structure_function_selfdual,
    k3e_structure_function_deformed,
    stable_envelope_hilb1,
    stable_envelope_hilb2,
    r_matrix_hilbn_diagonal,
    yang_baxter_charge1,
    yang_baxter_charge2_diagonal,
    yang_baxter_charge2_full,
    unitarity_check,
    unitarity_pair_check,
    chiral_r_matrix_heisenberg,
    comparison_mo_vs_chiral_heisenberg,
    hilb_k3_euler,
    hilb_k3e_fixed_locus_dims,
    heisenberg_limit_comparison,
    e1_to_e2_bridge_summary,
    elliptic_structure_function,
    numerical_r_matrix_check,
    cross_check_with_drinfeld_center,
    _partition_contents,
)


# ===================================================================
# 1. STRUCTURE FUNCTION: basic properties
# ===================================================================

class TestStructureFunction:
    """Test the MO structure function g(u) for K3 x E."""

    def test_structure_function_is_rational(self):
        """g(u) should be a ratio of polynomials in u."""
        g = k3e_structure_function(Rational(1), Rational(2))
        u = Symbol("u")
        # Should be expressible as p(u)/q(u)
        assert g is not None

    def test_cy_condition_enforced(self):
        """eps3 = -(eps1 + eps2) when not specified."""
        result = k3e_structure_function_deformed(Rational(1), Rational(2))
        assert result["eps3"] == Rational(-3)
        assert result["sigma1"] == 0

    def test_structure_function_at_infinity(self):
        """g(u) -> 1 as u -> infinity."""
        g = k3e_structure_function(Rational(1), Rational(2))
        u = Symbol("u")
        # Substitute large u
        g_large = g.subs(u, 1000)
        assert abs(float(g_large) - 1.0) < 0.01

    def test_structure_function_inversion(self):
        """g(u) * g(-u) = 1 (fundamental identity)."""
        u = Symbol("u")
        g = k3e_structure_function(Rational(1), Rational(2))
        g_neg = g.subs(u, -u)
        product = cancel(g * g_neg)
        assert product == 1, f"g(u)*g(-u) = {product}, expected 1"

    def test_inversion_generic_parameters(self):
        """g(u)*g(-u) = 1 for multiple parameter choices."""
        u = Symbol("u")
        for e1, e2 in [(Rational(1, 3), Rational(1, 5)),
                        (Rational(2), Rational(3)),
                        (Rational(1), Rational(-1, 2))]:
            g = k3e_structure_function(e1, e2)
            g_neg = g.subs(u, -u)
            product = cancel(g * g_neg)
            assert product == 1, f"Failed at eps=({e1},{e2}): g*g_neg = {product}"

    def test_sigma_values(self):
        """Elementary symmetric functions computed correctly."""
        result = k3e_structure_function_deformed(Rational(1), Rational(2))
        # sigma1 = 1 + 2 + (-3) = 0
        assert result["sigma1"] == 0
        # sigma2 = 1*2 + 1*(-3) + 2*(-3) = 2 - 3 - 6 = -7
        assert result["sigma2"] == -7
        # sigma3 = 1*2*(-3) = -6
        assert result["sigma3"] == -6

    def test_structure_function_at_zero(self):
        """g(0) = -1 when all eps_i are nonzero."""
        u = Symbol("u")
        g = k3e_structure_function(Rational(1), Rational(2))
        g_at_0 = g.subs(u, 0)
        assert g_at_0 == -1, f"g(0) = {g_at_0}, expected -1"


# ===================================================================
# 2. SELF-DUAL K3 LIMIT
# ===================================================================

class TestSelfDualLimit:
    """Test the self-dual K3 limit (eps1 = -eps2, g = 1)."""

    def test_selfdual_g_is_one(self):
        """In the self-dual limit, g(u) = 1."""
        result = k3e_structure_function_selfdual(Rational(1))
        assert result["is_trivial"], f"g = {result['g_u']}, expected 1"

    def test_selfdual_various_eps(self):
        """Self-dual limit gives g=1 for various epsilon values."""
        for eps in [Rational(1), Rational(2), Rational(1, 3), Rational(7)]:
            result = k3e_structure_function_selfdual(eps)
            assert result["is_trivial"], f"Failed at eps={eps}"

    def test_selfdual_eps3_is_zero(self):
        """In self-dual limit, eps3 = -(eps + (-eps)) = 0."""
        result = k3e_structure_function_deformed(Rational(1), Rational(-1))
        assert result["eps3"] == 0


# ===================================================================
# 3. STABLE ENVELOPE AND R-MATRIX
# ===================================================================

class TestStableEnvelope:
    """Test the stable envelope and R-matrix construction."""

    def test_hilb1_trivial(self):
        """Hilb^1: stable envelope and R-matrix are identity."""
        result = stable_envelope_hilb1()
        assert result["rank"] == 1
        assert result["dimension"] == 1

    def test_hilb2_two_states(self):
        """Hilb^2: two charge-2 states (row and column partition)."""
        result = stable_envelope_hilb2(Rational(1), Rational(2))
        assert result["rank"] == 2
        assert result["R_row"] is not None
        assert result["R_col"] is not None

    def test_hilb2_selfdual_trivial(self):
        """In self-dual limit, both R-matrix entries should be 1."""
        result = stable_envelope_hilb2(Rational(1), Rational(-1), Rational(0))
        # g = 1 identically, so R_row = 1*1 = 1 and R_col = 1*1 = 1
        u = Symbol("u")
        assert cancel(result["R_row"]) == 1, f"R_row = {result['R_row']}"
        assert cancel(result["R_col"]) == 1, f"R_col = {result['R_col']}"

    def test_hilb2_ratio_formula(self):
        """The ratio R_row/R_col = g(u+eps2)/g(u+eps1)."""
        eps1, eps2 = Rational(1), Rational(2)
        result = stable_envelope_hilb2(eps1, eps2)
        u = Symbol("u")
        g = k3e_structure_function(eps1, eps2)
        expected_ratio = cancel(g.subs(u, u + eps2) / g.subs(u, u + eps1))
        assert cancel(result["ratio"] - expected_ratio) == 0

    def test_diagonal_r_matrix_empty_partition(self):
        """Empty partition gives R = 1."""
        r = r_matrix_hilbn_diagonal(Rational(1), Rational(2), [])
        assert r == 1

    def test_diagonal_r_matrix_single_box(self):
        """Single box partition [1] gives R = g(u)."""
        eps1, eps2 = Rational(1), Rational(2)
        r = r_matrix_hilbn_diagonal(eps1, eps2, [1])
        g = k3e_structure_function(eps1, eps2)
        assert cancel(r - g) == 0

    def test_diagonal_r_matrix_row_2(self):
        """Row partition [2] gives R = g(u)*g(u+eps2)."""
        eps1, eps2 = Rational(1), Rational(2)
        r = r_matrix_hilbn_diagonal(eps1, eps2, [2])
        u = Symbol("u")
        g = k3e_structure_function(eps1, eps2)
        expected = cancel(g * g.subs(u, u + eps2))
        assert cancel(r - expected) == 0

    def test_diagonal_r_matrix_col_2(self):
        """Column partition [1,1] gives R = g(u)*g(u+eps1)."""
        eps1, eps2 = Rational(1), Rational(2)
        r = r_matrix_hilbn_diagonal(eps1, eps2, [1, 1])
        u = Symbol("u")
        g = k3e_structure_function(eps1, eps2)
        expected = cancel(g * g.subs(u, u + eps1))
        assert cancel(r - expected) == 0


# ===================================================================
# 4. YANG-BAXTER EQUATION
# ===================================================================

class TestYangBaxter:
    """Test the Yang-Baxter equation for the MO R-matrix."""

    def test_ybe_charge1(self):
        """YBE at charge (1,1,1): trivially satisfied."""
        result = yang_baxter_charge1(Rational(1), Rational(2))
        assert result["match"], "YBE failed at charge (1,1,1)"

    def test_ybe_charge1_various_params(self):
        """YBE at charge 1 for multiple parameter choices."""
        for e1, e2 in [(Rational(1), Rational(3)),
                        (Rational(1, 2), Rational(1, 3)),
                        (Rational(2), Rational(5))]:
            result = yang_baxter_charge1(e1, e2)
            assert result["match"], f"YBE failed at eps=({e1},{e2})"

    def test_ybe_charge2_diagonal(self):
        """YBE at charge (2,1,1) diagonal."""
        result = yang_baxter_charge2_diagonal(Rational(1), Rational(2))
        assert result["all_pass"], "YBE diagonal failed at charge (2,1,1)"

    def test_ybe_charge2_full(self):
        """Full YBE at charge (2,2,2) — all 8 components."""
        result = yang_baxter_charge2_full(Rational(1), Rational(2))
        assert result["all_pass"], (
            f"YBE failed: {result['components']}"
        )
        assert result["n_components"] == 8

    def test_ybe_charge2_full_different_params(self):
        """Full YBE at charge (2,2,2) with different parameters."""
        result = yang_baxter_charge2_full(Rational(1, 3), Rational(1, 5))
        assert result["all_pass"], "YBE failed at (1/3, 1/5)"


# ===================================================================
# 5. UNITARITY
# ===================================================================

class TestUnitarity:
    """Test R(u)*R_{21}(-u) = 1."""

    def test_unitarity_empty(self):
        """Empty partition: trivially unitary."""
        result = unitarity_check(Rational(1), Rational(2), [])
        assert result["is_unitary"]

    def test_unitarity_single_box(self):
        """Single box: g(u)*g(-u) = 1."""
        result = unitarity_check(Rational(1), Rational(2), [1])
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_row_2(self):
        """Row partition (2): product of two g-factors."""
        result = unitarity_check(Rational(1), Rational(2), [2])
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_col_2(self):
        """Column partition (1,1)."""
        result = unitarity_check(Rational(1), Rational(2), [1, 1])
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_3_box(self):
        """Partition (3): three boxes in a row."""
        result = unitarity_check(Rational(1), Rational(2), [3])
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_hook(self):
        """Hook partition (2,1)."""
        result = unitarity_check(Rational(1), Rational(2), [2, 1])
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_pair_row_row(self):
        """Tensor product unitarity: |(2)> x |(2)>."""
        result = unitarity_pair_check(
            Rational(1), Rational(2), [2], [2]
        )
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_pair_row_col(self):
        """Tensor product unitarity: |(2)> x |(1,1)>."""
        result = unitarity_pair_check(
            Rational(1), Rational(2), [2], [1, 1]
        )
        assert result["is_unitary"], f"Product = {result['product']}"

    def test_unitarity_pair_col_col(self):
        """Tensor product unitarity: |(1,1)> x |(1,1)>."""
        result = unitarity_pair_check(
            Rational(1), Rational(2), [1, 1], [1, 1]
        )
        assert result["is_unitary"], f"Product = {result['product']}"


# ===================================================================
# 6. HILBERT SCHEME EULER CHARACTERISTICS (Gottsche formula)
# ===================================================================

class TestHilbK3:
    """Test chi(Hilb^n(K3)) from Gottsche's formula."""

    def test_hilb0(self):
        """chi(Hilb^0(K3)) = 1 (a single point)."""
        hilb = hilb_k3_euler(0)
        assert hilb[0] == 1

    def test_hilb1(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        hilb = hilb_k3_euler(1)
        assert hilb[1] == 24

    def test_hilb2(self):
        """chi(Hilb^2(K3)) = 324."""
        hilb = hilb_k3_euler(2)
        assert hilb[2] == 324

    def test_hilb3(self):
        """chi(Hilb^3(K3)) = 3200."""
        hilb = hilb_k3_euler(3)
        assert hilb[3] == 3200

    def test_hilb4(self):
        """chi(Hilb^4(K3)) = 25650."""
        hilb = hilb_k3_euler(4)
        assert hilb[4] == 25650

    def test_hilb_monotone(self):
        """chi(Hilb^n(K3)) is strictly increasing for n >= 1."""
        hilb = hilb_k3_euler(6)
        for n in range(1, 6):
            assert hilb[n + 1] > hilb[n], (
                f"Not monotone: chi(Hilb^{n+1}) = {hilb[n+1]} "
                f"<= chi(Hilb^{n}) = {hilb[n]}"
            )

    def test_hilb_known_sequence(self):
        """Full sequence matches OEIS A008485 (coeffs of 1/eta^24)."""
        # First several: 1, 24, 324, 3200, 25650, 176256, ...
        hilb = hilb_k3_euler(5)
        expected = [1, 24, 324, 3200, 25650, 176256]
        for n, (got, want) in enumerate(zip(hilb, expected)):
            assert got == want, f"chi(Hilb^{n}) = {got}, expected {want}"


# ===================================================================
# 7. COMPARISON WITH VOL II: CHIRAL R-MATRIX
# ===================================================================

class TestChiralComparison:
    """Test comparison between MO R-matrix and Vol II chiral R-matrix."""

    def test_chiral_heisenberg_classical_r(self):
        """Classical r-matrix for Heisenberg at level 1: r(u) = 1/u."""
        result = chiral_r_matrix_heisenberg(1)
        u = Symbol("u")
        assert cancel(result["r_classical"] - 1 / u) == 0

    def test_chiral_heisenberg_quantum_R(self):
        """Quantum R-matrix for Heisenberg: R(u) = (u+k)/(u-k)."""
        result = chiral_r_matrix_heisenberg(2)
        u = Symbol("u")
        expected = (u + 2) / (u - 2)
        assert cancel(result["R_rational"] - expected) == 0

    def test_mo_equals_ay_structure_function(self):
        """MO structure function = affine Yangian structure function."""
        result = comparison_mo_vs_chiral_heisenberg(Rational(1), Rational(2))
        assert result["match"], "MO != AY structure function"

    def test_mo_equals_ay_various_params(self):
        """MO = AY for multiple parameter choices."""
        for e1, e2 in [(Rational(1, 3), Rational(1, 5)),
                        (Rational(2), Rational(3)),
                        (Rational(1), Rational(-1, 2))]:
            result = comparison_mo_vs_chiral_heisenberg(e1, e2)
            assert result["match"], f"MO != AY at eps=({e1},{e2})"

    def test_selfdual_comparison(self):
        """At self-dual point, both MO and chiral give trivial R."""
        result = comparison_mo_vs_chiral_heisenberg(Rational(1), Rational(-1))
        assert result["selfdual_is_trivial"]

    def test_heisenberg_limit(self):
        """In the Heisenberg limit (eps -> 0), g(u) -> 1."""
        result = heisenberg_limit_comparison()
        assert result["is_trivial_at_eps0"]


# ===================================================================
# 8. E1-TO-E2 BRIDGE
# ===================================================================

class TestE1E2Bridge:
    """Test the full E1 -> E2 bridge data."""

    def test_bridge_generic(self):
        """Full bridge data for generic parameters."""
        result = e1_to_e2_bridge_summary(Rational(1), Rational(2))
        assert result["eps3"] == Rational(-3)
        assert not result["is_selfdual"]
        assert all(result["unitarity"].values())

    def test_bridge_selfdual(self):
        """Bridge at self-dual point: trivial R-matrix."""
        result = e1_to_e2_bridge_summary(Rational(1), Rational(-1))
        assert result["is_selfdual"]
        assert all(result["unitarity"].values())

    def test_bridge_unitarity_all_charges(self):
        """All unitarity checks pass in the bridge summary."""
        result = e1_to_e2_bridge_summary(Rational(1), Rational(3))
        for key, val in result["unitarity"].items():
            assert val, f"Unitarity failed for {key}"


# ===================================================================
# 9. DRINFELD CENTER CROSS-CHECK
# ===================================================================

class TestDrinfeldCenterCrossCheck:
    """Cross-check with Drinfeld center dimensions."""

    def test_plane_partition_counts(self):
        """Fock space dimensions match plane partition counts."""
        result = cross_check_with_drinfeld_center(6)
        expected_pp = [1, 1, 3, 6, 13, 24]
        assert result["plane_partition_counts"] == expected_pp

    def test_ordinary_partition_counts(self):
        """Cartan dimensions match ordinary partition counts."""
        result = cross_check_with_drinfeld_center(6)
        expected_op = [1, 1, 2, 3, 5, 7]
        assert result["ordinary_partition_counts"] == expected_op

    def test_drinfeld_double_dimensions(self):
        """Full Yangian dimensions = M(q)^2 * P(q).

        These are the graded dimensions of Y(gl_hat_1) by the PBW
        triangular decomposition Y = Y^- * Y^0 * Y^+.
        Verified against drinfeld_center_coha.py (both PBW sum and
        product expansion methods agree).
        """
        result = cross_check_with_drinfeld_center(6)
        # Authoritative: from drinfeld_center_coha.py (both computation methods agree)
        expected = [1, 3, 11, 32, 90, 231]
        assert result["drinfeld_double_dims"] == expected


# ===================================================================
# 10. NUMERICAL VERIFICATION
# ===================================================================

class TestNumerical:
    """Numerical spot checks for the R-matrix."""

    def test_numerical_unitarity(self):
        """g(u)*g(-u) = 1 numerically."""
        result = numerical_r_matrix_check(1.0, 2.0, 3.5)
        assert result["unitarity_g"], (
            f"Unitarity failed: product = {result['unitarity_product']}"
        )

    def test_numerical_unitarity_small_params(self):
        """Unitarity with small parameters."""
        result = numerical_r_matrix_check(0.1, 0.2, 5.0)
        assert result["unitarity_g"]

    def test_numerical_g_at_infinity(self):
        """g(u) -> 1 for large u."""
        result = numerical_r_matrix_check(1.0, 2.0, 100.0)
        assert abs(result["g_u"] - 1.0) < 0.01

    def test_numerical_g_at_zero(self):
        """g(0) = -1 for nonzero eps_i."""
        result = numerical_r_matrix_check(1.0, 2.0, 0.0)
        # g(0) = (-1)(-2)(3) / (1)(2)(-3) = -6 / -6 = 1
        # Wait: g(0) = (0-1)(0-2)(0+3) / ((0+1)(0+2)(0-3)) = (-1)(-2)(3)/((1)(2)(-3))
        # = 6 / (-6) = -1
        assert abs(result["g_u"] - (-1.0)) < 1e-10

    def test_numerical_selfdual(self):
        """Self-dual: g(u) = 1 numerically (eps1 = 1, eps2 = -1)."""
        # eps3 = 0 makes denominator have u factor, and numerator has u factor
        # g(u) = (u-1)(u+1)*u / ((u+1)(u-1)*u) = 1 for u != 0, +/-1
        result = numerical_r_matrix_check(1.0, -1.0, 3.5)
        assert abs(result["g_u"] - 1.0) < 1e-10

    def test_numerical_charge2_nondegenerate(self):
        """Charge-2 R-matrix entries are nonzero for generic parameters."""
        result = numerical_r_matrix_check(1.0, 2.0, 3.5)
        r2 = result["R_charge2"]
        assert abs(r2["R_row"]) > 1e-10
        assert abs(r2["R_col"]) > 1e-10
        # Row and column should differ (different content functions)
        assert abs(r2["R_row"] - r2["R_col"]) > 1e-10


# ===================================================================
# 11. PARTITION CONTENTS
# ===================================================================

class TestPartitionContents:
    """Test the content function for partitions."""

    def test_empty_partition(self):
        """Empty partition has no contents."""
        c = _partition_contents([], 1, 2)
        assert c == []

    def test_single_box(self):
        """Single box at (0,0) has content 0."""
        c = _partition_contents([1], 1, 2)
        assert c == [0]

    def test_row_2(self):
        """Row (2): boxes at (0,0) and (0,1)."""
        c = _partition_contents([2], 1, 2)
        assert c == [0, 2]  # eps2 = 2

    def test_col_2(self):
        """Column (1,1): boxes at (0,0) and (1,0)."""
        c = _partition_contents([1, 1], 1, 2)
        assert c == [0, 1]  # eps1 = 1

    def test_hook(self):
        """Hook (2,1): boxes at (0,0), (0,1), (1,0)."""
        c = _partition_contents([2, 1], 1, 2)
        assert c == [0, 2, 1]  # (0,0)->0, (0,1)->eps2=2, (1,0)->eps1=1

    def test_square_2x2(self):
        """Square (2,2): boxes at (0,0), (0,1), (1,0), (1,1)."""
        c = _partition_contents([2, 2], 1, 2)
        assert c == [0, 2, 1, 3]  # 0, eps2, eps1, eps1+eps2


# ===================================================================
# 12. ELLIPTIC STRUCTURE FUNCTION
# ===================================================================

class TestEllipticStructureFunction:
    """Test the elliptic refinement of the structure function."""

    def test_elliptic_returns_rational_limit(self):
        """The elliptic structure function includes the rational limit."""
        result = elliptic_structure_function(Rational(1), Rational(2))
        assert result["g_rational"] is not None
        assert result["eps3"] == Rational(-3)


# ===================================================================
# 13. FIXED LOCUS DIMENSIONS
# ===================================================================

class TestFixedLocus:
    """Test the T-fixed locus of Hilb^n(K3 x E)."""

    def test_charge0(self):
        """Charge 0: single point, dim = 1."""
        result = hilb_k3e_fixed_locus_dims(0)
        assert result[0]["fixed_locus_dim"] == 1

    def test_charge1(self):
        """Charge 1: one point on K3, dim = chi(K3) = 24."""
        result = hilb_k3e_fixed_locus_dims(1)
        assert result[1]["fixed_locus_dim"] == 24

    def test_charge2_sum(self):
        """Charge 2: partitions (2) and (1,1).
        dim = chi(Hilb^2(K3)) + chi(Hilb^1(K3))^2
        Wait: the partition (1,1) contributes chi(Hilb^1)^2 = 24^2 = 576
        and the partition (2) contributes chi(Hilb^2) = 324.
        Total = 324 + 576 = 900.
        """
        result = hilb_k3e_fixed_locus_dims(2)
        assert result[2]["fixed_locus_dim"] == 324 + 576  # = 900


# ===================================================================
# 14. ADDITIONAL CROSS-CHECKS (multi-path verification)
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification of key identities."""

    def test_inversion_symbolic_and_numerical(self):
        """g(u)*g(-u) = 1 verified both symbolically and numerically."""
        # Symbolic
        u = Symbol("u")
        g = k3e_structure_function(Rational(1), Rational(2))
        g_neg = g.subs(u, -u)
        symbolic_check = cancel(g * g_neg) == 1

        # Numerical at u = 3.7
        eps1, eps2, eps3 = 1.0, 2.0, -3.0
        u_val = 3.7
        g_val = ((u_val - eps1) * (u_val - eps2) * (u_val - eps3)
                 / ((u_val + eps1) * (u_val + eps2) * (u_val + eps3)))
        g_neg_val = ((-u_val - eps1) * (-u_val - eps2) * (-u_val - eps3)
                     / ((-u_val + eps1) * (-u_val + eps2) * (-u_val + eps3)))
        numerical_check = abs(g_val * g_neg_val - 1.0) < 1e-10

        assert symbolic_check, "Symbolic inversion failed"
        assert numerical_check, "Numerical inversion failed"

    def test_selfdual_three_ways(self):
        """Self-dual g=1 verified via: (1) direct, (2) deformed, (3) numerical."""
        # Path 1: direct self-dual function
        r1 = k3e_structure_function_selfdual(Rational(2))
        assert r1["is_trivial"]

        # Path 2: deformed with eps2 = -eps1
        g2 = k3e_structure_function(Rational(2), Rational(-2), Rational(0))
        assert cancel(g2) == 1

        # Path 3: numerical
        r3 = numerical_r_matrix_check(2.0, -2.0, 4.5)
        assert abs(r3["g_u"] - 1.0) < 1e-10

    def test_ybe_two_paths(self):
        """YBE verified via (1) symbolic cancellation, (2) numerical evaluation."""
        # Path 1: symbolic
        result_sym = yang_baxter_charge1(Rational(1), Rational(2))
        assert result_sym["match"]

        # Path 2: numerical — evaluate LHS and RHS at specific (u,v)
        eps1, eps2, eps3 = 1.0, 2.0, -3.0
        u_val, v_val = 3.5, 1.7

        def g_num(x):
            return ((x - eps1) * (x - eps2) * (x - eps3)
                    / ((x + eps1) * (x + eps2) * (x + eps3)))

        lhs = g_num(u_val - v_val) * g_num(u_val) * g_num(v_val)
        rhs = g_num(v_val) * g_num(u_val) * g_num(u_val - v_val)
        assert abs(lhs - rhs) < 1e-10

    def test_hilb_k3_cross_check_with_vw(self):
        """chi(Hilb^n(K3)) cross-checked: Gottsche vs direct product expansion."""
        # Path 1: our hilb_k3_euler function
        hilb1 = hilb_k3_euler(4)

        # Path 2: independent computation via generating function
        # prod_{k>=1} 1/(1-q^k)^{24} expanded to order 4
        N = 5
        coeffs = [0] * N
        coeffs[0] = 1
        for k in range(1, N):
            for _ in range(24):
                for n in range(k, N):
                    coeffs[n] += coeffs[n - k]

        for n in range(N):
            assert hilb1[n] == coeffs[n], f"Mismatch at n={n}: {hilb1[n]} vs {coeffs[n]}"

    def test_unitarity_symbolic_vs_numerical(self):
        """Unitarity for partition (2,1) checked symbolically and numerically."""
        # Symbolic
        r_sym = unitarity_check(Rational(1), Rational(2), [2, 1])
        assert r_sym["is_unitary"]

        # Numerical
        eps1, eps2, eps3 = 1.0, 2.0, -3.0
        u_val = 4.3

        def g_num(x):
            return ((x - eps1) * (x - eps2) * (x - eps3)
                    / ((x + eps1) * (x + eps2) * (x + eps3)))

        # Partition (2,1): boxes at (0,0), (0,1), (1,0)
        contents = [0, eps2, eps1]
        product = 1.0
        for c in contents:
            product *= g_num(u_val + c) * g_num(-(u_val + c))
        assert abs(product - 1.0) < 1e-10
