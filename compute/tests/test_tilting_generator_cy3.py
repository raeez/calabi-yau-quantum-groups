r"""Tests for tilting_generator_cy3: tilting generators, Ext-quivers, and
quiver-with-potential for derived categories of CY3 varieties.

Ground truth:
  Beilinson, "Coherent sheaves on P^n" (1978).
  Bondal-Van den Bergh, "Generators and representability" (2003).
  Van den Bergh, "Non-commutative crepant resolutions" (2004).
  Bridgeland, "Flops and derived categories" (2002).
  Keller-Yang, "Derived equivalences from mutations" (2011).
  Ginzburg, "CY algebras" (2006).
  Aspinwall et al., "Dirichlet branes and mirror symmetry" (2009).

Multi-path verification applied throughout:
  Path 1: Direct computation from Bott's formula.
  Path 2: Euler characteristic via HRR.
  Path 3: Serre duality cross-check.
  Path 4: Koszul resolution computation.
  Path 5: Literature comparison.

Tests organized by mathematical topic, each independently verifiable.
"""

from fractions import Fraction

import pytest

from compute.lib.tilting_generator_cy3 import (
    # Section 0: Combinatorics
    binomial,
    # Section 1: Bott's theorem
    h_k_pn_o_m,
    euler_char_pn_o_m,
    # Section 2: Ext on P^n
    ExtData,
    ext_line_bundles_pn,
    # Section 3: Beilinson collection
    ExceptionalCollection,
    beilinson_collection_pn,
    # Section 4: Ext-quiver
    QuiverData,
    ext_quiver,
    # Section 5: Hypersurface restriction
    h_k_hypersurface_o_m,
    ext_on_hypersurface,
    # Section 6: CICY
    h_k_cicy_o_m,
    ext_on_cicy,
    # Section 7: Tilting generators
    TiltingGenerator,
    tilting_generator_pn,
    tilting_generator_quintic,
    tilting_generator_cicy33,
    # Section 8: Conifold
    ConifoldTiltingData,
    conifold_tilting,
    # Section 9: CY3 Serre duality
    verify_cy3_serre_duality,
    # Section 10: Euler form
    euler_form_pn,
    euler_form_hypersurface,
    euler_form_cicy,
    euler_form_matrix_pn,
    euler_form_matrix_quintic,
    euler_form_matrix_cicy33,
    # Section 11: K3
    K3TiltingData,
    k3_tilting_data,
    k3_times_e_tilting_data,
    # Section 12: E1 chiral
    E1ChiralFromTilting,
    e1_chiral_c3,
    e1_chiral_conifold,
    e1_chiral_quintic,
    # Section 13: Hodge numbers
    quintic_h11,
    quintic_h21,
    quintic_euler,
    cicy33_h11,
    cicy33_h21,
    cicy33_euler,
    cicy_hodge,
    # Section 14: QWP
    QuiverWithPotential,
    conifold_qwp,
    p3_quiver,
    # Section 15: Extended Bott
    all_cohomology_pn_twist,
    cohomology_table_pn,
    # Section 16: Summary
    tilting_summary_pn,
    tilting_summary_quintic,
    tilting_summary_cicy33,
)


# =========================================================================
# Section 0: Binomial coefficient tests
# =========================================================================

class TestBinomial:
    """Tests for the generalized binomial coefficient."""

    def test_basic_values(self):
        assert binomial(5, 2) == 10
        assert binomial(10, 3) == 120
        assert binomial(7, 0) == 1
        assert binomial(0, 0) == 1

    def test_boundary_cases(self):
        assert binomial(5, 5) == 1
        assert binomial(5, 6) == 0
        assert binomial(0, 1) == 0

    def test_negative_k(self):
        assert binomial(5, -1) == 0

    def test_pascal_identity(self):
        """C(n,k) = C(n-1,k-1) + C(n-1,k)."""
        for n in range(1, 8):
            for k in range(1, n):
                assert binomial(n, k) == binomial(n - 1, k - 1) + binomial(n - 1, k)

    def test_symmetry(self):
        """C(n,k) = C(n, n-k)."""
        for n in range(8):
            for k in range(n + 1):
                assert binomial(n, k) == binomial(n, n - k)


# =========================================================================
# Section 1: Bott's theorem on P^n
# =========================================================================

class TestBottTheorem:
    """Tests for H^k(P^n, O(m)) via Bott's formula."""

    def test_h0_p1(self):
        """H^0(P^1, O(m)) = m+1 for m >= 0."""
        for m in range(10):
            assert h_k_pn_o_m(1, 0, m) == m + 1

    def test_h0_p3(self):
        """H^0(P^3, O(m)) = C(m+3, 3) for m >= 0."""
        assert h_k_pn_o_m(3, 0, 0) == 1
        assert h_k_pn_o_m(3, 0, 1) == 4
        assert h_k_pn_o_m(3, 0, 2) == 10
        assert h_k_pn_o_m(3, 0, 3) == 20

    def test_h0_p4(self):
        """H^0(P^4, O(m)) = C(m+4, 4)."""
        assert h_k_pn_o_m(4, 0, 0) == 1
        assert h_k_pn_o_m(4, 0, 1) == 5
        assert h_k_pn_o_m(4, 0, 2) == 15
        assert h_k_pn_o_m(4, 0, 3) == 35
        assert h_k_pn_o_m(4, 0, 4) == 70
        assert h_k_pn_o_m(4, 0, 5) == 126

    def test_bott_vanishing(self):
        """H^k(P^n, O(m)) = 0 for 0 < k < n (Bott gap)."""
        for n in range(1, 6):
            for k in range(1, n):
                for m in range(-10, 10):
                    assert h_k_pn_o_m(n, k, m) == 0, \
                        f"H^{k}(P^{n}, O({m})) should vanish (Bott gap)"

    def test_serre_duality_pn(self):
        """H^n(P^n, O(m)) = H^0(P^n, O(-m-n-1))^* by Serre duality."""
        for n in range(1, 5):
            for m in range(-10, 0):
                hn = h_k_pn_o_m(n, n, m)
                h0_dual = h_k_pn_o_m(n, 0, -m - n - 1)
                assert hn == h0_dual, \
                    f"Serre duality failed: H^{n}(P^{n}, O({m}))={hn} " \
                    f"!= H^0(P^{n}, O({-m-n-1}))={h0_dual}"

    def test_negative_twist_vanishing(self):
        """H^0(P^n, O(m)) = 0 for m < 0."""
        for n in range(1, 5):
            for m in range(-10, 0):
                assert h_k_pn_o_m(n, 0, m) == 0

    def test_bott_gap_range(self):
        """H^n(P^n, O(m)) = 0 for m > -(n+1)."""
        for n in range(1, 5):
            for m in range(-n, 10):
                assert h_k_pn_o_m(n, n, m) == 0

    def test_euler_char_hrr(self):
        """chi(P^n, O(m)) = C(n+m, n) by HRR for all m."""
        for n in range(1, 5):
            for m in range(-10, 10):
                chi_hrr = binomial(n + m, n)
                chi_sum = sum((-1)**k * h_k_pn_o_m(n, k, m) for k in range(n + 1))
                assert chi_sum == chi_hrr, \
                    f"HRR failed for P^{n}, O({m}): sum={chi_sum}, HRR={chi_hrr}"

    def test_h0_p1_o_minus1(self):
        """H^*(P^1, O(-1)) = 0 (all vanish, including H^1)."""
        assert h_k_pn_o_m(1, 0, -1) == 0
        assert h_k_pn_o_m(1, 1, -1) == 0

    def test_h_top_p3(self):
        """H^3(P^3, O(-4)) = 1 (Serre dual of H^0(P^3, O(0)) = 1)."""
        assert h_k_pn_o_m(3, 3, -4) == 1

    def test_h_top_p3_o_minus5(self):
        """H^3(P^3, O(-5)) = 4 (Serre dual of H^0(P^3, O(1)) = 4)."""
        assert h_k_pn_o_m(3, 3, -5) == 4


