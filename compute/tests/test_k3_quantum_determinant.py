r"""Tests for the K3 quantum determinant engine.

Verifies:
1. Weyl shift computation from Mukai pairing eigenvalues
2. Quantum determinant zeros: u_i = rho_i + h_i
3. qdet is degree 24 with leading coefficient 1
4. qdet vanishes at its claimed zeros
5. Centrality (automatic for diagonal Lax)
6. Signature decomposition: qdet = qdet^+ * qdet^-
7. Polynomial coefficient analysis
8. sigma_1 deformation invariance
9. Serre null vector structure
10. Comparison: definite vs indefinite Mukai pairing
11. Comparison: sl_2 vs K3 qdet
12. BKM root connection (conjectural)
13. Full verification suite

STATUS: CONJECTURAL (AP-CY14). All results conditional on Y(g_{K3}).

AP-CY28 compliance: test points use values far from poles/zeros.
"""

from fractions import Fraction

from sympy import Rational, Symbol, Poly

from compute.lib.k3_quantum_determinant import (
    RANK,
    QDetData,
    SerreNullVector,
    WeylShiftData,
    definite_vs_indefinite_comparison,
    full_verification,
    qdet_bkm_connection,
    qdet_deformation_invariants,
    qdet_polynomial_coefficients,
    qdet_signature_decomposition,
    quantum_determinant_centrality,
    quantum_determinant_evaluate,
    quantum_determinant_symbolic,
    quantum_determinant_zeros,
    serre_ideal_structure,
    serre_null_vectors,
    sl2_vs_k3_qdet_comparison,
    verify_factorization_consistency,
    verify_qdet_degree,
    verify_qdet_zeros_are_correct,
    verify_sigma1_invariance,
    weyl_shift_profile,
    weyl_shifts_from_mukai,
)
from compute.lib.k3_yangian import (
    SIG_MINUS,
    SIG_PLUS,
    kummer_k3_parameters,
    mukai_diagonal_eigenvalues,
    null_kummer_parameters,
)


# =========================================================================
# 1. WEYL SHIFTS
# =========================================================================

class TestWeylShifts:
    """Tests for the cumulative Weyl shifts from the Mukai pairing."""

    def test_shift_count(self):
        """There should be exactly 24 Weyl shifts."""
        data = weyl_shifts_from_mukai()
        assert len(data.shifts) == RANK

    def test_first_shift_is_zero(self):
        """rho_1 = 0 (no predecessors)."""
        data = weyl_shifts_from_mukai()
        assert data.shifts[0] == 0

    def test_ascending_phase(self):
        """rho_1,...,rho_5 should be 0,1,2,3,4 (4 positive eigenvalues)."""
        data = weyl_shifts_from_mukai()
        assert data.shifts[:5] == [0, 1, 2, 3, 4]

    def test_descending_starts_at_5(self):
        """rho_6 = 3 (first negative eigenvalue subtracts 1)."""
        data = weyl_shifts_from_mukai()
        assert data.shifts[5] == 3  # 4 + (-1) = 3

    def test_max_shift(self):
        """Maximum shift is 4 (after all positive eigenvalues)."""
        data = weyl_shifts_from_mukai()
        assert data.max_shift == 4

    def test_min_shift(self):
        """Minimum shift is -15 (at position 24: 4 - 19 = -15)."""
        data = weyl_shifts_from_mukai()
        assert data.min_shift == -15

    def test_last_shift(self):
        """rho_{24} = 4 + 19*(-1) = 4 - 19 = -15."""
        data = weyl_shifts_from_mukai()
        assert data.shifts[23] == -15

    def test_total_shift(self):
        """Total shift = 4 - 20 = -16 = Tr(omega)."""
        data = weyl_shifts_from_mukai()
        assert data.total_shift == -16

    def test_signature(self):
        """Signature is (4, 20)."""
        data = weyl_shifts_from_mukai()
        assert data.signature == (4, 20)

    def test_cumulative_property(self):
        """rho_{i+1} = rho_i + sigma_i for all i."""
        data = weyl_shifts_from_mukai()
        eigenvalues = mukai_diagonal_eigenvalues()
        for i in range(RANK - 1):
            assert data.shifts[i + 1] == data.shifts[i] + eigenvalues[i]

    def test_shift_profile(self):
        """The profile function returns correct structure."""
        profile = weyl_shift_profile()
        assert profile['turning_point_index'] == SIG_PLUS + 1  # = 5
        assert profile['max_rho'] == 4
        assert profile['min_rho'] == -15
        assert profile['range'] == 19  # 4 - (-15)
        assert profile['total_shift'] == -16


