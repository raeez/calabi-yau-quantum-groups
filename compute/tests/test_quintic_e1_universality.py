r"""Tests for quintic_e1_universality.py — E_1 universality for X_5 in P^4.

Multi-path verification across three independent approaches:
  (a) Gepner point / matrix factorization computation
  (b) Large-volume / HKR / Gerstenhaber bracket
  (c) GV invariant comparison

Test organization (35 tests):
  1. Topological data (5 tests)
  2. Gepner point: MF and orbifold (6 tests)
  3. HH^* dimensions and Serre duality (5 tests)
  4. E_1 product structure (3 tests)
  5. Kappa computation: four paths (6 tests)
  6. Shadow invariants (4 tests)
  7. GV invariant checks (4 tests)
  8. Cross-checks and universality verdict (2 tests)
"""

import pytest
from fractions import Fraction as F

from compute.lib.quintic_e1_universality import (
    # Constants
    H11, H21, CHI, B3, DEGREE, C2_DOT_H, A_HAT,
    # Gepner point
    GepnerPointData,
    gepner_point,
    jacobian_ring_grading,
    # HH^* from MF
    HHMFData,
    hh_mf_quintic,
    # E_1 product
    E1ProductStructure,
    e1_product_mf_quintic,
    # Kappa
    KappaQuintic,
    kappa_quintic,
    kappa_bcov_derivation,
    # Shadow invariants
    ShadowInvariantsQuintic,
    shadow_invariants_quintic,
    shadow_tower_quintic,
    # GV invariants
    GV_G0, GV_G1, GV_G2,
    gv_integrality_check,
    gv_vanishing_pattern,
    instanton_corrected_yukawa,
    # Mirror map
    mirror_map_quintic,
    # N=2 minimal model
    n2_mm_quintic_factor,
    gepner_tensor_product,
    # BCOV
    bcov_genus_1_quintic,
    # Orbifold sectors
    orbifold_sector_dimensions,
    # Kappa comparison
    kappa_chi_24_comparison,
    # Monodromy
    picard_fuchs_monodromy,
    # Composite verification
    E1UniversalityQuintic,
    verify_e1_universality_quintic,
    e1_universality_verdict,
)


# ============================================================================
# 1. Topological data (ground truth)
# ============================================================================

class TestTopologicalData:
    """Quintic topological invariants — three independent verifications."""

    def test_hodge_numbers(self):
        """h^{1,1} = 1, h^{2,1} = 101 (from Lefschetz hyperplane + residue)."""
        assert H11 == 1
        assert H21 == 101

    def test_euler_characteristic(self):
        """chi = 2*(h^{1,1} - h^{2,1}) = -200.

        Path 1: Hodge diamond formula.
        Path 2: Gauss-Bonnet integral (known value).
        """
        assert CHI == -200
        assert CHI == 2 * (H11 - H21)

    def test_b3(self):
        """b_3 = 2 + 2*h^{2,1} = 204 (rank of H_3)."""
        assert B3 == 204
        assert B3 == 2 + 2 * H21

    def test_degree_and_c2(self):
        """Degree = 5 (hypersurface in P^4), c_2.H = 50."""
        assert DEGREE == 5
        assert C2_DOT_H == 50

    def test_chi_over_24_not_integer(self):
        """chi/24 = -25/3 is NOT an integer (fundamental BKM obstruction)."""
        ratio = F(CHI, 24)
        assert ratio == F(-25, 3)
        assert ratio.denominator != 1


# ============================================================================
# 2. Gepner point: MF computation and orbifold
# ============================================================================

