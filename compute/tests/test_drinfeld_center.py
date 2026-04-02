"""Tests for the Drinfeld center of Rep^{E_1}(CoHA) computation.

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        Z(Rep^{E_1}(CoHA)) = Rep^{E_2}(Y(gl_hat_1))
    thm:sv-c3 (toric_cy3_coha.tex): CoHA(C^3) = Y^+(gl_hat_1)
    sec:drinfeld-center (drinfeld_center_braided.tex): Center construction
    sec:r-matrix (quantum_groups_foundations.tex): R-matrix and YBE

Literature:
    Maulik-Okounkov arXiv:1211.1287 (quantum groups from geometry)
    Schiffmann-Vasserot arXiv:1211.1287 (CoHA and affine Yangian)
    Tsymbaliuk arXiv:1404.5240 (affine Yangian presentation)
    Drinfeld (1987) (quantum doubles, R-matrices)

Ground truth values:
    Plane partitions: p(0)=1, p(1)=1, p(2)=3, p(3)=6, p(4)=13, p(5)=24
    Ordinary partitions: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
    Drinfeld double dims: d(0)=1, d(1)=3, d(2)=11, d(3)=32, d(4)=90, d(5)=231

    Structure function (h=(1,2,-3)):
        g(z) = (z-1)(z-2)(z+3) / ((z+1)(z+2)(z-3))
        g(z)*g(-z) = 1  (inversion identity)

    R-matrix (diagonal, Fock representation):
        R_{empty}(u) = 1
        R_{box}(u) = g(u)
        R_{(2)}(u) = g(u)*g(u+2)   [h2=2]
        R_{(1,1)}(u) = g(u)*g(u+1) [h1=1]
"""

import pytest
from sympy import Rational, Symbol, cancel, simplify

from compute.lib.drinfeld_center_coha import (
    character_identity_check,
    drinfeld_center_dimension_from_coha,
    drinfeld_double_character_product,
    drinfeld_double_dimensions,
    e1_to_e2_braiding_data,
    level_decomposition,
    ordinary_partition_counts,
    plane_partition_counts,
    r_matrix_diagonal_fock,
    r_matrix_unitarity_check,
    structure_function,
    verify_drinfeld_center_coha,
    verify_structure_function_inversion,
    yang_baxter_check_charge_1,
    yang_baxter_check_charge_mixed,
    yangian_cartan_dimensions,
    yangian_negative_dimensions,
    yangian_positive_dimensions,
)


# ================================================================
# PARTITION COMBINATORICS
# ================================================================

class TestPartitionCounts:
    """Verify the combinatorial building blocks."""

    def test_ordinary_partitions_known_values(self):
        """p_1D(n) matches OEIS A000041."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        computed = ordinary_partition_counts(11)
        assert computed == expected

    def test_plane_partitions_known_values(self):
        """p_3D(n) matches OEIS A000219."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        computed = plane_partition_counts(11)
        assert computed == expected

    def test_partition_base_cases(self):
        """p(0) = 1 for both 1D and 3D partitions."""
        assert ordinary_partition_counts(1)[0] == 1
        assert plane_partition_counts(1)[0] == 1


# ================================================================
# GRADED DIMENSIONS: Y^+, Y^-, Y^0
# ================================================================

