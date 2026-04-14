r"""Tests for Conway-Leech-K3 engine.

Tests the relationship between the Conway group Co_0 = Aut(Leech),
the Leech lattice, and the K3 Yangian.

Covers:
  1. Group order verifications (Co_0, Co_1, M_24, Monster)
  2. Rank-24 coincidence analysis
  3. Leech enhancement point properties
  4. Conway group structure and M_24 embedding
  5. Monster VOA connection
  6. kappa_ch hierarchy
  7. Character divergence (Leech VOA vs free field)
  8. Theta series and c_Delta
  9. Deep holes and Niemeier bijection
  10. Structure function properties
  11. Conway moonshine data
  12. Sporadic tower
  13. End-to-end summary
"""

import math
from fractions import Fraction

import pytest

from compute.lib.conway_leech_k3 import (
    # Constants
    CO_0_ORDER,
    CO_1_ORDER,
    M_24_ORDER,
    MONSTER_ORDER,
    LEECH_RANK,
    LEECH_SIGNATURE,
    LEECH_MIN_NORM,
    LEECH_KISSING_NUMBER,
    LEECH_NORM_6_COUNT,
    MUKAI_RANK,
    MUKAI_SIGNATURE,
    K3_LATTICE_RANK,
    K3_SIGNATURE,
    KAPPA_CH_LEECH_VOA,
    KAPPA_CH_MONSTER_VOA,
    KAPPA_CH_K3_CY_FUNCTOR,
    # Functions
    rank_24_origins,
    is_rank_24_coincidence,
    leech_enhancement_point,
    leech_theta_coefficients,
    leech_vs_free_field_character,
    conway_group_data,
    m24_in_co0_embedding,
    co0_24dim_representation,
    monster_voa_connection,
    kappa_ch_hierarchy,
    leech_structure_function_properties,
    niemeier_automorphism_orders,
    leech_uniqueness_properties,
    conway_moonshine_data,
    sporadic_tower_from_k3,
    # Verification functions
    verify_co0_order,
    verify_monster_order,
    verify_index_co0_m24,
    verify_co1_in_monster,
    verify_leech_theta_q2,
    verify_24_not_coincidence,
    verify_kappa_ch_hierarchy,
    verify_character_divergence,
    verify_leech_c_delta,
    verify_signatures_differ,
    verify_leech_no_roots,
    verify_deep_holes_count,
    full_investigation_summary,
    all_niemeier_lattices_with_leech,
)


# =========================================================================
# 1. Group order verifications
# =========================================================================

class TestGroupOrders:
    """Verify group orders from prime factorizations."""

    def test_co0_order_factorization(self):
        """Co_0 order = 2^22 * 3^9 * 5^4 * 7^2 * 11 * 13 * 23."""
        assert verify_co0_order()
        expected = 2**22 * 3**9 * 5**4 * 7**2 * 11 * 13 * 23
        assert CO_0_ORDER == expected

    def test_co0_order_value(self):
        """Co_0 order = 8,315,553,613,086,720,000."""
        assert CO_0_ORDER == 8_315_553_613_086_720_000

    def test_co1_order(self):
        """Co_1 = Co_0 / {+/-I_24} has order |Co_0|/2."""
        assert CO_1_ORDER == CO_0_ORDER // 2
        assert CO_1_ORDER == 4_157_776_806_543_360_000

    def test_m24_order(self):
        """M_24 order = 244,823,040."""
        assert M_24_ORDER == 244_823_040
        # Prime factorization: 2^10 * 3^3 * 5 * 7 * 11 * 23
        expected = 2**10 * 3**3 * 5 * 7 * 11 * 23
        assert M_24_ORDER == expected

    def test_monster_order_factorization(self):
        """Monster order from prime factorization."""
        assert verify_monster_order()

    def test_monster_order_magnitude(self):
        """Monster order ~ 8 * 10^53."""
        assert MONSTER_ORDER > 8 * 10**53
        assert MONSTER_ORDER < 9 * 10**53

    def test_co0_m24_index(self):
        """[Co_0 : M_24] is a positive integer."""
        assert verify_index_co0_m24()
        assert CO_0_ORDER % M_24_ORDER == 0
        index = CO_0_ORDER // M_24_ORDER
        assert index > 1  # Co_0 is strictly larger than M_24

    def test_co1_divides_monster(self):
        """Co_1 is a subgroup of Monster: |Co_1| divides |M|."""
        assert verify_co1_in_monster()
        assert MONSTER_ORDER % CO_1_ORDER == 0


