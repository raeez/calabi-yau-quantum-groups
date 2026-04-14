"""Tests for Wilson lines as stratified factorization homology defects.

Verifies:
  1. Stratified defect classification (codim 0-3 hierarchy)
  2. Excision coproduct = Drinfeld coproduct (Wilson line collision)
  3. Triple excision coherence (spectral coassociativity, axiom H4)
  4. FH holonomy braiding at E_1, E_2, E_3 levels
  5. FH unitarity and YBE from holonomy
  6. Wilson surface defect data and categorical S-matrix
  7. Surface/line hierarchy consistency
  8. Axiom dictionary (H1)--(H5) completeness
  9. Cross-engine consistency with wilson_line_coproduct_engine
 10. Miki exchange from FH holonomy
 11. Normal bundle spectral parameter counting
 12. E_n level of defect computation

Test count: 54 tests across 10 suites.
"""

import numpy as np
import pytest

from compute.lib.wilson_stratified_fh import (
    AxiomDictionaryFH,
    StratifiedDefectData,
    TripleWilsonLineExcision,
    WilsonLineBraidingFH,
    WilsonLineCollisionExcision,
    WilsonSurfaceDefect,
)


# ===================================================================
# Suite 1: Stratified defect classification
# ===================================================================

class TestStratifiedDefectData:
    """Verify the defect classification table for C^3."""

    def test_codim0_bulk(self):
        d = StratifiedDefectData.get_defect_data(0)
        assert d["name"] == "bulk"
        assert d["en_level"] == 3
        assert d["spectral_params"] == 0

    def test_codim1_surface(self):
        d = StratifiedDefectData.get_defect_data(1)
        assert d["name"] == "Wilson surface"
        assert d["en_level"] == 2
        assert d["spectral_params"] == 1
        assert d["complex_codim"] == 1

    def test_codim2_line(self):
        d = StratifiedDefectData.get_defect_data(2)
        assert d["name"] == "Wilson line"
        assert d["en_level"] == 1
        assert d["spectral_params"] == 2
        assert d["complex_codim"] == 2

    def test_codim3_point(self):
        d = StratifiedDefectData.get_defect_data(3)
        assert d["name"] == "point operator"
        assert d["en_level"] == 0
        assert d["spectral_params"] == 3

    def test_invalid_codim(self):
        with pytest.raises(ValueError):
            StratifiedDefectData.get_defect_data(4)

    def test_normal_bundle_rank(self):
        """N_{C/C^3} = C^2, rank 2."""
        assert StratifiedDefectData.normal_bundle_rank(3, 1) == 2

    def test_normal_bundle_rank_surface(self):
        """N_{S/C^3} = C, rank 1."""
        assert StratifiedDefectData.normal_bundle_rank(3, 2) == 1

    def test_can_braid_lines_in_c3(self):
        """Wilson lines (real dim 2) can cross in C^3 (real dim 6)."""
        assert StratifiedDefectData.can_braid(6, 2) is True

    def test_cannot_braid_lines_in_c1(self):
        """Wilson lines cannot cross in C (real dim 2): codim < 2."""
        assert StratifiedDefectData.can_braid(2, 1) is False

    def test_can_braid_in_c2(self):
        """Wilson lines (real dim 2) can cross in C^2 (real dim 4)."""
        assert StratifiedDefectData.can_braid(4, 2) is True

    def test_spectral_params_monotone(self):
        """Higher codim -> more spectral parameters."""
        for k in range(3):
            d_k = StratifiedDefectData.get_defect_data(k)
            d_k1 = StratifiedDefectData.get_defect_data(k + 1)
            assert d_k1["spectral_params"] > d_k["spectral_params"]


# ===================================================================
# Suite 2: Excision coproduct = Drinfeld coproduct
# ===================================================================

