# Agent 06 Integration Verification Attack, Wave 2

Date: 2026-04-24.

Scope read: `chapters/theory/bps_positive_geometry_closure.tex`,
`compute/lib/bps_positive_truncation.py`,
`compute/tests/test_bps_positive_truncation.py`, `main.tex`,
and the existing BPS-positive synthesis notes.  Write scope honored:
only this note was changed.

Verdict: the wave-1 repair correctly separates zero-fiber schema from
constructed points.  The remaining defects are sharper: the finite oracle
does not yet falsify non-Hall-lower truncations or quotient-zeroing
associativity, one `ProvedHere` corollary lacks a proof body, and the
pro-completion / relative-orientation hypotheses need to be made
executable rather than only stated.

## Verification Commands Run

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_bps_positive_truncation.py

32 passed in 0.95s
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from compute.lib.bps_positive_truncation import *
b=TruncationBound(N=4,R_num=4)
print(derived_solution_stack_certificate(b).passed,
      derived_solution_stack_certificate(b).exact)
print(constructed_named_points_certificate(b).passed,
      constructed_named_points_certificate(b).exact,
      len(constructed_named_points_certificate(b).discrepancies))
for f in derived_solution_stack_factors(b):
    print(f.name, f.certificate.exact, f.obstruction.computed, f.solved)
print(seven_extension_resolution_certificate(b).passed,
      seven_extension_resolution_certificate(b).exact)
PY

derived True True
constructed_points False False 5
compact_nontoric_bms True True True
quintic_excert False False False
schoen_banana_gluing False False False
k3e_raw_radical False False False
theta_comparison False False False
hcs_named_zero_fiber False False False
seven True False
```

```text
rg -n -P '\\kappa(?!_)|bare kappa|bare \\kappa' \
  chapters/theory/bps_positive_geometry_closure.tex \
  compute/lib/bps_positive_truncation.py \
  compute/tests/test_bps_positive_truncation.py \
  main.tex \
  notes/bps_positive_geometry_total_resolution_20260424/platonic_closure_20260424.md \
  notes/bps_positive_geometry_total_resolution_20260424/seven_extension_resolution_20260424.md

no hits
```

```text
rg -n '\b(Wave|round|batch|AP-CY|Pattern|cache entry|notably|crucially|moreover|furthermore|let us now|we now turn|having established)\b' \
  chapters/theory/bps_positive_geometry_closure.tex

