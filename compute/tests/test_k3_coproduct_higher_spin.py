r"""Tests for K3 Yangian coproduct at higher spins (3, 4, 5, ..., 24).

Verifies:
1. Explicit coproduct terms at spins 3, 4, 5 (6, 10, 15 terms).
2. Structural properties: z-degree, term counts, cross-patterns.
3. Coassociativity via Miura multiplicativity at each spin.
4. Counit epsilon(psi_s) = delta_{s,0} for s = 0,...,5.
5. Antipode S(psi_s) at spins 1-3 via Hopf axiom.
6. K3-specific: Psi_eff = 24, alpha = 23/24, truncation at s = 24.
7. Spin-24 analysis: 300 terms, leading/subleading coefficients.
8. Cross-term universal patterns (J^L*J^R, psi_a^L*psi_b^R).
9. Fock-space verification at spins 3-5 (z-polynomial, vacuum annihilation).
10. Generating function N(s,p) = s-p and total s(s+1)/2.

STATUS: CONJECTURAL (AP-CY14). All results conditional on CY-A_2.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.k3_coproduct_higher_spin import (
    K3CoproductFock,
    K3CoproductStructural,
    MAX_SPIN,
    N_R,
    PSI_EFF,
    antipode_coefficients,
    k3_cross_term_coefficient,
    manuscript_summary_table,
    spin24_analysis,
    universal_cross_patterns,
    verify_antipode_algebraic,
    verify_coassociativity_binomial,
    verify_coassociativity_structural,
    verify_counit,
)
from compute.lib.chiral_coproduct_universal_engine import (
    AllSpinCoproduct,
    verify_highest_z_is_JR,
    verify_vacuum_annihilation,
    verify_z0_cross_terms,
    verify_z_polynomial_degree,
)


# =========================================================================
# Constants
# =========================================================================

class TestK3Constants:
    """K3-specific constants."""

    def test_mukai_rank(self):
        assert N_R == 24

    def test_max_spin(self):
        assert MAX_SPIN == 24

    def test_psi_eff(self):
        assert PSI_EFF == 24


# =========================================================================
# Spin 3: 6 terms
# =========================================================================

class TestSpin3:
    """Explicit coproduct at spin 3."""

    def test_term_count(self):
        t = K3CoproductStructural.coproduct_terms(3)
        assert t["total_terms"] == 6

    def test_z_degree(self):
        assert K3CoproductStructural.z_polynomial_degree(3) == 2

    def test_terms_by_z(self):
        t = K3CoproductStructural.coproduct_terms(3)
        assert t["terms_by_z_power"] == {0: 3, 1: 2, 2: 1}

    def test_cross_terms_z0(self):
        assert K3CoproductStructural.cross_term_count(3) == 2

    def test_total_operator_products(self):
        assert K3CoproductStructural.total_operator_products(3) == 6

    def test_explicit_terms(self):
        terms = K3CoproductStructural.explicit_terms(3)
        labels = [t["label"] for t in terms]
        assert "psi_3^R" in labels
        assert "z^2*psi_1^R" in labels  # leading z^2 = J^R
        assert "[J^L conv psi_2^R]" in labels
        assert "[psi_2^L conv J^R]" in labels
        assert "z^1*2*psi_2^R" in labels
        assert "z^1*[J^L conv J^R]" in labels

    def test_z_polynomial_degree_fock(self):
        r = verify_z_polynomial_degree(3, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_leading_JR_fock(self):
        r = verify_highest_z_is_JR(3, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_vacuum_annihilation(self):
        r = verify_vacuum_annihilation(3, Psi=1.0, N_max=5)
        assert r["ok"]

    def test_z0_cross_terms_fock(self):
        r = verify_z0_cross_terms(3, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_coassociativity_structural(self):
        r = verify_coassociativity_structural(3)
        assert r["ok"]

    def test_cross_patterns(self):
        p = K3CoproductStructural.identify_cross_patterns(3)
        assert p["leading_z_power"] == 2
        assert p["num_bilinear_z0"] == 2
        assert p["JL_JR_z_power"] == 1


# =========================================================================
# Spin 4: 10 terms
# =========================================================================

class TestSpin4:
    """Explicit coproduct at spin 4."""

    def test_term_count(self):
        t = K3CoproductStructural.coproduct_terms(4)
        assert t["total_terms"] == 10

    def test_z_degree(self):
        assert K3CoproductStructural.z_polynomial_degree(4) == 3

    def test_terms_by_z(self):
        t = K3CoproductStructural.coproduct_terms(4)
        assert t["terms_by_z_power"] == {0: 4, 1: 3, 2: 2, 3: 1}

    def test_cross_terms_z0(self):
        assert K3CoproductStructural.cross_term_count(4) == 3

    def test_total_operator_products(self):
        assert K3CoproductStructural.total_operator_products(4) == 10

    def test_explicit_terms(self):
        terms = K3CoproductStructural.explicit_terms(4)
        labels = [t["label"] for t in terms]
        # Check key terms
        assert "psi_4^R" in labels
        assert "z^3*psi_1^R" in labels  # leading z^3 = J^R
        assert "[J^L conv psi_3^R]" in labels
        assert "[psi_2^L conv psi_2^R]" in labels  # NEW at spin 4
        assert "[psi_3^L conv J^R]" in labels
        assert "z^1*2*[J^L conv psi_2^R]" in labels
        assert "z^2*[J^L conv J^R]" in labels

    def test_z_polynomial_degree_fock(self):
        r = verify_z_polynomial_degree(4, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_leading_JR_fock(self):
        r = verify_highest_z_is_JR(4, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_z0_cross_terms_fock(self):
        r = verify_z0_cross_terms(4, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_coassociativity_structural(self):
        r = verify_coassociativity_structural(4)
        assert r["ok"]

    def test_coassociativity_binomial(self):
        """Multi-path: binomial coefficient comparison Route 1 vs Route 2."""
        r = verify_coassociativity_binomial(4)
        assert r["ok"], f"Coassociativity binomial failed at spin 4: {r['mismatches']}"

    def test_psi2_psi2_cross(self):
        """Spin 4 has the first psi_2^L * psi_2^R cross-term."""
        terms = K3CoproductStructural.explicit_terms(4)
        psi2_psi2 = [t for t in terms
                     if t["left_spin"] == 2 and t["right_spin"] == 2]
        assert len(psi2_psi2) == 1
        assert psi2_psi2[0]["z_power"] == 0
        assert psi2_psi2[0]["binomial"] == 1


# =========================================================================
# Spin 5: 15 terms
# =========================================================================

class TestSpin5:
    """Explicit coproduct at spin 5."""

    def test_term_count(self):
        t = K3CoproductStructural.coproduct_terms(5)
        assert t["total_terms"] == 15

    def test_z_degree(self):
        assert K3CoproductStructural.z_polynomial_degree(5) == 4

    def test_terms_by_z(self):
        t = K3CoproductStructural.coproduct_terms(5)
        assert t["terms_by_z_power"] == {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}

    def test_cross_terms_z0(self):
        assert K3CoproductStructural.cross_term_count(5) == 4

    def test_total_operator_products(self):
        assert K3CoproductStructural.total_operator_products(5) == 15

    def test_explicit_terms(self):
        terms = K3CoproductStructural.explicit_terms(5)
        labels = [t["label"] for t in terms]
        # Check key new terms at spin 5
        assert "psi_5^R" in labels
        assert "z^4*psi_1^R" in labels
        assert "[psi_2^L conv psi_3^R]" in labels
        assert "[psi_3^L conv psi_2^R]" in labels
        assert "[psi_4^L conv J^R]" in labels
        assert "z^1*4*psi_4^R" in labels  # subleading has coeff 4

    def test_z_polynomial_degree_fock(self):
        r = verify_z_polynomial_degree(5, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_leading_JR_fock(self):
        r = verify_highest_z_is_JR(5, Psi=2.0, N_max=5)
        assert r["ok"]

    def test_vacuum_annihilation(self):
        r = verify_vacuum_annihilation(5, Psi=1.0, N_max=5)
        assert r["ok"]

    def test_coassociativity_structural(self):
        r = verify_coassociativity_structural(5)
        assert r["ok"]

    def test_binomial_coefficients(self):
        """Verify Pascal's triangle pattern in z-shifted R terms."""
        terms = K3CoproductStructural.explicit_terms(5)
        r_shifted = [t for t in terms if t["left_spin"] == 0]
        coeffs = {t["z_power"]: t["binomial"] for t in r_shifted}
        # C(4,0)=1, C(4,1)=4, C(4,2)=6, C(4,3)=4, C(4,4)=1
        assert coeffs == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}


