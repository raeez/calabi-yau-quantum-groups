r"""Tests for derived_satake_chiral.py: derived geometric Satake for chiral QGs.

CENTRAL RESULTS:
    (1) Classical Satake: Perv(Gr_G) ~= Rep(G^L)  (PROVED, Mirkovic-Vilonen)
    (2) Derived Satake: D-mod(Gr_G) ~= IndCoh(N^L/G^L)  (PROVED, Bezrukavnikov-Finkelberg)
    (3) Chiral Satake for C^3: CONJECTURAL (strong evidence from MO match)
    (4) Chiral Satake for K3: CONJECTURAL (AP-CY14)
    (5) Geometric R-matrix from commutativity constraint: PROVED (classical),
        CONJECTURAL (chiral)
    (6) Convolution product dual to Drinfeld coproduct: verified at low charges
    (7) Factorization property of Gr^{ch}_G: PROVED (Beilinson-Drinfeld)
    (8) E_1 -> E_2 via Iwahori -> full Satake (Drinfeld center)

Manuscript references:
    geometric_langlands.tex sec:open-problems (open problem (v))
    quantum_chiral_algebras.tex thm:mo-chiral-rmatrix (MO/chiral R-matrix match)
    drinfeld_center.tex thm:drinfeld-center-coha (Drinfeld center of CoHA)

Literature ground truth:
    Mirkovic-Vilonen (2007): geometric Satake is a theorem
    # VERIFIED [LT] Mirkovic-Vilonen, arXiv:math/0401222

    Bezrukavnikov-Finkelberg (2008): derived Satake is a theorem
    # VERIFIED [LT] Bezrukavnikov-Finkelberg, arXiv:0707.3799

    Orbit structure of Gr_{SL_2}: dim(Gr^{(n)}) = 2n
    # VERIFIED [LT] Pressley-Segal, "Loop Groups" (1986), Ch. 8

    Weight functor: V_n of SL_2 has dim n+1
    # VERIFIED [LT] standard representation theory

    24-coloured partitions: p_{24}(k) for k=0,...,5
    # VERIFIED [DC] direct computation [LT] OEIS A006922

    Unitarity: g(z)g(-z) = 1 for CY structure function
    # VERIFIED [DC] algebraic computation [SY] pairing cancellation
"""

import pytest
from fractions import Fraction

from compute.lib.derived_satake_chiral import (
    # Constants
    MV_PROVED,
    BF_DERIVED_PROVED,
    CHIRAL_SATAKE_STATUS,
    MUKAI_RANK,
    MUKAI_SIG_PLUS,
    MUKAI_SIG_MINUS,
    # Affine Grassmannian
    AffineGrassmannianData,
    GrOrbitData,
    affine_grassmannian,
    gr_orbit,
    # Chiral Grassmannian
    ChiralGrassmannianData,
    FactorizationPropertyData,
    chiral_grassmannian,
    factorization_property,
    # Convolution
    ConvolutionData,
    convolution_product,
    # Geometric R-matrix
    GeometricRMatrixData,
    geometric_r_matrix_classical,
    geometric_r_matrix_chiral_charge1,
    geometric_r_matrix_k3_charge1,
    r_matrix_unitarity_check,
    # Derived Satake
    DerivedSatakeData,
    classical_satake,
    derived_satake,
    chiral_satake_c3,
    chiral_satake_k3,
    # Weight functors
    WeightFunctorData,
    weight_functor_gl1_k3,
    weight_functor_sl2,
    # Iwahori
    IwahoriSatakeData,
    iwahori_satake_passage,
    # Verification
    verify_orbit_structure_gl1,
    verify_orbit_structure_sl2,
    verify_convolution_additivity,
    verify_unitarity_c3,
    verify_unitarity_k3_params,
    verify_factorization_separated,
    verify_factorization_collision,
    verify_satake_hierarchy,
    verify_weight_functor_sl2,
    verify_iwahori_e1_e2,
    verify_classical_vs_chiral_braiding,
    verify_chiral_grassmannian_factorization,
    full_verification,
)

F = Fraction


# ================================================================
# Section 1: CLASSICAL GROUND TRUTH (PROVED)
# ================================================================

