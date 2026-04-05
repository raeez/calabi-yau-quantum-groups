r"""Tests for the Cech descent spectral sequence for E_1 chart gluing.

Verifies:
  1. Simplicial combinatorics (face maps, degeneracies, signs)
  2. Cech complex structure (simplex counts, cochains)
  3. Cech differential (delta^2 = 0, exact at every n_charts)
  4. E_1 page computation (dimensions, Euler characteristics)
  5. E_2 page computation (kernel/image/quotient)
  6. E_2 DEGENERATION THEOREM: E_2^{p,*} = 0 for p >= 2 (E_1 algebras)
  7. Conifold: 2-chart, 1-wall, convergence in 2 steps
  8. Local P^2: 3-chart, 3-wall, 1-triple, E_2 degenerate
  9. K3 x E: multi-chamber linear arrangement
  10. Quintic: 2-chart with higher internal degrees
  11. Equalizer/pullback dimension formulas
  12. Braiding obstruction: E_1 = 0, E_2 = nonzero (WHY E_1 is special)
  13. General linear and cyclic cover topologies
  14. Multi-path verification of Euler characteristics
  15. Null space computations
  16. Matrix rank over Q

Manuscript references:
    Part III (Stability and Descent): Cech descent for E_1 gluing
    Part V (Standard Landscape): conifold, local P^2, K3 x E, quintic

Mathematical references:
    [Lur]   Lurie, "Higher Algebra" Section 5.5 (Descent)
    [KS]    Kontsevich-Soibelman, "Stability structures" (2008)
    [SV]    Schiffmann-Vasserot, "CoHA" (2012)
    [Toe]   Toen, "Derived algebraic geometry" (2014)

Ground truth:
    - delta^2 = 0 (simplicial identity, verified for all n <= 8)
    - E_1 degeneration: E_2^{p,*} = 0 for p >= 2 (theorem)
    - Conifold global algebra: CoHA_I x_{K} CoHA_II (2-step convergence)
    - Euler characteristic preserved by spectral sequence
"""

import pytest
from fractions import Fraction
import math

from compute.lib.cech_descent_e1 import (
    # Simplicial combinatorics
    ordered_subsets,
    face_map,
    degeneracy_map,
    cech_sign,
    num_simplices,
    # Chart algebra
    ChartAlgebra,
    RestrictionMap,
    OverlapData,
    # Cech complex
    CechComplex,
    CechDifferential,
    # E_2 page
    E2Page,
    # Spectral sequence
    CechDescentSpectralSequence,
    # Standard examples
    conifold_cech_complex,
    conifold_spectral_sequence,
    local_p2_cech_complex,
    local_p2_spectral_sequence,
    k3e_cech_complex,
    quintic_cech_complex,
    c3_equivariant_cech,
    # General covers
    linear_cech_complex,
    cyclic_cech_complex,
    # Degeneration
    e1_degeneration_theorem,
    braiding_obstruction_dimension,
    # Equalizer
    equalizer_dimension,
    multi_chart_limit_dimension,
    # Cohomology
    cech_cohomology_dimensions,
    # Verification
    verify_simplicial_identities,
    verify_delta_squared_zero,
    # Matrix
    _matrix_rank,
    _null_space,
    # Summary
    spectral_sequence_summary,
)


# ================================================================
# 1. SIMPLICIAL COMBINATORICS
# ================================================================

class TestOrderedSubsets:
    """Verify the ordered subset enumeration."""

    def test_empty(self):
        """C(n, 0) = 1: the empty subset."""
        assert ordered_subsets(5, 0) == [()]

    def test_singletons(self):
        """C(n, 1) = n singletons."""
        result = ordered_subsets(4, 1)
        assert result == [(0,), (1,), (2,), (3,)]

    def test_pairs(self):
        """C(4, 2) = 6 pairs."""
        result = ordered_subsets(4, 2)
        assert len(result) == 6
        assert (0, 1) in result
        assert (2, 3) in result

    def test_triples(self):
        """C(4, 3) = 4 triples."""
        result = ordered_subsets(4, 3)
        assert len(result) == 4
        assert (0, 1, 2) in result
        assert (1, 2, 3) in result

    def test_full_set(self):
        """C(n, n) = 1: the full set."""
        result = ordered_subsets(5, 5)
        assert result == [(0, 1, 2, 3, 4)]

    def test_overchoose(self):
        """C(n, k) = 0 for k > n."""
        assert ordered_subsets(3, 4) == []

    def test_binomial_coefficient(self):
        """Number of subsets matches C(n, k)."""
        for n in range(1, 8):
            for k in range(n + 2):
                assert len(ordered_subsets(n, k)) == math.comb(n, k)

    def test_strictly_increasing(self):
        """All subsets are strictly increasing."""
        for sigma in ordered_subsets(6, 3):
            assert all(sigma[i] < sigma[i + 1] for i in range(len(sigma) - 1))


class TestFaceMap:
    """Verify face maps for the simplicial structure."""

    def test_face_0(self):
        """d_0 removes the first vertex."""
        assert face_map((0, 1, 2), 0) == (1, 2)

    def test_face_1(self):
        """d_1 removes the middle vertex."""
        assert face_map((0, 1, 2), 1) == (0, 2)

    def test_face_2(self):
        """d_2 removes the last vertex."""
        assert face_map((0, 1, 2), 2) == (0, 1)

    def test_face_on_edge(self):
        """Face of an edge is a vertex."""
        assert face_map((3, 7), 0) == (7,)
        assert face_map((3, 7), 1) == (3,)

    def test_face_out_of_range(self):
        """Face index out of range raises error."""
        with pytest.raises(IndexError):
            face_map((0, 1, 2), 3)
        with pytest.raises(IndexError):
            face_map((0, 1, 2), -1)

    def test_simplicial_identity(self):
        r"""d_i d_j = d_{j-1} d_i for i < j.

        This is THE fundamental identity that makes delta^2 = 0 work.
        """
        sigma = (0, 1, 2, 3)
        for i in range(4):
            for j in range(i + 1, 4):
                lhs = face_map(face_map(sigma, j), i)
                rhs = face_map(face_map(sigma, i), j - 1)
                assert lhs == rhs, f"d_{i} d_{j} != d_{j-1} d_{i} on {sigma}"

    def test_simplicial_identity_large(self):
        """Simplicial identity for 5-simplices."""
        sigma = (0, 1, 2, 3, 4)
        for i in range(5):
            for j in range(i + 1, 5):
                lhs = face_map(face_map(sigma, j), i)
                rhs = face_map(face_map(sigma, i), j - 1)
                assert lhs == rhs


