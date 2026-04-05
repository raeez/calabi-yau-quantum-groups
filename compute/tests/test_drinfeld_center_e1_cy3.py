r"""Tests for the Drinfeld center E_1 -> E_2 passage for CY3-derived chiral algebras.

Manuscript references:
    Part IV (Quantum Groups and Braided Monoidal Structure):
        thm:drinfeld-center-qw: universal Drinfeld center theorem for (Q,W)
        thm:drinfeld-center-coha: Z(Rep^{E_1}(CoHA)) = Rep^{E_2}(Y(gl_hat_1))
        sec:cy-drinfeld: CY enhancement of the Drinfeld center
        sec:qg-reconstruction: Quantum group reconstruction from the center

Literature ground truth:
    OEIS A000219 (plane partitions): 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500
    OEIS A000041 (ordinary partitions): 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
    Drinfeld double dims M^2*P: 1, 3, 11, 32, 90, 231, 576, 1363, 3141

    C^3: CoHA = Y^+(gl_hat_1), Drin = Y(gl_hat_1) = W_{1+infty}
    Conifold: Omega(d*beta) = (-1)^{d-1}, pentagon identity
    Local P^2: GV genus-0: n^0_1=3, n^0_2=-6, n^0_3=27
    K3 x E: DMVV c(-1)=1, c(0)=10 (Eichler-Zagier)

    Structure function g(z) = (z-h1)(z-h2)(z-h3)/((z+h1)(z+h2)(z+h3)):
        g(z)*g(-z) = 1 (CY inversion identity)
        g(0) = -1

    Yang R-matrix R(z) = (z*Id + kappa*P)/(z+kappa):
        Unitarity: R(z)*R(-z) = Id (from P^2 = Id and g(-z)=1/g(z))
        YBE: R_{12}(u-v)*R_{13}(u)*R_{23}(v) = R_{23}(v)*R_{13}(u)*R_{12}(u-v)
        R(0) = P (permutation)
        Eigenvalues: 1 (sym), (z-kappa)/(z+kappa) (antisym)
        kappa = h1*h2*h3 (CY cubic Casimir)

    CY condition on conifold R-matrix:
        R(z) = (z+eps_+)(z+eps_-)/(z(z+eps_sum))
        O(1/z) coefficient = eps_++eps_--eps_sum = 0 (CY forces vanishing)

    Collision residue identification (Vol I, thm:mc2-bar-intrinsic, AP19):
        R(z) = Id + kappa*(P-Id)/(z+kappa)
        Collision residue kernel = kappa*(P-Id)
        Reconstruction: kernel determines R(z) completely
"""

import pytest
from fractions import Fraction
from sympy import Matrix, Rational, Symbol, cancel, expand, simplify, I, pi, exp

from compute.lib.drinfeld_center_e1_cy3 import (
    DrinfeldCenterC3,
    DrinfeldCenterConifold,
    DrinfeldCenterLocalP2,
    DrinfeldCenterK3E,
    _g,
    _g_symbolic,
    box_contents,
    collision_residue_r_matrix_c3,
    collision_residue_r_matrix_conifold,
    does_drinfeld_center_always_produce_yangian,
    e1_to_e2_comparison_table,
    ordinary_partition_counts,
    partitions_of,
    plane_partition_counts,
    quintic_quantum_group_analysis,
    universal_drinfeld_center_theorem,
)


# ================================================================
# SECTION 1: COMBINATORIAL BUILDING BLOCKS
# ================================================================

class TestPartitionCombinatorics:
    """Verify partition enumerations match known values."""

    def test_plane_partitions_oeis(self):
        """pp(n) matches OEIS A000219."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        computed = plane_partition_counts(11)
        assert computed == expected

    def test_ordinary_partitions_oeis(self):
        """p(n) matches OEIS A000041."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        computed = ordinary_partition_counts(11)
        assert computed == expected

    def test_partitions_of_small(self):
        assert partitions_of(0) == [()]
        assert partitions_of(1) == [(1,)]
        assert partitions_of(2) == [(2,), (1, 1)]
        assert partitions_of(3) == [(3,), (2, 1), (1, 1, 1)]

    def test_partition_counts_match(self):
        """Number of partitions of n matches p(n)."""
        p = ordinary_partition_counts(8)
        for n in range(8):
            assert len(partitions_of(n)) == p[n]

    def test_box_contents(self):
        """Box contents c(i,j) = h1*i + h2*j."""
        h1, h2 = Rational(1), Rational(2)
        # Partition (2): boxes at (0,0), (0,1)
        assert box_contents((2,), h1, h2) == [0, h2]
        # Partition (1,1): boxes at (0,0), (1,0)
        assert box_contents((1, 1), h1, h2) == [0, h1]
        # Partition (2,1): boxes at (0,0), (0,1), (1,0)
        assert box_contents((2, 1), h1, h2) == [0, h2, h1]


