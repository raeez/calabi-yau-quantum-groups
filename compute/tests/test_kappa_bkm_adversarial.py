r"""
Tests for kappa_bkm_adversarial.py -- adversarial investigation of the
Heisenberg-fibre equality kappa_BKM = kappa_ch^{Heis} + chi(O_fiber).

SUMMARY OF FINDINGS
====================

The equality kappa_BKM = kappa_ch^{Heis} + chi(O_{fiber}) is a numerical
coincidence for K3 x E (N=1).  It FAILS for all Z/NZ-orbifolds with
N >= 2.  The correct universal formula is the Borcherds weight formula:
kappa_BKM = c(0)/2.

These tests verify:
1. The Heisenberg-fibre coincidence holds for N=1 (K3 x E) only.
2. Explicit counterexamples at N=2 (Enriques) and N=3 (symplectic Z/3).
3. The Borcherds weight formula c(0)/2 holds universally.
4. The quintic has no BKM algebra.
5. The DMVV square root is consistent.
6. The delta pattern (kappa_BKM - kappa_ch) analysis.
7. The verdict: coincidence, not universal additive decomposition.
"""

import sys
import os
from fractions import Fraction

import pytest

# Import the engine
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from kappa_bkm_adversarial import (
    CHL_LITERAL_ADDITIVE_TABLE,
    CHL_LEVELS,
    ORBIFOLD_KAPPA_TABLE,
    chl_bkm_constants,
    count_literal_additive_split_failures,
    count_literal_additive_split_successes,
    literal_additive_split_all_chl_levels,
    literal_additive_split_success_rate,
    orbifold_kappa,
    heis_fiber_coincidence_all_N,
    test_decomposition_all_N as _lib_test_decomposition_all_N,
    count_heis_fiber_coincidence_successes,
    count_decomposition_successes,
    heis_fiber_coincidence_success_rate,
    decomposition_success_rate,
    fiber_vs_total_space,
    explicit_counterexample_N3,
    explicit_counterexample_N2,
    quintic_has_no_bkm,
    dmvv_square_root,
    c0_decomposition,
    c0_is_universal,
    second_quantization_correction,
    delta_pattern,
    effective_correction_formula,
    verdict,
    run_full_adversarial_analysis,
)


# =========================================================================
# 1. TABLE INTEGRITY
# =========================================================================

class TestTableIntegrity:
    """Verify the orbifold kappa table is self-consistent."""

    def test_table_has_eight_entries(self):
        assert len(ORBIFOLD_KAPPA_TABLE) == 8

    def test_all_N_present(self):
        for N in range(1, 9):
            assert N in ORBIFOLD_KAPPA_TABLE

    def test_borcherds_weight_formula(self):
        """kappa_BKM = c_N(0)/2 for all N (THEOREM, Borcherds 1998)."""
        for N in range(1, 9):
            d = ORBIFOLD_KAPPA_TABLE[N]
            assert d.kappa_BKM == d.c_N_0 // 2, (
                f"N={N}: kappa_BKM={d.kappa_BKM} != c(0)/2={d.c_N_0//2}"
            )

    def test_kappa_cat_total_vanishes(self):
        """chi(O_{CY3}) = 0 for all CY3 (h^{0,q} = (1,1,1,1) or similar)."""
        for N in range(1, 9):
            d = ORBIFOLD_KAPPA_TABLE[N]
            assert d.kappa_cat_total == 0

    def test_c_N_0_values(self):
        """Verify the literature c_N(0) values."""
        expected = {1: 10, 2: 8, 3: 6, 4: 4, 5: 4, 6: 2, 7: 2, 8: 2}
        for N, c0 in expected.items():
            assert ORBIFOLD_KAPPA_TABLE[N].c_N_0 == c0

    def test_kappa_BKM_values(self):
        """Verify the Borcherds weights."""
        expected = {1: 5, 2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1}
        for N, k in expected.items():
            assert ORBIFOLD_KAPPA_TABLE[N].kappa_BKM == k

    def test_kappa_BKM_monotone_decreasing(self):
        """kappa_BKM is weakly decreasing in N."""
        vals = [ORBIFOLD_KAPPA_TABLE[N].kappa_BKM for N in range(1, 9)]
        assert all(vals[i] >= vals[i+1] for i in range(len(vals)-1))

    def test_kappa_ch_values(self):
        """kappa_ch = 3 for N=1,3..8 (K3 fiber), 2 for N=2 (Enriques)."""
        expected_ch = {1: 3, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3}
        for N, k in expected_ch.items():
            assert ORBIFOLD_KAPPA_TABLE[N].kappa_ch == k

    def test_chi_O_fiber_values(self):
        """chi(O_S) = 2 for K3 (N=1,3..8), 1 for Enriques (N=2)."""
        expected_chi = {1: 2, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2}
        for N, c in expected_chi.items():
            assert ORBIFOLD_KAPPA_TABLE[N].kappa_cat_fiber == c


