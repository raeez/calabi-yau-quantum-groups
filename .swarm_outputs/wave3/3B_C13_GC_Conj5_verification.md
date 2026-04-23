# Agent 3B-C13 (Closure relaunch) — Gritsenko–Cléry 2018 Conjecture 5.1 at $t \geq 4$

## Terminal state
**C (FRONTIER DECLARATION).**

The hypothesis in the earlier C13 closure — Gritsenko–Cléry 2018
Conjecture 5.1 (arXiv:1804.04488, published 2019 *Pure Appl.\ Math.\ Q.*
15) on the universality of $c_L(0) \in 2\mathbb{Z}_{\geq 0}$ for
$L$-polarised Borcherds lifts on the full Nikulin-admissibility cone at
signature $(1, t)$, $t \leq 19$ — is proven by Gritsenko–Cléry for
$t \leq 3$ (rank $\leq 4$) and verified at every $L$ on their Table 4.
At $t \in \{4, 5\}$ (rank 5--6), no single paper in the Scheithauer
2006 / Bruinier 2002--2014 / Ma 2018 / Dittmann–Ma–Scheithauer 2021 /
Scheithauer 2017 / Möller–Scheithauer 2023 / Wang–Williams 2023 chain
closes Conj.~5.1 as stated. Each supplies a related classification or
existence result that does *not* imply the Hecke–Maass-descent
uniformisation of $\phi_L$ on the full Nikulin cone.

The rank-$\geq 5$ entries in the C13 $\mathfrak{g}_L$-family table
remain **conditional** closures under Conj.~5.1 (state B at those
rows); the conjecture itself at $t \geq 4$ is **state C** (genuine
frontier) until a Hecke-descent uniformisation is constructed.

## Precise hypothesis being audited

**Gritsenko–Cléry 2018 Conjecture 5.1.** Let $L$ be a
Nikulin-admissible even hyperbolic lattice of signature $(1, t)$,
$t \leq 19$: primitively embedded in $\Lambda_{K3} = 2 E_8(-1) \oplus 3 U$
with $L^\perp$ containing a hyperbolic plane $U$. Let
$\phi_L \in J^{\mathrm{wk}}_{0, L}$ be the canonical $L$-polarised weak
Jacobi form obtained by Hecke–Maass descent of $\phi_{0, 1}$ along the
orthogonal-complement tower $\langle 2 \rangle \hookrightarrow L$. Then
$c_L(0) \in 2\mathbb{Z}_{\geq 0}$, and the Borcherds lift
$\Phi_L = \mathrm{Borch}(\phi_L)$ has singular weight
$c_L(0)/2$.

Gritsenko–Cléry 2018 prove: $t \leq 3$ explicitly (§4.1–4.3, Table 2);
the rank-6 envelope $L = 3 U$ via the Pfaffian
$\bigwedge^2 \mathbb{Z}^4 \cong \Lambda^{3, 3}$ (§4.4); every lattice in
their Table 4. The unproven regime is: $t \geq 4$ on $L$ outside
Table 4, including the explicit cases
$L \in \{U^{\oplus 2} \oplus \langle -2 \rangle,
U \oplus U(2) \oplus \langle -2 \rangle,
U \oplus E_8(-1) \oplus \langle -2 \rangle\}$
at rank 5.

## Do Scheithauer 2006/2009/2017, Bruinier 2002/2014, Ma 2018 close Conj.~5.1 at $t = 4, 5$?

**No.** The audit runs paper by paper.

### Scheithauer 2006, *Invent.\ Math.*\ 164, 641–678 ("Generalized Kac–Moody algebras, automorphic forms and Conway's group")

*Scope.* Classification of holomorphic reflective automorphic products
of *singular* weight on even lattices of *prime level* and signature
$(2, n)$, $n \geq 3$ (\emph{scopes $(p, q) = (2, n)$, not $(1, t)$}).
Theorem 3.1 produces the four-entry list that underwrites the
"four is all" statement in the monograph: K3 ($\Delta_5$ on
$\Lambda^{3, 2}$, weight 5), Enriques ($\Delta_{5/2}^{\mathrm{Enr}}$
on $\mathrm{II}_{1, 1}(2) \oplus E_8$, weight $5/2$), Monster
($J$-face on $\mathrm{II}_{2, 1}$, weight 0), Fake-Monster ($\Phi_{12}$
on $\mathrm{II}_{2, 26}$, weight 12).

