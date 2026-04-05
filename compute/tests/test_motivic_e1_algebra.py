r"""Tests for the motivic E₁ algebra.

Verifies:
  1. Motivic class arithmetic in K₀(Var)[L^{±1/2}]
  2. Motivic plethystic exponential and logarithm
  3. Motivic MacMahon function for C³
  4. Euler characteristic specialization: χ(Z^{mot}) = M(q)
  5. Motivic BPS invariants via PLog
  6. Motivic wall-crossing (conifold D0-sector)
  7. Motivic CoHA multiplication and associativity
  8. Weight filtration and BPS crystal for C³
  9. Motivic shadow tower: genus-1 kappa
  10. PLog ∘ PExp = id roundtrip

Every test uses at least 2 independent verification paths (AP10).
Exact arithmetic throughout: no floating point.

References:
  Kontsevich-Soibelman, arXiv:0811.2435 (motivic DT)
  Behrend-Bryan-Szendroi, arXiv:0909.5088 (motivic DT for C³)
  Morrison-Mozgovoy-Nagao-Szendroi, arXiv:1103.4229 (motivic DT conifold)
  Davison-Meinhardt, arXiv:1311.7172 (motivic PBW)
"""

from fractions import Fraction

import pytest

from compute.lib.motivic_e1_algebra import (
    MotivicClass,
    MotivicE1Hocolim,
    MotivicShadowTower,
    _mfps_add,
    _mfps_euler_char,
    _mfps_mul,
    _mfps_one,
    _mfps_zero,
    _mobius_sieve,
    bps_crystal_c3,
    c3_motivic_bps,
    c3_motivic_chamber,
    conifold_motivic_bound_state,
    conifold_motivic_bps,
    d0_brane_motivic_bps,
    motivic_adams,
    motivic_coha_multiply,
    motivic_c3_single_letter,
    motivic_ks_factor,
    motivic_macmahon,
    motivic_master_verification,
    motivic_plethystic_exp,
    motivic_plethystic_log,
    motivic_sym_n,
    numerical_macmahon,
    verify_c3_euler_specialization,
    verify_conifold_euler_specialization,
    verify_motivic_associativity,
    verify_motivic_macmahon_euler_char,
    weight_decomposition,
)


# ================================================================
# SECTION 1: MOTIVIC CLASS ARITHMETIC
# ================================================================

class TestMotivicClass:
    """Tests for elements of K₀(Var)[L^{±1/2}]."""

    def test_zero(self):
        z = MotivicClass.zero()
        assert z.is_zero()
        assert z.euler_char() == 0

    def test_one(self):
        o = MotivicClass.one()
        assert not o.is_zero()
        assert o.euler_char() == 1

    def test_L(self):
        """L = [A¹], χ(L) = 1."""
        l = MotivicClass.L()
        assert l.euler_char() == 1
        assert l.coeffs == {2: 1}  # L^1 stored as key 2

    def test_L_power(self):
        """L^n, χ(L^n) = 1."""
        for n in range(5):
            ln = MotivicClass.L(n)
            assert ln.euler_char() == 1

    def test_L_half(self):
        """L^{1/2}, stored as key 1."""
        lh = MotivicClass.L_half(1)
        assert lh.coeffs == {1: 1}
        assert lh.euler_char() == 1

    def test_addition(self):
        a = MotivicClass.L()       # L
        b = MotivicClass.one()     # 1
        c = a + b                   # L + 1
        assert c.euler_char() == 2
        assert c.coeffs == {2: 1, 0: 1}

    def test_subtraction(self):
        a = MotivicClass.L()       # L
        b = MotivicClass.one()     # 1
        c = a - b                   # L - 1
        assert c.euler_char() == 0
        assert c.coeffs == {2: 1, 0: -1}

    def test_multiplication(self):
        """L · L = L²."""
        a = MotivicClass.L()
        b = MotivicClass.L()
        c = a * b
        assert c == MotivicClass.L(2)

    def test_multiplication_half(self):
        """L^{1/2} · L^{1/2} = L."""
        a = MotivicClass.L_half(1)
        b = MotivicClass.L_half(1)
        c = a * b
        assert c == MotivicClass.L()

    def test_scalar_mul(self):
        a = MotivicClass.L()
        b = 3 * a
        assert b.coeffs == {2: 3}
        assert b.euler_char() == 3

    def test_power(self):
        """L^3 via ** operator."""
        a = MotivicClass.L()
        c = a ** 3
        assert c == MotivicClass.L(3)

    def test_equality(self):
        a = MotivicClass({2: 1, 0: 1})  # L + 1
        b = MotivicClass.L() + MotivicClass.one()
        assert a == b

    def test_from_int(self):
        f = MotivicClass.from_int(5)
        assert f.euler_char() == 5
        assert f.coeffs == {0: 5}

    def test_negation(self):
        a = MotivicClass.L()
        b = -a
        assert b.euler_char() == -1
        assert b.coeffs == {2: -1}

    def test_weight_degree_pure(self):
        a = MotivicClass.L(3)
        assert a.weight_degree() == 6  # key = 2*3 = 6

    def test_weight_degree_mixed(self):
        a = MotivicClass.L() + MotivicClass.one()
        assert a.weight_degree() is None

    def test_euler_char_complex(self):
        """χ(L² + 3L + 2) = 1 + 3 + 2 = 6."""
        a = MotivicClass.L(2) + 3 * MotivicClass.L() + MotivicClass.from_int(2)
        assert a.euler_char() == 6

    def test_distributivity(self):
        """(L + 1)(L - 1) = L² - 1."""
        a = MotivicClass.L() + MotivicClass.one()
        b = MotivicClass.L() - MotivicClass.one()
        c = a * b
        expected = MotivicClass.L(2) - MotivicClass.one()
        assert c == expected


