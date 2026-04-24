# Agent A5 YBE One-Loop Repair

Date: 2026-04-24 SAST

## Scope

Ownership lane: K3 hCS one-loop/YBE compute repair.

Files intentionally touched:

- `compute/lib/k3_hcs_6d_oneloop.py`
- `compute/tests/test_k3_hcs_6d_oneloop.py`
- this report

The pre-existing two-loop diagnostic files were not overwritten. They already
contain a compatible exact one-loop normalization model and the negative
two-loop oracle.

## Exact Formula

The naive fish term

```text
R_fish(s) = (12 + c_v/2) hbar^2 P / s^2
```

is not YBE-admissible. For the normalized rational Yang matrix

```text
R_tree(s; hbar) = (s I + hbar P)/(s + hbar),
```

the order-`hbar^3` defect of the fish direction is

```text
((12 + c_v/2)/(u v (u-v))) * (P12 P23 - P23 P12).
```

The repaired one-loop direction is the tangent to the Yang family under
coupling renormalization

```text
hbar_eff = hbar + (12 + c_v/2) hbar^2.
```

Equivalently,

```text
R_tree(s; hbar_eff)
  = R_tree(s; hbar)
    + (12 + c_v/2) hbar^2 (P - I)/s
    + O(hbar^3).
```

Thus the theorem-grade compute statement is:

```text
R_repaired,1(s) = R_tree(s; hbar) + (12 + c_v/2) hbar^2 (P - I)/s
```

has zero order-`hbar^3` YBE obstruction, and the exact control
`R_tree(s; hbar_eff)` satisfies the difference-form YBE to machine
precision. The scalar-gauge variant `(12 + c_v/2) hbar^2 P/s` is equivalent
for the order-`hbar^3` obstruction, but the normalized Yang tangent is
`(P-I)/s`.

## Attack Result

The repair is mathematically real as a YBE repair. It is not yet a proof that
the original hCS fish integral literally equals this operator. What is proved
by the compute lane is the forced shape of any one-loop YBE-admissible
normalization in the rational Yang model:

```text
fish + CT_1 = R_tree(hbar + (12 + c_v/2) hbar^2) - R_tree(hbar).
```

Therefore the old `P/u^2` fish expression is a negative oracle, and the
renormalized Yang parameter is the repaired one-loop operator modulo the
remaining hCS derivation of `CT_1`.

## Tests

Command run:

```bash
python3 -m pytest compute/tests/test_k3_hcs_6d_oneloop.py compute/tests/test_k3_hcs_6d_twoloop.py -q
```

Result:

```text
14 passed in 2.54s
```

Coverage added:

- direct exact `S_3` group-algebra coefficient for the fish obstruction;
- exact vanishing of the order-`hbar^3` coefficient for the Yang tangent;
- direct matrix YBE for `R_tree(s; hbar_eff)` at `sl2` and `sl3`;
- finite-difference check that the tangent is the first-order term of the
  exact renormalization;
- scaling check that the repaired tangent residual starts at `hbar^4`, not
  `hbar^3`.

## Remaining Caveats

1. The hCS Feynman derivation of the counterterm `CT_1` is still not proved in
   this compute lane.
2. The repaired one-loop model removes the lower obstruction, but the legacy
   two-loop sunset ansatz still has a nonzero `hbar^5` obstruction.
3. No manuscript theorem status was changed.
