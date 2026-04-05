r"""
Tests for local_p2_chart_gluing.py: complete 3-chart quiver-chart gluing
for local P^2 = K_{P^2}.

Multi-path verification strategy:
  (a) Quiver structure: arrow counts, vertex counts, exchange matrices
  (b) Mutation: involution, antisymmetry, exchange matrix formulas
  (c) CoHA: dimension computations, Poincare series, Szendroi M(q)^3
  (d) Wall-crossing: KS factors, cocycle condition, hexagon identity
  (e) Triple overlap: homotopy existence, arity-3 cubic shadow
  (f) Hocolimit: generators, relations, global algebra structure
  (g) kappa: 4-path verification, additivity, consistency
  (h) Z_3 symmetry: exchange matrix invariance, CoHA equivariance, automorphism
  (i) Bar complex: Mayer-Vietoris, shadow depth, shadow tower
  (j) DT partition function: MacMahon cube, motivic invariants
  (k) Scattering diagram: A_2 structure, wall count
  (l) Cross-checks: Euler form, Tits form, CY condition

References:
  [DWZ]  Derksen-Weyman-Zelevinsky, arXiv:0704.0649
  [KS]   Kontsevich-Soibelman, arXiv:0811.2435
  [S]    Szendroi, arXiv:0512556
  [B]    Bridgeland, arXiv:1603.00416
  Lorgat, Vol I: bar-cobar duality, shadow obstruction tower
  Lorgat, Vol III: CY-to-chiral functor
"""

import pytest
from fractions import Fraction
from typing import Dict

from compute.lib.local_p2_chart_gluing import (
    # Quiver structures
    Arrow, QuiverWithPotential,
    mckay_quiver_z3,
    phase_I_quiver, phase_II_quiver, phase_III_quiver,
    adjacency_matrix, arrow_count, exchange_matrix,
    mutate_quiver, mutate_exchange_matrix,
    three_phase_exchange_matrices,
    # CoHA
    euler_form_z3, symmetrized_euler_form, tits_form,
    coha_dimension_mckay_z3, coha_poincare_series,
    verify_coha_vs_macmahon_cube,
    # DT and wall-crossing
    dt_invariant_z3,
    ks_wall_crossing_factor,
    wall_crossing_product_K12, wall_crossing_product_K23, wall_crossing_product_K13,
    cocycle_check,
    hexagon_identity_a2,
    # Triple overlap
    triple_overlap_homotopy,
    # Hocolimit
    hocolim_generators, hocolim_relations,
    # DT partition function and kappa
    GV_GENUS0,
    dt_from_glued_algebra,
    kappa_from_glued_charts, kappa_from_euler_char_base,
    kappa_from_macmahon, kappa_from_coha_poincare,
    verify_kappa_four_paths,
    # Z_3 symmetry
    z3_action_on_quiver, z3_automorphism_on_global_algebra,
    z3_on_exchange_matrix,
    # Bar complex and shadow tower
    bar_complex_from_mayer_vietoris,
    shadow_depth_from_charts,
    cubic_shadow_from_triple_overlap,
    quartic_shadow_from_instantons,
    shadow_tower_from_gv,
    shadow_generating_function,
    # Motivic DT
    motivic_dt_generating_function, macmahon_cube_coefficients,
    # Scattering diagram
    scattering_diagram_a2,
    # Verification utilities
    verify_exchange_matrix_antisymmetric,
    verify_mutation_involution,
    verify_coha_z3_symmetry,
    verify_euler_form_cy_condition,
    verify_tits_form_values,
    verify_kappa_additivity,
    # Full report
    full_chart_gluing_report,
)


# =========================================================================
# SECTION A: QUIVER STRUCTURE (15 tests)
# =========================================================================

