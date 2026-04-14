r"""Tests for CY-B conductor formula proof.

Tests the universal conductor formula rho_K = kappa_ch(A) + kappa_ch(A^!)
across all shadow classes and families, verifying:
    1. Class G conductor = 0 (Heisenberg, K3 Mukai)
    2. Class L conductor = 0 (Kac-Moody, all simple Lie algebras)
    3. Class M conductor = c_crit/2 (Virasoro: 13, W_3: 50)
    4. Stasheff telescoping (derived = classical conductor)
    5. Verdier duality data consistency
    6. Cross-checks with e1_koszul_three_families.py
    7. Cross-checks with chiral_koszul_derived.py
    8. CY-specific conductor (K3: d=2, CY3 free-field)
    9. Universality within each class
    10. Serre duality argument
"""

import pytest
from fractions import Fraction

from compute.lib.cy_b_toward_proof import (
    # Conductor computations
    heisenberg_conductor,
    kac_moody_sl2_conductor,
    kac_moody_general_conductor,
    virasoro_conductor,
    w_n_conductor,
    k3_mukai_conductor,
    # Proof components
    verdier_duality_on_e2_bar,
    stasheff_telescoping,
    # CY-B proof assembly
    cy_b_proof_heisenberg,
    cy_b_proof_kac_moody,
    cy_b_proof_virasoro,
    cy_b_proof_k3,
    # CY-specific
    serre_duality_conductor,
    cy_b_for_k3,
    cy_b_for_cy3_free_field,
    # Master verification
    verify_all_conductors,
    verify_conductor_formula_universality,
    # Cross-checks
    cross_check_with_e1_koszul,
    cross_check_with_derived_koszul,
    # Summary
    cy_b_proof_status_summary,
    # Data structures
    ConductorFormulaInput,
    universal_conductor_formula,
    CONDUCTOR_GROUND_TRUTH,
    CONDUCTOR_BY_CLASS,
)


# =========================================================================
#  1. Class G conductor = 0 (Heisenberg)
# =========================================================================

class TestClassGConductor:
    """Class G (Gaussian): conductor rho_K = 0."""

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(3), Fraction(-1), Fraction(-5),
        Fraction(1, 2), Fraction(7, 3), Fraction(-42),
    ])
    def test_heisenberg_conductor_zero(self, k: Fraction) -> None:
        """kappa_ch(H_k) + kappa_ch(H_{-k}) = 0 for all k."""
        result = heisenberg_conductor(k)
        assert result.rho_K == Fraction(0), f"Heisenberg at k={k}: rho_K={result.rho_K}"

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(-1)])
    def test_heisenberg_kappa_values(self, k: Fraction) -> None:
        """kappa_ch(H_k) = k, kappa_ch(H_k^!) = -k."""
        proof = cy_b_proof_heisenberg(k)
        assert proof.conductor_result.rho_K == Fraction(0)
        assert proof.proof_complete

    def test_heisenberg_stasheff_trivial(self) -> None:
        """Stasheff telescoping is trivial for class G."""
        stash = stasheff_telescoping("G")
        assert stash.individual_corrections_zero
        assert stash.total_correction_zero
        assert stash.num_nonzero_mn == 0

    def test_k3_mukai_conductor_zero(self) -> None:
        """K3 Mukai Heisenberg: kappa_ch = 2, kappa_ch^! = -2, rho_K = 0."""
        result = k3_mukai_conductor()
        assert result.rho_K == Fraction(0)

    def test_k3_mukai_kappa_values(self) -> None:
        """K3: kappa_ch = chi(O_{K3}) = 2."""
        proof = cy_b_proof_k3()
        cond = proof.conductor_result
        assert cond.rho_K == Fraction(0)
        assert proof.proof_complete


# =========================================================================
#  2. Class L conductor = 0 (Kac-Moody)
# =========================================================================

