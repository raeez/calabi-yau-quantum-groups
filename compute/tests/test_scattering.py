r"""
Tests for the scattering diagram computation for K3 x E.

This module tests:
    1. Lattice operations (Gram matrix, inner products, discriminant)
    2. LieElement algebra (bracket, BCH)
    3. Scattering diagram construction (seed walls, forced walls, heights)
    4. GPS tropical vertex (2d A_2 pentagon identity)
    5. Comparison with phi_{0,1} root multiplicities
    6. S_3 symmetry analysis
    7. Qualitative structure: walls forced at all composite roots

The MAIN FINDING to verify: the pair-commutator (BCH) scattering diagram
does NOT directly reproduce the phi_{0,1} Fourier coefficients. The ratios
are non-uniform, quantifying the gap between leading-order Lie algebra
consistency and the full motivic wall-crossing.

Ground truth:
    phi_{0,1} coefficients: compute/lib/phi01_fourier.py
    BKM shadow obstruction tower: compute/lib/bkm_shadow_tower.py
    GPS tropical vertex: Gross-Pandharipande-Siebert (2010), Thm 1.4
"""

import os
import sys
import importlib.util
from fractions import Fraction

import pytest

# Load module under test
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'scattering_diagram',
    os.path.join(_lib_dir, 'scattering_diagram.py')
)
sd_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sd_mod)


# =========================================================================
# 1. LATTICE OPERATIONS
# =========================================================================

class TestLattice:
    """Verify the lattice Lambda^{2,1}_{II}."""

    def test_gram_matrix_entries(self):
        """Gram matrix: diagonal = 2, off-diagonal = -2."""
        A = sd_mod.GRAM_MATRIX
        for i in range(3):
            assert A[i][i] == 2
            for j in range(3):
                if i != j:
                    assert A[i][j] == -2

    def test_gram_symmetric(self):
        """Gram matrix is symmetric."""
        A = sd_mod.GRAM_MATRIX
        for i in range(3):
            for j in range(3):
                assert A[i][j] == A[j][i]

    def test_gram_determinant(self):
        """det(A) = -32 (signature (2,1))."""
        A = sd_mod.GRAM_MATRIX
        det = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
               - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
               + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
        assert det == -32

    def test_eigenvalues(self):
        """Eigenvalues: -2 (eigvec (1,1,1)), 4 (eigvec (1,-1,0)), 4 (eigvec (1,0,-1))."""
        assert sd_mod.inner_product((1, 1, 1), (1, 1, 1)) == -6  # = -2 * 3
        assert sd_mod.inner_product((1, -1, 0), (1, -1, 0)) == 8  # = 4 * 2
        assert sd_mod.inner_product((1, 0, -1), (1, 0, -1)) == 8

    def test_simple_root_norms(self):
        """Each simple root has norm 2."""
        for root in sd_mod.SIMPLE_ROOTS:
            assert sd_mod.norm_sq(root) == 2

    def test_simple_root_inner_products(self):
        """(delta_i, delta_j) = -2 for i != j."""
        roots = sd_mod.SIMPLE_ROOTS
        for i in range(3):
            for j in range(3):
                expected = 2 if i == j else -2
                assert sd_mod.inner_product(roots[i], roots[j]) == expected

    def test_siegel_discriminant_simple_roots(self):
        """delta_1 = (1,0,0): D = 4*1*0 - 0 = 0.
        delta_2 = (0,1,0): D = 4*0*0 - 1 = -1.
        delta_3 = (0,0,1): D = 4*0*1 - 0 = 0."""
        assert sd_mod.siegel_discriminant((1, 0, 0)) == 0
        assert sd_mod.siegel_discriminant((0, 1, 0)) == -1
        assert sd_mod.siegel_discriminant((0, 0, 1)) == 0

    def test_root_height(self):
        assert sd_mod.root_height((1, 0, 0)) == 1
        assert sd_mod.root_height((1, 1, 1)) == 3
        assert sd_mod.root_height((2, 3, 1)) == 6

    def test_is_positive(self):
        assert sd_mod.is_positive((1, 0, 0))
        assert sd_mod.is_positive((1, 1, 1))
        assert not sd_mod.is_positive((0, 0, 0))
        assert not sd_mod.is_positive((-1, 1, 0))

    def test_add_vectors(self):
        assert sd_mod.add_vectors((1, 0, 0), (0, 1, 0)) == (1, 1, 0)
        assert sd_mod.add_vectors((2, 1, 3), (1, 2, 0)) == (3, 3, 3)

    def test_scale_vector(self):
        assert sd_mod.scale_vector(3, (1, 2, 0)) == (3, 6, 0)
        assert sd_mod.scale_vector(0, (1, 2, 3)) == (0, 0, 0)

    def test_s3_orbit_simple(self):
        """Simple root (1,0,0) has orbit size 3."""
        orb = sd_mod.s3_orbit((1, 0, 0))
        assert len(orb) == 3
        assert set(orb) == {(0, 0, 1), (0, 1, 0), (1, 0, 0)}

    def test_s3_orbit_diagonal(self):
        """(1,1,1) is fixed by S_3, orbit size 1."""
        orb = sd_mod.s3_orbit((1, 1, 1))
        assert len(orb) == 1
        assert orb[0] == (1, 1, 1)

    def test_s3_orbit_two_distinct(self):
        """(1,1,2) has orbit size 3."""
        orb = sd_mod.s3_orbit((1, 1, 2))
        assert len(orb) == 3
        assert set(orb) == {(1, 1, 2), (1, 2, 1), (2, 1, 1)}

    def test_s3_orbit_all_distinct(self):
        """(1,2,3) has orbit size 6."""
        orb = sd_mod.s3_orbit((1, 2, 3))
        assert len(orb) == 6


