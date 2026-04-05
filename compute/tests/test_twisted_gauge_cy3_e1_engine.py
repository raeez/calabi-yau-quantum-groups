r"""Tests for twisted gauge theories on CY3 and E_1 chiral algebra dictionary.

Verifies the four gauge theory twists (Haydys-Witten, Costello 7d CS,
Kapustin-Witten, 5d Seiberg-Witten) and their E_1 chiral algebras.

Multi-path verification per CLAUDE.md mandate:
    Path 1: Direct computation from defining formulas
    Path 2: Independent algorithm (product vs log-exp, etc.)
    Path 3: Known values from the literature (OEIS, published tables)
    Path 4: Cross-family consistency (Koszul duality, mirror symmetry)
    Path 5: Limiting cases (rank 1, Q=1, etc.)

Ground truth sources:
    - MacMahon (1916): plane partition generating function
    - OEIS A000219: plane partition counts
    - Schiffmann-Vasserot (2013): CoHA = Y^+(gl_hat_1)
    - RSYZ (2020): cohomological Hall algebras and Yangians
    - Costello (2017): 7d CS and affine Yangian
    - Kontsevich-Soibelman (2006): stability structures and DT
    - Nekrasov (2003): refined DT and the Nekrasov partition function

BEILINSON WARNINGS:
    AP10: Every hardcoded value is cross-checked by at least 2 methods.
    AP38: Convention: M(q) = prod 1/(1-q^n)^n (NOT M(-q)).
    AP42: "Gauge = chiral" identification tested at C^3 and conifold level only.
"""

import pytest
from fractions import Fraction

from compute.lib.twisted_gauge_cy3_e1_engine import (
    macmahon,
    macmahon_product,
    euler_product,
    HaydysWittenGL1,
    CostelloSevenDCS,
    KapustinWittenGL1,
    FiveDSeibergWitten,
    BRSTBarIdentification,
    CoulombHiggsDuality,
    ConifoldGaugeTheory,
    InstantonEngine,
    GaugeChiralDictionary,
    _poly_mul,
    _poly_inv,
    _poly_pow,
    _poly_log,
    _poly_exp,
    run_full_verification,
)


# ================================================================
# POWER SERIES ARITHMETIC
# ================================================================

class TestPowerSeriesArithmetic:
    """Test the exact rational power series operations."""

    def test_poly_mul_identity(self):
        """1 * f = f."""
        N = 10
        one = [Fraction(0)] * N
        one[0] = Fraction(1)
        f = [Fraction(i + 1) for i in range(N)]
        result = _poly_mul(one, f, N)
        assert all(result[k] == f[k] for k in range(N))

    def test_poly_mul_commutativity(self):
        """f * g = g * f."""
        N = 10
        f = [Fraction(1)] * N  # 1/(1-q)
        g = [Fraction(0)] * N
        g[0] = Fraction(1)
        g[1] = Fraction(-1)  # 1-q
        p1 = _poly_mul(f, g, N)
        p2 = _poly_mul(g, f, N)
        assert all(p1[k] == p2[k] for k in range(N))

    def test_poly_inv_roundtrip(self):
        """f * f^{-1} = 1."""
        N = 15
        f = [Fraction(0)] * N
        f[0] = Fraction(1)
        f[1] = Fraction(2)
        f[2] = Fraction(-3)
        finv = _poly_inv(f, N)
        product = _poly_mul(f, finv, N)
        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0), f"f * f^(-1) != 1 at q^{k}"

    def test_poly_log_exp_roundtrip(self):
        """exp(log(f)) = f for f with f[0] = 1."""
        N = 15
        f = [Fraction(0)] * N
        f[0] = Fraction(1)
        f[1] = Fraction(3)
        f[2] = Fraction(-2)
        f[3] = Fraction(7)
        L = _poly_log(f, N)
        assert L[0] == Fraction(0), "log should have zero constant term"
        roundtrip = _poly_exp(L, N)
        for k in range(N):
            assert roundtrip[k] == f[k], f"exp(log(f)) != f at q^{k}"

    def test_poly_exp_log_roundtrip(self):
        """log(exp(g)) = g for g with g[0] = 0."""
        N = 15
        g = [Fraction(0)] * N
        g[1] = Fraction(1)
        g[2] = Fraction(-1, 2)
        g[3] = Fraction(1, 3)
        E = _poly_exp(g, N)
        assert E[0] == Fraction(1), "exp should have unit constant term"
        roundtrip = _poly_log(E, N)
        for k in range(N):
            assert roundtrip[k] == g[k], f"log(exp(g)) != g at q^{k}"


