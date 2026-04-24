# Agent 03: Phi-Functor Foundations

Scope: `chapters/theory/cy_to_chiral.tex`, `chapters/theory/en_factorization.tex`, `chapters/theory/cy_categories.tex`, `chapters/theory/cy3_chain_level_bridge.tex`, `notes/wave12_a1_phi_functor_foundations.tex`, and Vol I/II grep concordance.

Verdict: the two-stage architecture is locally present and cross-volume concordant, but three phrases remain dangerous because they can be read as stronger than the proved surface: "functor" at `d=3`, "stage-1 output is E_1", and untagged `\Phi_d` where the specialisation datum is load-bearing. The safe spine is:
\[
\Phi_d^{(\Sigma_{d-1},C)}(\cC)=\SpCh_{\Sigma_{d-1},C}(\PhiFA_d(\cC)),
\qquad
n(d)=\infty,2,1\text{ for }d=1,2,\ge 3.
\]
Stage 1 is the native holomorphic factorisation algebra on the CY target, pinned only on verified loci. Stage 2 is factorisation homology over the chosen cycle and restriction to `C`. At `d=3`, the output is a framed object-level `E_1`-chiral algebra; arbitrary morphism functoriality remains `\ClaimStatusConjectured`.

## ATTACK_1: A Single Functor `\Phi` Is Not Supported

Attacked claim: `\Phi` is a single functor `CY-Cat -> ChirAlg`, or `\Phi_3` is already a functor on all smooth proper CY3 categories.

Local anchors:
- `chapters/theory/cy_to_chiral.tex:4-40`: headline theorem is `\ClaimStatusConditional`; arbitrary CY morphism functoriality and compact non-formal CY3 strictification are deferred.
- `chapters/theory/cy_to_chiral.tex:87-94`: object-level chain-level `\Phi_d` and `(infty,1)`-categorical `\Phi_d`-as-functor are separate statements.
- `chapters/theory/cy_to_chiral.tex:670-693`: `{ \Phi_d }` is a `d`-indexed correspondence programme, not a unified functor; U2 is conjectural.
- `chapters/theory/cy_to_chiral.tex:743-750`: per-`d` functoriality is `\ClaimStatusConjectured`.
- `chapters/theory/cy_categories.tex:240-255`: the phrase "the `d=3` extension exists as an `E_1`-chiral functor" is immediately narrowed to an object assignment after H1--H4 and fixed specialisation. The first sentence is too strong unless rewritten.

Failure mode: the theorem on objects can be silently upgraded to functoriality on morphisms. That makes later wall-crossing, Mukai-transform, and Fourier--Mukai-kernel statements circular: they would use morphism action to prove the construction that must first define morphism action.

HEAL_1:

Prerequisite chain:
1. Fix one dimension `d`; no cross-`d` target category is asserted.
2. Fix a cyclic `A_\infty` CY category with smooth/proper/CY data and negative cyclic CY class.
3. Construct `\PhiFA_d(\cC)` on the verified Stage-1 locus.
4. Fix an admissible specialisation datum `( \Sigma_{d-1}, C )`.
5. Define the object `\Phi_d^{(\Sigma_{d-1},C)}(\cC)`.
6. Add morphism action only under `Conjecture~\ref{conj:phi-d-functoriality}` or a separately verified case.

Replacement statement:

```tex
For fixed $d$ and fixed admissible $(\Sigma_{d-1},C)$, the constructed object is
\[
\Phi_d^{(\Sigma_{d-1},C)}(\cC)
=\SpCh_{\Sigma_{d-1},C}(\PhiFA_d(\cC)).
\]
At $d\le 2$ this is functorial on the stated smooth proper locus.
At $d=3$ it is the framed object-level assignment of
Theorem~\ref{thm:cy-to-chiral-d3}.  Functoriality on cyclic
$A_\infty$ morphisms is Conjecture~\ref{conj:phi-d-functoriality}.
```

Targeted local repair: in `chapters/theory/cy_categories.tex:243-246`, replace "exists as an `\Eone`-chiral functor" by "exists as a framed `\Eone`-chiral object assignment on the verified locus". This is a wording repair; the following paragraph already has the right scope.

Status recommendation: keep `\ClaimStatusConditional` for `thm:phi-platonic`; keep U2 explicitly conjectural.

## ATTACK_2: `\SpCh_{\Sigma,C}` Choices Are Not Canonical Globally

Attacked claim: the notation `\Phi_d(\cC)` determines a unique chiral output without tagging the cycle and curve.

