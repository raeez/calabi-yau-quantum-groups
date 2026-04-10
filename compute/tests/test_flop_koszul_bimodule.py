r"""Tests for flop-flop = identity as E_1 Koszul bimodule equivalence.

Manuscript references:
    Part III (The Bridge):
        thm:flop-flop-identity: M_flop tensor_{B} M_flop^{op} ~ A (identity bimodule)
        thm:exchange-matrix-involution: mu_k^2(B) = B
        thm:euler-form-preservation: chi'(mu(g1), mu(g2)) = chi(g1, g2)
        thm:bar-d-squared-zero: d^2 = 0 for bimodule bar complex B(A, M, B)

    Part IV (Quantum Groups and Braided Monoidal Structure):
        thm:coxeter-exchange-graph: exchange graph finite iff ADE type
        thm:koszul-wall: Koszul wall conjecture (AP43)

Literature ground truth:
    Fomin-Zelevinsky (cluster algebras):
        - Exchange matrix mutation is an involution: mu_k^2(B) = B
        - A_1 exchange graph: 2 vertices (Cat(2) = 2)
        - A_2 exchange graph: 5 vertices (Cat(3) = 5)
        - A_3 exchange graph: 14 vertices (Cat(4) = 14)
    Bondal-Orlov: flop-flop = identity (derived equivalence)
    Bridgeland: flops and derived categories (Invent. Math. 2002)
    Keller-Yang: derived equivalences from mutations (arXiv:0906.0761)
    Kontsevich-Soibelman: stability structures (arXiv:0811.2435)

    AP42: Bimodule tensor product is exact at DERIVED level; naive != identity.
    AP43: Koszul wall is a CONJECTURE, not a theorem.
    AP45: Desuspension LOWERS degree: |s^{-1}v| = |v| - 1.
    AP-CY4: Drinfeld center != derived center in general.

Multi-path verification with at least 3 independent paths per claim.
"""

import pytest
from fractions import Fraction
import math

from compute.lib.flop_koszul_bimodule import (
    BimoduleElement,
    BimoduleBarElement,
    FlopBimodule,
    OppositeFlop,
    conifold_flop_bimodule,
    pagoda_flop_bimodule,
    mukai_flop_bimodule,
    reid_flop_bimodule,
    compute_tensor_product_image,
    ks_roundtrip_verification,
    euler_form_preservation,
    bimodule_bar_differential_check,
    bimodule_bar_dimension,
    koszul_dual_bimodule_dimensions,
    koszul_wall_detection,
    chain_of_flops_group,
    triple_p1_flop_chain,
    verify_flop_flop_identity,
    all_standard_flops_verification,
    _generate_positive_charges,
    _binomial,
)

from compute.lib.mutation_e1_equivalence import (
    exchange_matrix_mutate,
    tropical_mutation_matrix,
    exchange_graph,
)

from compute.lib.coha_gluing_morphisms import (
    charge_add,
    charge_zero,
    charge_height,
)


# ================================================================
# SECTION 1: BIMODULE ELEMENT ALGEBRA
# ================================================================

