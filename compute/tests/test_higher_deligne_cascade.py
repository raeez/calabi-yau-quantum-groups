"""Tests for the higher Deligne cascade: E_1 -> E_2 -> E_3 via derived centers.

Verifies the mathematical content of the derived center promotion cascade:
  Step 1: E_1 -> E_2 (Deligne conjecture, BZFN agreement)
  Step 2: E_2 -> E_3 (higher Deligne, DIVERGENCE from iterated Drinfeld)
  Termination: E_3 -> E_4 blocked for CY inputs (E_1-stabilization)

Ground truth:
  p(n)    for n=0..9: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30   (OEIS A000041)
  tau_2(n) for n=0..9: 1, 2, 5, 10, 20, 36, 65, 110, 185, 300 (OEIS A000712)
  tau_3(n) for n=0..9: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479 (OEIS A000716)
  tau_4(n) for n=0..9: 1, 4, 14, 40, 105, 252, 574, 1240, 2580, 5180 (OEIS A023003)

Multi-path verification:
  Path 1: Direct multipartition convolution
  Path 2: Generating function coefficient extraction
  Path 3: Convolution consistency (tau_{k+1} = tau_k * p)
  Path 4: Cross-check with holomorphic_cs_chiral_engine.py
  Path 5: AP-CY4 compliance (Drinfeld center != derived center)
  Path 6: AP153 scope check (E_3 on cochains requires E_2+ input)
  Path 7: Dunn additivity decomposition verification
  Path 8: Cascade termination at E_3 for CY inputs

Manuscript references:
  chapters/theory/en_factorization.tex: sec:en-koszul-cascade
  chapters/theory/drinfeld_center.tex: thm:bzfn, rem:three-centers-sharp
  chapters/theory/e2_chiral_algebras.tex: rem:deligne-hochschild
"""

import pytest
from sympy import Rational

from compute.lib.higher_deligne_cascade import (
    CascadeTermination,
    CenterComparison,
    DerivedCenterResult,
    DunnDecomposition,
    DunnE1Factor,
    EnAlgebraData,
    PARTITION_GROUND_TRUTH,
    TAU_2_GROUND_TRUTH,
    TAU_3_GROUND_TRUTH,
    TAU_4_GROUND_TRUTH,
    cascade_summary,
    cascade_termination_analysis,
    compare_centers_step1,
    compare_centers_step2,
    compare_centers_step3,
    en_bar_differentials_vanish,
    en_bar_dimension,
    en_bar_hilbert_series,
    full_cascade,
    multipartition_count,
    partition_count,
    step1_e1_to_e2_heisenberg,
    step1_e1_to_e2_yangian,
    step2_e2_to_e3_heisenberg,
    step2_e2_to_e3_yangian,
    verify_dunn_e4_obstruction,
    yangian_dunn_factors,
)


# =========================================================================
# A. Partition function ground truth (Path 1: direct computation)
# =========================================================================

class TestPartitionGroundTruth:
    """Verify partition function computations against OEIS."""

    def test_partition_count_first_10(self):
        """p(n) for n=0..9 matches OEIS A000041."""
        computed = tuple(partition_count(n) for n in range(10))
        assert computed == PARTITION_GROUND_TRUTH

    def test_tau_2_first_10(self):
        """tau_2(n) for n=0..9 matches OEIS A000712."""
        computed = tuple(multipartition_count(n, 2) for n in range(10))
        assert computed == TAU_2_GROUND_TRUTH

    def test_tau_3_first_10(self):
        """tau_3(n) for n=0..9 matches OEIS A000716."""
        computed = tuple(multipartition_count(n, 3) for n in range(10))
        assert computed == TAU_3_GROUND_TRUTH

    def test_tau_4_first_10(self):
        """tau_4(n) for n=0..9 matches OEIS A023003."""
        computed = tuple(multipartition_count(n, 4) for n in range(10))
        assert computed == TAU_4_GROUND_TRUTH

    def test_tau_1_equals_p(self):
        """tau_1(n) = p(n) (1-component multipartition = partition)."""
        for n in range(15):
            assert multipartition_count(n, 1) == partition_count(n)


# =========================================================================
# B. Convolution consistency (Path 3: tau_{k+1} = tau_k * p)
# =========================================================================

