# Agent B5 YBE Compute Integration Audit

Date: 2026-04-24 SAST

## Scope

Audited files:

- `compute/lib/k3_hcs_6d_oneloop.py`
- `compute/lib/k3_hcs_6d_twoloop.py`
- `compute/lib/k3_hcs_6d_threeloop.py`
- `compute/lib/k3_hcs_6d_fourloop.py`
- `compute/tests/test_k3_hcs_6d_oneloop.py`
- `compute/tests/test_k3_hcs_6d_twoloop.py`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A5_ybe_oneloop_repair.md`

Instruction: report only.  No audited compute source or test file was edited.

## Verdict

The loop-filtration story is now internally consistent as a compute story:

1. The old fish term

   ```text
   R_fish(s) = (12 + c_v/2) hbar^2 P / s^2
   ```

   has an order-`hbar^3` YBE obstruction

   ```text
   ((12 + c_v/2)/(u v (u-v))) * (P12 P23 - P23 P12).
   ```

2. The repaired one-loop rational Yang model is the coupling-normalisation
   tangent

   ```text
   hbar_eff = hbar + (12 + c_v/2) hbar^2,
   R_tree(s; hbar_eff)
     = R_tree(s; hbar) + (12 + c_v/2) hbar^2 (P - I)/s + O(hbar^3).
   ```

   This kills the order-`hbar^3` obstruction in the rational Yang model.

3. The legacy two-loop sunset ansatz remains false after `CT_1`: its exact
   linearized obstruction at order `hbar^5` is nonzero.

4. The three- and four-loop files do not certify restoration.  They are
   explicitly diagnostic and report inherited lower-order obstruction:
   `legacy-hbar^3; after-CT1-hbar^5`.

Thus a two-loop, three-loop, or four-loop YBE theorem is not currently proved.
The repaired theorem-grade statement is only the one-loop rational Yang
normalisation statement, plus the negative oracle for the old sunset ansatz.

## Evidence

### One Loop

`compute/lib/k3_hcs_6d_oneloop.py` correctly separates the negative and repaired
objects:

- lines 224-227: `P/u^2` is explicitly not YBE-admissible and is kept as a
  negative oracle.
- lines 238-245: `k3_yang_one_loop_shift(c_v) = 12 + c_v/2` and
  `hbar_eff = hbar + c hbar^2`.
- lines 248-271: the repaired tangent is
  `c hbar^2 (P - I)/u`.
- lines 279-281: the exact control object is the normalized Yang matrix
  `R_tree_rational(u, hbar_eff, N)`.
- lines 342-366: `ybe_at_order` reports old-fish failure, repaired tangent
  order `hbar^4`, exact Yang-family YBE, and the caveat that the hCS integral
  derivation remains open.

`compute/tests/test_k3_hcs_6d_oneloop.py` gives independent checks:

- lines 82-96 prove the exact old-fish `hbar^3` commutator coefficient.
- lines 98-100 prove the Yang tangent kills the `hbar^3` coefficient.
- lines 103-113 check exact Yang-family YBE at `sl2` and `sl3`.
- lines 116-128 check the formal tangent is the first-order term of exact
  renormalisation.
- lines 130-148 check the tangent residual starts at `hbar^4`, not `hbar^3`.

### Two Loops

`compute/lib/k3_hcs_6d_twoloop.py` is consistent with the repaired filtration:

- lines 8-17 reject the historical two-loop YBE-preserving claim because the
  legacy ansatz still has an order-`hbar^3` one-loop obstruction.
- lines 19-28 record the correct one-loop normalisation and the residual
  nonzero `hbar^5` obstruction for the legacy sunset ansatz after `CT_1`.
- lines 371-432 compute the exact `S_3` group-algebra obstruction and its
  normalisation cure.
- lines 457-495 compute the exact `hbar^5` obstruction of the old sunset ansatz
  after `CT_1`.
- lines 498-523 give the numerical legacy two-loop diagnostic after exact
  one-loop normalisation.
- lines 688-695 keep `R_twoloop_YBE` only as a backward-compatible name and
  state that it is not known to preserve YBE.
- lines 718-808 make `ybe_at_hbar5` a negative oracle, returning
  `residual_order_detected = "hbar^3"` in the legacy path and
  `two_loop_hbar5_restored_after_CT1 = False`.

`compute/tests/test_k3_hcs_6d_twoloop.py` directly tests the story:

- lines 31-44: the current two-loop probe is `hbar^3`, not `hbar^5`.
- lines 47-88: exact `hbar^3` commutator coefficient.
- lines 91-107: exact Yang-coupling renormalisation satisfies YBE.
- lines 109-146: exact `CT_1` identity and one-loop normalized YBE.
- lines 149-177: old sunset after `CT_1` still has nonzero `hbar^5`
  obstruction and rejects the advertised theorem.

### Three and Four Loops

`compute/lib/k3_hcs_6d_threeloop.py` does not certify restoration:

- lines 20-27: three-loop module is an ansatz diagnostic, not a certified
  YBE-restoration oracle.
- lines 347-369: `R_threeloop_YBE` and `R_full_through_threeloop` are explicitly
  backward-compatible names inheriting lower-order obstruction.
- lines 464-523: `ybe_at_hbar7` reports
  `legacy-hbar^3; after-CT1-hbar^5`,
  `three_loop_verification_passed = False`, and filtration impossibility for
  an `hbar^6` counterterm to cancel lower defects.

`compute/lib/k3_hcs_6d_fourloop.py` also does not certify restoration:

- lines 15-21: four-loop module is a coefficient/ansatz diagnostic, not a
  certified YBE-restoration oracle.
- lines 529-538: `R_full_through_fourloop` inherits lower-order obstruction and
  is not certified.
- lines 653-707: `ybe_at_hbar9` reports
  `legacy-hbar^3; after-CT1-hbar^5` and
  `four_loop_counterterm_can_cancel_lower_residual = False`.

## Remaining Reader-Risk

The filtration story is repaired, but several historical/source-origin phrases
remain too strong if read as hCS derivations rather than rational-Yang
diagnostics:

- `compute/lib/k3_hcs_6d_threeloop.py:9` says `CT_1` is
  `[proved from FA1-FA4]`.  This conflicts with the A5 caveat that the hCS
  Feynman derivation of `CT_1` is not proved in the compute lane.
- `compute/lib/k3_hcs_6d_twoloop.py:95-101` still narrates an extraction of
  the historical `CT_1` from the factorisation axiom; the executable repair is
  instead the exact Yang normalisation identity.
- `compute/lib/k3_hcs_6d_twoloop.py:745-748` contains a stale comment about an
  approximated one-loop YBE counterterm.  The function now returns the correct
  exact-normalisation diagnostics, so this is a comment-level risk, not a test
  failure.

These are not contradictions in the active diagnostic outputs, but they should
be cleaned before manuscript prose cites these modules as hCS-derived
counterterm evidence.

## Verification Run

Targeted pytest:

```bash
python3 -m pytest compute/tests/test_k3_hcs_6d_oneloop.py compute/tests/test_k3_hcs_6d_twoloop.py -q
```

Result:

```text
14 passed in 0.21s
```

Direct diagnostic calls:

```bash
PYTHONPATH=compute/lib python3 - <<'PY'
from k3_hcs_6d_oneloop import ybe_at_order
from k3_hcs_6d_twoloop import ybe_at_hbar5, ybe_twoloop_after_one_loop_normalization
from k3_hcs_6d_threeloop import ybe_at_hbar7
from k3_hcs_6d_fourloop import ybe_at_hbar9