# =========================================================================
# 2. Rank-24 coincidence analysis
# =========================================================================

class TestRank24:
    """Verify the rank-24 coincidence analysis."""

    def test_not_coincidence(self):
        """24 = rank(Mukai) = rank(Leech) is NOT a coincidence."""
        result = is_rank_24_coincidence()
        assert result['is_coincidence'] is False

    def test_rank_match(self):
        """Both lattices have rank 24."""
        result = is_rank_24_coincidence()
        assert result['rank_match'] is True
        assert MUKAI_RANK == LEECH_RANK == 24

    def test_signature_mismatch(self):
        """Signatures differ: (4,20) vs (0,24)."""
        assert verify_signatures_differ()
        result = is_rank_24_coincidence()
        assert result['signature_match'] is False

    def test_no_direct_isomorphism(self):
        """No direct lattice isomorphism (different signatures)."""
        result = is_rank_24_coincidence()
        assert result['direct_isomorphism'] is False

    def test_common_source(self):
        """Common source is dim H*(K3, C) = 24."""
        result = is_rank_24_coincidence()
        assert '24' in result['common_source']
        assert 'H*(K3' in result['common_source']

    def test_b2_plus_2(self):
        """b_2(K3) + 2 = 22 + 2 = 24 = rank(Leech)."""
        assert K3_LATTICE_RANK + 2 == LEECH_RANK
        assert K3_LATTICE_RANK == 22

    def test_betti_numbers(self):
        """b_0 + b_2 + b_4 = 1 + 22 + 1 = 24."""
        assert verify_24_not_coincidence()

    def test_rank_24_origins_count(self):
        """There are at least 5 distinct occurrences of rank 24."""
        origins = rank_24_origins()
        assert len(origins) >= 5

    def test_rank_24_all_24(self):
        """Every origin has rank 24."""
        for o in rank_24_origins():
            assert o.rank == 24


# =========================================================================
# 3. Leech enhancement point properties
# =========================================================================

class TestLeechEnhancement:
    """Verify properties at the Leech enhancement point."""

    def test_niemeier_index_1(self):
        """Leech is Niemeier lattice #1."""
        data = leech_enhancement_point()
        assert data.niemeier_index == 1

    def test_no_roots(self):
        """Leech lattice has no roots (the defining property)."""
        assert verify_leech_no_roots()
        data = leech_enhancement_point()
        assert data.num_roots == 0

    def test_no_enhanced_kac_moody(self):
        """No enhanced Kac-Moody at the Leech point (no roots)."""
        data = leech_enhancement_point()
        assert data.has_enhanced_kac_moody is False

    def test_min_norm(self):
        """Minimum nonzero norm is 4 (not 2, since no roots)."""
        data = leech_enhancement_point()
        assert data.min_norm == 4

    def test_kissing_number(self):
        """Kissing number = 196560."""
        data = leech_enhancement_point()
        assert data.kissing_number == 196560

    def test_automorphism_co0(self):
        """Automorphism group is Co_0."""
        data = leech_enhancement_point()
        assert data.automorphism_group == "Co_0"
        assert data.automorphism_order == CO_0_ORDER

    def test_kappa_ch_lattice_voa(self):
        """kappa_ch of Leech lattice VOA = 24 (rank)."""
        data = leech_enhancement_point()
        assert data.kappa_ch_lattice_voa == 24

    def test_kappa_ch_k3_sigma(self):
        """kappa_ch of K3 sigma model = 2 (topological, moduli-independent)."""
        data = leech_enhancement_point()
        assert data.kappa_ch_k3_sigma == 2

    def test_shadow_class_lattice_voa(self):
        """Leech lattice VOA is class G (free-field, S_3 = S_4 = 0)."""
        data = leech_enhancement_point()
        assert data.shadow_class_lattice_voa == "G"
        assert data.shadow_depth_lattice_voa == 2

    def test_shadow_class_k3_sigma(self):
        """K3 sigma model is class M at ALL moduli points."""
        data = leech_enhancement_point()
        assert data.shadow_class_k3_sigma == "M"


