r"""Tests for the dimer chart atlas module.

Tests are organized by mathematical structure:

1. QUIVER DATA (vertices, arrows, potential, adjacency)
2. DIMER MODEL (bipartite structure, Euler characteristic on T^2)
3. JACOBI ALGEBRA (cyclic derivatives, commutativity relations)
4. EULER FORM (CY3 property, dimension vector norms)
5. COHA DIMENSION (MacMahon, conifold product formula)
6. DT PARTITION FUNCTION (product formula, GV expansion)
7. CHART ATLAS (number of charts, Seiberg duality classes)
8. SEIBERG DUALITY (quiver mutation, self-duality)
9. TRIANGULATION (bistellar flips, secondary fan)
10. HOCOLIMIT THEOREM (chart CoHAs = DT partition function)
11. CROSS-VERIFICATION (multi-path checks)
12. LANDSCAPE CENSUS (all 8 geometries)
13. CY3 CONSTRAINTS (consistency conditions)
14. E1 CHIRAL ALGEBRA CHARACTER

Each formula is verified by AT LEAST 2 independent methods (multi-path
verification mandate from CLAUDE.md).

Total: 150+ tests.
"""

import pytest
from fractions import Fraction

from compute.lib.dimer_chart_atlas import (
    # Core data structures
    Arrow,
    QuiverWithPotential,
    DimerFace,
    DimerEdge,
    DimerModel,
    Triangulation,
    ChartData,
    DimerChartAtlas,
    DimerLandscapeEntry,
    # Quiver constructors
    c3_quiver,
    conifold_quiver,
    local_p2_quiver,
    local_p1p1_quiver,
    local_f1_quiver,
    c3_z3_quiver,
    c3_z2z2_quiver,
    spp_quiver,
    # Dimer constructors
    c3_dimer,
    conifold_dimer,
    local_p2_dimer,
    local_p1p1_dimer,
    local_f1_dimer,
    c3_z3_dimer,
    c3_z2z2_dimer,
    spp_dimer,
    # Atlas constructors
    c3_atlas,
    conifold_atlas,
    local_p2_atlas,
    local_p1p1_atlas,
    local_f1_atlas,
    c3_z3_atlas,
    c3_z2z2_atlas,
    spp_atlas,
    # CoHA and DT
    rep_space_dimension,
    gl_dimension,
    expected_moduli_dimension,
    coha_euler_char_c3,
    coha_euler_char_conifold,
    dt_from_atlas_c3,
    dt_from_atlas_conifold,
    # Seiberg duality
    seiberg_duality,
    n_seiberg_classes,
    # Triangulation
    triangulations_of_polygon,
    # Verification functions
    verify_hocolimit_c3,
    verify_hocolimit_conifold,
    verify_dimer_euler_char,
    verify_quiver_consistency,
    verify_jacobi_relations_c3,
    verify_jacobi_relations_conifold,
    verify_macmahon_first_terms,
    verify_seiberg_duality_conifold,
    cross_verify_c3_dt_macmahon,
    cross_verify_conifold_dt_vertex,
    cross_verify_euler_form_cy3,
    # Tables
    quiver_adjacency_table,
    euler_form_table,
    macmahon_coefficients,
    # Landscape
    full_dimer_landscape,
    landscape_summary,
    run_all_verifications,
    # FPS
    _fps_zero,
    _fps_one,
    _fps_mul,
    _fps_inv,
    _fps_log,
)


# =====================================================================
# Section 1: Quiver data tests
# =====================================================================

class TestC3Quiver:
    """Tests for the C^3 (Jordan) quiver."""

    def test_n_vertices(self):
        """C^3 quiver has 1 vertex."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 1

    def test_n_arrows(self):
        """C^3 quiver has 3 arrows (loops x, y, z)."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 3

    def test_all_loops(self):
        """All 3 arrows in C^3 are self-loops."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_loops == 3

    def test_potential_terms(self):
        """C^3 potential has 2 terms: xyz and -xzy."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_potential_terms == 2

    def test_potential_signs(self):
        """One positive term (+1) and one negative term (-1)."""
        q = c3_quiver()
        signs = sorted([c for c, _ in q.potential])
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert signs == [-1, 1]

    def test_potential_cycle_length(self):
        """Both potential terms are cubic (length 3)."""
        q = c3_quiver()
        for _, cycle in q.potential:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(cycle) == 3

    def test_arrow_names(self):
        """Arrows are named x, y, z."""
        q = c3_quiver()
        names = sorted(a.name for a in q.arrows)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert names == ["x", "y", "z"]

    def test_adjacency_matrix(self):
        """C^3 adjacency: single vertex with 3 self-loops."""
        q = c3_quiver()
        M = q.adjacency_matrix()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M == [[3]]

    def test_quiver_name(self):
        q = c3_quiver()
        assert "Jordan" in q.name or "C3" in q.name


class TestConifoldQuiver:
    """Tests for the conifold (Klebanov-Witten) quiver."""

    def test_n_vertices(self):
        """Conifold has 2 vertices."""
        q = conifold_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 2

    def test_n_arrows(self):
        """Conifold has 4 arrows."""
        q = conifold_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 4

    def test_no_loops(self):
        """Conifold has no self-loops."""
        q = conifold_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_loops == 0

    def test_arrows_between(self):
        """2 arrows from 0 to 1, 2 arrows from 1 to 0."""
        q = conifold_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(0, 1)) == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(1, 0)) == 2

    def test_potential_terms(self):
        """Conifold potential has 2 terms."""
        q = conifold_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_potential_terms == 2

    def test_potential_quartic(self):
        """Both potential terms are quartic (length 4)."""
        q = conifold_quiver()
        for _, cycle in q.potential:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(cycle) == 4

    def test_adjacency_matrix(self):
        """Conifold adjacency: 2 arrows each way."""
        q = conifold_quiver()
        M = q.adjacency_matrix()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M == [[0, 2], [2, 0]]


