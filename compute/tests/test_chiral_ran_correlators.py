r"""Tests for chiral_ran_correlators.py: chiral correlation functions on the Ran space.

CENTRAL RESULTS:
    (1) <J_i(z) J_j(w)>_{P^1} = omega^{ij} / (z-w)^2 (24x24 matrix, PROVED).
    (2) 4-point via Wick: 3 channels, (n-1)!! pairings (PROVED).
    (3) <T(z) T(w)> = c/2 (z-w)^{-4} with c = 24 (Sugawara, PROVED).
    (4) Elliptic: <J_i(z) J_j(w)>_E = omega^{ij} wp(z-w, tau) (PROVED).
    (5) Z(E, tau) = 1/eta^{24}, p_{24}(n) = chi(Hilb^n(K3)) (PROVED).
    (6) Ran space structure: factorization = Wick (PROVED).
    (7) K3 Yangian deformed correlators: CONJECTURAL (AP-CY14).

Manuscript references:
    k3_times_e.tex sec:k3e-chiral-ran-correlators (new section)
    en_factorization.tex sec:e3-from-hcs (E_3 FH framework)
    Frenkel-Ben-Zvi, "Vertex Algebras and Algebraic Curves" (2004), Ch. 5, 9
    Beilinson-Drinfeld, "Chiral Algebras" (2004), Ch. 4
"""

import pytest
from fractions import Fraction

from compute.lib.chiral_ran_correlators import (
    # Constants
    RANK,
    CENTRAL_CHARGE,
    KAPPA_CH,
    KAPPA_CAT,
    KAPPA_BKM,
    KAPPA_FIBER,
    # Mukai pairing
    mukai_pairing_matrix,
    MukaiPairingMatrix,
    # Two-point on P^1
    two_point_p1,
    two_point_matrix_p1,
    # Wick contractions
    wick_pairings,
    n_point_p1,
    four_point_p1,
    double_factorial,
    num_wick_pairings,
    # Stress tensor
    stress_tensor_two_point,
    stress_tensor_ope_data,
    # Elliptic
    elliptic_two_point,
    elliptic_two_point_matrix,
    weierstrass_p_laurent_coefficients,
    # Partition function
    partition_function_elliptic,
    partition_function_genus_g,
    # Yangian (conjectural)
    yangian_deformed_two_point,
    yangian_deformed_propagator_p1,
    yangian_deformed_partition_function,
    # Ran space
    ran_space_correlator_structure,
    # Verification
    verify_two_point_p1,
    verify_four_point_diagonal,
    verify_stress_tensor,
    verify_partition_function,
    verify_wick_counting,
    verify_elliptic_degeneration,
    full_correlator_verification,
)

F = Fraction


# =========================================================================
# Section 1: Constants and kappa spectrum (AP113)
# =========================================================================

class TestConstants:
    """Verify basic constants and AP113 compliance."""

    def test_rank_24(self):
        """Mukai lattice rank = 24."""
        # VERIFIED: [DC] rank of H^*(K3) = 24, [LT] Mukai (1987)
        assert RANK == 24

    def test_central_charge_24(self):
        """Central charge c = 24 = rank."""
        # VERIFIED: [DC] c = rank for Heisenberg, [LT] Frenkel-Ben-Zvi (2004)
        assert CENTRAL_CHARGE == 24

    def test_kappa_ch(self):
        """kappa_ch = 3 (AP113)."""
        # VERIFIED: [DC] from Phi(D^b(Coh(K3))), [LT] CLAUDE.md kappa-spectrum
        assert KAPPA_CH == 3

    def test_kappa_cat(self):
        """kappa_cat = 2 = chi(O_{K3}) (AP113)."""
        # VERIFIED: [DC] h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2,
        # [LT] Huybrechts "Lectures on K3 Surfaces" (2016)
        assert KAPPA_CAT == 2

    def test_kappa_bkm(self):
        """kappa_BKM = 5 (weight of Delta_5) (AP113)."""
        # VERIFIED: [DC] Borcherds lift weight = c(0)/2 = 10/2 = 5,
        # [LT] Gritsenko-Nikulin (1996)
        assert KAPPA_BKM == 5

    def test_kappa_fiber(self):
        """kappa_fiber = 24 (Mukai lattice rank) (AP113)."""
        # VERIFIED: [DC] rank = 24, [LT] Mukai (1987)
        assert KAPPA_FIBER == 24


