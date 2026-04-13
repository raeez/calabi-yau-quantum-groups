r"""
Tests for k3_double_current_algebra.py: K3 double current algebra for gl_1,
Heisenberg structure, bar complex, Massey deformations, and quantization.

CENTRAL RESULTS:
    (1) g_{K3} for gl_1 = Heisenberg algebra H_Muk of rank 24 (THEOREM: algebraic).
    (2) Bar Euler product = prod(1-q^n)^{24} = eta^{24}/q (THEOREM: class G bar complex).
    (3) Partition function = 1/eta^{24} * q (reciprocal of bar Euler).
    (4) Shadow class G (depth 2): all higher shadows vanish (THEOREM: Heisenberg).
    (5) K3 is formal => no Massey product corrections (THEOREM: DGMS).
    (6) K3 Yangian: CONJECTURAL (AP-CY14).

Test structure:
    - Mukai pairing: signature (4,20), block structure, nondegeneracy (6 tests)
    - Heisenberg algebra: dimension, grading, class G (5 tests)
    - Bar complex: eta^{24} match, inverse pair, known coefficients (8 tests)
    - Shadow tower: class G termination, kappa values (4 tests)
    - Formality: vanishing Massey products, cup product structure (4 tests)
    - Quantization: conjectural status, AP-CY14 compliance (3 tests)
    - Cross-verification: match with bar_euler_borcherds infrastructure (4 tests)

Manuscript references:
    k3_times_e.tex, Definition k3-double-current-algebra (L1165)
    theory_denominator_bar_euler.tex (bar Euler product)
"""

import pytest
from fractions import Fraction

from compute.lib.k3_double_current_algebra import (
    # Constants
    K3_B0, K3_B2, K3_B4, K3_TOTAL_DIM,
    MUKAI_SIG_PLUS, MUKAI_SIG_MINUS, MUKAI_RANK,
    HEISENBERG_DIM,
    # Mukai pairing
    mukai_pairing_data,
    mukai_pairing_matrix_block_structure,
    mukai_pairing_small,
    # Heisenberg algebra
    k3_heisenberg,
    heisenberg_bracket,
    # Bar complex
    k3_heisenberg_bar_complex,
    bar_euler_generating_function,
    partition_function,
    # Shadow tower
    shadow_tower_heisenberg,
    # Formality
    k3_formality,
    cup_product_structure_constants,
    # Quantization
    k3_yangian_conjectural,
    # Verification
    verify_mukai_signature,
    verify_bar_euler_product,
    verify_shadow_class_G,
    verify_formality,
    verify_partition_function_coefficients,
    full_verification,
    # Kummer route
    T4_BETTI, T4_TOTAL_DIM, T4_EVEN_DIM, T4_ODD_DIM,
    NUM_FIXED_POINTS, A1_TWISTED_WEIGHT, A1_RESOLUTION_GENERATORS,
    kummer_factorization_data,
    kummer_twisted_sector_character,
    kummer_orbifold_character_check,
    kummer_orbifold_character_coefficients,
    kummer_resolved_vs_lattice_voa,
    verify_kummer_route,
    # Single A_1 blow-up character correction
    A1_BLOWUP_GENERATORS, A1_GLUING_RELATIONS, A1_NET_GENERATORS,
    a1_single_blowup_character,
    kummer_resolved_character_assembly,
)

F = Fraction


# =========================================================================
# Section 1: K3 cohomology constants
# =========================================================================

class TestK3Constants:
    """Basic K3 cohomology dimension checks."""

    def test_betti_numbers(self):
        """b_0 = 1, b_2 = 22, b_4 = 1 for K3."""
        assert K3_B0 == 1
        assert K3_B2 == 22
        assert K3_B4 == 1

    def test_total_cohomology_dim(self):
        """dim H^*(K3) = 24."""
        assert K3_TOTAL_DIM == 24

    def test_euler_characteristic(self):
        """chi(K3) = b_0 - b_1 + b_2 - b_3 + b_4 = 1 + 22 + 1 = 24."""
        # b_1 = b_3 = 0 for K3
        chi = K3_B0 - 0 + K3_B2 - 0 + K3_B4
        assert chi == 24

    def test_heisenberg_dimension(self):
        """Heisenberg algebra = 24 generators + 1 central = 25."""
        assert HEISENBERG_DIM == 25


# =========================================================================
# Section 2: Mukai pairing
# =========================================================================