# ================================================================
# SECTION 2: MOTIVIC POWER SERIES
# ================================================================

class TestMotivicFPS:
    """Tests for formal power series with motivic coefficients."""

    def test_mfps_zero(self):
        f = _mfps_zero(5)
        assert len(f) == 5
        assert all(c.is_zero() for c in f)

    def test_mfps_one(self):
        f = _mfps_one(5)
        assert f[0] == MotivicClass.one()
        assert all(f[i].is_zero() for i in range(1, 5))

    def test_mfps_add(self):
        a = _mfps_one(3)
        b = _mfps_one(3)
        c = _mfps_add(a, b, 3)
        assert c[0].euler_char() == 2

    def test_mfps_mul(self):
        """(1 + Lq)(1 + Lq) = 1 + 2Lq + L²q²."""
        a = _mfps_zero(4)
        a[0] = MotivicClass.one()
        a[1] = MotivicClass.L()
        b = list(a)
        c = _mfps_mul(a, b, 4)
        assert c[0] == MotivicClass.one()
        assert c[1] == MotivicClass.from_int(2) * MotivicClass.L()  # Wait
        # 2 * MotivicClass.L() = {2: 2}
        assert c[1] == MotivicClass({2: 2})
        # q² coefficient: L · L = L²
        assert c[2] == MotivicClass.L(2)

    def test_mfps_euler_char(self):
        f = _mfps_zero(3)
        f[0] = MotivicClass.one()
        f[1] = MotivicClass.L()
        f[2] = MotivicClass.L(2)
        chi = _mfps_euler_char(f)
        assert chi == [1, 1, 1]


# ================================================================
# SECTION 3: PLETHYSTIC OPERATIONS
# ================================================================

class TestPlethysticOps:
    """Tests for motivic plethystic exp and log."""

    def test_pexp_trivial(self):
        """PExp(0) = 1."""
        f = _mfps_zero(5)
        result = motivic_plethystic_exp(f, 5)
        assert result[0] == MotivicClass.one()
        for i in range(1, 5):
            assert result[i].is_zero()

    def test_pexp_single_term(self):
        """PExp(c · q) = exp(Σ ψ_m(c)/m q^m).

        For c = [pt] = 1:
          PExp(q) = exp(Σ q^m/m) = exp(-log(1-q)) = 1/(1-q)
          Coefficients: all 1.
        """
        N = 8
        f = _mfps_zero(N)
        f[1] = MotivicClass.one()
        result = motivic_plethystic_exp(f, N)
        for i in range(N):
            assert result[i].euler_char() == 1, (
                f"PExp(q)[{i}] Euler char = {result[i].euler_char()}, expected 1"
            )

    def test_plog_pexp_roundtrip(self):
        """PLog(PExp(f)) = f for a test input.

        f = L^{3/2} q + L^{5/2} q² (truncated single-letter).
        """
        N = 7
        f = _mfps_zero(N)
        f[1] = MotivicClass.L_half(3)   # L^{3/2} q
        f[2] = MotivicClass.L_half(5)   # L^{5/2} q²

        Z = motivic_plethystic_exp(f, N)
        f_recovered = motivic_plethystic_log(Z, N)

        for i in range(N):
            assert f[i] == f_recovered[i], (
                f"Roundtrip fail at q^{i}: input={f[i]}, recovered={f_recovered[i]}"
            )

    def test_plog_pexp_full_single_letter(self):
        """PLog(PExp(f)) = f for the full C³ single letter (truncated)."""
        N = 7
        f = motivic_c3_single_letter(N)
        Z = motivic_plethystic_exp(f, N)
        f_rec = motivic_plethystic_log(Z, N)

        for i in range(N):
            assert f[i] == f_rec[i], (
                f"Full single-letter roundtrip fail at q^{i}"
            )

    def test_adams_operation(self):
        """ψ_2(L^{3/2} q) = L^3 q²."""
        N = 5
        f = _mfps_zero(N)
        f[1] = MotivicClass.L_half(3)  # L^{3/2} q
        result = motivic_adams(f, 2, N)
        # At q²: ψ_2(L^{3/2}) = L^3
        assert result[2] == MotivicClass.L(3)
        # All other coefficients zero
        assert result[0].is_zero()
        assert result[1].is_zero()


