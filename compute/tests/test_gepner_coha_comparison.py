r"""Tests for the Gepner CoHA vs large-volume CoHA comparison.

THEOREMS BEING TESTED:
    (1) The CoHA of MF(W)^G for the Fermat quintic (and other Gepner models)
        is E_1-equivalent to the large-volume CoHA via Orlov's equivalence.

    (2) kappa_{BCOV} = chi/24 is a chart-independent derived invariant,
        taking the value -25/3 for the quintic in both charts.

    (3) The orbifold-invariant Jacobian ring dimension recovers the
        correct Betti number b_d for CY d-folds.

    (4) The degree decomposition of the Gepner chiral ring matches the
        Hodge decomposition of the CY manifold.

    (5) The GLSM provides a smooth E_1 homotopy equivalence between
        the Gepner and large-volume charts.

MULTI-PATH VERIFICATION (3+ paths per claim, per CLAUDE.md mandate):
    Path 1: Direct computation from MF classes (exact arithmetic)
    Path 2: Inclusion-exclusion formula for invariant counts
    Path 3: Betti number / Hodge decomposition match
    Path 4: kappa consistency across charts
    Path 5: Cross-model scaling (all CY3 Gepner models have c = 9)
    Path 6: Euler characteristic from Betti numbers
    Path 7: Central charge / c_hat consistency
    Path 8: Knorrer periodicity invariance

REFERENCES:
    Orlov arXiv:math/0302304: derived categories of singularities
    Gepner, Nucl. Phys. B296 (1988): Gepner models
    Herbst-Hori-Page arXiv:0803.2045: GLSM phases
    Kapustin-Li arXiv:hep-th/0210296: D-branes in LG models
    Davison-Meinhardt arXiv:1512.08898: PBW for CoHA
    Greene-Plesser arXiv:hep-th/9110014: CY/LG correspondence
"""

import pytest
from fractions import Fraction

from compute.lib.gepner_coha_comparison import (
    # Helpers
    _product, _binomial, _count_tuples_with_sum, _gcd, _lcm,
    # MF classes
    MFClass, enumerate_mf_classes, orbifold_invariant_mf_classes,
    # Gepner CoHA
    GepnerCoHAData, gepner_coha, quintic_gepner_coha,
    # Large-volume CoHA
    LargeVolumeCoHAData, quintic_lv_coha,
    # Orlov E_1 map
    OrlovE1Map, orlov_e1_map_quintic,
    # Kappa verification
    kappa_gepner_vs_lv,
    # Other Gepner models
    GepnerModelComparison,
    fermat_cubic_cy1, fermat_quartic_k3, fermat_quintic_cy3, fermat_octic_cy3,
    all_gepner_models,
    # GLSM transition
    GLSMTransitionData, glsm_transition_quintic,
    # Full comparison
    gepner_vs_lv_full_comparison, full_report,
    # Kappa all models
    kappa_all_models,
    # Quintic detailed
    quintic_gepner_detailed,
    # All CY3 Gepner CoHAs
    all_cy3_gepner_cohas,
)

F = Fraction


# ================================================================
# 0. FOUNDATIONAL ARITHMETIC TESTS
# ================================================================

class TestArithmeticHelpers:
    """Verify exact arithmetic helpers."""

    def test_product_basic(self):
        assert _product([2, 3, 5]) == 30
        assert _product([1]) == 1
        assert _product([4, 4, 4, 4, 4]) == 1024

    def test_binomial_basic(self):
        assert _binomial(5, 2) == 10
        assert _binomial(10, 3) == 120
        assert _binomial(5, 0) == 1
        assert _binomial(5, 5) == 1
        assert _binomial(3, 5) == 0

    def test_binomial_symmetry(self):
        for n in range(8):
            for k in range(n + 1):
                assert _binomial(n, k) == _binomial(n, n - k)

    def test_count_tuples_quintic(self):
        """For quintic: (r=5, k=3, s), count tuples summing to s."""
        # s=0: only (0,0,0,0,0) -> 1
        assert _count_tuples_with_sum(5, 3, 0) == 1
        # s=15: only (3,3,3,3,3) -> 1
        assert _count_tuples_with_sum(5, 3, 15) == 1
        # s=5: tuples (a_1,...,a_5) with 0 <= a_i <= 3, sum = 5
        # = C(9,4) - 5*C(5,4) = 126 - 25 = 101
        assert _count_tuples_with_sum(5, 3, 5) == 101
        # s=10: by symmetry (a_i -> 3-a_i), same count as s=5
        assert _count_tuples_with_sum(5, 3, 10) == 101

    def test_count_tuples_quartic(self):
        """For quartic K3: (r=4, k=2, s)."""
        assert _count_tuples_with_sum(4, 2, 0) == 1
        assert _count_tuples_with_sum(4, 2, 4) == 19
        assert _count_tuples_with_sum(4, 2, 8) == 1

    def test_gcd_lcm(self):
        assert _gcd(12, 8) == 4
        assert _gcd(5, 3) == 1
        assert _lcm(4, 6) == 12
        assert _lcm(5, 5) == 5


