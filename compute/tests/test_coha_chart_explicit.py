r"""Tests for explicit CoHA computations on every chart of every standard CY3.

THEOREM BEING TESTED:
    For each standard CY3 with quiver-chart (Q, W), the critical CoHA
        H(Q, W) = bigoplus_d H^{BM}_*(M_d(Q,W), phi_{Tr W})
    is an associative (E_1) algebra with explicit generators, relations,
    and E_1 multiplication.

    The Davison-Meinhardt PBW theorem:
        gr(CoHA(Q,W)) = Sym(BPS)

MULTI-PATH VERIFICATION (3+ paths per claim, per CLAUDE.md mandate):
    Path 1: Direct computation from definitions
    Path 2: Generating function comparison (MacMahon, Goettsche, plethystic)
    Path 3: Cross-family consistency (kappa additivity, McKay scaling)
    Path 4: DT/shadow identification (Faber-Pandharipande)
    Path 5: Bar complex Euler characteristic
    Path 6: Literature values (OEIS, Schiffmann-Vasserot, MNOP)
    Path 7: PBW filtration verification
    Path 8: Euler form / antisymmetry cross-check

REFERENCES:
    Schiffmann-Vasserot arXiv:1211.1287: CoHA(C^3) = Y^+(gl_hat_1)
    Davison-Meinhardt arXiv:1512.08898: PBW for CoHA
    Rapcak-Soibelman-Yang-Zhao arXiv:1810.10402: toric CY3 CoHA
    MNOP arXiv:math/0312059: DT/GW correspondence
    OEIS A000219: plane partitions
    OEIS A000041: ordinary partitions
    Goettsche (1990): chi(Hilb^n(S)) formula
"""

import pytest
from fractions import Fraction

from compute.lib.coha_chart_explicit import (
    # Power series
    _fps_zero, _fps_one, _fps_mul, _fps_inv, _fps_log, _fps_exp, _fps_power,
    # Partitions
    _plane_partition_counts, _partition_counts, _macmahon, _euler_product,
    _hilb_euler_chars, _mobius_sieve,
    # Plethystic
    plethystic_log, plethystic_exp,
    # Quivers
    QuiverWithPotential,
    jordan_quiver, conifold_quiver, local_p2_quiver,
    mckay_z2_quiver, mckay_zn_quiver,
    # Moduli / vanishing
    ModuliStack, VanishingCycleSheaf,
    # CoHA dimensions
    chart_coha_dimension,
    _jordan_coha_dim, _conifold_coha_dim, _local_p2_coha_dim,
    # BPS
    bps_invariants_jordan, bps_invariants_conifold,
    bps_invariants_local_p2, bps_invariants_mckay_z2,
    # Shuffle / multiplication
    ShuffleAlgebra, CoHAMultiplicationTable,
    # PBW
    PBWFiltration,
    # Chart
    ChartCoHA, ChartBarComplex,
    # Cross-chart
    cross_chart_kappa_additivity, cross_chart_bps_consistency,
    all_charts_pbw_verification, all_charts_full_report,
    # Euler form
    euler_form_matrix,
    # Detailed computations
    conifold_two_variable_character, conifold_wall_crossing_formula,
    local_p2_topological_vertex_check,
    # Multi-path verification
    jordan_character_three_paths, conifold_character_three_paths,
    local_p2_character_three_paths,
    # Faber-Pandharipande
    _faber_pandharipande,
)


# ================================================================
# 0. FOUNDATIONAL ARITHMETIC TESTS
# ================================================================

class TestPowerSeriesFoundation:
    """Verify the exact power series arithmetic layer."""

    def test_fps_one(self):
        f = _fps_one(5)
        assert f[0] == Fraction(1)
        assert all(f[i] == Fraction(0) for i in range(1, 5))

    def test_fps_mul_identity(self):
        f = [Fraction(1), Fraction(2), Fraction(3)]
        one = _fps_one(5)
        result = _fps_mul(f, one, 5)
        for i in range(3):
            assert result[i] == f[i]

    def test_fps_mul_commutativity(self):
        f = [Fraction(1), Fraction(1)]
        g = [Fraction(1), Fraction(-1)]
        assert _fps_mul(f, g, 5) == _fps_mul(g, f, 5)

    def test_fps_inv_round_trip(self):
        N = 12
        f = list(_macmahon(N))
        finv = _fps_inv(f, N)
        product = _fps_mul(f, finv, N)
        assert product[0] == Fraction(1)
        for i in range(1, N):
            assert product[i] == Fraction(0)

    def test_fps_log_exp_round_trip(self):
        N = 10
        f = list(_macmahon(N))
        log_f = _fps_log(f, N)
        exp_log_f = _fps_exp(log_f, N)
        for i in range(N):
            assert abs(f[i] - exp_log_f[i]) < Fraction(1, 10**10)

    def test_fps_power_squares(self):
        N = 10
        f = list(_macmahon(N))
        assert _fps_mul(f, f, N) == _fps_power(f, 2, N)

    def test_fps_power_cubes(self):
        N = 8
        f = list(_macmahon(N))
        f2 = _fps_mul(f, f, N)
        f3 = _fps_mul(f2, f, N)
        assert f3 == _fps_power(f, 3, N)


# ================================================================
# 1. PARTITION COMBINATORICS TESTS
# ================================================================

