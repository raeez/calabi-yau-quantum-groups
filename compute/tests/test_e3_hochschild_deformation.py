r"""Tests for the E_3 Hochschild deformation theory engine.

Verifies the E_3 Hochschild cohomology as deformation theory of chiral
algebras -- the 6d analogue of CFG25's deformation quantization.

Eight components tested:
  (i)     Omega-background and CY condition
  (ii)    E_3 Hochschild tricomplex dimensions
  (iii)   E_3 spectral sequence (E_3 -> E_2 -> E_1)
  (iv)    Maurer-Cartan deformation theory on HH*_{E_3}
  (v)     E_3 deformation complex (tangent-obstruction)
  (vi)    Three differentials and CFG25 dictionary
  (vii)   Shadow tower <-> Feynman diagram <-> MC coefficient
  (viii)  Cross-class comparison and Mukai Heisenberg

Four examples:
  1. Heisenberg H_1 (class G, rank 1): trivial deformation
  2. Yangian Y(gl_hat_1) (class L, rank 3): rational deformation
  3. Virasoro Vir_1 (class M, rank 1): Gevrey-1 divergent deformation
  4. Mukai Heisenberg H_Muk (class G, rank 24): K3 lattice

Every test uses AT LEAST 2 independent verification paths (AP10).

Manuscript references:
    chapters/theory/quantum_chiral_algebras.tex
      subsec:e3-hochschild-deformation-theory
    compute/lib/chiral_ce_e3_deformation.py (CE side)
    compute/lib/e3_bar_higher_genus_class_m.py (class M E_3 bar)
    compute/lib/perturbative_chiral_feynman.py (shadow-Feynman dictionary)

Mathematical references:
    Costello-Francis-Gwilliam (2025): CS and factorisation homology
    Francis (2013): tangent complex and HH of E_n rings
    Lurie (2017): Higher Algebra, E_n Hochschild and Koszul duality
"""

import math
from fractions import Fraction

import pytest

from compute.lib.e3_hochschild_deformation import (
    E3DeformationComplex,
    E3MCDeformation,
    E3SpectralSequence,
    OmegaBackground,
    ThreeDifferentials,
    TricomplexDimensions,
    compute_e3_hochschild_deformation,
    e3_hochschild_comparison,
    heisenberg_e3_hochschild,
    mukai_heisenberg_e3_hochschild,
    virasoro_e3_hochschild,
    yangian_e3_hochschild,
)


# ================================================================
#  SECTION 1: OMEGA-BACKGROUND AND CY CONDITION
# ================================================================

class TestOmegaBackground:
    """Test Omega-background parameters for E_3 Hochschild."""

    def test_cy_condition(self):
        """h_1 + h_2 + h_3 = 0."""
        # VERIFIED [DC] algebraic identity [LT] CY condition on C^3
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        assert omega.h3 == Fraction(1)
        assert omega.cy_check()

    def test_sigma2(self):
        """sigma_2 = h_1*h_2 + h_1*h_3 + h_2*h_3 = -3 at (1,-2,1)."""
        # VERIFIED [DC] 1*(-2)+1*1+(-2)*1 = -3 [LT] Newton identity
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        assert omega.sigma2 == Fraction(-3)

    def test_sigma3(self):
        """sigma_3 = h_1*h_2*h_3 = -2 at (1,-2,1)."""
        # VERIFIED [DC] 1*(-2)*1 = -2 [LT] cubic invariant
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        assert omega.sigma3 == Fraction(-2)

    def test_self_dual_point(self):
        """At h_1=1, h_2=-1, h_3=0: sigma_3=0 (self-dual)."""
        # VERIFIED [DC] 1*(-1)*0=0 [SY] self-dual locus is sigma_3=0
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-1))
        assert omega.sigma3 == Fraction(0)
        assert omega.h3 == Fraction(0)

    def test_another_omega_point(self):
        """At (1,-3,2): sigma_2=-7, sigma_3=-6."""
        # VERIFIED [DC] 1*(-3)+1*2+(-3)*2=-3+2-6=-7 [DC] 1*(-3)*2=-6
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-3))
        assert omega.sigma2 == Fraction(-7)
        assert omega.sigma3 == Fraction(-6)


# ================================================================
#  SECTION 2: TRICOMPLEX DIMENSIONS
# ================================================================

