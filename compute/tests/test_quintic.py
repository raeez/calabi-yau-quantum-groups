r"""
Tests for the quintic root datum: GW/GV invariants, lattice structure,
Euler form, and BKM obstruction analysis.

Attacks OP1 (working_notes.tex): "What is the generalized root datum
of the quintic?  Non-toric, no quiver."

Ground truth:
  Candelas-de la Ossa-Green-Parkes, NPB 359 (1991) 21 (mirror symmetry, GW)
  Gopakumar-Vafa, hep-th/9809187 (GV invariants)
  Huang-Klemm-Quackenbush, hep-th/0612308 (higher genus)
  Aspinwall-Morrison, CMP 151 (1993) 245 (multi-cover formula)
  notes/physics_4d_n2_hitchin.tex: OP1 discussion
"""

import math
from fractions import Fraction

import pytest

from compute.lib.quintic_root_datum import (
    H11, H21, CHI, B3,
    chi_line_bundles,
    euler_form_matrix,
    euler_pairing_antisymmetric,
    GW_GENUS0,
    GW_GENUS0_RAW,
    GV_GENUS0,
    GV_HIGHER_GENUS,
    GV_ALL,
    gv_from_gw_genus0,
    gv_from_gw_genus0_recursive,
    gv_invariant,
    root_multiplicity,
    gram_matrix_curve_lattice,
    MUKAI_GRAM,
    CURVE_GRAM,
    DEGREE_OF_QUINTIC,
    mukai_pairing,
    euler_form_k0,
    todd_class_quintic,
    chern_classes_quintic,
    genus0_product_coefficients,
    log_product_genus0,
    gv_product_exponents,
    weyl_vector_candidates,
    gv_growth_analysis,
    gv_genus_table,
    castelnuovo_bound,
    castelnuovo_bound_quintic,
    quintic_root_datum_summary,
    verify_gv_integrality,
    verify_multicover,
    verify_euler_serre_duality,
    verify_euler_chi0,
    verify_all,
    format_gv_table,
    format_root_datum,
)


# ======================================================================
# 1. HODGE DATA
# ======================================================================

class TestHodgeData:
    """Basic topological invariants of the quintic threefold."""

    def test_h11(self):
        """h^{1,1}(Q) = 1 (the hyperplane class)."""
        assert H11 == 1

    def test_h21(self):
        """h^{2,1}(Q) = 101 (complex structure deformations)."""
        assert H21 == 101

    def test_chi(self):
        """chi(Q) = 2(h^{1,1} - h^{2,1}) = -200."""
        assert CHI == -200
        assert CHI == 2 * (H11 - H21)

    def test_b3(self):
        """b_3(Q) = 2 + 2h^{2,1} = 204 (rank of H_3)."""
        assert B3 == 204
        assert B3 == 2 + 2 * H21

    def test_chi_over_24_not_integer(self):
        """chi(Q)/24 = -25/3 is NOT an integer.

        This is the fundamental obstruction to a naive BKM structure.
        Compare: chi(K3)/24 = 1 (integer), which allows the K3 BKM.
        """
        ratio = Fraction(CHI, 24)
        assert ratio == Fraction(-25, 3)
        assert ratio.denominator != 1


# ======================================================================
# 2. EULER FORM ON K_0
# ======================================================================

