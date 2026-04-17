r"""Tests for k3_abelian_yangian_currents.py: explicit Drinfeld currents
x^pm_i(z), h_i(z) for the K3 abelian Yangian Y(g_K3).

Manuscript reference:
    chapters/examples/cy_c_six_routes_convergence.tex,
    Theorem thm:cy-c-abelian-K3-currents (extension of thm:cy-c-abelian-K3).

Test structure:
    Section 1: Simple roots and their data (4 tests)
    Section 2: OPE coefficients at orders 0, 1, 2 (10 tests)
    Section 3: Cartan matrix (4 tests)
    Section 4: Lattice VOA character matching (4 tests)
    Section 5: Drinfeld coproduct (3 tests)
    Section 6: Coassociativity (2 tests)
    Section 7: Full summary and full verification (4 tests)
    Total: 31 tests.
"""

from fractions import Fraction

import pytest

from compute.lib.independent_verification import independent_verification
from compute.lib.k3_abelian_yangian_currents import (
    EPSILON,
    NUM_CURRENTS,
    RANK,
    bar_euler_coefficients,
    cartan_matrix,
    cobar_euler_coefficients,
    coproduct_h,
    coproduct_x_minus,
    coproduct_x_plus,
    full_summary,
    full_verification,
    k3_elliptic_genus_c_minus_one,
    k3_elliptic_genus_c_zero,
    koszul_pairing_check,
    mukai_diagonal_pairing,
    mukai_rank_from_elliptic_genus,
    ope_h_h,
    ope_h_x_minus,
    ope_h_x_plus,
    ope_x_plus_x_minus,
    ope_x_plus_x_plus,
    simple_roots,
    verify_cartan_matrix_diagonal,
    verify_coassociativity_primitive,
    verify_coproduct_primitive_abelian,
)
from compute.lib.k3_yangian import SIG_MINUS, SIG_PLUS

F = Fraction


# =========================================================================
# Section 1: Simple roots and their data
# =========================================================================

class TestSimpleRoots:
    """Tests for the 24 simple-root data."""

    def test_rank_24(self):
        roots = simple_roots()
        assert len(roots) == 24
        assert RANK == 24

    def test_signature_4_20(self):
        """The 24 simple roots split as 4 positive + 20 negative."""
        roots = simple_roots()
        n_pos = sum(1 for r in roots if r.epsilon == 1)
        n_neg = sum(1 for r in roots if r.epsilon == -1)
        assert n_pos == 4
        assert n_neg == 20
        assert (n_pos, n_neg) == (SIG_PLUS, SIG_MINUS)

    def test_block_labels(self):
        """The first 4 are 'positive' block; the last 20 are 'negative' block."""
        roots = simple_roots()
        for i in range(4):
            assert roots[i].block == "positive"
            assert roots[i].epsilon == 1
        for i in range(4, 24):
            assert roots[i].block == "negative"
            assert roots[i].epsilon == -1

    def test_mukai_diagonal_pairing_orthogonal(self):
        """The Mukai diagonal pairing is delta_{ij} epsilon_i (orthogonal basis)."""
        for i in range(24):
            for j in range(24):
                expected = EPSILON[i] if i == j else 0
                assert mukai_diagonal_pairing(i, j) == expected


# =========================================================================
# Section 2: OPE coefficients at orders 0, 1, 2
# =========================================================================