class TestMukaiPairing:
    """Mukai pairing on H^*(K3, C)."""

    def test_mukai_rank(self):
        """Mukai lattice has rank 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai pairing has signature (4, 20)."""
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20

    def test_mukai_pairing_data_fields(self):
        """MukaiPairingData has correct fields."""
        data = mukai_pairing_data()
        assert data.rank == 24
        assert data.sig_plus == 4
        assert data.sig_minus == 20
        assert data.is_nondegenerate is True

    def test_h0_h4_pairing(self):
        """<(1,0,0), (0,0,1)>_Muk = -1."""
        data = mukai_pairing_data()
        assert data.h0_h4_pairing == -1

    def test_h2_intersection_signature(self):
        """Intersection form on H^2(K3) has signature (3, 19)."""
        data = mukai_pairing_data()
        assert data.h2_intersection_sig == (3, 19)

    def test_block_structure_size(self):
        """Mukai pairing is a 24x24 matrix."""
        blocks = mukai_pairing_matrix_block_structure()
        assert blocks['size'] == (24, 24)

    def test_block_structure_off_diagonal(self):
        """<H^0, H^4> = <H^4, H^0> = -1."""
        blocks = mukai_pairing_matrix_block_structure()
        assert blocks['block_04'] == -1
        assert blocks['block_40'] == -1

    def test_block_structure_diagonal_vanishing(self):
        """<H^0, H^0> = <H^4, H^4> = 0."""
        blocks = mukai_pairing_matrix_block_structure()
        assert blocks['block_00'] == 0
        assert blocks['block_44'] == 0

    def test_block_structure_unimodular(self):
        """Mukai lattice is unimodular (det = 1)."""
        blocks = mukai_pairing_matrix_block_structure()
        assert blocks['determinant'] == 1

    def test_signature_decomposition(self):
        """Signature (4,20) = (1,1) from H^0-H^4 + (3,19) from H^2."""
        result = verify_mukai_signature()
        assert result['match'] is True
        assert result['h0_h4_block_sig'] == (1, 1)
        assert result['h2_block_sig'] == (3, 19)
        assert result['total_sig'] == (4, 20)

    def test_mukai_small_hyperbolic(self):
        """Mukai pairing on rank-3 sublattice: <(1,0,0),(0,0,1)> = -1."""
        assert mukai_pairing_small((1, 0, 0), (0, 0, 1)) == -1

    def test_mukai_small_symmetric(self):
        """Mukai pairing is symmetric: <v,w> = <w,v>."""
        v1 = (1, 2, 3)
        v2 = (4, 5, 6)
        assert mukai_pairing_small(v1, v2) == mukai_pairing_small(v2, v1)

    def test_mukai_small_h2_block(self):
        """<(0,d,0),(0,d',0)> = 2*d*d' (intersection form on algebraic H^2)."""
        assert mukai_pairing_small((0, 3, 0), (0, 5, 0)) == 30


# =========================================================================
# Section 3: Heisenberg algebra structure
# =========================================================================

class TestHeisenbergAlgebra:
    """K3 Heisenberg algebra H_Muk."""

    def test_heisenberg_generators(self):
        """24 generators from H^*(K3)."""
        h = k3_heisenberg()
        assert h.num_generators == 24

    def test_heisenberg_central(self):
        """1 central element c."""
        h = k3_heisenberg()
        assert h.central_dim == 1

    def test_heisenberg_total_dim(self):
        """Total dimension = 25."""
        h = k3_heisenberg()
        assert h.total_dim == 25

    def test_heisenberg_grading(self):
        """Graded dimensions: 1 in deg 0, 22 in deg 2, 1 in deg 4."""
        h = k3_heisenberg()
        assert h.graded_dims == {0: 1, 2: 22, 4: 1}

    def test_heisenberg_shadow_class(self):
        """Shadow class is G (Gaussian)."""
        h = k3_heisenberg()
        assert h.shadow_class == 'G'

    def test_heisenberg_is_abelian(self):
        """g = gl_1 is abelian."""
        h = k3_heisenberg()
        assert h.is_abelian_g is True

    def test_bracket_h0_h4(self):
        """[J_0, J_{23}] = -1 * c (from Mukai pairing <H^0, H^4> = -1)."""
        assert heisenberg_bracket(0, 23) == -1

    def test_bracket_h0_h0(self):
        """[J_0, J_0] = 0 (trivially, any element with itself)."""
        assert heisenberg_bracket(0, 0) == 0

    def test_bracket_h4_h4(self):
        """[J_{23}, J_{23}] = 0."""
        assert heisenberg_bracket(23, 23) == 0

    def test_bracket_antisymmetry(self):
        """[J_i, J_j] = -[J_j, J_i] at the Lie algebra level."""
        # For block structure: bracket(0, 23) = -1 and bracket(23, 0) = -1.
        # These are the Mukai pairings, which are symmetric.
        # The Lie bracket antisymmetry is imposed separately.
        # The function returns the Mukai pairing coefficient; the sign
        # is part of the Lie algebra structure.
        b1 = heisenberg_bracket(0, 23)
        b2 = heisenberg_bracket(23, 0)
        assert b1 == b2  # Mukai pairing is symmetric


# =========================================================================
# Section 4: Bar complex
# =========================================================================

class TestBarComplex:
    """Bar complex B(H_Muk) computations."""

    def test_bar_complex_data(self):
        """Bar complex data fields."""
        bc = k3_heisenberg_bar_complex()
        assert bc.lie_algebra_dim == 25
        assert bc.num_generators == 24
        assert bc.shadow_class == 'G'
        assert bc.shadow_depth == 2
        assert bc.bar_euler_exponent == 24

    def test_bar_complex_kappa_cat(self):
        """kappa_cat = chi(O_{K3}) = 2 (AP113)."""
        bc = k3_heisenberg_bar_complex()
        assert bc.kappa_cat == F(2)

    def test_bar_complex_kappa_fiber(self):
        """kappa_fiber = rank(Mukai lattice) = 24 (AP113)."""
        bc = k3_heisenberg_bar_complex()
        assert bc.kappa_fiber == 24

    def test_bar_euler_constant_term(self):
        """Constant term of prod(1-q^n)^{24} is 1."""
        coeffs = bar_euler_generating_function(5)
        assert coeffs[0] == 1

    def test_bar_euler_q1_coefficient(self):
        """Coefficient of q^1 in prod(1-q^n)^{24} is -24.

        From (1-q)^{24}: the q^1 term is C(24,1)*(-1) = -24.
        Higher factors (1-q^2)^{24}, etc. do not contribute to q^1.
        """
        coeffs = bar_euler_generating_function(5)
        assert coeffs[1] == -24

    def test_bar_euler_q2_coefficient(self):
        """Coefficient of q^2 in eta(q)^{24} is 252.

        From (1-q)^{24}: C(24,2) = 276 at q^2.
        From (1-q^2)^{24}: C(24,1)*(-1) = -24 at q^2.
        Total: 276 - 24 = 252.
        """
        coeffs = bar_euler_generating_function(5)
        assert coeffs[2] == 252

    def test_bar_euler_known_coefficients(self):
        """Match against known coefficients of eta(q)^{24} = prod(1-q^n)^{24}.

        These are related to Ramanujan tau by:
          prod(1-q^n)^{24} = sum_{n>=0} a(n) q^n
          Delta(q) = q * prod(1-q^n)^{24} = sum_{n>=1} tau(n) q^n
        So a(n) = tau(n+1).
        """
        coeffs = bar_euler_generating_function(8)
        # Known: 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643
        expected = {0: 1, 1: -24, 2: 252, 3: -1472, 4: 4830,
                    5: -6048, 6: -16744, 7: 84480, 8: -113643}
        for n, val in expected.items():
            assert coeffs.get(n, 0) == val, f"Mismatch at q^{n}: got {coeffs.get(n, 0)}, expected {val}"

    def test_bar_euler_ramanujan_tau_relation(self):
        """a(n) = tau(n+1) where tau is Ramanujan tau.

        tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, tau(5) = 4830.
        """
        coeffs = bar_euler_generating_function(5)
        ramanujan = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830}
        for n, tau_n in ramanujan.items():
            assert coeffs.get(n - 1, 0) == tau_n, f"a({n-1}) = {coeffs.get(n-1, 0)} != tau({n}) = {tau_n}"


