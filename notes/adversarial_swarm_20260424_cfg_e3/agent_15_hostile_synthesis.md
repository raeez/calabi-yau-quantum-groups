# Agent 15: Hostile Synthesis and Convergence

Date: 2026-04-24.

Ownership: this report only. Manuscript files were not edited.

Scope: hostile synthesis of the CY3/CFG/E3 adversarial reports in
`notes/adversarial_swarm_20260424_cfg_e3`, with local anchors in
`chapters/theory/cy3_chain_level_bridge.tex` and
`chapters/theory/cy_to_chiral.tex`.

## Executive Verdict

The swarm converges.

CFG 2026 proves a theorem for ordinary real 3-dimensional
Chern-Simons: BV quantization gives a locally constant filtered
`E_3` factorization algebra whose classical local model is
`C^*(\mathfrak g)`, with perfect modules producing RT traces by
factorization homology. This is a theorem-grade topological CS
template.

It is not the Vol III CY3 object. The CY3 object is the
Dolbeault/holomorphic many-variable `E_3` factorization algebra:
on a holomorphic polydisc `P = D_1 x D_2 x D_3`,
```tex
\mathfrak L_{\hCS}(P)
  = \Omega_c^{0,\bullet}(P,\mathfrak g)[1],
\qquad
\Obs_{\hCS}^{cl}(P)
  =
C^\bullet_{\Lie,cont}(\mathfrak L_{\hCS}(P),\mathbb C),
```
and, where the hCS realization is available,
```tex
\PhiFA_3(\mathcal C)|_P
  \simeq
U^{fact,E_3}_{P}(J^\infty_{hol}\mathfrak L_{\hCS}),
\qquad
B_{E_3}(\PhiFA_3(\mathcal C)|_P)
  \simeq
CE^{ch,E_3}_*(J^\infty_{hol}\mathfrak L_{\hCS}).
```
The ordinary `C^*(\mathfrak g)` is obtained only after the locally
constant shadow
```tex
\Omega^{0,\bullet}(P)\simeq \mathbb C,
\qquad
J^\infty_{hol}\mathfrak L_{\hCS}\rightsquigarrow \mathfrak g.
```

The final CY3 specialization is not native `E_3` and not native `E_2`:
```tex
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
  =
\left(\int_{\Sigma_2}\PhiFA_3(\mathcal C)\right)|_C
  \in E_1\text{-ChirAlg}(C).
```
The nonsymmetric quantum-group braiding, where constructed, is recovered
on `\mathcal Z(\Rep^{E_1}(A_\mathcal C))`, not on `A_\mathcal C`
itself.

The hCS-to-Hall comparison is the first missing lemma:
```tex
\Theta_{\hCS\to\Hall}^{or}\colon
\Obs_{\hCS}^q(-,\mathfrak g)
\longrightarrow
\CoHA_{\crit}^{or}(-).
```
It must preserve Dolbeault locality, Weiss descent, CY3 BV/Hall product
compatibility, the `\mathbb C^3` positive-half model, Drinfeld doubling,
orientation square roots, overlap cocycles, and Thom-Sebastiani
products. CFG supplies none of these data.

## Reports Read

| Agent | Synthesis |
|---|---|
| 01 formal moduli | Killed `C^*(\mathfrak g)` as the CY3 object; retained Dolbeault continuous CE with holomorphic jets. |
| 02 E3 operads | Split Stage 1 `E_3` from final `E_1`; CFG is ordinary locally constant CS only. |
| 03 filtered Koszul | CFG filtered Koszul duality is finite/ordinary CS; Hall, BKM, quantum-toroidal modules need new completions. |
| 04 Ran descent | `\SpCh_{\Sigma_2,C}` needs holomorphic pushforward/Weiss-Ran exactness; CFG torus pushforward is only grammar. |
| 05 BV-hCS | hCS fields are `\Omega^{0,*}(X,\mathfrak g)[1]`; quartic anomaly and hCS-to-Hall remain gates. |
| 06 factorization homology | CFG trace formalism is a test oracle, not a construction of CY3 traces or K3 x E outputs. |
| 07 Feynman compute | Tests strongly support `E_1`/Dolbeault guardrails; K3 hCS two-loop YBE probe is red. |
| 08 holography | CFG does not prove black-hole/holographic claims; theorem-grade physics stays with DVV/DMVV/Sen/CHL frames. |
| 09 defects/modules | CY3 perfect modules are holomorphic factorization modules with normal jets; CFG finite modules are shadows. |
| 10 cyclic A-infinity | Minimal input includes a negative-cyclic CY3 class, cyclic bar data, and an `S^3` framing witness. |
| 11 formality | `E_3` formality is theorem-level but carries a `GRT_1(Q)` torsor before fixing an associator. |
| 12 topology trace | Local constancy and RT trace are CFG theorems; CY3 trace theorem is conditional on the holomorphic object and modules. |

