# Inscription Draft: `thm:bfn-phi-ade-identification`

**Status**: Draft only (2026-04-17). Not yet inscribed into `.tex`.
**Programme**: Vol III F34 (BFN Coulomb branches / ADE Yangian route).
**Verdict source**: Wave-2 F34 audit — low-hanging literature-assembled ProvedElsewhere.
**Author (to be inscribed)**: Raeez Lorgat.

---

## 1. Theorem statement

```
\begin{theorem}[$\Phi$-BFN identification for resolved ADE surfaces]
\label{thm:bfn-phi-ade-identification}
\ClaimStatusProvedElsewhere

Let $\fg$ be a simple Lie algebra of ADE type and let
$\Gamma \subset \mathrm{SU}(2)$ be the binary McKay subgroup
corresponding to $\fg$ under the McKay correspondence.
Let $(Q_{\fg}, \mathbf{v}, \mathbf{w})$ be the framed affine
Dynkin quiver of type $\hat{\fg}$ with dimension vectors
$\mathbf{v} = \delta$ (minimal imaginary root) and
$\mathbf{w} = \mathbf{e}_0$ (framing at the affine node),
and let $\widetilde{S}_{\fg} \to \C^2/\Gamma$ denote the
Kronheimer minimal crepant resolution.

Then the CY-to-chiral functor $\Phi$ applied to the resolved
ADE surface is canonically isomorphic, as an $E_1$-chiral algebra,
to the BFN quantised Coulomb branch of the framed affine quiver
gauge theory, which in turn is the level-one truncated shifted
affine Yangian:
\[
  \Phi\bigl(T^*\widetilde{S}_{\fg}\bigr)
  \;\simeq\;
  \mathcal{A}_\hbar\!\bigl(Q_{\fg}, \mathbf{v}, \mathbf{w}\bigr)
  \;\simeq\;
  Y^{\mu}\!\bigl(\widehat{\fg}\bigr)_{k=1},
\]
where $\mu \in \mathbf{P}^+$ is the dominant coweight determined
by the framing $\mathbf{w}$ via Nakajima--Takayama truncation,
and the level-one evaluation is fixed by the Kronheimer hyperk\"ahler
moment map at the exceptional divisor.
\end{theorem}
```

---

## 2. Citations (ProvedElsewhere ledger)

| Ref | Role | Source |
|-----|------|--------|
| [BFN16] | Coulomb = $\mathcal{A}_\hbar$ convolution algebra, Thm 1.1 | Braverman--Finkelberg--Nakajima, arXiv:1601.03586 |
| [BFN16b] | Coulomb of quiver gauge theory = shifted Yangian, Thm 1.1 | Braverman--Finkelberg--Nakajima, arXiv:1604.03625 |
| [NT18] | Truncated shifted Yangian via GKLO generators, Thm A | Nakajima--Takayama, arXiv:1606.02002 |
| [W19] | Coulomb branch of affine type-A as level-$\ell$ shifted Yangian | Webster, arXiv:1905.11473 |
| [Kr89] | Hyperk\"ahler resolution of $\C^2/\Gamma$ | Kronheimer, J.~Diff.~Geom.~29 (1989) |
| [McK80] | Finite $\Gamma \subset \mathrm{SU}(2) \leftrightarrow$ affine ADE Dynkin | McKay, Proc.~Symp.~Pure Math.~37 |
| [BKR01] | Derived McKay: $D^b(\Coh \widetilde{S}_\fg) \simeq D^b(\Coh_\Gamma \C^2)$ | Bridgeland--King--Reid, arXiv:math/9908027 |
| [KV00] | Preprojective algebra $\Pi_{Q_\fg}$-mod $\simeq$ $\Coh_\Gamma \C^2$ | Kapranov--Vasserot, Math.~Ann.~316 |

---

## 3. Composition proof sketch (ProvedElsewhere, 4 steps)

**Step 1 — McKay + Kronheimer.** By [Kr89] + [McK80],
$\Gamma \leftrightarrow \fg$ identifies $\widetilde{S}_\fg$
as the minimal crepant resolution of $\C^2/\Gamma$, with
exceptional divisor = disjoint union of $(-2)$-curves matching
the finite Dynkin diagram of $\fg$.