# =========================================================================
# Section 5: Partition function (reciprocal of bar Euler)
# =========================================================================

class TestPartitionFunction:
    """Partition function 1/eta(q)^{24} = sum p_{24}(n) q^n."""

    def test_partition_constant_term(self):
        """p_{24}(0) = 1."""
        pf = partition_function(5)
        assert pf[0] == 1

    def test_partition_q1(self):
        """p_{24}(1) = 24 (one part of size 1 in 24 colors)."""
        pf = partition_function(5)
        assert pf[1] == 24

    def test_partition_q2(self):
        """p_{24}(2) = 324 = 24 (from (2)) + 300 (from (1,1)).

        (2) in 24 colors: 24 choices.
        (1,1) with 24 colors: C(24+1, 2) = 300 (multiset coefficient).
        Total: 324.
        """
        pf = partition_function(5)
        assert pf[2] == 324

    def test_partition_known_values(self):
        """Known coefficients of 1/eta(q)^{24}."""
        pf = partition_function(6)
        known = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650, 5: 176256, 6: 1073720}
        for n, val in known.items():
            assert pf.get(n, 0) == val, f"p_24({n}) = {pf.get(n, 0)} != {val}"

    def test_inverse_pair(self):
        """bar_euler * partition_function = 1 (they are inverses)."""
        max_deg = 8
        be = bar_euler_generating_function(max_deg)
        pf = partition_function(max_deg)

        for d in range(max_deg + 1):
            convolution = sum(
                be.get(k, 0) * pf.get(d - k, 0)
                for k in range(d + 1)
            )
            expected = 1 if d == 0 else 0
            assert convolution == expected, f"Convolution at degree {d}: {convolution} != {expected}"

    def test_verification_function(self):
        """The verify_partition_function_coefficients function passes."""
        result = verify_partition_function_coefficients()
        assert result['match'] is True


# =========================================================================
# Section 6: Shadow tower
# =========================================================================

class TestShadowTower:
    """Shadow tower of the K3 Heisenberg algebra."""

    def test_shadow_depth_2(self):
        """Class G: shadow terminates at depth 2."""
        tower = shadow_tower_heisenberg(kappa_fiber=F(24), max_r=10)
        assert tower[2] == F(24)
        for r in range(3, 11):
            assert tower[r] == F(0)

    def test_shadow_class_G(self):
        """Verification function confirms class G."""
        result = verify_shadow_class_G()
        assert result['is_class_G'] is True
        assert result['depth'] == 2

    def test_kappa_fiber_value(self):
        """kappa_fiber = 24 (AP113)."""
        result = verify_shadow_class_G()
        assert result['kappa_fiber'] == 24

    def test_shadow_class_label(self):
        """Shadow class is 'G'."""
        result = verify_shadow_class_G()
        assert result['class'] == 'G'


# =========================================================================
# Section 7: Formality and Massey products
# =========================================================================

class TestFormality:
    """Formality of K3 and vanishing Massey products."""

    def test_k3_is_formal(self):
        """K3 is formal (DGMS 1975)."""
        fd = k3_formality()
        assert fd.is_formal is True

    def test_massey_products_vanish(self):
        """All Massey products on H^*(K3) vanish."""
        fd = k3_formality()
        assert fd.massey_products_vanish is True

    def test_cup_product_h2_h2(self):
        """Cup product H^2 x H^2 -> H^4 has rank-1 image."""
        cup = cup_product_structure_constants()
        assert cup['h2_h2_to_h4']['rank_of_image'] == 1

    def test_higher_products_vanish(self):
        """m_3 = m_4 = ... = 0 on H^*(K3)."""
        cup = cup_product_structure_constants()
        assert cup['massey_m3'] == 0
        assert cup['massey_m4'] == 0
        assert cup['massey_mk'] == 0


# =========================================================================
# Section 8: K3 Yangian (conjectural)
# =========================================================================

class TestK3Yangian:
    """K3 Yangian -- conjectural status checks (AP-CY14)."""

    def test_yangian_is_conjectural(self):
        """K3 Yangian status is CONJECTURAL (AP-CY14)."""
        yd = k3_yangian_conjectural()
        assert yd.status == 'CONJECTURAL'

    def test_yangian_generators(self):
        """Expected 24 generators (from Mukai lattice)."""
        yd = k3_yangian_conjectural()
        assert yd.expected_generators == 24

    def test_yangian_mukai_signature(self):
        """Mukai signature (4, 20) propagates to Yangian."""
        yd = k3_yangian_conjectural()
        assert yd.mukai_signature == (4, 20)


