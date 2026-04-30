r"""Tests for the raw \(m_3\)--\(B^{(2)}_{\mathrm{term}}\) witness.

The owned engine verifies the strict termwise calculation

    [m_3,B^{(2)}_{\mathrm{term}}][a|a|a|a|b]=2\alpha[b].

It also asserts the corrected scope: local \(\mathbb P^2\) is a
noncompact diagnostic; \(B^{(2)}_{\mathrm{term}}\) is not Costello's
corrected \(B^{(2)}_{\mathrm{TCFT}}\); compact \(CY_3\) vanishing needs
a corrected TCFT comparison datum or an \(HH^{-2}\) filtration theorem.
"""

from fractions import Fraction

import pytest

from compute.lib.obs_ainf_local_p2 import (
    ExtGenerator,
    MinimalCyclicCY3,
    BarElement,
    BarLinComb,
    b2_map,
    b2_on_lincomb,
    m3_bar,
    m3_on_lincomb,
    commutator_m3_b2,
    compute_commutator_on_cc4,
    compute_commutator_on_cc5,
    compute_key_element_aaaab,
    compute_key_element_aabaa,
    master_obs_ainf_computation,
    full_obs_ainf_analysis,
    raw_witness_scope,
    serre_pairing,
    verify_pairing_nondegeneracy,
    verify_pairing_symmetry,
    ALL_GENERATORS,
    e, x1, x2, x3, y1, y2, y3, w,
)

F = Fraction


# ================================================================
# SECTION 1: ALGEBRA CONSISTENCY
# ================================================================

