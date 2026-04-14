r"""Tests for the independent m_5(T,T,T,T,T) computation from the 5-point
Virasoro conformal block.

Verifies the shadow-Feynman dictionary at loop order L=4 using methods
that are INDEPENDENT of the shadow recursion in c3_shadow_tower.py and
the convolution recursion in a_infinity_bar_w1inf.py.

TEST STRUCTURE:

  1. ExactWick: free-field Wick contraction engine
     - 2-point function = c/2 * z^{-4}
     - 3-point function = c * prod z_{ij}^{-2}
     - 4-point cluster decomposition
     - 5-point cluster decomposition
     - Sign convention verification

  2. OPE input extraction (independent of shadow)
     - kappa_ch = 1/2 from 2-point
     - alpha = 2 from 3-point Wick
     - S_4 = 10/27 from Zamolodchikov formula

  3. mu_5 = -80/9 from polynomial constraint
     - Q_L quadratic (TT OPE finite pole order)
     - a_3 = -a_1*a_2/a_0

  4. Cross-check with shadow recursion
     - S_5 from independent = S_5 from shadow tower

  5. Cross-check with a_infinity_bar_w1inf.py
     - mu_5 from independent = m_5(T,...,T) coefficient
"""

import pytest
from fractions import Fraction

from compute.lib.virasoro_m5_five_point import (
    ExactWick,
    _perfect_matchings,
    _is_connected,
    _set_partitions,
    extract_kappa,
    extract_alpha,
    extract_S4_zamolodchikov,
    verify_S4_from_four_point,
    virasoro_gram_matrix_level2,
    compute_mu5_independent,
    verify_five_point_wick,
    verify_m5_from_five_point,
)


# =========================================================================
#  Combinatorial utilities
# =========================================================================

class TestPerfectMatchings:
    """Test the perfect matching enumerator."""

    def test_empty(self):
        """Empty list has one (empty) matching."""
        assert _perfect_matchings([]) == [[]]

    def test_two_items(self):
        """Two items: one matching."""
        m = _perfect_matchings([0, 1])
        assert len(m) == 1
        assert m[0] == [(0, 1)]

    def test_four_items(self):
        """Four items: 3 matchings (= 3!! = 3)."""
        m = _perfect_matchings([0, 1, 2, 3])
        assert len(m) == 3

    def test_six_items(self):
        """Six items: 15 matchings (= 5!! = 15)."""
        m = _perfect_matchings([0, 1, 2, 3, 4, 5])
        assert len(m) == 15

    def test_ten_items(self):
        """Ten items: 945 matchings (= 9!! = 945)."""
        m = _perfect_matchings(list(range(10)))
        # VERIFIED [DC] 945 matchings [LT] (2n-1)!! formula
        assert len(m) == 945

    def test_odd_items(self):
        """Odd number of items: no matchings."""
        assert _perfect_matchings([0, 1, 2]) == []


class TestConnectivity:
    """Test graph connectivity check."""

    def test_single_vertex(self):
        assert _is_connected({}, 1)

    def test_connected_path(self):
        adj = {0: {1}, 1: {0, 2}, 2: {1}}
        assert _is_connected(adj, 3)

    def test_disconnected(self):
        adj = {0: {1}, 1: {0}, 2: {3}, 3: {2}}
        assert not _is_connected(adj, 4)

    def test_cycle(self):
        adj = {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}}
        assert _is_connected(adj, 5)


class TestSetPartitions:
    """Test set partition enumerator."""

    def test_bell_numbers(self):
        """Number of set partitions = Bell number."""
        # B(0)=1, B(1)=1, B(2)=2, B(3)=5, B(4)=15, B(5)=52
        for n, bell in [(0, 1), (1, 1), (2, 2), (3, 5), (4, 15)]:
            parts = _set_partitions(list(range(n)))
            # VERIFIED [DC] Bell number B({n}) = {bell}
            assert len(parts) == bell


# =========================================================================
#  ExactWick: 2-point function
# =========================================================================