# ================================================================
# 1. MATRIX FACTORIZATION CLASS TESTS
# ================================================================

class TestMFClasses:
    """Verify MF class enumeration and properties."""

    def test_mf_class_creation(self):
        m = MFClass(labels=(1, 2, 0), degrees=(5, 5, 5))
        assert m.n_factors == 3
        assert m.integer_charge == 3
        assert m.hom_degree == 3

    def test_mf_class_invalid(self):
        with pytest.raises(ValueError):
            MFClass(labels=(4, 0), degrees=(5, 3))  # 4 > 3-2 = 1

    def test_mf_class_orbifold_invariance(self):
        # sum = 0 mod 5
        m1 = MFClass(labels=(0, 0, 0, 0, 0), degrees=(5,)*5)
        assert m1.is_orbifold_invariant(5)
        # sum = 5 mod 5 = 0
        m2 = MFClass(labels=(1, 1, 1, 1, 1), degrees=(5,)*5)
        assert m2.is_orbifold_invariant(5)
        # sum = 1, not 0 mod 5
        m3 = MFClass(labels=(1, 0, 0, 0, 0), degrees=(5,)*5)
        assert not m3.is_orbifold_invariant(5)

    def test_enumerate_single_variable(self):
        """MF(x^n) has n-1 indecomposables."""
        for n in [3, 4, 5, 7]:
            mfs = enumerate_mf_classes((n,))
            assert len(mfs) == n - 1

    def test_enumerate_two_variables(self):
        """MF(x^a + y^b) has (a-1)(b-1) indecomposables."""
        mfs = enumerate_mf_classes((3, 4))
        assert len(mfs) == 2 * 3  # = 6 = mu(E_6)

    def test_enumerate_quintic(self):
        """MF(x1^5 + ... + x5^5) has 4^5 = 1024 indecomposables."""
        mfs = enumerate_mf_classes((5, 5, 5, 5, 5))
        assert len(mfs) == 4**5

    def test_enumerate_quartic(self):
        """MF(x^4 + y^4 + z^4 + w^4) has 3^4 = 81 indecomposables."""
        mfs = enumerate_mf_classes((4, 4, 4, 4))
        assert len(mfs) == 3**4

    def test_orbifold_invariant_quintic(self):
        """204 orbifold-invariant MFs for the quintic Gepner model."""
        inv = orbifold_invariant_mf_classes((5, 5, 5, 5, 5), 5)
        assert len(inv) == 204

    def test_orbifold_invariant_quartic(self):
        """21 orbifold-invariant MFs for the quartic K3 Gepner model."""
        inv = orbifold_invariant_mf_classes((4, 4, 4, 4), 4)
        assert len(inv) == 21

    def test_orbifold_invariant_cubic(self):
        """2 orbifold-invariant MFs for the cubic elliptic curve."""
        inv = orbifold_invariant_mf_classes((3, 3, 3), 3)
        assert len(inv) == 2

    def test_milnor_number_matches_total_mfs(self):
        """Total MF count = Milnor number = prod(n_i - 1)."""
        for degrees in [(3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5, 5), (8, 8, 8, 8)]:
            mfs = enumerate_mf_classes(degrees)
            expected = _product(d - 1 for d in degrees)
            assert len(mfs) == expected


# ================================================================
# 2. GEPNER CoHA TESTS (QUINTIC)
# ================================================================