# =========================================================================
# 2. LITERAL CHL ADDITIVE-SPLIT TESTS
# =========================================================================

class TestLiteralCHLAdditiveSplit:
    """Test the literal split kappa_BKM = kappa_ch + chi(O_fiber)."""

    def test_chl_levels_are_programme_active(self):
        assert CHL_LEVELS == (1, 2, 3, 4, 6)

    def test_chl_bkm_constants(self):
        """Exact constants: kappa_BKM(Phi_N)=c_N(0)/2 on the square-root
        CHL ladder (Jatkar--Sen / Govindarajan--Krishna); N=4 half-integral."""
        expected = {
            1: {"c_N_0": 10, "kappa_BKM": 5},
            2: {"c_N_0": 6, "kappa_BKM": 3},
            3: {"c_N_0": 4, "kappa_BKM": 2},
            4: {"c_N_0": 3, "kappa_BKM": Fraction(3, 2)},
            6: {"c_N_0": 2, "kappa_BKM": 1},
        }
        assert chl_bkm_constants() == expected
        for N, row in expected.items():
            assert row["kappa_BKM"] == Fraction(row["c_N_0"], 2)

    def test_literal_split_has_zero_successes(self):
        """The literal additive split fails at every CHL level."""
        assert count_literal_additive_split_successes() == 0
        assert count_literal_additive_split_failures() == 5
        assert literal_additive_split_success_rate() == Fraction(0, 1)

    def test_literal_split_failure_flags_all_levels(self):
        results = literal_additive_split_all_chl_levels()
        assert set(results) == set(CHL_LEVELS)
        for N, row in results.items():
            assert not row["additive_identity_holds"], f"N={N} should fail"

    def test_exact_rhs_values_where_reconstructed(self):
        """Exact RHS values currently reconstructed for N=1,2 only."""
        assert CHL_LITERAL_ADDITIVE_TABLE[1].additive_rhs == 0
        assert CHL_LITERAL_ADDITIVE_TABLE[2].additive_rhs == 1
        assert CHL_LITERAL_ADDITIVE_TABLE[1].kappa_BKM != 0
        assert CHL_LITERAL_ADDITIVE_TABLE[2].kappa_BKM != 1

    def test_N3_N4_N6_not_guessed(self):
        """The oracle records N=3,4,6 failure status without inventing RHS
        values.  The pre-correction N=3 cache RHS (=2) was computed against
        the retracted ladder; it numerically coincides with the corrected
        kappa_BKM = 2 and is deliberately absent rather than misread as the
        identity holding."""
        assert CHL_LITERAL_ADDITIVE_TABLE[3].additive_rhs is None
        assert CHL_LITERAL_ADDITIVE_TABLE[4].additive_rhs is None
        assert CHL_LITERAL_ADDITIVE_TABLE[6].additive_rhs is None
        assert CHL_LITERAL_ADDITIVE_TABLE[4].kappa_BKM == Fraction(3, 2)
        assert "exact RHS not reconstructed" in CHL_LITERAL_ADDITIVE_TABLE[4].source_status
        assert "exact RHS not reconstructed" in CHL_LITERAL_ADDITIVE_TABLE[6].source_status


# =========================================================================
# 3. HEISENBERG-FIBRE COINCIDENCE TESTS
# =========================================================================

