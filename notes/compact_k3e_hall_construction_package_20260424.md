# Compact K3 x E Hall Construction Package

Date: 2026-04-24.

## First-Principles Object

The eight requested constructions are one datum:

```tex
\mathfrak D_{K3\times E}
 =
(\mathfrak U,\mathfrak C,o_X,\mathrm{HN},Int^{mot},
 \theta,\mathbb U^{mot}_{prim},Rad_{\Delta_5},
 \Delta_+,\langle-,-\rangle,Z_{\mathrm{cent}}).
```

Here `\mathfrak U` is the DWR/Cech/Ran cover, `\mathfrak C` is the
oriented critical atlas, `o_X` is the orientation branch, `HN` is the
sector completion, `Int^{mot}` is motivic integration, `\theta` is the
hCS-to-Hall Maurer-Cartan solution, `\mathbb U^{mot}_{prim}` is the
primitive BPS seed, `Rad_{\Delta_5}` is the automorphic radical, and the
last three entries are exactly the double data.

The obstruction vector is:

```tex
\mathfrak O_{K3\times E}
 =
(o_{\mathrm{atlas}},o_{\mathrm{or}},o_{\mathrm{HN}},o_{\mathrm{TS}},
 o_{\mathrm{MC}},o_{\mathrm{gr}},o_{\mathrm{fact}},
 o_{\mathrm{prim}},o_{\mathrm{rad}},o_{\Delta},o_{\mathrm{pair}},
 o_{\mathrm{cent}}).
```

The construction closes exactly when this vector vanishes.

## Outputs

1. `\mathcal H^{mot,or}_{K3\times E,\sigma,-}` is the completed direct
   sum of oriented vanishing-cycle Borel-Moore groups on the full
   DWR/Cech/Ran nerve.  The structure maps are restriction/refinement,
   disjoint-union factorisation, and Hall extension correspondences.

2. `\Theta^{or}_{\hCS\to\Hall}` is the descended natural transformation
   produced by the Maurer-Cartan solution `\theta` in the comparison
   complex.

3. `AutBorch` is a functor on the subcategory of primitive BPS motives
   whose realizations satisfy the Borcherds lift hypotheses.

4. The Hall-BKM comparison is the composition:

```tex
\CoHA^{or}_{crit}
  \xrightarrow{Int^{mot}}
\widehat{\mathbb T}_{\Gamma_{\mathrm{eff}},\nu_{\Delta_5}}
  \twoheadrightarrow
\widehat{\mathbb T}_{\Gamma_{\mathrm{eff}},\nu_{\Delta_5}}/Rad_{\Delta_5}
  \hookrightarrow
U(Y^+(\mathfrak g_{\Delta_5}))_{num}.
```

5. The compact Hall-Drinfeld double is:

```tex
\mathcal D_\hbar
 =
(Y^-\widehat\bowtie Y^0\widehat\bowtie Y^+)/
\operatorname{Rad}\langle-,-\rangle.
```

It exists only after the negative half, Cartan completion, continuous
Hopf pairing, radical quotient, bracket comparison, and centre
compatibility are supplied.

6. Wall crossing equals DWR descent transport finite-first:

```tex
Dec(T^{DWR}_{\wp,N,R})=\operatorname{Ad}_{KS_{N,R}(\wp)}
```

for every charge-height and central-charge-radius truncation, then by
inverse limit.

## Igusa Boundary

The Igusa boundary remains the closed arithmetic anchor:

```tex
\operatorname{AutBorch}(\phi_{0,1})=\Delta_5,
\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5.
```

The positive cone and denominator normalisation do not construct the
double.  They determine the positive support and the automorphic radical
through which the Hall-BKM comparison factors.

## Remaining Exact Problem

The compact CY-C theorem is equivalent to:

```tex
\mathfrak O_{K3\times E}=0.
```

Every unresolved item in the eight-part list is one coordinate of this
vector.  The false shortcut is to infer the double from the positive
half; the correct construction supplies coproduct, negative half,
Cartan, continuous pairing, radical quotient, and centre compatibility
as separate data.