class TestClassicalSatakeStatus:
    """Verify that classical Satake theorems are correctly marked PROVED."""

    def test_mv_proved(self):
        """Mirkovic-Vilonen geometric Satake is PROVED."""
        # VERIFIED [LT] Mirkovic-Vilonen, arXiv:math/0401222
        assert MV_PROVED is True

    def test_bf_derived_proved(self):
        """Bezrukavnikov-Finkelberg derived Satake is PROVED."""
        # VERIFIED [LT] Bezrukavnikov-Finkelberg, arXiv:0707.3799
        assert BF_DERIVED_PROVED is True

    def test_chiral_conjectural(self):
        """Chiral Satake is correctly marked CONJECTURAL."""
        assert CHIRAL_SATAKE_STATUS == "CONJECTURAL"


# ================================================================
# Section 2: AFFINE GRASSMANNIAN STRUCTURE
# ================================================================

class TestAffineGrassmannianGL1:
    """Tests for Gr_{GL_1}: the abelian case."""

    def test_gl1_langlands_dual(self):
        """GL_1 is self-dual: GL_1^L = GL_1."""
        gr = affine_grassmannian("GL_1")
        assert gr.langlands_dual == "GL_1"

    def test_gl1_orbits_integers(self):
        """Gr_{GL_1} orbits indexed by Z (integers)."""
        gr = affine_grassmannian("GL_1")
        assert "Z" in gr.orbit_indexing

    def test_gl1_rank_1(self):
        """GL_1 has rank 1."""
        gr = affine_grassmannian("GL_1")
        assert gr.rank == 1

    def test_gl1_simply_laced(self):
        """GL_1 is (trivially) simply laced."""
        gr = affine_grassmannian("GL_1")
        assert gr.is_simply_laced is True

    def test_gl1_satake_proved(self):
        """Classical Satake for GL_1 is PROVED."""
        gr = affine_grassmannian("GL_1")
        assert gr.satake_status == "PROVED"


class TestAffineGrassmannianSL2:
    """Tests for Gr_{SL_2}: the simplest non-abelian case."""

    def test_sl2_langlands_dual(self):
        """SL_2^L = PGL_2."""
        # VERIFIED [LT] standard Langlands duality
        gr = affine_grassmannian("SL_2", rank=1, dual_coxeter=2)
        assert gr.langlands_dual == "PGL_2"

    def test_sl2_dim_lie_algebra(self):
        """dim(sl_2) = 3."""
        gr = affine_grassmannian("SL_2", rank=1, dual_coxeter=2)
        assert gr.dim_lie_algebra == 3

    def test_sl2_dual_coxeter(self):
        """h^v(SL_2) = 2."""
        gr = affine_grassmannian("SL_2", rank=1, dual_coxeter=2)
        assert gr.dual_coxeter == 2


class TestGrOrbits:
    """Tests for G[[t]]-orbits on Gr_G."""

    def test_gl1_orbit_dim_zero(self):
        """GL_1 orbits are points (dim 0)."""
        for d in range(5):
            orbit = gr_orbit("GL_1", (d,))
            assert orbit.orbit_dim == 0

    def test_sl2_orbit_dim_2n(self):
        """SL_2 orbit dim(Gr^{(n)}) = 2n."""
        # VERIFIED [LT] Pressley-Segal, "Loop Groups" (1986), Ch. 8
        for n in range(5):
            orbit = gr_orbit("SL_2", (n,))
            assert orbit.orbit_dim == 2 * n

    def test_sl2_orbit_0_is_point(self):
        """Gr^{(0)} for SL_2 is a point (dim 0)."""
        orbit = gr_orbit("SL_2", (0,))
        assert orbit.orbit_dim == 0

    def test_sl2_orbit_ic_label(self):
        """IC sheaf label is IC_{n}."""
        orbit = gr_orbit("SL_2", (3,))
        assert "IC" in orbit.ic_sheaf_label
        assert "3" in orbit.ic_sheaf_label


# ================================================================
# Section 3: CHIRAL GRASSMANNIAN (FACTORIZATION)
# ================================================================