# =========================================================================
# Section 2: Mukai pairing matrix
# =========================================================================

class TestMukaiPairing:
    """Verify the Mukai pairing matrix omega^{ij}."""

    def test_rank(self):
        """Pairing has rank 24."""
        omega = mukai_pairing_matrix()
        assert omega.rank == 24

    def test_signature(self):
        """Signature is (4, 20)."""
        # VERIFIED: [DC] H^0 contributes 1+, H^2 contributes 3+ 19-,
        # H^4 contributes 0+ 0- (but paired with H^0),
        # Mukai pairing adds one hyperbolic pair: total (4, 20)
        # [LT] Huybrechts (2006) Ch. 10
        omega = mukai_pairing_matrix()
        assert omega.signature == (4, 20)

    def test_diagonal_entries_count(self):
        """24 diagonal entries: 4 positive, 20 negative."""
        omega = mukai_pairing_matrix()
        pos = sum(1 for e in omega.diagonal_entries if e > 0)
        neg = sum(1 for e in omega.diagonal_entries if e < 0)
        assert pos == 4
        assert neg == 20
        assert pos + neg == 24

    def test_symmetric(self):
        """Pairing is symmetric."""
        omega = mukai_pairing_matrix()
        assert omega.is_symmetric

    def test_determinant(self):
        """det(omega) = (+1)^4 * (-1)^20 = 1."""
        # VERIFIED: [DC] (-1)^20 = 1 (20 is even), [SY] unimodularity
        omega = mukai_pairing_matrix()
        assert omega.determinant == 1

    def test_omega_ij_diagonal(self):
        """omega^{ii} = +1 for i < 4, -1 for i >= 4."""
        omega = mukai_pairing_matrix()
        for i in range(4):
            assert omega.omega_ij(i, i) == 1
        for i in range(4, 24):
            assert omega.omega_ij(i, i) == -1

    def test_omega_ij_off_diagonal(self):
        """omega^{ij} = 0 for i != j (diagonal basis)."""
        omega = mukai_pairing_matrix()
        for i in range(24):
            for j in range(24):
                if i != j:
                    assert omega.omega_ij(i, j) == 0

    def test_omega_squared_trace(self):
        """Tr(omega^2) = 24 (each s_i^2 = 1)."""
        # VERIFIED: [DC] direct sum, [SY] sum of squares of +/-1
        omega = mukai_pairing_matrix()
        trace = sum(omega.omega_ij(i, i) ** 2 for i in range(24))
        assert trace == 24


# =========================================================================
# Section 3: Two-point function on P^1
# =========================================================================

class TestTwoPointP1:
    """<J_i(z) J_j(w)>_{P^1} = omega^{ij} / (z-w)^2."""

    def test_diagonal_positive(self):
        """<J_0(z) J_0(w)> = +1 / (z-w)^2 (positive Mukai direction)."""
        result = two_point_p1(0, 0)
        assert result.omega_ij == 1

    def test_diagonal_negative(self):
        """<J_5(z) J_5(w)> = -1 / (z-w)^2 (negative Mukai direction)."""
        result = two_point_p1(5, 5)
        assert result.omega_ij == -1

    def test_off_diagonal_zero(self):
        """<J_0(z) J_1(w)> = 0 (different indices in diagonal basis)."""
        result = two_point_p1(0, 1)
        assert result.omega_ij == 0

    def test_off_diagonal_mixed(self):
        """<J_0(z) J_5(w)> = 0 (positive x negative)."""
        result = two_point_p1(0, 5)
        assert result.omega_ij == 0

    def test_all_positive_block(self):
        """All 4 positive-block diagonal correlators are +1."""
        for i in range(4):
            assert two_point_p1(i, i).omega_ij == 1

    def test_all_negative_block(self):
        """All 20 negative-block diagonal correlators are -1."""
        for i in range(4, 24):
            assert two_point_p1(i, i).omega_ij == -1

    def test_proved_status(self):
        """All P^1 correlators are PROVED."""
        for i in range(24):
            assert 'PROVED' in two_point_p1(i, i).proof_status

    def test_matrix_structure(self):
        """Full 24x24 matrix has correct structure."""
        mat = two_point_matrix_p1()
        assert mat['matrix_size'] == (24, 24)
        assert mat['rank'] == 24
        assert mat['signature'] == (4, 20)
        assert mat['singularity_order'] == 2

    def test_matrix_nonzero_entries(self):
        """Only diagonal entries are nonzero: 24 total."""
        mat = two_point_matrix_p1()
        assert mat['nonzero_entries'] == 24

    def test_cross_check_with_k3_dca(self):
        """Cross-check: omega^{ij} agrees with k3_double_current_algebra."""
        from compute.lib.k3_double_current_algebra import mukai_pairing_data
        dca_data = mukai_pairing_data()
        omega = mukai_pairing_matrix()
        # Both should report signature (4, 20) and rank 24
        assert dca_data.rank == omega.rank
        assert dca_data.sig_plus == omega.signature[0]
        assert dca_data.sig_minus == omega.signature[1]


