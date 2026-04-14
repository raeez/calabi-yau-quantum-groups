r"""Tests for K3 nonabelian R-matrix at ALL ADE enhancement types.

STATUS: CONJECTURAL (AP-CY14).  All results conditional on Y(g_{K3}).
The Lie algebra data and Yang R-matrices are unconditional mathematical facts;
the K3 embedding is conditional on CY-A_2 (proved at d=2).

Multi-path verification per AP10/AP128:
  [DC] direct computation from engine
  [LC] limiting case / cross-check with existing engines (A_1, D_4)
  [SY] symmetry (outer automorphisms, CY_2 constraint)
  [CF] cross-family (ADE comparison, monotonicity)
  [DA] dimensional analysis (state counting, central charge)
  [FO] formula verification (closed-form off-diagonal count)

AP-CY28: test points avoid poles at +/- h_i.
AP-CY14: all results CONJECTURAL.
AP-CY31: spectral parameter u (Yangian), NOT worldsheet z.
AP-CY30: pairwise YBE does NOT imply tetrahedron; not tested here.
AP113: all kappa subscripted.
"""

import numpy as np
import pytest
from fractions import Fraction

from compute.lib.k3_nonabelian_all_ade import (
    ADE_TYPES_ORDERED,
    FULL_ADE_DATA,
    OUTER_AUTOMORPHISMS,
    STATUS,
    a2_specific,
    branching_structure,
    cartan_matrix,
    d5_specific,
    dynkin_diagram_edges,
    e6_specific,
    e7_specific,
    e8_specific,
    full_ade_landscape,
    k3_embedding_parameters,
    master_all_ade,
    offdiag_growth_analysis,
    offdiagonal_count_general,
    outer_automorphism_landscape,
    serre_relations,
    structure_function_factored,
    yang_r_matrix_ade,
    yang_r_ybe_verification,
)


# =========================================================================
# 1. STATUS AND CONSTANTS
# =========================================================================

class TestStatusAndConstants:
    """Basic structural tests."""

    def test_status_conjectural(self):
        """Status is CONJECTURAL (AP-CY14)."""
        assert STATUS == 'CONJECTURAL'

    def test_ade_types_ordered(self):
        """Seven ADE types in rank order."""
        assert ADE_TYPES_ORDERED == ['A1', 'A2', 'D4', 'D5', 'E6', 'E7', 'E8']

    def test_full_ade_data_has_all_types(self):
        """FULL_ADE_DATA covers all seven types including D5."""
        for t in ADE_TYPES_ORDERED:
            assert t in FULL_ADE_DATA

    def test_d5_present(self):
        """D5 is present (absent from k3_rmatrix_enhanced.ADE_DATA)."""
        assert 'D5' in FULL_ADE_DATA
        assert FULL_ADE_DATA['D5']['rank'] == 5
        assert FULL_ADE_DATA['D5']['dim_V'] == 10

    def test_outer_automorphisms_defined(self):
        """Outer automorphisms defined for all types."""
        for t in ADE_TYPES_ORDERED:
            assert t in OUTER_AUTOMORPHISMS


# =========================================================================
# 2. OFF-DIAGONAL COUNT (all types)
# =========================================================================

