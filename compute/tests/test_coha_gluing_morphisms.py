r"""Tests for CoHA gluing morphisms: transition maps between chart CoHAs.

THEOREM: The KS wall-crossing automorphisms K_gamma are E_1 algebra
maps that serve as gluing morphisms for the quiver-chart atlas.

Multi-path verification:
    Path 1:  Lattice / charge arithmetic
    Path 2:  Generalized binomial coefficients
    Path 3:  CoHA element algebra (zero, add, scale, product)
    Path 4:  KS automorphism: Euler form pairings
    Path 5:  KS automorphism: action on generators (binomial formula)
    Path 6:  KS automorphism: special cases (m=0, m=1, m=-1)
    Path 7:  Conifold: explicit K_{(1,1)} on generators
    Path 8:  Pentagon identity in Hall algebra form
    Path 9:  Inverse automorphism K^{-1}
    Path 10: K o K^{-1} = id (roundtrip)
    Path 11: E_1 algebra map: K(ab) = K(a)K(b)
    Path 12: Local P^2: cocycle condition
    Path 13: Gauge element as power series
    Path 14: MC gauge transformation
    Path 15: Higher coherences: existence
    Path 16: Multi-wall composition consistency
    Path 17: Independence cross-checks (alternative computation paths)

Manuscript references:
    thm:wc-mc-gauge (physics_wall_crossing_mc.tex)
    thm:mc2-bar-intrinsic (Vol I)
    pentagon identity (Faddeev, Keller arXiv:1102.4148)

Ground truth:
    - Euler form: chi((a,b),(c,d)) = ad - bc
    - K_gamma(e_beta) = sum binom(m+k-1,k) e_{beta+k*gamma}, m = Omega*chi(gamma,beta)
    - Pentagon: K_{10} K_{01} = K_{01} K_{11} K_{10} (EXACT)
    - K o K^{-1} = id (EXACT)
    - K preserves Hall product (E_1 algebra map)
"""

import pytest
from fractions import Fraction

from compute.lib.coha_gluing_morphisms import (
    # Lattice
    euler_form,
    charge_add,
    charge_sub,
    charge_scale,
    charge_height,
    is_positive,
    charge_zero,
    generalized_binomial,
    # CoHA element
    CoHAElement,
    # KS automorphism
    KSWallAutomorphism,
    KSWallAutomorphismInverse,
    ComposedKSAutomorphism,
    # Conifold
    conifold_gluing_map,
    pentagon_hall_algebra,
    conifold_inverse_roundtrip,
    # E_1 verification
    verify_e1_algebra_map,
    # Local P^2
    local_p2_gluing_maps,
    local_p2_cocycle_condition,
    # Gauge / MC
    gauge_element_power_series,
    mc_gauge_transformation,
    # Lie algebra
    LieElement,
    ks_wall_log,
    bch,
    bch_multi,
    exp_ad,
    # Higher coherences
    higher_coherence_existence,
    multi_wall_consistency,
    # Summary
    gluing_data_summary,
)


# =====================================================================
# PATH 1: Charge lattice arithmetic
# =====================================================================

class TestChargeLattice:
    """Verify basic charge lattice operations."""

    def test_charge_add(self):
        assert charge_add((1, 0), (0, 1)) == (1, 1)
        assert charge_add((2, 3), (1, -1)) == (3, 2)

    def test_charge_sub(self):
        assert charge_sub((1, 1), (1, 0)) == (0, 1)
        assert charge_sub((3, 2), (1, 1)) == (2, 1)

    def test_charge_scale(self):
        assert charge_scale(3, (1, 1)) == (3, 3)
        assert charge_scale(0, (1, 2)) == (0, 0)

    def test_charge_height(self):
        assert charge_height((1, 0)) == 1
        assert charge_height((1, 1)) == 2
        assert charge_height((3, 2)) == 5

    def test_is_positive(self):
        assert is_positive((1, 0))
        assert is_positive((0, 1))
        assert is_positive((1, 1))
        assert not is_positive((0, 0))
        assert not is_positive((-1, 1))

    def test_charge_zero(self):
        assert charge_zero(2) == (0, 0)
        assert charge_zero(3) == (0, 0, 0)

    def test_euler_form_antisymmetric(self):
        """Euler form is antisymmetric: chi(g1,g2) = -chi(g2,g1)."""
        for g1 in [(1, 0), (0, 1), (1, 1), (2, 1)]:
            for g2 in [(1, 0), (0, 1), (1, 1), (1, 2)]:
                assert euler_form(g1, g2, 'A1') == -euler_form(g2, g1, 'A1')

    def test_euler_form_conifold_values(self):
        """Known Euler form values for the conifold."""
        assert euler_form((1, 0), (0, 1), 'A1') == 1
        assert euler_form((0, 1), (1, 0), 'A1') == -1
        assert euler_form((1, 0), (1, 0), 'A1') == 0
        assert euler_form((1, 1), (1, 0), 'A1') == -1
        assert euler_form((1, 1), (0, 1), 'A1') == 1

    def test_euler_form_a3_values(self):
        """Euler form for A_3 quiver: chi(e_i, e_j)."""
        e1, e2, e3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
        assert euler_form(e1, e2, 'A3') == 1
        assert euler_form(e2, e3, 'A3') == 1
        assert euler_form(e1, e3, 'A3') == 0  # no arrow 1->3


# =====================================================================
# PATH 2: Generalized binomial coefficients
# =====================================================================

