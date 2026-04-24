# Agent 14: cross-volume consistency for CY3/CFG/E3

Date: 2026-04-24.  Scope: adversarial consistency audit only.  No manuscript edits.

## Cycle 1: Stage-1 E3 hFA versus Stage-2 E1 chiral output

Claim attacked: "The CY-to-chiral functor at d=3 outputs an E3-chiral algebra."

Failure mode/proof: false as final-output wording.  Vol III separates
\[
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  = \operatorname{SpCh}_{\Sigma_2,C}(\Phi^{\mathrm{FA}}_3(\mathcal C))
  \in E_1\text{-}\mathrm{ChirAlg}(C).
\]
The E3 object is Stage 1, \(\Phi^{\mathrm{FA}}_3(\mathcal C)\), before
specialisation.  The non-symmetric E2 braiding is recovered through the
Drinfeld centre of the E1 representation category, not by restricting the
E3 structure.

Healed wording/formulas: "At d=3, \(\Phi^{\mathrm{FA}}_3(\mathcal C)\) is the
Stage-1 E3 holomorphic factorisation algebra.  After a chosen
\((\Sigma_2,C)\), the final chiral output
\(\Phi_3^{(\Sigma_2,C)}(\mathcal C)\) is natively E1 on \(C\)."

Exact anchors:
- Vol III correct: `chapters/theory/cy_to_chiral.tex:4798`,
  `:4800-4806`, `:4822-4836`, `:4856-4857`, `:4882-4883`.
- Local risky note: `notes/wave_cfg2026/agent_5_deligne_e3_hochschild.tex:597-602`
  says the functor "outputs an E3-chiral algebra"; this should be read as
  Stage-1 only or corrected by integration owner.
- Local correct note: `notes/wave_cfg2026/agent_4_e2_transverse_shadow.tex:983-993`.
- Cross-volume: Vol I `~/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex:107-108`,
  `:3221-3223`; Vol II
  `~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6665`.

Claim-status recommendation: Conditional for the global CY3 theorem; proved
on named toric/framed loci only as stated in Vol III.  Any unqualified
"E3-chiral output" at d=3 should be downgraded to Stage-1 wording.

## Cycle 2: CFG 2026 is not a shortcut for CY3 hCS-to-Hall

Claim attacked: "CFG 2026's topological E3 construction proves the CY3
holomorphic E3/hCS/Hall comparison."

Failure mode/proof: CFG 2026 supplies a topological E3 structure on
\(\mathrm{Obs}_{\mathrm{CS}}(\mathbb R^3)\).  Vol III names three different
E3 structures: CFG topological on \(\mathbb R^3\), hCS holomorphic on
\(\mathbb C^3\), and algebraic CY3-cyclic on Hochschild cochains.  They agree
chartwise only through HKR/Kontsevich-Tamarkin formality; global compact-CY3
compatibility is the open \(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\) problem.

Healed wording/formulas: "CFG 2026 is the 3d topological analogue.  The
6d hCS-to-Hall comparison must be stated as chartwise proved and globally
conditional on \(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\)."

Exact anchors:
- Vol III: `chapters/theory/quantum_chiral_algebras.tex:2452-2475`,
  `:2507-2509`; `chapters/theory/cy_to_chiral.tex:723-724`.
- Local note: `notes/wave_cfg2026/agent_5_deligne_e3_hochschild.tex:545-595`,
  `:605-636`.
- Cross-volume risk: Vol II
  `~/chiral-bar-cobar-vol2/chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:713-725`
  should carry the same chartwise/global-conditional qualifier when reused.

Claim-status recommendation: chartwise proved elsewhere; global compact-CY3
comparison conditional/open.  Do not promote CFG analogy to a source theorem.

## Cycle 3: \(C^*_{\mathrm{Lie}}(\mathfrak g)\) versus chiral CE

Claim attacked: "The one-dimensional topological CE algebra
\(C^*_{\mathrm{Lie}}(\mathfrak g[1])\) is the same object as the chiralized
many-variable CE/bar complex."

Failure mode/proof: \(C^*_{\mathrm{Lie}}(\mathfrak g[1])\) appears as the
1d topological factor in the 5d hCS tensor factorisation.  Chiral CE chains
and cochains are Ran-space/chiral objects: ordered or symmetric bar complexes,
and Hochschild cochains/derived chiral centre.  The Koszul dual \(A^!\) is
Verdier dual to the bar complex, not the CE cochain complex.