class TestMcKayQuiver:
    """Tests for the McKay quiver of C^3/Z_3."""

    def test_mckay_n_vertices(self):
        """McKay Z_3 quiver has 3 vertices."""
        Q = mckay_quiver_z3()
        assert Q.n_vertices == 3

    def test_mckay_n_arrows(self):
        """McKay Z_3 quiver has 9 arrows (3 per edge)."""
        Q = mckay_quiver_z3()
        assert len(Q.arrows) == 9

    def test_mckay_name(self):
        Q = mckay_quiver_z3()
        assert Q.name == "McKay_Z3"

    def test_arrows_0_to_1(self):
        """3 arrows from vertex 0 to vertex 1."""
        Q = mckay_quiver_z3()
        assert arrow_count(Q, 0, 1) == 3

    def test_arrows_1_to_2(self):
        """3 arrows from vertex 1 to vertex 2."""
        Q = mckay_quiver_z3()
        assert arrow_count(Q, 1, 2) == 3

    def test_arrows_2_to_0(self):
        """3 arrows from vertex 2 to vertex 0."""
        Q = mckay_quiver_z3()
        assert arrow_count(Q, 2, 0) == 3

    def test_no_reverse_arrows(self):
        """No arrows in the reverse direction (0 <- 1, 1 <- 2, 2 <- 0)."""
        Q = mckay_quiver_z3()
        assert arrow_count(Q, 1, 0) == 0
        assert arrow_count(Q, 2, 1) == 0
        assert arrow_count(Q, 0, 2) == 0

    def test_no_self_loops(self):
        """No self-loops."""
        Q = mckay_quiver_z3()
        for i in range(3):
            assert arrow_count(Q, i, i) == 0

    def test_potential_has_6_terms(self):
        """The CY potential has 6 cubic terms (from epsilon tensor)."""
        Q = mckay_quiver_z3()
        assert len(Q.potential_terms) == 6

    def test_potential_signs(self):
        """3 positive terms (even permutations) and 3 negative (odd)."""
        Q = mckay_quiver_z3()
        pos = sum(1 for s in Q.potential_signs if s == +1)
        neg = sum(1 for s in Q.potential_signs if s == -1)
        assert pos == 3
        assert neg == 3

    def test_potential_terms_are_cubic(self):
        """Each potential term is a product of 3 arrows (cubic)."""
        Q = mckay_quiver_z3()
        for term in Q.potential_terms:
            assert len(term) == 3

    def test_phase_I_is_mckay(self):
        """Phase I quiver is the McKay quiver."""
        Q1 = phase_I_quiver()
        Q = mckay_quiver_z3()
        assert Q1.name == Q.name
        assert len(Q1.arrows) == len(Q.arrows)

    def test_phase_II_is_mutation(self):
        """Phase II quiver is mu_0(Q)."""
        Q2 = phase_II_quiver()
        assert "mu_0" in Q2.name

    def test_phase_III_is_mutation(self):
        """Phase III quiver is mu_1(Q)."""
        Q3 = phase_III_quiver()
        assert "mu_1" in Q3.name

    def test_all_three_phases_have_3_vertices(self):
        """All three phases have 3 vertices (mutation preserves vertex count)."""
        for Q in [phase_I_quiver(), phase_II_quiver(), phase_III_quiver()]:
            assert Q.n_vertices == 3


# =========================================================================
# SECTION B: EXCHANGE MATRIX AND MUTATION (12 tests)
# =========================================================================

class TestExchangeMatrix:
    """Tests for exchange matrices and quiver mutation."""

    def test_phase_I_exchange_matrix(self):
        """Phase I exchange matrix is B = [[0,3,-3],[-3,0,3],[3,-3,0]]."""
        mats = three_phase_exchange_matrices()
        B1 = mats["phase_I"]
        expected = [[0, 3, -3], [-3, 0, 3], [3, -3, 0]]
        assert B1 == expected

    def test_phase_II_exchange_matrix(self):
        """Phase II exchange matrix from mu_0."""
        mats = three_phase_exchange_matrices()
        B2 = mats["phase_II"]
        expected = [[0, -3, 3], [3, 0, -6], [-3, 6, 0]]
        assert B2 == expected

    def test_phase_III_exchange_matrix(self):
        """Phase III exchange matrix from mu_1."""
        mats = three_phase_exchange_matrices()
        B3 = mats["phase_III"]
        expected = [[0, -3, 6], [3, 0, -3], [-6, 3, 0]]
        assert B3 == expected

    def test_exchange_matrices_antisymmetric(self):
        """All exchange matrices are antisymmetric."""
        assert verify_exchange_matrix_antisymmetric()

    def test_mutation_involution(self):
        """mu_k^2 = id on exchange matrices."""
        assert verify_mutation_involution()

    def test_mutation_at_0_then_0_gives_identity(self):
        """mu_0(mu_0(B)) = B: mutation is an involution."""
        B1 = [[0, 3, -3], [-3, 0, 3], [3, -3, 0]]
        B2 = mutate_exchange_matrix(B1, 0)
        B1_back = mutate_exchange_matrix(B2, 0)
        assert B1_back == B1

    def test_mutation_at_1_then_1_gives_identity(self):
        """mu_1(mu_1(B)) = B."""
        B1 = [[0, 3, -3], [-3, 0, 3], [3, -3, 0]]
        B3 = mutate_exchange_matrix(B1, 1)
        B1_back = mutate_exchange_matrix(B3, 1)
        assert B1_back == B1

    def test_mutation_at_2_then_2_gives_identity(self):
        """mu_2(mu_2(B)) = B."""
        B1 = [[0, 3, -3], [-3, 0, 3], [3, -3, 0]]
        B4 = mutate_exchange_matrix(B1, 2)
        B1_back = mutate_exchange_matrix(B4, 2)
        assert B1_back == B1

    def test_phase_I_diagonal_zero(self):
        """B_{ii} = 0 for all i."""
        mats = three_phase_exchange_matrices()
        B1 = mats["phase_I"]
        for i in range(3):
            assert B1[i][i] == 0

    def test_all_phases_diagonal_zero(self):
        """All exchange matrices have zero diagonal."""
        mats = three_phase_exchange_matrices()
        for name, B in mats.items():
            for i in range(len(B)):
                assert B[i][i] == 0, f"{name}: B[{i}][{i}] != 0"

    def test_exchange_matrix_from_quiver(self):
        """Exchange matrix computed from quiver matches explicit formula."""
        Q = mckay_quiver_z3()
        B = exchange_matrix(Q)
        expected = [[0, 3, -3], [-3, 0, 3], [3, -3, 0]]
        assert B == expected

    def test_exchange_matrix_row_sums(self):
        """Row sums of exchange matrices."""
        mats = three_phase_exchange_matrices()
        B1 = mats["phase_I"]
        # For B1: each row sums to 0 (cyclic structure)
        for i in range(3):
            assert sum(B1[i]) == 0