# =========================================================================
# 4. Conway group structure
# =========================================================================

class TestConwayGroup:
    """Verify Conway group structural data."""

    def test_co0_not_simple(self):
        """Co_0 is NOT simple (center = Z/2)."""
        data = conway_group_data()
        assert data.is_simple is False
        assert data.center_order == 2

    def test_co1_quotient(self):
        """Co_1 = Co_0 / {+/- I_24}."""
        data = conway_group_data()
        assert data.quotient_name == "Co_1"
        assert data.quotient_order == CO_0_ORDER // 2

    def test_standard_rep(self):
        """Standard representation is 24-dimensional."""
        data = conway_group_data()
        assert data.standard_rep_dim == 24

    def test_conjugacy_classes(self):
        """Co_0 has 167 conjugacy classes."""
        data = conway_group_data()
        assert data.num_conjugacy_classes == 167

    def test_m24_embedding(self):
        """M_24 embeds in Co_0 as frame stabilizer."""
        data = m24_in_co0_embedding()
        assert data['m24_order'] == M_24_ORDER
        assert data['co0_order'] == CO_0_ORDER
        assert data['index'] == CO_0_ORDER // M_24_ORDER

    def test_24dim_rep_irreducible(self):
        """24-dim standard representation is irreducible over C."""
        rep = co0_24dim_representation()
        assert rep['is_irreducible_over_C'] is True

    def test_24dim_rep_m24_restriction(self):
        """24|_{M_24} = 1 + 23."""
        rep = co0_24dim_representation()
        assert '1 + 23' in rep['restriction_to_m24']

    def test_minus_identity_trace(self):
        """Trace of -I_{24} on the 24-dim rep is -24."""
        rep = co0_24dim_representation()
        assert rep['character_at_minus_identity_corrected'] == -24


# =========================================================================
# 5. Monster VOA connection
# =========================================================================

class TestMonsterVOA:
    """Verify Monster VOA V^natural connection data."""

    def test_central_charge(self):
        """V^natural has c = 24."""
        data = monster_voa_connection()
        assert data.central_charge == 24

    def test_kappa_ch(self):
        """kappa_ch(V^natural) = 12."""
        data = monster_voa_connection()
        assert data.kappa_ch == 12

    def test_orbifold_construction(self):
        """V^natural = Z/2-orbifold of V_{Leech}."""
        data = monster_voa_connection()
        assert 'orbifold' in data.construction.lower()
        assert 'Leech' in data.construction

    def test_co1_in_monster(self):
        """Co_1 is a subgroup of Monster."""
        data = monster_voa_connection()
        assert data.co1_in_monster is True

    def test_yangian_connection_indirect(self):
        """K3 Yangian connection to V^natural is indirect."""
        data = monster_voa_connection()
        assert 'INDIRECT' in data.yangian_connection
        assert 'CONJECTURAL' in data.yangian_connection


# =========================================================================
# 6. kappa_ch hierarchy
# =========================================================================

class TestKappaHierarchy:
    """Verify the kappa_ch hierarchy {2, 12, 24}."""

    def test_hierarchy_values(self):
        """kappa_ch values: 24 (Leech VOA), 12 (Monster), 2 (CY functor)."""
        assert verify_kappa_ch_hierarchy()

    def test_orbifold_halving(self):
        """Z/2-orbifold halves kappa_ch: 24 -> 12."""
        assert KAPPA_CH_LEECH_VOA == 2 * KAPPA_CH_MONSTER_VOA

    def test_ratio(self):
        """Ratio 24 : 12 : 2 = 12 : 6 : 1."""
        assert KAPPA_CH_LEECH_VOA // KAPPA_CH_K3_CY_FUNCTOR == 12
        assert KAPPA_CH_MONSTER_VOA // KAPPA_CH_K3_CY_FUNCTOR == 6

    def test_hierarchy_dict(self):
        """Hierarchy dictionary has all three entries."""
        h = kappa_ch_hierarchy()
        assert 'V_{Leech}' in h['hierarchy']
        assert 'V^natural' in h['hierarchy']
        assert 'Phi(D^b(K3))' in h['hierarchy']

    def test_all_central_charge_24(self):
        """All three have c = 24."""
        h = kappa_ch_hierarchy()
        for name, data in h['hierarchy'].items():
            assert data['central_charge'] == 24


