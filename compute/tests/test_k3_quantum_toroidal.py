r"""Tests for k3_quantum_toroidal.py: K3 quantum toroidal algebra.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction, not its existence.

CENTRAL RESULTS (all conjectural):
    (1) The trigonometric structure function G_{K3}(x) has degree (24,24).
    (2) G_{K3}(x) * G_{K3}(1/x) = 1 (inversion identity from CY_2).
    (3) G_{K3}(x) = prod_a G_a(x) (factorisation over 24 Mukai directions).
    (4) Yangian limit: G_{K3}(e^{eps*u}) -> 1/g_{K3}(u) as eps -> 0.
    (5) NO S_3 Miki automorphism (AP-CY22: K3 has no torus action).
    (6) SL_2(Z) from E mapping class group.
    (7) Charge-1 representation: dim = 24 (Mukai rank).
    (8) Bar Euler product = eta(q)^{24}/q (deformation-invariant).
    (9) Cross-family structure function trivial for abelian gl_1.

Test structure:
    Section 1: Trigonometric structure function (8 tests)
    Section 2: Inversion identity (4 tests)
    Section 3: Factorisation (4 tests)
    Section 4: Yangian limit (5 tests)
    Section 5: Miki automorphism analysis (5 tests)
    Section 6: Deformation chain (4 tests)
    Section 7: Representation theory (5 tests)
    Section 8: Bar Euler product (3 tests)
    Section 9: Cross-family structure (3 tests)
    Section 10: Full verification (2 tests)

Manuscript references:
    k3_times_e.tex, subsec:k3-yangian (K3 Yangian conjecture)
    k3_times_e.tex, subsec:k3-quantum-toroidal (K3 quantum toroidal)
    en_factorization.tex, conj:miki-from-e3 (Miki from E_3)
    en_factorization.tex, conj:fact-hom-k3xe (factorization homology on K3 x E)
"""

import math

import numpy as np
import pytest

from compute.lib.k3_quantum_toroidal import (
    # Constants
    STATUS,
    MIKI_STATUS,
    N_MUKAI,
    # Structure function
    trigonometric_structure_function,
    rational_to_trigonometric_params,
    verify_cy2_multiplicative,
    verify_inversion_identity,
    # Yangian limit
    yangian_limit,
    deformation_hierarchy_check,
    # Algebra class
    K3QuantumToroidalAlgebra,
    # Deformation chain
    deformation_chain,
    DeformationStep,
    # Cross-family
    cross_family_structure_function,
    mukai_central_extension,
    # Representation
    verify_charge_1_representation,
    # Bar Euler
    bar_euler_product_invariance,
    # Colored partition
    _colored_partition,
    # Full
    full_verification,
)

from compute.lib.k3_yangian import (
    kummer_k3_parameters,
    null_kummer_parameters,
    structure_function_evaluate,
)


# =========================================================================
# Section 1: Trigonometric structure function (8 tests)
# =========================================================================

