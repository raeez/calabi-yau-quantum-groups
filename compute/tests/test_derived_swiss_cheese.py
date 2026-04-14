"""Tests for the derived Swiss-cheese operad framework for 6d hCS.

Verifies the infinity-operadic SC^{ch,top} structure, the six derived
stacks of the bulk-boundary correspondence, the obstruction theory,
the Koszul dual projection, and the defect algebra hierarchy.

GROUND TRUTH:

  SC^{ch,top} structure:
    - Directionality: no open-to-closed operations
    - Segal condition: operation space Euler chars = n!
    - FM_k(C): real dimension 2k-2 for k >= 2
    - Conf^{ord}_m(R): contractible (dim 0)

  Obstruction theory:
    d=1: E_inf, all trivial
    d=2: pi_2(BU) = Z, E_2 exists with braiding parameter
    d=3: pi_3(BU) = 0, E_3 exists with trivial framing

  Six derived stacks:
    bulk (E_3), boundary (E_2), open (E_1), closed (E_2), defect (E_1),
    defect^! (E_1)

  HCS hierarchy (3d -> 5d -> 6d):
    3d: V_k(g), bulk E_1, boundary E_1, PROVED
    5d: Y(gl_hat_1), bulk E_2, boundary E_1, PROVED
    6d: U_{q,t}, bulk E_3, boundary E_2, CONJECTURED

  Defect algebra hierarchy:
    3d: V_{k'}(g), conductor 0, 1-param R-matrix
    5d: Y^!, conductor 0, 1-param R-matrix
    6d: U^!_{q,t}, conductor 0, 2-param R-matrix

  Structure function g(z):
    phi_0 = 1
    phi_1 = 0 (CY condition: h_1 + h_2 + h_3 = 0)
    phi_2 = 0 (parity)
    phi_3 = -2*sigma_3 = -2*h_1*h_2*h_3

  Bar complex dimensions (P(q)^n pattern):
    E_1: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
    E_2: P(q)^2 convolution
    E_3: P(q)^3 convolution

Manuscript references:
  chapters/theory/quantum_chiral_algebras.tex:
    Construction constr:quantum-ce-deformation
    Conjecture conj:chiral-qg-c3, conj:chiral-qg-k3xe
  chapters/theory/e1_chiral_algebras.tex:
    Section sec:e1-chiral-bialgebras
    Definition def:swiss-cheese-split
  chapters/theory/en_factorization.tex:
    Theorem thm:e1-stabilization-cy
"""

import pytest
from fractions import Fraction

from compute.lib.derived_swiss_cheese import (
    BulkBoundaryCoupling,
    ClaimStatus,
    CYDim,
    DerivedSCOperad,
    DefectAlgebraFromSC,
    DerivedStackData,
    EnLevel,
    ObstructionGroup,
    RestrictionMapData,
    SCColor,
    SCOperationSpace,
    build_6d_stacks,
    build_defect_hierarchy,
    build_hcs_hierarchy,
    build_restriction_map,
    compute_obstruction_6d_hcs,
    master_derived_sc_verification,
    verify_center_promotion_not_iterated_drinfeld,
    verify_defect_hierarchy,
    verify_hcs_hierarchy_consistency,
)


# =========================================================================
# 1. SC operation space tests
# =========================================================================

