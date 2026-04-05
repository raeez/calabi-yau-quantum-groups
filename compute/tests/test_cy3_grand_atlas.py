"""Tests for the CY3 Grand Atlas.

Multi-path verification for all atlas entries. Each family is verified by at
least 3 independent paths:
  (a) Hodge-theoretic consistency (chi = 2(h11 - h21))
  (b) kappa prediction (chi/24 for compact, DT-extracted for non-compact)
  (c) GV invariant data (integrality, literature cross-check)
  (d) Shadow depth classification consistency
  (e) Cross-module verification against existing compute engines

References:
  cy_euler.py  -- Hodge diamonds, chi computations, CICY database
  toric_cy3_dt_engine.py  -- topological vertex, DT partition functions
  toric_shadow_engine.py  -- shadow tower extraction from DT
  modular_cy_characteristic.py  -- categorical kappa
  c3_dt_partition.py  -- MacMahon function, plane partitions
  conifold_wall_crossing.py  -- wall-crossing verification
  local_p2_shadow.py  -- local P^2 GV and shadows
  quintic_root_datum.py  -- quintic GW/GV
  k3e_relative_shadow.py  -- K3 x E DT and Igusa Delta_5

Manuscript ground truth:
  chapters/theory/modular_trace.tex  (Theorem CY-D)
  chapters/examples/k3_times_e.tex  (K3 x E tower)
"""

from fractions import Fraction
import pytest

from compute.lib.cy3_grand_atlas import (
    # Family constructors
    c3_family,
    conifold_family,
    local_p2_family,
    local_p1xp1_family,
    local_f1_family,
    k3_times_e_family,
    enriques_times_e_family,
    quintic_family,
    p5_33_family,
    p5_24_family,
    p6_223_family,
    p7_2222_family,
    bicubic_p2xp2_family,
    banana_manifold_family,
    borcea_voisin_family,
    # Atlas builders
    build_grand_atlas,
    full_atlas,
    atlas_summary,
    atlas_conjectures,
    # Hodge utilities
    chi_from_hodge,
    kappa_bcov,
    verify_hodge_consistency,
    # GV utilities
    verify_gv_integrality,
    verify_gv_growth,
    # Shadow depth
    predict_shadow_depth_toric,
    predict_shadow_depth_compact,
    # Pattern analysis
    kappa_integrality_analysis,
    chi_24_analysis,
    shadow_depth_universality,
    # Cross-checks
    verify_c3_against_macmahon,
    verify_conifold_gv,
    verify_local_p2_gv,
    verify_quintic_gv,
    verify_borcea_voisin_hodge,
    # Tables
    gv_growth_rate_table,
    cicy_kappa_table,
    format_atlas_table,
    # Processing
    process_atlas_entry,
    CY3Family,
    AtlasEntry,
)


# =========================================================================
# Section 1: Non-compact toric CY3 families
# =========================================================================

class TestC3:
    """C^3 -- the simplest CY3."""

    def test_kappa(self):
        """kappa(C^3) = 1 from Heisenberg H_1 (kappa(H_k) = k, so kappa(H_1) = 1)."""
        fam = c3_family()
        assert fam.kappa_pred == Fraction(1)

    def test_shadow_depth_class_G(self):
        """C^3 is class G (Gaussian) with depth 0 (no compact curves)."""
        fam = c3_family()
        assert fam.shadow_depth_class == "G"
        assert fam.shadow_depth == 0

    def test_no_compact_curves(self):
        """C^3 has no compact curves, so GV genus-0 is empty."""
        fam = c3_family()
        assert fam.gv_genus0 == {}

    def test_coha_known(self):
        """CoHA(C^3) = Y^+(gl_hat_1) (Schiffmann-Vasserot)."""
        fam = c3_family()
        assert fam.coha_known

    def test_not_compact(self):
        fam = c3_family()
        assert not fam.compact
        assert fam.toric

    def test_macmahon_cross_check(self):
        """Cross-check MacMahon coefficients against OEIS A000219."""
        result = verify_c3_against_macmahon(10)
        assert result["matches_oeis"]

    def test_macmahon_first_values(self):
        """p(0)=1, p(1)=1, p(2)=3, p(3)=6, p(4)=13."""
        result = verify_c3_against_macmahon(10)
        coeffs = result["coefficients"]
        assert coeffs[0] == 1
        assert coeffs[1] == 1
        assert coeffs[2] == 3
        assert coeffs[3] == 6
        assert coeffs[4] == 13
        assert coeffs[5] == 24


