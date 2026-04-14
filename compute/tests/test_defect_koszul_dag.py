"""Tests for the defect algebra from Koszul duality in derived algebraic geometry.

Verifies the five-stage DAG pipeline:
    Stage 1 (Bulk) -> Stage 2 (Bar) -> Stage 3 (Defect) -> Stage 4 (Conductor)
    Stage 2 -> Stage 5 (Morita)

GROUND TRUTH (from CLAUDE.md, manuscript, and existing engines):

  K3 (d=2, PROVED):
    kappa_ch(A_{K3}) = 2, kappa_ch(A_{K3}^!) = -2, K = 0
    Shadow class: G, shadow depth: 2

  K3 x E free-field (d=3, CONJECTURAL):
    kappa_ch = 3, kappa_ch^! = -3, K = 0
    Shadow class: G, shadow depth: 2

  K3 x E BKM (d=3, CONJECTURAL):
    kappa_ch = 3, kappa_ch^! = 2, K = 5 = kappa_BKM
    Shadow class: M, shadow depth: infinite

  C^3 (d=3, partially proved):
    kappa_ch = 1, kappa_ch^! = -1, K = 0
    Shadow class: G, shadow depth: 2

  Heisenberg H_k (PROVED):
    kappa_ch = k, kappa_ch^! = -k, K = 0
    Shadow class: G, shadow depth: 2

  Virasoro Vir_c (PROVED):
    kappa_ch = c/2, kappa_ch^! = (26-c)/2, K = 13
    Shadow class: M, shadow depth: infinite

Multi-path verification:
  Path 1: DAG pipeline (this engine)
  Path 2: Direct computation (e1_koszul_three_families.py ground truth)
  Path 3: Structure function inversion (k3_yangian.py)
  Path 4: Braiding reversal (e2_koszul_heisenberg.py)
  Path 5: Mirror Koszul diagnostics (k3_mirror_koszul.py)

Manuscript references:
  chapters/theory/quantum_chiral_algebras.tex:
    Construction constr:universal-defect
    Conjecture conj:chiral-qg-k3xe
    Construction constr:k3-boundary-defect
  chapters/theory/e1_chiral_algebras.tex:
    Section sec:e1-koszul-three-families
"""

import pytest
from fractions import Fraction

from compute.lib.defect_koszul_dag import (
    BulkAlgebraData,
    BarComplexData,
    ClaimStatus,
    CYDimension,
    DefectAlgebraData,
    DefectKoszulPipeline,
    KappaSpectrum,
    MoritaEquivalenceData,
    ShadowClass,
    c3_pipeline,
    cross_check_e1_koszul,
    cross_check_virasoro,
    elliptic_curve_pipeline,
    heisenberg_pipeline,
    k3_pipeline,
    k3_structure_function_inversion,
    k3xe_bkm_pipeline,
    k3xe_free_field_pipeline,
    master_verification,
    verify_all_conductors,
    verify_braiding_reversal,
    verify_structure_function_inversion,
    virasoro_pipeline,
)


# =========================================================================
# 1. K3 (d=2, PROVED): the central test case
# =========================================================================

