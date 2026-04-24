# Frontier-resolution lane 4: `G(X)`, centre/hocolim, descended `E_2`

Date: 2026-04-24.

## Claim Attacked

Attack target: the construction of

```tex
G_{\mathrm{adm}}(X) = \mathcal D(Y^+(X))
```

for compact CY3 targets by gluing local positive halves
`Y^+_\alpha(X)`, descending centres through the same atlas, and
recovering the braided `E_2` object only at the centre/representation
level.

The dangerous overclaim is:

```tex
\operatorname{hocolim}_\alpha Z(\operatorname{Rep}^{E_1}(A_\alpha))
  \simeq
Z(\operatorname{Rep}^{E_1}(\operatorname{hocolim}_\alpha A_\alpha)).
```

This is false in general.  The local source already records the
counter-mechanism: `working_notes.tex` label `wn:thm:GX-center-hocolim-criterion`
and `chapters/theory/cy_to_chiral.tex` label `prop:center-hocolim`.
The centre is a wall-invariant/global half-braiding condition, hence
limit/equalizer-like.  The raw hocolim of local centres contains local
central classes that can fail to commute with wall-crossing operators.

## Verdict

The construction is theorem-grade only as an admissible criterion.
General `G(X)` is not constructed.

The native compact CY3 chiral output remains `E_1`.  The `E_2` object is
the descended Drinfeld/chiral centre of the `E_1` representation category,
after centre descent and pairing compatibility have been supplied.

## Proved Core

1. `E_1` hocolim descent is available on the finite acyclic
   toric/quiver/Koszul chart locus.

   Local anchors:
   - `chapters/theory/cy_to_chiral.tex`: `conj:e1-chart-gluing`,
     `thm:toric-chart-gluing`, `thm:e1-descent-degeneration`.
   - `working_notes.tex`: `wn:thm:phi3-witnessed-domain-maximal`.

2. Bar-hocolim is only a shadow comparison.  It does not transport
   centres, braidings, Hopf pairings, antipodes, or Drinfeld doubles.

   Local anchors:
   - `chapters/theory/cy_to_chiral.tex`: `thm:bar-hocolim`,
     proof paragraph ending "No centre, E_2-braiding, Hopf pairing,
     antipode, or Drinfeld double...".
   - `chapters/examples/k3e_cy3_programme.tex`: `prop:bar-hocolim`.

3. The centre-hocolim obstruction is real.

   Local anchors:
   - `chapters/theory/cy_to_chiral.tex`: `prop:center-hocolim`.
   - `working_notes.tex`: "The center-hocolim obstruction" subsection.

   Computed witnesses:
   - `C^3`: obstruction `0`.
   - conifold: local centre dimensions `[2,3]`, hocolim of centres `3`,
     global centre `1`, obstruction `2`.
   - `K3 x E`: not computed away; recorded as massive / BKM-controlled.

4. Positive half, double, and centre are distinct stages.

   Local anchors:
   - `chapters/theory/quantum_groups_foundations.tex`:
     `lem:qgf-coha-double-centre-operadic-level`.
   - `chapters/theory/cy_to_chiral.tex`:
     `def:quantum-vertex-chiral-group`,
     `thm:GofC3-affine-yangian`, `thm:GofK3E-baseline`.

   Type discipline:

   ```tex
   Y^+       : E_1 \text{ Hall algebra},
   D(Y^+)    : quasitriangular Hopf object after Y^-,Y^0,\langle-,-\rangle,
   Z(Rep^{E_1}(Y^+)) : E_2 \text{ braided representation category}.
   ```

## Conditional Bridge

The admissible theorem should be stated as follows.

**Theorem (admissible centre-descended CY-C object).**  Let `X` be a
compact CY3 target equipped with a finite oriented Hall atlas
`{Y^+_\alpha(X)}`.  Assume:

1. `Y^+(X)=hocolim_\alpha Y^+_\alpha(X)` exists in complete `E_1` Hall
   bialgebras.
2. The bar comparison
   `B^{E_1}(Y^+(X)) -> hocolim_\alpha B^{E_1}(Y^+_\alpha(X))`
   is an equivalence on the Koszul/complete chart locus.