class TestOffdiagonalCount:
    """Test off-diagonal counting for all ADE types."""

    @pytest.mark.parametrize("ade_type,expected", [
        ('A1', 48),
        ('A2', 144),
        ('D4', 294),
        ('D5', 510),
        ('E6', 810),
        ('E7', 1218),
        ('E8', 1764),
    ])
    def test_offdiag_value(self, ade_type, expected):
        """Off-diagonal count matches expected value.
        # VERIFIED: [DC] direct computation, [FO] formula
        """
        result = offdiagonal_count_general(ade_type)
        assert result['off_diagonal']['total'] == expected

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_state_count_324(self, ade_type):
        """State decomposition sums to 324.
        # VERIFIED: [DA] dimensional analysis
        """
        result = offdiagonal_count_general(ade_type)
        assert result['state_decomposition']['total'] == 324

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_formula_consistency(self, ade_type):
        """Off-diagonal matches closed-form: d*(d-1)*(26-d) + C(d,2)*(C(d,2)-1).
        # VERIFIED: [FO] formula, [DC] direct computation
        """
        result = offdiagonal_count_general(ade_type)
        d = result['n_mukai_dirs']
        c2 = d * (d - 1) // 2
        expected = d * (d - 1) * (26 - d) + c2 * (c2 - 1)
        assert result['off_diagonal']['total'] == expected

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_central_charge_24(self, ade_type):
        """Total central charge at level 1 is 24.
        # VERIFIED: [DA] c(g,1) + c_Heis(24-r) = 24
        """
        result = offdiagonal_count_general(ade_type)
        assert result['central_charge']['c_total_is_24']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_complement_rank(self, ade_type):
        """Complement rank = 24 - n_mukai_dirs.
        # VERIFIED: [DA]
        """
        result = offdiagonal_count_general(ade_type)
        assert result['complement_rank'] == 24 - result['n_mukai_dirs']

    def test_offdiag_a1_cross_check(self):
        """A1 off-diagonal cross-check with k3_rmatrix_enhanced.
        # VERIFIED: [LC] limiting case
        """
        from compute.lib.k3_rmatrix_enhanced import offdiagonal_count_ade
        old = offdiagonal_count_ade('A1')
        new = offdiagonal_count_general('A1')
        assert old['off_diagonal']['total'] == new['off_diagonal']['total']

    def test_offdiag_d4_cross_check(self):
        """D4 off-diagonal cross-check with k3_rmatrix_enhanced.
        # VERIFIED: [LC] limiting case
        """
        from compute.lib.k3_rmatrix_enhanced import offdiagonal_count_ade
        old = offdiagonal_count_ade('D4')
        new = offdiagonal_count_general('D4')
        assert old['off_diagonal']['total'] == new['off_diagonal']['total']

    def test_offdiag_e8_cross_check(self):
        """E8 off-diagonal cross-check with k3_rmatrix_enhanced.
        # VERIFIED: [LC] limiting case
        """
        from compute.lib.k3_rmatrix_enhanced import offdiagonal_count_ade
        old = offdiagonal_count_ade('E8')
        new = offdiagonal_count_general('E8')
        assert old['off_diagonal']['total'] == new['off_diagonal']['total']


# =========================================================================
# 3. FULL LANDSCAPE
# =========================================================================

class TestFullLandscape:
    """Test the full ADE landscape."""

    def test_monotonic_in_rank(self):
        """Off-diagonal count is strictly monotonic in rank.
        # VERIFIED: [CF] cross-family comparison
        """
        landscape = full_ade_landscape()
        assert landscape['monotonic_in_rank']

    def test_all_seven_types(self):
        """Landscape contains all seven ADE types plus generic.
        # VERIFIED: [DA]
        """
        landscape = full_ade_landscape()
        for t in ADE_TYPES_ORDERED:
            assert t in landscape['landscape']
        assert 'generic' in landscape['landscape']

    def test_generic_is_zero(self):
        """Generic point has 0 off-diagonal entries.
        # VERIFIED: [LC] abelian limit
        """
        landscape = full_ade_landscape()
        assert landscape['landscape']['generic']['n_offdiag'] == 0

    def test_growth_ratios_decreasing(self):
        """Growth ratios decrease with rank (sub-quadratic growth).
        # VERIFIED: [CF]
        """
        landscape = full_ade_landscape()
        ratios = list(landscape['growth_ratios'].values())
        # Each ratio should be >= 1 (monotonic)
        for r in ratios:
            assert r > 1.0
        # Ratios should decrease (growth slows)
        for i in range(1, len(ratios)):
            assert ratios[i] <= ratios[i - 1] + 0.01  # small tolerance


# =========================================================================
# 4. CARTAN MATRICES AND ROOT SYSTEMS
# =========================================================================

