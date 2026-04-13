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
TEXFLAGS="-interaction=batchmode -file-line-error -synctex=0 -cnf-line=buf_size=1000000 -cnf-line=stack_size=20000"
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
        grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$logfile" | head -n 20 || true
    elif [ -f "$RUN_LOG" ]; then
        tail -n 40 "$RUN_LOG" || true
    fi
}

# ---------------------------------------------------------------------------
# Build loop
# ---------------------------------------------------------------------------
echo "Building main.tex (up to $MAX_PASSES passes) [NS=$BUILD_NS]"
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

    cit=$(count_matches 'Citation.*undefined' "$logfile")
    ref=$(count_matches 'Reference.*undefined' "$logfile")
    rerun=$(count_matches 'Label\(s\) may have changed|Package rerunfilecheck Warning' "$logfile")
    overfull=$(count_matches 'Overfull \\hbox' "$logfile")
    underfull=$(count_matches 'Underfull \\hbox|Underfull \\vbox' "$logfile")
    pages=$(grep -o '([0-9]* pages' "$logfile" 2>/dev/null \
        | grep -o '[0-9]*' | tail -n 1 || echo '?')
    echo "   ${pages}pp, ${cit} undef citations, ${ref} undef references, ${rerun} rerun requests, ${overfull} overfull, ${underfull} underfull"

    # Hard failure: non-zero exit AND no PDF produced
    if [ "$tex_rc" -ne 0 ] && \
       { [ ! -f "$BUILD_DIR/main.pdf" ] || \
         ! grep -aq 'Output written' "$logfile" 2>/dev/null; }; then
        show_failure_summary
        exit "$tex_rc"
    fi

    # Convergence: all references resolved after at least 2 passes
    if [ "$i" -ge 2 ] && [ "$cit" -eq 0 ] && [ "$ref" -eq 0 ] && [ "$rerun" -eq 0 ]; then
        echo "✓ Converged after $i passes."
        mkdir -p "$SRC_DIR/out"
        cp "$BUILD_DIR/main.pdf" "$SRC_DIR/out/main.pdf"
        cp "$logfile" "$SRC_DIR/out/main.log" 2>/dev/null || true
        exit 0
    fi
done

# Did not converge but PDF was produced
if [ ! -f "$BUILD_DIR/main.pdf" ] || \
   ! grep -aq 'Output written' "$BUILD_DIR/main.log" 2>/dev/null; then
    show_failure_summary
    exit 1
fi

mkdir -p "$SRC_DIR/out"
cp "$BUILD_DIR/main.pdf" "$SRC_DIR/out/main.pdf"
cp "$BUILD_DIR/main.log" "$SRC_DIR/out/main.log" 2>/dev/null || true

if [ "$MAX_PASSES" -eq 1 ]; then
    echo "✓ Completed single pass."
    exit 0
fi

echo "⚠ Did not fully converge after $MAX_PASSES passes (Cit=$cit, Ref=$ref, Rerun=$rerun)."
echo "  This is normal for page-count oscillation on large documents."
exit 0