class TestK3Pipeline:
    """K3 surface: CY-A_2 proved, the load-bearing verified case."""

    def setup_method(self):
        self.pipeline = k3_pipeline()

    # --- Stage 1: Bulk algebra ---

    def test_k3_bulk_kappa_ch(self):
        """kappa_ch(A_{K3}) = 2 (= chi(O_{K3}))."""
        assert self.pipeline.bulk.kappa_ch == Fraction(2)

    def test_k3_bulk_shadow_class_G(self):
        """K3 lattice VOA is class G (free-field)."""
        assert self.pipeline.bulk.shadow_class == ShadowClass.G

    def test_k3_bulk_shadow_depth_2(self):
        """Shadow depth = 2 for class G."""
        assert self.pipeline.bulk.shadow_depth == 2

    def test_k3_bulk_cy_dim(self):
        """K3 is CY dimension 2."""
        assert self.pipeline.bulk.cy_dim == CYDimension.D2

    def test_k3_bulk_rank_24(self):
        """Mukai lattice has rank 24."""
        assert self.pipeline.bulk.rank == 24

    def test_k3_bulk_proved(self):
        """CY-A_2 is proved."""
        assert self.pipeline.bulk.claim_status == ClaimStatus.PROVED_ELSEWHERE

    # --- Stage 2: Bar complex ---

    def test_k3_bar_differential_trivial(self):
        """d_bar = 0 for class G (free-field)."""
        assert self.pipeline.bar.differential_trivial is True

    def test_k3_bar_no_ainf_corrections(self):
        """No A_infinity corrections for class G."""
        assert self.pipeline.bar.a_inf_corrections is False

    def test_k3_bar_arity_1_dim(self):
        """Bar complex at arity 1: 24 generators (Mukai rank)."""
        assert self.pipeline.bar.dim_arity_1 == 24

    def test_k3_bar_arity_2_dim(self):
        """Bar complex at arity 2: 24^2 = 576."""
        assert self.pipeline.bar.dim_arity_2 == 576

    # --- Stage 3: Defect algebra ---

    def test_k3_defect_kappa_ch(self):
        """kappa_ch(A_{K3}^!) = -2 (free-field branch: K=0)."""
        assert self.pipeline.defect.kappa_ch == Fraction(-2)

    def test_k3_defect_conductor_zero(self):
        """Koszul conductor K = 0 for K3 on free-field branch."""
        assert self.pipeline.defect.koszul_conductor == Fraction(0)

    def test_k3_defect_structure_fn_inverted(self):
        """g^!(u) = 1/g(u) for the K3 Koszul dual."""
        assert self.pipeline.defect.structure_function_inverted is True

    def test_k3_defect_braiding_reversed(self):
        """Rep^{E_2}(A^!) = Rep^{E_2}(A)^{rev} (reversed braiding)."""
        assert self.pipeline.defect.braiding_reversed is True

    # --- Stage 4: Conductor verification ---

    def test_k3_conductor_verified(self):
        """kappa_ch(A) + kappa_ch(A^!) = K = 0 verified."""
        result = self.pipeline.verify_conductor()
        assert result['verified'] is True

    def test_k3_conductor_value(self):
        """K = 2 + (-2) = 0."""
        result = self.pipeline.verify_conductor()
        assert result['kappa_sum'] == Fraction(0)
        assert result['koszul_conductor'] == Fraction(0)

    # --- Stage 5: Morita equivalence ---

    def test_k3_morita_is_koszul(self):
        """K3 is on the Koszul locus (class G)."""
        assert self.pipeline.morita.is_koszul is True

    def test_k3_morita_cobar_recovers(self):
        """Omega(B(A_{K3})) ~ A_{K3}."""
        assert self.pipeline.morita.cobar_recovers_A is True

    def test_k3_morita_e2_level(self):
        """Morita equivalence at E_2 level for d=2."""
        assert self.pipeline.morita.en_level == 2

    # --- Full pipeline ---

    def test_k3_full_pipeline(self):
        """Full 5-stage pipeline for K3."""
        result = self.pipeline.full_verification()
        assert result['cy_dim'] == 2
        assert result['stage_4_conductor']['verified'] is True
        assert result['stage_5_morita']['is_koszul'] is True


# =========================================================================
# 2. K3 x E free-field branch (CONJECTURAL)
# =========================================================================

class TestK3xEFreeFieldPipeline:
    """K3 x E free-field/gl_1 branch: all results conditional on CY-A_3."""

    def setup_method(self):
        self.pipeline = k3xe_free_field_pipeline()

    def test_k3xe_ff_bulk_kappa_ch(self):
        """kappa_ch(A_{K3xE}) = 3 (additivity: 2+1)."""
        assert self.pipeline.bulk.kappa_ch == Fraction(3)

    def test_k3xe_ff_bulk_conjectural(self):
        """K3xE bulk is CONJECTURAL (depends on CY-A_3)."""
        assert self.pipeline.bulk.claim_status == ClaimStatus.CONJECTURED

    def test_k3xe_ff_bulk_depends_on_cy_a3(self):
        """Dependency chain includes CY-A_3."""
        assert "CY-A_3" in self.pipeline.bulk.dependencies

    def test_k3xe_ff_defect_kappa_ch(self):
        """kappa_ch(A^!) = -3 on the free-field branch."""
        assert self.pipeline.defect.kappa_ch == Fraction(-3)

    def test_k3xe_ff_conductor_zero(self):
        """K = 0 on the free-field branch."""
        assert self.pipeline.defect.koszul_conductor == Fraction(0)

    def test_k3xe_ff_conductor_verified(self):
        """3 + (-3) = 0 verified."""
        result = self.pipeline.verify_conductor()
        assert result['verified'] is True

    def test_k3xe_ff_defect_conjectural(self):
        """Defect algebra is CONJECTURAL (conditionality propagates, AP-CY11)."""
        assert self.pipeline.defect.claim_status == ClaimStatus.CONJECTURED

    def test_k3xe_ff_morita_e1_level(self):
        """Morita at E_1 level for d=3 (then E_2 via Drinfeld center)."""
        # For d=3: min(3, 2) = 2. But the E_1 bar-cobar is the base;
        # E_2 comes from the Drinfeld center passage.
        assert self.pipeline.morita.en_level == 2

    def test_k3xe_ff_full_pipeline(self):
        """Full pipeline for K3xE free-field."""
        result = self.pipeline.full_verification()
        assert result['cy_dim'] == 3
        assert result['stage_4_conductor']['verified'] is True
        assert result['stage_3_defect']['claim_status'] == 'Conjectured'