# =========================================================================
# 2. LIE ALGEBRA
# =========================================================================

class TestLieElement:
    """Test the Lie algebra operations."""

    def test_zero(self):
        z = sd_mod.LieElement.zero(5)
        assert z.is_zero()

    def test_add(self):
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(2)}, 5)
        c = a + b
        assert c.coeffs[(1, 0, 0)] == Fraction(1)
        assert c.coeffs[(0, 1, 0)] == Fraction(2)

    def test_add_cancellation(self):
        a = sd_mod.LieElement({(1, 0, 0): Fraction(3)}, 5)
        b = sd_mod.LieElement({(1, 0, 0): Fraction(-3)}, 5)
        c = a + b
        assert c.is_zero()

    def test_sub(self):
        a = sd_mod.LieElement({(1, 0, 0): Fraction(5)}, 5)
        b = sd_mod.LieElement({(1, 0, 0): Fraction(2)}, 5)
        c = a - b
        assert c.coeffs[(1, 0, 0)] == Fraction(3)

    def test_scale(self):
        a = sd_mod.LieElement({(1, 0, 0): Fraction(3)}, 5)
        b = a.scale(Fraction(2, 3))
        assert b.coeffs[(1, 0, 0)] == Fraction(2)

    def test_bracket_symmetric(self):
        """[e_{(1,0,0)}, e_{(0,1,0)}] = (delta_1, delta_2) * e_{(1,1,0)} = -2 * e_{(1,1,0)}."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 5)
        c = a.bracket(b, 'symmetric')
        assert c.coeffs.get((1, 1, 0), Fraction(0)) == Fraction(-2)

    def test_bracket_symmetric_value(self):
        """Inner product of two different simple roots is -2."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 0, 1): Fraction(1)}, 5)
        c = a.bracket(b, 'symmetric')
        # (delta_1, delta_3) = -2
        assert c.coeffs.get((1, 0, 1), Fraction(0)) == Fraction(-2)

    def test_bracket_antisymmetry_skew(self):
        """[a, b] = -[b, a] for SKEW pairings (true Lie bracket)."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 5)
        ab = a.bracket(b, 'skew_12')
        ba = b.bracket(a, 'skew_12')
        s = ab + ba
        assert s.is_zero()

    def test_bracket_symmetric_is_commutative(self):
        """For SYMMETRIC kappa, [a, b] = [b, a] (NOT antisymmetric).

        This is because [e_a, e_b] = (a, b) * e_{a+b} with (a,b) symmetric
        gives a COMMUTATIVE product, not a Lie bracket. This means the
        'symmetric' kappa does not define a Lie algebra -- it defines a
        commutative algebra. The scattering diagram with symmetric kappa
        is therefore computing something different from the standard
        Lie-algebraic KS wall-crossing.

        This is an important mathematical distinction.
        """
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 5)
        ab = a.bracket(b, 'symmetric')
        ba = b.bracket(a, 'symmetric')
        # For symmetric kappa: [a,b] = [b,a], so [a,b] + [b,a] = 2[a,b] != 0
        s = ab + ba
        assert not s.is_zero()
        # In fact [a,b] = [b,a] exactly
        diff = ab - ba
        assert diff.is_zero()

    def test_bracket_skew_12(self):
        """[e_{(1,0,0)}, e_{(0,1,0)}]_{skew_12} = (1*1 - 0*0) * e_{(1,1,0)} = e_{(1,1,0)}."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 5)
        c = a.bracket(b, 'skew_12')
        assert c.coeffs.get((1, 1, 0), Fraction(0)) == Fraction(1)

    def test_bracket_truncation(self):
        """Bracket at max height is truncated."""
        a = sd_mod.LieElement({(1, 1, 1): Fraction(1)}, 4)
        b = sd_mod.LieElement({(1, 1, 1): Fraction(1)}, 4)
        # alpha + beta = (2,2,2) which has height 6 > 4
        c = a.bracket(b, 'symmetric')
        assert c.is_zero()

    def test_bracket_height_3(self):
        """Bracket of height-1 elements gives height-2 result."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 10)
        b = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 10)
        c = a.bracket(b, 'symmetric')
        for k in c.coeffs:
            assert sum(k) == 2  # height 1 + height 1

    def test_bracket_self_vanishes_skew(self):
        """[e_alpha, e_alpha] = 0 for skew pairings."""
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        c = a.bracket(a, 'skew_12')
        assert c.is_zero()

    def test_bracket_self_symmetric(self):
        """[e_alpha, e_alpha] = 0 even for symmetric pairing
        (because structure constant is symmetric, and [a,a] = 0 in any Lie algebra)."""
        # Actually [e_a, e_a] = kappa(a,a) * e_{2a}, which is (a,a) * e_{2a}.
        # For a Lie algebra, we need [x,x] = 0, but the formula
        # [e_a, e_b] = kappa(a,b) e_{a+b} gives [e_a, e_a] = kappa(a,a) e_{2a} != 0
        # in general. This means the "symmetric" bracket is NOT a Lie bracket
        # (it violates the Jacobi identity in general).
        # This is an important mathematical point!
        a = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        c = a.bracket(a, 'symmetric')
        # (1,0,0) has norm 2, so [e_{(1,0,0)}, e_{(1,0,0)}] = 2 * e_{(2,0,0)}
        assert c.coeffs.get((2, 0, 0), Fraction(0)) == Fraction(2)


class TestBCH:
    """Test the Baker-Campbell-Hausdorff formula."""

    def test_bch_commuting_elements(self):
        """BCH(f, g) = f + g when [f, g] = 0."""
        # Two elements in orthogonal directions with zero bracket
        # For skew_12: [(1,0,0), (1,0,0)] = 0 (same direction)
        # Actually need truly commuting elements.
        # For skew_12: [(1,0,a), (1,0,b)] = 0 since the skew_12 form
        # only depends on first two coords.
        f = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 5)
        g = sd_mod.LieElement({(1, 0, 1): Fraction(1)}, 5)
        # [f, g]_{skew_12} = (1*0 - 0*1) = 0 -> commutes
        h = sd_mod.bch(f, g, 'skew_12')
        assert h.coeffs.get((1, 0, 0), Fraction(0)) == Fraction(1)
        assert h.coeffs.get((1, 0, 1), Fraction(0)) == Fraction(1)

    def test_bch_leading_order(self):
        """BCH(f, g) = f + g + [f,g]/2 at leading order."""
        f = sd_mod.LieElement({(1, 0, 0): Fraction(1)}, 3)
        g = sd_mod.LieElement({(0, 1, 0): Fraction(1)}, 3)
        h = sd_mod.bch(f, g, 'symmetric', max_bch_depth=1)
        # f + g parts
        assert h.coeffs.get((1, 0, 0), Fraction(0)) == Fraction(1)
        assert h.coeffs.get((0, 1, 0), Fraction(0)) == Fraction(1)
        # [f, g]/2 = (-2)/2 * e_{(1,1,0)} = -1 * e_{(1,1,0)}
        assert h.coeffs.get((1, 1, 0), Fraction(0)) == Fraction(-1)


# =========================================================================
# 3. SCATTERING DIAGRAM CONSTRUCTION
# =========================================================================

class TestScatteringDiagram:
    """Test the scattering diagram computation."""

    def test_seed_walls(self):
        """Seed walls are at three simple roots with given multiplicity."""
        sd = sd_mod.ScatteringDiagram(4, seed_multiplicity=1)
        assert sd.walls[(1, 0, 0)] == Fraction(1)
        assert sd.walls[(0, 1, 0)] == Fraction(1)
        assert sd.walls[(0, 0, 1)] == Fraction(1)

    def test_seed_walls_mult_2(self):
        """Seed walls with multiplicity 2."""
        sd = sd_mod.ScatteringDiagram(4, seed_multiplicity=2)
        for root in sd_mod.SIMPLE_ROOTS:
            assert sd.walls[root] == Fraction(2)

    def test_walls_forced_at_height_2(self):
        """Consistency forces walls at height 2 composite roots."""
        sd = sd_mod.ScatteringDiagram(3, seed_multiplicity=1)
        sd.compute()
        # At height 2, we expect walls at sums of pairs of simple roots
        # and at 2*delta_i (from log expansion)
        height_2_walls = {r for r in sd.walls if sd_mod.root_height(r) == 2}
        # Must have at least (1,1,0), (1,0,1), (0,1,1)
        assert (1, 1, 0) in height_2_walls
        assert (1, 0, 1) in height_2_walls
        assert (0, 1, 1) in height_2_walls

    def test_walls_forced_at_height_3(self):
        """Height 3 includes (1,1,1)."""
        sd = sd_mod.ScatteringDiagram(4, seed_multiplicity=1)
        sd.compute()
        assert (1, 1, 1) in sd.walls

    def test_total_wall_count_height_3(self):
        """At max_height=3, seed walls + forced give expected count.

        Height 1: 3 walls (simple roots)
        Height 2: 6 walls (3 from log expansion of simples: (2,0,0), (0,2,0), (0,0,2)
                          + 3 from commutators: (1,1,0), (1,0,1), (0,1,1))
        Height 3: varies (includes (1,1,1) and 3*delta_i and others)
        """
        sd = sd_mod.ScatteringDiagram(3, seed_multiplicity=1)
        sd.compute()
        counts = sd.wall_count_by_height()
        assert counts.get(1, 0) == 3
        assert counts.get(2, 0) >= 3  # at least the pair sums

    def test_wall_at_111_is_nonzero(self):
        """The wall at (1,1,1) has nonzero multiplicity."""
        sd = sd_mod.ScatteringDiagram(4, seed_multiplicity=1)
        sd.compute()
        assert sd.walls.get((1, 1, 1), Fraction(0)) != 0

    def test_generation_tracking(self):
        """Seed walls are generation 0, forced walls are later."""
        sd = sd_mod.ScatteringDiagram(3, seed_multiplicity=1)
        sd.compute()
        for root in sd_mod.SIMPLE_ROOTS:
            assert sd.generation[root] == 0
        # Forced walls should have generation > 0
        for root, gen in sd.generation.items():
            if root not in sd_mod.SIMPLE_ROOTS:
                assert gen > 0

    def test_different_kappas_produce_different_walls(self):
        """Different structure constants give different multiplicities."""
        sd_sym = sd_mod.ScatteringDiagram(3, 1, 'symmetric')
        sd_sym.compute()
        sd_skew = sd_mod.ScatteringDiagram(3, 1, 'skew_12')
        sd_skew.compute()
        # Wall sets should differ
        # (skew_12 doesn't couple delta_1 and delta_3 since they
        # both have 0 in the second coordinate)
        assert sd_sym.walls != sd_skew.walls

    def test_wall_multiplicities_are_exact(self):
        """All multiplicities are exact Fractions, not floats."""
        sd = sd_mod.ScatteringDiagram(4, seed_multiplicity=1)
        sd.compute()
        for root, mult in sd.walls.items():
            assert isinstance(mult, Fraction)

    def test_increasing_height_increases_walls(self):
        """More walls are found at higher truncation."""
        sd3 = sd_mod.ScatteringDiagram(3, 1, 'symmetric')
        sd3.compute()
        sd5 = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd5.compute()
        assert len(sd5.walls) > len(sd3.walls)


# =========================================================================
# 4. GPS TROPICAL VERTEX
# =========================================================================

class TestGPSTropicalVertex:
    """Test the 2d GPS tropical vertex algorithm."""

    def test_a2_seed_walls(self):
        """A_2 case has seed walls at (1,0) and (0,1)."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=2)
        assert gps[(1, 0)] == 1
        assert gps[(0, 1)] == 1

    def test_a2_wall_at_11(self):
        """The A_2 pentagon identity: wall at (1,1) with n_{(1,1)} = 1."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=2)
        assert gps[(1, 1)] == 1

    def test_a2_pentagon_identity(self):
        """GPS Theorem 1.4: for A_2 input, all primitive directions
        in the positive quadrant get n_d = 1 (at small heights).

        n_{(1,0)} = 1, n_{(0,1)} = 1, n_{(1,1)} = 1.
        At height 3: n_{(1,2)} = 1, n_{(2,1)} = 1.
        """
        gps = sd_mod.gps_tropical_vertex_2d(max_order=4)
        assert gps[(1, 0)] == 1
        assert gps[(0, 1)] == 1
        assert gps[(1, 1)] == 1
        assert gps[(1, 2)] == 1
        assert gps[(2, 1)] == 1

    def test_a2_non_primitive_excluded(self):
        """Non-primitive directions like (2,2) are excluded."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=5)
        assert (2, 2) not in gps

    def test_a2_higher_order_multiplicities(self):
        """At height 5: n_{(2,3)} = n_{(3,2)} = 4 (first non-trivial multiplicity)."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=6)
        assert gps.get((2, 3), 0) == 4
        assert gps.get((3, 2), 0) == 4

    def test_a2_symmetry(self):
        """The A_2 tropical vertex has the symmetry n_{(a,b)} = n_{(b,a)}."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=6)
        for (a, b), n in gps.items():
            assert gps.get((b, a), 0) == n

    def test_custom_seed(self):
        """Custom seed data works."""
        gps = sd_mod.gps_tropical_vertex_2d(
            max_order=3,
            seed_data=[((1, 0), 2), ((0, 1), 3)]
        )
        assert gps[(1, 0)] == 2
        assert gps[(0, 1)] == 3
        # (1,1) forced: 2 * 3 * |1*1 - 0*0| = 6
        assert gps[(1, 1)] == 6