class TestConvolutionConsistency:
    """tau_{k+1}(n) = sum_{a+b=n} tau_k(a) * p(b)."""

    def test_tau3_from_tau2_and_p(self):
        """tau_3(n) = convolution of tau_2 and p."""
        for n in range(10):
            conv = sum(
                multipartition_count(a, 2) * partition_count(n - a)
                for a in range(n + 1)
            )
            assert conv == multipartition_count(n, 3), f"Failed at n={n}"

    def test_tau4_from_tau3_and_p(self):
        """tau_4(n) = convolution of tau_3 and p."""
        for n in range(10):
            conv = sum(
                multipartition_count(a, 3) * partition_count(n - a)
                for a in range(n + 1)
            )
            assert conv == multipartition_count(n, 4), f"Failed at n={n}"

    def test_tau2_from_p_and_p(self):
        """tau_2(n) = sum_{a+b=n} p(a)*p(b) (definition)."""
        for n in range(10):
            conv = sum(
                partition_count(a) * partition_count(n - a)
                for a in range(n + 1)
            )
            assert conv == multipartition_count(n, 2), f"Failed at n={n}"


# =========================================================================
# C. E_n bar complex dimensions (Path 2: generating function)
# =========================================================================

class TestEnBarDimensions:
    """Verify B_{E_n}(H_k) dimensions match P(q)^n."""

    def test_e1_bar_is_p(self):
        """B_{E_1}(H_k) has dimension p(n) = P(q)."""
        for n in range(10):
            assert en_bar_dimension(1, n) == PARTITION_GROUND_TRUTH[n]

    def test_e2_bar_is_tau2(self):
        """B_{E_2}(H_k) has dimension tau_2(n) = P(q)^2."""
        for n in range(10):
            assert en_bar_dimension(2, n) == TAU_2_GROUND_TRUTH[n]

    def test_e3_bar_is_tau3(self):
        """B_{E_3}(H_k) has dimension tau_3(n) = P(q)^3."""
        for n in range(10):
            assert en_bar_dimension(3, n) == TAU_3_GROUND_TRUTH[n]

    def test_e4_bar_is_tau4(self):
        """B_{E_4}(H_k) (algebraic, no CY realization) has dim tau_4(n)."""
        for n in range(10):
            assert en_bar_dimension(4, n) == TAU_4_GROUND_TRUTH[n]

    def test_hilbert_series_length(self):
        """en_bar_hilbert_series returns correct number of terms."""
        for n in range(1, 5):
            series = en_bar_hilbert_series(n, max_degree=8)
            assert len(series) == 8

    def test_hilbert_series_leading_term(self):
        """All E_n bar complexes have dim 1 at degree 0."""
        for n in range(1, 6):
            assert en_bar_dimension(n, 0) == 1


# =========================================================================
# D. Step 1: E_1 -> E_2 (Deligne conjecture, BZFN agreement)
# =========================================================================

class TestStep1E1ToE2:
    """E_1 -> E_2 via derived center."""

    def test_heisenberg_step1_output_level(self):
        """Derived center of E_1 Heisenberg is E_2."""
        result = step1_e1_to_e2_heisenberg()
        assert result.output_n == 2

    def test_heisenberg_step1_bzfn_agrees(self):
        """BZFN theorem gives agreement at E_1 -> E_2."""
        result = step1_e1_to_e2_heisenberg()
        assert result.bzfn_agrees is True

    def test_heisenberg_step1_input_is_e1(self):
        """Input algebra is E_1."""
        result = step1_e1_to_e2_heisenberg()
        assert result.input_algebra.n == 1

    def test_heisenberg_step1_hh_dimension(self):
        """HH^*(H_k, H_k) dimension matches tau_2."""
        result = step1_e1_to_e2_heisenberg()
        assert result.hh_dimension_gf_coeffs == TAU_2_GROUND_TRUTH

    def test_yangian_step1_output_level(self):
        """Derived center of E_1 Y^+ is E_2."""
        result = step1_e1_to_e2_yangian()
        assert result.output_n == 2

    def test_yangian_step1_bzfn_agrees(self):
        """BZFN theorem gives agreement at E_1 -> E_2 for Yangian."""
        result = step1_e1_to_e2_yangian()
        assert result.bzfn_agrees is True

    def test_yangian_step1_output_name(self):
        """Y^+ -> Y(gl_hat_1) = W_{1+infty}."""
        result = step1_e1_to_e2_yangian()
        assert 'Y(gl_hat_1)' in result.output_name
        assert 'W_{1+infty}' in result.output_name

    def test_yangian_step1_class_L(self):
        """Y^+ is class L (not free-field)."""
        result = step1_e1_to_e2_yangian()
        assert result.input_algebra.shadow_class == 'L'

    def test_heisenberg_step1_class_G(self):
        """H_k is class G (free-field)."""
        result = step1_e1_to_e2_heisenberg()
        assert result.input_algebra.shadow_class == 'G'


