#!/usr/bin/env python3
"""
Audit ProvedHere coverage vs the independent-verification registry.

Scans chapters/, appendices/, notes/, working_notes.tex for
  \\ClaimStatusProvedHere
then pairs each with the nearest preceding \\label{...}. Imports every test
module in compute/tests/ so that @independent_verification decorators fire
and populate the registry. Reports:

  (a) How many ProvedHere claims have at least one independent test.
  (b) Which claims are uncovered (the gap to close).
  (c) Any registry entry that is tautological (source overlap) -- note:
      the decorator raises at import time, so a tautology prevents the
      test module from loading. We still report via a catch.
  (d) Orphan registry entries (decorated tests whose claim label is not
      actually ProvedHere anywhere).

Exit status
-----------
0   : no tautologies and no orphans (coverage gap is OK; gap reduction is a
      continuous project).
2   : at least one tautological decoration OR at least one orphan entry.

The CI gate uses the nonzero exit. Coverage percentage is reported but not
enforced -- enforcing a floor would incentivize tautological "fix" tests.
"""

from __future__ import annotations

import argparse
import importlib
import re
import sys
import traceback
from pathlib import Path

# Allow running this script directly via `python compute/scripts/...`.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compute.lib.independent_verification import (  # noqa: E402
    IndependentVerificationError,
    build_coverage_report,
    registry,
)


LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
PROVED_HERE_RE = re.compile(r"\\ClaimStatusProvedHere")
# Match Conjectured OR Conditional: both are "not-yet-proved" tags whose
# falsifiable predictions can carry @independent_verification decorations.
CONJECTURED_RE = re.compile(r"\\ClaimStatus(?:Conjectured|Conditional)")
# Construction/Definition environments: valid label-bearing definitional
# objects; tests verify properties of the constructed object via disjoint
# inputs.
CONSTRUCTION_BEGIN_RE = re.compile(r"\\begin\{(?:construction|definition)\}")


def _scrape_status_labels(tex_root: Path,
                          status_re: re.Pattern[str]) -> dict[str, list[Path]]:
    """Find every claim with the given status regex and the label it attaches to.

    Heuristic: for each match of status_re, walk BACKWARD through the same
    file looking for the nearest preceding ``\\label{...}`` within 80 lines.
    Theorem/Conjecture environments in Vol III convention put the label
    immediately after ``\\begin{theorem}[...]`` (or ``\\begin{conjecture}[...]``)
    and the ClaimStatus line inside the same environment. 80 lines is
    generous and tolerates inline remarks.

    Returns
    -------
    dict mapping label -> list of files it appears in (usually one).
    """
    search_dirs = [
        tex_root / "chapters",
        tex_root / "appendices",
    ]
    # Also look at working_notes.tex and any top-level .tex in notes/.
    aux_files = []
    wn = tex_root / "working_notes.tex"
    if wn.exists():
        aux_files.append(wn)
    notes_dir = tex_root / "notes"
    if notes_dir.exists():
        aux_files.extend(sorted(notes_dir.glob("*.tex")))

    tex_files: list[Path] = []
    for d in search_dirs:
        if d.exists():
            tex_files.extend(sorted(d.rglob("*.tex")))
    tex_files.extend(aux_files)

    found: dict[str, list[Path]] = {}
    for f in tex_files:
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for idx, line in enumerate(lines):
            if not status_re.search(line):
                continue
            lo = max(0, idx - 80)
            for back in range(idx, lo - 1, -1):
                m = LABEL_RE.search(lines[back])
                if m:
                    label = m.group(1)
                    found.setdefault(label, []).append(f)
                    break
    return found


def scrape_proved_here(tex_root: Path) -> dict[str, list[Path]]:
    """Find every ProvedHere claim and the label it attaches to."""
    return _scrape_status_labels(tex_root, PROVED_HERE_RE)


def scrape_conjectured(tex_root: Path) -> dict[str, list[Path]]:
    """Find every Conjectured claim and the label it attaches to.

    Used to validate ``@independent_verification`` decorations on conjectures
    (which verify falsifiable predictions of a conjecture, not its truth).
    """
    return _scrape_status_labels(tex_root, CONJECTURED_RE)


def scrape_constructions(tex_root: Path) -> dict[str, list[Path]]:
    """Find every \\begin{construction} or \\begin{definition} and its label.

    These environments produce labels that tests can decorate via
    ``@independent_verification`` (the test verifies properties of the
    constructed/defined object via disjoint inputs).

    Heuristic: for each match of CONSTRUCTION_BEGIN_RE, walk FORWARD through
    the same file looking for the nearest following ``\\label{...}`` within
    10 lines (constructions usually put the label immediately after the
    \\begin{...} line).
    """
    search_dirs = [
        tex_root / "chapters",
        tex_root / "appendices",
    ]
    aux_files = []
    wn = tex_root / "working_notes.tex"
    if wn.exists():
        aux_files.append(wn)
    notes_dir = tex_root / "notes"
    if notes_dir.exists():
        aux_files.extend(sorted(notes_dir.glob("*.tex")))

    tex_files: list[Path] = []
    for d in search_dirs:
        if d.exists():
            tex_files.extend(sorted(d.rglob("*.tex")))
    tex_files.extend(aux_files)

    found: dict[str, list[Path]] = {}
    for f in tex_files:
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for idx, line in enumerate(lines):
            if not CONSTRUCTION_BEGIN_RE.search(line):
                continue
            hi = min(len(lines), idx + 10)
            for fwd in range(idx, hi):
                m = LABEL_RE.search(lines[fwd])
                if m:
                    label = m.group(1)
                    found.setdefault(label, []).append(f)
                    break
    return found