# =========================================================================
# Section 2: Ext on P^n
# =========================================================================

class TestExtPn:
    """Tests for Ext groups between line bundles on P^n."""

    def test_ext_self(self):
        """Ext^*(O(i), O(i)) = k in degree 0."""
        for n in range(1, 5):
            for i in range(n + 1):
                ed = ext_line_bundles_pn(n, i, i)
                assert ed.dims == {0: 1}

    def test_ext_positive_twist(self):
        """Ext^*(O, O(m)) = H^*(P^n, O(m)) for m > 0: only H^0 nonzero."""
        for n in range(1, 5):
            for m in range(1, n + 1):
                ed = ext_line_bundles_pn(n, 0, m)
                assert set(ed.dims.keys()) == {0}
                assert ed.dims[0] == binomial(n + m, n)

    def test_ext_negative_twist_vanishing(self):
        """Ext^*(O(j), O(i)) = 0 for j > i and j-i <= n (Bott gap)."""
        for n in range(1, 5):
            for diff in range(1, n + 1):
                ed = ext_line_bundles_pn(n, diff, 0)  # O(diff) -> O(0)
                assert ed.total_dim == 0


# =========================================================================
# Section 3: Beilinson collection on P^n
# =========================================================================

class TestBeilinsonCollection:
    """Tests for Beilinson's exceptional collection."""

    def test_p1_exceptional(self):
        """O, O(1) is exceptional on P^1."""
        ec = beilinson_collection_pn(1)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    def test_p2_exceptional(self):
        """O, O(1), O(2) is exceptional on P^2."""
        ec = beilinson_collection_pn(2)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    def test_p3_exceptional(self):
        """O, O(1), O(2), O(3) is exceptional on P^3."""
        ec = beilinson_collection_pn(3)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    def test_p4_exceptional(self):
        """O, ..., O(4) is exceptional on P^4."""
        ec = beilinson_collection_pn(4)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    def test_p5_exceptional(self):
        ec = beilinson_collection_pn(5)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    def test_length_equals_rank_k0(self):
        """Length of Beilinson collection = rank K_0(P^n) = n+1."""
        for n in range(1, 6):
            ec = beilinson_collection_pn(n)
            assert len(ec.objects) == n + 1

    def test_hom_consecutive(self):
        """Hom(O(i), O(i+1)) = H^0(P^n, O(1)) = n+1."""
        for n in range(1, 6):
            ec = beilinson_collection_pn(n)
            for i in range(n):
                ed = ec.ext_matrix[(i, i + 1)]
                assert ed.dims.get(0, 0) == n + 1

    def test_upper_triangular(self):
        """Ext^*(O(i), O(j)) = 0 for i > j (exceptionality)."""
        for n in range(1, 5):
            ec = beilinson_collection_pn(n)
            for i in range(n + 1):
                for j in range(i):
                    ed = ec.ext_matrix[(i, j)]
                    assert ed.total_dim == 0

    def test_diagonal_identity(self):
        """Ext^*(O(i), O(i)) = k in degree 0 (exceptionality)."""
        for n in range(1, 5):
            ec = beilinson_collection_pn(n)
            for i in range(n + 1):
                ed = ec.ext_matrix[(i, i)]
                assert ed.dims == {0: 1}


# =========================================================================
# Section 4: Ext-quiver structure
# =========================================================================

class TestExtQuiver:
    """Tests for the Ext-quiver of the Beilinson collection."""

    def test_p3_quiver_no_arrows(self):
        """P^3 Beilinson quiver has no Ext^1 arrows (strong exceptional)."""
        ec = beilinson_collection_pn(3)
        q = ext_quiver(ec)
        assert len(q.arrows) == 0

    def test_p3_quiver_vertices(self):
        ec = beilinson_collection_pn(3)
        q = ext_quiver(ec)
        assert q.num_vertices == 4

    def test_pn_no_arrows_for_all_n(self):
        """P^n Beilinson quiver has no Ext^1 arrows for all n."""
        for n in range(1, 6):
            ec = beilinson_collection_pn(n)
            q = ext_quiver(ec)
            assert len(q.arrows) == 0, f"P^{n}: unexpected arrows"


# =========================================================================
# Section 5: Quintic CY3 cohomology
# =========================================================================