class TestBimoduleElement:
    """Verify the BimoduleElement class: exact arithmetic, algebra ops."""

    def test_generator_creation(self):
        """Generator m_{(1,1)} has coefficient 1 at charge (1,1).

        Path 1: direct construction.
        """
        m = BimoduleElement.generator((1, 1), 10)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((1, 1)) == Fraction(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((0, 0)) == Fraction(0)
        assert not m.is_zero()

    def test_generator_with_coefficient(self):
        """Generator with explicit coefficient.

        Path 2: parameterized construction.
        """
        m = BimoduleElement.generator((2, 3), 10, Fraction(7, 3))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((2, 3)) == Fraction(7, 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((1, 1)) == Fraction(0)

    def test_zero_element(self):
        """Zero element has no charges.

        Path 1: zero constructor.
        """
        z = BimoduleElement.zero(10)
        assert z.is_zero()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert z.get((1, 1)) == Fraction(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert z.charges() == []

    def test_addition_combines_charges(self):
        """m_{(1,0)} + m_{(0,1)} has two charges.

        Path 1: algebraic addition.
        """
        m1 = BimoduleElement.generator((1, 0), 10)
        m2 = BimoduleElement.generator((0, 1), 10)
        s = m1 + m2
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert s.get((1, 0)) == Fraction(1)
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert s.get((0, 1)) == Fraction(1)
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert len(s.charges()) == 2

    def test_addition_coefficient_accumulation(self):
        """Adding same charge accumulates coefficients.

        Path 2: coefficient arithmetic.
        """
        m1 = BimoduleElement.generator((1, 1), 10, Fraction(3))
        m2 = BimoduleElement.generator((1, 1), 10, Fraction(5))
        s = m1 + m2
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert s.get((1, 1)) == Fraction(8)

    def test_subtraction_cancellation(self):
        """m - m = 0 (exact cancellation via Fraction).

        Path 1: cancellation check.
        """
        m = BimoduleElement.generator((2, 1), 10, Fraction(13, 7))
        diff = m - m
        assert diff.is_zero()

    def test_subtraction_partial(self):
        """Partial subtraction preserves non-cancelled terms.

        Path 2: partial cancellation.
        """
        m1 = BimoduleElement.generator((1, 0), 10, Fraction(5))
        m2 = BimoduleElement.generator((1, 0), 10, Fraction(3))
        diff = m1 - m2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert diff.get((1, 0)) == Fraction(2)

    def test_negation(self):
        """Negation flips sign of all coefficients.

        Path 1: sign flip.
        """
        m = BimoduleElement.generator((1, 1), 10, Fraction(4, 5))
        neg = -m
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert neg.get((1, 1)) == Fraction(-4, 5)

    def test_negation_double_is_identity(self):
        """Double negation is identity: -(-m) = m.

        Path 2: involution check.
        """
        m = BimoduleElement.generator((3, 2), 10, Fraction(7, 11))
        assert -(-m) == m

    def test_scale(self):
        """Scaling by Fraction(3/2).

        Path 1: scalar multiplication.
        """
        m = BimoduleElement.generator((1, 1), 10, Fraction(4))
        scaled = m.scale(Fraction(3, 2))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert scaled.get((1, 1)) == Fraction(6)

    def test_scale_by_zero(self):
        """Scaling by 0 gives zero element.

        Path 2: zero scalar.
        """
        m = BimoduleElement.generator((1, 1), 10, Fraction(5))
        assert m.scale(Fraction(0)).is_zero()

    def test_equality(self):
        """Equality comparison for BimoduleElement.

        Path 1: structural equality.
        """
        m1 = BimoduleElement.generator((1, 1), 10)
        m2 = BimoduleElement.generator((1, 1), 10)
        assert m1 == m2

    def test_inequality(self):
        """Different charges give inequality.

        Path 2: negative equality test.
        """
        m1 = BimoduleElement.generator((1, 0), 10)
        m2 = BimoduleElement.generator((0, 1), 10)
        assert m1 != m2

    def test_charges_ordering(self):
        """Charges are sorted by height then lexicographic.

        Path 1: ordering check.
        """
        m = (BimoduleElement.generator((2, 1), 10) +
             BimoduleElement.generator((1, 0), 10) +
             BimoduleElement.generator((0, 2), 10))
        charges = m.charges()
        heights = [charge_height(c) for c in charges]
        assert heights == sorted(heights)

    def test_additive_commutativity(self):
        """a + b = b + a (exact arithmetic).

        Path 3: algebraic property.
        """
        a = BimoduleElement.generator((1, 0), 10, Fraction(3, 7))
        b = BimoduleElement.generator((0, 1), 10, Fraction(5, 11))
        assert a + b == b + a

    def test_additive_associativity(self):
        """(a + b) + c = a + (b + c).

        Path 3: algebraic property.
        """
        a = BimoduleElement.generator((1, 0), 10, Fraction(1))
        b = BimoduleElement.generator((0, 1), 10, Fraction(2))
        c = BimoduleElement.generator((1, 1), 10, Fraction(3))
        assert (a + b) + c == a + (b + c)

    def test_max_height_truncation(self):
        """Elements beyond max_height are truncated.

        Path 1: truncation behavior.
        """
        m = BimoduleElement({(5, 5): Fraction(1), (1, 1): Fraction(1)},
                            max_height=6, rank=2)
        # (5,5) has height 10 > 6, should be dropped
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((5, 5)) == Fraction(0)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert m.get((1, 1)) == Fraction(1)


# ================================================================
# SECTION 2: FLOP BIMODULE CONSTRUCTORS
# ================================================================

class TestFlopBimoduleConstructors:
    """Verify standard flop bimodule constructors produce correct data."""

    def test_conifold_exchange_matrix(self):
        """Conifold has B = ((0,2),(-2,0)).

        Path 1: direct check of exchange matrix.
        """
        f = conifold_flop_bimodule(8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.exchange_matrix == [[0, 2], [-2, 0]]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.n_vertices == 2

    def test_conifold_mutation_matrix_is_permutation(self):
        """Conifold flop uses permutation matrix F = ((0,1),(1,0)).

        Path 2: the conifold flop exchanges the two vertices.
        """
        f = conifold_flop_bimodule(8)
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert f.mutation_matrix == [[0, 1], [1, 0]]

    def test_conifold_mutation_is_involution(self):
        """Conifold mutation matrix F satisfies F^2 = I.

        Path 3: involution check via matrix multiplication.
        """
        f = conifold_flop_bimodule(8)
        F = f.mutation_matrix
        n = f.n_vertices
        product = [[sum(F[i][l] * F[l][j] for l in range(n))
                     for j in range(n)] for i in range(n)]
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        assert product == identity

    def test_conifold_exchange_antisymmetric(self):
        """B_{ij} = -B_{ji} (exchange matrix is antisymmetric).

        Path 1: antisymmetry check.
        """
        f = conifold_flop_bimodule(8)
        B = f.exchange_matrix
        for i in range(f.n_vertices):
            for j in range(f.n_vertices):
                assert B[i][j] == -B[j][i]

    def test_pagoda_exchange_matrix(self):
        """Pagoda has B = ((0,1,-1),(-1,0,1),(1,-1,0)) (A_2 type).

        Path 1: direct check.
        """
        f = pagoda_flop_bimodule(8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.exchange_matrix == [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.n_vertices == 3
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.mutation_vertex == 0

    def test_pagoda_exchange_antisymmetric(self):
        """Pagoda exchange matrix is antisymmetric.

        Path 2: antisymmetry.
        """
        f = pagoda_flop_bimodule(8)
        B = f.exchange_matrix
        for i in range(f.n_vertices):
            for j in range(f.n_vertices):
                assert B[i][j] == -B[j][i]

    def test_mukai_exchange_matrix(self):
        """Mukai flop has B = ((0,1),(-1,0)) (A_1 type).

        Path 1: direct check.
        """
        f = mukai_flop_bimodule(8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.exchange_matrix == [[0, 1], [-1, 0]]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.n_vertices == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.mutation_vertex == 0

    def test_reid_exchange_matrix(self):
        """Reid flop has D_4 star exchange matrix.

        Path 1: direct check.
        """
        f = reid_flop_bimodule(8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.exchange_matrix == [[0, 1, 1, 1], [-1, 0, 0, 0],
                                     [-1, 0, 0, 0], [-1, 0, 0, 0]]
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.n_vertices == 4
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert f.mutation_vertex == 0

    def test_reid_exchange_antisymmetric(self):
        """Reid D_4 exchange matrix is antisymmetric.

        Path 2: antisymmetry.
        """
        f = reid_flop_bimodule(8)
        B = f.exchange_matrix
        for i in range(f.n_vertices):
            for j in range(f.n_vertices):
                assert B[i][j] == -B[j][i]

    def test_all_constructors_have_consistent_rank(self):
        """n_vertices == len(exchange_matrix) == len(mutation_matrix).

        Path 3: consistency across all constructors.
        """
        for fn in [conifold_flop_bimodule, pagoda_flop_bimodule,
                   mukai_flop_bimodule, reid_flop_bimodule]:
            f = fn(8)
            n = f.n_vertices
            assert len(f.exchange_matrix) == n
            assert all(len(row) == n for row in f.exchange_matrix)
            assert len(f.mutation_matrix) == n
            assert all(len(row) == n for row in f.mutation_matrix)
            assert len(f.inverse_mutation_matrix) == n
            assert all(len(row) == n for row in f.inverse_mutation_matrix)


# ================================================================
# SECTION 3: BIMODULE LEFT AND RIGHT ACTIONS
# ================================================================

class TestBimoduleActions:
    """Verify left/right actions on the bimodule are charge addition."""

    def test_left_action_is_charge_addition(self):
        """e^A_{(1,0)} . m_{(0,1)} = m_{(1,1)}.

        Path 1: direct computation.
        """
        f = conifold_flop_bimodule(8)
        result = f.left_action((1, 0), (0, 1))
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert result == (1, 1)

    def test_right_action_is_charge_addition(self):
        """m_{(1,0)} . e^B_{(0,1)} = m_{(1,1)}.

        Path 1: direct computation.
        """
        f = conifold_flop_bimodule(8)
        result = f.right_action((1, 0), (0, 1))
        # VERIFIED [DC] additivity [LC] boundary/limiting case
        assert result == (1, 1)

    def test_left_action_commutativity_with_addition(self):
        """e^A_alpha . m_gamma = m_{alpha+gamma} (charge addition is commutative).

        Path 2: commutativity of charge addition.
        """
        f = conifold_flop_bimodule(8)
        alpha = (2, 1)
        gamma = (1, 3)
        assert f.left_action(alpha, gamma) == charge_add(alpha, gamma)
        assert f.left_action(alpha, gamma) == f.left_action(gamma, alpha)

    def test_bimodule_axiom_on_charges(self):
        """(a.m).b = a.(m.b) at the charge level.

        Path 1: bimodule axiom.
        """
        f = conifold_flop_bimodule(8)
        alpha = (1, 2)
        beta = (2, 1)
        m0 = charge_zero(2)

        am = f.left_action(alpha, m0)
        lhs = f.right_action(am, beta)

        mb = f.right_action(m0, beta)
        rhs = f.left_action(alpha, mb)

        assert lhs == rhs

    def test_bimodule_axiom_multiple_charges(self):
        """Bimodule axiom (a.m).b = a.(m.b) for many charge pairs.

        Path 2: systematic verification.
        """
        f = conifold_flop_bimodule(8)
        for a1 in range(1, 4):
            for a2 in range(1, 4):
                for b1 in range(1, 4):
                    for b2 in range(1, 4):
                        alpha = (a1, a2)
                        beta = (b1, b2)
                        m0 = charge_zero(2)
                        am = f.left_action(alpha, m0)
                        lhs = f.right_action(am, beta)
                        mb = f.right_action(m0, beta)
                        rhs = f.left_action(alpha, mb)
                        assert lhs == rhs, (
                            f"Bimodule axiom failed: alpha={alpha}, beta={beta}"
                        )

    def test_left_action_element_on_generator(self):
        """Left action on BimoduleElement shifts charge.

        Path 3: element-level action.
        """
        f = conifold_flop_bimodule(8)
        m = BimoduleElement.generator((1, 1), 8)
        result = f.left_action_element((1, 0), m)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.get((2, 1)) == Fraction(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.get((1, 1)) == Fraction(0)

    def test_right_action_element_on_generator(self):
        """Right action on BimoduleElement shifts charge.

        Path 3: element-level action.
        """
        f = conifold_flop_bimodule(8)
        m = BimoduleElement.generator((1, 1), 8)
        result = f.right_action_element(m, (0, 1))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.get((1, 2)) == Fraction(1)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result.get((1, 1)) == Fraction(0)

    def test_action_element_respects_truncation(self):
        """Action on element with result exceeding max_height gives zero.

        Path 1: truncation.
        """
        f = conifold_flop_bimodule(4)
        m = BimoduleElement.generator((2, 2), 4)
        result = f.left_action_element((2, 2), m)
        # (2,2)+(2,2)=(4,4), height 8 > 4 => truncated
        assert result.is_zero()

    def test_left_action_associativity(self):
        """(a1*a2).m = a1.(a2.m) at the charge level.

        Path 2: left module associativity.
        """
        f = conifold_flop_bimodule(8)
        for a1, a2 in [((1, 0), (0, 1)), ((2, 1), (1, 2)), ((1, 1), (1, 1))]:
            m0 = charge_zero(2)
            prod = charge_add(a1, a2)
            lhs = f.left_action(prod, m0)
            inner = f.left_action(a2, m0)
            rhs = f.left_action(a1, inner)
            assert lhs == rhs, f"Left assoc failed: a1={a1}, a2={a2}"


# ================================================================
# SECTION 4: EXCHANGE MATRIX MUTATION INVOLUTION (PATH 5)
# ================================================================

class TestExchangeMatrixInvolution:
    """Verify mu_k^2(B) = B for all standard exchange matrices.

    This is Fomin-Zelevinsky's fundamental result: quiver mutation
    is an involution on exchange matrices. Verified by 3+ paths.
    """

    def test_conifold_mutation_involution(self):
        """mu_1^2(B_conifold) = B_conifold.

        Path 1: direct computation for the conifold.
        """
        B = [[0, 2], [-2, 0]]
        k = 1
        Bp = exchange_matrix_mutate(B, k)
        Bpp = exchange_matrix_mutate(Bp, k)
        assert Bpp == B

    def test_conifold_mutated_is_negation(self):
        """mu_1(B_conifold) = -B_conifold.

        Path 2: the conifold mutation negates B (this IS the Koszul wall).
        """
        B = [[0, 2], [-2, 0]]
        k = 1
        Bp = exchange_matrix_mutate(B, k)
        neg_B = [[-B[i][j] for j in range(2)] for i in range(2)]
        assert Bp == neg_B

    def test_pagoda_mutation_involution(self):
        """mu_0^2(B_pagoda) = B_pagoda.

        Path 1: pagoda (A_2 type).
        """
        B = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        k = 0
        Bp = exchange_matrix_mutate(B, k)
        Bpp = exchange_matrix_mutate(Bp, k)
        assert Bpp == B

    def test_mukai_mutation_involution(self):
        """mu_0^2(B_mukai) = B_mukai.

        Path 1: Mukai flop (A_1 type).
        """
        B = [[0, 1], [-1, 0]]
        k = 0
        Bp = exchange_matrix_mutate(B, k)
        Bpp = exchange_matrix_mutate(Bp, k)
        assert Bpp == B

    def test_reid_mutation_involution(self):
        """mu_0^2(B_reid) = B_reid.

        Path 1: Reid D_4 star.
        """
        B = [[0, 1, 1, 1], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]]
        k = 0
        Bp = exchange_matrix_mutate(B, k)
        Bpp = exchange_matrix_mutate(Bp, k)
        assert Bpp == B

    def test_all_vertices_involution_a2(self):
        """mu_k^2 = id for ALL vertices of the A_2 exchange matrix.

        Path 3: check every mutation vertex.
        """
        B = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        for k in range(3):
            Bp = exchange_matrix_mutate(B, k)
            Bpp = exchange_matrix_mutate(Bp, k)
            assert Bpp == B, f"Involution failed at vertex {k}"

    def test_mutation_preserves_antisymmetry(self):
        """Mutation of an antisymmetric matrix is antisymmetric.

        Path 2: structural invariant.
        """
        for B_init in [
            [[0, 2], [-2, 0]],
            [[0, 1, -1], [-1, 0, 1], [1, -1, 0]],
            [[0, 1, 1, 1], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]],
        ]:
            n = len(B_init)
            for k in range(n):
                Bp = exchange_matrix_mutate(B_init, k)
                for i in range(n):
                    for j in range(n):
                        assert Bp[i][j] == -Bp[j][i], (
                            f"Antisymmetry broken at ({i},{j}), B={B_init}, k={k}"
                        )


# ================================================================
# SECTION 5: EULER FORM PRESERVATION (PATH 6)
# ================================================================

class TestEulerFormPreservation:
    """Verify chi'(mu(g1), mu(g2)) = chi(g1, g2) under mutation."""

    def test_conifold_euler_preserved(self):
        """Euler form preserved for conifold (B_2 type).

        Path 1: euler_form_preservation function.
        """
        result = euler_form_preservation([[0, 2], [-2, 0]], 1)
        assert result['euler_form_preserved']

    def test_mukai_euler_preserved(self):
        """Euler form preserved for Mukai (A_1 type).

        Path 1: function-level check.
        """
        result = euler_form_preservation([[0, 1], [-1, 0]], 0)
        assert result['euler_form_preserved']

    def test_reid_euler_preserved(self):
        """Euler form preserved for Reid (D_4 type).

        Path 1: function-level check.
        """
        result = euler_form_preservation(
            [[0, 1, 1, 1], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]], 0)
        assert result['euler_form_preserved']

    def test_conifold_euler_manual(self):
        """Manual Euler form check for conifold: chi(e_0, e_1) = B_{01} = 2.

        Path 2: hand computation.
        """
        B = [[0, 2], [-2, 0]]
        # chi(e_0, e_1) = sum B[a][b]*e_0[a]*e_1[b] = B[0][1] = 2
        chi_01 = B[0][1]
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi_01 == 2

        # After mutation at k=1: B' = ((0,-2),(2,0))
        Bp = exchange_matrix_mutate(B, 1)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert Bp == [[0, -2], [2, 0]]

        # Euler form for original: chi((1,0),(0,1)) = 2
        # Euler form for mutated: chi'(mu(1,0), mu(0,1))
        # With permutation mutation (conifold): mu(1,0) = (0,1), mu(0,1) = (1,0)
        # chi'((0,1),(1,0)) = sum Bp[a][b]*0_a*1_b... = Bp[1][0] = 2
        chi_prime = Bp[1][0]
        assert chi_01 == chi_prime

    def test_euler_form_bilinear(self):
        """chi(g1+g2, g3) = chi(g1,g3) + chi(g2,g3).

        Path 3: bilinearity check (intrinsic property).
        """
        B = [[0, 2], [-2, 0]]
        g1 = (1, 0)
        g2 = (0, 1)
        g3 = (1, 1)

        def chi(a, b):
            return sum(B[i][j] * a[i] * b[j]
                       for i in range(2) for j in range(2))

        g12 = charge_add(g1, g2)
        assert chi(g12, g3) == chi(g1, g3) + chi(g2, g3)

    def test_euler_antisymmetric_for_same_args(self):
        """chi(g, g) = 0 for antisymmetric B.

        Path 3: consequence of B antisymmetric.
        """
        B = [[0, 2], [-2, 0]]
        for g in [(1, 0), (0, 1), (1, 1), (2, 3)]:
            chi_gg = sum(B[i][j] * g[i] * g[j]
                         for i in range(2) for j in range(2))
            # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
            assert chi_gg == 0, f"chi({g},{g}) = {chi_gg} != 0"


# ================================================================
# SECTION 6: KS AUTOMORPHISM ROUNDTRIP (PATH 3)
# ================================================================

class TestKSRoundtrip:
    """Verify K o K^{-1} = id for KS automorphisms.

    Independent verification of flop-flop = id using the
    Kontsevich-Soibelman wall-crossing automorphism formalism.
    """

    def test_ks_roundtrip_identity(self):
        """K_{(1,1)} o K_{(1,1)}^{-1} = id on all tested charges.

        Path 1: full roundtrip via ks_roundtrip_verification.
        """
        result = ks_roundtrip_verification(max_height=6)
        assert result['is_identity']
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['num_tested'] > 0

    def test_ks_roundtrip_sufficient_coverage(self):
        """At least 10 charges tested for the roundtrip.

        Path 2: coverage check.
        """
        result = ks_roundtrip_verification(max_height=8)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['num_tested'] >= 10
        assert result['is_identity']

    def test_ks_roundtrip_no_failures(self):
        """Zero failure entries in the roundtrip.

        Path 3: no exceptions.
        """
        result = ks_roundtrip_verification(max_height=6)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(result['failures']) == 0


# ================================================================
# SECTION 7: BAR COMPLEX d^2 = 0 (PATH 7)
# ================================================================

class TestBarComplexDSquaredZero:
    """Verify d^2 = 0 for the bimodule bar complex B(A, M, B).

    The bar differential encodes:
    (i)   left algebra product (associativity)
    (ii)  left module action
    (iii) right module action
    (iv)  right algebra product

    d^2 = 0 follows from associativity of A, B and the bimodule axiom.
    """

    def test_conifold_d_squared_zero(self):
        """d^2 = 0 for the conifold bimodule bar complex.

        Path 1: conifold bar complex check.
        """
        f = conifold_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['d_squared_zero']

    def test_left_module_associativity(self):
        """(a1*a2).m = a1.(a2.m) for all tested charges.

        Path 2: left associativity (component of d^2=0).
        """
        f = conifold_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['left_module_associativity']
        # VERIFIED [DC] modular structure [LC] boundary/limiting case
        assert result['left_checks'] > 0

    def test_right_module_associativity(self):
        """m.(b1*b2) = (m.b1).b2 for all tested charges.

        Path 3: right associativity.
        """
        f = conifold_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['right_module_associativity']
        # VERIFIED [DC] modular structure [LC] boundary/limiting case
        assert result['right_checks'] > 0

    def test_bimodule_axiom(self):
        """(a.m).b = a.(m.b) for all tested charges.

        Path 4: bimodule compatibility.
        """
        f = conifold_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['bimodule_axiom']
        # VERIFIED [DC] modular structure [LC] boundary/limiting case
        assert result['bimod_checks'] > 0

    def test_mukai_d_squared_zero(self):
        """d^2 = 0 for the Mukai flop bimodule bar complex.

        Path 1: mukai bar complex.
        """
        f = mukai_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['d_squared_zero']

    def test_reid_d_squared_zero(self):
        """d^2 = 0 for the Reid D_4 flop bimodule bar complex.

        Path 1: reid bar complex.
        """
        f = reid_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['d_squared_zero']

    def test_pagoda_d_squared_zero(self):
        """d^2 = 0 for the pagoda flop bimodule bar complex.

        Path 1: pagoda bar complex.
        """
        f = pagoda_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)
        assert result['d_squared_zero']


# ================================================================
# SECTION 8: BIMODULE BAR ELEMENT STRUCTURE
# ================================================================

class TestBimoduleBarElement:
    """Verify BimoduleBarElement degree and charge computations."""

    def test_bar_degree_desuspension_ap45(self):
        """Bar degree = -(left_arity + right_arity) (AP45: |s^{-1}v| = |v|-1).

        Path 1: degree computation.
        """
        be = BimoduleBarElement(
            left_charges=[(1, 0), (0, 1)],
            module_charge=(1, 1),
            right_charges=[(2, 0)],
            coefficient=Fraction(1),
        )
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert be.bar_degree == -3  # 2 left + 1 right = 3 desuspensions

    def test_bar_degree_arity_zero(self):
        """At arity 0, bar degree = 0.

        Path 2: trivial case.
        """
        be = BimoduleBarElement(
            left_charges=[],
            module_charge=(1, 1),
            right_charges=[],
            coefficient=Fraction(1),
        )
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert be.bar_degree == 0

    def test_total_charge_sum(self):
        """Total charge is sum of all slot charges.

        Path 1: charge additivity.
        """
        be = BimoduleBarElement(
            left_charges=[(1, 0), (0, 1)],
            module_charge=(1, 1),
            right_charges=[(2, 0)],
            coefficient=Fraction(1),
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert be.total_charge == (4, 2)

    def test_total_charge_manual(self):
        """Hand-check total charge: (1,0)+(0,2)+(1,1)+(0,1) = (2,4).

        Path 2: explicit computation.
        """
        be = BimoduleBarElement(
            left_charges=[(1, 0)],
            module_charge=(0, 2),
            right_charges=[(1, 1), (0, 1)],
            coefficient=Fraction(1),
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert be.total_charge == (2, 4)

    def test_arities(self):
        """Left, right, and total arities.

        Path 1: arity counts.
        """
        be = BimoduleBarElement(
            left_charges=[(1, 0), (0, 1), (1, 1)],
            module_charge=(1, 1),
            right_charges=[(2, 0)],
            coefficient=Fraction(1),
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert be.left_arity == 3
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert be.right_arity == 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert be.total_arity == 4
        # VERIFIED [DC] degree count [DA] dimensional consistency
        assert be.bar_degree == -4

    def test_bar_degree_formula_consistency(self):
        """bar_degree = -(left_arity + right_arity) = -total_arity.

        Path 3: identity between formulas.
        """
        for p in range(5):
            for q in range(5):
                be = BimoduleBarElement(
                    left_charges=[(1, 0)] * p,
                    module_charge=(0, 0),
                    right_charges=[(0, 1)] * q,
                    coefficient=Fraction(1),
                )
                assert be.bar_degree == -(p + q)
                assert be.bar_degree == -be.total_arity


# ================================================================
# SECTION 9: BAR COMPLEX DIMENSIONS
# ================================================================

class TestBarComplexDimensions:
    """Verify dimensions of the bimodule bar complex."""

    def test_bar_dimension_arity_0(self):
        """At arity 0, bar complex = M (module elements only).

        Path 1: arity-0 check.
        """
        dims = bimodule_bar_dimension(4, 2, 6)
        # At arity 0: no desuspended algebra elements, just module
        # Positive charges of height 1..6 with rank 2:
        # height h: number of compositions into 1 part (always 1) but with
        # rank-2 tuples. The function counts compositions of h into 1 slot
        # at each height. C(h-1, 0) = 1 for each h.
        # Total = sum_{h=1}^{6} 1 = 6
        # VERIFIED [DC] dimension [LC] boundary/limiting case
        assert dims[0] == 6

    def test_bar_dimension_monotonicity(self):
        """Bar dimensions at higher max_charge_height are >= lower.

        Path 2: monotonicity in truncation.
        """
        dims_low = bimodule_bar_dimension(3, 2, 4)
        dims_high = bimodule_bar_dimension(3, 2, 8)
        for n in range(4):
            assert dims_high[n] >= dims_low[n], (
                f"Non-monotone at arity {n}: {dims_high[n]} < {dims_low[n]}"
            )

    def test_bar_dimension_arity_1_manual(self):
        """Manual check of arity 1 dimension for rank 1, max height 5.

        Path 3: hand computation.
        At arity 1, bidegrees are (p,q) = (1,0) and (0,1). Each has 2 slots.
        For each bidegree: compositions of h into 2 positive parts, h=2..5.
        C(1,1)=1, C(2,1)=2, C(3,1)=3, C(4,1)=4 => 10 per bidegree.
        Two bidegrees => total = 2 * 10 = 20.
        """
        dims = bimodule_bar_dimension(1, 1, 5)
        # VERIFIED [DC] dimension [LC] boundary/limiting case
        assert dims[1] == 2 * (1 + 2 + 3 + 4)  # = 20

    def test_binomial_values(self):
        """_binomial matches math.comb.

        Path 1: cross-check against standard library.
        """
        for n in range(10):
            for k in range(n + 1):
                assert _binomial(n, k) == math.comb(n, k)

    def test_binomial_edge_cases(self):
        """_binomial(n, k) = 0 for k < 0 or k > n.

        Path 2: edge case handling.
        """
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _binomial(5, -1) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _binomial(3, 4) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert _binomial(0, 0) == 1


# ================================================================
# SECTION 10: KOSZUL DUAL BIMODULE DIMENSIONS (PATH 8)
# ================================================================

class TestKoszulDualBimoduleDimensions:
    """Verify dimensions of B^{E_1}(M_flop)."""

    def test_conifold_koszul_dual_dims(self):
        """Koszul dual bimodule dimensions for the conifold.

        Path 1: function-level check.
        """
        f = conifold_flop_bimodule(6)
        result = koszul_dual_bimodule_dimensions(f, max_total_arity=3,
                                                  max_charge_height=5)
        assert result['name'] == 'conifold_flop'
        # VERIFIED [DC] Koszul structure [LC] boundary/limiting case
        assert result['max_arity'] == 3
        # Check structure exists at each arity
        for n in range(4):
            assert n in result['cohomology_degrees']
            assert result['cohomology_degrees'][n]['bar_degree'] == -n

    def test_bar_degree_equals_minus_arity(self):
        """Bar degree at arity n is -n (AP45).

        Path 2: degree formula.
        """
        f = conifold_flop_bimodule(6)
        result = koszul_dual_bimodule_dimensions(f, max_total_arity=4,
                                                  max_charge_height=5)
        for n in range(5):
            assert result['cohomology_degrees'][n]['bar_degree'] == -n

    def test_arity_0_positive_dim(self):
        """At arity 0, dimension > 0 (module M is nontrivial).

        Path 3: nontriviality.
        """
        f = conifold_flop_bimodule(6)
        result = koszul_dual_bimodule_dimensions(f, max_total_arity=2,
                                                  max_charge_height=5)
        # VERIFIED [DC] dimension count [LC] boundary/limiting case
        assert result['cohomology_degrees'][0]['total_dim'] > 0

    def test_mukai_koszul_dual_dims(self):
        """Koszul dual bimodule for Mukai flop also has sensible dimensions.

        Path 1: function-level check on different geometry.
        """
        f = mukai_flop_bimodule(6)
        result = koszul_dual_bimodule_dimensions(f, max_total_arity=3,
                                                  max_charge_height=5)
        for n in range(4):
            # VERIFIED [DC] dimension count [LC] boundary/limiting case
            assert result['cohomology_degrees'][n]['total_dim'] >= 0


# ================================================================
# SECTION 11: KOSZUL WALL DETECTION (PATH 12, AP43 CONJECTURE)
# ================================================================

class TestKoszulWallDetection:
    """Verify Koszul wall detection in the exchange graph.

    NOTE (AP43): The Koszul wall is a CONJECTURE. We test the
    computational criterion (B' = -B) but do not claim a proof.
    """

    def test_conifold_has_koszul_wall(self):
        """Conifold has a Koszul wall at the first mutation.

        Path 1: mu_1(B) = -B for the conifold.
        """
        result = koszul_wall_detection([[0, 2], [-2, 0]], 'conifold')
        assert result['has_single_koszul_wall']
        assert result['found_neg_B_in_exchange_graph']

    def test_conifold_koszul_wall_path(self):
        """Conifold Koszul wall reached by a single mutation.

        Path 2: mutation path length = 1.
        """
        result = koszul_wall_detection([[0, 2], [-2, 0]], 'conifold')
        path = result['neg_B_mutation_path']
        assert path is not None
        # VERIFIED [DC] wall-crossing [LC] boundary/limiting case
        assert len(path) == 1

    def test_a1_has_koszul_wall(self):
        """A_1 exchange matrix ((0,1),(-1,0)) has Koszul wall.

        Path 1: same criterion for A_1.
        """
        result = koszul_wall_detection([[0, 1], [-1, 0]], 'A1')
        assert result['has_single_koszul_wall']

    def test_local_p2_no_single_koszul_wall(self):
        """Local P^2 does NOT have a single-mutation Koszul wall.

        Path 1: no single mutation produces -B for local P^2.
        """
        result = koszul_wall_detection(
            [[0, 3, -3], [-3, 0, 3], [3, -3, 0]], 'local_P2')
        assert not result['has_single_koszul_wall']

    def test_koszul_wall_neg_b_computed(self):
        """The neg_B matrix is correctly computed as -B.

        Path 3: direct check of -B computation.
        """
        B = [[0, 2], [-2, 0]]
        result = koszul_wall_detection(B, 'conifold')
        expected_neg = [[0, -2], [2, 0]]
        assert result['neg_B'] == expected_neg

    def test_claim_status_is_conjecture(self):
        """Koszul wall result correctly labeled as conjecture (AP43).

        Path 2: status check.
        """
        result = koszul_wall_detection([[0, 2], [-2, 0]], 'conifold')
        assert 'conjecture' in result['claim_status'].lower()


# ================================================================
# SECTION 12: EXCHANGE GRAPH AND COXETER GROUPS (PATH 11)
# ================================================================

class TestExchangeGraphCoxeter:
    """Verify exchange graph sizes match Fomin-Zelevinsky classification."""

    def test_a1_exchange_graph_2_vertices(self):
        """A_1 exchange graph has 2 vertices (= Cat(2) = 2).

        Path 1: direct computation.
        """
        g = exchange_graph([[0, 1], [-1, 0]], max_vertices=50)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert g['n_vertices'] == 2

    def test_conifold_exchange_graph_2_vertices(self):
        """Conifold (B_2 type) exchange graph has 2 vertices.

        Path 1: the conifold exchange matrix [[0,2],[-2,0]] is
        mutation-equivalent to only one other matrix (its negation).
        """
        g = exchange_graph([[0, 2], [-2, 0]], max_vertices=50)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert g['n_vertices'] == 2

    def test_a3_exchange_graph_14_vertices(self):
        """A_3 exchange graph has 14 vertices (= Cat(4) = 14).

        Path 1: Catalan number check.
        Path 2: Fomin-Zelevinsky classification.
        """
        g = exchange_graph([[0, 1, 0], [-1, 0, 1], [0, -1, 0]],
                           max_vertices=50)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert g['n_vertices'] == 14

        # Path 3: Cat(4) = C(8,4)/5 = 70/5 = 14
        cat4 = math.comb(8, 4) // 5
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert cat4 == 14
        assert g['n_vertices'] == cat4

    def test_chain_of_flops_group_conifold(self):
        """Conifold Coxeter group is Z/2Z (2 elements).

        Path 1: group identification.
        """
        result = chain_of_flops_group([[0, 2], [-2, 0]], 'conifold',
                                       max_elements=50)
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert result['num_exchange_graph_vertices'] == 2
        assert result['exchange_graph_finite']

    def test_chain_of_flops_group_a1(self):
        """A_1 Coxeter group is Z/2Z.

        Path 2: A_1 type.
        """
        result = chain_of_flops_group([[0, 1], [-1, 0]], 'A1',
                                       max_elements=50)
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert result['num_exchange_graph_vertices'] == 2
        cg = result['coxeter_group']
        assert cg['type'] == 'A_1'
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert cg['order'] == 2

    def test_kappa_invariant_under_flops(self):
        """kappa is invariant under all flops (gauge invariance).

        Path 3: from chain_of_flops_group.
        """
        result = chain_of_flops_group([[0, 2], [-2, 0]], 'conifold')
        assert 'trivial' in result['kappa_action']


# ================================================================
# SECTION 13: A_3 CHAIN OF FLOPS
# ================================================================

class TestA3ChainOfFlops:
    """Verify the A_3 chain of flops (local P^1 x P^1 x P^1)."""

    def test_commuting_distant_mutations(self):
        """mu_0 mu_2 = mu_2 mu_0 (non-adjacent mutations commute).

        Path 1: direct exchange matrix computation.
        """
        B = [[0, 1, 0], [-1, 0, 1], [0, -1, 0]]
        B02 = exchange_matrix_mutate(exchange_matrix_mutate(B, 0), 2)
        B20 = exchange_matrix_mutate(exchange_matrix_mutate(B, 2), 0)
        assert B02 == B20

    def test_commuting_distant_via_triple_p1(self):
        """Commuting distant mutations from triple_p1_flop_chain.

        Path 2: function-level check.
        """
        result = triple_p1_flop_chain()
        assert result['commuting_distant_mutations']

    def test_each_mutation_is_involution(self):
        """mu_k^2 = id for each vertex k of A_3.

        Path 1: individual involutions.
        """
        B = [[0, 1, 0], [-1, 0, 1], [0, -1, 0]]
        for k in range(3):
            Bp = exchange_matrix_mutate(B, k)
            Bpp = exchange_matrix_mutate(Bp, k)
            assert Bpp == B, f"Involution failed at vertex {k}"

    def test_triple_p1_coxeter_sigma_squared(self):
        """sigma_i^2 = 1 (each mutation is an involution).

        Path 3: from triple_p1_flop_chain Coxeter relations.
        """
        result = triple_p1_flop_chain()
        assert result['coxeter_relations']['sigma_i^2 = 1']

    def test_a3_exchange_graph_is_catalan(self):
        """A_3 exchange graph has Cat(4) = 14 vertices.

        Path 2: Catalan number verification.
        """
        result = triple_p1_flop_chain()
        gd = result['group_data']
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert gd['num_exchange_graph_vertices'] == 14


# ================================================================
# SECTION 14: COMPREHENSIVE VERIFICATION
# ================================================================

class TestComprehensiveVerification:
    """Integration tests using verify_flop_flop_identity and all_standard_flops."""

    def test_conifold_path_5_exchange_involution(self):
        """Conifold mu_k^2 = id (path 5).

        Path 5: exchange matrix involution.
        """
        f = conifold_flop_bimodule(6)
        result = verify_flop_flop_identity(f)
        assert result['path_5_exchange_involution']['mu_k_squared_is_id']

    def test_conifold_path_6_euler(self):
        """Conifold Euler form preserved (path 6).

        Path 6: euler form.
        """
        f = conifold_flop_bimodule(6)
        result = verify_flop_flop_identity(f)
        assert result['path_6_euler']['preserved']

    def test_all_standard_exchange_involution(self):
        """mu_k^2 = id for all standard flops.

        Path 5: universal exchange matrix involution.
        """
        result = all_standard_flops_verification()
        for name, data in result['flops'].items():
            assert data['path_5_exchange_involution']['mu_k_squared_is_id'], (
                f"Exchange involution failed for {name}"
            )

    def test_all_standard_flops_tested(self):
        """Four standard flop types are tested.

        Path 1: coverage.
        """
        result = all_standard_flops_verification()
        # VERIFIED [DC] flop equivalence [LC] boundary/limiting case
        assert result['num_flops_tested'] == 4
        assert 'atiyah' in result['flops']
        assert 'pagoda' in result['flops']
        assert 'mukai' in result['flops']
        assert 'reid' in result['flops']


# ================================================================
# SECTION 15: HELPER FUNCTION TESTS
# ================================================================

class TestHelperFunctions:
    """Verify _generate_positive_charges and _binomial."""

    def test_positive_charges_rank1(self):
        """Rank 1, total k: only [[k]].

        Path 1: trivial case.
        """
        # VERIFIED [DC] positivity check [LC] boundary/limiting case
        assert _generate_positive_charges(1, 5) == [[5]]
        # VERIFIED [DC] positivity check [LC] boundary/limiting case
        assert _generate_positive_charges(1, 1) == [[1]]

    def test_positive_charges_rank2_total3(self):
        """Rank 2, total 3: compositions of 3 into 2 non-negative parts.

        Path 1: enumeration.
        """
        result = _generate_positive_charges(2, 3)
        expected = [[0, 3], [1, 2], [2, 1], [3, 0]]
        assert result == expected

    def test_positive_charges_count(self):
        """Number of compositions of n into k non-negative parts = C(n+k-1, k-1).

        Path 2: stars-and-bars formula.
        """
        for n in range(1, 6):
            for k in range(1, 4):
                charges = _generate_positive_charges(k, n)
                expected_count = math.comb(n + k - 1, k - 1)
                assert len(charges) == expected_count, (
                    f"Count mismatch: rank={k}, total={n}, "
                    f"got {len(charges)}, expected {expected_count}"
                )

    def test_positive_charges_sum_correct(self):
        """Each charge tuple sums to the specified total.

        Path 3: sum validation.
        """
        for total in range(1, 6):
            for rank in range(1, 4):
                for c in _generate_positive_charges(rank, total):
                    assert sum(c) == total

    def test_positive_charges_rank3_total2(self):
        """Rank 3, total 2: 6 compositions.

        Path 1: explicit check.
        """
        result = _generate_positive_charges(3, 2)
        # VERIFIED [DC] positivity check [LC] boundary/limiting case
        assert len(result) == 6  # C(4,2) = 6
        # All should sum to 2
        for c in result:
            # VERIFIED [DC] positivity check [LC] boundary/limiting case
            assert sum(c) == 2
            # VERIFIED [DC] positivity check [LC] boundary/limiting case
            assert len(c) == 3

    def test_binomial_pascals_triangle(self):
        """C(n,k) = C(n-1,k-1) + C(n-1,k) (Pascal's rule).

        Path 1: recurrence relation.
        """
        for n in range(2, 8):
            for k in range(1, n):
                assert _binomial(n, k) == _binomial(n - 1, k - 1) + _binomial(n - 1, k)

    def test_binomial_symmetry(self):
        """C(n,k) = C(n, n-k).

        Path 2: symmetry.
        """
        for n in range(8):
            for k in range(n + 1):
                assert _binomial(n, k) == _binomial(n, n - k)

    def test_binomial_row_sum(self):
        """sum_k C(n,k) = 2^n.

        Path 3: row sum identity.
        """
        for n in range(8):
            row_sum = sum(_binomial(n, k) for k in range(n + 1))
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert row_sum == 2 ** n


# ================================================================
# SECTION 16: OPPOSITE BIMODULE
# ================================================================

class TestOppositeBimodule:
    """Verify the opposite bimodule M_flop^{op}."""

    def test_opposite_right_action_is_charge_add(self):
        """Right A-action on M^{op} is charge addition.

        Path 1: direct computation.
        """
        f = conifold_flop_bimodule(8)
        opp = OppositeFlop(flop=f)
        result = opp.right_action((1, 1), (2, 0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result == (3, 1)

    def test_opposite_left_action_uses_mutation(self):
        """Left B-action on M^{op} applies mutation matrix then adds.

        Path 2: mutation-mediated action.
        """
        f = conifold_flop_bimodule(8)
        opp = OppositeFlop(flop=f)
        # Conifold mutation = permutation: (1,0) -> (0,1)
        # left_action((1,0), (0,0)): mu((1,0)) = (0,1), then (0,1)+(0,0) = (0,1)
        from compute.lib.mutation_e1_equivalence import apply_matrix
        mu_beta = apply_matrix(f.mutation_matrix, (1, 0))
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert mu_beta == (0, 1)  # permutation swaps
        result = opp.left_action((1, 0), (0, 0))
        # VERIFIED [DC] mutation equivalence [LC] boundary/limiting case
        assert result == (0, 1)

    def test_opposite_left_action_mukai(self):
        """Opposite left action for Mukai flop uses its mutation matrix.

        Path 3: different geometry.
        """
        f = mukai_flop_bimodule(8)
        opp = OppositeFlop(flop=f)
        # Mukai mutation_matrix = [[-1,0],[0,1]]
        # mu((1,0)) = (-1, 0)
        from compute.lib.mutation_e1_equivalence import apply_matrix
        mu_beta = apply_matrix(f.mutation_matrix, (1, 0))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert mu_beta == (-1, 0)
        # left_action((1,0), (2,1)): mu((1,0))=(-1,0), (-1,0)+(2,1)=(1,1)
        result = opp.left_action((1, 0), (2, 1))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result == (1, 1)


# ================================================================
# SECTION 17: TENSOR PRODUCT COMPUTATION
# ================================================================

class TestTensorProductComputation:
    """Verify the tensor product M tensor_B M^{op} computation.

    AP42 applies: the naive tensor product may not give identity.
    We test what the function actually computes.
    """

    def test_tensor_product_mutation_involution(self):
        """The exchange matrix involution holds in tensor product check.

        Path 1: mu_k^2(B) = B verified within tensor product.
        """
        f = conifold_flop_bimodule(6)
        result = compute_tensor_product_image(f, 6)
        assert result['mutation_involution_on_B']

    def test_tensor_product_charges_tested(self):
        """Tensor product computation tests a positive number of charges.

        Path 2: coverage.
        """
        f = conifold_flop_bimodule(6)
        result = compute_tensor_product_image(f, 6)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert result['charges_tested'] > 0

    def test_tensor_product_mukai_mutation_involution(self):
        """Mukai tensor product: exchange matrix involution holds.

        Path 3: different geometry.
        """
        f = mukai_flop_bimodule(6)
        result = compute_tensor_product_image(f, 6)
        assert result['mutation_involution_on_B']

    def test_tensor_product_reid_mutation_involution(self):
        """Reid tensor product: exchange matrix involution holds.

        Path 3: D_4 geometry.
        """
        f = reid_flop_bimodule(6)
        result = compute_tensor_product_image(f, 6)
        assert result['mutation_involution_on_B']


# ================================================================
# SECTION 18: MULTI-PATH CROSS-VALIDATION
# ================================================================

class TestMultiPathCrossValidation:
    """Cross-validate results from independent computation paths."""

    def test_exchange_involution_three_paths(self):
        """mu_k^2 = id verified by 3 independent methods for conifold.

        Path 1: direct exchange_matrix_mutate.
        Path 2: verify_flop_flop_identity path_5.
        Path 3: compute_tensor_product_image mutation_involution.
        """
        B = [[0, 2], [-2, 0]]
        k = 1

        # Path 1
        Bp = exchange_matrix_mutate(B, k)
        Bpp = exchange_matrix_mutate(Bp, k)
        path1 = (Bpp == B)

        # Path 2
        f = conifold_flop_bimodule(6)
        r = verify_flop_flop_identity(f)
        path2 = r['path_5_exchange_involution']['mu_k_squared_is_id']

        # Path 3
        t = compute_tensor_product_image(f, 6)
        path3 = t['mutation_involution_on_B']

        assert path1 and path2 and path3, (
            f"Exchange involution: path1={path1}, path2={path2}, path3={path3}"
        )

    def test_d_squared_zero_three_components(self):
        """d^2 = 0 verified by 3 independent sub-checks.

        Path 1: left module associativity
        Path 2: right module associativity
        Path 3: bimodule axiom
        """
        f = conifold_flop_bimodule(6)
        result = bimodule_bar_differential_check(f, max_arity=3)

        assert result['left_module_associativity'], "Left assoc failed"
        assert result['right_module_associativity'], "Right assoc failed"
        assert result['bimodule_axiom'], "Bimodule axiom failed"

        # d^2 = 0 is the conjunction
        assert result['d_squared_zero']

    def test_ks_and_exchange_agree(self):
        """KS roundtrip and exchange matrix involution both confirm involution.

        Path 1: KS roundtrip K o K^{-1} = id.
        Path 2: mu_k^2(B) = B.
        Path 3: conifold euler form preserved.
        """
        ks = ks_roundtrip_verification(max_height=6)
        path1 = ks['is_identity']

        B = [[0, 2], [-2, 0]]
        Bp = exchange_matrix_mutate(B, 1)
        Bpp = exchange_matrix_mutate(Bp, 1)
        path2 = (Bpp == B)

        euler = euler_form_preservation(B, 1)
        path3 = euler['euler_form_preserved']

        assert path1 and path2 and path3, (
            f"Involution cross-check: KS={path1}, exchange={path2}, euler={path3}"
        )

    def test_four_flop_types_exchange_involution(self):
        """Exchange matrix involution holds for all 4 standard flop types.

        Multi-path: 4 independent geometries all confirm mu_k^2 = id.
        """
        geometries = {
            'conifold': ([[0, 2], [-2, 0]], 1),
            'pagoda': ([[0, 1, -1], [-1, 0, 1], [1, -1, 0]], 0),
            'mukai': ([[0, 1], [-1, 0]], 0),
            'reid': ([[0, 1, 1, 1], [-1, 0, 0, 0],
                       [-1, 0, 0, 0], [-1, 0, 0, 0]], 0),
        }
        for name, (B, k) in geometries.items():
            Bp = exchange_matrix_mutate(B, k)
            Bpp = exchange_matrix_mutate(Bp, k)
            assert Bpp == B, f"Exchange involution failed for {name}"

    def test_four_flop_types_d_squared_zero(self):
        """d^2 = 0 for all 4 standard flop types.

        Multi-path: 4 independent geometries all confirm bar complex well-defined.
        """
        for fn in [conifold_flop_bimodule, pagoda_flop_bimodule,
                   mukai_flop_bimodule, reid_flop_bimodule]:
            f = fn(6)
            result = bimodule_bar_differential_check(f, max_arity=3)
            assert result['d_squared_zero'], (
                f"d^2 != 0 for {f.name}"
            )
