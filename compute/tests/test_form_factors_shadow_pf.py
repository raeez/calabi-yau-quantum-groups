"""Tests for form factors via Koszul duality and the shadow partition function.

Verifies the connection between Costello-Paquette form factors (bulk-to-boundary
OPE via Koszul duality) and the shadow partition function Theta_A of Volume I.

GROUND TRUTH:

  Form factor truncation by shadow class:
    G: only 2-particle form factor nonzero
    L: up to 3-particle form factor
    C: finite truncation
    M: all form factors nonzero (Gevrey-1 divergent)

  Integrated form factors = shadow invariants:
    S_2 = kappa_ch (for all classes)
    S_3 = alpha (cubic shadow, classes L, M)
    S_4 = Q (quartic shadow, classes C, M)

  Koszul projection type:
    G: quasi-isomorphism
    L: single A_inf correction
    C: finite corrections
    M: infinite corrections (Gevrey-1, Borel summable)

  Conductor (Theorem C, Vol I):
    Heisenberg: K = 0
    Kac-Moody: K = 0
    Virasoro: K = 13

  K3 bar Euler product:
    prod(1-q^n)^{24} = eta^{24}/q = Delta/q
    First coefficients: 1, -24, 252, -1472, 4830, -6048

  Virasoro shadow tower (spin-2 channel, c=1):
    S_2 = 1/2, S_3 = 2, S_4 = 10/27

Manuscript references:
  chapters/connections/bar_cobar_bridge.tex: sec:form-factors-shadow-pf
  chapters/connections/modular_koszul_bridge.tex: sec:modular-conv-cy
"""

import pytest
from fractions import Fraction

from compute.lib.form_factors_shadow_pf import (
    FormFactorData,
    KoszulProjectionData,
    ShadowPFFromFormFactors,
    ETA24_COEFFICIENTS,
    SHADOW_CLASS_FF_BEHAVIOUR,
    SHADOW_CLASS_KOSZUL_PROJ,
    form_factor_class_g,
    form_factor_class_l,
    form_factor_class_m,
    form_factor_landscape,
    k3_bar_euler_from_form_factors,
    k3_mukai_form_factors,
    koszul_projection,
    koszul_projection_by_class,
    master_form_factor_shadow_verification,
    shadow_pf_from_form_factors,
    verify_ff_shadow_identity_class_g,
    verify_ff_shadow_identity_class_m,
    virasoro_form_factors,
)


# =========================================================================
# 1. Class G form factor tests
# =========================================================================

class TestClassGFormFactors:
    """Form factors for class G (Heisenberg-type) algebras."""

    def test_2_particle_ff_heisenberg_k1(self):
        """2-particle form factor of Heisenberg at k=1: S_2 = kappa_ch = 1."""
        ff = form_factor_class_g(Fraction(1), 2)
        assert ff.integrated_ff == Fraction(1)
        assert ff.is_nonzero
        assert ff.shadow_class == "G"
        assert ff.koszul_projection_type == "quasi_isomorphism"

    def test_2_particle_ff_heisenberg_k2(self):
        """2-particle form factor of Heisenberg at k=2: S_2 = 2."""
        ff = form_factor_class_g(Fraction(2), 2)
        assert ff.integrated_ff == Fraction(2)
        assert ff.is_nonzero

    def test_3_particle_ff_vanishes(self):
        """3-particle form factor vanishes for class G."""
        ff = form_factor_class_g(Fraction(1), 3)
        assert ff.integrated_ff == Fraction(0)
        assert not ff.is_nonzero

    def test_4_particle_ff_vanishes(self):
        """4-particle form factor vanishes for class G."""
        ff = form_factor_class_g(Fraction(5), 4)
        assert ff.integrated_ff == Fraction(0)
        assert not ff.is_nonzero

    def test_higher_ff_all_vanish(self):
        """All higher form factors vanish for class G."""
        for n in range(3, 8):
            ff = form_factor_class_g(Fraction(3), n)
            assert ff.integrated_ff == Fraction(0)
            assert not ff.is_nonzero

    def test_koszul_projection_is_qi(self):
        """Koszul projection is a quasi-isomorphism for class G."""
        ff = form_factor_class_g(Fraction(1), 2)
        assert ff.koszul_projection_type == "quasi_isomorphism"

    def test_zero_kappa_gives_zero_ff(self):
        """kappa_ch = 0 gives zero 2-particle form factor."""
        ff = form_factor_class_g(Fraction(0), 2)
        assert ff.integrated_ff == Fraction(0)
        assert not ff.is_nonzero

    def test_negative_kappa(self):
        """Negative kappa_ch gives negative form factor."""
        ff = form_factor_class_g(Fraction(-3), 2)
        assert ff.integrated_ff == Fraction(-3)
        assert ff.is_nonzero

    def test_fractional_kappa(self):
        """Fractional kappa_ch works correctly."""
        ff = form_factor_class_g(Fraction(1, 2), 2)
        assert ff.integrated_ff == Fraction(1, 2)

    def test_invalid_n_particles(self):
        """n_particles < 2 raises ValueError."""
        with pytest.raises(ValueError):
            form_factor_class_g(Fraction(1), 1)