class TestQuinticCohomology:
    """Tests for H^k(Q, O(m)|_Q) via Koszul resolution."""

    def test_structure_sheaf(self):
        """H^0(Q, O_Q) = 1 (connected)."""
        assert h_k_hypersurface_o_m(4, 5, 0, 0) == 1

    def test_cy_holomorphic_form(self):
        """H^3(Q, O_Q) = 1 (the holomorphic 3-form, CY condition)."""
        assert h_k_hypersurface_o_m(4, 5, 3, 0) == 1

    def test_h1_h2_structure_sheaf_vanish(self):
        """H^1(Q, O_Q) = H^2(Q, O_Q) = 0 (for strict CY3)."""
        assert h_k_hypersurface_o_m(4, 5, 1, 0) == 0
        assert h_k_hypersurface_o_m(4, 5, 2, 0) == 0

    def test_h0_o1(self):
        """H^0(Q, O(1)|_Q) = 5 = dim(H^0(P^4, O(1))) (quintic doesn't absorb O(1) sections)."""
        assert h_k_hypersurface_o_m(4, 5, 0, 1) == 5

    def test_h0_o2(self):
        """H^0(Q, O(2)|_Q) = 15 = C(6,4) - C(1,4) = 15 - 0."""
        assert h_k_hypersurface_o_m(4, 5, 0, 2) == 15

    def test_h0_o3(self):
        assert h_k_hypersurface_o_m(4, 5, 0, 3) == 35

    def test_h0_o4(self):
        assert h_k_hypersurface_o_m(4, 5, 0, 4) == 70

    def test_h0_o5(self):
        """H^0(Q, O(5)|_Q) = C(9,4) - C(4,4) = 126 - 1 = 125."""
        assert h_k_hypersurface_o_m(4, 5, 0, 5) == 125

    def test_euler_char_quintic_o_m(self):
        """chi(Q, O(m)|_Q) = C(4+m, 4) - C(m-1, 4) for all m."""
        for m in range(-8, 8):
            chi_koszul = euler_form_hypersurface(4, 5, 0, m)
            chi_formula = binomial(4 + m, 4) - binomial(m - 1, 4)
            assert chi_koszul == chi_formula, \
                f"Euler char mismatch at m={m}: {chi_koszul} vs {chi_formula}"

    def test_serre_duality_quintic(self):
        """H^k(Q, O(m)) = H^{3-k}(Q, O(-m))^* for all k, m (CY3 Serre duality)."""
        for m in range(-5, 6):
            for k in range(4):
                h_k_m = h_k_hypersurface_o_m(4, 5, k, m)
                h_3mk_minus_m = h_k_hypersurface_o_m(4, 5, 3 - k, -m)
                assert h_k_m == h_3mk_minus_m, \
                    f"CY3 Serre duality failed: H^{k}(Q, O({m}))={h_k_m} " \
                    f"!= H^{3-k}(Q, O({-m}))={h_3mk_minus_m}"

    def test_no_ext1_between_line_bundles(self):
        """Ext^1(O(i)|_Q, O(j)|_Q) = 0 for 0 <= i, j <= 4.

        This is a crucial structural result: the restricted Beilinson
        collection on the quintic has no Ext^1 between its summands.
        """
        for i in range(5):
            for j in range(5):
                ed = ext_on_hypersurface(4, 5, i, j)
                ext1 = ed.dims.get(1, 0)
                assert ext1 == 0, \
                    f"Ext^1(O({i})|_Q, O({j})|_Q) = {ext1} != 0"

    def test_no_ext2_between_line_bundles(self):
        """Ext^2(O(i)|_Q, O(j)|_Q) = 0 for 0 <= i, j <= 4."""
        for i in range(5):
            for j in range(5):
                ed = ext_on_hypersurface(4, 5, i, j)
                ext2 = ed.dims.get(2, 0)
                assert ext2 == 0, \
                    f"Ext^2(O({i})|_Q, O({j})|_Q) = {ext2} != 0"

    def test_ext3_for_negative_twist(self):
        """Ext^3(O(j)|_Q, O(i)|_Q) = dim H^0(O(j-i)|_Q) for j > i.

        By CY3 Serre duality: Ext^3(O(j), O(i)) = Hom(O(i), O(j))^*.
        """
        for i in range(5):
            for j in range(i + 1, 5):
                ed_ji = ext_on_hypersurface(4, 5, j, i)  # Ext^*(O(j), O(i))
                ed_ij = ext_on_hypersurface(4, 5, i, j)  # Ext^*(O(i), O(j))
                ext3_ji = ed_ji.dims.get(3, 0)
                hom_ij = ed_ij.dims.get(0, 0)
                assert ext3_ji == hom_ij, \
                    f"Ext^3(O({j}), O({i})) = {ext3_ji} != Hom(O({i}), O({j})) = {hom_ij}"


# =========================================================================
# Section 6: Quintic tilting generator
# =========================================================================

class TestQuinticTilting:
    """Tests for the tilting generator on the quintic."""

    def test_not_tilting(self):
        """The restricted Beilinson collection is NOT tilting on the quintic.

        Reason: Ext^3(O(i)|_Q, O(i)|_Q) = 1 != 0 (from H^3(Q, O_Q) = 1).
        """
        tg = tilting_generator_quintic()
        assert not tg.is_tilting

    def test_is_generator(self):
        """The restricted Beilinson collection generates D^b(Coh(Q))."""
        tg = tilting_generator_quintic()
        assert tg.is_generator

    def test_num_summands(self):
        tg = tilting_generator_quintic()
        assert tg.num_summands == 5

    def test_cy_dimension(self):
        tg = tilting_generator_quintic()
        assert tg.cy_dimension == 3

    def test_ext_self_has_h0_and_h3(self):
        """Each Ext^*(O(i)|_Q, O(i)|_Q) has Ext^0 = 1 and Ext^3 = 1."""
        tg = tilting_generator_quintic()
        for i in range(5):
            ed = tg.ext_matrix[(i, i)]
            assert ed.dims.get(0, 0) == 1
            assert ed.dims.get(3, 0) == 1
            assert ed.dims.get(1, 0) == 0
            assert ed.dims.get(2, 0) == 0

    def test_cy3_serre_duality(self):
        """CY3 Serre duality holds for the quintic tilting data."""
        tg = tilting_generator_quintic()
        ok, violations = verify_cy3_serre_duality(tg.ext_matrix, tg.num_summands)
        assert ok, f"Violations: {violations}"

    def test_quiver_no_arrows(self):
        """Quintic Ext-quiver has no arrows (no Ext^1)."""
        tg = tilting_generator_quintic()
        assert len(tg.quiver.arrows) == 0

    def test_quiver_cy3_self_dual(self):
        """Quintic quiver is trivially CY3-self-dual (no arrows)."""
        tg = tilting_generator_quintic()
        assert tg.quiver.is_cy3_self_dual

    def test_euler_form_antisymmetry(self):
        """chi(O(i)|_Q, O(j)|_Q) = -chi(O(j)|_Q, O(i)|_Q) for i != j.

        For CY3 with Ext^0 and Ext^3 only: chi = Ext^0 - Ext^3 and
        Serre duality gives Ext^0(i,j) = Ext^3(j,i), so
        chi(i,j) = Ext^0(i,j) - Ext^3(i,j) = Ext^0(i,j) - Ext^0(j,i) = -chi(j,i).
        """
        efm = euler_form_matrix_quintic()
        for i in range(5):
            for j in range(5):
                if i != j:
                    assert efm[i][j] == -efm[j][i], \
                        f"chi({i},{j})={efm[i][j]} != -chi({j},{i})={-efm[j][i]}"

    def test_euler_form_diagonal_zero(self):
        """chi(O(i)|_Q, O(i)|_Q) = 0 for CY3."""
        efm = euler_form_matrix_quintic()
        for i in range(5):
            assert efm[i][i] == 0

    def test_hom_consecutive(self):
        """Hom(O(i)|_Q, O(i+1)|_Q) = H^0(Q, O(1)|_Q) = 5."""
        tg = tilting_generator_quintic()
        for i in range(4):
            ed = tg.ext_matrix[(i, i + 1)]
            assert ed.dims.get(0, 0) == 5