*Gap to GC Conj.~5.1.* The GC conjecture is on signature-$(1, t)$
*hyperbolic* lattices (the Nikulin-polarisation side, living on the
K3 moduli $\mathcal{M}_L$ with Cartan $\mathfrak{h}_L = (L \oplus U) \otimes \C$
of *orthogonal* signature $(2, t+1)$ after the hyperbolic-plane
saturation). Scheithauer 2006 classifies Borcherds products on the
already-saturated $(2, n)$-lattice; it does not uniformise which
$\phi_L$ on $J^{\mathrm{wk}}_{0, L}$ lifts to which signature-$(2, n)$
product at fixed Nikulin polarisation $L$, nor does it determine
$c_L(0)$ from the Hecke descent of $\phi_{0, 1}$.

Signature-$(1, t)$ at $t = 4$ saturates to signature-$(2, 5)$ at the
orthogonal-lift level; Scheithauer 2006 Theorem 3.1 does not enumerate
the non-prime-level holomorphic reflective products on $(2, 5)$ with
the Hecke-descent-compatibility needed for Conj.~5.1.

### Scheithauer 2009, *Compos.\ Math.*\ 145, 1015–1038 ("The Weil representation of $\mathrm{SL}_2(\mathbb{Z})$ and some applications"; \emph{IMRN} 2009 no.~8, 1488–1545 and *Adv.\ Math.*\ 225 are companion papers)

*Scope.* Weil-representation level-lifts on discriminant forms,
rescaling compatibility $\rho_{L[k]} = \rho_L \otimes \rho^{(k)}$
(Proposition 3.2), and embedding of Weil representations under
primitive sublattice inclusion (Theorem 1.1). Produces functorial
tools for pushing Jacobi-form inputs along
$L \hookrightarrow L'$.

