"""Pytest configuration for compute tests."""

import sys
from pathlib import Path

# Add repo root to sys.path so 'compute.lib' imports resolve when running
# pytest from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
