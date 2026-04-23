# Agent C25 — Orphan reference `prop:archetype-complementarity-bridge`

## Terminal state

**A — FULL CLOSURE.** The reference is **not orphaned**. The proposition
is fully stated and proved in
`/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`
at lines 1748–1942, carrying the label
`\label{prop:archetype-complementarity-bridge}` at line 1751 and flagged
`\ClaimStatusProvedHere`. Wave-2 A04's F3 diagnosis was inaccurate: both
`chiral_center_theorem.tex` and `landscape_census.tex` are `\include`d in
the Vol I `main.tex` build (line 1763: `\input{chapters/examples/landscape_census}`),
so the cross-file `\ref{prop:archetype-complementarity-bridge}` from
`chiral_center_theorem.tex` (lines 2859, 2889, 2959, 2988),
`hochschild_cohomology.tex` (line 4489), and `concordance.tex` (lines 90,
95, 208) resolves correctly in the compiled PDF.

No inscription is required. The bridge identity
$K^{\kappa_{\mathrm{ch}}}(A) = \varrho(A)\cdot K(A)$ is stated, tabulated
on the seven-witness landmark, and proved row-by-row via the
level-independence hypothesis $\varrho(A) = \varrho(A^!)$.

## Statement of the theorem (as it exists in Vol I)

**Proposition (Archetype-by-archetype $\kappa + \kappa^!$ arithmetic with
anomaly-ratio bridge).** `\ClaimStatusProvedHere`. *Regime:
curved-central, Koszul locus.* The scalar complementarity sum
$K^\kappa(\cA) := \kappa(\cA) + \kappa(\cA^!)$ and the Trinity conductor
$K(\cA) := c(\cA) + c(\cA^!)$ are related, on the witness landscape and
its $\mathcal{W}$- and $\mathcal{B}$-family extensions, by the
anomaly-ratio bridge
$$
 K^\kappa(\cA) \;=\; \varrho(\cA) \cdot K(\cA),
 \qquad
 \varrho(\cA) \;:=\; \frac{\kappa(\cA)}{c(\cA)}.
$$
On the seven landmark witnesses the bridge specialises to

| Archetype | Witness $\cA$ | $\varrho(\cA)$ | $K(\cA)$ | $K^\kappa(\cA)$ | $\kappa^*$ |
|---|---|---|---|---|---|
| $\mathsf{G}$ | $\cH_k$ | $1$ | $0$ | $0$ | $0$ |
| $\mathsf{L}$ | $\widehat{\fg}_k$ | $0$ | $2\dim\fg$ | $0$ | $0$ |
| $\mathsf{C}$ | $\beta\gamma_\lambda$ | $1/2$ | $0$ | $0$ | $0$ |
| $\mathsf{M}$ | $\mathrm{Vir}_c$ | $1/2$ | $26$ | $13$ | $13/2$ |
| $\mathsf{M}$-ext | $\mathcal{W}_3^k$ | $5/6$ | $100$ | $250/3$ | $125/3$ |
| $\mathsf{M}$-ext | $\mathrm{BP}_k$ | $1/6$ | $196$ | $98/3$ | $49/3$ |
| $\mathcal{B}$-fam | $\mathcal{H}_{\mathrm{Muk}}(K3)$ | $1/6$ | $48$ | $8$ | $4$ |

The family-dependent ceiling
$\{0, 8, 13, 250/3, 98/3\}$ on
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ is reproduced.
The $\mathcal{B}$-row records Mukai doubling: for
$D^b\mathrm{Coh}(K3)$ with Mukai pairing of signature $(4,20)$,
$c_+(\mathrm{Mukai}(K3)) = 4$ and
$K^\kappa = 2c_+(\mathrm{Mukai}(K3)) = 8$. Scope is the
Lorentzian-lattice-parametric $\mathcal{B}$-family, not universal.

## Proof (existing, summarised)

