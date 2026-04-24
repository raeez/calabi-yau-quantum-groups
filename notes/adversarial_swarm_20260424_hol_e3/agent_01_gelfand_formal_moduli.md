# Agent 01 -- Gelfand/Formal-Moduli

Scope: chain-level construction of the holomorphic `E_3` algebra, chiral deformation theory, Maurer--Cartan control, shifted chiral Hochschild/CE dgLa, and chiral Gerstenhaber brackets.

## Sources read

- `CLAUDE.md` lines 1--502.
- `AGENTS.md` local opening doctrine; user supplied full current instruction block.
- `.agents/skills/vol3-beilinson-loop/SKILL.md`.
- `.agents/skills/vol3-claim-verification/SKILL.md`.
- `chapters/theory/cy3_chain_level_bridge.tex` lines 1--678.
- `chapters/theory/cy_to_chiral.tex` relevant anchors:
  - `thm:phi-two-stage-factorisation-headline`, lines 4--44.
  - `prop:ptvv-shift-law`, lines 46--60.
  - `thm:cya3-existence-rigidity`, lines 62--89.
  - `rem:phi-d-chain-vs-inf1-functor`, lines 91--99.
  - two-stage frame, lines 147--212.
  - `def:phi-fa-and-sp`, lines 225--244.
  - `thm:phi-two-stage-factorisation`, lines 246--276.
  - `prop:native-en-level`, lines 278--285.
  - `prop:phi-fa-three-step-assembly`, lines 287--300.
  - `rem:three-step-slippage-precise`, lines 303--305.
  - `subsubsec:kt-e3-formality-grt1-torsor-cfg2026`, lines 309--414.
  - `rem:e2-on-drinfeld-centre`, lines 437--444.
  - derived-rigour definitions, lines 468--545.
  - `subsec:derived-stack-chiral`, lines 5881--5961.
- `compute/lib/chiral_ce_e3_deformation.py` lines 1--1244.
- `compute/tests/test_chiral_ce_e3_deformation.py` lines 1--833.
- Dependency inspection in `compute/lib/chiral_ce_complex.py` lines 1--220, 220--370, 390--590, 626--1010.
- Related comparison surface in `compute/lib/e3_hochschild_deformation.py` lines 430--560.

## Computational checks

- `pytest -q compute/tests/test_chiral_ce_e3_deformation.py`: `81 passed in 0.83s`.
- Direct `python3` probe of the same objects:
  - Heisenberg: `dim=1`, `tangent=1`, `obstruction=0`, `mc_desc=point ... vdim = 1`, `d_h_squared_zero=True`, coefficients `{2: 1/2}`.
  - Yangian truncation: `dim=3`, `tangent=3`, `obstruction=3`, `mc_desc=smooth of dimension 3 ... vdim = 0`, `d_h_squared_zero=True`, coefficients `{2: 1}`.
  - Virasoro LCA truncation: `dim=1`, `tangent=1`, `obstruction=0`, `mc_desc=singular ...`, coefficients `{2: 1/2, 3: 2, 4: 10/27}`.
  - `CEElement.basis((0,0,0)) = 0` and Virasoro `_d3` on that exterior encoding is `0`.
  - `LieConformalAlgebra.is_abelian` returns `False` for Heisenberg and `True` for the nonabelian Yangian truncation, so the property is semantically inverted in the dependency.

## Surviving core

The manuscript core in `cy3_chain_level_bridge.tex` is typed correctly. The hCS BV complex is defined as a Dolbeault field complex with action and anomaly gate (`def:cy3-hcs-bv-complex`, lines 11--43; `prop:cy3-hcs-quartic-anomaly-slot`, lines 280--299). The CY3 local observable model is not ordinary `C^\bullet(\mathfrak g)` but the many-variable Dolbeault--chiral CE factorisation algebra over holomorphic jets (`def:cy3-many-variable-chiral-ce`, lines 45--117). The typed bridge keeps `CoHA(\C^3)=Y^+` before Drinfeld doubling (`con:cy3-typed-bridge`, lines 119--142; `prop:cy3-c3-bridge-core`, lines 210--239). The hCS-to-Hall arrow remains open and is stated as an oriented factorisation-cosheaf comparison problem (`op:cy3-hcs-hall-comparison`, lines 324--372).

The Stage-1 envelope theorem is the strongest usable positive statement: after fixing the formality/associator datum and the verified Stage-1 locus, `\PhiFA_3(\cC)` factors through Hochschild cochains with a chain-level `E_3` structure, the topological factorisation envelope, and the Costello--Li holomorphic twist (`thm:cfg-factorization-envelope-stage-one`, lines 547--609). Its own scope restriction is correct: object level only, anomaly-gated, and not a CoHA comparison (`rem:cfg-envelope-scope`, lines 650--678).

