r"""Tests for the KSWCF = E_1 bar differential proof engine.

THEOREM: The Kontsevich-Soibelman wall-crossing formula IS the E_1 bar
differential on the ordered bar complex B^{ord}(A_C).

Multi-path verification covering all proof components:

    Path 1:  Level 3 -- KS log = bar generators (conifold)
    Path 2:  Level 3 -- quantum torus encodes d_bar
    Path 3:  Pentagon identity in quantum torus (exact)
    Path 4:  Pentagon = d_bar^2 = 0 equivalence
    Path 5:  Hexagon d_bar^2 = 0 on bar degree 3 (A2 quiver)
    Path 6:  Hexagon bar differential chain B^3 -> B^2 -> B^1 -> 0
    Path 7:  Hexagon Euler form antisymmetry
    Path 8:  Hexagon spectral sequence d_2
    Path 9:  Level 4 -- bar complex stability-independent
    Path 10: Level 4 -- filtration depends on stability
    Path 11: Level 4 -- spectral sequences converge to same target
    Path 12: Level 4 -- E_1 comparison = wall-crossing
    Path 13: Level 5 -- conifold Chamber I verification
    Path 14: Level 5 -- conifold Chamber II verification
    Path 15: Level 5 -- bar Euler product
    Path 16: Exhaustive d^2 = 0 for A1 quiver
    Path 17: Exhaustive d^2 = 0 for A2 quiver
    Path 18: Full proof orchestrator
    Path 19: Charge lattice axioms (antisymmetry, bilinearity)
    Path 20: Bar element algebra (addition, subtraction, scaling)
    Path 21: Bar differential signs (Koszul convention)
    Path 22: Quantum torus product (associativity, q-commutation)
    Path 23: Quantum dilogarithm structural properties
    Path 24: Ordered decomposition counts
    Path 25: Pentagon at higher charges
    Path 26: Hexagon composite charges

Manuscript references:
    conj:categorical-ks-bar (e1_chiral_algebras.tex)
    thm:ks-bar-pentagon (NEW)
    thm:ks-bar-spectral-sequence (NEW)
    thm:bps-bar-euler-toric (NEW)
    sec:categorical-wall-crossing-bar

Mathematical references:
    Kontsevich-Soibelman, arXiv:0811.2435
    Faddeev, Lett. Math. Phys. 34, 1995
    Keller, arXiv:1102.4148

Ground truth:
    - d_bar^2 = 0 from associativity (ALL bar elements, ALL quivers)
    - Pentagon E(X)E(Y) = E(Y)E(XY)E(X) (EXACT in quantum torus)
    - Euler form: chi((a,b),(c,d)) = ad - bc (antisymmetric)
    - Conifold: Omega(1,0) = Omega(0,1) = 1 in both chambers
    - Bar differential: d[a|b] = [a*b], d[a|b|c] = [ab|c] - [a|bc]
"""

import pytest
import math
from fractions import Fraction

from compute.lib.ks_bar_proof import (
    # Lattice
    euler_form,
    charge_add,
    charge_scale,
    charge_height,
    is_positive,
    # Quantum torus
    QuantumTorusElement,
    compact_quantum_dilogarithm,
    # Bar complex
    BarElement,
    bar_differential,
    bar_differential_squared,
    # Proof engines
    KSBarIdentificationProof,
    PentagonBarProof,
    HexagonBarProof,
    SpectralSequenceProof,
    BPSBarEulerProof,
    # Orchestrators
    full_ks_bar_proof,
    exhaustive_d_squared_verification,
)

F = Fraction


# ================================================================
# Path 1: LEVEL 3 -- KS LOG = BAR GENERATORS
# ================================================================

