"""Metadata guards for the Vol III frontier obstruction normal form."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLAIMS = ROOT / "metadata" / "claims.jsonl"


def _claims_by_label() -> dict[str, dict[str, object]]:
    claims: dict[str, dict[str, object]] = {}
    with CLAIMS.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            claim = json.loads(line)
            label = claim.get("label")
            if isinstance(label, str):
                claims[label] = claim
    return claims


def test_frontier_normal_form_is_inscribed_as_proved_guard() -> None:
    claims = _claims_by_label()
    claim = claims["thm:frontier-obstruction-normal-form"]
    assert claim["status"] == "ProvedHere"
    assert claim["file"] == "chapters/theory/cy_to_chiral.tex"


def test_cy_c_six_route_cycle_remains_conditional_until_maps_exist() -> None:
    claims = _claims_by_label()
    conditional_labels = {
        "thm:six-routes-isomorphism",
        "prop:route1-route2-bridge",
        "prop:route2-route3-bridge",
        "prop:route3-route4-bridge",
        "prop:route4-route5-bridge",
        "prop:route5-route6-bridge",
        "prop:route6-route1-closure",
        "prop:cy-c-bridge-obligations",
        "thm:pairwise-all-proved-closes-CY-C",
        "conj:harvey-moore-functorial",
    }
    assert {label: claims[label]["status"] for label in conditional_labels} == {
        label: "Conditional" for label in conditional_labels
    }
    assert claims["conj:cy-c-i3-half-bps"]["status"] == "Conjectured"


def test_compact_and_higher_dimensional_frontiers_are_not_silently_upgraded() -> None:
    claims = _claims_by_label()
    expected = {
        "prop:quintic-shadow-coefficients": "Conditional",
        "thm:cy-to-chiral-d3": "Conditional",
        "thm:phi3-witnessed-kernel-functoriality": "Conditional",
        "prop:phi3-arbitrary-morphism-obstruction-criterion": "Conditional",
        "conj:phi-d-functoriality": "Conjectured",
        "thm:phi-platonic": "Conditional",
        "thm:fake-monster-d5-bialgebra": "Conditional",
        "thm:phi-4-k3-k3-kunneth-explicit": "Conditional",
        "thm:phi-4-twist-classification": "Conditional",
        "thm:thy-fibration-borcherds-shadow": "Conditional",
    }
    assert {label: claims[label]["status"] for label in expected} == expected


def test_quantum_group_frontiers_keep_their_open_statuses() -> None:
    claims = _claims_by_label()
    expected = {
        "thm:Yfg-resurgent-Drinfeld-twist-non-simply-laced": "Conditional",
        "conj:zte-drinfeld-twist-completion": "Conjectured",
        "conj:osp-yangian-mukai": "Conjectured",
        "conj:k3-super-yangian": "Conjectured",
        "conj:k3e-shadow-pf": "Conjectured",
        "conj:k3e-shadow-rademacher": "Conjectured",
        "thm:k3-mock-modular-proof": "Conditional",
    }
    assert {label: claims[label]["status"] for label in expected} == expected