Local anchors used:

- `cy3_chain_level_bridge.tex:45-109`: many-variable chiral CE model and
  `C^*(\mathfrak g)` only as locally constant shadow.
- `cy3_chain_level_bridge.tex:112-135`: typed bridge
  `\PhiFA_3 -> \CoHA_{\crit} -> Y^+ -> D(Y^+) -> \mathcal W_{1+\infty}`.
- `cy3_chain_level_bridge.tex:203-218`: proved local
  `\CoHA(\mathbb C^3)=Y^+`, not `\mathcal W_{1+\infty}`.
- `cy3_chain_level_bridge.tex:273-312`: quartic CY3 hCS anomaly slot and
  no CFG shortcut.
- `cy3_chain_level_bridge.tex:317-365`: open oriented hCS-to-Hall
  comparison.
- `cy3_chain_level_bridge.tex:540-664`: Stage-1 envelope and CFG
  side-by-side scope restrictions.
- `cy_to_chiral.tex:4-40`: two-stage headline.
- `cy_to_chiral.tex:221-240`: `\PhiFA_d` and `\SpCh` definition.
- `cy_to_chiral.tex:242-299`: two-stage theorem and three-step Stage-1
  assembly.
- `cy_to_chiral.tex:271-278`: `n_native(d)=1` for `d>=3`.
- `cy_to_chiral.tex:4808-4836`: framed object-level `d=3` theorem and
  native `E_1` conclusion.
- `cy_to_chiral.tex:4857-4899`: Drinfeld-center braiding and residual
  hCS/Hall/global-`G` issues.
- `cy_to_chiral.tex:9446-9448`: summary: `\Phi_2` proved; `\Phi_3`
  framed object-level; global CY3 functoriality outside the theorem.

## ATTACK -> HEAL Cycles

### Cycle 1: CFG proves the CY3 hCS object

ATTACK. CFG constructs a filtered `E_3` algebra by BV quantization, so
it proves the CY3 hCS `E_3` factorization algebra.

FAILURE. CFG is ordinary 3d CS on real balls. The local collapse to
`C^*(\mathfrak g)` is precisely the locally constant Poincare lemma.
CY3 hCS keeps `\bar\partial`, `\Omega_X`, holomorphic jets in
`z_1,z_2,z_3`, polydisc factorization, and multidirectional residues.

HEAL. Cite CFG only as the topological CS template:
```tex
\Obs_{CS}^q(\mathbb R^3,\mathfrak g,\lambda)
  = A^\lambda,
\qquad
gr(A^\lambda)\simeq C^*(\mathfrak g).
```
The CY3 source theorem is Costello-Gwilliam/Costello-Li locality and the
Dolbeault chiral CE package, not CFG.

STATUS. CFG ordinary CS: proved elsewhere. CY3 hCS Stage 1:
conditional on the stated framed/holomorphic/anomaly hypotheses.

### Cycle 2: `C^*(\mathfrak g)` is `\PhiFA_3`

ATTACK. Since CFG identifies local classical observables with
`C^*(\mathfrak g)`, write `\PhiFA_3(\mathcal C)=C^*(\mathfrak g)`.

FAILURE. The manuscript explicitly obtains `C^*(\mathfrak g)` only after
the locally constant shadow. Before the shadow, the local object is
`C^\bullet_{\Lie,cont}(\Omega_c^{0,\bullet}(P,\mathfrak g)[1],\mathbb C)`
or its chiral/enveloping `E_3` factorization version.

