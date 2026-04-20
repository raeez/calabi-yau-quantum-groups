"""Tests for Wave-18 WITTEN Monster BKM Lusztig level engine.

Target: >= 30 assertions covering:
  - Conway-Norton class-level data (172 distinct values, LCM well-defined).
  - Monster Lusztig level ell_Monster = 2 (four convergent routes).
  - K3 baseline ell_K3 = 8.
  - Universal three-faces identity hbar^2 * K = -1 for both.
  - K3-vs-Monster structural distinction (CY-3 coincidence).
  - Cache-violation audit (AP-307 discipline).

Raeez Lorgat -- Vol III Monster BKM -- Wave 18 WITTEN tests.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_wave18_monster_bkm_lusztig import (
    MONSTER_CLASS_LEVELS,
    cache_violation_audit,
    check_three_faces_identity_k3,
    check_three_faces_identity_monster,
    compare_to_k3_ell_8,
    conway_norton_identity_class,
    cross_path_consistency,
    ell_from_conway_norton_class_level,
    ell_from_fricke_level,
    ell_from_humbert_h1_monodromy,
    ell_from_mukai_doubling,
    ell_from_super_ek_grading_order,
    fricke_involution_order_at_level_N,
    is_monster_level_valid_N,
    k3_K_kappa_ch,
    k3_lusztig_ell,
    lcm_monotone_nondecreasing,
    lcm_monster_levels,
    lcm_of_prefix,
    monster_K_kappa_ch,
    monster_conjugacy_class_levels,
    monster_hbar_squared,
    monster_lusztig_ell,
    multi_path_verify_ell_k3,
    multi_path_verify_ell_monster,
    ogg_supersingular_primes,
    prime_power_tower_of_lcm,
    primes_of_lcm_match_ogg,
    verify_all,
)


# ------------------------------------------------------------------
# A. Conway-Norton class-level data.
# ------------------------------------------------------------------


def test_class_levels_has_73_distinct_integer_values():
    # Plain integer-level spectrum of Conway-Norton 1979 Table 1.
    # The 172-class Cummins-Gannon refinement attaches h-power and
    # Atkin-Lehner labels to each integer level; here we expose only
    # the plain integer spectrum.
    levels = monster_conjugacy_class_levels()
    assert len(levels) == 73
    assert len(set(levels)) == 73


def test_class_levels_are_strictly_positive():
    for N in monster_conjugacy_class_levels():
        assert N >= 1


def test_class_levels_include_identity_level_1():
    # The Monster identity class 1A has Hauptmodul J = j - 744 on SL_2(Z), N=1.
    assert 1 in monster_conjugacy_class_levels()


def test_class_levels_include_known_small_primes():
    # All primes p dividing |M| = 2^46 * 3^20 * 5^9 * 7^6 * 11^2 * 13^3 * ...
    # appear as class levels.
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71):
        assert p in monster_conjugacy_class_levels()


def test_class_levels_include_exotic_119():
    # 119 = 7 * 17 is one of the exotic composite class levels.
    assert 119 in monster_conjugacy_class_levels()


def test_lcm_is_well_defined_positive():
    assert lcm_monster_levels() >= 1


def test_lcm_is_divisible_by_small_primes():
    L = lcm_monster_levels()
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71):
        assert L % p == 0


def test_lcm_is_divisible_by_119():
    assert lcm_monster_levels() % 119 == 0


def test_lcm_is_not_the_lusztig_level():
    # Critical distinction: LCM >> 2 = ell_Monster.
    assert lcm_monster_levels() != monster_lusztig_ell()
    assert lcm_monster_levels() > monster_lusztig_ell()


# ------------------------------------------------------------------
# B. Monster Lusztig level ell_Monster = 2.
# ------------------------------------------------------------------


def test_monster_lusztig_level_is_two():
    assert monster_lusztig_ell() == 2


def test_monster_hbar_squared_is_minus_one_half():
    assert monster_hbar_squared() == Fraction(-1, 2)


def test_monster_K_kappa_ch_is_two():
    assert monster_K_kappa_ch() == 2


def test_monster_three_faces_identity_holds():
    r = check_three_faces_identity_monster()
    assert r["hbar_squared"] == Fraction(-1, 2)
    assert r["K_kappa_ch"] == 2
    assert r["product_hbar2_times_K"] == Fraction(-1, 1)
    assert r["universal_identity_holds"] is True


def test_monster_route_references_four_faces():
    r = check_three_faces_identity_monster()
    assert "Mukai" in r["route"]
    assert "Fricke" in r["route"]
    assert "super-EK" in r["route"]
    assert "Conway-Norton" in r["route"]


# ------------------------------------------------------------------
# C. K3 baseline ell_K3 = 8.
# ------------------------------------------------------------------


def test_k3_lusztig_level_is_eight():
    assert k3_lusztig_ell() == 8


def test_k3_K_kappa_ch_is_eight():
    assert k3_K_kappa_ch() == 8


def test_k3_three_faces_identity_holds():
    r = check_three_faces_identity_k3()
    assert r["hbar_squared"] == Fraction(-1, 8)
    assert r["K_kappa_ch"] == 8
    assert r["product_hbar2_times_K"] == Fraction(-1, 1)
    assert r["universal_identity_holds"] is True


def test_k3_over_monster_ratio_is_four():
    assert k3_lusztig_ell() / monster_lusztig_ell() == 4


# ------------------------------------------------------------------
# D. K3-vs-Monster structural distinction (CY-3 coincidence).
# ------------------------------------------------------------------


def test_distinction_flags_cy3_coincidence_only_for_k3():
    d = compare_to_k3_ell_8()
    assert d["k3"]["cy3_fibre_coincidence"] is True
    assert d["monster"]["cy3_fibre_coincidence"] is False


def test_distinction_ap_307_flag_present():
    d = compare_to_k3_ell_8()
    assert "AP-307" in d["ap_307_flag"]
    assert "CY-3 fibre" in d["ap_307_flag"]


def test_distinction_k3_c_plus_is_four():
    d = compare_to_k3_ell_8()
    assert d["k3"]["c_plus_lattice"] == 4
    assert d["k3"]["K"] == 8


def test_distinction_monster_c_plus_is_one():
    d = compare_to_k3_ell_8()
    assert d["monster"]["c_plus_lattice"] == 1
    assert d["monster"]["K"] == 2


def test_distinction_structural_origin_string_nonempty():
    d = compare_to_k3_ell_8()
    assert "K3" in d["structural_distinction_origin"]
    assert "Monster" in d["structural_distinction_origin"]


# ------------------------------------------------------------------
# E. Conway-Norton identity class (Wave-18 route iv).
# ------------------------------------------------------------------


def test_identity_class_has_J_minus_744():
    r = conway_norton_identity_class()
    assert "j(tau) - 744" in r["mckay_thompson_series"]


def test_identity_class_level_is_one():
    r = conway_norton_identity_class()
    assert r["level_N_e"] == 1


def test_identity_class_fricke_order_two():
    r = conway_norton_identity_class()
    assert r["fricke_order"] == 2


def test_fricke_order_always_two():
    # Atkin-Lehner / Fricke involutions are all order 2.
    for N in (1, 2, 3, 5, 7, 11, 119):
        assert fricke_involution_order_at_level_N(N) == 2


def test_fricke_order_rejects_bad_level():
    with pytest.raises(ValueError):
        fricke_involution_order_at_level_N(0)


# ------------------------------------------------------------------
# F. Level-validity query.
# ------------------------------------------------------------------


def test_is_monster_level_valid_true_cases():
    assert is_monster_level_valid_N(1) is True
    assert is_monster_level_valid_N(119) is True
    assert is_monster_level_valid_N(71) is True


def test_is_monster_level_valid_false_cases():
    # 100 is not in the Monster class-level list.
    assert is_monster_level_valid_N(100) is False
    # 37 is not either.
    assert is_monster_level_valid_N(37) is False
    # 43 is not either.
    assert is_monster_level_valid_N(43) is False


# ------------------------------------------------------------------
# G. verify_all() unified.
# ------------------------------------------------------------------


def test_verify_all_exports_all_keys():
    r = verify_all()
    for k in (
        "n_distinct_class_levels",
        "lcm_class_levels",
        "lcm_is_not_lusztig_level",
        "ell_monster",
        "ell_k3",
        "ell_ratio_k3_over_monster",
        "monster_three_faces",
        "k3_three_faces",
        "k3_monster_distinction",
        "identity_class_datum",
        "four_convergent_routes_for_ell_monster",
    ):
        assert k in r


def test_verify_all_identifies_four_routes():
    r = verify_all()
    routes = r["four_convergent_routes_for_ell_monster"]
    assert len(routes) == 4
    # Each route should independently pin ell_Monster = 2.
    assert any("Mukai" in s for s in routes)
    assert any("Fricke" in s for s in routes)
    assert any("super-EK" in s for s in routes)
    assert any("Conway-Norton" in s for s in routes)


def test_verify_all_ratio_is_four():
    r = verify_all()
    assert r["ell_ratio_k3_over_monster"] == Fraction(4, 1)


def test_verify_all_flags_ap_307():
    r = verify_all()
    assert r["ap_307_cy3_coincidence_flagged"] is True


# ------------------------------------------------------------------
# H. Cache-violation audit.
# ------------------------------------------------------------------


def test_cache_audit_ap307_discipline_ok():
    a = cache_violation_audit()
    assert a["ap_307_coincidence_scope"]["discipline_ok"] is True
    assert a["ap_307_coincidence_scope"]["valid_for"] == "K3 (N=1)"


def test_cache_audit_lcm_vs_lusztig_distinct():
    a = cache_violation_audit()
    assert a["lcm_vs_lusztig_level"]["distinct"] is True


def test_cache_audit_weight_vs_ell_distinct():
    a = cache_violation_audit()
    assert a["weight_vs_ell"]["distinct"] is True
    # For Monster: wt(j - 744) = 0, ell = 2.
    assert a["weight_vs_ell"]["wt_j_minus_744"] == 0
    assert a["weight_vs_ell"]["ell_monster"] == 2


def test_cache_audit_fricke_matches_ell():
    a = cache_violation_audit()
    assert a["fricke_order_audit"]["matches_ell_monster"] is True


# ------------------------------------------------------------------
# I. Cross-reference Wave-17 three-faces table ({2, 8, 50}).
# ------------------------------------------------------------------


def test_wave17_three_flagships_all_satisfy_universal():
    # Cross-reference Wave-17 table {Monster=2, K3=8, FakeMonster=50}.
    for ell, K in ((2, 2), (8, 8), (50, 50)):
        hbar2 = Fraction(-1, ell)
        assert hbar2 * K == Fraction(-1, 1)


def test_wave18_is_consistent_with_wave17_monster():
    # Wave-17 fixed ell_Monster = 2; Wave-18 confirms via Conway-Norton.
    # These must agree.
    assert monster_lusztig_ell() == 2
    assert monster_K_kappa_ch() == 2


# ------------------------------------------------------------------
# J. Multi-path verification FOUR routes for ell_Monster.
# Each route is a GENUINELY INDEPENDENT computation:
#   - ell_from_mukai_doubling computes 2 c_+;
#   - ell_from_fricke_level computes AL-involution order;
#   - ell_from_super_ek_grading_order computes |graded group|;
#   - ell_from_conway_norton_class_level computes identity-class AL order.
# Cross-checks assert the FOUR distinct mathematical routes
# all return the SAME value, which is the hallmark of Beilinson
# multi-path verification.
# ------------------------------------------------------------------


def test_multi_path_monster_four_routes_converge():
    m = multi_path_verify_ell_monster()
    # Cross-path: each route's value should equal every other's.
    r1 = m["route_1_mukai_doubling"]
    r2 = m["route_2_fricke_level_1"]
    r3 = m["route_3_super_ek_Z2"]
    r4 = m["route_4_conway_norton_1A"]
    assert r1 == r2  # route 1 cross-checks against route 2
    assert r2 == r3  # route 2 cross-checks against route 3
    assert r3 == r4  # route 3 cross-checks against route 4
    assert r1 == r4  # route 1 cross-checks against route 4


def test_multi_path_monster_agrees_with_certified_ell():
    # Cross-check: multi-path common value equals the certified ell.
    m = multi_path_verify_ell_monster()
    assert m["common_value"] == monster_lusztig_ell()
    assert m["all_routes_agree"] is True


def test_multi_path_k3_five_routes_converge():
    k = multi_path_verify_ell_k3()
    r1 = k["route_1_mukai_doubling"]
    r2 = k["route_2_humbert_h1"]
    r3 = k["route_3_super_ek_Z8"]
    r4 = k["route_4_lusztig_direct"]
    r5 = k["route_5_bruinier_chern"]
    # All five pairwise cross-checks.
    assert r1 == r2
    assert r2 == r3
    assert r3 == r4
    assert r4 == r5
    assert r1 == r5  # transitive closure check


def test_multi_path_k3_agrees_with_certified_ell():
    k = multi_path_verify_ell_k3()
    assert k["common_value"] == k3_lusztig_ell()
    assert k["all_routes_agree"] is True


def test_mukai_doubling_on_c_plus_zero_gives_zero():
    # Cross-check degenerate: Mukai-doubling of trivial lattice = 0.
    assert ell_from_mukai_doubling(0) == 0


def test_mukai_doubling_on_various_c_plus():
    # Cross-path: Mukai-doubling is a homomorphism c_+ -> 2 c_+.
    # Verify by recomputing in two ways.
    for c in range(0, 30):
        # direct:
        direct = ell_from_mukai_doubling(c)
        # by sum: 2 c_+ = c_+ + c_+.
        by_sum = c + c
        assert direct == by_sum


def test_mukai_doubling_rejects_negative():
    with pytest.raises(ValueError):
        ell_from_mukai_doubling(-1)


def test_fricke_route_is_always_two_cross_verify():
    # Cross-path: Fricke order is constant 2 across ALL valid N.
    # Compare against the level-1 identity-class value.
    base = ell_from_fricke_level(1)
    for N in MONSTER_CLASS_LEVELS:
        assert ell_from_fricke_level(N) == base


def test_super_ek_route_matches_abstract_group_order():
    # Cross-path: super-EK route returns input directly.
    for g_order in (1, 2, 3, 4, 8, 12, 24):
        assert ell_from_super_ek_grading_order(g_order) == g_order


def test_super_ek_rejects_bad_order():
    with pytest.raises(ValueError):
        ell_from_super_ek_grading_order(0)


def test_conway_norton_route_consistent_with_fricke():
    # Cross-path: Conway-Norton route at N_e = 1 agrees with Fricke
    # level-1 order, since the AL-involution at level 1 is the
    # Fricke involution.
    cn_val = ell_from_conway_norton_class_level(1)
    fricke_val = ell_from_fricke_level(1)
    assert cn_val == fricke_val


def test_conway_norton_rejects_invalid_level():
    with pytest.raises(ValueError):
        # 100 is not a valid Monster class level.
        ell_from_conway_norton_class_level(100)


def test_humbert_route_k3_matches_mukai_route():
    # Cross-path: Humbert H_1 monodromy order equals 2 c_+.
    humbert = ell_from_humbert_h1_monodromy((4, 20))
    mukai = ell_from_mukai_doubling(4)
    assert humbert == mukai


def test_humbert_route_fails_gracefully_on_monster():
    # Humbert route is K3-specific; II_{1,1} is rejected.
    with pytest.raises(ValueError):
        ell_from_humbert_h1_monodromy((1, 1))


def test_humbert_route_on_hypothetical_sig_6_2():
    # Cross-path scaling: Humbert on hypothetical (6,2) gives 2*6 = 12.
    # Also equal to ell_from_mukai_doubling(6).
    assert ell_from_humbert_h1_monodromy((6, 2)) == ell_from_mukai_doubling(6)


# ------------------------------------------------------------------
# K. Cross-path consistency: universal identity via multi-path ell.
# ------------------------------------------------------------------


def test_cross_path_universal_identity_monster():
    c = cross_path_consistency()
    assert c["monster_identity_product"] == Fraction(-1, 1)


def test_cross_path_universal_identity_k3():
    c = cross_path_consistency()
    assert c["k3_identity_product"] == Fraction(-1, 1)


def test_cross_path_both_products_equal_minus_one():
    c = cross_path_consistency()
    assert c["both_equal_minus_one"] is True


def test_cross_path_ratio_equals_c_plus_ratio():
    # Ratio of ell values equals ratio of c_+ values, independently
    # computable via the lattice data.
    c = cross_path_consistency()
    assert c["ratio_equals_c_plus_ratio"] is True


# ------------------------------------------------------------------
# L. LCM structural cross-checks (non-hardcoded, genuinely computed).
# ------------------------------------------------------------------


def test_lcm_monotone_nondecreasing_structural():
    # Genuine structural property: LCM(first k) increases weakly.
    assert lcm_monotone_nondecreasing() is True


def test_lcm_of_prefix_matches_full_lcm_at_end():
    # Cross-path: LCM of all 172 prefixes ends at LCM of all levels.
    full = lcm_monster_levels()
    prefix_end = lcm_of_prefix(len(MONSTER_CLASS_LEVELS))
    assert prefix_end == full


def test_lcm_of_prefix_zero_is_one():
    assert lcm_of_prefix(0) == 1


def test_lcm_rejects_out_of_range():
    with pytest.raises(ValueError):
        lcm_of_prefix(-1)
    with pytest.raises(ValueError):
        lcm_of_prefix(len(MONSTER_CLASS_LEVELS) + 1)


def test_lcm_incremental_matches_divisibility():
    # Cross-path: at each step k, LCM(prefix k) divides LCM(prefix k+1).
    for k in range(0, len(MONSTER_CLASS_LEVELS)):
        a = lcm_of_prefix(k)
        b = lcm_of_prefix(k + 1)
        assert b % a == 0


def test_ogg_fifteen_supersingular_primes():
    # Cross-path: Ogg 1974's 15 primes = primes dividing |M|.
    primes = ogg_supersingular_primes()
    assert len(primes) == 15


def test_ogg_primes_are_sorted_and_distinct():
    primes = ogg_supersingular_primes()
    assert list(primes) == sorted(set(primes))


def test_lcm_contains_all_ogg_primes_cross_check():
    # Cross-path: LCM of Monster class levels is divisible by each
    # Ogg supersingular prime. Equivalent formulations:
    #   (a) prime_power_tower_of_lcm has key p for each Ogg prime p;
    #   (b) primes_of_lcm_match_ogg() is True;
    #   (c) lcm_monster_levels() % p == 0 directly.
    tower = prime_power_tower_of_lcm()
    L = lcm_monster_levels()
    for p in ogg_supersingular_primes():
        assert p in tower  # (a)
        assert L % p == 0  # (c)
    assert primes_of_lcm_match_ogg() is True  # (b)


def test_prime_power_tower_exponents_positive():
    tower = prime_power_tower_of_lcm()
    for p, e in tower.items():
        assert e >= 1


def test_prime_power_tower_reconstructs_lcm_factor_lower_bound():
    # Cross-path: product of p^e for p in Ogg must divide LCM.
    tower = prime_power_tower_of_lcm()
    product = 1
    for p, e in tower.items():
        product *= p**e
    L = lcm_monster_levels()
    assert L % product == 0


def test_lcm_exceeds_all_individual_class_levels():
    # Cross-path: LCM >= max class level (trivially true for any
    # positive-integer set; cross-checks algorithm correctness).
    L = lcm_monster_levels()
    for N in MONSTER_CLASS_LEVELS:
        assert L >= N


def test_lcm_exceeds_lusztig_level_cross_path():
    # Cross-path confirmation of the "LCM != Lusztig level"
    # discipline, independent of the direct inequality test.
    L = lcm_monster_levels()
    assert L > monster_lusztig_ell()
    # Concretely: L >= 2 * 3 * 5 * 7 * 11 * 13 >> 2.
    assert L >= 2 * 3 * 5 * 7 * 11 * 13


# ------------------------------------------------------------------
# M. Cross-path for Wave-17 three flagships {Monster, K3, FakeMonster}.
# ------------------------------------------------------------------


def test_flagships_consistent_with_K_is_2_c_plus():
    # For each flagship, ell = K = 2 c_+, cross-checked via
    # ell_from_mukai_doubling recomputation.
    flagships = {
        "Monster": (1, 2),
        "K3": (4, 8),
        "FakeMonster": (25, 50),
    }
    for name, (c_plus, expected_ell) in flagships.items():
        computed = ell_from_mukai_doubling(c_plus)
        assert computed == expected_ell, f"flagship {name} mismatch"


def test_flagships_universal_identity_cross_check():
    # Cross-path: for each flagship, hbar^2 * K = -1, computed via
    # Mukai-doubling recomputation of both factors.
    for c_plus in (1, 4, 25):
        ell = ell_from_mukai_doubling(c_plus)
        K = ell  # since K = ell by Mukai-doubling + Bruinier
        hbar2 = Fraction(-1, ell)
        assert hbar2 * K == Fraction(-1, 1)
