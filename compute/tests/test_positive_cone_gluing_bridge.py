"""Tests for the homotopy-gluing / positive-cone arithmetic bridge."""

from fractions import Fraction

from compute.lib.positive_cone_gluing_bridge import (
    RHO,
    alpha,
    all_alpha_identities,
    bps_pair,
    bridge_dictionary,
    chamber_wall_pairings,
    discriminant,
    in_closed_poly_ii,
    in_igusa_effective_chamber,
    kappa_bkm_from_constant_term,
    lorentz_pair,
    rho_wall_pairings,
    simple_root_gram,
)


def test_simple_root_gram_matrix():
    assert simple_root_gram() == (
        (Fraction(2), Fraction(-2), Fraction(-2)),
        (Fraction(-2), Fraction(2), Fraction(-2)),
        (Fraction(-2), Fraction(-2), Fraction(2)),
    )


def test_weyl_vector_wall_equations():
    assert rho_wall_pairings() == (Fraction(-1), Fraction(-1), Fraction(-1))
    assert in_closed_poly_ii(RHO)


def test_alpha_pairing_identity_on_sample():
    charges = [
        (0, -1, 0),
        (1, 0, 0),
        (0, 0, 1),
        (1, 1, 1),
        (2, -1, 3),
    ]
    assert all_alpha_identities(charges)


def test_alpha_square_is_discriminant():
    gamma = (2, -1, 3)
    assert lorentz_pair(alpha(gamma), alpha(gamma)) == -2 * discriminant(gamma)
    assert bps_pair(gamma, gamma) == discriminant(gamma)


def test_igusa_effective_chamber_lexicographic_boundary():
    assert in_igusa_effective_chamber((0, -1, 0))
    assert in_igusa_effective_chamber((1, 7, 0))
    assert in_igusa_effective_chamber((0, 7, 1))
    assert not in_igusa_effective_chamber((0, 1, 0))
    assert not in_igusa_effective_chamber((-1, 0, 1))


def test_positive_discriminant_terms_land_in_closed_chamber_after_rho_shift():
    # Lambda = rho + a for the first positive odd term (n,l,m)=(1,1,1)
    # has a=0 and lies in the closed chamber.
    lam = (Fraction(1), Fraction(-1, 2), Fraction(1))
    assert chamber_wall_pairings(lam) == (Fraction(-1), Fraction(-1), Fraction(-1))
    assert in_closed_poly_ii(lam)


def test_kappa_bkm_delta5_normalization():
    assert kappa_bkm_from_constant_term(10) == Fraction(5)


def test_bridge_dictionary_keeps_double_conditional():
    dictionary = bridge_dictionary()
    assert "DWR/Cech/Ran" in dictionary.homotopy_gluing_object
    assert "Gamma_eff" in dictionary.positive_cone_object
    assert "nu_Delta_5" in dictionary.orientation_character
    assert "conditional" in dictionary.status
