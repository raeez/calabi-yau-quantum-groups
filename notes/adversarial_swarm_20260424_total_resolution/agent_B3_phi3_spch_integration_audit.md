# Agent B3: Phi_3 / SpCh Integration Audit

Date: 2026-04-24

Scope: read-only second-pass audit of

- `chapters/theory/cy_to_chiral.tex`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A3_spch_functoriality.md`

No manuscript source was edited.

## Verdict

The A3 repair is mathematically coherent: arbitrary CY3 Fourier--Mukai
functoriality remains conjectural/open, while the new witnessed-kernel
statement is proved only because every coherence cell needed for the
construction is part of the input data.

The integration is not fully sealed. Three older manuscript surfaces still
state the two-stage or `SpCh` construction too broadly, using "admissible"
where the proof actually needs "witnessed admissible" and suggesting
functoriality in specialisation data beyond the supplied Beck--Chevalley,
Fubini/envelope, proper-support, Tor-independence, completion, and anomaly
cells.

## Confirmed Correct Boundaries

1. `cy_to_chiral.tex:518--555`
   defines witnessed admissible CY3 specialisation data and includes
   precisely the missing cells:

   - proper/Tor-independent incidence kernel;
   - Beck--Chevalley 2-cell;
   - Fubini/envelope 2-cell;
   - Hall/stable-envelope/Borcherds enlargement when invoked;
   - morphisms carrying coherent cyclic, formality, framing, anomaly,
     completion, and specialisation data.

2. `cy_to_chiral.tex:683--748`
   proves the correct witnessed theorem:
   `\Phi_3^{\mathrm{wit}}` is functorial on
   `\CY_3\text{-}\Cat_{\Phi_3}^{\mathrm{wit}}` because K1--K7 are
   included in the source category. The proof does not derive those cells
   from an arbitrary kernel; it transports through them.

3. `cy_to_chiral.tex:750--801`
   states the right obstruction criterion for arbitrary CY3 morphisms.
   If O1--O7 are absent, the two object-level outputs exist but no map
   `\Phi_3(f)` is defined.

4. `cy_to_chiral.tex:1369--1377`
   keeps per-`d` functoriality conjectural and explicitly says that at
   `d=3` only `\Phi_3`-admissible witnessed kernel data are covered.

5. `cy_to_chiral.tex:5451--5453` and `5482--5484`
   correctly exclude arbitrary CY3 morphisms, global `G(\mathcal C)`, and
   the hCS-to-Hall comparison from Theorem `thm:cy-to-chiral-d3`.

## Findings

### MODERATE: headline theorem still uses ordinary admissibility

Anchor: `cy_to_chiral.tex:4--44`.

`thm:phi-two-stage-factorisation-headline` is marked
`\ClaimStatusProvedHere{}` and states the construction for "an admissible
specialisation datum" before the witnessed datum is introduced. Its Stage-2
sentence says factorisation homology over the cycle and restriction to the
curve, but does not mention the Beck--Chevalley or Fubini/envelope cells.

Failure mode: a reader can cite this theorem for ordinary
pushforward/restriction without the witnessed support and envelope data.

Recommended repair: either replace "admissible" by "witnessed admissible
on the CY3 stage" or add a sentence saying that, at `d=3`, "admissible"
means the witnessed datum of Definition
`def:witnessed-admissible-specialisation-datum`; otherwise the statement is
only an object-level template.

### MODERATE: early two-stage theorem asserts functoriality in specialisation data too broadly

Anchor: `cy_to_chiral.tex:252--282`, especially `277--280`.

The theorem says that where the factorisation-homology kernels are defined,
the assignment

```tex
(\Sigma_{d-1}, C) \mapsto
\SpCh_{\Sigma_{d-1}, C}(\PhiFA_d(\mathcal C))
```

is functorial in the specialisation datum, symmetric monoidal under
disjoint union of admissible cycles, and Kunneth-compatible.

Failure mode: this is exactly the kind of pushforward/envelope commutation
overclaim A3 rejected. "Kernels are defined" is weaker than the witnessed
data actually used later: properness, Tor-independence, Beck--Chevalley,
Fubini/envelope, compact-support convention, holomorphic propagator, and
completion must be supplied.

Recommended repair: restrict the sentence to morphisms of witnessed
specialisation data. The theorem can remain proved only on that category;
outside it, functoriality is conditional or conjectural.

### MODERATE: `thm:cy-to-chiral-d3` conclusion says admissible, not witnessed

Anchor: `cy_to_chiral.tex:5391--5453`, especially `5405--5414`.

The theorem's conclusion forms

```tex
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  := \SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
```

"after choosing an admissible specialisation datum." Later scope text
correctly excludes arbitrary CY3 morphisms, but the object-level Stage-2
construction still needs the witnessed specialisation datum when the proof
uses `SpCh` as an exact functor with the pushforward/kernel formula.

Failure mode: this leaves a gap between the statement and the proof surface:
the proof invokes fixed Stage-2 specialisation, while the rigorous `SpCh`
proposition proves exactness only for witnessed data.

Recommended repair: change the d=3 theorem statement to "witnessed
admissible specialisation datum" or explicitly cite Definition
`def:witnessed-admissible-specialisation-datum` in the conclusion.

### LOW: definition names `SpCh` as a functor before the witness restriction

Anchor: `cy_to_chiral.tex:231--250`.

Definition `def:phi-fa-and-sp` defines the "chiral specialisation functor"
for an admissible cycle and curve using
`\int_{\Sigma_{d-1}}(-)|_C`. This is acceptable as notation, but it should
not be the cited proof of exactness or pushforward/envelope commutation.
The proof-grade statement is later Proposition `prop:spch-infty1-kernel`
on witnessed data.

Recommended repair: when this definition is next touched, add a scope
sentence: at `d=3`, functorial exactness and kernel formulas are those of
Proposition `prop:spch-infty1-kernel` and require witnessed data.

### WATCHLIST: non-B3 but surfaced while grepping Phi_3

Anchor: `cy_to_chiral.tex:5063`.

The shadow--BPS evidence table marks the quintic row as
`\textbf{Proved} (via \Phi_3, Thm.~\ref{thm:cy-to-chiral-d3})`. This
collides with nearby scope discipline saying compact non-formal CY3
instances require their own framing/strictification witnesses. This is not
a SpCh/morphism-level defect, but it is a likely status overclaim.

## A3 Report Consistency Check

A3's report states the correct theorem:

```text
WSpCY3 objects = CY3 category + formality point + S3 framing +
Costello--Li witness + completion + witnessed Stage-2 data.

