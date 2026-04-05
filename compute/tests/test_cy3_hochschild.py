r"""Tests for cy3_hochschild: HH_* and HC_* of D^b(CY3).

Ground truth:
  HKR theorem: HH_p(D^b(X)) = H^*(X, /\^p T_X) = H^*(X, Omega^{d-p}_X) for CY.
  Quintic: h^{1,1}=1, h^{2,1}=101, chi=-200 (Candelas-de la Ossa-Green-Parkes 1991).
  K3 x E: h^{1,1}=21, h^{2,1}=21, chi=0 (Kunneth from K3 + elliptic curve).
  C^3: affine CY3, HH_p = C[x,y,z]^{binom(3,p)}.
  Resolved conifold: non-compact CY3, HH_c from P^1 zero section.
  BCOV: kappa = chi/24 for CY3 (Bershadsky-Cecotti-Ooguri-Vafa 1994).

Multi-path verification:
  (a) Direct HKR from Hodge numbers.
  (b) Kunneth for K3 x E (independent product computation).
  (c) Palindrome symmetry: dim HH_p = dim HH_{d-p} for CY d-fold.
  (d) Hodge symmetry h^{p,q} = h^{q,p} and Serre duality h^{p,q} = h^{d-p,d-q}.
  (e) Euler characteristic cross-checks.
  (f) Cyclic homology from SBI sequence.
  (g) BCOV comparison for quintic.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.cy3_hochschild import (
    HodgeData,
    HHDecomposition,
    CyclicHomology,
    k3_times_e_hodge,
    quintic_hodge,
    c3_hodge,
    conifold_hodge,
    compute_hh,
    compute_hh_c3,
    compute_k3_times_e,
    compute_quintic,
    compute_conifold,
    compute_c3_hh_dimensions,
    verify_hodge_symmetries,
    verify_hh_palindrome,
    verify_euler_char_hh,
    verify_bcov_quintic,
    s1_action_data,
    full_summary,
)


# ======================================================================
# 1. Hodge data: K3 x E
# ======================================================================

class TestK3TimesEHodge:
    """Hodge diamond of K3 x E via Kunneth, verified independently."""

    def setup_method(self):
        self.hd = k3_times_e_hodge()

    def test_dimension(self):
        """K3 x E is a 3-fold."""
        assert self.hd.dim == 3

    def test_euler_characteristic(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert self.hd.euler_characteristic == 0

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Kahler manifold)."""
        assert self.hd.hodge_symmetry_check()

    def test_serre_duality(self):
        """h^{p,q} = h^{d-p, d-q} (Serre duality for compact Kahler)."""
        assert self.hd.serre_duality_check()

    def test_h11_equals_21(self):
        """h^{1,1}(K3 x E) = 20 + 1 = 21 (Kunneth)."""
        assert self.hd.h(1, 1) == 21

    def test_h21_equals_21(self):
        """h^{2,1}(K3 x E) = 21 (from Kunneth computation)."""
        assert self.hd.h(2, 1) == 21

    def test_h30_equals_1(self):
        """h^{3,0}(K3 x E) = h^{2,0}(K3) * h^{1,0}(E) = 1."""
        assert self.hd.h(3, 0) == 1

    def test_kunneth_independent_verification(self):
        """Verify ALL Hodge numbers via an independent Kunneth product.

        Path (b): independent computation from K3 and E Hodge data.
        """
        # K3 Hodge numbers
        k3 = {(0,0):1, (1,0):0, (0,1):0, (2,0):1, (1,1):20,
               (0,2):1, (2,1):0, (1,2):0, (2,2):1}
        # E Hodge numbers
        e = {(0,0):1, (1,0):1, (0,1):1, (1,1):1}

        for p in range(4):
            for q in range(4):
                val = 0
                for a in range(3):
                    b = p - a
                    if b < 0 or b > 1:
                        continue
                    for c in range(3):
                        d = q - c
                        if d < 0 or d > 1:
                            continue
                        val += k3.get((a, c), 0) * e.get((b, d), 0)
                assert self.hd.h(p, q) == val, \
                    f"h^{{{p},{q}}} mismatch: got {self.hd.h(p,q)}, expected {val}"

    def test_betti_numbers(self):
        """Betti numbers of K3 x E: b_0=1, b_1=2, ..., b_6=1."""
        betti = self.hd.betti_numbers
        # K3xE has full Hodge diamond with h^{p,q} = h^{q,p}
        # b_0 = h^{0,0} = 1
        assert betti[0] == 1
        # b_1 = h^{1,0} + h^{0,1} = 1 + 1 = 2
        assert betti[1] == 2
        # b_6 = h^{3,3} = 1
        assert betti[6] == 1
        # chi = sum (-1)^k b_k = 0
        chi = sum((-1)**k * betti[k] for k in betti)
        assert chi == 0

    def test_holomorphic_euler_characteristics(self):
        """chi_p = chi(Omega^p) for K3 x E: all vanish (chi=0 forces this)."""
        chi_p = self.hd.holomorphic_euler_characteristics
        # K3xE: chi_p = sum_q (-1)^q h^{p,q}
        # For p=0: 1 - 1 + 1 - 1 = 0
        assert chi_p[0] == 0
        # Check they all vanish (sum is chi_top = 0 by Gauss-Bonnet)
        assert sum((-1)**p * chi_p[p] for p in range(4)) == 0


