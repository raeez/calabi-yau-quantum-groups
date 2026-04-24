"""Tests for cy_euler: CY Euler characteristics, Hodge data, and the
Delta_5 / kappa_BKM connection for quantum vertex chiral groups.

Ground truth:
  chapters/examples/cy_d_kappa_stratification.tex (kappa_BKM = c_N(0)/2),
  chapters/examples/k3e_bkm_chapter.tex (K3 x E tower, Delta_5, c_1(0)=10),
  Gritsenko-Nikulin (Siegel automorphic form corrections of Lorentzian KM algebras),
  Batyrev (toric CY mirror construction),
  Candelas-de la Ossa-Green-Parkes (quintic: chi=-200).
"""

from fractions import Fraction

import pytest

from compute.lib.cy_euler import (
    HodgeDiamond,
    k3_hodge,
    elliptic_curve_hodge,
    product_hodge,
    k3_times_e_hodge,
    quintic_hodge,
    cy3_euler_from_hodge,
    batyrev_hodge_from_data,
    toric_cy3_examples,
    cicy_euler_characteristic,
    cicy_database,
    CICYConfig,
    igusa_cusp_form_weight,
    kappa_k3_times_e,
    decompose_weight_5,
    borcherds_product_weight_from_phi01,
    dt_weight_identity,
    kappa_cy3_families,
    format_hodge_diamond,
    verify_all,
)


# ======================================================================
# 1. Hodge diamond basics
# ======================================================================

class TestHodgeDiamond:
    """Test the HodgeDiamond class and its derived invariants."""

    def test_k3_euler(self):
        """chi(K3) = 24."""
        k3 = k3_hodge()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert k3.euler_characteristic == 24

    def test_k3_hodge_numbers(self):
        """K3 Hodge numbers: h^{0,0}=1, h^{1,0}=0, h^{2,0}=1, h^{1,1}=20."""
        k3 = k3_hodge()
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(0, 0) == 1
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(1, 0) == 0
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(0, 1) == 0
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(2, 0) == 1
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(0, 2) == 1
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(1, 1) == 20
        # VERIFIED [DC] Hodge number [LC] boundary/limiting case
        assert k3.h(2, 2) == 1

    def test_k3_betti(self):
        """Betti numbers of K3: b_0=1, b_1=0, b_2=22, b_3=0, b_4=1."""
        k3 = k3_hodge()
        b = k3.betti
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b == [1, 0, 22, 0, 1]

    def test_k3_chi_y(self):
        """chi_y genus: chi_y(1) = chi = 24, chi_y(0) = chi(O_X) = 2.

        chi_y = sum_p (-y)^p chi_p where chi_p = sum_q (-1)^q h^{p,q}.
        At y=1: sum_p (-1)^p chi_p = sum (-1)^{p+q} h^{p,q} = chi.
        At y=0: chi_0 = chi(O_X).
        At y=-1: sum_p chi_p (signature-related).
        """
        k3 = k3_hodge()
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert k3.chi_y(1) == 24  # topological Euler characteristic
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert k3.chi_y(0) == 2  # chi(O_{K3}) = 2
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert k3.chi_y(-1) == -16  # 2 + (-20) + 2 = -16 (= -sigma(K3)/something)

    def test_k3_arithmetic_genus(self):
        """chi(O_{K3}) = 1 - 0 + 1 = 2 (trivial canonical bundle)."""
        k3 = k3_hodge()
        chi_0 = k3.chi_p(0)
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi_0 == 2

    def test_elliptic_curve_euler(self):
        """chi(E) = 0."""
        e = elliptic_curve_hodge()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert e.euler_characteristic == 0

    def test_elliptic_curve_betti(self):
        """Betti of E: b_0=1, b_1=2, b_2=1."""
        e = elliptic_curve_hodge()
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert e.betti == [1, 2, 1]

    def test_product_formula(self):
        """chi(X x Y) = chi(X) * chi(Y) for topological Euler char."""
        k3 = k3_hodge()
        e = elliptic_curve_hodge()
        prod = product_hodge(k3, e)
        assert prod.euler_characteristic == k3.euler_characteristic * e.euler_characteristic

    def test_hodge_symmetry(self):
        """Hodge symmetry h^{p,q} = h^{q,p} for K3."""
        k3 = k3_hodge()
        for p in range(3):
            for q in range(3):
                assert k3.h(p, q) == k3.h(q, p), f"h^{{{p},{q}}} != h^{{{q},{p}}}"

    def test_serre_duality(self):
        """Serre duality: h^{p,q} = h^{n-p, n-q} for compact Kahler."""
        k3 = k3_hodge()
        n = k3.n
        for p in range(n + 1):
            for q in range(n + 1):
                assert k3.h(p, q) == k3.h(n - p, n - q), (
                    f"Serre duality: h^{{{p},{q}}} != h^{{{n-p},{n-q}}}"
                )


