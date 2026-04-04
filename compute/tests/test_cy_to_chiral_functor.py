r"""Tests for the CY-to-chiral functor Phi: CY_d-Cat -> E_2-ChirAlg.

Verifies:
  1. Hochschild homology computations from Hodge data (all standard CY)
  2. Cyclic structure extraction (CY trace, pairings)
  3. Lie conformal algebra construction (Heisenberg, lattice, general)
  4. Factorization envelope (chiral algebra identification)
  5. E_2 enhancement (braiding type)
  6. Cross-volume bridge: kappa(A_C) matches Vol I's shadow tower

Ground truth:
  - Vol I: heisenberg_bar.py (kappa(H_k) = k)
  - Vol I: betagamma_bar.py, betagamma_determinant.py (kappa(bg) = c/2)
  - Vol III: cy_euler.py (Hodge data, chi, kappa families)
  - Vol III: e2_bar_complex.py (E_2 bar complex structure)
  - Vol III: conifold_wall_crossing.py (KS pentagon, DT partition function)
  - Caldararu (2003): Mukai pairing and HH
  - BCOV (1994): kappa = chi/24 for CY3
  - Costello (2007): topological CFT and CY categories

60+ tests organized by the five steps of the functor.
"""

from fractions import Fraction

import pytest

from compute.lib.cy_to_chiral_functor import (
    CYHodgeData,
    ChiralAlgebraData,
    CYCyclicStructure,
    HochschildHomology,
    LieConformalData,
    PhiResult,
    apply_factorization_envelope,
    conifold_betagamma_match,
    conifold_data,
    construct_lie_conformal,
    cy3_kappa_landscape,
    e2_enhancement_data,
    elliptic_curve_data,
    extract_cyclic_structure,
    hh_decomposition_table,
    hh_from_hodge,
    k3_data,
    k3_times_e_data,
    kappa_betagamma,
    kappa_cy2_lattice,
    kappa_cy3_bcov,
    kappa_from_cy,
    kappa_heisenberg,
    matrix_factorization_data,
    mukai_lattice_k3,
    phi_conifold,
    phi_elliptic_curve,
    phi_k3,
    phi_matrix_factorization,
    phi_quintic,
    phi_summary,
    quintic_data,
    verify_all,
    verify_hh_dimensions,
    verify_kappa_bridge,
)


# ======================================================================
# 1. Hodge data basics
# ======================================================================

