r"""Tests for crystal bases from the E_1 bar filtration of CY3 chiral algebras.

THEOREM BEING TESTED:
    The crystal limit q -> 0 of the CoHA = Y^+(gl_hat_1) gives the
    Kashiwara crystal B(infinity), whose elements are plane partitions.

    The E_1 bar complex B^{E_1}(CoHA) has a natural filtration from
    the bar degree (tensor degree), and the associated graded
    gr_F B^{E_1} = crystal lattice L(infinity).

MULTI-PATH VERIFICATION (3+ paths per claim, per CLAUDE.md mandate):
    Path 1: Direct combinatorial construction of crystal elements
    Path 2: Generating function match (crystal char = CoHA char = MacMahon)
    Path 3: Crystal graph structure (highest weight, reachability, inverses)
    Path 4: Bar filtration consistency (Euler characteristic, PBW)
    Path 5: Cross-geometry verification (conifold, local P^2)
    Path 6: Tensor product from E_1 bar decomposition
    Path 7: Literature values (OEIS A000219, Goettsche, Kashiwara)

REFERENCES:
    Kashiwara (1990): Crystal bases for quantum groups
    Okounkov-Reshetikhin-Vafa (2003): Crystal melting / DT
    Schiffmann-Vasserot (2012): CoHA(C^3) = Y^+(gl_hat_1)
    Davison-Meinhardt (2015): PBW theorem for CoHA
    OEIS A000219: plane partition counts
    Goettsche (1990): chi(Hilb^n(S)) formula
"""

import pytest
from fractions import Fraction

from compute.lib.crystal_from_e1_bar_filtration import (
    # Plane partition primitives
    pp_empty,
    pp_size,
    pp_addable_boxes,
    pp_removable_boxes,
    pp_add_box,
    pp_remove_box,
    pp_color,
    pp_weight,
    pp_crystal_f0,
    pp_crystal_e0,
    pp_string_length_e0,
    pp_string_length_f0,
    _pp_to_canonical,
    _canonical_to_mutable,
    # Crystal enumeration
    c3_crystal_elements,
    c3_crystal_count_by_size,
    c3_crystal_character,
    verify_c3_crystal_character,
    # Crystal graph
    c3_crystal_graph,
    verify_c3_crystal_graph,
    # Bar filtration
    bar_filtration_crystal_dims,
    bar_associated_graded_character,
    bar_euler_char_crystal,
    verify_bar_filtration_crystal,
    # Conifold
    conifold_crystal_element,
    conifold_crystal_weight,
    conifold_crystal_diagonal_char,
    conifold_crystal_single_vertex_char,
    conifold_bps_crystal,
    verify_conifold_crystal_character,
    # Local P^2
    local_p2_crystal_element,
    local_p2_crystal_char,
    local_p2_bps_crystal,
    verify_local_p2_crystal_character,
    # Chart gluing
    tropical_wall_crossing,
    conifold_crystal_gluing,
    # Tensor product
    crystal_tensor_product_char,
    crystal_tensor_decomposition_sl2,
    verify_tensor_product_from_bar,
    # Littelmann
    littelmann_path_count,
    littelmann_crystal_bijection_sl2,
    chart_transition_paths,
    # Kashiwara data
    kashiwara_data_c3,
    crystal_string_data_c3,
    # Full verification
    full_crystal_verification,
)

from compute.lib.coha_chart_explicit import (
    _macmahon,
    _partition_counts,
    _plane_partition_counts,
    _fps_inv,
    _fps_zero,
    _fps_one,
    _fps_mul,
    plethystic_log,
)


# ================================================================
# 0. PLANE PARTITION PRIMITIVES
# ================================================================

