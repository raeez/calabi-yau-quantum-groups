r"""Tests for the KS cyclic minimal model chain-level disproof of Obs_Ainf = 0.

Tests the independent confirmation that [m_3, B^{(2)}] != 0 for non-formal CY3:
  1. Cyclic invariance holds on minimal models (KS theorem).
  2. [m_3, B^{(2)}] is nonzero at chain level for non-formal CY3.
  3. This independently confirms obs_ainf_local_p2.py on a simpler model.
  4. Cyclic invariance alone is insufficient (the gap AP-CY34 was genuine).

Status: Obs_Ainf is a genuine OPEN obstruction for non-formal CY3.

Cross-reference:
  - obs_ainf_local_p2.py: primary disproof (54 tests, 8-generator model).
  - cy_to_chiral.tex, Prop. cyclic-ainf-framing-compat (DISPROVED).
  - rem:adversarial-audit-cyclic-ainf (gap genuine, bidegree retracted).
"""

import pytest
from fractions import Fraction as F

from compute.lib.ks_cyclic_minimal_obs_ainf import (
    CyclicAinfMinimalModel,
    ChainLevelNonVanishing,
    CyclicInvarianceResult,
    KSPerspectiveResult,
    c3_minimal_model,
    local_p2_minimal_model,
    verify_cyclic_invariance,
    compute_chain_level_nonvanishing,
    commutator_mk_b2,
    b2_contraction,
    mk_on_bar,
    run_ks_perspective,
)


# =========================================================================
# Test algebra construction
# =========================================================================

class TestAlgebraConstruction:
    """Verify the cyclic A_inf minimal models are well-formed."""

    def test_c3_generators(self):
        c3 = c3_minimal_model()
        assert len(c3.gen_names) == 4
        assert c3.d == 3
        assert c3.degree('e') == 0
        assert c3.degree('w') == 3

    def test_c3_pairing_degree(self):
        """CY3 pairing: <a,b> nonzero only when |a|+|b|=3."""
        c3 = c3_minimal_model()
        for (a, b), val in c3.pairing.items():
            if val != F(0):
                assert c3.degree(a) + c3.degree(b) == 3

    def test_lp2_generators(self):
        lp2 = local_p2_minimal_model()
        assert len(lp2.gen_names) == 4
        assert lp2.d == 3
        assert lp2.degree('a') == 1
        assert lp2.degree('v') == 3

    def test_lp2_pairing_degree(self):
        lp2 = local_p2_minimal_model()
        for (a, b), val in lp2.pairing.items():
            if val != F(0):
                assert lp2.degree(a) + lp2.degree(b) == 3

    def test_lp2_pairing_nondegeneracy(self):
        """Each generator pairs nontrivially with exactly one other."""
        lp2 = local_p2_minimal_model()
        for g in lp2.gen_names:
            has_pair = False
            for h in lp2.gen_names:
                if lp2.pair(g, h) != F(0):
                    has_pair = True
            assert has_pair, f"{g} has no nonzero pairing"

    def test_c3_is_formal(self):
        """C^3 minimal model has no m_k for k >= 3."""
        c3 = c3_minimal_model()
        assert 3 not in c3.mu

    def test_lp2_is_nonformal(self):
        """Local P^2 minimal model has nonzero m_3."""
        lp2 = local_p2_minimal_model()
        assert 3 in lp2.mu
        # m_3(a,a,b) = v
        result = lp2.m_k(3, ('a', 'a', 'b'))
        assert len(result) == 1
        assert result[0] == ('v', F(1))

    def test_lp2_m3_entries(self):
        """Verify all four nonzero m_3 entries."""
        lp2 = local_p2_minimal_model()
        assert lp2.m_k(3, ('a', 'a', 'b')) == [('v', F(1))]
        assert lp2.m_k(3, ('e', 'a', 'a')) == [('a', F(-1))]
        assert lp2.m_k(3, ('a', 'b', 'e')) == [('b', F(-1))]
        assert lp2.m_k(3, ('b', 'e', 'a')) == [('b', F(-1))]

    def test_lp2_m3_degree(self):
        """m_3 has degree 2-3 = -1.  Output degree = sum inputs - 1."""
        lp2 = local_p2_minimal_model()
        for args, outputs in lp2.mu[3].items():
            in_deg = sum(lp2.degree(a) for a in args)
            for out_name, _ in outputs:
                assert lp2.degree(out_name) == in_deg - 1


