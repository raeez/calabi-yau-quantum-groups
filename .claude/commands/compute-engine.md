---
description: "Scaffold a new Vol III compute engine"
---

# New Compute Engine — Vol III

**Engine name/topic**: $ARGUMENTS

Same protocol as Vol I `/compute-engine`. Vol III compute modules live at `~/calabi-yau-quantum-groups/compute/`.

### Vol III-specific engine patterns
- CY category cyclic structure computations
- Borcherds product / denominator identity verification
- Quantum group R-matrix at roots of unity
- E_2-chiral algebra operations
- Drinfeld center computations
- K3/elliptic curve lattice shadow data
- Motivic DT invariant comparisons

### Convention discipline (AP49)
Vol III uses motivic/categorical conventions. When importing formulas from Vol I (OPE modes) or Vol II (lambda-brackets), include explicit conversion functions in the engine and test the conversion itself.

### Test standard
```bash
cd ~/calabi-yau-quantum-groups && python3 -m pytest compute/tests/test_{name}_engine.py -v
```

Minimum 30 tests, 3 verification paths per formula.
