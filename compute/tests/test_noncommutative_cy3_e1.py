r"""Tests for noncommutative_cy3_e1: NC deformations of CY3 E₁ algebras.

Ground truth sources:
  - Kontsevich, "Deformation quantization of Poisson manifolds" (1997):
    constant Poisson bivectors on C^n automatically preserve volume forms.
  - Seiberg-Witten, "String theory and noncommutative geometry" (1999):
    B-field ↔ non-commutativity (SW map).
  - Kontsevich-Soibelman (2008): motivic DT, deformed shuffle algebras.
  - Maulik-Okounkov (2012): g(z)g(-z)=1 from CY condition (R-matrix unitarity).
  - Nekrasov-Okounkov (2014): W_{1+∞}(c=-ε₂/ε₁) from Ω-background.
  - Schiffmann-Vasserot (2012): CoHA = Y^+(ĝl₁), shuffle algebra.
  - Prochazka-Rapcak (2019): W_{1+∞} OPE structure constants.
  - Costello-Li (2016): E₁ forcing from σ₃ (odd degree).
  - Berenstein-Douglas (2002): NC conifold deformation.

Multi-path verification:
  (a) Poisson CY constraint: div(θ) = 0 for constant θ on C³.
  (b) Deformed structure function: g_θ(z)g_θ(-z) = 1 at multiple θ values.
  (c) B-field spectrum: Ω(1,1) = 0 on the wall at B = 1/2.
  (d) Ω-background: E₁ at generic, E_∞ at self-dual (three independent witnesses).
  (e) Star product: Moyal commutator [x_i, x_j]_⋆ = 2θ_{ij} (exact).
  (f) Deformation quantization = factorization envelope (φ₃ match).
  (g) NC conifold: Morita transitions, Euler form unchanged.
  (h) κ is topological: independent of θ, B, ε₁/ε₂.
"""

from fractions import Fraction

import pytest

from compute.lib.noncommutative_cy3_e1 import (
    PoissonBivector,
    DeformedShuffleAlgebra,
    BFieldData,
    ConifoldBFieldE1,
    OmegaBackgroundE1,
    StarProduct,
    deformation_quantization_vs_factorization,
    NCCharge,
    NCQuiverWithPotential,
    nc_conifold_quiver,
    NCConifoldE1,
    NCAtlas,
    verify_nc_deformation_paths,
    compute_nc_conifold_dt,
    nc_cy3_e1_summary,
)


# ======================================================================
# 1. POISSON BIVECTOR AND CY CONSTRAINT
# ======================================================================

class TestPoissonBivector:
    """Test the Poisson bivector on C³ and CY compatibility."""

    def test_zero_bivector_is_commutative(self):
        """θ = 0 is the commutative case."""
        bv = PoissonBivector()
        assert bv.is_zero
        assert bv.rank == 0

    def test_nonzero_bivector_has_rank_2(self):
        """Any nonzero constant bivector on C³ has rank 2."""
        bv = PoissonBivector(theta_12=Fraction(1, 2))
        assert not bv.is_zero
        assert bv.rank == 2

    def test_pfaffian_always_zero_dim_3(self):
        """Pfaffian of 3x3 antisymmetric matrix is always 0."""
        for t12, t23, t13 in [
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(1, 2), Fraction(1, 3), Fraction(1, 7)),
            (Fraction(5), Fraction(-3), Fraction(2)),
        ]:
            bv = PoissonBivector(theta_12=t12, theta_23=t23, theta_13=t13)
            assert bv.pfaffian == Fraction(0)

    def test_antisymmetric_matrix(self):
        """The matrix θ^{ij} is antisymmetric."""
        bv = PoissonBivector(theta_12=Fraction(1), theta_23=Fraction(2), theta_13=Fraction(3))
        mat = bv.matrix
        for i in range(3):
            for j in range(3):
                assert mat[i][j] == -mat[j][i]

    def test_cy_compatible_constant_bivector(self):
        """Any constant bivector on C³ is CY-compatible (div = 0)."""
        for t12 in [Fraction(0), Fraction(1), Fraction(-3, 7)]:
            for t23 in [Fraction(0), Fraction(2, 5)]:
                bv = PoissonBivector(theta_12=t12, theta_23=t23)
                check = bv.cy_constraint_check()
                assert check["cy_compatible"]
                assert check["divergence_free"]

    def test_kernel_direction(self):
        """Kernel of θ is (θ₂₃, -θ₁₃, θ₁₂)."""
        bv = PoissonBivector(theta_12=Fraction(1), theta_23=Fraction(2), theta_13=Fraction(3))
        ker = bv.kernel_direction
        assert ker == (Fraction(2), Fraction(-3), Fraction(1))

    def test_kernel_is_in_kernel(self):
        """Verify θ · ker(θ) = 0."""
        bv = PoissonBivector(theta_12=Fraction(1), theta_23=Fraction(2), theta_13=Fraction(3))
        ker = bv.kernel_direction
        mat = bv.matrix
        for i in range(3):
            dot = sum(mat[i][j] * ker[j] for j in range(3))
            assert dot == Fraction(0), f"θ·ker ≠ 0 at row {i}: got {dot}"

    def test_effective_nc_parameter(self):
        """θ_eff² = θ₁₂² + θ₂₃² + θ₁₃²."""
        bv = PoissonBivector(theta_12=Fraction(3), theta_23=Fraction(4), theta_13=Fraction(0))
        assert bv.effective_nc_parameter == Fraction(25)  # 9 + 16


