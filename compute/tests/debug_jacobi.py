"""Diagnostic: locate the failing super-Jacobi triples."""
from __future__ import annotations
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent.parent / "lib"
sys.path.insert(0, str(_LIB))

from k3_yangian_jacobi_closure_sl2 import (
    COH_DIM, GEN_DIM, PARITY, TOTAL, _super_jacobi, _parity_of,
)
from itertools import combinations


failures_twisted = []
failures_plain = []
for trip in combinations(range(TOTAL), 3):
    r = _super_jacobi(*trip, twisted=True)
    if not r.is_zero():
        failures_twisted.append((trip, r.terms))
    r2 = _super_jacobi(*trip, twisted=False)
    if not r2.is_zero():
        failures_plain.append((trip, r2.terms))

print(f"twisted failures: {len(failures_twisted)}")
print(f"plain failures:   {len(failures_plain)}")

# Classify twisted failures by generator structure
print("\nFirst 10 twisted failures with decomposition:")
for (trip, terms) in failures_twisted[:10]:
    coords = []
    for gen in trip:
        if gen == GEN_DIM:
            coords.append(("c", "c"))
        else:
            a, i = divmod(gen, COH_DIM)
            parity_name = "odd" if PARITY[i] == 1 else "even"
            coords.append((["E","F","H"][a], f"i={i}({parity_name})"))
    print(f"  triple {trip} = {coords}")
    print(f"    terms: {terms[:3]}")

# Check whether all failures share a pattern
print("\nParity distribution of twisted failures:")
par_dist = {}
for (trip, _) in failures_twisted:
    parities = tuple(sorted([_parity_of(g) for g in trip]))
    par_dist[parities] = par_dist.get(parities, 0) + 1
print(par_dist)

# Do any failures involve central element?
with_central = sum(1 for (t, _) in failures_twisted if GEN_DIM in t)
print(f"twisted failures with central: {with_central}")

# How many purely in g (x) H^2^3?
pure_h2 = 0
for (trip, _) in failures_twisted:
    if GEN_DIM in trip:
        continue
    idxs = [g % COH_DIM for g in trip]
    if all(1 <= i <= 22 for i in idxs):
        pure_h2 += 1
print(f"twisted failures purely on H^2^3 sector: {pure_h2}")