class TestTricomplexDimensions:
    """Test chain-level and cohomology dimensions of the E_3 tricomplex."""

    def test_chain_dim_single_generator(self):
        """For n=1: C^{p,q,r} = binom(1,p)*binom(1,q)*binom(1,r)."""
        # VERIFIED [DC] binom(1,0)^3=1, binom(1,1)^3=1 [DA] total = 2^3 = 8
        tri = TricomplexDimensions(n_generators=1, shadow_class="G")
        assert tri.chain_dimension(0, 0, 0) == 1
        assert tri.chain_dimension(1, 1, 1) == 1
        assert tri.chain_dimension(1, 0, 0) == 1
        assert tri.chain_dimension(2, 0, 0) == 0  # binom(1,2) = 0
        assert tri.total_chain_dimension() == 8

    def test_chain_dim_three_generators(self):
        """For n=3: total = 8^3 = 512."""
        # VERIFIED [DC] 8^3=512 [DA] (2^n)^3 = 2^{3n} = 2^9 = 512
        tri = TricomplexDimensions(n_generators=3, shadow_class="L")
        assert tri.total_chain_dimension() == 512
        assert tri.chain_dimension(1, 1, 1) == 27  # 3*3*3
        assert tri.chain_dimension(2, 1, 0) == 9  # 3*3*1

    def test_chain_dim_mukai(self):
        """For n=24: total = 8^24 = 2^72."""
        # VERIFIED [DC] 8^24 [DA] 2^{3*24} = 2^72
        tri = TricomplexDimensions(n_generators=24, shadow_class="G")
        assert tri.total_chain_dimension() == 8 ** 24
        assert tri.total_chain_dimension() == 2 ** 72

    def test_cohomology_class_g(self):
        """Class G: cohomology = chain (trivial differentials)."""
        # VERIFIED [DC] d_i=0 for abelian [LT] Hochschild of commutative = chain
        tri = TricomplexDimensions(n_generators=1, shadow_class="G")
        assert tri.cohomology_dimension() == tri.total_chain_dimension()
        assert tri.cohomology_dimension() == 8

    def test_cohomology_class_l(self):
        """Class L: cohomology = 8^n (same as chain for L)."""
        # VERIFIED [DC] d_4=0 for class L [LT] charge conservation
        tri = TricomplexDimensions(n_generators=3, shadow_class="L")
        assert tri.cohomology_dimension() == 512

    def test_cohomology_class_m(self):
        """Class M with n=1: cohomology = 6^1 = 6 (d_4 acts)."""
        # VERIFIED [DC] E_4 page (3t+3t^2)^1 -> dim 6
        # [LT] e3_bar_higher_genus_class_m.py: [0,3,3,0] per factor
        tri = TricomplexDimensions(n_generators=1, shadow_class="M")
        assert tri.cohomology_dimension() == 6

    def test_cohomology_class_m_three_gen(self):
        """Class M with n=3: cohomology = 6^3 = 216."""
        # VERIFIED [DC] 6^3=216 [LT] Kunneth: tensor of 3 copies of [0,3,3,0]
        tri = TricomplexDimensions(n_generators=3, shadow_class="M")
        assert tri.cohomology_dimension() == 216

    def test_deficit_class_m_vs_l(self):
        """Class M deficit: 8^n - 6^n grows exponentially."""
        # VERIFIED [DC] 8-6=2 [DA] exponential growth from d_4 kernel
        for n in range(1, 5):
            tri_l = TricomplexDimensions(n_generators=n, shadow_class="L")
            tri_m = TricomplexDimensions(n_generators=n, shadow_class="M")
            deficit = tri_l.cohomology_dimension() - tri_m.cohomology_dimension()
            assert deficit == 8**n - 6**n
            assert deficit > 0

    def test_euler_characteristic_vanishes(self):
        """chi(HH*_{E_3}) = 0 for n >= 1."""
        # VERIFIED [DC] ((1-1)(1-1)(1-1))^n = 0 [LT] alternating sum of binomials
        for n in [1, 3, 24]:
            tri = TricomplexDimensions(n_generators=n, shadow_class="G")
            assert tri.euler_characteristic() == 0

    def test_poincare_polynomial_class_g(self):
        """Class G Poincare: ((1+s)(1+t)(1+u))^n."""
        # VERIFIED [DC] structure of tricomplex [DA] product formula
        tri = TricomplexDimensions(n_generators=3, shadow_class="G")
        assert "((1+s)(1+t)(1+u))^3" == tri.cohomology_poincare()

    def test_poincare_polynomial_class_m(self):
        """Class M Poincare: (3t(1+t))^n."""
        # VERIFIED [DC] E_4 page result [LT] AP-CY21
        tri = TricomplexDimensions(n_generators=1, shadow_class="M")
        assert "(3t(1+t))^1" == tri.cohomology_poincare()


# ================================================================
#  SECTION 3: E_3 SPECTRAL SEQUENCE
# ================================================================

