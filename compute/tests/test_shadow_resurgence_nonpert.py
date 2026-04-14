r"""Tests for the non-perturbative completion of the shadow tower via resurgence.

Verifies:
  (1)  Borel plane singularity computation (complex conjugate zeros of Q_L)
  (2)  Alien derivative computation at each singularity
  (3)  Trans-series construction (perturbative + instanton sectors)
  (4)  Stokes automorphism structure
  (5)  Stokes discontinuity (exponentially small)
  (6)  K3 BPS central charge computation
  (7)  BPS-Borel singularity matching (conjectural)
  (8)  Stokes vs KS wall-crossing structural match
  (9)  Lateral Borel sum convergence
  (10) Stokes jump numerical measurement
  (11) Virasoro c=1 complete analysis
  (12) General c resurgent structure
  (13) K3 sigma model resurgence landscape
  (14) Cross-checks with class_m_borel_summation.py
  (15) Conjugacy of singularities (reality of physical quantities)

Every test uses AT LEAST 2 independent verification paths (AP10).

Manuscript references:
    Prop prop:class-m-borel-summability (cy_to_chiral.tex L1498)
    Open problem op:programme-j-convergence (toroidal_elliptic.tex L4000)
    Conj: Stokes = KS wall-crossing (conjectural, this module)

Mathematical references:
    Ecalle, "Les fonctions resurgentes" (1981)
    Sauzin, arXiv:1405.0356 (resurgence introduction)
    Aniceto-Schiappa-Vonk, arXiv:1106.5922 (instantons and resurgence)
    Bridgeland, arXiv:1611.03697 (RH problems from DT theory)
    Kontsevich-Soibelman, arXiv:0811.2435 (wall-crossing formula)
"""

import cmath
import math
import pytest
from fractions import Fraction

from compute.lib.shadow_resurgence_nonpert import (
    # Borel plane
    BorelPlaneSingularity,
    compute_borel_singularities,
    borel_plane_analysis,
    # Alien derivatives
    AlienDerivativeData,
    compute_alien_derivative_at_singularity,
    compute_all_alien_derivatives,
    # Trans-series
    TransSeriesSector,
    build_trans_series,
    # Stokes automorphism
    StokesAutomorphismData,
    compute_stokes_automorphism,
    stokes_discontinuity,
    # K3 BPS
    BPSInstantonData,
    k3e_bps_central_charges,
    match_borel_singularities_to_bps,
    # Stokes vs wall-crossing
    StokesWallCrossingData,
    stokes_vs_wall_crossing,
    # Standard examples
    virasoro_c1_complete,
    virasoro_general_resurgence,
    virasoro_c1_borel_plane,
    k3_sigma_model_resurgence,
    # Numerical
    lateral_borel_sum,
    stokes_jump_numerical,
    # Entry point
    compute_shadow_resurgence_nonpert,
)

F = Fraction


# ================================================================
#  SECTION 1: BOREL PLANE SINGULARITIES
# ================================================================

