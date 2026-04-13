r"""Tests for the sl_2 chiral coproduct engine: breaking the abelian barrier.

THEOREM (CONDITIONAL on CY-A_3): The affine Yangian Y(sl_2_hat) arises from
the CY3-to-chiral functor applied to the A_1 McKay quiver (= resolved conifold
= C^2/Z_2 x C). The matrix-valued structure function g_{ij}(z), with
g_{01}(z) = 1/g_{00}(z), encodes the non-abelian Cartan data C_{01} = -2.

STATUS: The CoHA / shuffle algebra structure is PROVED (Schiffmann-Vasserot,
Rapcak-Soibelman-Yang-Zhao). The identification with the chiral algebra via
the functor Phi is part of the d=3 programme (CY-A_3, conjectural).

Multi-path verification:
    Path 1:  Structure function matrix entries g_{ij}(z) (5 tests)
    Path 2:  Inversion relation g_{00}*g_{01} = 1 (4 tests)
    Path 3:  Unitarity g_{ij}(z)*g_{ij}(-z) = 1 (3 tests)
    Path 4:  Laurent expansion coefficients (4 tests)
    Path 5:  Shuffle product at charges (1,0)x(0,1) (3 tests)
    Path 6:  Non-commutativity e_0*e_1 != e_1*e_0 (1 test)
    Path 7:  Same-node product symmetrization (2 tests)
    Path 8:  Serre relation at charge (2,1) (5 test points)
    Path 9:  Coproduct symbolic structure (2 tests)
    Path 10: Coproduct compatibility with exchange relation (1 test)
    Path 11: R-matrix scalar values (4 tests)
    Path 12: R-matrix cross-inversion R^{00}*R^{01} = 1 (4 tests)
    Path 13: R-matrix unitarity R(z)*R(-z) = 1 (4 tests)
    Path 14: Scalar YBE all node combinations (8 tests)
    Path 15: 4x4 R-matrix YBE (3 tests)
    Path 16: gl_1 vs sl_2 comparison: what is genuinely new (1 test)
    Path 17: Full verification suite (1 test)

Ground truth:
    - Cartan matrix A_1^{(1)}: C = ((2,-2),(-2,2))
    - g_{00}(z) = (z-h1)(z-h2)(z-h3)/((z+h1)(z+h2)(z+h3)) with h1+h2+h3=0
    - g_{01}(z) = 1/g_{00}(z) (from C_{01}=-2)
    - Expansion: phi^{00}_0=1, phi^{00}_1=phi^{00}_2=0, phi^{00}_3=-2*sigma_3
    - Serre: Sym_{z1,z2}[e_0(z1), [e_0(z2), e_1(w)]] = 0

Manuscript references:
    Vol III, Part III: CY landscape, conifold functor chain
    Vol III, Part IV: R-matrix from chart transitions
    conifold_e1_full_chain.py: E_1 functor chain for conifold
    affine_yangian_e1_cy3.py: Y(gl_hat_1) structure function
"""

import pytest
from fractions import Fraction

from compute.lib.sl2_chiral_coproduct_engine import (
    # Cartan data
    CARTAN_A1,
    cartan_entry,
    num_arrows,
    # Structure function
    StructureFunction,
    # Shuffle algebra
    ShuffleElement,
    ShuffleAlgebra,
    # Coproduct
    DrinfeldCoproduct,
    # R-matrix
    RMatrix,
    # Comparison
    gl1_vs_sl2_comparison,
    # Comprehensive
    sl2_coproduct_full_verification,
)


# ================================================================
# 1. CARTAN DATA
# ================================================================

class TestCartanData:
    """Verify the A_1^{(1)} Cartan matrix."""

    def test_cartan_diagonal(self):
        """Diagonal entries C_{ii} = 2."""
        # VERIFIED [DC] structural property [LT] Kac-Moody theory
        assert cartan_entry(0, 0) == 2
        assert cartan_entry(1, 1) == 2

    def test_cartan_off_diagonal(self):
        """Off-diagonal entries C_{ij} = -2 for A_1."""
        # VERIFIED [DC] structural property [LT] A_1^{(1)} Dynkin data
        assert cartan_entry(0, 1) == -2
        assert cartan_entry(1, 0) == -2

    def test_cartan_symmetry(self):
        """Cartan matrix is symmetric for A_1^{(1)}."""
        assert cartan_entry(0, 1) == cartan_entry(1, 0)

    def test_arrows_cross_node(self):
        """2 arrows between distinct nodes of A_1 McKay quiver."""
        assert num_arrows(0, 1) == 2
        assert num_arrows(1, 0) == 2

    def test_arrows_same_node(self):
        """No self-loops in the A_1 McKay quiver (before framing)."""
        assert num_arrows(0, 0) == 0
        assert num_arrows(1, 1) == 0

    def test_cartan_determinant_zero(self):
        """det(C) = 0 for affine Cartan matrix (null vector exists)."""
        det = CARTAN_A1[0][0] * CARTAN_A1[1][1] - CARTAN_A1[0][1] * CARTAN_A1[1][0]
        # VERIFIED [DC] affine property [LT] affine Lie algebra theory
        assert det == 0


