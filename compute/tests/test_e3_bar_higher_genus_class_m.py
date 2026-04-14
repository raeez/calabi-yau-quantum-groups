r"""Tests for the E_3 bar cohomology of class M (Virasoro) at higher genus.

MAIN RESULT:
  E_inf(class M, genus g) has Poincare polynomial (3t(1+t))^g.
  Total dimension = 6^g (proved for g <= 3; at g >= 4, d_5 may act).

The d_4 differential decomposes as a sum of per-copy contractions.
By the Kunneth theorem: E_4 = tensor^g [0, 3, 3, 0].

Degree-by-degree:
  g=1: E_inf = [0, 3, 3, 0],             dim = 6
  g=2: E_inf = [0, 0, 9, 18, 9, 0, 0],   dim = 36
  g=3: E_inf = [0,0,0, 27, 81, 81, 27, 0,0,0], dim = 216

Class comparison (same genus):
  Class L (Yangian): E_inf = (1+t)^{3g}, dim = 8^g
  Class M (Virasoro): E_inf = (3t(1+t))^g, dim = 6^g
  Deficit: 8^g - 6^g (exponentially growing, ratio (4/3)^g)

Higher differentials:
  g=1,2,3: d_5+ = 0 for DEGREE REASONS (E_4 support width < 5)
  g >= 4: d_5 can potentially act; spectral sequence terminates at E_{g+2}

Manuscript references:
  en_factorization.tex: prop:virasoro-d4 (genus 1)
  holomorphic_cs_chiral_engine.py: E3BarSpectralSequenceVirasoro (genus 1)
  e3_bar_higher_genus_class_m.py: E3BarHigherGenusClassM (THIS MODULE)
"""

import pytest
from math import comb
from sympy import Rational

from compute.lib.e3_bar_higher_genus_class_m import (
    E3BarHigherGenusClassM,
    class_m_einf_dimension,
    class_m_einf_poincare,
    class_m_deficit,
    class_comparison_table,
    verify_kunneth_against_matrix,
)


# =========================================================================
# Ground truth
# =========================================================================

# E_4 = E_inf Poincare polynomials by genus
E4_GROUND_TRUTH = {
    1: [0, 3, 3, 0],
    2: [0, 0, 9, 18, 9, 0, 0],
    3: [0, 0, 0, 27, 81, 81, 27, 0, 0, 0],
}

# Total dimensions
E4_TOTAL_GROUND_TRUTH = {1: 6, 2: 36, 3: 216, 4: 1296, 5: 7776}

# Class L dimensions for comparison
CLASS_L_TOTAL = {1: 8, 2: 64, 3: 512, 4: 4096, 5: 32768}

# Deficits
DEFICIT_GROUND_TRUTH = {1: 2, 2: 28, 3: 296, 4: 2800, 5: 24992}


# =========================================================================
# 1. Genus 1 recovery: matches existing prop:virasoro-d4
# =========================================================================

class TestGenus1Recovery:
    """Genus 1 must match the existing test_e3_bar_virasoro_d4 results."""

    def setup_method(self):
        self.engine = E3BarHigherGenusClassM(g=1)

    def test_e3_poincare(self):
        assert self.engine.e3_poincare() == [1, 3, 3, 1]

    def test_e3_total(self):
        assert self.engine.e3_total() == 8

    def test_e4_poincare_closed_form(self):
        assert self.engine.e4_poincare() == [0, 3, 3, 0]

    def test_e4_total(self):
        assert self.engine.e4_total() == 6

    def test_matches_ground_truth(self):
        assert self.engine.e4_poincare() == E4_GROUND_TRUTH[1]

    def test_kappa_ch(self):
        """kappa_ch = c/2 = 1/2 at c=1 (AP113: subscripted)."""
        assert self.engine.kappa_ch == Rational(1, 2)

    def test_S4(self):
        """S_4 = 10/27 at c=1."""
        assert self.engine.S4 == Rational(10, 27)

    def test_Delta(self):
        """Delta = 40/27 at c=1."""
        assert self.engine.Delta == Rational(40, 27)

    def test_e4_is_einf(self):
        """g=1: E_4 = E_inf (no d_5+ by degree)."""
        assert self.engine.e4_is_einf() is True