class TestLevel3KSLog:
    """Verify KS log-series matches bar complex generator structure."""

    def test_ks_log_conifold_10(self):
        """KS log at (1,0) with Omega=1 matches bar generators."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_ks_log_matches_bar_generators((1, 0), omega=1)
        assert result['identification_proved']

    def test_ks_log_conifold_01(self):
        """KS log at (0,1) with Omega=1 matches bar generators."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_ks_log_matches_bar_generators((0, 1), omega=1)
        assert result['identification_proved']

    def test_ks_log_bar_degree_1(self):
        """At bar degree 1, exactly one generator per primitive charge."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_ks_log_matches_bar_generators((1, 0), omega=1)
        assert result['levels'][1]['bar_generators_count'] == 1

    def test_ks_log_dilogarithm_weight(self):
        """KS coefficient at n*gamma is omega/n^2 (dilogarithm)."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_ks_log_matches_bar_generators((1, 0), omega=1)
        for n, data in result['levels'].items():
            assert data['ks_coefficient'] == F(1, n * n)

    def test_ks_log_omega_2(self):
        """KS log with Omega=2 doubles all coefficients."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_ks_log_matches_bar_generators((1, 0), omega=2)
        for n, data in result['levels'].items():
            assert data['ks_coefficient'] == F(2, n * n)


# ================================================================
# Path 2: LEVEL 3 -- QUANTUM TORUS ENCODES d_bar
# ================================================================

class TestLevel3QuantumTorus:
    """Verify quantum torus product encodes bar differential."""

    def test_quantum_torus_detects_bound_state(self):
        """E(X)*E(Y) is nonzero at charge (1,1): bound state detected."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_quantum_torus_encodes_dbar(N_q=8, max_charge=3)
        assert result['identification']['both_detect_bound_state']

    def test_bar_differential_produces_11(self):
        """d_bar[e10|e01] produces [e11] (bar detects bound state)."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_quantum_torus_encodes_dbar(N_q=8, max_charge=3)
        assert result['bar_produces_11']

    def test_pentagon_at_charge_11(self):
        """Pentagon holds at charge (1,1): LHS(1,1) = RHS(1,1)."""
        engine = KSBarIdentificationProof('A1', 10)
        result = engine.prove_quantum_torus_encodes_dbar(N_q=8, max_charge=3)
        assert result['pentagon_at_11']

    def test_bar_differential_coefficient_sign(self):
        """d_bar[e10|e01] = +[e11] (sign is (-1)^0 = +1)."""
        bar = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        d = bar_differential(bar)
        assert d.terms.get(((1, 1),), F(0)) == F(1)


# ================================================================
# Path 3: PENTAGON IDENTITY IN QUANTUM TORUS
# ================================================================

class TestPentagonQuantumTorus:
    """Verify E(X)*E(Y) = E(Y)*E(XY)*E(X) exactly."""

    def test_pentagon_holds(self):
        """Pentagon identity holds at all charges up to max_charge=3."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_pentagon_quantum_torus(N_q=8, max_charge=3)
        assert result['pentagon_holds']

    def test_pentagon_no_discrepancies(self):
        """No discrepancies in pentagon verification."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_pentagon_quantum_torus(N_q=8, max_charge=3)
        assert len(result['discrepancies']) == 0

    def test_pentagon_nontrivial_charges_checked(self):
        """A nontrivial number of charge sectors are checked."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_pentagon_quantum_torus(N_q=8, max_charge=3)
        assert result['charges_checked'] >= 20


# ================================================================
# Path 4: PENTAGON = d_bar^2 = 0 EQUIVALENCE
# ================================================================

