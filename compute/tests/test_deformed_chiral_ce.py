"""Tests for the deformed chiral CE differential d_h on V_k(gl_1).

Verifies Construction 5.12 (constr:quantum-ce-deformation) from
chapters/theory/quantum_chiral_algebras.tex, lines 400-412:

    d_h = d_CE + h_1*partial_1 + h_2*partial_2 + h_3*partial_3

for the rank-1 Kac-Moody vertex algebra V_k(gl_1) (Heisenberg VOA)
with single generator J(z) and OPE J(z)J(w) ~ k/(z-w)^2.

Key results:
- d_CE = 0 on arity 1 (abelian Lie algebra, no first-order pole)
- d_CE([s^{-1}J_{-m}|s^{-1}J_{-n}]) = k*m*delta_{m+n,0} (commutator)
- partial_i(s^{-1}J_{-n}) = w_i(n) * (scalar) (equivariant weight)
- d_h = d_CE for diagonal CY_3 embedding (E_3 Koszul triviality)
- d_h^2 = 0 when h_1+h_2+h_3 = 0 (Calabi-Yau constraint)
- d_h != d_CE for non-diagonal embeddings (deformation is visible)

VERIFIED sources:
[C512] Construction 5.12 (quantum CE deformation)
[E2B]  compute/lib/e2_bar_complex.py: d_Y = 0 for Heisenberg (consistent)
[DC]   Direct computation of commutators and equivariant weights
[KT]   Koszul triviality: free field admits no E_3 deformation
"""

import numpy as np
import pytest

from compute.lib.deformed_chiral_ce_engine import (
    BarElement,
    BarGenerator,
    DeformedChiralCE,
    EquivariantEmbedding,
    axis_embedding,
    diagonal_embedding,
    general_embedding,
    verify_arity2_explicit,
    verify_d_CE_arity1,
    verify_d_CE_arity2,
    verify_d_h_equals_d_CE_diagonal,
    verify_d_h_nontrivial_axis,
    verify_d_h_squared_axis_violates,
    verify_d_h_squared_zero,
    verify_general_embedding_compatible,
    verify_general_embedding_incompatible,
    verify_h_constraint_violation,
)


# ---------------------------------------------------------------------------
# Bar element algebra
# ---------------------------------------------------------------------------

class TestBarElement:
    """Basic algebraic operations on bar elements."""

    def test_basis_element(self):
        e = BarElement.basis((1, 2), 3.0)
        assert e.arity == 2
        assert e.terms[(1, 2)] == 3.0

    def test_addition(self):
        e1 = BarElement.basis((1,), 2.0)
        e2 = BarElement.basis((1,), 3.0)
        s = e1 + e2
        assert abs(s.terms[(1,)] - 5.0) < 1e-15

    def test_scalar_multiplication(self):
        e = BarElement.basis((1, -1), 1.0)
        se = 3.0 * e
        assert abs(se.terms[(1, -1)] - 3.0) < 1e-15

    def test_zero(self):
        z = BarElement.zero()
        assert z.is_zero()
        assert z.arity == 0

    def test_negation(self):
        e = BarElement.basis((2,), 5.0)
        ne = -e
        assert abs(ne.terms[(2,)] + 5.0) < 1e-15

    def test_mixed_arity_addition(self):
        e1 = BarElement.basis((), 1.0)  # arity 0
        e2 = BarElement.basis((1,), 2.0)  # arity 1
        s = e1 + e2
        assert s.arity is None  # mixed


class TestBarGenerator:
    """Properties of bar generators s^{-1}J_{-n}."""

    def test_degree(self):
        g = BarGenerator(mode=1)
        assert g.degree == 1

    def test_repr(self):
        g = BarGenerator(mode=2)
        assert "J" in repr(g)
        assert "-2" in repr(g)


# ---------------------------------------------------------------------------
# d_CE: the undeformed Chevalley-Eilenberg differential
# ---------------------------------------------------------------------------

class TestCEDifferentialArity1:
    """d_CE(s^{-1}J_{-n}) = 0 for abelian gl_1."""

    def test_d_CE_arity1_all_modes(self):
        # VERIFIED: [DC] gl_1 is abelian, no Lie bracket, d_CE = 0.
        r = verify_d_CE_arity1(k=1.0)
        assert r["ok"], "d_CE should be zero on all arity-1 elements"

    @pytest.mark.parametrize("n", [-3, -2, -1, 0, 1, 2, 3])
    def test_d_CE_arity1_individual(self, n):
        eng = DeformedChiralCE(k=1.0)
        result = eng.d_CE_arity1(n)
        assert result.is_zero(), f"d_CE(s^{{-1}}J_{{-{n}}}) should be 0"