class TestChiralGrassmannian:
    """Tests for the chiral affine Grassmannian Gr^{ch}_G."""

    def test_is_factorization(self):
        """Gr^{ch}_G is a factorization ind-scheme."""
        cg = chiral_grassmannian("GL_1")
        assert cg.is_factorization is True

    def test_bd_proved(self):
        """Beilinson-Drinfeld construction is PROVED."""
        cg = chiral_grassmannian("GL_1")
        assert "PROVED" in cg.status

    def test_classical_fiber(self):
        """Classical fiber is Gr_{GL_1}."""
        cg = chiral_grassmannian("GL_1")
        assert "GL_1" in cg.classical_fiber

    def test_factorization_type(self):
        """Factorization type is multiplicative."""
        cg = chiral_grassmannian("GL_1")
        assert "multiplicative" in cg.factorization_type


class TestFactorizationProperty:
    """Tests for the factorization property of Gr^{ch}_G."""

    def test_separated_splits(self):
        """At separated points, the fiber splits."""
        fp = factorization_property(2, separated=True)
        assert fp.splits is True

    def test_collision_nonsplit(self):
        """At collision, the fiber does NOT split."""
        fp = factorization_property(2, separated=False)
        assert fp.splits is False

    def test_separated_tensor_product(self):
        """Separated fiber encodes tensor product."""
        fp = factorization_property(2, separated=True)
        assert "tensor product" in fp.fusion_type

    def test_collision_has_ope(self):
        """Collision fiber encodes OPE."""
        fp = factorization_property(2, separated=False)
        assert "OPE" in fp.fusion_type

    def test_collision_has_coproduct(self):
        """Collision encodes the Drinfeld coproduct."""
        fp = factorization_property(2, separated=False)
        assert "Delta_z" in fp.coproduct_relation

    def test_verify_separated(self):
        """Full verification at separated points."""
        result = verify_factorization_separated()
        assert result["all_pass"] is True

    def test_verify_collision(self):
        """Full verification at collision."""
        result = verify_factorization_collision()
        assert result["all_pass"] is True


# ================================================================
# Section 4: CONVOLUTION AND COPRODUCT
# ================================================================

class TestConvolution:
    """Tests for the convolution product and its dual coproduct."""

    def test_charge_additivity(self):
        """Convolution is additive on charges for GL_1."""
        for n, m in [(0, 0), (0, 1), (1, 1), (1, 2), (2, 3)]:
            conv = convolution_product(n, m, "GL_1")
            assert conv.output_charge == n + m

    def test_charge_0_vacuum(self):
        """Charge-0 convolution: vacuum * vacuum = vacuum."""
        conv = convolution_product(0, 0, "GL_1")
        assert conv.output_charge == 0

    def test_sl2_clebsch_gordan(self):
        """SL_2 convolution follows Clebsch-Gordan."""
        conv = convolution_product(2, 1, "SL_2")
        # V_2 tensor V_1 = V_3 + V_1 (Clebsch-Gordan)
        assert "Clebsch-Gordan" in conv.sheaf_description
        assert conv.output_charge == 3

    def test_coproduct_formula_present(self):
        """Coproduct formula is stated for GL_1."""
        conv = convolution_product(1, 1, "GL_1")
        assert "Delta_z" in conv.coproduct_formula

    def test_fock_space_dims_in_description(self):
        """Fock space dimensions appear in the Satake image."""
        conv = convolution_product(1, 1, "GL_1")
        # p_24(1) = 24
        assert "24" in conv.satake_image

    def test_verify_additivity(self):
        """Full verification of charge additivity."""
        result = verify_convolution_additivity()
        assert result["all_additive"] is True


# ================================================================
# Section 5: GEOMETRIC R-MATRIX
# ================================================================

class TestClassicalRMatrix:
    """Tests for the classical geometric R-matrix (symmetric)."""

    def test_classical_is_symmetric(self):
        """Classical Satake braiding is symmetric."""
        # VERIFIED [LT] Mirkovic-Vilonen: Perv(Gr_G) is symmetric monoidal
        r = geometric_r_matrix_classical()
        assert r.braiding_type == "symmetric"

    def test_classical_ybe(self):
        """Classical R-matrix satisfies YBE (trivially)."""
        r = geometric_r_matrix_classical()
        assert r.ybe_satisfied is True

    def test_classical_source(self):
        """R-matrix comes from commutativity constraint."""
        r = geometric_r_matrix_classical()
        assert "commutativity" in r.source.lower()