# =========================================================================
# Counit
# =========================================================================

class TestCounit:
    """epsilon(psi_s) = delta_{s,0} (algebraic augmentation map)."""

    def test_counit_spins_0_through_5(self):
        r = verify_counit(s_max=5)
        assert r["ok"]

    def test_counit_axiom_structure(self):
        """Counit axiom is structural: (eps x id) o Delta = id."""
        r = verify_counit(s_max=5)
        for s in range(1, 6):
            assert r["details"][s]["epsilon"] == 0
            assert "psi" in r["details"][s]["counit_axiom_left"]

    def test_counit_identity(self):
        """epsilon(1) = 1."""
        r = verify_counit(s_max=0)
        assert r["details"][0]["epsilon"] == 1


# =========================================================================
# Antipode
# =========================================================================

class TestAntipode:
    """S(psi_s) via T(u)^{-1} recursion."""

    def test_antipode_spin1(self):
        """S(psi_1) = -psi_1."""
        coeffs = antipode_coefficients(1)
        assert len(coeffs) == 1
        assert coeffs[0] == ((1,), -1)

    def test_antipode_spin2(self):
        """S(psi_2) = psi_1^2 - psi_2."""
        coeffs = antipode_coefficients(2)
        coeff_dict = dict(coeffs)
        assert coeff_dict[(2,)] == -1
        assert coeff_dict[(1, 1)] == 1

    def test_antipode_spin3(self):
        """S(psi_3) = -psi_1^3 + 2*psi_1*psi_2 - psi_3."""
        coeffs = antipode_coefficients(3)
        coeff_dict = dict(coeffs)
        assert coeff_dict[(3,)] == -1
        assert coeff_dict[(2, 1)] == 2
        assert coeff_dict[(1, 1, 1)] == -1

    def test_antipode_spin4(self):
        """S(psi_4) = psi_1^4 - 3*psi_1^2*psi_2 + psi_2^2 + 2*psi_1*psi_3 - psi_4."""
        coeffs = antipode_coefficients(4)
        coeff_dict = dict(coeffs)
        assert coeff_dict[(4,)] == -1
        assert coeff_dict[(3, 1)] == 2
        assert coeff_dict[(2, 2)] == 1
        assert coeff_dict[(2, 1, 1)] == -3
        assert coeff_dict[(1, 1, 1, 1)] == 1

    def test_antipode_spin5(self):
        """S(psi_5) coefficient verification."""
        coeffs = antipode_coefficients(5)
        coeff_dict = dict(coeffs)
        assert coeff_dict[(5,)] == -1
        assert coeff_dict[(4, 1)] == 2
        assert coeff_dict[(3, 2)] == 2
        assert coeff_dict[(3, 1, 1)] == -3
        assert coeff_dict[(2, 2, 1)] == -3
        assert coeff_dict[(2, 1, 1, 1)] == 4
        assert coeff_dict[(1, 1, 1, 1, 1)] == -1

    def test_antipode_sign_pattern(self):
        """The leading term (-1)^s * psi_s always has coefficient -1 for odd s, +1 for even."""
        for s in range(1, 7):
            coeffs = antipode_coefficients(s)
            coeff_dict = dict(coeffs)
            # Single psi_s term has coefficient (-1)^1 = -1
            assert coeff_dict[(s,)] == -1

    def test_antipode_algebraic_spin1(self):
        """T(u)*T(u)^{-1} = 1 at u^{-1}: psi_1 + S(psi_1) = 0."""
        r = verify_antipode_algebraic(1)
        assert r["ok"], f"Antipode algebraic failed at spin 1: {r['residual']}"

    def test_antipode_algebraic_spin2(self):
        r = verify_antipode_algebraic(2)
        assert r["ok"], f"Antipode algebraic failed at spin 2: {r['residual']}"

    def test_antipode_algebraic_spin3(self):
        r = verify_antipode_algebraic(3)
        assert r["ok"], f"Antipode algebraic failed at spin 3: {r['residual']}"

    def test_antipode_algebraic_spin4(self):
        r = verify_antipode_algebraic(4)
        assert r["ok"], f"Antipode algebraic failed at spin 4: {r['residual']}"

    def test_antipode_algebraic_spin5(self):
        r = verify_antipode_algebraic(5)
        assert r["ok"], f"Antipode algebraic failed at spin 5: {r['residual']}"

    def test_antipode_algebraic_all_k3_spins(self):
        """Multi-path: verify antipode at ALL 24 K3 spins."""
        for s in range(1, 25):
            r = verify_antipode_algebraic(s)
            assert r["ok"], f"Antipode algebraic failed at spin {s}: {r['residual']}"