# =========================================================================
# 3. K3 x E BKM branch (CONJECTURAL, nonzero conductor)
# =========================================================================

class TestK3xEBKMPipeline:
    """K3 x E BKM/holographic branch: K = 5 (nonzero conductor)."""

    def setup_method(self):
        self.pipeline = k3xe_bkm_pipeline()

    def test_k3xe_bkm_bulk_kappa_ch(self):
        """kappa_ch = 3 on both branches."""
        assert self.pipeline.bulk.kappa_ch == Fraction(3)

    def test_k3xe_bkm_class_M(self):
        """BKM branch is class M (infinite shadow depth)."""
        assert self.pipeline.bulk.shadow_class == ShadowClass.M
        assert self.pipeline.bulk.shadow_depth is None

    def test_k3xe_bkm_defect_kappa_ch(self):
        """kappa_ch(A^!) = 2 on the BKM branch (K=5, kappa=3)."""
        assert self.pipeline.defect.kappa_ch == Fraction(2)

    def test_k3xe_bkm_conductor_five(self):
        """K = 5 = kappa_BKM on the BKM branch."""
        assert self.pipeline.defect.koszul_conductor == Fraction(5)

    def test_k3xe_bkm_conductor_verified(self):
        """3 + 2 = 5 verified."""
        result = self.pipeline.verify_conductor()
        assert result['verified'] is True
        assert result['kappa_sum'] == Fraction(5)

    def test_k3xe_bkm_kappa_spectrum(self):
        """Full kappa spectrum: ch=3, BKM=5, cat=2, fiber=24."""
        spec = self.pipeline.kappa_spectrum
        assert spec.kappa_ch == Fraction(3)
        assert spec.kappa_BKM == Fraction(5)
        assert spec.kappa_cat == Fraction(2)
        assert spec.kappa_fiber == Fraction(24)


# =========================================================================
# 4. C^3 reference case
# =========================================================================

class TestC3Pipeline:
    """C^3 (resolved): the toric CY3 reference case."""

    def setup_method(self):
        self.pipeline = c3_pipeline()

    def test_c3_bulk_kappa_ch(self):
        """kappa_ch(W_{1+inf}) = 1 for gl_1."""
        assert self.pipeline.bulk.kappa_ch == Fraction(1)

    def test_c3_defect_kappa_ch(self):
        """kappa_ch(W_{1+inf}^!) = -1."""
        assert self.pipeline.defect.kappa_ch == Fraction(-1)

    def test_c3_conductor_zero(self):
        """K = 0 for C^3 (class G)."""
        result = self.pipeline.verify_conductor()
        assert result['verified'] is True
        assert result['kappa_sum'] == Fraction(0)

    def test_c3_class_G(self):
        """W_{1+inf} at generic Psi is class G."""
        assert self.pipeline.bulk.shadow_class == ShadowClass.G


# =========================================================================
# 5. Elliptic curve (d=1, trivial)
# =========================================================================

class TestEllipticCurvePipeline:
    """Elliptic curve: d=1, trivial case."""

    def setup_method(self):
        self.pipeline = elliptic_curve_pipeline()

    def test_e_bulk_kappa_ch(self):
        """kappa_ch(H_1) = 1."""
        assert self.pipeline.bulk.kappa_ch == Fraction(1)

    def test_e_defect_kappa_ch(self):
        """kappa_ch(H_1^!) = -1."""
        assert self.pipeline.defect.kappa_ch == Fraction(-1)

    def test_e_conductor_zero(self):
        """K = 0 for d=1."""
        result = self.pipeline.verify_conductor()
        assert result['verified'] is True


