# Agent A3: SpCh and Phi_3 functoriality

Date: 2026-04-24

Scope: adversarial audit of `SpCh_{\Sigma_2,C}` beyond verified loci and
morphism-level functoriality of `\Phi_3`, with emphasis on
pushforward/envelope commutation and arbitrary CY3 Fourier--Mukai
functoriality.

## Verdict

The framed object-level construction survives:

`Phi_3^{(\Sigma_2,C)}(\mathcal C) =
SpCh_{\Sigma_2,C}(PhiFA_3(\mathcal C))` is a theorem on the stated
H1--H4 locus after a fixed admissible specialisation datum and the
Stage-1 witnesses are supplied. This is the content of
`chapters/theory/cy_to_chiral.tex:5060`--`5123`, reinforced by
`chapters/theory/cy3_chain_level_bridge.tex:679`--`716` and the scope
restriction at `chapters/theory/cy3_chain_level_bridge.tex:786`--`814`.

The following stronger readings do not survive:

1. arbitrary CY3 Fourier--Mukai kernels inducing `Phi_3` morphisms;
2. automatic commutation of Stage-2 pushforward with the factorisation
   envelope or Costello--Li holomorphic refinement;
3. automatic naturality of the Hall/CoHA/stable-envelope side under
   arbitrary kernels;
4. global hocolim/exactness for the CY3 construction outside the
   separately verified toric/Hall and framed object-level loci.

The repair is not to weaken the verified loci. The repair is to replace
"admissible datum" by a witnessed admissible datum and to require the
exact Beck--Chevalley, Fubini, orientation, and cyclic-functoriality
lemmas listed below.

## Attacked Claims

### A. "Admissible specialisation datum" is underdetermined

Anchors:

- `chapters/theory/introduction.tex:109`--`116`
- `chapters/theory/cy_to_chiral.tex:237`--`245`
- `chapters/theory/cy_to_chiral.tex:420`--`437`
- `chapters/theory/cy_to_chiral.tex:458`--`466`

Attack: the current local definition says "closed cycle for which
factorisation-homology pushforward is defined" plus a reference curve.
That is a useful shorthand, but it is not enough for the advertised
kernel formula or for morphism functoriality. A complex surface
`Sigma_2` can fail properness, transversality to the reference curve,
normal-orientation compatibility, or analytic finiteness; a
Fourier--Mukai kernel can move or mix the fixed `Sigma_2` datum.

Survives: the K3-fibre datum on `K3 x E`, the named toric/formal loci,
and any datum where the factorisation-homology kernel, restriction to
`C`, and compact-support conventions are explicitly witnessed.

Missing repair: define "witnessed admissible CY3 specialisation datum"
as data, not a property.

### B. `SpCh` as exact functor is true only after the factorisation-homology kernel exists

Anchors:

- `chapters/theory/cy_to_chiral.tex:537`--`553`
- `chapters/theory/cy_to_chiral.tex:556`--`575`

Attack: Proposition `prop:spch-infty1-kernel` is safe if read literally:
"For an already constructed `E_d`-holomorphic factorisation algebra and
an admissible specialisation datum." The problem is the proof of
`thm:phi-two-stage-derived`, especially
`chapters/theory/cy_to_chiral.tex:575`, which says hocolim preservation
and exactness are inherited from both factors. That sentence is too
strong at `d = 3` unless read through the caveat at
`chapters/theory/cy_to_chiral.tex:571`: arbitrary CY3 morphism
functoriality, hocolim preservation, and global exactness remain
conjectural unless separately verified.

Survives: exactness of Stage 2 as a functor on already constructed
hFAs and witnessed admissible kernels; the composite as an object-level
definition on the framed CY3 locus.

Missing repair: a CY3-specific projection-formula/Beck--Chevalley lemma
for holomorphic factorisation cosheaves with the chosen incidence
kernel `O_{Sigma_2 x C}`.

### C. Pushforward/envelope commutation is not automatic

Anchors:

- `chapters/theory/cy_to_chiral.tex:196`--`204`
- `chapters/theory/cy3_chain_level_bridge.tex:652`--`677`
- `chapters/theory/cy3_chain_level_bridge.tex:679`--`745`
- `chapters/theory/cy3_chain_level_bridge.tex:786`--`814`

Attack: the chain-level bridge proves the left end:
`PhiFA_3(\mathcal C)_F ~= Hol_{X,Omega_X}(U^FA(HH^*(\mathcal C)_F))`. It does not prove
that integrating over `Sigma_2` commutes with `U^FA`, with the
Costello--Li holomorphic refinement, or with renormalised BV
propagators. The scope remark explicitly says object level, not
morphism level; compact non-affine targets have an anomaly gate; and the
CoHA side is not reached.

Survives: `SpCh` may be applied after the hFA has been constructed.
No theorem needs pushforward/envelope commutation if `SpCh` is treated
as Stage 2 on an already constructed Stage-1 object.

Missing repair: a Fubini/envelope lemma:

