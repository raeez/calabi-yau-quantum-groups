# Platonic K3xE Double Resolution

## Claim Attacked

Positive-half Hall data for `K3 x E` had been read too strongly as a
completed Hall-Drinfeld double and as a BKM/Super-Yangian current
object.  The dangerous implication was:

```text
character equality / positive half
  => compact critical CoHA
  => negative half and Hall pairing
  => completed double
  => BKM current object
```

Only the first arrow is theorem-grade at the present surface.

## Failure Mode

The curve-stalk DWR/Ran atlas constructs a positive-half cosheaf and
monodromy cocycles.  It does not construct:

- an oriented compact critical CoHA on all of `K3 x E`;
- a nondegenerate finite-height positive-negative Hall pairing;
- a negative half as continuous graded dual modulo the Borcherds Cartan
  radical;
- a Hall coproduct whose associated graded is the primitive enveloping
  coproduct;
- equality of the Hall kernel with the Borcherds-Serre ideal;
- absence of extra primitive central classes;
- a pro-cone completion with compatible Siegel-Borcherds associator.

The denominator character `-Phi_10^{-1} = -Delta_5^{-2}` and
`kappa_BKM(Delta_5) = c_1(0)/2 = 5` remain theorem-grade.  They do not
construct any of the double data.

## Repair

Added a finite-height obstruction criterion:

- `chapters/examples/k3e_bkm_chapter.tex`
  - `cor:k3e-finite-height-promotion-obstruction`
  - repaired `thm:k3e-hall-drinfeld-super-yangian-criterion`
  - repaired `thm:k3e-bps-lie`
  - scoped `thm:plat-Sp-K3E` to the compact Hall promotion locus
- `chapters/theory/gluing/sec_8_k3xe_master.tex`
  - `gluing:rem:k3xe-finite-height-double-obstruction`

The criterion is formal and theorem-grade: a proposed
`Psi^+_{Hall->BKM}` promotes to a completed Hall-Drinfeld/BKM object iff
the finite-height primitive/PBW, pairing, coproduct, Serre, centre, and
completion/associator conditions hold at every height and commute with
transition maps.  One failed height obstructs promotion.

## Preserved Conventions

- `K3 x E` total-space spectrum remains `{0, 3, 5, 24}`.
- `chi(O_K3) = 2` remains a fibre witness only.
- `kappa_BKM(Delta_5) = 5` remains the Borcherds weight of the
  primitive denominator, not a chiral modular characteristic.
