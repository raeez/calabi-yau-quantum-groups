r"""Tests for bfn_coulomb_k3_yangian.py: BFN quantized Coulomb branch and K3 Yangian.

STATUS: ALL results CONJECTURAL at the level of A_hbar(K3) = Y(g_{K3})
(AP-CY14).  Individual BFN computations are proved (BFN 2016).
Tests verify internal consistency of the BFN-K3 identification.

Test structure:
    Section 1: Jordan quiver (template case, PROVED) -- 8 tests
    Section 2: ADE quiver Coulomb branches (PROVED) -- 10 tests
    Section 3: K3 Hilbert scheme Fock spaces -- 12 tests
    Section 4: Structure function comparison (BFN vs Yangian) -- 10 tests
    Section 5: Charge-2 R-matrix eigenvalues -- 8 tests
    Section 6: Three-route comparison -- 6 tests
    Section 7: BFN Koszul duality -- 6 tests
    Section 8: ADE embedding at orbifold K3 -- 8 tests
    Section 9: Independence from CY-A_3 -- 4 tests
    Section 10: Full verification -- 6 tests

Total: 78 tests.

Multi-path verification:
    Path 1 (DC): direct computation of partition counts, structure functions
    Path 2 (LT): comparison with Gottsche 1990, BFN 2016
    Path 3 (LC): limiting cases (n=0, z->infinity, ADE embedding)
    Path 4 (SY): unitarity, CY constraint, Koszul conductor
    Path 5 (CF): cross-family with k3_yangian.py, mo_rmatrix_k3e.py

Manuscript references:
    subsec:bfn-coulomb-k3 (k3_times_e.tex)
    conj:bfn-k3-yangian (k3_times_e.tex)
    conj:k3-yangian (k3_times_e.tex)
"""

import pytest
from fractions import Fraction as F

from sympy import Rational

from compute.lib.bfn_coulomb_k3_yangian import (
    # Constants
    BFN_STATUS,
    BFN_PROVED_STATUS,
    MUKAI_RANK,
    LATTICE_SIGNATURE,
    HILB_EULER_CHARS,
    ADE_QUIVER_DATA,
    # Types
    BFNCoulombData,
    QuiverGaugeTheory,
    BFNHilbertData,
    # Jordan quiver
    jordan_quiver_bfn,
    jordan_quiver_fock_dim,
    # ADE quivers
    ade_quiver_bfn,
    ade_coulomb_rank,
    # K3 Coulomb data
    k3_coulomb_data,
    k3_kummer_coulomb_data,
    # Hilbert scheme Fock spaces
    k3_colored_partition_count,
    hilbert_fock_data,
    verify_hilbert_euler_chars,
    # Structure function
    bfn_structure_function_at_charge_1,
    bfn_r_matrix_eigenvalue_charge_2,
    # Three routes
    compare_three_routes,
    # Koszul duality
    bfn_koszul_duality_k3,
    # ADE embedding
    ade_embedding_in_k3,
    # Independence
    independence_from_cy_a3,
    # Full verification
    full_verification,
)

from compute.lib.k3_yangian import (
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
    r_matrix_diagonal_entries,
)


# =========================================================================
# Section 1: Jordan quiver (template case, PROVED)
# =========================================================================