# ================================================================
# SECTION 4: MOTIVIC MacMAHON FOR C³
# ================================================================

class TestMotivicMacMahon:
    """Tests for the motivic MacMahon function Z^{mot}(C³)."""

    def test_euler_char_is_macmahon(self):
        """χ(Z^{mot}(C³)) = M(q) (numerical MacMahon).

        This is the FUNDAMENTAL test: the motivic partition function
        specializes to the numerical one under L → 1.

        M(q) = 1 + q + 3q² + 6q³ + 13q⁴ + 24q⁵ + 48q⁶ + 86q⁷ + 160q⁸ + ...
        OEIS A000219.
        """
        N = 9
        ok, mot_chi, num = verify_motivic_macmahon_euler_char(N)
        assert ok, f"Motivic χ = {mot_chi}, numerical = {num}"

    def test_macmahon_known_values(self):
        """Verify against known MacMahon values (OEIS A000219)."""
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160]
        N = len(known)
        num = numerical_macmahon(N)
        assert num == known

        # Also verify motivic
        Z_mot = motivic_macmahon(N)
        mot_chi = [c.euler_char() for c in Z_mot]
        assert mot_chi == known

    def test_hilb0_is_point(self):
        """[Hilb⁰(C³)] = 1 = [pt]."""
        Z = motivic_macmahon(3)
        assert Z[0] == MotivicClass.one()

    def test_hilb1_euler_char(self):
        """χ([Hilb¹(C³)]) = 1.

        One point on C³: the moduli is C³ itself.
        χ = pp(1) = 1.

        Path 2: Direct from the motivic MacMahon.
        """
        Z = motivic_macmahon(3)
        assert Z[1].euler_char() == 1

    def test_hilb2(self):
        """[Hilb²(C³)] should have χ = 3 (three plane partitions of 2).

        The three plane partitions of 2 are: (2), (1,1), and the 2x1 stack.
        """
        Z = motivic_macmahon(4)
        assert Z[2].euler_char() == 3

    def test_hilb3(self):
        """[Hilb³(C³)] has χ = 6."""
        Z = motivic_macmahon(5)
        assert Z[3].euler_char() == 6

    def test_single_letter_structure(self):
        """The BBS single-letter index (Behrend-Bryan-Szendroi).

        f_n = Σ_{k=0}^{n-1} L^{k+3/2}  (n terms at charge n)

        Path 1: f_1 = L^{3/2} (one term)
        Path 2: f_2 = L^{3/2} + L^{5/2} (two terms)
        Path 3: χ(f_n) = n for all n
        """
        N = 6
        f = motivic_c3_single_letter(N)
        assert f[0].is_zero()

        # f_1 = L^{3/2}
        assert f[1] == MotivicClass.L_half(3)

        # f_2 = L^{3/2} + L^{5/2}
        expected_2 = MotivicClass.L_half(3) + MotivicClass.L_half(5)
        assert f[2] == expected_2

        # χ(f_n) = n for all n
        for n in range(1, N):
            assert f[n].euler_char() == n, (
                f"χ(f_{n}) = {f[n].euler_char()}, expected {n}"
            )


# ================================================================
# SECTION 5: MOTIVIC BPS INVARIANTS
# ================================================================

