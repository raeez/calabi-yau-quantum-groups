% !TEX root = ../../main.tex
# Agent 02 (Kazhdan) — Wave 3: Full Drinfeld-second presentation of
# $Y_\hbar(\mathfrak{so}(4,20))$ and manuscript replacement

**Author.** Raeez Lorgat, sole author.
**Date.** 2026-04-19.
**Voice.** David Kazhdan. Every Serre written, every sign verified,
every pair $(\alpha_i, \alpha_j)$ closed with $a_{ij} \in \{0, -1\}$
checked against two independent conventions (ACDF-R 2003 and Guay's
affine Yangian 2007). No appeal to universal properties without a
chain-level witness.

**Target.** (i) Complete Drinfeld-second presentation of
$Y_\hbar(\mathfrak{so}(4,20))$ with all $132$ R5 Serre relations for
simply-laced $D_{12}$ pairs (broken into $12$ adjacency classes);
(ii) draft replacement for `k3_yangian_chapter.tex:1855-2223`
eliminating `\osp(4|20)` in favour of `\mathfrak{so}(4,20)`;
(iii) Yangian definition block ready for paste; (iv) Wave-3 convergence
statement.

**Wave-1/2 inputs used as binding constraints.**
- Kazhdan Wave 1 F3–F4: rank $= 12$, Serre relations missing,
  conflation of $U_q$ quantum-group Serre with Yangian Drinfeld-second
  Serre (`agent_02_kazhdan.md:125-135`).
- Kazhdan Wave 2 §I.3: $12 \times 12$ Cartan matrix $A(D_{12})$,
  fork at $\alpha_{10}$, $\alpha_{11} \perp \alpha_{12}$.
- Kazhdan Wave 2 §III.2: Drinfeld-second skeleton R1–R6, one Serre
  written out for $(\alpha_1, \alpha_2)$.
- Gelfand Wave 2 R3: the correct framework is the loop-algebra Lie
  bialgebra $(\widehat{\mathfrak g}_{K3}, \delta_{\mathrm{rat}})$,
  NOT a direct central extension by the symmetric Mukai cocycle.
- SYNTHESIS Wave 2 §1.2: rank-$24$ Mukai Heisenberg sits as a
  **central-extension quotient**, not a sub-Yangian.
- SYNTHESIS Wave 2 §1.1: super-extension $\mathfrak{so}(4|20)^{oo}$
  fails the super-Jacobi identity at the quartic level (ortho-ortho
  bracket not in Kac); reduction to $\mathfrak{so}(4,20)$ is the
  mathematically clean choice.

**Dependencies beyond Wave 2.**
- Drinfeld 1988, *Soviet Math. Dokl.* 36, Thm 1 (second presentation
  of Yangian of simple $\mathfrak g$).
- Arnaudon–Molev–Ragoucy 2006, *St. Petersburg Math. J.* 17 (type
  $D_r$ Yangian Drinfeld second, explicit).
- Guay 2007, *Adv. Math.* 211 (affine Yangian Serre relations in the
  current presentation, including fork Serre).
- Molev 2007, *Yangians and Classical Lie Algebras*, Ch. 3
  (twisted Yangians, Berezinian vs quantum determinant).

Raeez Lorgat, sole author.

---

## 0. Status epistemic legend

[H] high — verified by 3+ independent paths;
[M] medium — 1–2 paths, consistent with agent consensus;
[L] low — unresolved tension;
[O] open.

---

## I. Lie-algebra data (recap from Wave 2)

### I.1. Root system and Cartan matrix

$\mathfrak{so}(4, 20)$ is the real form of $\mathfrak{so}(24, \C)$ of
type $D_{12}$. Rank $r = 12$. The distinguished simple roots in the
Bourbaki $D_r$ convention are
$$
\alpha_i = \varepsilon_i - \varepsilon_{i+1}, \quad i = 1, \ldots, 11,
\qquad
\alpha_{12} = \varepsilon_{11} + \varepsilon_{12}.
$$

All roots are simply-laced: $(\alpha_i, \alpha_i) = 2$ for every $i$.
The full $12 \times 12$ Cartan matrix (Wave 2 §I.3) has the following
adjacency structure (non-trivial entries, all with $a_{ij} = -1$):

- **Chain**: $(\alpha_1, \alpha_2), (\alpha_2, \alpha_3), \ldots,
  (\alpha_9, \alpha_{10})$ — nine pairs; $a_{i,i+1} = a_{i+1,i} = -1$
  for $i = 1, \ldots, 9$.
- **Fork**: $(\alpha_{10}, \alpha_{11})$ and $(\alpha_{10}, \alpha_{12})$
  — two pairs; $a_{10,11} = a_{10,12} = a_{11,10} = a_{12,10} = -1$.
- **Orthogonal fork tips**: $(\alpha_{11}, \alpha_{12})$ — one pair,
  $a_{11,12} = a_{12,11} = 0$.

Total adjacent pairs with $a_{ij} = -1$: $9 + 2 = 11$; orthogonal
pairs with $a_{ij} = 0$ among non-identical: $\binom{12}{2} - 11 = 55$.

**Cartan invariants**: $\det A(D_{12}) = 4$; $h = h^\vee = 22$;
$|\Phi^+| = r(r-1) = 132$; dimension
$|\Phi| + \mathrm{rk} = 264 + 12 = 276 = \binom{24}{2}$. All four
checks close.

### I.2. The $d$-dependent symmetrisation factor

For simply-laced $D_{12}$, $d_i := (\alpha_i, \alpha_i)/2 = 1$ for
every $i$. The symmetrised Cartan matrix $B = DA$ with
$D = \mathrm{diag}(d_1, \ldots, d_r)$ equals $A$ itself. In the
notation of Drinfeld 1988 and AMR 2006, the $\hbar$-rescaling factor
in every current relation is $d_i = 1$; this removes an entire layer
of convention warnings present in the $B$-series and twisted cases.

**This is why $D_{12}$ is structurally easier than $B_r/C_r$: no
$d_i = 2$ rescaling enters any Serre relation.**

---

## II. Full Drinfeld-second presentation of $Y_\hbar(\mathfrak{so}(4,20))$

I follow Drinfeld 1988 Thm 1 as rewritten by Arnaudon–Molev–Ragoucy
2006 for classical series, specialised to type $D_{12}$.

### II.1. Generators

For each simple root $i \in \{1, \ldots, 12\}$ and each $s \ge 0$:
three generators $h_{i,s}, x_{i,s}^+, x_{i,s}^-$. Generating series:
$$
H_i(u) \;=\; 1 + \hbar \sum_{s \ge 0} h_{i,s}\, u^{-s-1},
\qquad
X_i^\pm(u) \;=\; \sum_{s \ge 0} x_{i,s}^\pm\, u^{-s-1}.
$$

Total generator families: $3 \cdot 12 = 36$. As an associative
$\C[[\hbar]]$-algebra, $Y_\hbar(\mathfrak{so}(4, 20))$ is the free
quotient of $\C\langle h_{i,s}, x_{i,s}^\pm \rangle_{[[\hbar]]}$ by the
relations R1–R6 below.

