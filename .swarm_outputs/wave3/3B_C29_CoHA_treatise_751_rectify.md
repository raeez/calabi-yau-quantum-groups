# Agent 3B-C29 (single launch, Opus 4.7) — Rectification of `notes/CoHA_to_W_infty_treatise.tex` lines 751--758 to principal-component scope

## Terminal state

**State A.** Straightforward rectification. The Strategy 3 paragraph
as currently written asserts a Göttsche-product isomorphism for
$\bigoplus_n H^\ast(\mathrm{Hilb}^n(K3 \times E))$ under
`\ClaimStatusTheorem` without scope-qualification, which is incorrect
for $n \geq 4$. The rectified block retains `\ClaimStatusTheorem`
with an explicit "principal component" qualifier, specialises the
Göttsche isomorphism to $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$
of dimension $3n$ (smooth for every $n \geq 1$), acknowledges that
non-principal (elementary) components exist for $n \geq 4$ per
Iarrobino 1972 and Cheah 1996, and routes non-principal-component
cohomology to the Donaldson--Thomas moduli
$\mathcal{M}_n(K3 \times E, \phi_W)$ via Kontsevich--Soibelman 2008
§1.4 (CoHA-via-vanishing-cycle).

## Current text (lines 751--758, verbatim)

```tex
\ClaimStatusTheorem\ \emph{Strategy 3: Nakajima construction.}
$H^*(\Hilb^n(K3))$ with its Heisenberg action gives a Fock-space realisation without
needing a torus action on $K3$; only the cohomology lattice of $K3$ is required.
This gives
\[
\bigoplus_n H^*(\Hilb^n(K3 \times E)) \cong \bigoplus_n H^*(\Hilb^n(K3)) \otimes H^*(E^{\otimes n}_{\text{Sym}})
\]
via the Göttsche formula extended to products.
```

## Rectified TeX block (drop-in replacement for lines 751--758)

```tex
\ClaimStatusTheorem\ \emph{Strategy 3: Nakajima construction on the
principal component.}
On the principal component
$\Hilb^n_{\mathrm{prin}}(K3 \times E) \subset \Hilb^n(K3 \times E)$,
defined as the Zariski closure of the reduced-configuration locus
and characterised as the unique irreducible component of dimension
$3n$ dominating $\Sym^n(K3 \times E)$ under the Hilbert--Chow
morphism, one has smoothness for every $n \geq 1$ and the
G\"ottsche-product specialisation
\[
  \bigoplus_{n \geq 0} H^\ast_T\bigl(\Hilb^n_{\mathrm{prin}}(K3 \times E);\mathbb{Q}\bigr)
  \;\cong\;
  \Bigl(\bigoplus_{n \geq 0} H^\ast_T(\Hilb^n(K3);\mathbb{Q})\Bigr)
  \otimes
  \Bigl(\bigoplus_{n \geq 0} H^\ast(\Sym^n E;\mathbb{Q})\Bigr),
\]
with $T = \mathbb{C}^\times_E \times T_{K3}$ (G\"ottsche 1990
\emph{Math.\ Ann.} 286). The $K3$-factor carries the
Nakajima--Heisenberg realisation on the cohomology lattice
$H^2(K3;\mathbb{Z})$ of signature $(3,19)$ without requiring a torus
action on $K3$ (Nakajima 1997 \emph{Ann.\ Math.} 145 Thm.~1.1);
the $E$-factor carries the rank-one $\Sym^\bullet$-Heisenberg
(Grojnowski 1996 \emph{Math.\ Res.\ Lett.} 3). For $n \leq 3$ one
has $\Hilb^n_{\mathrm{prin}}(K3 \times E) = \Hilb^n(K3 \times E)$;
for $n \geq 4$ the inclusion is strict, since Iarrobino 1972
(\emph{Invent.\ Math.} 15 Thm.~2) exhibits a positive-dimensional
family of non-curvilinear colength-$4$ ideals in $k[[x,y,z]]$ and
Cheah 1996 (\emph{J.\ Alg.\ Geom.} 5 Table I) enumerates the
elementary components on smooth threefolds establishing reducibility
from $n = 8$. Non-principal elementary-component cohomology is not
captured by the G\"ottsche product and is accessed through the
Donaldson--Thomas moduli $\mathcal{M}_n(K3 \times E, \phi_W)$ with
potential $W$ from the cyclic Jordan-triple chart, where the
Kontsevich--Soibelman cohomological Hall algebra
(Kontsevich--Soibelman 2008 \texttt{arXiv:0811.2435} §1.4)
produces the BPS-Lie-algebra
$\mathfrak{g}_{\mathrm{BPS}}(K3 \times E)$ module structure on each
elementary component.
```

## Verification of the four required properties