no hits
```

Full `make fast` was not run in this lane because this agent's write
surface was restricted to a note and the build writes shared auxiliary
and PDF surfaces during concurrent work.  Manuscript inclusion was
source-checked at `main.tex:1821`.

## Attack 1 -> Heal: Hall-lower certificate is tautological

Defect.  `finite_lower_set_certificate()` only loops over retained
charges as both summands.  Therefore the condition
`if alpha not in charges or beta not in charges` can never fire, and
the function cannot detect a retained charge whose positive HN summands
were omitted from the ambient visible monoid.

Concrete falsifier run:

```text
retain gamma=(1,1), omit (1,0) and (0,1)
finite_lower_set_certificate passes=True checked=0 discrepancies=()
```

Anchors:
`compute/lib/bps_positive_truncation.py:795`,
`compute/tests/test_bps_positive_truncation.py:111`,
`chapters/theory/bps_positive_geometry_closure.tex:50`.

Heal.  Replace the certificate signature by an ambient-aware predicate:

```python
finite_lower_set_certificate(retained, ambient_visible_monoid)
```

For every retained `gamma` and every decomposition
`gamma = alpha + beta` in the ambient active monoid with positive HN
summands, assert `alpha,beta in retained`.  Add a negative test retaining
only `(1,1)` while the ambient set contains `(1,0),(0,1),(1,1)`, and
assert the certificate fails.

## Attack 2 -> Heal: quotient-zeroing associativity is under-tested

Defect.  `hall_associativity_certificate()` checks only triples for
which `alpha+beta`, `beta+gamma`, and `alpha+beta+gamma` are all
retained.  That skips exactly the boundary cases where zeroing outside
the finite quotient can break associativity if the complement is not a
two-sided Hall ideal.

Concrete falsifier run:

```text
retained charges: (1,0), (0,1), (1,1), (2,1)
omitted charge: (2,0)
certificate passes=True checked=1 discrepancies=()
(a*a)*c = 0 because (2,0) is omitted
a*(a*c) = 1 because (2,1) is retained
```

Anchors:
`compute/lib/bps_positive_truncation.py:448`,
`compute/lib/bps_positive_truncation.py:324`,
`chapters/theory/bps_positive_geometry_closure.tex:146`.

Heal.  Either require the ambient-aware lower-set certificate before
associativity is asserted, or test all retained triples by actually
comparing the two quotient products, including cases where one
intermediate product is zero.  Add a negative test using the four-charge
falsifier above.

## Attack 3 -> Heal: `ProvedHere` corollary lacks proof body

Defect.  Every `ProvedHere` theorem/proposition in the new chapter has a
proof except `cor:bps-positive-theta-comparison`.

Script result:

```text
424 \begin{corollary}[Comparison packages] end 436 proof_after=False
```

Anchors:
`chapters/theory/bps_positive_geometry_closure.tex:424`,
`chapters/theory/bps_positive_geometry_closure.tex:440`.

Heal.  Insert a proof immediately after the corollary:
the external package gives a second finite parallel-transport system;
the ratio with the intrinsic Hall KS transport is a Cech cocycle valued
in finite quantum-torus automorphisms; vanishing of the package
existence vector and comparison cocycle gives equality of theta elements
and multiplication constants; equality of packages forces the cocycle
to be zero; transition compatibility gives the pro-object statement.

## Attack 4 -> Heal: hCS orientation class is stated absolutely

Defect.  The hCS theorem requires
`o_or=0` and identifies it as the orientation square-root Cech class.
The finite orientation oracle deliberately permits gerbe-twisted
orientation output.  Therefore the hCS obstruction must be relative to
the chosen Hall orientation coefficient system, not absolute triviality
of the square-root gerbe.

Anchors:
`chapters/theory/bps_positive_geometry_closure.tex:350`,
`chapters/theory/bps_positive_geometry_closure.tex:353`,
`compute/lib/bps_positive_truncation.py:128`,
`compute/tests/test_bps_positive_truncation.py:80`.

Heal.  Rename the hCS coordinate in theorem, code, and tests from an
absolute `o_or` to a relative orientation-compatibility class:

```text
o_or^rel = 0 in the torsor of coefficient systems over the chosen
orientation output o.
```

Add a test with a nontrivial but closed orientation Cech class and assert
that the hCS ledger asks for relative compatibility, not absolute
trivialization.

## Attack 5 -> Heal: pro-completion exactness is not executable

Defect.  The manuscript now names cofinal Mittag-Leffler towers and
closed quotient maps, but the oracle only checks isolated bounds.  It
does not test transition compatibility from `N=3` to `N=4`, preservation
of Hall multiplication under restriction, theta generator compatibility,
or obstruction-vector functoriality.

Anchors:
`chapters/theory/bps_positive_geometry_closure.tex:109`,
`chapters/theory/bps_positive_geometry_closure.tex:163`,
`chapters/theory/bps_positive_geometry_closure.tex:648`,
`compute/tests/test_bps_positive_truncation.py:340`.

Heal.  Add a `transition_certificate(bound_small, bound_big)` checking:
surjective quotient/restriction on retained charges, Hall product
compatibility after restriction, compatibility of theta transports, and
restriction of obstruction vectors.  The theorem should cite this as the
finite oracle for ML/separatedness rather than relying on single-bound
tests.

## Attack 6 -> Heal: exact-false ledgers no longer solve points, but the aggregate can still be misread

Result.  The wave-1 defect is healed in code: `SolutionStackFactor.solved`
requires `certificate.exact`, `certificate.passed`, and computed
vanishing obstruction.  The runtime inspection shows only
`compact_nontoric_bms` is solved; the five named residual factors are
closed substacks and not points.  `constructed_named_points_certificate`
correctly fails with five discrepancies.

Anchors:
`compute/lib/bps_positive_truncation.py:297`,
`compute/lib/bps_positive_truncation.py:1031`,
`compute/tests/test_bps_positive_truncation.py:320`,
`compute/tests/test_bps_positive_truncation.py:348`.

Heal.  Add one guard test asserting that no consumer may infer named
point construction from `seven_extension_resolution_certificate`, since
that aggregate is `passed=True` but `exact=False`.  The aggregate proves
typed schema coherence; the constructed-points certificate is the only
point-realization gate.

## Attack 7 -> Heal: full radical and finite oracle coverage are not yet direct

Defect.  The raw `K3 x E` factor now uses the full Hall-Borcherds
radical ledger, which is correct.  But the direct function
`full_hall_borcherds_radical_certificate()` is not imported or tested by
name; coverage reaches it only through `derived_solution_stack_factors`.
The finite Gram routine is separately tested, but no test prevents a
future reintroduction of a toy Gram matrix as the raw theorem.

Anchors:
`compute/lib/bps_positive_truncation.py:868`,
`compute/lib/bps_positive_truncation.py:938`,
`compute/tests/test_bps_positive_truncation.py:225`.

Heal.  Import `full_hall_borcherds_radical_certificate` directly in the
test file and assert `exact=False`, seven-coordinate theorem target
language, and Igusa source inheritance.  Keep
`radical_non_degeneracy_certificate()` only as a finite linear-algebra
primitive, never as the named `K3 x E` theorem.

## Attack 8 -> Heal: manuscript inclusion is present, but the frontier boundary needs one sentence

Result and defect.  The chapter is included:

```text
main.tex:1821 \input{chapters/theory/bps_positive_geometry_closure}
```

Immediately afterward, Part VII resumes with frontier obligations and
mentions the quintic as a non-formal CY3 construction obligation at
`main.tex:1848`.  This is not false, but without a transition sentence a
reader can confuse the post-closure classification frontier with the
closed-substack point-construction obligations of the BPS-positive
chapter.

Heal.  Insert after `main.tex:1821`:

```tex
The following frontier table concerns stage-two and classification
refinements after the chambered BPS positive geometry source object has
been constructed; the quintic, Schoen, raw \(K3\times E\), theta, and
hCS issues above are named closed substacks of \(\Sol^{\BPS}\), not
missing foundations.
```

## Files Changed

Only:

```text
notes/bps_positive_geometry_total_resolution_20260424/agent_attacks_wave2_20260424/agent_06_integration_verification.md
```

## Shortest Exact Remaining List

1. Make the lower-set and associativity certificates ambient-aware and
   add the two falsifier tests above.
2. Add the missing proof body for
   `cor:bps-positive-theta-comparison`.
3. Replace absolute hCS orientation triviality by relative orientation
   compatibility over the chosen orientation output.
4. Add transition/pro-completion certificates for ML, separatedness, and
   obstruction restriction.
5. Add direct test coverage for
   `full_hall_borcherds_radical_certificate`.
6. Add the Part VII transition sentence after the BPS-positive chapter
   inclusion.