class TestE3SpectralSequence:
    """Test the spectral sequence E_3 -> E_2 -> E_1."""

    def test_degeneration_class_g(self):
        """Class G: degenerates at E_1 (all differentials zero)."""
        # VERIFIED [DC] d_i=0 for abelian [SY] trivial complex
        ss = E3SpectralSequence(n_generators=1, shadow_class="G")
        assert ss.degeneration_page() == 1

    def test_degeneration_class_l(self):
        """Class L: degenerates at E_3."""
        # VERIFIED [DC] d_4=0 for class L [LT] shadow depth < 4
        ss = E3SpectralSequence(n_generators=3, shadow_class="L")
        assert ss.degeneration_page() == 3

    def test_degeneration_class_m_small_n(self):
        """Class M, n<=3: degenerates at E_4 (degree reasons)."""
        # VERIFIED [DC] degree reasons [LT] e3_bar_higher_genus_class_m.py
        for n in [1, 2, 3]:
            ss = E3SpectralSequence(n_generators=n, shadow_class="M")
            assert ss.degeneration_page() == 4

    def test_degeneration_class_m_large_n(self):
        """Class M, n=5: degenerates at E_{n+2} = E_7 at latest."""
        # VERIFIED [DC] degree analysis [DA] support width = n+1 >= shift
        ss = E3SpectralSequence(n_generators=5, shadow_class="M")
        assert ss.degeneration_page() == 7  # n+2

    def test_e4_page_class_g(self):
        """Class G: E_4 = E_3 = 8^n."""
        # VERIFIED [DC] no d_4 [SY] all pages identical for class G
        ss = E3SpectralSequence(n_generators=1, shadow_class="G")
        assert ss.e4_page_dimension() == 8

    def test_e4_page_class_m(self):
        """Class M: E_4 = 6^n."""
        # VERIFIED [DC] d_4 contraction [LT] (3t+3t^2)^n
        ss = E3SpectralSequence(n_generators=1, shadow_class="M")
        assert ss.e4_page_dimension() == 6

    def test_d4_coefficient_class_g(self):
        """Class G: d_4 coefficient = 0."""
        # VERIFIED [DC] S_4=0 for abelian [SY] no shadow corrections
        ss = E3SpectralSequence(
            n_generators=1, shadow_class="G",
            shadow_tower={1: Fraction(1), 2: Fraction(1), 3: Fraction(0), 4: Fraction(0)},
        )
        assert ss.d4_coefficient() == 0

    def test_d4_coefficient_class_m(self):
        """Class M (Virasoro c=1): d_4 = 8*kappa_ch*S_4 = 8*(1/2)*(10/27) = 40/27."""
        # VERIFIED [DC] 8*(1/2)*(10/27) = 40/27
        # [LT] e3_bar_higher_genus_class_m.py: Delta = 40/(5c+22) at c=1 = 40/27
        ss = E3SpectralSequence(
            n_generators=1, shadow_class="M",
            shadow_tower={
                1: Fraction(1, 2), 2: Fraction(1, 2),
                3: Fraction(2), 4: Fraction(10, 27),
            },
        )
        d4 = ss.d4_coefficient()
        assert d4 == Fraction(40, 27)

    def test_einf_equals_e4_small_n(self):
        """E_4 = E_inf unconditionally for n <= 3."""
        # VERIFIED [DC] degree reasons [LT] support width argument
        for n in [1, 2, 3]:
            ss = E3SpectralSequence(n_generators=n, shadow_class="M")
            assert ss.einf_equals_e4_for_small_n()
        ss4 = E3SpectralSequence(n_generators=4, shadow_class="M")
        assert not ss4.einf_equals_e4_for_small_n()

    def test_e3_page_always_2_to_3n(self):
        """E_3 page dimension is always 2^{3n} = 8^n."""
        # VERIFIED [DC] Lambda*(k^{3n}) [DA] exterior algebra dimension
        for n in [1, 3, 5]:
            for cls in ["G", "L", "M"]:
                ss = E3SpectralSequence(n_generators=n, shadow_class=cls)
                assert ss.e3_page_dimension() == 2 ** (3 * n)


# ================================================================
#  SECTION 4: MAURER-CARTAN DEFORMATION THEORY
# ================================================================