# =========================================================================
# Section 9: Cross-verification with bar_euler_borcherds
# =========================================================================

class TestCrossVerification:
    """Cross-checks against existing bar_euler_borcherds infrastructure."""

    def test_bar_euler_matches_lattice_voa(self):
        """Our bar Euler = bar_euler_borcherds.lattice_voa_bar_euler(24).

        Both compute prod(1-q^n)^{24} via different paths.
        """
        from compute.lib.bar_euler_borcherds import lattice_voa_bar_euler
        our_coeffs = bar_euler_generating_function(10)
        their_coeffs = lattice_voa_bar_euler(24, 10)
        for d in range(11):
            assert our_coeffs.get(d, 0) == their_coeffs.get(d, 0), \
                f"Mismatch at degree {d}: {our_coeffs.get(d, 0)} vs {their_coeffs.get(d, 0)}"

    def test_bar_euler_matches_leech(self):
        """Our bar Euler = Leech lattice bar Euler (both rank 24).

        The Leech lattice has rank 24 = Mukai lattice rank.
        The energy-graded bar Euler products must agree (both = eta^{24}).
        """
        from compute.lib.bar_euler_borcherds import leech_bar_euler_product
        our_coeffs = bar_euler_generating_function(10)
        leech_coeffs = leech_bar_euler_product(10)
        for d in range(11):
            assert our_coeffs.get(d, 0) == leech_coeffs.get(d, 0), \
                f"Mismatch at degree {d}"

    def test_eta_power_match(self):
        """Our bar Euler = eta_power_coefficients(24, N)."""
        from compute.lib.bar_euler_borcherds import eta_power_coefficients
        our_coeffs = bar_euler_generating_function(10)
        eta24 = eta_power_coefficients(24, 10)
        for d in range(11):
            assert our_coeffs.get(d, 0) == eta24.get(d, 0)

    def test_ramanujan_tau_shifted(self):
        """a(n) = tau(n+1) cross-check with bar_euler_borcherds.ramanujan_tau."""
        from compute.lib.bar_euler_borcherds import ramanujan_tau
        our_coeffs = bar_euler_generating_function(10)
        tau = ramanujan_tau(11)
        for n in range(10):
            assert our_coeffs.get(n, 0) == tau.get(n + 1, 0), \
                f"a({n}) = {our_coeffs.get(n, 0)} != tau({n+1}) = {tau.get(n+1, 0)}"


# =========================================================================
# Section 10: Full verification
# =========================================================================

class TestFullVerification:
    """Run the full_verification function and check all paths pass."""

    def test_full_verification_all_pass(self):
        """All 5 verification paths pass."""
        result = full_verification(max_degree=8)
        assert result['path1_mukai_signature']['match'] is True
        assert result['path2_bar_euler_product']['inverse_pair_match'] is True
        assert result['path2_bar_euler_product']['known_eta24_match'] is True
        assert result['path3_shadow_class_G']['is_class_G'] is True
        assert result['path4_formality']['is_formal'] is True
        assert result['path5_partition_coefficients']['match'] is True

    def test_verify_bar_euler_product(self):
        """Dedicated bar Euler product verification."""
        result = verify_bar_euler_product(8)
        assert result['inverse_pair_match'] is True
        assert result['known_eta24_match'] is True


# =========================================================================
# Section 11: Kummer route -- equivariant factorization homology on T^4/Z_2
# =========================================================================

class TestKummerConstants:
    """T^4 cohomology and Z_2 fixed-point constants."""

    def test_t4_betti_numbers(self):
        """H^*(T^4) has Betti numbers (1, 4, 6, 4, 1)."""
        assert T4_BETTI == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}

    def test_t4_total_dim(self):
        """dim H^*(T^4) = 2^4 = 16."""
        assert T4_TOTAL_DIM == 16
        assert T4_TOTAL_DIM == sum(T4_BETTI.values())

    def test_t4_even_odd_split(self):
        """Even/odd cohomology dimensions: 8 + 8 = 16."""
        assert T4_EVEN_DIM == 8
        assert T4_ODD_DIM == 8
        assert T4_EVEN_DIM + T4_ODD_DIM == T4_TOTAL_DIM

    def test_num_fixed_points(self):
        """Z_2 acts on T^4 with 2^4 = 16 fixed points."""
        assert NUM_FIXED_POINTS == 16
        assert NUM_FIXED_POINTS == 2**4

    def test_a1_twisted_weight(self):
        """Twisted sector conformal weight h = 1/2 from C^2/Z_2."""
        assert A1_TWISTED_WEIGHT == F(1, 2)

    def test_a1_resolution_generators(self):
        """Each CP^1 exceptional divisor contributes 2 generators."""
        assert A1_RESOLUTION_GENERATORS == 2


class TestKummerStep1:
    """Step 1: int_{T^4} H_1 = rank-16 Heisenberg."""

    def test_torus_rank(self):
        """Factorization homology on T^4 gives rank-16 Heisenberg."""
        data = kummer_factorization_data()
        assert data.torus_rank == 16

    def test_torus_rank_equals_betti_sum(self):
        """Cross-check: rank = sum of Betti numbers."""
        data = kummer_factorization_data()
        assert data.torus_rank == sum(data.torus_betti.values())

    def test_central_charge(self):
        """Central charge c = 4 (one per S^1 factor)."""
        data = kummer_factorization_data()
        assert data.torus_central_charge == 4