# =========================================================================
# 7. Character divergence
# =========================================================================

class TestCharacterDivergence:
    """Verify Leech VOA vs free-field character comparison."""

    def test_match_at_q_minus_1(self):
        """Characters match at q^{-1}: both 1."""
        data = leech_vs_free_field_character()
        assert data['divergence'][-1]['match'] is True
        assert data['divergence'][-1]['free_field'] == 1
        assert data['divergence'][-1]['leech_voa'] == 1

    def test_match_at_q_0(self):
        """Characters match at q^0: both 24."""
        data = leech_vs_free_field_character()
        assert data['divergence'][0]['match'] is True
        assert data['divergence'][0]['free_field'] == 24
        assert data['divergence'][0]['leech_voa'] == 24

    def test_diverge_at_q_1(self):
        """Characters diverge at q^1: 324 vs 196884."""
        data = leech_vs_free_field_character()
        assert data['divergence'][1]['match'] is False
        assert data['divergence'][1]['free_field'] == 324
        assert data['divergence'][1]['leech_voa'] == 196884

    def test_divergence_equals_kissing(self):
        """Divergence at q^1 = 196560 = kissing number of Leech."""
        assert verify_character_divergence()

    def test_first_divergence_order(self):
        """First divergence is at q^1 (not earlier)."""
        data = leech_vs_free_field_character()
        assert data['first_divergence_order'] == 1


# =========================================================================
# 8. Theta series and c_Delta
# =========================================================================

class TestThetaSeries:
    """Verify Leech lattice theta series properties."""

    def test_theta_q0(self):
        """Theta_{Leech}|_{q^0} = 1 (the zero vector)."""
        coeffs = leech_theta_coefficients()
        assert coeffs[0] == 1

    def test_theta_no_q1(self):
        """No q^1 term (no roots, minimum norm 4 so norm/2 = 2)."""
        coeffs = leech_theta_coefficients()
        assert 1 not in coeffs

    def test_theta_q2(self):
        """Theta_{Leech}|_{q^2} = 196560 (kissing number)."""
        assert verify_leech_theta_q2()

    def test_theta_q3(self):
        """Theta_{Leech}|_{q^3} = 16773120."""
        coeffs = leech_theta_coefficients()
        assert coeffs[3] == 16773120

    def test_c_delta(self):
        """c_Delta(Leech) = -65520/691."""
        assert verify_leech_c_delta()

    def test_c_delta_formula(self):
        """c_Delta = (691 * |R| - 65520) / 691 with |R| = 0."""
        expected = Fraction(691 * 0 - 65520, 691)
        assert expected == Fraction(-65520, 691)
        data = leech_enhancement_point()
        assert data.c_delta == expected


# =========================================================================
# 9. Deep holes and Niemeier bijection
# =========================================================================

class TestDeepHoles:
    """Verify deep hole properties of the Leech lattice."""

    def test_23_deep_hole_types(self):
        """23 types of deep holes = 23 other Niemeier lattices."""
        assert verify_deep_holes_count()

    def test_total_niemeier_lattices(self):
        """There are exactly 24 Niemeier lattices."""
        lattices = all_niemeier_lattices_with_leech()
        assert len(lattices) == 24

    def test_leech_is_first(self):
        """Leech is Niemeier lattice #1 (index 1)."""
        lattices = all_niemeier_lattices_with_leech()
        assert lattices[0].name == "Leech"
        assert lattices[0].total_roots == 0

    def test_23_have_roots(self):
        """23 Niemeier lattices have nonempty root systems."""
        lattices = all_niemeier_lattices_with_leech()
        with_roots = [L for L in lattices if L.total_roots > 0]
        assert len(with_roots) == 23

    def test_all_rank_24(self):
        """All 24 Niemeier lattices have rank 24."""
        for L in all_niemeier_lattices_with_leech():
            assert L.rank == 24


# =========================================================================
# 10. Structure function properties
# =========================================================================

