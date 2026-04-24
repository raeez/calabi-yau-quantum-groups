"""Tests for kappa_spectrum_reconciliation: the four-valued kappa-spectrum
for K3 and K3 x E.

Ground truth:
  chapters/examples/k3_times_e.tex (Proposition prop:kappa-spectrum-reconciliation)
  chapters/connections/modular_koszul_bridge.tex (Definition def:cy-categorical-kappa)
  chapters/theory/cy_to_chiral.tex (Proposition prop:cy-kappa-d2, Proposition prop:categorical-euler)
  CLAUDE.md (AP113: bare kappa FORBIDDEN; kappa-spectrum table)

AP113: every kappa value MUST carry a subscript {ch, cat, BKM, fiber}.
"""

from fractions import Fraction

import pytest

from compute.lib.kappa_spectrum_reconciliation import (
    HodgeData,
    elliptic_curve,
    k3_surface,
    k3_times_e,
    enriques_surface,
    quintic_threefold,
    abelian_surface,
    kappa_cat,
    kappa_ch,
    kappa_ch_compact_hodge,
    kappa_ch_rational,
    kappa_BKM,
    kappa_fiber,
    compute_spectrum,
    verify_kappa_cat_is_chi_O,
    verify_kappa_ch_equals_kappa_cat_at_d2,
    verify_kappa_ch_additivity,
    verify_chi_O_multiplicativity,
    verify_BKM_decomposition_k3e,
    borcherds_weight_from_h11,
    verify_chi_top_over_24_failure,
    k3_spectrum,
    k3e_spectrum,
    enriques_times_e_spectrum,
    physical_meaning,
    verify_all,
)


# ======================================================================
# 1. Hodge data
# ======================================================================

class TestHodgeData:
    """Verify Hodge numbers and chi(O_X) for standard CY manifolds."""

    def test_elliptic_curve_chi_O(self):
        """chi(O_E) = 1 - 1 = 0."""
        e = elliptic_curve()
        # VERIFIED [DC] chi(O_E) = 0 [LC] definition
        assert e.chi_O() == 0

    def test_k3_chi_O(self):
        """chi(O_{K3}) = 1 - 0 + 1 = 2."""
        k3 = k3_surface()
        # VERIFIED [DC] chi(O_{K3}) = 2 [LC] Hodge diamond
        assert k3.chi_O() == 2

    def test_k3xe_chi_O(self):
        """chi(O_{K3 x E}) = 1 - 1 + 1 - 1 = 0."""
        k3e = k3_times_e()
        # VERIFIED [DC] chi(O_{K3xE}) = 0 [LC] Kunneth
        assert k3e.chi_O() == 0

    def test_k3xe_h0q_kunneth(self):
        """h^{0,q}(K3 x E) by Kunneth: (1, 1, 1, 1)."""
        k3e = k3_times_e()
        # VERIFIED [DC] h^{0,q} Kunneth formula [LC] product formula
        assert k3e.h0q == (1, 1, 1, 1)

    def test_enriques_chi_O(self):
        """chi(O_{Enr}) = 1 - 0 + 0 = 1."""
        enr = enriques_surface()
        # VERIFIED [DC] chi(O_Enr) = 1 [LC] Hodge diamond
        assert enr.chi_O() == 1

    def test_quintic_chi_O(self):
        """chi(O_Quintic) = 1 - 0 + 0 - 1 = 0 (wait, h^{0,3}=1 for CY3).

        For the quintic: h^{0,0}=1, h^{0,1}=0, h^{0,2}=0, h^{0,3}=1.
        chi(O) = 1 - 0 + 0 - 1 = 0.
        """
        q = quintic_threefold()
        # VERIFIED [DC] chi(O_Quintic) = 0 [LC] CY3 Hodge constraint
        assert q.chi_O() == 0

    def test_abelian_surface_chi_O(self):
        """chi(O_{T^4}) = 1 - 2 + 1 = 0."""
        t4 = abelian_surface()
        # VERIFIED [DC] chi(O_{T^4}) = 0 [LC] abelian variety
        assert t4.chi_O() == 0

    def test_k3_chi_top(self):
        """chi_top(K3) = 24."""
        k3 = k3_surface()
        # VERIFIED [DC] chi_top(K3) = 24 [LC] boundary case
        assert k3.chi_top == 24

    def test_k3xe_chi_top(self):
        """chi_top(K3 x E) = chi_top(K3) * chi_top(E) = 24 * 0 = 0."""
        k3e = k3_times_e()
        # VERIFIED [DC] chi_top(K3xE) = 0 [LC] product formula
        assert k3e.chi_top == 0


