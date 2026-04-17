"""Tests for compact_geometric_koszul_d3.py: compact CY-B at d=3 via PTVV
+ Kapranov 3-shifted symplectic, quintic case.

Claims tested:
  1. HKR-matching theorem (PROVED necessary condition):
       dim HH_q(QCoh(T^*[-3] X_5)) = dim HH_q(X_5) = (1, 0, 101, 4, 101, 0, 1).
  2. PTVV (-3)-shifted symplectic existence on Perf(X_5).
  3. The implication "HKR matching => chain-level Koszul" is FALSE.
  4. Tilting-complex obstruction documented (BCOV / LG / Bridgeland routes
     all OPEN for compact quintic).
  5. Conductor consistency with prior wave: K(X_5) = -50/3, K(check X_5) = 50/3.

Independent verification path (decorator on the load-bearing claim):
  - DERIVATION: HKR isomorphism on D^b(Coh(X_5)) via Caldararu polyvector
    formula plus PTVV shifted symplectic structure on Perf(X_5).
  - VERIFICATION: classical Voisin Hodge theory of the quintic threefold
    (Lefschetz hyperplane, Griffiths transversality on the Jacobian ring),
    which computes the Hodge diamond (h^{1,1}=1, h^{2,1}=101) PURELY
    topologically, predating any HKR or PTVV machinery.

  These are independent: HKR/PTVV use dg-categorical / shifted-symplectic
  geometry; Voisin Hodge theory is purely classical algebraic geometry
  via Hodge filtration on hypersurfaces.

Inscription targets:
  - chapters/theory/e2_chiral_algebras.tex:
        thm:hkr-matching-predictor-quintic (NEW, PROVED)
        thm:ptvv-quintic (NEW, PROVED)
        rem:hkr-matching-not-koszul-duality (NEW, REFUTATION)
        rem:tilting-complex-obstruction-quintic (NEW, OPEN)
  - notes/wave_compact_CY_B_d3_quintic.md (full wave note)
"""

import pytest
from fractions import Fraction

from compute.lib.independent_verification import independent_verification

from compute.lib.compact_geometric_koszul_d3 import (
    QUINTIC_HODGE,
    hodge_diamond_quintic,
    hodge_sum_quintic,
    betti_numbers_quintic,
    euler_char_quintic,
    hh_homology_dimensions_quintic,
    hh_homology_total_quintic,
    hh_cohomology_dimensions_quintic,
    verdier_duality_check_quintic,
    hh_homology_dimensions_shifted_cotangent_quintic,
    hkr_matching_theorem_quintic,
    ptvv_quintic_existence,
    serre_pairing_degree_check,
    hkr_matching_implication_refutation,
    tilting_complex_obstruction_routes,
    quintic_conductor,
    mirror_quintic_conductor,
    conductor_sum_quintic_pair,
    verify_all,
)


# =========================================================================
# 1. Hodge diamond of the quintic
# =========================================================================