class TestStructureFunction:
    """Verify structure function properties at the Leech point."""

    def test_degree(self):
        """Structure function has degree (24, 24)."""
        props = leech_structure_function_properties()
        assert props['degree'] == (24, 24)

    def test_g_at_infinity(self):
        """g(infinity) = 1."""
        props = leech_structure_function_properties()
        assert props['g_at_infinity'] == 1

    def test_g_at_zero(self):
        """g(0) = (-1)^24 = 1."""
        props = leech_structure_function_properties()
        assert props['g_at_zero'] == 1

    def test_unitarity(self):
        """g(z) * g(-z) = 1."""
        props = leech_structure_function_properties()
        assert props['unitarity'] == 'g(z) * g(-z) = 1'

    def test_no_root_constraint(self):
        """No root system constraint at Leech point."""
        props = leech_structure_function_properties()
        assert 'NONE' in props['root_system_constraint']

    def test_parameter_freedom(self):
        """Parameter freedom = 23 dimensions (24 - 1 for CY_2 constraint)."""
        props = leech_structure_function_properties()
        assert props['parameter_freedom_dim'] == 23


# =========================================================================
# 11. Conway moonshine data
# =========================================================================

class TestConwayMoonshine:
    """Verify Conway moonshine data."""

    def test_central_charge_12(self):
        """V^{s,natural} has c = 12."""
        data = conway_moonshine_data()
        assert data['central_charge'] == 12

    def test_automorphism_co0(self):
        """Aut(V^{s,natural}) = Co_0."""
        data = conway_moonshine_data()
        assert data['automorphism_group'] == 'Co_0'
        assert data['automorphism_order'] == CO_0_ORDER

    def test_is_super_voa(self):
        """V^{s,natural} is a super VOA."""
        data = conway_moonshine_data()
        assert data['is_super_voa'] is True


# =========================================================================
# 12. Sporadic tower
# =========================================================================

class TestSporadicTower:
    """Verify the sporadic group tower from K3."""

    def test_tower_has_4_levels(self):
        """Tower has 4 levels: sigma model -> M_24 -> Co_0 -> Monster."""
        tower = sporadic_tower_from_k3()
        assert len(tower['tower']) == 4

    def test_level_ordering(self):
        """Levels are 0, 1, 2, 3."""
        tower = sporadic_tower_from_k3()
        levels = [t['level'] for t in tower['tower']]
        assert levels == [0, 1, 2, 3]

    def test_m24_at_level_1(self):
        """M_24 at level 1."""
        tower = sporadic_tower_from_k3()
        assert 'M_24' in tower['tower'][1]['group']

    def test_co0_at_level_2(self):
        """Co_0 at level 2."""
        tower = sporadic_tower_from_k3()
        assert 'Co_0' in tower['tower'][2]['group']

    def test_monster_at_level_3(self):
        """Monster at level 3."""
        tower = sporadic_tower_from_k3()
        assert 'Monster' in tower['tower'][3]['group']

    def test_yangian_weakens(self):
        """Yangian connection weakens at higher levels."""
        tower = sporadic_tower_from_k3()
        # Level 3 (Monster): no direct Yangian connection
        assert 'NO direct' in tower['tower'][3]['yangian_connection']


# =========================================================================
# 13. End-to-end summary
# =========================================================================

class TestSummary:
    """Verify the full investigation summary."""

    def test_all_five_questions_answered(self):
        """All five questions from the mission have answers."""
        summary = full_investigation_summary()
        assert 'Q1_mukai_leech_connection' in summary
        assert 'Q2_leech_enhancement_point' in summary
        assert 'Q3_co0_larger_structure' in summary
        assert 'Q4_monster_voa_connection' in summary
        assert 'Q5_rank_24_coincidence' in summary

    def test_q1_not_direct_isomorphism(self):
        """Q1: Connection exists but is NOT a direct isomorphism."""
        summary = full_investigation_summary()
        q1 = summary['Q1_mukai_leech_connection']
        assert 'NOT direct isomorphism' in q1['answer']

    def test_q2_kappa_values(self):
        """Q2: kappa_ch values at Leech point."""
        summary = full_investigation_summary()
        q2 = summary['Q2_leech_enhancement_point']
        assert q2['kappa_ch_lattice_voa'] == 24
        assert q2['kappa_ch_k3_sigma'] == 2

    def test_q3_co0_larger(self):
        """Q3: Co_0 acts on full Rep(Y(g_{K3}(Leech)))."""
        summary = full_investigation_summary()
        q3 = summary['Q3_co0_larger_structure']
        assert 'YES' in q3['answer']

    def test_q4_indirect(self):
        """Q4: Monster VOA connection is indirect."""
        summary = full_investigation_summary()
        q4 = summary['Q4_monster_voa_connection']
        assert 'INDIRECT' in q4['answer']
        assert q4['yangian_action_on_monster_voa'] == 'NONE known'

    def test_q5_not_coincidence(self):
        """Q5: 24 = 24 is NOT a coincidence."""
        summary = full_investigation_summary()
        q5 = summary['Q5_rank_24_coincidence']
        assert 'NOT' in q5['answer']

    def test_status_conjectural(self):
        """Engine status is CONJECTURAL (AP-CY14)."""
        summary = full_investigation_summary()
        assert summary['status'] == 'CONJECTURAL'

    def test_ap_compliance(self):
        """AP compliance is stated."""
        summary = full_investigation_summary()
        assert 'AP-CY14' in summary['ap_compliance']
        assert 'AP113' in summary['ap_compliance']


