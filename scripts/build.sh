#!/bin/bash
# Converging build script for pdflatex manuscripts.
# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
#
# BUILD ISOLATION
# ───────────────
# Each invocation builds in its own /tmp directory, controlled by:
#
#   MKD_BUILD_NS   Namespace identifier.  All builds sharing the same NS
#                  reuse the same /tmp directory (warm .aux files → faster
#                  convergence on subsequent runs).
#
#                  • Set per-agent:  export MKD_BUILD_NS="agent-$$"
#                                    make fast   # warm on second call
#                  • Unset:          each invocation gets a fresh directory
#                                    (cold start every time — safe default)
#
# The build dir is /tmp/mkd-<volume>-<NS>/ where <volume> is derived from
# the repo directory name.  No file-system lock needed; parallel builds
# with different NS values never touch the same files.
#
# Cleanup:  build dirs persist until reboot or `make clean-builds`.

set -euo pipefail

SRC_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SRC_DIR"

MAX_PASSES=${1:-7}
TEX="pdflatex"
TEXFLAGS="-interaction=batchmode -file-line-error -synctex=0 -cnf-line=buf_size=1000000 -cnf-line=stack_size=20000 -cnf-line=max_print_line=10000"
LOG_DIR="$SRC_DIR/.build_logs"

mkdir -p "$LOG_DIR"

# ---------------------------------------------------------------------------
# Build namespace → isolated /tmp directory
# ---------------------------------------------------------------------------
VOLUME_TAG="$(basename "$SRC_DIR")"
if [ -n "${MKD_BUILD_NS:-}" ]; then
    BUILD_NS="$MKD_BUILD_NS"
else
    # Fresh namespace per invocation (cold start).
    BUILD_NS="$(date +%Y%m%d%H%M%S)-$$"
fi
BUILD_DIR="/tmp/mkd-${VOLUME_TAG}-${BUILD_NS}"

# Create or reuse the build directory.
if [ -d "$BUILD_DIR" ]; then
    echo "Reusing build dir: $BUILD_DIR"
else
    echo "Creating build dir: $BUILD_DIR"
    mkdir -p "$BUILD_DIR"
fi

# Mirror every directory that contains .tex files so \include .aux files
# land in the right place (pdflatex writes them relative to -output-directory).
(cd "$SRC_DIR" && find . -name '*.tex' -exec dirname {} \; 2>/dev/null) \
    | sort -u | while read -r d; do
    mkdir -p "$BUILD_DIR/$d"
done

# TEXINPUTS: search build dir first (for .aux cross-refs), then source dir.
export TEXINPUTS="$BUILD_DIR:$SRC_DIR:"