class TestPlanePartitionPrimitives:
    """Test basic plane partition operations."""

    def test_empty_partition(self):
        """Empty partition has size 0."""
        assert pp_empty() == ()
        assert pp_size(pp_empty()) == 0

    def test_canonical_form(self):
        """Canonical form strips trailing zeros and empty rows."""
        pp = _pp_to_canonical([[1, 0], [0]])
        assert pp == ((1,),)

        pp2 = _pp_to_canonical([[2, 1], [1]])
        assert pp2 == ((2, 1), (1,))

        pp3 = _pp_to_canonical([[0]])
        assert pp3 == ()

    def test_roundtrip_canonical(self):
        """Canonical -> mutable -> canonical is idempotent."""
        cases = [
            ((2, 1), (1,)),
            ((3, 2, 1),),
            ((1,), (1,)),
            (),
        ]
        for pp in cases:
            mut = _canonical_to_mutable(pp)
            back = _pp_to_canonical(mut)
            assert back == pp, f"Roundtrip failed for {pp}"

    def test_size_computation(self):
        """Size = sum of all entries."""
        assert pp_size(()) == 0
        assert pp_size(((1,),)) == 1
        assert pp_size(((2, 1), (1,))) == 4
        assert pp_size(((3, 2, 1),)) == 6

    def test_addable_boxes_empty(self):
        """Empty partition has exactly one addable box: (0, 0, 1)."""
        addable = pp_addable_boxes(pp_empty())
        assert (0, 0, 1) in addable

    def test_addable_boxes_single(self):
        """Single box partition: three addable positions."""
        pp = ((1,),)
        addable = pp_addable_boxes(pp)
        # Can add at (0,0) -> height 2, (0,1) -> height 1, (1,0) -> height 1
        assert (0, 0, 2) in addable
        assert (0, 1, 1) in addable
        assert (1, 0, 1) in addable

    def test_removable_boxes_empty(self):
        """Empty partition has no removable boxes."""
        assert pp_removable_boxes(pp_empty()) == []

    def test_removable_boxes_single(self):
        """Single box partition: one removable box."""
        pp = ((1,),)
        removable = pp_removable_boxes(pp)
        assert len(removable) == 1
        assert removable[0] == (0, 0, 1)

    def test_add_remove_inverse(self):
        """Adding then removing at the same position is identity."""
        pp = ((2, 1), (1,))
        addable = pp_addable_boxes(pp)
        for (i, j, k) in addable:
            new_pp = pp_add_box(pp, i, j)
            back = pp_remove_box(new_pp, i, j)
            assert back == pp, f"Add-remove at ({i},{j}) failed"

    def test_remove_add_inverse(self):
        """Removing then adding at the same position is identity."""
        pp = ((2, 1), (1,))
        removable = pp_removable_boxes(pp)
        for (i, j, k) in removable:
            new_pp = pp_remove_box(pp, i, j)
            back = pp_add_box(new_pp, i, j)
            assert back == pp, f"Remove-add at ({i},{j}) failed"


# ================================================================
# 1. CRYSTAL OPERATORS
# ================================================================

class TestCrystalOperators:
    """Test Kashiwara crystal operators e_0, f_0."""

    def test_e0_on_empty(self):
        """e_0 on empty partition returns None (highest weight)."""
        assert pp_crystal_e0(pp_empty()) is None

    def test_f0_on_empty(self):
        """f_0 on empty partition gives a single-box partition."""
        result = pp_crystal_f0(pp_empty())
        assert len(result) == 1
        assert pp_size(result[0]) == 1

    def test_e0_f0_inverse(self):
        """e_0(f_0(b)) = b for small partitions."""
        for pp in c3_crystal_elements(4):
            f_results = pp_crystal_f0(pp)
            for f_pp in f_results:
                e_back = pp_crystal_e0(f_pp)
                assert e_back == pp, (
                    f"e_0(f_0({pp})) = {e_back} != {pp}"
                )

    def test_weight_is_negative_size(self):
        """Weight = (-|pi|,) for gl_hat_1."""
        assert pp_weight(pp_empty()) == (0,)
        assert pp_weight(((1,),)) == (-1,)
        assert pp_weight(((2, 1), (1,))) == (-4,)

    def test_string_length_e0(self):
        """epsilon_0(b) = |b| (size of partition)."""
        for pp in c3_crystal_elements(5):
            assert pp_string_length_e0(pp) == pp_size(pp)

    def test_color_trivial(self):
        """All boxes have color 0 for gl_hat_1."""
        for i in range(5):
            for j in range(5):
                for k in range(1, 5):
                    assert pp_color(i, j, k) == 0