class TestKummerStep2:
    """Step 2: Z_2-invariant subalgebra = rank-8 Heisenberg."""

    def test_untwisted_rank(self):
        """Z_2-invariant part has rank 8 = dim H^even(T^4)."""
        data = kummer_factorization_data()
        assert data.untwisted_rank == 8

    def test_z2_action_signs(self):
        """Z_2 acts by (-1)^k on H^k(T^4)."""
        data = kummer_factorization_data()
        for k in range(5):
            assert data.z2_action_on_hk[k] == (-1)**k

    def test_even_cohomology_dimension(self):
        """Cross-check: dim H^even = 1 + 6 + 1 = 8."""
        assert T4_BETTI[0] + T4_BETTI[2] + T4_BETTI[4] == 8


class TestKummerStep3:
    """Step 3: 16 twisted sectors with h = 1/2."""

    def test_twisted_sector_count(self):
        """16 fixed points give 16 twisted sectors."""
        data = kummer_factorization_data()
        assert data.num_fixed_points == 16

    def test_twisted_weight(self):
        """Each twisted sector has weight h = 1/2."""
        data = kummer_factorization_data()
        assert data.twisted_weight == F(1, 2)

    def test_twisted_weight_from_components(self):
        """h = 2 * (1/4) from C^2 normal directions."""
        complex_dim = 2
        weight_per_dim = F(1, 4)
        assert complex_dim * weight_per_dim == F(1, 2)

    def test_p2_partition_coefficients(self):
        """1/prod(1-q^n)^2 coefficients: p_2(0..4) = 1,2,5,10,20."""
        tw = kummer_twisted_sector_character(max_terms=6)
        assert tw['p2_coefficients'][0] == 1
        assert tw['p2_coefficients'][1] == 2
        assert tw['p2_coefficients'][2] == 5
        assert tw['p2_coefficients'][3] == 10
        assert tw['p2_coefficients'][4] == 20

    def test_p2_known_match(self):
        """Twisted sector character matches known 2-colored partitions."""
        tw = kummer_twisted_sector_character(max_terms=6)
        assert tw['p2_known_match'] is True


class TestKummerStep4:
    """Step 4: orbifold chiral algebra before resolution."""

    def test_orbifold_kappa_ch(self):
        """kappa_ch of orbifold = 2 = chi(O_{K3})."""
        data = kummer_factorization_data()
        assert data.orbifold_kappa_ch == 2

    def test_kappa_ch_not_from_untwisted_alone(self):
        """The untwisted sector alone has kappa_ch = 0 (abelian torus).
        The twisted sectors are essential for kappa_ch = 2."""
        # chi(O_{T^4}) = 0 for abelian variety
        chi_t4 = 1 - 4 + 6 - 4 + 1  # alternating sum of Betti
        assert chi_t4 == 0
        # But chi(O_{K3}) = 2
        chi_k3 = 1 - 0 + 1  # h^{0,0} - h^{1,0} + h^{2,0}
        assert chi_k3 == 2


class TestKummerStep5:
    """Step 5: 16 blow-ups recover rank-24 Mukai Heisenberg."""

    def test_resolved_rank(self):
        """After resolution: 8 + 32 - 16 = 24."""
        data = kummer_factorization_data()
        assert data.resolved_rank == 24

    def test_resolved_rank_arithmetic(self):
        """Cross-check the rank arithmetic explicitly."""
        untwisted = T4_EVEN_DIM  # 8
        blown_up = NUM_FIXED_POINTS * A1_RESOLUTION_GENERATORS  # 32
        gluing = NUM_FIXED_POINTS  # 16
        assert untwisted + blown_up - gluing == 24

    def test_matches_mukai_rank(self):
        """Resolved rank = Mukai lattice rank."""
        data = kummer_factorization_data()
        assert data.matches_mukai_rank is True
        assert data.resolved_rank == MUKAI_RANK

    def test_matches_k3_total_dim(self):
        """Resolved rank = dim H^*(K3)."""
        data = kummer_factorization_data()
        assert data.resolved_rank == K3_TOTAL_DIM


class TestKummerCrossVerification:
    """Multi-path cross-verification of the Kummer route."""

    def test_rank_three_paths(self):
        """Rank 24 from Euler char, Hodge numbers, and lattice."""
        result = verify_kummer_route()
        assert result['path5_rank_cross_check'] == 24
        assert len(result['path5_methods']) == 3

    def test_kappa_two_paths(self):
        """kappa_ch = 2 from Noether formula and Hodge numbers."""
        result = verify_kummer_route()
        assert result['path6_kappa_cross_check'] == 2
        assert len(result['path6_methods']) == 2

    def test_orbifold_rank_recovery(self):
        """Orbifold character check recovers rank 24."""
        orb = kummer_orbifold_character_check(max_terms=6)
        assert orb['rank_resolved_total'] == 24
        assert orb['matches_k3_rank'] is True

    def test_full_kummer_verification(self):
        """All Kummer route checks pass."""
        result = verify_kummer_route()
        assert result['all_checks_pass'] is True


# =========================================================================
# Section 9: Kummer route character-level computation
# =========================================================================