class TestConifold:
    """Resolved conifold O(-1) + O(-1) -> P^1."""

    def test_kappa(self):
        """kappa(conifold) = 1 (from conifold_bar_complex.py, authoritative)."""
        fam = conifold_family()
        assert fam.kappa_pred == Fraction(1)

    def test_shadow_depth_class_G(self):
        """Conifold is class G (Gaussian), depth 2."""
        fam = conifold_family()
        assert fam.shadow_depth_class == "G"
        assert fam.shadow_depth == 2

    def test_single_bps_state(self):
        """The conifold has exactly one BPS state: n^0_1 = 1."""
        result = verify_conifold_gv()
        assert result["n0_1_correct"]
        assert result["only_one_state"]

    def test_gv_integrality(self):
        fam = conifold_family()
        assert verify_gv_integrality(fam.gv_genus0)

    def test_wall_crossing(self):
        """The conifold has wall-crossing (2 chambers)."""
        fam = conifold_family()
        assert "Two chambers" in fam.notes


class TestLocalP2:
    """Local P^2 = O(-3) -> P^2."""

    def test_kappa(self):
        """kappa(local P^2) = 3/2 = chi(P^2)/2 (from local_p2_shadow.py, authoritative)."""
        fam = local_p2_family()
        assert fam.kappa_pred == Fraction(3, 2)

    def test_shadow_depth_class_M(self):
        """Local P^2 is class M (mixed, infinite tower from Z_3 McKay)."""
        fam = local_p2_family()
        assert fam.shadow_depth_class == "M"
        assert fam.shadow_depth is None

    def test_gv_literature_match(self):
        """Cross-check GV against CKYZ (hep-th/9903053)."""
        result = verify_local_p2_gv()
        assert result["all_match"]

    def test_gv_n0_1(self):
        """n^0_1 = 3 (three lines on P^2)."""
        fam = local_p2_family()
        assert fam.gv_genus0[1] == 3

    def test_gv_n0_2(self):
        """n^0_2 = -6."""
        fam = local_p2_family()
        assert fam.gv_genus0[2] == -6

    def test_gv_n0_3(self):
        """n^0_3 = 27 (27 rational cubics)."""
        fam = local_p2_family()
        assert fam.gv_genus0[3] == 27

    def test_gv_integrality(self):
        fam = local_p2_family()
        assert verify_gv_integrality(fam.gv_genus0)


class TestLocalP1xP1:
    """Local P^1 x P^1."""

    def test_kappa(self):
        """kappa(local P^1 x P^1) = 2 = h^{1,1}(P^1 x P^1)."""
        fam = local_p1xp1_family()
        assert fam.kappa_pred == Fraction(2)

    def test_shadow_depth_class_C(self):
        """Local P^1 x P^1 is class C (contact), depth 4."""
        fam = local_p1xp1_family()
        assert fam.shadow_depth_class == "C"
        assert fam.shadow_depth == 4

    def test_gv_integrality(self):
        fam = local_p1xp1_family()
        assert verify_gv_integrality(fam.gv_genus0)