# =========================================================================
# 2. Class L form factor tests
# =========================================================================

class TestClassLFormFactors:
    """Form factors for class L (Kac-Moody type) algebras."""

    def test_2_particle_ff(self):
        """2-particle form factor for class L: S_2 = kappa_ch."""
        ff = form_factor_class_l(Fraction(9, 4), Fraction(-1), 2)
        assert ff.integrated_ff == Fraction(9, 4)
        assert ff.shadow_class == "L"

    def test_3_particle_ff_nonzero(self):
        """3-particle form factor is nonzero for class L (first loop)."""
        ff = form_factor_class_l(Fraction(9, 4), Fraction(-1), 3)
        assert ff.integrated_ff == Fraction(-1)
        assert ff.is_nonzero

    def test_3_particle_equals_alpha(self):
        """Integrated 3-particle form factor = cubic shadow alpha."""
        alpha = Fraction(7, 3)
        ff = form_factor_class_l(Fraction(2), alpha, 3)
        assert ff.integrated_ff == alpha

    def test_4_particle_vanishes(self):
        """4-particle form factor vanishes for class L."""
        ff = form_factor_class_l(Fraction(9, 4), Fraction(-1), 4)
        assert ff.integrated_ff == Fraction(0)
        assert not ff.is_nonzero

    def test_5_particle_vanishes(self):
        """5-particle form factor vanishes for class L."""
        ff = form_factor_class_l(Fraction(9, 4), Fraction(-1), 5)
        assert ff.integrated_ff == Fraction(0)

    def test_koszul_projection_single_correction(self):
        """Koszul projection has single A_inf correction for class L."""
        ff = form_factor_class_l(Fraction(2), Fraction(1), 3)
        assert ff.koszul_projection_type == "single_correction"

    def test_zero_alpha_gives_zero_3_particle(self):
        """alpha = 0 gives zero 3-particle form factor."""
        ff = form_factor_class_l(Fraction(2), Fraction(0), 3)
        assert ff.integrated_ff == Fraction(0)
        assert not ff.is_nonzero


# =========================================================================
# 3. Class M form factor tests
# =========================================================================

class TestClassMFormFactors:
    """Form factors for class M (Virasoro type) algebras."""

    def test_2_particle_ff_equals_kappa(self):
        """2-particle form factor = kappa_ch for class M."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        ff = form_factor_class_m(Fraction(1, 2), coeffs, 2)
        assert ff.integrated_ff == Fraction(1, 2)
        assert ff.shadow_class == "M"

    def test_3_particle_ff_nonzero(self):
        """3-particle form factor is nonzero for class M."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        ff = form_factor_class_m(Fraction(1, 2), coeffs, 3)
        assert ff.integrated_ff == Fraction(2)
        assert ff.is_nonzero

    def test_4_particle_ff_nonzero(self):
        """4-particle form factor is nonzero for class M."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        ff = form_factor_class_m(Fraction(1, 2), coeffs, 4)
        assert ff.integrated_ff == Fraction(10, 27)
        assert ff.is_nonzero

    def test_virasoro_shadow_coefficients(self):
        """Virasoro shadow coefficients match a_infinity_bar_w1inf.py ground truth."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        ff2 = form_factor_class_m(Fraction(1, 2), coeffs, 2)
        ff3 = form_factor_class_m(Fraction(1, 2), coeffs, 3)
        ff4 = form_factor_class_m(Fraction(1, 2), coeffs, 4)
        assert ff2.integrated_ff == Fraction(1, 2)
        assert ff3.integrated_ff == Fraction(2)
        assert ff4.integrated_ff == Fraction(10, 27)

    def test_koszul_projection_infinite(self):
        """Koszul projection has infinite corrections for class M."""
        coeffs = {3: Fraction(2)}
        ff = form_factor_class_m(Fraction(1, 2), coeffs, 3)
        assert ff.koszul_projection_type == "infinite_corrections"

    def test_missing_coefficient_gives_zero(self):
        """Missing shadow coefficient gives zero form factor at that arity."""
        coeffs = {3: Fraction(2)}  # No S_5
        ff = form_factor_class_m(Fraction(1, 2), coeffs, 5)
        assert ff.integrated_ff == Fraction(0)