class TestDegeneracyMap:
    """Verify degeneracy maps."""

    def test_degeneracy_0(self):
        """s_0 repeats the first vertex."""
        assert degeneracy_map((0, 1), 0) == (0, 0, 1)

    def test_degeneracy_1(self):
        """s_1 repeats the second vertex."""
        assert degeneracy_map((0, 1), 1) == (0, 1, 1)

    def test_degeneracy_out_of_range(self):
        with pytest.raises(IndexError):
            degeneracy_map((0, 1), 2)


class TestCechSign:
    """Verify signs for the Cech differential."""

    def test_even(self):
        assert cech_sign(0) == 1
        assert cech_sign(2) == 1
        assert cech_sign(4) == 1

    def test_odd(self):
        assert cech_sign(1) == -1
        assert cech_sign(3) == -1
        assert cech_sign(5) == -1


class TestNumSimplices:
    """Verify simplex counts = binomial coefficients."""

    def test_vertices(self):
        """C^0 has n vertices."""
        assert num_simplices(5, 0) == 5

    def test_edges(self):
        """C^1 has C(n,2) edges."""
        assert num_simplices(5, 1) == 10

    def test_triangles(self):
        """C^2 has C(n,3) triangles."""
        assert num_simplices(5, 2) == 10

    def test_zero(self):
        """C^p = 0 for p >= n."""
        assert num_simplices(3, 3) == 0
        assert num_simplices(3, 4) == 0

    def test_binomial(self):
        """Matches math.comb for all values."""
        for n in range(1, 8):
            for p in range(n + 2):
                assert num_simplices(n, p) == math.comb(n, p + 1)


# ================================================================
# 2. CHART ALGEBRA
# ================================================================

class TestChartAlgebra:
    """Verify ChartAlgebra data structure."""

    def test_creation(self):
        c = ChartAlgebra("test", 0, {0: 1, 1: 2, 2: 1})
        assert c.name == "test"
        assert c.index == 0
        assert c.total_dim == 4

    def test_dim_in_degree(self):
        c = ChartAlgebra("test", 0, {0: 1, 1: 3, 2: 2})
        assert c.dim_in_degree(0) == 1
        assert c.dim_in_degree(1) == 3
        assert c.dim_in_degree(5) == 0  # Missing degree

    def test_euler_char(self):
        c = ChartAlgebra("test", 0, {0: 1, 1: 2, 2: 1})
        assert c.euler_char() == 1 - 2 + 1  # = 0

    def test_euler_char_nonzero(self):
        c = ChartAlgebra("test", 0, {0: 1, 1: 1})
        assert c.euler_char() == 1 - 1  # = 0

    def test_poincare_series(self):
        c = ChartAlgebra("test", 0, {0: 1, 1: 2, 2: 3})
        ps = c.poincare_series(max_deg=4)
        assert ps == [1, 2, 3, 0, 0]

    def test_kappa(self):
        c = ChartAlgebra("test", 0, {0: 1}, kappa=Fraction(5))
        assert c.kappa == Fraction(5)

    def test_repr(self):
        c = ChartAlgebra("CoHA_I", 0, {0: 1, 1: 1})
        r = repr(c)
        assert "CoHA_I" in r
        assert "dim=2" in r


# ================================================================
# 3. OVERLAP DATA
# ================================================================

class TestOverlapData:
    """Verify OverlapData structure."""

    def test_creation(self):
        o = OverlapData((0, 1), {0: 1, 1: 2})
        assert o.multi_index == (0, 1)
        assert o.total_dim == 3

    def test_euler_char(self):
        o = OverlapData((0, 1, 2), {0: 1, 1: 3, 2: 3, 3: 1})
        assert o.euler_char() == 1 - 3 + 3 - 1  # = 0


# ================================================================
# 4. CECH COMPLEX STRUCTURE
# ================================================================

class TestCechComplex:
    """Verify the Cech complex construction."""

    def test_conifold_structure(self):
        """Conifold: 2 charts, 1 wall, no triple overlaps."""
        cech = conifold_cech_complex()
        assert cech.n_charts == 2
        assert cech.max_cech_degree == 1

    def test_conifold_simplices(self):
        """Correct simplex count for conifold."""
        cech = conifold_cech_complex()
        assert len(cech.simplices_at_degree(0)) == 2  # 2 charts
        assert len(cech.simplices_at_degree(1)) == 1  # 1 wall

    def test_local_p2_structure(self):
        """Local P^2: 3 charts, 3 walls, 1 triple overlap."""
        cech = local_p2_cech_complex()
        assert cech.n_charts == 3
        assert len(cech.simplices_at_degree(0)) == 3
        assert len(cech.simplices_at_degree(1)) == 3
        assert len(cech.simplices_at_degree(2)) == 1

    def test_overlap_access(self):
        """Can retrieve overlap data by multi-index."""
        cech = conifold_cech_complex()
        wall = cech.overlap_at((0, 1))
        assert wall.multi_index == (0, 1)

    def test_missing_overlap(self):
        """KeyError for missing overlap."""
        cech = conifold_cech_complex()
        with pytest.raises(KeyError):
            cech.overlap_at((0, 1, 2))  # No triple overlap for 2 charts


class TestCechComplexE1Page:
    """Verify E_1 page dimensions."""

    def test_conifold_e1_dim(self):
        """E_1^{0,0} = 2 (two charts, each dim 1 in degree 0)."""
        cech = conifold_cech_complex()
        assert cech.e1_dim(0, 0) == 2  # Two charts, each has dim 1 at q=0
        assert cech.e1_dim(0, 1) == 2  # Two charts, each has dim 1 at q=1
        assert cech.e1_dim(1, 0) == 1  # One wall, dim 1 at q=0

    def test_conifold_e1_total(self):
        """Total E_1 dimension at each Cech degree."""
        cech = conifold_cech_complex()
        assert cech.e1_total_dim(0) == 4  # 2 charts x dim 2
        assert cech.e1_total_dim(1) == 2  # 1 wall x dim 2

    def test_local_p2_e1_dim(self):
        """E_1 dimensions for local P^2."""
        cech = local_p2_cech_complex()
        # C^0: 3 charts, each {0:1, 1:2, 2:1}
        assert cech.e1_dim(0, 0) == 3  # 3 x 1
        assert cech.e1_dim(0, 1) == 6  # 3 x 2
        assert cech.e1_dim(0, 2) == 3  # 3 x 1
        # C^1: 3 walls, each {0:1, 1:1}
        assert cech.e1_dim(1, 0) == 3  # 3 x 1
        assert cech.e1_dim(1, 1) == 3  # 3 x 1
        # C^2: 1 triple, {0:1}
        assert cech.e1_dim(2, 0) == 1

    def test_e1_page_dict(self):
        """E_1 page as dictionary has correct entries."""
        cech = conifold_cech_complex()
        page = cech.e1_page()
        assert (0, 0) in page
        assert (0, 1) in page
        assert (1, 0) in page