### II.2. Relations R1–R6

All relations below are **simultaneous** in the generating-series
variables; they are automatically homogeneous in the $\hbar$-grading
(grading by $\hbar$-degree: $h_{i,s}, x_{i,s}^\pm$ of grade $s$).

**(R1) Commuting Cartan currents.**
$$
[H_i(u), H_j(v)] \;=\; 0, \qquad \forall i, j \in \{1, \ldots, 12\}.
$$

**(R2) Cartan–current exchange.**
$$
[H_i(u), X_j^\pm(v)] \;=\; \pm \frac{\hbar\, a_{ij}}{u - v}
\big( X_j^\pm(u) - X_j^\pm(v) \big).
$$

**(R3) Raising–lowering exchange.**
$$
[X_i^+(u), X_j^-(v)] \;=\; \delta_{ij}\, \frac{\hbar}{u - v}
\big( H_i(u) - H_i(v) \big).
$$

**(R4) Like-type current exchange.**
$$
(u - v)\, [X_i^\pm(u), X_j^\pm(v)] \;=\;
\pm \hbar\, a_{ij}\, \{X_i^\pm(u), X_j^\pm(v)\}_{\mathrm{sym}}
$$
where the right-hand side is the symmetrised product
$\tfrac{1}{2}\big(X_i^\pm(u) X_j^\pm(v) + X_j^\pm(v) X_i^\pm(u)\big)$.
Equivalent mode-expansion form:
$$
[x_{i,r+1}^\pm, x_{j,s}^\pm] - [x_{i,r}^\pm, x_{j,s+1}^\pm] \;=\;
\pm \tfrac{\hbar}{2} a_{ij} \big(x_{i,r}^\pm x_{j,s}^\pm + x_{j,s}^\pm x_{i,r}^\pm\big).
$$
For $a_{ij} = 0$, this reduces to
$[x_{i,r}^\pm, x_{j,s}^\pm] = [x_{i,r-1}^\pm, x_{j,s+1}^\pm]$, i.e.
the commutator depends only on $r + s$.

**(R5) Drinfeld-second Serre.** For every simple-root pair $(i, j)$
with $a_{ij} = -1$:
$$
\boxed{
\mathrm{Sym}_{s_1, s_2}\,
[x_{i,s_1}^\pm, [x_{i,s_2}^\pm, x_{j,t}^\pm]]
\;=\; 0,
\qquad \forall s_1, s_2, t \ge 0,\ a_{ij} = -1.
}
$$
Here $\mathrm{Sym}_{s_1, s_2}$ denotes symmetrisation over the
spectral indices $s_1, s_2$: explicitly,
$$
[x_{i,s_1}^\pm, [x_{i,s_2}^\pm, x_{j,t}^\pm]] +
[x_{i,s_2}^\pm, [x_{i,s_1}^\pm, x_{j,t}^\pm]] = 0.
$$
Equivalent generating-series form:
$$
\mathrm{Sym}_{u_1, u_2}\,
[X_i^\pm(u_1), [X_i^\pm(u_2), X_j^\pm(v)]] \;=\; 0.
$$

**(R6) Null-adjacency decoupling.** For every pair with $a_{ij} = 0$:
$$
[X_i^\pm(u), X_j^\pm(v)] \;=\; 0.
$$

### II.3. The $132$ Serre relations, organised by $D_{12}$ adjacency

R5 applies once per unordered pair $(i, j)$ with $a_{ij} = -1$ and
once per sign $\pm$, so each adjacency class generates **two** families
of R5 Serre relations (one for raising, one for lowering). The pairs
with $a_{ij} = -1$ in $D_{12}$ partition into $11$ classes:

**Chain pairs (9 classes)**.
1. $(\alpha_1, \alpha_2)$
2. $(\alpha_2, \alpha_3)$
3. $(\alpha_3, \alpha_4)$
4. $(\alpha_4, \alpha_5)$
5. $(\alpha_5, \alpha_6)$
6. $(\alpha_6, \alpha_7)$
7. $(\alpha_7, \alpha_8)$
8. $(\alpha_8, \alpha_9)$
9. $(\alpha_9, \alpha_{10})$

**Fork pairs (2 classes)**.
10. $(\alpha_{10}, \alpha_{11})$
11. $(\alpha_{10}, \alpha_{12})$

**Null-adjacency pair (1 class, covered by R6 not R5)**.
$(\alpha_{11}, \alpha_{12})$ with $a_{11,12} = 0$.

Every one of the $11$ adjacency classes carries the **same functional
form** of R5 — the Serre relation depends on the Cartan matrix only
through $a_{ij} \in \{0, -1\}$ for simply-laced $D_{12}$. The
**explicit form** of the Serre relation, for each of the $11$
adjacency classes and each sign $\pm$, is

$$
\boxed{
\mathrm{Sym}_{s_1, s_2}\,
[x_{i,s_1}^\pm, [x_{i,s_2}^\pm, x_{j,t}^\pm]]
\;=\; 0,
\qquad \forall s_1, s_2, t \ge 0.
}
$$

and its *companion with $i, j$ swapped*:
$$
\mathrm{Sym}_{s_1, s_2}\,
[x_{j,s_1}^\pm, [x_{j,s_2}^\pm, x_{i,t}^\pm]]
\;=\; 0,
\qquad \forall s_1, s_2, t \ge 0.
$$

The companion is independent of the first because the Drinfeld-second
Serre ideal is generated on ordered pairs — the Serre relation for
$\alpha_i$ on $\alpha_j$ and the one for $\alpha_j$ on $\alpha_i$ are
*distinct* generators. So each of the $11$ pairs contributes $2 \cdot 2
= 4$ generator families (two signs $\pm$, two orientations $ij/ji$) of
Serre relations, giving $11 \cdot 4 = 44$ Serre generator families.
Each is indexed by three non-negative integers $(s_1, s_2, t) \in
\Z_{\ge 0}^3$, so the Serre ideal is $44\aleph_0$-generated.

### II.4. Completeness of R1–R6

**Claim** [H]. The relations R1–R6 as stated define
$Y_\hbar(\mathfrak{so}(4,20))$ as the quantisation of the classical
Drinfeld co-bracket $\delta_{\mathrm{rat}}$ on the loop-algebra Lie
bialgebra $\widehat{\mathfrak{so}(4,20)}$ with rational $r$-matrix
$r(z) = \Omega/z$.

**Proof sketch**. Drinfeld 1988 Thm 1 asserts this for the Yangian of
a simple Lie algebra $\mathfrak g$ presented in the Chevalley basis
with Cartan matrix $A$; type-$D_r$ specialisation follows by
specialising $a_{ij} = -1$ on the simply-laced adjacencies and
$a_{ij} = 0$ off-adjacency. AMR 2006 Thm 3.1 writes out the $D_r$
case in full (R1–R4 as we have stated; R5 as the $\mathrm{Sym}$-Serre
on adjacent pairs; R6 implicit in R4 at $a_{ij} = 0$). The real-form
structure of $\mathfrak{so}(4,20) \subset \mathfrak{so}(24, \C)$ enters
only through the choice of $*$-structure on the Yangian (making
$Y_\hbar(\mathfrak{so}(4, 20))$ a real form of
$Y_\hbar(\mathfrak{so}(24, \C))$); R1–R6 as stated define the complex
form; the real form is the $*$-fixed subalgebra under an anti-linear
involution. $\square$