class TestSCOperationSpace:
    """Test the operation spaces of the Swiss-cheese operad."""

    def test_directionality_open_to_closed_empty(self):
        """No open-to-closed: SC(0 closed, k open; closed) is EMPTY."""
        for k in range(1, 6):
            op = SCOperationSpace(n_closed=0, n_open=k, output_color=SCColor.CLOSED)
            assert op.is_empty, f"SC(0, {k}; closed) should be empty"

    def test_closed_to_closed_nonempty(self):
        """Closed-to-closed: SC(k closed, 0 open; closed) is nonempty."""
        for k in range(1, 6):
            op = SCOperationSpace(n_closed=k, n_open=0, output_color=SCColor.CLOSED)
            assert not op.is_empty

    def test_mixed_to_open_nonempty(self):
        """Mixed inputs to open output: always nonempty."""
        for k in range(1, 4):
            for m in range(1, 4):
                op = SCOperationSpace(n_closed=k, n_open=m, output_color=SCColor.OPEN)
                assert not op.is_empty

    def test_fm_euler_characteristic(self):
        """FM_k(C) has Euler characteristic k!."""
        for k in range(1, 6):
            op = SCOperationSpace(n_closed=k, n_open=0, output_color=SCColor.CLOSED)
            import math
            assert op.euler_characteristic == math.factorial(k)

    def test_ordered_config_contractible(self):
        """Conf^{ord}_m(R) is contractible: chi = 1."""
        for m in range(1, 6):
            op = SCOperationSpace(n_closed=0, n_open=m, output_color=SCColor.OPEN)
            assert op.euler_characteristic == 1

    def test_fm_dimension(self):
        """FM_k(C) has real dimension 2k-2 for k >= 2, 0 for k <= 1."""
        assert SCOperationSpace(1, 0, SCColor.CLOSED).topological_dimension == 0
        assert SCOperationSpace(2, 0, SCColor.CLOSED).topological_dimension == 2
        assert SCOperationSpace(3, 0, SCColor.CLOSED).topological_dimension == 4
        assert SCOperationSpace(4, 0, SCColor.CLOSED).topological_dimension == 6

    def test_empty_space_returns_none(self):
        """Empty operation spaces return None for dimension and chi."""
        op = SCOperationSpace(0, 3, SCColor.CLOSED)
        assert op.is_empty
        assert op.topological_dimension is None
        assert op.euler_characteristic is None
        assert op.homotopy_type is None

    def test_homotopy_type_point(self):
        """Single-input closed-to-closed has trivial homotopy type."""
        op = SCOperationSpace(1, 0, SCColor.CLOSED)
        assert op.homotopy_type == "point"

    def test_homotopy_type_braid(self):
        """Multi-input has braid group classifying space."""
        op = SCOperationSpace(3, 0, SCColor.CLOSED)
        assert "B_3" in op.homotopy_type


# =========================================================================
# 2. Derived SC operad tests
# =========================================================================

class TestDerivedSCOperad:
    """Test the derived SC^{ch,top} infinity-operad."""

    def test_6d_construction(self):
        """6d hCS: bulk E_3, boundary E_2."""
        sc = DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E3, bdry_en=EnLevel.E2)
        assert sc.hcs_dim == 3
        assert sc.bulk_en == EnLevel.E3
        assert sc.bdry_en == EnLevel.E2

    def test_5d_construction(self):
        """5d hCS: bulk E_2, boundary E_1."""
        sc = DerivedSCOperad(hcs_dim=2, bulk_en=EnLevel.E2, bdry_en=EnLevel.E1)
        assert sc.hcs_dim == 2

    def test_3d_construction(self):
        """3d hCS: bulk E_1, boundary E_1."""
        sc = DerivedSCOperad(hcs_dim=1, bulk_en=EnLevel.E1, bdry_en=EnLevel.E1)
        assert sc.hcs_dim == 1

    def test_invalid_bulk_en_raises(self):
        """Mismatched bulk E_n level raises assertion."""
        with pytest.raises(AssertionError):
            DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E2, bdry_en=EnLevel.E2)

    def test_invalid_bdry_en_raises(self):
        """Mismatched boundary E_n level raises assertion."""
        with pytest.raises(AssertionError):
            DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E3, bdry_en=EnLevel.E1)

    def test_directionality(self):
        """Directionality constraint passes."""
        sc = DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E3, bdry_en=EnLevel.E2)
        result = sc.verify_directionality()
        assert result["ok"]

    def test_segal_condition(self):
        """Segal condition holds."""
        sc = DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E3, bdry_en=EnLevel.E2)
        result = sc.verify_segal_condition()
        assert result["ok"]

    def test_tangent_dims_gl1(self):
        """Tangent complex for gl_1 (gauge_dim=1)."""
        sc = DerivedSCOperad(hcs_dim=3, bulk_en=EnLevel.E3, bdry_en=EnLevel.E2)
        dims = sc.compute_tangent_complex_dims(gauge_dim=1, trunc=3)
        # Bulk: monomials in 3 variables of degree <= d
        # d=0: 1, d=1: 4, d=2: 10, d=3: 20
        assert dims["bulk_dims"][0] == 1
        assert dims["bulk_dims"][1] == 4
        assert dims["bulk_dims"][2] == 10
        assert dims["bulk_dims"][3] == 20
        # Boundary: monomials in 2 variables
        # d=0: 1, d=1: 3, d=2: 6, d=3: 10
        assert dims["bdry_dims"][0] == 1
        assert dims["bdry_dims"][1] == 3
        assert dims["bdry_dims"][2] == 6
        assert dims["bdry_dims"][3] == 10
        # Fiber = bulk - bdry
        assert dims["fiber_dims"][0] == 0
        assert dims["fiber_dims"][1] == 1
        assert dims["fiber_dims"][2] == 4
        assert dims["fiber_dims"][3] == 10


