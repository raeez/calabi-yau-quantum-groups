# Agent 04 Report: CY Dimension and Kappa Stratification

Date: 2026-04-24.
Scope: `chapters/examples/cy_d_kappa_stratification.tex`,
`chapters/theory/en_factorization.tex`,
`chapters/theory/e1_chiral_algebras.tex`,
`chapters/theory/e2_chiral_algebras.tex`,
`compute/lib/cy_euler.py`, `compute/lib/kappa_ch_d3_formula.py`,
`compute/lib/local_p2_four_kappa_engine.py`,
`compute/lib/kappa_bkm_adversarial.py`, and
`~/chiral-bar-cobar/chapters/examples/landscape_census.tex`.

## Executive Verdict

The dimension/kappa architecture is recoverable, but three notational
interfaces remain dangerous:

1. `\kappa_{\mathrm{ch}}` is used for both the raw `\Phi^{FA}_d`
   Hodge-supertrace scalar and specialisation-side Heisenberg/BCOV
   scalars.
2. `\kappa_{\mathrm{fiber}}` is split between the K3 fibre categorical
   Euler value `2` and the Mukai-lattice rank `24`.
3. The CHL five-formula scope and the full Gritsenko--Clery eight-form
   scope are both present, but one catalogue table collapses their
   weights and covers.

No manuscript or compute source was changed. Files changed: this report only.

## ATTACK_1: K3 x E Kunneth Conflation

Claim attacked: the K3 x E spectrum may be written
`\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}},\kappa_{\mathrm{BKM}},
\kappa_{\mathrm{fibre}}\}(K3\times E)=\{0,3,5,24\}`.

Failure mode: `cy_d_kappa_stratification.tex:1400-1408` writes the
unsuperscripted `\kappa_{\mathrm{ch}}` entry as `3`. This contradicts
the same chapter's raw `\PhiFA_d` table:
`cy_d_kappa_stratification.tex:356-364` gives
`\kappa_{\mathrm{ch}}(K3\times E)=0`, and
`cy_d_kappa_stratification.tex:1036-1040` computes
`h^{0,\bullet}(K3\times E)=(1,1,1,1)` and
`\Xi=1-1+1-1=0`.

HEAL_1:

Use two explicitly different symbols:

```tex
\kappa_{\mathrm{cat}}(K3\times E)
  = \chi(\mathcal O_{K3})\chi(\mathcal O_E)=2\cdot 0=0,
```

```tex
\kappa_{\mathrm{ch}}^{\PhiFA}(K3\times E)
  = \Xi(K3\times E)=\Xi(K3)\Xi(E)=2\cdot 0=0,
```

```tex
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3
```

for the Mukai-Heisenberg specialisation. The correct specialisation-side
four-value slogan is therefore

```tex
\{\kappa_{\mathrm{cat}},
  \kappa_{\mathrm{ch}}^{\mathrm{Heis}},
  \kappa_{\mathrm{BKM}},
  \kappa_{\mathrm{fiber}}\}(K3\times E)=\{0,3,5,24\}.
```

Verification paths:

- Manuscript definition:
  `cy_d_kappa_stratification.tex:34-64` separates
  `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`,
  `\kappa_{\mathrm{BKM}}`, and `\kappa_{\mathrm{fiber}}`.
- Manuscript Kunneth computation:
  `cy_d_kappa_stratification.tex:391-406` states
  `\Xi(X\times Y)=\Xi(X)\Xi(Y)`.
- Compute witness:
  `cy_euler.verify_all()` returned
  `chi_K3xE_eq_0=True`, `h11_K3xE_eq_21=True`,
  `h21_K3xE_eq_21=True`, and `kappa_K3xE_eq_5=True`.

Status recommendation: local notation repair. Keep the mathematics, but
change the line `\{\kcat,\kch,\kBKM,\kappa_{\mathrm{fibre}}\}` at
`cy_d_kappa_stratification.tex:1402` to use
`\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`.

## ATTACK_2: Product-Additive `\kappa_{\mathrm{ch}}` as a Universal d=3 Formula

Claim attacked: `\kappa_{\mathrm{ch}}` at d=3 is universally computed by
a product-additive or BCOV rule.

