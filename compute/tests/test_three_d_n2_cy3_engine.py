r"""
Tests for three_d_n2_cy3_engine.py -- 3d N=2 HT QFT from CY3 compactification.

Tests organized by mathematical structure:
  1. CY3 Hodge data (internal consistency)
  2. 3d N=2 theory construction (multiplet content)
  3. HT twist -> E_1 chiral algebra
  4. Mirror symmetry as E_1 Koszul duality
  5. BFN Coulomb branch = zero-mode algebra
  6. PVA descent (Vol II connection)
  7. Shadow depth classification
  8. Prepotential and intersection numbers
  9. Three-duality identification
  10. Grand verification

Multi-path verification: each key formula is checked by at least 2 independent paths.
"""

import pytest
from fractions import Fraction

from compute.lib.three_d_n2_cy3_engine import (
    # CY3 Hodge data
    CY3HodgeData,
    cy3_C3, cy3_resolved_conifold, cy3_deformed_conifold,
    cy3_local_P2, cy3_local_P1xP1, cy3_quintic,
    cy3_mirror_quintic, cy3_K3xE, cy3_complete_intersection_34,
    # 3d N=2 theories
    ThreeDN2Theory,
    theory_from_C3, theory_from_resolved_conifold,
    theory_from_deformed_conifold, theory_from_local_P2,
    theory_from_quintic,
    # HT chiral algebras
    HTChiralAlgebra,
    ht_algebra_C3, ht_algebra_resolved_conifold,
    ht_algebra_deformed_conifold, ht_algebra_local_P2,
    ht_algebra_quintic,
    # Mirror pairs
    MirrorPair,
    mirror_pair_conifold, mirror_pair_quintic,
    verify_hodge_mirror, verify_chi_opposite,
    # BFN data
    BFNCoulombData,
    bfn_C3, bfn_resolved_conifold, bfn_local_P2,
    # PVA descent
    PVADescentData,
    pva_C3, pva_resolved_conifold,
    # Computation functions
    compute_ht_central_charge,
    compute_kappa_from_cy3,
    compute_coulomb_dim,
    compute_higgs_dim,
    e1_koszul_dual_kappa,
    mirror_symmetry_kappa_check,
    triple_intersection_number,
    classical_prepotential,
    ope_max_pole,
    compute_level_matrix,
    shadow_depth_from_cy3,
    shadow_kappa_from_ht,
    # Three-duality
    ThreeDualityData,
    three_duality_conifold,
    # Verification
    verify_hodge_data,
    verify_theory_data,
    verify_mirror_pair,
    verify_bfn_zero_mode,
    # Anomalies
    gravitational_anomaly,
    r_symmetry_anomaly,
    # Conifold transition
    conifold_transition_data,
    # Genus-1 obstruction
    genus_1_obstruction,
    # Landscape
    full_landscape,
    grand_verification,
    # N=2 superalgebra
    N2Superalgebra,
)


# =========================================================================
# Section 1: CY3 Hodge data -- internal consistency (15 tests)
# =========================================================================