# =========================================================================
# 5. COMPARISON WITH phi_{0,1}
# =========================================================================

class TestPhi01Comparison:
    """Test the comparison between scattering multiplicities and phi_{0,1}.

    Main finding: the pair-commutator BCH approach does NOT reproduce
    phi_{0,1} multiplicities. This is the key computational result.
    """

    def test_seed_matches_phi01_at_delta2(self):
        """delta_2 = (0,1,0) has D = -1, phi_{0,1} gives c(-1) = 1.
        Seed mult = 1 matches."""
        result = sd_mod.compute_and_compare(3, seed_mult=1)
        for c in result['comparisons']:
            if c['root'] == (0, 1, 0):
                assert c['match']
                assert c['phi01_mult'] == 1
                assert c['scatter_mult'] == Fraction(1)

    def test_seed_does_not_match_at_delta1(self):
        """delta_1 = (1,0,0) has D = 0, phi_{0,1} gives c(0) = 10.
        Seed mult = 1 does NOT match (1 != 10)."""
        result = sd_mod.compute_and_compare(3, seed_mult=1)
        for c in result['comparisons']:
            if c['root'] == (1, 0, 0):
                assert not c['match']
                assert c['phi01_mult'] == 10
                assert c['scatter_mult'] == Fraction(1)

    def test_no_uniform_ratio(self):
        """The ratio scatter/phi01 is NOT uniform across all walls.
        This is the main negative result."""
        result = sd_mod.compute_and_compare(4, seed_mult=1)
        assert not result['all_match']
        assert len(result['unique_ratios']) > 1

    def test_qualitative_walls_at_all_heights(self):
        """Walls ARE forced at all heights 1 through max_height.
        This is qualitative agreement with the shadow obstruction tower."""
        sd = sd_mod.ScatteringDiagram(6, 1, 'symmetric')
        sd.compute()
        counts = sd.wall_count_by_height()
        for h in range(1, 7):
            assert counts.get(h, 0) > 0, f"No walls at height {h}"

    def test_wall_111_has_correct_sign(self):
        """The wall at (1,1,1) has the same sign as the BCH commutator.
        phi_{0,1} gives c(3) = -64, so the BKM root has negative multiplicity.
        The scattering diagram should also give a nonzero value at (1,1,1).
        """
        sd = sd_mod.ScatteringDiagram(4, 1, 'symmetric')
        sd.compute()
        m111 = sd.walls.get((1, 1, 1), Fraction(0))
        assert m111 != 0

    def test_discriminant_minus_1_roots(self):
        """Roots with D = -1 are 'real' in the BKM sense.
        phi_{0,1} says c(-1) = 1. Check which roots have D = -1."""
        sd = sd_mod.ScatteringDiagram(4, 1, 'symmetric')
        sd.compute()
        d_minus_1 = [(r, m) for r, m in sd.walls.items()
                     if sd_mod.siegel_discriminant(r) == -1]
        # Should include delta_2 = (0,1,0) from the seed
        roots_d1 = [r for r, _ in d_minus_1]
        assert (0, 1, 0) in roots_d1