class TestAlgebraConsistency:
    """Verify the minimal cyclic A_infinity CY_3 algebra is self-consistent."""

    def test_cyclic_invariance_mu3_alpha1(self):
        """Cyclic invariance holds for mu_3 with alpha=1."""
        alg = MinimalCyclicCY3(alpha=F(1))
        ok, msg = alg.verify_cyclic_invariance_m3()
        assert ok, msg

    def test_cyclic_invariance_mu3_alpha2(self):
        """Cyclic invariance holds for mu_3 with alpha=2."""
        alg = MinimalCyclicCY3(alpha=F(2))
        ok, msg = alg.verify_cyclic_invariance_m3()
        assert ok, msg

    def test_cyclic_invariance_mu3_alpha0(self):
        """Cyclic invariance holds trivially for the formal case."""
        alg = MinimalCyclicCY3(alpha=F(0))
        ok, msg = alg.verify_cyclic_invariance_m3()
        assert ok, msg

    def test_ainf_relations_alpha1(self):
        """A_infinity relations hold through n=4 for alpha=1."""
        alg = MinimalCyclicCY3(alpha=F(1))
        ok, msg = alg.verify_ainf_relations()
        assert ok, msg

    def test_ainf_relations_alpha2(self):
        """A_infinity relations hold through n=4 for alpha=2."""
        alg = MinimalCyclicCY3(alpha=F(2))
        ok, msg = alg.verify_ainf_relations()
        assert ok, msg

    def test_ainf_relations_formal(self):
        """A_infinity relations hold trivially for the formal case."""
        alg = MinimalCyclicCY3(alpha=F(0))
        ok, msg = alg.verify_ainf_relations()
        assert ok, msg

    def test_pairing_nondegeneracy(self):
        """The CY_3 pairing is non-degenerate on the 8-generator model."""
        assert verify_pairing_nondegeneracy()

    def test_pairing_symmetry(self):
        """The CY_3 pairing satisfies graded symmetry."""
        assert verify_pairing_symmetry()

    def test_pairing_degree_constraint(self):
        """The CY_3 pairing vanishes unless |a|+|b|=3."""
        for a in ALL_GENERATORS:
            for b in ALL_GENERATORS:
                if a.degree + b.degree != 3:
                    assert serre_pairing(a, b) == F(0), (
                        f"<{a},{b}> should be 0 but got {serre_pairing(a, b)}"
                    )

    def test_mu3_strict_unitality(self):
        """mu_3 vanishes when any input is the unit."""
        alg = MinimalCyclicCY3(alpha=F(1))
        for x in alg.aug_basis:
            for y in alg.aug_basis:
                assert alg.m3(alg.UNIT, x, y) == []
                assert alg.m3(x, alg.UNIT, y) == []
                assert alg.m3(x, y, alg.UNIT) == []

    def test_mu3_only_nontrivial_on_aaa(self):
        """mu_3 is nonzero only on (a, a, a)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        for x in alg.aug_basis:
            for y in alg.aug_basis:
                for z in alg.aug_basis:
                    result = alg.m3(x, y, z)
                    if (x, y, z) == (alg.A, alg.A, alg.A):
                        assert result == [(F(1), alg.B)], (
                            f"mu_3(a,a,a) should be [(1, b)] but got {result}"
                        )
                    else:
                        assert result == [], (
                            f"mu_3({x},{y},{z}) should be [] but got {result}"
                        )

    def test_mu2_zero_on_augmentation(self):
        """mu_2 vanishes on the augmentation ideal."""
        alg = MinimalCyclicCY3(alpha=F(1))
        for x in alg.aug_basis:
            for y in alg.aug_basis:
                assert alg.m2(x, y) == [], (
                    f"mu_2({x},{y}) should be [] but got {alg.m2(x, y)}"
                )

    def test_dimension_count(self):
        """The algebra has 4 basis elements: e, a, b, w."""
        alg = MinimalCyclicCY3()
        assert len(alg.basis) == 4
        assert len(alg.aug_basis) == 3

    def test_degree_spectrum(self):
        """Degrees are 0, 1, 2, 3 (CY_3)."""
        alg = MinimalCyclicCY3()
        degrees = sorted(g.degree for g in alg.basis)
        assert degrees == [0, 1, 2, 3]


# ================================================================
# SECTION 2: FORMAL CASE (alpha = 0)
# ================================================================

class TestFormalCase:
    """When alpha=0 (formal), [m_3, B^{(2)}] = 0 trivially."""

    def test_formal_cc4_vanishes(self):
        """[m_3, B^{(2)}] = 0 on all of CC_4 for the formal algebra."""
        alg = MinimalCyclicCY3(alpha=F(0))
        cc4 = compute_commutator_on_cc4(alg)
        assert cc4["commutator_vanishes"]
        assert cc4["num_nonzero"] == 0

    def test_formal_cc5_vanishes(self):
        """[m_3, B^{(2)}] = 0 on all of CC_5 for the formal algebra."""
        alg = MinimalCyclicCY3(alpha=F(0))
        cc5 = compute_commutator_on_cc5(alg)
        assert cc5["commutator_vanishes"]
        assert cc5["num_nonzero"] == 0

    def test_formal_key_element_zero(self):
        """[m_3, B^{(2)}]([a|a|a|a|b]) = 0 for the formal algebra."""
        alg = MinimalCyclicCY3(alpha=F(0))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))
        comm = commutator_m3_b2(elem, alg)
        assert comm.is_zero

    def test_formal_master_computation(self):
        """Master computation records trivial raw vanishing for alpha=0."""
        result = master_obs_ainf_computation(alpha=F(0))
        assert result["raw_termwise_commutator_vanishes"]
        assert result["termwise_status"] == "zero_formal"
        assert result["compact_cy3_vanishing_proved"] is False


# ================================================================
# SECTION 3: RAW TERMWISE STRICT WITNESS
# ================================================================

class TestRawTermwiseWitness:
    """The central result: the raw termwise strict witness is nonzero."""

    def test_commutator_nonzero_on_aaaab(self):
        """[m_3, B^{(2)}]([a|a|a|a|b]) = 2*[b] != 0."""
        alg = MinimalCyclicCY3(alpha=F(1))
        result = compute_key_element_aaaab(alg)
        assert not result["commutator_is_zero"]
        assert result["commutator"] == "2*[b]"

    def test_commutator_nonzero_on_aabaa(self):
        """[m_3, B^{(2)}]([a|a|b|a|a]) = 4*[b] != 0."""
        alg = MinimalCyclicCY3(alpha=F(1))
        result = compute_key_element_aabaa(alg)
        assert not result["commutator_is_zero"]
        assert result["commutator"] == "4*[b]"

    def test_commutator_nonzero_on_aaaaa(self):
        """[m_3, B^{(2)}]([a|a|a|a|a]) = -6*[a] != 0."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen = alg.A
        elem = BarElement(factors=(a_gen,) * 5)
        comm = commutator_m3_b2(elem, alg)
        assert not comm.is_zero
        s = comm.simplify()
        assert len(s.terms) == 1
        assert s.terms[0].coeff == F(-6)
        assert s.terms[0].factors == (a_gen,)

    def test_cc4_has_10_nonzero(self):
        """Exactly 10 elements of CC_4 have nonzero commutator."""
        alg = MinimalCyclicCY3(alpha=F(1))
        cc4 = compute_commutator_on_cc4(alg)
        assert not cc4["commutator_vanishes"]
        assert cc4["num_nonzero"] == 10

    def test_cc5_has_57_nonzero(self):
        """57 elements of CC_5 have nonzero commutator."""
        alg = MinimalCyclicCY3(alpha=F(1))
        cc5 = compute_commutator_on_cc5(alg)
        assert not cc5["commutator_vanishes"]
        assert cc5["num_nonzero"] == 57

    def test_raw_termwise_status_is_nonzero_witness(self):
        """Master computation reports a nonzero raw termwise witness."""
        result = master_obs_ainf_computation(alpha=F(1))
        assert result["operator"] == "B^{(2)}_term"
        assert result["raw_witness_nonzero"]
        assert not result["raw_termwise_commutator_vanishes"]
        assert result["termwise_status"] == "nonzero_witness"
        assert result["compact_cy3_vanishing_proved"] is False

    def test_cyclicity_does_not_kill_raw_witness(self):
        """Cyclic invariance holds while the raw termwise witness is nonzero."""
        result = master_obs_ainf_computation(alpha=F(1))
        assert result["cyclic_invariance_ok"]
        assert result["raw_witness_nonzero"]