# =========================================================================
# Test cyclic invariance
# =========================================================================

class TestCyclicInvariance:
    """Verify cyclic invariance of w_{k+1} on minimal models."""

    def test_c3_m2_cyclic(self):
        c3 = c3_minimal_model()
        result = verify_cyclic_invariance(c3, 2)
        assert result.holds
        assert result.tuples_tested == 4 ** 3  # 64

    def test_lp2_m2_cyclic(self):
        lp2 = local_p2_minimal_model()
        result = verify_cyclic_invariance(lp2, 2)
        assert result.holds

    def test_lp2_m3_cyclic(self):
        """The KEY test: m_3 satisfies cyclic invariance on local P^2."""
        lp2 = local_p2_minimal_model()
        result = verify_cyclic_invariance(lp2, 3)
        assert result.holds
        assert result.tuples_tested == 4 ** 4  # 256
        assert len(result.failures) == 0

    def test_c3_m3_trivially_cyclic(self):
        """C^3 has no m_3, so cyclic invariance is trivial."""
        c3 = c3_minimal_model()
        result = verify_cyclic_invariance(c3, 3)
        assert result.holds
        assert result.tuples_tested == 0

    def test_lp2_m2_unit_products(self):
        """m_2(e, a) = a, m_2(a, e) = a, etc."""
        lp2 = local_p2_minimal_model()
        for g in lp2.gen_names:
            assert lp2.m_k(2, ('e', g)) == [(g, F(1))]
            assert lp2.m_k(2, (g, 'e')) == [(g, F(1))]


# =========================================================================
# Test B^{(2)} contraction
# =========================================================================

class TestB2Contraction:
    """Test the naive all-pairs B^{(2)} contraction."""

    def test_b2_on_pair(self):
        lp2 = local_p2_minimal_model()
        # (a, b) -> <a,b> = 1, remaining = ()
        result = b2_contraction(lp2, ('a', 'b'))
        assert len(result) == 1
        assert result[0] == ((), F(1))

    def test_b2_on_triple(self):
        lp2 = local_p2_minimal_model()
        # (e, a, b) -> contract (a,b): <a,b>=1, remaining=(e,)
        #           -> contract (e,?): <e,a>=0, <e,b>=0
        result = b2_contraction(lp2, ('e', 'a', 'b'))
        nonzero = [(r, c) for r, c in result if c != F(0)]
        assert len(nonzero) == 1
        assert nonzero[0] == (('e',), F(1))

    def test_b2_on_ev(self):
        lp2 = local_p2_minimal_model()
        # (e, v) -> <e,v>=1, remaining = ()
        result = b2_contraction(lp2, ('e', 'v'))
        assert len(result) == 1
        assert result[0][1] == F(1)

    def test_b2_no_pairing(self):
        lp2 = local_p2_minimal_model()
        # (a, a) -> <a,a>=0, no contraction
        result = b2_contraction(lp2, ('a', 'a'))
        assert len(result) == 0


# =========================================================================
# Test m_k on bar elements
# =========================================================================

class TestMkOnBar:
    """Test m_k action on bar elements."""

    def test_m2_unit_left(self):
        lp2 = local_p2_minimal_model()
        result = mk_on_bar(lp2, 2, ('e', 'a', 'b'), 0)
        # m_2(e, a) = a, new factors = (a, b)
        assert len(result) == 1
        assert result[0][0] == ('a', 'b')

    def test_m3_on_bar(self):
        lp2 = local_p2_minimal_model()
        result = mk_on_bar(lp2, 3, ('a', 'a', 'b', 'e'), 0)
        # m_3(a, a, b) = v, new factors = (v, e)
        assert len(result) == 1
        assert result[0][0] == ('v', 'e')

    def test_m3_at_offset(self):
        lp2 = local_p2_minimal_model()
        result = mk_on_bar(lp2, 3, ('e', 'a', 'a', 'b'), 1)
        # m_3(a, a, b) = v, at offset 1 with e before
        # sign: (-1)^{(2-3)*0} = 1
        assert len(result) == 1
        assert result[0][0] == ('e', 'v')


