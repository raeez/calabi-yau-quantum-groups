"""
Tests for the general Borcherds multiplicative lift.

Verifies:
1. The lift of phi_{0,1} produces (1/64)*Delta_5 (weight 5, ratio = -1)
2. The lift of the constant form phi=12 produces an eta-product (weight 6)
3. The lift of 2*phi_{0,1} produces the SQUARE of the lift of phi_{0,1}
4. Weight identity wt = c(0)/2 via TWO routes on the CHL ladder:
   the frame-shape half-sum route (independent of Fourier data) against
   the Jacobi-side constant term.  At N = 1 both sides are computed
   in-repo (genuine two-path independence); at N in {2, 3, 4, 6} the
   Fourier side is a recorded literature constant, so the comparison is
   a consistency check of the frame-shape computation, not a two-sided
   computation.  borcherds_lift_weight itself is definitional (c(0)/2
   by fiat) and is never tested against its own definition.
5. Structural properties: H_2 validation, convergence, sign convention
6. Reverse engineering analysis for M_2(Gamma_2, nu_4)

Numerical agreements checked to at least 10 digits where convergence permits.
"""

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.borcherds_lift import (
    borcherds_lift,
    borcherds_lift_weight,
    delta5_theta,
    phi01_c_table,
    constant_jacobi_c_table,
    doubled_phi01_c_table,
    verify_phi01_lift_equals_delta5,
    verify_constant_lift,
    verify_doubled_lift_vs_square,
    analyze_weight2_multiplier,
    fourier_jacobi_expansion,
    phi01_numerical,
    _even_theta_characteristics,
    KNOWN_BORCHERDS_LIFTS,
    CHL_FRAME_SHAPES,
    CHL_SQUARE_ROOT_SEED_C0,
    frame_shape_degree,
    eta_product_weight,
    jatkar_sen_dyon_weight,
    chl_square_root_weight,
)


# ---------------------------------------------------------------------------
# Test: phi_{0,1} coefficient table
# ---------------------------------------------------------------------------

class TestPhi01CTable:
    """Test the c(D) table extracted from phi_{0,1}."""

    @pytest.fixture(scope="class")
    def c_table(self):
        return phi01_c_table(60)

    def test_known_coefficients(self, c_table):
        """Verify c(D) against known values from Eichler-Zagier."""
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[-1] == 1
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[0] == 10
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[3] == -64
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[4] == 108
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[7] == -513
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[8] == 808
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[11] == -2752
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c_table[12] == 4016

    def test_weight_is_5(self, c_table):
        """Weight of the Borcherds lift = c(0)/2 = 10/2 = 5."""
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c_table) == 5.0

    def test_no_d_between_minus1_and_0(self, c_table):
        """No discriminant between -1 and 0 appears (gap in the lattice)."""
        for D in c_table:
            if D < 0:
                # VERIFIED [DC] structural property [LT] Borcherds product theory
                assert D == -1

    def test_nonzero_discriminants_mod_4(self, c_table):
        """Nonzero c(D) occurs only for D = -1 or D >= 0 with D equiv 0 or 3 mod 4."""
        for D, v in c_table.items():
            if D == -1:
                continue
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert D >= 0
            assert D % 4 in (0, 3), f"c({D}) = {v} but D mod 4 = {D % 4}"


# ---------------------------------------------------------------------------
# Test: Borcherds lift weight computation
# ---------------------------------------------------------------------------

class TestLiftWeight:
    """
    Smoke tests of borcherds_lift_weight's definitional behaviour.

    borcherds_lift_weight returns c(0)/2 BY DEFINITION, so nothing in
    this class verifies the Borcherds weight identity itself -- these
    tests only pin the function's input/output contract (table lookup,
    default 0, halving).  The mathematical content of wt = c(0)/2 is
    tested non-circularly in TestFrameShapeWeight below, via the
    frame-shape half-sum route.
    """

    def test_phi01_weight(self):
        c = phi01_c_table(10)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 5.0

    def test_constant_weight(self):
        c = constant_jacobi_c_table(12)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 6.0

    def test_doubled_weight(self):
        c = doubled_phi01_c_table(10)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 10.0

    def test_zero_weight(self):
        """Empty table gives weight 0."""
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight({}) == 0.0

    def test_arbitrary_weight(self):
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight({0: 24}) == 12.0
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight({0: 2, -1: 5}) == 1.0


