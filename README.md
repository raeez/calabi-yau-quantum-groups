# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | The categorical completion |

## The CY-to-Chiral Functor

The programme flow:

```
CY category C  -->  cyclic A-infinity  -->  Lie conformal algebra
                                                     |
                                            factorization envelope
                                                     |
                                              E_2-chiral algebra A_X
                                                     |
                                              bar complex B(A_X)
                                                /            \
                                   Euler product              shadow obstruction tower
                                        |                             |
                               BKM denominator identity      Vol I Theta_A
```

For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.

## Connection to Volumes I-II

| Input | Source | Role in Vol III |
|-------|--------|-----------------|
| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |

## Five-Part Structure

- **I. The CY Engine**: CY categories, cyclic A-infinity structures, Hochschild calculus (HKR, Gerstenhaber, BV, CY-to-Lie-conformal passage), E_1/E_2-chiral algebras, E_n factorization
- **II. The CY Characteristic Datum**: CY-to-chiral functor Phi, quantum chiral algebras, modular trace, quantum group foundations, braided factorization (U_q(g), R-matrix, YBE from bar coassociativity, braided bar-cobar adjunction CY-B, braided shadow tower), Drinfeld center and bulk algebras (BZF theorem, center vs derived center, Kazhdan-Lusztig at roots of unity)
- **III. The CY Landscape**: K3 x E, toric CY3 CoHA, Fukaya categories (elliptic/K3/abelian/CY3/wrapped, HMS compatibility), derived categories, matrix factorizations, quantum group representations (generic q vs roots of unity)
- **IV. Seven Faces of r_CY(z)**: Bar-cobar bridge to Vol I, CY holographic datum
- **V. The CY Frontier**: Geometric Langlands and CY quantum groups

## Status

| Component | Status |
|-----------|--------|
| CY_2 functor (d=2) | **Proved** |
| Lattice VOA bridge | **Proved** |
| CoHA = E_1 sector | **Proved** |
| Drinfeld center = E_2 | **Proved** |
| CY_3 functor (d=3) | **Conjectural** (central open problem) |
| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
| Langlands = Koszul | **Conjectural** |
| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |

| Metric | Value |
|--------|------:|
| Pages | ~325+ |
| Theory chapters | 13 |
| Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
| Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
| Working notes | 22 |
| Tagged claims | ~364 |
| Compute tests | ~17,700+ |
| Compute modules | 189 lib + 187 test |
| Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
| HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
| Bibliography | 38 bibitems (0 undefined citations, down from 62) |
| Genuine stubs (<50 lines) | 1 (quantum_groups_foundations at 24 lines) |

## Build

```bash
make              # full build
make fast         # single-pass quick check
```

Requires TeX Live 2024+ with pdflatex.