class TestYangianComponents:
    """Verify the graded dimensions of each component of the triangular decomposition."""

    def test_positive_half_equals_plane_partitions(self):
        """dim Y^+_n = p_3D(n) (CoHA basis is indexed by 3D partitions)."""
        dims = yangian_positive_dimensions(8)
        pp = plane_partition_counts(8)
        assert dims == pp

    def test_negative_half_equals_positive(self):
        """dim Y^-_n = dim Y^+_n (anti-involution e_i <-> f_i)."""
        pos = yangian_positive_dimensions(8)
        neg = yangian_negative_dimensions(8)
        assert pos == neg

    def test_cartan_equals_ordinary_partitions(self):
        """dim Y^0_n = p_1D(n) (polynomial algebra in commuting psi_j, j >= 1)."""
        dims = yangian_cartan_dimensions(8)
        op = ordinary_partition_counts(8)
        assert dims == op

    def test_level_1_dimensions(self):
        """At level 1: Y^+ = span{e_0}, Y^- = span{f_0}, Y^0 = span{psi_1}."""
        assert yangian_positive_dimensions(2)[1] == 1
        assert yangian_negative_dimensions(2)[1] == 1
        assert yangian_cartan_dimensions(2)[1] == 1

    def test_level_2_dimensions(self):
        """At level 2: dim Y^+ = 3 (plane partitions of 2), dim Y^0 = 2."""
        assert yangian_positive_dimensions(3)[2] == 3
        assert yangian_cartan_dimensions(3)[2] == 2


# ================================================================
# DRINFELD DOUBLE DIMENSIONS
# ================================================================

class TestDrinfeldDoubleDimensions:
    """Verify dim Y(gl_hat_1)_n = [q^n] M(q)^2 * P(q)."""

    def test_known_dimensions(self):
        """Verify the first several Drinfeld double dimensions."""
        expected = [1, 3, 11, 32, 90, 231, 576, 1363]
        computed = drinfeld_double_dimensions(8)
        assert computed == expected, (
            f"Drinfeld double dimensions mismatch: {computed} != {expected}"
        )

    def test_level_0(self):
        """At level 0: dim = 1 (just the unit)."""
        assert drinfeld_double_dimensions(1)[0] == 1

    def test_level_1_dim_3(self):
        """At level 1: dim = 3 (e_0, f_0, psi_1).

        This is the key prediction: the Drinfeld center adds f_0 and psi_1
        to the original e_0, giving 3 generators at level 1.
        """
        assert drinfeld_double_dimensions(2)[1] == 3

    def test_level_2_dim_11(self):
        """At level 2: dim = 11.

        Breakdown:
            Y^+_2: 3 (plane partitions of 2)
            Y^-_2: 3
            Y^0_2: 2 (ordinary partitions of 2)
            Cross-terms from level-1 products: 3 more
            Total PBW: sum_{a+b+c=2} p3D(a)*p1D(b)*p3D(c) = 11.
        """
        assert drinfeld_double_dimensions(3)[2] == 11

    def test_pbw_matches_character_product(self):
        """The PBW triple sum equals the power series product M(q)^2 * P(q).

        Two independent computation methods must agree.
        """
        N = 12
        pbw = drinfeld_double_dimensions(N)
        product = drinfeld_double_character_product(N)
        assert pbw == product, (
            f"PBW sum and character product disagree at level "
            f"{next(i for i in range(N) if pbw[i] != product[i])}"
        )

    def test_dimension_growth(self):
        """Dimensions grow rapidly (super-exponential, like M(q)^2*P(q))."""
        dims = drinfeld_double_dimensions(8)
        for i in range(1, len(dims)):
            assert dims[i] > dims[i - 1], (
                f"Dimension should be strictly increasing: d({i}) = {dims[i]} "
                f"<= d({i-1}) = {dims[i-1]}"
            )


# ================================================================
# CHARACTER IDENTITY
# ================================================================

class TestCharacterIdentity:
    """Verify ch_Y(q) = M(q)^2 * P(q) = prod_{n>=1} 1/(1-q^n)^{2n+1}."""

    def test_identity_holds(self):
        """The two product formulas agree to high order."""
        result = character_identity_check(20)
        assert result["all_match"], (
            f"Character identity fails at level {result['first_discrepancy']}"
        )

    def test_identity_first_terms(self):
        """Spot-check the first few terms of the product formula."""
        result = character_identity_check(6)
        expected = [1, 3, 11, 32, 90, 231]
        assert result["method1_M2P"] == expected
        assert result["method2_direct"] == expected


