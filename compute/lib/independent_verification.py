"""
Independent verification registry for ProvedHere claims.

MOTIVATION
----------
The 2026-04-16 adversarial audit (cache entries 57-68) exposed a systematic
failure mode: tests verify formulas against the SAME hardcoded table from
which the formula was derived. Example: kappa_BKM_universal.py defines
FRAME_SHAPE_DATA[N] = (weight, c_0, ...) with weight := c_0 / 2 literal, and
99 tests check Fraction(10, 2) == 5 against that table. This is tautology
dressed as verification.

PROTOCOL
--------
Every test that claims to verify a ProvedHere theorem must:

1. Declare its claim label via @independent_verification decorator.
2. Enumerate the DERIVATION sources (where the formula came from).
3. Enumerate the VERIFICATION sources (what the test compares against).
4. Assert derivation and verification sources are DISJOINT.

This module provides:
  - The decorator (run-time assertion + registry entry)
  - The registry (queryable by claim label, source, tautology status)
  - `assert_sources_disjoint`: the core disjointness check
  - `IndependentVerificationError`: raised when sources overlap

A companion lint (compute/scripts/audit_independent_verification.py) scans
.tex for ProvedHere tags and compares against the registry to produce a
coverage report.

USAGE
-----
    from compute.lib.independent_verification import independent_verification

    @independent_verification(
        claim="prop:bkm-weight-universal",
        derived_from=["Borcherds 1998 weight theorem",
                      "FRAME_SHAPE_DATA orbifold table (Gaberdiel-Volpato)"],
        verified_against=["Gritsenko-Nikulin Phi_10 denominator identity",
                          "Imaginary root multiplicities from g_{Delta_5} root system"],
        disjoint_rationale=(
            "FRAME_SHAPE_DATA supplies c_0 by definition of the lift input. "
            "Denominator identity independently computes the BKM central charge "
            "from imaginary root multiplicities without reference to the lift."),
    )
    def test_kappa_bkm_equals_bkm_central_charge():
        ...

If derived_from and verified_against share an element, the decorator raises
IndependentVerificationError at import time. This is intentional: tautological
tests must not silently register as verification.
"""

from __future__ import annotations

import functools
import inspect
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class VerificationEntry:
    """Record of one (test, claim) verification relationship."""
    claim: str
    test_qualname: str
    test_file: str
    derived_from: tuple[str, ...]
    verified_against: tuple[str, ...]
    disjoint_rationale: str

    def is_tautological(self) -> bool:
        """True if any derivation source also appears as a verification source.

        Comparison is case-insensitive and strips whitespace.
        """
        deriv = {s.strip().lower() for s in self.derived_from}
        verif = {s.strip().lower() for s in self.verified_against}
        return bool(deriv & verif)


# Module-level registry. Populated at import time as tests are loaded.
_REGISTRY: list[VerificationEntry] = []


def registry() -> list[VerificationEntry]:
    """Return the current registry (copy, so callers can't mutate)."""
    return list(_REGISTRY)


def claims_covered() -> set[str]:
    """Set of claim labels with at least one registered independent test."""
    return {e.claim for e in _REGISTRY if not e.is_tautological()}


def entries_for(claim: str) -> list[VerificationEntry]:
    """All entries registered against a specific claim label."""
    return [e for e in _REGISTRY if e.claim == claim]


def tautological_entries() -> list[VerificationEntry]:
    """Entries whose derivation and verification sources overlap."""
    return [e for e in _REGISTRY if e.is_tautological()]


def clear_registry() -> None:
    """Clear the registry. Used by the infra self-test to isolate state."""
    _REGISTRY.clear()


# ---------------------------------------------------------------------------
# Error
# ---------------------------------------------------------------------------


class IndependentVerificationError(AssertionError):
    """Raised when verification and derivation sources overlap.

    Subclasses AssertionError so pytest reports it as a test failure, not
    as a harness crash. This means: a tautological @independent_verification
    decoration will cause the test to fail at collection time.
    """


# ---------------------------------------------------------------------------
# Disjointness check
# ---------------------------------------------------------------------------


def assert_sources_disjoint(
    derived_from: Iterable[str],
    verified_against: Iterable[str],
    claim: str = "",
) -> None:
    """Raise IndependentVerificationError if the two source sets intersect.

    Whitespace-insensitive, case-insensitive comparison. Source labels must
    be exact strings (not substrings); callers are responsible for choosing
    canonical names.
    """
    deriv = {s.strip().lower() for s in derived_from}
    verif = {s.strip().lower() for s in verified_against}
    overlap = deriv & verif
    if overlap:
        raise IndependentVerificationError(
            f"claim={claim!r}: verification sources overlap with derivation "
            f"sources: {sorted(overlap)!r}. "
            "Tautological verification is not independent verification. "
            "Pick a source disjoint from the derivation, or restate the "
            "theorem's scope."
        )


