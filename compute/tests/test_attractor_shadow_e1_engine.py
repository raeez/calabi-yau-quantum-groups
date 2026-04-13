from compute.lib.attractor_shadow_e1_engine import (
    CONIFOLD_SHADOW,
    verify_bridge_conifold,
    verify_parallel_transport,
)


def test_conifold_bridge_is_proved_class_g_case():
    bridge = verify_bridge_conifold()

    assert bridge.Q_Z_proportional
    assert bridge.connection_match
    assert bridge.zero_attractor_match
    assert bridge.monodromy_match
    assert bridge.wall_crossing_match
    assert bridge.bridge_type.startswith("proved")


def test_conifold_shadow_parallel_transport_is_flat():
    transport = verify_parallel_transport(CONIFOLD_SHADOW, [0.0, 0.5, 1.0])

    assert transport["error"]
    assert max(transport["error"]) < 1e-8
