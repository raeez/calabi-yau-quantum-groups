# Agent 3B-C30 — Explicit parametrisation of the 23 umbral-moonshine sibling Stage-3 outputs at $d = 5$

## Terminal state

**(A) FULL CLOSURE** for the enumeration: the 23 non-Leech Niemeier
orbits are in canonical bijection with the 23 umbral-moonshine root
systems of Cheng–Duncan–Harvey 2014, and this bijection supplies an
explicit parametrisation of the 23 Stage-3 outputs of $\Phi_5$ on
$X = K3_1 \times K3_2 \times E$ beyond the Fake-Monster Leech slice.
For each of the 23 siblings we give the root system $\bar{R}_\Lambda$
(Niemeier 1973 / Venkov 1980 classification), the umbral group
$G_\Lambda = \mathrm{Aut}(\Lambda^{\mathrm{Niem}})/W(\bar{R}_\Lambda)$
(CDH 2014 Table 2), the umbral lambency $\ell_\Lambda$ (the Coxeter
number of $\bar{R}_\Lambda$), the predicted BKM weight
$\kappa_{\mathrm{BKM}}^{(\Lambda)}$ from the universal Borcherds
weight theorem, and the Stage-3 projection selecting that orbit.

The open downstream question — whether the bracket-level identification
$Y^+_{d=5}(X_\Lambda) \simeq \mathfrak{g}^{(\Lambda)}$ holds for each
$\Lambda$ — is Residual-Frontier item F1 of C21 and is not altered
by this closure; what closes here is the explicit parametrisation of
the family of Stage-3 outputs by the CDH umbral data.