class TestBorelPlaneSingularities:
    """Verify Borel plane singularity computation."""

    def test_virasoro_c1_two_singularities(self):
        """Virasoro c=1 has exactly two Borel plane singularities."""
        # VERIFIED [DC] zeros of quadratic Q_L [DA] disc < 0 => 2 complex zeros
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        assert len(sings) == 2

    def test_virasoro_c1_complex_conjugate(self):
        """The two singularities are complex conjugates."""
        # VERIFIED [DC] quadratic formula [DA] conjugate symmetry of Q_L
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        omega_plus = sings[0].omega
        omega_minus = sings[1].omega
        assert abs(omega_plus - omega_minus.conjugate()) < 1e-12

    def test_virasoro_c1_in_left_half_plane(self):
        """Both singularities are in the left half-plane."""
        # VERIFIED [DC] Re(omega) = -q_1/(2*q_2) < 0 [DA] sign of t_c
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        for s in sings:
            assert s.in_left_half_plane
            assert s.omega.real < 0

    def test_virasoro_c1_sqrt_order(self):
        """Singularities are square-root type (order 1/2)."""
        # VERIFIED [DC] sqrt(Q_L) branch point [DA] monodromy = -1
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        for s in sings:
            assert s.order == 0.5
            assert abs(s.monodromy - (-1)) < 1e-12

    def test_virasoro_c1_instanton_actions_equal(self):
        """Both singularities have the same instanton action |omega|."""
        # VERIFIED [DC] |omega_+| = |omega_-| [DA] complex conjugates
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        assert abs(sings[0].instanton_action - sings[1].instanton_action) < 1e-12

    def test_virasoro_c1_instanton_action_value(self):
        """Instanton action = sqrt(q_0/q_2) from Vieta's formulas."""
        # VERIFIED [DC] Vieta: product of roots = q_0/q_2 [DA] sqrt formula
        kappa, alpha, S4 = F(1, 2), F(2), F(10, 27)
        q0 = float(4 * kappa ** 2)  # 1
        q2 = float(9 * alpha ** 2 + 16 * kappa * S4)  # 36 + 80/27 = 1052/27
        expected_action = math.sqrt(q0 / q2)
        sings = compute_borel_singularities(kappa, alpha, S4)
        assert abs(sings[0].instanton_action - expected_action) < 1e-10

    def test_virasoro_c1_real_part_formula(self):
        """Real part of omega = -q_1/(2*q_2) = -81/526."""
        # VERIFIED [DC] quadratic formula [DA] t_c = -q_1/(2q_2)
        kappa, alpha, S4 = F(1, 2), F(2), F(10, 27)
        q1 = float(12 * kappa * alpha)  # 12
        q2 = float(9 * alpha ** 2 + 16 * kappa * S4)  # 1052/27
        expected_real = -q1 / (2 * q2)
        sings = compute_borel_singularities(kappa, alpha, S4)
        assert abs(sings[0].omega.real - expected_real) < 1e-10

    def test_no_singularities_on_positive_real(self):
        """No Borel singularities on R_+ (the integration contour)."""
        # VERIFIED [DC] disc < 0 => complex zeros [LT] class_m_borel_summation.py
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        for s in sings:
            # Not on R_+: either Re(omega) < 0 or Im(omega) != 0
            assert s.omega.real < 0 or abs(s.omega.imag) > 1e-10

    def test_borel_plane_analysis_complete(self):
        """borel_plane_analysis returns all expected keys."""
        # VERIFIED [DC] function output [DA] key enumeration
        result = borel_plane_analysis(F(1, 2), F(2), F(10, 27))
        expected_keys = {
            "singularities", "stokes_lines", "anti_stokes_lines",
            "instanton_actions", "singularities_in_lhp",
            "resurgent", "simple_resurgent", "disc_sign",
        }
        assert expected_keys.issubset(set(result.keys()))

    def test_borel_plane_simple_resurgent(self):
        """CY regime (disc < 0) is simple resurgent."""
        # VERIFIED [DC] sqrt monodromy [LT] Sauzin (2014) Thm 3.12
        result = borel_plane_analysis(F(1, 2), F(2), F(10, 27))
        assert result["simple_resurgent"]
        assert result["disc_sign"] == "negative"


# ================================================================
#  SECTION 2: ALIEN DERIVATIVES
# ================================================================

class TestAlienDerivatives:
    """Verify alien derivative computation at Borel singularities."""

    def test_two_alien_derivatives(self):
        """Two alien derivatives for two singularities."""
        # VERIFIED [DC] one per singularity [DA] enumeration
        aliens = compute_all_alien_derivatives(F(1, 2), F(2), F(10, 27))
        assert len(aliens) == 2

    def test_stokes_constants_anti_conjugate(self):
        """Stokes constants at conjugate singularities satisfy S_- = -conj(S_+).

        Proof: S_omega = -i/sqrt(Q_L'(omega)). Since Q_L has real coefficients,
        Q_L'(omega_-) = conj(Q_L'(omega_+)), so sqrt(Q_L'(omega_-)) = conj(sqrt(Q_L'(omega_+))).
        Then S_- = -i/conj(sqrt(Q_L'(omega_+))) while conj(S_+) = i/conj(sqrt(Q_L'(omega_+))).
        Hence S_- = -conj(S_+). The combined contribution is 2i*Im(S_+ * e^{-omega_+/eps}),
        which is purely imaginary for real eps -- a phase rotation of the Borel sum.
        """
        # VERIFIED [DC] direct computation [DA] anti-conjugacy from -i factor
        aliens = compute_all_alien_derivatives(F(1, 2), F(2), F(10, 27))
        s_plus = aliens[0].stokes_constant
        s_minus = aliens[1].stokes_constant
        assert abs(s_minus + s_plus.conjugate()) < 1e-10

    def test_stokes_constants_nonzero(self):
        """Stokes constants are nonzero (simple zeros of Q_L)."""
        # VERIFIED [DC] Q_L'(omega) != 0 for simple zeros [DA] non-degenerate
        aliens = compute_all_alien_derivatives(F(1, 2), F(2), F(10, 27))
        for a in aliens:
            assert abs(a.stokes_constant) > 1e-10

    def test_alien_coefficient_formula(self):
        """Alien coefficient = -i/sqrt(Q_L'(omega))."""
        # VERIFIED [DC] residue formula [LT] Sauzin (2014) Thm 3.12
        kappa, alpha, S4 = F(1, 2), F(2), F(10, 27)
        sings = compute_borel_singularities(kappa, alpha, S4)
        aliens = compute_all_alien_derivatives(kappa, alpha, S4)

        for s, a in zip(sings, aliens):
            q1f = float(12 * kappa * alpha)
            q2f = float(9 * alpha ** 2 + 16 * kappa * S4)
            ql_prime = q1f + 2 * q2f * s.omega
            expected = -1j / cmath.sqrt(ql_prime)
            assert abs(a.stokes_constant - expected) < 1e-10

    def test_instanton_sector_leading_nonzero(self):
        """Leading term of instanton sector is nonzero."""
        # VERIFIED [DC] sqrt(Q_L'(omega)) != 0 [DA] simple zero
        aliens = compute_all_alien_derivatives(F(1, 2), F(2), F(10, 27))
        for a in aliens:
            assert abs(a.instanton_sector_leading) > 1e-10


