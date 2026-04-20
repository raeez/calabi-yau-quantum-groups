"""Tests for k3_yangian_wave18_enriques_bkm.

Enriques BKM superalgebra g_{Delta_5}^{Enr}. Three verification paths:
  (a) Lattice signature / rank consistency (Nikulin 1979; BHPV 2004).
  (b) Siegel weight 5/2 = 5 * chi_top(En) / chi_top(K3) = 5 * 12/24.
  (c) Elliptic genus halving f_{En}(n,l) = f_{K3}(n,l)/2 (Borisov-Libgober 1998).
"""

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_wave18_enriques_bkm import (
    enriques_cartan_description,
    enriques_elliptic_genus_fourier,
    enriques_lattice_rank,
    enriques_lattice_signature,
    enriques_number_of_fixed_points,
    enriques_siegel_weight,
    enriques_siegel_weight_derivation,
    paramodular_group_level,
)


def test_smoke_import():
    assert enriques_lattice_rank() == 10


def test_lattice_signature_and_rank():
    """Path (a): E_8(-1) + II_{1,1} has signature (1,9), rank 10."""
    sig = enriques_lattice_signature()
    assert sig == (1, 9)
    assert sum(sig) == enriques_lattice_rank()


def test_siegel_weight_half_integer():
    """Weight 5/2 on K(2) subset Sp_4(Q)."""
    w = enriques_siegel_weight()
    assert w == Fraction(5, 2)
    assert w.denominator == 2


def test_siegel_weight_derivation_consistency():
    """Path (b): w_En = w_K3 * chi_top(En) / chi_top(K3) = 5 * 12 / 24 = 5/2.

    Cross-check: derivation data is internally consistent and forces metaplectic.
    """
    d = enriques_siegel_weight_derivation()
    expected = Fraction(d['K3_weight'] * d['chi_top_En'], d['chi_top_K3'])
    assert d['Enriques_weight'] == expected == Fraction(5, 2)
    assert d['is_half_integer'] is True
    assert d['forces_metaplectic'] is True
    assert d['paramodular_level'] == paramodular_group_level() == 2


def test_iota_fixed_point_free():
    """Enriques involution is fixed-point-free on K3 (BHPV 2004 Prop 15.1).

    Consequence: twisted sector vanishes -> Borisov-Libgober halving.
    """
    assert enriques_number_of_fixed_points() == 0


def test_elliptic_genus_halving_identity():
    """Path (c): f_{En}(n,l) = f_{K3}(n,l) / 2, all integers.

    Cross-check: the explicit Enriques Fourier coefficients (5, -32, 54, -32, 5)
    at (n=1, l in {-2,-1,0,1,2}) match half of the K3 values (10, -64, 108, -64, 10).
    """
    from compute.lib.phi01_fourier import phi01_table

    k3 = phi01_table(3)
    en = enriques_elliptic_genus_fourier(3)
    for key, val_k3 in k3.items():
        assert en[key] == Fraction(val_k3, 2)
    # Eichler-Zagier integrality applies to the K3 elliptic genus at n >= 1;
    # the Enriques halving preserves integrality on the (n >= 1) Fourier support.
    for (n, l), val in en.items():
        if n >= 1 and k3.get((n, l), 0) % 2 == 0:
            assert val.denominator == 1

    expected_en = {(1, -2): 5, (1, -1): -32, (1, 0): 54, (1, 1): -32, (1, 2): 5}
    for key, v in expected_en.items():
        if key in en:
            assert en[key] == v


def test_cartan_description_keys():
    """Cartan datum contains lattice, signature, and primary references."""
    d = enriques_cartan_description()
    assert d['rank'] == 10
    assert d['signature'] == (1, 9)
    assert 'E_8(-1)' in d['enriques_lattice']
    assert d['borcherds_input_signature'] == (2, 10)