# =========================================================================
# E. Step 2: E_2 -> E_3 (higher Deligne, DIVERGENCE)
# =========================================================================

class TestStep2E2ToE3:
    """E_2 -> E_3 via derived center (NOT iterated Drinfeld)."""

    def test_heisenberg_step2_output_level(self):
        """Derived center of E_2 Heisenberg is E_3."""
        result = step2_e2_to_e3_heisenberg()
        assert result.output_n == 3

    def test_heisenberg_step2_bzfn_does_not_agree(self):
        """BZFN does NOT apply at E_2 -> E_3 (it is E_1 -> E_2 only)."""
        result = step2_e2_to_e3_heisenberg()
        assert result.bzfn_agrees is False

    def test_heisenberg_step2_e3_type_bv(self):
        """E_infty input (H_k) gives BV-type E_3 (AP153 satisfied)."""
        result = step2_e2_to_e3_heisenberg()
        assert result.e3_type == 'bv'

    def test_heisenberg_step2_hh_dimension(self):
        """HH^*(H_k^{E_2}, H_k^{E_2}) dimension matches tau_3."""
        result = step2_e2_to_e3_heisenberg()
        assert result.hh_dimension_gf_coeffs == TAU_3_GROUND_TRUTH

    def test_yangian_step2_output_level(self):
        """Derived center of E_2 Yangian is E_3."""
        result = step2_e2_to_e3_yangian()
        assert result.output_n == 3

    def test_yangian_step2_bzfn_does_not_agree(self):
        """Iterated BZFN does NOT give E_3; it gives E_2-doubling."""
        result = step2_e2_to_e3_yangian()
        assert result.bzfn_agrees is False

    def test_yangian_step2_e3_type_generic(self):
        """E_2 input (Y, not E_infty) gives generic E_3, no BV (AP153)."""
        result = step2_e2_to_e3_yangian()
        assert result.e3_type == 'generic'

    def test_yangian_step2_output_toroidal(self):
        """E_3 output is the quantum toroidal algebra."""
        result = step2_e2_to_e3_yangian()
        assert 'U_{q,t}' in result.output_name

    def test_yangian_step2_hh_dimension(self):
        """Chain-level dimension of HH^*(Y, Y) matches tau_3."""
        result = step2_e2_to_e3_yangian()
        assert result.hh_dimension_gf_coeffs == TAU_3_GROUND_TRUTH


# =========================================================================
# F. AP-CY4: Drinfeld center != derived center (Path 5)
# =========================================================================

class TestAPCY4CenterDistinction:
    """AP-CY4 compliance: the three centers are distinct."""

    def test_step1_agreement(self):
        """At E_1 -> E_2: Drinfeld = derived (BZFN)."""
        comp = compare_centers_step1()
        assert comp.agrees is True
        assert comp.input_level == 1
        assert 'BZFN' in comp.explanation

    def test_step2_divergence(self):
        """At E_2 -> E_3: Drinfeld != derived.

        Iterated Drinfeld Z(B) = B boxtimes B^{rev} (E_2-doubling).
        Derived HH^*(B,B) = E_3 (higher Deligne).
        """
        comp = compare_centers_step2()
        assert comp.agrees is False
        assert 'boxtimes' in comp.drinfeld_output
        assert 'E_3' in comp.derived_output
        assert 'DIVERGENCE' in comp.explanation

    def test_step3_both_fail_cy(self):
        """At E_3 -> E_4: derived center works algebraically but no CY source."""
        comp = compare_centers_step3()
        assert comp.agrees is False
        assert 'TERMINATION' in comp.explanation
        assert 'no CY source' in comp.derived_output

    def test_drinfeld_never_gives_e3(self):
        """Iterated Drinfeld center NEVER produces E_3.

        Z(Z(C)) = C boxtimes C^{rev}, which is E_2 (doubled), not E_3.
        This is the mathematical content of rem:three-centers-sharp.
        """
        comp2 = compare_centers_step2()
        assert 'NOT E_3' in comp2.drinfeld_output

    def test_derived_does_give_e3(self):
        """Higher Deligne conjecture DOES produce E_3 from E_2 input."""
        comp2 = compare_centers_step2()
        assert 'E_3' in comp2.derived_output