class TestGeneralizedBinomial:
    """Verify generalized binomial coefficient computation."""

    def test_standard_values(self):
        """Standard binomial for non-negative integer n."""
        assert generalized_binomial(Fraction(5), 0) == 1
        assert generalized_binomial(Fraction(5), 1) == 5
        assert generalized_binomial(Fraction(5), 2) == 10
        assert generalized_binomial(Fraction(5), 3) == 10

    def test_negative_integer(self):
        """binom(-m, k) = (-1)^k binom(m+k-1, k)."""
        # binom(-1, 0) = 1
        assert generalized_binomial(Fraction(-1), 0) == 1
        # binom(-1, 1) = -1
        assert generalized_binomial(Fraction(-1), 1) == -1
        # binom(-1, 2) = 1
        assert generalized_binomial(Fraction(-1), 2) == 1
        # binom(-2, 1) = -2
        assert generalized_binomial(Fraction(-2), 1) == -2
        # binom(-2, 2) = 3
        assert generalized_binomial(Fraction(-2), 2) == 3

    def test_negative_binomial_identity(self):
        """binom(-m, k) * (-1)^k = binom(m+k-1, k) for positive m."""
        m = 3
        for k in range(6):
            lhs = generalized_binomial(Fraction(-m), k) * Fraction((-1) ** k)
            rhs = generalized_binomial(Fraction(m + k - 1), k)
            assert lhs == rhs, f"Failed at m={m}, k={k}"

    def test_zero_argument(self):
        assert generalized_binomial(Fraction(0), 0) == 1
        assert generalized_binomial(Fraction(0), 1) == 0
        assert generalized_binomial(Fraction(0), 5) == 0

    def test_fractional(self):
        """binom(1/2, 2) = (1/2)(1/2 - 1)/2! = -1/8."""
        assert generalized_binomial(Fraction(1, 2), 2) == Fraction(-1, 8)


# =====================================================================
# PATH 3: CoHA element algebra
# =====================================================================

class TestCoHAElement:
    """Verify CoHA element arithmetic."""

    def test_zero_element(self):
        z = CoHAElement.zero(10)
        assert z.is_zero()
        assert z.coeffs == {}

    def test_generator(self):
        e = CoHAElement.generator((1, 0), 10)
        assert e.get((1, 0)) == 1
        assert not e.is_zero()

    def test_addition(self):
        e1 = CoHAElement.generator((1, 0), 10)
        e2 = CoHAElement.generator((0, 1), 10)
        s = e1 + e2
        assert s.get((1, 0)) == 1
        assert s.get((0, 1)) == 1

    def test_subtraction_to_zero(self):
        e = CoHAElement.generator((1, 0), 10)
        assert (e - e).is_zero()

    def test_scaling(self):
        e = CoHAElement.generator((1, 0), 10)
        s = e.scale(Fraction(3))
        assert s.get((1, 0)) == 3

    def test_hall_product_generators(self):
        """e_{(1,0)} * e_{(0,1)} = e_{(1,1)} in the classical CoHA."""
        e10 = CoHAElement.generator((1, 0), 10)
        e01 = CoHAElement.generator((0, 1), 10)
        p = e10.hall_product(e01)
        assert p.get((1, 1)) == 1

    def test_hall_product_associativity(self):
        """(a*b)*c = a*(b*c) for the classical Hall product."""
        a = CoHAElement.generator((1, 0), 10)
        b = CoHAElement.generator((0, 1), 10)
        c = CoHAElement.generator((1, 0), 10)
        assert a.hall_product(b).hall_product(c) == a.hall_product(b.hall_product(c))

    def test_hall_product_commutativity(self):
        """Classical Hall product is commutative (q=1)."""
        a = CoHAElement.generator((1, 0), 10)
        b = CoHAElement.generator((0, 1), 10)
        assert a.hall_product(b) == b.hall_product(a)

    def test_truncation(self):
        """Elements beyond max_height are discarded."""
        e = CoHAElement({(100, 100): Fraction(1)}, 10)
        assert e.is_zero()

    def test_identity_product(self):
        """e_0 * e_gamma = e_gamma."""
        identity = CoHAElement.identity(2, 10)
        e10 = CoHAElement.generator((1, 0), 10)
        assert identity.hall_product(e10) == e10


# =====================================================================
# PATH 4: KS automorphism Euler form pairings
# =====================================================================

class TestKSPairings:
    """Verify Euler form pairings used by KS automorphisms."""

    def test_conifold_wall_pairings(self):
        """For the conifold wall gamma = (1,1):
        <(1,1), (1,0)> = -1, <(1,1), (0,1)> = +1, <(1,1),(1,1)> = 0."""
        K = KSWallAutomorphism((1, 1), 1, 12, 'A1')
        assert K.pairing_with((1, 0)) == -1
        assert K.pairing_with((0, 1)) == 1
        assert K.pairing_with((1, 1)) == 0

    def test_simple_root_pairings(self):
        """<(1,0), (0,1)> = 1 (the unique conifold pairing)."""
        K10 = KSWallAutomorphism((1, 0), 1, 12, 'A1')
        assert K10.pairing_with((0, 1)) == 1
        assert K10.pairing_with((1, 0)) == 0

    def test_a3_pairings(self):
        """A_3 quiver pairings: chi(e1,e2)=1, chi(e2,e3)=1, chi(e1,e3)=0."""
        K1 = KSWallAutomorphism((1, 0, 0), 1, 12, 'A3')
        K2 = KSWallAutomorphism((0, 1, 0), 1, 12, 'A3')
        assert K1.pairing_with((0, 1, 0)) == 1
        assert K2.pairing_with((0, 0, 1)) == 1
        assert K1.pairing_with((0, 0, 1)) == 0


# =====================================================================
# PATH 5: KS automorphism action on generators
# =====================================================================