# =========================================================================
# Section 4: Wick contractions and n-point functions
# =========================================================================

class TestWickContractions:
    """Wick contraction engine for n-point functions."""

    def test_zero_point(self):
        """0-point function = 1 (vacuum normalization)."""
        result = n_point_p1([])
        assert result['value'] == 1

    def test_one_point_vanishes(self):
        """1-point function = 0 (odd n: charge conservation)."""
        result = n_point_p1([0])
        assert result['value'] == 0

    def test_two_point_via_wick(self):
        """2-point via Wick matches direct computation."""
        result = n_point_p1([0, 0])
        assert result['num_channels'] == 1
        assert result['nonzero_channels'] == 1

    def test_three_point_vanishes(self):
        """3-point = 0 (odd n)."""
        result = n_point_p1([0, 0, 0])
        assert result['value'] == 0

    def test_four_point_3_channels(self):
        """4-point has 3 channels (3!! = 3)."""
        result = n_point_p1([0, 0, 0, 0])
        assert result['num_channels'] == 3

    def test_six_point_15_channels(self):
        """6-point has 15 channels (5!! = 15)."""
        result = n_point_p1([0, 0, 0, 0, 0, 0])
        assert result['num_channels'] == 15

    def test_four_point_same_index_all_nonzero(self):
        """<J_0 J_0 J_0 J_0>: all 3 channels nonzero."""
        result = n_point_p1([0, 0, 0, 0])
        assert result['nonzero_channels'] == 3

    def test_four_point_mixed_indices(self):
        """<J_0 J_0 J_5 J_5>: only s-channel nonzero."""
        # s: (01)(23) -> omega^{00} * omega^{55} = 1*1 = 1
        # t: (02)(13) -> omega^{05} * omega^{05} = 0
        # u: (03)(12) -> omega^{05} * omega^{05} = 0
        result = n_point_p1([0, 0, 5, 5])
        assert result['nonzero_channels'] == 1

    def test_four_point_orthogonal_vanishes(self):
        """<J_0 J_1 J_2 J_3>: all channels vanish (all off-diagonal)."""
        result = n_point_p1([0, 1, 2, 3])
        assert result['nonzero_channels'] == 0


class TestDoubleFactorial:
    """Double factorial (n-1)!! counts Wick pairings."""

    def test_double_factorial_values(self):
        """Known values: 1!!=1, 3!!=3, 5!!=15, 7!!=105."""
        # VERIFIED: [DC] direct computation, [LT] OEIS A001147
        assert double_factorial(1) == 1
        assert double_factorial(3) == 3
        assert double_factorial(5) == 15
        assert double_factorial(7) == 105

    def test_num_pairings_even(self):
        """num_wick_pairings(n) = (n-1)!! for even n."""
        # VERIFIED: [DC] enumeration, [LT] Isserlis theorem
        assert num_wick_pairings(0) == 1
        assert num_wick_pairings(2) == 1
        assert num_wick_pairings(4) == 3
        assert num_wick_pairings(6) == 15
        assert num_wick_pairings(8) == 105

    def test_num_pairings_odd_zero(self):
        """num_wick_pairings(n) = 0 for odd n."""
        for n in [1, 3, 5, 7, 9]:
            assert num_wick_pairings(n) == 0

    def test_wick_pairings_enumeration_n2(self):
        """Explicit pairings for n=2: one pairing."""
        pairings = wick_pairings([0, 1])
        assert len(pairings) == 1
        assert pairings[0] == [(0, 1)]

    def test_wick_pairings_enumeration_n4(self):
        """Explicit pairings for n=4: three pairings."""
        pairings = wick_pairings([0, 1, 2, 3])
        assert len(pairings) == 3
        # All should be different
        pairing_sets = [frozenset(frozenset(p) for p in pair) for pair in pairings]
        assert len(set(pairing_sets)) == 3

    def test_wick_pairings_odd_empty(self):
        """Odd number of elements: no pairings."""
        assert wick_pairings([0, 1, 2]) == []