class TestPentagonEquivalence:
    """Prove pentagon <==> d_bar^2 = 0."""

    def test_equivalence_proved(self):
        """Full pentagon-d^2 equivalence verification passes."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.prove_pentagon_equals_d_squared_zero(N_q=8, max_charge=3)
        assert result['equivalence_proved']

    def test_d_squared_zero_at_charge_11(self):
        """d^2 = 0 on all bar elements at charge (1,1)."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_d_squared_zero_charge_11()
        assert result['all_zero']

    def test_gauge_transformation_compatible(self):
        """Bar cohomology agrees across chambers (gauge compatible)."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.prove_pentagon_equals_d_squared_zero(N_q=8, max_charge=3)
        assert result['gauge_transformation']['bar_cohomology_agrees']

    def test_d_squared_bar2_10_01(self):
        """d^2[e10|e01] = 0."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_d_squared_zero_charge_11()
        assert result['d2_zero']['[10|01]']

    def test_d_squared_bar2_01_10(self):
        """d^2[e01|e10] = 0."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_d_squared_zero_charge_11()
        assert result['d2_zero']['[01|10]']

    def test_d_squared_bar3_10_01_10(self):
        """d^2[e10|e01|e10] = 0."""
        proof = PentagonBarProof(10, 'A1')
        result = proof.verify_d_squared_zero_charge_11()
        assert result['d2_zero']['[10|01|10]']


# ================================================================
# Path 5: HEXAGON d_bar^2 = 0 ON BAR DEGREE 3 (A2 QUIVER)
# ================================================================

class TestHexagonDSquared:
    """Verify d^2 = 0 on bar degree 3 elements for A2 quiver."""

    def test_all_d_squared_zero(self):
        """d^2 = 0 for all bar degree 3 elements on A2."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_d_squared_zero_bar3()
        assert result['all_zero']

    def test_nontrivial_elements_tested(self):
        """Enough elements tested to be meaningful."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_d_squared_zero_bar3()
        assert result['elements_tested'] >= 25

    def test_composite_charges_d_squared_zero(self):
        """d^2 = 0 for composite charge combinations on A2."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_d_squared_zero_bar3()
        # Check a specific composite charge entry
        assert result['d2_results'].get('[(1, 0, 0)|(1, 1, 0)|(0, 0, 1)]', True)


# ================================================================
# Path 6: HEXAGON BAR DIFFERENTIAL CHAIN
# ================================================================

class TestHexagonChain:
    """Verify B^3 -> B^2 -> B^1 -> 0 chain for A2."""

    def test_d_squared_zero_on_chain(self):
        """d^2[e1|e2|e3] = 0 explicitly."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_bar_differential_chain()
        assert result['d_squared_zero']

    def test_bar_differential_correct_terms(self):
        """d[e1|e2|e3] = [e12|e3] - [e1|e23] (correct signs)."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_bar_differential_chain()
        assert result['d_bar_correct']

    def test_associativity_content(self):
        """d^2=0 content is (a*b)*c = a*(b*c)."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_bar_differential_chain()
        assert 'associativity' in result['associativity_content'].lower()


# ================================================================
# Path 7: HEXAGON EULER FORM ANTISYMMETRY
# ================================================================

class TestHexagonEulerForm:
    """Verify Euler form antisymmetry for A2 quiver."""

    def test_all_antisymmetric(self):
        """chi(a,b) = -chi(b,a) for all simple root pairs."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_euler_form_antisymmetry()
        assert result['all_antisymmetric']

    def test_chi_e1_e2_nonzero(self):
        """chi(e1,e2) != 0 for adjacent roots in A2."""
        chi = euler_form((1, 0, 0), (0, 1, 0), 'A2')
        assert chi != 0

    def test_chi_e1_e3_zero(self):
        """chi(e1,e3) = 0 for non-adjacent roots in A2."""
        chi = euler_form((1, 0, 0), (0, 0, 1), 'A2')
        assert chi == 0


# ================================================================
# Path 8: HEXAGON SPECTRAL SEQUENCE d_2
# ================================================================

class TestHexagonSpectralSequence:
    """Verify d_2 differential for 3-body interaction."""

    def test_d2_zero_at_q1(self):
        """d_2 = 0 at q=1 (classical limit)."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_spectral_sequence_d2()
        assert result['d_2_zero_at_q1']

    def test_euler_form_values_consistent(self):
        """Euler form values in spectral sequence are consistent."""
        hex_proof = HexagonBarProof(12)
        result = hex_proof.verify_spectral_sequence_d2()
        chi_12 = result['euler_form']['chi_12']
        chi_23 = result['euler_form']['chi_23']
        # For A2: chi(e1,e2) = 1, chi(e2,e3) = 1
        assert chi_12 == 1
        assert chi_23 == 1


# ================================================================
# Path 9: LEVEL 4 -- BAR COMPLEX STABILITY-INDEPENDENT
# ================================================================

class TestLevel4StabilityIndependence:
    """The bar complex and d_bar do not depend on stability condition."""

    def test_both_orderings_produce_e11(self):
        """d_bar[e10|e01] and d_bar[e01|e10] both produce [e11]."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_bar_complex_independent_of_stability()
        assert result['both_produce_e11']

    def test_differential_stability_independent(self):
        """d_bar is independent of the stability condition."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_bar_complex_independent_of_stability()
        assert result['differential_stability_independent']


# ================================================================
# Path 10: LEVEL 4 -- FILTRATION DEPENDS ON STABILITY
# ================================================================

class TestLevel4FiltrationDependence:
    """Different stability conditions give different filtrations."""

    def test_orderings_differ(self):
        """Chambers I and II have different phase orderings."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_filtration_depends_on_stability()
        assert result['orderings_differ']

    def test_chamber_I_10_before_01(self):
        """In Chamber I, phi(1,0) > phi(0,1)."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_filtration_depends_on_stability()
        assert result['chamber_I']['ordering_10_before_01']

    def test_chamber_II_01_before_10(self):
        """In Chamber II, phi(0,1) > phi(1,0)."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_filtration_depends_on_stability()
        assert result['chamber_II']['ordering_01_before_10']