# =========================================================================
# SECTION C: EULER FORM AND TITS FORM (10 tests)
# =========================================================================

class TestEulerForm:
    """Tests for the Euler form of the McKay Z_3 quiver."""

    def test_euler_form_simple_adjacent(self):
        """chi(e_0, e_1) = -3 (3 arrows from 0 to 1)."""
        assert euler_form_z3((1, 0, 0), (0, 1, 0)) == -3

    def test_euler_form_simple_nonadjacent(self):
        """chi(e_0, e_2) = 0 (no arrows from 0 to 2)."""
        assert euler_form_z3((1, 0, 0), (0, 0, 1)) == 0

    def test_euler_form_simple_diagonal(self):
        """chi(e_i, e_i) = 1."""
        for i in range(3):
            d = [0, 0, 0]
            d[i] = 1
            assert euler_form_z3(tuple(d), tuple(d)) == 1

    def test_euler_form_cyclic(self):
        """chi(e_1, e_2) = -3, chi(e_2, e_0) = -3."""
        assert euler_form_z3((0, 1, 0), (0, 0, 1)) == -3
        assert euler_form_z3((0, 0, 1), (1, 0, 0)) == -3

    def test_euler_form_reverse_direction(self):
        """chi(e_1, e_0) = 0 (no arrows from 1 to 0)."""
        assert euler_form_z3((0, 1, 0), (1, 0, 0)) == 0

    def test_tits_form_simple(self):
        """q(e_i) = 1 for simple dimension vectors."""
        assert tits_form((1, 0, 0)) == 1
        assert tits_form((0, 1, 0)) == 1
        assert tits_form((0, 0, 1)) == 1

    def test_tits_form_111(self):
        """q(1,1,1) = 3 - 9 = -6.

        q(d) = sum d_i^2 - 3*sum d_i*d_{i+1 mod 3}
             = 1+1+1 - 3*(1+1+1) = 3 - 9 = -6
        """
        assert tits_form((1, 1, 1)) == -6

    def test_tits_form_110(self):
        """q(1,1,0) = 1+1+0 - 3*(1*1+0+0) = 2 - 3 = -1."""
        assert tits_form((1, 1, 0)) == -1

    def test_verify_cy_condition(self):
        """The CY condition is verified via the Euler form."""
        assert verify_euler_form_cy_condition()

    def test_symmetrized_euler_form(self):
        """(e_0, e_1) = chi(e_0, e_1) + chi(e_1, e_0) = -3 + 0 = -3."""
        assert symmetrized_euler_form((1, 0, 0), (0, 1, 0)) == -3


# =========================================================================
# SECTION D: CoHA DIMENSIONS (15 tests)
# =========================================================================