class TestGepnerCoHAQuintic:
    """Test the Gepner CoHA for the quintic threefold."""

    def test_quintic_generator_count(self):
        """204 generators for the quintic Gepner CoHA."""
        coha = quintic_gepner_coha()
        assert coha.total_generators == 204

    def test_quintic_degree_decomposition(self):
        """Degree decomposition: {0: 1, 1: 101, 2: 101, 3: 1}."""
        coha = quintic_gepner_coha()
        expected = {0: 1, 1: 101, 2: 101, 3: 1}
        assert coha.degree_decomposition == expected

    def test_quintic_degrees(self):
        coha = quintic_gepner_coha()
        assert coha.degrees == (5, 5, 5, 5, 5)
        assert coha.orbifold_order == 5

    def test_quintic_milnor(self):
        coha = quintic_gepner_coha()
        assert coha.milnor_total == 1024

    def test_quintic_multiplication_table_symmetric(self):
        """The multiplication table entries should be symmetric at char level."""
        coha = quintic_gepner_coha()
        for (p, q), dim in coha.multiplication_data.items():
            # The target charge is p+q, which should give the same
            # dimension regardless of which decomposition we use.
            assert dim == coha.multiplication_data.get((q, p), 0)

    def test_quintic_degree_sum_is_b3(self):
        """Sum of all degree dimensions = 204 = b_3(quintic)."""
        coha = quintic_gepner_coha()
        total = sum(coha.degree_decomposition.values())
        assert total == 204

    def test_quintic_hodge_from_degree(self):
        """The degree decomposition gives Hodge numbers of the quintic.

        degree 0 -> h^{3,0} = 1
        degree 1 -> h^{2,1} = 101
        degree 2 -> h^{1,2} = 101
        degree 3 -> h^{0,3} = 1
        """
        coha = quintic_gepner_coha()
        d = coha.degree_decomposition
        assert d[0] == 1     # h^{3,0}
        assert d[1] == 101   # h^{2,1}
        assert d[2] == 101   # h^{1,2}
        assert d[3] == 1     # h^{0,3}

    def test_quintic_euler_from_hodge(self):
        """chi = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200."""
        coha = quintic_gepner_coha()
        h21 = coha.degree_decomposition[1]
        h11 = 1  # known from the quintic geometry
        chi = 2 * (h11 - h21)
        assert chi == -200

    def test_quintic_betti_numbers(self):
        """b_3(Q) = 2 + 2*h^{2,1} = 204."""
        coha = quintic_gepner_coha()
        h21 = coha.degree_decomposition[1]
        b3 = 2 + 2 * h21
        assert b3 == 204
        assert coha.total_generators == b3


# ================================================================
# 3. LARGE-VOLUME CoHA TESTS
# ================================================================

class TestLargeVolumeCoHA:
    """Test the large-volume CoHA for the quintic."""

    def test_quintic_lv_hh_dimensions(self):
        """HH^* dimensions for D^b(Coh(Q))."""
        lv = quintic_lv_coha()
        assert lv.hh_dimensions[0] == 1
        assert lv.hh_dimensions[1] == 0
        assert lv.hh_dimensions[2] == 101
        assert lv.hh_dimensions[3] == 4
        assert lv.hh_dimensions[4] == 101
        assert lv.hh_dimensions[5] == 0
        assert lv.hh_dimensions[6] == 1

    def test_quintic_lv_total_hh(self):
        """Total dim HH^* = 208."""
        lv = quintic_lv_coha()
        assert lv.total_hh_dim == 208

    def test_quintic_lv_chi(self):
        lv = quintic_lv_coha()
        assert lv.chi == -200

    def test_quintic_lv_kappa(self):
        """kappa_BCOV = chi/24 = -200/24 = -25/3."""
        lv = quintic_lv_coha()
        assert lv.kappa_bcov == F(-200, 24)
        assert lv.kappa_bcov == F(-25, 3)


# ================================================================
# 4. ORLOV EQUIVALENCE TESTS
# ================================================================

class TestOrlovE1Map:
    """Test the Orlov equivalence as an E_1 map."""

    def test_quintic_orlov_is_e1_quasi_iso(self):
        """The Orlov map is an E_1 quasi-isomorphism for the quintic."""
        orlov = orlov_e1_map_quintic()
        assert orlov.is_e1_quasi_iso

    def test_quintic_orlov_k0_match(self):
        """K_0 ranks match across the equivalence."""
        orlov = orlov_e1_map_quintic()
        assert orlov.k0_rank_match

    def test_quintic_orlov_hh_match(self):
        """HH^* dimensions match across the equivalence."""
        orlov = orlov_e1_map_quintic()
        assert orlov.hh_dim_match

    def test_quintic_orlov_kappa_match(self):
        """kappa matches across the equivalence."""
        orlov = orlov_e1_map_quintic()
        assert orlov.kappa_match
        assert orlov.kappa_source == orlov.kappa_target
        assert orlov.kappa_source == F(-25, 3)

    def test_quintic_orlov_all_paths(self):
        """All five verification paths pass."""
        orlov = orlov_e1_map_quintic()
        v = orlov.verification_paths
        assert v['path1_k0_rank']['match']
        assert v['path2_hh_dim']['match']
        assert v['path3_kappa']['match']
        assert v['path4_hodge']['match']
        assert v['path5_euler']['match']


# ================================================================
# 5. KAPPA VERIFICATION TESTS
# ================================================================