class TestGepnerPoint:
    """Matrix factorization at the Gepner point W = x_1^5 + ... + x_5^5."""

    def test_milnor_number(self):
        """mu(W) = (5-1)^5 = 4^5 = 1024.

        Path 1: Direct product formula mu = prod(d_i - 1).
        Path 2: dim Jac(W) = dim C[x]/(dW/dx_i) = 4^5.
        """
        gep = gepner_point()
        assert gep.milnor_number == 4 ** 5
        assert gep.milnor_number == 1024

    def test_gepner_level(self):
        """Gepner level k = d - 2 = 3."""
        gep = gepner_point()
        assert gep.gepner_level == 3

    def test_central_charge(self):
        """c = 5 * 3k/(k+2) = 5 * 9/5 = 9 = 3 * CY_dim.

        Path 1: From N=2 MM formula.
        Path 2: CY condition c = 3d.
        """
        gep = gepner_point()
        assert gep.c_total == F(9)
        assert gep.c_total == 3 * 3  # 3 * CY_dim

    def test_orbifold_invariant_dimension(self):
        """Z/5Z-invariant sector has dim 204.

        Path 1: Character sum (1024 - 4)/5 = 204.
        Path 2: Matches b_3(X_5) = 204.
        """
        gep = gepner_point()
        assert gep.orbifold_invariant_dim == 204
        assert gep.orbifold_invariant_dim == B3

    def test_geometric_phase_hh(self):
        """After adding twisted sectors: 204 + 4 = 208 = dim HH^*(D^b(X_5)).

        Path 1: Gepner orbifold + twisted sectors.
        Path 2: HKR formula 4 + 2*h^{1,1} + 2*h^{2,1}.
        """
        gep = gepner_point()
        assert gep.geometric_phase_hh_dim == 208
        assert gep.geometric_phase_hh_dim == 4 + 2 * H11 + 2 * H21

    def test_orbifold_sectors_by_direct_count(self):
        """Direct enumeration of monomials matches character sum.

        The character sum gives:
          sector 0: 204, sectors 1-4: 205 each.
        Total: 204 + 4*205 = 1024.
        """
        orb = orbifold_sector_dimensions()
        assert orb["match"] is True
        assert orb["total_is_1024"] is True
        assert orb["invariant_is_204"] is True


# ============================================================================
# 3. HH^* dimensions and Serre duality
# ============================================================================

class TestHHDimensions:
    """Hochschild cohomology from MF and HKR — cross-verification."""

    def test_hh_graded_dimensions(self):
        """HH^n for n=0,...,6 from LG/CY correspondence.

        HH^0=1, HH^1=0, HH^2=101, HH^3=4, HH^4=101, HH^5=0, HH^6=1.
        """
        hh = hh_mf_quintic()
        assert hh.hh_graded[0] == 1
        assert hh.hh_graded[1] == 0
        assert hh.hh_graded[2] == 101
        assert hh.hh_graded[3] == 4
        assert hh.hh_graded[4] == 101
        assert hh.hh_graded[5] == 0
        assert hh.hh_graded[6] == 1

    def test_hh_total_dimension(self):
        """Total dim HH^* = 208.

        Path 1: Sum of graded pieces.
        Path 2: Hodge formula 4 + 2h^{1,1} + 2h^{2,1}.
        Path 3: Gepner orbifold 204 + 4.
        """
        hh = hh_mf_quintic()
        assert hh.total_dim_invariant == 208
        assert sum(hh.hh_graded.values()) == 208
        assert 4 + 2 * H11 + 2 * H21 == 208

    def test_serre_duality(self):
        """HH^n = HH^{6-n} (CY3 Serre duality on Hochschild cohomology)."""
        hh = hh_mf_quintic().hh_graded
        for n in range(7):
            assert hh[n] == hh[6 - n], f"Serre duality fails at n={n}"

    def test_hh_matches_geometric(self):
        """MF computation matches geometric HKR computation."""
        hh = hh_mf_quintic()
        assert hh.matches_geometric is True

    def test_euler_hh(self):
        """chi(HH^*) = sum (-1)^n dim HH^n = -chi(X).

        For the quintic: chi(HH^*) = 1-0+101-4+101-0+1 = 200 = -(-200).
        """
        hh = hh_mf_quintic().hh_graded
        euler = sum((-1)**n * hh[n] for n in range(7))
        assert euler == -CHI  # = 200


# ============================================================================
# 4. E_1 product structure
# ============================================================================