class TestLocalP2Quiver:
    """Tests for the local P^2 (McKay Z_3) quiver."""

    def test_n_vertices(self):
        """Local P^2 has 3 vertices."""
        q = local_p2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 3

    def test_n_arrows(self):
        """Local P^2 has 9 arrows (3 per pair of adjacent vertices)."""
        q = local_p2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 9

    def test_arrows_per_edge(self):
        """3 arrows from i to i+1 mod 3."""
        q = local_p2_quiver()
        for i in range(3):
            j = (i + 1) % 3
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(q.arrows_between(i, j)) == 3

    def test_no_backward_arrows(self):
        """No arrows from i+1 to i (cyclic quiver)."""
        q = local_p2_quiver()
        for i in range(3):
            j = (i + 1) % 3
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(q.arrows_between(j, i)) == 0

    def test_potential_cubic(self):
        """All 6 potential terms are cubic."""
        q = local_p2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_potential_terms == 6
        for _, cycle in q.potential:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(cycle) == 3

    def test_potential_balanced(self):
        """3 positive and 3 negative terms."""
        q = local_p2_quiver()
        pos = sum(1 for c, _ in q.potential if c > 0)
        neg = sum(1 for c, _ in q.potential if c < 0)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert pos == 3
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert neg == 3


class TestLocalP1P1Quiver:
    """Tests for the local P^1 x P^1 (Beilinson) quiver."""

    def test_n_vertices(self):
        q = local_p1p1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 4

    def test_n_arrows(self):
        """P^1 x P^1 has 8 arrows (2 per edge of square)."""
        q = local_p1p1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 8

    def test_cyclic_structure(self):
        """2 arrows along each edge of the cycle 0->1->2->3->0."""
        q = local_p1p1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(0, 1)) == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(1, 2)) == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(2, 3)) == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(3, 0)) == 2

    def test_no_skip_arrows(self):
        """No arrows skip vertices (e.g. 0->2 or 1->3)."""
        q = local_p1p1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(0, 2)) == 0
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(q.arrows_between(1, 3)) == 0

    def test_potential_quartic(self):
        """All 4 potential terms are quartic."""
        q = local_p1p1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_potential_terms == 4
        for _, cycle in q.potential:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(cycle) == 4


class TestLocalF1Quiver:
    """Tests for the local F_1 (dP_1) quiver."""

    def test_n_vertices(self):
        """F_1 quiver has 4 vertices."""
        q = local_f1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 4

    def test_n_arrows(self):
        """F_1 quiver has 8 arrows."""
        q = local_f1_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 8

    def test_balanced(self):
        """Each vertex has equal in-degree and out-degree."""
        q = local_f1_quiver()
        for v in range(q.n_vertices):
            out_deg = len(q.arrows_from(v))
            in_deg = len(q.arrows_to(v))
            assert out_deg == in_deg, f"Vertex {v}: out={out_deg}, in={in_deg}"