# ================================================================
# 2. CRYSTAL ENUMERATION AND CHARACTER (C^3)
# ================================================================

class TestC3CrystalEnumeration:
    """Test crystal element enumeration for C^3."""

    def test_crystal_count_small(self):
        """Crystal counts match plane partition counts.

        OEIS A000219: 1, 1, 3, 6, 13, 24, 48, 86, 160, ...
        """
        counts = c3_crystal_count_by_size(8)
        expected = [1, 1, 3, 6, 13, 24, 48, 86, 160]
        assert counts == expected, f"Got {counts}, expected {expected}"

    def test_crystal_character_eq_macmahon(self):
        """Crystal character = MacMahon function M(q).

        Path 1: Crystal enumeration.
        Path 2: MacMahon product formula.
        """
        result = verify_c3_crystal_character(7)
        assert result["all_match"], (
            f"Crystal/MacMahon/CoHA mismatch: {result}"
        )

    def test_crystal_character_multipath(self):
        """Three independent paths all give the same character."""
        result = verify_c3_crystal_character(6)
        assert result["crystal_eq_macmahon"]
        assert result["crystal_eq_coha"]
        assert result["macmahon_eq_coha"]

    def test_crystal_elements_at_size_0(self):
        """Size 0: just the empty partition."""
        elts = [pp for pp in c3_crystal_elements(3) if pp_size(pp) == 0]
        assert len(elts) == 1
        assert elts[0] == pp_empty()

    def test_crystal_elements_at_size_1(self):
        """Size 1: just the single-box partition ((1,),)."""
        elts = [pp for pp in c3_crystal_elements(3) if pp_size(pp) == 1]
        assert len(elts) == 1
        assert elts[0] == ((1,),)

    def test_crystal_elements_at_size_2(self):
        """Size 2: three plane partitions.

        ((2,),), ((1, 1),), ((1,), (1,))
        """
        elts = [pp for pp in c3_crystal_elements(3) if pp_size(pp) == 2]
        assert len(elts) == 3


# ================================================================
# 3. CRYSTAL GRAPH STRUCTURE
# ================================================================

class TestC3CrystalGraph:
    """Test crystal graph properties."""

    def test_unique_highest_weight(self):
        """B(infinity) has a unique highest weight = empty partition."""
        result = verify_c3_crystal_graph(5)
        assert result["unique_highest_weight"]

    def test_all_reachable(self):
        """Every crystal element is reachable from the empty partition."""
        result = verify_c3_crystal_graph(5)
        assert result["all_reachable"]

    def test_e_f_partial_inverse(self):
        """e_0(f_0(b)) = b for all b."""
        result = verify_c3_crystal_graph(4)
        assert result["e_f_inverse"]

    def test_graph_edges_consistent(self):
        """Number of edges = number of elements with size < max_size.

        The canonical f_0 operator is single-valued, so each element
        of size < max_size contributes exactly one outgoing edge.
        Verify this by two independent counts.
        """
        max_size = 4
        graph = c3_crystal_graph(max_size)
        elements = c3_crystal_elements(max_size)
        n_below_max = sum(1 for p in elements if pp_size(p) < max_size)
        assert graph["n_edges"] == n_below_max, (
            f"n_edges={graph['n_edges']} != n_below_max={n_below_max}"
        )


# ================================================================
# 4. BAR FILTRATION AND CRYSTAL LATTICE
# ================================================================

