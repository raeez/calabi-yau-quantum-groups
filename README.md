<p align="center">
  <br>
  <br>
  <strong><samp>CALABI-YAU QUANTUM GROUPS</samp></strong>
  <br>
  <samp>Chiral Algebras from Calabi-Yau Categories via E<sub>1</sub>/E<sub>2</sub> Factorization</samp>
  <br>
  <br>
  <a href="#the-thesis">Thesis</a> &middot;
  <a href="#architecture">Architecture</a> &middot;
  <a href="#compute">Compute</a> &middot;
  <a href="#build">Build</a> &middot;
  <a href="#status">Status</a>
  <br>
  <br>
</p>

---

<br>

> *The combinatorial skeleton of a Calabi-Yau threefold &mdash; its lattice, BPS spectrum, and symmetries &mdash; is the root datum of a quantum vertex chiral group G(X), an infinite-dimensional algebraic object that simultaneously generalizes Kac-Moody algebras, Borcherds superalgebras, affine Yangians, and vertex algebras. The bar complex of the associated chiral algebra is simultaneously a factorization coalgebra, a BKM superalgebra, a BPS spectrum, and an automorphic form.*

<br>

## The Thesis

**Volume III** of the modular Koszul duality programme.

| Volume | Title | Scope |
|:------:|-------|-------|
| I | *Modular Koszul Duality* | The bar-cobar machine for chiral algebras on curves |
| II | *A-infinity Chiral Algebras and 3D HT QFT* | The Swiss-cheese interpretation in three dimensions |
| **III** | **Calabi-Yau Quantum Groups** | **CY categories as quantum chiral algebras** |

The central question: *in what precise sense is a Calabi-Yau category a quantum chiral algebra?*

The answer passes through the **E<sub>1</sub>/E<sub>2</sub> chiral hierarchy**:

```
E_1  (associative)    =  CoHA  =  positive half of G(X)  =  tree-level / brane algebra
E_2  (braided)        =  full QVCG  =  Drinfeld double  =  quantum group R-matrix
```

And the **CY dimension** controls the framing:

```
CY_2  -->  E_2 directly  (Yangians, elliptic Hall algebras, Hitchin Hall algebras)
CY_3  =   CY_2 + automorphic correction via Borcherds lift
```

<br>

## The Central Identification

The **shadow Postnikov tower** from Volume I **is** the **automorphic correction** of the BKM superalgebra:

| Arity | Shadow tower | BKM algebra | BPS physics |
|:-----:|:------------|:-----------|:-----------|
| 2 | &kappa; (modular characteristic) | Real roots + Weyl vector | Perturbative spectrum |
| 3 | Cubic shadow *C* | First imaginary roots | 3-body bound states |
| 4 | Quartic shadow *Q* | Deeper imaginary roots | 4-body bound states |
| &infin; | Full &Theta;<sub>A</sub> | Complete BKM g<sub>X</sub> | Full non-perturbative BPS |

The **denominator identity** of the BKM superalgebra **is** the **bar-complex Euler product**:

$$\Phi_X(z) \;=\; e^{-2\pi i\langle\rho,z\rangle} \prod_{\alpha \in \Delta_+} \bigl(1 - e^{-2\pi i\langle\alpha,z\rangle}\bigr)^{\mathrm{mult}(\alpha)}$$

For K3 &times; E, this is the **Igusa cusp form &Delta;<sub>5</sub>** with root multiplicities from the K3 elliptic genus &phi;<sub>0,1</sub>.

<br>

## The Dualities are All the Same Duality

| Face | Statement |
|------|-----------|
| Koszul duality | G(X)<sup>!</sup> exchanges roots and coroots |
| Langlands duality | G(C, G)<sup>!</sup> = G(C, <sup>L</sup>G) |
| S-duality | Electric (W-bosons) &harr; magnetic (monopoles) |
| Mirror symmetry | G(X)<sup>!</sup> = G(X<sup>&vee;</sup>) |
| Holography | CoHA (brane) is Koszul dual to derived center (bulk) |

<br>

## Architecture