class TestPartitionCombinatorics:
    """Verify plane partition and ordinary partition counts against OEIS."""

    def test_plane_partitions_oeis_a000219(self):
        """pp(n) = OEIS A000219: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        pp = _plane_partition_counts(11)
        for i, e in enumerate(expected):
            assert pp[i] == e, f"pp({i}) = {pp[i]}, expected {e}"

    def test_ordinary_partitions_oeis_a000041(self):
        """p(n) = OEIS A000041: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        pc = _partition_counts(11)
        for i, e in enumerate(expected):
            assert pc[i] == e, f"p({i}) = {pc[i]}, expected {e}"

    def test_macmahon_equals_plane_partitions(self):
        N = 15
        mac = _macmahon(N)
        pp = _plane_partition_counts(N)
        for n in range(N):
            assert int(mac[n]) == pp[n]

    def test_euler_equals_ordinary_partitions(self):
        N = 15
        ep = _euler_product(N)
        pc = _partition_counts(N)
        for n in range(N):
            assert int(ep[n]) == pc[n]

    def test_hilb_euler_chars_c2(self):
        """chi(Hilb^d(C^2)) = p(d) (chi(C^2) = 1 effectively for point)."""
        # For chi_S = 1: prod 1/(1-q^n) = P(q) -> ordinary partitions
        hilb = _hilb_euler_chars(1, 11)
        pc = _partition_counts(11)
        for i in range(11):
            assert hilb[i] == pc[i]

    def test_hilb_euler_chars_p2(self):
        """chi(Hilb^d(P^2)) for chi(P^2) = 3: first values 1, 3, 9, 22, 51."""
        hilb = _hilb_euler_chars(3, 6)
        expected = [1, 3, 9, 22, 51, 108]
        for i, e in enumerate(expected):
            assert hilb[i] == e, f"Hilb^{i}(P^2) = {hilb[i]}, expected {e}"

    def test_macmahon_inverse(self):
        """M(q) * M(q)^{-1} = 1."""
        N = 12
        mac = list(_macmahon(N))
        inv_mac = _fps_inv(mac, N)
        product = _fps_mul(mac, inv_mac, N)
        assert product[0] == Fraction(1)
        for i in range(1, N):
            assert product[i] == Fraction(0)


# ================================================================
# 2. PLETHYSTIC OPERATIONS TESTS
# ================================================================

class TestPlethysticOperations:
    """Verify plethystic log and exp (BPS extraction)."""

    def test_plog_macmahon_gives_n(self):
        """PLog(M(q)) = sum n*q^n => Omega(n) = n for C^3."""
        N = 12
        mac = list(_macmahon(N))
        plog = plethystic_log(mac, N)
        for n in range(1, N):
            assert plog[n] == Fraction(n), f"PLog(M) at q^{n}: got {plog[n]}"

    def test_plog_euler_gives_1(self):
        """PLog(P(q)) = sum q^n => Omega(n) = 1 for C^2."""
        N = 12
        ep = list(_euler_product(N))
        plog = plethystic_log(ep, N)
        for n in range(1, N):
            assert plog[n] == Fraction(1), f"PLog(P) at q^{n}: got {plog[n]}"

    def test_plog_goettsche_p2_gives_3(self):
        """PLog(prod 1/(1-q^n)^3) = sum 3*q^n => Omega(n) = 3 for P^2."""
        N = 10
        # Build prod 1/(1-q^n)^3
        f = _fps_one(N)
        for k in range(1, N):
            for _ in range(3):
                for n in range(k, N):
                    f[n] += f[n - k]
        plog = plethystic_log(f, N)
        for n in range(1, N):
            assert plog[n] == Fraction(3), f"PLog at q^{n}: got {plog[n]}"

    def test_plog_pexp_round_trip(self):
        N = 12
        mac = list(_macmahon(N))
        plog = plethystic_log(mac, N)
        pexp = plethystic_exp(plog, N)
        for i in range(N):
            assert abs(mac[i] - pexp[i]) < Fraction(1, 10**10)

    def test_pexp_single_generator(self):
        """PExp(q) = 1/(1-q)."""
        N = 8
        g = _fps_zero(N)
        g[1] = Fraction(1)
        result = plethystic_exp(g, N)
        for n in range(N):
            assert result[n] == Fraction(1)

    def test_pexp_n_generators(self):
        """PExp(n*q) = 1/(1-q)^n."""
        N = 8
        for n_gen in [2, 3, 5]:
            g = _fps_zero(N)
            g[1] = Fraction(n_gen)
            result = plethystic_exp(g, N)
            # 1/(1-q)^n coefficients = C(n+k-1, k)
            for k in range(N):
                expected = Fraction(1)
                for j in range(1, k + 1):
                    expected *= Fraction(n_gen + j - 1, j)
                assert abs(result[k] - expected) < Fraction(1, 10**8), (
                    f"PExp({n_gen}*q)[{k}]: got {result[k]}, expected {expected}"
                )


# ================================================================
# 3. QUIVER DATA TESTS
# ================================================================

class TestQuiverData:
    """Test quiver-with-potential data structures."""

    def test_jordan_quiver(self):
        Q = jordan_quiver()
        assert Q.n_vertices == 1
        assert Q.n_arrows == 3
        assert Q.name == "Jordan (C^3)"
        assert len(Q.potential_terms) == 2

    def test_conifold_quiver(self):
        Q = conifold_quiver()
        assert Q.n_vertices == 2
        assert Q.n_arrows == 4
        assert len(Q.potential_terms) == 2

    def test_local_p2_quiver(self):
        Q = local_p2_quiver()
        assert Q.n_vertices == 3
        assert Q.n_arrows == 9
        assert len(Q.potential_terms) == 6

    def test_mckay_z2_quiver(self):
        Q = mckay_z2_quiver()
        assert Q.n_vertices == 2
        assert Q.n_arrows == 6

    def test_mckay_zn_vertex_count(self):
        for n in [2, 3, 4, 5, 6]:
            Q = mckay_zn_quiver(n)
            assert Q.n_vertices == n
            assert Q.n_arrows == 3 * n

    def test_jordan_euler_form(self):
        """chi(d, d) = d^2 - 3d^2 = -2d^2 for Jordan quiver."""
        Q = jordan_quiver()
        assert Q.euler_form((1,), (1,)) == -2
        assert Q.euler_form((2,), (1,)) == 2 - 6  # = -4
        assert Q.euler_form((2,), (2,)) == 4 - 12  # = -8

    def test_conifold_euler_form(self):
        """chi(e_1, e_1) = 1 - 0 = 1 (no loops at vertex 0)."""
        Q = conifold_quiver()
        # e_0 = (1,0), e_1 = (0,1)
        assert Q.euler_form((1, 0), (1, 0)) == 1  # 1*1 - 0 arrows 0->0
        assert Q.euler_form((0, 1), (0, 1)) == 1  # same for vertex 1
        # chi(e_0, e_1) = 0 - 2*1*1 = -2 (two arrows 0->1)
        assert Q.euler_form((1, 0), (0, 1)) == -2
        # chi(e_1, e_0) = 0 - 2*1*1 = -2 (two arrows 1->0)
        assert Q.euler_form((0, 1), (1, 0)) == -2

    def test_conifold_antisymmetric_form(self):
        """<e_0, e_1> = chi(e_0,e_1) - chi(e_1,e_0) = -2 - (-2) = 0."""
        Q = conifold_quiver()
        assert Q.antisymmetric_form((1, 0), (0, 1)) == 0

    def test_local_p2_euler_form(self):
        Q = local_p2_quiver()
        # chi(e_0, e_0) = 1 - 0 = 1 (no loops at vertex 0)
        assert Q.euler_form((1, 0, 0), (1, 0, 0)) == 1
        # chi(e_0, e_1) = 0 - 3 = -3 (three arrows 0->1)
        assert Q.euler_form((1, 0, 0), (0, 1, 0)) == -3
        # chi(e_0, e_2) = 0 - 0 = 0 (no arrows 0->2 directly)
        assert Q.euler_form((1, 0, 0), (0, 0, 1)) == 0

    def test_jordan_rep_space_dim(self):
        """dim Rep(Jordan, d) = 3d^2 (three d x d matrices)."""
        Q = jordan_quiver()
        for d in range(1, 6):
            assert Q.rep_space_dim((d,)) == 3 * d * d

    def test_jordan_virtual_dim(self):
        """vdim = rep_dim - gauge_dim = 3d^2 - d^2 = 2d^2."""
        Q = jordan_quiver()
        for d in range(1, 6):
            assert Q.virtual_dim((d,)) == 2 * d * d


