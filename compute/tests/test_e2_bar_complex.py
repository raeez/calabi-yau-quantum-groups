from sympy import Rational

from compute.lib.e2_bar_complex import compute_e2_bar_heisenberg, verify_qybe_sl2


def test_heisenberg_e2_bar_degenerates_to_einfty_case():
    result = compute_e2_bar_heisenberg(k=Rational(1), max_x=2, max_y=2)

    assert result["d_X_vanishes"]
    assert result["d_Y_vanishes"]
    assert result["braiding_symmetric"]


def test_sl2_kz_rmatrix_satisfies_qybe():
    assert verify_qybe_sl2(1) < 1e-12