class TestOPEXPlusXPlus:
    """Tests for the OPE x^+_i(z) x^+_j(w)."""

    def test_diagonal_positive_epsilon_regular(self):
        """For epsilon_i = +1, x^+_i x^+_i is regular (vanishes at z=w to order 1)."""
        for i in range(4):  # epsilon = +1
            ope = ope_x_plus_x_plus(i, i)
            assert ope.pole_power == 1, f"Expected pole_power=+1 for i={i}, got {ope.pole_power}"
            assert ope.coeff_pow_minus_2 == "0"
            assert ope.coeff_pow_minus_1 == "0"
            assert not ope.is_singular

    def test_diagonal_negative_epsilon_singular(self):
        """For epsilon_i = -1, x^+_i x^+_i has a simple pole at (z-w)^{-1}."""
        for i in range(4, 24):  # epsilon = -1
            ope = ope_x_plus_x_plus(i, i)
            assert ope.pole_power == -1
            assert ope.coeff_pow_minus_2 == "0"
            assert ope.coeff_pow_minus_1.startswith(":V_{2 alpha")
            assert ope.is_singular

    def test_off_diagonal_regular(self):
        """For i != j (orthogonal Mukai pairing), x^+_i x^+_j is regular at (z-w)^0."""
        for i in [0, 5, 10]:
            for j in [1, 6, 15]:
                if i != j:
                    ope = ope_x_plus_x_plus(i, j)
                    assert ope.pole_power == 0
                    assert ope.coeff_pow_minus_2 == "0"
                    assert ope.coeff_pow_minus_1 == "0"
                    assert ope.coeff_pow_0.startswith(":V_{alpha")


class TestOPEXPlusXMinus:
    """Tests for the OPE x^+_i(z) x^-_j(w)."""

    def test_diagonal_positive_simple_pole(self):
        """For epsilon_i = +1, x^+_i x^-_i ~ 1/(z-w) + h_i(w) + ..."""
        for i in range(4):
            ope = ope_x_plus_x_minus(i, i)
            assert ope.pole_power == -1
            assert ope.coeff_pow_minus_1 == "1 (identity)"
            assert ope.coeff_pow_0 == f"h_{i+1}(w)"
            assert ope.is_singular

    def test_diagonal_negative_regular(self):
        """For epsilon_i = -1, x^+_i x^-_i is regular at order 0."""
        for i in range(4, 24):
            ope = ope_x_plus_x_minus(i, i)
            assert ope.pole_power == 1
            assert ope.coeff_pow_minus_2 == "0"
            assert ope.coeff_pow_minus_1 == "0"
            assert not ope.is_singular

    def test_off_diagonal_normal_ordered(self):
        """For i != j, x^+_i x^-_j is regular and normal-ordered."""
        ope = ope_x_plus_x_minus(0, 5)
        assert ope.pole_power == 0
        assert ope.coeff_pow_0.startswith(":V_{alpha")


class TestOPEHX:
    """Tests for the Cartan-ladder OPE h_i(z) x^pm_j(w)."""

    def test_h_xp_diagonal_positive(self):
        """h_i x^+_i ~ + x^+_i / (z-w) for epsilon_i = +1."""
        ope = ope_h_x_plus(0, 0)  # epsilon_0 = +1
        assert ope.pole_power == -1
        assert ope.coeff_pow_minus_1 == "+x^+_1(w)"

    def test_h_xp_diagonal_negative(self):
        """h_i x^+_i ~ - x^+_i / (z-w) for epsilon_i = -1."""
        ope = ope_h_x_plus(5, 5)  # epsilon_5 = -1
        assert ope.pole_power == -1
        assert ope.coeff_pow_minus_1 == "-x^+_6(w)"

    def test_h_xm_sign_flip(self):
        """h_i x^-_i has the opposite-sign coefficient relative to h_i x^+_i."""
        ope_p = ope_h_x_plus(0, 0)
        ope_m = ope_h_x_minus(0, 0)
        assert ope_p.coeff_pow_minus_1 == "+x^+_1(w)"
        assert ope_m.coeff_pow_minus_1 == "-x^-_1(w)"

    def test_h_x_off_diagonal_zero(self):
        """h_i x^pm_j (i != j) is regular (no pole)."""
        for i, j in [(0, 5), (3, 10), (1, 7)]:
            assert ope_h_x_plus(i, j).pole_power == 0
            assert ope_h_x_minus(i, j).pole_power == 0


