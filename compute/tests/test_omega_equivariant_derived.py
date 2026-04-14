"""Tests for the Omega-background equivariant derived algebraic geometry engine.

Five consistency checks for the CY torus T = (C*)^3 / C*_diag on C^3:

  1. Equivariant index on Hilb^n(C^3) reproduces the MacMahon function
  2. K3 x C in the Omega-background gives the K3 Yangian (24 currents)
  3. Self-dual limit eps_1 = -eps_2 breaks E_3 to E_2 (K3 Heisenberg)
  4. NS limit eps_2 -> 0 breaks E_2 to E_1 (trivial structure function)
  5. Super-Yangian Y(gl(4|20)) from the Mukai lattice signature

Plus structural verifications of the K_T(pt) ring and the degeneration cascade.
"""

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.omega_equivariant_derived import (
    CYTorus,
    K3EquivariantCohomology,
    MukaiSuperStructure,
    NekrasovShatashviliLimit,
    SelfDualLimit,
    _macmahon_coefficients,
    equivariant_index_hilb_c3,
    verify_all,
    verify_check1_macmahon,
    verify_check2_k3_yangian,
    verify_check3_self_dual,
    verify_check4_ns_limit,
    verify_check5_super_yangian,
    verify_e3_e2_e1_cascade,
    verify_kt_ring_structure,
)


# =========================================================================
# CYTorus basic tests
# =========================================================================

class TestCYTorus:
    """Tests for the CY torus T = (C*)^3/C*_diag."""

    def test_cy_condition(self):
        """eps_1 + eps_2 + eps_3 = 0."""
        T = CYTorus(Fraction(3), Fraction(5))
        assert T.eps1 + T.eps2 + T.eps3 == 0

    def test_cy_condition_enforced(self):
        """Providing inconsistent eps_3 raises assertion."""
        with pytest.raises(AssertionError):
            CYTorus(Fraction(1), Fraction(2), Fraction(3))

    def test_sigma1_zero(self):
        """sigma_1 = 0 by CY condition."""
        T = CYTorus(Fraction(7), Fraction(11))
        assert T.sigma1 == 0

    def test_sigma2_formula(self):
        """sigma_2 = -(eps_1^2 + eps_1*eps_2 + eps_2^2)."""
        e1, e2 = Fraction(3), Fraction(5)
        T = CYTorus(e1, e2)
        assert T.sigma2 == -(e1**2 + e1 * e2 + e2**2)

    def test_sigma3_formula(self):
        """sigma_3 = -eps_1 * eps_2 * (eps_1 + eps_2)."""
        e1, e2 = Fraction(3), Fraction(5)
        T = CYTorus(e1, e2)
        assert T.sigma3 == -e1 * e2 * (e1 + e2)

    def test_calabi_yau_character_zero(self):
        """T-character of canonical bundle = 0 (CY condition)."""
        T = CYTorus(Fraction(3), Fraction(5))
        assert T.calabi_yau_character() == 0

    def test_weights_sum_to_zero(self):
        """Sum of T-weights on T_0(C^3) = 0."""
        T = CYTorus(Fraction(7), Fraction(-3))
        assert sum(T.weights_on_tangent_space()) == 0

    def test_structure_function_unitarity(self):
        """g(u) * g(-u) = 1 for generic u (CY inversion identity)."""
        T = CYTorus(Fraction(3), Fraction(5))
        u = Fraction(17)  # AP-CY28: safe test point
        g_u = T.structure_function(u)
        g_neg_u = T.structure_function(-u)
        assert g_u * g_neg_u == 1

    def test_structure_function_at_infinity(self):
        """g(u) -> 1 as u -> infinity (leading coefficient ratio)."""
        T = CYTorus(Fraction(1), Fraction(2))
        # At large u, g(u) ~ u^3/u^3 = 1
        u = Fraction(10000)
        g_val = T.structure_function(u)
        assert abs(float(g_val) - 1.0) < 1e-4

    def test_self_dual_detection(self):
        """Self-dual point detected when eps_3 = 0."""
        T_sd = CYTorus(Fraction(3), Fraction(-3))
        assert T_sd.is_self_dual
        T_gen = CYTorus(Fraction(3), Fraction(5))
        assert not T_gen.is_self_dual

    def test_ns_limit_detection(self):
        """NS limit detected when eps_2 = 0."""
        T_ns = CYTorus(Fraction(3), Fraction(0))
        assert T_ns.is_ns_limit
        T_gen = CYTorus(Fraction(3), Fraction(5))
        assert not T_gen.is_ns_limit

    def test_representation_ring_rank(self):
        """K_T(pt) = Z[eps_1, eps_2] has rank 2."""
        T = CYTorus(Fraction(3), Fraction(5))
        gens = T.representation_ring_generators()
        assert len(gens) == 2
        assert "eps_1" in gens
        assert "eps_2" in gens