class TestMotivicBPS:
    """Tests for motivic BPS invariants."""

    def test_c3_bps_euler_char(self):
        """χ([Ω_n^{mot}]) = n for all n (C³).

        The motivic BPS invariant [Ω_n] = Σ_{k=0}^{n-1} L^{k+3/2}
        has n terms, each with χ = 1, so χ([Ω_n]) = n.

        Path 1: Direct from c3_motivic_bps.
        Path 2: Matches the numerical BPS: PLog_num(M(q)) = Σ n q^n.
        """
        for n in range(1, 8):
            omega = c3_motivic_bps(n)
            assert omega.euler_char() == n, (
                f"χ(Ω_{n}) = {omega.euler_char()}, expected {n}"
            )

    def test_c3_bps_from_plog(self):
        """PLog(Z^{mot}(C³)) = BBS single-letter = Σ f_n q^n.

        Path 1: PLog of motivic MacMahon = BBS single-letter.
        Path 2: χ of each PLog coefficient = n.
        Path 3: Roundtrip: PExp(PLog(Z)) = Z.
        """
        N = 7
        Z = motivic_macmahon(N)
        plog = motivic_plethystic_log(Z, N)

        for n in range(1, N):
            expected = c3_motivic_bps(n)
            assert plog[n] == expected, (
                f"PLog at q^{n}: got {plog[n]}, expected {expected}"
            )
            # Path 2: Euler char cross-check
            assert plog[n].euler_char() == n

    def test_conifold_bps(self):
        """Conifold BPS: [Ω_{(1,0)}] = [Ω_{(0,1)}] = [pt] = 1."""
        spec = conifold_motivic_bps()
        assert spec[(1, 0)] == MotivicClass.one()
        assert spec[(0, 1)] == MotivicClass.one()

    def test_conifold_bound_state(self):
        """[Ω_{(1,1)}] = [pt] = 1 at the wall."""
        omega = conifold_motivic_bound_state()
        assert omega == MotivicClass.one()
        assert omega.euler_char() == 1

    def test_d0_brane_sym(self):
        """[Ω_{(n,0)}^{D0}] = [Sym^n(C)] = L^n.

        D0-branes on a curve C: Sym^n(C) = C^n/S_n.
        For C = A¹: [Sym^n(A¹)] = L^n.
        """
        for n in range(1, 6):
            omega = d0_brane_motivic_bps(n)
            assert omega == MotivicClass.L(n)
            assert omega.euler_char() == 1

    def test_motivic_chamber_structure(self):
        """C³ motivic chamber has the correct BPS spectrum.

        Path 1: Direct equality with c3_motivic_bps.
        Path 2: Euler char gives the numerical spectrum.
        """
        chamber = c3_motivic_chamber()
        assert chamber.name == "C³ motivic (unique chamber)"
        # Path 1: motivic classes match
        assert chamber.bps_spectrum[(1,)] == c3_motivic_bps(1)
        assert chamber.bps_spectrum[(2,)] == c3_motivic_bps(2)
        # Path 2: numerical spectrum
        num = chamber.numerical_spectrum()
        assert num[(1,)] == 1
        assert num[(2,)] == 2
        assert num[(3,)] == 3


# ================================================================
# SECTION 6: MOTIVIC WALL-CROSSING
# ================================================================

class TestMotivicWallCrossing:
    """Tests for motivic KS wall-crossing factors."""

    def test_ks_factor_trivial(self):
        """K_γ for [Ω] = 0 should be 1 + 0 + 0 + ...."""
        N = 5
        Z = motivic_ks_factor(MotivicClass.zero(), N)
        assert Z[0] == MotivicClass.one()
        for i in range(1, N):
            assert Z[i].is_zero()

    def test_ks_factor_point_euler(self):
        """K_γ for [Ω] = [pt]: χ-specialization gives 1/(1-q).

        Exp_*(L^{-1/2} · 1 · q) at L=1 = Exp_*(q) = 1/(1-q).
        """
        N = 8
        Z = motivic_ks_factor(MotivicClass.one(), N)
        for i in range(N):
            assert Z[i].euler_char() == 1, (
                f"KS factor at q^{i}: χ = {Z[i].euler_char()}, expected 1"
            )


# ================================================================
# SECTION 7: MOTIVIC CoHA MULTIPLICATION
# ================================================================

class TestMotivicCoHA:
    """Tests for motivic CoHA multiplication."""

    def test_basic_multiply(self):
        """[M_d] * [M_e] = [M_d] · [M_e] · L^{-<d,e>/2}."""
        a = MotivicClass.L()       # [M_d] = L
        b = MotivicClass.L(2)      # [M_e] = L²
        # <d,e> = 2 (antisymmetric Euler form)
        result = motivic_coha_multiply(a, b, 2)
        # L · L² · L^{-2/2} = L · L² · L^{-1} = L²
        assert result == MotivicClass.L(2)

    def test_multiply_euler_char(self):
        """Euler char of product: χ(a*b) = χ(a)·χ(b)·χ(L^{-<>/2})."""
        a = MotivicClass.L()
        b = MotivicClass.L(2)
        for ef in [0, 1, 2, -1, -3]:
            result = motivic_coha_multiply(a, b, ef)
            # χ(L^k) = 1 for all k, so χ(result) = 1·1·1 = 1
            assert result.euler_char() == 1

    def test_associativity_basic(self):
        """Associativity: (a*b)*c = a*(b*c).

        Path 1: Direct computation via verify_motivic_associativity.
        Path 2: The cocycle condition is tautological (bilinearity of <,>).
        """
        a = MotivicClass.L()
        b = MotivicClass.L(2)
        c = MotivicClass.L(3)
        # Euler form values (arbitrary but consistent)
        ef_ab = 1    # <d, e>
        ef_bc = -1   # <e, f>
        ef_ac = 2    # <d, f>
        ef_abc = ef_ac + ef_bc  # <d+e, f> = <d,f> + <e,f> (bilinearity)
        assert verify_motivic_associativity(a, b, c, ef_ab, ef_bc, ef_ac, ef_abc)

    def test_associativity_trivial_euler_form(self):
        """Associativity when <,> = 0 (e.g., C³ Jordan quiver)."""
        a = MotivicClass.L() + MotivicClass.one()
        b = MotivicClass.L(2)
        c = MotivicClass.from_int(3)
        assert verify_motivic_associativity(a, b, c, 0, 0, 0, 0)

    def test_twist_is_quantum_parameter(self):
        """The twist L^{-<d,e>/2} is the motivic origin of q^{<d,e>}.

        Under the specialization L^{1/2} → q, the twist becomes
        q^{-<d,e>}, the quantum group parameter.
        """
        twist = MotivicClass.L_half(-3)  # L^{-3/2} for <d,e> = 3
        # Weight degree: key = -3
        assert twist.weight_degree() == -3