# ================================================================
# 4. MODULI STACK TESTS
# ================================================================

class TestModuliStack:
    """Test moduli stack M_d(Q, W) dimensions and structure."""

    def test_jordan_moduli_d1(self):
        Q = jordan_quiver()
        M = ModuliStack(Q, (1,))
        assert M.rep_space_dim == 3
        assert M.gauge_dim == 1
        assert M.virtual_dim == 2

    def test_jordan_moduli_d2(self):
        Q = jordan_quiver()
        M = ModuliStack(Q, (2,))
        assert M.rep_space_dim == 12
        assert M.gauge_dim == 4
        assert M.virtual_dim == 8

    def test_conifold_moduli_11(self):
        Q = conifold_quiver()
        M = ModuliStack(Q, (1, 1))
        # rep_dim = a1: 1*1 + a2: 1*1 + b1: 1*1 + b2: 1*1 = 4
        assert M.rep_space_dim == 4
        # gauge_dim = 1^2 + 1^2 = 2
        assert M.gauge_dim == 2

    def test_local_p2_moduli_111(self):
        Q = local_p2_quiver()
        M = ModuliStack(Q, (1, 1, 1))
        # 9 arrows, each 1*1 = 9
        assert M.rep_space_dim == 9
        # gauge = 1+1+1 = 3
        assert M.gauge_dim == 3

    def test_moduli_summary_returns_dict(self):
        Q = jordan_quiver()
        M = ModuliStack(Q, (3,))
        s = M.summary()
        assert "rep_dim" in s
        assert "gauge_dim" in s
        assert s["d"] == (3,)


# ================================================================
# 5. VANISHING CYCLE TESTS
# ================================================================

class TestVanishingCycle:
    """Test vanishing cycle sheaf structure."""

    def test_jordan_is_constant(self):
        Q = jordan_quiver()
        phi = VanishingCycleSheaf(Q, (1,))
        assert phi.is_constant is True

    def test_jordan_euler_char_d1(self):
        Q = jordan_quiver()
        phi = VanishingCycleSheaf(Q, (1,))
        assert phi.euler_char == 1  # pp(1) = 1

    def test_jordan_euler_char_d3(self):
        Q = jordan_quiver()
        phi = VanishingCycleSheaf(Q, (3,))
        assert phi.euler_char == 6  # pp(3) = 6

    def test_bm_homology_dim_jordan(self):
        Q = jordan_quiver()
        for d, expected_pp in [(0, 1), (1, 1), (2, 3), (3, 6), (4, 13)]:
            phi = VanishingCycleSheaf(Q, (d,))
            assert phi.bm_homology_dim() == expected_pp


# ================================================================
# 6. CoHA DIMENSION TESTS (the central computation)
# ================================================================

class TestCoHADimensions:
    """Test dim CoHA_d for each chart, cross-checked against generating functions."""

    def test_jordan_dims_are_plane_partitions(self):
        """dim CoHA_n(Jordan) = pp(n). Path 1: direct."""
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for n, e in enumerate(expected):
            assert _jordan_coha_dim(n) == e

    def test_jordan_dims_match_macmahon(self):
        """dim CoHA_n(Jordan) = M(q) coefficient. Path 2: GF."""
        N = 11
        mac = _macmahon(N)
        for n in range(N):
            assert _jordan_coha_dim(n) == int(mac[n])

    def test_conifold_single_vertex_dims(self):
        """CoHA_{(d,0)} = p(d), CoHA_{(0,d)} = p(d)."""
        pc = _partition_counts(8)
        for d in range(8):
            assert _conifold_coha_dim(d, 0) == pc[d]
            assert _conifold_coha_dim(0, d) == pc[d]

    def test_conifold_diagonal_dims(self):
        """CoHA_{(d,d)} = pp(d) on diagonal."""
        pp = _plane_partition_counts(8)
        for d in range(8):
            assert _conifold_coha_dim(d, d) == pp[d]

    def test_conifold_symmetry(self):
        """dim CoHA_{(d1,d2)} = dim CoHA_{(d2,d1)} by Z_2 symmetry."""
        for d1 in range(6):
            for d2 in range(6):
                assert _conifold_coha_dim(d1, d2) == _conifold_coha_dim(d2, d1)

    def test_conifold_off_diagonal(self):
        """Known off-diagonal values for the conifold."""
        assert _conifold_coha_dim(2, 1) == 2
        assert _conifold_coha_dim(3, 1) == 3
        assert _conifold_coha_dim(3, 2) == 5
        assert _conifold_coha_dim(4, 1) == 5
        assert _conifold_coha_dim(4, 2) == 10

    def test_local_p2_symmetric_diagonal(self):
        """CoHA_{(d,d,d)} = chi(Hilb^d(P^2)) for local P^2."""
        hilb = _hilb_euler_chars(3, 6)
        for d in range(6):
            assert _local_p2_coha_dim(d, d, d) == hilb[d]

    def test_local_p2_single_vertex(self):
        """CoHA at a single vertex = p(d)."""
        pc = _partition_counts(6)
        for d in range(1, 6):
            assert _local_p2_coha_dim(d, 0, 0) == pc[d]
            assert _local_p2_coha_dim(0, d, 0) == pc[d]
            assert _local_p2_coha_dim(0, 0, d) == pc[d]

    def test_local_p2_two_vertices(self):
        """CoHA at (1,1,0) = 3 (3 arrows from vertex 0 to vertex 1)."""
        assert _local_p2_coha_dim(1, 1, 0) == 3
        assert _local_p2_coha_dim(1, 0, 1) == 3
        assert _local_p2_coha_dim(0, 1, 1) == 3

    def test_mckay_diagonal_is_plane_partitions(self):
        """McKay Z_n diagonal: dim CoHA_{(d,...,d)} = pp(d)."""
        pp = _plane_partition_counts(6)
        for n in [2, 3, 4]:
            Q = mckay_zn_quiver(n)
            for d in range(6):
                dvec = tuple([d] * n)
                assert chart_coha_dimension(Q, dvec) == pp[d]


