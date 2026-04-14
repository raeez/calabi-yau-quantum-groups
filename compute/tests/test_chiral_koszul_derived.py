r"""Tests for derived chiral Koszul duality engine.

Verifies the derived (infinity-categorical) Koszul duality adjunction
following the CFG25 paradigm, lifted to the E_1-chiral world.

MATHEMATICAL CLAIMS TESTED:

1. CONDUCTOR PRESERVATION: K^{der} = K_classical for all shadow classes.
   This is the A_infinity master equation (Stasheff telescoping).

2. BARR-BECK-LURIE CONDITIONS: the derived adjunction is monadic
   for all five standard families.

3. SHADOW CLASS -> DERIVED BEHAVIOUR:
   G -> classical exact (B^{der} = B)
   L -> finite corrections (m_3 only)
   M -> Gevrey-1 divergent (Borel summable)

4. STRUCTURE FUNCTION INVERSION: for the affine Yangian,
   g(u) * g^!(u) = 1 at all test points.

5. CFG25 HIERARCHY: E_1 -> E_2 -> E_3 Koszul duality cascade.

6. DERIVED BAR COMPLEX: partition function dimensions, formality,
   A_infinity correction structure.

7. INFINITY-CATEGORICAL EQUIVALENCE: type (strict/quasi/derived)
   matches the shadow class.

GROUND TRUTH:
  Heisenberg:   K = 0,   class G, B^{der} = B
  Kac-Moody:    K = 0,   class L, 1 correction (m_3)
  Virasoro:     K = 13,  class M, infinite corrections
  Yangian:      K = 0,   class L, 1 correction (Serre)
  K3 Mukai:     K = 0,   class G, B^{der} = B

Manuscript references:
  chapters/theory/e2_chiral_algebras.tex: sec:e2-koszul-and-bar
  chapters/theory/braided_factorization.tex: sec:braided-bar-cobar
  chapters/theory/e1_chiral_algebras.tex: sec:e1-koszul-three-families
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.chiral_koszul_derived import (
    # Data types
    DerivedKoszulDualData,
    DerivedBarData,
    InftyCatEquivalenceData,
    # Constants
    EN_KOSZUL_SHIFTS,
    SHADOW_CLASS_DERIVED,
    CONDUCTOR_GROUND_TRUTH,
    AINF_CORRECTION_STRUCTURE,
    # Operadic
    en_koszul_shift,
    en_operad_arity_dim,
    derived_en_operad_data,
    # Families
    heisenberg_derived_koszul,
    kac_moody_sl2_derived_koszul,
    kac_moody_general_derived_koszul,
    virasoro_derived_koszul,
    affine_yangian_derived_koszul,
    k3_mukai_derived_koszul,
    # Bar complex
    derived_bar_heisenberg,
    derived_bar_kac_moody_sl2,
    derived_bar_virasoro,
    derived_bar_affine_yangian,
    # Equivalences
    infty_cat_equivalence_heisenberg,
    infty_cat_equivalence_kac_moody,
    infty_cat_equivalence_virasoro,
    infty_cat_equivalence_yangian,
    # Conductor
    derived_conductor,
    conductor_comparison_table,
    # CFG25
    cfg25_hierarchy,
    cfg25_comparison,
    # Monad
    koszul_resolution_monad,
    # Master verification
    verify_derived_koszul_all_families,
    verify_conductor_universality,
    # Structure function
    yangian_structure_function,
    yangian_dual_structure_function,
    verify_structure_function_inversion,
)


# =========================================================================
# 1. E_n Koszul shift verification
# =========================================================================

class TestEnKoszulShift:
    """E_n^! = E_n{-n}: the Koszul shift equals n."""

    def test_e1_shift(self):
        """E_1^! = E_1{-1}: shift 1 = dim(R)."""
        assert en_koszul_shift(1) == 1

    def test_e2_shift(self):
        """E_2^! = E_2{-2}: shift 2 = dim(C)."""
        assert en_koszul_shift(2) == 2

    def test_e3_shift(self):
        """E_3^! = E_3{-3}: shift 3 = dim(R^3)."""
        assert en_koszul_shift(3) == 3

    def test_shift_constants(self):
        """Verify the EN_KOSZUL_SHIFTS dictionary."""
        for n in [1, 2, 3]:
            assert EN_KOSZUL_SHIFTS[n] == n

    def test_operad_arity_dim_factorial(self):
        """dim E_n(k) = k! for all n >= 1."""
        for n in [1, 2, 3]:
            for k in range(1, 6):
                from math import factorial
                assert en_operad_arity_dim(n, k) == factorial(k)

    def test_derived_operad_data_self_dual(self):
        """E_n is Koszul self-dual for all n >= 1."""
        for n in [1, 2, 3]:
            data = derived_en_operad_data(n)
            assert data["is_koszul_self_dual"]
            assert data["self_dual_with_shift"] == n


# =========================================================================
# 2. Derived Koszul duality: Heisenberg (class G)
# =========================================================================

class TestDerivedKoszulHeisenberg:
    """Derived Koszul duality for H_k: B^{der} = B (class G, formal)."""

    def test_dual_name(self):
        """Koszul dual of H_1 is H_{-1}."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert "H_-1" in data.dual_name

    def test_shadow_class_G(self):
        """Heisenberg is class G."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert data.shadow_class == "G"

    def test_derived_equals_classical(self):
        """For class G, derived = classical."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert data.derived_equals_classical

    def test_conductor_zero(self):
        """K = K^{der} = 0 for Heisenberg."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert data.conductor_classical == Fraction(0)
        assert data.conductor_derived == Fraction(0)

    def test_kappa_complementarity(self):
        """kappa_ch + kappa_ch^! = 0."""
        for k_val in [1, 2, 3, -1, Fraction(1, 2)]:
            k = Fraction(k_val)
            data = heisenberg_derived_koszul(k)
            assert data.kappa_ch + data.kappa_ch_dual == Fraction(0)

    def test_no_ainf_corrections(self):
        """Class G has 0 A_infinity corrections."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert data.num_ainf_corrections == 0

    def test_comparison_map_isomorphism(self):
        """B^{der} -> B is an isomorphism for class G."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert data.comparison_map_type == "isomorphism"

    def test_monadicity(self):
        """No monadicity obstruction for class G."""
        data = heisenberg_derived_koszul(Fraction(1))
        assert "none" in data.monadicity_obstruction


# =========================================================================
# 3. Derived Koszul duality: Kac-Moody sl_2 (class L)
# =========================================================================

class TestDerivedKoszulKacMoody:
    """Derived Koszul duality for V_k(sl_2): class L, one m_3 correction."""

    def test_feigin_frenkel_dual_level(self):
        """k' = -k - 4 (FF involution for sl_2)."""
        data = kac_moody_sl2_derived_koszul(Fraction(1))
        assert "V_-5" in data.dual_name

    def test_shadow_class_L(self):
        """V_k(sl_2) is class L."""
        data = kac_moody_sl2_derived_koszul(Fraction(1))
        assert data.shadow_class == "L"

    def test_derived_not_classical(self):
        """For class L, derived != classical (m_3 correction)."""
        data = kac_moody_sl2_derived_koszul(Fraction(1))
        assert not data.derived_equals_classical

    def test_conductor_zero(self):
        """K = K^{der} = 0 for KM algebras."""
        for k_val in [1, 2, 3, -1, -3]:
            k = Fraction(k_val)
            data = kac_moody_sl2_derived_koszul(k)
            assert data.conductor_classical == Fraction(0)
            assert data.conductor_derived == Fraction(0)

    def test_kappa_complementarity(self):
        """kappa_ch(V_k) + kappa_ch(V_{k'}) = 0."""
        for k_val in [1, 2, 3, -1, -3, 10]:
            k = Fraction(k_val)
            data = kac_moody_sl2_derived_koszul(k)
            assert data.kappa_ch + data.kappa_ch_dual == Fraction(0)

    def test_one_ainf_correction(self):
        """Class L has exactly 1 A_infinity correction (m_3)."""
        data = kac_moody_sl2_derived_koszul(Fraction(1))
        assert data.num_ainf_corrections == 1

    def test_comparison_map_quasi_iso(self):
        """B^{der} -> B is a quasi-isomorphism for class L."""
        data = kac_moody_sl2_derived_koszul(Fraction(1))
        assert data.comparison_map_type == "quasi-isomorphism"

    def test_critical_level_self_dual(self):
        """At k = -2 (critical level), k' = -k - 4 = -2 = k: self-dual."""
        data = kac_moody_sl2_derived_koszul(Fraction(-2))
        assert data.kappa_ch == Fraction(0)

    def test_general_lie_algebras(self):
        """Conductor K = 0 for general simple Lie algebras."""
        lie_data = [
            (3, 2, "sl_2"),
            (8, 3, "sl_3"),
            (15, 4, "sl_4"),
            (14, 4, "G_2"),
            (248, 30, "E_8"),
        ]
        for dim_g, h_dual, g_name in lie_data:
            data = kac_moody_general_derived_koszul(dim_g, h_dual, g_name)
            assert data.conductor_classical == Fraction(0)
            assert data.conductor_derived == Fraction(0)


