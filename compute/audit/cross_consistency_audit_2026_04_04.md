# Cross-Consistency Audit of Compute Modules (2026-04-04)

All three volumes: Vol I (~/chiral-bar-cobar), Vol II (~/chiral-bar-cobar-vol2), Vol III (~/calabi-yau-quantum-groups).

## Findings Register

### FINDING 1 [CRITICAL]: kappa(Heisenberg_k) = k/2 vs k

**Modules with WRONG value kappa = k/2:**
- `e2_bar_complex.py` (Vol III): line 265, `self.k / 2`
- `e2_barcobar_koszul.py` (Vol III): line 211, `kappa(H_k) = k/2`
- `hms_shadow_equivalence.py` (Vol III): lines 439/462, `Fraction(1, 2)` at k=1

**Modules with CORRECT value kappa = k:**
- `cross_volume_shadow_bridge.py` (Vol III): lines 102-108
- `geometric_langlands_shadow.py` (Vol III): lines 516-521
- `fukaya_shadow_tower.py` (Vol III): lines 311/416
- `genus_expansion.py` (Vol I): line 42
- `genus2_landscape.py`, `genus3_landscape.py`, `genus4_landscape.py` (Vol I)
- `euler_product_from_mc.py` (Vol I): line 659
- `genus1_kappa_verification.py` (Vol II): line 82/812

**Correct value:** kappa(H_k) = k. Source: `landscape_census.tex` line 69.

**Derivation:** V_Lambda = H_1^{tensor r} has kappa = r by additivity; each H_1 contributes 1. For H_k: kappa = k directly (the level). The formula kappa = c/2 applies to W-algebras, not Heisenberg (c = 1 for all k).

**Root cause:** AP1 (copy-paste without recomputation). The formula kappa = c/2 was applied to the Heisenberg family where it does not hold.

---

### FINDING 2 [CRITICAL]: kappa(affine KM) wrong formula in kazhdan_lusztig_shadow.py

**Wrong module:**
- `kazhdan_lusztig_shadow.py` (Vol III): line 76/95, uses `dim(g) * k / (2 * (k + h_dual))`

This is c/2 (Sugawara central charge divided by 2), NOT kappa.

**Correct formula:** `dim(g) * (k + h^v) / (2 * h^v)`

**Numerical discrepancy at sl_2, k=1:**
- WRONG: 3*1/(2*3) = 1/2
- CORRECT: 3*3/4 = 9/4

**Independent verification:** The wrong formula FAILS the complementarity test (AP24):
- Wrong: kappa(1) + kappa(-5) = 1/2 + 5/2 = 3 (should be 0)
- Correct: kappa(1) + kappa(-5) = 9/4 - 9/4 = 0

**Correct modules:** `geometric_langlands_shadow.py`, `cross_volume_shadow_bridge.py`, `topological_recursion_families.py` (Vol I), `exceptional_shadow_complete.py` (Vol I).

Source: `landscape_census.tex` lines 77, 81, 1154.

---

### FINDING 3 [SERIOUS]: Conifold/betagamma kappa value ambiguity

**Disagreement:**
- `hms_shadow_equivalence.py`: kappa(conifold) = -1/2 (lines 1206/1213/1246)
- `geometric_langlands_shadow.py`: kappa(betagamma) = -1/2 (line 502)
- `fukaya_shadow_tower.py`: kappa(bg, lambda=1) = 1, kappa(bg, lambda=1/2) = -1/2
- `cy_to_chiral_functor.py`: kappa(bg, lambda=1) = 1

**Root cause:** kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.
- At lambda=0 or 1 (standard weight): kappa = 1
- At lambda=1/2 (symplectic/Wakimoto): kappa = -1/2

Modules using kappa = -1/2 are applying the symplectic-weight value without specifying lambda. The geometric_langlands module explicitly says "c = -1" (which corresponds to lambda=1/2), not the standard betagamma.

**Fix:** All betagamma references must specify the conformal weight lambda.

---

### FINDING 4 [SERIOUS]: Conifold shadow depth class

**Disagreement:**
- `hms_shadow_equivalence.py`: conifold = class G (S4=0, lines 1282/1287)
- `fukaya_shadow_tower.py`: conifold = class G (line 940)
- `cy_to_chiral_functor.py`: conifold = betagamma = class C (depth 4, line 771)
- `cross_volume_shadow_bridge.py`: conifold -> class C (line 726)
- `depth_classification.py` (Vol I): betagamma = class C, r_max = 4 (line 499)

**Correct:** If the conifold chiral algebra is identified with betagamma, then class C (depth 4). The betagamma system has Q^contact != 0, giving non-trivial quartic shadow. hms and fukaya modules WRONG to classify as class G.

