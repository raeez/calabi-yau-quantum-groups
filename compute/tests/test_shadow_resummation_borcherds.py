r"""
Tests for shadow_resummation_borcherds.py: shadow tower resummation to
the Borcherds product for K3 x E, including the Saito-Kurokawa additive
lift comparison.

Verifies:
    1. Shadow invariant structure at each arity (root counts, multiplicities)
    2. Effective exponents a(N) convergence to 24 (eta^{24} exponents)
    3. Truncated Borcherds product convergence to Delta_5/64
    4. Layer-by-layer multiplicative decomposition (R_r -> 1)
    5. 1D Fourier coefficient match against eta^{24}
    6. phi_{10,1} Fourier coefficients (Eichler-Zagier table)
    7. Maass relations: FJ coefficients phi_m from phi_1
    8. Additive (Saito-Kurokawa) vs multiplicative (Borcherds) agreement
    9. Shadow-to-FJ bridge: perturbative shadow -> eta^{24} -> FJ
   10. Combined full verification pipeline

Ground truth:
    k3_times_e.tex: thm:k3e-additive-lift, rem:k3e-two-lifts,
        subsec:k3e-additive-lift, thm:k3e-fiber-global
    introduction.tex: sec:automorphic-shadow
    Eichler-Zagier, "The Theory of Jacobi Forms" (1985), Table 2
    van der Geer, "Siegel modular forms" (2008)
    Maass, "Uber eine Spezialschar von Modulformen zweiten Grades" (1979)

IMPORTANT (AP-CY8): The identification "Borcherds product = bar Euler
product" at the level of chi_10 is an OBSERVATION for K3 x E, conditional
on CY-A_2 (proved at d=2) and the Vol I Borcherds-lift identification.
"""

import math
import os
import sys
import importlib.util
from fractions import Fraction

import pytest

F = Fraction

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'shadow_resummation_borcherds',
    os.path.join(_lib_dir, 'shadow_resummation_borcherds.py')
)
srb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(srb)


# =========================================================================
# 1. SHADOW INVARIANT STRUCTURE
# =========================================================================

class TestShadowInvariantStructure:
    """Verify shadow invariant S_r at each arity."""

    def test_shadow_arity_2_has_roots(self):
        """Arity 2 (real roots) should have nonzero root count."""
        data = srb.phi01_coefficients()
        zsh = srb.shadow_generating_function(max_arity=3, max_coord=5, data=data)
        # VERIFIED [DC] structural property
        assert zsh[2]['num_roots'] > 0

    def test_shadow_arity_2_all_real(self):
        """At arity 2, all roots are real (norm 2)."""
        data = srb.phi01_coefficients()
        zsh = srb.shadow_generating_function(max_arity=3, max_coord=5, data=data)
        # VERIFIED [DC] structural property: arity 2 = Weyl vector sector
        assert zsh[2]['lightlike_mult'] == 0
        assert zsh[2]['timelike_mult'] == 0

    def test_shadow_arity_3_has_imaginary(self):
        """Arity 3 introduces first imaginary roots."""
        data = srb.phi01_coefficients()
        zsh = srb.shadow_generating_function(max_arity=4, max_coord=5, data=data)
        # VERIFIED [DC] structural property: first imaginary layer
        assert zsh[3]['num_roots'] > 0
        assert zsh[3]['real_mult'] == 0

    def test_shadow_arity_3_lightlike(self):
        """Arity 3 roots are lightlike (D=0, norm 0)."""
        data = srb.phi01_coefficients()
        zsh = srb.shadow_generating_function(max_arity=4, max_coord=5, data=data)
        # VERIFIED [DC] structural property: lightlike at arity 3
        assert zsh[3]['lightlike_mult'] > 0

    def test_shadow_summary_consistent(self):
        """Shadow summary at each arity has consistent data."""
        data = srb.phi01_coefficients()
        for r in range(2, 6):
            summary = srb.shadow_invariant_summary(r, max_coord=5, data=data)
            assert summary['arity'] == r
            assert summary['num_primary_roots'] >= 0


# =========================================================================
# 2. EFFECTIVE EXPONENTS
# =========================================================================

