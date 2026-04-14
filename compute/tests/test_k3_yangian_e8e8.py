r"""Tests for the K3 Yangian at the E_8 x E_8 maximal enhancement point.

Tests organized by topic:
  1. Mukai decomposition and central charge accounting
  2. Structure function factorization and unitarity
  3. Degree analysis (why (24,24) not (500,500))
  4. Serre relations and orthogonality
  5. R-matrix block structure
  6. E_8 Lax operator properties
  7. Heterotic string connection
  8. Leech lattice non-connection
  9. Shadow class analysis
  10. Enhancement comparison landscape

All test points satisfy AP-CY28 (avoid poles at +/- h_i).
"""

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.k3_yangian_e8e8 import (
    COMPLEMENT_RANK,
    COMPLEMENT_SIG_MINUS,
    COMPLEMENT_SIG_PLUS,
    E8E8_TOTAL_DIM_G,
    E8E8_TOTAL_RANK,
    E8_DIM_G,
    E8_DIM_V,
    E8_DUAL_COXETER,
    E8_DYNKIN_EDGES,
    E8_LEVEL1_CENTRAL_CHARGE,
    E8_RANK,
    MUKAI_RANK,
    STRUCTURE_FUNCTION_DEGREE,
    e8_lax_properties,
    e8_serre_exponents,
    e8e8_mukai_decomposition,
    e8e8_parameters,
    e8e8_rmatrix_data,
    e8e8_serre_data,
    e8e8_shadow_class,
    enhancement_comparison,
    full_e8e8_verification,
    heterotic_e8e8_data,
    leech_lattice_analysis,
    structure_function_degree_analysis,
    structure_function_e8e8,
    verify_central_charge_accounting,
    verify_serre_orthogonality,
)
from compute.lib.ade_yangian_level1 import ade_data, e8_lax_operator


# =========================================================================
# 1. Mukai lattice decomposition
# =========================================================================

class TestMukaiDecomposition:
    """Mukai lattice decomposition at the E8 x E8 point."""

    def test_mukai_rank(self):
        """Mukai rank is 24."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.mukai_rank == 24

    def test_mukai_signature(self):
        """Mukai signature is (4, 20)."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.mukai_signature == (4, 20)

    def test_e8_rank(self):
        """Each E_8 factor has rank 8."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.e8_rank == 8

    def test_e8e8_total_rank(self):
        """E_8 x E_8 total rank is 16."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.e8e8_total_rank == 16

    def test_complement_rank(self):
        """Orthogonal complement has rank 8."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.complement_rank == 8

    def test_rank_sum_is_24(self):
        """E_8 x E_8 rank + complement rank = 24."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.e8e8_total_rank + decomp.complement_rank == 24

    def test_complement_signature(self):
        """Complement U^4 has signature (4, 4)."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.complement_signature == (4, 4)

    def test_complement_is_U4(self):
        """Complement lattice is U^4."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.complement_lattice == 'U^4'

    def test_is_maximal_ade(self):
        """E_8 x E_8 is the maximal ADE enhancement."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.is_maximal_ade is True


# =========================================================================
# 2. Central charge accounting
# =========================================================================

class TestCentralCharge:
    """Central charge at the E8 x E8 point."""

    def test_c_e8_level1(self):
        """c(hat{e}_8, k=1) = 8."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.e8_central_charge_level1 == Fraction(8)

    def test_c_total_is_24(self):
        """c_total = 8 + 8 + 8 = 24."""
        decomp = e8e8_mukai_decomposition()
        assert decomp.total_central_charge == Fraction(24)

    def test_c_total_equals_mukai_rank(self):
        """c_total = Mukai rank = 24 (Freudenthal-de Vries at k=1)."""
        result = verify_central_charge_accounting()
        assert result['c_total_equals_mukai_rank']

    def test_freudenthal_de_vries_e8(self):
        """dim(e_8) = rank(e_8) * (1 + h^vee(e_8)) = 8 * 31 = 248."""
        data = ade_data('E8')
        assert data.dim_g == data.rank * (1 + data.dual_coxeter)
        assert data.dim_g == 248

    def test_c_e8_from_formula(self):
        """c = dim(g)/(1+h^vee) = 248/31 = 8."""
        assert Fraction(248, 31) == Fraction(8)


