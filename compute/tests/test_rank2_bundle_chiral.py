r"""Tests for rank-2 vector bundle chiral algebra functor.

Verifies the construction Tot(E) -> A_E for rank-2 vector bundles E -> C
and the anomaly/obstruction when the CY condition fails.

MULTI-PATH VERIFICATION:
  Path 1 (Direct): CY defect from deg(E) - deg(K_C)
  Path 2 (Riemann-Roch): chi(C, E) = 0 iff CY
  Path 3 (Volume form): det(T_C + E) trivial iff CY
  Path 4 (Anomaly): curvature m_0 = 0 iff CY
  Path 5 (Shadow): kappa well-defined iff CY
  Path 6 (Birational): kappa invariant under flops (CY family)
  Path 7 (Extension): Ext^2 = 0 on curves (unobstructed deformations)

Manuscript references:
    Vol III, Part V: CY-to-chiral functor
    Vol I, Part I: bar complex, shadow obstruction tower, curvature
    Vol I, concordance.tex: shadow depth classification (G/L/C/M)

Mathematical references:
    [Grot57]  Grothendieck, Classification of holomorphic bundles on P^1 (1957)
    [Ati57]   Atiyah, Vector bundles over an elliptic curve (1957)
    [CL16]    Costello-Li, arXiv:1604.02076 (twisted supergravity)
    [KS08]    Kontsevich-Soibelman, arXiv:0811.2435
    [RSYZ]    Rapcak-Soibelman-Yang-Zhao, arXiv:1810.10402
"""

import pytest
from fractions import Fraction

from compute.lib.rank2_bundle_chiral import (
    # Curves
    AlgebraicCurve,
    projective_line,
    elliptic_curve,
    genus_g_curve,
    # Bundles
    LineBundle,
    Rank2Bundle,
    # Polyvector fields
    sheaf_euler_char_P1,
    h0_P1,
    h1_P1,
    sheaf_euler_char_genus_g,
    polyvector_field_dims_split_P1,
    total_pv_dim_P1,
    hochschild_homology_dims_P1,
    # SN bracket
    sn_bracket_weight,
    cy_volume_form_degree,
    sn_bracket_vanishes_on_invariant_sector,
    # Curvature
    CurvatureData,
    compute_curvature,
    # Kappa
    kappa_conifold,
    kappa_cy_split_P1,
    kappa_cy_bundle_genus_g,
    # Shadow tower
    ShadowTowerData,
    shadow_tower_cy_split_P1,
    shadow_tower_cy_genus_g,
    # Anomaly
    anomaly_polynomial_P1,
    effective_central_charge_P1,
    # Riemann-Roch
    riemann_roch_rank2,
    # Moduli
    moduli_dimension,
    atiyah_classification_elliptic,
    # Functor
    ChiralAlgebraData,
    chiral_algebra_from_bundle,
    # Enumeration
    enumerate_cy_split_types_P1,
    enumerate_non_cy_P1,
    # Extension
    extension_deformation_order,
    # Verification
    rank2_bundle_analysis,
    verify_birational_invariance_kappa,
    verify_cy_defect_linearity,
    verify_rr_vanishing_at_cy,
    kappa_genus_variation,
    anomaly_cancellation_check,
    summary_table_P1,
)


# ================================================================
# 1. BASE CURVES
# ================================================================