Failure mode: `compute/lib/kappa_ch_d3_formula.py:49-67` assigns
`\kappa_{\mathrm{ch}}(K3\times E)=3`,
`\kappa_{\mathrm{ch}}(Q_5)=-25/3`,
`\kappa_{\mathrm{ch}}(\mathbb C^3)=1`, and
`\kappa_{\mathrm{ch}}(\mathrm{conifold})=1` under one name. The current
chapter uses a narrower raw convention:
`cy_d_kappa_stratification.tex:411-425` states

```tex
\kappa_{\mathrm{ch}}(\mathcal A_X)=
\Xi(X)=\sum_{q=0}^d(-1)^q h^{0,q}(X)
```

for compact CY targets at generic parameters, so the compact odd-d
raw value vanishes by Serre cancellation
(`cy_d_kappa_stratification.tex:113-129`).

HEAL_2:

The compute file is useful only after superscript normalisation:

```tex
\kappa_{\mathrm{ch}}^{\PhiFA}(X)=\Xi(X)
```

for the raw compact `\PhiFA_d` output;

```tex
\kappa_{\mathrm{ch}}^{\mathrm{BCOV}}(X)=\chi_{\mathrm{top}}(X)/24
```

for the one-loop BCOV constant-map scalar, e.g.
`\kappa_{\mathrm{ch}}^{\mathrm{BCOV}}(Q_5)=-200/24=-25/3`;

```tex
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3
```

for the Mukai-Heisenberg specialisation; and

```tex
\kappa_{\mathrm{ch}}^{\mathrm{McKay}}(\mathrm{loc}\,\mathbb P^2)=3/2,
\qquad
\kappa_{\mathrm{ch}}^{\mathrm{McKay}}(\mathrm{conifold})=1
```

for non-compact toric chain-level readings.

Verification paths:

- Raw compact table:
  `cy_d_kappa_stratification.tex:356-369`.
- Quintic disambiguation:
  `cy_d_kappa_stratification.tex:875-892`.
- Vol I BCOV row:
  `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5519-5533`.
- Direct compute run:
  `kappa_ch_d3_formula.verify_all()` returned
  `K3xE: kappa_ch_actual=3, chi_O_actual=0, clash=True`, confirming
  that this engine is not using the raw `\PhiFA_d` convention.

Status recommendation: do not use `compute/lib/kappa_ch_d3_formula.py`
as a source for the unsuperscripted chapter table until its API names
are split into `PhiFA`, `BCOV`, `Heis`, and `McKay` lanes.

## ATTACK_3: d >= 3 E2 Leakage

Claim attacked: the d=3 output algebra itself is natively `E_2`.

Failure mode: no fatal leakage survives in the inspected anchors, but
the failure mode is close enough to require a guard: any sentence
upgrading the d=3 algebra `A` from `E_1` to native `E_2` would contradict
the local doctrine.

HEAL_3:

The correct d-stratified operadic statement is:

```tex
d=2:\quad \Phi_{E_2}(\mathcal C)
  =\mathrm{SpCh}_{\Sigma_1,C}(\PhiFA_2(\mathcal C))
  \quad\text{is native }E_2.
```

```tex
d\ge 3:\quad A=\Phi_{E_1}(\mathcal C)\text{ is native }E_1,
\qquad
\mathcal Z(\mathrm{Rep}^{E_1}(A))
\simeq \mathrm{Rep}^{E_2}(\mathrm{Drin}(A))
```

is the derived-centre/braided enhancement. For CY3,
`\Phi_{E_2}=Z^{\mathrm{ch}}\circ\Phi_{E_1}` remains conjectural as a
chiral Drinfeld-centre identification, not a direct output theorem.

Verification paths:

- E1 primacy:
  `e1_chiral_algebras.tex:13-29`.
- d=3 native/centre split:
  `e1_chiral_algebras.tex:35-38`.
- Drinfeld-centre pathway:
  `e1_chiral_algebras.tex:234-244`.
- Obstruction to skipping E1:
  `e1_chiral_algebras.tex:414-416`.
- CY2 direct E2 and CY3 conjectural centre:
  `e2_chiral_algebras.tex:151-164` and
  `e2_chiral_algebras.tex:188-210`.
- Factorisation hierarchy:
  `en_factorization.tex:581-588` and
  `en_factorization.tex:2809-2812`.

Status recommendation: keep current `E_1`/derived-`E_2` wording. Any
future d=3 theorem statement should explicitly say "native `E_1`;
`E_2` on the Drinfeld centre of the representation category."

## ATTACK_4: Additive BKM Decomposition

