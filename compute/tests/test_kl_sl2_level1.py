"""Tests for kl_sl2_level1: Kazhdan-Lusztig equivalence Rep_q(sl_2) ~ KL_1(sl_2).

Claims tested:
1. q = exp(pi*i/3) is the correct root of unity for k=1, h^v=2
2. Quantum integers: [1]_q = 1, [2]_q = 1, [3]_q = 0 (truncation)
3. Number of simple objects: k+1 = 2 on both sides
4. Fusion rules match Z/2Z: L(1) x L(1) = L(0)
5. R-matrix eigenvalues: q (multiplicity 3) and -q^{-1} (multiplicity 1)
6. Drinfeld-Kohno theorem: KZ monodromy = QG R-matrix eigenvalues
7. Verlinde formula reproduces fusion coefficients from S-matrix
8. Modular relations: S^2 = C, (ST)^3 = S^2, S^4 = I
9. Conformal data: c = 1, h_0 = 0, h_1 = 1/4
10. Quantum dimensions from S-matrix match [j+1]_q

Ground truth:
    Kazhdan-Lusztig JAMS 6-7 (1993-1994)
    Drinfeld-Kohno theorem
    Bakalov-Kirillov AMS 2001, Chapter 7
"""

import cmath
import math

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.kl_sl2_level1 import (
    q_parameter,
    q_number,
    quantum_dimension,
    simple_objects,
    fusion_rules_level1,
    verlinde_coefficient,
    r_matrix_on_fund_tensor_fund,
    verify_r_matrix_eigenvalues,
    kz_eigenvalue,
    drinfeld_kohno_check,
    modular_s_matrix,
    modular_t_matrix,
    verify_verlinde_from_s,
    verify_modular_relations,
    quantum_dim_from_s_matrix,
    conformal_weight,
    central_charge,
    verify_kl_sl2_level1,
    verify_all,
)


# ======================================================================
# 1. Root of unity arithmetic
# ======================================================================

class TestRootOfUnity:
    """Verify q-parameter and quantum integers at k=1."""

    def test_q_is_sixth_root(self):
        """q = exp(pi*i/3): sixth root of unity, q^6 = 1."""
        q = q_parameter(1, 2)
        assert abs(q**6 - 1.0) < 1e-12

    def test_q_value(self):
        """q = (1 + i*sqrt(3))/2."""
        q = q_parameter(1, 2)
        expected = cmath.exp(1j * cmath.pi / 3)
        assert abs(q - expected) < 1e-12

    def test_quantum_1(self):
        """[1]_q = 1 for any q."""
        q = q_parameter(1, 2)
        assert abs(q_number(1, q) - 1.0) < 1e-10

    def test_quantum_2(self):
        """[2]_q = q + q^{-1} = 2*cos(pi/3) = 1."""
        q = q_parameter(1, 2)
        val = q_number(2, q)
        # VERIFIED [DC] quantum integer [LT] KL equivalence
        assert abs(val - 1.0) < 1e-10

    def test_quantum_3_truncation(self):
        """[3]_q = 0 at q = exp(pi*i/3) -- this drives truncation."""
        q = q_parameter(1, 2)
        val = q_number(3, q)
        # VERIFIED [DC] truncation condition [LT] KL theory
        assert abs(val) < 1e-10


# ======================================================================
# 2. Simple objects
# ======================================================================

class TestSimpleObjects:
    """Verify simple object classification."""

    def test_two_simples(self):
        """k=1 has exactly 2 simple objects: L(0) and L(1)."""
        simples = simple_objects(1, 2)
        assert len(simples) == 2

    def test_quantum_dimensions(self):
        """dim_q(V_0) = 1, dim_q(V_1) = 1."""
        q = q_parameter(1, 2)
        assert abs(quantum_dimension(0, q) - 1.0) < 1e-10
        assert abs(quantum_dimension(1, q) - 1.0) < 1e-10

    def test_quantum_dim_from_s_matrix_matches(self):
        """Quantum dimensions from S-matrix match from formula."""
        q = q_parameter(1, 2)
        for j in range(2):
            qdim_formula = quantum_dimension(j, q).real
            qdim_s = quantum_dim_from_s_matrix(j, 1)
            # Multi-path: S-matrix and formula give same answer
            assert abs(qdim_formula - qdim_s) < 1e-10


# ======================================================================
# 3. Fusion rules
# ======================================================================