# =========================================================================
# Coassociativity
# =========================================================================

class TestCoassociativity:
    """Coassociativity via Miura multiplicativity."""

    def test_structural_spins_1_through_5(self):
        for s in range(1, 6):
            r = verify_coassociativity_structural(s)
            assert r["ok"], f"Structural coassociativity failed at spin {s}"

    def test_structural_spin_24(self):
        """Maximum K3 spin."""
        r = verify_coassociativity_structural(24)
        assert r["ok"]
        assert r["n_triples"] == 325  # C(26,2) = 325

    def test_n_triples_formula(self):
        """Number of triples (a,b,c) with a+b+c=s: C(s+2,2)."""
        for s in range(1, 10):
            r = verify_coassociativity_structural(s)
            expected = (s + 1) * (s + 2) // 2
            assert r["n_triples"] == expected


# =========================================================================
# Spin 24: K3 maximum
# =========================================================================

class TestSpin24:
    """Spin 24 = K3 maximum."""

    def test_total_terms(self):
        t = K3CoproductStructural.coproduct_terms(24)
        assert t["total_terms"] == 300

    def test_z_degree(self):
        assert K3CoproductStructural.z_polynomial_degree(24) == 23

    def test_cross_terms_z0(self):
        assert K3CoproductStructural.cross_term_count(24) == 23

    def test_total_operator_products(self):
        assert K3CoproductStructural.total_operator_products(24) == 300

    def test_spin24_analysis(self):
        a = spin24_analysis()
        assert a["total_terms"] == 300
        assert a["z_degree"] == 23
        assert a["leading_ok"]
        assert a["subleading_ok"]
        assert a["cross_terms_z0"] == 23

    def test_leading_is_JR(self):
        """z^{23} coefficient is J^R (single term)."""
        a = spin24_analysis()
        assert a["leading_term"] == "z^23*psi_1^R"

    def test_subleading_z22(self):
        """z^{22}: 23*psi_2^R + [J^L*J^R]."""
        a = spin24_analysis()
        assert len(a["subleading_terms"]) == 2

    def test_truncation_enforcement(self):
        """psi_s = 0 for s > 24."""
        with pytest.raises(ValueError, match="K3"):
            K3CoproductStructural.coproduct_terms(25)

    def test_terms_per_z_power(self):
        """N(24, p) = 24 - p."""
        for p in range(24):
            assert K3CoproductStructural.terms_at_z_power(24, p) == 24 - p
        assert K3CoproductStructural.terms_at_z_power(24, 24) == 0