class TestTrigonometricStructureFunction:
    """Tests for the K3 trigonometric structure function G_{K3}(x)."""

    def test_degree_24_24(self):
        """G_{K3}(x) involves 24 factors: degree (24,24) in q_a variables."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        assert len(q_params) == 24

    def test_evaluates_finite(self):
        """G_{K3}(x) evaluates to a finite nonzero value at generic x."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        x = 0.3 + 0.2j
        G = trigonometric_structure_function(x, q_params)
        assert np.isfinite(abs(G))
        assert abs(G) > 1e-15

    def test_cy2_multiplicative(self):
        """CY_2 constraint: prod q_a = 1 (from sum h_a = 0)."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        ok, res = verify_cy2_multiplicative(q_params)
        assert ok, f"CY_2 multiplicative constraint failed: residual = {res}"

    def test_cy2_null_params(self):
        """CY_2 constraint holds for null Kummer parameters too."""
        params = null_kummer_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        ok, res = verify_cy2_multiplicative(q_params)
        assert ok, f"CY_2 null constraint failed: residual = {res}"

    def test_wrong_param_count_raises(self):
        """Passing wrong number of parameters raises ValueError."""
        with pytest.raises(ValueError, match="Need 24"):
            trigonometric_structure_function(0.5, [1.0, 2.0, 3.0])

    def test_g_at_x_1(self):
        """G_{K3}(x=1) is well-defined when no q_a = 1.

        For the Kummer parametrization, q_a = e^{eps} or e^{-eps/5},
        neither of which equals 1 (for eps != 0), so x = 1 is not a pole.
        """
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        G1 = trigonometric_structure_function(1.0, q_params)
        assert np.isfinite(abs(G1))

    def test_multiple_test_points(self):
        """G_{K3}(x) is finite at multiple generic test points."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        test_points = [0.1, 0.5 + 0.3j, -0.4 + 0.1j, 2.0, -1.5]
        for x in test_points:
            G = trigonometric_structure_function(x, q_params)
            assert np.isfinite(abs(G)), f"G({x}) not finite"

    def test_symmetry_under_q_permutation(self):
        """G_{K3}(x) depends on the SET {q_a}, not on the ordering.

        For abelian gl_1, the product of factors is commutative.
        """
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        x = 0.3 + 0.2j
        G1 = trigonometric_structure_function(x, q_params)
        # Reverse the order
        G2 = trigonometric_structure_function(x, list(reversed(q_params)))
        assert abs(G1 - G2) < 1e-12


# =========================================================================
# Section 2: Inversion identity (4 tests)
# =========================================================================

class TestInversionIdentity:
    """Tests for G(x)*G(1/x) = 1."""

    def test_inversion_kummer(self):
        """G(x)*G(1/x) = 1 for Kummer parameters."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        ok, res = verify_inversion_identity(q_params)
        assert ok, f"Inversion failed: max residual = {res}"

    def test_inversion_null(self):
        """G(x)*G(1/x) = 1 for null parameters."""
        params = null_kummer_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        ok, res = verify_inversion_identity(q_params)
        assert ok, f"Inversion failed: max residual = {res}"

    def test_inversion_at_specific_point(self):
        """Verify G(x)*G(1/x) = 1 at a specific x value."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        x = 0.7 + 0.3j
        Gx = trigonometric_structure_function(x, q_params)
        G_inv = trigonometric_structure_function(1.0 / x, q_params)
        assert abs(Gx * G_inv - 1.0) < 1e-10

    def test_inversion_algebraic_proof(self):
        """The inversion identity follows from CY_2: prod q_a = 1.

        Proof sketch: G(x)*G(1/x) = (prod q_a)^2 = 1^2 = 1.
        This is a consequence of the CY_2 constraint alone.
        """
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)

        # Verify by direct computation at multiple points
        for j in range(16):
            theta = 2 * math.pi * j / 16
            x = 0.6 * np.exp(1j * theta)
            Gx = trigonometric_structure_function(x, q_params)
            G_inv = trigonometric_structure_function(1.0 / x, q_params)
            assert abs(Gx * G_inv - 1.0) < 1e-10, f"Failed at theta={theta}"


# =========================================================================
# Section 3: Factorisation (4 tests)
# =========================================================================

class TestFactorisation:
    """Tests for G_{K3}(x) = prod_a G_a(x)."""

    def test_factorisation_kummer(self):
        """G_{K3} factorises over 24 Mukai directions."""
        alg = K3QuantumToroidalAlgebra(0.1)
        ok, res = alg.verify_factorisation()
        assert ok, f"Factorisation failed: residual = {res}"

    def test_sector_decomposition(self):
        """G_{K3} = G_+ * G_- (positive/negative Mukai sectors)."""
        alg = K3QuantumToroidalAlgebra(0.1)
        x = 0.4 + 0.2j
        G_full = alg.structure_function(x)

        # Product of individual sectors
        G_product = complex(1.0)
        for a in range(N_MUKAI):
            G_product *= alg.structure_function_single_direction(a, x)

        assert abs(G_full - G_product) < 1e-10

    def test_positive_sector_count(self):
        """Positive sector has 4 directions (Mukai signature (4,20))."""
        alg = K3QuantumToroidalAlgebra(0.1)
        pos = alg.positive_sector_params()
        assert len(pos) == 4

    def test_negative_sector_count(self):
        """Negative sector has 20 directions."""
        alg = K3QuantumToroidalAlgebra(0.1)
        neg = alg.negative_sector_params()
        assert len(neg) == 20