class TestBarFiltrationCrystal:
    """Test bar filtration F_k B^{E_1} and associated graded."""

    def test_gr_0_is_ground_field(self):
        """gr_0 = ground field (1-dim at weight 0, 0 elsewhere)."""
        dims = bar_filtration_crystal_dims(8)
        assert dims[0][0] == 1
        for n in range(1, 9):
            assert dims[0][n] == 0

    def test_gr_1_is_augmentation_ideal(self):
        """gr_1 = CoHA_+ = M(q) - 1.

        Path 1: Bar filtration.
        Path 2: MacMahon minus 1.
        """
        dims = bar_filtration_crystal_dims(8)
        N = 9
        mac = _macmahon(N)
        aug = [int(mac[n]) for n in range(N)]
        aug[0] = 0
        for n in range(N):
            assert dims[1][n] == aug[n], f"Mismatch at n={n}"

    def test_bar_euler_char_is_inverse_macmahon(self):
        """chi(B^{E_1}) = 1/M(q) = prod(1-q^n)^n.

        Path 1: Alternating sum of bar dimensions.
        Path 2: Power series inversion of MacMahon.
        Path 3: Direct product formula.
        """
        N = 10
        # Path 1: from bar filtration
        euler_bar = bar_euler_char_crystal(N - 1)

        # Path 2: inverse MacMahon
        mac = _macmahon(N)
        inv_mac = _fps_inv(mac, N)

        # Path 3: direct product
        direct = [Fraction(0)] * N
        direct[0] = Fraction(1)
        for m in range(1, N):
            for _ in range(m):
                for j in range(N - 1, m - 1, -1):
                    direct[j] -= direct[j - m]

        for n in range(N):
            assert euler_bar[n] == inv_mac[n], (
                f"Bar Euler != inv MacMahon at n={n}: "
                f"{euler_bar[n]} != {inv_mac[n]}"
            )
            assert inv_mac[n] == direct[n], (
                f"inv MacMahon != direct at n={n}"
            )

    def test_bps_generators(self):
        """PLog(M(q)) = sum n q^n (BPS = n generators at weight n)."""
        N = 12
        mac = _macmahon(N)
        bps = plethystic_log(list(mac), N)
        for n in range(1, N):
            assert abs(bps[n] - Fraction(n)) < Fraction(1, 10**6), (
                f"BPS[{n}] = {bps[n]}, expected {n}"
            )

    def test_bar_filtration_full_verification(self):
        """Full bar filtration verification."""
        result = verify_bar_filtration_crystal(8)
        assert result["all_pass"], f"Bar filtration failed: {result}"

    def test_associated_graded_character(self):
        """gr_k character = (M(q)-1)^k.

        Verify for k=2,3 against explicit computation.
        """
        N = 9
        mac = _macmahon(N)
        aug = list(mac)
        aug[0] = Fraction(0)

        for k in [2, 3]:
            gr_k = bar_associated_graded_character(k, N - 1)
            expected = _fps_one(N)
            base = list(aug)
            result = base
            for _ in range(k - 1):
                result = _fps_mul(result, base, N)
            for n in range(N):
                assert gr_k[n] == result[n], (
                    f"gr_{k}[{n}] mismatch: {gr_k[n]} != {result[n]}"
                )


# ================================================================
# 5. CONIFOLD CRYSTAL
# ================================================================