# =========================================================================
# 4. Derived Koszul duality: Virasoro (class M)
# =========================================================================

class TestDerivedKoszulVirasoro:
    """Derived Koszul duality for Vir_c: class M, infinite corrections."""

    def test_virasoro_involution(self):
        """c' = 26 - c."""
        data = virasoro_derived_koszul(Fraction(1))
        assert "Vir_25" in data.dual_name

    def test_shadow_class_M(self):
        """Virasoro is class M."""
        data = virasoro_derived_koszul(Fraction(1))
        assert data.shadow_class == "M"

    def test_shadow_depth_infinite(self):
        """Class M has infinite shadow depth."""
        data = virasoro_derived_koszul(Fraction(1))
        assert data.shadow_depth is None

    def test_derived_not_classical(self):
        """For class M, derived != classical."""
        data = virasoro_derived_koszul(Fraction(1))
        assert not data.derived_equals_classical

    def test_conductor_13(self):
        """K = K^{der} = 13 for Virasoro."""
        for c_val in [0, 1, 2, 13, 25, 26]:
            c = Fraction(c_val)
            data = virasoro_derived_koszul(c)
            assert data.conductor_classical == Fraction(13)
            assert data.conductor_derived == Fraction(13)

    def test_kappa_complementarity(self):
        """kappa_ch(Vir_c) + kappa_ch(Vir_{c'}) = 13."""
        for c_val in [0, 1, 2, Fraction(1, 2), 13, 25, 26]:
            c = Fraction(c_val)
            data = virasoro_derived_koszul(c)
            assert data.kappa_ch + data.kappa_ch_dual == Fraction(13)

    def test_infinite_ainf_corrections(self):
        """Class M has infinitely many A_infinity corrections."""
        data = virasoro_derived_koszul(Fraction(1))
        assert data.num_ainf_corrections == "infinite"

    def test_comparison_map_borel(self):
        """B^{der} -> B comparison is Borel resummation for class M."""
        data = virasoro_derived_koszul(Fraction(1))
        assert data.comparison_map_type == "Borel_resummation"

    def test_self_dual_point_c13(self):
        """c = 13 is the self-dual point: c' = 26 - 13 = 13."""
        data = virasoro_derived_koszul(Fraction(13))
        assert data.kappa_ch == Fraction(13, 2)
        assert data.kappa_ch_dual == Fraction(13, 2)
        assert data.kappa_ch == data.kappa_ch_dual