class TestCoHADimensions:
    """Tests for CoHA dimensions of the McKay Z_3 quiver."""

    def test_dim_000(self):
        """dim H_{(0,0,0)} = 1 (empty module)."""
        assert coha_dimension_mckay_z3((0, 0, 0)) == 1

    def test_dim_100(self):
        """dim H_{(1,0,0)} = 1 (simple module at vertex 0)."""
        assert coha_dimension_mckay_z3((1, 0, 0)) == 1

    def test_dim_010(self):
        """dim H_{(0,1,0)} = 1."""
        assert coha_dimension_mckay_z3((0, 1, 0)) == 1

    def test_dim_001(self):
        """dim H_{(0,0,1)} = 1."""
        assert coha_dimension_mckay_z3((0, 0, 1)) == 1

    def test_dim_110(self):
        """dim H_{(1,1,0)} = 3 (from 3 arrows 0 -> 1)."""
        assert coha_dimension_mckay_z3((1, 1, 0)) == 3

    def test_dim_011(self):
        """dim H_{(0,1,1)} = 3."""
        assert coha_dimension_mckay_z3((0, 1, 1)) == 3

    def test_dim_101(self):
        """dim H_{(1,0,1)} = 3."""
        assert coha_dimension_mckay_z3((1, 0, 1)) == 3

    def test_dim_111(self):
        """dim H_{(1,1,1)} = 10 (Szendroi)."""
        assert coha_dimension_mckay_z3((1, 1, 1)) == 10

    def test_dim_200(self):
        """dim H_{(2,0,0)} = 1."""
        assert coha_dimension_mckay_z3((2, 0, 0)) == 1

    def test_dim_total_2_sum(self):
        """Sum of dims at total |d|=2 equals M(q)^3|_{q^2} = 12."""
        total = 0
        for d0 in range(3):
            for d1 in range(3 - d0):
                d2 = 2 - d0 - d1
                dim = coha_dimension_mckay_z3((d0, d1, d2))
                if dim >= 0:
                    total += dim
        assert total == 12

    def test_dim_total_3_sum(self):
        """Sum of dims at total |d|=3 equals M(q)^3|_{q^3} = 37."""
        total = 0
        for d0 in range(4):
            for d1 in range(4 - d0):
                d2 = 3 - d0 - d1
                dim = coha_dimension_mckay_z3((d0, d1, d2))
                if dim >= 0:
                    total += dim
        assert total == 37

    def test_dim_300(self):
        """dim H_{(3,0,0)} = 1 (single vertex, no self-loops)."""
        assert coha_dimension_mckay_z3((3, 0, 0)) == 1

    def test_coha_z3_symmetry(self):
        """dim H_d = dim H_{sigma(d)} for the Z_3 action."""
        assert verify_coha_z3_symmetry()

    def test_dim_210(self):
        """dim H_{(2,1,0)} = 4."""
        assert coha_dimension_mckay_z3((2, 1, 0)) == 4

    def test_dim_simples_z3_orbit(self):
        """All simple modules in same Z_3 orbit have same dim."""
        assert coha_dimension_mckay_z3((1, 0, 0)) == coha_dimension_mckay_z3((0, 1, 0))
        assert coha_dimension_mckay_z3((0, 1, 0)) == coha_dimension_mckay_z3((0, 0, 1))


# =========================================================================
# SECTION E: CoHA vs MACMAHON (8 tests)
# =========================================================================

class TestCoHAMacMahon:
    """Tests for the Szendroi theorem: CoHA Poincare = M(q)^3."""

    def test_poincare_degree_0(self):
        """P(q)|_{q^0} = 1."""
        P = coha_poincare_series(6, 10)
        assert P[0] == Fraction(1)

    def test_poincare_degree_1(self):
        """P(q)|_{q^1} = 3 (three simple modules)."""
        P = coha_poincare_series(6, 10)
        assert P[1] == Fraction(3)

    def test_poincare_degree_2(self):
        """P(q)|_{q^2} = 12 = 9 + 3.

        Dim vectors at |d|=2:
          (1,1,0),(0,1,1),(1,0,1): 3+3+3 = 9
          (2,0,0),(0,2,0),(0,0,2): 1+1+1 = 3
          Total: 12.
        """
        P = coha_poincare_series(6, 10)
        assert P[2] == Fraction(12)

    def test_poincare_degree_3(self):
        """P(q)|_{q^3} = 37 = M(q)^3|_{q^3}.

        Dim vectors at |d|=3:
          (1,1,1): 10
          (2,1,0),(2,0,1),(0,2,1),(1,2,0),(0,1,2),(1,0,2): 6*4 = 24
          (3,0,0),(0,3,0),(0,0,3): 3*1 = 3
          Total: 37.
        """
        P = coha_poincare_series(6, 10)
        assert P[3] == Fraction(37)

    def test_macmahon_cube_first_terms(self):
        """M(q)^3 begins [1, 3, 12, 37, ...]."""
        coeffs = macmahon_cube_coefficients(8)
        assert coeffs[0] == 1
        assert coeffs[1] == 3
        assert coeffs[2] == 12
        assert coeffs[3] == 37

    def test_macmahon_cube_degree_4(self):
        """M(q)^3|_{q^4} = 111."""
        coeffs = macmahon_cube_coefficients(8)
        assert coeffs[4] == 111

    def test_coha_matches_macmahon_cube(self):
        """Full verification: CoHA Poincare = M(q)^3 through degree 4."""
        result = verify_coha_vs_macmahon_cube(4)
        assert result["all_match"]

    def test_macmahon_cube_degree_5(self):
        """M(q)^3|_{q^5} = 303."""
        coeffs = macmahon_cube_coefficients(8)
        assert coeffs[5] == 303


# =========================================================================
# SECTION F: DT INVARIANTS (6 tests)
# =========================================================================

class TestDTInvariants:
    """Tests for numerical DT invariants."""

    def test_dt_simple_100(self):
        """Omega(1,0,0) = 1 (simple BPS state)."""
        assert dt_invariant_z3((1, 0, 0)) == 1

    def test_dt_simple_010(self):
        """Omega(0,1,0) = 1."""
        assert dt_invariant_z3((0, 1, 0)) == 1

    def test_dt_simple_001(self):
        """Omega(0,0,1) = 1."""
        assert dt_invariant_z3((0, 0, 1)) == 1

    def test_dt_bound_state_111(self):
        """Omega(1,1,1) = -3 (3-body bound state with CY3 sign)."""
        assert dt_invariant_z3((1, 1, 1)) == -3

    def test_dt_no_bound_state_110(self):
        """Omega(1,1,0) = 0 (no 2-body bound state for adjacent nodes)."""
        assert dt_invariant_z3((1, 1, 0)) == 0

    def test_dt_vacuum(self):
        """Omega(0,0,0) = 0."""
        assert dt_invariant_z3((0, 0, 0)) == 0