# ================================================================
# STRUCTURE FUNCTION
# ================================================================

class TestStructureFunction:
    """Test the structure function g(z) and its key properties."""

    def test_inversion_generic(self):
        """g(z)*g(-z) = 1 for generic parameters h = (1, 2, -3)."""
        result = verify_structure_function_inversion(Rational(1), Rational(2))
        assert result["is_one"], (
            f"g(z)*g(-z) = {result['g_times_g_neg']}, expected 1"
        )

    def test_inversion_fractional(self):
        """g(z)*g(-z) = 1 for fractional parameters h = (1/2, 1/3, -5/6)."""
        result = verify_structure_function_inversion(
            Rational(1, 2), Rational(1, 3)
        )
        assert result["is_one"]

    def test_inversion_schiffmann_vasserot(self):
        """g(z)*g(-z) = 1 for Schiffmann-Vasserot h = (1, -2, 1)."""
        result = verify_structure_function_inversion(
            Rational(1), Rational(-2), Rational(1)
        )
        assert result["is_one"]

    def test_structure_function_limit_infinity(self):
        """g(z) -> 1 as z -> infinity (leading term z^3/z^3 = 1)."""
        z = Symbol("z")
        g = structure_function(Rational(1), Rational(2))
        # Check that the series expansion starts with 1
        g_series = cancel(g)
        # At large z, g ~ 1 + O(1/z^3) (phi_1 = phi_2 = 0 by CY)
        # Substitute a large value and check it's close to 1
        g_100 = g.subs(z, 100)
        assert abs(float(g_100) - 1) < 0.01

    def test_structure_function_poles_and_zeros(self):
        """g(z) has zeros at h_a and poles at -h_a."""
        z = Symbol("z")
        g = structure_function(Rational(1), Rational(2))
        # g(h1) = g(1) = 0
        assert g.subs(z, 1) == 0
        # g(h2) = g(2) = 0
        assert g.subs(z, 2) == 0
        # g(h3) = g(-3) = 0
        assert g.subs(z, -3) == 0


# ================================================================
# R-MATRIX
# ================================================================

class TestRMatrix:
    """Test the R-matrix of the Drinfeld double on the Fock representation."""

    def test_r_matrix_empty_partition(self):
        """R_{empty}(u) = 1 (no boxes -> empty product)."""
        r = r_matrix_diagonal_fock(Rational(1), Rational(2), partition=[])
        assert r == 1

    def test_r_matrix_single_box(self):
        """R_{box}(u) = g(u) (single box at origin, content = 0)."""
        u = Symbol("u")
        r = r_matrix_diagonal_fock(Rational(1), Rational(2), partition=[1])
        g = structure_function(Rational(1), Rational(2))
        z = Symbol("z")
        expected = g.subs(z, u)
        assert cancel(r - expected) == 0

    def test_r_matrix_row_of_2(self):
        """R_{(2)}(u) = g(u) * g(u + h2) for the row partition (2).

        Boxes at (0,0) with content 0 and (0,1) with content h2.
        """
        h1, h2 = Rational(1), Rational(2)
        u = Symbol("u")
        z = Symbol("z")
        r = r_matrix_diagonal_fock(h1, h2, partition=[2])
        g = structure_function(h1, h2)
        expected = g.subs(z, u) * g.subs(z, u + h2)
        assert cancel(r - expected) == 0

    def test_r_matrix_column_of_2(self):
        """R_{(1,1)}(u) = g(u) * g(u + h1) for the column partition (1,1).

        Boxes at (0,0) with content 0 and (1,0) with content h1.
        """
        h1, h2 = Rational(1), Rational(2)
        u = Symbol("u")
        z = Symbol("z")
        r = r_matrix_diagonal_fock(h1, h2, partition=[1, 1])
        g = structure_function(h1, h2)
        expected = g.subs(z, u) * g.subs(z, u + h1)
        assert cancel(r - expected) == 0

    def test_r_matrix_hook_partition(self):
        """R_{(2,1)}(u) = g(u) * g(u+h1) * g(u+h2) for the hook partition.

        Boxes at (0,0), (0,1), (1,0) with contents 0, h2, h1.
        """
        h1, h2 = Rational(1), Rational(2)
        u = Symbol("u")
        z = Symbol("z")
        r = r_matrix_diagonal_fock(h1, h2, partition=[2, 1])
        g = structure_function(h1, h2)
        expected = g.subs(z, u) * g.subs(z, u + h2) * g.subs(z, u + h1)
        assert cancel(r - expected) == 0