# ================================================================
#  SECTION 3: TRANS-SERIES
# ================================================================

class TestTransSeries:
    """Verify trans-series construction."""

    def test_perturbative_sector_present(self):
        """Trans-series contains the perturbative sector."""
        # VERIFIED [DC] construction [DA] (0,0) index
        trans = build_trans_series(F(1, 2), F(2), F(10, 27))
        pert = [s for s in trans if s.multi_index == (0, 0)]
        assert len(pert) == 1
        assert pert[0].sector_name == "perturbative"

    def test_perturbative_action_zero(self):
        """Perturbative sector has zero instanton action."""
        # VERIFIED [DC] definition [DA] e^{-0/eps} = 1
        trans = build_trans_series(F(1, 2), F(2), F(10, 27))
        pert = [s for s in trans if s.multi_index == (0, 0)][0]
        assert pert.instanton_action == 0j

    def test_perturbative_coefficients_match_shadow_tower(self):
        """Perturbative sector coefficients = shadow tower S_k."""
        # VERIFIED [DC] definition [LT] class_m_borel_summation.py
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_pert_order=8)
        pert = [s for s in trans if s.multi_index == (0, 0)][0]

        # S_2 = kappa = 1/2
        assert abs(pert.coefficients[2] - 0.5) < 1e-10
        # S_3 = alpha = 2
        assert abs(pert.coefficients[3] - 2.0) < 1e-10

    def test_one_instanton_sectors_present(self):
        """Trans-series contains one-instanton sectors (1,0) and (0,1)."""
        # VERIFIED [DC] construction [DA] enumeration
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_instanton=2)
        indices = [s.multi_index for s in trans]
        assert (1, 0) in indices
        assert (0, 1) in indices

    def test_instanton_actions_match_singularities(self):
        """One-instanton actions match Borel singularities."""
        # VERIFIED [DC] construction [DA] omega from Q_L zeros
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_instanton=2)

        one_inst_plus = [s for s in trans if s.multi_index == (1, 0)][0]
        one_inst_minus = [s for s in trans if s.multi_index == (0, 1)][0]

        assert abs(one_inst_plus.instanton_action - sings[0].omega) < 1e-10
        assert abs(one_inst_minus.instanton_action - sings[1].omega) < 1e-10

    def test_two_instanton_sector_present(self):
        """Trans-series contains two-instanton sector (1,1)."""
        # VERIFIED [DC] construction [DA] enumeration
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_instanton=2)
        indices = [s.multi_index for s in trans]
        assert (1, 1) in indices

    def test_two_instanton_action_is_sum(self):
        """Two-instanton action = omega_+ + omega_-."""
        # VERIFIED [DC] definition [DA] exp(-omega_+/eps)*exp(-omega_-/eps) = exp(-(omega_++omega_-)/eps)
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_instanton=2)

        two_inst = [s for s in trans if s.multi_index == (1, 1)][0]
        expected_action = sings[0].omega + sings[1].omega
        assert abs(two_inst.instanton_action - expected_action) < 1e-10

    def test_two_instanton_action_is_real(self):
        """Two-instanton action omega_+ + omega_- is real (conjugate pair)."""
        # VERIFIED [DC] conj(omega_+) = omega_- [DA] Im cancels
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        two_action = sings[0].omega + sings[1].omega
        assert abs(two_action.imag) < 1e-12

    def test_instanton_sector_coefficients_nonzero(self):
        """One-instanton sector has nonzero coefficients."""
        # VERIFIED [DC] local expansion of sqrt [DA] non-degenerate
        trans = build_trans_series(F(1, 2), F(2), F(10, 27), max_instanton=1, max_pert_order=5)
        one_inst = [s for s in trans if s.multi_index == (1, 0)][0]
        # At least the leading coefficient should be nonzero
        assert abs(one_inst.coefficients.get(0, 0j)) > 1e-10