class TestHeisFiberCoincidence:
    """Test the N=1 equality, not a theorem-level BKM decomposition."""

    def test_heis_fiber_coincidence_holds_only_for_N1(self):
        """The Heisenberg-fibre equality holds ONLY for N=1 (K3 x E)."""
        results = heis_fiber_coincidence_all_N()
        for N, r in results.items():
            if N == 1:
                assert r["heis_fiber_coincidence_holds"], (
                    "N=1 should satisfy the Heisenberg-fibre coincidence"
                )
            else:
                assert not r["heis_fiber_coincidence_holds"], (
                    f"N={N} should FAIL the Heisenberg-fibre equality, "
                    f"but got kappa_BKM={r['kappa_BKM']} == "
                    f"predicted={r['predicted']}"
                )

    def test_exactly_one_success(self):
        """Only 1 of 8 orbifolds satisfies the Heisenberg-fibre equality."""
        assert count_heis_fiber_coincidence_successes() == 1

    def test_success_rate_is_one_eighth(self):
        """Success rate = 1/8."""
        assert heis_fiber_coincidence_success_rate() == Fraction(1, 8)

    def test_legacy_decomposition_holds_access_is_alias_only(self):
        """Legacy access remains available but names only the N=1 coincidence."""
        d = ORBIFOLD_KAPPA_TABLE[1]
        assert d.heis_fiber_coincidence_holds is True
        assert d.decomposition_holds is d.heis_fiber_coincidence_holds
        assert "heis_fiber_coincidence_holds" in d._fields
        assert "decomposition_holds" not in d._fields

        canonical = heis_fiber_coincidence_all_N()
        legacy = _lib_test_decomposition_all_N()
        assert legacy == canonical
        assert (
            count_decomposition_successes()
            == count_heis_fiber_coincidence_successes()
        )
        assert (
            decomposition_success_rate()
            == heis_fiber_coincidence_success_rate()
        )

    def test_N1_specific_values(self):
        """N=1: kappa_BKM=5 = kappa_ch^{Heis}(3) + chi(O_{K3})(2)."""
        d = ORBIFOLD_KAPPA_TABLE[1]
        assert d.kappa_BKM == 5
        assert d.kappa_ch == 3
        assert d.kappa_cat_fiber == 2
        assert d.kappa_BKM == d.kappa_ch + d.kappa_cat_fiber
        assert d.heis_fiber_coincidence_holds

    def test_deficit_N2(self):
        """N=2 (Enriques): deficit = +1."""
        d = ORBIFOLD_KAPPA_TABLE[2]
        assert d.decomposition_deficit == 1

    def test_deficit_N3(self):
        """N=3: deficit = -2."""
        d = ORBIFOLD_KAPPA_TABLE[3]
        assert d.decomposition_deficit == -2

    def test_all_deficits(self):
        """Verify all decomposition deficits."""
        expected_deficit = {
            1: 0, 2: 1, 3: -2, 4: -3, 5: -3, 6: -4, 7: -4, 8: -4,
        }
        for N, exp in expected_deficit.items():
            d = ORBIFOLD_KAPPA_TABLE[N]
            assert d.decomposition_deficit == exp, (
                f"N={N}: deficit={d.decomposition_deficit}, expected={exp}"
            )


# =========================================================================
# 3. COUNTEREXAMPLE TESTS
# =========================================================================

class TestCounterexamples:
    """Test the explicit counterexamples."""

    def test_N3_counterexample(self):
        """N=3: kappa_BKM=3, predicted=5, deficit=-2."""
        r = explicit_counterexample_N3()
        assert r["kappa_BKM"] == 3
        assert r["predicted_by_decomposition"] == 5
        assert r["actual"] == 3
        assert not r["heis_fiber_coincidence_holds"]
        assert not r["decomposition_holds"]
        assert r["deficit"] == -2
        assert r["frame_shape"] == {1: 6, 3: 6}

    def test_N2_counterexample(self):
        """N=2 (Enriques): kappa_BKM=4, predicted=3, deficit=+1."""
        r = explicit_counterexample_N2()
        assert r["kappa_BKM"] == 4
        assert r["predicted_by_decomposition"] == 3
        assert r["actual"] == 4
        assert not r["heis_fiber_coincidence_holds"]
        assert not r["decomposition_holds"]
        assert r["deficit"] == 1
        assert r["chi_O_Enr"] == 1

    def test_quintic_has_no_bkm(self):
        """The quintic has no BKM algebra, so decomposition is inapplicable."""
        r = quintic_has_no_bkm()
        assert r["kappa_BKM"] is None
        assert not r["decomposition_applicable"]
        assert r["kappa_ch"] == Fraction(-25, 3)
        assert r["kappa_cat"] == 0

    def test_N3_crepant_resolution_is_K3(self):
        """For N>=3, crepant resolution is K3, so chi(O_S)=2 is unchanged."""
        for N in range(3, 9):
            d = ORBIFOLD_KAPPA_TABLE[N]
            assert d.kappa_cat_fiber == 2, (
                f"N={N}: chi(O_S)={d.kappa_cat_fiber}, expected 2 (K3)"
            )

    def test_N3_kappa_ch_unchanged(self):
        """For N>=3, kappa_ch = 3 (same as K3 x E, since resolution is K3)."""
        for N in range(3, 9):
            d = ORBIFOLD_KAPPA_TABLE[N]
            assert d.kappa_ch == 3