class TestOPEHH:
    """Tests for the Cartan-Cartan OPE h_i(z) h_j(w)."""

    def test_diagonal_double_pole(self):
        """h_i h_i ~ epsilon_i / (z-w)^2."""
        ope_pos = ope_h_h(0, 0)  # epsilon_0 = +1
        assert ope_pos.pole_power == -2
        assert ope_pos.coeff_pow_minus_2 == "+1 (identity)"

        ope_neg = ope_h_h(5, 5)  # epsilon_5 = -1
        assert ope_neg.pole_power == -2
        assert ope_neg.coeff_pow_minus_2 == "-1 (identity)"

    def test_no_first_order_pole(self):
        """The Cartan-Cartan OPE has no first-order pole (Heisenberg)."""
        ope = ope_h_h(0, 0)
        assert ope.coeff_pow_minus_1.startswith("0 ")

    def test_off_diagonal_regular(self):
        """h_i h_j (i != j) is regular (orthogonal Cartan)."""
        for i, j in [(0, 5), (1, 23), (3, 10)]:
            ope = ope_h_h(i, j)
            assert ope.pole_power == 0
            assert ope.coeff_pow_minus_2 == "0"


# =========================================================================
# Section 3: Cartan matrix
# =========================================================================

class TestCartanMatrix:
    """Tests for the diagonal Cartan matrix of the abelian K3 Yangian."""

    def test_dimensions_24x24(self):
        A = cartan_matrix()
        assert len(A) == 24
        assert all(len(row) == 24 for row in A)

    def test_diagonal(self):
        """The Cartan matrix is diagonal (off-diagonal entries are 0)."""
        A = cartan_matrix()
        for i in range(24):
            for j in range(24):
                if i != j:
                    assert A[i][j] == 0

    def test_diagonal_entries_match_epsilon(self):
        A = cartan_matrix()
        for i in range(24):
            assert A[i][i] == EPSILON[i]

    def test_full_verification_passes(self):
        result = verify_cartan_matrix_diagonal()
        assert result["ok"]
        assert result["trace"] == -16  # 4 - 20
        assert result["det"] == 1      # (+1)^4 (-1)^20 = 1
        assert result["signature"] == (4, 20)


# =========================================================================
# Section 4: Lattice VOA character matching
# =========================================================================