# =========================================================================
# 5. Derived Koszul duality: Affine Yangian (class L)
# =========================================================================

class TestDerivedKoszulYangian:
    """Derived Koszul duality for Y(gl_hat_1): CFG25 analogue at E_1."""

    def test_shadow_class_L(self):
        """Affine Yangian is class L."""
        data = affine_yangian_derived_koszul()
        assert data.shadow_class == "L"

    def test_conductor_zero(self):
        """K = 0 for the Yangian family."""
        data = affine_yangian_derived_koszul()
        assert data.conductor_classical == Fraction(0)
        assert data.conductor_derived == Fraction(0)

    def test_kappa_complementarity(self):
        """kappa_ch + kappa_ch^! = 0."""
        data = affine_yangian_derived_koszul()
        assert data.kappa_ch + data.kappa_ch_dual == Fraction(0)

    def test_level_computation(self):
        """Level k = -sigma_2 = -(h1*h2 + h1*h3 + h2*h3)."""
        h1, h2 = Rational(1), Rational(-2)
        h3 = -(h1 + h2)  # = 1
        sigma_2 = h1 * h2 + h1 * h3 + h2 * h3
        data = affine_yangian_derived_koszul(h1, h2)
        assert data.kappa_ch == Fraction(-sigma_2)

    def test_dual_has_inverted_structure_function(self):
        """The Koszul dual has g^! = 1/g."""
        data = affine_yangian_derived_koszul()
        assert "1/g" in data.dual_name

    def test_one_ainf_correction(self):
        """Class L has 1 correction (Serre relation)."""
        data = affine_yangian_derived_koszul()
        assert data.num_ainf_corrections == 1


# =========================================================================
# 6. Derived Koszul duality: K3 Mukai (class G, rank 24)
# =========================================================================

class TestDerivedKoszulK3:
    """Derived Koszul duality for K3 Mukai Heisenberg."""

    def test_shadow_class_G(self):
        """K3 Mukai Heisenberg is class G."""
        data = k3_mukai_derived_koszul()
        assert data.shadow_class == "G"

    def test_kappa_ch_2(self):
        """kappa_ch(A_{K3}) = 2 = chi(O_{K3})."""
        data = k3_mukai_derived_koszul()
        assert data.kappa_ch == Fraction(2)

    def test_kappa_ch_dual_minus_2(self):
        """kappa_ch(A_{K3}^!) = -2."""
        data = k3_mukai_derived_koszul()
        assert data.kappa_ch_dual == Fraction(-2)

    def test_conductor_zero(self):
        """K = 0 for class G."""
        data = k3_mukai_derived_koszul()
        assert data.conductor_classical == Fraction(0)
        assert data.conductor_derived == Fraction(0)

    def test_derived_equals_classical(self):
        """For class G, derived = classical."""
        data = k3_mukai_derived_koszul()
        assert data.derived_equals_classical

    def test_en_level_2(self):
        """K3 lives at E_2 level (CY_2)."""
        data = k3_mukai_derived_koszul()
        assert data.en_level == 2

    def test_signature_flip(self):
        """Koszul dual signature: (4,20) -> (20,4)."""
        data = k3_mukai_derived_koszul()
        assert "sig (4,20)" in data.name
        assert "sig (20,4)" in data.dual_name


# =========================================================================
# 7. Derived bar complex
# =========================================================================

class TestDerivedBarComplex:
    """Derived bar complex B^{der}(A) for each family."""

    def test_heisenberg_formal(self):
        """Heisenberg is formal: B^{der} = B."""
        bar = derived_bar_heisenberg()
        assert bar.is_formal
        assert bar.differentials_vanish
        assert len(bar.ainf_corrections) == 0

    def test_heisenberg_partition_dimensions(self):
        """B^{der}(H_k) has dim p(n) at weight n."""
        bar = derived_bar_heisenberg()
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22]
        for n in range(len(expected)):
            assert bar.weight_dimensions[n] == expected[n]

    def test_kac_moody_not_formal(self):
        """V_k(sl_2) is NOT formal (m_3 correction)."""
        bar = derived_bar_kac_moody_sl2()
        assert not bar.is_formal
        assert not bar.differentials_vanish
        assert len(bar.ainf_corrections) == 1

    def test_kac_moody_three_generators(self):
        """V_k(sl_2) has 3 generators (e, f, h)."""
        bar = derived_bar_kac_moody_sl2()
        assert len(bar.generators) == 3

    def test_virasoro_not_formal(self):
        """Virasoro is NOT formal (infinite tower)."""
        bar = derived_bar_virasoro()
        assert not bar.is_formal
        assert not bar.differentials_vanish

    def test_virasoro_shadow_corrections(self):
        """Virasoro has corrections m_3=-2, m_4=40/27."""
        bar = derived_bar_virasoro()
        assert len(bar.ainf_corrections) >= 2
        assert bar.ainf_corrections[0] == (3, Fraction(-2))
        assert bar.ainf_corrections[1] == (4, Fraction(40, 27))

    def test_yangian_three_generators(self):
        """Affine Yangian has 3 generators (e, f, psi)."""
        bar = derived_bar_affine_yangian()
        assert len(bar.generators) == 3

    def test_yangian_not_formal(self):
        """Affine Yangian is NOT formal (Serre correction)."""
        bar = derived_bar_affine_yangian()
        assert not bar.is_formal


