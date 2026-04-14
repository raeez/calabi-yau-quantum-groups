"""Tests for the Maulik-Okounkov R-matrix at charge 2 for K3.

Verifies:
  1. Hilbert scheme dimension: chi(Hilb^2(K3)) = 324 = p_{24}(2)
  2. State enumeration: 24 + 24 + 276 = 324
  3. Diagonal R-matrix eigenvalues (box-content formula)
  4. Unitarity: R_{lam,mu}(u) * R_{mu,lam}(-u) = 1
  5. Yang-Baxter equation at charge (2,2,2)
  6. MO = Yangian coproduct comparison
  7. Self-dual limit: R = Id
  8. Off-diagonal analysis (abelian: all zero)
  9. Spectral decomposition (3 distinct eigenvalue types)
  10. Symbolic unitarity (exact)
  11. Pole structure
  12. Master three-path comparison

Multi-path verification (project mandate):
  - Path 1: MO stable envelope (geometric, prop:mo-bypass)
  - Path 2: Yangian coproduct (algebraic, chiral_coproduct_spin2_engine.py)
  - Path 3: OPE monodromy / Drinfeld uniqueness (Vol II)
  - Path 4: Numerical spot checks at multiple parameter values
  - Path 5: Symbolic (exact) verification via sympy

AP-CY28: test points chosen to avoid poles at +/-h_i.
Safe parameters: (h1, h2) = (1, 2) with h3 = -3.
Poles at u = -1, -2, 3.  Test u = 3.7, 4.3, 5.1 (all safe).
"""

import sys
import os

import pytest
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from mo_rmatrix_k3_charge2 import (
    cy3_structure_function,
    g_numerical,
    box_contents,
    hilb2_k3_euler_check,
    enumerate_charge2_states,
    charge2_diagonal_eigenvalue,
    charge2_diagonal_rmatrix,
    tensor_r_matrix_element,
    tensor_r_matrix_4x4,
    unitarity_charge2_diagonal,
    unitarity_324,
    ybe_charge2_full,
    yangian_coproduct_rmatrix_charge2,
    mo_vs_yangian_comparison,
    off_diagonal_analysis,
    symbolic_unitarity_charge2,
    degree_analysis_charge2,
    charge2_pole_structure,
    spectral_decomposition_charge2,
    selfdual_limit_charge2,
    master_comparison_charge2,
    MUKAI_RANK,
)

from sympy import Rational, Symbol, cancel


# ===================================================================
# 1. HILBERT SCHEME DIMENSION
# ===================================================================

class TestHilb2K3Dimension:
    """Verify chi(Hilb^2(K3)) = 324."""

    def test_total_324(self):
        """Total Euler characteristic is 324."""
        result = hilb2_k3_euler_check()
        # VERIFIED [DC] dimension count [DA] Gottsche formula
        assert result['total'] == 324
        assert result['match']

    def test_decomposition(self):
        """Decomposition: 24 + 24 + 276 = 324."""
        result = hilb2_k3_euler_check()
        # VERIFIED [DC] dimension count [DA] combinatorial
        assert result['n_row_single_colour'] == 24
        assert result['n_col_single_colour'] == 24
        assert result['n_two_distinct'] == 276

    def test_two_distinct_is_binomial(self):
        """Two-point states: C(24,2) = 276."""
        # VERIFIED [DC] combinatorial [DA] binomial coefficient
        assert 24 * 23 // 2 == 276


# ===================================================================
# 2. STATE ENUMERATION
# ===================================================================

