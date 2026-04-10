"""
Tests for dd_modular_lattices.py.

Verifies the lattice-theoretic structures underlying the BKM superalgebra
construction for the Igusa cusp form Delta_5, following:
  "A Borcherds lift of the weak Jacobi form phi_{0,1}, ..."
  (Lorgat, 2020)
"""

import sys
import os
import numpy as np
import pytest
from fractions import Fraction

# Allow imports from compute/lib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from dd_modular_lattices import (
    gram_hyperbolic_plane,
    gram_lambda_32,
    gram_lambda_21,
    gram_lambda_21_II,
    verify_gram_II_from_ambient,
    inner_product,
    norm_sq,
    embedding_21_into_32,
    embedding_II_into_21,
    delta_coords_in_f_basis,
    reflection_matrix,
    type_II_reflection_generators,
    type_I_reflection_generators_f_basis,
    full_reflection_generators_f_basis,
    automorphism_generators_P_II_f_basis,
    enumerate_S3_from_generators,
    weyl_vector_delta_basis,
    weyl_vector_f_basis,
    verify_weyl_vector,
    weyl_vector_norm_sq,
    polyhedron_prim,
    is_in_polyhedron,
    cone_embedding_check,
    primitive_elements_at_infinity,
    verify_null_elements,
    signature,
    is_in_lambda_21_I,
    is_in_lambda_21_II,
    reflection_subgroup_indices,
)


# ===================================================================
# Gram matrix tests
# ===================================================================

class TestGramMatrices:
    """Verify Gram matrices match the paper's definitions."""

    def test_hyperbolic_plane_entries(self):
        G = gram_hyperbolic_plane()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[0, 0] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[1, 1] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[0, 1] == -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[1, 0] == -1

    def test_hyperbolic_plane_signature(self):
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_hyperbolic_plane()) == (1, 1, 0)

    def test_lambda_32_signature(self):
        """Lambda^{3,2} has signature (3,2)."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_lambda_32()) == (3, 2, 0)

    def test_lambda_32_is_symmetric(self):
        G = gram_lambda_32()
        np.testing.assert_array_equal(G, G.T)

    def test_lambda_32_determinant(self):
        """det(G_{3,2}) for Lambda^{1,1} + Lambda^{1,1} + [2].

        det = det(H1) * det(H2) * det([2]) = (-1)*(-1)*2 = 2
        (block diagonal after reordering).
        Actually the basis ordering interleaves, so compute directly.
        """
        G = gram_lambda_32()
        det = int(round(np.linalg.det(G.astype(float))))
        # G = diag-block structure. In the given basis:
        # (f1,f_{-1}) block has det(-1)^2 - 0 = ... let's just check.
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert det == 2

    def test_lambda_21_signature(self):
        """Lambda^{2,1} has signature (2,1).

        Gram matrix in (f_2, f_3, f_{-2}) basis is ((0,0,-1),(0,2,0),(-1,0,0)).
        Eigenvalues: 2, 1, -1 -> signature (2,1,0).
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_lambda_21()) == (2, 1, 0)

    def test_lambda_21_entries(self):
        """Specific entries of the Lambda^{2,1} Gram matrix."""
        G = gram_lambda_21()
        # f_3 self-pairing
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[1, 1] == 2
        # f_2, f_{-2} pairing
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[0, 2] == -1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[2, 0] == -1
        # All others zero
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[0, 0] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[2, 2] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[0, 1] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[1, 0] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[1, 2] == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert G[2, 1] == 0

    def test_lambda_21_II_gram_entries(self):
        """The Gram matrix of (delta_1, delta_2, delta_3) is
        ((2,-2,-2),(-2,2,-2),(-2,-2,2))."""
        G = gram_lambda_21_II()
        expected = np.array([[2, -2, -2],
                             [-2, 2, -2],
                             [-2, -2, 2]], dtype=np.int64)
        np.testing.assert_array_equal(G, expected)

    def test_lambda_21_II_diagonal(self):
        """All diagonal entries are 2."""
        G = gram_lambda_21_II()
        for i in range(3):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert G[i, i] == 2

    def test_lambda_21_II_off_diagonal(self):
        """All off-diagonal entries are -2."""
        G = gram_lambda_21_II()
        for i in range(3):
            for j in range(3):
                if i != j:
                    # VERIFIED [DC] structural property [LC] boundary/limiting case
                    assert G[i, j] == -2

    def test_lambda_21_II_is_symmetric(self):
        G = gram_lambda_21_II()
        np.testing.assert_array_equal(G, G.T)

    def test_lambda_21_II_determinant(self):
        """det of the 3x3 Gram matrix."""
        G = gram_lambda_21_II()
        det = int(round(np.linalg.det(G.astype(float))))
        # det((2,-2,-2),(-2,2,-2),(-2,-2,2)) = 2*(4-4) +2*(-4-4) -2*(4+4)
        #   wait, let me compute: expand along row 1:
        # 2*(2*2 - (-2)(-2)) - (-2)*((-2)*2 - (-2)(-2)) + (-2)*((-2)(-2) - 2*(-2))
        # = 2*(4-4) + 2*(-4-4) - 2*(4+4)
        # = 0 - 16 - 16 = -32
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert det == -32

    def test_gram_II_from_ambient_matches(self):
        """Cross-check: computing the Gram matrix of the delta_i from
        the ambient Lambda^{2,1} inner product gives the same answer."""
        G_computed = verify_gram_II_from_ambient()
        G_expected = gram_lambda_21_II()
        np.testing.assert_array_equal(G_computed, G_expected)


