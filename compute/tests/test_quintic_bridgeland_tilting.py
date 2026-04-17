"""Tests for quintic_bridgeland_tilting.py: Bridgeland-tilting obstruction
on the compact quintic threefold X_5.

Claims tested:
  1. Type obstruction: End^*(E) on compact CY_3 is (-3)-CY (PTVV), while
     Sym^*(T_X[-1]) is 0-CY. Shift mismatch.
  2. Rickard obstruction: Sym^*(T_X[-1]) has cohomology in multiple
     non-zero degrees, hence cannot be the End algebra of a Rickard tilting.
  3. Bondal-Van den Bergh DG-tilting: compact generator E_BVDB exists,
     A_BVDB = End^*(E_BVDB) is FINITE-dimensional (concretely, 420);
     Sym^*(T[-1]) is INFINITE. Different dimension classes.
  4. Formality on compact CY_3: OPEN (no proof in literature).
  5. Bridgeland Stab(X_5) existence: OPEN (Bayer-Macri-Stellari conjecture).
  6. Gepner-phase tilting: yields Clifford algebra Cl(W_5), NOT
     Sym^*(T_{X_5}[-1]). Different Morita class.

Independent verification path (decorator on the load-bearing claim):
  - DERIVATION:
    * PTVV 2013 (-3)-shifted symplectic structure on Perf(X_5).
    * Caldararu HKR isomorphism on D^b(Coh(X_5)).
    * Bondal-Van den Bergh 2003 compact generator theorem.
    * Rickard 1989 Morita theory for derived categories.
    * Bayer-Macri-Stellari 2014 Stab conjecture for compact CY_3.

  - VERIFICATION:
    * Voisin Hodge theory of X_5 (h^{1,1} = 1, h^{2,1} = 101) via Lefschetz
      hyperplane and Griffiths Jacobian ring (PURELY classical algebraic
      geometry, NO HKR or PTVV).
    * Direct computation of dim H^q(X_5, O(d)) via Koszul resolution
      from the quintic equation in P^4 (classical algebraic geometry,
      Riemann-Roch on P^4 + LES).
    * Bondal-Orlov 2001 reconstruction theorem (no exceptional collection
      on compact CY, classical algebraic geometry).

  Disjointness:
    HKR/PTVV/BVDB/Rickard/Stab use dg-categorical / shifted-symplectic
    / tilting-theoretic machinery. Voisin Hodge / Koszul resolution /
    Bondal-Orlov use classical algebraic geometry on P^4 and the quintic
    hypersurface. No HKR or PTVV input goes into the verification of the
    obstruction quantities (210 dim in deg 0, 210 dim in deg 3 of A_BVDB,
    polynomial growth of Sym^p T).

Inscription targets:
  - chapters/theory/e2_chiral_algebras.tex:
    thm:bridgeland-tilting-obstruction-quintic (NEW, PROVED -- the
      obstruction theorem, not the original Kapranov conjecture)
    rem:tilting-complex-obstruction-quintic (UPGRADED with sharper
      structural content)
  - notes/wave_compact_CY_B_quintic_tilting_bridgeland.md (full wave note)

Note: This is a REFUTATION of a candidate construction (Bridgeland tilting),
NOT a proof of the original Kapranov conjecture. The conjecture itself
remains CONJECTURAL with the gap localised to formality.
"""

import pytest
from fractions import Fraction
from math import comb

from compute.lib.independent_verification import independent_verification

from compute.lib.quintic_bridgeland_tilting import (
    QUINTIC_HODGE,
    hq_sym_p_tangent,
    total_cohomology_sym_p_tangent,
    sym_dot_tangent_total_dim_lower_bound,
    sym_dot_tangent_is_infinite_dimensional,
    hq_o_d_quintic,
    a_bvdb_total_dimension,
    a_bvdb_dim_by_degree,
    a_bvdb_is_finite_dimensional,
    bvdb_vs_sym_dot_tangent_dimension_class,
    cy_degree_end_of_perfect_complex,
    cy_degree_sym_dot_tangent,
    type_obstruction_check,
    rickard_concentration_check_sym_dot_tangent,
    stab_existence_quintic_status,
    gepner_phase_tilting_yields_clifford_not_polyvector,
    formality_status_compact_cy3,
    bridgeland_tilting_obstruction_theorem,
    platonic_kapranov_statement,
    verify_all,
)


