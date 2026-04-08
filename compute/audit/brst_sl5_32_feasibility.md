# BRST Spectral Sequence for (3,2) in sl_5: Feasibility Assessment

## The nilpotent

Partition (3,2) of 5. The associated sl_2 element is
h = diag(2, 0, -2, 1, -1). This is the first non-abelian test case
for the DS-KD intertwining conjecture.

## Dimensions

| Piece | dim | Elements |
|-------|-----|----------|
| g = sl_5 | 24 | |
| g_{-4} | 1 | E_{31} |
| g_{-3} | 2 | E_{34}, E_{51} |
| g_{-2} | 3 | E_{21}, E_{32}, E_{54} |
| g_{-1} | 4 | E_{24}, E_{35}, E_{41}, E_{52} |
| g_0 | 4 | H_1, H_2, H_3, H_4 (= Cartan) |
| g_{+1} | 4 | E_{14}, E_{25}, E_{42}, E_{53} |
| g_{+2} | 3 | E_{12}, E_{23}, E_{45} |
| g_{+3} | 2 | E_{15}, E_{43} |
| g_{+4} | 1 | E_{13} |

**Key numbers:**
- dim(n_+) = 10 (graded: 4 + 3 + 2 + 1)
- dim(g_{-1}) = 4
- dim(g_0) = 4 (Cartan subalgebra; Levi is abelian since all parts distinct)
- BRST order = 4 (= max grade in n_+)
- Ghost Fock space = Lambda(n_+*) = 2^10 = 1024

## Non-abelianity of n_+

n_+ is NON-ABELIAN: 20 nonzero commutator terms landing in 6 target
root spaces:

- [g_1, g_1] -> g_2: 3 independent brackets (E_{12}, E_{23}, E_{45})
- [g_1, g_2] -> g_3: 2 independent brackets (E_{15}, E_{43})
- [g_1, g_3] -> g_4: 1 independent bracket (E_{13})
- [g_2, g_2] -> g_4: same target E_{13}

Total: 6 distinct target root spaces. This matches the assessment's
"6 commutator landings."

These 20 terms generate the ghost-ghost piece Q_gh of the BRST charge,
which is the entire obstruction to the abelian-n_+ proof method.

## Naive feasibility: INFEASIBLE

The full BRST complex at conformal weight Delta has dimension
dim(V_Delta) * 1024, giving matrices:

| Weight | V-dim | BRST dim | Verdict |
|--------|-------|----------|---------|
| 0 | 1 | 1,024 | trivial |
| 1 | 24 | 24,576 | OK |
| 2 | 324 | 331,776 | large |
| 3 | 3,200 | 3,276,800 | infeasible naive |

## Kazhdan filtration approach: FEASIBLE

The correct approach uses the Kazhdan spectral sequence. The E_1 page
is H*(n_+, Sym^d(g_-)), which is Lie algebra cohomology of the
10-dimensional nilpotent Lie algebra n_+ acting on symmetric powers
of the 10-dimensional space g_-.

The CE complex decomposes by ghost number p (= exterior power of n_+*).
At each (d, p), the block is:

  dim = dim(Sym^d(g_-)) * C(10, p)

| Sym^d | dim(Sym^d) | max block (p=5) | Verdict |
|-------|------------|-----------------|---------|
| d=0 | 1 | 252 | trivial |
| d=1 | 10 | 2,520 | easy |
| d=2 | 55 | 13,860 | feasible |
| d=3 | 220 | 55,440 | feasible |
| d=4 | 715 | 180,180 | feasible (sparse) |
| d=5 | 2,002 | 504,504 | borderline |

**With weight decomposition** (g_0 = Cartan, so everything decomposes
by h-weight): blocks are much smaller than the worst case. Each
weight space of Sym^d(g_-) is a single monomial type, so the actual
block sizes at each h-weight are typically 10-100x smaller.

## Engine architecture

```
brst_sl5_32_engine.py

Input: sl_5 structure constants, partition (3,2)

Module 1: Lie algebra setup
  - Build sl_5 with standard basis {E_{ij}, H_k}
  - Compute Dynkin grading from partition (3,2)
  - Extract n_+, g_-, g_0 with gradings
  - Compute [n_+, n_+] structure constants (the 20 bracket terms)

Module 2: Coefficient spaces
  - Build Sym^d(g_-) as explicit vector space, d = 0, ..., D_max
  - Decompose by h-weight (Cartan eigenvalues)
  - Build n_+-action on Sym^d(g_-) as explicit matrices

Module 3: CE complex
  - Build C^p(d) = Sym^d(g_-) tensor Lambda^p(n_+*)
  - Build d_CE: C^p -> C^{p+1} including ghost-ghost terms
  - Verify d_CE^2 = 0

Module 4: Cohomology
  - Compute H^p(n_+, Sym^d(g_-)) = ker(d_CE^p) / im(d_CE^{p-1})
  - This is the E_1 page of the Kazhdan SS

Module 5: E_1 degeneration check
  - Build d_2 differential from Kazhdan filtration
  - Check d_2 = 0 on E_1
  - If d_2 = 0: E_1 degeneration holds, conjecture supported
  - If d_2 != 0: conjecture fails at this level

Tests:
  - Verify against known W(sl_5, f_{(3,2)}) character at low weights
  - Cross-check: principal (5) and hook (4,1) must give E_1 degeneration
  - Verify ghost-ghost terms vanish for hook-type (abelian n_+ check)
```

## Verdict

**FEASIBLE for a compute engine.** The Kazhdan-filtered approach
reduces the problem to Lie algebra cohomology computations with
matrices at most ~55K x 55K at d=3, and much smaller with weight
decomposition. Through d=3 (conformal weight 3), standard dense
linear algebra suffices. At d=4, sparse methods are needed but
the computation remains within a single-machine budget.

Checking E_1 degeneration at weights 0-3 would provide strong
computational evidence for or against the conjecture at this
first non-abelian case.

**Estimated development time:** 1 agent session for the engine,
1 session for tests and verification. No cluster needed.

**Key structural simplification:** g_0 = Cartan (abelian Levi),
because the parts of (3,2) are all distinct. This means all
representation theory decomposes into 1-dimensional weight spaces,
which is the best possible case for a non-abelian n_+.
