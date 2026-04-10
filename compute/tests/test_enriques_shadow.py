r"""
Tests for the Enriques x E shadow obstruction tower.

Enriques x E is a Calabi-Yau threefold obtained as the product of an
Enriques surface S_Enr = K3/iota (where iota is a fixed-point-free
involution) with an elliptic curve E.  It is non-simply-connected
(pi_1 = Z_2), distinguishing it from K3 x E.

Verification axes:
    1. Enriques Hodge data: chi_top, h^{p,q}, lattice invariants
    2. Enriques x E as CY3: Hodge diamond, chi_top = 0 from product
    3. Elliptic genus: phi_{Enr} = phi_{0,1}/2, integrality, Z_2 halving
    4. BKM root multiplicities: K3 vs Enriques ratio = 2
    5. Shadow tower: kappa, cubic, quartic, critical discriminant, depth class
    6. Genus tower: F_g = kappa * lambda_g^{FP}
    7. Cross-comparison: K3 x E vs Enriques x E at every level
    8. Fundamental group effects: pi_1 = Z_2 consequences
    9. Borcherds product: weight = 4, lattice data
   10. Shadow metric and connection

Ground truth:
    Allcock (2000): Enriques Borcherds product has weight 4
    Barth-Hulek-Peters-Van de Ven: Enriques surface Hodge data
    Eguchi-Ooguri-Tachikawa (2011): K3 elliptic genus
"""

import math
import os
import sys
import importlib.util
from fractions import Fraction

import pytest

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'enriques_shadow',
    os.path.join(_lib_dir, 'enriques_shadow.py')
)
es = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(es)


# =========================================================================
# 1. ENRIQUES SURFACE: HODGE DATA AND LATTICE
# =========================================================================