Scalar identity: assume $\varrho$ is level-independent on the family
$\mathcal{F}$, so $\varrho(\cA) = \kappa/c = \varrho(\cA^!) = \kappa^!/c^!$.
Then $\kappa + \kappa^! = \varrho(c + c^!) = \varrho K$.
Level-independence is Corollary~`cor:anomaly-ratio-ds` for
$\mathcal{W}^k(\fg)$ and is verified row-by-row on the other families.

Row verifications (primary-source-anchored):

- **$\mathsf{G}$:** OPE $J^a(z)J^b(w) \sim \delta^{ab}/(z-w)^2$ gives
  $c(\cH_k) = k$, $\kappa(\cH_k) = k$, $\varrho = 1$. Verdier dual
  $\cH_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$
  (Theorem `thm:heisenberg-koszul-dual-early`) with
  $\kappa(\cH_k^!) = -k$, $c(\cH_k^!) = -k$; $K = 0$, $\varrho K = 0$.
- **$\mathsf{L}$:** Feigin–Frenkel involution $k' = -k - 2h^\vee$ yields
  $c + c' = 2\dim\fg$ (Theorem `thm:central-charge-complementarity`(a));
  $\kappa + \kappa' = 0$ via antisymmetric Koszul-dual structure.
  Level-symmetrised $\varrho_{\mathrm{sym}} = 0$.
- **$\mathsf{C}$:** $c(\beta\gamma_\lambda) = 2(6\lambda^2 - 6\lambda + 1)$
  (Proposition `prop:betagamma-bc-koszul-detailed`); $c(bc_\lambda) =
  -c(\beta\gamma_\lambda)$ by Fock-space parity flip; $K = 0$,
  $\varrho = 1/2$.
- **$\mathsf{M}$:** Virasoro Verdier dual
  $\mathrm{Vir}_c^! \simeq \mathrm{Vir}_{26-c}$
  (Proposition `prop:virasoro-generic-koszul-dual`); $c + c' = 26$,
  $\varrho = 1/2$, $K^\kappa = 13$.
- **$\mathsf{M}$-ext ($\mathcal{W}_3^k$):** Drinfeld–Sokolov gives
  $\kappa = (5/6)c$ (Corollary `cor:anomaly-ratio-ds`) and $K = 100$ at
  $\fg = \mathfrak{sl}_3$ (Theorem `thm:central-charge-complementarity`(b));
  $K^\kappa = 500/6 = 250/3$.
- **$\mathsf{M}$-ext ($\mathrm{BP}_k$):** Minimal-nilpotent DS gives
  $\kappa = c/6$ (Proposition `prop:bp-kappa`) and $K = 196$
  (Proposition `prop:bp-self-duality`); $K^\kappa = 98/3$.
- **$\mathcal{B}$-fam ($\mathcal{H}_{\mathrm{Muk}}(K3)$):**
  Beilinson–Drinfeld Koszul-conductor identity pins
  $K^{\kappa_{\mathrm{ch}}} = 2c_+(\mathrm{Mukai}(K3)) = 8$ on
  $\Lambda_{\mathrm{Muk}} = \mathrm{II}_{4,20}$ via three independent
  faces: Mukai 1987 signature decomposition $c_+ = 4$; Bruinier 2002
  Heegner-Chern reciprocity on $H_1 \subset \overline{\mathcal{A}_2}$
  giving order-$8$ monodromy; Borcherds 1992 / Gritsenko 1999 product
  denominator formula for $\Delta_5$ pinning Lusztig $u_\zeta$ at
  $\ell = 8$ with $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$.

Self-dual values: $\kappa^*(\cA) = K^\kappa(\cA)/2$
(equation `eq:self-dual-kappa-star`).

## Hypothesis

Not applicable (terminal state A).

## Primary-source gap

Not applicable (terminal state A).

## Inscription-ready TeX block

Not applicable — the proposition is already inscribed in
`chapters/examples/landscape_census.tex` (lines 1748–1942). No new
inscription needed. Wave-2 A04 F3 should be **closed as unfounded**:
the reference resolves correctly in the compiled build.