# =========================================================================
# 3. E_8 Lie algebra data
# =========================================================================

class TestE8Data:
    """E_8 root system data."""

    def test_e8_dim_g(self):
        """dim(e_8) = 248."""
        assert E8_DIM_G == 248

    def test_e8_dim_V(self):
        """dim(V) = 248 (adjoint = smallest rep)."""
        assert E8_DIM_V == 248

    def test_e8_adjoint_is_smallest(self):
        """E_8 is unique: adjoint = smallest representation."""
        assert E8_DIM_G == E8_DIM_V

    def test_e8_dual_coxeter(self):
        """h^vee(e_8) = 30."""
        assert E8_DUAL_COXETER == 30

    def test_e8_rank(self):
        """rank(e_8) = 8."""
        assert E8_RANK == 8

    def test_e8_exponents(self):
        """E_8 exponents: 1, 7, 11, 13, 17, 19, 23, 29."""
        data = ade_data('E8')
        assert data.exponents == (1, 7, 11, 13, 17, 19, 23, 29)

    def test_e8_exponent_sum(self):
        """Sum of E_8 exponents = 120 = number of positive roots."""
        data = ade_data('E8')
        assert sum(data.exponents) == 120
        assert (data.dim_g - data.rank) // 2 == 120

    def test_e8e8_total_dim(self):
        """dim(e_8 x e_8) = 496."""
        assert E8E8_TOTAL_DIM_G == 496


# =========================================================================
# 4. Parameters and structure function
# =========================================================================

class TestParameters:
    """Yangian parameters at the E8 x E8 point."""

    def test_parameter_count(self):
        """24 parameters total."""
        params = e8e8_parameters()
        assert len(params.h) == 24

    def test_e8_1_count(self):
        """8 parameters for first E_8."""
        params = e8e8_parameters()
        assert len(params.h_e8_1) == 8

    def test_e8_2_count(self):
        """8 parameters for second E_8."""
        params = e8e8_parameters()
        assert len(params.h_e8_2) == 8

    def test_complement_count(self):
        """8 parameters for complement."""
        params = e8e8_parameters()
        assert len(params.h_complement) == 8

    def test_cy2_constraint(self):
        """CY_2 constraint: sum h_i = 0."""
        params = e8e8_parameters()
        assert abs(params.cy2_sum) < 1e-12, f"CY2 sum = {params.cy2_sum}"

    def test_parameters_nondegenerate(self):
        """No h_i = 0 (avoids degenerate structure function)."""
        params = e8e8_parameters()
        for i, h in enumerate(params.h):
            assert abs(h) > 1e-15, f"h_{i} = 0 (degenerate)"


class TestStructureFunction:
    """Structure function at the E8 x E8 point."""

    def test_factorization(self):
        """g_{K3}(z) = g_{E8,1}(z) * g_{E8,2}(z) * g_{U^4}(z)."""
        result = structure_function_e8e8(z=5.3)
        assert result['factored'], "Structure function factorization failed"

    def test_unitarity(self):
        """g(z) * g(-z) = 1."""
        result = structure_function_e8e8(z=5.3)
        assert result['unitarity'], "Unitarity failed"

    def test_unitarity_multiple_points(self):
        """Unitarity at several test points."""
        for z_val in [3.7, 5.3, 7.3, 11.1]:
            result = structure_function_e8e8(z=z_val)
            assert result['unitarity'], f"Unitarity failed at z={z_val}"

    def test_degree_is_24_24(self):
        """Total degree is (24, 24)."""
        result = structure_function_e8e8(z=5.3)
        assert result['degree'] == (24, 24)

    def test_degree_e8_factors(self):
        """Each E_8 factor has degree (8, 8)."""
        result = structure_function_e8e8(z=5.3)
        assert result['degree_e8_1'] == (8, 8)
        assert result['degree_e8_2'] == (8, 8)

    def test_degree_complement(self):
        """Complement has degree (8, 8)."""
        result = structure_function_e8e8(z=5.3)
        assert result['degree_complement'] == (8, 8)

    def test_g_at_infinity(self):
        """g_{K3}(z) -> 1 as z -> infinity."""
        result = structure_function_e8e8(z=10000.0)
        assert abs(result['g_total'] - 1.0) < 0.01

    def test_g_at_zero(self):
        """g_{K3}(0) = prod(-h_i/h_i) = (-1)^{24} = 1."""
        params = e8e8_parameters()
        # Check no h_i = 0 first
        if all(abs(h) > 1e-10 for h in params.h):
            result = structure_function_e8e8(z=0.0, params=params)
            # g(0) = prod (-h_i / h_i) = (-1)^{24} = 1
            assert abs(result['g_total'] - 1.0) < 1e-10