# =========================================================================
# 2. QUANTUM DETERMINANT ZEROS
# =========================================================================

class TestQDetZeros:
    """Tests for the zeros u_i = rho_i + h_i of qdet L(u)."""

    def test_num_zeros(self):
        """qdet has exactly 24 zeros."""
        data = quantum_determinant_zeros()
        assert data.degree == 24
        assert len(data.zeros) == 24

    def test_zeros_formula(self):
        """Each zero is u_i = rho_i + h_i."""
        params = kummer_k3_parameters()
        data = quantum_determinant_zeros(params)
        weyl = weyl_shifts_from_mukai()
        for i in range(RANK):
            expected = Rational(weyl.shifts[i]) + params.h[i]
            assert data.zeros[i] == expected, (
                f"Zero {i+1}: got {data.zeros[i]}, expected {expected}"
            )

    def test_positive_sector_zeros_kummer(self):
        """For Kummer params (h=eps=1 for positive), u_i = i-1 + 1 = i."""
        params = kummer_k3_parameters(epsilon=Rational(1))
        data = quantum_determinant_zeros(params)
        # Positive sector: rho = [0,1,2,3], h = [1,1,1,1]
        # zeros = [1, 2, 3, 4]
        assert data.zeros[0] == Rational(1)
        assert data.zeros[1] == Rational(2)
        assert data.zeros[2] == Rational(3)
        assert data.zeros[3] == Rational(4)

    def test_negative_sector_first_zero_kummer(self):
        """For Kummer params, u_5 = 4 + (-1/5) = 19/5."""
        params = kummer_k3_parameters(epsilon=Rational(1))
        data = quantum_determinant_zeros(params)
        assert data.zeros[4] == Rational(19, 5)  # 4 + (-1/5) = 19/5

    def test_null_params_zeros_differ(self):
        """Null parameters give different zeros (but same sigma_1)."""
        params_kummer = kummer_k3_parameters()
        params_null = null_kummer_parameters()
        data_kummer = quantum_determinant_zeros(params_kummer)
        data_null = quantum_determinant_zeros(params_null)
        # Zeros differ
        assert data_kummer.zeros != data_null.zeros
        # But sigma_1 is the same
        assert sum(data_kummer.zeros) == sum(data_null.zeros)

    def test_signature_in_data(self):
        """QDetData records signature (4, 20)."""
        data = quantum_determinant_zeros()
        assert data.signature == (4, 20)


# =========================================================================
# 3. QDET DEGREE AND POLYNOMIAL STRUCTURE
# =========================================================================

class TestQDetPolynomial:
    """Tests for qdet as a degree-24 polynomial."""

    def test_degree_is_24(self):
        """qdet(u) has degree 24."""
        result = verify_qdet_degree()
        assert result['is_degree_24']

    def test_leading_coefficient_is_1(self):
        """Leading coefficient is 1 (monic polynomial)."""
        result = verify_qdet_degree()
        assert result['leading_is_1']

    def test_qdet_vanishes_at_zeros(self):
        """qdet(u_i) = 0 for each claimed zero."""
        result = verify_qdet_zeros_are_correct()
        assert result['all_zeros_verified']

    def test_qdet_nonzero_away_from_zeros(self):
        """qdet is nonzero at a generic point far from zeros (AP-CY28)."""
        val = quantum_determinant_evaluate(Rational(1000))
        assert val != 0

    def test_qdet_evaluate_matches_symbolic(self):
        """Numerical evaluation matches symbolic at test point."""
        u_test = Rational(37)
        numerical = quantum_determinant_evaluate(u_test)
        u = Symbol("u")
        symbolic = quantum_determinant_symbolic()
        symbolic_val = symbolic.subs(u, u_test)
        assert numerical == symbolic_val


# =========================================================================
# 4. CENTRALITY
# =========================================================================

