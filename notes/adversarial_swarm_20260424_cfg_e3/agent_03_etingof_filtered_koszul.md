# Agent 03: Etingof-Kontsevich filtered-Koszul examiner

Date: 2026-04-24.

Assigned surface: filtered Koszul duality from filtered `E_3` observables to braided / quantum-group module categories, comparing Costello--Francis--Gwilliam 2026, arXiv:2602.12412, Sections 1.5--1.8 and 3, with the Vol III `\Phi_3` / CY3 claims.

Files edited: only this report.

Local manuscript files not edited.

## Executive verdict

CFG proves a precise theorem for ordinary 3-dimensional Chern--Simons theory:

```tex
A_0 = C^*(\g) = Sym(\g^\vee[-1]),\qquad
F^p A_0 = Sym^{\ge p}(\g^\vee[-1]),
```

with a filtered `E_3` quantization `A_hbar^lambda` over `C[[hbar]]`, `F^i C[[hbar]] = hbar^{2i} C[[hbar]]`, whose perfect modules form an `E_2`-monoidal category equivalent to finite-dimensional Drinfeld--Jimbo modules:

```tex
(C^*\g)^! \simeq (U\g)^\vee,\qquad
Perf_{C^*\g} \simeq Fin_{U\g}^{op},\qquad
Perf_{C^*_\hbar(\g)} \simeq Rep^{dg}_{fin}(U_\hbar\g).
```

This is a valid model theorem for the logical pattern

```tex
filtered E_3 observables -> filtered Koszul duality -> braided modules.
```

It is not a theorem proving the Vol III CY3 chain

```tex
\Phi_3^{(\Sigma_2,C)}(\cC)
  = \SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))
  \in E_1-ChirAlg(C),
```

nor the hCS-to-Hall comparison, nor the quantum-toroidal / BPS module category. CFG's `C^*(\g)` is the locally constant / topological associated model. The Vol III CY3 avatar is the Dolbeault chiral CE and chiral enveloping factorization algebra in three holomorphic variables, with holomorphic jets in `z_1,z_2,z_3`, multidirectional OPE residues over polydiscs, and Weiss/Ran descent. Vol III already states the correct restriction: CFG supplies the ordinary 3d CS analogue, not the 6d hCS-to-Hall theorem (`chapters/theory/en_factorization.tex:567`; `chapters/theory/cy3_chain_level_bridge.tex:227`).

## Source anchors

- CFG arXiv page: `https://arxiv.org/abs/2602.12412`, submitted 2026-02-12. The abstract states the filtered `E_3` algebra from BV quantization of Chern--Simons and perfect modules from Drinfeld--Jimbo representations.
- CFG Section 1.5: `LMod_A` for an `E_3` algebra is `E_2`-monoidal; filtered Koszul duality gives `Perf_{C^*(g)} ~= Rep_fin(g)^dg`.
- CFG Section 1.6: the deformation spaces of CS quantizations, filtered `E_3` deformations of `C^*(g)`, braided deformations of `Rep_fin(g)`, and quasi-triangular quasi-Hopf quantizations of `U(g)` are canonically bijective up to the named choices.
- CFG Section 1.7: Wilson lines are implemented by 1-dimensional fermionic defects; after quantization, boundary observables deform `C^*(g,S_V)` to an `A^lambda`-module.
- CFG Section 1.8: perfect `A`-modules for an `E_3` algebra produce Reshetikhin--Turaev tangle invariants by factorization homology.
- CFG Section 3: complete filtered complexes, `A = C^*g`, `(C^*g)^! ~= (Ug)^vee`, `Perf_{C^*g} ~= Fin_{Ug}^{op}`, and the quantized corollary `Perf_{C^*_\hbar(g)} ~= Rep^{dg}_{fin}(U_\hbar g)`.
- Vol III `\Phi_3`: `chapters/theory/cy_to_chiral.tex:4681` says the `d=3` output is native `E_1` and braiding is recovered through the Drinfeld centre; `chapters/theory/cy_to_chiral.tex:4691` is the conditional theorem; `chapters/theory/cy_to_chiral.tex:4739` states the `E_3 -> E_2` restriction is symmetric and non-symmetric quantum-group braiding comes from the Drinfeld center.
- Vol III CY3 local site: `chapters/theory/cy3_chain_level_bridge.tex:73` fixes the Dolbeault/Weiss/Ran site; `chapters/theory/cy3_chain_level_bridge.tex:277` requires locality for the Dolbeault topology and Weiss descent.
- Vol III bar--CE passage: `chapters/theory/cy_to_chiral.tex:4914` identifies the bar complex of the chiral envelope with the Chevalley--Eilenberg chain complex of the input Lie conformal algebra.
- Vol III `E_3` bar object: `chapters/theory/en_factorization.tex:636` states that `B_{E_3}` carries three commuting differentials and coproducts from OPE residues in each complex direction.