# =========================================================================
# G. AP153: E_3 scope restriction (Path 6)
# =========================================================================

class TestAP153ScopeRestriction:
    """AP153: E_3 on Hochschild cochains depends on the input level."""

    def test_heisenberg_is_e_infty(self):
        """H_k is E_infty (commutative vertex algebra)."""
        result = step2_e2_to_e3_heisenberg()
        assert result.input_algebra.is_commutative is True

    def test_yangian_is_not_e_infty(self):
        """Y^+ is E_1, NOT E_infty."""
        result = step1_e1_to_e2_yangian()
        assert result.input_algebra.is_commutative is False

    def test_e_infty_gives_bv_e3(self):
        """E_infty input -> full algebraic E_3 with BV (cup + Gerst + BV)."""
        result = step2_e2_to_e3_heisenberg()
        assert result.e3_type == 'bv'

    def test_e2_gives_generic_e3(self):
        """E_2 input (not E_infty) -> generic higher-Deligne E_3, no BV."""
        result = step2_e2_to_e3_yangian()
        assert result.e3_type == 'generic'


# =========================================================================
# H. Dunn additivity decomposition (Path 7)
# =========================================================================

class TestDunnAdditivity:
    """Dunn additivity E_n = E_1^{tensor n}: explicit factors."""

    def test_e1_has_one_factor(self):
        """E_1 = E_1 (single factor)."""
        factors = DunnDecomposition.e1_factors(1)
        assert len(factors) == 1
        assert factors[0] == 'instanton'

    def test_e2_has_two_factors(self):
        """E_2 = E_1 tensor E_1 (two factors)."""
        factors = DunnDecomposition.e1_factors(2)
        assert len(factors) == 2
        assert 'instanton' in factors
        assert 'spectral' in factors

    def test_e3_has_three_factors(self):
        """E_3 = E_1 tensor E_1 tensor E_1 (three factors)."""
        factors = DunnDecomposition.e1_factors(3)
        assert len(factors) == 3
        assert 'instanton' in factors
        assert 'spectral' in factors
        assert 'miki' in factors

    def test_yangian_three_factors(self):
        """U_{q,t}(gl_hat_hat_1) has three E_1 factors."""
        factors = yangian_dunn_factors()
        assert len(factors) == 3
        # Each factor has a distinct geometric direction
        directions = [f.geometric_direction for f in factors]
        assert len(set(directions)) == 3

    def test_factor1_is_coha(self):
        """First E_1 factor is the CoHA multiplication."""
        factors = yangian_dunn_factors()
        assert factors[0].name == 'instanton'
        assert 'CoHA' in factors[0].algebraic_operation
        assert 'q = e^{h_1}' == factors[0].parameter

    def test_factor2_is_spectral(self):
        """Second E_1 factor is the spectral parameter shift."""
        factors = yangian_dunn_factors()
        assert factors[1].name == 'spectral'
        assert 'spectral parameter' in factors[1].algebraic_operation
        assert 'derived center' in factors[1].algebraic_operation

    def test_factor3_is_miki(self):
        """Third E_1 factor generates the Miki automorphism."""
        factors = yangian_dunn_factors()
        assert factors[2].name == 'miki'
        assert 'Miki' in factors[2].algebraic_operation
        assert 'derived center' in factors[2].algebraic_operation

    def test_miki_is_step2(self):
        """The Miki direction is added by Step 2 (E_2 -> E_3)."""
        factors = yangian_dunn_factors()
        assert 'Step 2' in factors[2].algebraic_operation

    def test_spectral_is_step1(self):
        """The spectral direction is added by Step 1 (E_1 -> E_2)."""
        factors = yangian_dunn_factors()
        assert 'Step 1' in factors[1].algebraic_operation


# =========================================================================
# I. Cascade termination (Path 8)
# =========================================================================

