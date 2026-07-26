# Vol III Compute Verification Surface

This file is an index to the executable verification layer. It is not a
proof ledger and does not assert global theorem coverage.

Live lower bounds are recorded in `appendices/engine_catalogue.tex` and
guarded by `compute/tests/test_verification_surface_sanity.py`:

| Predicate | Lower bound |
|---|---:|
| `compute/lib/*.py` modules | 470 |
| `compute/tests/test_*.py` files | 500 |
| statically declared `test_*` functions | 1088 |
| `compute/scripts/` verification scripts | 4 |
| `compute/audit/` reports | 7 |

The static test-function count is intentionally conservative. Pytest
parametrisation may expand the collected cases on a given machine, but
no manuscript claim should cite a global expanded-test count. A
computational citation should name the engine or test, the finite object
being evaluated, and the comparison map that connects that finite object
to the surrounding theorem.

Core engine families include holomorphic Chern--Simons comparison,
K3/Yangian and K3 x E witnesses, bar--cobar and shadow-tower engines,
CoHA/Drinfeld-centre checks, Borcherds denominator normalisation, and
compact Hall recognition gates. The complete source of truth is the
`compute/lib/` and `compute/tests/` tree.