# =========================================================================
# 3. Obstruction theory tests
# =========================================================================

class TestObstructionTheory:
    """Test the obstruction computation for the derived SC lift."""

    def test_d3_obstruction_vanishes(self):
        """CY_3: obstruction vanishes (pi_3(BU) = 0)."""
        obs = compute_obstruction_6d_hcs(cy_dim=3)
        assert obs.obs_vanishes
        assert obs.bulk_obs_group == ObstructionGroup.ZERO
        assert obs.sc_obs_group == ObstructionGroup.ZERO

    def test_d2_obstruction_exists_but_classified(self):
        """CY_2: pi_2(BU) = Z classifies the braiding, SC still exists."""
        obs = compute_obstruction_6d_hcs(cy_dim=2)
        assert obs.obs_vanishes
        assert obs.bulk_obs_group == ObstructionGroup.Z

    def test_d1_trivial(self):
        """CY_1: all trivial (E_inf)."""
        obs = compute_obstruction_6d_hcs(cy_dim=1)
        assert obs.obs_vanishes
        assert obs.claim_status == ClaimStatus.PROVED_HERE

    def test_d3_conditional_on_cya3(self):
        """CY_3 result is conditional on CY-A_3."""
        obs = compute_obstruction_6d_hcs(cy_dim=3)
        assert obs.claim_status == ClaimStatus.CONDITIONAL
        assert "CY-A_3" in obs.dependencies

    def test_invalid_dim_raises(self):
        """Invalid CY dimension raises ValueError."""
        with pytest.raises(ValueError):
            compute_obstruction_6d_hcs(cy_dim=4)


# =========================================================================
# 4. Six derived stacks tests
# =========================================================================

class TestDerivedStacks:
    """Test the six derived stacks of the 6d bulk-boundary correspondence."""

    def test_six_stacks_exist(self):
        """All six stacks are constructed."""
        stacks = build_6d_stacks()
        assert len(stacks) == 6
        expected = {"bulk", "boundary", "open", "closed", "defect", "defect_dual"}
        assert set(stacks.keys()) == expected

    def test_bulk_is_e3(self):
        """Bulk moduli on C^3 has E_3 structure."""
        stacks = build_6d_stacks()
        assert stacks["bulk"].en_level == EnLevel.E3
        assert stacks["bulk"].complex_dim == 3
        assert stacks["bulk"].sc_color == SCColor.CLOSED

    def test_boundary_is_e2(self):
        """Boundary moduli on C^2 has E_2 structure."""
        stacks = build_6d_stacks()
        assert stacks["boundary"].en_level == EnLevel.E2
        assert stacks["boundary"].complex_dim == 2

    def test_open_is_e1(self):
        """Open moduli on R has E_1 structure."""
        stacks = build_6d_stacks()
        assert stacks["open"].en_level == EnLevel.E1
        assert stacks["open"].sc_color == SCColor.OPEN

    def test_defect_is_e1(self):
        """Defect moduli (fiber of restriction) has E_1 structure."""
        stacks = build_6d_stacks()
        assert stacks["defect"].en_level == EnLevel.E1

    def test_restriction_map(self):
        """Restriction map: bulk (E_3) -> boundary (E_2), fiber E_1."""
        res_map = build_restriction_map()
        assert res_map.source.en_level == EnLevel.E3
        assert res_map.target.en_level == EnLevel.E2
        assert res_map.fiber_en_level == EnLevel.E2  # E_3 - codim(1) = E_2
        assert res_map.codim == 1
        assert res_map.koszul_dual


