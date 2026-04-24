# Agent 19: K3 hCS two-loop/YBE red flag

## Claim inspected

Object: `compute/lib/k3_hcs_6d_twoloop.py`, the K3 x E 6d hCS two-loop sunset/counterterm lane.

Claim under attack: the two-loop corrected R-matrix
`R_tree + hbar^2 R_1,YBE + hbar^4 R_2,YBE` is YBE-restoring at order
`hbar^5`, with direct support from `ybe_at_hbar5` for `sl2` and `sl3`.

## Compute anchors

- `compute/lib/k3_hcs_6d_twoloop.py:87`-`93`: module docstring claims
  `tree + 1-loop-YBE + 2-loop-YBE` has YBE residual near machine precision.
- `compute/lib/k3_hcs_6d_twoloop.py:270`-`283`: `R_twoloop_counterterm`
  is advertised as YBE-restoring, but the numeric implementation uses the
  leading Fierz-diagonal approximation
  `t tensor t ~ (h^v / dim_g) * Id`.
- `compute/lib/k3_hcs_6d_twoloop.py:296`-`309`:
  `R_twoloop_YBE` and `R_full_through_twoloop` name the result
  "YBE-preserving".
- `compute/lib/k3_hcs_6d_twoloop.py:318`-`385`: `ybe_at_hbar5` defines the
  actual oracle. It returns `two_loop_verification_passed =
  abs(res_2loop_YBE) < 10*hbar**5`.
- `compute/lib/k3_hcs_6d_twoloop.py:362`-`364`: the direct oracle discards
  the supplied `dim_g` and calls `R_full_through_twoloop(...,
  dim_g=float(max(N, 1)))`. Thus the `sl3` probe is not using
  `dim_g=8`; the output also reports `dim_g_approx` at line `377`.
- `compute/lib/k3_hcs_6d_twoloop.py:579`-`590`: `run_all_wave3` records
  `sunset_gauge_sl2`, `sunset_gauge_sl3`, `A2_sl2`, `A2_sl3`,
  `ybe5_sl2`, and `ybe5_sl3`.
- `compute/lib/k3_hcs_6d_threeloop.py:108`-`116` and
  `compute/lib/k3_hcs_6d_fourloop.py:129`-`137`: later loop modules import
  `R_twoloop_YBE` and `R_full_through_twoloop`, so this red flag propagates
  upward into the three- and four-loop tower.
- `compute/lib/k3_yangian_costello_fiveloop.py:147`-`161`: the later audit
  already classifies `k3_hcs_6d_twoloop.py` as an ansatz surface: Fierz
  diagonal substitution, no `H^1_{hbar^4}(Def_BV)` computation, no proof
  that the counterterm exhausts `H^1`, and no non-Fierz BRST check.

Compute tests surface:

- No `compute/tests` file mentions `k3_hcs_6d_oneloop`,
  `k3_hcs_6d_twoloop`, `k3_hcs_6d_threeloop`, or
  `k3_hcs_6d_fourloop`.
- No `compute/tests` file mentions `two_loop_verification_passed`,
  `ybe_at_hbar5`, `R_twoloop_YBE`, or this K3 hCS two-loop lane.

## Probes run

Commands:

```bash
rg -n "k3_hcs_6d_twoloop|two_loop_verification_passed|hbar5|ybe_at_hbar5|R_twoloop_YBE|sunset_gauge_sl2|sunset_gauge_sl3|A2_sl2|A2_sl3|ybe5_sl2|ybe5_sl3" compute/lib compute/tests
rg -n "k3_hcs_6d_oneloop|k3_hcs_6d_twoloop|k3_hcs_6d_threeloop|k3_hcs_6d_fourloop" compute/tests
rg -n "k3_hcs_6d_twoloop|two_loop_verification_passed|ybe_at_hbar5|R_twoloop_YBE|hbar5|K3 hCS|hCS two-loop|two-loop/YBE|two-loop YBE|YBE-restoring|YBE preserving|YBE-preserving" chapters notes main.tex working_notes.tex
python3 - <<'PY'
import json, sys
sys.path.insert(0, 'compute/lib')
import k3_hcs_6d_twoloop as m
for name, N, cv, dimg, h in [('sl2', 2, 2.0, 3.0, 0.01), ('sl3', 3, 3.0, 8.0, 0.01)]:
    r = m.ybe_at_hbar5(N=N, c_v=cv, dim_g=dimg, hbar=h)
    print(name, json.dumps({
        'two_loop_verification_passed': r['two_loop_verification_passed'],
        'tree_ybe_residual': r['tree_ybe_residual'],
        'one_loop_naive_ybe_residual': r['one_loop_naive_ybe_residual'],
        'two_loop_YBE_residual': r['two_loop_YBE_residual'],
        'hbar5_coefficient_estimate': r['hbar5_coefficient_estimate'],
        'one_loop_expected_hbar3_ratio': r['one_loop_expected_hbar3_ratio'],
        'threshold_10_hbar5': 10*h**5,
        'reported_dim_g_approx': r['dim_g_approx'],
    }, sort_keys=True))
print('sl2_hbar_sweep')
for h in [0.02, 0.01, 0.005, 0.0025]:
    r = m.ybe_at_hbar5(N=2, c_v=2.0, dim_g=3.0, hbar=h)
    print(json.dumps({
        'hbar': h,
        'two_loop_YBE_residual': r['two_loop_YBE_residual'],
        'hbar5_coefficient_estimate': r['hbar5_coefficient_estimate'],
        'pass': r['two_loop_verification_passed'],
        'res_over_hbar3': r['two_loop_YBE_residual']/(h**3),
        'res_over_hbar5': r['two_loop_YBE_residual']/(h**5),
    }, sort_keys=True))
PY
```

Probe output:

```text
sl2 {"hbar5_coefficient_estimate": 61073.902685761226, "one_loop_expected_hbar3_ratio": 6.119755222876165, "one_loop_naive_ybe_residual": 6.1197552228761665e-06, "reported_dim_g_approx": 2, "threshold_10_hbar5": 1.0000000000000003e-09, "tree_ybe_residual": 3.469446951953614e-18, "two_loop_YBE_residual": 6.107390268579593e-06, "two_loop_verification_passed": false}
sl3 {"hbar5_coefficient_estimate": 63667.770951805745, "one_loop_expected_hbar3_ratio": 6.380148678864632, "one_loop_naive_ybe_residual": 6.380148678864633e-06, "reported_dim_g_approx": 3, "threshold_10_hbar5": 1.0000000000000003e-09, "tree_ybe_residual": 1.1102230246251565e-16, "two_loop_YBE_residual": 6.366777095291598e-06, "two_loop_verification_passed": false}
sl2_hbar_sweep
{"hbar": 0.02, "hbar5_coefficient_estimate": 16603.37812232513, "pass": false, "res_over_hbar3": 6.6413512489309205, "res_over_hbar5": 16603.3781223273, "two_loop_YBE_residual": 5.313080999144737e-05}
{"hbar": 0.01, "hbar5_coefficient_estimate": 61073.902685761226, "pass": false, "res_over_hbar3": 6.107390268579592, "res_over_hbar5": 61073.902685795925, "two_loop_YBE_residual": 6.107390268579593e-06}
{"hbar": 0.005, "hbar5_coefficient_estimate": 233105.90922323568, "pass": false, "res_over_hbar3": 5.827647730580892, "res_over_hbar5": 233105.90922323568, "two_loop_YBE_residual": 7.284559663226116e-07}
{"hbar": 0.0025, "hbar5_coefficient_estimate": 909636.680004322, "pass": false, "res_over_hbar3": 5.68522925004089, "res_over_hbar5": 909636.6800065424, "two_loop_YBE_residual": 8.883170703188892e-08}
```

