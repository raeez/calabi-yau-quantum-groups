from fractions import Fraction

from compute.lib.frontier_realization_gate import (
    CROSS_VOLUME_CY3_MAPS,
    five_gate_realization_certificate,
)


def test_five_gate_certificate_formally_closes_all_gates():
    cert = five_gate_realization_certificate()

    assert cert.formal_closure
    assert tuple(gate.name for gate in cert.gates) == (
        "completed Hall package",
        "quintic E100 finite table",
        "oriented hCS-to-Hall descent",
        "protected BPS product functor",
        "global CY3 Vol I promotion",
    )


def test_certificate_keeps_actual_residual_inputs_visible():
    cert = five_gate_realization_certificate()

    assert any("oriented critical CoHA" in item for item in cert.residual_inputs)
    assert any("singular-theta/Petersson" in item for item in cert.residual_inputs)
    assert any("Mittag-Leffler" in item for item in cert.residual_inputs)
    assert any("boundary OPE" in item for item in cert.residual_inputs)
    assert any("outside framed/toric/formal loci" in item for item in cert.residual_inputs)


def test_quintic_relation_and_pivot_are_exact():
    cert = five_gate_realization_certificate()

    assert cert.quintic_relation_coefficients == {
        -3: -57062154240000,
        -7: 0,
        -23: -23587200,
        -24: 23587200,
        -39: 36193,
    }
    assert cert.quintic_forced_pivot == Fraction(57062154240000, 36193)


def test_cross_volume_map_roster_is_complete_and_ordered():
    cert = five_gate_realization_certificate()

    assert cert.cross_volume_maps == CROSS_VOLUME_CY3_MAPS
    assert cert.cross_volume_maps == (
        "Theta_A^(3)",
        "Theta_B^(3)",
        "Theta_C^(3)",
        "Theta_C^der",
        "Theta_D^unif",
        "Theta_H^(3)",
        "Theta_Z^(3)",
    )