class TestCEDifferentialArity2:
    """d_CE on arity-2 bar elements encodes [J_{-m}, J_{-n}] = -k*m*delta."""

    def test_d_CE_arity2_k1(self):
        # VERIFIED: [DC] Commutator formula at k=1.
        r = verify_d_CE_arity2(k=1.0)
        assert r["ok"], f"Errors: {r['errors']}"

    def test_d_CE_arity2_k2(self):
        # VERIFIED: [DC] Commutator formula at k=2.
        r = verify_d_CE_arity2(k=2.0)
        assert r["ok"], f"Errors: {r['errors']}"

    def test_d_CE_arity2_k_half(self):
        # VERIFIED: [DC] Commutator formula at k=1/2.
        r = verify_d_CE_arity2(k=0.5)
        assert r["ok"], f"Errors: {r['errors']}"

    def test_diagonal_vanishes(self):
        """d_CE([s^{-1}J_{-m}|s^{-1}J_{-n}]) = 0 when m+n != 0."""
        eng = DeformedChiralCE(k=1.0)
        for m in range(-3, 4):
            for n in range(-3, 4):
                if m + n == 0:
                    continue
                result = eng.d_CE_arity2(m, n)
                assert result.is_zero(), f"m={m}, n={n}: should be 0"

    def test_specific_values(self):
        """Spot-check specific (m, n) pairs."""
        eng = DeformedChiralCE(k=2.0)

        # (1, -1): [J_{-1}, J_1] = -k*1 = -2, Koszul sign -> +k*m = 2
        r = eng.d_CE_arity2(1, -1)
        assert abs(r.terms.get((), 0.0) - 2.0) < 1e-12

        # (2, -2): k*m = 2*2 = 4
        r = eng.d_CE_arity2(2, -2)
        assert abs(r.terms.get((), 0.0) - 4.0) < 1e-12

        # (-1, 1): k*(-1) = -2
        r = eng.d_CE_arity2(-1, 1)
        assert abs(r.terms.get((), 0.0) - (-2.0)) < 1e-12

        # (0, 0): k*0 = 0
        r = eng.d_CE_arity2(0, 0)
        assert r.is_zero()

    def test_antisymmetry(self):
        """d_CE([a|b]) + d_CE([b|a]) = 0 (antisymmetry of Lie bracket)."""
        eng = DeformedChiralCE(k=1.0)
        for m in range(-3, 4):
            n = -m
            r1 = eng.d_CE_arity2(m, n)
            r2 = eng.d_CE_arity2(n, m)
            total = r1 + r2
            assert total.is_zero(), f"m={m}: antisymmetry fails"


class TestCEDifferentialArity3:
    """d_CE on arity-3 bar elements: B_3 -> B_1 via the Lie bracket."""

    def test_d_CE_arity3_generic_zero(self):
        """Most arity-3 triples give d_CE = 0 (no pairs summing to 0)."""
        eng = DeformedChiralCE(k=1.0)
        # (1, 2, 3): no pair sums to 0
        result = eng.d_CE_arity3(1, 2, 3)
        assert result.is_zero()

    def test_d_CE_arity3_first_pair(self):
        """(1, -1, 2): first pair sums to 0, giving -k*1 * s^{-1}J_{-2}."""
        eng = DeformedChiralCE(k=1.0)
        result = eng.d_CE_arity3(1, -1, 2)
        # mu(J_{-1}, J_1) = -k*1 = -1; coefficient = -1
        expected = BarElement.basis((2,), -1.0)
        diff = result + (-1.0) * expected
        assert diff.is_zero(), f"Got {result}, expected {expected}"

    def test_d_CE_arity3_second_pair(self):
        """(3, 1, -1): second pair sums to 0."""
        eng = DeformedChiralCE(k=1.0)
        result = eng.d_CE_arity3(3, 1, -1)
        # mu(J_{-1}, J_1) = -k*1 = -1; coefficient from bar diff = k*n = 1*1 = 1
        # -> 1 * s^{-1}J_{-3}
        expected = BarElement.basis((3,), 1.0)
        diff = result + (-1.0) * expected
        assert diff.is_zero(), f"Got {result}, expected {expected}"

    def test_d_CE_arity3_both_pairs(self):
        """(1, -1, 1): both pairs can have nontrivial brackets."""
        eng = DeformedChiralCE(k=1.0)
        result = eng.d_CE_arity3(1, -1, 1)
        # First pair (1,-1): mu = -k*1 = -1, coeff = -1, on s^{-1}J_{-1}
        # Second pair (-1,1): mu = -k*(-1) = 1, coeff = k*n = -1, on s^{-1}J_{-1}
        # Total: (-1 + (-1)) * s^{-1}J_{-1} = -2 * s^{-1}J_{-1}
        expected_coeff = result.terms.get((1,), 0.0)
        # First: -k*m = -1*1 = -1 on (p,) = (1,)
        # Second: k*n = 1*(-1) = -1 on (m,) = (1,)
        assert abs(expected_coeff - (-2.0)) < 1e-12, f"Got {expected_coeff}"


# ---------------------------------------------------------------------------
# Equivariant operators partial_i
# ---------------------------------------------------------------------------