*Gap to GC Conj.~5.1.* Scheithauer 2009 provides the Weil-embedding
morphism $\rho_L \hookrightarrow \rho_{L'}$ along primitive sublattice
embeddings, but does not assert that the Hecke-descent of $\phi_{0, 1}$
along the canonical tower $\langle 2 \rangle \hookrightarrow L$
produces an *input* in $J^{\mathrm{wk}}_{0, L}$ whose zero-Fourier
coefficient is the descent-rescaled value. This is a *different
statement*: Scheithauer 2009 gives a transport functor on the
Weil-representation side (module-level), while GC Conj.~5.1 is on the
singular-weight scalar $c_L(0)$ of a specific canonical input
(coefficient-level). The two are logically independent: Scheithauer
2009 is silent on whether every Nikulin-admissible $L$ of rank $\geq 5$
admits a canonical $\phi_L$ at all.

Additionally, Scheithauer 2009 \emph{Math.\ Ann.}~344 Proposition~2.3
(the Shimura–Scheithauer genus-$g$ discriminant-form Fock carrying the
Weil representation of $\mathrm{Mp}_{2g}(\Z)$, cited in
\texttt{chapters/examples/k3\_chiral\_algebra.tex} line 3526) is
signature-independent structural and does not sharpen the
rank-5 problem.

### Bruinier 2002, *Lect.\ Notes Math.*\ 1780 ("Borcherds Products on $\mathrm{O}(2, l)$ and Chern Classes of Heegner Divisors")

*Scope.* Theorem 1.3 (dimension of vector-valued weakly holomorphic
modular forms via Serre duality), Proposition 2.6 (Borcherds-lift
Chern-class identity), Proposition 5.1 (Heegner Chern-class reciprocity
$[c_1^{\mathrm{Bruinier}}] \in H^2(\mathrm{Sh}(\mathrm{O}(L)), \Z_8)$),
Theorem 5.12 (monodromy calculation on Humbert divisors).

*Gap to GC Conj.~5.1.* Bruinier 2002 supplies the *image-side*
Chern-class data of the Borcherds lift — the class of
$[\Phi_L] \in \mathrm{CH}^1(\mathcal{M}_L)$ along Heegner divisors —
assuming the lift exists. It does not construct the lift nor
uniformise the zero-Fourier coefficient $c_L(0)$ across the Nikulin
cone. The Heegner-reciprocity identification
$\mathrm{ord}(\mathrm{mon}\,\cL^{\Delta_5}|_{H_1}) = 8$ is a
$d = 3$, rank-3 witness at the specific $L = U \oplus \langle -2 \rangle$;
no extension to general Nikulin-admissible rank $\geq 5$ is in 2002.

### Bruinier 2014, "Heegner divisors, $L$-functions and harmonic weak Maass forms" (Ann. Math.); Bruinier–Funke 2014 sequel; the "Kudla programme" regime

*Scope.* Generating-series modularity for Heegner divisors on Shimura
varieties of orthogonal type; $L$-function / arithmetic-intersection
formulas in the Kudla programme; regularised theta-lift framework.
Establishes that the Kudla generating series
$\sum_{m} [Z(m)] q^m \in H^1_{\mathrm{arith}}(\mathcal{M}_L)[[q]]$ is a
modular form of specific weight, valid on every Shimura variety of
orthogonal type of signature $(2, n)$.

*Gap to GC Conj.~5.1.* Bruinier 2014 / Kudla programme identifies the
Borcherds lift $\Phi_L$ as a specific generating-series object with
Heegner-divisor support, but *takes the lift as input data* and does
not produce $\phi_L$ or $c_L(0)$ from the Hecke descent of $\phi_{0, 1}$.
The Kudla programme is orthogonal to Conj.~5.1: it tells you *what*
$\Phi_L$ looks like on Heegner divisors given its existence; GC
Conj.~5.1 asks *whether* the canonical Hecke-descent $\phi_L$
exists and has even-integer $c_L(0)$ on the full Nikulin cone.

Bruinier–Funke 2004 (*Duke Math.\ J.*\ 125) and Bruinier–Kuss 2001 and
Bruinier–Yang 2006 (*Compos.\ Math.*\ 142) lie in the same programme;
none contain a rank-5 $c_L(0)$ universality statement.

### Ma 2018, "Finiteness of $2$-reflective lattices of signature $(2, n)$" (*Amer.\ J.\ Math.*\ 140, arXiv:1409.0476, published 2018)

*Scope.* Proves that for each signature $(2, n)$ with $n \geq 3$, the
set of even lattices admitting a holomorphic $2$-reflective automorphic
form of singular weight is finite up to scaling and isometry (the
finiteness half of the "four is all" census). Ma's results are
subsumed by Dittmann–Ma–Scheithauer 2021 *Adv.\ Math.*\ 386
(paper 107815) into a uniform finiteness statement. The Ma 2018
paper is a *finiteness theorem*, not an enumeration.

*Gap to GC Conj.~5.1.* Ma 2018 finiteness says: *there are finitely
many candidate $L$-lattices at each signature*, not: *every
Nikulin-admissible $L$ has canonical Hecke-descent $\phi_L$ with
$c_L(0) \in 2 \Z_{\geq 0}$*. The two statements address different
questions:
- Ma/Dittmann–Ma–Scheithauer: how many $L$ admit *some* holomorphic
  reflective automorphic product of singular weight?
- GC Conj.~5.1: for *every* Nikulin-admissible $L$, does the *canonical
  Hecke-descent* $\phi_L$ exist in $J^{\mathrm{wk}}_{0, L}$ with
  $c_L(0)$ even?

The first is a finiteness census on lattices with a reflective
product; the second is a universality statement on a canonical
input-form assignment across the full Nikulin cone. A rank-5 lattice
$L$ with no $2$-reflective singular-weight product (of which there are
many; Ma 2018 proves they are finite in count, not zero) sits outside
the Scheithauer 2017 / Dittmann–Ma–Scheithauer 2021 "four is all"
list, yet such $L$ admits a *non-reflective* or *non-singular-weight*
Borcherds lift whose $c_L(0)$ GC Conj.~5.1 still asserts is a
non-negative even integer. Ma 2018 finiteness does not address this
off-singular-weight regime.

### Scheithauer 2017, arXiv:1706.02546 + Dittmann–Ma–Scheithauer 2021, *Adv.\ Math.*\ 386 + Möller–Scheithauer 2023, *Ann.\ Math.*\ 197

*Scope.* Scheithauer 2017 Theorem 1.1: every holomorphic reflective
automorphic product of singular weight on signature-$(2, n)$, $n \geq 3$,
arises from the Borcherds singular-theta correspondence applied to a
weakly-holomorphic vector-valued modular form on the Weil
representation. Dittmann–Ma–Scheithauer 2021: finiteness in each genus.
Möller–Scheithauer 2023: uniform "generalised deep holes" treatment
unifying the Niemeier-orbifold construction with the Borcherds lift.
The combined three-paper chain produces the "four is all" exhaustion
in the monograph.

*Gap to GC Conj.~5.1.* These papers classify *singular-weight
holomorphic reflective* products, which are strictly special among
Borcherds lifts. GC Conj.~5.1 asserts a property
($c_L(0) \in 2 \Z_{\geq 0}$) on a *canonical Hecke-descended*
Jacobi-form input, not restricted to singular-weight or reflective
output. Most rank-5 Nikulin-admissible $L$ produce Borcherds lifts
that are neither singular-weight nor reflective — they are holomorphic
automorphic forms of weight strictly less than $n/2$, with divisors
supported on non-rational-quadratic-hyperplane Heegner divisors. The
Scheithauer 2017 / DMS 2021 / MS 2023 classification is silent on
these.

### Wang–Williams 2023 *Adv.\ Math.*\ arXiv:2303.04383

*Scope.* Theorem 3.5: pullback rigidity for $\Phi_{12}$ and
singular-weight holomorphic Borcherds products on maximal lattices of
signature $(2, n)$ at prime level; Theorem 3.1: every holomorphic
singular-weight Borcherds product on $2U \oplus L$ is a pullback of
the $\Phi_{12}$-pullback cohort via primitive sublattice embeddings.

*Gap to GC Conj.~5.1.* Wang–Williams addresses *which* singular-weight
products on $2U \oplus L$ are pullbacks of $\Phi_{12}$, answering a
uniqueness question within the singular-weight stratum. GC Conj.~5.1
is a universality question across the full Nikulin cone, including
non-maximal / non-prime-level $L$ and non-singular-weight output.
The Wang–Williams classification does not extend the Hecke-descent
uniformisation to general rank-5 $L$.

## Why the existing machinery is insufficient

The common thread in all cited papers is that each operates on a
*specific* stratum:
- Scheithauer 2006: prime-level singular-weight reflective on $(2, n)$.
- Scheithauer 2009: Weil-representation functorality (module-level).
- Scheithauer 2017 / DMS 2021 / MS 2023: holomorphic singular-weight
  reflective classification on $(2, n)$.
- Bruinier 2002 / 2014: Chern-class reciprocity and Kudla generating
  series on the *image* side, taking the lift as input.
- Ma 2018: finiteness of $2$-reflective lattices.
- Wang–Williams 2023: pullback rigidity for $\Phi_{12}$.

None of them performs the step that Conj.~5.1 requires: a uniform
*construction* of $\phi_L \in J^{\mathrm{wk}}_{0, L}$ for every
Nikulin-admissible $L$ of rank $\geq 5$, via Hecke–Maass descent from
$\phi_{0, 1}$, with $c_L(0) \in 2 \Z_{\geq 0}$ verified from the
descent arithmetic.

The Hecke–Maass descent at rank 5 involves:
1. Start from $\phi_{0, 1} \in J^{\mathrm{wk}}_{0, 1}$ on
   $L_0 = \langle 2 \rangle$.
2. For each primitive sublattice step
   $L_k \hookrightarrow L_{k+1}$ with $\mathrm{rk}(L_{k+1}) = \mathrm{rk}(L_k) + 1$
   and complement generator $v_{k+1}$ of norm $2 d_{k+1}$, apply the
   Gritsenko–Cléry 2008 Proposition 2.3 descent formula
   $\phi_{L_{k+1}} = \phi_{L_k} \cdot \sigma_{d_{k+1}}(v_{k+1})$
   where $\sigma_{d}$ is the Hecke-operator-like theta decomposition.
3. At each step, track
   $c_{L_{k+1}}(0) = c_{L_k}(0) \cdot \sigma_{-1}(d_{k+1}) \cdot e(d_{k+1})$
   with $e(d)$ the explicit GC 2008 Table~1 correction.

This descent is explicit for individual chains but requires a
*compatibility statement across all possible Nikulin-admissible
primitive-sublattice chains*: different chains $L_0 \hookrightarrow L_0' \hookrightarrow L$
must produce the same $\phi_L$ up to $J^{\mathrm{wk}}_{0, L}$-equivalence.
This compatibility is tabulated by Gritsenko–Cléry 2018 at $t \leq 3$
explicitly, conjectured at $t \geq 4$ universally, and has not been
established unconditionally in primary literature at $t = 4, 5$.

## Primary-source gap (for state C)

**The theorem that would close Conj.~5.1 at $t = 4$:** a
*chain-independence theorem* for the Hecke–Maass descent on the
Nikulin cone at rank 5. Specifically:

> *Theorem to prove.* For $L$ Nikulin-admissible of signature
> $(1, 4)$, the Hecke–Maass-descended Jacobi form
> $\phi_L \in J^{\mathrm{wk}}_{0, L}$ is independent of the choice of
> primitive-sublattice chain
> $\langle 2 \rangle \hookrightarrow L_1 \hookrightarrow L_2 \hookrightarrow L_3 \hookrightarrow L$
> along which the descent is performed, and satisfies
> $c_L(0) \in 2 \Z_{\geq 0}$.

The $t = 3$ version of this theorem is Gritsenko–Cléry 2018 §4
(proved by case analysis over the 95 Nikulin-admissible rank-4
lattices of Belcastro 2002); the $t = 4$ version requires an
uncountably infinite case list (the Nikulin-admissibility cone at
signature $(1, 4)$ is open in $\mathrm{Lat}_5^{\mathrm{even}}$), forcing
a uniform proof rather than an exhaustive verification.

Three candidate strategies:

1. **Lattice-functorial Hecke descent.** Construct a
   Jacobi-form-valued functor $J : \mathsf{Nik}_{\leq 19} \to
   \mathsf{WeakJac}$ with $J(\langle 2 \rangle) = \phi_{0, 1}$ and
   $J(L \hookrightarrow L') = \sigma_{L \hookrightarrow L'}$ compatible
   with Weil-representation transport, then prove $J$ is well-defined
   on cocones. Scheithauer 2009 provides the Weil-representation side
   of this functor but not the Jacobi-form side.

2. **Modular-kernel uniformisation.** Extend the Eichler–Zagier
   theta decomposition at rank $t + 1$ to a canonical
   $J^{\mathrm{wk}}_{0, L}$-basis indexed by the discriminant-form
   cosets, then verify the zero-Fourier coefficient of $\phi_L$ in
   the descended basis. Gritsenko 1999 §5 provides this at
   genus-discriminant level; extension to full rank-5 discriminant
   forms requires a Scheithauer-type classification of level-$L$
   Jacobi forms, not in primary literature at $t = 4$.

3. **Kudla-programme Green-form descent.** Identify $c_L(0)$ as a
   Green-form regularised integral on $\mathcal{M}_L$ via Bruinier
   2014 / Kudla–Millson, then use Arakelov-geometric rigidity on the
   generating series. Requires extending Howard–Madapusi-Pera 2020
   (*Invent.\ Math.*\ 219) derived Kudla generating series to
   non-PEL Shimura varieties of signature $(2, 5)$.

None of the three is executed in published primary literature at
$t = 4, 5$.

## Inscription-ready TeX block

```latex
\begin{conjecture}[Gritsenko--Cl\'ery universality at $t \geq 4$]
\label{conj:gritsenko-clery-rank-ge-5-universality}
\ClaimStatusOpen
Let $L$ be a Nikulin-admissible even hyperbolic lattice of signature
$(1, t)$, $4 \leq t \leq 19$: primitively embedded in
$\Lambda_{K3} = 2 E_8(-1) \oplus 3 U$ with $L^\perp$ containing a
hyperbolic plane $U$. Let $\phi_L \in J^{\mathrm{wk}}_{0, L}$ be the
Hecke--Maass-descended weak Jacobi form obtained from
$\phi_{0, 1} \in J^{\mathrm{wk}}_{0, 1}$ along any primitive-sublattice
chain $\langle 2 \rangle \hookrightarrow L_1 \hookrightarrow \cdots
\hookrightarrow L$. The Borcherds lift
$\Phi_L = \mathrm{Borch}(\phi_L)$ has singular weight
\[
\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = \frac{c_L(0)}{2} \in \Z_{\geq 0},
\]
with $c_L(0)$ independent of the chain and equal to an explicit
lattice-arithmetic invariant computable via Gritsenko--Cl\'ery $2008$
Proposition~$2.3$ applied inductively.
\end{conjecture}

\begin{remark}[Scope of the conjecture]
\label{rem:gc-conj-scope-t4-t5}
Gritsenko--Cl\'ery $2018$ (\emph{Pure Appl.\ Math.\ Q.}~$15$, arXiv
$1804.04488$) prove Conjecture~\ref{conj:gritsenko-clery-rank-ge-5-universality}
at $t \leq 3$ (explicit case analysis over the $95$ Nikulin-admissible
rank-$4$ lattices of Belcastro $2002$), and verify it on every
lattice tabulated in Table~$4$ of that paper. At $t \geq 4$
the full Nikulin-admissibility cone carries uncountably many
$L$-lattices, forcing a uniform chain-independence theorem in place
of exhaustive verification. The Scheithauer $2006$/$2009$/$2017$
automorphic-product classifications, the Dittmann--Ma--Scheithauer
$2021$ and Ma $2018$ finiteness results on $2$-reflective lattices,
the Bruinier $2002$/$2014$ and Kudla--Millson--Rapoport Chern-class
and generating-series machinery, the M\"oller--Scheithauer $2023$
generalised-deep-hole uniformisation, and the Wang--Williams $2023$
pullback rigidity of $\Phi_{12}$ each establish related structural
statements on restricted strata (singular-weight reflective products
on signature-$(2, n)$ with $n \geq 3$, $2$-reflective finiteness,
image-side Heegner Chern classes, pullback rigidity of the
Fake-Monster lift) but do not imply the Hecke-descent uniformisation
required for Conjecture~\ref{conj:gritsenko-clery-rank-ge-5-universality}
across the full signature-$(1, t \geq 4)$ Nikulin cone. Three
candidate proof strategies --- lattice-functorial Jacobi descent,
discriminant-basis uniformisation via Gritsenko $1999$ \S$5$, or
Kudla-programme Green-form identification via Howard--Madapusi-Pera
$2020$ --- are compatible with the available machinery but
unexecuted in primary literature at $t = 4, 5$.
\end{remark}
```

## Consequence for C13 closure

The earlier C13 closure (state B) remains correct:

- **Rank 3 (signature $(1, 2)$):** state A (theorem-complete) under
  Borcherds 1998 Thm.~13.3 + Gritsenko–Nikulin 1998 Thm.~1.1 +
  Gritsenko–Cléry 2008 Thm.~3.
- **Rank 4 (signature $(1, 3)$):** state A under Borcherds 1995 §15 +
  Gritsenko–Nikulin 1998 Thm.~4.1 + Gritsenko–Cléry 2008 Table 3 +
  Scheithauer 2006 Thm.~4.7.
- **Rank 6 envelope (signature $(1, 5)$ at $3 U$):** state A under
  Borcherds 1998 Thm.~13.3 + Thm.~8.1 + Pfaffian Wave-16 U1 Prop.~3.1.
- **Rank $\geq 5$ general Nikulin-admissible $L$:** state B
  conditional on Conj.~5.1; Conj.~5.1 itself is state C at
  $t \geq 4$ outside Table 4 of Gritsenko–Cléry 2018.

No compound state-inflation to A is supported by Scheithauer
2006/2009/2017, Bruinier 2002/2014, Ma 2018, Dittmann–Ma–Scheithauer
2021, Möller–Scheithauer 2023, or Wang–Williams 2023.

## Cross-consistency notes

- **CLAUDE.md.** Subscript discipline preserved:
  $\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = c_L(0)/2$; $\Phi$-functor-
  vs-object-level scope preserved (the Borcherds lift
  $\Phi_L$ is not $\Phi_d(\cC)$; different symbols, different
  mathematics). The universal Borcherds weight identity at
  $N \in \{1, 2, 3, 4, 6\}$ (CHL scope) and $N \in \{1, \ldots, 8\}$
  (Gritsenko--Cléry 8-form scope on $\SpFour$-paramodular cover) is
  \emph{not} the same as GC Conj.~5.1: the former is verified at
  eight Nikulin-admissible $K3$-automorphism orders, the latter at
  every $L$ in the signature-$(1, t \geq 4)$ Nikulin cone.

- **CY-D dimensional stratification
  (\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex}
  Theorem~\ref{thm:borcherds-weight-kappa-BKM-universal}).** The
  universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ at
  $N \in \{1, \ldots, 8\}$ is established via Borcherds 1998
  Thm.~13.3 on $\SpFour$-paramodular covers and the Gritsenko 1994
  $\Gamma_0(N)^+$ construction; the proof does *not* pass through
  GC Conj.~5.1 and is unaffected by its frontier status at
  $t \geq 4$.