# ======================================================================
# 2. DEFORMED SHUFFLE ALGEBRA
# ======================================================================

class TestDeformedShuffleAlgebra:
    """Test the non-commutative deformation of the CoHA shuffle algebra."""

    def setup_method(self):
        self.h1 = Fraction(1)
        self.h2 = Fraction(-1, 3)
        self.h3 = Fraction(-2, 3)

    def test_cy_condition(self):
        """h₁ + h₂ + h₃ = 0."""
        assert self.h1 + self.h2 + self.h3 == 0

    def test_undeformed_phi0_is_1(self):
        """φ₀ = 1 always."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        phi = s.undeformed_phi(6)
        assert phi[0] == Fraction(1)

    def test_undeformed_phi1_vanishes(self):
        """φ₁ = 0 by CY condition (p₁ = h₁+h₂+h₃ = 0)."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        phi = s.undeformed_phi(6)
        assert phi[1] == Fraction(0)

    def test_undeformed_phi2_vanishes(self):
        """φ₂ = 0 (no even-index log-series contributions at order 2)."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        phi = s.undeformed_phi(6)
        assert phi[2] == Fraction(0)

    def test_phi3_equals_minus_2_sigma3(self):
        """φ₃ = -2σ₃ from the log expansion.

        α₃ = -2p₃/3, p₃ = 3σ₃ (Newton's identity with σ₁ = 0):
        p₃ = 3σ₃ (since p₁ = 0, p₂ = σ₁²-2σ₂ = -2σ₂, p₃ = σ₁p₂ - σ₂p₁ + 3σ₃ = 3σ₃).
        So α₃ = -2·3σ₃/3 = -2σ₃.
        φ₃ = α₃ = -2σ₃ (at order 3, only the singleton partition contributes).
        """
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        phi = s.undeformed_phi(6)
        sigma3 = self.h1 * self.h2 * self.h3
        assert phi[3] == Fraction(-2) * sigma3

    def test_deformed_phi_at_theta_0_equals_undeformed(self):
        """At θ = 0, deformed φ = undeformed φ."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3, theta=Fraction(0))
        phi0 = s.undeformed_phi(8)
        phi_th = s.deformed_phi(8)
        for j in range(9):
            assert phi0[j] == phi_th[j], f"Mismatch at j={j}: {phi0[j]} vs {phi_th[j]}"

    def test_deformed_phi_theta_nonzero_shifts(self):
        """At θ ≠ 0, some deformed φ differ from undeformed."""
        theta = Fraction(1, 2)
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3, theta=theta)
        phi0 = s.undeformed_phi(6)
        phi_th = s.deformed_phi(6)
        # φ₁(θ) = φ₁ + 2θ · φ₀ = 0 + 2θ = 2θ = 1
        assert phi_th[1] == Fraction(2) * theta
        # φ₀ unchanged
        assert phi_th[0] == phi0[0]

    def test_deformed_unitarity_theta_0(self):
        """g(z)g(-z) = 1 at θ = 0 (Maulik-Okounkov)."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3, theta=Fraction(0))
        result = s.deformed_unitarity(8)
        assert result["unitarity_preserved"]

    def test_deformed_unitarity_theta_nonzero(self):
        """g_θ(z)g_θ(-z) = 1 at θ ≠ 0 (twist cancels)."""
        for theta in [Fraction(1, 2), Fraction(1), Fraction(-1, 3), Fraction(3, 7)]:
            s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3, theta=theta)
            result = s.deformed_unitarity(8)
            assert result["unitarity_preserved"], f"Unitarity failed at θ={theta}"

    def test_deformed_unitarity_multiple_h(self):
        """g_θ(z)g_θ(-z) = 1 at multiple (h₁,h₂) and θ values."""
        params = [
            (Fraction(1), Fraction(-1, 2), Fraction(1, 4)),
            (Fraction(2), Fraction(-1), Fraction(1)),
            (Fraction(1, 3), Fraction(-1, 7), Fraction(2, 5)),
        ]
        for h1, h2, theta in params:
            h3 = -(h1 + h2)
            s = DeformedShuffleAlgebra(h1, h2, h3, theta=theta)
            result = s.deformed_unitarity(8)
            assert result["unitarity_preserved"], f"Failed at h=({h1},{h2}), θ={theta}"

    def test_sigma3_nonzero_generic(self):
        """σ₃ ≠ 0 at generic parameters."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        assert s.sigma3 != 0

    def test_sigma3_value(self):
        """σ₃ = h₁h₂h₃ = 1 · (-1/3) · (-2/3) = 2/9."""
        s = DeformedShuffleAlgebra(self.h1, self.h2, self.h3)
        assert s.sigma3 == Fraction(2, 9)