HEAL. The only allowed comparison is:
```tex
\PhiFA_3(\mathcal C)|_P
  \rightsquigarrow
C^*(\mathfrak g)
```
after explicitly naming the forgetful/locally constant shadow functor.

STATUS. Direct identification killed.

### Cycle 3: final `\Phi_3` is native `E_3` or native `E_2`

ATTACK. Stage-1 `E_3` or CFG module braiding should make the final CY3
chiral algebra native `E_3` or native `E_2`.

FAILURE. `cy_to_chiral.tex` fixes
```tex
n_{\mathrm{native}}(d)=
\begin{cases}
\infty,&d=1,\\
2,&d=2,\\
1,&d\ge 3.
\end{cases}
```
At `d=3`, Dunn restriction from `E_3` to `E_2` is symmetric at the
topological level; it is not the nonsymmetric Yangian `R`-matrix.

HEAL. Keep:
```tex
A_\mathcal C^{(\Sigma_2,C)}
  =
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  \in E_1\text{-ChirAlg}(C),
\qquad
E_2\text{ lives on }
\mathcal Z(\Rep^{E_1}(A_\mathcal C)).
```

STATUS. Native `E_2`/`E_3` final-output claims killed.

### Cycle 4: hCS-to-Hall follows from CFG or from chartwise CoHA

ATTACK. Since `\CoHA(\mathbb C^3)=Y^+` and CFG gives `E_3` observables,
the hCS-to-Hall map is essentially proved.

FAILURE. The typed bridge separates four objects:
```tex
\PhiFA_3(\mathcal C)
\dashrightarrow \CoHA_{\crit}(X)
\to Y^+
\to D(Y^+)
\to \mathcal W_{1+\infty}.
```
Only the `\mathbb C^3` Hall-side core is proved. The comparison
`\PhiFA_3 -> \CoHA_{\crit}` is exactly open.

HEAL. State the map as the open oriented comparison
`\Theta_{\hCS\to\Hall}^{or}` with the six manuscript conditions
from `cy3_chain_level_bridge.tex:349-361`.

STATUS. General hCS-to-Hall theorem: open. Toric chart gluing:
conditional on the oriented comparison data. `\CoHA(\mathbb C^3)=Y^+`:
proved elsewhere.

### Cycle 5: CFG traces give Borcherds, DT, or black-hole traces

ATTACK. CFG proves a factorization-homology trace equals RT invariants;
therefore CY3 curve-defect traces, Borcherds denominators, DT/PT/GW
traces, or black-hole entropy follow.

FAILURE. CFG needs a framed link in a real 3-manifold and a perfect
module over its filtered `E_3` algebra. CY3 needs a holomorphic
constructible factorization module over the Dolbeault/chiral `E_3`
object, with endpoint objects, orientation data, Hall comparison, and
automorphic input. `\kappa_{\mathrm{BKM}}=5` alone is not an entropy
theorem.

HEAL. Conditional theorem shape:
```tex
\text{construct } \PhiFA_3
\to
\text{construct perfect holomorphic defect/module}
\to
\text{take chiral/factorization trace}
\to
\Theta_{\hCS\to\Hall}
\to
\text{Hall/BPS/automorphic comparison}.
```

STATUS. CFG RT trace: proved elsewhere for ordinary CS. CY3 defect
trace: conditional/conjectural. Holographic/QG consequences:
theorem-grade only in standard DVV/DMVV/Sen/CHL frames; CY3 chiral
interpretation conditional.

### Cycle 6: a Hochschild trace or topological framing is enough

ATTACK. A smooth proper cyclic CY3 category with a Hochschild trace and
the topological vanishing `\pi_3(BU)=0` automatically gives
`\PhiFA_3`.

FAILURE. The input must include a negative-cyclic CY3 class
`[\sigma]\in HC^-_3(\mathcal C)`, cyclic bar/cobar data, Connes
compatibility, all `A_\infty` operations and homotopies, and a
chain-level `S^3` framing or Costello-TCFT cancellation witness.
Topological vanishing is not the chain-level framing map.