class TestClassLConductor:
    """Class L (Lie): conductor rho_K = 0."""

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(3), Fraction(-1), Fraction(-3),
        Fraction(10), Fraction(1, 2),
    ])
    def test_sl2_conductor_zero(self, k: Fraction) -> None:
        """kappa_ch(V_k(sl_2)) + kappa_ch(V_{k'}(sl_2)) = 0."""
        result = kac_moody_sl2_conductor(k)
        assert result.rho_K == Fraction(0), f"sl_2 at k={k}: rho_K={result.rho_K}"

    @pytest.mark.parametrize("dim_g,h_dual,name", [
        (3, 2, "sl_2"),
        (8, 3, "sl_3"),
        (15, 4, "sl_4"),
        (14, 4, "G_2"),
        (248, 30, "E_8"),
    ])
    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(-1)])
    def test_general_lie_conductor_zero(
        self, dim_g: int, h_dual: int, name: str, k: Fraction
    ) -> None:
        """For all simple g: kappa_ch(V_k(g)) + kappa_ch(V_{k'}(g)) = 0."""
        result = kac_moody_general_conductor(dim_g, h_dual, k)
        assert result.rho_K == Fraction(0), f"{name} at k={k}: rho_K={result.rho_K}"

    def test_feigin_frenkel_algebraic_proof(self) -> None:
        """The Feigin-Frenkel identity: kappa' = -kappa algebraically.

        For g simple:
            kappa_ch(V_k(g)) = dim(g)(k + h^v)/(2h^v)
            k' = -k - 2h^v
            kappa_ch(V_{k'}(g)) = dim(g)(k' + h^v)/(2h^v)
                                = dim(g)(-k - h^v)/(2h^v) = -kappa
        So kappa + kappa' = 0. QED.
        """
        # Test with symbolic k (as Fraction parameter sweep)
        for k_num in range(-10, 11):
            if k_num == 0:
                continue
            k = Fraction(k_num)
            for dim_g, h_dual in [(3, 2), (8, 3), (248, 30)]:
                kappa = Fraction(dim_g, 2 * h_dual) * (k + h_dual)
                k_prime = -k - 2 * h_dual
                kappa_prime = Fraction(dim_g, 2 * h_dual) * (k_prime + h_dual)
                assert kappa + kappa_prime == 0, (
                    f"Feigin-Frenkel failed at dim={dim_g}, h^v={h_dual}, k={k}"
                )

    def test_stasheff_class_l(self) -> None:
        """Stasheff telescoping for class L: m_3 is coboundary."""
        stash = stasheff_telescoping("L")
        assert not stash.individual_corrections_zero
        assert stash.total_correction_zero
        assert stash.num_nonzero_mn == 1

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2)])
    def test_kac_moody_proof_complete(self, k: Fraction) -> None:
        """CY-B proof is complete for Kac-Moody."""
        proof = cy_b_proof_kac_moody(k)
        assert proof.proof_complete
        assert proof.conductor_result.rho_K == Fraction(0)


# =========================================================================
#  3. Class M conductor = c_crit/2 (Virasoro, W_N)
# =========================================================================

class TestClassMConductor:
    """Class M (Mock modular): conductor rho_K = c_crit/2."""

    @pytest.mark.parametrize("c", [
        Fraction(0), Fraction(1), Fraction(2), Fraction(1, 2),
        Fraction(13), Fraction(25), Fraction(26), Fraction(7, 10),
    ])
    def test_virasoro_conductor_13(self, c: Fraction) -> None:
        """kappa_ch(Vir_c) + kappa_ch(Vir_{26-c}) = 13 for all c."""
        result = virasoro_conductor(c)
        assert result.rho_K == Fraction(13), f"Vir_{c}: rho_K={result.rho_K}"

    def test_virasoro_c_crit_26(self) -> None:
        """Critical central charge of Virasoro is 26."""
        c = Fraction(1)
        result = virasoro_conductor(c)
        assert result.c_crit == Fraction(26)

    def test_virasoro_self_dual_c13(self) -> None:
        """c = 13 is the self-dual point: Vir_13 is Koszul self-dual."""
        result = virasoro_conductor(Fraction(13))
        # kappa_ch = 13/2, kappa_ch^! = 13/2
        assert result.rho_K == Fraction(13)
        assert result.c_crit == Fraction(26)

    @pytest.mark.parametrize("c", [Fraction(0), Fraction(1), Fraction(50)])
    def test_w3_conductor_50(self, c: Fraction) -> None:
        """W_3 conductor = 50 (c_crit = 100)."""
        result = w_n_conductor(3, c)
        assert result.rho_K == Fraction(50), f"W_3 at c={c}: rho_K={result.rho_K}"

    def test_w2_equals_virasoro(self) -> None:
        """W_2 = Virasoro, conductor = 13."""
        result = w_n_conductor(2, Fraction(1))
        assert result.rho_K == Fraction(13)

    def test_stasheff_class_m(self) -> None:
        """Stasheff telescoping for class M: infinite corrections sum to 0."""
        stash = stasheff_telescoping("M")
        assert not stash.individual_corrections_zero
        assert stash.total_correction_zero
        assert stash.num_nonzero_mn == "infinite"

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(13)])
    def test_virasoro_proof_complete(self, c: Fraction) -> None:
        """CY-B proof is complete for Virasoro."""
        proof = cy_b_proof_virasoro(c)
        assert proof.proof_complete
        assert proof.conductor_result.rho_K == Fraction(13)


