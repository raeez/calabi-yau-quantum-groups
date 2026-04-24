# Agent 06: Francis-Gwilliam Factorization-Homology Examiner

Scope: CFG 2026 arXiv:2602.12412, Sections 1.1, 1.6-1.10, 2, and 4.5, against Vol III chain-level `\Phi_3`, the two-stage factorisation surfaces, and FRONTIER V3-F18/F27.

Owned file only: `notes/adversarial_swarm_20260424_cfg_e3/agent_06_francis_gwilliam_factorization_homology.md`.

## Sources read

Primary source:

- Costello-Francis-Gwilliam, *Chern-Simons factorization algebras and knot polynomials*, arXiv:2602.12412v1, submitted 2026-02-12.
- CFG sections read: 1.1, 1.6, 1.7, 1.8, 1.9, 1.10, 2, 4.5.

Local anchors:

- `FRONTIER.md:182`: V3-F18. CY-A_3 chain-level explicit for non-formal CY_3.
- `FRONTIER.md:212`: V3-F27 split, refined 2026-04-24.
- `FRONTIER.md:213`: CFG 2026 is ordinary 3d CS / knot-invariant source, not a 6d hCS source.
- `chapters/theory/cy_to_chiral.tex:222`: definition of `\PhiFA_d` and `\SpCh_{\Sigma_{d-1},C}`.
- `chapters/theory/cy_to_chiral.tex:243`: two-stage factorisation theorem.
- `chapters/theory/cy_to_chiral.tex:283`: three-step Stage-1 assembly and H1-H4.
- `chapters/theory/cy_to_chiral.tex:410`: `\SpCh` as factorisation-homology kernel.
- `chapters/theory/cy_to_chiral.tex:4692`: conditional framed object-level `d=3` theorem.
- `chapters/theory/cy_to_chiral.tex:4701`: chain-level `S^3`-framing hypothesis.
- `chapters/theory/cy_to_chiral.tex:4782`: status summary, residual issues.
- `chapters/theory/cy3_chain_level_bridge.tex:35`: typed CY3 bridge.
- `chapters/theory/cy3_chain_level_bridge.tex:227`: no CFG shortcut warning.
- `chapters/theory/cy3_chain_level_bridge.tex:247`: hCS-to-Hall open problem.
- `chapters/theory/en_factorization.tex:50`: Dunn-Lurie / `\SpCh` factorisation homology proposition.
- `chapters/theory/quantum_chiral_algebras.tex:20`: hCS observables as `E_3` Dolbeault-chiral CE algebra.
- `chapters/theory/quantum_chiral_algebras.tex:372`: chiral Chevalley-Eilenberg chains/cochains.
- `chapters/theory/quantum_chiral_algebras.tex:400`: bar complex as CE chains of a Lie conformal algebra.
- `chapters/theory/quantum_chiral_algebras.tex:3500`: `\Obs_{\hCS}(\mathbb C^3)` as `\CE^\bullet_{\bar\partial,\chir}`.
- `notes/wave12_f2_bv_brst_to_chiral_ce.tex:382`: 6d hCS BV complex and Dolbeault CE model.
- `notes/wave12_f2_bv_brst_to_chiral_ce.tex:443`: holomorphic chiral envelope on the transverse curve.
- `notes/wave12_f2_bv_brst_to_chiral_ce.tex:455`: bulk-to-boundary chiral CE pushforward.
- `notes/wave12_f2_bv_brst_to_chiral_ce.tex:466`: compact transverse fibres require genuine chiral lift, not simplification.
- `notes/wave12_u1_two_stage_functor.tex:1`: native holomorphic FA versus specialised chiral shadow.
- `notes/wave12_u1_two_stage_functor.tex:171`: CY-A_3 is one specialisation, not a universal theorem.

## Executive verdict

CFG proves a precise theorem for ordinary perturbative 3d Chern-Simons theory:

\[
  \int_{K\subset \mathbb R^3} \operatorname{tr}(V)
  =
  Z_V(K\subset \mathbb R^3)
\]