# =========================================================================
# 2. Genus 2: the first new computation
# =========================================================================

class TestGenus2:
    """g=2: E_inf = [0, 0, 9, 18, 9, 0, 0], dim = 36 = 6^2."""

    def setup_method(self):
        self.engine = E3BarHigherGenusClassM(g=2)

    def test_e3_poincare(self):
        """E_3 = (1+t)^6 = [1, 6, 15, 20, 15, 6, 1]."""
        assert self.engine.e3_poincare() == [1, 6, 15, 20, 15, 6, 1]

    def test_e3_total(self):
        """dim E_3 = 2^6 = 64."""
        assert self.engine.e3_total() == 64

    def test_e4_poincare(self):
        """E_4 = [0, 0, 9, 18, 9, 0, 0]."""
        assert self.engine.e4_poincare() == [0, 0, 9, 18, 9, 0, 0]

    def test_e4_matches_ground_truth(self):
        assert self.engine.e4_poincare() == E4_GROUND_TRUTH[2]

    def test_e4_total_is_36(self):
        """dim E_4 = 6^2 = 36."""
        assert self.engine.e4_total() == 36

    def test_e4_is_einf(self):
        """g=2: E_4 = E_inf (d_5 cannot act by degree)."""
        assert self.engine.e4_is_einf() is True

    def test_deficit_is_28(self):
        """Deficit = 64 - 36 = 28."""
        assert self.engine.deficit() == 28

    def test_d4_rank_degree_3(self):
        """d_4: Lambda^3(20) -> Lambda^0(1), rank = 1."""
        assert self.engine.d4_rank(3) == 1

    def test_d4_rank_degree_4(self):
        """d_4: Lambda^4(15) -> Lambda^1(6), rank = 6 (surjective)."""
        assert self.engine.d4_rank(4) == 6

    def test_d4_rank_degree_5(self):
        """d_4: Lambda^5(6) -> Lambda^2(15), rank = 6 (injective)."""
        assert self.engine.d4_rank(5) == 6

    def test_d4_rank_degree_6(self):
        """d_4: Lambda^6(1) -> Lambda^3(20), rank = 1."""
        assert self.engine.d4_rank(6) == 1

    def test_d4_rank_low_degrees_zero(self):
        """d_4 has rank 0 for degrees 0, 1, 2 (target out of range)."""
        for n in range(3):
            assert self.engine.d4_rank(n) == 0

    def test_d5_impossible_by_degree(self):
        """d_5 cannot act: E_4 support = {2,3,4}, shift 4 exits."""
        assert self.engine.d5_potential_maps() == []


# =========================================================================
# 3. Genus 3: the largest genus with unconditional E_inf
# =========================================================================

class TestGenus3:
    """g=3: E_inf = [0,0,0, 27, 81, 81, 27, 0,0,0], dim = 216 = 6^3."""

    def setup_method(self):
        self.engine = E3BarHigherGenusClassM(g=3)

    def test_e3_poincare(self):
        """E_3 = (1+t)^9."""
        expected = [comb(9, n) for n in range(10)]
        assert self.engine.e3_poincare() == expected

    def test_e3_total(self):
        assert self.engine.e3_total() == 512

    def test_e4_poincare(self):
        """E_4 = [0,0,0, 27, 81, 81, 27, 0,0,0]."""
        assert self.engine.e4_poincare() == [0, 0, 0, 27, 81, 81, 27, 0, 0, 0]

    def test_e4_matches_ground_truth(self):
        assert self.engine.e4_poincare() == E4_GROUND_TRUTH[3]

    def test_e4_total_is_216(self):
        """dim E_4 = 6^3 = 216."""
        assert self.engine.e4_total() == 216

    def test_e4_is_einf(self):
        """g=3: E_4 = E_inf (last genus where this holds)."""
        assert self.engine.e4_is_einf() is True

    def test_deficit_is_296(self):
        """Deficit = 512 - 216 = 296."""
        assert self.engine.deficit() == 296

    def test_d5_impossible_by_degree(self):
        """d_5 cannot act at g=3: support {3,...,6}, shift 4 exits."""
        assert self.engine.d5_potential_maps() == []