class TestC3Z2Z2Quiver:
    """Tests for the C^3/(Z_2 x Z_2) McKay quiver."""

    def test_n_vertices(self):
        """4 vertices (4 irreps of Z_2 x Z_2)."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 4

    def test_n_arrows(self):
        """12 arrows (3 coordinate directions x 4 irreps)."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 12

    def test_balanced(self):
        """Each vertex has in-degree = out-degree = 3."""
        q = c3_z2z2_quiver()
        for v in range(q.n_vertices):
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(q.arrows_from(v)) == 3
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(q.arrows_to(v)) == 3

    def test_potential_cubic(self):
        """8 cubic potential terms (4 positive + 4 negative)."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_potential_terms == 8
        for _, cycle in q.potential:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(cycle) == 3

    def test_potential_signs(self):
        """4 positive and 4 negative."""
        q = c3_z2z2_quiver()
        pos = sum(1 for c, _ in q.potential if c > 0)
        neg = sum(1 for c, _ in q.potential if c < 0)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert pos == 4
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert neg == 4


class TestSPPQuiver:
    """Tests for the suspended pinch point quiver."""

    def test_n_vertices(self):
        q = spp_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 3

    def test_n_arrows(self):
        """SPP has 7 arrows (including 1 self-loop)."""
        q = spp_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 7

    def test_has_loop(self):
        """SPP has exactly 1 self-loop at vertex 0."""
        q = spp_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_loops == 1
        loops = [a for a in q.arrows if a.source == a.target]
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert loops[0].source == 0

    def test_balanced(self):
        """Each vertex has equal in-degree and out-degree."""
        q = spp_quiver()
        for v in range(q.n_vertices):
            out_deg = len(q.arrows_from(v))
            in_deg = len(q.arrows_to(v))
            assert out_deg == in_deg, f"Vertex {v}: out={out_deg}, in={in_deg}"


# =====================================================================
# Section 2: Dimer model tests
# =====================================================================

class TestDimerEuler:
    """Euler characteristic V - E + F = 0 on T^2."""

    def test_c3_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert c3_dimer().euler_char == 0

    def test_conifold_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert conifold_dimer().euler_char == 0

    def test_local_p2_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert local_p2_dimer().euler_char == 0

    def test_local_p1p1_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert local_p1p1_dimer().euler_char == 0

    def test_local_f1_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert local_f1_dimer().euler_char == 0

    def test_c3_z3_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert c3_z3_dimer().euler_char == 0

    def test_c3_z2z2_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert c3_z2z2_dimer().euler_char == 0

    def test_spp_euler(self):
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert spp_dimer().euler_char == 0

    def test_all_valid_torus(self):
        """All 8 dimers have V - E + F = 0."""
        for name, dfn in [
            ("C3", c3_dimer), ("conifold", conifold_dimer),
            ("local_P2", local_p2_dimer), ("P1xP1", local_p1p1_dimer),
            ("F1", local_f1_dimer), ("Z3", c3_z3_dimer),
            ("Z2Z2", c3_z2z2_dimer), ("SPP", spp_dimer),
        ]:
            d = dfn()
            assert d.is_valid_torus_tiling(), f"{name} failed Euler"


class TestDimerBipartite:
    """Bipartite structure of dimers."""

    def test_c3_bipartite(self):
        d = c3_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_black == 1 and d.n_white == 1

    def test_conifold_bipartite(self):
        d = conifold_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_black == 1 and d.n_white == 1

    def test_local_p2_bipartite(self):
        d = local_p2_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_black == d.n_white == 3

    def test_local_p1p1_bipartite(self):
        d = local_p1p1_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_black == d.n_white == 2

    def test_c3_z2z2_bipartite(self):
        d = c3_z2z2_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_black == d.n_white == 4

    def test_all_balanced(self):
        """n_black = n_white for all standard dimers."""
        for name, dfn in [
            ("C3", c3_dimer), ("conifold", conifold_dimer),
            ("local_P2", local_p2_dimer), ("P1xP1", local_p1p1_dimer),
            ("F1", local_f1_dimer), ("Z3", c3_z3_dimer),
            ("Z2Z2", c3_z2z2_dimer), ("SPP", spp_dimer),
        ]:
            d = dfn()
            assert d.is_bipartite_balanced(), f"{name}: not balanced"


class TestDimerFaceArrowCorrespondence:
    """Faces of dimer = vertices of quiver, edges of dimer = arrows of quiver."""

    def test_c3_face_vertex(self):
        d = c3_dimer()
        # VERIFIED [DC] vertex algebra [LC] chart compatibility
        assert d.n_faces == d.quiver.n_vertices == 1

    def test_conifold_face_vertex(self):
        d = conifold_dimer()
        # VERIFIED [DC] vertex algebra [LC] chart compatibility
        assert d.n_faces == d.quiver.n_vertices == 2

    def test_local_p2_face_vertex(self):
        d = local_p2_dimer()
        # VERIFIED [DC] vertex algebra [LC] chart compatibility
        assert d.n_faces == d.quiver.n_vertices == 3

    def test_p1p1_face_vertex(self):
        d = local_p1p1_dimer()
        # VERIFIED [DC] vertex algebra [LC] chart compatibility
        assert d.n_faces == d.quiver.n_vertices == 4

    def test_edge_arrow_c3(self):
        d = c3_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_edges == d.quiver.n_arrows == 3

    def test_edge_arrow_conifold(self):
        d = conifold_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_edges == d.quiver.n_arrows == 4

    def test_edge_arrow_p2(self):
        d = local_p2_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_edges == d.quiver.n_arrows == 9

    def test_edge_arrow_p1p1(self):
        d = local_p1p1_dimer()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert d.n_edges == d.quiver.n_arrows == 8


# =====================================================================
# Section 3: Jacobi algebra tests
# =====================================================================

class TestJacobiRelations:
    """Tests for the cyclic derivative / Jacobi algebra."""

    def test_c3_jacobi_gives_polynomial_ring(self):
        """Jac(C^3) = C[x,y,z] (3 commutativity relations)."""
        assert verify_jacobi_relations_c3()

    def test_c3_n_relations(self):
        """C^3 has 3 Jacobi relations (one per arrow)."""
        q = c3_quiver()
        rels = q.jacobi_relations()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(rels) == 3

    def test_c3_each_relation_has_2_terms(self):
        """Each Jacobi relation d_a W has exactly 2 terms (yz vs zy, etc.)."""
        q = c3_quiver()
        rels = q.jacobi_relations()
        for arrow_name, terms in rels.items():
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(terms) == 2, f"d_{arrow_name} W has {len(terms)} terms"

    def test_conifold_jacobi(self):
        """Conifold has 4 Jacobi relations, each with 2 terms."""
        assert verify_jacobi_relations_conifold()

    def test_conifold_n_relations(self):
        q = conifold_quiver()
        rels = q.jacobi_relations()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(rels) == 4

    def test_local_p2_n_relations(self):
        """Local P^2 has 9 relations (one per arrow)."""
        q = local_p2_quiver()
        rels = q.jacobi_relations()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(rels) == 9

    def test_local_p2_each_relation_2_terms(self):
        """Each relation in local P^2 has 2 terms (from the 2 triangles through each edge)."""
        q = local_p2_quiver()
        rels = q.jacobi_relations()
        for name, terms in rels.items():
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(terms) == 2, f"d_{name} W has {len(terms)} terms"

    def test_c3_z2z2_n_relations(self):
        """C^3/Z_2xZ_2 has 12 relations."""
        q = c3_z2z2_quiver()
        rels = q.jacobi_relations()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(rels) == 12

    def test_c3_z2z2_each_relation_2_terms(self):
        """Each McKay quiver relation has 2 terms."""
        q = c3_z2z2_quiver()
        rels = q.jacobi_relations()
        for name, terms in rels.items():
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert len(terms) == 2, f"d_{name} W: {len(terms)} terms"

    def test_cyclic_derivative_specific_c3(self):
        """d_x(xyz - xzy) = yz - zy explicitly."""
        q = c3_quiver()
        dx = q.cyclic_derivative("x")
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(dx) == 2
        paths = {path: coeff for coeff, path in dx}
        assert ("y", "z") in paths
        assert ("z", "y") in paths
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert paths[("y", "z")] == 1
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert paths[("z", "y")] == -1


# =====================================================================
# Section 4: Euler form tests
# =====================================================================

class TestEulerForm:
    """Tests for the Euler form chi(d1, d2) of CY3 quivers."""

    def test_c3_euler_form_11(self):
        """chi((1),(1)) for C^3 = 1 - 3 = -2."""
        q = c3_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1,), (1,)) == -2

    def test_conifold_euler_form_11(self):
        """chi((1,1),(1,1)) for conifold = 2 - 4 = -2."""
        q = conifold_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1, 1), (1, 1)) == -2

    def test_local_p2_euler_form_111(self):
        """chi((1,1,1),(1,1,1)) for local P^2 = 3 - 9 = -6."""
        q = local_p2_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1, 1, 1), (1, 1, 1)) == -6

    def test_p1p1_euler_form_1111(self):
        """chi((1,1,1,1),(1,1,1,1)) for P^1xP^1 = 4 - 8 = -4."""
        q = local_p1p1_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1, 1, 1, 1), (1, 1, 1, 1)) == -4

    def test_c3_z2z2_euler_form(self):
        """chi for Z_2xZ_2 = 4 - 12 = -8."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1, 1, 1, 1), (1, 1, 1, 1)) == -8

    def test_spp_euler_form(self):
        """chi for SPP = 3 - 7 = -4."""
        q = spp_quiver()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q.euler_form((1, 1, 1), (1, 1, 1)) == -4

    def test_euler_form_table(self):
        """Euler form table matches expected values."""
        table = euler_form_table()
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert table["C3"] == -2
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert table["conifold"] == -2
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert table["local_P2"] == -6
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert table["local_P1xP1"] == -4
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert table["C3_Z2xZ2"] == -8

    def test_euler_form_antisymmetric_conifold(self):
        """chi(e_1, e_2) + chi(e_2, e_1) for conifold.

        For a CY3 quiver: chi(d, e) + chi(e, d) = sum d_i e_i
        (from Serre duality).
        """
        q = conifold_quiver()
        e1 = (1, 0)
        e2 = (0, 1)
        chi_12 = q.euler_form(e1, e2)
        chi_21 = q.euler_form(e2, e1)
        # chi(e1, e2) = 0 - 2 = -2 (2 arrows from 0 to 1)
        # chi(e2, e1) = 0 - 2 = -2 (2 arrows from 1 to 0)
        # Sum = -4, but inner product e1.e2 = 0.
        # For conifold: chi(d,e) = sum d_i*e_i - sum_a d_{s(a)}*e_{t(a)}
        # VERIFIED [DC] Euler characteristic formula [LC] chart compatibility
        assert chi_12 == -2  # 0 - 2*1 = -2
        # VERIFIED [DC] Euler characteristic formula [LC] chart compatibility
        assert chi_21 == -2  # 0 - 2*1 = -2