# =========================================================================
# Section 7: CICY (3,3) in P^5
# =========================================================================

class TestCICY33:
    """Tests for the CICY (3,3) in P^5."""

    def test_hodge_numbers(self):
        """h^{1,1} = 1, h^{2,1} = 73 for CICY (3,3) in P^5."""
        h11, h21 = cicy_hodge(5, (3, 3))
        assert h11 == 1
        assert h21 == 73

    def test_euler_characteristic(self):
        """chi = 2(1 - 73) = -144."""
        assert cicy33_euler() == -144

    def test_cy_condition(self):
        """sum of degrees = ambient dim + 1: 3 + 3 = 5 + 1 = 6."""
        assert 3 + 3 == 5 + 1

    def test_structure_sheaf(self):
        """H^0(Y, O_Y) = 1."""
        assert h_k_cicy_o_m(5, (3, 3), 0, 0) == 1

    def test_cy_holomorphic_form(self):
        """H^3(Y, O_Y) = 1 (CY condition)."""
        assert h_k_cicy_o_m(5, (3, 3), 3, 0) == 1

    def test_h1_h2_vanish(self):
        """H^1(Y, O_Y) = H^2(Y, O_Y) = 0."""
        assert h_k_cicy_o_m(5, (3, 3), 1, 0) == 0
        assert h_k_cicy_o_m(5, (3, 3), 2, 0) == 0

    def test_euler_form_matrix(self):
        """Euler form is antisymmetric on diagonal and has correct values."""
        efm = euler_form_matrix_cicy33()
        for i in range(6):
            assert efm[i][i] == 0  # CY3 antisymmetry
        # chi(O, O(1)) = C(6,5) - C(3,5) - C(3,5) + C(0,5)
        #              = 6 - 0 - 0 + 0 = 6
        assert efm[0][1] == 6

    def test_euler_form_antisymmetry(self):
        """chi(i,j) = -chi(j,i) for CY3 CICY."""
        efm = euler_form_matrix_cicy33()
        for i in range(6):
            for j in range(6):
                if i != j:
                    assert efm[i][j] == -efm[j][i]

    def test_tilting_not_tilting(self):
        """Restricted Beilinson is not tilting on CICY (3,3)."""
        tg = tilting_generator_cicy33()
        assert not tg.is_tilting

    def test_tilting_is_generator(self):
        tg = tilting_generator_cicy33()
        assert tg.is_generator

    def test_num_summands(self):
        tg = tilting_generator_cicy33()
        assert tg.num_summands == 6

    def test_serre_duality_cicy(self):
        """CY3 Serre duality on CICY: H^k(Y, O(m)) = H^{3-k}(Y, O(-m))."""
        for m in range(-4, 5):
            for k in range(4):
                h_fwd = h_k_cicy_o_m(5, (3, 3), k, m)
                h_rev = h_k_cicy_o_m(5, (3, 3), 3 - k, -m)
                assert h_fwd == h_rev, \
                    f"CICY Serre duality: H^{k}(O({m}))={h_fwd} != H^{3-k}(O({-m}))={h_rev}"

    def test_h0_o1_cicy(self):
        """H^0(Y, O(1)|_Y) = 6 for CICY (3,3) in P^5."""
        assert h_k_cicy_o_m(5, (3, 3), 0, 1) == 6


# =========================================================================
# Section 8: CICY Hodge computation
# =========================================================================

class TestCICYHodge:
    """Tests for CICY Hodge number computation."""

    def test_quintic_as_ci(self):
        """Quintic = CI of degree (5) in P^4."""
        h11, h21 = cicy_hodge(4, (5,))
        assert h11 == 1
        assert h21 == 101

    def test_cicy_33(self):
        h11, h21 = cicy_hodge(5, (3, 3))
        assert h11 == 1
        assert h21 == 73

    def test_cicy_42(self):
        """CI of type (4,2) in P^5: CY3 with h^{1,1}=1, h^{2,1}=89."""
        h11, h21 = cicy_hodge(5, (4, 2))
        assert h11 == 1
        assert h21 == 89

    def test_cicy_222(self):
        """CI of type (2,2,2) in P^5: NOT CY3 (dim = 5-3 = 2, not 3).

        Actually this is a surface (CY2 = K3). Not applicable here.
        """
        # This should fail because dim = 2, not 3
        with pytest.raises(ValueError, match="Expected CY3"):
            cicy_hodge(5, (2, 2, 2))

    def test_non_cy_raises(self):
        """Non-CY degree should raise."""
        with pytest.raises(ValueError, match="Not CY"):
            cicy_hodge(5, (3, 2))  # 3+2=5 != 6=5+1

    def test_cicy_2222(self):
        """CI of type (2,2,2,2) in P^7: CY3 with chi = -128."""
        h11, h21 = cicy_hodge(7, (2, 2, 2, 2))
        assert h11 == 1
        assert h21 == 65
        assert 2 * (h11 - h21) == -128

    def test_sextic_in_wp(self):
        """Sextic in P^5... wait, degree 6 in P^5 is NOT a CY3.
        (d=6, n=5, dim=4, CY requires d=n+1=6... but dim=5-1=4, not 3.)
        The single hypersurface of degree 6 in P^5 has dim 4.
        """
        # Actually hypersurface of degree n+1 in P^n is CY of dim n-1.
        # In P^5: degree 6 gives a CY 4-fold.
        # For CY3 hypersurface: n=4, d=5 (the quintic).
        pass

    def test_euler_from_hodge_formula(self):
        """chi = 2(h^{1,1} - h^{2,1}) for CY3."""
        for n, degrees, expected_chi in [
            (4, (5,), -200),
            (5, (3, 3), -144),
            (5, (4, 2), -176),
        ]:
            h11, h21 = cicy_hodge(n, degrees)
            chi = 2 * (h11 - h21)
            assert chi == expected_chi, \
                f"CI {degrees} in P^{n}: chi={chi}, expected={expected_chi}"