class TestCentrality:
    """Tests for centrality of qdet."""

    def test_centrality_report(self):
        """Centrality analysis returns correct structure."""
        result = quantum_determinant_centrality()
        assert result['is_degree_24']
        assert result['leading_is_1']

    def test_centrality_is_automatic(self):
        """For diagonal Lax (abelian gl_1), centrality is automatic."""
        result = quantum_determinant_centrality()
        assert 'AUTOMATIC' in result['centrality']


# =========================================================================
# 5. SIGNATURE DECOMPOSITION
# =========================================================================

class TestSignatureDecomposition:
    """Tests for qdet = qdet^+ * qdet^-."""

    def test_positive_sector_degree(self):
        """Positive sector has degree 4."""
        result = qdet_signature_decomposition()
        assert result['positive_sector']['degree'] == SIG_PLUS

    def test_negative_sector_degree(self):
        """Negative sector has degree 20."""
        result = qdet_signature_decomposition()
        assert result['negative_sector']['degree'] == SIG_MINUS

    def test_factorization_check(self):
        """qdet^+ * qdet^- = qdet at test point."""
        result = qdet_signature_decomposition()
        assert result['factorization_check']['match']

    def test_factorization_consistency_multiple_points(self):
        """qdet = qdet^+ * qdet^- at multiple test points."""
        result = verify_factorization_consistency()
        assert result['all_match']


# =========================================================================
# 6. SIGMA_1 INVARIANCE
# =========================================================================

class TestSigma1Invariance:
    """Tests for the deformation invariance of sigma_1."""

    def test_sigma1_invariant(self):
        """sigma_1 = sum rho_i is the same for all CY_2-satisfying params."""
        result = verify_sigma1_invariance()
        assert result['all_equal']

    def test_sigma1_equals_sum_rho(self):
        """sigma_1 = sum rho_i (since sum h_i = 0)."""
        params = kummer_k3_parameters()
        qdet_data = quantum_determinant_zeros(params)
        sigma1 = sum(qdet_data.zeros)
        sum_rho = sum(qdet_data.weyl_shifts)
        assert sigma1 == sum_rho

    def test_sigma1_value(self):
        """sigma_1 = 0+1+2+3+4+3+2+1+0+(-1)+...+(-15)."""
        weyl_data = weyl_shifts_from_mukai()
        sum_rho = sum(weyl_data.shifts)
        # Compute expected: sum_{k=0}^{3} k + sum_{k=-15}^{3} k (for neg sector)
        # But easier: ascending [0,1,2,3,4] + descending [3,2,1,0,-1,...,-15]
        expected = sum(range(5)) + sum(range(-15, 4))
        # range(5) = 0+1+2+3+4 = 10
        # range(-15, 4) = -15+-14+...+3 = 19 terms
        assert sum_rho == expected


# =========================================================================
# 7. SERRE NULL VECTORS
# =========================================================================

class TestSerreNullVectors:
    """Tests for Serre null vectors from qdet zeros."""

    def test_num_null_vectors(self):
        """There are 24 null vectors (one per qdet zero)."""
        vectors = serre_null_vectors()
        assert len(vectors) == RANK

    def test_positive_sector_count(self):
        """4 null vectors from the positive Mukai sector."""
        vectors = serre_null_vectors()
        pos = [v for v in vectors if v.sector == 'positive']
        assert len(pos) == SIG_PLUS

    def test_negative_sector_count(self):
        """20 null vectors from the negative Mukai sector."""
        vectors = serre_null_vectors()
        neg = [v for v in vectors if v.sector == 'negative']
        assert len(neg) == SIG_MINUS

    def test_null_vector_formula(self):
        """Each null vector has u_k = rho_k + h_k."""
        params = kummer_k3_parameters()
        vectors = serre_null_vectors(params)
        weyl = weyl_shifts_from_mukai()
        for v in vectors:
            expected = Rational(weyl.shifts[v.index - 1]) + params.h[v.index - 1]
            assert v.zero_u == expected

    def test_mukai_eigenvalues(self):
        """Null vectors in positive sector have eigenvalue +1, negative -1."""
        vectors = serre_null_vectors()
        for v in vectors:
            if v.sector == 'positive':
                assert v.mukai_eigenvalue == 1
            else:
                assert v.mukai_eigenvalue == -1