3. The centre descent map

   ```tex
   Z_{\mathrm{desc}}(X)
   :=
   \operatorname{Tot} C^\bullet(I,
      Z^{\mathrm{der}}_{\mathrm{ch}}(Y^+_\alpha))
   \longrightarrow
   Z^{\mathrm{der}}_{\mathrm{ch}}(Y^+(X))
   ```

   is an equivalence after the wall-invariant equalizer, completion,
   and radical quotient dictated by the atlas.
4. A Serre-dual negative half `Y^-`, a Cartan completion `Y^0`, and a
   continuous Hopf pairing

   ```tex
   \langle-,-\rangle:
   Y^+(X) \widehat\otimes Y^-(X) \to \widehat k
   ```

   are fixed, nondegenerate after quotienting the radical, and compatible
   with every wall transition:

   ```tex
   \langle K_{\alpha\beta}a, K^-_{\alpha\beta}b\rangle_\beta
     =
   \langle a,b\rangle_\alpha .
   ```

Then

```tex
G_{\mathrm{adm}}(X)
 :=
D(Y^+(X),Y^0,\langle-,-\rangle)
```

is a well-defined completed Hall-Drinfeld double.  The associated
braided object is not `Y^+(X)` and not the native chiral algebra; it is

```tex
Z(Rep^{E_1}(Y^+(X))) \simeq Rep^{E_2}(G_{\mathrm{adm}}(X))
```

on the loci where the centre theorem represents the centre by modules
over the completed double.  The object is terminal among local doubles
whose transition maps preserve the Hopf pairing and centre descent data.

This theorem is exactly a conditional bridge.  It becomes a construction
only after the four displayed inputs are actually built.

## Obstruction Coordinates

Killed or controlled:

```tex
o_{\mathrm{native}\ E_2}
```

is killed by the dimension/shift law: at `d=3`, the native algebra is
`E_1`; no theorem should promote `A_X` itself to `E_2`.

```tex
o_{\mathrm{bar-hocolim}}
```

is killed only on the finite cofibrant Koszul chart locus.  It controls
the CY-B/shadow/bar comparison, not the raw algebraic existence of a
Drinfeld double.

```tex
o_{\mathrm{cent}}(C^3)=0
```

on the single-chart locus.

Surviving:

```tex
o_{\mathrm{cent}}
```

survives for every multi-chart compact CY3 until the wall-invariant
centre totalization maps equivalently to the global centre.  It is
nonzero for the conifold test and unclosed for `K3 x E`.

```tex
o_{\mathrm{pair}}
```

survives until the continuous Hall-Serre/Hopf pairing is constructed,
shown nondegenerate after radical quotient, and proved invariant under
wall transitions.

```tex
o_{\Delta}
```

survives as negative-half and Cartan-completion data.  A positive half
alone is not a double.

```tex
o_{\mathrm{rad}}
```

survives wherever the automorphic radical quotient is not explicitly
identified.  For `K3 x E`, the positive-cone Hall-BKM comparison still
requires this quotient before the doubled map can be theorem-grade.

```tex
o_{\mathrm{prim}}
```

is controlled by the `phi_{0,1}` seed only on the Igusa/K3 boundary
where the Borcherds-Gritsenko-Nikulin input is supplied.  It is not a
general compact CY3 construction.

## `K3 x E` Outcome

Local anchors:
- `chapters/examples/k3e_cy3_programme.tex`:
  `constr:k3e-hcs-hall-borcherds-comparison`,
  `cor:k3e-cy3-platonic-Sp-K3E-explicit`.
- `chapters/theory/quantum_groups_foundations.tex`:
  `prop:qgf-k3e-source-target-comparison-maps`.
- `notes/platonic_resolution_eight_obligations_20260424.md`:
  Resolutions 4 and 5.

What is proved or conditionally organized:

```tex
\Theta_{\mathrm{HCS}\to\mathrm{Hall}}
```

and

```tex
\Theta_{\mathrm{Hall}\to\mathrm{Borch}}
```

compare hCS observables, completed Hall positive-half generators, and
primitive BKM root generators on the same charge lattice when the
oriented datum is supplied.