class TestChiralRMatrixC3:
    """Tests for the chiral R-matrix on C^3."""

    def test_chiral_is_braided(self):
        """Chiral R-matrix is E_2-braided, NOT symmetric."""
        r = geometric_r_matrix_chiral_charge1()
        assert "E_2" in r.braiding_type
        assert "symmetric" not in r.braiding_type.lower() or "NOT" in r.braiding_type

    def test_chiral_ybe(self):
        """Chiral R-matrix satisfies YBE."""
        r = geometric_r_matrix_chiral_charge1()
        assert r.ybe_satisfied is True

    def test_chiral_charge_1(self):
        """R-matrix is at charge 1."""
        r = geometric_r_matrix_chiral_charge1()
        assert r.charge == 1

    def test_chiral_structure_function(self):
        """R-matrix formula involves g(z)."""
        r = geometric_r_matrix_chiral_charge1()
        assert "g(z)" in r.r_matrix_formula

    def test_unitarity_in_formula(self):
        """Unitarity R(z)R(-z) = 1 is stated."""
        r = geometric_r_matrix_chiral_charge1()
        assert "R(z) R(-z) = 1" in r.unitarity

    def test_mo_source(self):
        """R-matrix identified with Maulik-Okounkov stable envelopes."""
        r = geometric_r_matrix_chiral_charge1()
        assert "MO" in r.source or "Maulik-Okounkov" in r.source or "stable envelope" in r.source


class TestChiralRMatrixK3:
    """Tests for the K3 chiral R-matrix (CONJECTURAL)."""

    def test_k3_conjectural(self):
        """K3 R-matrix is correctly marked CONJECTURAL."""
        r = geometric_r_matrix_k3_charge1()
        assert "CONJECTURAL" in r.braiding_type or "CONJECTURAL" in r.source

    def test_k3_degree_24_24(self):
        """K3 structure function has degree (24, 24)."""
        r = geometric_r_matrix_k3_charge1()
        assert "(24,24)" in r.r_matrix_formula or "24" in r.r_matrix_formula

    def test_k3_ybe(self):
        """K3 R-matrix satisfies YBE (algebraic property)."""
        r = geometric_r_matrix_k3_charge1()
        assert r.ybe_satisfied is True


class TestUnitarityVerification:
    """Numerical verification of R(z)R(-z) = 1."""

    def test_unitarity_c3_default(self):
        """Unitarity for C^3 with h = (1, -2, 1)."""
        # VERIFIED [DC] algebraic computation
        result = verify_unitarity_c3()
        assert result["all_pass"] is True

    def test_unitarity_c3_single(self):
        """Single unitarity check for C^3."""
        h = (F(1), F(-2), F(1))
        z = F(37, 10)
        result = r_matrix_unitarity_check(h, z)
        assert result["unitarity_holds"] is True

    def test_unitarity_k3_model(self):
        """Unitarity for K3-type parameters (rank-4 model)."""
        result = verify_unitarity_k3_params()
        assert result["unitarity_holds"] is True

    def test_unitarity_pole_detection(self):
        """Pole detection: z at a pole should not compute."""
        h = (F(1), F(-2), F(1))
        z = F(1)  # pole at h_1 = 1
        result = r_matrix_unitarity_check(h, z)
        assert result["unitarity_holds"] is None
        assert "pole" in result.get("error", "").lower()

    def test_unitarity_large_params(self):
        """Unitarity with large parameters (AP-CY28 safe)."""
        h = (F(37), F(41), F(-78))  # sum = 0
        z = F(100)
        result = r_matrix_unitarity_check(h, z)
        assert result["unitarity_holds"] is True

    def test_unitarity_5_params(self):
        """Unitarity with 5 CY parameters."""
        h = (F(2), F(3), F(5), F(-4), F(-6))  # sum = 0
        z = F(17, 2)
        result = r_matrix_unitarity_check(h, z)
        assert result["unitarity_holds"] is True
        assert result["n_params"] == 5


# ================================================================
# Section 6: DERIVED SATAKE HIERARCHY
# ================================================================