## Associated model versus chiralized filtered object

The exact comparison is a three-level filtration, not an identification of the CY3 avatar with ordinary `C^*(\g)`.

Topological associated model, CFG:

```tex
A^{top}_{CFG} = C^*(\g)
```

is the locally constant model obtained from the formal classifying stack of the constant gauge Lie algebra on a 3-ball.

CY3 chiralized filtered object, on a small holomorphic polydisc `P = D^3_{z_1,z_2,z_3} \subset X`:

```tex
\mathfrak L_X(P)
  :=
\Omega^{0,*}(P, J^{hol}_{z_1,z_2,z_3}\mathfrak l_X),
```

where `\mathfrak l_X` is the CY3 dg-Lie / Lie-conformal input supplied by polyvectors or the hCS gauge complex, `J^{hol}` denotes holomorphic jets in the three complex directions, and the differential includes `\bar\partial` plus the CE / BV differential. The classical chiral observable algebra is the completed Dolbeault CE object

```tex
\Obs^{cl}_{X}(P)
  =
C^*_{cont}\!\left(\mathfrak L_X(P)[1]\right),
```

and the bar side of the chiral envelope is

```tex
B_{E_3}\!\left(U^{ch}_{E_3}(\mathfrak L_X)\right)(P)
  \simeq
CE^{ch,Dolb}_*\!\left(\mathfrak L_X(P)\right).
```

The filtered quantum object has the schematic form

```tex
\Obs^q_X(P)
  =
C^*_{cont}\!\left(\mathfrak L_X(P)[1]\right)
[[\epsilon_1,\epsilon_2,\epsilon_3]]_{\,\epsilon_1+\epsilon_2+\epsilon_3=0}
```

with `E_3` factorization products over disjoint polydiscs and three OPE-residue directions. Its associated gradeds are:

```tex
gr_{\epsilon}\Obs^q_X(P)
  =
C^*_{cont}\!\left(\mathfrak L_X(P)[1]\right)
```

still Dolbeault, jet, and chiral; and only after taking the constant-mode / locally constant / finite Lie algebra specialization

```tex
H_{\bar\partial}(P)\to C,\qquad
J^{hol}_{z_1,z_2,z_3}\mathfrak l_X \to \mathfrak g_x,
```

does one recover the CFG-shaped model

```tex
C^*_{cont}(\mathfrak L_X(P)[1])
  \rightsquigarrow
C^*(\mathfrak g_x).
```

Thus `C^*(\g)` is an associated model of the constant topological limit. It is not the CY3 object.

## ATTACK -> HEAL cycle 1: the source algebra

ATTACK. Treating CFG's filtered `E_3` algebra as the Vol III CY3 Stage-1 algebra is false at the first object.

CFG object:

```tex
A_0 = C^*(\g) = (Sym(\g^\vee[-1]), d_{CE}),\qquad
F^p A_0 = Sym^{\ge p}(\g^\vee[-1]).
```

The classical stack is the formal neighbourhood of the trivial flat `G`-bundle on a 3-ball; the ball is contractible, so the classical observables are Lie algebra cochains. The associated graded check is exact:

```tex
gr_F A^\lambda_\hbar \cong C^*(\g)
```

as the commutative `E_\infty` algebra underlying the filtered `E_3` deformation.

Vol III CY3 Stage-1 object is not just `\PhiFA_3(\cC)` as a symbol; on a polydisc it is the Dolbeault chiral CE / enveloping factorization object

```tex
\PhiFA_3(\cC)(P)
  \simeq
\Obs^q_X(P)
  =
C^*_{cont}\!\left(
  \Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X)[1]
\right)[[\epsilon_1,\epsilon_2,\epsilon_3]],
\qquad
\epsilon_1+\epsilon_2+\epsilon_3=0.
```

