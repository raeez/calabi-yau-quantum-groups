# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization
Algebras on Algebraic Curves*, by Raeez Lorgat.

This volume studies the Calabi-Yau-to-chiral correspondence
\[
\Phi_d : \mathrm{CY}\text{-cat}_d \longrightarrow \mathrm{ChirAlg}
\]
and the quantum groups that arise from its canonical geometric examples:
K3 surfaces, K3-fibered Calabi-Yau threefolds, toric Calabi-Yau
threefolds, local surfaces, and Borcherds--Kac--Moody denominator
algebras. The central question is how a Calabi-Yau category produces a
chiral algebra, how its bar construction records BPS and Hall-algebraic
data, and how the resulting invariants compare with automorphic products.

The theorem scope is dimension-stratified.

- At \(d = 2\), the construction of \(\Phi_2\) is proved on the smooth
  proper Calabi-Yau surface locus. For K3 this gives the Mukai-lattice
  \(E_2\)-chiral algebra and \(\kappa_{\mathrm{ch}} = 2\).
- At \(d = 3\), the available theorem is the framed object-level
  assignment
  \[
  \Phi_3^{(\Sigma_2,C)}(\mathcal{C})
  =
  \mathrm{Sp}_{\Sigma_2,C}(\Phi^{\mathrm{FA}}_3(\mathcal{C}))
  \]
  under the stated H1--H4 hypotheses and a fixed specialisation datum.
  Toric and K3-fibered loci provide the main verified examples. Compact
  non-formal Calabi-Yau threefolds still require their own chain-level
  witnesses: strictified TCFT data, filtered Hochschild comparison,
  analytic completion, and an explicit \(S^3\)-framing homotopy.
- For \(d \geq 3\), the native output \(A\) is \(E_1\)-chiral. The
  braided \(E_2\) structure lives on the Drinfeld or derived centre,
  such as \(\mathcal{Z}(\mathrm{Rep}^{E_1}(A))\), under the relevant
  hypotheses.

## Mathematical Spine

The volume is organised around five interlocking constructions.

- **The functorial construction.** The first stage builds a factorisation
  algebra from Calabi-Yau data; the second stage specialises along
  \((\Sigma_{d-1}, C)\) to an ordered chiral target on a curve.
- **Bar--cobar and Hochschild calculus.** The bar complex \(B(A)\), its
  Euler product, and Hochschild shadows supply the bridge to Volumes I
  and II.
- **Cohomological Hall algebras.** For \(\mathbb{C}^3\),
  \(\mathrm{CoHA}(\mathbb{C}^3) \simeq
  Y^+(\widehat{\mathfrak{gl}}_1)\), the positive half. The full
  \(\mathcal{W}_{1+\infty}\) comparison enters only after the
  Drinfeld-centre, Drinfeld-double, or completion passage dictated by
  the example.
- **K3 quantum groups.** The K3 Yangian chapter concerns the Mukai
  self-mirror branch. The BKM object attached to \(K3 \times E\) is the
  Hall--Drinfeld double of the compact oriented positive Hall half once
  the compact double datum is supplied.
- **Borcherds products.** The K3-fibered class is controlled by
  Gritsenko--Nikulin and Borcherds denominator identities, with
  \[
  \kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2.
  \]

## Invariants

The invariant names are always subscripted.

- \(\kappa_{\mathrm{ch}}\): the chiral-side modular characteristic. On
  compact Calabi-Yau inputs it is read through the Hodge supertrace
  \[
  \kappa_{\mathrm{ch}}(A_X)=\sum_q(-1)^q h^{0,q}(X).
  \]
- \(\kappa_{\mathrm{cat}}\): the categorical Euler characteristic
  \(\chi(\mathcal{O}_X)\), multiplicative under products.
- \(\kappa_{\mathrm{BKM}}\): the Borcherds weight \(c_N(0)/2\) when a
  Borcherds lift is present.
- \(\kappa_{\mathrm{fiber}}\): the fibre or lattice contribution, kept
  separate from total-space invariants.

For \(K3 \times E\),
\[
\kappa_{\mathrm{cat}}(K3 \times E)=
\chi(\mathcal{O}_{K3})\chi(\mathcal{O}_E)=2\cdot 0=0.
\]
The four values
\[
\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}\}(K3 \times E)
=\{0,3,5,24\}
\]
come from four distinct constructions: total-space Euler characteristic,
Heisenberg--Mukai chiral specialisation, the \(\Delta_5\) Borcherds
weight, and the Mukai-lattice rank of the K3 fibre.

## Volume Structure

- **I. Foundations.** Calabi-Yau categories, cyclic \(A_\infty\)
  structures, factorisation algebras, and \(E_n\)-operations.
- **II. The Calabi-Yau-to-chiral construction.** The two-stage
  construction of \(\Phi_d\), the \(d = 2\) theorem, and the framed
  \(d = 3\) object-level theorem.
- **III. Chiral quantum groups.** Ordered \(E_1\)-chiral algebras,
  Drinfeld centres, braided factorisation, and \(R\)-matrix data.
- **IV. K3 and K3-fibered examples.** The Mukai self-mirror Yangian
  branch, the \(K3 \times E\) BKM branch, and Hall--Drinfeld doubles.
- **V. Calabi-Yau landscape.** Toric threefolds, local surfaces,
  conifold and local \(\mathbb{P}^2\), derived categories, Fukaya
  categories, and matrix factorisations.
- **VI. Seven faces of \(r_{\mathrm{CY}}\).** Bar--cobar,
  modular-Koszul, Hall, automorphic, physical, centre, and shadow
  realisations of the same comparison problem.
- **VII. Frontiers.** Compact non-formal \(d = 3\) chain-level
  strictification, non-abelian K3 extensions, higher-dimensional
  siblings, and the construction of \(G(X)\) beyond verified loci.

## Build

Compiled output is written to `out/`.

```bash
make fast                    # quick build to out/main.pdf
make                         # full build
make release                 # full rebuild plus release copy
make test                    # compute test suite
make verify-independence     # theorem/source independence checks
make clean-builds            # remove isolated temporary build directories
```

Builds use isolated `/tmp/mkd-calabi-yau-quantum-groups-<NS>/`
directories. Set `MKD_BUILD_NS` to reuse one namespace across commands:

```bash
export MKD_BUILD_NS="readme-$$"
make fast
```

Requires TeX Live 2024 or newer with `pdflatex`.

## Repository Landmarks

- `main.tex`: manuscript entry point.
- `chapters/theory/cy_to_chiral.tex`: construction of \(\Phi_d\) and
  the dimension-stratified scope.
- `chapters/examples/cy_d_kappa_stratification.tex`: canonical
  subscripted invariant tables and compact-family formulas.
- `chapters/examples/k3_yangian_chapter.tex`: Mukai self-mirror K3
  Yangian branch.
- `chapters/examples/k3e_bkm_chapter.tex`: \(K3 \times E\)
  Borcherds and BKM branch.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex`: Hall--Drinfeld
  double architecture.
- `compute/`: executable checks for numerical and structural claims.
- `scripts/hooks/beilinson-gate.sh`: local manuscript consistency gate.