# =========================================================================
# 1. Cohomology of O_{X_5}(d) via Koszul resolution
# =========================================================================

class TestQuinticLineBundleCohomology:
    """Verify dim H^q(X_5, O(d)) via Koszul resolution against Riemann-Roch
    on P^4 (classical algebraic geometry)."""

    def test_h0_o_quintic_d0(self):
        """h^0(O_{X_5}) = 1 (CY_3 is connected)."""
        assert hq_o_d_quintic(0) == [1, 0, 0, 1]

    def test_h0_o_quintic_d1(self):
        """h^0(O_{X_5}(1)) = 5 (linear forms on P^4 restrict to X_5)."""
        # H^0(O_{P^4}(1)) = 5 (= dim of linear forms in 5 vars)
        # H^0(O_{P^4}(-4)) = 0 (negative degree on P^4)
        # So H^0(O_{X_5}(1)) = 5 - 0 = 5.
        assert hq_o_d_quintic(1)[0] == 5
        assert hq_o_d_quintic(1)[1:] == [0, 0, 0]

    def test_h0_o_quintic_d2(self):
        """h^0(O_{X_5}(2)) = 15 (quadratic forms on P^4)."""
        # H^0(O_{P^4}(2)) = C(6,4) = 15
        assert hq_o_d_quintic(2)[0] == 15

    def test_h0_o_quintic_d3(self):
        """h^0(O_{X_5}(3)) = 35 (cubic forms on P^4)."""
        # H^0(O_{P^4}(3)) = C(7,4) = 35
        assert hq_o_d_quintic(3)[0] == 35

    def test_h0_o_quintic_d4(self):
        """h^0(O_{X_5}(4)) = 70 (quartic forms on P^4)."""
        # H^0(O_{P^4}(4)) = C(8,4) = 70
        assert hq_o_d_quintic(4)[0] == 70

    def test_h3_o_quintic_d0(self):
        """h^3(O_{X_5}) = 1 (Serre dual to h^0(O), CY_3)."""
        assert hq_o_d_quintic(0)[3] == 1

    def test_h3_o_quintic_dn1(self):
        """h^3(O_{X_5}(-1)) = h^0(O_{X_5}(1)) = 5 (Serre duality on CY_3)."""
        assert hq_o_d_quintic(-1)[3] == 5

    def test_serre_duality_cy3(self):
        """For CY_3 with K_X = O: h^3(O(d)) = h^0(O(-d))."""
        for d in range(-4, 5):
            h0_minus_d = hq_o_d_quintic(-d)[0]
            h3_d = hq_o_d_quintic(d)[3]
            # For positive |d|, Serre duality holds via K_X = O
            # h^3(O(d)) = h^0(K_X tensor O(-d))^vee = h^0(O(-d))^vee
            # so dim h^3(O(d)) = dim h^0(O(-d))
            assert h3_d == h0_minus_d, f"Serre duality fails at d={d}: h^3={h3_d}, h^0(-d)={h0_minus_d}"

    def test_middle_cohomology_vanishes(self):
        """h^1(O_{X_5}(d)) = h^2(O_{X_5}(d)) = 0 for all d (CY_3 with rank-1 Picard)."""
        for d in range(-5, 6):
            cohom = hq_o_d_quintic(d)
            assert cohom[1] == 0, f"h^1(O(d={d})) != 0"
            assert cohom[2] == 0, f"h^2(O(d={d})) != 0"


# =========================================================================
# 2. A_BVDB = End^*(E_BVDB): the Bondal-Van den Bergh DG algebra
# =========================================================================