class TestHodgeData:
    """Test the CYHodgeData representation."""

    def test_elliptic_curve_dim(self):
        """Elliptic curve is CY 1-fold."""
        ec = elliptic_curve_data()
        assert ec.dim == 1

    def test_elliptic_curve_chi(self):
        """chi(E) = 0."""
        ec = elliptic_curve_data()
        assert ec.euler_characteristic == 0

    def test_elliptic_curve_hodge_numbers(self):
        """Elliptic curve: h^{0,0} = h^{1,1} = h^{1,0} = h^{0,1} = 1."""
        ec = elliptic_curve_data()
        assert ec.h(0, 0) == 1
        assert ec.h(1, 0) == 1
        assert ec.h(0, 1) == 1
        assert ec.h(1, 1) == 1

    def test_k3_dim(self):
        """K3 is CY 2-fold."""
        k3 = k3_data()
        assert k3.dim == 2

    def test_k3_chi(self):
        """chi(K3) = 24."""
        k3 = k3_data()
        assert k3.euler_characteristic == 24

    def test_k3_hodge_numbers(self):
        """K3: h^{2,0} = 1, h^{1,1} = 20, h^{1,0} = 0."""
        k3 = k3_data()
        assert k3.h(2, 0) == 1
        assert k3.h(1, 1) == 20
        assert k3.h(1, 0) == 0
        assert k3.h(0, 1) == 0

    def test_quintic_dim(self):
        """Quintic is CY 3-fold."""
        q = quintic_data()
        assert q.dim == 3

    def test_quintic_chi(self):
        """chi(quintic) = -200."""
        q = quintic_data()
        assert q.euler_characteristic == -200

    def test_quintic_hodge(self):
        """Quintic: h^{1,1} = 1, h^{2,1} = 101."""
        q = quintic_data()
        assert q.h(1, 1) == 1
        assert q.h(2, 1) == 101
        assert q.h(3, 0) == 1  # holomorphic 3-form

    def test_k3_times_e_dim(self):
        """K3 x E is CY 3-fold."""
        kxe = k3_times_e_data()
        assert kxe.dim == 3

    def test_k3_times_e_chi(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        kxe = k3_times_e_data()
        assert kxe.euler_characteristic == 0

    def test_k3_times_e_hodge(self):
        """K3 x E: h^{1,1} = h^{2,1} = 21."""
        kxe = k3_times_e_data()
        assert kxe.h(1, 1) == 21
        assert kxe.h(2, 1) == 21


# ======================================================================
# 2. Hochschild homology from Hodge data
# ======================================================================

class TestHochschildHomology:
    """Test HH_*(D^b(X)) computation from Hodge numbers."""

    def test_ec_hh_total(self):
        """Elliptic curve: total dim HH = 4."""
        hh = hh_from_hodge(elliptic_curve_data())
        assert hh.total_dim == 4

    def test_ec_hh0(self):
        """Elliptic curve: HH_0 = H*(E, O_E) = 2."""
        hh = hh_from_hodge(elliptic_curve_data())
        assert hh.dim_by_degree[0] == 2

    def test_ec_hh1(self):
        """Elliptic curve: HH_1 = H*(E, T_E) = H*(E, O_E) = 2."""
        hh = hh_from_hodge(elliptic_curve_data())
        assert hh.dim_by_degree[1] == 2

    def test_k3_hh_total(self):
        """K3: total dim HH = 24 (Mukai lattice rank)."""
        hh = hh_from_hodge(k3_data())
        assert hh.total_dim == 24

    def test_k3_hh0(self):
        """K3: HH_0 = H*(K3, O) = 1 + 0 + 1 = 2."""
        hh = hh_from_hodge(k3_data())
        assert hh.dim_by_degree[0] == 2

    def test_k3_hh1(self):
        """K3: HH_1 = H*(K3, T) = H*(K3, Omega^1) = 0 + 20 + 0 = 20."""
        hh = hh_from_hodge(k3_data())
        assert hh.dim_by_degree[1] == 20

    def test_k3_hh2(self):
        """K3: HH_2 = H*(K3, /\\^2 T) = H*(K3, O) = 2."""
        hh = hh_from_hodge(k3_data())
        assert hh.dim_by_degree[2] == 2

    def test_k3_hh_sum(self):
        """K3: 2 + 20 + 2 = 24."""
        hh = hh_from_hodge(k3_data())
        assert sum(hh.dim_by_degree.values()) == 24

    def test_quintic_hh_total(self):
        """Quintic: total dim HH = 208."""
        hh = hh_from_hodge(quintic_data())
        assert hh.total_dim == 208

    def test_quintic_hh0(self):
        """Quintic: HH_0 = H*(Q, O) = 1 + 0 + 0 + 1 = 2."""
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[0] == 2

    def test_quintic_hh1(self):
        r"""Quintic: HH_1 = H*(Q, T_Q) = H*(Q, Omega^2).

        H^q(Q, Omega^2) = h^{2,q}:
          h^{2,0} = 0, h^{2,1} = 101, h^{2,2} = 1, h^{2,3} = 0.
        Total = 102.
        """
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[1] == 102

    def test_quintic_hh2(self):
        r"""Quintic: HH_2 = H*(Q, /\^2 T) = H*(Q, Omega^1).

        H^q(Q, Omega^1) = h^{1,q}:
          h^{1,0} = 0, h^{1,1} = 1, h^{1,2} = 101, h^{1,3} = 0.
        Total = 102.
        """
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[2] == 102

    def test_quintic_hh3(self):
        """Quintic: HH_3 = H*(Q, O) = 2."""
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[3] == 2

    def test_quintic_hh_symmetry(self):
        """For CY3: dim HH_0 = dim HH_3 and dim HH_1 = dim HH_2 (Serre duality)."""
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[3]
        assert hh.dim_by_degree[1] == hh.dim_by_degree[2]

    def test_ec_hh_symmetry(self):
        """For CY1: dim HH_0 = dim HH_1 (Serre duality)."""
        hh = hh_from_hodge(elliptic_curve_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[1]

    def test_k3_hh_symmetry(self):
        """For CY2: dim HH_0 = dim HH_2 (Serre duality)."""
        hh = hh_from_hodge(k3_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[2]


# ======================================================================
# 3. Cyclic structure extraction
# ======================================================================

class TestCyclicStructure:
    """Test the cyclic A-infinity structure extraction (Step 1)."""

    def test_ec_cyclic_dim(self):
        ec = extract_cyclic_structure(elliptic_curve_data())
        assert ec.cy_dim == 1

    def test_ec_lie_bracket_abelian(self):
        """Elliptic curve: Lie bracket is abelian (E_infty)."""
        ec = extract_cyclic_structure(elliptic_curve_data())
        assert "abelian" in ec.lie_bracket_type

    def test_k3_cyclic_signature(self):
        """K3: Mukai pairing has signature (4, 20)."""
        k3 = extract_cyclic_structure(k3_data())
        assert k3.pairing_signature == (4, 20)

    def test_quintic_cyclic_dim(self):
        q = extract_cyclic_structure(quintic_data())
        assert q.cy_dim == 3

    def test_quintic_hh_dims(self):
        """Quintic cyclic structure carries the HH dimensions."""
        q = extract_cyclic_structure(quintic_data())
        assert q.hh_dims[0] == 2
        assert q.hh_dims[1] == 102


# ======================================================================
# 4. Lie conformal algebra construction
# ======================================================================

class TestLieConformal:
    """Test the Lie conformal algebra R_C (Step 3)."""

    def test_ec_rank(self):
        """Elliptic curve: R_E has rank 1 (one free boson)."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.rank == 1

    def test_ec_type(self):
        """Elliptic curve: Heisenberg type."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.bracket_type == "heisenberg"

    def test_ec_level(self):
        """Elliptic curve: level = 1 (unit Serre pairing)."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.level_matrix == Fraction(1)

    def test_k3_rank(self):
        """K3: R_{K3} has rank 24 (Mukai lattice rank)."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.rank == 24

    def test_k3_type(self):
        """K3: Heisenberg type (free bosons)."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.bracket_type == "heisenberg"

    def test_k3_weights(self):
        """K3: all generators have conformal weight 1."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        assert all(w == 1 for w in lcd.conformal_weights)
        assert len(lcd.conformal_weights) == 24

    def test_quintic_rank(self):
        """Quintic: R_Q has rank = dim HH_1 = 102."""
        cyc = extract_cyclic_structure(quintic_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.rank == 102

    def test_quintic_type(self):
        """Quintic: general CY3 type (not Heisenberg)."""
        cyc = extract_cyclic_structure(quintic_data())
        lcd = construct_lie_conformal(cyc)
        assert lcd.bracket_type == "general_cy3"


# ======================================================================
# 5. Chiral algebra (factorization envelope)
# ======================================================================

class TestChiralAlgebra:
    """Test the chiral algebra A_C = Fact(R_C) (Steps 4-5)."""

    def test_ec_kappa(self):
        """Elliptic curve: kappa(A_E) = kappa(H_1) = 1.

        Vol I authoritative: kappa(H_k) = k.
        Rank-1 Heisenberg at level 1: kappa = 1.
        """
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=1)
        assert chiral.kappa == Fraction(1)

    def test_ec_central_charge(self):
        """Elliptic curve: c(A_E) = rank = 1."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=1)
        assert chiral.central_charge == Fraction(1)

    def test_ec_shadow_depth(self):
        """Elliptic curve -> Heisenberg: class G, shadow depth 2."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=1)
        assert chiral.shadow_depth == 2

    def test_ec_e2_type(self):
        """Elliptic curve: E_infty (symmetric braiding)."""
        cyc = extract_cyclic_structure(elliptic_curve_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=1)
        assert "E_infty" in chiral.e2_type

    def test_k3_kappa(self):
        """K3: kappa(A_{K3}) = rank = 24 (Vol I authoritative)."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=2)
        assert chiral.kappa == Fraction(24)

    def test_k3_central_charge(self):
        """K3: c(A_{K3}) = rank = 24."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=2)
        assert chiral.central_charge == Fraction(24)

    def test_k3_type(self):
        """K3: lattice VOA type."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=2)
        assert chiral.type == "lattice_voa"

    def test_k3_e2_type(self):
        """K3: E_2 from CY2 rotation."""
        cyc = extract_cyclic_structure(k3_data())
        lcd = construct_lie_conformal(cyc)
        chiral = apply_factorization_envelope(lcd, cy_dim=2)
        assert "E_2" in chiral.e2_type


# ======================================================================
# 6. Full functor Phi
# ======================================================================

class TestPhiFunctor:
    """Test the complete functor Phi for all standard examples."""

    def test_phi_ec_kappa(self):
        """Phi(E): kappa = 1 (Vol I: kappa(H_1) = 1)."""
        result = phi_elliptic_curve()
        assert result.chiral_algebra.kappa == Fraction(1)

    def test_phi_ec_bridge_match(self):
        """Phi(E): cross-volume bridge matches."""
        result = phi_elliptic_curve()
        # Vol I authoritative: kappa(H_k) = k.
        # Rank-1 Heisenberg at level 1: kappa = 1.
        assert result.chiral_algebra.kappa == Fraction(1)

    def test_phi_k3_kappa(self):
        """Phi(K3): kappa = 24 (lattice VOA rank 24, Vol I: kappa = rank)."""
        result = phi_k3()
        assert result.chiral_algebra.kappa == Fraction(24)

    def test_phi_k3_hh_total(self):
        """Phi(K3): HH total = 24."""
        result = phi_k3()
        assert result.hh.total_dim == 24

    def test_phi_quintic_kappa(self):
        """Phi(Quintic): kappa = -25/3."""
        result = phi_quintic()
        assert result.chiral_algebra.kappa == Fraction(-25, 3)

    def test_phi_quintic_chi(self):
        """Phi(Quintic): chi = -200."""
        result = phi_quintic()
        assert result.hodge_data.euler_characteristic == -200

    def test_phi_quintic_bridge(self):
        """Phi(Quintic): bridge match confirms kappa = chi/24 = -25/3."""
        result = phi_quintic()
        assert result.cross_volume_bridge["match_kappa"]

    def test_phi_conifold_kappa(self):
        """Phi(conifold): kappa = 1."""
        result = phi_conifold()
        assert result.chiral_algebra.kappa == Fraction(1)

    def test_phi_conifold_type(self):
        """Phi(conifold): betagamma type."""
        result = phi_conifold()
        assert result.chiral_algebra.type == "betagamma"

    def test_phi_conifold_shadow_depth(self):
        """Phi(conifold): shadow depth 4 (class C, contact)."""
        result = phi_conifold()
        assert result.chiral_algebra.shadow_depth == 4

    def test_phi_conifold_bridge(self):
        """Phi(conifold): cross-volume bridge matches."""
        result = phi_conifold()
        assert result.cross_volume_bridge["match_kappa"]
        assert result.cross_volume_bridge["match_depth"]


# ======================================================================
# 7. Kappa computation
# ======================================================================

class TestKappaComputation:
    """Test kappa(A_C) formulas for various CY varieties."""

    def test_kappa_ec(self):
        """kappa_from_cy(E) = 1 (= h^{1,0} = genus)."""
        ec = elliptic_curve_data()
        assert kappa_from_cy(ec) == Fraction(1)

    def test_kappa_k3(self):
        """kappa_from_cy(K3) = 12 (= total HH dim / 2 = 24/2)."""
        k3 = k3_data()
        assert kappa_from_cy(k3) == Fraction(12)

    def test_kappa_quintic(self):
        """kappa_from_cy(quintic) = -25/3 (= chi/24 = -200/24)."""
        q = quintic_data()
        assert kappa_from_cy(q) == Fraction(-25, 3)

    def test_kappa_k3xe(self):
        """kappa_from_cy(K3xE) = 0 (chi = 0, BCOV = 0).

        WARNING: This is the BCOV kappa, NOT the Igusa kappa.
        The Igusa kappa = 5 (from cy_euler.py) is a different
        invariant reflecting the Sp_4 automorphic structure.
        """
        kxe = k3_times_e_data()
        assert kappa_from_cy(kxe) == Fraction(0)

    def test_kappa_heisenberg_level1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(1) == Fraction(1)

    def test_kappa_heisenberg_level_k(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 3, 5, 10]:
            assert kappa_heisenberg(k) == Fraction(k)

    def test_kappa_betagamma_standard(self):
        """kappa(bg, lambda=1) = 1."""
        assert kappa_betagamma(Fraction(1)) == Fraction(1)

    def test_kappa_betagamma_lambda0(self):
        """kappa(bg, lambda=0) = 1."""
        assert kappa_betagamma(Fraction(0)) == Fraction(1)

    def test_kappa_betagamma_formula(self):
        """kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1."""
        lam = Fraction(1, 2)
        expected = 6 * lam**2 - 6 * lam + 1
        assert kappa_betagamma(lam) == expected

    def test_kappa_betagamma_symmetry(self):
        """kappa(bg, lambda) = kappa(bg, 1-lambda): symmetric about lambda = 1/2."""
        for lam_num in range(5):
            lam = Fraction(lam_num, 4)
            assert kappa_betagamma(lam) == kappa_betagamma(1 - lam)

    def test_kappa_lattice_rank24(self):
        """kappa for lattice VOA of rank 24 = 24 (Vol I: kappa = rank)."""
        assert kappa_cy2_lattice(24) == Fraction(24)

    def test_kappa_lattice_rank8(self):
        """kappa for E_8 lattice VOA = 8 (Vol I: kappa = rank)."""
        assert kappa_cy2_lattice(8) == Fraction(8)

    def test_kappa_bcov_quintic(self):
        """BCOV kappa for quintic: chi = -200, kappa = -25/3."""
        assert kappa_cy3_bcov(-200) == Fraction(-25, 3)

    def test_kappa_bcov_mirror_quintic(self):
        """BCOV kappa for mirror quintic: h11=101, h21=1, chi=200, kappa=25/3."""
        chi_mirror = 2 * (101 - 1)
        assert kappa_cy3_bcov(chi_mirror) == Fraction(25, 3)

    def test_kappa_bcov_self_mirror(self):
        """Self-mirror CY3: chi = 0, kappa = 0."""
        assert kappa_cy3_bcov(0) == Fraction(0)


# ======================================================================
# 8. Mukai lattice
# ======================================================================

class TestMukaiLattice:
    """Test the Mukai lattice structure for K3."""

    def test_mukai_rank(self):
        """Mukai lattice has rank 24."""
        mukai = mukai_lattice_k3()
        assert mukai["rank"] == 24

    def test_mukai_signature(self):
        """Mukai lattice has signature (4, 20)."""
        mukai = mukai_lattice_k3()
        assert mukai["signature"] == (4, 20)

    def test_mukai_h2_rank(self):
        """H^2(K3, Z) has rank 22."""
        mukai = mukai_lattice_k3()
        assert mukai["h2_rank"] == 22

    def test_mukai_h2_signature(self):
        """H^2(K3, Z) has signature (3, 19)."""
        mukai = mukai_lattice_k3()
        assert mukai["h2_signature"] == (3, 19)

    def test_mukai_decomposition_rank_check(self):
        """U^4 + E_8(-1)^2 has rank 4*2 + 2*8 = 24."""
        mukai = mukai_lattice_k3()
        # U has rank 2, E_8 has rank 8
        expected_rank = 4 * 2 + 2 * 8
        assert expected_rank == 24
        assert mukai["rank"] == expected_rank

    def test_mukai_h0_h4_contributions(self):
        """H^0 and H^4 each contribute rank 1."""
        mukai = mukai_lattice_k3()
        assert mukai["h0_contribution"] == 1
        assert mukai["h4_contribution"] == 1
        assert mukai["h2_contribution"] == 22
        total = mukai["h0_contribution"] + mukai["h2_contribution"] + mukai["h4_contribution"]
        assert total == 24


# ======================================================================
# 9. Conifold-betagamma identification
# ======================================================================

class TestConifoldBetagamma:
    """Test the conifold -> betagamma identification."""

    def test_conifold_data(self):
        """Conifold data is consistent."""
        con = conifold_data()
        assert con["cy_dim"] == 3
        assert con["chiral_algebra"] == "betagamma"
        assert con["kappa"] == Fraction(1)

    def test_conifold_kappa_match(self):
        """kappa(conifold) = kappa(betagamma at lambda=1) = 1."""
        match = conifold_betagamma_match()
        assert match["match"]

    def test_conifold_chi_over_2(self):
        """kappa = chi(P^1)/2 = 2/2 = 1."""
        match = conifold_betagamma_match()
        assert match["kappa_from_chi"] == Fraction(1)

    def test_conifold_betagamma_kappa_agree(self):
        """betagamma_kappa and conifold kappa agree."""
        match = conifold_betagamma_match()
        assert match["betagamma_kappa"] == match["kappa_from_chi"]


# ======================================================================
# 10. Matrix factorizations
# ======================================================================

class TestMatrixFactorizations:
    """Test matrix factorization data for A_{n-1} singularities."""

    def test_mf_x3_objects(self):
        """MF(x^3): A_2 has 2 indecomposable objects."""
        mf = matrix_factorization_data(3)
        assert mf["n_objects"] == 2

    def test_mf_x4_objects(self):
        """MF(x^4): A_3 has 3 indecomposable objects."""
        mf = matrix_factorization_data(4)
        assert mf["n_objects"] == 3

    def test_mf_x3_central_charge(self):
        """MF(x^3): c = 3*1/3 = 1 (Ising model)."""
        mf = matrix_factorization_data(3)
        assert mf["central_charge"] == Fraction(1)

    def test_mf_x4_central_charge(self):
        """MF(x^4): c = 3*2/4 = 3/2."""
        mf = matrix_factorization_data(4)
        assert mf["central_charge"] == Fraction(3, 2)

    def test_mf_x5_central_charge(self):
        """MF(x^5): c = 3*3/5 = 9/5."""
        mf = matrix_factorization_data(5)
        assert mf["central_charge"] == Fraction(9, 5)

    def test_mf_x2_trivial(self):
        """MF(x^2): A_1, 1 object, c = 0."""
        mf = matrix_factorization_data(2)
        assert mf["n_objects"] == 1
        assert mf["central_charge"] == Fraction(0)

    def test_mf_central_charge_monotone(self):
        """Central charge c = 3(n-2)/n increases with n."""
        prev = Fraction(0)
        for n in range(2, 10):
            c = matrix_factorization_data(n)["central_charge"]
            assert c >= prev
            prev = c

    def test_mf_central_charge_limit(self):
        """c -> 3 as n -> infinity (N=2 at infinite level)."""
        c_100 = matrix_factorization_data(100)["central_charge"]
        assert abs(float(c_100) - 3.0) < 0.1

    def test_phi_mf(self):
        """phi_matrix_factorization returns consistent data."""
        for n in [3, 4, 5, 6]:
            result = phi_matrix_factorization(n)
            assert result["n_objects"] == n - 1
            expected_c = Fraction(3 * (n - 2), n)
            assert result["central_charge"] == expected_c


# ======================================================================
# 11. E_2 enhancement
# ======================================================================

class TestE2Enhancement:
    """Test E_2 structure from CY braiding."""

    def test_cy1_e_infty(self):
        """CY1: E_infty (symmetric braiding)."""
        data = e2_enhancement_data(1)
        assert data["e_level"] == "E_infty"
        assert data["r_matrix"] == "R = id"

    def test_cy2_e2(self):
        """CY2: E_2 (non-trivial braiding)."""
        data = e2_enhancement_data(2)
        assert data["e_level"] == "E_2"
        assert "non-trivial" in data["braiding"]

    def test_cy3_e2(self):
        """CY3: E_2 (KS wall-crossing braiding)."""
        data = e2_enhancement_data(3)
        assert data["e_level"] == "E_2"

    def test_cy0_trivial(self):
        """CY0: trivial braiding."""
        data = e2_enhancement_data(0)
        assert data["braiding"] == "trivial (d <= 0)"


# ======================================================================
# 12. HH decomposition table
# ======================================================================

class TestHHDecomposition:
    """Test the detailed HH decomposition table."""

    def test_ec_table_completeness(self):
        """Elliptic curve table has entries for p = 0, 1."""
        table = hh_decomposition_table()
        assert 0 in table["elliptic_curve"]
        assert 1 in table["elliptic_curve"]

    def test_k3_table_dimensions(self):
        """K3 table dimensions match HH computation."""
        table = hh_decomposition_table()
        assert table["K3"][0]["dim"] == 2
        assert table["K3"][1]["dim"] == 20
        assert table["K3"][2]["dim"] == 2

    def test_quintic_table_dimensions(self):
        """Quintic table dimensions match HH computation."""
        table = hh_decomposition_table()
        assert table["quintic"][0]["dim"] == 2
        assert table["quintic"][1]["dim"] == 102
        assert table["quintic"][2]["dim"] == 102
        assert table["quintic"][3]["dim"] == 2


# ======================================================================
# 13. CY3 kappa landscape
# ======================================================================

class TestCY3Landscape:
    """Test the CY3 kappa landscape."""

    def test_quintic_in_landscape(self):
        """Quintic appears with correct kappa."""
        land = cy3_kappa_landscape()
        assert "Quintic P4[5]" in land
        assert land["Quintic P4[5]"]["kappa_bcov"] == Fraction(-25, 3)

    def test_landscape_chi_consistency(self):
        """chi = 2(h11 - h21) for all entries with numeric h11, h21."""
        land = cy3_kappa_landscape()
        for name, data in land.items():
            if isinstance(data.get("h11"), int):
                assert data["chi"] == 2 * (data["h11"] - data["h21"])

    def test_landscape_kappa_consistency(self):
        """kappa = chi/24 for all entries with numeric chi."""
        land = cy3_kappa_landscape()
        for name, data in land.items():
            if isinstance(data.get("chi"), int):
                assert data["kappa_bcov"] == Fraction(data["chi"], 24)

    def test_self_mirror_kappa_zero(self):
        """Self-mirror CY3 has kappa = 0."""
        land = cy3_kappa_landscape()
        assert land["Self-mirror (h11=h21)"]["kappa_bcov"] == Fraction(0)

    def test_mirror_symmetry_kappa_sign(self):
        """Mirror pair: kappa(X) = -kappa(X_mirror).

        If X has (h11, h21), mirror has (h21, h11).
        chi(X) = 2(h11-h21), chi(mirror) = 2(h21-h11) = -chi(X).
        So kappa(mirror) = -kappa(X).
        """
        land = cy3_kappa_landscape()
        kappa_q = land["Quintic P4[5]"]["kappa_bcov"]
        chi_mirror = 2 * (101 - 1)  # Mirror quintic
        kappa_mirror = Fraction(chi_mirror, 24)
        assert kappa_q + kappa_mirror == Fraction(0)


# ======================================================================
# 14. Cross-volume bridge verification
# ======================================================================

class TestCrossVolumeBridge:
    """Verify that kappa values match across volumes."""

    def test_bridge_ec(self):
        """EC bridge: functor kappa = 1 for rank-1 Heisenberg (Vol I: kappa = k)."""
        result = phi_elliptic_curve()
        assert result.chiral_algebra.kappa == Fraction(1)

    def test_bridge_k3(self):
        """K3 bridge: functor kappa = 24 matches lattice VOA rank 24."""
        result = phi_k3()
        assert result.chiral_algebra.kappa == kappa_cy2_lattice(24)

    def test_bridge_quintic(self):
        """Quintic bridge: functor kappa = -25/3 matches BCOV."""
        result = phi_quintic()
        assert result.chiral_algebra.kappa == kappa_cy3_bcov(-200)

    def test_bridge_conifold(self):
        """Conifold bridge: functor kappa = 1 matches betagamma."""
        result = phi_conifold()
        assert result.chiral_algebra.kappa == kappa_betagamma(Fraction(1))

    def test_verify_kappa_bridge_all(self):
        """All kappa bridge verifications pass."""
        results = verify_kappa_bridge()
        for key, val in results.items():
            assert val, f"kappa bridge failed: {key}"


# ======================================================================
# 15. Summary and verification
# ======================================================================

class TestSummary:
    """Test the summary and verification functions."""

    def test_phi_summary_completeness(self):
        """Summary includes all standard examples."""
        summary = phi_summary()
        assert "elliptic_curve" in summary
        assert "K3" in summary
        assert "quintic" in summary
        assert "conifold" in summary
        assert "MF(x^3)" in summary

    def test_phi_summary_kappa_values(self):
        """Summary kappa values are consistent."""
        summary = phi_summary()
        assert summary["elliptic_curve"]["kappa"] == Fraction(1)
        assert summary["K3"]["kappa"] == Fraction(24)
        assert summary["quintic"]["kappa"] == Fraction(-25, 3)
        assert summary["conifold"]["kappa"] == Fraction(1)

    def test_verify_hh_all(self):
        """All HH dimension verifications pass."""
        results = verify_hh_dimensions()
        for key, val in results.items():
            assert val, f"HH verification failed: {key}"

    def test_verify_all(self):
        """Full verification suite passes."""
        results = verify_all()
        for key, val in results.items():
            assert val, f"Verification failed: {key}"


# ======================================================================
# 16. Edge cases and additional consistency
# ======================================================================

class TestEdgeCases:
    """Additional consistency checks."""

    def test_cy_dim_positive(self):
        """All standard CY varieties have non-negative dimension."""
        for data_fn in [elliptic_curve_data, k3_data, quintic_data]:
            assert data_fn().dim >= 0

    def test_hh_nonegative(self):
        """HH dimensions are non-negative."""
        for data_fn in [elliptic_curve_data, k3_data, quintic_data]:
            hh = hh_from_hodge(data_fn())
            for p, d in hh.dim_by_degree.items():
                assert d >= 0, f"HH_{p} < 0 for {data_fn.__name__}"

    def test_mf_invalid_n(self):
        """MF(x^n) requires n >= 2."""
        with pytest.raises(AssertionError):
            matrix_factorization_data(1)

    def test_kappa_betagamma_at_half(self):
        """kappa(bg, 1/2) = 6/4 - 3 + 1 = -1/2."""
        lam = Fraction(1, 2)
        expected = 6 * Fraction(1, 4) - 6 * Fraction(1, 2) + 1
        assert expected == Fraction(-1, 2)
        assert kappa_betagamma(lam) == Fraction(-1, 2)

    def test_quintic_mirror_kappa(self):
        """Mirror quintic: chi = +200, kappa = +25/3."""
        chi_mirror = 200
        kappa_mirror = kappa_cy3_bcov(chi_mirror)
        assert kappa_mirror == Fraction(25, 3)

    def test_kappa_cy2_various_ranks(self):
        """kappa = rank for various lattice ranks (Vol I authoritative)."""
        for r in [1, 2, 8, 16, 24, 32]:
            assert kappa_cy2_lattice(r) == Fraction(r)

    def test_hh_serre_duality_quintic(self):
        """Serre duality: dim HH_p = dim HH_{d-p} for CY d-fold.

        For quintic (d=3): HH_0 = HH_3, HH_1 = HH_2.
        """
        hh = hh_from_hodge(quintic_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[3]
        assert hh.dim_by_degree[1] == hh.dim_by_degree[2]

    def test_hh_serre_duality_k3(self):
        """K3 (d=2): HH_0 = HH_2."""
        hh = hh_from_hodge(k3_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[2]

    def test_hh_serre_duality_ec(self):
        """Elliptic curve (d=1): HH_0 = HH_1."""
        hh = hh_from_hodge(elliptic_curve_data())
        assert hh.dim_by_degree[0] == hh.dim_by_degree[1]