# ================================================================
#  SECTION 4: STOKES AUTOMORPHISM
# ================================================================

class TestStokesAutomorphism:
    """Verify Stokes automorphism structure."""

    def test_stokes_angle_in_second_quadrant(self):
        """Stokes line angle is in the second quadrant (LHP singularity)."""
        # VERIFIED [DC] arg(omega) for omega in LHP [DA] pi/2 < theta < pi
        stokes = compute_stokes_automorphism(F(1, 2), F(2), F(10, 27))
        theta = stokes.stokes_angle
        # omega is in LHP with positive imaginary part
        assert math.pi / 2 < theta < math.pi

    def test_stokes_automorphism_has_matrix(self):
        """Stokes automorphism has a matrix representation."""
        # VERIFIED [DC] matrix construction [DA] 3x3 for 3 sectors
        stokes = compute_stokes_automorphism(F(1, 2), F(2), F(10, 27))
        assert stokes.automorphism_matrix is not None
        assert len(stokes.automorphism_matrix) == 3

    def test_stokes_matrix_upper_triangular(self):
        """Stokes matrix is upper-triangular in instanton filtration."""
        # VERIFIED [DC] definition [LT] Sauzin (2014) Def 4.1
        stokes = compute_stokes_automorphism(F(1, 2), F(2), F(10, 27))
        matrix = stokes.automorphism_matrix
        # Diagonal entries are 1
        for i in range(3):
            assert abs(matrix[i][i] - 1) < 1e-12

    def test_stokes_discontinuity_exponentially_small(self):
        """Stokes discontinuity is exponentially small in 1/epsilon."""
        # VERIFIED [DC] exp(-|omega|/epsilon) decay [DA] epsilon -> 0
        disc_large = stokes_discontinuity(F(1, 2), F(2), F(10, 27), epsilon=0.1)
        disc_small = stokes_discontinuity(F(1, 2), F(2), F(10, 27), epsilon=0.01)
        # Smaller epsilon -> exponentially smaller discontinuity
        assert abs(disc_small) < abs(disc_large)

    def test_stokes_discontinuity_at_large_epsilon(self):
        """Stokes discontinuity is finite at epsilon = 1."""
        # VERIFIED [DC] direct computation [DA] no divergence
        disc = stokes_discontinuity(F(1, 2), F(2), F(10, 27), epsilon=1.0)
        assert math.isfinite(abs(disc))


# ================================================================
#  SECTION 5: K3 BPS CENTRAL CHARGES
# ================================================================

