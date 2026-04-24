# CY3/CFG/E3 adversarial swarm synthesis

Date: 2026-04-24.

Scope: fifteen attack-heal reports on the chain-level construction of
`Phi` on CY3, the Stage-1 `E_3` holomorphic factorization algebra, and
the comparison with Costello--Francis--Gwilliam 2026,
arXiv:2602.12412.

## Convergence verdict

The swarm converged on a narrow theorem spine.

CFG 2026 is a theorem-grade source for ordinary real 3-dimensional
Chern--Simons: BV quantization gives a locally constant filtered `E_3`
factorization algebra, its classical local model is `C^*(g)`, and
perfect modules produce Reshetikhin--Turaev traces by factorization
homology.

That theorem is not the CY3 object.  The CY3 Stage-1 object keeps the
Dolbeault differential, the CY volume form, holomorphic jets in
`z_1,z_2,z_3`, polydisc factorization, many-variable residues,
orientation data, and the separate Hall comparison problem.

On a holomorphic polydisc `P=D_1 x D_2 x D_3`, the local normal form is
the Dolbeault/chiral CE package

```tex
\mathfrak L_{\mathcal C}(P)
  =
\Omega_c^{0,\bullet}
\bigl(P,J^\infty_{\mathrm{hol},z_1,z_2,z_3}
\mathfrak l_{\mathcal C}\bigr)[1],
\qquad
d_{\mathfrak L}=\bar\partial+d_{\mathfrak l},
```

```tex
\Obs_{\mathcal C}^{cl}(P)
  =
C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\mathfrak L_{\mathcal C}(P),\mathbb C\bigr),
```

and, where the hCS realization is available,

```tex
\Phi^{FA}_3(\mathcal C)|_P
  \simeq
U^{fact,E_3}_P(\mathfrak L_{\mathcal C}),
\qquad
B_{E_3}(\Phi^{FA}_3(\mathcal C)|_P)
  \simeq
CE^{ch,E_3}_*(\mathfrak L_{\mathcal C}).
```

The ordinary `C^*(g)` appears only after the locally constant shadow

```tex
\Omega^{0,\bullet}(P)\simeq\mathbb C,
\qquad
J^\infty_{\mathrm{hol}}\mathfrak l_{\mathcal C}
  \rightsquigarrow H^\bullet(\mathfrak l_{\mathcal C,x}),
```

and in the constant hCS chart this becomes `C^*(g)`.

## Claims killed

1. CFG proves `Phi^{FA}_3` for CY3.
2. `Phi^{FA}_3(C)=C^*(g)` before the locally constant shadow.
3. The final `d=3` chiral output is native `E_3` or native braided
   `E_2`.
4. The Dunn restriction `E_3 -> E_2` is the Yangian `R`-matrix.
5. CFG perfect modules are already CY3 Hall/BKM/DT modules.
6. CFG factorization traces imply Borcherds denominators, DT traces, or
   black-hole entropy without further comparison maps.
7. `Theta_{hCS->Hall}` follows from CFG or from chartwise
   `CoHA(C^3)=Y^+`.
8. A Hochschild trace replaces the negative-cyclic CY3 orientation and
   chain-level `S^3` framing witness.
9. `CoHA(C^3)=W_{1+\infty}` directly.
10. The K3 hCS two-loop/YBE lane is theorem-grade in the present
    compute state.

## Surviving spine

Stage 1, conditional on the verified CY3/framed/anomaly locus:

```tex
\Phi^{FA}_3(\mathcal C)\in E_3\text{-HolFA}(X).
```

Stage 2:

```tex
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
\SpCh_{\Sigma_2,C}(\Phi^{FA}_3(\mathcal C))
  \in E_1\text{-ChirAlg}(C).
```

The non-symmetric braiding lives on the constructed Drinfeld/derived
center:

```tex
\mathcal Z(\Rep^{E_1}(A_{\mathcal C}))
  \simeq
\Rep^{E_2}(Z^{der}_{ch}(A_{\mathcal C})),
```

not on the final `E_1` algebra as a native `E_2` structure.

Hall side:

```tex
\CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1),
\qquad
D(Y^+)\to \mathcal W_{1+\infty}
```

only after doubling/evaluation.  The comparison
`Phi^{FA}_3 -> CoHA_crit` is the open oriented hCS-to-Hall map.

For `K3 x E`, the K3 surface used in Stage 2 is

```tex
\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3,\qquad C=E,
```

not `p_{K3}^{-1}(pt)`.

## Manuscript integration

Integrated patches:

- `chapters/theory/cy3_chain_level_bridge.tex`: strengthened the
  many-variable chiral CE model to include holomorphic jets and a local
  dg Lie algebra; added the locally constant-shadow guardrail; added the
  normal-form cross-reference after the Stage-1 envelope formula; removed
  the unsafe CFG/CY3 quasi-isomorphism sentence.
- `chapters/theory/cy_to_chiral.tex`: made Stage-1 canonicity
  torsor-aware; replaced the self-referential
  `p^{-1}_{\Sigma_2}(pt)` phrase; qualified the K3 x E BKM summaries by
  the K3-fibre Hall--Borcherds hypotheses; repaired the proof-status
  pass by adding the missing loci, torsor point, chain-level witnesses,
  Hall--Borcherds hypotheses, and fibered root datum instead of weakening
  the manuscript.
- `main.tex`: corrected the K3-fibre projection to
  `p_E^{-1}(pt)` earlier in the integration pass.
- `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex`
  and
  `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex`:
  propagated the K3-fibre correction to the Vol I anchors.

## Evidence and red flags

Agent-reported targeted checks collectively covered the CY3 guardrails,
CFG consistency, Dolbeault homotopy, `S^3` framing, chiral CE, hCS
defect OPE, factorization categories, chiral homology, holography, and
entropy-shadow surfaces.  The hostile synthesis reran the core guardrail
suite with `342 passed`.

Red flag: the direct K3 hCS two-loop/YBE probe currently reports

```text
sl2: two_loop_verification_passed=False
sl3: two_loop_verification_passed=False
```

so that lane remains computational evidence at best, not a theorem.

## Open obligations

1. Construct the orientation-preserving
   `Theta_{hCS->Hall}^{or}` with shifts, Tate twists, completions,
   determinant-line square roots, overlap coherences, and
   Thom--Sebastiani compatibility.
2. Prove the continuous Dolbeault/chiral CE to `E_3` bar identification
   with compact-support conventions fixed.
3. Prove holomorphic pushforward/envelope commutation for
   `SpCh_{\Sigma_2,C}` beyond the verified loci.
4. Build CY3 holomorphic perfect defect/module categories with endpoint
   and puncture data.
5. Repair the K3 hCS two-loop/YBE compute lane by adding the missing
   proof or witness; until then do not use that computation as a theorem
   input.
6. Keep holographic and quantum-gravity interpretations conditional
   unless the BPS/Hall/duality comparison maps are constructed.

## Continuation batch

Agents 16--19 ran after the first synthesis.  Their checks found no TeX
macro blocker in the patched surfaces; forced the status pass to become a
proof-healing pass; propagated the K3 projection correction across the
checked Vol I anchors; and isolated the two-loop/YBE residual as order
`hbar^3`, so it cannot be absorbed by the claimed `O(hbar^5)` remainder.