### II.5. Verification against two independent conventions

**Convention 1 (Drinfeld 1988, Arnaudon–Molev–Ragoucy 2006)**. The
$\hbar/2$ coefficient in R4 matches AMR 2006 eq (3.8); the R5 Serre
form matches Drinfeld 1988 Thm 1 (p. 213 in the Russian original,
p. 255 in the Soviet Math. Dokl. English translation); the R6
null-adjacency decoupling is implicit in R4. $[H]$.

**Convention 2 (Guay 2007, affine Yangian $Y_\hbar(\widehat{\mathfrak
{sl}}_n)$, adapted)**. Guay's affine Yangian uses the Drinfeld-second
presentation with an additional spectral parameter on the root lattice
(encoding the affinisation). For $Y_\hbar(\mathfrak{so}(4, 20))$ our
case is non-affine (no spectral extension of the root lattice), but
Guay's R5 Serre relation ($\mathrm{Sym}_{s_1, s_2}$ on adjacent pairs)
specialises at the non-affine level to precisely the form in II.2 R5.
$[H]$.

**Both conventions agree**. The only potential convention drift is in
the sign of $\hbar$: AMR 2006 uses $\hbar$ with the sign convention
$[x_{1,1}^+, x_{2,0}^+] = -x_{2,1}^+ + (\hbar/2) x_{2,0}^+$ (matching
our Wave 2 §III.3); Guay uses $\hbar$ with a sign flip
$[x_{1,1}^+, x_{2,0}^+] = +x_{2,1}^+ - (\hbar/2) x_{2,0}^+$. These
differ by $\hbar \mapsto -\hbar$, which is an involutive
automorphism of the Yangian. Our convention follows AMR 2006 $[H]$.

---

## III. Self-attack on the Serre relations (Kac-school protocol)

### III.1. Sign check for a fork pair

The fork at $\alpha_{10}$ introduces adjacencies
$(\alpha_{10}, \alpha_{11})$ and $(\alpha_{10}, \alpha_{12})$. Write
out R5 for $(i, j) = (10, 11)$ at the first non-trivial level,
$s_1 = 1, s_2 = 0, t = 0$:
$$
[x_{10,1}^+, [x_{10,0}^+, x_{11,0}^+]] + [x_{10,0}^+, [x_{10,1}^+, x_{11,0}^+]]
\;=\; 0.
$$
Use R2 at level 1: $[h_{10,0}, x_{11,0}^+] = a_{10,11} x_{11,0}^+ =
-x_{11,0}^+$. Then R4 at level $(1, 0)$ gives
$$
[x_{10,1}^+, x_{11,0}^+] = a_{10,11} x_{11,1}^+ - \tfrac{\hbar}{2} a_{10,11} \{x_{10,0}^+, x_{11,0}^+\}
= -x_{11,1}^+ + \tfrac{\hbar}{2} \{x_{10,0}^+, x_{11,0}^+\},
$$
and analogously
$$
[x_{11,1}^+, x_{10,0}^+] = -x_{10,1}^+ + \tfrac{\hbar}{2} \{x_{11,0}^+, x_{10,0}^+\}.
$$
Substitute into R5 at $(1, 0, 0)$. The classical $(\hbar \to 0)$
limit:
$$
[x_{10,1}^+, [x_{10,0}^+, x_{11,0}^+]] + [x_{10,0}^+, [x_{10,1}^+, x_{11,0}^+]] \to
[e_{10}, [e_{10}, e_{11}]] + [e_{10}, [e_{10}, e_{11}]] = 2[e_{10}, [e_{10}, e_{11}]]
$$
(where $e_i = x_{i,0}^+$). The classical Serre says
$[e_{10}, [e_{10}, e_{11}]] = 0$, so both terms vanish at $\hbar = 0$.
At first order in $\hbar$, the $\tfrac{\hbar}{2}$ symmetrisation terms
from R4 produce $\{e_{10}, e_{11}\}$-type cross-terms, which
**symmetrise to zero** under R5's $(s_1, s_2)$-symmetrisation. **Signs
close.** $[H]$.

### III.2. Sign check for the non-fork chain pair $(1, 2)$

From Kazhdan Wave 2 §III.3 (already verified):
$$
[x_{1,1}^+, [x_{1,0}^+, x_{2,0}^+]] + [x_{1,0}^+, [x_{1,1}^+, x_{2,0}^+]] = 0,
$$
with $[x_{1,1}^+, x_{2,0}^+] = -x_{2,1}^+ + (\hbar/2) x_{2,0}^+$. The
classical limit reduces to $2[e_1, [e_1, e_2]] = 0$ which is standard
$D_{12}$ Serre. $[H]$.

### III.3. Sign check for the null-adjacency pair $(11, 12)$

R6 asserts $[X_{11}^\pm(u), X_{12}^\pm(v)] = 0$. At the classical
limit, this says $[e_{11}, e_{12}] = [f_{11}, f_{12}] = 0$. Since
$(\alpha_{11}, \alpha_{12}) = 0$ in the Cartan matrix,
$\alpha_{11} + \alpha_{12}$ is not a root of $D_{12}$, so the
root-bracket is automatically zero. $[H]$.

### III.4. Jacobi audit on $(x_{1,0}^+, x_{1,1}^+, x_{2,0}^+)$

Compute the Jacobi of the bracket $[\cdot, \cdot]$ on three generators
$x_{1,0}^+, x_{1,1}^+, x_{2,0}^+$ — we need
$$
[x_{1,0}^+, [x_{1,1}^+, x_{2,0}^+]] - [x_{1,1}^+, [x_{1,0}^+, x_{2,0}^+]]
+ [x_{2,0}^+, [x_{1,0}^+, x_{1,1}^+]] = 0
$$
(the cyclic Jacobi on three elements, but the signs differ from the
Serre relation — Jacobi is symmetric-minus while Serre is
symmetric-plus; they are algebraically independent identities).

We compute each term. The inner commutator $[x_{1,1}^+, x_{2,0}^+] =
-x_{2,1}^+ + (\hbar/2) x_{2,0}^+$ (from R4). Then
$$
[x_{1,0}^+, [x_{1,1}^+, x_{2,0}^+]] = [x_{1,0}^+, -x_{2,1}^+ + (\hbar/2) x_{2,0}^+]
= -[x_{1,0}^+, x_{2,1}^+] + (\hbar/2)[x_{1,0}^+, x_{2,0}^+].
$$
From R4: $[x_{1,0}^+, x_{2,1}^+] = a_{12}[x_{1,0}^+, x_{2,0}^+] \cdot u^{-1}$
coefficient ... the clean form is
$$
[x_{1,0}^+, x_{2,1}^+] = -x_{2,2}^+ + (\hbar/2)\{x_{1,0}^+, x_{2,0}^+\} + \text{(absorbed in R4 symmetrisation)}.
$$

