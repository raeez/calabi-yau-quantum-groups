# Agent 03 -- Etingof/Deformation Quantization

Date: 2026-04-24.

Scope: hostile audit of `compute/lib/chiral_ce_e3_deformation.py` against the
local manuscript claims on `sigma_2`, `sigma_3`, Omega-background parameters,
one- versus two-parameter deformation, the CY condition `h_1+h_2+h_3=0`,
rational/Gevrey assertions, and compatibility with affine Yangian / quantum
toroidal statements.  No chapter or compute file was edited.  This report is
the only file written.

## Verdict

CONVERGED with six repairs recommended.

The local arithmetic of the Omega-background is correct:

```tex
h_3 = -h_1-h_2,\qquad
\sigma_2 = h_1h_2+h_1h_3+h_2h_3,\qquad
\sigma_3=h_1h_2h_3.
```

At the standard point `(h_1,h_2,h_3)=(1,-2,1)`,

```tex
\sigma_2=-3,\qquad \sigma_3=-2,\qquad k=-\sigma_2=3,
\qquad
g(5)=28/27.
```

The exact affine-Yangian structure function is

```tex
g(u)=\prod_{i=1}^3 {u-h_i \over u+h_i}
     ={u^3+\sigma_2 u-\sigma_3\over u^3+\sigma_2 u+\sigma_3}.
```

For `h_1+h_2+h_3=0`,

```tex
g(u)=1-{2\sigma_3\over u^3}
       +{2\sigma_2\sigma_3\over u^5}
       +{2\sigma_3^2\over u^6}
       +O(u^{-7}).
```

Thus `sigma_2` is the `E_1`/defect level datum `k=-sigma_2`; `sigma_3`
is the first scalar structure-function correction.  They must not be
collapsed.

## Verification Run

```bash
python3 -m pytest compute/tests/test_chiral_ce_e3_deformation.py -q
```

Result: `81 passed in 4.59s`.

```bash
python3 -m pytest compute/tests/test_e3_koszul_heisenberg.py \
  compute/tests/test_e3_koszul_yangian.py -q
```

Result: `75 passed in 0.25s`.

```bash
python3 -m pytest compute/tests/test_chiral_rmatrix_e3_braiding.py \
  compute/tests/test_cfg25_e1_chiral_lift.py -q
```

Result: `178 passed in 0.32s`.

```bash
python3 -m pytest compute/tests/test_quantum_toroidal_e1_cy3.py \
  compute/tests/test_affine_yangian_e1_cy3.py -q
```

Result: `383 passed in 15.19s`.

Total targeted surface: `717` passing tests.  The green surface verifies
the current local conventions; it does not remove the convention collisions
below.

## Local Anchors

- `compute/lib/chiral_ce_e3_deformation.py:185`: Omega parameters.
- `compute/lib/chiral_ce_e3_deformation.py:230`: rational structure function.
- `compute/lib/chiral_ce_e3_deformation.py:250`: claimed deformed CE differential.
- `compute/lib/chiral_ce_e3_deformation.py:336`: `sigma_3`-weighted full differential.
- `compute/lib/chiral_ce_e3_deformation.py:451`: two free parameters but one essential parameter language.
- `compute/lib/chiral_ce_e3_deformation.py:581`: Koszul conductor implementation.
- `compute/lib/chiral_ce_e3_deformation.py:1002`: Heisenberg `kappa_ch=k/2`.
- `compute/lib/chiral_ce_e3_deformation.py:1052`: Yangian `kappa_ch=1`.
- `compute/lib/holomorphic_cs_chiral_engine.py:805`: Heisenberg `kappa_ch=-sigma_2`.
- `compute/lib/holomorphic_cs_chiral_engine.py:1296`: Yangian `kappa_ch=-sigma_2`.
- `chapters/theory/cy_to_chiral.tex:3598`: affine Yangian structure function.
- `chapters/theory/en_factorization.tex:923`: Heisenberg level `k=-sigma_2`.
- `chapters/theory/en_factorization.tex:994`: Yangian conductor relation.
- `chapters/theory/quantum_chiral_algebras.tex:1461`: `kappa_ch(A)=-sigma_2`, `kappa_ch(A^!)=sigma_2`.
- `chapters/theory/quantum_chiral_algebras.tex:2186`: parameter inversion proposition.

## ATTACK -> HEAL Cycles

### Cycle 1 -- `sigma_2`/`sigma_3` role collapse

ATTACK.  Treat `sigma_3` as the only deformation parameter and demote
`sigma_2` to a harmless rescaling everywhere.

FAILURE MODE.  The structure function uses both invariants:

```tex
g(u)={u^3+\sigma_2u-\sigma_3\over u^3+\sigma_2u+\sigma_3}.
```

The large-`u` scalar expansion starts with `-2 sigma_3/u^3`, but the
restricted curve/defect level is `k=-sigma_2`.  The direct computation
at `(1,-2,1)` gives `sigma_2=-3`, `sigma_3=-2`, `k=3`, `g(5)=28/27`.

HEAL.  Use the two-slot formula:

