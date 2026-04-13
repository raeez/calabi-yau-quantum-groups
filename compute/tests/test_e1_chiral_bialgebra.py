"""Tests for E_1-chiral bialgebra axioms on W_{1+infinity}.

Verifies that W_{1+infinity} (= affine Yangian Y(gl_hat_1)) satisfies
the five axioms of an E_1-chiral bialgebra:

  1. E_1-ALGEBRA: ordered OPE product, Virasoro Jacobi identity, nonzero
     commutator (ordering asymmetry = R-matrix content).

  2. E_1-COALGEBRA: deconcatenation coproduct on B^{ord}, bar differential
     from OPE, MacMahon grading, weight conservation.

  3. BIALGEBRA COMPATIBILITY: Delta_z is an algebra homomorphism.
     Virasoro c_eff = 2 + 2*(Psi-1)^2, mixed [Delta(T), Delta(J)] factor Psi,
     Heisenberg doubled level 2*Psi.

  4. COASSOCIATIVITY: (Delta_w x id) o Delta_{z+w} = (id x Delta_z) o Delta_w
     at spin 2 (Miura triple product) and spin 1 (primitive).

  5. AVERAGING MAP: Delta_z vs Delta_z^{op} detects R-matrix (nontrivial at
     z != 0, trivial at z=0). Averaging kills R-matrix data. kappa_ch = Psi.

VERIFIED sources:
[DC] Direct computation on truncated Fock space
[TM] Transfer matrix multiplicative coproduct (Drinfeld 1987, Tsymbaliuk 2014)
[YA] Yangian axiomatics
[E1] E_1-chiral theory (Vol III, Chapter e1_chiral_algebras)
"""

import pytest

from compute.lib.e1_chiral_bialgebra_engine import (
    E1AlgebraVerifier,
    E1CoalgebraVerifier,
    BialgebraCompatibilityVerifier,
    CoassociativityVerifier,
    AveragingMapVerifier,
)


# ===================================================================
# AXIOM 1: E_1-algebra structure
# ===================================================================

class TestE1AlgebraAssociativity:
    """Virasoro Jacobi identity (E_1-algebra is strictly associative)."""

    def test_jacobi_Psi1(self):
        # VERIFIED: [DC] Jacobi identity on Sugawara Virasoro at Psi=1.
        v = E1AlgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_ordered_product_associativity()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_jacobi_Psi2(self):
        # VERIFIED: [DC] Jacobi identity at Psi=2.
        v = E1AlgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_ordered_product_associativity()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_jacobi_parametric(self, Psi):
        # VERIFIED: [DC] Jacobi identity across Psi range.
        v = E1AlgebraVerifier(Psi=Psi, N_max=5)
        r = v.verify_ordered_product_associativity()
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"


class TestE1AlgebraRMatrix:
    """R-matrix from Virasoro commutator (c=1 Sugawara)."""

    def test_virasoro_commutator_Psi1(self):
        # VERIFIED: [DC] [T_m, T_n] = Virasoro with c=1.
        v = E1AlgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_r_matrix_from_commutator()
        assert r["ok"], f"max error {r['max_error']:.2e}"
        assert abs(r["c"] - 1.0) < 1e-12

    def test_virasoro_commutator_Psi2(self):
        # VERIFIED: [DC] Same c=1 at Psi=2 (Sugawara c is Psi-independent).
        v = E1AlgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_r_matrix_from_commutator()
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestE1AlgebraOrdering:
    """E_1 ordering asymmetry: T_m T_n != T_n T_m for m != n."""

    def test_ordering_Psi1(self):
        # VERIFIED: [E1] Nonzero commutator confirms E_1 non-commutativity.
        v = E1AlgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_ordering_asymmetry()
        assert r["ok"], f"asymmetry {r['max_asymmetry']:.4f} too small"

    def test_ordering_Psi2(self):
        # VERIFIED: [E1] Same at Psi=2.
        v = E1AlgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_ordering_asymmetry()
        assert r["ok"], f"asymmetry {r['max_asymmetry']:.4f} too small"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_ordering_parametric(self, Psi):
        # VERIFIED: [E1] Ordering asymmetry is universal.
        v = E1AlgebraVerifier(Psi=Psi, N_max=5)
        r = v.verify_ordering_asymmetry()
        assert r["ok"], f"Psi={Psi}: asymmetry {r['max_asymmetry']:.4f}"