# ================================================================
# 2. STRUCTURE FUNCTION
# ================================================================

class TestStructureFunction:
    """Verify the matrix-valued structure function g_{ij}(z)."""

    @pytest.fixture
    def sf(self):
        return StructureFunction()

    @pytest.fixture
    def sf_generic(self):
        """Generic parameters h1=2, h2=-1, h3=-1."""
        return StructureFunction(h1=Fraction(2), h2=Fraction(-1))

    def test_cy_condition(self, sf):
        """CY condition h1+h2+h3 = 0."""
        # VERIFIED [DC] constraint [LT] Calabi-Yau condition
        assert sf.h1 + sf.h2 + sf.h3 == 0

    def test_cy_condition_generic(self, sf_generic):
        """CY condition for generic parameters."""
        sf = sf_generic
        assert sf.h1 + sf.h2 + sf.h3 == 0

    def test_g_base_at_infinity(self, sf):
        """g_base(z) -> 1 as z -> infinity (leading coefficient)."""
        # For large z, g(z) ~ z^3/z^3 = 1
        g_val = sf.g_base(Fraction(1000))
        # Should be very close to 1
        assert abs(g_val - 1) < Fraction(1, 100)

    def test_same_node_equals_base(self, sf):
        """g_{00}(z) = g_base(z) (same-node is the base function)."""
        z = Fraction(3)
        assert sf.g(0, 0, z) == sf.g_base(z)
        assert sf.g(1, 1, z) == sf.g_base(z)

    def test_cross_node_is_inverse(self, sf):
        """g_{01}(z) = 1/g_{00}(z) (the key non-abelian relation)."""
        z = Fraction(3)
        g00 = sf.g(0, 0, z)
        g01 = sf.g(0, 1, z)
        # VERIFIED [DC] structural property [LT] Cartan matrix inversion
        assert g00 * g01 == Fraction(1)

    def test_inversion_multiple_points(self, sf):
        """g_{00}(z) * g_{01}(z) = 1 at multiple z values."""
        for z_val in [Fraction(2), Fraction(3), Fraction(5), Fraction(7),
                      Fraction(11), Fraction(13)]:
            result = sf.verify_inversion(z_val)
            assert result["is_one"], f"Inversion failed at z={z_val}"

    def test_inversion_generic_params(self, sf_generic):
        """Inversion holds for generic CY parameters."""
        for z_val in [Fraction(3), Fraction(7), Fraction(11)]:
            result = sf_generic.verify_inversion(z_val)
            assert result["is_one"], f"Inversion failed at z={z_val}"

    def test_unitarity_same_node(self, sf):
        """g_{00}(z) * g_{00}(-z) = 1."""
        z = Fraction(3)
        g_z = sf.g(0, 0, z)
        g_neg_z = sf.g(0, 0, -z)
        # VERIFIED [DC] unitarity [LT] g(-z) = 1/g(z) from CY symmetry
        assert g_z * g_neg_z == Fraction(1)

    def test_unitarity_cross_node(self, sf):
        """g_{01}(z) * g_{01}(-z) = 1."""
        z = Fraction(5)
        g_z = sf.g(0, 1, z)
        g_neg_z = sf.g(0, 1, -z)
        assert g_z * g_neg_z == Fraction(1)

    def test_unitarity_all_nodes(self, sf):
        """Unitarity g_{ij}(z)*g_{ij}(-z)=1 for all i,j."""
        z = Fraction(7)
        results = sf.verify_unitarity(z)
        for key, val in results.items():
            assert val["is_one"], f"Unitarity failed for {key}"

    def test_symmetry_g01_g10(self, sf):
        """g_{01}(z) = g_{10}(z) (Cartan symmetry C_{01}=C_{10})."""
        z = Fraction(4)
        assert sf.g(0, 1, z) == sf.g(1, 0, z)

    def test_node_symmetry_g00_g11(self, sf):
        """g_{00}(z) = g_{11}(z) (both diagonal nodes are equivalent)."""
        z = Fraction(6)
        assert sf.g(0, 0, z) == sf.g(1, 1, z)


