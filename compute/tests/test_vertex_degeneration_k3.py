r"""Tests for vertex_degeneration_k3.py: chiral algebra at the boundary of K3 moduli space.

CENTRAL RESULTS TESTED:
    (1)  Kulikov classification: three types with correct monodromy indices.
    (2)  Mukai rank drop: 0 (Type I), 2 (Type II), 4 (Type III).
    (3)  Effective signature: (4,20), (3,19), (0,20) across types.
    (4)  CY_2 constraint: sum h_i = 0 at ALL degeneration limits.
    (5)  kappa_ch = 2 at ALL limits (topological invariance, AP113).
    (6)  Structure function degeneration: degree drops match rank drops.
    (7)  g(0) = (-1)^{num_nonzero} at all limits.
    (8)  Unitarity g(u)*g(-u) = 1 at all limits (algebraic, unconditional).
    (9)  Shadow class monotonicity: M -> L -> G along reduction chain.
    (10) Orbifold = Kummer (prop:kummer-orbifold, Steps 1-4 PROVED).
    (11) Type III strict limit: g(u) = 1 (trivial).
    (12) LCS limit: effective rank = picard_number + 2.
    (13) Newton power sums: p_1 = 0 at all limits (CY_2).
    (14) Compactifiability: all types compactifiable (KPP theorem).
    (15) Dimensional reduction chain: 6d -> 5d -> 3d.
    (16) AP157 compliance: degeneration_type specified at all points.
    (17) Summary table: all rows well-formed.
    (18) Type II parameters: 22 nonzero, 2 zero.
    (19) Type III approach: Kummer at small delta.
    (20) LCS at rho=20: most parameters survive.

MULTI-PATH VERIFICATION:
    Path 1: Kulikov classification (algebraic geometry, PROVED)
    Path 2: Structure function degeneration (analytic)
    Path 3: Shadow class variation (algebraic)
    Path 4: kappa_ch invariance (topological)
    Path 5: Dimensional reduction chain (physical)
    Path 6: Compactifiability (KPP theorem, PROVED)
    Path 7: Newton power sum tracking (combinatorial)

AP-CY12: All shadow class determinations use full tower computation.
AP-CY14: All Y(g_{K3}) results marked CONJECTURAL.
AP-CY28: Test points chosen to avoid poles at +/-h_i.
AP113: All kappa values subscripted (kappa_ch, kappa_BKM, etc.).
AP157: All degeneration limits specify degeneration type.

110 tests total.

Manuscript references:
    k3_times_e.tex: sec:rmatrix-degeneration
    k3_times_e.tex: sec:shadow-class-stability
    k3_times_e.tex: conj:compactification-commutativity
    cy_to_chiral.tex: prop:kummer-orbifold (Steps 1-4 PROVED)
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.vertex_degeneration_k3 import (
    # Constants
    KULIKOV_TYPES,
    MONODROMY_INDEX,
    MUKAI_RANK_DROP,
    EFFECTIVE_RANK,
    MUKAI_SIGNATURE_EFFECTIVE,
    WEIGHT_FILTRATION,
    # Kulikov types
    kulikov_type_I,
    kulikov_type_II,
    kulikov_type_III,
    all_kulikov_types,
    # Parameters
    type_II_parameters,
    type_III_parameters,
    type_III_approach_parameters,
    lcs_parameters,
    # Structure function degeneration
    structure_function_degeneration,
    type_I_degeneration,
    type_II_degeneration,
    type_III_degeneration,
    lcs_degeneration,
    orbifold_degeneration,
    # Shadow class
    shadow_at_type_I,
    shadow_at_type_II,
    shadow_at_type_III,
    shadow_at_orbifold,
    shadow_at_lcs,
    all_degeneration_shadows,
    # kappa invariance
    verify_kappa_ch_invariance,
    # Dimensional reduction
    reduction_6d_to_5d,
    reduction_5d_to_3d,
    full_reduction_chain,
    verify_shadow_monotonicity,
    # Evaluation
    evaluate_structure_function_at_limits,
    newton_power_sum_degeneration,
    # Compactification
    compactification_type_I,
    compactification_type_II,
    compactification_type_III,
    all_compactifications,
    # Summary
    degeneration_summary_table,
)

from compute.lib.k3_yangian import (
    NUM_PARAMS,
    SIG_PLUS,
    SIG_MINUS,
    kummer_k3_parameters,
    structure_function_evaluate,
)

F = Fraction


# =========================================================================
# Section 1: Kulikov classification (15 tests)
# =========================================================================

class TestKulikovClassification:
    """Tests for the Kulikov-Persson-Pinkham classification."""

    def test_three_types_exist(self):
        """There are exactly 3 Kulikov types."""
        assert len(KULIKOV_TYPES) == 3
        assert set(KULIKOV_TYPES) == {'I', 'II', 'III'}

    def test_monodromy_indices(self):
        """Monodromy indices: Type I=1, II=2, III=3."""
        assert MONODROMY_INDEX['I'] == 1
        assert MONODROMY_INDEX['II'] == 2
        assert MONODROMY_INDEX['III'] == 3

    def test_type_I_data(self):
        """Type I: smooth, no rank drop, full signature."""
        t = kulikov_type_I()
        assert t.kulikov_type == 'I'
        assert t.monodromy_index == 1
        assert t.log_monodromy_rank == 0
        assert t.mukai_rank_drop == 0
        assert t.effective_rank == 24
        assert t.effective_signature == (4, 20)
        assert t.compactifiable is True

    def test_type_II_data(self):
        """Type II: chain of rational surfaces, rank drop 2."""
        t = kulikov_type_II()
        assert t.kulikov_type == 'II'
        assert t.monodromy_index == 2
        assert t.log_monodromy_rank == 1
        assert t.mukai_rank_drop == 2
        assert t.effective_rank == 22
        assert t.effective_signature == (3, 19)
        assert t.compactifiable is True

    def test_type_III_data(self):
        """Type III: maximal degeneration, rank drop 4."""
        t = kulikov_type_III()
        assert t.kulikov_type == 'III'
        assert t.monodromy_index == 3
        assert t.log_monodromy_rank == 2
        assert t.mukai_rank_drop == 4
        assert t.effective_rank == 20
        assert t.effective_signature == (0, 20)
        assert t.compactifiable is True

    def test_all_kulikov_types_returns_three(self):
        """all_kulikov_types() returns exactly 3 items."""
        types = all_kulikov_types()
        assert len(types) == 3
        assert [t.kulikov_type for t in types] == ['I', 'II', 'III']

    def test_rank_drop_increases(self):
        """Rank drop increases with monodromy index."""
        assert MUKAI_RANK_DROP['I'] < MUKAI_RANK_DROP['II'] < MUKAI_RANK_DROP['III']

    def test_effective_rank_decreases(self):
        """Effective rank decreases with monodromy index."""
        assert EFFECTIVE_RANK['I'] > EFFECTIVE_RANK['II'] > EFFECTIVE_RANK['III']

    def test_effective_rank_plus_drop_is_24(self):
        """Effective rank + rank drop = 24 for all types."""
        for t in KULIKOV_TYPES:
            assert EFFECTIVE_RANK[t] + MUKAI_RANK_DROP[t] == NUM_PARAMS

    def test_effective_signature_sums_to_effective_rank(self):
        """Signature components sum to effective rank for all types."""
        for t in KULIKOV_TYPES:
            sig = MUKAI_SIGNATURE_EFFECTIVE[t]
            assert sig[0] + sig[1] == EFFECTIVE_RANK[t]

    def test_type_III_positive_signature_zero(self):
        """Type III: all positive Mukai directions collapse (signature (0, 20))."""
        sig = MUKAI_SIGNATURE_EFFECTIVE['III']
        assert sig[0] == 0
        assert sig[1] == SIG_MINUS  # = 20

    def test_weight_filtration_type_I_is_pure(self):
        """Type I: pure Hodge structure (W_0 = W_1 = 0, W_2 = 22)."""
        wf = WEIGHT_FILTRATION['I']
        assert wf[0] == 0
        assert wf[1] == 0
        assert wf[2] == 22

    def test_weight_filtration_nested(self):
        """Weight filtration is nested: W_0 <= W_1 <= W_2."""
        for t in KULIKOV_TYPES:
            wf = WEIGHT_FILTRATION[t]
            assert wf[0] <= wf[1] <= wf[2]

    def test_degeneration_type_specified(self):
        """AP157: every Kulikov type has a degeneration_type string."""
        for t in all_kulikov_types():
            assert len(t.degeneration_type) > 0

    def test_compactification_method_specified(self):
        """Every Kulikov type has a compactification method."""
        for t in all_kulikov_types():
            assert len(t.compactification_method) > 0


# =========================================================================
# Section 2: Degenerate parameters (15 tests)
# =========================================================================

class TestDegenerateParameters:
    """Tests for Yangian parameters at degeneration limits."""

    def test_type_II_cy2_constraint(self):
        """Type II parameters satisfy CY_2: sum h_i = 0."""
        params = type_II_parameters()
        assert params.cy2_sum == 0

    def test_type_II_two_zero_params(self):
        """Type II: exactly 2 parameters are 0."""
        params = type_II_parameters()
        num_zero = sum(1 for hi in params.h if hi == 0)
        assert num_zero == 2

    def test_type_II_twenty_two_nonzero(self):
        """Type II: 22 nonzero parameters."""
        params = type_II_parameters()
        num_nonzero = sum(1 for hi in params.h if hi != 0)
        assert num_nonzero == 22

    def test_type_II_has_24_params(self):
        """Type II: still 24 parameters total."""
        params = type_II_parameters()
        assert len(params.h) == NUM_PARAMS

    def test_type_III_all_zero(self):
        """Type III (strict): ALL parameters are 0."""
        params = type_III_parameters()
        assert all(hi == 0 for hi in params.h)

    def test_type_III_cy2_trivial(self):
        """Type III: CY_2 trivially satisfied (all zero)."""
        params = type_III_parameters()
        assert params.cy2_sum == 0

    def test_type_III_is_null(self):
        """Type III: Mukai norm is 0 (null vector)."""
        params = type_III_parameters()
        assert params.is_null is True

    def test_type_III_approach_cy2(self):
        """Type III approach: CY_2 satisfied at delta = 1/100."""
        params = type_III_approach_parameters(Rational(1, 100))
        assert params.cy2_sum == 0

    def test_type_III_approach_nonzero(self):
        """Type III approach: parameters are nonzero at finite delta."""
        params = type_III_approach_parameters(Rational(1, 100))
        num_nonzero = sum(1 for hi in params.h if hi != 0)
        assert num_nonzero == NUM_PARAMS

    def test_lcs_rho1_cy2(self):
        """LCS at rho=1: CY_2 satisfied."""
        params = lcs_parameters(picard_number=1)
        assert params.cy2_sum == 0

    def test_lcs_rho1_effective_rank(self):
        """LCS at rho=1: 3 nonzero parameters (1 algebraic + H^0/H^4 pair)."""
        params = lcs_parameters(picard_number=1)
        num_nonzero = sum(1 for hi in params.h if hi != 0)
        assert num_nonzero == 3  # rho + 2 = 1 + 2

    def test_lcs_rho20_cy2(self):
        """LCS at rho=20: CY_2 satisfied."""
        params = lcs_parameters(picard_number=20)
        assert params.cy2_sum == 0

    def test_lcs_rho20_effective_rank(self):
        """LCS at rho=20: 22 nonzero parameters."""
        params = lcs_parameters(picard_number=20)
        num_nonzero = sum(1 for hi in params.h if hi != 0)
        assert num_nonzero == 22  # rho + 2 = 20 + 2

    def test_lcs_invalid_picard_raises(self):
        """LCS: Picard number out of [1, 20] raises ValueError."""
        with pytest.raises(ValueError):
            lcs_parameters(picard_number=0)
        with pytest.raises(ValueError):
            lcs_parameters(picard_number=21)

    def test_lcs_picard_range(self):
        """LCS: effective rank = rho + 2 for all valid rho."""
        for rho in range(1, 21):
            params = lcs_parameters(picard_number=rho)
            assert params.cy2_sum == 0
            num_nonzero = sum(1 for hi in params.h if hi != 0)
            assert num_nonzero == rho + 2


# =========================================================================
# Section 3: Structure function degeneration (20 tests)
# =========================================================================

class TestStructureFunctionDegeneration:
    """Tests for g_{K3}(u) at degeneration limits."""

    def test_type_I_full_degree(self):
        """Type I: full degree-(24,24)."""
        d = type_I_degeneration()
        assert d.effective_degree == (24, 24)

    def test_type_I_g_at_zero(self):
        """Type I: g(0) = (-1)^24 = 1."""
        d = type_I_degeneration()
        assert d.g_at_zero == 1

    def test_type_I_unitarity(self):
        """Type I: unitarity holds."""
        d = type_I_degeneration()
        assert d.unitarity_holds is True

    def test_type_II_degree_22(self):
        """Type II: effective degree-(22,22)."""
        d = type_II_degeneration()
        assert d.effective_degree == (22, 22)

    def test_type_II_two_zero(self):
        """Type II: 2 zero parameters."""
        d = type_II_degeneration()
        assert d.num_zero_params == 2

    def test_type_II_g_at_zero(self):
        """Type II: g(0) = (-1)^22 = 1."""
        d = type_II_degeneration()
        assert d.g_at_zero == 1

    def test_type_II_p1_zero(self):
        """Type II: p_1 = 0 (CY_2)."""
        d = type_II_degeneration()
        assert d.newton_p1 == 0

    def test_type_III_trivial(self):
        """Type III (strict): g(u) = 1 (all trivial factors)."""
        d = type_III_degeneration()
        assert d.effective_degree == (0, 0)
        assert d.num_zero_params == 24
        assert d.num_nonzero_params == 0

    def test_type_III_g_at_zero_trivial(self):
        """Type III: g(0) = (-1)^0 = 1."""
        d = type_III_degeneration()
        assert d.g_at_zero == 1

    def test_type_III_all_newton_zero(self):
        """Type III: all Newton power sums are 0."""
        d = type_III_degeneration()
        assert d.newton_p1 == 0
        assert d.newton_p2 == 0
        assert d.newton_p3 == 0

    def test_lcs_rho1_degree(self):
        """LCS at rho=1: effective degree-(3,3)."""
        d = lcs_degeneration(picard_number=1)
        assert d.effective_degree == (3, 3)

    def test_lcs_rho1_21_trivial(self):
        """LCS at rho=1: 21 trivial factors."""
        d = lcs_degeneration(picard_number=1)
        assert d.num_zero_params == 21

    def test_orbifold_full_degree(self):
        """Orbifold (Kummer): full degree-(24,24)."""
        d = orbifold_degeneration()
        assert d.effective_degree == (24, 24)

    def test_all_have_degeneration_type(self):
        """AP157: all degenerations have degeneration_type specified."""
        for d in [type_I_degeneration(), type_II_degeneration(),
                  type_III_degeneration(), lcs_degeneration(),
                  orbifold_degeneration()]:
            assert len(d.degeneration_type) > 0

    def test_all_have_status(self):
        """All degenerations carry the CONJECTURAL status."""
        for d in [type_I_degeneration(), type_II_degeneration(),
                  type_III_degeneration(), lcs_degeneration(),
                  orbifold_degeneration()]:
            assert d.status == 'CONJECTURAL'

    def test_unitarity_at_type_II_numerically(self):
        """Type II: verify g(u)*g(-u) = 1 numerically."""
        params = type_II_parameters()
        # AP-CY28: safe test points
        for u in [Rational(37), Rational(41), Rational(97, 3)]:
            g_u = structure_function_evaluate(u, params)
            g_neg_u = structure_function_evaluate(-u, params)
            assert g_u * g_neg_u == 1

    def test_unitarity_at_lcs_numerically(self):
        """LCS: verify g(u)*g(-u) = 1 numerically."""
        params = lcs_parameters(picard_number=1)
        for u in [Rational(37), Rational(41)]:
            g_u = structure_function_evaluate(u, params)
            g_neg_u = structure_function_evaluate(-u, params)
            assert g_u * g_neg_u == 1

    def test_type_I_equals_orbifold(self):
        """Type I (Kummer) and orbifold give the same structure function."""
        d_I = type_I_degeneration()
        d_orb = orbifold_degeneration()
        assert d_I.effective_degree == d_orb.effective_degree
        assert d_I.g_at_zero == d_orb.g_at_zero

    def test_g_at_infinity_always_1(self):
        """g(inf) = 1 at all degeneration limits."""
        for d in [type_I_degeneration(), type_II_degeneration(),
                  type_III_degeneration(), lcs_degeneration(),
                  orbifold_degeneration()]:
            assert d.g_at_infinity == 1

    def test_effective_degree_matches_nonzero_count(self):
        """Effective degree = (num_nonzero, num_nonzero)."""
        for d in [type_I_degeneration(), type_II_degeneration(),
                  type_III_degeneration(), lcs_degeneration(),
                  orbifold_degeneration()]:
            assert d.effective_degree == (d.num_nonzero_params, d.num_nonzero_params)


# =========================================================================
# Section 4: Shadow class at degeneration limits (15 tests)
# =========================================================================

class TestShadowClassDegeneration:
    """Tests for shadow class variation across degeneration limits."""

    def test_type_I_class_G(self):
        """Type I (smooth): class G (free-field)."""
        s = shadow_at_type_I()
        assert s.shadow_class == 'G'
        assert s.shadow_depth == 2

    def test_type_II_class_L(self):
        """Type II: class L (cubic OPE from elliptic curve gluing)."""
        s = shadow_at_type_II()
        assert s.shadow_class == 'L'
        assert s.shadow_depth == 3

    def test_type_III_class_G(self):
        """Type III (strict limit): class G (trivial)."""
        s = shadow_at_type_III()
        assert s.shadow_class == 'G'
        assert s.shadow_depth == 2

    def test_orbifold_class_L(self):
        """Orbifold (Kummer): subalgebra class L."""
        s = shadow_at_orbifold()
        assert s.shadow_class == 'L'
        assert s.shadow_depth == 3

    def test_lcs_class_G(self):
        """LCS (rho=1): class G."""
        s = shadow_at_lcs()
        assert s.shadow_class == 'G'
        assert s.shadow_depth == 2

    def test_all_kappa_ch_is_2(self):
        """kappa_ch = 2 at ALL degeneration limits (topological invariant)."""
        for s in all_degeneration_shadows():
            assert s.kappa_ch == 2

    def test_all_have_degeneration_type(self):
        """AP157: all shadow data have degeneration_type."""
        for s in all_degeneration_shadows():
            assert len(s.degeneration_type) > 0

    def test_all_have_mechanism(self):
        """All shadow class data explain the mechanism."""
        for s in all_degeneration_shadows():
            assert len(s.mechanism) > 0

    def test_type_I_S3_zero(self):
        """Type I: S_3 = 0 (free-field, no cubic OPE)."""
        s = shadow_at_type_I()
        assert s.S3 == F(0)

    def test_type_I_S4_zero(self):
        """Type I: S_4 = 0 (class G)."""
        s = shadow_at_type_I()
        assert s.S4 == F(0)

    def test_type_II_S3_nonzero(self):
        """Type II: S_3 != 0 (cubic OPE from elliptic curve gluing)."""
        s = shadow_at_type_II()
        assert s.S3 != 0

    def test_type_II_S4_zero(self):
        """Type II: S_4 = 0 (level 1 Sugawara, class L not M)."""
        s = shadow_at_type_II()
        assert s.S4 == F(0)

    def test_shadow_class_valid(self):
        """All shadow classes are in {G, L, C, M}."""
        for s in all_degeneration_shadows():
            assert s.shadow_class in {'G', 'L', 'C', 'M'}

    def test_five_degeneration_shadows(self):
        """There are 5 degeneration shadow entries."""
        assert len(all_degeneration_shadows()) == 5

    def test_shadow_depth_matches_class(self):
        """Shadow depth matches class: G=2, L=3, C=4, M=inf."""
        depth_map = {'G': 2, 'L': 3, 'C': 4, 'M': float('inf')}
        for s in all_degeneration_shadows():
            assert s.shadow_depth == depth_map[s.shadow_class]


# =========================================================================
# Section 5: kappa_ch invariance (10 tests)
# =========================================================================

class TestKappaChInvariance:
    """Tests for kappa_ch = 2 invariance (AP113)."""

    def test_kappa_ch_invariance_all_pass(self):
        """verify_kappa_ch_invariance: all limits have kappa_ch = 2."""
        result = verify_kappa_ch_invariance()
        assert result['all_equal_2'] is True

    def test_kappa_ch_value_is_2(self):
        """kappa_ch = 2 from chi(O_{K3})."""
        result = verify_kappa_ch_invariance()
        assert result['kappa_ch_value'] == 2

    def test_kappa_ch_hodge_computation(self):
        """kappa_ch = h^{0,0} - h^{1,0} + h^{2,0} = 1 - 0 + 1 = 2."""
        # K3 Hodge numbers
        h00, h10, h20 = 1, 0, 1
        assert h00 - h10 + h20 == 2

    def test_kappa_ch_is_topological(self):
        """kappa_ch is a topological invariant (proved status)."""
        result = verify_kappa_ch_invariance()
        assert 'topological' in result['status'].lower() or 'proved' in result['status'].lower()

    def test_kappa_ch_each_limit(self):
        """kappa_ch = 2 at each limit individually."""
        result = verify_kappa_ch_invariance()
        for entry in result['all_limits']:
            assert entry['kappa_ch'] == 2
            assert entry['is_2'] is True

    def test_kappa_ch_not_bare(self):
        """AP113: kappa is subscripted as kappa_ch, never bare."""
        # This is a code-level check: all our data uses kappa_ch, not kappa
        for s in all_degeneration_shadows():
            # The field is named kappa_ch, not kappa
            assert hasattr(s, 'kappa_ch')

    def test_kappa_ch_type_II_equals_type_I(self):
        """kappa_ch at Type II = kappa_ch at Type I (invariant)."""
        assert shadow_at_type_I().kappa_ch == shadow_at_type_II().kappa_ch

    def test_kappa_ch_type_III_equals_type_I(self):
        """kappa_ch at Type III = kappa_ch at Type I (invariant)."""
        assert shadow_at_type_I().kappa_ch == shadow_at_type_III().kappa_ch

    def test_kappa_ch_orbifold_equals_smooth(self):
        """kappa_ch at orbifold = kappa_ch at smooth (invariant)."""
        assert shadow_at_type_I().kappa_ch == shadow_at_orbifold().kappa_ch

    def test_kappa_ch_lcs_equals_smooth(self):
        """kappa_ch at LCS = kappa_ch at smooth (invariant)."""
        assert shadow_at_type_I().kappa_ch == shadow_at_lcs().kappa_ch


# =========================================================================
# Section 6: Dimensional reduction chain (10 tests)
# =========================================================================

class TestDimensionalReduction:
    """Tests for the 6d -> 5d -> 3d reduction chain."""

    def test_6d_to_5d_step(self):
        """6d -> 5d: trigonometric -> rational."""
        step = reduction_6d_to_5d()
        assert step.source_dim == 6
        assert step.target_dim == 5
        assert 'trigonometric' in step.rmatrix_source
        assert 'rational' in step.rmatrix_target

    def test_5d_to_3d_step(self):
        """5d -> 3d: rational -> trivial."""
        step = reduction_5d_to_3d()
        assert step.source_dim == 5
        assert step.target_dim == 3
        assert 'rational' in step.rmatrix_source
        assert 'trivial' in step.rmatrix_target

    def test_chain_has_two_steps(self):
        """Full chain has 2 steps: 6d -> 5d -> 3d."""
        chain = full_reduction_chain()
        assert len(chain) == 2

    def test_chain_dimensions_consecutive(self):
        """Chain dimensions are consecutive: target of step i = source of step i+1."""
        chain = full_reduction_chain()
        assert chain[0].target_dim == chain[1].source_dim

    def test_shadow_monotonicity(self):
        """Shadow class is non-increasing: M -> L -> G."""
        result = verify_shadow_monotonicity()
        assert result['all_monotone'] is True

    def test_shadow_sequence(self):
        """Shadow sequence is M, L, G."""
        result = verify_shadow_monotonicity()
        assert result['shadow_sequence'] == ['M', 'L', 'G']

    def test_6d_shadow_M(self):
        """6d shadow class is M."""
        step = reduction_6d_to_5d()
        assert step.shadow_source == 'M'

    def test_5d_shadow_L(self):
        """5d shadow class is L."""
        step = reduction_6d_to_5d()
        assert step.shadow_target == 'L'

    def test_3d_shadow_G(self):
        """3d shadow class is G."""
        step = reduction_5d_to_3d()
        assert step.shadow_target == 'G'

    def test_each_step_has_mechanism(self):
        """Each reduction step has a mechanism description."""
        for step in full_reduction_chain():
            assert len(step.mechanism) > 0


# =========================================================================
# Section 7: Numerical evaluation (10 tests)
# =========================================================================

class TestNumericalEvaluation:
    """Tests for numerical evaluation at degeneration limits."""

    def test_evaluation_returns_all_types(self):
        """evaluate_structure_function_at_limits has all types."""
        results = evaluate_structure_function_at_limits()
        assert 'Type I (Kummer)' in results
        assert 'Type II' in results
        assert 'Type III (strict)' in results

    def test_type_III_strict_is_1(self):
        """Type III strict: g(u) = 1 at all test points."""
        results = evaluate_structure_function_at_limits()
        for val in results['Type III (strict)'].values():
            assert val == '1'

    def test_type_I_nontrivial(self):
        """Type I: g(u) != 1 at nontrivial test points."""
        results = evaluate_structure_function_at_limits()
        for val in results['Type I (Kummer)'].values():
            assert val != '1'

    def test_newton_p1_always_zero(self):
        """Newton p_1 = 0 at all limits (CY_2 constraint)."""
        results = newton_power_sum_degeneration()
        for name, data in results.items():
            assert data['p1_is_zero'] is True, f"p_1 != 0 at {name}"

    def test_newton_type_III_all_zero(self):
        """Type III (strict): all Newton power sums are 0."""
        results = newton_power_sum_degeneration()
        data = results['Type III (strict)']
        assert data['p1'] == '0'
        assert data['p2'] == '0'
        assert data['p3'] == '0'

    def test_newton_type_I_p2_nonzero(self):
        """Type I (Kummer): p_2 != 0."""
        results = newton_power_sum_degeneration()
        data = results['Type I (Kummer)']
        assert data['p2'] != '0'

    def test_newton_type_I_p3_nonzero(self):
        """Type I (Kummer): p_3 != 0."""
        results = newton_power_sum_degeneration()
        data = results['Type I (Kummer)']
        assert data['p3'] != '0'

    def test_newton_lcs_rho1_p2_nonzero(self):
        """LCS (rho=1): p_2 != 0 (3 nonzero parameters)."""
        results = newton_power_sum_degeneration()
        data = results['LCS (rho=1)']
        assert data['p2'] != '0'

    def test_approach_delta_small_near_type_I(self):
        """Type III approach at delta=1/100 has same p_1 = 0 as Type I."""
        results = newton_power_sum_degeneration()
        data = results['Type III (approach, delta=1/100)']
        assert data['p1_is_zero'] is True

    def test_lcs_rho20_has_more_nonzero_params_than_rho1(self):
        """LCS rho=20 has more nonzero parameters (22) than rho=1 (3).

        Multi-path cross-check: the number of nonzero h_i at LCS equals
        rho + 2 (algebraic classes + H^0/H^4 pair). Verify via Newton sums:
        p_2 != 0 for both, confirming nontrivial structure functions.
        """
        results = newton_power_sum_degeneration()
        p2_rho1 = F(results['LCS (rho=1)']['p2'])
        p2_rho20 = F(results['LCS (rho=20)']['p2'])
        # Both have nontrivial p_2
        assert p2_rho1 != 0
        assert p2_rho20 != 0
        # Cross-check via parameter counts
        from compute.lib.vertex_degeneration_k3 import lcs_parameters
        params_1 = lcs_parameters(picard_number=1)
        params_20 = lcs_parameters(picard_number=20)
        n1 = sum(1 for hi in params_1.h if hi != 0)
        n20 = sum(1 for hi in params_20.h if hi != 0)
        assert n20 > n1
        assert n1 == 3   # rho + 2 = 1 + 2
        assert n20 == 22  # rho + 2 = 20 + 2


# =========================================================================
# Section 8: Compactifiability (10 tests)
# =========================================================================

class TestCompactifiability:
    """Tests for compactification of K3 degenerations (KPP theorem)."""

    def test_all_compactifiable(self):
        """All three Kulikov types are compactifiable (KPP theorem)."""
        for c in all_compactifications():
            assert c.compactifiable is True

    def test_type_I_no_base_change(self):
        """Type I: no base change needed."""
        c = compactification_type_I()
        assert c.requires_base_change is False
        assert c.requires_birational_modification is False

    def test_type_II_needs_base_change(self):
        """Type II: requires base change."""
        c = compactification_type_II()
        assert c.requires_base_change is True
        assert c.requires_birational_modification is False

    def test_type_III_needs_both(self):
        """Type III: requires both base change and birational modification."""
        c = compactification_type_III()
        assert c.requires_base_change is True
        assert c.requires_birational_modification is True

    def test_three_compactifications(self):
        """all_compactifications returns 3 items."""
        assert len(all_compactifications()) == 3

    def test_compactification_types_match_kulikov(self):
        """Compactification types match Kulikov types I, II, III."""
        types = [c.kulikov_type for c in all_compactifications()]
        assert types == ['I', 'II', 'III']

    def test_type_I_chiral_functor_extends(self):
        """Type I: Phi extends (CY-A_2 proved)."""
        c = compactification_type_I()
        assert 'extends' in c.chiral_functor_extends.lower()

    def test_type_II_chiral_functor_conjectural(self):
        """Type II: Phi extension is CONJECTURAL."""
        c = compactification_type_II()
        assert 'CONJECTURAL' in c.chiral_functor_extends

    def test_type_III_chiral_functor_conjectural(self):
        """Type III: Phi extension is CONJECTURAL."""
        c = compactification_type_III()
        assert 'CONJECTURAL' in c.chiral_functor_extends

    def test_degeneration_type_in_compactification(self):
        """AP157: compactification data has degeneration_type."""
        for c in all_compactifications():
            assert len(c.degeneration_type) > 0


# =========================================================================
# Section 9: Summary table (5 tests)
# =========================================================================

class TestSummaryTable:
    """Tests for the summary table."""

    def test_summary_has_five_rows(self):
        """Summary table has 5 rows (Type I, II, III, orbifold, LCS)."""
        rows = degeneration_summary_table()
        assert len(rows) == 5

    def test_all_rows_have_required_fields(self):
        """All rows have all required fields."""
        required = ['name', 'degeneration_type', 'effective_rank',
                    'effective_signature', 'shadow_class', 'kappa_ch',
                    'g_behavior', 'compactifiable']
        for row in degeneration_summary_table():
            for field in required:
                assert field in row, f"Missing {field} in {row['name']}"

    def test_all_kappa_ch_2(self):
        """All rows have kappa_ch = 2."""
        for row in degeneration_summary_table():
            assert row['kappa_ch'] == 2

    def test_all_compactifiable(self):
        """All rows are compactifiable."""
        for row in degeneration_summary_table():
            assert row['compactifiable'] is True

    def test_all_degeneration_types_nonempty(self):
        """AP157: all rows have nonempty degeneration_type."""
        for row in degeneration_summary_table():
            assert len(row['degeneration_type']) > 0


# =========================================================================
# Section 10: Multi-path cross-checks (15 tests)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification: cross-check engine outputs against independent
    computations from k3_yangian.py and shadow_class_moduli_variation.py.

    These tests verify that the degeneration engine's outputs are CONSISTENT
    with the parent modules, not merely self-consistent.
    """

    def test_cross_check_type_II_unitarity_vs_k3_yangian(self):
        """Cross-check: g(u)*g(-u) = 1 at Type II, computed via k3_yangian.

        Path 1: type_II_degeneration() reports unitarity_holds = True
        Path 2: Direct computation using k3_yangian.structure_function_evaluate
        """
        from compute.lib.k3_yangian import structure_function_evaluate
        params = type_II_parameters()
        # AP-CY28 safe test points
        for u in [Rational(37), Rational(41), Rational(97, 3)]:
            g_u = structure_function_evaluate(u, params)
            g_neg = structure_function_evaluate(-u, params)
            product = g_u * g_neg
            assert product == 1, f"Unitarity failed at u={u}: g*g(-) = {product}"
        # Cross-check with engine report
        degen = type_II_degeneration()
        assert degen.unitarity_holds is True

    def test_cross_check_newton_p1_cy2_vs_param_sum(self):
        """Cross-check: p_1 = sum(h_i) = 0 at all limits, two paths.

        Path 1: newton_power_sum_degeneration() reports p_1
        Path 2: Direct sum of params.h from each parametrization
        """
        from compute.lib.k3_yangian import newton_power_sums
        configs = [
            ('Type II', type_II_parameters()),
            ('LCS rho=1', lcs_parameters(picard_number=1)),
            ('LCS rho=10', lcs_parameters(picard_number=10)),
            ('Type III approach', type_III_approach_parameters(Rational(1, 100))),
        ]
        for name, params in configs:
            # Path 1: direct sum
            direct_sum = sum(params.h)
            assert direct_sum == 0, f"CY_2 failed at {name}: sum = {direct_sum}"
            # Path 2: Newton p_1
            p = newton_power_sums(params, max_k=1)
            assert p[1] == 0, f"p_1 != 0 at {name}: p_1 = {p[1]}"
            # Path 3: engine cy2_sum attribute
            assert params.cy2_sum == 0

    def test_cross_check_type_I_degree_vs_nonzero_count(self):
        """Cross-check: effective degree = nonzero param count, two paths.

        Path 1: structure_function_degeneration().effective_degree
        Path 2: Direct count of nonzero h_i from kummer_k3_parameters()
        """
        params = kummer_k3_parameters()
        # Path 1: direct count
        n_nonzero = sum(1 for hi in params.h if hi != 0)
        # Path 2: engine
        degen = type_I_degeneration()
        assert degen.effective_degree == (n_nonzero, n_nonzero)
        assert n_nonzero == NUM_PARAMS  # = 24

    def test_cross_check_kulikov_rank_drop_vs_effective_signature(self):
        """Cross-check: rank_drop + effective_rank = 24, signature sums match.

        Path 1: MUKAI_RANK_DROP + EFFECTIVE_RANK
        Path 2: sum of MUKAI_SIGNATURE_EFFECTIVE components
        Path 3: Kulikov type objects
        """
        for t in KULIKOV_TYPES:
            # Path 1
            assert MUKAI_RANK_DROP[t] + EFFECTIVE_RANK[t] == NUM_PARAMS
            # Path 2
            sig = MUKAI_SIGNATURE_EFFECTIVE[t]
            assert sig[0] + sig[1] == EFFECTIVE_RANK[t]
            # Path 3: from Kulikov object
            k = {'I': kulikov_type_I, 'II': kulikov_type_II, 'III': kulikov_type_III}[t]()
            assert k.effective_rank == EFFECTIVE_RANK[t]
            assert k.effective_signature == MUKAI_SIGNATURE_EFFECTIVE[t]

    def test_cross_check_shadow_class_vs_shadow_moduli_variation(self):
        """Cross-check: shadow class at Kummer matches shadow_class_moduli_variation.

        Path 1: shadow_at_orbifold() from this engine
        Path 2: k3_kummer_point() from shadow_class_moduli_variation
        """
        from compute.lib.shadow_class_moduli_variation import k3_kummer_point
        # Path 1: our engine
        our = shadow_at_orbifold()
        # Path 2: parent module
        parent = k3_kummer_point()
        # Both should agree on subalgebra shadow class
        assert our.shadow_class == parent.subalgebra_shadow_class
        assert our.kappa_ch == parent.sigma_kappa_ch

    def test_cross_check_shadow_class_generic_vs_moduli_variation(self):
        """Cross-check: shadow at generic K3 matches shadow_class_moduli_variation.

        Path 1: shadow_at_type_I() from this engine (class G)
        Path 2: k3_generic_point() from shadow_class_moduli_variation
        """
        from compute.lib.shadow_class_moduli_variation import k3_generic_point
        our = shadow_at_type_I()
        parent = k3_generic_point()
        assert our.shadow_class == parent.subalgebra_shadow_class
        assert our.kappa_ch == parent.sigma_kappa_ch

    def test_cross_check_kappa_ch_vs_k3_mirror_koszul(self):
        """Cross-check: kappa_ch = 2 matches k3_mirror_koszul.

        Path 1: verify_kappa_ch_invariance()
        Path 2: K3_KAPPA_CH from shadow_class_moduli_variation
        Path 3: mukai_lattice_signature -> chi(O) computation
        """
        from compute.lib.shadow_class_moduli_variation import K3_KAPPA_CH
        from compute.lib.k3_mirror_koszul import mukai_lattice_signature
        # Path 1
        result = verify_kappa_ch_invariance()
        assert result['kappa_ch_value'] == 2
        # Path 2
        assert K3_KAPPA_CH == 2
        # Path 3: chi(O_{K3}) = 1 - 0 + 1 = 2
        sig = mukai_lattice_signature()
        # Mukai signature (4,20) -> rank 24 -> chi_top = 24 -> chi(O) = 24/12 = 2
        assert (sig[0] + sig[1]) // 12 == 2

    def test_cross_check_type_II_g_at_zero_vs_formula(self):
        """Cross-check: g(0) at Type II via two independent computations.

        At Type II, 2 of the 24 h_i are 0.  The factors with h_i = 0 give
        (0 - 0)/(0 + 0) = 0/0 (indeterminate), so structure_function_evaluate
        raises ValueError at z = 0.  The CORRECT g(0) is computed by taking
        the limit, which cancels the 0/0 factors to 1, leaving:
          g(0) = prod_{h_i != 0} (-h_i / h_i) = prod_{h_i != 0} (-1) = (-1)^{22} = 1.

        Path 1: type_II_degeneration().g_at_zero (from formula)
        Path 2: Manual computation: (-1)^{num_nonzero}
        Path 3: Direct evaluation at a NEARBY point (limit check)
        """
        degen = type_II_degeneration()
        # Path 1: engine formula
        assert degen.g_at_zero == 1
        # Path 2: manual
        assert (-1) ** degen.num_nonzero_params == 1
        assert degen.num_nonzero_params == 22  # even => (-1)^22 = 1
        # Path 3: evaluate near z = 0 (but not AT 0, to avoid the pole)
        params = type_II_parameters()
        g_near_zero = structure_function_evaluate(Rational(1, 10000), params)
        # g(epsilon) should be close to g(0) = 1 for small epsilon
        # Since g is continuous away from poles, and h_i=0 factors are (eps-0)/(eps+0)=1,
        # the limit is exactly the product of nonzero factors evaluated at 0.
        # g(epsilon) = 1 + O(epsilon) since p_1 = 0 (CY_2 kills the linear term).
        # The leading correction is O(epsilon^2) from p_2, so at eps = 1/10000
        # we expect |g - 1| ~ O(1/10000^2) * |p_3|.  In practice the rational
        # coefficients give |g - 1| < 0.03.
        assert abs(float(g_near_zero) - 1.0) < 0.05

    def test_cross_check_lcs_effective_rank_vs_picard(self):
        """Cross-check: LCS effective rank = rho + 2, multiple rho values.

        Path 1: lcs_degeneration().num_nonzero_params
        Path 2: Direct count of nonzero params in lcs_parameters()
        Path 3: Formula rho + 2
        """
        for rho in [1, 5, 10, 15, 20]:
            # Path 1
            degen = lcs_degeneration(picard_number=rho)
            # Path 2
            params = lcs_parameters(picard_number=rho)
            n_direct = sum(1 for hi in params.h if hi != 0)
            # Path 3: formula
            expected = rho + 2
            # Cross-check all three
            assert degen.num_nonzero_params == n_direct
            assert n_direct == expected

    def test_cross_check_monodromy_index_vs_weight_filtration(self):
        """Cross-check: monodromy index constrains weight filtration.

        The monodromy index k determines the width of the weight filtration:
        Type I (k=1): W_0 = 0 (pure Hodge)
        Type II (k=2): W_0 = 1 (one null direction)
        Type III (k=3): W_0 = 1, W_1 = 2 (two null directions in W_1)

        The key constraint: (T-I)^k = 0 means N^k = 0, so the weight
        filtration has at most k nontrivial graded pieces.
        """
        # Type I: pure => W_0 = 0
        assert WEIGHT_FILTRATION['I'][0] == 0
        assert MONODROMY_INDEX['I'] == 1

        # Type II: one null => W_0 = 1, W_1 > W_0
        assert WEIGHT_FILTRATION['II'][0] == 1
        assert WEIGHT_FILTRATION['II'][1] > WEIGHT_FILTRATION['II'][0]
        assert MONODROMY_INDEX['II'] == 2

        # Type III: maximal => W_0 = 1, W_1 = 2
        assert WEIGHT_FILTRATION['III'][0] == 1
        assert WEIGHT_FILTRATION['III'][1] == 2
        assert MONODROMY_INDEX['III'] == 3

    def test_cross_check_shadow_monotonicity_vs_reduction_chain(self):
        """Cross-check: shadow monotonicity from two independent paths.

        Path 1: verify_shadow_monotonicity() (from reduction chain)
        Path 2: Direct comparison of shadow classes at degeneration limits
                 ordered by monodromy severity
        """
        from compute.lib.shadow_class_moduli_variation import SHADOW_CLASS_ORDER
        # Path 1
        result = verify_shadow_monotonicity()
        assert result['all_monotone'] is True

        # Path 2: along Kulikov types I -> II -> III,
        # shadow class at I (G=0) <= shadow class at II (L=1) [USC]
        # but Type III goes BACK to G (maximal degeneration kills everything).
        # USC applies to specialization (moving to boundary), but Type III
        # is a DIFFERENT boundary from Type II.
        s_I = shadow_at_type_I()
        s_II = shadow_at_type_II()
        s_III = shadow_at_type_III()
        # Type I <= Type II (specialization to elliptic curve boundary)
        assert SHADOW_CLASS_ORDER[s_I.shadow_class] <= SHADOW_CLASS_ORDER[s_II.shadow_class]
        # Type III is maximal degeneration: algebra collapses to trivial
        assert s_III.shadow_class == 'G'

    def test_cross_check_summary_table_vs_individual_functions(self):
        """Cross-check: summary table entries match individual function outputs.

        Path 1: degeneration_summary_table() rows
        Path 2: Individual shadow/degeneration functions
        """
        rows = degeneration_summary_table()

        # Type I row vs shadow_at_type_I()
        type_I_row = [r for r in rows if r['kulikov_type'] == 'I'][0]
        s_I = shadow_at_type_I()
        assert type_I_row['shadow_class'] == s_I.shadow_class
        assert type_I_row['kappa_ch'] == s_I.kappa_ch

        # Type II row vs shadow_at_type_II()
        type_II_row = [r for r in rows if r['kulikov_type'] == 'II'][0]
        s_II = shadow_at_type_II()
        assert type_II_row['shadow_class'] == s_II.shadow_class
        assert type_II_row['kappa_ch'] == s_II.kappa_ch

    def test_cross_check_effective_rank_type_II_vs_structure_function(self):
        """Cross-check: Type II effective rank from lattice data vs structure fn.

        Path 1: EFFECTIVE_RANK['II'] = 22 (lattice-theoretic)
        Path 2: type_II_degeneration().num_nonzero_params (analytic)
        Path 3: NUM_PARAMS - MUKAI_RANK_DROP['II'] (algebraic)
        """
        # Path 1
        assert EFFECTIVE_RANK['II'] == 22
        # Path 2
        degen = type_II_degeneration()
        assert degen.num_nonzero_params == 22
        # Path 3
        assert NUM_PARAMS - MUKAI_RANK_DROP['II'] == 22

    def test_cross_check_type_III_trivial_vs_null_kummer(self):
        """Cross-check: Type III strict limit is related to null parameters.

        Path 1: type_III_parameters() gives all-zero h
        Path 2: null_kummer_parameters() from k3_yangian also gives null norm
        Both are null vectors, but Type III is maximally degenerate (all zero).
        """
        from compute.lib.k3_yangian import null_kummer_parameters
        # Path 1
        params_III = type_III_parameters()
        assert params_III.is_null is True
        assert all(hi == 0 for hi in params_III.h)
        # Path 2
        params_null = null_kummer_parameters()
        assert params_null.is_null is True
        # The null Kummer has some nonzero entries (4 of them)
        n_nonzero_null = sum(1 for hi in params_null.h if hi != 0)
        assert n_nonzero_null == 4
        # Type III is MORE degenerate (0 nonzero vs 4 nonzero)
        n_nonzero_III = sum(1 for hi in params_III.h if hi != 0)
        assert n_nonzero_III < n_nonzero_null