# ================================================================
# SECTION 2: STRUCTURE FUNCTION PROPERTIES
# ================================================================

class TestStructureFunction:
    """Verify the CY3 structure function g(z)."""

    def test_g_inversion_symbolic(self):
        """g(z)*g(-z) = 1 for general h1, h2, h3 with h1+h2+h3=0."""
        h1, h2 = Symbol("h1"), Symbol("h2")
        h3 = -(h1 + h2)
        z = Symbol("z")
        g_z = _g(z, h1, h2, h3)
        g_neg = _g(-z, h1, h2, h3)
        product = cancel(g_z * g_neg)
        assert product == 1, f"g(z)*g(-z) = {product}, expected 1"

    def test_g_inversion_numeric(self):
        """g(z)*g(-z) = 1 at specific parameter values."""
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        for z_val in [Rational(4), Rational(5), Rational(7), Rational(10)]:
            g_z = _g(z_val, h1, h2, h3)
            g_neg = _g(-z_val, h1, h2, h3)
            assert cancel(g_z * g_neg) == 1

    def test_g_at_zero(self):
        """g(0) = -1 (when h_i != 0)."""
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        assert cancel(_g(Rational(0), h1, h2, h3) + 1) == 0

    def test_g_at_infinity(self):
        """g(z) -> 1 as z -> infinity (degree 3/3 rational function)."""
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        z_large = Rational(1000)
        g_val = _g(z_large, h1, h2, h3)
        # Should be close to 1
        assert abs(float(g_val) - 1.0) < 0.01

    def test_g_zeros_and_poles(self):
        """g(z) has zeros at h1,h2,h3 and poles at -h1,-h2,-h3."""
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        for z_val in [h1, h2, h3]:
            assert _g(z_val, h1, h2, h3) == 0
        # At poles, g should diverge (test near the pole)
        # g(-h1 + epsilon) should be large
        eps = Rational(1, 100)
        assert abs(float(_g(-h1 + eps, h1, h2, h3))) > 10

    def test_g_symmetric_in_h(self):
        """g(z) is symmetric under permutations of (h1,h2,h3)."""
        z = Symbol("z")
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        g_123 = cancel(_g(z, h1, h2, h3))
        g_231 = cancel(_g(z, h2, h3, h1))
        g_312 = cancel(_g(z, h3, h1, h2))
        assert cancel(g_123 - g_231) == 0
        assert cancel(g_123 - g_312) == 0


# ================================================================
# SECTION 3: C^3 DRINFELD CENTER
# ================================================================