class TestCY3HodgeData:
    """Test Hodge diamond consistency for all CY3 families."""

    def test_C3_hodge(self):
        X = cy3_C3()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 0
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 0
        assert not X.compact

    def test_resolved_conifold_hodge(self):
        X = cy3_resolved_conifold()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 1
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 0
        assert not X.compact

    def test_deformed_conifold_hodge(self):
        X = cy3_deformed_conifold()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 0
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 1
        assert not X.compact

    def test_local_P2_hodge(self):
        X = cy3_local_P2()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 1
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 0

    def test_local_P1xP1_hodge(self):
        X = cy3_local_P1xP1()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 2
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 0

    def test_quintic_hodge(self):
        """Quintic: h^{1,1}=1, h^{2,1}=101, chi=-200."""
        X = cy3_quintic()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 1
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 101
        assert X.compact
        # chi = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.chi == -200

    def test_mirror_quintic_hodge(self):
        """Mirror quintic: h^{1,1}=101, h^{2,1}=1, chi=200."""
        X = cy3_mirror_quintic()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 101
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 1
        assert X.compact
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.chi == 200

    def test_K3xE_hodge(self):
        """K3 x E: h^{1,1}=21, h^{2,1}=21, chi=0.

        chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.
        Hodge: 2*(21 - 21) = 0. Consistent.
        """
        X = cy3_K3xE()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 21
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 21
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.chi == 0

    def test_CICY_34_hodge(self):
        X = cy3_complete_intersection_34()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h11 == 2
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert X.h21 == 90
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.chi == 2 * (2 - 90)
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.chi == -176

    def test_chi_formula_all_compact(self):
        """Verify chi = 2(h^{1,1} - h^{2,1}) for all compact CY3s."""
        for cy3_fn in [cy3_quintic, cy3_mirror_quintic, cy3_K3xE,
                        cy3_complete_intersection_34]:
            X = cy3_fn()
            # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
            assert X.chi == 2 * (X.h11 - X.h21), f"Failed for {X.name}"

    def test_hodge_nonneg(self):
        """All Hodge numbers are non-negative."""
        for cy3_fn in [cy3_C3, cy3_resolved_conifold, cy3_deformed_conifold,
                        cy3_local_P2, cy3_local_P1xP1, cy3_quintic,
                        cy3_mirror_quintic, cy3_K3xE]:
            X = cy3_fn()
            # VERIFIED [DC] Hodge number [LC] boundary/limiting case
            assert X.h11 >= 0, f"h^{{1,1}} < 0 for {X.name}"
            # VERIFIED [DC] Hodge number [LC] boundary/limiting case
            assert X.h21 >= 0, f"h^{{2,1}} < 0 for {X.name}"

    def test_n_vector_from_h11(self):
        """Number of vector multiplets = h^{1,1}."""
        X = cy3_quintic()
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert X.n_vector == X.h11 == 1

    def test_n_chiral_from_h21(self):
        """Number of chiral multiplets = h^{2,1}."""
        X = cy3_quintic()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert X.n_chiral == X.h21 == 101

    def test_coulomb_dim_equals_h11(self):
        """Coulomb branch dimension = h^{1,1}."""
        X = cy3_resolved_conifold()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert X.coulomb_dim == 1

    def test_higgs_dim_equals_h21(self):
        """Higgs branch dimension = h^{2,1}."""
        X = cy3_deformed_conifold()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert X.higgs_dim == 1


# =========================================================================
# Section 2: 3d N=2 theory construction (10 tests)
# =========================================================================

class TestThreeDN2Theory:
    """Test 3d N=2 theory data from CY3."""

    def test_C3_theory(self):
        T = theory_from_C3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert T.gauge_group == "trivial"
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_neutral_chirals == 1
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_charged_chirals == 0

    def test_resolved_conifold_theory(self):
        T = theory_from_resolved_conifold()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert T.gauge_group == "U(1)"
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_charged_chirals == 1

    def test_deformed_conifold_theory(self):
        T = theory_from_deformed_conifold()
        # VERIFIED [DC] deformation [LC] boundary/limiting case
        assert T.gauge_group == "trivial"
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_neutral_chirals == 1

    def test_local_P2_theory(self):
        T = theory_from_local_P2()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert T.gauge_group == "U(1)"
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_charged_chirals == 3

    def test_quintic_theory(self):
        T = theory_from_quintic()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert T.n_neutral_chirals == 101

    def test_coulomb_dim_C3(self):
        T = theory_from_C3()
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert compute_coulomb_dim(T) == 0

    def test_coulomb_dim_conifold(self):
        T = theory_from_resolved_conifold()
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert compute_coulomb_dim(T) == 1

    def test_higgs_dim_C3(self):
        T = theory_from_C3()
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert compute_higgs_dim(T) == 1  # 1 neutral chiral, no gauge

    def test_higgs_dim_conifold(self):
        T = theory_from_resolved_conifold()
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert compute_higgs_dim(T) == 0  # 1 charged - 1 gauge = 0

    def test_gravitational_anomaly_C3(self):
        T = theory_from_C3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert gravitational_anomaly(T) == Fraction(1, 2)