```
calabi-yau-quantum-groups/
  main.tex                    Monograph (memoir, EB Garamond)
  working_notes.tex           Standalone working notes
  Makefile                    Build system
  
  chapters/
    theory/                   14 chapter files (Parts I-IV)
    examples/                 6 chapter files (Part V)
    connections/              3 chapter files (Part VI)
  
  appendices/                 Conventions
  
  notes/
    theory_*.tex              11 mathematical theory notes (~12K lines)
    physics_*.tex             11 theoretical physics notes (~10K lines)
    research_*.md             10 combinatorial datum research notes
    audit_*.md                9 adversarial audit reports
  
  compute/
    lib/                      20 Python modules (~24K lines)
    tests/                    22 test suites (~12K lines)
    scripts/                  3 verification scripts
```

<br>

## The Standard Landscape

### K3 &times; E &ensp;|&ensp; The Prototype

The elliptically fibered CY3 X = (S &times; E) / (&Zopf;/N&Zopf;) produces the **BKM superalgebra g<sub>&Delta;<sub>5</sub></sub>** whose denominator identity is the Igusa cusp form of weight 5.

```
Lattice:       &Lambda;^{3,2} = &Lambda;^{1,1} + &Lambda;^{1,1} + [2],  signature (3,2)
Gram matrix:   ((2,-2,-2), (-2,2,-2), (-2,-2,2))
Weyl vector:   &rho; = (1/2)(delta_1 + delta_2 + delta_3),  (&rho;, &delta;_i) = -1
Root mults:    f(nm, l) from &phi;_{0,1}  (K3 elliptic genus)
&kappa;:            5 = weight(&Delta;_5) = h^{1,1}(K3)/4
```

### Toric CY3 &ensp;|&ensp; The Tree Level

The toric diagram determines a quiver Q<sub>X</sub>. The critical CoHA is the positive half of the affine super Yangian.

```
C^3:           CoHA = Y^+(gl-hat_1) = W_{1+infty}     dim Y^+_n = p(n)
Conifold:      Two chambers, pentagon identity, wall-crossing verified
Local P^2:     GV invariants extracted: n_1=3, n_2=-6, n_3=27, n_4=-192
```

### Higgs Sheaves &ensp;|&ensp; The CY<sub>2</sub> Escape

CY<sub>2</sub> categories give E<sub>2</sub> structure directly from the S<sup>2</sup>-framing.

```
Genus 0:       Yangians          (rational R-matrix)
Genus 1:       Elliptic Hall     (elliptic R-matrix, spherical DAHA)
Genus >= 2:    Hitchin algebras  (R-matrices on C x C)
```

### The Quintic &ensp;|&ensp; The Frontier

```
h^{1,1} = 1,  h^{2,1} = 101,  chi = -200
GV:  n^0_1 = 2875,  n^0_2 = 609250,  n^0_3 = 317206375
chi/24 = -25/3  (not integer: obstruction to naive BKM structure)
```

<br>

## Compute

20 modules, 22 test suites, **~1600 tests**.

| Module | What it computes | Tests |
|--------|-----------------|:-----:|
| `phi01_fourier` | K3 elliptic genus &phi;<sub>0,1</sub> via theta functions | 51 |
| `c3_dt_partition` | MacMahon function, plane partitions, Y<sup>+</sup>(gl-hat<sub>1</sub>) | 57 |
| `dd_modular_lattices` | Lattice &Lambda;<sup>3,2</sup>, reflection groups, Weyl vector | 65 |
| `topological_vertex` | AKMV vertex, Schur functions, local P<sup>2</sup> | 151 |
| `igusa_product_formula` | &Delta;<sub>5</sub> via theta constants, Borcherds product (25-58 digit precision) | 79 |
| `affine_yangian_gl1` | Structure function g(z), mode algebra, crystal melting | 81 |
| `bkm_shadow_tower` | Shadow tower projections, arity decomposition (verified arities 2-6) | 67 |
| `elliptic_hall` | E<sub>q,t</sub> Drinfeld presentation, Macdonald representation | 78 |
| `cy_euler` | Hodge diamonds, CY Euler characteristics, &kappa; identification | 85 |
| `wkb_denominator` | Weyl-Kac-Borcherds denominator identity (sum/product agreement) | 54 |
| `higgs_p1_coha` | CoHA of Higgs sheaves on P<sup>1</sup>, Yangian Y(gl<sub>2</sub>) | 84 |
| `borcherds_lift` | General multiplicative lift: Jacobi form &rarr; Siegel modular form | 46 |
| `scattering_diagram` | KS consistency algorithm, GPS tropical vertex | 86 |
| `vafa_witten_k3` | VW(K3, SU(2)) = g<sub>&Delta;<sub>5</sub></sub> via DMVV | 56 |
| `drinfeld_center_coha` | Z(Rep<sup>E<sub>1</sub></sup>(CoHA)) verification, R-matrix unitarity + YBE | 49 |
| `kl_sl2_level1` | Kazhdan-Lusztig equivalence: fusion, R-matrix, modular data, DK theorem | 61 |
| `e2_bar_complex` | First explicit B<sub>E<sub>2</sub></sub>(A): Heisenberg (trivial) and V<sub>k</sub>(sl<sub>2</sub>) (non-trivial) | 93 |
| `hitchin_sl2_genus2` | M<sub>H</sub>(C, SL<sub>2</sub>) for genus 2: Lagrangian CY3-type, Sp<sub>4</sub> connection | 101 |
| `conifold_wall_crossing` | Pentagon identity (Faddeev), DT in both chambers, gauge transformation | 43 |
| `quintic_root_datum` | GV invariants as root multiplicities, &chi;/24 obstruction | 88 |

