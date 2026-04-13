# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | E_n-chiral algebras as algebraic-geometric objects on curves and configuration spaces |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | Derived centres interpreted physically as 3d HT gauge theories |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | Concrete CY quantum groups as examples of Vol I's abstract E_1-chiral quantum groups |

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
| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |

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
| CoHA as E_1 sector (toric CY3) | **Proved** |
| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
| Langlands = Koszul | **Conjectural** |
| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |

| Metric | Value |
|--------|------:|
| Pages | 367 |
| Theory chapters | 13 |
| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
| Working notes | Separate PDF in build |
| Tagged claims | 451 |
| Compute tests | 19,838 collected |
| Compute modules | 196 lib + 204 test |
| Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
| HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |
| Bibliography | 39 bibitems |

## Build

```bash
make              # full build
make fast         # single-pass quick check
```

Requires TeX Live 2024+ with pdflatex.