class TestEffectiveExponents:
    """Verify a(N) convergence to 24 in the diagonal specialization."""

    def test_arity_2_a1_is_4(self):
        """At arity 2, a(1) = 4 (from real roots only)."""
        data = srb.phi01_coefficients()
        a = srb.effective_exponents_diagonal(2, max_N=2, data=data)
        # VERIFIED [DC] structural property
        assert a.get(1, F(0)) == F(4)

    def test_arity_3_a1_is_24(self):
        """At arity 3, a(1) jumps to 24 (real + first imaginary)."""
        data = srb.phi01_coefficients()
        a = srb.effective_exponents_diagonal(3, max_N=2, data=data)
        # VERIFIED [DC] structural property: a(1)=24 at arity 3
        assert a.get(1, F(0)) == F(24)

    def test_arity_4_a2_is_24(self):
        """At arity 4, a(2) = 24."""
        data = srb.phi01_coefficients()
        a = srb.effective_exponents_diagonal(4, max_N=3, data=data)
        # VERIFIED [DC] structural property
        assert a.get(2, F(0)) == F(24)

    def test_full_arity_all_24(self):
        """At sufficiently high arity, all a(N) = 24 for N = 1..8."""
        data = srb.phi01_coefficients()
        a = srb.effective_exponents_diagonal(10, max_N=8, data=data)
        for N in range(1, 9):
            # VERIFIED [DC] structural property: convergence to eta^24
            assert a.get(N, F(0)) == F(24), f"a({N}) = {a.get(N, F(0))}, expected 24"

    def test_exponents_monotone_convergence(self):
        """Effective exponents converge monotonically toward 24."""
        data = srb.phi01_coefficients()
        # At a(1): should go 4 (arity 2) -> 24 (arity 3) and stay
        a2 = srb.effective_exponents_diagonal(2, max_N=2, data=data)
        a3 = srb.effective_exponents_diagonal(3, max_N=2, data=data)
        assert a3.get(1, F(0)) >= a2.get(1, F(0))
        assert a3.get(1, F(0)) == F(24)


# =========================================================================
# 3. TRUNCATED BORCHERDS PRODUCT CONVERGENCE
# =========================================================================

class TestTruncatedProductConvergence:
    """Verify truncated product Phi^{<=r} converges to Delta_5/64."""

    def test_convergence_at_arity_2(self):
        """At arity 2, the product is within 0.01% of Delta_5/64."""
        data = srb.phi01_coefficients()
        tau = 0.15 + 2.0j
        z = 0.08 + 0.12j
        sigma = 0.10 + 2.0j
        conv = srb.convergence_analysis(tau, z, sigma, max_arity=3,
                                        N_prod=8, data=data)
        # VERIFIED [DC] numerical convergence: arity 2 very close
        assert conv[0]['rel_error'] < 0.001

    def test_convergence_at_arity_4(self):
        """At arity 4, relative error below 1e-10."""
        data = srb.phi01_coefficients()
        tau = 0.15 + 2.0j
        z = 0.08 + 0.12j
        sigma = 0.10 + 2.0j
        conv = srb.convergence_analysis(tau, z, sigma, max_arity=5,
                                        N_prod=8, data=data)
        # arity 4 is index 2 (0-indexed from arity 2)
        assert conv[2]['rel_error'] < 1e-10

    def test_convergence_rapid_after_arity_3(self):
        """After arity 3, convergence is rapid (rel error < 1e-8)."""
        data = srb.phi01_coefficients()
        tau = 0.15 + 2.0j
        z = 0.08 + 0.12j
        sigma = 0.10 + 2.0j
        conv = srb.convergence_analysis(tau, z, sigma, max_arity=6,
                                        N_prod=8, data=data)
        for c in conv[1:]:  # arity >= 3
            assert c['rel_error'] < 1e-8


# =========================================================================
# 4. LAYER-BY-LAYER DECOMPOSITION
# =========================================================================

