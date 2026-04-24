# Frontier Resolution Lane 6: N=5,7,8 Hosts and AutBorch

## Claim attacked

The attacked claim is the promotion of the N=5,7,8 boundary automorphic
rows to compact CHL Calabi--Yau threefold denominator theorems, and the
parallel promotion of `AutBorch` from a Borcherds-denominator
construction to a primitive-BPS-motive-to-Hall-algebra functor.

Verdict: the promotion fails. The exact automorphic constants are known
in their declared normalisations, but compact CY_3 host data are not
supplied. A bare product `K3 x E`, and even a free translation quotient
of it, does not supply the missing cover, automorphic line, partition
function, or root-multiplicity identification.

## Proved core

The live host criterion is `working_notes.tex:23541-23567`. A boundary
row N in `{5,7,8}` becomes a compact CY_3 denominator theorem only after
one supplies

```tex
(X_N, \widetilde\Gamma_N, \mathcal L_N, Z_N)
```

where `X_N` is a compact or stacky/metaplectic compact CY_3 with reduced
DT orientation theory, `\widetilde\Gamma_N` makes the multiplier honest,
`\mathcal L_N` is the automorphic line of weight `c_N(0)/2`, `Z_N` is
the reduced DT/chiral character equal to the corresponding Borcherds
product, and root multiplicities are Fourier coefficients of the same
Jacobi input that computes `Z_N`.

For the order-indexed Nikulin/Gritsenko boundary ladder used by
`working_notes.tex:23479-23521`, the constants are

| N | `c_N(0)` | `\kappa_{\mathrm{BKM}}=c_N(0)/2` | current status |
|---|---:|---:|---|
| 5 | 4 | 2 | automorphic boundary constant; host witness required |
| 7 | 2 | 1 | automorphic boundary constant; host witness required |
| 8 | 2 | 1 | automorphic boundary constant; host witness required |

This is the same order-indexed lane recorded in
`chapters/examples/cy_d_kappa_stratification.tex:2466-2535` and
`chapters/examples/k3e_bkm_chapter.tex:13012-13041`. It is not the
Gritsenko--Clery dd-modular triple catalogue.

The genuine Gritsenko--Clery dd-catalogue is a separate
`(t,N;k)`-indexed catalogue. The manuscript theorem
`chapters/examples/cy_d_kappa_stratification.tex:2160-2241` lists the
eight triples and explicitly separates them from the CHL and
order-indexed boundary ladders. Local Wave-16/19 notes also use a
cover-sensitive "N=5,7,8" shorthand with constants
`(c_N(0),\kappa_{\mathrm{BKM}})=(1,1/2),(1/2,1/4),(0,0)`; that shorthand
is a consistency target only unless its indexing is restated. It must
not be substituted for the order-indexed host criterion.

## Boundary rows

### N=5

Killed: the automorphic constant in the order-indexed lane is
`c_5(0)=4`, hence `\kappa_{\mathrm{BKM}}=2`. The local derivation uses
frame shape `1^4 5^4`, Lefschetz trace `T_{H^*}(g_5)=8`, correction
`A_5=2`, and Borcherds weight extraction
`c_5(0)=T_{H^*}(g_5)-2A_5=4`
(`chapters/examples/k3e_bkm_chapter.tex:13022-13026`).

Surviving: `X_5^{BV}` is a plausible non-CHL geometry, not a compact
CHL host theorem. Wave-19 Z1 proves the Borcea--Voisin threefold
geometry from Borcea--Voisin data and records the metaplectic root
picture, but its reduced DT equality
`(Z^{X_5^{BV}})^(-1/4)=Delta_{1/2}^{(5)}` and BPS algebra comparison
remain conjectural (`notes/wave19_z1_N5_Borcea_Voisin.tex:207-216`).
Thus host criterion item (i) is only partially supplied, and (iv)--(v)
are open.

Sufficient host data: a resolved Borcea--Voisin CY_3 with reduced
DT orientation, the exact extended paramodular/metaplectic group for
the selected normalisation, the automorphic line of weight 2 in the
order-indexed lane or weight 1/2 in the dd-catalogue lane, a partition
function equality with the corresponding Borcherds product, and a
root-multiplicity theorem using the same `g_5`-twined Jacobi input.

### N=7

Killed: the order-indexed automorphic constant is `c_7(0)=2`, hence
`\kappa_{\mathrm{BKM}}=1`; the local derivation uses frame shape
`1^3 7^3`, `T_{H^*}(g_7)=6`, `A_7=2`
(`chapters/examples/k3e_bkm_chapter.tex:13028-13029`).

