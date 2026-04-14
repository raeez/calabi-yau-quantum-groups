"""Tests for Rep^{E_2}(Y(g_{K3})): the chiral quantum group output category.

STATUS: All results CONJECTURAL (AP-CY14) — the K3 Yangian Y(g_{K3}) is NOT
constructed.  Tests verify internal consistency of what the category MUST be.

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        thm:bzfn (drinfeld_center.tex): Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}(A))
        cor:zder-drinfeld: chiral derived center = Drinfeld center
        sec:drinfeld-center-def: definition of Drinfeld center
    Chapter on K3 x E (k3_times_e.tex):
        K3 geometry, Igusa cusp form, K3 DCA

Literature ground truth:
    24-coloured partitions (coefficients of 1/eta^{24}):
        p_{24}(0) = 1, p_{24}(1) = 24, p_{24}(2) = 324,
        p_{24}(3) = 3200, p_{24}(4) = 25650, p_{24}(5) = 176256
    # VERIFIED [DC] Euler product computation [LT] OEIS A006922

    Mukai lattice: rank 24, signature (4, 20)
    # VERIFIED [LT] Mukai, "On the moduli space of bundles on K3" (1987)

    Structure function: g_a(u) = (u - h_a)/(u + h_a)
        g_a(u) * g_a(-u) = 1 (unitarity)
        g_a(0) = -1 (fermionic twist)
        g_a(infinity) = 1 (normalization)
    # VERIFIED [DC] algebraic computation [LT] Maulik-Okounkov arXiv:1211.1287

    Drinfeld double: dim Drin(H_Muk) = 49 = 24 + 24 + 1
    # VERIFIED [DC] generator count [LT] Kassel, "Quantum Groups" (1995)

    Ribbon twist: theta = g(0)^{-1} = -1 on charge-1 modules
    # VERIFIED [DC] algebraic computation [SY] spin-statistics for half-hypers
"""

import pytest
from fractions import Fraction

from compute.lib.chiral_qg_rep_category import (
    BPSCorrespondence,
    EvaluationModule,
    RibbonData,
    braiding_charge_1,
    braiding_charge_2_same_direction,
    braiding_cross_direction,
    bps_correspondence,
    charge_2_state_decomposition,
    coloured_partitions_count,
    evaluation_module,
    fock_space_dimension,
    fusion_locus_full_k3,
    fusion_locus_single_direction,
    is_tensor_product_irreducible,
    modularity_obstruction,
    rep_e2_summary,
    ribbon_structure,
    simple_objects_charge_1,
    tensor_product_module,
    verify_braiding_unitarity,
    verify_braiding_ybe_scalar,
    verify_full_category,
    verify_twist_compatibility,
)

F = Fraction


# ================================================================
# Section 1: COLOURED PARTITION COMBINATORICS
# ================================================================