# ================================================================
# 3. EXPANSION COEFFICIENTS
# ================================================================

class TestExpansionCoefficients:
    """Verify Laurent expansion of g_{ij}(z) at z=infinity."""

    @pytest.fixture
    def sf(self):
        return StructureFunction()

    def test_same_node_leading(self, sf):
        """phi^{00}_0 = 1 (leading coefficient)."""
        phi = sf.g_expansion(0, 0, N=8)
        assert phi[0] == Fraction(1)

    def test_same_node_phi1_phi2_zero(self, sf):
        """phi^{00}_1 = phi^{00}_2 = 0 (from CY condition sigma_1=0)."""
        phi = sf.g_expansion(0, 0, N=8)
        # VERIFIED [DC] vanishing [LT] CY condition h1+h2+h3=0
        assert phi[1] == Fraction(0)
        assert phi[2] == Fraction(0)

    def test_same_node_phi3(self, sf):
        """phi^{00}_3 = -2*sigma_3 (first non-trivial coefficient)."""
        phi = sf.g_expansion(0, 0, N=8)
        expected = -2 * sf.sigma3
        # VERIFIED [DC] coefficient value [LT] structure function expansion
        assert phi[3] == expected

    def test_cross_node_leading(self, sf):
        """phi^{01}_0 = 1 (leading coefficient of inverse series)."""
        phi = sf.g_expansion(0, 1, N=8)
        assert phi[0] == Fraction(1)

    def test_cross_node_phi1_phi2_zero(self, sf):
        """phi^{01}_1 = phi^{01}_2 = 0."""
        phi = sf.g_expansion(0, 1, N=8)
        assert phi[1] == Fraction(0)
        assert phi[2] == Fraction(0)

    def test_cross_node_phi3(self, sf):
        """phi^{01}_3 = +2*sigma_3 (opposite sign from same-node!)."""
        phi = sf.g_expansion(0, 1, N=8)
        expected = 2 * sf.sigma3
        # VERIFIED [DC] sign flip [LT] g_{01} = 1/g_{00} gives opposite phi_3
        assert phi[3] == expected

    def test_expansion_product_is_one(self, sf):
        """Product of same-node and cross-node expansions = [1, 0, 0, ...].

        This is the expansion-level verification of g_{00}*g_{01} = 1.
        """
        phi_00 = sf.g_expansion(0, 0, N=8)
        phi_01 = sf.g_expansion(0, 1, N=8)
        N = 8

        # Multiply the two power series
        product = [Fraction(0)] * N
        for k in range(N):
            for j in range(k + 1):
                product[k] += phi_00[j] * phi_01[k - j]

        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0), (
                f"Product coefficient at z^{{-{k}}} = {product[k]}, expected 0"
            )


# ================================================================
# 4. SHUFFLE PRODUCT (CoHA)
# ================================================================