class TestEquivariantOperators:
    """partial_i = iota_{xi_i} on bar generators."""

    def test_diagonal_weight(self):
        """Diagonal embedding: w_i(n) = n for all i."""
        emb = diagonal_embedding()
        for i in range(1, 4):
            for n in range(-3, 4):
                assert emb.weight(i, n) == n

    def test_axis_weight(self):
        """Axis-1 embedding: w_1(n) = n, w_2(n) = w_3(n) = 0."""
        emb = axis_embedding(1)
        for n in range(-3, 4):
            assert emb.weight(1, n) == n
            assert emb.weight(2, n) == 0
            assert emb.weight(3, n) == 0

    def test_general_weight(self):
        """General embedding: w_i(n) = W_i * n."""
        W = np.array([1.0, 2.0, -3.0])
        emb = general_embedding(W)
        assert emb.weight(1, 5) == 5.0
        assert emb.weight(2, 5) == 10.0
        assert emb.weight(3, 5) == -15.0

    def test_partial_i_arity1_diagonal(self):
        """partial_i(s^{-1}J_{-n}) = n * (scalar) for diagonal embedding."""
        eng = DeformedChiralCE(k=1.0, embedding=diagonal_embedding())
        for i in range(1, 4):
            for n in range(-3, 4):
                result = eng.partial_i_arity1(i, n)
                expected_coeff = float(n)
                actual_coeff = result.terms.get((), 0.0)
                assert abs(actual_coeff - expected_coeff) < 1e-12, (
                    f"partial_{i}(J_{{-{n}}}): got {actual_coeff}, expected {n}"
                )

    def test_partial_i_arity2_leibniz(self):
        """partial_i([a|b]) = w_i(m)*[b] - w_i(n)*[a] (Leibniz rule)."""
        eng = DeformedChiralCE(k=1.0, embedding=diagonal_embedding())
        m, n = 2, -3
        for i in range(1, 4):
            result = eng.partial_i_arity2(i, m, n)
            # w_i(m) = m, w_i(n) = n for diagonal
            expected = BarElement.basis((n,), float(m)) + BarElement.basis((m,), float(-n))
            diff = result + (-1.0) * expected
            assert diff.is_zero(), f"i={i}: Leibniz fails"

    def test_partial_i_arity2_axis(self):
        """Axis-1: partial_1([a|b]) = m*[b] - n*[a], partial_2 = partial_3 = 0."""
        eng = DeformedChiralCE(k=1.0, embedding=axis_embedding(1))
        m, n = 2, -3

        # partial_1 is nontrivial
        r1 = eng.partial_i_arity2(1, m, n)
        assert not r1.is_zero()

        # partial_2, partial_3 are zero
        r2 = eng.partial_i_arity2(2, m, n)
        r3 = eng.partial_i_arity2(3, m, n)
        assert r2.is_zero()
        assert r3.is_zero()

    def test_partial_i_arity3_leibniz(self):
        """partial_i([a|b|c]) = w(m)[b|c] - w(n)[a|c] + w(p)[a|b]."""
        eng = DeformedChiralCE(k=1.0, embedding=diagonal_embedding())
        m, n, p = 1, -2, 3
        for i in range(1, 4):
            result = eng.partial_i_arity3(i, m, n, p)
            # For diagonal: w_i = identity, so w(m)=m, w(n)=n, w(p)=p
            expected = (
                BarElement.basis((n, p), float(m))
                + BarElement.basis((m, p), float(-n))
                + BarElement.basis((m, n), float(p))
            )
            diff = result + (-1.0) * expected
            assert diff.is_zero(), f"i={i}: arity-3 Leibniz fails"


# ---------------------------------------------------------------------------
# E_3 Koszul triviality: d_h = d_CE for diagonal Heisenberg
# ---------------------------------------------------------------------------

class TestKoszulTriviality:
    """For diagonal embedding with h1+h2+h3=0, d_h = d_CE identically.

    This is the central structural result: the Heisenberg (free field)
    is E_3-trivial. The Omega-background deformation has no effect because
    the equivariant weights are all equal and h1+h2+h3=0 forces cancellation.
    """

    def test_koszul_triviality_basic(self):
        # VERIFIED: [KT] E_3 Koszul triviality, h = (1, -0.5, -0.5).
        r = verify_d_h_equals_d_CE_diagonal(k=1.0, h=(1.0, -0.5, -0.5))
        assert r["ok"], f"Errors: {r['errors']}"

    def test_koszul_triviality_generic_h(self):
        # VERIFIED: [KT] Generic h with h1+h2+h3=0.
        r = verify_d_h_equals_d_CE_diagonal(k=1.0, h=(0.3, -0.1, -0.2))
        assert r["ok"], f"Errors: {r['errors']}"

    def test_koszul_triviality_large_h(self):
        # VERIFIED: [KT] Large h values.
        r = verify_d_h_equals_d_CE_diagonal(k=1.0, h=(100.0, -37.5, -62.5))
        assert r["ok"], f"Errors: {r['errors']}"

    @pytest.mark.parametrize("k", [0.5, 1.0, 2.0, 5.0])
    def test_koszul_triviality_various_k(self, k):
        # VERIFIED: [KT] Independence of level k.
        r = verify_d_h_equals_d_CE_diagonal(k=k, h=(1.0, -0.3, -0.7))
        assert r["ok"], f"k={k}: errors {r['errors']}"

    def test_koszul_triviality_complex_h(self):
        # VERIFIED: [KT] Complex Omega-background parameters.
        h = (0.5 + 0.2j, -0.1 - 0.3j, -0.4 + 0.1j)
        r = verify_d_h_equals_d_CE_diagonal(k=1.0, h=h)
        assert r["ok"], f"Errors: {r['errors']}"

    def test_h_zero_trivially(self):
        """At h=0, d_h = d_CE trivially."""
        r = verify_d_h_equals_d_CE_diagonal(k=1.0, h=(0.0, 0.0, 0.0))
        assert r["ok"]