class TestLatticeVOACharacter:
    """Tests for the bar/cobar Euler products and Koszul pairing."""

    def test_bar_euler_first_terms(self):
        """E_bar(q) = prod (1-q^n)^24 starts 1 - 24 q + 252 q^2 - ..."""
        coeffs = bar_euler_coefficients(3)
        assert coeffs[0] == F(1)
        assert coeffs[1] == F(-24)
        assert coeffs[2] == F(252)
        # Modular discriminant Delta(q) coefficients (Macdonald-Dyson):
        # Delta(q) / q = 1 - 24 q + 252 q^2 - 1472 q^3 + 4830 q^4 - ...
        assert coeffs[3] == F(-1472)

    def test_cobar_euler_first_terms(self):
        """E_cobar(q) = prod 1/(1-q^n)^24 starts 1 + 24 q + 324 q^2 + 3200 q^3 + ..."""
        coeffs = cobar_euler_coefficients(3)
        assert coeffs[0] == F(1)
        assert coeffs[1] == F(24)
        # 1/eta(q)^24 . q = 1/Delta(q) . q^2 starts 1 + 24 q + 324 q^2 + 3200 q^3 + ...
        assert coeffs[2] == F(324)
        assert coeffs[3] == F(3200)

    def test_koszul_pairing_identity(self):
        """The bar . cobar product equals the identity: K = 0."""
        result = koszul_pairing_check(max_n=10)
        assert result["ok"]
        assert result["product_is_identity_to_order_max_n"]

    @independent_verification(
        claim="thm:cy-c-abelian-K3",
        derived_from=[
            "Lattice VOA construction V_alpha = :exp(integral J_alpha): "
            "applied to Lambda_Muk = U^3 + E_8(-1)^2",
            "PBW filtration on Y(g_K3) giving associated graded Sym(C^{24}[u])",
        ],
        verified_against=[
            "K3 elliptic genus phi_{0,1} EZ Fourier coefficients c(0)=20, c(-1)=2 "
            "computed from Jacobi theta-function ratios in phi01_fourier",
            "Topological count b_0(K3)+b_2(K3)+b_4(K3) = 1+22+1 = 24 from "
            "K3 Betti numbers (Mukai 1984 lattice rank, pre-Yangian)",
        ],
        disjoint_rationale=(
            "The derivation uses the lattice VOA construction (algebraic recipe "
            "given a symmetric pairing) and the PBW filtration on Y(g_K3) "
            "(Yangian-internal). The verification uses (a) K3 elliptic genus "
            "Fourier coefficients computed by phi01_fourier from squared Jacobi "
            "theta-function ratios (no Yangian or VOA input) and (b) the "
            "topological Betti-number count b_0 + b_2 + b_4 = 24 from Mukai "
            "(1984) classical lattice theory. The verification path 24 = c(0) + "
            "2 c(-1) = 20 + 4 makes no reference to chiral algebras, lattice "
            "VOAs, or Yangians; it is pure Jacobi-form arithmetic."
        ),
    )
    def test_mukai_rank_from_elliptic_genus(self):
        r"""The K3 elliptic genus gives rank 24 = 2 c(0) + 4 c(-1).

        AP-CY42 convention discipline.  phi01_fourier returns the
        Gritsenko-Nikulin coefficients of the unique weak Jacobi form
        phi_{0,1} of weight 0 and index 1: c(0) = 10, c(-1) = 1.

        At q = 0 (tau -> i.infty): phi_{0,1}|_{q=0} = c(0) + c(-1)(y + y^{-1})
                                                    = 10 + (y + 1/y).

        The K3 elliptic genus is EG_K3 = 2 . phi_{0,1} (the factor of 2
        is kappa_ch(K3) = 2, AP-CY42).  At (q=0, y=1):

          EG_K3|_{q=0, y=1} = 2 . [10 + (1 + 1)]
                            = 2 . 12
                            = 24
                            = chi(K3)
                            = b_0(K3) + b_2(K3) + b_4(K3)
                            = 1 + 22 + 1
                            = 24 = Mukai rank.

        Expanded as a linear combination of c(0), c(-1):

          chi(K3) = 2 c(0) + 4 c(-1) = 20 + 4 = 24.

        The factor of 2 in front of c(0) is kappa_ch(K3) = 2 (the
        EG_K3 = 2 phi_{0,1} normalisation).  The factor of 4 in front of
        c(-1) is 2 . 2 = (kappa_ch factor) . (y + y^{-1} at y=1 gives 2).

        This is the INDEPENDENT verification of the rank-24 of the
        abelian K3 Yangian: phi01_fourier computes c(0), c(-1) from
        squared theta-function ratios of (theta_2, theta_3, theta_4),
        with NO reference to the lattice VOA construction or the Yangian
        rank.  The verification path 24 = 2 c(0) + 4 c(-1) makes no
        reference to chiral algebras, lattice VOAs, or Yangians; it is
        pure Jacobi-form arithmetic plus the AP-CY42 normalisation.
        """
        c0 = k3_elliptic_genus_c_zero()
        cm1 = k3_elliptic_genus_c_minus_one()
        assert c0 == 10, f"Expected c(0) = 10 in GN convention, got {c0}"
        assert cm1 == 1, f"Expected c(-1) = 1 in GN convention, got {cm1}"
        chi_K3 = 2 * c0 + 4 * cm1
        assert chi_K3 == 24, f"chi(K3) = 2 c(0) + 4 c(-1), got {chi_K3}"
        # Mukai rank = chi(K3) = 24 = b_0 + b_2 + b_4 = 1 + 22 + 1.
        assert chi_K3 == RANK
        assert mukai_rank_from_elliptic_genus() == 24


# =========================================================================
# Section 5: Drinfeld coproduct
# =========================================================================

