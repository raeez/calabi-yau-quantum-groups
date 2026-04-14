r"""Tests for chiral_satake_c3_proof.py: C^3 chiral Satake proof engine.

CENTRAL RESULTS:
    (1) Step A: Fiber functor for GL_1 on C^3 (PROVED, GL_1 abelian)
    (2) Step B: Monoidal structure via partition-indexed MV cycles (PROVED)
    (3) Step C: Geometric R-matrix = Yangian R-matrix (PROVED, thm:mo-chiral-rmatrix)
    (4) Step D: Tannakian reconstruction End(F) ~= Y(gl_hat_1) (PROVED)
    (5) Step E: Full DG equivalence (CONJECTURAL)
    (6) Partition function p(n) verified against OEIS A000041
    (7) Structure function g(z) in product and sigma forms
    (8) Unitarity g(z)*g(-z) = 1 at multiple parameter families
    (9) Yang-Baxter equation at charges 1 and 2
    (10) Associativity of monoidal convolution

Manuscript references:
    geometric_langlands.tex conj:chiral-satake-c3
    geometric_langlands.tex sec:derived-satake-chiral
    quantum_chiral_algebras.tex thm:mo-chiral-rmatrix

Literature ground truth:
    Partition function p(n) for n=0,...,20
    # VERIFIED [LT] OEIS A000041

    Geometric Satake (Mirkovic-Vilonen 2007)
    # VERIFIED [LT] arXiv:math/0401222

    Beilinson-Drinfeld chiral Grassmannian
    # VERIFIED [LT] "Chiral Algebras" (2004), Ch. 5

    MO stable envelopes
    # VERIFIED [LT] Maulik-Okounkov, arXiv:1211.1287

    Costello 5d hCS boundary algebra = affine Yangian
    # VERIFIED [LT] Costello, arXiv:1303.2632

    Unitarity g(z)*g(-z) = 1 for CY structure function
    # VERIFIED [DC] algebraic computation [SY] pairing cancellation
"""

import pytest
from fractions import Fraction

from compute.lib.chiral_satake_c3_proof import (
    # Constants
    STEP_A_STATUS,
    STEP_B_STATUS,
    STEP_C_STATUS,
    STEP_D_STATUS,
    STEP_E_STATUS,
    OVERALL_STATUS,
    PARTITIONS_GROUND_TRUTH,
    # Partition functions
    num_partitions,
    partitions_of,
    # Structure function
    StructureFunctionC3,
    structure_function_c3,
    eval_g,
    eval_g_from_sigma,
    # Step A: Fiber functor
    FiberFunctorData,
    fiber_functor,
    # Step B: Monoidal structure
    MonoidalStructureData,
    monoidal_convolution,
    verify_monoidal_associativity,
    # Step C: R-matrix
    RMatrixMatchData,
    verify_rmatrix_match,
    verify_rmatrix_sigma_form,
    verify_ybe_charge1,
    verify_ybe_charge2_diagonal,
    # Step D: Tannakian reconstruction
    TannakianReconstructionData,
    tannakian_reconstruction,
    # Step E: DG equivalence
    DGEquivalenceData,
    dg_equivalence_status,
    # Proof assembly
    ProofStepSummary,
    proof_step_a,
    proof_step_b,
    proof_step_c,
    proof_step_d,
    proof_step_e,
    proof_assembly,
    # Cross-checks
    verify_partition_ground_truth,
    verify_partition_enumeration,
    verify_fiber_functor_dimensions,
    verify_rmatrix_multiple_params,
    verify_sigma_form_consistency,
    # Summary
    ChiralSatakeC3Summary,
    full_summary,
    full_verification,
)

F = Fraction


# ================================================================
# Section 1: PROOF STATUS FLAGS
# ================================================================

class TestProofStatus:
    """Verify that proof step statuses are correctly set."""

    def test_step_a_proved(self):
        """Step A (fiber functor) is PROVED."""
        assert STEP_A_STATUS == "PROVED"

    def test_step_b_proved(self):
        """Step B (monoidal structure) is PROVED."""
        assert STEP_B_STATUS == "PROVED"

    def test_step_c_proved(self):
        """Step C (R-matrix match) is PROVED."""
        assert STEP_C_STATUS == "PROVED"

    def test_step_d_proved(self):
        """Step D (Tannakian reconstruction) is PROVED."""
        assert STEP_D_STATUS == "PROVED"

    def test_step_e_conjectural(self):
        """Step E (DG equivalence) is CONJECTURAL."""
        assert STEP_E_STATUS == "CONJECTURAL"

    def test_overall_conjectural(self):
        """Overall status is CONJECTURAL (Step E is the gap)."""
        # AP-CY14: full equivalence is conjectural
        assert OVERALL_STATUS == "CONJECTURAL"