class TestCartanMatrices:
    """Test Cartan matrices for all types."""

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_cartan_symmetric(self, ade_type):
        """Cartan matrix is symmetric (simply-laced).
        # VERIFIED: [DC]
        """
        C = cartan_matrix(ade_type)
        assert np.array_equal(C, C.T)

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_cartan_diagonal_2(self, ade_type):
        """Diagonal entries equal 2.
        # VERIFIED: [DC]
        """
        C = cartan_matrix(ade_type)
        for i in range(C.shape[0]):
            assert C[i, i] == 2

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_cartan_offdiag_range(self, ade_type):
        """Off-diagonal entries in {0, -1} (simply-laced).
        # VERIFIED: [DC]
        """
        C = cartan_matrix(ade_type)
        r = C.shape[0]
        for i in range(r):
            for j in range(r):
                if i != j:
                    assert C[i, j] in {0, -1}, f"{ade_type}: C[{i},{j}]={C[i, j]}"

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_cartan_positive_definite(self, ade_type):
        """Cartan matrix is positive definite (finite-type condition).
        # VERIFIED: [DC]
        """
        C = cartan_matrix(ade_type)
        eigenvalues = np.linalg.eigvalsh(C.astype(float))
        assert all(ev > 0 for ev in eigenvalues), f"{ade_type}: eigenvalues={eigenvalues}"

    @pytest.mark.parametrize("ade_type,expected_rank", [
        ('A1', 1), ('A2', 2), ('D4', 4), ('D5', 5),
        ('E6', 6), ('E7', 7), ('E8', 8),
    ])
    def test_cartan_rank(self, ade_type, expected_rank):
        """Cartan matrix has correct rank.
        # VERIFIED: [DA]
        """
        C = cartan_matrix(ade_type)
        assert C.shape == (expected_rank, expected_rank)


# =========================================================================
# 5. DYNKIN DIAGRAM AND BRANCHING
# =========================================================================

class TestDynkinDiagram:
    """Test Dynkin diagram structure."""

    @pytest.mark.parametrize("ade_type,expected_edges", [
        ('A1', 0), ('A2', 1), ('D4', 3), ('D5', 4),
        ('E6', 5), ('E7', 6), ('E8', 7),
    ])
    def test_num_edges(self, ade_type, expected_edges):
        """Number of edges = rank - 1.
        # VERIFIED: [DA]
        """
        edges = dynkin_diagram_edges(ade_type)
        assert len(edges) == expected_edges

    def test_a2_linear(self):
        """A2 is linear (no fork).
        # VERIFIED: [DC]
        """
        b = branching_structure('A2')
        assert not b['is_fork']
        assert b['diagram_type'] == 'linear'

    def test_d4_fork(self):
        """D4 has a fork (branching node with valence 3).
        # VERIFIED: [DC]
        """
        b = branching_structure('D4')
        assert b['is_fork']
        assert b['diagram_type'] == 'fork_D'
        assert any(v >= 3 for v in b['valences'].values())

    def test_d5_fork(self):
        """D5 has a fork.
        # VERIFIED: [DC]
        """
        b = branching_structure('D5')
        assert b['is_fork']
        assert b['diagram_type'] == 'fork_D'

    def test_e6_fork(self):
        """E6 has a fork.
        # VERIFIED: [DC]
        """
        b = branching_structure('E6')
        assert b['is_fork']
        assert b['diagram_type'] == 'fork_E'

    def test_d5_branching_node_valence_3(self):
        """D5 branching node has valence 3.
        # VERIFIED: [DC]
        """
        b = branching_structure('D5')
        bnode = b['branching_node']
        assert b['valences'][bnode] == 3

    def test_e_type_branching_node_valence_3(self):
        """E-type branching nodes have valence 3.
        # VERIFIED: [DC]
        """
        for t in ['E6', 'E7', 'E8']:
            b = branching_structure(t)
            bnode = b['branching_node']
            assert b['valences'][bnode] == 3, f"{t}: valence={b['valences'][bnode]}"


# =========================================================================
# 6. SERRE RELATIONS
# =========================================================================

class TestSerreRelations:
    """Test Serre relations for all types."""

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_num_serre_equals_rank_minus_1(self, ade_type):
        """Number of Serre relations = rank - 1.
        # VERIFIED: [DA]
        """
        s = serre_relations(ade_type)
        assert s['correct_num_edges']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_all_degree_2(self, ade_type):
        """All Serre relations have degree 2 (simply-laced).
        # VERIFIED: [DC]
        """
        s = serre_relations(ade_type)
        assert s['all_degree_2']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_mixing_serre_trivial(self, ade_type):
        """Mixing Serre integral vanishes by Mukai orthogonality.
        # VERIFIED: [SY]
        """
        s = serre_relations(ade_type)
        assert s['mixing_serre_trivial']