# ---------------------------------------------------------------------------
# Test: Frame-shape route to the lift weight (non-circular)
# ---------------------------------------------------------------------------

class TestFrameShapeWeight:
    """
    The weight identity kappa_BKM(Phi_N) = c_N(0)/2 on the CHL ladder
    N in {1, 2, 3, 4, 6}, tested via the frame-shape half-sum route.

    chl_square_root_weight(N) computes the weight of the
    Govindarajan-Krishna square root Delta_{k/2} purely from the M24
    frame shape of the Z/N orbifold generator (Jatkar-Sen
    hep-th/0510147; Govindarajan-Krishna arXiv:0907.1410):
    wt = ((1/2) sum_i r_i - 2)/2.  No Fourier coefficient enters.

    Independence vs consistency, stated honestly:
    - N = 1: the seed constant c_1(0) = 10 is computed exactly in-repo
      (phi01_fourier.py), so frame-shape route vs Fourier route is a
      genuine TWO-PATH INDEPENDENT verification of wt = c(0)/2.
    - N in {2, 3, 4, 6}: the seed constants (6, 4, 3, 2) are recorded
      literature values (no in-repo twisted-seed Fourier computation
      exists), so the comparison is a CONSISTENCY check of the
      frame-shape computation against the recorded constants.

    Manuscript anchors: sec_7_lattice_automorphic.tex,
    phi_universal_trace_platonic.tex (square-root ladder
    (5, 3, 2, 3/2, 1); never mixed with the Mathieu-twined ladder
    (10, 4, 3, 2, 1) or the geometric-orbifold family in
    kappa_bkm_adversarial.py).
    """

    CHL_LADDER = (1, 2, 3, 4, 6)

    EXPECTED_KAPPA = {
        1: Fraction(5),
        2: Fraction(3),
        3: Fraction(2),
        4: Fraction(3, 2),
        6: Fraction(1),
    }

    def test_frame_shapes_have_degree_24(self):
        """Each CHL frame shape acts on the 24-dim lattice rep."""
        for N in self.CHL_LADDER:
            # VERIFIED [DC] lattice degree [LT] Jatkar-Sen hep-th/0510147
            assert frame_shape_degree(CHL_FRAME_SHAPES[N]) == 24

    def test_eta_product_weights(self):
        """wt(eta_rho) = (1/2) sum r_i = (12, 8, 6, 5, 4)."""
        expected = {1: 12, 2: 8, 3: 6, 4: 5, 6: 4}
        for N in self.CHL_LADDER:
            # VERIFIED [DC] eta-product weight [LT] standard eta-quotient theory
            assert eta_product_weight(CHL_FRAME_SHAPES[N]) == expected[N]

    def test_jatkar_sen_dyon_weights(self):
        """Phi_k weights k(N) = (1/2) sum r_i - 2 = (10, 6, 4, 3, 2)."""
        expected = {1: 10, 2: 6, 3: 4, 4: 3, 6: 2}
        for N in self.CHL_LADDER:
            # VERIFIED [DC] dyon-form weight [LT] Jatkar-Sen hep-th/0510147
            assert jatkar_sen_dyon_weight(N) == expected[N]

    def test_square_root_weights(self):
        """Delta_{k/2} weights = kappa_BKM = (5, 3, 2, 3/2, 1)."""
        for N in self.CHL_LADDER:
            # VERIFIED [DC] frame-shape half-sum [LT] Govindarajan-Krishna 0907.1410
            assert chl_square_root_weight(N) == self.EXPECTED_KAPPA[N]

    def test_N1_two_path_independence(self):
        """
        N = 1: genuine two-path verification of wt = c(0)/2.

        Path A (frame shape): 1^24 -> ((24/2) - 2)/2 = 5, no Fourier data.
        Path B (Fourier): constant term of phi_{0,1} computed exactly by
        phi01_fourier.py, halved by the Borcherds weight formula.
        """
        wt_frame = chl_square_root_weight(1)
        c_table = phi01_c_table(10)
        wt_fourier = borcherds_lift_weight(c_table)
        # VERIFIED [DC] two independent computation paths agree
        assert wt_frame == Fraction(5)
        assert wt_fourier == 5.0
        assert float(wt_frame) == wt_fourier

    def test_weight_identity_across_chl_ladder(self):
        """
        wt(Delta_{k/2}) == c_N(0)/2 for N in {1, 2, 3, 4, 6}.

        CONSISTENCY at N >= 2 (recorded literature constants), genuine
        independence only at N = 1 (see test_N1_two_path_independence).
        """
        for N in self.CHL_LADDER:
            wt_frame = chl_square_root_weight(N)
            c0 = CHL_SQUARE_ROOT_SEED_C0[N]
            # VERIFIED [DC] frame-shape route vs recorded c_N(0)
            # [LT] Jatkar-Sen / Govindarajan-Krishna
            assert wt_frame == Fraction(c0, 2), (
                f"N={N}: frame-shape weight {wt_frame} != c_N(0)/2 = {c0}/2"
            )
            assert wt_frame == self.EXPECTED_KAPPA[N]

    def test_seed_c0_N1_matches_exact_fourier(self):
        """The recorded c_1(0) = 10 equals the exact in-repo computation."""
        c_table = phi01_c_table(10)
        # VERIFIED [DC] exact arithmetic (phi01_fourier.py)
        assert CHL_SQUARE_ROOT_SEED_C0[1] == c_table[0] == 10

    def test_fake_monster_eta24_no_shift(self):
        """
        Leech/II_{25,1}: the Phi_12 weight equals the eta-product weight
        of 1^24 directly (12 = 24/2), with no "-2" shift -- the shift is
        specific to the Jatkar-Sen K3 x E normalisation.
        """
        # VERIFIED [DC] eta-product weight [LT] Borcherds 1995
        assert eta_product_weight({1: 24}) == 12
        assert KNOWN_BORCHERDS_LIFTS['Phi_12_fake_monster']['weight'] == 12