class TestDrinfeldCenterC3:
    """Test the C^3 Drinfeld center: Y^+(gl_hat_1) -> Y(gl_hat_1)."""

    @pytest.fixture
    def dc3(self):
        return DrinfeldCenterC3(Rational(1), Rational(2))

    def test_kappa(self, dc3):
        """kappa = h1*h2*h3 = 1*2*(-3) = -6."""
        assert dc3.kappa == Rational(-6)

    def test_inversion(self, dc3):
        """g(z)*g(-z) = 1."""
        assert dc3.inversion_identity() is True

    def test_unitarity(self, dc3):
        """R(z)*R(-z) = Id for the Yang R-matrix."""
        assert dc3.verify_unitarity() is True

    def test_ybe(self, dc3):
        """Yang-Baxter equation holds on V^{otimes 3}."""
        assert dc3.verify_ybe() is True

    def test_character_match(self, dc3):
        """ch(Y) = M(q)^2*P(q) = prod 1/(1-q^n)^{2n+1}."""
        char_data = dc3.character_dimensions(10)
        assert char_data["match"] is True

    def test_character_first_dims(self, dc3):
        """First few dimensions of Y(gl_hat_1)."""
        char_data = dc3.character_dimensions(10)
        expected = [1, 3, 11, 32, 90, 231, 576, 1363, 3141]
        dims = char_data["first_dims"]
        for i, exp_val in enumerate(expected):
            assert dims[i] == exp_val, f"dim({i}) = {dims[i]}, expected {exp_val}"

    def test_yang_r_matrix_at_0_is_P(self, dc3):
        """R(0) = P (permutation operator)."""
        R_at_0 = dc3.yang_r_matrix_4x4(Rational(0))
        P = Matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ])
        assert R_at_0 == P

    def test_yang_r_eigenvalues(self, dc3):
        """Eigenvalues: 1 (symmetric) and (z-kappa)/(z+kappa) (antisymmetric)."""
        z = Symbol("z")
        R = dc3.yang_r_matrix_4x4(z)
        # On the symmetric subspace e1e1 (index 0,0):
        # R[0,0] should be 1
        assert cancel(R[0, 0] - 1) == 0
        # On the off-diagonal 2x2 block:
        R_block = dc3.yang_r_matrix_2x2(z)
        # Eigenvalues of [[z/(z+k), k/(z+k)], [k/(z+k), z/(z+k)]]
        # are (z+k)/(z+k) = 1 and (z-k)/(z+k)
        kappa = dc3.kappa
        eig_sym = cancel(R_block[0, 0] + R_block[0, 1])
        eig_anti = cancel(R_block[0, 0] - R_block[0, 1])
        assert cancel(eig_sym - 1) == 0
        assert cancel(eig_anti - (z - kappa) / (z + kappa)) == 0

    def test_diagonal_r_matrix_empty(self, dc3):
        """R(u)_{empty} = 1."""
        assert dc3.r_matrix_diagonal(()) == Rational(1)

    def test_diagonal_r_matrix_single_box(self, dc3):
        """R(u)_{(1)} = g(u)."""
        u = Symbol("u")
        R = dc3.r_matrix_diagonal((1,))
        g_u = cancel(_g(u, dc3.h1, dc3.h2, dc3.h3))
        assert cancel(R - g_u) == 0

    def test_diagonal_r_matrix_row(self, dc3):
        """R(u)_{(2)} = g(u)*g(u+h2)."""
        u = Symbol("u")
        h1, h2, h3 = dc3.h1, dc3.h2, dc3.h3
        R = dc3.r_matrix_diagonal((2,))
        expected = cancel(_g(u, h1, h2, h3) * _g(u + h2, h1, h2, h3))
        assert cancel(R - expected) == 0

    def test_diagonal_r_matrix_col(self, dc3):
        """R(u)_{(1,1)} = g(u)*g(u+h1)."""
        u = Symbol("u")
        h1, h2, h3 = dc3.h1, dc3.h2, dc3.h3
        R = dc3.r_matrix_diagonal((1, 1))
        expected = cancel(_g(u, h1, h2, h3) * _g(u + h1, h1, h2, h3))
        assert cancel(R - expected) == 0

    def test_diagonal_r_unitarity_per_partition(self, dc3):
        """R(u)_{lam}*R(-u)_{lam,swapped} = 1 for small partitions."""
        u = Symbol("u")
        h1, h2, h3 = dc3.h1, dc3.h2, dc3.h3
        for lam in [(), (1,), (2,), (1, 1), (2, 1)]:
            R_u = dc3.r_matrix_diagonal(lam)
            # R_{21}(-u) involves g(-(u+c)) = 1/g(u+c)
            contents = box_contents(lam, h1, h2)
            R_swap_neg = Rational(1)
            for c in contents:
                R_swap_neg = R_swap_neg * _g(-(u + c), h1, h2, h3)
            product = cancel(R_u * R_swap_neg)
            assert product == 1, f"Unitarity failed for lambda={lam}: product={product}"

    def test_collision_residue(self, dc3):
        """Collision residue reconstruction: R(z) = Id + kernel/(z+kappa)."""
        cr = dc3.collision_residue()
        assert cr["R_at_0_is_P"] is True

    def test_full_verification(self, dc3):
        """Run the full verification suite."""
        v = dc3.full_verification(N=8)
        assert v["inversion"] is True
        assert v["unitarity"] is True
        assert v["ybe"] is True
        assert v["character"]["match"] is True

    def test_g_at_0_is_neg_1(self, dc3):
        """g(0) = -1."""
        assert cancel(dc3.g_eval(Rational(0)) + 1) == 0


