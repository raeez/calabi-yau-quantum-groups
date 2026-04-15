#!/bin/bash
# ==========================================================================
# CACHE INJECTION — PreToolUse hook for ALL Agent launches
# ==========================================================================
# UNCONDITIONAL. Every agent. No exceptions. No keyword filter.
# Injects: full /investigate protocol, cache write-back mandate,
# top confusion types, file paths for cache writes.
# ==========================================================================

cat <<'HOOKEOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "MANDATORY FIRST-PRINCIPLES PROTOCOL (injected by cache-injection hook, applies to ALL agents):\n\nYou MUST follow this protocol for EVERY confusion, mistake, error, inconsistency, or wrong claim you encounter:\n\n## STEP 1: INVESTIGATE FROM FIRST PRINCIPLES\nFor each issue found, answer ALL THREE:\n(a) What does the claim get RIGHT? (the ghost of a true theorem)\n(b) What does it get WRONG? (the precise conflation or error)\n(c) What is the CORRECT mathematical relationship?\n\n## STEP 2: FIX WITH SUBSTANCE\nEvery correction MUST contain actual mathematics — a remark, a factorization, an adjunction, a construction. NO shallow term swaps. If you replace 'X is Y' with 'X is Z', you must explain WHY Z is correct and HOW X and Z are related.\n\n## STEP 3: WRITE TO CACHE\nIf you find ANY new confusion pattern, or if any pattern appears 2+ times, you MUST append a new entry to the cache file:\n  File: appendices/first_principles_cache.md\n  Format: | # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |\nUse the Edit tool to append to the end of the file. This is NOT optional.\n\n## TOP 15 CACHED CONFUSIONS (check ALL claims against these):\n1. specific/general: toric result applied to all CY (SN vanishing, Omega-bg, kappa=c/2)\n2. label/content: bare kappa (AP113), bare 'ordered' (AP152), bare 'Hochschild' (AP160)\n3. native/derived: E_n on wrong object. d>=3: A is E_1, E_2 on Z(Rep(A)) only\n4. construction/narration: 'X gives Y' needs explicit arrow (AP-CY57)\n5. algebra/coalgebra: CoHA != bar complex (algebra vs coalgebra)\n6. CoHA != chiral: CoHA is associative, not a vertex algebra (AP-CY7)\n7. Drinfeld center != averaging: center is right adjoint to forgetful (AP-CY54)\n8. scope: CY-B d-dependent (AP-CY58). Phi output d-dependent (FM43)\n9. AP-CY8: denominator=bar Euler needs BOTH CY-A AND Vol I anchor\n10. CY-C CONJECTURAL. G(X) unconstructed. Super-Yangian CONJECTURAL\n11. convention: two hbar without bridge = disaster (AP151)\n12. mechanism: N_{C/Y} -> spectral params needs Omega intermediary (AP-CY20)\n13. chain/cohom: class M E_3 bar = 6^g (cohom), NOT infinite\n14. part/whole: {b_k,B2}=0 per-k FALSE; only total vanishes\n15. coincidence: kappa_BKM = kappa_ch + chi(O_fiber) is N=1 COINCIDENCE\n\nKEY FACTS:\n- kappa_cat(K3xE) = 0 (total space), NOT 2 (fiber)\n- CoHA(C^3) = Y^+ (positive half), NOT W_{1+inf} (full Yangian)\n- Six routes to G(K3xE) are six DIFFERENT constructions, NOT six Phi applications\n- Phi gives ONE output per category. Different kappas from DIFFERENT constructions."
  }
}
HOOKEOF