class TestKSAction:
    """Verify KS automorphism action on CoHA generators."""

    def test_trivial_pairing_leaves_generator_fixed(self):
        """If <gamma, beta> = 0, then K_gamma(e_beta) = e_beta."""
        K = KSWallAutomorphism((1, 1), 1, 12, 'A1')
        # <(1,1),(1,1)> = 0
        result = K.act_on_generator((1, 1))
        expected = CoHAElement.generator((1, 1), 12, quiver='A1')
        assert result == expected

    def test_positive_pairing_adds_terms(self):
        """If <gamma, beta> > 0, K_gamma adds e_{beta+k*gamma} terms."""
        K = KSWallAutomorphism((1, 1), 1, 12, 'A1')
        # <(1,1),(0,1)> = 1, m = 1
        result = K.act_on_generator((0, 1))
        # binom(k, k) = 1 for all k, so result = sum e_{(0,1)+k(1,1)}
        assert result.get((0, 1)) == 1
        assert result.get((1, 2)) == 1
        assert result.get((2, 3)) == 1

    def test_negative_pairing_alternates(self):
        """If <gamma, beta> < 0, K_gamma has alternating coefficients."""
        K = KSWallAutomorphism((1, 1), 1, 12, 'A1')
        # <(1,1),(1,0)> = -1, m = -1
        result = K.act_on_generator((1, 0))
        # binom(-2, 0) = 1, binom(-2, 1) = -2... wait
        # m = -1, binom(m+k-1, k) = binom(-2+k, k) = binom(k-2, k)
        # k=0: binom(-2, 0) = 1
        # k=1: binom(-1, 1) = -1
        # k=2: binom(0, 2) = 0  -> series terminates
        assert result.get((1, 0)) == 1
        assert result.get((2, 1)) == -1
        # No higher terms (binom(0,2)=0, binom(1,3)=0, etc.)
        assert result.get((3, 2)) == 0

    def test_k10_on_01(self):
        """K_{(1,0)}(e_{(0,1)}): <(1,0),(0,1)> = 1, m = 1."""
        K = KSWallAutomorphism((1, 0), 1, 8, 'A1')
        result = K.act_on_generator((0, 1))
        # m = 1, binom(k, k) = 1, so e_{(0,1)} + e_{(1,1)} + e_{(2,1)} + ...
        assert result.get((0, 1)) == 1
        assert result.get((1, 1)) == 1
        assert result.get((2, 1)) == 1

    def test_k01_on_10(self):
        """K_{(0,1)}(e_{(1,0)}): <(0,1),(1,0)> = -1, m = -1."""
        K = KSWallAutomorphism((0, 1), 1, 8, 'A1')
        result = K.act_on_generator((1, 0))
        # m = -1: binom(-2, 0)=1, binom(-1, 1)=-1, binom(0, 2)=0
        assert result.get((1, 0)) == 1
        assert result.get((1, 1)) == -1
        assert result.get((1, 2)) == 0

    def test_pairing_m2(self):
        """For m = 2: binom(k+1, k) = k+1."""
        # Need <gamma, beta> = 2.  Use gamma=(1,0), beta=(-2,... )
        # Actually, for positive beta with <(1,0), beta> = 2:
        # beta = (a,b), <(1,0),(a,b)> = b.  So b = 2 -> beta = (0,2).
        K = KSWallAutomorphism((1, 0), 1, 12, 'A1')
        result = K.act_on_generator((0, 2))
        # m = 2: binom(k+1, k) = k+1
        assert result.get((0, 2)) == 1   # k=0: binom(1,0) = 1
        assert result.get((1, 2)) == 2   # k=1: binom(2,1) = 2
        assert result.get((2, 2)) == 3   # k=2: binom(3,2) = 3
        assert result.get((3, 2)) == 4   # k=3: binom(4,3) = 4


# =====================================================================
# PATH 6: KS special cases
# =====================================================================

class TestKSSpecialCases:
    """Verify KS automorphism in special cases."""

    def test_m_zero_is_identity(self):
        """m = 0 => K_gamma(e_beta) = e_beta."""
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        # <(1,1), (1,1)> = 0
        result = K.act_on_generator((1, 1))
        assert result == CoHAElement.generator((1, 1), 10, quiver='A1')

    def test_m_one_geometric_series(self):
        """m = 1 => K_gamma(e_beta) = e_beta/(1 - e_gamma) = sum e_{beta+k*gamma}."""
        K = KSWallAutomorphism((1, 0), 1, 6, 'A1')
        result = K.act_on_generator((0, 1))  # m = 1
        # All coefficients should be 1
        for k in range(4):
            assert result.get(charge_add((0, 1), charge_scale(k, (1, 0)))) == 1

    def test_m_minus_one_finite(self):
        """m = -1 => K_gamma(e_beta) = (1 - e_gamma) * e_beta = e_beta - e_{beta+gamma}."""
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        result = K.act_on_generator((1, 0))  # m = -1
        assert result.get((1, 0)) == 1
        assert result.get((2, 1)) == -1
        # Verify no further terms
        for k in range(2, 6):
            target = charge_add((1, 0), charge_scale(k, (1, 1)))
            if charge_height(target) <= 10:
                assert result.get(target) == 0

    def test_omega_zero_is_identity(self):
        """Omega = 0 => K_gamma = id (no wall-crossing)."""
        K = KSWallAutomorphism((1, 1), 0, 10, 'A1')
        result = K.act_on_generator((1, 0))
        assert result == CoHAElement.generator((1, 0), 10, quiver='A1')


# =====================================================================
# PATH 7: Conifold explicit K_{(1,1)}
# =====================================================================

class TestConifoldGluing:
    """Verify explicit conifold gluing morphism."""

    def test_conifold_gluing_map(self):
        data = conifold_gluing_map(12)
        assert data['pairing_11_10'] == -1
        assert data['pairing_11_01'] == 1
        assert data['pairing_11_11'] == 0

    def test_action_on_10_leading(self):
        """K_{(1,1)}(e_{(1,0)}) = e_{(1,0)} - e_{(2,1)}."""
        data = conifold_gluing_map(12)
        action = data['action_on_10']
        assert action.get((1, 0)) == 1
        assert action.get((2, 1)) == -1

    def test_action_on_01_leading(self):
        """K_{(1,1)}(e_{(0,1)}) = e_{(0,1)} + e_{(1,2)} + e_{(2,3)} + ..."""
        data = conifold_gluing_map(12)
        action = data['action_on_01']
        assert action.get((0, 1)) == 1
        assert action.get((1, 2)) == 1
        assert action.get((2, 3)) == 1

    def test_action_on_11_fixed(self):
        """K_{(1,1)}(e_{(1,1)}) = e_{(1,1)} (since <(1,1),(1,1)>=0)."""
        data = conifold_gluing_map(12)
        action = data['action_on_11']
        assert action == CoHAElement.generator((1, 1), 12, quiver='A1')

    def test_inverse_action_on_10(self):
        """K^{-1}_{(1,1)}(e_{(1,0)}) = e_{(1,0)} + e_{(2,1)}."""
        data = conifold_gluing_map(12)
        inv_action = data['inverse_action_on_10']
        # m = -1, but with -Omega: m = 1, so geometric series
        assert inv_action.get((1, 0)) == 1
        assert inv_action.get((2, 1)) == 1

    def test_inverse_action_on_01(self):
        """K^{-1}_{(1,1)}(e_{(0,1)}) = e_{(0,1)} - e_{(1,2)}."""
        data = conifold_gluing_map(12)
        inv_action = data['inverse_action_on_01']
        # m = 1 with -Omega: m = -1, so finite: e_{01} - e_{12}
        assert inv_action.get((0, 1)) == 1
        assert inv_action.get((1, 2)) == -1