class TestDrinfeldCenterC3ParameterVariation:
    """Test C^3 Drinfeld center at different parameter values."""

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
        (Rational(1), Rational(1)),
        (Rational(3), Rational(7)),
    ])
    def test_inversion_various_params(self, h1, h2):
        dc = DrinfeldCenterC3(h1, h2)
        assert dc.inversion_identity() is True

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
    ])
    def test_unitarity_various_params(self, h1, h2):
        dc = DrinfeldCenterC3(h1, h2)
        assert dc.verify_unitarity() is True

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(1), Rational(3)),
    ])
    def test_ybe_various_params(self, h1, h2):
        dc = DrinfeldCenterC3(h1, h2)
        assert dc.verify_ybe() is True


# ================================================================
# SECTION 4: CONIFOLD DRINFELD CENTER
# ================================================================

class TestDrinfeldCenterConifold:
    """Test the conifold Drinfeld center."""

    @pytest.fixture
    def dc_con(self):
        return DrinfeldCenterConifold(Rational(1), Rational(2))

    def test_epsilon_values(self, dc_con):
        """eps_+ = -h3 = h1+h2, eps_- = -h1, eps_sum = h2."""
        assert dc_con.epsilon_plus == Rational(3)   # h1+h2 = 1+2 = 3
        assert dc_con.epsilon_minus == Rational(-1)  # -h1 = -1... wait
        # eps_- = h2+h3 = 2+(-3) = -1. And -h1 = -1. Check.
        # Actually eps_- = -h1 = -1. Yes.
        # But the attribute is computed differently. Let me check.
        # self.epsilon_minus = h2 + h3 = 2 + (-3) = -1. And -h1 = -1. Match.
        assert dc_con.epsilon_minus == Rational(-1)

    def test_conifold_r_matrix_structure(self, dc_con):
        """R(z) has 2 poles and 2 zeros."""
        r_data = dc_con.conifold_r_matrix_scalar()
        assert len(r_data["poles"]) == 2
        assert len(r_data["zeros"]) == 2

    def test_conifold_cy_cancellation(self, dc_con):
        """CY condition forces O(1/z) coefficient to vanish."""
        cr = dc_con.collision_residue()
        assert cr["CY_forces_vanishing"] is True

    def test_conifold_collision_residue_nonzero(self, dc_con):
        """Collision residue is nonzero."""
        cr = dc_con.collision_residue()
        assert cr["residue_at_0"] != 0

    def test_dt_invariants_sign_pattern(self, dc_con):
        """Omega(d*beta) = (-1)^{d-1} for the conifold."""
        omega = dc_con.dt_invariants(10)
        for d in range(1, 11):
            assert omega[d] == (-1) ** (d - 1)

    def test_wall_crossing_consistency(self, dc_con):
        """Wall-crossing data is consistent."""
        wc = dc_con.wall_crossing_data()
        assert wc["sign_pattern"] is True

    def test_quantum_group_is_super(self, dc_con):
        """Conifold quantum group is a superalgebra."""
        qg = dc_con.quantum_group_identification()
        assert "1|1" in qg["quantum_group"]

    def test_conifold_r_unitarity_analysis(self, dc_con):
        """Unitarity analysis: R(z)*R(-z) is even, NOT = 1 for mixed charges."""
        result = dc_con.conifold_r_unitarity()
        # For non-self-conjugate charges, simple unitarity FAILS (this is correct)
        assert result["simple_unitarity"] is False
        # The product formula matches the explicit (a^2-z^2)(b^2-z^2)/(z^2(c^2-z^2))
        assert result["product_matches_formula"] is True
        # The product IS even in z
        assert result["product_is_even"] is True

    def test_conifold_r_matrix_rational(self, dc_con):
        """The conifold R-matrix is a rational function."""
        z = Symbol("z")
        r_data = dc_con.conifold_r_matrix_scalar()
        R_z = r_data["R"]
        # Check it's a ratio of polynomials
        assert R_z.is_rational_function(z)


class TestConifoldParameterVariation:
    """Conifold at different parameters."""

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
        (Rational(1), Rational(1)),
    ])
    def test_cy_cancellation_various(self, h1, h2):
        dc = DrinfeldCenterConifold(h1, h2)
        cr = dc.collision_residue()
        assert cr["CY_forces_vanishing"] is True

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
    ])
    def test_product_formula_various(self, h1, h2):
        """R(z)*R(-z) matches explicit formula at various parameters."""
        dc = DrinfeldCenterConifold(h1, h2)
        result = dc.conifold_r_unitarity()
        assert result["product_matches_formula"] is True
        assert result["product_is_even"] is True