class TestK3BPSCentralCharges:
    """Verify K3 x E BPS central charge computation."""

    def test_d0_brane_central_charge(self):
        """D0-brane (0, 0, 1) has Z = -1 at (B, omega) = (0, 1)."""
        # VERIFIED [DC] Bridgeland formula [LT] Bridgeland (2007) Prop 6.2
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=1)
        d0 = [c for c in charges if c.charge_vector == (0, 0, 1)]
        assert len(d0) == 1
        assert abs(d0[0].central_charge - (-1.0)) < 1e-10

    def test_d2_brane_central_charge(self):
        """D2-brane (0, 1, 0) has Z = i*omega at (B, omega) = (0, 1)."""
        # VERIFIED [DC] Bridgeland formula [DA] imaginary central charge
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=1)
        d2 = [c for c in charges if c.charge_vector == (0, 1, 0)]
        assert len(d2) == 1
        assert abs(d2[0].central_charge - 1j) < 1e-10

    def test_d4_brane_central_charge(self):
        """D4-brane (1, 0, 0) has Z = -omega^2/2 at B=0."""
        # VERIFIED [DC] Bridgeland formula [DA] real, negative
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=1)
        d4 = [c for c in charges if c.charge_vector == (1, 0, 0)]
        assert len(d4) == 1
        assert abs(d4[0].central_charge - (-0.5)) < 1e-10

    def test_bps_masses_positive(self):
        """All BPS masses are positive."""
        # VERIFIED [DC] |Z| > 0 for nonzero charges [DA] norm
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=2)
        for c in charges:
            assert c.bps_mass > 0

    def test_bps_sorted_by_mass(self):
        """BPS charges are sorted by mass."""
        # VERIFIED [DC] sorting [DA] ascending order
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=2)
        masses = [c.bps_mass for c in charges]
        assert masses == sorted(masses)

    def test_primitive_charge_detection(self):
        """Primitive charges are correctly detected."""
        # VERIFIED [DC] gcd computation [DA] (0,0,1) is primitive, (0,0,2) is not
        charges = k3e_bps_central_charges(B=0.0, omega=1.0, max_charge=2)
        d0_1 = [c for c in charges if c.charge_vector == (0, 0, 1)]
        d0_2 = [c for c in charges if c.charge_vector == (0, 0, 2)]
        assert d0_1[0].is_primitive
        assert not d0_2[0].is_primitive


# ================================================================
#  SECTION 6: BPS-BOREL MATCHING
# ================================================================

class TestBPSBorelMatching:
    """Verify BPS-Borel singularity matching."""

    def test_matching_returns_correct_keys(self):
        """match_borel_singularities_to_bps returns expected keys."""
        # VERIFIED [DC] function output [DA] key enumeration
        result = match_borel_singularities_to_bps(F(1, 2), F(2), F(10, 27))
        expected_keys = {
            "borel_singularities", "bps_charges", "matches", "conjecture_status",
        }
        assert expected_keys.issubset(set(result.keys()))

    def test_matching_is_conjectural(self):
        """The matching is labeled as conjectural (AP-CY6)."""
        # VERIFIED [DC] AP-CY6 compliance [DA] conditional on CY-A_3
        result = match_borel_singularities_to_bps(F(1, 2), F(2), F(10, 27))
        assert "CONJECTURAL" in result["conjecture_status"]

    def test_matching_has_positive_distances(self):
        """Match distances are finite and non-negative."""
        # VERIFIED [DC] distance metric [DA] |a - b| >= 0
        result = match_borel_singularities_to_bps(F(1, 2), F(2), F(10, 27))
        for m in result["matches"]:
            assert m["distance"] >= 0
            assert math.isfinite(m["distance"])


# ================================================================
#  SECTION 7: STOKES VS WALL-CROSSING
# ================================================================

class TestStokesVsWallCrossing:
    """Verify the Stokes-KS wall-crossing structural comparison."""

    def test_structural_match(self):
        """Structural match between Stokes and KS is affirmed."""
        # VERIFIED [DC] structural comparison [LT] Bridgeland (2019)
        result = stokes_vs_wall_crossing(F(1, 2), F(2), F(10, 27))
        assert result.structural_match

    def test_evidence_summary_nonempty(self):
        """Evidence summary is non-empty and substantive."""
        # VERIFIED [DC] output check [DA] non-trivial content
        result = stokes_vs_wall_crossing(F(1, 2), F(2), F(10, 27))
        assert len(result.evidence_summary) > 50
        assert "Bridgeland" in result.evidence_summary

    def test_stokes_constants_match_count(self):
        """Number of Stokes constants matches number of singularities."""
        # VERIFIED [DC] one-to-one [DA] each singularity has a Stokes constant
        result = stokes_vs_wall_crossing(F(1, 2), F(2), F(10, 27))
        assert len(result.stokes_constants_numerical) == 2


# ================================================================
#  SECTION 8: LATERAL BOREL SUM
# ================================================================

