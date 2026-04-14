r"""Tests for super_yangian_resolves.py: what Y(gl(4|20)) resolves.

STATUS: ALL results CONJECTURAL (AP-CY14).
Tests verify internal consistency of the five analyses:
  1. Representation theory (typical/atypical)
  2. Super R-matrix enhanced properties
  3. Kac-Kazhdan determinant structure
  4. Sigma model supertrace
  5. Root of unity MTC comparison

SECTIONS:
    1. Atypicality analysis (7 tests)
    2. Atypicality degree computation (6 tests)
    3. Mukai vector typicality classification (5 tests)
    4. Super R-matrix enhanced properties (7 tests)
    5. Fusion dimension identity (5 tests)
    6. Spectral decomposition (5 tests)
    7. Kac-Kazhdan structure (7 tests)
    8. Kac-Kazhdan explicit small rank (5 tests)
    9. Sigma model supertrace (6 tests)
    10. Restricted super-partitions (6 tests)
    11. Root of unity comparison (6 tests)
    12. Full resolution report (4 tests)
    13. Multi-path cross-verification (8 tests)

Total: 77 tests.
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.super_yangian_resolves import (
    M_EVEN,
    N_ODD,
    SUPER_DIM,
    TOTAL_DIM,
    atypicality_analysis,
    atypicality_degree,
    classify_mukai_vector_typicality,
    super_rmatrix_enhanced_properties,
    verify_fusion_dimension_identity,
    super_spectral_decomposition_small,
    kac_kazhdan_structure,
    kac_kazhdan_explicit_small,
    sigma_model_supertrace,
    restricted_super_partitions,
    _count_restricted,
    root_of_unity_comparison,
    super_partition_generating_function,
    full_super_yangian_resolves_report,
)

from compute.lib.k3_super_yangian import (
    mukai_super_grading,
    super_permutation_spectrum,
    super_t_matrix_structure,
    verify_entry_count_matches_adversarial,
)


# =========================================================================
# 1. Atypicality analysis
# =========================================================================

class TestAtypicalityAnalysis:
    """Tests for atypicality data of gl(m|n)."""

    def test_max_atypicality_k3(self):
        """Max atypicality for gl(4|20) is min(4,20) = 4."""
        data = atypicality_analysis()
        assert data.max_atypicality == 4

    def test_atypicality_conditions_count(self):
        """Number of atypicality conditions is m*n = 80."""
        data = atypicality_analysis()
        assert data.num_atypicality_conditions == 80

    def test_even_positive_roots(self):
        """Even positive roots: C(4,2) + C(20,2) = 6 + 190 = 196."""
        data = atypicality_analysis()
        assert data.even_positive_roots == 196

    def test_odd_positive_roots(self):
        """Odd positive roots: 4 * 20 = 80."""
        data = atypicality_analysis()
        assert data.odd_positive_roots == 80

    def test_all_odd_roots_isotropic(self):
        """For gl(m|n), ALL odd roots are isotropic."""
        data = atypicality_analysis()
        assert data.isotropic_odd_roots == data.odd_positive_roots

    def test_total_positive_roots(self):
        """Total: 196 + 80 = 276."""
        data = atypicality_analysis()
        assert data.total_positive_roots == 276

    def test_small_rank(self):
        """Atypicality for gl(2|1): max = 1, conditions = 2."""
        data = atypicality_analysis(m=2, n=1)
        assert data.max_atypicality == 1
        assert data.num_atypicality_conditions == 2
        assert data.even_positive_roots == 1  # C(2,2) + C(1,2) = 1 + 0
        assert data.odd_positive_roots == 2


# =========================================================================
# 2. Atypicality degree computation
# =========================================================================

class TestAtypicalityDegree:
    """Tests for computing the degree of atypicality of a weight."""

    def test_typical_weight_gl21(self):
        """A generic weight for gl(2|1) is typical (degree 0)."""
        # lambda = (5, 3 | 0) -- no atypicality condition satisfied
        # Condition 1: 5 - 0 = 5, need i - m - j = 1 - 2 - 1 = -2. 5 != -2.
        # Condition 2: 3 - 0 = 3, need 2 - 2 - 1 = -1. 3 != -1.
        assert atypicality_degree([5, 3, 0], m=2, n=1) == 0

    def test_atypical_weight_gl21(self):
        """An atypical weight for gl(2|1) has degree 1."""
        # lambda = (0, 0 | 2): condition 1: 0 - 2 = -2 = 1-2-1. YES.
        assert atypicality_degree([0, 0, 2], m=2, n=1) == 1

    def test_atypical_weight_gl21_second_condition(self):
        """Second atypicality condition for gl(2|1)."""
        # lambda = (0, 0 | 1): condition 2: 0 - 1 = -1 = 2-2-1. YES.
        assert atypicality_degree([0, 0, 1], m=2, n=1) == 1

    def test_maximally_atypical_gl21(self):
        """Maximally atypical for gl(2|1) is degree 1 = min(2,1)."""
        # Both conditions: 0 - 2 = -2 AND 0 - 1 = -1? Need lambda = (0, 0 | 2)
        # Then cond 2: 0 - 2 = -2, need -1. NO.
        # So max degree 1 for gl(2|1) with single condition.
        # lambda = (-2, -1 | 0): cond 1: -2-0=-2=1-3=-2 YES; cond 2: -1-0=-1=2-3=-1 YES.
        # Both satisfied! But min(2,1) = 1, so degree capped at 1.
        result = atypicality_degree([-2, -1, 0], m=2, n=1)
        assert result == 1  # capped at min(m,n)

    def test_wrong_length_raises(self):
        """Wrong weight length raises ValueError."""
        with pytest.raises(ValueError):
            atypicality_degree([1, 2], m=2, n=1)

    def test_typical_generic_large(self):
        """A large generic weight for gl(4|20) is typical."""
        # Use large values far from any atypicality condition
        lam = [100 + i * 17 for i in range(4)] + [-(200 + j * 13) for j in range(20)]
        assert atypicality_degree(lam) == 0


# =========================================================================
# 3. Mukai vector typicality classification
# =========================================================================

class TestMukaiVectorTypicality:
    """Tests for classifying Mukai vectors by typicality."""

    def test_real_root(self):
        """v^2 = -2 (real root) -> maximally atypical."""
        result = classify_mukai_vector_typicality(-2)
        assert result['root_type'] == 'real'
        assert result['generic_typicality'] == 'maximally_atypical'
        assert result['atypicality_degree_generic'] == 4

    def test_null_root(self):
        """v^2 = 0 (null root) -> atypical degree 1."""
        result = classify_mukai_vector_typicality(0)
        assert result['root_type'] == 'null'
        assert result['atypicality_degree_generic'] == 1

    def test_imaginary_root(self):
        """v^2 > 0 (imaginary root) -> typical."""
        result = classify_mukai_vector_typicality(2)
        assert result['root_type'] == 'imaginary'
        assert result['generic_typicality'] == 'typical'
        assert result['atypicality_degree_generic'] == 0

    def test_not_a_root(self):
        """v^2 < -2 -> not a root, typical."""
        result = classify_mukai_vector_typicality(-4)
        assert result['root_type'] == 'not_a_root'
        assert result['generic_typicality'] == 'typical'

    def test_bps_correspondence(self):
        """Module types map to BPS multiplet types."""
        real = classify_mukai_vector_typicality(-2)
        null = classify_mukai_vector_typicality(0)
        imag = classify_mukai_vector_typicality(2)
        assert real['module_type'] == 'short_multiplet'
        assert null['module_type'] == 'semi_short_multiplet'
        assert imag['module_type'] == 'long_multiplet'


# =========================================================================
# 4. Super R-matrix enhanced properties
# =========================================================================

class TestSuperRMatrixProperties:
    """Tests for enhanced super R-matrix properties."""

    def test_crossing_shift_super(self):
        """Crossing shift for gl(4|20) is (4-20) = -16."""
        props = super_rmatrix_enhanced_properties()
        assert props.crossing_shift_super == -16

    def test_crossing_shift_ordinary(self):
        """Crossing shift for gl(24) is 24."""
        props = super_rmatrix_enhanced_properties()
        assert props.crossing_shift_ordinary == 24

    def test_crossing_parameter_super(self):
        """Crossing parameter for gl(4|20) is -8."""
        props = super_rmatrix_enhanced_properties()
        assert props.crossing_parameter_super == Fraction(-8, 1)

    def test_crossing_parameter_ordinary(self):
        """Crossing parameter for gl(24) is 12."""
        props = super_rmatrix_enhanced_properties()
        assert props.crossing_parameter_ordinary == Fraction(12, 1)

    def test_sym_super_dim(self):
        """Super-symmetric dim: 4*5/2 + 20*21/2 + 4*20 = 10 + 210 + 80 = 300."""
        props = super_rmatrix_enhanced_properties()
        assert props.sym_super_dim == 300

    def test_antisym_super_dim(self):
        """Super-antisymmetric dim: 4*3/2 + 20*19/2 + 4*20 = 6 + 190 + 80 = 276."""
        props = super_rmatrix_enhanced_properties()
        assert props.antisym_super_dim == 276

    def test_fusion_dim_match(self):
        """Super and ordinary fusion dimensions match."""
        props = super_rmatrix_enhanced_properties()
        assert props.fusion_dim_match is True


# =========================================================================
# 5. Fusion dimension identity
# =========================================================================

class TestFusionDimensionIdentity:
    """Tests for the identity dim S^2(C^{m|n}) = dim S^2(C^{m+n})."""

    def test_identity_k3(self):
        """Identity holds for (4,20)."""
        result = verify_fusion_dimension_identity()
        assert result['identity_verified'] is True

    def test_symmetric_match(self):
        """Super-symmetric dim = ordinary symmetric dim = 300."""
        result = verify_fusion_dimension_identity()
        assert result['super_symmetric_dim'] == 300
        assert result['ordinary_symmetric_dim'] == 300
        assert result['symmetric_match'] is True

    def test_antisymmetric_match(self):
        """Super-antisymmetric dim = ordinary antisymmetric dim = 276."""
        result = verify_fusion_dimension_identity()
        assert result['super_antisymmetric_dim'] == 276
        assert result['ordinary_antisymmetric_dim'] == 276

    def test_total(self):
        """Total = 576 = 24^2."""
        result = verify_fusion_dimension_identity()
        assert result['total_super'] == 576
        assert result['total_ordinary'] == 576

    def test_identity_small(self):
        """Identity holds for (2,1)."""
        result = verify_fusion_dimension_identity(m=2, n=1)
        assert result['identity_verified'] is True
        assert result['super_symmetric_dim'] == 6  # 3*4/2
        assert result['super_antisymmetric_dim'] == 3  # 3*2/2


# =========================================================================
# 6. Spectral decomposition
# =========================================================================

class TestSpectralDecomposition:
    """Tests for R_s(u) at u = +/- hbar."""

    def test_rank_at_plus_hbar_gl21(self):
        """R_s(hbar) for gl(2|1) has rank = dim S^2(C^{2|1}) = 6."""
        result = super_spectral_decomposition_small(m=2, n=1)
        assert result['rank_at_plus_hbar'] == 6

    def test_rank_at_minus_hbar_gl21(self):
        """R_s(-hbar) for gl(2|1) has rank = dim Lambda^2(C^{2|1}) = 3."""
        result = super_spectral_decomposition_small(m=2, n=1)
        assert result['rank_at_minus_hbar'] == 3

    def test_ranks_match_expected(self):
        """Ranks match expected dimensions."""
        result = super_spectral_decomposition_small(m=2, n=1)
        assert result['rank_matches_sym'] is True
        assert result['rank_matches_antisym'] is True

    def test_projectors_idempotent(self):
        """R(+/-hbar)/(+/-2*hbar) are idempotent projectors."""
        result = super_spectral_decomposition_small(m=2, n=1)
        assert result['projector_plus_idempotent'] is True
        assert result['projector_minus_idempotent'] is True

    def test_rank_sum_equals_total(self):
        """Rank at +hbar + rank at -hbar = d^2 = 9."""
        result = super_spectral_decomposition_small(m=2, n=1)
        assert result['rank_at_plus_hbar'] + result['rank_at_minus_hbar'] == 9


# =========================================================================
# 7. Kac-Kazhdan structure
# =========================================================================

class TestKacKazhdanStructure:
    """Tests for Kac-Kazhdan determinant structure."""

    def test_even_roots_k3(self):
        """C(4,2) + C(20,2) = 6 + 190 = 196."""
        kk = kac_kazhdan_structure()
        assert kk.even_positive_roots == 196

    def test_odd_roots_k3(self):
        """4 * 20 = 80 odd roots."""
        kk = kac_kazhdan_structure()
        assert kk.odd_positive_roots == 80

    def test_isotropic_equals_odd(self):
        """All odd roots are isotropic for gl(m|n)."""
        kk = kac_kazhdan_structure()
        assert kk.isotropic_odd_roots == kk.odd_positive_roots

    def test_total_roots(self):
        """Total: 196 + 80 = 276."""
        kk = kac_kazhdan_structure()
        assert kk.total_positive_roots == 276

    def test_max_simultaneous_null(self):
        """Max simultaneous null vectors: min(4,20) = 4."""
        kk = kac_kazhdan_structure()
        assert kk.max_simultaneous_null == 4

    def test_b_block_match(self):
        """80 odd roots = 80 B-block fermionic entries."""
        kk = kac_kazhdan_structure()
        assert kk.b_block_fermionic_match is True

    def test_small_rank(self):
        """Kac-Kazhdan for gl(2|1): 1 even, 2 odd, 2 isotropic."""
        kk = kac_kazhdan_structure(m=2, n=1)
        assert kk.even_positive_roots == 1
        assert kk.odd_positive_roots == 2
        assert kk.isotropic_odd_roots == 2
        assert kk.max_simultaneous_null == 1


# =========================================================================
# 8. Kac-Kazhdan explicit small rank
# =========================================================================

class TestKacKazhdanExplicit:
    """Tests for explicit Kac-Kazhdan root structure at small rank."""

    def test_gl21_even_roots(self):
        """gl(2|1) has 1 even positive root: e_1 - e_2."""
        result = kac_kazhdan_explicit_small(m=2, n=1)
        assert result['num_even'] == 1

    def test_gl21_odd_roots(self):
        """gl(2|1) has 2 odd positive roots."""
        result = kac_kazhdan_explicit_small(m=2, n=1)
        assert result['num_odd'] == 2

    def test_gl21_all_odd_isotropic(self):
        """All odd roots isotropic for gl(2|1)."""
        result = kac_kazhdan_explicit_small(m=2, n=1)
        assert result['all_odd_are_isotropic'] is True

    def test_gl21_atypicality_conditions(self):
        """gl(2|1) has 2 atypicality conditions."""
        result = kac_kazhdan_explicit_small(m=2, n=1)
        assert len(result['atypicality_conditions']) == 2

    def test_gl11(self):
        """gl(1|1) has 0 even roots and 1 odd root."""
        result = kac_kazhdan_explicit_small(m=1, n=1)
        assert result['num_even'] == 0
        assert result['num_odd'] == 1
        assert result['max_atypicality'] == 1


# =========================================================================
# 9. Sigma model supertrace
# =========================================================================

class TestSigmaModelSupertrace:
    """Tests for the sigma model trace/supertrace comparison."""

    def test_trace_starts_at_1(self):
        """Ordinary trace Z starts with coefficient 1."""
        result = sigma_model_supertrace(num_terms=10)
        assert result['trace_coeffs'][0] == 1

    def test_supertrace_starts_at_1(self):
        """Supertrace Z_s starts with coefficient 1."""
        result = sigma_model_supertrace(num_terms=10)
        assert result['supertrace_coeffs'][0] == 1

    def test_ratio_starts_at_1(self):
        """Ratio Z_s/Z starts at 1."""
        result = sigma_model_supertrace(num_terms=10)
        assert abs(result['ratio_coeffs'][0] - 1.0) < 1e-6

    def test_trace_second_coeff_is_24(self):
        """Z = 1/eta^{24}: coefficient of q^1 is 24."""
        result = sigma_model_supertrace(num_terms=10)
        assert result['trace_coeffs'][1] == 24

    def test_ratio_matches_theory(self):
        """Z_s/Z matches the theoretical formula prod (1-q^{2k})^{20}."""
        result = sigma_model_supertrace(num_terms=10)
        assert result['ratio_matches_theory'] is True

    def test_small_rank_trace(self):
        """Trace for (m=1, n=1) starts 1, 2, ..."""
        result = sigma_model_supertrace(num_terms=6, m=1, n=1)
        assert result['trace_coeffs'][0] == 1
        assert result['trace_coeffs'][1] == 2  # 1/(1-q)^2 -> [1, 2, 3, ...]


# =========================================================================
# 10. Restricted super-partitions
# =========================================================================

class TestRestrictedSuperPartitions:
    """Tests for restricted super-partition counting."""

    def test_charge_0(self):
        """At charge 0, there is exactly 1 super-partition: (empty, empty)."""
        assert restricted_super_partitions(0, N=3) == 1

    def test_charge_1_small(self):
        """At charge 1 for gl(2|1), N=3: partition (1|0) or (0|1) = 2+1 = 3."""
        # Even: partitions of 1 into <= 2 parts, each < 3 -> [1] = 1 way
        # Odd: partitions of 0 into <= 1 part, each < 3 -> [empty] = 1 way
        # So a=1, b=0: 1*1 = 1
        # a=0, b=1: even partitions of 0 = 1; odd partitions of 1 into <=1 parts each <3 = 1
        # Total: 1 + 1 = 2
        result = restricted_super_partitions(1, N=3, m=2, n=1)
        assert result == 2

    def test_restricted_partitions_basic(self):
        """Partitions of 3 into at most 2 parts each <= 2: {(2,1), (1,1,1)->NO(3 parts)}."""
        # Actually: at most 2 parts, each <= 2: (2,1) and (2,0)->counted as (2)
        # Wait: partitions of 3 into at most 2 parts each <= 2:
        # 2+1=3 -> (2,1) YES; 2+2=4 NO; 1+1+1 = 3 parts NO.
        # So just 1 partition: (2,1).
        assert _count_restricted(3, 2, 2) == 1

    def test_restricted_partitions_charge0(self):
        """Partitions of 0 into anything is always 1."""
        assert _count_restricted(0, 5, 10) == 1

    def test_restricted_partitions_1_part(self):
        """Partitions of k into at most 1 part each <= M: 1 if k <= M, else 0."""
        assert _count_restricted(3, 1, 5) == 1
        assert _count_restricted(6, 1, 5) == 0

    def test_abelian_vs_super_charge_0(self):
        """At charge 0, abelian and super counts both equal 1."""
        N = 5
        assert _count_restricted(0, 24, N - 1) == 1
        assert restricted_super_partitions(0, N) == 1


# =========================================================================
# 11. Root of unity comparison
# =========================================================================

class TestRootOfUnityComparison:
    """Tests comparing Y(gl(4|20)) vs Y(gl_1)^24 at root of unity."""

    def test_charge_0_match(self):
        """At charge 0, both have 1 simple."""
        result = root_of_unity_comparison(N=3, max_charge=3)
        assert result['charge_0_match'] is True

    def test_abelian_factorized(self):
        """Abelian S-matrix is factorized."""
        result = root_of_unity_comparison(N=3)
        assert result['s_matrix_factorized_abelian'] is True

    def test_super_not_factorized(self):
        """Super S-matrix is NOT factorized."""
        result = root_of_unity_comparison(N=3)
        assert result['s_matrix_factorized_super'] is False

    def test_counts_are_positive(self):
        """Both abelian and super counts are positive."""
        result = root_of_unity_comparison(N=3, max_charge=2)
        assert result['total_abelian_simples'] > 0
        assert result['total_super_simples'] > 0

    def test_charge_1_abelian(self):
        """At charge 1 for N=3: abelian partitions of 1 into <=24 parts each <3 = 1."""
        result = root_of_unity_comparison(N=3, max_charge=1)
        assert result['abelian_counts_by_charge'][1] == 1

    def test_charge_1_super(self):
        """At charge 1 for N=3: super-partitions = p_4(1<3)*p_20(0<3) + p_4(0<3)*p_20(1<3) = 1+1 = 2."""
        # Even: partitions of 1 into <=4 parts each <=2 -> just (1) -> 1
        # Odd: partitions of 0 -> 1
        # plus even: part of 0 -> 1; odd: part of 1 into <=20 parts each <=2 -> 1
        # total: 1*1 + 1*1 = 2
        result = root_of_unity_comparison(N=3, max_charge=1)
        assert result['super_counts_by_charge'][1] == 2


# =========================================================================
# 12. Full resolution report
# =========================================================================

class TestFullReport:
    """Tests for the comprehensive resolution report."""

    def test_max_atypicality(self):
        """Report has max_atypicality = 4."""
        result = full_super_yangian_resolves_report()
        assert result['rep_theory']['max_atypicality'] == 4

    def test_crossing_shift(self):
        """Report has crossing shift -16."""
        result = full_super_yangian_resolves_report()
        assert result['r_matrix']['crossing_shift'] == -16

    def test_b_block_match(self):
        """Report confirms B-block / odd root correspondence."""
        result = full_super_yangian_resolves_report()
        assert result['kac_kazhdan']['b_block_match'] is True

    def test_resolves_list(self):
        """Report lists at least 5 things the super-structure resolves."""
        result = full_super_yangian_resolves_report()
        assert len(result['resolves']) >= 5


# =========================================================================
# 13. Multi-path cross-verification (AP10)
# =========================================================================

class TestCrossVerification:
    """Cross-checks between independent computation paths."""

    def test_odd_roots_equals_fermionic_entries(self):
        """Kac-Kazhdan odd roots = T-matrix fermionic entries = 80.

        Path 1: from root system (kac_kazhdan_structure).
        Path 2: from T-matrix block structure (super_t_matrix_structure).
        """
        kk = kac_kazhdan_structure()
        t = super_t_matrix_structure()
        assert kk.odd_positive_roots == 80
        assert t.fermionic_entries == 160  # B + C = 80 + 80
        # Each odd root corresponds to entries in BOTH B and C blocks
        assert kk.odd_positive_roots * 2 == t.fermionic_entries

    def test_atypicality_conditions_equals_b_block(self):
        """Atypicality conditions (80) = B-block entries (80).

        Path 1: from Kac representation theory.
        Path 2: from RTT matrix structure.
        """
        atyp = atypicality_analysis()
        t = super_t_matrix_structure()
        b_entries = t.block_dims['B'][0] * t.block_dims['B'][1]
        assert atyp.num_atypicality_conditions == b_entries == 80

    def test_sym_dim_from_two_paths(self):
        """Super-symmetric dimension from two independent computations.

        Path 1: from R-matrix enhanced properties.
        Path 2: from fusion dimension identity.
        """
        rmat = super_rmatrix_enhanced_properties()
        fusion = verify_fusion_dimension_identity()
        assert rmat.sym_super_dim == fusion['super_symmetric_dim'] == 300

    def test_total_roots_plus_atypicality(self):
        """Total positive roots = even roots + odd roots.
        And odd roots = atypicality walls.

        Path 1: total from root counting.
        Path 2: sum of even and odd from separate counts.
        """
        kk = kac_kazhdan_structure()
        assert kk.total_positive_roots == kk.even_positive_roots + kk.odd_positive_roots
        assert kk.atypicality_walls == kk.odd_positive_roots

    def test_spectral_decomp_consistent_with_fusion_dims(self):
        """Spectral decomposition ranks match fusion dimensions.

        Path 1: numerical rank of R(+/-hbar) at gl(2|1).
        Path 2: analytical formula for S^2, Lambda^2 dimensions.
        """
        spec = super_spectral_decomposition_small(m=2, n=1)
        fusion = verify_fusion_dimension_identity(m=2, n=1)
        assert spec['rank_at_plus_hbar'] == fusion['super_symmetric_dim']
        assert spec['rank_at_minus_hbar'] == fusion['super_antisymmetric_dim']

    def test_crossing_parameter_equals_half_superdim(self):
        """Crossing parameter = superdimension / 2.

        Path 1: from super R-matrix properties.
        Path 2: from Mukai super-grading.
        """
        rmat = super_rmatrix_enhanced_properties()
        grading = mukai_super_grading()
        assert rmat.crossing_parameter_super == Fraction(grading.superdimension, 2)

    def test_max_atypicality_equals_min_rank(self):
        """Max atypicality = min(m_even, n_odd) from two independent sources.

        Path 1: from atypicality analysis.
        Path 2: from super-grading dimensions.
        """
        atyp = atypicality_analysis()
        grading = mukai_super_grading()
        assert atyp.max_atypicality == min(grading.m_even, grading.n_odd) == 4

    def test_super_partition_vs_abelian_at_charge_0(self):
        """Both counting methods agree at charge 0 for all N.

        Path 1: restricted super-partitions.
        Path 2: ordinary restricted partitions (abelian).
        """
        for N in [3, 5, 7]:
            assert restricted_super_partitions(0, N) == 1
            assert _count_restricted(0, 24, N - 1) == 1