class TestQuinticHodgeDiamond:
    """Verify the Hodge diamond against classical Voisin computation."""

    def test_h11_quintic(self):
        """h^{1,1}(X_5) = 1 (Lefschetz on the hyperplane)."""
        assert QUINTIC_HODGE[(1, 1)] == 1

    def test_h21_quintic(self):
        """h^{2,1}(X_5) = 101 (Voisin: h^0(O(5)) - 25 = 126 - 25)."""
        assert QUINTIC_HODGE[(2, 1)] == 101

    def test_h12_quintic_symmetry(self):
        """Hodge symmetry h^{1,2} = h^{2,1} = 101."""
        assert QUINTIC_HODGE[(1, 2)] == QUINTIC_HODGE[(2, 1)]

    def test_corners(self):
        """Four corners h^{0,0}, h^{0,3}, h^{3,0}, h^{3,3} all equal 1."""
        for (p, q) in [(0, 0), (0, 3), (3, 0), (3, 3)]:
            assert QUINTIC_HODGE[(p, q)] == 1

    def test_h22(self):
        """h^{2,2} = h^{1,1} = 1 (CY_3 hard Lefschetz)."""
        assert QUINTIC_HODGE[(2, 2)] == 1

    def test_off_diagonal_zeros(self):
        """h^{p,0} = h^{0,p} = 0 for p in {1, 2} on CY_3 (Bogomolov-Tian-Todorov)."""
        for (p, q) in [(0, 1), (0, 2), (1, 0), (2, 0), (1, 3), (3, 1), (2, 3), (3, 2)]:
            assert QUINTIC_HODGE[(p, q)] == 0

    def test_hodge_sum_total(self):
        """Total Hodge sum = 4 corners + 2 middle diagonal + 202 off-diagonal = 208."""
        assert hodge_sum_quintic() == 208

    def test_betti_numbers(self):
        """Betti numbers of X_5 from Hodge: (1, 0, 1, 204, 1, 0, 1).

        b_3 = 2(h^{2,1} + h^{0,3}) = 2(101 + 1) = 204.
        Wait: b_3 = h^{0,3} + h^{1,2} + h^{2,1} + h^{3,0} = 1 + 101 + 101 + 1 = 204.
        """
        betti = betti_numbers_quintic()
        assert betti == [1, 0, 1, 204, 1, 0, 1]

    def test_euler_char_quintic(self):
        """chi_top(X_5) = sum (-1)^n b_n = 1 - 0 + 1 - 204 + 1 - 0 + 1 = -200."""
        assert euler_char_quintic() == -200


# =========================================================================
# 2. HKR Hochschild homology of the quintic
# =========================================================================

class TestQuinticHKR:
    """Verify HKR Hochschild homology dimensions of X_5."""

    @independent_verification(
        claim="thm:hkr-matching-predictor-quintic",
        derived_from=[
            "Caldararu HKR isomorphism on D^b(Coh(X_5)) via polyvector cohomology (Caldararu 2003, arXiv:math/0308080), the manuscript's chosen tool",
            "PTVV (-3)-shifted symplectic structure on Perf(X_5) (Pantev-Toen-Vaquie-Vezzosi 2013), the manuscript's chosen geometric input",
        ],
        verified_against=[
            "Voisin Hodge theory and complex algebraic geometry II (Cambridge 2003), classical Hodge diamond of the quintic via Lefschetz hyperplane theorem and Griffiths transversality on the Jacobian ring, with NO HKR or PTVV input",
            "Classical Betti numbers of the quintic from singular cohomology with rational coefficients, predating any dg-categorical machinery (1950s-era Lefschetz computation)",
        ],
        disjoint_rationale=(
            "The DERIVATION uses Caldararu HKR (polyvector cohomology of the "
            "tangent complex) and PTVV (-3)-shifted symplectic on Perf(X_5) "
            "to compute Hochschild homology dimensions for both X_5 and "
            "QCoh(T^*[-3] X_5). The VERIFICATION uses Voisin's classical "
            "Hodge diamond computation for the quintic threefold (h^{1,1}=1 "
            "from Lefschetz, h^{2,1}=101 from Griffiths/Jacobian ring) and "
            "the classical Betti number b_3 = 204 from singular cohomology. "
            "Neither verification source uses HKR or PTVV; both reach the "
            "Hodge values through purely classical algebraic geometry. The "
            "matching dimension vector (1, 0, 101, 4, 101, 0, 1) is computed "
            "from Voisin Hodge data via anti-diagonal sums (no HKR), and "
            "this serves as the independent check on the HKR-derived "
            "claim."
        ),
    )
    def test_hh_homology_dim_vector(self):
        """dim HH_q(X_5) for q = -3..3 is (1, 0, 101, 4, 101, 0, 1)."""
        dims = hh_homology_dimensions_quintic()
        assert dims == [1, 0, 101, 4, 101, 0, 1]

    def test_hh_homology_total(self):
        """sum_q dim HH_q(X_5) = 208 (= sum_{p,q} h^{p,q})."""
        assert hh_homology_total_quintic() == 208

    def test_hh_cohomology_dim_vector(self):
        """dim HH^n(X_5) for n = 0..6 is (1, 0, 101, 4, 101, 0, 1).

        Same vector as homology, shifted by 3 (Verdier duality on CY_3).
        """
        dims = hh_cohomology_dimensions_quintic()
        assert dims == [1, 0, 101, 4, 101, 0, 1]

    def test_verdier_duality_quintic(self):
        """HH^n(X_5) and HH_{n-3}(X_5) have matching dimension vectors."""
        check = verdier_duality_check_quintic()
        assert check['agree_under_3_shift'] is True

    def test_hh_neg3_quintic(self):
        """HH_{-3}(X_5) = h^{3,0}(X_5) = 1 (the holomorphic 3-form)."""
        dims = hh_homology_dimensions_quintic()
        assert dims[0] == 1  # index 0 corresponds to q = -3

    def test_hh_neg1_quintic(self):
        """HH_{-1}(X_5) = h^{2,1}(X_5) = 101 (deformation count)."""
        dims = hh_homology_dimensions_quintic()
        assert dims[2] == 101  # index 2 corresponds to q = -1

    def test_hh_zero_quintic(self):
        """HH_0(X_5) = 4 = h^{0,0}+h^{1,1}+h^{2,2}+h^{3,3}."""
        dims = hh_homology_dimensions_quintic()
        assert dims[3] == 4  # index 3 corresponds to q = 0