Local anchors:
- `chapters/theory/cy_to_chiral.tex:303-344`: canonical specialisation cycles exist only per CY class, not uniformly; untagged `\Phi_d` is governed by three reading conventions.
- `chapters/theory/cy_to_chiral.tex:322-329`: multiple specialisations of one `\PhiFA_d` produce multiple `E_1` shadows.
- `chapters/theory/cy_to_chiral.tex:4774-4784`: K3 x E alternatives are Stage-2 specialisations of one Stage-1 output, not repeated `\Phi_3` applications.
- `chapters/theory/en_factorization.tex:86-90`: `( \Sigma_{d-1}, C )` moduli are the parameter space of `E_1` shadows.
- `notes/wave12_a1_phi_functor_foundations.tex:889-923`: the earlier adversarial cycle already isolates "six routes" as Stage-2 multiplicity.

Failure mode: untagged notation turns the `(\Sigma_{d-1},C)` choice into an invisible parameter. For K3 x E this can create the false statement that six BKM outputs are six applications of `\Phi_3`, or that a Borcherds weight is read from an untargeted Euler characteristic.

HEAL_2:

Prerequisite chain:
1. Stage 1: construct `\PhiFA_d(\cC)` once.
2. Stage 2: choose a closed oriented/framed admissible `(d-1)`-cycle `\Sigma_{d-1}` and a reference curve `C` transverse to it.
3. Apply factorisation homology and restriction:
   \[
   \SpCh_{\Sigma_{d-1},C}(\cF)
   =
   \left(\int_{\Sigma_{d-1}}\cF\right)\big|_C.
   \]
4. If two Stage-2 outputs are compared, both cycle-pairs must be named.

Replacement statement:

```tex
The unqualified symbol $\Phi_d(\cC)$ is permitted only when the
canonical specialisation datum for the CY class has been fixed earlier,
or when the statement is uniform in $(\Sigma_{d-1},C)$.  Otherwise write
\[
\Phi_d^{(\Sigma_{d-1},C)}(\cC)
:=\SpCh_{\Sigma_{d-1},C}(\PhiFA_d(\cC)).
\]
The multiplicity of shadows is the multiplicity of admissible
Stage-2 data, not a multiplicity of Stage-1 outputs.
```

Vol I/II concordance by grep:
- Vol I `CLAUDE.md:57-63` and `81-89` state the same two-stage factorisation and family of `E_1` shadows.
- Vol II `CLAUDE.md:349-358` and `514-518` state Stage 1 followed by specialisation to the `E_1`-chiral shadow.

Status recommendation: no theorem-status change; notation discipline is the repair.

## ATTACK_3: `E_d`, `E_1`, and `E_2` Are Still Locally Slippery

Attacked claim: Stage 1 itself is `E_1` at `d >= 3`, or the `E_2` braiding at `d >= 3` lives on the specialised chiral algebra.

Local anchors:
- `chapters/theory/cy_to_chiral.tex:10-13`, `221-236`, `243-267`: Stage 1 lands in `\EdHolFA(X)`; Stage 2 lands on the curve.
- `chapters/theory/cy_to_chiral.tex:272-278`: the specialised shadow has native level `\infty,2,1`.
- `chapters/theory/cy_to_chiral.tex:316-321`: at `d >= 3`, `E_2` lives on the derived chiral centre, not on `A_\cC`.
- `chapters/theory/en_factorization.tex:7-12`: correctly says the `E_n` apparatus targets Stage 1 and Stage 2 collapses `E_d -> E_1`.
- `chapters/theory/en_factorization.tex:25`, `45`, `48`: dangerous phrasing says Stage 1 produces `\Eone` or is `\Eone`-stabilised on `X`.
- `chapters/theory/cy_to_chiral.tex:4681-4784`: the `d=3` theorem states the specialised output is natively `\Eone`, with `\Etwo` recovered by the Drinfeld centre.

Failure mode: two different meanings of "native level" are being interchanged:
- ambient holomorphic factorisation level on the CY target: `\PhiFA_d(\cC) \in \EdHolFA(X)`;
- surviving chiral operadic level on the reference curve after Stage 2: `E_{n(d)}` with `n(d)=1` for `d>=3`.

HEAL_3:

Prerequisite chain:
1. From the CY bracket and formality, Stage 1 is an `E_d`-holomorphic factorisation algebra on `X`.
2. Dunn--Lurie gives `E_d \simeq E_{d-1} \otimes E_1`.
3. Factorisation homology over the transverse `(d-1)`-cycle consumes the `E_{d-1}` factor.
4. The residual chiral algebra on `C` is `E_1` for `d>=3`, `E_2` for `d=2`, `E_\infty` for `d=1`.
5. At `d>=3`, any quantum-group `E_2` braiding belongs to `\cZ(\Rep^{E_1}(A_\cC))`, not to `A_\cC`.

