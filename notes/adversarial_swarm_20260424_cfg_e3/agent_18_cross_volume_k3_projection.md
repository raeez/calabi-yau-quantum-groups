# Agent 18: Cross-volume K3-fibre projection audit

Scope: Vol III `/Users/raeez/calabi-yau-quantum-groups`, Vol I
`/Users/raeez/chiral-bar-cobar`, and Vol II
`/Users/raeez/chiral-bar-cobar-vol2`.  I did not edit cross-repo files.

Correct convention:

```tex
X = K3 \times E,\qquad p_{K3}:X\to K3,\qquad p_E:X\to E.
```

Therefore

```tex
p_{K3}^{-1}(\mathrm{pt}) = \{\mathrm{pt}\}\times E \simeq E,
\qquad
\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3,\qquad C=E.
```

Plain requested form: `Sigma_2=p_E^{-1}(pt) ~= K3, C=E`.

## Fixed-string rg commands run

Roots used in all searches:

```bash
/Users/raeez/calabi-yau-quantum-groups /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2
```

Commands:

```bash
rg -nF --hidden --glob '!**/.git/**' 'p_{K3}^{-1}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{K3}^{-1}(\mathrm{pt})' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{K3}^{-1}(pt)' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{K3}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{\mathrm{K3}}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_E^{-1}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_E^{-1}(\mathrm{pt})' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{E}^{-1}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'p_{\mathrm{E}}^{-1}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'K3-fibre' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'K3 fibre' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'K3 fiber' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'elliptic fibre' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'elliptic fiber' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'K3-fibre of $p_{K3}' ROOTS
rg -nF --hidden --glob '!**/.git/**' 'Sigma_2 = K3' ROOTS
rg -nF --hidden --glob '!**/.git/**' '(\Sigma_2, C) = (K3, E)' ROOTS
```

## False anchors

### Vol I manuscript

- `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:4472`
  writes
  `\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2 = p_{K3}^{-1}(\mathrm{pt}), C = E}`
  and the surrounding sentence calls Stage 2 homology over a closed
  `2`-cycle.  Classification: false projection, plus dimension-risk.
  Minimal patch: replace `p_{K3}^{-1}(\mathrm{pt})` by
  `p_E^{-1}(\mathrm{pt})\simeq K3`; replace "closed `2`-cycle" by
  "holomorphic surface" or "complex surface specialisation datum".

- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex:1123`
  writes
  `\SpCh_{\Sigma_2 = p_{K3}^{-1}(\mathrm{pt}),\, C = E}`.
  Classification: false.  Minimal patch: `p_E^{-1}(\mathrm{pt})`.

- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex:3220`
  repeats the same Stage-2 shadow
  `\SpCh_{\Sigma_2 = p_{K3}^{-1}(\mathrm{pt}),\, C = E}`.
  Classification: false.  Minimal patch: `p_E^{-1}(\mathrm{pt})`.

- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex:3293`
  theorem statement says
  `\Sigma_2 = p_{K3}^{-1}(\mathrm{pt})` of the `K3 \times E` geometry.
  Classification: false.  Minimal patch: state
  `\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3`.

### Vol I notes

- `/Users/raeez/chiral-bar-cobar/notes/wave17_opus_20260424/opus_06_G4_phi_functor.tex:824`
  says "the K3-fibre of `$p_{K3}: X \to K3$`".
  Classification: false if this note is promoted or used as source.
  Minimal patch: "the K3 fibre of `$p_E:X\to E$`".

### Hidden Vol III worktrees

These are not current mainline Vol III, but they are inside hidden
`.claude/worktrees` and should not be promoted during integration.

- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ac0fc1ac/main.tex:1476`
- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ae1c7771/main.tex:1476`

Both use `\Sigma_2 = p_{K3}^{-1}(\mathrm{pt})` for the K3-fibre
specialisation.  Classification: false stale worktree copies.  Minimal
patch on integration only: use the current mainline wording
`\Sigma_2 = p_E^{-1}(\mathrm{pt})` to the elliptic base `C=E`.

- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ac0fc1ac/chapters/theory/cy_to_chiral.tex:184`
- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ae1c7771/chapters/theory/cy_to_chiral.tex:184`

Both call `\Sigma_2` a real `2`-cycle and identify
`\Sigma_2=p_{K3}^{-1}(\mathrm{pt})\simeq K3`.  Classification: false
projection and false dimension.  Minimal patch on integration only:
`\Sigma_2\subset X` is a complex surface specialisation datum, and for
`X=K3\times E` it is `p_E^{-1}(\mathrm{pt})\simeq K3`.

- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ac0fc1ac/chapters/theory/cy_to_chiral.tex:213`
- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ae1c7771/chapters/theory/cy_to_chiral.tex:213`
- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ac0fc1ac/chapters/theory/cy_to_chiral.tex:460`
- `/Users/raeez/calabi-yau-quantum-groups/.claude/worktrees/agent-ae1c7771/chapters/theory/cy_to_chiral.tex:460`