<br>

## Key Computational Results

**The closed loop** (computationally verified):

```
K3 geometry  -->  VW invariants  -->  DMVV formula  -->  phi_{0,1} coefficients
     |                                                          |
     |                                                          v
     +--  DT partition function  <--  Delta_5  <--  Borcherds product
                                        |
                                        v
                                  BKM root multiplicities  =  shadow tower
```

**The Borcherds product sign**: resolved to 58 decimal digits. The ratio is exactly &minus;1, traced to the unique odd simple root &delta;<sub>3</sub> = f<sub>3</sub> (the fermionic root with discriminant D = &minus;1).

**The scattering diagram**: qualitative agreement (walls forced at all positive roots) but quantitative BCH multiplicities do not match &phi;<sub>0,1</sub>. The gap measures higher BPS bound-state contributions requiring the full motivic Hall algebra.

<br>

## Build

```bash
make fast              # Quick build (manuscript, 2 passes)
make working-notes     # Build working notes
make release           # Full release: manuscript + notes + all tests
make test              # Run ~1600 compute tests
make count             # Manuscript statistics
make dist              # Create distribution archive
```

Requires: pdflatex with memoir/ebgaramond/newtxmath, Python 3.10+ with numpy/pytest (mpmath for high-precision modules).

<br>

## Status

### What is proved

- Generalized root datum axioms CY1-CY7
- E<sub>2</sub>-chiral algebra formalism and bar complex
- **Theorem CY-A<sub>2</sub>**: CY-to-chiral functor for d = 2 (S<sup>2</sup>-framing &rarr; E<sub>2</sub>)
- CoHA = E<sub>1</sub>-sector for toric CY3 (Schiffmann-Vasserot, RSYZ)
- Drinfeld center equivalence (Ben-Zvi-Francis-Nadler, Lurie)
- All lattice theory and BKM constructions for K3 &times; E (Gritsenko-Nikulin)
- Shadow tower arity decomposition (computationally verified arities 2-6, 1600+ tests)

### What is conjectural

- **Conjecture CY-A<sub>3</sub>**: Extension to d = 3 (chain-level S<sup>3</sup>-framing, Drinfeld center route for quantum group braiding)
- **Conjecture CY-C**: Quantum group realization for general CY categories
- The chiral algebra A<sub>K3&times;E</sub> (requires CY-A<sub>3</sub>)
- Langlands = Koszul duality of quantum vertex chiral groups
- Wall-crossing = MC gauge equivalence (at the motivic level)

### The core combinatorial datum

**D = (&Gamma;, S, &Phi;, E<sub>2</sub>)**: a consistent scattering diagram on the tropical skeleton of a CY degeneration, enriched with local vertex algebra data. The KS completion algorithm **is** the shadow tower from Volume I.

<br>

## The Programme

```
CY category  --[Phi]-->  E_2-chiral algebra  --[bar]-->  factorization coalgebra
                                                               |
                                                               |  Euler product
                                                               v
                                                        automorphic form
                                                               |
                                                               |  Borcherds
                                                               v
                                                        BKM superalgebra
                                                               |
                                                               |  representations
                                                               v
                                                     braided monoidal category
                                                               |
                                                               |  Koszul
                                                               v
                                                      Langlands dual G(C, ^LG)
```

<br>

---

<p align="center">
  <samp>Raeez Lorgat &middot; 2026</samp>
</p>