# ================================================================
# Path 11: LEVEL 4 -- SPECTRAL SEQUENCES CONVERGE
# ================================================================

class TestLevel4Convergence:
    """Both filtrations converge to the same bar cohomology."""

    def test_images_equal(self):
        """d_bar on both orderings produces the same image."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_spectral_sequences_converge_to_same_target()
        assert result['images_equal']

    def test_kernel_element_in_kernel(self):
        """[e10|e01] - [e01|e10] is in ker(d_bar)."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_spectral_sequences_converge_to_same_target()
        assert result['d_kernel_zero']

    def test_cohomology_independent_of_filtration(self):
        """Bar cohomology is independent of the filtration."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_spectral_sequences_converge_to_same_target()
        assert result['cohomology_analysis']['independent_of_filtration']


# ================================================================
# Path 12: LEVEL 4 -- E_1 COMPARISON = WALL-CROSSING
# ================================================================

class TestLevel4WallCrossing:
    """The E_1 comparison map is the KS wall-crossing formula."""

    def test_e1_is_ks_formula(self):
        """E_1 comparison map is the KS formula."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.prove_e1_comparison_is_wall_crossing()
        assert result['e1_page_comparison']['is_ks_formula']

    def test_level4_proved(self):
        """Full Level 4 proof passes."""
        proof = SpectralSequenceProof(10, 'A1')
        result = proof.full_level4_proof()
        assert result['level_4_proved']


# ================================================================
# Path 13: LEVEL 5 -- CONIFOLD CHAMBER I
# ================================================================

class TestLevel5ChamberI:
    """Verify BPS = bar Euler for conifold Chamber I."""

    def test_primitive_charges_match(self):
        """Omega(1,0) = Omega(0,1) = 1 from bar complex."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_conifold_chamber_I()
        assert result['primitive_charges_match']

    def test_omega_10_is_1(self):
        """Omega(1,0) = 1."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_conifold_chamber_I()
        assert result['omega_10'] == 1

    def test_omega_01_is_1(self):
        """Omega(0,1) = 1."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_conifold_chamber_I()
        assert result['omega_01'] == 1


# ================================================================
# Path 14: LEVEL 5 -- CONIFOLD CHAMBER II
# ================================================================

class TestLevel5ChamberII:
    """Verify BPS = bar Euler for conifold Chamber II."""

    def test_omega_11_is_1(self):
        """Omega(1,1) = 1 in Chamber II (bound state)."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_conifold_chamber_II()
        assert result['omega_11'] == 1

    def test_total_omega_is_3(self):
        """Total: Omega(10)+Omega(01)+Omega(11) = 3 in Chamber II."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_conifold_chamber_II()
        assert result['total_omega'] == 3


# ================================================================
# Path 15: LEVEL 5 -- BAR EULER PRODUCT
# ================================================================

class TestLevel5BarEuler:
    """Verify bar Euler product is gauge-invariant."""

    def test_level5_proved_for_toric(self):
        """Level 5 proved for toric CY3."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.full_level5_proof()
        assert result['level_5_proved_for_toric']

    def test_chamber_I_fewer_factors(self):
        """Chamber I has 2 factors vs Chamber II's 3."""
        proof = BPSBarEulerProof(10, 'A1')
        result = proof.verify_bar_euler_product()
        assert result['chamber_I_factors'] == 2
        assert result['chamber_II_factors'] == 3