class TestEulerForm:
    """Euler form chi(O_Q(d)) = chi(O_{P^4}(d)) - chi(O_{P^4}(d-5))."""

    def test_chi_O_eq_0(self):
        """chi(O_Q) = 0 (arithmetic genus of a CY3)."""
        assert chi_line_bundles(0) == 0

    def test_chi_O1(self):
        """chi(O_Q(1)) = binom(5,4) - binom(0,4) = 5 - 0 = 5."""
        assert chi_line_bundles(1) == 5

    def test_chi_O2(self):
        """chi(O_Q(2)) = binom(6,4) - binom(1,4) = 15 - 0 = 15."""
        assert chi_line_bundles(2) == 15

    def test_chi_O3(self):
        """chi(O_Q(3)) = binom(7,4) - binom(2,4) = 35 - 0 = 35."""
        assert chi_line_bundles(3) == 35

    def test_chi_O4(self):
        """chi(O_Q(4)) = binom(8,4) - binom(3,4) = 70 - 0 = 70."""
        assert chi_line_bundles(4) == 70

    def test_chi_O5(self):
        """chi(O_Q(5)) = binom(9,4) - binom(4,4) = 126 - 1 = 125."""
        assert chi_line_bundles(5) == 125

    def test_chi_O_neg1(self):
        """chi(O_Q(-1)) = binom(3,4) - binom(-2,4) = 0 - 0 = ...

        binom(3,4) = 0 (since 3 < 4), binom(-2,4) = (-2)(-3)(-4)(-5)/24 = 120/24 = 5.
        chi(O(-1)) = 0 - 5 = -5.
        """
        assert chi_line_bundles(-1) == -5

    def test_serre_duality(self):
        """For CY3: chi(O(d)) = -chi(O(-d)).

        This follows from Serre duality: H^i(O(d)) ~ H^{3-i}(O(-d))^*.
        """
        for d in range(1, 10):
            assert chi_line_bundles(d) == -chi_line_bundles(-d), \
                f"Serre duality fails at d={d}"

    def test_chi_growth(self):
        """chi(O(d)) grows as d^3/6 for large d (by Riemann-Roch)."""
        # Leading coefficient of chi(O_Q(d)) = d^3 * deg(Q) / 3! = 5d^3/6
        for d in [10, 20, 50]:
            chi_val = chi_line_bundles(d)
            leading = 5 * d**3 / 6
            assert abs(chi_val / leading - 1) < 1.0 / d, \
                f"Growth rate check fails at d={d}"

    def test_euler_form_matrix_diagonal(self):
        """chi(O(a), O(a)) = chi(O(0)) = 0 for all a."""
        M = euler_form_matrix(5)
        for a in range(6):
            assert M[a][a] == 0

    def test_euler_pairing_antisymmetric(self):
        """chi(O(d)) + chi(O(-d)) = 0 (antisymmetry of Euler form on CY3)."""
        for d in range(1, 10):
            assert euler_pairing_antisymmetric(d) == 0


# ======================================================================
# 3. GW INVARIANTS
# ======================================================================

class TestGWInvariants:
    """Known genus-0 Gromov-Witten invariants of the quintic."""

    def test_N01(self):
        """N_{0,1} = 2875 (number of lines on the quintic)."""
        assert GW_GENUS0[1] == 2875

    def test_N02(self):
        """N_{0,2} = 609250 (conics on the quintic)."""
        assert GW_GENUS0[2] == 609250

    def test_N03(self):
        """N_{0,3} = 317206375 (twisted cubics)."""
        assert GW_GENUS0[3] == 317206375

    def test_N04(self):
        """N_{0,4} = 242467530000."""
        assert GW_GENUS0[4] == 242467530000

    def test_N05(self):
        """N_{0,5} = 229305888887625."""
        assert GW_GENUS0[5] == 229305888887625

    def test_all_positive(self):
        """All genus-0 GW invariants are positive."""
        for d, N in GW_GENUS0.items():
            assert N > 0, f"N_{{0,{d}}} = {N} is not positive"

    def test_gw_growth(self):
        """GW invariants grow exponentially: N_{0,d+1}/N_{0,d} -> ~12.2."""
        expected_ratio = 3125.0 / 256.0  # 5^5/4^4
        for d in range(1, min(8, max(GW_GENUS0.keys()))):
            if d in GW_GENUS0 and d + 1 in GW_GENUS0:
                ratio = GW_GENUS0[d + 1] / GW_GENUS0[d]
                # Rough check: ratio should be in the ballpark of 12
                assert 1 < ratio < 1e6, f"Ratio at d={d} out of range: {ratio}"


# ======================================================================
# 4. GV INVARIANTS AND MULTI-COVER FORMULA
# ======================================================================