class TestExcisionCoproduct:
    """Verify Wilson line collision via excision = Drinfeld coproduct."""

    def test_excision_spin1_primitive(self):
        """Spin-1 excision coproduct is primitive."""
        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        result = wlce.excision_coproduct_spin1(0)
        assert result["primitive"] is True
        assert result["z_independent"] is True
        assert result["axiom"] == "(H2): E_1-chiral coalgebra, primitive sector"

    def test_excision_spin2_nonprimitive(self):
        """Spin-2 excision coproduct is not primitive at z != 0."""
        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        result = wlce.excision_coproduct_spin2(0, z=0.3 + 0.2j)
        assert result["primitive"] is False
        assert result["spin"] == 2

    def test_excision_equals_drinfeld_psi2(self):
        r = WilsonLineCollisionExcision(Psi=2.0, N_max=5).verify_excision_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_excision_equals_drinfeld_psi1(self):
        """Free boson (Psi=1): cross-term vanishes."""
        r = WilsonLineCollisionExcision(Psi=1.0, N_max=5).verify_excision_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_excision_equals_drinfeld_psi3(self):
        r = WilsonLineCollisionExcision(Psi=3.0, N_max=5).verify_excision_equals_drinfeld()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_excision_equals_drinfeld_complex_z(self):
        r = WilsonLineCollisionExcision(Psi=2.0, N_max=5).verify_excision_equals_drinfeld(
            z=0.7 - 0.4j
        )
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_excision_axiom_label(self):
        """Excision result carries correct axiom label."""
        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        r = wlce.verify_excision_equals_drinfeld()
        assert "(H2)" in r["axiom"]


# ===================================================================
# Suite 3: Triple excision (spectral coassociativity)
# ===================================================================

class TestTripleExcision:
    """Verify spectral coassociativity from triple Wilson line excision."""

    def test_triple_coassociativity(self):
        """(H4) from triple Wilson line collision."""
        twle = TripleWilsonLineExcision(Psi=2.0, N_max=3)
        r = twle.verify_spectral_coassociativity()
        assert r["ok"], (
            f"spin2_err={r['spin2_max_error']:.2e}, "
            f"coassoc_err={r['coassociativity_error']:.2e}"
        )
        assert r["spin1_ok"]

    def test_triple_coassociativity_psi1(self):
        """Free boson: triple excision is trivially coassociative."""
        twle = TripleWilsonLineExcision(Psi=1.0, N_max=3)
        r = twle.verify_spectral_coassociativity()
        assert r["ok"]

    def test_triple_axiom_label(self):
        twle = TripleWilsonLineExcision(Psi=2.0, N_max=3)
        r = twle.verify_spectral_coassociativity()
        assert "(H4)" in r["axiom"]

    def test_triple_product_exists(self):
        """Triple Miura product is computable."""
        twle = TripleWilsonLineExcision(Psi=2.0, N_max=3)
        triple = twle.miura_triple_product(0, 0.3 + 0.1j, 0.2 - 0.15j)
        assert triple.shape[0] == triple.shape[1]
        assert triple.shape[0] > 0


# ===================================================================
# Suite 4: FH holonomy at each E_n level
# ===================================================================

class TestFHHolonomy:
    """Verify the factorization homology holonomy (R-matrix) at each level."""

    def test_e1_holonomy_trivial(self):
        """E_1: no braiding, R = 1."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        r = wlbf.fh_holonomy_e1()
        assert r["R"] == 1.0
        assert r["en_level"] == 1
        assert r["crossing_possible"] is False

    def test_e2_holonomy_nontrivial(self):
        """E_2: one-parameter R-matrix from Yangian."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        r = wlbf.fh_holonomy_e2(3.5 + 0.7j)
        assert r["en_level"] == 2
        assert r["spectral_params"] == 1
        assert r["crossing_possible"] is True
        # R(u) = g(u) should be nontrivial
        assert abs(r["R"] - 1.0) > 1e-6

    def test_e3_holonomy_nontrivial(self):
        """E_3: two-parameter R-matrix from quantum toroidal."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        r = wlbf.fh_holonomy_e3(3.5 + 0.7j, -2.3 + 1.1j)
        assert r["en_level"] == 3
        assert r["spectral_params"] == 2
        assert r["crossing_possible"] is True
        assert abs(r["R"] - 1.0) > 1e-6

    def test_e3_zamolodchikov_factors(self):
        """E_3 R-matrix factorises as g(u)*g(v)*g(u-v)."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        u, v = 3.5 + 0.7j, -2.3 + 1.1j
        r = wlbf.fh_holonomy_e3(u, v)
        factors = r["zamolodchikov_factors"]
        expected = factors["R_1"] * factors["R_2"] * factors["R_12"]
        assert abs(r["R"] - expected) < 1e-12

    def test_e2_holonomy_generic_omega(self):
        """E_2 holonomy at generic Omega-background h=(3,-5,2)."""
        wlbf = WilsonLineBraidingFH(3.0, -5.0, 2.0)
        r = wlbf.fh_holonomy_e2(4.0 + 1.0j)
        assert r["en_level"] == 2
        assert abs(r["R"]) > 0

    def test_cy_condition_enforced(self):
        """CY condition h1+h2+h3=0 is enforced."""
        with pytest.raises(AssertionError):
            WilsonLineBraidingFH(1.0, 2.0, 3.0)