# ================================================================
# MACMAHON FUNCTION
# ================================================================

class TestMacMahon:
    """Test M(q) = prod_{n>=1} 1/(1-q^n)^n."""

    KNOWN_PP = {
        0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24,
        6: 48, 7: 86, 8: 160, 9: 282, 10: 500,
    }

    def test_macmahon_known_values(self):
        """M(q) coefficients = plane partition counts (OEIS A000219)."""
        m = macmahon(11)
        for k, expected in self.KNOWN_PP.items():
            assert int(m[k]) == expected, f"p({k}) = {int(m[k])}, expected {expected}"

    def test_macmahon_two_methods(self):
        """Cross-validate log-exp vs direct product."""
        N = 25
        m1 = macmahon(N)
        m2 = macmahon_product(N)
        for k in range(N):
            assert m1[k] == m2[k], f"Methods disagree at q^{k}: {m1[k]} vs {m2[k]}"

    def test_macmahon_constant_term(self):
        """M(0) = 1 (empty plane partition)."""
        m = macmahon(5)
        assert m[0] == Fraction(1)

    def test_macmahon_positivity(self):
        """All plane partition counts are positive."""
        m = macmahon(30)
        for k in range(30):
            assert m[k] > 0, f"p({k}) = {m[k]} is not positive"

    def test_macmahon_monotonicity(self):
        """p(n) is strictly increasing for n >= 1."""
        m = macmahon(30)
        for k in range(2, 30):
            assert m[k] > m[k - 1], f"p({k}) <= p({k-1})"

    def test_macmahon_integrality(self):
        """All coefficients are integers."""
        m = macmahon(30)
        for k in range(30):
            assert m[k].denominator == 1, f"p({k}) = {m[k]} is not integer"


# ================================================================
# GAUGE THEORY (a): HAYDYS-WITTEN / 6d N=(1,0)
# ================================================================

class TestHaydysWitten:
    """Test the 6d N=(1,0) theory twisted on CY3 = C^3."""

    def setup_method(self):
        self.hw = HaydysWittenGL1(30)

    def test_partition_function_is_macmahon(self):
        """Z = M(q) (crystal melting partition function)."""
        Z = self.hw.partition_function()
        M = macmahon(30)
        for k in range(30):
            assert Z[k] == M[k], f"Z != M(q) at q^{k}"

    def test_bps_degeneracies_are_plane_partitions(self):
        """BPS(n) = p(n) for all n."""
        bps = self.hw.bps_degeneracies()
        known = {0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24, 6: 48}
        for n, expected in known.items():
            assert bps[n] == expected, f"BPS({n}) = {bps[n]}, expected {expected}"

    def test_e1_character_equals_macmahon(self):
        """char(E_1 algebra) = M(q)."""
        ch = self.hw.e1_character()
        M = macmahon(30)
        assert all(ch[k] == M[k] for k in range(30))

    def test_hilbert_scheme_euler_chars(self):
        """chi(Hilb^n(C^3)) = p(n)."""
        for n in range(10):
            chi = self.hw.hilbert_scheme_euler_char(n)
            expected = int(macmahon(n + 1)[n])
            assert chi == expected, f"chi(Hilb^{n}) = {chi}, expected {expected}"

    def test_one_instanton(self):
        """One-instanton contribution = p(1) = 1."""
        assert self.hw.instanton_contribution(1) == Fraction(1)

    def test_two_instanton(self):
        """Two-instanton contribution = p(2) = 3."""
        assert self.hw.instanton_contribution(2) == Fraction(3)

    def test_crystal_melting_verification(self):
        """Two-method cross-validation passes."""
        v = self.hw.verify_crystal_melting()
        assert v["match"] is True

    def test_brst_index_alternating_signs(self):
        """BRST index has alternating signs: Ind(Q, n) = (-1)^n p(n)."""
        for n in range(10):
            expected = int(macmahon(n + 1)[n]) * ((-1) ** n)
            assert self.hw.brst_index(n) == expected

    def test_free_energy_positive(self):
        """Connected free energy F_n > 0 for n >= 1."""
        F = self.hw.free_energy()
        for n in range(1, 20):
            assert F[n] > 0, f"F_{n} = {F[n]} is not positive"


# ================================================================
# GAUGE THEORY (b): COSTELLO 7d CS
# ================================================================