# =========================================================================
# 7. YANG R-MATRIX
# =========================================================================

class TestYangRMatrix:
    """Test Yang R-matrix for each type."""

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'D5', 'E6'])
    def test_unitarity(self, ade_type):
        """R(u)*R(-u) = (1-u^2)*Id.
        # VERIFIED: [DC]
        """
        result = yang_r_matrix_ade(ade_type)
        assert result['unitarity_holds']

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'D5', 'E6'])
    def test_offdiag_from_P(self, ade_type):
        """Off-diagonal = N*(N-1) from permutation operator.
        # VERIFIED: [DC], [FO]
        """
        result = yang_r_matrix_ade(ade_type)
        assert result['offdiag_matches_formula']

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'D5', 'E6'])
    def test_trace(self, ade_type):
        """tr(R(u)) = u*N^2 + N.
        # VERIFIED: [DC], [FO]
        """
        result = yang_r_matrix_ade(ade_type)
        assert result['trace_matches']

    def test_e7_unitarity(self):
        """E7 Yang R-matrix satisfies unitarity.
        # VERIFIED: [DC]
        """
        result = yang_r_matrix_ade('E7')
        assert result['unitarity_holds']

    def test_e7_offdiag(self):
        """E7 off-diagonal = 56*55 = 3080.
        # VERIFIED: [DC]
        """
        result = yang_r_matrix_ade('E7')
        assert result['offdiagonal_nonzero'] == 56 * 55

    def test_e8_structural(self):
        """E8 properties are structural (matrix not constructed).
        # VERIFIED: [DA]
        """
        result = yang_r_matrix_ade('E8')
        assert not result['R_constructed']
        assert result['offdiagonal_nonzero'] == 248 * 247
        assert result['unitarity_holds']

    @pytest.mark.parametrize("ade_type,expected_N", [
        ('A1', 2), ('A2', 3), ('D4', 8), ('D5', 10),
        ('E6', 27), ('E7', 56), ('E8', 248),
    ])
    def test_dim_V(self, ade_type, expected_N):
        """Defining representation dimension.
        # VERIFIED: [DA]
        """
        result = yang_r_matrix_ade(ade_type)
        assert result['N'] == expected_N


# =========================================================================
# 8. YANG-BAXTER EQUATION
# =========================================================================

class TestYBE:
    """Test Yang-Baxter equation verification."""

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'D5'])
    def test_ybe_numerical(self, ade_type):
        """YBE satisfied numerically for small N.
        # VERIFIED: [DC]
        """
        result = yang_r_ybe_verification(ade_type)
        assert result['ybe_satisfied']
        assert result['verified_numerically']
        assert result['error_norm'] < 1e-10

    def test_ybe_e6_numerical(self):
        """YBE satisfied numerically for E6 (N=27).
        # VERIFIED: [DC]
        """
        result = yang_r_ybe_verification('E6')
        assert result['ybe_satisfied']
        assert result['verified_numerically']

    def test_ybe_e7_analytical(self):
        """E7 YBE guaranteed analytically (N=56 too large for numerical).
        # VERIFIED: [DA]
        """
        result = yang_r_ybe_verification('E7')
        assert result['ybe_satisfied']
        assert not result['verified_numerically']

    def test_ybe_e8_analytical(self):
        """E8 YBE guaranteed analytically (N=248 too large for numerical).
        # VERIFIED: [DA]
        """
        result = yang_r_ybe_verification('E8')
        assert result['ybe_satisfied']
        assert not result['verified_numerically']


# =========================================================================
# 9. K3 EMBEDDING
# =========================================================================