# =====================================================================
# PATH 8: Pentagon identity
# =====================================================================

class TestPentagon:
    """Verify the pentagon identity as BCH in the pro-nilpotent Lie algebra.

    Pentagon: BCH(L_{10}, L_{01}) = BCH(L_{01}, L_{11}, L_{10})

    This is the correct form: an identity about ordered products,
    NOT about composition of automorphisms on generators (AP42).

    CAUTION: The BCH is computed to finite depth. Heights 1-2 match
    exactly with depth-4 BCH. Higher heights require higher BCH depth
    (or are verified independently by the MC equation).
    """

    def test_pentagon_low_heights_4(self):
        """Pentagon holds at heights 1-2 with max_height=4."""
        result = pentagon_hall_algebra(4)
        assert result['pentagon_holds_low_heights']

    def test_pentagon_low_heights_6(self):
        """Pentagon holds at heights 1-2 with max_height=6."""
        result = pentagon_hall_algebra(6)
        assert result['pentagon_holds_low_heights']

    def test_pentagon_low_heights_8(self):
        """Pentagon holds at heights 1-2 with max_height=8."""
        result = pentagon_hall_algebra(8)
        assert result['pentagon_holds_low_heights']

    def test_pentagon_no_low_height_mismatches(self):
        result = pentagon_hall_algebra(6)
        assert len(result['low_height_mismatches']) == 0

    def test_pentagon_verifies_multiple_heights(self):
        result = pentagon_hall_algebra(6)
        assert result['num_heights_verified'] >= 3

    def test_pentagon_height_1_exact(self):
        """Height 1 terms: just the wall logs themselves. Must match."""
        result = pentagon_hall_algebra(8)
        assert result['height_data'][1]['match']

    def test_pentagon_height_2_exact(self):
        """Height 2 terms: first BCH correction. Must match."""
        result = pentagon_hall_algebra(8)
        assert result['height_data'][2]['match']


# =====================================================================
# PATH 9: Inverse automorphism
# =====================================================================

class TestInverse:
    """Verify inverse KS automorphism."""

    def test_inverse_has_negated_omega(self):
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        K_inv = K.inverse()
        assert K_inv.omega == -1
        assert K_inv.gamma == (1, 1)

    def test_explicit_inverse_on_10(self):
        """K^{-1}_{(1,1)}(e_{(1,0)}) uses -Omega."""
        K_inv = KSWallAutomorphismInverse((1, 1), 1, 10, 'A1')
        result = K_inv.act_on_generator((1, 0))
        # m = Omega * <(1,1),(1,0)> = 1 * (-1) = -1
        # K^{-1}: (1-e_gamma)^m = (1-e_{11})^{-1} = 1 + e_{11} + e_{22} + ...
        # binom(-1, k)*(-1)^k = binom(k, k) = 1 for all k
        assert result.get((1, 0)) == 1
        assert result.get((2, 1)) == 1  # e_{(1,0)+(1,1)}

    def test_explicit_inverse_on_01(self):
        """K^{-1}_{(1,1)}(e_{(0,1)}) uses (1-e_{11})^1."""
        K_inv = KSWallAutomorphismInverse((1, 1), 1, 10, 'A1')
        result = K_inv.act_on_generator((0, 1))
        # m = 1*1 = 1
        # (1-e_{11})^1 * e_{01} = e_{01} - e_{12}
        assert result.get((0, 1)) == 1
        assert result.get((1, 2)) == -1
        # No higher terms (binom(1, k)*(-1)^k = 0 for k >= 2)
        assert result.get((2, 3)) == 0

    def test_inverse_via_negated_omega_matches_explicit(self):
        """K.inverse() should agree with KSWallAutomorphismInverse."""
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        K_inv_auto = K.inverse()
        K_inv_explicit = KSWallAutomorphismInverse((1, 1), 1, 10, 'A1')

        for beta in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]:
            auto_result = K_inv_auto.act_on_generator(beta)
            explicit_result = K_inv_explicit.act_on_generator(beta)
            assert auto_result == explicit_result, f"Mismatch at beta={beta}"


# =====================================================================
# PATH 10: K o K^{-1} = id (roundtrip)
# =====================================================================

class TestRoundtrip:
    """Verify K o K^{-1} = id."""

    def test_roundtrip_conifold(self):
        result = conifold_inverse_roundtrip(8)
        assert result['is_identity']

    def test_roundtrip_individual_generators(self):
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K, K_inv])

        for beta in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (3, 0)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 10, quiver='A1')
            assert result == expected, f"Roundtrip failed at beta={beta}"

    def test_inverse_roundtrip_other_direction(self):
        """K^{-1} o K = id as well."""
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K_inv, K])

        for beta in [(1, 0), (0, 1), (1, 1), (2, 1)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 10, quiver='A1')
            assert result == expected, f"K^-1 o K failed at beta={beta}"

    def test_roundtrip_simple_root_walls(self):
        """K_{(1,0)} o K_{(1,0)}^{-1} = id."""
        K = KSWallAutomorphism((1, 0), 1, 8, 'A1')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K, K_inv])

        for beta in [(0, 1), (0, 2), (1, 1)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 8, quiver='A1')
            assert result == expected

    def test_roundtrip_a3_quiver(self):
        """Roundtrip for A_3 quiver automorphisms."""
        K = KSWallAutomorphism((1, 1, 0), 1, 6, 'A3')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K, K_inv])

        for beta in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 6, quiver='A3')
            assert result == expected, f"A3 roundtrip failed at {beta}"