```tex
\text{level / }E_1\text{ defect datum}: k=-\sigma_2,
\qquad
\text{first scalar Yangian correction}: \phi_3=-2\sigma_3.
```

Status recommendation: `sigma_2` is proved arithmetic and level data;
`sigma_3` is proved arithmetic and the first scalar structure-function
correction.  A sentence saying "the deformation is controlled only by
`sigma_3`" is correct only after explicitly quotienting by level
rescaling and fixing the `E_1` normalization.

### Cycle 2 -- CY condition as a proof that `d_h^2=0`

ATTACK.  Read `d_h=d_CE+h_1 partial_1+h_2 partial_2+h_3 partial_3` and
`h_1+h_2+h_3=0` as a proof that `d_h^2=0`.

FAILURE MODE.  The CY condition is necessary for the equivariant volume
constraint, but it does not by itself prove nilpotence on the CE complex.
Nilpotence also requires the three operators to be compatible
differentials or an equivariant Cartan differential whose square vanishes
on the invariant/CY subcomplex.  The implementation does not construct
the three operators.  On arity one and two it delegates to `d_CE`; in
`d_h_full` it adds only formal `sigma_3`-weighted `L_infinity`
corrections.

HEAL.  Replace the proof claim by the conditional statement:

```tex
d_{\boldsymbol h}=d_{\mathrm{CE}}+\sum_i h_i\partial_i
```

is a differential on the equivariant CY subcomplex when the `partial_i`
are the commuting equivariant operators supplied by the holomorphic
factorization model and are compatible with `d_CE`.  The arithmetic
condition `sum h_i=0` is the CY input; it is not the whole proof of
`d_{\boldsymbol h}^2=0`.

Status recommendation: keep `d_h^2=0` as computed/model-conditional in
`chiral_ce_e3_deformation.py`, not as an independent theorem.

### Cycle 3 -- One-parameter versus two-parameter deformation

ATTACK.  Use `QuantumCEDeformation.essential_param == sigma_3` to
identify the `E_3`/DIM deformation with a one-parameter family.

FAILURE MODE.  The additive Omega background on `C^3` has two free
parameters after `h_1+h_2+h_3=0`.  Equivalently, the unordered quotient
is parametrized by `(sigma_2,sigma_3)`.  The multiplicative DIM algebra
has two parameters `(q,t)` with

```tex
q=e^{h_1},\qquad t=e^{-h_2},\qquad q_3=(qt^{-1})^{-1}.
```

The manuscript already marks quantum toroidal `gl_1` as a two-parameter
algebra.  The affine Yangian/rational normalized slice can be described
by `sigma_3` only after the level/scale datum is fixed.

HEAL.  Separate the three layers:

```tex
\text{Omega base}: (h_1,h_2,h_3),\quad \sum h_i=0,\quad \dim=2.
```

```tex
\text{symmetric invariants}: (\sigma_2,\sigma_3).
```

```tex
\text{normalized affine-Yangian scalar correction}: \sigma_3
\text{ after fixing } k=-\sigma_2.
```

Status recommendation: manuscript statements about quantum toroidal
algebras must say "two-parameter"; statements about the normalized
affine Yangian may say "one effective parameter" only with the
normalization clause.

### Cycle 4 -- Rational and Gevrey claims as proved by the CE engine

ATTACK.  Treat the strings

```text
G -> polynomial, L -> rational, M -> Gevrey-1 divergent
```

in `deformation_type()` and `deformation_series_radius()` as analytic
proofs.

FAILURE MODE.  The implementation is a lookup table keyed by
`shadow_class`.  It does not estimate coefficients, prove a radius of
convergence, or produce a Borel transform.  The rational part is proved
only for the explicit affine-Yangian structure function `g(u)` above.
The Gevrey-1 assertion for class M belongs to the external topological
string / shadow-tower asymptotic evidence, not to this CE engine.

HEAL.  Use this status split:

```tex
\text{Class L rationality}: proved for the explicit }g(u)
\text{ and for rational shuffle kernels in the cited Yangian model.}
```

```tex
\text{Class M Gevrey-1}: expected/computed from the infinite shadow tower
\text{ or BCOV/topological-string asymptotics; not proved by this module.}
```

Status recommendation: keep rational/Gevrey claims as classification
metadata in the compute file unless an independent analytic coefficient
estimate is cited.

### Cycle 5 -- Koszul parameter inversion versus dual level

ATTACK.  Since `sigma_2(-h)=sigma_2(h)`, conclude that the Koszul dual
level is preserved and that the class L conductor is `2k=-2sigma_2`.

FAILURE MODE.  This is the central collision.  Parameter inversion alone
preserves `sigma_2` and flips `sigma_3`:

```tex
\sigma_2(-h)=\sigma_2(h),\qquad \sigma_3(-h)=-\sigma_3(h).
```

But the Koszul dual modular characteristic uses the Verdier/Shapovalov
sign on the restricted `E_1` level:

```tex
\kappa_{\mathrm{ch}}(A)=-\sigma_2,\qquad
\kappa_{\mathrm{ch}}(A^!)=\sigma_2,\qquad
\rho_K=0
```