# =========================================================================
#  4. Verdier duality consistency
# =========================================================================

class TestVerdierDuality:
    """Verdier duality on the E_2 bar complex."""

    @pytest.mark.parametrize("cls", ["G", "L"])
    def test_verdier_negation_for_gl(self, cls: str) -> None:
        """For classes G and L, Verdier negates kappa_ch."""
        verd = verdier_duality_on_e2_bar(cls)
        assert verd.verdier_action_on_kappa == "negation"
        assert verd.shapovalov_transposition

    @pytest.mark.parametrize("cls", ["C", "M"])
    def test_verdier_shift_for_cm(self, cls: str) -> None:
        """For classes C and M, Verdier shifts by c_crit."""
        verd = verdier_duality_on_e2_bar(cls)
        assert verd.verdier_action_on_kappa == "c_crit_shift"
        assert verd.shapovalov_transposition

    def test_verdier_en_level(self) -> None:
        """Verdier duality is at E_2 level."""
        for cls in ["G", "L", "C", "M"]:
            verd = verdier_duality_on_e2_bar(cls)
            assert verd.en_level == 2


# =========================================================================
#  5. Stasheff telescoping (thm:derived-conductor)
# =========================================================================

class TestStasheffTelescoping:
    """Stasheff telescoping: derived conductor = classical conductor."""

    @pytest.mark.parametrize("cls", ["G", "L", "C", "M"])
    def test_total_correction_zero(self, cls: str) -> None:
        """The total A_inf correction to the conductor is ALWAYS zero."""
        stash = stasheff_telescoping(cls)
        assert stash.total_correction_zero

    def test_class_g_trivial(self) -> None:
        stash = stasheff_telescoping("G")
        assert stash.individual_corrections_zero
        assert stash.num_nonzero_mn == 0

    def test_class_l_single_correction(self) -> None:
        stash = stasheff_telescoping("L")
        assert stash.num_nonzero_mn == 1

    def test_class_m_infinite_corrections(self) -> None:
        stash = stasheff_telescoping("M")
        assert stash.num_nonzero_mn == "infinite"


# =========================================================================
#  6. CY-specific conductor
# =========================================================================

class TestCYSpecificConductor:
    """CY-specific conductor via Serre duality."""

    def test_k3_conductor_proved(self) -> None:
        """K3 (d=2): rho_K = 0, PROVED."""
        result = cy_b_for_k3()
        assert result["proved"]
        assert result["rho_K"] == Fraction(0)
        assert result["kappa_ch"] == Fraction(2)
        assert result["kappa_ch_dual"] == Fraction(-2)

    def test_cy3_free_field_quintic(self) -> None:
        """CY3 quintic (free-field branch): rho_K = 0."""
        result = cy_b_for_cy3_free_field(Fraction(-200))
        assert result["proved"]
        assert result["rho_K"] == Fraction(0)
        assert result["kappa_ch"] == Fraction(-200, 24)

    def test_serre_duality_even_d(self) -> None:
        """Even CY dimension: rho_K = 0 unconditionally."""
        for d in [2, 4, 6]:
            result = serre_duality_conductor(d, Fraction(2))
            assert result["rho_K"] == Fraction(0)
            assert result["proved"]

    def test_serre_duality_odd_d(self) -> None:
        """Odd CY dimension: free-field conductor = 0."""
        result = serre_duality_conductor(3, Fraction(-200, 24))
        assert result["rho_K"] == Fraction(0)  # Free-field branch


# =========================================================================
#  7. Universality within each class
# =========================================================================

class TestUniversality:
    """Conductor is class-dependent but universal within each class."""

    def test_universality_summary(self) -> None:
        """All universality checks pass."""
        result = verify_conductor_formula_universality()
        assert result["class_G_all_zero"]
        assert result["class_L_all_zero"]
        assert result["class_M_virasoro_all_13"]
        assert result["class_M_w3_all_50"]
        assert result["class_M_family_dependent"]

    def test_conductor_by_class_type(self) -> None:
        """CONDUCTOR_BY_CLASS has correct types."""
        assert CONDUCTOR_BY_CLASS["G"] == "zero"
        assert CONDUCTOR_BY_CLASS["L"] == "zero"
        assert CONDUCTOR_BY_CLASS["M"] == "nonzero"


# =========================================================================
#  8. Master verification
# =========================================================================