# =========================================================================
# 6. Heisenberg family (cross-check with e1_koszul_three_families)
# =========================================================================

class TestHeisenbergCrossCheck:
    """Cross-check against e1_koszul_three_families.py."""

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(-1), Fraction(1, 2), Fraction(7, 3),
    ])
    def test_heisenberg_conductor_zero(self, k):
        """kappa_ch(H_k) + kappa_ch(H_k^!) = 0 for all k."""
        pipeline = heisenberg_pipeline(k)
        result = pipeline.verify_conductor()
        assert result['verified'] is True
        assert result['kappa_sum'] == Fraction(0)

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(3),
    ])
    def test_heisenberg_cross_check(self, k):
        """Cross-check against direct computation."""
        result = cross_check_e1_koszul(k)
        assert result['match'] is True

    def test_heisenberg_defect_kappa_is_neg_k(self):
        """kappa_ch(H_k^!) = -k for all k."""
        for k in [Fraction(1), Fraction(5), Fraction(-3)]:
            pipeline = heisenberg_pipeline(k)
            assert pipeline.defect.kappa_ch == -k


# =========================================================================
# 7. Virasoro family (cross-check, nonzero conductor)
# =========================================================================

class TestVirassoroCrossCheck:
    """Cross-check against e1_koszul_three_families.py."""

    @pytest.mark.parametrize("c", [
        Fraction(0), Fraction(1), Fraction(13), Fraction(25), Fraction(26),
    ])
    def test_virasoro_conductor_13(self, c):
        """kappa_ch(Vir_c) + kappa_ch(Vir_{26-c}) = 13 for all c."""
        pipeline = virasoro_pipeline(c)
        result = pipeline.verify_conductor()
        assert result['verified'] is True
        assert result['kappa_sum'] == Fraction(13)

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(13), Fraction(26)])
    def test_virasoro_cross_check(self, c):
        """Cross-check against direct computation."""
        result = cross_check_virasoro(c)
        assert result['match'] is True

    def test_virasoro_self_dual_c13(self):
        """At c=13: kappa_ch = 13/2, kappa_ch^! = 13/2, K = 13."""
        pipeline = virasoro_pipeline(Fraction(13))
        assert pipeline.defect.kappa_ch == Fraction(13, 2)
        assert pipeline.bulk.kappa_ch == Fraction(13, 2)


# =========================================================================
# 8. Structure function inversion
# =========================================================================

class TestStructureFunctionInversion:
    """Verify g^!(u) = 1/g(u) for the K3 Yangian."""

    def test_k3_unitarity(self):
        """g(u) * g(-u) = 1 for K3 parameters."""
        result = k3_structure_function_inversion()
        assert result['all_pass'] is True

    def test_k3_inversion_n24(self):
        """Inversion identity with 24 parameters."""
        result = k3_structure_function_inversion(n_test_points=10)
        assert result['n_params'] == 24
        assert result['all_pass'] is True

    def test_generic_unitarity(self):
        """g(u)*g(-u)=1 for generic CY parameters (3 parameters, C^3)."""
        import numpy as np
        h = np.array([1.0, -2.0, 1.0])  # h1+h2+h3=0
        # AP-CY28: avoid poles at +/-h_i = +/-1, +/-2
        test_u = np.array([5.0, 10.0, 15.0, 20.0])
        result = verify_structure_function_inversion(h, test_u)
        assert result['all_pass'] is True

    def test_symmetric_params_unitarity(self):
        """g(u)*g(-u)=1 for symmetric parameters."""
        import numpy as np
        # 6 parameters: 3 positive, 3 negative, sum=0
        h = np.array([2.0, 3.0, 5.0, -2.0, -3.0, -5.0])
        test_u = np.array([7.0, 11.0, 13.0, 17.0])
        result = verify_structure_function_inversion(h, test_u)
        assert result['all_pass'] is True


# =========================================================================
# 9. Braiding reversal
# =========================================================================