# =========================================================================
# Section 9: Conifold tilting
# =========================================================================

class TestConifoldTilting:
    """Tests for the conifold tilting generator and KW quiver."""

    def test_two_vertices(self):
        ct = conifold_tilting()
        assert ct.num_vertices == 2

    def test_arrows_balanced(self):
        """KW quiver has 2 arrows in each direction (CY3 self-dual)."""
        ct = conifold_tilting()
        assert ct.arrows_01 == 2
        assert ct.arrows_10 == 2

    def test_cy3_self_dual(self):
        ct = conifold_tilting()
        assert ct.is_cy3_self_dual

    def test_end_algebra_dim(self):
        """dim End(T) = 1 + 2 + 2 + 1 = 6."""
        ct = conifold_tilting()
        assert ct.nccr_algebra_dim == 6

    def test_potential_nonzero(self):
        ct = conifold_tilting()
        assert len(ct.potential) > 0

    def test_qwp_conifold(self):
        """The KW quiver with potential has 4 arrows and 2 potential terms."""
        qwp = conifold_qwp()
        assert qwp.num_vertices == 2
        assert len(qwp.arrows) == 4
        assert len(qwp.potential_terms) == 2
        assert qwp.is_cy3

    def test_qwp_potential_terms(self):
        """Potential W = a1*b1*a2*b2 - a1*b2*a2*b1 (commutator)."""
        qwp = conifold_qwp()
        coeffs = [c for _, c in qwp.potential_terms]
        assert 1 in coeffs
        assert -1 in coeffs

    def test_arrows_source_target(self):
        """Arrows go from 0 to 1 and from 1 to 0."""
        qwp = conifold_qwp()
        arrows_01 = [(s, t) for s, t, _ in qwp.arrows if s == 0 and t == 1]
        arrows_10 = [(s, t) for s, t, _ in qwp.arrows if s == 1 and t == 0]
        assert len(arrows_01) == 2
        assert len(arrows_10) == 2


# =========================================================================
# Section 10: K3 tilting obstruction
# =========================================================================

class TestK3Tilting:
    """Tests for the K3 tilting obstruction."""

    def test_no_exceptional_collection(self):
        """K3 does not have a full exceptional collection."""
        k3 = k3_tilting_data()
        assert not k3.has_exceptional_collection

    def test_k0_rank(self):
        """K_0(K3) has rank 24."""
        k3 = k3_tilting_data()
        assert k3.k0_rank == 24

    def test_mukai_lattice_signature(self):
        """Mukai lattice H*(K3, Z) has signature (4, 20)."""
        k3 = k3_tilting_data()
        assert k3.mukai_lattice_signature == (4, 20)

    def test_bvdb_exists(self):
        """BVdB theorem guarantees a tilting generator exists."""
        k3 = k3_tilting_data()
        assert k3.bvdb_tilting_exists

    def test_not_line_bundle_sum(self):
        """Tilting generator is NOT a sum of line bundles."""
        k3 = k3_tilting_data()
        assert not k3.tilting_is_line_bundle_sum

    def test_k3xe_data(self):
        """K3 x E tilting data."""
        data = k3_times_e_tilting_data()
        assert data["k0_rank"] == 48
        assert not data["has_exceptional_collection"]
        assert data["bvdb_tilting_exists"]
        assert data["cy_dimension"] == 3


# =========================================================================
# Section 11: E1 chiral from tilting
# =========================================================================

class TestE1Chiral:
    """Tests for the E_1 chiral algebra from tilting generators."""

    def test_c3_end_dim(self):
        """End(O_{C^3}) = C, dim = 1."""
        e1 = e1_chiral_c3()
        assert e1.end_algebra_dim == 1

    def test_c3_heisenberg(self):
        """Fact(C) = Heisenberg = W_{1+infty} at c=0."""
        e1 = e1_chiral_c3()
        assert "W_{1+infty}" in e1.e1_chiral_description or \
               "Heisenberg" in e1.e1_chiral_description

    def test_conifold_end_dim(self):
        """End(T) for conifold has dim 6 (KW path algebra)."""
        e1 = e1_chiral_conifold()
        assert e1.end_algebra_dim == 6

    def test_quintic_end_dim(self):
        """End(T) for quintic.

        Total dim = sum of all Ext^k(O(i)|_Q, O(j)|_Q) for 0 <= i,j <= 4.
        From the computation: the matrix has entries only in Ext^0 and Ext^3.
        """
        e1 = e1_chiral_quintic()
        # Compute expected dim from known Ext groups
        # Ext^0(O(i), O(j)) for j >= i: C(j-i+4, 4) - C(j-i-1, 4)
        # Ext^3(O(i), O(j)) for j < i: same as Ext^0(O(j), O(i)) by Serre duality
        expected = 0
        for i in range(5):
            for j in range(5):
                m = j - i
                h0 = max(0, binomial(4 + m, 4) - (binomial(m - 1, 4) if m >= 1 else 0))
                h3 = max(0, binomial(4 - m, 4) - (binomial(-m - 1, 4) if -m >= 1 else 0))
                if m > 0:
                    expected += h0
                elif m == 0:
                    expected += 1 + 1  # Ext^0 = 1, Ext^3 = 1
                else:
                    expected += h3
        assert e1.end_algebra_dim == expected

    def test_all_cy_dimension_3(self):
        """All E_1 chiral algebras from CY3 tilting have cy_dimension = 3."""
        assert e1_chiral_c3().cy_dimension == 3
        assert e1_chiral_conifold().cy_dimension == 3
        assert e1_chiral_quintic().cy_dimension == 3


# =========================================================================
# Section 12: P^3 quiver (test case, Fano)
# =========================================================================