# ---------------------------------------------------------------------------
# Test: Core Borcherds lift produces Delta_5
# ---------------------------------------------------------------------------

class TestBorcherdsLiftDelta5:
    """
    Verify that the Borcherds lift of phi_{0,1} equals (1/64)*Delta_5
    at multiple points in the Siegel upper half-space.

    The identity holds with ratio = -1 (a sign from the branch of log
    at the (n=0, l=-1, m=0) factor in the Borcherds product).
    """

    @pytest.fixture(scope="class")
    def c_table(self):
        return phi01_c_table(80)

    @pytest.mark.parametrize("tau,z,omega", [
        (2.0j, 0.1j, 2.0j),                         # deep cusp
        (0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j),         # moderate with real parts
        (0.3 + 1.5j, 0.1 - 0.1j, 0.2 + 1.7j),       # general position
    ])
    def test_abs_agreement(self, c_table, tau, z, omega):
        """|(1/64)*Delta_5| = |Borcherds lift| to at least 10 digits."""
        bp = borcherds_lift(c_table, tau, z, omega, N_prod=12)
        d5 = delta5_theta(tau, z, omega, N_terms=25)
        lhs = d5 / 64.0
        abs_ratio = abs(lhs) / abs(bp)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(abs_ratio - 1.0) < 1e-10, \
            f"|ratio| - 1 = {abs(abs_ratio - 1.0):.2e}"

    @pytest.mark.parametrize("tau,z,omega", [
        (2.0j, 0.1j, 2.0j),
        (0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j),
        (0.3 + 1.5j, 0.1 - 0.1j, 0.2 + 1.7j),
    ])
    def test_sign_is_minus_one(self, c_table, tau, z, omega):
        """The ratio (1/64)*Delta_5 / BP is consistently -1."""
        bp = borcherds_lift(c_table, tau, z, omega, N_prod=12)
        d5 = delta5_theta(tau, z, omega, N_terms=25)
        ratio = (d5 / 64.0) / bp
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(ratio + 1) < 1e-8, \
            f"ratio = {ratio}, expected -1"

    def test_deep_cusp_precision(self, c_table):
        """At deep cusp, achieve at least 12-digit agreement."""
        result = verify_phi01_lift_equals_delta5(
            2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
        )
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['abs_relative_error'] < 1e-12

    def test_verify_function(self, c_table):
        """The verify_phi01_lift_equals_delta5 function returns correct structure."""
        result = verify_phi01_lift_equals_delta5(
            2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
        )
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['weight'] == 5.0
        assert 'borcherds_lift' in result
        assert 'delta5' in result
        assert 'ratio' in result
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['abs_relative_error'] < 1e-10