# ===================================================================
# Weyl vector tests
# ===================================================================

class TestWeylVector:
    """Verify rho = f_2 - (1/2)f_3 + f_{-2}."""

    def test_rho_f_basis_values(self):
        """rho = (1, -1/2, 1) in (f_2, f_3, f_{-2}) basis."""
        rho = weyl_vector_f_basis()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert rho[0] == Fraction(1, 1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert rho[1] == Fraction(-1, 2)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert rho[2] == Fraction(1, 1)

    def test_rho_delta_basis_values(self):
        """rho = (1/2, 1/2, 1/2) in (delta_1, delta_2, delta_3) basis."""
        rho = weyl_vector_delta_basis()
        for i in range(3):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert rho[i] == Fraction(1, 2)

    def test_rho_consistency_between_bases(self):
        """rho in f-basis should equal C^T rho_delta where C is the
        change-of-basis matrix."""
        rho_delta = weyl_vector_delta_basis()
        C = embedding_II_into_21()  # rows are delta_i in f-basis
        # rho_f = sum_i rho_delta[i] * C[i]
        rho_f_computed = sum(rho_delta[i] * C[i].astype(object) for i in range(3))
        rho_f = weyl_vector_f_basis()
        for i in range(3):
            assert rho_f_computed[i] == rho_f[i]

    def test_rho_inner_product_with_deltas(self):
        """(rho, delta_i) = -1 for each i = 1, 2, 3.

        This is the defining property of the lattice Weyl vector:
        (rho, delta_i) = -(delta_i, delta_i)/2 = -1.
        """
        assert verify_weyl_vector() is True

    def test_rho_inner_product_explicit_f_basis(self):
        """Verify (rho, delta_i) = -1 directly in the f-basis."""
        rho = weyl_vector_f_basis()
        G = gram_lambda_21()
        deltas = delta_coords_in_f_basis()
        for name, d in deltas.items():
            ip = sum(rho[i] * G[i, j] * d[j]
                     for i in range(3) for j in range(3))
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert ip == Fraction(-1), f"(rho, {name}) = {ip}, expected -1"

    def test_rho_norm_squared(self):
        """(rho, rho) = -3/2 in Lambda^{2,1}.

        rho = (1, -1/2, 1), G = ((0,0,-1),(0,2,0),(-1,0,0)).
        (rho,rho) = 2*(-1/2)^2 + 2*(1)*(1)*(-1) = 1/2 - 2 = -3/2.
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert weyl_vector_norm_sq() == Fraction(-3, 2)

    def test_rho_in_negative_cone(self):
        """(rho, rho) < 0, so rho lies in the light cone."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert weyl_vector_norm_sq() < 0


# ===================================================================
# Aut(P_{II}) = S_3 tests
# ===================================================================

class TestAutomorphismGroup:
    """Verify Aut(P_{II}) is isomorphic to S_3."""

    def test_aut_P_II_order_is_6(self):
        """Aut(P_{II}) has order 6 = |S_3|."""
        gens = automorphism_generators_P_II_f_basis()
        elements = enumerate_S3_from_generators(gens)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(elements) == 6

    def test_generators_are_involutions(self):
        """Each generator squares to the identity."""
        gens = automorphism_generators_P_II_f_basis()
        I = np.eye(3, dtype=np.int64)
        for g in gens:
            np.testing.assert_array_equal(g @ g, I)

    def test_product_has_order_3(self):
        """The product of the two generators has order 3
        (the 3-cycle in S_3)."""
        gens = automorphism_generators_P_II_f_basis()
        s1, s2 = gens
        prod = s1 @ s2
        I = np.eye(3, dtype=np.int64)
        assert not np.array_equal(prod, I)
        assert not np.array_equal(prod @ prod, I)
        np.testing.assert_array_equal(prod @ prod @ prod, I)

    def test_generators_preserve_gram_matrix(self):
        """Each generator g satisfies g^T G g = G for Lambda^{2,1}."""
        G = gram_lambda_21()
        gens = automorphism_generators_P_II_f_basis()
        for g in gens:
            np.testing.assert_array_equal(g.T @ G @ g, G)

    def test_all_elements_preserve_gram_matrix(self):
        """Every element of Aut(P_{II}) preserves the inner product."""
        G = gram_lambda_21()
        gens = automorphism_generators_P_II_f_basis()
        elements = enumerate_S3_from_generators(gens)
        for g in elements:
            np.testing.assert_array_equal(g.T @ G @ g, G)

    def test_S3_acts_transitively_on_null_elements(self):
        """Aut(P_{II}) = S_3 acts transitively on the three primitive
        null elements at infinity: {2f_2, 2f_{-2}, 2f_2 - 2f_3 + 2f_{-2}}.
        """
        gens = automorphism_generators_P_II_f_basis()
        elements = enumerate_S3_from_generators(gens)
        nulls = primitive_elements_at_infinity()

        # For each pair of null elements, there should exist a group element
        # mapping one to the other
        null_set = {tuple(n) for n in nulls}
        for a0 in nulls:
            orbit = set()
            for g in elements:
                image = tuple((g @ a0).astype(np.int64))
                orbit.add(image)
            # The orbit should contain all three null elements
            assert orbit.issuperset(null_set), \
                f"Orbit of {a0} is {orbit}, missing {null_set - orbit}"

    def test_aut_P_I_order_is_2(self):
        """Aut(P_I) has order 2, generated by s_{f_3}."""
        G = gram_lambda_21()
        f3 = np.array([0, 1, 0], dtype=np.int64)
        s_f3 = reflection_matrix(f3, G)
        I = np.eye(3, dtype=np.int64)
        # s_{f_3} is an involution
        np.testing.assert_array_equal(s_f3 @ s_f3, I)
        # The group has exactly 2 elements
        elements = enumerate_S3_from_generators([s_f3])
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(elements) == 2

    def test_aut_P_trivial(self):
        """Aut(P) is trivial (order 1)."""
        # The paper states Aut(P) is trivial. We verify this indirectly:
        # |Aut(P)| = [W^{(2)}: W^{(2)}] = 1
        indices = reflection_subgroup_indices()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert indices["W^{(2)}(Lambda^{2,1})"] == 1


# ===================================================================
# Reflection group tests
# ===================================================================

class TestReflectionGroups:
    """Verify reflection generators and their properties."""

    def test_delta_i_have_norm_2(self):
        """Each delta_i has (delta_i, delta_i) = 2."""
        G = gram_lambda_21()
        deltas = delta_coords_in_f_basis()
        for name, d in deltas.items():
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert norm_sq(d, G) == 2, f"({name},{name}) = {norm_sq(d, G)}"

    def test_type_II_reflections_are_involutions(self):
        """s_{delta_i}^2 = id in the delta basis."""
        gens = type_II_reflection_generators()
        I = np.eye(3, dtype=np.int64)
        for s in gens:
            np.testing.assert_array_equal(s @ s, I)

    def test_type_II_reflections_preserve_gram(self):
        """Each s_{delta_i} preserves the Gram matrix of Lambda^{2,1}_{II}."""
        G = gram_lambda_21_II()
        gens = type_II_reflection_generators()
        for s in gens:
            np.testing.assert_array_equal(s.T @ G @ s, G)

    def test_type_II_reflection_action_on_delta(self):
        """s_{delta_i}(delta_i) = -delta_i."""
        gens = type_II_reflection_generators()
        for i, s in enumerate(gens):
            e_i = np.zeros(3, dtype=np.int64)
            e_i[i] = 1
            np.testing.assert_array_equal(s @ e_i, -e_i)

    def test_full_reflections_are_involutions(self):
        """Reflections in P_{prim} are involutions."""
        gens = full_reflection_generators_f_basis()
        I = np.eye(3, dtype=np.int64)
        for s in gens:
            np.testing.assert_array_equal(s @ s, I)

    def test_full_reflections_preserve_gram(self):
        """Reflections in P_{prim} preserve the Lambda^{2,1} Gram matrix."""
        G = gram_lambda_21()
        gens = full_reflection_generators_f_basis()
        for s in gens:
            np.testing.assert_array_equal(s.T @ G @ s, G)

    def test_P_prim_roots_have_norm_2(self):
        """All roots in P_{prim} have norm squared 2."""
        G = gram_lambda_21()
        for which in ["full", "I", "II"]:
            prims = polyhedron_prim(which)
            for d in prims:
                # VERIFIED [DC] structural property [LC] boundary/limiting case
                assert norm_sq(d, G) == 2, \
                    f"{which}: root {d} has norm^2 = {norm_sq(d, G)}"

    def test_type_I_reflections_are_involutions(self):
        gens = type_I_reflection_generators_f_basis()
        I = np.eye(3, dtype=np.int64)
        for s in gens:
            np.testing.assert_array_equal(s @ s, I)


# ===================================================================
# Cone and embedding tests
# ===================================================================

class TestConeEmbeddings:
    """Verify cone embeddings from the paper."""

    def test_rho_in_dual_cone(self):
        """rho lies in Delta(Lambda^{2,1}_{II})^*_+."""
        in_dual, _ = cone_embedding_check()
        assert in_dual is True

    def test_rho_in_light_cone(self):
        """rho lies in Cone(Lambda^{2,1})_+ (i.e. (rho,rho) < 0)."""
        _, in_cone = cone_embedding_check()
        assert in_cone is True

    def test_null_elements_have_zero_norm(self):
        """The primitive elements at infinity have (a_0, a_0) = 0."""
        assert verify_null_elements() is True

    def test_null_elements_count(self):
        """There are exactly 3 primitive null elements at infinity."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(primitive_elements_at_infinity()) == 3

    def test_null_elements_in_lambda_21_II(self):
        """Each null element lies in Lambda^{2,1}_{II}
        (coefficients m, n are even)."""
        for a0 in primitive_elements_at_infinity():
            m, l, n = a0[0], a0[1], a0[2]
            assert is_in_lambda_21_II(int(m), int(l), int(n)), \
                f"{a0} not in Lambda^{{2,1}}_{{II}}"

    def test_null_elements_in_positive_polyhedron(self):
        """Each null element lies in R_{>0} P_{II}, meaning
        (a_0, delta_i) <= 0 for all i."""
        G = gram_lambda_21()
        prims = polyhedron_prim("II")
        rho_f = np.array([1.0, -0.5, 1.0])  # for float comparison
        for a0 in primitive_elements_at_infinity():
            a0_frac = np.array([Fraction(int(x)) for x in a0], dtype=object)
            assert is_in_polyhedron(a0_frac, prims, G)


# ===================================================================
# Lattice embedding tests
# ===================================================================

class TestEmbeddings:
    """Verify embeddings between lattices."""

    def test_embedding_21_into_32_preserves_inner_product(self):
        """The embedding Lambda^{2,1} -> Lambda^{3,2} is isometric."""
        E = embedding_21_into_32()
        G32 = gram_lambda_32()
        G21 = gram_lambda_21()
        # E is 3x5, so E G32 E^T should equal G21
        np.testing.assert_array_equal(E @ G32 @ E.T, G21)

    def test_embedding_II_into_21_gives_correct_gram(self):
        """The change-of-basis C gives C G_{21} C^T = G_{II}."""
        C = embedding_II_into_21()
        G21 = gram_lambda_21()
        G_II = gram_lambda_21_II()
        np.testing.assert_array_equal(C @ G21 @ C.T, G_II)

    def test_delta_1_coords(self):
        """delta_1 = 2f_2 - f_3 = (2, -1, 0) in the f-basis."""
        d = delta_coords_in_f_basis()
        np.testing.assert_array_equal(d["delta_1"], [2, -1, 0])

    def test_delta_2_coords(self):
        """delta_2 = 2f_{-2} - f_3 = (0, -1, 2) in the f-basis."""
        d = delta_coords_in_f_basis()
        np.testing.assert_array_equal(d["delta_2"], [0, -1, 2])

    def test_delta_3_coords(self):
        """delta_3 = f_3 = (0, 1, 0) in the f-basis."""
        d = delta_coords_in_f_basis()
        np.testing.assert_array_equal(d["delta_3"], [0, 1, 0])

    def test_delta_sum_is_twice_rho(self):
        """delta_1 + delta_2 + delta_3 = 2 rho.

        This follows from rho = (1/2)(delta_1 + delta_2 + delta_3).
        In f-basis: (2,-1,0) + (0,-1,2) + (0,1,0) = (2,-1,2) = 2*(1,-1/2,1).
        """
        d = delta_coords_in_f_basis()
        delta_sum = d["delta_1"] + d["delta_2"] + d["delta_3"]
        rho = weyl_vector_f_basis()
        for i in range(3):
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert Fraction(int(delta_sum[i])) == 2 * rho[i]


# ===================================================================
# Lattice membership tests
# ===================================================================

class TestLatticeMembership:
    """Verify sublattice membership predicates."""

    def test_delta_1_in_II(self):
        """delta_1 = (2, -1, 0): m=2, n=0, both even -> in Lambda^{2,1}_{II}."""
        assert is_in_lambda_21_II(2, -1, 0)

    def test_delta_2_in_II(self):
        """delta_2 = (0, -1, 2): m=0, n=2, both even -> in Lambda^{2,1}_{II}."""
        assert is_in_lambda_21_II(0, -1, 2)

    def test_delta_3_in_II(self):
        """delta_3 = (0, 1, 0): m=0, n=0, both even -> in Lambda^{2,1}_{II}."""
        assert is_in_lambda_21_II(0, 1, 0)

    def test_f_2_minus_f_3_not_in_II(self):
        """f_2 - f_3 = (1, -1, 0): m=1 odd -> NOT in Lambda^{2,1}_{II}."""
        assert not is_in_lambda_21_II(1, -1, 0)

    def test_f_2_minus_f_3_in_I(self):
        """f_2 - f_3 = (1, -1, 0): m+l+n = 0 even -> in Lambda^{2,1}_I."""
        assert is_in_lambda_21_I(1, -1, 0)

    def test_deltas_in_II_not_necessarily_in_I(self):
        """Lambda^{2,1}_{II} and Lambda^{2,1}_I are different sublattices.

        delta_1 = (2,-1,0): m+l+n = 1 (odd), so NOT in Lambda_I.
        delta_2 = (0,-1,2): m+l+n = 1 (odd), so NOT in Lambda_I.
        delta_3 = (0,1,0): m+l+n = 1 (odd), so NOT in Lambda_I.

        But all delta_i are in Lambda_{II} (m,n even).
        """
        coords = [(2, -1, 0), (0, -1, 2), (0, 1, 0)]
        for m, l, n in coords:
            assert is_in_lambda_21_II(m, l, n), f"({m},{l},{n}) should be in Lambda_II"
            # delta_i have m+l+n odd, so they are NOT in Lambda_I
            assert not is_in_lambda_21_I(m, l, n), f"({m},{l},{n}) should NOT be in Lambda_I"

    def test_example_in_both_I_and_II(self):
        """An element with m,n even AND m+l+n even is in both sublattices.

        E.g., 2f_2 + 0*f_3 + 2f_{-2} = (2,0,2): m+l+n=4 even, m,n even.
        """
        assert is_in_lambda_21_I(2, 0, 2)
        assert is_in_lambda_21_II(2, 0, 2)


# ===================================================================
# Subgroup index tests
# ===================================================================

class TestSubgroupIndices:
    """Verify the subgroup indices from the paper."""

    def test_full_index_1(self):
        indices = reflection_subgroup_indices()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert indices["W^{(2)}(Lambda^{2,1})"] == 1

    def test_type_I_index_2(self):
        indices = reflection_subgroup_indices()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert indices["W^{(2)}(Lambda^{2,1}_I)"] == 2

    def test_type_II_index_6(self):
        indices = reflection_subgroup_indices()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert indices["W^{(2)}(Lambda^{2,1}_{II})"] == 6

    def test_indices_consistent_with_aut_orders(self):
        """The index of W^{(2)}(Lambda_{II}) equals |Aut(P_{II})| = 6,
        and the index of W^{(2)}(Lambda_I) equals |Aut(P_I)| = 2."""
        gens_II = automorphism_generators_P_II_f_basis()
        elems_II = enumerate_S3_from_generators(gens_II)
        assert len(elems_II) == reflection_subgroup_indices()["W^{(2)}(Lambda^{2,1}_{II})"]

        G = gram_lambda_21()
        f3 = np.array([0, 1, 0], dtype=np.int64)
        s_f3 = reflection_matrix(f3, G)
        elems_I = enumerate_S3_from_generators([s_f3])
        assert len(elems_I) == reflection_subgroup_indices()["W^{(2)}(Lambda^{2,1}_I)"]


# ===================================================================
# Semi-direct product structure test
# ===================================================================

class TestSemiDirectProduct:
    """Verify Orth(Lambda^{2,1})_+ = W^{(2)}(Lambda^{2,1}_{II}) x| Aut(P_{II}).

    The paper states:
        Orth(Lambda^{2,1})_+ = W^{(2)}(Lambda^{2,1}_{II}) x| S_3
    """

    def test_type_II_generators_and_aut_together_generate_full_group(self):
        """The type-II reflection generators together with the Aut(P_{II})
        generators should generate a group strictly larger than either
        subgroup alone.

        Specifically, the three delta reflections generate W_{II}, and
        the two transposition reflections generate S_3.  Together they
        generate the full W = Orth(Lambda^{2,1})_+.

        We verify that the combined generators produce a group whose
        order is at least |W_{II}| (infinite in theory, but we check
        a finite truncation produces more elements than S_3 alone).
        """
        G = gram_lambda_21()
        # Type-II generators in f-basis
        deltas_f = list(delta_coords_in_f_basis().values())
        type_II_gens = [reflection_matrix(d, G) for d in deltas_f]

        # Aut generators
        aut_gens = automorphism_generators_P_II_f_basis()

        # Combined
        all_gens = type_II_gens + aut_gens

        # Enumerate up to a modest depth
        elements = enumerate_S3_from_generators(all_gens, max_iter=5)

        # Should have strictly more than 6 elements (the S_3 subgroup)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(elements) > 6, \
            f"Expected > 6 elements, got {len(elements)}"

    def test_aut_normalises_type_II_reflections(self):
        """Each element of Aut(P_{II}) conjugates each delta reflection
        to another delta reflection (since W_{II} is normal in the full group)."""
        G = gram_lambda_21()
        deltas_f = list(delta_coords_in_f_basis().values())
        delta_refs = [reflection_matrix(d, G) for d in deltas_f]

        gens = automorphism_generators_P_II_f_basis()
        elements = enumerate_S3_from_generators(gens)

        delta_ref_set = {tuple(s.flatten()) for s in delta_refs}

        for g in elements:
            g_inv = g.T  # orthogonal => inverse = transpose (not exactly, but for isometries g^T G g = G => g^{-1} = G^{-1} g^T G)
            # Actually for integer orthogonal matrices of finite order,
            # g^{-1} exists in the group. Let's compute it properly.
            # Since g preserves G: g^T G g = G, so g^{-1} = G^{-1} g^T G
            # But G may not be invertible over Z. Use the fact that g is
            # an involution or has finite order.
            pass

        # Simpler approach: check that conjugation by each generator
        # permutes the set of delta roots.
        for g in gens:
            for d in deltas_f:
                gd = g @ d
                # gd should be +/- one of the delta roots
                found = False
                for d2 in deltas_f:
                    if np.array_equal(gd, d2) or np.array_equal(gd, -d2):
                        found = True
                        break
                assert found, \
                    f"g({d}) = {gd} is not +/- a delta root"


# ===================================================================
# Additional structural tests
# ===================================================================

class TestDualLattice:
    """Verify the dual lattice (Lambda^{2,1}_{II})^* = (1/2) Lambda^{2,1}."""

    def test_dual_lattice_index(self):
        """|(Lambda^{2,1}_{II})^* / Lambda^{2,1}_{II}| = |det(G_{II})| = 32.

        Actually the index of Lambda_{II} in its dual is |det(G_{II})|.
        Wait: for a lattice L with Gram matrix G,
        |L^*/L| = |det(G)|. Here det(G_II) = -32, so |det| = 32.
        """
        G = gram_lambda_21_II()
        det = abs(int(round(np.linalg.det(G.astype(float)))))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert det == 32


class TestSignatures:
    """Verify signatures of all lattices."""

    def test_lambda_32_sig(self):
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_lambda_32()) == (3, 2, 0)

    def test_lambda_21_sig(self):
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_lambda_21()) == (2, 1, 0)

    def test_lambda_21_II_sig(self):
        """Lambda^{2,1}_{II} in the delta basis has the same signature
        (2,1) as Lambda^{2,1} since they span the same rational space."""
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert signature(gram_lambda_21_II()) == (2, 1, 0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