where BV quantization of 3d CS for a semisimple Lie algebra `\mathfrak g` and invariant pairing `\lambda` gives a filtered `E_3`-algebra `\mathcal A^\lambda`, and a finite-dimensional Drinfeld-Jimbo module gives a perfect `\mathcal A^\lambda`-module.

This theorem proves the trace and Morita mechanism for `E_3` topological factorization homology. It does not prove the CY3 chain-level functor `\Phi_3`, the 6d holomorphic Chern-Simons avatar, the hCS-to-critical-CoHA comparison, the K3 x E Borcherds output, or the K3 quantum toroidal algebra. It is an exact analogue and a formal test oracle, not a source theorem for Vol III CY3.

The correct Vol III use is:

\[
  \Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
  \SpCh_{\Sigma_2,C}\bigl(\PhiFA_3(\mathcal C)\bigr)
  =
  \left(\int_{\Sigma_2}\PhiFA_3(\mathcal C)\right)\bigm|_C,
\]

provided `\PhiFA_3(\mathcal C)` has already been constructed as a holomorphic `E_3` factorisation algebra and the `(\Sigma_2,C)` kernel is admissible. CFG supplies the trace formalism after this input exists. It does not construct that input.

Steering correction integrated: CFG's `C^*(\mathfrak g)` is only the locally constant / topological associated model. The Vol III CY3 avatar must not be collapsed to ordinary Lie cochains. The relevant object is the Dolbeault-chiral Chevalley-Eilenberg algebra in three holomorphic variables:

\[
  \Obs_{\hCS}(\mathbb C^3)
  \simeq
  \CE^\bullet_{\bar\partial,\chir}
  \bigl(\Omega^{0,\bullet}_c(\mathbb C^3,\mathfrak g)[1],\mathcal O_{\mathbb C^3}\bigr),
\]

with holomorphic jets in `z_1,z_2,z_3`, multidirectional OPE/factorisation over polydiscs, and `E_3` composition over configuration spaces of polydiscs. The Stage-2 comparison must pass through

\[
  \text{Dolbeault BV/BRST}
  \to
  \CE^\bullet_{\bar\partial,\chir}
  \to
  \mathfrak L_C
  \to
  U^{\mathrm{ch}}(\mathfrak L_C)
  \to
  \bar B(U^{\mathrm{ch}}(\mathfrak L_C))\simeq \chCE_*(\mathfrak L_C),
\]

before any CFG-style trace class is formed.

## CFG theorem import

What CFG proves:

- `E_3` source: BV quantization of ordinary 3d Chern-Simons on `\mathbb R^3` gives a filtered `E_3`-algebra deforming `C^*(\mathfrak g)`.
- Deformation class: the deformation problem is controlled by `\hbar H^3(\mathfrak g)[[\hbar]]`; for simple `\mathfrak g`, `H^4(\mathfrak g)=0` removes the obstruction and `H^3(\mathfrak g)` supplies the level parameter.
- Category bridge: perfect modules over the `E_3` algebra form an `E_2`-monoidal category, identified through filtered Koszul duality with finite-dimensional representations of `\mathfrak g`, and then with Drinfeld-Jimbo quantum-group representations after deformation.
- Trace bridge: for an `E_n`-algebra `A` and perfect `A`-module `V`, the trace class
  \[
    \operatorname{tr}(V)\in HH_*(A)^{\otimes \pi_0K}
    \simeq
    \int_{K\times \mathbb R^{n-1}} A
  \]
  maps along `K x R^{n-1} -> M` to an element of `\int_M A`.
- Stratified/Morita mechanism: an `E_{1\subset n}` coefficient system plus a perfect bimodule gives a natural map from stratified factorization homology to ordinary `\int_M A`.
- Nontriviality of the `E_3` deformation: Section 4.5 verifies it by (i) pushforward along `T^2 x R -> R`, producing a noncommutative `E_1` deformation, and (ii) a direct `P_3` bracket computation. To first order in `\hbar`, the `-2`-shifted Poisson bracket on `C^*(\mathfrak g)[[\hbar]]` is determined by `\lambda mod \hbar` on linear observables.