Interpretation: the residual is of order `hbar^3`, not `hbar^5`.
`res_over_hbar3` stays around `5.7` to `6.6`; `res_over_hbar5` diverges as
`hbar` decreases. The two-loop counterterm does not cancel the surviving
one-loop-scale YBE residual in the current oracle.

No pytest run was useful: there is no direct pytest surface for this lane,
and collecting the whole compute suite would not be a narrow falsifier.

## Manuscript and notes status

Manuscript:

- `chapters/theory/quantum_chiral_algebras.tex:993`-`1006` states the K3
  universal defect hierarchy as a conjecture; the 5d K3 hCS Yangian row is
  explicitly `Conjectural`, and the 6d non-Lagrangian row is also
  `Conjectural`.
- I found no current chapter-level direct citation of
  `compute/lib/k3_hcs_6d_twoloop.py`, `ybe_at_hbar5`,
  `two_loop_verification_passed`, or "K3 hCS two-loop/YBE" as theorem-grade.

Notes:

- Old note `notes/k3_nonabelian_yangian_swarm_wave3_20260419/agent_09_costello_wave3.md:385`-`406`
  already listed the numerical residuals as `6.11e-06` for `sl2` and
  `6.37e-06` for `sl3`, then explained them away by Fierz collapse.
- The same old note at `:408`-`:419` nevertheless states a "Wave-3 theorem"
  that YBE holds at `hbar^5`, with `ClaimStatusProvedHere` structurally and
  `ClaimStatusConjectured` for full chain-level adjoint verification. This is
  the stale theorem-grade citation.
- `notes/k3_nonabelian_yangian_swarm_wave8_20260419/agent_09_costello_wave8.md:32`
  says the Wave-3 module computed sunset only and silently omitted the
  wheel-of-wheels topology; `:482` says the Wave-3 sunset diagram is
  superseded by Wave-8 cycle 1 analysis.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_07_nekrasov_feynman_compute.md:87`-`91`
  flags `two_loop_verification_passed=false` and no matching pytest files;
  `:230`-`:254` calls the two-loop failure decisive for status.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_15_hostile_synthesis.md:271`-`290`
  independently confirms the `sl2`/`sl3` failure and marks the lane red.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:68`-`84` lists
  "The K3 hCS two-loop/YBE lane is theorem-grade in the present compute
  state" under "Claims killed"; `:157`-`:164` states the direct red flag and
  concludes the lane is computational evidence at best, not a theorem.

## Status recommendation

Recommended status: not theorem-grade.

More precise status:

- Two-loop coefficient templates: computed/heuristic evidence, with Fierz
  and topology omissions explicitly recorded.
- Two-loop YBE restoration at `hbar^5`: open/conjectural in mathematics and
  currently red in the direct compute oracle.
- Any manuscript use should remain `ClaimStatusConjectured` unless the
  non-Fierz Casimir-sector calculation and direct tests are supplied.

## Minimal patches

Do not patch compute or manuscript from this file ownership lane.

Minimal future patches:

1. Add `compute/tests/test_k3_hcs_6d_twoloop.py` with direct `sl2` and `sl3`
   probes over a small `(u, v, hbar)` grid. The test should require either
   `two_loop_verification_passed=True` after a real repair, or be marked
   expected-failure while the red flag is open.
2. In `ybe_at_hbar5`, stop replacing the supplied `dim_g` by `max(N, 1)`.
   The present `sl3` oracle is not actually using `dim_g=8`.
3. Replace the Fierz-diagonal `t tensor t` shadow by an actual Casimir-sector
   implementation, or rename the `R_twoloop_YBE`/`R_full_through_twoloop`
   functions and docstrings to "ansatz" rather than "YBE-preserving".
4. If note edits are permitted later, mark the old Wave-3 theorem paragraph
   at `notes/k3_nonabelian_yangian_swarm_wave3_20260419/agent_09_costello_wave3.md:408`-`419`
   as superseded by the Wave-8 and 2026-04-24 red-flag audits.