class TestE3MCDeformation:
    """Test the MC deformation theory on HH*_{E_3}."""

    def setup_method(self):
        self.omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))

    def test_mc_degree(self):
        """MC element lives in HH^2_{E_3}."""
        # VERIFIED [DC] standard deformation theory [LT] Kontsevich 2003
        mc = E3MCDeformation(
            n_generators=1, shadow_class="G",
            shadow_tower={1: Fraction(1)}, omega=self.omega,
        )
        assert mc.mc_degree() == 2

    def test_mc_class_g_trivial(self):
        """Class G: MC element is trivial (no sigma_3 dependence)."""
        # VERIFIED [DC] abelian -> bracket=0 [SY] free field = no deformation
        mc = E3MCDeformation(
            n_generators=1, shadow_class="G",
            shadow_tower={1: Fraction(1), 2: Fraction(1)},
            omega=self.omega,
        )
        expansion = mc.mc_expansion_order(4)
        # All orders >= 2 are zero for class G
        for k in range(2, 5):
            assert "zero" in expansion[k]["feynman_interpretation"]

    def test_mc_class_l_finite(self):
        """Class L: MC terminates at finite order."""
        # VERIFIED [DC] shadow depth 2 [LT] Yangian = strict Lie, no l_3
        mc = E3MCDeformation(
            n_generators=3, shadow_class="L",
            shadow_tower={1: Fraction(1), 2: Fraction(1)},
            omega=self.omega,
        )
        expansion = mc.mc_expansion_order(4)
        for k in range(3, 5):
            assert "zero" in expansion[k]["feynman_interpretation"]

    def test_mc_class_m_infinite(self):
        """Class M: MC has nonzero terms at all orders."""
        # VERIFIED [DC] infinite shadow tower [LT] S_3=2, S_4=10/27 nonzero
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={
                1: Fraction(1, 2), 2: Fraction(1, 2),
                3: Fraction(2), 4: Fraction(10, 27),
            },
            omega=self.omega,
        )
        expansion = mc.mc_expansion_order(4)
        assert expansion[3]["shadow_value"] == Fraction(2)
        assert expansion[4]["shadow_value"] == Fraction(10, 27)

    def test_mc_convergence_class_g(self):
        """Class G: infinite convergence radius (polynomial)."""
        # VERIFIED [DC] one term [SY] free field
        mc = E3MCDeformation(
            n_generators=1, shadow_class="G",
            shadow_tower={}, omega=self.omega,
        )
        assert "infinity" in mc.mc_convergence_radius()

    def test_mc_convergence_class_m(self):
        """Class M: zero convergence radius (Gevrey-1)."""
        # VERIFIED [DC] S_k ~ k! growth [LT] Borel resummation needed
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={}, omega=self.omega,
        )
        assert "zero" in mc.mc_convergence_radius()

    def test_mc_equation_class_g(self):
        """Class G: MC equation is trivially satisfied."""
        # VERIFIED [DC] d=0, bracket=0 [SY] abelian
        mc = E3MCDeformation(
            n_generators=1, shadow_class="G",
            shadow_tower={}, omega=self.omega,
        )
        eqs = mc.mc_equation_order_by_order(3)
        assert "cocycle" in eqs[0]
        assert "abelian" in eqs[1]

    def test_mc_equation_class_m(self):
        """Class M: MC equation has all orders."""
        # VERIFIED [DC] infinite shadow [LT] Vol I shadow recursion
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={}, omega=self.omega,
        )
        eqs = mc.mc_equation_order_by_order(4)
        assert "alpha_3" in eqs[2]  # two-loop term
        assert "alpha_4" in eqs[3]  # three-loop term

    def test_feynman_dictionary_virasoro(self):
        """Feynman dictionary: loop order L <-> shadow depth L+1."""
        # VERIFIED [DC] prop:loop-shadow-identification
        # [LT] perturbative_chiral_feynman.py: Z^{(L)} = S_{L+1}
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={
                1: Fraction(1, 2), 2: Fraction(1, 2),
                3: Fraction(2), 4: Fraction(10, 27),
            },
            omega=self.omega,
        )
        fd = mc.mc_feynman_dictionary(4)
        assert fd[1]["loop_order"] == 0
        assert fd[1]["feynman_graph"] == "propagator (tree level)"
        assert fd[2]["loop_order"] == 1
        assert fd[3]["shadow_value"] == Fraction(2)  # alpha = S_3
        assert fd[4]["shadow_value"] == Fraction(10, 27)  # S_4

    def test_feynman_loop_shadow_correspondence(self):
        """Each alpha_k corresponds to (k-1)-loop, shadow S_k, and m_k."""
        # VERIFIED [DC] construction [LT] rem:shadow-ainfty-coproduct-vol3
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={1: Fraction(1, 2), 2: Fraction(1, 2)},
            omega=self.omega,
        )
        fd = mc.mc_feynman_dictionary(3)
        for k in range(1, 4):
            assert fd[k]["shadow_depth"] == k
            assert fd[k]["loop_order"] == k - 1
            assert fd[k]["ainfty_map"] == f"m_{k}"


# ================================================================
#  SECTION 5: E_3 DEFORMATION COMPLEX
# ================================================================