What CFG does not prove:

- no 6d holomorphic Chern-Simons construction on a complex CY3;
- no holomorphic `\PhiFA_3(\mathcal C)` for a CY3 category;
- no `\Theta_{\hCS\to\Hall}` from hCS observables to oriented critical CoHA;
- no `CoHA(\mathbb C^3)=Y^+` theorem;
- no Drinfeld double or `\mathcal W_{1+\infty}` evaluation theorem;
- no K3 x E Borcherds/Gritsenko denominator output;
- no K3 quantum toroidal `U_{q,t}(\widehat{\widehat{\mathfrak g}_{K3}})`;
- no arbitrary CY3 morphism functoriality or global quantum vertex group `G(\mathcal C)`.

## Exact CY3 avatar dictionary

| CFG object | Vol III avatar | Status |
|---|---|---|
| ordinary 3d CS observables `\Obs^\lambda` on `\mathbb R^3` | 6d hCS / holomorphic `E_3` observables on complex CY3 `X` | analogous only; source is Costello-Li / Costello-Gwilliam-Li, not CFG |
| filtered `E_3` algebra deforming `C^*(\mathfrak g)` | the locally constant associated model of the true CY3 object | useful only after forgetting Dolbeault/chiral data |
| topological cochains `C^*(\mathfrak g)` | Dolbeault-chiral CE `\CE^\bullet_{\bar\partial,\chir}(\Omega^{0,\bullet}_c(X,\mathfrak g)[1],\mathcal O_X)` | required Vol III avatar |
| binary operations of little 3-disks | multidirectional OPE/factorisation over holomorphic polydiscs in `z_1,z_2,z_3` | must be retained before pushforward |
| filtered `E_3` deformation | `\PhiFA_3(\mathcal C)` built from Hochschild/Gerstenhaber data, Dolbeault CE, chiral envelope, and holomorphic locality | conditional on H1-H4 and chain-level framing data |
| framed link `K\subset M` | admissible Stage-2 datum `(\Sigma_2,C)` | not the same category: CFG uses real framed links; Vol III uses holomorphic pushforward/specialisation kernels |
| `\int_{K\subset M}\operatorname{tr}(V)` | `(\int_{\Sigma_2}\PhiFA_3(\mathcal C))|_C` and later traces/characters of the specialised chiral algebra | formal mechanism, not output identification |
| perfect `A`-module `V` | line/defect module or representation of the specialised `E_1` chiral algebra | unconstructed in general |
| RT invariant `Z_V(K)` | Borcherds denominator, Hall character, BPS/CoHA trace, or quantum-toroidal character | case-by-case; no CFG theorem gives these |
| `P_3` bracket from pairing `\lambda` | CY3 Gerstenhaber/BV bracket from the CY trace and shifted symplectic structure | analogous degree `-2`; formula is different |

## Attack-heal cycles

### Cycle 1: CFG as a direct proof of `\PhiFA_3`

Attack: One might cite CFG to claim that `\PhiFA_3(\mathcal C)` exists for CY3 categories because CFG constructs a filtered `E_3` algebra by BV quantization.

Failure mode: CFG starts with ordinary 3d Chern-Simons for a semisimple finite-dimensional `\mathfrak g` on `\mathbb R^3`; the local algebra is a deformation of `C^*(\mathfrak g)`. That is the locally constant associated model after forgetting holomorphic jets and chiral OPE data. Vol III starts with a CY3 category `\mathcal C`, Hochschild/Gerstenhaber data, a holomorphic CY3 target `X`, Dolbeault fields in `z_1,z_2,z_3`, and a chain-level `S^3`-framing hypothesis. The inputs and the retained structures are different.