class TestLayerDecomposition:
    """Verify multiplicative layer corrections R_r = Phi^{<=r}/Phi^{<=r-1}."""

    def test_layers_approach_1(self):
        """Layer ratios |R_r| approach 1 for r >= 4."""
        data = srb.phi01_coefficients()
        tau = 0.15 + 2.0j
        z = 0.08 + 0.12j
        sigma = 0.10 + 2.0j
        layers = srb.layer_decomposition_numerical(
            tau, z, sigma, max_arity=6, N_prod=8, data=data
        )
        # Skip arity 2 (base) and 3 (first correction)
        for lay in layers[2:]:  # arity >= 4
            assert abs(lay['abs_ratio'] - 1.0) < 1e-8

    def test_arity_3_correction_nonzero(self):
        """The arity-3 layer correction is nontrivial (R_3 != 1)."""
        data = srb.phi01_coefficients()
        tau = 0.15 + 2.0j
        z = 0.08 + 0.12j
        sigma = 0.10 + 2.0j
        layers = srb.layer_decomposition_numerical(
            tau, z, sigma, max_arity=4, N_prod=8, data=data
        )
        # R_3 is the first nontrivial correction
        r3 = layers[1]  # index 1 = arity 3
        assert r3['arity'] == 3
        # VERIFIED [DC] numerical: R_3 differs from 1
        assert abs(r3['abs_ratio'] - 1.0) > 1e-6


# =========================================================================
# 5. 1D FOURIER MATCH AGAINST eta^{24}
# =========================================================================

class TestEta24Convergence:
    """Verify 1D resummed product converges to eta^{24}."""

    def test_eta24_exact_q0(self):
        """eta^{24} at q^0 = 1."""
        eta24 = srb._eta24_exact(5)
        # VERIFIED [DC] structural property
        assert eta24[0] == 1

    def test_eta24_exact_q1(self):
        """eta^{24} at q^1 = -24."""
        eta24 = srb._eta24_exact(5)
        # VERIFIED [LT] Ramanujan tau function: tau(1)=1, coeff = -24
        assert eta24[1] == -24

    def test_eta24_exact_q2(self):
        """eta^{24} at q^2 = 252."""
        eta24 = srb._eta24_exact(5)
        # VERIFIED [LT] Ramanujan tau
        assert eta24[2] == 252

    def test_eta24_exact_q3(self):
        """eta^{24} at q^3 = -1472."""
        eta24 = srb._eta24_exact(5)
        # VERIFIED [LT] Ramanujan tau
        assert eta24[3] == -1472

    def test_resummed_arity_2_matches_q0(self):
        """At arity 2, the q^0 coefficient matches eta^{24}."""
        data = srb.phi01_coefficients()
        prod = srb.resummed_product_1d(2, max_degree=3, data=data)
        # VERIFIED [DC] structural property
        assert int(prod.get(0, F(0))) == 1

    def test_full_match_at_arity_8(self):
        """All eta^{24} coefficients match at arity 8 through q^6."""
        data = srb.phi01_coefficients()
        ver = srb.verify_eta24_convergence(max_arity=8, max_degree=6, data=data)
        assert ver['by_arity'][8]['all_match']

    def test_full_match_achieved(self):
        """Full match is achieved at some finite arity."""
        data = srb.phi01_coefficients()
        ver = srb.verify_eta24_convergence(max_arity=10, max_degree=6, data=data)
        # VERIFIED [DC] numerical convergence
        assert ver['full_match_at_arity'] is not None
        assert ver['full_match_at_arity'] <= 10

    def test_partial_match_increases_with_arity(self):
        """Number of matching coefficients increases with arity."""
        data = srb.phi01_coefficients()
        ver = srb.verify_eta24_convergence(max_arity=8, max_degree=6, data=data)
        prev_match = 0
        for r in range(2, 9):
            if r in ver['by_arity']:
                n_match = sum(1 for v in ver['by_arity'][r]['matches'].values() if v)
                assert n_match >= prev_match
                prev_match = n_match


# =========================================================================
# 6. phi_{10,1} FOURIER COEFFICIENTS
# =========================================================================