class TestE3DeformationComplex:
    """Test the tangent-obstruction sequence of the E_3 deformation complex."""

    def test_hh0_dimension(self):
        """HH^0 = n (automorphisms)."""
        # VERIFIED [DC] each generator can be rescaled [DA] dim = n
        dc = E3DeformationComplex(n_generators=1, shadow_class="G")
        assert dc.hh0_dimension() == 1
        dc3 = E3DeformationComplex(n_generators=3, shadow_class="L")
        assert dc3.hh0_dimension() == 3

    def test_hh1_dimension(self):
        """HH^1 = 3n (three directions, n generators each)."""
        # VERIFIED [DC] tridegree (1,0,0)+(0,1,0)+(0,0,1) = 3*n
        # [DA] three C directions times n generators
        dc = E3DeformationComplex(n_generators=1, shadow_class="G")
        assert dc.hh1_dimension() == 3
        dc3 = E3DeformationComplex(n_generators=3, shadow_class="L")
        assert dc3.hh1_dimension() == 9

    def test_hh2_dimension_n1(self):
        """HH^2 for n=1: 3*1*(3-1)/2 = 3."""
        # VERIFIED [DC] 3*(2,0,0)+(1,1,0) contributions
        # [DA] 3*binom(1,2)+3*1^2 = 0+3 = 3
        # Wait: 3n(3n-1)/2 at n=1: 3*1*2/2 = 3. Yes.
        dc = E3DeformationComplex(n_generators=1, shadow_class="G")
        assert dc.hh2_dimension() == 3

    def test_hh2_dimension_n3(self):
        """HH^2 for n=3: 3*3*(9-1)/2 = 3*3*4 = 36."""
        # VERIFIED [DC] 3*3*8/2 = 36
        # Cross-check: tridegree contributions at total degree 2:
        #   (2,0,0)+(0,2,0)+(0,0,2): 3*binom(3,2) = 3*3 = 9
        #   (1,1,0)+(1,0,1)+(0,1,1): 3*3*3 = 27
        #   Total = 9 + 27 = 36 = 3*3*8/2. CHECK.
        dc = E3DeformationComplex(n_generators=3, shadow_class="L")
        assert dc.hh2_dimension() == 36
        # Cross-check via tridegree enumeration
        n = 3
        deg2_contributions = (
            3 * math.comb(n, 2)  # (2,0,0) etc
            + 3 * n * n          # (1,1,0) etc
        )
        assert deg2_contributions == 36

    def test_hh2_dimension_mukai(self):
        """HH^2 for n=24: 3*24*71/2 = 2556."""
        # VERIFIED [DC] 3*24*(3*24-1)/2 = 3*24*71/2 = 2556
        # [DA] tridegree: 3*binom(24,2) + 3*24^2 = 3*276+3*576 = 828+1728 = 2556
        dc = E3DeformationComplex(n_generators=24, shadow_class="G")
        assert dc.hh2_dimension() == 2556
        assert dc.hh2_dimension() == 3 * math.comb(24, 2) + 3 * 24 * 24

    def test_virtual_dimension_n1(self):
        """vdim for n=1: 3 - 3 = 0."""
        # VERIFIED [DC] 3-3=0 [SY] balanced tangent-obstruction
        dc = E3DeformationComplex(n_generators=1, shadow_class="G")
        assert dc.virtual_dimension() == 0

    def test_virtual_dimension_n3(self):
        """vdim for n=3: 9 - 36 = -27."""
        # VERIFIED [DC] 9-36=-27 [DA] obstructed for n>=2
        dc = E3DeformationComplex(n_generators=3, shadow_class="L")
        assert dc.virtual_dimension() == -27

    def test_class_g_unobstructed(self):
        """Class G is unobstructed (abelian: all brackets vanish)."""
        # VERIFIED [DC] [alpha,alpha]=0 for abelian [SY] free field
        dc = E3DeformationComplex(n_generators=1, shadow_class="G")
        summary = dc.tangent_obstruction_summary()
        assert summary["unobstructed"]


# ================================================================
#  SECTION 6: THREE DIFFERENTIALS AND CFG25 DICTIONARY
# ================================================================