class TestK3Embedding:
    """Test K3 Yangian parameters at each enhancement point."""

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_cy2_constraint(self, ade_type):
        """CY_2 constraint: sum h_i = 0.
        # VERIFIED: [SY]
        """
        result = k3_embedding_parameters(ade_type)
        assert result['cy2_satisfied']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_total_params_24(self, ade_type):
        """Total parameters = 24 (Mukai rank).
        # VERIFIED: [DA]
        """
        result = k3_embedding_parameters(ade_type)
        assert result['total_params'] == 24

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_central_charge_24(self, ade_type):
        """Central charge = 24 at level 1.
        # VERIFIED: [DA]
        """
        result = k3_embedding_parameters(ade_type)
        assert result['central_charge']['c_total_is_24']


# =========================================================================
# 10. STRUCTURE FUNCTION
# =========================================================================

class TestStructureFunction:
    """Test structure function factorization."""

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_factorization(self, ade_type):
        """g_K3(z) = g_ADE(z) * g_compl(z).
        # VERIFIED: [DC]
        """
        result = structure_function_factored(ade_type)
        assert result['factored']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_unitarity(self, ade_type):
        """g(z) * g(-z) = 1.
        # VERIFIED: [DC], [SY]
        """
        result = structure_function_factored(ade_type)
        assert result['unitarity_holds']

    @pytest.mark.parametrize("ade_type", ADE_TYPES_ORDERED)
    def test_total_degree_24(self, ade_type):
        """Total degree = (24, 24).
        # VERIFIED: [DA]
        """
        result = structure_function_factored(ade_type)
        assert result['g_total_degree'] == (24, 24)


# =========================================================================
# 11. A_2 SPECIFIC
# =========================================================================

class TestA2Specific:
    """Test A_2 = sl_3 specific features."""

    def test_rank(self):
        result = a2_specific()
        assert result['rank'] == 2

    def test_dim_g(self):
        result = a2_specific()
        assert result['dim_g'] == 8

    def test_dim_V(self):
        result = a2_specific()
        assert result['dim_V'] == 3

    def test_yang_offdiag_6(self):
        """3x3 Yang R-matrix has 6 off-diagonal entries.
        # VERIFIED: [DC], [FO]: N*(N-1) = 3*2 = 6
        """
        result = a2_specific()
        assert result['yang_r_matrix']['matches']
        assert result['yang_r_matrix']['offdiagonal_nonzero'] == 6

    def test_ybe(self):
        """Yang R-matrix satisfies YBE.
        # VERIFIED: [DC]
        """
        result = a2_specific()
        assert result['yang_r_matrix']['ybe_satisfied']

    def test_unitarity(self):
        result = a2_specific()
        assert result['yang_r_matrix']['unitarity_holds']

    def test_one_serre_relation(self):
        """A2 has 1 Serre relation.
        # VERIFIED: [DA]: rank - 1 = 1
        """
        result = a2_specific()
        assert result['serre']['num_relations'] == 1

    def test_z2_outer(self):
        """A2 has Z_2 outer automorphism (charge conjugation).
        # VERIFIED: [DC]
        """
        result = a2_specific()
        assert 'Z_2' in result['outer_aut']

    def test_k3_offdiag_144(self):
        """A2 has 144 off-diagonal in 324x324.
        # VERIFIED: [FO]
        """
        result = a2_specific()
        assert result['k3_offdiag_324'] == 144

    def test_c_level1(self):
        """c(sl_3, k=1) = 8/4 = 2.
        # VERIFIED: [DA]
        """
        result = a2_specific()
        assert result['c_level1'] == '2'


# =========================================================================
# 12. D_5 SPECIFIC
# =========================================================================