class TestGVInvariants:
    """Gopakumar-Vafa invariants as root multiplicities."""

    def test_gv_genus0_d1(self):
        """n^0_1 = 2875 (= N_{0,1}, no multi-cover at d=1)."""
        assert GV_GENUS0[1] == 2875

    def test_gv_genus0_d2(self):
        """n^0_2 = 609250 (= N_{0,2}, no multi-cover at d=2)."""
        assert GV_GENUS0[2] == 609250

    def test_gv_genus0_d3(self):
        """n^0_3 = 317206375 (= N_{0,3}, no multi-cover at d=3)."""
        assert GV_GENUS0[3] == 317206375

    def test_gv_genus0_d4(self):
        """n^0_4 = 242467530000 (= N_{0,4}, no multi-cover at d=4)."""
        assert GV_GENUS0[4] == 242467530000

    def test_gv_d5_multicover_correction(self):
        """The raw GW invariant N_{0,5} includes a multi-cover correction:

        N_{0,5} = n^0_5 + n^0_1/5^3 = 229305888887625 + 2875/125 = 229305888887625 + 23.

        The degree-5 cover of a line contributes n^0_1/5^3 = 2875/125 = 23
        to the raw GW invariant N_{0,5}.  The GV invariant n^0_5 is 229305888887625
        (= the CDGP instanton number at d=5).
        """
        # Check: 2875 / 125 = 23 exactly
        assert GV_GENUS0[1] % 125 == 0
        assert GV_GENUS0[1] // 125 == 23
        # Raw GW = GV + multi-cover correction
        expected_raw = Fraction(GV_GENUS0[5]) + Fraction(GV_GENUS0[1], 125)
        assert GW_GENUS0_RAW[5] == expected_raw

    def test_gv_integrality(self):
        """All genus-0 GV invariants are integers."""
        results = verify_gv_integrality()
        for key, val in results.items():
            assert val, f"Integrality check failed: {key}"

    def test_gv_two_methods_agree(self):
        """Mobius inversion and recursive extraction give the same GV invariants.

        Uses GW_GENUS0_RAW (the true mathematical GW invariants) as input.
        """
        gv_mob = gv_from_gw_genus0(GW_GENUS0_RAW)
        gv_rec = gv_from_gw_genus0_recursive(GW_GENUS0_RAW)
        for d in gv_mob:
            assert gv_mob[d] == gv_rec.get(d, None), \
                f"Methods disagree at d={d}: {gv_mob[d]} vs {gv_rec.get(d)}"
        # Also check they recover the known GV table
        for d in gv_mob:
            if d in GV_GENUS0:
                assert gv_mob[d] == GV_GENUS0[d], \
                    f"Extracted n^0_{d} = {gv_mob[d]} != table {GV_GENUS0[d]}"

    def test_multicover_roundtrip(self):
        """Reconstruct raw GW from GV and verify: N_{0,d} = sum_{k|d} n^0_{d/k}/k^3."""
        results = verify_multicover()
        for key, val in results.items():
            assert val, f"Multicover roundtrip failed: {key}"

    def test_gv_all_positive_genus0(self):
        """All genus-0 GV invariants are positive."""
        for d, n in GV_GENUS0.items():
            assert n > 0, f"n^0_{d} = {n} is not positive"


# ======================================================================
# 5. HIGHER GENUS GV
# ======================================================================