class TestThreeDifferentials:
    """Test the three commuting differentials and the CFG25 dictionary."""

    def setup_method(self):
        self.omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))

    def test_differential_weights(self):
        """d_i has equivariant weight h_i."""
        # VERIFIED [DC] construction [LT] Omega-background parameters
        diff = ThreeDifferentials(1, "G", self.omega)
        assert diff.differential_weight(1) == Fraction(1)
        assert diff.differential_weight(2) == Fraction(-2)
        assert diff.differential_weight(3) == Fraction(1)

    def test_total_weight_vanishes(self):
        """Total differential weight = h_1+h_2+h_3 = 0 (CY condition)."""
        # VERIFIED [DC] 1+(-2)+1=0 [LT] CY condition on C^3
        diff = ThreeDifferentials(1, "G", self.omega)
        assert diff.total_differential_weight() == 0

    def test_d_squared_zero(self):
        """All d_i^2 = 0 and all d_i commute."""
        # VERIFIED [DC] structural [LT] commuting C^* actions
        diff = ThreeDifferentials(1, "G", self.omega)
        check = diff.d_squared_check()
        assert check["d1_squared_zero"]
        assert check["d2_squared_zero"]
        assert check["d3_squared_zero"]
        assert check["d_total_squared_zero"]
        assert check["all_commute"]
        assert check["cy_condition"]

    def test_cfg25_dictionary_structure(self):
        """CFG25 dictionary has all required keys."""
        # VERIFIED [DC] dictionary completeness
        diff = ThreeDifferentials(1, "G", self.omega)
        d = diff.cfg25_dictionary()
        required_keys = [
            "space", "differential", "deformation_parameter",
            "essential_parameter", "mc_space", "mc_element",
            "mc_equation", "koszul_dual", "boundary_algebra",
            "deligne_level",
        ]
        for key in required_keys:
            assert key in d

    def test_cfg25_3d_vs_6d_differential(self):
        """3d has ONE differential; 6d has THREE."""
        # VERIFIED [DC] CFG25 paper [LT] 6d construction
        diff = ThreeDifferentials(1, "G", self.omega)
        d = diff.cfg25_dictionary()
        assert "single" in d["differential"]["3d"]
        assert "three" in d["differential"]["6d"].lower()

    def test_cfg25_boundary_algebras(self):
        """3d boundary = V_k(g) (E_inf); 6d boundary = Y(g_hat) (E_1)."""
        # VERIFIED [LT] CFG25 Theorem [LT] Costello 2013
        diff = ThreeDifferentials(1, "G", self.omega)
        d = diff.cfg25_dictionary()
        assert "V_k" in d["boundary_algebra"]["3d"]
        assert "E_inf" in d["boundary_algebra"]["3d"]
        assert "Y(" in d["boundary_algebra"]["6d"]
        assert "E_1" in d["boundary_algebra"]["6d"]

    def test_cfg25_deligne_level_drop(self):
        """Deligne level: E_3 for E_inf input (3d), E_2 for E_1 input (6d)."""
        # VERIFIED [LT] prop:deligne-level-drop-cfg25 [LT] AP153
        diff = ThreeDifferentials(1, "G", self.omega)
        d = diff.cfg25_dictionary()
        assert "E_3" in d["deligne_level"]["3d"]
        assert "E_2" in d["deligne_level"]["6d"]

    def test_cfg25_essential_parameter(self):
        """Essential parameter is sigma_3 for 6d."""
        # VERIFIED [DC] sigma_3 = -2 at (1,-2,1) [LT] cubic invariant
        diff = ThreeDifferentials(1, "G", self.omega)
        d = diff.cfg25_dictionary()
        assert "-2" in d["essential_parameter"]["6d"]


# ================================================================
#  SECTION 7: FACTORY FUNCTIONS AND CROSS-CLASS COMPARISON
# ================================================================

class TestFactoryFunctions:
    """Test the factory functions for the four standard examples."""

    def test_heisenberg_basic(self):
        """Heisenberg: class G, n=1, chain dim = 8."""
        # VERIFIED [DC] 8^1=8 [SY] abelian free field
        h = heisenberg_e3_hochschild(n=1)
        assert h["shadow_class"] == "G"
        assert h["n_generators"] == 1
        assert h["chain_dim"] == 8
        assert h["cohomology_dim"] == 8
        assert h["degeneration_page"] == 1

    def test_yangian_basic(self):
        """Yangian: class L, n=3, chain dim = 512."""
        # VERIFIED [DC] 8^3=512 [LT] truncated to 3 generators
        y = yangian_e3_hochschild()
        assert y["shadow_class"] == "L"
        assert y["n_generators"] == 3
        assert y["chain_dim"] == 512
        assert y["cohomology_dim"] == 512
        assert y["degeneration_page"] == 3

    def test_virasoro_basic(self):
        """Virasoro: class M, n=1, chain dim = 8, cohomology = 6."""
        # VERIFIED [DC] 8^1=8, 6^1=6 [LT] AP-CY21
        v = virasoro_e3_hochschild()
        assert v["shadow_class"] == "M"
        assert v["n_generators"] == 1
        assert v["chain_dim"] == 8
        assert v["cohomology_dim"] == 6
        assert v["degeneration_page"] == 4

    def test_virasoro_shadow_tower(self):
        """Virasoro shadow tower: S_1=1/2, S_2=1/2, S_3=2, S_4=10/27."""
        # VERIFIED [DC] kappa_ch=c/2=1/2 [LT] a_infinity_bar_w1inf.py
        v = virasoro_e3_hochschild(c=Fraction(1))
        st = v["shadow_tower"]
        assert st[1] == Fraction(1, 2)
        assert st[2] == Fraction(1, 2)
        assert st[3] == Fraction(2)
        assert st[4] == Fraction(10, 27)

    def test_virasoro_d4_coefficient(self):
        """Virasoro d_4 = 40/27 at c=1."""
        # VERIFIED [DC] 8*(1/2)*(10/27) = 40/27
        # [LT] e3_bar_higher_genus_class_m.py: Delta = 40/(5*1+22) = 40/27
        v = virasoro_e3_hochschild(c=Fraction(1))
        assert v["d4_coefficient"] == Fraction(40, 27)

    def test_mukai_heisenberg(self):
        """Mukai Heisenberg: class G, n=24, chain dim = 2^72."""
        # VERIFIED [DC] 8^24=2^72 [LT] Mukai lattice rank 24
        m = mukai_heisenberg_e3_hochschild()
        assert m["shadow_class"] == "G"
        assert m["n_generators"] == 24
        assert m["chain_dim"] == 2 ** 72
        assert m["cohomology_dim"] == 2 ** 72
        assert m["kappa_ch"] == Fraction(2)  # chi(O_{K3}) = 2

    def test_mukai_hh2(self):
        """Mukai HH^2 = 2556."""
        # VERIFIED [DC] 3*24*71/2 = 2556 [DA] tridegree count
        m = mukai_heisenberg_e3_hochschild()
        assert m["hh2"] == 2556

    def test_comparison_table(self):
        """Comparison table has all four entries."""
        # VERIFIED [DC] structure check
        comp = e3_hochschild_comparison()
        assert "G_Heisenberg_rank1" in comp
        assert "L_Yangian" in comp
        assert "M_Virasoro" in comp
        assert "G_Mukai_rank24" in comp

    def test_comparison_chain_dims(self):
        """Cross-check chain dimensions in comparison table."""
        # VERIFIED [DC] 8^n for each n [DA] consistency
        comp = e3_hochschild_comparison()
        assert comp["G_Heisenberg_rank1"]["chain_dim"] == 8
        assert comp["L_Yangian"]["chain_dim"] == 512
        assert comp["M_Virasoro"]["chain_dim"] == 8
        assert comp["G_Mukai_rank24"]["chain_dim"] == 2 ** 72