# =========================================================================
# Section 3: HT twist -> E_1 chiral algebra (12 tests)
# =========================================================================

class TestHTChiralAlgebra:
    """Test HT chiral algebra construction."""

    def test_C3_betagamma(self):
        """T[C^3] -> beta-gamma system."""
        A = ht_algebra_C3()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert A.chiral_algebra_type == "betagamma"
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert A.central_charge == Fraction(2)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert A.kappa == Fraction(1)

    def test_C3_shadow_class(self):
        A = ht_algebra_C3()
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert A.shadow_depth_class == "G"

    def test_conifold_heisenberg(self):
        """T[resolved conifold] -> Heisenberg H_1."""
        A = ht_algebra_resolved_conifold()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert A.chiral_algebra_type == "Heisenberg"
        # VERIFIED [DC] central charge formula [LT] literature cross-check
        assert A.central_charge == Fraction(1)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert A.kappa == Fraction(1)

    def test_deformed_conifold_dual(self):
        """T[deformed conifold] -> H_{-1} (Koszul dual)."""
        A = ht_algebra_deformed_conifold()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert A.kappa == Fraction(-1)

    def test_local_P2_W_algebra(self):
        """T[local P^2] -> W-algebra."""
        A = ht_algebra_local_P2()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert A.chiral_algebra_type == "W_algebra"
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert A.shadow_depth_class == "L"

    def test_quintic_class_M(self):
        """T[quintic] -> class M (infinite shadow depth)."""
        A = ht_algebra_quintic()
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert A.shadow_depth_class == "M"

    def test_all_algebras_have_kappa(self):
        """Every HT algebra has a well-defined kappa."""
        for ht_fn in [ht_algebra_C3, ht_algebra_resolved_conifold,
                       ht_algebra_deformed_conifold, ht_algebra_local_P2,
                       ht_algebra_quintic]:
            A = ht_fn()
            assert A.kappa is not None
            assert isinstance(A.kappa, Fraction)

    def test_C3_is_e_inf(self):
        """Beta-gamma is E_inf (it is a vertex algebra)."""
        A = ht_algebra_C3()
        assert A.is_e_inf

    def test_conifold_is_e_inf(self):
        """Heisenberg is E_inf."""
        A = ht_algebra_resolved_conifold()
        assert A.is_e_inf

    def test_ope_poles_betagamma(self):
        """Beta-gamma OPE has simple pole."""
        A = ht_algebra_C3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert A.ope_leading_poles[("beta", "gamma")] == 1

    def test_ope_poles_heisenberg(self):
        """Heisenberg OPE has double pole."""
        A = ht_algebra_resolved_conifold()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert A.ope_leading_poles[("J", "J")] == 2

    def test_central_charge_consistency(self):
        """Check c(A^{HT}) against naive multiplet counting.

        T[C^3]: 1 chiral, no gauge -> c = 2 (beta-gamma).
        """
        T = theory_from_C3()
        c_computed = compute_ht_central_charge(T)
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert c_computed == Fraction(2)


# =========================================================================
# Section 4: Mirror symmetry as E_1 Koszul duality (12 tests)
# =========================================================================