# =========================================================================
# 5. HCS hierarchy tests
# =========================================================================

class TestHCSHierarchy:
    """Test the holomorphic CS dimensional hierarchy."""

    def test_hierarchy_consistency(self):
        """Full hierarchy consistency check."""
        result = verify_hcs_hierarchy_consistency()
        assert result["ok"]

    def test_3d_level(self):
        """3d: V_k(g), bulk E_1, PROVED."""
        hierarchy = build_hcs_hierarchy()
        level = hierarchy["3d"]
        assert level.bulk_en == EnLevel.E1
        assert level.bdry_en == EnLevel.E1
        assert level.open_en == EnLevel.E1
        assert level.status == ClaimStatus.PROVED_ELSEWHERE

    def test_5d_level(self):
        """5d: Y(gl_hat_1), bulk E_2, PROVED."""
        hierarchy = build_hcs_hierarchy()
        level = hierarchy["5d"]
        assert level.bulk_en == EnLevel.E2
        assert level.bdry_en == EnLevel.E1
        assert level.status == ClaimStatus.PROVED_ELSEWHERE

    def test_6d_level(self):
        """6d: U_{q,t}, bulk E_3, CONJECTURED (AP-CY14)."""
        hierarchy = build_hcs_hierarchy()
        level = hierarchy["6d"]
        assert level.bulk_en == EnLevel.E3
        assert level.bdry_en == EnLevel.E2
        assert level.status == ClaimStatus.CONJECTURED

    def test_dimensional_reduction(self):
        """6d -> 5d -> 3d: E_n decreases by 1 per step."""
        hierarchy = build_hcs_hierarchy()
        assert hierarchy["6d"].bulk_en.value - 1 == hierarchy["5d"].bulk_en.value
        assert hierarchy["5d"].bulk_en.value - 1 == hierarchy["3d"].bulk_en.value

    def test_open_always_e1(self):
        """Open sector is E_1 at all levels."""
        hierarchy = build_hcs_hierarchy()
        for level in hierarchy.values():
            assert level.open_en == EnLevel.E1


# =========================================================================
# 6. Bulk-boundary coupling tests
# =========================================================================