# =========================================================================
# 8. SERRE IDEAL STRUCTURE
# =========================================================================

class TestSerreIdealStructure:
    """Tests for the structure of the Serre ideal."""

    def test_num_zeros(self):
        """24 zeros in the Serre ideal."""
        result = serre_ideal_structure()
        assert result['num_zeros'] == RANK

    def test_no_degeneracies_kummer(self):
        """Kummer parametrization gives no degenerate zeros."""
        result = serre_ideal_structure()
        assert not result['has_degeneracies']

    def test_positive_sector_info(self):
        """Positive sector has 4 zeros."""
        result = serre_ideal_structure()
        assert result['positive_sector']['num_zeros'] == SIG_PLUS

    def test_negative_sector_info(self):
        """Negative sector has 20 zeros."""
        result = serre_ideal_structure()
        assert result['negative_sector']['num_zeros'] == SIG_MINUS

    def test_sorted_zeros_ascending(self):
        """Sorted zeros are in ascending order."""
        result = serre_ideal_structure()
        sorted_z = [Rational(z) for z in result['sorted_zeros']]
        for i in range(len(sorted_z) - 1):
            assert sorted_z[i] <= sorted_z[i + 1]


# =========================================================================
# 9. POLYNOMIAL COEFFICIENTS
# =========================================================================

class TestPolynomialCoefficients:
    """Tests for the polynomial coefficients of qdet."""

    def test_sigma_1_equals_sum_rho(self):
        """sigma_1 = sum rho_i (since sum h_i = 0 by CY_2)."""
        result = qdet_polynomial_coefficients()
        assert result['sigma_1_decomposition']['sum_h_is_zero']
        assert result['sigma_1_decomposition']['sigma_1_equals_sum_rho']

    def test_degree(self):
        """Polynomial degree is 24."""
        result = qdet_polynomial_coefficients()
        assert result['degree'] == RANK


# =========================================================================
# 10. DEFINITE VS INDEFINITE COMPARISON
# =========================================================================

class TestDefiniteVsIndefinite:
    """Tests comparing definite and indefinite Mukai pairing."""

    def test_definite_is_monotonic(self):
        """Positive-definite pairing gives monotonic Weyl shifts."""
        result = definite_vs_indefinite_comparison()
        assert result['definite']['monotonic']

    def test_indefinite_is_non_monotonic(self):
        """Indefinite Mukai pairing gives non-monotonic shifts."""
        result = definite_vs_indefinite_comparison()
        assert not result['indefinite']['monotonic']

    def test_definite_max_shift(self):
        """Definite: max shift = 23."""
        result = definite_vs_indefinite_comparison()
        assert result['definite']['max_shift'] == RANK - 1  # = 23

    def test_indefinite_max_shift(self):
        """Indefinite: max shift = 4 (much less than 23)."""
        result = definite_vs_indefinite_comparison()
        assert result['indefinite']['max_shift'] == SIG_PLUS  # = 4

    def test_definite_min_shift(self):
        """Definite: min shift = 0."""
        result = definite_vs_indefinite_comparison()
        assert result['definite']['min_shift'] == 0

    def test_indefinite_min_shift(self):
        """Indefinite: min shift = -15 (negative!)."""
        result = definite_vs_indefinite_comparison()
        assert result['indefinite']['min_shift'] == -15

    def test_definite_sum_rho(self):
        """Definite: sum rho = 0+1+...+23 = 276."""
        result = definite_vs_indefinite_comparison()
        assert result['definite']['sum_rho'] == 276


# =========================================================================
# 11. SL_2 VS K3 COMPARISON
# =========================================================================

class TestSl2VsK3:
    """Tests for the sl_2 vs K3 qdet comparison."""

    def test_sl2_rank(self):
        """sl_2 has rank 2."""
        result = sl2_vs_k3_qdet_comparison()
        assert result['sl2']['rank'] == 2

    def test_k3_rank(self):
        """K3 has rank 24."""
        result = sl2_vs_k3_qdet_comparison()
        assert result['k3_gl1']['rank'] == RANK

    def test_sl2_not_diagonal(self):
        """sl_2 Lax is non-diagonal."""
        result = sl2_vs_k3_qdet_comparison()
        assert not result['sl2']['is_diagonal']

    def test_k3_is_diagonal(self):
        """K3 gl_1 Lax is diagonal."""
        result = sl2_vs_k3_qdet_comparison()
        assert result['k3_gl1']['is_diagonal']

    def test_sl2_weyl_shifts(self):
        """sl_2 Weyl shifts are [0, 1]."""
        result = sl2_vs_k3_qdet_comparison()
        assert result['sl2']['weyl_shifts'] == [0, 1]