# ======================================================================
# 2. kappa_cat = chi(O_X)
# ======================================================================

class TestKappaCat:
    """kappa_cat(C) := chi^{CY}(C) = chi(O_X)."""

    def test_kappa_cat_E(self):
        """kappa_cat(E) = chi(O_E) = 0."""
        e = elliptic_curve()
        # VERIFIED [DC] kappa_cat = chi(O_X) [LC] definition
        assert kappa_cat(e) == 0

    def test_kappa_cat_K3(self):
        """kappa_cat(K3) = chi(O_{K3}) = 2."""
        k3 = k3_surface()
        # VERIFIED [DC] kappa_cat(K3) = 2 [LC] Hodge diamond
        assert kappa_cat(k3) == 2

    def test_kappa_cat_K3xE(self):
        """kappa_cat(K3 x E) = chi(O_{K3xE}) = 0. NOT 2.

        The value 2 in the CLAUDE.md table refers to kappa_cat(K3),
        the fiber value, not kappa_cat(K3 x E) = chi(O_{K3xE}) = 0.
        """
        k3e = k3_times_e()
        # VERIFIED [DC] kappa_cat(K3xE) = 0 [LC] Kunneth
        assert kappa_cat(k3e) == 0

    def test_kappa_cat_Enriques(self):
        """kappa_cat(Enr) = chi(O_{Enr}) = 1."""
        enr = enriques_surface()
        # VERIFIED [DC] kappa_cat(Enr) = 1 [LC] Hodge diamond
        assert kappa_cat(enr) == 1

    def test_kappa_cat_quintic(self):
        """kappa_cat(Quintic) = chi(O_Quintic) = 0."""
        q = quintic_threefold()
        # VERIFIED [DC] kappa_cat(Quintic) = 0 [LC] CY3 constraint
        assert kappa_cat(q) == 0

    def test_kappa_cat_is_chi_O_all(self):
        """kappa_cat = chi(O_X) for all standard manifolds."""
        for X in [elliptic_curve(), k3_surface(), k3_times_e(),
                  enriques_surface(), quintic_threefold(), abelian_surface()]:
            # VERIFIED [DC] universality of kappa_cat = chi(O) [LC] definition
            assert verify_kappa_cat_is_chi_O(X), f"Failed for {X.name}"

    def test_chi_O_multiplicativity(self):
        """chi(O_{K3 x E}) = chi(O_{K3}) * chi(O_E) = 2 * 0 = 0."""
        k3 = k3_surface()
        e = elliptic_curve()
        k3e = k3_times_e()
        # VERIFIED [DC] Kunneth multiplicativity [LC] product formula
        assert verify_chi_O_multiplicativity(k3, e, k3e)
        assert k3e.chi_O() == k3.chi_O() * e.chi_O()


# ======================================================================
# 3. kappa_ch (chiral modular characteristic)
# ======================================================================