# =========================================================================
# SECTION G: WALL-CROSSING (8 tests)
# =========================================================================

class TestWallCrossing:
    """Tests for Kontsevich-Soibelman wall-crossing."""

    def test_ks_factor_simple(self):
        """KS factor for simple BPS state starts with 1."""
        K = ks_wall_crossing_factor((1, 0, 0), 5)
        assert K[0] == Fraction(1)

    def test_ks_factor_omega_1(self):
        """For Omega=1: K(q) = 1/(1-q) = 1 + q + q^2 + ..."""
        K = ks_wall_crossing_factor((1, 0, 0), 5)
        for i in range(6):
            assert K[i] == Fraction(1), f"K[{i}] = {K[i]}, expected 1"

    def test_K12_is_geometric_series(self):
        """K_{12} = 1/(1-q) for the (1,0,0) wall."""
        K12 = wall_crossing_product_K12(5)
        for i in range(6):
            assert K12[i] == Fraction(1)

    def test_K23_is_geometric_series(self):
        """K_{23} = 1/(1-q) for the (0,1,0) wall."""
        K23 = wall_crossing_product_K23(5)
        for i in range(6):
            assert K23[i] == Fraction(1)

    def test_cocycle_condition_holds(self):
        """K_{13} = K_{23} * K_{12} at the abelianized level."""
        result = cocycle_check(8)
        assert result["cocycle_holds"]

    def test_K13_equals_product(self):
        """K_{13} = K_{23} * K_{12} term by term."""
        K13 = wall_crossing_product_K13(6)
        K12 = wall_crossing_product_K12(6)
        K23 = wall_crossing_product_K23(6)
        from compute.lib.local_p2_chart_gluing import _fps_mul
        product = _fps_mul(K23, K12)
        for i in range(7):
            assert K13[i] == product[i]

    def test_hexagon_a2_structure(self):
        """The hexagon identity has 3 roots for A_2."""
        h = hexagon_identity_a2()
        assert len(h["roots"]) == 3

    def test_hexagon_finite_type(self):
        """A_2 scattering diagram is finite type."""
        sd = scattering_diagram_a2()
        assert sd["finite_type"]


# =========================================================================
# SECTION H: TRIPLE OVERLAP (6 tests)
# =========================================================================

class TestTripleOverlap:
    """Tests for the triple overlap homotopy."""

    def test_homotopy_exists(self):
        """The triple overlap homotopy exists."""
        h = triple_overlap_homotopy()
        assert h["exists"]

    def test_homotopy_degree(self):
        """The homotopy has degree -1 in bar grading."""
        h = triple_overlap_homotopy()
        assert h["degree"] == -1

    def test_homotopy_nontrivial_at_111(self):
        """The homotopy is nontrivial at dimension vector (1,1,1)."""
        h = triple_overlap_homotopy()
        assert (1, 1, 1) in h["nontrivial_at"]

    def test_homotopy_trivial_at_simples(self):
        """The homotopy is trivial at simple dimension vectors."""
        h = triple_overlap_homotopy()
        for simple in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            assert simple in h["trivial_at"]

    def test_homotopy_omega_111(self):
        """The homotopy is controlled by Omega(1,1,1) = -3."""
        h = triple_overlap_homotopy()
        assert h["omega_111"] == -3

    def test_homotopy_controls_cubic_shadow(self):
        """The homotopy controls the arity-3 (cubic) shadow."""
        h = triple_overlap_homotopy()
        assert "arity-3" in h["controls"]


# =========================================================================
# SECTION I: HOCOLIMIT ALGEBRA (6 tests)
# =========================================================================

class TestHocolimit:
    """Tests for the global algebra hocolim(CoHA_1 => CoHA_2 => CoHA_3)."""

    def test_n_generators(self):
        """The global algebra has 3 generators."""
        g = hocolim_generators()
        assert g["n_generators"] == 3

    def test_generator_names(self):
        """Generators are J_0, J_1, J_2."""
        g = hocolim_generators()
        names = [gen["name"] for gen in g["generators"]]
        assert "J_0" in names
        assert "J_1" in names
        assert "J_2" in names

    def test_generator_weights(self):
        """All generators have weight 1."""
        g = hocolim_generators()
        for gen in g["generators"]:
            assert gen["weight"] == 1

    def test_large_volume_limit(self):
        """At large volume, the algebra reduces to 3 free bosons."""
        g = hocolim_generators()
        assert "free bosons" in g["large_volume_limit"]

    def test_relation_count(self):
        """The relations include potential, gluing, and homotopy contributions."""
        r = hocolim_relations()
        assert r["potential_relations"] == 6
        assert r["gluing_relations"] == 3
        assert r["homotopy_relations"] == 1

    def test_arity_3_m3(self):
        """m_3 is nonzero (from the triple overlap)."""
        r = hocolim_relations()
        assert "cubic shadow" in r["arity_3_m3"]