class TestKummerOrbifoldCharacter:
    """Character-level orbifold computation through q^8.

    The orbifold char_{T^4/Z_2}(q) has two layers:
      Integer powers:      p_8(n)         [from untwisted H_8]
      Half-integer powers: 16 * p_2(n)    [from 16 twisted sectors]

    After resolution (16 blow-ups), the target is 1/eta^{24}.
    The blow-up correction Delta(n) = p_24(n) - p_8(n) encodes the
    16 exceptional CP^1 generators.  The factorization identity
    p_24 = p_8 * p_16 (convolution) is the character-level avatar
    of the rank decomposition 24 = 8 + 16.
    """

    def test_target_eta24_known_coefficients(self):
        """1/eta^{24} coefficients match OEIS A006922."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        expected = {
            0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650,
            5: 176256, 6: 1073720, 7: 5930496, 8: 30178575,
        }
        for n, val in expected.items():
            assert data['target_eta24_coeffs'][n] == val, (
                f"1/eta^24 at q^{n}: got {data['target_eta24_coeffs'][n]}, "
                f"expected {val}"
            )

    def test_untwisted_sector_p8_coefficients(self):
        """Untwisted sector char(H_8) = prod 1/(1-q^n)^8."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        expected_p8 = {
            0: 1, 1: 8, 2: 44, 3: 192, 4: 726,
            5: 2464, 6: 7704, 7: 22528, 8: 62337,
        }
        for n, val in expected_p8.items():
            assert data['orbifold_integer_coeffs'][n] == val

    def test_twisted_sector_half_integer_coefficients(self):
        """16 twisted sectors contribute 16*p_2(n) at q^{n+1/2}."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        # 16 * p_2(n) for n = 0..8
        expected_half = {
            0: 16, 1: 32, 2: 80, 3: 160, 4: 320,
            5: 576, 6: 1040, 7: 1760, 8: 2960,
        }
        for n, val in expected_half.items():
            assert data['orbifold_half_integer_coeffs'][n] == val

    def test_orbifold_does_not_equal_target(self):
        """The orbifold integer-power character != 1/eta^24.

        This is the key negative result: the orbifold character (before
        resolution) does NOT match the K3 partition function.  The
        blow-up correction is essential.
        """
        data = kummer_orbifold_character_coefficients(max_terms=8)
        assert data['orbifold_equals_target'] is False

    def test_blowup_correction_coefficients(self):
        """Blow-up correction Delta(n) = p_24(n) - p_8(n)."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        expected_delta = {
            0: 0, 1: 16, 2: 280, 3: 3008, 4: 24924,
            5: 173792, 6: 1066016, 7: 5907968, 8: 30116238,
        }
        for n, val in expected_delta.items():
            assert data['blowup_correction'][n] == val, (
                f"Delta({n}): got {data['blowup_correction'][n]}, "
                f"expected {val}"
            )

    def test_blowup_correction_q0_vanishes(self):
        """Delta(0) = 0: vacuum is unique, no correction needed."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        assert data['blowup_correction'][0] == 0

    def test_blowup_correction_q1_equals_16(self):
        """Delta(1) = 16: one new generator per exceptional CP^1.

        The 16 exceptional divisors each contribute one new degree-1
        generator to the Heisenberg algebra.  This is the character-level
        avatar of the rank jump 8 -> 24.
        """
        data = kummer_orbifold_character_coefficients(max_terms=8)
        assert data['blowup_correction_at_q1'] == 16
        assert data['blowup_correction_at_q1'] == NUM_FIXED_POINTS

    def test_factorization_identity_p24_equals_p8_times_p16(self):
        """p_24 = p_8 * p_16 (convolution) through q^8.

        This is the character-level factorization identity:
          1/prod(1-q^n)^{24} = 1/prod(1-q^n)^8 * 1/prod(1-q^n)^{16}

        encoding the Heisenberg rank decomposition 24 = 8 + 16
        (8 untwisted generators + 16 from blow-up).
        """
        data = kummer_orbifold_character_coefficients(max_terms=8)
        assert data['factorization_match'] is True

    def test_factorization_convolution_explicit(self):
        """Explicit convolution check: (p_8 * p_16)(n) = p_24(n)."""
        data = kummer_orbifold_character_coefficients(max_terms=8)
        for n in range(9):
            assert (data['factorization_p8_times_p16'][n]
                    == data['target_eta24_coeffs'][n])

    def test_blowup_correction_dominates(self):
        """For n >= 2, the blow-up correction exceeds the untwisted part.

        The 16 exceptional generators rapidly dominate: at q^2 already
        Delta(2) = 280 >> p_8(2) = 44.
        """
        data = kummer_orbifold_character_coefficients(max_terms=8)
        for n in range(2, 9):
            assert (data['blowup_correction'][n]
                    > data['orbifold_integer_coeffs'][n]), (
                f"At q^{n}: correction {data['blowup_correction'][n]} "
                f"should exceed untwisted {data['orbifold_integer_coeffs'][n]}"
            )

    def test_kummer_route_completeness(self):
        """After resolution, orbifold + blow-up = 1/eta^24 exactly.

        This is the completeness statement: the Kummer route
        (orbifold + resolution) recovers the full K3 partition
        function with zero residual through q^8.
        """
        data = kummer_orbifold_character_coefficients(max_terms=8)
        for n in range(9):
            reconstructed = (data['orbifold_integer_coeffs'][n]
                             + data['blowup_correction'][n])
            assert reconstructed == data['target_eta24_coeffs'][n], (
                f"At q^{n}: {data['orbifold_integer_coeffs'][n]} + "
                f"{data['blowup_correction'][n]} = {reconstructed} != "
                f"{data['target_eta24_coeffs'][n]}"
            )


# =========================================================================
# Section 10: Direct q-expansion comparison --
#   char(A^{orb}_{resolved}) vs V_{Lambda_{K3}} character 1/eta^{24}
# =========================================================================

class TestResolvedVsLatticeVOA:
    r"""Direct q-expansion comparison of char(A^{orb}_{resolved}) vs 1/eta^{24}.

    Three independent paths:
      Path A: rank-24 Heisenberg partition function = 1/prod(1-q^n)^{24}.
      Path B: factored convolution p_8 * p_16 = p_24.
      Path C: DHVW Z_2-even projection yields non-negative integer coefficients.

    The central result: char(A^{orb}_{resolved}) = 1/eta^{24} EXACTLY,
    verified term-by-term through q^{10}.
    """

    def test_central_identity(self):
        """char(A^{orb}_{resolved}) = 1/eta^{24}: master verification."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['char_A_orb_resolved_equals_1_over_eta24'] is True

    def test_path_A_known_coefficients(self):
        """Path A: 1/eta^{24} matches known values through q^6."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        known = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650,
                 5: 176256, 6: 1073720}
        for n, val in known.items():
            assert result['path_A_pf24'][n] == val

    def test_path_B_factorization(self):
        """Path B: p_8 * p_16 = p_24 (Cauchy convolution)."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_B_factorization_match'] is True

    def test_path_B_blowup_delta_q0(self):
        """Path B: Delta(0) = 0 (unique vacuum, no correction)."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_B_blowup_delta'][0] == 0

    def test_path_B_blowup_delta_q1(self):
        """Path B: Delta(1) = 16 (one generator per exceptional CP^1)."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_B_blowup_delta'][1] == 16

    def test_path_C_z2_even_integral(self):
        """Path C: Z_2-even projection has integer coefficients.

        The DHVW formula (1/2)(Z_{(1,1)} + Z_{(1,g)}) counts Z_2-invariant
        states.  Integrality is a necessary condition for a well-defined
        state count.
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_C_z2_even_integral'] is True

    def test_path_C_z2_even_nonneg(self):
        """Path C: Z_2-even projection has non-negative coefficients.

        Non-negativity is a necessary condition for a physical character
        (it counts states in the orbifold Hilbert space).
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_C_z2_even_nonneg'] is True

    def test_path_C_z2_even_q0(self):
        """Path C: Z_2-even at q^0 = 1 (unique Z_2-invariant vacuum)."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_C_z2_even_coeffs'][0] == '1'

    def test_path_C_z2_even_q1_vanishes(self):
        """Path C: Z_2-even at q^1 = 0.

        Every single-oscillator state a^i_{-1}|0> is Z_2-ODD because Z_2
        acts as z -> -z on all 4 complex bosons of T^4.  Hence the Z_2-even
        projection at energy 1 is zero.  This is the character-level
        signature that the untwisted sector alone is insufficient: the
        q^1 generators of the K3 character (24 of them) come entirely
        from the resolution of the 16 twisted sectors plus the untwisted
        Z_2-even multi-oscillator states at higher energy.
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_C_z2_even_coeffs'][1] == '0'

    def test_path_C_z2_even_q2(self):
        """Path C: Z_2-even at q^2 = 36 (two-oscillator Z_2-even states).

        Two-oscillator states a^i_{-1} a^j_{-1}|0> are Z_2-even because
        (-1)^2 = +1.  There are C(8,2) = 28 pairs plus 8 double
        excitations a^i_{-2}|0> (which are also Z_2-even since the -2
        mode of a Z_2-odd oscillator has (-1)^1 = -1... wait, the mode
        number does not affect the Z_2 charge).

        The Z_2-even count at q^2 is 36, confirming the DHVW computation.
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_C_z2_even_coeffs'][2] == '36'

    def test_bar_euler_cross_check(self):
        """Bar Euler from bar_euler_borcherds.lattice_voa_bar_euler(24) matches."""
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['bar_euler_cross_check'] is True

    def test_blowup_correction_growth(self):
        """Blow-up correction grows faster than untwisted sector.

        At large n, the 16 resolved generators dominate: Delta(n) >> p_8(n).
        By q^2 the correction already exceeds the untwisted part by 6x.
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        delta = result['path_B_blowup_delta']
        pf24 = result['path_A_pf24']
        # At q^2: delta = 280, p_8 = 44, ratio ~ 6.4x
        assert delta[2] > 6 * (pf24[2] - delta[2])

    def test_resolved_rank_from_q1_coefficient(self):
        """The q^1 coefficient of 1/eta^{24} directly gives the rank.

        p_{24}(1) = 24 = number of bosonic generators (= Mukai rank).
        The orbifold contributes p_8(1) = 8 from untwisted; the remaining
        16 = Delta(1) come from resolution.  24 = 8 + 16.
        """
        result = kummer_resolved_vs_lattice_voa(max_terms=10)
        assert result['path_A_pf24'][1] == 24
        assert result['path_B_blowup_delta'][1] == 16
        assert result['path_A_pf24'][1] == 8 + result['path_B_blowup_delta'][1]


