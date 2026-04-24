# Agent 10 - hCS / factorization algebra / Costello lane

Date: 2026-04-24

Mode: adversarial attack-heal, report-only. No manuscript edits, no commits, no destructive git.

Scope: 6d holomorphic Chern-Simons, Stage-1 factorization algebra, BV-BRST, E_n hierarchy, Costello-Gwilliam/Costello claims, and chain-level versus (infinity,1)-categorical proof lanes.

## Local surfaces inspected

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `notes/vol3_rearchitecture_proposal.tex`
- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/theory/hochschild_calculus.tex`
- `chapters/examples/cy_d_kappa_stratification.tex`
- `compute/lib/costello_5d_verification.py`
- `compute/tests/test_costello_5d_verification.py`
- `compute/lib/holomorphic_cs_chiral_engine.py`
- `compute/tests/test_holomorphic_cs_chiral_engine.py`
- `compute/lib/costello_paquette_defect_chiral.py`
- `compute/tests/test_costello_paquette_defect_chiral.py`
- `compute/lib/k3_yangian_twisted_11dsugra_1loop.py`
- `compute/tests/test_k3_yangian_twisted_11dsugra_1loop.py`

External primary anchors checked:

- Costello, `Supersymmetric gauge theory and the Yangian`, arXiv:1303.2632: https://arxiv.org/abs/1303.2632. The arXiv abstract explicitly places the exact calculation in perturbation theory.
- Fresse-Willwacher, `The intrinsic formality of E_n-operads`, arXiv:1503.08699: https://arxiv.org/abs/1503.08699. The statement is rational intrinsic formality for E_n operads for n >= 3, not a canonical contractible choice of every downstream algebraic lift.

## Computations run

Command:

```bash
python3 -m pytest compute/tests/test_costello_5d_verification.py compute/tests/test_holomorphic_cs_chiral_engine.py compute/tests/test_costello_paquette_defect_chiral.py compute/tests/test_k3_yangian_twisted_11dsugra_1loop.py -q
```

Result: `237 passed in 18.62s`.

Environment note: `python -m pytest ...` failed because `python` is not on PATH; the same test set passed under `python3`.

What the tests certify:

- `compute/tests/test_costello_5d_verification.py:7-20` checks 87 identities around the 5d gl_1 model: CY constraint, structure function reflection, `\phi_j` coefficients, one-loop CY constraint, Omega-background deformation, charge-2 R-matrix, Koszul duality, and AP compliance.
- `compute/lib/costello_5d_verification.py:10-13` itself separates 3d/5d proved cases from the 6d quantum-toroidal case, which it marks conjectural.
- `compute/tests/test_holomorphic_cs_chiral_engine.py:29-33` advertises multi-path checks, but the implemented assertions are algebraic parameter and combinatorial-bar checks, not a proof of hCS-to-Hall comparison.
- `compute/lib/costello_paquette_defect_chiral.py:20-24` and `:65-73` correctly mark the 6d lift and K3 x E defect endomorphism algebra as conjectural/not constructed.
- `compute/tests/test_k3_yangian_twisted_11dsugra_1loop.py:60-75` verifies the weight identity `5 = 2 + 3`; `:82-91` verifies `\hbar^2 = -1/8`; `:98-140` verifies selected Bruinier/EOT/Gritsenko leading Fourier coefficients.

What the tests do not certify:

- analytic convergence of all perturbative orders;
- a global 6d hCS quantization on compact CY_3;
- a chain-level quasi-isomorphism `Theta_{hCS -> Hall}`;
- algebra-level identification of `CoHA(K3 x E)` with the positive half of `\mathfrak g_{\Delta_5}`;
- on-the-nose boundary factorization algebra identification with `H_{\Delta_5}`.

## Executive verdict

The local value computations and gl_1 flat-model checks are healthy. The dangerous claims are scope claims: several manuscript statements promote perturbative/formal, flat, value-level, or conditional facts into all-orders, global, canonical, or algebra-level theorems. The heal is not to delete the mathematics; it is to split each claim by proof lane and status.

Recommended global status rule for this lane:

- `ClaimStatusProvedElsewhere`: operad-level E_n rational formality for n >= 3; 5d gl_1 Yangian perturbative construction on `C^2 x R`; value-level Borcherds/Gritsenko/Bruinier Fourier constants where checked.
- `ClaimStatusProvedHere`: local algebraic identities actually computed in `compute/`, e.g. `h_1+h_2+h_3=0`, `g(u)g(-u)=1`, `\phi_3=-2\sigma_3`, `5=2+3`.
- `ClaimStatusConditional`: Stage-1 `\Phi^{FA}_3` on verified framed/formal loci after a chosen formality datum; hCS-to-Hall; boundary restriction to `H_{\Delta_5}`; compact CY_3 BV quantization when obstruction vanishing is assumed.
- `ClaimStatusConjectured`: all-orders 6d hCS/K3 x E quantum-toroidal lift; `G(X)` in general; algebra-level K3 x E Hall-BKM equivalence beyond numerical/graded data.

## ATTACK_1 - Unsupported all-orders and convergence claims

Target claims:

- `chapters/theory/cy_to_chiral.tex:671-686` states an all-orders, simply-laced bosonic 5d hCS-to-Yangian VOA theorem and adds analytic-sounding convergence via Kontsevich-Tamarkin formality.
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:330-336` upgrades a one-loop/low-loop story toward unconditional all-orders `1/\Phi_{10}` by assuming higher heat coefficients vanish.
- `compute/lib/costello_5d_verification.py:10-13` is more disciplined than the manuscript: it marks the 6d holomorphic theory -> quantum toroidal step conjectural.