# =========================================================================
# 4. Virasoro form factors
# =========================================================================

class TestVirasoroFormFactors:
    """Virasoro algebra form factors at central charge c."""

    def test_virasoro_c1_kappa(self):
        """Virasoro at c=1: kappa_ch = 1/2."""
        ffs = virasoro_form_factors(Fraction(1), 4)
        assert ffs[2].kappa_ch == Fraction(1, 2)

    def test_virasoro_c1_2_particle(self):
        """Virasoro at c=1: S_2 = 1/2."""
        ffs = virasoro_form_factors(Fraction(1), 4)
        assert ffs[2].integrated_ff == Fraction(1, 2)

    def test_virasoro_c1_3_particle(self):
        """Virasoro at c=1: S_3 = alpha = 2."""
        ffs = virasoro_form_factors(Fraction(1), 4)
        assert ffs[3].integrated_ff == Fraction(2)

    def test_virasoro_c1_4_particle(self):
        """Virasoro at c=1: S_4 = 10/27."""
        ffs = virasoro_form_factors(Fraction(1), 5)
        assert ffs[4].integrated_ff == Fraction(10, 27)

    def test_virasoro_all_class_m(self):
        """All Virasoro form factors are class M."""
        ffs = virasoro_form_factors(Fraction(1), 5)
        for n in ffs:
            assert ffs[n].shadow_class == "M"


# =========================================================================
# 5. K3 form factors
# =========================================================================

class TestK3FormFactors:
    """K3 Mukai Heisenberg and bar Euler product."""

    def test_k3_mukai_kappa_ch(self):
        """K3 Mukai kappa_ch = 2 (NOT kappa_BKM = 5; AP113)."""
        ffs = k3_mukai_form_factors(4)
        assert ffs[2].kappa_ch == Fraction(2)

    def test_k3_mukai_2_particle_nonzero(self):
        """K3 Mukai 2-particle form factor is nonzero."""
        ffs = k3_mukai_form_factors(4)
        assert ffs[2].is_nonzero
        assert ffs[2].integrated_ff == Fraction(2)

    def test_k3_mukai_3_particle_zero(self):
        """K3 Mukai 3-particle form factor vanishes (class G)."""
        ffs = k3_mukai_form_factors(4)
        assert not ffs[3].is_nonzero

    def test_k3_mukai_class_g(self):
        """K3 Mukai Heisenberg is class G."""
        ffs = k3_mukai_form_factors(4)
        assert ffs[2].shadow_class == "G"

    def test_k3_bar_euler_coefficients(self):
        """Bar Euler product coefficients match Ramanujan tau."""
        result = k3_bar_euler_from_form_factors(6)
        assert result["matches_known_tau"]

    def test_k3_bar_euler_first_coefficients(self):
        """First coefficients: 1, -24, 252, -1472, 4830, -6048."""
        result = k3_bar_euler_from_form_factors(6)
        coeffs = result["eta24_coefficients"]
        assert coeffs[0] == 1
        assert coeffs[1] == -24
        assert coeffs[2] == 252
        assert coeffs[3] == -1472
        assert coeffs[4] == 4830
        assert coeffs[5] == -6048

    def test_k3_total_2_particle_ff(self):
        """Total 2-particle form factor = 24 (rank of Mukai lattice)."""
        result = k3_bar_euler_from_form_factors(6)
        assert result["total_2_particle_ff"] == Fraction(24)

    def test_k3_per_generator_ff(self):
        """Per-generator form factor = 1 (rank-1 Heisenberg)."""
        result = k3_bar_euler_from_form_factors(6)
        assert result["per_generator_ff"] == Fraction(1)

    def test_k3_rank_vs_kappa(self):
        """K3: rank = 24 != kappa_ch = 2. Bar Euler uses rank."""
        result = k3_bar_euler_from_form_factors(6)
        assert result["rank"] == 24
        assert result["kappa_ch_mukai"] == Fraction(2)
        assert result["rank"] != int(result["kappa_ch_mukai"])

    def test_k3_bar_euler_ok(self):
        """K3 bar Euler verification passes."""
        result = k3_bar_euler_from_form_factors(6)
        assert result["ok"]


# =========================================================================
# 6. Form factor -- shadow PF identity tests
# =========================================================================