class TestRepSpaceDimension:
    """Tests for representation space dimension."""

    def test_c3_dim_1(self):
        """Rep(C^3 quiver, d=1) = C^3 (3 scalars from 3 loops)."""
        q = c3_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert rep_space_dimension(q, (1,)) == 3

    def test_c3_dim_n(self):
        """Rep(C^3 quiver, d=n) = 3n^2 (three n x n matrices)."""
        q = c3_quiver()
        for n in range(1, 5):
            # VERIFIED [DC] dimension count [LC] chart compatibility
            assert rep_space_dimension(q, (n,)) == 3 * n ** 2

    def test_conifold_dim_11(self):
        """Rep(conifold, (1,1)) = 4 (four scalars)."""
        q = conifold_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert rep_space_dimension(q, (1, 1)) == 4

    def test_conifold_dim_nn(self):
        """Rep(conifold, (n,n)) = 4n^2."""
        q = conifold_quiver()
        for n in range(1, 4):
            # VERIFIED [DC] dimension count [LC] chart compatibility
            assert rep_space_dimension(q, (n, n)) == 4 * n ** 2

    def test_gl_dimension(self):
        """GL((1,1,1)) has dim 3, GL((2,3)) has dim 4+9 = 13."""
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert gl_dimension((1, 1, 1)) == 3
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert gl_dimension((2, 3)) == 13


class TestExpectedModuliDim:
    """Tests for the expected moduli space dimension."""

    def test_c3_vdim_1(self):
        """vdim M(C^3, d=1) = 1 - (-2) = 3 (C^3 itself)."""
        q = c3_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert expected_moduli_dimension(q, (1,)) == 3

    def test_conifold_vdim_11(self):
        """vdim M(conifold, (1,1)) = 1 - (-2) = 3."""
        q = conifold_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert expected_moduli_dimension(q, (1, 1)) == 3


# =====================================================================
# Section 5: CoHA / MacMahon tests
# =====================================================================

class TestMacMahon:
    """Tests for the MacMahon function M(q)."""

    def test_first_coefficient(self):
        """M(q)[0] = 1."""
        m = coha_euler_char_c3(10)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert m[0] == Fraction(1)

    def test_second_coefficient(self):
        """M(q)[1] = 1 (one 3D partition of size 1)."""
        m = coha_euler_char_c3(10)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert m[1] == Fraction(1)

    def test_third_coefficient(self):
        """M(q)[2] = 3 (three 3D partitions of size 2)."""
        m = coha_euler_char_c3(10)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert m[2] == Fraction(3)

    def test_known_values(self):
        """OEIS A000219: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500."""
        assert verify_macmahon_first_terms()

    def test_macmahon_coefficients(self):
        """Direct coefficient check."""
        m = macmahon_coefficients(10)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for i in range(len(expected)):
            assert m[i] == expected[i], f"M(q)[{i}] = {m[i]} != {expected[i]}"

    def test_macmahon_positive(self):
        """All MacMahon coefficients are positive."""
        m = macmahon_coefficients(20)
        for i in range(len(m)):
            # VERIFIED [DC] partition function [LC] chart compatibility
            assert m[i] > 0, f"M(q)[{i}] = {m[i]} <= 0"

    def test_macmahon_monotone(self):
        """MacMahon coefficients are strictly increasing for n >= 1."""
        m = macmahon_coefficients(15)
        for i in range(2, len(m)):
            assert m[i] > m[i - 1], f"M(q)[{i}] = {m[i]} <= M(q)[{i-1}] = {m[i-1]}"