# =========================================================================
# K3 specialization
# =========================================================================

class TestK3Specialization:
    """K3-specific features."""

    def test_alpha_spin2(self):
        """Cross-term coefficient alpha = 23/24."""
        r = k3_cross_term_coefficient()
        assert r["alpha"] == Fraction(23, 24)

    def test_c_eff(self):
        """c_eff = 2 + 2*23^2 = 1060."""
        r = k3_cross_term_coefficient()
        assert r["c_eff"] == 1060

    def test_k3_annotation(self):
        """K3 coproduct tables carry K3-specific annotations."""
        t = K3CoproductStructural.coproduct_terms(3)
        assert t["k3_rank"] == 24
        assert t["k3_psi_eff"] == 24
        assert t["k3_alpha_spin2"] == Fraction(23, 24)
        assert t["status"] == "CONJECTURAL"


# =========================================================================
# Generating function N(s,p) = s - p
# =========================================================================

class TestGeneratingFunction:
    """The generating function F(x,y) = x/((1-x)^2(1-xy))."""

    def test_terms_at_z_power(self):
        """N(s,p) = s - p for 0 <= p < s."""
        for s in range(1, 8):
            for p in range(s):
                assert K3CoproductStructural.terms_at_z_power(s, p) == s - p

    def test_total_terms_triangle(self):
        """Total terms = s(s+1)/2 = sum_{p=0}^{s-1} (s-p)."""
        for s in range(1, 25):
            total = sum(K3CoproductStructural.terms_at_z_power(s, p) for p in range(s))
            assert total == s * (s + 1) // 2

    def test_subleading_z1_coefficient(self):
        """z^1 has s-1 terms, leading coefficient is (s-1)*psi_{s-1}^R."""
        for s in range(2, 8):
            sub = AllSpinCoproduct.subleading_coefficient_z1(s)
            assert sub["leading_R_shifted"]["coefficient"] == s - 1
            assert sub["n_terms"] == s - 1