class TestFusionRules:
    """Verify fusion rules at level 1."""

    def test_z2_fusion(self):
        """Fusion rules are Z/2Z: L(1) x L(1) = L(0)."""
        rules = fusion_rules_level1()
        # VERIFIED [DC] fusion rule [LT] KL equivalence
        assert rules[(0, 0)] == [0]
        assert rules[(0, 1)] == [1]
        assert rules[(1, 0)] == [1]
        assert rules[(1, 1)] == [0]

    def test_verlinde_reproduces_fusion(self):
        """Verlinde formula from S-matrix reproduces combinatorial fusion."""
        # Multi-path: Verlinde formula and combinatorial rule agree
        assert verify_verlinde_from_s(1) is True

    def test_verlinde_higher_level(self):
        """Verlinde formula also works at k=2 (3 simples)."""
        assert verify_verlinde_from_s(2) is True


# ======================================================================
# 4. R-matrix
# ======================================================================

class TestRMatrix:
    """Verify R-matrix eigenvalues on V_1 x V_1."""

    def test_eigenvalues_match(self):
        """R-matrix has eigenvalues q (x3) and -q^{-1} (x1)."""
        q = q_parameter(1, 2)
        R = r_matrix_on_fund_tensor_fund(q)
        check = verify_r_matrix_eigenvalues(q, R)
        # VERIFIED [DC] R-matrix eigenvalue [LT] quantum group theory
        assert check['eigenvalues_match'] is True
        assert check['V2_multiplicity'] == 3
        assert check['V0_multiplicity'] == 1

    def test_r_matrix_shape(self):
        """R-matrix is 4x4 on V_1 x V_1 = C^2 x C^2."""
        q = q_parameter(1, 2)
        R = r_matrix_on_fund_tensor_fund(q)
        assert R.shape == (4, 4)


# ======================================================================
# 5. Drinfeld-Kohno theorem
# ======================================================================

class TestDrinfeldKohno:
    """Verify KZ monodromy = QG R-matrix (the Drinfeld-Kohno theorem)."""

    def test_drinfeld_kohno_level1(self):
        """All fusion channels at k=1: QG and KZ eigenvalues agree."""
        check = drinfeld_kohno_check(k=1, h_dual=2)
        # VERIFIED [DC] Drinfeld-Kohno matching [LT] KL equivalence
        assert check['all_match'] is True

    def test_drinfeld_kohno_level2(self):
        """The theorem also holds at level k=2."""
        check = drinfeld_kohno_check(k=2, h_dual=2)
        assert check['all_match'] is True


# ======================================================================
# 6. Modular data
# ======================================================================

class TestModularData:
    """Verify S and T matrices satisfy SL(2,Z) relations."""

    def test_modular_relations_level1(self):
        """S^2=C, (ST)^3=S^2, S^4=I at level 1."""
        rels = verify_modular_relations(1)
        assert rels['S_squared_is_C'] is True
        assert rels['ST_cubed_is_S_squared'] is True
        assert rels['S_fourth_is_identity'] is True

    def test_s_matrix_unitarity(self):
        """S-matrix is unitary."""
        S = modular_s_matrix(1)
        product = S @ S.conj().T
        assert np.allclose(product, np.eye(2), atol=1e-10)

    def test_s_matrix_symmetric(self):
        """S-matrix is symmetric."""
        S = modular_s_matrix(1)
        assert np.allclose(S, S.T, atol=1e-10)


# ======================================================================
# 7. Conformal data
# ======================================================================

class TestConformalData:
    """Verify central charge and conformal weights."""

    def test_central_charge_level1(self):
        """c = 3*1/(1+2) = 1."""
        c = central_charge(1, 2)
        # VERIFIED [DC] central charge [LT] WZW model
        assert c == Fraction(1)

    def test_conformal_weight_vacuum(self):
        """h_0 = 0."""
        h = conformal_weight(0, 1, 2)
        assert h == Fraction(0)

    def test_conformal_weight_fundamental(self):
        """h_1 = 1*3/(4*3) = 1/4."""
        h = conformal_weight(1, 1, 2)
        assert h == Fraction(1, 4)


# ======================================================================
# 8. Full verification
# ======================================================================

class TestFullVerification:
    """Run the comprehensive verification suite."""

    def test_verify_all_passes(self):
        """verify_all returns True (all sub-checks pass)."""
        assert verify_all() is True

    def test_verify_kl_sl2_level1(self):
        """Full KLVerification tuple: all_pass = True."""
        result = verify_kl_sl2_level1()
        assert result.all_pass is True
        assert result.simples_match is True
        assert result.fusion_match is True
        assert result.quantum_dims_match is True
        assert result.r_matrix_eigenvalues_match is True
        assert result.drinfeld_kohno_match is True
        assert result.verlinde_from_s is True