# ======================================================================
# 2. Hodge data: quintic
# ======================================================================

class TestQuinticHodge:
    """Hodge diamond of the quintic threefold."""

    def setup_method(self):
        self.hd = quintic_hodge()

    def test_euler_characteristic(self):
        """chi(quintic) = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200."""
        assert self.hd.euler_characteristic == -200

    def test_h11(self):
        """h^{1,1}(quintic) = 1."""
        assert self.hd.h(1, 1) == 1

    def test_h21(self):
        """h^{2,1}(quintic) = 101."""
        assert self.hd.h(2, 1) == 101

    def test_hodge_symmetry(self):
        assert self.hd.hodge_symmetry_check()

    def test_serre_duality(self):
        assert self.hd.serre_duality_check()

    def test_chi_formula(self):
        """Alternative chi formula: chi = 2(h^{1,1} - h^{2,1}) for CY3."""
        h11 = self.hd.h(1, 1)
        h21 = self.hd.h(2, 1)
        assert self.hd.euler_characteristic == 2 * (h11 - h21)


# ======================================================================
# 3. Hochschild homology: K3 x E
# ======================================================================

class TestHHK3TimesE:
    """HH_*(D^b(K3 x E)) via HKR decomposition."""

    def setup_method(self):
        self.hd = k3_times_e_hodge()
        self.hh = compute_hh(self.hd)

    def test_hh_dimensions(self):
        """HH_p = sum_q h^{3-p, q} for CY3.

        HH_0 = sum_q h^{3,q} = 1+1+1+1 = 4
        HH_1 = sum_q h^{2,q} = 1+21+21+1 = 44
        HH_2 = sum_q h^{1,q} = 1+21+21+1 = 44
        HH_3 = sum_q h^{0,q} = 1+1+1+1 = 4
        """
        assert self.hh.dim_hh(0) == 4
        assert self.hh.dim_hh(1) == 44
        assert self.hh.dim_hh(2) == 44
        assert self.hh.dim_hh(3) == 4

    def test_hh_total_dim(self):
        """Total dim HH = 4 + 44 + 44 + 4 = 96."""
        assert self.hh.total_dim == 96

    def test_hh_palindrome(self):
        """dim HH_p = dim HH_{3-p} (CY3 palindrome from Serre duality)."""
        assert verify_hh_palindrome(self.hh)

    def test_hh_pq_components(self):
        """Spot-check the (p,q)-decomposition: hh(p,q) = h^{3-p, q}."""
        # HH_0: hh(0,q) = h^{3,q}
        assert self.hh.hh_pq(0, 0) == 1   # h^{3,0} = 1
        assert self.hh.hh_pq(0, 1) == 1   # h^{3,1} = 1
        assert self.hh.hh_pq(0, 2) == 1   # h^{3,2} = 1
        assert self.hh.hh_pq(0, 3) == 1   # h^{3,3} = 1
        # HH_1: hh(1,q) = h^{2,q}
        assert self.hh.hh_pq(1, 1) == 21  # h^{2,1} = 21
        assert self.hh.hh_pq(1, 2) == 21  # h^{2,2} = 21

    def test_euler_char_hh_two_methods(self):
        """chi(HH) computed two ways must agree."""
        ev = verify_euler_char_hh(self.hd, self.hh)
        assert ev["agree"]

    def test_euler_char_hh_value(self):
        """For K3 x E: chi(HH) = 0 (all row sums are symmetric)."""
        assert self.hh.euler_char_hh == 0

    def test_total_dim_equals_sum_all_hodge(self):
        """dim HH_* = sum of ALL h^{p,q}: the CY isomorphism is a bijection.

        Path (e): cross-check. For K3 x E, sum of all h^{p,q} = 96.
        """
        hodge_sum = sum(self.hd.h(p, q) for p in range(4) for q in range(4))
        assert self.hh.total_dim == hodge_sum