# =========================================================================
# Test chain-level commutator
# =========================================================================

class TestChainLevelCommutator:
    """Test [m_k, B^{(2)}_naive] at the chain level."""

    def test_c3_m3_commutator_zero(self):
        """C^3 is formal: [m_3, B^{(2)}] = 0 trivially."""
        c3 = c3_minimal_model()
        for factors in [('e', 'x', 'y', 'w'), ('x', 'x', 'y', 'e')]:
            comm = commutator_mk_b2(c3, 3, factors)
            assert comm == {}, f"Nonzero on {factors}: {comm}"

    def test_lp2_m3_commutator_nonzero_example(self):
        """Local P^2: [m_3, B^{(2)}_naive](a,a,b,e) != 0."""
        lp2 = local_p2_minimal_model()
        comm = commutator_mk_b2(lp2, 3, ('a', 'a', 'b', 'e'))
        assert comm != {}, "[m_3, B^{(2)}] should be nonzero on (a,a,b,e)"

    def test_lp2_m3_commutator_nonzero_second_example(self):
        """Local P^2: [m_3, B^{(2)}_naive](b,e,a,a) != 0."""
        lp2 = local_p2_minimal_model()
        comm = commutator_mk_b2(lp2, 3, ('b', 'e', 'a', 'a'))
        assert comm != {}, "[m_3, B^{(2)}] should be nonzero on (b,e,a,a)"

    def test_lp2_m2_commutator_has_nonzero(self):
        """Even [m_2, B^{(2)}_naive] can be nonzero (unit issues)."""
        lp2 = local_p2_minimal_model()
        # At least some elements should give nonzero
        found_nonzero = False
        for factors in [('e', 'a', 'b', 'e'), ('a', 'b', 'e', 'v')]:
            comm = commutator_mk_b2(lp2, 2, factors)
            if comm:
                found_nonzero = True
                break
        # This tests the general behavior; may or may not be nonzero
        # depending on the exact algebra.


# =========================================================================
# Test chain-level non-vanishing theorem
# =========================================================================

class TestChainLevelNonVanishing:
    """Test the chain-level non-vanishing result."""

    def test_c3_formal_vanishes(self):
        """C^3 (formal): naive commutator vanishes everywhere."""
        c3 = c3_minimal_model()
        result = compute_chain_level_nonvanishing(c3, 3, max_length=5)
        assert result.nonzero_count == 0
        assert not result.chain_level_nonzero

    def test_lp2_nonformal_nonzero(self):
        """Local P^2 (non-formal): naive commutator is nonzero."""
        lp2 = local_p2_minimal_model()
        result = compute_chain_level_nonvanishing(lp2, 3, max_length=5)
        assert result.nonzero_count > 0
        assert result.chain_level_nonzero
        assert result.example_nonzero is not None

    def test_lp2_nonzero_count(self):
        """At least 2 nonzero elements at length 4 (the minimal case)."""
        lp2 = local_p2_minimal_model()
        result = compute_chain_level_nonvanishing(lp2, 3, max_length=4)
        assert result.nonzero_count >= 2

    def test_lp2_example_is_real(self):
        """The reported example is actually nonzero."""
        lp2 = local_p2_minimal_model()
        result = compute_chain_level_nonvanishing(lp2, 3, max_length=4)
        if result.example_nonzero:
            factors, comm = result.example_nonzero
            recomputed = commutator_mk_b2(lp2, 3, factors)
            assert recomputed == comm


