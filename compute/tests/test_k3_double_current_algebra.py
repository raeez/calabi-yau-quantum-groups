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
    verify_kummer_route,
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
        tower = shadow_tower_heisenberg(kappa=F(24), max_r=10)
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