`int_{Sigma_2} Hol_{X,Omega_X}(U^FA(A))`
is equivalent to the holomorphic curve-level envelope obtained after
integrating the `E_3` algebra in the `Sigma_2` directions, with compact
support, anomaly, and propagator choices matching. This must be a
specified 2-cell, not a slogan.

### D. Arbitrary CY3 Fourier--Mukai functoriality fails without extra hypotheses

Anchors:

- `chapters/theory/cy_to_chiral.tex:515`--`534`
- `chapters/theory/cy_to_chiral.tex:993`--`1040`
- `chapters/theory/cy_to_chiral.tex:1064`--`1083`
- `chapters/theory/cy3_chain_level_bridge.tex:795`--`799`

Attack: the kernel formula in `prop:phifa-infty1-kernel` is explicitly
conditional on the functoriality conjecture. A Fourier--Mukai kernel
does not automatically preserve:

- the negative-cyclic CY class;
- the chosen `GRT_1(Q)` formality point;
- the chain-level `S^3` framing homotopy;
- the Costello--Li anomaly-cancellation witness;
- the analytic completion/sewing choices;
- the fixed `(\Sigma_2,C)` datum.

Even if it gives a derived equivalence of `Perf`, it need not define a
morphism between the specialised chiral shadows. It may move the cycle,
mix K3 and elliptic factors, or fail to preserve the line-defect/Brauer
twisting.

Survives: conditional morphism functoriality for kernels preserving all
framed data and for which the derived-centre convolution is constructed,
as in `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:3930`
--`3975`.

Missing repair: a morphism of witnessed admissible data, not merely a
Fourier--Mukai kernel.

### E. Stable-envelope/Hall naturality is a separate theorem

Anchors:

- `chapters/theory/cy_to_chiral.tex:8973`--`8990`
- `chapters/theory/cy3_chain_level_bridge.tex:198`--`260`
- `chapters/theory/cy3_chain_level_bridge.tex:325`--`360`

Attack: Maulik--Okounkov stable envelopes are chamber-, polarization-,
slope-, and torus-data dependent. Oriented critical CoHAs require
vanishing cycles, Thom--Sebastiani coherences, Tate shifts, and
orientation local systems. A Fourier--Mukai kernel preserving the
derived category does not automatically preserve this package. The
typed bridge makes the missing arrow explicit:
`PhiFA_3(\mathcal C) --> CoHA_crit(X)` is open in general.

Survives: the proved `C^3` Hall-side positive-half theorem and the
conditional toric descent package under an oriented comparison map on
the full DWR Cech/Ran nerve.

Missing repair: Hall naturality under the same morphism of witnessed
admissible data, including orientation, chamber, stable-envelope pairing,
and completion compatibility.

### F. Borcherds pushforward/banding compatibility is not general `Phi_3` functoriality

Anchors:

- `chapters/theory/cy_to_chiral.tex:9796`--`9830`
- `chapters/theory/cy_to_chiral.tex:9883`--`9940`

Attack: the K3/K3xE Borcherds pushforward statements live over a
banded framed locus and after the Borcherds pushforward has put both
sides in the same target. They do not supply arbitrary `Phi_3`
morphism functoriality. In particular, the claimed gerbe monomorphism
requires the banding pullback, line-defect twisting, and
`Phi^{Borch}_*` compatibility as part of the datum.

Survives: the K3-fibred banded comparison on the stated framed locus.

Missing repair: a naturality lemma for Borcherds pushforward with
respect to the same admissible-data morphisms.

## Strongest Admissible-Datum Theorem

The true theorem should be stated with the following data.

**Witnessed CY3 specialisation datum.** For a smooth CY3 target `X`,
a smooth proper CY3 category `\mathcal C`, and a curve `C_0`, a witnessed
datum is:

1. a Stage-1 witness: negative-cyclic CY class, formality point
   `F in Form_3(Q)`, chain-level `S^3` framing, Costello--Li
   holomorphic witness, anomaly cancellation, and completion;
2. a compact or properly supported complex surface/cycle
   `Sigma_2 subset X` with oriented/tubular normal data and compact
   support convention;
3. a smooth reference curve `i:C_0 -> X` and an incidence kernel
   `O_{Sigma_2 x C_0}` whose projections satisfy properness,
   Tor-independence, and the projection formula in the holomorphic
   factorisation-cosheaf category;
4. a factorisation-homology pushforward
   `int_{Sigma_2}` on the chosen Weiss/DWR basis;
5. a Beck--Chevalley 2-cell identifying pushforward then restriction
   with the kernel formula for `SpCh`;
6. if a Hall or Borcherds comparison is invoked, orientation data,
   vanishing-cycle normalisation, chamber/polarisation/slope data, and
   the relevant pushforward/banding compatibility.

**Theorem.** Given such a witnessed datum on the verified Stage-1 CY3
locus, the composite

`Phi_3^{(Sigma_2,C_0)}(\mathcal C) =
SpCh_{Sigma_2,C_0}(PhiFA_3(\mathcal C)_F)`