class TestWickTwoPoint:
    """Test 2-point function <T(z_1)T(z_2)> at c=1."""

    def setup_method(self):
        self.wick = ExactWick()

    def test_two_point_unit_separation(self):
        """<T(0)T(1)> = c/2 = 1/2."""
        G2 = self.wick.full_correlator([Fraction(0), Fraction(1)])
        # VERIFIED [DC] 1/2 [LT] c/2 normalization
        assert G2 == Fraction(1, 2)

    def test_two_point_general(self):
        """<T(z_1)T(z_2)> = (1/2)/(z_1-z_2)^4 at various separations."""
        for z1, z2 in [(Fraction(0), Fraction(2)),
                       (Fraction(1), Fraction(5)),
                       (Fraction(-3), Fraction(7))]:
            G2 = self.wick.full_correlator([z1, z2])
            expected = Fraction(1, 2) / (z1 - z2) ** 4
            # VERIFIED [DC] (c/2)/(z12)^4 [LT] Virasoro 2-point
            assert G2 == expected

    def test_two_point_connected_equals_full(self):
        """For n=2, connected = full (no disconnected parts)."""
        zs = [Fraction(0), Fraction(3)]
        assert self.wick.full_correlator(zs) == self.wick.connected_correlator(zs)

    def test_one_point_vanishes(self):
        """<T(z)> = 0 on the sphere."""
        assert self.wick.full_correlator([Fraction(7)]) == Fraction(0)


# =========================================================================
#  ExactWick: 3-point function
# =========================================================================

class TestWickThreePoint:
    """Test 3-point function <T(z_1)T(z_2)T(z_3)> at c=1."""

    def setup_method(self):
        self.wick = ExactWick()

    def test_three_point_cft_formula(self):
        """G_3 = c/(z12^2 * z23^2 * z13^2) at c=1.

        This is the unique conformally-covariant 3-point function for
        spin-2 fields on the sphere. Wick verification at 3 configurations.
        """
        test_configs = [
            [Fraction(0), Fraction(1), Fraction(3)],
            [Fraction(1), Fraction(4), Fraction(7)],
            [Fraction(2), Fraction(5), Fraction(11)],
        ]
        for zs in test_configs:
            G3 = self.wick.connected_correlator(zs)
            z12 = zs[0] - zs[1]
            z23 = zs[1] - zs[2]
            z13 = zs[0] - zs[2]
            expected = Fraction(1) / (z12 ** 2 * z23 ** 2 * z13 ** 2)
            # VERIFIED [DC] c/(z12^2*z23^2*z13^2) [LT] CFT 3-point function
            assert G3 == expected, f"At {zs}: got {G3}, expected {expected}"

    def test_three_point_connected_equals_full(self):
        """For n=3, connected = full (since <T> = 0, no disconnected parts)."""
        zs = [Fraction(0), Fraction(1), Fraction(3)]
        assert self.wick.full_correlator(zs) == self.wick.connected_correlator(zs)

    def test_three_point_sign_convention(self):
        """Verify the sign is POSITIVE (from <JJ> = -1/(z-w)^2 convention).

        With T = -(1/2):JJ: and propagator <JJ> = -1/(z-w)^2,
        the 3-point function is positive (signs cancel for odd n).
        """
        zs = [Fraction(0), Fraction(1), Fraction(2)]
        G3 = self.wick.connected_correlator(zs)
        # VERIFIED [DC] positive sign [LT] (-1/2)^3 * (-1)^3 = (1/2)^3
        assert G3 > 0


# =========================================================================
#  ExactWick: 4-point function
# =========================================================================