class TestCostello7dCS:
    """Test Costello's 7d CS on CY3 x R."""

    def setup_method(self):
        self.cs = CostelloSevenDCS(25)

    def test_cy_condition(self):
        """sigma1 + sigma2 + sigma3 = 0."""
        assert self.cs.cy_condition_check()

    def test_boundary_character_is_macmahon(self):
        """Boundary E_1 algebra char = M(q)."""
        bc = self.cs.boundary_character()
        M = macmahon(25)
        assert all(bc[k] == M[k] for k in range(25))

    def test_bulk_character_is_macmahon(self):
        """Bulk W_{1+infty} character = M(q) at self-dual."""
        bc = self.cs.bulk_character()
        M = macmahon(25)
        assert all(bc[k] == M[k] for k in range(25))

    def test_phi1_vanishes(self):
        """phi_1 = 0 by the CY condition h1+h2+h3 = 0."""
        phi = self.cs.structure_constants(5)
        assert phi[1] == 0, f"phi_1 = {phi[1]}, should be 0 by CY condition"

    def test_phi2_vanishes(self):
        """phi_2 = 0 (even structure constants vanish for symmetric g(z))."""
        phi = self.cs.structure_constants(5)
        assert phi[2] == 0, f"phi_2 = {phi[2]}, should be 0"

    def test_phi0_is_one(self):
        """phi_0 = 1 (normalization)."""
        phi = self.cs.structure_constants(5)
        assert phi[0] == 1, f"phi_0 = {phi[0]}, should be 1"

    def test_phi3_formula(self):
        """phi_3 = -2*sigma_3 where sigma_3 = h1*h2*h3.

        For default h1=1, h2=1, h3=-2: sigma_3 = 1*1*(-2) = -2.
        phi_3 = -2*(-2)/3 * 3 = -2*p_3/3 where p_3 = h1^3+h2^3+h3^3.
        p_3 = 1 + 1 + (-8) = -6. alpha_3 = -2*(-6)/3 = 4.
        phi_3 = alpha_3 = 4.
        """
        phi = self.cs.structure_constants(5)
        h1, h2, h3 = Fraction(1), Fraction(1), Fraction(-2)
        p3 = h1**3 + h2**3 + h3**3
        alpha3 = Fraction(-2) * p3 / Fraction(3)
        assert phi[3] == alpha3, f"phi_3 = {phi[3]}, expected {alpha3}"

    def test_cy_condition_various_params(self):
        """CY condition holds for different sigma1, sigma2."""
        for s1, s2 in [(Fraction(1), Fraction(2)),
                        (Fraction(3, 2), Fraction(-1, 2)),
                        (Fraction(0), Fraction(0))]:
            cs = CostelloSevenDCS(10, sigma1=s1, sigma2=s2)
            assert cs.cy_condition_check()

    def test_koszul_dual_is_inverse(self):
        """Koszul dual character = 1/M(q)."""
        kd = self.cs.koszul_dual_character()
        M = macmahon(25)
        product = _poly_mul(kd, list(M), 25)
        assert product[0] == Fraction(1)
        for k in range(1, 25):
            assert product[k] == Fraction(0), f"M * M^{-1} != 1 at q^{k}"


# ================================================================
# GAUGE THEORY (c): KAPUSTIN-WITTEN
# ================================================================

class TestKapustinWitten:
    """Test the 4d N=4 theory with KW twist on S^2 x C^3."""

    def setup_method(self):
        self.kw = KapustinWittenGL1(20)

    def test_coulomb_character_is_geometric_series(self):
        """Coulomb branch char = 1/(1-q) = 1 + q + q^2 + ..."""
        ch = self.kw.coulomb_character()
        for k in range(20):
            assert ch[k] == Fraction(1), f"Coulomb[{k}] = {ch[k]}, expected 1"

    def test_higgs_character_is_exterior(self):
        """Higgs branch char = 1 + q (exterior algebra)."""
        ch = self.kw.higgs_character()
        assert ch[0] == Fraction(1)
        assert ch[1] == Fraction(1)
        for k in range(2, 20):
            assert ch[k] == Fraction(0), f"Higgs[{k}] = {ch[k]}, expected 0"

    def test_mirror_symmetry_check(self):
        """Coulomb * Higgs = (1+q)/(1-q) = 1 + 2q + 2q^2 + ..."""
        result = self.kw.mirror_symmetry_check()
        assert result["match"] is True
        assert result["koszul_dual_polynomial"] is True

    def test_koszul_product_explicit(self):
        """1/(1-q) * (1+q) = (1+q)/(1-q) = 1 + 2q + 2q^2 + ..."""
        c = self.kw.coulomb_character()
        h = self.kw.higgs_character()
        product = _poly_mul(c, h, 20)
        assert product[0] == Fraction(1)
        for k in range(1, 20):
            assert product[k] == Fraction(2), f"Product[{k}] = {product[k]}, expected 2"

    def test_coulomb_inverse_is_polynomial(self):
        """Coulomb^{-1} = 1-q (polynomial = Koszul property)."""
        c = self.kw.coulomb_character()
        c_inv = _poly_inv(c, 20)
        assert c_inv[0] == Fraction(1)
        assert c_inv[1] == Fraction(-1)
        for k in range(2, 20):
            assert c_inv[k] == Fraction(0), f"c^{-1}[{k}] = {c_inv[k]}, expected 0"

    def test_partition_function_is_coulomb(self):
        """Partition function = Coulomb branch character."""
        Z = self.kw.partition_function()
        c = self.kw.coulomb_character()
        assert all(Z[k] == c[k] for k in range(20))