Heal: CFG may be cited as the ordinary 3d CS analogue and as a model for what a finished `E_3` trace theorem should look like after passing to a locally constant model. The construction of `\PhiFA_3` must continue to rest on Kontsevich-Tamarkin, Costello-Gwilliam-Li, Costello-Li hCS, the Dolbeault-chiral CE model, and the H1-H4 framed object-level theorem in `cy_to_chiral.tex`.

Verdict: CFG does not close Stage 1. Status remains conditional for `\PhiFA_3` at `d=3` outside the verified object-level loci.

### Cycle 2: CFG pushforward as a proof of `\SpCh_{\Sigma_2,C}`

Attack: CFG Section 4.5 pushes factorization algebras along `\pi:T^2 x R -> R`; therefore `\SpCh_{\Sigma_2,C}` follows by the same pushforward argument.

Failure mode: CFG's pushforward is ordinary topological factorization algebra pushforward:
\[
  \pi_*\mathcal F(U)=\mathcal F(\pi^{-1}U).
\]
It proves that compactifying ordinary CS along a real torus produces a noncommutative `E_1` deformation. Vol III's `\SpCh_{\Sigma_2,C}` is a holomorphic/categorical kernel, often with `\Sigma_2=K3` and `C=E`. That is not a framed real 2-torus calculation. A literal import also risks a dimension mismatch: CFG works in real framed manifolds, while Vol III's `\Sigma_2` is a complex surface in a complex threefold.

Heal: Read `\SpCh_{\Sigma_2,C}` as the Vol III holomorphic pushforward kernel applied to the Dolbeault-chiral CE / chiral-envelope object
\[
  \bigl((\pi_C)_*(\pi_X^*\mathcal F\otimes^{\mathbb L}\mathcal O_{\Sigma_2\times C})\bigr)^{E_1},
\]
not as a direct CFG `T^2` reduction. The proof obligation is an admissibility theorem for the holomorphic kernel, the Dolbeault pushforward, and the multidirectional factorization products over polydiscs.

Verdict: CFG supports the pushforward grammar. It does not prove the K3-fibre specialisation. The local Vol III kernel proposition remains the relevant anchor; its CY3 applications inherit the H1-H4 and hCS-to-Hall gates.

### Cycle 3: CFG trace as a proof of CY3 chiral characters

Attack: Since CFG proves the factorization-homology trace equals the RT invariant, the CY3 specialised trace should equal the Borcherds denominator or the quantum-toroidal character.

Failure mode: CFG's trace theorem requires a perfect `A`-module `V` and a framed link `K`. The output is an RT link invariant for a Drinfeld-Jimbo quantum group representation. The Borcherds denominator, K3 x E BKM algebra, and quantum toroidal characters require different representation data: Hall/CoHA state spaces, BKM root multiplicities, orientation data, and Drinfeld doubling. CFG supplies none of these.

Heal: The right Vol III theorem form is conditional and CE-to-chiral:

1. construct the Dolbeault-chiral CE object with holomorphic jets in `z_1,z_2,z_3`;
2. pass to the Lie conformal algebra on the reference curve through the holomorphic pushforward;
3. apply the chiral envelope `U^{\mathrm{ch}}`;
4. use `\bar B(U^{\mathrm{ch}}(\mathfrak L_C))\simeq \chCE_*(\mathfrak L_C)` to locate the trace complex;
5. construct perfect modules or trace-class defects for `A_{\mathcal C}^{(\Sigma_2,C)}`;
6. identify their characters by independent Hall/Borcherds/automorphic input.

Verdict: CFG trace formalism is importable only after the CY3 chiral algebra and its perfect modules are built. It does not identify the exact CY3 chiral avatar.

### Cycle 4: CFG `P_3` bracket as the CY3 chain-level bracket

Attack: CFG Section 4.5 computes the `P_3` bracket; this should be the missing chain-level CY3 bracket in `\PhiFA_3`.