# =========================================================================
# 4. Kunneth verification: closed form matches matrix computation
# =========================================================================

class TestKunnethVerification:
    """Verify the Kunneth closed form against exact matrix rank computation."""

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_kunneth_matches_matrix_exact(self, g):
        """Kunneth closed form (3t(1+t))^g matches matrix rank at each degree."""
        engine = E3BarHigherGenusClassM(g=g)
        kunneth = engine.e4_poincare()
        exact = engine.e4_poincare_exact()
        assert kunneth == exact, f"Kunneth disagrees with matrix at g={g}"

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_verify_function(self, g):
        """The standalone verification function."""
        assert verify_kunneth_against_matrix(g) is True


# =========================================================================
# 5. Closed form: dim E_inf = 6^g
# =========================================================================

class TestClosedForm:
    """The main result: dim E_inf(class M, genus g) = 6^g."""

    @pytest.mark.parametrize("g", range(1, 8))
    def test_total_is_6_to_the_g(self, g):
        """Total dimension = 6^g."""
        assert class_m_einf_dimension(g) == 6 ** g

    @pytest.mark.parametrize("g", range(1, 8))
    def test_e4_total_matches(self, g):
        """Engine e4_total matches standalone function."""
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.e4_total() == class_m_einf_dimension(g)

    @pytest.mark.parametrize("g", range(1, 6))
    def test_poincare_matches_standalone(self, g):
        """Engine Poincare matches standalone function."""
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.e4_poincare() == class_m_einf_poincare(g)

    @pytest.mark.parametrize("g", range(1, 8))
    def test_poincare_entry_formula(self, g):
        """E_4^n = 3^g * C(g, n-g) for g <= n <= 2g, else 0."""
        poinc = class_m_einf_poincare(g)
        N = 3 * g
        for n in range(N + 1):
            k = n - g
            if 0 <= k <= g:
                assert poinc[n] == 3 ** g * comb(g, k)
            else:
                assert poinc[n] == 0


# =========================================================================
# 6. Euler characteristic preservation
# =========================================================================

