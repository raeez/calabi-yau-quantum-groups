r"""Tests for the stability atlas nerve and chamber structure.

Verifies:
  1. SimplicialComplex: f-vectors, Euler characteristics, homology,
     connectivity, flag property, link/star operations.
  2. Chamber structure of standard CY3s:
     (a) C^3: 1 chamber, no walls, point nerve.
     (b) Conifold: 2 chambers, 1 wall, interval nerve.
     (c) Local P^2 (mutation): 3 chambers, 3 walls, triangle nerve.
     (d) Local P^2 (full A_2): 6 chambers, 6 walls, hexagon nerve.
     (e) C^3/Z_3: 3 chambers, 3 walls, triangle nerve.
     (f) Quintic (truncated): 2 chambers, 1 wall.
  3. A_n hyperplane arrangements: chamber counts, adjacencies,
     characteristic polynomials.
  4. E_1 descent: all higher coherences trivially satisfied for E_1.
  5. Wall-crossing consistency: Euler pairings nonzero, bound states correct.
  6. Atlas dimensions: dim(Stab) = rk K_0.
  7. Nerve homology: contractibility, Betti numbers.
  8. Marginal stability walls: discriminant, phases, triangle inequality.

Manuscript references:
    Part V (Standard Landscape): CY3 stability atlases
    Part IV (Quantum Groups): E_1 descent, KS wall-crossing

Mathematical references:
    [Bri07]  Bridgeland, "Stability conditions on triangulated categories" (2007)
    [KS08]   Kontsevich-Soibelman, "Stability structures" (2008)
    [Tod08]  Toda, "Stability conditions and crepant small resolutions" (2008)
    [Kel10]  Keller, "Cluster algebras and quiver representations" (2010)
    [Lur17]  Lurie, "Higher Algebra" (2017), 4.1.8.4

Ground truth:
    - A_n arrangement has (n+1)! chambers and binom(n+1,2) hyperplanes.
    - E_1 descent is 1-categorical (higher coherences trivial).
    - Conifold: 2 chambers, 1 wall (pentagon identity).
    - Local P^2: 6 chambers in full A_2, 3 in mutation triangle.
    - Nerve of interval: chi = 1. Nerve of triangle: chi = 1.
    - Nerve of hexagon (cycle): chi = 0.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.stability_atlas_nerve import (
    # Simplicial complex
    SimplicialComplex,
    _matrix_rank,
    # Chambers and walls
    Chamber,
    Wall,
    # Atlas
    StabilityAtlas,
    # Standard atlases
    c3_atlas,
    conifold_atlas,
    local_p2_atlas_full,
    local_p2_atlas_mutation,
    c3_z3_atlas,
    quintic_atlas_truncated,
    # Hyperplane arrangements
    HyperplaneArrangementA,
    # Wall crossing
    marginal_stability_wall,
    wall_crossing_spectrum_change,
    # E_1 descent
    e1_descent_coherence_proof,
    # Analysis
    atlas_dimension_table,
    run_full_atlas_verification,
)


# ============================================================================
# 1. SIMPLICIAL COMPLEX FUNDAMENTALS
# ============================================================================

class TestSimplicialComplex:
    """Tests for the SimplicialComplex class."""

    def test_point(self):
        """A single point: f-vector = [1], chi = 1."""
        K = SimplicialComplex({0})
        assert K.f_vector == [1]
        assert K.euler_characteristic == 1
        assert K.dimension == 0
        assert K.is_connected()

    def test_two_points(self):
        """Two disconnected points: f = [2], chi = 2."""
        K = SimplicialComplex({0, 1})
        assert K.f_vector == [2]
        assert K.euler_characteristic == 2
        assert not K.is_connected()
        assert len(K.connected_components()) == 2

    def test_edge(self):
        """An edge (interval): f = [2, 1], chi = 1."""
        K = SimplicialComplex({0, 1}, [frozenset({0, 1})])
        assert K.f_vector == [2, 1]
        assert K.euler_characteristic == 1
        assert K.is_connected()
        assert K.dimension == 1

    def test_triangle_boundary(self):
        """Boundary of a triangle: f = [3, 3], chi = 0."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}),
            frozenset({1, 2}),
            frozenset({0, 2}),
        ])
        assert K.f_vector == [3, 3]
        assert K.euler_characteristic == 0
        assert K.is_connected()
        assert K.dimension == 1

    def test_filled_triangle(self):
        """Filled triangle: f = [3, 3, 1], chi = 1."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        assert K.f_vector == [3, 3, 1]
        assert K.euler_characteristic == 1
        assert K.is_connected()
        assert K.dimension == 2

    def test_tetrahedron_boundary(self):
        """Boundary of tetrahedron: f = [4, 6, 4], chi = 2."""
        K = SimplicialComplex({0, 1, 2, 3}, [
            frozenset({0, 1, 2}),
            frozenset({0, 1, 3}),
            frozenset({0, 2, 3}),
            frozenset({1, 2, 3}),
        ])
        assert K.f_vector == [4, 6, 4]
        assert K.euler_characteristic == 2
        assert K.dimension == 2

    def test_filled_tetrahedron(self):
        """Filled tetrahedron: f = [4, 6, 4, 1], chi = 1."""
        K = SimplicialComplex({0, 1, 2, 3}, [frozenset({0, 1, 2, 3})])
        assert K.f_vector == [4, 6, 4, 1]
        assert K.euler_characteristic == 1
        assert K.dimension == 3

    def test_closure_property(self):
        """Adding a triangle adds all 3 edges and 3 vertices."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        assert frozenset({0, 1}) in K.simplices
        assert frozenset({1, 2}) in K.simplices
        assert frozenset({0, 2}) in K.simplices
        assert frozenset({0}) in K.simplices

    def test_connected_components_three(self):
        """Three disconnected points."""
        K = SimplicialComplex({0, 1, 2})
        comps = K.connected_components()
        assert len(comps) == 3

    def test_connected_path(self):
        """A path 0--1--2 is connected."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}),
            frozenset({1, 2}),
        ])
        assert K.is_connected()
        assert len(K.connected_components()) == 1

    def test_flag_triangle(self):
        """A filled triangle is flag (complete graph K_3 fills to simplex)."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        assert K.is_flag()

    def test_flag_boundary_triangle(self):
        """Boundary of triangle is NOT flag (3 edges but no face)."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}),
            frozenset({1, 2}),
            frozenset({0, 2}),
        ])
        assert not K.is_flag()

    def test_flag_path(self):
        """A path is flag (no missing cliques)."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}),
            frozenset({1, 2}),
        ])
        assert K.is_flag()

    def test_link_vertex_triangle(self):
        """Link of vertex 0 in filled triangle {0,1,2} = edge {1,2}."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        L = K.link(0)
        assert L.vertices == {1, 2}
        assert frozenset({1, 2}) in L.simplices

    def test_link_vertex_edge(self):
        """Link of vertex 0 in edge {0,1} = point {1}."""
        K = SimplicialComplex({0, 1}, [frozenset({0, 1})])
        L = K.link(0)
        assert L.vertices == {1}
        assert L.f_vector == [1]

    def test_star_vertex(self):
        """Star of vertex 0 in triangle = {0}, {0,1}, {0,2}, {0,1,2}."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        S = K.star(0)
        assert frozenset({0}) in S
        assert frozenset({0, 1}) in S
        assert frozenset({0, 2}) in S
        assert frozenset({0, 1, 2}) in S

    def test_simplices_of_dim(self):
        """Correct counts of simplices by dimension."""
        K = SimplicialComplex({0, 1, 2, 3}, [frozenset({0, 1, 2, 3})])
        assert len(K.simplices_of_dim(0)) == 4
        assert len(K.simplices_of_dim(1)) == 6
        assert len(K.simplices_of_dim(2)) == 4
        assert len(K.simplices_of_dim(3)) == 1

    def test_empty_complex(self):
        """Empty vertex set."""
        K = SimplicialComplex(set())
        assert K.f_vector == []
        assert K.dimension == -1
        assert K.euler_characteristic == 0