Replacement statement for `en_factorization.tex:25,45,48`:

```tex
For $d\ge 3$, $\PhiFA_d(\cC)$ remains an $E_d$-holomorphic
factorisation algebra on $X$.  After the Stage-2 specialisation
\[
\SpCh_{\Sigma_{d-1},C}(\PhiFA_d(\cC)),
\]
the chiral algebra on $C$ is natively $E_1$.  The higher $E_d$
structure survives as shifted/framing data and as the Drinfeld-centre
braiding on representations; it is not an $E_2$ structure on the
specialised algebra itself.
```

Vol I/II concordance by grep:
- Vol I `chapters/theory/en_koszul_duality.tex:8188-8194`: K3 x E at `d=3` is natively `E_1`; `E_2` lives on the Drinfeld centre.
- Vol II `chapters/frame/preface.tex:837-862`: `E_1 -> E_2` is Hochschild/derived-centre promotion, not the original boundary algebra.

Status recommendation: moderate wording defect, not a mathematical contradiction if repaired by distinguishing ambient `E_d` from curve-level `E_1`.

## ATTACK_4: Chain-Level and `(infty,1)`-Categorical Claims Must Not Prove Each Other

Attacked claim: chain-level object construction and `(infty,1)` functoriality are interchangeable, or the derived-kernel statement proves full `d=3` functoriality.

Local anchors:
- `chapters/theory/cy_to_chiral.tex:87-94`: the two scopes are explicitly distinct.
- `chapters/theory/cy_to_chiral.tex:388-445`: Stage-1 kernel is conditional; Stage-2 is proved; the composite is functorial at `d<=2`, but at `d=3` it is object-level and morphism functoriality remains conjectural.
- `chapters/theory/cy_categories.tex:11-25`: chain-level and `(infty,1)`-categorical lanes are equal status, neither a shadow of the other.
- `chapters/theory/cy_categories.tex:230-255`: cyclic `A_\infty` enhancement is needed before `\Phi`; at `d=3` the general theorem is conditional on `S^3` framing and fixed specialisation.
- `notes/wave12_a1_phi_functor_foundations.tex:479-520`: previous foundation note declares object-level `\Phi_d` and morphism preservation as separate.

Failure mode: the proof sketch of `prop:phifa-infty1-kernel` can be overread. Tamarkin functoriality and Costello--Gwilliam locality give parts of the assembly, but the holomorphic twist, framing, and cyclic `A_\infty` compatibility are exactly where `d>=3` ceases to be automatic.

HEAL_4:

Prerequisite chain for object-level chain construction:
1. smooth proper cyclic `A_\infty` CY data;
2. Gerstenhaber bracket of degree `1-d`;
3. Kontsevich--Tamarkin formality up to contractible choice;
4. Costello--Gwilliam locality;
5. Costello--Li holomorphic twist with CY form;
6. for `d=3`, H1--H4 plus chain-level `S^3` framing;
7. admissible `( \Sigma_2, C )`.

Prerequisite chain for `(infty,1)` functoriality:
1. all object-level prerequisites above;
2. cyclic `A_\infty` morphism compatible with the framing;
3. Fourier--Mukai or equivalent kernel representing the morphism;
4. convolution compatibility of Hochschild-to-factorisation assembly;
5. holomorphic twist functoriality at the relevant dimension;
6. proof of identity/composition preservation in `E_{n(d)}-\mathrm{ChirAlg}`.

Replacement statement:

```tex
The chain-level assignment constructs objects with explicit witnessing
homotopies.  The $(\infty,1)$-categorical functor requires a separate
morphism theorem.  At $d=3$ the manuscript proves the framed object
assignment on H1--H4 loci; it does not prove arbitrary morphism
functoriality, hocolim exactness, or global exactness.
```

Status recommendation: keep the chain/infinity parity remark. Do not use `(infty,1)` terminology to upgrade a chain-level object theorem.

## ATTACK_5: The CY3 hCS-to-Hall Bridge Cannot Be Used as a Functoriality Proof

Attacked claim: six-real-dimensional hCS, critical CoHA, `Y^+`, and `\mathcal W_{1+\infty}` are already one functorial `\Phi_3` output.

