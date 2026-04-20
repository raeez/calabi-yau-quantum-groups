"""Pytest configuration for compute tests."""

import sys
from pathlib import Path

# Add repo root to sys.path so 'compute.lib' imports resolve when running
# pytest from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# Also add compute/lib on sys.path so modules with bare sibling imports
# (Wave-2 through Wave-5) resolve without the ``compute.lib.`` prefix.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))


def pytest_addoption(parser):
    """Add --run-slow flag for opt-in heavy smoke tests (Wave 5 main())."""
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="Run slow regression tests (multi-minute tensor scans).",
    )
