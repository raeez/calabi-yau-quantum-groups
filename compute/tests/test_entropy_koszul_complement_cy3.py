from fractions import Fraction

from compute.lib.entropy_koszul_complement_cy3 import (
    complementarity_landscape,
    k3e_kappa,
    verify_complementarity_consistency,
    verify_faber_pandharipande,
)


def test_faber_pandharipande_seed_values():
    checks = verify_faber_pandharipande()

    assert checks[1] == (Fraction(1, 24), Fraction(1, 24))
    assert checks[2] == (Fraction(7, 5760), Fraction(7, 5760))
    assert checks[3] == (Fraction(31, 967680), Fraction(31, 967680))


def test_complementarity_landscape_internal_consistency():
    assert all(verify_complementarity_consistency().values())


def test_k3e_bkm_dual_scalar_is_open_not_minus_five():
    data = k3e_kappa()

    assert data.kappa == Fraction(5)
    assert data.family_type == "BKM_class_M"
    assert data.kappa_dual is None
    assert data.complementarity_sum is None
    assert "open" in data.dual_status


def test_landscape_records_k3e_complementarity_as_open():
    entries = {entry.name: entry for entry in complementarity_landscape()}
    k3e = entries["K3 x E"]

    assert k3e.comp_sum is None
    assert k3e.kappa_dual is None
    assert k3e.is_antisymmetric is False
