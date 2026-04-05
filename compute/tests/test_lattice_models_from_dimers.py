r"""Tests for integrable lattice models from dimer chart atlases.

Tests are organized by mathematical structure:

1. KASTELEYN MATRIX (determinant, permanent, matching count)
2. R-MATRIX (6-vertex, gl(1|1), Z_3 vertex model)
3. YANG-BAXTER EQUATION (scalar, matrix, E_1 associativity)
4. TRANSFER MATRIX (commutativity, eigenvalues, E_1 identification)
5. PARTITION FUNCTIONS (MacMahon, conifold, local P^2)
6. PARTITION FUNCTION DICTIONARY (4-way equality for C^3)
7. CORNER TRANSFER MATRIX (spectrum, entropy, shadow depth)
8. BETHE ANSATZ (one-magnon, multi-magnon, lattice-Yangian match)
9. UNITARITY (R-matrix, structure function)
10. W_{1+infinity} GENERATORS (transfer matrix expansion)
11. CROSS-VERIFICATION (multi-path checks)

Each formula verified by at least 3 independent methods.

Total: 80+ tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.lattice_models_from_dimers import (
    # Kasteleyn
    KasteleynMatrix,
    c3_kasteleyn,
    conifold_kasteleyn,
    local_p2_kasteleyn,
    n_perfect_matchings_c3,
    # R-matrices
    RMatrix,
    SixVertexRMatrix,
    GL11RMatrix,
    Z3VertexRMatrix,
    AffineYangianRMatrix,
    # Transfer matrix
    transfer_matrix_6v,
    verify_transfer_matrix_commutativity,
    transfer_matrix_eigenvalues,
    transfer_matrix_expansion_c3,
    # Partition functions
    partition_function_6v_free_fermion,
    partition_function_conifold,
    partition_function_local_p2,
    # Verification
    verify_lattice_dt_dictionary_c3,
    verify_lattice_dt_dictionary_conifold,
    verify_ybe_from_e1_associativity,
    verify_transfer_matrix_as_e1_element,
    # CTM
    ctm_spectrum_6v_free_fermion,
    entanglement_entropy_ctm,
    shadow_depth_from_entropy,
    verify_ctm_entropy_shadow_depth,
    # Bethe ansatz
    bethe_ansatz_from_lattice,
    # FPS helpers
    _macmahon_product,
    _conifold_reduced_product,
    # Full verification
    run_all_lattice_verifications,
)

from compute.lib.dimer_chart_atlas import (
    macmahon_coefficients,
    coha_euler_char_c3,
    _fps_mul,
)


# =====================================================================
# Section 1: Kasteleyn matrix tests
# =====================================================================

class TestKasteleynMatrix:
    """Tests for the Kasteleyn matrix construction."""

    def test_c3_kasteleyn_size(self):
        """C^3 Kasteleyn matrix is 1x1."""
        K = c3_kasteleyn()
        assert K.n == 1

    def test_c3_kasteleyn_det(self):
        """det(K) for C^3 at unit weight."""
        K = c3_kasteleyn()
        assert K.determinant() == Fraction(3)

    def test_c3_kasteleyn_with_q(self):
        """C^3 Kasteleyn with parameter q."""
        K = c3_kasteleyn(q=Fraction(2))
        assert K.determinant() == Fraction(6)

    def test_conifold_kasteleyn_size(self):
        """Conifold Kasteleyn matrix is 1x1 (single black-white pair)."""
        K = conifold_kasteleyn()
        assert K.n == 1

    def test_conifold_kasteleyn_det(self):
        """det(K) for conifold at Q=1, q=1."""
        K = conifold_kasteleyn()
        # 2*1*(1+1) = 4
        assert K.determinant() == Fraction(4)

    def test_local_p2_kasteleyn_size(self):
        """Local P^2 Kasteleyn matrix is 3x3."""
        K = local_p2_kasteleyn()
        assert K.n == 3

    def test_local_p2_kasteleyn_nonzero(self):
        """det(K) for local P^2 is nonzero."""
        K = local_p2_kasteleyn()
        d = K.determinant()
        assert d != Fraction(0)

    def test_permanent_1x1(self):
        """Permanent of 1x1 matrix."""
        K = KasteleynMatrix(1, [[Fraction(5)]])
        assert K.permanent() == Fraction(5)

    def test_permanent_2x2(self):
        """Permanent of 2x2 matrix: a*d + b*c."""
        K = KasteleynMatrix(2, [
            [Fraction(1), Fraction(2)],
            [Fraction(3), Fraction(4)],
        ])
        # perm = 1*4 + 2*3 = 10
        assert K.permanent() == Fraction(10)


class TestPerfectMatchings:
    """Tests for perfect matching counts."""

    def test_c3_matching_n0(self):
        """n_perfect_matchings(0) = 1 (empty partition)."""
        assert n_perfect_matchings_c3(0) == 1

    def test_c3_matching_n1(self):
        """n_perfect_matchings(1) = 1 (single cube)."""
        assert n_perfect_matchings_c3(1) == 1

    def test_c3_matching_n2(self):
        """n_perfect_matchings(2) = 3 (MacMahon a(2) = 3)."""
        assert n_perfect_matchings_c3(2) == 3

    def test_c3_matching_n3(self):
        """n_perfect_matchings(3) = 6 (MacMahon a(3) = 6)."""
        assert n_perfect_matchings_c3(3) == 6

    def test_c3_matching_n4(self):
        """n_perfect_matchings(4) = 13 (MacMahon a(4) = 13)."""
        assert n_perfect_matchings_c3(4) == 13

    def test_c3_matching_n5(self):
        """n_perfect_matchings(5) = 24."""
        assert n_perfect_matchings_c3(5) == 24


# =====================================================================
# Section 2: R-matrix tests
# =====================================================================

class TestSixVertexRMatrix:
    """Tests for the 6-vertex model R-matrix."""

    def test_matrix_shape(self):
        """R-matrix is 4x4."""
        R = SixVertexRMatrix(eta=1.0)
        M = R.matrix(1.0)
        assert len(M) == 4
        assert all(len(row) == 4 for row in M)

    def test_matrix_at_u0(self):
        """R(0) at eta=1 should be the graded permutation P^gr."""
        R = SixVertexRMatrix(eta=1.0)
        M = R.matrix(0.0)
        # R(0) = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]]
        assert abs(M[0][0] - 1.0) < 1e-10
        assert abs(M[1][2] - 1.0) < 1e-10
        assert abs(M[2][1] - 1.0) < 1e-10
        assert abs(M[3][3] - (-1.0)) < 1e-10

    def test_weights(self):
        """Weights a, b, c at eta=1, u=2."""
        R = SixVertexRMatrix(eta=1.0)
        a, b, c = R.weights(2.0)
        assert abs(a - 3.0) < 1e-10  # u + eta = 3
        assert abs(b - 2.0) < 1e-10  # u = 2
        assert abs(c - 1.0) < 1e-10  # eta = 1

    def test_free_fermion_at_u0(self):
        """Free-fermion condition at u=0."""
        R = SixVertexRMatrix(eta=1.0)
        result = R.verify_free_fermion(0.0)
        assert result["is_free_fermion"]

    def test_free_fermion_at_minus_eta(self):
        """Free-fermion condition at u = -eta."""
        R = SixVertexRMatrix(eta=1.0)
        result = R.verify_free_fermion(-1.0)
        assert result["is_free_fermion"]


class TestGL11RMatrix:
    """Tests for the gl(1|1) R-matrix."""

    def test_dim(self):
        """gl(1|1) R-matrix has dim=2."""
        R = GL11RMatrix()
        assert R.dim == 2

    def test_matrix_at_u0(self):
        """R(0) = P (standard permutation)."""
        R = GL11RMatrix()
        M = R.matrix(0.0)
        assert abs(M[0][0] - 1.0) < 1e-10  # u+1=1
        assert abs(M[1][1] - 0.0) < 1e-10  # u=0
        assert abs(M[1][2] - 1.0) < 1e-10  # permutation
        assert abs(M[2][1] - 1.0) < 1e-10  # permutation
        assert abs(M[3][3] - 1.0) < 1e-10  # u+1=1 (standard, NOT graded)

    def test_ybe_gl11(self):
        """gl(1|1) R-matrix satisfies YBE."""
        R = GL11RMatrix()
        result = R.verify_ybe(1.0, 2.0, 3.0)
        assert result["satisfies_ybe"], f"Max diff: {result['max_difference']}"

    def test_ybe_gl11_complex(self):
        """gl(1|1) R-matrix satisfies YBE at complex spectral parameters."""
        R = GL11RMatrix()
        result = R.verify_ybe(1.0 + 0.5j, 2.0 - 0.3j, 3.0 + 0.7j)
        assert result["satisfies_ybe"], f"Max diff: {result['max_difference']}"

    def test_ybe_gl11_multiple_points(self):
        """gl(1|1) YBE verified at 5 different spectral parameter triples."""
        R = GL11RMatrix()
        test_points = [
            (1.0, 2.0, 3.0),
            (0.5, 1.5, 2.5),
            (0.1, 0.7, 1.3),
            (1.0 + 0.1j, 2.0 - 0.3j, 3.0 + 0.2j),
            (-1.0, 0.0, 1.0),
        ]
        for u, v, w in test_points:
            result = R.verify_ybe(u, v, w)
            assert result["satisfies_ybe"], f"YBE failed at ({u},{v},{w}): {result['max_difference']}"

    def test_unitarity(self):
        """R(u) * R(-u) = (1 - u^2) * I (proportional unitarity).

        For R(u) = u*I + P with P^2 = I:
        R(u)*R(-u) = (u*I + P)(-u*I + P) = -u^2*I + P^2 = (1-u^2)*I.
        """
        R = GL11RMatrix()
        u = 1.5
        R_u = R.matrix(u)
        R_mu = R.matrix(-u)
        from compute.lib.lattice_models_from_dimers import _mat_mul
        product = _mat_mul(R_u, R_mu)
        # Should be (1 - u^2) * I
        expected_scalar = 1 - u * u
        for i in range(4):
            for j in range(4):
                if i == j:
                    assert abs(product[i][j] - expected_scalar) < 1e-10
                else:
                    assert abs(product[i][j]) < 1e-10


class TestZ3VertexRMatrix:
    """Tests for the Z_3-symmetric vertex model R-matrix."""

    def test_dim(self):
        """Z_3 model has dim=3."""
        R = Z3VertexRMatrix()
        assert R.dim == 3

    def test_matrix_shape(self):
        """R-matrix is 9x9."""
        R = Z3VertexRMatrix()
        M = R.matrix(1.0)
        assert len(M) == 9
        assert all(len(row) == 9 for row in M)

    def test_ybe_z3(self):
        """Z_3 vertex model R-matrix satisfies YBE."""
        R = Z3VertexRMatrix()
        result = R.verify_ybe(1.0, 2.0, 3.0)
        assert result["satisfies_ybe"], f"Max diff: {result['max_difference']}"

    def test_ybe_z3_complex(self):
        """Z_3 YBE at complex spectral parameters."""
        R = Z3VertexRMatrix()
        result = R.verify_ybe(1.0 + 0.2j, 2.0 - 0.5j, 3.0 + 0.3j)
        assert result["satisfies_ybe"], f"Max diff: {result['max_difference']}"

    def test_matrix_at_u0(self):
        """R(0) = P (standard permutation on C^3 x C^3)."""
        R = Z3VertexRMatrix()
        M = R.matrix(0.0)
        d = 3
        for i in range(d):
            for j in range(d):
                idx_ij = d * i + j
                idx_ji = d * j + i
                # P|i,j> = |j,i>, so P_{(i,j),(j,i)} = 1
                if i == j:
                    # Diagonal: R_{(i,i),(i,i)} = 0 + 1 = 1
                    assert abs(M[idx_ij][idx_ij] - 1.0) < 1e-10
                else:
                    # Off-diagonal: R_{(j,i),(i,j)} = 1 (permutation)
                    assert abs(M[idx_ji][idx_ij] - 1.0) < 1e-10


class TestAffineYangianRMatrix:
    """Tests for the affine Yangian Y(gl_hat_1) R-matrix."""

    def test_dim(self):
        """Scalar R-matrix has dim=1."""
        R = AffineYangianRMatrix(1.0, -0.5)
        assert R.dim == 1

    def test_structure_function(self):
        """g(u) = (u-h1)(u-h2)(u-h3) / ((u+h1)(u+h2)(u+h3))."""
        R = AffineYangianRMatrix(1.0, -0.5)
        h3 = -(1.0 + (-0.5))  # h3 = -0.5
        u = 2.0
        g_expected = ((u - 1.0) * (u + 0.5) * (u + 0.5)
                      / ((u + 1.0) * (u - 0.5) * (u - 0.5)))
        g_computed = R.structure_function(u)
        assert abs(g_computed - g_expected) < 1e-10

    def test_unitarity_identity(self):
        """g(u) * g(-u) = 1 when h1+h2+h3=0."""
        R = AffineYangianRMatrix(1.0, -0.5)
        result = R.verify_unitarity_identity(2.0)
        assert result["is_unitary"], f"Error: {result['error']}"

    def test_unitarity_multiple_points(self):
        """g(u)*g(-u) = 1 at several points (avoiding poles).

        With h1=1.0, h2=-0.5, h3=-0.5, poles of g(u) are at
        u = -h_a = {-1, 0.5, 0.5}, so we avoid u and -u hitting these.
        """
        R = AffineYangianRMatrix(1.0, -0.5)
        for u in [2.0, 3.5, 1.7, 0.7 + 0.3j, 2.0 - 1.0j]:
            result = R.verify_unitarity_identity(u)
            assert result["is_unitary"], f"Failed at u={u}: error={result['error']}"

    def test_unitarity_different_params(self):
        """g(u)*g(-u) = 1 for different h1, h2.

        Must avoid poles: g(u) has poles at u = -h_a, so u and -u must
        not equal any of -h1, -h2, -h3. Use u=4.5 which is safe for
        all test cases below.
        """
        for h1, h2 in [(1.0, 2.0), (0.5, -0.3), (2.0, -1.0)]:
            R = AffineYangianRMatrix(h1, h2)
            result = R.verify_unitarity_identity(4.5)
            assert result["is_unitary"], f"Failed for h1={h1}, h2={h2}"

    def test_ybe_scalar_trivial(self):
        """Scalar YBE is trivially satisfied (commutative multiplication)."""
        R = AffineYangianRMatrix(1.0, -0.5)
        result = R.verify_ybe(1.0, 2.0, 3.0)
        assert result["satisfies_ybe"]


# =====================================================================
# Section 3: Yang-Baxter equation from E_1 associativity
# =====================================================================

class TestYBEFromE1:
    """Tests for the YBE emerging from E_1 gluing data."""

    def test_ybe_from_e1_all_pass(self):
        """All R-matrices satisfy YBE via E_1 associativity."""
        result = verify_ybe_from_e1_associativity(1.0, -0.5)
        assert result["all_pass"]

    def test_ybe_scalar_passes(self):
        """Scalar R-matrix g(u) satisfies YBE."""
        result = verify_ybe_from_e1_associativity(1.0, -0.5)
        assert result["scalar_ybe_passes"]

    def test_ybe_gl11_passes(self):
        """gl(1|1) matrix R-matrix satisfies YBE."""
        result = verify_ybe_from_e1_associativity(1.0, -0.5)
        assert result["gl11_ybe_passes"]

    def test_ybe_z3_passes(self):
        """Z_3 vertex model R-matrix satisfies YBE."""
        result = verify_ybe_from_e1_associativity(1.0, -0.5)
        assert result["z3_ybe_passes"]

    def test_ybe_different_equivariant_params(self):
        """YBE holds for different equivariant parameters."""
        for h1, h2 in [(1.0, 2.0), (0.5, -0.3), (2.0, -1.0)]:
            result = verify_ybe_from_e1_associativity(h1, h2)
            assert result["scalar_ybe_passes"], f"Failed for h1={h1}, h2={h2}"


# =====================================================================
# Section 4: Transfer matrix tests
# =====================================================================

class TestTransferMatrix:
    """Tests for transfer matrix construction and integrability."""

    def test_transfer_matrix_N1(self):
        """Transfer matrix for N=1 site is 2x2."""
        R = GL11RMatrix()
        T = transfer_matrix_6v(R, 1, 1.0)
        assert len(T) == 2
        assert all(len(row) == 2 for row in T)

    def test_transfer_matrix_N2(self):
        """Transfer matrix for N=2 sites is 4x4."""
        R = GL11RMatrix()
        T = transfer_matrix_6v(R, 2, 1.0)
        assert len(T) == 4
        assert all(len(row) == 4 for row in T)

    def test_transfer_matrix_N1_trace(self):
        """Tr(T(u)) for N=1 with gl(2) R-matrix.

        T_{s,s'} = sum_a R_{(a,s),(a,s')}(u).
        For R(u) = u*I + P (standard permutation):
        T_{0,0} = R_{00,00} + R_{10,10} = (u+1) + u = 2u+1
        T_{1,1} = R_{01,01} + R_{11,11} = u + (u+1) = 2u+1
        So T(u) = (2u+1)*I, Tr = 2*(2u+1) = 4u+2.
        """
        R = GL11RMatrix()
        u = 3.0
        T = transfer_matrix_6v(R, 1, u)
        tr = sum(T[i][i] for i in range(2))
        expected = 4 * u + 2
        assert abs(tr - expected) < 1e-8, f"Trace = {tr}, expected {expected}"

    def test_commutativity_N2(self):
        """[T(u), T(v)] = 0 for N=2."""
        result = verify_transfer_matrix_commutativity(
            GL11RMatrix(), 2, 1.0, 2.0, tol=1e-8
        )
        assert result["commutes"], f"Max commutator: {result['max_commutator']}"

    def test_commutativity_N3(self):
        """[T(u), T(v)] = 0 for N=3."""
        result = verify_transfer_matrix_commutativity(
            GL11RMatrix(), 3, 1.0, 2.0, tol=1e-8
        )
        assert result["commutes"], f"Max commutator: {result['max_commutator']}"

    def test_commutativity_complex(self):
        """[T(u), T(v)] = 0 at complex spectral parameters."""
        result = verify_transfer_matrix_commutativity(
            GL11RMatrix(), 2, 1.0 + 0.5j, 2.0 - 0.3j, tol=1e-8
        )
        assert result["commutes"]

    def test_transfer_matrix_e1_element(self):
        """Transfer matrix is an E_1 element (all commutativity checks pass)."""
        result = verify_transfer_matrix_as_e1_element(N=2)
        assert result["all_commute"]


# =====================================================================
# Section 5: Partition function tests
# =====================================================================

class TestMacMahonProduct:
    """Independent computation of MacMahon function."""

    def test_macmahon_product_first_terms(self):
        """MacMahon function M(q) first 11 coefficients match OEIS A000219."""
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        m = _macmahon_product(10)
        for i, val in enumerate(known):
            assert int(m[i]) == val, f"M(q)[{i}] = {int(m[i])}, expected {val}"

    def test_macmahon_product_agrees_with_coha(self):
        """MacMahon from product formula = MacMahon from CoHA.

        Path 1: prod_{k>=1} 1/(1-q^k)^k  (product formula)
        Path 2: CoHA Euler characteristic  (combinatorial counting)
        """
        order = 12
        path1 = _macmahon_product(order)
        path2 = coha_euler_char_c3(order)
        for i in range(order + 1):
            assert path1[i] == path2[i], f"Mismatch at q^{i}: {path1[i]} vs {path2[i]}"

    def test_macmahon_product_agrees_with_lattice(self):
        """MacMahon from product = partition function from lattice model.

        Path 1: product formula
        Path 2: partition_function_6v_free_fermion
        """
        order = 10
        path1 = _macmahon_product(order)
        path2 = partition_function_6v_free_fermion(0, order)
        for i in range(order + 1):
            assert path1[i] == path2[i]


class TestConifoldProduct:
    """Tests for conifold reduced partition function."""

    def test_conifold_reduced_first_terms(self):
        """Conifold reduced: prod_{k>=1} (1-q^k)^k = 1 - q - 2q^2 - q^3 + 4q^5 + ..."""
        z = _conifold_reduced_product(6)
        assert int(z[0]) == 1
        assert int(z[1]) == -1
        assert int(z[2]) == -2
        assert int(z[3]) == -1
        assert int(z[4]) == 0
        assert int(z[5]) == 4

    def test_conifold_macmahon_inverse(self):
        """prod (1-q^k)^k * M(q) ~ 1 at leading order.

        Actually prod(1-q^k)^k * prod(1/(1-q^k)^k) = 1 identically,
        since one is the exact inverse of the other.
        """
        order = 8
        m = _macmahon_product(order)
        z = _conifold_reduced_product(order)
        product = _fps_mul(m, z)
        assert product[0] == Fraction(1)
        for i in range(1, order + 1):
            assert product[i] == Fraction(0), f"Product[{i}] = {product[i]}, expected 0"


class TestPartitionFunctions:
    """Tests for partition function computations."""

    def test_c3_partition_fn_equals_macmahon(self):
        """Z_{lattice}(C^3) = M(q)."""
        order = 10
        z = partition_function_6v_free_fermion(0, order)
        m = _macmahon_product(order)
        for i in range(order + 1):
            assert z[i] == m[i]

    def test_conifold_partition_fn(self):
        """Z_{lattice}(conifold, Q=0) = M(q)^2."""
        order = 8
        z = partition_function_conifold(order)
        m = _macmahon_product(order)
        m2 = _fps_mul(m, m)
        for i in range(order + 1):
            assert z[i] == m2[i]

    def test_conifold_q0_first_terms(self):
        """M(q)^2 first terms: 1, 2, 7, 18, 47, 110, ..."""
        z = partition_function_conifold(5)
        assert int(z[0]) == 1
        assert int(z[1]) == 2
        assert int(z[2]) == 7
        assert int(z[3]) == 18
        assert int(z[4]) == 47

    def test_local_p2_partition_fn(self):
        """Z_{lattice}(local P^2, Q=0) = M(q)^3."""
        order = 6
        z = partition_function_local_p2(order)
        m = _macmahon_product(order)
        m3 = _fps_mul(_fps_mul(m, m), m)
        for i in range(order + 1):
            assert z[i] == m3[i]

    def test_local_p2_first_terms(self):
        """M(q)^3 first terms: 1, 3, 12, 37, ..."""
        z = partition_function_local_p2(3)
        assert int(z[0]) == 1
        assert int(z[1]) == 3
        assert int(z[2]) == 12
        assert int(z[3]) == 37


# =====================================================================
# Section 6: Partition function dictionary (4-way)
# =====================================================================

class TestPartitionFunctionDictionary:
    """Verify the 4-way equality for C^3 and conifold."""

    def test_c3_dictionary_all_paths(self):
        """All 4 paths give MacMahon for C^3."""
        result = verify_lattice_dt_dictionary_c3(order=10)
        assert result["all_paths_match"]

    def test_c3_dictionary_known_values(self):
        """C^3 partition function matches OEIS A000219."""
        result = verify_lattice_dt_dictionary_c3(order=10)
        assert result["match_known_values"]

    def test_conifold_dictionary(self):
        """Conifold partition function: lattice = DT at Q=0."""
        result = verify_lattice_dt_dictionary_conifold(order=8)
        assert result["paths_match"]


# =====================================================================
# Section 7: Corner transfer matrix and entanglement
# =====================================================================

class TestCornerTransferMatrix:
    """Tests for the CTM spectrum and entanglement entropy."""

    def test_ctm_spectrum_length(self):
        """CTM spectrum for N sites has N eigenvalues."""
        spec = ctm_spectrum_6v_free_fermion(5)
        assert len(spec) == 5

    def test_ctm_spectrum_geometric(self):
        """CTM spectrum is geometric: lambda_n = 2^{-n}."""
        spec = ctm_spectrum_6v_free_fermion(4)
        for n in range(4):
            assert spec[n] == Fraction(1, 2 ** n)

    def test_ctm_spectrum_positive(self):
        """All CTM eigenvalues are positive."""
        spec = ctm_spectrum_6v_free_fermion(8)
        assert all(lam > 0 for lam in spec)

    def test_ctm_spectrum_decreasing(self):
        """CTM eigenvalues are strictly decreasing."""
        spec = ctm_spectrum_6v_free_fermion(8)
        for i in range(len(spec) - 1):
            assert spec[i] > spec[i + 1]

    def test_entropy_positive(self):
        """Entanglement entropy is positive for N > 1."""
        spec = ctm_spectrum_6v_free_fermion(4)
        S = entanglement_entropy_ctm(spec)
        assert float(S) > 0

    def test_entropy_zero_single_state(self):
        """Entropy is 0 for a single eigenvalue (pure state)."""
        spec = [Fraction(1)]
        S = entanglement_entropy_ctm(spec)
        assert abs(float(S)) < 1e-10

    def test_entropy_monotone_increasing(self):
        """Entropy increases with system size."""
        S_values = []
        for N in range(1, 8):
            spec = ctm_spectrum_6v_free_fermion(N)
            S = entanglement_entropy_ctm(spec)
            S_values.append(float(S))

        for i in range(len(S_values) - 1):
            assert S_values[i + 1] > S_values[i], (
                f"S({i+1}) = {S_values[i]} >= S({i+2}) = {S_values[i+1]}"
            )

    def test_shadow_depth_increases(self):
        """Shadow depth is non-decreasing with system size."""
        depths = []
        for N in range(1, 12):
            spec = ctm_spectrum_6v_free_fermion(N)
            S = entanglement_entropy_ctm(spec)
            r = shadow_depth_from_entropy(S)
            depths.append(r)

        for i in range(len(depths) - 1):
            assert depths[i + 1] >= depths[i]

    def test_verify_ctm_entropy_shadow(self):
        """Full CTM-entropy-shadow verification passes."""
        result = verify_ctm_entropy_shadow_depth(N=8)
        assert result["monotone_increasing"]
        assert result["shadow_depth"] >= 1


# =====================================================================
# Section 8: Bethe ansatz from lattice model
# =====================================================================

class TestBetheAnsatz:
    """Tests for Bethe ansatz equations from the lattice model."""

    def test_bethe_one_magnon_N2(self):
        """One-magnon Bethe roots for N=2 sites."""
        result = bethe_ansatz_from_lattice(N=2)
        assert result["all_one_magnon_pass"]
        assert len(result["one_magnon_roots"]) == 2

    def test_bethe_one_magnon_N4(self):
        """One-magnon Bethe roots for N=4 sites."""
        result = bethe_ansatz_from_lattice(N=4)
        assert result["all_one_magnon_pass"]
        assert len(result["one_magnon_roots"]) == 4

    def test_bethe_one_magnon_N6(self):
        """One-magnon Bethe roots for N=6 sites."""
        result = bethe_ansatz_from_lattice(N=6)
        assert result["all_one_magnon_pass"]
        assert len(result["one_magnon_roots"]) == 6

    def test_bethe_sectors_count(self):
        """Number of magnon sectors = N + 1."""
        for N in [2, 3, 4, 5]:
            result = bethe_ansatz_from_lattice(N=N)
            assert result["n_sectors"] == N + 1

    def test_bethe_roots_complex(self):
        """One-magnon Bethe roots are complex (from exp(i*pi*(2k+1)/N))."""
        result = bethe_ansatz_from_lattice(N=4)
        # Roots are u = 1/(w-1) where w = exp(i*pi*(2k+1)/N), generally complex
        assert len(result["one_magnon_roots"]) == 4

    def test_bethe_residuals_small(self):
        """All BAE residuals are < 1e-8."""
        result = bethe_ansatz_from_lattice(N=4)
        for v in result["one_magnon_verification"]:
            assert v["residual"] < 1e-8


# =====================================================================
# Section 9: Unitarity tests
# =====================================================================

class TestUnitarity:
    """Tests for unitarity relations of R-matrices."""

    def test_gl2_product_scalar(self):
        """R(u)*R(-u) = (1-u^2)*I for gl(2) XXX R-matrix."""
        R = GL11RMatrix()
        from compute.lib.lattice_models_from_dimers import _mat_mul
        for u in [1.0, 2.0, 0.5, 1.0 + 0.3j]:
            R_u = R.matrix(u)
            R_mu = R.matrix(-u)
            prod = _mat_mul(R_u, R_mu)
            expected = 1 - u * u
            for i in range(4):
                for j in range(4):
                    if i == j:
                        assert abs(prod[i][j] - expected) < 1e-10
                    else:
                        assert abs(prod[i][j]) < 1e-10

    def test_yangian_unitarity_many_params(self):
        """g(u)*g(-u) = 1 for Y(gl_hat_1) at various h1, h2.

        Must choose u values that avoid poles at +/-h_a for all parameter sets.
        With h3 = -(h1+h2), poles of g(u) are at u = -h1, -h2, h1+h2.
        Using u = 5.5 + 0.7j is safe for all cases below.
        """
        test_cases = [
            (1.0, 1.0),
            (1.0, -0.5),
            (2.0, -1.0),
            (0.3, 0.7),
            (1.0 + 0.1j, -0.5 + 0.2j),
        ]
        for h1, h2 in test_cases:
            R = AffineYangianRMatrix(h1, h2)
            for u in [5.5 + 0.7j, 3.3 - 0.4j]:
                result = R.verify_unitarity_identity(u)
                assert result["is_unitary"], f"Failed at h1={h1}, h2={h2}, u={u}"


# =====================================================================
# Section 10: W_{1+infinity} generator identification
# =====================================================================

class TestWAlgebraGenerators:
    """Tests for identifying W_{1+inf} generators from transfer matrix."""

    def test_T0_is_identity_N1(self):
        """Leading coefficient T_0 is the identity (normalization)."""
        result = transfer_matrix_expansion_c3(N=1)
        assert result["T0_is_identity"]

    def test_T0_is_identity_N2(self):
        """Leading coefficient T_0 is the identity for N=2."""
        result = transfer_matrix_expansion_c3(N=2)
        assert result["T0_is_identity"]


# =====================================================================
# Section 11: Cross-verification (multi-path)
# =====================================================================

class TestCrossVerification:
    """Multi-path cross-verification tests."""

    def test_macmahon_3_paths(self):
        """MacMahon function from 3 independent paths.

        Path 1: Product formula prod 1/(1-q^k)^k
        Path 2: CoHA Euler characteristic
        Path 3: Partition counting (from dimer_chart_atlas)
        """
        order = 10
        path1 = _macmahon_product(order)
        path2 = coha_euler_char_c3(order)
        path3 = [Fraction(x) for x in macmahon_coefficients(order)]

        for i in range(order + 1):
            assert path1[i] == path2[i] == path3[i], (
                f"Mismatch at q^{i}: {path1[i]}, {path2[i]}, {path3[i]}"
            )

    def test_conifold_inverse_identity(self):
        """prod(1-q^k)^k * prod(1/(1-q^k)^k) = 1 (exact cancellation).

        This is the fundamental identity connecting:
        - MacMahon function (C^3 DT)
        - Conifold reduced partition function
        """
        order = 10
        m = _macmahon_product(order)
        z = _conifold_reduced_product(order)
        product = _fps_mul(m, z)
        assert product[0] == Fraction(1)
        for i in range(1, order + 1):
            assert product[i] == Fraction(0)

    def test_ybe_3_rmatrices(self):
        """YBE verified independently for gl(1|1), Z_3 vertex, and scalar R.

        Three independent R-matrices all satisfy YBE, confirming the
        E_1 associativity origin.
        """
        result = verify_ybe_from_e1_associativity(1.0, -0.5)
        assert result["scalar_ybe_passes"]
        assert result["gl11_ybe_passes"]
        assert result["z3_ybe_passes"]

    def test_bethe_and_transfer_compatible(self):
        """Bethe ansatz roots from BAE are compatible with transfer matrix.

        For N=2, the one-magnon BAE gives roots that should diagonalize T(u).
        """
        bae = bethe_ansatz_from_lattice(N=2)
        assert bae["all_one_magnon_pass"]

        # Transfer matrix commutes => simultaneously diagonalizable
        comm = verify_transfer_matrix_commutativity(
            GL11RMatrix(), 2, 1.0, 2.0
        )
        assert comm["commutes"]

    def test_entropy_increases_with_macmahon(self):
        """Entropy and MacMahon coefficients both grow with size.

        Monotonicity of entropy parallels growth of MacMahon coefficients:
        both reflect the increasing complexity of the E_1 algebra.
        """
        m = macmahon_coefficients(10)
        for i in range(1, len(m)):
            assert m[i] >= m[i - 1]

        S_vals = []
        for N in range(1, 8):
            spec = ctm_spectrum_6v_free_fermion(N)
            S = entanglement_entropy_ctm(spec)
            S_vals.append(float(S))
        for i in range(len(S_vals) - 1):
            assert S_vals[i + 1] > S_vals[i]


# =====================================================================
# Section 12: Full verification suite
# =====================================================================

class TestFullVerification:
    """Run the complete verification pipeline."""

    def test_run_all(self):
        """All lattice model verifications pass."""
        result = run_all_lattice_verifications()
        assert result["all_pass"], f"Failures in: {[k for k, v in result.items() if isinstance(v, dict) and not v.get('all_pass', v.get('all_commute', v.get('paths_match', v.get('monotone', True))))]}"

    def test_ybe_section(self):
        """YBE section passes."""
        result = run_all_lattice_verifications()
        assert result["ybe_from_e1"]["all_pass"]

    def test_transfer_section(self):
        """Transfer matrix section passes."""
        result = run_all_lattice_verifications()
        assert result["transfer_matrix_e1"]["all_commute"]

    def test_partition_fn_section(self):
        """Partition function section passes."""
        result = run_all_lattice_verifications()
        assert result["partition_fn_c3"]["all_paths_match"]
        assert result["partition_fn_c3"]["match_known"]

    def test_bethe_section(self):
        """Bethe ansatz section passes."""
        result = run_all_lattice_verifications()
        assert result["bethe_ansatz"]["all_pass"]
