# Platonic Resolution of the Eight Positive-Cone / Homotopy-Gluing Obligations

Date: 2026-04-24.

## Principle

The eight obligations are not eight unrelated problems.  They are the
eight faces of one typed object:

```tex
\mathcal P^{BPS}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 =
(\mathcal H^{mot,or}_{\sigma,-}, Int^{mot}, Real, Dec, Enh)
```

over the chamber-sector base

```tex
(X,\sigma,Q,S,o,T_{\mathrm{eq}}).
```

The local-to-global mechanism is DWR/Cech/Ran descent.  The positive
geometry is the decategorified support/completion system extracted by
`Dec`.  The Igusa positive cone is the first non-toric automorphic
boundary of this object.  The Hall--Drinfeld double is an enhancement,
not part of the positive half.

The platonic resolution is therefore:

```tex
\text{construct the positive half as a Hall cosheaf;}
\quad
\text{integrate it to a chambered quantum torus;}
\quad
\text{attach optional typed enhancements.}
```

Each optional enhancement has its own input data and obstruction class.
No enhancement is obtained by naming the positive half.

## Resolution 1. Compact `K3 x E` Oriented Critical Hall Cosheaf

**Object.**

```tex
\mathcal H^{mot,or}_{K3\times E,\sigma,-}:
\mathsf{Sect}_{\sigma}(D^b\operatorname{Coh}(K3\times E))
  \longrightarrow
\mathsf{CAlg}^{\wedge}_{\mathsf{Mot}}
```

on the full DWR/Cech/Ran site.

**Construction.**  For a finite DWR simplex

```tex
\tau=(I,\{P_i\Subset U_{i,0}\cap\cdots\cap U_{i,p}\}_{i\in I})
```

define

```tex
\mathcal H^{mot,or}_{K3\times E,\sigma,S}(\tau)
 =
\widehat{\bigoplus}_{\gamma\in\Gamma_{\sigma,S}^{I}}
\widehat{\bigotimes}_{i\in I}
H^{BM}_{G_{\gamma_i}}
(\operatorname{Crit}(f_{P_i,\gamma_i}),
 \phi_{f_{P_i,\gamma_i}}\otimes\mathscr L_{o_{P_i,\gamma_i}})
[s(P_i,\gamma_i)](t(P_i,\gamma_i)).
```

The structure maps are restriction/refinement pushforwards,
disjoint-union factorisation, and Hall extension correspondences.  The
orientation output is Joyce--Kontsevich--Soibelman:

```tex
OrOut=Or^0\sqcup Or^{tw}(c_o).
```

`K3 x E` carries the untwisted branch on the product-compatible locus by
the global volume form `Omega_K3 wedge Omega_E`; twisted branches remain
allowed in the typed category.

**Status.**  Conditional construction.  The formula is a definition once
the oriented `(-1)`-shifted critical atlas and orientation branch are
supplied.  Compact `K3 x E` supplies the canonical product orientation,
but the full motivic atlas and all overlap compatibilities remain part
of the input datum.

**Obstruction.**

```tex
o_{\mathrm{HallCosheaf}}
 =
(o_{\mathrm{atlas}},o_{\mathrm{or}},o_{\mathrm{HN}},o_{\mathrm{TS}}).
```

The cosheaf exists exactly when the oriented critical atlas glues, the
orientation branch is coherent on triple overlaps, the HN sector
completion is locally finite, and the Thom--Sebastiani associator is
coherent.

## Resolution 2. Global `Theta^{or}_{hCS -> Hall}`

**Object.**

```tex
\Theta^{or}_{\hCS\to\Hall}:
\Obs^q_{\hCS}(-,\mathfrak g)
  \longrightarrow
\CoHA^{or}_{crit}(-)
```

as a continuous natural transformation on the full DWR/Cech/Ran nerve.

**Construction.**  A local stationary-phase calibration is a family

```tex
\theta_{P,\gamma}:
\Obs^q_{\hCS}(P,\mathfrak g)
\to
H^{BM}_{G_\gamma}
(\operatorname{Crit}(f_{P,\gamma}),
 \phi_{f_{P,\gamma}}\otimes\mathscr L_{o_{P,\gamma}})
[s(P,\gamma)](t(P,\gamma)).
```

The global map exists if these maps satisfy:

```tex
chain,\quad compact-support Beck-Chevalley,\quad Cech/Ran naturality,
\quad Hall convolution,\quad orientation transport,\quad HN completion,
\quad wall-crossing transport.
```