WSpCY3 morphisms = cyclic Fourier--Mukai/A_infty kernels plus all
negative-cyclic, Hochschild/brace, S3, Costello--Li, support,
Beck--Chevalley, Fubini/envelope, identity, and associativity coherences.
```

The integrated theorem `thm:phi3-witnessed-kernel-functoriality` matches
this: it is a functor because the source category has been enlarged until
the desired map is tautologically constructible by composition of specified
cells. It is not a proof that arbitrary Fourier--Mukai kernels act on
`\Phi_3`.

## Pushforward / Envelope Commutation Status

Proved on witnessed data:

- `cy_to_chiral.tex:538--545`: Beck--Chevalley and Fubini/envelope cells are
  input data.
- `cy_to_chiral.tex:595--596`: the proof of `SpCh` exactness explicitly
  uses these cells plus properness and Tor-independence.
- `cy_to_chiral.tex:729--734`: witnessed kernel functoriality pushes through
  Stage 2 only after K6 supplies the cells.

Not proved beyond witnessed data:

- ordinary admissible cycles without proper/Tor-independent incidence
  kernels;
- arbitrary Fourier--Mukai kernels that move or mix the chosen
  `(\Sigma_2,C)`;
- kernels crossing Hall/stable-envelope chambers without an explicit
  wall-crossing `R`-matrix;
- compact non-formal CY3 targets lacking Costello--Li naturality and
  analytic-completion transport.

## Verification Commands

Read-only commands used:

```bash
sed -n '1,260p' notes/adversarial_swarm_20260424_total_resolution/agent_A3_spch_functoriality.md
sed -n '261,620p' notes/adversarial_swarm_20260424_total_resolution/agent_A3_spch_functoriality.md
rg -n "SpCh|specialisation|witness|witnessed|Fourier|Mukai|kernel|pushforward|envelope|commut|Beck|Fubini|cyclic|coherence|arbitrary|morphism|Phi_3|PhiFA|functorial" chapters/theory/cy_to_chiral.tex
rg -n "thm:cy-to-chiral-d3|conj:phi-d-functoriality|phi3-admissible|witnessed data|morphism of witnessed|arbitrary CY\\$?_?3|Fourier--Mukai" chapters/theory/cy_to_chiral.tex
rg -n "pushforward.*envelope|envelope.*pushforward|commut|Fubini|Beck--Chevalley|where the factorisation-homology kernels are defined|functorial in the specialisation datum|exact .*SpCh|SpCh.*exact" chapters/theory/cy_to_chiral.tex
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1,125p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '218,286p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '518,620p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '620,805p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1260,1385p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '5388,5500p'
```

No tests or build were run; this was a read-only theorem-scope audit plus
the requested report write.