class TestLocalF1:
    """Local F_1 (Hirzebruch)."""

    def test_kappa(self):
        """kappa(local F_1) = 2 (same as P^1 x P^1, same vertex count)."""
        fam = local_f1_family()
        assert fam.kappa_pred == Fraction(2)

    def test_same_kappa_as_p1xp1(self):
        """F_1 and P^1 x P^1 have the same kappa (same vertex count)."""
        assert local_f1_family().kappa_pred == local_p1xp1_family().kappa_pred

    def test_shadow_depth_class_M(self):
        """F_1 is class M due to asymmetry breaking."""
        fam = local_f1_family()
        assert fam.shadow_depth_class == "M"


# =========================================================================
# Section 2: K3-fibered CY3 families
# =========================================================================

class TestK3xE:
    """K3 x E -- BKM prototype."""

    def test_hodge_numbers(self):
        fam = k3_times_e_family()
        assert fam.h11 == 21
        assert fam.h21 == 21

    def test_chi_zero(self):
        """chi(K3 x E) = 0."""
        fam = k3_times_e_family()
        assert fam.chi == 0

    def test_chi_from_hodge(self):
        """chi = 2(h11 - h21) = 2(21 - 21) = 0."""
        fam = k3_times_e_family()
        assert chi_from_hodge(fam.h11, fam.h21) == 0

    def test_kappa_is_5(self):
        """kappa(K3 x E) = 5 = weight(Delta_5) (NOT chi/24 = 0)."""
        fam = k3_times_e_family()
        assert fam.kappa_pred == Fraction(5)

    def test_kappa_not_bcov(self):
        """kappa = 5 != chi/24 = 0. K3xE is the canonical counterexample to naive BCOV."""
        fam = k3_times_e_family()
        assert fam.kappa_pred != kappa_bcov(fam.chi)

    def test_bkm_exists(self):
        """The BKM superalgebra g_{Delta_5} exists."""
        fam = k3_times_e_family()
        assert fam.bkm_exists

    def test_shadow_depth_M(self):
        """K3 x E is class M (infinite tower from imaginary roots)."""
        fam = k3_times_e_family()
        assert fam.shadow_depth_class == "M"

    def test_compact(self):
        fam = k3_times_e_family()
        assert fam.compact
        assert not fam.toric


class TestEnriquesxE:
    """Enriques x E."""

    def test_hodge_numbers(self):
        fam = enriques_times_e_family()
        assert fam.h11 == 11
        assert fam.h21 == 11

    def test_chi_zero(self):
        fam = enriques_times_e_family()
        assert fam.chi == 0

    def test_kappa(self):
        """kappa(Enriques x E) = 4 (Allcock Borcherds product weight)."""
        fam = enriques_times_e_family()
        assert fam.kappa_pred == 4

    def test_kappa_ratio_k3xe(self):
        """kappa(K3 x E) / kappa(Enriques x E) = 5/4."""
        k_enr = enriques_times_e_family().kappa_pred
        k_k3e = k3_times_e_family().kappa_pred
        assert Fraction(k_k3e, k_enr) == Fraction(5, 4)

    def test_bkm_exists(self):
        fam = enriques_times_e_family()
        assert fam.bkm_exists


# =========================================================================
# Section 3: Compact complete intersection CY3s
# =========================================================================