# =========================================================================
# 3. HKR matching: the necessary-condition theorem
# =========================================================================

class TestHKRMatchingTheorem:
    """Verify the HKR-matching predictor for QCoh(T^*[-3] X_5)."""

    def test_shifted_cotangent_dims_match_quintic(self):
        """dim HH_q(QCoh(T^*[-3] X_5)) = dim HH_q(X_5) for all q."""
        match = hkr_matching_theorem_quintic()
        assert match['dimensions_match'] is True

    def test_shifted_cotangent_total_matches(self):
        """Total HH_* dimension matches: 208 = 208."""
        match = hkr_matching_theorem_quintic()
        assert match['totals_match'] is True

    def test_match_against_expected_vector(self):
        """The matched vector is (1, 0, 101, 4, 101, 0, 1)."""
        match = hkr_matching_theorem_quintic()
        assert match['HH_dims_quintic'] == [1, 0, 101, 4, 101, 0, 1]
        assert match['HH_dims_shifted_cotangent'] == [1, 0, 101, 4, 101, 0, 1]

    def test_match_total_is_208(self):
        """Total HH_*(X_5) = 208."""
        match = hkr_matching_theorem_quintic()
        assert match['total_quintic'] == 208

    def test_match_status_proved(self):
        """The HKR-matching theorem is PROVED as a necessary condition."""
        match = hkr_matching_theorem_quintic()
        assert 'PROVED' in match['status']

    def test_match_status_sufficiency_refuted(self):
        """The status acknowledges sufficiency is REFUTED separately."""
        match = hkr_matching_theorem_quintic()
        assert 'sufficiency REFUTED' in match['status']


# =========================================================================
# 4. PTVV (-3)-shifted symplectic existence
# =========================================================================