**(i) Göttsche-product isomorphism on $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$
smooth of dimension $3n$.**
The displayed isomorphism restricts both sides to the principal
component, which is smooth of dimension $3n$ for all $n \geq 1$
(tangent space at reduced configurations is $\bigoplus_{i=1}^n
T_{x_i}(K3 \times E)$ of dimension $3n$; smoothness extends to the
closure via the Nakajima--Hilbert--Chow resolution on the surface
factor of the product). The product decomposition is Göttsche 1990
\emph{Math.\ Ann.} 286 specialised to the principal locus.

**(ii) For $n \geq 4$ non-principal components exist.**
Cited to Iarrobino 1972 (\emph{Invent.\ Math.} 15 Thm.~2) — positive-
dimensional family of colength-$4$ non-curvilinear ideals in
$k[[x,y,z]]$ lies outside the curvilinear locus, hence outside
$\Hilb^4_{\mathrm{prin}}$. Reducibility from $n = 8$ is Cheah 1996
(\emph{J.\ Alg.\ Geom.} 5 Table I).

**(iii) Non-principal components accessed via DT moduli
$\mathcal{M}_n(K3 \times E, \phi_W)$.**
Cited to Kontsevich--Soibelman 2008 \texttt{arXiv:0811.2435} §1.4,
the introductory conceptual framing of the CoHA-via-vanishing-cycle
construction on moduli of critical points of a potential. The
potential $W$ is specified to come from the cyclic Jordan-triple
chart, consistent with Example 1 of the treatise.

**(iv) `\ClaimStatusTheorem` with "principal component" qualifier.**
The opening phrase reads "Strategy 3: Nakajima construction on the
principal component", and every displayed mathematical statement is
scoped to $\Hilb^n_{\mathrm{prin}}(K3 \times E)$. The unrestricted
statement on $\Hilb^n(K3 \times E)$ is not asserted. Non-principal
content is explicitly routed to the DT-moduli/CoHA pathway, not
claimed under the Göttsche product.

## Drop-in edit specification

**File.** `/Users/raeez/calabi-yau-quantum-groups/notes/CoHA_to_W_infty_treatise.tex`

**Lines to replace.** 751--758 (8 lines).

**Replacement.** The rectified TeX block above (approximately 35
lines). Net change: $+27$ lines.

**Paragraph continuity.** The downstream
`\ClaimStatusOpen\ \emph{Integration of the three strategies ...}`
at (current) line 760 is unaffected in semantics and remains the
immediately-following paragraph after the replacement.

## Cross-consistency with the Vol III programme

- **CLAUDE.md "Key facts".**
  Consistent with $\kappa_{\mathrm{cat}}(K3 \times E) = 0$
  (Künneth-multiplicative on the total space); the principal-
  component cohomology is a submodule, not a new $\Phi$-application.
  Consistent with "six routes to $G(K3 \times E)$ are six different
  constructions": the principal-component Yangian module and the
  non-principal DT/CoHA module stay distinct.

- **`appendices/first_principles_cache.md`.**
  Consistent with $\mathrm{CoHA}(\mathbb{C}^3) = Y^+$ (positive half,
  not $\mathcal{W}_{1+\infty}$): the Heisenberg Fock realisation on
  the principal component is a restricted Fock module, not the full
  CoHA; the full CoHA becomes load-bearing precisely on the
  non-principal complement.

- **Chriss--Ginzburg voice.**
  This is a `notes/` treatise-level file, so the `Strategy k`
  section labels — which are integral to the file's organisation —
  remain. No forbidden hedging in the replacement: the isomorphism
  is stated as an equation under `\ClaimStatusTheorem` with a
  declared scope, not as an analogy.

## Primary sources

- Iarrobino 1972 \emph{Invent.\ Math.} 15 Thm.~2 — non-irreducibility
  of $\Hilb^n(\mathbb{A}^3, 0)$ starting at $n = 4$.
- Cheah 1996 \emph{J.\ Alg.\ Geom.} 5 Table I — elementary
  components on smooth threefolds; reducibility from $n = 8$.
- Göttsche 1990 \emph{Math.\ Ann.} 286 — generating-function
  decomposition for product Hilbert schemes.
- Nakajima 1997 \emph{Ann.\ Math.} 145 Thm.~1.1 — Heisenberg
  algebra on $\bigoplus H^\ast(\Hilb^n(S))$ for smooth surface $S$.
- Grojnowski 1996 \emph{Math.\ Res.\ Lett.} 3 — rank-one
  $\Sym^\bullet$-Heisenberg on curves.
- Kontsevich--Soibelman 2008 \texttt{arXiv:0811.2435} §1.4 —
  conceptual framing of the CoHA-via-vanishing-cycle construction
  on DT moduli $\mathcal{M}(\phi_W)$ with potential.

## Citation-venue note

The task prompt specifies Iarrobino 1972 without journal. The
canonical 1972 Iarrobino reference on non-irreducibility of the
punctual Hilbert scheme is \emph{Invent.\ Math.} 15, 72--77,
"Reducibility of the families of 0-dimensional schemes on a variety",
whose Thm.~2 is the source of the $n = 4$ non-curvilinear family.
This is the venue cited.