It is built from the CY3 Hochschild / polyvector data, holomorphic jets, the Dolbeault differential, Costello--Li holomorphic hCS locality, and an `S^3` framing datum. Its factorization products are products over disjoint holomorphic polydiscs; its bar object carries three directional OPE-residue differentials. For `K3 x E`, the local manuscript anchor says this is a 6d holomorphic Chern--Simons factorization algebra on the CY3 target, not ordinary 3d CS (`chapters/theory/cy_to_chiral.tex:4689`).

HEAL. Use CFG only as the 3d topological model:

```tex
C^*(\g) \leadsto C^*_\hbar(\g)
```

For CY3, the honest replacement is the chiralized Dolbeault CE object:

```tex
\mathfrak L_X(P)=\Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X),
\qquad
\Obs_X(P)=C^*_{cont}(\mathfrak L_X(P)[1])
  \quad\text{with a separate comparison map}\quad
\Theta_{hCS\to Hall}.
```

NO-GO POINT. There is no algebra map in CFG identifying

```tex
C^*_\hbar(\g) \simeq \PhiFA_3(\Perf(X)).
```

The left side is the finite semisimple Lie algebra cochain model for ordinary 3d topological CS. The right side is a Dolbeault / holomorphic-jet / chiral CE factorization algebra with a still separate hCS-to-Hall datum. The former is only the constant-mode associated model of the latter.

## ATTACK -> HEAL cycle 2: filtered Koszul duality and finiteness

ATTACK. CFG's Koszul duality depends on complete filtered complexes and finite-dimensional Lie theory. It is the constant-mode associated model of the CY3 chiral CE story, not its replacement. The exact CFG presentation is:

```tex
(C^*\g)^! = C \otimes^{L}_{C^*\g} C \simeq (U\g)^\vee
```

as complete filtered Hopf algebras. Then:

```tex
Perf_{C^*\g} \simeq Fin_{U\g}^{op}
```

where `Fin` means bounded total finite-dimensional cohomology.

The associated graded check is the PBW filtration:

```tex
gr_F U\g \cong Sym(\g),
```

dual to the symmetric filtration on `C^*\g`.

The CY3 chiral CE object has a different associated-graded tower:

```tex
gr_{\epsilon} CE^{ch,Dolb}_*(\mathfrak L_X(P))
  =
CE^{ch,Dolb}_*\!\left(
  \Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X)
\right),
```

with the `E_3` bar differential split into the Dolbeault differential, the CE differential, and the three OPE-residue directions. Only after the extra specialization

```tex
\Omega^{0,*}(P,-)\to H^0_{\bar\partial}(P,-),\qquad
J^{hol}\to \text{constant jets},\qquad
\mathfrak l_X\to \mathfrak g_x
```

does it collapse to the CFG-shaped `CE_*(\mathfrak g_x)` or dually `C^*(\mathfrak g_x)`.

Vol III CY3 quantum-group candidates are typically not finite-dimensional semisimple `U\g` modules. Toric `C^3` gives `CoHA(C^3) = Y^+(\widehat{\mathfrak{gl}}_1)`, a positive half; `K3 x E` gives a BKM / Hall--Drinfeld / Borcherds object. These require topological completions, equivariant parameters, root completions, and often Fock-type modules, not `Fin_{U\g}`.

HEAL. The correct transplant is a conditional filtered-topological analogue:

```tex
Perf^{cont}_{A_X}
  \stackrel{?}{\simeq}
Rep^{cont}_{finite-energy}(G_X),
```

where `A_X = \Phi_3^{(\Sigma_2,C)}(\cC)` is the specialized `E_1` chiral algebra and `G_X` is only constructed on named loci. For `C^3`, the proved Hall-side object is the positive half; full braided data requires the Drinfeld double / center passage.

NO-GO POINT. CFG does not justify replacing `CE^{ch,Dolb}_*(\mathfrak L_X(P))` by `CE_*(\g)`, nor replacing `Fin_{U\g}` by modules over `Y^+`, a quantum toroidal algebra, or a BKM quantum group. The finiteness, PBW, completion, and chiral-envelope hypotheses must be reproved after the Dolbeault/chiral CE object is kept.