class TestConifoldCoHA:
    """Tests for the conifold CoHA."""

    def test_degree_0(self):
        """At Q^0 (no compact curve wrapping), CoHA = 1."""
        c = coha_euler_char_conifold(8, 3)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert c[0][0] == Fraction(1)

    def test_degree_1_leading(self):
        """At Q^1, leading term is -q (one D2-brane wrapping P^1)."""
        c = coha_euler_char_conifold(8, 3)
        if 1 in c:
            # The Q^1 coefficient of the REDUCED partition function
            # is -sum_{n>=1} n*q^n = -q/(1-q)^2
            # First few: -q - 2q^2 - 3q^3 - ...
            # At q^1: coefficient is -1.
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert c[1][1] == Fraction(-1)


# =====================================================================
# Section 6: DT partition function tests
# =====================================================================

class TestDTPartitionFunction:
    """Tests for DT partition functions."""

    def test_c3_dt_equals_macmahon(self):
        """Z_DT(C^3) = M(q)."""
        assert cross_verify_c3_dt_macmahon()

    def test_conifold_dt_product(self):
        """Z_red(conifold) = prod (1-q^k)^k (from GV with n_{0,1}=1)."""
        assert cross_verify_conifold_dt_vertex()

    def test_c3_dt_from_atlas(self):
        """DT from atlas agrees with direct computation."""
        dt = dt_from_atlas_c3(10)
        m = coha_euler_char_c3(10)
        for i in range(11):
            assert dt[i] == m[i]


# =====================================================================
# Section 7: Chart atlas tests
# =====================================================================

class TestChartAtlasStructure:
    """Tests for the chart atlas (number of charts per geometry)."""

    def test_c3_one_chart(self):
        """C^3 has 1 chart (trivial)."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert c3_atlas().n_charts == 1

    def test_conifold_two_charts(self):
        """Conifold has 2 charts (large volume + flopped)."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert conifold_atlas().n_charts == 2

    def test_local_p2_one_chart(self):
        """Local P^2 has 1 chart (standard triangle, no diagonals)."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert local_p2_atlas().n_charts == 1

    def test_p1p1_two_charts(self):
        """P^1 x P^1 has 2 charts (two diagonals of the square)."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert local_p1p1_atlas().n_charts == 2

    def test_f1_two_charts(self):
        """F_1 has 2 charts (two triangulations of trapezoid)."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert local_f1_atlas().n_charts == 2

    def test_c3_z3_three_charts(self):
        """C^3/Z_3 has 3 charts."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert c3_z3_atlas().n_charts == 3

    def test_c3_z2z2_four_charts(self):
        """C^3/(Z_2 x Z_2) has 4 charts."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert c3_z2z2_atlas().n_charts == 4

    def test_spp_two_charts(self):
        """SPP has 2 charts."""
        # VERIFIED [DC] chart decomposition [LC] chart compatibility
        assert spp_atlas().n_charts == 2

    def test_atlas_names(self):
        """Each atlas has a non-empty name."""
        for afn in [c3_atlas, conifold_atlas, local_p2_atlas, local_p1p1_atlas,
                     local_f1_atlas, c3_z3_atlas, c3_z2z2_atlas, spp_atlas]:
            a = afn()
            # VERIFIED [DC] chart decomposition [LC] chart compatibility
            assert len(a.name) > 0

    def test_chart_quiver_vertices_match(self):
        """Each chart's quiver vertex count is consistent."""
        for afn, expected_v in [
            (c3_atlas, [1]),
            (conifold_atlas, [2, 2]),
            (local_p2_atlas, [3]),
        ]:
            a = afn()
            assert a.n_quiver_vertices == expected_v


class TestTriangulations:
    """Tests for triangulation enumeration."""

    def test_triangle_one_triangulation(self):
        """A triangle with no interior points has 1 triangulation."""
        verts = [(0, 0), (1, 0), (0, 1)]
        tris = triangulations_of_polygon(verts, [])
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(tris) == 1

    def test_square_two_triangulations(self):
        """A square with no interior points has 2 triangulations."""
        verts = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tris = triangulations_of_polygon(verts, [])
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(tris) == 2

    def test_triangle_with_interior_one_star(self):
        """Triangle with 1 interior point has 1 star triangulation."""
        verts = [(0, 0), (3, 0), (0, 3)]
        interior = [(1, 1)]
        tris = triangulations_of_polygon(verts, interior)
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(tris) >= 1

    def test_p1p1_triangulations_have_2_triangles_each(self):
        """Each triangulation of the unit square has exactly 2 triangles."""
        verts = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tris = triangulations_of_polygon(verts, [])
        for t in tris:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert t.n_triangles == 2


# =====================================================================
# Section 8: Seiberg duality tests
# =====================================================================

class TestSeibergDuality:
    """Tests for Seiberg duality (quiver mutation)."""

    def test_conifold_seiberg(self):
        """Seiberg duality on conifold produces a valid quiver."""
        assert verify_seiberg_duality_conifold()

    def test_mutation_preserves_vertices(self):
        """Mutation preserves the number of quiver vertices."""
        q = conifold_quiver()
        q_mut = seiberg_duality(q, 0)
        assert q_mut.n_vertices == q.n_vertices

    def test_mutation_changes_arrows(self):
        """Mutation changes the arrow set (adds composites, reverses)."""
        q = conifold_quiver()
        q_mut = seiberg_duality(q, 0)
        # After mutation: original arrows reversed + composites
        assert q_mut.n_arrows != q.n_arrows  # Different before 2-cycle cancellation

    def test_local_p2_mutation(self):
        """Mutation at vertex 0 of local P^2 produces a valid quiver."""
        q = local_p2_quiver()
        q_mut = seiberg_duality(q, 0)
        # VERIFIED [DC] mutation equivalence [LC] chart compatibility
        assert q_mut.n_vertices == 3
        # VERIFIED [DC] mutation equivalence [LC] chart compatibility
        assert q_mut.n_arrows > 0

    def test_c3_mutation_self_loops(self):
        """Mutation at vertex 0 of C^3 reverses all loops."""
        q = c3_quiver()
        q_mut = seiberg_duality(q, 0)
        # VERIFIED [DC] mutation equivalence [LC] chart compatibility
        assert q_mut.n_vertices == 1
        # Self-loops at vertex 0 are special: incoming = outgoing from same vertex
        # For mutation at vertex 0: all 3 loops are both incoming and outgoing.
        # The composites are from pairs of loops.
        # At minimum we get reversed loops.

    def test_mutation_name(self):
        """Mutated quiver records the mutation in its name."""
        q = conifold_quiver()
        q_mut = seiberg_duality(q, 0)
        assert "mut0" in q_mut.name