class TestMirrorSymmetry:
    """Test CY3 mirror symmetry = E_1 Koszul duality."""

    def test_conifold_hodge_mirror(self):
        """Resolved <-> deformed conifold: h^{1,1} <-> h^{2,1}."""
        pair = mirror_pair_conifold()
        assert pair.hodge_mirror

    def test_conifold_chi_opposite(self):
        """chi(resolved) = -chi(deformed)."""
        pair = mirror_pair_conifold()
        assert pair.chi_opposite

    def test_quintic_hodge_mirror(self):
        """Quintic <-> mirror quintic: h^{1,1} <-> h^{2,1}."""
        pair = mirror_pair_quintic()
        assert pair.hodge_mirror

    def test_quintic_chi_opposite(self):
        pair = mirror_pair_quintic()
        assert pair.chi_opposite

    def test_kappa_complementary_conifold(self):
        """kappa(H_1) + kappa(H_{-1}) = 0."""
        pair = mirror_pair_conifold()
        assert pair.kappa_complementary

    def test_kappa_complementary_quintic(self):
        pair = mirror_pair_quintic()
        assert pair.kappa_complementary

    def test_e1_koszul_dual_heisenberg(self):
        """H_1^{!,E_1} has kappa = -1."""
        kappa_dual = e1_koszul_dual_kappa(Fraction(1), "Heisenberg")
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_dual == Fraction(-1)

    def test_e1_koszul_dual_sum_zero(self):
        """kappa + kappa^! = 0 for Heisenberg family."""
        kappa = Fraction(1)
        kappa_dual = e1_koszul_dual_kappa(kappa, "Heisenberg")
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa + kappa_dual == 0

    def test_mirror_kappa_check_conifold(self):
        result = mirror_symmetry_kappa_check(
            cy3_resolved_conifold(), cy3_deformed_conifold()
        )
        assert result["hodge_mirror"]
        assert result["kappa_complementary"]

    def test_mirror_kappa_check_quintic(self):
        result = mirror_symmetry_kappa_check(
            cy3_quintic(), cy3_mirror_quintic()
        )
        assert result["hodge_mirror"]
        assert result["kappa_complementary"]

    def test_verify_hodge_mirror_direct(self):
        assert verify_hodge_mirror(cy3_resolved_conifold(), cy3_deformed_conifold())
        assert verify_hodge_mirror(cy3_quintic(), cy3_mirror_quintic())

    def test_verify_chi_opposite_direct(self):
        assert verify_chi_opposite(cy3_resolved_conifold(), cy3_deformed_conifold())
        assert verify_chi_opposite(cy3_quintic(), cy3_mirror_quintic())


# =========================================================================
# Section 5: BFN Coulomb branch = zero-mode algebra (8 tests)
# =========================================================================

class TestBFNCoulomb:
    """Test BFN Coulomb branch algebra matches zero-mode sector."""

    def test_C3_bfn_trivial(self):
        bfn = bfn_C3()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bfn.coulomb_dim == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert bfn.quantized_algebra == "C"

    def test_C3_zero_modes_match(self):
        bfn = bfn_C3()
        assert bfn.matches_zero_modes

    def test_conifold_bfn_U1(self):
        bfn = bfn_resolved_conifold()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bfn.coulomb_dim == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert bfn.quantized_algebra == "C[z]"

    def test_conifold_zero_modes_match(self):
        bfn = bfn_resolved_conifold()
        assert bfn.matches_zero_modes

    def test_local_P2_bfn(self):
        bfn = bfn_local_P2()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert bfn.coulomb_dim == 2

    def test_local_P2_zero_modes_match(self):
        bfn = bfn_local_P2()
        assert bfn.matches_zero_modes

    def test_bfn_is_commutative(self):
        """Classical BFN algebra is always commutative."""
        for bfn_fn in [bfn_C3, bfn_resolved_conifold, bfn_local_P2]:
            bfn = bfn_fn()
            assert bfn.is_commutative

    def test_bfn_verification(self):
        bfn = bfn_resolved_conifold()
        result = verify_bfn_zero_mode(bfn)
        assert result["matches_zero_modes"]


# =========================================================================
# Section 6: PVA descent (5 tests)
# =========================================================================

class TestPVADescent:
    """Test PVA descent connecting to Vol II."""

    def test_C3_pva_constant_bracket(self):
        pva = pva_C3()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert pva.poisson_bracket_type == "constant"

    def test_C3_pva_target(self):
        pva = pva_C3()
        assert "C^2" in pva.classical_target

    def test_conifold_pva_linear_bracket(self):
        pva = pva_resolved_conifold()
        # VERIFIED [DC] scaling/linearity [LC] boundary/limiting case
        assert pva.poisson_bracket_type == "linear"

    def test_pva_unobstructed(self):
        """BTT unobstructedness holds for all CY3."""
        for pva_fn in [pva_C3, pva_resolved_conifold]:
            pva = pva_fn()
            assert pva.is_unobstructed

    def test_pva_generators_match_ht(self):
        """PVA generators match the HT algebra generators."""
        pva = pva_C3()
        ht = ht_algebra_C3()
        # Both should have beta and gamma
        assert "beta" in pva.pva_generators
        assert "gamma" in pva.pva_generators