# ---------------------------------------------------------------------------
# d_h^2 = 0: the fundamental identity
# ---------------------------------------------------------------------------

class TestDhSquared:
    """d_h^2 = 0 for various embeddings and parameters."""

    def test_d_h_squared_diagonal_real(self):
        # VERIFIED: [C512] d_h^2 = 0, diagonal embedding, real h.
        r = verify_d_h_squared_zero(k=1.0, h=(1.0, -0.3, -0.7))
        assert r["ok"], f"Errors: {r['errors']}"

    def test_d_h_squared_diagonal_complex(self):
        # VERIFIED: [C512] d_h^2 = 0, diagonal embedding, complex h.
        r = verify_d_h_squared_zero(
            k=1.0, h=(0.5 + 0.1j, -0.2 - 0.1j, -0.3)
        )
        assert r["ok"], f"Errors: {r['errors']}"

    @pytest.mark.parametrize("k", [0.5, 1.0, 2.0])
    def test_d_h_squared_various_k(self, k):
        # VERIFIED: [C512] d_h^2 = 0 independent of level k.
        r = verify_d_h_squared_zero(k=k, h=(0.7, -0.2, -0.5))
        assert r["ok"], f"k={k}: errors {r['errors']}"

    def test_d_h_squared_axis_embedding(self):
        # VERIFIED: [DC] d_h^2 = 0 for axis embedding (abelian automatic).
        r = verify_d_h_squared_axis_violates(k=1.0, h=(1.0, -0.3, -0.7))
        assert r["ok"], f"Errors: {r['errors']}"

    def test_d_h_squared_general_compatible(self):
        """d_h^2 = 0 for general embedding with h . W = 0 (compatible)."""
        # VERIFIED: [DC] h . W = 0 is the necessary condition, not h1+h2+h3=0.
        W = np.array([1.0, 2.0, -3.0])
        emb = general_embedding(W)
        # h = (1, -2, -1): h.W = 1 - 4 + 3 = 0
        r = verify_d_h_squared_zero(
            k=1.0, h=(1.0, -2.0, -1.0), embedding=emb
        )
        assert r["ok"], f"Errors: {r['errors']}"

    def test_d_h_squared_general_incompatible_arity3(self):
        """d_h^2 != 0 at arity 3 for general embedding with h . W != 0.

        This is a GENUINE mathematical result: the compatibility condition
        for d_h^2 = 0 is h . W = 0, not merely h_1+h_2+h_3 = 0.
        """
        r = verify_general_embedding_incompatible(k=1.0)
        assert r["ok"], "Should see arity-2 OK but arity-3 failure"
        assert r["arity2_ok"], "Arity 2 should still be OK (abelian)"
        assert r["arity3_fails"], "Arity 3 should fail when h.W != 0"

    def test_d_h_squared_arity3_explicit(self):
        """d_h^2 = 0 on specific arity-3 elements."""
        h = (1.0, -0.3, -0.7)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=diagonal_embedding())
        for m, n, p in [(1, -1, 2), (1, 2, -3), (1, -1, 1), (0, 1, -1)]:
            result = eng.d_h_squared_arity3(m, n, p)
            assert result.is_zero(), (
                f"d_h^2 != 0 on ({m},{n},{p}): {result}"
            )

    def test_d_h_squared_cy_violation_abelian(self):
        """With h1+h2+h3 != 0, d_h^2 still = 0 for abelian gl_1."""
        # VERIFIED: [DC] Abelian algebra is special: d_h^2 = 0 regardless.
        r = verify_h_constraint_violation(k=1.0)
        assert r["ok"], "d_h^2 should be 0 even without CY constraint"


# ---------------------------------------------------------------------------
# Non-trivial deformation for non-diagonal embeddings
# ---------------------------------------------------------------------------

class TestNonDiagonalDeformation:
    """d_h != d_CE when the embedding is not diagonal."""

    def test_axis_deformation_visible(self):
        # VERIFIED: [DC] Axis embedding makes deformation visible.
        r = verify_d_h_nontrivial_axis(k=1.0, h=(1.0, -0.3, -0.7))
        assert r["ok"], "Deformation should be nontrivial for axis embedding"

    def test_axis_arity1_explicit(self):
        """For axis-1, d_h(s^{-1}J_{-n}) = h_1*n*(scalar)."""
        h = (0.5, -0.2, -0.3)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=axis_embedding(1))
        for n in range(-3, 4):
            result = eng.d_h_arity1(n)
            expected = h[0] * n  # h_1 * w_1(n) = h_1 * n
            actual = result.terms.get((), 0.0)
            assert abs(actual - expected) < 1e-12, (
                f"n={n}: got {actual}, expected {expected}"
            )

    def test_general_embedding_compatible_nontrivial(self):
        """General compatible (h.W=0) embedding: visible deformation, d_h^2=0."""
        r = verify_general_embedding_compatible(k=1.0)
        assert r["ok"]
        assert r["nontrivial_deformation"]
        assert r["d_h_squared_zero"]


# ---------------------------------------------------------------------------
# Explicit arity-2 computations
# ---------------------------------------------------------------------------