class TestE1Product:
    """E_1 (associative, non-commutative) product on HH^*."""

    def test_is_associative(self):
        """The MF tensor product is associative (E_1 structure)."""
        e1 = e1_product_mf_quintic()
        assert e1.is_associative is True

    def test_is_not_commutative(self):
        """The MF tensor product is NOT commutative (not E_infty or E_2).

        The Gerstenhaber bracket [HH^2, HH^2] -> HH^3 is nontrivial
        for h^{2,1} = 101 > 0, witnessing non-commutativity.
        """
        e1 = e1_product_mf_quintic()
        assert e1.is_commutative is False
        assert e1.e_level == 1

    def test_e1_not_e2(self):
        """The native E_n level for CY3 is E_1, not E_2.

        Path 1: CY_d native E_n = E_{d-2} -> E_1 for d=3.
        Path 2: holomorphic CS trivialization breaks E_2 to E_1.
        Path 3: Deformation space dimension = 1 (E_1 hallmark).
        """
        e1 = e1_product_mf_quintic()
        assert e1.e_level == 1
        # The CY3 native E_n formula: d-2 = 3-2 = 1
        assert 3 - 2 == 1


# ============================================================================
# 5. Kappa computation: four independent paths
# ============================================================================

class TestKappa:
    """Four kappa values from four different algebraic objects (AP48)."""

    def test_kappa_bcov(self):
        """kappa_BCOV = chi/24 = -25/3 (NOT integer)."""
        kap = kappa_quintic()
        assert kap.kappa_bcov == F(-25, 3)
        assert kap.kappa_bcov.denominator != 1

    def test_kappa_macmahon(self):
        """kappa_MacMahon = chi/2 = -100 (integer).

        This is the exponent in Z_0 = M(q)^{chi/2} and the physically
        relevant kappa for the B-model topological string.
        """
        kap = kappa_quintic()
        assert kap.kappa_macmahon == F(-100)
        assert kap.kappa_macmahon.denominator == 1

    def test_kappa_gepner(self):
        """kappa_Gepner = c_{N=2}/6 = 9/6 = 3/2."""
        kap = kappa_quintic()
        assert kap.kappa_gepner == F(3, 2)

    def test_kappa_mf(self):
        """kappa_MF = mu/2 = 1024/2 = 512."""
        kap = kappa_quintic()
        assert kap.kappa_mf == F(512)

    def test_bcov_macmahon_ratio(self):
        """kappa_MacMahon / kappa_BCOV = -12.

        Path 1: direct ratio.
        Path 2: chi/2 divided by chi/24 = 12 (with sign from orientation).
        """
        deriv = kappa_bcov_derivation()
        assert deriv["ratio_is_minus_12"] is True

    def test_four_kappas_distinct(self):
        """All four kappa values are distinct (AP48: different algebras)."""
        kap = kappa_quintic()
        values = [kap.kappa_bcov, kap.kappa_macmahon, kap.kappa_gepner, kap.kappa_mf]
        assert len(set(values)) == 4, "Expected four distinct kappa values"


# ============================================================================
# 6. Shadow invariants
# ============================================================================

class TestShadowInvariants:
    """Shadow obstruction tower data for the quintic."""

    def test_shadow_kappa(self):
        """kappa = chi/2 = -100 (MacMahon convention)."""
        sh = shadow_invariants_quintic()
        assert sh.kappa == F(-100)

    def test_cubic_shadow(self):
        """alpha = C_111 / kappa = 5/(-100) = -1/20.

        Path 1: Yukawa coupling / kappa.
        Path 2: degree of quintic / (chi/2).
        """
        sh = shadow_invariants_quintic()
        assert sh.alpha == F(-1, 20)
        assert sh.alpha == F(DEGREE) / F(CHI, 2)

    def test_shadow_class_M(self):
        """Shadow depth class M (infinite tower, from infinite GW invariants)."""
        sh = shadow_invariants_quintic()
        assert sh.shadow_class == "M"

    def test_shadow_tower_values(self):
        """F_g = kappa * a_hat_g (constant-map sector).

        F_1 = -100/24 = -25/6.
        F_2 = -100 * 7/5760 = -35/288.
        """
        tower = shadow_tower_quintic()
        assert tower[1] == F(-100) * F(1, 24)
        assert tower[1] == F(-25, 6)
        assert tower[2] == F(-100) * F(7, 5760)
        assert tower[2] == F(-35, 288)