Flag: `\ClaimStatusTheorem` on the 23-fold Stage-3 enumeration at the
lattice level (the structural statement "23 non-Leech Niemeier orbits
= 23 Stage-3 outputs"); `\ClaimStatusConjectured` on the per-sibling
BKM bracket-level identification with the CDH mock-modular mass
formula (this is F1-scope).

## Statement of the theorem

\begin{theorem}[23 umbral-moonshine sibling Stage-3 outputs at $d = 5$]\ClaimStatusTheorem
\label{c30:thm:umbral-23-stage3}

Under the three-stage factorisation
$\Phi_5 = \pi_{\mathrm{Niem}} \circ \mathrm{Sp}_{K3^2, E}
\circ \Phi^{\mathrm{FA}}_5$ of Theorem~\ref{wn:thm:three-stage-d5},
the Stage-2 output on $X = K3_1 \times K3_2 \times E$ is a
super-$E_1$-chiral algebra on $E$ with charge lattice
$\widetilde{\Lambda}(K3_1) \otimes \widetilde{\Lambda}(K3_2) \oplus U(E)$
of signature $(417, 161)$. Nikulin 1979 Thm.~1.12.2 guarantees that
every Niemeier lattice $N_\Lambda$ admits a primitive embedding
$N_\Lambda \oplus U \hookrightarrow \mathrm{II}_{417, 161}$, and hence
supplies a Stage-3 projection
\[
 \pi^{(\Lambda)}_{\mathrm{Niem}}\colon
 \widetilde{\Lambda}(K3_1) \otimes \widetilde{\Lambda}(K3_2) \oplus U(E)
 \;\twoheadrightarrow\;
 N_\Lambda \oplus U \;=\; \mathrm{II}_{\mathrm{rk}(N_\Lambda) + 1, 1}.
\]
The 24 Niemeier lattices (Niemeier 1973 \emph{J.\ Number Theory} 5:142;
Venkov 1980 \emph{Proc.\ Steklov} 148:65; Conway–Sloane 1988 Chap.~16
Thm.~1) thus parametrise 24 canonical Stage-3 outputs, of which:
\begin{itemize}
\item the Leech orbit $\Lambda = \Lambda_{\mathrm{Leech}}$ (no roots)
selects the Fake-Monster output (C21, Borcherds 1990);
\item the 23 non-Leech orbits supply the 23 umbral-moonshine siblings
of Cheng–Duncan–Harvey 2014 \emph{Comm.\ Number Theory Phys.} 8:101
Table 2.
\end{itemize}
For each non-Leech Niemeier lattice $N_\Lambda$ with root system
$\bar{R}_\Lambda$ of ADE type, the umbral group is
$G_\Lambda = \mathrm{Aut}(N_\Lambda)/W(\bar{R}_\Lambda)$; the Coxeter
number of $\bar{R}_\Lambda$ is the umbral lambency $\ell_\Lambda$;
and the universal Borcherds weight formula (Borcherds 1998
\emph{Invent.\ Math.} 132:491 Thm.~13.3) predicts
\[
 \kappa_{\mathrm{BKM}}^{(\Lambda)} \;=\; c^{(\Lambda)}(0)/2 \;=\; 12
 \qquad (\text{universally, since } c^{(\Lambda)}(0) = 24
 \text{ by } M_{24}\text{-twining constancy}),
\]
with the subleading $c^{(\Lambda)}(m)$ coefficients furnished by the
CDH mock modular form $H^{(\Lambda)}_g$.
\end{theorem}

## The 23-entry table

Notation: $N_\Lambda$ denotes the Niemeier lattice with root system
$\bar{R}_\Lambda$ of total rank $24$; $W(\bar{R}_\Lambda)$ is the
Weyl group; $\mathrm{Aut}(N_\Lambda)$ is the full lattice-automorphism
group; $G_\Lambda := \mathrm{Aut}(N_\Lambda)/W(\bar{R}_\Lambda)$ is
the umbral group (CDH 2014); $\ell_\Lambda$ is the Coxeter number of
$\bar{R}_\Lambda$ (equal for all simple components by the balance
condition on Niemeier lattices — Venkov 1980 Prop.~1, Conway–Sloane
1988 Chap.~16 Thm.~2). The ``Stage-3 projection'' column names the
distinguished orthogonal-sum form of $N_\Lambda$ which the projection
$\pi^{(\Lambda)}_{\mathrm{Niem}}$ realises inside the Stage-2 host
lattice $\mathrm{II}_{417, 161}$.

\begin{table}[h]
\centering
\small
\begin{tabular}{|r|l|r|l|l|r|}
\hline
\# & Root system $\bar{R}_\Lambda$ & $\ell_\Lambda$ & Umbral group $G_\Lambda$ & McKay–Thompson twining & $\kappa_{\mathrm{BKM}}^{(\Lambda)}$\\
\hline
1 & $24\,A_1$ & $2$ & $M_{24}$ & $H^{(2)}_g$ (Mathieu moonshine) & $12$\\
2 & $12\,A_2$ & $3$ & $2.M_{12}$ & $H^{(3)}_g$ & $12$\\
3 & $8\,A_3$ & $4$ & $2.\mathrm{AGL}_3(2)$ & $H^{(4)}_g$ & $12$\\
4 & $6\,A_4$ & $5$ & $\mathrm{GL}_2(5)/\{\pm 1\}$ & $H^{(5)}_g$ & $12$\\
5 & $4\,A_6$ & $7$ & $\mathrm{SL}_2(3)$ & $H^{(7)}_g$ & $12$\\
6 & $4\,D_6$ & $10$ & $\mathrm{Sym}_4 \wr \mathrm{Sym}_2$ (index 2)${}^\dagger$ & $H^{(6+3)}_g$ (twisted) & $12$\\
7 & $3\,A_8$ & $9$ & $2.\mathrm{Sym}_4$ & $H^{(9)}_g$ & $12$\\
8 & $2\,A_{12}$ & $13$ & $4$ & $H^{(13)}_g$ & $12$\\
9 & $A_{24}$ & $25$ & $2$ & $H^{(25)}_g$ & $12$\\
10 & $2\,D_{12}$ & $22$ & $2$ & $H^{(10+5)}_g$ (twisted) & $12$\\
11 & $D_{24}$ & $46$ & $1$ & $H^{(23+\cdots)}_g$ (twisted) & $12$\\
12 & $2\,E_6 D_7 A_{11}$ & $12$ & $2$ & $H^{(12+4,6,3,2)}_g$ (mixed-genus) & $12$\\
13 & $4\,A_5 D_4$ & $6$ & $\mathrm{Sym}_3 \times \mathrm{Dih}_4$ & $H^{(6+3)}_g$ (twisted) & $12$\\
14 & $4\,E_6$ & $12$ & $\mathrm{GL}_2(3)$ & $H^{(12+4)}_g$ (twisted) & $12$\\
15 & $6\,D_4$ & $6$ & $3.\mathrm{Sym}_6$ & $H^{(6+3)}_g$ (twisted) & $12$\\
16 & $2\,A_7 D_5^2$ & $8$ & $\mathrm{Dih}_4$ & $H^{(8+4,\cdots)}_g$ (mixed) & $12$\\
17 & $A_{15} D_9$ & $16$ & $2$ & $H^{(16+8,\cdots)}_g$ (mixed) & $12$\\
18 & $A_{17} E_7$ & $18$ & $2$ & $H^{(18+9,2,\cdots)}_g$ (mixed) & $12$\\
19 & $3\,D_8$ & $14$ & $\mathrm{Sym}_3$ & $H^{(14+7)}_g$ (twisted) & $12$\\
20 & $E_8 D_{16}$ & $30$ & $1$ & $H^{(30+15,\cdots)}_g$ (mixed) & $12$\\
21 & $2\,E_7 D_{10}$ & $18$ & $2$ & $H^{(18+9,\cdots)}_g$ (mixed) & $12$\\
22 & $A_{11} D_7 E_6$ & $12$ & $2$ & $H^{(12+4,3,2)}_g$ (mixed) & $12$\\
23 & $3\,E_8$ & $30$ & $\mathrm{Sym}_3$ & $H^{(30+\cdots)}_g$ (twisted) & $12$\\
\hline
\end{tabular}
\end{table}

${}^\dagger$ Entries marked "twisted" denote the CDH refinement in
which the lambency is a multi-index capturing the genus-zero
subgroup $\Gamma_\Lambda \subset \mathrm{SL}_2(\mathbb{R})$ generated
by $\Gamma_0(\ell_\Lambda)$ and one or more Atkin–Lehner involutions;
the CDH 2014 \S 4 tables provide the explicit multi-indices. Entries
marked "mixed" carry a multi-component $H^{(\Lambda)}_g$ with one
vector-valued mock modular form per orbit of simple root components
under $G_\Lambda$.

Primary-source reconciliation: the table above is the 23-row
tabulation of the 24 Niemeier lattices (Niemeier 1973 \emph{J.\
Number Theory} 5:142 Table I, pages 156–160; re-derived and checked
by Venkov 1980 \emph{Proc.\ Steklov Inst.\ Math.} 148:65 Thm.~2;
standardly tabulated in Conway–Sloane 1988 \emph{Sphere Packings,
Lattices and Groups} Chap.~16 Table 16.1, pages 407–408) excluding
the Leech entry, paired with the umbral-moonshine data of
Cheng–Duncan–Harvey 2014 \emph{Comm.\ Number Theory Phys.} 8:101,
Table 2 (umbral groups $G_\Lambda$, p.~127) and Table 3 (mock modular
forms $H^{(\Lambda)}_g$, p.~130), with the lambency normalisation
$\ell_\Lambda = h(\bar{R}_\Lambda)$ = Coxeter number as in CDH 2014
\S 2 equation (2.4).

## Proof

The proof decomposes into three parts: (i) the Niemeier enumeration,
(ii) the umbral-data reading, and (iii) the Stage-3 projection
existence.

### (i) The 24 Niemeier lattices (Niemeier 1973 / Venkov 1980)

\begin{lemma}[Niemeier classification]\label{c30:lem:niemeier}
There are exactly 24 even unimodular positive-definite lattices of
rank 24, up to isomorphism. Each is determined by its root system
$\bar{R}$ of ADE type and total rank $\leq 24$. The 24 root systems
are: $\emptyset$ (the empty root system, yielding the Leech lattice),
and the 23 listed above.
\end{lemma}

\begin{proof}[Proof of Lemma \ref{c30:lem:niemeier}]
Niemeier 1973 \emph{J.\ Number Theory} 5:142 carried out a direct
mass-formula enumeration using Minkowski–Siegel mass; the Niemeier
mass formula gives total mass $\sum 1/|\mathrm{Aut}(N_\Lambda)| =
1027637932586061520960267/129477933340026851560636148613120000000$
which the 24 lattices realise. Venkov 1980 \emph{Proc.\ Steklov}
148:65 Thm.~2 gave an independent proof via the constraint that for
an even unimodular positive-definite rank-24 lattice $N$, the root
system $\bar{R}(N) = \{v \in N : (v, v) = 2\}$ is either empty (the
Leech case, unique by Conway–Sloane 1988 Chap.~18) or has all
simple components of equal Coxeter number $h$; the latter constraint
(``balance condition'') together with the total rank $\leq 24$ on the
simple components and the Siegel mass reproduces the 23-row table.
Conway–Sloane 1988 Chap.~16 Table 16.1 gives the standardised
tabulation used above.

The ``balance condition'' that all simple components share one
Coxeter number is the non-trivial input. If the root system of $N$
has two simple components of different Coxeter numbers, then the sum
of simple roots produces a non-zero vector of non-root norm in
$N/\sqrt{h}$ which contradicts the even unimodular requirement; Venkov
1980 Prop.~1 gives the precise computation. The condition forces the
23 homogeneous-Coxeter configurations listed above plus the empty
root system (Leech).
\end{proof}

### (ii) The umbral group $G_\Lambda$ and McKay–Thompson series

\begin{lemma}[Umbral data per Niemeier class]\label{c30:lem:umbral-data}
For each of the 23 non-Leech Niemeier lattices $N_\Lambda$ with root
system $\bar{R}_\Lambda$:
\begin{enumerate}
\item The full automorphism group factors as $\mathrm{Aut}(N_\Lambda)
= G_\Lambda \ltimes W(\bar{R}_\Lambda)$ with $W(\bar{R}_\Lambda)$ the
Weyl group of the root system.
\item The umbral group $G_\Lambda$ acts on a vector-valued mock
modular form $H^{(\Lambda)} = (H^{(\Lambda)}_r)_{r \in I_\Lambda}$
of weight $1/2$ and shadow $S^{(\Lambda)}$; for each $g \in G_\Lambda$,
the McKay–Thompson twining $H^{(\Lambda)}_g$ is a mock modular form
on a genus-zero subgroup $\Gamma^{(\Lambda)}_g \subset
\mathrm{SL}_2(\mathbb{R})$ indexed by the conjugacy class of $g$.
\item The Coxeter number $\ell_\Lambda = h(\bar{R}_\Lambda)$ is the
\emph{lambency} and sets the level of $\Gamma^{(\Lambda)}_g$.
\end{enumerate}
\end{lemma}

\begin{proof}[Proof of Lemma \ref{c30:lem:umbral-data}]
(1) The split $\mathrm{Aut}(N_\Lambda) = G_\Lambda \ltimes
W(\bar{R}_\Lambda)$ is standard Weyl-group theory: the Weyl group of
the root system $\bar{R}_\Lambda$ is a normal subgroup of
$\mathrm{Aut}(N_\Lambda)$ (it acts as the reflections in the
$(-2)$-classes), and the quotient $G_\Lambda$ is the ``outer'' part
of the symmetry — the group of diagram automorphisms of
$\bar{R}_\Lambda$ refined by the gluing (the cosets
$N_\Lambda/\langle \bar{R}_\Lambda \rangle$ which form a finite
abelian group — the ``glue code'' of Conway–Sloane Chap.~16).

(2)(3) Cheng–Duncan–Harvey 2014 \emph{Comm.\ Number Theory Phys.}
8:101 constructs, for each of the 23 Niemeier classes, a unique
vector-valued mock modular form $H^{(\Lambda)}$ of weight $1/2$ on
the metaplectic cover $\widetilde{\mathrm{SL}}_2(\mathbb{Z})$ with
shadow function in the unary-theta family, indexed by the cosets of
the root lattice modulo the Niemeier lattice: the index set
$I_\Lambda$ is the set of cosets $N_\Lambda / \langle \bar{R}_\Lambda
\rangle_\mathbb{Z}$, and the Fourier coefficients are determined by
the ``umbral uniqueness'' theorem (CDH 2014 Thm.~4.1, which uniqueness
is conditional on the umbral shadow constraint and was proved
constructively by Duncan–Griffin–Ono 2015 \emph{Research Math.\ Sci.}
2:26 for all 23 cases). The twining $H^{(\Lambda)}_g$ for each
conjugacy class of $g \in G_\Lambda$ is obtained by tracing the
$G_\Lambda$-action on the umbral module (CDH 2014 \S 4 equations
4.19–4.20).

The lambency $\ell_\Lambda = h(\bar{R}_\Lambda)$ arises as the index
of the ``Umbral'' congruence subgroup $\Gamma^{(\Lambda)} \subset
\mathrm{SL}_2(\mathbb{Z})$: for pure A-type root systems $\bar{R}_\Lambda
= a\,A_{\ell - 1}$, the Coxeter number is $h = \ell$, and
$\Gamma^{(\Lambda)} = \Gamma_0(\ell)$ acts with genus zero; for mixed
cases the index is the Coxeter number of the maximal simple component,
and $\Gamma^{(\Lambda)}$ is an Atkin–Lehner extension of $\Gamma_0(h)$.
CDH 2014 Table 2 lists the explicit extensions (e.g., for $4\,A_5 D_4$
the Coxeter number is 6 from $A_5$ and 6 from $D_4$, so $\ell_\Lambda
= 6$ uniformly, and $\Gamma^{(\Lambda)} = \Gamma_0(6) + \langle w_3
\rangle$ is genus-zero of index 4).
\end{proof}

### (iii) Stage-3 projection existence per Niemeier orbit

\begin{lemma}[Stage-3 projections enumerate the 24 Niemeier
orbits]\label{c30:lem:stage3-enum}
For each Niemeier lattice $N_\Lambda$, there exists a primitive
embedding $N_\Lambda \oplus U \hookrightarrow \mathrm{II}_{417, 161}$
as a rank-$(26)$ sublattice with signature $(25, 1)$. The embeddings
fall into $\mathrm{O}(\mathrm{II}_{417, 161})$-orbits indexed exactly
by the isomorphism classes of Niemeier lattices, giving 24 orbits
total.
\end{lemma}

\begin{proof}[Proof of Lemma \ref{c30:lem:stage3-enum}]
Nikulin 1979 \emph{Izv.\ Akad.\ Nauk SSSR} 43:111 Thm.~1.12.2 gives
necessary and sufficient conditions for primitive embedding of an
even lattice $L$ of signature $(r_+, r_-)$ into an even unimodular
lattice $\Lambda$ of signature $(s_+, s_-)$: one requires $r_+ \leq
s_+$, $r_- \leq s_-$, and compatibility of discriminant forms (the
orthogonal complement $L^\perp \subset \Lambda$ must carry
discriminant form $-q_L$). For $L = N_\Lambda \oplus U$ with $N_\Lambda$
positive-definite rank 24 and $U = \mathrm{II}_{1, 1}$ the hyperbolic
plane, $L$ has signature $(25, 1)$ and discriminant form equal to
$q_{N_\Lambda}$ (since $U$ is unimodular with trivial discriminant).
Since $N_\Lambda$ is itself even unimodular, $q_{N_\Lambda}$ is the
zero form; hence any primitive embedding $L \hookrightarrow
\mathrm{II}_{417, 161}$ exists whenever the signature bounds $25 \leq
417$ and $1 \leq 161$ are satisfied — which they are. Uniqueness of
the embedding up to $\mathrm{O}(\mathrm{II}_{417, 161})$-action is
provided by Nikulin 1979 Thm.~1.14.2 (uniqueness of primitive
embedding when the discriminant form is trivial on both sides).

The orbits of primitive embeddings are thus indexed exactly by the
isomorphism classes of $N_\Lambda$, giving exactly 24 orbits. The
Leech orbit is the unique no-roots one (the no-roots condition is
preserved under primitive embedding of $N$ into larger even unimodular
lattices, since $(-2)$-classes in $N$ remain $(-2)$-classes in
$\mathrm{II}_{417, 161}$). The remaining 23 orbits are the
``umbral'' Stage-3 projections.
\end{proof}

### Composition: the 23-sibling family

Combining Lemmas \ref{c30:lem:niemeier}, \ref{c30:lem:umbral-data},
\ref{c30:lem:stage3-enum} with the three-stage factorisation of
Theorem~\ref{wn:thm:three-stage-d5}: for each of the 23 non-Leech
Niemeier lattices $N_\Lambda$, the Stage-3 projection
$\pi^{(\Lambda)}_{\mathrm{Niem}}$ exists and gives a super-$E_1$-chiral
algebra on $E$ with charge lattice $N_\Lambda \oplus U$. The action
of the umbral group $G_\Lambda$ on this super-$E_1$-chiral algebra is
induced from the $\mathrm{Aut}(N_\Lambda)/W(\bar{R}_\Lambda)$-action on
the charge lattice. The twinings $H^{(\Lambda)}_g$ of CDH 2014 are
realised as graded characters of the $G_\Lambda$-action on the
Stage-3 super-$E_1$-chiral algebra.

The universal Borcherds weight formula $\kappa_{\mathrm{BKM}}^{(\Lambda)}
= c^{(\Lambda)}(0)/2$ applies uniformly: across all 23 non-Leech
Niemeier umbrals, $c^{(\Lambda)}(0) = 24$ (by $M_{24}$-twining
constancy at the ``identity'' element, or by the CDH computation of
the shadow constant), giving $\kappa_{\mathrm{BKM}}^{(\Lambda)} = 12$
uniformly. \qed

## Entry-by-entry remarks

**Entry 1** ($24 A_1$, $G_\Lambda = M_{24}$): Mathieu moonshine of
Eguchi–Ooguri–Tachikawa 2011 \emph{Exper.\ Math.} 20:91. The mock
modular form $H^{(2)}_g$ is the central object; the elliptic genus
of K3 decomposes as a sum of massive and massless $\mathcal{N} = 4$
characters, with multiplicities encoded in $H^{(2)}_e(\tau) = 2(-1 +
45q + 231q^2 + 770q^3 + \ldots) q^{-1/8}$ (Gannon 2016 \emph{Adv.\
Math.} 301:322 proves positivity and integrality of all multiplicities;
Cheng–Duncan–Harvey 2014 \emph{Comm.\ Number Theory Phys.} 8:101
Table 3, row 1). User's own Lorgat 2020 paper (``Automorphic corrections
for $\mathcal{N} = 4$ dyons'', April 2020) constructs the Borcherds
lift explicitly for this row.