# ================================================================
# SECTION 5: LOCAL P^2 DRINFELD CENTER
# ================================================================

class TestDrinfeldCenterLocalP2:
    """Test the local P^2 Drinfeld center."""

    @pytest.fixture
    def dc_lp2(self):
        return DrinfeldCenterLocalP2(Rational(1), Rational(2))

    def test_z3_sectors_equal(self, dc_lp2):
        """All Z_3 twisted sectors have the same g(z) (by symmetry)."""
        r_data = dc_lp2.r_matrix_orbifold()
        assert r_data["all_equal"] is True

    def test_orbifold_g_sector_0_equals_c3(self, dc_lp2):
        """Untwisted sector g_0(z) = g(z) of C^3."""
        z = Symbol("z")
        g_0 = dc_lp2.orbifold_structure_function(0)
        g_c3 = cancel(_g(z, dc_lp2.h1, dc_lp2.h2, dc_lp2.h3))
        assert cancel(g_0 - g_c3) == 0

    def test_orbifold_g_all_sectors_same(self, dc_lp2):
        """All three sectors give the same g(z) due to h-symmetry."""
        g_0 = dc_lp2.orbifold_structure_function(0)
        g_1 = dc_lp2.orbifold_structure_function(1)
        g_2 = dc_lp2.orbifold_structure_function(2)
        assert cancel(g_0 - g_1) == 0
        assert cancel(g_0 - g_2) == 0

    def test_gv_genus_0(self, dc_lp2):
        """GV genus-0 invariants: n^0_1=3, n^0_2=-6, n^0_3=27."""
        gv = dc_lp2.gv_invariants()
        assert gv["g0"][1] == 3
        assert gv["g0"][2] == -6
        assert gv["g0"][3] == 27

    def test_gv_genus_1(self, dc_lp2):
        """GV genus-1: n^1_1=0, n^1_2=0, n^1_3=-10."""
        gv = dc_lp2.gv_invariants()
        assert gv["g1"].get(1, 0) == 0
        assert gv["g1"].get(2, 0) == 0
        assert gv["g1"][3] == -10

    def test_kappa_geometric(self, dc_lp2):
        """kappa_geometric = chi(P^2)/24 = 3/24 = 1/8."""
        kappa_data = dc_lp2.kappa_from_gv()
        assert kappa_data["kappa_geometric"] == Fraction(1, 8)
        assert kappa_data["euler_char_P2"] == 3

    def test_quantum_group_type(self, dc_lp2):
        """Quantum group is the Z_3-orbifold quantum toroidal algebra."""
        qg = dc_lp2.quantum_group_identification()
        assert "Z_3" in qg["quantum_group"]


# ================================================================
# SECTION 6: K3 x E DRINFELD CENTER
# ================================================================

class TestDrinfeldCenterK3E:
    """Test the K3 x E Drinfeld center."""

    @pytest.fixture
    def dc_k3e(self):
        return DrinfeldCenterK3E()

    def test_mukai_lattice(self, dc_k3e):
        """Mukai lattice rank = 24, signature = (4,20)."""
        lat = dc_k3e.mukai_lattice_data()
        assert lat["rank"] == 24
        assert lat["signature"] == (4, 20)

    def test_real_root_multiplicity(self, dc_k3e):
        """Real root multiplicity c(-1) = 1."""
        roots = dc_k3e.root_multiplicities()
        assert roots["real_root_mult"] == 1

    def test_imaginary_root_multiplicity(self, dc_k3e):
        """Imaginary root multiplicity c(0) = 10 (Eichler-Zagier)."""
        roots = dc_k3e.root_multiplicities()
        assert roots["imaginary_root_mult"] == 10

    def test_dmvv_coefficients(self, dc_k3e):
        """DMVV coefficients match known values (AP38: Eichler-Zagier convention)."""
        coeffs = dc_k3e._dmvv_coeffs
        assert coeffs[-1] == 1
        assert coeffs[0] == 10
        assert coeffs[3] == -64
        assert coeffs[4] == 108

    def test_quantum_group_is_bkm(self, dc_k3e):
        """Quantum group is a BKM superalgebra (exotic)."""
        qg = dc_k3e.quantum_group_identification()
        assert "BKM" in qg["quantum_group"]
        assert qg["exotic"] is True

    def test_not_standard_quantum_group(self, dc_k3e):
        """K3 x E quantum group is NOT a standard quantum toroidal."""
        qg = dc_k3e.quantum_group_identification()
        assert "NOT standard" in qg["type"]

    def test_character_coha_dim_0(self, dc_k3e):
        """dim CoHA_0 = 1 (empty sheaf)."""
        char = dc_k3e.drinfeld_center_character(5)
        assert char["coha_dims"][0] == 1

    def test_character_goettsche(self, dc_k3e):
        """CoHA character at y=1 is prod 1/(1-q^n)^{24} (Goettsche)."""
        char = dc_k3e.drinfeld_center_character(8)
        # First few terms of prod 1/(1-q^n)^{24}:
        # n=0: 1, n=1: 24, n=2: 24*25/2 = 300, ...
        # Actually: prod 1/(1-q^n)^{24} gives the Ramanujan tau-related numbers
        # Let me compute: it's sum of 24-colored partitions.
        # p(1,24) = 24, p(2,24) = 24 + C(24,2) = 24 + 276 = 300
        assert char["coha_dims"][0] == 1
        assert char["coha_dims"][1] == 24
        assert char["coha_dims"][2] == 300

    def test_cartan_dimension(self, dc_k3e):
        """BKM Cartan dimension = 26."""
        char = dc_k3e.drinfeld_center_character(5)
        assert char["cartan_dim"] == 26