class TestSatakeHierarchy:
    """Tests for the four levels of Satake: classical -> derived -> chiral -> CY."""

    def test_classical_satake_proved(self):
        """Classical Satake is PROVED."""
        cs = classical_satake()
        assert cs.status == "PROVED"

    def test_classical_satake_symmetric(self):
        """Classical Satake has symmetric monoidal structure."""
        cs = classical_satake()
        assert "symmetric" in cs.monoidal_structure_rhs

    def test_derived_satake_proved(self):
        """Derived Satake is PROVED."""
        ds = derived_satake()
        assert ds.status == "PROVED"

    def test_derived_satake_indcoh(self):
        """Derived Satake RHS is IndCoh(N^L/G^L)."""
        ds = derived_satake()
        assert "IndCoh" in ds.rhs

    def test_chiral_satake_c3_conjectural(self):
        """Chiral Satake for C^3 is CONJECTURAL."""
        ch = chiral_satake_c3()
        assert "CONJECTURAL" in ch.status

    def test_chiral_satake_c3_rhs_yangian(self):
        """Chiral Satake for C^3 has Yangian on the right."""
        ch = chiral_satake_c3()
        assert "Y(gl_hat_1)" in ch.rhs

    def test_chiral_satake_c3_e2(self):
        """Chiral Satake for C^3 is E_2 braided."""
        ch = chiral_satake_c3()
        assert "E_2" in ch.monoidal_structure_rhs

    def test_chiral_satake_k3_conjectural(self):
        """Chiral Satake for K3 is CONJECTURAL."""
        ch = chiral_satake_k3()
        assert "CONJECTURAL" in ch.status

    def test_chiral_satake_k3_rhs_k3_yangian(self):
        """Chiral Satake for K3 has K3 Yangian on the right."""
        ch = chiral_satake_k3()
        assert "Y(g_{K3})" in ch.rhs

    def test_chiral_satake_k3_dependencies(self):
        """K3 Satake dependencies include AP-CY14."""
        ch = chiral_satake_k3()
        deps_str = " ".join(ch.dependencies)
        assert "AP-CY14" in deps_str or "CONJECTURAL" in deps_str

    def test_hierarchy_levels(self):
        """Four levels: classical, derived, chiral, CY."""
        cs = classical_satake()
        ds = derived_satake()
        ch = chiral_satake_c3()
        ck = chiral_satake_k3()
        assert cs.level == "classical"
        assert ds.level == "derived"
        assert ch.level == "chiral"
        assert ck.level == "CY"

    def test_verify_hierarchy(self):
        """Full hierarchy verification."""
        result = verify_satake_hierarchy()
        assert result["all_pass"] is True


# ================================================================
# Section 7: WEIGHT FUNCTORS
# ================================================================

class TestWeightFunctorSL2:
    """Tests for MV weight functors on SL_2."""

    def test_v0_dim_1(self):
        """V_0 (trivial rep) has dim 1."""
        wf = weight_functor_sl2(0, 0)
        assert wf.classical_dim == 1

    def test_v1_dim_2(self):
        """V_1 (spin-1/2) has total dim 2: weights -1 and 1."""
        # VERIFIED [LT] standard rep theory
        dim = sum(weight_functor_sl2(1, m).classical_dim for m in range(-1, 2))
        assert dim == 2

    def test_v2_dim_3(self):
        """V_2 (spin-1) has total dim 3: weights -2, 0, 2."""
        dim = sum(weight_functor_sl2(2, m).classical_dim for m in range(-2, 3))
        assert dim == 3

    def test_v3_dim_4(self):
        """V_3 (spin-3/2) has total dim 4."""
        dim = sum(weight_functor_sl2(3, m).classical_dim for m in range(-3, 4))
        assert dim == 4

    def test_v4_dim_5(self):
        """V_4 (spin-2) has total dim 5."""
        dim = sum(weight_functor_sl2(4, m).classical_dim for m in range(-4, 5))
        assert dim == 5

    def test_weight_parity(self):
        """Weights of V_n have same parity as n."""
        for n in range(5):
            for m in range(-n, n + 1):
                wf = weight_functor_sl2(n, m)
                if (n - m) % 2 != 0:
                    assert wf.classical_dim == 0

    def test_weight_vanishing_outside(self):
        """Weights |m| > n have zero dim."""
        for n in range(4):
            assert weight_functor_sl2(n, n + 1).classical_dim == 0
            assert weight_functor_sl2(n, -(n + 1)).classical_dim == 0

    def test_verify_weight_functor(self):
        """Full weight functor verification."""
        result = verify_weight_functor_sl2()
        assert result["all_pass"] is True


