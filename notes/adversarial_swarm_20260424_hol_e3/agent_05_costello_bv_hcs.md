# Agent 05: Costello/BV hCS adversarial report

Date: 2026-04-24.

Scope: BV holomorphic Chern-Simons, Costello-Li holomorphic twist, anomaly gate, quartic invariant polynomial, and quantum observables. This report reads the live working tree and proposes patches only. No chapter or compute file is edited here.

## Verification surface

Primary manuscript anchors:

- `chapters/theory/cy3_chain_level_bridge.tex:11`: hCS BV complex.
- `chapters/theory/cy3_chain_level_bridge.tex:25`: BV pairing, now explicitly degree `(-1)` with compact-support inputs.
- `chapters/theory/cy3_chain_level_bridge.tex:35`: local classical hCS functional.
- `chapters/theory/cy3_chain_level_bridge.tex:55`: many-variable Dolbeault-chiral CE model.
- `chapters/theory/cy3_chain_level_bridge.tex:293`: quartic, not cubic, anomaly slot.
- `chapters/theory/cy3_chain_level_bridge.tex:337`: open hCS-to-Hall comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:412`: left-end chain-level assembly.
- `chapters/theory/cy3_chain_level_bridge.tex:470`: Tradler-Menichi-Ginzburg BV layer.
- `chapters/theory/cy3_chain_level_bridge.tex:511`: `E_3` lift as Stage-1 data.
- `chapters/theory/cy3_chain_level_bridge.tex:578`: Stage-1 envelope through `Hol_{X,\Omega_X}`.
- `chapters/theory/cy_to_chiral.tex:226`: native hFA and `SpCh` definition.
- `chapters/theory/cy_to_chiral.tex:287`: three-step Stage-1 assembly.
- `chapters/theory/cy_to_chiral.tex:4896`: d=3 framed object-level scope.

Primary compute anchors:

- `compute/lib/holomorphic_cs_chiral_engine.py:1`: hCS-to-chiral engine scope.
- `compute/lib/holomorphic_cs_chiral_engine.py:88`: Omega-background CY condition.
- `compute/lib/holomorphic_cs_chiral_engine.py:147`: boundary algebra hierarchy.
- `compute/lib/holomorphic_cs_chiral_engine.py:298`: `E_n` structure verifier.
- `compute/lib/holomorphic_cs_chiral_engine.py:883`: class L/Yangian `E_3` bar model.
- `compute/lib/holomorphic_cs_chiral_engine.py:1480`: class C/betagamma quartic shadow model.
- `compute/lib/holomorphic_cs_chiral_engine.py:2301`: class M/Virasoro `d_4` quartic differential.

Tests run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_holomorphic_cs_chiral_engine.py \
  compute/tests/test_e3_bar_yangian.py
```

Result: `207 passed in 1.80s`.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_e3_bar_betagamma.py \
  compute/tests/test_e3_bar_virasoro_d4.py
