# Agent 6 Verification Attack/Heal

Date: 2026-04-24.

## Scope

Owned write paths:

- `notes/swarm_20260424_remaining/agent_6_verification_attack_heal.md`
- `compute/tests/test_verification_surface_sanity.py`

Read-only context:

- `pytest.ini`
- `Makefile`
- `compute/lib/c3_hcs_hall_theta.py`
- `compute/tests/test_c3_hcs_hall_theta.py`
- `compute/lib/cy3_bridge_normal_form.py`
- `compute/tests/test_cy3_bridge_normal_form.py`
- `compute/lib/bkm_d3_explicit_generators.py`
- `compute/tests/test_bkm_d3_explicit_generators.py`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/examples/toric_cy3_coha.tex`

## Attack Findings

1. `make test` is a full compute-suite command, not a short gate.
   `Makefile` runs:

   ```bash
   pytest compute/tests/ -q -ra --durations=10
   ```

   `pytest.ini` declares a `slow` marker but does not set `addopts = -m "not slow"`.
   Slow tests are deselected only when the command explicitly supplies
   `-m "not slow"`. The marker description says slow tests are excluded from
   short passes, but configuration alone does not enforce that.

2. The local shell has two pytest surfaces. `python3 -m pytest` fails with
   `No module named pytest`; the `pytest` executable is available and reports
   `pytest 9.0.2`. Verification commands in this checkout should use `pytest`
   directly or an explicitly activated environment.

3. The full-suite size is not stable during the swarm. Collection observed:

   - `37968 tests collected` before the sanity test and before later concurrent edits.
   - `38009 tests collected` in a later full collection.
   - `38015/38029 tests collected (14 deselected)` in the latest
     `-m "not slow"` collection.

   Treat the count as a moving integration-surface signal until the integration
   owner freezes writes.

4. The CY3 bridge oracle is a regression witness, not an independent proof of
   the analytic hCS-to-Hall morphism. `compute/lib/c3_hcs_hall_theta.py`
   implements the finite torus-fixed abelian shuffle witness. Its tests check
   the SV kernel formula, binary localization, zero differential, and filtration
   metadata. Several assertions compare against functions in the same module,
   so they are useful for convention drift but not an independent analytic
   construction.

   This matches the manuscript: `chapters/theory/cy3_chain_level_bridge.tex`
   states that the executable witness records the kernel, two-point
   localization, zero differential, and filtration bound, and that it makes no
   claim about analytic extension to the full renormalised hCS factorisation
   algebra or descent over a non-affine cover.

5. The normal-form gate tests are cheap and mostly well targeted. The brittle
   point is exact tuple-order checking in
   `compute/tests/test_cy3_bridge_normal_form.py`; this is acceptable for a
   typed gate ledger but will produce churn if an integration owner inserts a
   new intermediate gate. One test name says "only the local yplus bridge" while
   the assertions also close `w_infty_representation`; this is naming drift, not
   a current test failure.

6. The repaired D=3 lattice-vector threshold is correctly covered by the
   targeted D=3 surface. `test_count_exceeds_64` now asserts
   `lattice_vector_count_at_d3(50) == 50` and `lattice_vector_count_at_d3(65) >
   64`, matching the odd-l threshold.

## Heal

Added a tiny sanity test at `compute/tests/test_verification_surface_sanity.py`.
It adds three cheap checks:

- every CY3 bridge target uses declared gate keys and the target packages are
  nested from local C3 to protected physics;
- the seven rigidifications are declared inside the protected package and have
  nonempty layer/statement metadata;
- the C3 theta continuity bound covers the arity-zero and arity-three cases
  without symbolic shuffle expansion.

This improves the verification surface without touching the main chapter or
other agents' files.

## Verification Strategy

Use the narrowest falsifying command first.

1. Tiny Agent-6 sanity gate:

   ```bash
   pytest -q compute/tests/test_verification_surface_sanity.py
   ```

   Observed: `3 passed in 0.44s`. Expected surface: under 1 second pytest time.

2. CY3 bridge and repaired D=3 regression gate:

   ```bash
   pytest -q \
     compute/tests/test_verification_surface_sanity.py \
     compute/tests/test_c3_hcs_hall_theta.py \
     compute/tests/test_cy3_bridge_normal_form.py \
     compute/tests/test_bkm_d3_explicit_generators.py \
     --durations=10
   ```

   Observed: `120 passed in 0.84s`; shell wall time about 1.9 seconds. This is
   the correct per-agent gate for the CY3 bridge/D=3 repair surface.

3. Same bridge/D=3 surface without the Agent-6 sanity file:

   ```bash
   pytest -q -m "not slow" \
     compute/tests/test_c3_hcs_hall_theta.py \
     compute/tests/test_cy3_bridge_normal_form.py \
     compute/tests/test_bkm_d3_explicit_generators.py
   ```

   Observed: `117 passed in 1.03s`.

4. Short compute-suite collection before a broad integration run:

   ```bash
   pytest --collect-only -q -m "not slow" compute/tests
   ```

   Latest observed collection: `38015/38029 tests collected (14 deselected)` in
   6.39 seconds of pytest-reported time. Use this to confirm that discovery
   still works before spending the full execution budget.

5. Short compute-suite execution when the integration owner wants a broad
   compute pass without symbolic/random slow tests:

   ```bash
   pytest -q -m "not slow" compute/tests --durations=20
   ```

   Equivalent Makefile form:

   ```bash
   PYTEST='pytest -m "not slow"' make test
   ```

   Expected surface: broad suite, excludes only the 14 marked slow tests. It may
   still be minutes because many unmarked tests are large symbolic or
   cross-engine checks.

6. Full compute suite only at integration freeze:

   ```bash
   pytest -q compute/tests --durations=20
   ```

   Equivalent:

   ```bash
   make test
   ```

   Expected surface: about 38k tests and all marked slow tests included. Use
   only after concurrent writes stop or when the integration owner needs the
   complete signal.

7. Manuscript fatal-error check after TeX edits:

   ```bash
   make check
   ```

   Not rerun by this agent because the Agent-6 write set touched only a compute
   test and an internal Markdown note, and the prompt states the current
   `make check` surface already passed.

## Commands Run

Context and audit:

```bash
sed -n '1,220p' ./CLAUDE.md
sed -n '1,240p' .agents/skills/vol3-build-surface/SKILL.md
sed -n '1,240p' .agents/skills/vol3-compute-engine/SKILL.md
sed -n '1,180p' ~/ecosystem/INVARIANTS.md
sed -n '1,180p' ~/ecosystem/AGENTS-HARNESS.md
git status --short
sed -n '1,220p' pytest.ini
rg -n "^(check|test|fast|pytest|compute|full|smoke|slow|quality|lint)[: ]|pytest|PYTHONPATH|make check" Makefile pytest.ini
sed -n '90,180p' Makefile
sed -n '1,260p' compute/lib/c3_hcs_hall_theta.py
sed -n '1,320p' compute/tests/test_c3_hcs_hall_theta.py
sed -n '1,320p' compute/lib/cy3_bridge_normal_form.py
sed -n '1,360p' compute/tests/test_cy3_bridge_normal_form.py
sed -n '1,240p' compute/tests/test_bkm_d3_explicit_generators.py
sed -n '1,260p' compute/lib/bkm_d3_explicit_generators.py
sed -n '420,460p' compute/lib/bkm_d3_explicit_generators.py
sed -n '280,430p' compute/tests/test_bkm_d3_explicit_generators.py
sed -n '1,120p' compute/tests/conftest.py
sed -n '3188,3262p' chapters/theory/cy3_chain_level_bridge.tex
rg -n -F "hCS-to-Hall" chapters/theory/cy3_chain_level_bridge.tex chapters/examples/toric_cy3_coha.tex compute/lib/cy3_bridge_normal_form.py compute/lib/c3_hcs_hall_theta.py
rg -n -F "normal form" chapters/theory/cy3_chain_level_bridge.tex chapters/examples/toric_cy3_coha.tex compute/lib/cy3_bridge_normal_form.py compute/lib/c3_hcs_hall_theta.py
```

Verification:

```bash
python3 -m pytest --collect-only -q compute/tests/test_c3_hcs_hall_theta.py compute/tests/test_cy3_bridge_normal_form.py compute/tests/test_bkm_d3_explicit_generators.py
```

Failed as an environment check: `/Library/Developer/CommandLineTools/usr/bin/python3: No module named pytest`.

```bash
pytest --version
pytest --collect-only -q compute/tests/test_c3_hcs_hall_theta.py compute/tests/test_cy3_bridge_normal_form.py compute/tests/test_bkm_d3_explicit_generators.py
pytest --collect-only -q -m "not slow" compute/tests | tail -n 20
pytest --collect-only -q compute/tests | tail -n 5
pytest -q compute/tests/test_verification_surface_sanity.py
pytest -q -m "not slow" compute/tests/test_c3_hcs_hall_theta.py compute/tests/test_cy3_bridge_normal_form.py compute/tests/test_bkm_d3_explicit_generators.py
time pytest -q compute/tests/test_verification_surface_sanity.py compute/tests/test_c3_hcs_hall_theta.py compute/tests/test_cy3_bridge_normal_form.py compute/tests/test_bkm_d3_explicit_generators.py --durations=10
pytest --collect-only -q -m "not slow" compute/tests | tail -n 5
```

## Remaining Verification Risks

1. The full compute suite was not executed by this agent. The latest collection
   count moved during concurrent work, so a final full run should wait for the
   integration owner to freeze writes.

2. `make test` includes marked slow tests unless the caller overrides `PYTEST`
   or calls pytest directly with `-m "not slow"`.

3. `pytest.ini` does not encode `testpaths`, `addopts`, or `pythonpath`; import
   stability currently comes from `compute/tests/conftest.py`, not root pytest
   configuration.

4. The CY3 finite-mode theta tests are same-engine regression checks. They
   guard kernel/sign/order drift but do not independently prove the analytic
   hCS-to-Hall extension, global DWR descent, Hall--Borcherds bialgebra datum,
   or protected-physics functor.

5. Broad unmarked tests may still be expensive even under `-m "not slow"`.
   Slow marker coverage is partial; the command excludes 14 marked slow tests,
   not every expensive test.