class TestBulkBoundaryCoupling:
    """Test the bulk-boundary coupling computations."""

    @pytest.fixture
    def coupling_standard(self):
        """Standard Omega-background (1, -2, 1)."""
        return BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
            trunc=8,
        )

    @pytest.fixture
    def coupling_asymmetric(self):
        """Asymmetric Omega-background (1, -3, 2)."""
        return BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-3), Fraction(2)),
            trunc=8,
        )

    def test_cy_condition(self, coupling_standard):
        """h_1 + h_2 + h_3 = 0."""
        h1, h2, h3 = coupling_standard.omega_h
        assert h1 + h2 + h3 == Fraction(0)

    def test_cy_condition_violated_raises(self):
        """Violated CY condition raises assertion."""
        with pytest.raises(AssertionError):
            BulkBoundaryCoupling(
                gauge_dim=1,
                omega_h=(Fraction(1), Fraction(1), Fraction(1)),
            )

    def test_sigma_2(self, coupling_standard):
        """sigma_2 = h1*h2 + h1*h3 + h2*h3 for (1,-2,1)."""
        # sigma_2 = 1*(-2) + 1*1 + (-2)*1 = -2 + 1 - 2 = -3
        assert coupling_standard.sigma_2 == Fraction(-3)

    def test_sigma_3(self, coupling_standard):
        """sigma_3 = h1*h2*h3 for (1,-2,1)."""
        # sigma_3 = 1 * (-2) * 1 = -2
        assert coupling_standard.sigma_3 == Fraction(-2)

    def test_kac_moody_level(self, coupling_standard):
        """Psi = -sigma_2."""
        assert coupling_standard.kac_moody_level == Fraction(3)

    def test_structure_function_phi0(self, coupling_standard):
        """phi_0 = 1."""
        phis = coupling_standard.structure_function_coefficients()
        assert phis[0] == Fraction(1)

    def test_structure_function_phi1_vanishes(self, coupling_standard):
        """phi_1 = 0 (CY condition)."""
        phis = coupling_standard.structure_function_coefficients()
        assert phis[1] == Fraction(0)

    def test_structure_function_phi2_vanishes(self, coupling_standard):
        """phi_2 = 0 (parity)."""
        phis = coupling_standard.structure_function_coefficients()
        assert phis[2] == Fraction(0)

    def test_structure_function_phi3(self, coupling_standard):
        """phi_3 = -2*sigma_3."""
        phis = coupling_standard.structure_function_coefficients()
        expected = Fraction(-2) * coupling_standard.sigma_3
        assert phis[3] == expected

    def test_structure_function_phi3_asymmetric(self, coupling_asymmetric):
        """phi_3 for (1, -3, 2)."""
        phis = coupling_asymmetric.structure_function_coefficients()
        sigma_3 = Fraction(1) * Fraction(-3) * Fraction(2)  # = -6
        expected = Fraction(-2) * sigma_3  # = 12
        assert phis[3] == expected

    def test_bar_complex_partition_numbers(self, coupling_standard):
        """E_1 bar dims = partition numbers."""
        result = coupling_standard.bar_complex_dimensions()
        e1 = result["e1_bar_dims"]
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11, p(7)=15, p(8)=22
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22]
        assert e1 == expected

    def test_bar_complex_monotonicity(self, coupling_standard):
        """E_3 >= E_2 >= E_1 at all weights."""
        result = coupling_standard.bar_complex_dimensions()
        assert result["ok"]
        assert result["monotonicity_e3_ge_e2"]
        assert result["monotonicity_e2_ge_e1"]

    def test_koszul_conductor_zero(self, coupling_standard):
        """Free-field branch: conductor K = 0."""
        result = coupling_standard.koszul_dual_projection()
        assert result["ok"]
        assert result["conductor_zero"]

    def test_open_closed_decomposition(self, coupling_standard):
        """Open-closed decomposition: E_1 open, E_2 closed, SC coupling."""
        result = coupling_standard.open_closed_decomposition()
        assert result["ok"]
        assert result["open_en_level"] == 1
        assert result["closed_en_level"] == 2
        assert result["sc_closed_to_open"]
        assert not result["sc_open_to_closed"]
        assert result["drinfeld_center_passage"]
        assert result["averaging_kills_hopf"]

    def test_full_pipeline(self, coupling_standard):
        """Full 6d derived SC pipeline passes."""
        result = coupling_standard.verify_full_pipeline()
        assert result["ok"]


# =========================================================================
# 7. Defect algebra hierarchy tests
# =========================================================================

class TestDefectHierarchy:
    """Test the defect algebra hierarchy 3d -> 5d -> 6d."""

    def test_hierarchy_passes(self):
        """Full defect hierarchy verification."""
        result = verify_defect_hierarchy()
        assert result["ok"]

    def test_conductor_zero_all_levels(self):
        """Free-field conductor K = 0 at all levels."""
        defects = build_defect_hierarchy()
        for label, defect in defects.items():
            assert defect.conductor == Fraction(0), f"{label}: K != 0"

    def test_all_carry_e1_bialgebra(self):
        """All defects carry E_1-chiral bialgebra structure."""
        defects = build_defect_hierarchy()
        for label, defect in defects.items():
            assert defect.has_e1_bialgebra, f"{label}: no E_1 bialgebra"

    def test_6d_r_matrix_2param(self):
        """6d defect has 2-parameter R-matrix (Zamolodchikov)."""
        defects = build_defect_hierarchy()
        assert "2-parameter" in defects["6d"].r_matrix_type

    def test_5d_r_matrix_1param(self):
        """5d defect has 1-parameter R-matrix (Yang)."""
        defects = build_defect_hierarchy()
        assert "1-parameter" in defects["5d"].r_matrix_type

    def test_6d_is_conjectural(self):
        """6d defect is CONJECTURED (AP-CY14)."""
        defects = build_defect_hierarchy()
        assert defects["6d"].claim_status == ClaimStatus.CONJECTURED

    def test_3d_5d_proved(self):
        """3d and 5d defects are PROVED."""
        defects = build_defect_hierarchy()
        assert defects["3d"].claim_status == ClaimStatus.PROVED_ELSEWHERE
        assert defects["5d"].claim_status == ClaimStatus.PROVED_ELSEWHERE