class TestD5Specific:
    """Test D_5 = so_{10} specific features."""

    def test_rank(self):
        result = d5_specific()
        assert result['rank'] == 5

    def test_dim_g(self):
        result = d5_specific()
        assert result['dim_g'] == 45

    def test_dim_V(self):
        result = d5_specific()
        assert result['dim_V'] == 10

    def test_no_triality(self):
        """D5 does NOT have triality (unique to D4).
        # VERIFIED: [DC]: Out(D_5) = Z_2, not S_3
        """
        result = d5_specific()
        assert result['no_triality']
        assert result['triality_unique_to_d4']

    def test_z2_outer(self):
        """D5 has Z_2 outer automorphism (spinor swap).
        # VERIFIED: [DC]
        """
        result = d5_specific()
        assert 'Z_2' in result['outer_aut']

    def test_yang_offdiag_90(self):
        """10x10 Yang R-matrix has 90 off-diagonal entries.
        # VERIFIED: [DC], [FO]: N*(N-1) = 10*9 = 90
        """
        result = d5_specific()
        assert result['yang_r_matrix']['matches']
        assert result['yang_r_matrix']['offdiagonal_nonzero'] == 90

    def test_unitarity(self):
        result = d5_specific()
        assert result['yang_r_matrix']['unitarity_holds']

    def test_spinor_dim_16(self):
        """D5 spinor dimension = 2^4 = 16.
        # VERIFIED: [DA]: 2^{n-1} for D_n
        """
        result = d5_specific()
        assert result['spinor_dim'] == 16

    def test_fork_structure(self):
        """D5 has fork structure.
        # VERIFIED: [DC]
        """
        result = d5_specific()
        assert result['branching']['is_fork']
        assert result['branching']['diagram_type'] == 'fork_D'

    def test_k3_offdiag_510(self):
        """D5 has 510 off-diagonal in 324x324.
        # VERIFIED: [FO]
        """
        result = d5_specific()
        assert result['k3_offdiag_324'] == 510

    def test_c_level1(self):
        """c(so_{10}, k=1) = 45/9 = 5.
        # VERIFIED: [DA]
        """
        result = d5_specific()
        assert result['c_level1'] == '5'

    def test_four_serre_relations(self):
        """D5 has 4 Serre relations (rank - 1 = 4).
        # VERIFIED: [DA]
        """
        result = d5_specific()
        assert result['serre']['num_relations'] == 4


# =========================================================================
# 13. E_6 SPECIFIC
# =========================================================================

class TestE6Specific:
    """Test E_6 specific features: 27-dim fundamental."""

    def test_rank(self):
        result = e6_specific()
        assert result['rank'] == 6

    def test_dim_g(self):
        result = e6_specific()
        assert result['dim_g'] == 78

    def test_dim_V_27(self):
        """E6 fundamental is 27-dimensional.
        # VERIFIED: [DA]
        """
        result = e6_specific()
        assert result['dim_V'] == 27

    def test_yang_offdiag_702(self):
        """27x27 Yang R-matrix has 702 off-diagonal entries.
        # VERIFIED: [DC], [FO]: 27*26 = 702
        """
        result = e6_specific()
        assert result['yang_r_matrix']['matches']
        assert result['yang_r_matrix']['offdiagonal_nonzero'] == 702

    def test_unitarity(self):
        result = e6_specific()
        assert result['yang_r_matrix']['unitarity_holds']

    def test_z2_outer(self):
        """E6 has Z_2 outer automorphism (diagram flip).
        # VERIFIED: [DC]
        """
        result = e6_specific()
        assert 'Z_2' in result['outer_aut']

    def test_cubic_surface_27_lines(self):
        """27 of E_6 parametrizes lines on a cubic surface.
        # VERIFIED: [DA]
        """
        result = e6_specific()
        assert result['exceptional_geometry']['cubic_surface_lines'] == 27

    def test_k3_offdiag_810(self):
        """E6 has 810 off-diagonal in 324x324.
        # VERIFIED: [FO]
        """
        result = e6_specific()
        assert result['k3_offdiag_324'] == 810

    def test_c_level1(self):
        """c(E_6, k=1) = 78/13 = 6.
        # VERIFIED: [DA]
        """
        result = e6_specific()
        assert result['c_level1'] == '6'


# =========================================================================
# 14. E_7 SPECIFIC
# =========================================================================