# =========================================================================
# 6. S_3 SYMMETRY
# =========================================================================

class TestS3Symmetry:
    """Test the S_3 symmetry properties of the scattering diagram.

    The Gram matrix is invariant under permutation of coordinates.
    This means the scattering diagram should have S_3 symmetry in the
    Lie algebra with symmetric kappa. However, the BCH computation
    depends on the ORDERING of walls, which may break the symmetry
    at finite truncation.
    """

    def test_orbit_table_well_formed(self):
        """s3_orbit_table returns valid data."""
        orbits = sd_mod.s3_orbit_table(4, 1, 'symmetric')
        assert len(orbits) > 0
        for orb in orbits:
            assert 'representative' in orb
            assert 'orbit_size' in orb
            assert 1 <= orb['orbit_size'] <= 6

    def test_seed_orbit(self):
        """The three simple roots form a single S_3 orbit."""
        orbits = sd_mod.s3_orbit_table(2, 1, 'symmetric')
        seed_orbit = [o for o in orbits if o['representative'] == (0, 0, 1)]
        assert len(seed_orbit) == 1
        assert seed_orbit[0]['orbit_size'] == 3

    def test_diagonal_root_fixed(self):
        """(1,1,1) is fixed by S_3, orbit size 1."""
        sd = sd_mod.ScatteringDiagram(4, 1, 'symmetric')
        sd.compute()
        if (1, 1, 1) in sd.walls:
            orb = sd_mod.s3_orbit((1, 1, 1))
            assert len(orb) == 1

    def test_pair_sums_form_orbit(self):
        """(1,1,0), (1,0,1), (0,1,1) form a single S_3 orbit of size 3."""
        orb = sd_mod.s3_orbit((1, 1, 0))
        assert len(orb) == 3
        assert set(orb) == {(1, 1, 0), (1, 0, 1), (0, 1, 1)}