class TestConifoldCrystal:
    """Test 2-colored crystal for the resolved conifold."""

    def test_diagonal_is_plane_partitions(self):
        """Diagonal (d, d) crystal count = pp(d).

        Path 1: Crystal count.
        Path 2: Plane partition count (OEIS A000219).
        """
        pp_counts = _plane_partition_counts(8)
        for d in range(8):
            assert conifold_crystal_element(d, d) == pp_counts[d], (
                f"Conifold crystal({d},{d}) = {conifold_crystal_element(d,d)}"
                f" != pp({d}) = {pp_counts[d]}"
            )

    def test_single_vertex_is_partitions(self):
        """Single-vertex (d, 0) crystal count = p(d).

        Path 1: Crystal count.
        Path 2: Partition count (OEIS A000041).
        """
        p_counts = _partition_counts(8)
        for d in range(8):
            assert conifold_crystal_element(d, 0) == p_counts[d], (
                f"Conifold crystal({d},0) = {conifold_crystal_element(d,0)}"
                f" != p({d}) = {p_counts[d]}"
            )

    def test_symmetry(self):
        """Crystal count is symmetric: crystal(d1, d2) = crystal(d2, d1)."""
        for d1 in range(6):
            for d2 in range(6):
                assert conifold_crystal_element(d1, d2) == \
                       conifold_crystal_element(d2, d1), (
                    f"Asymmetry at ({d1},{d2})"
                )

    def test_weight(self):
        """Weight of conifold crystal element."""
        assert conifold_crystal_weight(3, 2) == (-3, -2)
        assert conifold_crystal_weight(0, 0) == (0, 0)

    def test_bps_structure(self):
        """BPS invariants: Omega(n,0) = n, Omega(0,n) = n, Omega(n,n) = 1."""
        bps = conifold_bps_crystal(5)
        for n in range(1, 6):
            assert bps[(n, 0)] == n, f"Omega({n},0) = {bps[(n,0)]}"
            assert bps[(0, n)] == n, f"Omega(0,{n}) = {bps[(0,n)]}"
            assert bps[(n, n)] == 1, f"Omega({n},{n}) = {bps[(n,n)]}"

    def test_conifold_character_multipath(self):
        """Three-path verification of conifold crystal character."""
        result = verify_conifold_crystal_character(8)
        assert result["all_match"], f"Conifold crystal mismatch: {result}"

    def test_diagonal_char_is_macmahon(self):
        """Diagonal character = M(q)."""
        N = 10
        diag_char = conifold_crystal_diagonal_char(N)
        mac = _macmahon(N)
        for n in range(N):
            assert diag_char[n] == mac[n]


# ================================================================
# 6. LOCAL P^2 CRYSTAL
# ================================================================

class TestLocalP2Crystal:
    """Test 3-colored crystal for local P^2."""

    def test_symmetric_diagonal_values(self):
        """chi(Hilb^d(P^2)) matches known values.

        OEIS / Goettsche: 1, 3, 9, 22, 51, 108, 221, 429
        """
        expected = [1, 3, 9, 22, 51, 108, 221, 429]
        for d, exp in enumerate(expected):
            assert local_p2_crystal_element(d) == exp, (
                f"Local P^2 crystal({d}) = {local_p2_crystal_element(d)}"
                f" != {exp}"
            )

    def test_bps_is_3(self):
        """BPS invariants: Omega(d,d,d) = 3 for d >= 1.

        chi(P^2) = 3, reflecting three torus fixed points.
        """
        bps = local_p2_bps_crystal(5)
        for d in range(1, 6):
            assert bps[(d, d, d)] == 3

    def test_character_is_goettsche(self):
        """Character = prod 1/(1-q^n)^3 (Goettsche with chi=3)."""
        N = 10
        crystal_char = local_p2_crystal_char(N)
        # Direct product computation
        goettsche = _fps_one(N)
        for k in range(1, N):
            for _ in range(3):
                for n in range(k, N):
                    goettsche[n] += goettsche[n - k]
        for n in range(N):
            assert crystal_char[n] == goettsche[n]

    def test_local_p2_multipath(self):
        """Three-path verification of local P^2 crystal character."""
        result = verify_local_p2_crystal_character(8)
        assert result["all_match"], f"Local P^2 mismatch: {result}"


# ================================================================
# 7. CHART GLUING AT CRYSTAL LEVEL
# ================================================================

class TestChartGluing:
    """Test crystal-level chart gluing via tropical wall-crossing."""

    def test_conifold_gluing_all_pass(self):
        """Full conifold gluing verification."""
        result = conifold_crystal_gluing(10)
        assert result["all_pass"], f"Conifold gluing failed: {result}"

    def test_wall_crossing_product_identity(self):
        """1/M(q) * M(q) = 1 (wall-crossing involution on diagonal)."""
        result = conifold_crystal_gluing(10)
        assert result["wc_product_is_identity"]

    def test_colimit_is_macmahon(self):
        """Colimit crystal character = M(q) on diagonal."""
        result = conifold_crystal_gluing(10)
        assert result["colimit_matches_macmahon"]

    def test_tropical_wall_crossing_trivial(self):
        """Tropical KW with identical BPS on both sides is identity."""
        N = 10
        bps = {n: n for n in range(1, N)}
        ratio = tropical_wall_crossing(bps, bps, N)
        for n in range(N):
            expected = Fraction(1) if n == 0 else Fraction(0)
            assert abs(ratio[n] - expected) < Fraction(1, 10**8), (
                f"Tropical KW not identity at n={n}: {ratio[n]}"
            )