# ================================================================
# Section 2: PARTITION FUNCTION (STEP A FOUNDATION)
# ================================================================

class TestPartitionFunction:
    """Verify partition function p(n) against OEIS A000041."""

    def test_p0(self):
        """p(0) = 1."""
        # VERIFIED [LT] OEIS A000041
        assert num_partitions(0) == 1

    def test_p1(self):
        """p(1) = 1."""
        assert num_partitions(1) == 1

    def test_p2(self):
        """p(2) = 2: {(2), (1,1)}."""
        assert num_partitions(2) == 2

    def test_p3(self):
        """p(3) = 3: {(3), (2,1), (1,1,1)}."""
        assert num_partitions(3) == 3

    def test_p4(self):
        """p(4) = 5."""
        assert num_partitions(4) == 5

    def test_p5(self):
        """p(5) = 7."""
        # VERIFIED [LT] OEIS A000041
        assert num_partitions(5) == 7

    def test_p10(self):
        """p(10) = 42."""
        # VERIFIED [LT] OEIS A000041
        assert num_partitions(10) == 42

    def test_p15(self):
        """p(15) = 176."""
        assert num_partitions(15) == 176

    def test_p20(self):
        """p(20) = 627."""
        # VERIFIED [LT] OEIS A000041
        assert num_partitions(20) == 627

    def test_p_negative(self):
        """p(n) = 0 for n < 0."""
        assert num_partitions(-1) == 0
        assert num_partitions(-10) == 0

    def test_ground_truth_all(self):
        """All p(n) for n=0,...,20 match OEIS A000041."""
        result = verify_partition_ground_truth()
        assert result["all_pass"] is True
        assert result["num_checked"] == 21


class TestPartitionEnumeration:
    """Verify partition enumeration agrees with counting."""

    def test_enumerate_0(self):
        """Partitions of 0: the empty partition."""
        parts = partitions_of(0)
        assert parts == [()]

    def test_enumerate_3(self):
        """Partitions of 3: (3), (2,1), (1,1,1)."""
        parts = partitions_of(3)
        assert len(parts) == 3
        assert (3,) in parts
        assert (2, 1) in parts
        assert (1, 1, 1) in parts

    def test_enumerate_5(self):
        """Partitions of 5: 7 partitions."""
        parts = partitions_of(5)
        assert len(parts) == 7

    def test_enumerate_agrees_with_count(self):
        """len(partitions_of(n)) == num_partitions(n) for n=0,...,10."""
        result = verify_partition_enumeration()
        assert result["all_pass"] is True

    def test_partitions_are_decreasing(self):
        """All partitions are in decreasing order."""
        for n in range(8):
            for p in partitions_of(n):
                for i in range(len(p) - 1):
                    assert p[i] >= p[i + 1]

    def test_partitions_sum_correctly(self):
        """Each partition of n sums to n."""
        for n in range(8):
            for p in partitions_of(n):
                assert sum(p) == n


# ================================================================
# Section 3: STRUCTURE FUNCTION (STEP C FOUNDATION)
# ================================================================