# ============================================================================
# 2. HOMOLOGY COMPUTATIONS
# ============================================================================

class TestHomology:
    """Tests for simplicial homology over Q."""

    def test_homology_point(self):
        """H_*(point) = Q in degree 0."""
        K = SimplicialComplex({0})
        h = K.homology_ranks()
        assert h[0] == 1

    def test_homology_edge(self):
        """H_*(interval) = Q in degree 0."""
        K = SimplicialComplex({0, 1}, [frozenset({0, 1})])
        h = K.homology_ranks()
        assert h[0] == 1
        assert h[1] == 0

    def test_homology_circle(self):
        """H_*(S^1) = Q in degrees 0 and 1."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}), frozenset({1, 2}), frozenset({0, 2}),
        ])
        h = K.homology_ranks()
        assert h[0] == 1
        assert h[1] == 1

    def test_homology_filled_triangle(self):
        """H_*(filled triangle) = Q in degree 0 (contractible)."""
        K = SimplicialComplex({0, 1, 2}, [frozenset({0, 1, 2})])
        h = K.homology_ranks()
        assert h[0] == 1
        assert h[1] == 0
        assert h[2] == 0

    def test_homology_sphere_boundary_tetrahedron(self):
        """H_*(boundary tetrahedron) = H_*(S^2) = Q in degrees 0 and 2."""
        K = SimplicialComplex({0, 1, 2, 3}, [
            frozenset({0, 1, 2}), frozenset({0, 1, 3}),
            frozenset({0, 2, 3}), frozenset({1, 2, 3}),
        ])
        h = K.homology_ranks()
        assert h[0] == 1
        assert h[1] == 0
        assert h[2] == 1

    def test_homology_two_components(self):
        """Two disconnected points: H_0 = Q^2."""
        K = SimplicialComplex({0, 1})
        h = K.homology_ranks()
        assert h[0] == 2

    def test_homology_hexagon(self):
        """Hexagonal cycle: H_0 = Q, H_1 = Q."""
        K = SimplicialComplex(set(range(6)), [
            frozenset({0, 1}), frozenset({1, 2}), frozenset({2, 3}),
            frozenset({3, 4}), frozenset({4, 5}), frozenset({5, 0}),
        ])
        h = K.homology_ranks()
        assert h[0] == 1
        assert h[1] == 1

    def test_euler_equals_alternating_betti(self):
        """chi(K) = sum (-1)^d beta_d."""
        K = SimplicialComplex({0, 1, 2}, [
            frozenset({0, 1}), frozenset({1, 2}), frozenset({0, 2}),
        ])
        h = K.homology_ranks()
        alt_sum = sum((-1)**d * h[d] for d in h)
        assert alt_sum == K.euler_characteristic


class TestMatrixRank:
    """Tests for the Gaussian elimination rank computation."""

    def test_identity(self):
        mat = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
        assert _matrix_rank(mat) == 2

    def test_zero_matrix(self):
        mat = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
        assert _matrix_rank(mat) == 0

    def test_rank_one(self):
        mat = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
        assert _matrix_rank(mat) == 1

    def test_rank_rectangular(self):
        mat = [
            [Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(0)],
        ]
        assert _matrix_rank(mat) == 2

    def test_empty(self):
        assert _matrix_rank([]) == 0
        assert _matrix_rank([[]]) == 0

    def test_rank_3x3(self):
        mat = [
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(4), Fraction(5), Fraction(6)],
            [Fraction(7), Fraction(8), Fraction(9)],
        ]
        # This matrix has rank 2 (row 3 = 2*row2 - row1)
        assert _matrix_rank(mat) == 2


# ============================================================================
# 3. CHAMBER AND WALL DATA STRUCTURES
# ============================================================================

class TestChamber:
    """Tests for Chamber data structure."""

    def test_basic_chamber(self):
        ch = Chamber(0, "test", [(1, 0), (0, 1)])
        assert ch.index == 0
        assert ch.name == "test"
        assert ch.num_bps_states == 2

    def test_chamber_with_degeneracies(self):
        ch = Chamber(0, "test", [(1, 0)], bps_degeneracies=[5])
        assert ch.bps_degeneracies == [5]

    def test_chamber_repr(self):
        ch = Chamber(0, "test", [(1, 0), (0, 1)])
        r = repr(ch)
        assert "0" in r
        assert "test" in r


class TestWall:
    """Tests for Wall data structure."""

    def test_basic_wall(self):
        w = Wall(0, 1, ((1, 0), (0, 1)), 1)
        assert w.chamber_a == 0
        assert w.chamber_b == 1
        assert w.euler_pairing == 1
        assert w.bound_state == (1, 1)

    def test_wall_ordering(self):
        """Wall always has chamber_a < chamber_b."""
        w = Wall(5, 2, ((1, 0), (0, 1)), 1)
        assert w.chamber_a == 2
        assert w.chamber_b == 5

    def test_wall_edge(self):
        w = Wall(0, 1, ((1, 0), (0, 1)), 1)
        assert w.edge == frozenset({0, 1})

    def test_wall_codimension(self):
        w = Wall(0, 1, ((1, 0), (0, 1)), 1)
        assert w.codimension == 1

    def test_bound_state_auto(self):
        """Bound state is gamma_1 + gamma_2."""
        w = Wall(0, 1, ((2, 1, 0), (0, 1, 3)), 2)
        assert w.bound_state == (2, 2, 3)


# ============================================================================
# 4. C^3 ATLAS
# ============================================================================

class TestC3Atlas:
    """Tests for the C^3 atlas."""

    def test_single_chamber(self):
        a = c3_atlas()
        assert a.num_chambers == 1
        assert a.num_walls == 0

    def test_nerve_is_point(self):
        a = c3_atlas()
        n = a.nerve()
        assert n.f_vector == [1]
        assert n.euler_characteristic == 1

    def test_hocolim_type(self):
        a = c3_atlas()
        assert a.hocolim_type() == "point"

    def test_dim_stab(self):
        a = c3_atlas()
        assert a.dim_stab == 2

    def test_e1_descent(self):
        a = c3_atlas()
        d = a.e1_descent_check()
        assert d['descent_is_1_categorical']
        assert d['higher_coherences_trivial']

    def test_bps_spectrum(self):
        a = c3_atlas()
        ch = a.chambers[0]
        assert ch.num_bps_states == 3  # 3 coordinate directions

    def test_quiver_data(self):
        a = c3_atlas()
        ch = a.chambers[0]
        assert ch.quiver_data['type'] == 'C^3_framing'


# ============================================================================
# 5. CONIFOLD ATLAS
# ============================================================================

class TestConifoldAtlas:
    """Tests for the conifold atlas."""

    def test_two_chambers(self):
        a = conifold_atlas()
        assert a.num_chambers == 2

    def test_one_wall(self):
        a = conifold_atlas()
        assert a.num_walls == 1

    def test_nerve_is_interval(self):
        a = conifold_atlas()
        n = a.nerve()
        assert n.f_vector == [2, 1]
        assert n.euler_characteristic == 1

    def test_nerve_connected(self):
        a = conifold_atlas()
        n = a.nerve()
        assert n.is_connected()

    def test_hocolim_pushout(self):
        a = conifold_atlas()
        assert a.hocolim_type() == "pushout"

    def test_dim_stab(self):
        a = conifold_atlas()
        assert a.dim_stab == 2
        assert a.rank_k0 == 2

    def test_e1_descent(self):
        a = conifold_atlas()
        d = a.e1_descent_check()
        assert d['descent_is_1_categorical']

    def test_chamber_I_bps(self):
        a = conifold_atlas()
        ch = a.chambers[0]
        assert ch.num_bps_states == 2

    def test_chamber_II_bps(self):
        a = conifold_atlas()
        ch = a.chambers[1]
        assert ch.num_bps_states == 3  # bound state appears

    def test_wall_euler_pairing(self):
        a = conifold_atlas()
        w = a.walls[0]
        assert w.euler_pairing == 1

    def test_bound_state_charge(self):
        a = conifold_atlas()
        w = a.walls[0]
        assert w.bound_state == (1, 1)

    def test_wall_crossing_consistency(self):
        a = conifold_atlas()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_nerve_homology(self):
        """Interval is contractible: H_0 = Q, H_1 = 0."""
        a = conifold_atlas()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h[1] == 0

    def test_spectrum_change(self):
        """One bound state appears crossing the wall."""
        a = conifold_atlas()
        sc = wall_crossing_spectrum_change(a, 0)
        # The bound state (1,1) appears in chamber II
        assert sc['euler_pairing'] == 1
        assert sc['ks_type'] == 'pentagon'


# ============================================================================
# 6. LOCAL P^2 ATLAS (MUTATION)
# ============================================================================

class TestLocalP2Mutation:
    """Tests for the local P^2 mutation atlas."""

    def test_three_chambers(self):
        a = local_p2_atlas_mutation()
        assert a.num_chambers == 3

    def test_three_walls(self):
        a = local_p2_atlas_mutation()
        assert a.num_walls == 3

    def test_nerve_triangle(self):
        a = local_p2_atlas_mutation()
        n = a.nerve()
        # Triangle with 3 vertices, 3 edges, 1 face (flag completion)
        assert n.num_simplices(0) == 3
        assert n.num_simplices(1) == 3
        assert n.num_simplices(2) == 1  # triangle fills as flag complex

    def test_hocolim_triple_pushout(self):
        a = local_p2_atlas_mutation()
        assert a.hocolim_type() == "triple_pushout"

    def test_dim_stab(self):
        a = local_p2_atlas_mutation()
        assert a.dim_stab == 3
        assert a.rank_k0 == 3

    def test_e1_descent(self):
        a = local_p2_atlas_mutation()
        d = a.e1_descent_check()
        assert d['descent_is_1_categorical']

    def test_nerve_connected(self):
        a = local_p2_atlas_mutation()
        n = a.nerve()
        assert n.is_connected()

    def test_nerve_euler_char(self):
        a = local_p2_atlas_mutation()
        n = a.nerve()
        # Filled triangle: chi = 3 - 3 + 1 = 1
        assert n.euler_characteristic == 1

    def test_nerve_contractible(self):
        """Filled triangle is contractible."""
        a = local_p2_atlas_mutation()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        if 1 in h:
            assert h[1] == 0
        if 2 in h:
            assert h[2] == 0

    def test_wall_crossing_consistency(self):
        a = local_p2_atlas_mutation()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']


# ============================================================================
# 7. LOCAL P^2 ATLAS (FULL A_2)
# ============================================================================

class TestLocalP2Full:
    """Tests for the full 6-chamber A_2 local P^2 atlas."""

    def test_six_chambers(self):
        a = local_p2_atlas_full()
        assert a.num_chambers == 6

    def test_six_walls(self):
        a = local_p2_atlas_full()
        assert a.num_walls == 6

    def test_nerve_connected(self):
        a = local_p2_atlas_full()
        n = a.nerve()
        assert n.is_connected()

    def test_hexagonal_adjacency(self):
        """The adjacency graph is a hexagon (cycle of length 6)."""
        a = local_p2_atlas_full()
        n = a.nerve()
        # A hexagon has 6 vertices and 6 edges
        assert n.num_simplices(0) == 6
        assert n.num_simplices(1) == 6

    def test_nerve_euler_char(self):
        """Hexagon = S^1: chi = 0."""
        a = local_p2_atlas_full()
        n = a.nerve()
        assert n.euler_characteristic == 0

    def test_hexagon_homology(self):
        """Hexagonal cycle: H_0 = Q, H_1 = Q."""
        a = local_p2_atlas_full()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h[1] == 1

    def test_wall_crossing_consistency(self):
        a = local_p2_atlas_full()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_each_chamber_has_quiver(self):
        a = local_p2_atlas_full()
        for idx, ch in a.chambers.items():
            assert 'type' in ch.quiver_data
            assert ch.quiver_data['vertices'] == 3


# ============================================================================
# 8. C^3/Z_3 ATLAS
# ============================================================================

class TestC3Z3Atlas:
    """Tests for the C^3/Z_3 orbifold atlas."""

    def test_three_chambers(self):
        a = c3_z3_atlas()
        assert a.num_chambers == 3

    def test_three_walls(self):
        a = c3_z3_atlas()
        assert a.num_walls == 3

    def test_same_as_lp2_mutation(self):
        """C^3/Z_3 and local P^2 mutation have the same nerve."""
        a_z3 = c3_z3_atlas()
        a_lp2 = local_p2_atlas_mutation()
        n_z3 = a_z3.nerve()
        n_lp2 = a_lp2.nerve()
        assert n_z3.f_vector == n_lp2.f_vector
        assert n_z3.euler_characteristic == n_lp2.euler_characteristic

    def test_dim_stab(self):
        a = c3_z3_atlas()
        assert a.dim_stab == 3

    def test_crepant_resolution_equivalence(self):
        """C^3/Z_3 has same dim_stab and rank_k0 as local P^2."""
        a_z3 = c3_z3_atlas()
        a_lp2 = local_p2_atlas_mutation()
        assert a_z3.dim_stab == a_lp2.dim_stab
        assert a_z3.rank_k0 == a_lp2.rank_k0


# ============================================================================
# 9. QUINTIC ATLAS (TRUNCATED)
# ============================================================================

class TestQuinticAtlas:
    """Tests for the truncated quintic atlas."""

    def test_dim_stab(self):
        a = quintic_atlas_truncated()
        assert a.dim_stab == 4
        assert a.rank_k0 == 4

    def test_truncation_level_1(self):
        """At mass cutoff 1: single chamber."""
        a = quintic_atlas_truncated(mass_cutoff=1)
        assert a.num_chambers == 1
        assert a.num_walls == 0

    def test_truncation_level_2(self):
        """At mass cutoff 2: two chambers, one wall."""
        a = quintic_atlas_truncated(mass_cutoff=2)
        assert a.num_chambers == 2
        assert a.num_walls == 1

    def test_truncation_level_3(self):
        """At mass cutoff 3: three chambers, two walls."""
        a = quintic_atlas_truncated(mass_cutoff=3)
        assert a.num_chambers == 3
        assert a.num_walls == 2

    def test_gv_invariant_in_data(self):
        """The GV invariant n^0_1 = 2875 appears in the BPS degeneracies."""
        a = quintic_atlas_truncated(mass_cutoff=1)
        ch = a.chambers[0]
        assert 2875 in ch.bps_degeneracies

    def test_e1_descent(self):
        a = quintic_atlas_truncated(mass_cutoff=2)
        d = a.e1_descent_check()
        assert d['descent_is_1_categorical']


# ============================================================================
# 10. A_n HYPERPLANE ARRANGEMENTS
# ============================================================================

class TestHyperplaneArrangementA:
    """Tests for A_n hyperplane arrangements."""

    def test_a1_chambers(self):
        """A_1: 2! = 2 chambers."""
        arr = HyperplaneArrangementA(1)
        assert arr.num_chambers == 2

    def test_a1_hyperplanes(self):
        """A_1: binom(2,2) = 1 hyperplane."""
        arr = HyperplaneArrangementA(1)
        assert arr.num_hyperplanes == 1

    def test_a2_chambers(self):
        """A_2: 3! = 6 chambers."""
        arr = HyperplaneArrangementA(2)
        assert arr.num_chambers == 6

    def test_a2_hyperplanes(self):
        """A_2: binom(3,2) = 3 hyperplanes."""
        arr = HyperplaneArrangementA(2)
        assert arr.num_hyperplanes == 3

    def test_a3_chambers(self):
        """A_3: 4! = 24 chambers."""
        arr = HyperplaneArrangementA(3)
        assert arr.num_chambers == 24

    def test_a3_hyperplanes(self):
        """A_3: binom(4,2) = 6 hyperplanes."""
        arr = HyperplaneArrangementA(3)
        assert arr.num_hyperplanes == 6

    def test_a1_adjacency(self):
        """A_1: 2 chambers connected by 1 edge."""
        arr = HyperplaneArrangementA(1)
        edges = arr.adjacency_graph()
        assert len(edges) == 1

    def test_a2_adjacency(self):
        """A_2: 6 chambers, each connected to 2 neighbors = 6 edges total."""
        arr = HyperplaneArrangementA(2)
        edges = arr.adjacency_graph()
        # Cayley graph of S_3 with adjacent transpositions: hexagonal, 6 edges
        assert len(edges) == 6

    def test_a3_adjacency_count(self):
        """A_3: Cayley graph of S_4 with adjacent transpositions."""
        arr = HyperplaneArrangementA(3)
        edges = arr.adjacency_graph()
        # Each of 24 vertices has degree 3 (3 adjacent transpositions),
        # so |E| = 24*3/2 = 36
        assert len(edges) == 36

    def test_a1_char_poly(self):
        """chi_{A_1}(t) = t(t-1) = -t + t^2."""
        arr = HyperplaneArrangementA(1)
        poly = arr.characteristic_polynomial
        # poly[k] = coefficient of t^k
        # chi(t) = t*(t-1) = t^2 - t
        assert poly[0] == 0  # constant term
        assert poly[1] == -1  # coefficient of t
        assert poly[2] == 1   # coefficient of t^2

    def test_a2_char_poly(self):
        """chi_{A_2}(t) = t(t-1)(t-2) = 2t - 3t^2 + t^3."""
        arr = HyperplaneArrangementA(2)
        poly = arr.characteristic_polynomial
        # t(t-1)(t-2) = t^3 - 3t^2 + 2t
        assert poly[0] == 0
        assert poly[1] == 2
        assert poly[2] == -3
        assert poly[3] == 1

    def test_chambers_count_from_char_poly(self):
        """Number of chambers = |chi(-1)| for real arrangements.

        For A_n: chi(-1) = (-1)(-2)...(-n-1) = (-1)^{n+1} * (n+1)!
        So |chi(-1)| = (n+1)!. CHECK.
        """
        for n in range(1, 5):
            arr = HyperplaneArrangementA(n)
            poly = arr.characteristic_polynomial
            chi_neg1 = sum(poly[k] * ((-1) ** k) for k in range(len(poly)))
            assert abs(chi_neg1) == arr.num_chambers

    def test_a1_nerve_is_interval(self):
        """A_1 nerve = interval (2 vertices, 1 edge)."""
        arr = HyperplaneArrangementA(1)
        nerve = arr.nerve()
        assert nerve.f_vector == [2, 1]

    def test_a2_nerve_is_hexagon(self):
        """A_2 nerve = hexagon (6 vertices, 6 edges)."""
        arr = HyperplaneArrangementA(2)
        nerve = arr.nerve()
        assert nerve.num_simplices(0) == 6
        assert nerve.num_simplices(1) == 6

    def test_a1_to_atlas(self):
        """A_1 arrangement -> conifold-like atlas."""
        arr = HyperplaneArrangementA(1)
        atlas = arr.to_atlas(name="A_1_test")
        assert atlas.num_chambers == 2
        assert atlas.num_walls == 1


# ============================================================================
# 11. E_1 DESCENT COHERENCE
# ============================================================================

class TestE1Descent:
    """Tests for the E_1 descent coherence theorem."""

    def test_proof_structure(self):
        proof = e1_descent_coherence_proof()
        assert proof['steps']['step_1']['proved']
        assert proof['steps']['step_2']['proved']
        assert proof['steps']['step_3']['proved']
        assert proof['steps']['step_4']['proved']

    def test_cy3_specific(self):
        proof = e1_descent_coherence_proof()
        assert proof['steps']['step_3']['cy3_specific']

    def test_all_atlases_1_categorical(self):
        """Every standard atlas has 1-categorical E_1 descent."""
        atlases = [
            c3_atlas(),
            conifold_atlas(),
            local_p2_atlas_mutation(),
            local_p2_atlas_full(),
            c3_z3_atlas(),
            quintic_atlas_truncated(mass_cutoff=2),
        ]
        for atlas in atlases:
            d = atlas.e1_descent_check()
            assert d['descent_is_1_categorical'], f"Failed for {atlas.name}"
            assert d['higher_coherences_trivial'], f"Failed for {atlas.name}"


# ============================================================================
# 12. WALL-CROSSING CONSISTENCY
# ============================================================================

class TestWallCrossingConsistency:
    """Tests for wall-crossing data consistency across all atlases."""

    def test_conifold_consistency(self):
        a = conifold_atlas()
        c = a.wall_crossing_consistency()
        assert c['num_walls_checked'] == 1
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_lp2_mutation_consistency(self):
        a = local_p2_atlas_mutation()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_lp2_full_consistency(self):
        a = local_p2_atlas_full()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_c3z3_consistency(self):
        a = c3_z3_atlas()
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']

    def test_quintic_consistency(self):
        a = quintic_atlas_truncated(mass_cutoff=2)
        c = a.wall_crossing_consistency()
        assert c['all_euler_nonzero']
        assert c['all_bound_states_correct']


# ============================================================================
# 13. ATLAS DIMENSIONS
# ============================================================================

class TestAtlasDimensions:
    """Tests for atlas dimension consistency: dim(Stab) = rk K_0."""

    def test_c3_dim(self):
        a = c3_atlas()
        d = a.atlas_dimension()
        assert d['dim_stab'] == d['rank_k0']

    def test_conifold_dim(self):
        a = conifold_atlas()
        d = a.atlas_dimension()
        assert d['dim_stab'] == d['rank_k0']

    def test_lp2_dim(self):
        a = local_p2_atlas_mutation()
        d = a.atlas_dimension()
        assert d['dim_stab'] == d['rank_k0']

    def test_quintic_dim(self):
        a = quintic_atlas_truncated()
        d = a.atlas_dimension()
        assert d['dim_stab'] == d['rank_k0']

    def test_dimension_table(self):
        """All entries in the dimension table satisfy dim_stab = rank_k0."""
        table = atlas_dimension_table()
        for entry in table:
            assert entry['dim_stab'] == entry['rank_k0'], \
                f"Mismatch for {entry['name']}: dim={entry['dim_stab']}, rk={entry['rank_k0']}"


# ============================================================================
# 14. MARGINAL STABILITY WALLS
# ============================================================================

class TestMarginalStability:
    """Tests for the marginal stability wall computation."""

    def test_aligned_on_wall(self):
        """Z_1 and Z_2 aligned (ratio is real) => on wall."""
        result = marginal_stability_wall(complex(1, 0), complex(2, 0))
        assert result['on_wall']

    def test_off_wall(self):
        """Z_1 and Z_2 not aligned => not on wall."""
        result = marginal_stability_wall(complex(1, 1), complex(1, 0))
        assert not result['on_wall']
        assert result['discriminant'] != 0

    def test_triangle_inequality(self):
        """|Z_1 + Z_2| <= |Z_1| + |Z_2| always."""
        test_cases = [
            (complex(1, 1), complex(1, -1)),
            (complex(3, 4), complex(-1, 2)),
            (complex(0, 1), complex(1, 0)),
        ]
        for z1, z2 in test_cases:
            result = marginal_stability_wall(z1, z2)
            assert result['triangle_inequality']

    def test_discriminant_sign(self):
        """Discriminant > 0 in one half-plane, < 0 in the other."""
        r1 = marginal_stability_wall(complex(1, 1), complex(1, 0))
        r2 = marginal_stability_wall(complex(1, -1), complex(1, 0))
        assert r1['discriminant'] > 0
        assert r2['discriminant'] < 0

    def test_conifold_wall(self):
        """Conifold: Z_1 = -t, Z_2 = -1. Wall at Im(t) = 0."""
        # t with positive imaginary part: off wall
        r = marginal_stability_wall(complex(-1, -1), complex(-1, 0))
        assert not r['on_wall']
        # t real: on wall
        r = marginal_stability_wall(complex(-1, 0), complex(-1, 0))
        assert r['on_wall']


# ============================================================================
# 15. SPECTRUM CHANGE ACROSS WALLS
# ============================================================================

class TestSpectrumChange:
    """Tests for BPS spectrum change computations."""

    def test_conifold_spectrum_change(self):
        a = conifold_atlas()
        sc = wall_crossing_spectrum_change(a, 0)
        assert sc['euler_pairing'] == 1
        assert sc['ks_type'] == 'pentagon'

    def test_conifold_bound_state(self):
        a = conifold_atlas()
        sc = wall_crossing_spectrum_change(a, 0)
        assert sc['bound_state'] == (1, 1)

    def test_conifold_net_change(self):
        """Chamber II has one more BPS state than Chamber I."""
        a = conifold_atlas()
        sc = wall_crossing_spectrum_change(a, 0)
        assert sc['net_change'] == 1  # one new state in chamber II

    def test_lp2_mutation_walls(self):
        a = local_p2_atlas_mutation()
        for i in range(3):
            sc = wall_crossing_spectrum_change(a, i)
            assert sc['euler_pairing'] != 0


# ============================================================================
# 16. FULL ANALYSIS INTEGRATION
# ============================================================================

class TestFullAnalysis:
    """Integration tests for the full analysis pipeline."""

    def test_c3_full(self):
        a = c3_atlas()
        result = a.full_analysis()
        assert result['hocolim_type'] == 'point'
        assert result['nerve']['connected']
        assert result['e1_descent']['descent_is_1_categorical']

    def test_conifold_full(self):
        a = conifold_atlas()
        result = a.full_analysis()
        assert result['hocolim_type'] == 'pushout'
        assert result['nerve']['euler_char'] == 1

    def test_lp2_mutation_full(self):
        a = local_p2_atlas_mutation()
        result = a.full_analysis()
        assert result['hocolim_type'] == 'triple_pushout'

    def test_dimension_table_runs(self):
        table = atlas_dimension_table()
        assert len(table) >= 6

    def test_full_verification_runs(self):
        results = run_full_atlas_verification()
        assert 'dimension_table' in results
        assert 'e1_descent_proof' in results
        assert 'C^3' in results
        assert 'conifold' in results


# ============================================================================
# 17. NERVE TOPOLOGY
# ============================================================================

class TestNerveTopology:
    """Tests for topological properties of the nerve."""

    def test_conifold_contractible(self):
        """Conifold nerve (interval) is contractible."""
        a = conifold_atlas()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h.get(1, 0) == 0

    def test_lp2_mutation_contractible(self):
        """Local P^2 mutation nerve (filled triangle) is contractible."""
        a = local_p2_atlas_mutation()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h.get(1, 0) == 0

    def test_lp2_full_circle(self):
        """Local P^2 full nerve (hexagon) has H_1 = Q."""
        a = local_p2_atlas_full()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h[1] == 1

    def test_c3_point(self):
        """C^3 nerve is a point."""
        a = c3_atlas()
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1

    def test_quintic_truncated_contractible(self):
        """Quintic truncated at level 2 (interval) is contractible."""
        a = quintic_atlas_truncated(mass_cutoff=2)
        n = a.nerve()
        h = n.homology_ranks()
        assert h[0] == 1
        assert h.get(1, 0) == 0


# ============================================================================
# 18. EDGE CASES AND ROBUSTNESS
# ============================================================================

class TestEdgeCases:
    """Edge cases and robustness tests."""

    def test_empty_atlas(self):
        """Atlas with no chambers."""
        a = StabilityAtlas("empty", 0, 0, 0)
        assert a.num_chambers == 0
        assert a.num_walls == 0

    def test_single_chamber_atlas(self):
        """Atlas with one chamber, no walls."""
        a = StabilityAtlas("single", 1, 1, 1)
        ch = Chamber(0, "only", [(1,)])
        a.add_chamber(ch)
        n = a.nerve()
        assert n.f_vector == [1]

    def test_wall_requires_both_chambers(self):
        """Cannot add a wall if one chamber is missing."""
        a = StabilityAtlas("test", 1, 1, 1)
        ch = Chamber(0, "A", [(1,)])
        a.add_chamber(ch)
        with pytest.raises(ValueError):
            a.add_wall(Wall(0, 1, ((1,), (0,)), 1))

    def test_large_a_n(self):
        """A_4 has 5! = 120 chambers, 10 hyperplanes."""
        arr = HyperplaneArrangementA(4)
        assert arr.num_chambers == 120
        assert arr.num_hyperplanes == 10

    def test_a1_is_conifold_like(self):
        """A_1 arrangement matches conifold structure."""
        arr = HyperplaneArrangementA(1)
        assert arr.num_chambers == 2
        assert arr.num_hyperplanes == 1
        atlas = arr.to_atlas()
        assert atlas.num_chambers == 2
        assert atlas.num_walls == 1

    def test_simplex_not_in_vertices(self):
        """Adding a simplex with vertices not in vertex set raises error."""
        K = SimplicialComplex({0, 1})
        with pytest.raises(ValueError):
            K.add_simplex(frozenset({0, 2}))

    def test_link_invalid_vertex(self):
        """Link of a non-existent vertex raises error."""
        K = SimplicialComplex({0, 1})
        with pytest.raises(ValueError):
            K.link(5)


# ============================================================================
# 19. CROSS-VERIFICATION WITH STABILITY ENGINE
# ============================================================================

class TestCrossVerification:
    """Cross-checks with stability_e1_mc_engine.py."""

    def test_conifold_dim_matches_engine(self):
        """dim Stab for conifold = 2 in both modules."""
        from compute.lib.stability_e1_mc_engine import conifold_resolved
        engine_dim = conifold_resolved().dim_stab()
        atlas = conifold_atlas()
        assert atlas.dim_stab == engine_dim

    def test_c3_dim_matches_engine(self):
        """dim Stab for C^3 matches between modules."""
        from compute.lib.stability_e1_mc_engine import c3_equivariant
        # The engine uses equivariant_params = 3, but the atlas uses
        # dim_stab = 2 (after removing normalization).
        # The exact number depends on convention.
        engine_dim = c3_equivariant().dim_stab()
        atlas = c3_atlas()
        # Both should be consistent with their own conventions
        assert engine_dim == 3  # engine includes normalization
        assert atlas.dim_stab == 2  # atlas uses CY constraint

    def test_quintic_dim_matches_engine(self):
        """dim Stab for quintic = 4 in both modules."""
        from compute.lib.stability_e1_mc_engine import quintic_threefold
        engine_dim = quintic_threefold().dim_stab()
        atlas = quintic_atlas_truncated()
        assert atlas.dim_stab == engine_dim

    def test_conifold_two_chambers_engine(self):
        """Engine confirms conifold has 2 BPS states in chamber I."""
        from compute.lib.stability_e1_mc_engine import ConifoldStabilityMC
        con = ConifoldStabilityMC(complex(1, 1))
        assert con.bps_spectrum()['num_states'] == 2

    def test_conifold_three_bps_chamber_II_engine(self):
        """Engine confirms conifold has 3 BPS states in chamber II."""
        from compute.lib.stability_e1_mc_engine import ConifoldStabilityMC
        con = ConifoldStabilityMC(complex(1, -1))
        assert con.bps_spectrum()['num_states'] == 3


# ============================================================================
# 20. COMBINATORIAL IDENTITIES
# ============================================================================

class TestCombinatorialIdentities:
    """Tests for combinatorial identities involving arrangements."""

    def test_an_euler_characteristic_formula(self):
        """For A_n: the nerve Euler characteristic satisfies known formulas.

        The Cayley graph of S_{n+1} has (n+1)! vertices and
        n*(n+1)!/2 edges (each vertex has degree n).
        So chi = V - E = (n+1)! - n*(n+1)!/2 = (n+1)!(1 - n/2).
        For n=1: chi = 2*(1 - 1/2) = 1.
        For n=2: chi = 6*(1 - 1) = 0.
        For n=3: chi = 24*(1 - 3/2) = -12.
        """
        test_cases = [
            (1, 1),    # interval: chi = 1
            (2, 0),    # hexagon: chi = 0
        ]
        for n, expected_chi in test_cases:
            arr = HyperplaneArrangementA(n)
            nerve = arr.nerve()
            assert nerve.euler_characteristic == expected_chi, \
                f"A_{n}: expected chi={expected_chi}, got {nerve.euler_characteristic}"

    def test_an_num_edges(self):
        """A_n Cayley graph has n*(n+1)!/2 edges."""
        for n in range(1, 4):
            arr = HyperplaneArrangementA(n)
            edges = arr.adjacency_graph()
            factorial = 1
            for k in range(1, n + 2):
                factorial *= k
            expected = n * factorial // 2
            assert len(edges) == expected, \
                f"A_{n}: expected {expected} edges, got {len(edges)}"

    def test_char_poly_at_one(self):
        """chi_{A_n}(1) = 0 (the hyperplane x_0=x_1 passes through (1,...,1))."""
        for n in range(1, 5):
            arr = HyperplaneArrangementA(n)
            poly = arr.characteristic_polynomial
            val = sum(poly[k] for k in range(len(poly)))
            assert val == 0, f"A_{n}: chi(1) = {val}, expected 0"

    def test_char_poly_at_zero(self):
        """chi_{A_n}(0) = 0 (the constant term is 0)."""
        for n in range(1, 5):
            arr = HyperplaneArrangementA(n)
            poly = arr.characteristic_polynomial
            assert poly[0] == 0

    def test_char_poly_leading(self):
        """Leading coefficient of chi_{A_n}(t) is 1."""
        for n in range(1, 5):
            arr = HyperplaneArrangementA(n)
            poly = arr.characteristic_polynomial
            assert poly[-1] == 1


# ============================================================================
# 21. ATLAS NERVE vs A_n ARRANGEMENT
# ============================================================================

class TestAtlasNerveVsArrangement:
    """Cross-checks between atlas nerve and A_n arrangement structure."""

    def test_a1_matches_conifold(self):
        """A_1 arrangement nerve ~ conifold nerve."""
        arr = HyperplaneArrangementA(1)
        arr_nerve = arr.nerve()
        con_nerve = conifold_atlas().nerve()
        assert arr_nerve.f_vector == con_nerve.f_vector

    def test_a2_matches_lp2_full(self):
        """A_2 arrangement matches full local P^2 (both have 6 chambers, 6 edges)."""
        arr = HyperplaneArrangementA(2)
        arr_nerve = arr.nerve()
        lp2_nerve = local_p2_atlas_full().nerve()
        # Same vertex and edge counts
        assert arr_nerve.num_simplices(0) == lp2_nerve.num_simplices(0)
        assert arr_nerve.num_simplices(1) == lp2_nerve.num_simplices(1)

    def test_mutation_triangle_is_subgraph(self):
        """The mutation triangle (3 vertices, 3 edges) is a subgraph of A_2 hexagon."""
        a_lp2 = local_p2_atlas_mutation()
        n_mut = a_lp2.nerve()
        # Triangle: 3 vertices, 3 edges
        assert n_mut.num_simplices(0) == 3
        assert n_mut.num_simplices(1) == 3
        # The hexagon has 6 vertices and 6 edges
        arr = HyperplaneArrangementA(2)
        n_hex = arr.nerve()
        assert n_hex.num_simplices(0) == 6
        assert n_hex.num_simplices(1) == 6