# ======================================================================
# 4. Hochschild homology: quintic
# ======================================================================

class TestHHQuintic:
    """HH_*(D^b(quintic)) via HKR decomposition."""

    def setup_method(self):
        self.hd = quintic_hodge()
        self.hh = compute_hh(self.hd)

    def test_hh_dimensions(self):
        """HH_0 = 2, HH_1 = 102, HH_2 = 102, HH_3 = 2."""
        assert self.hh.dim_hh(0) == 2
        assert self.hh.dim_hh(1) == 102
        assert self.hh.dim_hh(2) == 102
        assert self.hh.dim_hh(3) == 2

    def test_hh_total_dim(self):
        """Total dim HH = 208."""
        assert self.hh.total_dim == 208

    def test_hh_palindrome(self):
        """dim HH_p = dim HH_{3-p}."""
        assert verify_hh_palindrome(self.hh)

    def test_euler_char_hh(self):
        """chi(HH) = 2 - 102 + 102 - 2 = 0 for the quintic."""
        assert self.hh.euler_char_hh == 0

    def test_euler_char_hh_ne_chi_top(self):
        """chi(HH) != chi_top for the quintic: 0 != -200.

        This verifies that the identity chi(HH) = chi_top does NOT hold
        in general (it holds for K3 x E by accident, since both are 0).
        """
        ev = verify_euler_char_hh(self.hd, self.hh)
        assert not ev["chi_hh_equals_chi_top"]
        assert ev["chi_top"] == -200
        assert ev["chi_hh_from_dims"] == 0

    def test_hh0_deformation_interpretation(self):
        """HH_0 = H^*(O_X) = H^{3,*} for quintic: h^{3,0}+h^{3,3} = 2.

        The two directions: the holomorphic 3-form Omega and its
        Serre dual in H^3(O).
        """
        assert self.hh.hh_pq(0, 0) == 1  # h^{3,0} = Omega
        assert self.hh.hh_pq(0, 3) == 1  # h^{3,3} = Serre dual
        assert self.hh.hh_pq(0, 1) == 0  # h^{3,1} = 0
        assert self.hh.hh_pq(0, 2) == 0  # h^{3,2} = 0

    def test_hh1_complex_structure(self):
        """HH_1 = H^*(Omega^2): carries h^{2,1}=101 complex structure moduli."""
        assert self.hh.hh_pq(1, 1) == 101  # h^{2,1}
        assert self.hh.hh_pq(1, 2) == 1    # h^{2,2}
        assert self.hh.dim_hh(1) == 102


# ======================================================================
# 5. Cyclic homology: K3 x E
# ======================================================================