for the free-field / `gl_1` / class L branch.  The dedicated engines
`E3BarComplexHeisenberg` and `E3BarComplexYangian` implement this and
the tests enforce it.  `chiral_ce_e3_deformation.py` instead returns
`conductor = -2*sigma_2` for class L away from `sigma_3=0`.

Direct default comparison:

```text
chiral_ce Yangian: kappa_ch=1, conductor=6, level_preserved=True
holomorphic_cs Yangian: kappa_ch=3, kappa_dual=-3, conductor=0
```

HEAL.  Distinguish two operations:

```tex
\text{Omega parity check}: h\mapsto -h,\quad \sigma_2\text{ even},\quad \sigma_3\text{ odd}.
```

```tex
\text{Koszul-dual characteristic}: \kappa_{\mathrm{ch}}^!=-\kappa_{\mathrm{ch}}
\text{ for the free-field/class L branch, hence }\rho_K=0.
```

Status recommendation: `E3KoszulDual.parameter_inversion_check()` is
valid as an Omega parity check.  Its class L `conductor` formula in
`chiral_ce_e3_deformation.py` is incompatible with the manuscript and
with `holomorphic_cs_chiral_engine.py`; the healed value for the
`gl_1`/class L branch is `rho_K=0`.

### Cycle 6 -- Compatibility with affine Yangian and quantum toroidal

ATTACK.  Identify the CE deformation, affine Yangian, and quantum
toroidal algebra as the same object at the same parameter level.

FAILURE MODE.  The local files enforce a hierarchy:

```tex
\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
```

is the cohomological/positive-half affine Yangian statement.  The
Drinfeld double gives the full affine Yangian.  The multiplicative
quantum toroidal `U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)` is the
two-parameter trigonometric/DIM lift.  The `E_3` master structure and
its Koszul duality remain conditional in the 6d holomorphic framework.

HEAL.  Use the following compatibility ladder:

```tex
\text{cohomological/rational: }Y^+(\widehat{\mathfrak{gl}}_1),
\quad
D(Y^+)=Y(\widehat{\mathfrak{gl}}_1),
```

```tex
\text{multiplicative/toroidal: }
U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1),
\quad q=e^{h_1},\ t=e^{-h_2},\ q_1q_2q_3=1,
```

```tex
\text{6d }E_3\text{ origin: conditional on the holomorphic factorization
comparison and CY-A}_3.
```

Status recommendation: the CE engine may serve as a toy/checking model
for parameter arithmetic and finite CE examples.  It should not be
cited as constructing the full quantum toroidal or proving the full
`E_3` Koszul duality.

## Additional Compute-Side Hazards

1. `compute/tests/test_chiral_ce_e3_deformation.py:85` says in its
   docstring that `sigma_2=-5` at `(1,-2,1)`, but the comment and
   assertion correctly give `-3`.  The assertion is right; the docstring
   is stale.

2. `compute/lib/chiral_ce_e3_deformation.py:1002` sets Heisenberg
   `kappa_ch=k/2`, while the manuscript and
   `holomorphic_cs_chiral_engine.py` use `kappa_ch(H_k)=k=-sigma_2`.
   At `(1,-2,1)`, the CE wrapper reports `1/2` by default, while the
   holomorphic engine reports `3`.

3. `compute/lib/chiral_ce_e3_deformation.py:1052` sets Yangian
   `kappa_ch=1`, independent of Omega parameters.  The manuscript and
   holomorphic engine use `kappa_ch=-sigma_2`; at `(1,-2,1)` this is `3`.

4. `compute/lib/chiral_rmatrix_e3_braiding.py` contains a local prose
   formula saying the CY-normalized structure function has leading
   `-2 sigma_2/z^2`.  The symbolic expansion shows the scalar
   structure-function leading term is `-2 sigma_3/z^3`.  The `-sigma_2`
   datum belongs to the classical `r`-matrix/level normalization, not to
   the scalar large-`u` coefficient of `g`.

## Final Status Recommendations

- `OmegaParams` arithmetic in `chiral_ce_e3_deformation.py`: computed,
  correct.
- `g(u)` formula and CY unitarity `g(u)g(-u)=1`: proved algebraically;
  the unitarity identity does not require `sum h_i=0`.
- CY condition `sum h_i=0`: proved arithmetic; it removes the
  `u^{-1}` term and in fact the scalar expansion begins at `u^{-3}`.
- `d_h^2=0` in the CE engine: computed/model-conditional, not a proof of
  the holomorphic `E_3` differential.
- One-parameter language: valid only after fixing/quotienting the
  `sigma_2` level; invalid for quantum toroidal/DIM.
- Rational class L: proved for the explicit rational structure
  function; broader rational convergence is classification metadata.
- Gevrey-1 class M: expected/computed from external shadow/BCOV evidence;
  not proved by this CE engine.
- Koszul conductor for `gl_1` class G/L: healed value `rho_K=0` with
  `kappa_ch^!=-\kappa_ch`; the class L conductor in
  `chiral_ce_e3_deformation.py` is not compatible with the manuscript.