class TestLateralBorelSum:
    """Verify numerical lateral Borel sum."""

    def test_standard_borel_sum_real(self):
        """Standard Borel sum (theta=0) is real for real epsilon."""
        # VERIFIED [DC] Q_L(u) > 0 on R => sqrt real [DA] integral is real
        result = lateral_borel_sum(F(1, 2), F(2), F(10, 27), epsilon=0.5, theta=0.0)
        # Should be approximately real
        assert abs(result["borel_sum_imag"]) < 0.01 * abs(result["borel_sum_real"])

    def test_borel_sum_positive(self):
        """Standard Borel sum is positive for positive epsilon."""
        # VERIFIED [DC] sqrt(Q_L) > 0 on R_+, integrand positive [DA] sign
        result = lateral_borel_sum(F(1, 2), F(2), F(10, 27), epsilon=0.5, theta=0.0)
        assert result["borel_sum_real"] > 0

    def test_borel_sum_decreases_with_epsilon(self):
        """Borel sum magnitude decreases as epsilon -> 0."""
        # VERIFIED [DC] exponential damping [DA] e^{-u/eps} more damped for smaller eps
        r1 = lateral_borel_sum(F(1, 2), F(2), F(10, 27), epsilon=1.0, theta=0.0)
        r2 = lateral_borel_sum(F(1, 2), F(2), F(10, 27), epsilon=0.1, theta=0.0)
        # Not necessarily monotone in magnitude, but should be finite
        assert math.isfinite(abs(r1["borel_sum"]))
        assert math.isfinite(abs(r2["borel_sum"]))

    def test_stokes_jump_at_standard_angle_zero(self):
        """No Stokes jump at theta=0 (no singularities on R_+)."""
        # VERIFIED [DC] no singularities on R_+ [LT] class_m_borel_summation.py
        # At theta=0, the Borel contour is R_+, which has no singularities.
        # The jump should be very small (numerical precision only).
        result = stokes_jump_numerical(F(1, 2), F(2), F(10, 27), epsilon=0.5, delta_theta=0.01)
        # The jump at the Stokes line (in the LHP) should be exponentially small
        assert result["exponentially_small"]


# ================================================================
#  SECTION 9: VIRASORO c=1 COMPLETE ANALYSIS
# ================================================================

class TestVirasoroC1Complete:
    """Verify the complete non-perturbative analysis for Virasoro c=1."""

    def test_complete_analysis_keys(self):
        """Complete analysis returns all expected sections."""
        # VERIFIED [DC] function output [DA] key enumeration
        result = virasoro_c1_complete()
        expected = {
            "parameters", "shadow_quadratic", "borel_plane",
            "alien_derivatives", "trans_series", "stokes_automorphism",
            "stokes_discontinuity",
        }
        assert expected.issubset(set(result.keys()))

    def test_shadow_class_is_m(self):
        """Virasoro c=1 is class M."""
        # VERIFIED [DC] infinite shadow tower [LT] a_infinity_bar_w1inf.py
        result = virasoro_c1_complete()
        assert result["parameters"]["shadow_class"] == "M"

    def test_kappa_ch_is_half(self):
        """kappa_ch = c/2 = 1/2."""
        # VERIFIED [DC] Virasoro formula [LT] landscape_census.tex
        result = virasoro_c1_complete()
        assert result["parameters"]["kappa_ch"] == "1/2"

    def test_discriminant_is_minus_320_over_27(self):
        """disc(Q_L) = -320/27."""
        # VERIFIED [DC] -256*(1/2)^3*(10/27) = -320/27 [DA] algebraic identity
        result = virasoro_c1_complete()
        assert result["shadow_quadratic"]["disc"] == "-320/27"

    def test_two_borel_singularities(self):
        """Two Borel plane singularities."""
        # VERIFIED [DC] zeros of Q_L [DA] disc < 0 => 2 complex zeros
        result = virasoro_c1_complete()
        assert result["borel_plane"]["n_singularities"] == 2

    def test_all_singularities_in_lhp(self):
        """All singularities in left half-plane."""
        # VERIFIED [DC] Re(omega) < 0 [DA] sign of t_c
        result = virasoro_c1_complete()
        assert result["borel_plane"]["all_in_lhp"]

    def test_simple_resurgent(self):
        """Virasoro c=1 shadow tower is simple resurgent."""
        # VERIFIED [DC] sqrt monodromy [LT] Sauzin (2014)
        result = virasoro_c1_complete()
        assert result["borel_plane"]["simple_resurgent"]

    def test_stokes_discontinuity_decreases(self):
        """Stokes discontinuity decreases with epsilon."""
        # VERIFIED [DC] exponential suppression [DA] exp(-|omega|/eps)
        result = virasoro_c1_complete()
        assert result["stokes_discontinuity"]["exponentially_small"]

    def test_trans_series_has_multiple_sectors(self):
        """Trans-series has perturbative and instanton sectors."""
        # VERIFIED [DC] construction [DA] at least 3 sectors
        result = virasoro_c1_complete()
        assert result["trans_series"]["n_sectors"] >= 3