# ================================================================
# SECTION 4: ALPHA-SCALING (LINEARITY)
# ================================================================

class TestAlphaScaling:
    """The raw termwise witness scales linearly in alpha."""

    def test_aaaab_linear_in_alpha(self):
        """[m_3, B^{(2)}]([a|a|a|a|b]) = 2*alpha*[b]."""
        for alpha_val in [0, 1, 2, 3, 5, -1]:
            alg = MinimalCyclicCY3(alpha=F(alpha_val))
            a_gen, b_gen = alg.A, alg.B
            elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))
            comm = commutator_m3_b2(elem, alg).simplify()

            if alpha_val == 0:
                assert comm.is_zero
            else:
                assert len(comm.terms) == 1
                assert comm.terms[0].factors == (b_gen,)
                assert comm.terms[0].coeff == F(2 * alpha_val)

    def test_aaaaa_linear_in_alpha(self):
        """[m_3, B^{(2)}]([a|a|a|a|a]) = -6*alpha*[a]."""
        for alpha_val in [0, 1, 2, 3, -1]:
            alg = MinimalCyclicCY3(alpha=F(alpha_val))
            a_gen = alg.A
            elem = BarElement(factors=(a_gen,) * 5)
            comm = commutator_m3_b2(elem, alg).simplify()

            if alpha_val == 0:
                assert comm.is_zero
            else:
                assert len(comm.terms) == 1
                assert comm.terms[0].coeff == F(-6 * alpha_val)

    def test_baaaa_linear_in_alpha(self):
        """[m_3, B^{(2)}]([b|a|a|a|a]) = 6*alpha*[b]."""
        for alpha_val in [0, 1, 2]:
            alg = MinimalCyclicCY3(alpha=F(alpha_val))
            a_gen, b_gen = alg.A, alg.B
            elem = BarElement(factors=(b_gen, a_gen, a_gen, a_gen, a_gen))
            comm = commutator_m3_b2(elem, alg).simplify()

            if alpha_val == 0:
                assert comm.is_zero
            else:
                assert len(comm.terms) == 1
                assert comm.terms[0].coeff == F(6 * alpha_val)

    def test_obstruction_proportional_to_alpha(self):
        """CC_4 nonzero count is 0 iff alpha = 0, positive otherwise."""
        for alpha_val in [0, 1, 2, -1]:
            alg = MinimalCyclicCY3(alpha=F(alpha_val))
            cc4 = compute_commutator_on_cc4(alg)
            if alpha_val == 0:
                assert cc4["num_nonzero"] == 0
            else:
                assert cc4["num_nonzero"] > 0