Failure mode:

Costello 2013 gives an exact calculation in perturbation theory for the Yangian gauge-theory model. That is not analytic convergence of a full path integral and does not by itself cover compact CY_3, 6d hCS, K3 x E, or all higher-loop BV exponentiation. The phrase "simply-laced bosonic" is also too broad for anomaly cancellation if the proof relies on vanishing of cubic or higher invariant tensors; type A and E6 require separate checks.

Exact formulas/constants locally verified:

- `g(u)=\prod_{i=1}^3 (u-h_i)/\prod_{i=1}^3 (u+h_i)`, `h_1+h_2+h_3=0`: `compute/lib/costello_5d_verification.py:40-41`, `compute/tests/test_costello_5d_verification.py:70-75`.
- `\phi_0=1`, `\phi_1=0`, `\phi_2=0`, `\phi_3=-2\sigma_3`: `compute/lib/costello_5d_verification.py:49-51`, `compute/tests/test_costello_5d_verification.py:167-200`.
- `\Psi=-\sigma_2`, with test values `1,3,7`: `compute/tests/test_costello_paquette_defect_chiral.py:151-183`.

HEAL_1:

Use this theorem scope:

```tex
\ClaimStatusProvedElsewhere[formal perturbative 5d flat model]
For the gl_1 holomorphic-topological theory on \mathbb C^2 \times \mathbb R
with Omega-background parameters h_1+h_2+h_3=0, the perturbative boundary
algebra has the affine-Yangian structure function
g(u)=\prod_i(u-h_i)/\prod_i(u+h_i).
This is a formal perturbative statement in the Costello 2013 sense.
It does not assert analytic convergence of the perturbation series, nor a
compact CY_3 or K3 \times E quantization.
```

Replace the simply-laced/all-orders claim by:

```tex
\ClaimStatusConditional
For non-abelian \mathfrak g, all-order perturbative quantization is asserted
only under the explicit Costello anomaly-cancellation hypotheses for the
chosen invariant tensors of \mathfrak g. The manuscript does not use this as
a proof of the 6d K3 \times E quantum-toroidal lift.
```

Open obligation:

Construct or cite a loop-order-by-loop-order anomaly cancellation theorem for the exact gauge algebra used in Vol III. Do not replace it by "simply-laced" unless the invariant-tensor check is written.

## ATTACK_2 - Stage-1 factorization algebra canonicity and E_3 formality

Target claims:

- `chapters/theory/cy_to_chiral.tex:22-29` and `:242-262` say Stage 1 is pinned up to contractible choice by Kontsevich-Tamarkin/Tamarkin plus Costello-Gwilliam locality.
- `chapters/theory/cy_to_chiral.tex:280-294` says Step (a) lifts up to contractible choice and Step (c) is resolved at d=3 by S^3 framing plus Costello TCFT.
- `chapters/theory/hochschild_calculus.tex:382-400` calls the relevant E_3 lift a contractible infinity-groupoid while also describing a GRT torsor.

