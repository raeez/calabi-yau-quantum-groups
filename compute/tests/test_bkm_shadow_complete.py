r"""
Tests for bkm_shadow_complete.py: comprehensive BKM shadow obstruction tower computation.

Covers all 8 computation targets:
1. Monster Lie algebra: denominator formula, first 5 coefficients
2. Fake Monster Lie algebra: multiplicities, shadow difference
3. Borcherds products from shadow: Leech lattice multiplicities
4. BKM from CY: conifold BPS algebra
5. Generalized denominator from shadow: Hecke operators
6. Igusa cusp form chi_10: Fourier coefficients
7. Enriques surface BKM: lattice data
8. Modularity of root multiplicities: shadow invariants

55+ tests organized by section.
"""

import math
import os
import sys
import importlib.util
from fractions import Fraction

import pytest

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'bkm_shadow_complete',
    os.path.join(_lib_dir, 'bkm_shadow_complete.py')
)
bkm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bkm)


# =========================================================================
# 1. MONSTER LIE ALGEBRA
# =========================================================================

class TestMonsterMultiplicities:
    """Verify Monster Lie algebra root multiplicities c(n) = dim V^natural_n."""

    def test_c1_value(self):
        """c(1) = 196884 (the famous moonshine number)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[1] == 196884

    def test_c2_value(self):
        """c(2) = 21493760."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[2] == 21493760

    def test_c3_value(self):
        """c(3) = 864299970."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[3] == 864299970

    def test_c4_value(self):
        """c(4) = 20245856256."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[4] == 20245856256

    def test_c5_value(self):
        """c(5) = 333202640600."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[5] == 333202640600

    def test_c1_is_196883_plus_1(self):
        """c(1) = 196883 + 1 (McKay's observation: dim(V_1) = dim(rho_1) + 1)."""
        # 196883 is the dimension of the smallest nontrivial irrep of the Monster.
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.MONSTER_MULTIPLICITIES[1] == 196883 + 1

    def test_multiplicities_positive(self):
        """All Monster multiplicities are positive (V^natural is a genuine module)."""
        for n, c_n in bkm.MONSTER_MULTIPLICITIES.items():
            # VERIFIED [DC] positivity check [CF] cross-family census
            assert c_n > 0, f"c({n}) = {c_n} is not positive"

    def test_multiplicities_grow(self):
        """c(n) is strictly increasing for n >= 1."""
        ns = sorted(bkm.MONSTER_MULTIPLICITIES.keys())
        for i in range(1, len(ns)):
            assert bkm.MONSTER_MULTIPLICITIES[ns[i]] > bkm.MONSTER_MULTIPLICITIES[ns[i - 1]]


class TestMonsterJFunction:
    """Verify the j-function coefficient table."""

    def test_j_minus1(self):
        """j(tau) - 744 has leading coefficient c(-1) = 1 (the q^{-1} term)."""
        j = bkm.j_function_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert j[-1] == 1

    def test_j_zero(self):
        """j(tau) - 744 has c(0) = 0 (the constant term vanishes after subtraction)."""
        j = bkm.j_function_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert j[0] == 0

    def test_j_positive_match_multiplicities(self):
        """j-function coefficients match Monster multiplicities for n >= 1."""
        j = bkm.j_function_coefficients(5)
        for n in range(1, 6):
            assert j[n] == bkm.MONSTER_MULTIPLICITIES[n]


class TestMonsterDenominator:
    """Verify the Monster denominator formula log-coefficients."""

    def test_log_coeff_11(self):
        """Log coefficient at (1,1) is -c(1) = -196884."""
        log = bkm.monster_denominator_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[(1, 1)] == Fraction(-196884)

    def test_log_coeff_21(self):
        """Log coefficient at (2,1) is -c(2) = -21493760."""
        log = bkm.monster_denominator_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[(2, 1)] == Fraction(-21493760)

    def test_log_coeff_12(self):
        """Log coefficient at (1,2) is -c(2) = -21493760 (symmetry)."""
        log = bkm.monster_denominator_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[(1, 2)] == Fraction(-21493760)

    def test_log_coeff_22(self):
        """Log coefficient at (2,2) is -c(4) - c(1)/2.

        From the expansion: the (2,2) term gets:
          -c(2*2)/1 from the (m=2,n=2,k=1) term: -c(4)
          -c(1*1)/2 from the (m=1,n=1,k=2) term: -c(1)/2
        Total: -c(4) - c(1)/2 = -20245856256 - 98442 = -20245954698
        """
        log = bkm.monster_denominator_coefficients(5)
        expected = Fraction(-bkm.MONSTER_MULTIPLICITIES[4]) + Fraction(-bkm.MONSTER_MULTIPLICITIES[1], 2)
        assert log[(2, 2)] == expected

    def test_log_coeff_31(self):
        """Log coefficient at (3,1) is -c(3) = -864299970."""
        log = bkm.monster_denominator_coefficients(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[(3, 1)] == Fraction(-864299970)

    def test_verify_leading_terms(self):
        """The verification function reports all matches."""
        result = bkm.verify_monster_denominator_leading(5)
        assert result['all_match']

    def test_monster_kappa(self):
        """Monster shadow kappa = 1 (Weyl vector coefficient)."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert bkm.monster_kappa() == 1


class TestMonsterDenominatorFirstFive:
    """Verify the first 5 log-coefficients of the Monster denominator."""

    def test_all_log_match(self):
        """All log-coefficient cross-checks pass."""
        result = bkm.monster_denominator_verify_first_5()
        assert result['all_log_match']


# =========================================================================
# 2. FAKE MONSTER LIE ALGEBRA
# =========================================================================

class TestFakeMonster:
    """Verify Fake Monster Lie algebra properties."""

    def test_lightlike_multiplicity_24(self):
        """Lightlike imaginary roots (norm 0) have multiplicity 24."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.fake_monster_multiplicity(0) == 24

    def test_norm_minus2_multiplicity(self):
        """Norm -2 roots have multiplicity p_{24}(2) = 324."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.fake_monster_multiplicity(-2) == 324

    def test_norm_minus4_multiplicity(self):
        """Norm -4 roots have multiplicity p_{24}(3) = 3200."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.fake_monster_multiplicity(-4) == 3200

    def test_denominator_weight(self):
        """Fake Monster denominator Phi_12 has weight 12."""
        # VERIFIED [DC] conformal weight [CF] cross-family census
        assert bkm.fake_monster_denominator_weight() == 12


class TestShadowDifference:
    """Shadow difference between Monster and Fake Monster."""

    def test_shadow_kappas_differ(self):
        """Monster kappa = 1, Fake Monster kappa = 12."""
        diff = bkm.shadow_difference_monster_fake()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert diff['shadow_kappa_monster'] == 1
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert diff['shadow_kappa_fake_monster'] == 12

    def test_monster_grows_faster(self):
        """Monster multiplicities grow faster than Fake Monster at each level."""
        diff = bkm.shadow_difference_monster_fake()
        for n, data in diff['level_comparison'].items():
            if data['fake_monster_p24'] > 0:
                # Monster c(n) >> Fake Monster p_{24} at the same level
                # VERIFIED [DC] structural property [CF] cross-family census
                assert data['ratio'] > 1, (
                    f"At n={n}: Monster c(n)={data['monster_c(n)']} vs "
                    f"Fake p24={data['fake_monster_p24']}"
                )


# =========================================================================
# 3. BORCHERDS PRODUCTS FROM SHADOW (Leech lattice)
# =========================================================================

class TestLeechLattice:
    """Verify Leech lattice Borcherds product multiplicities."""

    def test_weyl_vector_coefficient(self):
        """c(-1) = 1 for the Leech lattice input (= p_{24}(0))."""
        mult = bkm.leech_lattice_multiplicities(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[-1] == 1

    def test_lightlike_24(self):
        """c(0) = 24 for the Leech lattice input (= p_{24}(1))."""
        mult = bkm.leech_lattice_multiplicities(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[0] == 24

    def test_c1_equals_324(self):
        """c(1) = p_{24}(2) = 324."""
        mult = bkm.leech_lattice_multiplicities(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[1] == 324

    def test_c2_equals_3200(self):
        """c(2) = p_{24}(3) = 3200."""
        mult = bkm.leech_lattice_multiplicities(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[2] == 3200

    def test_c3_equals_25650(self):
        """c(3) = p_{24}(4) = 25650."""
        mult = bkm.leech_lattice_multiplicities(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[3] == 25650

    def test_weight_12(self):
        """Borcherds product for Leech has weight c(0)/2 = 12."""
        # VERIFIED [DC] conformal weight [CF] cross-family census
        assert bkm.borcherds_product_weight_leech() == 12

    def test_leech_theta_no_norm2(self):
        """Leech lattice has no vectors of norm 2 (minimum norm is 4)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.LEECH_THETA_COEFFICIENTS[1] == 0

    def test_leech_theta_norm4(self):
        """Leech lattice has 196560 vectors of norm 4."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.LEECH_THETA_COEFFICIENTS[2] == 196560


# =========================================================================
# 4. BKM FROM CALABI-YAU (Conifold)
# =========================================================================

class TestConifoldBPS:
    """Verify conifold BPS algebra."""

    def test_bps_invariants_alternating(self):
        """Omega(d) = (-1)^{d-1}: alternating +1, -1, +1, -1, ..."""
        omega = bkm.conifold_bps_invariants(5)
        # VERIFIED [DC] BPS state [CF] cross-family census
        assert omega[1] == 1
        # VERIFIED [DC] BPS state [CF] cross-family census
        assert omega[2] == -1
        # VERIFIED [DC] BPS state [CF] cross-family census
        assert omega[3] == 1
        # VERIFIED [DC] BPS state [CF] cross-family census
        assert omega[4] == -1
        # VERIFIED [DC] BPS state [CF] cross-family census
        assert omega[5] == 1

    def test_denominator_leading_coefficients(self):
        """First coefficients of the conifold denominator product.

        prod_{d>0} (1-q^d)^{(-1)^{d-1}} = 1/prod_{k odd}(1-q^k)
        = 1 + q + q^2 + 2q^3 + 2q^4 + 3q^5 + ...
        (distinct partition / odd partition numbers)
        """
        coeffs = bkm.conifold_denominator_coefficients(10)
        expected = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 8, 10: 10}
        for n, exp in expected.items():
            assert coeffs[n] == exp, f"At n={n}: got {coeffs[n]}, expected {exp}"

    def test_distinct_partition_match(self):
        """Conifold denominator matches distinct partition generating function."""
        result = bkm.identify_conifold_automorphic_form()
        assert result['distinct_partition_match']

    def test_conifold_is_eta_quotient(self):
        """The automorphic form is eta(2tau)/eta(tau) (up to q-shift)."""
        result = bkm.identify_conifold_automorphic_form()
        assert 'eta' in result['automorphic_form']

    def test_conifold_modular_group(self):
        """The conifold form has Gamma_0(2) modularity."""
        result = bkm.identify_conifold_automorphic_form()
        assert 'Gamma_0(2)' in result['modular_group']


class TestConifoldLogDenominator:
    """Verify log-expansion of the conifold denominator."""

    def test_log_coeff_1(self):
        """Log coefficient at q^1: -Omega(1)/1 = -1/1 = -1.

        Actually: sum_{d|1} (-1)^d / (1/d) = (-1)^1 / 1 = -1.
        But from conifold_log_denominator: -Omega(d) = -(-1)^{d-1} gives
        at d=1, k=1: -(-1)^{1-1}/1 = -1/1 = -1. Correct.
        """
        log = bkm.conifold_log_denominator(10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[1] == Fraction(-1)

    def test_log_coeff_2(self):
        """Log coefficient at q^2.

        d=1, k=2: -Omega(1)/2 = -1/2
        d=2, k=1: -Omega(2)/1 = -(-1)/1 = 1
        Total: -1/2 + 1 = 1/2
        """
        log = bkm.conifold_log_denominator(10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[2] == Fraction(1, 2)

    def test_log_coeff_3(self):
        """Log coefficient at q^3.

        d=1, k=3: -1/3
        d=3, k=1: -1/1 = -1
        Total: -1/3 - 1 = -4/3
        """
        log = bkm.conifold_log_denominator(10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[3] == Fraction(-4, 3)


# =========================================================================
# 5. GENERALIZED DENOMINATOR FROM SHADOW
# =========================================================================

class TestHeckeOperator:
    """Verify Hecke operator on multiplicity sequences."""

    def test_hecke_T1_is_identity(self):
        """T_1 applied to c gives c itself (T_1 = identity).

        (T_1 c)(n) = sum_{d|gcd(1,n)} d * c(n/d^2)
        Since gcd(1,n)=1, only d=1: c(n).
        """
        c = {1: 10, 2: 20, 3: 30}
        result = bkm.hecke_operator_on_multiplicities(c, 1, 5)
        for n in range(1, 4):
            # VERIFIED [DC] structural property [CF] cross-family census
            assert result.get(n, Fraction(0)) == Fraction(c[n])

    def test_hecke_T2_on_simple(self):
        """T_2 on c = {1: 1}.

        (T_2 c)(n) = sum_{d|gcd(2,n)} d * c(2n/d^2)
        For n=1: gcd(2,1)=1, d=1: c(2) = 0. Result: 0.
        For n=2: gcd(2,2)=2, d in {1,2}.
          d=1: c(4) = 0.
          d=2: 2*c(1) = 2*1 = 2. Result: 2.
        """
        c = {1: 1}
        result = bkm.hecke_operator_on_multiplicities(c, 2, 5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result.get(1, Fraction(0)) == Fraction(0)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result.get(2, Fraction(0)) == Fraction(2)


class TestShadowGenusDecomposition:
    """Verify genus decomposition of log-denominator."""

    def test_genus1_is_multiplicities(self):
        """Genus-1 contribution F_1(q) = -sum c(n) q^n.

        F_1 at q^n = -c(n)/1 = -c(n).
        """
        c = {1: 5, 2: 10, 3: 15}
        decomp = bkm.shadow_genus_decomposition(c, max_genus=3, max_n=5)
        f1 = decomp[1]
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f1.get(1, Fraction(0)) == Fraction(-5)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f1.get(2, Fraction(0)) == Fraction(-10)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f1.get(3, Fraction(0)) == Fraction(-15)

    def test_genus2_coefficient(self):
        """Genus-2 contribution F_2 at q^{2n} = -c(n)/2."""
        c = {1: 6, 2: 12}
        decomp = bkm.shadow_genus_decomposition(c, max_genus=3, max_n=10)
        f2 = decomp[2]
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f2.get(2, Fraction(0)) == Fraction(-6, 2)  # = -3
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert f2.get(4, Fraction(0)) == Fraction(-12, 2)  # = -6

    def test_reconstruction(self):
        """Sum of genus contributions reconstructs the full log.

        With c = {1: 196884, 2: 21493760}, the full log at q^N gets
        contributions from k up to N (genus k from n*k=N). For N=6
        we need genus up to 6. We use max_genus >= max_n.
        """
        c = {1: 196884, 2: 21493760}
        result = bkm.verify_log_reconstruction(c, max_genus=10, max_n=6)
        assert result['match'], f"Reconstruction failed: {result['errors']}"


class TestLogReconstruction:
    """Verify that genus decomposition reconstructs full log."""

    def test_monster_reconstruction(self):
        """Monster multiplicities: genus sum = full log."""
        # Use first 3 Monster multiplicities
        c = {n: bkm.MONSTER_MULTIPLICITIES[n] for n in range(1, 4)}
        result = bkm.verify_log_reconstruction(c, max_genus=5, max_n=5)
        assert result['match']

    def test_conifold_reconstruction(self):
        """Conifold: genus sum = full log."""
        c = bkm.conifold_bps_invariants(5)
        result = bkm.verify_log_reconstruction(c, max_genus=5, max_n=5)
        assert result['match']

    def test_fake_monster_reconstruction(self):
        """Fake Monster (simplified): genus sum = full log."""
        c = {1: 24, 2: 324, 3: 3200}
        result = bkm.verify_log_reconstruction(c, max_genus=5, max_n=5)
        assert result['match']


# =========================================================================
# 6. IGUSA CUSP FORM chi_10
# =========================================================================

class TestIgusaFourierCoefficients:
    """Verify phi_{0,1} Fourier coefficients (Igusa input)."""

    def test_all_coefficients_match(self):
        """All verified phi_{0,1} coefficients match known values."""
        result = bkm.verify_igusa_fourier_coefficients()
        if result.get('status') == 'phi01_fourier not available':
            pytest.skip("phi01_fourier module not available")
        assert result['all_match']

    def test_c_minus1(self):
        """c(-1) = 1 (polar coefficient)."""
        result = bkm.verify_igusa_fourier_coefficients()
        if result.get('status') == 'phi01_fourier not available':
            pytest.skip("phi01_fourier module not available")
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result['c(-1)']['actual'] == 1

    def test_c_0(self):
        """c(0) = 10 (EZ normalization)."""
        result = bkm.verify_igusa_fourier_coefficients()
        if result.get('status') == 'phi01_fourier not available':
            pytest.skip("phi01_fourier module not available")
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result['c(0)']['actual'] == 10

    def test_c_3(self):
        """c(3) = -64."""
        result = bkm.verify_igusa_fourier_coefficients()
        if result.get('status') == 'phi01_fourier not available':
            pytest.skip("phi01_fourier module not available")
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result['c(3)']['actual'] == -64

    def test_c_4(self):
        """c(4) = 108."""
        result = bkm.verify_igusa_fourier_coefficients()
        if result.get('status') == 'phi01_fourier not available':
            pytest.skip("phi01_fourier module not available")
        # VERIFIED [DC] structural property [CF] cross-family census
        assert result['c(4)']['actual'] == 108


class TestIgusaFromPhi01:
    """Verify the Borcherds lift of phi_{0,1}."""

    def test_lift_weight(self):
        """Borcherds lift of phi_{0,1} has weight 5 = c(0)/2."""
        result = bkm.igusa_chi10_from_phi01()
        if result.get('status') == 'borcherds_lift not available':
            pytest.skip("borcherds_lift module not available")
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['weight'] == 5.0

    def test_lift_is_delta5(self):
        """The lift equals (1/64)*Delta_5."""
        result = bkm.igusa_chi10_from_phi01()
        if result.get('status') == 'borcherds_lift not available':
            pytest.skip("borcherds_lift module not available")
        assert 'Delta_5' in result['form']


# =========================================================================
# 7. ENRIQUES SURFACE BKM
# =========================================================================

class TestEnriques:
    """Verify Enriques surface BKM algebra."""

    def test_lattice_rank(self):
        """Enriques lattice has rank 10."""
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert bkm.ENRIQUES_LATTICE_RANK == 10

    def test_signature(self):
        """Enriques lattice has signature (1, 9)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.ENRIQUES_SIGNATURE == (1, 9)

    def test_e8_theta_constant(self):
        """E_8 theta series: a(0) = 1 (the zero vector)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.E8_THETA_COEFFICIENTS[0] == 1

    def test_e8_theta_240(self):
        """E_8 theta series: a(1) = 240 (240 roots of E_8)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.E8_THETA_COEFFICIENTS[1] == 240

    def test_e8_theta_2160(self):
        """E_8 theta series: a(2) = 2160."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert bkm.E8_THETA_COEFFICIENTS[2] == 2160

    def test_denominator_weight(self):
        """Enriques Borcherds product has weight 4."""
        # VERIFIED [DC] conformal weight [CF] cross-family census
        assert bkm.enriques_denominator_weight() == 4

    def test_shadow_kappa(self):
        """Enriques shadow kappa = 4."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert bkm.enriques_shadow_kappa() == 4

    def test_root_multiplicities_from_e8(self):
        """Root multiplicities come from E_8 theta coefficients."""
        mult = bkm.enriques_root_multiplicities(3)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[0] == 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[1] == 240
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[2] == 2160
        # VERIFIED [DC] structural property [CF] cross-family census
        assert mult[3] == 6720


class TestEnriquesLogDenominator:
    """Verify Enriques log-denominator expansion."""

    def test_log_coeff_1(self):
        """Log coefficient at q^1 = -a(1) = -240."""
        log = bkm.enriques_log_denominator(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log[1] == Fraction(-240)

    def test_log_coeff_2(self):
        """Log coefficient at q^2 = -a(2) - a(1)/2 = -2160 - 120 = -2280."""
        log = bkm.enriques_log_denominator(5)
        expected = Fraction(-2160) + Fraction(-240, 2)
        assert log[2] == expected


# =========================================================================
# 8. MODULARITY OF ROOT MULTIPLICITIES
# =========================================================================

class TestShadowInvariants:
    """Verify shadow invariants S_r from BKM root multiplicities."""

    def test_s1_is_sum_cn(self):
        """S_1 = sum c(n) (the total multiplicity, divided by 1!)."""
        c = {1: 10, 2: 20, 3: 30}
        S = bkm.shadow_invariants_from_multiplicities(c, max_r=3)
        expected = Fraction(10 + 20 + 30)
        assert S[1] == expected

    def test_s2_computation(self):
        """S_2 = (1/2!) * sum n * c(n)."""
        c = {1: 10, 2: 20, 3: 30}
        S = bkm.shadow_invariants_from_multiplicities(c, max_r=3)
        expected = Fraction(1 * 10 + 2 * 20 + 3 * 30, 2)  # = (10+40+90)/2 = 70
        assert S[2] == expected

    def test_monster_s1(self):
        """Monster S_1 = c(1) + c(2) + ... (truncated)."""
        c = {n: bkm.MONSTER_MULTIPLICITIES[n] for n in range(1, 4)}
        S = bkm.shadow_invariants_from_multiplicities(c, max_r=2)
        total = sum(bkm.MONSTER_MULTIPLICITIES[n] for n in range(1, 4))
        # VERIFIED [DC] structural property [CF] cross-family census
        assert S[1] == Fraction(total)


class TestModularityCheck:
    """Verify modularity tests on root multiplicities."""

    def test_monster_growth_consistent(self):
        """Monster multiplicities have consistent exponential growth."""
        c = {n: bkm.MONSTER_MULTIPLICITIES[n] for n in range(1, 6)}
        result = bkm.verify_modularity_of_multiplicities(c, 'Monster')
        assert result['growth_consistent']

    def test_shadow_invariants_assemble(self):
        """Shadow invariants assemble from Monster multiplicities."""
        c = {n: bkm.MONSTER_MULTIPLICITIES[n] for n in range(1, 6)}
        result = bkm.shadow_invariants_assemble_modular(c, max_r=3)
        # All shadow invariants should be positive (Monster has positive c(n))
        for r, val in result['shadow_invariants'].items():
            # VERIFIED [DC] shadow structure [CF] cross-family census
            assert val > 0, f"S_{r} = {val} should be positive for Monster"

    def test_conifold_modularity(self):
        """Conifold BPS invariants: growth check (trivial for alternating +/-1)."""
        # Conifold has |Omega(d)| = 1 for all d, so growth rate is O(1).
        # This is NOT characteristic of a typical modular form, but the
        # DENOMINATOR PRODUCT is modular. The test just verifies the computation runs.
        c = {d: abs((-1) ** (d - 1)) for d in range(1, 6)}  # all 1s for |Omega|
        result = bkm.verify_modularity_of_multiplicities(c, 'Conifold')
        assert 'name' in result


# =========================================================================
# 9. PARTITION FUNCTION p_{24}(n)
# =========================================================================

class TestPartitions24:
    """Verify 24-colored partition function."""

    def test_p24_0(self):
        """p_{24}(0) = 1."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[0] == 1

    def test_p24_1(self):
        """p_{24}(1) = 24."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[1] == 24

    def test_p24_2(self):
        """p_{24}(2) = 324."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[2] == 324

    def test_p24_3(self):
        """p_{24}(3) = 3200."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[3] == 3200

    def test_p24_4(self):
        """p_{24}(4) = 25650."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[4] == 25650

    def test_p24_5(self):
        """p_{24}(5) = 176256."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[5] == 176256

    def test_p24_6(self):
        """p_{24}(6) = 1073720."""
        p = bkm.partitions_24_colors(6)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert p[6] == 1073720

    def test_verify_all_p24_values(self):
        """All p_{24} values match the known table."""
        result = bkm.verify_p24_values()
        for n, v in result.items():
            assert v['match'], f"p_24({n}): expected {v['expected']}, got {v['actual']}"


# =========================================================================
# 10. CROSS-BKM COMPARISON
# =========================================================================

class TestBKMComparison:
    """Verify the cross-BKM comparison table."""

    def test_all_entries_present(self):
        """Table has entries for all 5 BKM algebras."""
        table = bkm.bkm_comparison_table()
        assert 'Monster' in table
        assert 'Fake Monster' in table
        assert 'g_{Delta_5}' in table
        assert 'Conifold' in table
        assert 'Enriques' in table

    def test_monster_kappa_in_table(self):
        """Monster kappa = 1 in the comparison table."""
        table = bkm.bkm_comparison_table()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert table['Monster']['kappa'] == 1

    def test_fake_monster_kappa_in_table(self):
        """Fake Monster kappa = 12 in the table."""
        table = bkm.bkm_comparison_table()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert table['Fake Monster']['kappa'] == 12

    def test_delta5_kappa_in_table(self):
        """g_{Delta_5} kappa = 5 in the table."""
        table = bkm.bkm_comparison_table()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert table['g_{Delta_5}']['kappa'] == 5

    def test_enriques_kappa_in_table(self):
        """Enriques kappa = 4 in the table."""
        table = bkm.bkm_comparison_table()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert table['Enriques']['kappa'] == 4

    def test_all_class_M(self):
        """All BKM algebras have shadow depth = infinity (class M)."""
        table = bkm.bkm_comparison_table()
        for name, data in table.items():
            assert 'infinity' in data['shadow_depth'] or 'M' in data['shadow_depth'], (
                f"{name} should be class M, got {data['shadow_depth']}"
            )


# =========================================================================
# 11. KOSZUL BRIDGE
# =========================================================================

class TestKoszulBridge:
    """Verify the BKM-to-shadow bridge."""

    def test_kappa_from_weight(self):
        """Shadow kappa equals denominator weight."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert bkm.bkm_shadow_kappa_from_weight(5) == 5
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert bkm.bkm_shadow_kappa_from_weight(12) == 12
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert bkm.bkm_shadow_kappa_from_weight(4) == 4

    def test_kappa_weight_correspondence(self):
        """For each BKM, shadow kappa = denominator weight (within BKM conventions)."""
        table = bkm.bkm_comparison_table()
        # g_{Delta_5}: weight 5, kappa 5
        assert table['g_{Delta_5}']['kappa'] == table['g_{Delta_5}']['denominator_weight']
        # Fake Monster: weight 12, kappa 12
        assert table['Fake Monster']['kappa'] == table['Fake Monster']['denominator_weight']
        # Enriques: weight 4, kappa 4
        assert table['Enriques']['kappa'] == table['Enriques']['denominator_weight']