is a well-defined `E_1`-chiral algebra on `C_0`, exact and symmetric
monoidal in disjoint unions of witnessed specialisation cycles. If
`(K,eta)` is a morphism of witnessed data from
`(X,\mathcal C,Sigma_2,C_0)` to `(Y,\mathcal C',Sigma'_2,C'_0)` consisting of a cyclic
Fourier--Mukai/A_infty functor `K:\mathcal C -> \mathcal C'` plus coherences preserving
all witnesses above, then there is an induced `E_1`-chiral morphism

`Phi_3^{(Sigma_2,C_0)}(\mathcal C) -> Phi_3^{(Sigma'_2,C'_0)}(\mathcal C')`.

These morphisms compose up to the specified natural quasi-isomorphisms
only if the coherences are compatible with Fourier--Mukai convolution
and the `GRT_1(Q)`/framing torsor actions.

This theorem preserves the proved K3-fibred and toric/formal loci and
does not assert arbitrary CY3 morphism functoriality.

## Exact Missing Lemmas

1. **Cyclic Hochschild naturality.** A cyclic `A_infty` functor
   preserving the negative-cyclic CY class induces an `E_3`-algebra map
   on Hochschild cochains compatible with braces, BV, the chosen
   `GRT_1(Q)` formality point, and the `S^3` framing homotopy.

2. **Costello--Li naturality.** The holomorphic refinement
   `Hol_{X,Omega_X}` is natural under the allowed kernel, preserves the
   anomaly-cancellation class, and respects the analytic completion.

3. **Envelope/Fubini commutation.** The topological factorisation
   envelope and the holomorphic refinement commute with factorisation
   homology over `Sigma_2` under the stated properness and compact-support
   hypotheses.

4. **Specialisation Beck--Chevalley.** For a morphism of witnessed
   data, there is a coherent 2-cell

   `SpCh_{Sigma'_2,C'_0} o PhiFA_3(K)
    ~= K_C^{ch} o SpCh_{Sigma_2,C_0}`

   in `E_1-HolFA`, compatible with composition of kernels.

5. **Hall orientation naturality.** The hCS-to-Hall map, where invoked,
   is a continuous natural transformation on the full DWR Cech/Ran nerve
   and preserves orientation local systems, Thom--Sebastiani
   isomorphisms, shifts, twists, and completions.

6. **Stable-envelope naturality.** Stable-envelope pairings are preserved
   only under chamber/polarisation/slope-compatible morphisms; otherwise
   the discrepancy is an explicit wall-crossing `R`-matrix, not equality.

7. **Borcherds pushforward naturality.** `Phi_*^{Borch}` commutes with
   the admissible-data morphism and pulls back the gerbe banding cocycle
   as stated.

8. **Composition coherence.** The preceding 2-cells are associative for
   convolution of Fourier--Mukai kernels and respect identity kernels.

## Proof Outline for the Repaired Statement

1. Use Theorem `thm:cy-to-chiral-d3` to construct the Stage-1
   `PhiFA_3(\mathcal C)_F` on the H1--H4 locus.
2. Apply Proposition `prop:spch-infty1-kernel` only after the witnessed
   admissible datum supplies the factorisation-homology kernel and
   projection formula.
3. The `E_1` operadic level follows from the native-level calculation
   and Dunn restriction; the `E_2` braiding, when present, lives in the
   Drinfeld centre, not on the output algebra.
4. For morphisms, combine cyclic Hochschild naturality, Costello--Li
   naturality, envelope/Fubini commutation, and specialisation
   Beck--Chevalley. Without all four, there is no `Phi_3(K)`.
5. For Hall/Borcherds comparisons, add the orientation/stable-envelope
   and Borcherds-pushforward naturality lemmas. These are separate
   theorem inputs, not consequences of the object-level construction.

## File Anchors

- `chapters/theory/cy_to_chiral.tex:7`--`43`: headline two-stage scope.
- `chapters/theory/cy_to_chiral.tex:62`--`89`: CY-A3 object-level theorem.
- `chapters/theory/cy_to_chiral.tex:91`--`99`: object-level versus
  functor distinction.
- `chapters/theory/cy_to_chiral.tex:228`--`247`: `PhiFA_d` and `SpCh`
  definitions.
- `chapters/theory/cy_to_chiral.tex:515`--`534`: conditional
  Fourier--Mukai-type kernel.
- `chapters/theory/cy_to_chiral.tex:537`--`575`: `SpCh` kernel and
  composite exactness caveat.
- `chapters/theory/cy_to_chiral.tex:1075`--`1083`: per-d functoriality
  conjecture.
- `chapters/theory/cy_to_chiral.tex:5060`--`5123`: framed object-level
  `Phi_3` theorem.
- `chapters/theory/cy3_chain_level_bridge.tex:198`--`260`: typed
  hCS/Hall bridge and Hall target.
- `chapters/theory/cy3_chain_level_bridge.tex:679`--`716`: Stage-1
  envelope theorem.
- `chapters/theory/cy3_chain_level_bridge.tex:786`--`814`: envelope
  scope restrictions.
- `chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:3930`
  --`3975`: conditional categorical package preserving framed data.

## Files Changed

Only this report:

- `notes/adversarial_swarm_20260424_frontier_resolution/agent_A3_spch_functoriality.md`

No manuscript TeX files were modified.