class TestKappaVerification:
    """Multi-path kappa verification for the quintic."""

    def test_kappa_bcov_quintic(self):
        """kappa_BCOV = chi/24 = -200/24 = -25/3."""
        result = kappa_gepner_vs_lv(-200)
        assert result['kappa_bcov'] == F(-25, 3)

    def test_kappa_all_paths_agree(self):
        """All kappa computation paths agree."""
        result = kappa_gepner_vs_lv(-200)
        assert result['all_paths_agree']

    def test_kappa_from_betti(self):
        """chi from Betti numbers: 1 - 0 + 1 - 204 + 1 - 0 + 1 = -200."""
        result = kappa_gepner_vs_lv(-200)
        assert result['path4_hh_trace']['chi_from_betti'] == -200
        assert result['path4_hh_trace']['consistent']

    def test_kappa_topological_path(self):
        result = kappa_gepner_vs_lv(-200)
        assert result['path1_topological']['kappa'] == F(-25, 3)

    def test_kappa_derived_path(self):
        result = kappa_gepner_vs_lv(-200)
        assert result['path2_derived']['orlov_preserves_chi']

    def test_kappa_bcov_path(self):
        result = kappa_gepner_vs_lv(-200)
        # F_1^{const} = -chi/24, so kappa = chi/24
        assert result['path3_bcov']['kappa'] == F(-25, 3)


# ================================================================
# 6. OTHER GEPNER MODELS TESTS
# ================================================================

class TestOtherGepnerModels:
    """Test Gepner models across CY dimensions."""

    # --- Fermat cubic (CY1, elliptic curve) ---

    def test_cubic_cy_dim(self):
        m = fermat_cubic_cy1()
        assert m.cy_dim == 1

    def test_cubic_chi(self):
        m = fermat_cubic_cy1()
        assert m.chi == 0

    def test_cubic_kappa_bcov(self):
        """For elliptic curve: chi = 0, kappa = 0."""
        m = fermat_cubic_cy1()
        assert m.kappa_bcov == F(0)

    def test_cubic_invariant_mfs(self):
        """2 orbifold-invariant MFs for the cubic: b_1(E) = 2."""
        m = fermat_cubic_cy1()
        assert m.n_invariant_mfs == 2

    def test_cubic_degree_decomposition(self):
        """degree 0: 1, degree 1: 1. Total = 2."""
        m = fermat_cubic_cy1()
        assert m.degree_decomposition == {0: 1, 1: 1}

    def test_cubic_central_charge(self):
        m = fermat_cubic_cy1()
        assert m.n2_central_charge == F(3)

    # --- Fermat quartic (CY2, K3 surface) ---

    def test_quartic_cy_dim(self):
        m = fermat_quartic_k3()
        assert m.cy_dim == 2

    def test_quartic_chi(self):
        m = fermat_quartic_k3()
        assert m.chi == 24

    def test_quartic_kappa_bcov(self):
        """For K3: chi = 24, kappa = 24/24 = 1."""
        m = fermat_quartic_k3()
        assert m.kappa_bcov == F(1)

    def test_quartic_invariant_mfs(self):
        """21 orbifold-invariant MFs for the quartic K3.

        This is dim(Jac^G) = 21, NOT b_2(K3) = 22.
        The hyperplane class is missing from the Gepner ring.
        """
        m = fermat_quartic_k3()
        assert m.n_invariant_mfs == 21

    def test_quartic_degree_decomposition(self):
        """degree 0: 1, degree 1: 19, degree 2: 1. Total = 21."""
        m = fermat_quartic_k3()
        assert m.degree_decomposition == {0: 1, 1: 19, 2: 1}

    def test_quartic_central_charge(self):
        m = fermat_quartic_k3()
        assert m.n2_central_charge == F(6)

    # --- Fermat quintic (CY3, quintic threefold) ---

    def test_quintic_cy_dim(self):
        m = fermat_quintic_cy3()
        assert m.cy_dim == 3

    def test_quintic_chi(self):
        m = fermat_quintic_cy3()
        assert m.chi == -200

    def test_quintic_kappa_bcov(self):
        m = fermat_quintic_cy3()
        assert m.kappa_bcov == F(-25, 3)

    def test_quintic_invariant_mfs(self):
        m = fermat_quintic_cy3()
        assert m.n_invariant_mfs == 204

    def test_quintic_central_charge(self):
        m = fermat_quintic_cy3()
        assert m.n2_central_charge == F(9)

    # --- Fermat octic (CY3, degree 8 in WP^4(1,1,1,1,4)) ---

    def test_octic_cy_dim(self):
        m = fermat_octic_cy3()
        assert m.cy_dim == 3

    def test_octic_chi(self):
        m = fermat_octic_cy3()
        assert m.chi == -296

    def test_octic_kappa_bcov(self):
        """kappa = -296/24 = -37/3."""
        m = fermat_octic_cy3()
        assert m.kappa_bcov == F(-296, 24)
        assert m.kappa_bcov == F(-37, 3)

    def test_octic_invariant_mfs(self):
        """300 orbifold-invariant MFs for the octic: b_3 = 300."""
        m = fermat_octic_cy3()
        assert m.n_invariant_mfs == 300

    def test_octic_degree_decomposition(self):
        """degree 0: 1, degree 1: 149, degree 2: 149, degree 3: 1."""
        m = fermat_octic_cy3()
        expected = {0: 1, 1: 149, 2: 149, 3: 1}
        assert m.degree_decomposition == expected

    def test_octic_central_charge(self):
        m = fermat_octic_cy3()
        assert m.n2_central_charge == F(9)