# =====================================================================
# PATH 11: E_1 algebra map
# =====================================================================

class TestE1AlgebraMap:
    """Verify K_gamma preserves the Hall product."""

    def test_conifold_wall_is_e1(self):
        result = verify_e1_algebra_map((1, 1), 1, 5, 'A1')
        assert result['is_e1_map']

    def test_simple_root_10_is_e1(self):
        result = verify_e1_algebra_map((1, 0), 1, 5, 'A1')
        assert result['is_e1_map']

    def test_simple_root_01_is_e1(self):
        result = verify_e1_algebra_map((0, 1), 1, 5, 'A1')
        assert result['is_e1_map']

    def test_a3_root_is_e1(self):
        result = verify_e1_algebra_map((1, 1, 0), 1, 4, 'A3')
        assert result['is_e1_map']

    def test_e1_tests_many_pairs(self):
        result = verify_e1_algebra_map((1, 1), 1, 4, 'A1')
        assert result['num_pairs_tested'] >= 5

    def test_e1_explicit_pair(self):
        """K_{(1,1)}(e_{(1,0)} * e_{(0,1)}) = K_{(1,1)}(e_{(1,0)}) * K_{(1,1)}(e_{(0,1)})."""
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')

        # LHS: K(e_{(1,0)} * e_{(0,1)}) = K(e_{(1,1)})
        e10 = CoHAElement.generator((1, 0), 10, quiver='A1')
        e01 = CoHAElement.generator((0, 1), 10, quiver='A1')
        product = e10.hall_product(e01)  # = e_{(1,1)}
        lhs = K.act_on_element(product)

        # RHS: K(e_{(1,0)}) * K(e_{(0,1)})
        Ke10 = K.act_on_generator((1, 0))
        Ke01 = K.act_on_generator((0, 1))
        rhs = Ke10.hall_product(Ke01)

        assert lhs == rhs


# =====================================================================
# PATH 12: Local P^2 cocycle condition
# =====================================================================

class TestLocalP2:
    """Verify local P^2 gluing maps: individual automorphisms and their properties.

    The hexagon/cocycle identity for A_3 holds in the pro-nilpotent completion
    but requires all-orders BCH; finite-depth BCH is insufficient.
    We verify the computable properties: individual KS actions, E_1 map,
    inverse roundtrip, and Euler form structure.
    """

    def test_local_p2_six_roots(self):
        result = local_p2_gluing_maps(6)
        assert result['num_positive_roots'] == 6

    def test_local_p2_euler_pairings(self):
        """Check A_3 Euler form structure."""
        result = local_p2_gluing_maps(6)
        p = result['pairings']
        assert p['(1, 0, 0),(0, 1, 0)'] == 1
        assert p['(0, 1, 0),(0, 0, 1)'] == 1
        assert p['(1, 0, 0),(0, 0, 1)'] == 0  # no direct arrow

    def test_local_p2_euler_antisymmetric(self):
        """Euler form on A_3 is antisymmetric."""
        roots = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)]
        for g1 in roots:
            for g2 in roots:
                assert euler_form(g1, g2, 'A3') == -euler_form(g2, g1, 'A3')

    def test_local_p2_e12_is_e1_map(self):
        """K_{e_{12}} is an E_1 algebra map."""
        result = verify_e1_algebra_map((1, 1, 0), 1, 4, 'A3')
        assert result['is_e1_map']

    def test_local_p2_e23_is_e1_map(self):
        """K_{e_{23}} is an E_1 algebra map."""
        result = verify_e1_algebra_map((0, 1, 1), 1, 4, 'A3')
        assert result['is_e1_map']

    def test_local_p2_e123_is_e1_map(self):
        """K_{e_{123}} is an E_1 algebra map."""
        result = verify_e1_algebra_map((1, 1, 1), 1, 4, 'A3')
        assert result['is_e1_map']

    def test_local_p2_roundtrip_e12(self):
        """K_{e12} o K_{e12}^{-1} = id."""
        K = KSWallAutomorphism((1, 1, 0), 1, 6, 'A3')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K, K_inv])
        for beta in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 6, quiver='A3')
            assert result == expected

    def test_local_p2_roundtrip_e123(self):
        """K_{e123} o K_{e123}^{-1} = id."""
        K = KSWallAutomorphism((1, 1, 1), 1, 6, 'A3')
        K_inv = K.inverse()
        comp = ComposedKSAutomorphism([K, K_inv])
        for beta in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            result = comp.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 6, quiver='A3')
            assert result == expected

    def test_local_p2_ks_action_e12_on_e1(self):
        """K_{e12}(e_1): <(1,1,0),(1,0,0)> = 0*0-1*1+1*0-0*0 = -1."""
        K = KSWallAutomorphism((1, 1, 0), 1, 8, 'A3')
        # <(1,1,0),(1,0,0)> = 1*0-1*1 + 1*0-0*0 = -1
        assert K.pairing_with((1, 0, 0)) == -1
        result = K.act_on_generator((1, 0, 0))
        # m = -1: e_1 - e_{e1+e12} = e_1 - e_{(2,1,0)}
        assert result.get((1, 0, 0)) == 1
        assert result.get((2, 1, 0)) == -1

    def test_local_p2_ks_action_e12_on_e3(self):
        """K_{e12}(e_3): <(1,1,0),(0,0,1)> = 1*0-0*0 + 1*1-0*0 = 1."""
        K = KSWallAutomorphism((1, 1, 0), 1, 8, 'A3')
        assert K.pairing_with((0, 0, 1)) == 1
        result = K.act_on_generator((0, 0, 1))
        # m = 1: geometric series
        assert result.get((0, 0, 1)) == 1
        assert result.get((1, 1, 1)) == 1  # e_3 + e_{12} = e_{123}


# =====================================================================
# PATH 13: Gauge element
# =====================================================================