print('one_loop', ybe_at_order(N=2, c_v=2.0, hbar=1e-3)['naive_fish_ybe_preserved_at_hbar3'], ybe_at_order(N=2, c_v=2.0, hbar=1e-3)['renormalized_yang_exact_ybe'])
print('two_loop_legacy', ybe_at_hbar5(N=2, c_v=2.0, dim_g=3.0, hbar=1e-4)['residual_order_detected'])
print('two_loop_after_CT1', ybe_twoloop_after_one_loop_normalization(N=2, c_v=2.0, dim_g=3.0)['two_loop_hbar5_restored'])
print('three_loop', ybe_at_hbar7(N=2, c_v=2.0, dim_g=3.0)['residual_order_detected'], ybe_at_hbar7(N=2, c_v=2.0, dim_g=3.0)['three_loop_verification_passed'])
print('four_loop', ybe_at_hbar9(N=2, c_v=2.0, dim_g=3.0)['residual_order_detected'], ybe_at_hbar9(N=2, c_v=2.0, dim_g=3.0)['four_loop_counterterm_can_cancel_lower_residual'])
PY
```

Result:

```text
one_loop False True
two_loop_legacy hbar^3
two_loop_after_CT1 False
three_loop legacy-hbar^3; after-CT1-hbar^5 False
four_loop legacy-hbar^3; after-CT1-hbar^5 False
```

Syntax check:

```bash
python3 -m py_compile compute/lib/k3_hcs_6d_oneloop.py compute/lib/k3_hcs_6d_twoloop.py compute/lib/k3_hcs_6d_threeloop.py compute/lib/k3_hcs_6d_fourloop.py
```

Result: passed with no output.

## Status Recommendation

Keep the K3 hCS YBE lane at:

```text
Proved/computed: one-loop rational Yang normalization repairs the hbar^3 YBE obstruction.
Computed negative oracle: naive fish has hbar^3 obstruction.
Computed negative oracle: legacy sunset has nonzero hbar^5 obstruction after CT_1.
Conditional/open: hCS Feynman derivation of CT_1 and a genuine two-loop repair.
Not proved: three-loop and four-loop YBE restoration.
```