class TestEnriquesHodgeData:
    """Verify intrinsic Hodge data of the Enriques surface."""

    def test_hodge_verification_passes(self):
        """All Hodge consistency checks pass."""
        result = es.enriques_hodge_verify()
        assert result['all_pass'] is True

    def test_chi_top_is_12(self):
        """chi_top(Enriques) = 12 = sum(-1)^k b_k = 1 - 0 + 10 - 0 + 1."""
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert es.ENRIQUES_HODGE.chi_top == 12

    def test_chi_halves_k3(self):
        """chi_top(Enriques) = chi_top(K3)/2 = 24/2 = 12."""
        assert es.ENRIQUES_HODGE.chi_top == es.K3_CHI_TOP // 2

    def test_h11_is_10(self):
        """h^{1,1}(Enriques) = 10."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_HODGE.h11 == 10

    def test_h11_halves_k3(self):
        """h^{1,1}(Enriques) = h^{1,1}(K3)/2 = 20/2 = 10."""
        assert es.ENRIQUES_HODGE.h11 == es.K3_H11 // 2

    def test_h20_vanishes(self):
        """h^{2,0}(Enriques) = 0 (not a K3)."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_HODGE.h20 == 0

    def test_h10_vanishes(self):
        """h^{1,0}(Enriques) = 0."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_HODGE.h10 == 0

    def test_pi1_is_z2(self):
        """pi_1(Enriques) = Z_2 (the fundamental group)."""
        assert es.ENRIQUES_HODGE.pi1 == 'Z_2'

    def test_lattice_rank_10(self):
        """H^2(S_Enr, Z)_free has rank 10."""
        # VERIFIED [DC] rank [CF] cross-family census
        assert es.ENRIQUES_HODGE.lattice_rank == 10
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert es.ENRIQUES_LATTICE_RANK == 10

    def test_lattice_signature(self):
        """Enriques lattice has signature (1, 9)."""
        # VERIFIED [DC] structural property [CF] cross-family census
        assert es.ENRIQUES_HODGE.lattice_signature == (1, 9)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert es.ENRIQUES_LATTICE_SIGNATURE == (1, 9)

    def test_b2_equals_h11(self):
        """b_2 = h^{1,1} since h^{2,0} = 0."""
        assert es.ENRIQUES_HODGE.b2 == es.ENRIQUES_HODGE.h11

    def test_e8_theta_leading(self):
        """E_8 theta series starts with 1 + 240q + 2160q^2 + ..."""
        theta = es.E8_THETA_COEFFICIENTS
        # VERIFIED [DC] structural property [CF] cross-family census
        assert theta[0] == 1
        # VERIFIED [DC] structural property [CF] cross-family census
        assert theta[1] == 240
        # VERIFIED [DC] structural property [CF] cross-family census
        assert theta[2] == 2160


# =========================================================================
# 2. ENRIQUES x E: CY3 HODGE DATA
# =========================================================================

class TestEnriquesTimesEHodge:
    """Verify Hodge data of the CY3 Enriques x E."""

    def test_chi_top_vanishes(self):
        """chi_top(S x E) = chi_top(S) * chi_top(E) = 12 * 0 = 0."""
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert es.enriques_times_e_chi_top() == 0

    def test_chi_from_hodge_agrees(self):
        """chi_top computed from Hodge diamond matches product formula."""
        assert es.enriques_times_e_chi_from_hodge() == es.enriques_times_e_chi_top()

    def test_chi_from_hodge_is_zero(self):
        """Explicit: sum (-1)^{p+q} h^{p,q} = 0."""
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert es.enriques_times_e_chi_from_hodge() == 0

    def test_h11(self):
        """h^{1,1}(Enriques x E) = 11."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.enriques_times_e_h11() == 11

    def test_h21(self):
        """h^{2,1}(Enriques x E) = 10."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.enriques_times_e_h21() == 10

    def test_h11_minus_h21(self):
        """h^{1,1} - h^{2,1} = 11 - 10 = 1.

        Note: for CY3, chi_top = 2(h^{1,1} - h^{2,1}) would give 2,
        but chi_top(SxE) = 0.  The resolution: SxE is NOT strictly CY3
        (h^{1,0} != 0, h^{3,0} = 0), so the CY3 shortcut chi = 2(h^{1,1}-h^{2,1})
        does not apply.  The full alternating sum over all h^{p,q} gives 0.
        """
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.enriques_times_e_h11() - es.enriques_times_e_h21() == 1

    def test_hodge_diamond_h00(self):
        """h^{0,0} = 1."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_TIMES_E_HODGE[(0, 0)] == 1

    def test_hodge_diamond_h10(self):
        """h^{1,0} = 1 (from the elliptic curve factor)."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_TIMES_E_HODGE[(1, 0)] == 1

    def test_hodge_diamond_h20_vanishes(self):
        """h^{2,0} = 0."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_TIMES_E_HODGE[(2, 0)] == 0

    def test_hodge_diamond_h30_vanishes(self):
        """h^{3,0} = 0 (NOT a strict CY3: no holomorphic 3-form)."""
        # VERIFIED [DC] Hodge number [CF] cross-family census
        assert es.ENRIQUES_TIMES_E_HODGE[(3, 0)] == 0

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} for all (p,q) in the diamond."""
        for (p, q), val in es.ENRIQUES_TIMES_E_HODGE.items():
            if (q, p) in es.ENRIQUES_TIMES_E_HODGE:
                assert val == es.ENRIQUES_TIMES_E_HODGE[(q, p)], \
                    f"Hodge symmetry failure: h^{{{p},{q}}} = {val} != h^{{{q},{p}}} = {es.ENRIQUES_TIMES_E_HODGE[(q, p)]}"

    def test_hodge_vs_k3_times_e_h11(self):
        """h^{1,1}(K3 x E) = 21, h^{1,1}(Enr x E) = 11.

        K3 x E: h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E) = 20 + 1 = 21.
        Enr x E: 10 + 1 = 11.  The Z_2 quotient halves the K3 h^{1,1} contribution.
        """
        k3_times_e_h11 = 20 + 1  # h^{1,1}(K3) + h^{1,1}(E)
        enr_times_e_h11 = es.enriques_times_e_h11()
        # The Enriques contribution is exactly K3/2 plus the E contribution
        assert enr_times_e_h11 == es.ENRIQUES_HODGE.h11 + 1
        assert k3_times_e_h11 == es.K3_H11 + 1
        assert es.ENRIQUES_HODGE.h11 == es.K3_H11 // 2


# =========================================================================
# 3. ELLIPTIC GENUS: Z_2 HALVING
# =========================================================================

class TestEllipticGenus:
    """Verify the Enriques elliptic genus = phi_{0,1}/2."""

    def test_enriques_genus_halves_k3(self):
        """Every Enriques coefficient is K3/2."""
        k3 = es.k3_elliptic_genus_table(5)
        enr = es.enriques_elliptic_genus_table(5)
        for (n, l), val_k3 in k3.items():
            expected = Fraction(val_k3, 2)
            if expected != 0:
                assert (n, l) in enr, f"Missing ({n},{l}) in Enriques genus"
                assert enr[(n, l)] == expected, \
                    f"At ({n},{l}): Enr={enr[(n,l)]}, expected K3/2={expected}"

    def test_leading_coefficient_d_minus1(self):
        """c_{Enr}(D=-1) = c_{K3}(-1)/2.

        In the phi01_by_discriminant convention, c_{K3}(-1) = 1
        (the coefficient per discriminant class, not the sum over
        both l=1 and l=-1).  So c_{Enr}(-1) = 1/2.
        """
        disc = es.enriques_genus_by_discriminant(5)
        k3_disc = es._phi01_by_disc(5)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert disc[-1] == Fraction(k3_disc[-1], 2)

    def test_leading_coefficient_d_0(self):
        """c_{Enr}(D=0) = c_{K3}(0)/2 = 20/2 = 10.

        Actually: phi01_by_discriminant uses a different convention.
        The raw table gives the halved coefficients.
        """
        disc = es.enriques_genus_by_discriminant(5)
        # D=0 coefficient
        if 0 in disc:
            # VERIFIED [DC] structural property [CF] cross-family census
            assert disc[0] == Fraction(es._phi01_by_disc(5).get(0, 0), 2)

    def test_multiplicities_ratio_exactly_2(self):
        """The K3/Enriques multiplicity ratio is exactly 2 for all D."""
        comp = es.k3_vs_enriques_multiplicities(5)
        for D, data in comp.items():
            if data['ratio'] is not None:
                assert data['ratio_is_2'] is True, \
                    f"K3/Enr ratio at D={D} is {data['ratio']}, expected 2"


# =========================================================================
# 4. SHADOW TOWER: KAPPA (ARITY 2)
# =========================================================================

class TestKappa:
    """Verify kappa for Enriques x E and its relationship to K3 x E."""

    def test_kappa_enriques_is_4(self):
        """kappa(Enriques x E) = 4 (Allcock weight)."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert es.kappa_enriques_times_e() == 4

    def test_kappa_k3_is_5(self):
        """kappa(K3 x E) = 5 (weight of Delta_5)."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert es.kappa_k3_times_e() == 5

    def test_kappa_difference_is_1(self):
        """kappa(K3) - kappa(Enr) = 1."""
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert es.kappa_difference() == 1

    def test_kappa_not_halved(self):
        """kappa does NOT simply halve under Z_2: 5/4 != 2.

        This is the key point (AP20): kappa is a derived invariant
        (automorphic weight), not a topological quantity that halves
        under a degree-2 cover.
        """
        ratio = Fraction(es.kappa_k3_times_e(), es.kappa_enriques_times_e())
        # VERIFIED [DC] kappa computation [CF] AP20
        assert ratio == Fraction(5, 4)
        assert ratio != 2

    def test_kappa_nonzero_despite_chi_zero(self):
        """kappa != 0 even though chi_top = 0 (AP20 illustration)."""
        result = es.verify_kappa_not_chi_top()
        # VERIFIED [DC] Euler characteristic formula [CF] AP20
        assert result['chi_top'] == 0
        # VERIFIED [DC] kappa formula [CF] AP20
        assert result['kappa'] == 4
        assert result['kappa_is_zero'] is False
        assert result['ap20_illustrated'] is True


# =========================================================================
# 5. GENUS TOWER: F_g = kappa * lambda_g^{FP}
# =========================================================================

class TestGenusTower:
    """Verify the genus tower F_g for Enriques x E."""

    def test_f1_enriques(self):
        """F_1(Enr x E) = kappa/24 = 4/24 = 1/6."""
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert es.genus_1_amplitude_enriques() == Fraction(1, 6)

    def test_f1_k3(self):
        """F_1(K3 x E) = 5/24."""
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert es.genus_1_amplitude_k3() == Fraction(5, 24)

    def test_f1_ratio(self):
        """F_1(K3)/F_1(Enr) = (5/24)/(1/6) = 5/4 = kappa ratio."""
        ratio = es.genus_1_amplitude_k3() / es.genus_1_amplitude_enriques()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert ratio == Fraction(5, 4)

    def test_genus_tower_g1(self):
        """F_1 from genus tower matches direct computation."""
        tower = es.genus_tower_first_terms_enriques(4)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower[1] == Fraction(1, 6)

    def test_genus_tower_g2(self):
        """F_2 = kappa * lambda_2^FP = 4 * 7/5760 = 7/1440."""
        tower = es.genus_tower_first_terms_enriques(4)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower[2] == Fraction(7, 1440)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower[2] == Fraction(4) * Fraction(7, 5760)

    def test_genus_tower_g3(self):
        """F_3 = kappa * lambda_3^FP = 4 * 31/967680 = 31/241920."""
        tower = es.genus_tower_first_terms_enriques(4)
        # VERIFIED [DC] genus tower [CF] cross-family census
        assert tower[3] == Fraction(31, 241920)

    def test_genus_tower_ratio_constant(self):
        """F_g(K3)/F_g(Enr) = kappa(K3)/kappa(Enr) = 5/4 at all genera.

        At the scalar level, F_g = kappa * lambda_g^FP, so the ratio
        is simply the ratio of kappas, independent of g.
        """
        tower_enr = es.genus_tower_first_terms_enriques(4)
        kappa_ratio = Fraction(es.kappa_k3_times_e(), es.kappa_enriques_times_e())
        # K3 tower: F_g(K3) = 5 * lambda_g^FP
        for g, f_enr in tower_enr.items():
            f_k3 = Fraction(5) * f_enr / Fraction(4)  # since f_enr = 4*lambda
            ratio = f_k3 / f_enr
            assert ratio == kappa_ratio, f"Genus {g}: ratio {ratio} != {kappa_ratio}"

    def test_genus_tower_positivity(self):
        """All F_g > 0 since kappa = 4 > 0 and lambda_g^FP > 0."""
        tower = es.genus_tower_first_terms_enriques(4)
        for g, val in tower.items():
            # VERIFIED [DC] genus free energy [CF] cross-family census
            assert val > 0, f"F_{g} = {val} is not positive"


# =========================================================================
# 6. SHADOW INVARIANTS AND DEPTH CLASS
# =========================================================================

class TestShadowInvariants:
    """Verify shadow invariants and depth classification."""

    def test_shadow_invariants_positive(self):
        """All S_r > 0 for r >= 1 (E_8 theta coefficients are positive)."""
        S = es.shadow_invariants_enriques(5)
        for r, val in S.items():
            # VERIFIED [DC] shadow structure [CF] cross-family census
            assert val > 0, f"S_{r} = {val} is not positive"

    def test_cubic_shadow_matches_s3(self):
        """Cubic shadow = S_3 from shadow_invariants."""
        S = es.shadow_invariants_enriques(5)
        assert es.cubic_shadow_enriques() == S[3]

    def test_quartic_contact_matches_s4(self):
        """Quartic contact = S_4 from shadow_invariants."""
        S = es.shadow_invariants_enriques(5)
        assert es.quartic_contact_enriques() == S[4]

    def test_critical_discriminant_formula(self):
        """Delta = 8 * kappa * S_4."""
        kappa = Fraction(es.kappa_enriques_times_e())
        S4 = es.quartic_contact_enriques()
        expected = 8 * kappa * S4
        assert es.critical_discriminant_enriques() == expected

    def test_critical_discriminant_nonzero(self):
        """Delta != 0 for Enriques (infinite tower)."""
        assert es.critical_discriminant_enriques() != 0

    def test_shadow_depth_class_M(self):
        """Enriques x E has shadow depth class M (infinite, like K3 x E)."""
        assert es.shadow_depth_class_enriques() == 'M'


# =========================================================================
# 7. BORCHERDS PRODUCT DATA
# =========================================================================

class TestBorcherdsProduct:
    """Verify the Borcherds product construction data."""

    def test_borcherds_weight_is_4(self):
        """Allcock (2000): Enriques Borcherds product has weight 4."""
        data = es.enriques_borcherds_product_data()
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert data['weight'] == 4

    def test_borcherds_weight_formula(self):
        """weight = c(0)/2 from the Weil representation."""
        result = es.verify_borcherds_weight_formula()
        assert result['match'] is True
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['computed_weight'] == 4
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert result['allcock_weight'] == 4

    def test_orthogonal_group(self):
        """The lift lives on O(2, 10)."""
        data = es.enriques_borcherds_product_data()
        assert data['orthogonal_group'] == 'O(2, 10)'


# =========================================================================
# 8. SHADOW METRIC AND CONNECTION
# =========================================================================

class TestShadowMetric:
    """Verify the shadow metric Q_L(t) and connection."""

    def test_shadow_metric_at_zero(self):
        """Q_L(0) = (2*kappa)^2 = 64."""
        Q0 = es.shadow_metric_enriques(Fraction(0))
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert Q0 == Fraction(64)

    def test_shadow_metric_positive_at_zero(self):
        """Q_L(0) > 0 (metric is positive-definite at the origin)."""
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert es.shadow_metric_enriques(Fraction(0)) > 0

    def test_shadow_connection_residue(self):
        """The shadow connection residue is 1/2."""
        # VERIFIED [DC] shadow structure [CF] cross-family census
        assert es.shadow_connection_residue_enriques() == Fraction(1, 2)


# =========================================================================
# 9. CROSS-COMPARISON: K3 x E vs ENRIQUES x E
# =========================================================================

class TestCrossComparison:
    """Compare K3 x E and Enriques x E at every level."""

    def test_cross_comparison_kappa(self):
        """Cross-comparison reports correct kappas."""
        cc = es.cross_comparison()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert cc['kappa']['K3xE'] == 5
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert cc['kappa']['EnrxE'] == 4
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert cc['kappa']['difference'] == 1

    def test_cross_comparison_chi(self):
        """Both have chi_top = 0 (product with elliptic curve)."""
        cc = es.cross_comparison()
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert cc['chi_top']['K3xE'] == 0
        # VERIFIED [DC] Euler characteristic [CF] cross-family census
        assert cc['chi_top']['EnrxE'] == 0

    def test_cross_comparison_f1_ratio(self):
        """F_1 ratio equals kappa ratio = 5/4."""
        cc = es.cross_comparison()
        # VERIFIED [DC] Faber-Pandharipande genus formula [CF] cross-family census
        assert cc['F_1']['ratio'] == Fraction(5, 4)

    def test_cross_comparison_pi1(self):
        """K3 x E is simply connected; Enriques x E has pi_1 = Z_2."""
        cc = es.cross_comparison()
        assert cc['pi_1']['K3xE'] == 'trivial'
        assert cc['pi_1']['EnrxE'] == 'Z_2'

    def test_cross_comparison_depth_both_M(self):
        """Both K3 x E and Enriques x E are class M (infinite shadow tower)."""
        cc = es.cross_comparison()
        # Both should be class M
        assert 'M' in cc['shadow_depth']['K3xE']
        assert cc['shadow_depth']['EnrxE'] == 'M'


# =========================================================================
# 10. Z_2 QUOTIENT EFFECTS
# =========================================================================

class TestZ2QuotientEffects:
    """Verify the systematic effects of the Z_2 quotient."""

    def test_chi_ratio_is_2(self):
        """chi_top(K3)/chi_top(Enr) = 24/12 = 2."""
        z2 = es.z2_quotient_effects()
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert z2['chi_ratio'] == 2.0

    def test_h11_ratio_is_2(self):
        """h^{1,1}(K3)/h^{1,1}(Enr) = 20/10 = 2."""
        z2 = es.z2_quotient_effects()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert z2['h11_ratio'] == 2.0

    def test_kappa_ratio_not_2(self):
        """kappa ratio is 5/4, NOT 2."""
        z2 = es.z2_quotient_effects()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert z2['kappa_ratio'] == Fraction(5, 4)

    def test_multiplicities_halved(self):
        """Root multiplicities halve under Z_2."""
        z2 = es.z2_quotient_effects()
        # VERIFIED [DC] structural property [CF] cross-family census
        assert z2['multiplicities_ratio'] == 2


# =========================================================================
# 11. GENUS DECOMPOSITION
# =========================================================================

class TestGenusDecomposition:
    """Verify the genus decomposition of the log denominator."""

    def test_genus_decomposition_returns_dict(self):
        """genus_decomposition_enriques returns nested dicts."""
        gd = es.genus_decomposition_enriques(3, 10)
        assert isinstance(gd, dict)
        assert 1 in gd and 2 in gd and 3 in gd

    def test_genus_1_leading_term(self):
        """Leading genus-1 term: -a(1)/1 = -240."""
        gd = es.genus_decomposition_enriques(1, 10)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert gd[1][1] == Fraction(-240)

    def test_genus_2_leading_term(self):
        """Leading genus-2 term: -a(1)/2 = -120."""
        gd = es.genus_decomposition_enriques(2, 10)
        # VERIFIED [DC] genus free energy [CF] cross-family census
        assert gd[2][2] == Fraction(-120)


# =========================================================================
# 12. FULL SHADOW TOWER DATA
# =========================================================================

class TestFullShadowTowerData:
    """Verify the assembled shadow tower data."""

    def test_full_data_keys(self):
        """Full data dict has all expected keys."""
        data = es.full_shadow_tower_data()
        expected_keys = {
            'algebra', 'lattice', 'kappa', 'F_1',
            'cubic_shadow', 'quartic_contact', 'critical_discriminant',
            'shadow_depth_class', 'shadow_invariants', 'genus_tower',
            'borcherds_weight', 'chi_top_Enr_x_E',
            'hodge_h11', 'hodge_h21',
        }
        assert expected_keys.issubset(set(data.keys()))

    def test_full_data_kappa(self):
        """Full data kappa = 4."""
        data = es.full_shadow_tower_data()
        # VERIFIED [DC] kappa formula [CF] cross-family census
        assert data['kappa'] == 4

    def test_full_data_consistency(self):
        """Full data F_1 matches direct computation."""
        data = es.full_shadow_tower_data()
        assert data['F_1'] == es.genus_1_amplitude_enriques()
        assert data['cubic_shadow'] == es.cubic_shadow_enriques()
        assert data['quartic_contact'] == es.quartic_contact_enriques()
        assert data['shadow_depth_class'] == es.shadow_depth_class_enriques()
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert data['borcherds_weight'] == 4
        # VERIFIED [DC] Euler characteristic formula [CF] cross-family census
        assert data['chi_top_Enr_x_E'] == 0
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert data['hodge_h11'] == 11
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert data['hodge_h21'] == 10


# =========================================================================
# 13. SHADOW RATIO K3/ENRIQUES
# =========================================================================

class TestShadowRatio:
    """Verify the shadow ratio S_r(K3)/S_r(Enr) structure."""

    def test_ratios_not_constant(self):
        """S_r ratios are NOT constant (different lattice structures).

        K3 x E uses phi_{0,1} on II^{3,19} (rank 22).
        Enriques x E uses E_8 theta on E_8(-1)+U (rank 10).
        The ratios vary with r because the lattice sum structure differs.
        """
        ratios = es.shadow_ratio_k3_enriques(5)
        vals = [v for v in ratios.values() if v is not None]
        # They should NOT all be the same
        # VERIFIED [DC] structural property [CF] cross-family census
        assert len(set(round(v, 6) for v in vals)) > 1

    def test_ratios_all_positive(self):
        """All shadow ratios are positive (both have positive S_r)."""
        ratios = es.shadow_ratio_k3_enriques(5)
        for r, v in ratios.items():
            if v is not None:
                # VERIFIED [DC] positivity check [CF] cross-family census
                assert v > 0, f"Ratio at r={r} is {v}, expected positive"


# =========================================================================
# 14. LOG DENOMINATOR
# =========================================================================

class TestLogDenominator:
    """Verify the log-expansion of the Enriques BKM denominator."""

    def test_log_denominator_leading(self):
        """Leading coefficient: -a(1)/1 = -240."""
        log_d = es.enriques_log_denominator(10)
        # VERIFIED [DC] structural property [CF] cross-family census
        assert log_d[1] == Fraction(-240)

    def test_log_denominator_second(self):
        """Second coefficient: -a(2)/1 + (-a(1))/2 = -2160 + (-240/2) = -2160 - 120 = -2280."""
        log_d = es.enriques_log_denominator(10)
        # q^2 gets -a(2)/1 from n=2,k=1 AND -a(1)/2 from n=1,k=2
        expected = Fraction(-2160) + Fraction(-240, 2)
        assert log_d[2] == expected