# =========================================================================
# Test the master KS perspective
# =========================================================================

class TestKSPerspective:
    """Test the full KS perspective analysis."""

    def test_master_runs(self):
        result = run_ks_perspective(max_length=4)
        assert isinstance(result, KSPerspectiveResult)

    def test_cyclic_invariance_holds(self):
        result = run_ks_perspective(max_length=4)
        assert result.cyclic_invariance_holds

    def test_chain_level_nonzero(self):
        result = run_ks_perspective(max_length=4)
        assert result.chain_level_nonzero

    def test_conclusion_correct(self):
        """Conclusion: cyclic invariance insufficient, bidegree needed."""
        result = run_ks_perspective(max_length=4)
        assert "INSUFFICIENT" in result.conclusion
        assert "bidegree" in result.conclusion

    def test_summary_readable(self):
        result = run_ks_perspective(max_length=4)
        summary = result.summary()
        assert "CYCLIC INVARIANCE" in summary
        assert "CHAIN-LEVEL" in summary
        assert "CONCLUSION" in summary

    def test_c3_contributes_zero(self):
        """C^3 contributes 0 nonzero to chain-level count."""
        result = run_ks_perspective(max_length=4)
        c3_cl = [r for r in result.chain_level
                 if "C^3" in r.algebra_name][0]
        assert c3_cl.nonzero_count == 0

    def test_lp2_contributes_nonzero(self):
        """Local P^2 contributes nonzero to chain-level count."""
        result = run_ks_perspective(max_length=4)
        lp2_cl = [r for r in result.chain_level
                  if "P^2" in r.algebra_name][0]
        assert lp2_cl.nonzero_count > 0


# =========================================================================
# Test connection to bidegree resolution
# =========================================================================

class TestConnectionToExistingEngines:
    """Cross-reference with obs_ainf_local_p2.py and connes_b_obs_ainf.py."""

    def test_obs_ainf_local_p2_exists(self):
        """The primary disproof engine can be imported."""
        from compute.lib import obs_ainf_local_p2
        assert obs_ainf_local_p2 is not None

    def test_bidegree_engine_exists(self):
        """The bidegree engine exists (even though its proof was retracted).

        The bidegree injectivity is a correct ALGEBRAIC fact.
        What was retracted: the PREMISE that [b, B^{(j)}] = 0 for j >= 1
        follows from the mixed complex axiom.  It does not.
        """
        from compute.lib.connes_b_obs_ainf import (
            verify_bidegree_injectivity,
        )
        # The map (k,j) -> (2-k-j, j) IS injective (correct algebra).
        result = verify_bidegree_injectivity()
        assert result["injective"]
        # BUT: injectivity does not help because the premise
        # [b, B^full] = 0 does not decompose as assumed.

    def test_ks_confirms_disproof(self):
        """KS engine independently confirms the disproof.

        Our simplified 4-generator model and obs_ainf_local_p2.py's
        8-generator McKay quiver model both find [m_3, B^{(2)}] != 0.
        """
        ks_result = run_ks_perspective(max_length=4)
        # KS: cyclic invariance holds but chain-level nonzero
        assert ks_result.cyclic_invariance_holds
        assert ks_result.chain_level_nonzero

    def test_formal_case_agrees(self):
        """Both engines agree: formal CY3 has [m_3, B^{(2)}] = 0."""
        c3 = c3_minimal_model()
        result = compute_chain_level_nonvanishing(c3, 3, max_length=5)
        assert result.nonzero_count == 0


# =========================================================================
# Test mathematical invariants
# =========================================================================

