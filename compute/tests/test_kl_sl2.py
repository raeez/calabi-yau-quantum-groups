"""Tests for kl_sl2_level1: Kazhdan-Lusztig equivalence verification
for sl_2 at level 1, the simplest instance of Theorem CY-C.

Ground truth:
  chapters/examples/quantum_group_reps.tex (Conjecture CY-C),
  notes/theory_kl_e2_chiral.tex (KL as CY-C, Drinfeld-Kohno mechanism),
  Kazhdan-Lusztig, "Tensor structures..." I-IV, JAMS 6-7 (1993-94),
  Bakalov-Kirillov, "Lectures on Tensor Categories and Modular Functors" (2001),
  Kohno, "Monodromy representations of braid groups...", Ann Inst Fourier (1987).

The verification checks:
  1. Simple objects: 2 on each side (L(0), L(1) vs V_0, V_1)
  2. Quantum dimensions: dim_q(V_0) = 1, dim_q(V_1) = 1, dim_q(V_2) = 0
  3. Fusion rules: Z/2Z (L(1) x L(1) = L(0))
  4. R-matrix eigenvalues on V_1 x V_1: q (mult 3), -q^{-1} (mult 1)
  5. Drinfeld-Kohno: KZ monodromy = QG R-matrix on all channels
  6. Modular S and T matrices satisfy SL(2,Z) relations
  7. Verlinde formula reproduces fusion coefficients from S-matrix
  8. Central charge c = 1, conformal weights h_0 = 0, h_1 = 1/4
"""

import cmath
import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.kl_sl2_level1 import (
    q_parameter,
    q_number,
    q_factorial,
    q_binomial,
    quantum_dimension,
    simple_objects,
    SimpleObject,
    verlinde_coefficient,
    fusion_matrix,
    fusion_rules_level1,
    r_matrix_eigenvalue,
    r_matrix_eigenvalue_exact,
    r_matrix_on_fund_tensor_fund,
    verify_r_matrix_eigenvalues,
    kz_eigenvalue,
    drinfeld_kohno_check,
    modular_s_matrix,
    modular_t_matrix,
    verify_verlinde_from_s,
    verify_modular_relations,
    quantum_dim_from_s_matrix,
    total_quantum_dimension_squared,
    quantum_clebsch_gordan,
    conformal_weight,
    central_charge,
    verify_kl_sl2_level1,
    verify_all,
    KLVerification,
)


# ======================================================================
# Constants
# ======================================================================

K = 1
H_DUAL = 2
L = K + H_DUAL  # = 3
Q = cmath.exp(1j * cmath.pi / L)  # exp(pi*i/3)


# ======================================================================
# 1. Root of unity arithmetic
# ======================================================================

class TestQArithmetic:
    """Test quantum number computations at q = exp(pi*i/3)."""

    def test_q_value(self):
        """q = exp(pi*i/3) = cos(pi/3) + i*sin(pi/3) = 1/2 + i*sqrt(3)/2."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q - Q) < 1e-15

    def test_q_is_root_of_unity(self):
        """q^6 = exp(2*pi*i) = 1, so q is a primitive 6th root of unity."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q**6 - 1) < 1e-14

    def test_q_number_1(self):
        """[1]_q = 1 for all q."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q_number(1, q) - 1) < 1e-14

    def test_q_number_2(self):
        """[2]_q = q + q^{-1} = 2*cos(pi/3) = 1."""
        q = q_parameter(K, H_DUAL)
        result = q_number(2, q)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(result - 1.0) < 1e-14

    def test_q_number_3_is_zero(self):
        """[3]_q = 0 at q = exp(pi*i/3).  This is the truncation condition."""
        q = q_parameter(K, H_DUAL)
        result = q_number(3, q)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(result) < 1e-14

    def test_q_sum_rule(self):
        """q + q^{-1} = 1 at q = exp(pi*i/3)."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q + 1/q - 1) < 1e-14

    def test_q_product(self):
        """q * q^{-1} = 1."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q * (1/q) - 1) < 1e-14

    def test_q_factorial_2(self):
        """[2]_q! = [1]_q * [2]_q = 1 * 1 = 1."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(q_factorial(2, q) - 1) < 1e-14