HEAL. Minimal true input:
```tex
(\mathcal C,\{m_n\},[\sigma]\in HC^-_3(\mathcal C),
B(\mathcal C),B_{cyc}(\mathcal C),B_{\Connes},
(X,\Omega_X),\text{chain }S^3\text{-framing},(\Sigma_2,C)).
```

STATUS. Bare Hochschild trace and automatic-framing claims killed.

### Cycle 7: compute output proves the compact CY3 theorem

ATTACK. Existing compute engines prove the general compact CY3
chain-level theorem or the K3 hCS multi-loop/YBE tower.

FAILURE. The tests are strong guardrails, not a compact theorem.
Direct probe confirms Agent 07's red flag:
```text
sl2 two_loop_verification_passed = False
sl3 two_loop_verification_passed = False
```
The residuals are order `6.1e-06` at `hbar=0.01`, with
`hbar5_coefficient_estimate` of order `6e4`, so the advertised two-loop
YBE preservation is not verified by the current probe.

HEAL. Use compute evidence as local/toric/formal support. Add a targeted
test oracle before theorem-level citation of K3 hCS multi-loop claims.

STATUS. Compute support: useful. K3 hCS two-loop theorem evidence:
red until repaired.

### Cycle 8: K3-fibre specialization is just CFG `T^2` pushforward

ATTACK. The K3 x E specialization can be treated as CFG's real torus
pushforward.

FAILURE. In the current manuscript the canonical datum is holomorphic:
`\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3` over the elliptic base.
The CFG pushforward over real framed manifolds is only an analogy.

HEAL. Write K3 x E as holomorphic pushforward/chiral homology along the
K3 fibre, with `C=E`, and keep the Hall-Borcherds comparison conditional.

STATUS. CFG pushforward import killed. Holomorphic `\SpCh_{K3,E}`:
conditional on the manuscript hypotheses.

## Fatal Claims Killed

1. `CFG proves \PhiFA_3` for CY3.
2. `\PhiFA_3(\mathcal C)=C^*(\mathfrak g)` before locally constant
   shadow.
3. The final `d=3` chiral output is native `E_3` or native braided `E_2`.
4. The `E_3 -> E_2` Dunn restriction supplies the quantum-group
   `R`-matrix.
5. `CFG perfect modules = CY3 Hall/BKM/DT/PT/GW modules`.
6. `CFG trace = Borcherds denominator / black-hole entropy`.
7. `\Theta_{\hCS\to\Hall}` follows from CFG, KS wall-crossing, or
   chartwise `\CoHA(\mathbb C^3)=Y^+`.
8. A Hochschild trace is enough; the negative-cyclic CY3 class is
   optional.
9. `\pi_3(BU)=0` constructs the chain-level `S^3` framing.
10. K3 hCS two-loop/YBE evidence is theorem-grade in its current state.

## Surviving Theorem Spine

1. Input datum, conditional:
```tex
\mathcal C
\in CY_3\text{-Cat}
```
with smooth/proper cyclic `A_\infty` model, `HH^0(\mathcal C)=k`,
negative-cyclic CY3 class, CY3 target `(X,\Omega_X)`, chain-level
`S^3` framing/TCFT witness, and admissible `(\Sigma_2,C)`.

2. Stage 1, conditional object-level:
```tex
\PhiFA_3(\mathcal C)\in E_3\text{-HolFA}(X).
```
On hCS local charts:
```tex
\PhiFA_3(\mathcal C)|_P
  \simeq
U^{fact,E_3}_{P}(J^\infty_{hol}\mathfrak L_{\hCS}).
```

3. CFG theorem, external:
```tex
\Obs^q_{CS}(\mathbb R^3,\mathfrak g,\lambda)
\text{ is a locally constant filtered }E_3\text{-algebra},
\quad
gr\simeq C^*(\mathfrak g).
```
This is a template and locally constant shadow, not the CY3 object.

4. Stage 2, conditional:
```tex
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
  \in E_1\text{-ChirAlg}(C).
```

5. Braiding, constructed on loci where the center is built:
```tex
\mathcal Z(\Rep^{E_1}(A_\mathcal C))
\simeq
\Rep^{E_2}(Z^{der}_{ch}(A_\mathcal C)).
```