The compute file is useful as a finite shadow oracle for toy CE dimensions, Omega-parameter arithmetic, and recorded shadow coefficients. It is not yet a first-principles formal-moduli engine for the holomorphic `E_3` factorisation algebra or for the specialised `E_1` chiral algebra.

## ATTACK->HEAL cycles

### 1. Attack: the object carrying `E_3` is not the final chiral algebra

Claim attacked: `CE^{ch}_*(L)` can be treated as the `E_3`-chiral deformation object of the CY3 output.

Failure mode: `cy_to_chiral.tex` says Stage 1 lands in `\EdHolFA(X)` and Stage 2 lands in `E_{n(d)}` chiral algebras with `n(d)=1` for `d >= 3` (`thm:phi-two-stage-factorisation-headline`, lines 7--20). The same chapter says the framed CY3 assignment is `\Phi_3^{(\Sigma_2,C)}(\cC) in \Eone-ChirAlg(C)` (`cy_to_chiral.tex`, lines 153--160), and `prop:native-en-level` fixes `E_1` for `d >= 3` (`cy_to_chiral.tex`, lines 278--285). The `E_3` datum lives natively on `\PhiFA_3(\cC)` before specialisation, not on the final curve algebra. `rem:e2-on-drinfeld-centre` also forbids promoting the output algebra itself beyond `E_1` (`cy_to_chiral.tex`, lines 437--444).

Heal: split all statements into two deformation functors.

Proposed text:

```tex
\begin{proposition}[Two deformation complexes at CY$_3$]
Fix a CY$_3$ category $\cC$, a formality point $F\in\mathrm{Form}_3(\mathbb Q)$, a CY form $\Omega_X$, and an admissible specialisation datum $(\Sigma_2,C)$ on the verified Stage-$1$ locus. The native object
\[
  \PhiFA_3(\cC)_F\in E_3\text{-}\mathrm{HolFA}(X)
\]
has a holomorphic $E_3$ deformation complex. Its specialised chiral shadow
\[
  A_{\Sigma_2,C}:=\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC)_F)
  \in E_1\text{-}\mathrm{ChirAlg}(C)
\]
has a separate $E_1$ chiral Hochschild deformation complex. The second is obtained from the first only after applying the specialisation kernel; it is not the same formal moduli problem.
\end{proposition}
```

Patch suggestion: in `compute/lib/chiral_ce_e3_deformation.py`, rename the advertised object from "E_3-chiral deformation of CE" to "finite CE shadow of the native `E_3` deformation", or add a `stage` field with values `native_E3_hFA` and `specialized_E1_chiral`.

Status: healed at statement level; code remains over-advertised.

### 2. Attack: finite exterior CE cochains do not control the full formal moduli problem

Claim attacked: `MC(CE^{ch,*}(L)[1])` with dimensions `binom(n,k)` is the formal moduli problem of chiral deformations.

Failure mode: `cy3_chain_level_bridge.tex` defines the local CY3 model as
`\Omega^{0,\bullet}_c(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]` and continuous chiral CE over compactly supported Dolbeault jets (`def:cy3-many-variable-chiral-ce`, lines 45--75). The ordinary finite CE object appears only after the locally constant shadow (`cy3_chain_level_bridge.tex`, lines 101--116). In contrast, `DerivedCenterCE` only returns `math.comb(n,k)` (`compute/lib/chiral_ce_complex.py`, lines 969--1003), and `ChiralMCDeformation` uses these dimensions for tangent and obstruction (`compute/lib/chiral_ce_e3_deformation.py`, lines 691--715). This omits holomorphic jets, lambda powers, compact supports, continuous duals, coefficients, and completions.

Heal: the controlling dgLa must be completed and model-qualified.

Proposed text:

```tex
\begin{definition}[Completed chiral deformation dgLa]
Let $P\subset X$ be a holomorphic polydisc and let
\[
  \mathfrak L_\cC(P)=
  \Omega^{0,\bullet}_c(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1].
\]
The local formal moduli problem of the CY$_3$ chiral CE model is controlled by the filtered continuous dgLa
\[
  \Def_{\mathrm{CE}}^{\mathrm{ch,cont}}(P)
  :=
  C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\mathfrak L_\cC(P),\mathfrak L_\cC(P)\bigr)[s],
\]
where the shift $s$ is the one making the chiral Gerstenhaber bracket degree zero. The filtration is the joint arity, jet, charge/HN, and $\hbar$-adic filtration. Maurer--Cartan elements over an Artin cdga $R$ lie in
\[
  F^1\Def_{\mathrm{CE}}^{\mathrm{ch,cont}}(P)^1\widehat\otimes\mathfrak m_R.
\]
The finite exterior complex $\Hom(\Lambda^\bullet L,\mathbb C)$ is only the locally constant associated graded shadow.
\end{definition}
```