Healed wording/formulas:
\[
B^{\mathrm{ord}}(A)=T^c(s^{-1}\bar A),\qquad
C^\bullet_{\mathrm{ch}}(A,A)=\mathrm{RHom}(\Omega B(A),A)
   =Z^{\mathrm{der}}_{\mathrm{ch}}(A),\qquad
A^!=D_{\mathrm{Ran}}(B(A)).
\]
Use \(C^*_{\mathrm{Lie}}(\mathfrak g[1])\) only for the topological factor.

Exact anchors:
- Vol III: `notes/wave_cfg2026/agent_8_5d_hcs_cfg.tex:120-133`;
  `chapters/theory/cy_to_chiral.tex:655`;
  `chapters/theory/quantum_chiral_algebras.tex:377-387`, `:400-411`.
- Cross-volume: Vol II
  `~/chiral-bar-cobar-vol2/chapters/connections/chiral_ce_factalg_gen_rel.tex:104-111`,
  `:1053-1079`; `~/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:2141-2168`;
  `~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6005-6007`,
  `:6068-6073`.

Claim-status recommendation: definitional/proved on the stated models.  Any
plain "CE" reference must name ordinary Lie CE, chiral CE chains, chiral CE
cochains, or derived centre.

## Cycle 4: \(\mathrm{CoHA}(\mathbb C^3)=Y^+\), not \(\mathcal W_{1+\infty}\)

Claim attacked: "\(\mathrm{CoHA}(\mathbb C^3)\) is
\(\mathcal W_{1+\infty}\)" or "\(\Phi^{\mathrm{FA}}_3(\mathrm{Perf}(\mathbb C^3))
=\mathrm{CoHA}(\mathbb C^3)=Y^+\)" without operadic qualifiers.

Failure mode/proof: Vol III states the equality
\(\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)\) as an
associative E1 Hall algebra.  The full affine Yangian is the Drinfeld
double \(D(Y^+)\).  The map to \(\mathcal W_{1+\infty}\) is an evaluation
to endomorphisms of a vacuum module, not an identity of vertex algebras.

Healed wording/formulas:
\[
\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)
\hookrightarrow Y(\widehat{\mathfrak{gl}}_1)
\xrightarrow{\mathrm{ev}_\lambda}
\mathrm{End}(\mathcal W_{1+\infty}[\lambda]\text{-vac}).
\]
The Stage-1-to-CoHA comparison must be labelled by the comparison map and
operadic level, not written as a raw equality of hFA, CoHA, and VOA.

Exact anchors:
- Vol III: `chapters/theory/quantum_groups_foundations.tex:391-405`;
  `notes/wave_cfg2026/agent_8_5d_hcs_cfg.tex:355-365`;
  risky title in `notes/wave_cfg2026/agent_10_coha_e3_factorization.tex:1`.
- Cross-volume: Vol I
  `~/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:3685-3688`,
  `:3750-3753`, `:3885`; Vol III agrees at
  `chapters/theory/quantum_chiral_algebras.tex:2676-2682`.

Claim-status recommendation: \(\mathrm{CoHA}(\mathbb C^3)=Y^+\) is
proved elsewhere; the evaluation chain is proved elsewhere; any direct
CoHA=\(\mathcal W_{1+\infty}\) identity is false.

## Cycle 5: K3 fibre projection

Claim attacked: "The K3 fibre in \(K3\times E\) is
\(p_{K3}^{-1}(\mathrm{pt})\)."

Failure mode/proof: with \(p_{K3}:K3\times E\to K3\), the fibre over a
point is \(E\).  The K3 fibre over the elliptic base is
\(p_E^{-1}(\mathrm{pt})\simeq K3\).  Vol III currently uses the correct
projection; Vol I still has contrary anchors.

Healed wording/formulas:
\[
\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3,\qquad C=E,\qquad
\operatorname{SpCh}_{K3,E}=\text{pushforward along }p_E\text{ then restriction to }E.
\]
Do not call \(p_{K3}^{-1}(\mathrm{pt})\) the K3 fibre.

Exact anchors:
- Vol III correct: `chapters/theory/cy_to_chiral.tex:416-420`,
  `:453`, `:715`, `:726-730`.
- Cross-volume false anchors needing integration-owner propagation:
  Vol I `~/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:4472`;
  `~/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex:1123`,
  `:3220`, `:3293`.
- Rg found no corresponding Vol II false \(p_{K3}^{-1}\) hit in the searched
paths.

Claim-status recommendation: geometric correction is proved by product
projection.  Vol I propagation required; out of this agent's write scope.