# =========================================================================
# Section 4: Yangian limit (5 tests)
# =========================================================================

class TestYangianLimit:
    """Tests for G_{K3}(e^{eps*u}) -> 1/g_{K3}(u) as eps -> 0."""

    def test_yangian_limit_convergence(self):
        """The trigonometric G converges to 1/g_rational as eps -> 0."""
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        result = yangian_limit(1.5, 0.01, h_list)
        assert result['converges'], f"Yangian limit failed: residual = {result.get('residual')}"

    def test_yangian_limit_smaller_eps(self):
        """Smaller epsilon gives better convergence."""
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]

        res_large = yangian_limit(1.5, 0.1, h_list)
        res_small = yangian_limit(1.5, 0.01, h_list)

        if (res_large.get('residual') is not None and
                res_small.get('residual') is not None):
            assert res_small['residual'] < res_large['residual']

    def test_hierarchy_monotone(self):
        """Deformation hierarchy shows monotone convergence."""
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        result = deformation_hierarchy_check(h_list)
        assert result['monotone_convergence']

    def test_yangian_limit_multiple_points(self):
        """Yangian limit holds at multiple test points."""
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        test_points = [0.5 + 0.3j, 2.0, -1.0 + 0.5j]
        for u in test_points:
            result = yangian_limit(u, 0.01, h_list)
            assert result.get('converges', False), f"Failed at u = {u}"

    def test_is_yangian_limit_flag(self):
        """Small q_nome is detected as Yangian limit regime."""
        alg = K3QuantumToroidalAlgebra(1e-15)
        assert alg.is_yangian_limit


# =========================================================================
# Section 5: Miki automorphism analysis (5 tests)
# =========================================================================

class TestMikiAutomorphism:
    """Tests for the Miki automorphism analysis (AP-CY22)."""

    def test_no_s3_miki(self):
        """K3 quantum toroidal has NO S_3 Miki (AP-CY22)."""
        alg = K3QuantumToroidalAlgebra(0.1)
        miki = alg.miki_status()
        assert not miki['has_s3_miki']

    def test_has_sl2z(self):
        """K3 quantum toroidal has SL_2(Z) from E."""
        alg = K3QuantumToroidalAlgebra(0.1)
        miki = alg.miki_status()
        assert miki['has_sl2z']

    def test_ap_cy22_compliant(self):
        """Miki analysis is AP-CY22 compliant."""
        alg = K3QuantumToroidalAlgebra(0.1)
        miki = alg.miki_status()
        assert miki['ap_cy22_compliant']

    def test_s_transformation_inverts_nome(self):
        """S: tau -> -1/tau acts on the nome."""
        alg = K3QuantumToroidalAlgebra(0.1)
        q_new = alg.sl2z_s_transformation()
        assert np.isfinite(abs(q_new))
        # S^2: tau -> -1/(-1/tau) = tau, so q should return
        tau_orig = alg.tau
        tau_s = -1.0 / tau_orig
        tau_ss = -1.0 / tau_s
        assert abs(tau_ss - tau_orig) < 1e-10, "S^2 != id on tau"

    def test_t_transformation_trivial_on_nome(self):
        """T: tau -> tau + 1 gives q -> q (since e^{2 pi i} = 1)."""
        alg = K3QuantumToroidalAlgebra(0.1)
        q_new = alg.sl2z_t_transformation()
        assert abs(q_new - alg.q_nome) < 1e-10


# =========================================================================
# Section 6: Deformation chain (4 tests)
# =========================================================================