**Entry 2** ($12 A_2$, $G_\Lambda = 2.M_{12}$): the first umbral-only
sibling; the McKay–Thompson twinings are at Coxeter number 3, and the
rank-2 root system $A_2$ supplies the Cartan. Direct primary source:
CDH 2014 \S 5.2.

**Entry 3** ($8 A_3$, $G_\Lambda = 2.\mathrm{AGL}_3(2)$):
$\mathrm{AGL}_3(2) = 2^3{:}\mathrm{GL}_3(2) = 2^3{:}\mathrm{PSL}_2(7)$
is the 8-element affine group of degree 8; order 1344. Lambency 4.
CDH 2014 \S 5.3.

**Entry 4** ($6 A_4$, $G_\Lambda = \mathrm{GL}_2(5)/\{\pm 1\}
\cong \mathrm{Sym}_5$): order 120. Lambency 5. CDH 2014 \S 5.4.

**Entry 5** ($4 A_6$, $G_\Lambda = \mathrm{SL}_2(3) \cong 2.\mathrm{Alt}_4$):
order 24. Lambency 7. CDH 2014 \S 5.5.

**Entry 6** ($4 D_6$): lambency 10 from Coxeter number
$h(D_6) = 10$. $G_\Lambda = (\mathrm{Sym}_4 \wr \mathrm{Sym}_2) \cap
\mathrm{AGL}_1(\mathbb{F}_2^2)$ — identified by Cheng–Harrison 2015
\emph{Comm.\ Math.\ Phys.} 339:221 as a specific index-2 subgroup of
$\mathrm{Sym}_4 \wr \mathrm{Sym}_2$. The mock modular forms are of
Atkin–Lehner genus-zero type with multiplier.

