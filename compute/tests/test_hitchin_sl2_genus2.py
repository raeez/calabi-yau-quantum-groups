from compute.lib.hitchin_sl2_genus2 import (
    hitchin_dimensions,
    spectral_curve_sl2,
    verify_all,
)


def test_sl2_genus2_distinguished_dimensions():
    dims = hitchin_dimensions("SL_2", 2)

    assert dims.dim_complex == 6
    assert dims.dim_hitchin_base == 3
    assert dims.is_lagrangian_cy3


def test_hitchin_seed_verification_surface():
    spectral = spectral_curve_sl2(2)

    assert spectral.genus_spectral == 5
    assert spectral.dim_prym == 3
    assert all(verify_all().values())