Failure mode: CFG's bracket is the first-order `-2`-shifted Poisson bracket on `C^*(\mathfrak g)[[\hbar]]`, determined by the invariant pairing `\lambda` on linear observables. CY3 `\PhiFA_3` uses the Gerstenhaber bracket of degree `-2` on Hochschild cochains, the CY trace pairing, the BV operator on cyclic chains, and the holomorphic volume form. The degree agrees; the complex and pairing do not.

Heal: Use CFG 4.5 as a normal-form test: a valid CY3 analogue should exhibit the corresponding `S^2` descent operation and show how the CY pairing supplies the degree `-2` bracket. The formula must be written in Hochschild/BV/Dolbeault-chiral CE variables, with fields in `\Omega^{0,\bullet}(X,\mathfrak g)[1]`, not copied from ordinary `C^*(\mathfrak g)`.

Verdict: CFG proves a bracket template, not the CY3 bracket formula. The chain-level `S^3`-framing and hCS-to-Hall comparison remain separate.

### Cycle 4b: ordinary CE collapse versus Dolbeault-chiral CE avatar

Attack: Replace the CY3 avatar by ordinary `C^*(\mathfrak g)` because CFG does so locally.

Failure mode: This erases the very data that makes Vol III CY3 rather than topological CS: holomorphic jets in three variables, the Dolbeault differential `\bar\partial`, Bochner-Martinelli / heat-kernel OPE kernels, polydisc factorization, and the chiral envelope. Ordinary `C^*(\mathfrak g)` is the locally constant shadow after forgetting these structures.

Heal: The avatar is the many-variable Dolbeault-chiral CE object
\[
  \CE^\bullet_{\bar\partial,\chir}
  \bigl(\Omega^{0,\bullet}_c(X,\mathfrak g)[1],\mathcal O_X\bigr),
\]
then its pushforward to a curve produces a Lie conformal algebra `\mathfrak L_C`, then `U^{\mathrm{ch}}(\mathfrak L_C)` is the factorization algebra whose bar is the chiral CE chain complex. The trace/pushforward comparison must be formulated at this level. The ordinary CE complex is allowed only as an associated graded / locally constant test model.

Verdict: Add a hard guardrail: never identify the CY3 avatar with ordinary `C^*(\mathfrak g)` except after explicitly naming the forgetful functor to the locally constant associated model.

### Cycle 5: CFG braided category as native `E_2` at `d=3`

Attack: CFG obtains a braided monoidal category from perfect modules over an `E_3` algebra; therefore the CY3 chiral algebra should be natively `E_2`-chiral.

Failure mode: CFG obtains an `E_2`-monoidal module category from an `E_3` algebra. Vol III's `d=3` output on the curve is explicitly `E_1`-chiral; the nonsymmetric `E_2` braiding appears through the Drinfeld center of the `E_1` representation category, not as native structure on the chiral algebra. This is the `n_{\mathrm{native}}(3)=1` discipline.

Heal: The CY3 avatar of CFG's braided category is:
\[
  \mathcal Z(\operatorname{Rep}^{E_1}(A_{\mathcal C}))
\]
not an `E_2` enhancement of `A_{\mathcal C}` itself.

Verdict: Keep `d=3` output `E_1`. CFG reinforces the module-category route to braiding; it does not overturn `E_1` stabilisation.

### Cycle 6: CFG as a bypass of V3-F18/F27

Attack: CFG factorization homology might bypass CY-A_3 and construct the 6d hCS / K3 quantum toroidal pipeline directly.

Failure mode: FRONTIER already separates the issue. V3-F18 remains the chain-level CY-A_3 explicit problem for non-formal CY3 categories. V3-F27a is the 6d hCS construction on `\mathbb C^3`; V3-F27b is K3 quantum toroidal and is gated on CY-A_3 data. CFG is explicitly classified in `FRONTIER.md:213` as a 3d CS / knot-invariant source, not a 6d hCS source.