# =========================================================================
# 8. Infinity-categorical equivalence
# =========================================================================

class TestInftyCatEquivalence:
    """The infinity-categorical equivalence (CFG25 paradigm)."""

    def test_heisenberg_strict_equivalence(self):
        """Class G: strict equivalence (no higher coherences)."""
        eq = infty_cat_equivalence_heisenberg()
        assert eq.equivalence_type == "strict"
        assert eq.monadicity
        assert eq.comonadicity

    def test_kac_moody_quasi_equivalence(self):
        """Class L: quasi-equivalence."""
        eq = infty_cat_equivalence_kac_moody()
        assert eq.equivalence_type == "quasi"
        assert eq.monadicity

    def test_virasoro_derived_equivalence(self):
        """Class M: derived equivalence (Borel resummation)."""
        eq = infty_cat_equivalence_virasoro()
        assert eq.equivalence_type == "derived"
        assert eq.monadicity

    def test_yangian_quasi_equivalence(self):
        """Yangian: quasi-equivalence (class L)."""
        eq = infty_cat_equivalence_yangian()
        assert eq.equivalence_type == "quasi"
        assert eq.monadicity

    def test_barr_beck_conditions_all_pass(self):
        """Barr-Beck-Lurie conditions satisfied for all families."""
        for eq_func in [
            infty_cat_equivalence_heisenberg,
            infty_cat_equivalence_kac_moody,
            infty_cat_equivalence_virasoro,
            infty_cat_equivalence_yangian,
        ]:
            eq = eq_func()
            bb = eq.barr_beck_conditions
            assert bb["BB1_conservative"]
            assert bb["BB2_preserves_geometric_realizations"]

    def test_lurie_conditions_met(self):
        """Lurie monadicity conditions satisfied for all families."""
        for eq_func in [
            infty_cat_equivalence_heisenberg,
            infty_cat_equivalence_kac_moody,
            infty_cat_equivalence_virasoro,
            infty_cat_equivalence_yangian,
        ]:
            eq = eq_func()
            assert eq.lurie_conditions_met


# =========================================================================
# 9. Conductor preservation theorem
# =========================================================================

class TestConductorPreservation:
    """K^{der} = K_classical universally (A_infinity master equation)."""

    def test_conductor_universality(self):
        """Verify K^{der} = K for all families at multiple parameters."""
        results = verify_conductor_universality()
        for family, passed in results.items():
            assert passed, f"Conductor preservation failed for {family}"

    def test_conductor_heisenberg_parametric(self):
        """K = 0 for Heisenberg at 7 parameter values."""
        for k_val in [1, 2, 3, -1, -5, Fraction(1, 2), Fraction(7, 3)]:
            k = Fraction(k_val)
            data = heisenberg_derived_koszul(k)
            cond = derived_conductor(data.kappa_ch, data.kappa_ch_dual, "G")
            assert cond["conductors_agree"]
            assert cond["derived_conductor"] == Fraction(0)

    def test_conductor_virasoro_parametric(self):
        """K = 13 for Virasoro at 7 parameter values."""
        for c_val in [0, 1, 2, Fraction(1, 2), 13, 25, 26]:
            c = Fraction(c_val)
            data = virasoro_derived_koszul(c)
            cond = derived_conductor(data.kappa_ch, data.kappa_ch_dual, "M")
            assert cond["conductors_agree"]
            assert cond["derived_conductor"] == Fraction(13)

    def test_conductor_comparison_table(self):
        """All entries in the comparison table have K^{der} = K."""
        table = conductor_comparison_table()
        for row in table:
            assert row["agree"], f"Failed for {row['family']}"

    def test_conductor_ground_truth(self):
        """Conductor values match ground truth constants."""
        assert heisenberg_derived_koszul(Fraction(1)).conductor_classical == CONDUCTOR_GROUND_TRUTH["Heisenberg"]
        assert kac_moody_sl2_derived_koszul(Fraction(1)).conductor_classical == CONDUCTOR_GROUND_TRUTH["Kac-Moody"]
        assert virasoro_derived_koszul(Fraction(1)).conductor_classical == CONDUCTOR_GROUND_TRUTH["Virasoro"]
        assert affine_yangian_derived_koszul().conductor_classical == CONDUCTOR_GROUND_TRUTH["Yangian"]
        assert k3_mukai_derived_koszul().conductor_classical == CONDUCTOR_GROUND_TRUTH["K3_Mukai"]


# =========================================================================
# 10. Structure function inversion (Yangian Koszul dual)
# =========================================================================