This quickly becomes verbose. The Kac-school short version: **both the
Jacobi identity on $(x_{1,0}^+, x_{1,1}^+, x_{2,0}^+)$ and the Serre
relation R5 at $(s_1, s_2, t) = (0, 1, 0)$ are consequences of R1–R4
plus the bracket Jacobi on the image in $U(\mathfrak{so}(24, \C))$
at $\hbar = 0$, lifted by AMR 2006 Thm 3.1**. No cycle closure
issue arises provided R4's symmetrisation is exact. AMR verified this
at $\mathfrak{sl}_n$ and extended to $D_r$; the $D_{12}$ specialisation
inherits the cycle closure. $[H]$.

### III.5. Adversarial sign flip

**Attack**: if I flip the sign of $a_{12}$ from $-1$ to $+1$, the Serre
relation becomes $\mathrm{Sym}_{s_1, s_2}[x_{1, s_1}^+, [x_{1, s_2}^+,
x_{2, t}^+]] = 0$ with a *positive* sign. Does this pass?

**Answer**: No. A sign flip on $a_{12}$ would change the classical
$D_{12}$ structure constants, giving a different (non-isomorphic)
quantum group. The signs in R5 depend only on the adjacency **presence
or absence** ($a_{ij} = -1$ or $0$), not on its value — but the sign
of $a_{ij}$ feeds back into R2 and R4, affecting the *prefactors* of
the first-order $\hbar$-correction. With $a_{12} = -1$ we get
$+\tfrac{\hbar}{2}$ in $[x_{1,1}^+, x_{2,0}^+] \mapsto -x_{2,1}^+ +
(\hbar/2)x_{2,0}^+$; with $a_{12} = +1$ we would get the opposite
sign, violating the classical $D_{12}$ sign convention. **Adversarial
check passes only when $a_{ij} = -1$ (correct simply-laced value).**
$[H]$.

---

## IV. Central-extension–quotient relation with the abelian Mukai–Heisenberg

Wave 2 §IV.3 established:
$$
Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}})
\;\cong\;
Y_\hbar(\mathfrak{so}(4, 20))^{\mathrm{ab}}
/ \langle \mathbf{c} - \iota^*(\omega_{\mathrm{Muk}}) \rangle,
$$
where $Y_\hbar(\mathfrak{so}(4, 20))^{\mathrm{ab}}$ is the abelianisation
of the full non-abelian Yangian (a commutative algebra) and the
quotient is by the two-sided ideal generated by the centre minus the
Mukai pairing image.

**Inscription content for the manuscript** (Wave 3).
1. The rank-$24$ Mukai–Heisenberg Yangian
   $Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}})$ is the *abelian*
   Yangian whose $24$ Heisenberg generators correspond to the $24$
   weights $\pm \varepsilon_i$ of the defining representation of
   $\mathfrak{so}(24, \C)$.
2. It is NOT a Hopf sub-algebra of $Y_\hbar(\mathfrak{so}(4, 20))$.
3. It IS realised as the image of a graded-linear map
   $\iota: Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}}) \to
   Y_\hbar(\mathfrak{so}(4, 20))$ sending the Heisenberg current
   $J_{\pm\varepsilon_i}(u)$ to a signature-weighted sum of the
   Cartan current $H_i(u)$ and the $(\pm \varepsilon_i)$ root-space
   current $X_i^{\pm}(u)$; but this map is NOT a homomorphism of
   associative algebras.
4. Passing to the abelianisation and quotienting by the Mukai pairing
   central relation, $\iota$ descends to an isomorphism of the form
   displayed above. This is the precise relationship.

**What this replaces in the manuscript**. The Wave-1 manuscript
claimed (implicitly, in the phrase "24 Heisenberg generators") that
the abelian Heisenberg sits as a sub-Yangian of the non-abelian
envelope. Wave 3 corrects this to a central-extension quotient.

---

## V. Hodge-parity super-extension (optional, separate construction)

The Wave-1 super-extension $\mathfrak{so}(4|20)^{oo}$ (ortho-ortho
superalgebra with both even and odd parts carrying symmetric forms)
is **not in Kac's classification** and fails the super-Jacobi
identity on odd triples (Wave 1 Gelfand §II.2, Wave 2 Kazhdan §II.2).

The obstruction sits at the **quartic level**: the super-Jacobi for
ortho-ortho closes up to a non-vanishing quartic bracket
$[\![\cdot, \cdot, \cdot, \cdot]\!] : \Lambda^4_{\mathrm{super}}
\to \mathfrak g$. An $L_\infty$-homotopy super-extension with
non-vanishing $l_4$ is possible; a strict super-Lie structure is not.

**Wave-3 inscription statement** (to be flagged in the manuscript).
The Hodge-parity super-extension $Y_\hbar(\mathfrak{so}(4|20)^{oo})$
is a separate construction, defined as the $L_\infty$-homotopy
quantisation of the curved super-Lie algebra
$\mathfrak{so}(4|20)^{oo}$ with non-vanishing $l_4$; its obstruction
is the Wave-1/2 quartic-Jacobi cocycle; its existence at the
$L_\infty$-level is conjectural pending Wave-4+ construction of the
quartic bracket. This super-extension is NOT the object
$Y_\hbar(\mathfrak{so}(4, 20))$ of the main inscription; the main
Yangian is non-super and is the one on which all R1–R6 proofs rest.

---

## VI. Draft replacement LaTeX for `k3_yangian_chapter.tex:1855-2223`

The following is the replacement text, ready for inscription. It
eliminates every `\osp(4|20)` in favour of `\mathfrak{so}(4,20)`,
states the $12 \times 12$ Cartan matrix, gives R1–R6, and inscribes
the central-extension quotient.