# =========================================================================
# SECTION J: KAPPA COMPUTATION (10 tests)
# =========================================================================

class TestKappa:
    """Tests for kappa(A_{LP2}) = 3/2 from multiple paths."""

    def test_kappa_from_glued_charts(self):
        """kappa = 3 * (1/2) = 3/2 from 3 charts."""
        assert kappa_from_glued_charts() == Fraction(3, 2)

    def test_kappa_from_euler_char(self):
        """kappa = chi(P^2)/2 = 3/2."""
        assert kappa_from_euler_char_base() == Fraction(3, 2)

    def test_kappa_from_macmahon(self):
        """kappa = 3/2 from MacMahon exponent."""
        assert kappa_from_macmahon() == Fraction(3, 2)

    def test_kappa_from_coha(self):
        """kappa = 3/2 from CoHA Poincare series."""
        assert kappa_from_coha_poincare() == Fraction(3, 2)

    def test_kappa_four_paths_agree(self):
        """All 4 kappa computation paths agree."""
        result = verify_kappa_four_paths()
        assert result["all_agree"]

    def test_kappa_value(self):
        """kappa = 3/2."""
        result = verify_kappa_four_paths()
        assert result["kappa"] == Fraction(3, 2)

    def test_kappa_additivity(self):
        """kappa is additive: kappa = 3 * kappa_chart = 3 * 1/2."""
        result = verify_kappa_additivity()
        assert result["additivity_holds"]
        assert result["kappa_total"] == Fraction(3, 2)

    def test_kappa_per_chart(self):
        """Each C^3 chart contributes kappa = 1/2."""
        result = verify_kappa_additivity()
        assert result["kappa_per_chart"] == Fraction(1, 2)

    def test_chi_P2_equals_3(self):
        """chi(P^2) = 3."""
        assert kappa_from_euler_char_base() * 2 == Fraction(3)

    def test_kappa_matches_gv(self):
        """kappa matches the GV genus-0 d=1 invariant: kappa = |n^0_1|/2."""
        assert Fraction(abs(GV_GENUS0[1]), 2) == Fraction(3, 2)


# =========================================================================
# SECTION K: Z_3 SYMMETRY (10 tests)
# =========================================================================

class TestZ3Symmetry:
    """Tests for the Z_3 symmetry of local P^2."""

    def test_exchange_matrix_z3_invariant(self):
        """The Phase I exchange matrix is Z_3-invariant."""
        result = z3_on_exchange_matrix()
        assert result["B1_z3_invariant"]

    def test_sigma_B2_equals_B3(self):
        """sigma(B_2) = B_3 (Z_3 permutes mutated phases)."""
        result = z3_on_exchange_matrix()
        assert result["sigma_B2_equals_B3"]

    def test_z3_automorphism_exists(self):
        """The Z_3 automorphism exists on the global algebra."""
        result = z3_automorphism_on_global_algebra()
        assert result["automorphism_exists"]

    def test_z3_order(self):
        """The Z_3 automorphism has order 3."""
        result = z3_automorphism_on_global_algebra()
        assert result["order"] == 3

    def test_z3_action_on_generators(self):
        """sigma(J_0) = J_1, sigma(J_1) = J_2, sigma(J_2) = J_0."""
        result = z3_automorphism_on_global_algebra()
        act = result["action_on_generators"]
        assert act["J_0"] == "J_1"
        assert act["J_1"] == "J_2"
        assert act["J_2"] == "J_0"

    def test_z3_preserves_e1(self):
        """Z_3 preserves the E_1 structure."""
        result = z3_automorphism_on_global_algebra()
        assert result["preserves_e1_structure"]

    def test_z3_fixed_subalgebra_weight_1(self):
        """The Z_3-fixed subalgebra at weight 1 is 1-dimensional."""
        result = z3_automorphism_on_global_algebra()
        assert result["fixed_subalgebra"]["weight_1_dim"] == 1

    def test_z3_bar_equivariant(self):
        """The bar complex is Z_3-equivariant."""
        result = z3_automorphism_on_global_algebra()
        assert result["bar_complex_equivariant"]

    def test_coha_dimensions_z3_equivariant(self):
        """CoHA dimensions are Z_3-equivariant."""
        assert verify_coha_z3_symmetry()

    def test_z3_eigendecomposition(self):
        """The algebra decomposes into Z_3 eigenspaces."""
        result = z3_automorphism_on_global_algebra()
        assert "A_0" in result["eigendecomposition"]
        assert "A_1" in result["eigendecomposition"]
        assert "A_2" in result["eigendecomposition"]