class TestGaugeElement:
    """Verify gauge element as power series in the Lie algebra."""

    def test_wall_log_leading_term(self):
        """L_{(1,1)} starts with e_{(1,1)}."""
        L = ks_wall_log((1, 1), 1, 10, 'A1')
        assert L.get((1, 1)) == 1
        assert L.get((2, 2)) == Fraction(1, 2)
        assert L.get((3, 3)) == Fraction(1, 3)

    def test_wall_log_scaling(self):
        """L_gamma with Omega = 2 is 2 * L_gamma with Omega = 1."""
        L1 = ks_wall_log((1, 1), 1, 10, 'A1')
        L2 = ks_wall_log((1, 1), 2, 10, 'A1')
        for gamma in L1.charges():
            assert L2.get(gamma) == 2 * L1.get(gamma)

    def test_gauge_element_series(self):
        data = gauge_element_power_series(10)
        assert data['theta_I_charges'] > 0
        assert data['theta_II_charges'] > data['theta_I_charges']

    def test_bracket_nonzero(self):
        """[L_{(1,1)}, L_{(1,0)} + L_{(0,1)}] should be nonzero."""
        L_11 = ks_wall_log((1, 1), 1, 10, 'A1')
        L_10 = ks_wall_log((1, 0), 1, 10, 'A1')
        L_01 = ks_wall_log((0, 1), 1, 10, 'A1')
        theta = L_10 + L_01
        bracket = L_11.bracket(theta)
        assert not bracket.is_zero()


# =====================================================================
# PATH 14: MC gauge transformation
# =====================================================================

class TestMCGauge:
    """Verify MC gauge transformation."""

    def test_pentagon_bch_low_heights(self):
        """Pentagon via BCH at heights 1-2 (exact at finite BCH depth)."""
        result = mc_gauge_transformation(8)
        # Check low-height match directly
        L10 = ks_wall_log((1, 0), 1, 8, 'A1')
        L01 = ks_wall_log((0, 1), 1, 8, 'A1')
        L11 = ks_wall_log((1, 1), 1, 8, 'A1')
        S_I = bch(L10, L01)
        S_II = bch_multi([L01, L11, L10])
        diff = S_I - S_II
        for gamma, coeff in diff.coeffs.items():
            if charge_height(gamma) <= 2:
                assert coeff == 0, f"Pentagon fails at {gamma}"

    def test_mc_equations(self):
        result = mc_gauge_transformation(8)
        assert result['mc_I_zero']
        assert result['mc_II_zero']

    def test_bch_pentagon_height_2_exact(self):
        """Pentagon at height 2 is exact regardless of truncation."""
        for max_h in [6, 8, 10]:
            L10 = ks_wall_log((1, 0), 1, max_h, 'A1')
            L01 = ks_wall_log((0, 1), 1, max_h, 'A1')
            L11 = ks_wall_log((1, 1), 1, max_h, 'A1')
            S_I = bch(L10, L01)
            S_II = bch_multi([L01, L11, L10])
            diff = S_I - S_II
            for gamma, coeff in diff.coeffs.items():
                if charge_height(gamma) <= 2:
                    assert coeff == 0, f"Height-2 pentagon fails at {gamma}, max_h={max_h}"


# =====================================================================
# PATH 15: Higher coherences
# =====================================================================

class TestHigherCoherences:
    """Verify higher coherences at triple overlaps."""

    def test_coherence_existence(self):
        result = higher_coherence_existence(6)
        assert result['coherence_exists']

    def test_sequences_agree_low_heights(self):
        """Different maximal green sequences agree at heights 1-2."""
        result = higher_coherence_existence(6)
        assert result['sequences_agree_low_heights']

    def test_contractibility_argument(self):
        """The proof of existence is by contractibility of E_1 equivalences."""
        result = higher_coherence_existence(6)
        assert 'contractible' in result['proof_summary']

    def test_pairing_e2_e123(self):
        """Euler pairing <e2, e123>."""
        result = higher_coherence_existence(6)
        # For A_3: <(0,1,0),(1,1,1)> = 0*1-1*1 + 1*1-0*1 = -1+1 = 0
        assert result['pairing_e2_e123'] == 0


# =====================================================================
# PATH 16: Multi-wall composition
# =====================================================================

class TestMultiWallComposition:
    """Verify composition of multiple gluing maps."""

    def test_conifold_associative(self):
        result = multi_wall_consistency(6)
        assert result['conifold_associative']

    def test_a3_associative(self):
        result = multi_wall_consistency(6)
        assert result['a3_associative']

    def test_strict_associativity(self):
        result = multi_wall_consistency(6)
        assert result['strict_associativity']


# =====================================================================
# PATH 17: Cross-check independence
# =====================================================================