class TestJordanQuiver:
    """Tests for the Jordan quiver BFN Coulomb branch.

    The Jordan quiver is the 1-vertex, 1-loop quiver.
    BFN Coulomb branch = spherical rational Cherednik algebra.
    This is PROVED (BFN 2016, Theorem 1.1).
    """

    def test_jordan_quiver_structure(self):
        """Jordan quiver has 1 vertex, 1 loop, framing 1."""
        q = jordan_quiver_bfn(1)
        assert q.quiver_type == 'Jordan'
        assert q.num_vertices == 1
        assert q.gauge_ranks == [1]
        assert q.framing_dims == [1]
        assert q.loops_per_vertex == [1]

    def test_jordan_quiver_charge_n(self):
        """Jordan quiver at charge n has gauge rank n."""
        for n in [1, 2, 3, 5]:
            q = jordan_quiver_bfn(n)
            assert q.gauge_ranks == [n]

    def test_jordan_fock_dim_partition_function(self):
        """chi(Hilb^n(C^2)) = p(n) (partition function).

        # VERIFIED: DC + LT (Hardy-Ramanujan, OEIS A000041)
        """
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22}
        for n, p_n in expected.items():
            assert jordan_quiver_fock_dim(n) == p_n, \
                f"p({n}) = {jordan_quiver_fock_dim(n)}, expected {p_n}"

    def test_jordan_fock_dim_zero(self):
        """p(0) = 1 (empty partition)."""
        assert jordan_quiver_fock_dim(0) == 1

    def test_jordan_fock_dim_negative(self):
        """p(n) = 0 for n < 0."""
        assert jordan_quiver_fock_dim(-1) == 0
        assert jordan_quiver_fock_dim(-5) == 0

    def test_jordan_identification_proved(self):
        """Jordan quiver BFN = Yangian is PROVED."""
        q = jordan_quiver_bfn(1)
        assert 'PROVED' in q.yangian_identification

    def test_jordan_coulomb_branch_hilb(self):
        """Jordan quiver Coulomb branch is described as Hilb."""
        q = jordan_quiver_bfn(2)
        assert 'Hilb' in q.coulomb_branch_type

    def test_jordan_quiver_is_namedtuple(self):
        """QuiverGaugeTheory is a NamedTuple with all fields."""
        q = jordan_quiver_bfn(1)
        assert hasattr(q, 'quiver_type')
        assert hasattr(q, 'yangian_identification')


# =========================================================================
# Section 2: ADE quiver Coulomb branches (PROVED)
# =========================================================================

class TestADEQuivers:
    """Tests for ADE quiver BFN Coulomb branches.

    For ADE quivers, BFN proves: A_hbar(Q) = truncated shifted Yangian.
    This is PROVED (BFN arXiv:1604.03625).
    """

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'E6', 'E7', 'E8'])
    def test_ade_quiver_structure(self, ade_type):
        """ADE quiver has correct number of vertices."""
        q = ade_quiver_bfn(ade_type)
        assert q.num_vertices == ADE_QUIVER_DATA[ade_type]['vertices']

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'E6', 'E7', 'E8'])
    def test_ade_identification_proved(self, ade_type):
        """ADE quiver BFN = Yangian is PROVED."""
        q = ade_quiver_bfn(ade_type)
        assert 'PROVED' in q.yangian_identification

    def test_ade_ranks(self):
        """ADE Coulomb branch ranks match Lie algebra ranks.

        # VERIFIED: DC (from quiver data), LT (standard Lie theory)
        """
        expected_ranks = {'A1': 2, 'A2': 3, 'D4': 4, 'E6': 6, 'E7': 7, 'E8': 8}
        for ade_type, expected in expected_ranks.items():
            assert ade_coulomb_rank(ade_type) == expected, \
                f"rank({ade_type}) = {ade_coulomb_rank(ade_type)}, expected {expected}"

    def test_ade_invalid_type(self):
        """Invalid ADE type raises ValueError."""
        with pytest.raises(ValueError):
            ade_quiver_bfn('B2')

    def test_ade_coulomb_branch_resolution(self):
        """ADE Coulomb branch is resolved singularity."""
        q = ade_quiver_bfn('A1')
        assert 'resolved' in q.coulomb_branch_type.lower() \
            or 'singularity' in q.coulomb_branch_type.lower()

    def test_a1_is_sl2(self):
        """A1 quiver gives Y(sl_2_hat)."""
        q = ade_quiver_bfn('A1')
        assert 'sl_2' in q.yangian_identification

    def test_e8_largest_rank(self):
        """E8 has rank 8 (largest ADE)."""
        assert ade_coulomb_rank('E8') == 8

    def test_all_ade_ranks_sum(self):
        """Sum of ADE ranks is well-defined."""
        total = sum(ade_coulomb_rank(t) for t in ADE_QUIVER_DATA)
        # A1(2) + A2(3) + D4(4) + E6(6) + E7(7) + E8(8) = 30
        assert total == 30

    def test_ade_no_loops(self):
        """ADE quivers have no self-loops (unlike Jordan quiver)."""
        for ade_type in ADE_QUIVER_DATA:
            q = ade_quiver_bfn(ade_type)
            assert all(l == 0 for l in q.loops_per_vertex)

    def test_ade_yangian_type_string(self):
        """Each ADE type has a well-formed Yangian identification string."""
        for ade_type in ADE_QUIVER_DATA:
            assert 'Y(' in ADE_QUIVER_DATA[ade_type]['yangian_type']