Failure mode:

The same `cy_to_chiral.tex` file later records the noncanonical datum correctly:

- `chapters/theory/cy_to_chiral.tex:301-306`: the lift is not unique.
- `chapters/theory/cy_to_chiral.tex:318-325`: `Form_3(\mathbb Q)` is a free transitive `GRT_1(\mathbb Q)` torsor.
- `chapters/theory/cy_to_chiral.tex:333-340`: Stage-1 pinning is conditional on choosing a torsor point.
- `chapters/theory/cy_to_chiral.tex:400-402`: the torsor does not supply a canonical associator, does not rigidify S^3 framing, and does not commute automatically with Stage 2.

Fresse-Willwacher proves rational intrinsic formality of E_n operads for n >= 3. That proves an operad-level formality theorem. It does not make the downstream choice of rational formality datum contractible in Vol III's Stage-1 construction.

HEAL_2:

Replace all "contractible choice" language for d=3 Stage 1 by:

```tex
\ClaimStatusConditional
After choosing a rational E_3-formality datum
\alpha \in \operatorname{Form}_3(\mathbb Q),
with \operatorname{Form}_3(\mathbb Q) a GRT_1(\mathbb Q)-torsor,
Costello-Gwilliam locality assembles the corresponding local
factorization algebra on the verified formal/framed locus. The induced
cohomological E_3/Pois_3 invariants are independent of replacing
\alpha by an equivalent point, but the construction is not canonical
and not a contractible choice.
```

Status labels:

- Operad-level E_3 rational formality: `ClaimStatusProvedElsewhere`.
- Stage-1 factorization algebra for a concrete CY_3 object: `ClaimStatusConditional`.
- Canonical/functorial Stage-1 over all CY_3 categories: not proved; use `ClaimStatusConjectured` or avoid the claim.

Open obligation:

For every theorem invoking Stage 1, state the input datum explicitly: `(CY_3 object, holomorphic twist, framing/formality datum, locality hypothesis)`.

## ATTACK_3 - One-loop, BV-BRST, and Costello-Li graph claims