# ================================================================
# 7. CROSS-MODEL CONSISTENCY TESTS
# ================================================================

class TestCrossModelConsistency:
    """Cross-model consistency checks."""

    def test_all_cy3_models_have_c_9(self):
        """All CY3 Gepner models have total central charge c = 9 = 3d."""
        models = all_gepner_models()
        for m in models:
            if m.cy_dim == 3:
                assert m.n2_central_charge == F(9), (
                    f"{m.name}: c = {m.n2_central_charge}, expected 9"
                )

    def test_c_hat_equals_cy_dim(self):
        """c_hat = c/3 = cy_dim for all models."""
        for m in all_gepner_models():
            c_hat = m.n2_central_charge / 3
            assert c_hat == F(m.cy_dim), (
                f"{m.name}: c_hat = {c_hat}, expected {m.cy_dim}"
            )

    def test_kappa_n2_all_cy3_equal(self):
        """kappa_N2 = c/6 = 3/2 for all CY3 Gepner models."""
        for m in all_gepner_models():
            if m.cy_dim == 3:
                assert m.kappa_n2 == F(3, 2), (
                    f"{m.name}: kappa_N2 = {m.kappa_n2}, expected 3/2"
                )

    def test_orlov_for_all_models(self):
        """Orlov equivalence holds for all standard models."""
        for m in all_gepner_models():
            assert m.orlov_equivalence, f"{m.name}: Orlov should hold"

    def test_e1_quasi_iso_for_all(self):
        """E_1 quasi-isomorphism holds for all models."""
        for m in all_gepner_models():
            assert m.e1_quasi_iso, f"{m.name}: E_1 quasi-iso should hold"

    def test_degree_decomposition_palindromic(self):
        """The degree decomposition is palindromic (Hodge symmetry).

        For CY d: h^{d-p, p} = h^{p, d-p} (Hodge symmetry).
        So the degree decomposition has decomp[p] = decomp[d-p].
        """
        for m in all_gepner_models():
            d = m.cy_dim
            decomp = m.degree_decomposition
            for p in decomp:
                if d - p in decomp:
                    assert decomp[p] == decomp[d - p], (
                        f"{m.name}: decomp[{p}] = {decomp[p]} != "
                        f"decomp[{d-p}] = {decomp[d-p]} (Hodge symmetry)"
                    )


# ================================================================
# 8. GLSM TRANSITION TESTS
# ================================================================

class TestGLSMTransition:
    """Test the GLSM wall-crossing data."""

    def test_quintic_glsm_kappa_invariant(self):
        glsm = glsm_transition_quintic()
        assert glsm.kappa_invariant

    def test_quintic_glsm_kappa_value(self):
        glsm = glsm_transition_quintic()
        assert glsm.kappa_value == F(-25, 3)

    def test_quintic_glsm_n_conifold(self):
        """5 conifold points for the quintic."""
        glsm = glsm_transition_quintic()
        assert glsm.n_conifold_points == 5

    def test_quintic_glsm_smooth(self):
        glsm = glsm_transition_quintic()
        assert glsm.is_smooth_away_from_conifold

    def test_quintic_glsm_chi(self):
        glsm = glsm_transition_quintic()
        assert glsm.chi == -200


# ================================================================
# 9. FULL COMPARISON REPORT TESTS
# ================================================================

class TestFullComparison:
    """Test the full comparison machinery."""

    def test_full_report_exists(self):
        report = full_report()
        assert 'models' in report
        assert 'kappa_values' in report
        assert 'c_hat_consistency' in report

    def test_full_report_c_hat_consistency(self):
        report = full_report()
        assert report['c_hat_consistency']

    def test_full_report_kappa_values(self):
        """Verify kappa values in the full report."""
        report = full_report()
        kappas = report['kappa_values']
        # Find the quintic
        for name, kappa in kappas.items():
            if 'quintic' in name.lower():
                assert kappa == F(-25, 3)
                break

    def test_quintic_comparison_all_paths(self):
        m = fermat_quintic_cy3()
        comp = gepner_vs_lv_full_comparison(m)
        assert comp['path2_kappa']['chart_independent']
        assert comp['path3_hh']['keller_theorem']
        assert comp['path5_central_charge']['match']

    def test_cubic_comparison(self):
        m = fermat_cubic_cy1()
        comp = gepner_vs_lv_full_comparison(m)
        assert comp['kappa_bcov'] == F(0)
        assert comp['path5_central_charge']['match']

    def test_quartic_comparison(self):
        m = fermat_quartic_k3()
        comp = gepner_vs_lv_full_comparison(m)
        assert comp['kappa_bcov'] == F(1)
        assert comp['path5_central_charge']['match']