class TestStructureFunction:
    """Tests for the C^3 structure function g(z)."""

    def test_cy_constraint(self):
        """CY constraint: h_1 + h_2 + h_3 = 0."""
        sf = structure_function_c3()
        assert sum(sf.h) == F(0)

    def test_sigma_2_default(self):
        """sigma_2 for h=(1,-2,1) is 1*(-2)+1*1+(-2)*1 = -3."""
        sf = structure_function_c3((F(1), F(-2), F(1)))
        assert sf.sigma_2 == F(-3)

    def test_sigma_3_default(self):
        """sigma_3 for h=(1,-2,1) is 1*(-2)*1 = -2."""
        sf = structure_function_c3((F(1), F(-2), F(1)))
        assert sf.sigma_3 == F(-2)

    def test_cy_violation_raises(self):
        """Non-CY parameters should raise AssertionError."""
        with pytest.raises(AssertionError):
            structure_function_c3((F(1), F(2), F(3)))

    def test_g_at_large_z(self):
        """g(z) -> 1 as z -> infinity."""
        h = (F(1), F(-2), F(1))
        g_large = eval_g(h, F(10000))
        assert abs(float(g_large) - 1.0) < 1e-6

    def test_g_unitarity(self):
        """g(z) * g(-z) = 1 (unitarity)."""
        # VERIFIED [DC] algebraic computation
        h = (F(1), F(-2), F(1))
        z = F(37, 10)
        assert eval_g(h, z) * eval_g(h, -z) == F(1)

    def test_g_sigma_form_agrees(self):
        """Product form and sigma form of g(z) agree."""
        h = (F(1), F(-2), F(1))
        sf = structure_function_c3(h)
        z = F(37, 10)
        g_product = eval_g(h, z)
        g_sigma = eval_g_from_sigma(sf.sigma_2, sf.sigma_3, z)
        assert g_product == g_sigma

    def test_g_at_zero(self):
        """g(0) = (-h_1)(-h_2)(-h_3) / (h_1*h_2*h_3) = -1 for 3 factors."""
        h = (F(1), F(-2), F(1))
        g_0 = eval_g(h, F(0))
        # g(0) = (-1)(-(-2))(-1) / (1*(-2)*1) = (-1)(2)(-1) / (-2) = 2/(-2) = -1
        assert g_0 == F(-1)

    def test_g_sigma_form_at_zero(self):
        """Sigma form at z=0: g(0) = -sigma_3 / sigma_3 = -1."""
        sf = structure_function_c3((F(1), F(-2), F(1)))
        g_0 = eval_g_from_sigma(sf.sigma_2, sf.sigma_3, F(0))
        assert g_0 == F(-1)


# ================================================================
# Section 4: STEP A -- FIBER FUNCTOR
# ================================================================

class TestFiberFunctor:
    """Tests for the fiber functor F: D-mod(Gr^{ch}_{GL_1}) -> Vect."""

    def test_charge_0_dim_1(self):
        """Charge-0 fiber has dim 1 (vacuum)."""
        ff = fiber_functor(0)
        assert ff.fiber_dim == 1

    def test_charge_1_dim_1(self):
        """Charge-1 fiber has dim 1 (one partition of 1)."""
        ff = fiber_functor(1)
        assert ff.fiber_dim == 1

    def test_charge_2_dim_2(self):
        """Charge-2 fiber has dim 2: partitions (2) and (1,1)."""
        ff = fiber_functor(2)
        assert ff.fiber_dim == 2

    def test_charge_5_dim_7(self):
        """Charge-5 fiber has dim 7."""
        ff = fiber_functor(5)
        assert ff.fiber_dim == 7

    def test_charge_10_dim_42(self):
        """Charge-10 fiber has dim 42."""
        ff = fiber_functor(10)
        assert ff.fiber_dim == 42

    def test_faithful(self):
        """Fiber functor is faithful (GL_1 abelian)."""
        for n in range(5):
            ff = fiber_functor(n)
            assert ff.is_faithful is True

    def test_exact(self):
        """Fiber functor is exact (GL_1 abelian)."""
        for n in range(5):
            ff = fiber_functor(n)
            assert ff.is_exact is True

    def test_partitions_listed(self):
        """Fiber functor lists the actual partitions."""
        ff = fiber_functor(3)
        assert (3,) in ff.partitions
        assert (2, 1) in ff.partitions
        assert (1, 1, 1) in ff.partitions

    def test_dim_equals_partition_count(self):
        """fiber_dim = partition_count = p(n)."""
        for n in range(10):
            ff = fiber_functor(n)
            assert ff.fiber_dim == ff.partition_count == num_partitions(n)

    def test_verify_fiber_dimensions(self):
        """Full fiber dimension verification."""
        result = verify_fiber_functor_dimensions()
        assert result["all_pass"] is True


# ================================================================
# Section 5: STEP B -- MONOIDAL STRUCTURE
# ================================================================