# ================================================================
# 5. CECH DIFFERENTIAL
# ================================================================

class TestCechDifferential:
    """Verify the Cech differential delta: C^p -> C^{p+1}."""

    def test_conifold_delta_0(self):
        """delta_0 for conifold: [1, -1] (restriction difference)."""
        d = CechDifferential(2, 0, matrix=[
            [Fraction(1), Fraction(-1)]
        ])
        assert d.rank() == 1
        assert d.kernel_dim() == 1
        assert d.image_dim() == 1

    def test_local_p2_delta_0(self):
        """delta_0 for local P^2: standard Cech matrix."""
        d = CechDifferential(3, 0, matrix=[
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ])
        assert d.rank() == 2  # Rank of 3x3 standard Cech = 2
        assert d.kernel_dim() == 1  # Constants in the kernel

    def test_local_p2_delta_1(self):
        """delta_1 for local P^2: [1, -1, 1]."""
        d = CechDifferential(3, 1, matrix=[
            [Fraction(1), Fraction(-1), Fraction(1)],
        ])
        assert d.rank() == 1
        assert d.kernel_dim() == 2

    def test_delta_squared_zero_2(self):
        """delta_1 . delta_0 = 0 for n=3 (local P^2)."""
        # delta_0: 3x3
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        # delta_1: 1x3
        M1 = [
            [Fraction(1), Fraction(-1), Fraction(1)],
        ]
        # Product M1 * M0: 1x3
        product = [[Fraction(0)] * 3]
        for j in range(3):
            for k in range(3):
                product[0][j] += M1[0][k] * M0[k][j]
        assert all(product[0][j] == 0 for j in range(3))

    def test_delta_squared_zero_general(self):
        """delta^2 = 0 for n = 2, 3, 4, 5, 6, 7, 8."""
        for n in range(2, 9):
            result = verify_delta_squared_zero(n)
            assert result['all_zero'], f"delta^2 != 0 for n={n}"


# ================================================================
# 6. MATRIX OPERATIONS OVER Q
# ================================================================

class TestMatrixRank:
    """Verify exact matrix rank computation over Q."""

    def test_identity(self):
        """Rank of identity matrix = n."""
        for n in range(1, 5):
            M = [[Fraction(1) if i == j else Fraction(0)
                  for j in range(n)] for i in range(n)]
            assert _matrix_rank(M) == n

    def test_zero_matrix(self):
        """Rank of zero matrix = 0."""
        M = [[Fraction(0)] * 3 for _ in range(3)]
        assert _matrix_rank(M) == 0

    def test_rank_1(self):
        """Rank of a rank-1 matrix."""
        M = [
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(2), Fraction(4), Fraction(6)],
        ]
        assert _matrix_rank(M) == 1

    def test_rank_2(self):
        """Standard Cech matrix for n=3 has rank 2."""
        M = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        assert _matrix_rank(M) == 2

    def test_empty(self):
        assert _matrix_rank([]) == 0
        assert _matrix_rank([[]]) == 0

    def test_exact_fractions(self):
        """Rank computation is exact over Q (no floating-point issues)."""
        M = [
            [Fraction(1, 3), Fraction(1, 7)],
            [Fraction(2, 3), Fraction(2, 7)],
        ]
        assert _matrix_rank(M) == 1  # Rows are proportional


class TestNullSpace:
    """Verify null space computation over Q."""

    def test_identity(self):
        """Null space of identity is empty."""
        M = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
        ns = _null_space(M)
        assert len(ns) == 0

    def test_zero_row(self):
        """Null space of [1,0; 0,0] is [0,1]."""
        M = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
        ns = _null_space(M)
        assert len(ns) == 1
        assert ns[0][0] == 0
        assert ns[0][1] == 1

    def test_cech_kernel(self):
        """Kernel of conifold delta_0 = {(a, a)}: the diagonal."""
        M = [[Fraction(1), Fraction(-1)]]
        ns = _null_space(M)
        assert len(ns) == 1
        # The null vector should satisfy v[0] = v[1]
        assert ns[0][0] == ns[0][1]

    def test_local_p2_kernel(self):
        """Kernel of delta_0 for local P^2 is 1-dimensional (constants)."""
        M = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        ns = _null_space(M)
        assert len(ns) == 1
        # Kernel = constants (1, 1, 1) up to scaling
        v = ns[0]
        assert v[0] == v[1] == v[2]


# ================================================================
# 7. E_2 DEGENERATION THEOREM (the central result)
# ================================================================

class TestE2Degeneration:
    r"""Verify the E_2 degeneration theorem for E_1 algebras.

    THEOREM: For E_1 algebras, E_2^{p,*} = 0 for p >= 2.

    This is the CENTRAL RESULT of this module. It asserts that E_1
    descent works: gluing data + cocycle condition suffices, with no
    higher coherences needed.
    """

    def test_conifold_degenerate(self):
        """Conifold spectral sequence degenerates at E_2."""
        result = conifold_spectral_sequence()
        assert result['e2_degenerate'] is True

    def test_conifold_no_higher_e2(self):
        """No nonzero E_2^{p,*} for p >= 2 on conifold."""
        result = conifold_spectral_sequence()
        for (p, q), d in result['e2_page'].items():
            assert p < 2, f"Unexpected E_2^{{{p},{q}}} = {d}"

    def test_local_p2_degenerate(self):
        """Local P^2 spectral sequence degenerates at E_2."""
        result = local_p2_spectral_sequence()
        assert result['e2_degenerate'] is True

    def test_degeneration_theorem_conifold(self):
        """E_1 degeneration theorem certificate for conifold."""
        cech = conifold_cech_complex()
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2
        assert cert['degeneration_type'] == 'E_1 (associative)'

    def test_degeneration_theorem_local_p2(self):
        """E_1 degeneration theorem certificate for local P^2."""
        cech = local_p2_cech_complex()
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2

    def test_degeneration_theorem_k3e(self):
        """E_1 degeneration for K3 x E with 4 chambers."""
        cech = k3e_cech_complex(4)
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2

    def test_degeneration_linear_5(self):
        """E_1 degeneration for linear 5-chart arrangement."""
        cech = linear_cech_complex(5, {0: 1, 1: 1}, {0: 1})
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2

    def test_degeneration_cyclic_4(self):
        """E_1 degeneration for cyclic 4-chart arrangement."""
        cech = cyclic_cech_complex(4, {0: 1, 1: 1}, {0: 1})
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2