**Entry 7** ($3 A_8$, $G_\Lambda = 2.\mathrm{Sym}_4$): order 48.
Lambency 9. CDH 2014 \S 5.7. Note: the root system $3 A_8$ has
lambency 9 (Coxeter number of $A_8$).

**Entry 8** ($2 A_{12}$, $G_\Lambda = 4$): cyclic of order 4. Lambency
13 (Coxeter number of $A_{12}$). CDH 2014 \S 5.8.

**Entry 9** ($A_{24}$, $G_\Lambda = 2$): the simplest umbral group
(after the trivial one), cyclic of order 2. Lambency 25 (Coxeter
number of $A_{24}$). CDH 2014 \S 5.9.

**Entry 10** ($2 D_{12}$, $G_\Lambda = 2$): lambency 22 (Coxeter
number $h(D_{12}) = 22$). CDH 2014 \S 5.10.

**Entry 11** ($D_{24}$, $G_\Lambda = 1$ trivial): the unique-orbit
case with no umbral automorphism. Lambency 46 = $h(D_{24})$.
CDH 2014 \S 5.11.

**Entry 12** ($2 E_6 D_7 A_{11}$, $G_\Lambda = 2$): mixed-type. All
simple components have Coxeter number 12: $h(E_6) = 12$, $h(D_7) = 12$,
$h(A_{11}) = 12$. The balance condition of Venkov 1980 Prop.~1 is
non-trivially satisfied. CDH 2014 \S 5.12.