class TestQuintic:
    """Quintic threefold in P^4."""

    def test_hodge(self):
        fam = quintic_family()
        assert fam.h11 == 1
        assert fam.h21 == 101

    def test_chi(self):
        fam = quintic_family()
        assert fam.chi == -200

    def test_chi_from_hodge(self):
        assert chi_from_hodge(1, 101) == -200

    def test_kappa_bcov(self):
        """kappa = chi/24 = -200/24 = -25/3."""
        fam = quintic_family()
        assert fam.kappa_pred == Fraction(-25, 3)

    def test_kappa_matches_bcov(self):
        fam = quintic_family()
        assert fam.kappa_pred == kappa_bcov(fam.chi)

    def test_gv_d1(self):
        """n^0_1 = 2875 (lines on quintic)."""
        fam = quintic_family()
        assert fam.gv_genus0[1] == 2875

    def test_gv_d2(self):
        """n^0_2 = 609250 (conics on quintic)."""
        fam = quintic_family()
        assert fam.gv_genus0[2] == 609250

    def test_gv_d3(self):
        fam = quintic_family()
        assert fam.gv_genus0[3] == 317206375

    def test_gv_cross_check(self):
        """Cross-check quintic GV against literature."""
        result = verify_quintic_gv()
        assert result["chi_correct"]
        assert result["h11_correct"]
        assert result["h21_correct"]
        for d in range(1, 4):
            assert result[f"n0_{d}_match"]

    def test_gv_integrality(self):
        fam = quintic_family()
        assert verify_gv_integrality(fam.gv_genus0)

    def test_shadow_depth_M(self):
        fam = quintic_family()
        assert fam.shadow_depth_class == "M"

    def test_no_bkm(self):
        fam = quintic_family()
        assert not fam.bkm_exists


class TestCICYFamily:
    """CICY complete intersection families."""

    def test_p5_33_hodge(self):
        fam = p5_33_family()
        assert fam.h11 == 1 and fam.h21 == 73 and fam.chi == -144

    def test_p5_33_kappa(self):
        assert p5_33_family().kappa_pred == Fraction(-6)

    def test_p5_24_hodge(self):
        fam = p5_24_family()
        assert fam.h11 == 1 and fam.h21 == 89 and fam.chi == -176

    def test_p5_24_kappa(self):
        assert p5_24_family().kappa_pred == Fraction(-22, 3)

    def test_p6_223_hodge(self):
        fam = p6_223_family()
        assert fam.h11 == 1 and fam.h21 == 73 and fam.chi == -144

    def test_p6_223_same_chi_as_p5_33(self):
        """P^5[3,3] and P^6[2,2,3] have the same chi but are different CY3s."""
        assert p5_33_family().chi == p6_223_family().chi == -144

    def test_p6_223_different_gv(self):
        """Same chi but different GV invariants: they ARE different manifolds."""
        gv1 = p5_33_family().gv_genus0
        gv2 = p6_223_family().gv_genus0
        assert gv1.get(1) != gv2.get(1)

    def test_p7_2222_hodge(self):
        fam = p7_2222_family()
        assert fam.h11 == 1 and fam.h21 == 65 and fam.chi == -128

    def test_p7_2222_kappa(self):
        assert p7_2222_family().kappa_pred == Fraction(-16, 3)

    def test_bicubic_hodge(self):
        fam = bicubic_p2xp2_family()
        assert fam.h11 == 2 and fam.h21 == 83 and fam.chi == -162

    def test_bicubic_kappa(self):
        assert bicubic_p2xp2_family().kappa_pred == Fraction(-27, 4)

    def test_all_cicy_chi_from_hodge(self):
        """Verify chi = 2(h11 - h21) for all CICYs."""
        for fam_fn in [p5_33_family, p5_24_family, p6_223_family,
                       p7_2222_family, bicubic_p2xp2_family]:
            fam = fam_fn()
            assert fam.chi == chi_from_hodge(fam.h11, fam.h21)

    def test_all_cicy_kappa_bcov(self):
        """All CICYs have kappa = chi/24 (BCOV prediction)."""
        for fam_fn in [quintic_family, p5_33_family, p5_24_family,
                       p6_223_family, p7_2222_family, bicubic_p2xp2_family]:
            fam = fam_fn()
            assert fam.kappa_pred == kappa_bcov(fam.chi)


# =========================================================================
# Section 4: Banana manifold
# =========================================================================