# ================================================================
# GAUGE THEORY (d): 5d SEIBERG-WITTEN
# ================================================================

class TestFiveDSeibergWitten:
    """Test the 5d N=1 theory twisted on CY3."""

    def setup_method(self):
        self.sw = FiveDSeibergWitten(25)

    def test_dt_c3_behrend_signs(self):
        """Z^DT(q) = M(-q) = sum (-1)^n p(n) q^n."""
        dt = self.sw.dt_partition_c3()
        m = macmahon(25)
        for k in range(25):
            expected = m[k] * Fraction((-1) ** k)
            assert dt[k] == expected, f"DT[{k}] = {dt[k]}, expected {expected}"

    def test_dt_c3_first_values(self):
        """First few DT invariants: 1, -1, 3, -6, 13, -24, 48, ..."""
        dt = self.sw.dt_partition_c3()
        expected = [1, -1, 3, -6, 13, -24, 48, -86, 160, -282]
        for k, exp in enumerate(expected):
            assert int(dt[k]) == exp, f"DT[{k}] = {int(dt[k])}, expected {exp}"

    def test_gv_conifold_q1_is_inverse_macmahon(self):
        """GV conifold partition at Q=1: prod(1-q^n)^n = 1/M(q)."""
        gv = self.sw.gv_partition_conifold(Q=Fraction(1))
        m = macmahon(25)
        m_inv = _poly_inv(list(m), 25)
        for k in range(25):
            assert gv[k] == m_inv[k], f"GV[{k}] = {gv[k]}, expected {m_inv[k]}"

    def test_gv_integrality(self):
        """GV integrality check passes."""
        result = self.sw.gv_integrality_check()
        assert result["integrality"] is True

    def test_refined_dt_at_t1(self):
        """Refined DT at t=1 gives M(q) (unrefined limit).

        Z^{ref}(q, t=1) = prod_{n>=1} 1/(1-q^n)^n = M(q).
        At t=1 all factors 1/(1 - t^m q^n) become 1/(1-q^n),
        and there are n such factors for each n, giving prod 1/(1-q^n)^n.
        """
        ref = self.sw.refined_dt_c3(t=Fraction(1))
        M = macmahon(25)
        for k in range(min(20, len(ref))):
            assert ref[k] == M[k], f"Refined(t=1)[{k}] = {ref[k]}, expected {M[k]}"

    def test_refined_dt_positivity_at_t_neg1(self):
        """Refined DT at t=-1 has non-negative integer coefficients."""
        ref = self.sw.refined_dt_c3(t=Fraction(-1))
        for k in range(min(15, len(ref))):
            assert ref[k] >= 0, f"Refined(t=-1)[{k}] = {ref[k]} is negative"
            assert ref[k].denominator == 1, f"Refined(t=-1)[{k}] = {ref[k]} not integer"


# ================================================================
# BRST = BAR IDENTIFICATION
# ================================================================