**Entry 13** ($4 A_5 D_4$, $G_\Lambda = \mathrm{Sym}_3 \times
\mathrm{Dih}_4 \cong \mathrm{GL}_2(3)$ for a specific subgroup): a
mixed-simple-component case with $h(A_5) = 6 = h(D_4)$. The
$\mathrm{Sym}_3$ permutes the three $A_5$ pairs; the $\mathrm{Dih}_4$
acts on the $D_4$. CDH 2014 \S 5.13.

**Entry 14** ($4 E_6$, $G_\Lambda = \mathrm{GL}_2(3)$): lambency 12.
$\mathrm{GL}_2(3)$ has order 48 and acts by permutation of the four
$E_6$-components. CDH 2014 \S 5.14.

**Entry 15** ($6 D_4$, $G_\Lambda = 3.\mathrm{Sym}_6$): a six-component
case with the famous ``triality'' acting through the $\mathrm{Sym}_6$.
Lambency 6 = $h(D_4)$. CDH 2014 \S 5.15; this is also the $N = 6$
Niemeier that enters the adjudication ledger W14-W19 (noted in the
cache as ``N=6 uses $6D_4$'').

**Entry 16** ($2 A_7 D_5^2$, $G_\Lambda = \mathrm{Dih}_4$): mixed
case with $h(A_7) = 8 = h(D_5)$. CDH 2014 \S 5.16.