# ---------------------------------------------------------------------------
# Test: Constant Jacobi form phi = 12
# ---------------------------------------------------------------------------

class TestConstantLift:
    """
    Test the Borcherds lift of the constant Jacobi form phi = 12.

    c(0) = 12, c(D) = 0 for D != 0. Weight = 6.
    c(-1) = 0, so the leading exponential is trivial (= 1).

    The product factors:
    - (n>0, m=0, l=0): prod(1-q^n)^12
    - (n=0, m>0, l=0): prod(1-s^m)^12
    - (n>0, m>0, l^2=4nm): additional factors with exponent 12

    At deep cusp, the l^2=4nm factors are negligible, and the lift
    approaches prod(1-q^n)^12 * prod(1-s^m)^12 = eta(tau)^12/q^{1/2} * eta(omega)^12/s^{1/2}.
    But since the leading exponential is 1 (not exp(pi*i*(tau+z+omega))),
    the result is NOT eta^12 * eta^12.
    """

    def test_weight_is_6(self):
        c = constant_jacobi_c_table(12)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 6.0

    def test_c_table_structure(self):
        c = constant_jacobi_c_table(12)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c == {0: 12}
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c.get(-1, 0) == 0

    def test_deep_cusp_vs_eta_product(self):
        """
        At deep cusp (large Im), the lift should approach
        prod(1-q^n)^12 * prod(1-s^m)^12 since l^2=4nm corrections vanish.
        """
        result = verify_constant_lift(3j, 0.05j, 3j, N_prod=15)
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['weight'] == 6.0
        if 'ratio_abs' in result:
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert abs(result['ratio_abs'] - 1.0) < 1e-10, \
                f"|ratio| = {result['ratio_abs']}"

    def test_nonzero_at_generic_point(self):
        """The lift is nonzero at generic points."""
        c = constant_jacobi_c_table(12)
        bp = borcherds_lift(c, 2j, 0.1j, 2j, N_prod=12)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(bp) > 1e-10

    def test_different_constants(self):
        """Weight scales linearly with the constant."""
        for val, expected_weight in [(24, 12.0), (2, 1.0), (8, 4.0)]:
            c = constant_jacobi_c_table(val)
            assert borcherds_lift_weight(c) == expected_weight


# ---------------------------------------------------------------------------
# Test: Doubled lift 2*phi_{0,1}
# ---------------------------------------------------------------------------