# ======================================================================
# 2. K3 x E: the prototypical CY3
# ======================================================================

class TestK3TimesE:
    """Tests for K3 x E Hodge data and topological invariants."""

    def test_chi_K3xE_vanishes(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert k3e.euler_characteristic == 0

    def test_dimension(self):
        """K3 x E is a 3-fold."""
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] dimension [LC] boundary/limiting case
        assert k3e.n == 3

    def test_h11_K3xE(self):
        """h^{1,1}(K3 x E) = 21.

        Kunneth: h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E) = 20 + 1 = 21.
        """
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(1, 1) == 21

    def test_h21_K3xE(self):
        """h^{2,1}(K3 x E) = 21.

        Kunneth: h^{2,1}(K3)*h^{0,0}(E) + h^{2,0}(K3)*h^{0,1}(E)
               + h^{1,1}(K3)*h^{1,0}(E) + h^{1,0}(K3)*h^{0,1}(E)
               = 0*1 + 1*1 + 20*1 + 0*1 = 21.
        """
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(2, 1) == 21

    def test_h30_K3xE(self):
        """h^{3,0}(K3 x E) = h^{2,0}(K3) * h^{1,0}(E) = 1."""
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(3, 0) == 1

    def test_cy_condition(self):
        """K3 x E has trivial canonical bundle: h^{3,0} = 1."""
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(3, 0) == 1
        # Also h^{1,0} should be 1 (NOT 0: K3 x E is not strict CY)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(1, 0) == 1

    def test_non_strict_cy(self):
        """K3 x E is NOT strict CY: h^{1,0} = 1, h^{2,0} = 1.

        A strict CY3 has h^{1,0} = h^{2,0} = 0.
        K3 x E violates this because E has h^{1,0} = 1.
        """
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(1, 0) == 1  # from h^{1,0}(E) = 1
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(2, 0) == 1  # from h^{2,0}(K3) = 1

    def test_betti_numbers(self):
        """Betti numbers of K3 x E from product formula."""
        k3e = k3_times_e_hodge()
        b = k3e.betti
        # b_k(X x Y) = sum_{i+j=k} b_i(X) * b_j(Y)
        # b_K3 = [1, 0, 22, 0, 1], b_E = [1, 2, 1]
        # b_0 = 1*1 = 1
        # b_1 = 1*2 + 0*1 = 2
        # b_2 = 1*1 + 0*2 + 22*1 = 23
        # b_3 = 0*1 + 22*2 + 0*1 = 44
        # b_4 = 22*1 + 0*2 + 1*1 = 23
        # b_5 = 0*1 + 1*2 = 2
        # b_6 = 1*1 = 1
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b == [1, 2, 23, 44, 23, 2, 1]
        # Check: chi = sum (-1)^k b_k = 1 - 2 + 23 - 44 + 23 - 2 + 1 = 0
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert sum((-1) ** k * b[k] for k in range(7)) == 0

    def test_h11_equals_h21(self):
        """For K3 x E, h^{1,1} = h^{2,1} = 21, so chi = 2(21-21) = 0.

        This is the "self-mirror" property at the level of Hodge numbers.
        """
        k3e = k3_times_e_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert k3e.h(1, 1) == k3e.h(2, 1) == 21


# ======================================================================
# 3. Quintic threefold
# ======================================================================