class TestKappaCh:
    """kappa_ch: the genus-1 bar-complex coefficient of A = Phi(C)."""

    def test_kappa_ch_E(self):
        """kappa_ch(E) = 1 = dim_C(E). Note: != chi(O_E) = 0."""
        e = elliptic_curve()
        # VERIFIED [DC] kappa_ch(E) = 1 [LC] chiral de Rham
        assert kappa_ch(e) == 1
        # Critical: kappa_ch(E) != kappa_cat(E)
        assert kappa_ch(e) != kappa_cat(e)

    def test_kappa_ch_K3(self):
        """kappa_ch(K3) = 2 = chi(O_{K3}). At d=2, kappa_ch = kappa_cat."""
        k3 = k3_surface()
        # VERIFIED [DC] kappa_ch(K3) = 2 [LC] five independent paths
        assert kappa_ch(k3) == 2
        # At d=2, kappa_ch = kappa_cat (PROVED)
        assert kappa_ch(k3) == kappa_cat(k3)

    def test_kappa_ch_K3xE(self):
        """K3 x E has compact value 0 and Heisenberg-specialisation value 3."""
        k3e = k3_times_e()
        # VERIFIED [DC] compact Hodge/PhiFA supertrace [LC] Kunneth
        assert kappa_ch_compact_hodge(k3e) == 0
        # VERIFIED [DC] kappa_ch^{Heis}(K3xE) = 3 [LC] specialisation additivity
        assert kappa_ch(k3e) == 3

    def test_kappa_ch_additivity(self):
        """kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E)."""
        k3 = k3_surface()
        e = elliptic_curve()
        k3e = k3_times_e()
        # VERIFIED [DC] chiral characteristic additivity [LC] K3 x E
        assert verify_kappa_ch_additivity(k3, e, k3e)
        assert kappa_ch(k3e) == kappa_ch(k3) + kappa_ch(e)

    def test_kappa_ch_equals_kappa_cat_at_d2(self):
        """At d=2: kappa_ch = kappa_cat. Proposition prop:kappa-cat-chi-cy."""
        k3 = k3_surface()
        # VERIFIED [DC] kappa_ch = kappa_cat at d=2 [LC] CY-A_2 proved
        assert verify_kappa_ch_equals_kappa_cat_at_d2(k3)

    def test_kappa_ch_neq_kappa_cat_at_d1(self):
        """At d=1: kappa_ch(E) = 1 != kappa_cat(E) = 0."""
        e = elliptic_curve()
        # VERIFIED [DC] kappa_ch != kappa_cat at d=1 [LC] explicit
        assert kappa_ch(e) != kappa_cat(e)

    def test_kappa_ch_Enriques(self):
        """kappa_ch(Enr) = 1 = chi(O_Enr). Halving of K3 value."""
        enr = enriques_surface()
        # VERIFIED [DC] kappa_ch(Enr) = 1 [LC] Z/2 quotient
        assert kappa_ch(enr) == 1
        assert kappa_ch(enr) == kappa_ch(k3_surface()) // 2

    def test_kappa_ch_quintic_is_rational(self):
        """kappa_ch(Quintic) = -25/3 (rational, from BCOV formula)."""
        q = quintic_threefold()
        # VERIFIED [DC] kappa_ch(Quintic) = -25/3 [LC] BCOV formula
        assert kappa_ch_rational(q) == Fraction(-25, 3)

    def test_kappa_ch_abelian_surface(self):
        """kappa_ch(T^4) = 0 = chi(O_{T^4})."""
        t4 = abelian_surface()
        # VERIFIED [DC] kappa_ch(T^4) = 0 [LC] abelian variety
        assert kappa_ch(t4) == 0


# ======================================================================
# 4. kappa_BKM (Borcherds-Kac-Moody weight)
# ======================================================================

class TestKappaBKM:
    """kappa_BKM: weight of the BKM automorphic form."""

    def test_kappa_BKM_K3xE(self):
        """kappa_BKM(K3 x E) = 5 = wt(Delta_5)."""
        k3e = k3_times_e()
        # VERIFIED [DC] kappa_BKM = 5 [LC] Borcherds lift weight
        assert kappa_BKM(k3e) == 5

    def test_kappa_BKM_from_h11(self):
        """kappa_BKM = c_f(0)/2 = h^{1,1}(K3)/4 = 20/4 = 5."""
        result = borcherds_weight_from_h11()
        # VERIFIED [DC] Borcherds weight formula [LC] h^{1,1}
        assert result["c_f_0_from_h11"] == 10
        assert result["c_f_0_from_chi"] == 10
        assert result["c_f_0_consistent"]
        assert result["weight_Delta5"] == 5
        assert result["kappa_BKM"] == 5

    def test_kappa_BKM_from_chi(self):
        """kappa_BKM = (chi_top(K3) - 4) / 4 = (24-4)/4 = 5."""
        k3 = k3_surface()
        # VERIFIED [DC] alternative weight formula [LC] chi_top
        assert (k3.chi_top - 4) // 4 == 5

    def test_phi10_weight(self):
        """wt(Phi_{10}) = 10 = 2 * kappa_BKM."""
        result = borcherds_weight_from_h11()
        # VERIFIED [DC] Phi_10 weight identity [LC] Siegel modular form
        assert result["weight_Phi10"] == 10
        assert result["Phi10_is_Delta5_squared"]

    def test_kappa_BKM_not_defined_for_K3_alone(self):
        """kappa_BKM is not naturally defined for K3 at d=2."""
        k3 = k3_surface()
        # VERIFIED [DC] kappa_BKM undefined at d=2 [LC] scope
        assert kappa_BKM(k3) is None


# ======================================================================
# 5. kappa_fiber (lattice rank)
# ======================================================================