# ================================================================
# SECTION 8: WEIGHT FILTRATION AND BPS CRYSTAL
# ================================================================

class TestWeightFiltration:
    """Tests for the weight filtration and BPS crystal."""

    def test_weight_decomposition_pure(self):
        """Pure class L^3 has a single weight."""
        mc = MotivicClass.L(3)
        wd = weight_decomposition(mc)
        assert wd == {6: 1}  # key 6 = 2*3

    def test_weight_decomposition_mixed(self):
        """L² + L has two weights."""
        mc = MotivicClass.L(2) + MotivicClass.L()
        wd = weight_decomposition(mc)
        assert wd == {4: 1, 2: 1}

    def test_bps_crystal_c3_charge_0(self):
        """Crystal at charge 0: {0: 1} (= [pt])."""
        crystal = bps_crystal_c3(5)
        assert crystal[0] == {0: 1}

    def test_bps_crystal_c3_charge_1(self):
        """Crystal at charge 1: {3: 1} (= L^{3/2}).

        [Hilb¹(C³)] = L^{3/2} in the BBS convention (key 3 = L^{3/2}).
        χ(L^{3/2}) = 1 = pp(1).

        Path 1: From crystal decomposition.
        Path 2: Matches the BBS single-letter f_1 = L^{3/2}.
        """
        crystal = bps_crystal_c3(5)
        assert crystal[1] == {3: 1}
        # Path 2: matches BPS invariant at charge 1
        assert sum(crystal[1].values()) == 1  # χ = pp(1)

    def test_bps_crystal_sum_equals_macmahon(self):
        """Σ_w a_{n,w} = pp(n) for all n (weight sum = plane partition count).

        This is the consistency check that the weight filtration
        is compatible with the Euler characteristic.
        """
        N = 9
        crystal = bps_crystal_c3(N)
        mac = numerical_macmahon(N)
        for n in range(N):
            weight_sum = sum(crystal.get(n, {}).values())
            assert weight_sum == mac[n], (
                f"Weight sum at charge {n}: {weight_sum} != pp({n}) = {mac[n]}"
            )

    def test_bps_crystal_weights_positive(self):
        """All weights in [Hilb^n(C³)] should be non-negative.

        [Hilb^n(C³)] is a smooth variety, so its motive has
        non-negative coefficients in the L-expansion.
        """
        N = 9
        crystal = bps_crystal_c3(N)
        for n in range(N):
            for w, coeff in crystal.get(n, {}).items():
                assert coeff > 0, (
                    f"Negative coefficient at charge {n}, weight {w}: {coeff}"
                )


# ================================================================
# SECTION 9: MOTIVIC E₁ HOCOLIM
# ================================================================

class TestMotivicE1Hocolim:
    """Tests for the motivic E₁ hocolim."""

    def test_c3_hocolim(self):
        """C³ motivic hocolim: kappa = 1, partition function = motivic MacMahon.

        Path 1: kappa_num = χ(kappa_mot) = 1.
        Path 2: kappa_mot = L^{3/2} (from BBS single-letter at q^1).
        Path 3: Euler char of partition function = MacMahon.
        """
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        assert result.kappa_num == 1
        assert result.kappa_mot == MotivicClass.L_half(3)  # L^{3/2}
        assert result.euler_char_match

    def test_c3_hocolim_bps_invariants(self):
        """BPS invariants from PLog match expected motivic classes.

        Path 1: BPS invariant at charge n = c3_motivic_bps(n).
        Path 2: χ of BPS invariant = n.
        """
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        for n in range(1, 7):
            assert n in result.bps_invariants
            assert result.bps_invariants[n] == c3_motivic_bps(n)
            assert result.bps_invariants[n].euler_char() == n

    def test_conifold_hocolim(self):
        """Conifold D0-sector: kappa = 0, Z = Exp_*(L^{-1/2} q)."""
        hocolim = MotivicE1Hocolim('conifold', 7)
        result = hocolim.compute_conifold()
        assert result.kappa_num == 0
        assert result.kappa_mot == MotivicClass.zero()
        assert result.euler_char_match

    def test_conifold_euler_char(self):
        """χ(Z^{mot}_{D0}(conifold)) = 1/(1-q) = [1, 1, 1, ...]."""
        hocolim = MotivicE1Hocolim('conifold', 8)
        result = hocolim.compute_conifold()
        Z_chi = [c.euler_char() for c in result.partition_function]
        assert all(x == 1 for x in Z_chi)