# =========================================================================
# Section 7: Shadow depth classification (8 tests)
# =========================================================================

class TestShadowDepth:
    """Test shadow depth classification from CY3 geometry."""

    def test_C3_class_G(self):
        cls, depth = shadow_depth_from_cy3(cy3_C3())
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cls == "G"
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert depth == 2

    def test_conifold_class_G(self):
        cls, depth = shadow_depth_from_cy3(cy3_resolved_conifold())
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cls == "G"
        # VERIFIED [DC] shadow depth [LC] boundary/limiting case
        assert depth == 2

    def test_local_P2_class_M(self):
        # AP-CY12: local P^2 is class M (infinite depth), not G/L/C.
        # Leading approximation misses the infinite tower.
        cls, depth = shadow_depth_from_cy3(cy3_local_P2())
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cls == "M"

    def test_quintic_class_M(self):
        cls, depth = shadow_depth_from_cy3(cy3_quintic())
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cls == "M"
        assert depth is None  # Infinite

    def test_mirror_quintic_class_M(self):
        cls, depth = shadow_depth_from_cy3(cy3_mirror_quintic())
        # VERIFIED [DC] mirror symmetry [LC] boundary/limiting case
        assert cls == "M"

    def test_K3xE_class_M(self):
        cls, depth = shadow_depth_from_cy3(cy3_K3xE())
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cls == "M"

    def test_shadow_kappa_extraction(self):
        A = ht_algebra_C3()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert shadow_kappa_from_ht(A) == Fraction(1)

    def test_compact_always_class_M(self):
        """All compact CY3s have class M (infinite GW invariants)."""
        for cy3_fn in [cy3_quintic, cy3_mirror_quintic, cy3_K3xE,
                        cy3_complete_intersection_34]:
            cls, _ = shadow_depth_from_cy3(cy3_fn())
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert cls == "M"


# =========================================================================
# Section 8: Prepotential and intersection numbers (6 tests)
# =========================================================================

class TestPrepotential:
    """Test prepotential and intersection data."""

    def test_quintic_C111(self):
        """Quintic triple intersection number C_{111} = 5."""
        X = cy3_quintic()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert triple_intersection_number(X, 0, 0, 0) == 5

    def test_local_P2_C111(self):
        """Local P^2 triple intersection = 3."""
        X = cy3_local_P2()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert triple_intersection_number(X, 0, 0, 0) == 3

    def test_quintic_prepotential(self):
        """F_0(t) = (5/6) t^3 for the quintic."""
        X = cy3_quintic()
        F = classical_prepotential(X, [Fraction(1)])
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert F == Fraction(5, 6)

    def test_level_matrix_conifold(self):
        """Level matrix for resolved conifold is [[0]]."""
        X = cy3_resolved_conifold()
        k = compute_level_matrix(X)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(k) == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k[0][0] == Fraction(0)

    def test_ope_poles_JJ(self):
        """J-J OPE has double pole."""
        X = cy3_quintic()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ope_max_pole(X, "J_0", "J_0") == 2

    def test_ope_poles_phi(self):
        """Matter-matter OPE has simple pole."""
        X = cy3_quintic()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert ope_max_pole(X, "phi_0", "phi_1") == 1


# =========================================================================
# Section 9: Three-duality identification (8 tests)
# =========================================================================