# ================================================================
# 7. BPS INVARIANT TESTS
# ================================================================

class TestBPSInvariants:
    """Test BPS invariants Omega(d) from plethystic logarithm."""

    def test_jordan_bps_omega_n_equals_n(self):
        """C^3: Omega(n) = n for all n >= 1."""
        bps = bps_invariants_jordan(12)
        for n in range(1, 12):
            assert bps[n] == n

    def test_conifold_bps_vertex_sectors(self):
        """Conifold: Omega(n,0) = n, Omega(0,n) = n."""
        bps = bps_invariants_conifold(8)
        for n in range(1, 8):
            assert bps[(n, 0)] == n
            assert bps[(0, n)] == n

    def test_conifold_bps_diagonal(self):
        """Conifold: Omega(n,n) = 1 (single D2-brane)."""
        bps = bps_invariants_conifold(8)
        for n in range(1, 8):
            assert bps[(n, n)] == 1

    def test_local_p2_bps_symmetric(self):
        """Local P^2: Omega(d,d,d) = 3 = chi(P^2)."""
        bps = bps_invariants_local_p2(8)
        for d in range(1, 8):
            assert bps[(d, d, d)] == 3

    def test_local_p2_bps_single_vertex(self):
        """Local P^2: Omega(d,0,0) = d."""
        bps = bps_invariants_local_p2(6)
        for d in range(1, 6):
            assert bps[(d, 0, 0)] == d

    def test_mckay_z2_bps_diagonal(self):
        """C^3/Z_2: Omega(d,d) = d on diagonal."""
        bps = bps_invariants_mckay_z2(8)
        for d in range(1, 8):
            assert bps[(d, d)] == d

    def test_bps_from_plog_jordan(self):
        """Verify BPS via PLog(M(q)) = sum n*q^n independently."""
        N = 10
        mac = list(_macmahon(N))
        plog = plethystic_log(mac, N)
        for n in range(1, N):
            assert plog[n] == Fraction(n)


# ================================================================
# 8. SHUFFLE ALGEBRA TESTS
# ================================================================

class TestShuffleAlgebra:
    """Test the shuffle algebra realization of CoHA multiplication."""

    def test_jordan_product_character(self):
        """Character-level product maps to CoHA_{a+b}."""
        sa = ShuffleAlgebra(jordan_quiver(), N=12)
        for a in range(5):
            for b in range(5 - a):
                pp = _plane_partition_counts(a + b + 1)
                assert sa.shuffle_product_character(a, b) == pp[a + b]

    def test_conifold_product_character(self):
        sa = ShuffleAlgebra(conifold_quiver(), N=12)
        pp = _plane_partition_counts(6)
        for d in range(6):
            assert sa.shuffle_product_character(d, 0) == pp[d]

    def test_zeta_at_zero(self):
        """zeta(0) = 1 at the CY point."""
        sa = ShuffleAlgebra(jordan_quiver())
        assert sa.zeta_function(Fraction(0)) == Fraction(1)


# ================================================================
# 9. E_1 MULTIPLICATION TABLE TESTS
# ================================================================

class TestMultiplicationTable:
    """Test the explicit E_1 multiplication tables."""

    def test_jordan_dimensions(self):
        mt = CoHAMultiplicationTable(jordan_quiver(), max_weight=8)
        pp = _plane_partition_counts(9)
        for d in range(9):
            assert mt.dimension(d) == pp[d]

    def test_jordan_product_dimensions(self):
        mt = CoHAMultiplicationTable(jordan_quiver(), max_weight=6)
        table = mt.product_dimensions()
        pp = _plane_partition_counts(7)
        for a in range(7):
            for b in range(7 - a):
                assert table[(a, b)] == pp[a + b]

    def test_associativity_characters(self):
        """Associativity at the character level for all charts."""
        for quiver_fn in [jordan_quiver, conifold_quiver, local_p2_quiver]:
            mt = CoHAMultiplicationTable(quiver_fn(), max_weight=6)
            assert mt.verify_associativity_characters() is True

    def test_tensor_decomposition_dimensions(self):
        mt = CoHAMultiplicationTable(jordan_quiver(), max_weight=5)
        dec = mt.tensor_decomposition(2, 3)
        pp = _plane_partition_counts(6)
        assert dec["source_dim"] == pp[2] * pp[3]  # 3 * 6 = 18
        assert dec["target_dim"] == pp[5]  # 24

    def test_generator_names(self):
        mt = CoHAMultiplicationTable(jordan_quiver(), max_weight=4)
        names = mt.generator_names(2)
        assert len(names) == 3  # pp(2) = 3

    def test_full_table_returns_dict(self):
        mt = CoHAMultiplicationTable(jordan_quiver(), max_weight=4)
        table = mt.full_table()
        assert "quiver" in table
        assert "dimensions" in table
        assert table["associative"] is True

    def test_conifold_multiplication_table(self):
        mt = CoHAMultiplicationTable(conifold_quiver(), max_weight=5)
        table = mt.product_dimensions()
        # On diagonal: dim(d) = pp(d)
        pp = _plane_partition_counts(6)
        for d in range(6):
            assert table[(d, 0)] == pp[d]

    def test_local_p2_multiplication_table(self):
        mt = CoHAMultiplicationTable(local_p2_quiver(), max_weight=5)
        hilb = _hilb_euler_chars(3, 6)
        for d in range(6):
            assert mt.dimension(d) == hilb[d]


# ================================================================
# 10. PBW FILTRATION TESTS (Davison-Meinhardt)
# ================================================================