class TestCrossChecks:
    """Independent cross-checks between different computation paths."""

    def test_hall_action_vs_lie_adjoint_conifold(self):
        """The Hall algebra K_{(1,1)} action on e_{(1,0)} should be
        consistent with the Lie algebra exp(ad_{L_{(1,1)}})(e_{(1,0)}).

        In the Lie algebra:
            exp(ad_L)(e_{10}) = e_{10} + [L_{11}, e_{10}] + ...

        The leading bracket [e_{(1,1)}, e_{(1,0)}]:
            <(1,1), (1,0)> = -1, so [e_{11}, e_{10}] = -1 * e_{21} = -e_{(2,1)}.

        So exp(ad_L)(e_{10}) = e_{10} - e_{(2,1)} + ... (higher order).

        The Hall algebra action:
            K_{(1,1)}(e_{10}) = e_{10} - e_{(2,1)} (exactly, since m=-1).

        The leading terms MUST agree.
        """
        # Lie algebra computation
        L_11 = ks_wall_log((1, 1), 1, 10, 'A1')
        e_10 = LieElement.generator((1, 0), 10, quiver='A1')
        lie_result = exp_ad(L_11, e_10)

        # Hall algebra computation
        K = KSWallAutomorphism((1, 1), 1, 10, 'A1')
        hall_result = K.act_on_generator((1, 0))

        # Leading terms agree
        assert lie_result.get((1, 0)) == hall_result.get((1, 0))
        assert lie_result.get((2, 1)) == hall_result.get((2, 1))

    def test_hall_action_vs_lie_adjoint_01(self):
        """Same check for e_{(0,1)}."""
        L_11 = ks_wall_log((1, 1), 1, 8, 'A1')
        e_01 = LieElement.generator((0, 1), 8, quiver='A1')
        lie_result = exp_ad(L_11, e_01)

        K = KSWallAutomorphism((1, 1), 1, 8, 'A1')
        hall_result = K.act_on_generator((0, 1))

        # Both should have e_{(0,1)} with coeff 1
        assert lie_result.get((0, 1)) == 1
        assert hall_result.get((0, 1)) == 1
        # Both should have e_{(1,2)} with coeff 1
        assert lie_result.get((1, 2)) == hall_result.get((1, 2))

    def test_pentagon_bch_low_heights_at_two_truncations(self):
        """Pentagon at heights 1-2 must hold at BOTH truncation 5 and 8."""
        result5 = pentagon_hall_algebra(5)
        result8 = pentagon_hall_algebra(8)
        assert result5['pentagon_holds_low_heights']
        assert result8['pentagon_holds_low_heights']

    def test_pentagon_bch_direct_low_heights(self):
        """Pentagon via direct BCH: verified at heights 1-2."""
        L10 = ks_wall_log((1, 0), 1, 8, 'A1')
        L01 = ks_wall_log((0, 1), 1, 8, 'A1')
        L11 = ks_wall_log((1, 1), 1, 8, 'A1')
        S_I = bch(L10, L01)
        S_II = bch_multi([L01, L11, L10])
        diff = S_I - S_II
        # Heights 1-2 must match exactly
        for gamma, coeff in diff.coeffs.items():
            if charge_height(gamma) <= 2:
                assert coeff == 0, f"Pentagon fails at {gamma}"

    def test_roundtrip_via_explicit_inverse_class(self):
        """K * K^{-1}(explicit) = id on generators, using both inverse implementations."""
        K = KSWallAutomorphism((1, 1), 1, 8, 'A1')
        K_inv_negated = K.inverse()
        K_inv_explicit = KSWallAutomorphismInverse((1, 1), 1, 8, 'A1')

        for beta in [(1, 0), (0, 1), (2, 0)]:
            # Method 1: K o K_inv_negated
            step1a = K_inv_negated.act_on_generator(beta)
            result_a = K.act_on_element(step1a)
            # Method 2: K o K_inv_explicit
            step1b = K_inv_explicit.act_on_generator(beta)
            result_b = K.act_on_element(step1b)
            expected = CoHAElement.generator(beta, 8, quiver='A1')
            assert result_a == expected, f"Method 1 failed at {beta}"
            assert result_b == expected, f"Method 2 failed at {beta}"

    def test_e1_map_direct_computation(self):
        """Direct computation: K_{(1,0)}(e_{10}*e_{01}) vs K(e_{10})*K(e_{01})."""
        K = KSWallAutomorphism((1, 0), 1, 8, 'A1')
        # Product e_{10}*e_{01} = e_{11}
        lhs = K.act_on_generator((1, 1))  # K(e_{11})
        # K(e_{10}) * K(e_{01})
        Ke10 = K.act_on_generator((1, 0))
        Ke01 = K.act_on_generator((0, 1))
        rhs = Ke10.hall_product(Ke01)
        assert lhs == rhs

    def test_conifold_summary(self):
        """Full summary computation runs without error."""
        result = gluing_data_summary(6)
        assert result['conifold']['pentagon']
        assert result['conifold']['inverse_roundtrip']
        assert result['conifold']['e1_algebra_map']

    def test_wall_log_antisymmetry(self):
        """Wall logs of opposite charges: L_gamma and L_{-gamma} should
        not both be in the positive cone (one is zero)."""
        L_pos = ks_wall_log((1, 1), 1, 10, 'A1')
        assert not L_pos.is_zero()
        # Negative charge: not in positive cone
        L_neg = ks_wall_log((-1, -1), 1, 10, 'A1')
        assert L_neg.is_zero()

    def test_composition_of_three_walls(self):
        """ComposedKSAutomorphism([K1, K2, K3]) applies K1 first, then K2, then K3."""
        K1 = KSWallAutomorphism((1, 0), 1, 6, 'A1')
        K2 = KSWallAutomorphism((1, 1), 1, 6, 'A1')
        K3 = KSWallAutomorphism((0, 1), 1, 6, 'A1')

        comp = ComposedKSAutomorphism([K1, K2, K3])

        # Step by step in same order: K1 first, then K2, then K3
        beta = (1, 0)
        step1 = K1.act_on_element(CoHAElement.generator(beta, 6, quiver='A1'))
        step2 = K2.act_on_element(step1)
        step3 = K3.act_on_element(step2)

        composed = comp.act_on_generator(beta)
        assert composed == step3

    def test_binomial_generating_function(self):
        """Verify: sum_{k>=0} binom(m+k-1, k) x^k = (1-x)^{-m} for small m."""
        # For m = 1: (1-x)^{-1} = 1 + x + x^2 + ...
        # binom(k, k) = 1 for all k
        for k in range(6):
            assert generalized_binomial(Fraction(k), k) == 1

        # For m = 2: (1-x)^{-2} = 1 + 2x + 3x^2 + 4x^3 + ...
        # binom(k+1, k) = k+1
        for k in range(6):
            assert generalized_binomial(Fraction(k + 1), k) == k + 1

        # For m = 3: (1-x)^{-3} = 1 + 3x + 6x^2 + 10x^3 + ...
        # binom(k+2, k) = (k+1)(k+2)/2
        for k in range(6):
            expected = Fraction((k + 1) * (k + 2), 2)
            assert generalized_binomial(Fraction(k + 2), k) == expected

    def test_a3_six_roots_complete(self):
        """For A_3 quiver, exactly 6 positive roots with all pairings consistent."""
        e1 = (1, 0, 0)
        e2 = (0, 1, 0)
        e3 = (0, 0, 1)
        e12 = (1, 1, 0)
        e23 = (0, 1, 1)
        e123 = (1, 1, 1)

        roots = [e1, e2, e3, e12, e23, e123]
        assert len(roots) == 6  # n(n+1)/2 = 3*4/2 = 6

        # Verify: e12 = e1 + e2, e23 = e2 + e3, e123 = e1 + e2 + e3
        assert charge_add(e1, e2) == e12
        assert charge_add(e2, e3) == e23
        assert charge_add(e1, charge_add(e2, e3)) == e123

        # Euler form between composite roots
        # <(1,1,0),(0,1,1)> = 1*1-1*0 + 1*1-0*1 = 2
        assert euler_form(e12, e23, 'A3') == 2
        # <(1,1,0),(0,0,1)> = 1*0-0*0 + 1*1-0*0 = 1
        assert euler_form(e12, e3, 'A3') == 1
        # <(1,0,0),(0,1,1)> = 1*1-0*0 + 0*1-0*1 = 1
        assert euler_form(e1, e23, 'A3') == 1

    def test_composed_inverse(self):
        """Inverse of composition = composition of inverses in reverse."""
        K1 = KSWallAutomorphism((1, 0), 1, 6, 'A1')
        K2 = KSWallAutomorphism((0, 1), 1, 6, 'A1')

        comp = ComposedKSAutomorphism([K2, K1])
        comp_inv = comp.inverse()

        # K2 K1 K1^{-1} K2^{-1} = id
        full = ComposedKSAutomorphism(comp.factors + comp_inv.factors)
        for beta in [(1, 0), (0, 1), (1, 1)]:
            result = full.act_on_generator(beta)
            expected = CoHAElement.generator(beta, 6, quiver='A1')
            assert result == expected, f"Composed inverse failed at {beta}"