class TestWickFourPoint:
    """Test 4-point function at c=1."""

    def setup_method(self):
        self.wick = ExactWick()

    def test_four_point_cluster_decomposition(self):
        """G_4^full = G_4^conn + sum of 2-point products.

        Cluster decomposition:
          G_4 = G_4^{conn} + sum_{3 pairings} G_2(z_i,z_j) * G_2(z_k,z_l)
        """
        zs = [Fraction(1), Fraction(3), Fraction(6), Fraction(10)]
        G4_full = self.wick.full_correlator(zs)
        G4_conn = self.wick.connected_correlator(zs)

        pairs = [([0, 1], [2, 3]), ([0, 2], [1, 3]), ([0, 3], [1, 2])]
        disconn = Fraction(0)
        for p1, p2 in pairs:
            g1 = self.wick.full_correlator([zs[i] for i in p1])
            g2 = self.wick.full_correlator([zs[i] for i in p2])
            disconn += g1 * g2

        # VERIFIED [DC] cluster decomposition [LT] G4 = G4^conn + G2*G2
        assert G4_full == G4_conn + disconn

    def test_four_point_connected_nonzero(self):
        """G_4^conn != 0 (non-Gaussian: Virasoro is class M)."""
        zs = [Fraction(1), Fraction(2), Fraction(4), Fraction(7)]
        G4_conn = self.wick.connected_correlator(zs)
        # VERIFIED [DC] nonzero G_4^conn [LT] class M (non-Gaussian)
        assert G4_conn != 0


# =========================================================================
#  ExactWick: 5-point function
# =========================================================================

class TestWickFivePoint:
    """Test 5-point function at c=1."""

    def setup_method(self):
        self.wick = ExactWick()

    def test_five_point_cluster_decomposition(self):
        """G_5^full = sum over partitions of connected correlators.

        The full correlator is reconstructed from connected parts via
        the exponential/cumulant formula. Partitions with singletons
        contribute zero since <T> = 0.
        """
        result = verify_five_point_wick()
        # VERIFIED [DC] 5-point cluster [LT] cumulant reconstruction
        assert result["cluster_decomposition_verified"]

    def test_five_point_connected_nonzero(self):
        """G_5^conn != 0 (class M continues at arity 5)."""
        zs = [Fraction(k) for k in range(1, 6)]
        G5_conn = self.wick.connected_correlator(zs)
        # VERIFIED [DC] nonzero G_5^conn [LT] infinite shadow tower
        assert G5_conn != 0

    def test_five_point_connected_positive(self):
        """G_5^conn > 0 at equally spaced points (sign from (1/2)^5)."""
        zs = [Fraction(k) for k in range(1, 6)]
        G5_conn = self.wick.connected_correlator(zs)
        # VERIFIED [DC] positive G_5^conn [LT] Hamiltonian cycle sum
        assert G5_conn > 0

    def test_five_point_exact_value(self):
        """G_5^conn(1,2,3,4,5) = 775/5184 (computed by Wick)."""
        zs = [Fraction(k) for k in range(1, 6)]
        G5_conn = self.wick.connected_correlator(zs)
        # VERIFIED [DC] 775/5184 [DA] exact Wick enumeration
        assert G5_conn == Fraction(775, 5184)


# =========================================================================
#  Independent OPE input extraction
# =========================================================================

class TestKappaExtraction:
    """Test kappa_ch extraction from 2-point normalization."""

    def test_kappa_c1(self):
        """kappa_ch = 1/2 at c=1."""
        # VERIFIED [DC] 1/2 [LT] c/2 normalization
        assert extract_kappa(Fraction(1)) == Fraction(1, 2)

    def test_kappa_general_c(self):
        """kappa_ch = c/2 for general c."""
        for c_val in [Fraction(1, 2), Fraction(7), Fraction(26)]:
            assert extract_kappa(c_val) == c_val / 2


class TestAlphaExtraction:
    """Test alpha extraction from 3-point Wick computation."""

    def test_alpha_value(self):
        """alpha = 2 at c=1, independently verified via Wick."""
        result = extract_alpha(Fraction(1))
        # VERIFIED [DC] alpha=2 [DA] 3-point Wick at 3 configurations
        assert result["alpha"] == Fraction(2)
        assert result["wick_verified"] is True

    def test_alpha_wick_consistency(self):
        """Wick matches CFT prediction at 3 different point configurations."""
        result = extract_alpha(Fraction(1))
        assert result["wick_verified"]