## ATTACK -> HEAL cycle 3: where braiding lives

ATTACK. A common false shortcut is:

```tex
E_3\text{-observables} \Rightarrow E_2\text{-braiding} \Rightarrow R\text{-matrix on }\Phi_3(\cC).
```

CFG permits this for ordinary 3d CS because `LMod_A` for an `E_3` algebra is `E_2`-monoidal, and filtered Koszul duality identifies this `E_2` category with a Drinfeld--Jimbo braided category.

Vol III explicitly blocks the same inference for CY3. The local theorem states:

```tex
A_\cC^{(\Sigma_2,C)} \in E_1-ChirAlg(C),
```

and:

```tex
Z(Rep^{E_1}(A_\cC^{(\Sigma_2,C)}))
```

is where the non-symmetric `E_2` braiding is recovered (`chapters/theory/cy_to_chiral.tex:4719`). The manuscript also states that the `E_3 -> E_2` restriction from the `S^3` framing is topologically symmetric because `pi_1 Conf_2(R^3)=0` (`chapters/theory/cy_to_chiral.tex:4739`).

Associated graded check:

```tex
gr(R) = 1 + \hbar r + O(\hbar^2),\qquad r + r^{21} = \Omega
```

for the Drinfeld--Jimbo side. The symmetric part is forced by the Casimir; the skew part supplies the cobracket. Vol III's `E_3` restriction alone has no such non-symmetric skew half-braiding. The half-braiding is extra center data:

```tex
R(z) = \sigma_{V_u}(V_v),\qquad z=u-v.
```

HEAL. State the CY3 route as:

```tex
E_1\text{-chiral } A_X
  \longrightarrow
Z(Rep^{E_1}(A_X))
  \longrightarrow
R\text{-matrix / quantum-group modules}.
```

CFG supports the existence of such a pattern in one topological case, but the CY3 braiding proof is center-theoretic, not a direct consequence of `E_3` observables.

NO-GO POINT. Do not cite CFG to assert native non-symmetric `E_2` braiding on `\Phi_3(\cC)`. For `d=3`, native output is `E_1`; non-symmetric braiding lives on the Drinfeld center of its representation category.

## ATTACK -> HEAL cycle 4: deformation parameters and associated graded

ATTACK. CFG's deformation parameter is the CS level / invariant pairing, with deformation space noncanonically identified with:

```tex
\hbar H^3(\g)[[\hbar]]
```

for semisimple `g`. The filtered base convention in CFG is:

```tex
F^i C[[\hbar]] = \hbar^{2i} C[[\hbar]].
```

In the CY3 / quantum-toroidal direction, the natural parameters are:

```tex
h_1+h_2+h_3=0,\qquad
g(u)=\prod_{i=1}^3 {u-h_i \over u+h_i},
```

or multiplicatively `(q,t,q_3)` with `q t q_3 = 1`. There are two free equivariant parameters, and Miki triality permutes the three directions.

Associated graded computation run in this turn:

```text
verify_structure_function_inversion():
u=37:  g=12636/12635, g^!=12635/12636, product=1
u=41:  g=17200/17199, g^!=17199/17200, product=1
u=-53: g=37179/37180, g^!=37180/37179, product=1
u=97:  g=228096/228095, g^!=228095/228096, product=1
```

This verifies the local Koszul-inversion identity `g(u)g^!(u)=1` for the Yangian-style structure function. It does not identify the deformation complex with CFG's `H^3(g)[[hbar]]`.

HEAL. Keep two statements separate:

```tex
CFG:       one-parameter filtered E_3 deformation of C^*(\g).
CY3/DIM:  two-parameter equivariant deformation with h_1+h_2+h_3=0.
```

Use the computed inversion identity as evidence for the CY3 Koszul-duality pattern, not as a CFG theorem transfer.

NO-GO POINT. There is no parameter-preserving map from CFG's semisimple CS deformation functor to the quantum-toroidal deformation functor. Miki triality has no CFG counterpart.

## ATTACK -> HEAL cycle 5: hCS-to-Hall and positive half versus full quantum group

ATTACK. CFG Section 1.6 identifies the braided deformation category with quasi-triangular quasi-Hopf quantizations of `U(g)` up to Drinfeld twist. That is a full quantum group module category.

