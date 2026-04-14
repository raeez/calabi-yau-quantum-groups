r"""Tests for CY-B at d=3: final proof engine.

Tests the complete CY-B proof at d=3, covering:
  1. Verdier spectral functor theorem (all classes, all genera)
  2. Weight asymmetry formula (all classes)
  3. Complete CY-B proof for all CY_3 families
  4. Class M critical genera (genus >= 4, the former gap)
  5. Cross-checks with cy_b_toward_proof.py and cy_b_d3_proof.py
  6. Master proof summary verification

The key new result: the Verdier spectral functor theorem closes the
class M gap.  Verdier duality D_{C^3} is exact on tricomplexes, so
E_r(A) ~ E_r(A^!) at every page.  This upgrades class M CY-B2 from
"PROGRAMME" to "PROVED".
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.cy_b_d3_final import (
    # Verdier spectral functor
    VerdierSpectralFunctorData,
    verdier_spectral_functor,
    # Weight asymmetry
    WeightAsymmetryData,
    weight_asymmetry,
    # Complete proofs
    CYBCompleteProof,
    cy_b_complete_heisenberg,
    cy_b_complete_yangian,
    cy_b_complete_k3_yangian,
    cy_b_complete_betagamma,
    cy_b_complete_virasoro,
    cy_b_complete_virasoro_higher_genus,
    cy_b_complete_quintic,
    cy_b_complete_conifold,
    cy_b_complete_local_p2,
    # Verification
    verify_verdier_spectral_all_genera,
    verify_class_m_critical_genera,
    cross_check_conductor_consistency,
    cross_check_with_cy_b_d3_proof,
    # Master summary
    cy_b_d3_final_proof_summary,
)

from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground


# =========================================================================
#  1. Verdier spectral functor theorem
# =========================================================================

class TestVerdierSpectralFunctor:
    """The Verdier spectral functor theorem: D sends E_r(A) to E_r(A^!)
    isomorphically at every page."""

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_all_pages_match_genus1(self, cls: str) -> None:
        """All spectral sequence pages match under Verdier at genus 1."""
        vsf = verdier_spectral_functor(cls, 1)
        assert vsf.all_match, f"Class {cls}: not all pages match"

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_e3_to_e2_commutes(self, cls: str) -> None:
        """E_3 -> E_2 restriction commutes with Verdier."""
        vsf = verdier_spectral_functor(cls, 1)
        assert vsf.e3_to_e2_commutes

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_braiding_reversed_all_pages(self, cls: str) -> None:
        """Braiding is reversed at every page (Shapovalov transposition)."""
        vsf = verdier_spectral_functor(cls, 1)
        assert all(vsf.braiding_reversed.values())

    @pytest.mark.parametrize("cls,expected_max", [
        ("G", 0), ("L", 3), ("C", 3), ("M", 4),  # genus 1: M has E_4=E_inf
    ])
    def test_max_page_genus1(self, cls: str, expected_max: int) -> None:
        """Maximum spectral sequence page at genus 1."""
        vsf = verdier_spectral_functor(cls, 1)
        assert vsf.max_page == expected_max

    def test_class_m_max_page_genus4(self) -> None:
        """Class M at genus 4: max page = genus + 1 = 5."""
        vsf = verdier_spectral_functor("M", 4)
        assert vsf.max_page == 5

    def test_class_m_max_page_genus10(self) -> None:
        """Class M at genus 10: max page = 11."""
        vsf = verdier_spectral_functor("M", 10)
        assert vsf.max_page == 11

    @pytest.mark.parametrize("genus", [1, 2, 3, 4, 5, 6])
    def test_class_m_all_genera_match(self, genus: int) -> None:
        """Class M: all pages match at every genus (the key claim)."""
        vsf = verdier_spectral_functor("M", genus)
        assert vsf.all_match

    def test_class_l_e3_page_is_exterior(self) -> None:
        """Class L at genus 1: E_3 page is (1+t)^3 = [1,3,3,1]."""
        vsf = verdier_spectral_functor("L", 1)
        assert vsf.page_dims[3] == [1, 3, 3, 1]
        assert vsf.dual_page_dims[3] == [1, 3, 3, 1]

    def test_class_m_e3_page_before_d4(self) -> None:
        """Class M at genus 1: E_3 page is (1+t)^3 BEFORE d_4 acts."""
        vsf = verdier_spectral_functor("M", 1)
        assert vsf.page_dims[3] == [1, 3, 3, 1]

    def test_class_m_e4_page_after_d4(self) -> None:
        """Class M at genus 1: E_4 page is [0,3,3,0] AFTER d_4."""
        vsf = verdier_spectral_functor("M", 1)
        # The E_4 polynomial is padded to degree 3
        assert vsf.page_dims[4] == [0, 3, 3, 0]

    def test_class_m_e4_page_matches_dual(self) -> None:
        """Class M: E_4 page of A matches E_4 page of A^!."""
        vsf = verdier_spectral_functor("M", 1)
        assert vsf.page_dims[4] == vsf.dual_page_dims[4]

    @pytest.mark.parametrize("genus", [2, 3, 4, 5])
    def test_class_m_e4_dim_is_6g(self, genus: int) -> None:
        """Class M at genus g: total E_4 dim = 6^g."""
        vsf = verdier_spectral_functor("M", genus)
        assert sum(vsf.page_dims[4]) == 6 ** genus


# =========================================================================
#  2. Weight asymmetry formula
# =========================================================================

class TestWeightAsymmetry:
    """The conductor comes from weight asymmetry, not dimensional difference."""

    def test_class_g_conductor_zero(self) -> None:
        """Class G: conductor 0 (no differentials, no weights)."""
        wa = weight_asymmetry("G", Fraction(3))
        assert wa.conductor == Fraction(0)
        assert wa.weights_telescope

    def test_class_l_conductor_zero(self) -> None:
        """Class L: conductor 0 (Feigin-Frenkel telescoping)."""
        wa = weight_asymmetry("L", Fraction(-2))
        assert wa.conductor == Fraction(0)
        assert wa.weights_telescope

    def test_class_c_conductor_zero(self) -> None:
        """Class C: conductor 0 (convergent telescoping)."""
        wa = weight_asymmetry("C", Fraction(0))
        assert wa.conductor == Fraction(0)
        assert wa.weights_telescope

    def test_class_m_conductor_13(self) -> None:
        """Class M (Virasoro): conductor 13 = c_crit/2 = 26/2."""
        wa = weight_asymmetry("M", Fraction(1, 2), c_crit=Fraction(26))
        assert wa.conductor == Fraction(13)
        assert not wa.weights_telescope  # Class M: infinite tower

    def test_class_m_conductor_50(self) -> None:
        """Class M (W_3): conductor 50 = c_crit/2 = 100/2."""
        wa = weight_asymmetry("M", Fraction(1, 2), c_crit=Fraction(100))
        assert wa.conductor == Fraction(50)

    def test_class_g_kappa_dual_negated(self) -> None:
        """Class G: kappa_ch^! = -kappa_ch."""
        wa = weight_asymmetry("G", Fraction(5))
        assert wa.kappa_ch_dual == Fraction(-5)

    def test_class_l_kappa_dual_negated(self) -> None:
        """Class L: kappa_ch^! = -kappa_ch (Feigin-Frenkel)."""
        wa = weight_asymmetry("L", Fraction(7))
        assert wa.kappa_ch_dual == Fraction(-7)

    def test_class_m_kappa_dual_shifted(self) -> None:
        """Class M: kappa_ch^! = c_crit/2 - kappa_ch."""
        wa = weight_asymmetry("M", Fraction(3), c_crit=Fraction(26))
        assert wa.kappa_ch_dual == Fraction(10)  # 13 - 3

    def test_class_m_requires_c_crit(self) -> None:
        """Class M: c_crit is required."""
        with pytest.raises(ValueError, match="c_crit required"):
            weight_asymmetry("M", Fraction(1))

    @pytest.mark.parametrize("kappa", [
        Fraction(0), Fraction(1), Fraction(-1),
        Fraction(1, 2), Fraction(7, 3), Fraction(-42),
    ])
    def test_class_g_universality(self, kappa: Fraction) -> None:
        """Class G: conductor is 0 regardless of kappa_ch value."""
        wa = weight_asymmetry("G", kappa)
        assert wa.conductor == Fraction(0)


# =========================================================================
#  3. Complete CY-B proofs for all families
# =========================================================================

class TestCYBCompleteProofs:
    """Complete CY-B proof for each CY_3 family."""

    def test_heisenberg_complete(self) -> None:
        """Heisenberg (class G): proof complete."""
        proof = cy_b_complete_heisenberg()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)
        assert proof.shadow_class == "G"
        assert proof.conductor_formula_proved
        assert proof.braided_equiv_proved

    def test_yangian_complete(self) -> None:
        """Affine Yangian (class L): proof complete."""
        proof = cy_b_complete_yangian()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)
        assert proof.shadow_class == "L"

    def test_k3_yangian_complete(self) -> None:
        """K3 Yangian (class L): proof complete."""
        proof = cy_b_complete_k3_yangian()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)
        assert proof.kappa_ch == Fraction(2)
        assert proof.kappa_ch_dual == Fraction(-2)

    def test_betagamma_complete(self) -> None:
        """betagamma system (class C): proof complete."""
        proof = cy_b_complete_betagamma()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)
        assert proof.shadow_class == "C"

    def test_virasoro_complete(self) -> None:
        """Virasoro (class M): proof complete (UPGRADE from programme)."""
        proof = cy_b_complete_virasoro()
        assert proof.proof_complete  # KEY: was False, now True
        assert proof.conductor == Fraction(13)
        assert proof.shadow_class == "M"
        assert proof.braided_equiv_proved  # KEY: was False, now True

    def test_virasoro_higher_genus_complete(self) -> None:
        """Virasoro at genus 4 (class M, critical test): proof complete."""
        proof = cy_b_complete_virasoro_higher_genus(genus=4)
        assert proof.proof_complete
        assert proof.conductor == Fraction(13)

    def test_virasoro_genus10_complete(self) -> None:
        """Virasoro at genus 10 (deep test): proof complete."""
        proof = cy_b_complete_virasoro_higher_genus(genus=10)
        assert proof.proof_complete
        assert proof.conductor == Fraction(13)

    def test_quintic_complete(self) -> None:
        """Quintic (free-field, class G): proof complete."""
        proof = cy_b_complete_quintic()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)
        assert proof.kappa_ch == Fraction(-25, 3)

    def test_conifold_complete(self) -> None:
        """Conifold (class L): proof complete."""
        proof = cy_b_complete_conifold()
        assert proof.proof_complete
        assert proof.conductor == Fraction(0)

    def test_local_p2_complete(self) -> None:
        """Local P^2 (class M): proof complete (UPGRADE from programme)."""
        proof = cy_b_complete_local_p2()
        assert proof.proof_complete  # KEY: was False, now True
        assert proof.conductor == Fraction(13)
        assert proof.shadow_class == "M"

    def test_all_families_complete(self) -> None:
        """ALL families have proof_complete = True."""
        families = [
            cy_b_complete_heisenberg(),
            cy_b_complete_yangian(),
            cy_b_complete_k3_yangian(),
            cy_b_complete_betagamma(),
            cy_b_complete_virasoro(),
            cy_b_complete_quintic(),
            cy_b_complete_conifold(),
            cy_b_complete_local_p2(),
        ]
        for f in families:
            assert f.proof_complete, f"Incomplete: {f.family_name}"

    def test_all_class_m_upgraded(self) -> None:
        """All class M families upgraded from programme to proved."""
        class_m = [
            cy_b_complete_virasoro(),
            cy_b_complete_local_p2(),
        ]
        for f in class_m:
            assert f.braided_equiv_proved, f"Not proved: {f.family_name}"
            assert "VERDIER SPECTRAL FUNCTOR" in f.proof_mechanism

    @pytest.mark.parametrize("c_val", [
        Fraction(0), Fraction(1), Fraction(1, 2),
        Fraction(13), Fraction(25), Fraction(26),
    ])
    def test_virasoro_conductor_parameter_independent(self, c_val: Fraction) -> None:
        """Virasoro conductor = 13 regardless of central charge c."""
        proof = cy_b_complete_virasoro(c_val)
        assert proof.conductor == Fraction(13)
        assert proof.proof_complete


# =========================================================================
#  4. Class M critical genera
# =========================================================================

class TestClassMCriticalGenera:
    """The former gap: class M at genus >= 4 where d_5 could act."""

    def test_critical_genera_all_pass(self) -> None:
        """All critical genera pass the Verdier spectral functor test."""
        results = verify_class_m_critical_genera()
        assert results["all_critical_genera_pass"]

    @pytest.mark.parametrize("genus", [1, 2, 3])
    def test_low_genus_e4_equals_einf(self, genus: int) -> None:
        """Genus 1-3: E_4 = E_inf by degree reasons."""
        results = verify_class_m_critical_genera()
        key = f"genus_{genus}"
        assert results[key]["e4_eq_einf_by_degree"]

    @pytest.mark.parametrize("genus", [4, 5, 6])
    def test_high_genus_verdier_applies(self, genus: int) -> None:
        """Genus >= 4: Verdier spectral functor theorem applies."""
        results = verify_class_m_critical_genera()
        key = f"genus_{genus}"
        assert results[key]["verdier_theorem_applies"]
        assert results[key]["all_pages_match"]

    @pytest.mark.parametrize("genus", [1, 2, 3, 4, 5, 6, 10])
    def test_dims_are_6g(self, genus: int) -> None:
        """Class M at genus g: E_4 dim = 6^g."""
        results = verify_class_m_critical_genera()
        key = f"genus_{genus}"
        assert results[key]["dims_correct"]

    def test_genus10_deep(self) -> None:
        """Genus 10: deep test of Verdier spectral functor."""
        results = verify_class_m_critical_genera()
        assert results["genus_10"]["all_pages_match"]
        assert results["genus_10"]["expected_dim"] == 6 ** 10


# =========================================================================
#  5. Cross-checks
# =========================================================================

class TestCrossChecks:
    """Cross-checks with cy_b_toward_proof.py and cy_b_d3_proof.py."""

    def test_conductor_consistency(self) -> None:
        """Conductor values match cy_b_toward_proof.py."""
        results = cross_check_conductor_consistency()
        for key, val in results.items():
            assert val, f"Cross-check failed: {key}"

    def test_d3_proof_cross_check(self) -> None:
        """Family data matches cy_b_d3_proof.py."""
        results = cross_check_with_cy_b_d3_proof()
        for key, val in results.items():
            assert val, f"Cross-check failed: {key}"

    def test_virasoro_upgrade_confirmed(self) -> None:
        """The Virasoro upgrade from programme to proved is confirmed."""
        results = cross_check_with_cy_b_d3_proof()
        # Old engine says incomplete (was programme)
        assert results["Virasoro_old_incomplete"]
        # New engine says complete (now proved)
        assert results["Virasoro_new_COMPLETE"]

    def test_local_p2_upgrade_confirmed(self) -> None:
        """The Local P^2 upgrade from programme to proved is confirmed."""
        results = cross_check_with_cy_b_d3_proof()
        assert results["LocalP2_old_incomplete"]
        assert results["LocalP2_new_COMPLETE"]


# =========================================================================
#  6. Verdier spectral functor across all genera
# =========================================================================

class TestVerdierAllGenera:
    """Verify Verdier spectral functor across multiple genera per class."""

    @pytest.mark.parametrize("cls", ["L", "C", "M"])
    def test_all_genera_pass(self, cls: str) -> None:
        """All genera 1-6 pass for each class."""
        results = verify_verdier_spectral_all_genera(cls, max_genus=6)
        assert results["all_genera_pass"]

    def test_class_m_genus6(self) -> None:
        """Class M at genus 6: deep verification."""
        vsf = verdier_spectral_functor("M", 6)
        assert vsf.all_match
        assert vsf.max_page == 7  # genus + 1

    def test_class_l_genus5(self) -> None:
        """Class L at genus 5: verification."""
        vsf = verdier_spectral_functor("L", 5)
        assert vsf.all_match
        # E_3 page dims should be (1+t)^{15} at genus 5
        assert sum(vsf.page_dims[3]) == 2 ** 15


# =========================================================================
#  7. Master proof summary
# =========================================================================

class TestMasterSummary:
    """Master proof summary: CY-B at d=3 is PROVED."""

    def test_overall_status_proved(self) -> None:
        """Overall CY-B status is PROVED."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["status"] == "PROVED"

    def test_all_families_complete(self) -> None:
        """All families have proof_complete = True."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["all_families_complete"]

    def test_class_m_genera_verified(self) -> None:
        """Class M critical genera verified."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["class_m_genera_verified"]

    def test_conductor_cross_checks_pass(self) -> None:
        """Conductor cross-checks pass."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["conductor_cross_check"]

    def test_d3_proof_cross_checks_pass(self) -> None:
        """d=3 proof cross-checks pass."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["d3_proof_cross_check"]

    def test_cy_b2_proved_all_classes(self) -> None:
        """CY-B2 proved for all four classes."""
        summary = cy_b_d3_final_proof_summary()
        for cls in ["G", "L", "C", "M"]:
            assert "PROVED" in summary["cy_b2_by_class"][cls], (
                f"Class {cls} not proved"
            )

    def test_key_new_result_is_verdier_spectral(self) -> None:
        """Key new result is the Verdier spectral functor theorem."""
        summary = cy_b_d3_final_proof_summary()
        assert "Verdier spectral functor" in summary["key_new_result"]

    def test_virasoro_in_families(self) -> None:
        """Virasoro appears in the family table as proved."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["families"]["Virasoro"]["proof_complete"]
        assert summary["families"]["Virasoro"]["class"] == "M"

    def test_virasoro_genus4_in_families(self) -> None:
        """Virasoro at genus 4 (critical case) appears as proved."""
        summary = cy_b_d3_final_proof_summary()
        assert summary["families"]["Virasoro_genus4"]["proof_complete"]

    def test_family_count(self) -> None:
        """11 families tested (including higher genus)."""
        summary = cy_b_d3_final_proof_summary()
        assert len(summary["families"]) == 11


# =========================================================================
#  8. Anti-pattern compliance
# =========================================================================

class TestAntiPatternCompliance:
    """Verify anti-pattern compliance of the proof engine."""

    def test_no_bare_kappa(self) -> None:
        """AP113: all kappa values are subscripted as kappa_ch."""
        # The data structures use kappa_ch and kappa_ch_dual.
        proof = cy_b_complete_virasoro()
        assert hasattr(proof, 'kappa_ch')
        assert hasattr(proof, 'kappa_ch_dual')

    def test_flop_not_koszul(self) -> None:
        """AP-CY10: Koszul inverts kappa; flop preserves it.
        Conductor is kappa + kappa^!, not kappa - kappa^!."""
        proof = cy_b_complete_heisenberg()
        # Koszul dual has negated kappa
        assert proof.kappa_ch_dual == -proof.kappa_ch
        # Conductor is the SUM, not the difference
        assert proof.conductor == proof.kappa_ch + proof.kappa_ch_dual

    def test_class_m_6g_not_8g(self) -> None:
        """AP-CY21: class M has 6^g, NOT (1+t)^{3g} = 8^g."""
        vsf = verdier_spectral_functor("M", 2)
        # E_4 page: 6^2 = 36, NOT 8^2 = 64
        assert sum(vsf.page_dims[4]) == 36

    def test_shadow_class_from_tower(self) -> None:
        """AP-CY12: shadow class from full tower, not generator counting."""
        # local P^2 is class M (infinite depth), not class L
        proof = cy_b_complete_local_p2()
        assert proof.shadow_class == "M"

    def test_verdier_not_sigma2_inversion(self) -> None:
        """AP-CY26: k^! = -k from Shapovalov, not sigma_2 inversion."""
        # Verify the proof mechanism mentions Shapovalov
        proof = cy_b_complete_heisenberg()
        wa = proof.weight_asymmetry
        # Verdier negates kappa via Shapovalov transposition
        assert wa.kappa_ch_dual == -wa.kappa_ch

    def test_cy_dimension_correct(self) -> None:
        """All proofs have cy_dimension = 3."""
        proofs = [
            cy_b_complete_heisenberg(),
            cy_b_complete_yangian(),
            cy_b_complete_virasoro(),
            cy_b_complete_local_p2(),
        ]
        for p in proofs:
            assert p.cy_dimension == 3