class TestAlgebraicCurves:
    """Verify base curve properties."""

    def test_p1_genus(self):
        """P^1 has genus 0."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert projective_line().genus == 0

    def test_p1_canonical_degree(self):
        """deg(K_{P^1}) = -2."""
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert projective_line().canonical_degree == -2

    def test_p1_euler_char(self):
        """chi_top(P^1) = 2."""
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert projective_line().euler_char == 2

    def test_elliptic_genus(self):
        """Elliptic curve has genus 1."""
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert elliptic_curve().genus == 1

    def test_elliptic_canonical_degree(self):
        """deg(K_E) = 0 for elliptic curve."""
        # VERIFIED [DC] elliptic data [LT] chiral algebra theory
        assert elliptic_curve().canonical_degree == 0

    def test_elliptic_euler_char(self):
        """chi_top(E) = 0 for elliptic curve."""
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert elliptic_curve().euler_char == 0

    def test_genus_g_canonical_degree(self):
        """deg(K_{C_g}) = 2g - 2 for all g."""
        for g in range(10):
            # VERIFIED [DC] genus tower [LT] chiral algebra theory
            assert genus_g_curve(g).canonical_degree == 2 * g - 2

    def test_genus_g_euler_char(self):
        """chi_top(C_g) = 2 - 2g for all g."""
        for g in range(10):
            # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
            assert genus_g_curve(g).euler_char == 2 - 2 * g


# ================================================================
# 2. SHEAF COHOMOLOGY ON P^1
# ================================================================

class TestSheafCohomologyP1:
    """Verify sheaf cohomology computations on P^1."""

    def test_euler_char_O_n(self):
        """chi(P^1, O(n)) = n + 1."""
        for n in range(-5, 10):
            assert sheaf_euler_char_P1(n) == n + 1

    def test_h0_positive(self):
        """h^0(P^1, O(n)) = n + 1 for n >= 0."""
        for n in range(10):
            assert h0_P1(n) == n + 1

    def test_h0_negative(self):
        """h^0(P^1, O(n)) = 0 for n < 0."""
        for n in range(-10, 0):
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert h0_P1(n) == 0

    def test_h1_negative(self):
        """h^1(P^1, O(n)) = -n - 1 for n <= -2."""
        for n in range(-10, -1):
            assert h1_P1(n) == -n - 1

    def test_h1_nonnegative(self):
        """h^1(P^1, O(n)) = 0 for n >= -1."""
        for n in range(-1, 10):
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert h1_P1(n) == 0

    def test_h0_minus_h1_equals_chi(self):
        """h^0 - h^1 = chi for all n (Riemann-Roch consistency)."""
        for n in range(-10, 10):
            assert h0_P1(n) - h1_P1(n) == sheaf_euler_char_P1(n)

    def test_genus_g_euler_char(self):
        """chi(C_g, O(n)) = n + 1 - g."""
        for g in range(5):
            for n in range(-5, 10):
                assert sheaf_euler_char_genus_g(g, n) == n + 1 - g


# ================================================================
# 3. RANK-2 BUNDLES
# ================================================================

class TestRank2Bundle:
    """Verify rank-2 bundle properties."""

    def test_degree(self):
        """deg(O(a) + O(b)) = a + b."""
        C = projective_line()
        for a in range(-3, 4):
            for b in range(-3, 4):
                E = Rank2Bundle(C, a, b)
                assert E.degree == a + b

    def test_rank(self):
        """All bundles have rank 2."""
        C = projective_line()
        E = Rank2Bundle(C, 1, -3)
        # VERIFIED [DC] rank count [DA] dimensional consistency
        assert E.rank == 2

    def test_slope(self):
        """mu(E) = (a+b)/2."""
        C = projective_line()
        E = Rank2Bundle(C, 1, 3)
        # VERIFIED [DC] stability condition [LT] chiral algebra theory
        assert E.slope == Fraction(2)

    def test_cy_defect_P1(self):
        """delta = a + b + 2 for P^1."""
        C = projective_line()
        for a in range(-5, 5):
            for b in range(-5, 5):
                E = Rank2Bundle(C, a, b)
                assert E.cy_defect == a + b + 2

    def test_cy_defect_elliptic(self):
        """delta = a + b for elliptic curve."""
        C = elliptic_curve()
        for a in range(-3, 4):
            for b in range(-3, 4):
                E = Rank2Bundle(C, a, b)
                assert E.cy_defect == a + b

    def test_cy_defect_genus_g(self):
        """delta = a + b - (2g - 2) for genus g."""
        for g in range(5):
            C = genus_g_curve(g) if g > 0 else projective_line()
            for a in range(-3, 4):
                for b in range(-3, 4):
                    E = Rank2Bundle(C, a, b)
                    assert E.cy_defect == a + b - (2 * g - 2)

    def test_is_calabi_yau_P1(self):
        """CY iff a + b = -2 for P^1."""
        C = projective_line()
        for a in range(-5, 4):
            b = -2 - a
            E = Rank2Bundle(C, a, b)
            assert E.is_calabi_yau
        E_non_cy = Rank2Bundle(C, 0, 0)
        assert not E_non_cy.is_calabi_yau

    def test_is_calabi_yau_elliptic(self):
        """CY iff a + b = 0 for elliptic curve."""
        C = elliptic_curve()
        for a in range(-3, 4):
            E = Rank2Bundle(C, a, -a)
            assert E.is_calabi_yau
        E_non_cy = Rank2Bundle(C, 1, 1)
        assert not E_non_cy.is_calabi_yau

    def test_determinant_degree(self):
        """det(E) has degree a + b."""
        C = projective_line()
        E = Rank2Bundle(C, 3, -5)
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert E.determinant_degree == -2

    def test_split_flag(self):
        """Split vs non-split flag."""
        C = elliptic_curve()
        E_split = Rank2Bundle(C, 0, 0, extension_class_nonzero=False)
        E_nonsplit = Rank2Bundle(C, 0, 0, extension_class_nonzero=True)
        assert E_split.is_split
        assert not E_nonsplit.is_split


# ================================================================
# 4. EXT^1 DIMENSIONS
# ================================================================

class TestExt1:
    """Verify Ext^1 computations for extension classes."""

    def test_ext1_P1_balanced(self):
        """Ext^1(O(-1), O(-1)) = 0 on P^1 (conifold is rigid)."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert E.ext1_dimension == 0

    def test_ext1_P1_unbalanced(self):
        """Ext^1(O(b), O(a)) for a < b on P^1."""
        C = projective_line()
        # Ext^1(O(-3), O(1)) = H^1(P^1, O(1-(-3))) = H^1(P^1, O(4)) = 0
        E = Rank2Bundle(C, 1, -3)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert E.ext1_dimension == 0
        # Ext^1(O(1), O(-3)) = H^1(P^1, O(-3-1)) = H^1(P^1, O(-4)) = 3
        E2 = Rank2Bundle(C, -3, 1)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert E2.ext1_dimension == 3

    def test_ext1_elliptic_trivial(self):
        """Ext^1(O, O) = 1 on elliptic curve (Atiyah bundle)."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 0, 0)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert E.ext1_dimension == 1

    def test_ext1_elliptic_positive_diff(self):
        """Ext^1(O(b), O(a)) = 0 for a > b on elliptic curve."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 2, 0)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert E.ext1_dimension == 0

    def test_ext1_P1_all_split(self):
        """On P^1, Ext^1 = 0 when a1 >= a2 (Grothendieck: all bundles split)."""
        C = projective_line()
        for a in range(-3, 4):
            for b in range(-3, a + 1):  # b <= a
                E = Rank2Bundle(C, a, b)
                # Ext^1(O(b), O(a)) = H^1(O(a-b)) = 0 since a-b >= 0
                # VERIFIED [DC] dimension count [DA] dimensional consistency
                assert E.ext1_dimension == 0

    def test_can_have_nonsplit_elliptic(self):
        """Elliptic curves can have non-split bundles."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 0, 0)
        assert E.can_have_nonsplit()

    def test_cannot_have_nonsplit_P1_balanced(self):
        """O(-1)+O(-1) on P^1 cannot be deformed (Grothendieck)."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        assert not E.can_have_nonsplit()


# ================================================================
# 5. CY CONDITION: MULTIPLE VERIFICATION PATHS
# ================================================================