## Cycle 6: \(B(A)\), \(A^i\), \(A^!\), and \(Z^{\mathrm{der}}_{\mathrm{ch}}(A)\)

Claim attacked: "\(B(A)\), \(A^i\), \(A^!\), \(\Omega B(A)\), and the derived
chiral centre are interchangeable bar-cobar outputs."

Failure mode/proof: Vol III and Vol I explicitly distinguish them.
\(B(A)\) is a coalgebra.  \(A^i=H^*(B(A))\) is bar cohomology / dual
coalgebra.  \(A^!=(A^i)^\vee\) or \(D_{\mathrm{Ran}}(B(A))\) is the Koszul
dual algebra/defect.  \(\Omega(B(A))\simeq A\) is inversion.  The derived
chiral centre \(Z^{\mathrm{der}}_{\mathrm{ch}}(A)=\mathrm{RHom}(\Omega B(A),A)\)
is the bulk.

Healed wording/formulas:
\[
B(A)\neq \Omega(B(A))\neq A^!\neq Z^{\mathrm{der}}_{\mathrm{ch}}(A),
\qquad
\Omega(B(A))\simeq A,\quad
A^!=D_{\mathrm{Ran}}(B(A)),\quad
Z^{\mathrm{der}}_{\mathrm{ch}}(A)=\mathrm{RHom}(\Omega B(A),A).
\]

Exact anchors:
- Vol III: `chapters/theory/cy_to_chiral.tex:2277-2291`;
  `chapters/connections/bar_cobar_bridge.tex:30-33`, `:76-82`;
  `chapters/theory/quantum_chiral_algebras.tex:385-387`, `:1072-1080`.
- Cross-volume: Vol I
  `~/chiral-bar-cobar/chapters/theory/bar_construction.tex:129-135`,
  `:222-231`; Vol II
  `~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6068-6073`.

Claim-status recommendation: definitional/proved on the Koszul locus with
completion qualifiers; never write \(A^!=\Omega B(A)\) unless explicitly
declaring a nonstandard convention and reconciling it with the Verdier leg.

## Tests and rg commands run

No build or test suite was run; this was a read-only cross-volume audit plus
this note.  Commands included:

- Repo-local doctrine was read before editing; `sed -n '1,160p' AGENTS.md`.
- `git status --short`; `ls notes/adversarial_swarm_20260424_cfg_e3`.
- Fixed-string local sweeps with `rg -n -F` for `Phi^{FA}`,
  `Sp_{`, `E_3`, `CFG`, `Costello`, `Francis`, `Gwilliam`,
  `C^*(`, `Chevalley`, `chiralized`, `many-variable`, `CoHA`, `Y^+`,
  `W_{1+\infty}`, `p_E`, `p_{K3}`, `B(A)`, `A^i`, `A^!`,
  and `Z^{\mathrm{der}}_{\mathrm{ch}}`.
- Targeted line reads with `nl -ba ... | sed -n ...` on Vol III files and
  CFG notes listed above.
- Cross-volume `rg` only in `~/chiral-bar-cobar` and
  `~/chiral-bar-cobar-vol2`, including the exact projection searches
  `p_{K3}^{-1}(\mathrm{pt})` and `p_E^{-1}(\mathrm{pt})`.

Initial regex-form `rg` attempts failed on TeX backslashes; all cited anchors
come from rerun fixed-string searches or numbered local reads.

## Files changed

- `notes/adversarial_swarm_20260424_cfg_e3/agent_14_cross_volume_consistency.md`

No manuscript files were edited.  No other swarm note was modified.

## Remaining open obligations

1. Vol I has live false K3-fibre projection anchors using
   \(p_{K3}^{-1}(\mathrm{pt})\); integration owner should propagate the
   Vol III convention \(p_E^{-1}(\mathrm{pt})\).
2. `notes/wave_cfg2026/agent_5_deligne_e3_hochschild.tex:597-602` should be
   normalized from "outputs an E3-chiral algebra" to "Stage-1 E3 hFA, final
   Stage-2 E1 chiral output" before any manuscript import.
3. `notes/wave_cfg2026/agent_10_coha_e3_factorization.tex:1` should be
   treated as shorthand only after inserting the CoHA/E1/Drinfeld-double/VOA
   evaluation-chain qualifiers.
4. Vol II's CFG/hCS avatar statements should be reread during integration so
   "one E3 algebra" claims carry the chartwise/global-conditional
   \(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\) qualifier.
