# ============================================================================
#  Makefile — Calabi-Yau Quantum Groups
# ============================================================================
#
#  Usage:
#    make               Full converging build → main.pdf
#    make fast           Quick build (up to 4 passes)
#    make clean          Remove LaTeX build artifacts
#    make veryclean      Remove artifacts AND compiled PDFs
#    make count          Line counts and page estimate
#    make check          Halt-on-error validation
#    make test           Run compute test suite
#    make help           Show available targets
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
TEX       := pdflatex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0
BUILD_SCRIPT := ./scripts/build.sh
LOG_DIR   := .build_logs

PASSES    := 6
FAST_PASSES := 4

SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/theory/*.tex) \
             $(wildcard chapters/examples/*.tex) \
             $(wildcard chapters/connections/*.tex) \
             $(wildcard appendices/*.tex)

PDF       := $(MAIN).pdf
OUT_DIR   := out
OUT_PDF   := $(OUT_DIR)/calabi_yau_quantum_groups.pdf

STAMP     := .build_stamp

ifeq (,$(wildcard $(PDF)))
  $(shell rm -f $(STAMP))
endif

AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.PHONY: all fast clean veryclean count check test publish help

## all: Full converging build
all: $(STAMP) publish

$(STAMP): $(SOURCES) $(BUILD_SCRIPT)
	@echo "======================================================"
	@echo "  Building: $(MAIN).tex  ->  $(PDF)"
	@echo "  Engine:   quiet $(TEX) wrapper (up to $(PASSES) passes)"
	@echo "======================================================"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ ! -f $(MAIN).pdf ]; then \
		echo "  Build failed -- no PDF produced."; exit 1; \
	fi
	@touch $(STAMP)
	@echo ""
	@echo "  $(PDF) built successfully."
	@echo ""

## fast: Quick converging build
fast:
	@echo "  -- Fast build (up to $(FAST_PASSES) passes) --"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"

## publish: Copy final PDF to out/
publish:
	@mkdir -p $(OUT_DIR)
	@if [ -f $(PDF) ]; then cp $(PDF) $(OUT_PDF); echo "  $(OUT_PDF)"; \
	else echo "  $(PDF) not found -- run 'make fast' first."; fi

## check: Halt-on-error validation
check:
	@echo "  -- Error check (halt-on-error) --"
	@mkdir -p $(LOG_DIR)
	@$(TEX) -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex >$(LOG_DIR)/check.log 2>&1 || { \
		echo "  Check failed. See $(LOG_DIR)/check.log"; \
		grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/check.log | head -n 20 || tail -n 40 $(LOG_DIR)/check.log; \
		exit 1; \
	}
	@echo "  No fatal errors."

## test: Run compute test suite
test:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  -- Running compute test suite --"; \
		python3 -m pytest compute/tests/ -q -ra --durations=10; \
	else \
		echo "  (no compute tests found -- skipping)"; \
	fi

## clean: Remove build debris
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  Clean."

## veryclean: Remove everything including PDF
veryclean: clean
	@rm -f $(MAIN).pdf $(STAMP)
	@rm -rf $(OUT_DIR)
	@echo "  Stamp, PDFs, and out/ removed."

## count: Manuscript statistics
count:
	@echo ""
	@echo "  -- Manuscript Statistics --"
	@echo ""
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './archive/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './archive/*' -exec cat {} + | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		PAGES=$$(strings $(PDF) | grep -c '/Type /Page' 2>/dev/null || echo '?'); \
		printf "  PDF pages:     %s\n" "$$PAGES"; \
		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:           (not yet built)"; \
	fi
	@echo ""

## help: Show available targets
help:
	@echo ""
	@echo "  Calabi-Yau Quantum Groups -- Build System"
	@echo "  ------------------------------------------"
	@echo ""
	@echo "  make               Full converging build"
	@echo "  make fast          Quick build (up to $(FAST_PASSES) passes)"
	@echo "  make check         Halt-on-error validation"
	@echo "  make test          Run compute tests"
	@echo "  make clean         Remove build debris"
	@echo "  make veryclean     Remove everything including PDF"
	@echo "  make count         Manuscript statistics"
	@echo "  make publish       Copy PDF to out/"
	@echo "  make help          This message"
	@echo ""