Surviving: no smooth diagonal `K3 x E / Z_7` CY_3 host exists. The
order-7 K3 automorphism has three fixed points, and no elliptic curve
has an origin-preserving order-7 automorphism. Wave-19 Z2 proposes a
`mu_4`-gerbe/Cheeger--Simons package over a singular quotient, with
eighth-root DT identity and BPS algebra comparison explicitly
conjectural (`notes/wave19_z2_N7_order4_gerbe.tex:76-104`,
`145-158`, `176-192`). Host criterion items (i)--(v) all remain open
except for the automorphic weight/cover side.

Sufficient host data: a crepant/stacky CY_3 model with a proved
order-4 gerbe and reduced DT orientation, an honest cover carrying the
selected multiplier, an automorphic line of weight 1 in the
order-indexed lane or weight 1/4 in the spin-cover dd lane, a
Cheeger--Simons phase-normalised partition equality, and root
multiplicities computed from the same spin-cover weak Jacobi input.

### N=8

Killed: the order-indexed automorphic constant is `c_8(0)=2`, hence
`\kappa_{\mathrm{BKM}}=1`; the local derivation uses frame shape
`1^2 2 4 8^2`, `T_{H^*}(g_8)=6`, `A_8=2`
(`chapters/examples/k3e_bkm_chapter.tex:13031-13032`).

Surviving: the proposed Mongardi--Tari--Wandel model is not a compact
CY_3 host. Wave-19 Z3 identifies an order-8 symplectic automorphism on
the Kummer-3 hyperkahler fourfold and explicitly states the dimensional
jump: the candidate is a CY_4/fourfold endpoint, not a CY_3 continuation
(`notes/wave19_z3_N8_Kummer3.tex:55-65`, `167-181`, `226-245`). The
dd-catalogue endpoint has weight zero in the cover-sensitive notes, but
that is the abelian/degenerate consistency target, not the
order-indexed CY_3 theorem.

Sufficient host data: an actual compact or stacky CY_3 with reduced DT
orientation, not the MTW CY_4; an honest multiplier cover and weight-1
line for the order-indexed row; a partition function equal to the
order-indexed Borcherds product; and a root-multiplicity theorem from
the same order-8 twined input. None is currently supplied.

## Why `K3 x E` cannot host the rows

The product `K3 x E` supplies only the N=1 denominator theorem. The
origin-preserving automorphism group of a complex elliptic curve has
orders `1,2,3,4,6` only; it has no order `5,7,8` element. A torsion
translation on `E` can make `(S x E)/<g_N,t_N>` smooth and CY, but it
acts trivially on `H^{1,0}(E)` and does not produce the
origin-preserving automorphic multiplier line. Therefore translation
quotients supply at most geometry; they do not supply the denominator
theorem (`working_notes.tex:23523-23539`).

## AutBorch

The honest construction from current data is the denominator functor

```tex
AutBorch^{den}:
\mathsf{BPSSeed}^{mot}_{Aut} -> \mathsf{DenBKM}.
```

Its source may contain

```tex
(M^{mot}_{prim}, \Gamma, \Gamma_{eff}, \alpha, \Lambda,
 Poly, \rho, \epsilon, J, o),
```

where `J` extracts the weak Jacobi input and the remaining data choose
chamber, lattice, multiplier, and orientation. For the K3 x E seed,
local notes give the theorem-grade value

```tex
AutBorch^{den}(\phi_{0,1})
  = (\Delta_5, \nu_{\Delta_5}, 64^{-1}\Delta_5(2Z)).
```

This is the correct Igusa-side consistency target: `Delta_5` is the
character-valued denominator half, while `Delta_5^2` is the scalar
Igusa square. No file in `/Users/raeez/igusa-cusp-form` is touched.

The stronger Hall functor is only conditional:

```tex
AutBorch^{Hall}:
\mathsf{BPSSeed}^{mot,br}_{Aut} -> \mathsf{BKM}^{+}_{Hall}.
```

It requires bracket data

```tex
[-,-]_{Hall}^{prim}, Serre_{real}, Rel_{imag}, o_{HB}^{bracket}=0.
```

A primitive motive plus Jacobi character does not reconstruct the Hall
commutator. This is the obstruction identified in
`notes/bps_positive_geometry_total_resolution_20260424/agent_11_hostile_synthesis.md:688-768`.

## Obstruction coordinates

Killed:

- Automorphic weight extraction in the declared normalisation:
  `\kappa_{\mathrm{BKM}}=c_N(0)/2`.
- The elliptic-origin obstruction: no smooth CHL product quotient for
  N=5,7,8.
- The K3 x E denominator value of `AutBorch^{den}` at `\phi_{0,1}`.

Surviving:

- `o_host` for every N=5,7,8 boundary row.
- For N=5: reduced DT orientation/equality and root-multiplicity match.
- For N=7: stacky/gerbe CY_3 construction, eighth-root normalisation,
  partition equality, and BPS bracket.