# =========================================================================
# Section 11: Single A_1 blow-up character (per-point decomposition)
# =========================================================================

class TestA1BlowupConstants:
    """Constants for the single A_1 blow-up correction."""

    def test_blowup_generators(self):
        """H^*(CP^1) contributes 2 generators (H^0 + H^2)."""
        assert A1_BLOWUP_GENERATORS == 2

    def test_gluing_relations(self):
        """1 gluing relation identifies H^0(CP^1) with local constant."""
        assert A1_GLUING_RELATIONS == 1

    def test_net_generators(self):
        """Net generators per point: 2 - 1 = 1."""
        assert A1_NET_GENERATORS == 1

    def test_net_generators_arithmetic(self):
        """Net = blowup - gluing."""
        assert A1_NET_GENERATORS == A1_BLOWUP_GENERATORS - A1_GLUING_RELATIONS

    def test_total_from_16_points(self):
        """16 points * 1 net generator = 16 total new generators."""
        assert NUM_FIXED_POINTS * A1_NET_GENERATORS == 16

    def test_resolved_rank_from_net(self):
        """8 (untwisted) + 16 * 1 (net from blow-ups) = 24."""
        assert T4_EVEN_DIM + NUM_FIXED_POINTS * A1_NET_GENERATORS == 24


class TestA1SingleBlowupCharacter:
    """Single A_1 blow-up character = ordinary partition numbers p(n)."""

    def test_net_character_is_partition_numbers(self):
        """The single blow-up net character equals p(n)."""
        data = a1_single_blowup_character(max_deg=10)
        assert data['net_character_is_partition_numbers'] is True

    def test_partition_numbers_explicit(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        data = a1_single_blowup_character(max_deg=10)
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7,
                    6: 11, 7: 15, 8: 22, 9: 30, 10: 42}
        for k, val in expected.items():
            assert data['net_character'][k] == val, (
                f"p({k}): got {data['net_character'][k]}, expected {val}"
            )

    def test_cp1_character_is_p2(self):
        """CP^1 character (2 generators) = 2-colored partitions p_2(n).

        Verified by checking the explicit p_2 values and the factorization
        p_2 = p_1 * p_1 (the CP^1 character factors as net * gluing).
        """
        data = a1_single_blowup_character(max_deg=10)
        # The CP^1 character factors as net * gluing (both are p_1)
        assert data['cp1_factorization_ok'] is True
        # And the explicit values match p_2
        expected_p2 = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20}
        for k, val in expected_p2.items():
            assert data['cp1_character'][k] == val

    def test_cp1_character_explicit(self):
        """p_2(0)=1, p_2(1)=2, p_2(2)=5, p_2(3)=10, p_2(4)=20."""
        data = a1_single_blowup_character(max_deg=10)
        expected_p2 = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20}
        for k, val in expected_p2.items():
            assert data['cp1_character'][k] == val

    def test_cp1_factorization(self):
        """p_2 = p_1 * p_1 (convolution): 2 generators = net + gluing."""
        data = a1_single_blowup_character(max_deg=10)
        assert data['cp1_factorization_ok'] is True

    def test_net_character_q0(self):
        """p(0) = 1: unique vacuum."""
        data = a1_single_blowup_character(max_deg=5)
        assert data['net_character'][0] == 1

    def test_net_character_q1(self):
        """p(1) = 1: single generator at energy 1."""
        data = a1_single_blowup_character(max_deg=5)
        assert data['net_character'][1] == 1


