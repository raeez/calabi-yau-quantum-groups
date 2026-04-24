# Agent 13 - Compute Oracles for Chambered Effective BPS Positive Geometry

Date: 2026-04-24.

Owned file: `notes/adversarial_bps_positive_geometry_20260424/agent_13_compute_oracles.md`.
No manuscript files edited.

## Sources read

- Doctrine: `CLAUDE.md`, `AGENTS.md`.
- Manuscript target: `chapters/theory/quantum_groups_foundations.tex`, especially `def:universal-positive-geometry-grammar`, `thm:quantum-group-as-positive-geometry-double`, `prop:toric-effective-geometry-terminal-degeneration`, `conj:effective-bps-cone-positive-basis`.
- Cross anchors: `chapters/theory/cy_to_chiral.tex`, `chapters/examples/toric_cy3_coha.tex`.
- Compute/test surface: `compute/lib/{toric_cy3_dt_engine.py,conifold_wall_crossing.py,local_p2_shadow.py,local_p2_four_kappa_engine.py,coha_chart_explicit.py,scattering_diagram.py,kappa_ch_d3_formula.py,cy_d_kappa_d3.py}` and the corresponding test files.

## Tests and computations run

Command:

```bash
python3 -m pytest compute/tests/test_conifold_wall_crossing.py compute/tests/test_conifold_wc.py compute/tests/test_toric_cy3_dt_engine.py compute/tests/test_local_p2_shadow.py compute/tests/test_local_p2_four_kappa_engine.py compute/tests/test_coha_chart_explicit.py compute/tests/test_scattering.py compute/tests/test_scattering_diagram.py compute/tests/test_kappa_ch_d3_formula.py compute/tests/test_cy_d_kappa_d3.py -q
```

Result: `671 passed in 1.70s`.

Representative values extracted:

- Conifold quantum-torus pentagon: `pentagon_identity_quantum_torus(N_q=12,max_charge=6)["pentagon_holds"] = True`.
- Conifold numerical Schrodinger check: `pentagon_numerical(0.3,50)["match"] = True`, relative error `1.16e-16`; similarly `q=0.5`, relative error `2.56e-16`, and `q=0.1`, relative error `3.25e-16`.
- Conifold chamber I support: `{(1,0):-1,(0,1):-1}`.
- Conifold chamber II support through `n=4`: `{(0,1):-1,(1,0):-1,(1,1):-1,(1,2):-1,(1,3):-1,(1,4):-1}`.
- Local `\mathbb P^2`: `\kappa_{\mathrm{ch}}=3/2`, `\kappa_{\mathrm{cat}}=1`, `\kappa_{\mathrm{BKM}}` undefined, `\kappa_{\mathrm{fiber}}=1`; all local four-kappa checks passed.
- Local `\mathbb P^2` GV data used by the engine: `n^0_1=3`, `n^0_2=-6`, `n^0_3=27`, `n^0_4=-192`, `n^0_5=1695`; `n^1_3=-10`, `n^1_4=231`, `n^1_5=-4452`.
- PBW character oracle: `PExp(PLog(character)) = character` for `\mathbb C^3`, conifold diagonal, local `\mathbb P^2`.
- Canonical chart `\kappa_{\mathrm{ch}}`: `\mathbb C^3=1`, conifold `=1`, local `\mathbb P^2=3/2`.
- Scattering RED oracle: symmetric pair-commutator scattering has wall `(1,1,1)` with multiplicity `8/3`, but `ratio_analysis(4,1,"symmetric")["uniform"] = False`.

## Cycle 1 - Toric Effective Monoid and Terminal Degeneration

Status: computed for standard quiver charts; conditional for arbitrary toric CY3.

Attacked claim: `\Gamma_{\mathrm{eff},\sigma}(X_\Sigma)=\mathbb Z_{\ge 0}^{Q_0}` and `Y^+_\sigma(X_\Sigma)=\mathrm{CoHA}(Q,W)` for toric CY3 positive geometry.

Failure mode: the current engines compute the standard chart monoids and characters for `\mathbb C^3`, conifold, and local `\mathbb P^2`; they do not parse an arbitrary toric fan, build its dimer/quiver-with-potential, prove nonzero BPS support for every chamber generator, or verify determinant-line orientations. Thus the manuscript proposition is executable only on the standard toric Hall loci named by the compute surface.

Healed theorem/formula/test oracle: state the computed toric degeneration as:

```tex
\Gamma_{\mathrm{eff}}(\mathbb C^3)=\mathbb Z_{\ge0},\quad
\Gamma_{\mathrm{eff}}(\mathrm{conifold})=\mathbb Z_{\ge0}^2,\quad
\Gamma_{\mathrm{eff}}(K_{\mathbb P^2})=\mathbb Z_{\ge0}^3
```