class TestBRSTBarIdentification:
    """Test the BV/BRST = E_1 bar identification for CY3."""

    def setup_method(self):
        self.brst = BRSTBarIdentification(25)

    def test_brst_pf_is_macmahon(self):
        """BRST partition function = M(q)."""
        Z = self.brst.brst_partition_function()
        M = macmahon(25)
        assert all(Z[k] == M[k] for k in range(25))

    def test_bar_euler_char_alternating(self):
        """Bar Euler characteristic: chi(B_n) = (-1)^n p(n)."""
        chi = self.brst.bar_euler_characteristic()
        m = macmahon(25)
        for k in range(25):
            assert chi[k] == m[k] * Fraction((-1)**k)

    def test_one_instanton(self):
        """One-instanton test: Hilb^1(C^3) = point, contribution = 1."""
        result = self.brst.one_instanton_test()
        assert result["match"] is True
        assert result["hilb1_euler_char"] == 1
        assert result["z_coefficient_q1"] == 1

    def test_two_instanton(self):
        """Two-instanton test: Hilb^2(C^3) has chi = 3."""
        result = self.brst.two_instanton_test()
        assert result["match"] is True
        assert result["hilb2_euler_char"] == 3
        assert result["z_coefficient_q2"] == 3

    def test_dt_match(self):
        """DT = Behrend-weighted bar Euler characteristic."""
        result = self.brst.verify_dt_match()
        assert result["match"] is True

    def test_brst_cohomology_dimensions(self):
        """BRST cohomology dim at degree n = p(n)."""
        dims = self.brst.brst_cohomology_dimensions(10)
        known = {0: 1, 1: 1, 2: 3, 3: 6, 4: 13, 5: 24}
        for n, expected in known.items():
            assert dims[n] == expected, f"H^{n}(Q_BRST) dim = {dims[n]}, expected {expected}"

    def test_anomaly_coefficient(self):
        """Anomaly coefficient kappa = 1 for GL(1) on C^3."""
        result = self.brst.anomaly_coefficient()
        assert result["kappa_prediction"] == 1


# ================================================================
# COULOMB/HIGGS DUALITY (3d MIRROR SYMMETRY)
# ================================================================

class TestCoulombHiggsDuality:
    """Test Coulomb/Higgs duality = Koszul duality of E_1 algebras."""

    def test_rank1_koszul_duality(self):
        """Rank 1: Sym * Ext = 1/(1-q^2)."""
        ch = CoulombHiggsDuality(20, rank=1)
        result = ch.verify_koszul_duality()
        assert result["match"] is True

    def test_rank2_koszul_duality(self):
        """Rank 2: 1/(1-q)^2 * (1+q)^2 = 1/(1-q^2)^2."""
        ch = CoulombHiggsDuality(20, rank=2)
        result = ch.verify_koszul_duality()
        assert result["match"] is True

    def test_rank3_koszul_duality(self):
        """Rank 3: 1/(1-q)^3 * (1+q)^3 = 1/(1-q^2)^3."""
        ch = CoulombHiggsDuality(20, rank=3)
        result = ch.verify_koszul_duality()
        assert result["match"] is True

    def test_rank4_koszul_duality(self):
        """Rank 4: higher-rank check."""
        ch = CoulombHiggsDuality(20, rank=4)
        result = ch.verify_koszul_duality()
        assert result["match"] is True

    def test_coulomb_rank1_character(self):
        """Coulomb at rank 1 = 1/(1-q)."""
        ch = CoulombHiggsDuality(15, rank=1)
        c = ch.coulomb_character()
        for k in range(15):
            assert c[k] == Fraction(1)

    def test_coulomb_rank2_character(self):
        """Coulomb at rank 2 = 1/(1-q)^2 = sum (n+1) q^n."""
        ch = CoulombHiggsDuality(15, rank=2)
        c = ch.coulomb_character()
        for k in range(15):
            assert c[k] == Fraction(k + 1), f"c[{k}] = {c[k]}, expected {k+1}"

    def test_higgs_rank1_character(self):
        """Higgs at rank 1 = 1 + q."""
        ch = CoulombHiggsDuality(15, rank=1)
        h = ch.higgs_character()
        assert h[0] == Fraction(1)
        assert h[1] == Fraction(1)
        for k in range(2, 15):
            assert h[k] == Fraction(0)

    def test_higgs_rank2_character(self):
        """Higgs at rank 2 = (1+q)^2 = 1 + 2q + q^2."""
        ch = CoulombHiggsDuality(15, rank=2)
        h = ch.higgs_character()
        assert h[0] == Fraction(1)
        assert h[1] == Fraction(2)
        assert h[2] == Fraction(1)
        for k in range(3, 15):
            assert h[k] == Fraction(0)

    def test_higgs_rank3_character(self):
        """Higgs at rank 3 = (1+q)^3 = 1 + 3q + 3q^2 + q^3."""
        ch = CoulombHiggsDuality(15, rank=3)
        h = ch.higgs_character()
        assert h[0] == Fraction(1)
        assert h[1] == Fraction(3)
        assert h[2] == Fraction(3)
        assert h[3] == Fraction(1)
        for k in range(4, 15):
            assert h[k] == Fraction(0)

    def test_koszul_complex_rank1(self):
        """Koszul complex at rank 1: (1+q)/(1-q) = 1 + 2q + 2q^2 + ..."""
        ch = CoulombHiggsDuality(15, rank=1)
        kc = ch.koszul_complex_character()
        assert kc[0] == Fraction(1)
        for k in range(1, 15):
            assert kc[k] == Fraction(2), f"KC[{k}] = {kc[k]}, expected 2"

    def test_koszul_complex_rank2(self):
        """Koszul complex at rank 2: ((1+q)/(1-q))^2 = 1 + 4q + 8q^2 + ..."""
        ch = CoulombHiggsDuality(15, rank=2)
        kc = ch.koszul_complex_character()
        # ((1+q)/(1-q))^2 = (1+2q+2q^2+...)^2
        # k=0: 1, k=1: 4, k=2: 8, k=3: 12, k=4: 16, ...
        # General: 4k for k >= 1, 1 for k=0
        assert kc[0] == Fraction(1)
        for k in range(1, 15):
            assert kc[k] == Fraction(4 * k), f"KC[{k}] = {kc[k]}, expected {4*k}"

    def test_koszul_polynomial_property(self):
        """Coulomb^{-1} = (1-q)^r is a polynomial of degree r."""
        for r in range(1, 5):
            ch = CoulombHiggsDuality(15, rank=r)
            result = ch.verify_koszul_duality()
            assert result["koszul_polynomial"] is True, \
                f"Coulomb^{{-1}} not polynomial at rank {r}"