# =========================================================================
# 4. FIBER vs TOTAL SPACE
# =========================================================================

class TestFiberVsTotalSpace:
    """Test the fiber vs total space analysis."""

    def test_total_space_chi_vanishes(self):
        """chi(O_{K3 x E}) = 0."""
        r = fiber_vs_total_space()
        assert r["total_space_chi"] == 0

    def test_fiber_chi_is_two(self):
        """chi(O_{K3}) = 2."""
        r = fiber_vs_total_space()
        assert r["fiber_chi"] == 2

    def test_total_space_fails(self):
        """Using chi(O_{K3 x E}) = 0 gives 3 + 0 = 3 != 5."""
        r = fiber_vs_total_space()
        assert not r["total_space_predicts_correctly"]
        assert r["with_total_space"] == 3

    def test_fiber_works_for_N1(self):
        """Using chi(O_{K3}) = 2 gives 3 + 2 = 5 = kappa_BKM. (N=1 only.)"""
        r = fiber_vs_total_space()
        assert r["fiber_predicts_correctly"]
        assert r["with_fiber"] == 5


# =========================================================================
# 5. BORCHERDS WEIGHT FORMULA (UNIVERSAL)
# =========================================================================

class TestBorcherdsUniversal:
    """Test that kappa_BKM = c(0)/2 holds universally."""

    def test_c0_is_universal(self):
        """The Borcherds weight formula holds for all eight orbifolds."""
        assert c0_is_universal()

    def test_c0_decomposition_all_hold(self):
        """Verify c_N(0)/2 = kappa_BKM for each N individually."""
        results = c0_decomposition()
        for N, r in results.items():
            assert r["borcherds_formula_holds"], (
                f"N={N}: c(0)/2 formula fails"
            )


# =========================================================================
# 6. DMVV SQUARE ROOT
# =========================================================================

class TestDMVV:
    """Test the DMVV formula and square root structure."""

    def test_phi10_weight(self):
        r = dmvv_square_root()
        assert r["weight_Phi10"] == 10

    def test_delta5_weight(self):
        r = dmvv_square_root()
        assert r["weight_Delta5"] == 5

    def test_phi10_equals_delta5_squared(self):
        r = dmvv_square_root()
        assert r["Phi10_equals_Delta5_squared"]

    def test_kappa_BKM_is_delta5(self):
        r = dmvv_square_root()
        assert r["kappa_BKM_is_Delta5_weight"]
        assert r["kappa_BKM_not_Phi10_weight"]


# =========================================================================
# 7. DELTA PATTERN
# =========================================================================

