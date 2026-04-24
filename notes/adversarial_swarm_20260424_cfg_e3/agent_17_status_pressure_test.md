# Agent 17: Claim-Status Pressure Test

Date: 2026-04-24.

Owned file: `notes/adversarial_swarm_20260424_cfg_e3/agent_17_status_pressure_test.md`.

Scope: status levels in `chapters/theory/cy3_chain_level_bridge.tex` and
`chapters/theory/cy_to_chiral.tex` after the CY3/CFG/E3 integration. No
manuscript file was edited.

## Verdict

The integrated spine is directionally correct: CFG is not used as an
hCS-to-Hall theorem; `\Theta_{\hCS\to\Hall}` is open; the final
`d=3` output is native `E_1`; K3 x E BKM claims are mostly qualified by
Hall--Borcherds hypotheses.

The remaining pressure points are status granularity. Several statements
carry `\ClaimStatusProvedHere` while their own prose makes them conditional
on H1--H4, the chain-level `S^3` framing, holomorphic pushforward exactness,
or the hCS-to-Hall / Hall--Borcherds comparison. A few `Definitional`
badges also hide non-definitional quasi-isomorphism or negative-scope
claims.

## Attack-Heal Cycles

### Cycle 1: Many-variable chiral CE model as a definition

Claim attacked: `chapters/theory/cy3_chain_level_bridge.tex:45-117`,
especially lines `76-88`, labelled `\ClaimStatusDefinitional`.

Failure mode: lines `48-75` define the local dg Lie algebra and continuous
CE object. Lines `76-88` then assert
`\PhiFA_3(\cC)|_P \simeq U^{fact,E_3}_P(\mathfrak L_\cC)` and
`B_{E_3}(\PhiFA_3(\cC)|_P) \simeq CE^{ch,E_3}_*(\mathfrak L_\cC)`.
Those are comparison/quasi-isomorphism claims on the hCS-realised locus,
not mere definitions.

Healed status wording: keep `Definitional` for `\mathfrak L_\cC(P)` and
`\Obs_\cC^{cl}(P)`. Mark the two displayed identifications as
`Conditional on the hCS realisation of \PhiFA_3 and the continuous
Dolbeault/chiral CE bar comparison with compact-support conventions fixed`.

Severity: moderate. The present text is safe only because line `88` says
`on the loci where the hCS realisation ... is available`.

### Cycle 2: Local `\C^3` Hall core

Claim attacked: `chapters/theory/cy3_chain_level_bridge.tex:210-239`,
labelled `\ClaimStatusProvedElsewhere`.

Failure mode: none fatal. The direct theorem is
`\CoHA(\C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1)` by KS/SV, and the
text correctly prevents the false `\CoHA(\C^3)=\mathcal W_{1+\infty}`
identification at lines `222-224`.

Healed status wording: retain `ProvedElsewhere`; if sharpened, write
`ProvedElsewhere for the Hall-side positive-half identification;
Drinfeld-double/Fock passage is representation-theoretic, not the
hCS-to-Hall comparison`.

Severity: none.

### Cycle 3: CFG no-shortcut warning

Claim attacked: `chapters/theory/cy3_chain_level_bridge.tex:301-319`,
labelled `\ClaimStatusDefinitional`.

Failure mode: the badge is slightly too weak for the negative claim. The
warning uses a theorem-grade comparison: CFG constructs ordinary real
3d topological CS observables, while CY3 hCS keeps Dolbeault data,
holomorphic jets, polydisc residues, orientation data, and a separate
Hall target. This is not just terminology.

Healed status wording: acceptable as a warning, but the theorem-strength
version is `ProvedHere as a scope-separation lemma from the definitions
of CFG topological CS and the CY3 Dolbeault/chiral CE model; no
hCS-to-Hall comparison follows`.

Severity: low. The content is correct.

### Cycle 4: hCS-to-Hall comparison and toric descent

Claim attacked: `chapters/theory/cy3_chain_level_bridge.tex:241-275`,
`324-372`, and the status ledger `374-397`.

Failure mode: no overclaim in the ledger. The local-to-toric descent
package is correctly `Conditional` at lines `243-244`; the open problem
correctly requires orientation, shifts, Tate twists, completion,
equivariance, stability, anomaly cancellation, overlap orientation
cocycles, and Thom--Sebastiani compatibility at lines `349-368`.

Healed status wording: retain:
`General hCS-to-Hall comparison: Open. Toric descent: Conditional on
\Theta_{\hCS\to\Hall}^{or}. Local \C^3 Hall side: ProvedElsewhere.`

Severity: none.

### Cycle 5: Stage-1 envelope theorem

Claim attacked: `chapters/theory/cy3_chain_level_bridge.tex:547-609`,
labelled `\ClaimStatusConditional`.

Failure mode: the status is correct, but the equality
`\PhiFA_3(\cC)=\mathrm{Hol}_X(\cU^\FA(\HH^\bullet(\cC)))` at lines
`555-560` would be too strong without the parenthetical at lines
`549-550`. The proof also relies on the holomorphic twist and anomaly
gate, not on CFG.

