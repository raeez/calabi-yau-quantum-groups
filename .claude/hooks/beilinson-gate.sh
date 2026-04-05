#!/bin/bash
# ==========================================================================
# BEILINSON GATE — Vol III PostToolUse hook for Edit|Write
# ==========================================================================
# Comprehensive enforcement: shared AP checks (from Vol I) + Vol III-specific
# (AP-CY1 through AP-CY8). All fixes from RED audit applied.
# ==========================================================================

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  *.tex|*.py) ;;
  *) exit 0 ;;
esac

ISSUES=""
WARNINGS=""

if [[ "$FILE_PATH" == *.tex ]]; then

  # === SHARED CHECKS (same as Vol I, propagated to prevent drift) ===

  # --- AP24: Unqualified kappa+kappa'=0 ---
  if grep -q 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" | grep -v 'Kac--Moody\|Kac-Moody\|free.field\|self-contragredient\|lattice\|principal\|Heisenberg\|affine' | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP24: Possibly unqualified kappa+kappa'=0. For Virasoro: =13, NOT 0. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP25/AP34: bar != Verdier != cobar ---
  if grep -qi 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|cobar.*Koszul dual' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|cobar.*Koszul dual' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP25/AP34: Omega(B(A))=A (inversion), NOT bulk. D_Ran(B(A))=B(A!) (Verdier). Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP40: Environment/tag mismatch (uses printf, not echo) ---
  if grep -q 'ClaimStatusConjectured' "$FILE_PATH" 2>/dev/null; then
    CONJ_LINES=$(grep -n 'ClaimStatusConjectured' "$FILE_PATH" | cut -d: -f1)
    for LINE in $CONJ_LINES; do
      START=$((LINE - 10))
      [ $START -lt 1 ] && START=1
      CONTEXT=$(sed -n "${START},${LINE}p" "$FILE_PATH")
      if printf '%s\n' "$CONTEXT" | grep -q 'begin{theorem}\|begin{proposition}\|begin{lemma}\|begin{corollary}'; then
        ISSUES="${ISSUES}AP40: ClaimStatusConjectured in proof-bearing environment near line ${LINE}.\n"
        break
      fi
    done
  fi

  # === VOL III-SPECIFIC CHECKS ===

  # --- AP-CY6: A_X for CY3 does NOT exist ---
  if grep -qi 'A_X.*CY3\|chiral algebra.*CY.*3\|A_{CY_3}' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'A_X.*CY3\|chiral algebra.*CY.*3\|A_{CY_3}' "$FILE_PATH" | grep -v 'conditional\|conjectural\|if.*exists\|programme\|target\|conjecture' | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP-CY6: A_X for CY3 does NOT exist yet. CY-A proved only for d=2. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP-CY7: CoHA != E1-chiral algebra ---
  if grep -qi 'CoHA.*is.*E_1\|CoHA.*=.*E_1\|CoHA.*chiral algebra' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'CoHA.*is.*E_1\|CoHA.*=.*E_1\|CoHA.*chiral algebra' "$FILE_PATH" | grep -v 'target\|should match\|conjecture\|if.*exists' | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP-CY7: CoHA is associative, NOT E1-chiral. Requires G(X) existence. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP43: G(X) used without definition ---
  if grep -qi 'G(X)\|quantum vertex chiral group' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'G(X)\|quantum vertex chiral group' "$FILE_PATH" | grep -v 'Conjecture\|conjecture\|if.*exists\|formal definition\|begin{definition}' | head -3)
    if [ -n "$MATCHES" ]; then
      WARNINGS="${WARNINGS}AP43: G(X) used without formal definition. Must have begin{definition} before use. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP49: Cross-volume convention reference ---
  if grep -qi 'Vol.*I\|Vol.*II\|chiral-bar-cobar' "$FILE_PATH" 2>/dev/null; then
    WARNINGS="${WARNINGS}AP49: Cross-volume reference. Vol III uses motivic/categorical conventions. Verify compatibility before citing Vol I/II formulas.\n"
  fi

  # --- PROSE ---
  for WORD in notably crucially remarkably interestingly importantly furthermore moreover additionally delve leverage utilize underscore facilitate pivotal nuanced intricate streamline tapestry multifaceted cornerstone; do
    if grep -qi "\\b${WORD}\\b" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "\\b${WORD}\\b" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: '${WORD}'. Line: ${LINE}\n"
    fi
  done

  for PHRASE in "it is worth noting" "having established" "we now turn to" "in this section we" "as we shall see" "let us now" "we proceed to" "the key insight is" "it turns out that" "this brings us to" "with this in hand"; do
    if grep -qi "$PHRASE" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "$PHRASE" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: Signpost '${PHRASE}'. Line: ${LINE}\n"
    fi
  done
fi

# ---------------------------------------------------------------------------
# SECTION 2: COMPUTE LAYER CHECKS (for .py files)
# ---------------------------------------------------------------------------
if [[ "$FILE_PATH" == *.py ]]; then
  if grep -q 'assert.*==' "$FILE_PATH" 2>/dev/null; then
    HARDCODED=$(grep -c 'assert.*==.*[0-9]' "$FILE_PATH" 2>/dev/null)
    CROSSCHECK=$(grep -c 'assert.*approx\|assert.*close\|verify_.*path\|cross_check\|independent' "$FILE_PATH" 2>/dev/null)
    if [ "$HARDCODED" -gt 5 ] && [ "$CROSSCHECK" -lt 2 ]; then
      WARNINGS="${WARNINGS}AP10: ${HARDCODED} hardcoded assertions but only ${CROSSCHECK} cross-checks. Add multi-path verification.\n"
    fi
  fi
fi

# ---------------------------------------------------------------------------
# SECTION 3: BUILD DISCIPLINE
# ---------------------------------------------------------------------------
COUNTER_FILE="/tmp/claude_beilinson_edit_count_vol3"
COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

BUILD_REMINDER=""
if (( COUNT % 5 == 0 )); then
  BUILD_REMINDER="BUILD: ${COUNT} edits. Run: pkill -9 -f pdflatex; sleep 2; cd ~/calabi-yau-quantum-groups && make fast"
fi

# ---------------------------------------------------------------------------
# SECTION 4: CROSS-VOLUME PROPAGATION
# ---------------------------------------------------------------------------
PROPAGATION=""
if [[ "$FILE_PATH" == *.tex ]]; then
  NEW_CONTENT=$(echo "$INPUT" | jq -r '(.tool_input.new_string // .tool_input.content) // empty' 2>/dev/null)
  if echo "$NEW_CONTENT" | grep -q '\\kappa\|\\Theta\|CY.*functor\|E_2.*chiral\|CoHA\|Borcherds\|quantum.*group' 2>/dev/null; then
    PROPAGATION="AP5/AP49: Formula edit. Grep ALL THREE volumes. Convention: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic/categorical."
  fi
fi

# ---------------------------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------------------------
CONTEXT=""
[ -n "$ISSUES" ] && CONTEXT="${CONTEXT}VIOLATIONS:\n${ISSUES}\n"
[ -n "$WARNINGS" ] && CONTEXT="${CONTEXT}WARNINGS:\n${WARNINGS}\n"
[ -n "$BUILD_REMINDER" ] && CONTEXT="${CONTEXT}${BUILD_REMINDER}\n"
[ -n "$PROPAGATION" ] && CONTEXT="${CONTEXT}${PROPAGATION}\n"

if [ -n "$CONTEXT" ]; then
  jq -n --arg ctx "$CONTEXT" '{
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": $ctx
    }
  }'
fi

exit 0