class TestArity2Explicit:
    """Detailed arity-2 computations of d_h."""

    def test_arity2_comprehensive(self):
        # VERIFIED: [DC] Comprehensive arity-2 check.
        r = verify_arity2_explicit(k=1.0)
        assert r["ok"], f"Details: {r['details']}"

    def test_diagonal_arity2_m_plus_n_nonzero(self):
        """For diagonal embedding, d_h([J_{-1}|J_{-2}]) = 0 (m+n=3 != 0)."""
        h = (1.0, -0.3, -0.7)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=diagonal_embedding())
        result = eng.d_h_arity2(1, 2)
        assert result.is_zero(), f"Should be 0, got {result}"

    def test_diagonal_arity2_m_plus_n_zero(self):
        """For diagonal embedding, d_h([J_{-2}|J_2]) = k*2 * (scalar)."""
        h = (1.0, -0.3, -0.7)
        eng = DeformedChiralCE(k=3.0, h=h, embedding=diagonal_embedding())
        result = eng.d_h_arity2(2, -2)
        expected = 3.0 * 2  # k*m = 3*2 = 6
        actual = result.terms.get((), 0.0)
        assert abs(actual - expected) < 1e-12

    def test_axis_arity2_structure(self):
        """For axis-1 embedding, d_h has both arity-0 and arity-1 components."""
        h = (1.0, -0.3, -0.7)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=axis_embedding(1))

        # d_h([J_{-1}|J_1]) should have:
        #   arity-0: k*1 = 1 (from d_CE)
        #   arity-1: h_1*(1*s^{-1}J_1 + 1*s^{-1}J_{-1}) (from partial_1)
        result = eng.d_h_arity2(1, -1)
        assert abs(result.terms.get((), 0.0) - 1.0) < 1e-12  # scalar
        assert abs(result.terms.get((-1,), 0.0) - 1.0) < 1e-12  # h_1*s^{-1}J_1
        assert abs(result.terms.get((1,), 0.0) - 1.0) < 1e-12  # h_1*s^{-1}J_{-1}

    def test_axis_arity2_off_diagonal(self):
        """For axis-1, d_h([J_{-1}|J_{-2}]) has only arity-1 terms."""
        h = (2.0, -0.5, -1.5)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=axis_embedding(1))

        # m=1, n=2, m+n=3 != 0, so d_CE = 0.
        # partial_1: h_1*(w_1(1)*s^{-1}J_{-2} - w_1(2)*s^{-1}J_{-1})
        #          = 2*(1*s^{-1}J_{-2} - 2*s^{-1}J_{-1})
        result = eng.d_h_arity2(1, 2)
        assert abs(result.terms.get((), 0.0)) < 1e-12  # no scalar
        assert abs(result.terms.get((2,), 0.0) - 2.0) < 1e-12   # h_1*1
        assert abs(result.terms.get((1,), 0.0) - (-4.0)) < 1e-12  # -h_1*2


# ---------------------------------------------------------------------------
# CY constraint and structural properties
# ---------------------------------------------------------------------------

class TestCYConstraint:
    """Properties related to the Calabi-Yau constraint h1+h2+h3=0."""

    def test_cy_satisfied(self):
        eng = DeformedChiralCE(h=(1.0, -0.3, -0.7))
        assert eng.calabi_yau_satisfied

    def test_cy_violated(self):
        eng = DeformedChiralCE(h=(1.0, 1.0, 1.0))
        assert not eng.calabi_yau_satisfied

    def test_h_sum_formula(self):
        eng = DeformedChiralCE(h=(0.5, -0.2, -0.3))
        assert abs(eng.h_sum) < 1e-15

    def test_diagonal_triviality_implies_cy(self):
        """The diagonal embedding makes d_h trivial precisely because
        all w_i are equal, and h1+h2+h3=0 forces the sum to vanish.

        Mathematically: d_h - d_CE = n*(h_1+h_2+h_3) = 0.
        """
        for n in range(-5, 6):
            eng = DeformedChiralCE(
                k=1.0,
                h=(1.0, -0.3, -0.7),
                embedding=diagonal_embedding(),
            )
            deformation = eng.d_h_arity1(n) + (-1.0) * eng.d_CE_arity1(n)
            assert deformation.is_zero()


# ---------------------------------------------------------------------------
# Consistency with e2_bar_complex.py
# ---------------------------------------------------------------------------