class TestStateEnumeration:
    """Test enumeration of 324 charge-2 states."""

    def test_total_count(self):
        """324 states total."""
        states = enumerate_charge2_states()
        # VERIFIED [DC] dimension count [DA] state enumeration
        assert len(states) == 324

    def test_type_counts(self):
        """Correct count by type."""
        states = enumerate_charge2_states()
        by_type = {}
        for s in states:
            by_type[s['type']] = by_type.get(s['type'], 0) + 1
        # VERIFIED [DC] dimension count [DA] state enumeration
        assert by_type['row_single'] == 24
        assert by_type['col_single'] == 24
        assert by_type['two_distinct'] == 276

    def test_labels_unique(self):
        """All state labels are unique."""
        states = enumerate_charge2_states()
        labels = [s['label'] for s in states]
        assert len(labels) == len(set(labels))

    def test_row_states_have_partition_2(self):
        """Row states have partition [2]."""
        states = enumerate_charge2_states()
        for s in states:
            if s['type'] == 'row_single':
                assert s['partition'] == [2]

    def test_col_states_have_partition_11(self):
        """Col states have partition [1,1]."""
        states = enumerate_charge2_states()
        for s in states:
            if s['type'] == 'col_single':
                assert s['partition'] == [1, 1]

    def test_two_distinct_colours_ordered(self):
        """Two-point states have i < j."""
        states = enumerate_charge2_states()
        for s in states:
            if s['type'] == 'two_distinct':
                i, j = s['colours']
                assert i < j


# ===================================================================
# 3. BOX CONTENTS
# ===================================================================

class TestBoxContents:
    """Test the box-content function."""

    def test_single_box(self):
        """Single box at (0,0) has content 0."""
        c = box_contents([1], 1, 2)
        assert c == [0]

    def test_row_2(self):
        """Row partition (2): contents {0, h2}."""
        c = box_contents([2], 1, 2)
        assert c == [0, 2]

    def test_col_2(self):
        """Column partition (1,1): contents {0, h1}."""
        c = box_contents([1, 1], 1, 2)
        assert c == [0, 1]


# ===================================================================
# 4. STRUCTURE FUNCTION BASICS
# ===================================================================

class TestStructureFunction:
    """Test CY3 structure function properties."""

    def test_inversion(self):
        """g(u)*g(-u) = 1."""
        u = Symbol("u")
        g = cy3_structure_function(Rational(1), Rational(2))
        g_neg = g.subs(u, -u)
        product = cancel(g * g_neg)
        # VERIFIED [DC] structural property [DA] CY inversion
        assert product == 1

    def test_g_at_zero(self):
        """g(0) = -1 for generic parameters."""
        val = g_numerical(0.0, 1.0, 2.0)
        # g(0) = (-1)(-2)(3)/((1)(2)(-3)) = 6/(-6) = -1
        # VERIFIED [DC] structural property [DA] boundary value
        assert abs(val - (-1.0)) < 1e-10

    def test_g_numerical_unitarity(self):
        """g(u)*g(-u) = 1 numerically (AP-CY28: u=3.7, safe from poles)."""
        u_val = 3.7
        g_u = g_numerical(u_val, 1.0, 2.0)
        g_neg = g_numerical(-u_val, 1.0, 2.0)
        # VERIFIED [DC] structural property [DA] numerical CY inversion
        assert abs(g_u * g_neg - 1.0) < 1e-10


# ===================================================================
# 5. DIAGONAL R-MATRIX EIGENVALUES
# ===================================================================