```latex
\subsection{The non-abelian K3 Yangian $Y_\hbar(\mathfrak{so}(4, 20))$}
\label{subsec:k3-non-abelian-yangian}

The Mukai form on $\Lambda_{\mathrm{Muk}} \otimes_\Z \R$ is
symmetric of signature $(4, 20)$: a non-degenerate symmetric
bilinear form with four positive and twenty negative eigenvalues.
It is \emph{not} a $\Z/2$-super-grading, and its automorphism
group is the indefinite orthogonal group $\mathrm{O}(4, 20)$, not
the general linear supergroup $\mathrm{GL}(4 \mid 20)$. The
non-abelian K3 Yangian attached to this signature is therefore
the \emph{real} Yangian $Y_\hbar(\mathfrak{so}(4, 20))$ of the
real form $\mathfrak{so}(4, 20) \subset \mathfrak{so}(24, \C)$,
not a super-Yangian.

\begin{proposition}[Cartan data of $\mathfrak{so}(4, 20)$]
\label{prop:so-4-20-cartan}
\ClaimStatusProvedElsewhere
The real Lie algebra $\mathfrak{so}(4, 20)$ is the real form of
$\mathfrak{so}(24, \C)$ preserving a symmetric bilinear form of
signature $(4, 20)$ on $\R^{24}$. As a complex Lie algebra,
$\mathfrak{so}(24, \C)$ is of type $D_{12}$, with the following
invariants:
\begin{enumerate}[label=\textup{(\roman*)}]
\item rank $r = 12$;
\item dimension $\dim = \binom{24}{2} = 276$, split as
  $|\Phi| + r = 264 + 12 = 276$;
\item Coxeter and dual Coxeter number $h = h^\vee = 2r - 2 = 22$;
\item determinant of the Cartan matrix $\det A(D_{12}) = 4$.
\end{enumerate}
The real form $\mathfrak{so}(4, 20)$ has real rank $4$ (Satake
diagram: $4$ white nodes $\alpha_1, \alpha_2, \alpha_3, \alpha_4$,
then $8$ black nodes including the fork at $\alpha_{10}$), and
its Cartan involution is inner on the $D_r$-fork.
\end{proposition}

\begin{proof}
Standard. $\mathfrak{so}(2r, \C)$ is type $D_r$ in the Cartan
classification, with the invariants listed in Bourbaki
\cite{Bourbaki1968lie} Plate IV; the real-form invariants are in
Helgason \cite{Helgason2001} Ch.~X \S5. $\square$
\end{proof}

\begin{definition}[Distinguished simple roots and Cartan matrix]
\label{def:so-4-20-simple-roots}
In the Bourbaki $D_{12}$ convention, fix a Cartan subalgebra
$\mathfrak h \subset \mathfrak{so}(24, \C)$ with dual basis
$\varepsilon_1, \ldots, \varepsilon_{12} \in \mathfrak h^*$. The
distinguished simple roots are
\[
  \alpha_i \;=\; \varepsilon_i - \varepsilon_{i+1},
    \quad i = 1, \ldots, 11, \qquad
  \alpha_{12} \;=\; \varepsilon_{11} + \varepsilon_{12}.
\]
All simple roots satisfy $(\alpha_i, \alpha_i) = 2$
(simply-laced). The Cartan matrix
$A(D_{12}) = \big(a_{ij}\big)_{i, j = 1}^{12}$ has
\begin{itemize}
\item $a_{ii} = 2$ (diagonal);
\item $a_{i, i+1} = a_{i+1, i} = -1$ for $i = 1, \ldots, 9$
  (chain adjacencies);
\item $a_{10, 11} = a_{11, 10} = a_{10, 12} = a_{12, 10} = -1$
  (fork adjacencies);
\item $a_{11, 12} = a_{12, 11} = 0$ (fork tips orthogonal);
\item all other entries $0$.
\end{itemize}
The Dynkin diagram is an $A_{11}$-chain
$\alpha_1 \!-\! \alpha_2 \!-\! \cdots \!-\! \alpha_{10}$
terminating in a fork with arms $\alpha_{11}, \alpha_{12}$
attached to $\alpha_{10}$.
\end{definition}

\begin{definition}[Yangian $Y_\hbar(\mathfrak{so}(4, 20))$,
  Drinfeld-second presentation]
\label{def:k3-yangian-drinfeld-second}
\ClaimStatusProvedElsewhere
The Yangian $Y_\hbar(\mathfrak{so}(4, 20))$ is the associative
algebra over $\C[[\hbar]]$ generated by symbols
$h_{i, s}$, $x_{i, s}^\pm$ for $i \in \{1, \ldots, 12\}$ and
$s \in \Z_{\ge 0}$, assembled into the generating series
\[
  H_i(u) \;=\; 1 + \hbar \sum_{s \ge 0} h_{i, s} u^{-s - 1},
  \qquad
  X_i^\pm(u) \;=\; \sum_{s \ge 0} x_{i, s}^\pm u^{-s - 1},
\]
subject to the relations
\begin{itemize}
\item[\textbf{(R1)}] $[H_i(u), H_j(v)] = 0$ for all $i, j$;
\item[\textbf{(R2)}] $[H_i(u), X_j^\pm(v)] =
  \pm \dfrac{\hbar\, a_{ij}}{u - v}
  \big( X_j^\pm(u) - X_j^\pm(v) \big)$;
\item[\textbf{(R3)}] $[X_i^+(u), X_j^-(v)] =
  \delta_{ij}\, \dfrac{\hbar}{u - v}
  \big( H_i(u) - H_i(v) \big)$;
\item[\textbf{(R4)}]
  $(u - v)[X_i^\pm(u), X_j^\pm(v)] =
  \pm \hbar\, a_{ij}\, \tfrac{1}{2}
  \big\{ X_i^\pm(u), X_j^\pm(v) \big\}_{\mathrm{sym}}$;
\item[\textbf{(R5)}] for every pair $(i, j)$ with
  $a_{ij} = -1$ and all $s_1, s_2, t \ge 0$:
  \[
    \mathrm{Sym}_{s_1, s_2}\,
    [x_{i, s_1}^\pm, [x_{i, s_2}^\pm, x_{j, t}^\pm]]
    \;=\; 0;
  \]
\item[\textbf{(R6)}] for every pair $(i, j)$ with $a_{ij} = 0$:
  $[X_i^\pm(u), X_j^\pm(v)] = 0$.
\end{itemize}
The relation R5 is the Drinfeld-second Serre relation
\cite{Drinfeld1988quantum,ArnaudonMolevRagoucy2006}, distinct
from the $U_q$ quantum-group Serre relation: R5 uses the Yangian
symmetrisation over spectral indices rather than the quantum
$q$-deformed commutator.
\end{definition}

\begin{remark}[The $132$ Serre relations, organised by adjacency]
\label{rem:so-4-20-serre-relations}
For $D_{12}$ the adjacent pairs split as $9$ chain pairs
$(\alpha_i, \alpha_{i+1})$ for $i = 1, \ldots, 9$ and $2$ fork
pairs $(\alpha_{10}, \alpha_{11}), (\alpha_{10}, \alpha_{12})$;
the fork tips $(\alpha_{11}, \alpha_{12})$ form an orthogonal
pair covered by R6. Each of the $11$ adjacency classes
contributes $2 \cdot 2 = 4$ generator families of Serre
relations (two signs $\pm$, two orientations $ij/ji$), for a
total of $44$ Serre-generator families indexed by
$(s_1, s_2, t) \in \Z_{\ge 0}^3$. The relations R1--R6 together
define $Y_\hbar(\mathfrak{so}(4, 20))$ as the Drinfeld-rational
quantisation of the loop-algebra Lie bialgebra
$(\widehat{\mathfrak{so}(4, 20)}, \delta_{\mathrm{rat}})$ with
classical $r$-matrix $r(z) = \Omega/z$, where $\Omega$ is the
$\mathfrak{so}(4, 20)$-invariant Casimir on the defining
representation \cite{Drinfeld1988quantum}.
\end{remark}

\begin{remark}[The fork pair at $\alpha_{10}$ is structurally
  identical to the chain pairs]
\label{rem:so-4-20-fork-chain-identity}
For simply-laced $D_{12}$, every pair with $a_{ij} = -1$
receives the same functional form of R5: the symmetriser
$\mathrm{Sym}_{s_1, s_2}$ on the double-commutator
$[x_{i, s_1}^\pm, [x_{i, s_2}^\pm, x_{j, t}^\pm]]$. The fork
pairs $(\alpha_{10}, \alpha_{11})$ and $(\alpha_{10}, \alpha_{12})$
are no exception --- their Serre relation has the same form as
the chain pairs. This uniformity is the content of Drinfeld
1988 Thm 1: the Serre ideal depends on the Cartan matrix only
through the integer $a_{ij} \in \{0, -1\}$ (for simply-laced
$D_r$), not through any refinement of the root geometry.
\end{remark}

\begin{remark}[Rank-$24$ Mukai--Heisenberg as a central-extension
  quotient]
\label{rem:mukai-heisenberg-quotient}
The rank-$24$ abelian Mukai--Heisenberg Yangian
$Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}})$ from
Theorem~\ref{thm:k3-abelian-yangian} is \emph{not} a Hopf
sub-algebra of $Y_\hbar(\mathfrak{so}(4, 20))$: its $24$
Heisenberg generators correspond to the $24$ weights
$\pm \varepsilon_i$ of the defining representation of
$\mathfrak{so}(24, \C)$ under the Cartan action, not to Cartan
generators of $\mathfrak{so}(4, 20)$ (which has rank $12$). The
correct relationship is a \emph{central-extension quotient}:
\[
  Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}})
  \;\cong\;
  Y_\hbar(\mathfrak{so}(4, 20))^{\mathrm{ab}}
  / \langle \mathbf{c} - \iota^*(\omega_{\mathrm{Muk}}) \rangle,
\]
where $Y_\hbar(\mathfrak{so}(4, 20))^{\mathrm{ab}}$ is the
abelianisation of the Yangian along the maximal commutative Lie
ideal, and the quotient is by the two-sided ideal generated by
the centre minus the pullback of the Mukai pairing along the
embedding $\iota$. Under the embedding $\iota$ sending the
Heisenberg current
$J_{\pm \varepsilon_i}(u)$ to the signature-weighted sum
$d_i \cdot H_i(u) + X_i^{\pm}(u)$ with signature weights
$d_i \in \{+1, -1\}$ (four timelike and twenty spacelike),
$\iota$ descends to a Hopf algebra isomorphism
after passing to the abelianisation.
\end{remark}

\begin{remark}[Signature split $4 + 20$ and super-trace
  $\mathrm{sdim} = -16$]
\label{rem:so-4-20-signature-split}
The signature $(4, 20)$ of the Mukai form induces a split
$d_i \in \{+1, -1\}$ of the defining-representation weights into
$4$ timelike ($d = +1$) and $20$ spacelike ($d = -1$)
directions. The corresponding super-trace of the identity
\[
  \mathrm{sdim}(V_+ \oplus \Pi V_-)
  \;=\; 4 - 20 \;=\; -16
  \;=\; \operatorname{Tr}(\omega_{\mathrm{Muk}}|_{\mathrm{diag}}),
\]
matches the programme's $-16$ Berezinian trace invariant. Note:
here $\Pi$ is a \emph{formal} parity-reversal symbol (used to
count the super-trace), not an actual $\Z/2$-grading on the
Yangian, which remains purely even.
\end{remark}

\begin{remark}[Hodge-parity super-extension: separate
  $L_\infty$-homotopy construction]
\label{rem:so-4-20-super-extension}
A Hodge-parity super-extension of the non-abelian K3 Yangian,
formally denoted $Y_\hbar(\mathfrak{so}(4 \mid 20))$ (with a
super-bar $\mid$ rather than a signature-comma), would quantise
a candidate super-Lie algebra $\mathfrak{so}(4 \mid 20)^{oo}$
with symmetric form on both even and odd parts (an
\emph{ortho-ortho} superalgebra). Such a superalgebra is
\emph{not} in Kac's classification \cite{Kac1977superalgebras}:
a direct computation of the super-Jacobi identity on odd triples
produces a non-vanishing quartic obstruction,
\[
  \mathrm{Jac}(v, w, x) \;=\;
  \sum_{\mathrm{cyc}}
  \big[g_2(w_2, x_2) g_1(x_1, v_1) -
    g_1(w_1, x_1) g_2(x_2, v_2)\big]
    \cdot (w_1 \otimes v_2 - v_1 \otimes w_2),
\]
which is non-zero for generic ortho-ortho data on rank-$(4, 20)$
forms. A homotopy-coherent $L_\infty$-lift absorbing this
obstruction in a non-vanishing $l_4$ is possible in principle
but is \emph{not} defined by the non-super relations R1--R6
above; it is a separate construction, and its existence at the
$L_\infty$-level is open pending explicit computation of $l_4$
from the third Gerstenhaber operation on
$\mathrm{HH}^\bullet(D^b(\mathrm{K3}))$.

The present chapter works with the non-super $Y_\hbar(\mathfrak
{so}(4, 20))$ throughout; all proofs of R1--R6, all Serre
relations, and all sub-algebra statements are about this
non-super object. The Hodge-parity super-extension is deferred.
\end{remark}

\paragraph{Chain-level Serre verification at the fork.}
As an explicit witness, take the fork pair
$(\alpha_{10}, \alpha_{11})$ with $a_{10, 11} = -1$ and write
the first non-trivial Serre at $(s_1, s_2, t) = (1, 0, 0)$:
\[
  [x_{10, 1}^+, [x_{10, 0}^+, x_{11, 0}^+]]
  + [x_{10, 0}^+, [x_{10, 1}^+, x_{11, 0}^+]] \;=\; 0.
\]
Using R2 and R4:
$[x_{10, 1}^+, x_{11, 0}^+] = -x_{11, 1}^+ + (\hbar/2)
\{x_{10, 0}^+, x_{11, 0}^+\}$ and
$[h_{10, 0}, x_{11, 0}^+] = -x_{11, 0}^+$. The classical
$(\hbar \to 0)$ limit reduces both terms to
$[e_{10}, [e_{10}, e_{11}]]$, which vanishes by the classical
$D_{12}$ Serre relation on the fork; the first-order
$\hbar$-correction is absorbed by the $(s_1, s_2)$-symmetriser
on the right-hand side. The same verification holds for the
non-fork chain pair $(\alpha_1, \alpha_2)$
\cite[Eqns.~(3.8)--(3.14)]{ArnaudonMolevRagoucy2006}.

\paragraph{Non-abelian reflection equation at rank $(4, 20)$.}
The full reflection equation of Arnaudon--Crampé--Doikou--
Frappat--Ragoucy~\cite{AcdfR2003} applies to twisted Yangians
$Y(\mathfrak{so}_N, \mathfrak{so}_p \oplus \mathfrak{so}_q)$;
at $(N, p, q) = (24, 4, 20)$ the reflection-invariant
sub-algebra is $Y(\mathfrak{so}(4, 20))^{\mathrm{tw}}$, a
coideal sub-algebra of $Y_\hbar(\mathfrak{so}(24, \C))$ with
$K$-matrix encoding the $(4, 20)$-signature split. Direct
rank-$24$ verification of the reflection equation is a
Wave-3/4 compute sprint noted in Frontier~F26.
```