# ================================================================
# SECTION 5: B^{(2)} SIGN CONVENTION (BAR-DESUSPENDED)
# ================================================================

class TestB2SignConvention:
    """Verify the bar-desuspended sign convention for B^{(2)}."""

    def test_b2_on_aaaab_is_4aaa(self):
        """B^{(2)}([a|a|a|a|b]) = 4*[a|a|a].

        All 4 contractions (i,4) have the same sign +1 because
        |s^{-1}a| = 0 (degree-1 elements are degree-0 after desuspension).
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))
        result = b2_map(elem, alg).simplify()
        assert len(result.terms) == 1
        assert result.terms[0].factors == (a_gen, a_gen, a_gen)
        assert result.terms[0].coeff == F(4)

    def test_b2_on_bab_is_2b(self):
        """B^{(2)}([b|a|b]) = 2*[b].

        pair(0,1): <b,a>=1, sign=+1 -> [b]
        pair(1,2): <a,b>=1, sign=+1 -> [b]
        pair(0,2): <b,b>=0
        Total: 2*[b]
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(b_gen, a_gen, b_gen))
        result = b2_map(elem, alg).simplify()
        assert len(result.terms) == 1
        assert result.terms[0].coeff == F(2)

    def test_b2_on_abb_is_zero(self):
        """B^{(2)}([a|b|b]) = 0.

        pair(0,1): <a,b>=1, sign=+1 -> [b]
        pair(0,2): <a,b>=1, sign=(-1)^{(|b|-1)*(|b|-1)} = (-1)^1 = -1 -> -[b]
        pair(1,2): <b,b>=0
        Total: [b] - [b] = 0.

        This is the KEY CANCELLATION: the bar-desuspended sign of
        s^{-1}b (degree 1) passing s^{-1}b (degree 1) gives -1.
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, b_gen, b_gen))
        result = b2_map(elem, alg).simplify()
        assert result.is_zero

    def test_b2_on_ab_is_unit(self):
        """B^{(2)}([a|b]) = [e].

        Only one pair: (0,1), <a,b>=1, sign=+1.
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, b_gen))
        result = b2_map(elem, alg).simplify()
        assert len(result.terms) == 1
        assert result.terms[0].coeff == F(1)


# ================================================================
# SECTION 6: m_3 BAR DIFFERENTIAL
# ================================================================

class TestM3Bar:
    """Verify the m_3 component of the bar differential."""

    def test_m3_on_aaaab(self):
        """m_3([a|a|a|a|b]) = [b|a|b] + [a|b|b].

        Position (0,1,2): m_3(a,a,a)=b, bar_sign=+1 -> [b|a|b]
        Position (1,2,3): m_3(a,a,a)=b, bar_sign=+1 -> [a|b|b]
        Position (2,3,4): m_3(a,a,b)=0
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))
        result = m3_bar(elem, alg).simplify()
        assert len(result.terms) == 2

    def test_m3_on_aaa(self):
        """m_3([a|a|a]) = [b].

        Only position (0,1,2): m_3(a,a,a)=b, bar_sign=+1.
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen))
        result = m3_bar(elem, alg).simplify()
        assert len(result.terms) == 1
        assert result.terms[0].factors == (b_gen,)
        assert result.terms[0].coeff == F(1)

    def test_m3_on_bbb_is_zero(self):
        """m_3([b|b|b]) = 0 (mu_3(b,b,b)=0)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        b_gen = alg.B
        elem = BarElement(factors=(b_gen, b_gen, b_gen))
        result = m3_bar(elem, alg)
        assert result.simplify().is_zero

    def test_m3_on_aaaa(self):
        """m_3([a|a|a|a]) has 2 terms (positions 0 and 1)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen = alg.A
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen))
        result = m3_bar(elem, alg).simplify()
        assert len(result.terms) == 2

    def test_m3_formal_is_zero(self):
        """m_3 = 0 for the formal algebra on all CC_4 elements."""
        alg = MinimalCyclicCY3(alpha=F(0))
        a_gen = alg.A
        for combo in [(a_gen,)*5, (a_gen, a_gen, a_gen, a_gen, alg.B)]:
            elem = BarElement(factors=combo)
            result = m3_bar(elem, alg)
            assert result.simplify().is_zero


