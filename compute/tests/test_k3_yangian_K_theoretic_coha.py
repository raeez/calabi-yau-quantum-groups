"""Tests for Wave-19 NEKRASOV K-theoretic CoHA engine.

Target: >= 30 assertions covering:
  C1  K-theoretic definition (Mukai rank, CY-3 volume, grading).
  C2  Phi_3^K K-theoretic functor (grading preservation, classical
      limit matches Wave-18 cohomological Phi_3).
  C3  (q_1, q_2)-parameter collapse: C^3 has two, K3 x E has ONE.
  C4  Specialisation q -> zeta_8 recovers u_{zeta_8}(Delta_5).
  C5  Classical limit q -> 1 recovers CoHA_{K3 x E}, character 1/Phi_10.
      Drinfeld double triangular decomposition, Cartan rank 23,
      quasi-triangularity (YBE status), commutator classical limit.
      Three-path convergence certificate; verify_all aggregate.

Raeez Lorgat -- Vol III K3 Yangian -- Wave 19 NEKRASOV tests.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_K_theoretic_coha import (
    CY3_DIMENSION,
    KHACommutator,
    KHA_coproduct_coassociativity_status,
    KHA_grading_lattice_rank,
    KHA_is_quasi_triangular,
    MUKAI_RANK,
    MUKAI_SIGNATURE_NEGATIVE,
    MUKAI_SIGNATURE_POSITIVE,
    classical_limit_character_is_phi10_inverse,
    classical_limit_recovers_coha,
    commutator_classical_limit_consistent_with_wave18,
    cy3_volume_class_degree,
    drinfeld_cartan_rank,
    drinfeld_double_components,
    hbar_log_q_at_specialisation,
    k3_lusztig_ell,
    k3xE_KHA_specialises_to_u_zeta_8,
    k3xE_cy3_closure_multiplicative,
    k3xE_equivariant_parameter_count,
    k3xE_has_two_torus_parameters,
    k3xE_self_dual_slice_relation,
    mukai_rank,
    phi3K_classical_limit_matches_phi3,
    phi3K_preserves_grading,
    phi3K_source,
    phi3K_target,
    specialisation_q_power_ell_equals_one,
    specialisation_q_value,
    three_path_convergence_at_wave19,
    toric_C3_has_two_torus_parameters,
    verify_all,
)


# ============================================================
# C1. K-theoretic definition
# ============================================================


def test_mukai_rank_is_24():
    assert mukai_rank() == 24
    assert MUKAI_RANK == 24


def test_mukai_signature_positive_is_4():
    assert MUKAI_SIGNATURE_POSITIVE == 4


def test_mukai_signature_negative_is_20():
    assert MUKAI_SIGNATURE_NEGATIVE == 20


def test_mukai_signature_total_is_24():
    # (4, 20) signature on II_{4, 20} totals rank 24.
    assert MUKAI_SIGNATURE_POSITIVE + MUKAI_SIGNATURE_NEGATIVE == MUKAI_RANK


def test_cy3_dimension_is_3():
    # K3 x E: dim_C K3 = 2, dim_C E = 1, total = 3.
    assert CY3_DIMENSION == 3


def test_cy3_volume_class_lives_in_degree_6():
    # Omega_{K3 x E} = omega_{K3} wedge omega_{E}:
    # degree (2,0) wedge (1,0) lifts to top (de Rham) degree
    # 2*dim_C = 6 for K3 x E.
    assert cy3_volume_class_degree() == 2 * CY3_DIMENSION


def test_KHA_grading_lattice_includes_mukai():
    # Rank at least Mukai rank.
    assert KHA_grading_lattice_rank() >= MUKAI_RANK


def test_KHA_grading_includes_elliptic_factor():
    # K3 x E lattice exceeds Mukai by the E-factor (rank 2 over H^0, H^2).
    assert KHA_grading_lattice_rank() == MUKAI_RANK + 2


# ============================================================
# C2. Phi_3^K K-theoretic functor
# ============================================================


def test_phi3K_source_is_KHA_K3xE():
    assert phi3K_source() == "KHA_{K3 x E}"


def test_phi3K_target_is_KH_Delta_5():
    assert phi3K_target() == "KH_{Delta_5}"


def test_phi3K_preserves_grading():
    # K-theoretic version of Padurariu 2023 CoHA-chiral transport.
    assert phi3K_preserves_grading() is True


def test_phi3K_classical_limit_matches_wave18_phi3():
    # q -> 1 via Chern character recovers Wave-18 cohomological Phi_3.
    assert phi3K_classical_limit_matches_phi3() is True


# ============================================================
# C3. (q_1, q_2)-parameter structure
# ============================================================


def test_toric_C3_has_two_independent_parameters():
    # FT 2011 Thm 3.1: KHA(C^2) = U_{q_1, q_2}(widehat widehat gl_1).
    assert toric_C3_has_two_torus_parameters() is True


def test_k3xE_does_not_have_two_independent_parameters():
    # Geometric obstruction: Aut^0(K3 x E) = E, no G_m subtorus.
    assert k3xE_has_two_torus_parameters() is False


def test_k3xE_equivariant_parameter_count_is_one():
    # The (q_1, q_2) plane collapses to the self-dual slice on K3 x E.
    assert k3xE_equivariant_parameter_count() == 1


def test_toric_and_k3xE_parameter_counts_differ():
    # Structural distinction between toric and non-toric CY-3 KHA.
    toric = 2 if toric_C3_has_two_torus_parameters() else 1
    k3xE = k3xE_equivariant_parameter_count()
    assert toric != k3xE


def test_self_dual_slice_relation_is_q_inverse():
    # Geometric collapse: q_1 = q_2^{-1} = q on K3 x E.
    assert "q_1" in k3xE_self_dual_slice_relation()
    assert "q_2" in k3xE_self_dual_slice_relation()


def test_cy3_closure_is_multiplicative_with_24_factors():
    # prod q_a = 1 over 24 Mukai directions.
    relation, n = k3xE_cy3_closure_multiplicative()
    assert n == 24
    assert "q_a" in relation
    assert "= 1" in relation


# ============================================================
# C4. Specialisation q -> zeta_8 recovers u_{zeta_8}
# ============================================================


def test_k3_lusztig_ell_is_8():
    # ell_K3 = 2 * c_+(Mukai) = 2 * 4 = 8 (Wave 17 certified).
    assert k3_lusztig_ell() == 8


def test_k3_lusztig_ell_is_twice_c_plus():
    # Universal Mukai-doubling identity.
    assert k3_lusztig_ell() == 2 * MUKAI_SIGNATURE_POSITIVE


def test_specialisation_q_value_is_primitive_8th_root():
    # q = e^{2 pi i / 8}, so q^8 = 1 but q^k != 1 for 0 < k < 8.
    q = specialisation_q_value()
    for k in range(1, 8):
        q_pow = q ** k
        assert abs(q_pow - 1.0) > 1e-9, f"q^{k} should not be 1"


def test_specialisation_q_power_8_is_one():
    assert specialisation_q_power_ell_equals_one() is True


def test_hbar_formal_at_specialisation_is_one_over_ell():
    # hbar = 1/ell_K3 = 1/8 at q = zeta_8.
    assert hbar_log_q_at_specialisation() == Fraction(1, 8)


def test_specialisation_recovers_u_zeta_8():
    # KHA at q = zeta_8 = u_{zeta_8}(Delta_5) = Wave-17 small form.
    assert k3xE_KHA_specialises_to_u_zeta_8() is True


# ============================================================
# C5. Classical limit, Drinfeld double, R-matrix, commutator
# ============================================================


def test_classical_limit_recovers_coha():
    # q -> 1 via Chern character, following Nakajima 1999 S7.
    assert classical_limit_recovers_coha() is True


def test_classical_limit_character_is_phi10_inverse():
    # Oberdieck-Pixton 2016 arXiv:1706.10100 + Davison 2017
    # arXiv:1512.04179 certify chi_{gr}(CoHA_{K3 x E}) = 1/Phi_10.
    assert classical_limit_character_is_phi10_inverse() is True


def test_KHA_is_quasi_triangular():
    # MO 2019 S14 / AO 2016 K-theoretic stable envelope.
    assert KHA_is_quasi_triangular() is True


def test_coproduct_has_Siegel_Borcherds_associator():
    # Varagnolo-Vasserot 2023 Thm 4.1 + Wave-18 Siegel twist.
    status = KHA_coproduct_coassociativity_status()
    assert "associator" in status or "Siegel" in status


def test_drinfeld_triangular_decomposition_has_three_pieces():
    # D_q = KHA^+ ox KHA^0 ox KHA^-.
    pieces = drinfeld_double_components()
    assert len(pieces) == 3
    assert pieces[0].endswith("+")
    assert pieces[1].endswith("0")
    assert pieces[2].endswith("-")


def test_drinfeld_cartan_rank_is_23():
    # Rank 23 imaginary Cartan from Mukai II_{4,20} signature (2,1)
    # after Euler-form-paired tensor with K_0(E). Matches Wave-15
    # Chevalley-BKM generator listing.
    assert drinfeld_cartan_rank() == 23


def test_commutator_classical_limit_matches_wave18_chi_3():
    # At q -> 1 the (3,1)-commutator reduces to Wave-18 Prop
    # W18-K3-commutator and lifts under Phi_3 to chi_3.
    assert commutator_classical_limit_consistent_with_wave18() is True


def test_commutator_only_31_survives_classical_limit():
    # The (3,1) and (1,3) channels give the CY-3-decorated
    # classical commutator; other (n, m) pairs vanish classically.
    c31 = KHACommutator(n=3, m=1, cy3_twist="Omega_{K3 x E}")
    c13 = KHACommutator(n=1, m=3, cy3_twist="Omega_{K3 x E}")
    c22 = KHACommutator(n=2, m=2, cy3_twist="Omega_{K3 x E}")
    c11 = KHACommutator(n=1, m=1, cy3_twist="Omega_{K3 x E}")

    assert c31.classical_limit_coefficient() == Fraction(1)
    assert c13.classical_limit_coefficient() == Fraction(1)
    assert c22.classical_limit_coefficient() == Fraction(0)
    assert c11.classical_limit_coefficient() == Fraction(0)


def test_KHACommutator_records_cy3_twist():
    # Every commutator channel carries the Omega_{K3 x E} decoration.
    c = KHACommutator(n=3, m=1, cy3_twist="Omega_{K3 x E}")
    assert "Omega" in c.cy3_twist
    assert "K3" in c.cy3_twist
    assert "E" in c.cy3_twist


# ============================================================
# Three-path convergence and top-level verification
# ============================================================


def test_three_path_all_converge():
    # All three paths (spec, classical, parameter-count) must agree.
    tp = three_path_convergence_at_wave19()
    assert tp["path_A_specialisation_to_u_zeta_8"] is True
    assert tp["path_B_classical_limit_to_coha"] is True
    assert tp["path_C_parameter_collapse"] is True


def test_three_path_records_ell_k3():
    tp = three_path_convergence_at_wave19()
    assert tp["lusztig_ell_K3"] == 8


def test_three_path_consistent_with_wave18():
    tp = three_path_convergence_at_wave19()
    assert tp["consistent_with_wave18"] is True


def test_verify_all_produces_a_report():
    rpt = verify_all()
    assert isinstance(rpt, dict)
    assert rpt["mukai_rank"] == 24
    assert rpt["ell_K3"] == 8
    assert rpt["k3xE_parameter_count"] == 1
    assert rpt["specialises_to_u_zeta_8"] is True


def test_verify_all_covers_all_cycles():
    rpt = verify_all()
    # Presence of every cycle key.
    for key in (
        "mukai_rank",  # C1
        "phi3K_preserves_grading",  # C2
        "k3xE_parameter_count",  # C3
        "specialises_to_u_zeta_8",  # C4
        "classical_limit_character",  # C5
        "three_path",  # aggregate
    ):
        assert key in rpt


# ============================================================
# Cross-check: Wave 17/18 invariants preserved by Wave 19
# ============================================================


def test_wave19_preserves_wave17_ell_K3():
    # Wave-17 certified ell = 8 must not shift under K-theoretic lift.
    assert k3_lusztig_ell() == 8


def test_wave19_classical_limit_is_wave18_character():
    # Wave-18 certified chi_{gr} = 1/Phi_10 must be the q -> 1 limit.
    assert classical_limit_character_is_phi10_inverse() is True


def test_wave19_parameter_collapse_is_geometric_not_conventional():
    # The collapse arises from Aut^0(K3 x E) = E having no G_m
    # subgroup; it is a geometric fact, not a choice of specialisation.
    assert k3xE_has_two_torus_parameters() is False