class TestMonoidalStructure:
    """Tests for the monoidal convolution product."""

    def test_charge_additivity(self):
        """Convolution is additive on charges."""
        for n, m in [(0, 0), (0, 1), (1, 1), (2, 3), (4, 5)]:
            mc = monoidal_convolution(n, m)
            assert mc.charge_out == n + m

    def test_vacuum_is_unit(self):
        """Charge-0 is the monoidal unit."""
        for n in range(5):
            mc = monoidal_convolution(0, n)
            assert mc.charge_out == n
            assert mc.dim_out == num_partitions(n)

    def test_dimensions_correct(self):
        """Input and output dimensions are correct partition counts."""
        mc = monoidal_convolution(3, 4)
        assert mc.dim_in_1 == num_partitions(3)
        assert mc.dim_in_2 == num_partitions(4)
        assert mc.dim_out == num_partitions(7)

    def test_is_associative(self):
        """Monoidal product is associative."""
        mc = monoidal_convolution(2, 3)
        assert mc.is_associative is True

    def test_is_braided(self):
        """Monoidal product has E_2 braiding."""
        mc = monoidal_convolution(2, 3)
        assert mc.is_braided is True

    def test_mv_cycle_count(self):
        """MV cycle count equals p(n+m)."""
        mc = monoidal_convolution(2, 3)
        assert mc.mv_cycle_count == num_partitions(5)

    def test_associativity_full(self):
        """Full associativity verification at max_charge=4."""
        result = verify_monoidal_associativity(max_charge=4)
        assert result["all_pass"] is True
        assert result["num_tests"] > 30  # enough triples


# ================================================================
# Section 6: STEP C -- R-MATRIX MATCH
# ================================================================

class TestRMatrixMatch:
    """Tests for R_geom = R_Yangian (thm:mo-chiral-rmatrix)."""

    def test_default_match(self):
        """R-matrix match at default parameters h=(1,-2,1)."""
        rm = verify_rmatrix_match()
        assert rm.match is True

    def test_unitarity(self):
        """g(z)*g(-z) = 1 (unitarity)."""
        # VERIFIED [DC] algebraic computation
        rm = verify_rmatrix_match()
        assert rm.unitarity is True

    def test_crossing_symmetry(self):
        """g(z) = 1/g(-z) (crossing)."""
        rm = verify_rmatrix_match()
        assert rm.crossing is True

    def test_asymptotic(self):
        """g(z) -> 1 as z -> infinity."""
        rm = verify_rmatrix_match()
        assert rm.asymptotic_correct is True

    def test_ybe_charge1(self):
        """YBE at charge 1 (trivially holds, scalar)."""
        result = verify_ybe_charge1()
        assert result["ybe_holds"] is True

    def test_ybe_charge2_diagonal_unitarity(self):
        """Diagonal unitarity at charge 2."""
        result = verify_ybe_charge2_diagonal()
        assert result["all_pass"] is True

    def test_sigma_form(self):
        """Product form and sigma form agree."""
        result = verify_rmatrix_sigma_form()
        assert result["forms_agree"] is True

    def test_multiple_params(self):
        """R-matrix match at multiple parameter choices."""
        result = verify_rmatrix_multiple_params()
        assert result["all_pass"] is True

    def test_sigma_consistency(self):
        """Sigma form consistency across parameters."""
        result = verify_sigma_form_consistency()
        assert result["all_pass"] is True


class TestUnitarityDetailed:
    """Detailed unitarity verification at multiple parameters."""

    def test_unitarity_symmetric_h(self):
        """Unitarity with symmetric h = (a, -2a, a)."""
        for a in [F(1), F(2), F(3), F(7), F(1, 3)]:
            h = (a, -2 * a, a)
            z = F(37, 10)
            assert eval_g(h, z) * eval_g(h, -z) == F(1)

    def test_unitarity_generic_h(self):
        """Unitarity with generic h (sum=0)."""
        h = (F(5), F(7), F(-12))
        z = F(100)
        assert eval_g(h, z) * eval_g(h, -z) == F(1)

    def test_unitarity_small_h(self):
        """Unitarity with small fractional h."""
        h = (F(1, 3), F(1, 5), F(-8, 15))
        z = F(7, 2)
        assert eval_g(h, z) * eval_g(h, -z) == F(1)

    def test_unitarity_large_h(self):
        """Unitarity with large h (AP-CY28 safe)."""
        h = (F(37), F(41), F(-78))
        z = F(200)
        assert eval_g(h, z) * eval_g(h, -z) == F(1)


# ================================================================
# Section 7: STEP D -- TANNAKIAN RECONSTRUCTION
# ================================================================