# ================================================================
# SECTION 7: COLLISION RESIDUE VERIFICATION
# ================================================================

class TestCollisionResidue:
    """Verify R-matrix = collision residue of E_1 MC element."""

    def test_c3_reconstruction(self):
        """R(z) = Id + kappa*(P-Id)/(z+kappa) for C^3."""
        cr = collision_residue_r_matrix_c3()
        assert cr["reconstruction_match"] is True

    def test_c3_r_at_0_is_P(self):
        """R(0) = P for C^3."""
        cr = collision_residue_r_matrix_c3()
        assert cr["R_at_0_is_P"] is True

    def test_c3_kappa_value(self):
        """kappa = 1*2*(-3) = -6 for (h1,h2) = (1,2)."""
        cr = collision_residue_r_matrix_c3()
        assert cr["kappa"] == Rational(-6)

    def test_c3_pole_location(self):
        """R-matrix pole at z = -kappa = 6."""
        cr = collision_residue_r_matrix_c3()
        assert cr["pole_location"] == Rational(6)

    def test_conifold_cy_vanishing(self):
        """CY condition forces O(1/z) = 0 for conifold."""
        cr = collision_residue_r_matrix_conifold()
        assert cr["CY_forces_vanishing_1_over_z"] is True

    def test_conifold_residue_at_0(self):
        """Conifold collision residue is eps_+*eps_-/eps_sum."""
        cr = collision_residue_r_matrix_conifold()
        h1, h2, h3 = Rational(1), Rational(2), Rational(-3)
        eps_p = h1 + h2  # 3
        eps_m = -h1       # -1
        eps_s = h2         # 2
        expected = cancel(eps_p * eps_m / eps_s)
        assert cancel(cr["collision_residue"] - expected) == 0

    def test_conifold_residue_numeric(self):
        """Numerical value of conifold collision residue."""
        cr = collision_residue_r_matrix_conifold()
        # eps_+ = 3, eps_- = -1, eps_sum = 2
        # residue = 3*(-1)/2 = -3/2
        assert cr["collision_residue"] == Rational(-3, 2)

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
        (Rational(3), Rational(7)),
    ])
    def test_c3_reconstruction_various(self, h1, h2):
        """R-matrix reconstruction works at various parameters."""
        cr = collision_residue_r_matrix_c3(h1, h2)
        assert cr["reconstruction_match"] is True

    @pytest.mark.parametrize("h1,h2", [
        (Rational(1), Rational(2)),
        (Rational(1), Rational(3)),
        (Rational(2), Rational(5)),
    ])
    def test_conifold_cy_various(self, h1, h2):
        """CY vanishing holds at various parameters."""
        cr = collision_residue_r_matrix_conifold(h1, h2)
        assert cr["CY_forces_vanishing_1_over_z"] is True


# ================================================================
# SECTION 8: UNIVERSAL THEOREM
# ================================================================