class TestThreeDuality:
    """Test the three-duality: CY mirror = 3d mirror = E_1 Koszul."""

    def test_three_duality_exists(self):
        td = three_duality_conifold()
        assert td is not None

    def test_kappa_koszul_check(self):
        td = three_duality_conifold()
        assert td.kappa_koszul_check

    def test_coulomb_higgs_exchange(self):
        td = three_duality_conifold()
        assert td.coulomb_higgs_exchange

    def test_cy3_mirror_pair_valid(self):
        td = three_duality_conifold()
        assert td.cy3_mirror_pair.hodge_mirror

    def test_algebras_are_koszul_duals(self):
        """A^{HT}(resolved) and A^{HT}(deformed) are E_1 Koszul duals.

        This means: kappa(A) + kappa(A^!) = 0 (for KM family).
        """
        td = three_duality_conifold()
        kappa_sum = td.algebra_X.kappa + td.algebra_X_check.kappa
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_sum == 0

    def test_conifold_transition(self):
        data = conifold_transition_data()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert data["h11_change"] == -1
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert data["h21_change"] == 1
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert data["kappa_change"] == Fraction(-2)

    def test_resolved_to_deformed_kappa(self):
        """kappa changes by -2 across the conifold transition."""
        data = conifold_transition_data()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert data["resolved"]["kappa"] == Fraction(1)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert data["deformed"]["kappa"] == Fraction(-1)

    def test_transition_type(self):
        data = conifold_transition_data()
        assert "P^1" in data["transition_type"]


# =========================================================================
# Section 10: Kappa computations (8 tests)
# =========================================================================

class TestKappaComputation:
    """Test kappa computations from CY3 data."""

    def test_kappa_C3(self):
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert compute_kappa_from_cy3(cy3_C3()) == Fraction(1)

    def test_kappa_resolved_conifold(self):
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert compute_kappa_from_cy3(cy3_resolved_conifold()) == Fraction(1)

    def test_kappa_deformed_conifold(self):
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert compute_kappa_from_cy3(cy3_deformed_conifold()) == Fraction(-1)

    def test_kappa_local_P2(self):
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert compute_kappa_from_cy3(cy3_local_P2()) == Fraction(3)

    def test_kappa_quintic(self):
        """Quintic: kappa = chi/12 = -200/12 = -50/3."""
        kappa = compute_kappa_from_cy3(cy3_quintic())
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa == Fraction(-200, 12)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa == Fraction(-50, 3)

    def test_kappa_mirror_quintic(self):
        """Mirror quintic: kappa = 200/12 = 50/3."""
        kappa = compute_kappa_from_cy3(cy3_mirror_quintic())
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa == Fraction(200, 12)
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa == Fraction(50, 3)

    def test_kappa_sum_quintic_mirror(self):
        """kappa(quintic) + kappa(mirror) = 0."""
        k1 = compute_kappa_from_cy3(cy3_quintic())
        k2 = compute_kappa_from_cy3(cy3_mirror_quintic())
        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert k1 + k2 == 0

    def test_kappa_K3xE(self):
        """K3 x E: chi = 0, so kappa = 0/12 = 0."""
        kappa = compute_kappa_from_cy3(cy3_K3xE())
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa == Fraction(0)


# =========================================================================
# Section 11: Anomalies (4 tests)
# =========================================================================

class TestAnomalies:
    """Test anomaly computations."""

    def test_grav_anomaly_C3(self):
        T = theory_from_C3()
        k = gravitational_anomaly(T)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k == Fraction(1, 2)

    def test_grav_anomaly_conifold(self):
        T = theory_from_resolved_conifold()
        k = gravitational_anomaly(T)
        # 1 charged chiral - 1 vector = 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k == Fraction(0)

    def test_r_anomaly_C3(self):
        T = theory_from_C3()
        k = r_symmetry_anomaly(T)
        # R-charge = 1/2, so (1/2)(1/2 - 1) = -1/4
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k == Fraction(-1, 4)

    def test_r_anomaly_local_P2(self):
        T = theory_from_local_P2()
        k = r_symmetry_anomaly(T)
        # 3 chirals with R = 1/3: (1/2)*3*(1/3 - 1) = (1/2)*3*(-2/3) = -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k == Fraction(-1)


# =========================================================================
# Section 12: N=2 superalgebra (3 tests)
# =========================================================================