class TestConsistencyWithE2Bar:
    """Cross-check with the E_2 bar complex engine.

    From e2_bar_complex.py (HeisenbergOPE):
    - d_Y = 0 for Heisenberg (no Gerstenhaber bracket)
    - The E_2 structure is E_infty (symmetric braiding)
    - R-matrix is trivial

    Our d_CE = 0 on arity 1 is consistent: the Y-direction differential
    (Gerstenhaber/CE direction) is zero for the free field.
    """

    def test_arity1_zero_consistent(self):
        """d_CE = 0 on arity 1 <-> d_Y = 0 in E_2 bar complex."""
        eng = DeformedChiralCE(k=1.0)
        for n in range(-5, 6):
            assert eng.d_CE_arity1(n).is_zero()

    def test_abelian_bracket_consistent(self):
        """No first-order pole <-> vanishing chiral bracket <-> d_CE on
        arity 1 is zero. This is the same statement in three languages."""
        # The OPE J(z)J(w) ~ k/(z-w)^2 has NO (z-w)^{-1} term.
        # Therefore: mu(J, J) = 0 (chiral bracket vanishes).
        # Therefore: the Lie algebra of modes is ABELIAN modulo central ext.
        # Therefore: d_CE = 0 on single generators.
        eng = DeformedChiralCE(k=1.0)
        for n in range(-3, 4):
            assert eng.d_CE_arity1(n).is_zero()

    def test_diagonal_reduces_to_undeformed(self):
        """d_h = d_CE for diagonal embedding confirms that the Heisenberg
        E_2 bar complex sees no deformation from the Omega-background.

        This is the E_3 Koszul theorem: the free field (Heisenberg) is
        the maximally degenerate case where the E_3 structure collapses
        to E_infty.
        """
        h = (2.5, -1.0, -1.5)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=diagonal_embedding())
        for m in range(-2, 3):
            for n in range(-2, 3):
                dh = eng.d_h_arity2(m, n)
                dce = eng.d_CE_arity2(m, n)
                diff = dh + (-1.0) * dce
                assert diff.is_zero(), f"({m},{n}): d_h != d_CE"


# ---------------------------------------------------------------------------
# Edge cases and robustness
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_zero_mode(self):
        """J_0 mode: d_CE, partial_i, d_h all handle n=0 correctly."""
        eng = DeformedChiralCE(k=1.0, h=(1.0, -0.5, -0.5))
        assert eng.d_CE_arity1(0).is_zero()
        assert eng.d_h_arity1(0).is_zero()
        assert eng.d_CE_arity2(0, 0).is_zero()

    def test_k_zero(self):
        """At k=0 (degenerate level), d_CE vanishes entirely."""
        eng = DeformedChiralCE(k=0.0, h=(1.0, -0.5, -0.5))
        for m in range(-3, 4):
            for n in range(-3, 4):
                assert eng.d_CE_arity2(m, n).is_zero()

    def test_large_modes(self):
        """Computations remain valid for large mode numbers."""
        eng = DeformedChiralCE(k=1.0, h=(1.0, -0.3, -0.7))
        result = eng.d_CE_arity2(100, -100)
        assert abs(result.terms.get((), 0.0) - 100.0) < 1e-10

    def test_negative_k(self):
        """Negative level (relevant for reflected level k' = -k-2h^v)."""
        eng = DeformedChiralCE(k=-1.0)
        result = eng.d_CE_arity2(1, -1)
        assert abs(result.terms.get((), 0.0) - (-1.0)) < 1e-12


# ---------------------------------------------------------------------------
# Multi-path cross-verification (AP10)
# ---------------------------------------------------------------------------