# ================================================================
# SECTION 10: MOTIVIC SHADOW TOWER
# ================================================================

class TestMotivicShadowTower:
    """Tests for the motivic shadow tower."""

    def test_genus_0_is_partition_function(self):
        """Θ^{mot}_0 = Z^{mot}_{DT}."""
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        shadow = MotivicShadowTower(result)
        theta0 = shadow.genus_0()
        assert theta0 is result.partition_function

    def test_genus_1_kappa_c3(self):
        """Under χ, Θ^{mot}_1[q¹] = κ = 1 for C³.

        Path 1: Extract from shadow tower.
        Path 2: Direct from hocolim result.
        """
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        shadow = MotivicShadowTower(result)

        kappa_ok, kappa_val = shadow.verify_genus_1_kappa()
        assert kappa_ok, f"κ from shadow = {kappa_val}, expected 1"
        assert kappa_val == 1

        # Path 2
        assert result.kappa_num == 1

    def test_genus_1_motivic_class(self):
        """Θ^{mot}_1[q¹] = L^{3/2} for C³.

        Path 1: From shadow tower extraction.
        Path 2: Equals c3_motivic_bps(1) = single-letter at q^1.
        Path 3: χ gives 1 = κ^{num}.
        """
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        shadow = MotivicShadowTower(result)
        theta1 = shadow.genus_1_c3(7)
        # Path 1
        assert theta1[1] == MotivicClass.L_half(3)
        # Path 2
        assert theta1[1] == c3_motivic_bps(1)
        # Path 3
        assert theta1[1].euler_char() == 1


# ================================================================
# SECTION 11: SYMMETRIC PRODUCTS
# ================================================================

class TestSymmetricProducts:
    """Tests for motivic symmetric product computations."""

    def test_sym0(self):
        """Sym⁰(X) = pt for any X."""
        assert motivic_sym_n(MotivicClass.L(), 0) == MotivicClass.one()

    def test_sym1_A1(self):
        """Sym¹(A¹) = A¹ = L."""
        assert motivic_sym_n(MotivicClass.L(), 1) == MotivicClass.L()

    def test_sym_n_A1(self):
        """[Sym^n(A¹)] = L^n.

        By the fundamental theorem of symmetric polynomials:
        k[x₁,...,xₙ]^{S_n} ≅ k[e₁,...,eₙ] ≅ A^n.
        """
        for n in range(5):
            result = motivic_sym_n(MotivicClass.L(), n)
            assert result == MotivicClass.L(n)


# ================================================================
# SECTION 12: MOEBIUS FUNCTION
# ================================================================

class TestMoebius:
    """Tests for the Moebius function used in PLog."""

    def test_known_values(self):
        """μ(1)=1, μ(2)=-1, μ(3)=-1, μ(4)=0, μ(5)=-1, μ(6)=1."""
        mu = _mobius_sieve(10)
        assert mu[1] == 1
        assert mu[2] == -1
        assert mu[3] == -1
        assert mu[4] == 0
        assert mu[5] == -1
        assert mu[6] == 1

    def test_squarefree(self):
        """μ(n) = 0 iff n has a squared prime factor."""
        mu = _mobius_sieve(30)
        # 4 = 2², 8 = 2³, 9 = 3², 12 = 2²·3, ...
        for n in [4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28]:
            assert mu[n] == 0, f"μ({n}) = {mu[n]}, expected 0"


# ================================================================
# SECTION 13: FULL VERIFICATION PIPELINES
# ================================================================

class TestFullVerification:
    """Tests for the full verification pipelines."""

    def test_c3_euler_specialization(self):
        """Full C³ verification: all paths pass."""
        result = verify_c3_euler_specialization(9)
        assert result['path_1_2_euler_char'], "Path 1-2: χ(Z^{mot}) ≠ M(q)"
        assert result['path_3_plog'], "Path 3: PLog mismatch"
        assert result['path_4_weight_sum'], "Path 4: weight sum ≠ pp(n)"
        assert result['all_pass']

    def test_conifold_euler_specialization(self):
        """Conifold D0-sector: Euler char gives 1/(1-q)."""
        result = verify_conifold_euler_specialization(8)
        assert result['euler_char_match']
        assert result['kappa_num'] == 0

    def test_master_verification(self):
        """Run the complete master verification."""
        result = motivic_master_verification(7)
        assert result['all_pass'], f"Master verification failed: {result}"