# =========================================================================
# 12. BKM CONNECTION
# =========================================================================

class TestBKMConnection:
    """Tests for the BKM root structure connection (conjectural)."""

    def test_bkm_report_exists(self):
        """BKM connection report is generated."""
        result = qdet_bkm_connection()
        assert result['num_qdet_zeros'] == RANK

    def test_kappa_connection(self):
        """kappa_fiber = 24 = degree of qdet."""
        result = qdet_bkm_connection()
        assert 'kappa_fiber = 24' in result['kappa_connection']


# =========================================================================
# 13. DEFORMATION INVARIANTS
# =========================================================================

class TestDeformationInvariants:
    """Tests for deformation-invariant quantities."""

    def test_sigma1_invariant_across_params(self):
        """sigma_1 is the same for Kummer and null parameters."""
        result = qdet_deformation_invariants()
        assert result['sigma_1_invariant']

    def test_weyl_shifts_invariant(self):
        """Weyl shifts are independent of h_i."""
        result = qdet_deformation_invariants()
        assert result['weyl_shifts_invariant']


# =========================================================================
# 14. FULL VERIFICATION
# =========================================================================

class TestFullVerification:
    """Tests for the complete verification suite."""

    def test_full_suite_runs(self):
        """Full verification suite completes without error."""
        result = full_verification()
        assert result['status'] == 'CONJECTURAL'

    def test_all_zeros_verified(self):
        """All qdet zeros are verified in the full suite."""
        result = full_verification()
        assert result['path2_qdet_zeros']['zeros_verified']['all_zeros_verified']

    def test_degree_verified(self):
        """Degree 24 is verified in the full suite."""
        result = full_verification()
        assert result['path3_qdet_degree']['is_degree_24']

    def test_sigma1_invariance_verified(self):
        """sigma_1 invariance is verified in the full suite."""
        result = full_verification()
        assert result['path8_sigma1_invariance']['all_equal']

    def test_factorization_verified(self):
        """Factorization consistency is verified in the full suite."""
        result = full_verification()
        assert result['path9_factorization']['all_match']


# =========================================================================
# 15. MULTI-PATH CROSS-VERIFICATION
# =========================================================================

