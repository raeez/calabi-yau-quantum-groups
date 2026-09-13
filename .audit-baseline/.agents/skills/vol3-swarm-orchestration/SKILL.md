---
name: vol3-swarm-orchestration
description: Codex-native analogue of the Claude-side swarm routines such as research-swarm, Beilinson-swarm, and rectify-all. Use only when the user explicitly authorizes sub-agents, delegation, or parallel agent work.
---

# Vol III Swarm Orchestration

This skill exists for parity with Claude-side swarm routines, but Codex may use it only when the user explicitly authorizes delegation.

## Modes

- `research-swarm`: split frontier questions by independent mathematical axes
- `beilinson-swarm`: split rectification by disjoint chapter/theorem surfaces
- `rectify-all`: split large cross-volume cleanup by independent write scopes after a local root audit

## Rules

1. Keep the immediate blocking task local unless delegation truly removes idle time.
2. Give each worker a disjoint write scope.
3. Tell workers they are not alone in the tree and must not revert others' work.
4. Do not duplicate unresolved work across workers.
5. Use one local integration pass after workers return.
6. End with:
   - what each worker owned
   - what verification ran
   - what remains pending

## Default when delegation is not authorized

Run the same logical workflow locally with:

- `vol3-beilinson-loop`
- `vol3-chriss-ginzburg-rectification`
- `vol3-claim-verification`
- `vol3-cross-volume-propagation`
- `vol3-frontier-research`
