---
description: "Deep Beilinson audit for Vol III"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Deep Beilinson Audit — Vol III

**Target**: $ARGUMENTS

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

Same protocol as Vol I `/audit`. Vol III-specific:

Key audit targets:
1. CY-A scope: proved for d=2 ONLY. d=3 is conditional on chain-level S^3-framing.
2. CY-B, CY-C, CY-D: verify theorem vs conjecture status matches LaTeX environment (AP40)
3. G(X) usage: must have formal definition (AP43)
4. CoHA identification: conditional on G(X) existence (AP-CY7)
5. All cross-volume citations: convention compatibility (AP49)
6. Borcherds products: source convention documented (AP38)

Build: `cd ~/calabi-yau-quantum-groups && make fast`
Tests: `cd ~/calabi-yau-quantum-groups && python3 -m pytest compute/tests/ -x --tb=short -q`