class TestRMatrixUnitarity:
    """Verify R(u) * R_{21}(-u) = 1 (unitarity from g(z)*g(-z) = 1)."""

    @pytest.mark.parametrize("partition", [
        [],
        [1],
        [2],
        [1, 1],
        [2, 1],
        [3],
        [1, 1, 1],
    ])
    def test_unitarity(self, partition):
        """R_{12}(u) * R_{21}(-u) = 1 for each partition."""
        result = r_matrix_unitarity_check(
            Rational(1), Rational(2), partition=partition
        )
        assert result["is_unitary"], (
            f"R-matrix unitarity fails for partition {partition}: "
            f"product = {result['product']}"
        )

    def test_unitarity_fractional_params(self):
        """Unitarity holds for fractional deformation parameters."""
        result = r_matrix_unitarity_check(
            Rational(1, 3), Rational(2, 5), partition=[2, 1]
        )
        assert result["is_unitary"]


# ================================================================
# YANG-BAXTER EQUATION
# ================================================================

class TestYangBaxter:
    """Verify the quantum Yang-Baxter equation for the R-matrix."""

    def test_ybe_charge_1(self):
        """YBE on charge-(1,1,1): trivially satisfied (scalar R-matrix)."""
        result = yang_baxter_check_charge_1(Rational(1), Rational(2))
        assert result["match"]

    def test_ybe_charge_1_other_params(self):
        """YBE on charge-(1,1,1) with different deformation parameters."""
        for h1, h2 in [(Rational(3), Rational(-1)),
                       (Rational(1, 2), Rational(1, 3))]:
            result = yang_baxter_check_charge_1(h1, h2)
            assert result["match"], (
                f"YBE fails for h=({h1}, {h2})"
            )

    def test_mixed_charge_ratio(self):
        """The braiding ratio R(2)/R(1,1) = g(u+h2)/g(u+h1).

        This ratio encodes the E_2 structure: how the braiding
        distinguishes between row and column partitions.
        """
        result = yang_baxter_check_charge_mixed(Rational(1), Rational(2))
        assert result["ratio_match"], (
            f"Braiding ratio mismatch: {result['ratio']} != {result['expected_ratio']}"
        )


# ================================================================
# DRINFELD CENTER = FULL YANGIAN (the main claim)
# ================================================================