# ================================================================
# SECTION 7: DETAILED ROUTE VERIFICATION
# ================================================================

class TestRouteVerification:
    """Independently verify both routes of the commutator."""

    def test_route1_aaaab(self):
        """Route 1: m_3(B^{(2)}([a|a|a|a|b])) = m_3(4*[a|a|a]) = 4*[b]."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))

        # B^{(2)} first
        b2_result = b2_map(elem, alg).simplify()
        assert b2_result.terms[0].coeff == F(4)

        # Then m_3
        route1 = m3_on_lincomb(b2_result, alg).simplify()
        assert len(route1.terms) == 1
        assert route1.terms[0].coeff == F(4)
        assert route1.terms[0].factors == (b_gen,)

    def test_route2_aaaab(self):
        """Route 2: B^{(2)}(m_3([a|a|a|a|b])) = B^{(2)}([b|a|b]+[a|b|b]) = 2*[b]."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))

        # m_3 first
        m3_result = m3_bar(elem, alg)

        # Then B^{(2)}
        route2 = b2_on_lincomb(m3_result, alg).simplify()
        assert len(route2.terms) == 1
        assert route2.terms[0].coeff == F(2)
        assert route2.terms[0].factors == (b_gen,)

    def test_commutator_aaaab_is_2b(self):
        """[m_3, B^{(2)}]([a|a|a|a|b]) = route1 - route2 = 4[b] - 2[b] = 2[b]."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen))
        comm = commutator_m3_b2(elem, alg).simplify()
        assert len(comm.terms) == 1
        assert comm.terms[0].coeff == F(2)
        assert comm.terms[0].factors == (b_gen,)


# ================================================================
# SECTION 8: OBSTRUCTION STRUCTURE
# ================================================================

class TestObstructionStructure:
    """Analyze the structure of the nonzero obstruction."""

    def test_nonzero_cc4_elements_all_contain_enough_a(self):
        """All nonzero CC_4 elements have >= 3 copies of 'a'.

        m_3(a,a,a) = b requires 3 copies of a in the m_3 block, and
        B^{(2)} requires a compatible pair for contraction.
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        cc4 = compute_commutator_on_cc4(alg)
        for entry in cc4["nonzero_results"]:
            # Parse the input to count 'a' factors
            inp = entry["input"]
            a_count = inp.count("|a") + (1 if inp.startswith("[a") else 0)
            assert a_count >= 3, (
                f"Nonzero input {inp} has only {a_count} copies of 'a'"
            )

    def test_pure_a_element(self):
        """[m_3, B^{(2)}]([a|a|a|a|a]) = -6*[a].

        This is purely from m_3(a,a,a)=b followed by <b,a>=1 contraction.
        """
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen = alg.A
        elem = BarElement(factors=(a_gen,) * 5)
        comm = commutator_m3_b2(elem, alg).simplify()
        assert not comm.is_zero
        assert comm.terms[0].coeff == F(-6)

    def test_pure_b_element_is_zero(self):
        """[m_3, B^{(2)}]([b|b|b|b|b]) = 0 (no m_3 can fire)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        b_gen = alg.B
        elem = BarElement(factors=(b_gen,) * 5)
        comm = commutator_m3_b2(elem, alg)
        assert comm.is_zero

    def test_w_elements_give_zero(self):
        """Elements with only w and b factors give zero (no m_3 fires)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        b_gen, w_gen = alg.B, alg.W
        for combo in [
            (w_gen, w_gen, w_gen, w_gen, w_gen),
            (b_gen, w_gen, b_gen, w_gen, b_gen),
            (w_gen, b_gen, w_gen, b_gen, w_gen),
        ]:
            elem = BarElement(factors=combo)
            comm = commutator_m3_b2(elem, alg)
            assert comm.is_zero, f"Expected 0 on {elem} but got {comm}"