# =========================================================================
# Check 1: MacMahon function from equivariant index
# =========================================================================

class TestCheck1MacMahon:
    """Equivariant index on Hilb^n(C^3) = MacMahon function."""

    def test_oeis_seed_values(self):
        """First 11 plane partition counts match OEIS A000219."""
        counts = equivariant_index_hilb_c3(11)
        assert counts == [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]

    def test_p3_of_zero(self):
        """p_3(0) = 1 (empty partition)."""
        assert equivariant_index_hilb_c3(1) == [1]

    def test_monotone_growth(self):
        """p_3(n) is strictly increasing for n >= 1."""
        counts = equivariant_index_hilb_c3(20)
        for i in range(2, 20):
            assert counts[i] > counts[i - 1]

    def test_verify_check1(self):
        """Full check 1 verification."""
        result = verify_check1_macmahon(15)
        assert result["seed_values_match_oeis"]
        assert result["cy_weight_cancellation"]

    def test_p3_20(self):
        """p_3(20) = 75278 (deep verification)."""
        counts = equivariant_index_hilb_c3(21)
        assert counts[20] == 75278


# =========================================================================
# Check 2: K3 Yangian from equivariant cohomology
# =========================================================================

class TestCheck2K3Yangian:
    """K3 x C in the Omega-background gives K3 Yangian."""

    def test_24_currents(self):
        """K3 Yangian has 24 currents (= rank of Mukai lattice)."""
        K3 = K3EquivariantCohomology()
        assert K3.num_currents == 24

    def test_mukai_signature(self):
        """Mukai pairing has signature (4, 20)."""
        K3 = K3EquivariantCohomology()
        assert K3.MUKAI_SIGNATURE == (4, 20)

    def test_euler_characteristic(self):
        """chi(K3) = 24."""
        K3 = K3EquivariantCohomology()
        assert K3.EULER_CHAR == 24

    def test_betti_numbers(self):
        """K3 Betti numbers: 1, 0, 22, 0, 1."""
        K3 = K3EquivariantCohomology()
        assert K3.BETTI == [1, 0, 22, 0, 1]
        assert sum(K3.BETTI) == 24

    def test_mukai_pairing_matrix(self):
        """Mukai pairing is diagonal with signature (4, 20)."""
        K3 = K3EquivariantCohomology()
        omega = K3.mukai_pairing_matrix()
        assert omega.shape == (24, 24)
        assert np.trace(omega) == 4 - 20  # = -16
        pos = np.sum(np.diag(omega) > 0)
        neg = np.sum(np.diag(omega) < 0)
        assert pos == 4
        assert neg == 20

    def test_parameters_sum_to_zero(self):
        """K3 Yangian parameters satisfy sum h_i = 0."""
        K3 = K3EquivariantCohomology()
        h = K3.k3_yangian_parameters()
        assert abs(np.sum(h)) < 1e-12

    def test_unitarity_identity(self):
        """g_{K3}(u) * g_{K3}(-u) = 1 at safe test points."""
        K3 = K3EquivariantCohomology()
        h = K3.k3_yangian_parameters()
        for u in [3.7, 5.3, 11.1, -4.2, 17.9]:
            result = K3.verify_unitarity(u, h)
            assert result["is_unity"], f"Unitarity fails at u={u}"

    def test_g_at_zero_is_one(self):
        """g_{K3}(0) = (-1)^24 = 1 (even rank)."""
        K3 = K3EquivariantCohomology()
        h = K3.k3_yangian_parameters()
        g0 = K3.k3_structure_function(0.0, h)
        assert abs(g0 - 1.0) < 1e-8

    def test_equivariant_cohomology_rank(self):
        """H^*_T(K3) has rank 24 over C[eps]."""
        K3 = K3EquivariantCohomology()
        assert K3.equivariant_cohomology_rank() == 24

    def test_verify_check2(self):
        """Full check 2 verification."""
        result = verify_check2_k3_yangian()
        assert result["currents_match_betti"]
        assert result["unitarity_all_pass"]
        assert result["sum_h_i_zero"]