class TestShuffleProduct:
    """Verify the CoHA shuffle product for the A_1 McKay quiver."""

    @pytest.fixture
    def sa(self):
        return ShuffleAlgebra()

    def test_e0_e1_is_g01(self, sa):
        """(e_0 * e_1)(z,w) = g_{01}(z-w)."""
        z, w = Fraction(3), Fraction(7)
        product = sa.product_e0_e1(z, w)
        expected = sa.sf.g(0, 1, z - w)
        assert product == expected

    def test_e1_e0_is_g10(self, sa):
        """(e_1 * e_0)(w,z) = g_{10}(w-z)."""
        z, w = Fraction(3), Fraction(7)
        product = sa.product_e1_e0(w, z)
        expected = sa.sf.g(1, 0, w - z)
        assert product == expected

    def test_noncommutativity(self, sa):
        """e_0 * e_1 != e_1 * e_0 (the shuffle product is non-commutative).

        This is the FUNDAMENTAL non-abelian feature. In gl_1, the single
        generator e commutes with itself under the shuffle product (after
        symmetrization). In sl_2, two different generators do NOT commute.

        Compare: (e_0*e_1)(z,w) = g_{01}(z-w) vs (e_1*e_0)(w,z) = g_{10}(w-z).
        Since g_{10}(w-z) = g_{01}(w-z) = g_{01}(-(z-w)) = 1/g_{01}(z-w),
        these are reciprocals, hence unequal (for z != w away from poles).
        """
        z, w = Fraction(3), Fraction(7)
        p1 = sa.product_e0_e1(z, w)   # g_{01}(z-w)
        p2 = sa.product_e1_e0(w, z)   # g_{10}(w-z) = 1/g_{01}(z-w)
        # VERIFIED [DC] non-commutativity [LT] g_{01}(z-w) != 1/g_{01}(z-w)
        assert p1 != p2
        # Cross-check: they are reciprocals
        assert p1 * p2 == Fraction(1)

    def test_exchange_relation(self, sa):
        """e_0*e_1 / e_1*e_0 = g_{01}(z-w) / g_{10}(w-z) = g_{01}(z-w)^2.

        The exchange relation: e_0(z)e_1(w) = [g_{01}(z-w)/g_{10}(w-z)] e_1(w)e_0(z).

        Since g_{10}(w-z) = g_{01}(w-z) (by C_{01}=C_{10}) and g_{01}(-u) = 1/g_{01}(u),
        the ratio is g_{01}(z-w) / g_{01}(-(z-w)) = g_{01}(z-w)^2.
        """
        z, w = Fraction(3), Fraction(7)
        e0e1 = sa.product_e0_e1(z, w)
        e1e0 = sa.product_e1_e0(w, z)
        ratio = e0e1 / e1e0
        expected = sa.sf.g(0, 1, z - w) ** 2
        assert ratio == expected

    def test_same_node_product_symmetrization(self, sa):
        """e_0*e_0 is symmetrized: (e_0*e_0)(z1,z2) = g_{00}(z1-z2) + g_{00}(z2-z1)."""
        z1, z2 = Fraction(3), Fraction(7)
        product = sa.product_e0_e0(z1, z2)
        expected = sa.sf.g(0, 0, z1 - z2) + sa.sf.g(0, 0, z2 - z1)
        assert product == expected

    def test_same_node_product_unitarity(self, sa):
        """e_0*e_0 uses g_{00}(-z)=1/g_{00}(z), so product = g+1/g."""
        z1, z2 = Fraction(3), Fraction(7)
        g_val = sa.sf.g(0, 0, z1 - z2)
        product = sa.product_e0_e0(z1, z2)
        expected = g_val + Fraction(1) / g_val
        assert product == expected

    def test_e0_e0_symmetric(self, sa):
        """(e_0*e_0)(z1,z2) = (e_0*e_0)(z2,z1) (symmetrization)."""
        z1, z2 = Fraction(3), Fraction(7)
        p12 = sa.product_e0_e0(z1, z2)
        p21 = sa.product_e0_e0(z2, z1)
        assert p12 == p21

    def test_e1_e1_equals_e0_e0(self, sa):
        """(e_1*e_1)(z1,z2) = (e_0*e_0)(z1,z2) by A_1 node symmetry."""
        z1, z2 = Fraction(3), Fraction(7)
        p00 = sa.product_e0_e0(z1, z2)
        p11 = sa.product_e1_e1(z1, z2)
        assert p00 == p11


# ================================================================
# 5. SERRE RELATION
# ================================================================

class TestSerreRelation:
    """Verify the quantum Serre relation at charge (2,1)."""

    @pytest.fixture
    def sa(self):
        return ShuffleAlgebra()

    @pytest.fixture
    def sa_generic(self):
        """Generic CY parameters."""
        sf = StructureFunction(h1=Fraction(2), h2=Fraction(-1))
        return ShuffleAlgebra(sf)

    def test_serre_default_params(self, sa):
        """Serre relation vanishes at default parameters h1=1, h2=-1/2."""
        result = sa.verify_serre_relation()
        # VERIFIED [DC] Serre vanishing [LT] quantum group Serre relation
        assert result["serre_relation_holds"]

    def test_serre_generic_params(self, sa_generic):
        """Serre relation vanishes at generic parameters h1=2, h2=-1."""
        result = sa_generic.verify_serre_relation()
        assert result["serre_relation_holds"]

    def test_serre_individual_points(self, sa):
        """Check Serre vanishing at each test point individually."""
        test_points = [
            (Fraction(3), Fraction(7), Fraction(5)),
            (Fraction(2), Fraction(11), Fraction(4)),
            (Fraction(1), Fraction(6), Fraction(3)),
            (Fraction(10), Fraction(3), Fraction(7)),
            (Fraction(5), Fraction(17), Fraction(11)),
        ]
        for z1, z2, w in test_points:
            val = sa.serre_integrand_at_21(z1, z2, w)
            assert val == Fraction(0), (
                f"Serre integrand nonzero at z1={z1}, z2={z2}, w={w}: {val}"
            )

    def test_serre_charge(self, sa):
        """Serre relation is at charge (2,1) = 2*gamma_0 + 1*gamma_1."""
        result = sa.verify_serre_relation()
        assert result["charge"] == "(2, 1)"

    def test_serre_cartan_entry(self, sa):
        """Serre uses C_{01} = -2 (determines 3 iterations)."""
        result = sa.verify_serre_relation()
        assert result["cartan_entry"] == "C_{01} = -2"

    def test_serre_additional_points(self, sa):
        """Serre at additional test points for robustness."""
        extra_points = [
            (Fraction(13), Fraction(19), Fraction(7)),
            (Fraction(4), Fraction(9), Fraction(2)),
            (Fraction(6), Fraction(14), Fraction(8)),
        ]
        result = sa.verify_serre_relation(test_points=extra_points)
        assert result["serre_relation_holds"]