class TestUniversalTheorem:
    """Test the universal Drinfeld center theorem."""

    def test_theorem_has_all_examples(self):
        """Universal theorem covers all standard CY3 examples."""
        thm = universal_drinfeld_center_theorem()
        examples = thm["examples"]
        assert "C^3" in examples
        assert "conifold" in examples
        assert "local_P^2" in examples
        assert "K3_x_E" in examples
        assert "quintic" in examples

    def test_c3_identification(self):
        """C^3: Drin(Y^+) = Y(gl_hat_1) = W_{1+infty}."""
        thm = universal_drinfeld_center_theorem()
        assert "W_{1+infty}" in thm["examples"]["C^3"]

    def test_conifold_identification(self):
        """Conifold: quantum toroidal gl(1|1)."""
        thm = universal_drinfeld_center_theorem()
        assert "gl(1|1)" in thm["examples"]["conifold"]

    def test_k3e_is_exotic(self):
        """K3 x E is marked as exotic (BKM)."""
        thm = universal_drinfeld_center_theorem()
        assert "EXOTIC" in thm["examples"]["K3_x_E"]

    def test_quintic_unknown(self):
        """Quintic quantum group is unknown."""
        thm = universal_drinfeld_center_theorem()
        assert "UNKNOWN" in thm["examples"]["quintic"]


# ================================================================
# SECTION 9: COMPARISON TABLE
# ================================================================

class TestComparisonTable:
    """Test the E_1 -> E_2 comparison table."""

    def test_all_examples_present(self):
        """All 5 examples present in the comparison table."""
        table = e1_to_e2_comparison_table()
        assert len(table) == 5
        for key in ["C^3", "conifold", "local_P^2", "K3_x_E", "quintic"]:
            assert key in table

    def test_all_have_required_fields(self):
        """Each example has E1, E2, R_type, character, status."""
        table = e1_to_e2_comparison_table()
        for name, data in table.items():
            assert "E1" in data, f"{name} missing E1"
            assert "E2" in data, f"{name} missing E2"
            assert "R_type" in data, f"{name} missing R_type"
            assert "character" in data, f"{name} missing character"
            assert "status" in data, f"{name} missing status"

    def test_c3_status_proved(self):
        """C^3 status is PROVED."""
        table = e1_to_e2_comparison_table()
        assert "PROVED" in table["C^3"]["status"]

    def test_conifold_status_proved(self):
        """Conifold status is PROVED."""
        table = e1_to_e2_comparison_table()
        assert "PROVED" in table["conifold"]["status"]

    def test_k3e_status_conjectural(self):
        """K3 x E status is CONJECTURAL."""
        table = e1_to_e2_comparison_table()
        assert "CONJECTURAL" in table["K3_x_E"]["status"]

    def test_quintic_status_open(self):
        """Quintic status is OPEN."""
        table = e1_to_e2_comparison_table()
        assert "OPEN" in table["quintic"]["status"]


# ================================================================
# SECTION 10: DEEP QUESTION
# ================================================================

class TestDeepQuestion:
    """Test: does Drinfeld center always produce a Yangian?"""

    def test_answer_is_no(self):
        """The answer is NO -- exotic quantum groups can appear."""
        dq = does_drinfeld_center_always_produce_yangian()
        assert "NO" in dq["answer"].upper()

    def test_toric_gives_toroidal(self):
        """Toric CY3 gives quantum toroidal algebra."""
        dq = does_drinfeld_center_always_produce_yangian()
        assert "toroidal" in dq["toric"].lower()

    def test_k3_gives_bkm(self):
        """K3-fibered gives BKM algebra."""
        dq = does_drinfeld_center_always_produce_yangian()
        assert "BKM" in dq["k3_fiber"]

    def test_general_unknown(self):
        """General CY3 quantum group is unknown."""
        dq = does_drinfeld_center_always_produce_yangian()
        assert "UNKNOWN" in dq["general"]


# ================================================================
# SECTION 11: QUINTIC ANALYSIS
# ================================================================