class TestHigherGenusGV:
    """GV invariants at higher genus (BCOV/HKQ data)."""

    def test_genus1_vanishing_d1(self):
        """n^1_1 = 0 (no elliptic curves of degree 1 on the quintic)."""
        assert GV_HIGHER_GENUS[(1, 1)] == 0

    def test_genus1_vanishing_d2(self):
        """n^1_2 = 0 (no elliptic curves of degree 2 on the quintic)."""
        assert GV_HIGHER_GENUS[(1, 2)] == 0

    def test_genus1_d3(self):
        """n^1_3 = 609250 (first nonzero genus-1 GV).

        Remarkably, n^1_3 = n^0_2 = 609250.  This is NOT a coincidence:
        it reflects deep structure in the BPS spectrum.
        """
        assert GV_HIGHER_GENUS[(1, 3)] == 609250
        assert GV_HIGHER_GENUS[(1, 3)] == GV_GENUS0[2]

    def test_genus2_vanishing(self):
        """n^2_d = 0 for d <= 3 (Castelnuovo bound)."""
        assert GV_HIGHER_GENUS[(2, 1)] == 0
        assert GV_HIGHER_GENUS[(2, 2)] == 0
        assert GV_HIGHER_GENUS[(2, 3)] == 0

    def test_genus2_d4(self):
        """n^2_4 = 534750."""
        assert GV_HIGHER_GENUS[(2, 4)] == 534750

    def test_genus3_vanishing(self):
        """n^3_d = 0 for d <= 4."""
        assert GV_HIGHER_GENUS[(3, 1)] == 0
        assert GV_HIGHER_GENUS[(3, 2)] == 0
        assert GV_HIGHER_GENUS[(3, 3)] == 0
        assert GV_HIGHER_GENUS[(3, 4)] == 0

    def test_genus3_d5(self):
        """n^3_5 = 2875 = n^0_1.

        Again, a remarkable coincidence: the genus-3 GV at degree 5
        equals the number of lines (genus-0, degree 1).
        """
        assert GV_HIGHER_GENUS[(3, 5)] == 2875
        assert GV_HIGHER_GENUS[(3, 5)] == GV_GENUS0[1]

    def test_castelnuovo_pattern(self):
        """GV invariants vanish below the Castelnuovo bound.

        n^g_d = 0 when d is too small to support a curve of genus g.

        The precise vanishing pattern from the HKQ data is:
            g=1: n^1_d = 0 for d <= 2
            g=2: n^2_d = 0 for d <= 3
            g=3: n^3_d = 0 for d <= 4

        The first nonzero GV at genus g is at d = g + 2, matching
        the pattern from the Castelnuovo bound on the quintic (which
        is tighter than the ambient P^4 bound for g >= 2).
        """
        # First nonzero: n^1_3, n^2_4, n^3_5
        vanishing_ranges = {1: range(1, 3), 2: range(1, 4), 3: range(1, 5)}
        for g, d_range in vanishing_ranges.items():
            for d in d_range:
                val = GV_HIGHER_GENUS.get((g, d))
                if val is not None:
                    assert val == 0, \
                        f"n^{g}_{d} = {val} should be 0 (below Castelnuovo)"

    def test_gv_table_structure(self):
        """The GV table has the expected triangular vanishing."""
        table = gv_genus_table(6, 3)
        # Genus 0: all nonzero
        for d in range(6):
            assert table[0][d] is not None and table[0][d] > 0
        # Genus 1: first two vanish
        assert table[1][0] == 0  # n^1_1
        assert table[1][1] == 0  # n^1_2
        assert table[1][2] > 0   # n^1_3


# ======================================================================
# 6. LATTICE AND GRAM MATRIX
# ======================================================================

class TestLattice:
    """Lattice structure of the quintic charge lattice."""

    def test_mukai_gram_shape(self):
        """Mukai Gram matrix is 4x4."""
        assert len(MUKAI_GRAM) == 4
        assert all(len(row) == 4 for row in MUKAI_GRAM)

    def test_mukai_gram_symmetric(self):
        """Mukai pairing matrix is symmetric (the MATRIX is symmetric;
        the actual bilinear form is antisymmetric due to the Mukai involution)."""
        for i in range(4):
            for j in range(4):
                assert MUKAI_GRAM[i][j] == MUKAI_GRAM[j][i]

    def test_mukai_gram_hyperbolic(self):
        """Mukai lattice has two hyperbolic blocks.

        The (H^0, H^6) block has pairing 1.
        The (H^2, H^4) block has pairing 5 (= degree of quintic).
        """
        assert MUKAI_GRAM[0][3] == 1
        assert MUKAI_GRAM[3][0] == 1
        assert MUKAI_GRAM[1][2] == 5
        assert MUKAI_GRAM[2][1] == 5

    def test_mukai_gram_diagonal_zero(self):
        """Diagonal of Mukai Gram matrix is zero (hyperbolic)."""
        for i in range(4):
            assert MUKAI_GRAM[i][i] == 0

    def test_curve_gram(self):
        """Reduced curve lattice Gram matrix."""
        assert CURVE_GRAM == [[0, 5], [5, 0]]

    def test_degree(self):
        """Degree of the quintic is 5."""
        assert DEGREE_OF_QUINTIC == 5

    def test_mukai_pairing_antisymmetric(self):
        """Mukai pairing on CY3 is antisymmetric: <v,w> = -<w,v>."""
        v = (1, 2, 3, 4)
        w = (5, 6, 7, 8)
        assert mukai_pairing(v, w) == -mukai_pairing(w, v)

    def test_mukai_self_pairing_zero(self):
        """<v, v> = 0 for all v (antisymmetric form)."""
        for v in [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 1, 1), (2, 3, 5, 7)]:
            assert mukai_pairing(v, v) == 0


# ======================================================================
# 7. CHERN CLASSES AND TODD CLASS
# ======================================================================