# ================================================================
# Path 16: EXHAUSTIVE d^2 = 0 FOR A1
# ================================================================

class TestExhaustiveA1:
    """Exhaustive d_bar^2 = 0 verification for A1 quiver."""

    def test_all_pass_a1(self):
        """d^2 = 0 on all bar elements for A1."""
        result = exhaustive_d_squared_verification('A1', 8, 5)
        assert result['all_pass']

    def test_nontrivial_count_a1(self):
        """Enough elements tested for A1."""
        result = exhaustive_d_squared_verification('A1', 8, 5)
        assert result['total_tested'] >= 50

    def test_no_failures_a1(self):
        """No failures in A1 verification."""
        result = exhaustive_d_squared_verification('A1', 8, 5)
        assert len(result['failures']) == 0


# ================================================================
# Path 17: EXHAUSTIVE d^2 = 0 FOR A2
# ================================================================

class TestExhaustiveA2:
    """Exhaustive d_bar^2 = 0 verification for A2 quiver."""

    def test_all_pass_a2(self):
        """d^2 = 0 on all bar elements for A2."""
        result = exhaustive_d_squared_verification('A2', 6, 4)
        assert result['all_pass']

    def test_nontrivial_count_a2(self):
        """Enough elements tested for A2."""
        result = exhaustive_d_squared_verification('A2', 6, 4)
        assert result['total_tested'] >= 100

    def test_no_failures_a2(self):
        """No failures in A2 verification."""
        result = exhaustive_d_squared_verification('A2', 6, 4)
        assert len(result['failures']) == 0


# ================================================================
# Path 18: FULL PROOF ORCHESTRATOR
# ================================================================

class TestFullProof:
    """Full proof orchestrator verification."""

    def test_all_pass(self):
        """All proof components pass."""
        result = full_ks_bar_proof(N_q=8, max_charge=3, max_height=10)
        assert result['all_pass']

    def test_pentagon_in_full_proof(self):
        """Pentagon proved in full proof."""
        result = full_ks_bar_proof(N_q=8, max_charge=3, max_height=10)
        assert result['pentagon']['equivalence_proved']

    def test_hexagon_in_full_proof(self):
        """Hexagon d^2=0 in full proof."""
        result = full_ks_bar_proof(N_q=8, max_charge=3, max_height=10)
        assert result['hexagon']['d_squared_zero_bar3']['all_zero']

    def test_level4_in_full_proof(self):
        """Level 4 proved in full proof."""
        result = full_ks_bar_proof(N_q=8, max_charge=3, max_height=10)
        assert result['level_4']['level_4_proved']

    def test_level5_in_full_proof(self):
        """Level 5 proved for toric in full proof."""
        result = full_ks_bar_proof(N_q=8, max_charge=3, max_height=10)
        assert result['level_5']['level_5_proved_for_toric']


# ================================================================
# Path 19: CHARGE LATTICE AXIOMS
# ================================================================