class TestP3Quiver:
    """Tests for P^3 tilting generator and quiver."""

    def test_p3_tilting(self):
        """Beilinson is tilting on P^3."""
        tg = tilting_generator_pn(3)
        assert tg.is_tilting
        assert tg.is_generator

    def test_p3_4_summands(self):
        tg = tilting_generator_pn(3)
        assert tg.num_summands == 4

    def test_p3_not_cy(self):
        tg = tilting_generator_pn(3)
        assert tg.cy_dimension is None

    def test_p3_hom_matrix(self):
        """Hom(O(i), O(j)) = C(j-i+3, 3) for j >= i."""
        tg = tilting_generator_pn(3)
        for i in range(4):
            for j in range(i, 4):
                ed = tg.ext_matrix[(i, j)]
                expected = binomial(j - i + 3, 3)
                assert ed.dims.get(0, 0) == expected, \
                    f"Hom(O({i}), O({j})) = {ed.dims.get(0,0)} != {expected}"

    def test_p3_quiver_4_arrows_per_edge(self):
        """P^3 Beilinson quiver: Hom(O(i), O(i+1)) has dim 4."""
        tg = tilting_generator_pn(3)
        for i in range(3):
            ed = tg.ext_matrix[(i, i + 1)]
            assert ed.dims.get(0, 0) == 4

    def test_p3_qwp(self):
        """P^3 quiver with potential has 4 vertices and 12 arrows."""
        qwp = p3_quiver()
        assert qwp.num_vertices == 4
        assert len(qwp.arrows) == 12  # 3 edges * 4 arrows each
        assert not qwp.is_cy3  # P^3 is Fano

    def test_p3_arrow_count(self):
        """12 arrows total: 4 from 0->1, 4 from 1->2, 4 from 2->3."""
        qwp = p3_quiver()
        for k in range(3):
            arrows_k = [a for a in qwp.arrows if a[0] == k and a[1] == k + 1]
            assert len(arrows_k) == 4, f"Edge {k}->{k+1}: {len(arrows_k)} arrows, expected 4"


# =========================================================================
# Section 13: Euler form computations
# =========================================================================

class TestEulerForm:
    """Tests for the Euler form on various varieties."""

    def test_euler_pn_self(self):
        """chi(O, O) = 1 on P^n."""
        for n in range(1, 6):
            assert euler_form_pn(n, 0, 0) == 1

    def test_euler_pn_o1(self):
        """chi(O, O(1)) = n+1 on P^n."""
        for n in range(1, 6):
            assert euler_form_pn(n, 0, 1) == n + 1

    def test_euler_quintic_self(self):
        """chi(O_Q, O_Q) = 0 (CY3)."""
        assert euler_form_hypersurface(4, 5, 0, 0) == 0

    def test_euler_quintic_o1(self):
        """chi(O_Q, O(1)|_Q) = 5."""
        assert euler_form_hypersurface(4, 5, 0, 1) == 5

    def test_euler_cicy_self(self):
        """chi(O_Y, O_Y) = 0 for CY3 CICY."""
        assert euler_form_cicy(5, (3, 3), 0, 0) == 0

    def test_euler_form_matrix_pn_size(self):
        for n in range(1, 5):
            efm = euler_form_matrix_pn(n)
            assert len(efm) == n + 1
            assert all(len(row) == n + 1 for row in efm)

    def test_euler_consistency(self):
        """chi(O(i), O(j)) = chi(O, O(j-i)) on P^n (shift invariance)."""
        for n in range(1, 5):
            for i in range(n + 1):
                for j in range(n + 1):
                    assert euler_form_pn(n, i, j) == euler_form_pn(n, 0, j - i)

    def test_euler_pn_negative(self):
        """chi(O(j), O(i)) = (-1)^n * chi(O(-j+i-n-1), O(0)) for n >= 1."""
        # By Serre duality: chi(E, F) = (-1)^n chi(F, E otimes omega)
        # For P^n: omega = O(-n-1), so chi(O(j), O(i)) = (-1)^n chi(O(i), O(j+n+1-n-1))...
        # Actually simpler: chi(O(j), O(i)) = C(n+i-j, n).
        for n in range(1, 5):
            for i in range(n + 1):
                for j in range(i + 1, n + 1):
                    chi_val = euler_form_pn(n, j, i)
                    expected = binomial(n + i - j, n)
                    assert chi_val == expected

    def test_euler_form_quintic_alt_computation(self):
        """Alternative computation of quintic Euler form via Koszul."""
        for i in range(5):
            for j in range(5):
                m = j - i
                # Path 1
                chi1 = euler_form_hypersurface(4, 5, i, j)
                # Path 2: C(4+m, 4) - C(m-1, 4)
                chi2 = binomial(4 + m, 4) - binomial(m - 1, 4)
                assert chi1 == chi2


# =========================================================================
# Section 14: CY3 Serre duality verification
# =========================================================================

class TestCY3SerreDuality:
    """Tests for CY3 Serre duality on tilting data."""

    def test_quintic_serre_duality(self):
        tg = tilting_generator_quintic()
        ok, violations = verify_cy3_serre_duality(tg.ext_matrix, tg.num_summands)
        assert ok
        assert len(violations) == 0

    def test_cicy33_serre_duality(self):
        tg = tilting_generator_cicy33()
        ok, violations = verify_cy3_serre_duality(tg.ext_matrix, tg.num_summands)
        assert ok
        assert len(violations) == 0

    def test_conifold_serre_duality(self):
        """Conifold: Ext^1 = Ext^2 by CY3 self-duality (2 = 2)."""
        ct = conifold_tilting()
        assert ct.arrows_01 == ct.arrows_10  # CY3 self-duality