class TestBraidingReversal:
    """Verify braiding reversal for the defect algebra."""

    def test_k3_braiding_reversed(self):
        """K3: kappa^! = -2 = -kappa, so braiding is reversed."""
        result = verify_braiding_reversal(Fraction(2), Fraction(-2))
        assert result['braiding_reversed'] is True
        assert result['is_free_field_branch'] is True

    def test_heisenberg_braiding_reversed(self):
        """H_k: braiding reversed on free-field branch."""
        for k in [Fraction(1), Fraction(3), Fraction(-2)]:
            result = verify_braiding_reversal(k, -k)
            assert result['braiding_reversed'] is True

    def test_virasoro_braiding_not_simply_reversed(self):
        """Vir_c: K=13, NOT free-field, braiding reversal is more subtle."""
        result = verify_braiding_reversal(Fraction(1, 2), Fraction(25, 2))
        assert result['is_free_field_branch'] is False


# =========================================================================
# 10. Conditionality propagation (AP-CY11)
# =========================================================================

class TestConditionalityPropagation:
    """AP-CY11: conditionality on CY-A_3 propagates through all stages."""

    def test_k3xe_defect_is_conjectural(self):
        """K3xE defect algebra inherits CONJECTURED status."""
        pipeline = k3xe_free_field_pipeline()
        assert pipeline.defect.claim_status == ClaimStatus.CONJECTURED

    def test_k3xe_morita_is_conjectural(self):
        """K3xE Morita equivalence inherits CONJECTURED status."""
        pipeline = k3xe_free_field_pipeline()
        assert pipeline.morita.claim_status == ClaimStatus.CONJECTURED

    def test_k3_defect_is_proved(self):
        """K3 defect algebra is PROVED (CY-A_2 is proved)."""
        pipeline = k3_pipeline()
        assert pipeline.defect.claim_status == ClaimStatus.PROVED_ELSEWHERE

    def test_k3_morita_is_proved(self):
        """K3 Morita equivalence is PROVED."""
        pipeline = k3_pipeline()
        assert pipeline.morita.claim_status == ClaimStatus.PROVED_ELSEWHERE

    def test_bkm_defect_is_conjectural(self):
        """K3xE BKM defect is CONJECTURED."""
        pipeline = k3xe_bkm_pipeline()
        assert pipeline.defect.claim_status == ClaimStatus.CONJECTURED


# =========================================================================
# 11. Kappa spectrum (AP113: zero tolerance for bare kappa)
# =========================================================================

class TestKappaSpectrum:
    """AP113: verify all kappa values are subscripted."""

    def test_k3_spectrum(self):
        """K3: ch=2, BKM=None, cat=2, fiber=24."""
        pipeline = k3_pipeline()
        s = pipeline.kappa_spectrum
        assert s.kappa_ch == Fraction(2)
        assert s.kappa_BKM is None
        assert s.kappa_cat == Fraction(2)
        assert s.kappa_fiber == Fraction(24)

    def test_k3xe_bkm_spectrum(self):
        """K3xE BKM: ch=3, BKM=5, cat=2, fiber=24."""
        pipeline = k3xe_bkm_pipeline()
        s = pipeline.kappa_spectrum
        assert s.kappa_ch == Fraction(3)
        assert s.kappa_BKM == Fraction(5)
        assert s.kappa_cat == Fraction(2)
        assert s.kappa_fiber == Fraction(24)

    def test_kappa_ch_plus_kappa_bkm_for_k3xe(self):
        """kappa_ch(3) + kappa_BKM(5) = 8, not equal."""
        pipeline = k3xe_bkm_pipeline()
        s = pipeline.kappa_spectrum
        assert s.kappa_ch != s.kappa_BKM
        assert s.kappa_ch + s.kappa_BKM == Fraction(8)


# =========================================================================
# 12. Master verification: all targets
# =========================================================================

class TestMasterVerification:
    """Run all pipelines and check global consistency."""

    def test_all_conductors_verified(self):
        """All Koszul conductors verified across all standard targets."""
        results = verify_all_conductors()
        for name, verified in results.items():
            assert verified, f"Conductor verification failed for {name}"

    def test_master_returns_all_targets(self):
        """Master verification returns results for all targets."""
        results = master_verification()
        expected = {
            'elliptic_curve', 'heisenberg_k1', 'heisenberg_k2',
            'heisenberg_k_neg', 'k3', 'c3',
            'k3xe_free_field', 'k3xe_bkm',
            'virasoro_c1', 'virasoro_c13', 'virasoro_c26',
        }
        assert set(results.keys()) == expected

    def test_free_field_conductors_zero(self):
        """All class G targets have K = 0."""
        class_g_targets = ['elliptic_curve', 'heisenberg_k1', 'k3', 'c3',
                           'k3xe_free_field']
        results = master_verification()
        for name in class_g_targets:
            K = results[name]['stage_4_conductor']['koszul_conductor']
            assert K == Fraction(0), f"{name}: expected K=0, got {K}"

    def test_class_M_conductors_positive(self):
        """Class M targets have K > 0 (when BKM data available)."""
        results = master_verification()
        k3xe_bkm = results['k3xe_bkm']
        assert k3xe_bkm['stage_4_conductor']['koszul_conductor'] == Fraction(5)

    def test_virasoro_conductor_13(self):
        """All Virasoro targets have K = 13."""
        results = master_verification()
        for name in ['virasoro_c1', 'virasoro_c13', 'virasoro_c26']:
            K = results[name]['stage_4_conductor']['kappa_sum']
            assert K == Fraction(13), f"{name}: expected sum=13, got {K}"