---

### FINDING 5 [SERIOUS]: K3 kappa value multiplicity

**Values across modules:**
- hms_shadow_equivalence.py: 1 (chi/24), 11 (rank(T)/2), 12 (Mukai/2)
- cy_to_chiral_functor.py: 12 (rank/2)
- fukaya_shadow_tower.py: 11 (transcendental/2)
- vafa_witten_shadow.py: 12 or 11 (unresolved)

**Root cause:** Multiple K3-associated chiral algebras exist. But the underlying issue is Finding 6 (wrong lattice kappa formula).

---

### FINDING 6 [CRITICAL]: kappa(lattice VOA) = rank vs rank/2

**Vol I (CORRECT): kappa = rank**
- `lattice_voa_shadows.py`: line 118, returns `Rational(rank)`
- `genus3_landscape.py`: line 152, returns `Fraction(rank)`
- `cross_volume_shadow_bridge.py`: line 172, `kappa_lattice(rank) = rank`
- `genus_expansions.tex`: line 2083, "kappa(V_Lambda) = d"

**Vol III (WRONG): kappa = rank/2**
- `cy_to_chiral_functor.py`: lines 539/548/879
- `hms_shadow_equivalence.py`: lines 543/579/1572
- `fukaya_shadow_tower.py`: lines 1572/1580

**Derivation:** V_Lambda = H_1^{otimes rank} otimes C[Lambda]. By additivity: kappa = rank * kappa(H_1) = rank * 1 = rank. The rank/2 error comes from a CY-geometric definition that does not match the chiral-algebraic one.

---

### FINDING 7 [SERIOUS]: Quintic kappa value (factor of -24)

**Disagreement:**
- `cy_to_chiral_functor.py`: kappa = chi/24 = -25/3
- `modular_cy_characteristic.py`: kappa = chi/24 = -25/3
- `fukaya_shadow_tower.py`: kappa = -chi(Q) = 200
- `hms_shadow_equivalence.py`: kappa = 200 (from F_1 = kappa/24 = 25/3)

**Root cause:** Two different "kappa" for CY3:
1. kappa_BCOV = chi/24 = -25/3 (BCOV coefficient in holomorphic anomaly equation)
2. kappa_shadow = 24 * F_1 = 200 (modular characteristic from shadow obstruction tower)

These differ by a factor of -24.

---

### FINDING 8 [MODERATE]: C_{empty,empty,empty} convention

- `c3_dt_partition.py`: C_{0,0,0} = M(q) (MacMahon function)
- `topological_vertex.py`: C_{0,0,0} = M(q) (consistent)
- `coha_drinfeld_bulk.py`: C_{0,0,0} = 1 (bare vertex, Z_{C^3} = M(q))

The COHA module uses a convention where the vertex amplitude is 1 and the full partition function Z = sum over internal partitions gives M(q). The other modules identify C_{0,0,0} with the full partition function directly.

---

### CLEAN CHECKS (no inconsistencies found)

**Faber-Pandharipande lambda_g^FP:** All modules agree on the Bernoulli formula. lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680. Verified across 5 implementations.

**j-function coefficients:** c(1) = 196884 in all modules that compute it (`bkm_shadow_complete.py`, `moonshine_shadow_atlas.py`).

**MacMahon function M(q):** Coefficients [1, 1, 3, 6, 13, 24, 48, 86] agree across `c3_dt_partition.py`, `topological_vertex.py`.

**Complementarity sum:** KM = 0 (all families), Virasoro = 13, betagamma = 0, W_3 = 250/3, N=2 SCA = 1. All correct. No cross-module contradictions.

## Summary

| Finding | Severity | Description |
|---------|----------|-------------|
| 1 | CRITICAL | kappa(H_k) = k/2 in 3 modules (should be k) |
| 2 | CRITICAL | kappa(KM) uses c/2 formula in kazhdan_lusztig (should be dim*(k+h^v)/(2h^v)) |
| 3 | SERIOUS | betagamma kappa = -1/2 without specifying lambda=1/2 |
| 4 | SERIOUS | Conifold classified as class G (should be C, depth 4) |
| 5 | SERIOUS | K3 kappa has 3 different values (1, 11, 12) |
| 6 | CRITICAL | kappa(lattice) = rank/2 in Vol III (should be rank) |
| 7 | SERIOUS | Quintic kappa differs by factor -24 across modules |
| 8 | MODERATE | C_{0,0,0} convention (1 vs M(q)) |

3 CRITICAL, 4 SERIOUS, 1 MODERATE, 4 CLEAN.