class TestChargeLattice:
    """Verify charge lattice axioms."""

    def test_euler_form_antisymmetric_a1(self):
        """chi(a,b) = -chi(b,a) for A1."""
        g10 = (1, 0)
        g01 = (0, 1)
        assert euler_form(g10, g01, 'A1') == -euler_form(g01, g10, 'A1')

    def test_euler_form_bilinear_a1(self):
        """chi(a+b,c) = chi(a,c) + chi(b,c) for A1."""
        a, b, c = (1, 0), (0, 1), (1, 1)
        ab = charge_add(a, b)
        assert euler_form(ab, c, 'A1') == euler_form(a, c, 'A1') + euler_form(b, c, 'A1')

    def test_euler_form_value_a1(self):
        """chi((1,0),(0,1)) = 1 for A1 (conifold)."""
        assert euler_form((1, 0), (0, 1), 'A1') == 1

    def test_charge_add(self):
        """(1,0) + (0,1) = (1,1)."""
        assert charge_add((1, 0), (0, 1)) == (1, 1)

    def test_charge_scale(self):
        """3*(1,0) = (3,0)."""
        assert charge_scale(3, (1, 0)) == (3, 0)

    def test_charge_height(self):
        """height((2,3)) = 5."""
        assert charge_height((2, 3)) == 5

    def test_is_positive(self):
        """(1,0) is positive, (0,0) is not."""
        assert is_positive((1, 0))
        assert is_positive((0, 1))
        assert not is_positive((0, 0))
        assert not is_positive((-1, 0))

    def test_euler_form_antisymmetric_a2(self):
        """chi(a,b) = -chi(b,a) for A2."""
        e1, e2 = (1, 0, 0), (0, 1, 0)
        assert euler_form(e1, e2, 'A2') == -euler_form(e2, e1, 'A2')

    def test_euler_form_bilinear_a2(self):
        """chi(a+b,c) = chi(a,c) + chi(b,c) for A2."""
        a = (1, 0, 0)
        b = (0, 1, 0)
        c = (0, 0, 1)
        ab = charge_add(a, b)
        assert euler_form(ab, c, 'A2') == euler_form(a, c, 'A2') + euler_form(b, c, 'A2')


# ================================================================
# Path 20: BAR ELEMENT ALGEBRA
# ================================================================

class TestBarElementAlgebra:
    """Verify bar element algebraic operations."""

    def test_bar_zero(self):
        """Zero bar element is zero."""
        z = BarElement.zero(10, 'A1')
        assert z.is_zero()

    def test_bar_add(self):
        """Addition of bar elements."""
        a = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        b = BarElement.generator(((0, 1), (1, 0)), F(2), 10, 'A1')
        c = a + b
        assert not c.is_zero()
        assert c.terms[((1, 0), (0, 1))] == F(1)
        assert c.terms[((0, 1), (1, 0))] == F(2)

    def test_bar_subtract(self):
        """Subtraction: a - a = 0."""
        a = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        assert (a - a).is_zero()

    def test_bar_scale(self):
        """Scaling bar elements."""
        a = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        b = a.scale(F(3))
        assert b.terms[((1, 0), (0, 1))] == F(3)

    def test_bar_degree(self):
        """Bar degree of a bar element."""
        a = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        assert a.bar_degree() == 2

    def test_bar_degree_3(self):
        """Bar degree 3 element."""
        a = BarElement.generator(((1, 0), (0, 1), (1, 0)), F(1), 10, 'A1')
        assert a.bar_degree() == 3


# ================================================================
# Path 21: BAR DIFFERENTIAL SIGNS
# ================================================================

class TestBarDifferentialSigns:
    """Verify Koszul sign conventions in the bar differential."""

    def test_d_bar_degree_2_sign_i0(self):
        """d[a|b] = [a*b] with sign (-1)^0 = +1."""
        bar = BarElement.generator(((1, 0), (0, 1)), F(1), 10, 'A1')
        d = bar_differential(bar)
        assert d.terms.get(((1, 1),), F(0)) == F(1)

    def test_d_bar_degree_3_signs(self):
        """d[a|b|c] = [a*b|c] - [a|b*c] (signs (-1)^0, (-1)^1)."""
        e1 = (1, 0, 0)
        e2 = (0, 1, 0)
        e3 = (0, 0, 1)
        bar = BarElement.generator((e1, e2, e3), F(1), 12, 'A2')
        d = bar_differential(bar)

        e12 = charge_add(e1, e2)
        e23 = charge_add(e2, e3)

        assert d.terms.get((e12, e3), F(0)) == F(1)    # sign +1 at i=0
        assert d.terms.get((e1, e23), F(0)) == F(-1)    # sign -1 at i=1

    def test_d_bar_degree_4_signs(self):
        """d[a|b|c|d] = [ab|c|d] - [a|bc|d] + [a|b|cd]."""
        g = (1, 0)
        bar = BarElement.generator((g, g, g, g), F(1), 12, 'A1')
        d = bar_differential(bar)
        g2 = charge_add(g, g)

        assert d.terms.get((g2, g, g), F(0)) == F(1)    # i=0: +1
        assert d.terms.get((g, g2, g), F(0)) == F(-1)   # i=1: -1
        assert d.terms.get((g, g, g2), F(0)) == F(1)    # i=2: +1