6. Hall side:
```tex
\CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1),
\qquad
D(Y^+)\to \mathcal W_{1+\infty}
\text{ only after doubling/evaluation}.
```
The map from hCS/Stage-1 to Hall is open in general.

7. K3 x E, conditional:
```tex
\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3,\qquad C=E,
```
and, assuming hCS-to-Hall plus Hall-Borcherds comparison,
```tex
\SpCh_{K3,E}(\PhiFA_3(\Perf(K3\times E)))
\leadsto
U_{ch}(\mathfrak g_{\Delta_5}),
\qquad
\kappa_{\mathrm{BKM}}=c(0)/2=5.
```

## Exact Manuscript Patches Recommended

No manuscript files were edited. Recommended patches:

1. `chapters/theory/cy_to_chiral.tex:22` and `:256`:
   replace "Stage 1 is pinned up to contractible choice" with a
   torsor-aware statement:
```tex
After fixing the relevant \(E_d\)-formality/associator datum, Stage~1 is
pinned up to contractible choice on the verified locus; at \(d=3\) the
unfixed formality data form the standard \(\mathrm{GRT}_1(\mathbb Q)\)-torsor.
```

2. `chapters/theory/cy3_chain_level_bridge.tex:626-630`:
   the current side-by-side remark risks saying CFG and CY3 agree before
   the locally constant shadow. Replace the paragraph by:
```tex
The two constructions have the same \(E_3\)-envelope grammar only after
applying the locally constant shadow and specialising the CY$_3$
Dolbeault input to a finite Lie algebra. Before this forgetful step,
CFG has no Dolbeault differential, holomorphic jets, polydisc OPE
residues, orientation datum, or Hall target; no quasi-isomorphism with
\(\PhiFA_3\) is asserted.
```

3. `chapters/theory/cy3_chain_level_bridge.tex:540-552`:
   after the displayed formula for
   `\PhiFA_3(\mathcal C)=Hol_X(U^FA(HH^\bullet(\mathcal C)))`,
   add an explicit local normal-form cross-reference:
```tex
On a holomorphic polydisc this is the many-variable model of
Definition~\ref{def:cy3-many-variable-chiral-ce}; ordinary
\(C^\bullet(\mathfrak g)\) appears only after the locally constant
shadow \(\Omega^{0,\bullet}(P)\simeq\mathbb C\).
```

4. `chapters/theory/cy_to_chiral.tex:664`:
   replace the self-referential phrase
   `\Sigma_2 = p^{-1}_{\Sigma_2}(\mathrm{pt})` by:
```tex
specialising along the chosen holomorphic surface
\(\Sigma_2\subset X\) (for \(K3\times E\),
\(\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3\)).
```

5. `chapters/theory/cy_to_chiral.tex:9448` and the duplicate closing
   summary near `:10689`:
   qualify the K3 x E BKM sentence:
```tex
the Borcherds--Monster BKM on \(K3\times E\), under the
K3-fibre Hall--Borcherds hypotheses of
Theorem~\ref{thm:g-delta5-is-sp-k3}, ...
```
This prevents the summary from reading as an unconditional hCS-to-Hall
or CFG consequence.

6. Any theorem-level citation of `compute/lib/k3_hcs_6d_twoloop.py`:
   downgrade to computational evidence until a test equivalent to
   `test_k3_hcs_twoloop_ybe_passes_on_grid` passes and the loop modules
   receive pytest coverage. The current direct probe returns
   `two_loop_verification_passed=False` for `sl2` and `sl3`.

## Claim Statuses