class TestE7Specific:
    """Test E_7 specific features: 56-dim fundamental."""

    def test_rank(self):
        result = e7_specific()
        assert result['rank'] == 7

    def test_dim_g(self):
        result = e7_specific()
        assert result['dim_g'] == 133

    def test_dim_V_56(self):
        """E7 fundamental is 56-dimensional.
        # VERIFIED: [DA]
        """
        result = e7_specific()
        assert result['dim_V'] == 56

    def test_yang_offdiag_3080(self):
        """56x56 Yang R-matrix has 3080 off-diagonal entries.
        # VERIFIED: [DC], [FO]: 56*55 = 3080
        """
        result = e7_specific()
        assert result['yang_r_matrix']['matches']
        assert result['yang_r_matrix']['offdiagonal_nonzero'] == 3080

    def test_unitarity(self):
        result = e7_specific()
        assert result['yang_r_matrix']['unitarity_holds']

    def test_trivial_outer(self):
        """E7 has trivial outer automorphism.
        # VERIFIED: [DC]
        """
        result = e7_specific()
        assert 'trivial' in result['outer_aut']

    def test_self_dual(self):
        """56 is self-dual.
        # VERIFIED: [DA]
        """
        result = e7_specific()
        assert result['self_dual']

    def test_k3_offdiag_1218(self):
        """E7 has 1218 off-diagonal in 324x324.
        # VERIFIED: [FO]
        """
        result = e7_specific()
        assert result['k3_offdiag_324'] == 1218


# =========================================================================
# 15. E_8 SPECIFIC
# =========================================================================