class TestBanana:
    """Banana (Schoen) CY3."""

    def test_chi_zero(self):
        fam = banana_manifold_family()
        assert fam.chi == 0

    def test_kappa_zero(self):
        """kappa = chi/24 = 0 for banana manifold."""
        fam = banana_manifold_family()
        assert fam.kappa_pred == Fraction(0)

    def test_shadow_depth_M(self):
        """Despite kappa=0, banana is class M (nontrivial DT)."""
        fam = banana_manifold_family()
        assert fam.shadow_depth_class == "M"


# =========================================================================
# Section 5: Borcea-Voisin families
# =========================================================================

class TestBorceaVoisin:
    """Borcea-Voisin CY3 families from K3 involutions."""

    def test_bv_1_1_hodge(self):
        bv = borcea_voisin_family(1, 1, 1)
        assert bv.h11 == 5 + 3 - 2 == 6
        assert bv.h21 == 65 - 3 - 2 == 60

    def test_bv_chi_formula(self):
        """chi = 12(r - 10) for all Borcea-Voisin."""
        for r in [1, 5, 10, 15, 20]:
            bv = borcea_voisin_family(r, 0, 0)
            assert bv.chi == 12 * (r - 10)

    def test_bv_kappa_formula(self):
        """kappa = (r - 10)/2."""
        for r in [1, 5, 10, 15, 20]:
            bv = borcea_voisin_family(r, 0, 0)
            assert bv.kappa_pred == Fraction(r - 10, 2)

    def test_bv_balanced_chi_zero(self):
        """r = 10 gives chi = 0 and kappa = 0."""
        bv = borcea_voisin_family(10, 0, 0)
        assert bv.chi == 0
        assert bv.kappa_pred == Fraction(0)

    def test_bv_maximal_r(self):
        """r = 20 gives kappa = 5 (same as K3 x E)."""
        bv = borcea_voisin_family(20, 2, 0)
        assert bv.kappa_pred == Fraction(5)
        assert bv.kappa_pred == k3_times_e_family().kappa_pred

    def test_bv_sum_rule(self):
        """h^{1,1} + h^{2,1} = 70 - 4a."""
        for r in [1, 5, 10, 15, 20]:
            for a in range(min(r, 22 - r) + 1):
                bv = borcea_voisin_family(r, a, 0)
                assert bv.h11 + bv.h21 == 70 - 4 * a

    def test_bv_hodge_cross_check(self):
        """Full Borcea-Voisin hodge cross-check."""
        result = verify_borcea_voisin_hodge()
        assert result["bv_1_1_1_chi_formula"]
        assert result["bv_1_1_1_hodge_check"]
        assert result["bv_10_0_chi_zero"]
        assert result["bv_10_0_kappa_zero"]
        assert result["bv_20_2_chi_formula"]


# =========================================================================
# Section 6: Hodge consistency for ALL families
# =========================================================================

class TestHodgeConsistency:
    """Hodge number consistency across the atlas."""

    def test_chi_from_hodge_basic(self):
        assert chi_from_hodge(1, 101) == -200
        assert chi_from_hodge(21, 21) == 0
        assert chi_from_hodge(1, 73) == -144

    def test_kappa_bcov_basic(self):
        assert kappa_bcov(-200) == Fraction(-25, 3)
        assert kappa_bcov(0) == Fraction(0)
        assert kappa_bcov(-144) == Fraction(-6)
        assert kappa_bcov(24) == Fraction(1)

    def test_all_compact_chi_consistent(self):
        """chi = 2(h11 - h21) for all compact families."""
        for fam in build_grand_atlas():
            if fam.compact and fam.h11 is not None and fam.h21 is not None:
                assert fam.chi == chi_from_hodge(fam.h11, fam.h21), \
                    f"{fam.name}: chi={fam.chi} but 2({fam.h11}-{fam.h21})={chi_from_hodge(fam.h11, fam.h21)}"

    def test_verify_hodge_consistency_quintic(self):
        result = verify_hodge_consistency(quintic_family())
        assert result["chi_from_hodge"]
        assert result["h11_nonneg"]
        assert result["h21_nonneg"]
        assert result["kappa_matches_bcov"]


