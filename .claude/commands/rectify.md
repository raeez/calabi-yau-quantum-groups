---
description: "Beilinson rectification loop on a Vol III chapter"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Beilinson Rectification Loop — Vol III

**Target**: $ARGUMENTS

Read CLAUDE.md (Vol III) before beginning. All Vol I/II anti-patterns apply. Vol III-specific: AP-CY1 through AP-CY8. The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

## Key Vol III constraints

- **AP-CY6**: A_X for CY3 does NOT exist. CY-A proved only for d=2.
- **AP-CY7**: CoHA is associative, NOT E1-chiral. Identification requires G(X) existence.
- **AP-CY8**: Borcherds denominator != bar Euler product (requires CY-to-chiral functor).
- **AP43**: G(X) must have formal definition before use.
- **AP49**: Vol III uses motivic/categorical conventions. NEVER paste from Vol I/II without conversion.

### Build
```bash
pkill -9 -f pdflatex; sleep 2; cd ~/calabi-yau-quantum-groups && make fast
```

### Phases 1-4
Same as Vol I `/rectify`. This volume is younger and more conjectural — be especially vigilant about AP36 (biconditional overclaims) and AP40 (theorem env for conjectures).

CONVERGE before stopping.