# =========================================================================
# Check 3: Self-dual limit
# =========================================================================

class TestCheck3SelfDual:
    """Self-dual limit eps_1 = -eps_2 breaks E_3 to E_2."""

    def test_eps3_zero(self):
        """eps_3 = 0 at the self-dual point."""
        sd = SelfDualLimit(Fraction(3))
        assert sd.torus.eps3 == 0

    def test_sigma3_zero(self):
        """sigma_3 = 0 at the self-dual point."""
        sd = SelfDualLimit(Fraction(3))
        assert sd.torus.sigma3 == 0

    def test_structure_function_reduces(self):
        """Structure function reduces from deg (3,3) to (2,2)."""
        sd = SelfDualLimit(Fraction(3))
        checks = sd.verify_degeneration()
        assert checks["structure_fn_reduces"]

    def test_heisenberg_from_yangian(self):
        """K3 Yangian becomes K3 Heisenberg at self-dual point."""
        sd = SelfDualLimit(Fraction(3))
        heis = sd.heisenberg_from_yangian()
        assert heis["is_heisenberg"]
        assert heis["algebra"] == "K3 Heisenberg H_Muk"

    def test_km_level_positive(self):
        """KM level k = eps^2 > 0 at self-dual point."""
        sd = SelfDualLimit(Fraction(3))
        checks = sd.verify_degeneration()
        assert checks["km_level_positive"]
        assert checks["km_level"] == Fraction(9)

    def test_verify_check3(self):
        """Full check 3 verification."""
        result = verify_check3_self_dual()
        d = result["degeneration"]
        assert d["eps3_zero"]
        assert d["sigma3_zero"]
        assert d["structure_fn_reduces"]


# =========================================================================
# Check 4: Nekrasov-Shatashvili limit
# =========================================================================

class TestCheck4NSLimit:
    """NS limit eps_2 -> 0 breaks E_2 to E_1."""

    def test_eps2_zero(self):
        """eps_2 = 0 in the NS limit."""
        ns = NekrasovShatashviliLimit(Fraction(3))
        assert ns.torus.eps2 == 0

    def test_sigma3_zero(self):
        """sigma_3 = 0 in the NS limit."""
        ns = NekrasovShatashviliLimit(Fraction(3))
        assert ns.torus.sigma3 == 0

    def test_structure_function_trivial(self):
        """g(u) = 1 for all u in the NS limit."""
        ns = NekrasovShatashviliLimit(Fraction(3))
        # Test at multiple safe points (AP-CY28)
        for u in [Fraction(7), Fraction(11), Fraction(-5), Fraction(23)]:
            assert ns.torus.structure_function(u) == 1

    def test_bethe_level(self):
        """Bethe ansatz level = eps_1^2."""
        ns = NekrasovShatashviliLimit(Fraction(3))
        assert ns.bethe_ansatz_level() == Fraction(9)

    def test_verify_check4(self):
        """Full check 4 verification."""
        result = verify_check4_ns_limit()
        d = result["degeneration"]
        assert d["eps2_zero"]
        assert d["sigma3_zero"]
        assert d["structure_fn_trivial"]


# =========================================================================
# Check 5: Super-Yangian Y(gl(4|20))
# =========================================================================