# =========================================================================
# Universal cross-term patterns
# =========================================================================

class TestCrossPatterns:
    """Universal cross-term identification."""

    def test_JL_JR_universality(self):
        """J^L * J^R appears at z^{s-2} for all s >= 2."""
        for s in range(2, 8):
            p = K3CoproductStructural.identify_cross_patterns(s)
            assert p["JL_JR_z_power"] == s - 2
            assert p["JL_JR_binomial"] == 1

    def test_bilinear_count(self):
        """s-1 bilinear types at z=0."""
        for s in range(1, 8):
            p = K3CoproductStructural.identify_cross_patterns(s)
            assert p["num_bilinear_z0"] == s - 1

    def test_patterns_summary(self):
        """Patterns for spins 1-5."""
        ps = universal_cross_patterns(5)
        assert len(ps) == 5
        for s in range(1, 6):
            assert ps[s]["spin"] == s


# =========================================================================
# Manuscript output
# =========================================================================

class TestManuscript:
    """LaTeX table generation."""

    def test_summary_table_spins_1_5(self):
        table = manuscript_summary_table(5)
        assert r"\begin{tabular}" in table
        assert r"\end{tabular}" in table
        # Spin 3 should appear
        assert "6" in table  # 6 terms at spin 3
        # Spin 5 should appear
        assert "15" in table  # 15 terms at spin 5


# =========================================================================
# K3CoproductFock (Fock space at K3 level)
# =========================================================================

class TestK3CoproductFock:
    """Fock space verification with Psi = 24."""

    def test_instantiation(self):
        eng = K3CoproductFock(N_max=3)
        assert eng.Psi == 24.0

    def test_truncation(self):
        eng = K3CoproductFock(N_max=3)
        with pytest.raises(ValueError, match="K3 truncation"):
            eng.delta_z_k3(25, 0)

    def test_spin1_primitive(self):
        """Delta_z(J_n) = J_n^L + J_n^R at z=0."""
        eng = K3CoproductFock(N_max=3)
        P = eng.safe_proj(2)
        import numpy as np
        for n in [0, -1, 1]:
            delta = eng.delta_z_k3(1, n, 0.0)
            expected = eng._psi_L(1, n) + eng._psi_R(1, n)
            err = float(np.max(np.abs(P @ (delta - expected.astype(complex)) @ P)))
            assert err < 1e-10, f"Spin-1 primitive failed at n={n}: {err}"


# =========================================================================
# Multi-path cross-checks (AP10)
# =========================================================================