class TestDeltaPattern:
    """Test the delta = kappa_BKM - kappa_ch pattern."""

    def test_N1_delta_is_chi_O_K3(self):
        """N=1: delta = 5 - 3 = 2 = chi(O_{K3})."""
        dp = delta_pattern()
        assert dp["N1_delta_is_chi_O_K3"]

    def test_N2_delta_is_chi_O_K3_not_Enr(self):
        """N=2: delta = 4 - 2 = 2 = chi(O_{K3}), NOT chi(O_{Enr})=1."""
        dp = delta_pattern()
        assert dp["N2_delta_is_chi_O_K3"]
        assert dp["N2_delta_is_NOT_chi_O_Enr"]

    def test_N3_delta_zero(self):
        """N=3: delta = 3 - 3 = 0."""
        dp = delta_pattern()
        assert dp["N3_delta_zero"]

    def test_negative_deltas_exist(self):
        """N >= 4 have negative deltas."""
        dp = delta_pattern()
        assert len(dp["negative_deltas"]) > 0
        assert 4 in dp["negative_deltas"]

    def test_delta_values(self):
        """Verify all delta values."""
        sq = second_quantization_correction()
        expected_delta = {1: 2, 2: 2, 3: 0, 4: -1, 5: -1, 6: -2, 7: -2, 8: -2}
        for N, exp in expected_delta.items():
            assert sq[N]["delta"] == exp, (
                f"N={N}: delta={sq[N]['delta']}, expected={exp}"
            )


# =========================================================================
# 8. VERDICT
# =========================================================================

class TestVerdict:
    """Test the final verdict."""

    def test_literal_split_zero_successes(self):
        v = verdict()
        assert v["literal_additive_split_successes"] == 0
        assert v["literal_additive_split_failures"] == 5

    def test_exactly_one_success(self):
        v = verdict()
        assert v["successes"] == 1

    def test_is_coincidence(self):
        v = verdict()
        assert v["is_coincidence"]

    def test_not_universal(self):
        v = verdict()
        assert not v["is_universal"]

    def test_seven_failures(self):
        v = verdict()
        assert len(v["failures"]) == 7

    def test_correct_formula_is_borcherds(self):
        v = verdict()
        assert "c(0)/2" in v["correct_universal_formula"]

    def test_manuscript_correctly_conjectural(self):
        v = verdict()
        assert "conjectural" in v["manuscript_status"]


# =========================================================================
# 9. FULL ANALYSIS
# =========================================================================

class TestFullAnalysis:
    """Test the complete adversarial analysis pipeline."""

    def test_full_analysis_runs(self):
        """The full analysis completes without error."""
        results = run_full_adversarial_analysis(verbose=False)
        assert "verdict" in results
        assert "decomposition_test" in results
        assert "counterexample_N3" in results
        assert "counterexample_N2" in results
        assert "c0_holds_universally" in results

    def test_full_analysis_verdict(self):
        results = run_full_adversarial_analysis(verbose=False)
        assert results["verdict"]["is_coincidence"]
        assert results["c0_holds_universally"]


# =========================================================================
# 10. MULTI-PATH CROSS-CHECKS WITH EXISTING ENGINES (AP10)
# =========================================================================