Healed status wording: retain `Conditional`, with the exact scope:
`Conditional on the Stage-1 verified locus, fixed formality/associator
datum, Costello--Li holomorphic twist, and anomaly cancellation. Does
not imply \Theta_{\hCS\to\Hall}.`

Severity: none after the integration.

### Cycle 6: CY-A3 object-level existence badge

Claim attacked: `chapters/theory/cy_to_chiral.tex:62-88`, labelled
`\ClaimStatusProvedHere`.

Failure mode: too strong. The theorem itself says the object lies on a
`verified object-level locus` and depends on H1--H3 plus chain-level
witnesses. Lines `75-82` correctly deny equivalence, morphism
functoriality, and global `G(\cC)`, but the badge does not expose the
H4/framing and analytic-completion dependencies later made explicit in
Theorem `thm:cy-to-chiral-d3` at lines `4858-4918`.

Healed status wording:
`ClaimStatusConditional (proved here under H1--H4, fixed admissible
(\Sigma_2,C), chain-level S^3-framing witness, and the named analytic
completion hypotheses; not a global functor and not a construction of
G(\cC)).`

Severity: high. This is the main remaining status mismatch.

### Cycle 7: Three-step Stage-1 assembly

Claim attacked: `chapters/theory/cy_to_chiral.tex:286-300`, labelled
`\ClaimStatusProvedHere{steps (a),(b); conjectural at step (c) for
d \geq 3}`.

Failure mode: the macro says `ProvedHere` while the parenthetical says
the third step is conjectural/obstructed at `d >= 3`. The prose at
lines `299-300` then says the obstruction is resolved
`\infty`-categorically and chain-level at `d=3` by other theorems, which
is stronger than the displayed mixed status unless H4 and the verified
loci are named.

Healed status wording:
`ClaimStatusConditional{steps (a),(b) proved by Kontsevich--Tamarkin and
Costello--Gwilliam on H1--H4; step (c) unconditional at d<=2 and
conditional at d=3 on the chain-level framing/Costello--Li verified
locus; conjectural beyond the verified d>=3 loci.}`

Severity: high.

### Cycle 8: Stage-1 pinning via the GRT torsor

Claim attacked: `chapters/theory/cy_to_chiral.tex:339-351`, labelled
`\ClaimStatusProvedHereConditional`.

Failure mode: the step-(a) torsor statement is theorem-grade, using
Fresse--Willwacher/Willwacher and Tamarkin. The last sentence at lines
`346-347` upgrades from Hochschild `E_3` structures to
`E_3`-holomorphic factorisation algebras in `\EdHolFA(X)`, which imports
the Stage-1 holomorphic-twist hypotheses. The composite macro is
appropriate only if it is read as conditional, not as `ProvedHere`.

Healed status wording:
`ProvedElsewhere/ProvedHere for the E_3 formality torsor on Hochschild
cochains after choosing F; Conditional for the induced holomorphic
factorisation algebra \PhiFA_3(\cC)_F on the Stage-1 verified locus.`

Severity: moderate.

### Cycle 9: GRT invariance of the four `\kappa` invariants

Claim attacked: `chapters/theory/cy_to_chiral.tex:363-381`, labelled
`\ClaimStatusProvedHere`.

Failure mode: overbroad quantification. `\kcat` and
`\kappa_{\mathrm{fibre}}` are external to the formality torsor;
Heisenberg `\kch` is cohomological on constructed outputs; but
`\kBKM(\Phi_N)=c_N(0)/2` exists only when a Borcherds input has been
chosen. The claim cannot hold literally for every CY3 category and every
specialisation datum unless the Borcherds branch exists.

Healed status wording:
`ClaimStatusConditional{GRT-invariant on constructed Stage-2 outputs;
\kcat and \kappa_{\mathrm{fibre}} are independent of the torsor,
Heisenberg \kch is cohomological, and \kBKM is included only on the
Borcherds-input branch where c_N(0)/2 is defined.}`

Severity: moderate.

### Cycle 10: Stage-2 `\SpCh` as an exact functor

Claim attacked: `chapters/theory/cy_to_chiral.tex:533-550`, labelled
`\ClaimStatusProvedHere`.

Failure mode: too strong. Abstract factorisation homology and exact
restriction are standard, but the Vol III `\SpCh_{\Sigma_{d-1},C}`
kernel formula at lines `541-545` assumes admissibility, holomorphic
pushforward/restriction, and the compatibility of the `E_d` holomorphic
FA with the chosen cycle. Swarm synthesis lists holomorphic
pushforward/envelope commutation beyond verified loci as an open
obligation.

Healed status wording:
`ClaimStatusConditional{ProvedElsewhere for abstract factorisation
homology on an already constructed E_d-holomorphic FA and admissible
cycle; conditional for the Vol III kernel/pushforward model and for
CY3 compact/non-formal applications.}`

Severity: high.

### Cycle 11: K3 x E Hall--Borcherds endpoint and landscape table

Claim attacked: `chapters/theory/cy_to_chiral.tex:9382-9400`,
`9441-9473`, and `9501-9503`.