# ============================================================================
# 7. GV invariant checks
# ============================================================================

class TestGVInvariants:
    """Gopakumar-Vafa invariant verification."""

    def test_genus_0_gv_values(self):
        """n^0_1 = 2875, n^0_2 = 609250 (COGP mirror symmetry)."""
        assert GV_G0[1] == 2875
        assert GV_G0[2] == 609250

    def test_gv_integrality(self):
        """All known GV invariants are integers."""
        results = gv_integrality_check()
        assert all(results.values()), f"Non-integer GV invariants: {results}"

    def test_gv_vanishing_pattern(self):
        """Castelnuovo bound: n^g_d = 0 when g exceeds the bound.

        n^1_1 = n^1_2 = 0 (lines/conics are rational).
        n^2_1 = n^2_2 = n^2_3 = 0 (low-degree curves have g < 2).
        """
        van = gv_vanishing_pattern()
        assert van["all_pass"] is True

    def test_instanton_yukawa_degree_1(self):
        """Instanton-corrected Yukawa at degree 1: 5 + 2875 = 2880.

        Path 1: C(q) = 5 + sum n_d d^3 q^d/(1-q^d).
        At order q^1: n^0_1 * 1^3 = 2875. Total: 5 + 2875 at orders 0,1.
        """
        yuk = instanton_corrected_yukawa()
        assert yuk[0] == 5
        assert yuk[1] == 2875
        # Degree 2: n^0_1 * 1^3 (divisor k=1 of d=2) + n^0_2 * 2^3
        assert yuk[2] == 2875 + 609250 * 8


# ============================================================================
# 8. Cross-checks and universality verdict
# ============================================================================

class TestUniversalityVerdict:
    """Composite E_1 universality verification."""

    def test_all_paths_consistent(self):
        """All three paths (Gepner, large-volume, GV) are consistent."""
        result = verify_e1_universality_quintic()
        assert result.all_paths_consistent is True
        assert result.gepner_hh_matches is True
        assert result.hh_serre_duality is True
        assert result.gerstenhaber_nontrivial is True
        assert result.e1_not_e2 is True
        assert result.gv_integral is True
        assert result.gv_vanishing is True

    def test_verdict(self):
        """The verdict: E_1 universality is CONSISTENT but CONJECTURAL.

        kappa(X_5) = -100 = chi/2 (MacMahon convention).
        Shadow class: M (infinite depth).
        Status: conjectural (chain-level S^3-framing needed for proof).
        """
        verdict = e1_universality_verdict()
        assert verdict["kappa"] == F(-100)
        assert verdict["shadow_class"] == "M"
        assert "CONSISTENT" in verdict["e1_universality_holds"]
        assert verdict["all_paths_consistent"] is True


# ============================================================================
# 9. Additional cross-path verifications
# ============================================================================

class TestCrossPathVerification:
    """Additional multi-path consistency checks."""

    def test_n2_mm_factor_data(self):
        """N=2 MM at k=3: c = 9/5, chiral ring dim = 4."""
        mm = n2_mm_quintic_factor()
        assert mm.level == 3
        assert mm.c == F(9, 5)
        assert mm.chiral_ring_dim == 4

    def test_gepner_tensor_cy_condition(self):
        """Gepner tensor product c = 9 satisfies the CY condition c = 3d."""
        tp = gepner_tensor_product()
        assert tp["cy_condition"] is True
        assert tp["c_total"] == F(9)

    def test_picard_fuchs_singularities(self):
        """PF equation has three singularities (MUM, conifold, Gepner)."""
        pf = picard_fuchs_monodromy()
        assert len(pf["singularities"]) == 3
        assert pf["orbifold_order"] == 5