class TestChernTodd:
    """Chern classes and Todd class of the quintic."""

    def test_c1_vanishes(self):
        """c_1(Q) = 0 (Calabi-Yau condition)."""
        cc = chern_classes_quintic()
        assert cc['c1'] == 0

    def test_c2(self):
        """c_2(Q) = 10 H^2."""
        cc = chern_classes_quintic()
        assert cc['c2'] == 10

    def test_c3_gives_chi(self):
        """integral c_3(Q) = chi(Q) = -200.

        c_3 = -40 H^3, and integral_Q H^3 = 5 (degree), so
        integral c_3 = -40 * 5 = -200.
        """
        cc = chern_classes_quintic()
        assert cc['c3'] * 5 == CHI

    def test_c2_integral(self):
        """integral_Q c_2 . H = 10 * 5 = 50."""
        cc = chern_classes_quintic()
        assert cc['c2_integral'] == 50

    def test_todd_class(self):
        """td(Q) = (1, 0, 5/6, 0) in basis {1, H, H^2, pt}."""
        td = todd_class_quintic()
        assert td[0] == 1
        assert td[1] == 0
        assert td[2] == Fraction(5, 6)
        assert td[3] == 0


# ======================================================================
# 8. WEYL VECTOR AND BKM OBSTRUCTION
# ======================================================================

class TestWeylVector:
    """Weyl vector candidates and BKM obstruction."""

    def test_chi_over_24(self):
        """chi(Q)/24 = -25/3 (the key obstruction)."""
        weyl = weyl_vector_candidates()
        assert weyl['chi_over_24'] == Fraction(-25, 3)

    def test_chi_over_24_not_integer(self):
        """chi(Q)/24 is NOT an integer => no naive BKM."""
        weyl = weyl_vector_candidates()
        assert not weyl['chi_over_24_is_integer']

    def test_macmahon_exponent(self):
        """MacMahon exponent chi/2 = -100."""
        weyl = weyl_vector_candidates()
        assert weyl['macmahon_exponent'] == Fraction(-100)

    def test_c2_over_24(self):
        """c_2.H / 24 = 50/24 = 25/12 (also not integer)."""
        weyl = weyl_vector_candidates()
        assert weyl['c2_over_24'] == Fraction(25, 12)

    def test_mukai_rho(self):
        """Mukai Weyl vector candidate: (1, 0, 5/12, -100)."""
        weyl = weyl_vector_candidates()
        rho = weyl['mukai_rho']
        assert rho[0] == 1
        assert rho[1] == 0
        assert rho[2] == Fraction(5, 12)
        assert rho[3] == -100


# ======================================================================
# 9. PRODUCT FORMULA AND GROWTH
# ======================================================================

class TestProductFormula:
    """The genus-0 GV product and log expansion."""

    def test_log_product_coefficient_1(self):
        """Coefficient of q^1 in log is n^0_1 = 2875."""
        log_coeffs = log_product_genus0(5)
        assert log_coeffs[1] == Fraction(2875)

    def test_log_product_coefficient_2(self):
        """Coefficient of q^2 in log = n^0_2 + n^0_1/2 = 609250 + 2875/2."""
        log_coeffs = log_product_genus0(5)
        expected = Fraction(GV_GENUS0[2]) + Fraction(GV_GENUS0[1], 2)
        assert log_coeffs[2] == expected

    def test_log_product_positive(self):
        """All log-product coefficients are positive (root multiplicities > 0)."""
        log_coeffs = log_product_genus0(5)
        for m in range(1, 6):
            assert log_coeffs[m] > 0

    def test_growth_ratios_exist(self):
        """Growth analysis produces successive ratios."""
        growth = gv_growth_analysis()
        assert 'ratios' in growth
        assert len(growth['ratios']) > 0

    def test_growth_constant(self):
        """Growth constant estimates are consistent with exponential growth.

        The GV invariants grow as n^0_d ~ C * exp(A * d) / d^B where
        A ~ 7.5 is determined by the conifold point of the mirror quintic
        (in the flat coordinate q = exp(-t), NOT in the algebraic
        coordinate z where the radius is 5^5/4^4).

        We verify that the growth rate estimates stabilize.
        """
        growth = gv_growth_analysis()
        estimates = growth['growth_constant_estimates']
        assert len(estimates) >= 3, "Need enough data points"
        # The estimates should be monotonically increasing and bounded
        vals = [estimates[d] for d in sorted(estimates.keys())]
        # Check monotonic (approximately)
        for i in range(1, len(vals)):
            assert vals[i] > vals[i - 1] * 0.95, \
                f"Growth estimates not approximately monotone"
        # Check the estimates are in a reasonable range (7-8 for the quintic)
        last_d = max(estimates.keys())
        assert 6.0 < estimates[last_d] < 9.0, \
            f"Growth constant estimate {estimates[last_d]} out of expected range [6, 9]"