# ================================================================
# SECTION 9: FULL ANALYSIS
# ================================================================

class TestFullAnalysis:
    """Test the full_obs_ainf_analysis() master function."""

    def test_full_analysis_runs(self):
        """The full analysis completes without error."""
        result = full_obs_ainf_analysis()
        assert "verdict" in result

    def test_formal_case_raw_vanishing(self):
        """Formal alpha=0 case reports trivial raw vanishing."""
        result = full_obs_ainf_analysis()
        assert result["formal_case"]["raw_termwise_commutator_vanishes"]
        assert result["formal_case"]["termwise_status"] == "zero_formal"

    def test_alpha1_strict_witness_nonzero(self):
        """Alpha=1 reports the strict nonzero raw witness."""
        result = full_obs_ainf_analysis()
        assert result["strict_witness_alpha1"]["raw_witness_nonzero"]
        assert not result["strict_witness_alpha1"]["raw_termwise_commutator_vanishes"]
        assert result["strict_witness_alpha1"]["termwise_status"] == "nonzero_witness"

    def test_alpha2_strict_witness_nonzero(self):
        """Alpha=2 also reports the strict nonzero raw witness."""
        result = full_obs_ainf_analysis()
        assert result["strict_witness_alpha2"]["raw_witness_nonzero"]
        assert not result["strict_witness_alpha2"]["raw_termwise_commutator_vanishes"]
        assert result["strict_witness_alpha2"]["termwise_status"] == "nonzero_witness"

    def test_verdict_consistency(self):
        """The verdict matches the individual results."""
        result = full_obs_ainf_analysis()
        v = result["verdict"]
        assert v["carrier"] == "B^{(2)}_term"
        assert v["raw_termwise_witness_nonzero"] is True
        assert v["compact_cy3_vanishing_proved"] is False
        assert v["identifies_b_term_with_b_tcft"] is False

    def test_corrected_scope_contract(self):
        """The scope record forbids compact-vanishing and TCFT conflation."""
        scope = raw_witness_scope()
        assert scope["carrier"] == "B^{(2)}_term"
        assert scope["not_carrier"] == "B^{(2)}_TCFT"
        assert scope["local_p2_scope"] == "noncompact diagnostic"
        assert scope["compact_cy3_vanishing_theorem"] is False
        assert scope["identifies_b_term_with_b_tcft"] is False
        assert scope["cyclicity_implies_termwise_vanishing"] is False
        assert scope["toric_bv_implies_raw_ainf_vanishing"] is False
        assert "HH^{-2}" in scope["compact_vanishing_requires"]


# ================================================================
# SECTION 10: CROSS-CHECKS
# ================================================================