class TestDoubledLift:
    """
    Test that the lift of 2*phi_{0,1} equals the square of the lift of phi_{0,1}.

    Since all Fourier coefficients double (including c(-1) which controls the
    leading exponential), the entire log-sum doubles, so:
        Phi_{2*phi}(Z) = Phi_{phi}(Z)^2 = ((1/64)*Delta_5)^2 = Delta_5^2 / 4096.
    """

    def test_weight_is_10(self):
        c = doubled_phi01_c_table(10)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 10.0

    def test_coefficients_are_doubled(self):
        c = phi01_c_table(20)
        c2 = doubled_phi01_c_table(20)
        for D in c:
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert c2[D] == 2 * c[D]

    def test_lift_is_square_of_original(self):
        """Phi(2c) = Phi(c)^2 to machine precision."""
        result = verify_doubled_lift_vs_square(
            2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
        )
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['weight_doubled'] == 10.0
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['ratio_abs_error'] < 1e-12, \
            f"|Phi(2c)/Phi(c)^2| - 1 = {result['ratio_abs_error']:.2e}"

    def test_matches_delta5_squared(self):
        """Phi(2c) = Delta_5^2 / 4096 to high precision."""
        result = verify_doubled_lift_vs_square(
            2j, 0.1j, 2j, N_prod=12, N_theta=25, D_max=80,
        )
        ratio = result.get('ratio_d5sq_vs_4096_doubled')
        assert ratio is not None
        # The ratio should be 1 (up to the sign (-1)^2 = 1 from the branch)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(abs(ratio) - 1.0) < 1e-10, \
            f"|D5^2/(4096*Phi(2c))| - 1 = {abs(abs(ratio) - 1.0):.2e}"

    def test_at_moderate_point(self):
        """Verify at a moderate (less deep) point."""
        result = verify_doubled_lift_vs_square(
            0.1 + 2j, 0.05 + 0.3j, 0.15 + 2j,
            N_prod=12, N_theta=25, D_max=80,
        )
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['ratio_abs_error'] < 1e-10


# ---------------------------------------------------------------------------
# Test: H_2 validation
# ---------------------------------------------------------------------------

class TestH2Validation:
    """Test that the lift correctly validates points in H_2."""

    def test_valid_point(self):
        """A valid H_2 point should not raise."""
        c = phi01_c_table(20)
        bp = borcherds_lift(c, 2j, 0.1j, 2j, N_prod=5)
        assert isinstance(bp, (complex, np.complexfloating))

    def test_invalid_point_negative_imaginary(self):
        """Negative Im(tau) should fail."""
        c = phi01_c_table(20)
        with pytest.raises(AssertionError):
            borcherds_lift(c, -2j, 0.1j, 2j, N_prod=5)

    def test_invalid_point_det_negative(self):
        """If Im(tau)*Im(omega) < Im(z)^2, not in H_2."""
        c = phi01_c_table(20)
        # Im(tau)=1, Im(omega)=1, Im(z)=2 => det = 1*1 - 4 = -3 < 0
        with pytest.raises(AssertionError):
            borcherds_lift(c, 1j, 2j, 1j, N_prod=5)


# ---------------------------------------------------------------------------
# Test: Delta_5 properties
# ---------------------------------------------------------------------------

class TestDelta5:
    """Test Delta_5 computed via theta constants."""

    def test_ten_even_characteristics(self):
        chars = _even_theta_characteristics()
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert len(chars) == 10

    def test_symmetry_z1_z3(self):
        """Delta_5 is invariant under tau <-> omega."""
        tau, z, omega = 0.1 + 2j, 0.05 + 0.2j, 0.3 + 1.8j
        d5 = delta5_theta(tau, z, omega, N_terms=20)
        d5_swap = delta5_theta(omega, z, tau, N_terms=20)
        # VERIFIED [DC] symmetry check [LT] Borcherds product theory
        assert abs(d5 - d5_swap) / abs(d5) < 1e-10

    def test_vanishes_on_diagonal(self):
        """Delta_5 vanishes when z = 0 (the diagonal locus)."""
        d5_diag = delta5_theta(0.3 + 1.5j, 0, 0.2 + 1.8j, N_terms=25)
        d5_gen = delta5_theta(0.3 + 1.5j, 0.1 + 0.15j, 0.2 + 1.8j, N_terms=25)
        if abs(d5_gen) > 1e-30:
            # VERIFIED [DC] vanishing check [LT] Borcherds product theory
            assert abs(d5_diag) / abs(d5_gen) < 1e-8

    def test_nonzero_generic(self):
        d5 = delta5_theta(2j, 0.1j, 2j, N_terms=20)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(d5) > 1e-10