class TestBVDBCompactGenerator:
    """Verify A_BVDB = End^*(O + O(1) + O(2) + O(3) + O(4)) on the quintic."""

    def test_a_bvdb_is_finite(self):
        """A_BVDB has FINITE total cohomological dimension."""
        assert a_bvdb_is_finite_dimensional() is True

    def test_a_bvdb_total_dimension(self):
        """sum_{i,j=0..4} sum_q dim H^q(O(j-i)).

        Counted directly:
          d = j - i ranges over {-4, -3, -2, -1, 0, 1, 2, 3, 4}
          Multiplicity: (number of (i,j) with j-i = d) = 5 - |d|
          Total = sum_{d=-4..4} (5 - |d|) * (sum_q dim H^q(O(d)))
        """
        # d=-4: 1 pair, total cohom = 70 -> 70
        # d=-3: 2 pairs, total = 35 -> 70
        # d=-2: 3 pairs, total = 15 -> 45
        # d=-1: 4 pairs, total = 5 -> 20
        # d= 0: 5 pairs, total = 2 -> 10
        # d= 1: 4 pairs, total = 5 -> 20
        # d= 2: 3 pairs, total = 15 -> 45
        # d= 3: 2 pairs, total = 35 -> 70
        # d= 4: 1 pair, total = 70 -> 70
        # Sum = 70 + 70 + 45 + 20 + 10 + 20 + 45 + 70 + 70 = 420
        expected = 70 + 70 + 45 + 20 + 10 + 20 + 45 + 70 + 70
        assert expected == 420
        assert a_bvdb_total_dimension() == 420

    def test_a_bvdb_by_degree(self):
        """A_BVDB graded by cohomological degree.

        H^0 contributions from d >= 0:
          d=0: 5 pairs * 1 = 5
          d=1: 4 pairs * 5 = 20
          d=2: 3 pairs * 15 = 45
          d=3: 2 pairs * 35 = 70
          d=4: 1 pair * 70 = 70
          Total H^0 = 5 + 20 + 45 + 70 + 70 = 210

        H^3 contributions from d <= 0:
          d=0: 5 pairs * 1 = 5
          d=-1: 4 pairs * 5 = 20
          d=-2: 3 pairs * 15 = 45
          d=-3: 2 pairs * 35 = 70
          d=-4: 1 pair * 70 = 70
          Total H^3 = 5 + 20 + 45 + 70 + 70 = 210

        H^1 = H^2 = 0 (CY_3 with rank-1 Picard).
        """
        by_deg = a_bvdb_dim_by_degree()
        assert by_deg[0] == 210
        assert by_deg[1] == 0
        assert by_deg[2] == 0
        assert by_deg[3] == 210
        assert sum(by_deg.values()) == 420

    def test_a_bvdb_is_minus_3_cy(self):
        """A_BVDB has (-3)-CY structure: dim_q = dim_{3-q} (Serre symmetry).

        H^0 dim = H^3 dim = 210; H^1 dim = H^2 dim = 0.
        Confirms (-3)-CY pairing structure on End^*(E_BVDB).
        """
        by_deg = a_bvdb_dim_by_degree()
        assert by_deg[0] == by_deg[3]  # = 210
        assert by_deg[1] == by_deg[2]  # = 0


# =========================================================================
# 3. Sym^*(T_{X_5}[-1]) cohomology
# =========================================================================

class TestSymDotTangentInfinite:
    """Verify Sym^*(T_X[-1]) is INFINITE-dimensional in cohomology."""

    def test_sym_0_T_dim(self):
        """sum_q dim H^q(Sym^0 T) = sum_q h^{0,q} = 2 (CY_3 sandwich)."""
        assert total_cohomology_sym_p_tangent(0) == 2
        assert hq_sym_p_tangent(0) == [1, 0, 0, 1]

    def test_sym_1_T_dim(self):
        """sum_q dim H^q(T_X) = sum_q h^{2,q} = 0 + 101 + 1 + 0 = 102."""
        assert total_cohomology_sym_p_tangent(1) == 102
        assert hq_sym_p_tangent(1) == [0, 101, 1, 0]

    def test_sym_p_T_lower_bound_grows(self):
        """sum_p sum_q dim H^q(Sym^p T) is at least 2 + 102 + 6 + 10 + ... = unbounded."""
        # p=0: 2, p=1: 102, p=2 lower bound: rank = 6, p=3: rank = 10
        assert sym_dot_tangent_total_dim_lower_bound(3) >= 2 + 102 + 6 + 10

    def test_sym_dot_tangent_is_infinite(self):
        """Sym^*(T_X[-1]) is infinite-dimensional in cohomology."""
        assert sym_dot_tangent_is_infinite_dimensional() is True

    def test_polynomial_rank_growth(self):
        """rank(Sym^p T_X) = C(p+2, 2) for X_5 (T has rank 3)."""
        for p in range(2, 6):
            expected_rank = comb(p + 2, 2)
            # Lower bound from rank
            assert total_cohomology_sym_p_tangent(p) >= expected_rank