Patch suggestion: introduce a `ComplexModel` enum in compute:
`FINITE_EXTERIOR_CE`, `ORDERED_BAR`, `DOLBEAULT_JET_CHIRAL_CE`. Disallow "formal moduli proved" output unless the model is at least `ORDERED_BAR` and the filtration is present.

Status: current theorem can be made correct with this model qualifier.

### 3. Attack: the Maurer--Cartan dimensions contradict the claimed moduli spaces

Claim attacked: Heisenberg MC space is a point, Yangian MC is smooth by BTT, and Virasoro MC is singular, as computed by the current engine.

Failure mode:

- Heisenberg: the engine reports tangent dimension `1` and obstruction dimension `0`, but also `MC = {0}` and `vdim = 1` (`compute/lib/chiral_ce_e3_deformation.py`, lines 691--750; tests lines 511--519). For an abelian controlling dgLa with nonzero degree-1 tangent and zero bracket, the pointed formal moduli functor is formally affine unless the deformation problem fixes the bracket/level and discards tangent directions by definition.
- Yangian: the engine reports `CE^2 = 3` and then asserts obstructions are "killed by Jacobi" and "BTT unobstructedness" (`compute/lib/chiral_ce_e3_deformation.py`, lines 727--743; tests lines 520--528). BTT is a theorem for complex-structure deformations of Calabi--Yau varieties, not a theorem for arbitrary Lie conformal or Yangian-truncation deformations.
- Virasoro: the LCA truncation has one generator, so `CE^2=0` (`compute/lib/chiral_ce_e3_deformation.py`, lines 703--715), yet the engine asserts singularity from an infinite tower. The singularity is not seen by the exterior CE computation.

Heal: state three different deformation problems.

Patch suggestion:

1. `fixed_lca`: deformations of nothing but the fixed bracket; Heisenberg is a point by definition.
2. `central_extension_or_pairing`: Heisenberg level/pairing deforms; tangent is nonzero.
3. `full_vertex_ordered_bar`: Virasoro class M obstructions appear in the ordered bar / vertex algebra, not in the exterior CE quotient.

Proposed replacement for the current MC paragraph:

```tex
The phrase "the Maurer--Cartan moduli" is model-dependent. For the fixed Lie conformal algebra $L$, the deformation functor fixes the $\lambda$-bracket and can be a point. For deformations of the chiral algebra structure on the underlying graded vector space, the controlling object is the shifted chiral Hochschild complex with coefficients, and its tangent is not computed by $\dim\Hom(\Lambda^1 L,\mathbb C)$ alone. For class $\mathbf M$, the obstruction classes live on the ordered bar/vertex model; the exterior CE quotient does not detect repeated inputs such as $T,T,T$.
```

Status: current compute output is internally diagnostic but not a proof.

### 4. Attack: class M higher brackets are recorded but not acted on

Claim attacked: the current `LInfinityCEComplex` computes the class M `l_3,l_4,...` differential corrections.

Failure mode: the dependency file itself states the obstruction. `CEElement.basis` kills repeated indices in the exterior algebra (`compute/lib/chiral_ce_complex.py`, lines 401--407). The `_d3` implementation says the shadow tower lives on the ordered tensor coalgebra, not in the exterior algebra (`compute/lib/chiral_ce_complex.py`, lines 853--870), but still returns an exterior CE element. The direct check gives `CEElement.basis((0,0,0)) = 0` and Virasoro `_d3(...) = 0`, while `deformation_coefficients()` still returns `{2: 1/2, 3: 2, 4: 10/27}` from coefficient lookup (`compute/lib/chiral_ce_complex.py`, lines 936--955).

Heal: class M must be moved to an ordered bar complex, or the current engine must be labelled as coefficient registry only.

Patch suggestion:

- Add an `OrderedBarElement` allowing repeated generator labels and arity words.
- Implement `d_3(T|T|T) = -2T` and `d_4(T|T|T|T) = (40/27)T` on the ordered bar side.
- Add tests that apply `_d3` and `_d4` to nonzero ordered words and then verify the `L_\infty` identities through the claimed order.
- Keep the exterior CE engine only for strict Lie conformal algebras and locally constant shadows.