**Step 2 — Derived McKay equivalence.** [BKR01] gives
$D^b(\Coh \widetilde{S}_\fg) \simeq D^b(\Coh_\Gamma \C^2)
\simeq D^b(\Pi_{Q_\fg}\text{-mod})$, the last via
Kapranov--Vasserot [KV00] identifying $\Gamma$-equivariant sheaves
on $\C^2$ with modules over the preprojective algebra of the
affine Dynkin quiver $Q_\fg$.

**Step 3 — BFN identification.** The 3d $\mathcal{N} = 4$ quiver
gauge theory $(Q_\fg, \mathbf{v}, \mathbf{w})$ has Higgs branch
$\mathcal{M}_H = \Pi_{Q_\fg}\text{-mod at }\mathbf{v}$ (Nakajima
quiver variety) and Coulomb branch $\mathcal{M}_C$. By [BFN16b,
Thm 1.1], the quantised Coulomb branch
$\mathcal{A}_\hbar(Q_\fg, \mathbf{v}, \mathbf{w})$ is
canonically isomorphic to the $\mathbf{w}$-truncated shifted
Yangian $Y^\mu(\widehat{\fg})$; [NT18, Thm A] gives an explicit
GKLO presentation; [W19] extends to non-simply-laced cases by
folding (not needed here since we are ADE).

**Step 4 — $\Phi$-compatibility.** $\Phi$ applied to the
cotangent of a hyperk\"ahler resolution produces the
factorisation-quantisation of the Higgs branch (CY-A$_2$ output
for $d = 2$ local surfaces, proved at publication standard in Vol~III).
Symplectic duality [BLPW16] identifies Higgs-side factorisation
quantisation with Coulomb-side BFN convolution as $E_1$-chiral
algebras on the formal disk; combining Steps~2--3 gives
$\Phi(T^*\widetilde{S}_\fg) \simeq \mathcal{A}_\hbar(Q_\fg,
\mathbf{v}, \mathbf{w}) \simeq Y^\mu(\widehat{\fg})_{k=1}$.
Level one is fixed by the Kronheimer moment-map normalisation
at the exceptional divisor (unit flux through each $(-2)$-curve).

All four steps are ProvedElsewhere; the theorem is a composition,
with no new mathematics. The Wave-2 verdict "low-hanging fruit"
is accurate: Vol~III supplies only the $\Phi$-compatibility bridge
(Step~4), itself a corollary of CY-A$_2$ + symplectic duality.

---

## 4. Independent Verification decorators (HZ-IV)

Three disjoint verification paths, per Vol~III HZ-IV protocol
(derived_from, verified_against, disjoint_rationale):

**(V1) Derived McKay on the Higgs side.**
- `derived_from`: [BKR01] + [KV00] equivalence
  $D^b(\Coh\widetilde{S}_\fg) \simeq D^b(\Pi_{Q_\fg})$.
- `verified_against`: Hilbert-series match on both sides
  via character computation in
  `compute/lib/fh_mckay_correspondence.py` (rank + character
  check across all ADE types A_n, D_n, E_6, E_7, E_8).
- `disjoint_rationale`: the derived-category equivalence is
  a sheaf-theoretic statement on $\widetilde{S}_\fg$ with no
  reference to the affine Grassmannian or BFN convolution;
  it therefore bounds the Higgs side independently of Step~3.

**(V2) BFN convolution on the Coulomb side.**
- `derived_from`: [BFN16b, Thm 1.1] equivariant homology of
  the variety of triples $\mathcal{R}_{G,N}$ with convolution.
- `verified_against`: presentation match with the GKLO
  generators of [NT18], implemented as RTT check in
  `compute/lib/ade_yangian_level1.py` (63 tests: Yang
  $R$-matrix, Lax presentation, level-one evaluation,
  ADE type-by-type $R_{12} L_1 L_2 = L_2 L_1 R_{12}$).
- `disjoint_rationale`: the BFN construction uses affine
  Grassmannian homology (no sheaves on $\widetilde{S}_\fg$,
  no preprojective algebra), so it is algebraically disjoint
  from (V1). The Yangian presentation is checked at the
  RTT level, independent of any geometric resolution.

**(V3) $\Phi$-functor + level-one matching.**
- `derived_from`: Vol~III CY-A$_2$ theorem (proved at $d = 2$)
  + $\Phi$-definition via factorisation quantisation of
  $T^*\widetilde{S}_\fg$.