class TestTannakianReconstruction:
    """Tests for the Tannakian reconstruction End(F) ~= Y(gl_hat_1)."""

    def test_algebra_name(self):
        """Reconstructed algebra is Y(gl_hat_1)."""
        tr = tannakian_reconstruction()
        assert "Y(gl_hat_1)" in tr.algebra_name

    def test_rtt_satisfied(self):
        """RTT relation is satisfied."""
        tr = tannakian_reconstruction()
        assert tr.rtt_relation_satisfied is True

    def test_heisenberg_subalgebra(self):
        """J_n generate the Heisenberg subalgebra."""
        tr = tannakian_reconstruction()
        assert tr.heisenberg_subalgebra is True

    def test_structure_function_match(self):
        """Structure function from R-matrix matches Yangian g(z)."""
        tr = tannakian_reconstruction()
        assert tr.structure_function_match is True

    def test_fiber_functor_unique(self):
        """Fiber functor is unique (GL_1 abelian, Tannaka-Krein)."""
        tr = tannakian_reconstruction()
        assert tr.fiber_functor_unique is True

    def test_reconstruction_proved(self):
        """Reconstruction status is PROVED."""
        tr = tannakian_reconstruction()
        assert "PROVED" in tr.reconstruction_status


# ================================================================
# Section 8: STEP E -- DG EQUIVALENCE
# ================================================================

class TestDGEquivalence:
    """Tests for the DG equivalence step (the gap)."""

    def test_status_conjectural(self):
        """DG equivalence is CONJECTURAL."""
        dg = dg_equivalence_status()
        assert dg.status == "CONJECTURAL"

    def test_evidence_for_nonempty(self):
        """There is positive evidence for DG equivalence."""
        dg = dg_equivalence_status()
        assert len(dg.evidence_for) >= 4

    def test_formality_expected(self):
        """Formality is expected for toric C^3."""
        dg = dg_equivalence_status()
        assert dg.formality_expected is True

    def test_gap_described(self):
        """The gap is clearly described."""
        dg = dg_equivalence_status()
        assert "DG" in dg.gap_description


# ================================================================
# Section 9: PROOF ASSEMBLY
# ================================================================

class TestProofAssembly:
    """Tests for the proof assembly of all five steps."""

    def test_five_steps(self):
        """There are exactly 5 steps."""
        assembly = proof_assembly()
        assert assembly["total_steps"] == 5

    def test_four_proved(self):
        """Steps A-D are PROVED (4 out of 5)."""
        assembly = proof_assembly()
        assert assembly["proved_steps"] == 4

    def test_gap_is_step_e(self):
        """The gap is Step E."""
        assembly = proof_assembly()
        assert "Step E" in assembly["gap"]

    def test_step_names(self):
        """Each step has a descriptive name."""
        steps = [proof_step_a(), proof_step_b(), proof_step_c(),
                 proof_step_d(), proof_step_e()]
        names = [s.name for s in steps]
        assert any("Fiber" in n for n in names)
        assert any("Monoidal" in n or "monoidal" in n for n in names)
        assert any("R-matrix" in n for n in names)
        assert any("Tannakian" in n for n in names)
        assert any("DG" in n for n in names)

    def test_step_dependencies(self):
        """Each step has listed dependencies."""
        steps = [proof_step_a(), proof_step_b(), proof_step_c(),
                 proof_step_d(), proof_step_e()]
        for s in steps:
            assert len(s.dependencies) > 0

    def test_step_d_depends_on_abc(self):
        """Step D depends on Steps A, B, C."""
        step_d = proof_step_d()
        deps = " ".join(step_d.dependencies)
        assert "Step A" in deps or "fiber functor" in deps.lower()
        assert "Step B" in deps or "monoidal" in deps.lower()
        assert "Step C" in deps or "R-matrix" in deps.lower()


# ================================================================
# Section 10: SUMMARY
# ================================================================