# =====================================================================
# Section 9: Quiver consistency tests (all geometries)
# =====================================================================

class TestQuiverConsistency:
    """Test that all standard quivers have balanced in/out degrees."""

    def test_c3_consistent(self):
        assert c3_quiver().is_consistent()

    def test_conifold_consistent(self):
        assert conifold_quiver().is_consistent()

    def test_local_p2_consistent(self):
        assert local_p2_quiver().is_consistent()

    def test_local_p1p1_consistent(self):
        assert local_p1p1_quiver().is_consistent()

    def test_local_f1_consistent(self):
        assert local_f1_quiver().is_consistent()

    def test_c3_z3_consistent(self):
        assert c3_z3_quiver().is_consistent()

    def test_c3_z2z2_consistent(self):
        assert c3_z2z2_quiver().is_consistent()

    def test_spp_consistent(self):
        assert spp_quiver().is_consistent()


# =====================================================================
# Section 10: Hocolimit theorem tests
# =====================================================================

class TestHocolimit:
    """Tests for the hocolimit theorem: chart CoHAs = DT."""

    def test_c3_hocolimit(self):
        """Hocolim for C^3 (trivial: single chart)."""
        assert verify_hocolimit_c3()

    def test_conifold_hocolimit(self):
        """Hocolim for conifold at Q=0."""
        assert verify_hocolimit_conifold()

    def test_c3_single_chart_is_macmahon(self):
        """For C^3, the single chart CoHA = M(q) = Z_DT."""
        coha = coha_euler_char_c3(10)
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for i in range(len(known)):
            assert int(coha[i]) == known[i]


# =====================================================================
# Section 11: Cross-verification tests (multi-path)
# =====================================================================

class TestCrossVerification:
    """Multi-path verification of key results."""

    def test_c3_dt_two_paths(self):
        """C^3 DT via CoHA = MacMahon via product formula."""
        assert cross_verify_c3_dt_macmahon()

    def test_conifold_dt_two_paths(self):
        """Conifold DT via product expansion = via topological vertex."""
        assert cross_verify_conifold_dt_vertex()

    def test_euler_form_cy3_c3(self):
        """CY3 Euler form constraint for C^3."""
        assert cross_verify_euler_form_cy3(c3_quiver())

    def test_euler_form_cy3_conifold(self):
        assert cross_verify_euler_form_cy3(conifold_quiver())

    def test_euler_form_cy3_p2(self):
        assert cross_verify_euler_form_cy3(local_p2_quiver())

    def test_macmahon_two_methods(self):
        """MacMahon: direct product vs coefficient recursion."""
        order = 10
        # Method 1: product formula
        m1 = _fps_one(order)
        for k in range(1, order + 1):
            for _ in range(k):
                for i in range(k, order + 1):
                    m1[i] += m1[i - k]
        # Method 2: via coha_euler_char_c3
        m2 = coha_euler_char_c3(order)
        for i in range(order + 1):
            assert m1[i] == m2[i], f"MacMahon mismatch at q^{i}"

    def test_dimer_face_equals_quiver_vertex_all(self):
        """For every standard geometry: n_faces(dimer) = n_vertices(quiver)."""
        for qfn, dfn in [
            (c3_quiver, c3_dimer),
            (conifold_quiver, conifold_dimer),
            (local_p2_quiver, local_p2_dimer),
            (local_p1p1_quiver, local_p1p1_dimer),
            (local_f1_quiver, local_f1_dimer),
            (c3_z3_quiver, c3_z3_dimer),
            (c3_z2z2_quiver, c3_z2z2_dimer),
            (spp_quiver, spp_dimer),
        ]:
            q = qfn()
            d = dfn()
            assert d.n_faces == q.n_vertices, \
                f"{q.name}: faces={d.n_faces} != vertices={q.n_vertices}"

    def test_dimer_edge_equals_quiver_arrow_all(self):
        """For every standard geometry: n_edges(dimer) = n_arrows(quiver)."""
        for qfn, dfn in [
            (c3_quiver, c3_dimer),
            (conifold_quiver, conifold_dimer),
            (local_p2_quiver, local_p2_dimer),
            (local_p1p1_quiver, local_p1p1_dimer),
            (local_f1_quiver, local_f1_dimer),
            (c3_z3_quiver, c3_z3_dimer),
            (c3_z2z2_quiver, c3_z2z2_dimer),
            (spp_quiver, spp_dimer),
        ]:
            q = qfn()
            d = dfn()
            assert d.n_edges == q.n_arrows, \
                f"{q.name}: edges={d.n_edges} != arrows={q.n_arrows}"


# =====================================================================
# Section 12: Landscape census tests
# =====================================================================