# ================================================================
# CONIFOLD GAUGE THEORY
# ================================================================

class TestConifoldGaugeTheory:
    """Test gauge theory on the resolved conifold."""

    def setup_method(self):
        self.con = ConifoldGaugeTheory(25)

    def test_reduced_dt_is_inverse_macmahon(self):
        """prod (1-q^n)^n = 1/M(q)."""
        result = self.con.verify_reduced_dt_is_inverse_macmahon()
        assert result["match"] is True

    def test_reduced_dt_first_values(self):
        """First coefficients of prod (1-q^n)^n."""
        red = self.con.reduced_dt()
        # prod (1-q^n)^n: first few are 1, -1, -2, 2, 3, 2, -5, ...
        # This is 1/M(q). Check: M(q) * (1/M(q)) = 1
        M = macmahon(25)
        product = _poly_mul(red, list(M), 25)
        assert product[0] == Fraction(1)
        for k in range(1, 25):
            assert product[k] == Fraction(0)

    def test_bps_spectrum_chamber_I(self):
        """Chamber I has 2 BPS states."""
        bps = self.con.bps_spectrum()
        assert bps["chamber_I"]["num_states"] == 2

    def test_bps_spectrum_chamber_II(self):
        """Chamber II has 3 BPS states."""
        bps = self.con.bps_spectrum()
        assert bps["chamber_II"]["num_states"] == 3

    def test_wall_crossing_trivial_at_Q1(self):
        """At Q=1, the wall-crossing product is trivial."""
        wc = self.con.wall_crossing_product()
        assert wc[0] == Fraction(1)
        for k in range(1, 25):
            assert wc[k] == Fraction(0), f"WC[{k}] = {wc[k]}, expected 0"


# ================================================================
# INSTANTON CORRECTIONS
# ================================================================

class TestInstantonEngine:
    """Test instanton corrections to the E_1 shadow."""

    def setup_method(self):
        self.inst = InstantonEngine(25)

    def test_free_energy_two_methods(self):
        """Cross-validate free energy: sigma_2/k vs log M(q)."""
        result = self.inst.verify_free_energy_two_methods()
        assert result["match"] is True

    def test_F1_equals_one(self):
        """F_1 = 1 (one-instanton = single point)."""
        assert self.inst.one_instanton_amplitude() == Fraction(1)

    def test_F2_equals_five_halves(self):
        """F_2 = sigma_2(2)/2 = (1+4)/2 = 5/2."""
        assert self.inst.two_instanton_amplitude() == Fraction(5, 2)

    def test_F3_value(self):
        """F_3 = sigma_2(3)/3 = (1+9)/3 = 10/3."""
        F3 = self.inst.n_instanton_amplitude(3)
        assert F3 == Fraction(10, 3)

    def test_F4_value(self):
        """F_4 = sigma_2(4)/4 = (1+4+16)/4 = 21/4."""
        F4 = self.inst.n_instanton_amplitude(4)
        assert F4 == Fraction(21, 4)

    def test_F6_value(self):
        """F_6 = sigma_2(6)/6 = (1+4+9+36)/6 = 50/6 = 25/3."""
        F6 = self.inst.n_instanton_amplitude(6)
        assert F6 == Fraction(50, 6)

    def test_sigma2_values(self):
        """sigma_2(n) = sum d^2 for d|n."""
        assert self.inst.sigma_2(1) == 1
        assert self.inst.sigma_2(2) == 5   # 1 + 4
        assert self.inst.sigma_2(3) == 10  # 1 + 9
        assert self.inst.sigma_2(4) == 21  # 1 + 4 + 16
        assert self.inst.sigma_2(5) == 26  # 1 + 25
        assert self.inst.sigma_2(6) == 50  # 1 + 4 + 9 + 36

    def test_instanton_sum_reproduces_macmahon(self):
        """exp(sum F_n q^n) = M(q)."""
        result = self.inst.verify_instanton_sum_reproduces_macmahon()
        assert result["match"] is True

    def test_free_energy_positivity(self):
        """F_n > 0 for all n >= 1."""
        F = self.inst.free_energy()
        for n in range(1, 25):
            assert F[n] > 0, f"F_{n} = {F[n]} is not positive"

    def test_sigma2_multiplicative_at_coprime(self):
        """sigma_2 is multiplicative: sigma_2(mn) = sigma_2(m)*sigma_2(n) for gcd(m,n)=1."""
        for m in range(1, 10):
            for n in range(1, 10):
                if math.gcd(m, n) == 1:
                    assert (self.inst.sigma_2(m * n) ==
                            self.inst.sigma_2(m) * self.inst.sigma_2(n)), \
                        f"sigma_2({m}*{n}) != sigma_2({m})*sigma_2({n})"