Status: fatal for any first-principles class M claim based on the current exterior CE code; heal is straightforward but not implemented here.

### 5. Attack: the Omega-deformed differential is not coherently defined

Claim attacked: the CY condition `h_1+h_2+h_3=0` alone gives the deformed differential and `d_h^2=0`.

Failure mode: `compute/lib/chiral_ce_e3_deformation.py` gives three incompatible descriptions:

- module docstring: `d_h = d_CE + h_1*d_1 + h_2*d_2 + h_3*d_3`, and the CY condition ensures `d_h^2=0` (lines 24--27);
- `E3ChiralCEDeformation`: for diagonal embedding the equivariant correction vanishes, so `d_h=d_CE` on arity 1 and 2 (lines 314--335);
- `QuantumCEDeformation`: "d_h = d_1 + d_2 + d_3 (not the sum h_i*d_i)" (lines 433--439).

The test suite verifies only selected consequences: arithmetic for `h_1+h_2+h_3=0`, `\sigma_2=-3`, `\sigma_3=-2`, and `d_h_squared_zero()` on the finite examples (`compute/tests/test_chiral_ce_e3_deformation.py`, lines 74--178). It does not verify pairwise anticommutation of the three differentials or an MC equation for the Omega deformation.

Heal: define the tricomplex first.

Proposed text:

```tex
\begin{definition}[Omega tricomplex]
An Omega-deformed CY$_3$ chiral CE model is a filtered complex
\[
  (C,d_{\mathrm{CE}},\partial_1,\partial_2,\partial_3)
\]
with
\[
  d_{\mathrm{CE}}^2=0,\qquad
  [d_{\mathrm{CE}},\partial_i]=0,\qquad
  [\partial_i,\partial_j]=0
\]
in the completed endomorphism dgLa. For weights $h_1+h_2+h_3=0$,
\[
  d_{\Omega}=d_{\mathrm{CE}}+\sum_i h_i\partial_i
\]
is a differential only because these commutators vanish. In the diagonal Heisenberg shadow, the weighted correction vanishes by the weight identity; this is a special case, not the definition.
\end{definition}
```

Patch suggestion: replace string-level `d_h_squared_zero()` tests with tests of the three commutators and the weighted differential on representative generators.

Status: arithmetic checks survive; first-principles derivability does not yet.

### 6. Attack: the chiral Gerstenhaber bracket is not implemented

Claim attacked: the code verifies the shifted chiral Hochschild/CE dgLa bracket.

Failure mode: the CE differential uses only the zero-th product of the lambda bracket (`compute/lib/chiral_ce_complex.py`, lines 223--234 and 546--548). Central and higher lambda terms are either discarded for the Lie bracket or treated as arity-lowering scalars in the finite CE complex (`compute/lib/chiral_ce_complex.py`, lines 549--554). `DerivedCenterCE` has dimensions but no differential, no cochain bracket, and no chiral Hochschild insertions (`compute/lib/chiral_ce_complex.py`, lines 969--1003). The manuscript's derived stack model uses `L_V=\mathrm{CHoch}^*(V,V)[1]` with Gerstenhaber bracket (`cy_to_chiral.tex`, lines 5883--5895), which is a different object.

Heal: implement or explicitly cite a chiral Hochschild bracket model.

Patch suggestion:

- Add `ChiralHochschildCochain` with inputs, lambda powers, translation covariance, and residue convention.
- Implement the insertion/pre-Lie product and commutator bracket.
- Test skew-symmetry, Jacobi, and `d\mu + 1/2[\mu,\mu]=0` for Heisenberg and one nonabelian strict example.
- Add a comparison map from the finite CE shadow to the chiral Hochschild model and test that it is a shadow map, not an equality.

Status: no current first-principles bracket witness.

### 7. Attack: small code inconsistencies lower the evidential value of the tests

Claim attacked: the passing test file gives robust evidence for the stated formal-moduli claims.

Failure mode:

- `LieConformalAlgebra.is_abelian` returns `True` when a nonzero zero-th product exists and `False` otherwise (`compute/lib/chiral_ce_complex.py`, lines 237--243). Direct probe: Heisenberg gives `False`; Yangian and Virasoro truncations give `True`.
- A test docstring says `\sigma_2=-5` at `(1,-2,1)` but the test and arithmetic correctly assert `-3` (`compute/tests/test_chiral_ce_e3_deformation.py`, lines 84--90).
- The module comments include one line where the cubic invariant is named with an unsubscripted invariant symbol (`compute/lib/chiral_ce_e3_deformation.py`, line 108), violating the repo's invariant-subscript discipline.