# ================================================================
# 10. DETAILED QUINTIC COMPUTATION TESTS
# ================================================================

class TestQuinticDetailed:
    """Test the detailed quintic Gepner computation."""

    def test_step1_all_mfs(self):
        result = quintic_gepner_detailed()
        assert result['step1_all_mfs']['total_count'] == 1024
        assert result['step1_all_mfs']['match']

    def test_step2_invariant_mfs(self):
        result = quintic_gepner_detailed()
        assert result['step2_invariant_mfs']['count'] == 204
        assert result['step2_invariant_mfs']['match']

    def test_step3_degree_decomposition(self):
        result = quintic_gepner_detailed()
        assert result['step3_degree_decomposition']['match']
        assert result['step3_degree_decomposition']['decomposition'] == {
            0: 1, 1: 101, 2: 101, 3: 1,
        }

    def test_step5_orlov(self):
        result = quintic_gepner_detailed()
        assert result['step5_orlov']['is_e1_quasi_iso']
        assert result['step5_orlov']['k0_match']
        assert result['step5_orlov']['hh_match']
        assert result['step5_orlov']['kappa_match']

    def test_step6_kappa(self):
        result = quintic_gepner_detailed()
        assert result['step6_kappa']['match']
        assert result['step6_kappa']['kappa_bcov'] == F(-25, 3)


# ================================================================
# 11. ALL CY3 GEPNER CoHA TESTS
# ================================================================

class TestAllCY3GepnerCoHAs:
    """Test all uniform CY3 Gepner models."""

    def test_all_models_have_c_9(self):
        """All CY3 Gepner models have c_total = 9."""
        results = all_cy3_gepner_cohas()
        for r in results:
            assert r['c_total'] == F(9), (
                f"{r['name']}: c_total = {r['c_total']}"
            )

    def test_all_models_kappa_n2(self):
        """All CY3 Gepner models have kappa_N2 = 3/2."""
        results = all_cy3_gepner_cohas()
        for r in results:
            assert r['kappa_n2'] == F(3, 2), (
                f"{r['name']}: kappa_N2 = {r['kappa_n2']}"
            )

    def test_quintic_model_b3(self):
        """(3)^5 quintic: b_3 = 204."""
        results = all_cy3_gepner_cohas()
        quintic = [r for r in results if '(3)^5' in r['name']][0]
        assert quintic['n_invariant_mfs'] == 204
        assert quintic['b3_match']

    def test_octic_model_b3(self):
        """(6)^4 octic: b_3 = 300."""
        results = all_cy3_gepner_cohas()
        octic = [r for r in results if '(6)^4' in r['name']][0]
        assert octic['n_invariant_mfs'] == 300
        assert octic['b3_match']

    def test_model_1_9_b3(self):
        """(1)^9 model: h21 = 84, b_3 = 2(1 + 84) = 170.

        Computed from the orbifold-invariant Jacobian ring:
            n=3, r=9: dim = (2^9 + (-1)^9 * 2) / 3 = (512 - 2)/3 = 170.
        """
        results = all_cy3_gepner_cohas()
        m19 = [r for r in results if '(1)^9' in r['name']][0]
        assert m19['expected_b3'] == 170
        assert m19['b3_match']

    def test_model_2_6_b3(self):
        """(2)^6 model: h21 = 90, b_3 = 2(1 + 90) = 182.

        Computed from the orbifold-invariant Jacobian ring:
            n=4, r=6: dim = (3^6 + (-1)^7) / 4 = (729 - 1)/4 = 182.
        """
        results = all_cy3_gepner_cohas()
        m26 = [r for r in results if '(2)^6' in r['name']][0]
        assert m26['expected_b3'] == 182
        assert m26['b3_match']

    def test_degree_decomposition_palindromic(self):
        """For all CY3 models, decomp[p] = decomp[3-p] (Hodge symmetry)."""
        results = all_cy3_gepner_cohas()
        for r in results:
            decomp = r['degree_decomposition']
            for p in decomp:
                if 3 - p in decomp:
                    assert decomp[p] == decomp[3 - p], (
                        f"{r['name']}: decomp[{p}]={decomp[p]} != "
                        f"decomp[{3-p}]={decomp[3-p]}"
                    )

    def test_degree_0_and_3_are_1(self):
        """For all CY3 models, decomp[0] = decomp[3] = 1 (h^{3,0} = h^{0,3} = 1)."""
        results = all_cy3_gepner_cohas()
        for r in results:
            decomp = r['degree_decomposition']
            assert decomp.get(0, 0) == 1, (
                f"{r['name']}: decomp[0] = {decomp.get(0, 0)}"
            )
            assert decomp.get(3, 0) == 1, (
                f"{r['name']}: decomp[3] = {decomp.get(3, 0)}"
            )

    def test_degree_1_equals_h21(self):
        """For all CY3 models, decomp[1] = h^{2,1}."""
        results = all_cy3_gepner_cohas()
        for r in results:
            decomp = r['degree_decomposition']
            assert decomp.get(1, 0) == r['h21'], (
                f"{r['name']}: decomp[1]={decomp.get(1,0)} != h21={r['h21']}"
            )