# =========================================================================
# 5. Degree analysis
# =========================================================================

class TestDegreeAnalysis:
    """Degree analysis of the structure function."""

    def test_degree_not_500(self):
        """The degree is (24,24), NOT (500,500)."""
        result = structure_function_degree_analysis()
        assert result['not_500']
        assert result['total_degree'] == (24, 24)

    def test_degree_sum_check(self):
        """8 + 8 + 8 = 24."""
        result = structure_function_degree_analysis()
        assert result['sum_equals_24']
        assert result['sum_check'] == (24, 24)

    def test_structure_function_degree_constant(self):
        """Structure function degree = Mukai rank = 24 (always)."""
        assert STRUCTURE_FUNCTION_DEGREE == MUKAI_RANK == 24


# =========================================================================
# 6. Serre relations
# =========================================================================

class TestSerreRelations:
    """Serre ideal at the E8 x E8 point."""

    def test_e8_dynkin_edges(self):
        """E_8 Dynkin diagram has 7 edges."""
        serre = e8e8_serre_data()
        assert serre.num_serre_e8_1 == 7

    def test_total_serre(self):
        """Total nontrivial Serre relations: 7 + 7 = 14."""
        serre = e8e8_serre_data()
        assert serre.num_serre_total == 14

    def test_mixing_serre_vanishes(self):
        """Mixing Serre I_mix = 0 by Mukai orthogonality."""
        serre = e8e8_serre_data()
        assert serre.mixing_serre_vanishes is True

    def test_abelian_relations(self):
        """Abelian complement has C(8,2) = 28 commutativity relations."""
        serre = e8e8_serre_data()
        assert serre.abelian_relations == 28

    def test_serre_decomposition(self):
        """Serre ideal = I_{E8,1} + I_{E8,2} + I_{ab}."""
        serre = e8e8_serre_data()
        assert serre.decomposition == 'I_{E8,1} + I_{E8,2} + I_{ab}'


class TestSerreExponents:
    """Serre exponents for the E_8 Dynkin diagram."""

    def test_adjacent_exponent_2(self):
        """Adjacent pairs have Serre exponent 2."""
        result = e8_serre_exponents()
        assert result['all_adjacent_exponent_2']

    def test_non_adjacent_exponent_1(self):
        """Non-adjacent pairs have Serre exponent 1."""
        result = e8_serre_exponents()
        assert result['all_non_adjacent_exponent_1']

    def test_7_adjacent_pairs(self):
        """E_8 has 7 adjacent pairs (7 Dynkin edges)."""
        result = e8_serre_exponents()
        assert result['num_adjacent'] == 7

    def test_total_pairs(self):
        """Total pairs = C(8,2) = 28."""
        result = e8_serre_exponents()
        assert result['total_pairs'] == 28
        assert result['expected_total_pairs'] == 28


class TestSerreOrthogonality:
    """Verify mixing Serre relations vanish."""

    def test_cross_sector_trivial(self):
        """Cross-sector structure functions are trivial (g = 1)."""
        result = verify_serre_orthogonality(z=5.3)
        assert result['cross_sector_all_trivial']

    def test_mixing_vanishes(self):
        """I_mix = 0 by Mukai orthogonality."""
        result = verify_serre_orthogonality(z=5.3)
        assert result['mixing_serre_vanishes']

    def test_intra_e8_has_nontrivial(self):
        """Intra-E_8 structure functions include nontrivial entries."""
        result = verify_serre_orthogonality(z=5.3)
        assert result['intra_e8_nontrivial_pairs'] > 0


# =========================================================================
# 7. R-matrix
# =========================================================================