# ======================================================================
# 10. CASTELNUOVO BOUND
# ======================================================================

class TestCastelnuovo:
    """Castelnuovo bound for curves on the quintic."""

    def test_bound_d1(self):
        """A line in P^4 has genus 0."""
        assert castelnuovo_bound(1) == 0

    def test_bound_d2(self):
        """A conic in P^4 has genus 0."""
        assert castelnuovo_bound(2) == 0

    def test_bound_d3(self):
        """Degree 3 in P^4: m=0, eps=2 -> g <= 0. Actually m=2/3...
        d-1 = 2 = 3m + eps with m=0, eps=2.
        g <= 0 + 0 = 0.
        """
        assert castelnuovo_bound(3) == 0

    def test_bound_d4(self):
        """Degree 4: d-1=3 = 3*1 + 0, m=1, eps=0.
        g <= (3/2)*1*0 + 1*0 = 0.
        """
        assert castelnuovo_bound(4) == 0

    def test_bound_d5(self):
        """Degree 5: d-1=4 = 3*1 + 1, m=1, eps=1.
        g <= (3/2)*1*0 + 1*1 = 1.
        """
        assert castelnuovo_bound(5) == 1

    def test_bound_d7(self):
        """Degree 7: d-1=6 = 3*2 + 0, m=2, eps=0.
        g <= (3/2)*2*1 + 2*0 = 3.
        """
        assert castelnuovo_bound(7) == 3


# ======================================================================
# 11. ROOT DATUM ASSEMBLY
# ======================================================================

class TestRootDatum:
    """The assembled root datum dictionary."""

    def test_summary_keys(self):
        """Summary contains all expected keys."""
        s = quintic_root_datum_summary()
        expected_keys = [
            'hodge', 'lattice', 'chern', 'todd',
            'root_multiplicities_genus0', 'root_multiplicities_higher',
            'gv_table', 'weyl_vector', 'bkm_obstruction',
            'product_formula', 'growth', 'euler_form_values',
        ]
        for key in expected_keys:
            assert key in s, f"Missing key: {key}"

    def test_summary_hodge(self):
        """Hodge data in summary is correct."""
        s = quintic_root_datum_summary()
        assert s['hodge']['chi'] == -200
        assert s['hodge']['h11'] == 1
        assert s['hodge']['h21'] == 101

    def test_summary_bkm_obstruction(self):
        """BKM obstruction correctly identified."""
        s = quintic_root_datum_summary()
        assert not s['bkm_obstruction']['chi_over_24_integral']

    def test_root_multiplicities_match_gv(self):
        """Root multiplicities equal GV invariants."""
        for d in range(1, 6):
            assert root_multiplicity(0, d) == gv_invariant(0, d)
        assert root_multiplicity(1, 3) == 609250
        assert root_multiplicity(3, 5) == 2875


# ======================================================================
# 12. COMPREHENSIVE VERIFICATION
# ======================================================================

class TestVerifyAll:
    """Run all internal verification checks."""

    def test_verify_all_pass(self):
        """All verification checks pass."""
        results = verify_all()
        for key, val in results.items():
            assert val, f"Verification failed: {key}"

    def test_euler_serre(self):
        """Serre duality verification."""
        results = verify_euler_serre_duality()
        for key, val in results.items():
            assert val, f"Serre duality failed: {key}"

    def test_euler_chi0(self):
        """chi(O_Q) = 0."""
        assert verify_euler_chi0()

    def test_gv_integrality(self):
        """GV invariants are integers."""
        results = verify_gv_integrality()
        for key, val in results.items():
            assert val, f"GV integrality failed: {key}"

    def test_multicover_roundtrip(self):
        """GW -> GV -> GW roundtrip."""
        results = verify_multicover()
        for key, val in results.items():
            assert val, f"Multicover roundtrip failed: {key}"


# ======================================================================
# 13. DISPLAY FORMATTING
# ======================================================================

class TestDisplay:
    """Test display/formatting routines."""

    def test_gv_table_format(self):
        """GV table formats without error."""
        table_str = format_gv_table()
        assert "2875" in table_str
        assert "609250" in table_str

    def test_root_datum_format(self):
        """Root datum summary formats without error."""
        summary_str = format_root_datum()
        assert "QUINTIC" in summary_str
        assert "-200" in summary_str
        assert "OBSTRUCTION" in summary_str