RUN_LOG="$LOG_DIR/tex-build.stdout.log"
TEX_FILE_LINE_PREFIX='^(/|\./)?[^[:space:]]+\.(tex|sty|cls):[0-9]+:'
TEX_ERROR_SIGNATURE='Undefined control sequence|LaTeX Error:|Package [^[:space:]]+ Error:|Class [^[:space:]]+ Error:|Double (subscript|superscript)|Emergency stop|Runaway argument|Fatal error|File ended while scanning|Missing \$ inserted|No pages of output'
TEX_ERROR_PATTERN="^! |${TEX_FILE_LINE_PREFIX}.*(${TEX_ERROR_SIGNATURE})|${TEX_ERROR_SIGNATURE}"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
count_matches() {
    local pattern=$1
    local file=$2
    local count
    count=$(grep -aEc "$pattern" "$file" 2>/dev/null || true)
    count=${count##*$'\n'}
    if [ -z "$count" ]; then
        count=0
    fi
    printf '%s\n' "$count"
}

show_failure_summary() {
    local logfile="$BUILD_DIR/main.log"
    echo "✗ Build failed."
    echo "  Build dir: $BUILD_DIR"
    echo "  Logs: $RUN_LOG and $logfile"
    if [ -f "$logfile" ]; then
        grep -aE "$TEX_ERROR_PATTERN" "$logfile" | head -n 20 || true
    elif [ -f "$RUN_LOG" ]; then
        tail -n 40 "$RUN_LOG" || true
    fi
}

log_has_tex_errors() {
    local logfile=$1
    grep -aEq "$TEX_ERROR_PATTERN" "$logfile"
}

require_clean_tex_pass() {
    local tex_rc=$1
    local logfile=$2

    if [ "$tex_rc" -ne 0 ]; then
        echo "  pdflatex exited with status $tex_rc."
        show_failure_summary
        exit "$tex_rc"
    fi

    if log_has_tex_errors "$logfile"; then
        echo "  TeX error marker found in the final pass log."
        show_failure_summary
        exit 1
    fi
}

publish_pdf() {
    local logfile=$1

    # Recheck the final log at the publication boundary.  A PDF artifact or an
    # "Output written" marker can survive a failed pass; neither proves that
    # the TeX pass succeeded.
    if log_has_tex_errors "$logfile"; then
        echo "  TeX error marker found in the final pass log."
        show_failure_summary
        exit 1
    fi
    if [ ! -f "$BUILD_DIR/main.pdf" ]; then
        echo "  No PDF produced by the successful TeX pass."
        show_failure_summary
        exit 1
    fi

    mkdir -p "$SRC_DIR/out"
    cp "$BUILD_DIR/main.pdf" "$SRC_DIR/out/main.pdf"
    cp "$logfile" "$SRC_DIR/out/main.log" 2>/dev/null || true
}

# ---------------------------------------------------------------------------
# Build loop
# ---------------------------------------------------------------------------
echo "Building main.tex (up to $MAX_PASSES passes) [NS=$BUILD_NS]"
prev_stats=""
for i in $(seq 1 $MAX_PASSES); do
    echo "── Pass $i / $MAX_PASSES ──"
    : > "$RUN_LOG"
    set +e
    $TEX $TEXFLAGS -output-directory="$BUILD_DIR" main.tex >"$RUN_LOG" 2>&1
    tex_rc=$?
    set -e

    if [ -f "$BUILD_DIR/main.idx" ]; then
        makeindex -q "$BUILD_DIR/main.idx" 2>/dev/null || true
    fi

    logfile="$BUILD_DIR/main.log"

    if [ ! -f "$logfile" ]; then
        echo "  No log file produced — pdflatex may have crashed."
        show_failure_summary
        exit 1
    fi

    require_clean_tex_pass "$tex_rc" "$logfile"

    cit=$(count_matches 'Citation.*undefined' "$logfile")
    ref=$(count_matches 'Reference.*undefined' "$logfile")
    rerun=$(count_matches 'Label\(s\) may have changed|Package rerunfilecheck Warning' "$logfile")
    overfull=$(count_matches 'Overfull \\hbox' "$logfile")
    underfull=$(count_matches 'Underfull \\hbox|Underfull \\vbox' "$logfile")
    pages=$(grep -o '([0-9]* pages' "$logfile" 2>/dev/null \
        | grep -o '[0-9]*' | tail -n 1 || echo '?')
    echo "   ${pages}pp, ${cit} undef citations, ${ref} undef references, ${rerun} rerun requests, ${overfull} overfull, ${underfull} underfull"
    stats="${pages}:${cit}:${ref}:${rerun}"

    # Convergence: all references resolved after at least 2 passes
    if [ "$i" -ge 2 ] && [ "$cit" -eq 0 ] && [ "$ref" -eq 0 ] && [ "$rerun" -eq 0 ]; then
        echo "✓ Converged after $i passes."
        publish_pdf "$logfile"
        exit 0
    fi

    # Fixed point with unresolved external/stale references: more passes cannot
    # change the result unless the source labels change.  Avoids spending
    # additional pdflatex passes (and risking OOM on heavy manuscripts) when
    # the converged state is stable but not zero.
    if [ "$i" -ge 3 ] && [ "$rerun" -eq 0 ] && [ "$stats" = "$prev_stats" ]; then
        echo "✓ Stable warning state after $i passes (Cit=$cit, Ref=$ref, Rerun=$rerun)."
        publish_pdf "$logfile"
        exit 0
    fi

    prev_stats="$stats"
done

# Did not converge, but the last pass itself succeeded.  Publication still
# goes through the final-log and artifact gates above.
publish_pdf "$BUILD_DIR/main.log"

if [ "$MAX_PASSES" -eq 1 ]; then
    echo "✓ Completed single pass."
    exit 0
fi

echo "⚠ Did not fully converge after $MAX_PASSES passes (Cit=$cit, Ref=$ref, Rerun=$rerun)."
echo "  This is normal for page-count oscillation on large documents."
exit 0