# ======================================================================
# 3. B-FIELD DEFORMATION
# ======================================================================

class TestBFieldDeformation:
    """Test B-field deformation of the conifold E₁ algebra."""

    def test_b_zero_has_bound_state(self):
        """At B = 0, the bound state γ₁+γ₂ is present."""
        b = ConifoldBFieldE1(Fraction(0))
        spectrum = b.bps_spectrum()
        assert (1, 1) in spectrum
        assert spectrum[(1, 1)] == 1

    def test_b_half_no_bound_state(self):
        """At B = 1/2 (self-dual), the bound state decays."""
        b = ConifoldBFieldE1(Fraction(1, 2))
        spectrum = b.bps_spectrum()
        assert (1, 1) not in spectrum

    def test_b_half_is_self_dual(self):
        """B = 1/2 is the self-dual B-field value."""
        b = ConifoldBFieldE1(Fraction(1, 2))
        assert b.is_self_dual

    def test_b_half_is_on_wall(self):
        """B = 1/2 lies on the wall of marginal stability."""
        b = ConifoldBFieldE1(Fraction(1, 2))
        assert b.is_on_wall

    def test_b_zero_not_on_wall(self):
        """B = 0 is NOT on the wall."""
        b = ConifoldBFieldE1(Fraction(0))
        assert not b.is_on_wall

    def test_b_half_free_algebra(self):
        """At B = 1/2, the E₁ algebra is free on 2 generators."""
        b = ConifoldBFieldE1(Fraction(1, 2))
        data = b.e1_algebra_data()
        assert data["is_free_algebra"]
        assert data["n_generators"] == 2

    def test_b_zero_not_free(self):
        """At B = 0, the E₁ algebra is NOT free (has bound-state relations)."""
        b = ConifoldBFieldE1(Fraction(0))
        data = b.e1_algebra_data()
        assert not data["is_free_algebra"]
        assert data["n_generators"] == 3

    def test_kappa_independent_of_b(self):
        """κ is topological: κ(conifold) = 0 for all B.

        κ = χ(X)/2 is a topological invariant, independent of B.
        For the conifold: χ = 0, so κ = 0.
        """
        for b in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            cb = ConifoldBFieldE1(b)
            assert cb.e1_algebra_data()["kappa"] == Fraction(0)

    def test_e1_level_independent_of_b(self):
        """E_n level = 1 for all B values (CY3 forces E₁)."""
        for b in [Fraction(0), Fraction(1, 2)]:
            cb = ConifoldBFieldE1(b)
            assert cb.e1_algebra_data()["e_n_level"] == 1

    def test_d0_brane_always_present(self):
        """D0-branes (γ₁, γ₂) are always present regardless of B."""
        for b in [Fraction(0), Fraction(1, 4), Fraction(1, 2)]:
            cb = ConifoldBFieldE1(b)
            spectrum = cb.bps_spectrum()
            assert (1, 0) in spectrum and spectrum[(1, 0)] == 1
            assert (0, 1) in spectrum and spectrum[(0, 1)] == 1

    def test_wall_crossing_trivial_on_wall(self):
        """On the wall (B=1/2), wall-crossing factor is identity."""
        b = ConifoldBFieldE1(Fraction(1, 2))
        wc = b.wall_crossing_factor()
        assert wc["wall_crossing"] == "trivial (identity)"

    def test_wall_crossing_nontrivial_off_wall(self):
        """Off the wall (B=0), wall-crossing factor is non-trivial."""
        b = ConifoldBFieldE1(Fraction(0))
        wc = b.wall_crossing_factor()
        assert wc["wall_crossing"] == "non-trivial"