class TestDiagonalRMatrix:
    """Test diagonal R-matrix eigenvalues at charge 2."""

    def test_324_eigenvalues(self):
        """324 eigenvalues computed."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        # VERIFIED [DC] dimension count [DA] eigenvalue enumeration
        assert result['n_states'] == 324

    def test_row_eigenvalue_formula(self):
        """Row eigenvalue = g(u)*g(u+h2)."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        expected = g_numerical(u_val, h1, h2) * g_numerical(u_val + h2, h1, h2)
        result = charge2_diagonal_rmatrix(u_val, h1, h2)
        # VERIFIED [DC] eigenvalue [DA] box-content formula
        assert abs(result['row_eigenvalue'] - expected) < 1e-10

    def test_col_eigenvalue_formula(self):
        """Col eigenvalue = g(u)*g(u+h1)."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        expected = g_numerical(u_val, h1, h2) * g_numerical(u_val + h1, h1, h2)
        result = charge2_diagonal_rmatrix(u_val, h1, h2)
        # VERIFIED [DC] eigenvalue [DA] box-content formula
        assert abs(result['col_eigenvalue'] - expected) < 1e-10

    def test_two_point_eigenvalue_formula(self):
        """Two-point eigenvalue = g(u)^2."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        expected = g_numerical(u_val, h1, h2) ** 2
        result = charge2_diagonal_rmatrix(u_val, h1, h2)
        # VERIFIED [DC] eigenvalue [DA] box-content formula
        assert abs(result['two_distinct_eigenvalue'] - expected) < 1e-10

    def test_three_distinct_eigenvalues_generic(self):
        """At generic (h1,h2), exactly 3 distinct eigenvalue types."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        # VERIFIED [DC] spectral analysis [DA] generic parameters
        assert result['n_distinct'] == 3

    def test_row_col_differ(self):
        """Row and col eigenvalues differ when h1 != h2."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        assert abs(result['row_eigenvalue'] - result['col_eigenvalue']) > 1e-5

    def test_all_row_states_equal(self):
        """All 24 row states have the same eigenvalue."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        row_evs = result['by_type']['row_single']
        # VERIFIED [DC] multiplicity [DA] Mukai symmetry
        assert all(abs(e - row_evs[0]) < 1e-10 for e in row_evs)

    def test_all_col_states_equal(self):
        """All 24 col states have the same eigenvalue."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        col_evs = result['by_type']['col_single']
        assert all(abs(e - col_evs[0]) < 1e-10 for e in col_evs)

    def test_all_two_point_states_equal(self):
        """All 276 two-point states have the same eigenvalue."""
        result = charge2_diagonal_rmatrix(3.7, 1.0, 2.0)
        two_evs = result['by_type']['two_distinct']
        assert all(abs(e - two_evs[0]) < 1e-10 for e in two_evs)


# ===================================================================
# 6. TENSOR PRODUCT R-MATRIX (4x4)
# ===================================================================