Claim attacked:

```tex
\kappa_{\mathrm{BKM}}
  =\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})
```

as a universal identity.

Failure mode: the identity fails under the raw total-space convention
already at `N=1`:

```tex
5\ne
\kappa_{\mathrm{ch}}^{\PhiFA}(K3\times E)+\chi(\mathcal O_E)
=0+0.
```

Under the specialisation convention it is still only the numerical
coincidence `5=3+2` at `N=1`, and it fails on orbifold frames. The
compute engine confirms a success rate of `1/8` for the specialisation
decomposition:

```text
N=1: BKM=5, predicted=5, holds=True
N=2: BKM=4, predicted=3, holds=False
N=3: BKM=3, predicted=5, holds=False
N=4: BKM=2, predicted=5, holds=False
N=5: BKM=2, predicted=5, holds=False
N=6: BKM=1, predicted=5, holds=False
N=7: BKM=1, predicted=5, holds=False
N=8: BKM=1, predicted=5, holds=False
```

HEAL_4:

The only universal BKM-lane formula is:

```tex
\kappa_{\mathrm{BKM}}(\Phi_N)=\mathrm{wt}(\Phi_N)=c_N(0)/2.
```

For the five CHL denominator frame shapes
`N in {1,2,3,4,6}`:

```tex
(c_N(0))=(10,8,6,4,2),
\qquad
(\kappa_{\mathrm{BKM}}(\Phi_N))=(5,4,3,2,1).
```

Verification paths:

- Theorem statement:
  `cy_d_kappa_stratification.tex:2013-2052`.
- Borcherds product proof:
  `cy_d_kappa_stratification.tex:2054-2105`.
- Additive refutation:
  `cy_d_kappa_stratification.tex:2269-2281`.
- Three-source verification:
  `cy_d_kappa_stratification.tex:2466-2506`.
- Compute witness:
  `kappa_bkm_adversarial.c0_is_universal()` returned `True`; the same
  run returned decomposition success rate `1/8`.

Status recommendation: mark all additive decompositions as false or
as the single `N=1` specialisation-side coincidence. Never route
`\kappa_{\mathrm{BKM}}` through a Hodge supertrace or fibre Euler
formula.

## ATTACK_5: Full Eight-Form Scope and Cross-Volume Spectrum Drift

Claim attacked: the eight-form catalogue can be read from the same CHL
weight table and with the same integral cover data.

Failure mode A: `cy_d_kappa_stratification.tex:155-169` correctly
separates the CHL averaged family from the full Gritsenko--Clery
eight-form family, giving full values

```tex
(5,2,1,1,1/2,1,1/4,0).
```

But `cy_d_kappa_stratification.tex:2130-2147` lists the later catalogue
with integral-looking entries for `N=5,7,8` and `\SpFour` covers. This
collides with the local doctrine in `CLAUDE.md:255-260`, which requires
half-integral and quarter-integral cover stratification:
`\Sp_4(\mathbb Z)` for integral weights, `\Mp_4` for half-integral
weights, and `\widetilde{\Mp}_4` for quarter-integral weights, with
weight `0` terminal at `N=8`.

Failure mode B: Vol I's K3 x E row
`~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5254-5258`
writes

```tex
\kappa_{\mathrm{fiber}}(K3)=2,
```

while Vol III's canonical fibre invariant is the Mukai-lattice rank
`24` (`cy_d_kappa_stratification.tex:146`). The value `2` is
`\kappa_{\mathrm{cat}}(K3)=\chi(\mathcal O_{K3})`, not
`\kappa_{\mathrm{fiber}}` in the Vol III sense.

HEAL_5:

Use two explicitly scoped catalogues:

```tex
\text{CHL denominator scope }N\in\{1,2,3,4,6\}:
\quad \kappa_{\mathrm{BKM}}=(5,4,3,2,1).
```

```tex
\text{Full Gritsenko--Clery singular-theta scope }N=1,\ldots,8:
\quad \kappa_{\mathrm{BKM}}=(5,2,1,1,1/2,1,1/4,0),
```

with the cover group chosen by the weight denominator. For the K3 x E
cross-volume row, replace `\kappa_{\mathrm{fiber}}(K3)=2` by one of two
honest readings:

```tex
\kappa_{\mathrm{cat}}(K3)=2
```

if the row means the K3 fibre arithmetic genus, or

