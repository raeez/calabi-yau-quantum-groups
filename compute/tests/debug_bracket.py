"""Diagnostic: where does the bracket term fail?"""
from __future__ import annotations
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent.parent / "lib"
sys.path.insert(0, str(_LIB))

from k3_yangian_jacobi_closure_sl2 import (
    COH_DIM, CENTRAL, PARITY, TOTAL, _super_jacobi, _split_bracket_central,
)
from itertools import combinations


failures = []
for trip in combinations(range(TOTAL), 3):
    r = _super_jacobi(*trip, twisted=True)
    bt, cc = _split_bracket_central(r)
    if not bt.is_zero():
        failures.append((trip, bt.terms))

print(f"twisted bracket-term failures: {len(failures)}")

# Show first 10 with decomposition
for (trip, terms) in failures[:10]:
    coords = []
    for gen in trip:
        if gen == CENTRAL:
            coords.append(("c", "c"))
        else:
            a, i = divmod(gen, COH_DIM)
            coords.append((["E","F","H"][a], i))
    # Decode output terms
    out_coords = []
    for (idx, coef) in terms:
        if idx == CENTRAL:
            out_coords.append(("c", coef))
        else:
            a, i = divmod(idx, COH_DIM)
            out_coords.append((["E","F","H"][a], i, coef))
    print(f"  triple {trip} = {coords}")
    print(f"    bracket output: {out_coords}")

# Classify by cohomology structure
print("\nCohomology pattern distribution:")
dist = {}
for (trip, _) in failures:
    coh_idx = tuple(sorted([g % COH_DIM for g in trip if g != CENTRAL]))
    dist[coh_idx] = dist.get(coh_idx, 0) + 1
for key, val in sorted(dist.items()):
    print(f"  coh_indices={key}: {val}")