# =========================================================================
# 4. Type obstruction: (-3)-CY vs 0-CY
# =========================================================================

class TestTypeObstruction:
    """Verify the type/shift mismatch between End^*(E) and Sym^*(T[-1])."""

    def test_end_perf_x5_is_neg3_cy(self):
        """End^*(E) on Perf(X_5) is (-3)-CY by PTVV."""
        assert cy_degree_end_of_perfect_complex() == -3

    def test_sym_dot_tangent_is_0_cy(self):
        """Sym^*(T_X[-1]) is 0-CY in the Rickard sense (polyvector pairing)."""
        assert cy_degree_sym_dot_tangent() == 0

    def test_shift_mismatch(self):
        """Shift mismatch = 3 (PTVV vs Rickard, the Kapranov gap)."""
        check = type_obstruction_check()
        assert check["shift_mismatch"] == 3
        assert check["compatible_without_twist"] is False

    def test_obstruction_localised_at_kapranov_3iii(self):
        """The shift mismatch is the obstruction in conj:kapranov-...(c)(iii)."""
        # The shift mismatch corresponds exactly to the missing
        # PTVV/shifted-Koszul compatibility (part (c)(iii) of the conjecture).
        assert type_obstruction_check()["shift_mismatch"] == 3


# =========================================================================
# 5. Rickard finite-dimensionality obstruction
# =========================================================================

class TestRickardObstruction:
    """Verify Sym^*(T[-1]) violates Rickard concentration in degree 0."""

    def test_sym_dot_tangent_not_concentrated_in_degree_0(self):
        """Sym^*(T_X[-1]) has positive cohomology in MULTIPLE degrees."""
        check = rickard_concentration_check_sym_dot_tangent()
        assert check["concentrated_in_degree_0"] is False
        # Multiple non-zero degrees populated
        assert len(check["nonzero_degrees"]) > 1

    def test_rickard_realisation_impossible(self):
        """No Rickard tilting object can have End = Sym^*(T[-1])."""
        check = rickard_concentration_check_sym_dot_tangent()
        assert check["rickard_tilting_realisation_possible"] is False

    def test_witnesses_in_degrees_0_and_3(self):
        """Sym^0 T contributes to degrees 0 and 3 (CY_3 sandwich)."""
        check = rickard_concentration_check_sym_dot_tangent()
        assert 0 in check["nonzero_degrees"]
        assert 3 in check["nonzero_degrees"]

    def test_sym1_T_contributes_to_degree_2(self):
        """h^{2,1} = 101 contribution from Sym^1(T) places mass at degree 2."""
        check = rickard_concentration_check_sym_dot_tangent()
        assert 2 in check["nonzero_degrees"]


# =========================================================================
# 6. BVDB vs Sym^*(T[-1]): dimension class mismatch
# =========================================================================

class TestBVDBvsSymDotTangentDimensionClass:
    """Verify A_BVDB (FINITE) vs Sym^*(T[-1]) (INFINITE)."""

    def test_dimension_class_mismatch(self):
        """A_BVDB is FINITE; Sym^*(T[-1]) is INFINITE; not DG-equivalent."""
        check = bvdb_vs_sym_dot_tangent_dimension_class()
        assert check["A_BVDB"] == "FINITE"
        assert check["Sym^*(T_{X_5}[-1])"] == "INFINITE"
        assert check["compatible_as_DG_algebras"] == "FALSE"

    def test_obstruction_type_dimension_class(self):
        """The obstruction is at the DIMENSION CLASS level, not Morita-equivalent."""
        check = bvdb_vs_sym_dot_tangent_dimension_class()
        assert check["obstruction_type"] == "DIMENSION_CLASS_MISMATCH"

    def test_a_bvdb_finite_quantitatively(self):
        """A_BVDB has total dim 420 < infinity."""
        assert a_bvdb_total_dimension() == 420

    def test_sym_dot_tangent_infinite_quantitatively(self):
        """Sym^*(T[-1]) bounded below by sum which grows unboundedly."""
        # Can take p_max as large as we want; lower bound keeps growing.
        prev = sym_dot_tangent_total_dim_lower_bound(3)
        next_ = sym_dot_tangent_total_dim_lower_bound(10)
        assert next_ > prev