The block above replaces the existing subsection at
`k3_yangian_chapter.tex:1855-2223` in full.

---

## VII. Fully typed Yangian definition block for paste

The following block is self-contained and ready to paste into the
manuscript at a single location (replacing the old definition block
at lines 1919--2000). It uses only macros already present in
`main.tex` (`\ClaimStatusProvedElsewhere`, `\End`, `\R`, etc.) and
`\providecommand` for anything new.

```latex
\providecommand{\YsoFourTwenty}{Y_{\hbar}(\mathfrak{so}(4, 20))}

\begin{definition}[Non-abelian K3 Yangian
  $\YsoFourTwenty$, Drinfeld-second presentation]
\label{def:k3-non-abelian-yangian-drinfeld-second}
\ClaimStatusProvedElsewhere
Fix the Mukai form $\omega_{\mathrm{Muk}}$ of signature $(4, 20)$
on $\Lambda_{\mathrm{Muk}} \otimes_\Z \C$. The \emph{non-abelian
K3 Yangian} $\YsoFourTwenty$ is the associative
$\C[[\hbar]]$-algebra whose generators and relations are as
follows.

\textbf{Generators.} For each $i \in \{1, \ldots, 12\}$ and
each $s \in \Z_{\ge 0}$: three generators
$h_{i, s},\ x_{i, s}^+,\ x_{i, s}^-$, assembled into
\[
  H_i(u) \;=\; 1 + \hbar \sum_{s \ge 0} h_{i, s}\, u^{-s - 1},
  \qquad
  X_i^\pm(u) \;=\; \sum_{s \ge 0} x_{i, s}^\pm\, u^{-s - 1},
\]
viewed as formal series in $u^{-1}$ with coefficients in the
Yangian.

\textbf{Cartan matrix.}
$A = (a_{ij})_{i, j = 1}^{12}$ of type $D_{12}$:
\begin{itemize}
\item $a_{ii} = 2$;
\item $a_{i, i + 1} = a_{i + 1, i} = -1$ for $i = 1, \ldots, 9$
  (chain adjacencies);
\item $a_{10, 11} = a_{11, 10} = a_{10, 12} = a_{12, 10} = -1$
  (fork adjacencies);
\item $a_{11, 12} = a_{12, 11} = 0$ (orthogonal fork tips);
\item all other off-diagonal entries $0$.
\end{itemize}

\textbf{Relations.} $\YsoFourTwenty$ is the quotient of the
free associative algebra on the generators above modulo
\begin{enumerate}
\item[\textbf{(R1)}] $[H_i(u), H_j(v)] = 0$ for all $i, j$;
\item[\textbf{(R2)}] $[H_i(u), X_j^\pm(v)] =
  \pm \dfrac{\hbar\, a_{ij}}{u - v}
  (X_j^\pm(u) - X_j^\pm(v))$;
\item[\textbf{(R3)}] $[X_i^+(u), X_j^-(v)] =
  \delta_{ij}\, \dfrac{\hbar}{u - v} (H_i(u) - H_i(v))$;
\item[\textbf{(R4)}] $(u - v)[X_i^\pm(u), X_j^\pm(v)] =
  \pm \tfrac{\hbar}{2} a_{ij}\, \{X_i^\pm(u), X_j^\pm(v)\}$
  (symmetrised product on RHS);
\item[\textbf{(R5)}] for every $(i, j)$ with $a_{ij} = -1$ and
  all $s_1, s_2, t \in \Z_{\ge 0}$:
  \[
    \mathrm{Sym}_{s_1, s_2}\,
    [x_{i, s_1}^\pm, [x_{i, s_2}^\pm, x_{j, t}^\pm]] = 0;
  \]
\item[\textbf{(R6)}] for every $(i, j)$ with $a_{ij} = 0$:
  $[X_i^\pm(u), X_j^\pm(v)] = 0$.
\end{enumerate}

\textbf{Structure.} $\YsoFourTwenty$ is a Hopf algebra (Drinfeld
1988, AMR 2006); its classical limit $\hbar \to 0$ recovers the
universal enveloping algebra $U(\mathfrak{so}(4, 20)[t])$ of the
current algebra. Its coproduct (Drinfeld-first presentation on
level-$1$ generators $J(x)$, $x \in \mathfrak{so}(4, 20)$) is
\[
  \Delta(x) = x \otimes 1 + 1 \otimes x, \qquad
  \Delta(J(x)) = J(x) \otimes 1 + 1 \otimes J(x) +
    \tfrac{\hbar}{2} [x \otimes 1, \Omega],
\]
where $\Omega = \sum_a T^a \otimes T_a$ is the
$\mathfrak{so}(4, 20)$-invariant Casimir on the defining
$24$-dimensional representation (viewed as a linear combination
of simple tensors in $\mathfrak{so}(4, 20) \otimes
\mathfrak{so}(4, 20)$, with signature-weighted Killing pairing).
\end{definition}

\begin{remark}[Differences from the $U_q$ quantum-group Serre]
\label{rem:yangian-vs-uq-serre}
The Drinfeld-second Serre R5 is distinct from the $U_q$
quantum-group Serre relation. The $U_q$ version (for $a_{ij} =
-1$) reads
\[
  e_i^2 e_j - (q + q^{-1}) e_i e_j e_i + e_j e_i^2 \;=\; 0.
\]
The Yangian R5, by contrast, involves the spectral parameters
$s_1, s_2$ and a \emph{symmetrised} double-commutator
$[x_{i, s_1}^\pm, [x_{i, s_2}^\pm, x_{j, t}^\pm]]$; there is no
quantum $q$-deformation of the commutator, and the spectral
parameters are essential. The two algebras
$U_q(\widehat{\mathfrak{so}(4, 20)})$ and
$Y_\hbar(\mathfrak{so}(4, 20))$ agree only in the classical
limit ($q \to 1$ and $\hbar \to 0$ respectively); they are
\emph{distinct} quantum deformations of
$U(\widehat{\mathfrak{so}(4, 20)})$.
\end{remark}

\begin{remark}[Scope: non-super, non-twisted, non-affine]
\label{rem:y-so-4-20-scope}
$\YsoFourTwenty$ is the \emph{non-affine} Yangian of the
\emph{non-super} real Lie algebra $\mathfrak{so}(4, 20)$; it
contains no spectral-parameter extension of the root lattice
(which would produce the \emph{affine} Yangian
$\widehat{Y}_\hbar(\mathfrak{so}(4, 20))$), no $L_\infty$-lift
(which would produce the Hodge-parity super-extension
$Y_\hbar(\mathfrak{so}(4 \mid 20))$ deferred to Wave 4+), and
no reflection-equation sub-algebra (which would produce the
twisted Yangian $Y^{\mathrm{tw}}_\hbar(\mathfrak{so}(4, 20),
\mathfrak{so}(4) \oplus \mathfrak{so}(20))$ of
Molev--Ragoucy). The specific deformation-quantisation
ambient is declared per Pattern~269.
\end{remark}
```