- **C15 Mordell–Weil Delta-5 real roots (state-B).** The elliptic-
  fibration signature-$(2, 16)$ or $(2, 18)$ candidate for a common
  ambient GBKM $\mathfrak{g}_{\mathrm{amb}}$ on
  $\widetilde{\Lambda}_{K3}$ of signature $(4, 20)$ remains frontier;
  independent of Conj.~5.1 (Conj.~5.1 is on signature-$(1, t)$
  polarisation cones, not on signature-$(2, n)$ ambient lattices).
  No transport from C13 to C15.

- **Scheithauer $2000$ / non-Leech Niemeier 22-BKM census
  (\texttt{chapters/theory/cy\_to\_chiral.tex \S\ref{sec:psi-nonsurjectivity-gn}}).**
  Independent mathematics: those 22 BKMs live on signature-$(25, 1)$
  Niemeier-plus-hyperbolic lattices, outside the Nikulin cone
  scope of Conj.~5.1 and outside the GC 8-form cover. No interaction
  with C13 rank-5 closure.

- **Wave-1 spine** (`platonic_synthesis_post_adversarial.tex`) +
  **Wave-2 refinement** (Tier III residual-frontier list at line 855):
  the rank-$\geq 3$ $\mathfrak{g}_L$ family is Tier III at rank $\geq 5$;
  this closure confirms that Tier III status is frontier at
  $t \geq 4$ pending Conj.~5.1, not a conditional hypothesis in the
  state-B sense. The monograph should adopt `\ClaimStatusOpen` at
  the rank-5--19 rows outside Table 4 of GC 2018, not
  `\ClaimStatusConjectured`, to distinguish genuine-frontier gaps
  from conditional-theorem gaps.