class TestStructureFunctionInversion:
    """g(u) * g^!(u) = 1: the Yangian Koszul dual inverts g."""

    def test_inversion_default_params(self):
        """g * g^! = 1 at h = (1, -2, 1), test points far from poles."""
        result = verify_structure_function_inversion()
        assert result["all_inversions_verified"]

    def test_inversion_alternative_params(self):
        """g * g^! = 1 at h = (2, -3, 1)."""
        result = verify_structure_function_inversion(
            h1=Rational(2), h2=Rational(-3)
        )
        assert result["all_inversions_verified"]

    def test_inversion_at_specific_point(self):
        """g(37) * g^!(37) = 1 at default parameters."""
        g = yangian_structure_function(Rational(37))
        g_dual = yangian_dual_structure_function(Rational(37))
        assert g * g_dual == 1

    def test_inversion_large_params(self):
        """g * g^! = 1 with large Omega-background parameters (AP-CY28)."""
        result = verify_structure_function_inversion(
            h1=Rational(37), h2=Rational(41),
            test_points=[Rational(100), Rational(200), Rational(-150)],
        )
        assert result["all_inversions_verified"]

    def test_structure_function_not_one(self):
        """g(u) is not identically 1 (it encodes genuine data)."""
        g = yangian_structure_function(Rational(37))
        assert g != 1


# =========================================================================
# 11. CFG25 hierarchy
# =========================================================================

class TestCFG25Hierarchy:
    """The dimensional hierarchy E_1 -> E_2 -> E_3."""

    def test_hierarchy_three_levels(self):
        """Three levels: E_1 (3d), E_2 (5d), E_3 (6d)."""
        hierarchy = cfg25_hierarchy()
        assert "E_1" in hierarchy
        assert "E_2" in hierarchy
        assert "E_3" in hierarchy

    def test_e1_proved(self):
        """E_1 level (3d hol CS -> KM) is PROVED."""
        hierarchy = cfg25_hierarchy()
        assert "PROVED" in hierarchy["E_1"]["status"]

    def test_e3_conjectural(self):
        """E_3 level (6d -> quantum toroidal) is CONJECTURAL."""
        hierarchy = cfg25_hierarchy()
        assert "CONJECTURAL" in hierarchy["E_3"]["status"]

    def test_cfg25_comparison_product(self):
        """g * g^! = 1 in the CFG25 comparison."""
        result = cfg25_comparison()
        assert result["product_is_one"]

    def test_hierarchy_dimensions(self):
        """hol CS dimensions: 3, 5, 6."""
        hierarchy = cfg25_hierarchy()
        assert hierarchy["E_1"]["hol_cs_dim"] == 3
        assert hierarchy["E_2"]["hol_cs_dim"] == 5
        assert hierarchy["E_3"]["hol_cs_dim"] == 6


# =========================================================================
# 12. Koszul resolution monad
# =========================================================================

class TestKoszulResolutionMonad:
    """The monad T = Omega^{der} o B^{der}."""

    def test_class_G_identity(self):
        """For class G: T = id (identity monad)."""
        monad = koszul_resolution_monad("G", 2)
        assert monad["monad_type"] == "identity"
        assert monad["resolution_length"] == 0

    def test_class_L_idempotent(self):
        """For class L: T is idempotent (finite resolution)."""
        monad = koszul_resolution_monad("L", 2)
        assert monad["monad_type"] == "idempotent"

    def test_class_C_convergent(self):
        """For class C: T converges."""
        monad = koszul_resolution_monad("C")
        assert monad["monad_type"] == "convergent"

    def test_class_M_borel(self):
        """For class M: T is Borel (Gevrey-1 divergent)."""
        monad = koszul_resolution_monad("M")
        assert monad["monad_type"] == "Borel"
        assert "Borel" in monad["convergence"]

    def test_barr_beck_all_classes(self):
        """Barr-Beck satisfied for all shadow classes."""
        for cls in ["G", "L", "C", "M"]:
            monad = koszul_resolution_monad(cls)
            assert "satisfied" in monad["barr_beck"]


# =========================================================================
# 13. Master verification pipeline
# =========================================================================

class TestMasterVerification:
    """Full pipeline: all five families pass all checks."""

    def test_all_families_pass(self):
        """All five families pass the master verification."""
        results = verify_derived_koszul_all_families()
        for family, data in results.items():
            assert data["all_checks_pass"], f"Master verification failed for {family}"

    def test_five_families_present(self):
        """All five standard families are tested."""
        results = verify_derived_koszul_all_families()
        expected = {"Heisenberg", "Kac-Moody_sl2", "Virasoro", "Yangian", "K3_Mukai"}
        assert set(results.keys()) == expected


# =========================================================================
# 14. Shadow class -> derived behaviour consistency
# =========================================================================