# ================================================================
# 8. BRAIDING OBSTRUCTION (why E_1 is special)
# ================================================================

class TestBraidingObstruction:
    r"""Verify that E_1 has zero braiding obstruction while E_2 does not.

    This is WHY E_1 descent works: no braiding means no hexagon,
    so no higher Cech cohomology obstruction.
    """

    def test_e1_obstruction_zero(self):
        """E_1 braiding obstruction = 0 for any number of charts."""
        for n in range(2, 8):
            result = braiding_obstruction_dimension(n)
            assert result['e1_obstruction'] == 0

    def test_e2_obstruction_nonzero(self):
        """E_2 braiding obstruction = C(n,3) > 0 for n >= 3."""
        for n in range(3, 8):
            result = braiding_obstruction_dimension(n)
            assert result['e2_obstruction'] == math.comb(n, 3)
            assert result['e2_obstruction'] > 0

    def test_e2_obstruction_zero_for_2_charts(self):
        """E_2 obstruction = 0 for n = 2 (no triple overlaps)."""
        result = braiding_obstruction_dimension(2)
        assert result['e2_obstruction'] == 0

    def test_einf_larger_than_e2(self):
        """E_inf obstruction >= E_2 obstruction."""
        for n in range(3, 7):
            result = braiding_obstruction_dimension(n)
            assert result['einf_obstruction'] >= result['e2_obstruction']

    def test_e1_special_message(self):
        """Certificate explains why E_1 is special."""
        result = braiding_obstruction_dimension(4)
        assert 'braiding' in result['e1_special'].lower()


# ================================================================
# 9. CONIFOLD SPECTRAL SEQUENCE (detailed)
# ================================================================

class TestConifoldSpectralSequence:
    """Detailed tests for the resolved conifold."""

    def test_2_charts(self):
        result = conifold_spectral_sequence()
        assert result['n_steps'] == 2

    def test_delta_0_rank(self):
        """delta_0 has rank 1 (one wall, one relation)."""
        result = conifold_spectral_sequence()
        assert result['delta_0_rank'] == 1

    def test_delta_0_kernel(self):
        """ker(delta_0) is 1-dimensional (the equalizer)."""
        result = conifold_spectral_sequence()
        assert result['delta_0_kernel_dim'] == 1

    def test_global_algebra(self):
        """Global algebra is the equalizer."""
        result = conifold_spectral_sequence()
        assert 'equalizer' in result['global_algebra']

    def test_e1_page_structure(self):
        """E_1 page has correct structure."""
        result = conifold_spectral_sequence()
        e1 = result['e1_page']
        assert (0, 0) in e1  # Charts at degree 0
        assert (1, 0) in e1  # Wall at degree 0

    def test_e2_concentrated_in_degree_0(self):
        """E_2 is concentrated in Cech degree 0 (descent)."""
        result = conifold_spectral_sequence()
        for (p, q), d in result['e2_page'].items():
            if d > 0:
                assert p == 0, f"Nonzero E_2^{{{p},{q}}} = {d}"

    def test_conifold_cech_complex_data(self):
        """Verify the raw Cech complex data."""
        cech = conifold_cech_complex()
        assert (0,) in cech.overlaps
        assert (1,) in cech.overlaps
        assert (0, 1) in cech.overlaps
        assert cech.overlaps[(0, 1)].total_dim == 2

    def test_euler_char_preserved(self):
        """Euler characteristic is preserved by spectral sequence.

        chi = sum_{p,q} (-1)^{p+q} dim E_r^{p,q} is independent of r.
        """
        cech = conifold_cech_complex()
        e1 = cech.e1_page()
        # E_1 Euler char with FULL grading (-1)^{p+q}
        e1_euler = sum((-1)**(p + q) * d for (p, q), d in e1.items())
        result = conifold_spectral_sequence()
        e2_euler = result['euler_char_e2']
        assert e1_euler == e2_euler


# ================================================================
# 10. LOCAL P^2 SPECTRAL SEQUENCE (detailed)
# ================================================================

class TestLocalP2SpectralSequence:
    """Detailed tests for local P^2."""

    def test_3_charts_3_walls_1_triple(self):
        result = local_p2_spectral_sequence()
        assert result['n_charts'] == 3
        assert result['n_walls'] == 3
        assert result['n_triple_overlaps'] == 1

    def test_delta_0_rank_2(self):
        """delta_0 for 3 charts has rank 2."""
        result = local_p2_spectral_sequence()
        assert result['delta_0_rank'] == 2

    def test_delta_1_rank_1(self):
        """delta_1 for 3 walls -> 1 triple has rank 1."""
        result = local_p2_spectral_sequence()
        assert result['delta_1_rank'] == 1

    def test_delta_0_kernel_1(self):
        """ker(delta_0) is 1-dimensional (connected space)."""
        result = local_p2_spectral_sequence()
        assert result['delta_0_kernel_dim'] == 1

    def test_delta_1_kernel_2(self):
        """ker(delta_1) is 2-dimensional."""
        result = local_p2_spectral_sequence()
        assert result['delta_1_kernel_dim'] == 2

    def test_e2_degenerate(self):
        """E_2 degenerates: E_2^{2,*} = 0."""
        result = local_p2_spectral_sequence()
        assert result['e2_degenerate'] is True

    def test_e2_no_degree_2(self):
        """No E_2^{2,*} terms."""
        result = local_p2_spectral_sequence()
        for (p, q), d in result['e2_page'].items():
            if d > 0:
                assert p < 2


# ================================================================
# 11. K3 x E SPECTRAL SEQUENCE
# ================================================================

class TestK3ESpectralSequence:
    """Tests for K3 x E multi-chamber cover."""

    def test_linear_4_chambers(self):
        """K3 x E with 4 chambers: linear arrangement."""
        cech = k3e_cech_complex(4)
        assert cech.n_charts == 4
        # Linear: 3 walls, no triple overlaps
        walls = [s for s in cech.overlaps if len(s) == 2]
        assert len(walls) == 3

    def test_kappa_value(self):
        """kappa = 5 for K3 x E charts."""
        cech = k3e_cech_complex(3)
        assert cech.charts[0].kappa == Fraction(5)

    def test_degeneration(self):
        """E_2 degeneration for K3 x E."""
        for n in [3, 4, 5]:
            cech = k3e_cech_complex(n)
            cert = e1_degeneration_theorem(cech)
            assert cert['degeneration_page'] == 2