class TestKappaFiber:
    """kappa_fiber: rank of the Mukai lattice."""

    def test_kappa_fiber_K3(self):
        """kappa_fiber(K3) = 24 = rank(Lambda_{Mukai})."""
        k3 = k3_surface()
        # VERIFIED [DC] Mukai lattice rank [LC] h^0+h^2+h^4 = 1+22+1
        assert kappa_fiber(k3) == 24

    def test_kappa_fiber_K3xE(self):
        """kappa_fiber(K3 x E) = 24 (same Mukai lattice)."""
        k3e = k3_times_e()
        # VERIFIED [DC] fiber rank for K3xE [LC] same K3 lattice
        assert kappa_fiber(k3e) == 24


# ======================================================================
# 6. Relations between kappa values
# ======================================================================

class TestKappaRelations:
    """Cross-relations between the four kappa invariants."""

    def test_BKM_decomposition(self):
        """The canonical additive BKM decomposition is false.

        The equality 3 + 2 = 5 survives only as a named
        Heisenberg-specialisation fibre coincidence at N=1.
        """
        result = verify_BKM_decomposition_k3e()
        # VERIFIED [DC] BKM decomposition rejected [LC] Borcherds weight theorem
        assert not result["decomposition_holds"]
        assert not result["compact_total_plus_K3_fiber_holds"]
        assert not result["compact_total_plus_elliptic_fiber_holds"]
        assert result["heis_fiber_coincidence_holds"]
        assert result["kappa_ch_Heis_K3xE"] == 3
        assert result["kappa_ch_compact_hodge_K3xE"] == 0
        assert result["kappa_BKM_K3xE"] == 5
        assert result["kappa_cat_K3"] == 2
        assert result["kappa_cat_E"] == 0
        assert result["kappa_cat_K3xE"] == 0
        # Critical: uses FIBER chi(O), not total space chi(O)
        assert result["fiber_not_total_space"]
        assert result["chi_O_total_space_vanishes"]

    def test_chi_top_24_failures(self):
        """chi_top/24 does NOT give kappa_ch in general."""
        result = verify_chi_top_over_24_failure()
        # VERIFIED [DC] chi_top/24 failure [LC] multiple examples
        assert result["E_fails"]      # 0 != 1
        assert result["K3_fails"]     # 1 != 2
        assert result["K3xE_compact_matches"]  # 0 = 0
        assert result["K3xE_heis_fails"]       # 0 != 3
        # But quintic matches
        assert result["Quintic_matches"]  # -25/3 = -25/3

    def test_kappa_ch_neq_chi_O_for_E(self):
        """kappa_ch(E) = 1 != chi(O_E) = 0.

        This is the simplest demonstration that kappa_ch is NOT
        always chi(O_X). At d=1, kappa_ch = dim_C.
        """
        e = elliptic_curve()
        # VERIFIED [DC] kappa_ch != chi(O) at d=1 [LC] explicit
        assert kappa_ch(e) == 1
        assert kappa_cat(e) == 0
        assert kappa_ch(e) != kappa_cat(e)

    def test_four_values_distinct_K3xE(self):
        """The K3 x E total package and fibre witness are separated.

        Total-space package: {0, 3, 5, 24}.
        Including the K3-fibre witness gives {0, 2, 3, 5, 24}.
        """
        spec = k3e_spectrum()
        # VERIFIED [DC] total-space package [LC] explicit
        assert spec["spectrum_set_total_space"] == [0, 3, 5, 24]
        # VERIFIED [DC] fibre witness separated [LC] explicit
        assert spec["spectrum_set_with_fiber_witness"] == [0, 2, 3, 5, 24]

    def test_kappa_BKM_over_kappa_ch_ratio(self):
        """kappa_BKM / kappa_ch^{Heis} = 5/3."""
        k3e = k3_times_e()
        # VERIFIED [DC] BKM/ch ratio [LC] second quantization
        assert Fraction(kappa_BKM(k3e), kappa_ch(k3e)) == Fraction(5, 3)

    def test_kappa_fiber_minus_kappa_BKM(self):
        """kappa_fiber - kappa_BKM = 24 - 5 = 19.

        The 19 "lost" units correspond to the codimension of
        Lambda^{3,2} (rank 5) in the Mukai lattice (rank 24).
        """
        k3e = k3_times_e()
        # VERIFIED [DC] fiber-BKM deficit [LC] lattice codimension
        deficit = kappa_fiber(k3e) - kappa_BKM(k3e)
        assert deficit == 19
        # Lattice explanation: rank(Mukai) - rank(Lambda^{3,2}) = 24-5
        assert deficit == 24 - 5