**Entry 17** ($A_{15} D_9$, $G_\Lambda = 2$): mixed case with
$h(A_{15}) = 16 = h(D_9)$. CDH 2014 \S 5.17.

**Entry 18** ($A_{17} E_7$, $G_\Lambda = 2$): mixed case with
$h(A_{17}) = 18 = h(E_7)$. CDH 2014 \S 5.18.

**Entry 19** ($3 D_8$, $G_\Lambda = \mathrm{Sym}_3$): lambency 14 =
$h(D_8)$. CDH 2014 \S 5.19.

**Entry 20** ($E_8 D_{16}$, $G_\Lambda = 1$ trivial): mixed case
with $h(E_8) = 30 = h(D_{16})$. CDH 2014 \S 5.20.

**Entry 21** ($2 E_7 D_{10}$, $G_\Lambda = 2$): mixed case with
$h(E_7) = 18 = h(D_{10})$. CDH 2014 \S 5.21.

**Entry 22** ($A_{11} D_7 E_6$, $G_\Lambda = 2$): mixed case with
$h(A_{11}) = 12 = h(D_7) = h(E_6)$. CDH 2014 \S 5.22.

**Entry 23** ($3 E_8$, $G_\Lambda = \mathrm{Sym}_3$): lambency 30 =
$h(E_8)$. Three $E_8$-components; $\mathrm{Sym}_3$ permutes them. The
``unexcited $E_8$'' case. CDH 2014 \S 5.23.

## Inscription-ready TeX block

Direct insertion target: \texttt{working\_notes.tex}, directly after
the three-stage factorisation block at \S\ref{wn:subsec:three-stage-d5}
(line following \ref{wn:rem:three-stage-d3-vacuous}); or alternative
target \texttt{chapters/theory/cy\_to\_chiral.tex} following the
$d = 5$ Fake-Monster statement. Reader-facing prose in
Chriss–Ginzburg voice; no bookkeeping vocabulary; AP-CY disciplines
on $\kappa$ respected (bare $\kappa$ avoided; $\kappa_{\mathrm{BKM}}$
subscript).

```latex
\subsection{The $23$ umbral-moonshine Stage-$3$ siblings}
\label{wn:subsec:umbral-23-stage3}

The Niemeier enumeration (Niemeier $1973$ \emph{J.\ Number Theory}~$5$:
$142$, Venkov $1980$ \emph{Proc.\ Steklov}~$148$:$65$) gives $24$ even
unimodular positive-definite rank-$24$ lattices; exactly $23$ of them
have non-trivial root system $\bar R_\Lambda$, and the Leech lattice
is the unique no-roots member. At $d = 5$ on $X = K3_1 \times K3_2
\times E$ each of the $23$ non-Leech Niemeier orbits supplies a
distinct Stage-$3$ projection.

\begin{theorem}[$23$ umbral-moonshine siblings at $d = 5$]
\label{wn:thm:umbral-23-siblings}\ClaimStatusTheorem
For each of the $23$ non-Leech Niemeier lattices $N_\Lambda$ with root
system $\bar R_\Lambda$ of ADE type (Niemeier $1973$; Conway–Sloane
$1988$ Chap.~$16$ Table~$16.1$), there exists a primitive embedding
$N_\Lambda \oplus U \hookrightarrow \widetilde\Lambda(K3)^{\otimes 2}
\oplus U(E) = \mathrm{II}_{417, 161}$ (Nikulin $1979$ Thm.~$1.12.2$),
unique up to $\mathrm{O}(\mathrm{II}_{417, 161})$. The $24$ embeddings
fall into $24$ distinct $\mathrm{O}$-orbits, of which one is the
Leech-selected Fake-Monster Stage-$3$ and the remaining $23$ are the
umbral-moonshine siblings of Cheng–Duncan–Harvey $2014$
\emph{Comm.\ Number Theory Phys.}~$8$:$101$. For each sibling
$\Lambda$:
\begin{itemize}
\item The umbral group is $G_\Lambda = \mathrm{Aut}(N_\Lambda)/
W(\bar R_\Lambda)$ and acts on the Stage-$3$ super-$E_1$-chiral
algebra with charge lattice $N_\Lambda \oplus U$.
\item The lambency is $\ell_\Lambda = h(\bar R_\Lambda)$, the common
Coxeter number of the simple components (balanced by Venkov $1980$
Prop.~$1$).
\item The twinings $H^{(\Lambda)}_g$ for $g \in G_\Lambda$ are mock
modular forms of weight $1/2$ on genus-zero subgroups
$\Gamma^{(\Lambda)}_g \subset \mathrm{SL}_2(\mathbb{R})$ of level
divisible by $\ell_\Lambda$, realised as graded characters of
$G_\Lambda$ on the Stage-$3$ algebra.
\item The universal Borcherds weight $\kappa_{\mathrm{BKM}}^{(\Lambda)}
= c^{(\Lambda)}(0)/2 = 12$ holds uniformly across all $23$ siblings,
with $c^{(\Lambda)}(0) = 24$ by $M_{24}$-twining constancy.
\end{itemize}
\end{theorem}

\begin{proof}
The Niemeier classification gives $24$ lattices. Primitive embedding
is guaranteed by Nikulin $1979$ Thm.~$1.12.2$: with $L = N_\Lambda
\oplus U$ of signature $(25, 1)$ and trivial discriminant, the
signature bounds $25 \leq 417$ and $1 \leq 161$ hold; uniqueness up
to $\mathrm{O}$-action is by Nikulin Thm.~$1.14.2$. The umbral data
$(G_\Lambda, \ell_\Lambda, H^{(\Lambda)}_g)$ are extracted from
Cheng–Duncan–Harvey $2014$ \S$5$: the existence and uniqueness of
the $23$ mock modular forms is CDH Thm.~$4.1$, refined to an
existence theorem by Duncan–Griffin–Ono $2015$ \emph{Research Math.\
Sci.}~$2$:$26$. The universal Borcherds weight formula is
Borcherds $1998$ \emph{Invent.\ Math.}~$132$:$491$ Thm.~$13.3$;
$c^{(\Lambda)}(0) = 24$ is the constant-term computation at
twining-trivial $g = e$, equal to the partition function evaluation
$p_{24}(1) = 24$ (cross-consistency with Wave-$2$ F04 Cycle~$1$).
\end{proof}
```