Vol III toric CY3 starts with the Hall positive half:

```tex
CoHA(C^3) \simeq Y^+(\widehat{\mathfrak{gl}}_1),
```

not the full `W_{1+\infty}` and not automatically the full quantum toroidal algebra. The local theorem records that for `C^3`, the full `W_{1+\infty}` at `c=1` is recovered only after the Drinfeld double / center / vacuum evaluation passage (`chapters/theory/cy_to_chiral.tex:10570`).

Associated graded check:

```tex
Y^+ \subsetneq D(Y^+) = Y,\qquad
Z(Rep^{E_1}(Y^+))\ \text{is extra data}.
```

CFG starts after the corresponding full Drinfeld--Jimbo category has already been identified by filtered Koszul duality. Vol III still has to construct the center passage and, for compact CY3, the map

```tex
\Theta_{hCS\to Hall}.
```

HEAL. The admissible statement is:

```tex
CFG proves the 3d CS filtered-Koszul model.
Vol III CY3 has an analogous target diagram only on named loci:
  PhiFA_3 -> SpCh -> E_1 chiral A_X -> center/double -> braided modules.
```

NO-GO POINT. Do not collapse `Y^+`, `D(Y^+)`, `W_{1+\infty}`, and `\Phi_3(\cC)`. CFG's theorem has no positive-half stage; Vol III does.

## ATTACK -> HEAL cycle 6: Wilson lines, traces, and knot invariants

ATTACK. CFG Sections 1.7--1.8 are not merely module-category statements. They use 1-dimensional defects, perfect `A`-modules, the Tangle Hypothesis, and factorization homology traces to recover Reshetikhin--Turaev link invariants:

```tex
\int_{K\subset R^3} tr(V) = Z_V(K\subset R^3).
```

The line-defect presentation is concrete: a fermion pair

```tex
\psi \in \Omega^0(R,V),\qquad
\bar\psi \in \Omega^0(R,V^*)
```

with coupling

```tex
S_{coup}=\int_K <\bar\psi,(d+K^*A)\psi>_V
```

produces Clifford observables and, after quantization, an `A^\lambda`-module.

Vol III CY3 has codimension-two / curve-defect analogues, but the full chiral Kontsevich or RT-style invariant is not supplied by CFG. The local compute witness `compute/lib/cfg25_adversarial_consistency.py` reports this correctly at the level of attack summary: Kontsevich analogue partial, Jones analogue structural, WRT/RT major gaps. Running `CFG25AdversarialSuite().summary_report()` in this turn returned:

```text
1_kontsevich: PARTIAL
2_jones: STRUCTURAL
3_volume_conjecture: FILLED (analogue, not lift)
4_verlinde: PARTIAL
5_wrt: MAJOR
6_rt: MAJOR
```

HEAL. The CY3 statement must be phrased as a separate defect construction problem:

```tex
\text{holomorphic curve } C\subset X
  \leadsto
\text{constructible hCS factorization algebra}
  \leadsto
\text{trace / chiral invariant}.
```

CFG supplies the topological line-defect prototype, not the CY3 curve-defect theorem.

NO-GO POINT. A finite-dimensional Drinfeld--Jimbo representation `V` in CFG does not automatically define a perfect module for the CY3 `\PhiFA_3` or specialized `E_1` chiral algebra. That module must be constructed from the CY3 defect theory.

## Concrete algebraic presentations retained

CFG finite semisimple presentation:

```tex
A_0 = C^*(\g),\quad
F^p A_0 = Sym^{\ge p}(\g^\vee[-1]),\quad
A_0^! = C\otimes^L_{A_0}C \simeq (U\g)^\vee,
```

```tex
Perf_{A_0} \simeq Fin_{U\g}^{op},\qquad
Perf_{A_\hbar^\lambda} \simeq Rep^{dg}_{fin}(U_\hbar\g)
\quad(E_2\text{-monoidal}).
```

Vol III CY3 scoped presentation:

```tex
\Phi_3^{(\Sigma_2,C)}(\cC)
  = \SpCh_{\Sigma_2,C}(\PhiFA_3(\cC))
  = A_\cC^{(\Sigma_2,C)}
  \in E_1-ChirAlg(C),
```