Equivalently, the five obstruction tuple of
`cy3_chain_level_bridge.tex` vanishes:

```tex
\mathfrak o(\theta)
 =
(o_{\mathrm{MC}},o_{\mathrm{or}},o_{\mathrm{gr}},
  o_{\mathrm{TS}},o_{\mathrm{fact}})
 =
0.
```

**Status.**  The descent criterion is proved: supplied local maps glue
iff the obstruction tuple vanishes and the degree-zero MC solution is
invertible.  The existence of the local stationary-phase maps on compact
`K3 x E` is conditional.

## Resolution 3. `AutBorch` as a Functor

**Object.**

```tex
\operatorname{AutBorch}:
K_0(BPS^{mot,prim}_{\Lambda,S,o})
  \longrightarrow
\mathsf{BorchDen}_{(2,n)}
```

where the target is the groupoid of automorphic denominator data:

```tex
(L,\Gamma^+,\rho,\epsilon,\Psi,\operatorname{div}\Psi,\operatorname{den}).
```

**Construction.**  A primitive BPS motive gives a vector-valued weak
Jacobi input after realization:

```tex
\mathbb U^{mot}
\mapsto
\phi(\tau,z)=\sum c(n,l)q^nr^l.
```

If the input satisfies the Borcherds lift hypotheses
integrality/weak-holomorphy, discriminant boundedness, lattice
compatibility, and orientation character compatibility, define

```tex
\operatorname{AutBorch}(\mathbb U^{mot})
 =
\operatorname{Borch}(\phi).
```

For the Igusa boundary:

```tex
\phi=\phi_{0,1},\qquad
\operatorname{AutBorch}(\phi_{0,1})=\Delta_5,\qquad
\kappa_{\mathrm{BKM}}=c_1(0)/2=5.
```

**Status.**  Proved for the Igusa input by Borcherds--Gritsenko--
Nikulin.  A genuine functor exists on the full subcategory of primitive
BPS motives whose realized Jacobi input satisfies the lift hypotheses.
Universal construction for all compact CY3 motives is conjectural.

## Resolution 4. Hall--BKM Comparison

**Object.**

```tex
\Psi^+_{\Hall\to\BKM}:
\CoHA^{or}_{crit}(K3\times E)_{\sigma,S}^{num}
\longrightarrow
U(Y^+(\mathfrak g_{\Delta_5}))_{num}.
```

**Construction.**  The comparison factors through the automorphic
radical quotient of the sector-completed Hall algebra:

```tex
\CoHA^{or}_{crit}
  \xrightarrow{Int^{mot}}
\widehat{\mathbb T}_{\Gamma_{\mathrm{eff}},\nu_{\Delta_5}}
  \twoheadrightarrow
\widehat{\mathbb T}_{\Gamma_{\mathrm{eff}},\nu_{\Delta_5}}/Rad_{\Delta_5}
  \hookrightarrow
U(Y^+(\mathfrak g_{\Delta_5}))_{num}.
```

The primitive seed is

```tex
\phi_{0,1}=r^{-1}+10+r+O(q).
```

The chamber is

```tex
\Gamma_{\mathrm{eff}}
 =
\{m>0,n\ge0\}\cup\{m=0,n>0\}\cup\{m=n=0,l<0\}.
```

The Lorentzian degree is

```tex
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2},
```

and signed multiplicities are

```tex
\operatorname{smult}(\alpha(n,l,m))=f(nm,l).
```

**Status.**  The Igusa denominator equality proves the target
root-multiplicity system.  The Hall-to-denominator map is conditional
on identifying the primitive Hall motive with the `\phi_{0,1}` seed and
on quotienting by the automorphic radical.

## Resolution 5. Compact Hall--Drinfeld Double

**Object.**

```tex
\mathcal D_\hbar(\CoHA^{or}_{crit}(K3\times E))
 =
Y^- \widehat\bowtie Y^0 \widehat\bowtie Y^+.
```

**Construction data.**

```tex
Y^+ = \CoHA^{or}_{crit}(K3\times E)_{\sigma,S}^{\wedge},
\qquad
Y^- = \mathbb D_{\mathrm{Serre}}(Y^+),
```

```tex
Y^0=\widehat{\mathbb C[\Lambda_{K3}]},
\qquad
\Lambda_{K3}=H^{even}(K3,\mathbb Z)\cong II_{4,20}.
```

The double exists after:

```tex
\Delta:Y^+\to Y^+\widehat\otimes Y^+,
\quad
\langle-,-\rangle:Y^+\widehat\otimes Y^-\to\widehat{\mathbb C},
\quad
\operatorname{Rad}\langle-,-\rangle,
\quad
Z(\operatorname{Rep}^{E_1}(Y^+))\text{ compatibility}.
```

The Borcherds associator is the boundary enhancement:

```tex
\Phi_{\Delta_5}\in
\mathcal D_\hbar^{\otimes3}[[\Delta_5^{-1}]]
```

on the paramodular locus where the denominator is nonzero.

**Status.**  This is the main CY-C frontier.  The positive half is
separated from the double.  No homotopy-colimit construction of the
positive half implies the double without dualisability, coproduct,
pairing, completion, radical quotient, and centre compatibility.

## Resolution 6. Wall-Crossing Equals Descent Transport

**Object.**

```tex
Dec(T_{\wp}^{DWR}) = \operatorname{Ad}_{KS(\wp)}
```

for any admissible wall path `wp`.

**Construction.**  On the Hall side, a wall path is a chain of sector
refinements and tilts in the DWR descent category.  On the quantum-torus
side it is the KS product

```tex
A_S(\sigma)
 =
\prod_{\ell\subset S}^{clockwise}
\prod_{Z_\sigma(\gamma)\in\ell}
\mathbb E(x_\gamma)^{\Omega^{mot}_{\sigma,o}(\gamma)}.
```

The theorem is finite-first:

```tex
Dec(T_{\wp,N,R}^{DWR})=\operatorname{Ad}_{KS_{N,R}(\wp)}
```

for every charge-height and central-charge-radius truncation, then pass
to the inverse limit.

**Status.**  Proved for supplied motivic Hall cosheaves by functoriality
of motivic integration.  Concrete compact CY3 verification requires the
cosheaf of Resolution 1 and the comparison map of Resolution 2.

## Resolution 7. Manuscript Validation

**Object.**  The new material lives in three surfaces:

```tex
notes/homotopy_gluing_positive_cone_synthesis_20260424.md,
notes/platonic_resolution_eight_obligations_20260424.md,
chapters/theory/gluing/sec_10_unifying.tex.
```

**Decision.**  The theorem
`gluing:thm:positive-cone-descent-index` should stay in
`sec_10_unifying.tex` for now.  It is not a standalone positive-geometry
chapter yet; it is the terminal synthesis of the gluing chapter.  A
future split is justified only after Resolutions 1, 2, and 6 are
constructed beyond the supplied-datum theorem.

**Validation.**  Run:

```bash
pytest compute/tests/test_positive_cone_gluing_bridge.py \
       compute/tests/test_platonic_resolution_registry.py -q
make fast
```

The build result is the verdict on labels/macros after inscription.

## Resolution 8. Cross-Repo Propagation to `~/igusa-cusp-form`

**Object.**  The Igusa side receives a compatibility note:

```tex
agent_material/06_vol3_homotopy_positive_cone_dictionary.tex
```

and the main manuscript includes it before the bibliography.

**Dictionary.**

```tex
\text{DWR/Cech/Ran Hall cosheaf}
\quad\longleftrightarrow\quad
\text{chambered positive cone after }Dec,
```

```tex
\Gamma_{\mathrm{eff}}
\xrightarrow{\alpha}
\Poly_{II},
\qquad
\epsilon_o=\nu_{\Delta_5},
\qquad
\operatorname{AutBorch}(\phi_{0,1})=\Delta_5,
```

```tex
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
Z^X_{\square}=C_{\square}\Delta_5^{-2}.
```

**Status.**  Propagation is terminological and normalisation-preserving.
It does not add a new BKM theorem to the Igusa paper.

## Closed Core and Open Frontier

The closed core is:

```tex
\text{DWR/Cech/Ran descent from supplied oriented Hall data}
\Rightarrow
\text{chambered positive geometry after }Dec.
```

The Igusa boundary arithmetic is closed:

```tex
\phi_{0,1}\mapsto\Delta_5,\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
\kappa_{\mathrm{BKM}}=5.
```

The open frontier is exactly:

```tex
\text{construct the compact }K3\times E\text{ Hall cosheaf,}
\quad
\Theta^{or}_{\hCS\to\Hall},
\quad
\mathcal D_\hbar,
\quad
\Psi^+_{\Hall\to\BKM}
```

without supplying them as hypotheses.