class TestPTVVQuinticExistence:
    """Verify PTVV (-3)-shifted symplectic on Perf(X_5) exists."""

    def test_ptvv_shift_degree(self):
        """PTVV form on Perf(X_5) is (-3)-shifted (CY_3 standard)."""
        ptvv = ptvv_quintic_existence()
        assert ptvv['shift_degree'] == -3

    def test_ptvv_underlying_stack(self):
        """The form lives on Perf(X_5)."""
        ptvv = ptvv_quintic_existence()
        assert ptvv['underlying_stack'] == 'Perf(X_5)'

    def test_ptvv_tangent_complex(self):
        """Tangent complex at E in Perf(X_5) is RHom(E, E)[1]."""
        ptvv = ptvv_quintic_existence()
        assert 'RHom(E, E)[1]' in ptvv['tangent_complex_at_E']

    def test_ptvv_form_formula(self):
        """The form is the Serre-trace pairing: int Tr(alpha smile beta) Omega."""
        ptvv = ptvv_quintic_existence()
        assert 'int_{X_5} Tr' in ptvv['form_formula']
        assert 'Omega_{X_5}' in ptvv['form_formula']

    def test_ptvv_trivialisation(self):
        """The CY_3 trivialisation K_{X_5} ~ O is named."""
        ptvv = ptvv_quintic_existence()
        assert 'K_{X_5}' in ptvv['omega_X5_trivialisation']

    def test_ptvv_existence_unconditional(self):
        """PTVV existence is unconditional (PTVV 2013 Theorem 2.5)."""
        ptvv = ptvv_quintic_existence()
        assert ptvv['existence_unconditional'] is True

    def test_serre_pairing_degree(self):
        """Serre pairing has degree sum 3 (CY_3 standard)."""
        sp = serre_pairing_degree_check()
        assert sp['pairing_degree_sum'] == 3

    def test_serre_pairing_target_h03(self):
        """Trace target is H^3(X_5, O), which has dim h^{0,3}(X_5) = 1."""
        sp = serre_pairing_degree_check()
        assert sp['h_03_quintic'] == 1
        assert sp['trace_dim'] == 1

    def test_serre_duality_holds(self):
        """Serre duality on X_5 gives the non-degenerate pairing."""
        sp = serre_pairing_degree_check()
        assert sp['serre_duality_holds'] is True


# =========================================================================
# 5. The REFUTED implication: HKR matching is not sufficient
# =========================================================================

class TestImplicationRefutation:
    """Verify the implication "HKR match => Koszul" is FALSE."""

    def test_implication_truth_value_false(self):
        """The brief's predictor "HKR matching => Koszul" is FALSE."""
        ref = hkr_matching_implication_refutation()
        assert ref['implication_truth_value'] is False

    def test_necessary_condition_proved(self):
        """The HKR-matching is PROVED as a necessary condition."""
        ref = hkr_matching_implication_refutation()
        assert ref['necessary_condition_proved'] is True

    def test_sufficient_condition_open(self):
        """The chain-level Koszul-dual identification remains OPEN."""
        ref = hkr_matching_implication_refutation()
        assert ref['sufficient_condition_status'] == 'OPEN'

    def test_genuine_obstruction_named(self):
        """The genuine obstruction is the tilting complex E_{X_5}."""
        ref = hkr_matching_implication_refutation()
        assert 'tilting complex' in ref['genuine_obstruction']

    def test_bondal_orlov_obstruction(self):
        """Bondal-Orlov: compact CY has no exceptional collection."""
        ref = hkr_matching_implication_refutation()
        assert 'Compact CY' in ref['bondal_orlov_obstruction']
        assert 'exceptional collection' in ref['bondal_orlov_obstruction']

    def test_manuscript_status_unchanged(self):
        """The conjecture remains CONJECTURAL (no upgrade)."""
        ref = hkr_matching_implication_refutation()
        assert 'NONE' in ref['manuscript_status_change']
        assert 'CONJECTURAL' in ref['manuscript_status_change']


class TestTiltingComplexRoutes:
    """Verify the three documented obstruction routes are all OPEN."""

    def test_route_BCOV_open(self):
        """BCOV wave-function quantization route is OPEN."""
        routes = tilting_complex_obstruction_routes()
        assert 'OPEN' in routes['route_BCOV']['status']

    def test_route_LG_mirror_open(self):
        """LG mirror route is OPEN (HMS gives equivalence, not Koszul)."""
        routes = tilting_complex_obstruction_routes()
        assert 'OPEN' in routes['route_LG_mirror']['status']

    def test_route_Bridgeland_open(self):
        """Bridgeland stability tilting route is OPEN."""
        routes = tilting_complex_obstruction_routes()
        assert 'OPEN' in routes['route_Bridgeland_stability']['status']

    def test_route_BCOV_reference(self):
        """BCOV route cites Bershadsky-Cecotti-Ooguri-Vafa 1993."""
        routes = tilting_complex_obstruction_routes()
        assert 'Bershadsky' in routes['route_BCOV']['reference']

    def test_route_LG_mirror_reference(self):
        """LG mirror route cites Sheridan 2015."""
        routes = tilting_complex_obstruction_routes()
        assert 'Sheridan' in routes['route_LG_mirror']['reference']

    def test_route_Bridgeland_reference(self):
        """Bridgeland route cites Bridgeland 2007."""
        routes = tilting_complex_obstruction_routes()
        assert 'Bridgeland 2007' in routes['route_Bridgeland_stability']['reference']

    def test_three_routes_present(self):
        """Exactly three candidate routes are documented."""
        routes = tilting_complex_obstruction_routes()
        assert len(routes) == 3