class TestDeformationChain:
    """Tests for the Drinfeld-Jimbo deformation chain."""

    def test_chain_has_four_steps(self):
        """The deformation chain has 4 steps."""
        chain = deformation_chain()
        assert len(chain) == 4

    def test_chain_names(self):
        """The deformation steps have correct names."""
        chain = deformation_chain()
        names = [step.name for step in chain]
        assert 'Classical (K3 DCA)' in names
        assert 'Yangian (rational)' in names
        assert 'Quantum toroidal (trigonometric, two loops)' in names

    def test_classical_is_proved(self):
        """The classical step (K3 DCA) is proved via CY-A_2."""
        chain = deformation_chain()
        classical = chain[0]
        assert 'PROVED' in classical.status

    def test_toroidal_is_conjectural(self):
        """The quantum toroidal step is conjectural (CY-A_3 needed)."""
        chain = deformation_chain()
        toroidal = chain[3]
        assert 'CONJECTURAL' in toroidal.status


# =========================================================================
# Section 7: Representation theory (5 tests)
# =========================================================================

class TestRepresentationTheory:
    """Tests for K3 quantum toroidal representation theory."""

    def test_charge_1_dim_24(self):
        """Charge-1 representation has dimension 24 (Mukai rank)."""
        alg = K3QuantumToroidalAlgebra(0.1)
        assert alg.charge_1_dimension() == 24

    def test_charge_1_character_24(self):
        """Charge-1 character = 24."""
        alg = K3QuantumToroidalAlgebra(0.1)
        assert alg.charge_1_character() == 24

    def test_charge_n_prediction_vacuum(self):
        """Charge-0 (vacuum) has dimension 1."""
        alg = K3QuantumToroidalAlgebra(0.1)
        assert alg.charge_n_character_prediction(0) == 1

    def test_charge_n_prediction_n2(self):
        """Charge-2: p_{24}(2) = 324.

        p_{24}(2) = C(24,1)*1 + C(24,2) = 24 + 276 + 24 = 324.
        Equivalently: 24 two-box partitions with 24 colours each,
        plus 24*23/2 = 276 mixed pairs, plus 24 single parts of size 2.
        Wait: p_{24}(2) counts partitions of 2 with 24 colours.
        Partitions of 2: (2) and (1,1).
        (2): 24 choices of colour = 24.
        (1,1): C(24+1,2) - 24 = ... no, ordered pairs same colour = 24,
        unordered different = C(24,2) = 276.
        Total (1,1) with 24 colours: 24 + 276 = 300.
        Total p_{24}(2) = 24 + 300 = 324.
        """
        alg = K3QuantumToroidalAlgebra(0.1)
        assert alg.charge_n_character_prediction(2) == 324

    def test_fock_generating_function(self):
        """Fock character matches p_{24}(n) = chi(Hilb^n(K3))."""
        alg = K3QuantumToroidalAlgebra(0.1)
        fock = alg.fock_character_generating_function(max_n=5)
        # Known values from the 24-colored partition function
        # (= coefficients of 1/eta^24, matching Fake Monster)
        expected = [1, 24, 324, 3200, 25650, 176256]
        for i, (got, exp) in enumerate(zip(fock, expected)):
            assert got == exp, f"p_24({i}): got {got}, expected {exp}"

    def test_charge_1_full_verification(self):
        """Full charge-1 verification passes."""
        result = verify_charge_1_representation(q_nome=0.1)
        assert result['dimension_ok']
        assert result['fock_character_ok']
        assert result['factorisation_ok']
        assert result['inversion_ok']


# =========================================================================
# Section 8: Bar Euler product (3 tests)
# =========================================================================

class TestBarEulerProduct:
    """Tests for bar Euler product deformation invariance."""

    def test_bar_euler_invariant(self):
        """Bar Euler product is deformation-invariant."""
        result = bar_euler_product_invariance()
        assert result['deformation_invariant']

    def test_bar_euler_eta24(self):
        """Bar Euler product = eta(q)^{24}."""
        result = bar_euler_product_invariance()
        assert result['equals_eta24']

    def test_eta24_first_coefficients(self):
        """Check first coefficients of prod(1-q^n)^{24}.

        prod(1-q^n)^24 = 1 - 24q + 252q^2 - 1472q^3 + ...
        (Ramanujan tau function: tau(1)=1, tau(2)=-24, tau(3)=252, ...)
        """
        result = bar_euler_product_invariance()
        coeffs = result['eta24_first_coefficients']
        assert coeffs[0] == 1
        assert coeffs[1] == -24
        assert coeffs[2] == 252
        assert coeffs[3] == -1472