class TestShadowClassDerivedBehaviour:
    """Shadow class determines the type of derived Koszul duality."""

    def test_class_G_classical_exact(self):
        """Class G -> classical exact."""
        assert SHADOW_CLASS_DERIVED["G"] == "classical_exact"

    def test_class_L_finite_corrections(self):
        """Class L -> finite corrections."""
        assert SHADOW_CLASS_DERIVED["L"] == "finite_corrections"

    def test_class_C_convergent_series(self):
        """Class C -> convergent series."""
        assert SHADOW_CLASS_DERIVED["C"] == "convergent_series"

    def test_class_M_gevrey_divergent(self):
        """Class M -> Gevrey-1 divergent."""
        assert SHADOW_CLASS_DERIVED["M"] == "gevrey_1_divergent"

    def test_ainf_structure_class_G(self):
        """Class G: 0 corrections, formal."""
        data = AINF_CORRECTION_STRUCTURE["G"]
        assert data["num_corrections"] == 0
        assert data["formal"]

    def test_ainf_structure_class_L(self):
        """Class L: 1 correction (m_3), not formal."""
        data = AINF_CORRECTION_STRUCTURE["L"]
        assert data["num_corrections"] == 1
        assert data["highest_nonzero_mn"] == 3
        assert not data["formal"]

    def test_ainf_structure_class_M(self):
        """Class M: infinite corrections, all m_n nonzero."""
        data = AINF_CORRECTION_STRUCTURE["M"]
        assert data["num_corrections"] == "infinite"
        assert data["highest_nonzero_mn"] == "all"
        assert not data["formal"]