class TestE8Specific:
    """Test E_8 specific features: adjoint = smallest rep."""

    def test_rank(self):
        result = e8_specific()
        assert result['rank'] == 8

    def test_dim_g(self):
        result = e8_specific()
        assert result['dim_g'] == 248

    def test_dim_V_248(self):
        """E8 fundamental = adjoint = 248.
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert result['dim_V'] == 248

    def test_adjoint_equals_fundamental(self):
        """E8 is the ONLY type where adjoint = fundamental.
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert result['adjoint_equals_fundamental']

    def test_trivial_outer(self):
        """E8 has trivial outer automorphism.
        # VERIFIED: [DC]
        """
        result = e8_specific()
        assert 'trivial' in result['outer_aut']

    def test_trivial_center(self):
        """E8 has trivial center.
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert 'trivial' in result['center']

    def test_terminal(self):
        """E8 is the terminal case (max rank for ADE on K3).
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert result['terminal_case']

    def test_k3_offdiag_1764(self):
        """E8 has 1764 off-diagonal in 324x324 (maximum).
        # VERIFIED: [FO]
        """
        result = e8_specific()
        assert result['k3_offdiag_324'] == 1764

    def test_yang_offdiag_61256(self):
        """248x248 Yang R-matrix has 61256 off-diagonal entries.
        # VERIFIED: [FO]: 248*247 = 61256
        """
        result = e8_specific()
        assert result['yang_r_matrix']['offdiagonal_from_P'] == 248 * 247

    def test_c_level1(self):
        """c(E_8, k=1) = 248/31 = 8.
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert result['c_level1'] == '8'

    def test_matrix_not_constructed(self):
        """E8 matrix is NOT explicitly constructed (too large).
        # VERIFIED: [DA]
        """
        result = e8_specific()
        assert result['yang_r_matrix']['matrix_not_constructed']


# =========================================================================
# 16. OUTER AUTOMORPHISMS
# =========================================================================

class TestOuterAutomorphisms:
    """Test outer automorphism landscape."""

    def test_d4_unique_s3(self):
        """D4 is the only type with S_3 outer automorphism.
        # VERIFIED: [DC]
        """
        result = outer_automorphism_landscape()
        assert result['d4_triality_unique']
        assert result['max_outer_type'] == 'D4'
        assert result['max_outer_order'] == 6

    def test_trivial_outer_types(self):
        """A1, E7, E8 have trivial outer automorphisms.
        # VERIFIED: [DC]
        """
        result = outer_automorphism_landscape()
        assert 'A1' in result['trivial_outer']
        assert 'E7' in result['trivial_outer']
        assert 'E8' in result['trivial_outer']

    def test_z2_types(self):
        """A2, D5, E6 have Z_2 outer automorphisms.
        # VERIFIED: [DC]
        """
        result = outer_automorphism_landscape()
        for t in ['A2', 'D5', 'E6']:
            assert t in result['nontrivial_outer']
            assert OUTER_AUTOMORPHISMS[t]['order'] == 2


# =========================================================================
# 17. GROWTH ANALYSIS
# =========================================================================

class TestGrowthAnalysis:
    """Test the growth pattern analysis."""

    def test_data_has_all_types(self):
        result = offdiag_growth_analysis()
        assert len(result['data']) == 7

    def test_ade_two_dominates_at_e8(self):
        """ADE two-point block dominates at E8.
        # VERIFIED: [CF]
        """
        result = offdiag_growth_analysis()
        assert result['ade_two_dominates_at_e8']

    def test_increments_positive(self):
        """All increments are positive (monotonic).
        # VERIFIED: [CF]
        """
        result = offdiag_growth_analysis()
        for inc in result['increments']:
            assert inc['increment'] > 0


# =========================================================================
# 18. MASTER SUMMARY
# =========================================================================

class TestMasterSummary:
    """Test the complete master summary."""

    def test_all_central_charge_24(self):
        """All types have total central charge 24.
        # VERIFIED: [DA]
        """
        result = master_all_ade()
        assert result['key_findings']['all_central_charge_24']

    def test_all_cy2_satisfied(self):
        """All types satisfy CY_2 constraint.
        # VERIFIED: [SY]
        """
        result = master_all_ade()
        assert result['key_findings']['all_cy2_satisfied']

    def test_all_yang_unitarity(self):
        """All Yang R-matrices satisfy unitarity.
        # VERIFIED: [DC]
        """
        result = master_all_ade()
        assert result['key_findings']['all_yang_unitarity']

    def test_monotonic(self):
        """Off-diagonal count is monotonic in rank.
        # VERIFIED: [CF]
        """
        result = master_all_ade()
        assert result['key_findings']['offdiag_monotonic_in_rank']

    def test_offdiag_range(self):
        """Range is 48 (A1) to 1764 (E8).
        # VERIFIED: [FO]
        """
        result = master_all_ade()
        assert '48' in result['key_findings']['offdiag_range']
        assert '1764' in result['key_findings']['offdiag_range']

    def test_all_types_present(self):
        """All seven types in summary.
        # VERIFIED: [DA]
        """
        result = master_all_ade()
        for t in ADE_TYPES_ORDERED:
            assert t in result['type_summaries']


# =========================================================================
# 19. CROSS-CHECKS WITH EXISTING ENGINES
# =========================================================================

class TestCrossChecks:
    """Cross-checks with k3_nonabelian_rmatrix_a1 and k3_yangian_d4_triality."""

    def test_a1_offdiag_48(self):
        """A1 off-diagonal = 48 matches k3_nonabelian_rmatrix_a1.
        # VERIFIED: [LC]
        """
        result = offdiagonal_count_general('A1')
        assert result['off_diagonal']['total'] == 48

    def test_d4_offdiag_294(self):
        """D4 off-diagonal = 294.
        # VERIFIED: [LC]
        """
        result = offdiagonal_count_general('D4')
        assert result['off_diagonal']['total'] == 294

    def test_d4_dim_V_8(self):
        """D4 vector rep is 8-dimensional (matches k3_yangian_d4_triality).
        # VERIFIED: [LC]
        """
        assert FULL_ADE_DATA['D4']['dim_V'] == 8

    def test_d4_triality_s3(self):
        """D4 has S_3 outer automorphism (triality).
        # VERIFIED: [LC]
        """
        assert OUTER_AUTOMORPHISMS['D4']['order'] == 6
        assert OUTER_AUTOMORPHISMS['D4']['group'] == 'S_3'

    def test_a1_dim_g_3(self):
        """A1 = sl_2 has dim 3.
        # VERIFIED: [LC]
        """
        assert FULL_ADE_DATA['A1']['dim_g'] == 3

    def test_ade_data_consistency_with_level1(self):
        """FULL_ADE_DATA consistent with ade_yangian_level1 for all types.
        # VERIFIED: [LC]
        """
        from compute.lib.ade_yangian_level1 import ade_data as ade_data_func
        for label in ADE_TYPES_ORDERED:
            our = FULL_ADE_DATA[label]
            theirs = ade_data_func(label)
            assert our['rank'] == theirs.rank, f"{label} rank mismatch"
            assert our['dim_g'] == theirs.dim_g, f"{label} dim_g mismatch"
            assert our['dim_V'] == theirs.dim_V, f"{label} dim_V mismatch"
            assert our['h_dual'] == theirs.dual_coxeter, f"{label} h_dual mismatch"