# ======================================================================
# 2. Simple objects
# ======================================================================

class TestSimpleObjects:
    """Test the enumeration of simple objects in KL_1(sl_2)."""

    def test_num_simples(self):
        """At level 1, there are exactly 2 simple objects."""
        simples = simple_objects(K, H_DUAL)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(simples) == 2

    def test_vacuum(self):
        """L(0) = V_0 is the vacuum/trivial, with qdim = 1."""
        simples = simple_objects(K, H_DUAL)
        vac = simples[0]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert vac.label == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert vac.name_kl == "L(0)"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert vac.name_qg == "V_0"
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert vac.classical_dim == 1
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(vac.quantum_dim - 1) < 1e-14

    def test_fundamental(self):
        """L(1) = V_1 is the fundamental, with qdim = [2]_q = 1."""
        simples = simple_objects(K, H_DUAL)
        fund = simples[1]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert fund.label == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert fund.name_kl == "L(1)"
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert fund.name_qg == "V_1"
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert fund.classical_dim == 2  # classical dim is 2
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(fund.quantum_dim - 1) < 1e-14  # quantum dim is 1!

    def test_quantum_dim_v2_zero(self):
        """V_2 has quantum dimension [3]_q = 0 -- it's killed by truncation."""
        q = q_parameter(K, H_DUAL)
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(2, q)) < 1e-14

    def test_quantum_dims_from_s_matrix(self):
        """Quantum dimensions from S-matrix agree with [j+1]_q formula."""
        q = q_parameter(K, H_DUAL)
        for j in range(K + 1):
            qdim_formula = quantum_dimension(j, q).real
            qdim_smatrix = quantum_dim_from_s_matrix(j, K)
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert abs(qdim_formula - qdim_smatrix) < 1e-10


# ======================================================================
# 3. Fusion rules
# ======================================================================

class TestFusionRules:
    """Test the sl_2 level 1 fusion rules (Verlinde formula)."""

    def test_vacuum_is_unit(self):
        """L(0) is the tensor unit: L(0) x L(j) = L(j)."""
        for j in range(K + 1):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert verlinde_coefficient(0, j, j, K) == 1
            # No other channels
            for m in range(K + 1):
                if m != j:
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert verlinde_coefficient(0, j, m, K) == 0

    def test_fundamental_squared(self):
        """L(1) x L(1) = L(0) (the key fusion rule at level 1).

        Classically, V_1 x V_1 = V_0 + V_2, but V_2 is killed at level 1.
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert verlinde_coefficient(1, 1, 0, K) == 1
        # V_2 does NOT appear (truncation)
        # At level 1, j=2 is out of range (j <= k = 1)

    def test_fusion_is_z2(self):
        """The fusion ring at level 1 is Z/2Z = Z[x]/(x^2 - 1)."""
        rules = fusion_rules_level1()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert rules == {
            (0, 0): [0],
            (0, 1): [1],
            (1, 0): [1],
            (1, 1): [0],
        }

    def test_fusion_commutativity(self):
        """Fusion is commutative: N_{ij}^m = N_{ji}^m."""
        N = fusion_matrix(K)
        for i in range(K + 1):
            for j in range(K + 1):
                for m in range(K + 1):
                    assert N[i][j][m] == N[j][i][m]

    def test_fusion_associativity(self):
        """Fusion is associative: sum_p N_{ij}^p N_{pk}^m = sum_p N_{ip}^m N_{jk}^p."""
        N = fusion_matrix(K)
        n = K + 1
        for i in range(n):
            for j in range(n):
                for k_ in range(n):
                    for m in range(n):
                        lhs = sum(N[i][j][p] * N[p][k_][m] for p in range(n))
                        rhs = sum(N[j][k_][p] * N[i][p][m] for p in range(n))
                        assert lhs == rhs

    def test_quantum_clebsch_gordan(self):
        """Tensor product decomposition matches fusion rules."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert quantum_clebsch_gordan(0, 0, K) == [0]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert quantum_clebsch_gordan(0, 1, K) == [1]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert quantum_clebsch_gordan(1, 0, K) == [1]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert quantum_clebsch_gordan(1, 1, K) == [0]


