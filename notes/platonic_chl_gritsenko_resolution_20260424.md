# CHL Versus Gritsenko-Clery Normalization Resolution

## Claim Attacked

The row `{5,4,3,2,2}` in Vol II `FRONTIER.md` was advertised as the value
of the three-factor trace identity
`tr_ghost(Q_BRST^2) = tr_Pentagon = omega_Borcherds = c_N(0)/2`
at `N in {1,2,3,4,6}`.

## Failure Mode

The row is not a valid scope.

- CHL-averaged BKM-denominator scope: `N in {1,2,3,4,6}` has
  `c_N(0)=(10,8,6,4,2)` and
  `kappa_BKM(Phi_N)=c_N(0)/2=(5,4,3,2,1)`.
- Gritsenko-Clery eight-form atlas: the separate triple-indexed
  simplest-divisor forms have weights
  `kappa_BKM=(5,2,3,1,2,1/2,3/2,1)` in the live Vol III
  two-scope theorem.
- The two scopes overlap only at the common `Delta_5` row. They are not
  two enumerations of one linear `N`-indexed table.

Thus `{5,4,3,2,2}` takes the first four CHL entries and an invalid
terminal entry; it is neither the CHL row nor the Gritsenko-Clery atlas.

## Local Anchors

- `chapters/examples/cy_d_kappa_stratification.tex:159`: declares the
  two-scope split.
- `chapters/examples/cy_d_kappa_stratification.tex:168`: gives CHL
  weights `(5,4,3,2,1)` and constants `(10,8,6,4,2)`.
- `chapters/examples/cy_d_kappa_stratification.tex:2053`: states
  `kappa_BKM(Phi_N)=c_N(0)/2` for the five CHL frame shapes.
- `chapters/examples/cy_d_kappa_stratification.tex:2121`: repeats
  the CHL constants `(10,8,6,4,2)`.
- `chapters/examples/cy_c_six_routes_convergence.tex:1108`: records
  the live Gritsenko-Clery eight-form catalogue as the triple-indexed
  row `(5,2,3,1,2,1/2,3/2,1)`.
- `FRONTIER.md:45`: carries the same live eight-form row.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:393`
  and older cache entries record a stale Scope B row; those are not
  strong enough to override the live theorem surface.

## Exact Normalization Statement

Use

`kappa_BKM(Phi_N)=c_N(0)/2`

only after naming the family:

- `Phi_N^{CHL}`: CHL-averaged BKM-denominator scope,
  `N in {1,2,3,4,6}`, values `(5,4,3,2,1)`.
- `F_{t,N}^{GC}`: Gritsenko-Clery simplest-divisor atlas, eight
  triple-indexed rows, values `(5,2,3,1,2,1/2,3/2,1)`.

The physical Igusa square / dyon-counting convention is a third
normalization and must not be silently substituted for either row.

## Remaining Primitive Obligations

1. Choose the default Stage-2 `Phi_N` notation in reader-facing Vol III:
   either CHL-averaged `Phi_N^{CHL}` or twined/singular-weight notation,
   but not an unsuperscripted mixture.
2. Reconcile older cache entries and `cy_d_kappa_stratification.tex`
   occurrences against the live two-scope theorem.
3. Split compute oracles so the diagonal Nikulin eight-order table is
   not used as the Gritsenko-Clery atlas.
4. Audit remaining live `FRONTIER.md` and chapter references for the
   stale terminal value `2` at CHL order `N=6`.