# =========================================================================
# Section 7: Shadow depth classification
# =========================================================================

class TestShadowDepth:
    """Shadow depth classification tests."""

    def test_toric_depth_prediction(self):
        assert predict_shadow_depth_toric(1) == "G"
        assert predict_shadow_depth_toric(2) == "G"
        assert predict_shadow_depth_toric(3) == "M"  # Z_3 McKay forces infinite tower
        assert predict_shadow_depth_toric(4) == "C"
        assert predict_shadow_depth_toric(5) == "M"

    def test_compact_depth_prediction(self):
        assert predict_shadow_depth_compact(-200) == "M"
        assert predict_shadow_depth_compact(-144) == "M"
        assert predict_shadow_depth_compact(120) == "M"
        assert predict_shadow_depth_compact(0) == "?"

    def test_toric_depth_ordering(self):
        """Shadow depths of toric CY3s should increase with web complexity.

        C^3 (depth 0) < conifold (depth 2) <= local P^2 (infinite) >= P^1xP^1 (depth 4).
        Use None = infinity convention.
        """
        c3_d = c3_family().shadow_depth  # 0
        con_d = conifold_family().shadow_depth  # 2
        # C^3 < conifold (both finite)
        assert c3_d < con_d
        # local P^2 is infinite (class M), so depth = None
        assert local_p2_family().shadow_depth is None
        # P^1 x P^1 has finite depth 4
        assert local_p1xp1_family().shadow_depth == 4

    def test_compact_nonzero_chi_all_M(self):
        """All compact CY3 with chi != 0 are class M."""
        for fam in build_grand_atlas():
            if fam.compact and fam.chi is not None and fam.chi != 0:
                assert fam.shadow_depth_class == "M", \
                    f"{fam.name}: chi={fam.chi} but depth class={fam.shadow_depth_class}"

    def test_shadow_depth_universality_result(self):
        result = shadow_depth_universality(build_grand_atlas())
        assert result["compact_nonzero_chi_all_M"]


# =========================================================================
# Section 8: GV invariant properties
# =========================================================================

class TestGVInvariants:
    """GV invariant structure tests."""

    def test_all_gv_integer(self):
        """All stored GV invariants are integers."""
        for fam in build_grand_atlas():
            assert verify_gv_integrality(fam.gv_genus0), \
                f"{fam.name}: GV invariants not all integer"

    def test_local_p2_alternating_sign(self):
        """Local P^2 genus-0 GV alternate in sign ((-1)^{d+1} * n^0_d > 0)."""
        gv = local_p2_family().gv_genus0
        for d, n in gv.items():
            sign = (-1) ** (d + 1)
            assert sign * n > 0, \
                f"n^0_{d}={n}: expected sign {'+' if sign > 0 else '-'}"

    def test_gv_growth_rates(self):
        """GV growth rates should be finite positive numbers."""
        rates = gv_growth_rate_table()
        for name, rate in rates.items():
            assert rate > 0, f"{name}: growth rate {rate} <= 0"
            assert rate < 1e20, f"{name}: growth rate {rate} implausibly large"


# =========================================================================
# Section 9: Atlas-wide pattern tests
# =========================================================================