class TestColouredPartitions:
    """Test the 24-coloured partition function (Fock space dimensions)."""

    def test_p24_0(self):
        """p_{24}(0) = 1: empty partition."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(0) == 1

    def test_p24_1(self):
        """p_{24}(1) = 24: one box in one of 24 colours."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(1) == 24

    def test_p24_2(self):
        """p_{24}(2) = 324 = 24 + 24 + 276."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(2) == 324

    def test_p24_3(self):
        """p_{24}(3) = 3200."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(3) == 3200

    def test_p24_4(self):
        """p_{24}(4) = 25650."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(4) == 25650

    def test_p24_5(self):
        """p_{24}(5) = 176256."""
        # VERIFIED [DC] direct computation [LT] OEIS A006922
        assert coloured_partitions_count(5) == 176256

    def test_negative(self):
        """p_{24}(n) = 0 for n < 0."""
        assert coloured_partitions_count(-1) == 0
        assert coloured_partitions_count(-5) == 0

    def test_fock_dimension_equals_partition_count(self):
        """Fock space dimension = coloured partition count."""
        for n in range(6):
            assert fock_space_dimension(n) == coloured_partitions_count(n)

    def test_p1_is_ordinary_partitions(self):
        """With 1 colour, should recover ordinary partition numbers."""
        # p(n) = 1, 1, 2, 3, 5, 7, 11  (OEIS A000041)
        expected = [1, 1, 2, 3, 5, 7, 11]
        for n, exp in enumerate(expected):
            assert coloured_partitions_count(n, colours=1) == exp

    def test_p2_coloured(self):
        """With 2 colours: p_2(n)."""
        # Coefficients of 1/(1-q)^2 * 1/(1-q^2)^2 * ...
        # p_2(0)=1, p_2(1)=2, p_2(2)=5, p_2(3)=10, p_2(4)=20
        # VERIFIED [DC] direct computation
        assert coloured_partitions_count(0, colours=2) == 1
        assert coloured_partitions_count(1, colours=2) == 2
        assert coloured_partitions_count(2, colours=2) == 5


class TestCharge2Decomposition:
    """Test the decomposition of the charge-2 Fock space."""

    def test_total_equals_324(self):
        """Total charge-2 states = 324 = p_{24}(2)."""
        decomp = charge_2_state_decomposition()
        assert decomp['total'] == 324

    def test_type_a_count(self):
        """Type A (double point, single colour): 24 states."""
        decomp = charge_2_state_decomposition()
        assert decomp['type_A_double_point'] == 24

    def test_type_b_count(self):
        """Type B (fat point, single colour): 24 states."""
        decomp = charge_2_state_decomposition()
        assert decomp['type_B_fat_point'] == 24

    def test_type_c_count(self):
        """Type C (two distinct colours): C(24,2) = 276 states."""
        decomp = charge_2_state_decomposition()
        assert decomp['type_C_two_distinct'] == 276

    def test_decomposition_formula(self):
        """24 + 24 + 276 = 324."""
        decomp = charge_2_state_decomposition()
        assert (decomp['type_A_double_point']
                + decomp['type_B_fat_point']
                + decomp['type_C_two_distinct']) == 324


# ================================================================
# Section 2: SIMPLE OBJECTS (EVALUATION MODULES)
# ================================================================

class TestSimpleObjects:
    """Test the structure of simple objects at charge 1."""

    def test_num_families(self):
        """24 families of evaluation modules (one per Mukai direction)."""
        simples = simple_objects_charge_1()
        assert simples['num_families'] == 24

    def test_positive_mukai_directions(self):
        """4 positive Mukai directions."""
        simples = simple_objects_charge_1()
        assert simples['num_positive_mukai'] == 4

    def test_negative_mukai_directions(self):
        """20 negative Mukai directions."""
        simples = simple_objects_charge_1()
        assert simples['num_negative_mukai'] == 20

    def test_is_continuous(self):
        """Simple objects form a continuous family (not finite)."""
        simples = simple_objects_charge_1()
        assert simples['is_continuous'] is True

    def test_evaluation_module_creation(self):
        """Can create evaluation modules in valid directions."""
        for d in [1, 12, 24]:
            mod = evaluation_module(F(3), d)
            assert mod.mukai_direction == d
            assert mod.charge == 1
            assert mod.status == 'CONJECTURAL'

    def test_evaluation_module_invalid_direction(self):
        """Direction out of range raises ValueError."""
        with pytest.raises(ValueError):
            evaluation_module(F(1), 0)
        with pytest.raises(ValueError):
            evaluation_module(F(1), 25)

    def test_evaluation_module_positive_mukai(self):
        """Directions 1-4 have positive h values (Kummer parametrization)."""
        for d in range(1, 5):
            mod = evaluation_module(F(1), d)
            assert mod.h_value > 0

    def test_evaluation_module_negative_mukai(self):
        """Directions 5-24 have negative h values (Kummer parametrization)."""
        for d in range(5, 25):
            mod = evaluation_module(F(1), d)
            assert mod.h_value < 0

    def test_tensor_product_charge(self):
        """Tensor product of n charge-1 modules has charge n."""
        mods = [evaluation_module(F(k), k) for k in range(1, 5)]
        tp = tensor_product_module(mods)
        assert tp['charge'] == 4
        assert tp['num_particles'] == 4


# ================================================================
# Section 3: BRAIDING (E_2 STRUCTURE)
# ================================================================

class TestBraiding:
    """Test the braiding on Rep^{E_2}(Y(g_{K3}))."""

    def test_same_direction_nontrivial(self):
        """Braiding in the same direction is nontrivial (g(u) != 1)."""
        # AP-CY28: avoid poles. Use u_a = 7, u_b = 3.
        result = braiding_charge_1(F(7), F(3), 1, 1)
        assert result['same_direction'] is True
        assert result['braiding_value'] != 1

    def test_same_direction_value(self):
        """Check explicit braiding value for direction 1 (h = 1)."""
        # h_1 = 1 (Kummer, eps=1). u - v = 4.
        # g_1(4) = (4-1)/(4+1) = 3/5
        result = braiding_charge_1(F(7), F(3), 1, 1)
        assert result['braiding_value'] == F(3, 5)

    def test_different_direction_is_swap(self):
        """Different Mukai directions: braiding is the swap operator."""
        result = braiding_charge_1(F(7), F(3), 1, 5)
        assert result['same_direction'] is False
        assert result['braiding_value'] == 'P (swap)'

    def test_pole_detection(self):
        """Braiding detects the pole at u - v = -h_a."""
        # Direction 1: h_1 = 1. Pole at u - v = -1.
        # Choose u = 3, v = 4 so u - v = -1.
        result = braiding_charge_1(F(3), F(4), 1, 1)
        assert result['braiding_value'] == 'POLE'

    def test_braiding_at_zero_spectral_diff(self):
        """At u = v: g(0) = -1 for h != 0."""
        # u_a = u_b = 5, direction 1, h_1 = 1.
        # g_1(0) = (0-1)/(0+1) = -1.
        result = braiding_charge_1(F(5), F(5), 1, 1)
        assert result['braiding_value'] == F(-1)


class TestBraidingUnitarity:
    """Test R(u) * R(-u) = 1 (unitarity)."""

    def test_unitarity_positive_direction(self):
        """Unitarity at a positive Mukai direction."""
        # AP-CY28: use safe test point u = 3, direction 1 (h = 1).
        result = verify_braiding_unitarity(F(3), 1)
        assert result['unitarity_holds'] is True

    def test_unitarity_negative_direction(self):
        """Unitarity at a negative Mukai direction."""
        # Direction 5: h_5 = -1/5. Use u = 3.
        result = verify_braiding_unitarity(F(3), 5)
        assert result['unitarity_holds'] is True

    def test_unitarity_multiple_points(self):
        """Unitarity at multiple test points and directions."""
        test_points = [F(3), F(7), F(11), F(13, 3)]
        for u in test_points:
            for d in [1, 5, 13, 24]:
                result = verify_braiding_unitarity(u, d)
                assert result['unitarity_holds'] is True, (
                    f"Unitarity failed at u={u}, direction={d}"
                )


class TestBraidingYBE:
    """Test Yang-Baxter equation at charge 1."""

    def test_ybe_scalar(self):
        """YBE is trivial at charge 1 (scalar R-matrix)."""
        result = verify_braiding_ybe_scalar(F(3), F(7), 1)
        assert result['ybe_holds'] is True

    def test_ybe_multiple_directions(self):
        """YBE holds at all Mukai directions (scalar case)."""
        for d in [1, 5, 12, 24]:
            result = verify_braiding_ybe_scalar(F(3), F(7), d)
            assert result['ybe_holds'] is True


class TestCharge2Braiding:
    """Test the charge-2 R-matrix."""

    def test_charge_2_same_direction_diagonal(self):
        """Charge-2 R-matrix is diagonal for abelian Yangian."""
        # AP-CY28: use u far from poles. Direction 1 (h=1), u = 7.
        result = braiding_charge_2_same_direction(F(7), 1)
        assert result['is_diagonal'] is True

    def test_charge_2_eigenvalues_distinct(self):
        """The two eigenvalues lambda_{(2)} and lambda_{(1,1)} differ."""
        result = braiding_charge_2_same_direction(F(7), 1)
        assert result['eigenvalue_partition_2'] != result['eigenvalue_partition_11']

    def test_cross_direction_factorizes(self):
        """Cross-direction R-matrix factorizes: g_a(u) * g_b(u)."""
        result = braiding_cross_direction(F(7), 1, 5)
        assert result['factorizes'] is True

    def test_cross_direction_value(self):
        """Check explicit cross-direction value."""
        # Direction 1: h_1 = 1. g_1(7) = (7-1)/(7+1) = 6/8 = 3/4.
        # Direction 5: h_5 = -1/5. g_5(7) = (7+1/5)/(7-1/5) = (36/5)/(34/5) = 36/34 = 18/17.
        # Product: 3/4 * 18/17 = 54/68 = 27/34.
        result = braiding_cross_direction(F(7), 1, 5)
        assert result['R_value'] == F(27, 34)

    def test_cross_direction_rejects_same(self):
        """Cross-direction function rejects a = b."""
        with pytest.raises(ValueError):
            braiding_cross_direction(F(7), 1, 1)


# ================================================================
# Section 4: FUSION RULES
# ================================================================

class TestFusionRules:
    """Test the fusion rules: when tensor products are reducible."""

    def test_fusion_locus_direction_1(self):
        """Direction 1 (h=1): reducible at u-v = +/-1."""
        result = fusion_locus_single_direction(1)
        assert result['h_value'] == F(1)
        assert F(1) in result['fusion_locus']
        assert F(-1) in result['fusion_locus']

    def test_fusion_locus_direction_5(self):
        """Direction 5 (h=-1/5): reducible at u-v = +/-(-1/5)."""
        result = fusion_locus_single_direction(5)
        assert result['h_value'] == F(-1, 5)
        assert F(-1, 5) in result['fusion_locus']
        assert F(1, 5) in result['fusion_locus']

    def test_generic_irreducible(self):
        """Generic spectral parameter difference gives irreducible."""
        result = fusion_locus_single_direction(1)
        assert result['generic_irreducible'] is True

    def test_full_k3_fusion_locus(self):
        """Full K3 has 2 distinct fusion magnitudes (Kummer parametrization)."""
        # |h| = 1 (directions 1-4) and |h| = 1/5 (directions 5-24)
        result = fusion_locus_full_k3()
        assert result['num_distinct_magnitudes'] == 2

    def test_irreducible_different_directions(self):
        """Different Mukai directions: always irreducible."""
        result = is_tensor_product_irreducible(F(3), F(7), 1, 5)
        assert result['irreducible'] is True

    def test_irreducible_generic_same_direction(self):
        """Same direction, generic u-v: irreducible."""
        # Direction 1, h=1. u-v = 4 != +/-1.
        result = is_tensor_product_irreducible(F(7), F(3), 1, 1)
        assert result['irreducible'] is True

    def test_reducible_at_fusion(self):
        """Same direction, u-v = h: reducible."""
        # Direction 1, h=1. u-v = 1.
        result = is_tensor_product_irreducible(F(4), F(3), 1, 1)
        assert result['irreducible'] is False

    def test_reducible_at_negative_fusion(self):
        """Same direction, u-v = -h: reducible."""
        # Direction 1, h=1. u-v = -1.
        result = is_tensor_product_irreducible(F(3), F(4), 1, 1)
        assert result['irreducible'] is False


# ================================================================
# Section 5: RIBBON STRUCTURE AND MODULARITY
# ================================================================

class TestRibbon:
    """Test the ribbon (twist) structure."""

    def test_has_ribbon(self):
        """Rep^{E_2}(Y(g_{K3})) has ribbon structure."""
        ribbon = ribbon_structure()
        assert ribbon.has_ribbon is True

    def test_twist_charge_1(self):
        """Twist on charge-1 modules: theta = -1 (fermionic)."""
        ribbon = ribbon_structure()
        assert ribbon.twist_value_charge_1 == F(-1)

    def test_twist_compatibility(self):
        """Twist axiom: theta_{V tensor W} = beta^2 * (theta_V theta_W)."""
        result = verify_twist_compatibility()
        assert result['consistency'] is True

    def test_twist_charge_2_bosonic(self):
        """Charge-2 twist: theta = (-1)^2 = 1 (bosonic bound state)."""
        result = verify_twist_compatibility()
        assert result['theta_charge_2'] == F(1)


class TestModularity:
    """Test that the category is NOT modular."""

    def test_not_modular(self):
        """Rep^{E_2}(Y(g_{K3})) is NOT a modular tensor category."""
        result = modularity_obstruction()
        assert result['is_modular'] is False

    def test_three_obstructions(self):
        """There are exactly 3 obstructions to modularity."""
        result = modularity_obstruction()
        assert len(result['obstructions']) == 3

    def test_continuous_simples_obstruction(self):
        """First obstruction: continuous family of simples."""
        result = modularity_obstruction()
        assert 'Continuous simples' == result['obstructions'][0]['name']


# ================================================================
# Section 6: BPS CORRESPONDENCE
# ================================================================

class TestBPSCorrespondence:
    """Test the BPS physics interpretation."""

    def test_bps_correspondence_type(self):
        """BPS correspondence returns proper type."""
        bps = bps_correspondence()
        assert isinstance(bps, BPSCorrespondence)

    def test_bps_status_conjectural(self):
        """BPS correspondence is CONJECTURAL."""
        bps = bps_correspondence()
        assert bps.status == 'CONJECTURAL'

    def test_charge_lattice_rank_24(self):
        """Charge lattice has rank 24 (Mukai lattice)."""
        bps = bps_correspondence()
        assert '24' in bps.charge_lattice

    def test_signature_4_20(self):
        """Mass formula has signature (4,20)."""
        bps = bps_correspondence()
        assert '4' in bps.mass_formula and '20' in bps.mass_formula


# ================================================================
# Section 7: FULL CATEGORY VERIFICATION
# ================================================================

class TestFullCategory:
    """Test the complete category structure."""

    def test_full_verification_passes(self):
        """All consistency checks pass."""
        result = verify_full_category()
        assert result['all_pass'] is True

    def test_fock_dimensions_correct(self):
        """Fock space dimensions match known values."""
        result = verify_full_category()
        assert result['fock_dimensions']['pass'] is True

    def test_unitarity_passes(self):
        """Unitarity R(u)*R(-u) = 1 passes at all test points."""
        result = verify_full_category()
        assert result['unitarity']['all_pass'] is True

    def test_ybe_passes(self):
        """Yang-Baxter equation passes."""
        result = verify_full_category()
        assert result['ybe']['all_pass'] is True

    def test_twist_consistent(self):
        """Ribbon twist is consistent."""
        result = verify_full_category()
        assert result['twist']['consistent'] is True

    def test_status_conjectural(self):
        """Overall status is CONJECTURAL."""
        result = verify_full_category()
        assert result['status'] == 'CONJECTURAL'


class TestSummary:
    """Test the full summary function."""

    def test_summary_name(self):
        """Category name is correct."""
        summary = rep_e2_summary()
        assert summary['name'] == 'Rep^{E_2}(Y(g_{K3}))'

    def test_summary_type(self):
        """Category type is braided monoidal (E_2)."""
        summary = rep_e2_summary()
        assert 'E_2' in summary['type']

    def test_summary_24_families(self):
        """24 families of simple objects."""
        summary = rep_e2_summary()
        assert summary['simple_objects']['num_families'] == 24

    def test_summary_continuous(self):
        """Simple objects form a continuous family."""
        summary = rep_e2_summary()
        assert summary['simple_objects']['is_continuous'] is True

    def test_summary_not_modular(self):
        """Category is not modular."""
        summary = rep_e2_summary()
        assert summary['is_modular'] is False

    def test_summary_fock_dim_0(self):
        """Fock dim at charge 0 is 1."""
        summary = rep_e2_summary()
        assert summary['fock_dimensions'][0] == 1

    def test_summary_fock_dim_1(self):
        """Fock dim at charge 1 is 24."""
        summary = rep_e2_summary()
        assert summary['fock_dimensions'][1] == 24

    def test_summary_fock_dim_2(self):
        """Fock dim at charge 2 is 324."""
        summary = rep_e2_summary()
        assert summary['fock_dimensions'][2] == 324

    def test_summary_classical_dim(self):
        """Classical limit: Drinfeld double has dimension 49."""
        summary = rep_e2_summary()
        assert summary['classical_limit']['dimension'] == 49

    def test_summary_has_ribbon(self):
        """Summary reports ribbon structure."""
        summary = rep_e2_summary()
        assert summary['ribbon']['has_ribbon'] is True

    def test_summary_ybe(self):
        """Summary reports YBE satisfaction."""
        summary = rep_e2_summary()
        assert summary['braiding']['ybe'] is True

    def test_summary_4_dependencies(self):
        """Summary lists exactly 4 dependencies."""
        summary = rep_e2_summary()
        assert len(summary['dependencies']) == 4