# ================================================================
# 6. COPRODUCT
# ================================================================

class TestDrinfeldCoproduct:
    """Verify the Drinfeld coproduct for Y(sl_2_hat)."""

    @pytest.fixture
    def dc(self):
        return DrinfeldCoproduct()

    def test_e0_coproduct_formula(self, dc):
        """Delta_z(e_0) has the correct symbolic form."""
        result = dc.coproduct_e0_symbolic()
        assert "psi_0^L" in result["formula"]
        assert "e_{0,0}^R" in result["formula"]

    def test_e1_coproduct_formula(self, dc):
        """Delta_z(e_1) has the correct symbolic form."""
        result = dc.coproduct_e1_symbolic()
        assert "psi_1^L" in result["formula"]
        assert "e_{1,0}^R" in result["formula"]

    def test_coproduct_non_primitive(self, dc):
        """The sl_2 coproduct is non-primitive (Cartan-weighted)."""
        result = dc.coproduct_e0_symbolic()
        assert "NOT primitive" in result["key_difference"]

    def test_coproduct_compatibility(self, dc):
        """Coproduct compatible with exchange relation."""
        result = dc.coproduct_cross_check(Fraction(1))
        assert result["compatible"]

    def test_gl1_comparison(self, dc):
        """The gl_1 comparison is present and meaningful."""
        result = dc.coproduct_e0_symbolic()
        assert "gl_1" in result["gl1_comparison"]
        assert "primitive" in result["gl1_comparison"]


# ================================================================
# 7. R-MATRIX
# ================================================================

class TestRMatrix:
    """Verify the R-matrix of Y(sl_2_hat)."""

    @pytest.fixture
    def rm(self):
        return RMatrix()

    def test_same_node_R_equals_g00(self, rm):
        """R^{00}(z) = g_{00}(z) (same-node R-matrix)."""
        z = Fraction(3)
        R00 = rm.R_scalar(0, 0, z)
        g00 = rm.sf.g(0, 0, z)
        assert R00 == g00

    def test_cross_node_R_equals_g01(self, rm):
        """R^{01}(z) = g_{01}(z) = 1/g_{00}(z) (cross-node R-matrix)."""
        z = Fraction(3)
        R01 = rm.R_scalar(0, 1, z)
        g01 = rm.sf.g(0, 1, z)
        assert R01 == g01

    def test_cross_inversion(self, rm):
        """R^{00}(z) * R^{01}(z) = 1 (the non-abelian signature)."""
        for z_val in [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]:
            result = rm.verify_cross_inversion(z_val)
            # VERIFIED [DC] R-matrix inversion [LT] Cartan-based R^{ij}
            assert result["is_one"]

    def test_unitarity_same_node(self, rm):
        """R^{00}(z) * R^{00}(-z) = 1."""
        z = Fraction(5)
        result = rm.verify_unitarity(0, 0, z)
        assert result["is_one"]

    def test_unitarity_cross_node(self, rm):
        """R^{01}(z) * R^{01}(-z) = 1."""
        z = Fraction(5)
        result = rm.verify_unitarity(0, 1, z)
        assert result["is_one"]

    def test_unitarity_all_nodes(self, rm):
        """Unitarity holds for all node combinations."""
        for z_val in [Fraction(2), Fraction(3), Fraction(5)]:
            for i in range(2):
                for j in range(2):
                    result = rm.verify_unitarity(i, j, z_val)
                    assert result["is_one"], (
                        f"Unitarity failed for R^{i}{j} at z={z_val}"
                    )

    def test_ybe_scalar_all_nodes(self, rm):
        """Scalar YBE for all 8 node combinations."""
        z1, z2, z3 = Fraction(3), Fraction(7), Fraction(11)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result = rm.verify_ybe_scalar(z1, z2, z3, i, j, k)
                    assert result["ybe_holds"], (
                        f"YBE failed for nodes ({i},{j},{k})"
                    )

    def test_ybe_4x4(self, rm):
        """Full 4x4 R-matrix YBE."""
        result = rm.verify_ybe_2x2(Fraction(3), Fraction(7), Fraction(11))
        assert result["ybe_holds"]

    def test_ybe_4x4_different_params(self, rm):
        """4x4 YBE at different spectral parameters."""
        result = rm.verify_ybe_2x2(Fraction(2), Fraction(5), Fraction(13))
        assert result["ybe_holds"]

    def test_ybe_4x4_close_params(self, rm):
        """4x4 YBE with close spectral parameters."""
        result = rm.verify_ybe_2x2(Fraction(10), Fraction(11), Fraction(12))
        assert result["ybe_holds"]

    def test_R_node_symmetry(self, rm):
        """R^{00} = R^{11} and R^{01} = R^{10} by A_1 node symmetry."""
        z = Fraction(4)
        assert rm.R_scalar(0, 0, z) == rm.R_scalar(1, 1, z)
        assert rm.R_scalar(0, 1, z) == rm.R_scalar(1, 0, z)