# =========================================================================
# 15. Multi-path cross-checks with existing engines (AP10)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification against existing Vol III engines.

    Path 1: chiral_koszul_derived (this engine)
    Path 2: e1_koszul_three_families (classical E_1 Koszul)
    Path 3: e2_koszul_heisenberg (E_2 Koszul for Heisenberg)
    Path 4: e2_koszul_k3_landscape (E_2 Koszul for K3)
    Path 5: e2_barcobar_koszul (E_2 bar-cobar adjunction)
    Path 6: holomorphic_cs_chiral_engine (hCS boundary algebras)
    """

    # --- Path 1 x Path 2: derived engine vs e1_koszul_three_families ---

    def test_heisenberg_kappa_path1_vs_path2(self):
        """kappa_ch(H_k): derived engine vs e1_koszul_three_families.

        Path 1: heisenberg_derived_koszul(k).kappa_ch
        Path 2: heisenberg_kappa_ch(k) from e1_koszul_three_families
        """
        from compute.lib.e1_koszul_three_families import heisenberg_kappa_ch
        for k_val in [1, 2, 3, -1, Fraction(1, 2), Fraction(7, 3)]:
            k = Fraction(k_val)
            path1 = heisenberg_derived_koszul(k).kappa_ch
            path2 = heisenberg_kappa_ch(k)
            assert path1 == path2, f"Heisenberg kappa mismatch at k={k}: {path1} vs {path2}"

    def test_heisenberg_conductor_path1_vs_path2(self):
        """Conductor(H_k): derived engine vs e1_koszul_three_families.

        Path 1: heisenberg_derived_koszul(k).conductor_derived
        Path 2: heisenberg_verify_conductor(k)["sum"] from e1
        """
        from compute.lib.e1_koszul_three_families import heisenberg_verify_conductor
        for k_val in [1, 2, 3, -1, Fraction(1, 2)]:
            k = Fraction(k_val)
            path1 = heisenberg_derived_koszul(k).conductor_derived
            path2_result = heisenberg_verify_conductor(k)
            path2 = path2_result["sum"]
            assert path1 == path2, f"Conductor mismatch at k={k}: {path1} vs {path2}"

    def test_virasoro_kappa_path1_vs_path2(self):
        """kappa_ch(Vir_c): derived engine vs e1_koszul_three_families.

        Path 1: virasoro_derived_koszul(c).kappa_ch
        Path 2: virasoro_kappa_ch(c) from e1_koszul_three_families
        """
        from compute.lib.e1_koszul_three_families import virasoro_kappa_ch
        for c_val in [0, 1, 2, Fraction(1, 2), 13, 25, 26]:
            c = Fraction(c_val)
            path1 = virasoro_derived_koszul(c).kappa_ch
            path2 = virasoro_kappa_ch(c)
            assert path1 == path2, f"Virasoro kappa mismatch at c={c}: {path1} vs {path2}"

    def test_virasoro_conductor_path1_vs_path2(self):
        """Conductor(Vir_c): derived engine vs e1_koszul_three_families.

        Path 1: virasoro_derived_koszul(c).conductor_derived
        Path 2: virasoro_verify_conductor(c)["sum"] from e1
        """
        from compute.lib.e1_koszul_three_families import virasoro_verify_conductor
        for c_val in [0, 1, 2, 13, 25, 26]:
            c = Fraction(c_val)
            path1 = virasoro_derived_koszul(c).conductor_derived
            path2_result = virasoro_verify_conductor(c)
            path2 = path2_result["sum"]
            assert path1 == path2, f"Conductor mismatch at c={c}: {path1} vs {path2}"

    def test_km_kappa_path1_vs_path2(self):
        """kappa_ch(V_k(sl_2)): derived engine vs e1_koszul_three_families.

        Path 1: kac_moody_sl2_derived_koszul(k).kappa_ch
        Path 2: kac_moody_sl2_kappa_ch(k) from e1_koszul_three_families
        """
        from compute.lib.e1_koszul_three_families import kac_moody_sl2_kappa_ch
        for k_val in [1, 2, 3, -1, -3, 10]:
            k = Fraction(k_val)
            path1 = kac_moody_sl2_derived_koszul(k).kappa_ch
            path2 = kac_moody_sl2_kappa_ch(k)
            assert path1 == path2, f"KM kappa mismatch at k={k}: {path1} vs {path2}"

    def test_km_conductor_path1_vs_path2(self):
        """Conductor(V_k): derived engine vs e1_koszul_three_families.

        Path 1: kac_moody_sl2_derived_koszul(k).conductor_derived
        Path 2: kac_moody_sl2_verify_conductor(k)["sum"] from e1
        """
        from compute.lib.e1_koszul_three_families import kac_moody_sl2_verify_conductor
        for k_val in [1, 2, 3, -1, -3]:
            k = Fraction(k_val)
            path1 = kac_moody_sl2_derived_koszul(k).conductor_derived
            path2_result = kac_moody_sl2_verify_conductor(k)
            path2 = path2_result["sum"]
            assert path1 == path2, f"Conductor mismatch at k={k}: {path1} vs {path2}"

    def test_km_general_conductor_path1_vs_path2(self):
        """Conductor(V_k(g)): derived engine vs e1_koszul_three_families.

        Path 1: kac_moody_general_derived_koszul(...).conductor_derived
        Path 2: kac_moody_general_verify_conductor(...)["sum"] from e1
        """
        from compute.lib.e1_koszul_three_families import kac_moody_general_verify_conductor
        lie_data = [
            (3, 2, "sl_2"),
            (8, 3, "sl_3"),
            (15, 4, "sl_4"),
            (14, 4, "G_2"),
            (248, 30, "E_8"),
        ]
        for dim_g, h_dual, g_name in lie_data:
            k = Fraction(1)
            path1 = kac_moody_general_derived_koszul(dim_g, h_dual, g_name, k).conductor_derived
            path2_result = kac_moody_general_verify_conductor(dim_g, h_dual, k)
            path2 = path2_result["sum"]
            assert path1 == path2, f"Conductor mismatch for {g_name}: {path1} vs {path2}"

    # --- Path 1 x Path 3: derived engine vs e2_koszul_heisenberg ---

    def test_heisenberg_e2_kappa_path1_vs_path3(self):
        """kappa_ch(H_k): derived engine vs E2BarComplexHeisenberg.

        Path 1: heisenberg_derived_koszul(k).kappa_ch
        Path 3: E2BarComplexHeisenberg(omega).kappa_ch()
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        from compute.lib.e2_koszul_heisenberg import E2BarComplexHeisenberg
        # At (1, 0, -1): level = -sigma_2 = -(0 + (-1) + 0) = 1
        omega = OmegaBackground(1, 0)
        e2bar = E2BarComplexHeisenberg(omega)
        path3_kappa = e2bar.kappa_ch()
        path3_dual = e2bar.kappa_ch_dual()
        path3_sum = e2bar.kappa_sum()
        # Derived engine at same level
        level = e2bar.level
        path1 = heisenberg_derived_koszul(Fraction(level))
        assert Fraction(path1.kappa_ch) == Fraction(path3_kappa), \
            f"kappa mismatch: derived={path1.kappa_ch}, e2={path3_kappa}"
        assert Fraction(path1.kappa_ch_dual) == Fraction(path3_dual), \
            f"kappa_dual mismatch: derived={path1.kappa_ch_dual}, e2={path3_dual}"
        assert Fraction(path1.conductor_derived) == Fraction(path3_sum), \
            f"conductor mismatch: derived={path1.conductor_derived}, e2={path3_sum}"

    def test_heisenberg_e2_braiding_reversal_path1_vs_path3(self):
        """Braiding reversal: derived engine vs E2BarComplexHeisenberg.

        Path 1: comparison_map_type == 'isomorphism' (class G)
        Path 3: E2BarComplexHeisenberg.braiding_is_reversed()
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground
        from compute.lib.e2_koszul_heisenberg import E2BarComplexHeisenberg
        omega = OmegaBackground(1, -2)
        e2bar = E2BarComplexHeisenberg(omega)
        # Path 3: braiding IS reversed for Koszul dual
        assert e2bar.braiding_is_reversed()
        # Path 1: Heisenberg at this level is class G, derived = classical
        level = e2bar.level
        path1 = heisenberg_derived_koszul(Fraction(level))
        assert path1.derived_equals_classical
        assert path1.shadow_class == "G"

    def test_heisenberg_bar_dims_path1_vs_path3(self):
        """Bar complex partition dimensions: derived engine vs e2_koszul_heisenberg.

        Path 1: derived_bar_heisenberg.weight_dimensions[n]
        Path 3: _partition_count(n) from holomorphic_cs_chiral_engine
        """
        from compute.lib.holomorphic_cs_chiral_engine import _partition_count
        bar = derived_bar_heisenberg(max_weight=10)
        for n in range(11):
            path1 = bar.weight_dimensions[n]
            path3 = _partition_count(n)
            assert path1 == path3, f"Partition dim mismatch at n={n}: {path1} vs {path3}"

    # --- Path 1 x Path 4: derived engine vs e2_koszul_k3_landscape ---

    def test_k3_kappa_path1_vs_path4(self):
        """kappa_ch(K3): derived engine vs e2_koszul_k3_landscape.

        Path 1: k3_mukai_derived_koszul().kappa_ch
        Path 4: KAPPA_CH_K3 from e2_koszul_k3_landscape
        """
        from compute.lib.e2_koszul_k3_landscape import KAPPA_CH_K3, KAPPA_CH_K3_DUAL
        path1 = k3_mukai_derived_koszul()
        assert path1.kappa_ch == KAPPA_CH_K3, \
            f"K3 kappa mismatch: derived={path1.kappa_ch}, landscape={KAPPA_CH_K3}"
        assert path1.kappa_ch_dual == KAPPA_CH_K3_DUAL, \
            f"K3 kappa_dual mismatch: derived={path1.kappa_ch_dual}, landscape={KAPPA_CH_K3_DUAL}"

    def test_k3_conductor_path1_vs_path4(self):
        """K3 conductor: derived engine vs e2_koszul_k3_landscape.

        Path 1: k3_mukai_derived_koszul().conductor_derived
        Path 4: KAPPA_CH_K3 + KAPPA_CH_K3_DUAL from landscape
        """
        from compute.lib.e2_koszul_k3_landscape import KAPPA_CH_K3, KAPPA_CH_K3_DUAL
        path1 = k3_mukai_derived_koszul().conductor_derived
        path4 = KAPPA_CH_K3 + KAPPA_CH_K3_DUAL
        assert path1 == path4, f"K3 conductor mismatch: derived={path1}, landscape={path4}"

    # --- Path 1 x Path 5: derived engine vs e2_barcobar_koszul ---

    def test_e2_koszul_shift_path1_vs_path5(self):
        """E_2 Koszul shift: derived engine vs e2_barcobar_koszul.

        Path 1: en_koszul_shift(2)
        Path 5: e2_koszul_shift() from e2_barcobar_koszul
        """
        from compute.lib.e2_barcobar_koszul import e2_koszul_shift
        path1 = en_koszul_shift(2)
        path5 = e2_koszul_shift()
        assert path1 == path5, f"E_2 shift mismatch: derived={path1}, barcobar={path5}"

    def test_en_koszul_shift_path1_vs_path5(self):
        """E_n Koszul shifts: derived engine vs e2_barcobar_koszul.

        Path 1: en_koszul_shift(n) for n=1,2,3
        Path 5: en_koszul_shift(n) from e2_barcobar_koszul
        """
        from compute.lib.e2_barcobar_koszul import en_koszul_shift as path5_shift
        for n in [1, 2, 3]:
            path1 = en_koszul_shift(n)
            path5 = path5_shift(n)
            assert path1 == path5, f"E_{n} shift mismatch: derived={path1}, barcobar={path5}"

    # --- Path 1 x Path 6: derived engine vs holomorphic_cs_chiral_engine ---

    def test_yangian_level_path1_vs_path6(self):
        """Yangian level: derived engine vs holomorphic_cs_chiral_engine.

        Path 1: affine_yangian_derived_koszul().kappa_ch
        Path 6: BoundaryAlgebra(2, omega).kappa_ch() (which calls omega.kac_moody_level())
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground, BoundaryAlgebra
        h1, h2 = Rational(1), Rational(-2)
        omega = OmegaBackground(h1, h2)
        ba = BoundaryAlgebra(2, omega)
        path6_kappa = ba.kappa_ch()
        path1 = affine_yangian_derived_koszul(h1, h2)
        assert Fraction(path1.kappa_ch) == Fraction(path6_kappa), \
            f"Yangian kappa mismatch: derived={path1.kappa_ch}, hCS={path6_kappa}"

    def test_koszul_dual_kappa_path1_vs_path6(self):
        """Koszul dual kappa: derived engine vs holomorphic_cs_chiral_engine.

        Path 1: heisenberg_derived_koszul(k).kappa_ch_dual
        Path 6: KoszulDual(ba).kappa_ch_dual()
        """
        from compute.lib.holomorphic_cs_chiral_engine import OmegaBackground, BoundaryAlgebra, KoszulDual
        omega = OmegaBackground(1, 0)
        ba = BoundaryAlgebra(1, omega)
        kd = KoszulDual(ba)
        path6_kappa_dual = kd.kappa_ch_dual()
        level = omega.kac_moody_level()
        path1 = heisenberg_derived_koszul(Fraction(level))
        assert Fraction(path1.kappa_ch_dual) == Fraction(path6_kappa_dual), \
            f"Dual kappa mismatch: derived={path1.kappa_ch_dual}, hCS={path6_kappa_dual}"

    # --- Internal multi-path: structure function inversion via two methods ---

    def test_structure_function_inversion_two_paths(self):
        """g * g^! = 1 verified via explicit formula AND cfg25_comparison.

        Path A: verify_structure_function_inversion (direct evaluation)
        Path B: cfg25_comparison (product_is_one check)
        """
        path_a = verify_structure_function_inversion()
        path_b = cfg25_comparison()
        assert path_a["all_inversions_verified"], "Path A (direct) failed"
        assert path_b["product_is_one"], "Path B (cfg25) failed"

    # --- Internal multi-path: conductor via table AND direct computation ---

    def test_conductor_table_vs_direct(self):
        """Conductor: comparison table vs direct computation, all families.

        Path A: conductor_comparison_table() (tabular path)
        Path B: family-specific derived_koszul functions (direct path)
        """
        table = conductor_comparison_table()
        # Extract Heisenberg k=1 row from table
        h1_row = [r for r in table if "H_1" in r["family"]][0]
        path_a = h1_row["K_derived"]
        path_b = heisenberg_derived_koszul(Fraction(1)).conductor_derived
        assert path_a == path_b, f"Heisenberg conductor: table={path_a} vs direct={path_b}"

        # Extract Vir_1 row
        v1_row = [r for r in table if "Vir_1" in r["family"]][0]
        path_a = v1_row["K_derived"]
        path_b = virasoro_derived_koszul(Fraction(1)).conductor_derived
        assert path_a == path_b, f"Virasoro conductor: table={path_a} vs direct={path_b}"