Target claims:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:49-59` gives the 6d hCS BV field/action and a Bochner-Martinelli propagator coefficient.
- `chapters/theory/hochschild_calculus.tex:403-416` says Costello-Li heat-kernel/BV construction degenerates to the Bochner-Martinelli propagator and graph weights equal Kontsevich integrals selecting the Kontsevich associator.
- `chapters/theory/hochschild_calculus.tex:418-447` writes a one-loop curving as `(\chi(X)/24)[\Omega_X]^{0,1}`, which is type-unstable.
- `chapters/examples/cy_d_kappa_stratification.tex:65-99` gives the better-typed anomaly definition:
  `\alpha_{BCOV}=(\chi_{top}(X)/24)\operatorname{tr}At(T_X)\in H^1(X,\mathcal O_X)`.

Failure mode:

The Bochner-Martinelli kernel is a local flat-chain witness. It is not, by itself, a graph-by-graph proof that Costello-Li compact heat-kernel weights equal the Kontsevich/Fresse-Willwacher E_3 formality weights. The `[\Omega_X]^{0,1}` expression is ill typed for a holomorphic `(3,0)` volume form; the typed object in the kappa-stratification file is the Atiyah-class trace.

Local formulas/constants to preserve:

- hCS field: `\mathcal A=c+A_{0,1}+A^*_{0,2}+c^*_{0,3}\in\Omega^{0,\bullet}(X,\mathfrak g)[1]`, `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:49-51`.
- hCS action:
  `S_{cl}=\int_X\Omega_X\wedge\langle A,\bar\partial A+\frac13[A,A]\rangle`, same local block.
- BM kernel coefficient:
  `P_{BM}(z)=2/(2\pi i)^3 * \sum_i (-1)^{i-1}\bar z_i d\bar z_{\hat i}/\|z\|^6`, `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:53-56`.
- Better anomaly typing:
  `\alpha_{BCOV}=(\chi_{top}(X)/24)\operatorname{tr}At(T_X)\in H^1(X,\mathcal O_X)`, `chapters/examples/cy_d_kappa_stratification.tex:65-99`.

HEAL_3:

Proposed replacement for the Costello-Li paragraph:

```tex
\ClaimStatusConditional
On the flat chart \mathbb C^3 the BV gauge-fixed kernel is represented by
the Bochner-Martinelli kernel
P_{BM}(z)=\frac{2}{(2\pi i)^3}
\frac{\sum_i(-1)^{i-1}\bar z_i\,d\bar z_{\widehat i}}{\|z\|^6}.
This is the chain-level propagator witness used in the local hCS lane.
The identification of the compact Costello-Li heat-kernel graph weights
with a chosen E_3 formality morphism is a separate graph-comparison
obligation and is not used as a proved canonical associator.
```

Proposed anomaly correction:

```tex
\alpha_{BCOV}(X)
=\frac{\chi_{top}(X)}{24}\operatorname{tr}At(T_X)
\in H^1(X,\mathcal O_X),
```

with the caveat:

```tex
For strict compact CY_3 with H^1(X,\mathcal O_X)=0 this class vanishes.
For K3\times E, \chi_{top}(K3\times E)=24\cdot 0=0, so the coefficient
vanishes before any stronger chain-level comparison is invoked.
```

Status labels:

- Flat BM kernel formula: `ClaimStatusComputed` or `ClaimStatusProvedHere` if derived locally.
- Compact graph-weight equality to E_3 formality: `ClaimStatusConditional`.
- `\alpha_{BCOV}` typed Atiyah-class formula: `ClaimStatusProvedElsewhere/Computed`, depending on citation.

Open obligation:

Add a graph-by-graph compactification/Feynman-integral comparison if the manuscript wants to say "selects the Kontsevich associator".

## ATTACK_4 - hCS-to-Hall and K3 x E Hall-BKM upgrade

Target claims:

- `chapters/theory/cy_to_chiral.tex:118-139` correctly says `CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1)` is Hall-side and that the missing comparison is `\Theta_{hCS\to Hall}`.
- `chapters/theory/cy_to_chiral.tex:560-589` correctly says critical CoHAs are Hall-side E_1 algebras, not inputs to `\Phi_3`.
- `chapters/theory/quantum_groups_foundations.tex:4286-4429` overpromotes K3 x E motivic DT/CoHA/Phi_3/Hall-Drinfeld/BKM claims into a single theorem.
- `chapters/theory/quantum_groups_foundations.tex:4437-4447` then admits the motivic lift is conjectural for K3 x E and strict theorem level is currently C^3/toric.

Failure mode:

The manuscript has the correct distinction in `cy_to_chiral.tex` but violates it in `quantum_groups_foundations.tex`. Numerical or graded equality of partition functions is not an algebra-level CoHA bracket theorem, and neither implies the hCS factorization algebra comparison.

Facts to preserve:

- `CoHA(\mathbb C^3)=Y^+`, positive half, not `\mathcal W_{1+\infty}` directly: `chapters/theory/cy_to_chiral.tex:118-139`.
- K3 x E value fingerprint:
  `\kappa_{ch}(K3\times E)=0`,
  `\kappa_{cat}(K3\times E)=0`,
  `\kappa_{ch}^{Heis}=3`,
  `\kappa_{BKM}(\Delta_5)=c_1(0)/2=5`,
  `\kappa_{fiber}(K3)=24`,
  `chapters/theory/quantum_groups_foundations.tex:5937-5967`.
- Weight identity `wt(\Delta_5)=5=2+3`, with `24` Kodaira `I_1` fibres contributing `24\cdot(1/8)=3`: `compute/lib/k3_yangian_twisted_11dsugra_1loop.py:62-72`, `:127-144`.
- Self-dual refined value `\hbar^2=-1/8`: `compute/lib/k3_yangian_twisted_11dsugra_1loop.py:79-92`.

HEAL_4:

Split the theorem into four statuses:

```tex
\ClaimStatusProvedElsewhere
The reduced numerical K3\times E DT partition function has the Oberdieck
Siegel modular form expression, and the Borcherds/Gritsenko side gives
\kappa_{BKM}(\Delta_5)=c_1(0)/2=5.

\ClaimStatusComputed
The local Fourier and weight checks used here give
wt(\Delta_5)=5=2+3 and the checked Bruinier/EOT/Gritsenko coefficients.

\ClaimStatusConjectured
The motivic K3\times E CoHA is the positive half of the Borcherds
superalgebra \mathfrak g_{\Delta_5} as an algebra with bracket and Hopf
pairing.