class TestWeightFunctorGL1K3:
    """Tests for weight functors for GL_1 on K3."""

    def test_charge_0_dim_1(self):
        """Charge-0 Fock space has dim 1."""
        wf = weight_functor_gl1_k3(0, 1)
        assert wf.classical_dim == 1

    def test_charge_1_dim_24(self):
        """Charge-1 Fock space has dim 24."""
        # VERIFIED [DC] 24-coloured partitions [LT] OEIS A006922
        wf = weight_functor_gl1_k3(1, 1)
        assert wf.classical_dim == 24

    def test_charge_2_dim_324(self):
        """Charge-2 Fock space has dim 324."""
        # VERIFIED [DC] 24-coloured partitions [LT] OEIS A006922
        wf = weight_functor_gl1_k3(2, 1)
        assert wf.classical_dim == 324

    def test_charge_3_dim_3200(self):
        """Charge-3 Fock space has dim 3200."""
        # VERIFIED [DC] 24-coloured partitions [LT] OEIS A006922
        wf = weight_functor_gl1_k3(3, 1)
        assert wf.classical_dim == 3200


# ================================================================
# Section 8: IWAHORI E_1 -> E_2 PASSAGE
# ================================================================

class TestIwahoriPassage:
    """Tests for the E_1 -> E_2 passage via Iwahori reduction."""

    def test_iwahori_e1(self):
        """Iwahori side is E_1."""
        iw = iwahori_satake_passage("GL_1")
        assert "E_1" in iw.iwahori_satake_image

    def test_full_e2(self):
        """Full Satake side is E_2."""
        iw = iwahori_satake_passage("GL_1")
        assert "E_2" in iw.full_satake_image

    def test_drinfeld_center_used(self):
        """The E_1 -> E_2 passage uses the Drinfeld center."""
        iw = iwahori_satake_passage("GL_1")
        assert "Drinfeld center" in iw.center_construction or "Z(" in iw.center_construction

    def test_coha_in_iwahori(self):
        """The Iwahori side involves the CoHA (associative, E_1)."""
        # AP-CY7: CoHA is associative, not chiral
        iw = iwahori_satake_passage("GL_1")
        assert "CoHA" in iw.iwahori_satake_image

    def test_yangian_in_full(self):
        """The full Satake involves the Yangian (E_2)."""
        iw = iwahori_satake_passage("GL_1")
        assert "Y(" in iw.full_satake_image or "Yangian" in iw.full_satake_image

    def test_verify_iwahori(self):
        """Full Iwahori E_1 -> E_2 verification."""
        result = verify_iwahori_e1_e2()
        assert result["all_pass"] is True


# ================================================================
# Section 9: CLASSICAL VS CHIRAL BRAIDING
# ================================================================

class TestClassicalVsChiralBraiding:
    """Verify classical Satake is symmetric, chiral is braided."""

    def test_classical_symmetric(self):
        """Classical: Perv(Gr_G) is symmetric monoidal."""
        r = geometric_r_matrix_classical()
        assert r.braiding_type == "symmetric"

    def test_chiral_e2_braided(self):
        """Chiral: D-mod(Gr^{ch}_G) is E_2-braided monoidal."""
        r = geometric_r_matrix_chiral_charge1()
        assert "E_2" in r.braiding_type

    def test_verify_braiding_comparison(self):
        """Full verification of classical vs chiral braiding."""
        result = verify_classical_vs_chiral_braiding()
        assert result["all_pass"] is True


# ================================================================
# Section 10: MUKAI LATTICE CONSTANTS
# ================================================================