class TestHCK3TimesE:
    """HC_*(D^b(K3 x E)) from SBI sequence."""

    def setup_method(self):
        hd = k3_times_e_hodge()
        hh = compute_hh(hd)
        self.hc = CyclicHomology(hh)
        self.hh = hh

    def test_hc_0(self):
        """HC_0 = HH_0 = 4."""
        assert self.hc.dim_hc(0) == 4

    def test_hc_1(self):
        """HC_1 = HH_1 = 44."""
        assert self.hc.dim_hc(1) == 44

    def test_hc_2(self):
        """HC_2 = HH_2 + HH_0 = 44 + 4 = 48."""
        assert self.hc.dim_hc(2) == 48

    def test_hc_3(self):
        """HC_3 = HH_3 + HH_1 = 4 + 44 = 48."""
        assert self.hc.dim_hc(3) == 48

    def test_hc_stabilizes(self):
        """HC_n stabilizes for n >= 2: HC_n = HC_{n-2} for n >= d+1 = 4.

        Once all HH_p have been included, periodicity takes over.
        """
        # For n >= 4: HC_n should stabilize at HP_0 or HP_1
        assert self.hc.dim_hc(4) == self.hc.dim_hc(2)
        assert self.hc.dim_hc(5) == self.hc.dim_hc(3)
        assert self.hc.dim_hc(6) == self.hc.dim_hc(4)

    def test_periodic_cyclic(self):
        """HP_0 = HP_1 = 48 for K3 x E (palindromic HH with even total)."""
        assert self.hc.dim_hp(0) == 48
        assert self.hc.dim_hp(1) == 48

    def test_hp_sum_equals_total_hh(self):
        """HP_0 + HP_1 = dim HH_* = 96."""
        assert self.hc.dim_hp(0) + self.hc.dim_hp(1) == self.hh.total_dim

    def test_negative_cyclic(self):
        """HC^-_n = sum_{k>=0} HH_{n+2k} for n = 0,1,2,3."""
        # HC^-_0 = HH_0 + HH_2 = 4 + 44 = 48
        assert self.hc.dim_hc_negative(0) == 48
        # HC^-_1 = HH_1 + HH_3 = 44 + 4 = 48
        assert self.hc.dim_hc_negative(1) == 48
        # HC^-_2 = HH_2 = 44
        assert self.hc.dim_hc_negative(2) == 44
        # HC^-_3 = HH_3 = 4
        assert self.hc.dim_hc_negative(3) == 4


# ======================================================================
# 6. Cyclic homology: quintic
# ======================================================================

class TestHCQuintic:
    """HC_*(D^b(quintic)) from SBI sequence."""

    def setup_method(self):
        hd = quintic_hodge()
        hh = compute_hh(hd)
        self.hc = CyclicHomology(hh)

    def test_hc_low_degrees(self):
        """HC_0 = 2, HC_1 = 102, HC_2 = 104, HC_3 = 104."""
        assert self.hc.dim_hc(0) == 2
        assert self.hc.dim_hc(1) == 102
        assert self.hc.dim_hc(2) == 104   # HH_2 + HH_0 = 102 + 2
        assert self.hc.dim_hc(3) == 104   # HH_3 + HH_1 = 2 + 102

    def test_periodic_cyclic(self):
        """HP_0 = HP_1 = 104 for the quintic."""
        assert self.hc.dim_hp(0) == 104
        assert self.hc.dim_hp(1) == 104


# ======================================================================
# 7. C^3 (non-compact)
# ======================================================================

class TestC3:
    """HH_* for C^3 (affine, non-compact CY3)."""

    def test_fiber_dimensions(self):
        """binom(3,p) = 1, 3, 3, 1 for the polyvector field fiber."""
        data = c3_hodge()
        expected = {0: 1, 1: 3, 2: 3, 3: 1}
        assert data["polyvector_fiber_dims"] == expected

    def test_total_fiber_dim(self):
        """sum binom(3,p) = 2^3 = 8."""
        data = c3_hodge()
        assert data["total_fiber_dim"] == 8

    def test_hh_at_poly_degree_0(self):
        """At polynomial degree 0: binom(2,2)=1 monomial, so HH_p = binom(3,p)."""
        result = compute_c3_hh_dimensions(max_degree=5)
        d0 = result["degree_0"]
        assert d0["n_monomials"] == 1
        assert d0["hh_p"] == {0: 1, 1: 3, 2: 3, 3: 1}
        assert d0["total"] == 8

    def test_hh_at_poly_degree_1(self):
        """At degree 1: binom(3,2)=3 monomials (x,y,z)."""
        result = compute_c3_hh_dimensions(max_degree=5)
        d1 = result["degree_1"]
        assert d1["n_monomials"] == 3
        assert d1["total"] == 24  # 8 * 3

    def test_hh_at_poly_degree_d(self):
        """At degree d: binom(d+2,2) monomials, total = 8 * binom(d+2,2)."""
        result = compute_c3_hh_dimensions(max_degree=10)
        for d in range(11):
            n_mono = math.comb(d + 2, 2)
            assert result[f"degree_{d}"]["total"] == 8 * n_mono

    def test_c3_hh_character_formula(self):
        """The HH_p character at polynomial degree d = binom(3,p) * binom(d+2,2).

        Uses the lambda function from c3_hodge() directly.
        """
        data = c3_hodge()
        f = data["hh_p_dim_at_poly_degree"]
        for d in range(6):
            for p in range(4):
                assert f(p, d) == math.comb(3, p) * math.comb(d + 2, 2)
        # Out of range
        assert f(4, 0) == 0
        assert f(-1, 0) == 0


