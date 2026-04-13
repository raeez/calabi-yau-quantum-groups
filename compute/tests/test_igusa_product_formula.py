from compute.lib.igusa_product_formula import verify_eta9_identity, verify_product_formula


def test_eta9_fourier_jacobi_identity():
    result = verify_eta9_identity(20)

    assert all(abs(abs(entry["ratio"]) - 1.0) < 1e-3 for entry in result["test_results"])


def test_borcherds_product_matches_delta5_in_absolute_value():
    result = verify_product_formula(2.0j, 0.1j, 2.0j, N_prod=10, N_theta=20, D_max=60)

    assert result["abs_relative_error"] < 1e-6
