"""Source guard for the Bar-Cobar Bridge label surface."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
BAR_COBAR = REPO_ROOT / "chapters/connections/bar_cobar_bridge.tex"


def test_bi_based_labels_exist_on_source_surface() -> None:
    text = BAR_COBAR.read_text(encoding="utf-8")

    assert r"\label{sec:bar-cobar-bi-based-k3e}" in text
    assert r"\label{def:bar-cobar-bi-based-ran-datum}" in text


def test_local_cy_parenthetical_closes_before_comma() -> None:
    text = BAR_COBAR.read_text(encoding="utf-8")

    assert r"conifold\textup{), the toric" not in text
    assert r"conifold\textup{)}, the toric" in text