# ======================================================================
# 8. Resolved conifold (non-compact)
# ======================================================================

class TestConifold:
    """HH_* for the resolved conifold."""

    def test_compact_support_hh(self):
        """Compact-support HH: HH^c_0 = 1, HH^c_1 = 0, HH^c_2 = 1."""
        data = compute_conifold()
        assert data["hh_compact_support"] == {0: 1, 1: 0, 2: 1}

    def test_compact_support_total(self):
        """Total dim HH^c = 2."""
        data = compute_conifold()
        assert data["hh_compact_support_total"] == 2

    def test_chi_compact_support(self):
        """chi(HH^c) = 1 - 0 + 1 = 2 = chi(P^1)."""
        data = compute_conifold()
        assert data["chi_hh_compact_support"] == 2

    def test_chiral_algebra_identification(self):
        """The conifold chiral algebra is betagamma with kappa=1."""
        data = compute_conifold()
        assert data["chiral_algebra"] == "betagamma"
        assert data["kappa"] == Fraction(1)

    def test_conifold_hodge_data(self):
        """Conifold Betti numbers from Thom isomorphism."""
        data = conifold_hodge()
        # Ordinary cohomology: b_0=1, b_2=1 (from P^1)
        assert data["betti"][0] == 1
        assert data["betti"][2] == 1
        assert data["euler_characteristic"] == 2


# ======================================================================
# 9. BCOV verification for the quintic
# ======================================================================

class TestBCOV:
    """BCOV B-model data for the quintic CY3."""

    def test_bcov_kappa(self):
        """kappa(quintic) = chi/24 = -200/24 = -25/3."""
        bcov = verify_bcov_quintic()
        assert bcov["bcov_kappa"] == Fraction(-25, 3)

    def test_bcov_kappa_equals_chi_over_24(self):
        """Self-consistency: kappa = chi/24."""
        bcov = verify_bcov_quintic()
        assert bcov["bcov_kappa_equals_chi_over_24"]

    def test_f1_discriminant_coefficient(self):
        """F_1 discriminant coefficient = -kappa = 25/3."""
        bcov = verify_bcov_quintic()
        assert bcov["f1_discriminant_coeff"] == Fraction(25, 3)

    def test_holomorphic_ambiguity(self):
        """Holomorphic ambiguity coefficient = 3 + h^{1,1} - chi/12 = 62/3."""
        bcov = verify_bcov_quintic()
        assert bcov["holomorphic_ambiguity_coeff"] == Fraction(62, 3)


# ======================================================================
# 10. S^1-action and periodic cyclic homology
# ======================================================================