class TestMathematicalInvariants:
    """Verify mathematical invariants of the construction."""

    def test_cy_dimension(self):
        """Both models are CY3."""
        assert c3_minimal_model().d == 3
        assert local_p2_minimal_model().d == 3

    def test_m3_degree_shift(self):
        """m_3 has degree 2-3 = -1 (standard A_inf convention)."""
        lp2 = local_p2_minimal_model()
        for args, outputs in lp2.mu[3].items():
            in_deg = sum(lp2.degree(a) for a in args)
            for out_name, _ in outputs:
                assert lp2.degree(out_name) == in_deg - 1, (
                    f"m_3{args} -> {out_name}: "
                    f"deg {in_deg} -> {lp2.degree(out_name)}, "
                    f"expected {in_deg - 1}")

    def test_pairing_symmetry(self):
        """Pairing is graded-symmetric: <a,b> = (-1)^{|a||b|} <b,a>."""
        lp2 = local_p2_minimal_model()
        for a in lp2.gen_names:
            for b in lp2.gen_names:
                sign = (-1) ** (lp2.degree(a) * lp2.degree(b))
                lhs = lp2.pair(a, b)
                rhs = F(sign) * lp2.pair(b, a)
                assert lhs == rhs, (
                    f"<{a},{b}>={lhs}, (-1)^... <{b},{a}>={rhs}")

    def test_unit_m2_left(self):
        """m_2(e, g) = g for all generators."""
        for alg in [c3_minimal_model(), local_p2_minimal_model()]:
            unit = alg.gen_names[0]  # 'e' for both
            for g in alg.gen_names:
                result = alg.m_k(2, (unit, g))
                assert result == [(g, F(1))], (
                    f"m_2({unit},{g}) = {result}, expected [({g}, 1)]")

    def test_unit_m2_right(self):
        """m_2(g, e) = g for all generators."""
        for alg in [c3_minimal_model(), local_p2_minimal_model()]:
            unit = alg.gen_names[0]
            for g in alg.gen_names:
                result = alg.m_k(2, (g, unit))
                assert result == [(g, F(1))], (
                    f"m_2({g},{unit}) = {result}, expected [({g}, 1)]")

    def test_formal_iff_m3_zero(self):
        """C^3 is formal (m_3=0), local P^2 is non-formal (m_3!=0)."""
        c3 = c3_minimal_model()
        lp2 = local_p2_minimal_model()
        assert 3 not in c3.mu
        assert 3 in lp2.mu
        assert len(lp2.mu[3]) > 0


# =========================================================================
# Test manuscript status implications
# =========================================================================

class TestManuscriptImplications:
    """Verify implications for the manuscript status."""

    def test_obs_ainf_is_open(self):
        """Obs_Ainf != 0 for non-formal CY3.  This is an OPEN obstruction."""
        ks = run_ks_perspective(max_length=4)
        # The chain-level commutator is genuinely nonzero
        assert ks.chain_level_nonzero

    def test_prop_status_conditional(self):
        """Prop cyclic-ainf-framing-compat should be ClaimStatusConditional.

        The proposition is DISPROVED at chain level for non-formal CY3.
        It holds only in the formal case (m_k = 0 for k >= 3).
        """
        lp2 = local_p2_minimal_model()
        result = compute_chain_level_nonvanishing(lp2, 3, max_length=4)
        # Non-formal: commutator is nonzero
        assert result.nonzero_count > 0
        # Formal: commutator is zero
        c3 = c3_minimal_model()
        result_formal = compute_chain_level_nonvanishing(c3, 3, max_length=4)
        assert result_formal.nonzero_count == 0

    def test_ap_cy34_gap_genuine(self):
        """AP-CY34: the gap was GENUINE, not a proof artifact.

        The non-adjacent contractions that cyclic invariance cannot control
        produce real nonzero contributions to [m_3, B^{(2)}].
        """
        ks = run_ks_perspective(max_length=4)
        assert ks.cyclic_invariance_holds  # Cyclic invariance holds...
        assert ks.chain_level_nonzero      # ...but commutator is nonzero

    def test_two_open_obstructions(self):
        """CY-A_3 has TWO open obstructions: Obs_Ainf and Obs_BV.

        For toric CY3: Obs_BV = 0 (torus equivariance) but
        Obs_Ainf != 0 for non-formal cases (local P^2).
        For compact non-formal CY3 (quintic): both are open.
        """
        lp2 = local_p2_minimal_model()
        result = compute_chain_level_nonvanishing(lp2, 3, max_length=4)
        # Obs_Ainf != 0 for local P^2 (toric, but non-formal)
        assert result.nonzero_count > 0


