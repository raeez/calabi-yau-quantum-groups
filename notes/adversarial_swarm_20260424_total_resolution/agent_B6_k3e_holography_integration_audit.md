# Agent B6: K3 x E Hall-Borcherds and holography integration audit

## Scope

Audited files:

- `chapters/examples/k3e_bkm_chapter.tex`
- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/cy3_chain_level_bridge.tex`
- `chapters/connections/cy_holographic_datum_master.tex`
- `notes/adversarial_swarm_20260424_total_resolution/agent_A6_k3e_hb_holography.md`

No manuscript source was edited.

## Verdict

The main K3 x E algebra lane is mostly fenced correctly after the A6 integration:

- `Delta_5` is the primitive BKM denominator, with `kappa_BKM(Delta_5)=5`.
- `Phi_10 = const * Delta_5^2` is the dyonic / reduced-DT square, with weight `10`.
- `thm:g-delta5-is-sp-k3` is conditional.
- `thm:g-delta5-sp-k3-bialgebra` is conditional.
- `thm:plat-Sp-K3E` is now conditional on the K3-fibre Hall-Borcherds comparison datum.
- The holography/QG gate exists and is mathematically well typed.

Five overclaim or normalization anchors remain. Two are substantive and should be repaired before the manuscript claims an integrated closure.

## Positive Checks

### Delta_5 / Phi_10 normalization

The local convention is correct at `chapters/examples/k3e_bkm_chapter.tex:470-472`:

```tex
Delta_5: Borcherds lift of phi_{0,1}, weight 5.
Phi_10: Borcherds lift of 2 phi_{0,1}, weight 10.
Phi_10 = const * Delta_5^2.
```

The same normalization is correctly reflected in A6:

- `agent_A6_k3e_hb_holography.md:13-35`: primitive denominator versus dyonic square.
- `agent_A6_k3e_hb_holography.md:152-184`: primitive chiral half controlled by `Delta_5^{-1}`, physical genus-2 BPS trace by `Phi_10^{-1}`.

### Conditional Hall-Borcherds closure in `cy_to_chiral`

`chapters/theory/cy_to_chiral.tex:947-955` states `thm:g-delta5-is-sp-k3` as conditional on Problem `op:cy3-hcs-hall-comparison` and the K3-fibre Hall-Borcherds comparison.

`chapters/theory/cy_to_chiral.tex:988-1008` states the bialgebra enhancement as conditional on:

- `thm:g-delta5-is-sp-k3`;
- the oriented hCS-to-Hall comparison;
- Hall-Borcherds coproduct / associator / R-matrix comparisons.

This is the correct status.

### Conditional status of `thm:plat-Sp-K3E`

`chapters/examples/k3e_bkm_chapter.tex:12141-12152` is repaired:

- line `12143`: `\ClaimStatusConditional`;
- lines `12149-12152`: the displayed decomposition is explicitly under the oriented hCS-Hall map, witnessed K3-fibre specialisation, Hall-Drinfeld completion, Borcherds denominator comparison, and transported coproduct/associator/R data.

This no longer asserts an unconditional non-abelian BPS/Borcherds algebra decomposition.

### Holography/QG gate

`chapters/connections/cy_holographic_datum_master.tex:463-565` is correctly fenced. The `Holographic bridge gate` says physical arguments transfer to CY-to-chiral theorem statements only after the product comparison, orientation-line compatibility, and wall-crossing coherence are present.

`chapters/theory/cy3_chain_level_bridge.tex:1581-1658` also contains the correct protected-physics fence: holographic, black-hole, and QG statements become theorems only after the protected physical comparison datum is supplied.

## Remaining Overclaim Anchors

### B6-1. Substantive: K3 x E hCS-to-Hall map is asserted later as globally constructed

Anchor:

- `chapters/theory/cy3_chain_level_bridge.tex:2396-2420`
- `chapters/theory/cy3_chain_level_bridge.tex:2479-2508`

Problem:

`thm:r6-k3e-local-chart-qiso-inscribed` states that, on a DWR cover of `K3 x E`, chartwise quasi-isomorphisms

```tex
Theta_i : Obs_hCS^q(U_i; ghat) -> CoHA_crit^or(U_i)
```

are compatible on all overlaps, all five obstruction classes vanish, and hence a global morphism

```tex
Theta_{hCS->Hall}^{K3 x E}
```

exists. The follow-up status remark at lines `2482-2508` says all seven conditions of Problem `op:cy3-hcs-hall-comparison` hold on the DWR cover.

This conflicts with the A1/A6 conclusion: the current manuscript has an obstruction formalism and local/toric normal forms, but not an independently constructed global oriented hCS-to-Hall comparison for compact `K3 x E`. Conditioning only on "DWR cover and abelian ghat" is not enough; the missing datum is precisely the comparison map plus its overlap/orientation/TS/factorisation coherences.

Recommended repair:

Restate this as a criterion conditional on supplying the chartwise comparison maps and all overlap homotopies, or restrict it to the already verified affine toric `C^3` / explicitly witnessed toric chart locus. It should not be used as the proof that `Theta_{hCS->Hall}^{or}` exists for compact `K3 x E`.

### B6-2. Substantive: holographic datum master opener outruns the bridge gate

Anchor:

- `chapters/connections/cy_holographic_datum_master.tex:2288-2304`

Problem:

The K3-base opener says the CY holographic datum master "transports through the CY-to-chiral functor `Phi`" to the chiral holographic datum master, then asserts that the six-tuple master equation holds jointly on both sides.

This outruns the gate at `chapters/connections/cy_holographic_datum_master.tex:504-565`. The transport to `mathbf H_{Delta_5}` requires the same missing Hall-Borcherds and protected comparison data; without them it is a conditional diagram, not an established transport theorem.

Recommended repair:

Make the opener conditional on the complete pure mathematical holographic bridge datum and the Hall-Borcherds bialgebra datum, or rewrite it as the target diagram expected after those data are supplied.

### B6-3. Normalization error: `Phi_10` of weight 5

Anchor:

- `chapters/examples/k3e_bkm_chapter.tex:12435`

Problem:

The proof chain says:

```tex
Borcherds 1998 lifts 2 phi_{0,1} ... to Phi_10 of weight 5
```

This contradicts the local convention at `k3e_bkm_chapter.tex:470-472` and A6. The primitive half has weight `5`:

```tex
Bor(phi_{0,1}) = Delta_5,  wt(Delta_5)=5.
```

The doubled K3 elliptic genus gives the square:

```tex
Bor(2 phi_{0,1}) = Phi_10 = const * Delta_5^2,  wt(Phi_10)=10.
```

Recommended repair:

Replace the line with the primitive/square distinction above.

Related caution:

`chapters/examples/k3e_bkm_chapter.tex:12439` says the Borcherds-product expansion of `Delta_5^2` identifies `c_K3(nm,l)` with `mult_{g_{Delta_5}}(alpha)`. That line needs the same primitive/square separation: primitive root multiplicities belong to the `Delta_5` denominator; the reduced-DT / DVV trace is the square.

### B6-4. Normalization error: `c_1(0)/2` placed on `Phi_10`

Anchor:

- `chapters/connections/cy_holographic_datum_master.tex:1627-1629`

Problem:

The line says:

```tex
kappa_BKM = 5 (from the Borcherds weight c_1(0)/2 on Phi_10)
```

This is the exact false formula A6 repaired elsewhere. The `5` is `c_1(0)/2` for the primitive `Delta_5` input. In the Igusa-square convention, `Phi_10` has weight `10`.

Recommended repair:

Write "from the Borcherds weight `c_1(0)/2` on `Delta_5`; the square `Phi_10=Delta_5^2` has weight `10`."

### B6-5. Minor wording risk: conditional theorem described as already identifying the associator class

Anchor:

- `chapters/theory/cy_to_chiral.tex:1048`

Problem:

The paragraph says "The proof of Theorem `thm:g-delta5-sp-k3-bialgebra` identifies..." the transported formality cocycle with the `Phi_10/eta^24` line. The theorem and proof immediately below are conditional and correctly say the transport/non-vanishing is open.

Recommended repair:

Change the setup sentence to "Under the hypotheses of Theorem..." or "The conditional theorem requires..." so the prose matches the theorem status.

## Holography/QG Status

No broad QG theorem is established by the audited text alone.

Allowed theorem-grade lane:

- arithmetic identities for `Delta_5`, `Phi_10`, and `kappa_BKM=c(0)/2`;
- character-level / index-level statements about `1/Phi_10` where backed by Oberdieck-Pixton / reduced DT / Rademacher results;
- conditional transfer results after the complete bridge datum is supplied.

Still conditional:

- compact `K3 x E` hCS-to-Hall comparison;
- Hall-Drinfeld double identification with the BKM target;
- coproduct, associator, and R-matrix transport;
- protected AdS / black-hole / QG interpretation as a theorem of the CY-to-chiral programme.

## Final Status Recommendation

Keep:

- `thm:g-delta5-is-sp-k3`: conditional.
- `thm:g-delta5-sp-k3-bialgebra`: conditional.
- `thm:plat-Sp-K3E`: conditional as patched.
- holography/QG claims: conditional on the bridge datum, except for arithmetic/index statements.

Repair before claiming closure:

1. The late `cy3_chain_level_bridge.tex` R6 K3 x E global `Theta` theorem/status remark.
2. The K3-base holographic datum opener.
3. The two remaining `Phi_10`/`Delta_5` normalization slips.

No tests were run for this audit; it was a local source-status and normalization pass.