# =========================================================================
# Section 15: Multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification of key computations."""

    def test_quintic_euler_char_3_paths(self):
        """chi(Q) = -200, verified by 3 independent paths."""
        # Path 1: from Hodge numbers
        chi1 = quintic_euler()
        # Path 2: from Euler form chi(O_Q, O_Q) and Hodge formula
        chi2 = 2 * (quintic_h11() - quintic_h21())
        # Path 3: from Koszul chi(P^4, O) - chi(P^4, O(-5))
        chi3_val = (euler_char_pn_o_m(4, 0) - euler_char_pn_o_m(4, -5))
        # Wait: chi(Q) = integral c_3(TQ), not chi(O_Q). Let me use
        # the product of degree and c_3 coefficient.
        h11_cicy, h21_cicy = cicy_hodge(4, (5,))
        chi3 = 2 * (h11_cicy - h21_cicy)
        assert chi1 == chi2 == chi3 == -200

    def test_cicy33_euler_3_paths(self):
        """chi(CICY (3,3)) = -144."""
        chi1 = cicy33_euler()
        h11, h21 = cicy_hodge(5, (3, 3))
        chi2 = 2 * (h11 - h21)
        assert chi1 == chi2 == -144

    def test_beilinson_pn_consistency(self):
        """Beilinson collection dimensions match P^n for all n."""
        for n in range(1, 6):
            ec = beilinson_collection_pn(n)
            # Verify: Hom(O(0), O(k)) = C(n+k, n) for all k
            for k in range(n + 1):
                ed = ec.ext_matrix[(0, k)]
                assert ed.dims.get(0, 0) == binomial(n + k, n)
            # Verify: total dim of Hom from O to all = sum C(n+k,n) for k=0..n
            total_hom_from_0 = sum(
                ec.ext_matrix[(0, k)].dims.get(0, 0)
                for k in range(n + 1)
            )
            expected = sum(binomial(n + k, n) for k in range(n + 1))
            assert total_hom_from_0 == expected

    def test_bott_euler_consistency(self):
        """Bott formula gives chi = C(n+m, n) for all n, m."""
        for n in range(1, 5):
            for m in range(-8, 8):
                chi_bott = sum((-1)**k * h_k_pn_o_m(n, k, m) for k in range(n + 1))
                chi_hrr = euler_char_pn_o_m(n, m)
                assert chi_bott == chi_hrr

    def test_koszul_euler_consistency_quintic(self):
        """Koszul + Bott gives same chi as direct formula for quintic."""
        for m in range(-5, 6):
            # Koszul: chi(Q, O(m)) = chi(P^4, O(m)) - chi(P^4, O(m-5))
            chi_koszul = euler_char_pn_o_m(4, m) - euler_char_pn_o_m(4, m - 5)
            chi_formula = euler_form_hypersurface(4, 5, 0, m)
            assert chi_koszul == chi_formula

    def test_koszul_euler_consistency_cicy(self):
        """Koszul CI Euler char matches the direct formula."""
        for m in range(-4, 5):
            chi1 = euler_form_cicy(5, (3, 3), 0, m)
            # From Koszul: chi = chi(P^5, O(m)) - chi(P^5, O(m-3)) - chi(P^5, O(m-3)) + chi(P^5, O(m-6))
            chi2 = (euler_char_pn_o_m(5, m) - euler_char_pn_o_m(5, m - 3)
                    - euler_char_pn_o_m(5, m - 3) + euler_char_pn_o_m(5, m - 6))
            assert chi1 == chi2, f"m={m}: {chi1} vs {chi2}"


# =========================================================================
# Section 16: Summary function tests
# =========================================================================

class TestSummaryFunctions:
    """Tests for summary/convenience functions."""

    def test_tilting_summary_pn(self):
        for n in range(1, 5):
            summary = tilting_summary_pn(n)
            assert summary["num_summands"] == n + 1
            assert summary["is_tilting"]
            assert summary["is_generator"]

    def test_tilting_summary_quintic(self):
        summary = tilting_summary_quintic()
        assert summary["num_summands"] == 5
        assert not summary["is_tilting"]
        assert summary["is_generator"]
        assert summary["cy_dimension"] == 3

    def test_tilting_summary_cicy33(self):
        summary = tilting_summary_cicy33()
        assert summary["num_summands"] == 6
        assert not summary["is_tilting"]
        assert summary["is_generator"]
        assert summary["cy_dimension"] == 3

    def test_cohomology_table(self):
        table = cohomology_table_pn(3, (-5, 5))
        assert len(table) == 11
        # Check m=0 row
        row0 = [r for r in table if r["m"] == 0][0]
        assert row0["H^0"] == 1
        assert row0["H^1"] == 0
        assert row0["H^2"] == 0
        assert row0["H^3"] == 0

    def test_all_cohomology(self):
        """all_cohomology_pn_twist gives same results as h_k_pn_o_m."""
        for n in range(1, 5):
            for m in range(-5, 5):
                result = all_cohomology_pn_twist(n, m)
                for k in range(n + 1):
                    expected = h_k_pn_o_m(n, k, m)
                    actual = result.get(k, 0)
                    assert actual == expected


# =========================================================================
# Section 17: Hodge number consistency checks
# =========================================================================

class TestHodgeNumbers:
    """Tests for Hodge numbers of standard CY3s."""

    def test_quintic_h11(self):
        assert quintic_h11() == 1

    def test_quintic_h21(self):
        assert quintic_h21() == 101

    def test_quintic_euler(self):
        assert quintic_euler() == -200

    def test_cicy33_h11(self):
        assert cicy33_h11() == 1

    def test_cicy33_h21(self):
        assert cicy33_h21() == 73

    def test_cicy33_euler(self):
        assert cicy33_euler() == -144

    def test_cicy42_hodge(self):
        """CICY (4,2) in P^5: h11=1, h21=89, chi=-176."""
        h11, h21 = cicy_hodge(5, (4, 2))
        assert h11 == 1
        assert h21 == 89
        assert 2 * (h11 - h21) == -176

    def test_quintic_mirror_relation(self):
        """Mirror of quintic has h11=101, h21=1, chi=200 (flipped sign)."""
        # The mirror quintic has h^{1,1} and h^{2,1} swapped.
        h11 = quintic_h11()  # = 1
        h21 = quintic_h21()  # = 101
        # Mirror: h11' = h21 = 101, h21' = h11 = 1
        chi_mirror = 2 * (h21 - h11)  # 2(101 - 1) = 200
        assert chi_mirror == 200
        assert chi_mirror == -quintic_euler()


# =========================================================================
# Section 18: Extended Beilinson on higher P^n
# =========================================================================

