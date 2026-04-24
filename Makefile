# ============================================================================
#  Makefile - Calabi-Yau Quantum Groups (Vol III)
# ============================================================================
#
#  Usage:
#    make               Full converging build → out/main.pdf
#    make fast           Quick build (up to 4 passes) → out/main.pdf
#    make release        Full release → out/ + iCloud
#    make standalone     Build standalone documents → out/
#    make clean          Remove LaTeX build artifacts
#    make veryclean      Remove artifacts AND out/ (forces rebuild)
#    make clean-builds   Remove all /tmp/mkd-* isolated build directories
#    make count          Line counts and page estimate
#    make check          Halt-on-error validation
#    make test           Run compute test suite
#    make help           Show available targets
#
#  Build isolation (parallel agents):
#    Each build runs in its own /tmp directory.  Set MKD_BUILD_NS to reuse
#    the same directory across invocations (warm .aux files = faster builds):
#
#      export MKD_BUILD_NS="agent-$$"   # set once per agent session
#      make fast                         # cold first time, warm thereafter
#
#  All compiled output goes to out/.
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
TEX       := pdflatex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0
PYTEST    ?= pytest
BUILD_SCRIPT := ./scripts/build.sh
LOG_DIR   := .build_logs

# iCloud destination for release PDFs
ICLOUD_DIR := /Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

PASSES    := 6
FAST_PASSES := 4

SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/theory/*.tex) \
             $(wildcard chapters/examples/*.tex) \
             $(wildcard chapters/connections/*.tex) \
             $(wildcard chapters/frame/*.tex) \
             $(wildcard appendices/*.tex)

# Output -- everything goes to out/
OUT_DIR   := out
PDF       := $(OUT_DIR)/main.pdf
ICLOUD_MAIN_PREREQ := $(if $(wildcard $(PDF)),,$(PDF))

# Working notes
WN_TEX    := working_notes.tex

# Standalone documents
STANDALONE_TEX := $(wildcard standalone/*.tex)
STANDALONE_PASSES := 3

STAMP     := .build_stamp

ifeq (,$(wildcard $(PDF)))
  $(shell rm -f $(STAMP))
endif

AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.DEFAULT_GOAL := all

.PHONY: all fast clean veryclean clean-builds count check test help release working-notes standalone dist icloud verify-independence verify-independence-verbose

## icloud: Copy latest PDFs to iCloud Drive (subject-organised)
icloud: $(ICLOUD_MAIN_PREREQ) standalone
	@echo "  ── Copying Vol III to iCloud (subject-organised) ──"
	@mkdir -p "$(ICLOUD_DIR)/volumes"
	@mkdir -p "$(ICLOUD_DIR)/vol3_6d_hcs_cy"
	@[ -f $(PDF) ] && cp $(PDF) "$(ICLOUD_DIR)/volumes/vol3_calabi_yau_quantum_groups.pdf" \
		&& echo "    ✓ volumes/vol3" || true
	@for pdf in $(OUT_DIR)/*.pdf; do \
		name=$$(basename "$$pdf"); \
		if [ "$$name" != "main.pdf" ]; then \
			cp "$$pdf" "$(ICLOUD_DIR)/vol3_6d_hcs_cy/$$name"; \
			echo "    ✓ vol3_6d_hcs_cy/$$name"; \
		fi; \
	done
	@echo "  Vol III PDFs copied to iCloud."

## all: Full converging build → out/
all: $(STAMP)

$(STAMP): $(SOURCES) $(BUILD_SCRIPT)
	@echo "======================================================"
	@echo "  Building: $(MAIN).tex  ->  $(PDF)"
	@echo "======================================================"
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ ! -f $(PDF) ]; then \
		echo "  Build failed -- no PDF produced."; exit 1; \
	fi
	@touch $(STAMP)
	@echo ""
	@echo "  $(PDF) built successfully."
	@echo ""

$(PDF): $(STAMP)
	@true

## fast: Quick converging build → out/main.pdf
fast:
	@echo "  -- Fast build (up to $(FAST_PASSES) passes) --"
	@$(BUILD_SCRIPT) $(FAST_PASSES)

## working-notes: Build the working notes → out/working_notes.pdf
working-notes:
	@echo "  -- Building working notes --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) $(WN_TEX) >$(LOG_DIR)/working-notes.log 2>&1 || true
	@$(TEX) $(TEXFLAGS) $(WN_TEX) >$(LOG_DIR)/working-notes.log 2>&1 || true
	@if [ -f working_notes.pdf ]; then \
		mv working_notes.pdf $(OUT_DIR)/working_notes.pdf; \
		rm -f working_notes.aux working_notes.log working_notes.out working_notes.toc 2>/dev/null; \
		echo "  $(OUT_DIR)/working_notes.pdf"; \
	else \
		echo "  Working notes build failed. See $(LOG_DIR)/working-notes.log"; \
		exit 1; \
	fi

## release: Full rebuild → out/ + standalones + iCloud
release:
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@mkdir -p $(LOG_DIR) $(OUT_DIR)
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  ── RELEASE BUILD (Vol III) ──"
	@echo "  ══════════════════════════════════════════"
	@echo ""
	@echo "  [1/3] Main manuscript"
	@$(BUILD_SCRIPT) $(PASSES)
	@if [ -f $(PDF) ]; then \
		echo "  ✓  $(PDF)"; \
		cp $(PDF) calabi_yau_quantum_groups.pdf; \
		echo "  ✓  calabi_yau_quantum_groups.pdf"; \
	else \
		echo "  ✗  Manuscript build failed."; \
	fi
	@echo ""
	@echo "  [2/3] Working notes"
	@$(MAKE) --no-print-directory working-notes
	@echo ""
	@echo "  [3/3] Standalone documents and iCloud"
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  ══════════════════════════════════════════"
	@echo "  Release complete. All output in out/:"
	@ls -1 $(OUT_DIR)/*.pdf 2>/dev/null | sed 's/^/    /'
	@echo "  ══════════════════════════════════════════"

## standalone: Build standalone documents → out/
standalone:
	@echo "  -- Building standalone documents --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@if [ -z "$(strip $(STANDALONE_TEX))" ]; then \
		echo "  (no standalone documents found)"; \
	else \
		failures=0; \
		for tex in $(STANDALONE_TEX); do \
			if [ ! -f "$$tex" ]; then continue; fi; \
			base=$$(basename "$$tex" .tex); \
			if [ -f "$(OUT_DIR)/$$base.pdf" ] && [ "$(OUT_DIR)/$$base.pdf" -nt "$$tex" ]; then \
				echo "  ok  $(OUT_DIR)/$$base.pdf (up to date)"; \
				continue; \
			fi; \
			tmpdir=$$(mktemp -d "/tmp/mkd-$$(basename "$$(pwd)")-standalone-$$base.XXXXXX"); \
			echo "  [standalone] $$tex -> $(OUT_DIR)/$$base.pdf"; \
			for pass in $$(seq 1 $(STANDALONE_PASSES)); do \
				TEXINPUTS="$$tmpdir:$$(pwd):$$(pwd)/standalone:" $(TEX) $(TEXFLAGS) -output-directory="$$tmpdir" "$$tex" >"$(LOG_DIR)/standalone-$$base-pass$$pass.log" 2>&1; rc=$$?; \
				if [ -f "$$tmpdir/$$base.idx" ]; then makeindex -q "$$tmpdir/$$base.idx" >/dev/null 2>&1 || true; fi; \
				if [ $$rc -ne 0 ]; then \
					if grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOG_DIR)/standalone-$$base-pass$$pass.log" >/dev/null 2>&1; then \
						echo "  fail  $$tex failed on pass $$pass. See $(LOG_DIR)/standalone-$$base-pass$$pass.log"; \
						grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOG_DIR)/standalone-$$base-pass$$pass.log" | head -n 20 || tail -n 40 "$(LOG_DIR)/standalone-$$base-pass$$pass.log"; \
						failures=$$((failures + 1)); \
						break; \
					else \
						echo "  warn  $$tex returned $$rc on pass $$pass; continuing."; \
					fi; \
				fi; \
			done; \
			if [ -f "$$tmpdir/$$base.pdf" ]; then \
				cp "$$tmpdir/$$base.pdf" "$(OUT_DIR)/$$base.pdf"; \
				echo "  ok  $(OUT_DIR)/$$base.pdf"; \
			elif [ $$failures -eq 0 ]; then \
				echo "  fail  no PDF produced for $$tex"; \
				failures=$$((failures + 1)); \
			fi; \
		done; \
		if [ $$failures -ne 0 ]; then \
			echo "  fail  $$failures standalone document(s) failed."; \
			exit 1; \
		fi; \
	fi

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
		$(PYTEST) compute/tests/ -q -ra --durations=10; \
	else \
		echo "  (no compute tests found -- skipping)"; \
	fi

## verify-independence: Audit ProvedHere claims vs independent-verification registry
##                     (tautology / orphan check; coverage metric reported)
verify-independence:
	@python3 compute/scripts/audit_independent_verification.py

## verify-independence-verbose: Same, with full list of uncovered claims
verify-independence-verbose:
	@python3 compute/scripts/audit_independent_verification.py --verbose --show-orphans

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

## veryclean: Remove everything including out/
veryclean: clean
	@rm -f $(STAMP)
	@rm -rf $(OUT_DIR)
	@echo "  Stamp and out/ removed."

## clean-builds: Remove ALL /tmp/mkd-* isolated build directories (all volumes).
clean-builds:
	@echo "  Cleaning isolated build directories..."
	@rm -rf /tmp/mkd-chiral-bar-cobar-* /tmp/mkd-chiral-bar-cobar-vol2-* /tmp/mkd-calabi-yau-quantum-groups-*
	@echo "  ✓  All /tmp/mkd-* build directories removed."

## count: Manuscript statistics
count:
	@echo ""
	@echo "  -- Manuscript Statistics --"
	@echo ""
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './archive/*' -not -path './out/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './archive/*' -not -path './out/*' -exec cat {} + | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		PAGES=$$(strings $(PDF) | grep -c '/Type /Page' 2>/dev/null || echo '?'); \
		printf "  PDF pages:     %s\n" "$$PAGES"; \
		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:           (not yet built)"; \
	fi
	@echo ""

## dist: Create archive for distribution.
dist: release
	@echo "  -- Creating archive --"
	@rm -f $(OUT_DIR)/CalabiYauQuantumGroups.zip
	@zip -r $(OUT_DIR)/CalabiYauQuantumGroups.zip \
		main.tex working_notes.tex chapters/ appendices/ notes/ compute/ \
		Makefile CLAUDE.md scripts/ \
		$(PDF) \
		$(OUT_DIR)/working_notes.pdf \
		-x '.*' -x '**/.*' -x '**/__pycache__/*' -x '**/*.pyc' \
		-x 'compute/.venv/*' \
		>$(LOG_DIR)/dist.log 2>&1
	@echo "  $(OUT_DIR)/CalabiYauQuantumGroups.zip ($$(du -h $(OUT_DIR)/CalabiYauQuantumGroups.zip | cut -f1))"

## help: Show available targets
help:
	@echo ""
	@echo "  Calabi-Yau Quantum Groups -- Build System"
	@echo "  ------------------------------------------"
	@echo "  All compiled output goes to out/"
	@echo ""
	@echo "  make               Full converging build → out/"
	@echo "  make fast          Quick build → out/main.pdf"
	@echo "  make release       Full release → out/ + standalones + iCloud"
	@echo "  make working-notes Build working notes → out/working_notes.pdf"
	@echo "  make standalone    Build standalone documents → out/"
	@echo "  make dist          Create archive in out/"
	@echo "  make check         Halt-on-error validation"
	@echo "  make test          Run compute tests"
	@echo "  make clean         Remove build debris"
	@echo "  make veryclean     Remove everything including out/"
	@echo "  make clean-builds  Remove /tmp/mkd-* isolated build directories"
	@echo "  make count         Manuscript statistics"
	@echo "  make help          This message"
	@echo ""
