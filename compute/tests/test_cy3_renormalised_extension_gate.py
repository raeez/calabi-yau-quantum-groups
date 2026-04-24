from compute.lib.cy3_renormalised_extension_gate import (
    ResidualStrength,
    dwr_descended_comparison,
    fixed_finite_chart,
    monotone_strength_chain,
    renormalised_local_chart,
)


def test_fixed_chart_kills_only_finite_projected_obstruction():
    datum = fixed_finite_chart()

    assert datum.closes("finite_fixed_projection")
    assert not datum.closes("renormalised_local_chart")
    assert not datum.closes("dwr_descended_comparison")
    assert datum.residual_obstructions() == ("o_theta^ren", "o_theta^des")
    assert datum.strength() == ResidualStrength.FIXED_FINITE_MODE


def test_anomaly_gate_alone_does_not_construct_renormalised_transfer():
    datum = fixed_finite_chart().with_gates("anomaly_free_qme")
    missing = tuple(gate.key for gate in datum.missing_for("renormalised_local_chart"))

    assert missing == (
        "nuclear_continuity",
        "renormalised_transfer",
        "differential_compatibility",
        "mc_multiplicativity",
    )
    assert datum.strength() == ResidualStrength.FIXED_FINITE_MODE


def test_renormalised_local_chart_still_requires_dwr_descent():
    datum = renormalised_local_chart()

    assert datum.closes("renormalised_local_chart")
    assert not datum.closes("dwr_descended_comparison")
    assert datum.residual_obstructions() == ("o_theta^des",)
    assert datum.strength() == ResidualStrength.RENORMALISED_LOCAL_CHART


def test_dwr_descended_comparison_closes_all_residual_theta_terms():
    datum = dwr_descended_comparison()

    assert datum.closes("dwr_descended_comparison")
    assert datum.residual_obstructions() == ()
    assert datum.strength() == ResidualStrength.DWR_DESCENDED_COMPARISON


def test_strength_chain_is_monotone():
    assert monotone_strength_chain(
        (
            fixed_finite_chart(),
            renormalised_local_chart(),
            dwr_descended_comparison(),
        )
    ) == (
        ResidualStrength.FIXED_FINITE_MODE,
        ResidualStrength.RENORMALISED_LOCAL_CHART,
        ResidualStrength.DWR_DESCENDED_COMPARISON,
    )