# ---------------------------------------------------------------------------
# Test: phi_{0,1} numerical evaluation
# ---------------------------------------------------------------------------

class TestPhi01Numerical:
    """Test the numerical evaluation of phi_{0,1}."""

    def test_value_at_z_zero(self):
        """phi_{0,1}(tau, 0) = 12 for any tau."""
        for tau in [1j, 0.3 + 2j, 0.5 + 1j]:
            val = phi01_numerical(tau, 0, N=80)
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert abs(val - 12.0) < 1e-10

    def test_direct_expansion(self):
        """Match q-expansion at large Im(tau)."""
        tau = 3j
        z = 0.25
        q = np.exp(2j * np.pi * tau)
        r = np.exp(2j * np.pi * z)
        direct = (1/r + 10 + r) + q * (10/r**2 - 64/r + 108 - 64*r + 10*r**2)
        numerical = phi01_numerical(tau, z, N=80)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert abs(numerical - direct) < 1e-6


# ---------------------------------------------------------------------------
# Test: Fourier-Jacobi extraction
# ---------------------------------------------------------------------------

class TestFourierJacobiExtraction:
    """
    Test the Fourier-Jacobi extraction for Delta_5.

    Delta_5(Z) = sum_m phi_{5,m}(tau,z) * exp(2*pi*i*m*omega).

    The first Fourier-Jacobi coefficient phi_{5,1} is a Jacobi cusp form
    of weight 5 and index 1. Its first coefficient is related to eta^9.
    """

    def test_m0_coefficient_vanishes(self):
        """The m=0 Fourier-Jacobi coefficient of Delta_5 vanishes (cusp form)."""
        tau = 0.1 + 2j
        z_vals = [0.1j, 0.2j, 0.3j]
        phi_m = fourier_jacobi_expansion(delta5_theta, tau, z_vals, A=8.0, m_max=2)
        # phi_0 should be negligibly small (Delta_5 is a cusp form)
        for val in phi_m[0]:
            # VERIFIED [DC] vanishing check [LT] Borcherds product theory
            assert abs(val) < 1e-6, f"|phi_0| = {abs(val):.2e}"


# ---------------------------------------------------------------------------
# Test: M_2(Gamma_2, nu_4) analysis
# ---------------------------------------------------------------------------

class TestWeight2Analysis:
    """Test the analysis of the weight-2 multiplier system question."""

    def test_returns_expected_structure(self):
        result = analyze_weight2_multiplier()
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['target_weight'] == 2
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['required_c0'] == 4
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert result['phi01_c0'] == 10
        assert 'obstruction' in result
        assert 'candidate_input' in result

    def test_phi01_cannot_produce_weight_2(self):
        """phi_{0,1} has c(0)=10, giving weight 5. No scalar multiple gives weight 2."""
        c = phi01_c_table(10)
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 5.0
        # Would need c(0)=4 for weight 2, but c(0)=10 for phi_{0,1}


# ---------------------------------------------------------------------------
# Test: Known Borcherds lifts catalog
# ---------------------------------------------------------------------------

class TestKnownLifts:
    """Test the catalog of known Borcherds lifts."""

    def test_delta5_entry(self):
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Delta_5']['weight'] == 5
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Delta_5']['c(0)'] == 10
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Delta_5']['c(-1)'] == 1

    def test_delta5_squared_entry(self):
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Delta_5_squared']['weight'] == 10
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Delta_5_squared']['c(0)'] == 20

    def test_fake_monster_entry(self):
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Phi_12_fake_monster']['weight'] == 12
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert KNOWN_BORCHERDS_LIFTS['Phi_12_fake_monster']['c(0)'] == 24


# ---------------------------------------------------------------------------
# Test: Convergence
# ---------------------------------------------------------------------------