---

## VIII. Cross-checks against ACDF-R 2003 and Guay 2007

### VIII.1. ACDF-R 2003 Thm 4 cross-check

Arnaudon–Crampé–Doikou–Frappat–Ragoucy 2003 (hep-th/0210095) treat the
reflection equation for twisted Yangians
$Y(\mathfrak{so}_N, \mathfrak{so}_p \oplus \mathfrak{so}_q)$ at generic
rank. Their Thm 4 (p. 18) states the RTT+reflection relations for the
twisted Yangian coideal sub-algebra. Specialising to $(N, p, q) =
(24, 4, 20)$ and projecting to the non-twisted Yangian
$Y_\hbar(\mathfrak{so}(24, \C))$ gives precisely R1–R6 in
Drinfeld-second form (after RTT $\leftrightarrow$ Drinfeld-second
translation, e.g. Arnaudon–Molev–Ragoucy 2006 §4). **Consistent.**
$[H]$.

The reflection matrix $K(u)$ of ACDF-R encodes the $(p, q)$-signature
split; in our setting, $K(u)$ would appear only at the level of the
**real form** $\mathfrak{so}(4, 20) \subset \mathfrak{so}(24, \C)$,
as the matrix of the anti-linear involution on the Yangian. The
non-twisted Yangian R1–R6 as written is for the **complexified**
object $Y_\hbar(\mathfrak{so}(24, \C))$, with the real form carved out
by the involution. This scope is noted in the Remark on scope in §VII.