# =====================================================================
# Additional structural tests
# =====================================================================

class TestStructural:
    """Structural properties of the gluing morphisms."""

    def test_lie_bracket_antisymmetric(self):
        """[f, g] = -[g, f] in the Lie algebra."""
        f = LieElement.generator((1, 0), 10, quiver='A1')
        g = LieElement.generator((0, 1), 10, quiver='A1')
        fg = f.bracket(g)
        gf = g.bracket(f)
        assert fg == -gf

    def test_lie_bracket_jacobi(self):
        """[[f,g],h] + [[g,h],f] + [[h,f],g] = 0."""
        f = LieElement.generator((1, 0), 10, quiver='A1')
        g = LieElement.generator((0, 1), 10, quiver='A1')
        h = LieElement.generator((1, 1), 10, quiver='A1')

        fg = f.bracket(g)
        gh = g.bracket(h)
        hf = h.bracket(f)

        term1 = fg.bracket(h)
        term2 = gh.bracket(f)
        term3 = hf.bracket(g)

        jacobi = term1 + term2 + term3
        assert jacobi.is_zero()

    def test_bch_leading_term(self):
        """BCH(f, g) = f + g + [f,g]/2 + ... at leading order."""
        f = LieElement.generator((1, 0), 10, quiver='A1')
        g = LieElement.generator((0, 1), 10, quiver='A1')
        result = bch(f, g)

        # f + g terms
        assert result.get((1, 0)) == 1
        assert result.get((0, 1)) == 1
        # [f, g]/2 = chi((1,0),(0,1))/2 * e_{(1,1)} = 1/2 * e_{(1,1)}
        assert result.get((1, 1)) == Fraction(1, 2)

    def test_exp_ad_first_order(self):
        """exp(ad_alpha)(target) = target + [alpha, target] + ... at first order."""
        alpha = LieElement.generator((1, 1), 10, Fraction(1), 'A1')
        target = LieElement.generator((1, 0), 10, quiver='A1')
        result = exp_ad(alpha, target, max_order=1)

        # target + [alpha, target]
        # [(1,1), (1,0)] = chi((1,1),(1,0)) = -1, so [alpha, target] = -e_{(2,1)}
        assert result.get((1, 0)) == 1
        assert result.get((2, 1)) == -1

    def test_coha_element_equality(self):
        """CoHA element equality is based on coefficients."""
        e1 = CoHAElement({(1, 0): Fraction(1)}, 10, 'A1')
        e2 = CoHAElement({(1, 0): Fraction(1)}, 10, 'A1')
        assert e1 == e2

    def test_coha_zero_product(self):
        """Product with zero element."""
        z = CoHAElement.zero(10)
        e = CoHAElement.generator((1, 0), 10)
        assert z.hall_product(e).is_zero()

    def test_multiple_omega_values(self):
        """KS automorphism with Omega = 2 doubles the effective pairing."""
        K1 = KSWallAutomorphism((1, 1), 1, 8, 'A1')
        K2 = KSWallAutomorphism((1, 1), 2, 8, 'A1')

        # For Omega=1, m=-1: K(e10) = e10 - e21
        r1 = K1.act_on_generator((1, 0))
        # For Omega=2, m=-2: K(e10) = e10 + binom(-3,1)*e21 + binom(-1,2)*e32 + ...
        # binom(-3, 0)=1, binom(-3,1)=-3, binom(-3,2)=6...
        # Wait: m = 2*(-1) = -2
        # binom(m+k-1, k) = binom(-3+k, k) = binom(k-3, k)
        # k=0: binom(-3,0) = 1
        # k=1: binom(-2,1) = -2
        # k=2: binom(-1,2) = 1
        # k=3: binom(0,3) = 0
        r2 = K2.act_on_generator((1, 0))
        assert r2.get((1, 0)) == 1
        assert r2.get((2, 1)) == -2
        assert r2.get((3, 2)) == 1

    def test_wall_log_height_truncation(self):
        """Wall log respects max_height truncation."""
        L = ks_wall_log((1, 1), 1, 4, 'A1')
        assert L.get((1, 1)) == 1
        assert L.get((2, 2)) == Fraction(1, 2)
        # (3,3) has height 6 > 4, should be absent
        assert L.get((3, 3)) == 0

    def test_lie_element_zero(self):
        z = LieElement.zero(10)
        assert z.is_zero()

    def test_coha_charges_sorted(self):
        e = CoHAElement({(2, 1): Fraction(1), (1, 0): Fraction(1),
                         (0, 1): Fraction(1)}, 10, 'A1')
        charges = e.charges()
        assert charges[0] in [(1, 0), (0, 1)]
        assert charges[-1] == (2, 1)