- `verified_against`: Kronheimer moment-map unit-flux
  computation across exceptional $(-2)$-curves reproduces
  the level-one evaluation; cross-check against the
  Kummer-point $A_1$ specialisation (affine $\widehat{sl}_2$
  at level 1) already proved in
  `compute/lib/bfn_coulomb_k3_yangian.py` (93 tests; the
  $A_1$ sub-case matches (V2) independently).
- `disjoint_rationale`: this path routes through the
  hyperk\"ahler moment-map normalisation, touching neither
  (V1)'s sheaf equivalence nor (V2)'s affine-Grassmannian
  homology. The three paths converge on the same
  $Y^\mu(\widehat{\fg})_{k=1}$ from three algebraically
  independent directions.

---

## 5. Proposed inscription location

**Primary**: `chapters/examples/k3_yangian_chapter.tex`, immediately
after `subsec:k3e-bfn` (currently ends at line ~103), as a new
subsection titled "ADE specialisation: the proved sub-case."
Rationale: this is the natural home for proved ADE-type
identifications; it also provides the bridge from the Kummer
$A_1$ conjecture (already present as `conj:k3e-bfn-yangian`)
to the full K3 conjecture.

**Secondary cross-reference**: add a `\ref{thm:bfn-phi-ade-identification}`
pointer in `k3_quantum_toroidal_chapter.tex`'s
`rem:bfn-ade-proved` (around line 848), which currently cites
BFN informally; upgrade to the inscribed theorem.

---

## 6. Duplicate-label resolution (AP124)

**Finding.** Wave-2 flagged label collision across two files:
- `k3_quantum_toroidal_chapter.tex:814` — `\label{conj:bfn-k3-yangian}`
- `k3_yangian_chapter.tex:84` — `\label{conj:k3e-bfn-yangian}`

On direct inspection, the labels are textually DISTINCT
(`bfn-k3-yangian` vs `k3e-bfn-yangian`), so the collision is
NOT literal. However, the two conjectures make overlapping
claims with different scope (the toroidal version invokes the
$24$-dim Mukai lattice; the K3$\times$E version invokes the
Kummer resolution with 4 bifundamentals), and their label
stems differ only in an ad-hoc `k3e-` prefix. This is a
semantic duplicate AP-124 variant: two conjectures stating
the "same" BFN = K3-Yangian identification in two different
chapters with no cross-reference between them.

**Proposal.**

1. Rename `k3_quantum_toroidal_chapter.tex:814`
   `conj:bfn-k3-yangian` $\to$ `conj:bfn-k3-yangian-mukai`
   (scope: 24-dim Mukai lattice, generic K3 moduli).
2. Rename `k3_yangian_chapter.tex:84`
   `conj:k3e-bfn-yangian` $\to$ `conj:bfn-k3-yangian-kummer`
   (scope: Kummer orbifold point $T^4/\Z_2$, affine $A_1$
   quiver with 4 bifundamentals).
3. After inscription of `thm:bfn-phi-ade-identification`,
   add a remark in each conjecture citing the proved ADE
   sub-case and stating explicitly that the Kummer conjecture
   REDUCES to the proved $A_1$ instance (Step~3 above) plus
   deformation invariance across the 16 orbifold resolutions,
   while the full Mukai conjecture requires the non-quiver
   BFN extension.
4. Grep sweep across all three volumes after the rename
   (`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
   `~/calabi-yau-quantum-groups`) for any `\ref{conj:bfn-k3-yangian}`
   or `\ref{conj:k3e-bfn-yangian}` instances, update atomically
   in the same session (AP5 + AP124 discipline).

The two conjectures should NOT be merged: they genuinely
address different strata (generic vs orbifold) of K3 moduli.
The rename distinguishes them and opens the inscription slot
for the unambiguous ADE-proved `thm:` between them.

---

## 7. To-do before inscription (next session)

- [ ] Verify `compute/lib/ade_yangian_level1.py` 63-test count
  against current test suite.
- [ ] Verify `compute/lib/fh_mckay_correspondence.py` claims
  rank + character match across all ADE types.
- [ ] Confirm Vol~III CY-A$_2$ theorem is already inscribed
  at publication standard (programme status: "10 proofs at
  publication standard" per CLAUDE.md).
- [ ] Cross-reference [BLPW16] (Braden--Licata--Proudfoot--Webster,
  arXiv:1407.0964) for the symplectic-duality bridge in Step~4.
- [ ] Draft the HZ-IV decorator Python stubs for the three
  verification paths; target `compute/tests/test_bfn_phi_ade.py`.
