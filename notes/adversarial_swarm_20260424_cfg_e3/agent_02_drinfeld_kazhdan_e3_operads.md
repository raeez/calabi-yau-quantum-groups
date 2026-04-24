# Agent 02 -- Drinfeld-Kazhdan E3-Operad Examination

Date: 2026-04-24

Object attacked: chain-level \(\Phi\) on CY\(_3\), especially the claim that \(\Phi_3\) produces \(E_3\) holomorphic factorization algebras, compared with Costello--Francis--Gwilliam 2026, arXiv:2602.12412, around Proposition 4.6, Lemma 4.7, and Lemma 4.9.

Verdict: the safe statement is two-tiered. Stage 1 \(\PhiFA_3(\mathcal C)\) may be treated as a conditional \(E_3\)-holomorphic factorization algebra on the CY\(_3\) target under the stated formality/locality/framing/anomaly hypotheses. The actual CY-to-chiral output \(\Phi_3^{(\Sigma_2,C)}(\mathcal C)=\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))\) is an \(E_1\)-chiral algebra on \(C\). CFG 2026 proves a locally constant topological Chern--Simons \(E_3\)-algebra on \(\mathbb R^3\); it does not prove the six-real-dimensional holomorphic hCS-to-Hall comparison.

## Source Anchors

- Local \(\Phi\) two-stage and native level: `chapters/theory/cy_to_chiral.tex:272`, `chapters/theory/cy_to_chiral.tex:430`, `chapters/theory/cy_to_chiral.tex:4692`.
- Local CY3 hCS/Hall bridge: `chapters/theory/cy3_chain_level_bridge.tex:12`, `chapters/theory/cy3_chain_level_bridge.tex:46`, `chapters/theory/cy3_chain_level_bridge.tex:230`, `chapters/theory/cy3_chain_level_bridge.tex:245`.
- Local \(E_3\) and CFG comparison: `chapters/theory/en_factorization.tex:567`, `chapters/theory/en_factorization.tex:589`, `chapters/theory/quantum_chiral_algebras.tex:260`, `chapters/theory/quantum_chiral_algebras.tex:650`, `chapters/theory/quantum_chiral_algebras.tex:2042`, `chapters/theory/quantum_chiral_algebras.tex:2497`.
- CFG 2026: Proposition 4.6 constructs BV-quantized observables \(\Obs^\lambda\) on \(\mathbb R^3\) reducing mod \(\hbar\) to classical observables; Lemma 4.7 proves local constancy and hence a filtered \(E_3\)-algebra; Lemma 4.9 computes the first-order \((-2)\)-shifted Poisson bracket from the \(S^2\) binary-operation class in the little \(3\)-disks operad.

## ATTACK -> HEAL Cycles

### Cycle 1 -- Native \(E_3\) vs native \(E_1\)

Attack status: HEALED WITH SCOPE RESTRICTION.

Attack: the phrase "\(\Phi_3\) produces an \(E_3\)-holomorphic factorization algebra" is false if \(\Phi_3\) means the final chiral output. `chapters/theory/cy_to_chiral.tex:272` states \(n_{\mathrm{native}}(d)=1\) for \(d\ge 3\), and `chapters/theory/cy_to_chiral.tex:4692` states the CY3 theorem's conclusion as an \(E_1\)-chiral algebra after choosing \((\Sigma_2,C)\).

Heal: reserve \(E_3\) for Stage 1, written \(\PhiFA_3(\mathcal C)\). Reserve \(\Phi_3^{(\Sigma_2,C)}\) for the \(E_1\)-chiral curve shadow. The precise safe sentence is:
\[
\Phi_3^{(\Sigma_2,C)}=\SpCh_{\Sigma_2,C}\circ\PhiFA_3,\qquad
\PhiFA_3(\mathcal C)\in E_3\text{-}\mathrm{HolFA}(X),\quad
\Phi_3^{(\Sigma_2,C)}(\mathcal C)\in E_1\text{-}\mathrm{ChirAlg}(C).
\]

### Cycle 2 -- CFG locally constant \(E_3\) vs holomorphic CY3 \(E_3\)

Attack status: SURVIVES AS A GUARDRAIL.

Attack: CFG Proposition 4.6 and Lemma 4.7 cannot be cited as the source theorem for CY3 hCS/Hall. CFG's local constancy comes from the de Rham complex of ordinary \(3\)-dimensional Chern--Simons theory on \(\mathbb R^3\); by Lurie HA 5.4.5.9, locally constant factorization algebras on \(\mathbb R^3\) are \(E_3\)-algebras. The CY3 bridge instead uses Dolbeault/hCS observables on a complex threefold, and the comparison to critical CoHA is a separate map \(\Theta_{\hCS\to\Hall}\).

Heal: use CFG only as the topological CS analogue and module-category model. For Vol III, cite Costello--Li / Costello--Gwilliam--Li for hCS locality and keep `chapters/theory/cy3_chain_level_bridge.tex:230` and `chapters/theory/cy_to_chiral.tex:607` as the no-shortcut anchors. The hCS-to-Hall comparison remains `chapters/theory/cy3_chain_level_bridge.tex:245`, not a consequence of CFG.

### Cycle 3 -- Little disks, Dunn additivity, and the source of braiding

Attack status: HEALED BY SEPARATING HOMOLOGY BRACKET FROM BRAIDING.