# ===================================================================
# Suite 5: FH unitarity and YBE
# ===================================================================

class TestFHBraidingProperties:
    """Verify braiding properties from FH holonomy."""

    def test_unitarity(self):
        r = WilsonLineBraidingFH(1.0, -2.0, 1.0).verify_unitarity_fh()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_ybe(self):
        r = WilsonLineBraidingFH(1.0, -2.0, 1.0).verify_ybe_fh()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_miki_exchange(self):
        r = WilsonLineBraidingFH(1.0, -2.0, 1.0).verify_e3_miki_from_fh()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_unitarity_generic(self):
        """Unitarity at generic Omega-background h=(3,-5,2)."""
        r = WilsonLineBraidingFH(3.0, -5.0, 2.0).verify_unitarity_fh()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"

    def test_ybe_generic(self):
        """YBE at generic Omega-background h=(3,-5,2)."""
        r = WilsonLineBraidingFH(3.0, -5.0, 2.0).verify_ybe_fh()
        assert r["ok"], f"max_error = {r['max_error']:.2e}"


# ===================================================================
# Suite 6: Wilson surface defects
# ===================================================================

class TestWilsonSurface:
    """Verify Wilson surface defect data and categorical S-matrix."""

    def test_surface_defect_data(self):
        wsd = WilsonSurfaceDefect(1.0, -2.0, 1.0)
        d = wsd.surface_defect_data()
        assert d["complex_codim"] == 1
        assert d["normal_bundle_rank"] == 1
        assert d["spectral_params"] == 1
        assert d["en_level_of_restriction"] == 2

    def test_categorical_s_charge1_trivial(self):
        """Charge-1 categorical S-matrix is trivial (=1) by CY unitarity."""
        wsd = WilsonSurfaceDefect(1.0, -2.0, 1.0)
        r = wsd.categorical_s_matrix_charge1(3.5 + 0.7j, -2.3 + 1.1j)
        assert r["trivial"] is True
        assert abs(r["S_matrix"] - 1.0) < 1e-10

    def test_categorical_s_generic_omega(self):
        """Charge-1 S-matrix trivial at generic h=(3,-5,2)."""
        wsd = WilsonSurfaceDefect(3.0, -5.0, 2.0)
        r = wsd.categorical_s_matrix_charge1(4.0 + 1.0j, 2.0 - 0.5j)
        assert r["trivial"] is True

    def test_surface_line_hierarchy(self):
        """Wilson surface/line hierarchy is consistent."""
        wsd = WilsonSurfaceDefect(1.0, -2.0, 1.0)
        r = wsd.verify_surface_line_hierarchy()
        assert r["ok"]

    def test_surface_cy_condition(self):
        """CY condition enforced for Wilson surface."""
        with pytest.raises(AssertionError):
            WilsonSurfaceDefect(1.0, 1.0, 1.0)


# ===================================================================
# Suite 7: Axiom dictionary (H1)--(H5)
# ===================================================================

class TestAxiomDictionary:
    """Verify the axiom dictionary is complete and consistent."""

    def test_dictionary_complete(self):
        r = AxiomDictionaryFH.verify_dictionary_completeness()
        assert r["ok"]
        assert r["complete"]
        assert len(r["missing"]) == 0

    def test_all_axioms_present(self):
        for hid in ["H1", "H2", "H3", "H4", "H5"]:
            d = AxiomDictionaryFH.get_axiom(hid)
            assert "fh_statement" in d
            assert "bialgebra_statement" in d

    def test_invalid_axiom(self):
        with pytest.raises(ValueError):
            AxiomDictionaryFH.get_axiom("H6")

    def test_h1_is_algebra(self):
        d = AxiomDictionaryFH.get_axiom("H1")
        assert "E_1-chiral algebra" in d["name"]
        assert "restriction" in d["fh_operation"]

    def test_h2_is_coalgebra(self):
        d = AxiomDictionaryFH.get_axiom("H2")
        assert "coalgebra" in d["name"]
        assert "excision" in d["fh_operation"]

    def test_h3_is_compatibility(self):
        d = AxiomDictionaryFH.get_axiom("H3")
        assert "compatibility" in d["name"].lower()

    def test_h4_is_coassociativity(self):
        d = AxiomDictionaryFH.get_axiom("H4")
        assert "coassociativity" in d["name"].lower()
        assert "K_3" in d["fh_statement"]

    def test_h5_is_antipode(self):
        d = AxiomDictionaryFH.get_axiom("H5")
        assert "antipode" in d["name"].lower()
        assert "reversal" in d["fh_operation"].lower()