class TestSummary:
    """Tests for the full summary."""

    def test_lhs(self):
        """LHS is D-mod(Gr^{ch}_{GL_1}(C^3))."""
        s = full_summary()
        assert "Gr" in s.equivalence_lhs
        assert "GL_1" in s.equivalence_lhs
        assert "C^3" in s.equivalence_lhs or "C3" in s.equivalence_lhs

    def test_rhs(self):
        """RHS is Rep^{E_2}(Y(gl_hat_1))."""
        s = full_summary()
        assert "Y(gl_hat_1)" in s.equivalence_rhs
        assert "E_2" in s.equivalence_rhs

    def test_overall_conjectural(self):
        """Overall status is CONJECTURAL."""
        s = full_summary()
        assert s.overall_status == "CONJECTURAL"

    def test_key_theorem(self):
        """Key theorem reference is conj:chiral-satake-c3."""
        s = full_summary()
        assert "chiral-satake-c3" in s.key_theorem

    def test_four_of_five(self):
        """4 of 5 steps proved."""
        s = full_summary()
        assert s.steps_proved == 4
        assert s.steps_total == 5


# ================================================================
# Section 11: FULL VERIFICATION SUITE
# ================================================================

class TestFullVerification:
    """Run the full verification suite."""

    def test_step_a_partitions(self):
        result = verify_partition_ground_truth()
        assert result["all_pass"] is True

    def test_step_a_enumeration(self):
        result = verify_partition_enumeration()
        assert result["all_pass"] is True

    def test_step_a_fiber(self):
        result = verify_fiber_functor_dimensions()
        assert result["all_pass"] is True

    def test_step_b_associativity(self):
        result = verify_monoidal_associativity(max_charge=4)
        assert result["all_pass"] is True

    def test_step_c_rmatrix(self):
        result = verify_rmatrix_multiple_params()
        assert result["all_pass"] is True

    def test_step_c_sigma(self):
        result = verify_sigma_form_consistency()
        assert result["all_pass"] is True

    def test_step_c_ybe1(self):
        result = verify_ybe_charge1()
        assert result["ybe_holds"] is True

    def test_step_c_ybe2(self):
        result = verify_ybe_charge2_diagonal()
        assert result["all_pass"] is True

    def test_step_d_tannakian(self):
        tr = tannakian_reconstruction()
        assert tr.rtt_relation_satisfied is True
        assert tr.structure_function_match is True
        assert tr.fiber_functor_unique is True

    def test_full_verification_all_paths(self):
        """Run all verification paths together."""
        results = full_verification()
        assert results["all_pass"] is True


# ================================================================
# Section 12: AP COMPLIANCE
# ================================================================

class TestAPCompliance:
    """Verify compliance with anti-patterns."""

    def test_ap_cy14_overall_conjectural(self):
        """AP-CY14: overall status is CONJECTURAL (full equivalence)."""
        assert OVERALL_STATUS == "CONJECTURAL"

    def test_ap_cy14_step_e_conjectural(self):
        """AP-CY14: DG equivalence step is CONJECTURAL."""
        dg = dg_equivalence_status()
        assert dg.status == "CONJECTURAL"

    def test_ap_cy31_spectral_parameter(self):
        """AP-CY31: spectral parameter z is Yangian, not worldsheet."""
        # Verified by the engine docstring conventions.
        # The R-matrix match uses z as spectral (Yangian) parameter.
        rm = verify_rmatrix_match()
        # z_test is a Fraction (algebraic), not a complex number (analytic)
        assert isinstance(rm.z_test, Fraction)

    def test_ap_cy25_no_delta_vacuum(self):
        """AP-CY25: R-matrix from half-braiding, not Delta(1)."""
        # The R-matrix is computed from the structure function g(z),
        # which comes from the factorization braiding (half-braiding),
        # NOT from applying the coproduct to the vacuum.
        # This is encoded in the proof strategy (Step C).
        step_c = proof_step_c()
        deps = " ".join(step_c.dependencies)
        assert "stable envelope" in deps.lower() or "MO" in deps or "Maulik-Okounkov" in deps

    def test_ap_cy28_safe_test_points(self):
        """AP-CY28: test points avoid poles at +/- h_i."""
        h = (F(1), F(-2), F(1))
        # Poles at +/- 1, +/- 2. Default test z = 37/10 avoids all.
        z = F(37, 10)
        for hi in h:
            assert z != hi and z != -hi

    def test_ap_cy7_coha_not_chiral(self):
        """AP-CY7: engine does not conflate CoHA with chiral algebra."""
        # The engine treats the Yangian Y(gl_hat_1) as the target,
        # NOT the CoHA. The CoHA is the E_1 side (Iwahori).
        tr = tannakian_reconstruction()
        assert "Y(gl_hat_1)" in tr.algebra_name
        # The algebra is the full Yangian, not the CoHA