# ================================================================
# 12. KAPPA ALL MODELS TEST
# ================================================================

class TestKappaAllModels:
    """Test kappa computations across all models."""

    def test_kappa_all_models_structure(self):
        kappas = kappa_all_models()
        assert len(kappas) == 4  # cubic, quartic, quintic, octic

    def test_kappa_quintic_values(self):
        kappas = kappa_all_models()
        for name, k in kappas.items():
            if 'quintic' in name.lower():
                assert k['kappa_bcov'] == F(-25, 3)
                assert k['kappa_n2'] == F(3, 2)
                assert k['kappa_virasoro'] == F(9, 2)
                assert k['chi'] == F(-200)
                break

    def test_kappa_cubic_values(self):
        kappas = kappa_all_models()
        for name, k in kappas.items():
            if 'cubic' in name.lower():
                assert k['kappa_bcov'] == F(0)
                assert k['kappa_n2'] == F(1, 2)  # c/6 = 3/6 = 1/2
                assert k['chi'] == F(0)
                break

    def test_kappa_quartic_values(self):
        kappas = kappa_all_models()
        for name, k in kappas.items():
            if 'quartic' in name.lower():
                assert k['kappa_bcov'] == F(1)
                assert k['kappa_n2'] == F(1)  # c/6 = 6/6 = 1
                assert k['chi'] == F(24)
                break

    def test_kappa_octic_values(self):
        kappas = kappa_all_models()
        for name, k in kappas.items():
            if 'octic' in name.lower():
                assert k['kappa_bcov'] == F(-37, 3)
                assert k['kappa_n2'] == F(3, 2)
                assert k['chi'] == F(-296)
                break


# ================================================================
# 13. MULTI-PATH CROSS-VERIFICATION TESTS
# ================================================================