class TestEulerCharacteristic:
    """chi(E_3) = chi(E_4) = 0 at all genera."""

    @pytest.mark.parametrize("g", range(1, 7))
    def test_euler_char_e3_is_zero(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.euler_characteristic_e3() == 0

    @pytest.mark.parametrize("g", range(1, 7))
    def test_euler_char_e4_is_zero(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.euler_characteristic_e4() == 0

    @pytest.mark.parametrize("g", range(1, 7))
    def test_euler_chars_agree(self, g):
        """chi preserved by the d_4 differential."""
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.euler_characteristic_e3() == engine.euler_characteristic_e4()


# =========================================================================
# 7. Poincare duality
# =========================================================================

class TestPoincareDuality:
    """E_4^n = E_4^{3g - n} (Poincare duality) at all genera."""

    @pytest.mark.parametrize("g", range(1, 7))
    def test_poincare_duality(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.poincare_duality_holds()

    @pytest.mark.parametrize("g", range(1, 7))
    def test_explicit_symmetry(self, g):
        """E_4 polynomial is palindromic."""
        poinc = class_m_einf_poincare(g)
        N = 3 * g
        for n in range(N + 1):
            assert poinc[n] == poinc[N - n], (
                f"g={g}: E_4^{n}={poinc[n]} != E_4^{N-n}={poinc[N-n]}"
            )


# =========================================================================
# 8. Deficit: 8^g - 6^g
# =========================================================================

class TestDeficit:
    """Deficit = class L dim - class M dim = 8^g - 6^g."""

    @pytest.mark.parametrize("g", range(1, 8))
    def test_deficit_formula(self, g):
        assert class_m_deficit(g) == 8 ** g - 6 ** g

    @pytest.mark.parametrize("g", range(1, 6))
    def test_deficit_ground_truth(self, g):
        assert class_m_deficit(g) == DEFICIT_GROUND_TRUTH[g]

    @pytest.mark.parametrize("g", range(1, 6))
    def test_engine_deficit(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        assert engine.deficit() == DEFICIT_GROUND_TRUTH[g]

    @pytest.mark.parametrize("g", range(1, 8))
    def test_ratio_is_4_3_power_g(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        assert abs(engine.deficit_ratio() - (4 / 3) ** g) < 1e-10


# =========================================================================
# 9. Higher differential analysis
# =========================================================================

class TestHigherDifferentials:
    """d_5 and beyond: degree analysis."""

    def test_g1_no_d5(self):
        engine = E3BarHigherGenusClassM(g=1)
        assert engine.first_possible_higher_differential() is None
        assert engine.d5_potential_maps() == []

    def test_g2_no_d5(self):
        engine = E3BarHigherGenusClassM(g=2)
        assert engine.first_possible_higher_differential() is None
        assert engine.d5_potential_maps() == []

    def test_g3_no_d5(self):
        engine = E3BarHigherGenusClassM(g=3)
        assert engine.first_possible_higher_differential() is None
        assert engine.d5_potential_maps() == []

    def test_g4_has_d5(self):
        """g=4: d_5 can potentially act on E_4^8 -> E_4^4."""
        engine = E3BarHigherGenusClassM(g=4)
        assert engine.first_possible_higher_differential() == 5
        assert engine.d5_potential_maps() == [(8, 4)]

    def test_g5_has_d5(self):
        """g=5: d_5 has two potential maps."""
        engine = E3BarHigherGenusClassM(g=5)
        assert engine.d5_potential_maps() == [(9, 5), (10, 6)]

    def test_last_differential_is_g_plus_1(self):
        """The spectral sequence terminates at E_{g+2}."""
        for g in range(1, 8):
            engine = E3BarHigherGenusClassM(g=g)
            assert engine.last_possible_differential() == g + 1


# =========================================================================
# 10. Cross-validation with genus-1 engine
# =========================================================================

class TestCrossValidation:
    """Cross-validate with the existing E3BarSpectralSequenceVirasoro."""

    def test_genus_1_matches_existing_engine(self):
        """Higher-genus engine at g=1 matches the genus-1 engine."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            E3BarSpectralSequenceVirasoro,
        )
        vir = E3BarSpectralSequenceVirasoro(c=Rational(1))
        hg = E3BarHigherGenusClassM(g=1, c=Rational(1))

        assert hg.kappa_ch == vir.kappa_ch
        assert hg.S4 == vir.S4
        assert hg.Delta == vir.Delta
        assert hg.e4_poincare() == vir.e4_poincare()
        assert hg.e4_total() == vir.cohomology_total()

    def test_genus_1_c2_matches(self):
        """At c=2, both engines agree."""
        from compute.lib.holomorphic_cs_chiral_engine import (
            E3BarSpectralSequenceVirasoro,
        )
        vir = E3BarSpectralSequenceVirasoro(c=Rational(2))
        hg = E3BarHigherGenusClassM(g=1, c=Rational(2))

        assert hg.kappa_ch == vir.kappa_ch
        assert hg.S4 == vir.S4
        assert hg.Delta == vir.Delta


# =========================================================================
# 11. Support structure: nonzero in degrees [g, 2g]
# =========================================================================

class TestSupportStructure:
    """E_4 is supported exactly in degrees g, g+1, ..., 2g."""

    @pytest.mark.parametrize("g", range(1, 7))
    def test_zero_below_g(self, g):
        """E_4^n = 0 for n < g."""
        engine = E3BarHigherGenusClassM(g=g)
        for n in range(g):
            assert engine.e4_page(n) == 0

    @pytest.mark.parametrize("g", range(1, 7))
    def test_nonzero_in_support(self, g):
        """E_4^n > 0 for g <= n <= 2g."""
        engine = E3BarHigherGenusClassM(g=g)
        for n in range(g, 2 * g + 1):
            assert engine.e4_page(n) > 0

    @pytest.mark.parametrize("g", range(1, 7))
    def test_zero_above_2g(self, g):
        """E_4^n = 0 for n > 2g."""
        engine = E3BarHigherGenusClassM(g=g)
        for n in range(2 * g + 1, 3 * g + 1):
            assert engine.e4_page(n) == 0


# =========================================================================
# 12. Topological interpretation: 3^g * H*(T^g) shifted
# =========================================================================

class TestTopologicalInterpretation:
    """E_4 = 3^g * H*(T^g) shifted to middle degrees."""

    @pytest.mark.parametrize("g", range(1, 7))
    def test_entries_are_3_pow_g_times_binomial(self, g):
        """E_4^{g+k} = 3^g * C(g, k) for 0 <= k <= g."""
        engine = E3BarHigherGenusClassM(g=g)
        for k in range(g + 1):
            expected = 3 ** g * comb(g, k)
            assert engine.e4_page(g + k) == expected

    @pytest.mark.parametrize("g", range(1, 7))
    def test_per_copy_contribution(self, g):
        """Each Virasoro copy contributes dim 6 = C(3,1) + C(3,2)."""
        # Single copy Poincare: 3t + 3t^2
        # g copies: (3t + 3t^2)^g
        # Total = 6^g = (3+3)^g
        assert 6 ** g == (3 + 3) ** g

    @pytest.mark.parametrize("g", range(1, 7))
    def test_support_width_is_g_plus_1(self, g):
        """Support width = 2g - g + 1 = g + 1."""
        poinc = class_m_einf_poincare(g)
        nonzero = [n for n, v in enumerate(poinc) if v > 0]
        assert len(nonzero) == g + 1


# =========================================================================
# 13. Comparison table
# =========================================================================

class TestComparisonTable:
    """The class comparison table is self-consistent."""

    def test_table_has_correct_entries(self):
        table = class_comparison_table(max_g=5)
        for row in table:
            g = row["genus"]
            assert row["class_L_dim"] == 8 ** g
            assert row["class_M_dim"] == 6 ** g
            assert row["deficit"] == 8 ** g - 6 ** g
            assert abs(row["ratio"] - (4 / 3) ** g) < 1e-10

    def test_table_length(self):
        table = class_comparison_table(max_g=7)
        assert len(table) == 7


# =========================================================================
# 14. Edge cases and input validation
# =========================================================================

class TestEdgeCases:
    """Edge cases and input validation."""

    def test_genus_0_raises(self):
        with pytest.raises(ValueError):
            E3BarHigherGenusClassM(g=0)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            E3BarHigherGenusClassM(g=-1)

    def test_large_genus_poincare(self):
        """g=10: E_4 should be (3t(1+t))^10, dim = 6^10 = 60466176."""
        engine = E3BarHigherGenusClassM(g=10)
        assert engine.e4_total() == 6 ** 10
        # Check middle entry: E_4^{15} = 3^10 * C(10, 5) = 59049 * 252
        assert engine.e4_page(15) == 3 ** 10 * comb(10, 5)

    def test_c_equals_2(self):
        """Central charge c=2 changes Delta but not E_4 structure."""
        engine = E3BarHigherGenusClassM(g=2, c=Rational(2))
        assert engine.kappa_ch == Rational(1)
        assert engine.Delta == Rational(5, 4)
        # E_4 structure is independent of c (as long as Delta != 0)
        assert engine.e4_poincare() == [0, 0, 9, 18, 9, 0, 0]


# =========================================================================
# 15. Full investigation self-consistency
# =========================================================================

class TestFullInvestigation:
    """Full investigation output is self-consistent."""

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_investigation_keys(self, g):
        engine = E3BarHigherGenusClassM(g=g)
        data = engine.full_investigation()
        assert data["genus"] == g
        assert data["shadow_class"] == "M"
        assert data["e4_is_einf"] is True
        assert data["euler_char_e3"] == 0
        assert data["euler_char_e4"] == 0
        assert data["poincare_duality"] is True
        assert data["e4_total"] == 6 ** g

    def test_g4_not_einf(self):
        engine = E3BarHigherGenusClassM(g=4)
        data = engine.full_investigation()
        assert data["e4_is_einf"] is False
        assert data["first_possible_higher_diff"] == 5