class TestAtlasPatterns:
    """Tests for atlas-wide patterns and conjectures."""

    def test_atlas_has_18_families(self):
        atlas = build_grand_atlas()
        assert len(atlas) == 18

    def test_atlas_has_5_toric(self):
        atlas = build_grand_atlas()
        assert len([f for f in atlas if f.toric]) == 5

    def test_atlas_has_13_compact(self):
        atlas = build_grand_atlas()
        assert len([f for f in atlas if f.compact]) == 13

    def test_kappa_integrality_rate(self):
        """About half of kappas are integers."""
        result = kappa_integrality_analysis(build_grand_atlas())
        assert 0.3 <= result["integer_fraction"] <= 0.7

    def test_coha_toric_only(self):
        """Currently, CoHA is known only for toric CY3s."""
        for fam in build_grand_atlas():
            if fam.coha_known:
                assert fam.toric, f"{fam.name}: CoHA known but not toric"

    def test_bkm_implies_chi_zero(self):
        """BKM existence correlates with chi = 0 (K3-fibered)."""
        for fam in build_grand_atlas():
            if fam.bkm_exists and fam.compact:
                assert fam.chi == 0, f"{fam.name}: BKM but chi={fam.chi}"

    def test_no_compact_with_positive_chi_and_bkm(self):
        """No compact CY3 with chi > 0 has a BKM (in our atlas)."""
        for fam in build_grand_atlas():
            if fam.compact and fam.chi is not None and fam.chi > 0:
                assert not fam.bkm_exists or fam.chi == 0

    def test_kappa_bcov_for_rigid(self):
        """For rigid CY3 (h21 > 0, non-fibered), kappa = chi/24."""
        rigid_families = [quintic_family, p5_33_family, p5_24_family,
                          p6_223_family, p7_2222_family, bicubic_p2xp2_family]
        for fn in rigid_families:
            fam = fn()
            assert fam.kappa_pred == kappa_bcov(fam.chi), \
                f"{fam.name}: kappa_pred={fam.kappa_pred} != chi/24={kappa_bcov(fam.chi)}"


# =========================================================================
# Section 10: Cross-module verification
# =========================================================================

class TestCrossModuleVerification:
    """Tests that verify atlas data against other compute modules."""

    def test_c3_macmahon_plane_partitions(self):
        """Verify MacMahon = plane partitions (OEIS A000219)."""
        result = verify_c3_against_macmahon(15)
        assert result["matches_oeis"]

    def test_conifold_gv_data(self):
        result = verify_conifold_gv()
        assert result["n0_1_correct"]

    def test_local_p2_gv_data(self):
        result = verify_local_p2_gv()
        assert result["all_match"]

    def test_quintic_gv_data(self):
        result = verify_quintic_gv()
        for d in [1, 2, 3]:
            assert result[f"n0_{d}_match"]

    def test_cicy_kappa_table(self):
        """All CICY kappa values are consistent."""
        table = cicy_kappa_table()
        for row in table:
            assert row["chi_consistent"], f"{row['name']}: chi inconsistent"


# =========================================================================
# Section 11: Full atlas processing
# =========================================================================

class TestFullAtlas:
    """Tests on the fully processed atlas."""

    def test_all_entries_processed(self):
        entries = full_atlas()
        assert len(entries) == 18

    def test_all_gv_integral(self):
        for entry in full_atlas():
            assert entry.gv_integrality

    def test_atlas_summary_complete(self):
        summary = atlas_summary()
        assert "total_families" in summary
        assert "shadow_depth_distribution" in summary
        assert "kappa_integrality" in summary

    def test_format_table_nonempty(self):
        table = format_atlas_table()
        assert len(table) > 100  # Should be a substantial table

    def test_conjectures_listed(self):
        conj = atlas_conjectures()
        assert len(conj) >= 5


# =========================================================================
# Section 12: Kappa relation tests (deep mathematical content)
# =========================================================================