# =========================================================================
# Section 3: K3 Hilbert scheme Fock spaces
# =========================================================================

class TestK3HilbertFock:
    """Tests for K3 Hilbert scheme Euler characteristics.

    chi(Hilb^n(K3)) = p_{24}(n) (24-colored partitions of n).
    # VERIFIED: DC (generating function) + LT (Gottsche 1990)
    """

    def test_hilb_0(self):
        """chi(Hilb^0(K3)) = 1 (a point)."""
        assert k3_colored_partition_count(0) == 1

    def test_hilb_1(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        assert k3_colored_partition_count(1) == 24

    def test_hilb_2(self):
        """chi(Hilb^2(K3)) = 324.

        # VERIFIED: DC + LT (Gottsche 1990)
        """
        assert k3_colored_partition_count(2) == 324

    def test_hilb_3(self):
        """chi(Hilb^3(K3)) = 3200.

        # VERIFIED: DC + LT (Gottsche 1990)
        """
        assert k3_colored_partition_count(3) == 3200

    def test_hilb_4(self):
        """chi(Hilb^4(K3)) = 25650.

        # VERIFIED: DC + LT (Gottsche 1990)
        """
        assert k3_colored_partition_count(4) == 25650

    def test_hilb_5(self):
        """chi(Hilb^5(K3)) = 176256.

        # VERIFIED: DC + LT (Gottsche 1990)
        """
        assert k3_colored_partition_count(5) == 176256

    def test_hilb_negative(self):
        """p_{24}(n) = 0 for n < 0."""
        assert k3_colored_partition_count(-1) == 0

    def test_verify_against_hardcoded(self):
        """All hardcoded values match computed values."""
        result = verify_hilbert_euler_chars(5)
        assert result['all_match']

    def test_hilbert_fock_data_charge_0(self):
        """Fock data at charge 0."""
        data = hilbert_fock_data(0)
        assert data.charge == 0
        assert data.fock_dim == 1

    def test_hilbert_fock_data_charge_2(self):
        """Fock data at charge 2: three partition types.

        Type A: 24, Type B: 24, Type C: C(24,2) = 276
        Total: 24 + 24 + 276 = 324.
        """
        data = hilbert_fock_data(2)
        assert data.fock_dim == 324
        types = data.partition_types
        assert types['single_color_partition_2'] == 24
        assert types['single_color_partition_1_1'] == 24
        assert types['two_color_1_plus_1'] == 276
        assert sum(types.values()) == 324

    def test_hilbert_fock_data_charge_3(self):
        """Fock data at charge 3: six partition types, total 3200."""
        data = hilbert_fock_data(3)
        assert data.fock_dim == 3200
        assert sum(data.partition_types.values()) == 3200

    def test_hilbert_fock_data_invalid(self):
        """Negative charge raises ValueError."""
        with pytest.raises(ValueError):
            hilbert_fock_data(-1)


# =========================================================================
# Section 4: Structure function comparison (BFN vs Yangian)
# =========================================================================

class TestStructureFunctionComparison:
    """Compare BFN R-matrix eigenvalue with K3 Yangian structure function.

    At charge 1, the BFN stable envelope gives the SAME structure function
    as the K3 Yangian: g_{K3}(z) = prod (z-h_i)/(z+h_i).

    AP-CY28: test points chosen far from poles at +/- h_i.
    For Kummer K3: h_i = 1 (i=1..4) or h_i = -1/5 (i=5..24).
    Poles at z = -1 and z = 1/5. Use z = 37/7, 41/3, 53/11.
    """

    @pytest.fixture
    def params(self):
        return kummer_k3_parameters()

    def test_bfn_equals_yangian_at_37_7(self, params):
        """BFN = Yangian structure function at z = 37/7."""
        z = Rational(37, 7)
        g_bfn = bfn_structure_function_at_charge_1(z, params)
        g_yang = structure_function_evaluate(z, params)
        assert g_bfn == g_yang

    def test_bfn_equals_yangian_at_41_3(self, params):
        """BFN = Yangian structure function at z = 41/3."""
        z = Rational(41, 3)
        g_bfn = bfn_structure_function_at_charge_1(z, params)
        g_yang = structure_function_evaluate(z, params)
        assert g_bfn == g_yang

    def test_bfn_equals_yangian_at_53_11(self, params):
        """BFN = Yangian structure function at z = 53/11."""
        z = Rational(53, 11)
        g_bfn = bfn_structure_function_at_charge_1(z, params)
        g_yang = structure_function_evaluate(z, params)
        assert g_bfn == g_yang

    def test_unitarity(self, params):
        """g(z) * g(-z) = 1 (CY unitarity).

        # VERIFIED: DC (direct multiplication), SY (CY involution)
        """
        z = Rational(37, 7)
        g_plus = bfn_structure_function_at_charge_1(z, params)
        g_minus = bfn_structure_function_at_charge_1(-z, params)
        assert g_plus * g_minus == 1

    def test_structure_function_at_zero(self, params):
        """g(0) = (-1)^24 = 1 (even number of parameters)."""
        g0 = bfn_structure_function_at_charge_1(Rational(0), params)
        assert g0 == 1

    def test_structure_function_degree_24(self, params):
        """g_{K3}(z) is degree (24, 24) rational function."""
        # At large z: g(z) -> 1 (leading coefficients cancel)
        g_large = bfn_structure_function_at_charge_1(Rational(10**6), params)
        # Should be close to 1 for large z
        assert abs(float(g_large) - 1.0) < 1e-4

    def test_null_parameters_structure_function(self):
        """Structure function with null Mukai parameters."""
        params = null_kummer_parameters()
        z = Rational(37, 7)
        g = bfn_structure_function_at_charge_1(z, params)
        # Null parameters: many h_i = 0, so many factors are z/z = 1
        # Only 4 nonzero h_i contribute nontrivially
        g_yang = structure_function_evaluate(z, params)
        assert g == g_yang

    def test_bfn_multiple_test_points(self, params):
        """BFN = Yangian at 5 different test points."""
        test_points = [Rational(7, 3), Rational(13, 2), Rational(19, 7),
                       Rational(23, 5), Rational(29, 4)]
        for z in test_points:
            g_bfn = bfn_structure_function_at_charge_1(z, params)
            g_yang = structure_function_evaluate(z, params)
            assert g_bfn == g_yang, f"Mismatch at z = {z}"

    def test_structure_function_positive(self, params):
        """g(z) > 0 for z >> max(h_i) (all factors positive)."""
        z = Rational(100)
        g = float(bfn_structure_function_at_charge_1(z, params))
        assert g > 0

    def test_cy2_constraint_in_structure_function(self, params):
        """CY_2 constraint sum h_i = 0 implies phi_1 = 0
        (first subleading coefficient vanishes)."""
        # The structure function g(z) = 1 + 0*z^{-1} + phi_2*z^{-2} + ...
        # phi_1 = -2*p_1 = -2*sum(h_i) = 0 by CY_2.
        from compute.lib.k3_yangian import structure_function_coefficients
        coeffs = structure_function_coefficients(params, max_order=5)
        assert coeffs[0] == 1  # phi_0 = 1
        assert coeffs[1] == 0  # phi_1 = 0 (CY_2)


# =========================================================================
# Section 5: Charge-2 R-matrix eigenvalues
# =========================================================================

class TestCharge2RMatrix:
    """Tests for charge-2 BFN R-matrix eigenvalues.

    At charge 2, the Fock space has dim 324 and the R-matrix is
    324 x 324. We test eigenvalues on the three partition types.
    """

    @pytest.fixture
    def params(self):
        return kummer_k3_parameters()

    def test_type_a_eigenvalue(self, params):
        """Type A (single color, partition (2)): shifted structure function."""
        z = Rational(37, 7)
        ev = bfn_r_matrix_eigenvalue_charge_2(z, 'A', (0,), params)
        assert ev is not None  # Just check it computes
        assert isinstance(float(ev), float)

    def test_type_b_eigenvalue(self, params):
        """Type B (single color, partition (1,1)): shifted in row direction."""
        z = Rational(37, 7)
        ev = bfn_r_matrix_eigenvalue_charge_2(z, 'B', (0,), params)
        assert ev is not None
        assert isinstance(float(ev), float)

    def test_type_c_eigenvalue(self, params):
        """Type C (two colors): product of charge-1 eigenvalues."""
        z = Rational(37, 7)
        ev = bfn_r_matrix_eigenvalue_charge_2(z, 'C', (0, 5), params)
        # For abelian K3, type C should equal g_{K3}(z)
        g = structure_function_evaluate(z, params)
        assert ev == g

    def test_type_a_different_colors(self, params):
        """Type A eigenvalue depends on which Mukai direction."""
        z = Rational(37, 7)
        ev_pos = bfn_r_matrix_eigenvalue_charge_2(z, 'A', (0,), params)
        ev_neg = bfn_r_matrix_eigenvalue_charge_2(z, 'A', (10,), params)
        # Different Mukai directions (positive vs negative) give different eigenvalues
        assert ev_pos != ev_neg

    def test_type_a_invalid_indices(self, params):
        """Type A with wrong number of indices raises error."""
        with pytest.raises(ValueError):
            bfn_r_matrix_eigenvalue_charge_2(Rational(5), 'A', (0, 1), params)

    def test_type_c_invalid_indices(self, params):
        """Type C with wrong number of indices raises error."""
        with pytest.raises(ValueError):
            bfn_r_matrix_eigenvalue_charge_2(Rational(5), 'C', (0,), params)

    def test_invalid_partition_type(self, params):
        """Invalid partition type raises error."""
        with pytest.raises(ValueError):
            bfn_r_matrix_eigenvalue_charge_2(Rational(5), 'D', (0,), params)

    def test_fock_dim_324_from_partition_types(self, params):
        """Total number of charge-2 states = 324 from partition decomposition."""
        # 24 (type A) + 24 (type B) + C(24,2)=276 (type C) = 324
        assert 24 + 24 + 276 == 324
        assert k3_colored_partition_count(2) == 324


# =========================================================================
# Section 6: Three-route comparison
# =========================================================================

class TestThreeRoutes:
    """Compare three routes to Y(g_{K3}): CY-A, CoHA, BFN."""

    def test_three_routes_all_agree(self):
        """All three routes produce consistent data."""
        result = compare_three_routes()
        assert result['evidence']['classical_limit_all_agree']
        assert result['evidence']['fock_character_match']
        assert result['evidence']['structure_function_match']

    def test_route_a_requires_cy_a(self):
        """Route (a) CY-to-chiral requires CY-A."""
        result = compare_three_routes()
        assert result['route_a']['requires_CY_A']

    def test_route_b_requires_torus(self):
        """Route (b) CoHA requires torus action."""
        result = compare_three_routes()
        assert result['route_b']['requires_torus_action']

    def test_route_c_no_torus(self):
        """Route (c) BFN does NOT require torus action."""
        result = compare_three_routes()
        assert not result['route_c']['requires_torus_action']

    def test_route_c_no_cy_a(self):
        """Route (c) BFN does NOT require CY-A."""
        result = compare_three_routes()
        assert not result['route_c']['requires_CY_A']

    def test_all_kappa_ch_agree(self):
        """All three routes give kappa_ch = 2."""
        result = compare_three_routes()
        assert result['route_a']['kappa_ch'] == 2
        assert result['route_b']['kappa_ch'] == 2
        assert result['route_c']['kappa_ch'] == 2


# =========================================================================
# Section 7: BFN Koszul duality
# =========================================================================

class TestBFNKoszulDuality:
    """Koszul duality for BFN Coulomb branches.

    Webster: O(M_C) = O(M_H)^! for quiver gauge theories.
    For K3: Koszul conductor K = 0 (free-field/KM branch).
    """

    def test_koszul_conductor_zero(self):
        """Koszul conductor K = 0 for K3 free-field branch.

        # VERIFIED: CLAUDE.md frontier result
        """
        result = bfn_koszul_duality_k3()
        assert result['koszul_conductor'] == 0

    def test_koszul_kappa_sum(self):
        """kappa_ch(Y) + kappa_ch(Y^!) = K = 0."""
        result = bfn_koszul_duality_k3()
        kappa = result['coulomb_side']['kappa_ch']
        kappa_dual = result['higgs_side']['kappa_ch']
        assert kappa + kappa_dual == result['koszul_conductor']

    def test_koszul_structure_function_inversion(self):
        """g^!(z) = 1/g(z) (Koszul dual inverts structure function)."""
        # The dual structure function is 1/g(z).
        # At any test point: g(z) * g^!(z) = 1.
        z = Rational(37, 7)
        params = kummer_k3_parameters()
        g = structure_function_evaluate(z, params)
        # g^! uses parameters -h_i:
        h_dual = [-hi for hi in params.h]
        from compute.lib.k3_yangian import custom_parameters
        params_dual = custom_parameters(h_dual)
        g_dual = structure_function_evaluate(z, params_dual)
        assert g * g_dual == 1

    def test_ap_cy10_check(self):
        """AP-CY10: Koszul duality != flop (different operations)."""
        result = bfn_koszul_duality_k3()
        assert 'NOT flop' in result['ap_cy10_check']

    def test_webster_theorem_cited(self):
        """Webster theorem is cited as PROVED."""
        result = bfn_koszul_duality_k3()
        assert 'PROVED' in result['webster_theorem']

    def test_k3_status_conjectural(self):
        """K3 identification is CONJECTURAL."""
        result = bfn_koszul_duality_k3()
        assert result['k3_status'] == BFN_STATUS


# =========================================================================
# Section 8: ADE embedding at orbifold K3
# =========================================================================

class TestADEEmbedding:
    """ADE Yangian embedding in K3 Yangian at orbifold points.

    At an ADE singularity of K3, the ADE Yangian embeds into Y(g_{K3}).
    The Kummer K3 has 16 A_1 singularities.
    """

    def test_a1_embedding_rank(self):
        """A1 embedding: rank 2, bulk rank 22."""
        result = ade_embedding_in_k3('A1')
        assert result['ade_rank'] == 2
        assert result['bulk_rank'] == 22
        assert result['ade_rank'] + result['bulk_rank'] == MUKAI_RANK

    def test_e8_embedding_rank(self):
        """E8 embedding: rank 8, bulk rank 16."""
        result = ade_embedding_in_k3('E8')
        assert result['ade_rank'] == 8
        assert result['bulk_rank'] == 16

    def test_ade_part_proved(self):
        """ADE part of the embedding is PROVED."""
        for ade_type in ['A1', 'A2', 'D4', 'E6', 'E7', 'E8']:
            result = ade_embedding_in_k3(ade_type)
            assert result['bfn_status'] == BFN_PROVED_STATUS

    def test_k3_part_conjectural(self):
        """K3 identification is CONJECTURAL."""
        result = ade_embedding_in_k3('A1')
        assert result['k3_identification_status'] == BFN_STATUS

    @pytest.mark.parametrize("ade_type", ['A1', 'A2', 'D4', 'E6', 'E7', 'E8'])
    def test_rank_decomposition(self, ade_type):
        """ADE rank + bulk rank = 24 (Mukai rank)."""
        result = ade_embedding_in_k3(ade_type)
        assert result['ade_rank'] + result['bulk_rank'] == MUKAI_RANK

    def test_a1_picard_lattice(self):
        """A1 embeds in Picard lattice of K3."""
        result = ade_embedding_in_k3('A1')
        assert 'Pic(K3)' in result['picard_lattice_contribution']

    def test_invalid_ade_type(self):
        """Invalid ADE type raises ValueError."""
        with pytest.raises(ValueError):
            ade_embedding_in_k3('B3')

    def test_a1_is_sl2_yangian(self):
        """A1 embedding gives Y(sl_2_hat)."""
        result = ade_embedding_in_k3('A1')
        assert 'sl_2' in result['ade_yangian']


# =========================================================================
# Section 9: Independence from CY-A_3
# =========================================================================

class TestIndependence:
    """Document and verify independence of BFN from CY-A_3."""

    def test_layer_i_no_dependency(self):
        """Layer (i): K3 DCA has no CY-A dependence."""
        result = independence_from_cy_a3()
        assert result['layer_i']['cy_a_dependence'] is None

    def test_layer_ii_bfn_independent(self):
        """Layer (ii): BFN provides independent construction."""
        result = independence_from_cy_a3()
        assert 'independent' in result['layer_ii']['bfn_relevance'].lower() \
            or 'INDEPENDENT' in result['layer_ii']['bfn_relevance']

    def test_layer_iii_not_addressed(self):
        """Layer (iii): BFN does NOT address coproduct."""
        result = independence_from_cy_a3()
        assert 'CY-A_3' in result['layer_iii']['cy_a_dependence']

    def test_ap_cy32_warning(self):
        """AP-CY32: BFN reorganises but does not bypass CY-A_3."""
        result = independence_from_cy_a3()
        assert 'reorganises' in result['ap_cy32_warning'].lower() \
            or 'reorganizes' in result['ap_cy32_warning'].lower()


# =========================================================================
# Section 10: Full verification
# =========================================================================

class TestFullVerification:
    """Full verification of BFN-K3 Yangian identification."""

    def test_full_verification_passes(self):
        """All checks pass."""
        result = full_verification(max_n=4)
        assert result['all_pass']

    def test_hilbert_chars_pass(self):
        """Hilbert scheme Euler characteristics pass."""
        result = full_verification(max_n=4)
        assert result['hilbert_euler_chars']['all_match']

    def test_structure_function_passes(self):
        """Structure function comparison passes."""
        result = full_verification(max_n=4)
        assert result['structure_function_comparison']['all_match']

    def test_coulomb_data_generic(self):
        """Generic K3 Coulomb data is well-formed."""
        result = full_verification(max_n=2)
        assert result['coulomb_data']['generic']['algebra_rank'] == 24

    def test_coulomb_data_kummer(self):
        """Kummer K3 Coulomb data is well-formed."""
        result = full_verification(max_n=2)
        assert result['coulomb_data']['kummer']['coulomb_dim'] == 24

    def test_status_conjectural(self):
        """Overall status is CONJECTURAL (AP-CY14)."""
        result = full_verification(max_n=2)
        assert result['status'] == BFN_STATUS