# =========================================================================
# Section 5: Four-point function
# =========================================================================

class TestFourPoint:
    """4-point function via Wick with 3 channels (s, t, u)."""

    def test_num_channels(self):
        """Always 3 channels for 4-point."""
        for i, j, k, l in [(0, 0, 0, 0), (0, 1, 2, 3), (0, 0, 5, 5)]:
            result = four_point_p1(i, j, k, l)
            assert result['num_channels'] == 3

    def test_same_index_total(self):
        """<J_0 J_0 J_0 J_0>: total omega = 3."""
        # VERIFIED: [DC] 3 channels each contribute 1,
        # [LT] free boson c=1 Wick (Polchinski Ch. 2)
        result = four_point_p1(0, 0, 0, 0)
        assert result['total_omega_coefficient'] == 3

    def test_negative_index_total(self):
        """<J_5 J_5 J_5 J_5>: total omega = 3 ((-1)^2 = 1 per channel)."""
        # VERIFIED: [DC] each channel: (-1)*(-1) = 1, three channels: 3
        # [SY] omega^{55}*omega^{55} = (-1)^2 = 1
        result = four_point_p1(5, 5, 5, 5)
        assert result['total_omega_coefficient'] == 3

    def test_two_pairs(self):
        """<J_0 J_0 J_5 J_5>: only s-channel survives, total = -1."""
        # VERIFIED: [DC] s: omega^{00}*omega^{55} = (+1)*(-1) = -1,
        # t and u vanish (omega^{05} = 0)
        # [SY] sign from indefinite Mukai pairing: positive x negative = negative
        result = four_point_p1(0, 0, 5, 5)
        assert result['s_channel']['omega_product'] == -1
        assert result['t_channel']['omega_product'] == 0
        assert result['u_channel']['omega_product'] == 0
        assert result['total_omega_coefficient'] == -1

    def test_alternating_indices(self):
        """<J_0 J_5 J_0 J_5>: only t-channel survives, total = -1."""
        # VERIFIED: [DC] s: omega^{05}*omega^{05} = 0,
        # t: omega^{00}*omega^{55} = (+1)*(-1) = -1, u: omega^{05}*omega^{50} = 0
        # [SY] sign from indefinite Mukai pairing
        result = four_point_p1(0, 5, 0, 5)
        assert result['s_channel']['omega_product'] == 0
        assert result['t_channel']['omega_product'] == -1
        assert result['u_channel']['omega_product'] == 0
        assert result['total_omega_coefficient'] == -1

    def test_all_different_vanishes(self):
        """<J_0 J_1 J_2 J_3>: all channels vanish, total = 0."""
        # VERIFIED: [DC] all omega^{ij} = 0 for i != j in diagonal basis
        result = four_point_p1(0, 1, 2, 3)
        assert result['total_omega_coefficient'] == 0

    def test_crossing_symmetry(self):
        """Crossing: <J_i J_j J_k J_l> swapping (j,k) exchanges s <-> t."""
        r1 = four_point_p1(0, 0, 5, 5)
        r2 = four_point_p1(0, 5, 0, 5)
        # Swapping 2nd and 3rd indices exchanges s and t channels
        assert r1['s_channel']['omega_product'] == r2['t_channel']['omega_product']
        assert r1['t_channel']['omega_product'] == r2['s_channel']['omega_product']


# =========================================================================
# Section 6: Stress tensor correlator
# =========================================================================