class TestPBWFiltration:
    """Test the PBW theorem: gr(CoHA) = Sym(BPS)."""

    def test_jordan_pbw(self):
        """PBW for C^3: PExp(sum n*q^n) = M(q)."""
        pbw = PBWFiltration(jordan_quiver(), N=12)
        result = pbw.verify_pbw()
        assert result["pexp_match"] is True

    def test_conifold_pbw(self):
        """PBW for conifold diagonal."""
        pbw = PBWFiltration(conifold_quiver(), N=12)
        result = pbw.verify_pbw()
        assert result["pexp_match"] is True

    def test_local_p2_pbw(self):
        """PBW for local P^2: PExp(3*sum q^n) = prod 1/(1-q^n)^3."""
        pbw = PBWFiltration(local_p2_quiver(), N=10)
        result = pbw.verify_pbw()
        assert result["pexp_match"] is True

    def test_mckay_z2_pbw(self):
        """PBW for C^3/Z_2."""
        pbw = PBWFiltration(mckay_zn_quiver(2), N=10)
        result = pbw.verify_pbw()
        assert result["pexp_match"] is True

    def test_mckay_z3_pbw(self):
        """PBW for C^3/Z_3."""
        pbw = PBWFiltration(mckay_zn_quiver(3), N=10)
        result = pbw.verify_pbw()
        assert result["pexp_match"] is True

    def test_jordan_bps_from_pbw(self):
        """BPS from PBW gives Omega(n) = n for C^3."""
        pbw = PBWFiltration(jordan_quiver(), N=10)
        bps = pbw.bps_dimensions(8)
        for n in range(1, 8):
            assert bps[n] == n

    def test_local_p2_bps_from_pbw(self):
        """BPS from PBW gives Omega(n) = 3 for local P^2."""
        pbw = PBWFiltration(local_p2_quiver(), N=10)
        bps = pbw.bps_dimensions(8)
        for n in range(1, 8):
            assert bps[n] == 3

    def test_sym_0_is_ground_field(self):
        """Sym^0(BPS) = ground field (dim 1 at weight 0)."""
        pbw = PBWFiltration(jordan_quiver(), N=10)
        sym0 = pbw.sym_k_bps_character(0)
        assert sym0[0] == Fraction(1)
        for n in range(1, 10):
            assert sym0[n] == Fraction(0)

    def test_sym_1_is_bps(self):
        """Sym^1(BPS) = BPS itself."""
        pbw = PBWFiltration(jordan_quiver(), N=10)
        sym1 = pbw.sym_k_bps_character(1)
        bps = pbw.bps_character
        for n in range(10):
            assert abs(sym1[n] - bps[n]) < Fraction(1, 10**8)

    def test_filtration_step_dims_jordan(self):
        """Filtration steps for C^3."""
        pbw = PBWFiltration(jordan_quiver(), N=10)
        steps = pbw.filtration_step_dims(3)
        # gr_0 = ground field
        assert steps[0][0] == 1
        assert all(steps[0][n] == 0 for n in range(1, min(10, len(steps[0]))))
        # gr_1 at weight n = Omega(n) = n
        for n in range(1, min(8, len(steps[1]))):
            assert steps[1][n] == n


# ================================================================
# 11. CHART CoHA TESTS (integrated per-chart computation)
# ================================================================