# =========================================================================
# 6. Conductor consistency
# =========================================================================

class TestConductor:
    """Verify K(X_5) and the conductor sum vanish (consistency with prior wave)."""

    def test_quintic_K_value(self):
        """K(X_5) = chi_top/12 = -200/12 = -50/3."""
        assert quintic_conductor() == Fraction(-50, 3)

    def test_mirror_quintic_K_value(self):
        """K(check X_5) = +50/3 (Hodge-mirror swap)."""
        assert mirror_quintic_conductor() == Fraction(50, 3)

    def test_conductor_sum_zero(self):
        """K(X_5) + K(check X_5) = 0 (free-field class)."""
        assert conductor_sum_quintic_pair() == Fraction(0)


# =========================================================================
# 7. Cross-engine consistency with geometric_koszul_dual_d3.py
# =========================================================================

class TestCrossEngineConsistency:
    """Verify consistency with the prior engine geometric_koszul_dual_d3.py."""

    def test_quintic_K_matches_prior_engine(self):
        """K(X_5) here matches QUINTIC.koszul_conductor() in prior engine."""
        from compute.lib.geometric_koszul_dual_d3 import QUINTIC
        assert quintic_conductor() == QUINTIC.koszul_conductor()

    def test_mirror_quintic_K_matches_prior_engine(self):
        """K(check X_5) here matches the prior MIRROR_QUINTIC."""
        from compute.lib.geometric_koszul_dual_d3 import MIRROR_QUINTIC
        assert mirror_quintic_conductor() == MIRROR_QUINTIC.koszul_conductor()

    def test_conductor_sum_consistent(self):
        """The conductor sum vanishes in both engines."""
        from compute.lib.geometric_koszul_dual_d3 import (
            QUINTIC, conductor_coincidence,
        )
        prior_sum = conductor_coincidence(QUINTIC)['sum']
        here_sum = conductor_sum_quintic_pair()
        assert prior_sum == here_sum


# =========================================================================
# 8. Full verification entry point
# =========================================================================

class TestVerifyAll:
    """Smoke-test the full summary."""

    def test_verify_all_runs(self):
        """The full verification runs without error."""
        r = verify_all()
        assert isinstance(r, dict)

    def test_verify_all_quintic_chi_top(self):
        """quintic chi_top = -200 surfaces in summary."""
        r = verify_all()
        assert r['quintic_chi_top'] == -200

    def test_verify_all_HH_dims(self):
        """The HH dimension vector (1, 0, 101, 4, 101, 0, 1) surfaces."""
        r = verify_all()
        assert r['quintic_HH_dims'] == [1, 0, 101, 4, 101, 0, 1]

    def test_verify_all_hkr_matching(self):
        """The HKR matching theorem is verified."""
        r = verify_all()
        assert r['hkr_matching']['dimensions_match'] is True

    def test_verify_all_PTVV_existence(self):
        """The PTVV existence theorem is reported."""
        r = verify_all()
        assert r['ptvv_existence']['existence_unconditional'] is True

    def test_verify_all_implication_refuted(self):
        """The implication "HKR => Koszul" is REFUTED."""
        r = verify_all()
        assert r['implication_refutation']['implication_truth_value'] is False

    def test_verify_all_three_open_routes(self):
        """Three candidate routes are reported, all OPEN."""
        r = verify_all()
        assert len(r['tilting_routes']) == 3
        for route in r['tilting_routes'].values():
            assert 'OPEN' in route['status']

    def test_verify_all_conductor_zero(self):
        """K(X_5) + K(mirror X_5) = 0 surfaces in summary."""
        r = verify_all()
        assert r['conductor_sum'] == Fraction(0)
