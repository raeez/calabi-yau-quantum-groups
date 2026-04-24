r"""Tests for k3e_e1_chiral_yangian.py: K3 x E E_1-chiral Yangian.

STATUS: ALL results are CONJECTURAL (AP-CY6/AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction, conditional on
CY-A_3.  The chiral algebra A_{K3 x E} does NOT exist.

CENTRAL RESULTS (all conjectural):
    (1) Structure function g(u) has degree (3,3) with CY condition.
    (2) Unitarity: g(u) * g(-u) = 1.
    (3) CY_3 parity: g(0) = -1.
    (4) Self-dual degeneration: hbar -> 0 gives g(u) = 1.
    (5) Sigma-form matches product form.
    (6) Rank-1 character: 1/eta(q)^{24} (Goettsche, 24-colored partitions).
    (7) Coproduct: z-polynomial degree s-1 at spin s, terminates at s=3 (rank 3).
    (8) R-matrix: scalar at charge 1, diagonal at charge 2.
    (9) Generator count: 73 generating currents (3*24 + 1).
    (10) CY_2 vs CY_3 comparison: E_2 -> E_1 transition at hbar != 0.

Test structure:
    Section 1: Omega parameters and CY condition (6 tests)
    Section 2: Structure function (8 tests)
    Section 3: Unitarity (4 tests)
    Section 4: Self-dual limit (5 tests)
    Section 5: Generators and character (6 tests)
    Section 6: Relations (4 tests)
    Section 7: Coproduct (8 tests)
    Section 8: R-matrix (6 tests)
    Section 9: CY_2 vs CY_3 comparison (3 tests)
    Section 10: Cross-validation with existing engines (5 tests)

Manuscript references:
    k3_times_e.tex: Conjecture conj:k3e-e1-chiral-yangian
    e1_chiral_algebras.tex: Section sec:k3e-e1-chiral-yangian
    cy_to_chiral.tex: Conjecture cy-a-3
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, cancel

from compute.lib.k3e_e1_chiral_yangian import (
    # Status
    STATUS,
    # Parameters
    OmegaParams,
    omega_params,
    omega_params_safe,
    # Structure function
    structure_function,
    structure_function_evaluate,
    structure_function_in_sigma,
    # Verification
    verify_unitarity,
    verify_cy3_parity,
    verify_sigma_form,
    selfdual_degeneration,
    # Generators
    generators,
    rank1_character_coefficients,
    K3EYangianGenerators,
    # Relations
    relations,
    K3EYangianRelations,
    # Coproduct
    coproduct_spin1,
    coproduct_spin2,
    coproduct_spin3,
    coproduct_general_spin,
    coproduct_term_count,
    # R-matrix
    rmatrix_charge1,
    rmatrix_charge2,
    rmatrix_charge_n_diagonal,
    # Comparison
    cy2_vs_cy3_comparison,
    omega_symmetric_functions,
    # Full
    full_verification,
)


F = Fraction


# ===================================================================
# Section 1: Omega parameters and CY condition (6 tests)
# ===================================================================

class TestOmegaParams:
    """Tests for Omega-background parameter construction."""

    def test_cy_condition_default(self):
        """sigma_1 = eps1 + eps2 + eps3 = 0 for default params."""
        p = omega_params()
        assert p.sigma1 == 0, f"CY condition violated: sigma_1 = {p.sigma1}"

    def test_cy_condition_safe(self):
        """sigma_1 = 0 for safe (large) params."""
        p = omega_params_safe()
        assert p.sigma1 == 0

    def test_cy_condition_arbitrary(self):
        """sigma_1 = 0 for arbitrary (eps1, eps2)."""
        for e1, e2 in [(3, 7), (-5, 2), (1, 1), (0, 0)]:
            p = omega_params(Rational(e1), Rational(e2))
            assert p.sigma1 == 0, f"Failed for ({e1}, {e2})"

    def test_eps3_computed(self):
        """eps3 = -(eps1 + eps2) is correctly computed."""
        p = omega_params(Rational(3), Rational(7))
        assert p.eps3 == Rational(-10)

    def test_hbar_is_sigma3(self):
        """hbar = sigma_3 = eps1 * eps2 * eps3."""
        p = omega_params(Rational(1), Rational(-2))
        # eps3 = 1, so sigma_3 = 1 * (-2) * 1 = -2
        assert p.hbar == Rational(1) * Rational(-2) * Rational(1)
        assert p.hbar == p.sigma3

    def test_selfdual_detection(self):
        """is_selfdual is True iff eps1 = -eps2."""
        p_sd = omega_params(Rational(3), Rational(-3))
        assert p_sd.is_selfdual
        p_nsd = omega_params(Rational(3), Rational(-2))
        assert not p_nsd.is_selfdual


# ===================================================================
# Section 2: Structure function (8 tests)
# ===================================================================

class TestStructureFunction:
    """Tests for the K3 x E structure function g(u)."""

    def test_degree(self):
        """g(u) has degree (3, 3) as a rational function."""
        u = Symbol("u")
        g = structure_function()
        # Check that it's a ratio of degree-3 polynomials
        from sympy import degree, Poly, numer, denom
        n = Poly(cancel(numer(g)), u)
        d = Poly(cancel(denom(g)), u)
        assert n.degree() == 3
        assert d.degree() == 3

    def test_value_at_zero(self):
        """g(0) = -1 for CY_3 (odd parity)."""
        g0 = structure_function_evaluate(Rational(0))
        assert g0 == Rational(-1)

    def test_value_at_zero_safe(self):
        """g(0) = -1 with safe parameters."""
        p = omega_params_safe()
        g0 = structure_function_evaluate(Rational(0), p)
        assert g0 == Rational(-1)

    def test_poles_at_neg_eps(self):
        """g(u) has poles at u = -eps1, -eps2, -eps3."""
        p = omega_params(Rational(1), Rational(-2))
        # Poles at u = -1, u = 2, u = -1 (eps3 = 1, so -eps3 = -1)
        # Note: eps1 = 1, eps2 = -2, eps3 = 1
        # Poles at -eps1 = -1, -eps2 = 2, -eps3 = -1
        with pytest.raises(ValueError):
            structure_function_evaluate(Rational(-1), p)
        with pytest.raises(ValueError):
            structure_function_evaluate(Rational(2), p)

    def test_zeros_at_eps(self):
        """g(u) has zeros at u = eps1, eps2, eps3."""
        p = omega_params(Rational(3), Rational(7))
        # eps3 = -10. Zeros at 3, 7, -10.
        assert structure_function_evaluate(Rational(3), p) == 0
        assert structure_function_evaluate(Rational(7), p) == 0
        assert structure_function_evaluate(Rational(-10), p) == 0

    def test_asymptotic_at_large_u(self):
        """g(u) -> 1 as u -> infinity (leading coefficients cancel)."""
        p = omega_params()
        # Check at large u (ratio should approach 1)
        large_u = Rational(10000)
        g_large = structure_function_evaluate(large_u, p)
        # g(10000) = (10000-1)(10000+2)(10000-1) / ((10000+1)(10000-2)(10000+1))
        # ~ 1 - O(1/u)
        # Check it's close to 1
        diff = abs(float(g_large) - 1.0)
        assert diff < 1e-3, f"g(10000) = {g_large}, diff from 1 = {diff}"

    def test_sigma_form_matches_product(self):
        """g(u) in sigma form equals g(u) in product form."""
        result = verify_sigma_form()
        assert result["match"], f"Mismatch: diff = {result['difference']}"

    def test_sigma_form_safe_params(self):
        """sigma form matches product form with safe params."""
        p = omega_params_safe()
        result = verify_sigma_form(p)
        assert result["match"]


# ===================================================================
# Section 3: Unitarity (4 tests)
# ===================================================================

class TestUnitarity:
    """Tests for g(u) * g(-u) = 1."""

    def test_unitarity_symbolic(self):
        """g(u) * g(-u) = 1 symbolically."""
        result = verify_unitarity()
        assert result["symbolic_ok"], f"Symbolic product = {result['symbolic_product']}"

    def test_unitarity_numerical(self):
        """g(u) * g(-u) = 1 at numerical test points."""
        result = verify_unitarity()
        assert result["all_numerical_pass"]

    def test_unitarity_safe_params(self):
        """Unitarity with safe (large) parameters."""
        p = omega_params_safe()
        result = verify_unitarity(p)
        assert result["symbolic_ok"]
        assert result["all_numerical_pass"]

    def test_unitarity_multiple_params(self):
        """Unitarity for several (eps1, eps2) choices."""
        test_cases = [
            (1, -2), (3, 7), (-5, 2), (11, -3), (1, 1),
        ]
        for e1, e2 in test_cases:
            p = omega_params(Rational(e1), Rational(e2))
            result = verify_unitarity(p)
            assert result["symbolic_ok"], f"Unitarity failed for ({e1}, {e2})"


# ===================================================================
# Section 4: Self-dual limit (5 tests)
# ===================================================================

class TestSelfdualLimit:
    """Tests for the CY_2 degeneration at hbar = 0."""

    def test_selfdual_hbar_zero(self):
        """hbar = 0 in the self-dual limit."""
        result = selfdual_degeneration()
        assert result["hbar_is_zero"]

    def test_selfdual_g_trivial(self):
        """g(u) = 1 in the self-dual limit."""
        result = selfdual_degeneration()
        assert result["g_is_trivial"], f"g(u) = {result['g_u']}"

    def test_selfdual_eps3_zero(self):
        """eps3 = 0 in the self-dual limit."""
        result = selfdual_degeneration()
        assert result["params"]["eps3"] == 0

    def test_selfdual_is_detected(self):
        """The is_selfdual flag is set correctly."""
        result = selfdual_degeneration()
        assert result["is_selfdual"]

    def test_cy3_parity(self):
        """CY_3 parity check: g(0) = -1 for generic params."""
        result = verify_cy3_parity()
        assert result["match"], f"g(0) = {result['g_at_0']}, expected {result['expected']}"


# ===================================================================
# Section 5: Generators and character (6 tests)
# ===================================================================

class TestGenerators:
    """Tests for generator structure and character."""

    def test_mukai_directions(self):
        """24 Mukai lattice directions."""
        g = generators()
        assert g.num_mukai_directions == 24

    def test_structure_function_degree(self):
        """Structure function has degree (3, 3)."""
        g = generators()
        assert g.structure_function_degree == (3, 3)

    def test_status_conjectural(self):
        """All generators are conjectural."""
        g = generators()
        assert g.status == "CONJECTURAL"

    def test_rank1_character_first_terms(self):
        """Rank-1 character: first coefficients of prod 1/(1-q^n)^{24}.

        # VERIFIED: [DC] direct computation, [LT] OEIS A000935.
        p_{24}(0) = 1, p_{24}(1) = 24, p_{24}(2) = 324, p_{24}(3) = 3200.
        """
        coeffs = rank1_character_coefficients(max_n=5)
        # VERIFIED: OEIS A000935, cross-check with k3_double_current_algebra
        assert coeffs[0] == 1, f"p_24(0) = {coeffs[0]}"
        assert coeffs[1] == 24, f"p_24(1) = {coeffs[1]}"
        assert coeffs[2] == 324, f"p_24(2) = {coeffs[2]}"
        assert coeffs[3] == 3200, f"p_24(3) = {coeffs[3]}"

    def test_rank1_character_partitions(self):
        """Rank-1 character counts 24-colored partitions.

        # VERIFIED: [DC] p_{24}(4) = 25650, [LT] OEIS A000935.
        """
        coeffs = rank1_character_coefficients(max_n=4)
        assert coeffs[4] == 25650, f"p_24(4) = {coeffs[4]}"

    def test_rank1_character_monotone(self):
        """Rank-1 character coefficients are strictly increasing."""
        coeffs = rank1_character_coefficients(max_n=6)
        for n in range(1, 7):
            assert coeffs[n] > coeffs[n - 1], (
                f"p_24({n}) = {coeffs[n]} <= p_24({n-1}) = {coeffs[n-1]}"
            )


# ===================================================================
# Section 6: Relations (4 tests)
# ===================================================================

class TestRelations:
    """Tests for the K3 x E Yangian relations."""

    def test_relations_returned(self):
        """relations() returns a valid K3EYangianRelations."""
        r = relations()
        assert isinstance(r, K3EYangianRelations)

    def test_status_conjectural(self):
        """Relations are conjectural."""
        r = relations()
        assert r.status == "CONJECTURAL"

    def test_cy_condition_in_relations(self):
        """CY condition is stated in the relations."""
        r = relations()
        assert "0" in r.cy_condition

    def test_mukai_pairing_role(self):
        """Mukai pairing role is described."""
        r = relations()
        assert "(4,20)" in r.mukai_pairing_role


# ===================================================================
# Section 7: Coproduct (8 tests)
# ===================================================================

class TestCoproduct:
    """Tests for the Drinfeld coproduct Delta_z."""

    def test_spin1_primitive(self):
        """Spin-1 coproduct is primitive (no z-dependence)."""
        c = coproduct_spin1()
        assert c["type"] == "primitive"
        assert c["z_degree"] == 0

    def test_spin2_z_degree(self):
        """Spin-2 coproduct has z-polynomial degree 1."""
        c = coproduct_spin2()
        assert c["z_degree"] == 1

    def test_spin3_z_degree(self):
        """Spin-3 coproduct has z-polynomial degree 2."""
        c = coproduct_spin3()
        assert c["z_degree"] == 2

    def test_spin_s_z_degree(self):
        """Spin-s coproduct has z-polynomial degree s-1 for s = 1,...,5."""
        for s in range(1, 6):
            c = coproduct_general_spin(s)
            assert c["z_degree"] == s - 1, f"Spin {s}: z_degree = {c['z_degree']}"

    def test_rank3_truncation(self):
        """Coproduct truncates at s > 3 in rank-3 framework."""
        c4 = coproduct_general_spin(4)
        assert c4["rank3_truncated"]
        c3 = coproduct_general_spin(3)
        assert not c3["rank3_truncated"]

    def test_term_count_spin2(self):
        """Spin-2 has s(s+1)/2 = 3 total terms."""
        tc = coproduct_term_count(2)
        assert tc["total_terms"] == 3

    def test_term_count_spin3(self):
        """Spin-3 has s(s+1)/2 = 6 total terms."""
        tc = coproduct_term_count(3)
        assert tc["total_terms"] == 6

    def test_term_count_formula(self):
        """Total terms = s(s+1)/2 for s = 1,...,10."""
        for s in range(1, 11):
            tc = coproduct_term_count(s)
            expected = s * (s + 1) // 2
            assert tc["total_terms"] == expected, (
                f"Spin {s}: total = {tc['total_terms']}, expected {expected}"
            )


# ===================================================================
# Section 8: R-matrix (6 tests)
# ===================================================================

class TestRMatrix:
    """Tests for the Maulik-Okounkov R-matrix."""

    def test_charge1_scalar(self):
        """R-matrix at charge 1 is scalar (1x1)."""
        r = rmatrix_charge1()
        assert r["dimension"] == "1x1 (scalar)"

    def test_charge1_ybe(self):
        """YBE is trivially satisfied at charge 1."""
        r = rmatrix_charge1()
        assert r["satisfies_ybe"]

    def test_charge2_diagonal(self):
        """R-matrix at charge 2 is diagonal (2x2)."""
        r = rmatrix_charge2()
        assert r["dimension"] == "2x2 (diagonal)"

    def test_charge2_ybe(self):
        """YBE is satisfied at charge 2 (diagonal case)."""
        r = rmatrix_charge2()
        assert r["satisfies_ybe"]

    def test_charge_n_empty_partition(self):
        """R-matrix for empty partition is 1."""
        r = rmatrix_charge_n_diagonal([])
        assert r["charge"] == 0
        assert "1" in r["R_element"]

    def test_charge_n_single_box(self):
        """R-matrix for single-box partition [1] equals g(u)."""
        p = omega_params_safe()
        r = rmatrix_charge_n_diagonal([1], p)
        assert r["charge"] == 1
        assert r["degree"] == (3, 3)


# ===================================================================
# Section 9: CY_2 vs CY_3 comparison (3 tests)
# ===================================================================

class TestCY2vsCY3:
    """Tests for the CY_2 -> CY_3 transition."""

    def test_en_levels(self):
        """CY_2 is E_2, CY_3 is E_1."""
        comp = cy2_vs_cy3_comparison()
        assert "E_2" in comp["k3_cy2"]["en_level"]
        assert "E_1" in comp["k3e_cy3"]["en_level"]

    def test_kappa_values(self):
        """K3 has kappa_ch=2; compact K3 x E has kappa_ch=0 and Heis=3."""
        comp = cy2_vs_cy3_comparison()
        assert comp["k3_cy2"]["kappa_ch"] == 2
        assert comp["k3e_cy3"]["kappa_ch"] == 0
        assert comp["k3e_cy3"]["kappa_ch_Heis"] == 3

    def test_status_asymmetry(self):
        """CY_2 is proved, CY_3 is conjectural."""
        comp = cy2_vs_cy3_comparison()
        assert "PROVED" in comp["k3_cy2"]["status"]
        assert "CONJECTURAL" in comp["k3e_cy3"]["status"]


# ===================================================================
# Section 10: Cross-validation with existing engines (5 tests)
# ===================================================================

class TestCrossValidation:
    """Cross-validation with k3_yangian.py and mo_rmatrix_k3e.py."""

    def test_structure_function_matches_mo(self):
        """K3 x E structure function matches mo_rmatrix_k3e.py.

        Both should give g(u) = (u-e1)(u-e2)(u-e3) / ((u+e1)(u+e2)(u+e3))
        for the same (eps1, eps2, eps3).

        # VERIFIED: [CF] cross-family with mo_rmatrix_k3e.py
        """
        from compute.lib.mo_rmatrix_k3e import k3e_structure_function
        u = Symbol("u")
        e1, e2 = Rational(1), Rational(-2)
        e3 = -(e1 + e2)

        # Our structure function
        p = omega_params(e1, e2)
        our_g = structure_function(p)

        # MO engine structure function
        mo_g = k3e_structure_function(e1, e2, e3)

        diff = cancel(our_g - mo_g)
        assert diff == 0, f"Structure function mismatch: diff = {diff}"

    def test_selfdual_matches_mo(self):
        """Self-dual limit matches mo_rmatrix_k3e.py selfdual check.

        # VERIFIED: [CF] cross-family with mo_rmatrix_k3e.py
        """
        from compute.lib.mo_rmatrix_k3e import k3e_structure_function_selfdual
        eps = Rational(1)
        mo_result = k3e_structure_function_selfdual(eps)
        assert mo_result["is_trivial"]

        our_result = selfdual_degeneration()
        assert our_result["g_is_trivial"]

    def test_rank1_character_matches_k3_bar_euler(self):
        """Rank-1 character reciprocal matches K3 bar Euler.

        1/eta(q)^{24} has coefficients p_{24}(n), while
        eta(q)^{24} has coefficients tau(n+1) (Ramanujan).
        Product: p_{24} * tau = delta (convolution identity).

        # VERIFIED: [CF] cross-engine with k3_double_current_algebra.py
        """
        from compute.lib.k3_double_current_algebra import bar_euler_generating_function

        bar_coeffs = bar_euler_generating_function(5)
        char_coeffs = rank1_character_coefficients(5)

        # Convolution identity: sum_{k=0}^{n} p_{24}(k) * bar(n-k) = delta_{n,0}
        for n in range(6):
            conv = sum(
                char_coeffs.get(k, 0) * bar_coeffs.get(n - k, 0)
                for k in range(n + 1)
            )
            expected = 1 if n == 0 else 0
            assert conv == expected, (
                f"Convolution at n={n}: got {conv}, expected {expected}"
            )

    def test_omega_symmetric_functions(self):
        """sigma_1 = 0, sigma_2 and sigma_3 computed correctly."""
        p = omega_params(Rational(1), Rational(-2))
        sf = omega_symmetric_functions(p)
        assert sf["sigma_1"] == 0
        # eps1=1, eps2=-2, eps3=1
        # sigma_2 = 1*(-2) + 1*1 + (-2)*1 = -2 + 1 - 2 = -3
        assert sf["sigma_2"] == Rational(-3)
        # sigma_3 = 1*(-2)*1 = -2
        assert sf["sigma_3"] == Rational(-2)

    def test_full_verification_passes(self):
        """The full verification suite completes without errors."""
        result = full_verification()
        assert result["status"] == "CONJECTURAL"
        assert result["path1_cy_condition"]["is_zero"]
        assert result["path2_unitarity"]["symbolic_ok"]
        assert result["path3_cy3_parity"]["match"]
        assert result["path4_selfdual"]["hbar_is_zero"]
        assert result["path5_sigma_form"]["match"]