All repeat the false `p_{K3}^{-1}(\mathrm{pt})` K3-fibre claim.
Classification: false stale worktree copies.  Minimal patch on
integration only: `p_E^{-1}(\mathrm{pt})`.

## Acceptable anchors

- `/Users/raeez/calabi-yau-quantum-groups/main.tex:1486` uses
  `\Sigma_2 = p_E^{-1}(\mathrm{pt})` to the elliptic base `C=E`.
  Classification: acceptable.

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:425`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:459`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:670`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:721`

These current Vol III anchors use
`\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3`, with `C=E` or "elliptic
base" context.  Classification: acceptable.

- `/Users/raeez/calabi-yau-quantum-groups/notes/adversarial_swarm_20260424_cfg_e3/agent_02_drinfeld_kazhdan_e3_operads.md:67`
  quotes the old false claim only to attack it and gives the correct
  formula.  Classification: acceptable audit note.

- `/Users/raeez/calabi-yau-quantum-groups/notes/adversarial_swarm_20260424_cfg_e3/agent_14_cross_volume_consistency.md:141-153`
  explicitly says not to call `p_{K3}^{-1}(\mathrm{pt})` the K3 fibre.
  Classification: acceptable audit note.

- `/Users/raeez/calabi-yau-quantum-groups/notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:128-131`
  records the correct formula and rejects `p_{K3}^{-1}(pt)`.
  Classification: acceptable synthesis note.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:2193`
  uses `p_{K3}` as a point-coordinate name in a stalk
  `(p_{K3},z,t)`, not as the projection `p_{K3}:K3\times E\to K3`.
  Classification: acceptable.

- `/Users/raeez/calabi-yau-quantum-groups/.swarm_outputs/wave1/A07_kontsevich_Linf_minimal.md:230`
  uses `p_{K3}^*\At(T_{K3})\oplus p_E^*\At(T_E)` for the product
  Atiyah-class decomposition.  Classification: acceptable; not an
  inverse-fibre claim.

## Risky but not a projection error

Many files use the shorthand `\Sigma_2=K3` or
`(\Sigma_2,C)=(K3,E)`.  This is acceptable when it means
`K3\times\{\mathrm{pt}\}=p_E^{-1}(\mathrm{pt})`, but integration should
prefer the explicit formula at first occurrence in a section.

Adjacent example:

- `/Users/raeez/chiral-bar-cobar/standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1171`
  says `\Sigma_2 = K3` is "a primitive curve class".  This is not the
  `p_{K3}^{-1}` projection error, but it is dimension-risky if promoted:
  K3 is a complex surface, not a curve.  Minimal patch if promoted:
  "Taking the K3 surface specialisation
  `\Sigma_2=p_E^{-1}(\mathrm{pt})`".

## No positive `p_{K3}^{-1}`-as-E cases found

No hit used `p_{K3}^{-1}(\mathrm{pt})` correctly to denote the elliptic
fibre `E`.  Every inverse-projection hit was either a false K3-fibre
claim or an audit/synthesis note explicitly rejecting that claim.