# Need math import for gcd
import math


# ================================================================
# EULER PRODUCT
# ================================================================

class TestEulerProduct:
    """Test the Euler product prod(1-q^n)^power."""

    def test_euler_product_power1_is_euler_function(self):
        """prod (1-q^n) = Euler function (OEIS A010815)."""
        N = 15
        ep = euler_product(N, power=1)
        # Known: 1, -1, -1, 0, 1, 0, 1, 0, -1, 0, 0, 0, -1, ...
        # Wait, this is prod(1-q^n) = sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}
        # First terms at k=0,1,-1,2,-2: q^0=1, q^1=-1, q^2=-1, ...
        # Euler's pentagonal theorem: pentagonal numbers 0,1,2,5,7,12,15,...
        assert ep[0] == Fraction(1)
        assert ep[1] == Fraction(-1)
        assert ep[2] == Fraction(-1)
        assert ep[3] == Fraction(0)
        assert ep[4] == Fraction(0)
        assert ep[5] == Fraction(1)

    def test_euler_product_power_neg1_is_partition_gen(self):
        """prod 1/(1-q^n) = partition generating function."""
        N = 15
        ep = euler_product(N, power=-1)
        # p(n) = ordinary partitions: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
        known_partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for k, expected in enumerate(known_partitions):
            assert int(ep[k]) == expected, f"p({k}) = {int(ep[k])}, expected {expected}"


# ================================================================
# COMPREHENSIVE DICTIONARY TESTS
# ================================================================

class TestGaugeChiralDictionary:
    """Test the full gauge theory / chiral algebra dictionary."""

    def test_verify_all_theories(self):
        """All four theories pass verification."""
        results = GaugeChiralDictionary.verify_all_theories(20)

        # Haydys-Witten
        assert results["haydys_witten"]["crystal_melting"]["match"] is True
        assert results["haydys_witten"]["one_instanton"] is True
        assert results["haydys_witten"]["bps_first_10"] == [1, 1, 3, 6, 13, 24, 48, 86, 160, 282]

        # Costello
        assert results["costello_7d_cs"]["cy_condition"] is True

        # KW
        assert results["kapustin_witten"]["mirror_symmetry"]["match"] is True

        # BRST
        assert results["brst_bar_id"]["one_instanton"]["match"] is True
        assert results["brst_bar_id"]["two_instanton"]["match"] is True
        assert results["brst_bar_id"]["dt_match"]["match"] is True

        # Coulomb-Higgs
        assert results["coulomb_higgs"]["rank1_duality"]["match"] is True