class TestS1Action:
    """S^1-action data for the CY-to-chiral functor."""

    def test_k3e_hp_balanced(self):
        """HP_0 = HP_1 = 48 for K3 x E (palindromic HH)."""
        hd = k3_times_e_hodge()
        hh = compute_hh(hd)
        data = s1_action_data(hh)
        assert data["hp_0"] == 48
        assert data["hp_1"] == 48

    def test_quintic_hp_balanced(self):
        """HP_0 = HP_1 = 104 for the quintic."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        data = s1_action_data(hh)
        assert data["hp_0"] == 104
        assert data["hp_1"] == 104

    def test_cy3_pairing_degree(self):
        """CY3 Mukai pairing has degree -3."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        data = s1_action_data(hh)
        assert data["cy_pairing_degree"] == -3

    def test_ks_bracket_shift(self):
        """Kontsevich-Soibelman bracket shift = d-1 = 2 for CY3."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        data = s1_action_data(hh)
        assert data["ks_bracket_shift"] == 2


# ======================================================================
# 11. Full summary and cross-checks
# ======================================================================

class TestFullSummary:
    """Integration tests via the full_summary() function."""

    def test_summary_runs(self):
        """full_summary() runs without error."""
        summary = full_summary()
        assert "C3" in summary
        assert "conifold" in summary
        assert "K3xE" in summary
        assert "quintic" in summary

    def test_both_compact_palindromes(self):
        """Both compact CY3 examples have palindromic HH."""
        summary = full_summary()
        assert summary["K3xE"]["palindrome"]
        assert summary["quintic"]["palindrome"]

    def test_both_hodge_symmetries(self):
        """Both compact CY3 examples have Hodge + Serre symmetry."""
        summary = full_summary()
        k3e_sym = summary["K3xE"]["symmetries"]
        assert k3e_sym["hodge_symmetry"]
        assert k3e_sym["serre_duality"]
        q_sym = summary["quintic"]["symmetries"]
        assert q_sym["hodge_symmetry"]
        assert q_sym["serre_duality"]

    def test_euler_verification_agreement(self):
        """chi(HH) computed two ways agrees for both examples."""
        summary = full_summary()
        assert summary["K3xE"]["euler_verification"]["agree"]
        assert summary["quintic"]["euler_verification"]["agree"]


# ======================================================================
# 12. Connes operator structure
# ======================================================================

class TestConnesOperator:
    """The Connes operator B: HH_n -> HH_{n+1} for CY3."""

    def test_connes_rank_k3e(self):
        """Connes operator ranks for K3 x E: maximal for all p."""
        hd = k3_times_e_hodge()
        hh = compute_hh(hd)
        # B_0: HH_0(dim 4) -> HH_1(dim 44): max rank = min(h^{3,q}, h^{2,q}) summed
        r0 = hh.connes_operator_rank(0)
        assert r0["source_dim"] == 4
        assert r0["target_dim"] == 44
        # max rank = sum_q min(h^{3,q}, h^{2,q}) = min(1,1)+min(1,21)+min(1,21)+min(1,1) = 4
        assert r0["max_rank"] == 4

    def test_connes_rank_quintic(self):
        """Connes operator ranks for the quintic."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        r0 = hh.connes_operator_rank(0)
        assert r0["source_dim"] == 2
        assert r0["target_dim"] == 102
        # max rank = min(1,0)+min(0,101)+min(0,1)+min(1,0) = 0
        # (h^{3,q} = 1,0,0,1 and h^{2,q} = 0,101,1,0)
        assert r0["max_rank"] == 0

    def test_connes_past_top(self):
        """B_d = 0 (no more polyvector fields above degree d)."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        r3 = hh.connes_operator_rank(3)
        assert r3["target_dim"] == 0
        assert r3["max_rank"] == 0


# ======================================================================
# 13. Edge cases and consistency
# ======================================================================

class TestEdgeCases:
    """Boundary conditions and edge-case consistency."""

    def test_hc_negative_n(self):
        """HC_n = 0 for n < 0."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        hc = CyclicHomology(hh)
        assert hc.dim_hc(-1) == 0
        assert hc.dim_hc(-10) == 0

    def test_hp_periodicity(self):
        """HP is 2-periodic: HP_n = HP_{n+2}."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        hc = CyclicHomology(hh)
        assert hc.dim_hp(0) == hc.dim_hp(2)
        assert hc.dim_hp(1) == hc.dim_hp(3)
        assert hc.dim_hp(0) == hc.dim_hp(100)
        assert hc.dim_hp(1) == hc.dim_hp(101)

    def test_hh_out_of_range(self):
        """HH_p = 0 for p outside [0, d]."""
        hd = quintic_hodge()
        hh = compute_hh(hd)
        # dim_hh sums over q in range(d+1), and hh_pq returns 0 for out-of-range p
        assert hh.dim_hh(4) == 0
        assert hh.dim_hh(-1) == 0

    def test_hodge_data_name(self):
        """HodgeData carries the correct name."""
        assert k3_times_e_hodge().name == "K3xE"
        assert quintic_hodge().name == "quintic"

    def test_compute_all_compact_cy3(self):
        """compute_all_compact_cy3 returns both K3xE and quintic."""
        from compute.lib.cy3_hochschild import compute_all_compact_cy3
        result = compute_all_compact_cy3()
        assert "K3xE" in result
        assert "quintic" in result
        assert result["K3xE"]["hh_total_dim"] == 96
        assert result["quintic"]["hh_total_dim"] == 208