class TestChartCoHA:
    """Test the complete ChartCoHA class for each standard CY3."""

    def test_c3_chart_basic(self):
        chart = ChartCoHA(jordan_quiver(), N=10)
        assert chart.name == "Jordan (C^3)"
        assert chart.coha_dimension(0) == 1
        assert chart.coha_dimension(1) == 1
        assert chart.coha_dimension(2) == 3

    def test_c3_kappa(self):
        """kappa(C^3) = 1 (Heisenberg at k=1, AP48: NOT c/2)."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        assert chart.kappa() == Fraction(1)

    def test_conifold_kappa(self):
        """kappa(conifold) = 2."""
        chart = ChartCoHA(conifold_quiver(), N=10)
        assert chart.kappa() == Fraction(2)

    def test_local_p2_kappa(self):
        """kappa(local P^2) = 3."""
        chart = ChartCoHA(local_p2_quiver(), N=10)
        assert chart.kappa() == Fraction(3)

    def test_mckay_z2_kappa(self):
        """kappa(C^3/Z_2) = 2."""
        chart = ChartCoHA(mckay_zn_quiver(2), N=10)
        assert chart.kappa() == Fraction(2)

    def test_mckay_z3_kappa(self):
        """kappa(C^3/Z_3) = 3."""
        chart = ChartCoHA(mckay_zn_quiver(3), N=10)
        assert chart.kappa() == Fraction(3)

    def test_c3_shadow_genus_1(self):
        """F_1(C^3) = 1/24."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        assert chart.shadow_genus_1() == Fraction(1, 24)

    def test_conifold_shadow_genus_1(self):
        """F_1(conifold) = 2/24 = 1/12."""
        chart = ChartCoHA(conifold_quiver(), N=10)
        assert chart.shadow_genus_1() == Fraction(1, 12)

    def test_c3_shadow_genus_2(self):
        """F_2(C^3) = 7/5760."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        assert chart.shadow_genus_g(2) == Fraction(7, 5760)

    def test_conifold_shadow_genus_2(self):
        """F_2(conifold) = 2 * 7/5760 = 7/2880."""
        chart = ChartCoHA(conifold_quiver(), N=10)
        assert chart.shadow_genus_g(2) == Fraction(7, 2880)

    def test_c3_full_report_has_keys(self):
        chart = ChartCoHA(jordan_quiver(), N=8)
        report = chart.full_report()
        assert "chart" in report
        assert "coha_dimensions" in report
        assert "bps_dimensions" in report
        assert "kappa" in report
        assert "pbw_verification" in report

    def test_conifold_full_report(self):
        chart = ChartCoHA(conifold_quiver(), N=8)
        report = chart.full_report()
        assert report["kappa"] == Fraction(2)

    def test_c3_verify_pbw(self):
        chart = ChartCoHA(jordan_quiver(), N=10)
        result = chart.verify_pbw()
        assert result["pexp_match"] is True

    def test_conifold_verify_pbw(self):
        chart = ChartCoHA(conifold_quiver(), N=10)
        result = chart.verify_pbw()
        assert result["pexp_match"] is True

    def test_local_p2_full_report(self):
        chart = ChartCoHA(local_p2_quiver(), N=8)
        report = chart.full_report()
        assert report["kappa"] == Fraction(3)
        assert report["coha_dimensions"][0] == 1

    def test_mckay_z4_chart(self):
        chart = ChartCoHA(mckay_zn_quiver(4), N=8)
        assert chart.kappa() == Fraction(4)
        assert chart.shadow_genus_1() == Fraction(1, 6)

    def test_mckay_z5_chart(self):
        chart = ChartCoHA(mckay_zn_quiver(5), N=8)
        assert chart.kappa() == Fraction(5)


# ================================================================
# 12. BAR COMPLEX TESTS
# ================================================================

class TestChartBarComplex:
    """Test bar complex computation on each chart."""

    def test_jordan_euler_char_two_paths(self):
        """chi(B(CoHA(C^3))) = 1/M(q) computed two ways."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        bar = ChartBarComplex(chart, max_arity=6)
        result = bar.verify_euler_char()
        assert result["match"] is True

    def test_conifold_euler_char_two_paths(self):
        chart = ChartCoHA(conifold_quiver(), N=10)
        bar = ChartBarComplex(chart, max_arity=6)
        result = bar.verify_euler_char()
        assert result["match"] is True

    def test_local_p2_euler_char_two_paths(self):
        chart = ChartCoHA(local_p2_quiver(), N=8)
        bar = ChartBarComplex(chart, max_arity=5)
        result = bar.verify_euler_char()
        assert result["match"] is True

    def test_jordan_bar_inverse_is_product(self):
        """1/M(q) = prod(1-q^n)^n for C^3."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        bar = ChartBarComplex(chart)
        inv = bar.euler_char_from_inverse()
        # 1/M(q) first few: 1, -1, -2, -1, 0, 4, 4, ...
        assert int(inv[0]) == 1
        assert int(inv[1]) == -1
        assert int(inv[2]) == -2

    def test_bps_from_bar_h1(self):
        """BPS from bar H^1 matches PLog."""
        chart = ChartCoHA(jordan_quiver(), N=10)
        bar = ChartBarComplex(chart)
        bps = bar.bps_from_h1()
        for n in range(1, 10):
            assert bps[n] == Fraction(n)

    def test_arity_0_is_ground_field(self):
        chart = ChartCoHA(jordan_quiver(), N=8)
        bar = ChartBarComplex(chart)
        a0 = bar.arity_k_gf(0)
        assert a0[0] == Fraction(1)
        for n in range(1, 8):
            assert a0[n] == Fraction(0)

    def test_arity_1_is_augmentation(self):
        """Arity-1 bar component = CoHA_+ (augmentation ideal)."""
        chart = ChartCoHA(jordan_quiver(), N=8)
        bar = ChartBarComplex(chart)
        a1 = bar.arity_k_gf(1)
        assert a1[0] == Fraction(0)  # augmentation ideal
        assert a1[1] == Fraction(1)  # pp(1) = 1
        assert a1[2] == Fraction(3)  # pp(2) = 3


# ================================================================
# 13. CROSS-CHART CONSISTENCY TESTS
# ================================================================

class TestCrossChartConsistency:
    """Test cross-chart relations (kappa additivity, BPS, PBW)."""

    def test_kappa_additivity(self):
        result = cross_chart_kappa_additivity()
        assert result["all_consistent"] is True

    def test_mckay_kappa_scaling(self):
        result = cross_chart_kappa_additivity()
        assert result["mckay_scaling"] is True

    def test_conifold_kappa_relation(self):
        result = cross_chart_kappa_additivity()
        assert result["conifold_relation"] is True

    def test_p2_kappa_relation(self):
        result = cross_chart_kappa_additivity()
        assert result["p2_relation"] is True

    def test_bps_consistency(self):
        result = cross_chart_bps_consistency()
        assert result["c3_omega_is_n"] is True
        assert result["conifold_omega_is_n"] is True
        assert result["p2_omega_is_3"] is True

    def test_all_charts_pbw(self):
        result = all_charts_pbw_verification()
        assert result["all_pass"] is True

    def test_all_charts_full_report(self):
        reports = all_charts_full_report()
        assert len(reports) >= 5
        for name, report in reports.items():
            assert "coha_dimensions" in report
            assert "kappa" in report


# ================================================================
# 14. EULER FORM AND ANTISYMMETRY TESTS
# ================================================================

class TestEulerFormMatrix:
    """Test Euler form matrices for all quivers."""

    def test_jordan_euler_matrix(self):
        Q = jordan_quiver()
        data = euler_form_matrix(Q)
        assert data["euler_matrix"][(0, 0)] == -2

    def test_conifold_euler_matrix(self):
        Q = conifold_quiver()
        data = euler_form_matrix(Q)
        # chi(e_0, e_0) = 1, chi(e_0, e_1) = -2
        assert data["euler_matrix"][(0, 0)] == 1
        assert data["euler_matrix"][(0, 1)] == -2
        assert data["euler_matrix"][(1, 0)] == -2
        assert data["euler_matrix"][(1, 1)] == 1

    def test_conifold_antisymmetry(self):
        Q = conifold_quiver()
        data = euler_form_matrix(Q)
        # Antisymmetric = 0 for conifold (balanced arrows)
        assert data["antisymmetric_matrix"][(0, 1)] == 0

    def test_local_p2_euler_matrix(self):
        Q = local_p2_quiver()
        data = euler_form_matrix(Q)
        # chi(e_0, e_0) = 1 (no loops at vertex 0)
        assert data["euler_matrix"][(0, 0)] == 1
        # chi(e_0, e_1) = -3 (three arrows 0->1)
        assert data["euler_matrix"][(0, 1)] == -3

    def test_local_p2_antisymmetry(self):
        Q = local_p2_quiver()
        data = euler_form_matrix(Q)
        # <e_0, e_1> = chi(e_0,e_1) - chi(e_1,e_0)
        # = -3 - 0 = -3 (arrows only from 0 to 1, none from 1 to 0)
        assert data["antisymmetric_matrix"][(0, 1)] == -3


# ================================================================
# 15. CONIFOLD DETAILED TESTS
# ================================================================

class TestConifoldDetailed:
    """Detailed tests for the conifold CoHA."""

    def test_two_variable_character(self):
        char = conifold_two_variable_character(5)
        assert char[(0, 0)] == 1
        assert char[(1, 0)] == 1
        assert char[(0, 1)] == 1
        assert char[(1, 1)] == 1
        assert char[(2, 0)] == 2
        assert char[(0, 2)] == 2

    def test_wall_crossing(self):
        result = conifold_wall_crossing_formula(12)
        assert result["product_is_one"] is True

    def test_conifold_euler_form_balanced(self):
        """Conifold has balanced arrows: 2 each way, so chi symmetric."""
        Q = conifold_quiver()
        for d in range(1, 4):
            d1 = (d, 0)
            d2 = (0, d)
            # chi(d1, d2) = 0 - 2d^2 = -2d^2
            assert Q.euler_form(d1, d2) == -2 * d * d

    def test_conifold_virtual_dim(self):
        Q = conifold_quiver()
        # vdim(1,1) = rep_dim - gauge_dim = 4 - 2 = 2
        assert Q.virtual_dim((1, 1)) == 2
        # vdim(2,2) = 16 - 8 = 8
        assert Q.virtual_dim((2, 2)) == 8


# ================================================================
# 16. LOCAL P^2 DETAILED TESTS
# ================================================================

class TestLocalP2Detailed:
    """Detailed tests for the local P^2 CoHA."""

    def test_topological_vertex_check(self):
        result = local_p2_topological_vertex_check(8)
        assert result["match"] is True

    def test_hilb_p2_values(self):
        """chi(Hilb^d(P^2)): 1, 3, 9, 22, 51, 108, 221, 429."""
        hilb = _hilb_euler_chars(3, 8)
        expected = [1, 3, 9, 22, 51, 108, 221, 429]
        for i, e in enumerate(expected):
            assert hilb[i] == e

    def test_p2_virtual_dim(self):
        Q = local_p2_quiver()
        # vdim(1,1,1) = 9 - 3 = 6
        assert Q.virtual_dim((1, 1, 1)) == 6

    def test_p2_rep_space_dim(self):
        Q = local_p2_quiver()
        # 9 arrows, each 1*1 at (1,1,1) => 9
        assert Q.rep_space_dim((1, 1, 1)) == 9


# ================================================================
# 17. McKAY QUIVER TESTS
# ================================================================

class TestMcKayQuivers:
    """Tests for McKay quiver C^3/Z_n family."""

    def test_z2_kappa_equals_2(self):
        chart = ChartCoHA(mckay_zn_quiver(2), N=8)
        assert chart.kappa() == Fraction(2)

    def test_z3_kappa_equals_3(self):
        chart = ChartCoHA(mckay_zn_quiver(3), N=8)
        assert chart.kappa() == Fraction(3)

    def test_z4_kappa_equals_4(self):
        chart = ChartCoHA(mckay_zn_quiver(4), N=8)
        assert chart.kappa() == Fraction(4)

    def test_z5_kappa_equals_5(self):
        chart = ChartCoHA(mckay_zn_quiver(5), N=8)
        assert chart.kappa() == Fraction(5)

    def test_mckay_linear_kappa(self):
        """kappa(C^3/Z_n) = n (linear in n)."""
        for n in range(2, 8):
            chart = ChartCoHA(mckay_zn_quiver(n), N=8)
            assert chart.kappa() == Fraction(n)

    def test_mckay_diagonal_dims_match_c3(self):
        """On diagonal, McKay Z_n CoHA dims = pp(d) (same as C^3)."""
        pp = _plane_partition_counts(6)
        for n in [2, 3, 4]:
            chart = ChartCoHA(mckay_zn_quiver(n), N=8)
            for d in range(6):
                assert chart.coha_dimension(d) == pp[d]

    def test_mckay_shadow_genus_1(self):
        """F_1(Z_n) = n/24."""
        for n in [2, 3, 4, 5]:
            chart = ChartCoHA(mckay_zn_quiver(n), N=8)
            assert chart.shadow_genus_1() == Fraction(n, 24)


# ================================================================
# 18. FABER-PANDHARIPANDE INVARIANTS TESTS
# ================================================================

class TestFaberPandharipande:
    """Test Faber-Pandharipande shadow invariants."""

    def test_lambda_1(self):
        assert _faber_pandharipande(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert _faber_pandharipande(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert _faber_pandharipande(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        assert _faber_pandharipande(4) == Fraction(127, 154828800)

    def test_lambda_5(self):
        assert _faber_pandharipande(5) == Fraction(73, 3503554560)

    def test_lambda_positivity(self):
        """All lambda_g > 0 (from (x/2)/sin(x/2) having positive coefficients)."""
        for g in range(1, 8):
            assert _faber_pandharipande(g) > 0

    def test_lambda_decreasing(self):
        """lambda_g decreases with g."""
        for g in range(1, 7):
            assert _faber_pandharipande(g) > _faber_pandharipande(g + 1)

    def test_shadow_kappa_times_lambda(self):
        """F_g(Q) = kappa(Q) * lambda_g for each chart."""
        for quiver_fn, expected_kappa in [
            (jordan_quiver, 1),
            (conifold_quiver, 2),
            (local_p2_quiver, 3),
        ]:
            chart = ChartCoHA(quiver_fn(), N=8)
            for g in range(1, 4):
                assert chart.shadow_genus_g(g) == (
                    Fraction(expected_kappa) * _faber_pandharipande(g)
                )


# ================================================================
# 19. MULTI-PATH VERIFICATION TESTS
# ================================================================

class TestMultiPathVerification:
    """Three-path verification for each chart character (CLAUDE.md mandate)."""

    def test_jordan_three_paths(self):
        result = jordan_character_three_paths(12)
        assert result["all_match"] is True

    def test_conifold_three_paths(self):
        result = conifold_character_three_paths(10)
        assert result["all_match"] is True

    def test_local_p2_three_paths(self):
        result = local_p2_character_three_paths(8)
        assert result["all_match"] is True

    def test_jordan_path_1_vs_2(self):
        result = jordan_character_three_paths(15)
        assert result["match_12"] is True

    def test_jordan_path_2_vs_3(self):
        result = jordan_character_three_paths(15)
        assert result["match_23"] is True


# ================================================================
# 20. COMPREHENSIVE INTEGRATION TESTS
# ================================================================

class TestComprehensiveIntegration:
    """Full pipeline tests combining all components."""

    def test_c3_complete_pipeline(self):
        """C^3: quiver -> moduli -> phi -> BM -> CoHA -> BPS -> PBW -> shadow."""
        Q = jordan_quiver()
        assert Q.n_vertices == 1 and Q.n_arrows == 3

        # Moduli and vanishing
        M = ModuliStack(Q, (3,))
        assert M.rep_space_dim == 27
        phi = VanishingCycleSheaf(Q, (3,))
        assert phi.bm_homology_dim() == 6  # pp(3) = 6

        # Chart CoHA
        chart = ChartCoHA(Q, N=10)
        assert chart.coha_dimensions(5) == [1, 1, 3, 6, 13, 24]
        assert chart.kappa() == Fraction(1)
        assert chart.shadow_genus_1() == Fraction(1, 24)

        # PBW
        pbw_result = chart.verify_pbw()
        assert pbw_result["pexp_match"] is True

        # Bar complex
        bar = ChartBarComplex(chart, max_arity=5)
        ec_result = bar.verify_euler_char()
        assert ec_result["match"] is True

    def test_conifold_complete_pipeline(self):
        """Conifold: full pipeline."""
        Q = conifold_quiver()
        chart = ChartCoHA(Q, N=10)

        # Dimensions on diagonal
        pp = _plane_partition_counts(6)
        for d in range(6):
            assert chart.coha_dimension(d) == pp[d]

        # kappa = 2
        assert chart.kappa() == Fraction(2)
        assert chart.shadow_genus_1() == Fraction(1, 12)

        # PBW
        assert chart.verify_pbw()["pexp_match"] is True

    def test_local_p2_complete_pipeline(self):
        """Local P^2: full pipeline."""
        Q = local_p2_quiver()
        chart = ChartCoHA(Q, N=8)

        hilb = _hilb_euler_chars(3, 6)
        for d in range(6):
            assert chart.coha_dimension(d) == hilb[d]

        assert chart.kappa() == Fraction(3)
        assert chart.shadow_genus_1() == Fraction(1, 8)
        assert chart.verify_pbw()["pexp_match"] is True

    def test_mckay_family_pipeline(self):
        """McKay Z_n family: kappa scaling + PBW for n = 2, 3, 4."""
        for n in [2, 3, 4]:
            chart = ChartCoHA(mckay_zn_quiver(n), N=8)
            assert chart.kappa() == Fraction(n)
            assert chart.verify_pbw()["pexp_match"] is True

    def test_shadow_genus_additivity_across_charts(self):
        """F_g is proportional to kappa across all charts."""
        lambda_1 = _faber_pandharipande(1)
        lambda_2 = _faber_pandharipande(2)
        for quiver_fn, k in [
            (jordan_quiver, 1), (conifold_quiver, 2),
            (local_p2_quiver, 3),
        ]:
            chart = ChartCoHA(quiver_fn(), N=8)
            assert chart.shadow_genus_g(1) == Fraction(k) * lambda_1
            assert chart.shadow_genus_g(2) == Fraction(k) * lambda_2

    def test_bar_euler_all_charts(self):
        """Bar complex Euler characteristic for all standard charts."""
        for quiver_fn in [jordan_quiver, conifold_quiver, local_p2_quiver]:
            chart = ChartCoHA(quiver_fn(), N=8)
            bar = ChartBarComplex(chart, max_arity=5)
            result = bar.verify_euler_char()
            assert result["match"] is True

    def test_cross_chart_consistency_full(self):
        """All cross-chart consistency checks pass."""
        assert cross_chart_kappa_additivity()["all_consistent"] is True
        assert cross_chart_bps_consistency()["c3_omega_is_n"] is True
        assert all_charts_pbw_verification()["all_pass"] is True

    def test_mckay_z2_explicit_report(self):
        chart = ChartCoHA(mckay_z2_quiver(), N=8)
        assert chart.kappa() == Fraction(2)
        dims = chart.coha_dimensions(5)
        pp = _plane_partition_counts(6)
        for d in range(6):
            assert dims[d] == pp[d]


# ================================================================
# 21. EDGE CASES AND BOUNDARY TESTS
# ================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_dimension_zero(self):
        """CoHA at d=0 is the ground field (dim 1)."""
        for quiver_fn in [jordan_quiver, conifold_quiver, local_p2_quiver]:
            chart = ChartCoHA(quiver_fn(), N=8)
            assert chart.coha_dimension(0) == 1

    def test_dimension_one(self):
        """CoHA at d=1 has known dimension."""
        assert _jordan_coha_dim(1) == 1  # pp(1) = 1
        assert _conifold_coha_dim(1, 1) == 1  # pp(1) = 1
        # Local P^2 at (1,1,1): chi(Hilb^1(P^2)) = 3 (three fixed points)
        assert _local_p2_coha_dim(1, 1, 1) == 3

    def test_negative_dimension(self):
        assert _jordan_coha_dim(-1) == 0

    def test_faber_pandharipande_computed_matches_hardcoded(self):
        """Verify that the power series computation matches hardcoded values."""
        for g in [1, 2, 3, 4, 5]:
            computed = _faber_pandharipande(g)
            # Recompute independently from scratch
            M = 2 * g + 2
            f = _fps_zero(M)
            for k in range(M // 2 + 1):
                if 2 * k < M:
                    denom = 1
                    for j in range(1, 2 * k + 2):
                        denom *= j
                    f[2 * k] = Fraction((-1) ** k, (2 ** (2 * k)) * denom)
            inv_f = _fps_inv(f, M)
            if 2 * g < M:
                assert computed == inv_f[2 * g], (
                    f"FP mismatch at g={g}: {computed} vs {inv_f[2*g]}"
                )

    def test_mobius_sieve_small_values(self):
        """Verify Mobius function at small values."""
        mu = _mobius_sieve(10)
        assert mu[1] == 1
        assert mu[2] == -1
        assert mu[3] == -1
        assert mu[4] == 0  # 4 = 2^2, square factor
        assert mu[5] == -1
        assert mu[6] == 1  # 6 = 2*3, even number of prime factors

    def test_large_partition_count(self):
        """p(20) = 627 (OEIS)."""
        pc = _partition_counts(21)
        assert pc[20] == 627

    def test_large_plane_partition_count(self):
        """pp(10) = 500 (OEIS A000219)."""
        pp = _plane_partition_counts(11)
        assert pp[10] == 500