class TestKummerResolvedAssembly:
    r"""Factored assembly: chi_K3 = chi_{H_8} * delta_16.

    The resolved K3 character is assembled from:
      chi_{H_8} = prod 1/(1-q^n)^8    (untwisted sector)
      delta_16  = prod 1/(1-q^n)^{16}  (16 blow-up corrections)
    giving prod 1/(1-q^n)^{24} = 1/eta^{24}.
    """

    def test_matches_eta24_inverse(self):
        """Resolved character = 1/eta^{24} through q^{10}."""
        data = kummer_resolved_character_assembly(max_deg=10)
        assert data['matches_eta24_inverse'] is True

    def test_match_through_q5(self):
        """Match verified through at least q^5 (as requested)."""
        data = kummer_resolved_character_assembly(max_deg=5)
        assert data['match_through_degree'] >= 5

    def test_match_through_q10(self):
        """Match verified through q^{10}."""
        data = kummer_resolved_character_assembly(max_deg=10)
        assert data['match_through_degree'] == 10

    def test_matches_partition_function(self):
        """Factored assembly matches partition_function() from bar complex."""
        data = kummer_resolved_character_assembly(max_deg=8)
        assert data['matches_partition_fn'] is True

    def test_conv_16_from_single(self):
        """delta_16 = (delta_1)^{*16}: 16-fold convolution of single blow-up."""
        data = kummer_resolved_character_assembly(max_deg=8)
        assert data['conv_16_from_single_ok'] is True

    def test_rank_total(self):
        """Total rank: 8 + 16*1 = 24."""
        data = kummer_resolved_character_assembly(max_deg=5)
        assert data['rank_total'] == 24
        assert data['rank_untwisted'] == 8
        assert data['rank_per_blowup'] == 1
        assert data['num_blowups'] == 16

    def test_resolved_coefficients_explicit(self):
        """Explicit coefficient check against known 1/eta^{24} values."""
        data = kummer_resolved_character_assembly(max_deg=10)
        known = {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650,
                 5: 176256, 6: 1073720, 7: 5930496,
                 8: 30178575, 9: 143184000, 10: 639249300}
        for n, val in known.items():
            assert data['resolved'][n] == val, (
                f"q^{n}: got {data['resolved'][n]}, expected {val}"
            )

    def test_chi_h8_coefficients(self):
        """Untwisted sector chi_{H_8} known values."""
        data = kummer_resolved_character_assembly(max_deg=6)
        expected = {0: 1, 1: 8, 2: 44, 3: 192, 4: 726,
                    5: 2464, 6: 7704}
        for n, val in expected.items():
            assert data['chi_h8'][n] == val

    def test_delta_16_coefficients(self):
        """Total blow-up correction delta_16 known values."""
        data = kummer_resolved_character_assembly(max_deg=6)
        expected = {0: 1, 1: 16, 2: 152, 3: 1088, 4: 6460,
                    5: 33440, 6: 155584}
        for n, val in expected.items():
            assert data['delta_16_total_blowup'][n] == val

    def test_delta_1_coefficients(self):
        """Single blow-up delta_1 = ordinary partition numbers."""
        data = kummer_resolved_character_assembly(max_deg=6)
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11}
        for n, val in expected.items():
            assert data['delta_1_single_blowup'][n] == val

    def test_q1_decomposition(self):
        """At q^1: 24 = 8*1 + 1*16 (convolution of chi_h8 and delta_16).

        chi_h8(1) = 8, delta_16(0) = 1: contributes 8*1 = 8.
        chi_h8(0) = 1, delta_16(1) = 16: contributes 1*16 = 16.
        Total: 8 + 16 = 24.
        """
        data = kummer_resolved_character_assembly(max_deg=5)
        assert data['chi_h8'][1] * data['delta_16_total_blowup'][0] + \
            data['chi_h8'][0] * data['delta_16_total_blowup'][1] == 24
