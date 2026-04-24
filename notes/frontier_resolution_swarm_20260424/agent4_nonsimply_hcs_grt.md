# Agent 4: non-simply-laced 5d hCS and GRT_1

## Verdict

Undecidable on the present chain-level evidence.

The scoped material proves neither a nonzero pure-gauge four-loop
obstruction nor an explicit GRT_1-twisted nullhomotopy.  The existing
candidate omega_4 is a target cochain.  It becomes a theorem only after
the lacing-decorated four-loop boundary matrix, the graph-to-BV chain
map, and either a nonzero detector or a GRT_1-twisted nullhomotopy are
constructed.

## Claim attacked

Claim: non-simply-laced 5d holomorphic Chern--Simons on R_t x C^2
fails at four loops for g = G_2, or else admits a GRT_1-twisted
resolution.

Failure mode: the manuscript had a candidate Dynkin-twisted graph
cochain with numerical coefficients, but no constructed complex-level
differential, no graph-to-BV chain map, no detector alpha_4, and no
twisted GRT_1 action rho_tw producing a nullhomotopy.

## Local anchors

- `chapters/theory/quantum_groups_foundations.tex:6952` defines the
  lacing-decorated four-loop BV deformation complex.
- `chapters/theory/quantum_groups_foundations.tex:7028` restates
  omega_4(G_2) as a conditional obstruction target, not a proved class.
- `chapters/theory/quantum_groups_foundations.tex:7101` states the
  missing finite computation and the two linear systems.
- `chapters/theory/e1_chiral_algebras.tex:3302` blocks the resurgent
  split-Stokes data from being read as a four-loop hCS nullhomotopy.
- `chapters/theory/en_factorization.tex:2069` blocks untwisted GRT_1
  invariance from being read as an action on the lacing-decorated
  hCS complex before rho_tw is constructed.
- `compute/tests/test_resurgent_twist_non_simply_laced.py:5`,
  `compute/tests/test_zte_deformation_cohomology.py:7`,
  `compute/tests/test_zte_t_matrix_exact.py:5`, and
  `compute/tests/test_costello_5d_verification.py:6` state that those
  test suites do not decide the four-loop hCS/GRT_1 question.

## Exact deformation complex

The complex is
`Def^{tw}_{5d}(g) = prod_{L,m >= 0} hbar^L O_loc^m(E_g)^g
hat tensor Gra^{tw}_{L,m}(g)`, where
`E_g = Omega^*(R_t) hat tensor Omega^{0,*}(C^2) tensor g[1]`.

The differential is
`D_tw = d_BV + partial_split^{tw} + hbar Delta_BV`, with
`d_BV = (bar partial_{C^2} + d_t) + {S_cl,-}_BV` and
`partial_split^{tw}` weighted by the symmetrised Cartan pairing
`kappa_Dyn(g)_{ij} = ((alpha_i,alpha_i)/2) a_ij`.

For a three-loop solution `I_{<=3}`, the four-loop obstruction
representative is
`o_4(g) = Delta_BV I_3 + 1/2({I_1,I_3}+{I_2,I_2}+{I_3,I_1})_BV`
in `F^4 Def^{tw,1}_{5d}(g)/F^5`.

A GRT_1-twisted resolution is a pair `(tau_4,H_4)` satisfying
`(D_tw + rho_tw(tau_4)) H_4 = o_4(g)`.

## First missing computation

Compute the finite matrix of `partial_split^{tw}` on the ordered
four-loop basis
`{wheel_4, prism, cube, octahedron, K_4, peripheral} tensor
{long,short}^{E(Gamma)}` for G_2, then apply the Costello graph-to-BV
realisation and solve:

1. `D_tw H = omega_4(G_2)`;
2. `(D_tw + rho_tw(tau)) H = omega_4(G_2)`, with
   `tau in grt_1`.

If both systems fail and a constructed detector alpha_4 is nonzero on
the cokernel, the obstruction is proved.  If the second system has a
solution, the GRT_1-twisted nullhomotopy is constructed.

## Tests run

`python3 -m pytest compute/tests/test_resurgent_twist_non_simply_laced.py compute/tests/test_zte_deformation_cohomology.py compute/tests/test_zte_t_matrix_exact.py compute/tests/test_costello_5d_verification.py`

Result: 251 passed in 50.76s.

## Files changed

- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/theory/e1_chiral_algebras.tex`
- `chapters/theory/en_factorization.tex`
- `compute/tests/test_resurgent_twist_non_simply_laced.py`
- `compute/tests/test_zte_deformation_cohomology.py`
- `compute/tests/test_zte_t_matrix_exact.py`
- `compute/tests/test_costello_5d_verification.py`
- `notes/frontier_resolution_swarm_20260424/agent4_nonsimply_hcs_grt.md`

## Remaining open questions

1. Construct `rho_tw: grt_1 -> End(Def^{tw}_{5d}(g))`.
2. Compute the four-loop lacing-decorated boundary matrix for G_2.
3. Construct the graph-to-BV chain map in the twisted complex.
4. Either build alpha_4 as a theorem-grade detector or solve the
   GRT_1-twisted nullhomotopy equation.