def load_test_modules(tests_dir: Path) -> list[tuple[str, BaseException]]:
    """Import every test_*.py under tests_dir to populate the registry.

    Returns a list of (module_name, error) for modules that failed to
    import. An IndependentVerificationError during import means a
    tautological decoration was caught -- we surface those separately.
    """
    failures: list[tuple[str, BaseException]] = []
    if not tests_dir.exists():
        return failures
    for test_file in sorted(tests_dir.glob("test_*.py")):
        # Build an importable dotted path from the repo root.
        rel = test_file.resolve().relative_to(REPO_ROOT)
        module_name = ".".join(rel.with_suffix("").parts)
        try:
            importlib.import_module(module_name)
        except BaseException as exc:  # noqa: BLE001
            failures.append((module_name, exc))
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tex-root", type=Path, default=REPO_ROOT,
        help="Manuscript root (default: repo root)",
    )
    parser.add_argument(
        "--tests-dir", type=Path,
        default=REPO_ROOT / "compute" / "tests",
        help="Directory with test_*.py files",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print every uncovered claim (can be long)",
    )
    parser.add_argument(
        "--show-orphans", action="store_true",
        help="Print every orphan registry entry",
    )
    args = parser.parse_args(argv)

    print(f"[audit] scanning {args.tex_root} for ProvedHere claims...")
    proved_here = scrape_proved_here(args.tex_root)
    print(f"[audit] found {len(proved_here)} ProvedHere-tagged labels.")

    print(f"[audit] scanning {args.tex_root} for Conjectured claims...")
    conjectured = scrape_conjectured(args.tex_root)
    print(f"[audit] found {len(conjectured)} Conjectured-tagged labels.")

    print(f"[audit] scanning {args.tex_root} for Construction/Definition labels...")
    constructions = scrape_constructions(args.tex_root)
    print(f"[audit] found {len(constructions)} Construction/Definition labels.")

    print(f"[audit] importing test modules from {args.tests_dir}...")
    failures = load_test_modules(args.tests_dir)

    # Separate tautological-decoration import failures from real errors.
    tautology_failures: list[tuple[str, IndependentVerificationError]] = []
    other_failures: list[tuple[str, BaseException]] = []
    for name, exc in failures:
        cause = exc
        is_tautology = False
        while cause is not None:
            if isinstance(cause, IndependentVerificationError):
                is_tautology = True
                break
            cause = cause.__cause__ or cause.__context__
        if is_tautology:
            tautology_failures.append((name, cause))  # type: ignore[arg-type]
        else:
            other_failures.append((name, exc))

    if other_failures:
        print(f"[audit] WARNING: {len(other_failures)} test module(s) failed "
              "to import (non-tautology). These are not counted as coverage.")
        for name, exc in other_failures[:5]:
            print(f"         {name}: {type(exc).__name__}: {exc}")

    # Conjectured + Construction/Definition labels both count as valid
    # decoration targets (they're not ProvedHere claims, but they're real
    # mathematical content in the manuscript).
    valid_non_proved = set(conjectured.keys()) | set(constructions.keys())
    report = build_coverage_report(proved_here.keys(), valid_non_proved)

    print()
    print("=" * 72)
    print("INDEPENDENT VERIFICATION COVERAGE")
    print("=" * 72)
    print(report.summary())
    print()

    if tautology_failures:
        print("TAUTOLOGICAL DECORATIONS (blocked at import time):")
        for name, exc in tautology_failures:
            print(f"  - {name}")
            for line in str(exc).splitlines():
                print(f"      {line}")
        print()

    if report.tautological:
        # Should be empty in practice because the decorator raises at import
        # time. Still report for completeness in case someone bypasses.
        print("TAUTOLOGICAL REGISTRY ENTRIES (check decorator path):")
        for e in report.tautological:
            print(f"  - {e.claim}  [{e.test_qualname}]")
        print()

    if report.orphan_entries:
        print(f"ORPHAN REGISTRY ENTRIES ({len(report.orphan_entries)}): "
              "test decorates a claim label not found in any .tex as ProvedHere")
        if args.show_orphans:
            for e in report.orphan_entries:
                print(f"  - {e.claim}  [{e.test_qualname}]")
        else:
            for e in report.orphan_entries[:5]:
                print(f"  - {e.claim}  [{e.test_qualname}]")
            if len(report.orphan_entries) > 5:
                print(f"  ... and {len(report.orphan_entries) - 5} more "
                      "(use --show-orphans to see all)")
        print()

    if args.verbose and report.uncovered_claims:
        print(f"UNCOVERED CLAIMS ({len(report.uncovered_claims)}):")
        for c in sorted(report.uncovered_claims):
            files = proved_here.get(c, [])
            loc = files[0].relative_to(args.tex_root) if files else "<?>"
            print(f"  - {c}    ({loc})")
        print()

    # Exit status: fail on tautology or orphan; coverage gap is a metric, not
    # a gate (enforcing a coverage floor would incentivize low-quality tests).
    fail = bool(tautology_failures) or bool(report.orphan_entries) \
        or bool(report.tautological)
    if fail:
        print("AUDIT RESULT: FAIL "
              "(tautological decoration or orphan entry present)")
        return 2
    print("AUDIT RESULT: PASS (no tautologies, no orphans)")
    print(f"           coverage gap: {len(report.uncovered_claims)} claims "
          "without independent verification -- address incrementally")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