class TestFFShadowIdentity:
    """Form factor -- shadow partition function identity."""

    def test_class_g_identity_kappa_1(self):
        """Class G identity at kappa_ch = 1."""
        result = verify_ff_shadow_identity_class_g(Fraction(1))
        assert result["ok"]
        assert result["s2_equals_kappa"]
        assert result["higher_ff_vanish"]

    def test_class_g_identity_kappa_2(self):
        """Class G identity at kappa_ch = 2."""
        result = verify_ff_shadow_identity_class_g(Fraction(2))
        assert result["ok"]

    def test_class_g_identity_kappa_24(self):
        """Class G identity at kappa_ch = 24 (K3 lattice rank)."""
        result = verify_ff_shadow_identity_class_g(Fraction(24))
        assert result["ok"]

    def test_class_g_s2_equals_kappa(self):
        """S_2 = kappa_ch for class G."""
        result = verify_ff_shadow_identity_class_g(Fraction(7))
        assert result["S_2"] == Fraction(7)

    def test_class_g_higher_vanish(self):
        """S_3 = S_4 = 0 for class G."""
        result = verify_ff_shadow_identity_class_g(Fraction(3))
        assert result["S_3"] == Fraction(0)
        assert result["S_4"] == Fraction(0)

    def test_class_g_ff_determines_shadow_pf(self):
        """Form factor (S_2 only) determines entire shadow PF for class G."""
        result = verify_ff_shadow_identity_class_g(Fraction(5))
        assert result["ff_determines_shadow_pf"]

    def test_class_m_identity_virasoro(self):
        """Class M identity for Virasoro at c=1."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        result = verify_ff_shadow_identity_class_m(Fraction(1, 2), coeffs)
        assert result["ok"]

    def test_class_m_s2_equals_kappa(self):
        """S_2 = kappa_ch for class M."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        result = verify_ff_shadow_identity_class_m(Fraction(1, 2), coeffs)
        assert result["s2_equals_kappa"]

    def test_class_m_s3_nonzero(self):
        """S_3 nonzero for class M (first loop correction)."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        result = verify_ff_shadow_identity_class_m(Fraction(1, 2), coeffs)
        assert result["s3_nonzero"]

    def test_class_m_convergence_type(self):
        """Class M convergence type is Gevrey-1 divergent."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        result = verify_ff_shadow_identity_class_m(Fraction(1, 2), coeffs)
        assert result["convergence_type"] == "gevrey_1_divergent"

    def test_class_m_borel_summable(self):
        """Class M form factor series is Borel summable."""
        coeffs = {3: Fraction(2)}
        result = verify_ff_shadow_identity_class_m(Fraction(1, 2), coeffs)
        assert result["borel_summable"]


# =========================================================================
# 7. Koszul projection tests
# =========================================================================

class TestKoszulProjection:
    """Koszul projection pi: Obs_bulk -> Obs_boundary^!."""

    def test_class_g_is_qi(self):
        """Class G: Koszul projection is a quasi-isomorphism."""
        proj = koszul_projection_by_class("G")
        assert proj["is_quasi_isomorphism"]

    def test_class_l_not_qi(self):
        """Class L: Koszul projection is NOT a quasi-isomorphism."""
        proj = koszul_projection_by_class("L")
        assert not proj["is_quasi_isomorphism"]

    def test_class_m_not_qi(self):
        """Class M: Koszul projection is NOT a quasi-isomorphism."""
        proj = koszul_projection_by_class("M")
        assert not proj["is_quasi_isomorphism"]

    def test_class_g_zero_corrections(self):
        """Class G: zero A_inf corrections."""
        proj = koszul_projection_by_class("G")
        assert proj["ainf_corrections"] == 0

    def test_class_l_one_correction(self):
        """Class L: single A_inf correction (m_3)."""
        proj = koszul_projection_by_class("L")
        assert proj["ainf_corrections"] == 1

    def test_class_m_infinite_corrections(self):
        """Class M: infinite A_inf corrections."""
        proj = koszul_projection_by_class("M")
        assert proj["ainf_corrections"] == "infinite"

    def test_class_g_max_2_particles(self):
        """Class G: max 2 particles in form factors."""
        proj = koszul_projection_by_class("G")
        assert proj["max_ff_particles"] == 2

    def test_class_l_max_3_particles(self):
        """Class L: max 3 particles in form factors."""
        proj = koszul_projection_by_class("L")
        assert proj["max_ff_particles"] == 3

    def test_class_m_infinite_particles(self):
        """Class M: infinite form factor particles."""
        proj = koszul_projection_by_class("M")
        assert proj["max_ff_particles"] == "infinite"

    def test_all_classes_ok(self):
        """All four shadow classes pass Koszul projection verification."""
        for cls in ["G", "L", "C", "M"]:
            proj = koszul_projection_by_class(cls)
            assert proj["ok"]


# =========================================================================
# 8. Conductor tests
# =========================================================================