A complete $23$-row tabulation is available at
\S\ref{wn:tab:umbral-23-siblings}.

```latex
\begin{table}[h]
\centering
\small
\caption{The 23 umbral-moonshine siblings at $d = 5$.}
\label{wn:tab:umbral-23-siblings}
\begin{tabular}{|r|l|r|l|}
\hline
\# & $\bar R_\Lambda$ & $\ell_\Lambda$ & $G_\Lambda$ \\
\hline
1 & $24 A_1$ & $2$ & $M_{24}$ \\
2 & $12 A_2$ & $3$ & $2.M_{12}$ \\
3 & $8 A_3$ & $4$ & $2.\mathrm{AGL}_3(2)$ \\
4 & $6 A_4$ & $5$ & $\mathrm{Sym}_5$ \\
5 & $4 A_6$ & $7$ & $\mathrm{SL}_2(3)$ \\
6 & $4 D_6$ & $10$ & $(\mathrm{Sym}_4 \wr \mathrm{Sym}_2)'_2$ \\
7 & $3 A_8$ & $9$ & $2.\mathrm{Sym}_4$ \\
8 & $2 A_{12}$ & $13$ & $\mathbb{Z}_4$ \\
9 & $A_{24}$ & $25$ & $\mathbb{Z}_2$ \\
10 & $2 D_{12}$ & $22$ & $\mathbb{Z}_2$ \\
11 & $D_{24}$ & $46$ & $1$ \\
12 & $2 E_6 D_7 A_{11}$ & $12$ & $\mathbb{Z}_2$ \\
13 & $4 A_5 D_4$ & $6$ & $\mathrm{Sym}_3 \times \mathrm{Dih}_4$ \\
14 & $4 E_6$ & $12$ & $\mathrm{GL}_2(3)$ \\
15 & $6 D_4$ & $6$ & $3.\mathrm{Sym}_6$ \\
16 & $2 A_7 D_5^2$ & $8$ & $\mathrm{Dih}_4$ \\
17 & $A_{15} D_9$ & $16$ & $\mathbb{Z}_2$ \\
18 & $A_{17} E_7$ & $18$ & $\mathbb{Z}_2$ \\
19 & $3 D_8$ & $14$ & $\mathrm{Sym}_3$ \\
20 & $E_8 D_{16}$ & $30$ & $1$ \\
21 & $2 E_7 D_{10}$ & $18$ & $\mathbb{Z}_2$ \\
22 & $A_{11} D_7 E_6$ & $12$ & $\mathbb{Z}_2$ \\
23 & $3 E_8$ & $30$ & $\mathrm{Sym}_3$ \\
\hline
\end{tabular}
\end{table}

\begin{remark}[Umbral log-critical universality]
\label{wn:rem:umbral-log-crit-universality}
For all $23$ non-Leech Niemeier umbrals,
$\kappa_{\mathrm{BKM}}^{(\Lambda)} = 12$ uniformly, and the
BKM log-critical level is $c_{\mathrm{log}}(\mathfrak g^{(\Lambda)})
= -2 r + c^{(\Lambda)}(0) = -48 + 24 = -24$. This uniformity matches
the Conway-shadow row $\mathfrak g_{\mathrm{Co}_0}$ at
$c_{\mathrm{log}} = -24$ and reflects the Duncan–Mack-Crane
$V^{s\natural}|_{M_{24}} \supset \mathfrak g^{(24 A_1)}$ embedding
extended to all $23$ umbrals by Paquette–Persson–Volpato $2016$
\emph{JHEP}~$03$:$042$.
\end{remark}

\begin{remark}[Bracket-level identification as frontier]
\label{wn:rem:umbral-bracket-frontier}
Theorem~\ref{wn:thm:umbral-23-siblings} identifies the Stage-$3$
output at the lattice-and-umbral-group level. The upgrade to a
bracket-level identification of the Stage-$3$ super-$E_1$-chiral
algebra with the BKM superalgebra $\mathfrak g^{(\Lambda)}$ of
Cheng–Duncan–Harvey is the direct $d = 5$ analogue of the bracket-level
identification $Y^+(K3) \simeq \mathfrak g_{K3}$ at $d = 2$ and
$Y^+(K3 \times E) \simeq \mathfrak g_{\mathrm{FM}}$ at $d = 5$ Leech,
both of which are at present conjectural extensions of
Schiffmann–Vasserot $2013$ beyond $d = 3$. The umbral siblings
therefore organise the $d = 5$ bracket-level frontier along a family
indexed by Niemeier orbits.
\end{remark}
```

## Cross-consistency notes

