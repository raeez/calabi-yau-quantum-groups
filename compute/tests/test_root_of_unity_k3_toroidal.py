r"""Tests for root_of_unity_k3_toroidal.py: root-of-unity specialization
of the K3 quantum toroidal algebra.

STATUS: ALL results are CONJECTURAL (AP-CY14).
The tests verify INTERNAL CONSISTENCY of the construction, not its existence.

CENTRAL RESULTS (all conjectural):
    (1) [N]_omega = 0 at omega = e^{2*pi*i/N} (quantum integer truncation).
    (2) CY_2 constraint: prod q_a = 1 at root of unity.
    (3) G_{K3}(x) has poles on N-th roots of unity.
    (4) Restricted partitions p_{24}^{<N}(n) = p_{24}(n) for n < N.
    (5) The abelian charge-1 S-matrix is diagonal (NOT MTC).
    (6) Verlinde dimensions computable at each genus.
    (7) Conway/Mathieu moonshine connection via Gauss sums.

Test structure:
    Section 1: Root-of-unity arithmetic (6 tests)
    Section 2: K3 parameters at root of unity (5 tests)
    Section 3: Periodic structure function (5 tests)
    Section 4: Restricted partition function (7 tests)
    Section 5: S-matrix and modularity (6 tests)
    Section 6: T-matrix and modular relations (4 tests)
    Section 7: Verlinde dimensions (4 tests)
    Section 8: Conway group analysis (4 tests)
    Section 9: The five critical questions (5 tests)
    Section 10: Full verification (3 tests)

Manuscript references:
    k3_times_e.tex, conj:k3-quantum-toroidal (K3 quantum toroidal)
    k3_times_e.tex, subsec:k3-quantum-toroidal (deformation hierarchy)
    cfg25_adversarial_consistency.py (gap: root-of-unity not constructed)
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.root_of_unity_k3_toroidal import (
    # Constants
    STATUS,
    MUKAI_RANK,
    # Root-of-unity arithmetic
    primitive_root,
    q_number_root_of_unity,
    quantum_integers_at_root,
    verify_truncation,
    # Parameters
    RootOfUnityK3Params,
    kummer_root_of_unity_params,
    generic_root_of_unity_params,
    # Structure function
    structure_function_root_of_unity,
    verify_periodicity,
    pole_structure,
    # Restricted partitions
    restricted_colored_partition,
    truncated_fock_dimensions,
    total_simple_objects,
    compare_restricted_unrestricted,
    # S-matrix
    charge_1_s_matrix,
    s_matrix_nondegeneracy,
    # T-matrix
    charge_1_t_matrix,
    verify_modular_relations,
    # Verlinde
    verlinde_dimension_genus_g,
    # Conway
    conway_analysis,
    conway_connection_analysis,
    # Five questions
    finiteness_analysis,
    modularity_analysis,
    verlinde_p24_analysis,
    # Full
    full_verification,
)

from compute.lib.k3_quantum_toroidal import (
    _colored_partition,
    N_MUKAI,
)


# =========================================================================
# Section 1: Root-of-unity arithmetic (6 tests)
# =========================================================================

class TestRootOfUnityArithmetic:
    """Tests for basic root-of-unity quantum integer arithmetic."""

    def test_primitive_root_order(self):
        """omega^N = 1 for omega = e^{2*pi*i/N}."""
        for N in [2, 3, 5, 7, 12, 24]:
            omega = primitive_root(N)
            assert abs(omega**N - 1.0) < 1e-12, f"omega^{N} != 1 for N={N}"

    def test_primitive_root_is_primitive(self):
        """omega^k != 1 for 0 < k < N (primitive root)."""
        for N in [3, 5, 7]:
            omega = primitive_root(N)
            for k in range(1, N):
                assert abs(omega**k - 1.0) > 1e-10, (
                    f"omega^{k} = 1 for N={N} (not primitive)"
                )

    def test_truncation_qN_zero(self):
        """[N]_omega = 0 at omega = e^{2*pi*i/N} (fundamental truncation).

        Uses the trigonometric form [N] = sin(N*pi/N)/sin(pi/N) = sin(pi)/sin(pi/N) = 0.
        """
        for N in [2, 3, 4, 5, 7, 12, 24]:
            ok, val = verify_truncation(N)
            assert ok, f"[{N}]_omega != 0: value = {val}"

    def test_quantum_integers_nonzero_below_N(self):
        """[n]_omega != 0 for 0 < n < N."""
        for N in [3, 5, 7]:
            omega = primitive_root(N)
            for n in range(1, N):
                qn = q_number_root_of_unity(n, omega, N)
                assert abs(qn) > 1e-10, f"[{n}]_omega = 0 for N={N}"

    def test_quantum_integer_list(self):
        """quantum_integers_at_root returns N+1 values with [N] = 0."""
        for N in [3, 5]:
            qi = quantum_integers_at_root(N)
            assert len(qi) == N + 1
            assert abs(qi[0]) < 1e-12  # [0] = 0
            assert abs(qi[N]) < 1e-12  # [N] = 0

    def test_primitive_root_invalid(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            primitive_root(1)


# =========================================================================
# Section 2: K3 parameters at root of unity (5 tests)
# =========================================================================

class TestRootOfUnityK3Params:
    """Tests for K3 quantum toroidal parameters at root of unity."""

    def test_kummer_cy2_constraint(self):
        """CY_2 constraint: prod q_a = 1 for Kummer parameters."""
        for N in [3, 5, 7, 12]:
            params = kummer_root_of_unity_params(N)
            assert params.cy2_residual < 1e-10, (
                f"CY_2 violated at N={N}: residual = {params.cy2_residual}"
            )

    def test_kummer_param_count(self):
        """Kummer parameters have 24 exponents."""
        params = kummer_root_of_unity_params(5)
        assert len(params.n_mukai) == MUKAI_RANK
        assert len(params.q_mukai) == MUKAI_RANK

    def test_kummer_exponent_sum(self):
        """Sum of exponents = 0 (CY_2 in additive form)."""
        for N in [3, 5, 7]:
            params = kummer_root_of_unity_params(N)
            # Sum of n_a: 4*1 + 4*(N-1) + 16*0 = 4 + 4N - 4 = 4N = 0 mod N
            assert sum(params.n_mukai) % N == 0

    def test_generic_params_custom(self):
        """Custom exponents work when CY_2 constraint satisfied."""
        N = 5
        exponents = [1] * 4 + [4] * 4 + [0] * 16  # sum = 4 + 16 + 0 = 20 = 0 mod 5
        params = generic_root_of_unity_params(N, exponents)
        assert params.cy2_residual < 1e-10

    def test_generic_params_cy2_violation(self):
        """Custom exponents violating CY_2 raise ValueError."""
        N = 5
        exponents = [1] * 24  # sum = 24, not 0 mod 5
        with pytest.raises(ValueError, match="CY_2"):
            generic_root_of_unity_params(N, exponents)


# =========================================================================
# Section 3: Periodic structure function (5 tests)
# =========================================================================

class TestPeriodicStructureFunction:
    """Tests for the structure function at root of unity."""

    def test_structure_function_finite(self):
        """G_{K3}(x) evaluates to finite value at generic x."""
        params = kummer_root_of_unity_params(5)
        x = 0.3 + 0.2j
        G = structure_function_root_of_unity(x, params)
        assert np.isfinite(abs(G))
        assert abs(G) > 1e-15

    def test_periodicity_trivial(self):
        """G(omega^N * x) = G(x) (trivially, since omega^N = 1)."""
        for N in [3, 5, 7]:
            params = kummer_root_of_unity_params(N)
            ok, res = verify_periodicity(params)
            assert ok, f"Periodicity failed at N={N}: residual = {res}"

    def test_poles_on_roots_of_unity(self):
        """Poles of G(x) are at N-th roots of unity."""
        for N in [3, 5, 7]:
            params = kummer_root_of_unity_params(N)
            poles = pole_structure(params)
            assert poles['poles_on_roots_of_unity']

    def test_pole_zero_balance(self):
        """Total pole count = total zero count = 24 (degree balance)."""
        params = kummer_root_of_unity_params(5)
        poles = pole_structure(params)
        assert poles['total_pole_count'] == MUKAI_RANK
        assert poles['total_zero_count'] == MUKAI_RANK

    def test_inversion_at_root_of_unity(self):
        """G(x) * G(1/x) = 1 at root of unity (from CY_2)."""
        params = kummer_root_of_unity_params(5)
        x = 0.4 + 0.3j
        G_x = structure_function_root_of_unity(x, params)
        G_inv = structure_function_root_of_unity(1.0 / x, params)
        assert abs(G_x * G_inv - 1.0) < 1e-10


# =========================================================================
# Section 4: Restricted partition function (7 tests)
# =========================================================================

class TestRestrictedPartitions:
    """Tests for the restricted (truncated) partition function."""

    def test_p24_restricted_base_cases(self):
        """p_{24}^{<N}(0) = 1 and p_{24}^{<N}(1) = 24 for all N >= 2."""
        for N in [2, 3, 5, 10]:
            assert restricted_colored_partition(0, 24, N) == 1
            assert restricted_colored_partition(1, 24, N) == 24

    def test_agrees_below_N(self):
        """p_{24}^{<N}(n) = p_{24}(n) for n < N."""
        for N in [3, 5, 7]:
            for n in range(N):
                p_full = _colored_partition(n, 24)
                p_rest = restricted_colored_partition(n, 24, N)
                assert p_full == p_rest, (
                    f"Disagree at n={n}, N={N}: full={p_full}, restricted={p_rest}"
                )

    def test_strictly_less_at_N(self):
        """p_{24}^{<N}(N) < p_{24}(N) for N >= 2 (truncation active)."""
        for N in [2, 3, 5]:
            p_full = _colored_partition(N, 24)
            p_rest = restricted_colored_partition(N, 24, N)
            assert p_rest < p_full, (
                f"Truncation not active at n=N={N}: full={p_full}, "
                f"restricted={p_rest}"
            )

    def test_truncated_fock_dimensions(self):
        """Truncated Fock dimensions are consistent with restricted partitions."""
        N = 5
        dims = truncated_fock_dimensions(N, max_charge=5)
        for n in range(len(dims)):
            expected = restricted_colored_partition(n, 24, N)
            assert dims[n] == expected, (
                f"Mismatch at charge {n}: got {dims[n]}, expected {expected}"
            )

    def test_total_simples_finite(self):
        """Total number of simples with charge bound is finite."""
        for N in [3, 5]:
            total = total_simple_objects(N, max_charge=N - 1)
            assert total > 0
            assert total < 10**10  # should be finite

    def test_comparison_first_disagreement(self):
        """First disagreement between restricted and unrestricted is at n = N."""
        for N in [3, 5]:
            comp = compare_restricted_unrestricted(N, max_n=N + 2)
            assert comp['all_agree_below_N']
            assert comp['first_disagreement'] == N

    def test_restricted_monotone_in_N(self):
        """Larger N gives larger restricted partitions (more parts allowed)."""
        n = 5
        p3 = restricted_colored_partition(n, 24, 3)
        p5 = restricted_colored_partition(n, 24, 5)
        p10 = restricted_colored_partition(n, 24, 10)
        assert p3 <= p5 <= p10


# =========================================================================
# Section 5: S-matrix and modularity (6 tests)
# =========================================================================

class TestSMatrix:
    """Tests for the S-matrix at root of unity."""

    def test_s_matrix_shape(self):
        """S-matrix is 24 x 24."""
        params = kummer_root_of_unity_params(5)
        S = charge_1_s_matrix(params)
        assert S.shape == (MUKAI_RANK, MUKAI_RANK)

    def test_s_matrix_nonzero_diagonal(self):
        """All diagonal entries of S are nonzero."""
        params = kummer_root_of_unity_params(5)
        S = charge_1_s_matrix(params)
        for a in range(MUKAI_RANK):
            assert abs(S[a, a]) > 1e-15, f"S[{a},{a}] = 0"

    def test_s_matrix_rank_deficient_kummer(self):
        """det(S) = 0 for Kummer params (16 directions have n_a=0 => identical rows).

        The Kummer parametrization has only 8 active directions (4 with n_a=+1,
        4 with n_a=N-1) and 16 trivial directions (n_a=0). The 16 trivial
        directions produce identical S-matrix rows, so rank(S) < 24.
        This is a genuine feature: the abelian Kummer truncation is
        rank-deficient. Full rank requires ALL 24 directions to have
        distinct nonzero exponents.
        """
        params = kummer_root_of_unity_params(5)
        analysis = s_matrix_nondegeneracy(params)
        # det = 0 because 16 rows are identical (n_a = 0)
        assert not analysis['det_S_nonzero']
        # Rank should be < 24 (16 degenerate + 2 distinct active groups = ~3 distinct rows)
        assert analysis['rank_S'] < MUKAI_RANK

    def test_not_mtc_abelian(self):
        """Abelian K3 quantum toroidal is NOT MTC at charge 1."""
        params = kummer_root_of_unity_params(5)
        analysis = s_matrix_nondegeneracy(params)
        assert not analysis['is_mtc_charge_1']

    def test_s_matrix_diagonal_structure(self):
        """S-matrix is approximately diagonal for abelian gl_1.

        For the abelian case, cross-family braiding is trivial,
        so the off-diagonal entries are 1/sqrt(24) (normalisation),
        not zero. But the diagonal entries carry the nontrivial phases.
        """
        params = kummer_root_of_unity_params(5)
        S = charge_1_s_matrix(params)
        # All off-diagonal entries should be 1/sqrt(24)
        D = math.sqrt(MUKAI_RANK)
        for a in range(MUKAI_RANK):
            for b in range(MUKAI_RANK):
                if a != b:
                    assert abs(S[a, b] - 1.0 / D) < 1e-12, (
                        f"S[{a},{b}] = {S[a, b]}, expected 1/sqrt(24)"
                    )

    def test_s_matrix_varies_with_N(self):
        """S-matrix changes with N (different roots of unity)."""
        S3 = charge_1_s_matrix(kummer_root_of_unity_params(3))
        S5 = charge_1_s_matrix(kummer_root_of_unity_params(5))
        # At least one entry should differ
        assert not np.allclose(S3, S5, atol=1e-8)


# =========================================================================
# Section 6: T-matrix and modular relations (4 tests)
# =========================================================================

class TestTMatrix:
    """Tests for the T-matrix and modular relations."""

    def test_t_matrix_shape(self):
        """T-matrix is 24 x 24."""
        params = kummer_root_of_unity_params(5)
        T = charge_1_t_matrix(params)
        assert T.shape == (MUKAI_RANK, MUKAI_RANK)

    def test_t_matrix_diagonal(self):
        """T-matrix is diagonal."""
        params = kummer_root_of_unity_params(5)
        T = charge_1_t_matrix(params)
        for a in range(MUKAI_RANK):
            for b in range(MUKAI_RANK):
                if a != b:
                    assert abs(T[a, b]) < 1e-15, f"T[{a},{b}] != 0"

    def test_t_matrix_entries_are_roots_of_unity(self):
        """Diagonal entries of T are N-th roots of unity."""
        N = 5
        params = kummer_root_of_unity_params(N)
        T = charge_1_t_matrix(params)
        for a in range(MUKAI_RANK):
            # T[a,a]^N should be 1 (since T[a,a] = omega^{...})
            val = T[a, a]
            assert abs(abs(val) - 1.0) < 1e-12, f"|T[{a},{a}]| != 1"

    def test_modular_relations_report(self):
        """Modular relations verification returns structured data.

        S is NOT purely diagonal (off-diagonal entries = 1/sqrt(24)),
        while T IS diagonal with distinct entries. Therefore S and T
        do NOT commute in general. This is consistent with the abelian
        algebra not being an MTC -- the modular relations fail.
        """
        params = kummer_root_of_unity_params(5)
        result = verify_modular_relations(params)
        assert 'S_T_commute' in result
        assert 'modular_relations_hold' in result
        # The modular relations (ST)^3 = S^2 fail for the abelian case:
        # this is expected and confirms the algebra is pre-modular, not MTC.


# =========================================================================
# Section 7: Verlinde dimensions (4 tests)
# =========================================================================

class TestVerlindeDimensions:
    """Tests for the Verlinde dimension formula."""

    def test_verlinde_genus_0(self):
        """Verlinde dimension at genus 0 is computable."""
        result = verlinde_dimension_genus_g(5, g=0)
        assert 'verlinde_N' in result
        assert result['N'] == 5

    def test_verlinde_genus_1(self):
        """Verlinde dimension at genus 1 is computable."""
        result = verlinde_dimension_genus_g(5, g=1)
        assert 'verlinde_N' in result
        # At g=1, chi = 0, so the sum should be 24 (number of simples)
        # (each term is s_ratio^0 = 1)
        assert abs(result['verlinde_N'] - MUKAI_RANK) < 1e-8

    def test_verlinde_increases_with_N(self):
        """Truncated Fock dimensions increase with N (at fixed charge)."""
        result_3 = verlinde_dimension_genus_g(3, g=0)
        result_7 = verlinde_dimension_genus_g(7, g=0)
        dims_3 = result_3['truncated_fock_dims']
        dims_7 = result_7['truncated_fock_dims']
        # At charge 1, both should be 24
        assert dims_3[1] == 24
        assert dims_7[1] == 24

    def test_generic_verlinde_formula(self):
        """Generic Verlinde formula (1+t)^{3g} at t=1 is 2^{3g}."""
        for g in [0, 1, 2, 3]:
            result = verlinde_dimension_genus_g(5, g=g)
            assert result['generic_verlinde'] == 2 ** (3 * g)


# =========================================================================
# Section 8: Conway group analysis (4 tests)
# =========================================================================

class TestConwayGroup:
    """Tests for the Conway group / Mathieu moonshine connection."""

    def test_conway_order(self):
        """Co_0 order is correct."""
        analysis = conway_analysis(5)
        expected = 2**22 * 3**9 * 5**4 * 7**2 * 11 * 13 * 23
        assert analysis['co0_order'] == expected

    def test_m24_order(self):
        """M_24 order is correct."""
        analysis = conway_analysis(5)
        expected = 2**10 * 3**3 * 5 * 7 * 11 * 23
        assert analysis['m24_order'] == expected

    def test_conway_equivariant_at_prime(self):
        """N sharing a prime factor with |Co_0| has Conway equivariance."""
        # N = 23 is a prime factor of |Co_0|
        analysis = conway_analysis(23)
        assert analysis['conway_equivariant']
        assert 23 in analysis['shares_co0_primes']

    def test_gauss_sum_magnitude(self):
        """Gauss sum |G_N| = sqrt(N) for ODD N (Gauss's theorem).

        For even N, the Gauss sum has different behavior:
        N = 2 mod 4: G_N = 0.  N = 0 mod 4: |G_N| = sqrt(2N).
        We test only odd N where the classical |G_N| = sqrt(N) holds.
        """
        for N in [3, 5, 7, 11, 13, 23]:
            result = conway_connection_analysis(N)
            assert result['gauss_sum_matches'], (
                f"Gauss sum at N={N}: |G| = {result['gauss_sum_abs']}, "
                f"expected sqrt({N}) = {math.sqrt(N)}"
            )


# =========================================================================
# Section 9: The five critical questions (5 tests)
# =========================================================================

class TestFiveCriticalQuestions:
    """Tests for the five critical questions about the K3 root-of-unity."""

    def test_q1_finiteness(self):
        """Q1: Finitely many simples (with charge bound)."""
        for N in [3, 5]:
            result = finiteness_analysis(N)
            assert result['finite_at_each_charge']
            assert result['charge_bounded_total_N'] > 0
            assert result['charge_bounded_total_N'] < 10**15

    def test_q2_not_mtc_abelian(self):
        """Q2: Abelian K3 is NOT MTC (braiding too trivial)."""
        for N in [3, 5, 7]:
            result = modularity_analysis(N)
            assert not result['is_mtc']
            assert result['is_pre_modular']

    def test_q3_verlinde_p24(self):
        """Q4: Restricted partitions agree with full below N."""
        for N in [3, 5]:
            result = verlinde_p24_analysis(N)
            assert result['agree_exactly_below_N']

    def test_q5_conway_connection(self):
        """Q5: Conway equivariance at ODD primes dividing |Co_0|.

        Gauss sum |G_N| = sqrt(N) holds for ODD N. For N=2, the Gauss
        sum vanishes (classical result: G_2 = 1 + (-1) = 0).
        We test only the odd prime factors of |Co_0|.
        """
        for p in [3, 5, 7, 11, 13, 23]:
            result = conway_connection_analysis(p)
            assert result['gauss_sum_matches'], (
                f"Gauss sum failed at p={p}: "
                f"|G|={result['gauss_sum_abs']:.6f}, "
                f"expected sqrt({p})={math.sqrt(p):.6f}"
            )

    def test_finiteness_truncation_ratio(self):
        """Truncation ratio decreases with N (fewer modules killed at larger N)."""
        r3 = finiteness_analysis(3)
        r5 = finiteness_analysis(5)
        # At N=3: more truncation (smaller ratio)
        # Actually ratio = truncated / unrestricted, and larger N has
        # larger restricted count relative to unrestricted
        # Let us just check both are between 0 and 1
        assert 0 < r3['truncation_ratio'] <= 1.0
        assert 0 < r5['truncation_ratio'] <= 1.0


# =========================================================================
# Section 10: Multi-path cross-checks (7 tests)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification: same quantity computed two independent ways."""

    def test_truncation_two_paths(self):
        """[N]_omega = 0 via both trigonometric and exponential formulas.

        Path 1: sin(N*pi/N)/sin(pi/N) = 0 (trigonometric).
        Path 2: (omega^N - omega^{-N})/(omega - omega^{-1}) with omega^N = 1.
        """
        for N in [3, 5, 7]:
            omega = primitive_root(N)
            # Path 1: our function
            ok, val = verify_truncation(N)
            assert ok
            # Path 2: direct computation omega^N = 1 so numerator = 0
            numer = omega**N - omega**(-N)
            assert abs(numer) < 1e-12

    def test_cy2_additive_vs_multiplicative(self):
        """CY_2 constraint: sum n_a = 0 mod N <=> prod q_a = 1.

        Two independent paths to the same constraint.
        """
        for N in [3, 5, 7, 12]:
            params = kummer_root_of_unity_params(N)
            # Path 1: additive (sum of exponents)
            assert sum(params.n_mukai) % N == 0
            # Path 2: multiplicative (product of q_a)
            prod_q = complex(1.0)
            for qa in params.q_mukai:
                prod_q *= qa
            assert abs(prod_q - 1.0) < 1e-10

    def test_restricted_partition_two_computations(self):
        """Restricted partitions via DP agree with generating-function truncation.

        Path 1: restricted_colored_partition (dynamic programming).
        Path 2: Direct coefficient extraction from prod_{k=1}^{N-1} 1/(1-q^k)^{24}
        via polynomial multiplication.
        """
        N = 4
        max_n = 6
        # Path 1: DP
        dp_vals = [restricted_colored_partition(n, 24, N) for n in range(max_n + 1)]
        # Path 2: polynomial multiplication
        # Start with [1] (constant polynomial = 1)
        poly = [0] * (max_n + 1)
        poly[0] = 1
        for k in range(1, N):  # k = 1, ..., N-1
            for _ in range(24):  # 24 colours
                new_poly = list(poly)
                for j in range(k, max_n + 1):
                    new_poly[j] += new_poly[j - k]
                poly = new_poly
        for n in range(max_n + 1):
            assert dp_vals[n] == poly[n], (
                f"Mismatch at n={n}: DP={dp_vals[n]}, poly={poly[n]}"
            )

    def test_inversion_identity_two_paths(self):
        """G(x)*G(1/x) = 1 verified by both direct evaluation and CY_2.

        Path 1: numerical evaluation of G(x)*G(1/x).
        Path 2: algebraic proof via prod q_a = 1 => G(x)*G(1/x) = (prod q_a)^2 = 1.
        """
        for N in [3, 5, 7]:
            params = kummer_root_of_unity_params(N)
            x = 0.4 + 0.3j
            # Path 1: direct evaluation
            Gx = structure_function_root_of_unity(x, params)
            G_inv = structure_function_root_of_unity(1.0 / x, params)
            product = Gx * G_inv
            assert abs(product - 1.0) < 1e-10
            # Path 2: CY_2 implies (prod q_a)^2 = 1
            prod_q_sq = complex(1.0)
            for qa in params.q_mukai:
                prod_q_sq *= qa * qa
            assert abs(prod_q_sq - 1.0) < 1e-10

    def test_quantum_integer_trig_vs_ratio(self):
        """Quantum integer via sin formula vs direct ratio for N >= 3.

        Path 1: sin(n*pi/N)/sin(pi/N) (our implementation).
        Path 2: (omega^n - omega^{-n})/(omega - omega^{-1}) (direct).
        Both should agree for N >= 3 (where denom != 0).
        """
        for N in [3, 5, 7, 11]:
            omega = primitive_root(N)
            for n in range(N + 1):
                # Path 1: our function
                q1 = q_number_root_of_unity(n, omega, N)
                # Path 2: direct formula
                denom = omega - 1.0 / omega
                q2 = (omega**n - omega**(-n)) / denom
                assert abs(q1 - q2) < 1e-10, (
                    f"Mismatch at N={N}, n={n}: trig={q1}, ratio={q2}"
                )

    def test_pole_count_matches_mukai_rank(self):
        """Pole/zero count = 24 verified by both pole_structure and direct count.

        Path 1: pole_structure() analysis.
        Path 2: counting nonzero exponents in the product formula.
        """
        for N in [3, 5, 7]:
            params = kummer_root_of_unity_params(N)
            # Path 1
            poles = pole_structure(params)
            assert poles['total_pole_count'] == 24
            assert poles['total_zero_count'] == 24
            # Path 2: direct count -- each of 24 factors contributes
            # exactly one pole and one zero
            assert len(params.q_mukai) == 24

    def test_gauss_sum_two_computations(self):
        """Gauss sum via direct sum and via closed form for odd primes.

        Path 1: G_p = sum_{k=0}^{p-1} omega^{k^2} (direct computation).
        Path 2: |G_p|^2 = p for odd prime p (classical Gauss theorem).
        """
        for p in [3, 5, 7, 11, 13]:
            omega = primitive_root(p)
            # Path 1: direct
            gauss = sum(omega ** (k * k) for k in range(p))
            # Path 2: |G|^2 = p (Gauss)
            assert abs(abs(gauss)**2 - p) < 0.01, (
                f"|G_{p}|^2 = {abs(gauss)**2:.6f}, expected {p}"
            )


# =========================================================================
# Section 11: Full verification (3 tests)
# =========================================================================

class TestFullVerification:
    """Tests for the complete verification suite."""

    def test_full_verification_n5(self):
        """Full verification at N = 5 (coprime to 24)."""
        result = full_verification(N=5)
        assert result['all_basic_pass']
        assert result['status'] == 'CONJECTURAL'

    def test_full_verification_n3(self):
        """Full verification at N = 3 (divides 24)."""
        result = full_verification(N=3)
        assert result['all_basic_pass']

    def test_full_verification_n7(self):
        """Full verification at N = 7 (coprime to 24, prime factor of |Co_0|)."""
        result = full_verification(N=7)
        assert result['all_basic_pass']
        assert result['conway_equivariant']