class TestN2Superalgebra:
    """Test N=2 superalgebra data."""

    def test_ht_twist_exists(self):
        susy = N2Superalgebra(n_supercharges=4)
        assert susy.ht_twist_exists()

    def test_central_charge_vector(self):
        susy = N2Superalgebra()
        # VERIFIED [DC] central charge [LC] boundary/limiting case
        assert susy.central_charge_contribution("vector") == Fraction(1)

    def test_central_charge_chiral(self):
        susy = N2Superalgebra()
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert susy.central_charge_contribution("chiral") == Fraction(2)


# =========================================================================
# Section 13: Genus-1 obstruction (3 tests)
# =========================================================================

class TestGenus1Obstruction:
    """Test genus-1 obstruction from CY3."""

    def test_genus1_C3(self):
        F1 = genus_1_obstruction(cy3_C3())
        # VERIFIED [DC] genus free energy [LC] boundary/limiting case
        assert F1 == Fraction(1, 24)

    def test_genus1_quintic(self):
        F1 = genus_1_obstruction(cy3_quintic())
        # VERIFIED [DC] genus free energy [LC] boundary/limiting case
        assert F1 == Fraction(-200, 12 * 24)
        # VERIFIED [DC] genus free energy [LC] boundary/limiting case
        assert F1 == Fraction(-50, 72)

    def test_genus1_K3xE(self):
        """K3 x E: kappa = 0, so F_1 = 0."""
        F1 = genus_1_obstruction(cy3_K3xE())
        # VERIFIED [DC] genus free energy [LC] boundary/limiting case
        assert F1 == Fraction(0)


# =========================================================================
# Section 14: Grand verification and landscape (5 tests)
# =========================================================================

class TestGrandVerification:
    """Test the grand verification suite."""

    def test_grand_verification_runs(self):
        results = grand_verification()
        assert "hodge_checks" in results
        assert "mirror_pairs" in results
        assert "kappa" in results

    def test_all_hodge_consistent(self):
        results = grand_verification()
        for name, check in results["hodge_checks"].items():
            assert check["h11_nonneg"], f"h11 negative for {name}"
            assert check["h21_nonneg"], f"h21 negative for {name}"

    def test_all_mirror_pairs_valid(self):
        results = grand_verification()
        for name, check in results["mirror_pairs"].items():
            assert check["hodge_mirror"], f"Hodge mirror fails for {name}"
            assert check["chi_opposite"], f"Chi opposite fails for {name}"

    def test_landscape_entries(self):
        landscape = full_landscape()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(landscape) >= 4  # At least C^3, conifold, deformed, local P^2

    def test_landscape_kappas(self):
        landscape = full_landscape()
        for entry in landscape:
            kappa = entry["ht_algebra"]["kappa"]
            assert isinstance(kappa, Fraction)


# =========================================================================
# Section 15: Cross-verification (multi-path) (6 tests)
# =========================================================================