- For N=8: compact CY_3 host itself.
- For `AutBorch^{Hall}`: primitive Hall bracket, real-root Serre
  relations, imaginary relations, PBW/radical comparison.

## Proposed final theorem statement

For N in `{5,7,8}`, the order-indexed Nikulin/Gritsenko boundary
ladder has exact Borcherds constants

```tex
(c_N(0),\kappa_{\mathrm{BKM}})=(4,2),(2,1),(2,1).
```

These constants are automorphic data, not compact CHL CY_3 host
theorems. Such a row becomes a compact CY_3 denominator theorem if and
only if a host datum

```tex
(X_N,\widetilde\Gamma_N,\mathcal L_N,Z_N)
```

satisfying the five clauses of `wn:thm:N578-host-criterion` is supplied.
The current data do not supply such a datum for any of N=5,7,8. The
only theorem-grade functor presently available from primitive
automorphic BPS seed data is `AutBorch^{den}`; the Hall-valued version
requires bracket-refined seed data and remains conditional.

## Proof skeleton

1. Read `working_notes.tex:23479-23567`: the programme theorem separates
   N in `{1,2,3,4,6}` from N in `{5,7,8}` and states the host criterion.
2. Read `working_notes.tex:2840-2869`: compact CY_3 apex closure makes
   boundary rows theorem-grade exactly when the host criterion is met.
3. Separate normalisations using
   `chapters/examples/cy_d_kappa_stratification.tex:2160-2241`,
   `2466-2535`, and `chapters/examples/k3e_bkm_chapter.tex:13264-13281`.
4. Audit host notes: N=5 Borcea--Voisin gives geometry but conjectural
   DT/BPS identification; N=7 gives a conjectural gerbe package; N=8
   gives a fourfold endpoint, not CY_3.
5. Split `AutBorch` by source data: denominator functor from Jacobi
   seed/chamber/cover data, Hall functor only after bracket data.

## Primary anchors needed

- Gritsenko--Clery, "The Siegel modular forms of genus 2 with the
  simplest divisor", J. Reine Angew. Math. 678 (2013), 119--137,
  arXiv:1108.0934: dd-catalogue and Borcherds product weights.
- Borcherds, Invent. Math. 132 (1998), Theorems 10.1 and 13.3:
  singular theta lift, cover/multiplier, weight formula.
- Gritsenko--Nikulin, Internat. J. Math. 9 (1998), Part II:
  BKM denominator identities on the CHL/integer-weight slice.
- Nikulin 1980 and Mukai 1988: K3 symplectic automorphism orders and
  fixed-point data.
- Borcea 1997 and Voisin 1993 for the N=5 candidate geometry.
- Cheeger--Simons/Brylinski/Mathai--Murray--Stevenson for the N=7
  gerbe package if it is retained.
- Mongardi--Tari--Wandel 2018 for the N=8 fourfold endpoint.

The local notes sometimes cite "GC 2008 arXiv:0812.3962"; the live
bibliography has the Gritsenko--Clery simplest-divisor paper as
arXiv:1108.0934 / JRAM 2013. Before manuscript inscription, reconcile
that bibliographic anchor.

## Computations and tests run

No build or mathematical test suite was run. Verification was by local
source audit only:

- `rg` over `working_notes.tex`, `notes/`, `chapters/`, `compute/`,
  `bibliography/`, and `metadata/` for `Gritsenko-Clery`, `N=5`,
  `N=7`, `N=8`, `boundary rows`, `host criterion`, and `AutBorch`.
- Direct reads of the requested local notes:
  `notes/wave15_m2_EZ_basis_N1_to_8.tex`,
  `notes/wave16_v1_N578_non_CHL.tex`,
  `notes/wave16_v4_8_form_kappaBKM_audit.tex`,
  `notes/wave19_z1_N5_Borcea_Voisin.tex`,
  `notes/wave19_z2_N7_order4_gerbe.tex`,
  `notes/wave19_z3_N8_Kummer3.tex`.
- Additional reads for normalization and AutBorch separation:
  `notes/wave19_z4_N578_joint_automorphic.tex`,
  `notes/wave19_s1_8_form_synthesis.tex`, and
  `notes/bps_positive_geometry_total_resolution_20260424/agent_11_hostile_synthesis.md`.

The requested label `wn:thm:programme-constants-boundary-rows` was not
present in `working_notes.tex` at audit time; the corresponding theorem
title is "Programme constants and boundary automorphic rows" with label
`wn:thm:eight-dd-forms-full` at `working_notes.tex:23479-23481`.

## Files changed

- `notes/frontier_resolution_swarm_20260424_n578_hosts_autborch.md`