class TestCheck5SuperYangian:
    """Super-Yangian Y(gl(4|20)) from the Mukai lattice."""

    def test_super_dimension(self):
        """sdim = 4 - 20 = -16."""
        MS = MukaiSuperStructure()
        assert MS.super_dimension == -16

    def test_total_dimension(self):
        """Total dimension = 24 (Mukai rank)."""
        MS = MukaiSuperStructure()
        assert MS.total_dimension == 24

    def test_lie_algebra_dimension(self):
        """dim gl(4|20) = 24^2 = 576."""
        MS = MukaiSuperStructure()
        assert MS.total_super_lie_dimension == 576

    def test_even_plus_odd(self):
        """even + odd = total."""
        MS = MukaiSuperStructure()
        assert (MS.even_part_dimension + MS.odd_part_dimension
                == MS.total_super_lie_dimension)

    def test_even_part(self):
        """dim gl(4|20)_0 = 4^2 + 20^2 = 416."""
        MS = MukaiSuperStructure()
        assert MS.even_part_dimension == 416

    def test_odd_part(self):
        """dim gl(4|20)_1 = 2*4*20 = 160."""
        MS = MukaiSuperStructure()
        assert MS.odd_part_dimension == 160

    def test_super_casimir(self):
        """Super-Casimir(fund) = sdim/2 = -8."""
        MS = MukaiSuperStructure()
        assert MS.super_casimir() == -8

    def test_hirzebruch_mukai_coincidence(self):
        """Hirzebruch sig = Mukai sig = -16 (numerical coincidence)."""
        MS = MukaiSuperStructure()
        checks = MS.verify_dimensions()
        assert checks["hirzebruch_equals_mukai_numerically"]
        assert checks["hirzebruch_sig"] == -16
        assert checks["mukai_sig"] == -16

    def test_verify_check5(self):
        """Full check 5 verification."""
        result = verify_check5_super_yangian()
        assert result["dimensions"]["total_is_rank_squared"]
        assert result["dimensions"]["even_plus_odd"]
        assert result["dimensions"]["sdim_is_signature"]
        assert result["dimensions"]["euler_char"]


# =========================================================================
# Cascade and ring structure
# =========================================================================

class TestCascade:
    """E_3 -> E_2 -> E_1 degeneration cascade."""

    def test_full_cascade(self):
        """The cascade is correct at all three levels."""
        result = verify_e3_e2_e1_cascade()
        assert result["cascade_correct"]

    def test_generic_e3(self):
        """Generic point has sigma_3 != 0 and nontrivial g."""
        result = verify_e3_e2_e1_cascade()
        assert result["generic_E3"]["sigma3_nonzero"]
        assert result["generic_E3"]["g_nontrivial"]

    def test_self_dual_e2(self):
        """Self-dual point has sigma_3 = 0 and reduced g."""
        result = verify_e3_e2_e1_cascade()
        assert result["self_dual_E2"]["sigma3_zero"]
        assert result["self_dual_E2"]["g_reduces_to_2param"]

    def test_ns_e1(self):
        """NS point has trivial structure function g = 1."""
        result = verify_e3_e2_e1_cascade()
        assert result["ns_limit_E1"]["sigma3_zero"]
        assert result["ns_limit_E1"]["g_trivial"]


class TestKTRing:
    """K_T(pt) = Z[eps_1, eps_2] ring structure."""

    def test_ring_structure(self):
        """Full K_T ring verification."""
        result = verify_kt_ring_structure()
        assert result["sigma1_zero"]
        assert result["sigma2_formula_match"]
        assert result["sigma3_formula_match"]
        assert result["level_positive"]
        assert result["rank"] == 2


# =========================================================================
# Full verification suite
# =========================================================================

class TestFullSuite:
    """Run the full verification suite."""

    def test_verify_all(self):
        """All five checks pass."""
        results = verify_all()
        assert results["check1_macmahon"]["seed_values_match_oeis"]
        assert results["check1_macmahon"]["cy_weight_cancellation"]
        assert results["check2_k3_yangian"]["unitarity_all_pass"]
        assert results["check3_self_dual"]["degeneration"]["sigma3_zero"]
        assert results["check4_ns_limit"]["degeneration"]["structure_fn_trivial"]
        assert results["check5_super_yangian"]["dimensions"]["total_is_rank_squared"]
        assert results["cascade_e3_e2_e1"]["cascade_correct"]
        assert results["kt_ring"]["sigma1_zero"]


# =========================================================================
# Multi-path cross-checks (AP10 compliance)
# =========================================================================