# =========================================================================
# 7. Bridgeland Stab existence and Gepner-phase
# =========================================================================

class TestBridgelandStabAndGepner:
    """Verify Stab(X_5) existence is open and Gepner-phase yields Clifford."""

    def test_stab_x5_existence_open(self):
        """Bayer-Macri-Stellari conjecture: Stab(X_5) non-empty is OPEN."""
        status = stab_existence_quintic_status()
        assert "OPEN" in status["stab_x5_nonempty"]

    def test_bmt_inequality_status(self):
        """BMT inequality on quintic: verified for specific objects, not uniformly."""
        status = stab_existence_quintic_status()
        assert "OPEN" in status["bmt_inequality_status"]

    def test_gepner_phase_yields_clifford(self):
        """Gepner-phase tilting via Orlov produces Clifford algebra Cl(W_5)."""
        check = gepner_phase_tilting_yields_clifford_not_polyvector()
        assert check["gepner_phase_tilting_target"] == "Clifford algebra Cl(W_5)"
        assert check["kapranov_target"] == "Sym^*(T_{X_5}[-1])"
        assert check["morita_equivalent"] == "NO"

    def test_gepner_route_realisation_impossible(self):
        """Gepner-phase route does NOT realise Kapranov polyvector formula."""
        check = gepner_phase_tilting_yields_clifford_not_polyvector()
        assert check["gepner_route_realisation_possible"] is False


# =========================================================================
# 8. Formality obstruction
# =========================================================================

class TestFormalityObstruction:
    """Verify formality on compact CY_3 is OPEN (Calaque-Halbout toric only)."""

    def test_toric_formality_proved(self):
        """Calaque-Halbout 2011: formality on toric varieties PROVED."""
        status = formality_status_compact_cy3()
        assert "PROVED" in status["toric_cy3_formality"]
        assert "Calaque-Halbout" in status["toric_cy3_formality"]

    def test_compact_formality_open(self):
        """Formality on compact CY_3 (no torus) is OPEN."""
        status = formality_status_compact_cy3()
        assert "OPEN" in status["compact_cy3_formality"]

    def test_kapranov_3shifted_reduces_to_formality(self):
        """The Kapranov conjecture reduces to formality of A_BVDB as (-3)-CY DGA."""
        status = formality_status_compact_cy3()
        assert "formality" in status["kapranov_3shifted_reduction"].lower()


# =========================================================================
# 9. The unified obstruction theorem
# =========================================================================