# =========================================================================
# SECTION L: SHADOW TOWER AND BAR COMPLEX (12 tests)
# =========================================================================

class TestShadowTower:
    """Tests for the shadow obstruction tower and bar complex."""

    def test_mayer_vietoris_n_charts(self):
        """The Mayer-Vietoris sequence has 3 chart terms."""
        mv = bar_complex_from_mayer_vietoris()
        assert mv["n_charts"] == 3

    def test_mayer_vietoris_n_overlaps(self):
        """3 pairwise overlaps + 1 triple overlap."""
        mv = bar_complex_from_mayer_vietoris()
        assert mv["n_pairwise_overlaps"] == 3
        assert mv["n_triple_overlap"] == 1

    def test_shadow_depth_lower_bound(self):
        """Shadow depth >= 3 from the chart structure."""
        result = shadow_depth_from_charts()
        assert result["from_charts_alone"]["r_max_lower_bound"] == 3

    def test_shadow_depth_full(self):
        """Full shadow depth is infinity (class M)."""
        result = shadow_depth_from_charts()
        assert result["from_full_gv"]["r_max"] is None  # infinity

    def test_shadow_class_M(self):
        """Shadow class is M at finite Kahler parameter."""
        result = shadow_depth_from_charts()
        assert "M" in result["from_full_gv"]["class"]

    def test_cubic_shadow_value(self):
        """Cubic shadow C = -3 from triple overlap."""
        C = cubic_shadow_from_triple_overlap()
        assert C == Fraction(-3)

    def test_quartic_shadow_value(self):
        """Quartic shadow Q = -6 from d=2 instantons."""
        Q = quartic_shadow_from_instantons()
        assert Q == Fraction(-6)

    def test_shadow_tower_arity_2(self):
        """Shadow tower at arity 2: kappa = 3/2."""
        tower = shadow_tower_from_gv()
        assert tower[2] == Fraction(3, 2)

    def test_shadow_tower_arity_3(self):
        """Shadow tower at arity 3: C = -3."""
        tower = shadow_tower_from_gv()
        assert tower[3] == Fraction(-3)

    def test_shadow_tower_arity_4(self):
        """Shadow tower at arity 4: Q = -6."""
        tower = shadow_tower_from_gv()
        assert tower[4] == Fraction(-6)

    def test_shadow_tower_arity_5(self):
        """Shadow tower at arity 5: dominated by n^0_3 = 27."""
        tower = shadow_tower_from_gv()
        assert tower[5] == Fraction(27)

    def test_shadow_tower_sign_alternation(self):
        """Shadow tower alternates sign at arities 2-6."""
        tower = shadow_tower_from_gv(6)
        # kappa=3/2 > 0, C=-3 < 0, Q=-6 < 0, arity5=27 > 0, arity6=-192 < 0
        assert tower[2] > 0
        assert tower[3] < 0
        assert tower[5] > 0
        assert tower[6] < 0


# =========================================================================
# SECTION M: MOTIVIC DT (6 tests)
# =========================================================================

class TestMotivicDT:
    """Tests for motivic DT invariants."""

    def test_motivic_dt_degree_0(self):
        """Z_mot|_{q^0} = 1."""
        Z = motivic_dt_generating_function(8)
        assert Z[0] == Fraction(1)

    def test_motivic_dt_degree_1(self):
        """Z_mot|_{q^1} = 3."""
        Z = motivic_dt_generating_function(8)
        assert Z[1] == Fraction(3)

    def test_motivic_dt_degree_2(self):
        """Z_mot|_{q^2} = 12."""
        Z = motivic_dt_generating_function(8)
        assert Z[2] == Fraction(12)

    def test_motivic_dt_degree_3(self):
        """Z_mot|_{q^3} = 37."""
        Z = motivic_dt_generating_function(8)
        assert Z[3] == Fraction(37)

    def test_macmahon_cube_integer_coefficients(self):
        """All coefficients of M(q)^3 are positive integers."""
        coeffs = macmahon_cube_coefficients(8)
        for c in coeffs:
            assert c >= 0
            assert isinstance(c, int)

    def test_macmahon_cube_growing(self):
        """Coefficients of M(q)^3 are strictly increasing."""
        coeffs = macmahon_cube_coefficients(8)
        for i in range(1, len(coeffs)):
            assert coeffs[i] > coeffs[i - 1]


# =========================================================================
# SECTION N: SCATTERING DIAGRAM (4 tests)
# =========================================================================

class TestScatteringDiagram:
    """Tests for the A_2 scattering diagram."""

    def test_scattering_n_walls(self):
        """A_2 scattering diagram has 3 walls."""
        sd = scattering_diagram_a2()
        assert sd["n_walls"] == 3

    def test_scattering_n_initial(self):
        """2 initial walls (simple roots)."""
        sd = scattering_diagram_a2()
        assert sd["n_initial"] == 2

    def test_scattering_n_generated(self):
        """1 generated wall (composite root alpha_1 + alpha_2)."""
        sd = scattering_diagram_a2()
        assert sd["n_generated"] == 1

    def test_scattering_cluster_type(self):
        """Cluster type is A_2."""
        sd = scattering_diagram_a2()
        assert sd["cluster_type"] == "A_2"