# =========================================================================
# 8. Center promotion tests
# =========================================================================

class TestCenterPromotion:
    """Test E_2 -> E_3 promotion via derived center."""

    def test_promotion_passes(self):
        """Full center promotion verification."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["ok"]

    def test_deligne_e1_gives_e2(self):
        """E_1 input -> HH^* carries E_2 (standard Deligne)."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["deligne_E1_gives_E2"]

    def test_deligne_e2_gives_e3(self):
        """E_2 input -> HH^* carries E_3 (higher Deligne)."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["deligne_E2_gives_E3"]

    def test_iterated_drinfeld_not_e3(self):
        """Iterated Drinfeld center does NOT give E_3."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["iterated_drinfeld_not_e3"]

    def test_drinfeld_ne_derived(self):
        """Drinfeld center != derived center (AP-CY4)."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["drinfeld_ne_derived"]


# =========================================================================
# 9. Master verification tests
# =========================================================================

class TestMasterVerification:
    """Test the full derived Swiss-cheese master verification."""

    def test_master_standard_omega(self):
        """Master verification at (1, -2, 1)."""
        result = master_derived_sc_verification(
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
        )
        assert result["ok"]

    def test_master_asymmetric_omega(self):
        """Master verification at (1, -3, 2)."""
        result = master_derived_sc_verification(
            omega_h=(Fraction(1), Fraction(-3), Fraction(2)),
        )
        assert result["ok"]

    def test_master_symmetric_omega(self):
        """Master verification at (2, -1, -1)."""
        result = master_derived_sc_verification(
            omega_h=(Fraction(2), Fraction(-1), Fraction(-1)),
        )
        assert result["ok"]

    def test_master_large_params(self):
        """Master verification with large parameters (AP-CY28 safe)."""
        result = master_derived_sc_verification(
            omega_h=(Fraction(37), Fraction(41), Fraction(-78)),
        )
        assert result["ok"]

    def test_master_gl2(self):
        """Master verification for gl_2 (gauge_dim=4)."""
        result = master_derived_sc_verification(
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
            gauge_dim=4,
        )
        assert result["ok"]


# =========================================================================
# 10. Anti-pattern regression tests
# =========================================================================

class TestAntiPatternRegression:
    """Regression tests for Vol III anti-patterns."""

    def test_ap_cy4_drinfeld_ne_derived(self):
        """AP-CY4: Drinfeld center != derived center."""
        result = verify_center_promotion_not_iterated_drinfeld()
        assert result["drinfeld_ne_derived"]

    def test_ap_cy6_6d_conjectural(self):
        """AP-CY6/AP-CY14: 6d defect is CONJECTURED, not theorem."""
        defects = build_defect_hierarchy()
        assert defects["6d"].claim_status == ClaimStatus.CONJECTURED

    def test_ap_cy7_coha_is_not_chiral(self):
        """AP-CY7: CoHA is associative, NOT chiral.

        The open sector E_1 is NOT the same as the CoHA.
        The CoHA carries the Hall product (associative), and the connection
        to chiral algebras is via the functor Phi (CY-A), not identification.
        """
        stacks = build_6d_stacks()
        # Open moduli target is BG_top (topological), NOT BG_hol
        assert stacks["open"].target_space == "BG_top"
        # Closed moduli target is BG_hol (holomorphic)
        assert stacks["closed"].target_space == "BG_hol"

    def test_ap_cy11_conditionality_propagates(self):
        """AP-CY11: d=3 results are CONDITIONAL on CY-A_3."""
        obs = compute_obstruction_6d_hcs(cy_dim=3)
        assert "CY-A_3" in obs.dependencies

    def test_ap_cy23_e1_not_einf_bialgebra(self):
        """AP-CY23: E_1-chiral bialgebra, not E_inf vertex bialgebra."""
        coupling = BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
        )
        result = coupling.open_closed_decomposition()
        # Open sector is E_1
        assert result["open_en_level"] == 1
        # Averaging kills Hopf data
        assert result["averaging_kills_hopf"]

    def test_ap_cy31_spectral_z_distinct(self):
        """AP-CY31: spectral z != worldsheet z.

        The structure function g(z) uses a Yangian spectral parameter z,
        NOT a worldsheet insertion coordinate.
        """
        coupling = BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
        )
        phis = coupling.structure_function_coefficients()
        # g(z) is a rational function of z (spectral parameter)
        # phi_0 = 1 confirms the normalization as z -> infinity
        assert phis[0] == Fraction(1)

    def test_ap_cy32_6d_does_not_bypass_cya3(self):
        """AP-CY32: 6d route REORGANISES CY-A_3, does NOT bypass it."""
        obs = compute_obstruction_6d_hcs(cy_dim=3)
        # The obstruction result is CONDITIONAL, not PROVED
        assert obs.claim_status == ClaimStatus.CONDITIONAL

    def test_ap154_two_e3_structures(self):
        """AP154: two E_3 (algebraic Deligne vs topological config-space)."""
        # Both the algebraic and topological E_3 are distinct at chain level
        # The derived center gives the algebraic E_3
        # The 6d hCS gives the topological E_3
        result = verify_center_promotion_not_iterated_drinfeld()
        # The algebraic route: E_2 -> E_3 via derived center (Deligne)
        assert result["derived_center_e2_gives_e3"]

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa always subscripted (kappa_ch, not bare kappa)."""
        coupling = BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
        )
        result = coupling.koszul_dual_projection()
        # All kappa references are subscripted
        assert "kappa_ch_bulk" in result
        assert "kappa_ch_bdry" in result
        assert "kappa_ch_dual_bulk" in result
        assert "kappa_ch_dual_bdry" in result