For completeness, the existing inscription is quoted verbatim from
Vol I `landscape_census.tex`:

```tex
\begin{proposition}[Archetype-by-archetype
$\kappa + \kappa^!$ arithmetic with anomaly-ratio bridge;
\ClaimStatusProvedHere]
\label{prop:archetype-complementarity-bridge}
\index{complementarity!archetype-by-archetype}
\index{Trinity conductor!anomaly-ratio bridge}
\index{kappa plus kappa dual@$\kappa{+}\kappa^!$!archetype table}
\textup{[Regime: curved-central, Koszul locus;
Convention~\textup{\ref{conv:regime-tags}}.]}
The scalar complementarity sum
$K^\kappa(\cA) := \kappa(\cA) + \kappa(\cA^!)$ and the Trinity
conductor $K(\cA) := c(\cA) + c(\cA^!)$ are related, on the witness
landscape and its $\mathcal{W}$-family and $\mathcal{B}$-family extensions, by the
\emph{anomaly-ratio bridge}
\begin{equation}\label{eq:kappa-sum-rho-K-bridge}
 K^\kappa(\cA) \;=\; \varrho(\cA) \cdot K(\cA),
 \qquad
 \varrho(\cA) \;:=\; \frac{\kappa(\cA)}{c(\cA)},
\end{equation}
[... full table and scope declaration at landscape_census.tex:1774-1812 ...]
\end{proposition}
\begin{proof}
[... row-by-row verification at landscape_census.tex:1815-1942 ...]
\end{proof}
```

## Cross-consistency notes

- **Spine (Wave 1):** Bezrukavnikov A09 correctly cited
  Proposition~`archetype-complementarity-bridge` as the source of
  $K^\kappa = \varrho K$; the derivation there is consistent with the
  existing Vol I proof.
- **Refinement (Wave 2):** A04 F3 misidentified the reference as
  orphaned. The reference is present; A04's tabular derivation of the
  $\mathcal{B}$-row $(\varrho, K) = (1/6, 48) \mapsto K^\kappa = 8$ is
  consistent with landscape_census.tex:1795 and landscape_census.tex:1929.
- **CoHA treatise:** no direct interaction — the archetype bridge is
  Vol I scalar content, not CoHA lifting.
- **CLAUDE.md:** The five-theorem core (Theorem C derived-centre
  complementarity) cites $K^\kappa \in \{0, 8, 13, 250/3, 98/3\}$
  exactly as computed here; the $\mathsf{B}$-row Mukai-enhanced K3
  Heisenberg witness via Bruinier Heegner Chern-class reciprocity is
  the Vol III bridge, inscribed at Vol III
  `chapters/examples/k3_chiral_bialgebra_platonic.tex`
  Remark `rem:mukai-doubling-K-kappa`.
- **Build verification:** In Vol I `main.tex`:
  - Line 1138: `\include{chapters/frame/heisenberg_frame}` — fails here, recovered to `chiral_center_theorem.tex` via include chain.
  - Line 1763: `\input{chapters/examples/landscape_census}` — defines
    the proposition and its label.
  - LaTeX resolves `\ref{prop:archetype-complementarity-bridge}`
    across `\include` and `\input` boundaries identically within one
    document build.

## Action items

- **No inscription required** (terminal state A).
- **Wave-2 A04 F3** (`prop:archetype-complementarity-bridge` orphan
  claim) should be marked **resolved — unfounded** in the Wave-3
  closure ledger.
- **Recommendation:** add a `\phantomsection\label{}` mirror in
  `chiral_center_theorem.tex` near line 2859 referencing
  `prop:archetype-complementarity-bridge` is not needed — the label
  already resolves. But if future chapter reordering could move
  `landscape_census.tex` before `chiral_center_theorem.tex` or vice
  versa (they are already in that order), the current resolution
  continues to work since LaTeX `\ref` is position-independent within
  a build.