class TestConductor:
    """Koszul conductor K = kappa_ch(A) + kappa_ch(A^!)."""

    def test_heisenberg_conductor_zero(self):
        """Heisenberg: K = 0 (free-field anti-symmetry)."""
        proj = koszul_projection("Heisenberg", "G", Fraction(1), Fraction(-1))
        assert proj.conductor == Fraction(0)

    def test_virasoro_conductor_13(self):
        """Virasoro: K = 13 (c/2 + (26-c)/2 = 13)."""
        proj = koszul_projection("Virasoro", "M", Fraction(1, 2), Fraction(25, 2))
        assert proj.conductor == Fraction(13)

    def test_k3_mukai_conductor_zero(self):
        """K3 Mukai: K = 0 (lattice VOA, free-field branch)."""
        proj = koszul_projection("K3_Mukai", "G", Fraction(2), Fraction(-2))
        assert proj.conductor == Fraction(0)

    def test_yangian_conductor_zero(self):
        """Yangian: K = 0."""
        proj = koszul_projection("Yangian", "L", Fraction(0), Fraction(0))
        assert proj.conductor == Fraction(0)

    def test_virasoro_c26_conductor_13(self):
        """Virasoro at c=26: K = 13 (26/2 + 0/2 = 13)."""
        proj = koszul_projection("Virasoro_26", "M", Fraction(13), Fraction(0))
        assert proj.conductor == Fraction(13)


# =========================================================================
# 9. Shadow PF reconstruction tests
# =========================================================================

class TestShadowPFReconstruction:
    """Shadow partition function reconstruction from form factors."""

    def test_class_g_truncation(self):
        """Class G: exact truncation at arity 2."""
        spf = shadow_pf_from_form_factors(
            "Heisenberg_1", "G", Fraction(1), {}
        )
        assert spf.max_nonzero_arity == 2
        assert spf.convergence_type == "exact_truncation"

    def test_class_l_truncation(self):
        """Class L: exact truncation at arity 3."""
        spf = shadow_pf_from_form_factors(
            "KM_sl2", "L", Fraction(9, 4), {3: Fraction(-1)}
        )
        assert spf.max_nonzero_arity == 3
        assert spf.convergence_type == "exact_truncation"

    def test_class_m_no_truncation(self):
        """Class M: no truncation (infinite depth)."""
        spf = shadow_pf_from_form_factors(
            "Virasoro_1", "M", Fraction(1, 2), {3: Fraction(2), 4: Fraction(10, 27)}
        )
        assert spf.max_nonzero_arity is None
        assert spf.convergence_type == "gevrey_1_divergent"

    def test_shadow_invariants_include_kappa(self):
        """Shadow invariants always include S_2 = kappa_ch."""
        spf = shadow_pf_from_form_factors(
            "Test", "G", Fraction(7), {}
        )
        assert spf.shadow_invariants[2] == Fraction(7)

    def test_class_g_bar_euler_uniform(self):
        """Class G: bar Euler exponents are uniform (all = kappa_ch)."""
        spf = shadow_pf_from_form_factors(
            "Heisenberg_3", "G", Fraction(3), {}, 6
        )
        for k in range(1, 7):
            assert spf.bar_euler_exponents[k] == 3


# =========================================================================
# 10. Partition function coefficient tests
# =========================================================================

class TestPartitionFunctionCoefficients:
    """Coefficients of prod(1-q^n)^a."""

    def test_eta24_first_coefficients(self):
        """eta^{24} first coefficients match known values."""
        result = k3_bar_euler_from_form_factors(6)
        coeffs = result["eta24_coefficients"]
        for k, v in ETA24_COEFFICIENTS.items():
            if k <= 6:
                assert coeffs[k] == v, f"Mismatch at q^{k}: {coeffs[k]} != {v}"

    def test_eta1_coefficients(self):
        """prod(1-q^n)^1 = 1 - q - q^2 + q^5 + q^7 - ..."""
        # Euler's pentagonal number theorem
        result = verify_ff_shadow_identity_class_g(Fraction(1), 8)
        coeffs = result["shadow_pf_first_coeffs"]
        assert coeffs[0] == Fraction(1)
        assert coeffs[1] == Fraction(-1)
        assert coeffs[2] == Fraction(-1)
        assert coeffs[3] == Fraction(0)
        # q^4: 0, q^5: 1 (pentagonal number theorem)
        assert coeffs[4] == Fraction(0)
        assert coeffs[5] == Fraction(1)


# =========================================================================
# 11. Form factor landscape tests
# =========================================================================

class TestFormFactorLandscape:
    """Cross-class form factor landscape."""

    def test_landscape_ok(self):
        """Form factor landscape passes all checks."""
        result = form_factor_landscape(6)
        assert result["ok"]

    def test_landscape_has_all_classes(self):
        """Landscape includes G, G_K3, L, M."""
        result = form_factor_landscape(6)
        assert "G" in result
        assert "G_K3" in result
        assert "L" in result
        assert "M" in result

    def test_landscape_class_l_truncation(self):
        """Class L in landscape: 4-particle form factor vanishes."""
        result = form_factor_landscape(6)
        assert result["L"]["ff_4"].integrated_ff == Fraction(0)

    def test_landscape_class_l_3_particle_nonzero(self):
        """Class L in landscape: 3-particle form factor is nonzero."""
        result = form_factor_landscape(6)
        assert result["L"]["ff_3"].is_nonzero