# ================================================================
# 8. TENSOR PRODUCT FROM E_1
# ================================================================

class TestTensorProduct:
    """Test crystal tensor product rule from E_1 bar filtration."""

    def test_bar_euler_product(self):
        """chi(B(A1 tensor A2)) = chi(B(A1)) * chi(B(A2)) = 1/M^2.

        Path 1: Direct product of inverse MacMahon.
        Path 2: Inverse of M^2.
        Path 3: Direct product formula prod(1-q^n)^{2n}.
        """
        result = verify_tensor_product_from_bar(10)
        assert result["all_match"], f"Tensor product failed: {result}"

    def test_tensor_product_character_is_product(self):
        """char(B1 x B2) = char(B1) * char(B2)."""
        N = 10
        mac = _macmahon(N)
        char1 = list(mac)
        char2 = list(mac)
        product = crystal_tensor_product_char(char1, char2, N)
        mac_sq = _fps_mul(mac, mac, N)
        for n in range(N):
            assert product[n] == mac_sq[n]

    def test_sl2_tensor_sizes(self):
        """sl_2 tensor product: |B(V) x B(V)| = 4 = 2 * 2."""
        result = crystal_tensor_decomposition_sl2(10)
        assert result["size_match"]
        assert result["tensor_total"] == 4
        assert result["decomp_total"] == 4

    def test_sl2_fundamental_character(self):
        """B(omega) for sl_2 has 2 elements: char = 1 + q."""
        result = crystal_tensor_decomposition_sl2(10)
        assert result["fund_char"][:3] == [1, 1, 0]

    def test_sl2_tensor_character(self):
        """(1+q)^2 = 1 + 2q + q^2."""
        result = crystal_tensor_decomposition_sl2(10)
        assert result["tensor_char"][:4] == [1, 2, 1, 0]


# ================================================================
# 9. LITTELMANN PATHS
# ================================================================

class TestLittelmannPaths:
    """Test Littelmann path model correspondence."""

    def test_sl2_catalan(self):
        """sl_2 Littelmann path counts = Catalan numbers.

        C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42
        """
        expected_catalan = [1, 1, 2, 5, 14, 42]
        for n, exp in enumerate(expected_catalan):
            assert littelmann_path_count(1, n) == exp, (
                f"Catalan({n}) = {littelmann_path_count(1, n)} != {exp}"
            )

    def test_sl2_crystal_path_bijection(self):
        """Littelmann paths biject with crystal elements for sl_2."""
        result = littelmann_crystal_bijection_sl2(8)
        assert result["all_match"]

    def test_sl3_fuss_catalan(self):
        """sl_3 path counts = Fuss-Catalan numbers.

        C^(3)_n = C(3n, n) / (2n + 1)
        """
        import math
        for n in range(6):
            expected = math.comb(3 * n, n) // (2 * n + 1)
            assert littelmann_path_count(2, n) == expected

    def test_chart_transition_conifold(self):
        """Conifold chart transition: 1 wall, trivial on diagonal."""
        result = chart_transition_paths(5)
        assert result["n_walls"] == 1
        assert result["transition_trivial_on_diagonal"]


# ================================================================
# 10. KASHIWARA DATA
# ================================================================

class TestKashiwaraData:
    """Test Kashiwara crystal data for C^3."""

    def test_empty_partition_data(self):
        """Kashiwara data for the empty partition (highest weight)."""
        data = kashiwara_data_c3(pp_empty())
        assert data["size"] == 0
        assert data["weight"] == (0,)
        assert data["epsilon_0"] == 0
        assert data["e_0"] is None
        assert data["f_0"] is not None

    def test_single_box_data(self):
        """Kashiwara data for the single-box partition."""
        pp = ((1,),)
        data = kashiwara_data_c3(pp)
        assert data["size"] == 1
        assert data["weight"] == (-1,)
        assert data["epsilon_0"] == 1
        assert data["e_0"] == pp_empty()

    def test_string_data_consistency(self):
        """String data: epsilon_0(b) = |b| for all elements."""
        data = crystal_string_data_c3(4)
        for pp, info in data.items():
            assert info["epsilon_0"] == info["size"]