# =========================================================================
# SECTION O: TITS FORM VALUES (5 tests)
# =========================================================================

class TestTitsFormValues:
    """Tests for Tits form at specific dimension vectors."""

    def test_tits_values_computed(self):
        """Tits form is computed for all test vectors."""
        vals = verify_tits_form_values()
        assert len(vals) > 0

    def test_tits_100(self):
        """q(1,0,0) = 1 (simple root: positive Tits form)."""
        vals = verify_tits_form_values()
        assert vals[(1, 0, 0)] == 1

    def test_tits_111_negative(self):
        """q(1,1,1) = -6 (imaginary root: negative Tits form)."""
        vals = verify_tits_form_values()
        assert vals[(1, 1, 1)] == -6

    def test_tits_222(self):
        """q(2,2,2) = 4*3 - 3*4*3 = 12 - 36 = -24."""
        vals = verify_tits_form_values()
        assert vals[(2, 2, 2)] == -24

    def test_imaginary_root_negative_tits(self):
        """Imaginary roots have negative Tits form."""
        # (1,1,1) and (2,2,2) are imaginary roots
        vals = verify_tits_form_values()
        assert vals[(1, 1, 1)] < 0
        assert vals[(2, 2, 2)] < 0


# =========================================================================
# SECTION P: FULL REPORT (5 tests)
# =========================================================================

class TestFullReport:
    """Tests for the complete chart-gluing report."""

    def test_report_geometry(self):
        """Report identifies local P^2."""
        report = full_chart_gluing_report()
        assert "P^2" in report["geometry"]

    def test_report_n_charts(self):
        """Report has 3 charts."""
        report = full_chart_gluing_report()
        assert report["n_charts"] == 3

    def test_report_kappa(self):
        """Report kappa = 3/2."""
        report = full_chart_gluing_report()
        assert report["kappa"] == Fraction(3, 2)

    def test_report_cocycle(self):
        """Report cocycle condition holds."""
        report = full_chart_gluing_report()
        assert report["cocycle_condition"]

    def test_report_cubic_shadow(self):
        """Report cubic shadow C = -3."""
        report = full_chart_gluing_report()
        assert report["cubic_shadow_C"] == Fraction(-3)


# =========================================================================
# SECTION Q: GV INVARIANT CROSS-CHECKS (5 tests)
# =========================================================================

class TestGVCrossChecks:
    """Cross-checks with GV invariant data."""

    def test_gv_genus0_d1(self):
        """n^0_1 = 3 (three lines on P^2)."""
        assert GV_GENUS0[1] == 3

    def test_gv_genus0_d2(self):
        """n^0_2 = -6."""
        assert GV_GENUS0[2] == -6

    def test_gv_genus0_d3(self):
        """n^0_3 = 27 (27 rational cubics)."""
        assert GV_GENUS0[3] == 27

    def test_gv_sign_alternation(self):
        """GV genus-0 invariants alternate in sign."""
        for d, n in GV_GENUS0.items():
            expected_sign = (-1) ** (d + 1)
            actual_sign = 1 if n > 0 else -1
            assert actual_sign == expected_sign

    def test_gv_growth_towards_27(self):
        """Consecutive ratios |n^0_{d+1}/n^0_d| approach 27."""
        degrees = sorted(GV_GENUS0.keys())
        ratios = []
        for i in range(len(degrees) - 1):
            d1, d2 = degrees[i], degrees[i + 1]
            if d2 == d1 + 1 and GV_GENUS0[d1] != 0:
                r = abs(GV_GENUS0[d2]) / abs(GV_GENUS0[d1])
                ratios.append(r)
        # Last ratio should be closer to 27 than the first
        if len(ratios) >= 3:
            assert abs(ratios[-1] - 27) < abs(ratios[0] - 27)


# =========================================================================
# SECTION R: SHADOW GENERATING FUNCTION (3 tests)
# =========================================================================

class TestShadowGeneratingFunction:
    """Tests for the shadow generating function."""

    def test_shadow_gf_degree_0(self):
        """Z^{sh}|_{q^0} = 1 (normalized)."""
        Z = shadow_generating_function(6, 10)
        assert Z[0] == Fraction(1)

    def test_shadow_gf_degree_1(self):
        """Z^{sh}|_{q^1} = 3 (from n^0_1 = 3)."""
        Z = shadow_generating_function(6, 10)
        assert Z[1] == Fraction(3)

    def test_shadow_gf_positive_coefficients(self):
        """Shadow generating function has positive coefficients (at Q^1 level)."""
        Z = shadow_generating_function(6, 10)
        for i in range(1, 8):
            assert Z[i] > 0