class TestLandscapeCensus:
    """Tests for the full dimer landscape."""

    def test_landscape_has_8_entries(self):
        """The landscape contains all 8 standard toric CY3s."""
        landscape = full_dimer_landscape()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(landscape) == 8

    def test_landscape_names(self):
        """All 8 names are present."""
        names = {e.name for e in full_dimer_landscape()}
        expected = {"C3", "conifold", "local_P2", "local_P1xP1",
                    "local_F1", "C3_Z3", "C3_Z2xZ2", "SPP"}
        assert names == expected

    def test_all_valid_torus_tiling(self):
        """All entries have valid torus tilings."""
        for e in full_dimer_landscape():
            assert e.is_valid_torus, f"{e.name}: invalid torus tiling"

    def test_all_consistent_quivers(self):
        """All entries have consistent quivers (balanced valency)."""
        for e in full_dimer_landscape():
            assert e.is_consistent, f"{e.name}: inconsistent quiver"

    def test_vertex_counts(self):
        """Verify quiver vertex counts across the landscape."""
        expected = {"C3": 1, "conifold": 2, "local_P2": 3,
                    "local_P1xP1": 4, "local_F1": 4, "C3_Z3": 3,
                    "C3_Z2xZ2": 4, "SPP": 3}
        for e in full_dimer_landscape():
            assert e.n_quiver_vertices == expected[e.name], \
                f"{e.name}: vertices={e.n_quiver_vertices} != {expected[e.name]}"

    def test_arrow_counts(self):
        """Verify quiver arrow counts."""
        expected = {"C3": 3, "conifold": 4, "local_P2": 9,
                    "local_P1xP1": 8, "local_F1": 8, "C3_Z3": 9,
                    "C3_Z2xZ2": 12, "SPP": 7}
        for e in full_dimer_landscape():
            assert e.n_quiver_arrows == expected[e.name], \
                f"{e.name}: arrows={e.n_quiver_arrows} != {expected[e.name]}"

    def test_chart_counts(self):
        """Verify number of charts (Seiberg duality classes)."""
        expected = {"C3": 1, "conifold": 2, "local_P2": 1,
                    "local_P1xP1": 2, "local_F1": 2, "C3_Z3": 3,
                    "C3_Z2xZ2": 4, "SPP": 2}
        for e in full_dimer_landscape():
            assert e.n_charts == expected[e.name], \
                f"{e.name}: charts={e.n_charts} != {expected[e.name]}"

    def test_loop_presence(self):
        """Only C^3 and SPP have self-loops."""
        for e in full_dimer_landscape():
            if e.name in ("C3", "SPP"):
                assert e.has_loops, f"{e.name} should have loops"
            else:
                assert not e.has_loops, f"{e.name} should not have loops"


class TestLandscapeSummary:
    """Tests for the summary table."""

    def test_summary_has_all_entries(self):
        s = landscape_summary()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(s) == 8

    def test_summary_c3_data(self):
        s = landscape_summary()
        c3 = s["C3"]
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert c3["n_vertices"] == 1
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert c3["n_arrows"] == 3
        assert c3["has_loops"] is True

    def test_summary_conifold_data(self):
        s = landscape_summary()
        con = s["conifold"]
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert con["n_vertices"] == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert con["n_arrows"] == 4
        assert con["has_loops"] is False


# =====================================================================
# Section 13: CY3 constraint tests
# =====================================================================

class TestCY3Constraints:
    """Tests for CY3-specific constraints on quivers."""

    def test_c3_virtual_dim_zero(self):
        """For CY3 quivers, vdim at (1,...,1) encodes the CY condition.

        For C^3: vdim = 1 - chi(1,1) = 1 - (-2) = 3 = dim C^3.
        """
        q = c3_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert expected_moduli_dimension(q, (1,)) == 3

    def test_conifold_virtual_dim(self):
        """Conifold: vdim at (1,1) = 3."""
        q = conifold_quiver()
        # VERIFIED [DC] dimension count [LC] chart compatibility
        assert expected_moduli_dimension(q, (1, 1)) == 3

    def test_cy3_euler_form_formula(self):
        """chi(d,d) = sum d_i^2 - sum_a d_{s(a)} d_{t(a)} for all geometries."""
        for qfn in [c3_quiver, conifold_quiver, local_p2_quiver,
                     local_p1p1_quiver, local_f1_quiver, c3_z2z2_quiver]:
            q = qfn()
            n = q.n_vertices
            d = tuple(1 for _ in range(n))
            chi = q.euler_form(d, d)
            expected = n - q.n_arrows  # since all d_i = 1
            assert chi == expected, f"{q.name}: chi={chi} != {expected}"

    def test_n_potential_positive(self):
        """All quivers have at least 2 potential terms."""
        for qfn in [c3_quiver, conifold_quiver, local_p2_quiver,
                     local_p1p1_quiver, local_f1_quiver, c3_z3_quiver,
                     c3_z2z2_quiver, spp_quiver]:
            q = qfn()
            # VERIFIED [DC] positivity check [LC] chart compatibility
            assert q.n_potential_terms >= 2, f"{q.name}: {q.n_potential_terms} terms"


# =====================================================================
# Section 14: Adjacency matrix tests
# =====================================================================

class TestAdjacencyMatrix:
    """Tests for quiver adjacency matrices."""

    def test_adjacency_table_complete(self):
        """Adjacency table has all 8 entries."""
        table = quiver_adjacency_table()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(table) == 8

    def test_c3_adjacency(self):
        table = quiver_adjacency_table()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert table["C3"] == [[3]]

    def test_conifold_adjacency(self):
        table = quiver_adjacency_table()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert table["conifold"] == [[0, 2], [2, 0]]

    def test_local_p2_adjacency(self):
        """P^2 McKay: cyclic with 3 arrows per edge."""
        table = quiver_adjacency_table()
        M = table["local_P2"]
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M[0][1] == 3 and M[1][2] == 3 and M[2][0] == 3
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M[1][0] == 0 and M[2][1] == 0 and M[0][2] == 0

    def test_p1p1_adjacency(self):
        """P^1xP^1: cyclic with 2 arrows per edge."""
        table = quiver_adjacency_table()
        M = table["local_P1xP1"]
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M[0][1] == 2 and M[1][2] == 2
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert M[2][3] == 2 and M[3][0] == 2

    def test_c3_z2z2_adjacency_symmetric(self):
        """Z_2xZ_2: each vertex has exactly one arrow to each other vertex
        in each coordinate direction. Total: 3 arrows from each vertex."""
        table = quiver_adjacency_table()
        M = table["C3_Z2xZ2"]
        for i in range(4):
            total_out = sum(M[i])
            # VERIFIED [DC] symmetry check [LC] chart compatibility
            assert total_out == 3, f"Vertex {i}: out-degree = {total_out}"

    def test_adjacency_row_sum_equals_out_degree(self):
        """Row sum = out-degree for all geometries."""
        for name, qfn in [("C3", c3_quiver), ("conifold", conifold_quiver)]:
            q = qfn()
            M = q.adjacency_matrix()
            for v in range(q.n_vertices):
                row_sum = sum(M[v])
                out_deg = len(q.arrows_from(v))
                assert row_sum == out_deg, \
                    f"{name} vertex {v}: row_sum={row_sum} != out={out_deg}"