# ================================================================
# 11. COMPREHENSIVE VERIFICATION
# ================================================================

class TestFullVerification:
    """Run the full crystal verification suite."""

    def test_full_verification(self):
        """All verification checks pass."""
        result = full_crystal_verification(max_size=5, N=8)
        assert result["all_pass"], (
            f"Full verification failed. Failing components: "
            + ", ".join(
                k for k, v in result.items()
                if isinstance(v, dict) and not v.get("all_match",
                    v.get("all_pass",
                    v.get("unique_highest_weight",
                    v.get("size_match", True))))
            )
        )


# ================================================================
# 12. CROSS-GEOMETRY CONSISTENCY
# ================================================================

class TestCrossGeometryConsistency:
    """Verify consistency across C^3, conifold, local P^2."""

    def test_c3_and_conifold_diagonal_agree(self):
        """C^3 crystal = conifold diagonal crystal (both = M(q)).

        Path 1: C^3 crystal count.
        Path 2: Conifold diagonal crystal count.
        Path 3: MacMahon coefficients.
        """
        N = 8
        c3 = c3_crystal_count_by_size(N - 1)
        conifold_diag = [conifold_crystal_element(d, d) for d in range(N)]
        mac = _macmahon(N)
        mac_int = [int(mac[d]) for d in range(N)]

        assert c3 == mac_int, "C^3 crystal != MacMahon"
        assert conifold_diag == mac_int, "Conifold diagonal != MacMahon"

    def test_bps_scaling_relation(self):
        """BPS invariants scale with chi(S) for toric surfaces.

        C^3 (chi=1): Omega(n) = n
        Local P^2 (chi=3): Omega(n) = 3
        """
        N = 8
        mac = _macmahon(N)
        bps_c3 = plethystic_log(list(mac), N)
        for n in range(1, N):
            assert abs(bps_c3[n] - Fraction(n)) < Fraction(1, 10**6)

        p2_char = local_p2_crystal_char(N)
        bps_p2 = plethystic_log(p2_char, N)
        for n in range(1, N):
            assert abs(bps_p2[n] - Fraction(3)) < Fraction(1, 10**6)

    def test_inverse_macmahon_across_geometries(self):
        """1/M(q) = prod(1-q^n)^n is the bar Euler char for C^3.

        Computed coefficients verified by three paths:
        Path 1: bar_euler_char_crystal (power series inversion).
        Path 2: Direct product formula prod(1-q^n)^n.
        Path 3: Hardcoded OEIS values.
        """
        N = 10
        # Path 1: bar Euler characteristic
        inv_mac = bar_euler_char_crystal(N - 1)

        # Path 2: direct product prod(1-q^n)^n
        direct = [Fraction(0)] * N
        direct[0] = Fraction(1)
        for m in range(1, N):
            for _ in range(m):
                for j in range(N - 1, m - 1, -1):
                    direct[j] -= direct[j - m]

        # Path 3: OEIS A000219 inverse (signed)
        # 1/M(q) = 1 - q - 2q^2 - q^3 + 4q^5 + 4q^6 + 7q^7 + 3q^8 - 2q^9 - ...
        expected_start = [1, -1, -2, -1, 0, 4, 4, 7, 3, -2]

        for n in range(min(N, len(expected_start))):
            assert int(inv_mac[n]) == expected_start[n], (
                f"1/M(q)[{n}] = {int(inv_mac[n])} != {expected_start[n]}"
            )
            assert int(direct[n]) == expected_start[n], (
                f"direct[{n}] = {int(direct[n])} != {expected_start[n]}"
            )
            assert inv_mac[n] == direct[n], (
                f"Path 1 != Path 2 at n={n}"
            )