at the quiver-chart level, because the computed BPS support contains the vertex basis charges:
`(1)`, `(1,0),(0,1)`, and `(1,0,0),(0,1,0),(0,0,1)`. The associated positive half is the computed CoHA character, not yet a full global atlas theorem.

Local anchors:

- `chapters/theory/quantum_groups_foundations.tex:16`, `:44`, `:89`, `:130`, `:137`, `:143`, `:159`.
- `compute/lib/coha_chart_explicit.py:385`, `:405`, `:430`, `:756`, `:772`, `:789`, `:1316`.
- `compute/tests/test_coha_chart_explicit.py:562`, `:567`, `:581`, `:825`.

Tests/computations run: full command above; direct extraction of `bps_invariants_jordan(5)`, `bps_invariants_conifold(3)`, `bps_invariants_local_p2(3)`.

Remaining obstruction: smallest executable witness is a fan-to-quiver oracle:

```text
toric fan / brane tiling -> quiver with potential -> basis charge support -> monoid closure -> orientation flag.
```

It should verify that the primitive vertex charges have nonzero BPS invariants and generate the chamber monoid.

## Cycle 2 - Conifold Chamber Change and KS Path Ordering

Status: computed/proved inside the rank-two quantum-torus truncation; conditional for arbitrary KS paths.

Attacked claim: the conifold chamber change supplies a computable chambered positive geometry and a path-ordered KS consistency check.

Failure mode: the exact conifold pentagon is implemented in the quantum torus. The Lie algebra Maurer-Cartan helper is not a substitute: `[\Theta,\Theta]=0` there is automatic by antisymmetry, and the manuscript already records that BCH captures only the leading commutator, not the full pentagon.

Healed theorem/formula/test oracle: for the resolved conifold rank-two sublattice with `YX=qXY`,

```tex
E(X)E(Y)=E(Y)E(XY)E(X)
```

is the executable chamber-change identity. Chamber I has primitive rays `(1,0),(0,1)`. Chamber II adds the bound-state tower `(1,n)`, visible in finite truncation. The chamber-independent scalar invariant used here is `\kappa_{\mathrm{ch}}(\mathrm{conifold})=1`.

Local anchors:

- `chapters/theory/cy_to_chiral.tex:3210`, `:4216`, `:4230`, `:5428`.
- `chapters/examples/toric_cy3_coha.tex:415`, `:803`, `:902`, `:1498`.
- `compute/lib/conifold_wall_crossing.py:359`, `:433`, `:501`, `:511`, `:556`, `:583`, `:754`.
- `compute/tests/test_conifold_wall_crossing.py:70`, `:77`, `:96`, `:141`, `:160`, `:199`, `:244`.
- `compute/tests/test_conifold_wc.py:228`, `:234`, `:242`, `:266`, `:292`, `:302`, `:369`.

Tests/computations run: exact pentagon at `(N_q,max_charge)=(12,6)`, numerical checks at `q=0.1,0.3,0.5`, chamber spectra, gauge transformation, DT/MacMahon decomposition.

Remaining obstruction: smallest executable witness for general chambered geometry is a path-word engine:

```text
ordered wall list + antisymmetric Euler pairing + wall functions E_\gamma^{\Omega(\gamma)}
-> quantum-torus automorphism product along a loop -> identity modulo charge/q truncation.
```

## Cycle 3 - Local `\mathbb P^2` Coefficients and Four-Kappa Sanity

Status: computed for stored GV/topological-vertex data; conditional as an all-degree theorem.

Attacked claim: local `\mathbb P^2` supplies a computable positive geometry with class `\mathbf M` shadow depth and stable kappa data.

Failure mode: the engines verify finite GV tables, Euler-product agreement through chosen truncations, and four-kappa consistency. They do not generate all local `\mathbb P^2` GV invariants from the mirror curve or topological vertex ab initio. Therefore class `\mathbf M` is computed from the stored high-degree GV table and growth witness, not proved as an all-degree theorem by this oracle alone.

Healed theorem/formula/test oracle:

```tex
(\kappa_{\mathrm{ch}},\kappa_{\mathrm{cat}},\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}})
(K_{\mathbb P^2})=(3/2,1,\text{undefined},1).
```

The coefficient oracle records:

```tex
n^0_1=3,\quad n^0_2=-6,\quad n^0_3=27,\quad n^0_4=-192,\quad n^0_5=1695,
```