```tex
\kappa_{\mathrm{fiber}}(K3)=24
```

if the row means the Vol III Mukai-lattice fibre invariant.

Verification paths:

- Full eight-form values:
  `cy_d_kappa_stratification.tex:155-169`.
- CHL theorem:
  `cy_d_kappa_stratification.tex:2013-2029`.
- Local doctrine:
  `CLAUDE.md:255-260`.
- Cross-volume row:
  `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5248-5266`.
- Vol I Borcherds/Heegner check:
  `~/chiral-bar-cobar/chapters/examples/landscape_census.tex:5417-5450`.

Status recommendation: the CHL five-family theorem remains proved in
its denominator scope. The full eight-form catalogue requires the
cover-stratified values and host-status caveats before it can carry
`\ClaimStatusProvedHere` at the table level.

## Verification Run

Commands run:

```bash
PYTHONPATH=compute/lib python3 - <<'PY'
import cy_euler
import local_p2_four_kappa_engine as lp2
import kappa_bkm_adversarial as bkm
import kappa_ch_d3_formula as d3

# Printed selected values from:
# cy_euler.verify_all()
# cy_euler.decompose_weight_5()
# lp2.full_report()
# bkm.test_decomposition_all_N()
# bkm.c0_is_universal()
# d3.verify_all()
PY
```

Key outputs:

- `cy_euler.verify_all()` subset:
  `chi_K3xE_eq_0=True`,
  `h11_K3xE_eq_21=True`,
  `h21_K3xE_eq_21=True`,
  `kappa_K3xE_eq_5=True`,
  `igusa_weight_eq_5=True`,
  `borcherds_weight_eq_5=True`,
  `dt_weight_all_10=True`.
- `cy_euler.decompose_weight_5()` subset:
  `chi_K3=24`, `chi_E=0`, `chi_K3xE=0`,
  `kappa_label=kappa_BKM`, `kappa_BKM_K3xE=5`,
  `c_1_0=10`, source `Borcherds weight: c_1(0)/2`.
- `local_p2_four_kappa_engine.full_report()`:
  `all_verified=True`,
  spectrum `(3/2, 1, None, 1)`;
  four `\kappa_{\mathrm{ch}}` paths agree, three
  `\kappa_{\mathrm{cat}}` paths agree, three
  `\kappa_{\mathrm{fiber}}` paths agree, and
  `\kappa_{\mathrm{BKM}}` is undefined for toric local `\mathbb P^2`.
- `kappa_bkm_adversarial`:
  decomposition success rate `1/8`; `c0_is_universal=True`.
- `kappa_ch_d3_formula.verify_all()`:
  all internal numerical checks passed, but the output confirms this
  engine uses the product-additive/BCOV convention, not the raw
  `\PhiFA_d` Hodge-supertrace convention.

Focused pytest:

```bash
pytest -q compute/tests/test_cy_d_kappa_stratification.py \
  compute/tests/test_kappa_ch_d3_formula.py \
  compute/tests/test_local_p2_four_kappa_engine.py \
  compute/tests/test_kappa_bkm_adversarial.py \
  compute/tests/test_cy_euler.py
```

Result: `295 passed, 4 failed`. The four failures are all
`compute/tests/test_cy_euler.py::TestDecomposeWeight5` key-name drift:
the tests expect `formula_h11_over_4_matches`,
`formula_chi_minus_4_over_4_matches`, `c_f_0`, and
`two_kappa_equals_weight_inverse_Z`, while
`compute/lib/cy_euler.py:823-850` now returns
`h11_over_4_matches_kappa_BKM`,
`chi_minus_4_over_4_matches_kappa_BKM`, `c_1_0`, and
`two_kappa_BKM_equals_weight_inverse_Z`.

## Remaining Open Obligations

1. Normalize `compute/lib/kappa_ch_d3_formula.py` so its public API names
   carry the same superscripts as the manuscript lanes.
2. Repair `cy_d_kappa_stratification.tex:1402` by replacing raw
   `\kch` with `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`.
3. Repair the eight-form catalogue table at
   `cy_d_kappa_stratification.tex:2130-2147` to match the
   cover-stratified values.
4. Reconcile the Vol I K3 x E row so `2` is not called
   `\kappa_{\mathrm{fiber}}` when Vol III uses `24`.
5. Update the four stale `cy_euler` test keys or add compatibility
   aliases, then rerun the focused pytest slice.