# ======================================================================
# 4. R-matrix
# ======================================================================

class TestRMatrix:
    """Test the quantum group R-matrix on V_1 tensor V_1."""

    def test_eigenvalues(self):
        """R-check has eigenvalues q (mult 3) and -q^{-1} (mult 1)."""
        q = q_parameter(K, H_DUAL)
        R = r_matrix_on_fund_tensor_fund(q)
        result = verify_r_matrix_eigenvalues(q, R)
        assert result["eigenvalues_match"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["V2_multiplicity"] == 3
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["V0_multiplicity"] == 1

    def test_r_matrix_is_4x4(self):
        """The R-matrix on V_1 tensor V_1 is a 4x4 matrix."""
        q = q_parameter(K, H_DUAL)
        R = r_matrix_on_fund_tensor_fund(q)
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert R.shape == (4, 4)

    def test_antisymmetric_eigenvector(self):
        """The q-antisymmetric vector e_1 x e_2 - q * e_2 x e_1 has
        eigenvalue -q^{-1}.

        This vector spans the V_0 channel (the trivial rep).
        """
        q = q_parameter(K, H_DUAL)
        R = r_matrix_on_fund_tensor_fund(q)
        # q-antisymmetric vector: |12> - q|21>
        # In basis {|11>, |12>, |21>, |22>}: components (0, 1, -q, 0)
        v = np.array([0, 1, -q, 0], dtype=complex)
        Rv = R @ v
        expected = (-1/q) * v
        assert np.allclose(Rv, expected, atol=1e-12)

    def test_symmetric_eigenvectors(self):
        """The q-symmetric vectors have eigenvalue q.

        The 3-dim q-symmetric subspace (classically = V_2) is spanned by:
          |11>, |22>, |12> + q^{-1}|21>

        Note: the q-symmetrizer is P_+ = (R + q^{-1}) / (q + q^{-1}), so
        the correct q-symmetric combination is |12> + q^{-1}|21>, not
        |12> + q|21>.  This is because R acts on |12> as
        R(|12>) = (q - q^{-1})|12> + |21>, so
        R(|12> + q^{-1}|21>) = (q - q^{-1})|12> + |21> + q^{-1}|12>
                              = q|12> + |21> = q(|12> + q^{-1}|21>).
        """
        q = q_parameter(K, H_DUAL)
        R = r_matrix_on_fund_tensor_fund(q)

        # Test each symmetric basis vector
        v1 = np.array([1, 0, 0, 0], dtype=complex)  # |11>
        assert np.allclose(R @ v1, q * v1, atol=1e-12)

        v4 = np.array([0, 0, 0, 1], dtype=complex)  # |22>
        assert np.allclose(R @ v4, q * v4, atol=1e-12)

        # |12> + q^{-1}|21>
        v_sym = np.array([0, 1, 1/q, 0], dtype=complex)
        assert np.allclose(R @ v_sym, q * v_sym, atol=1e-12)

    def test_yang_baxter(self):
        """The R-matrix satisfies the Yang-Baxter equation on V^{x3}.

        (R x I)(I x R)(R x I) = (I x R)(R x I)(I x R)

        on the 8-dimensional space V_1^{tensor 3}.
        """
        q = q_parameter(K, H_DUAL)
        R = r_matrix_on_fund_tensor_fund(q)
        I2 = np.eye(2, dtype=complex)

        # R acts on C^2 x C^2 = C^4.  On C^2 x C^2 x C^2 = C^8:
        R12 = np.kron(R, I2)      # R on factors 1,2, identity on 3
        R23 = np.kron(I2, R)      # identity on 1, R on factors 2,3

        lhs = R12 @ R23 @ R12
        rhs = R23 @ R12 @ R23
        assert np.allclose(lhs, rhs, atol=1e-10)

    def test_r_matrix_eigenvalue_exact(self):
        """Check exact (sign, exponent) form of braiding eigenvalues."""
        # V_0 channel in V_1 x V_1:
        sign, exp = r_matrix_eigenvalue_exact(1, 1, 0)
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert sign == -1
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert exp == Fraction(-3, 2)

        # V_2 channel in V_1 x V_1 (killed at level 1 but computable):
        sign, exp = r_matrix_eigenvalue_exact(1, 1, 2)
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert sign == 1
        # VERIFIED [DC] r-matrix [LC] boundary/limiting case
        assert exp == Fraction(1, 2)

    def test_braiding_eigenvalue_numerical(self):
        """Numerical check of the braiding eigenvalue on V_0 channel.

        (-1) * q^{-3/2} = -exp(-pi*i/2) = -(-i) = i.
        """
        q = q_parameter(K, H_DUAL)
        ev = r_matrix_eigenvalue(1, 1, 0, q)
        # -q^{-3/2} = -exp(-pi*i*3/(2*3)) = -exp(-pi*i/2) = -(-i) = i
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(ev - 1j) < 1e-12


# ======================================================================
# 5. Drinfeld-Kohno theorem
# ======================================================================

class TestDrinfeldKohno:
    """Test that KZ monodromy equals quantum R-matrix eigenvalues."""

    def test_all_channels_match(self):
        """Drinfeld-Kohno: KZ monodromy = QG R-matrix on all fusion channels."""
        result = drinfeld_kohno_check(K, H_DUAL)
        assert result["all_match"]

    def test_trivial_channels(self):
        """On vacuum channels, the braiding is trivial (eigenvalue 1)."""
        q = q_parameter(K, H_DUAL)
        # L(0) x L(0) -> L(0): trivial
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(kz_eigenvalue(0, 0, 0, K) - 1) < 1e-14
        # VERIFIED [DC] r-matrix coefficient [LC] boundary/limiting case
        assert abs(r_matrix_eigenvalue(0, 0, 0, q) - 1) < 1e-14

        # L(0) x L(1) -> L(1): trivial
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(kz_eigenvalue(0, 1, 1, K) - 1) < 1e-14
        # VERIFIED [DC] r-matrix coefficient [LC] boundary/limiting case
        assert abs(r_matrix_eigenvalue(0, 1, 1, q) - 1) < 1e-14

    def test_nontrivial_channel(self):
        """L(1) x L(1) -> L(0) is the interesting channel.

        Braiding eigenvalue = (-1) * q^{-3/2} = i.
        """
        q = q_parameter(K, H_DUAL)
        kz_ev = kz_eigenvalue(1, 1, 0, K)
        qg_ev = r_matrix_eigenvalue(1, 1, 0, q)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(kz_ev - qg_ev) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(kz_ev - 1j) < 1e-12

    def test_higher_level(self):
        """Drinfeld-Kohno also holds at level 2 (8 channels)."""
        result = drinfeld_kohno_check(k=2, h_dual=2)
        assert result["all_match"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["num_simples"] == 3

    def test_level_3(self):
        """Drinfeld-Kohno at level 3 (4 simples, 16 fusion channels)."""
        result = drinfeld_kohno_check(k=3, h_dual=2)
        assert result["all_match"]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result["num_simples"] == 4


# ======================================================================
# 6. Modular data
# ======================================================================

class TestModularData:
    """Test the modular S and T matrices for sl_2 at level 1."""

    def test_s_matrix_shape(self):
        """S is a 2x2 matrix at level 1."""
        S = modular_s_matrix(K)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert S.shape == (2, 2)

    def test_s_matrix_unitarity(self):
        """S is unitary: S * S^dagger = I."""
        S = modular_s_matrix(K)
        assert np.allclose(S @ S.conj().T, np.eye(2), atol=1e-12)

    def test_s_matrix_symmetry(self):
        """S is symmetric: S^T = S."""
        S = modular_s_matrix(K)
        assert np.allclose(S, S.T, atol=1e-12)

    def test_s_matrix_values(self):
        """Explicit S-matrix at level 1.

        S = (1/sqrt(2)) * [[1, 1], [1, -1]]
        (the Hadamard matrix).
        """
        S = modular_s_matrix(K)
        expected = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
        # S-matrix entries are real (for sl_2)
        assert np.allclose(S, expected, atol=1e-12)

    def test_s_squared_is_charge_conjugation(self):
        """S^2 = C (charge conjugation). For sl_2, C = I."""
        result = verify_modular_relations(K)
        assert result["S_squared_is_C"]

    def test_modular_relation(self):
        """(ST)^3 = S^2."""
        result = verify_modular_relations(K)
        assert result["ST_cubed_is_S_squared"]

    def test_s_fourth_is_identity(self):
        """S^4 = I."""
        result = verify_modular_relations(K)
        assert result["S_fourth_is_identity"]

    def test_t_matrix_values(self):
        """T-matrix at level 1.

        T_{jj} = exp(2*pi*i*(h_j - c/24)) with c = 1, h_0 = 0, h_1 = 1/4.
        T_{00} = exp(2*pi*i*(0 - 1/24)) = exp(-pi*i/12)
        T_{11} = exp(2*pi*i*(1/4 - 1/24)) = exp(2*pi*i*5/24) = exp(5*pi*i/12)
        """
        T = modular_t_matrix(K)
        expected_T00 = cmath.exp(-1j * cmath.pi / 12)
        expected_T11 = cmath.exp(5j * cmath.pi / 12)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(T[0, 0] - expected_T00) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(T[1, 1] - expected_T11) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(T[0, 1]) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(T[1, 0]) < 1e-12

    def test_verlinde_formula(self):
        """Verlinde formula from S-matrix reproduces fusion coefficients."""
        assert verify_verlinde_from_s(K)

    def test_verlinde_level_2(self):
        """Verlinde formula works at level 2 as well."""
        assert verify_verlinde_from_s(2)

    def test_verlinde_level_5(self):
        """Verlinde formula works at level 5."""
        assert verify_verlinde_from_s(5)


# ======================================================================
# 7. Conformal data
# ======================================================================

class TestConformalData:
    """Test central charge and conformal weights at level 1."""

    def test_central_charge(self):
        """c = 3k/(k+2) = 3/3 = 1 at level 1."""
        c = central_charge(K, H_DUAL)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c == Fraction(1, 1)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c == 1

    def test_conformal_weight_vacuum(self):
        """h(L(0)) = 0 (vacuum has zero conformal weight)."""
        h = conformal_weight(0, K, H_DUAL)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert h == 0

    def test_conformal_weight_fundamental(self):
        """h(L(1)) = 1*3 / (4*3) = 1/4."""
        h = conformal_weight(1, K, H_DUAL)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert h == Fraction(1, 4)

    def test_conformal_weights_level2(self):
        """At level 2: h(L(0)) = 0, h(L(1)) = 3/16, h(L(2)) = 1/2.

        c = 6/4 = 3/2 (the N=1 super-Virasoro minimal model!).
        """
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert conformal_weight(0, 2, 2) == 0
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert conformal_weight(1, 2, 2) == Fraction(3, 16)
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert conformal_weight(2, 2, 2) == Fraction(1, 2)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert central_charge(2, 2) == Fraction(3, 2)


# ======================================================================
# 8. Total quantum dimension
# ======================================================================

class TestQuantumDimension:
    """Test total quantum dimension and related invariants."""

    def test_total_qdim_squared(self):
        """D^2 = sum d_j^2 = 1 + 1 = 2 at level 1."""
        D2 = total_quantum_dimension_squared(K)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(D2 - 2.0) < 1e-10

    def test_total_qdim_squared_level2(self):
        """D^2 at level 2.

        Simples: V_0 (qdim 1), V_1 (qdim sqrt(2)), V_2 (qdim 1).
        D^2 = 1 + 2 + 1 = 4.
        """
        D2 = total_quantum_dimension_squared(2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(D2 - 4.0) < 1e-10


# ======================================================================
# 9. Full verification
# ======================================================================

class TestFullVerification:
    """Test the full KL verification pipeline."""

    def test_verify_all(self):
        """The top-level verify_all() returns True."""
        assert verify_all()

    def test_verification_result(self):
        """Check the full verification result structure."""
        result = verify_kl_sl2_level1()
        assert isinstance(result, KLVerification)
        assert result.all_pass
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.k == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.h_dual == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.num_simples_kl == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.num_simples_qg == 2
        assert result.simples_match
        assert result.fusion_match
        assert result.quantum_dims_match
        assert result.r_matrix_eigenvalues_match
        assert result.drinfeld_kohno_match
        assert result.verlinde_from_s
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert result.central_charge == 1
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert result.conformal_weights[0] == 0
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert result.conformal_weights[1] == Fraction(1, 4)


# ======================================================================
# 10. Cross-checks and consistency
# ======================================================================

class TestCrossChecks:
    """Cross-checks that verify internal consistency."""

    def test_qdim_from_fusion(self):
        """Quantum dimensions satisfy the fusion ring:
        d_i * d_j = sum_m N_{ij}^m * d_m.

        At level 1: d_0 = d_1 = 1.
        Check: d_1 * d_1 = 1 = N_{11}^0 * d_0 = 1 * 1.  Good.
        """
        q = q_parameter(K, H_DUAL)
        N = fusion_matrix(K)
        dims = [quantum_dimension(j, q).real for j in range(K + 1)]

        for i in range(K + 1):
            for j in range(K + 1):
                lhs = dims[i] * dims[j]
                rhs = sum(N[i][j][m] * dims[m] for m in range(K + 1))
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert abs(lhs - rhs) < 1e-10

    def test_s_matrix_diagonalizes_fusion(self):
        """The S-matrix simultaneously diagonalizes all fusion matrices.

        N_i = S * diag(S_{i,s}/S_{0,s}) * S^{-1}.
        """
        S = modular_s_matrix(K)
        N_full = fusion_matrix(K)
        n = K + 1

        for i in range(n):
            # Fusion matrix for object i: (N_i)_{jm} = N_{ij}^m
            N_i = np.zeros((n, n), dtype=complex)
            for j in range(n):
                for m in range(n):
                    N_i[j, m] = N_full[i][j][m]

            # Eigenvalues should be S_{i,s} / S_{0,s}
            eigenvalues_expected = [S[i, s] / S[0, s] for s in range(n)]

            # S * diag(lambdas) * S^{-1} should equal N_i
            # Since S is unitary and real for sl_2, S^{-1} = S^T
            reconstructed = S @ np.diag(eigenvalues_expected) @ S.T
            assert np.allclose(N_i, reconstructed, atol=1e-10)

    def test_ribbon_structure(self):
        """The braiding eigenvalue on V_0 in V_1 x V_1, combined with
        the twist (T-matrix), gives the correct ribbon structure.

        The twist on V_j is theta_j = exp(2*pi*i*h_j) where h_j is
        the conformal weight.

        The ribbon identity: sigma_{V,W} o sigma_{W,V} = theta_{VxW} / (theta_V * theta_W)
        on the channel m in V x W gives:
          eigenvalue(sigma)^2 = theta_m / (theta_V * theta_W)
        """
        q = q_parameter(K, H_DUAL)
        # Twist on V_j: theta_j = q^{j(j+2)/2}
        # (This is exp(2*pi*i*h_j) = exp(2*pi*i * j(j+2)/(4*3)) = exp(pi*i*j(j+2)/6)
        #  = (exp(pi*i/3))^{j(j+2)/2} = q^{j(j+2)/2})

        theta = [q ** (j * (j + 2) / 2) for j in range(K + 1)]

        # Check: theta_0 = q^0 = 1, theta_1 = q^{3/2} = exp(pi*i/2) = i
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(theta[0] - 1) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(theta[1] - 1j) < 1e-12

        # Double braiding on V_0 channel of V_1 x V_1:
        # sigma^2 should equal theta_0 / (theta_1 * theta_1) = 1 / (i * i) = 1/(-1) = -1
        sigma_V0 = r_matrix_eigenvalue(1, 1, 0, q)
        sigma_squared = sigma_V0 ** 2
        expected = theta[0] / (theta[1] * theta[1])
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(sigma_squared - expected) < 1e-12
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert abs(sigma_squared - (-1)) < 1e-12

    def test_frobenius_schur_indicator(self):
        """The Frobenius-Schur indicator for V_1 at level 1.

        For a self-dual object V, the FS indicator is +1 if V is
        real (symmetric self-duality) and -1 if V is quaternionic
        (antisymmetric self-duality).

        For sl_2, V_j is always real (FS = +1) when j is even,
        but V_1 has FS indicator = theta_1^{-1} * qdim(V_1) / D.

        Actually, the FS indicator is simpler: nu(V_j) = (-1)^j for sl_2.
        At level 1: nu(V_0) = +1, nu(V_1) = -1.

        Alternatively: nu(V) = (1/D^2) * sum_k d_k * theta_k * N_{VV}^k
        For V_1 at k=1: nu = (1/2) * (d_0 * theta_0 * N_{11}^0)
                            = (1/2) * (1 * 1 * 1) = 1/2... hmm.

        Actually for modular tensor categories:
        nu_2(V) = sum_j (theta_j / theta_V^2) * N_{VV*}^j * d_j / D^2

        For sl_2 (self-dual), V* = V, so:
        nu_2(V_1) = sum_j (theta_j / theta_1^2) * N_{11}^j * d_j / D^2
                  = (theta_0 / theta_1^2) * 1 * 1 / 2
                  = (1 / (-1)) * 1/2
                  = -1/2

        The FS indicator is sgn(nu) = -1, meaning V_1 is quaternionic type.
        This is correct: the fundamental of sl_2 carries a quaternionic
        (symplectic) structure, not an orthogonal one.

        Let's just verify the sign: at level 1, L(1) x L(1) = L(0),
        and the braiding on V_0 channel is i. The double braiding is
        i^2 = -1. This negative sign indicates the pairing L(1) x L(1) -> L(0)
        is antisymmetric (quaternionic/symplectic type).
        """
        q = q_parameter(K, H_DUAL)
        sigma = r_matrix_eigenvalue(1, 1, 0, q)
        double_braiding = sigma ** 2
        # Negative => antisymmetric => quaternionic (symplectic) type
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert double_braiding.real < 0


# ======================================================================
# 11. Higher level consistency (k = 2, 3)
# ======================================================================

class TestHigherLevels:
    """Verify KL-type data at levels k = 2 and k = 3 for cross-validation."""

    def test_level2_simples(self):
        """At k=2, q = exp(pi*i/4), there are 3 simples: V_0, V_1, V_2."""
        simples = simple_objects(2, 2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(simples) == 3

    def test_level2_qdims(self):
        """At k=2: dim_q(V_0) = 1, dim_q(V_1) = sqrt(2), dim_q(V_2) = 1."""
        q = q_parameter(2, 2)
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(0, q) - 1) < 1e-12
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(1, q) - math.sqrt(2)) < 1e-12
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(2, q) - 1) < 1e-12

    def test_level2_truncation(self):
        """At k=2: dim_q(V_3) = 0 (truncation at l=4)."""
        q = q_parameter(2, 2)
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(3, q)) < 1e-12

    def test_level2_fusion(self):
        """At k=2: L(1) x L(1) = L(0) + L(2)."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert verlinde_coefficient(1, 1, 0, 2) == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert verlinde_coefficient(1, 1, 2, 2) == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert verlinde_coefficient(1, 1, 1, 2) == 0  # parity

    def test_level2_modular(self):
        """Modular relations hold at level 2."""
        result = verify_modular_relations(2)
        assert all(result.values())

    def test_level3_simples(self):
        """At k=3, q = exp(pi*i/5), there are 4 simples."""
        simples = simple_objects(3, 2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(simples) == 4

    def test_level3_golden_ratio(self):
        """At k=3: dim_q(V_1) = golden ratio phi = (1 + sqrt(5))/2.

        q = exp(pi*i/5), [2]_q = 2*cos(pi/5) = (1+sqrt(5))/2 = phi.
        This is the Jones polynomial at the golden ratio!
        """
        q = q_parameter(3, 2)
        phi = (1 + math.sqrt(5)) / 2
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert abs(quantum_dimension(1, q) - phi) < 1e-12