class TestCrossChecks:
    """Multi-path verification: same facts derived by independent methods.

    Each test here computes the SAME quantity by TWO or more independent
    paths and asserts agreement.  This catches confabulated ground-truth
    values (AP-CY24) and single-path errors.
    """

    def test_macmahon_two_methods(self):
        """Cross-check MacMahon coefficients via log-exp AND direct product.

        Path A: log M(q), exponentiate (engine method).
        Path B: iterated multiplication by 1/(1-q^n) (c3_dt_partition method).
        """
        from compute.lib.c3_dt_partition import macmahon_coefficients_product
        N = 25
        path_a = _macmahon_coefficients(N)
        path_b = macmahon_coefficients_product(N)
        for k in range(N):
            assert path_a[k] == path_b[k], \
                f"MacMahon disagrees at k={k}: {path_a[k]} vs {path_b[k]}"

    def test_sigma2_two_formulas(self):
        """Cross-check sigma_2 via definition and closed-form.

        Path A: sigma_2 = e1*e2 + e1*e3 + e2*e3 (definition, computed in CYTorus).
        Path B: sigma_2 = -(e1^2 + e1*e2 + e2^2) (using e3 = -(e1+e2)).
        Verified at 5 independent parameter choices.
        """
        params = [(1, 2), (3, 5), (7, 11), (-4, 9), (13, -6)]
        for e1_val, e2_val in params:
            e1, e2 = Fraction(e1_val), Fraction(e2_val)
            T = CYTorus(e1, e2)
            path_a = T.sigma2
            path_b = -(e1**2 + e1 * e2 + e2**2)
            assert path_a == path_b, \
                f"sigma_2 mismatch at ({e1},{e2}): {path_a} vs {path_b}"

    def test_sigma3_two_formulas(self):
        """Cross-check sigma_3 via definition and closed-form.

        Path A: sigma_3 = e1*e2*e3 (definition).
        Path B: sigma_3 = -e1*e2*(e1+e2) (using e3 = -(e1+e2)).
        """
        params = [(1, 2), (3, 5), (7, 11), (-4, 9), (13, -6)]
        for e1_val, e2_val in params:
            e1, e2 = Fraction(e1_val), Fraction(e2_val)
            T = CYTorus(e1, e2)
            path_a = T.sigma3
            path_b = -e1 * e2 * (e1 + e2)
            assert path_a == path_b, \
                f"sigma_3 mismatch at ({e1},{e2}): {path_a} vs {path_b}"

    def test_unitarity_exact_vs_numerical(self):
        """Cross-check g(u)*g(-u)=1 via exact Fraction AND float.

        Path A: exact rational arithmetic (Fraction).
        Path B: floating-point (numpy).
        Agreement to machine epsilon validates both paths.
        """
        # Exact path
        T_exact = CYTorus(Fraction(3), Fraction(5))
        u_exact = Fraction(17)
        product_exact = (T_exact.structure_function(u_exact)
                         * T_exact.structure_function(-u_exact))
        assert product_exact == 1

        # Float path (independent computation)
        e1, e2, e3 = 3.0, 5.0, -8.0
        u = 17.0
        g_u = ((u - e1) * (u - e2) * (u - e3)
               / ((u + e1) * (u + e2) * (u + e3)))
        g_neg = ((-u - e1) * (-u - e2) * (-u - e3)
                 / ((-u + e1) * (-u + e2) * (-u + e3)))
        product_float = g_u * g_neg
        assert abs(product_float - 1.0) < 1e-12

    def test_ns_trivial_two_paths(self):
        """Cross-check that g(u)=1 in NS limit via algebra AND factorization.

        Path A: CYTorus.structure_function(u) with eps2=0.
        Path B: explicit factorization (u-e1)*u*(u+e1) / ((u+e1)*u*(u-e1)) = 1.
        """
        e1 = Fraction(7)
        T = CYTorus(e1, Fraction(0))
        u = Fraction(23)

        # Path A
        path_a = T.structure_function(u)

        # Path B: manual
        num = (u - e1) * u * (u + e1)
        den = (u + e1) * u * (u - e1)
        path_b = num / den

        assert path_a == 1
        assert path_b == 1

    def test_k3_unitarity_vs_explicit_product(self):
        """Cross-check K3 unitarity via engine AND explicit numpy product.

        Path A: K3EquivariantCohomology.verify_unitarity().
        Path B: Independent numpy computation of prod (u-h_i)/(u+h_i) *
                prod(-u-h_i)/(-u+h_i).
        """
        K3 = K3EquivariantCohomology()
        h = K3.k3_yangian_parameters()
        u = 7.3

        # Path A
        result_a = K3.verify_unitarity(u, h)

        # Path B: independent
        g_u = np.prod([(u - hi) / (u + hi) for hi in h])
        g_neg = np.prod([(-u - hi) / (-u + hi) for hi in h])
        product_b = g_u * g_neg

        assert result_a["is_unity"]
        assert abs(product_b - 1.0) < 1e-10

    def test_mukai_signature_two_paths(self):
        """Cross-check Mukai signature via stored constant AND eigenvalue count.

        Path A: K3EquivariantCohomology.MUKAI_SIGNATURE = (4, 20).
        Path B: Count positive/negative eigenvalues of the pairing matrix.
        """
        K3 = K3EquivariantCohomology()
        omega = K3.mukai_pairing_matrix()
        eigenvalues = np.linalg.eigvalsh(omega)
        n_pos = int(np.sum(eigenvalues > 0.5))
        n_neg = int(np.sum(eigenvalues < -0.5))
        assert (n_pos, n_neg) == K3.MUKAI_SIGNATURE

    def test_super_dimension_two_paths(self):
        """Cross-check sdim via stored value AND Betti number computation.

        Path A: MukaiSuperStructure.super_dimension = -16.
        Path B: From Betti numbers: sum(-1)^i b_i = 24 (Euler char),
                and sig(H^2) = b_2^+ - b_2^- = 3 - 19 = -16.
        """
        MS = MukaiSuperStructure()
        # Path A
        sdim_a = MS.super_dimension

        # Path B: from Betti numbers of K3
        # b_0=1, b_2=22, b_4=1; H^2 has intersection form of sig (3,19)
        # Mukai: the hyperbolic plane from H^0+H^4 adds (1,1) to (3,19)
        # giving (4,20). sdim = 4-20 = -16.
        h2_pos, h2_neg = 3, 19  # intersection form on H^2(K3)
        hyp_pos, hyp_neg = 1, 1  # hyperbolic plane from H^0 + H^4
        mukai_pos = h2_pos + hyp_pos  # = 4
        mukai_neg = h2_neg + hyp_neg  # = 20
        sdim_b = mukai_pos - mukai_neg  # = -16

        assert sdim_a == sdim_b == -16
        assert mukai_pos + mukai_neg == 24  # Mukai rank

    def test_self_dual_level_two_paths(self):
        """Cross-check KM level at self-dual via sigma_2 AND direct computation.

        Path A: level = -sigma_2 from CYTorus.
        Path B: level = eps^2 (direct from self-dual condition).
        """
        for eps_val in [1, 3, 7, 13]:
            eps = Fraction(eps_val)
            sd = SelfDualLimit(eps)
            path_a = -sd.torus.sigma2
            path_b = eps ** 2
            assert path_a == path_b, \
                f"Level mismatch at eps={eps}: {path_a} vs {path_b}"

    def test_macmahon_vs_c3_dt_engine(self):
        """Cross-check against the existing c3_dt_partition engine.

        Path A: equivariant_index_hilb_c3() from this engine.
        Path B: plane_partition_counts() from c3_dt_partition.
        Two independent implementations of the same quantity.
        """
        from compute.lib.c3_dt_partition import plane_partition_counts
        N = 20
        path_a = equivariant_index_hilb_c3(N)
        path_b = plane_partition_counts(N)
        assert path_a == path_b

    def test_gl_dimensions_three_paths(self):
        """Cross-check gl(4|20) dimensions via three formulas.

        Path A: even + odd from MukaiSuperStructure.
        Path B: (m+n)^2 = m^2 + 2mn + n^2.
        Path C: Manual: 4^2 + 20^2 + 2*4*20 = 16 + 400 + 160 = 576.
        """
        MS = MukaiSuperStructure()
        m, n = 4, 20

        path_a = MS.even_part_dimension + MS.odd_part_dimension
        path_b = (m + n) ** 2
        path_c = m**2 + n**2 + 2 * m * n

        assert path_a == path_b == path_c == 576