# ================================================================
# CROSS-FAMILY CONSISTENCY
# ================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks across the four gauge theories."""

    def test_all_theories_agree_on_c3_pf(self):
        """All theories on C^3 agree: Z = M(q) (modulo signs)."""
        N = 20
        hw_Z = HaydysWittenGL1(N).partition_function()
        cs_Z = CostelloSevenDCS(N).boundary_character()
        brst_Z = BRSTBarIdentification(N).brst_partition_function()
        M = macmahon(N)

        for k in range(N):
            assert hw_Z[k] == M[k], f"HW != M at {k}"
            assert cs_Z[k] == M[k], f"CS != M at {k}"
            assert brst_Z[k] == M[k], f"BRST != M at {k}"

    def test_dt_vs_e1_behrend_sign(self):
        """Z^DT(q) = Z^{E_1}(-q) (Behrend function sign flip)."""
        N = 20
        sw = FiveDSeibergWitten(N)
        dt = sw.dt_partition_c3()
        M = macmahon(N)
        for k in range(N):
            assert dt[k] == M[k] * Fraction((-1)**k)

    def test_conifold_reduces_to_c3(self):
        """At Q=1, conifold reduced DT * M(q) = 1.

        The conifold at Q=1 gives 1/M(q), so
        Z_full = M(q) * 1/M(q) = 1 (trivial at Q=1).
        """
        N = 20
        con = ConifoldGaugeTheory(N)
        red = con.reduced_dt()
        M = macmahon(N)
        product = _poly_mul(red, list(M), N)
        assert product[0] == Fraction(1)
        for k in range(1, N):
            assert product[k] == Fraction(0)

    def test_instanton_exp_equals_character(self):
        """exp(instanton free energy) = E_1 character = M(q)."""
        N = 20
        inst = InstantonEngine(N)
        F = inst.free_energy()
        Z_inst = _poly_exp(F, N)
        M = macmahon(N)
        for k in range(N):
            assert Z_inst[k] == M[k]

    def test_koszul_duality_is_mirror_symmetry(self):
        """For all ranks 1-5: Coulomb * Higgs = 1/(1-q^2)^r."""
        for r in range(1, 6):
            ch = CoulombHiggsDuality(15, rank=r)
            result = ch.verify_koszul_duality()
            assert result["match"] is True, f"Koszul duality fails at rank {r}"


# ================================================================
# LIMITING CASES
# ================================================================

class TestLimitingCases:
    """Verify behavior at limiting parameter values."""

    def test_macmahon_limit_q0(self):
        """M(0) = 1 (empty partition)."""
        M = macmahon(5)
        assert M[0] == Fraction(1)

    def test_free_energy_limit_q0(self):
        """F(0) = 0 (no connected contribution at zero coupling)."""
        inst = InstantonEngine(5)
        F = inst.free_energy()
        assert F[0] == Fraction(0)

    def test_rank0_coulomb_is_trivial(self):
        """Rank 0 Coulomb branch = constant 1 (no fields)."""
        ch = CoulombHiggsDuality(10, rank=0)
        c = ch.coulomb_character()
        assert c[0] == Fraction(1)
        for k in range(1, 10):
            assert c[k] == Fraction(0)

    def test_rank0_higgs_is_trivial(self):
        """Rank 0 Higgs branch = constant 1 (no fields)."""
        ch = CoulombHiggsDuality(10, rank=0)
        h = ch.higgs_character()
        assert h[0] == Fraction(1)
        for k in range(1, 10):
            assert h[k] == Fraction(0)

    def test_costello_symmetric_params(self):
        """At h1 = h2 = 1, h3 = -2: phi_1 = 0 (CY condition)."""
        cs = CostelloSevenDCS(10, sigma1=Fraction(1), sigma2=Fraction(1))
        phi = cs.structure_constants(3)
        assert phi[1] == Fraction(0)

    def test_costello_all_zero_params(self):
        """At h1 = h2 = h3 = 0: all phi_j = 0 for j >= 1."""
        cs = CostelloSevenDCS(10, sigma1=Fraction(0), sigma2=Fraction(0))
        phi = cs.structure_constants(8)
        assert phi[0] == Fraction(1)
        for j in range(1, 8):
            assert phi[j] == Fraction(0), f"phi_{j} = {phi[j]} at zero params"


# ================================================================
# COMPREHENSIVE RUN
# ================================================================

class TestComprehensiveRun:
    """Test the full verification suite."""

    def test_run_full_verification(self):
        """Full verification runs without error and all checks pass."""
        results = run_full_verification(20)

        assert results["haydys_witten_crystal"]["match"] is True
        assert results["costello_cy_check"] is True
        assert results["costello_phi_vanishing"]["phi_1"] is True
        assert results["costello_phi_vanishing"]["phi_2"] is True
        assert results["kw_mirror"]["match"] is True
        assert results["sw_gv"]["integrality"] is True
        assert results["brst_one_inst"]["match"] is True
        assert results["brst_two_inst"]["match"] is True
        assert results["brst_dt_match"]["match"] is True
        assert results["conifold_reduced_dt"]["match"] is True
        assert results["instanton_free_energy"]["match"] is True
        assert results["instanton_sum_macmahon"]["match"] is True

        for r in [1, 2, 3]:
            assert results[f"coulomb_higgs_rank{r}"]["match"] is True