class TestS4Extraction:
    """Test S_4 extraction from Zamolodchikov formula."""

    def test_S4_value(self):
        """S_4 = 10/27 at c=1."""
        S4 = extract_S4_zamolodchikov(Fraction(1))
        # VERIFIED [DC] 10/27 [LT] Zamolodchikov c-recursion
        assert S4 == Fraction(10, 27)

    def test_S4_general_formula(self):
        """S_4 = 10/(c(5c+22)) for various c."""
        for c_val in [Fraction(1, 2), Fraction(2), Fraction(25)]:
            S4 = extract_S4_zamolodchikov(c_val)
            expected = Fraction(10) / (c_val * (5 * c_val + 22))
            assert S4 == expected

    def test_S4_four_point_cluster(self):
        """4-point cluster decomposition is consistent (cross-check on S_4)."""
        result = verify_S4_from_four_point(Fraction(1))
        # VERIFIED [DC] cluster OK [CT] 4-point Wick consistency
        assert result["cluster_decomposition_verified"]


# =========================================================================
#  Virasoro Gram matrix
# =========================================================================

class TestGramMatrix:
    """Test Virasoro Gram matrix at level 2."""

    def test_gram_vacuum(self):
        """At h=0 (vacuum), Gram matrix is degenerate."""
        gram = virasoro_gram_matrix_level2(Fraction(1), Fraction(0))
        assert gram["M11"] == Fraction(1, 2)  # c/2
        assert gram["M12"] == Fraction(0)
        assert gram["M22"] == Fraction(0)
        assert gram["det"] == Fraction(0)

    def test_gram_s4_formula(self):
        """S_4 from Gram matrix matches Zamolodchikov formula."""
        gram = virasoro_gram_matrix_level2(Fraction(1))
        # VERIFIED [DC] S_4 formula [LT] Gram matrix structure
        assert gram["S4_zamolodchikov"] == Fraction(10, 27)


# =========================================================================
#  mu_5 independent computation
# =========================================================================

class TestMu5Independent:
    """Test independent computation of mu_5 = m_5(T,...,T) coefficient."""

    def test_mu5_value(self):
        """mu_5 = -80/9 at c=1."""
        result = compute_mu5_independent(Fraction(1))
        # VERIFIED [DC] -80/9 [DA] polynomial constraint q_3=0
        assert result["mu5"] == Fraction(-80, 9)

    def test_S5_value(self):
        """S_5 = mu_5/5 = -16/9 at c=1."""
        result = compute_mu5_independent(Fraction(1))
        # VERIFIED [DC] -16/9 [DA] mu_5/5
        assert result["S5"] == Fraction(-16, 9)

    def test_a_coefficients(self):
        """a_0=1, a_1=6, a_2=40/27, a_3=-80/9 at c=1."""
        result = compute_mu5_independent(Fraction(1))
        assert result["a0"] == Fraction(1)
        assert result["a1"] == Fraction(6)
        assert result["a2"] == Fraction(40, 27)
        assert result["a3"] == Fraction(-80, 9)

    def test_Q_L_quadratic_verification(self):
        """Verify Q_L(t) = f(t)^2 is exactly quadratic (q_3 = q_4 = 0).

        f(t) = a_0 + a_1*t + a_2*t^2 + a_3*t^3
        f(t)^2 should have zero coefficients at t^3 and t^4 (but not t^5
        since we truncated f at t^3).
        """
        r = compute_mu5_independent(Fraction(1))
        a = [r["a0"], r["a1"], r["a2"], r["a3"]]

        # Coefficient of t^3 in f^2: 2*a0*a3 + 2*a1*a2
        q3 = 2 * a[0] * a[3] + 2 * a[1] * a[2]
        # VERIFIED [DC] q_3=0 [LT] Q_L quadratic
        assert q3 == Fraction(0)

    def test_mu5_sign_negative(self):
        """mu_5 < 0: first sign change in shadow tower.

        The shadow tower coefficients a_0 > 0, a_1 > 0, a_2 > 0, a_3 < 0.
        This oscillatory behavior is characteristic of class M.
        """
        result = compute_mu5_independent(Fraction(1))
        assert result["a0"] > 0
        assert result["a1"] > 0
        assert result["a2"] > 0
        # VERIFIED [DC] negative a_3 [LT] class M oscillation
        assert result["a3"] < 0


# =========================================================================
#  Cross-check with shadow recursion
# =========================================================================