class TestStressTensor:
    """<T(z)T(w)> = c/2 (z-w)^{-4} with c = 24."""

    def test_central_charge(self):
        """c = 24 = rank of Mukai lattice = kappa_fiber (AP113)."""
        # VERIFIED: [DC] Sugawara trace, [LT] Frenkel-Ben-Zvi (2004)
        # [CF] cross-check with k3_double_current_algebra.py MUKAI_RANK = 24
        result = stress_tensor_two_point()
        assert result.central_charge == 24

    def test_coefficient_c_over_2(self):
        """Coefficient is c/2 = 12."""
        # VERIFIED: [DC] Wick contraction of normal-ordered products,
        # [LT] Virasoro algebra (BPZ 1984)
        result = stress_tensor_two_point()
        assert result.coefficient == F(12)

    def test_singularity_order_4(self):
        """Singularity is (z-w)^{-4}."""
        result = stress_tensor_two_point()
        assert result.singularity_order == 4

    def test_proved_status(self):
        """Result is PROVED (Sugawara)."""
        result = stress_tensor_two_point()
        assert 'PROVED' in result.proof_status

    def test_cross_check_central_charge_rank(self):
        """Cross-check c = 24 against Mukai rank from k3_double_current_algebra."""
        from compute.lib.k3_double_current_algebra import MUKAI_RANK
        result = stress_tensor_two_point()
        assert result.central_charge == MUKAI_RANK

    def test_cross_check_central_charge_chiral_homology(self):
        """Cross-check c = 24 against chiral_homology_ran_k3 constant."""
        from compute.lib.chiral_homology_ran_k3 import CENTRAL_CHARGE_HMUK
        result = stress_tensor_two_point()
        assert result.central_charge == CENTRAL_CHARGE_HMUK

    def test_ope_data_virasoro(self):
        """OPE data contains Virasoro algebra structure."""
        ope = stress_tensor_ope_data()
        assert ope['central_charge'] == 24
        # Three singular terms: (z-w)^{-4}, (z-w)^{-2}, (z-w)^{-1}
        assert len(ope['ope_singular_terms']) == 3
        # Check orders
        orders = [t['order'] for t in ope['ope_singular_terms']]
        assert orders == [-4, -2, -1]

    def test_virasoro_c_over_12(self):
        """c/12 = 2 (appears in mode commutator)."""
        # VERIFIED: [DC] c/12 = 24/12 = 2, [LT] Virasoro algebra
        ope = stress_tensor_ope_data()
        assert ope['virasoro_algebra']['c_over_12'] == F(2)


# =========================================================================
# Section 7: Elliptic curve correlators
# =========================================================================

class TestEllipticCorrelators:
    """<J_i(z) J_j(w)>_E = omega^{ij} * wp(z-w, tau)."""

    def test_diagonal_positive_nonzero(self):
        """<J_0(z) J_0(w)>_E != 0 (positive direction)."""
        result = elliptic_two_point(0, 0)
        assert result.omega_ij == 1

    def test_diagonal_negative_nonzero(self):
        """<J_5(z) J_5(w)>_E != 0 (negative direction)."""
        result = elliptic_two_point(5, 5)
        assert result.omega_ij == -1

    def test_off_diagonal_zero(self):
        """<J_0(z) J_1(w)>_E = 0."""
        result = elliptic_two_point(0, 1)
        assert result.omega_ij == 0

    def test_ap156_compliance(self):
        """AP156: Weierstrass convention is specified."""
        result = elliptic_two_point(0, 0)
        assert 'Weierstrass' in result.weierstrass_function

    def test_quasi_periodicity_stated(self):
        """Quasi-periodicity of wp is stated."""
        result = elliptic_two_point(0, 0)
        assert 'periodic' in result.quasi_periodicity.lower()

    def test_p1_limit_stated(self):
        """Degeneration to P^1 is documented."""
        result = elliptic_two_point(0, 0)
        assert '1/u^2' in result.p1_limit or 'P^1' in result.p1_limit

    def test_omega_matches_p1(self):
        """Same omega^{ij} as on P^1 (geometry-independent)."""
        for i in range(24):
            for j in [i, (i + 1) % 24]:
                e_val = elliptic_two_point(i, j).omega_ij
                p1_val = two_point_p1(i, j).omega_ij
                assert e_val == p1_val, f"omega mismatch at ({i},{j})"

    def test_proved_status(self):
        """Elliptic correlators are PROVED."""
        result = elliptic_two_point(0, 0)
        assert 'PROVED' in result.proof_status

    def test_elliptic_matrix_structure(self):
        """24x24 elliptic matrix has correct structure."""
        mat = elliptic_two_point_matrix()
        assert mat['matrix_size'] == (24, 24)
        assert mat['signature'] == (4, 20)
        assert 'wp' in mat['propagator'] or 'Weierstrass' in mat['propagator']

    def test_weierstrass_laurent(self):
        """Laurent expansion of wp has correct leading term."""
        coeffs = weierstrass_p_laurent_coefficients()
        assert -2 in coeffs
        assert coeffs[-2] == '1'  # leading term 1/u^2


