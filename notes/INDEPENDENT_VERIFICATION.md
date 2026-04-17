# Independent Verification Protocol

**Motivation.** The 2026-04-16 adversarial audit (first_principles_cache.md #57-68) exposed a systematic failure mode: tests verify formulas against the same hardcoded table from which the formula was derived. The κ_BKM_universal engine defines `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with `weight := c_0 / 2` literal, and 99 tests check `Fraction(10, 2) == 5` against that table. This is tautology dressed as verification.

**Solution.** Every `\ClaimStatusProvedHere` must have at least one test that computes the claimed value from a data source **disjoint** from the derivation source. The disjointness is machine-checked at test-import time.

## How to decorate a test

```python
from compute.lib.independent_verification import independent_verification

@independent_verification(
    claim="thm:phi-k3-explicit",
    derived_from=[
        "HKR isomorphism on D^b(Coh(K3))",
        "Hodge diamond of K3",
    ],
    verified_against=[
        "Mukai 1984 lattice rank 24",
        "Classical Betti numbers b_0+b_2+b_4 = 24",
    ],
    disjoint_rationale=(
        "HKR reconstructs total_dim via polyvector cohomology; "
        "Mukai/Betti gives it as a topological invariant without "
        "any reference to HH_*. Independent derivations."),
)
def test_total_dimension_24():
    ...
```

- `claim` must match a `\label{...}` in the manuscript.
- `derived_from` lists canonical names of the data/papers/conventions the **formula** relies on. These are the "suspect" sources the test must avoid.
- `verified_against` lists independent sources the **test** computes against.
- `disjoint_rationale` is a one-sentence audit explaining why the two sets are genuinely independent (not renamed).

## Invariants enforced at import time

1. **Disjointness.** If `derived_from ∩ verified_against` is non-empty (case/whitespace-insensitive), `IndependentVerificationError` is raised at decoration time. The test module fails to import; the audit surfaces it.
2. **Rationale presence.** Empty or whitespace-only `disjoint_rationale` is rejected.
3. **No claim inflation.** A decoration with a `claim` that does not appear as `\ClaimStatusProvedHere` anywhere in the manuscript is an **orphan** — the audit flags it and returns nonzero.

## Audit lint

```
make verify-independence           # summary
make verify-independence-verbose   # list every uncovered claim
```

Output:

```
ProvedHere claims found in .tex: 283
Claims with independent verification: 2 (0.7%)
Claims WITHOUT independent verification: 281
Tautological registry entries: 0
Orphan registry entries: 0
AUDIT RESULT: PASS
```

Exit status is nonzero on tautology or orphan. Coverage percentage is a metric, not a gate — enforcing a coverage floor would incentivize low-quality "independent" tests.

## How to heal a tautological claim

Three options when honest decoration fails the disjointness check:

1. **Find a disjoint verification source.** Best outcome. Example: `thm:phi-k3-explicit` was nominally at risk (HKR on K3 computes rank 24), but Mukai lattice theory provides a classical independent source.

2. **Restrict the scope of the claim.** If the claim is only provable within a specific dataset, tag it with that scope explicitly: downgrade `\begin{theorem}` to `\begin{proposition}[for the 8 diagonal Z/NZ symplectic orbifolds]` and note in the proof that general K3-fibered CY3s are conjectural.

3. **Downgrade the status.** If no independent verification exists and scope restriction is not enough, replace `\ClaimStatusProvedHere` with `\ClaimStatusConjectured`. This is the honest fallback — an "independently verified" claim without an independent test should not be tagged as proved.

Each of these is a concrete, local edit the audit can motivate. The audit does NOT automatically choose; it surfaces the choice.

## Known-tautological registry

Maintained at `notes/tautology_registry.md`. Claims listed there have failed honest decoration and are awaiting one of the three healings above. This registry is the working queue for manuscript healing.

## For agents and future sessions

When writing a new theorem tagged `\ClaimStatusProvedHere`:

1. Before writing the LaTeX, answer: "What is my independent verification source?"
2. If you cannot name one, either restrict the scope or tag conjectural.
3. Write the test with `@independent_verification(...)` from day one.
4. Run `make verify-independence` before commit.

The decorator is an assertion about mathematical practice, not a bureaucratic tag. A claim without independent verification is a claim you cannot distinguish from a circular fit.