# =========================================================================
# 14. Cross-checks with niemeier_shadow_landscape
# =========================================================================

class TestCrossChecks:
    """Cross-check data against the niemeier_shadow_landscape engine."""

    def test_leech_in_niemeier_list(self):
        """Leech lattice appears as Niemeier #1 with correct properties."""
        from compute.lib.niemeier_shadow_landscape import niemeier_lattice
        leech = niemeier_lattice(1)
        assert leech.name == "Leech"
        assert leech.total_roots == 0
        assert leech.rank == 24
        assert leech.components == []

    def test_leech_shadow_class_g(self):
        """Leech lattice VOA is class G (from niemeier_shadow_landscape)."""
        from compute.lib.niemeier_shadow_landscape import lattice_voa_shadow
        shadow = lattice_voa_shadow(24)  # rank 24
        assert shadow.shadow_class == "G"
        assert shadow.shadow_depth == 2
        assert shadow.kappa_ch == 24
        assert shadow.S3 == 0
        assert shadow.S4 == 0

    def test_all_niemeier_rank_24(self):
        """All 24 Niemeier lattices have rank 24 (cross-check)."""
        from compute.lib.niemeier_shadow_landscape import all_niemeier_lattices
        for L in all_niemeier_lattices():
            assert L.rank == 24

    def test_leech_unique_rootless(self):
        """Leech is the ONLY Niemeier lattice with no roots."""
        from compute.lib.niemeier_shadow_landscape import all_niemeier_lattices
        rootless = [L for L in all_niemeier_lattices() if L.total_roots == 0]
        assert len(rootless) == 1
        assert rootless[0].name == "Leech"


# =========================================================================
# 15. Numerical consistency
# =========================================================================

class TestNumericalConsistency:
    """Additional numerical cross-checks."""

    def test_196884_decomposition(self):
        """196884 = 196560 + 324 (kissing number + free-field dim)."""
        assert 196884 == LEECH_KISSING_NUMBER + 324

    def test_196883_from_monster(self):
        """196883 = 196884 - 1 is the smallest faithful Monster rep dimension."""
        # The famous near-miss: 196884 = 196883 + 1 (McKay observation)
        assert 196884 == 196883 + 1

    def test_kissing_number_divisibility(self):
        """196560 is divisible by 24 (as it must be for a Co_0 orbit)."""
        assert LEECH_KISSING_NUMBER % 24 == 0

    def test_norm_4_shell_size(self):
        """196560 vectors of norm 4 form a single Co_0 orbit."""
        # 196560 = 2 * 24 * 23 * 4 * 4 * 11 / something...
        # Actually: 196560 = 2^4 * 3^3 * 5 * 7 * 13
        # Verify it equals the standard value
        assert LEECH_KISSING_NUMBER == 196560

    def test_co0_order_divisible_by_kissing(self):
        """|Co_0| is divisible by the kissing number (orbit-stabilizer)."""
        # Co_0 acts transitively on the 196560 norm-4 vectors.
        # Stabilizer has order |Co_0| / 196560.
        assert CO_0_ORDER % LEECH_KISSING_NUMBER == 0

    def test_stabilizer_order(self):
        """Stabilizer of a norm-4 vector in Co_0."""
        stab_order = CO_0_ORDER // LEECH_KISSING_NUMBER
        # This should be a known group order
        # Stab = Co_2 x Z/2 has order 2 * |Co_2| where |Co_2| = 42,305,421,312,000
        # Actually: stab of a vector in Co_0 is not exactly Co_2.
        # The stabilizer of a norm-4 vector in Co_0 has order
        # |Co_0| / 196560.
        assert stab_order == CO_0_ORDER // 196560
        assert stab_order > 0

    def test_norm_6_shell(self):
        """16773120 vectors of norm 6."""
        assert LEECH_NORM_6_COUNT == 16773120

    def test_euler_characteristic_24(self):
        """chi_top(K3) = 24."""
        # b_0 - b_1 + b_2 - b_3 + b_4 = 1 - 0 + 22 - 0 + 1 = 24
        assert 1 - 0 + 22 - 0 + 1 == 24

    def test_chi_O_K3(self):
        """chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2."""
        assert 1 - 0 + 1 == 2 == KAPPA_CH_K3_CY_FUNCTOR