class TestRMatrix:
    """R-matrix at the E8 x E8 point."""

    def test_e8_block_size(self):
        """E_8 R-matrix block is 248 x 248."""
        rmatrix = e8e8_rmatrix_data()
        assert rmatrix.e8_block_size == 248

    def test_complement_block_size(self):
        """Complement R-matrix block is 8 x 8."""
        rmatrix = e8e8_rmatrix_data()
        assert rmatrix.complement_block_size == 8

    def test_satisfies_ybe(self):
        """R-matrix satisfies YBE (abelian case: trivially)."""
        rmatrix = e8e8_rmatrix_data()
        assert rmatrix.satisfies_ybe

    def test_complement_diagonal(self):
        """Complement R-matrix is diagonal."""
        rmatrix = e8e8_rmatrix_data()
        assert rmatrix.complement_diagonal


# =========================================================================
# 8. E_8 Lax operator
# =========================================================================

class TestE8Lax:
    """E_8 Lax operator properties."""

    def test_lax_shape_248(self):
        """E_8 Lax operator is 248 x 248."""
        result = e8_lax_properties(u=5.3)
        assert result['lax_is_248x248']

    def test_transfer_matrix(self):
        """Transfer matrix t(u) = 248u + 1 (adjoint HW)."""
        result = e8_lax_properties(u=5.3)
        assert result['transfer_correct']

    def test_adjoint_equals_smallest(self):
        """E_8: adjoint = smallest representation."""
        result = e8_lax_properties(u=5.3)
        assert result['adjoint_equals_smallest']
        assert result['dim_g_equals_dim_V']

    def test_lax_direct_construction(self):
        """Direct Lax operator construction matches."""
        u = 7.3  # AP-CY28 safe
        L = e8_lax_operator(u)
        assert L.shape == (248, 248)
        # Transfer matrix = trace(L)
        t = np.trace(L)
        assert abs(t - (248 * u + 1.0)) < 1e-10


# =========================================================================
# 9. Heterotic string connection
# =========================================================================

class TestHeteorticConnection:
    """Connection to the E_8 x E_8 heterotic string."""

    def test_gauge_group(self):
        """Gauge group is E_8 x E_8."""
        data = heterotic_e8e8_data()
        assert data.gauge_group == 'E_8 x E_8'

    def test_gauge_rank(self):
        """Gauge rank is 16."""
        data = heterotic_e8e8_data()
        assert data.gauge_rank == 16

    def test_heterotic_central_charge(self):
        """Heterotic central charge from compact bosons is 16."""
        data = heterotic_e8e8_data()
        assert data.heterotic_central_charge == 16

    def test_maximal_enhancement(self):
        """E_8 x E_8 is the maximal enhancement."""
        data = heterotic_e8e8_data()
        assert data.maximal_enhancement is True

    def test_horava_witten(self):
        """M-theory lift via Horava-Witten interval."""
        data = heterotic_e8e8_data()
        assert data.horava_witten_interval is True

    def test_cy_a_2_proved(self):
        """CY-A_2 is required and PROVED."""
        data = heterotic_e8e8_data()
        assert data.cy_a_2_required is True
        assert data.cy_a_2_status == 'PROVED'


# =========================================================================
# 10. Leech lattice analysis
# =========================================================================

class TestLeechLattice:
    """The Leech lattice is NOT obtained from the Mukai lattice."""

    def test_different_signatures(self):
        """Mukai (4,20) vs Leech (0,24): different signatures."""
        result = leech_lattice_analysis()
        assert result['mukai_signature'] == (4, 20)
        assert result['leech_signature'] == (0, 24)
        assert result['same_signature'] is False

    def test_same_rank(self):
        """Both have rank 24."""
        result = leech_lattice_analysis()
        assert result['same_rank'] is True

    def test_cannot_obtain_leech(self):
        """Cannot obtain Leech from Mukai by removing directions."""
        result = leech_lattice_analysis()
        assert result['can_obtain_leech_from_mukai'] is False


# =========================================================================
# 11. Shadow class
# =========================================================================