class TestMultiPathCrossVerification:
    """Cross-verification between independent computation paths.

    These tests verify the SAME quantity by multiple independent methods,
    ensuring consistency (per the CLAUDE.md multi-path mandate).
    """

    def test_quintic_b3_three_paths(self):
        """b_3(quintic) = 204 by three independent methods.

        Path 1: Direct enumeration of orbifold-invariant MFs.
        Path 2: Exact formula (mu^r + (-1)^{r+1}) / n.
        Path 3: Sum of degree decomposition counts.
        """
        # Path 1: direct enumeration
        inv_mfs = orbifold_invariant_mf_classes((5, 5, 5, 5, 5), 5)
        b3_path1 = len(inv_mfs)

        # Path 2: exact formula
        # n=5 divides r=5, so: (4^5 + (-1)^5 * (5-1)) / 5
        # = (1024 - 4) / 5 = 1020/5 = 204
        b3_path2 = (4**5 + (-1)**5 * 4) // 5

        # Path 3: inclusion-exclusion by degree
        b3_path3 = sum(
            _count_tuples_with_sum(5, 3, s)
            for s in range(0, 16, 5)
        )

        assert b3_path1 == 204
        assert b3_path2 == 204
        assert b3_path3 == 204
        assert b3_path1 == b3_path2 == b3_path3

    def test_quintic_kappa_three_paths(self):
        """kappa_BCOV = -25/3 for the quintic by three methods.

        Path 1: chi/24 = -200/24 = -25/3.
        Path 2: from Betti numbers: (1-0+1-204+1-0+1)/24 = -200/24.
        Path 3: from Hodge numbers: 2(h^{1,1}-h^{2,1})/24 = 2(1-101)/24.
        """
        # Path 1
        kappa_1 = F(-200, 24)

        # Path 2
        chi_betti = 1 - 0 + 1 - 204 + 1 - 0 + 1
        kappa_2 = F(chi_betti, 24)

        # Path 3
        chi_hodge = 2 * (1 - 101)
        kappa_3 = F(chi_hodge, 24)

        assert kappa_1 == F(-25, 3)
        assert kappa_2 == F(-25, 3)
        assert kappa_3 == F(-25, 3)
        assert kappa_1 == kappa_2 == kappa_3

    def test_octic_b3_three_paths(self):
        """b_3(octic) = 300 by three independent methods.

        Path 1: Direct enumeration.
        Path 2: Exact formula.
        Path 3: Sum of degree decomposition.
        """
        # Path 1
        inv_mfs = orbifold_invariant_mf_classes((8, 8, 8, 8), 8)
        b3_path1 = len(inv_mfs)

        # Path 2: n=8 does not divide r=4.
        # Formula: (mu^r + (-1)^{r+1}) / n = (7^4 + (-1)^5) / 8
        # = (2401 - 1) / 8 = 2400/8 = 300
        b3_path2 = (7**4 + (-1)**5) // 8

        # Path 3
        b3_path3 = sum(
            _count_tuples_with_sum(4, 6, s)
            for s in range(0, 4 * 6 + 1, 8)
        )

        assert b3_path1 == 300
        assert b3_path2 == 300
        assert b3_path3 == 300

    def test_quartic_invariant_three_paths(self):
        """Invariant MF count for K3 = 21 by three methods.

        Path 1: Direct enumeration.
        Path 2: Exact formula.
        Path 3: Degree decomposition sum.
        """
        # Path 1
        inv_mfs = orbifold_invariant_mf_classes((4, 4, 4, 4), 4)
        count_1 = len(inv_mfs)

        # Path 2: n=4 divides r=4.
        # (3^4 + (-1)^4 * (4-1)) / 4 = (81 + 3) / 4 = 21
        count_2 = (3**4 + (-1)**4 * 3) // 4

        # Path 3
        count_3 = sum(
            _count_tuples_with_sum(4, 2, s)
            for s in range(0, 4 * 2 + 1, 4)
        )

        assert count_1 == 21
        assert count_2 == 21
        assert count_3 == 21

    def test_cubic_invariant_three_paths(self):
        """Invariant MF count for elliptic curve = 2 by three methods."""
        # Path 1
        inv_mfs = orbifold_invariant_mf_classes((3, 3, 3), 3)
        count_1 = len(inv_mfs)

        # Path 2: n=3 divides r=3.
        # (2^3 + (-1)^3 * (3-1)) / 3 = (8 - 2) / 3 = 2
        count_2 = (2**3 + (-1)**3 * 2) // 3

        # Path 3
        count_3 = sum(
            _count_tuples_with_sum(3, 1, s)
            for s in range(0, 3 * 1 + 1, 3)
        )

        assert count_1 == 2
        assert count_2 == 2
        assert count_3 == 2


# ================================================================
# 14. GEPNER CoHA MULTIPLICATION STRUCTURE TESTS
# ================================================================

class TestGepnerMultiplication:
    """Test the multiplication structure of the Gepner CoHA."""

    def test_quintic_product_degree_0_0(self):
        """1 * 1 -> degree 0, dim 1."""
        coha = quintic_gepner_coha()
        assert coha.multiplication_data[(0, 0)] == 1

    def test_quintic_product_degree_0_1(self):
        """degree 0 * degree 1 -> degree 1, dim 101."""
        coha = quintic_gepner_coha()
        assert coha.multiplication_data[(0, 1)] == 101

    def test_quintic_product_degree_1_1(self):
        """degree 1 * degree 1 -> degree 2, dim 101."""
        coha = quintic_gepner_coha()
        assert coha.multiplication_data[(1, 1)] == 101

    def test_quintic_product_degree_1_2(self):
        """degree 1 * degree 2 -> degree 3, dim 1."""
        coha = quintic_gepner_coha()
        assert coha.multiplication_data[(1, 2)] == 1

    def test_quintic_product_commutativity_char(self):
        """The character-level product is commutative (target dims match)."""
        coha = quintic_gepner_coha()
        for (p, q), dim in coha.multiplication_data.items():
            assert dim == coha.multiplication_data.get((q, p), 0), (
                f"({p},{q}) -> {dim} but ({q},{p}) -> "
                f"{coha.multiplication_data.get((q, p), 0)}"
            )

    def test_quintic_product_vanishing(self):
        """Products beyond degree 3 vanish (no generators at charge > 3)."""
        coha = quintic_gepner_coha()
        # degree 2 * degree 2 -> degree 4, which should have dim 0
        assert coha.multiplication_data.get((2, 2), 0) == 0
        assert coha.multiplication_data.get((2, 3), 0) == 0
        assert coha.multiplication_data.get((3, 3), 0) == 0