# ======================================================================
# 7. Spectrum tables
# ======================================================================

class TestSpectrumTables:
    """Full spectrum tables matching the manuscript."""

    def test_k3_spectrum(self):
        """K3 spectrum: {2, 24}."""
        spec = k3_spectrum()
        # VERIFIED [DC] K3 spectrum [LC] Proposition prop:k3-trichotomy
        assert spec["kappa_cat"] == 2
        assert spec["kappa_ch"] == 2
        assert spec["kappa_ch_equals_kappa_cat"]
        assert spec["kappa_fiber"] == 24
        assert spec["kappa_BKM"] is None

    def test_k3e_spectrum(self):
        """K3 x E total spectrum is {0, 3, 5, 24}; fibre witness adds 2."""
        spec = k3e_spectrum()
        # VERIFIED [DC] K3xE spectrum [LC] Proposition prop:kappa-spectrum-reconciliation
        assert spec["kappa_cat_total_space"] == 0
        assert spec["kappa_cat_K3_fiber"] == 2
        assert spec["kappa_ch"] == 3
        assert spec["kappa_ch_Heis"] == 3
        assert spec["kappa_ch_compact_hodge"] == 0
        assert spec["kappa_BKM"] == 5
        assert spec["kappa_fiber"] == 24
        assert not spec["BKM_decomposition"]
        assert spec["BKM_heis_fiber_coincidence"]
        assert spec["spectrum_set_total_space"] == [0, 3, 5, 24]
        assert spec["spectrum_set_with_fiber_witness"] == [0, 2, 3, 5, 24]

    def test_enriques_spectrum(self):
        """Enriques x E conjectural spectrum."""
        spec = enriques_times_e_spectrum()
        # VERIFIED [DC] Enriques spectrum [LC] Conjecture conj:enriques-kappa-spectrum
        assert spec["kappa_cat_Enr"] == 1
        assert spec["kappa_ch_Enr"] == 1
        assert spec["kappa_BKM_conjectural"] == 4
        assert spec["halving_ratio"] == Fraction(5, 4)


# ======================================================================
# 8. Physical meaning
# ======================================================================

class TestPhysicalMeaning:
    """Physical interpretations are documented (no computation to verify)."""

    def test_physical_meaning_keys(self):
        """All four kappa subscripts have physical interpretations."""
        pm = physical_meaning()
        # VERIFIED [DC] all subscripts documented [LC] AP113
        assert set(pm.keys()) == {"kappa_cat", "kappa_ch", "kappa_BKM", "kappa_fiber"}


# ======================================================================
# 9. Master verification
# ======================================================================

class TestMasterVerification:
    """End-to-end verification."""

    def test_verify_all_passes(self):
        """All verifications pass."""
        results = verify_all()
        # All kappa_cat = chi(O) checks
        for X_name in ["K3", "E", "K3xE", "Quintic", "Enr", "T^4"]:
            assert results[f"kappa_cat_is_chiO_{X_name}"]

        # kappa_ch = kappa_cat at d=2
        assert results["kappa_ch_eq_kappa_cat_K3"]
        assert results["kappa_ch_eq_kappa_cat_T4"]

        # Heisenberg-specialisation additivity
        assert results["additivity_K3xE"]
        assert results["heis_additivity_K3xE"]

        # chi(O) multiplicativity
        assert results["chi_O_multiplicative"]

        # BKM decomposition is false; the N=1 Heisenberg-fibre coincidence remains
        assert not results["BKM_decomposition"]["decomposition_holds"]
        assert results["BKM_decomposition"]["heis_fiber_coincidence_holds"]

        # Borcherds weight
        assert results["borcherds_weight"]["kappa_BKM"] == 5

    def test_spectrum_numerical_values(self):
        """Final numerical check against CLAUDE.md table."""
        results = verify_all()
        vals = results["K3xE_spectrum_values"]
        # VERIFIED [DC] CLAUDE.md kappa-spectrum table [LC] AP113
        assert vals["kappa_cat_total"] == 0
        assert vals["kappa_cat_fiber"] == 2
        assert vals["kappa_ch"] == 3
        assert vals["kappa_ch_Heis"] == 3
        assert vals["kappa_ch_compact_hodge"] == 0
        assert vals["kappa_BKM"] == 5
        assert vals["kappa_fiber"] == 24