Attack: "little \(3\)-disks \(E_3\) gives the quantum-group braiding" is not the right mechanism. CFG Lemma 4.9 uses the fundamental class of \(S^2\) in the binary operations of \(E_3\) to produce a \((-2)\)-shifted Poisson bracket. That is not a braid-group \(\pi_1\) effect. Locally, Vol III already says the topological restriction has trivial \(\pi_1\) braiding and the non-symmetric quantum-group braiding at \(d=3\) comes through the Drinfeld center, not from the \(E_3\to E_2\) restriction (`chapters/theory/cy_to_chiral.tex:4692`).

Heal: state Dunn additivity as an operadic tensor-product tool, not as a braiding extractor. The \(E_3\) Stage-1 structure can control shifted Poisson/deformation data; the non-symmetric \(R\)-matrix on the final \(E_1\)-chiral algebra must pass through \(\mathcal Z(\Rep^{E_1}(A))\), as in `chapters/theory/quantum_chiral_algebras.tex:91` and `chapters/theory/quantum_chiral_algebras.tex:2042`.

### Cycle 4 -- Module-category consequences

Attack status: BLOCKED FOR CY3; PROVED ONLY IN CFG TOPOLOGICAL CS.

Attack: importing CFG's perfect-module theorem would wrongly imply that modules over the 6d hCS/quantum-toroidal object already give RT-type invariants. CFG proves that perfect modules over the filtered \(E_3\)-algebra \(A^\lambda\) from ordinary Chern--Simons supply tangle field theories. Vol III's 6d analogue is explicitly conjectural: the quantum toroidal Koszul duality and ZTE-corrected \(E_3\) coherence are not constructed (`chapters/theory/quantum_chiral_algebras.tex:2104`, `chapters/theory/quantum_chiral_algebras.tex:2124`).

Heal: module-category consequences may be used as a model only after three additional CY3 inputs are supplied: the holomorphic \(E_3\) factorization algebra, the hCS-to-Hall comparison, and the ZTE-compatible ternary correction. Without those, the only proved categorical passage on constructed CY3 loci is \(E_1\to E_2\) by Drinfeld center.

### Cycle 5 -- Deligne/Dunn level drop

Attack status: HEALED; KEEP AS A MAIN STRUCTURAL LESSON.

Attack: the internal higher-Deligne route does not recover the external \(E_3\) needed for the 6d story once the boundary algebra is \(E_1\). `chapters/theory/quantum_chiral_algebras.tex:2042` states the level drop: CFG boundary \(V_k(\mathfrak g)\) is \(E_\infty\)-chiral, so Hochschild cochains can carry \(E_3\); the 6d lift boundary \(Y(\widehat{\mathfrak{gl}}_1)\) is \(E_1\)-chiral, so Hochschild cochains carry only \(E_2\).

Heal: the extra \(E_3\) direction must be external, from the holomorphic configuration/Omega-background geometry of \(\mathbb C^3\), not from Hochschild cochains of the \(E_1\) boundary algebra. This matches the CFG dictionary in `chapters/theory/quantum_chiral_algebras.tex:2497` and the two-source warning in `chapters/theory/en_factorization.tex:589`.

### Cycle 6 -- K3-fibre specialisation notation

Attack status: OPEN LOCAL CORRECTION NEEDED; NOT EDITED BY THIS AGENT.

Attack: the K3-fibre specialisation anchors contain a projection/dimension inconsistency. `chapters/theory/cy_to_chiral.tex:307`, `chapters/theory/cy_to_chiral.tex:336`, and `chapters/theory/cy_to_chiral.tex:598` write \(\Sigma_2=p_{K3}^{-1}(\mathrm{pt})\simeq K3\). With \(p_{K3}:K3\times E\to K3\), the fibre over a point is \(E\), not \(K3\). The K3 fibre over the elliptic base is \(p_E^{-1}(\mathrm{pt})\simeq K3\). The same lines also call \(\Sigma_2\) a real \(2\)-cycle while K3 is a complex surface, real dimension \(4\).

Heal: integration should replace the geometric phrase by one of two consistent conventions. If \(\Sigma_2\) means "complex surface specialisation", write \(\Sigma_2=p_E^{-1}(\mathrm{pt})\simeq K3\) and stop calling it a real \(2\)-cycle. If \(\Sigma_2\) really means a real \(2\)-cycle, then the K3-fibre Borcherds specialisation cannot be described by the whole K3 fibre without an additional pushforward/trace over a real \(2\)-cycle inside K3. I made no manuscript edit.

## Recommendation

Claim-status recommendation: Stage-1 \(E_3\)-holomorphic factorization algebra for CY3 should remain conditional/proved-only-on-stated loci; final \(\Phi_3^{(\Sigma_2,C)}\) output should remain \(E_1\)-chiral. CFG 2026 may be cited for ordinary \(3\)d CS locally constant \(E_3\) and perfect-module technology, but not as the proof of CY3 hCS-to-Hall or quantum-toroidal \(E_3\) coherence.

Files changed: this report only.

Verification run: `pytest -q compute/tests/test_cfg25_e1_chiral_lift.py compute/tests/test_qg_from_fh_3d_6d.py compute/tests/test_e3_two_parameter_rmatrix.py compute/tests/test_cy3_chain_framing.py` -- 290 passed.