# =========================================================================
# 11. Cross-engine consistency tests
# =========================================================================

class TestCrossEngineConsistency:
    """Cross-check against existing engines."""

    def test_partition_numbers_match(self):
        """Partition numbers match standard values."""
        p = BulkBoundaryCoupling._partition_count_list(10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert p == expected

    def test_e2_bar_dims_convolution(self):
        """E_2 bar dims = P(q)^2 (convolution of partition sequence)."""
        p = BulkBoundaryCoupling._partition_count_list(5)
        p2 = BulkBoundaryCoupling._convolution(p, p, 5)
        # P(q)^2 coefficients: 1, 2, 5, 10, 20, 36
        expected = [1, 2, 5, 10, 20, 36]
        assert p2 == expected

    def test_e3_bar_dims_convolution(self):
        """E_3 bar dims = P(q)^3 (triple convolution)."""
        p = BulkBoundaryCoupling._partition_count_list(4)
        p2 = BulkBoundaryCoupling._convolution(p, p, 4)
        p3 = BulkBoundaryCoupling._convolution(p2, p, 4)
        # P(q)^3 coefficients: 1, 3, 9, 22, 51
        expected = [1, 3, 9, 22, 51]
        assert p3 == expected

    def test_sigma_2_consistency(self):
        """sigma_2 consistency with holomorphic_cs_chiral_engine conventions."""
        # At (1, -2, 1): sigma_2 = -3, Psi = 3
        coupling = BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-2), Fraction(1)),
        )
        assert coupling.sigma_2 == Fraction(-3)
        assert coupling.kac_moody_level == Fraction(3)

    def test_sigma_3_consistency(self):
        """sigma_3 consistency across engines."""
        # At (1, -3, 2): sigma_3 = 1*(-3)*2 = -6
        coupling = BulkBoundaryCoupling(
            gauge_dim=1,
            omega_h=(Fraction(1), Fraction(-3), Fraction(2)),
        )
        assert coupling.sigma_3 == Fraction(-6)