class TestCascadeTermination:
    """E_1-stabilization at d >= 4: cascade stops at E_3."""

    def test_cy3_terminates_at_e3(self):
        """CY_3 cascade terminates at E_3."""
        term = cascade_termination_analysis(3)
        assert term.max_n == 3

    def test_cy3_has_3_directions(self):
        """CY_3 has 3 complex directions."""
        term = cascade_termination_analysis(3)
        assert term.num_cy_directions == 3

    def test_e4_needs_4_factors(self):
        """E_4 = E_1^{tensor 4} would need 4 E_1 factors."""
        term = cascade_termination_analysis(3)
        assert term.num_e1_factors_needed == 4

    def test_cy4_also_terminates_at_e3(self):
        """CY_4 is E_1-stabilized; cascade still E_3 max."""
        term = cascade_termination_analysis(4)
        assert term.max_n == 3
        assert 'E_1-stabilized' in term.obstruction_type

    def test_cy4_bott_obstruction(self):
        """CY_4 has pi_4(BU) = Z (Pontryagin class) obstruction."""
        term = cascade_termination_analysis(4)
        assert 'pi_4(BU) = Z' in term.bott_group

    def test_cy2_terminates_at_e3(self):
        """CY_2 native E_2; one derived center step gives E_3 max."""
        term = cascade_termination_analysis(2)
        assert term.max_n == 3

    def test_cy1_is_e_infty(self):
        """CY_1 is E_infty (commutative); no termination needed."""
        term = cascade_termination_analysis(1)
        assert term.max_n == 999  # E_infty sentinel

    def test_cy5_e1_stabilized(self):
        """CY_5 is E_1-stabilized with Z_2 from Sp refinement."""
        term = cascade_termination_analysis(5)
        assert term.max_n == 3
        assert 'pi_5(BU) = 0' in term.bott_group

    def test_cy6_e1_stabilized(self):
        """CY_6 is E_1-stabilized with pi_6(BU) = Z."""
        term = cascade_termination_analysis(6)
        assert 'pi_6(BU) = Z' in term.bott_group

    def test_invalid_cy_dim(self):
        """CY dimension must be positive."""
        with pytest.raises(ValueError):
            cascade_termination_analysis(0)


# =========================================================================
# J. E_4 obstruction verification
# =========================================================================

class TestE4Obstruction:
    """Verify E_4 has no CY-geometric realization."""

    def test_e4_deficit(self):
        """CY_3 provides 3 directions; E_4 needs 4; deficit = 1."""
        obs = verify_dunn_e4_obstruction()
        assert obs['e4_requires'] == 4
        assert obs['cy3_provides'] == 3
        assert obs['deficit'] == 1

    def test_cy4_stabilized(self):
        """CY_4 has E_1-stabilization (not E_4)."""
        obs = verify_dunn_e4_obstruction()
        assert obs['cy4_stabilized'] is True

    def test_cy4_pontryagin_obstruction(self):
        """CY_4 obstruction is the first Pontryagin class p_1."""
        obs = verify_dunn_e4_obstruction()
        assert 'Pontryagin' in obs['cy4_obstruction']

    def test_cy3_free_params(self):
        """CY_3 has 2 free parameters (h_1, h_2; h_3 = -(h_1+h_2))."""
        obs = verify_dunn_e4_obstruction()
        assert obs['cy3_free_params'] == 2


# =========================================================================
# K. Full cascade integration tests
# =========================================================================

class TestFullCascade:
    """End-to-end cascade tests."""

    def test_heisenberg_cascade_length(self):
        """Heisenberg cascade has 2 steps (E_1->E_2, E_2->E_3)."""
        cascade = full_cascade('heisenberg')
        assert len(cascade) == 2

    def test_yangian_cascade_length(self):
        """Yangian cascade has 2 steps."""
        cascade = full_cascade('yangian')
        assert len(cascade) == 2

    def test_cascade_levels_monotone(self):
        """Output levels are monotonically increasing: 2, 3."""
        for algebra in ('heisenberg', 'yangian'):
            cascade = full_cascade(algebra)
            levels = [r.output_n for r in cascade]
            assert levels == [2, 3]

    def test_cascade_bzfn_pattern(self):
        """BZFN agrees at step 1, diverges at step 2."""
        for algebra in ('heisenberg', 'yangian'):
            cascade = full_cascade(algebra)
            assert cascade[0].bzfn_agrees is True
            assert cascade[1].bzfn_agrees is False

    def test_cascade_summary_keys(self):
        """Summary contains all expected keys."""
        summary = cascade_summary()
        assert 'center_comparisons' in summary
        assert 'heisenberg_cascade' in summary
        assert 'yangian_cascade' in summary
        assert 'termination' in summary
        assert 'dunn_factors' in summary
        assert 'e4_obstruction' in summary

    def test_cascade_three_comparisons(self):
        """Summary has 3 center comparisons (steps 1, 2, 3)."""
        summary = cascade_summary()
        assert len(summary['center_comparisons']) == 3

    def test_invalid_algebra_raises(self):
        """Unknown algebra name raises ValueError."""
        with pytest.raises(ValueError):
            full_cascade('unknown')


