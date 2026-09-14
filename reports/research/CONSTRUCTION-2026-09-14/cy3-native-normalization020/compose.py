from pathlib import Path
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/cy3-native-normalization020/source'
assert not (R/'source-freeze.json').exists()
p=S/'research-candidates/critical-hall-two-nonzero-blocks/two_nonzero_blocks.tex'
t=p.read_text();needle=r'\section{Four distinct eigenvalues and the geometric boundary}'
assert t.count(needle)==1
bridge=r'''\section{Polarizations and the sign of a flag sheet}
\label{ts22:sec:normalization}

A complex orientation of an incidence normal bundle fixes its Thom map.
Its coefficient in vanishing-cycle generators also depends on their
polarization. One eigenline pair determines this dependence.
Rescale a nonzero eigenvalue difference in the $C$ coordinates and write
\[
 q=b_{ij}c_{ji}-b_{ji}c_{ij},\qquad i<j.
\]
The two positive real disks, with their complex parameter orientations, are
\[
\begin{array}{c|cccc}
 &b_{ij}&b_{ji}&c_{ij}&c_{ji}\\ \hline
 D_B&(u)&v&-\bar v&\bar u\\
 D_+&p&-\bar t&t&\bar p.
\end{array}
\]
Here $(u,v)$ and $(p,t)$ range over small balls in $\C^2$.
The restrictions of $q$ are $|u|^2+|v|^2$ and $|p|^2+|t|^2$.
Their spheres retract the positive Milnor fibre. The $B$-polarization
uses $(b_{ij},b_{ji})$. The upper-$(B,C)$ polarization uses
$(b_{ij},c_{ij})$. These are maximal isotropic complex planes.

Both generators use the same support and cone convention.
Put $P_q=\{\Re q\le0\}$. Restriction to either positive disk
identifies the degree-four support group at the origin with
$H^4(D,D\setminus\{0\};\Q)$. Define its generator to be the
positive relative Thom class of that oriented disk.
This also specifies its sign in $\Phi_q=\Fib(i^*\to\psi_q)$.
Indeed, the fibre differential is
$d(a,b)=(da,a|_{F_q}-db)$.
If $\alpha$ is the positive angular class on the Milnor sphere,
the positive relative class is represented by $(0,-\alpha)$.
To check the sign, extend $\alpha$ to a cochain $\beta$ on a disk
with $d\beta$ a positive relative Thom representative.
Then $(d\beta,0)-d(\beta,0)=(0,-\alpha)$ on the pair.
Thus the support generator and its cone representative have a fixed
comparison. No independent sign is assigned to the nearby-cycle term.

On a product of positive disks, the external support product is the
product of relative Thom classes. Their degrees are even.
The inclusion $P_q\times P_{q'}\subset P_{q+q'}$ restricts to the
identity on the relative product disk, with support at its origin.
Rounding its corners preserves its orientation. Hence
$\TS_{q,q'}$ sends the ordered product generator to the generator
of the sum. This verifies the normalization for the actual support
morphism of Lemma~\ref{ts22:lem:support-product}.

The change of parameters between the displayed disks is
$(p,t)=(u,-\bar v)$. Its real determinant is $-1$.
Thus the upper-$(B,C)$ generator is minus the $B$ generator.
The incidence has lower normal coordinates $(b_{ji},c_{ji})$.
Their projections from the disks are
\[
 D_B:\ (u,v)\longmapsto(v,\bar u),\qquad
 D_+:\ (p,t)\longmapsto(-\bar t,\bar p).
\]
The first has real determinant $-1$, and the second has determinant
$+1$. Radial normalization gives the same degrees on the spheres.
Pullback of the positive complex normal Thom class therefore gives
minus the $B$ generator and plus the upper-$(B,C)$ generator.

For a matrix with $n$ distinct eigenvalues, denote the product of
these $B$ generators by $u_n$. Include the free coordinates and
shift $[2n^2]$, so $u_n$ trivializes $\cP_n=\Q[2n]$.
Put $u_1=1$ in $\Phi_0\Q[2]=\Q[2]$.
There are $\binom n2$ eigenline pairs. The upper-$(B,C)$ product
therefore defines
\[
 e_n=\epsilon_nu_n,\qquad
 \epsilon_n=(-1)^{\binom n2},\qquad
 (\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4,\epsilon_5)
       =(1,-1,-1,1,1).
\]
This definition applies to the ranks through five used below.

\begin{proposition}[Coefficients in the two polarizations]
\label{ts22:prop:normalization}
For each coefficient map $\mu_{d,e}$ constructed in these two chapters,
its restriction to the distinct-eigenvalue locus has coefficient
$(-1)^{de}$ on every flag sheet in the $u$ generators.
In the $e$ generators every sheet has coefficient $+1$.
The two statements describe the same derived morphism.
\end{proposition}

\begin{proof}
Order the eigenlines by the submodule and then the quotient.
The normal quadratic decomposes into internal pairs and $de$ cross pairs.
The support product preserves the ordered internal generators by the
relative-disk calculation above. For each cross pair, the lower $A$
normal cancels the flag tangent under flag integration: the derivative
of the preservation equation in that tangent is multiplication by the
nonzero eigenvalue difference. This is a complex linear isomorphism
and has positive real determinant. The remaining normal map is exactly
the projection to $(b_{ji},c_{ji})$ calculated above.
It contributes $-1$ in the $B$ polarization.
The product of all cross contributions is $(-1)^{de}$.
All involved Thom degrees are even, so regrouping introduces no sign.

The input change of generators is $\epsilon_d\epsilon_e$, whereas
the output change is $\epsilon_{d+e}$. The identity
\[
 \binom{d+e}{2}=\binom d2+\binom e2+de
\]
therefore makes the coefficient in the $e$ generators
$\epsilon_d\epsilon_e(-1)^{de}/\epsilon_{d+e}=1$.
Neither the complex Thom map nor the support morphism has changed.
\end{proof}

For a flag with successive dimensions $(d_1,d_2,d_3)$, the number
of cross pairs is $N=d_1d_2+d_1d_3+d_2d_3$.
The two factorizations give the same exponent because
\[
 d_1d_2+(d_1+d_2)d_3=d_2d_3+d_1(d_2+d_3)=N.
\]
For $(2,1,1)$, $N=5$. Its two sign products are
$(+1)(-1)=(-1)(+1)=-1$. Its invariant constant vector therefore
maps to $-12u_4$ in $u$ coordinates and to $12e_4$ in $e$ coordinates.
The input vectors differ by $\epsilon_2\epsilon_1^2=-1$.
For $(2,2,1)$, $N=8$ and both sign products are $+1$.
Its trace is $+30$ in either convention, since
$\epsilon_2^2\epsilon_1=\epsilon_5=1$.
These changes of coordinates preserve both derived associativity
identities, including their intermediate coefficient maps.

'''
t=t.replace(needle,bridge+needle)
a=t.index('The real normal orientations can be fixed')
b=t.index('\nThere are six invariant planes',a)
t=t[:a]+r'''Use the generators $e_n$ of Section~\ref{ts22:sec:normalization}.
They use the upper-$(B,C)$ polarization in each eigenline pair.
The support product carries the product normal generator to that
of their sum, by the product of relative normal disks.
'''+t[b:]
a=t.index('At any such plane the normal incidence')
b=t.index('\nFor flags of type $(2,1,1)$',a)
t=t[:a]+r'''At any such plane the normal incidence is a
maximal isotropic subspace in the complementary hyperbolic directions.
Proposition~\ref{ts22:prop:normalization} gives coefficient $+1$
for each sheet in the $e$ generators. In the $u$ generators the
coefficient is also $+1$, since there are four cross pairs.
The $B$-polarized complex orientation is invariant under changes
of eigenbasis, and $e_n=\epsilon_nu_n$ retains that invariance.
Hence $\mu_{2,2}$ is the sum of these six sheet coefficients.
'''+t[b:]
t=t.replace('same sum on twelve coordinates, giving $4\\cdot3=6\\cdot2=12$ on\nthe invariant constant class.','same sum on twelve $e$ coordinates, giving $4\\cdot3=6\\cdot2=12$ on\nthe invariant constant class. In $u$ coordinates both maps are minus\nthe sheet sum, giving $-12$, as calculated in\nProposition~\\ref{ts22:prop:normalization}.')
p.write_text(t)
p=S/'research-candidates/cy3-flag221019/flag221.tex';t=p.read_text()
t=t.replace('The trivialization uses the complex orientation of the paired\n$B,C$ normal directions and is compatible with conjugation.','The trivialization $u_n$ uses the complex orientation of the\nmaximal isotropic $B$ normal bundle and is compatible with conjugation.\nThe generators $e_n=\\epsilon_nu_n$, with\n$\\epsilon_n=(-1)^{\\binom n2}$, define a second trivialization.')
t=t.replace('The maximal isotropic $B$ directions have their complex orientation.','The maximal isotropic $B$ directions have their complex orientation.\nUse their positive relative Thom class and its cone representative\nas in Section~\\ref{ts22:sec:normalization}.')
needle='\nWhen $A$ has five distinct eigenvalues, there are ten pairs of'
assert t.count(needle)==1
descent=r'''
The comparison extends across the entire cyclic locus, including
nondiagonalizable matrices. The quotient of the $B$ bundle by the
centralizer bundle is a complex vector bundle of rank $n^2-n$.
Its dual is paired by $\Tr(B[C,A])$ with the corresponding $C$ quotient.
Local complements form affine spaces, and Hermitian metrics form
contractible spaces. They give the positive disks used to define $u_n$.
Complex frame changes preserve their orientations and their relative
Thom classes. Thus the disk generators agree on overlaps and on
all levels of the conjugation action diagram.
Multiplication by the constant $\epsilon_n$ gives $e_n$ on that
same whole diagram. It requires no eigenline splitting at a collision.

Both trivializations respect potential monodromy. For a quadratic
in $2r$ variables, continuation once around zero induces the antipodal
map on $S^{2r-1}$, of degree $(-1)^{2r}=1$.
The zero-potential case $n=1$ has identity monodromy directly.
More generally the scalar automorphism $\epsilon_n1_{\cP_n}$
commutes with all continuation maps of the entire coefficient complex.

For any analytic family pulled back from the cyclic locus, the
central-restriction-to-nearby-cycles map commutes with these constant
scalar changes. On an ordered flag family with cyclic constituents,
the incoming scalar is the product of the constituent scalars.
The outgoing scalar is that of their total rank. Proper direct image
and the coefficient map retain this comparison. Consequently the
$u$ and $e$ descriptions give conjugate diagrams of actual sheaf maps
at both regular and singular fibres. Vanishing cycles remain the
pullback of the ambient coefficient complex.
'''
t=t.replace(needle,'\n'+descent+needle)
a=t.index('For each flag the complementary normal\nquadratic is hyperbolic.')
b=t.index('\nThere are $\\binom54',a)
t=t[:a]+r'''For each flag the complementary normal
quadratic has eight cross-eigenline pairs. Each lower-normal
projection has degree $-1$ in the $B$ polarization, so their product
has degree $(-1)^8=1$. Proposition~\ref{ts22:prop:normalization}
therefore gives coefficient $+1$ for each flag sheet in the $u$
trivializations of Lemma~\ref{fl221:lem:cyclic}.
The $e$ trivializations give the same coefficient because the incoming
change is $\epsilon_2^2\epsilon_1=1$ and the outgoing change is
$\epsilon_5=1$.
'''+t[b:]
t=t.replace('Permuting\neigenlines exchanges pairs of hyperbolic factors, giving sign\n$+1$. This computation fixes the regular trace normalization.','Conjugation invariance of\n$u_n$ and $e_n$ makes this description independent of the eigenbasis.\nThus the trace normalization is the same in both specified conventions.')
# Preserve complete collision gluing proof, adding the generator identification immediately before it.
needle='\\begin{proposition}[Coefficient specialization at the collision]'
t=t.replace(needle,r'''For this family the input and output $u$ and $e$ trivializations agree:
$e_2\boxtimes e_2\boxtimes e_1=u_2\boxtimes u_2\boxtimes u_1$
and $e_5=u_5$. This equality holds over the central point as well,
by the cyclic construction above. The following trace uses these
identical trivializations.

'''+needle)
p.write_text(t)
# Explicit normalizations at both native consumers and the focused consumer.
consumer=r'''The regular traces use the generators $e_n$ of
Proposition~\ref{ts22:prop:normalization}. Relative to the cyclic
$B$-polarized generators $u_n$, they satisfy
$e_n=(-1)^{\binom n2}u_n$. The $(2,1,1)$ trace is $+12$ in $e$
coordinates and $-12$ in $u$ coordinates; the $(2,2,1)$ trace is
$+30$ in both. These are coordinates of the same coefficient maps.
'''
p=S/'platonic/chapters/hall_coefficient_maps.tex';t=p.read_text();t+='\n'+consumer;p.write_text(t)
p=S/'platonic/chapters/Volume_IV_Calabi_Yau_Quantum_Groups.tex';t=p.read_text();needle='The correspondence displayed here orders the quotient before the';assert t.count(needle)==1;t=t.replace(needle,consumer+'\n'+needle);p.write_text(t)
print('Composed normalization proof and four consumer source edits')

p=S/'platonic/chapters/Volume_IV_Calabi_Yau_Quantum_Groups.tex';t=p.read_text();needle='These are coordinates of the same coefficient maps.\n';assert t.count(needle)==1;t=t.replace(needle,needle+'The separated rank-two coordinates $(b_{12},c_{12})$ in\nEquation~\\ref{eq:c3-separated-quadratic} use this same upper polarization.\n');p.write_text(t)