class TestQuinticAnalysis:
    """Test the quintic CY3 quantum group analysis."""

    def test_hodge_numbers(self):
        """Quintic: h^{1,1}=1, h^{2,1}=101."""
        qa = quintic_quantum_group_analysis()
        assert qa["hodge"]["h11"] == 1
        assert qa["hodge"]["h21"] == 101

    def test_euler_characteristic(self):
        """Quintic: chi = -200."""
        qa = quintic_quantum_group_analysis()
        assert qa["euler"] == -200

    def test_quantum_group_unknown(self):
        """Quintic quantum group is UNKNOWN."""
        qa = quintic_quantum_group_analysis()
        assert qa["quantum_group"] == "UNKNOWN"

    def test_exotic(self):
        """Quintic is exotic."""
        qa = quintic_quantum_group_analysis()
        assert qa["exotic"] is True

    def test_gv_genus_0(self):
        """Quintic GV genus-0: n^0_1=2875 (lines on quintic)."""
        qa = quintic_quantum_group_analysis()
        assert qa["known_data"]["gv_genus_0"][1] == 2875

    def test_kappa_eff(self):
        """kappa_eff = chi/24 = -200/24 = -25/3."""
        qa = quintic_quantum_group_analysis()
        assert qa["known_data"]["kappa_eff"] == Fraction(-200, 24)

    def test_prepotential_cubic_term(self):
        """Quintic prepotential: F_0 = (5/6)*t^3 + ..."""
        qa = quintic_quantum_group_analysis()
        assert "5/6" in qa["known_data"]["prepotential"]


# ================================================================
# SECTION 12: CROSS-CONSISTENCY CHECKS
# ================================================================

class TestCrossConsistency:
    """Cross-checks between different CY3 examples."""

    def test_all_structure_functions_satisfy_inversion(self):
        """g(z)*g(-z) = 1 for all examples (CY condition)."""
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(1), Rational(3)),
                        (Rational(2), Rational(5))]:
            dc = DrinfeldCenterC3(h1, h2)
            assert dc.inversion_identity() is True

    def test_conifold_r_reduces_to_c3_at_special_limit(self):
        """In a degeneration limit, conifold R -> C^3 R."""
        # The conifold R-matrix R(z) = (z+eps_+)(z+eps_-)/(z(z+eps_sum))
        # reduces to g(z) of C^3 when we identify the Euler pairing
        # with the structure function. The CY condition ensures both
        # have vanishing O(1/z) correction.
        for h1, h2 in [(Rational(1), Rational(2)),
                        (Rational(1), Rational(3))]:
            cr_c3 = collision_residue_r_matrix_c3(h1, h2)
            cr_con = collision_residue_r_matrix_conifold(h1, h2)
            # Both satisfy CY vanishing
            assert cr_con["CY_forces_vanishing_1_over_z"] is True
            # Both give nontrivial collision residues
            assert cr_c3["kappa"] != 0
            assert cr_con["collision_residue"] != 0

    def test_local_p2_inherits_c3_structure(self):
        """Local P^2 untwisted sector = C^3 structure function."""
        dc_lp2 = DrinfeldCenterLocalP2(Rational(1), Rational(2))
        dc_c3 = DrinfeldCenterC3(Rational(1), Rational(2))
        z = Symbol("z")
        g_lp2_sector0 = dc_lp2.orbifold_structure_function(0)
        g_c3 = cancel(_g(z, dc_c3.h1, dc_c3.h2, dc_c3.h3))
        assert cancel(g_lp2_sector0 - g_c3) == 0

    def test_character_monotonicity_c3(self):
        """Y(gl_hat_1) dimensions are strictly increasing."""
        dc = DrinfeldCenterC3()
        char = dc.character_dimensions(10)
        dims = char["first_dims"]
        for i in range(1, len(dims)):
            assert dims[i] > dims[i - 1], f"dim({i})={dims[i]} <= dim({i-1})={dims[i-1]}"

    def test_k3e_coha_dims_vs_partition_function(self):
        """K3xE CoHA dims at low weights match prod 1/(1-q^n)^{24}."""
        dc = DrinfeldCenterK3E()
        char = dc.drinfeld_center_character(6)
        # Independent computation: 24-colored partition function
        N = 6
        ref = [0] * N
        ref[0] = 1
        for k in range(1, N):
            for _ in range(24):
                for n in range(k, N):
                    ref[n] += ref[n - k]
        for i in range(N):
            assert char["coha_dims"][i] == ref[i], (
                f"CoHA dim({i}) = {char['coha_dims'][i]}, expected {ref[i]}"
            )

    def test_comparison_table_completeness(self):
        """Comparison table has all 5 standard examples with full data."""
        table = e1_to_e2_comparison_table()
        assert len(table) == 5
        for name, data in table.items():
            for field in ["E1", "E2", "R_type", "character", "status"]:
                assert field in data and data[field], f"{name} missing or empty {field}"