class TestCrossChecks:
    """Cross-check the computation with independent methods."""

    def test_cc4_count_is_3_to_5(self):
        """CC_4 has 3^5 = 243 elements (3 augmentation ideal generators, 5 slots)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        cc4 = compute_commutator_on_cc4(alg)
        assert cc4["num_inputs"] == 3 ** 5

    def test_cc5_count_is_3_to_6(self):
        """CC_5 has 3^6 = 729 elements."""
        alg = MinimalCyclicCY3(alpha=F(1))
        cc5 = compute_commutator_on_cc5(alg)
        assert cc5["num_inputs"] == 3 ** 6

    def test_commutator_antilinear_in_coeff(self):
        """Scaling the input by c scales the commutator by c."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem1 = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen), coeff=F(1))
        elem3 = BarElement(factors=(a_gen, a_gen, a_gen, a_gen, b_gen), coeff=F(3))
        comm1 = commutator_m3_b2(elem1, alg).simplify()
        comm3 = commutator_m3_b2(elem3, alg).simplify()
        assert comm3.terms[0].coeff == F(3) * comm1.terms[0].coeff

    def test_b2_then_b2_is_well_defined(self):
        """B^{(2)} . B^{(2)} maps CC_4 -> CC_0 (a well-defined composition)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen, b_gen = alg.A, alg.B
        elem = BarElement(factors=(a_gen, b_gen, a_gen, b_gen, a_gen))
        b2_1 = b2_map(elem, alg)
        b2_2 = b2_on_lincomb(b2_1, alg).simplify()
        # Just check it doesn't crash and produces a result
        assert isinstance(b2_2, BarLinComb)

    def test_m3_then_m3_needs_cc6(self):
        """m_3 . m_3 is only nonzero on CC_6+ (6 factors minimum: 3+3-2=4 output)."""
        alg = MinimalCyclicCY3(alpha=F(1))
        a_gen = alg.A
        # On CC_4 (5 factors): m_3 gives CC_2 (3 factors), m_3 again gives CC_0 (1 factor)
        elem = BarElement(factors=(a_gen,) * 5)
        m3_1 = m3_bar(elem, alg)
        m3_2 = m3_on_lincomb(m3_1, alg).simplify()
        # m3_1 has 3-factor elements; m_3 on 3 factors gives 1 factor: valid
        assert isinstance(m3_2, BarLinComb)


# =========================================================================
# INDEPENDENT VERIFICATION (HZ3-11) -- raw termwise witness scope
# =========================================================================


from compute.lib.independent_verification import independent_verification


class TestRawTermwiseWitnessIV:
    r"""Independent verification: raw nonzero termwise witness, exact scope.

    The strict witness proves a statement about \(B^{(2)}_{\mathrm{term}}\):
    the pair-contraction commutator is nonzero on \([a|a|a|a|b]\) when
    \(\alpha\neq0\).  It does not prove a compact \(CY_3\) theorem and does
    not identify \(B^{(2)}_{\mathrm{term}}\) with \(B^{(2)}_{\mathrm{TCFT}}\).
    """

    @independent_verification(
        claim="raw-termwise-m3-b2-witness",
        derived_from=[
            "Direct route computation: m_3(B_term^(2)([a|a|a|a|b])) "
            "= 4 alpha [b]",
            "Direct route computation: B_term^(2)(m_3([a|a|a|a|b])) "
            "= 2 alpha [b]",
            "Scope record: local P^2 is noncompact diagnostic data; "
            "compact CY3 vanishing requires TCFT comparison or HH^{-2}.",
        ],
        verified_against=[
            "standalone/m3_b2_obstruction_vol3.tex strict witness: "
            "[m_3,B_term^(2)][a|a|a|a|b] = 2 alpha [b] != 0",
            "bidegree_decomposition_bB.py corrected theorem: bidegree "
            "bookkeeping is diagnostic, not a per-k vanishing proof",
            "spectral_seq_obs_ainf.py corrected theorem: termwise exactness "
            "requires corrected TCFT or HH^{-2} filtration input",
            "hopf_fibration_s3_framing.py scope record: toric BV "
            "triviality does not erase the raw A-infinity witness",
        ],
        disjoint_rationale=(
            "The route computation gives the coefficient. The scope record "
            "separates the raw carrier from Costello's corrected TCFT "
            "operator and from compact CY3 derived obstruction theorems."),
    )
    def test_raw_termwise_witness_scope(self):
        """Direct route computation plus corrected scope contract."""
        result = compute_key_element_aaaab(MinimalCyclicCY3(alpha=F(1)))
        assert result["step2_m3_of_b2"] == "4*[b]"
        assert result["step4_b2_of_m3"] == "2*[b]"
        assert result["commutator"] == "2*[b]"

        scope = raw_witness_scope()
        assert scope["witness_formula"] == (
            "[m_3,B^{(2)}_term][a|a|a|a|b] = 2*alpha*[b]"
        )
        assert scope["compact_cy3_vanishing_theorem"] is False
        assert scope["identifies_b_term_with_b_tcft"] is False