Failure mode: the conjecture at lines `9382-9400` is correctly labelled
`Conjectured`. The landscape table at lines `9441-9473` is less safe:
the `K3 \times E` row lists `D(Y^+(\fg_{K3}))` and `\mathbf G via
Borcherds`, and the prose says entries marked `yes` enjoy three-path
cross-verification at formality. That can be read as an algebra-level
`G(K3\times E)` theorem, contradicting the conjectural endpoint at
lines `9386-9398` and the conditional K3-fibre theorem at
`718-727`.

Healed status wording:
`K3 x E automorphic denominator and \kBKM(\Delta_5)=5: ProvedElsewhere
under Borcherds/Gritsenko normalisation. K3 x E Hall--Borcherds double
G(K3 x E)=D(Y^+_{\Hall}(K3 x E)): Conjectural/Conditional on the
positive half, Hopf pairing, completion, hCS-to-Hall map, and
bracket-preserving Hall--Borcherds comparison.`

Severity: high for the table prose, not for the conjecture block.

### Cycle 12: Root multiplicity transfer

Claim attacked: `chapters/theory/cy_to_chiral.tex:10648-10664` and
`10695-10699`, labelled `\ClaimStatusProvedHere`.

Failure mode: the formula `\mathrm{mult}_3(n,l,m):=f(nm,l)` is introduced
definitionally at lines `10654-10658`. The proposition then promotes it
to `ProvedHere` under the fibration and states K3 consequences. For the
K3 Jacobi input, the consequences are Borcherds/Gritsenko coefficient
facts; for general CY2 input, the transfer is part of the chosen root
datum or the conditional Borcherds-lift theorem, not an independent
proved-here theorem.

Healed status wording:
`ClaimStatusDefinitional for the transfer rule in the constructed
fibered root datum; ProvedElsewhere for the K3 \phi_{0,1} coefficient
consequences; Conditional when asserted as a CY2-to-CY3 fibration theorem.`

Severity: moderate.

## Status Table

| Claim surface | Present status | Pressure-test result |
|---|---:|---|
| Many-variable CE object definition | Definitional | Split: definition plus conditional comparison. |
| `\CoHA(\C^3)=Y^+` | ProvedElsewhere | Correct. |
| `\Theta_{\hCS\to\Hall}^{or}` | Open | Correct. |
| Stage-1 envelope theorem | Conditional | Correct. |
| CY-A3 object-level existence | ProvedHere | Too strong; use Conditional / ProvedHereConditional. |
| Stage-1 three-step assembly | ProvedHere with conjectural clause | Too strong at macro level; use Conditional mixed status. |
| GRT torsor pinning | ProvedHereConditional | Correct only with explicit Stage-1 verified-locus reading. |
| GRT invariance of four `\kappa` invariants | ProvedHere | Too broad; condition the Borcherds branch. |
| Stage-2 `\SpCh` kernel exactness | ProvedHere | Too strong beyond abstract factorisation homology. |
| K3 x E algebra-level `G(K3 x E)` | Conjectured/Conditional in theorem blocks | Correct there; table prose needs the same condition. |
| `\kBKM(\Delta_5)=5` | ProvedElsewhere | Correct, as automorphic/Borcherds input, not a chiral `\kappa_{\mathrm{ch}}`. |
| Root multiplicity transfer | ProvedHere | Should be definitional/proved-elsewhere/conditional by scope. |

## Recommended Manuscript Edits

No edits were made. If the integrator chooses to patch, the narrow changes
are:

1. Downgrade `thm:cya3-existence-rigidity` from `\ClaimStatusProvedHere`
   to a conditional badge matching `thm:cy-to-chiral-d3`.
2. Replace the mixed `\ClaimStatusProvedHere{steps (a),(b); conjectural
   ...}` on `prop:phi-fa-three-step-assembly` with a conditional mixed
   status.
3. Downgrade or split `prop:spch-infty1-kernel`: abstract
   factorisation homology is proved elsewhere; the Vol III kernel model
   is conditional on admissibility and verified holomorphic pushforward.
4. Split `def:cy3-many-variable-chiral-ce` so the local object remains
   definitional and the `\PhiFA_3` / `E_3`-bar comparison carries its
   conditional status.
5. Add a condition directly to the K3 x E row in
   `rem:cy3-landscape-GofX-table`, mirroring
   `thm:GofK3E-baseline`.
6. Reclassify `prop:thy-fibration-root-mult-transfer` as definitional
   for the transfer rule, proved elsewhere for K3 Jacobi coefficients,
   conditional for general CY2-to-CY3 fibration.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/vol3-beilinson-loop/SKILL.md`
- `.agents/skills/vol3-claim-verification/SKILL.md`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/theory/cy_to_chiral.tex`
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md`
- `notes/adversarial_swarm_20260424_cfg_e3/agent_15_hostile_synthesis.md`

Commands used included targeted `rg`, `nl -ba ... | sed -n`, `wc -l`,
and `git status --short`. No build was run because the assignment was a
status audit with no manuscript edit.