# =========================================================================
# Section 8: Partition function
# =========================================================================

class TestPartitionFunction:
    """Z(E, tau) = 1/eta(tau)^{24}."""

    def test_central_charge(self):
        """c = 24."""
        pf = partition_function_elliptic()
        assert pf.central_charge == 24

    def test_l0_shift(self):
        """L_0 shift = c/24 = 1."""
        # VERIFIED: [DC] 24/24 = 1, [LT] Zhu (1996)
        pf = partition_function_elliptic()
        assert pf.l0_shift == F(1)

    def test_modular_weight(self):
        """Modular weight = -c/2 = -12."""
        # VERIFIED: [DC] -24/2 = -12, [LT] eta^{-24} has weight -12
        pf = partition_function_elliptic()
        assert pf.modular_weight == F(-12)

    def test_p24_0(self):
        """p_{24}(0) = 1."""
        # VERIFIED: [DC] empty partition, [LT] Gottsche (1990)
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[0] == 1

    def test_p24_1(self):
        """p_{24}(1) = 24."""
        # VERIFIED: [DC] 24 colours one part, [LT] Gottsche (1990)
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[1] == 24

    def test_p24_2(self):
        """p_{24}(2) = 324 = C(25,2) + 24."""
        # VERIFIED: [DC] two-part + single-part,
        # [LT] Gottsche (1990) chi(Hilb^2(K3)) = 324
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[2] == 324

    def test_p24_3(self):
        """p_{24}(3) = 3200."""
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990)
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[3] == 3200

    def test_p24_4(self):
        """p_{24}(4) = 25650."""
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990)
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[4] == 25650

    def test_p24_5(self):
        """p_{24}(5) = 176256."""
        # VERIFIED: [DC] recursion, [LT] Gottsche (1990)
        pf = partition_function_elliptic()
        assert pf.q_expansion_coefficients[5] == 176256

    def test_cross_check_gottsche(self):
        """Cross-check against GOTTSCHE_COEFFICIENTS from chiral_homology_ran_k3."""
        from compute.lib.chiral_homology_ran_k3 import GOTTSCHE_COEFFICIENTS
        pf = partition_function_elliptic(max_degree=6)
        for n, expected in GOTTSCHE_COEFFICIENTS.items():
            assert pf.q_expansion_coefficients[n] == expected, \
                f"p_24({n}): got {pf.q_expansion_coefficients[n]}, expected {expected}"

    def test_cross_check_chiral_homology_character(self):
        """Cross-check against chiral_homology_e_heisenberg character."""
        from compute.lib.chiral_homology_ran_k3 import chiral_homology_e_heisenberg
        ch = chiral_homology_e_heisenberg(max_degree=6)
        pf = partition_function_elliptic(max_degree=6)
        for n in range(7):
            assert pf.q_expansion_coefficients[n] == ch.character_coefficients[n], \
                f"n={n}: correlator {pf.q_expansion_coefficients[n]} != ch {ch.character_coefficients[n]}"

    def test_proved_status(self):
        """Partition function is PROVED."""
        pf = partition_function_elliptic()
        assert 'PROVED' in pf.proof_status

    def test_modular_group(self):
        """Modular group is SL_2(Z)."""
        pf = partition_function_elliptic()
        assert 'SL_2(Z)' in pf.modular_group