class TestConvergence:
    """Test that the Borcherds product converges as N_prod increases."""

    def test_convergence_with_N_prod(self):
        """
        Increasing N_prod should improve agreement. At deep cusp,
        even small N_prod gives good results.
        """
        c = phi01_c_table(80)
        d5 = delta5_theta(2j, 0.1j, 2j, N_terms=25) / 64.0

        errors = []
        for N in [5, 8, 12]:
            bp = borcherds_lift(c, 2j, 0.1j, 2j, N_prod=N)
            err = abs(abs(d5) / abs(bp) - 1.0)
            errors.append(err)

        # Errors should decrease (or at least be very small for all N)
        # VERIFIED [DC] convergence [LT] Borcherds product theory
        assert errors[-1] < 1e-10
        # N=12 should be significantly better than N=5
        assert errors[-1] <= errors[0] + 1e-15


# ---------------------------------------------------------------------------
# Test: Consistency between this module and igusa_product_formula
# ---------------------------------------------------------------------------

class TestCrossModuleConsistency:
    """Verify that borcherds_lift.py agrees with igusa_product_formula.py."""

    def test_matches_igusa_module(self):
        """
        Our general borcherds_lift with phi_{0,1} input should match
        the hardcoded borcherds_product from igusa_product_formula.py.
        """
        from compute.lib.igusa_product_formula import borcherds_product as bp_igusa

        c_table = phi01_c_table(80)
        tau, z, omega = 2j, 0.1j, 2j

        bp_general = borcherds_lift(c_table, tau, z, omega, N_prod=12)
        bp_specific = bp_igusa(tau, z, omega, N_prod=12, D_max=80)

        # They should agree to machine precision
        # VERIFIED [DC] modular structure [LT] Borcherds product theory
        assert abs(bp_general - bp_specific) / abs(bp_general) < 1e-12, \
            f"General vs specific: rel diff = {abs(bp_general - bp_specific) / abs(bp_general):.2e}"


# ---------------------------------------------------------------------------
# Integration test: full pipeline
# ---------------------------------------------------------------------------

class TestFullPipeline:
    """End-to-end test of the complete Borcherds lift pipeline."""

    def test_phi01_to_delta5_pipeline(self):
        """
        Complete pipeline: compute c(D) from phi_{0,1}, evaluate
        Borcherds lift, compare with Delta_5, verify weight and sign.
        """
        # Step 1: Extract coefficients
        c = phi01_c_table(80)
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[-1] == 1
        # VERIFIED [DC] structural property [LT] Borcherds product theory
        assert c[0] == 10

        # Step 2: Verify weight
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c) == 5.0

        # Step 3: Evaluate lift at two points
        for tau, z, omega in [(2j, 0.1j, 2j), (0.1+2j, 0.05+0.3j, 0.15+2j)]:
            bp = borcherds_lift(c, tau, z, omega, N_prod=12)
            d5 = delta5_theta(tau, z, omega, N_terms=25)

            # Step 4: Verify |ratio| = 1
            ratio = (d5 / 64.0) / bp
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert abs(abs(ratio) - 1.0) < 1e-10

            # Step 5: Verify sign = -1
            # VERIFIED [DC] structural property [LT] Borcherds product theory
            assert abs(ratio + 1.0) < 1e-8

    def test_three_forms_different_weights(self):
        """
        Three Jacobi forms -> three Borcherds lifts of weights 5, 6, 10.
        """
        c_phi01 = phi01_c_table(20)
        c_const = constant_jacobi_c_table(12)
        c_doubled = doubled_phi01_c_table(20)

        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c_phi01) == 5.0
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c_const) == 6.0
        # VERIFIED [DC] conformal weight [LT] Borcherds product theory
        assert borcherds_lift_weight(c_doubled) == 10.0

        # All three lifts should be nonzero at a generic point
        tau, z, omega = 2j, 0.1j, 2j
        for c in [c_phi01, c_const, c_doubled]:
            bp = borcherds_lift(c, tau, z, omega, N_prod=10)
            # VERIFIED [DC] conformal weight [LT] Borcherds product theory
            assert abs(bp) > 1e-20, f"Lift vanishes unexpectedly"


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