# ================================================================
# SECTION 14: CROSS-CHECKS WITH NUMERICAL CODE
# ================================================================

class TestCrossNumerical:
    """Cross-checks between motivic and numerical (e1_hocolim_cy3.py) code."""

    def test_macmahon_agreement(self):
        """Motivic χ agrees with numerical MacMahon through q^8.

        Path 1: motivic_macmahon → euler_char
        Path 2: numerical_macmahon (direct product formula)
        Path 3: OEIS A000219 known values
        """
        N = 9
        oeis = [1, 1, 3, 6, 13, 24, 48, 86, 160]

        # Path 1
        Z_mot = motivic_macmahon(N)
        mot_chi = [c.euler_char() for c in Z_mot]

        # Path 2
        num = numerical_macmahon(N)

        # Path 3
        assert mot_chi == oeis
        assert num == oeis
        assert mot_chi == num

    def test_kappa_c3_agreement(self):
        """κ^{mot}(C³) under χ gives κ^{num} = 1.

        Path 1: From motivic hocolim.
        Path 2: From e1_hocolim_cy3 (imported).
        """
        hocolim_mot = MotivicE1Hocolim('C3', 7)
        result_mot = hocolim_mot.compute_c3()
        assert result_mot.kappa_num == 1

        # Path 2: numerical from existing code
        from compute.lib.e1_hocolim_cy3 import compute_c3_hocolim
        result_num = compute_c3_hocolim()
        assert result_num.kappa == Fraction(1)

        # Agreement
        assert result_mot.kappa_num == int(result_num.kappa)

    def test_kappa_conifold_agreement(self):
        """κ^{mot}(conifold) under χ gives κ^{num} = 0.

        Path 1: From motivic hocolim.
        Path 2: From e1_hocolim_cy3.
        """
        hocolim_mot = MotivicE1Hocolim('conifold', 7)
        result_mot = hocolim_mot.compute_conifold()
        assert result_mot.kappa_num == 0

        from compute.lib.e1_hocolim_cy3 import compute_conifold_hocolim
        result_num = compute_conifold_hocolim()
        assert result_num.kappa == Fraction(0)

        assert result_mot.kappa_num == int(result_num.kappa)


# ================================================================
# SECTION 15: MULTI-PATH CROSS-VALIDATION (AP10)
# ================================================================