class TestPartitionFunctionGenusG:
    """Partition function at various genera."""

    def test_genus0(self):
        """Z_0 = 1."""
        result = partition_function_genus_g(0)
        assert 'vacuum' in result['formula'].lower() or '1' in result['formula']

    def test_genus1(self):
        """Z_1 = 1/eta^{24}."""
        result = partition_function_genus_g(1)
        assert 'eta' in result['formula']
        assert result['modular_weight'] == -12

    def test_genus2(self):
        """Z_2 = 1/chi_{10}^2."""
        result = partition_function_genus_g(2)
        assert 'chi_{10}' in result['formula'] or 'chi_10' in result['formula']
        assert result['modular_weight'] == -20

    def test_genus2_weight_cross_check(self):
        """Genus-2 weight -20 = -10 * c/12 = -10 * 2."""
        # VERIFIED: [DC] -10 * 24/12 = -20,
        # [LT] Igusa cusp form chi_{10} has weight 10
        result = partition_function_genus_g(2)
        expected = -10 * 24 // 12
        assert result['modular_weight'] == expected

    def test_genus3_modular_group(self):
        """Genus-3 modular group is Sp_6(Z)."""
        result = partition_function_genus_g(3)
        assert 'Sp_6' in result['modular_group'] or 'Sp_{6}' in result['modular_group']


# =========================================================================
# Section 9: Yangian-deformed correlators (CONJECTURAL)
# =========================================================================

class TestYangianDeformed:
    """K3 Yangian deformed correlators: all CONJECTURAL (AP-CY14)."""

    def test_conjectural_status(self):
        """All Yangian results are CONJECTURAL."""
        result = yangian_deformed_two_point()
        assert result.status == 'CONJECTURAL'

    def test_conditions_stated(self):
        """Conditions for Yangian deformation are stated."""
        result = yangian_deformed_two_point()
        assert len(result.conditions) > 0
        conditions_text = ' '.join(result.conditions)
        assert 'CY-A' in conditions_text or 'AP-CY14' in conditions_text

    def test_classical_part(self):
        """Classical part is c/2 (z-w)^{-4} = 12 / (z-w)^4."""
        result = yangian_deformed_two_point()
        assert '12' in result.classical_part or 'c/2' in result.classical_part

    def test_ap_cy31_compliance(self):
        """AP-CY31: spectral parameter != worldsheet coordinate."""
        result = yangian_deformed_two_point()
        assert 'spectral' in result.spectral_parameter_note.lower()
        assert 'worldsheet' in result.spectral_parameter_note.lower()

    def test_structure_function_connection(self):
        """Deformation connected to g_{K3}(u) structure function."""
        result = yangian_deformed_two_point()
        assert 'g_{K3}' in result.structure_function

    def test_deformed_propagator_conjectural(self):
        """Deformed propagator is CONJECTURAL."""
        result = yangian_deformed_propagator_p1()
        assert 'CONJECTURAL' in result['status']

    def test_deformed_partition_conjectural(self):
        """Deformed partition function is CONJECTURAL."""
        result = yangian_deformed_partition_function()
        assert 'CONJECTURAL' in result['status']

    def test_deformed_partition_borcherds(self):
        """Deformed partition function involves Borcherds product."""
        result = yangian_deformed_partition_function()
        assert 'Borcherds' in result['borcherds_connection']


# =========================================================================
# Section 10: Ran space structure
# =========================================================================

class TestRanSpaceStructure:
    """Ran space structure underlying correlators."""

    def test_ran_2point(self):
        """2-point lives on |S| = 2 subset."""
        result = ran_space_correlator_structure(2)
        assert result.num_points == 2

    def test_ran_4point(self):
        """4-point lives on |S| = 4 subset."""
        result = ran_space_correlator_structure(4)
        assert result.num_points == 4

    def test_factorization_property_stated(self):
        """Factorization property is documented."""
        result = ran_space_correlator_structure(2)
        assert 'factorization' in result.factorization_property.lower()

    def test_e1_ordering(self):
        """E_1 ordering is documented (AP152)."""
        result = ran_space_correlator_structure(2)
        assert 'E_1' in result.e1_ordering
        assert 'labeled' in result.e1_ordering.lower()

    def test_excision_coproduct(self):
        """Excision coproduct from Ran diagonal."""
        result = ran_space_correlator_structure(4)
        assert 'coproduct' in result.excision_coproduct.lower()

    def test_proved_status(self):
        """Ran space structure is PROVED."""
        result = ran_space_correlator_structure(2)
        assert 'PROVED' in result.proof_status


# =========================================================================
# Section 11: Verification suite
# =========================================================================