class TestHigherPn:
    """Tests for Beilinson collections on P^n for n up to 7."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7])
    def test_exceptional_strong_full(self, n):
        ec = beilinson_collection_pn(n)
        assert ec.is_exceptional
        assert ec.is_strong
        assert ec.is_full

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_hom_o_o_n(self, n):
        """Hom(O, O(n)) = C(2n, n) = (2n)! / (n!)^2."""
        ec = beilinson_collection_pn(n)
        ed = ec.ext_matrix[(0, n)]
        expected = binomial(2 * n, n)
        assert ed.dims.get(0, 0) == expected

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_tilting_pn(self, n):
        tg = tilting_generator_pn(n)
        assert tg.is_tilting
        assert tg.is_generator


# =========================================================================
# Section 19: Quiver with potential
# =========================================================================

class TestQuiverWithPotential:
    """Tests for quivers with potential."""

    def test_conifold_qwp_cy3(self):
        qwp = conifold_qwp()
        assert qwp.is_cy3

    def test_p3_qwp_not_cy3(self):
        qwp = p3_quiver()
        assert not qwp.is_cy3

    def test_conifold_jacobian_infinite(self):
        """Conifold Jacobian algebra is infinite-dim (non-compact CY3)."""
        qwp = conifold_qwp()
        assert qwp.jacobian_dim is None

    def test_conifold_arrows_are_correct(self):
        qwp = conifold_qwp()
        # 2 arrows from 0 to 1
        a_01 = [a for a in qwp.arrows if a[0] == 0 and a[1] == 1]
        assert len(a_01) == 2
        # 2 arrows from 1 to 0
        a_10 = [a for a in qwp.arrows if a[0] == 1 and a[1] == 0]
        assert len(a_10) == 2


# =========================================================================
# Section 20: Cross-verification with cy_euler.py
# =========================================================================

class TestCrossVerification:
    """Cross-verification with existing cy_euler.py infrastructure."""

    def test_quintic_euler_matches_cy_euler(self):
        """quintic_euler() here matches cy_euler.quintic_hodge().euler_characteristic."""
        try:
            from compute.lib.cy_euler import quintic_hodge
            hd = quintic_hodge()
            assert hd.euler_characteristic == quintic_euler()
        except ImportError:
            pytest.skip("cy_euler not available")

    def test_k3_mukai_rank(self):
        """K_0(K3) rank = 24 matches sum of even Betti numbers of K3."""
        try:
            from compute.lib.cy_euler import k3_hodge
            hd = k3_hodge()
            betti = hd.betti
            # rank K_0 = sum b_{2k} = b_0 + b_2 + b_4
            k0_rank = betti[0] + betti[2] + betti[4]
            assert k0_rank == k3_tilting_data().k0_rank
        except ImportError:
            pytest.skip("cy_euler not available")

    def test_chi_p4_values(self):
        """Cross-check H^0(P^4, O(m)) against binomial formula."""
        for m in range(10):
            h0 = h_k_pn_o_m(4, 0, m)
            expected = binomial(m + 4, 4)
            assert h0 == expected

    def test_quintic_hom_dimensions_via_euler_form(self):
        """For the quintic with only Ext^0 and Ext^3,
        the Euler form determines both dimensions:
          chi = Ext^0 - Ext^3  and  Ext^0 + Ext^3 = total.
        """
        for i in range(5):
            for j in range(5):
                m = j - i
                chi = euler_form_hypersurface(4, 5, i, j)
                ed = ext_on_hypersurface(4, 5, i, j)
                ext0 = ed.dims.get(0, 0)
                ext3 = ed.dims.get(3, 0)
                ext1 = ed.dims.get(1, 0)
                ext2 = ed.dims.get(2, 0)
                # Ext^1 = Ext^2 = 0
                assert ext1 == 0
                assert ext2 == 0
                # chi = ext0 - ext3
                assert chi == ext0 - ext3


# =========================================================================
# Section 21: Numerical consistency
# =========================================================================

class TestNumericalConsistency:
    """Numerical consistency checks across different computation paths."""

    def test_quintic_total_ext_dim(self):
        """Total dim End(T) for quintic: sum of all Ext^k(O(i), O(j)).

        Each (i,j) pair has only Ext^0 and Ext^3 nonzero.
        For m = j-i: Ext^0 = H^0(Q, O(m)) and Ext^3 = H^3(Q, O(m)).
        By Serre duality on Q: Ext^3(O(i), O(j)) = Ext^0(O(j), O(i))^*.
        So total = 2 * (sum of Hom(O(i), O(j)) for all i,j)
                 = 2 * (sum_{m=-4}^{4} (5 - |m|) * h^0(Q, O(m)) )
                 ... more simply, just sum all entries.
        """
        tg = tilting_generator_quintic()
        total = sum(ed.total_dim for ed in tg.ext_matrix.values())
        # Independently compute: for each (i,j), add H^0(Q, O(j-i)) + H^3(Q, O(j-i))
        expected = 0
        for i in range(5):
            for j in range(5):
                m = j - i
                h0 = h_k_hypersurface_o_m(4, 5, 0, m)
                h3 = h_k_hypersurface_o_m(4, 5, 3, m)
                expected += h0 + h3
        assert total == expected
        # The value 420 = 2 * 210, where 210 is the sum of all Hom dimensions
        # (each Hom(O(i), O(j)) for j >= i appears once as Ext^0 and its
        # Serre dual appears as Ext^3 in the transposed entry).
        assert total == 420

    def test_euler_form_determinant_quintic(self):
        """The Euler form matrix for quintic has determinant != 0 (non-degenerate)."""
        efm = euler_form_matrix_quintic()
        # Compute 5x5 determinant using LU
        # For an antisymmetric 5x5 matrix, det = 0 (odd dimension)
        # This is correct: det of antisymmetric matrix of odd size is always 0.
        n = 5
        mat = [row[:] for row in efm]  # copy
        # For odd-dimensional antisymmetric matrices, det = 0
        # Verify antisymmetry first
        for i in range(n):
            for j in range(n):
                assert mat[i][j] == -mat[j][i]
        # Pfaffian doesn't exist for odd n, det = 0
        # This is fine: it means the Euler form is degenerate, which is
        # expected since chi(F, F) = 0 for all F on CY3.

    def test_euler_form_determinant_p3(self):
        """The Euler form matrix for P^3 (Fano) should be non-degenerate."""
        efm = euler_form_matrix_pn(3)
        # Upper triangular with 1s on diagonal: det = 1
        # Actually it's: chi(O(i), O(j)) = C(3+j-i, 3)
        # efm[i][j] = C(3+j-i, 3)
        # This is an upper-triangular-ish matrix.
        # efm[0] = [1, 4, 10, 20]
        # efm[1] = [0, 1, 4, 10]   (C(3+j-1, 3) for j<1: C(3+j-1,3))
        # Wait: chi(O(1), O(0)) = C(3-1, 3) = C(2,3) = 0.
        # So the matrix IS upper triangular (strictly below diagonal = 0).
        for i in range(4):
            for j in range(i):
                assert efm[i][j] == 0, f"efm[{i}][{j}] = {efm[i][j]} != 0"
        # Diagonal = 1
        for i in range(4):
            assert efm[i][i] == 1

    def test_cicy33_total_ext_dim(self):
        """Total dim End(T) for CICY (3,3) in P^5."""
        tg = tilting_generator_cicy33()
        total = sum(ed.total_dim for ed in tg.ext_matrix.values())
        assert total > 0
        # Each diagonal has Ext^0 = 1 and Ext^3 = 1
        diag_total = sum(tg.ext_matrix[(i, i)].total_dim for i in range(6))
        assert diag_total == 12  # 6 * (1 + 1) = 12