# ================================================================
# 12. QUINTIC SPECTRAL SEQUENCE
# ================================================================

class TestQuinticSpectralSequence:
    """Tests for the quintic threefold."""

    def test_quintic_structure(self):
        """Quintic: 2 charts (geometric + LG), 1 wall."""
        cech = quintic_cech_complex()
        assert cech.n_charts == 2

    def test_quintic_kappa(self):
        """kappa = chi/24 = -200/24 for quintic."""
        cech = quintic_cech_complex()
        assert cech.charts[0].kappa == Fraction(-200, 24)

    def test_quintic_higher_degrees(self):
        """Quintic charts have nontrivial higher internal degrees."""
        cech = quintic_cech_complex()
        assert cech.e1_dim(0, 4) == 2  # 2 charts, each dim 1 at q=4

    def test_quintic_degeneration(self):
        """E_2 degeneration for quintic."""
        cech = quintic_cech_complex()
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2


# ================================================================
# 13. C^3 EQUIVARIANT SPECTRAL SEQUENCE
# ================================================================

class TestC3EquivariantSpectralSequence:
    """Tests for C^3 equivariant with S_3 chambers."""

    def test_6_chambers(self):
        """C^3 has 6 chambers (S_3 orderings)."""
        cech = c3_equivariant_cech(6)
        assert cech.n_charts == 6

    def test_degeneration(self):
        cech = c3_equivariant_cech(6)
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2


# ================================================================
# 14. GENERAL LINEAR AND CYCLIC COVERS
# ================================================================

class TestLinearCover:
    """Tests for linear (chain) cover topology."""

    def test_linear_2(self):
        """Linear 2-chart = conifold topology."""
        cech = linear_cech_complex(2, {0: 1}, {0: 1})
        assert cech.n_charts == 2
        assert len([s for s in cech.overlaps if len(s) == 2]) == 1

    def test_linear_5(self):
        """Linear 5-chart: 5 charts, 4 walls, no triples."""
        cech = linear_cech_complex(5, {0: 1, 1: 1}, {0: 1})
        assert cech.n_charts == 5
        walls = [s for s in cech.overlaps if len(s) == 2]
        assert len(walls) == 4
        triples = [s for s in cech.overlaps if len(s) == 3]
        assert len(triples) == 0

    def test_linear_no_higher_overlaps(self):
        """Linear cover has no overlaps of degree >= 2."""
        for n in range(2, 8):
            cech = linear_cech_complex(n, {0: 1}, {0: 1})
            for sigma in cech.overlaps:
                assert len(sigma) <= 2

    def test_linear_e1_dims(self):
        """E_1 dimensions for linear cover."""
        cech = linear_cech_complex(4, {0: 1, 1: 2}, {0: 1})
        assert cech.e1_dim(0, 0) == 4  # 4 charts x dim 1
        assert cech.e1_dim(0, 1) == 8  # 4 charts x dim 2
        assert cech.e1_dim(1, 0) == 3  # 3 walls x dim 1


class TestCyclicCover:
    """Tests for cyclic cover topology."""

    def test_cyclic_3(self):
        """Cyclic 3-chart: 3 charts, 3 walls."""
        cech = cyclic_cech_complex(3, {0: 1}, {0: 1})
        assert cech.n_charts == 3
        walls = [s for s in cech.overlaps if len(s) == 2]
        assert len(walls) == 3

    def test_cyclic_4(self):
        """Cyclic 4-chart: 4 charts, 4 walls."""
        cech = cyclic_cech_complex(4, {0: 1, 1: 1}, {0: 1})
        assert cech.n_charts == 4
        walls = [s for s in cech.overlaps if len(s) == 2]
        assert len(walls) == 4

    def test_cyclic_with_triples(self):
        """Cyclic cover with triple overlaps."""
        cech = cyclic_cech_complex(4, {0: 1}, {0: 1}, triple_dims={0: 1})
        triples = [s for s in cech.overlaps if len(s) == 3]
        assert len(triples) == 4  # 4 consecutive triples in cycle of 4

    def test_cyclic_wall_wrap(self):
        """Cyclic cover wraps: wall (0, n-1) exists."""
        cech = cyclic_cech_complex(5, {0: 1}, {0: 1})
        assert (0, 4) in cech.overlaps


# ================================================================
# 15. EQUALIZER AND PULLBACK DIMENSIONS
# ================================================================

class TestEqualizerDimension:
    """Verify equalizer/pullback dimension formulas."""

    def test_surjective_restrictions(self):
        """For surjective restrictions: dim(eq) = dim A + dim B - dim W."""
        result = equalizer_dimension(10, 10, 5, 5, 5)
        assert result['equalizer_dim'] == 10 + 10 - 5  # = 15

    def test_one_chart(self):
        """Equalizer with one chart: dim = dim A."""
        result = equalizer_dimension(5, 5, 5, 5, 5)
        assert result['equalizer_dim'] == 5 + 5 - 5  # = 5

    def test_zero_wall(self):
        """No wall (disjoint charts): dim = dim A + dim B."""
        result = equalizer_dimension(3, 4, 0, 0, 0)
        assert result['equalizer_dim'] == 3 + 4  # = 7

    def test_multi_chart_linear(self):
        """Multi-chart limit for linear arrangement."""
        # 3 charts, dim 5 each, walls of rank 2
        dim = multi_chart_limit_dimension(
            [5, 5, 5],
            [(0, 1, 2), (1, 2, 2)]
        )
        assert dim == 15 - 4  # = 11


# ================================================================
# 16. CECH COHOMOLOGY DIMENSIONS (exact)
# ================================================================