# ===================================================================
# AXIOM 2: E_1-coalgebra structure
# ===================================================================

class TestE1CoalgebraDeconcatenation:
    """Primitive coproduct = deconcatenation at degree 1."""

    def test_deconcatenation_Psi1(self):
        # VERIFIED: [DC] Delta(J) = J^L + J^R (primitive, 2 terms = n+1 at n=1).
        v = E1CoalgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_deconcatenation_vs_coshuffle_spin1()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_deconcatenation_Psi2(self):
        # VERIFIED: [DC] Same at Psi=2.
        v = E1CoalgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_deconcatenation_vs_coshuffle_spin1()
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestE1CoalgebraBarDifferential:
    """Bar differential encodes Virasoro OPE."""

    def test_bar_differential_Psi1(self):
        # VERIFIED: [DC] d_B[T_m|T_n] = [T_m, T_n] = Virasoro comm.
        v = E1CoalgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_bar_differential_from_ope()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_bar_differential_Psi2(self):
        # VERIFIED: [DC] Same at Psi=2.
        v = E1CoalgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_bar_differential_from_ope()
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestE1CoalgebraMacMahon:
    """MacMahon grading: Fock space dimension = partition count."""

    def test_macmahon_Psi1(self):
        # VERIFIED: [DC] Level counts match p(n) = {1,1,2,3,5,7,...}.
        v = E1CoalgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_macmahon_grading()
        assert r["ok"]
        assert r["grading_matches"]
        assert r["vacuum_weight_zero"]

    def test_macmahon_Psi2(self):
        # VERIFIED: [DC] MacMahon grading is Psi-independent (same Fock space).
        v = E1CoalgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_macmahon_grading()
        assert r["ok"]

    def test_partition_counts_explicit(self):
        """Explicit check: p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        v = E1CoalgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_macmahon_grading()
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for n, count in expected.items():
            assert r["level_counts"][n] == count, (
                f"p({n}) = {r['level_counts'][n]}, expected {count}"
            )


class TestE1CoalgebraWeightConservation:
    """[L_0^{tot}, Delta(T_n)] = -n * Delta(T_n)."""

    def test_weight_conservation_Psi1(self):
        # VERIFIED: [DC] Total conformal weight preserved by coproduct.
        v = E1CoalgebraVerifier(Psi=1.0, N_max=5)
        r = v.verify_coproduct_weight_conservation()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_weight_conservation_Psi2(self):
        # VERIFIED: [DC] Same at Psi=2.
        v = E1CoalgebraVerifier(Psi=2.0, N_max=5)
        r = v.verify_coproduct_weight_conservation()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_weight_conservation_parametric(self, Psi):
        # VERIFIED: [DC] Weight conservation across Psi range.
        v = E1CoalgebraVerifier(Psi=Psi, N_max=5)
        r = v.verify_coproduct_weight_conservation()
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"


# ===================================================================
# AXIOM 3: Bialgebra compatibility
# ===================================================================

class TestBialgebraVirasoro:
    """[Delta(T_m), Delta(T_n)] = Virasoro with c_eff = 2 + 2*(Psi-1)^2."""

    def test_virasoro_hom_Psi1(self):
        # VERIFIED: [DC]+[TM] c_eff = 2 at Psi=1 (free boson, no cross-term).
        v = BialgebraCompatibilityVerifier(Psi=1.0, N_max=5)
        r = v.verify_homomorphism_virasoro()
        assert r["ok"], f"max error {r['max_error']:.2e}"
        assert abs(r["c_eff"] - 2.0) < 1e-12

    def test_virasoro_hom_Psi2(self):
        # VERIFIED: [DC]+[TM] c_eff = 4 at Psi=2.
        v = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        r = v.verify_homomorphism_virasoro()
        assert r["ok"], f"max error {r['max_error']:.2e}"
        assert abs(r["c_eff"] - 4.0) < 1e-12

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_virasoro_hom_parametric(self, Psi):
        # VERIFIED: [DC] c_eff formula across Psi range.
        v = BialgebraCompatibilityVerifier(Psi=Psi, N_max=5)
        r = v.verify_homomorphism_virasoro()
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"
        expected_c = 2.0 + 2.0 * (Psi - 1.0) ** 2
        assert abs(r["c_eff"] - expected_c) < 1e-10, (
            f"Psi={Psi}: c_eff={r['c_eff']}, expected {expected_c}"
        )

    def test_virasoro_hom_z_complex(self):
        # VERIFIED: [DC]+[SY] Holds at complex z.
        v = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        r = v.verify_homomorphism_virasoro(z=0.7 + 0.4j)
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestBialgebraMixed:
    """[Delta(T_n), Delta(J_m)] = -Psi*m * Delta(J_{n+m})."""

    def test_mixed_hom_Psi1(self):
        # VERIFIED: [DC] Factor Psi=1 at free boson.
        v = BialgebraCompatibilityVerifier(Psi=1.0, N_max=5)
        r = v.verify_homomorphism_mixed()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_mixed_hom_Psi2(self):
        # VERIFIED: [DC] Factor Psi=2.
        v = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        r = v.verify_homomorphism_mixed()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_mixed_hom_parametric(self, Psi):
        # VERIFIED: [DC] Factor Psi across range.
        v = BialgebraCompatibilityVerifier(Psi=Psi, N_max=5)
        r = v.verify_homomorphism_mixed()
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"


class TestBialgebraHeisenberg:
    """[Delta(J_m), Delta(J_n)] = 2*Psi*m * delta (doubled level)."""

    def test_heisenberg_hom_Psi1(self):
        # VERIFIED: [DC] Effective level 2*Psi=2 at Psi=1.
        v = BialgebraCompatibilityVerifier(Psi=1.0, N_max=5)
        r = v.verify_homomorphism_heisenberg()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_heisenberg_hom_Psi2(self):
        # VERIFIED: [DC] Effective level 2*Psi=4 at Psi=2.
        v = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        r = v.verify_homomorphism_heisenberg()
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ===================================================================
# AXIOM 4: Coassociativity
# ===================================================================

class TestCoassociativitySpin2:
    """(Delta_w x id) o Delta_{z+w} = (id x Delta_z) o Delta_w at spin 2."""

    def test_coassoc_Psi2(self):
        # VERIFIED: [YA] Yangian coassociativity with spectral shift.
        v = CoassociativityVerifier(Psi=2.0, N_max=4)
        r = v.verify_coassociativity_spin2()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_coassoc_Psi1(self):
        # VERIFIED: [YA] Free boson: primitive, trivially coassociative.
        v = CoassociativityVerifier(Psi=1.0, N_max=4)
        r = v.verify_coassociativity_spin2()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_coassoc_parametric(self, Psi):
        # VERIFIED: [YA] Coassociativity across Psi range.
        v = CoassociativityVerifier(Psi=Psi, N_max=3)
        r = v.verify_coassociativity_spin2()
        assert r["ok"], f"Psi={Psi}: max error {r['max_error']:.2e}"

    def test_coassoc_real_z(self):
        # VERIFIED: [YA] Coassociativity at real spectral parameters.
        v = CoassociativityVerifier(Psi=2.0, N_max=4)
        r = v.verify_coassociativity_spin2(z=0.7, w=1.3)
        assert r["ok"], f"max error {r['max_error']:.2e}"


class TestCoassociativitySpin1:
    """Coassociativity for J (primitive, trivially satisfied)."""

    def test_coassoc_J_Psi2(self):
        # VERIFIED: [DC] J is primitive: coassociativity is additive.
        v = CoassociativityVerifier(Psi=2.0, N_max=4)
        r = v.verify_coassociativity_J()
        assert r["ok"], f"max error {r['max_error']:.2e}"

    def test_coassoc_J_Psi1(self):
        # VERIFIED: [DC] Same at Psi=1.
        v = CoassociativityVerifier(Psi=1.0, N_max=4)
        r = v.verify_coassociativity_J()
        assert r["ok"], f"max error {r['max_error']:.2e}"


# ===================================================================
# AXIOM 5: Averaging map kills Hopf data
# ===================================================================

class TestRMatrixFromOppositeCoproduct:
    """Delta_z != Delta_z^{op} for z != 0 (R-matrix nontrivial)."""

    def test_r_matrix_Psi2(self):
        # VERIFIED: [DC] Cocommutative at z=0, nontrivial R at z!=0.
        v = AveragingMapVerifier(Psi=2.0, N_max=5)
        r = v.verify_r_matrix_from_opposite_coproduct()
        assert r["ok"]
        assert r["cocommutative_at_z0"]
        assert r["r_matrix_nontrivial"]

    def test_r_matrix_Psi1(self):
        # VERIFIED: [DC] Free boson: still has R-matrix from z-shift.
        v = AveragingMapVerifier(Psi=1.0, N_max=5)
        r = v.verify_r_matrix_from_opposite_coproduct()
        assert r["ok"]
        assert r["cocommutative_at_z0"]
        assert r["r_matrix_nontrivial"]

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_r_matrix_parametric(self, Psi):
        # VERIFIED: [DC] R-matrix structure across Psi range.
        v = AveragingMapVerifier(Psi=Psi, N_max=5)
        r = v.verify_r_matrix_from_opposite_coproduct()
        assert r["ok"], (
            f"Psi={Psi}: z0_diff={r['max_diff_z0']:.2e}, "
            f"z_diff={r['max_diff_z_nonzero']:.4f}"
        )


class TestAveragingKillsRMatrix:
    """Averaged coproduct vacuum expectation is z-independent."""

    def test_av_kills_r_Psi2(self):
        # VERIFIED: [DC] av(Delta_z) vacuum expectation is z-independent.
        v = AveragingMapVerifier(Psi=2.0, N_max=5)
        r = v.verify_averaging_kills_r_matrix()
        assert r["ok"], f"max spread {r['max_spread']:.2e}"

    def test_av_kills_r_Psi1(self):
        # VERIFIED: [DC] Same at Psi=1.
        v = AveragingMapVerifier(Psi=1.0, N_max=5)
        r = v.verify_averaging_kills_r_matrix()
        assert r["ok"], f"max spread {r['max_spread']:.2e}"

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.7])
    def test_av_kills_r_parametric(self, Psi):
        # VERIFIED: [DC] Averaging kills R across Psi range.
        v = AveragingMapVerifier(Psi=Psi, N_max=5)
        r = v.verify_averaging_kills_r_matrix()
        assert r["ok"], f"Psi={Psi}: max spread {r['max_spread']:.2e}"


class TestKappaCh:
    """kappa_ch = Psi: the collision residue of r(z) = Psi*Omega/z."""

    def test_kappa_ch_Psi1(self):
        # VERIFIED: [DC] kappa_ch = 1 at free boson.
        v = AveragingMapVerifier(Psi=1.0, N_max=5)
        r = v.verify_kappa_ch_from_averaging()
        assert r["ok"]
        assert abs(r["kappa_ch"] - 1.0) < 1e-12

    def test_kappa_ch_Psi2(self):
        # VERIFIED: [DC] kappa_ch = 2 at Psi=2.
        v = AveragingMapVerifier(Psi=2.0, N_max=5)
        r = v.verify_kappa_ch_from_averaging()
        assert r["ok"]
        assert abs(r["kappa_ch"] - 2.0) < 1e-12

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0, 3.7])
    def test_kappa_ch_equals_Psi(self, Psi):
        # VERIFIED: [DC] kappa_ch = Psi universally.
        v = AveragingMapVerifier(Psi=Psi, N_max=5)
        r = v.verify_kappa_ch_from_averaging()
        assert r["ok"]
        assert abs(r["kappa_ch"] - Psi) < 1e-12, (
            f"kappa_ch = {r['kappa_ch']}, expected {Psi}"
        )


class TestAsymmetryGrowth:
    """||Delta_z - Delta_z^{op}|| grows linearly with |z|."""

    def test_asym_growth_Psi2(self):
        # VERIFIED: [DC] Linear growth at Psi=2.
        v = AveragingMapVerifier(Psi=2.0, N_max=5)
        r = v.verify_opposite_coproduct_asymmetry_grows()
        assert r["ok"], (
            f"monotone={r['monotone']}, ratio={r['linear_scaling_ratio']:.2f}"
        )

    def test_asym_growth_Psi1(self):
        # VERIFIED: [DC] Linear growth at Psi=1 (from z-shift alone).
        v = AveragingMapVerifier(Psi=1.0, N_max=5)
        r = v.verify_opposite_coproduct_asymmetry_grows()
        assert r["ok"], (
            f"monotone={r['monotone']}, ratio={r['linear_scaling_ratio']:.2f}"
        )

    @pytest.mark.parametrize("Psi", [0.5, 1.0, 2.0, 3.0])
    def test_asym_growth_parametric(self, Psi):
        # VERIFIED: [DC] Linear growth across Psi range.
        v = AveragingMapVerifier(Psi=Psi, N_max=5)
        r = v.verify_opposite_coproduct_asymmetry_grows()
        assert r["ok"], (
            f"Psi={Psi}: monotone={r['monotone']}, "
            f"ratio={r['linear_scaling_ratio']:.2f}"
        )


# ===================================================================
# Cross-axiom structural tests
# ===================================================================

class TestCrossAxiomStructure:
    """Tests that connect multiple axioms."""

    def test_psi1_free_boson_primitive(self):
        """At Psi=1 (free boson), the coproduct is primitive (alpha=0).

        This means: Delta(T) = T^L + T^R (no cross-term), c_eff = 2 = 1+1,
        and the E_1 bialgebra degenerates to a direct sum. The R-matrix
        from Delta vs Delta^{op} comes only from the z-shift, not from
        interaction terms.
        """
        # Bialgebra: c_eff = 2 (two decoupled copies)
        bv = BialgebraCompatibilityVerifier(Psi=1.0, N_max=5)
        r = bv.verify_homomorphism_virasoro()
        assert r["ok"]
        assert abs(r["c_eff"] - 2.0) < 1e-10

        # Averaging: kappa_ch = 1
        av = AveragingMapVerifier(Psi=1.0, N_max=5)
        r = av.verify_kappa_ch_from_averaging()
        assert abs(r["kappa_ch"] - 1.0) < 1e-12

    def test_c_eff_quadratic_in_psi(self):
        """c_eff = 2 + 2*(Psi-1)^2 across several Psi values.

        This is the spin-2 manifestation of the bialgebra compatibility:
        the interaction between E_1-ordered product and deconcatenation
        coproduct produces a Psi-dependent central charge.
        """
        for Psi in [0.5, 1.0, 2.0, 3.0]:
            bv = BialgebraCompatibilityVerifier(Psi=Psi, N_max=5)
            r = bv.verify_homomorphism_virasoro()
            expected = 2.0 + 2.0 * (Psi - 1.0) ** 2
            assert abs(r["c_eff"] - expected) < 1e-8, (
                f"Psi={Psi}: c_eff={r['c_eff']}, expected={expected}"
            )

    def test_coassociativity_implies_triple_miura(self):
        """Coassociativity at two different spectral parameter pairs.

        Both (z,w) and (z',w') give the same Miura triple product,
        verifying that the bialgebra structure is coherent.
        """
        for z, w in [(0.3 + 0.2j, 0.5 - 0.1j), (0.7, 1.3)]:
            cv = CoassociativityVerifier(Psi=2.0, N_max=4)
            r = cv.verify_coassociativity_spin2(z=z, w=w)
            assert r["ok"], f"z={z}, w={w}: max error {r['max_error']:.2e}"

    def test_full_axiom_suite_Psi2(self):
        """All five axioms at Psi=2 (the standard non-degenerate case)."""
        e1a = E1AlgebraVerifier(Psi=2.0, N_max=5)
        assert e1a.verify_ordered_product_associativity()["ok"]
        assert e1a.verify_r_matrix_from_commutator()["ok"]
        assert e1a.verify_ordering_asymmetry()["ok"]

        e1c = E1CoalgebraVerifier(Psi=2.0, N_max=5)
        assert e1c.verify_deconcatenation_vs_coshuffle_spin1()["ok"]
        assert e1c.verify_bar_differential_from_ope()["ok"]
        assert e1c.verify_macmahon_grading()["ok"]
        assert e1c.verify_coproduct_weight_conservation()["ok"]

        bv = BialgebraCompatibilityVerifier(Psi=2.0, N_max=5)
        assert bv.verify_homomorphism_virasoro()["ok"]
        assert bv.verify_homomorphism_mixed()["ok"]
        assert bv.verify_homomorphism_heisenberg()["ok"]

        cv = CoassociativityVerifier(Psi=2.0, N_max=4)
        assert cv.verify_coassociativity_spin2()["ok"]
        assert cv.verify_coassociativity_J()["ok"]

        av = AveragingMapVerifier(Psi=2.0, N_max=5)
        assert av.verify_r_matrix_from_opposite_coproduct()["ok"]
        assert av.verify_averaging_kills_r_matrix()["ok"]
        assert av.verify_kappa_ch_from_averaging()["ok"]
        assert av.verify_opposite_coproduct_asymmetry_grows()["ok"]