class TestVerificationSuite:
    """Full verification suite running all cross-checks."""

    def test_verify_two_point(self):
        result = verify_two_point_p1()
        assert result['signature_match'] is True
        assert result['all_diagonal_nonzero'] is True
        assert result['all_offdiag_zero'] is True

    def test_verify_four_point(self):
        result = verify_four_point_diagonal()
        assert result['J0J0J0J0']['match'] is True
        assert result['J0J0J0J0']['expected'] == 3
        assert result['J0J0J5J5']['match'] is True
        assert result['J0J0J5J5']['expected'] == -1  # positive x negative
        assert result['J0J1J0J1']['match'] is True
        assert result['J0J1J0J1']['expected'] == 1   # positive x positive
        assert result['J0J5J0J5']['match'] is True
        assert result['J0J5J0J5']['expected'] == -1  # positive x negative

    def test_verify_stress_tensor(self):
        result = verify_stress_tensor()
        assert result['c_match'] is True
        assert result['coeff_match'] is True
        assert result['order_match'] is True

    def test_verify_partition_function(self):
        result = verify_partition_function()
        assert result['shift_match'] is True
        assert result['weight_match'] is True
        assert result['gottsche_match'] is True

    def test_verify_wick_counting(self):
        result = verify_wick_counting()
        for n, data in result.items():
            assert data['match'] is True, f"Wick counting failed at n={n}"

    def test_verify_elliptic_degeneration(self):
        result = verify_elliptic_degeneration()
        assert result['omega_values_agree'] is True

    def test_full_verification(self):
        """Run full_correlator_verification and check all paths."""
        result = full_correlator_verification()
        assert result['path1_two_point_p1']['signature_match'] is True
        assert result['path3_stress_tensor']['c_match'] is True
        assert result['path4_partition_function']['gottsche_match'] is True
        assert result['path6_elliptic_degeneration']['omega_values_agree'] is True


# =========================================================================
# Section 12: Cross-engine consistency
# =========================================================================

class TestCrossEngineConsistency:
    """Cross-checks with other Vol III compute engines."""

    def test_rank_agrees_k3_dca(self):
        """Rank 24 matches k3_double_current_algebra MUKAI_RANK."""
        from compute.lib.k3_double_current_algebra import MUKAI_RANK
        assert RANK == MUKAI_RANK

    def test_signature_agrees_k3_dca(self):
        """Signature (4,20) matches k3_double_current_algebra."""
        from compute.lib.k3_double_current_algebra import MUKAI_SIG_PLUS, MUKAI_SIG_MINUS
        omega = mukai_pairing_matrix()
        assert omega.signature[0] == MUKAI_SIG_PLUS
        assert omega.signature[1] == MUKAI_SIG_MINUS

    def test_central_charge_agrees_chiral_homology(self):
        """c = 24 matches chiral_homology_ran_k3 CENTRAL_CHARGE_HMUK."""
        from compute.lib.chiral_homology_ran_k3 import CENTRAL_CHARGE_HMUK
        assert CENTRAL_CHARGE == CENTRAL_CHARGE_HMUK

    def test_drinfeld_double_dim_49(self):
        """Drinfeld double has dim 49 = 2*24 + 1."""
        from compute.lib.drinfeld_center_k3_heisenberg import DRINFELD_DOUBLE_DIM
        assert DRINFELD_DOUBLE_DIM == 2 * RANK + 1

    def test_partition_function_agrees_fh(self):
        """Partition function coefficients agree with k3_factorization_homology."""
        from compute.lib.k3_factorization_homology import tree_level_character_coefficients
        fh_coeffs = tree_level_character_coefficients(6)
        pf = partition_function_elliptic(max_degree=6)
        for n in range(7):
            assert pf.q_expansion_coefficients[n] == fh_coeffs[n], \
                f"n={n}: correlator {pf.q_expansion_coefficients[n]} != FH {fh_coeffs[n]}"

    def test_kappa_spectrum_agrees_summary(self):
        """kappa values agree with chiral_homology_summary."""
        from compute.lib.chiral_homology_ran_k3 import chiral_homology_summary
        summary = chiral_homology_summary()
        assert summary['kappa_ch'] == KAPPA_CH
        assert summary['kappa_cat'] == KAPPA_CAT
        assert summary['kappa_BKM'] == KAPPA_BKM
        assert summary['kappa_fiber'] == KAPPA_FIBER