\ClaimStatusConditional
\Phi_3(D^bCoh(K3\times E))\simeq H_{\Delta_5} only after the oriented
comparison \Theta^{or}_{hCS\to Hall}, the Hall-Borcherds bracket
identification, and the Drinfeld-double pairing are constructed.
```

Open obligation:

Write the comparison object as an actual map:

```tex
\Theta^{or}_{hCS\to Hall}:
Obs^{q}_{hCS}(X,\mathfrak g) \longrightarrow CoHA(X)
```

with orientation data, multiplication compatibility, coproduct/Hopf pairing compatibility, and a checked image of the BM one-loop class.

## ATTACK_5 - Factorization-to-chiral / Costello-Paquette boundary claims

Target claims:

- `chapters/theory/quantum_groups_foundations.tex:5672-5935` states a Costello-Li-Paquette style 3d holomorphic-topological QFT proposition and identifies the boundary restriction with `H_{\Delta_5}` on the nose at chain level.
- `chapters/theory/quantum_groups_foundations.tex:5937-5967` then takes the K3 x E fingerprint as a corollary of that boundary identification.
- `compute/lib/costello_paquette_defect_chiral.py:20-24` and `:65-73` are stricter: they mark the 6d lift and K3 x E universal defect as conjectural/not constructed.

Failure mode:

Costello-Paquette style defect/Koszul duality can motivate the architecture, but the local code and the repo cache do not prove a boundary restriction quasi-isomorphism

```tex
i^*\mathcal F_{THT} \simeq H_{\Delta_5}
```

for K3 x E. The seven-face `r_{CY}` statement is therefore not a proved consequence of the boundary factorization algebra unless the boundary map is constructed.

HEAL_5:

Keep the value corollary, detach it from the unproved boundary theorem:

```tex
\ClaimStatusComputed/ProvedElsewhere
The numerical fingerprint for K3\times E is
\{\kappa_{ch},\kappa_{cat},\kappa_{ch}^{Heis},
\kappa_{BKM},\kappa_{fiber}\}=\{0,0,3,5,24\},
with the displayed meanings of the five entries.
```

Change the boundary proposition to:

```tex
\ClaimStatusConditional
Assume a two-coloured factorization algebra for the
holomorphic-topological theory on E\times \mathbb R_{\ge 0} with boundary
condition B, and assume a chain-level quasi-isomorphism
i^*\mathcal F_{THT,B}\simeq H_{\Delta_5} compatible with OPE,
factorization products, and the Hopf pairing. Under these assumptions,
the seven faces of r_{CY} attach to the same K3\times E boundary object.
```

Open obligation:

Construct the two-coloured factorization algebra and the boundary restriction map. Until then, do not state "on the nose chain-level".

## ATTACK_6 - `G(X)` representability and global quantum vertex group

Target claims:

- `chapters/theory/quantum_groups_foundations.tex:555-640` states `thm:qgf-G-X-representability` as `ClaimStatusProvedHere`, using Brown-Lurie style representability to assert an abstract quantum vertex chiral group `G(X)` for compact and noncompact CYs.
- Repo instruction cache says `G(X)` is unconstructed in general and CY-C remains conjectural.

Failure mode:

Representability of a formal moduli functor is not the same as constructing the quantum vertex chiral group with the multiplication, coproduct, OPE, factorization, and Hopf pairing needed in the later hCS/Hall/BKM arguments. The theorem currently makes the hard CY-C object look automatic.

HEAL_6:

Proposed replacement scope:

```tex
\ClaimStatusConjectured
There is expected to be a quantum vertex chiral group G(X) representing
the chiral deformation functor attached to \Phi(X), when the relevant
presentability, continuity, dualisability, and factorization-Hopf
conditions hold. This theorem records the moduli problem and the
representability criterion; it does not construct G(X) in general.
```

Add a proved subcase only if the local model is present:

```tex
\ClaimStatusProvedElsewhere
For the flat toric \mathbb C^3/Hall-side model, the positive-half
algebra is the known CoHA/Yangian object. This is not the general
CY-C group G(X).
```

Open obligation:

List the exact category, compactness/presentability hypotheses, and limit-preservation proof for the functor represented by `G(X)`. Without those, keep the theorem conjectural.

## ATTACK_7 - Chain-level versus (infinity,1)-categorical lane conflation

Target claims:

- `notes/vol3_rearchitecture_proposal.tex:47-57` says the infinity-categorical route resolves the object-level CY-A3 obstruction via `HH^{-2}_{E1}=0` and contractibility of E1 lifts.
- `notes/vol3_rearchitecture_proposal.tex:555-569` packages a four-step factorization envelope and says the S^3 obstruction is resolved on verified framed loci.
- `chapters/theory/hochschild_calculus.tex:543-592` states broad HH^{-2} vanishings, while K3 x E and generic compact CY_3 examples have nontrivial Hodge pieces unless extra hypotheses are imposed.

Failure mode:

The categorical lane can prove deformation control under its hypotheses. It does not automatically produce a chain-level BV kernel, a compact Feynman expansion, or the hCS-to-Hall quasi-isomorphism. Conversely, the chain-level BM/Feynman lane gives local witnesses but not global functoriality.

HEAL_7:

Use this lane declaration before CY_3 Stage-1 statements:

```tex
There are two load-bearing lanes.
The chain-level lane supplies explicit BV complexes, propagators, and
Feynman/CoHA comparison maps when they are constructed.
The (infinity,1)-categorical lane supplies deformation-theoretic control
of the object-level functor under the stated vanishing and dualisability
hypotheses. Neither lane replaces the other. In particular, categorical
rigidity does not prove analytic all-orders hCS convergence, and a local
propagator does not prove global \Phi_3 functoriality.
```

Status labels:

- Object-level CY-A3 on verified formal/framed loci: `ClaimStatusConditional` or `ClaimStatusProvedHereConditional`, but only with H1-H4 displayed.
- Arbitrary smooth proper CY_3 Stage-1 functorial theorem: not proved.
- hCS-Hall map: `ClaimStatusOpen/Conditional`.

Open obligation:

When invoking `HH^{-2}_{E1}=0`, state the exact hypothesis: Koszul/formal locus, `HT^1=0`, or the verified object-level class. Do not state it for every smooth proper CY_3.

## Proposed text edits by file

### `chapters/theory/cy_to_chiral.tex`

1. At `:22-29`, `:256-262`, `:293`, replace "pinned up to contractible choice" by "after choosing a rational E_d-formality datum; for d=3 the choices form a `GRT_1(\mathbb Q)`-torsor".
2. At `:671-686`, replace the all-orders/convergence theorem by a formal perturbative theorem on the flat 5d model plus an explicit conditional clause for non-abelian anomaly cancellation.
3. Preserve `:118-139` and `:560-589` as the correct hCS/Hall discipline; use those paragraphs to correct `quantum_groups_foundations.tex`.
4. At `:637-656`, clarify whether the theory is genuinely 5d (`\mathbb C^2\times\mathbb R`) or a 7-real-dimensional product (`CY_3\times\mathbb R_t`). The current notation `Y=X\times\mathbb R_t` with `X` a CY_3 conflicts with the "5d" label.

### `chapters/theory/hochschild_calculus.tex`

1. At `:382-400`, split E_3 rational formality from the noncanonical formality datum; remove "contractible infinity-groupoid" if a GRT torsor is in play.
2. At `:403-416`, downgrade the Costello-Li/BM-to-Kontsevich graph comparison to conditional unless a graph-by-graph proof is supplied.
3. At `:418-447`, replace `[\Omega_X]^{0,1}` with `( \chi_{top}(X)/24 ) tr At(T_X) in H^1(X,O_X)`, matching `cy_d_kappa_stratification.tex:65-99`.
4. At `:543-592`, narrow HH^{-2} vanishing to the stated verified locus; do not use it for all smooth proper CY_3.

### `chapters/theory/quantum_groups_foundations.tex`

1. At `:555-640`, downgrade `G(X)` representability to a conjectural representability criterion unless the category and functorial hypotheses are proved.
2. At `:4286-4429`, split K3 x E into numerical DT, graded/Borcherds constants, conjectural motivic CoHA algebra, and conditional `\Phi_3`/Hall double comparison.
3. At `:5672-5935`, change Costello-Li-Paquette boundary identification with `H_{\Delta_5}` from `ProvedHere` to `Conditional`.
4. At `:5937-5967`, keep the fingerprint values but make clear they are independently verified constants, not proof of the boundary equivalence.

### `chapters/examples/cy_d_kappa_stratification.tex`

1. Preserve the anomaly definition at `:65-99`; it is better typed than the Hochschild paragraph.
2. For local conifold/local `\mathbb P^2` `\kappa_{chBV}` rows around `:1774-1894`, consider `ClaimStatusComputed` or `ClaimStatusConditional` rather than `ProvedHere` unless the boundary-link zeta regularisation is independently checked.

### `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`

1. At `:13-15`, replace Stage-1 "canonical up to contractible choice" by torsor-choice language.
2. At `:330-336`, keep T-CL-K3 and T-AllLoop separated; do not close all-orders from assumed vanishing of heat coefficients.
3. At `:391-397`, retain the warning that CFG 2026 is 3d CS/knot, not 6d hCS.

## Local constants ledger

- 6d hCS field package:
  `\mathcal A=c+A_{0,1}+A^*_{0,2}+c^*_{0,3}\in\Omega^{0,\bullet}(X,\mathfrak g)[1]`.
- 6d hCS classical action:
  `S_{cl}=\int_X\Omega_X\wedge\langle A,\bar\partial A+\frac13[A,A]\rangle`.
- Flat BM propagator coefficient:
  `2/(2\pi i)^3`.
- Omega-background CY constraint:
  `h_1+h_2+h_3=0`.
- Affine-Yangian structure function:
  `g(u)=\prod_i(u-h_i)/\prod_i(u+h_i)`.
- Leading coefficient:
  `\phi_3=-2\sigma_3`, with `\sigma_3=h_1h_2h_3`.
- Defect/effective level:
  `\Psi=-\sigma_2`, with `\sigma_2=h_1h_2+h_1h_3+h_2h_3`.
- Tested values:
  self-dual `(1,0,-1)`: `\sigma_2=-1`, `\sigma_3=0`, `\kappa_{ch}=1`;
  SV N=2 `(1,-2,1)`: `\sigma_2=-3`, `\sigma_3=-2`, `\kappa_{ch}=3`;
  generic `(1,-3,2)`: `\sigma_2=-7`, `\sigma_3=-6`, `\kappa_{ch}=7`.
- BCOV/BV anomaly typing:
  `\alpha_{BCOV}=(\chi_{top}(X)/24)tr At(T_X)\in H^1(X,\mathcal O_X)`.
- K3 x E:
  `\chi_{top}(K3\times E)=24\cdot 0=0`,
  `\kappa_{ch}(K3\times E)=0`,
  `\kappa_{cat}(K3\times E)=0`,
  `\kappa_{ch}^{Heis}=3`,
  `\kappa_{BKM}(\Delta_5)=c_1(0)/2=5`,
  `\kappa_{fiber}(K3)=24`.
- One-loop/Borcherds weight check:
  `wt(\Delta_5)=5=2+3`,
  `24\cdot(1/8)=3`,
  `\hbar^2=-1/8` at the self-dual refined Omega point.

## Remaining open obligations

1. Construct `\Theta^{or}_{hCS\to Hall}` as a chain-level map with orientation data, multiplication compatibility, and Hopf pairing compatibility.
2. Prove or cite the graph-by-graph comparison between compact Costello-Li heat-kernel weights and the selected E_3 formality morphism.
3. Rewrite Stage-1 factorization statements so the GRT torsor is explicit and no canonical associator is smuggled into the theorem.
4. Verify non-abelian one-loop and higher-loop anomaly cancellation by invariant tensor, not by the word "simply-laced".
5. Resolve the "5d hCS" dimensional convention where `X` is a CY_3 but the product `X\times\mathbb R_t` is used.
6. Downgrade `G(X)` in general until the representing category, continuity, presentability, and Hopf/factorization structure are constructed.
7. Separate K3 x E numerical DT/Borcherds data from motivic CoHA algebra, Hall-BKM bracket, Drinfeld double, and `\Phi_3` comparison.
8. Keep the K3 x E fingerprint values, but do not use them to prove the boundary factorization algebra equivalence.

## Bottom line

The hCS/Costello lane is viable after status repair. The flat 5d gl_1 and value-level one-loop/Borcherds computations are useful, tested, and should remain. The current theorem prose must stop upgrading them to canonical Stage-1 functoriality, global 6d hCS quantization, hCS-to-Hall algebra equivalence, or all-orders convergence without the missing chain-level maps and anomaly checks.