Local anchors:
- `chapters/theory/cy3_chain_level_bridge.tex:46-68`: typed bridge is `\PhiFA_3 -> CoHA_crit -> Y^+ -> D(Y^+) -> W_{1+\infty}`, with the first arrow dashed.
- `chapters/theory/cy3_chain_level_bridge.tex:137-164`: proved local core is `CoHA(C^3) ~= Y^+`; `W_{1+\infty}` is reached after doubling and representation.
- `chapters/theory/cy3_chain_level_bridge.tex:245-288`: hCS-to-Hall comparison is an open problem requiring orientation, shifts, completion, stability, anomaly cancellation, and Thom--Sebastiani coherence.
- `chapters/theory/cy3_chain_level_bridge.tex:295-310`: status ledger marks `\PhiFA_3(\cC) -> CoHA_crit(X)` open in general.
- `chapters/theory/cy_categories.tex:294-302`: writing `\Phi(\CoHA(\C^3))` is a type error; CoHA is an associative algebra, not a CY-category input.

Failure mode: local representation-theoretic theorems are being promoted into a global CY3 functor. This loses the orientation datum and turns the Drinfeld double into an ordinary Stage-2 output.

HEAL_5:

Prerequisite chain:
1. `\PhiFA_3(\cC)` is a holomorphic factorisation algebra.
2. A comparison to critical CoHA requires a natural orientation-preserving quasi-isomorphism in `\mathsf{FactCosh}_{\Hall}^{or,\wedge}`.
3. On `\C^3`, the algebraic Hall side is proved: `\CoHA(\C^3) \cong Y^+(\widehat{\mathfrak{gl}}_1)`.
4. The full `\mathcal W_{1+\infty}` appears only after Drinfeld doubling and Fock/evaluation representation, equivalently through the centre/representation passage.
5. None of these steps proves arbitrary `\Phi_3` morphism functoriality.

Replacement statement:

```tex
On toric CY3 charts, the Hall-side local model gives
\[
\CoHA(\C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1).
\]
The comparison from $\PhiFA_3$ to oriented critical CoHA is the open
map $\Theta_{\hCS\to\Hall}^{or}$.  The full
$\mathcal W_{1+\infty}$ is obtained after Drinfeld doubling and
Fock/evaluation, or equivalently through the Drinfeld-centre passage;
it is not the direct $\Phi_3$ output.
```

Status recommendation: keep `cy3_chain_level_bridge.tex` as the blocking ledger for non-formal compact CY3 claims. Any theorem using the hCS-to-Hall arrow outside toric verified cases must be `\ClaimStatusConditional` or `\ClaimStatusOpen`.

## Cross-Volume Concordance

Vol I concords with the healed spine:
- `~/chiral-bar-cobar/CLAUDE.md:57-63`: two-stage factorisation and family of `E_1` shadows.
- `~/chiral-bar-cobar/CLAUDE.md:81-89`: Stage 1 is canonical `E_d`-holomorphic factorisation; Stage 2 is factorisation homology over `\Sigma_{d-1}` and restriction to `C`.
- `~/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:8188-8194`: at `d=3`, K3 x E is natively `E_1`; the `E_2` braided enhancement lives on the Drinfeld centre.

Vol II concords with the healed spine:
- `~/chiral-bar-cobar-vol2/CLAUDE.md:64-74`: Vol III two-stage factorisation gives the `E_1` chiral shadow after Stage 2.
- `~/chiral-bar-cobar-vol2/CLAUDE.md:349-366`: Stage 1 is holomorphic/braided local observables; Stage 2 is ordered/topological `E_1`.
- `~/chiral-bar-cobar-vol2/CLAUDE.md:514-518`: MC5 specialises the Stage-1 algebra along `\Sigma_{d-1}` to the `E_1` shadow on `C`.
- `~/chiral-bar-cobar-vol2/chapters/frame/preface.tex:441-448`: chiral Hochschild is the bridge from Vol II structure to Vol III CY input.

No cross-volume disagreement was found by grep. The local report findings are wording/scope repairs, not a divergence between volumes.

## Files Changed

- `notes/adversarial_architecture_swarm_20260424/agent_03_phi_functor.md`

## Verification Surface

Commands run:
- `sed -n` on `CLAUDE.md` and `AGENTS.md`.
- `rg` and targeted `sed` on all five anchor files.
- `rg` and targeted `sed` across `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2` for two-stage factorisation, `E_1/E_2`, Drinfeld centre, and `\Phi_d` concordance.

No LaTeX build was run; this report adds no compiled manuscript surface.