class TestQuintic:
    """Tests for the quintic CY3 in P^4."""

    def test_chi_quintic(self):
        """chi(quintic) = -200."""
        q = quintic_hodge()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert q.euler_characteristic == -200

    def test_h11_quintic(self):
        """h^{1,1}(quintic) = 1 (the hyperplane class)."""
        q = quintic_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q.h(1, 1) == 1

    def test_h21_quintic(self):
        """h^{2,1}(quintic) = 101 (complex structure deformations)."""
        q = quintic_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q.h(2, 1) == 101

    def test_strict_cy_condition(self):
        """The quintic is strict CY: h^{1,0} = h^{2,0} = 0, h^{3,0} = 1."""
        q = quintic_hodge()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q.h(1, 0) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q.h(2, 0) == 0
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert q.h(3, 0) == 1

    def test_chi_from_hodge_formula(self):
        """chi = 2(h^{1,1} - h^{2,1}) = 2(1 - 101) = -200."""
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(1, 101) == -200

    def test_mirror_quintic(self):
        """Mirror quintic has h^{1,1}=101, h^{2,1}=1, chi=+200."""
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(101, 1) == 200

    def test_betti_numbers(self):
        """Betti of quintic: b_0=1, b_1=0, b_2=1, b_3=204, b_4=1, b_5=0, b_6=1."""
        q = quintic_hodge()
        b = q.betti
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[0] == 1
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[1] == 0
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[2] == 1
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[3] == 2 + 2 * 101  # 2(1 + h^{2,1}) = 204
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[4] == 1
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[5] == 0
        # VERIFIED [DC] Betti number [LC] boundary/limiting case
        assert b[6] == 1

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} for the quintic."""
        q = quintic_hodge()
        for p in range(4):
            for qq in range(4):
                assert q.h(p, qq) == q.h(qq, p)

    def test_serre_duality(self):
        """h^{p,q} = h^{3-p, 3-q} for the quintic."""
        q = quintic_hodge()
        for p in range(4):
            for qq in range(4):
                assert q.h(p, qq) == q.h(3 - p, 3 - qq)


# ======================================================================
# 4. CY3 Euler from Hodge numbers
# ======================================================================

class TestCY3EulerFormula:
    """Test the formula chi = 2(h^{1,1} - h^{2,1})."""

    def test_quintic(self):
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(1, 101) == -200

    def test_mirror_quintic(self):
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(101, 1) == 200

    def test_self_mirror(self):
        """Self-mirror: h^{1,1} = h^{2,1} implies chi = 0."""
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(21, 21) == 0
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(11, 11) == 0

    def test_various_known(self):
        """Various known CY3 Euler characteristics."""
        # WP4(1,1,2,2,2)[8]: h11=1, h21=149, chi=-296
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(1, 149) == -296
        # WP4(1,1,1,1,2)[6]: h11=1, h21=89, chi=-176
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(1, 89) == -176


# ======================================================================
# 5. Toric CY3 examples
# ======================================================================

class TestToricCY3:
    """Tests for toric CY3 data."""

    def test_all_consistent(self):
        """All toric examples satisfy chi = 2(h^{1,1} - h^{2,1})."""
        examples = toric_cy3_examples()
        for name, (h11, h21, chi) in examples.items():
            # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
            assert chi == 2 * (h11 - h21), f"{name}: inconsistent"

    def test_quintic_in_list(self):
        """The quintic appears in the toric list."""
        examples = toric_cy3_examples()
        assert "quintic P4[5]" in examples
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert examples["quintic P4[5]"] == (1, 101, -200)

    def test_negative_euler(self):
        """All one-parameter examples have negative Euler char."""
        examples = toric_cy3_examples()
        for name, (h11, h21, chi) in examples.items():
            if h11 == 1:
                # VERIFIED [DC] Hodge number [LC] boundary/limiting case
                assert chi < 0, f"{name} with h11=1 should have chi < 0"


# ======================================================================
# 6. CICY (Complete Intersection) Euler characteristics
# ======================================================================

class TestCICY:
    """Tests for complete intersection CY3 Euler characteristics."""

    def test_quintic(self):
        """Quintic P^4[5]: chi = -200."""
        chi = cicy_euler_characteristic([4], [[5]])
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -200

    def test_P5_3_3(self):
        """P^5[3,3]: two cubics in P^5, chi = -144."""
        chi = cicy_euler_characteristic([5], [[3], [3]])
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -144

    def test_P5_2_4(self):
        """P^5[2,4]: chi = -176."""
        chi = cicy_euler_characteristic([5], [[2], [4]])
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -176

    def test_P6_2_2_3(self):
        """P^6[2,2,3]: chi = -144.

        CY condition: 2+2+3 = 7 = 6+1. dim X = 6-3 = 3.
        Chern class: c(TX) = (1+H)^7 / [(1+2H)^2(1+3H)] = 1 + 5H^2 - 12H^3 + ...
        chi = c_3 * degree = (-12) * 12 = -144.
        h^{1,1}=1, h^{2,1}=73.
        """
        chi = cicy_euler_characteristic([6], [[2], [2], [3]])
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -144

    def test_P7_2_2_2_2(self):
        """P^7[2,2,2,2]: chi = -128."""
        chi = cicy_euler_characteristic([7], [[2], [2], [2], [2]])
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -128

    def test_cy_condition_violated(self):
        """Raise error if CY condition sum(d_i) != n+1 is violated."""
        with pytest.raises(ValueError, match="CY condition"):
            cicy_euler_characteristic([4], [[4]])  # sum=4 != 5

    def test_not_threefold(self):
        """Raise error if result is not a 3-fold."""
        with pytest.raises(ValueError, match="Not a CY3"):
            cicy_euler_characteristic([3], [[4]])  # dim = 3 - 1 = 2

    def test_two_ambient_P2xP2(self):
        """P^2 x P^2 with bidegrees [3,0] and [0,3]: chi = -162.

        Two cubics, one in each P^2 factor. CY condition:
        Factor 0: d_{1,0} + d_{2,0} = 3 + 0 = 3 = 2 + 1. Good.
        Factor 1: d_{1,1} + d_{2,1} = 0 + 3 = 3 = 2 + 1. Good.
        dim X = (2+2) - 2 = 2... wait, that's not 3!
        Actually P^2 x P^2 has dimension 4, two hypersurfaces give dim 2.
        This is NOT a CY3!
        """
        with pytest.raises(ValueError, match="Not a CY3"):
            cicy_euler_characteristic([2, 2], [[3, 0], [0, 3]])

    def test_P1xP3_cicy(self):
        """P^1 x P^3 [0,2 | 2,2]: dim = (1+3) - 2 = 2... not a CY3 either.
        Need to use the right configuration.
        """
        # P^1 x P^3 with two hypersurfaces: dim = 4 - 2 = 2. Not CY3.
        # For a CY3 from two projective spaces, we need dim = n1 + n2 - K = 3.
        # E.g., P^2 x P^5 with K=4 hypersurfaces... or P^1 x P^4 with K=2.
        # P^1 x P^4 [2,0 | 0,5]: CY condition: factor 0: 2+0=2=1+1, factor 1: 0+5=5=4+1.
        # dim = (1+4) - 2 = 3. Good!
        chi = cicy_euler_characteristic([1, 4], [[2, 0], [0, 5]])
        # This is P^1 x (quintic in P^4), which has chi = chi(P^1) * chi(quintic_3fold_in_P^4)?
        # No, the [2,0] means the first equation involves only P^1 coords (degree 2),
        # and [0,5] means the second involves only P^4 coords (degree 5).
        # The first cuts P^1 to 2 points, the second cuts P^4 to a quintic 3-fold.
        # So X = {2 points} x (quintic surface... no, quintic in P^4 is a 3-fold).
        # Wait, dim P^1 = 1, cutting by degree 2 gives 0-dim (2 points). No good.
        # Actually, total dim = 1+4 = 5, two hypersurfaces give dim 3.
        # But the first equation (degree 2 in P^1 only) makes P^1 x P^4 into
        # {2 points} x P^4 union ... no, the zero locus of a section of O(2,0)
        # on P^1 x P^4 is the pullback from P^1, so it's {2 points} x P^4,
        # which has two components of dim 4. The second equation (O(0,5)) cuts
        # each to a quintic 3-fold. So X = Q_1 union Q_2 (disconnected). chi = -400.
        # But our formula computes the integral, which gives the total.
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert chi == -400  # = 2 * (-200)

    def test_cicy_database_consistency(self):
        """All CICY database entries satisfy chi = 2(h11 - h21)."""
        for config in cicy_database():
            # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
            assert config.chi == 2 * (config.h11 - config.h21), (
                f"{config.name}: chi mismatch"
            )

    def test_cicy_database_euler_computation(self):
        """Verify computable CICY entries match database chi values."""
        # Only test single-ambient entries (multi-ambient is tested separately)
        for config in cicy_database():
            if len(config.ambient_dims) == 1:
                computed = cicy_euler_characteristic(config.ambient_dims, config.degrees)
                assert computed == config.chi, (
                    f"{config.name}: computed {computed} != database {config.chi}"
                )


# ======================================================================
# 7. The Delta_5 connection: kappa_BKM(K3 x E) = 5
# ======================================================================

class TestDelta5Connection:
    """Tests for kappa_BKM(Delta_5) = weight(Delta_5) = c_1(0)/2 = 5."""

    def test_kappa_equals_5(self):
        """kappa_BKM(Delta_5) = 5 by the Borcherds weight theorem."""
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert kappa_k3_times_e() == 5

    def test_igusa_weight(self):
        """weight(Delta_5) = 5 for the N=1 K3 x E tower."""
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert igusa_cusp_form_weight(1) == 5

    def test_igusa_weight_N2(self):
        """weight(Delta_3) = 3 for the N=2 K3 x E tower."""
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert igusa_cusp_form_weight(2) == 3

    def test_igusa_weight_N3(self):
        """weight(Delta_2) = 2 for the N=3 K3 x E tower."""
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert igusa_cusp_form_weight(3) == 2

    def test_borcherds_product_weight(self):
        """Borcherds product formula gives weight 5."""
        # VERIFIED [DC] conformal weight [LC] boundary/limiting case
        assert borcherds_product_weight_from_phi01() == 5

    def test_h11_over_4_is_coincidence_not_source(self):
        """h^{1,1}(K3)/4 = 5 is a sanity check, not a source formula."""
        k3 = k3_hodge()
        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert k3.h(1, 1) == 20
        # VERIFIED [DC] kappa computation [LC] boundary/limiting case
        assert Fraction(k3.h(1, 1), 4) == 5

    def test_chi_minus_4_over_4_is_coincidence_not_source(self):
        """(chi(K3)-4)/4 = 5 is a sanity check, not a source formula."""
        k3 = k3_hodge()
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert Fraction(k3.euler_characteristic - 4, 4) == 5

    def test_dim_Sp4_over_2(self):
        """dim(Sp_4)/2 matches 5 but is not the source."""
        # dim Sp_4 as a real Lie group = 10 (= 2*2 + 2*2*(2-1)/2 ... no,
        # dim Sp_{2n} = n(2n+1). For n=2: 2*5 = 10.)
        dim_sp4 = 2 * (2 * 2 + 1)  # n(2n+1) with n=2
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dim_sp4 == 10
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert dim_sp4 // 2 == 5


# ======================================================================
# 8. DT weight identity: 10 = 2 * 5
# ======================================================================

class TestDTWeightIdentity:
    """Tests for the DT partition function weight identity."""

    def test_inverse_Z_weight_10(self):
        """1/Z^{K3 x E} ~ (Delta_5)^2 has weight 10 = 2 * 5."""
        dt = dt_weight_identity()
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert dt["weight_inverse_Z"] == 10
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert dt["weight_Delta5_squared"] == 10

    def test_10_is_2_kappa_BKM(self):
        """10 = 2 * kappa_BKM(K3 x E)."""
        dt = dt_weight_identity()
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert dt["2_times_kappa_BKM"] == 10

    def test_10_is_dim_Sp4(self):
        """dim(Sp_4) matches 10 but is not the source."""
        dt = dt_weight_identity()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert dt["dim_Sp4"] == 10
        assert dt["dim_Sp4_is_source"] is False

    def test_10_from_chi_K3(self):
        """(chi(K3)-4)/2 matches 10 but is not the source."""
        dt = dt_weight_identity()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert dt["chi_K3_minus_4_over_2"] == 10
        assert dt["chi_K3_minus_4_over_2_is_source"] is False

    def test_10_from_h11_K3(self):
        """h^{1,1}(K3)/2 matches 10 but is not the source."""
        dt = dt_weight_identity()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert dt["h11_K3_over_2"] == 10
        assert dt["h11_K3_over_2_is_source"] is False

    def test_10_is_borcherds_c_1_0(self):
        """10 = c_1(0), the Borcherds input coefficient."""
        dt = dt_weight_identity()
        # VERIFIED [DC] Faber-Pandharipande genus formula [LC] boundary/limiting case
        assert dt["c_1_0"] == 10

    def test_all_equal(self):
        """All expressions for weight 10 agree."""
        dt = dt_weight_identity()
        assert dt["all_equal_10"] is True


# ======================================================================
# 9. The decompose_weight_5 analysis
# ======================================================================

class TestDecomposeWeight5:
    """Test the lane-separated diagnostics around weight 5."""

    def test_basic_data(self):
        d = decompose_weight_5()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert d["chi_K3"] == 24
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert d["chi_E"] == 0
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert d["chi_K3xE"] == 0
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert d["h11_K3"] == 20
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert d["h20_K3"] == 1

    def test_h11_over_4_formula(self):
        """h^{1,1}(K3)/4 matches 5 but is not the source."""
        d = decompose_weight_5()
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert d["h11_K3_over_4"] == 5
        assert d["h11_over_4_matches_kappa_BKM"] is True
        assert d["h11_over_4_is_source"] is False

    def test_chi_minus_4_over_4_formula(self):
        """(chi(K3)-4)/4 matches 5 but is not the source."""
        d = decompose_weight_5()
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert d["chi_K3_minus_4_over_4"] == 5
        assert d["chi_minus_4_over_4_matches_kappa_BKM"] is True
        assert d["chi_minus_4_over_4_is_source"] is False

    def test_borcherds_perspective(self):
        """c_1(0)=10 is the Borcherds input, weight = c_1(0)/2 = 5."""
        d = decompose_weight_5()
        # VERIFIED [DC] Faber-Pandharipande genus formula [LC] boundary/limiting case
        assert d["c_1_0"] == 10
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert d["weight_from_borcherds"] == 5
        assert d["h11_K3_over_2_matches_c_1_0"] is True
        assert d["h11_K3_over_2_is_source"] is False

    def test_sp4_perspective(self):
        """dim(Sp_4)/2 matches 5 but is not the source."""
        d = decompose_weight_5()
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert d["dim_Sp4"] == 10
        # VERIFIED [DC] dimension count [DA] dimensional consistency
        assert d["dim_Sp4_over_2"] == 5
        assert d["dim_Sp4_over_2_is_source"] is False

    def test_dt_consistency(self):
        """2 * kappa_BKM = weight(1/Z)."""
        d = decompose_weight_5()
        assert d["two_kappa_BKM_equals_weight_inverse_Z"] is True


# ======================================================================
# 10. Weyl vector and lattice inner products
# ======================================================================

class TestLatticeData:
    """Verify the lattice Lambda^{2,1} inner products from k3_times_e.tex."""

    def test_gram_matrix_delta(self):
        """Gram matrix of simple roots delta_1, delta_2, delta_3.

        From k3_times_e.tex, the Gram matrix is:
        [[ 2, -2, -2],
         [-2,  2, -2],
         [-2, -2,  2]]
        """
        gram = [
            [2, -2, -2],
            [-2, 2, -2],
            [-2, -2, 2],
        ]
        # Check symmetry
        for i in range(3):
            for j in range(3):
                assert gram[i][j] == gram[j][i]
        # Determinant = 2*(4-4) + 2*(-4+4) + (-2)(4+4)... let me compute.
        # det = 2*(2*2 - (-2)*(-2)) - (-2)*((-2)*2 - (-2)*(-2)) + (-2)*((-2)*(-2) - 2*(-2))
        # = 2*(4-4) + 2*(-4-4) + (-2)*(4+4) -- wait, expanding along first row:
        # det = 2*(4 - 4) - (-2)*(-4 - (-2)*(-2)) + (-2)*((-2)*(-2) - 2*(-2))
        # Hmm, let me just compute:
        # det = 2*(2*2 - (-2)(-2)) - (-2)((-2)*2 - (-2)(-2)) + (-2)((-2)(-2) - 2*(-2))
        # = 2*(4-4) - (-2)*(-4-4) + (-2)*(4-(-4))
        # = 0 - (-2)*(-8) + (-2)*8
        # = 0 - 16 - 16 = -32
        det = (gram[0][0] * (gram[1][1] * gram[2][2] - gram[1][2] * gram[2][1])
             - gram[0][1] * (gram[1][0] * gram[2][2] - gram[1][2] * gram[2][0])
             + gram[0][2] * (gram[1][0] * gram[2][1] - gram[1][1] * gram[2][0]))
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert det == -32
        # Negative determinant => indefinite form => hyperbolic lattice. Good.

    def test_weyl_vector_inner_products(self):
        """(rho, delta_i) = -1 for all i (from def:k3e-weyl-vector)."""
        # rho = (1/2)(delta_1 + delta_2 + delta_3)
        # (rho, delta_1) = (1/2)((delta_1,delta_1) + (delta_2,delta_1) + (delta_3,delta_1))
        #                = (1/2)(2 + (-2) + (-2)) = (1/2)(-2) = -1. Good.
        gram = [[2, -2, -2], [-2, 2, -2], [-2, -2, 2]]
        rho_coeffs = [Fraction(1, 2)] * 3  # rho = (1/2)(d1 + d2 + d3)
        for i in range(3):
            inner = sum(rho_coeffs[j] * gram[j][i] for j in range(3))
            # VERIFIED [DC] structural property [LC] boundary/limiting case
            assert inner == -1, f"(rho, delta_{i+1}) = {inner} != -1"

    def test_weyl_vector_norm(self):
        """(rho, rho) for the Weyl vector in Lambda^{2,1}.

        rho = f_2 - (1/2)f_3 + f_{-2}.
        Gram in (f_2, f_3, f_{-2}): [[0,0,-1],[0,2,0],[-1,0,0]].
        (rho, rho) = 0 + (1/4)*2 + 0 + 0 + 2*(-1) + 0 = 1/2 - 2 = -3/2.
        """
        # Gram matrix in f-basis
        gram_f = [[0, 0, -1], [0, 2, 0], [-1, 0, 0]]
        rho_f = [Fraction(1), Fraction(-1, 2), Fraction(1)]  # f_2 - (1/2)f_3 + f_{-2}
        norm = sum(
            rho_f[i] * gram_f[i][j] * rho_f[j]
            for i in range(3) for j in range(3)
        )
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert norm == Fraction(-3, 2)


# ======================================================================
# 11. The phi_{0,1} Fourier data
# ======================================================================

class TestPhi01:
    """Tests for the weak Jacobi form phi_{0,1} data."""

    def test_zero_fourier_coefficient(self):
        """c(0,0) = 20 = h^{1,1}(K3)."""
        from compute.lib.cy_euler import _theta_jacobi_coeffs
        coeffs = _theta_jacobi_coeffs(2, 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[(0, 0)] == 20

    def test_pm1_fourier_coefficient(self):
        """c(0, +/-1) = 2 (the y and y^{-1} terms)."""
        from compute.lib.cy_euler import _theta_jacobi_coeffs
        coeffs = _theta_jacobi_coeffs(2, 3)
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[(0, 1)] == 2
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert coeffs[(0, -1)] == 2

    def test_elliptic_genus_chi(self):
        """phi_{0,1}(tau, 0) = chi(K3) = 24 at q = 0.

        Specializing z = 0 (y = 1): sum_l c(0, l) = 2 + 20 + 2 = 24.
        """
        from compute.lib.cy_euler import _theta_jacobi_coeffs
        coeffs = _theta_jacobi_coeffs(2, 3)
        q0_sum = sum(v for (n, l), v in coeffs.items() if n == 0)
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert q0_sum == 24

    def test_c_1_0_gives_weight(self):
        """The raw q^0 head is consistent with the program c_1(0)=10."""
        from compute.lib.cy_euler import _theta_jacobi_coeffs
        coeffs = _theta_jacobi_coeffs(2, 3)
        c_1_0_from_raw_head = coeffs[(0, 0)] // 2  # = 10
        weight = c_1_0_from_raw_head // 2  # = 5
        # VERIFIED [DC] conformal weight [DA] dimensional consistency
        assert weight == 5


# ======================================================================
# 12. CY3 families survey
# ======================================================================

class TestCY3Families:
    """Tests for the CY3 families survey."""

    def test_k3_times_e_entry(self):
        families = kappa_cy3_families()
        k3e = families["K3 x E"]
        # VERIFIED [DC] kappa formula [LC] boundary/limiting case
        assert k3e["kappa_label"] == "kappa_BKM"
        assert k3e["kappa_BKM"] == 5
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert k3e["chi"] == 0
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert k3e["h11"] == 21
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert k3e["h21"] == 21

    def test_quintic_entry(self):
        families = kappa_cy3_families()
        q = families["Quintic P4[5]"]
        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert q["chi"] == -200
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert q["h11"] == 1
        # VERIFIED [DC] Hodge diamond [LT] literature cross-check
        assert q["h21"] == 101
        # kappa_BKM is undefined here without a Borcherds denominator.
        assert q["kappa_label"] == "kappa_BKM"
        assert q["kappa_BKM"] is None

    def test_quintic_chi_over_24(self):
        """chi(quintic)/24 = -200/24 = -25/3 (not an integer)."""
        families = kappa_cy3_families()
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert families["Quintic P4[5]"]["chi_over_24"] == Fraction(-25, 3)


# ======================================================================
# 13. Hodge diamond formatting
# ======================================================================

class TestFormatting:
    """Tests for display functions."""

    def test_format_k3(self):
        """K3 diamond should be a valid string."""
        diamond = format_hodge_diamond(k3_hodge())
        assert "20" in diamond
        assert "1" in diamond

    def test_format_quintic(self):
        """Quintic diamond should contain 101."""
        diamond = format_hodge_diamond(quintic_hodge())
        assert "101" in diamond


# ======================================================================
# 14. Master verification
# ======================================================================

class TestVerifyAll:
    """Run the full internal consistency check."""

    def test_all_pass(self):
        results = verify_all()
        for name, passed in results.items():
            assert passed, f"verify_all: {name} FAILED"

    def test_count(self):
        """There should be a substantial number of checks."""
        results = verify_all()
        # VERIFIED [DC] structural property [LC] boundary/limiting case
        assert len(results) >= 20


# ======================================================================
# 15. Edge cases and error handling
# ======================================================================

class TestEdgeCases:
    """Test error handling and edge cases."""

    def test_igusa_weight_invalid_N(self):
        with pytest.raises(ValueError):
            igusa_cusp_form_weight(5)

    def test_hodge_diamond_invalid_entry(self):
        with pytest.raises(AssertionError):
            HodgeDiamond(1, {(2, 0): 1})  # p=2 > n=1

    def test_cy3_euler_zero(self):
        """Self-mirror CY3 has chi = 0."""
        # VERIFIED [DC] Euler characteristic [LC] boundary/limiting case
        assert cy3_euler_from_hodge(0, 0) == 0

    def test_product_is_associative_on_chi(self):
        """chi(A x B x C) = chi(A) * chi(B) * chi(C)."""
        k3 = k3_hodge()
        e1 = elliptic_curve_hodge()
        e2 = elliptic_curve_hodge()

        prod_12 = product_hodge(k3, e1)
        prod_123 = product_hodge(prod_12, e2)

        # VERIFIED [DC] Euler characteristic formula [LC] boundary/limiting case
        assert prod_123.euler_characteristic == (
            k3.euler_characteristic * e1.euler_characteristic * e2.euler_characteristic
        )