class TestShadowClass:
    """Shadow class at the E8 x E8 point."""

    def test_subalgebra_class_L(self):
        """hat{e}_8 + hat{e}_8 subalgebra: class L."""
        result = e8e8_shadow_class()
        assert result['subalgebra_shadow_class'] == 'L'

    def test_subalgebra_depth_3(self):
        """Subalgebra shadow depth = 3."""
        result = e8e8_shadow_class()
        assert result['subalgebra_shadow_depth'] == 3

    def test_complement_class_G(self):
        """U^4 complement: class G (Heisenberg)."""
        result = e8e8_shadow_class()
        assert result['complement_shadow_class'] == 'G'

    def test_full_sigma_model_class_M(self):
        """Full sigma model: class M (always for K3)."""
        result = e8e8_shadow_class()
        assert result['full_sigma_model_class'] == 'M'

    def test_kappa_ch_is_2(self):
        """kappa_ch = 2 at ALL K3 moduli points (AP113)."""
        result = e8e8_shadow_class()
        assert result['kappa_ch'] == 2

    def test_kappa_ch_independent(self):
        """kappa_ch independent of enhancement type."""
        result = e8e8_shadow_class()
        assert result['kappa_ch_independent_of_enhancement'] is True


# =========================================================================
# 12. Enhancement comparison
# =========================================================================

class TestEnhancementComparison:
    """Comparison of E8 x E8 with other enhancement points."""

    def test_comparison_has_entries(self):
        """Comparison includes multiple enhancement points."""
        comparison = enhancement_comparison()
        assert len(comparison) >= 6

    def test_e8e8_is_maximal(self):
        """E8 x E8 entry is marked as maximal."""
        comparison = enhancement_comparison()
        e8e8_entry = [c for c in comparison if c['label'] == 'E8 x E8']
        assert len(e8e8_entry) == 1
        assert e8e8_entry[0]['is_maximal'] is True

    def test_all_c_total_24(self):
        """All enhancement points have c_total = 24."""
        comparison = enhancement_comparison()
        for entry in comparison:
            assert entry['c_total'] == '24', (
                f"{entry['label']}: c_total = {entry['c_total']}"
            )

    def test_generic_has_no_serre(self):
        """Generic point has 0 nontrivial Serre relations."""
        comparison = enhancement_comparison()
        generic = [c for c in comparison if c['label'] == 'Generic'][0]
        assert generic['serre_relations'] == 0

    def test_e8e8_has_14_serre(self):
        """E8 x E8 has 14 nontrivial Serre relations."""
        comparison = enhancement_comparison()
        e8e8 = [c for c in comparison if c['label'] == 'E8 x E8'][0]
        assert e8e8['serre_relations'] == 14


# =========================================================================
# 13. Constants consistency
# =========================================================================

class TestConstants:
    """Consistency of module-level constants."""

    def test_e8_rank(self):
        assert E8_RANK == 8

    def test_e8_dim_g(self):
        assert E8_DIM_G == 248

    def test_e8_dim_v(self):
        assert E8_DIM_V == 248

    def test_e8_dual_coxeter(self):
        assert E8_DUAL_COXETER == 30

    def test_e8_level1_cc(self):
        assert E8_LEVEL1_CENTRAL_CHARGE == Fraction(8)

    def test_e8e8_total_rank(self):
        assert E8E8_TOTAL_RANK == 16

    def test_e8e8_total_dim(self):
        assert E8E8_TOTAL_DIM_G == 496

    def test_complement_rank(self):
        assert COMPLEMENT_RANK == 8

    def test_complement_sig(self):
        assert COMPLEMENT_SIG_PLUS == 4
        assert COMPLEMENT_SIG_MINUS == 4

    def test_e8_dynkin_edges(self):
        assert E8_DYNKIN_EDGES == 7

    def test_structure_fn_degree(self):
        assert STRUCTURE_FUNCTION_DEGREE == 24


# =========================================================================
# 14. Full verification
# =========================================================================

class TestFullVerification:
    """Comprehensive end-to-end verification."""

    def test_full_verification_passes(self):
        """All sub-verifications pass."""
        result = full_e8e8_verification()
        assert result['all_ok'], "Full verification failed"

    def test_status_is_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        result = full_e8e8_verification()
        assert result['status'] == 'CONJECTURAL'