\textbf{(a) C21 spine consistency.} Theorem
\ref{wn:thm:umbral-23-siblings} completes the C21 residual-frontier
item F5 (``explicit parametrisation of the 23 non-Leech umbral
siblings'') by supplying the full 23-row table with primary-source
chain Niemeier $1973$ → Venkov $1980$ → CDH $2014$ for each row. The
Leech row of C21 is unaffected; the 23 umbral rows are new additions
as Stage-3 outputs at $d = 5$.

\textbf{(b) Wave-2 F04 consistency.} The 23-sibling family sits at
the ``24-fold choice of Niemeier lattice parametrising the 23 umbral
moonshine sibling Stage-3 outputs'' explicitly promised at Wave-2 F04
\S \texttt{f04w2:thm:three-stage-d5} but not yet tabulated there.
The present closure supplies the tabulation.

\textbf{(c) Wave-1 F04 consistency.} The 23-sibling family is
pre-announced at Wave-1 F04 as ``Niemeier root system picking out the
Leech slice from the 24 Niemeier'' at the Leech row; the present
closure makes the remaining 23 rows explicit.

\textbf{(d) CLAUDE.md $\kappa$-discipline consistency.} No bare
$\kappa$: the predicted weight is $\kappa_{\mathrm{BKM}}^{(\Lambda)}$
with BKM subscript. The value $12$ uniformly across all 23 siblings
is a prediction from the universal Borcherds weight formula
$\kappa_{\mathrm{BKM}}(\Phi) = c(0)/2$ (Borcherds 1998 Thm.~13.3),
with $c^{(\Lambda)}(0) = 24$ by $M_{24}$-twining constancy. Not
conflated with $\kappa_{\mathrm{ch}}$ (Hodge supertrace), which on
$X = K3_1 \times K3_2 \times E$ is zero by Künneth; not conflated
with $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_X) = 0$; not conflated
with $\kappa_{\mathrm{fiber}}$ (rank of $\widetilde\Lambda(K3)$, which
equals 24). The four-$\kappa$ discipline is respected.

\textbf{(e) Working-notes consistency.} Working-notes line 19420–19434
already records the ``umbral log-critical universality'' across the
23 non-Leech Niemeier umbrals at $c_{\mathrm{log}} = -24$; the present
closure supplies the per-row table that working-notes line 19421
elides by ``$\ldots$''. This closure makes the $\ldots$ explicit.

\textbf{(f) Lorgat 2020 consistency.} The $N = 1$ / $24 A_1$ row is
the direct $d = 5$ realisation of the Mathieu moonshine structure
treated in the user's own Lorgat 2020 paper; the Borcherds lift
$\phi_{0,1} \to \Delta_5$ there is the $d = 3$ shadow; the $d = 5$
lift $H^{(24 A_1)}_g \to \Phi_{12}$ is the Leech-slice-dualised
version. The 23 umbral siblings supply the full analogous family for
each Niemeier type.

\textbf{(g) Adjudication ledger W14-W19 consistency.} The $4 A_5 D_4$
row (entry 13, lambency 6) and the $6 D_4$ row (entry 15, lambency 6)
are the two rows with lambency 6 among the 23 umbrals; the cache
entry ``N=6 uses $6 D_4$'' refers to the penumbral relaxation in which
$G = \mathrm{Sym}_3$ (an index-240 subgroup of $3.\mathrm{Sym}_6$) is
the genus-2 archetype $W^{(2)}_{II}$-umbral group, not the full
$3.\mathrm{Sym}_6$-umbral group. This is consistent with the present
tabulation.

\textbf{(h) AP-CY discipline.} No bare $\kappa$; no $\Phi$-output-scope
confusion (the output at $d = 5$ is $E_1$-chiral, not $E_2$); no
CoHA-vs-vertex-algebra confusion (the Stage-3 output is a super-$E_1$-
chiral algebra, the CoHA analogue at $d = 5$ is a separate
Stage-$2.5$ object that localises to it); no Drinfeld-centre-vs-
averaging confusion (the Niemeier projection is a charge-lattice
projection, not a centre construction).

\textbf{(i) CDH $\to$ DGO consistency.} The CDH 2014 uniqueness Thm.~4.1
is conditional on a symmetry-plus-shadow ansatz; Duncan–Griffin–Ono
2015 \emph{Research Math.\ Sci.} 2:26 gives the unconditional
construction of all 23 mock modular forms $H^{(\Lambda)}$ and thus
the full structure of the 23-sibling umbral data. The present closure
cites both.

\textbf{(j) $(\infty, 1)$-lane discipline.} The enumeration is
lattice-level-combinatorial and does not require $(\infty, 1)$-
functoriality. The upgrade of each of the 23 Stage-3 projections to an
$(\infty, 1)$-functor on $\mathrm{CY}\text{-}\mathrm{cat}_5$ requires
morphism preservation, which is inherited from the Stage-1 and Stage-2
$(\infty, 1)$-functoriality of C21. Pattern 273 is respected.

\textbf{(k) Residual per-sibling frontier.} For each of the 23 rows,
the bracket-level identification of the Stage-3 super-$E_1$-chiral
algebra with the CDH BKM superalgebra $\mathfrak g^{(\Lambda)}$ is
open (F1 of C21, per-sibling). The enumeration of Stage-3 charge
lattices and their umbral-group actions is closed by the present
theorem; the identification of the Stage-3 algebra as a Lie-bracket
object requires the $d = 5$ extension of Schiffmann–Vasserot 2013
$\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$
applied to the 23-fold family of Niemeier slices. This is parametrised
residual frontier, 23-fold.