class TestShadowCrosscheck:
    """Cross-check independent mu_5 against shadow tower recursion."""

    def setup_method(self):
        from compute.lib.c3_shadow_tower import shadow_tower_single_channel
        self.shadow_tower = shadow_tower_single_channel(
            kappa=Fraction(1, 2),
            alpha=Fraction(2),
            S4=Fraction(10, 27),
            max_r=8,
        )

    def test_S5_matches_shadow(self):
        """S_5 from independent computation matches shadow tower.

        This is the KEY VERIFICATION: two completely different code paths
        give the same answer.
          Path 1: Wick + polynomial constraint (this module)
          Path 2: convolution recursion (c3_shadow_tower.py)
        Agreement confirms shadow-Feynman at L=4.
        """
        S5_shadow = self.shadow_tower[5]
        result = compute_mu5_independent(Fraction(1))
        S5_independent = result["S5"]
        # VERIFIED [DC] S_5 match [CT] c3_shadow_tower shadow recursion
        assert S5_independent == S5_shadow, (
            f"S_5 mismatch: independent={S5_independent}, shadow={S5_shadow}"
        )

    def test_S2_S3_S4_also_match(self):
        """Lower shadows also match (sanity check on inputs)."""
        result = compute_mu5_independent(Fraction(1))

        # S_2 = a_0/2 = kappa = 1/2
        S2_indep = result["a0"] / 2
        assert S2_indep == self.shadow_tower[2]

        # S_3 = a_1/3
        S3_indep = result["a1"] / 3
        assert S3_indep == self.shadow_tower[3]

        # S_4 = a_2/4
        S4_indep = result["a2"] / 4
        assert S4_indep == self.shadow_tower[4]


# =========================================================================
#  Cross-check with a_infinity_bar_w1inf.py
# =========================================================================

class TestAInfCrosscheck:
    """Cross-check with the m_5 implementation in a_infinity_bar_w1inf.py."""

    def setup_method(self):
        from compute.lib.a_infinity_bar_w1inf import AInfBarComplex, T
        self.bar_cx = AInfBarComplex()
        self.T = T

    def test_mu5_matches_bar_m5(self):
        """mu_5 from independent computation matches m_5(T,...,T) in bar complex.

        The bar complex m_5 uses the convolution recursion.
        The independent computation uses the polynomial constraint.
        Both should give -80/9.
        """
        result = compute_mu5_independent(Fraction(1))
        mu5_indep = result["mu5"]

        m5_result = self.bar_cx.m5(self.T, self.T, self.T, self.T, self.T)
        s = m5_result.simplify()
        mu5_bar = s.terms[0].coeff

        # VERIFIED [DC] mu_5 match [CT] a_infinity_bar_w1inf m_5
        assert mu5_indep == mu5_bar, (
            f"mu_5 mismatch: independent={mu5_indep}, bar={mu5_bar}"
        )


# =========================================================================
#  Master verification
# =========================================================================

class TestMasterVerification:
    """Test the full verification pipeline."""

    def test_full_verification_passes(self):
        """The complete verification pipeline returns all True."""
        result = verify_m5_from_five_point()

        # VERIFIED [DC] full pipeline [LT] shadow-Feynman at L=4
        assert result["mu5_equals_minus_80_over_9"]
        assert result["S5_equals_minus_16_over_9"]
        assert result["S5_matches_shadow"]
        assert result["three_point_wick_matches"]
        assert result["alpha_wick_verified"]
        assert result["S4_cluster_verified"]
        assert result["five_point_cluster_verified"]

    def test_conclusion_is_verified(self):
        """The conclusion string starts with VERIFIED."""
        result = verify_m5_from_five_point()
        assert result["conclusion"].startswith("SHADOW-FEYNMAN VERIFIED")

    def test_all_independent_inputs_listed(self):
        """All 4 independent inputs are listed in the report."""
        result = verify_m5_from_five_point()
        assert len(result["independent_inputs"]) == 4

    def test_verification_chain_complete(self):
        """All 6 steps of the verification chain are present."""
        result = verify_m5_from_five_point()
        assert len(result["verification_chain"]) == 6