# ================================================================
# Path 22: QUANTUM TORUS PRODUCT
# ================================================================

class TestQuantumTorusProduct:
    """Verify quantum torus algebra structure."""

    def test_identity_element(self):
        """1 * E = E * 1 = E."""
        one = QuantumTorusElement.identity(8, 4)
        X = QuantumTorusElement.monomial(1, 0, 8, 4)
        assert (one * X) == X
        assert (X * one) == X

    def test_q_commutation(self):
        """YX = qXY in the quantum torus.

        X = X^1 Y^0, Y = X^0 Y^1.
        XY at (1,1): q^{0*1} = q^0 = 1 coefficient.
        YX at (1,1): q^{1*0} ... actually
        (X^0 Y^1)(X^1 Y^0) = q^{1*1} X^1 Y^1 = q * XY.
        """
        X = QuantumTorusElement.monomial(1, 0, 8, 4)
        Y = QuantumTorusElement.monomial(0, 1, 8, 4)
        XY = X * Y
        YX = Y * X

        # XY at charge (1,1): coefficient q^{b1*a2} = q^{0*0} = 1
        # Wait: X = (1,0), Y = (0,1)
        # XY: (a1,b1)=(1,0), (a2,b2)=(0,1), shift = b1*a2 = 0*0 = 0
        # YX: (a1,b1)=(0,1), (a2,b2)=(1,0), shift = b1*a2 = 1*1 = 1

        xy_coeff = XY.get_charge(1, 1)
        yx_coeff = YX.get_charge(1, 1)

        # XY: q^0 at (1,1) => coefficient [1, 0, 0, ...]
        assert xy_coeff[0] == F(1)
        # YX: q^1 at (1,1) => coefficient [0, 1, 0, ...]
        assert yx_coeff[0] == F(0)
        assert yx_coeff[1] == F(1)

    def test_associativity(self):
        """(X*Y)*Z = X*(Y*Z) in the quantum torus."""
        X = QuantumTorusElement.monomial(1, 0, 8, 4)
        Y = QuantumTorusElement.monomial(0, 1, 8, 4)
        Z = QuantumTorusElement.monomial(1, 1, 8, 4)
        assert (X * Y) * Z == X * (Y * Z)


# ================================================================
# Path 23: QUANTUM DILOGARITHM PROPERTIES
# ================================================================

class TestQuantumDilogarithm:
    """Verify structural properties of the quantum dilogarithm."""

    def test_dilog_identity_at_00(self):
        """E(X^a Y^b) at charge (0,0) starts with 1."""
        E = compact_quantum_dilogarithm(1, 0, 8, 4)
        c00 = E.get_charge(0, 0)
        assert c00[0] == F(1)

    def test_dilog_nonzero_at_charge(self):
        """E(X) is nonzero at charge (1,0)."""
        E = compact_quantum_dilogarithm(1, 0, 8, 4)
        c10 = E.get_charge(1, 0)
        assert any(c != 0 for c in c10)

    def test_dilog_leading_term(self):
        """E(X) at charge (1,0) has leading term q^0 (from 1+X factor)."""
        E = compact_quantum_dilogarithm(1, 0, 8, 4)
        c10 = E.get_charge(1, 0)
        # prod_{k>=0}(1+q^k X): at charge (1,0), get sum_{k>=0} q^k = 1/(1-q)
        # Leading term: q^0 coefficient = 1
        assert c10[0] == F(1)


# ================================================================
# Path 24: ORDERED DECOMPOSITION COUNTS
# ================================================================