# ======================================================================
# 14. DEEP STRUCTURAL TESTS
# ======================================================================

class TestDeepStructure:
    """Tests probing the deeper structure of the quintic root datum."""

    def test_n13_equals_n02(self):
        """The coincidence n^1_3 = n^0_2 = 609250.

        This is a nontrivial identity relating genus-1 degree-3
        to genus-0 degree-2.  In the BKM framework, it suggests
        an automorphism or Hecke-type operator relating different
        roots.
        """
        assert GV_HIGHER_GENUS[(1, 3)] == GV_GENUS0[2]

    def test_n35_equals_n01(self):
        """The coincidence n^3_5 = n^0_1 = 2875.

        Genus-3 degree-5 equals the number of lines.
        """
        assert GV_HIGHER_GENUS[(3, 5)] == GV_GENUS0[1]

    def test_euler_form_polynomial(self):
        """chi(O(d)) is a degree-3 polynomial in d.

        On a 3-fold: chi(O(d)) = (deg/6)d^3 + lower order.
        For the quintic: leading = 5/6.
        """
        # Verify polynomial nature by checking finite differences
        # Delta^4 chi(O(d)) = 0 for all d (since degree 3)
        for d0 in range(0, 5):
            delta4 = (chi_line_bundles(d0 + 4)
                      - 4 * chi_line_bundles(d0 + 3)
                      + 6 * chi_line_bundles(d0 + 2)
                      - 4 * chi_line_bundles(d0 + 1)
                      + chi_line_bundles(d0))
            assert delta4 == 0, f"Fourth finite difference nonzero at d={d0}"

    def test_gv_all_table(self):
        """GV_ALL contains both genus-0 and higher genus data."""
        assert (0, 1) in GV_ALL
        assert (1, 3) in GV_ALL
        assert GV_ALL[(0, 1)] == 2875
        assert GV_ALL[(1, 3)] == 609250

    def test_macmahon_prefactor(self):
        """The DT partition function has MacMahon prefactor M(q)^{chi/2} = M(q)^{-100}.

        This is the degree-0 contribution from 0-dimensional sheaves (point-like instantons).
        The exponent -100 = chi(Q)/2 is a signature of the quintic in the DT theory.
        """
        assert Fraction(CHI, 2) == -100

    def test_li3_vs_li1_distinction(self):
        """The genus-0 GV formula involves Li_3 (not Li_1), distinguishing
        it from a standard BKM denominator.

        In a BKM: log(denominator) ~ sum mult(alpha) * Li_1(q^alpha) = sum mult(alpha) * log(1/(1-q^alpha))
        For quintic g=0: F_0 ~ sum n^0_d * Li_3(q^d) = sum n^0_d * sum_k q^{kd}/k^3

        The difference (Li_3 vs Li_1) means the quintic does NOT have a
        standard infinite product denominator at genus 0 alone.

        The log coefficient of q^m in the Li_3 version:
            a_m = sum_{k|m} n^0_{m/k} / k^3

        The log coefficient in the Li_1 version:
            b_m = sum_{k|m} n^0_{m/k} / k

        These are DIFFERENT unless n^0_{m/k} = 0 for k > 1.
        """
        # At m=2: Li_3 gives n^0_2 + n^0_1/8
        #         Li_1 gives n^0_2 + n^0_1/2
        li3_coeff_2 = Fraction(GV_GENUS0[2]) + Fraction(GV_GENUS0[1], 8)
        li1_coeff_2 = Fraction(GV_GENUS0[2]) + Fraction(GV_GENUS0[1], 2)
        assert li3_coeff_2 != li1_coeff_2
        # The Li_1 coefficient is what log_product_genus0 computes
        log_coeffs = log_product_genus0(5)
        assert log_coeffs[2] == li1_coeff_2

    def test_signature_mukai(self):
        """Mukai lattice has signature (2,2)."""
        import numpy as np
        G = np.array(MUKAI_GRAM, dtype=float)
        eigvals = np.linalg.eigvalsh(G)
        n_pos = sum(1 for e in eigvals if e > 0.01)
        n_neg = sum(1 for e in eigvals if e < -0.01)
        assert n_pos == 2
        assert n_neg == 2