```tex
B^{E_1}(A_\cC^{(\Sigma_2,C)}) \simeq CC_\bullet^{E_1}(\cC)
\quad\text{only on the constructed framed locus}.
```

CY3 chiralized filtered object before Stage-2 specialization:

```tex
\mathfrak L_X(P)
  =
\Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X),
\qquad
\Obs_X^q(P)
  =
C^*_{cont}(\mathfrak L_X(P)[1])
[[\epsilon_1,\epsilon_2,\epsilon_3]]_{\epsilon_1+\epsilon_2+\epsilon_3=0}.
```

```tex
B_{E_3}(U^{ch}_{E_3}(\mathfrak L_X))(P)
  \simeq
CE^{ch,Dolb}_*(\mathfrak L_X(P)),
```

with three OPE-residue differentials and three factorization coproducts from the polydisc directions `z_1,z_2,z_3`.

Braiding target:

```tex
Z(Rep^{E_1}(A_\cC)),\qquad
R(z)=\sigma_{V_u}(V_v).
```

Toric / Yangian structure-function check:

```tex
g(u)=\prod_{i=1}^3 {u-h_i\over u+h_i},\qquad
g^!(u)=g(u)^{-1},\qquad
h_1+h_2+h_3=0.
```

## Exact no-go list

1. CFG `C^*_\hbar(\g)` is not `\PhiFA_3(\Perf(X))`; it is only a locally constant / constant-mode associated model.
2. The CY3 filtered object is `C^*_{cont}(\Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X)[1])` with chiral factorization over polydiscs, not ordinary `C^*(\g)`.
3. CFG ordinary 3d topological CS is not six-real-dimensional holomorphic CS on a CY3.
4. CFG filtered Koszul duality uses finite semisimple `U\g` modules; quantum toroidal, Hall, BKM, and Fock modules require new completion and finiteness proofs.
5. CFG's `E_3` module category braiding is not the Vol III `d=3` braiding mechanism. Vol III braiding is through `Z(Rep^{E_1}(A_X))`.
6. CFG has no positive-half stage; Vol III toric CY3 does: `CoHA = Y^+`, with the full object only after double / center.
7. CFG does not construct `\Theta_{hCS\to Hall}`.
8. CFG line-defect RT traces do not automatically produce CY3 curve-defect invariants.
9. CFG's one-parameter CS deformation functor does not match the CY3 two-parameter Omega-background / Miki-triality deformation functor.

## Verification run

Commands run:

```bash
pytest -q compute/tests/test_chiral_koszul_derived.py::TestStructureFunctionInversion \
  compute/tests/test_chiral_koszul_derived.py::TestCFG25Hierarchy
```

Result:

```text
10 passed in 0.34s
```

Additional direct checks:

```bash
python3 - <<'PY'
from compute.lib.chiral_koszul_derived import verify_structure_function_inversion
print(verify_structure_function_inversion())
PY
```

returned `all_inversions_verified: True`.

```bash
python3 - <<'PY'
from compute.lib.qg_from_fh_3d_6d import verdict
print(verdict())
PY
```

returned the correct high-level verdict: CFG and the conjectural 6d hCS / quantum-toroidal construction share the logical pattern, but the implementation differs by holomorphic-vs-topological origin, parameter count, and Miki automorphism.

## Status recommendation

Keep CFG 2026 as `ProvedElsewhere` only for the ordinary 3d Chern--Simons statement:

```tex
filtered E_3 deformation of C^*(\g)
  -> perfect modules
  -> Drinfeld--Jimbo braided category
  -> RT link invariants.
```

For Vol III CY3, keep:

```tex
\Phi_3^{(\Sigma_2,C)}(\cC) \in E_1-ChirAlg(C)
```

conditional on the framed object-level hypotheses, with its Stage-1 filtered object represented locally by the Dolbeault chiral CE/enveloping factorization algebra

```tex
CE^{ch,Dolb}_*\!\left(\Omega^{0,*}(P,J^{hol}_{z_1,z_2,z_3}\mathfrak l_X)\right)
```

and not by bare `C^*(\g)`. Braiding is recovered through the Drinfeld center on constructed loci. The hCS-to-Hall comparison and quantum-toroidal / BKM module category remain separate conditional or conjectural obligations unless independently proved.
