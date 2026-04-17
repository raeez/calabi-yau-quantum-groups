"""
Self-test of the independent-verification infrastructure.

Tests the registry/decorator mechanism itself, independent of any
particular manuscript claim. Exercises three invariants:

1. A valid @independent_verification decoration registers the test and
   preserves its behaviour.

2. A tautological decoration (derivation source == verification source)
   raises IndependentVerificationError at decoration time.

3. Missing disjoint_rationale is rejected.

4. Coverage report math: covered == registry claims intersected with the
   supplied ProvedHere set.

These tests run in every `make test` invocation and guard the pipeline
against silent regression of the decorator semantics.
"""

from __future__ import annotations

import importlib
import pytest

from compute.lib import independent_verification as iv


@pytest.fixture(autouse=True)
def _isolate_registry():
    """Snapshot + restore the registry around each test.

    Without this, decorations registered by sibling test modules in the
    same pytest session would leak into these tests' assertions about
    registry size.
    """
    saved = iv.registry()
    iv.clear_registry()
    try:
        yield
    finally:
        iv.clear_registry()
        # Replay the saved registry so later tests see a consistent state.
        iv._REGISTRY.extend(saved)


def test_valid_decoration_registers_and_preserves_behaviour():
    @iv.independent_verification(
        claim="thm:fake-for-infra-test",
        derived_from=["paper A"],
        verified_against=["paper B"],
        disjoint_rationale="A and B use disjoint data (for the infra self-test).",
    )
    def inner(x):
        return x * 2

    # Behaviour preserved.
    assert inner(21) == 42

    # Exactly one entry registered, with the right shape.
    entries = iv.entries_for("thm:fake-for-infra-test")
    assert len(entries) == 1
    e = entries[0]
    assert e.derived_from == ("paper A",)
    assert e.verified_against == ("paper B",)
    assert not e.is_tautological()
    assert e.test_qualname.endswith("inner")


def test_tautological_decoration_raises_at_decoration_time():
    with pytest.raises(iv.IndependentVerificationError) as excinfo:
        @iv.independent_verification(
            claim="thm:tautology",
            derived_from=["shared source"],
            verified_against=["shared source"],
            disjoint_rationale="they are not actually disjoint",
        )
        def _bad():
            pass

    assert "shared source" in str(excinfo.value).lower()
    # Registry stays empty -- the tautology is caught before registration.
    assert iv.entries_for("thm:tautology") == []


def test_tautology_is_case_and_whitespace_insensitive():
    with pytest.raises(iv.IndependentVerificationError):
        @iv.independent_verification(
            claim="thm:case-taut",
            derived_from=["  Paper A "],
            verified_against=["paper a"],
            disjoint_rationale="whitespace/case masking",
        )
        def _bad():
            pass


def test_missing_rationale_raises():
    with pytest.raises(iv.IndependentVerificationError):
        @iv.independent_verification(
            claim="thm:no-rationale",
            derived_from=["A"],
            verified_against=["B"],
            disjoint_rationale="   ",
        )
        def _bad():
            pass


def test_coverage_report_math():
    @iv.independent_verification(
        claim="thm:alpha",
        derived_from=["src1"],
        verified_against=["src2"],
        disjoint_rationale="alpha is fine",
    )
    def _a():
        pass

    @iv.independent_verification(
        claim="thm:beta",
        derived_from=["src3"],
        verified_against=["src4"],
        disjoint_rationale="beta is fine",
    )
    def _b():
        pass

    # Pretend .tex declares thm:alpha and thm:gamma as ProvedHere.
    report = iv.build_coverage_report(["thm:alpha", "thm:gamma"])

    assert report.proved_here_claims == {"thm:alpha", "thm:gamma"}
    assert report.covered_claims == {"thm:alpha"}
    assert report.uncovered_claims == {"thm:gamma"}
    # thm:beta has a test but no ProvedHere => orphan.
    orphan_claims = {e.claim for e in report.orphan_entries}
    assert orphan_claims == {"thm:beta"}


def test_assert_sources_disjoint_direct_use():
    # Usable without the decorator.
    iv.assert_sources_disjoint(["x"], ["y"], claim="thm:ok")
    with pytest.raises(iv.IndependentVerificationError):
        iv.assert_sources_disjoint(["x"], ["x", "z"], claim="thm:bad")


def test_audit_script_importable():
    """The lint script should be importable without executing side effects."""
    mod = importlib.import_module(
        "compute.scripts.audit_independent_verification"
    )
    assert hasattr(mod, "scrape_proved_here")
    assert hasattr(mod, "main")