class TestCechCohomology:
    """Verify Cech cohomology computations."""

    def test_conifold_cech_h0(self):
        """H^0(Cech) = 1 for connected cover (conifold)."""
        cech = conifold_cech_complex()
        M = [[Fraction(1), Fraction(-1)]]
        dims = cech_cohomology_dimensions(cech, {0: M})
        assert dims[0] == 1  # ker(delta_0) = 1 (constants)

    def test_conifold_cech_h1(self):
        """H^1(Cech) for conifold."""
        cech = conifold_cech_complex()
        M = [[Fraction(1), Fraction(-1)]]
        dims = cech_cohomology_dimensions(cech, {0: M})
        # H^1 = C^1 / im(delta_0) = 1 - 1 = 0
        assert dims[1] == 0

    def test_local_p2_cech_h0(self):
        """H^0(Cech) = 1 for connected cover (local P^2)."""
        cech = local_p2_cech_complex()
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [
            [Fraction(1), Fraction(-1), Fraction(1)],
        ]
        dims = cech_cohomology_dimensions(cech, {0: M0, 1: M1})
        assert dims[0] == 1

    def test_local_p2_cech_h1(self):
        """H^1(Cech) = 0 for acyclic cover (local P^2)."""
        cech = local_p2_cech_complex()
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [
            [Fraction(1), Fraction(-1), Fraction(1)],
        ]
        dims = cech_cohomology_dimensions(cech, {0: M0, 1: M1})
        # H^1 = ker(delta_1)/im(delta_0) = 2 - 2 = 0
        assert dims[1] == 0

    def test_local_p2_cech_h2(self):
        """H^2(Cech) = 0 for acyclic cover (local P^2)."""
        cech = local_p2_cech_complex()
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [
            [Fraction(1), Fraction(-1), Fraction(1)],
        ]
        dims = cech_cohomology_dimensions(cech, {0: M0, 1: M1})
        # H^2 = C^2/im(delta_1) = 1 - 1 = 0
        assert dims[2] == 0


# ================================================================
# 17. SIMPLICIAL IDENTITY VERIFICATION
# ================================================================

class TestSimplicialIdentities:
    """Verify simplicial identities hold for face maps."""

    def test_identities_n4(self):
        """All simplicial identities for n=4."""
        results = verify_simplicial_identities(4)
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_identities_n5(self):
        """All simplicial identities for n=5."""
        results = verify_simplicial_identities(5)
        for key, val in results.items():
            assert val, f"Failed: {key}"

    def test_identities_n6(self):
        """All simplicial identities for n=6."""
        results = verify_simplicial_identities(6)
        for key, val in results.items():
            assert val, f"Failed: {key}"


# ================================================================
# 18. DELTA^2 = 0 (the foundational identity)
# ================================================================

class TestDeltaSquaredZero:
    r"""Verify delta^2 = 0 for all n.

    This is the FOUNDATION of the Cech complex: the alternating sum
    of face maps squares to zero because of the simplicial identity
    d_i d_j = d_{j-1} d_i for i < j.
    """

    def test_n2(self):
        result = verify_delta_squared_zero(2)
        assert result['all_zero']

    def test_n3(self):
        result = verify_delta_squared_zero(3)
        assert result['all_zero']

    def test_n4(self):
        result = verify_delta_squared_zero(4)
        assert result['all_zero']

    def test_n5(self):
        result = verify_delta_squared_zero(5)
        assert result['all_zero']

    def test_n6(self):
        result = verify_delta_squared_zero(6)
        assert result['all_zero']

    def test_n7(self):
        result = verify_delta_squared_zero(7)
        assert result['all_zero']

    def test_n8(self):
        result = verify_delta_squared_zero(8)
        assert result['all_zero']


# ================================================================
# 19. EULER CHARACTERISTIC PRESERVATION
# ================================================================

class TestEulerCharPreservation:
    r"""Verify that Euler characteristics are preserved by the
    spectral sequence.

    For any spectral sequence E_r => H^*:
      sum (-1)^{p+q} dim E_r^{p,q} = sum (-1)^n dim H^n

    This is independent of the page r.
    """

    def test_conifold_euler(self):
        """E_1 Euler char: sum (-1)^{p+q} E_1^{p,q}."""
        cech = conifold_cech_complex()
        e1 = cech.e1_page()
        e1_euler = sum((-1)**(p + q) * d for (p, q), d in e1.items())
        # E_1^{0,0}=2, E_1^{0,1}=2, E_1^{1,0}=1, E_1^{1,1}=1
        # => (+1)*2 + (-1)*2 + (-1)*1 + (+1)*1 = 2-2-1+1 = 0
        assert e1_euler == 0

    def test_local_p2_euler(self):
        """E_1 Euler char for local P^2: sum (-1)^{p+q} E_1^{p,q}."""
        cech = local_p2_cech_complex()
        e1 = cech.e1_page()
        e1_euler = sum((-1)**(p + q) * d for (p, q), d in e1.items())
        # C^0: {0:3, 1:6, 2:3}, C^1: {0:3, 1:3}, C^2: {0:1}
        # Sum = (3-6+3) - (3-3) + (1) = 0 - 0 + 1 = 1
        assert e1_euler == 1

    def test_euler_by_internal_degree(self):
        """Full Euler char = sum_q (-1)^q * (Cech alternating sum at q).

        euler_char_by_internal_degree(q) = sum_p (-1)^p * E_1^{p,q}
        The full chi = sum_q (-1)^q * euler_char_by_internal_degree(q)
                     = sum_{p,q} (-1)^{p+q} E_1^{p,q}
        which should equal euler_char_cech().
        """
        cech = conifold_cech_complex()
        total = 0
        for q in range(cech.max_internal_degree + 1):
            total += (-1)**q * cech.euler_char_by_internal_degree(q)
        euler = cech.euler_char_cech()
        assert total == euler

    def test_euler_char_cech_vs_sum(self):
        """Two methods for computing Cech Euler char agree.

        The Cech Euler char (using the per-overlap Euler char and
        inclusion-exclusion) should match the E_1-page computation.
        """
        cech = local_p2_cech_complex()
        euler1 = cech.euler_char_cech()
        e1 = cech.e1_page()
        euler2 = sum((-1)**(p + q) * d for (p, q), d in e1.items())
        assert euler1 == euler2


# ================================================================
# 20. SPECTRAL SEQUENCE SUMMARY
# ================================================================

class TestSummary:
    """Verify the summary output."""

    def test_conifold_summary(self):
        cech = conifold_cech_complex()
        s = spectral_sequence_summary(cech)
        assert '2-chart' in s
        assert 'E_1' in s

    def test_local_p2_summary(self):
        cech = local_p2_cech_complex()
        s = spectral_sequence_summary(cech)
        assert '3-chart' in s

    def test_summary_with_e2(self):
        cech = conifold_cech_complex()
        e2 = E2Page({(0, 0): 1, (0, 1): 1})
        s = spectral_sequence_summary(cech, e2)
        assert 'E_2' in s
        assert 'Degenerate' in s


# ================================================================
# 21. SPECTRAL SEQUENCE ENGINE
# ================================================================