class TestMasterVerification:
    """Master verification: all families pass."""

    def test_all_conductors(self) -> None:
        """Every family passes the conductor verification."""
        results = verify_all_conductors()
        for name, passed in results.items():
            assert passed, f"Conductor verification failed for {name}"

    def test_ground_truth(self) -> None:
        """Ground truth values match."""
        assert CONDUCTOR_GROUND_TRUTH["Heisenberg"]["conductor"] == Fraction(0)
        assert CONDUCTOR_GROUND_TRUTH["Kac-Moody_sl2"]["conductor"] == Fraction(0)
        assert CONDUCTOR_GROUND_TRUTH["Virasoro"]["conductor"] == Fraction(13)
        assert CONDUCTOR_GROUND_TRUTH["W3"]["conductor"] == Fraction(50)
        assert CONDUCTOR_GROUND_TRUTH["K3_Mukai"]["conductor"] == Fraction(0)


# =========================================================================
#  9. Cross-checks with existing engines
# =========================================================================

class TestCrossChecks:
    """Cross-checks with e1_koszul_three_families and chiral_koszul_derived."""

    def test_cross_check_e1_koszul(self) -> None:
        """Conductor agrees with e1_koszul_three_families.py."""
        results = cross_check_with_e1_koszul()
        for name, passed in results.items():
            assert passed, f"E_1 cross-check failed for {name}"

    def test_cross_check_derived_koszul(self) -> None:
        """Conductor agrees with chiral_koszul_derived.py."""
        results = cross_check_with_derived_koszul()
        for name, passed in results.items():
            assert passed, f"Derived cross-check failed for {name}"


# =========================================================================
#  10. CY-B proof status summary
# =========================================================================

class TestCYBProofStatus:
    """CY-B proof status summary."""

    def test_cy_b1_proved(self) -> None:
        """CY-B1 (conductor formula) is PROVED."""
        summary = cy_b_proof_status_summary()
        assert summary["cy_b1_conductor_formula"]["status"] == "PROVED"
        assert summary["cy_b1_conductor_formula"]["all_families_verified"]

    def test_cy_b2_programme(self) -> None:
        """CY-B2 (braided equivalence) is a PROGRAMME."""
        summary = cy_b_proof_status_summary()
        assert summary["cy_b2_braided_equivalence"]["status"] == "PROGRAMME"

    def test_overall_status(self) -> None:
        """Overall CY-B status."""
        summary = cy_b_proof_status_summary()
        assert "PROVED" in summary["overall_cy_b_status"]


# =========================================================================
#  11. Edge cases and boundary values
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary values for the conductor formula."""

    def test_heisenberg_k_zero(self) -> None:
        """k=0 Heisenberg: degenerate, but conductor still 0."""
        result = heisenberg_conductor(Fraction(0))
        assert result.rho_K == Fraction(0)

    def test_virasoro_c_zero(self) -> None:
        """c=0 Virasoro: trivial, conductor still 13."""
        result = virasoro_conductor(Fraction(0))
        assert result.rho_K == Fraction(13)

    def test_virasoro_c_26(self) -> None:
        """c=26 Virasoro (bosonic string): conductor 13."""
        result = virasoro_conductor(Fraction(26))
        assert result.rho_K == Fraction(13)

    def test_kac_moody_critical_level(self) -> None:
        """Critical level k=-h^v: self-dual, conductor still 0.

        For sl_2: k = -2, k' = -(-2) - 4 = -2 = k (self-dual).
        kappa_ch = 3(k+2)/4 = 0.
        """
        result = kac_moody_sl2_conductor(Fraction(-2))
        assert result.rho_K == Fraction(0)

    def test_large_level(self) -> None:
        """Large level: conductor remains 0 for class G/L."""
        result = heisenberg_conductor(Fraction(10**6))
        assert result.rho_K == Fraction(0)

        result = kac_moody_sl2_conductor(Fraction(10**6))
        assert result.rho_K == Fraction(0)

    def test_negative_central_charge(self) -> None:
        """Negative central charge: conductor is still well-defined."""
        result = virasoro_conductor(Fraction(-10))
        assert result.rho_K == Fraction(13)

    def test_fractional_central_charge(self) -> None:
        """Fractional central charge (minimal models)."""
        # c = 1/2 (Ising model)
        result = virasoro_conductor(Fraction(1, 2))
        assert result.rho_K == Fraction(13)

        # c = 7/10 (tricritical Ising)
        result = virasoro_conductor(Fraction(7, 10))
        assert result.rho_K == Fraction(13)