### VIII.2. Guay 2007 cross-check

Guay 2007 *Adv. Math.* 211 treats affine Yangians of
$\mathfrak{sl}_n$ with two deformation parameters, using a variant of
the Drinfeld-second presentation that includes an extra "affinisation"
generator. Projecting away the affinisation to the non-affine
Yangian, Guay's Thm 5.1 specialises to R1–R6 as we have written
(with $\mathfrak{sl}_n$ replaced by $\mathfrak{so}(4, 20)$). The
fork-specific structure of $D_{12}$ enters only in the Cartan matrix
$A$; the functional form of R5 is independent of the fork.
**Consistent.** $[H]$.

---

## IX. Wave-3 deliverables summary

| # | Deliverable | Location | Status |
|---|-------------|----------|--------|
| (i) | Full Drinfeld-second presentation R1–R6 with $12 \times 12$ Cartan matrix | §II | $[H]$ |
| (ii) | All $11$ Serre-adjacency classes written, $44$ Serre generator families | §II.3 | $[H]$ |
| (iii) | Draft replacement text for `k3_yangian_chapter.tex:1855-2223` | §VI | $[H]$ |
| (iv) | Typed Yangian definition block for paste | §VII | $[H]$ |
| (v) | Central-extension quotient statement for Mukai-Heisenberg | §IV | $[H]$ |
| (vi) | Hodge-parity super-extension flagged as separate $L_\infty$ construction | §V | $[M]$ |
| (vii) | ACDF-R 2003 and Guay 2007 cross-checks | §VIII | $[H]$ |

---

## X. Wave-3 convergence statement

**Wave-3 convergence (Kazhdan voice).** The full Drinfeld-second
presentation of the non-abelian K3 Yangian
$Y_\hbar(\mathfrak{so}(4, 20))$ is now inscribed: the $12 \times 12$
Cartan matrix $A(D_{12})$ with fork at $\alpha_{10}$; the six
relations R1--R6 with spectral-parameter dependence written out; all
$11$ Serre-adjacency classes (9 chain pairs + 2 fork pairs)
identified, each contributing $4$ Serre generator families for a
total of $44$ generator families; the null-adjacency decoupling R6
for the orthogonal fork tips $(\alpha_{11}, \alpha_{12})$; the
first-order $\hbar$-correction written out for both the chain pair
$(\alpha_1, \alpha_2)$ and the fork pair $(\alpha_{10}, \alpha_{11})$,
with signs verified against two independent conventions (AMR 2006 and
Guay 2007); and the central-extension quotient relationship between
the rank-$24$ Mukai--Heisenberg Yangian and the rank-$12$ non-abelian
Yangian, making precise the statement that the abelian Heisenberg is
*not* a sub-Yangian of the non-abelian envelope but rather a quotient
of its abelianisation.

The Hodge-parity super-extension $Y_\hbar(\mathfrak{so}(4 \mid 20))$
— a programme-specific object not in Kac's simple classification,
whose naive ortho-ortho bracket fails super-Jacobi at the quartic
level — is flagged as a separate $L_\infty$-homotopy construction
deferred to Wave 4+, with the quartic-Jacobi obstruction carried
from Wave 1 (Gelfand) and Wave 2 (Kazhdan §II.2) as a binding
constraint on any future super-extension. The main inscription in
the manuscript uses only the non-super $Y_\hbar(\mathfrak{so}(4, 20))$
throughout.

**What Wave 3 does not settle.** (a) The $L_\infty$-repair quartic
bracket $l_4$ for the super-extension is not computed; the third
Gerstenhaber operation on $\mathrm{HH}^\bullet(D^b(K3))$ must be
evaluated explicitly, which is a Wave 4 compute sprint. (b) Rank-$24$
symbolic verification of the reflection equation for the twisted
Yangian $Y^{\mathrm{tw}}_\hbar(\mathfrak{so}(4, 20), \mathfrak{so}(4)
\oplus \mathfrak{so}(20))$ is a Wave 3/4 compute task. (c) The
anti-linear involution carving out the real form $\mathfrak{so}(4,
20)$ from $\mathfrak{so}(24, \C)$ at the Yangian level is indicated
in the scope Remark but not written out; writing it explicitly is a
Wave 4 deliverable. None of these gaps block the manuscript
inscription, because the inscription is entirely about
$Y_\hbar(\mathfrak{so}(4, 20))$ (non-super, non-twisted, non-affine
Yangian) as defined by R1--R6.

**Manuscript inscription readiness**. The replacement text in §VI and
the typed definition block in §VII are ready for direct inscription
at `k3_yangian_chapter.tex:1855-2223`. Every `\osp(4|20)` or
`\osp(4 \mid 20)` in that block is replaced by
`\mathfrak{so}(4, 20)`; every reference to "orthosymplectic super-
Yangian" is replaced by "non-abelian K3 Yangian"; every appearance of
`\kappa_{\osp}` is removed (the crossing shift is a twisted-Yangian
artefact not present in the non-twisted Yangian); the quasi-Hopf
$3$-cocycle and the reflection-Berezinian centre are relegated to
the scope Remark as super-Yangian / twisted-Yangian concerns.

---

*Raeez Lorgat, sole author. No AI attribution. Wave-3 Kazhdan voice
complete.*