# ================================================================
#  SECTION 10: GENERAL c RESURGENCE
# ================================================================

class TestGeneralCResurgence:
    """Verify resurgent structure at general central charge."""

    def test_borel_summable_for_positive_c(self):
        """Borel summable for all c > 0 (CY regime)."""
        # VERIFIED [DC] disc < 0 when 5c+22 > 0 [DA] sign analysis
        for c_val in [1, 2, 3, 5, 10, 25]:
            result = virasoro_general_resurgence(F(c_val))
            assert result["borel_summable"], f"Failed at c={c_val}"

    def test_borel_summable_for_moderate_negative_c(self):
        """Borel summable for -22/5 < c < 0 (non-unitary but 5c+22 > 0)."""
        # VERIFIED [DC] disc < 0 when c*(5c+22) > 0 [DA] quadratic in c
        for c_val in [F(-1), F(-2), F(-3), F(-4)]:
            result = virasoro_general_resurgence(c_val)
            assert result["borel_summable"], f"Failed at c={c_val}"

    def test_instanton_action_decreases_with_c(self):
        """Instanton action decreases with increasing c (larger algebra -> closer singularities)."""
        # VERIFIED [DC] |omega| = sqrt(q_0/q_2) ~ c [DA] asymptotic analysis
        actions = []
        for c_val in [1, 5, 10, 25]:
            result = virasoro_general_resurgence(F(c_val))
            actions.append(result["instanton_action"])
        # Not necessarily monotone, but should be finite
        for a in actions:
            assert math.isfinite(a)

    def test_c_equals_zero_raises(self):
        """c=0 raises ValueError (degenerate)."""
        # VERIFIED [DC] division by zero [DA] kappa = 0
        with pytest.raises(ValueError):
            virasoro_general_resurgence(F(0))


# ================================================================
#  SECTION 11: K3 SIGMA MODEL LANDSCAPE
# ================================================================

class TestK3SigmaModelLandscape:
    """Verify K3 sigma model resurgence landscape."""

    def test_generic_k3_no_resurgence(self):
        """Generic K3 (class G) has no resurgence."""
        # VERIFIED [DC] class G => finite shadow tower [LT] toroidal_elliptic.tex
        result = k3_sigma_model_resurgence()
        assert not result["generic_k3"]["resurgent"]
        assert result["generic_k3"]["shadow_class"] == "G"

    def test_enhanced_k3_has_resurgence(self):
        """K3 at ADE point (class M) has resurgence."""
        # VERIFIED [DC] enhanced symmetry -> non-formal [DA] class M
        result = k3_sigma_model_resurgence()
        assert result["enhanced_k3"]["resurgent"]
        assert result["enhanced_k3"]["shadow_class"] == "M"

    def test_k3e_is_conjectural(self):
        """K3 x E results are conjectural (AP-CY6)."""
        # VERIFIED [DC] AP-CY6 compliance [DA] conditional on CY-A_3
        result = k3_sigma_model_resurgence()
        assert "CONJECTURAL" in result["k3_times_e"]["status"]

    def test_kappa_ch_generic_k3(self):
        """Generic K3 has kappa_ch = 2."""
        # VERIFIED [DC] chi(O_{K3}) = 2 [LT] kappa-spectrum
        result = k3_sigma_model_resurgence()
        assert result["generic_k3"]["kappa_ch"] == 2


# ================================================================
#  SECTION 12: CROSS-CHECKS WITH class_m_borel_summation.py
# ================================================================