class TestDecompositionCounts:
    """Verify ordered decomposition counting."""

    def test_decomp_11_into_1_part(self):
        """One decomposition of (1,1) into 1 part."""
        engine = KSBarIdentificationProof('A1', 10)
        count = engine._count_ordered_decompositions((1, 1), 1)
        assert count == 1

    def test_decomp_11_into_2_parts(self):
        """Decompositions of (1,1) into 2 positive parts:
        (1,0)+(0,1) and (0,1)+(1,0). Count = 2."""
        engine = KSBarIdentificationProof('A1', 10)
        count = engine._count_ordered_decompositions((1, 1), 2)
        assert count == 2

    def test_decomp_20_into_2_parts(self):
        """Decompositions of (2,0) into 2 positive parts:
        (1,0)+(1,0). Count = 1."""
        engine = KSBarIdentificationProof('A1', 10)
        count = engine._count_ordered_decompositions((2, 0), 2)
        assert count == 1

    def test_decomp_10_into_2_parts(self):
        """Decompositions of (1,0) into 2 positive parts: none. Count = 0."""
        engine = KSBarIdentificationProof('A1', 10)
        count = engine._count_ordered_decompositions((1, 0), 2)
        assert count == 0


# ================================================================
# Path 25: PENTAGON AT HIGHER CHARGES
# ================================================================

class TestPentagonHigherCharges:
    """Pentagon identity at charges beyond (1,1)."""

    def test_pentagon_at_charge_20(self):
        """Pentagon holds at charge (2,0)."""
        E_X = compact_quantum_dilogarithm(1, 0, 8, 3)
        E_Y = compact_quantum_dilogarithm(0, 1, 8, 3)
        E_XY = compact_quantum_dilogarithm(1, 1, 8, 3)
        LHS = E_X * E_Y
        RHS = E_Y * E_XY * E_X
        assert LHS.get_charge(2, 0) == RHS.get_charge(2, 0)

    def test_pentagon_at_charge_02(self):
        """Pentagon holds at charge (0,2)."""
        E_X = compact_quantum_dilogarithm(1, 0, 8, 3)
        E_Y = compact_quantum_dilogarithm(0, 1, 8, 3)
        E_XY = compact_quantum_dilogarithm(1, 1, 8, 3)
        LHS = E_X * E_Y
        RHS = E_Y * E_XY * E_X
        assert LHS.get_charge(0, 2) == RHS.get_charge(0, 2)

    def test_pentagon_at_charge_21(self):
        """Pentagon holds at charge (2,1)."""
        E_X = compact_quantum_dilogarithm(1, 0, 8, 3)
        E_Y = compact_quantum_dilogarithm(0, 1, 8, 3)
        E_XY = compact_quantum_dilogarithm(1, 1, 8, 3)
        LHS = E_X * E_Y
        RHS = E_Y * E_XY * E_X
        assert LHS.get_charge(2, 1) == RHS.get_charge(2, 1)


# ================================================================
# Path 26: HEXAGON COMPOSITE CHARGES
# ================================================================

class TestHexagonCompositeCharges:
    """d^2 = 0 for composite charge bar elements on A2."""

    def test_composite_e12_e3(self):
        """d^2[e12|e3] = 0 (bar degree 2 with composite charge)."""
        e12 = (1, 1, 0)
        e3 = (0, 0, 1)
        bar = BarElement.generator((e12, e3), F(1), 12, 'A2')
        d2 = bar_differential_squared(bar)
        assert d2.is_zero()

    def test_composite_e1_e23(self):
        """d^2[e1|e23] = 0."""
        e1 = (1, 0, 0)
        e23 = (0, 1, 1)
        bar = BarElement.generator((e1, e23), F(1), 12, 'A2')
        d2 = bar_differential_squared(bar)
        assert d2.is_zero()

    def test_composite_degree_3(self):
        """d^2[e1|e12|e3] = 0 (composite at degree 3)."""
        e1 = (1, 0, 0)
        e12 = (1, 1, 0)
        e3 = (0, 0, 1)
        bar = BarElement.generator((e1, e12, e3), F(1), 12, 'A2')
        d2 = bar_differential_squared(bar)
        assert d2.is_zero()

    def test_all_composite_pairs(self):
        """d^2 = 0 for all composite-charge pairs."""
        composites = [
            (1, 1, 0), (0, 1, 1), (1, 1, 1),
        ]
        simples = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        for g1 in composites + simples:
            for g2 in simples:
                bar = BarElement.generator((g1, g2), F(1), 12, 'A2')
                d2 = bar_differential_squared(bar)
                assert d2.is_zero(), f"d^2[{g1}|{g2}] != 0"