# ================================================================
# 8. gl_1 vs sl_2 COMPARISON
# ================================================================

class TestComparison:
    """Verify the systematic gl_1 vs sl_2 comparison."""

    def test_comparison_runs(self):
        """The comparison function runs without error."""
        result = gl1_vs_sl2_comparison()
        assert "summary" in result

    def test_new_features_listed(self):
        """All genuinely new sl_2 features are identified."""
        result = gl1_vs_sl2_comparison()
        new = result["summary"]["what_is_new"]
        assert len(new) >= 5
        # Check key features are listed
        features_text = " ".join(new).lower()
        assert "matrix" in features_text
        assert "serre" in features_text
        assert "inversion" in features_text or "inverse" in features_text

    def test_serre_in_comparison(self):
        """Serre relation verified in comparison."""
        result = gl1_vs_sl2_comparison()
        assert result["serre_relation"]["serre_relation_holds"]

    def test_noncommutativity_in_comparison(self):
        """Non-commutativity demonstrated in comparison."""
        result = gl1_vs_sl2_comparison()
        assert result["shuffle_product"]["non_commutative"]


# ================================================================
# 9. COMPREHENSIVE VERIFICATION
# ================================================================

class TestComprehensive:
    """Run the full sl_2 coproduct verification suite."""

    @pytest.fixture(scope="class")
    def full_results(self):
        return sl2_coproduct_full_verification()

    def test_all_inversions(self, full_results):
        """All g_{00}*g_{01}=1 checks pass."""
        assert full_results["all_inversions_hold"]

    def test_serre_verified(self, full_results):
        """Serre relation verified in full suite."""
        assert full_results["serre_relation"]["serre_relation_holds"]

    def test_ybe_all_hold(self, full_results):
        """All YBE checks pass."""
        assert full_results["ybe_all_hold"]

    def test_ybe_4x4_in_full(self, full_results):
        """4x4 YBE passes in full suite."""
        assert full_results["ybe_4x4"]["ybe_holds"]

    def test_abelian_barrier_broken(self, full_results):
        """The summary confirms the abelian barrier is broken."""
        assert full_results["summary"]["abelian_barrier_broken"]

    def test_coha_noncommutative(self, full_results):
        """CoHA product is non-commutative."""
        assert full_results["coha_product"]["non_commutative"]

    def test_expansion_same_node(self, full_results):
        """Same-node expansion starts with phi_0=1."""
        assert full_results["expansion_same_node"][0] == "1"

    def test_expansion_cross_node(self, full_results):
        """Cross-node expansion starts with phi_0=1."""
        assert full_results["expansion_cross_node"][0] == "1"

    def test_key_result_stated(self, full_results):
        """The key result is correctly stated in summary."""
        assert "1/g_{00}" in full_results["summary"]["key_result"]

    def test_genuinely_new_features(self, full_results):
        """At least 5 genuinely new features identified."""
        assert len(full_results["summary"]["genuinely_new_features"]) >= 5