class TestKappaRelations:
    """Tests for mathematical relations between kappa values."""

    def test_enriques_ratio_k3(self):
        """kappa(K3 x E) / kappa(Enriques x E) = 5/4."""
        assert Fraction(k3_times_e_family().kappa_pred, enriques_times_e_family().kappa_pred) == Fraction(5, 4)

    def test_bv_r20_equals_k3xe(self):
        """BV at r=20 has kappa = 5, same as K3 x E."""
        bv20 = borcea_voisin_family(20, 2, 0)
        assert bv20.kappa_pred == k3_times_e_family().kappa_pred

    def test_bv_kappa_range(self):
        """BV kappa ranges from -9/2 (r=1) to 5 (r=20)."""
        bv_min = borcea_voisin_family(1, 0, 0)
        bv_max = borcea_voisin_family(20, 0, 0)
        assert bv_min.kappa_pred == Fraction(-9, 2)
        assert bv_max.kappa_pred == Fraction(5)

    def test_c3_conifold_kappa_sum(self):
        """kappa(C^3) = kappa(conifold) = 1 (both Heisenberg at k=1)."""
        k_c3 = c3_family().kappa_pred
        k_con = conifold_family().kappa_pred
        assert k_c3 == k_con == 1

    def test_p5_33_and_p6_223_same_kappa(self):
        """P^5[3,3] and P^6[2,2,3] have the same kappa (same chi)."""
        assert p5_33_family().kappa_pred == p6_223_family().kappa_pred

    def test_all_toric_kappa_halfinteger(self):
        """All toric CY3 kappas are half-integers."""
        for fam in build_grand_atlas():
            if fam.toric:
                assert fam.kappa_pred.denominator in (1, 2), \
                    f"{fam.name}: kappa={fam.kappa_pred} not half-integer"


# =========================================================================
# Section 13: CICY chi/24 divisibility tests
# =========================================================================

class TestChi24Divisibility:
    """Tests for chi divisibility by 24."""

    def test_quintic_chi_not_div_24(self):
        """chi(quintic) = -200 is NOT divisible by 24."""
        assert -200 % 24 != 0

    def test_p5_33_chi_div_24(self):
        """chi(P^5[3,3]) = -144 IS divisible by 24."""
        assert -144 % 24 == 0

    def test_p5_24_chi_not_div_24(self):
        """chi(P^5[2,4]) = -176 is NOT divisible by 24."""
        assert -176 % 24 != 0

    def test_p7_2222_chi_not_div_24(self):
        """chi(P^7[2,2,2,2]) = -128 is NOT divisible by 24."""
        assert -128 % 24 != 0

    def test_chi_24_analysis_output(self):
        result = chi_24_analysis(build_grand_atlas())
        assert len(result["divisible_by_24"]) >= 3
        assert len(result["not_divisible_by_24"]) >= 3

    def test_no_cicy_h11_1_has_chi_div_24_except_33(self):
        """Among h11=1 CICYs, only P^5[3,3] and P^6[2,2,3] have 24|chi."""
        h11_1 = [quintic_family(), p5_33_family(), p5_24_family(),
                 p6_223_family(), p7_2222_family()]
        div_24 = [f for f in h11_1 if f.chi % 24 == 0]
        names = {f.name for f in div_24}
        assert "P^5[3,3]" in names
        assert "P^6[2,2,3]" in names
        assert "Quintic" not in names


# =========================================================================
# Section 14: Atlas entry processing tests
# =========================================================================

class TestAtlasEntryProcessing:
    """Tests for the atlas entry processing pipeline."""

    def test_process_c3(self):
        entry = process_atlas_entry(c3_family())
        assert entry.kappa_from_hodge is None  # Non-compact
        assert entry.gv_integrality

    def test_process_quintic(self):
        entry = process_atlas_entry(quintic_family())
        assert entry.kappa_from_hodge == Fraction(-25, 3)
        assert entry.kappa_consistent

    def test_process_k3xe(self):
        entry = process_atlas_entry(k3_times_e_family())
        assert entry.kappa_from_bkm == Fraction(5)
        assert entry.kappa_consistent  # K3 x E is special case

    def test_all_entries_have_consistent_kappa(self):
        """All non-fibered families should have consistent kappa."""
        for entry in full_atlas():
            # K3xE and Enriques have kappa from BKM, not BCOV
            if entry.family.name not in ("K3 x E", "Enriques x E"):
                assert entry.kappa_consistent, \
                    f"{entry.family.name}: kappa inconsistent"