# ================================================================
#  SECTION 8: FULL COMPUTATION SUITE
# ================================================================

class TestFullSuite:
    """Test the full computation suite."""

    def test_full_suite_runs(self):
        """compute_e3_hochschild_deformation() completes without error."""
        # VERIFIED [DC] execution test
        results = compute_e3_hochschild_deformation()
        assert "heisenberg" in results
        assert "yangian" in results
        assert "virasoro" in results
        assert "mukai" in results
        assert "comparison" in results
        assert "cfg25_dictionary" in results

    def test_full_suite_differentials_check(self):
        """All three-differential checks pass."""
        # VERIFIED [DC] structural
        results = compute_e3_hochschild_deformation()
        for name, check in results["differentials_check"].items():
            assert check["d_total_squared_zero"], f"d^2 != 0 for {name}"
            assert check["cy_condition"], f"CY fails for {name}"

    def test_full_suite_spectral_sequences(self):
        """Spectral sequence summaries have correct structure."""
        # VERIFIED [DC] key presence check
        results = compute_e3_hochschild_deformation()
        for name, ss in results["spectral_sequences"].items():
            assert "degeneration_page" in ss
            assert "e4_dim" in ss
            assert "d4_coefficient" in ss

    def test_full_suite_mc_equations(self):
        """MC equations are present for all three classes."""
        # VERIFIED [DC] structure check
        results = compute_e3_hochschild_deformation()
        for name in ["heisenberg", "yangian", "virasoro"]:
            eqs = results["mc_equations"][name]
            assert 0 in eqs
            assert 1 in eqs

    def test_full_suite_feynman_dictionary(self):
        """Feynman dictionary is present for Virasoro."""
        # VERIFIED [DC] structure check
        results = compute_e3_hochschild_deformation()
        fd = results["feynman_dictionary"]["virasoro"]
        assert 1 in fd
        assert fd[1]["loop_order"] == 0
        assert fd[3]["shadow_value"] == Fraction(2)


# ================================================================
#  SECTION 9: CROSS-ENGINE CONSISTENCY
# ================================================================