# =========================================================================
# 13. DAG structure verification
# =========================================================================

class TestDAGStructure:
    """Verify the DAG dependency structure of the pipeline."""

    def test_bar_depends_on_bulk(self):
        """Bar complex uses bulk shadow class."""
        pipeline = k3_pipeline()
        assert pipeline.bar.shadow_class == pipeline.bulk.shadow_class

    def test_defect_depends_on_bar(self):
        """Defect inherits shadow class from bar."""
        pipeline = k3_pipeline()
        assert pipeline.defect.shadow_class == pipeline.bar.shadow_class

    def test_morita_depends_on_bar(self):
        """Morita uses bar data (koszul locus check)."""
        pipeline = k3_pipeline()
        # Class G -> koszul locus
        assert pipeline.bar.shadow_class == ShadowClass.G
        assert pipeline.morita.is_koszul is True

    def test_pipeline_is_lazy(self):
        """Pipeline stages are computed lazily (on first access)."""
        pipeline = k3_pipeline()
        # Before access, internal cache should be None
        assert pipeline._bar is None
        assert pipeline._defect is None
        assert pipeline._morita is None
        # After access, cache is populated
        _ = pipeline.bar
        assert pipeline._bar is not None
        _ = pipeline.defect
        assert pipeline._defect is not None
        _ = pipeline.morita
        assert pipeline._morita is not None


# =========================================================================
# 14. Anti-pattern compliance
# =========================================================================

class TestAntiPatternCompliance:
    """Verify compliance with the AP-CY anti-patterns."""

    def test_ap_cy6_no_constructed_k3xe(self):
        """AP-CY6: K3xE bulk is NOT constructed, claim is CONJECTURED."""
        pipeline = k3xe_free_field_pipeline()
        assert pipeline.bulk.claim_status == ClaimStatus.CONJECTURED

    def test_ap_cy10_flop_not_koszul(self):
        """AP-CY10: Flop preserves kappa; Koszul inverts (K=0 branch).

        K3 Koszul: kappa goes from 2 to -2 (inverted).
        K3 flop: would preserve kappa at 2.
        These are different operations.
        """
        pipeline = k3_pipeline()
        assert pipeline.bulk.kappa_ch == Fraction(2)
        assert pipeline.defect.kappa_ch == Fraction(-2)
        # Flop would give kappa = 2 (preserved), NOT -2
        assert pipeline.defect.kappa_ch != pipeline.bulk.kappa_ch

    def test_ap_cy14_unconstructed_uses_conjecture(self):
        """AP-CY14: Results depending on unconstructed A_{K3xE} are conjectural."""
        for factory in [k3xe_free_field_pipeline, k3xe_bkm_pipeline]:
            pipeline = factory()
            assert pipeline.defect.claim_status == ClaimStatus.CONJECTURED

    def test_ap113_no_bare_kappa(self):
        """AP113: All kappa values are subscripted via KappaSpectrum."""
        pipeline = k3xe_bkm_pipeline()
        spec = pipeline.kappa_spectrum.values()
        # Every key must have a subscript
        for key in spec:
            assert key.startswith('kappa_'), f"Bare kappa found: {key}"

    def test_ap_cy11_conditionality_propagates(self):
        """AP-CY11: CY-A_3 dependency propagates to defect and morita."""
        pipeline = k3xe_free_field_pipeline()
        assert "CY-A_3" in pipeline.bulk.dependencies
        # Conditionality propagates:
        assert pipeline.defect.claim_status == ClaimStatus.CONJECTURED
        assert pipeline.morita.claim_status == ClaimStatus.CONJECTURED