class TestMultiPathVerification:
    """Cross-verify key results via independent computation paths.

    Each test computes the same quantity in two or more independent ways
    and checks agreement. This guards against correlated errors in the
    engine (AP10 mandate: hardcoded assertions must be cross-checked).
    """

    def test_d_CE_arity2_via_commutator_and_antisymmetry(self):
        """Path A: d_CE(m,-m) = k*m directly.
        Path B: d_CE(-m,m) = -k*m (antisymmetry) => d_CE(m,-m) + d_CE(-m,m) = 0.
        Cross-check: both paths agree with the Heisenberg commutator [J_m, J_n].
        """
        for k in [0.5, 1.0, 2.0, 3.7]:
            eng = DeformedChiralCE(k=k)
            for m in range(1, 5):
                # Path A: direct
                r_direct = eng.d_CE_arity2(m, -m)
                val_a = r_direct.terms.get((), 0.0)
                # Path B: antisymmetry
                r_anti = eng.d_CE_arity2(-m, m)
                val_b = r_anti.terms.get((), 0.0)
                # Path C: commutator formula [J_{-m}, J_m] = -k*m
                val_c = k * m  # expected from Koszul-signed bar differential
                # Cross-check A vs C
                assert abs(val_a - val_c) < 1e-12, (
                    f"k={k}, m={m}: direct {val_a} != commutator {val_c}"
                )
                # Cross-check A + B = 0 (antisymmetry)
                assert abs(val_a + val_b) < 1e-12, (
                    f"k={k}, m={m}: antisymmetry fails: {val_a} + {val_b}"
                )

    def test_d_h_arity1_three_embeddings_diagonal_sum(self):
        """The deformation on arity 1 for diagonal embedding is
        (h1+h2+h3)*n = 0. Cross-verify via three independent paths:

        Path A: compute d_h directly from the engine
        Path B: compute sum_i h_i * partial_i manually
        Path C: compute h . W * n analytically (should be 0 for diagonal)
        """
        h = (1.7, -0.3, -1.4)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=diagonal_embedding())
        for n in range(-4, 5):
            # Path A: engine
            result_a = eng.d_h_arity1(n)
            val_a = result_a.terms.get((), 0.0)
            # Path B: manual sum of partial_i
            val_b = sum(
                hi * eng.embedding.weight(i, n)
                for i, hi in enumerate([eng.h1, eng.h2, eng.h3], start=1)
            )
            # Path C: analytic (h_sum * n for diagonal)
            val_c = (h[0] + h[1] + h[2]) * n
            # All three must agree
            assert abs(val_a - val_b) < 1e-12, (
                f"n={n}: engine {val_a} != manual {val_b}"
            )
            assert abs(val_b - val_c) < 1e-12, (
                f"n={n}: manual {val_b} != analytic {val_c}"
            )

    def test_d_h_arity2_decomposition_crosscheck(self):
        """Verify d_h = d_CE + deformation by computing each piece
        independently and checking the sum.

        Path A: d_h from engine (monolithic)
        Path B: d_CE + sum_i h_i * partial_i (component-wise)
        """
        h = (0.5 + 0.1j, -0.2 - 0.3j, -0.3 + 0.2j)
        for emb_name, emb in [
            ("diagonal", diagonal_embedding()),
            ("axis-1", axis_embedding(1)),
        ]:
            eng = DeformedChiralCE(k=2.0, h=h, embedding=emb)
            for m in range(-2, 3):
                for n in range(-2, 3):
                    # Path A: monolithic
                    dh = eng.d_h_arity2(m, n)
                    # Path B: component-wise
                    dce = eng.d_CE_arity2(m, n)
                    deform = BarElement.zero()
                    for idx, hi in enumerate([eng.h1, eng.h2, eng.h3], start=1):
                        if abs(hi) >= 1e-15:
                            deform = deform + hi * eng.partial_i_arity2(idx, m, n)
                    path_b = dce + deform
                    # Compare all terms
                    all_keys = set(dh.terms.keys()) | set(path_b.terms.keys())
                    for key in all_keys:
                        va = dh.terms.get(key, 0.0)
                        vb = path_b.terms.get(key, 0.0)
                        assert abs(va - vb) < 1e-12, (
                            f"{emb_name} ({m},{n}) key={key}: "
                            f"monolithic {va} != components {vb}"
                        )

    def test_d_h_squared_two_paths_arity2(self):
        """d_h^2 on arity-2 elements via two independent paths.

        Path A: engine's d_h_squared_arity2 (applies d_h then d_h)
        Path B: manually expand d_h^2 = (d_CE + h*partial)^2
               = d_CE^2 + d_CE*h*partial + h*partial*d_CE + h^2*partial^2
               Each term computed independently.
        """
        h = (1.0, -0.3, -0.7)
        eng = DeformedChiralCE(k=1.0, h=h, embedding=diagonal_embedding())
        for m in range(-2, 3):
            for n in range(-2, 3):
                # Path A: engine
                result_a = eng.d_h_squared_arity2(m, n)
                # Path B: manual expansion
                # d_CE on arity 2 -> arity 0 (scalar). d_h on arity 0 = 0.
                # partial_i on arity 2 -> arity 1. d_CE on arity 1 = 0.
                # partial_j on arity 1 -> arity 0. So:
                # d_h^2 = sum_i h_i * d_h(partial_i(...))
                #       = sum_i h_i * [d_CE(partial_i) + sum_j h_j*partial_j(partial_i)]
                #       = sum_i h_i * sum_j h_j * partial_j(partial_i(...))
                # since d_CE on arity-1 is 0.
                result_b = BarElement.zero()
                for i, hi in enumerate([eng.h1, eng.h2, eng.h3], start=1):
                    if abs(hi) < 1e-15:
                        continue
                    pi_result = eng.partial_i_arity2(i, m, n)
                    for modes, coeff in pi_result.terms.items():
                        if abs(coeff) < 1e-15 or len(modes) != 1:
                            continue
                        # Apply d_h to this arity-1 element
                        inner = eng.d_h_arity1(modes[0])
                        result_b = result_b + (hi * coeff) * inner

                diff = result_a + (-1.0) * result_b
                assert diff.is_zero(tol=1e-11), (
                    f"({m},{n}): two-path disagreement: {diff}"
                )

    def test_koszul_triviality_via_h_dot_W(self):
        """Cross-verify E_3 Koszul triviality via the h.W inner product.

        Path A: d_h = d_CE (computed term by term)
        Path B: h . W = 0 (algebraic, from h_dot_W method)

        The mathematical theorem: d_h = d_CE for ALL elements
        iff h . W(n) = 0 for all n.
        """
        for h_vals in [
            (1.0, -0.5, -0.5),
            (3.0, 1.0, -4.0),
            (0.1 + 0.2j, -0.05 - 0.1j, -0.05 - 0.1j),
        ]:
            eng = DeformedChiralCE(k=1.0, h=h_vals, embedding=diagonal_embedding())
            # Path B: algebraic check
            h_dot_w = eng.h_dot_W(1)
            h_dot_w_zero = abs(h_dot_w) < 1e-12
            # Path A: term-by-term check
            dh_eq_dce = True
            for n in range(-3, 4):
                diff = eng.d_h_arity1(n) + (-1.0) * eng.d_CE_arity1(n)
                if not diff.is_zero():
                    dh_eq_dce = False
                    break
            # Cross-check: both paths agree
            assert h_dot_w_zero == dh_eq_dce, (
                f"h={h_vals}: h.W=0 is {h_dot_w_zero} but d_h=d_CE is {dh_eq_dce}"
            )

    def test_embedding_compatible_predicts_d_h_squared(self):
        """The embedding_compatible property correctly predicts d_h^2=0 at arity 3.

        Path A: embedding_compatible (algebraic check of h.W)
        Path B: explicit d_h^2 computation at arity 3
        """
        W = np.array([1.0, 2.0, -3.0])
        test_cases = [
            # (h, expected_compatible)
            ((1.0, -2.0, -1.0), True),   # h.W = 1 - 4 + 3 = 0
            ((0.5, -0.2, -0.3), False),   # h.W = 0.5 - 0.4 + 0.9 = 1.0
            ((3.0, 0.0, -1.0), True),     # h.W = 3 + 0 + 3 = 6... no
        ]
        # Recompute last case: h.W = 3*1 + 0*2 + (-1)*(-3) = 3 + 0 + 3 = 6.
        # Not compatible. Let's use h=(3, -3, 0): h.W = 3 - 6 + 0 = -3. No.
        # h=(6, -3, 0): h.W = 6 - 6 + 0 = 0. Yes but h1+h2+h3 = 3.
        # h=(3, 0, -1): h.W = 3 + 0 + 3 = 6. Use h=(-3, 0, 1): h.W = -3+0-3=-6.
        # Let me just use (0, 3, -2): h.W = 0 + 6 + 6 = 12. No.
        # Solve: h1 + 2*h2 - 3*h3 = 0. e.g. (5, -1, 1): 5 - 2 - 3 = 0. Yes.
        test_cases = [
            ((1.0, -2.0, -1.0), True),   # h.W = 1 - 4 + 3 = 0
            ((0.5, -0.2, -0.3), False),   # h.W = 0.5 - 0.4 + 0.9 = 1.0
            ((5.0, -1.0, 1.0), True),     # h.W = 5 - 2 - 3 = 0
        ]
        emb = general_embedding(W)
        for h_vals, expected in test_cases:
            eng = DeformedChiralCE(k=1.0, h=h_vals, embedding=emb)
            # Path A: algebraic
            compat = eng.embedding_compatible
            assert compat == expected, (
                f"h={h_vals}: embedding_compatible={compat}, expected={expected}, "
                f"h.W={eng.h_dot_W(1)}"
            )
            # Path B: explicit d_h^2 at arity 3
            if compat:
                for m, n, p in [(-1, 1, -1), (1, -1, 1), (-1, -1, 1)]:
                    result = eng.d_h_squared_arity3(m, n, p)
                    assert result.is_zero(), (
                        f"h={h_vals} ({m},{n},{p}): compatible but d_h^2 != 0"
                    )
            else:
                found_nonzero = False
                for m, n, p in [(-1, 1, -1), (1, -1, 1), (-1, -1, 1)]:
                    result = eng.d_h_squared_arity3(m, n, p)
                    if not result.is_zero():
                        found_nonzero = True
                        break
                assert found_nonzero, (
                    f"h={h_vals}: incompatible but d_h^2 = 0 on all test triples"
                )

    def test_d_CE_arity3_vs_iterated_arity2(self):
        """Cross-verify d_CE on arity 3 via two independent paths.

        Path A: d_CE_arity3 (direct formula from the bar differential)
        Path B: d_CE on arity 3 as the composition of two arity-2 operations
                d_CE([a|b|c]) = [J_{-m},J_{-n}]|c - a|[J_{-n},J_{-p}]
                computed by evaluating commutators directly.
        """
        eng = DeformedChiralCE(k=2.0)
        for m, n, p in [
            (1, -1, 2), (2, -2, 1), (1, -1, 1), (3, 1, -1), (-2, 2, -1),
        ]:
            # Path A: engine
            result_a = eng.d_CE_arity3(m, n, p)
            # Path B: manual from commutators
            # [J_{-m}, J_{-n}] = k*(-m)*delta_{m+n,0}  => bracket = -k*m
            # [J_{-n}, J_{-p}] = k*(-n)*delta_{n+p,0}  => bracket = -k*n
            result_b = BarElement.zero()
            if m + n == 0:
                # mu(a,b)|c: coefficient = -k*m (the bracket), on s^{-1}J_{-p}
                result_b = result_b + BarElement.basis((p,), -eng.k * m)
            if n + p == 0:
                # -a|mu(b,c): coefficient = -(-k*n) = k*n, on s^{-1}J_{-m}
                result_b = result_b + BarElement.basis((m,), eng.k * n)
            # Compare
            diff = result_a + (-1.0) * result_b
            assert diff.is_zero(), (
                f"({m},{n},{p}): path A = {result_a}, path B = {result_b}"
            )

    def test_k_linearity_crosscheck(self):
        """d_CE scales linearly with k. Cross-verify:
        d_CE at level 2k should equal 2 * d_CE at level k."""
        for k in [1.0, 0.5, 3.0]:
            eng_k = DeformedChiralCE(k=k)
            eng_2k = DeformedChiralCE(k=2 * k)
            for m in range(-3, 4):
                n = -m
                r_k = eng_k.d_CE_arity2(m, n)
                r_2k = eng_2k.d_CE_arity2(m, n)
                val_k = r_k.terms.get((), 0.0)
                val_2k = r_2k.terms.get((), 0.0)
                assert abs(val_2k - 2 * val_k) < 1e-12, (
                    f"k={k}, m={m}: linearity fails: "
                    f"d(2k)={val_2k} != 2*d(k)={2*val_k}"
                )