| Claim | Status |
|---|---|
| CFG ordinary 3d CS filtered `E_3` algebra and RT trace | Proved elsewhere. |
| `C^*(\mathfrak g)` as locally constant shadow | Proved/definitional after the shadow functor is named. |
| `C^*(\mathfrak g)` as CY3 `\PhiFA_3` | False. |
| Stage-1 `\PhiFA_3` on CY3 verified loci | Conditional object-level theorem. |
| Final `\Phi_3^{(\Sigma_2,C)}` | Conditional `E_1`-chiral object-level theorem. |
| Native `E_2` or `E_3` final CY3 output | False. |
| `E_2` braiding via Drinfeld center | Proved/constructed on stated loci; not global in arbitrary CY3. |
| `\Theta_{\hCS\to\Hall}^{or}` | Open. |
| `\CoHA(\mathbb C^3)=Y^+` | Proved elsewhere. |
| `\mathcal W_{1+\infty}` direct from CoHA | False; needs double/center/evaluation. |
| K3 x E `\Delta_5`, `\kappa_{\mathrm{BKM}}=5` automorphic side | Proved elsewhere under Borcherds/Gritsenko normalization. |
| K3 x E hCS/Hall/chiral BKM identification | Conditional on hCS-to-Hall and Hall-Borcherds comparison. |
| Holographic/QG consequences from CFG | False; at best conditional/metaphorical unless independent duality maps are named. |

## Computational Evidence and Red Flags

Agent-reported tests:

- Agent 01: 451 passed.
- Agent 02: 290 passed.
- Agent 03: 10 passed plus direct structure-function probes.
- Agent 04: 339 passed.
- Agent 05: 359 passed plus API checks.
- Agent 06: 135 passed.
- Agent 07: 535 passed on targeted core; 4730 passed on filename-matched
  broad surface; direct two-loop red flag.
- Agent 08: 51 + 65 + 4 + 134 passed.
- Agent 09: 319 passed.
- Agent 10: 301 passed and 248 passed.
- Agent 11 and Agent 12: report-only primary-source/local-anchor passes.

Agent 15 verification:

```bash
python3 -m pytest -q \
  compute/tests/test_s3_framing_chain_level.py \
  compute/tests/test_dolbeault_cy3_homotopy.py \
  compute/tests/test_cfg25_adversarial_consistency.py \
  compute/tests/test_chiral_ce_complex.py \
  compute/tests/test_hcs_codim2_defect_ope.py
```

Result: `342 passed in 0.56s`.

Direct K3 hCS two-loop probe:

```text
sl2: two_loop_verification_passed=False,
     two_loop_YBE_residual=6.107390268579593e-06.
sl3: two_loop_verification_passed=False,
     two_loop_YBE_residual=6.366777095291598e-06.
```

Interpretation: the guardrails are test-backed; the multi-loop K3 hCS
claim is not theorem-backed.

## Convergence Criterion

The CY3/CFG/E3 surface is converged when all manuscript claims satisfy
the following five checks:

1. Every CFG citation is typed as ordinary 3d CS theorem, formal/test
   oracle, or locally constant shadow.
2. Every occurrence of `C^*(\mathfrak g)` in the CY3 lane names the
   forgetful/locally constant shadow unless it is explicitly rejected.
3. Every final `d=3` chiral output is `E_1`; any `E_2` braiding is placed
   on a Drinfeld/derived center.
4. Every Hall/BKM/DT/holographic consequence names the intervening
   hCS-to-Hall, orientation, perfect-module, and automorphic comparison
   hypotheses.
5. No K3 hCS multi-loop statement is theorem-level until the two-loop
   YBE red flag is repaired by tests.

No fatal attack survives these restrictions. The surviving theorem spine
is narrower, but it is mathematically coherent and matches the local
anchors.

## Files Changed

- Added `notes/adversarial_swarm_20260424_cfg_e3/agent_15_hostile_synthesis.md`.

No manuscript files edited. No other agent report modified.

## Remaining Open Obligations

1. Construct `\Theta_{\hCS\to\Hall}^{or}` with orientation square roots,
   shifts, Tate twists, completions, overlap coherences, and
   Thom-Sebastiani compatibility.
2. Prove the Dolbeault/chiral CE-to-`E_3` bar identification with
   continuous duals and compact-support conventions fixed.
3. Prove holomorphic pushforward/envelope commutation for
   `\SpCh_{\Sigma_2,C}` beyond the current verified loci.
4. Build holomorphic perfect defect/module categories for CY3, including
   endpoint/puncture duality data.
5. Repair or downgrade the K3 hCS two-loop/YBE compute lane.
6. Keep holographic/QG consequences conditional unless the BPS/Hall/duality
   comparison maps are explicitly constructed.