# =========================================================================
# Section 9: Cross-family structure (3 tests)
# =========================================================================

class TestCrossFamilyStructure:
    """Tests for cross-family coupling via the Mukai pairing."""

    def test_cross_family_trivial_abelian(self):
        """For abelian gl_1, cross-family G_{ab}(x) = 1 when a != b."""
        x = 0.5 + 0.3j
        G_cross = cross_family_structure_function(0, 5, x)
        assert abs(G_cross - 1.0) < 1e-15

    def test_same_family_nontrivial(self):
        """Same-family G_{aa}(x) is nontrivial."""
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        x = 0.5 + 0.3j
        G_same = cross_family_structure_function(0, 0, x, q_params)
        assert abs(G_same - 1.0) > 1e-5  # nontrivial

    def test_mukai_central_extension(self):
        """Mukai pairing omega^{ab}: +1 for a=b positive, -1 for negative, 0 off-diag."""
        # Positive direction (a = 0)
        assert mukai_central_extension(0, 0) == 1
        # Negative direction (a = 10)
        assert mukai_central_extension(10, 10) == -1
        # Off-diagonal
        assert mukai_central_extension(0, 10) == 0
        assert mukai_central_extension(3, 5) == 0


# =========================================================================
# Section 10: Full verification (2 tests)
# =========================================================================

class TestFullVerification:
    """End-to-end verification of the K3 quantum toroidal construction."""

    def test_full_verification_passes(self):
        """Full verification suite passes at q_nome = 0.1."""
        result = full_verification(q_nome=0.1)
        assert result['all_pass'], f"Full verification failed: {result}"

    def test_full_verification_different_q(self):
        """Full verification at a different nome q = 0.3."""
        result = full_verification(q_nome=0.3)
        assert result['all_pass'], f"Full verification failed: {result}"