```

Result: `359 passed in 2.23s`.

Direct witness values from the engine:

- At `OmegaBackground(1,-2)`: `(h_1,h_2,h_3)=(1,-2,1)`, `sigma_2=-3`, `sigma_3=-2`.
- `BoundaryAlgebra(3,omega)`: `Quantum Toroidal`, `E_3`, `kappa_ch=3`.
- `EnStructureVerifier`: `e1_associativity=True`, `e2_yang_baxter=True`, `e3_triple_compat=True`.
- `E3BarComplexYangian`: class `L`, shadow depth `3`, `phi_3=4`, Poincare `[1,3,3,1]`, total `8`, Euler `0`.
- `E3BarComplexBetaGamma`: class `C`, shadow depth `4`, `S_4=1`, `d_4` vanishes on the `E_3` page, Poincare `[1,6,15,20,15,6,1]`, total `64`.
- `E3BarSpectralSequenceVirasoro(c=1)`: class `M`, `S_4=10/27`, `d_4=40/27`, `E_inf=[0,3,3,0]`, total `6`.

## Cycle 1: field complex

ATTACK. The displayed global field complex
\[
\mathcal E_{\mathrm{hCS}}(X,\mathfrak g)=\Omega^{0,\bullet}(X,\mathfrak g)[1],
\qquad Q_{\mathrm{hCS}}=\bar\partial
\]
is correct as a formal global shorthand, but on non-compact charts and for local observables the BV pairing is only honest after a support/duality convention is fixed. The live tree partly heals this by using compact-support inputs in the pairing at `cy3_chain_level_bridge.tex:31`, while the named field complex at `:19-23` remains non-compact.

HEAL. Read the definition as two objects:
\[
\mathcal E_c(U)=\Omega_c^{0,\bullet}(U,\mathfrak g)[1],
\qquad
\mathcal E(U)=\Omega^{0,\bullet}(U,\mathfrak g)[1],
\]
paired by Serre duality. For compact `X`, the distinction may be suppressed; for `U \simeq C^3` it is load-bearing.

Patch suggestion. After `cy3_chain_level_bridge.tex:23`, add one sentence:

```tex
On an open chart \(U\) the local BV theory uses
\(\mathcal E_c(U)=\Omega_c^{0,\bullet}(U,\mathfrak g)[1]\) paired with
\(\mathcal E(U)=\Omega^{0,\bullet}(U,\mathfrak g)[1]\); when \(X\) is
compact the support subscript is suppressed.
```

Severity: moderate, because the open comparison problem itself requires the compact-support convention at `cy3_chain_level_bridge.tex:365-368`.

## Cycle 2: BV pairing

ATTACK. Before the current live edits, the BV pairing was implicit. The current tree now states
\[
(\alpha,\beta)_{\mathrm{hCS}}
=\int_X \Omega_X\wedge\langle\alpha,\beta\rangle,
\qquad
\alpha,\beta\in\Omega_c^{0,\bullet}(X,\mathfrak g)[1],
\]
and calls it degree `(-1)` at `cy3_chain_level_bridge.tex:25-34`. This is the right object. The remaining gap is that the inverse kernel defining the odd Poisson bracket is not normalized, so `\Obs^q` later depends on a hidden propagator convention.

HEAL. The pairing has degree `-1` because the Dolbeault pairing has total complex degree `3`, the CY form converts `(0,3)` to a scalar, and the two `[1]` shifts lower the cohomological degree by `2`. The induced BV bracket is the inverse of this pairing after choosing the Costello heat-kernel gauge fix.

Patch suggestion. Add a cross-reference from the pairing sentence to the quantum-observable definition proposed in Cycle 7:

```tex
The inverse kernel is fixed below by the Costello heat-kernel
regularisation used in the definition of \(\Obs_{\hCS}^{q}\).
```

Severity: minor after the live pairing insertion.

## Cycle 3: local functional and CME

ATTACK. The local functional
\[
I_{\mathrm{hCS}}(\alpha)=
\int_X\Omega_X\wedge
\left(
\frac12\langle\alpha,\bar\partial\alpha\rangle+
\frac16\langle\alpha,[\alpha,\alpha]\rangle
\right)
\]
at `cy3_chain_level_bridge.tex:35-45` is the standard superfield expression, but the coefficient `1/6` is convention-dependent. Without the variation formula, a reader cannot check whether the bracket convention is the graded Lie bracket or the wedge-Lie bracket with a hidden factor of `2`.

HEAL. With
\[
[\alpha,\beta]=\alpha\wedge\beta\otimes[x,y]_{\mathfrak g}
\]
and the invariant metric on `g`, the displayed normalization is correct if the Euler-Lagrange equation is
\[
\delta I_{\mathrm{hCS}}(\alpha)
=\int_X\Omega_X\wedge
\left\langle \delta\alpha,\,
\bar\partial\alpha+\frac12[\alpha,\alpha]\right\rangle.
\]
The classical master equation then follows from `\bar\partial^2=0`, invariance of `\langle-,-\rangle`, and Jacobi:
\[
\{I_{\mathrm{hCS}},I_{\mathrm{hCS}}\}_{\mathrm{BV}}=0.
\]

Patch suggestion. After `cy3_chain_level_bridge.tex:48`, add the variation equation and one sentence naming the bracket convention.

Severity: moderate; the formula is likely right, but the convention should be pinned before the anomaly gate.

## Cycle 4: anomaly gate

ATTACK. Proposition `prop:cy3-hcs-quartic-anomaly-slot` correctly says the complex-threefold anomaly lands in the degree-4 invariant-polynomial slot (`cy3_chain_level_bridge.tex:293-301`). The proof at `:304-311` is too compressed: "the wheel anomaly has d+1 Lie-algebra inputs" is the conclusion, not the cohomological mechanism.

HEAL. The Costello-Li local Lie-algebra cohomology statement should be named in the proof. In complex dimension `d`, the one-loop obstruction class is represented by an invariant polynomial
\[
P_{d+1}\in\mathrm{Sym}^{d+1}(\mathfrak g^\vee)^{\mathfrak g}
\]
through a local cocycle of the schematic form
\[
\Theta_{P_{d+1}}(\alpha_0,\ldots,\alpha_d)
=
\int_X\Omega_X\wedge
P_{d+1}(\alpha_0,\partial\alpha_1,\ldots,\partial\alpha_d),
\]
with Dolbeault heat-kernel regularisation supplying the local functional. For `d=3`, this is the quartic slot
\[
P_4\in\mathrm{Sym}^4(\mathfrak g^\vee)^{\mathfrak g}.
\]

Patch suggestion. Replace the proof at `cy3_chain_level_bridge.tex:304-311` by a proof explicitly invoking Costello-Li local Lie-algebra cohomology and the map `P_{d+1} -> Theta_{P_{d+1}}`; keep the final sentence excluding the `d=2` cubic slot.

Severity: high, because this is the gate that decides whether quantum observables exist.

## Cycle 5: quartic invariant polynomial versus quartic shadow

ATTACK. The manuscript and engine both use "quartic" in two adjacent but different senses:

- hCS anomaly gate: quartic invariant polynomial `P_4` on `g`, `cy3_chain_level_bridge.tex:293-301`.
- shadow tower: quartic shadow `S_4` and `d_4` in the `E_3` bar spectral sequence, `holomorphic_cs_chiral_engine.py:1480-1874` and `:2301-2610`.

These are not automatically the same invariant. The tests verify the bar-shadow behavior, not the Costello-Li gauge-anomaly class.

HEAL. Keep the following separation:

- Gauge anomaly cancellation: `P_4^{\mathrm{gauge}}+P_4^{\mathrm{matter}}=0` in `Sym^4(g^*)^g`.
- Class C shadow: `S_4 != 0`, but `d_4=0` on the `E_3` page by charge conservation. Engine witness: betagamma has `S_4=1`, Poincare `[1,6,15,20,15,6,1]`, total `64`.
- Class M shadow: `S_4=10/27`, `d_4=8*kappa_ch*S_4=40/27`, so `[1,3,3,1]` becomes `[0,3,3,0]`. Engine witness: `holomorphic_cs_chiral_engine.py:2511-2525` and `:2596-2610`.

Patch suggestion. Add a warning near the anomaly proposition:

```tex
The quartic Costello--Li anomaly polynomial \(P_4\in\mathrm{Sym}^4(\mathfrak g^\vee)^{\mathfrak g}\)
is not the same datum as the shadow coefficient \(S_4\) in the
\(E_3\)-bar spectral sequence; comparisons between them require an
explicit BV-to-bar transfer map.
```

Severity: high. This prevents a false proof that the shadow `S_4` test cancels the hCS anomaly.

## Cycle 6: Costello-Li holomorphic twist and the Stage-1 envelope

ATTACK. The live tree has already repaired the largest issue: `cy3_chain_level_bridge.tex:511-530` now says the `E_3` lift is extra Stage-1 data, not a consequence of BV alone. The theorem statement at `:590-608` also now uses
\[
\PhiFA_3(\mathcal C)_F\simeq
\mathrm{Hol}_{X,\Omega_X}\left(\mathcal U^{\mathrm{FA}}(\HH^\bullet(\mathcal C)_F)\right).
\]
Two residual inconsistencies remain:

1. The proof at `cy3_chain_level_bridge.tex:619-624` still says the `E_3` structure is "composed of the unframed E_2 from braces and the framed E_2 \otimes_Dunn E_1 = E_3 from the BV operator." This contradicts the new proposition at `:511-530`.
2. The proof at `:629-634` says the topological factorisation algebra is on `R^6`, while the definition at `:551-575` constructs `U^FA(A)` on `R^3`.

HEAL. The correct reading is:

- `\mathcal U^{FA}` is the topological envelope of the chosen `E_3` algebra on real `R^3`.
- `\mathrm{Hol}_{X,\Omega_X}` is not a naive functor from `FAct(R^6)` applied to the same object; it is the Costello-Li Dolbeault refinement that replaces local constants by the Dolbeault-chiral CE model:
\[
\mathrm{Hol}_{X,\Omega_X}(\mathcal U^{FA}(A))|_P
\simeq
C^\bullet_{\mathrm{Lie,cont}}
\left(
\Omega_c^{0,\bullet}
\left(P,J^\infty_{\mathrm{hol}}\mathfrak l_{\mathcal C}\right)[1],
\mathbb C
\right).
\]

Patch suggestions:

1. Replace `cy3_chain_level_bridge.tex:619-624` with: "Propositions ... supply the framed `E_2`/`BV_\infty` layer; Proposition ... supplies the additional chosen `E_3` lift."
2. Replace `cy3_chain_level_bridge.tex:629-634` with: "`Hol_{X,\Omega_X}` is the Dolbeault refinement of the `R^3` topological envelope whose local normal form is Definition `def:cy3-many-variable-chiral-ce`; no separate `R^6` locally constant envelope is asserted."

Severity: high, because the current proof body partly reintroduces the false Dunn/BV shortcut that the new proposition correctly blocks.

## Cycle 7: quantum observables

ATTACK. `\Obs_{\hCS}^q(X,\mathfrak g)` is named at `cy3_chain_level_bridge.tex:49-52` only "when the local anomaly is cancelled." The open comparison problem then requires anomaly cancellation, completion, and compact-support convention at `:365-368`. There is still no local definition of `\Obs^q` by scale-dependent effective interactions and the QME.

HEAL. Add the Costello-Gwilliam definition at the level needed by this chapter:
\[
\Obs_{\hCS}^{q}(U,\mathfrak g)
=
\left(
\mathcal O(\mathcal E_c(U))[[\hbar]],
Q+\{I[L],-\}_{\mathrm{BV}}+\hbar\Delta_L
\right),
\]
where `I[L]` is the renormalised effective interaction at scale `L`, `\Delta_L` is the BV Laplacian defined by the heat kernel, and the QME is
\[
Q I[L]+\frac12\{I[L],I[L]\}_{\mathrm{BV}}+\hbar\Delta_L I[L]=0.
\]
The factorisation product is induced by disjoint support. In the abelian flat `C^3` branch, `notes/wave13_g2_costello_EFT_hCS.tex:64-80` and `:137-171` give a local model: pure quadratic action, vanishing cubic vertex for `g=C`, QME, and quantum observables as the free holomorphic boson/Fock factorisation algebra.

Patch suggestion. Add a definition immediately after the existing hCS BV complex definition, or add a short "Quantum observables" definition before the anomaly gate. It must include the scale `L`, QME, support convention, and anomaly-cancellation hypothesis.

Severity: high, because the comparison map
\[
\Theta_{\mathrm{hCS}\to\mathrm{Hall}}^{\mathrm{or}}:
\Obs_{\hCS}^q(-,\mathfrak g)\to\CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
\]
cannot be formulated proof-grade without the source factorisation algebra.

## Engine audit

The compute engine is a useful oracle for Omega-background, boundary specialisation, and `E_3` bar spectral-sequence numerics. It is not a BV hCS field-complex implementation.

Verified by tests:

- CY condition and structure function: `test_holomorphic_cs_chiral_engine.py:58-120`.
- Boundary hierarchy and `E_n` checks: `test_holomorphic_cs_chiral_engine.py:126-260`.
- Pipeline and `kappa_ch` preservation: `test_holomorphic_cs_chiral_engine.py:334-397`.
- Class L/Yangian `E_3` bar: `test_e3_bar_yangian.py:68-280`.
- Class C/betagamma quartic shadow: `test_e3_bar_betagamma.py:79-129`.
- Class M/Virasoro nonzero `d_4`: `test_e3_bar_virasoro_d4.py:73-240`.

Residual engine patch suggestion. The docstring at `holomorphic_cs_chiral_engine.py:3-28` should say that `dim=3 -> Quantum Toroidal` is a boundary/specialisation/completion model. Before Drinfeld double or completion, the manuscript's typed bridge keeps
\[
\CoHA(\mathbb C^3)=Y^+
\]
as the positive half, with the `W_{1+\infty}` comparison only after the double and Fock/evaluation passage. This avoids using the engine as evidence for a direct hCS-to-quantum-toroidal theorem.

## Final status

CONVERGED for this agent note: seven ATTACK->HEAL cycles completed, target tests passed, and the remaining obligations are patch suggestions rather than silent contradictions.

Highest-priority manuscript patches:

1. Strengthen the anomaly-gate proof with the Costello-Li local Lie-algebra cohomology class `P_4`.
2. Add the explicit quantum-observable/QME definition of `\Obs_{\hCS}^q`.
3. Remove the residual Dunn/BV shortcut in the proof of the Stage-1 envelope.
4. Normalize `Hol_{X,\Omega_X}` as the Dolbeault refinement of the `R^3` envelope, not as a naive `R^6` locally constant envelope.
5. Add the warning separating Costello-Li quartic anomaly polynomials from shadow `S_4` coefficients.