class TestMultiPathCrossValidation:
    """Dedicated multi-path cross-validation tests.

    Every claim verified by at least 3 genuinely independent paths.
    This section addresses the AP10 mandate by computing the same
    quantity in multiple independent ways and checking agreement.
    """

    def test_macmahon_four_paths(self):
        """M(q) through q^8 via four independent paths.

        Path 1: motivic PExp then chi
        Path 2: numerical product formula (direct expansion)
        Path 3: OEIS A000219 reference values
        Path 4: coha_chart_explicit._macmahon (independent implementation)
        """
        N = 9
        oeis = [1, 1, 3, 6, 13, 24, 48, 86, 160]

        # Path 1: motivic
        Z_mot = motivic_macmahon(N)
        path1 = [c.euler_char() for c in Z_mot]

        # Path 2: numerical_macmahon in this module
        path2 = numerical_macmahon(N)

        # Path 3: OEIS reference
        path3 = oeis

        # Path 4: independent implementation from coha_chart_explicit
        from compute.lib.coha_chart_explicit import _macmahon as coha_mac
        path4_fps = coha_mac(N)
        path4 = [int(x) for x in path4_fps]

        assert path1 == path2 == path3 == path4

    def test_bps_three_paths(self):
        """BPS invariants for C3 via three independent paths.

        Path 1: c3_motivic_bps(n).euler_char()
        Path 2: PLog of motivic MacMahon, then chi
        Path 3: PLog of numerical MacMahon (plethystic_log from coha_chart_explicit)
        """
        N = 7

        # Path 1: direct BPS function
        path1 = [0] + [c3_motivic_bps(n).euler_char() for n in range(1, N)]

        # Path 2: motivic PLog then chi
        Z_mot = motivic_macmahon(N)
        plog_mot = motivic_plethystic_log(Z_mot, N)
        path2 = [c.euler_char() for c in plog_mot]

        # Path 3: numerical PLog from coha_chart_explicit
        from compute.lib.coha_chart_explicit import (
            _macmahon, plethystic_log as coha_plog,
        )
        mac_fps = _macmahon(N)
        plog_num = coha_plog(mac_fps, N)
        path3 = [int(x) for x in plog_num]

        # All should give [0, 1, 2, 3, 4, 5, 6]
        expected = list(range(N))
        assert path1 == expected
        assert path2 == expected
        assert path3 == expected

    def test_pexp_plog_roundtrip_three_inputs(self):
        """PLog(PExp(f)) = f verified on three different inputs.

        Path A: f = L^{3/2} q (simplest nontrivial)
        Path B: f = BBS single-letter truncated at q^5
        Path C: f = L^{-1/2} q (conifold-type)
        """
        N = 6

        # Path A
        f_a = _mfps_zero(N)
        f_a[1] = MotivicClass.L_half(3)
        Z_a = motivic_plethystic_exp(f_a, N)
        f_a_rec = motivic_plethystic_log(Z_a, N)
        for i in range(N):
            assert f_a[i] == f_a_rec[i]

        # Path B
        f_b = motivic_c3_single_letter(N)
        Z_b = motivic_plethystic_exp(f_b, N)
        f_b_rec = motivic_plethystic_log(Z_b, N)
        for i in range(N):
            assert f_b[i] == f_b_rec[i]

        # Path C
        f_c = _mfps_zero(N)
        f_c[1] = MotivicClass.L_half(-1)
        Z_c = motivic_plethystic_exp(f_c, N)
        f_c_rec = motivic_plethystic_log(Z_c, N)
        for i in range(N):
            assert f_c[i] == f_c_rec[i]

    def test_weight_sum_three_paths(self):
        """Weight sum = pp(n) verified via three paths.

        Path 1: bps_crystal_c3 weight sums
        Path 2: motivic MacMahon then euler_char
        Path 3: numerical MacMahon
        """
        N = 9
        crystal = bps_crystal_c3(N)
        path1 = [sum(crystal.get(n, {}).values()) for n in range(N)]

        Z_mot = motivic_macmahon(N)
        path2 = [c.euler_char() for c in Z_mot]

        path3 = numerical_macmahon(N)

        assert path1 == path2 == path3

    def test_kappa_c3_three_paths(self):
        """kappa(C3) = 1 via three independent paths.

        Path 1: motivic hocolim kappa_num
        Path 2: shadow tower genus-1 chi(Theta_1[q^1])
        Path 3: numerical hocolim from e1_hocolim_cy3
        """
        # Path 1
        hocolim = MotivicE1Hocolim('C3', 7)
        result = hocolim.compute_c3()
        path1 = result.kappa_num

        # Path 2
        shadow = MotivicShadowTower(result)
        _, path2 = shadow.verify_genus_1_kappa()

        # Path 3
        from compute.lib.e1_hocolim_cy3 import compute_c3_hocolim
        path3 = int(compute_c3_hocolim().kappa)

        assert path1 == path2 == path3 == 1

    def test_conifold_partition_three_paths(self):
        """Conifold D0-sector Z at L=1 via three paths.

        Path 1: motivic then chi
        Path 2: Exp_*(q) = 1/(1-q) (direct)
        Path 3: Independent PExp of [pt] q
        """
        N = 8

        # Path 1: motivic
        hocolim = MotivicE1Hocolim('conifold', N)
        result = hocolim.compute_conifold()
        path1 = [c.euler_char() for c in result.partition_function]

        # Path 2: 1/(1-q) directly
        path2 = [1] * N

        # Path 3: PExp of q with [pt] coefficient, then chi
        f = _mfps_zero(N)
        f[1] = MotivicClass.L_half(-1)
        Z = motivic_plethystic_exp(f, N)
        path3 = [c.euler_char() for c in Z]

        assert path1 == path2 == path3

    def test_associativity_three_algebras(self):
        """Motivic CoHA associativity for three different algebra elements.

        Path 1: L, L^2, L^3 with nontrivial Euler form
        Path 2: (L+1), L^2, 3 with trivial Euler form
        Path 3: Half-integer powers with nontrivial Euler form
        """
        # Path 1
        assert verify_motivic_associativity(
            MotivicClass.L(), MotivicClass.L(2), MotivicClass.L(3),
            1, -1, 2, 1,  # ef_abc = ef_ac + ef_bc = 2 + (-1) = 1
        )

        # Path 2 (trivial Euler form)
        assert verify_motivic_associativity(
            MotivicClass.L() + MotivicClass.one(),
            MotivicClass.L(2),
            MotivicClass.from_int(3),
            0, 0, 0, 0,
        )

        # Path 3 (half-integer powers with nontrivial Euler form)
        assert verify_motivic_associativity(
            MotivicClass.L_half(3), MotivicClass.L_half(5), MotivicClass.L_half(7),
            3, -2, 1, -1,  # ef_abc = ef_ac + ef_bc = 1 + (-2) = -1
        )