# =========================================================================
# 12. Ground truth consistency tests
# =========================================================================

class TestGroundTruth:
    """Consistency with ground truth from other engines."""

    def test_heisenberg_ground_truth(self):
        """Heisenberg H_1: S_2=1, S_3=0, S_4=0 (ground truth)."""
        ff2 = form_factor_class_g(Fraction(1), 2)
        ff3 = form_factor_class_g(Fraction(1), 3)
        ff4 = form_factor_class_g(Fraction(1), 4)
        assert ff2.integrated_ff == Fraction(1)
        assert ff3.integrated_ff == Fraction(0)
        assert ff4.integrated_ff == Fraction(0)

    def test_virasoro_ground_truth(self):
        """Virasoro Vir_1: S_2=1/2, S_3=2, S_4=10/27 (ground truth)."""
        coeffs = {3: Fraction(2), 4: Fraction(10, 27)}
        ff2 = form_factor_class_m(Fraction(1, 2), coeffs, 2)
        ff3 = form_factor_class_m(Fraction(1, 2), coeffs, 3)
        ff4 = form_factor_class_m(Fraction(1, 2), coeffs, 4)
        assert ff2.integrated_ff == Fraction(1, 2)
        assert ff3.integrated_ff == Fraction(2)
        assert ff4.integrated_ff == Fraction(10, 27)

    def test_k3_rank_24(self):
        """K3 Yangian: rank 24, bar Euler exponent 24."""
        result = k3_bar_euler_from_form_factors(4)
        assert result["rank"] == 24

    def test_shadow_class_behaviour_dict(self):
        """SHADOW_CLASS_FF_BEHAVIOUR has all four classes."""
        assert len(SHADOW_CLASS_FF_BEHAVIOUR) == 4
        assert "G" in SHADOW_CLASS_FF_BEHAVIOUR
        assert "L" in SHADOW_CLASS_FF_BEHAVIOUR
        assert "C" in SHADOW_CLASS_FF_BEHAVIOUR
        assert "M" in SHADOW_CLASS_FF_BEHAVIOUR


# =========================================================================
# 13. Master verification test
# =========================================================================

class TestMasterVerification:
    """Master form factor--shadow PF verification."""

    def test_master_ok(self):
        """Master verification passes."""
        result = master_form_factor_shadow_verification(6)
        assert result["ok"]

    def test_master_class_g_identity(self):
        """Master: class G identity passes."""
        result = master_form_factor_shadow_verification(6)
        assert result["class_g_identity"]["ok"]

    def test_master_k3_bar_euler(self):
        """Master: K3 bar Euler passes."""
        result = master_form_factor_shadow_verification(6)
        assert result["k3_bar_euler"]["ok"]

    def test_master_k3_mukai_ffs(self):
        """Master: K3 Mukai form factors pass."""
        result = master_form_factor_shadow_verification(6)
        assert result["k3_mukai_ffs"]["ok"]

    def test_master_class_m_identity(self):
        """Master: class M identity passes."""
        result = master_form_factor_shadow_verification(6)
        assert result["class_m_identity"]["ok"]

    def test_master_conductor_heisenberg(self):
        """Master: Heisenberg conductor K = 0."""
        result = master_form_factor_shadow_verification(6)
        assert result["conductor_heisenberg"]["ok"]

    def test_master_conductor_virasoro(self):
        """Master: Virasoro conductor K = 13."""
        result = master_form_factor_shadow_verification(6)
        assert result["conductor_virasoro"]["ok"]

    def test_master_shadow_pf_g(self):
        """Master: shadow PF reconstruction class G."""
        result = master_form_factor_shadow_verification(6)
        assert result["shadow_pf_reconstruction_G"]["ok"]

    def test_master_shadow_pf_m(self):
        """Master: shadow PF reconstruction class M."""
        result = master_form_factor_shadow_verification(6)
        assert result["shadow_pf_reconstruction_M"]["ok"]

    def test_master_landscape(self):
        """Master: form factor landscape passes."""
        result = master_form_factor_shadow_verification(6)
        assert result["landscape"]["ok"]


# =========================================================================
# 14. Multi-path cross-checks against other engines (AP10)
# =========================================================================