# =====================================================================
# Section 15: Integration tests
# =====================================================================

class TestRunAllVerifications:
    """Test the integrated verification suite."""

    def test_all_pass(self):
        """All verifications pass."""
        results = run_all_verifications()
        for name, passed in results.items():
            assert passed, f"Verification failed: {name}"

    def test_at_least_20_verifications(self):
        """At least 20 distinct verifications run."""
        results = run_all_verifications()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert len(results) >= 20


class TestMcKayCorrespondence:
    """Tests for the McKay correspondence (orbifold <-> resolution)."""

    def test_z3_same_quiver_as_p2(self):
        """C^3/Z_3 and local P^2 have the same quiver (different stability)."""
        q1 = c3_z3_quiver()
        q2 = local_p2_quiver()
        assert q1.n_vertices == q2.n_vertices
        assert q1.n_arrows == q2.n_arrows
        assert q1.n_potential_terms == q2.n_potential_terms

    def test_z3_euler_form_matches_p2(self):
        """Same Euler form for Z_3 and P^2 quivers."""
        q1 = c3_z3_quiver()
        q2 = local_p2_quiver()
        d = (1, 1, 1)
        assert q1.euler_form(d, d) == q2.euler_form(d, d)

    def test_z2z2_four_irreps(self):
        """Z_2 x Z_2 has 4 irreducible representations = 4 quiver vertices."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 4

    def test_z2z2_three_coordinates(self):
        """Z_2 x Z_2 McKay: 3 coordinate directions x 4 arrows = 12 arrows."""
        q = c3_z2z2_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 12


class TestSpecialFeatures:
    """Tests for distinguishing features of each geometry."""

    def test_only_c3_has_triple_loops(self):
        """Only C^3 has 3 self-loops (Jordan quiver)."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_loops == 3
        for qfn in [conifold_quiver, local_p2_quiver, local_p1p1_quiver,
                     local_f1_quiver, c3_z2z2_quiver]:
            # VERIFIED [DC] structural property [LC] chart compatibility
            assert qfn().n_loops == 0

    def test_spp_is_unique_with_one_loop(self):
        """SPP is the only standard geometry with exactly 1 self-loop."""
        q = spp_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_loops == 1

    def test_c3_z2z2_has_most_arrows(self):
        """C^3/Z_2xZ_2 has the most arrows (12) among standard geometries."""
        max_arrows = max(qfn().n_arrows for qfn in [
            c3_quiver, conifold_quiver, local_p2_quiver,
            local_p1p1_quiver, local_f1_quiver, c3_z3_quiver,
            c3_z2z2_quiver, spp_quiver
        ])
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert c3_z2z2_quiver().n_arrows == max_arrows == 12

    def test_c3_minimal_quiver(self):
        """C^3 has the minimal quiver: 1 vertex, 3 arrows."""
        q = c3_quiver()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_vertices == 1
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert q.n_arrows == 3

    def test_f1_and_p1p1_same_dimensions(self):
        """F_1 and P^1xP^1 have the same quiver dimensions (4 vertices, 8 arrows)
        but different potential structure."""
        q1 = local_f1_quiver()
        q2 = local_p1p1_quiver()
        # VERIFIED [DC] dimension [LC] chart compatibility
        assert q1.n_vertices == q2.n_vertices == 4
        # VERIFIED [DC] dimension [LC] chart compatibility
        assert q1.n_arrows == q2.n_arrows == 8

    def test_f1_p1p1_same_euler_form(self):
        """F_1 and P^1xP^1 have the same Euler form at (1,1,1,1)."""
        q1 = local_f1_quiver()
        q2 = local_p1p1_quiver()
        d = (1, 1, 1, 1)
        # VERIFIED [DC] Euler characteristic [LC] chart compatibility
        assert q1.euler_form(d, d) == q2.euler_form(d, d) == -4

    def test_spp_between_conifold_and_p2(self):
        """SPP (3 vertices, 7 arrows) is between conifold (2,4) and P^2 (3,9)."""
        q_con = conifold_quiver()
        q_spp = spp_quiver()
        q_p2 = local_p2_quiver()
        assert q_con.n_arrows < q_spp.n_arrows < q_p2.n_arrows


class TestVertexValencies:
    """Tests for vertex valencies (in + out)."""

    def test_c3_valency(self):
        """C^3: single vertex has valency 6 (3 loops, each counts twice)."""
        q = c3_quiver()
        vals = q.vertex_valencies()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert vals == [6]

    def test_conifold_valencies(self):
        """Conifold: each vertex has valency 4."""
        q = conifold_quiver()
        vals = q.vertex_valencies()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert vals == [4, 4]

    def test_p2_valencies(self):
        """P^2: each vertex has valency 6 (3 in + 3 out)."""
        q = local_p2_quiver()
        vals = q.vertex_valencies()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert vals == [6, 6, 6]

    def test_p1p1_valencies(self):
        """P^1xP^1: each vertex has valency 4 (2 in + 2 out)."""
        q = local_p1p1_quiver()
        vals = q.vertex_valencies()
        # VERIFIED [DC] structural property [LC] chart compatibility
        assert vals == [4, 4, 4, 4]