class TestCrossChecksMultiPath:
    """Multi-path verification against diagonal_siegel_cy_orbifolds.py and
    kappa_spectrum_reconciliation.py.

    AP10 compliance: every numerical assertion in this engine is
    cross-checked against at least one independent computation path
    from an existing engine.
    """

    # --- Path A: diagonal_siegel_cy_orbifolds.py ---

    def test_kappa_BKM_vs_diagonal_siegel_all_N(self):
        """Cross-check kappa_BKM against diagonal_siegel_cy_orbifolds.kappa_bkm."""
        from diagonal_siegel_cy_orbifolds import kappa_bkm as ds_kappa_bkm
        for N in range(1, 9):
            ours = ORBIFOLD_KAPPA_TABLE[N].kappa_BKM
            theirs = ds_kappa_bkm(N)
            assert ours == theirs, (
                f"N={N}: adversarial kappa_BKM={ours} != "
                f"diagonal_siegel kappa_bkm={theirs}"
            )

    def test_c_N_0_vs_diagonal_siegel_all_N(self):
        """Cross-check c_N(0) against diagonal_siegel FRAME_SHAPE_DATA."""
        from diagonal_siegel_cy_orbifolds import FRAME_SHAPE_DATA
        for N in range(1, 9):
            ours = ORBIFOLD_KAPPA_TABLE[N].c_N_0
            theirs = FRAME_SHAPE_DATA[N].c_disc_0
            assert ours == theirs, (
                f"N={N}: adversarial c_N(0)={ours} != "
                f"FRAME_SHAPE_DATA c_disc_0={theirs}"
            )

    def test_borcherds_weight_vs_diagonal_siegel_all_N(self):
        """Cross-check Borcherds weight = c_N(0)/2 via diagonal_siegel."""
        from diagonal_siegel_cy_orbifolds import (
            borcherds_weight as ds_weight,
            c_disc_0 as ds_c0,
        )
        for N in range(1, 9):
            w = ds_weight(N)
            c0 = ds_c0(N)
            assert w == c0 // 2, (
                f"N={N}: diagonal_siegel weight={w} != c(0)/2={c0//2}"
            )
            assert ORBIFOLD_KAPPA_TABLE[N].kappa_BKM == w

    def test_kappa_spectrum_vs_diagonal_siegel_all_N(self):
        """Cross-check Heisenberg, total-space, and fibre kappas against diagonal_siegel."""
        from diagonal_siegel_cy_orbifolds import kappa_spectrum as ds_spec
        for N in range(1, 9):
            ours = ORBIFOLD_KAPPA_TABLE[N]
            theirs = ds_spec(N)
            assert ours.kappa_ch == theirs['kappa_ch_Heis'], (
                f"N={N}: kappa_ch_Heis mismatch: {ours.kappa_ch} vs {theirs['kappa_ch_Heis']}"
            )
            assert ours.kappa_cat_total == theirs['kappa_cat_total_space'], (
                f"N={N}: total kappa_cat mismatch: {ours.kappa_cat_total} vs {theirs['kappa_cat_total_space']}"
            )
            assert ours.kappa_cat_fiber == theirs['kappa_cat_fiber'], (
                f"N={N}: fibre kappa_cat mismatch: {ours.kappa_cat_fiber} vs {theirs['kappa_cat_fiber']}"
            )

    # --- Path B: kappa_spectrum_reconciliation.py ---

    def test_k3xe_kappa_ch_vs_reconciliation(self):
        """Cross-check kappa_ch(K3 x E) against kappa_spectrum_reconciliation."""
        from kappa_spectrum_reconciliation import (
            kappa_ch as recon_kappa_ch,
            k3_times_e,
        )
        k3e = k3_times_e()
        assert ORBIFOLD_KAPPA_TABLE[1].kappa_ch == recon_kappa_ch(k3e)

    def test_k3xe_kappa_BKM_vs_reconciliation(self):
        """Cross-check kappa_BKM(K3 x E) against kappa_spectrum_reconciliation."""
        from kappa_spectrum_reconciliation import (
            kappa_BKM as recon_kappa_BKM,
            k3_times_e,
        )
        k3e = k3_times_e()
        assert ORBIFOLD_KAPPA_TABLE[1].kappa_BKM == recon_kappa_BKM(k3e)

    def test_k3xe_chi_O_fiber_vs_reconciliation(self):
        """Cross-check chi(O_{K3}) against kappa_spectrum_reconciliation."""
        from kappa_spectrum_reconciliation import (
            kappa_cat as recon_kappa_cat,
            k3_surface,
        )
        k3 = k3_surface()
        assert ORBIFOLD_KAPPA_TABLE[1].kappa_cat_fiber == recon_kappa_cat(k3)

    def test_k3xe_decomposition_vs_reconciliation(self):
        """Cross-check canonical failure and N=1 Heisenberg-fibre coincidence."""
        from kappa_spectrum_reconciliation import verify_BKM_decomposition_k3e
        recon = verify_BKM_decomposition_k3e()
        assert not recon["decomposition_holds"]
        assert (
            recon["heis_fiber_coincidence_holds"]
            == ORBIFOLD_KAPPA_TABLE[1].heis_fiber_coincidence_holds
        )
        assert recon["kappa_ch_K3xE"] == ORBIFOLD_KAPPA_TABLE[1].kappa_ch
        assert recon["kappa_BKM_K3xE"] == ORBIFOLD_KAPPA_TABLE[1].kappa_BKM
        assert recon["kappa_cat_K3"] == ORBIFOLD_KAPPA_TABLE[1].kappa_cat_fiber

    def test_k3_chi_O_vs_reconciliation_hodge(self):
        """Cross-check chi(O_{K3}) via Hodge data from reconciliation."""
        from kappa_spectrum_reconciliation import k3_surface
        k3 = k3_surface()
        # chi(O_{K3}) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 1 = 2
        assert k3.chi_O() == 2
        assert k3.chi_O() == ORBIFOLD_KAPPA_TABLE[1].kappa_cat_fiber

    def test_enriques_chi_O_vs_reconciliation(self):
        """Cross-check chi(O_{Enr}) via reconciliation Hodge data."""
        from kappa_spectrum_reconciliation import enriques_surface
        enr = enriques_surface()
        assert enr.chi_O() == 1
        assert enr.chi_O() == ORBIFOLD_KAPPA_TABLE[2].kappa_cat_fiber

    def test_k3xe_chi_O_total_vs_reconciliation(self):
        """Cross-check chi(O_{K3xE}) = 0 via reconciliation."""
        from kappa_spectrum_reconciliation import k3_times_e
        k3e = k3_times_e()
        assert k3e.chi_O() == 0
        assert k3e.chi_O() == ORBIFOLD_KAPPA_TABLE[1].kappa_cat_total

    # --- Path C: borcherds_denominator_phi10_engine.py ---

    def test_kappa_BKM_vs_borcherds_denominator(self):
        """Cross-check kappa_BKM=5 against borcherds_denominator_phi10_engine."""
        from borcherds_denominator_phi10_engine import bkm_data
        bkm = bkm_data()
        assert bkm['kappa_BKM'] == 5
        assert bkm['kappa_BKM'] == ORBIFOLD_KAPPA_TABLE[1].kappa_BKM

    def test_weight_delta5_vs_borcherds_denominator(self):
        """Cross-check wt(Delta_5)=5 against borcherds_denominator engine."""
        from borcherds_denominator_phi10_engine import bkm_data
        bkm = bkm_data()
        assert bkm['weight_denominator'] == 5
        assert bkm['weight_chi10'] == 10
        assert bkm['weight_chi10'] == 2 * bkm['weight_denominator']

    # --- Path D: borcherds_lift.py ---

    def test_c0_10_vs_borcherds_lift(self):
        """Cross-check c(0)=10 for phi_{0,1} against borcherds_lift."""
        from borcherds_lift import phi01_c_table, borcherds_lift_weight
        c_table = phi01_c_table(20)
        assert c_table[0] == 10
        assert borcherds_lift_weight(c_table) == 5.0
        assert ORBIFOLD_KAPPA_TABLE[1].c_N_0 == 10

    # --- Path E: bkm_chiral_algebra.py ---

    def test_lattice_voa_central_charge(self):
        """Cross-check c=3 for V_{Lambda^{2,1}_{II}}^{formal} against bkm_chiral_algebra."""
        from bkm_chiral_algebra import LATTICE_VOA_CENTRAL_CHARGE
        assert LATTICE_VOA_CENTRAL_CHARGE == 3

    # --- Consistency across ALL paths ---

    def test_all_five_paths_agree_on_kappa_BKM_K3xE(self):
        """Five independent paths all give kappa_BKM(K3 x E) = 5."""
        from diagonal_siegel_cy_orbifolds import kappa_bkm as ds_kappa
        from kappa_spectrum_reconciliation import kappa_BKM as recon_kappa, k3_times_e
        from borcherds_denominator_phi10_engine import bkm_data
        from borcherds_lift import phi01_c_table, borcherds_lift_weight

        path_A = ds_kappa(1)
        path_B = recon_kappa(k3_times_e())
        path_C = bkm_data()['kappa_BKM']
        path_D = int(borcherds_lift_weight(phi01_c_table(20)))
        path_E = ORBIFOLD_KAPPA_TABLE[1].kappa_BKM

        assert path_A == path_B == path_C == path_D == path_E == 5, (
            f"Five-path disagreement: A={path_A}, B={path_B}, "
            f"C={path_C}, D={path_D}, E={path_E}"
        )

    def test_orbifold_kappa_function(self):
        """The orbifold_kappa(N) function returns correct data."""
        d = orbifold_kappa(1)
        assert d.N == 1
        assert d.kappa_BKM == 5
        assert d.heis_fiber_coincidence_holds
        assert d.decomposition_holds

    def test_orbifold_kappa_out_of_range(self):
        """orbifold_kappa raises for N outside 1..8."""
        with pytest.raises(ValueError):
            orbifold_kappa(0)
        with pytest.raises(ValueError):
            orbifold_kappa(9)