class TestCrossEngineVerification:
    """Cross-engine verification: form factor results must agree with
    independent computations from other Vol III engines.

    These tests import from sibling engines and verify that the form
    factor shadow PF engine produces values consistent with independent
    calculations.  Each test computes the same quantity via TWO DIFFERENT
    PATHS and asserts equality.
    """

    def test_k3_eta24_vs_k3_yangian_engine(self):
        """Cross-check: eta^{24} coefficients from form_factors_shadow_pf
        must match k3_yangian.bar_euler_product_yangian.

        Path 1: form_factors_shadow_pf._partition_function_coefficients(24, N)
        Path 2: k3_yangian.bar_euler_product_yangian(N)
        """
        from compute.lib.form_factors_shadow_pf import _partition_function_coefficients
        from compute.lib.k3_yangian import bar_euler_product_yangian

        ff_coeffs = _partition_function_coefficients(24, 8)
        k3_coeffs = bar_euler_product_yangian(8)

        for n in range(9):
            assert ff_coeffs[n] == k3_coeffs.get(n, 0), (
                f"eta^{{24}} coefficient mismatch at q^{n}: "
                f"form_factor={ff_coeffs[n]}, k3_yangian={k3_coeffs.get(n, 0)}"
            )

    def test_virasoro_shadow_vs_a_infinity_bar(self):
        """Cross-check: Virasoro shadow coefficients from form factors must
        match a_infinity_bar_w1inf shadow tower data.

        Path 1: form_factors_shadow_pf.virasoro_form_factors(c=1)
        Path 2: a_infinity_bar_w1inf.AInfShadowTower (independent computation)
                alpha_per_channel()[2] = 2, S4_per_channel()[2] = 10/27
        """
        from compute.lib.a_infinity_bar_w1inf import (
            AInfBarComplex,
            AInfShadowTower,
            W1InfOPE,
        )

        # Path 1: form factor engine
        ffs = virasoro_form_factors(Fraction(1), 5)
        ff_s3 = ffs[3].integrated_ff  # Should be alpha = 2
        ff_s4 = ffs[4].integrated_ff  # Should be S_4 = 10/27

        # Path 2: a_infinity_bar engine (independent computation)
        ope = W1InfOPE(c=Fraction(1))
        bar_cx = AInfBarComplex(ope=ope)
        shadow = AInfShadowTower(bar_cx, max_spin=3)

        # Spin-2 channel alpha (cubic shadow)
        alpha_from_ainf = shadow.alpha_per_channel()[2]
        assert ff_s3 == alpha_from_ainf, (
            f"S_3 mismatch: form_factor={ff_s3}, a_infinity={alpha_from_ainf}"
        )

        # Spin-2 channel S_4 (quartic shadow)
        s4_from_ainf = shadow.S4_per_channel()[2]
        assert ff_s4 == s4_from_ainf, (
            f"S_4 mismatch: form_factor={ff_s4}, a_infinity={s4_from_ainf}"
        )

    def test_conductor_vs_chiral_koszul_derived(self):
        """Cross-check: Koszul conductors from form_factors_shadow_pf must
        match chiral_koszul_derived ground truth.

        Path 1: koszul_projection() from this engine
        Path 2: CONDUCTOR_GROUND_TRUTH from chiral_koszul_derived
        """
        from compute.lib.chiral_koszul_derived import CONDUCTOR_GROUND_TRUTH as CKD_CONDUCTORS

        # Heisenberg: K = 0
        heis_proj = koszul_projection("Heisenberg", "G", Fraction(1), Fraction(-1))
        assert heis_proj.conductor == CKD_CONDUCTORS["Heisenberg"], (
            f"Heisenberg conductor mismatch: {heis_proj.conductor} vs {CKD_CONDUCTORS['Heisenberg']}"
        )

        # Virasoro: K = 13
        vir_proj = koszul_projection("Virasoro", "M", Fraction(1, 2), Fraction(25, 2))
        assert vir_proj.conductor == CKD_CONDUCTORS["Virasoro"], (
            f"Virasoro conductor mismatch: {vir_proj.conductor} vs {CKD_CONDUCTORS['Virasoro']}"
        )

        # Yangian: K = 0
        yang_proj = koszul_projection("Yangian", "L", Fraction(0), Fraction(0))
        assert yang_proj.conductor == CKD_CONDUCTORS["Yangian"], (
            f"Yangian conductor mismatch: {yang_proj.conductor} vs {CKD_CONDUCTORS['Yangian']}"
        )

    def test_kappa_ch_vs_cross_volume_bridge(self):
        """Cross-check: kappa_ch values from form factors must match
        cross_volume_shadow_bridge authoritative formulas.

        Path 1: form_factor_class_g(kappa_ch=k, 2).integrated_ff
        Path 2: cross_volume_shadow_bridge.kappa_heisenberg(k)
        """
        from compute.lib.cross_volume_shadow_bridge import kappa_heisenberg

        for k in [1, 2, 3, 5, 24]:
            # Path 1: form factor
            ff = form_factor_class_g(Fraction(k), 2)
            # Path 2: cross-volume bridge
            kappa_cv = kappa_heisenberg(Fraction(k))
            assert ff.integrated_ff == kappa_cv, (
                f"kappa_ch mismatch at k={k}: form_factor={ff.integrated_ff}, "
                f"cross_volume={kappa_cv}"
            )

    def test_shadow_class_vs_derived_koszul(self):
        """Cross-check: shadow class -> derived behaviour mapping agrees
        with chiral_koszul_derived.SHADOW_CLASS_DERIVED.

        Path 1: SHADOW_CLASS_FF_BEHAVIOUR from this engine
        Path 2: SHADOW_CLASS_DERIVED from chiral_koszul_derived
        """
        from compute.lib.chiral_koszul_derived import SHADOW_CLASS_DERIVED

        # Both dictionaries must cover the same four classes
        assert set(SHADOW_CLASS_FF_BEHAVIOUR.keys()) == set(SHADOW_CLASS_DERIVED.keys())

        # Class G: both should indicate exact/formal/truncated
        assert "truncated" in SHADOW_CLASS_FF_BEHAVIOUR["G"]
        assert "classical_exact" == SHADOW_CLASS_DERIVED["G"]

        # Class M: both should indicate infinite/Gevrey
        assert "infinite" in SHADOW_CLASS_FF_BEHAVIOUR["M"]
        assert "gevrey" in SHADOW_CLASS_DERIVED["M"]

    def test_k3_kappa_ch_spectrum(self):
        """Cross-check: K3 kappa spectrum values (AP113).

        The K3 kappa-spectrum has four distinct values:
            kappa_ch = 2 (from chiral algebra via Phi, NOT 5)
            kappa_BKM = 5 (Borcherds-Kac-Moody)
            kappa_cat = 2 (chi(O_{K3}))
            kappa_fiber = 24 (lattice rank)

        Verify: kappa_ch from form factors matches kappa_cat.
        Verify: bar Euler exponent = kappa_fiber = 24.
        """
        k3_ffs = k3_mukai_form_factors(3)
        k3_bar = k3_bar_euler_from_form_factors(4)

        # kappa_ch = 2 = kappa_cat (AP113)
        assert k3_ffs[2].kappa_ch == Fraction(2)

        # Bar Euler exponent = 24 = kappa_fiber (lattice rank)
        assert k3_bar["rank"] == 24

        # kappa_ch != kappa_BKM (AP113: these are DIFFERENT kappas)
        kappa_ch = k3_ffs[2].kappa_ch
        kappa_bkm = Fraction(5)
        assert kappa_ch != kappa_bkm, (
            "kappa_ch should not equal kappa_BKM for K3"
        )

        # kappa_ch != kappa_fiber
        kappa_fiber = Fraction(24)
        assert kappa_ch != kappa_fiber, (
            "kappa_ch (=2) should not equal kappa_fiber (=24)"
        )

    def test_pentagonal_theorem_independent(self):
        """Cross-check: prod(1-q^n)^1 via form factor engine matches
        Euler's pentagonal number theorem computed independently.

        Path 1: _partition_function_coefficients(1, N)
        Path 2: Independent pentagonal number computation

        Euler's theorem: prod(1-q^n) = sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}
        """
        from compute.lib.form_factors_shadow_pf import _partition_function_coefficients

        coeffs = _partition_function_coefficients(1, 12)

        # Independent pentagonal number computation
        pent = [0] * 13
        for k in range(-6, 7):
            idx = k * (3 * k - 1) // 2
            if 0 <= idx <= 12:
                pent[idx] += (-1) ** k

        for n in range(13):
            assert coeffs[n] == pent[n], (
                f"Pentagonal mismatch at q^{n}: engine={coeffs[n]}, pentagonal={pent[n]}"
            )

    def test_k3_mukai_rank_vs_k3_double_current(self):
        """Cross-check: Mukai rank from form factors matches
        k3_double_current_algebra.MUKAI_RANK.

        Path 1: k3_bar_euler_from_form_factors()["rank"]
        Path 2: k3_double_current_algebra.MUKAI_RANK
        """
        from compute.lib.k3_double_current_algebra import MUKAI_RANK

        k3_bar = k3_bar_euler_from_form_factors(4)
        assert k3_bar["rank"] == MUKAI_RANK, (
            f"Mukai rank mismatch: form_factor={k3_bar['rank']}, "
            f"k3_double_current={MUKAI_RANK}"
        )