What is not proved:

```tex
D(\CoHA(K3\times E)) \simeq U_q(\mathfrak g_{\Delta_5})
```

as a completed Hall-Drinfeld double.  That equality still requires the
negative half, Cartan completion, nondegenerate Hopf pairing, automorphic
radical quotient, and centre compatibility.

The Maulik-Okounkov stable envelope supplies the chamber `R`-matrix on
the K3 stable-envelope side.  It can kill the local `R`-matrix
construction problem on MO-accessible loci, but it does not by itself
kill `o_cent` for a compact CY3 atlas.  To descend to `G_adm(K3 x E)`,
the MO wall-crossing operators must be shown compatible with the Hall
pairing, radical quotient, and centre totalization.

## Proof Skeleton

1. Start with the witnessed compact CY3 `E_1` output:
   `working_notes.tex` `wn:thm:phi3-witnessed-domain-maximal` and
   `chapters/theory/cy_to_chiral.tex` `thm:cy-to-chiral-d3`.

2. Assemble the positive half by `E_1` descent only:
   `chapters/theory/cy_to_chiral.tex` `conj:e1-chart-gluing`,
   `thm:toric-chart-gluing`, `thm:e1-descent-degeneration`.

3. Use bar-hocolim only for shadow compatibility:
   `chapters/theory/cy_to_chiral.tex` `thm:bar-hocolim`.

4. Replace raw hocolim of centres by centre totalization/equalizer:
   `chapters/theory/cy_to_chiral.tex` `prop:center-hocolim` gives the
   obstruction; `working_notes.tex` `wn:thm:GX-center-hocolim-criterion`
   and `wn:thm:GX-admissible-construction` give the admissible package.

5. Form the Drinfeld double only after pairing data:
   `chapters/theory/quantum_groups_foundations.tex`
   `thm:quantum-group-as-positive-geometry-double` and
   `lem:qgf-coha-double-centre-operadic-level`.

6. Put the `E_2` structure on the centre/representation category:
   `chapters/theory/cy_to_chiral.tex` `rem:e2-on-drinfeld-centre`,
   `constr:rmatrix-from-center`, `thm:c3-drinfeld-center`.

7. For `K3 x E`, use the source-target decomposition:
   `chapters/theory/quantum_groups_foundations.tex`
   `prop:qgf-k3e-source-target-comparison-maps`; the positive-half
   comparison is not the full BKM double before Step 5.

## Primary Source Anchors Needed

- Beilinson-Drinfeld, *Chiral Algebras*, for chiral/factorization
  categories and chiral pairings.
- Lurie, *Higher Algebra*, for Dunn additivity, factorization homology,
  and higher algebraic centres.
- Ben-Zvi-Francis-Nadler / Francis 2013, for the Drinfeld centre of an
  `E_1`-monoidal category as the `E_2` centre.
- Ayala-Francis, for factorization homology and pair-factorization
  centre technology.
- Maulik-Okounkov 2012, stable envelopes, especially Definition 4.2.1,
  Theorem 4.6.1, and the stable-envelope pairing/R-matrix locus.
- Kontsevich-Soibelman 2008 and Toën 2007, for motivic DT, CY
  categories, and descent of dg categories.
- Drinfeld 1987 and Majid 1995, for Hopf pairings and Drinfeld doubles.
- Schiffmann-Vasserot, Davison-Meinhardt, and RSYZ for constructed toric
  CoHA positive halves and doubles.
- Borcherds, Gritsenko-Nikulin, and Gritsenko-Clery for the
  `K3 x E` denominator and `kappa_BKM=c(0)/2` input.

## Computations / Tests Run

```bash
pytest compute/tests/test_drinfeld_center_hocolim.py \
       compute/tests/test_swiss_cheese_chart_gluing.py \
       compute/tests/test_bar_hocolim_commutation.py \
       compute/tests/test_compact_hall_construction_package.py -q
```

Result:

```text
273 passed in 1.53s
```

## Files Changed

Created:

```text
notes/frontier_resolution_swarm_20260424_gx_center_hocolim.md
```

No edits were made to `working_notes.tex` or to files outside the
assigned write scope.
