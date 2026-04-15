# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

Constructs the functor Phi: CY_d-Cat -> E_n-ChirAlg from Calabi-Yau categories to chiral algebras, proved for all d (CY-A_2 at d=2; CY-A_3 at d=3 via the infinity-categorical proof that HH^{-2}_{E_1}=0 and the space of E_3-liftings is contractible). The E_n level is dimension-dependent: E_inf at d=1, E_2 at d=2, E_1 at d>=3, with the braided E_2 structure at d>=3 constructed via the Drinfeld center Z(Rep^{E_1}(A)) — the right adjoint to the forgetful functor, not a categorified averaging map. The K3 Yangian Y(g_{K3}) has 24 generators, Mukai-signature (4,20) Serre relations, and degree-(24,24) structure function. Six independent constructions approach G(K3 x E); their conjectural convergence is CY-C.

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
                                                chiral target A_X
                                                     |
                                              bar complex B(A_X)
                                                /            \
                                   Euler product              shadow obstruction tower
                                        |                             |
                               BKM denominator identity      Vol I Theta_A
```

For d=2: the functor Phi_2 is proved (Theorem CY-A_2). For d=3: the infinity-categorical proof resolves the chain-level S^3-framing obstruction (Theorem CY-A_3). For toric CY3: a separate proved E_1 CoHA/chart-gluing package provides independent verification. The E_n-chiral Koszul duality (Theorem CY-B) is proved at d=3 via the Verdier spectral functor: E_1-Koszul on A, inducing E_2 on the Drinfeld center. CY-C (quantum group realization) and CY-D (modular characteristic at d>=3) remain conjectural/programme.

## Connection to Volumes I-II

| Input | Source | Role in Vol III |
|-------|--------|-----------------|
| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
| Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |

## Seven-Part Structure

- **I. Foundations**: CY categories, cyclic A-infinity, Hochschild calculus
- **II. CY-to-Chiral Functor**: Construction of Phi, the [m_3,B^{(2)}] saga, kappa-spectrum
- **III. E_n Hierarchy and Chiral Quantum Groups**: E_1/E_2-chiral algebras, E_n factorization, quantum groups, Drinfeld center, braided factorization
- **IV. The K3 Yangian**: Phi(K3) explicit, abelian Yangian, K3 x E BKM, quantum toroidal, six routes to G(K3 x E)
- **V. CY Landscape**: toric CY3 CoHA, Fukaya, derived, matrix factorizations, quantum group reps
- **VI. Seven Faces of r_CY(z)**: bar-cobar bridge, modular Koszul bridge, CY holographic datum
- **VII. Frontiers**: geometric Langlands, nonabelian Yangian, ZTE, root of unity

## Status

| Component | Status |
|-----------|--------|
| CY-A (CY-to-chiral functor) | **Proved** at all d (CY-A_2 at d=2; CY-A_3 at d=3, inf-cat) |
| CY-B (E_n-chiral Koszul duality) | **Proved** at d=3 via Verdier spectral functor |
| K3 Yangian Y(g_{K3}) | **Proved** (24 generators, Mukai signature, abelian presentation) |
| Phi(K3) explicit | **Proved** (H_Muk, kappa_ch=2) |
| CoHA as E_1 sector (toric CY3) | **Proved** |
| Drinfeld center E_1 -> E_2 | **Proved** (right adjoint to forgetful, half-braiding construction) |
| CY-C (quantum group realization) | **Conjectural** (G(X) not constructed in general) |
| CY-D (modular characteristic d>=3) | **Programme** |
| Langlands = Koszul | **Conjectural** |

| Metric | Value |
|--------|------:|
| Pages | ~757 |
| Parts | 7 (with Part openers and 3 reading paths) |
| Theory chapters | 14 |
| Example chapters | 11 |
| Connection chapters | 4 |
| Working notes | ~89pp (separate PDF) |
| Compute engines | ~570 |
| Compute tests | ~39,500 |
| Anti-patterns | AP-CY1 through AP-CY61 + AP150-AP157 + FM24-FM46 |
| HOT ZONE entries | HZ3-1 through HZ3-10 |
| First-principles cache | 179 entries, 30 confusion types |
| Bibliography | 39+ bibitems |

## Build

All compiled output goes to `out/`.

```bash
make fast                    # quick converging build → out/main.pdf
make                         # full build → out/
make release                 # full rebuild → out/ + iCloud
make test                    # compute test suite
make clean-builds            # remove /tmp/mkd-* isolated build directories
```

Each build runs in its own `/tmp/mkd-calabi-yau-quantum-groups-<NS>/`
directory, so parallel agents never clobber each other. Set
`MKD_BUILD_NS` for warm rebuilds across invocations:

```bash
export MKD_BUILD_NS="agent-$$"
make fast                         # warm on second call
```

Requires TeX Live 2024+ with pdflatex.