# ---------------------------------------------------------------------------
# Decorator
# ---------------------------------------------------------------------------


def independent_verification(
    *,
    claim: str,
    derived_from: Iterable[str],
    verified_against: Iterable[str],
    disjoint_rationale: str,
) -> Callable:
    """Register a test as independently verifying a ProvedHere claim.

    Parameters
    ----------
    claim : str
        Label of the theorem/proposition being verified. Must match a
        \\label{...} in chapters/ or working_notes.tex. Convention: use the
        LaTeX label verbatim, e.g., "thm:phi-k3-explicit".
    derived_from : list[str]
        Canonical names of the data/papers/conventions from which the
        CLAIMED FORMULA was derived. These are the "suspect" sources that
        the test must AVOID when computing the verification value.
    verified_against : list[str]
        Canonical names of independent data/papers/conventions from which
        the TEST computes its expected value. These must be disjoint from
        derived_from.
    disjoint_rationale : str
        One-sentence explanation of why the two source sets are genuinely
        independent (not just renamed). Reviewed during audit.

    Raises
    ------
    IndependentVerificationError
        At decoration time, if derived_from and verified_against overlap.
        This surfaces as a test collection failure -- the tautology is
        caught before the test runs.

    Notes
    -----
    The decorator does not change test behaviour. It only installs a
    registry entry and enforces the disjointness invariant.
    """
    derived_tuple = tuple(derived_from)
    verified_tuple = tuple(verified_against)
    # Fail fast at import time -- tautological decorations cannot even be
    # registered.
    assert_sources_disjoint(derived_tuple, verified_tuple, claim=claim)
    if not disjoint_rationale or not disjoint_rationale.strip():
        raise IndependentVerificationError(
            f"claim={claim!r}: disjoint_rationale is required and must be "
            "non-empty. Explain WHY the two source sets are independent."
        )

    def decorator(fn: Callable) -> Callable:
        module = inspect.getmodule(fn)
        test_file = (
            str(Path(module.__file__).resolve())
            if module and module.__file__
            else "<unknown>"
        )
        entry = VerificationEntry(
            claim=claim,
            test_qualname=f"{fn.__module__}.{fn.__qualname__}",
            test_file=test_file,
            derived_from=derived_tuple,
            verified_against=verified_tuple,
            disjoint_rationale=disjoint_rationale.strip(),
        )
        _REGISTRY.append(entry)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        # Expose the entry on the wrapper for introspection.
        wrapper._iv_entry = entry  # type: ignore[attr-defined]
        return wrapper

    return decorator


# ---------------------------------------------------------------------------
# Coverage helpers (used by the lint script)
# ---------------------------------------------------------------------------


@dataclass
class CoverageReport:
    """Summary of ProvedHere coverage vs the registry."""
    proved_here_claims: set[str] = field(default_factory=set)
    covered_claims: set[str] = field(default_factory=set)
    tautological: list[VerificationEntry] = field(default_factory=list)

    @property
    def uncovered_claims(self) -> set[str]:
        return self.proved_here_claims - self.covered_claims

    @property
    def orphan_entries(self) -> list[VerificationEntry]:
        """Registry entries whose claim is not actually ProvedHere in any .tex."""
        return [
            e for e in _REGISTRY
            if e.claim not in self.proved_here_claims
        ]

    def summary(self) -> str:
        n_proved = len(self.proved_here_claims)
        n_covered = len(self.covered_claims)
        pct = (100.0 * n_covered / n_proved) if n_proved else 0.0
        lines = [
            f"ProvedHere claims found in .tex: {n_proved}",
            f"Claims with independent verification:  {n_covered} ({pct:.1f}%)",
            f"Claims WITHOUT independent verification: {len(self.uncovered_claims)}",
            f"Tautological registry entries: {len(self.tautological)}",
            f"Orphan registry entries (claim not found in .tex): "
            f"{len(self.orphan_entries)}",
        ]
        return "\n".join(lines)


def build_coverage_report(proved_here_labels: Iterable[str]) -> CoverageReport:
    """Combine the current registry with a set of ProvedHere labels.

    The caller (lint script) supplies labels scraped from .tex. This module
    stays independent of the scraper so the module is testable without any
    .tex files present.
    """
    labels = set(proved_here_labels)
    return CoverageReport(
        proved_here_claims=labels,
        covered_claims=claims_covered() & labels,
        tautological=tautological_entries(),
    )