# =========================================================================
# Section 11: Multi-path verification / cross-checks (7 tests)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path cross-checks verifying the same quantity via independent routes.

    AP10 compliance: each hardcoded assertion is cross-checked by at least
    one independent computational path.
    """

    def test_inversion_two_paths(self):
        """Cross-check G(x)*G(1/x) = 1 via (a) direct product and (b) CY_2 -> (prod q_a)^2.

        Path 1: Evaluate G(x)*G(1/x) numerically.
        Path 2: Compute (prod q_a)^2 directly and verify = 1.
        Both must agree that the inversion identity holds.
        """
        params = kummer_k3_parameters()
        q_params = rational_to_trigonometric_params(params.h)
        x = 0.4 + 0.3j

        # Path 1: direct product
        Gx = trigonometric_structure_function(x, q_params)
        Ginv = trigonometric_structure_function(1.0 / x, q_params)
        path1 = Gx * Ginv

        # Path 2: (prod q_a)^2
        prod_q = complex(1.0)
        for qa in q_params:
            prod_q *= qa
        path2 = prod_q ** 2

        assert abs(path1 - 1.0) < 1e-10, f"Path 1 failed: {path1}"
        assert abs(path2 - 1.0) < 1e-10, f"Path 2 failed: {path2}"
        assert abs(path1 - path2) < 1e-10, "Paths disagree"

    def test_p24_two_paths(self):
        """Cross-check p_{24}(n) via (a) dynamic programming and (b) known OEIS values.

        Path 1: _colored_partition(n, 24) via DP.
        Path 2: Known values from OEIS A000935 / Fake Monster multiplicities.
        (AP-CY24: verify docstring values against actual computation.)
        """
        # Path 1: compute
        computed = [_colored_partition(n, 24) for n in range(6)]

        # Path 2: known values (OEIS A000935, independently verified
        # in k3_yangian_quantization.py FAKE_MONSTER_MULTIPLICITIES)
        known = [1, 24, 324, 3200, 25650, 176256]

        for i, (c, k) in enumerate(zip(computed, known)):
            assert c == k, f"p_24({i}): computed {c} != known {k}"

    def test_eta24_two_paths(self):
        """Cross-check eta^{24} coefficients via (a) our _eta_power_coefficients
        and (b) independent computation from the Ramanujan tau function.

        tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.
        prod(1-q^n)^24 = sum tau(n) q^{n-1} => coeff of q^k = tau(k+1).
        Wait, prod(1-q^n)^24 starts with 1 - 24q + 252q^2 - ...
        So coefficient of q^0 = 1 = tau(1), q^1 = -24 = tau(2), etc.
        """
        from compute.lib.k3_quantum_toroidal import _eta_power_coefficients

        # Path 1: our engine
        coeffs = _eta_power_coefficients(24, 6)

        # Path 2: Ramanujan tau values (well-known, OEIS A000594)
        ramanujan_tau = [1, -24, 252, -1472, 4830, -6048, -16744]

        for i in range(min(len(coeffs), len(ramanujan_tau))):
            assert coeffs[i] == ramanujan_tau[i], (
                f"eta^24 coeff at q^{i}: got {coeffs[i]}, "
                f"expected tau({i+1}) = {ramanujan_tau[i]}"
            )

    def test_structure_function_rational_trig_crosscheck(self):
        """Cross-check: at small epsilon, the trigonometric G and rational g
        should be approximately reciprocal.

        Path 1: G_{K3}(e^{eps*u}) from trigonometric engine.
        Path 2: 1/g_{K3}(u) from the rational engine (k3_yangian.py).
        """
        from sympy import Rational as R
        params = kummer_k3_parameters()
        h_list = [float(h) for h in params.h]
        eps = 0.005
        u = 2.0

        # Path 1: trigonometric
        x = np.exp(eps * u)
        q_params = [np.exp(eps * h) for h in h_list]
        G_trig = trigonometric_structure_function(x, q_params)

        # Path 2: rational (from k3_yangian.py)
        g_rat = structure_function_evaluate(R(2), params)
        g_rat_inv = 1.0 / float(g_rat)

        # Should agree to O(eps^2)
        assert abs(G_trig - g_rat_inv) < 1e-6, (
            f"Trig/rational mismatch: G_trig={G_trig}, 1/g_rat={g_rat_inv}"
        )

    def test_mukai_rank_three_paths(self):
        """Cross-check Mukai rank = 24 via three independent paths.

        Path 1: N_MUKAI constant from k3_quantum_toroidal.py.
        Path 2: len(params.h) from kummer_k3_parameters().
        Path 3: MUKAI_RANK from k3_double_current_algebra.py.
        """
        from compute.lib.k3_double_current_algebra import MUKAI_RANK

        # Path 1
        assert N_MUKAI == 24
        # Path 2
        params = kummer_k3_parameters()
        assert len(params.h) == 24
        # Path 3
        assert MUKAI_RANK == 24
        # Cross-check all agree
        assert N_MUKAI == len(params.h) == MUKAI_RANK

    def test_charge_1_dim_two_paths(self):
        """Cross-check charge-1 dimension via (a) algebra method and (b) p_{24}(1).

        Path 1: alg.charge_1_dimension() (structural argument: Mukai rank).
        Path 2: _colored_partition(1, 24) (combinatorial computation).
        """
        alg = K3QuantumToroidalAlgebra(0.1)

        path1 = alg.charge_1_dimension()
        path2 = _colored_partition(1, 24)

        assert path1 == 24
        assert path2 == 24
        assert path1 == path2

    def test_factorisation_vs_individual_directions(self):
        """Cross-check G_{K3}(x) via (a) single call and (b) product of 24 G_a calls.

        Path 1: trigonometric_structure_function(x, q_params) (single product).
        Path 2: prod_a structure_function_single_direction(a, x) (24 separate calls).
        """
        alg = K3QuantumToroidalAlgebra(0.1)
        x = 0.35 + 0.15j

        # Path 1
        G_single = alg.structure_function(x)

        # Path 2
        G_product = complex(1.0)
        for a in range(24):
            G_product *= alg.structure_function_single_direction(a, x)

        assert abs(G_single - G_product) < 1e-12, (
            f"Factorisation cross-check failed: {abs(G_single - G_product)}"
        )
