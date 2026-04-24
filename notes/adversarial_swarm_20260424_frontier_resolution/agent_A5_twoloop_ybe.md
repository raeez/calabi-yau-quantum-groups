# Agent A5 Two-Loop/YBE Report

Date: 2026-04-24 08:15 SAST

## Scope

Ownership lane: K3 hCS two-loop/YBE repair compute lane only.

Touched only compute/tests and this report. No manuscript statuses were changed.

## Located Probe

The relevant probe is `compute/lib/k3_hcs_6d_twoloop.py`, especially
`ybe_at_hbar5()`. There was no existing dedicated
`compute/tests/test_k3_hcs_6d_twoloop.py`; I added one diagnostic test
module.

## Result

Repair did not succeed. The obstruction is not a two-loop `hbar^5`
normalization/sign problem. The current two-loop checker is blocked by a
one-loop `hbar^3` defect inherited from
`R_oneloop_correction(s) = (12 + c_v/2) hbar^2 P/s^2`.

For the rational Yang normalization

```text
R_tree(s) = (s I + hbar P)/(s + hbar),
r(s) = (P - I)/s,
q(s) = c P/s^2,   c = 12 + c_v/2,
```

the linearized YBE defect at order `hbar^3` is

```text
c / (u v (u - v)) * (P12 P23 - P23 P12).
```

For `sl2`, `c_v = 2`, `c = 13`, `(u, v) = (2.3, 1.7)`, this coefficient is

```text
13 / (2.3 * 1.7 * 0.6) = 6500/1173 = 5.541346973572037...
```

Direct scaling confirms this is the observed leading term. At `hbar=0.01`
the existing probe reports residual `6.107390268579593e-06`, while
`10*hbar^5 = 1e-09`; the test is therefore not `O(hbar^5)`.

## Formula Attack

The two-loop counterterm in `R_twoloop_counterterm()` starts at `hbar^4`.
Crossing it with the tree `hbar` term can affect order `hbar^5`, but it
cannot cancel a pre-existing order `hbar^3` obstruction. Changing the
two-loop sign or coefficient therefore cannot repair the current probe.

A control calculation shows that an exact Yang coupling renormalization

```text
hbar_eff = hbar + 13 hbar^2,
R_tree(s; hbar_eff)
```

does satisfy the difference-form YBE to machine precision. That control
does not justify replacing the current fish term: it only isolates the
kind of one-loop direction that is YBE-admissible. A real repair needs a
new one-loop normalization or counterterm derivation before the two-loop
`hbar^5` claim can be tested honestly.

## Files Changed

- `compute/tests/test_k3_hcs_6d_twoloop.py`
- `notes/adversarial_swarm_20260424_frontier_resolution/agent_A5_twoloop_ybe.md`

## Tests

New targeted test command:

```bash
python3 -m pytest compute/tests/test_k3_hcs_6d_twoloop.py -q
```

Actual outcome:

```text
3 passed, 1 xfailed in 3.15s
```

## Material Commands Run

```bash
git status --short
rg -n "two[-_ ]loop|2[-_ ]loop|YBE|Yang.?Baxter|hbar\\^3|hbar\\^5|O\\(hbar\\^5\\)|residual|R[-_ ]?matrix|classical Yang|CYBE" compute tests notes chapters -g '*.{py,md,tex}'
rg --files compute tests | sort
find notes -maxdepth 2 -type f -path '*adversarial_swarm_20260424_frontier_resolution*' -print | sort
find compute -maxdepth 3 -type f -print | sort
rg -n "residual|YBE|Yang|Baxter|hbar\\^3|hbar3|hbar\\^5|hbar5|O\\(hbar\\^5\\)|two[-_ ]loop|twoloop|normal|sign" compute/lib/k3_hcs_6d_twoloop.py compute/tests -g '*.py'
rg -n "k3_hcs_6d_twoloop|hcs_6d_twoloop|twoloop|two_loop|two-loop|6d.*hCS|hCS.*6d" compute/tests compute/lib -g '*.py'
sed -n '1,260p' compute/lib/k3_hcs_6d_twoloop.py
sed -n '260,620p' compute/lib/k3_hcs_6d_twoloop.py
git diff -- compute/lib/k3_hcs_6d_twoloop.py compute/tests | sed -n '1,240p'
rg -n "k3_hcs_6d_(one|two|three|four)|R_oneloop|one.?loop.*YBE|counterterm|ybe_residual|def R_|def ybe|def permutation|def embed" compute/lib/k3_hcs_6d_oneloop.py compute/tests -g '*.py'
sed -n '1,240p' compute/lib/k3_hcs_6d_oneloop.py
sed -n '240,560p' compute/lib/k3_hcs_6d_oneloop.py
rg -n "k3_hcs_6d_twoloop|twoloop|two_loop|ybe5|R_full_through_twoloop|two_loop_YBE_residual" compute/tests -g '*.py'
python3 compute/lib/k3_hcs_6d_twoloop.py
python3 k3_hcs_6d_twoloop.py
PYTHONPATH=compute/lib python3 compute/lib/k3_hcs_6d_twoloop.py
PYTHONPATH=compute/lib python3 - <<'PY'
# linearized coefficient and hbar-scaling probe
PY
PYTHONPATH=compute/lib python3 - <<'PY'
# exact group-algebra derivation of c/(uv(u-v)) [P12,P23]
PY
date '+%Y-%m-%d %H:%M:%S %Z'
python3 -m pytest compute/tests/test_k3_hcs_6d_twoloop.py -q
```

Two early direct script invocations failed before the correct
`PYTHONPATH=compute/lib` command: one had the wrong working-directory
path, and one used `/usr/bin/python3` without `numpy`.