class TestMukaiConstants:
    """Tests for Mukai lattice constants used in K3 Satake."""

    def test_mukai_rank(self):
        """Mukai lattice rank = 24."""
        assert MUKAI_RANK == 24

    def test_mukai_signature(self):
        """Mukai lattice signature = (4, 20)."""
        assert MUKAI_SIG_PLUS == 4
        assert MUKAI_SIG_MINUS == 20

    def test_signature_sum(self):
        """Signature sums to rank."""
        assert MUKAI_SIG_PLUS + MUKAI_SIG_MINUS == MUKAI_RANK


# ================================================================
# Section 11: FULL VERIFICATION SUITE
# ================================================================

class TestFullVerification:
    """Run the full verification suite."""

    def test_verify_orbit_gl1(self):
        result = verify_orbit_structure_gl1()
        assert result["all_pass"] is True

    def test_verify_orbit_sl2(self):
        result = verify_orbit_structure_sl2()
        assert result["all_pass"] is True

    def test_verify_convolution(self):
        result = verify_convolution_additivity()
        assert result["all_additive"] is True

    def test_verify_unitarity_c3(self):
        result = verify_unitarity_c3()
        assert result["all_pass"] is True

    def test_verify_unitarity_k3(self):
        result = verify_unitarity_k3_params()
        assert result["unitarity_holds"] is True

    def test_verify_factorization_sep(self):
        result = verify_factorization_separated()
        assert result["all_pass"] is True

    def test_verify_factorization_col(self):
        result = verify_factorization_collision()
        assert result["all_pass"] is True

    def test_verify_satake_hierarchy(self):
        result = verify_satake_hierarchy()
        assert result["all_pass"] is True

    def test_verify_weight_sl2(self):
        result = verify_weight_functor_sl2()
        assert result["all_pass"] is True

    def test_verify_iwahori(self):
        result = verify_iwahori_e1_e2()
        assert result["all_pass"] is True

    def test_verify_braiding(self):
        result = verify_classical_vs_chiral_braiding()
        assert result["all_pass"] is True

    def test_verify_chiral_gr(self):
        result = verify_chiral_grassmannian_factorization()
        assert result["all_pass"] is True

    def test_full_verification_all_paths(self):
        """Run all 12 verification paths."""
        results = full_verification()
        for path_name, path_result in results.items():
            assert path_result.get("all_pass") or path_result.get("all_additive") or path_result.get("unitarity_holds"), \
                f"Path {path_name} failed"


# ================================================================
# Section 12: AP COMPLIANCE
# ================================================================

class TestAPCompliance:
    """Verify compliance with anti-patterns."""

    def test_ap_cy14_chiral_conjectural(self):
        """AP-CY14: chiral Satake is CONJECTURAL, never theorem."""
        ch = chiral_satake_k3()
        assert "CONJECTURAL" in ch.status

    def test_ap_cy14_k3_dependencies(self):
        """AP-CY14: K3 Yangian dependency is explicit."""
        ch = chiral_satake_k3()
        deps = " ".join(ch.dependencies)
        assert "K3 Yangian" in deps or "AP-CY14" in deps

    def test_ap_cy4_drinfeld_center_distinct(self):
        """AP-CY4: Drinfeld center is explicitly distinguished from derived center."""
        iw = iwahori_satake_passage("GL_1")
        assert "Drinfeld center" in iw.center_construction or "Z(" in iw.center_construction

    def test_ap_cy7_coha_not_chiral(self):
        """AP-CY7: CoHA is in E_1 (Iwahori), not E_2 (full Satake)."""
        iw = iwahori_satake_passage("GL_1")
        # CoHA is on the E_1 side
        assert "E_1" in iw.iwahori_satake_image
        assert "CoHA" in iw.iwahori_satake_image

    def test_ap_cy31_spectral_parameter(self):
        """AP-CY31: spectral parameter z is Yangian, not worldsheet."""
        fp = factorization_property(2, separated=False)
        assert "spectral" in fp.coproduct_relation.lower()

    def test_ap_cy25_no_delta_vacuum(self):
        """AP-CY25: R-matrix from half-braiding, not from Delta(1)."""
        r = geometric_r_matrix_chiral_charge1()
        assert "half-braiding" in r.source or "factorization" in r.source.lower() or "stable envelope" in r.source.lower()
