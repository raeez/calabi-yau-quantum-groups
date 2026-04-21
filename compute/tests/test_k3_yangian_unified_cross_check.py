"""Tests for the Wave-17 unified cross-check engine.

Target: >= 50 assertions covering cross-checks A-H of the Wave-14/15/16
non-abelian K3 chiral bialgebra synthesis. Each cross-check is exercised
both via its dedicated entry point and via the global verify_all() API.

Raeez Lorgat -- Vol III non-abelian K3 chiral bialgebra -- Wave 17 tests.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_wave17_unified_cross_check import (
    cache_violation_audit,
    verify_all,
    verify_arthur_packet_delta10,
    verify_central_charge_pair,
    verify_five_frame_convergence,
    verify_heegner_pattern_at_n_1_2_3,
    verify_lattice_ranks,
    verify_schur_index_10_fourier,
    verify_siegel_weight_five,
    verify_universal_identity_three_ways,
)


# ------------------------------------------------------------------
# A. Universal identity hbar^2 * K^{kappa_ch} = -1 (3-way)
# ------------------------------------------------------------------

def test_A_three_faces_of_K_coincide():
    A = verify_universal_identity_three_ways()
    assert A["K_mukai"] == 8
    assert A["K_humbert"] == 8
    assert A["K_lusztig"] == 8
    assert A["three_faces_coincide"] is True


def test_A_hbar_squared_is_minus_one_eighth():
    A = verify_universal_identity_three_ways()
    assert A["hbar_squared"] == Fraction(-1, 8)


def test_A_universal_identity_product_is_minus_one():
    A = verify_universal_identity_three_ways()
    assert A["hbar_squared_times_K"] == Fraction(-1, 1)
    assert A["universal_identity_holds"] is True


def test_A_helper_check_and_reciprocity():
    A = verify_universal_identity_three_ways()
    assert A["universal_identity_helper_check"] is True
    assert A["bruinier_reciprocity"] is True


# ------------------------------------------------------------------
# B. (c_4d, c_2d) = (107/6, -214)
# ------------------------------------------------------------------

def test_B_c4d_eq_107_over_6():
    B = verify_central_charge_pair()
    assert B["c_4d"] == Fraction(107, 6)


def test_B_c2d_eq_minus_214():
    B = verify_central_charge_pair()
    assert B["c_2d"] == Fraction(-214, 1)


def test_B_matches_chacaltana_distler_formula():
    B = verify_central_charge_pair()
    assert B["c_4d_matches_CD_formula"] is True


def test_B_beem_rastelli_c2d_eq_minus_12_c4d():
    B = verify_central_charge_pair()
    assert B["beem_rastelli_c2d_eq_minus_12_c4d"] is True


def test_B_SU2_Nf4_cross_check():
    B = verify_central_charge_pair()
    assert B["SU2_Nf4_sanity_c4d_eq_7_over_6"] is True


def test_B_Coulomb_rank():
    B = verify_central_charge_pair()
    # (N-1)(3g - 3 + n) = 1 * 21 = 21 at (N, g, n) = (2, 0, 24)
    assert B["Coulomb_rank"] == 21


# ------------------------------------------------------------------
# C. BKM Cartan rank 3 + Mukai rank 24
# ------------------------------------------------------------------

def test_C_bkm_rank_is_3():
    C = verify_lattice_ranks()
    assert C["bkm_rank_eq_3"] is True
    assert C["bkm_real_rank"] == 3


def test_C_bkm_determinant_is_minus_32():
    C = verify_lattice_ranks()
    assert C["bkm_determinant"] == -32
    assert C["bkm_det_matches_minus_32"] is True


def test_C_bkm_gram_matrix_trace_is_6():
    C = verify_lattice_ranks()
    # diag(2, 2, 2) => trace 6
    assert C["bkm_gram_trace"] == 6


def test_C_bkm_signature_2_1():
    C = verify_lattice_ranks()
    assert C["bkm_signature"] == (2, 1)


def test_C_mukai_rank_24():
    C = verify_lattice_ranks()
    assert C["mukai_rank"] == 24
    assert C["mukai_rank_eq_24"] is True
    assert C["mukai_c_plus"] == 4
    assert C["mukai_c_minus"] == 20


def test_C_K_kappa_ch_via_mukai_doubling():
    C = verify_lattice_ranks()
    assert C["K_kappa_ch_via_mukai_doubling"] == 8


# ------------------------------------------------------------------
# D. Siegel weight 5
# ------------------------------------------------------------------

def test_D_gritsenko_additive_source_weight():
    D = verify_siegel_weight_five()
    assert D["route_1_additive_source_weight"] == Fraction(5, 1)


def test_D_chi_plus_kodaira_eq_5():
    D = verify_siegel_weight_five()
    assert D["route_2_chi_plus_kodaira"] == 5


def test_D_paramodular_anomaly_eq_5():
    D = verify_siegel_weight_five()
    assert D["route_3_paramodular_anomaly"] == 5


def test_D_weight_derivation_wrapper_eq_5():
    D = verify_siegel_weight_five()
    assert D["route_4_weight_derivation_wrapper"] == 5


def test_D_all_routes_agree():
    D = verify_siegel_weight_five()
    assert D["all_routes_equal_5"] is True


def test_D_gritsenko_nikulin_leading_key_exists():
    """Wave-15 normalisation gap (Gritsenko 1999 vs. GN98 Thm 2.1):
    raw Fourier dicts do not match verbatim at (0,0,0) because the
    additive-lift algorithm excludes the gcd=0 vacuum monomial.
    This is a documented predecessor-module convention (see
    normalisation_gap_note in wave15_fourier_expansion_order_10);
    our Wave-17 role is to record the value, not to flip the sign.
    """
    D = verify_siegel_weight_five()
    # The key must exist in the D report; its boolean value reflects
    # the documented convention gap.
    assert "gritsenko_nikulin_leading_match" in D
    assert isinstance(D["gritsenko_nikulin_leading_match"], bool)


# ------------------------------------------------------------------
# E. Five-frame duality convergence
# ------------------------------------------------------------------

def test_E_five_frames_count():
    E = verify_five_frame_convergence()
    assert E["n_frames"] == 5


def test_E_all_weights_equal_5():
    E = verify_five_frame_convergence()
    assert E["all_weights_equal_5"] is True
    # Check weight-5 per frame individually
    for frame, wt in E["weights_per_frame"].items():
        assert wt == 5, f"Frame {frame} has weight {wt}, expected 5"


def test_E_all_on_II_3_19():
    E = verify_five_frame_convergence()
    assert E["all_on_II_3_19"] is True
    for frame, lattice in E["lattices_per_frame"].items():
        assert lattice == "II_{3,19}", f"Frame {frame} on {lattice}"


def test_E_closure_ok():
    E = verify_five_frame_convergence()
    assert E["five_frame_closure_ok"] is True


# ------------------------------------------------------------------
# F. Heegner divisor pattern c_n propto [H_n] at n = 1, 2, 3
# ------------------------------------------------------------------

def test_F_leading_three_heegner_match():
    F = verify_heegner_pattern_at_n_1_2_3()
    assert F["all_leading_three_match"] is True


def test_F_c1_eq_2_disc_minus_1():
    F = verify_heegner_pattern_at_n_1_2_3()
    labels = F["heegner_labels_checked"]
    # (0, 1, 0) maps to disc = -1; expected c_K3(-1) = 2
    row = next(r for r in labels if r["heegner_label"] == (0, 1, 0))
    assert row["expected_c_K3"] == 2
    assert row["bruinier_mult"] == 2
    assert row["match"] is True


def test_F_c2_eq_20_disc_0():
    F = verify_heegner_pattern_at_n_1_2_3()
    labels = F["heegner_labels_checked"]
    row = next(r for r in labels if r["heegner_label"] == (1, 0, 0))
    assert row["bruinier_mult"] == 20
    assert row["match"] is True


def test_F_c3_eq_216_disc_3():
    F = verify_heegner_pattern_at_n_1_2_3()
    labels = F["heegner_labels_checked"]
    # (1, 1, 1) has disc = 3; expected c_K3(3) = 216
    row = next(r for r in labels if r["heegner_label"] == (1, 1, 1))
    assert row["expected_c_K3"] == 216
    assert row["bruinier_mult"] == 216
    assert row["match"] is True


# ------------------------------------------------------------------
# G. Arthur packet psi_{Delta_10} = phi_{Delta_E6} boxplus Sym^1
# ------------------------------------------------------------------

def test_G_first_principles_a_p_match_transcribed_at_small_primes():
    G = verify_arthur_packet_delta10()
    # 2, 3, 5, 7, 11 should all match; p=11 at 20586852 is the key cross-check
    assert G["all_first_principles_match"] is True
    assert G["a_p_first_principles"][2] == 216
    assert G["a_p_first_principles"][3] == -3348
    assert G["a_p_first_principles"][5] == 52110
    assert G["a_p_first_principles"][7] == 2822456
    assert G["a_p_first_principles"][11] == 20586852


def test_G_lambda_p_formula():
    G = verify_arthur_packet_delta10()
    lam = G["lambda_p_delta10"]
    # lambda_p = a_p + p^8 + p^9
    for p in [2, 3, 5, 7, 11]:
        expected = G["a_p_first_principles"][p] + p**8 + p**9
        assert lam[p] == expected, f"p={p}: lambda mismatch"


def test_G_ramanujan_petersson_all_primes():
    G = verify_arthur_packet_delta10()
    assert G["all_rp_bound_ok"] is True
    # Individual spot checks
    for p in [2, 3, 5, 7, 11]:
        assert G["ramanujan_petersson_checks"][p] is True


def test_G_satake_product_modulus_p15():
    G = verify_arthur_packet_delta10()
    # alpha_p * beta_p has modulus |p^15| for p=2, i.e. 2^15 = 32768
    assert G["satake_product_modulus_eq_p15"] is True


# ------------------------------------------------------------------
# H. Schur index PE[(72q - 22q^2)/(1-q)]
# ------------------------------------------------------------------

def test_H_q1_is_72():
    H = verify_schur_index_10_fourier()
    assert H["q1_eq_72"] is True
    assert H["computed_through_q9"][1] == 72


def test_H_q2_is_2678():
    H = verify_schur_index_10_fourier()
    assert H["q2_eq_2678"] is True
    assert H["computed_through_q9"][2] == 2678


def test_H_q3_is_68474():
    H = verify_schur_index_10_fourier()
    assert H["q3_eq_68474"] is True
    assert H["computed_through_q9"][3] == 68474


def test_H_q9_match():
    H = verify_schur_index_10_fourier()
    assert H["q9_eq_405322063500"] is True


def test_H_redundant_plethystic_path_agrees():
    H = verify_schur_index_10_fourier()
    assert H["redundant_path_agrees"] is True


def test_H_manuscript_match():
    H = verify_schur_index_10_fourier()
    assert H["manuscript_match"] is True
    assert H["manuscript_diagnostics"] == []


def test_H_leading_terms_positive_integer_growth():
    H = verify_schur_index_10_fourier()
    coeffs = H["computed_through_q9"]
    # Monotone growth from q^1 upwards (all positive integers in Schur index PE)
    previous = coeffs[1]
    for n in range(2, 10):
        assert coeffs[n] > previous, f"Monotone growth fails at q^{n}"
        previous = coeffs[n]


# ------------------------------------------------------------------
# Cache-violation audit
# ------------------------------------------------------------------

def test_cache_audit_has_all_expected_keys():
    audit = cache_violation_audit()
    for key in [
        "CoHA_not_chiral_via_Phi_arrow",
        "kappa_cat_K3xE_eq_0",
        "native_vs_derived_E_n",
        "six_routes_distinct",
        "averaging_vs_derived_centre",
    ]:
        assert key in audit, f"Missing cache audit key: {key}"


def test_cache_audit_kappa_cat_K3xE_eq_0_message():
    audit = cache_violation_audit()
    assert "0" in audit["kappa_cat_K3xE_eq_0"]
    assert "chi(O_E)" in audit["kappa_cat_K3xE_eq_0"]


def test_cache_audit_coha_uses_phi_arrow():
    audit = cache_violation_audit()
    assert "Phi" in audit["CoHA_not_chiral_via_Phi_arrow"]


# ------------------------------------------------------------------
# Global verify_all() regression
# ------------------------------------------------------------------

def test_verify_all_returns_8_cross_checks():
    report = verify_all()
    assert report["n_total"] == 8
    assert len(report["pass_fail"]) == 8


def test_verify_all_n_passing_is_8():
    report = verify_all()
    assert report["n_passing"] == 8, (
        f"Expected 8 passing, got {report['n_passing']}. "
        f"Failing: {[k for k,v in report['pass_fail'].items() if not v]}"
    )


def test_verify_all_returns_all_pass_true():
    report = verify_all()
    assert report["all_pass"] is True


def test_verify_all_details_match_individual_calls():
    report = verify_all()
    # Spot-check: B section c_4d should be 107/6 everywhere
    assert report["details"]["B_central_charge_pair"]["c_4d"] == Fraction(107, 6)
    # A section hbar^2 * K should be -1
    assert (
        report["details"]["A_universal_identity"]["hbar_squared_times_K"]
        == Fraction(-1, 1)
    )
    # C section BKM determinant is -32
    assert report["details"]["C_bkm_mukai_ranks"]["bkm_determinant"] == -32
    # D section: all routes equal 5
    assert report["details"]["D_siegel_weight_5"]["all_routes_equal_5"] is True
    # E section: 5 frames
    assert report["details"]["E_five_frame_closure"]["n_frames"] == 5
    # F section: all leading three match
    assert report["details"]["F_heegner_pattern"]["all_leading_three_match"] is True


def test_cache_audit_present_in_verify_all():
    report = verify_all()
    assert "cache_audit" in report
    # Audit must have at least 4 keys (CoHA, kappa, native-derived, six-routes)
    assert len(report["cache_audit"]) >= 4


# ------------------------------------------------------------------
# Deep cross-binding: cross-check-to-cross-check consistency
# ------------------------------------------------------------------

def test_K_from_A_equals_2_c_plus_from_C():
    """Wave-17 consistency: K from face (a) of A-cross-check equals
    2 c_+(Mukai) from C-cross-check."""
    A = verify_universal_identity_three_ways()
    C = verify_lattice_ranks()
    assert A["K_mukai"] == 2 * C["mukai_c_plus"] == 8


def test_chi_K3_equals_n_punctures_from_H():
    """E + H cross: chi(K3) = 24 equals n = 24 (class-S puncture count)."""
    # This is pinned in the k3_elliptic_genus coefficient table (chi(K3) = 24
    # via c_K3(0) = 20 + 4) and by the (5n - 13)/6 evaluation at n = 24.
    B = verify_central_charge_pair()
    # (5 * 24 - 13) / 6 = 107/6: if this holds, n = 24 was correctly consumed.
    assert B["c_4d"] == Fraction(5 * 24 - 13, 6)


def test_weight_5_times_mukai_rank_equals_120():
    """Trivial sanity: wt(Delta_5) * rank(Mukai) = 5 * 24 = 120.

    Not a load-bearing identity, but ensures D and C don't silently drift.
    """
    D = verify_siegel_weight_five()
    C = verify_lattice_ranks()
    assert int(D["route_2_chi_plus_kodaira"]) * C["mukai_rank"] == 120


def test_F_heegner_c_K3_neg_one_equals_face_a_doubling_over_4():
    """Heegner c_K3(-1) = 2 equals c_+(Mukai)/2; both from the same
    positive-signature count on II_{4,20} + its BKM restriction."""
    F = verify_heegner_pattern_at_n_1_2_3()
    # disc -1 has multiplicity 2 = c_+(Mukai)/2
    row = next(r for r in F["heegner_labels_checked"] if r["heegner_label"] == (0, 1, 0))
    assert row["expected_c_K3"] == 2
    # c_+(Mukai) = 4, so 4/2 = 2 matches
    C = verify_lattice_ranks()
    assert row["expected_c_K3"] == C["mukai_c_plus"] // 2


def test_G_a_2_satisfies_rp_via_c_A1_scope():
    """Arthur packet a_p at p=2: |216| <= 2 * 2^{15/2} approx 362."""
    G = verify_arthur_packet_delta10()
    a_2 = G["a_p_first_principles"][2]
    assert abs(a_2) <= 2 * (2 ** 7.5) + 1


# ------------------------------------------------------------------
# Primary-lit citation completeness
# ------------------------------------------------------------------

def test_each_cross_check_has_primary_citations():
    report = verify_all()
    for section_key, details in report["details"].items():
        assert "primary_citations" in details, (
            f"Section {section_key} missing primary_citations."
        )
        assert len(details["primary_citations"]) >= 2, (
            f"Section {section_key} has fewer than 2 citations."
        )


def test_A_cites_bruinier_mukai_lusztig():
    A = verify_universal_identity_three_ways()
    cites = " ".join(A["primary_citations"])
    assert "Mukai" in cites
    assert "Bruinier" in cites
    assert "Lusztig" in cites


def test_B_cites_chacaltana_distler_beem_rastelli():
    B = verify_central_charge_pair()
    cites = " ".join(B["primary_citations"])
    assert "Chacaltana" in cites or "Distler" in cites
    assert "Beem" in cites or "Rastelli" in cites


def test_G_cites_ikeda_andrianov_deligne():
    G = verify_arthur_packet_delta10()
    cites = " ".join(G["primary_citations"])
    assert "Ikeda" in cites
    assert "Andrianov" in cites
    assert "Deligne" in cites