# =========================================================================
# L. Bar differential vanishing by shadow class
# =========================================================================

class TestBarDifferentials:
    """Verify bar differential vanishing depends on shadow class."""

    def test_class_G_vanishes(self):
        """Class G (free-field): all bar differentials vanish."""
        assert en_bar_differentials_vanish('G') is True

    def test_class_L_does_not_vanish(self):
        """Class L: differentials nonzero (spectral sequence needed)."""
        assert en_bar_differentials_vanish('L') is False

    def test_class_C_does_not_vanish(self):
        """Class C: differentials nonzero."""
        assert en_bar_differentials_vanish('C') is False

    def test_class_M_does_not_vanish(self):
        """Class M: all differentials active, infinite shadow tower."""
        assert en_bar_differentials_vanish('M') is False


# =========================================================================
# M. Cross-check with holomorphic_cs_chiral_engine (Path 4)
# =========================================================================

class TestCrossCheckWithHCSEngine:
    """Cross-check dimensions with the existing HCS engine."""

    def test_partition_consistency(self):
        """Our partition_count matches the HCS engine's _partition_count."""
        try:
            from compute.lib.holomorphic_cs_chiral_engine import _partition_count
            for n in range(15):
                assert partition_count(n) == _partition_count(n), \
                    f"Mismatch at n={n}: ours={partition_count(n)}, " \
                    f"HCS={_partition_count(n)}"
        except ImportError:
            pytest.skip("holomorphic_cs_chiral_engine not available")

    def test_tau3_vs_macmahon_distinction(self):
        """tau_3 (P(q)^3) != MacMahon M(q) (plane partitions).

        _macmahon_coefficient computes M(q) = prod 1/(1-q^m)^m (3D partitions,
        OEIS A000219), NOT P(q)^3 = tau_3 (3-component multipartitions,
        OEIS A000716).  They agree at n=0 (both 1) but diverge at n=1:
        tau_3(1) = 3, M(1) = 1.  This test verifies the distinction.
        """
        try:
            from compute.lib.holomorphic_cs_chiral_engine import _macmahon_coefficient
            # M(q) and P(q)^3 agree at n=0
            assert multipartition_count(0, 3) == _macmahon_coefficient(0) == 1
            # They DIVERGE at n=1: tau_3(1) = 3, M(1) = 1
            assert multipartition_count(1, 3) == 3
            assert _macmahon_coefficient(1) == 1
            assert multipartition_count(1, 3) != _macmahon_coefficient(1)
        except (ImportError, AttributeError):
            pytest.skip("holomorphic_cs_chiral_engine._macmahon_coefficient not available")


# =========================================================================
# N. Deformation parameter counting
# =========================================================================

class TestDeformationParameters:
    """Verify deformation parameter counts match the E_n level."""

    def test_e1_one_param(self):
        """E_1 algebra has 1 effective deformation parameter (k)."""
        assert DunnDecomposition.num_effective_params(1) == 1

    def test_e2_one_effective(self):
        """E_2 algebra has 1 effective param (sigma_3 only)."""
        assert DunnDecomposition.num_effective_params(2) == 1

    def test_e3_one_effective(self):
        """E_3 algebra on C^3 has 1 effective param (sigma_3)."""
        assert DunnDecomposition.num_effective_params(3) == 1

    def test_e4_two_effective(self):
        """E_4 algebra on C^4 (algebraic, no CY) has 2 effective params."""
        assert DunnDecomposition.num_effective_params(4) == 2

    def test_e3_params_are_omega(self):
        """E_3 deformation params are the Omega-background (h_1, h_2, h_3)."""
        params = DunnDecomposition.deformation_params(3)
        assert 'h_1' in params
        assert 'h_2' in params
        assert 'h_3' in params