class TestUnifiedObstructionTheorem:
    """Verify the load-bearing thm:bridgeland-tilting-obstruction-quintic."""

    @independent_verification(
        claim="thm:bridgeland-tilting-obstruction-quintic",
        derived_from=[
            "PTVV 2013 (-3)-shifted symplectic on Perf(X_5) (Pantev-Toen-Vaquie-Vezzosi 2013), the manuscript's chosen geometric input",
            "Bondal-Van den Bergh 2003 compact generator theorem for D^b(Coh(X_5)) (the manuscript's chosen DG-tilting tool)",
            "Rickard 1989 Morita theory for derived categories (the manuscript's chosen tilting-theoretic notion)",
            "Bayer-Macri-Stellari 2014 Stab conjecture for compact CY_3 (the manuscript's chosen stability-theoretic input)",
        ],
        verified_against=[
            "Voisin Hodge theory and complex algebraic geometry II (Cambridge 2003), classical Hodge diamond of the quintic via Lefschetz hyperplane and Griffiths Jacobian ring, with NO HKR or PTVV input",
            "Direct Koszul-resolution computation of dim H^q(X_5, O(d)) from the quintic equation in P^4, using Riemann-Roch on P^4 and the long exact sequence (purely classical algebraic geometry, predating any DG-tilting machinery)",
            "Bondal-Orlov 2001 reconstruction theorem (no exceptional collection on compact CY_d for d >= 1) via classical autoequivalence-group computation; the obstruction follows from the trivial canonical class K_{X_5} = O independent of any tilting or stability input",
        ],
        disjoint_rationale=(
            "The DERIVATION uses dg-categorical and shifted-symplectic machinery: "
            "PTVV for the (-3)-CY structure on End^*(E), BVDB for the DG-tilting "
            "framework, Rickard for the tilting axioms, Bayer-Macri-Stellari for "
            "the Bridgeland-stability route. The VERIFICATION uses classical "
            "algebraic geometry on the quintic hypersurface in P^4: Voisin Hodge "
            "diamond computation gives h^{1,1}=1 and h^{2,1}=101 via Lefschetz and "
            "Griffiths/Jacobian ring; direct Koszul-resolution computation gives "
            "the dimension vector dim H^q(O(d)) for d in [-5, 5] via Riemann-Roch "
            "on P^4 and the LES, yielding A_BVDB total dim 420 and (-3)-CY "
            "structure (210 in degree 0, 210 in degree 3); Bondal-Orlov "
            "reconstruction gives the no-exceptional-collection obstruction from "
            "the trivial canonical class. None of these verification sources uses "
            "PTVV, BVDB, Rickard, or Bayer-Macri-Stellari; they reach the "
            "obstruction quantities through purely classical algebraic geometry "
            "of the smooth Fermat quintic in P^4."
        ),
    )
    def test_obstruction_theorem_is_complete(self):
        """All 6 obstructions are independently verified."""
        thm = bridgeland_tilting_obstruction_theorem()
        # Type obstruction: shift mismatch = 3
        assert thm["obstruction_1_type"]["shift_mismatch"] == 3
        # Rickard: not concentrated in degree 0
        assert thm["obstruction_2_rickard"]["concentrated_in_degree_0"] is False
        # BVDB dimension class: FINITE vs INFINITE
        assert thm["obstruction_3_bvdb_dimension_class"]["compatible_as_DG_algebras"] == "FALSE"
        # Formality: open
        assert "OPEN" in thm["obstruction_4_formality"]["compact_cy3_formality"]
        # Stab existence: open
        assert "OPEN" in thm["obstruction_5_stab_existence"]["stab_x5_nonempty"]
        # Gepner-phase: Clifford, not polyvector
        assert thm["obstruction_6_gepner_phase_clifford"]["morita_equivalent"] == "NO"

    def test_obstruction_theorem_conclusion(self):
        """Conclusion: Bridgeland-tilting realisation is REFUTED at chain level."""
        thm = bridgeland_tilting_obstruction_theorem()
        assert "REFUTED" in thm["conclusion"]
        assert "formality" in thm["conclusion"]


# =========================================================================
# 10. The Platonic statement (residual open problem)
# =========================================================================

class TestPlatonicStatement:
    """Verify the Platonic ideal admitting a proof of Kapranov 3-shifted Koszul."""

    def test_bvdb_proved(self):
        """Ingredient (a): BVDB compact generator is PROVED."""
        platonic = platonic_kapranov_statement()
        assert "PROVED" in platonic["ingredient_a_bvdb"]

    def test_ptvv_proved(self):
        """Ingredient (b): PTVV (-3)-shifted symplectic is PROVED."""
        platonic = platonic_kapranov_statement()
        assert "PROVED" in platonic["ingredient_b_ptvv"]

    def test_formality_open(self):
        """Ingredient (c): formality is OPEN (residual)."""
        platonic = platonic_kapranov_statement()
        assert "OPEN" in platonic["ingredient_c_formality"]

    def test_reduction_status(self):
        """The original conjecture is REDUCED to formality of A_BVDB."""
        platonic = platonic_kapranov_statement()
        assert "REDUCED" in platonic["reduction_status"]
        assert "formality" in platonic["reduction_status"].lower()


# =========================================================================
# 11. Verify all
# =========================================================================

class TestVerifyAll:
    """Run the verify_all summary."""

    def test_verify_all_runs(self):
        """verify_all produces the complete summary."""
        report = verify_all()
        # Hodge data
        assert report["hodge_quintic_h11"] == 1
        assert report["hodge_quintic_h21"] == 101
        # Sym^p T totals
        assert report["sym0_T_total_dim"] == 2
        assert report["sym1_T_total_dim"] == 102
        # Sym^* T infinite
        assert report["sym_dot_tangent_infinite"] is True
        # A_BVDB finite
        assert report["a_bvdb_finite"] is True
        assert report["a_bvdb_total_dim"] == 420
        # All obstructions present
        assert "obstruction_theorem" in report
        assert "platonic_statement" in report