Heal: CFG can reorganize the obstruction language: if a 6d hCS avatar is constructed, its observables should be an `E_3` factorization algebra and should admit CFG-style pushforward, trace, and Morita tests. It does not remove the need to construct the 6d hCS avatar, the `\Theta_{\hCS\to\Hall}` map, or the CY3 chiral sewing/OPE completion.

Verdict: No bypass. F18 and F27 remain correctly scoped.

## Status recommendations

1. `CFG -> \PhiFA_3`: mark as **analogy / formal test oracle**, not source theorem.
2. `C^*(\mathfrak g)`: treat as **locally constant associated model only**. The CY3 object is Dolbeault-chiral CE in three holomorphic variables.
3. `\PhiFA_3`: require the passage
   \[
     \Omega^{0,\bullet}(X,\mathfrak g)[1]
     \to
     \CE^\bullet_{\bar\partial,\chir}
     \to
     \mathfrak L_C
     \to
     U^{\mathrm{ch}}(\mathfrak L_C)
   \]
   before any trace statement.
4. `\SpCh_{\Sigma_2,C}`: retain as **factorization-homology / holomorphic pushforward kernel** only when the holomorphic admissibility data are named. For K3 x E, avoid any wording that makes it a direct CFG `T^2` pushforward.
5. `\int_{\Sigma_2}` over K3: if meant literally as topological factorization homology, specify real framing and dimension conventions. If meant holomorphically, say "holomorphic pushforward / chiral homology kernel" rather than relying on CFG framed-manifold language.
6. `hCS -> Hall`: keep **open**. The required map is `\Theta_{\hCS\to\Hall}^{or}` in `cy3_chain_level_bridge.tex`.
7. `CoHA(\mathbb C^3)`: keep `CoHA(\mathbb C^3)=Y^+`; `\mathcal W_{1+\infty}` appears only after Drinfeld double / center / Fock evaluation.
8. `K3 x E`: CFG does not prove `\SpCh_{K3,E}(\PhiFA_3)=\mathbf H_{\Delta_5}`. That identification remains conditional on the hCS-to-Hall and Borcherds comparison data.
9. V3-F18: CFG does not close chain-level `S^3`-framing for arbitrary non-formal CY3. It supplies a model for packaging chain data into BV observables after the Dolbeault-chiral CE object is built.
10. V3-F27: current split is correct. CFG is not a 6d hCS source; F27a is a 6d hCS avatar construction, F27b is K3 quantum toroidal gated on CY-A_3 data.

## Files changed

- Added this report only.

No manuscript files edited.

## Verification

- Read CFG arXiv source directly from arXiv e-print.
- Read local Vol III anchors listed above.
- Ran targeted verification:

```bash
pytest compute/tests/test_cfg25_adversarial_consistency.py compute/tests/test_qg_from_fh_3d_6d.py -q
```

Result: `135 passed in 0.39s`.

## Remaining open questions

1. Write a standalone holomorphic `\SpCh_{\Sigma_2,C}` admissibility lemma separating ordinary real framed factorization homology from holomorphic pushforward along complex surfaces.
2. Construct `\Theta_{\hCS\to\Hall}^{or}` with orientation data, Tate shifts, completions, Thom-Sebastiani compatibility, and overlap coherences.
3. For K3 x E, specify the perfect modules or trace-class defect objects whose CFG-style trace should be compared with the Borcherds denominator.
4. For `\mathbb C^3`, exhibit the CY3 `S^2` descent bracket in Hochschild/BV/Dolbeault-chiral CE variables and compare it with CFG's `C^*(\mathfrak g)` calculation only after naming the forgetful functor to the locally constant model.
5. Write the many-variable CE-to-chiral CE passage explicitly: holomorphic jets in `z_1,z_2,z_3`, OPE kernels over polydiscs, Lie conformal algebra on the reference curve, and `U^{\mathrm{ch}}` envelope.
6. Decide whether the phrase "factorization homology over K3" should be replaced everywhere, in theorem statements, by the holomorphic kernel expression unless a real framed model is actually supplied.