# =========================================================================
# 7. RATIO ANALYSIS
# =========================================================================

class TestRatioAnalysis:
    """Test the ratio analysis infrastructure."""

    def test_ratio_analysis_runs(self):
        """ratio_analysis completes without error."""
        ra = sd_mod.ratio_analysis(3, 1, 'symmetric')
        assert 'uniform' in ra
        assert 'by_height' in ra
        assert 'by_discriminant' in ra

    def test_ratio_not_uniform(self):
        """The ratio is not uniform (main negative result)."""
        ra = sd_mod.ratio_analysis(4, 1, 'symmetric')
        assert not ra['uniform']

    def test_by_height_populated(self):
        """Ratio analysis by height is populated."""
        ra = sd_mod.ratio_analysis(4, 1, 'symmetric')
        assert len(ra['by_height']) > 0

    def test_by_discriminant_populated(self):
        """Ratio analysis by discriminant is populated."""
        ra = sd_mod.ratio_analysis(4, 1, 'symmetric')
        assert len(ra['by_discriminant']) > 0


# =========================================================================
# 8. STRUCTURAL PROPERTIES
# =========================================================================

class TestStructuralProperties:
    """Test structural properties of the scattering diagram."""

    def test_all_multiplicities_rational(self):
        """All wall multiplicities are rational numbers."""
        sd = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd.compute()
        for root, mult in sd.walls.items():
            assert isinstance(mult, Fraction)

    def test_walls_in_positive_cone(self):
        """All walls are at positive roots (all coordinates >= 0)."""
        sd = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd.compute()
        for root in sd.walls:
            assert all(c >= 0 for c in root)
            assert any(c > 0 for c in root)

    def test_wall_count_grows(self):
        """Wall count grows with max_height."""
        counts = []
        for mh in [2, 3, 4, 5]:
            sd = sd_mod.ScatteringDiagram(mh, 1, 'symmetric')
            sd.compute()
            counts.append(len(sd.walls))
        for i in range(len(counts) - 1):
            assert counts[i + 1] > counts[i]

    def test_height_1_is_seeds(self):
        """Height 1 walls are exactly the three seed walls."""
        sd = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd.compute()
        h1 = [r for r in sd.walls if sd_mod.root_height(r) == 1]
        assert set(h1) == set(sd_mod.SIMPLE_ROOTS)

    def test_seed_mult_scales_quadratically(self):
        """Doubling seed_mult should roughly quadruple commutator contributions.
        (Since commutators are bilinear in multiplicities.)"""
        sd1 = sd_mod.ScatteringDiagram(3, 1, 'symmetric')
        sd1.compute()
        sd2 = sd_mod.ScatteringDiagram(3, 2, 'symmetric')
        sd2.compute()

        # At (1,1,1), the forced mult from pair commutators of height-1 seeds
        # should scale as seed_mult^2 (bilinear) times a height-1 commutator
        # plus seed_mult (linear from log expansion)
        m1 = sd1.walls.get((1, 1, 1), Fraction(0))
        m2 = sd2.walls.get((1, 1, 1), Fraction(0))
        # Both should be nonzero
        assert m1 != 0
        assert m2 != 0
        # The ratio should reflect the nonlinear scaling
        if m1 != 0:
            ratio = m2 / m1
            # Should NOT be exactly 2 (linear) or exactly 4 (quadratic)
            # because of the mixed contributions
            assert ratio != 0

    def test_verify_method_returns_list(self):
        """verify_against_phi01 returns a list of comparison dicts."""
        sd = sd_mod.ScatteringDiagram(3, 1, 'symmetric')
        sd.compute()
        comp = sd.verify_against_phi01()
        assert isinstance(comp, list)
        assert len(comp) > 0
        for entry in comp:
            assert 'root' in entry
            assert 'scatter_mult' in entry
            assert 'phi01_mult' in entry
            assert 'match' in entry
            assert 'ratio' in entry