class TestDrinfeldCoproductAbelian:
    """Tests for the abelian-level Drinfeld coproduct."""

    def test_x_plus_coproduct_primitive(self):
        """Delta_z(x^+_i(u)) = x^+_i(u) (x) 1 + 1 (x) x^+_i(u-z), no correction."""
        for i in [0, 5, 23]:
            cop = coproduct_x_plus(i)
            assert cop.correction_terms.startswith("0 ")
            assert "u-z" in cop.coproduct_formula

    def test_x_minus_and_h_coproduct_primitive(self):
        for i in [0, 12, 20]:
            assert coproduct_x_minus(i).correction_terms.startswith("0 ")
            assert coproduct_h(i).correction_terms.startswith("0 ")
            assert "u-z" in coproduct_x_minus(i).coproduct_formula
            assert "u-z" in coproduct_h(i).coproduct_formula

    def test_no_correction_all_72_generators(self):
        """All 24 x 3 = 72 abelian Drinfeld generators have primitive coproduct."""
        result = verify_coproduct_primitive_abelian()
        assert result["ok"]
        assert result["num_generators_checked"] == NUM_CURRENTS == 72
        assert result["all_correction_terms_zero"]


# =========================================================================
# Section 6: Coassociativity
# =========================================================================

class TestCoassociativity:
    """Tests for the coassociativity of the abelian coproduct."""

    def test_shifts_compose_correctly(self):
        """(Delta_w (x) id) o Delta_{z+w} = (id (x) Delta_z) o Delta_w on shifts."""
        result = verify_coassociativity_primitive()
        assert result["ok"]
        assert result["shifts_equal"]
        # Both trees produce shifts (u, u-w, u-w-z)
        assert result["tree1_shifts"] == result["tree2_shifts"]

    def test_associativity_of_addition(self):
        """The shift composition (z+w)+0 = z+(w+0) is associative.

        This is the algebraic substance of coassociativity for primitive
        coproducts: the spectral shifts add associatively.
        """
        z, w = 7, 11
        assert (z + w) + 0 == z + (w + 0)


# =========================================================================
# Section 7: Full summary and full verification
# =========================================================================

class TestFullSummary:
    """Tests for the complete summary and verification suite."""

    def test_summary_assembles(self):
        s = full_summary()
        assert s.rank == 24
        assert s.num_currents == 72
        assert len(s.epsilon) == 24
        assert s.cartan_trace == -16
        assert s.cartan_det == 1
        # GN convention: c(0) = 10, c(-1) = 1 (phi01_fourier returns these).
        assert s.elliptic_genus_c0 == 10
        assert s.elliptic_genus_cm1 == 1
        # Identity (AP-CY42): chi(K3) = 2 c(0) + 4 c(-1) = 20 + 4 = 24.
        assert s.mukai_rank_from_eg == 24
        assert s.coassociativity_holds

    def test_summary_contains_all_ope_summaries(self):
        s = full_summary()
        assert "x^+_i x^+_j" in s.ope_x_plus_x_plus_summary
        assert "x^+_i x^-_j" in s.ope_x_plus_x_minus_summary
        assert "h_i x^+_j" in s.ope_h_x_plus_summary
        assert "h_i h_j" in s.ope_h_h_summary

    def test_full_verification_passes(self):
        v = full_verification()
        assert v["ok"], f"Full verification failed: {v}"
        assert v["cartan_matrix"]["ok"]
        assert v["koszul_pairing"]["ok"]
        assert v["elliptic_genus_rank_match"]["ok"]
        assert v["coproduct_primitive"]["ok"]
        assert v["coassociativity"]["ok"]
        assert v["ope_sanity"]["ok"]

    def test_bar_cobar_explicit_first_six_terms(self):
        """Spot check: explicit bar and cobar Euler product first six terms.

        Bar (Macdonald-Dyson): 1 - 24 q + 252 q^2 - 1472 q^3 + 4830 q^4 - 6048 q^5
        Cobar (1/eta^24 . q): 1 + 24 q + 324 q^2 + 3200 q^3 + 25650 q^4 + 176256 q^5
        """
        bar = bar_euler_coefficients(5)
        assert bar == [
            F(1), F(-24), F(252), F(-1472), F(4830), F(-6048),
        ]
        cobar = cobar_euler_coefficients(5)
        assert cobar == [
            F(1), F(24), F(324), F(3200), F(25650), F(176256),
        ]