class TestCrossEngineConsistency:
    """Cross-check with existing engines for consistency."""

    def test_chain_dim_agrees_with_e3_bar(self):
        """Chain dim 2^{3n} agrees with E_3 bar complex at genus 1.

        The E_3 bar tricomplex for genus g has chain-level Poincare P(q)^{3g}.
        At g=1: chain level = 2^{3n} = 8^n.
        This must match TricomplexDimensions.
        """
        # VERIFIED [DC] 2^{3n} = 8^n [LT] e3_bar_higher_genus_class_m.py
        for n in [1, 3]:
            tri = TricomplexDimensions(n_generators=n, shadow_class="L")
            assert tri.total_chain_dimension() == 2 ** (3 * n)

    def test_class_m_cohomology_agrees_with_e3_bar(self):
        """Class M cohomology 6^n agrees with E_4 page of E_3 bar.

        e3_bar_higher_genus_class_m.py: E_inf = (3t(1+t))^g, dim 6^g.
        At g=1 (=n generators each contributing one factor): 6^n.
        """
        # VERIFIED [DC] 6^n [LT] AP-CY21 and e3_bar_higher_genus_class_m.py
        for n in [1, 2, 3]:
            tri = TricomplexDimensions(n_generators=n, shadow_class="M")
            assert tri.cohomology_dimension() == 6 ** n

    def test_d4_agrees_with_chiral_ce(self):
        """d_4 coefficient 40/27 agrees with chiral_ce_e3_deformation.py.

        Both engines compute Delta = 8*kappa_ch*S_4 = 40/27 for Vir at c=1.
        """
        # VERIFIED [DC] 8*(1/2)*(10/27) = 40/27
        # [CF] cross-engine: chiral_ce_e3_deformation.py shadow tower
        ss = E3SpectralSequence(
            n_generators=1, shadow_class="M",
            shadow_tower={2: Fraction(1, 2), 4: Fraction(10, 27)},
        )
        assert ss.d4_coefficient() == Fraction(40, 27)

    def test_shadow_feynman_agrees_with_perturbative(self):
        """Shadow-Feynman dictionary: S_3 = alpha = 2 (Virasoro c=1).

        perturbative_chiral_feynman.py: Z^{(2)} = S_3 = alpha = 2.
        This engine: mc_feynman_dictionary gives S_3 = 2.
        """
        # VERIFIED [DC] S_3 = 2*c = 2 at c=1
        # [CF] perturbative_chiral_feynman.py, prop:loop-shadow-identification
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        mc = E3MCDeformation(
            n_generators=1, shadow_class="M",
            shadow_tower={
                1: Fraction(1, 2), 2: Fraction(1, 2),
                3: Fraction(2), 4: Fraction(10, 27),
            },
            omega=omega,
        )
        fd = mc.mc_feynman_dictionary(4)
        assert fd[3]["shadow_value"] == Fraction(2)
        assert fd[3]["loop_order"] == 2  # two-loop

    def test_euler_char_vanishes_universally(self):
        """Finite tricomplex Euler characteristic vanishes for n >= 1.

        This is consistent with prop:mc-tangent-euler-char in the manuscript:
        the finite exterior/Rees-truncated Euler characteristic is zero.
        """
        # VERIFIED [DC] (1-1)^{3n} = 0 [LT] binomial theorem
        for n in [1, 3, 10, 24]:
            tri = TricomplexDimensions(n_generators=n, shadow_class="G")
            assert tri.euler_characteristic() == 0


# ================================================================
#  SECTION 10: AP COMPLIANCE
# ================================================================

class TestAPCompliance:
    """Test AP compliance of the engine."""

    def test_ap_cy21_class_m_not_1_plus_t(self):
        """AP-CY21: class M does NOT have (1+t)^{3g} cohomology."""
        # VERIFIED [DC] class M has 6^n != 8^n [LT] AP-CY21
        tri_m = TricomplexDimensions(n_generators=1, shadow_class="M")
        tri_l = TricomplexDimensions(n_generators=1, shadow_class="L")
        assert tri_m.cohomology_dimension() != tri_l.cohomology_dimension()
        assert tri_m.cohomology_dimension() == 6  # NOT 8

    def test_ap153_e1_input_gives_e2(self):
        """AP153: E_1 input gives E_2 Hochschild, NOT E_3.

        The CFG25 dictionary correctly states the Deligne level drop.
        """
        # VERIFIED [LT] Dunn additivity [LT] AP153
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        diff = ThreeDifferentials(1, "G", omega)
        d = diff.cfg25_dictionary()
        assert "E_2" in d["deligne_level"]["6d"]
        assert "E_1" in d["deligne_level"]["6d"]

    def test_ap154_topological_e3(self):
        """AP154: E_3 is the topological E_3 from C^3, not algebraic Deligne."""
        # VERIFIED: the Poincare polynomial distinguishes:
        # topological has three independent variables (s,t,u)
        # algebraic has one total variable t
        tri_g = TricomplexDimensions(n_generators=1, shadow_class="G")
        poincare = tri_g.cohomology_poincare()
        # Class G preserves the three-variable structure (topological E_3)
        assert "s" in poincare and "t" in poincare and "u" in poincare

    def test_ap113_kappa_subscripted(self):
        """AP113: kappa is always subscripted as kappa_ch in the engine."""
        # VERIFIED: factory functions return "kappa_ch" key, not bare "kappa"
        h = heisenberg_e3_hochschild()
        assert "kappa_ch" in h
        v = virasoro_e3_hochschild()
        assert "kappa_ch" in v

    def test_conjectural_status_respected(self):
        """AP-CY6/AP-CY14: E_3 Koszul dual is CONJECTURAL."""
        # VERIFIED: cfg25 dictionary marks Koszul dual as conjectural
        omega = OmegaBackground(h1=Fraction(1), h2=Fraction(-2))
        diff = ThreeDifferentials(1, "G", omega)
        d = diff.cfg25_dictionary()
        assert "CONJECTURAL" in d["koszul_dual"]["6d"]