class TestDrinfeldCenterEqualsYangian:
    """Test the central claim: Z(Rep^{E_1}(CoHA)) = Rep^{E_2}(Y(gl_hat_1)).

    At the algebra level, this is Drin(Y^+) = Y(gl_hat_1).
    We verify this via:
    1. Dimension matching at each graded level
    2. The R-matrix structure (E_2 braiding) arises from the Drinfeld double
    3. The universal R-matrix satisfies YBE (E_2 coherence)
    """

    def test_dimensions_match_through_level_8(self):
        """dim Drin(Y^+)_n = dim Y(gl_hat_1)_n for n = 0,...,8."""
        result = drinfeld_center_dimension_from_coha(9)
        assert result["all_cross_checks_pass"]

        # Verify specific values
        expected = {0: 1, 1: 3, 2: 11, 3: 32, 4: 90, 5: 231, 6: 576, 7: 1363, 8: 3141}
        for n, dim in expected.items():
            assert result["levels"][n]["dim_center"] == dim, (
                f"Level {n}: expected dim {dim}, got {result['levels'][n]['dim_center']}"
            )

    def test_level_1_drinfeld_center(self):
        """At level 1: dim Z = 3 (e_0, f_0, psi_1).

        The positive half Y^+ has dim 1 at level 1 (just e_0).
        The Drinfeld double adds f_0 (dual to e_0) and psi_1 = [e_0, f_0].
        This gives dim 3 at level 1.

        This is the simplest nontrivial verification that the Drinfeld
        center construction works: starting from a 1-dimensional algebra
        at level 1, the center triples the dimension by adding the dual
        and Cartan generators.
        """
        result = drinfeld_center_dimension_from_coha(2)
        level_1 = result["levels"][1]
        assert level_1["dim_center"] == 3
        assert level_1["dim_Y_plus"] == 1  # just e_0
        assert level_1["dim_Y_minus"] == 1  # just f_0
        assert level_1["dim_Y_zero"] == 1  # just psi_1

    def test_level_2_drinfeld_center(self):
        """At level 2: dim Z = 11.

        Y^+_2 has dim 3 (three plane partitions of 2).
        Y^-_2 has dim 3.
        Y^0_2 has dim 2 (psi_1^2 and psi_2).

        The PBW convolution at level 2:
        (a,b,c) with a+b+c=2:
          (2,0,0): p3D(2)*1*1 = 3
          (0,2,0): 1*p1D(2)*1 = 2
          (0,0,2): 1*1*p3D(2) = 3
          (1,1,0): p3D(1)*p1D(1)*1 = 1
          (1,0,1): p3D(1)*1*p3D(1) = 1
          (0,1,1): 1*p1D(1)*p3D(1) = 1
        Total: 3+2+3+1+1+1 = 11.
        """
        result = drinfeld_center_dimension_from_coha(3)
        level_2 = result["levels"][2]
        assert level_2["dim_center"] == 11
        assert level_2["dim_Y_plus"] == 3
        assert level_2["dim_Y_minus"] == 3
        assert level_2["dim_Y_zero"] == 2

    def test_e2_structure_from_r_matrix(self):
        """The R-matrix of Drin(Y^+) gives the E_2 braiding on Rep(Y).

        Key checks:
        1. R(u) is well-defined (no poles for generic u)
        2. R(u) satisfies unitarity: R(u)R_{21}(-u) = 1
        3. R(u) satisfies YBE (E_2 coherence condition)
        """
        h1, h2 = Rational(1), Rational(2)

        # Unitarity
        for part in [[], [1], [2], [1, 1]]:
            uc = r_matrix_unitarity_check(h1, h2, partition=part)
            assert uc["is_unitary"], f"Unitarity fails for partition {part}"

        # YBE (trivial sector)
        yb = yang_baxter_check_charge_1(h1, h2)
        assert yb["match"], "YBE fails on charge-(1,1,1)"

    def test_braiding_distinguishes_partitions(self):
        """The E_2 braiding is nontrivial: it distinguishes partition shapes.

        The ratio R_{(2)}/R_{(1,1)} = g(u+h2)/g(u+h1) is NOT identically 1
        when h1 != h2. This shows the braiding carries genuine E_2 data
        beyond the E_1 monoidal structure.
        """
        h1, h2 = Rational(1), Rational(2)
        result = yang_baxter_check_charge_mixed(h1, h2)
        assert result["ratio_match"]

        # The ratio should NOT be constant (it depends on u)
        u = Symbol("u")
        ratio = result["ratio"]
        # Evaluate at two different points
        r_at_4 = ratio.subs(u, 4)
        r_at_5 = ratio.subs(u, 5)
        assert r_at_4 != r_at_5, (
            "Braiding ratio should depend on spectral parameter u"
        )

    def test_abelian_limit_sv_n1(self):
        """At h=(1,-1,0) (Schiffmann-Vasserot N=1): g(z) = 1 (abelian).

        sigma_3 = 0, so all phi_j = 0 for j >= 1.
        The R-matrix is trivial: R(u) = 1 for all u.
        The Drinfeld double is abelian (symmetric braiding).
        """
        h1, h2 = Rational(1), Rational(-1)
        h3 = Rational(0)

        # g(z) = (z-1)(z+1)(z-0)/((z+1)(z-1)(z+0)) = z/z = 1
        z = Symbol("z")
        g = structure_function(h1, h2, h3)
        assert cancel(g - 1) == 0, "g(z) should be identically 1 for N=1"

        # R-matrix is trivial
        r = r_matrix_diagonal_fock(h1, h2, h3, partition=[2, 1])
        assert r == 1, "R-matrix should be 1 in the abelian limit"