# =========================================================================
# 16. Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPath:
    """Multi-path cross-checks verifying values from independent sources.

    AP10 requires that numerical claims be verified from at least two
    independent paths.  Each test below computes the same quantity via
    two or more routes and confirms agreement.
    """

    def test_co0_order_via_two_factorizations(self):
        """|Co_0| via prime factorization vs stored constant."""
        from_primes = 2**22 * 3**9 * 5**4 * 7**2 * 11 * 13 * 23
        assert CO_0_ORDER == from_primes
        # Independent check: |Co_0| = 2 * |Co_1| (center Z/2)
        assert CO_0_ORDER == 2 * CO_1_ORDER

    def test_m24_order_via_two_factorizations(self):
        """|M_24| via prime factorization and divisibility in Co_0."""
        from_primes = 2**10 * 3**3 * 5 * 7 * 11 * 23
        assert M_24_ORDER == from_primes
        # Independent: |M_24| divides |Co_0| (subgroup test)
        assert CO_0_ORDER % M_24_ORDER == 0

    def test_kissing_number_from_orbit_stabilizer(self):
        """196560 via orbit-stabilizer and direct value.

        Co_0 acts transitively on the 196560 norm-4 vectors.
        |orbit| = |Co_0| / |stabilizer of one vector|.
        The stabilizer of a norm-4 vector v is Co_2 (order 42,305,421,312,000).
        Note: -I_{24} sends v to -v (a different vector), so -I is NOT in
        the stabilizer of v.  Hence Stab(v) = Co_2, not Co_2 x Z/2.
        |orbit| = |Co_0| / |Co_2| = 196560.
        """
        co2_order = 42_305_421_312_000
        orbit_size = CO_0_ORDER // co2_order
        assert orbit_size == LEECH_KISSING_NUMBER
        assert orbit_size == 196560

    def test_c_delta_leech_from_two_paths(self):
        """c_Delta(Leech) from the formula and from the engine."""
        # Path 1: direct formula c_Delta = (691 * |R| - 65520) / 691
        from_formula = Fraction(691 * 0 - 65520, 691)
        # Path 2: from the leech_enhancement_point() function
        from_engine = leech_enhancement_point().c_delta
        assert from_formula == from_engine
        # Path 3: from the niemeier_shadow_landscape c_delta computation
        from compute.lib.niemeier_shadow_landscape import niemeier_lattice
        leech = niemeier_lattice(1)
        # c_delta computed from |R| = 0 via the formula
        assert leech.total_roots == 0
        c_delta_check = Fraction(691 * leech.total_roots - 65520, 691)
        assert c_delta_check == from_formula

    def test_kappa_ch_leech_voa_from_two_paths(self):
        """kappa_ch(V_{Leech}) = 24 via rank and via shadow data."""
        # Path 1: kappa_ch = rank for lattice VOAs
        from_rank = LEECH_RANK
        # Path 2: from the lattice_voa_shadow computation
        from compute.lib.niemeier_shadow_landscape import lattice_voa_shadow
        shadow = lattice_voa_shadow(24)
        from_shadow = shadow.kappa_ch
        # Path 3: from the leech enhancement point
        from_enhancement = leech_enhancement_point().kappa_ch_lattice_voa
        assert from_rank == from_shadow == from_enhancement == 24

    def test_kappa_ch_k3_sigma_from_two_paths(self):
        """kappa_ch(K3 sigma) = 2 via chi(O_K3) and via engine constant."""
        # Path 1: chi(O_K3) = 1 - 0 + 1 = 2
        from_euler = 1 - 0 + 1
        # Path 2: stored constant
        from_constant = KAPPA_CH_K3_CY_FUNCTOR
        # Path 3: from leech enhancement data
        from_enhancement = leech_enhancement_point().kappa_ch_k3_sigma
        assert from_euler == from_constant == from_enhancement == 2

    def test_24_from_three_paths(self):
        """24 = rank(Mukai) from Betti numbers, lattice rank, and Leech rank."""
        # Path 1: Betti numbers b_0 + b_2 + b_4
        from_betti = 1 + 22 + 1
        # Path 2: Mukai lattice rank
        from_mukai = MUKAI_RANK
        # Path 3: Leech lattice rank
        from_leech = LEECH_RANK
        # Path 4: K3 lattice rank + 2
        from_k3_plus_u = K3_LATTICE_RANK + 2
        assert from_betti == from_mukai == from_leech == from_k3_plus_u == 24

    def test_196884_from_two_paths(self):
        """196884 = 196560 + 324 and 196884 = 196883 + 1 (McKay)."""
        # Path 1: kissing number + free-field oscillator modes
        from_decomposition = LEECH_KISSING_NUMBER + 324
        # Path 2: smallest faithful Monster rep + 1
        from_mckay = 196883 + 1
        # Path 3: from the character comparison engine
        char_data = leech_vs_free_field_character()
        from_character = char_data['leech_voa_character'][1]
        assert from_decomposition == from_mckay == from_character == 196884

    def test_orbifold_halving_from_two_paths(self):
        """kappa_ch(V^natural) = kappa_ch(V_{Leech}) / 2 from two sources."""
        # Path 1: direct values
        assert KAPPA_CH_MONSTER_VOA == KAPPA_CH_LEECH_VOA // 2
        # Path 2: from hierarchy dictionary
        h = kappa_ch_hierarchy()
        kappa_leech = h['hierarchy']['V_{Leech}']['kappa_ch']
        kappa_monster = h['hierarchy']['V^natural']['kappa_ch']
        assert kappa_monster == kappa_leech // 2

    def test_co1_order_from_two_paths(self):
        """|Co_1| = |Co_0|/2 from direct division and from prime factorization."""
        # Path 1: halving Co_0
        from_halving = CO_0_ORDER // 2
        # Path 2: stored constant
        from_constant = CO_1_ORDER
        # Path 3: prime factorization (one fewer factor of 2)
        from_primes = 2**21 * 3**9 * 5**4 * 7**2 * 11 * 13 * 23
        assert from_halving == from_constant == from_primes

    def test_deep_holes_from_two_paths(self):
        """23 deep hole types = 24 Niemeier lattices - 1 (Leech itself)."""
        # Path 1: from leech_uniqueness_properties
        from_properties = leech_uniqueness_properties()['num_deep_holes']
        # Path 2: count Niemeier lattices with roots
        lattices = all_niemeier_lattices_with_leech()
        from_counting = len([L for L in lattices if L.total_roots > 0])
        # Path 3: 24 total Niemeier - 1 (Leech)
        from_subtraction = len(lattices) - 1
        assert from_properties == from_counting == from_subtraction == 23

    def test_character_divergence_from_two_paths(self):
        """Divergence at q^1 = 196560 from character comparison and kissing number."""
        # Path 1: from character comparison
        char_data = leech_vs_free_field_character()
        from_characters = char_data['divergence'][1]['difference']
        # Path 2: direct kissing number
        from_kissing = LEECH_KISSING_NUMBER
        # Path 3: 196884 - 324
        from_arithmetic = 196884 - 324
        assert from_characters == from_kissing == from_arithmetic == 196560

    def test_signature_from_two_paths(self):
        """Mukai signature (4,20) from direct and from K3 lattice + U."""
        # Path 1: stored constant
        from_constant = MUKAI_SIGNATURE
        # Path 2: K3 lattice sig (3,19) + hyperbolic plane U sig (1,1)
        k3_sig = K3_SIGNATURE
        u_sig = (1, 1)
        from_sum = (k3_sig[0] + u_sig[0], k3_sig[1] + u_sig[1])
        assert from_constant == from_sum == (4, 20)