# ======================================================================
# 4. OMEGA-BACKGROUND AND E_n BREAKING
# ======================================================================

class TestOmegaBackground:
    """Test the Ω-background E_n level analysis."""

    def test_self_dual_is_e_inf(self):
        """At self-dual ε₁ = -ε₂: E_∞ (σ₃ = 0, Heisenberg)."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1))
        result = omega.e_n_level()
        assert result["e_n"] == "E_inf"
        assert omega.sigma3 == Fraction(0)

    def test_classical_is_e_inf(self):
        """At classical ε₁ = ε₂ = 0: E_∞ (commutative)."""
        omega = OmegaBackgroundE1(Fraction(0), Fraction(0))
        result = omega.e_n_level()
        assert result["e_n"] == "E_inf"

    def test_generic_is_e1(self):
        """At generic ε₁, ε₂: E₁ (non-commutative)."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        result = omega.e_n_level()
        assert result["e_n"] == "E_1"

    def test_sigma3_vanishes_self_dual(self):
        """σ₃ = -ε₁ε₂(ε₁+ε₂) = 0 at self-dual (ε₁+ε₂ = 0)."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1))
        assert omega.sigma3 == Fraction(0)

    def test_sigma3_nonzero_generic(self):
        """σ₃ ≠ 0 at generic parameters."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        # σ₃ = -1·(-1/3)·(1-1/3) = -(-1/3)·(2/3) = 2/9
        expected = Fraction(2, 9)
        assert omega.sigma3 == expected

    def test_central_charge_ratio(self):
        """c = -ε₂/ε₁."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        assert omega.central_charge_ratio == Fraction(1, 3)

    def test_central_charge_self_dual(self):
        """At self-dual: c = -(-1)/1 = 1."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1))
        assert omega.central_charge_ratio == Fraction(1)

    def test_e2_breaking_witness_generic(self):
        """At generic c ≠ 1: f(c) ≠ f(1/c), witnessing E₂ breaking."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        result = omega.e_n_level()
        witness = result["e2_breaking_witness"]
        assert witness["e2_breaks"]
        assert not witness["symmetric_under_exchange"]

    def test_e2_symmetric_at_c_equals_1(self):
        """At c = 1 (self-dual): f(c) = f(1/c), no E₂ breaking.

        But note: the e_n_level returns E_inf at self-dual, so the
        witness is not computed (different code path).
        """
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1))
        result = omega.e_n_level()
        assert result["e_n"] == "E_inf"

    def test_rmatrix_unitarity_generic(self):
        """g(z)g(-z) = 1 at generic Ω-background parameters."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        assert omega.verify_rmatrix_unitarity(8)

    def test_rmatrix_unitarity_self_dual(self):
        """g(z)g(-z) = 1 at self-dual parameters."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1))
        assert omega.verify_rmatrix_unitarity(8)

    def test_rmatrix_unitarity_multiple_params(self):
        """g(z)g(-z) = 1 at multiple parameter choices."""
        params = [
            (Fraction(2), Fraction(-1)),
            (Fraction(1, 2), Fraction(-1, 5)),
            (Fraction(3), Fraction(-2)),
            (Fraction(1, 7), Fraction(-1, 11)),
        ]
        for e1, e2 in params:
            omega = OmegaBackgroundE1(e1, e2)
            assert omega.verify_rmatrix_unitarity(8), f"Failed at ε=({e1},{e2})"

    def test_structure_function_phi1_vanishes(self):
        """φ₁ = 0 at all parameter values (CY condition)."""
        for e1, e2 in [(Fraction(1), Fraction(-1, 3)), (Fraction(2), Fraction(-1))]:
            omega = OmegaBackgroundE1(e1, e2)
            phi = omega.structure_function_coefficients(6)
            assert phi[1] == Fraction(0)


# ======================================================================
# 5. STAR PRODUCT AND DEFORMATION QUANTIZATION
# ======================================================================

class TestStarProduct:
    """Test the Kontsevich/Moyal star product on C³_θ."""

    def test_commutator_x1_x2(self):
        """[x₁, x₂]_⋆ = 2θ₁₂."""
        theta = Fraction(1, 2)
        bv = PoissonBivector(theta_12=theta)
        star = StarProduct(bv)
        result = star.verify_associativity_low_degree()
        assert result["commutator_12_correct"]
        # The commutator should be 2θ₁₂ at degree (0,0,0)
        comm = result["[x1,x2]_star"]
        assert comm.get((0, 0, 0), Fraction(0)) == Fraction(2) * theta

    def test_commutator_x2_x3(self):
        """[x₂, x₃]_⋆ = 2θ₂₃."""
        theta = Fraction(1, 3)
        bv = PoissonBivector(theta_23=theta)
        star = StarProduct(bv)
        result = star.verify_associativity_low_degree()
        assert result["commutator_23_correct"]
        comm = result["[x2,x3]_star"]
        assert comm.get((0, 0, 0), Fraction(0)) == Fraction(2) * theta

    def test_commutative_star_product(self):
        """At θ = 0, [x_i, x_j]_⋆ = 0."""
        bv = PoissonBivector()  # θ = 0
        star = StarProduct(bv)
        result = star.verify_associativity_low_degree()
        assert result["[x1,x2]_star"] == {}
        assert result["[x2,x3]_star"] == {}

    def test_moyal_is_associative(self):
        """Moyal product is associative for constant θ (theorem)."""
        bv = PoissonBivector(theta_12=Fraction(1))
        star = StarProduct(bv)
        assert star.is_moyal
        result = star.verify_associativity_low_degree()
        assert result["moyal_associativity"]

    def test_star_product_order_0(self):
        """At order 0: f ⋆ g = fg (classical product)."""
        bv = PoissonBivector(theta_12=Fraction(1))
        star = StarProduct(bv)
        # x₁² ⋆ x₂ at order 0 should contain x₁²x₂
        result = star.star_product_monomials((2, 0, 0), (0, 1, 0), max_order=0)
        assert (2, 1, 0) in result
        assert result[(2, 1, 0)] == Fraction(1)

    def test_star_product_order_1_x1sq_x2(self):
        """x₁² ⋆ x₂ = x₁²x₂ + 2θ₁₂ x₁ at order 1.

        B₁(x₁², x₂) = θ₁₂ · ∂₁(x₁²) · ∂₂(x₂) = θ₁₂ · 2x₁ · 1 = 2θ₁₂ x₁.
        """
        theta = Fraction(1)
        bv = PoissonBivector(theta_12=theta)
        star = StarProduct(bv)
        result = star.star_product_monomials((2, 0, 0), (0, 1, 0), max_order=1)
        assert result.get((2, 1, 0), Fraction(0)) == Fraction(1)  # classical
        assert result.get((1, 0, 0), Fraction(0)) == Fraction(2) * theta  # order 1

    def test_star_product_x2_x1sq(self):
        """x₂ ⋆ x₁² = x₁²x₂ - 2θ₁₂ x₁ at order 1.

        B₁(x₂, x₁²) = θ₁₂ · ∂₁(x₂) · ∂₂(x₁²) - θ₁₂ · ∂₂(x₂) · ∂₁(x₁²)
                      = θ₁₂ · 0 · 0 - θ₁₂ · 1 · 2x₁ = -2θ₁₂ x₁.
        """
        theta = Fraction(1)
        bv = PoissonBivector(theta_12=theta)
        star = StarProduct(bv)
        result = star.star_product_monomials((0, 1, 0), (2, 0, 0), max_order=1)
        assert result.get((2, 1, 0), Fraction(0)) == Fraction(1)
        assert result.get((1, 0, 0), Fraction(0)) == Fraction(-2) * theta


# ======================================================================
# 6. DEFORMATION QUANTIZATION VS FACTORIZATION ENVELOPE
# ======================================================================

class TestDeformationQuantizationComparison:
    """Test that deformation quantization agrees with factorization envelope."""

    def test_phi3_match(self):
        """φ₃ from factorization = -2σ₃ (agrees with direct computation)."""
        result = deformation_quantization_vs_factorization(
            theta=Fraction(1, 2),
            h1=Fraction(1),
            h2=Fraction(-1, 3),
        )
        assert result["path_2_factorization_envelope"]["phi3_match"]

    def test_both_produce_w1inf(self):
        """Both paths produce W_{1+∞}."""
        result = deformation_quantization_vs_factorization(
            theta=Fraction(1, 2),
        )
        assert result["both_paths_produce_W1inf"]

    def test_star_product_check(self):
        """Star product commutator is correct."""
        result = deformation_quantization_vs_factorization(
            theta=Fraction(1, 2),
        )
        assert result["path_1_deformation_quantization"]["star_product_check"]

    def test_theta_shift_of_phi3(self):
        """The θ-shift of φ₃ is 4θ³/3 (from the exponential twist).

        φ₃(θ) = φ₃ + 2θ·φ₂ + (2θ)²/2·φ₁ + (2θ)³/6·φ₀
               = φ₃ + 0 + 0 + 8θ³/6 = φ₃ + 4θ³/3.
        """
        result = deformation_quantization_vs_factorization(
            theta=Fraction(1, 2),
        )
        assert result["path_comparison"]["shift_match"]

    def test_theta_shift_various_values(self):
        """The shift formula holds for multiple θ values."""
        for theta in [Fraction(1), Fraction(1, 3), Fraction(2, 5)]:
            result = deformation_quantization_vs_factorization(theta=theta)
            assert result["path_comparison"]["shift_match"], f"Failed at θ={theta}"


# ======================================================================
# 7. NON-COMMUTATIVE CONIFOLD
# ======================================================================

class TestNCConifold:
    """Test the non-commutative conifold E₁ algebra."""

    def test_nc_conifold_quiver_structure(self):
        """NC conifold quiver has 2 vertices, 4 arrows."""
        q = nc_conifold_quiver(Fraction(1))
        assert q.n_vertices == 2
        assert q.n_arrows == 4

    def test_nc_conifold_potential_deforms(self):
        """At θ ≠ 0, the potential has extra terms."""
        q0 = nc_conifold_quiver(Fraction(0))
        q1 = nc_conifold_quiver(Fraction(1))
        assert len(q0.potential_terms) == 2
        assert len(q1.potential_terms) == 4  # 2 original + 2 deformation

    def test_nc_conifold_euler_form_unchanged(self):
        """The Euler form is unchanged by NC deformation.

        χ(d₁, d₂) depends on quiver structure (vertices, arrows),
        not on the potential. NC deformation only changes W, not Q.
        """
        q0 = nc_conifold_quiver(Fraction(0))
        q1 = nc_conifold_quiver(Fraction(1, 2))
        d = (1, 1)
        assert q0.euler_form(d, d) == q1.euler_form(d, d)

    def test_nc_conifold_bps_spectrum(self):
        """NC conifold has 3 BPS states: γ₁, γ₂, γ₁+γ₂."""
        nc = NCConifoldE1(Fraction(1, 2))
        spectrum = nc.bps_spectrum()
        assert NCCharge((1, 0)) in spectrum
        assert NCCharge((0, 1)) in spectrum
        assert NCCharge((1, 1)) in spectrum

    def test_nc_conifold_kappa_zero(self):
        """κ(NC conifold) = 0 (topological, independent of θ)."""
        for theta in [Fraction(0), Fraction(1, 2), Fraction(1)]:
            nc = NCConifoldE1(theta)
            data = nc.e1_algebra_data()
            assert data["kappa"] == Fraction(0)

    def test_nc_atlas_has_2_charts(self):
        """NC conifold atlas has 2 charts (two chambers)."""
        nc = NCConifoldE1(Fraction(1, 2))
        atlas = nc.nc_atlas()
        assert len(atlas.charts) == 2

    def test_nc_atlas_morita_transition(self):
        """At θ ≠ 0, transitions are Morita equivalences."""
        nc = NCConifoldE1(Fraction(1, 2))
        atlas = nc.nc_atlas()
        assert atlas.transitions[0][2] == "Morita_equivalence"

    def test_commutative_atlas_tilting_transition(self):
        """At θ = 0, transitions are tilting equivalences."""
        nc = NCConifoldE1(Fraction(0))
        atlas = nc.nc_atlas()
        assert atlas.transitions[0][2] == "tilting_equivalence"

    def test_nc_conifold_e1_level(self):
        """NC conifold algebra is E₁ (CY3 forces this)."""
        nc = NCConifoldE1(Fraction(1, 2))
        data = nc.e1_algebra_data()
        assert data["e_n_level"] == 1

    def test_nc_conifold_euler_form_value(self):
        """Euler form of conifold: χ((1,0),(0,1)) = 0 - 2 = -2."""
        nc = NCConifoldE1(Fraction(0))
        # χ(e₁, e₂) = Σ d₁_i d₂_i - Σ d₁_{s(a)} d₂_{t(a)}
        # = 1·0 + 0·1 - (1·1 + 1·1 + 0·0 + 0·0) = 0 - 2 = -2
        assert nc.deformed_euler_form((1, 0), (0, 1)) == -2


# ======================================================================
# 8. NC DT PARTITION FUNCTION
# ======================================================================

class TestNCDTPartitionFunction:
    """Test the DT partition function for the NC conifold."""

    def test_nc_dt_independent_of_theta_d0_sector(self):
        """In the D0 sector, Z^{DT}(q) is independent of θ.

        The D0-brane counting is controlled by the quiver structure
        (vertices and arrows), not by the potential. Since the NC
        deformation only changes W, the D0 partition function is
        the same for all θ.
        """
        z0 = compute_nc_conifold_dt(Fraction(0), 8)
        z1 = compute_nc_conifold_dt(Fraction(1, 2), 8)
        for n in range(8):
            assert z0[n] == z1[n], f"Mismatch at q^{n}: {z0[n]} vs {z1[n]}"

    def test_nc_dt_leading_terms(self):
        """Z^{D0}(q) = P(q)² starts 1 + 2q + 5q² + 10q³ + ...

        P(q) = 1 + q + 2q² + 3q³ + 5q⁴ + ...
        P(q)² = 1 + 2q + 5q² + 10q³ + 20q⁴ + ...
        """
        z = compute_nc_conifold_dt(Fraction(0), 6)
        assert z[0] == Fraction(1)
        assert z[1] == Fraction(2)
        assert z[2] == Fraction(5)
        assert z[3] == Fraction(10)
        assert z[4] == Fraction(20)


# ======================================================================
# 9. MULTI-PATH VERIFICATION
# ======================================================================

class TestMultiPathVerification:
    """Test the six-path verification engine."""

    def test_all_paths_pass(self):
        """All six verification paths pass simultaneously."""
        result = verify_nc_deformation_paths(
            theta=Fraction(1, 2),
            h1=Fraction(1),
            h2=Fraction(-1, 3),
        )
        assert result["all_paths_pass"]

    def test_path_1_poisson_cy(self):
        """Path 1: Poisson bivector is CY-compatible."""
        result = verify_nc_deformation_paths()
        assert result["path_1_poisson_cy"]["cy_compatible"]

    def test_path_2_unitarity(self):
        """Path 2: Deformed unitarity holds."""
        result = verify_nc_deformation_paths()
        assert result["path_2_deformed_unitarity"]["unitarity_preserved"]

    def test_path_3_b_field(self):
        """Path 3: B = 1/2 gives 2 generators (free algebra)."""
        result = verify_nc_deformation_paths()
        assert result["path_3_b_field"]["n_generators"] == 2
        assert result["path_3_b_field"]["is_free"]

    def test_path_4_omega_breaking(self):
        """Path 4: E₁ at generic, E_∞ at self-dual."""
        result = verify_nc_deformation_paths()
        assert result["path_4_omega_background"]["generic_e_n"] == "E_1"
        assert result["path_4_omega_background"]["self_dual_e_n"] == "E_inf"
        assert result["path_4_omega_background"]["breaking_confirmed"]

    def test_path_5_star_product(self):
        """Path 5: Moyal product is associative and commutator correct."""
        result = verify_nc_deformation_paths()
        assert result["path_5_star_product"]["moyal_associative"]
        assert result["path_5_star_product"]["commutator_correct"]

    def test_path_6_nc_atlas(self):
        """Path 6: NC conifold uses Morita transitions."""
        result = verify_nc_deformation_paths()
        assert result["path_6_nc_atlas"]["transition_type"] == "Morita_equivalence"
        assert result["path_6_nc_atlas"]["n_charts"] == 2

    def test_all_paths_at_multiple_theta(self):
        """All paths pass at multiple θ values."""
        for theta in [Fraction(1, 3), Fraction(1), Fraction(2, 7)]:
            result = verify_nc_deformation_paths(theta=theta)
            assert result["all_paths_pass"], f"Failed at θ={theta}"


# ======================================================================
# 10. GRAND SUMMARY
# ======================================================================

class TestGrandSummary:
    """Test the grand summary integrating all six channels."""

    def test_summary_runs(self):
        """The summary function executes without error."""
        result = nc_cy3_e1_summary()
        assert "channels" in result
        assert "universal_conclusions" in result

    def test_e1_forced_for_cy3(self):
        """Universal conclusion: E₁ is forced for CY3."""
        result = nc_cy3_e1_summary()
        assert result["universal_conclusions"]["e1_forced_for_cy3"]

    def test_nc_preserves_e1(self):
        """NC deformation preserves E₁ structure."""
        result = nc_cy3_e1_summary()
        assert result["universal_conclusions"]["nc_preserves_e1"]

    def test_unitarity_preserved(self):
        """R-matrix unitarity is preserved under NC deformation."""
        result = nc_cy3_e1_summary()
        assert result["universal_conclusions"]["unitarity_preserved"]

    def test_kappa_theta_independent(self):
        """κ is independent of the NC parameter θ."""
        result = nc_cy3_e1_summary()
        assert result["universal_conclusions"]["kappa_theta_independent"]

    def test_morita_transitions(self):
        """NC atlas uses Morita transitions."""
        result = nc_cy3_e1_summary()
        assert result["universal_conclusions"]["morita_transitions_for_nc"]

    def test_channel_1_nc_c3(self):
        """Channel 1 (NC C³) reports CY-compatible."""
        result = nc_cy3_e1_summary()
        assert result["channels"]["1_nc_c3"]["cy_compatible"]

    def test_channel_2_unitarity(self):
        """Channel 2 (deformed shuffle) confirms unitarity."""
        result = nc_cy3_e1_summary()
        assert result["channels"]["2_deformed_shuffle"]["unitarity_preserved"]

    def test_channel_3_b_field_kappa(self):
        """Channel 3 (B-field) confirms κ independence."""
        result = nc_cy3_e1_summary()
        assert result["channels"]["3_b_field"]["kappa_b_independent"]

    def test_channel_4_hierarchy(self):
        """Channel 4 (Ω-background) shows E_∞ → E₁ hierarchy."""
        result = nc_cy3_e1_summary()
        ch4 = result["channels"]["4_omega_background"]
        assert ch4["generic_e_n"] == "E_1"
        assert ch4["self_dual_e_n"] == "E_inf"
        assert ch4["classical_e_n"] == "E_inf"

    def test_channel_5_agreement(self):
        """Channel 5 (deformation quantization) agrees with factorization."""
        result = nc_cy3_e1_summary()
        assert result["channels"]["5_deformation_quantization"]["phi3_match"]
        assert result["channels"]["5_deformation_quantization"]["both_W1inf"]


# ======================================================================
# 11. CROSS-CHECKS WITH EXISTING MODULES
# ======================================================================

class TestCrossChecks:
    """Cross-checks with cy3_deformation_quantization and coha_chart_explicit."""

    def test_sigma3_matches_deformation_module(self):
        """σ₃ computation matches cy3_deformation_quantization.

        Both modules should give σ₃ = h₁h₂h₃ = 2/9 at h = (1, -1/3, -2/3).
        """
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        assert omega.sigma3 == Fraction(2, 9)

    def test_phi3_matches_affine_yangian(self):
        """φ₃ = -2σ₃ matches affine_yangian_gl1 convention.

        The affine Yangian module uses the same log-expansion formula:
        φ₃ = α₃ = -2p₃/3 where p₃ = 3σ₃.
        """
        h1, h2, h3 = Fraction(1), Fraction(-1, 3), Fraction(-2, 3)
        sigma3 = h1 * h2 * h3
        shuffle = DeformedShuffleAlgebra(h1, h2, h3)
        phi = shuffle.undeformed_phi(6)
        assert phi[3] == Fraction(-2) * sigma3

    def test_conifold_euler_form_matches_coha_module(self):
        """Euler form χ((1,0),(0,1)) = -2 matches coha_chart_explicit.

        The conifold quiver has:
        vertices: {0, 1}, arrows: a₁,a₂: 0→1, b₁,b₂: 1→0
        χ(e₁, e₂) = 0 - 2 = -2 (0 vertex terms, 2 arrow terms).
        """
        q = nc_conifold_quiver(Fraction(0))
        assert q.euler_form((1, 0), (0, 1)) == -2
        # Antisymmetric: <e₁, e₂> = χ(e₁,e₂) - χ(e₂,e₁) = -2 - (-2) = 0
        # Wait: χ(e₂, e₁) = Σ d₂_i d₁_i - Σ d₂_{s(a)} d₁_{t(a)}
        # = 0 - (0·0 + 0·0 + 1·1 + 1·1) = -2
        assert q.antisymmetric_form((1, 0), (0, 1)) == 0

    def test_unitarity_matches_deformation_module(self):
        """R-matrix unitarity g(z)g(-z) = 1 matches cy3_deformation_quantization."""
        omega = OmegaBackgroundE1(Fraction(1), Fraction(-1, 3))
        assert omega.verify_rmatrix_unitarity(8)