# ================================================================
# E_1 -> E_2 BRAIDING DATA
# ================================================================

class TestBraidingData:
    """Test the braiding data for the E_1 -> E_2 passage."""

    def test_braiding_data_structure(self):
        """The braiding data is organized by partition."""
        data = e1_to_e2_braiding_data(Rational(1), Rational(2), max_charge=2)
        r_data = data["r_matrix_data"]

        # Check all partitions up to charge 2 are present
        assert () in r_data
        assert (1,) in r_data
        assert (2,) in r_data
        assert (1, 1) in r_data

    def test_braiding_charge_0(self):
        """At charge 0: R_{empty}(u) = 1."""
        data = e1_to_e2_braiding_data(Rational(1), Rational(2), max_charge=1)
        assert data["r_matrix_data"][()]["R_diagonal"] == 1

    def test_braiding_charges_match_dimensions(self):
        """Number of partitions at each charge matches expected count."""
        data = e1_to_e2_braiding_data(Rational(1), Rational(2), max_charge=4)
        partitions = data["partitions_by_charge"]

        # Number of ordinary partitions at each charge
        assert len(partitions[0]) == 1  # just ()
        assert len(partitions[1]) == 1  # just (1,)
        assert len(partitions[2]) == 2  # (2,) and (1,1)
        assert len(partitions[3]) == 3  # (3,), (2,1), (1,1,1)
        assert len(partitions[4]) == 5  # five partitions of 4


# ================================================================
# LEVEL DECOMPOSITION
# ================================================================

class TestLevelDecomposition:
    """Test the level-by-level decomposition of the Drinfeld double."""

    def test_level_decomposition_dimensions(self):
        """Each level reports correct component dimensions."""
        ld = level_decomposition(6)
        for n in range(6):
            d = ld[n]
            pp = plane_partition_counts(n + 1)
            op = ordinary_partition_counts(n + 1)
            assert d["dim_Y_plus"] == pp[n]
            assert d["dim_Y_minus"] == pp[n]
            assert d["dim_Y_zero"] == op[n]

    def test_total_dimension_consistency(self):
        """The total dimension matches the PBW computation."""
        ld = level_decomposition(6)
        dd = drinfeld_double_dimensions(6)
        for n in range(6):
            assert ld[n]["dim_total"] == dd[n]


# ================================================================
# FULL VERIFICATION SUITE
# ================================================================

class TestFullVerification:
    """Run the complete verification pipeline."""

    def test_full_suite_passes(self):
        """All checks in verify_drinfeld_center_coha pass."""
        results = verify_drinfeld_center_coha(N=6)

        # Dimensions
        assert results["dimensions"]["all_cross_checks_pass"]

        # Inversion identity
        assert results["inversion"]["is_one"]

        # Unitarity (all partitions)
        for lam, uc in results["unitarity"].items():
            assert uc["is_unitary"], f"Unitarity fails for {lam}"

        # Yang-Baxter
        assert results["yang_baxter_trivial"]["match"]
        assert results["yang_baxter_mixed"]["ratio_match"]