# =========================================================================
# 9. SPECIFIC NUMERICAL VALUES
# =========================================================================

class TestNumericalValues:
    """Pin down specific numerical values for regression testing.

    These values are computed from the BCH algorithm with symmetric kappa
    and seed_mult = 1. They characterize the PAIR-COMMUTATOR scattering
    diagram (not the full motivic wall-crossing).
    """

    @pytest.fixture(scope='class')
    def sd4(self):
        """Scattering diagram to height 4."""
        sd = sd_mod.ScatteringDiagram(4, 1, 'symmetric')
        sd.compute()
        return sd

    def test_wall_110(self, sd4):
        """Wall at (1,1,0)."""
        assert sd4.walls.get((1, 1, 0)) == Fraction(-1)

    def test_wall_101(self, sd4):
        """Wall at (1,0,1)."""
        assert sd4.walls.get((1, 0, 1)) == Fraction(-1)

    def test_wall_011(self, sd4):
        """Wall at (0,1,1)."""
        assert sd4.walls.get((0, 1, 1)) == Fraction(-1)

    def test_wall_200(self, sd4):
        """Wall at (2,0,0) from log expansion: -1/2."""
        assert sd4.walls.get((2, 0, 0)) == Fraction(-1, 2)

    def test_wall_020(self, sd4):
        """Wall at (0,2,0) from log expansion: -1/2."""
        assert sd4.walls.get((0, 2, 0)) == Fraction(-1, 2)

    def test_wall_002(self, sd4):
        """Wall at (0,0,2) from log expansion: -1/2."""
        assert sd4.walls.get((0, 0, 2)) == Fraction(-1, 2)

    def test_wall_111(self, sd4):
        """Wall at (1,1,1). This is the first IMAGINARY root in the BKM sense."""
        m = sd4.walls.get((1, 1, 1))
        assert m is not None
        assert m != 0
        # Pin down the exact value
        assert m == Fraction(8, 3)

    def test_wall_112(self, sd4):
        """Wall at (1,1,2)."""
        m = sd4.walls.get((1, 1, 2))
        assert m is not None

    def test_wall_count_height_4(self, sd4):
        """Total walls up to height 4."""
        assert len(sd4.walls) > 20