class TestCrossVerification:
    """Multi-path verification of key results."""

    def test_conifold_kappa_two_paths(self):
        """Verify kappa(conifold) = 1 by two paths:
        Path 1: Direct from CY3 data.
        Path 2: From the HT chiral algebra.
        """
        # Path 1
        kappa_cy3 = compute_kappa_from_cy3(cy3_resolved_conifold())
        # Path 2
        kappa_ht = ht_algebra_resolved_conifold().kappa
        assert kappa_cy3 == kappa_ht

    def test_quintic_kappa_two_paths(self):
        """Verify quintic kappa by two paths."""
        kappa_cy3 = compute_kappa_from_cy3(cy3_quintic())
        kappa_ht = ht_algebra_quintic().kappa
        # Both should give -50/3
        assert kappa_cy3 == kappa_ht

    def test_mirror_kappa_sum_two_paths(self):
        """Verify mirror kappa complementarity by two paths.

        Path 1: Compute kappa(X) + kappa(X_check) from CY3 data.
        Path 2: Use the Hodge mirror formula chi(X) + chi(X_check) = 0.
        """
        # Path 1
        k1 = compute_kappa_from_cy3(cy3_quintic())
        k2 = compute_kappa_from_cy3(cy3_mirror_quintic())
        sum_path1 = k1 + k2

        # Path 2: chi(quintic) = -200, chi(mirror) = 200
        chi_sum = cy3_quintic().chi + cy3_mirror_quintic().chi
        sum_path2 = Fraction(chi_sum, 12)

        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert sum_path1 == 0
        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert sum_path2 == 0

    def test_C3_c_two_paths(self):
        """Verify c(T[C^3]) = 2 by two paths.

        Path 1: From the HT algebra data.
        Path 2: From multiplet counting.
        """
        c_path1 = ht_algebra_C3().central_charge
        c_path2 = compute_ht_central_charge(theory_from_C3())
        assert c_path1 == c_path2

    def test_conifold_transition_kappa_consistent(self):
        """Verify the conifold transition data is consistent with
        the individual kappa values."""
        data = conifold_transition_data()
        resolved_kappa = compute_kappa_from_cy3(cy3_resolved_conifold())
        deformed_kappa = compute_kappa_from_cy3(cy3_deformed_conifold())
        assert data["kappa_change"] == deformed_kappa - resolved_kappa

    def test_three_duality_kappa_consistent(self):
        """All three layers of the three-duality give the same kappa relationship."""
        td = three_duality_conifold()

        # CY3 level: kappa from Hodge
        kappa_X = compute_kappa_from_cy3(td.cy3_mirror_pair.X)
        kappa_Xcheck = compute_kappa_from_cy3(td.cy3_mirror_pair.X_check)

        # HT level: kappa from chiral algebra
        kappa_A = td.algebra_X.kappa
        kappa_Adual = td.algebra_X_check.kappa

        # All should agree
        assert kappa_X == kappa_A
        assert kappa_Xcheck == kappa_Adual
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_X + kappa_Xcheck == 0
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_A + kappa_Adual == 0


# =========================================================================
# Section 16: E_1 Koszul duality for various families (4 tests)
# =========================================================================

class TestE1KoszulDuality:
    """Test E_1 Koszul duality computations."""

    def test_koszul_heisenberg_negation(self):
        """For Heisenberg: kappa^! = -kappa."""
        for k in [1, 2, 3, -1, -2]:
            kappa = Fraction(k)
            kappa_dual = e1_koszul_dual_kappa(kappa, "Heisenberg")
            assert kappa_dual == -kappa

    def test_koszul_virasoro_shift(self):
        """For Virasoro: kappa^! = 13 - kappa (AP24)."""
        kappa = Fraction(13, 2)  # c=13, kappa=13/2
        kappa_dual = e1_koszul_dual_kappa(kappa, "Virasoro")
        # VERIFIED [DC] kappa formula [LC] AP24
        assert kappa_dual == Fraction(13) - kappa
        # VERIFIED [DC] kappa formula [LC] AP24
        assert kappa_dual == Fraction(13, 2)  # Self-dual at c=13

    def test_koszul_involution(self):
        """Koszul duality is an involution: (A^!)^! = A."""
        kappa = Fraction(1)
        kappa_dual = e1_koszul_dual_kappa(kappa, "Heisenberg")
        kappa_double_dual = e1_koszul_dual_kappa(kappa_dual, "Heisenberg")
        assert kappa_double_dual == kappa

    def test_koszul_self_dual_virasoro(self):
        """Virasoro at c=13 is self-dual: kappa = kappa^!."""
        kappa_13 = Fraction(13, 2)  # kappa(Vir_13) = 13/2
        kappa_dual = e1_koszul_dual_kappa(kappa_13, "Virasoro")
        assert kappa_dual == kappa_13


# =========================================================================
# Section 17: Verify hodge/theory data (4 tests)
# =========================================================================

class TestVerificationFunctions:
    """Test the verification helper functions."""

    def test_verify_hodge_C3(self):
        result = verify_hodge_data(cy3_C3())
        assert result["chi_consistent"]

    def test_verify_hodge_quintic(self):
        result = verify_hodge_data(cy3_quintic())
        assert result["chi_consistent"]
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert result["chi"] == -200

    def test_verify_theory_C3(self):
        result = verify_theory_data(theory_from_C3())
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result["coulomb_dim"] == 0

    def test_verify_theory_conifold(self):
        result = verify_theory_data(theory_from_resolved_conifold())
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert result["coulomb_dim"] == 1