- **CoHA treatise** (`CoHA_to_W_infty_treatise.tex`). The rank-3
  anchor $\mathfrak{g}_{\Delta_5}$ at $L = U \oplus \langle -2 \rangle$
  remains state A; no rank-$\geq 5$ CoHA constructions depend on
  Conj.~5.1.

## Primary-source register (delta beyond C13)

- Bruinier, J.H.\ $2014$ "Heegner divisors, $L$-functions and
  harmonic weak Maass forms" \emph{Ann.\ Math.}~$177$ (published 2013).
- Bruinier, J.H., Funke, J.\ $2004$ "On two geometric theta lifts"
  \emph{Duke Math.\ J.}~$125$, $45$--$90$.
- Bruinier, J.H., Kuss, M.\ $2001$ "Eisenstein series attached to
  lattices and modular forms on orthogonal groups" \emph{Manuscripta
  Math.}~$106$, $443$--$459$.
- Bruinier, J.H., Yang, T.\ $2006$ "CM values of automorphic Green
  functions on orthogonal groups over totally real fields"
  \emph{Compos.\ Math.}~$142$, $536$--$566$.
- Dittmann, M., Ma, S., Scheithauer, N.R.\ $2021$ "Finiteness of
  reflective lattices of signature $(2, n)$" \emph{Adv.\ Math.}~$386$,
  paper $107815$.
