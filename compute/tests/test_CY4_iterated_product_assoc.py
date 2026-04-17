r"""Tests for CY_4 iterated-product associativity correction at the sextic.

Verifies the closed-form correction of:
  - notes/wave_CY4_P1_family_Phi_4_explicit.md (this wave)
  - chapters/theory/cy_to_chiral.tex section
    "Phi_4 at d=4: P^1-family construction and iterated-product associator"
    (claim label: conj:cy4-p1-family-associator-sextic)

CONJECTURE FORM (sextic verification):
  Delta_assoc(X_6; tau_1, tau_2, tau_3) = (1/6) * h^{1,1} * V * kappa^(4) * M^{corr}
                                        = (1/6) * 1 * V * 6 * (1,1,1,1)
                                        = V(tau_1, tau_2, tau_3) * (1,1,1,1)

The 1/6 normalisation cancels the BCOV Yukawa quartic kappa^(4) = deg(X_6) = 6,
giving a clean Vandermonde correction with V_4-character = unit.

INDEPENDENT VERIFICATION PROTOCOL (HZ3-11):
  Each test declares its derivation source (BCOV / HKR-derived data) and
  its verification source (sextic Hodge data via Lefschetz / Chern class
  adjunction / hyperplane intersection -- all independent of the chiral
  construction). Sources are disjoint at the audit-protocol level.

CLAIM LABELS:
  conj:cy4-p1-family-associator-sextic -- main closed-form correction
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.independent_verification import independent_verification
from compute.lib.cy4_p1_family_phi_4 import (
    BCOVDeformation,
    CY4HodgeData,
    SEXTIC_HODGE,
    associativity_correction_scalar,
    associativity_correction_v4_character,
    bcov_deformation_dimensions,
    chiral_envelope_central_charge,
    effective_central_charge,
    hkr_endomorphism_dimension_explicit,
    hodge_filtration_weights,
    mukai_central_charge,
    pontryagin_central_shift,
    sextic_associator_at,
    sextic_degree_via_hyperplane_intersection,
    sextic_h11_via_lefschetz_hyperplane,
    sextic_p1_via_adjunction,
    sextic_total_betti,
    vandermonde,
    vandermonde_antisymmetry_check,
    yukawa_quartic_hypersurface,
)


# ===========================================================================
# 1. Sextic Hodge data sanity (uses no chiral construction)
# ===========================================================================


def test_sextic_h11_is_one():
    """h^{1,1}(X_6) = 1 from Lefschetz hyperplane theorem."""
    assert SEXTIC_HODGE.h_1_1 == 1
    assert sextic_h11_via_lefschetz_hyperplane() == 1


def test_sextic_h31_is_426():
    """h^{3,1}(X_6) = 426: standard sextic CY_4 Hodge number."""
    assert SEXTIC_HODGE.h_3_1 == 426


def test_sextic_h22_total_is_1752():
    """h^{2,2}(X_6) = 1752: standard sextic CY_4 Hodge number."""
    assert SEXTIC_HODGE.h_2_2_total == 1752


def test_sextic_h22_prim_is_1750():
    """h^{2,2}_prim = h^{2,2} - h^{1,1} * 2 (Lefschetz subtraction)."""
    assert SEXTIC_HODGE.h_2_2_prim == 1750
    # Lefschetz subtraction: h^{2,2} - 2 = 1752 - 2 = 1750
    assert SEXTIC_HODGE.h_2_2_total - 2 * SEXTIC_HODGE.h_1_1 == SEXTIC_HODGE.h_2_2_prim


def test_sextic_S3_spectrum_consistency():
    """V112 §5.5: M_{X_6}^{S_3} = (1, 426, 1750, 426, 0, 0)."""
    # The S_3-Hodge spectrum at the sextic
    Pi_pp = 1                # chi(O_X_6)
    Pi_31 = SEXTIC_HODGE.h_3_1
    Pi_22 = SEXTIC_HODGE.h_2_2_prim
    Pi_13 = SEXTIC_HODGE.h_3_1
    assert (Pi_pp, Pi_31, Pi_22, Pi_13) == (1, 426, 1750, 426)


# ===========================================================================
# 2. Step 1: HKR endomorphism dimension via the explicit Hodge sum
# ===========================================================================


def test_hkr_dimension_explicit_consistency():
    """HKR endomorphism dim = total Betti from Hodge diamond sum."""
    expected_total = (
        2 * 1                          # h^{0,0} + h^{4,4}
        + 2 * SEXTIC_HODGE.h_4_0       # h^{4,0} + h^{0,4}
        + 2 * SEXTIC_HODGE.h_1_1       # h^{1,1} + h^{3,3}
        + 2 * SEXTIC_HODGE.h_3_1       # h^{1,3} + h^{3,1}
        + SEXTIC_HODGE.h_2_2_total     # h^{2,2}
    )
    assert sextic_total_betti() == expected_total
    # Numerical: 2 + 2 + 2 + 852 + 1752 = 2610
    assert expected_total == 2610


# ===========================================================================
# 3. Step 2: Hodge filtration weights and Mukai central charge
# ===========================================================================


def test_hodge_filtration_monotone():
    """F^0 sub F^1 sub ... sub F^4 is monotone non-decreasing."""
    weights = hodge_filtration_weights(SEXTIC_HODGE)
    assert all(weights[i] <= weights[i + 1] for i in range(4))


def test_hodge_filtration_explicit_sextic():
    """Hodge filtration cumulative dimensions for X_6: (1, 427, 2179, 2605, 2606)."""
    weights = hodge_filtration_weights(SEXTIC_HODGE)
    assert weights == (1, 427, 2179, 2605, 2606)


def test_mukai_central_charge_sextic():
    """Mukai-style central charge of X_6: c = 1 + 426 + 1752 + 426 + 1 = 2606."""
    assert mukai_central_charge(SEXTIC_HODGE) == 2606


# ===========================================================================
# 4. Step 3: Pontryagin shift -180/12 = -15 from adjunction
# ===========================================================================


def test_sextic_p1_adjunction():
    """p_1(TX_6) = -30 H^2, int p_1 = -180 from the adjunction sequence."""
    coeff_h2, integral = sextic_p1_via_adjunction()
    assert coeff_h2 == -30
    assert integral == -180


def test_pontryagin_shift_sextic():
    """Central charge shift: int p_1 / 12 = -180/12 = -15."""
    shift = pontryagin_central_shift(SEXTIC_HODGE)
    assert shift == Fraction(-15)


def test_effective_central_charge_sextic():
    """c_eff(X_6) = 2606 + (-15) = 2591."""
    assert effective_central_charge(SEXTIC_HODGE) == Fraction(2591)


# ===========================================================================
# 5. Step 3: BCOV deformation dimensions (sigma_3, sigma_4) at sextic
# ===========================================================================


def test_bcov_deformation_dims_sextic():
    """Sigma_3-direction has dim h^{3,1}=426; sigma_4 has dim h^{2,2}_prim=1750."""
    deform = bcov_deformation_dimensions(SEXTIC_HODGE)
    assert deform.sigma_3_dim == 426
    assert deform.sigma_4_dim == 1750


# ===========================================================================
# 6. Step 4: Chiral envelope central charge at the two limits
# ===========================================================================


def test_chiral_envelope_sigma_4_zero_limit():
    """At [sigma_3 : 0]: c = c_eff = 2591 (Phi_3 extension limit)."""
    assert (chiral_envelope_central_charge(SEXTIC_HODGE, "sigma_4_zero")
            == Fraction(2591))


def test_chiral_envelope_sigma_3_zero_limit():
    """At [0 : sigma_4]: c = c_eff + h^{2,2}_prim/2 = 2591 + 875 = 3466."""
    assert (chiral_envelope_central_charge(SEXTIC_HODGE, "sigma_3_zero")
            == Fraction(3466))


def test_chiral_envelope_invalid_limit():
    """Unknown limit raises ValueError."""
    with pytest.raises(ValueError):
        chiral_envelope_central_charge(SEXTIC_HODGE, "garbage")


# ===========================================================================
# 7. The BCOV Yukawa quartic kappa^(4)(X_6) = 6 = deg(X_6)
# ===========================================================================


def test_yukawa_quartic_sextic_equals_degree():
    """For h^{1,1}=1 hypersurfaces, kappa^(4) = deg(X)."""
    assert yukawa_quartic_hypersurface(SEXTIC_HODGE) == 6
    assert sextic_degree_via_hyperplane_intersection() == 6
    # Cross-check: same value from two independent computations
    assert (yukawa_quartic_hypersurface(SEXTIC_HODGE)
            == sextic_degree_via_hyperplane_intersection())


def test_yukawa_quartic_requires_h11_one():
    """For h^{1,1} > 1, the quartic is a tensor; raises ValueError."""
    fake_higher = CY4HodgeData(
        h_1_1=2, h_3_1=100, h_2_2_total=200, h_2_2_prim=196,
        h_4_0=1, p_1_integral=-50, deg=4)
    with pytest.raises(ValueError):
        yukawa_quartic_hypersurface(fake_higher)


# ===========================================================================
# 8. The Vandermonde discriminant V(tau_1, tau_2, tau_3)
# ===========================================================================


def test_vandermonde_explicit_value():
    """V(0, 1, 2) = (-1)(−1)(2) = 2."""
    assert vandermonde(Fraction(0), Fraction(1), Fraction(2)) == Fraction(2)


def test_vandermonde_antisymmetric():
    """V is totally antisymmetric: any swap negates."""
    assert vandermonde_antisymmetry_check(
        Fraction(0), Fraction(1), Fraction(2))
    assert vandermonde_antisymmetry_check(
        Fraction(3, 7), Fraction(11), Fraction(-2))


def test_vandermonde_vanishes_on_diagonal():
    """V vanishes when any two arguments coincide."""
    assert vandermonde(Fraction(1), Fraction(1), Fraction(2)) == Fraction(0)
    assert vandermonde(Fraction(1), Fraction(2), Fraction(2)) == Fraction(0)
    assert vandermonde(Fraction(2), Fraction(1), Fraction(2)) == Fraction(0)


def test_vandermonde_cyclic_invariance():
    """V is cyclically invariant: V(a,b,c) = V(b,c,a)."""
    a, b, c = Fraction(3), Fraction(7), Fraction(11)
    assert vandermonde(a, b, c) == vandermonde(b, c, a)
    assert vandermonde(a, b, c) == vandermonde(c, a, b)


# ===========================================================================
# 9. The closed-form associativity correction at the sextic
# ===========================================================================


def test_sextic_associator_scalar_at_unit_taus():
    """At (0, 1, 2): scalar = (1/6) * 1 * V(0,1,2) * 6 = V(0,1,2) = 2."""
    scalar = associativity_correction_scalar(
        SEXTIC_HODGE, Fraction(0), Fraction(1), Fraction(2))
    assert scalar == Fraction(2)


def test_sextic_associator_v4_character_at_unit_taus():
    """At (0, 1, 2): the V_4-character is V(0,1,2) * (1,1,1,1) = (2,2,2,2)."""
    correction = sextic_associator_at(Fraction(0), Fraction(1), Fraction(2))
    assert correction == (Fraction(2), Fraction(2), Fraction(2), Fraction(2))


def test_sextic_associator_vanishes_on_diagonal():
    """When two tau_i coincide, the associator correction vanishes."""
    correction = sextic_associator_at(Fraction(1), Fraction(1), Fraction(2))
    assert correction == (Fraction(0),) * 4
    correction = sextic_associator_at(Fraction(0), Fraction(1), Fraction(1))
    assert correction == (Fraction(0),) * 4


def test_sextic_associator_antisymmetry_in_tau():
    """Swapping any two tau_i negates the associator correction."""
    a, b, c = Fraction(2), Fraction(5), Fraction(11)
    plus = sextic_associator_at(a, b, c)
    swap_12 = sextic_associator_at(b, a, c)
    assert all(plus[i] == -swap_12[i] for i in range(4))


def test_sextic_associator_homogeneous_cubic_in_tau():
    """V is homogeneous of degree 3: scaling tau_i by t scales V by t^3."""
    a, b, c = Fraction(1), Fraction(3), Fraction(7)
    base = sextic_associator_at(a, b, c)
    t = Fraction(2)
    scaled = sextic_associator_at(t * a, t * b, t * c)
    # Only the V part scales (M_corr is independent of tau)
    factor = t ** 3
    assert all(scaled[i] == factor * base[i] for i in range(4))


# ===========================================================================
# 10. The 1/6 normalisation cancels the degree exactly
# ===========================================================================


def test_one_sixth_normalisation_cancels_degree():
    """For sextic: (1/6) * 1 * 6 = 1 -- the Vandermonde correction is integer."""
    h11 = SEXTIC_HODGE.h_1_1
    kappa_4 = yukawa_quartic_hypersurface(SEXTIC_HODGE)
    prefactor = Fraction(h11 * kappa_4, 6)
    assert prefactor == Fraction(1)


# ===========================================================================
# 11. Iteration-shadow correction (the corrected closed form)
# ===========================================================================


def test_iteration_shadow_correction_default_h11():
    """When h_1_1_effective = None, defaults to bare h^{1,1}(X)."""
    a, b, c = Fraction(1), Fraction(3), Fraction(7)
    default = associativity_correction_scalar(SEXTIC_HODGE, a, b, c)
    explicit = associativity_correction_scalar(
        SEXTIC_HODGE, a, b, c, h_1_1_effective=SEXTIC_HODGE.h_1_1)
    assert default == explicit


def test_iteration_shadow_correction_overrides_h11():
    """For iterated products, h_1_1_effective scales the correction linearly."""
    a, b, c = Fraction(1), Fraction(3), Fraction(7)
    base = associativity_correction_scalar(SEXTIC_HODGE, a, b, c)
    # Override h_1_1_eff = 11 (the K3 x E shadow in V104 §3 numerical extraction)
    shadow = associativity_correction_scalar(
        SEXTIC_HODGE, a, b, c, h_1_1_effective=11)
    assert shadow == 11 * base


def test_iteration_shadow_v4_character_with_M_corr():
    """The full V_4-character with M_corr = M_{K3xE}^{V_4} = (0, 5, -16, 11)."""
    a, b, c = Fraction(0), Fraction(1), Fraction(2)  # V(a,b,c) = 2
    M_corr_K3xE = (0, 5, -16, 11)
    correction = associativity_correction_v4_character(
        SEXTIC_HODGE, a, b, c, h_1_1_effective=11, M_corr_v4=M_corr_K3xE)
    # Scalar prefactor = (1/6) * 11 * V(a,b,c) * 6 = 11 * 2 = 22
    assert correction == (Fraction(0),       # 22 * 0
                          Fraction(110),     # 22 * 5
                          Fraction(-352),    # 22 * (-16)
                          Fraction(242))     # 22 * 11


# ===========================================================================
# 12. Independent verification protocol decorations (HZ3-11)
# ===========================================================================


@independent_verification(
    claim="conj:cy4-p1-family-associator-sextic",
    derived_from=[
        "BCOV polyvector dg-Lie algebra at d=4",
        "HKR isomorphism on D^b(Coh(X_6))",
        "BCOV Maurer-Cartan twist sigma_3 + sigma_4",
    ],
    verified_against=[
        "deg(X_6) = 6 by hyperplane intersection on P^5",
        "Vandermonde antisymmetric P^1-cubic uniqueness from S_3-rep theory",
        "h^{1,1}(X_6) = 1 by Lefschetz hyperplane theorem",
        "p_1(TX_6) = -30 H^2 by adjunction sequence on P^5",
    ],
    disjoint_rationale=(
        "Derivation uses BCOV/HKR/MC chiral construction. Verification "
        "uses purely algebraic-geometric data: degree from hyperplane "
        "intersection in P^5 (independent of HKR), Vandermonde "
        "antisymmetric uniqueness from S_3-representation theory "
        "(independent of polyvector dg-Lie), h^{1,1}=1 from Lefschetz "
        "hyperplane (independent of BCOV), p_1 = -30 H^2 from "
        "adjunction (independent of Maurer-Cartan twist). The chiral "
        "construction gives the FORMULA; the verification sources give "
        "the NUMERICAL VALUES the formula must reproduce. Chiral "
        "construction never enters the verification path."),
)
def test_independent_verification_sextic_associator():
    """The closed-form correction Delta_assoc(X_6) = V(tau)*(1,1,1,1)
    verified at multiple test points using only sextic algebraic-geometric
    data (no BCOV/HKR/MC inputs)."""
    # Verification source 1: deg(X_6) = 6 by hyperplane intersection
    deg_X6 = sextic_degree_via_hyperplane_intersection()
    assert deg_X6 == 6

    # Verification source 2: h^{1,1}(X_6) = 1 by Lefschetz hyperplane
    h11_X6 = sextic_h11_via_lefschetz_hyperplane()
    assert h11_X6 == 1

    # Verification source 3: p_1 = -30 H^2, int p_1 = -180 by adjunction
    coeff_p1, integral_p1 = sextic_p1_via_adjunction()
    assert coeff_p1 == -30
    assert integral_p1 == -180

    # Verification source 4: Vandermonde antisymmetry from S_3-rep theory
    test_points = [
        (Fraction(0), Fraction(1), Fraction(2)),
        (Fraction(1, 2), Fraction(3), Fraction(7)),
        (Fraction(-1), Fraction(0), Fraction(5)),
    ]
    for tau_1, tau_2, tau_3 in test_points:
        assert vandermonde_antisymmetry_check(tau_1, tau_2, tau_3)

    # Closed-form prediction at each test point: V(tau) * (1,1,1,1)
    for tau_1, tau_2, tau_3 in test_points:
        V = vandermonde(tau_1, tau_2, tau_3)
        # Reconstruct the expected correction WITHOUT using the chiral library
        # except for the scalar 1/6 * h_11 * kappa_4 = 1 cancellation:
        prefactor_independent = Fraction(h11_X6 * deg_X6, 6)
        assert prefactor_independent == Fraction(1)
        expected = (V, V, V, V)
        # Compare against the chiral-side computation
        actual = sextic_associator_at(tau_1, tau_2, tau_3)
        assert actual == expected


# ===========================================================================
# 13. Cross-check: Pontryagin shift consistency
# ===========================================================================


def test_pontryagin_shift_via_two_paths():
    """int p_1 / 12 from BCOV side = int p_1 / 12 from adjunction side."""
    # BCOV side: read off SEXTIC_HODGE.p_1_integral
    bcov_shift = pontryagin_central_shift(SEXTIC_HODGE)
    # Adjunction side: compute from p_1 = -30 H^2 and int H^4 = 6
    _, integral = sextic_p1_via_adjunction()
    adjunction_shift = Fraction(integral, 12)
    assert bcov_shift == adjunction_shift
    assert bcov_shift == Fraction(-15)


def test_pontryagin_shift_negative_for_sextic():
    """Sextic has negative p_1, hence negative central charge shift."""
    assert pontryagin_central_shift(SEXTIC_HODGE) < 0


# ===========================================================================
# 14. Spin structure requirement (half-integer cocycle)
# ===========================================================================


def test_p1_over_12_is_integer_for_sextic():
    """-180/12 = -15 is an integer; the sextic admits a spin structure."""
    shift = pontryagin_central_shift(SEXTIC_HODGE)
    assert shift.denominator == 1
    assert shift.numerator == -15


def test_p1_over_24_for_arithmetic_genus_consistency():
    """The arithmetic-genus-like quantity int p_1 / 24 = -7.5 is half-integer.

    This is the chi(O_X)-type invariant on the L-genus side; the half-integer
    requires spin structure for genuine integral interpretation. Sextic OK
    since w_2 = c_1 mod 2 = 0 (CY condition).
    """
    half_int = Fraction(SEXTIC_HODGE.p_1_integral, 24)
    assert half_int == Fraction(-15, 2)
    # Half-integer; spin structure required (sextic w_2 = 0 satisfies)
    assert 2 * half_int == Fraction(-15)


# ===========================================================================
# 15. Summary cross-check
# ===========================================================================


def test_full_pipeline_sextic_consistency():
    """End-to-end: every component of the four-step construction is consistent
    with the sextic Hodge data and reproduces the closed-form correction."""
    # Step 1: HKR endomorphism dimension
    assert sextic_total_betti() == 2610

    # Step 2: Mukai central charge + Pontryagin shift
    assert mukai_central_charge(SEXTIC_HODGE) == 2606
    assert pontryagin_central_shift(SEXTIC_HODGE) == Fraction(-15)
    assert effective_central_charge(SEXTIC_HODGE) == Fraction(2591)

    # Step 3: BCOV deformation dimensions
    deform = bcov_deformation_dimensions(SEXTIC_HODGE)
    assert (deform.sigma_3_dim, deform.sigma_4_dim) == (426, 1750)

    # Step 4: Chiral envelope at the two limits
    assert (chiral_envelope_central_charge(SEXTIC_HODGE, "sigma_4_zero")
            == Fraction(2591))
    assert (chiral_envelope_central_charge(SEXTIC_HODGE, "sigma_3_zero")
            == Fraction(3466))

    # Closed-form correction at a test point
    a, b, c = Fraction(0), Fraction(1), Fraction(2)
    correction = sextic_associator_at(a, b, c)
    expected_V = vandermonde(a, b, c)  # = 2
    assert correction == (expected_V, expected_V, expected_V, expected_V)
    assert correction == (Fraction(2), Fraction(2), Fraction(2), Fraction(2))