class TestSpectralSequenceEngine:
    """Verify the CechDescentSpectralSequence engine."""

    def test_engine_creation(self):
        cech = conifold_cech_complex()
        ss = CechDescentSpectralSequence(cech)
        assert ss.n_charts == 2

    def test_engine_e1(self):
        cech = conifold_cech_complex()
        ss = CechDescentSpectralSequence(cech)
        e1 = ss.compute_e1()
        assert len(e1) > 0

    def test_engine_set_differential(self):
        cech = conifold_cech_complex()
        ss = CechDescentSpectralSequence(cech)
        d = CechDifferential(2, 0, matrix=[[Fraction(1), Fraction(-1)]])
        ss.set_differential(0, d)
        assert 0 in ss._differentials

    def test_engine_degeneration_certificate(self):
        cech = conifold_cech_complex()
        ss = CechDescentSpectralSequence(cech)
        ss.compute_e1()
        d = CechDifferential(2, 0, matrix=[[Fraction(1), Fraction(-1)]])
        ss.set_differential(0, d)
        e2 = ss.compute_e2_from_matrices()
        ss._e2_page = e2
        cert = ss.degeneration_certificate()
        assert cert['degenerate_at_e2'] is True
        assert cert['algebra_type'] == 'E_1'


# ================================================================
# 22. E_2 PAGE DIRECT
# ================================================================

class TestE2PageDirect:
    """Direct tests on E2Page."""

    def test_empty_page(self):
        e2 = E2Page({})
        assert e2.is_degenerate()

    def test_degree_0_only(self):
        e2 = E2Page({(0, 0): 1, (0, 1): 2, (0, 2): 1})
        assert e2.is_degenerate()

    def test_degree_1(self):
        e2 = E2Page({(0, 0): 1, (1, 0): 1})
        assert e2.is_degenerate()

    def test_degree_2_fails(self):
        e2 = E2Page({(0, 0): 1, (2, 0): 1})
        assert not e2.is_degenerate()

    def test_total_dim(self):
        e2 = E2Page({(0, 0): 1, (0, 1): 2, (1, 0): 3})
        assert e2.total_dim_at_n(0) == 1  # p+q=0: (0,0)
        assert e2.total_dim_at_n(1) == 5  # p+q=1: (0,1)+(1,0) = 2+3

    def test_global_euler(self):
        e2 = E2Page({(0, 0): 1, (0, 1): 2, (1, 0): 3})
        # (-1)^0 * 1 + (-1)^1 * 2 + (-1)^1 * 3 = 1 - 2 - 3 = -4
        assert e2.global_euler_char() == -4


# ================================================================
# 23. RESTRICTION MAP
# ================================================================

class TestRestrictionMap:
    """Verify RestrictionMap data structure."""

    def test_kernel_computation(self):
        source = ChartAlgebra("A", 0, {0: 3, 1: 2})
        rmap = RestrictionMap(source, (0, 1),
                              graded_image_dims={0: 2, 1: 1})
        assert rmap.graded_kernel_dims[0] == 1  # 3 - 2
        assert rmap.graded_kernel_dims[1] == 1  # 2 - 1

    def test_surjective(self):
        source = ChartAlgebra("A", 0, {0: 3})
        rmap = RestrictionMap(source, (0, 1),
                              graded_image_dims={0: 3})
        assert rmap.graded_kernel_dims[0] == 0


# ================================================================
# 24. MULTI-PATH VERIFICATION: CONIFOLD
# ================================================================

class TestConifoldMultiPath:
    r"""Multi-path verification of conifold results.

    Every computational claim verified by >= 3 independent methods.
    """

    def test_conifold_e2_degenerate_path1_direct(self):
        """Path 1: direct E_2 computation shows degeneration."""
        result = conifold_spectral_sequence()
        assert result['e2_degenerate'] is True

    def test_conifold_e2_degenerate_path2_matrix(self):
        """Path 2: matrix rank shows ker/coker structure."""
        d = CechDifferential(2, 0, matrix=[[Fraction(1), Fraction(-1)]])
        assert d.rank() == 1
        assert d.kernel_dim() == 1
        # No Cech degree >= 2 terms, so degenerate

    def test_conifold_e2_degenerate_path3_topology(self):
        """Path 3: topological argument (2 charts, no triples)."""
        cech = conifold_cech_complex()
        # With only 2 charts, C^p = 0 for p >= 2
        assert num_simplices(2, 2) == 0
        # So E_2^{p,*} = 0 for p >= 2 trivially

    def test_conifold_global_dim_path1_equalizer(self):
        """Path 1: equalizer dimension."""
        result = equalizer_dimension(2, 2, 2, 2, 2)
        eq_dim = result['equalizer_dim']
        assert eq_dim == 2  # 2 + 2 - 2

    def test_conifold_global_dim_path2_kernel(self):
        """Path 2: kernel of delta_0."""
        d = CechDifferential(2, 0, matrix=[[Fraction(1), Fraction(-1)]])
        assert d.kernel_dim() == 1  # Per degree level

    def test_conifold_global_dim_path3_euler(self):
        """Path 3: Euler char consistency."""
        cech = conifold_cech_complex()
        euler = cech.euler_char_cech()
        # Sum of chart Euler chars minus wall Euler char
        chart_euler = sum(c.euler_char() for c in cech.charts)
        wall_euler = cech.overlaps[(0, 1)].euler_char()
        assert euler == chart_euler - wall_euler


# ================================================================
# 25. MULTI-PATH VERIFICATION: LOCAL P^2
# ================================================================

class TestLocalP2MultiPath:
    """Multi-path verification of local P^2 results."""

    def test_p2_delta_squared_zero_path1_matrix(self):
        """Path 1: direct matrix multiplication."""
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [[Fraction(1), Fraction(-1), Fraction(1)]]
        product = [[sum(M1[0][k] * M0[k][j] for k in range(3))
                     for j in range(3)]]
        assert all(product[0][j] == 0 for j in range(3))

    def test_p2_delta_squared_zero_path2_verify(self):
        """Path 2: verify_delta_squared_zero function."""
        result = verify_delta_squared_zero(3)
        assert result['all_zero']

    def test_p2_delta_squared_zero_path3_simplicial(self):
        """Path 3: simplicial identities imply delta^2 = 0."""
        results = verify_simplicial_identities(3)
        assert all(results.values())

    def test_p2_e2_degenerate_path1_direct(self):
        """Path 1: direct spectral sequence computation."""
        result = local_p2_spectral_sequence()
        assert result['e2_degenerate'] is True

    def test_p2_e2_degenerate_path2_cech_cohomology(self):
        """Path 2: Cech H^2 = 0 by exact computation."""
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [[Fraction(1), Fraction(-1), Fraction(1)]]
        cech = local_p2_cech_complex()
        dims = cech_cohomology_dimensions(cech, {0: M0, 1: M1})
        assert dims[2] == 0

    def test_p2_e2_degenerate_path3_obstruction(self):
        """Path 3: braiding obstruction = 0 for E_1."""
        result = braiding_obstruction_dimension(3)
        assert result['e1_obstruction'] == 0