# ===================================================================
# Suite 8: Cross-engine consistency
# ===================================================================

class TestCrossEngine:
    """Verify consistency with wilson_line_coproduct_engine."""

    def test_excision_matches_wilson_line_miura(self):
        """Excision coproduct agrees with Wilson line Miura verifier."""
        from compute.lib.wilson_line_coproduct_engine import WilsonLineMiuraVerifier

        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        wlm = WilsonLineMiuraVerifier(Psi=2.0, N_max=5)

        z = 0.3 + 0.2j
        P = wlce.TH.safe_proj(3)

        # Both engines should produce the same Delta_z(T_n)
        mx = 0.0
        for n in [0, -1, -2, 1]:
            exc_dt = wlce.TH.Delta_T(n, z)
            wlm_dt = wlm.TH.Delta_T(n, z)
            err = float(np.max(np.abs(P @ (exc_dt - wlm_dt) @ P)))
            mx = max(mx, err)
        assert mx < 1e-12, f"max_error = {mx:.2e}"

    def test_fh_rmatrix_matches_wilson_line(self):
        """FH holonomy R-matrix matches WilsonLineRMatrix."""
        from compute.lib.wilson_line_coproduct_engine import WilsonLineRMatrix

        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        wlr = WilsonLineRMatrix(1.0, -2.0, 1.0)

        for j in range(8):
            u = 3.5 + 0.7j * (j + 1) / 8
            v = -2.3 + 1.1j * (j + 1) / 8
            r_fh = wlbf.fh_holonomy_e3(u, v)["R"]
            r_wl = wlr.r_matrix_e3_charge1(u, v)
            assert abs(r_fh - r_wl) < 1e-12, \
                f"j={j}: |R_fh - R_wl| = {abs(r_fh - r_wl):.2e}"

    def test_fh_sigma2_matches_holomorphic_cs(self):
        """sigma_2 in FH engine matches holomorphic_cs_chiral_engine."""
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground

        omega = OmegaBackground(1, -2)
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        assert abs(float(omega.sigma2) - wlbf.sigma2) < 1e-12

    def test_excision_matches_e1_bialgebra_engine(self):
        """Excision coproduct agrees with e1_chiral_bialgebra_engine."""
        from compute.lib.e1_chiral_bialgebra_engine import BialgebraCompatibilityVerifier

        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        bv = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        P = wlce.TH.safe_proj(3)
        z = 0.3 + 0.2j
        mx = 0.0
        for n in [0, -1, -2, 1]:
            exc_dt = wlce.TH.Delta_T(n, z)
            bv_dt = bv.TH.Delta_T(n, z)
            err = float(np.max(np.abs(P @ (exc_dt - bv_dt) @ P)))
            mx = max(mx, err)
        assert mx < 1e-12, f"max_error = {mx:.2e}"

    def test_fh_e3_matches_e3_two_param(self):
        """FH E_3 holonomy matches e3_two_parameter_rmatrix engine."""
        from compute.lib.e3_two_parameter_rmatrix import (
            two_param_structure_function_additive,
        )

        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        for j in range(8):
            u = 3.5 + 0.7j * (j + 1) / 8
            v = -2.3 + 1.1j * (j + 1) / 8
            r_fh = wlbf.fh_holonomy_e3(u, v)["R"]
            r_e3 = two_param_structure_function_additive(u, v, 1.0, -2.0, 1.0)
            assert abs(r_fh - r_e3) < 1e-10, \
                f"j={j}: |R_fh - R_e3| = {abs(r_fh - r_e3):.2e}"

    def test_excision_spin1_matches_3d_primitive(self):
        """Excision spin-1 = 3d primitive coproduct from wilson_line_coproduct."""
        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        wlc = wlce.WLC
        P = wlce.TH.safe_proj(3)
        mx = 0.0
        for n in [-2, -1, 0, 1, 2]:
            exc = wlce.excision_coproduct_spin1(n)["Delta_exc_J"]
            prim = wlc.coproduct_3d(n)["Delta_J"]
            err = float(np.max(np.abs(P @ (exc - prim) @ P)))
            mx = max(mx, err)
        assert mx < 1e-12, f"max_error = {mx:.2e}"

    def test_fh_unitarity_two_paths(self):
        """Multi-path: FH unitarity via (a) verify method (b) direct computation."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        # Path A: verify method
        r_a = wlbf.verify_unitarity_fh()
        assert r_a["ok"]
        # Path B: direct computation at specific points
        g = wlbf.structure_function
        for u_val in [3.5 + 0.7j, 4.0 + 1.0j, -2.0 + 3.0j]:
            for v_val in [-1.0 + 0.5j, 2.0 - 1.5j]:
                G_pos = wlbf.fh_holonomy_e3(u_val, v_val)["R"]
                G_neg = wlbf.fh_holonomy_e3(-u_val, -v_val)["R"]
                assert abs(G_pos * G_neg - 1.0) < 1e-10, \
                    f"R({u_val},{v_val})*R({-u_val},{-v_val}) != 1"

    def test_zamolodchikov_two_paths(self):
        """Multi-path: Zamolodchikov factorisation via (a) engine (b) manual."""
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        g = wlbf.structure_function
        for u_val in [3.5 + 0.7j, 5.0 - 1.0j]:
            for v_val in [-2.3 + 1.1j, 4.0 + 0.5j]:
                # Path A: via fh_holonomy_e3
                r_a = wlbf.fh_holonomy_e3(u_val, v_val)["R"]
                # Path B: manual g(u)*g(v)*g(u-v)
                r_b = g(u_val) * g(v_val) * g(u_val - v_val)
                assert abs(r_a - r_b) < 1e-12


# ===================================================================
# Suite 9: E_n level computation
# ===================================================================

class TestEnLevel:
    """Verify E_n level computation for defects."""

    def test_en_level_bulk(self):
        """Bulk (codim 0) has E_3."""
        assert StratifiedDefectData.en_level_of_defect(3, 3) == 3

    def test_en_level_surface(self):
        """Surface (codim 1) has E_2."""
        assert StratifiedDefectData.en_level_of_defect(3, 2) == 2

    def test_en_level_line(self):
        """Line (codim 2) has E_1."""
        assert StratifiedDefectData.en_level_of_defect(3, 1) == 1

    def test_en_level_point(self):
        """Point (codim 3) has E_0."""
        assert StratifiedDefectData.en_level_of_defect(3, 0) == 0


# ===================================================================
# Suite 10: AP compliance
# ===================================================================

class TestAPCompliance:
    """Verify compliance with anti-patterns."""

    def test_ap_cy31_spectral_not_worldsheet(self):
        """AP-CY31: z is spectral, not worldsheet.
        The excision coproduct at z=0 is well-defined (no singularity).
        """
        wlce = WilsonLineCollisionExcision(Psi=2.0, N_max=5)
        result = wlce.excision_coproduct_spin2(0, z=0.0)
        # z=0 should produce a finite matrix (no OPE singularity)
        assert np.all(np.isfinite(result["Delta_exc_T"]))

    def test_ap_cy22_miki_not_operadic(self):
        """AP-CY22: Miki automorphism is algebra-specific, not operadic."""
        # The Miki exchange test verifies the ALGEBRA-SPECIFIC identity
        # G(u,v)/G(v,u) = g(u-v)^2, which is a property of the quantum
        # toroidal algebra, NOT a general E_3 identity.
        r = WilsonLineBraidingFH(1.0, -2.0, 1.0).verify_e3_miki_from_fh()
        assert r["ok"]

    def test_ap_cy28_pole_safe(self):
        """AP-CY28: test points avoid poles at +/- h_i."""
        # For h = (1, -2, 1): poles at z = +/-1, +/-2
        # Test point z = 3.5 + 0.7j is safe (far from all +/- h_i)
        wlbf = WilsonLineBraidingFH(1.0, -2.0, 1.0)
        r = wlbf.fh_holonomy_e2(3.5 + 0.7j)
        assert np.isfinite(r["R"])