class TestMultiPathCrossVerification:
    """Multi-path cross-checks: verify the same quantity via independent routes.

    Each test computes one result via at least two independent methods and
    asserts they agree.  This catches confabulation of ground-truth values
    (AP-CY24) and formula transcription errors.
    """

    def test_sigma1_three_paths(self):
        """sigma_1 via (a) qdet zeros, (b) direct Weyl sum, (c) polynomial coeff.

        Path A: sum of zeros u_i from quantum_determinant_zeros.
        Path B: sum of rho_i from weyl_shifts_from_mukai (plus CY_2 sum h=0).
        Path C: sigma_1 coefficient extracted from qdet_polynomial_coefficients.
        """
        params = kummer_k3_parameters()

        # Path A: sum of zeros
        qdet_data = quantum_determinant_zeros(params)
        sigma1_A = sum(qdet_data.zeros)

        # Path B: sum of Weyl shifts (sum h_i = 0 by CY_2)
        weyl_data = weyl_shifts_from_mukai()
        sigma1_B = Rational(sum(weyl_data.shifts))

        # Path C: from polynomial coefficients
        poly_data = qdet_polynomial_coefficients(params)
        sigma1_C = Rational(poly_data['sigma_1_decomposition']['sigma_1'])

        assert sigma1_A == sigma1_B, f"Path A ({sigma1_A}) != Path B ({sigma1_B})"
        assert sigma1_B == sigma1_C, f"Path B ({sigma1_B}) != Path C ({sigma1_C})"

    def test_qdet_evaluation_two_paths(self):
        """qdet(u) at test point via (a) product formula, (b) symbolic polynomial.

        Path A: quantum_determinant_evaluate (product of linear factors).
        Path B: quantum_determinant_symbolic evaluated at the same point.
        """
        params = kummer_k3_parameters()
        u_test = Rational(137)  # large prime, far from all zeros (AP-CY28)

        # Path A: product formula
        val_A = quantum_determinant_evaluate(u_test, params)

        # Path B: symbolic polynomial
        u = Symbol("u")
        poly = quantum_determinant_symbolic(params)
        val_B = poly.subs(u, u_test)

        assert val_A == val_B, f"Product ({val_A}) != Symbolic ({val_B})"

    def test_qdet_evaluation_negative_point(self):
        """Same as above at a negative test point."""
        params = kummer_k3_parameters()
        u_test = Rational(-89)

        val_A = quantum_determinant_evaluate(u_test, params)
        u = Symbol("u")
        poly = quantum_determinant_symbolic(params)
        val_B = poly.subs(u, u_test)

        assert val_A == val_B

    def test_factorization_cross_path(self):
        """qdet = qdet^+ * qdet^- cross-checked against direct evaluation.

        Path A: qdet_signature_decomposition (separate pos/neg products).
        Path B: quantum_determinant_evaluate (single full product).
        """
        params = kummer_k3_parameters()
        qdet_data = quantum_determinant_zeros(params)
        zeros = qdet_data.zeros
        pos_zeros = zeros[:SIG_PLUS]
        neg_zeros = zeros[SIG_PLUS:]

        for u_val in [Rational(200), Rational(-73), Rational(41, 3)]:
            # Path A: separate sector products
            qdet_pos = Rational(1)
            for ui in pos_zeros:
                qdet_pos *= (u_val - ui)
            qdet_neg = Rational(1)
            for ui in neg_zeros:
                qdet_neg *= (u_val - ui)
            val_A = qdet_pos * qdet_neg

            # Path B: full product
            val_B = quantum_determinant_evaluate(u_val, params)

            assert val_A == val_B, (
                f"Factorization mismatch at u={u_val}: {val_A} != {val_B}"
            )

    def test_degree_cross_path(self):
        """Degree of qdet via (a) verify_qdet_degree, (b) counting zeros.

        Path A: Poly.degree() on the symbolic polynomial.
        Path B: len(quantum_determinant_zeros().zeros).
        """
        # Path A
        result_A = verify_qdet_degree()
        degree_A = result_A['degree']

        # Path B
        data_B = quantum_determinant_zeros()
        degree_B = len(data_B.zeros)

        assert degree_A == degree_B == RANK

    def test_weyl_shift_sum_two_paths(self):
        """sum rho_i via (a) cumulative shift list, (b) direct formula.

        Path A: sum(weyl_shifts_from_mukai().shifts)
        Path B: sum_{i=0}^{23} sum_{j=0}^{i-1} sigma_j
               = sum_{j=0}^{22} sigma_j * (23 - j)
               (each sigma_j is counted (23-j) times in the cumulative sums)
        """
        eigenvalues = mukai_diagonal_eigenvalues()

        # Path A
        weyl_data = weyl_shifts_from_mukai()
        sum_A = sum(weyl_data.shifts)

        # Path B: direct formula
        # rho_i = sum_{j<i} sigma_j, so sum_i rho_i = sum_j sigma_j * (N-1-j)
        sum_B = sum(eigenvalues[j] * (RANK - 1 - j) for j in range(RANK))

        assert sum_A == sum_B, f"Path A ({sum_A}) != Path B ({sum_B})"

    def test_null_params_sigma1_cross_check(self):
        """sigma_1 is identical for null and Kummer params (CY_2 invariance).

        Cross-checks the deformation-invariance claim against both
        parameter families independently.
        """
        params_k = kummer_k3_parameters()
        params_n = null_kummer_parameters()

        zeros_k = quantum_determinant_zeros(params_k).zeros
        zeros_n = quantum_determinant_zeros(params_n).zeros

        # sigma_1 from zeros
        s1_k = sum(zeros_k)
        s1_n = sum(zeros_n)

        # sigma_1 from Weyl shifts
        s1_rho = Rational(sum(weyl_shifts_from_mukai().shifts))

        assert s1_k == s1_rho
        assert s1_n == s1_rho

    def test_serre_vectors_match_qdet_zeros(self):
        """Serre null vectors have the same u-values as qdet zeros.

        Path A: serre_null_vectors()[k].zero_u
        Path B: quantum_determinant_zeros().zeros[k]
        """
        params = kummer_k3_parameters()
        vectors = serre_null_vectors(params)
        qdet_data = quantum_determinant_zeros(params)

        for k in range(RANK):
            assert vectors[k].zero_u == qdet_data.zeros[k], (
                f"Serre vector {k+1}: {vectors[k].zero_u} "
                f"!= qdet zero: {qdet_data.zeros[k]}"
            )

    def test_positive_negative_sector_partition(self):
        """The 4+20 decomposition covers all 24 directions exactly.

        Cross-check: serre_null_vectors sectors must partition {1,...,24}.
        """
        vectors = serre_null_vectors()
        pos_indices = {v.index for v in vectors if v.sector == 'positive'}
        neg_indices = {v.index for v in vectors if v.sector == 'negative'}

        assert len(pos_indices) == SIG_PLUS
        assert len(neg_indices) == SIG_MINUS
        assert pos_indices | neg_indices == set(range(1, RANK + 1))
        assert pos_indices & neg_indices == set()

    def test_qdet_at_zero_vs_product_of_negated_zeros(self):
        """qdet(0) = prod(-u_i) via (a) evaluate, (b) direct product of -u_i.

        Path A: quantum_determinant_evaluate(0).
        Path B: prod_{i=1}^{24} (0 - u_i) = prod (-u_i).
        """
        params = kummer_k3_parameters()
        qdet_data = quantum_determinant_zeros(params)

        # Path A
        val_A = quantum_determinant_evaluate(Rational(0), params)

        # Path B
        val_B = Rational(1)
        for ui in qdet_data.zeros:
            val_B *= (-ui)

        assert val_A == val_B

    def test_weyl_shift_range_cross_check(self):
        """Range of Weyl shifts via (a) profile, (b) direct computation.

        Path A: weyl_shift_profile()['range']
        Path B: max(shifts) - min(shifts) computed directly
        """
        # Path A
        profile = weyl_shift_profile()
        range_A = profile['range']

        # Path B
        shifts = weyl_shifts_from_mukai().shifts
        range_B = max(shifts) - min(shifts)

        assert range_A == range_B

    def test_indefinite_sum_rho_cross_check(self):
        """Sum rho for indefinite pairing via two independent formulas.

        Path A: sum of cumulative shifts.
        Path B: (SIG_PLUS * (SIG_PLUS - 1) / 2) - SIG_MINUS * SIG_PLUS
                + SIG_MINUS * (SIG_MINUS - 1) / 2 ... (closed-form).

        Derivation of Path B closed-form:
          rho_i = i-1 for i=1..SIG_PLUS (ascending +1 steps)
          rho_{SIG_PLUS+1} = SIG_PLUS (peak)
          rho_{SIG_PLUS+k} = SIG_PLUS - (k-1) for k=1..SIG_MINUS
                           (descending -1 steps)

          sum over ascending: sum_{i=0}^{SIG_PLUS-1} i = SIG_PLUS*(SIG_PLUS-1)/2
          sum over descending: sum_{k=1}^{SIG_MINUS} (SIG_PLUS - k + 1)
                             = SIG_MINUS*SIG_PLUS - SIG_MINUS*(SIG_MINUS-1)/2
        """
        # Path A
        shifts = weyl_shifts_from_mukai().shifts
        sum_A = sum(shifts)

        # Path B: closed form
        p = SIG_PLUS    # = 4
        m = SIG_MINUS   # = 20
        ascending_sum = p * (p - 1) // 2  # 0+1+2+3 = 6
        # Descending: rho_{p+k} = p - (k-1) for k=1..m
        # Values: p, p-1, ..., p-m+1
        descending_sum = sum(p - (k - 1) for k in range(1, m + 1))
        sum_B = ascending_sum + descending_sum

        assert sum_A == sum_B, f"Path A ({sum_A}) != Path B ({sum_B})"