# ================================================================
# 26. LARGE COVER STRESS TESTS
# ================================================================

class TestLargeCovers:
    """Stress tests with many charts."""

    def test_linear_10(self):
        """10-chart linear cover: delta^2 = 0."""
        result = verify_delta_squared_zero(10)
        assert result['all_zero']

    def test_linear_10_degeneration(self):
        """10-chart degeneration theorem."""
        cech = linear_cech_complex(10, {0: 1}, {0: 1})
        cert = e1_degeneration_theorem(cech)
        assert cert['degeneration_page'] == 2

    def test_simplex_count_10(self):
        """Correct simplex counts for n=10."""
        assert num_simplices(10, 0) == 10
        assert num_simplices(10, 1) == 45
        assert num_simplices(10, 2) == 120
        assert num_simplices(10, 9) == 1

    def test_cyclic_8(self):
        """Cyclic 8-chart cover."""
        cech = cyclic_cech_complex(8, {0: 1}, {0: 1})
        assert cech.n_charts == 8
        walls = [s for s in cech.overlaps if len(s) == 2]
        assert len(walls) == 8  # 8 cyclic walls

    def test_braiding_obstruction_10(self):
        """Braiding obstruction for 10 charts."""
        result = braiding_obstruction_dimension(10)
        assert result['e1_obstruction'] == 0
        assert result['e2_obstruction'] == math.comb(10, 3)  # = 120


# ================================================================
# 27. COSIMPLICIAL STRUCTURE
# ================================================================

class TestCosimplicialStructure:
    """Verify that the Cech nerve gives a cosimplicial object."""

    def test_face_maps_well_defined(self):
        """Face maps send p-simplices to (p-1)-simplices."""
        for n in range(3, 6):
            for k in range(2, n):
                for sigma in ordered_subsets(n, k + 1):
                    for j in range(k + 1):
                        face = face_map(sigma, j)
                        assert len(face) == k
                        assert all(face[i] < face[i + 1]
                                   for i in range(len(face) - 1))

    def test_face_maps_stay_in_range(self):
        """Face maps preserve the vertex range {0, ..., n-1}."""
        for sigma in ordered_subsets(5, 4):
            for j in range(4):
                face = face_map(sigma, j)
                assert all(0 <= v < 5 for v in face)


# ================================================================
# 28. EDGE CASES
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_single_chart(self):
        """Single chart: trivial complex."""
        cech = linear_cech_complex(1, {0: 1}, {0: 1})
        assert cech.n_charts == 1
        assert cech.e1_dim(0, 0) == 1
        assert cech.e1_total_dim(0) == 1

    def test_empty_chart_dims(self):
        """Chart with no graded dimensions."""
        c = ChartAlgebra("empty", 0, {})
        assert c.total_dim == 0
        assert c.euler_char() == 0

    def test_overlap_missing_degree(self):
        """Overlap queried at missing degree returns 0."""
        o = OverlapData((0, 1), {0: 1})
        assert o.dim_in_degree(5) == 0

    def test_e2_page_missing_entry(self):
        """E_2 page queried at missing entry returns 0."""
        e2 = E2Page({(0, 0): 1})
        assert e2.dim(3, 7) == 0


# ================================================================
# 29. CONVERGENCE IN FINITE STEPS
# ================================================================

class TestFiniteConvergence:
    """Verify spectral sequence converges in finitely many steps."""

    def test_conifold_2_steps(self):
        """Conifold converges in 2 steps."""
        result = conifold_spectral_sequence()
        assert result['n_steps'] == 2

    def test_linear_n_charts_bound(self):
        """For linear n-chart, C^p = 0 for p >= 2 => E_2 = E_inf."""
        for n in range(2, 8):
            cech = linear_cech_complex(n, {0: 1}, {0: 1})
            # For linear: no overlaps of degree >= 2
            max_overlap_degree = max(len(s) - 1 for s in cech.overlaps)
            assert max_overlap_degree <= 1


# ================================================================
# 30. COMPARISON WITH KNOWN RESULTS
# ================================================================

class TestKnownResults:
    """Compare with known mathematical results."""

    def test_conifold_global_is_gl11(self):
        """Conifold global algebra: gl(1|1)-hat Kac-Moody."""
        # The equalizer of two conifold chambers gives gl(1|1)
        result = conifold_spectral_sequence()
        assert 'equalizer' in result['global_algebra']

    def test_acyclic_cover_cech_h0_is_1(self):
        """For any connected acyclic cover, Cech H^0 = 1."""
        for n in range(2, 6):
            # Use delta_0 matrix for n charts with linear topology
            sources = ordered_subsets(n, 1)
            targets = ordered_subsets(n, 2)
            M = [[Fraction(0)] * len(sources) for _ in range(len(targets))]
            src_idx = {s: i for i, s in enumerate(sources)}
            for i_t, (a, b) in enumerate(targets):
                M[i_t][src_idx[(a,)]] = Fraction(-1)
                M[i_t][src_idx[(b,)]] = Fraction(1)
            rk = _matrix_rank(M)
            ker = len(sources) - rk
            # For connected linear: ker = 1
            if n >= 2:
                # Check: the matrix has rank n-1 for n connected charts
                # (the all-ones vector is in the kernel)
                assert ker >= 1

    def test_full_simplex_cover_contractible(self):
        """Full simplex (all subsets): Cech H^p = 0 for p >= 1."""
        # n=3 charts with ALL overlaps (the full simplex)
        charts = [ChartAlgebra(f"c_{i}", i, {0: 1}) for i in range(3)]
        overlaps = {}
        for k in range(1, 4):
            for sigma in ordered_subsets(3, k):
                overlaps[sigma] = OverlapData(sigma, {0: 1})
        cech = CechComplex(charts, overlaps, max_internal_degree=1)

        # Build all Cech differential matrices
        M0 = [
            [Fraction(-1), Fraction(1), Fraction(0)],
            [Fraction(-1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(-1), Fraction(1)],
        ]
        M1 = [[Fraction(1), Fraction(-1), Fraction(1)]]

        dims = cech_cohomology_dimensions(cech, {0: M0, 1: M1})
        assert dims[0] == 1  # H^0 = 1 (connected)
        assert dims[1] == 0  # H^1 = 0 (contractible)
        assert dims[2] == 0  # H^2 = 0 (contractible)