Heal: these are local compute-file patchlets, not manuscript changes.

Patch suggestion:

- Fix `is_abelian` to return `False` on a detected nonzero bracket and `True` after the scan.
- Correct the `\sigma_2` docstring to `-3`.
- Replace the unsubscripted invariant mention by `\sigma_3` or a specific subscripted invariant, depending on the intended mathematical object.

Status: low mathematical severity individually; high value as a hygiene patch before relying on this engine in a theorem.

## Proposed theorem/proposition surface

The following is the strongest statement I would inscribe after the above heals, with the proof obligations explicit.

```tex
\begin{proposition}[Formal moduli of the CY$_3$ Stage-$1$ chiral CE model]
Let $\cC$ be a smooth proper cyclic $\Ainf$ category of CY dimension $3$ on the verified Stage-$1$ locus of Theorem~\ref{thm:cfg-factorization-envelope-stage-one}. Fix a formality point $F\in\mathrm{Form}_3(\mathbb Q)$, a CY form $\Omega_X$, and a holomorphic polydisc $P\subset X$. Let
\[
  \mathfrak L_\cC(P)=
  \Omega^{0,\bullet}_c(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1].
\]
Then infinitesimal deformations of the local Dolbeault--chiral CE factorisation algebra with fixed underlying polydisc, fixed CY form, and fixed formality point are governed by the completed continuous deformation dgLa
\[
  \Def^{\mathrm{ch,cont}}_{\cC,P}
  =
  C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\mathfrak L_\cC(P),\mathfrak L_\cC(P)\bigr)[s],
\]
with the shift $s$ chosen so that the chiral Gerstenhaber bracket has degree zero. For an Artin cdga $R$, deformations over $R$ are Maurer--Cartan elements in
\[
  F^1\Def^{\mathrm{ch,cont}}_{\cC,P}\widehat\otimes\mathfrak m_R.
\]
If the local model is strict and locally constant, this reduces to the ordinary CE shadow; otherwise the ordered bar and Dolbeault-jet terms are essential.
\end{proposition}
```

```tex
\begin{proposition}[Specialisation changes the deformation problem]
Let $A_{\Sigma_2,C}=\SpCh_{\Sigma_2,C}(\PhiFA_3(\cC)_F)$. The formal moduli problem of $A_{\Sigma_2,C}$ as an $E_1$ chiral algebra on $C$ is controlled by the shifted chiral Hochschild complex
\[
  \CHoch^\bullet_{\mathrm{ch},E_1}(A_{\Sigma_2,C},A_{\Sigma_2,C})[1],
\]
not by the native $E_3$ deformation complex before specialisation. The comparison map from the native complex to the specialised complex is induced by the factorisation-homology kernel for $(\Sigma_2,C)$ and is an extra datum.
\end{proposition}
```

## Open obligations

1. Construct the completed continuous dgLa with an explicit filtration: arity, holomorphic-jet order, charge/HN, and `\hbar`-adic order.
2. Implement or cite the chiral Gerstenhaber bracket on `\CHoch^\bullet_{\mathrm{ch}}`, including lambda-mode and residue conventions.
3. Build an ordered-bar compute witness for class M so repeated inputs survive and `l_3,l_4` act nontrivially.
4. Replace Yangian "BTT unobstructedness" with an actual `H^2` obstruction computation in the relevant chiral Hochschild/CE complex, or mark it as conjectural in the compute report.
5. Prove the comparison from the native `E_3` deformation complex to the specialised `E_1` chiral Hochschild complex through the `\SpCh_{\Sigma_2,C}` kernel.
6. Test `d_\Omega^2=0` by commutators of the tricomplex differentials, not by class labels or string descriptions.
7. Keep `\Theta_{\hCS\to\Hall}` separate: no formal-moduli repair here proves the hCS-to-Hall comparison of `op:cy3-hcs-hall-comparison`.

## Claim-status recommendation

- Manuscript Stage-1 left end: proved/conditional exactly as currently scoped in `thm:cfg-factorization-envelope-stage-one`.
- Full hCS-to-Hall bridge: open, anchored by `op:cy3-hcs-hall-comparison`.
- Compute engine `chiral_ce_e3_deformation.py`: computed finite CE shadow plus coefficient registry; not a proof of formal moduli, not a proof of chiral Gerstenhaber control, and not a proof of class M all-order MC.
- Proposed formal-moduli propositions: ready as conditional propositions after the dgLa model, bracket convention, ordered-bar witness, and filtration are supplied.