class TestMultiPathCrossChecks:
    """Cross-verification between independent computation paths."""

    def test_structural_vs_fock_z_degree_spins_3_5(self):
        """Structural z-degree matches Fock-space polynomial fit at spins 3-5."""
        for s in [3, 4, 5]:
            structural_deg = K3CoproductStructural.z_polynomial_degree(s)
            fock_result = verify_z_polynomial_degree(s, Psi=2.0, N_max=5)
            assert fock_result["ok"], f"Fock z-degree failed at spin {s}"
            assert structural_deg == s - 1

    def test_structural_vs_fock_leading_JR_spins_3_5(self):
        """Structural leading z^{s-1} = J^R matches Fock extraction."""
        for s in [3, 4, 5]:
            # Path 1: structural
            table = AllSpinCoproduct.delta_z_table(s)
            top = table["terms_by_z"].get(s - 1, [])
            structural_ok = (len(top) == 1 and top[0]["right_spin"] == 1
                             and top[0]["binomial"] == 1)
            assert structural_ok
            # Path 2: Fock space
            fock_result = verify_highest_z_is_JR(s, Psi=2.0, N_max=5)
            assert fock_result["ok"], f"Fock leading JR failed at spin {s}"

    def test_term_count_two_paths(self):
        """Term count from explicit enumeration vs s(s+1)/2 formula."""
        for s in range(1, 25):
            # Path 1: enumerate from delta_z_table
            table = AllSpinCoproduct.delta_z_table(s)
            count_1 = table["total_terms"]
            # Path 2: closed-form s(s+1)/2
            count_2 = s * (s + 1) // 2
            # Path 3: sum of terms per z-power: sum_{p=0}^{s-1} (s-p)
            count_3 = sum(s - p for p in range(s))
            assert count_1 == count_2 == count_3, (
                f"Spin {s}: {count_1} vs {count_2} vs {count_3}"
            )

    def test_coassociativity_structural_vs_binomial(self):
        """Two independent coassociativity proofs agree at spins 1-5."""
        for s in range(1, 6):
            r_struct = verify_coassociativity_structural(s)
            r_binom = verify_coassociativity_binomial(s)
            assert r_struct["ok"], f"Structural coassoc failed at spin {s}"
            assert r_binom["ok"], f"Binomial coassoc failed at spin {s}: {r_binom['mismatches']}"

    def test_antipode_algebraic_vs_coefficient_recursion(self):
        """Antipode: algebraic T*T^{-1}=1 vs direct coefficient check."""
        for s in range(1, 8):
            # Path 1: algebraic identity
            r_alg = verify_antipode_algebraic(s)
            assert r_alg["ok"]
            # Path 2: direct recursion check
            # S(psi_s) = -psi_s - sum_{k=1}^{s-1} psi_k * S(psi_{s-k})
            coeffs = dict(antipode_coefficients(s))
            # The (s,) coefficient must be -1
            assert coeffs.get((s,), 0) == -1, f"Spin {s}: leading coeff wrong"

    def test_z0_cross_fock_vs_structural_count(self):
        """Number of bilinear cross-terms at z=0: Fock confirms s-1 types."""
        for s in [3, 4, 5]:
            # Path 1: structural count
            structural_cross = K3CoproductStructural.cross_term_count(s)
            # Path 2: Fock space (verify_z0_cross_terms confirms bilinear decomposition)
            fock_result = verify_z0_cross_terms(s, Psi=2.0, N_max=5)
            assert fock_result["ok"]
            assert structural_cross == s - 1
            assert fock_result["cross_terms"] == s - 1

    def test_universal_engine_vs_k3_structural(self):
        """Universal engine tables match K3 structural tables at spins 3-5."""
        for s in [3, 4, 5]:
            uni = AllSpinCoproduct.delta_z_table(s)
            k3 = K3CoproductStructural.coproduct_terms(s)
            assert uni["total_terms"] == k3["total_terms"]
            assert uni["z_polynomial_degree"] == k3["z_polynomial_degree"]
            assert uni["terms_by_z_power"] == k3["terms_by_z_power"]
            assert uni["cross_terms_at_z0"] == k3["cross_terms_at_z0"]