- Howard, B., Madapusi-Pera, K.\ $2020$ "Arithmetic of Borcherds
  products" \emph{Invent.\ Math.}~$219$, $1$--$97$.
- Kudla, S.S., Millson, J.J.\ $1990$ "Intersection numbers of cycles
  on locally symmetric spaces and Fourier coefficients of holomorphic
  modular forms in several complex variables"
  \emph{Publ.\ Math.\ IHES}~$71$, $121$--$172$.
- Ma, S.\ $2018$ "Finiteness of $2$-reflective lattices of signature
  $(2, n)$" \emph{Amer.\ J.\ Math.}~$140$, $1$--$36$ (arXiv:$1409.0476$).
- M\"oller, S., Scheithauer, N.R.\ $2023$ "Dimension formulae and
  generalised deep holes of the Leech lattice vertex operator algebra"
  \emph{Ann.\ Math.}~$197$, $221$--$288$.
- Scheithauer, N.R.\ $2009$ "The Weil representation of
  $\mathrm{SL}_2(\Z)$ and some applications" \emph{IMRN} $2009$ no.~$8$,
  $1488$--$1545$.
- Scheithauer, N.R.\ $2009$ "Some constructions of modular forms for
  the Weil representation of $\mathrm{SL}_2(\Z)$" \emph{Compos.\
  Math.}~$145$, $1015$--$1038$.
- Wang, H., Williams, B.\ $2023$ "Uniqueness of Borcherds products
  of singular weight" arXiv:$2303.04383$.
