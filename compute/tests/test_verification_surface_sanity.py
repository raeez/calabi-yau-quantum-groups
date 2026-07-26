"""Cheap verification-surface invariants for the CY3 bridge gates."""

import re
from pathlib import Path

from compute.lib.c3_hcs_hall_theta import continuity_bound_for_modes
from compute.lib.cy3_bridge_normal_form import (
    GATES,
    PROTECTED_PHYSICS_GATES,
    SEVEN_RIGIDIFICATIONS,
    TARGETS,
)

ROOT = Path(__file__).resolve().parents[2]


def _macro_int(source: str, name: str) -> int:
    match = re.search(rf"\\newcommand{{\\{name}}}{{([0-9]+)}}", source)
    assert match is not None
    return int(match.group(1))


def test_bridge_targets_use_declared_gates_and_are_nested() -> None:
    ordered_targets = (
        "local_c3_to_yplus",
        "w_infty_representation",
        "global_hcs_hall",
        "hall_borcherds_bkm",
        "protected_physics",
    )

    previous = set()
    for target in ordered_targets:
        current = TARGETS[target]
        assert all(key in GATES for key in current)
        assert previous.issubset(current)
        previous = set(current)

    assert TARGETS["protected_physics"] == PROTECTED_PHYSICS_GATES


def test_seven_rigidifications_are_declared_inside_protected_package() -> None:
    protected = set(TARGETS["protected_physics"])

    assert set(SEVEN_RIGIDIFICATIONS).issubset(protected)
    assert all(GATES[key].layer for key in SEVEN_RIGIDIFICATIONS)
    assert all(GATES[key].statement for key in SEVEN_RIGIDIFICATIONS)


def test_c3_theta_continuity_bound_covers_ternary_case() -> None:
    assert continuity_bound_for_modes(()) == (0, 0, 0)
    assert continuity_bound_for_modes((0, 1, 2)) == (3, 3, 3)


def test_compiled_verification_appendix_uses_live_lower_bounds() -> None:
    main = (ROOT / "main.tex").read_text(encoding="utf-8")
    appendix_path = ROOT / "appendices" / "engine_catalogue.tex"
    appendix = appendix_path.read_text(encoding="utf-8")
    engine_index = (ROOT / "compute" / "ENGINES.md").read_text(encoding="utf-8")

    assert "\\input{appendices/engine_catalogue}" in main
    assert "\\input{appendices/engine_table_rows}" not in appendix
    assert "\\input{appendices/test_suite}" not in main
    assert "34,000" not in engine_index
    assert "30,613" not in engine_index

    lib_modules = list((ROOT / "compute" / "lib").glob("*.py"))
    test_files = list((ROOT / "compute" / "tests").glob("test_*.py"))
    scripts = [p for p in (ROOT / "compute" / "scripts").iterdir() if p.is_file()]
    audits = [p for p in (ROOT / "compute" / "audit").iterdir() if p.is_file()]

    static_tests = 0
    for path in test_files:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("def test_") or line.startswith("async def test_"):
                static_tests += 1

    assert len(lib_modules) >= _macro_int(appendix, "VerificationSurfaceEngineLowerBound")
    assert len(test_files) >= _macro_int(appendix, "VerificationSurfaceTestFileLowerBound")
    assert static_tests >= _macro_int(appendix, "VerificationSurfaceStaticTestLowerBound")
    assert len(scripts) >= _macro_int(appendix, "VerificationSurfaceScriptLowerBound")
    assert len(audits) >= _macro_int(appendix, "VerificationSurfaceAuditLowerBound")