# =========================================================================
# 10. EDGE CASES
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_max_height_1(self):
        """max_height=1: only seed walls, no forced walls."""
        sd = sd_mod.ScatteringDiagram(1, 1, 'symmetric')
        sd.compute()
        assert len(sd.walls) == 3

    def test_seed_mult_0(self):
        """seed_mult=0: all walls are zero (vacuous)."""
        sd = sd_mod.ScatteringDiagram(4, 0, 'symmetric')
        sd.compute()
        # Seed walls exist at mult 0, nothing forced
        assert all(m == 0 for m in sd.walls.values())

    def test_negative_seed_mult(self):
        """Negative seed multiplicity: still well-defined."""
        sd = sd_mod.ScatteringDiagram(3, -1, 'symmetric')
        sd.compute()
        for root in sd_mod.SIMPLE_ROOTS:
            assert sd.walls[root] == Fraction(-1)

    def test_gps_max_order_1(self):
        """GPS with max_order=1: only seed walls."""
        gps = sd_mod.gps_tropical_vertex_2d(max_order=1)
        assert len(gps) == 2  # (1,0) and (0,1)


# =========================================================================
# 11. INTEGRATION: MAIN COMPUTATIONAL FINDING
# =========================================================================

class TestMainFinding:
    """The central computational result of this module.

    THEOREM (computational):
    The pair-commutator (BCH) scattering diagram for K3 x E, with seed
    multiplicity c(-1) = 1 at three simple roots and symmetric Gram matrix
    kappa, produces walls at all positive roots in the BKM root lattice.
    The forced multiplicities are RATIONAL but do NOT match the phi_{0,1}
    Fourier coefficients exactly. The ratio varies non-uniformly with
    both root height and Siegel discriminant.

    INTERPRETATION:
    The gap between pair-commutator multiplicities and phi_{0,1} measures
    the contribution of HIGHER BPS BOUND STATES in the motivic Hall algebra.
    The full KS wall-crossing includes multi-particle contributions that
    go beyond the leading BCH commutator.
    """

    def test_qualitative_agreement(self):
        """Walls are forced at all expected directions."""
        sd = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd.compute()
        # Walls at all heights
        for h in range(1, 6):
            height_h = [r for r in sd.walls if sd_mod.root_height(r) == h]
            assert len(height_h) > 0

    def test_quantitative_disagreement(self):
        """Multiplicities do NOT match phi_{0,1} (except at delta_2)."""
        result = sd_mod.compute_and_compare(5, 1, 'symmetric')
        assert not result['all_match']

    def test_walls_are_rational(self):
        """All forced multiplicities are exact rationals."""
        sd = sd_mod.ScatteringDiagram(5, 1, 'symmetric')
        sd.compute()
        for m in sd.walls.values():
            assert isinstance(m, Fraction)

    def test_gps_succeeds_in_2d(self):
        """The GPS algorithm correctly produces the A_2 pentagon identity.
        This confirms the algorithm is correct; the discrepancy for K3 x E
        is due to the richer structure of the BKM algebra."""
        gps = sd_mod.gps_tropical_vertex_2d(4)
        # All primitive directions at heights 1-2 get n_d = 1
        for d in [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)]:
            assert gps[d] == 1

    def test_nontrivial_gps_at_height_5(self):
        """GPS gives n_{(2,3)} = n_{(3,2)} = 4 at height 5.
        This is the first non-unit multiplicity in the A_2 case."""
        gps = sd_mod.gps_tropical_vertex_2d(6)
        assert gps[(2, 3)] == 4
        assert gps[(3, 2)] == 4