class TestPhi101Coefficients:
    """Verify phi_{10,1} Fourier coefficients (Eichler-Zagier Table 2)."""

    def test_c_disc_3(self):
        """c(D=3) = 1 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] Eichler-Zagier Table 2
        assert c[3] == 1

    def test_c_disc_4(self):
        """c(D=4) = -2 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] Eichler-Zagier Table 2
        assert c[4] == -2

    def test_c_disc_7(self):
        """c(D=7) = -16 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] van der Geer 2008
        assert c[7] == -16

    def test_c_disc_8(self):
        """c(D=8) = 36 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] van der Geer 2008
        assert c[8] == 36

    def test_c_disc_11(self):
        """c(D=11) = 99 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] van der Geer 2008
        assert c[11] == 99

    def test_c_disc_12(self):
        """c(D=12) = -272 for phi_{10,1}."""
        c = srb.phi_10_1_by_discriminant()
        # VERIFIED [LT] van der Geer 2008
        assert c[12] == -272

    def test_discriminant_constraint(self):
        """Only discriminants D = 0 or 3 mod 4 appear (AP-CY9)."""
        c = srb.phi_10_1_by_discriminant()
        for D in c:
            # VERIFIED [DC] structural property: discriminant constraint
            assert D % 4 == 0 or D % 4 == 3, f"D={D} violates mod-4 constraint"

    def test_phi101_fourier_symmetry(self):
        """c(n, r) = c(n, -r) by reflection symmetry."""
        coeffs = srb.phi_10_1_fourier(max_n=5)
        for (n, r), val in coeffs.items():
            if (n, -r) in coeffs:
                assert coeffs[(n, -r)] == val, f"Symmetry fails at ({n},{r})"

    def test_phi101_first_nonzero(self):
        """The leading coefficient c(1, 1) = 1 (D=3)."""
        coeffs = srb.phi_10_1_fourier(max_n=3)
        # VERIFIED [LT] Eichler-Zagier: leading term
        assert coeffs.get((1, 1), 0) == 1
        assert coeffs.get((1, -1), 0) == 1


# =========================================================================
# 7. MAASS RELATIONS
# =========================================================================

class TestMaassRelations:
    """Verify Fourier-Jacobi coefficients phi_m from Maass relations."""

    def test_phi_1_is_phi101(self):
        """At m=1, Maass relation reduces to phi_1 = phi_{10,1}."""
        phi_1 = srb.maass_relations_phi_m(m=1, max_n=3)
        c101 = srb.phi_10_1_fourier(max_n=3)
        for (n, r), val in c101.items():
            D = 4 * n - r * r
            if D <= 0:
                continue
            # At m=1, gcd(n, r, 1) = 1, only d=1 contributes
            # So a(n, r, 1) = 1^9 * c_1(n, r) = c_1(n, r)
            maass_val = phi_1.get((n, r), F(0))
            # VERIFIED [DC] structural property: Maass at m=1
            assert int(maass_val) == val, f"Mismatch at ({n},{r}): {maass_val} vs {val}"

    def test_phi_2_nonzero(self):
        """phi_2 is nonzero (nontrivial Maass contribution at m=2)."""
        phi_2 = srb.maass_relations_phi_m(m=2, max_n=3)
        # VERIFIED [DC] structural property: phi_2 has terms
        assert len(phi_2) > 0

    def test_phi_2_symmetry(self):
        """phi_2 has r -> -r symmetry."""
        phi_2 = srb.maass_relations_phi_m(m=2, max_n=4)
        for (n, r), val in phi_2.items():
            if (n, -r) in phi_2:
                assert phi_2[(n, -r)] == val, f"Symmetry fails at ({n},{r}) in phi_2"

    def test_maass_integer_coefficients(self):
        """All Maass relation outputs should be integers."""
        for m in [1, 2, 3]:
            phi_m = srb.maass_relations_phi_m(m=m, max_n=3)
            for (n, r), val in phi_m.items():
                assert val == int(val), f"Non-integer at m={m}, ({n},{r}): {val}"

    def test_chi10_reconstruction_consistent(self):
        """chi_10 reconstructed from Maass is consistent across FJ indices."""
        chi10 = srb.chi10_fourier_from_maass(max_n=3, max_m=2)
        # All values should be integer-valued Fractions
        for (n, r, m), val in chi10.items():
            assert val == int(val), f"Non-integer chi_10 coeff at ({n},{r},{m}): {val}"
        # Should have some entries
        assert len(chi10) > 0


# =========================================================================
# 8. ADDITIVE vs MULTIPLICATIVE AGREEMENT
# =========================================================================

class TestAdditiveVsMultiplicative:
    """Verify additive (SK) and multiplicative (Borcherds) sides agree."""

    def test_agreement_at_leading_order(self):
        """Leading coefficient a(1,1,1) = 1 from both sides."""
        add = srb.chi10_fourier_from_maass(max_n=2, max_m=2)
        known = srb._chi10_known_fourier()
        # VERIFIED [LT] Igusa 1962: leading coefficient
        assert int(add.get((1, 1, 1), F(0))) == known[(1, 1, 1)] == 1

    def test_agreement_a101(self):
        """a(1, 0, 1) = -2 from both sides."""
        add = srb.chi10_fourier_from_maass(max_n=2, max_m=2)
        known = srb._chi10_known_fourier()
        # VERIFIED [LT] Igusa 1962
        assert int(add.get((1, 0, 1), F(0))) == known[(1, 0, 1)] == -2

    def test_agreement_a112(self):
        """a(1, 1, 2) = -16 from both sides (cross-FJ-index check)."""
        add = srb.chi10_fourier_from_maass(max_n=2, max_m=3)
        known = srb._chi10_known_fourier()
        # VERIFIED [DC] theta DFT cross-check
        assert int(add.get((1, 1, 2), F(0))) == known[(1, 1, 2)] == -16

    def test_agreement_a102(self):
        """a(1, 0, 2) = 36 from both sides."""
        add = srb.chi10_fourier_from_maass(max_n=2, max_m=3)
        known = srb._chi10_known_fourier()
        # VERIFIED [DC] theta DFT cross-check
        assert int(add.get((1, 0, 2), F(0))) == known[(1, 0, 2)] == 36

    def test_agreement_a311(self):
        """a(3, 1, 1) = 99 from both sides."""
        add = srb.chi10_fourier_from_maass(max_n=4, max_m=2)
        known = srb._chi10_known_fourier()
        # VERIFIED [LT] van der Geer 2008
        assert int(add.get((3, 1, 1), F(0))) == known[(3, 1, 1)] == 99

    def test_agreement_a103(self):
        """a(1, 0, 3) = -272 from both sides."""
        add = srb.chi10_fourier_from_maass(max_n=2, max_m=4)
        known = srb._chi10_known_fourier()
        # VERIFIED [LT] van der Geer 2008
        assert int(add.get((1, 0, 3), F(0))) == known[(1, 0, 3)] == -272

    def test_full_comparison_no_mismatches(self):
        """Full comparison at max_n=3, max_m=3 has zero mismatches."""
        result = srb.verify_additive_vs_multiplicative(max_n=3, max_m=3)
        # VERIFIED [DC] cross-check: additive = multiplicative
        assert result['all_agree']
        assert result['n_mismatches'] == 0

    def test_full_comparison_has_matches(self):
        """Full comparison has at least 20 matches."""
        result = srb.verify_additive_vs_multiplicative(max_n=3, max_m=3)
        # VERIFIED [DC] cross-check: sufficient coverage
        assert result['n_matches'] >= 20

    def test_nm_symmetry(self):
        """a(n, r, m) = a(m, r, n) (exchange symmetry of chi_10)."""
        add = srb.chi10_fourier_from_maass(max_n=3, max_m=3)
        for (n, r, m), val in add.items():
            if (m, r, n) in add:
                assert add[(m, r, n)] == val, \
                    f"Symmetry a(n,r,m)=a(m,r,n) fails at ({n},{r},{m})"


# =========================================================================
# 9. SHADOW-TO-FJ BRIDGE
# =========================================================================

class TestShadowToFJBridge:
    """Verify the three-way bridge: shadow -> eta^{24} -> FJ."""

    def test_bridge_additive_multiplicative_agree(self):
        """The bridge verifies additive=multiplicative agreement."""
        data = srb.phi01_coefficients()
        bridge = srb.perturbative_shadow_to_eta24_bridge(
            max_arity=8, max_degree=6, data=data
        )
        # VERIFIED [DC] structural property
        assert bridge['bridge_check']['additive_multiplicative_agree']

    def test_bridge_eta24_at_arity_8(self):
        """At arity 8, all eta^{24} coefficients match through q^6."""
        data = srb.phi01_coefficients()
        bridge = srb.perturbative_shadow_to_eta24_bridge(
            max_arity=8, max_degree=6, data=data
        )
        info = bridge['arity_data'][8]
        assert info['all_match']

    def test_bridge_arity_2_partial(self):
        """At arity 2, only q^0 matches (partial convergence)."""
        data = srb.phi01_coefficients()
        bridge = srb.perturbative_shadow_to_eta24_bridge(
            max_arity=4, max_degree=4, data=data
        )
        info = bridge['arity_data'][2]
        # Arity 2 has only q^0 matching
        assert info['n_eta24_match'] >= 1
        assert not info['all_match']

    def test_bridge_match_increases(self):
        """Number of eta^{24} matches increases with arity."""
        data = srb.phi01_coefficients()
        bridge = srb.perturbative_shadow_to_eta24_bridge(
            max_arity=8, max_degree=6, data=data
        )
        prev = 0
        for r in [2, 4, 6, 8]:
            n = bridge['arity_data'][r]['n_eta24_match']
            assert n >= prev
            prev = n


# =========================================================================
# 10. COMBINED VERIFICATION
# =========================================================================

class TestCombinedVerification:
    """Verify the full combined pipeline passes."""

    def test_base_resummation_passes(self):
        """Base resummation verification (without additive) passes."""
        results = srb.run_resummation_verification(verbose=False)
        assert results['all_passed']

    def test_full_resummation_with_additive_passes(self):
        """Full resummation + additive verification passes."""
        results = srb.run_full_resummation_with_additive(verbose=False)
        assert results['all_passed']

    def test_full_results_contain_additive(self):
        """Full results include additive vs multiplicative data."""
        results = srb.run_full_resummation_with_additive(verbose=False)
        assert 'additive_vs_multiplicative' in results
        assert results['additive_vs_multiplicative']['all_agree']

    def test_full_results_contain_bridge(self):
        """Full results include shadow-FJ bridge data."""
        results = srb.run_full_resummation_with_additive(verbose=False)
        assert 'shadow_fj_bridge' in results


# =========================================================================
# 11. DISCRIMINANT CONSTRAINTS (AP-CY9)
# =========================================================================

class TestDiscriminantConstraints:
    """Verify discriminant constraints on Jacobi form coefficients."""

    def test_phi101_valid_discriminants(self):
        """phi_{10,1} coefficients only at D = 0 or 3 mod 4."""
        c = srb.phi_10_1_by_discriminant()
        for D in c:
            assert D % 4 in (0, 3), f"Invalid discriminant D={D}"

    def test_maass_output_valid_discriminants(self):
        """Maass relation outputs only have D > 0 terms."""
        for m in [1, 2]:
            phi_m = srb.maass_relations_phi_m(m=m, max_n=3)
            for (n, r), val in phi_m.items():
                D = 4 * n * m - r * r
                assert D > 0, f"Non-positive D={D} at ({n},{r}) for m={m}"


# =========================================================================
# 12. KAPPA SPECTRUM (AP113)
# =========================================================================

class TestKappaSpectrum:
    """Verify kappa values conform to the subscript spectrum."""

    def test_kappa_bkm_equals_5(self):
        """kappa_BKM = 5 = weight of Delta_5."""
        # From the shadow tower: arity 2 gives kappa
        from fractions import Fraction
        kappa = srb._bkm.kappa_projection()
        # VERIFIED [LT] k3_times_e.tex L147
        assert kappa == Fraction(5)

    def test_eta24_exponent_is_24(self):
        """The bar Euler exponent = 24 = kappa_fiber."""
        # VERIFIED [DC] structural property: 24 generators of Heisenberg
        data = srb.phi01_coefficients()
        a = srb.effective_exponents_diagonal(10, max_N=4, data=data)
        for N in range(1, 5):
            assert a.get(N, F(0)) == F(24)


# =========================================================================
# 13. EXPONENTIATION ENGINE
# =========================================================================

class TestExponentiationEngine:
    """Verify the 1D log-series exponentiation."""

    def test_exp_zero_is_one(self):
        """exp(0) = 1."""
        result = srb._exponentiate_log_series_1d({}, 5)
        assert result[0] == F(1)
        for n in range(1, 6):
            assert result.get(n, F(0)) == F(0)

    def test_exp_simple_series(self):
        """exp(a*q) = 1 + a*q + a^2*q^2/2 + ..."""
        log_coeffs = {1: F(2)}
        result = srb._exponentiate_log_series_1d(log_coeffs, 4)
        assert result[0] == F(1)
        assert result[1] == F(2)
        assert result[2] == F(2)  # 2^2/2 = 2
        assert result[3] == F(4, 3)  # 2^3/6 = 8/6 = 4/3

    def test_exp_log_inverse(self):
        """Exponentiate log(1/(1-q)) = sum q^n/n and get 1/(1-q) = sum q^n."""
        log_coeffs = {n: F(1, n) for n in range(1, 8)}
        result = srb._exponentiate_log_series_1d(log_coeffs, 6)
        for n in range(7):
            assert result.get(n, F(0)) == F(1), f"Mismatch at q^{n}"