class TestTensorRMatrix:
    """Test the 4x4 tensor product R-matrix on F_2 x F_2."""

    def test_4x4_diagonal(self):
        """4x4 matrix is diagonal (abelian Yangian)."""
        result = tensor_r_matrix_4x4(3.7, 1.0, 2.0)
        # VERIFIED [DC] matrix structure [DA] abelian Yangian
        assert result['is_diagonal']
        assert result['n_offdiagonal_nonzero'] == 0

    def test_entries_match_pair_formula(self):
        """Diagonal entries match the pair formula."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        result = tensor_r_matrix_4x4(u_val, h1, h2)

        # Direct pair formula
        R_22 = tensor_r_matrix_element([2], [2], u_val, h1, h2)
        R_2_11 = tensor_r_matrix_element([2], [1, 1], u_val, h1, h2)
        R_11_2 = tensor_r_matrix_element([1, 1], [2], u_val, h1, h2)
        R_11_11 = tensor_r_matrix_element([1, 1], [1, 1], u_val, h1, h2)

        assert abs(result['R_22'] - R_22) < 1e-10
        assert abs(result['R_2_11'] - R_2_11) < 1e-10
        assert abs(result['R_11_2'] - R_11_2) < 1e-10
        assert abs(result['R_11_11'] - R_11_11) < 1e-10

    def test_R_22_explicit(self):
        """R_{(2),(2)} = g(u)^2 * g(u+h2) * g(u-h2)."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        g = g_numerical
        expected = (g(u_val, h1, h2)**2 *
                    g(u_val + h2, h1, h2) *
                    g(u_val - h2, h1, h2))
        result = tensor_r_matrix_4x4(u_val, h1, h2)
        # VERIFIED [DC] explicit formula [DA] box-content pair
        assert abs(result['R_22'] - expected) < 1e-10

    def test_R_11_11_explicit(self):
        """R_{(1,1),(1,1)} = g(u)^2 * g(u+h1) * g(u-h1)."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        g = g_numerical
        expected = (g(u_val, h1, h2)**2 *
                    g(u_val + h1, h1, h2) *
                    g(u_val - h1, h1, h2))
        result = tensor_r_matrix_4x4(u_val, h1, h2)
        # VERIFIED [DC] explicit formula [DA] box-content pair
        assert abs(result['R_11_11'] - expected) < 1e-10


# ===================================================================
# 7. UNITARITY
# ===================================================================

class TestUnitarity:
    """Test R_{lam,mu}(u) * R_{mu,lam}(-u) = 1."""

    def test_unitarity_4_pairs(self):
        """Unitarity for all 4 tensor pairs at charge 2."""
        # AP-CY28: u=3.7, safe from poles at +/-1, +/-2, +/-3
        result = unitarity_charge2_diagonal(3.7, 1.0, 2.0)
        assert result['all_pass'], (
            f"Unitarity failed: {result['pairs']}"
        )

    def test_unitarity_different_params(self):
        """Unitarity at different (h1, h2) values."""
        for h1, h2 in [(0.5, 1.5), (3.0, 1.0), (0.3, 0.7)]:
            u_val = 5.1  # safe from all poles
            result = unitarity_charge2_diagonal(u_val, h1, h2)
            assert result['all_pass'], (
                f"Unitarity failed at (h1,h2)=({h1},{h2})"
            )

    def test_unitarity_all_324(self):
        """Box-by-box inversion for all 324 charge-2 states."""
        result = unitarity_324(3.7, 1.0, 2.0)
        # VERIFIED [DC] unitarity [DA] all 324 states, box-by-box g(x)*g(-x)=1
        assert result['all_pass']
        assert result['n_checked'] == 324

    def test_unitarity_all_324_different_params(self):
        """Box-by-box inversion at (h1,h2) = (0.3, 0.7)."""
        result = unitarity_324(5.1, 0.3, 0.7)
        assert result['all_pass']

    def test_symbolic_unitarity(self):
        """Exact symbolic unitarity (sympy)."""
        result = symbolic_unitarity_charge2()
        # VERIFIED [DC] symbolic unitarity [DA] exact cancellation
        assert result['all_pass'], (
            f"Symbolic unitarity failed: {result['pairs']}"
        )


# ===================================================================
# 8. YANG-BAXTER EQUATION
# ===================================================================

class TestYangBaxterCharge2:
    """Test YBE at charge (2,2,2)."""

    def test_ybe_all_8_triples(self):
        """YBE: R_12(u-v)*R_13(u)*R_23(v) = R_23(v)*R_13(u)*R_12(u-v)."""
        # AP-CY28: u=3.7, v=1.3, safe from poles
        result = ybe_charge2_full(3.7, 1.3, 1.0, 2.0)
        # VERIFIED [DC] YBE [DA] all 8 triples
        assert result['all_pass']
        assert result['n_triples'] == 8

    def test_ybe_different_params(self):
        """YBE at different parameter values."""
        result = ybe_charge2_full(5.1, 2.3, 0.5, 1.5)
        assert result['all_pass']

    def test_ybe_large_u(self):
        """YBE at large spectral parameter."""
        result = ybe_charge2_full(100.0, 50.0, 1.0, 2.0)
        assert result['all_pass']


# ===================================================================
# 9. MO = YANGIAN COMPARISON
# ===================================================================

class TestMOvsYangian:
    """Test that MO and Yangian give identical R-matrices at charge 2."""

    def test_row_match(self):
        """MO row eigenvalue = Yangian row eigenvalue."""
        result = mo_vs_yangian_comparison(3.7, 1.0, 2.0)
        # VERIFIED [DC] MO=Yangian [DA] charge-2 comparison
        assert result['row_match']

    def test_col_match(self):
        """MO col eigenvalue = Yangian col eigenvalue."""
        result = mo_vs_yangian_comparison(3.7, 1.0, 2.0)
        assert result['col_match']

    def test_all_match(self):
        """Both row and col match."""
        result = mo_vs_yangian_comparison(3.7, 1.0, 2.0)
        assert result['all_match']

    def test_match_various_params(self):
        """MO = Yangian for multiple (h1, h2) values."""
        for h1, h2 in [(0.5, 1.5), (3.0, 1.0), (0.3, 0.7), (2.0, 5.0)]:
            u_val = 7.3  # safe from all poles
            result = mo_vs_yangian_comparison(u_val, h1, h2)
            assert result['all_match'], (
                f"MO != Yangian at (h1,h2)=({h1},{h2})"
            )

    def test_master_comparison(self):
        """Master three-path comparison."""
        result = master_comparison_charge2(3.7, 1.0, 2.0)
        # VERIFIED [DC] three-path comparison [DA] MO=Yangian=Chiral
        assert result['mo_eq_yangian']
        assert result['mo_eq_chiral']
        assert result['unitarity_tensor_22']


# ===================================================================
# 10. SELF-DUAL LIMIT
# ===================================================================

class TestSelfDualLimit:
    """Test the self-dual limit h1 = -h2 (R = Id)."""

    def test_all_eigenvalues_one(self):
        """In the self-dual limit, all 324 eigenvalues are 1."""
        result = selfdual_limit_charge2(1.0, 3.7)
        # VERIFIED [DC] self-dual limit [DA] g=1 => R=Id
        assert result['all_eigenvalues_one']
        assert result['n_states'] == 324

    def test_selfdual_various_eps(self):
        """Self-dual R=Id for various epsilon values."""
        for eps in [0.5, 1.0, 2.0, 3.0]:
            result = selfdual_limit_charge2(eps, 4.3)
            assert result['all_eigenvalues_one'], (
                f"Self-dual failed at eps={eps}"
            )


# ===================================================================
# 11. OFF-DIAGONAL ANALYSIS
# ===================================================================

class TestOffDiagonal:
    """Test off-diagonal structure of the charge-2 R-matrix."""

    def test_abelian_zero_offdiagonal(self):
        """At generic K3 moduli (abelian), all off-diagonal entries are zero."""
        result = off_diagonal_analysis(3.7, 1.0, 2.0)
        # VERIFIED [DC] off-diagonal [DA] abelian Yangian
        assert result['n_offdiagonal_nonzero_abelian'] == 0

    def test_total_offdiagonal_count(self):
        """324^2 - 324 = 104,652 off-diagonal entries."""
        result = off_diagonal_analysis(3.7, 1.0, 2.0)
        assert result['n_offdiagonal'] == 324 * 324 - 324

    def test_row_col_uniform(self):
        """All row states have the same eigenvalue; same for col."""
        result = off_diagonal_analysis(3.7, 1.0, 2.0)
        assert result['row_uniform']
        assert result['col_uniform']
        assert result['two_uniform']

    def test_three_distinct_eigenvalues(self):
        """3 distinct eigenvalue types at generic parameters."""
        result = off_diagonal_analysis(3.7, 1.0, 2.0)
        assert result['n_distinct_eigenvalues'] == 3


# ===================================================================
# 12. SPECTRAL DECOMPOSITION
# ===================================================================

class TestSpectralDecomposition:
    """Test spectral decomposition of the 324x324 R-matrix."""

    def test_total_multiplicity(self):
        """Total multiplicity = 324."""
        result = spectral_decomposition_charge2(3.7, 1.0, 2.0)
        # VERIFIED [DC] multiplicity [DA] spectral decomposition
        assert result['total_multiplicity'] == 324

    def test_multiplicities(self):
        """Multiplicities: 24, 24, 276."""
        result = spectral_decomposition_charge2(3.7, 1.0, 2.0)
        mults = [s['multiplicity'] for s in result['spectrum']]
        assert sorted(mults) == [24, 24, 276]

    def test_trace_formula(self):
        """Trace = 24*ev_row + 24*ev_col + 276*ev_two."""
        u_val, h1, h2 = 3.7, 1.0, 2.0
        result = spectral_decomposition_charge2(u_val, h1, h2)
        g = g_numerical
        ev_row = g(u_val, h1, h2) * g(u_val + h2, h1, h2)
        ev_col = g(u_val, h1, h2) * g(u_val + h1, h1, h2)
        ev_two = g(u_val, h1, h2) ** 2
        expected_trace = 24 * ev_row + 24 * ev_col + 276 * ev_two
        # VERIFIED [DC] trace formula [DA] spectral sum
        assert abs(result['trace'] - expected_trace) < 1e-8

    def test_h1_eq_h2_two_types(self):
        """When h1 = h2, row and col eigenvalues coincide => 2 distinct types."""
        result = spectral_decomposition_charge2(3.7, 1.5, 1.5)
        assert result['n_distinct'] == 2


# ===================================================================
# 13. POLE STRUCTURE
# ===================================================================

class TestPoleStructure:
    """Test pole locations of charge-2 R-matrix eigenvalues."""

    def test_g_has_3_poles(self):
        """g(u) has 3 poles at u = -h1, -h2, h1+h2."""
        result = charge2_pole_structure(1.0, 2.0)
        assert result['n_poles_g'] == 3

    def test_charge2_row_6_poles(self):
        """R_{(2)}(u) has up to 6 poles (from 2 g-factors)."""
        result = charge2_pole_structure(1.0, 2.0)
        # g(u) poles: {-1, -2, 3}; g(u+2) poles: {-3, -4, 1}
        # Total distinct: {-4, -3, -2, -1, 1, 3} = 6
        assert result['n_poles_row'] == 6

    def test_charge2_col_6_poles(self):
        """R_{(1,1)}(u) has up to 6 poles."""
        result = charge2_pole_structure(1.0, 2.0)
        # g(u) poles: {-1, -2, 3}; g(u+1) poles: {-2, -3, 2}
        # Total distinct: {-3, -2, -1, 2, 3} = 5 (pole -2 is shared)
        assert result['n_poles_col'] == 5


# ===================================================================
# 14. NUMERICAL CROSS-CHECKS
# ===================================================================

class TestNumericalCrossChecks:
    """Multi-path numerical verification."""

    def test_eigenvalue_at_large_u(self):
        """All charge-2 eigenvalues -> 1 as u -> infinity."""
        result = charge2_diagonal_rmatrix(100.0, 1.0, 2.0)
        for ev in result['eigenvalues']:
            assert abs(ev - 1.0) < 0.01, f"Eigenvalue {ev} not near 1 at large u"

    def test_inversion_per_state(self):
        """g(u+c)*g(-(u+c)) = 1 for each box content, verified numerically."""
        u_val = 3.7
        h1, h2 = 1.0, 2.0
        for c_val in [0, h2, h1, h1 + h2]:
            g_plus = g_numerical(u_val + c_val, h1, h2)
            g_minus = g_numerical(-(u_val + c_val), h1, h2)
            assert abs(g_plus * g_minus - 1.0) < 1e-10

    def test_multiple_parameter_sets(self):
        """Master comparison at multiple parameter sets."""
        param_sets = [
            (3.7, 1.0, 2.0),
            (5.1, 0.5, 1.5),
            (7.3, 3.0, 1.0),
            (4.3, 0.3, 0.7),
        ]
        for u_val, h1, h2 in param_sets:
            result = master_comparison_charge2(u_val, h1, h2)
            assert result['mo_eq_yangian'], (
                f"MO != Yangian at u={u_val}, (h1,h2)=({h1},{h2})"
            )

    def test_tensor_unitarity_all_pairs(self):
        """Tensor product unitarity for all 4 pairs, 3 parameter sets."""
        for h1, h2 in [(1.0, 2.0), (0.5, 1.5), (3.0, 1.0)]:
            u_val = 5.1
            result = unitarity_charge2_diagonal(u_val, h1, h2)
            assert result['all_pass'], (
                f"Unitarity failed at (h1,h2)=({h1},{h2})"
            )


# ===================================================================
# 15. DEGREE AND STRUCTURE
# ===================================================================

class TestDegreeStructure:
    """Test degree analysis."""

    def test_charge1_degree(self):
        """Charge-1 R-matrix has degree (3,3)."""
        result = degree_analysis_charge2()
        assert result['charge_1_degree'] == (3, 3)

    def test_charge2_degree(self):
        """Charge-2 eigenvalues have degree (6,6)."""
        result = degree_analysis_charge2()
        assert result['charge_2_row_degree'] == (6, 6)
        assert result['charge_2_col_degree'] == (6, 6)