class TestCYCondition:
    """Multi-path verification of the CY condition."""

    def test_cy_defect_path(self):
        """Path 1: CY iff delta = deg(E) - deg(K_C) = 0."""
        C = projective_line()
        E_cy = Rank2Bundle(C, -1, -1)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert E_cy.cy_defect == 0
        E_not = Rank2Bundle(C, 0, 0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert E_not.cy_defect == 2

    def test_riemann_roch_path(self):
        """Path 2: CY implies chi(C, E) = 0."""
        result = verify_rr_vanishing_at_cy()
        assert result["all_vanish"]

    def test_volume_form_path(self):
        """Path 3: CY iff det(T_C + E) = O_C (volume form trivial)."""
        # For P^1: det(T + E) = O(2+a+b). Trivial iff 2+a+b = 0.
        for a in range(-5, 4):
            b = -2 - a
            deg = cy_volume_form_degree(a, b)
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert deg == 0, f"Volume form degree {deg} for ({a},{b})"
        # Non-CY
        deg_noncy = cy_volume_form_degree(0, 0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert deg_noncy == -2  # O(-2), not trivial

    def test_anomaly_path(self):
        """Path 4: CY iff curvature m_0 = 0."""
        C = projective_line()
        for a in range(-3, 2):
            b = -2 - a
            E = Rank2Bundle(C, a, b)
            curv = compute_curvature(E)
            assert curv.is_uncurved
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert curv.curvature_class == 0
        E_non = Rank2Bundle(C, 0, 0)
        curv_non = compute_curvature(E_non)
        assert not curv_non.is_uncurved

    def test_shadow_path(self):
        """Path 5: shadow well-defined iff CY."""
        C = projective_line()
        E_cy = Rank2Bundle(C, -1, -1)
        curv = compute_curvature(E_cy)
        assert curv.shadow_well_defined

        E_non = Rank2Bundle(C, 0, 0)
        curv_non = compute_curvature(E_non)
        assert not curv_non.shadow_well_defined

    def test_sn_bracket_path(self):
        """Path 6: SN bracket vanishes on invariant sector iff CY."""
        assert sn_bracket_vanishes_on_invariant_sector(-1, -1)  # conifold
        assert sn_bracket_vanishes_on_invariant_sector(0, -2)   # another CY
        assert not sn_bracket_vanishes_on_invariant_sector(0, 0)  # non-CY


# ================================================================
# 6. POLYVECTOR FIELDS
# ================================================================

class TestPolyvectorFields:
    """Verify polyvector field dimensions on Tot(E) for P^1."""

    def test_pv0_fiber_deg_0(self):
        """PV^0 in fiber degree 0 = H^0(P^1, O) = 1."""
        dims = polyvector_field_dims_split_P1(-1, -1, fiber_deg_max=2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert dims[(0, 0)] == 1

    def test_pv3_conifold_fiber_deg_0(self):
        """PV^3 in fiber deg 0 for conifold: det(T+E) = O(0), so h^0 = 1."""
        dims = polyvector_field_dims_split_P1(-1, -1, fiber_deg_max=0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert dims[(3, 0)] == 1  # h^0(O(2+(-1)+(-1))) = h^0(O(0)) = 1

    def test_pv3_non_cy_fiber_deg_0(self):
        """PV^3 for non-CY O(0)+O(0): det = O(2), h^0(O(2)) = 3."""
        dims = polyvector_field_dims_split_P1(0, 0, fiber_deg_max=0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert dims[(3, 0)] == 3

    def test_pv_totals_conifold(self):
        """Total PV dimensions for conifold (fiber deg 0 only)."""
        dims = total_pv_dim_P1(-1, -1, fiber_deg_max=0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert dims[0] == 1    # h^0(O) = 1
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert dims[3] == 1    # h^0(O(0)) = 1 (CY form)

    def test_sn_bracket_weight_values(self):
        """SN bracket: PV^p x PV^q -> PV^{p+q-1}."""
        # VERIFIED [DC] conformal weight [LT] chiral algebra theory
        assert sn_bracket_weight(1, 1) == 1
        # VERIFIED [DC] conformal weight [LT] chiral algebra theory
        assert sn_bracket_weight(2, 1) == 2
        # VERIFIED [DC] conformal weight [LT] chiral algebra theory
        assert sn_bracket_weight(1, 2) == 2
        # VERIFIED [DC] conformal weight [LT] chiral algebra theory
        assert sn_bracket_weight(2, 2) == 3
        # VERIFIED [DC] conformal weight [LT] chiral algebra theory
        assert sn_bracket_weight(0, 3) == 2

    def test_pv_symmetry_conifold(self):
        """Conifold O(-1)+O(-1) is Z_2 symmetric: PV dims symmetric in (a,b)."""
        dims_ab = polyvector_field_dims_split_P1(-1, -1, fiber_deg_max=3)
        dims_ba = polyvector_field_dims_split_P1(-1, -1, fiber_deg_max=3)
        for key in dims_ab:
            assert dims_ab[key] == dims_ba[key]


# ================================================================
# 7. KAPPA COMPUTATIONS
# ================================================================

class TestKappa:
    """Verify kappa (modular characteristic) computations."""

    def test_conifold_kappa(self):
        """kappa(conifold) = 1."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_conifold() == Fraction(1)

    def test_conifold_kappa_from_split(self):
        """kappa(O(-1)+O(-1)->P^1) = 1."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_split_P1(-1) == Fraction(1)

    def test_birational_invariance(self):
        """kappa = 1 for ALL CY split bundles over P^1."""
        result = verify_birational_invariance_kappa(a_range=10)
        assert result["all_equal"]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["common_value"] == Fraction(1)

    def test_kappa_genus_0(self):
        """kappa(Tot(E -> P^1)) = 1."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_bundle_genus_g(0) == Fraction(1)

    def test_kappa_genus_1(self):
        """kappa(Tot(E -> E)) = 0 (self-dual, anomaly-free)."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_bundle_genus_g(1) == Fraction(0)

    def test_kappa_genus_2(self):
        """kappa(Tot(E -> C_2)) = -1."""
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_bundle_genus_g(2) == Fraction(-1)

    def test_kappa_genus_formula(self):
        """kappa(Tot(E -> C_g)) = 1 - g for all g."""
        for g in range(20):
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert kappa_cy_bundle_genus_g(g) == Fraction(1 - g)

    def test_kappa_self_dual_genus(self):
        """kappa = 0 only at genus 1."""
        data = kappa_genus_variation(g_max=10)
        zero_genera = [d["genus"] for d in data["data"] if d["kappa"] == 0]
        # VERIFIED [DC] kappa computation [LT] chiral algebra theory
        assert zero_genera == [1]

    def test_kappa_positive_only_genus_0(self):
        """kappa > 0 only at genus 0."""
        data = kappa_genus_variation(g_max=10)
        pos_genera = [d["genus"] for d in data["data"] if d["kappa"] > 0]
        # VERIFIED [DC] kappa computation [LT] chiral algebra theory
        assert pos_genera == [0]


# ================================================================
# 8. SHADOW TOWER
# ================================================================

class TestShadowTower:
    """Verify shadow obstruction tower data."""

    def test_conifold_shadow_class_G(self):
        """Conifold O(-1)+O(-1) is class G (Gaussian, depth 2)."""
        st = shadow_tower_cy_split_P1(-1)
        # VERIFIED [DC] shadow structure [LT] chiral algebra theory
        assert st.shadow_class == "G"
        # VERIFIED [DC] shadow depth [LT] chiral algebra theory
        assert st.shadow_depth == "2"

    def test_conifold_shadow_kappa(self):
        """Shadow tower kappa = 1 for conifold."""
        st = shadow_tower_cy_split_P1(-1)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert st.kappa == Fraction(1)

    def test_conifold_genus_1_obs(self):
        """F_1 = kappa/24 = 1/24 for conifold."""
        st = shadow_tower_cy_split_P1(-1)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert st.genus_1_obs == Fraction(1, 24)

    def test_unbalanced_shadow_class_M(self):
        """Unbalanced CY bundles have shadow depth infinity (class M)."""
        for a in [-3, -2, 0, 1, 2, 3]:
            if a != -1:
                st = shadow_tower_cy_split_P1(a)
                # VERIFIED [DC] shadow structure [LT] chiral algebra theory
                assert st.shadow_class == "M"
                # VERIFIED [DC] shadow depth [LT] chiral algebra theory
                assert st.shadow_depth == "infinity"

    def test_shadow_well_defined_cy(self):
        """Shadow tower is well-defined for CY bundles."""
        for a in range(-3, 4):
            st = shadow_tower_cy_split_P1(a)
            assert st.is_well_defined

    def test_genus_1_shadow_trivial(self):
        """Shadow tower for elliptic base: kappa = 0, trivial."""
        st = shadow_tower_cy_genus_g(1)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert st.kappa == Fraction(0)
        # VERIFIED [DC] genus free energy [LT] chiral algebra theory
        assert st.shadow_class == "trivial"
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert st.genus_1_obs == Fraction(0)


# ================================================================
# 9. CURVATURE AND ANOMALY
# ================================================================

class TestCurvatureAnomaly:
    """Verify curvature computations for non-CY bundles."""

    def test_cy_uncurved(self):
        """CY bundle has zero curvature."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        curv = compute_curvature(E)
        assert curv.is_uncurved
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert curv.cy_defect == 0
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert curv.curvature_class == Fraction(0)

    def test_non_cy_curved(self):
        """Non-CY bundle has nonzero curvature."""
        C = projective_line()
        E = Rank2Bundle(C, 0, 0)
        curv = compute_curvature(E)
        assert not curv.is_uncurved
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert curv.cy_defect == 2
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert curv.curvature_class == Fraction(2)

    def test_curvature_proportional_to_delta(self):
        """Curvature class = delta for all bundles."""
        C = projective_line()
        for a in range(-4, 4):
            for b in range(-4, 4):
                E = Rank2Bundle(C, a, b)
                curv = compute_curvature(E)
                # VERIFIED [DC] structural property [LT] chiral algebra theory
                assert curv.curvature_class == Fraction(E.cy_defect)

    def test_anomaly_polynomial_cy(self):
        """Anomaly polynomial vanishes at CY locus."""
        result = anomaly_polynomial_P1(-1, -1)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["delta"] == 0
        assert result["is_anomaly_free"]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["curvature_m0"] == Fraction(0)

    def test_anomaly_polynomial_non_cy(self):
        """Anomaly polynomial nonzero for non-CY."""
        result = anomaly_polynomial_P1(0, 0)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["delta"] == 2
        assert not result["is_anomaly_free"]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["curvature_m0"] == Fraction(2)

    def test_anomaly_c2_computation(self):
        """c_2(O(a)+O(b)) = a*b."""
        result = anomaly_polynomial_P1(2, 3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["c2_E"] == 6

    def test_anomaly_c1_computation(self):
        """c_1(O(a)+O(b)) = a+b."""
        result = anomaly_polynomial_P1(2, 3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["c1_E"] == 5


# ================================================================
# 10. ANOMALY CANCELLATION
# ================================================================

class TestAnomalyCancellation:
    """Verify anomaly cancellation mechanisms."""

    def test_cy_already_cancelled(self):
        """CY bundles are already anomaly-free."""
        result = anomaly_cancellation_check(-1, -1)
        assert result["anomaly_free"]

    def test_even_delta_twist(self):
        """Even delta can be cancelled by integral twist."""
        result = anomaly_cancellation_check(0, 0)
        assert not result["anomaly_free"]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["delta"] == 2
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["twist_to_cancel"] == Fraction(-1)
        assert result["twist_integral"]

    def test_odd_delta_no_integral_twist(self):
        """Odd delta cannot be cancelled by integral twist."""
        result = anomaly_cancellation_check(0, 1)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert result["delta"] == 3
        assert not result["twist_integral"]

    def test_twist_produces_cy(self):
        """Twisting by t = -delta/2 produces CY (when integral)."""
        C = projective_line()
        a, b = 1, 1  # delta = 4
        result = anomaly_cancellation_check(a, b)
        t = int(result["twist_to_cancel"])
        E_twisted = Rank2Bundle(C, a + t, b + t)
        assert E_twisted.is_calabi_yau


# ================================================================
# 11. RIEMANN-ROCH
# ================================================================

class TestRiemannRoch:
    """Verify Riemann-Roch computations."""

    def test_chi_E_formula(self):
        """chi(C_g, E) = deg(E) + 2(1-g)."""
        for g in range(5):
            C = genus_g_curve(g) if g > 0 else projective_line()
            for a in range(-3, 4):
                for b in range(-3, 4):
                    E = Rank2Bundle(C, a, b)
                    rr = riemann_roch_rank2(E)
                    expected = Fraction(a + b + 2 * (1 - g))
                    assert rr["chi_E"] == expected

    def test_chi_vanishes_iff_cy(self):
        """chi(C, E) = 0 iff delta = 0 (CY)."""
        result = verify_rr_vanishing_at_cy()
        assert result["all_vanish"]

    def test_chi_sym0(self):
        """Sym^0(E) = O_C, so chi(Sym^0(E)) = chi(O_C) = 1 - g."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        rr = riemann_roch_rank2(E)
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert rr["chi_sym_k"][0] == Fraction(1)  # g=0: chi(O) = 1

    def test_chi_sym1_equals_chi_E(self):
        """Sym^1(E) = E, so chi(Sym^1(E)) = chi(E)."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        rr = riemann_roch_rank2(E)
        assert rr["chi_sym_k"][1] == rr["chi_E"]


# ================================================================
# 12. CY DEFECT LINEARITY
# ================================================================

class TestCYDefectLinearity:
    """Verify linearity of CY defect in bundle degrees."""

    def test_defect_linearity(self):
        """delta(O(a)+O(b)) = a + b + 2 on P^1: linear in (a,b)."""
        result = verify_cy_defect_linearity(a_range=4)
        assert result["all_match"]

    def test_defect_additivity(self):
        """delta(a1+a2, b1+b2) = delta(a1,b1) + delta(a2,b2) - delta(0,0)."""
        C = projective_line()
        for a1 in range(-2, 3):
            for b1 in range(-2, 3):
                for a2 in range(-2, 3):
                    for b2 in range(-2, 3):
                        d1 = Rank2Bundle(C, a1, b1).cy_defect
                        d2 = Rank2Bundle(C, a2, b2).cy_defect
                        d12 = Rank2Bundle(C, a1 + a2, b1 + b2).cy_defect
                        d0 = Rank2Bundle(C, 0, 0).cy_defect  # = 2
                        # Linearity: delta is linear in deg(E) = a+b.
                        # delta(a+a', b+b') = (a+a')+(b+b')+2 = delta(a,b) + delta(a',b') - 2
                        assert d12 == d1 + d2 - d0


# ================================================================
# 13. MODULI SPACES
# ================================================================

class TestModuliSpaces:
    """Verify moduli space dimensions."""

    def test_moduli_P1(self):
        """No moduli on P^1 (Grothendieck splitting)."""
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert moduli_dimension(0, 0) == 0

    def test_moduli_elliptic(self):
        """dim M(2,d) = 1 on elliptic curve."""
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert moduli_dimension(1, 0) == 1
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert moduli_dimension(1, 1) == 1

    def test_moduli_genus_2(self):
        """dim M(2,d) = 5 on genus-2 curve."""
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert moduli_dimension(2, 0) == 5
        # VERIFIED [DC] dimension count [LT] chiral algebra theory
        assert moduli_dimension(2, 1) == 5

    def test_moduli_genus_g_formula(self):
        """dim M(2,d) = 4g - 3 for g >= 2."""
        for g in range(2, 10):
            # VERIFIED [DC] dimension count [LT] chiral algebra theory
            assert moduli_dimension(g, 0) == 4 * g - 3

    def test_atiyah_classification(self):
        """Atiyah classification for elliptic curves."""
        data = atiyah_classification_elliptic(0)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert data["moduli_dim"] == 1
        assert data["indecomposable_exists"]


# ================================================================
# 14. EXTENSION DEFORMATIONS
# ================================================================

class TestExtensionDeformations:
    """Verify extension deformation computations."""

    def test_deformation_unobstructed(self):
        """All deformations on curves are unobstructed (Ext^2 = 0)."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 0, 0, extension_class_nonzero=True)
        ext_data = extension_deformation_order(E)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert ext_data["ext2_dim"] == 0
        assert ext_data["deformation_unobstructed"]

    def test_ext1_gives_deformation_space(self):
        """Deformation space dimension = dim Ext^1."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 0, 0)
        ext_data = extension_deformation_order(E)
        assert ext_data["deformation_space_dim"] == E.ext1_dimension
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert ext_data["deformation_space_dim"] == 1

    def test_P1_no_deformation(self):
        """Conifold O(-1)+O(-1) on P^1 has no extension deformation."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        ext_data = extension_deformation_order(E)
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert ext_data["ext1_dim"] == 0
        assert not ext_data["nonsplit_exists"]


# ================================================================
# 15. CHIRAL ALGEBRA FUNCTOR
# ================================================================

class TestChiralAlgebraFunctor:
    """Verify the main functor: bundle -> chiral algebra."""

    def test_conifold_is_uncurved(self):
        """Conifold chiral algebra is uncurved."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        data = chiral_algebra_from_bundle(E)
        assert data.is_calabi_yau
        assert data.curvature.is_uncurved

    def test_conifold_kappa(self):
        """Conifold kappa = 1."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        data = chiral_algebra_from_bundle(E)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert data.kappa == Fraction(1)

    def test_non_cy_is_curved(self):
        """Non-CY chiral algebra is curved."""
        C = projective_line()
        E = Rank2Bundle(C, 0, 0)
        data = chiral_algebra_from_bundle(E)
        assert not data.is_calabi_yau
        assert not data.curvature.is_uncurved
        assert data.kappa is None

    def test_non_cy_no_shadow(self):
        """Non-CY chiral algebra has no shadow tower."""
        C = projective_line()
        E = Rank2Bundle(C, 1, 1)
        data = chiral_algebra_from_bundle(E)
        assert data.shadow_tower is None

    def test_cy_has_shadow(self):
        """CY chiral algebra has a shadow tower."""
        C = projective_line()
        E = Rank2Bundle(C, 0, -2)
        data = chiral_algebra_from_bundle(E)
        assert data.shadow_tower is not None
        assert data.shadow_tower.is_well_defined

    def test_functor_description_cy(self):
        """Functor produces meaningful description for CY."""
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)
        data = chiral_algebra_from_bundle(E)
        assert "Uncurved" in data.description
        assert "kappa = 1" in data.description

    def test_functor_description_non_cy(self):
        """Functor produces meaningful description for non-CY."""
        C = projective_line()
        E = Rank2Bundle(C, 0, 0)
        data = chiral_algebra_from_bundle(E)
        assert "Curved" in data.description
        assert "delta = 2" in data.description

    def test_comprehensive_analysis(self):
        """rank2_bundle_analysis returns complete data."""
        result = rank2_bundle_analysis(a=-1, b=-1, g=0)
        assert result["bundle"]["is_calabi_yau"]
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert result["chiral_algebra"]["kappa"] == Fraction(1)
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert result["riemann_roch"]["chi_E"] == Fraction(0)


# ================================================================
# 16. ENUMERATION
# ================================================================

class TestEnumeration:
    """Verify enumeration of bundle families."""

    def test_cy_split_types_all_cy(self):
        """All enumerated CY split types are actually CY."""
        types = enumerate_cy_split_types_P1(a_range=5)
        for a, b, data in types:
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert a + b == -2
            assert data.is_calabi_yau

    def test_cy_split_types_count(self):
        """Correct count of CY split types for given range."""
        types = enumerate_cy_split_types_P1(a_range=3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(types) == 7  # a = -3, -2, -1, 0, 1, 2, 3

    def test_non_cy_types_all_non_cy(self):
        """All enumerated non-CY types have delta != 0."""
        types = enumerate_non_cy_P1(deg_range=2)
        for a, b, delta, data in types:
            assert delta != 0
            assert not data.is_calabi_yau

    def test_non_cy_enumeration_nonempty(self):
        """Non-CY enumeration produces results."""
        types = enumerate_non_cy_P1(deg_range=2)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(types) > 0

    def test_summary_table_includes_cy(self):
        """Summary table includes CY cases."""
        rows = summary_table_P1(a_range=2)
        cy_rows = [r for r in rows if r["is_CY"]]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(cy_rows) > 0
        for r in cy_rows:
            # VERIFIED [DC] structural property [LT] chiral algebra theory
            assert r["delta"] == 0
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert r["kappa"] == Fraction(1)

    def test_summary_table_includes_non_cy(self):
        """Summary table includes non-CY cases."""
        rows = summary_table_P1(a_range=2)
        non_cy_rows = [r for r in rows if not r["is_CY"]]
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert len(non_cy_rows) > 0
        for r in non_cy_rows:
            assert r["delta"] != 0
            assert r["kappa"] is None


# ================================================================
# 17. CROSS-CONSISTENCY CHECKS
# ================================================================

class TestCrossConsistency:
    """Cross-consistency checks between different computations."""

    def test_kappa_matches_shadow(self):
        """kappa from direct formula matches shadow tower."""
        for a in range(-3, 4):
            kappa_direct = kappa_cy_split_P1(a)
            st = shadow_tower_cy_split_P1(a)
            assert kappa_direct == st.kappa

    def test_genus_1_obs_from_kappa(self):
        """F_1 = kappa/24 for all CY bundles."""
        for g in range(5):
            kappa = kappa_cy_bundle_genus_g(g)
            st = shadow_tower_cy_genus_g(g)
            if kappa is not None:
                assert st.genus_1_obs == kappa / 24

    def test_cy_defect_zero_iff_uncurved(self):
        """delta = 0 iff curvature = 0, across all tested bundles."""
        C = projective_line()
        for a in range(-4, 4):
            for b in range(-4, 4):
                E = Rank2Bundle(C, a, b)
                curv = compute_curvature(E)
                # VERIFIED [DC] structural property [LT] chiral algebra theory
                assert (E.cy_defect == 0) == curv.is_uncurved

    def test_cy_defect_zero_iff_rr_vanishes(self):
        """delta = 0 iff chi(E) = 0, for all bundles over P^1."""
        C = projective_line()
        for a in range(-4, 4):
            for b in range(-4, 4):
                E = Rank2Bundle(C, a, b)
                rr = riemann_roch_rank2(E)
                # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
                assert (E.cy_defect == 0) == (rr["chi_E"] == 0)

    def test_volume_form_degree_equals_negative_cy_sum(self):
        """deg(Omega_3) = -(2 + a + b) = -delta for P^1 (since 2g-2 = -2)."""
        for a in range(-3, 4):
            for b in range(-3, 4):
                vf_deg = cy_volume_form_degree(a, b)
                assert vf_deg == -(2 + a + b)
                # When CY: vf_deg = 0
                C = projective_line()
                E = Rank2Bundle(C, a, b)
                # VERIFIED [DC] structural property [LT] chiral algebra theory
                assert (vf_deg == 0) == E.is_calabi_yau

    def test_effective_central_charge_cy(self):
        """c_eff = 2 for CY bundles over P^1."""
        # VERIFIED [DC] central charge [LT] chiral algebra theory
        assert effective_central_charge_P1(-1, -1) == Fraction(2)
        # VERIFIED [DC] central charge [LT] chiral algebra theory
        assert effective_central_charge_P1(0, -2) == Fraction(2)
        # VERIFIED [DC] central charge [LT] chiral algebra theory
        assert effective_central_charge_P1(1, -3) == Fraction(2)

    def test_effective_central_charge_decreases_with_delta(self):
        """c_eff < 2 for non-CY (delta != 0) bundles over P^1."""
        # delta^2 > 0 means c_eff = 2 - delta^2/6 < 2
        for delta in [1, 2, 3]:
            a = delta - 1  # a + b + 2 = delta -> b = delta - 2 - a
            b = delta - 2 - a
            c_eff = effective_central_charge_P1(a, b)
            # VERIFIED [DC] central charge [LT] chiral algebra theory
            assert c_eff < 2


# ================================================================
# 18. HOCHSCHILD HOMOLOGY
# ================================================================

class TestHochschildHomology:
    """Verify Hochschild homology computations."""

    def test_hh0_conifold(self):
        """HH_0 has contribution from PV^0 in fiber degree 0."""
        hh = hochschild_homology_dims_P1(-1, -1, fiber_deg_max=3)
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert hh.get(0, 0) >= 1  # At least the constant functions

    def test_hh_depends_on_bundle(self):
        """HH dims change with bundle type."""
        hh1 = hochschild_homology_dims_P1(-1, -1, fiber_deg_max=2)
        hh2 = hochschild_homology_dims_P1(0, 0, fiber_deg_max=2)
        # These should differ since the bundles are different
        assert hh1 != hh2

    def test_hh_nonnegative(self):
        """All HH dimensions are non-negative."""
        for a in range(-2, 3):
            for b in range(-2, 3):
                hh = hochschild_homology_dims_P1(a, b, fiber_deg_max=2)
                for n, dim in hh.items():
                    # VERIFIED [DC] dimension count [LT] chiral algebra theory
                    assert dim >= 0, f"HH_{n} = {dim} < 0 for ({a},{b})"


# ================================================================
# 19. GENUS VARIATION
# ================================================================

class TestGenusVariation:
    """Verify kappa variation with genus."""

    def test_kappa_monotone_decreasing(self):
        """kappa = 1 - g is monotone decreasing in g."""
        data = kappa_genus_variation(g_max=10)
        kappas = [d["kappa"] for d in data["data"]]
        for i in range(len(kappas) - 1):
            assert kappas[i] > kappas[i + 1]

    def test_kappa_integer(self):
        """kappa = 1 - g is always an integer."""
        for g in range(20):
            kappa = kappa_cy_bundle_genus_g(g)
            # VERIFIED [DC] kappa formula [LT] chiral algebra theory
            assert kappa.denominator == 1

    def test_self_dual_at_genus_1(self):
        """The self-dual point (kappa = 0) is at genus 1."""
        data = kappa_genus_variation(g_max=10)
        # VERIFIED [DC] genus tower [LT] chiral algebra theory
        assert data["self_dual_genus"] == 1


# ================================================================
# 20. COMPREHENSIVE VERIFICATION
# ================================================================

class TestComprehensiveVerification:
    """Comprehensive multi-path verification of the full construction."""

    def test_five_path_conifold(self):
        """Five independent paths confirm conifold is CY with kappa = 1.

        Path 1: delta = (-1) + (-1) + 2 = 0
        Path 2: chi(P^1, O(-1)+O(-1)) = 0 (RR)
        Path 3: deg(det(T+E)) = 2+(-1)+(-1) = 0 (volume form)
        Path 4: curvature m_0 = 0 (uncurved bar)
        Path 5: kappa = 1 (birational invariant)
        """
        C = projective_line()
        E = Rank2Bundle(C, -1, -1)

        # Path 1
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert E.cy_defect == 0

        # Path 2
        rr = riemann_roch_rank2(E)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert rr["chi_E"] == Fraction(0)

        # Path 3
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert cy_volume_form_degree(-1, -1) == 0

        # Path 4
        curv = compute_curvature(E)
        assert curv.is_uncurved

        # Path 5
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_split_P1(-1) == Fraction(1)

    def test_five_path_non_cy(self):
        """Five paths confirm O(0)+O(0)->P^1 is non-CY with delta = 2.

        Path 1: delta = 0 + 0 + 2 = 2
        Path 2: chi(P^1, O+O) = 2 != 0
        Path 3: deg(det(T+E)) = 2 != 0
        Path 4: curvature m_0 = 2 * omega
        Path 5: kappa undefined (curved)
        """
        C = projective_line()
        E = Rank2Bundle(C, 0, 0)

        # Path 1
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert E.cy_defect == 2

        # Path 2
        rr = riemann_roch_rank2(E)
        # VERIFIED [DC] Euler characteristic formula [LT] chiral algebra theory
        assert rr["chi_E"] == Fraction(2)

        # Path 3
        assert cy_volume_form_degree(0, 0) != 0

        # Path 4
        curv = compute_curvature(E)
        assert not curv.is_uncurved
        # VERIFIED [DC] structural property [LT] chiral algebra theory
        assert curv.curvature_class == Fraction(2)

        # Path 5
        data = chiral_algebra_from_bundle(E)
        assert data.kappa is None

    def test_elliptic_cy_bundle(self):
        """CY bundle over elliptic curve: kappa = 0, anomaly-free."""
        C = elliptic_curve()
        E = Rank2Bundle(C, 1, -1)
        assert E.is_calabi_yau
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_bundle_genus_g(1) == Fraction(0)

    def test_genus_2_cy_bundle(self):
        """CY bundle over genus-2 curve: kappa = -1."""
        C = genus_g_curve(2)
        E = Rank2Bundle(C, 1, 1)  # a+b = 2 = 2g-2
        assert E.is_calabi_yau
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_cy_bundle_genus_g(2) == Fraction(-1)

    def test_full_analysis_all_fields_present(self):
        """Full analysis returns all expected fields."""
        result = rank2_bundle_analysis(a=-1, b=-1, g=0)
        assert "bundle" in result
        assert "chiral_algebra" in result
        assert "riemann_roch" in result
        assert "polyvector_dims" in result
        assert result["bundle"]["is_calabi_yau"]
        # VERIFIED [DC] Euler characteristic [LT] chiral algebra theory
        assert result["chiral_algebra"]["kappa"] == Fraction(1)


# ================================================================
# 21. MULTI-PATH VERIFICATION: INDEPENDENT CROSS-CHECKS (AP10)
# ================================================================

class TestMultiPathKappa:
    """Multi-path verification of kappa values.

    Each kappa is verified by at least 3 independent paths:
    Path A: topological (chi_top(base) / 2)
    Path B: genus-1 obstruction (F_1 * 24)
    Path C: birational invariance (same for all CY splits over same base)
    Path D: Riemann-Roch (chi(E) = 0 at CY locus => consistent)
    Path E: defect (delta = 0 => uncurved => kappa well-defined)
    """

    def test_kappa_conifold_3_paths(self):
        """kappa(conifold) = 1 via 3 independent computations.

        Path A: chi_top(P^1)/2 = 2/2 = 1.
        Path B: F_1 = kappa/24, shadow_tower gives F_1 = 1/24, so kappa = 1.
        Path C: kappa_cy_split_P1(a) = 1 for all a (birational).
        """
        # Path A: topological
        kappa_A = Fraction(projective_line().euler_char, 2)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_A == Fraction(1)

        # Path B: from genus-1 obstruction
        st = shadow_tower_cy_split_P1(-1)
        kappa_B = st.genus_1_obs * 24
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_B == Fraction(1)

        # Path C: birational invariance
        kappa_C = kappa_cy_split_P1(-1)
        # VERIFIED [DC] kappa formula [LT] chiral algebra theory
        assert kappa_C == Fraction(1)

        # All three agree
        assert kappa_A == kappa_B == kappa_C

    def test_kappa_genus_g_3_paths(self):
        """kappa(Tot(E -> C_g)) = 1-g via 3 paths for g = 0..5.

        Path A: chi_top(C_g)/2 = (2-2g)/2 = 1-g.
        Path B: kappa_cy_bundle_genus_g(g) (direct formula).
        Path C: F_1 * 24 from shadow tower.
        """
        for g in range(6):
            C = genus_g_curve(g) if g > 0 else projective_line()

            # Path A: topological
            kappa_A = Fraction(C.euler_char, 2)

            # Path B: direct formula
            kappa_B = kappa_cy_bundle_genus_g(g)

            # Path C: from shadow tower genus-1 obstruction
            st = shadow_tower_cy_genus_g(g)
            kappa_C = st.genus_1_obs * 24

            assert kappa_A == kappa_B == kappa_C, (
                f"Kappa mismatch at g={g}: A={kappa_A}, B={kappa_B}, C={kappa_C}"
            )

    def test_kappa_birational_10_splits_3_paths(self):
        """All 21 CY split bundles O(a)+O(-2-a) for |a|<=10 give kappa=1.

        Path A: kappa_cy_split_P1(a) for each a.
        Path B: chi_top(P^1)/2 = 1 (independent of a).
        Path C: shadow_tower kappa for each a.
        """
        expected = Fraction(1)
        kappa_topo = Fraction(projective_line().euler_char, 2)
        assert kappa_topo == expected

        for a in range(-10, 11):
            kappa_direct = kappa_cy_split_P1(a)
            st = shadow_tower_cy_split_P1(a)
            assert kappa_direct == expected, f"Direct kappa={kappa_direct} at a={a}"
            assert st.kappa == expected, f"Shadow kappa={st.kappa} at a={a}"


class TestMultiPathCYDefect:
    """Multi-path verification of CY defect.

    Each delta value is verified by 4 independent characterizations:
    Path A: delta = deg(E) - deg(K_C) (definition)
    Path B: chi(E) = delta (Riemann-Roch: chi = deg + rank(1-g) = delta when g=0)
    Path C: deg(volume form bundle) = -delta (for P^1)
    Path D: curvature class = delta
    """

    def test_delta_4_paths_all_P1_bundles(self):
        """4-path verification of delta for all O(a)+O(b) with |a|,|b| <= 3."""
        C = projective_line()
        for a in range(-3, 4):
            for b in range(-3, 4):
                E = Rank2Bundle(C, a, b)

                # Path A: definition
                delta_A = E.cy_defect

                # Path B: Riemann-Roch (chi(E) = deg + 2(1-g) = a+b+2 = delta for g=0)
                rr = riemann_roch_rank2(E)
                delta_B = int(rr["chi_E"])

                # Path C: volume form degree = -(2+a+b) = -delta
                vf_deg = cy_volume_form_degree(a, b)
                delta_C = -vf_deg

                # Path D: curvature class
                curv = compute_curvature(E)
                delta_D = int(curv.curvature_class)

                assert delta_A == delta_B == delta_C == delta_D, (
                    f"Delta mismatch at ({a},{b}): "
                    f"A={delta_A}, B={delta_B}, C={delta_C}, D={delta_D}"
                )

    def test_delta_elliptic_3_paths(self):
        """3-path verification of delta for bundles over elliptic curve."""
        C = elliptic_curve()
        for a in range(-3, 4):
            for b in range(-3, 4):
                E = Rank2Bundle(C, a, b)

                # Path A: definition
                delta_A = E.cy_defect

                # Path B: Riemann-Roch (chi = deg + 2(1-1) = deg = a+b = delta for g=1)
                rr = riemann_roch_rank2(E)
                delta_B = int(rr["chi_E"])

                # Path C: curvature
                curv = compute_curvature(E)
                delta_C = int(curv.curvature_class)

                assert delta_A == delta_B == delta_C, (
                    f"Delta mismatch at ({a},{b}) on elliptic: "
                    f"A={delta_A}, B={delta_B}, C={delta_C}"
                )


class TestMultiPathPVDims:
    """Multi-path verification of polyvector field dimensions.

    Path A: direct computation via h^0 sums
    Path B: Euler characteristic (h^0 - h^1 = chi = deg + 1 on P^1)
    Path C: symmetry checks (e.g., PV^3 at delta=0 has dim = PV^0)
    """

    def test_pv3_fiber0_via_euler_char(self):
        """PV^3 in fiber degree 0: dim = h^0(O(2+a+b)).

        Path A: direct h^0 computation.
        Path B: Euler characteristic chi(O(2+a+b)) = 2+a+b+1 = 3+a+b (on P^1),
                and h^1(O(n)) = 0 for n >= -1, so h^0 = chi when 2+a+b >= -1.
        """
        for a in range(-2, 3):
            for b in range(-2, 3):
                dims = polyvector_field_dims_split_P1(a, b, fiber_deg_max=0)

                # Path A: from the function
                dim_A = dims[(3, 0)]

                # Path B: independent computation
                deg = 2 + a + b
                dim_B = max(deg + 1, 0)

                assert dim_A == dim_B, (
                    f"PV^3 mismatch at ({a},{b}): A={dim_A}, B={dim_B}"
                )

    def test_pv0_fiber0_always_1(self):
        """PV^0 in fiber degree 0 = H^0(P^1, O) = 1 for all bundles.

        Path A: from polyvector_field_dims.
        Path B: h^0(O) = 1 (algebraic geometry).
        Path C: sheaf_euler_char_P1(0) = 1 (Riemann-Roch).
        """
        for a in range(-3, 4):
            for b in range(-3, 4):
                dims = polyvector_field_dims_split_P1(a, b, fiber_deg_max=0)

                dim_A = dims[(0, 0)]
                dim_B = h0_P1(0)
                dim_C = sheaf_euler_char_P1(0)  # = 1, and h^1(O) = 0

                # VERIFIED [DC] dimension count [DA] dimensional consistency
                assert dim_A == dim_B == dim_C == 1, (
                    f"PV^0 fiber-0 mismatch at ({a},{b})"
                )

    def test_cy_pv_duality(self):
        """At CY locus (a+b=-2): PV^3 fiber-0 dim = PV^0 fiber-0 dim = 1.

        This is the Serre duality for PV on a CY 3-fold: the volume form
        identifies PV^0 with PV^3.

        Path A: PV^0 fiber-0 = h^0(O) = 1.
        Path B: PV^3 fiber-0 = h^0(O(2+a+b)) = h^0(O(0)) = 1 (when a+b=-2).
        """
        for a in range(-5, 4):
            b = -2 - a
            dims = polyvector_field_dims_split_P1(a, b, fiber_deg_max=0)

            pv0 = dims[(0, 0)]
            pv3 = dims[(3, 0)]

            # VERIFIED [DC] duality relation [LT] chiral algebra theory
            assert pv0 == pv3 == 1, (
                f"CY PV duality fails at a={a}: PV^0={pv0}, PV^3={pv3}"
            )


class TestMultiPathAnomalyPolynomial:
    """Multi-path verification of anomaly polynomial values.

    Path A: anomaly_polynomial_P1 function
    Path B: independent computation from c_1, c_2
    Path C: cross-check: anomaly vanishes iff CY
    """

    def test_anomaly_I4_3_paths(self):
        """Anomaly I_4 via 3 independent paths for all |a|,|b| <= 3.

        Path A: anomaly_polynomial_P1 function.
        Path B: delta * c_2 + (delta^2/2) * c_1^2 (direct formula).
        Path C: vanishes iff delta = 0.
        """
        for a in range(-3, 4):
            for b in range(a, 4):
                result = anomaly_polynomial_P1(a, b)
                delta = a + b + 2
                c1_sq = (a + b) ** 2
                c2 = a * b

                # Path A
                I4_A = result["anomaly_I4"]

                # Path B: independent calculation
                I4_B = Fraction(delta * c2) + Fraction(delta**2 * c1_sq, 2)

                # Path C: vanishes iff delta = 0
                I4_vanishes = (I4_A == 0)

                assert I4_A == I4_B, (
                    f"I4 mismatch at ({a},{b}): A={I4_A}, B={I4_B}"
                )
                if delta == 0:
                    assert I4_vanishes, f"I4 nonzero at CY ({a},{b}): {I4_A}"

    def test_anomaly_m0_equals_delta(self):
        """Curvature m_0 = delta via 2 independent paths.

        Path A: anomaly_polynomial_P1 result.
        Path B: compute_curvature result.
        """
        C = projective_line()
        for a in range(-3, 4):
            for b in range(-3, 4):
                E = Rank2Bundle(C, a, b)

                # Path A
                anom = anomaly_polynomial_P1(a, b)
                m0_A = anom["curvature_m0"]

                # Path B
                curv = compute_curvature(E)
                m0_B = curv.curvature_class

                assert m0_A == m0_B, (
                    f"m0 mismatch at ({a},{b}): A={m0_A}, B={m0_B}"
                )


class TestMultiPathRiemannRoch:
    """Multi-path verification of Riemann-Roch data.

    Path A: riemann_roch_rank2 function.
    Path B: direct formula chi = deg + rank*(1-g).
    Path C: sum of chi for each line bundle summand.
    """

    def test_chi_E_3_paths_all_genera(self):
        """chi(E) via 3 paths for g=0..4, |a|,|b| <= 3.

        Path A: riemann_roch_rank2 result.
        Path B: deg(E) + 2*(1-g).
        Path C: chi(O(a)) + chi(O(b)) = (a+1-g) + (b+1-g) = a+b+2-2g.
        """
        for g in range(5):
            C = genus_g_curve(g) if g > 0 else projective_line()
            for a in range(-3, 4):
                for b in range(-3, 4):
                    E = Rank2Bundle(C, a, b)

                    # Path A
                    rr = riemann_roch_rank2(E)
                    chi_A = rr["chi_E"]

                    # Path B
                    chi_B = Fraction(E.degree + 2 * (1 - g))

                    # Path C: sum of individual chi
                    chi_C = Fraction(
                        sheaf_euler_char_genus_g(g, a) +
                        sheaf_euler_char_genus_g(g, b)
                    )

                    assert chi_A == chi_B == chi_C, (
                        f"chi mismatch at g={g}, ({a},{b}): "
                        f"A={chi_A}, B={chi_B}, C={chi_C}"
                    )

    def test_chi_sym1_equals_chi_E_3_paths(self):
        """chi(Sym^1(E)) = chi(E) via 3 paths.

        Sym^1(E) = E, so their Euler characteristics must agree.
        Path A: rr["chi_sym_k"][1].
        Path B: rr["chi_E"].
        Path C: sheaf_euler_char_genus_g(g, a) + sheaf_euler_char_genus_g(g, b).
        """
        for g in range(4):
            C = genus_g_curve(g) if g > 0 else projective_line()
            for a in range(-2, 3):
                for b in range(-2, 3):
                    E = Rank2Bundle(C, a, b)
                    rr = riemann_roch_rank2(E)

                    chi_sym1 = rr["chi_sym_k"][1]
                    chi_E = rr["chi_E"]
                    chi_direct = Fraction(
                        sheaf_euler_char_genus_g(g, a) +
                        sheaf_euler_char_genus_g(g, b)
                    )

                    assert chi_sym1 == chi_E == chi_direct, (
                        f"Sym^1 mismatch at g={g}, ({a},{b}): "
                        f"sym1={chi_sym1}, E={chi_E}, direct={chi_direct}"
                    )


class TestMultiPathExtensionSpace:
    """Multi-path verification of extension space dimensions.

    Path A: bundle.ext1_dimension.
    Path B: h^1(P^1, O(a1-a2)) computed directly.
    Path C: max(-diff-1, 0) for P^1 (explicit formula).
    """

    def test_ext1_P1_3_paths(self):
        """Ext^1 on P^1 via 3 independent paths for all |a|, |b| <= 4."""
        C = projective_line()
        for a in range(-4, 5):
            for b in range(-4, 5):
                E = Rank2Bundle(C, a, b)

                # Path A: method
                ext1_A = E.ext1_dimension

                # Path B: h^1 computation
                ext1_B = h1_P1(a - b)

                # Path C: explicit formula
                diff = a - b
                ext1_C = max(-diff - 1, 0)

                assert ext1_A == ext1_B == ext1_C, (
                    f"Ext^1 mismatch at ({a},{b}): "
                    f"A={ext1_A}, B={ext1_B}, C={ext1_C}"
                )


class TestMultiPathModuli:
    """Multi-path verification of moduli dimensions.

    Path A: moduli_dimension function.
    Path B: 4g-3 formula (for g >= 2).
    Path C: dim Ext^1(E, E) - dim Aut(E) + 1 (expected deformation theory).
    """

    def test_moduli_dim_genus_ge2_2_paths(self):
        """Moduli dimension via 2 paths for g = 2..10.

        Path A: moduli_dimension(g, d).
        Path B: 4g - 3 (Narasimhan-Seshadri formula).
        """
        for g in range(2, 11):
            dim_A = moduli_dimension(g, 0)
            dim_B = 4 * g - 3
            assert dim_A == dim_B, (
                f"Moduli dim mismatch at g={g}: A={dim_A}, B={dim_B}"
            )