and first genus-one nonzero value `n^1_3=-10`. The local surface formula is `\kappa_{\mathrm{ch}}=\chi_{\mathrm{top}}(\mathbb P^2)/2=3/2`; `\kappa_{\mathrm{BKM}}` is not defined because the toric local surface lacks the hyperbolic BKM lattice and Borcherds denominator input.

Local anchors:

- `chapters/examples/toric_cy3_coha.tex:1270`, `:1498`.
- `chapters/theory/cy_to_chiral.tex:5027`, `:5031`.
- `compute/lib/local_p2_shadow.py:237`, `:252`, `:1052`, `:1201`, `:1275`.
- `compute/lib/local_p2_four_kappa_engine.py:260`, `:475`, `:609`.
- `compute/tests/test_local_p2_shadow.py:65`, `:94`, `:248`, `:493`, `:527`.
- `compute/tests/test_local_p2_four_kappa_engine.py:176`, `:268`, `:375`.

Tests/computations run: local `\mathbb P^2` shadow tests, four-kappa tests, extracted GV values, Euler-product vs GV verification through degree `5`.

Remaining obstruction: smallest executable witness is an independent all-degree mirror/topological-vertex generator:

```text
mirror Picard-Fuchs / topological vertex -> GV extraction -> sign/growth/kappa checks -> comparison with stored table.
```

## Cycle 4 - PBW Hilbert-Series Shadows

Status: computed necessary condition; not a basis theorem by itself.

Attacked claim: PBW Hilbert-series shadows prove the positive basis or the Drinfeld double.

Failure mode: `coha_chart_explicit.py` verifies the character identity

```tex
\operatorname{PExp}(\operatorname{PLog} Z_{\mathrm{CoHA}})=Z_{\mathrm{CoHA}},
```

for the chart examples. This is a Hilbert-series shadow. It does not compute Hall multiplication structure constants, the perverse PBW filtration maps, nondegenerate Hall pairing, orientation local systems, or theta-basis positivity. The default finite `Sym^k` helper is not the independent theorem; the tested invariant is `pexp_match=True`.

Healed theorem/formula/test oracle: use the PBW engine as a falsifier/necessary condition:

```tex
\operatorname{gr}\mathrm{CoHA}\ \text{has the same character as}\ \mathrm{Sym}(\mathrm{BPS})
```

for `\mathbb C^3`, conifold diagonal, and local `\mathbb P^2`. Do not cite it as a proof of `\Theta^{\mathrm{BPS}}_\sigma` or of `D(Y^+_\sigma)`.

Local anchors:

- `chapters/theory/quantum_groups_foundations.tex:97`, `:99`, `:113`.
- `compute/lib/coha_chart_explicit.py:1042`, `:1093`, `:1149`, `:1281`.
- `compute/tests/test_coha_chart_explicit.py:703`, `:708`, `:714`, `:720`, `:883`, `:888`.

Tests/computations run: `ChartCoHA(...).verify_pbw()` for `\mathbb C^3`, conifold, local `\mathbb P^2`; all `pexp_match=True`.

Remaining obstruction: smallest executable witness is a low-charge shuffle/Hall product oracle:

```text
BPS primitive basis + shuffle kernel + Hall product constants
-> PBW filtration map -> associated-graded comparison -> Hall-pairing matrix determinant.
```

## Cycle 5 - Scattering, BPS Cone Closure, and `\phi_{0,1}` Overclaim

Status: RED/computed negative result for the present scattering engine; conjectural for general BPS positive bases.

Attacked claim: the current scattering diagram engine computes the full KS scattering diagram, root multiplicities, or `\Theta^{\mathrm{BPS}}_\sigma`.

Failure mode: `scattering_diagram.py` is explicitly a pair-commutator/leading BCH model. The symmetric Gram "bracket" is commutative rather than antisymmetric, so it is not a Lie bracket. Its wall multiplicities are rational and force composite positive roots, but the ratio to `\phi_{0,1}` coefficients is non-uniform. It is a useful RED oracle against overclaiming, not a full motivic KS computation.

Healed theorem/formula/test oracle: the admissible computed statement is:

```tex
\text{leading pair-commutator scattering forces walls in the positive cone,}
```

with qualitative `S_3` structure and nonzero `(1,1,1)` wall, but

```tex
\text{it does not compute the Borcherds/root-multiplicity scattering diagram.}
```

For conifold chamber consistency, use the quantum-torus pentagon in Cycle 2, not this BCH engine.

Local anchors:

- `chapters/theory/quantum_groups_foundations.tex:65`, `:71`, `:73`, `:173`, `:176`, `:179`.
- `compute/lib/scattering_diagram.py:4`, `:9`, `:15`, `:19`, `:131`, `:173`, `:355`, `:534`.
- `compute/tests/test_scattering.py:13`, `:231`, `:548`, `:654`, `:866`, `:891`.
- `compute/tests/test_scattering_diagram.py:6`.

Tests/computations run: scattering tests; extracted `scattering_diagram_walls(4)[(1,1,1)] = 8/3` and `ratio_analysis(4,1,"symmetric")["uniform"] = False`.

Remaining obstruction: smallest executable witness is a true KS automorphism oracle:

```text
antisymmetric Euler form + motivic BPS invariants \Omega(\gamma)
-> wall automorphisms on completed quantum torus
-> path-ordered products around loops
-> comparison with conifold pentagon and, separately, with BKM denominator data where defined.
```

## Cycle 6 - Kappa and Orientation Sanity

Status: computed for canonical toric kappa values; conditional for orientation data.

Attacked claim: kappa and orientation data are automatic consequences of chambered wall crossing.

Failure mode: wall crossing does not compute determinant-line square roots. The positive-geometry definition separately assumes orientation data and an oriented critical atlas. The compute layer also contains legacy chart-shadow normalisations, so the manuscript insertion must distinguish canonical `\kappa_{\mathrm{ch}}` from chart-shadow counts:

```tex
\kappa_{\mathrm{ch}}(\mathbb C^3)=1,\quad
\kappa_{\mathrm{ch}}(\mathrm{conifold})=1,\quad
\kappa_{\mathrm{ch}}(K_{\mathbb P^2})=3/2.
```

Conifold `\chi_{\mathrm{top}}/24=1/12` is not the chiral modular characteristic; local-surface `\chi_{\mathrm{top}}(S)/2` does not apply to the conifold because it is not `K_S`.

Healed theorem/formula/test oracle: orientation must remain a hypothesis in the positive-geometry theorem; the compute report can only certify the scalar kappa values and warn against the legacy doubled chart-shadow normalisations.

Local anchors:

- `chapters/theory/quantum_groups_foundations.tex:25`, `:59`, `:97`, `:99`.
- `chapters/theory/cy_to_chiral.tex:4163`, `:4682`, `:5027`, `:5141`, `:5161`, `:5428`.
- `chapters/examples/toric_cy3_coha.tex:719`, `:902`, `:1498`.
- `compute/lib/coha_chart_explicit.py:1284`, `:1316`.
- `compute/lib/kappa_ch_d3_formula.py:64`, `:67`, `:302`, `:688`.
- `compute/lib/cy_d_kappa_d3.py:75`, `:76`, `:507`.
- `compute/tests/test_kappa_ch_d3_formula.py:286`, `:431`, `:478`, `:481`.
- `compute/tests/test_cy_d_kappa_d3.py:557`, `:701`.

Tests/computations run: d=3 kappa tests, local four-kappa tests, canonical chart `kappa_ch()` extraction.

Remaining obstruction: smallest executable witness is an orientation oracle:

```text
critical chart atlas + determinant-line transition functions
-> Z/2 Cech cocycle
-> square-root trivialisation check on C3, conifold, local P2.
```

## Integration Verdict

Computed/proved in current oracle layer:

- Standard toric chart monoids and CoHA character/PBW Hilbert-series shadows for `\mathbb C^3`, conifold, local `\mathbb P^2`.
- Conifold quantum-torus pentagon and finite chamber-support changes.
- Local `\mathbb P^2` GV/kappa data on stored tables and tested truncations.
- Canonical toric values `\kappa_{\mathrm{ch}}(\mathbb C^3)=1`, `\kappa_{\mathrm{ch}}(\mathrm{conifold})=1`, `\kappa_{\mathrm{ch}}(K_{\mathbb P^2})=3/2`.

Conditional:

- `D(Y^+_\sigma)` as a quantum group: requires oriented critical atlas, Davison-Meinhardt PBW in the relevant category, and nondegenerate Hall pairing.
- Toric terminal degeneration beyond the standard executable examples: requires fan-to-quiver and orientation witnesses.
- Chambered KS consistency beyond the conifold: requires a path-ordered quantum-torus automorphism engine.

Conjectural/uncomputed by present engines:

- General `\Theta^{\mathrm{BPS}}_\sigma` positive basis.
- General BPS cone local finiteness and scattering consistency.
- Full chambered effective BPS positive geometry for non-toric CY3.
- Any toric `\kappa_{\mathrm{BKM}}` claim analogous to `K3\times E`; local `\mathbb P^2` has no BKM denominator datum in the current four-kappa engine.