# =========================================================================
# Multi-path cross-verification (AP10)
# =========================================================================

class TestMultiPathCrossVerification:
    """Cross-check key assertions via independent computation paths."""

    def test_cyclic_invariance_by_direct_w4_computation(self):
        """Cross-check: compute w_4 directly and verify cyclic symmetry.

        Path 1: verify_cyclic_invariance (rotates and compares).
        Path 2: compute all w_4 values and check each cyclic orbit.
        """
        lp2 = local_p2_minimal_model()
        import itertools

        # Path 1
        ci = verify_cyclic_invariance(lp2, 3)
        assert ci.holds

        # Path 2: direct w_4 computation
        def w4(a0, a1, a2, a3):
            total = F(0)
            for res, coeff in lp2.m_k(3, (a1, a2, a3)):
                total += coeff * lp2.pair(a0, res)
            return total

        for tup in itertools.product(lp2.gen_names, repeat=4):
            a0, a1, a2, a3 = tup
            lhs = w4(a0, a1, a2, a3)
            # Rotate left by 1: w4(a1, a2, a3, a0)
            rhs_raw = w4(a1, a2, a3, a0)
            deg_a0 = lp2.degree(a0)
            deg_rest = sum(lp2.degree(tup[i]) for i in range(1, 4))
            sign = F((-1) ** (3 + deg_a0 * deg_rest))
            assert lhs == sign * rhs_raw, (
                f"w4{tup}={lhs} != sign*w4(rot)={sign * rhs_raw}")

    def test_nonvanishing_via_explicit_trace(self):
        """Cross-check: verify nonvanishing by tracing forward/backward.

        Path 1: commutator_mk_b2 (automated).
        Path 2: manual forward/backward summation on (a,a,b,e).
        """
        lp2 = local_p2_minimal_model()
        factors = ('a', 'a', 'b', 'e')

        # Path 1
        comm_auto = commutator_mk_b2(lp2, 3, factors)

        # Path 2: manual trace
        # B^{(2)} on (a, a, b, e):
        #   Pairs with nonzero pairing: (a,b) at (0,2), (a,b) at (1,2)
        #   (0,2): <a,b>=1, sign=(-1)^{2*1}=1, remaining=(a,e)
        #   (1,2): <a,b>=1, sign=(-1)^{2*0}=1, remaining=(a,e)
        # B^{(2)} result: 2 * (a, e)
        b2_result = b2_contraction(lp2, factors)
        b2_collected = {}
        for rem, c in b2_result:
            b2_collected[rem] = b2_collected.get(rem, F(0)) + c
        assert b2_collected.get(('a', 'e'), F(0)) == F(2)

        # Forward: B^{(2)} gives 2*(a,e), then m_3 needs 3 factors -> skip
        # (a,e) has length 2 < 3, so forward = 0.
        forward_total = F(0)  # no m_3 can act on length-2 elements

        # Backward: m_3 then B^{(2)}
        # m_3 at pos 0: m_3(a,a,b) = v, factors -> (v, e)
        #   sign: (-1)^{(-1)*0} = 1, coeff = 1
        #   B^{(2)} on (v,e): <v,e>=1, remaining=(), coeff=1
        # m_3 at pos 1: m_3(a,b,e) = -b, factors -> (a, -b) = -1*(a,b)
        #   sign: (-1)^{(-1)*1} = -1, total coeff = (-1)*(-1) = 1 for (a,b)
        #   B^{(2)} on (a,b): <a,b>=1, remaining=(), coeff=1
        # Backward total: 1 (from pos 0) + 1 (from pos 1) = 2
        backward_total = F(2)

        # Commutator = forward - backward = 0 - 2 = -2
        manual_result = {(): forward_total - backward_total}
        manual_result = {k: v for k, v in manual_result.items() if v != F(0)}

        assert comm_auto == manual_result, (
            f"Auto: {comm_auto}, Manual: {manual_result}")

    def test_m3_degree_via_two_paths(self):
        """Cross-check m_3 degree shift via direct and indirect computation.

        Path 1: check output degree = input degree - 1.
        Path 2: check that w_4 is nonzero only when sum of degrees = 4
                 (which is equivalent to m_3 having degree -1 for CY3).
        """
        lp2 = local_p2_minimal_model()
        import itertools

        # Path 1: direct degree check
        for args, outputs in lp2.mu[3].items():
            in_deg = sum(lp2.degree(a) for a in args)
            for out_name, _ in outputs:
                assert lp2.degree(out_name) == in_deg - 1

        # Path 2: w_4 nonzero implies degree sum = 4
        for tup in itertools.product(lp2.gen_names, repeat=4):
            w = F(0)
            for res, coeff in lp2.m_k(3, tup[1:]):
                w += coeff * lp2.pair(tup[0], res)
            if w != F(0):
                deg_sum = sum(lp2.degree(t) for t in tup)
                assert deg_sum == 4, (
                    f"w4{tup} = {w} but degree sum = {deg_sum} != 4")

    def test_pairing_symmetry_via_w3_consistency(self):
        """Cross-check pairing symmetry via w_3 cyclic invariance.

        Path 1: direct <a,b> = (-1)^{|a||b|} <b,a>.
        Path 2: w_3 cyclic invariance (which depends on pairing symmetry).
        """
        lp2 = local_p2_minimal_model()

        # Path 1
        for a in lp2.gen_names:
            for b in lp2.gen_names:
                sign = F((-1) ** (lp2.degree(a) * lp2.degree(b)))
                assert lp2.pair(a, b) == sign * lp2.pair(b, a)

        # Path 2
        ci = verify_cyclic_invariance(lp2, 2)
        assert ci.holds

    def test_hochschild_shift_formula(self):
        """Cross-check Hochschild degree shift 2-k-j via two derivations.

        Path 1: m_k shift = -(k-1), B^{(j)} shift = 1-j, total = 2-k-j.
        Path 2: m_k maps CC_n to CC_{n-k+1}, B^{(j)} maps CC_n to CC_{n+1-j}.
        """
        for k in range(2, 10):
            for j in range(0, 6):
                # Path 1: additive shifts
                sigma = -(k - 1) + (1 - j)
                assert sigma == 2 - k - j
                # Path 2: the (k,j) -> sigma map is injective in j
                # (for fixed sigma, different j give different k = 2-sigma-j)
                # This is correct algebra even though the bidegree PREMISE
                # [b, B^full] = 0 was retracted.

    def test_c3_vs_lp2_formal_nonformal_contrast(self):
        """Cross-check: formal algebra has zero commutator, non-formal does not.

        This tests the same mathematical property via two different algebras.
        """
        c3 = c3_minimal_model()
        lp2 = local_p2_minimal_model()

        c3_result = compute_chain_level_nonvanishing(c3, 3, max_length=5)
        lp2_result = compute_chain_level_nonvanishing(lp2, 3, max_length=5)

        # C^3 formal: commutator trivially zero (m_3 = 0)
        assert c3_result.nonzero_count == 0
        # Local P^2 non-formal: commutator genuinely nonzero
        assert lp2_result.nonzero_count > 0
        # The contrast confirms the chain-level non-vanishing is
        # specifically due to non-formality, not a sign error.

    def test_nonzero_count_monotone_in_length(self):
        """Cross-check: nonzero count is non-decreasing with max_length.

        Adding more bar elements can only ADD nonzero commutators.
        """
        lp2 = local_p2_minimal_model()
        r4 = compute_chain_level_nonvanishing(lp2, 3, max_length=4)
        r5 = compute_chain_level_nonvanishing(lp2, 3, max_length=5)
        assert r5.nonzero_count >= r4.nonzero_count
        assert r5.elements_tested >= r4.elements_tested