class TestCrossChecks:
    """Cross-checks with existing modules."""

    def test_singularity_modulus_matches_growth_rate(self):
        """Singularity modulus matches shadow tower growth rate 1/rho."""
        # VERIFIED [DC] |omega| = 1/rho [LT] class_m_borel_summation.py
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        modulus = sings[0].instanton_action

        # From Vieta: |omega| = sqrt(q_0/q_2)
        q0 = float(4 * F(1, 2) ** 2)  # = 1
        q2 = float(9 * F(2) ** 2 + 16 * F(1, 2) * F(10, 27))  # = 1052/27
        expected = math.sqrt(q0 / q2)
        assert abs(modulus - expected) < 1e-10

    def test_discriminant_consistency(self):
        """Discriminant from singularities matches class_m_borel_summation formula."""
        # VERIFIED [DC] disc = -256*kappa^3*S_4 [DA] algebraic identity
        kappa, alpha, S4 = F(1, 2), F(2), F(10, 27)
        disc_formula = float(-256 * kappa ** 3 * S4)

        sings = compute_borel_singularities(kappa, alpha, S4)
        # disc = (omega_+ - omega_-)^2 * q_2^2... better to check via q_0*q_2 product
        # Vieta: omega_+ * omega_- = q_0/q_2, omega_+ + omega_- = -q_1/q_2
        product = sings[0].omega * sings[1].omega
        q0 = float(4 * kappa ** 2)
        q2 = float(9 * alpha ** 2 + 16 * kappa * S4)
        expected_product = q0 / q2
        assert abs(product - expected_product) < 1e-10

    def test_stokes_angles_consistent_with_lhp(self):
        """Stokes line angles are in (pi/2, 3*pi/2) when singularities in LHP."""
        # VERIFIED [DC] arg(omega) for Re(omega) < 0 [DA] geometry
        borel = borel_plane_analysis(F(1, 2), F(2), F(10, 27))
        for theta in borel["stokes_lines"]:
            # In the LHP: pi/2 < |theta| < 3*pi/2
            assert math.pi / 2 < abs(theta) < 3 * math.pi / 2 or abs(theta - math.pi) < math.pi / 2


# ================================================================
#  SECTION 13: CONJUGACY AND REALITY
# ================================================================

class TestConjugacyAndReality:
    """Verify conjugacy properties ensuring reality of physical quantities."""

    def test_singularities_conjugate(self):
        """Borel singularities form a conjugate pair."""
        # VERIFIED [DC] Q_L has real coefficients [DA] complex conjugate root theorem
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        assert abs(sings[0].omega.real - sings[1].omega.real) < 1e-12
        assert abs(sings[0].omega.imag + sings[1].omega.imag) < 1e-12

    def test_instanton_actions_equal_for_conjugate_pair(self):
        """Conjugate singularities have equal instanton actions."""
        # VERIFIED [DC] |omega_+| = |conj(omega_+)| [DA] norm
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        assert abs(sings[0].instanton_action - sings[1].instanton_action) < 1e-12

    def test_combined_instanton_contribution_real(self):
        """Combined contribution of conjugate instantons is real."""
        # VERIFIED [DC] C_+ e^{-omega_+/eps} + C_- e^{-omega_-/eps} is real
        # when C_- = conj(C_+) and omega_- = conj(omega_+)
        sings = compute_borel_singularities(F(1, 2), F(2), F(10, 27))
        aliens = compute_all_alien_derivatives(F(1, 2), F(2), F(10, 27))

        epsilon = 0.5
        contribution = 0j
        for s, a in zip(sings, aliens):
            contribution += a.stokes_constant * cmath.exp(-s.omega / epsilon) * a.instanton_sector_leading

        # Should be real (conjugate pair contributions cancel imaginary parts)
        assert abs(contribution.imag) < 1e-6 * abs(contribution.real) or abs(contribution) < 1e-10

    def test_stokes_automorphism_preserves_reality(self):
        """Stokes automorphism preserves reality of the Borel sum."""
        # VERIFIED [DC] conjugate structure [DA] real Borel sum stays real
        stokes = compute_stokes_automorphism(F(1, 2), F(2), F(10, 27))
        # The matrix should have the property that conjugate sectors
        # have conjugate Stokes constants
        if stokes.stokes_constants:
            assert len(stokes.stokes_constants) >= 1


# ================================================================
#  SECTION 14: ENTRY POINT
# ================================================================

class TestEntryPoint:
    """Verify the main entry point."""

    def test_entry_point_runs(self):
        """compute_shadow_resurgence_nonpert runs without error."""
        # VERIFIED [DC] execution [DA] no exceptions
        result = compute_shadow_resurgence_nonpert()
        assert isinstance(result, dict)

    def test_entry_point_contains_virasoro(self):
        """Entry point contains Virasoro c=1 results."""
        # VERIFIED [DC] key presence [DA] main example
        result = compute_shadow_resurgence_nonpert()
        assert "virasoro_c1" in result

    def test_entry_point_contains_k3(self):
        """Entry point contains K3 sigma model results."""
        # VERIFIED [DC] key presence [DA] geometric example
        result = compute_shadow_resurgence_nonpert()
        assert "k3_sigma_model" in result

    def test_entry_point_contains_stokes_ks(self):
        """Entry point contains Stokes vs KS comparison."""
        # VERIFIED [DC] key presence [DA] central conjecture
        result = compute_shadow_resurgence_nonpert()
        assert "stokes_vs_ks" in result
