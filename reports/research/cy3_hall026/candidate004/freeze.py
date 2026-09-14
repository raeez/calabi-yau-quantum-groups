"""Freeze the built candidate after the recorded visual inspection."""

from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re
import subprocess


report = Path(__file__).resolve().parent
root = report.parents[3]
source = root/"research-candidates/cy3_hall026/candidate004"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(name, value):
    (report/name).write_text(json.dumps(value, indent=2)+"\n")


closure = json.loads((report/"tex-input-closure.json").read_text())
mismatches = [name for name, sha in closure.items()
              if not Path(name).exists() or digest(Path(name)) != sha]
assert not mismatches
source_files = sorted(p for p in source.rglob("*") if p.is_file())
patterns = {
    "manuscript_firewall": r"\b(agent|reviewer|worktree|candidate|TODO|harness|archive|workflow|session)\b|/Users/|github\.com",
    "private_paths": r"~/(kernel|centcom|moxie|ecosystem)|/Users/[^/ ]+/(kernel|centcom|moxie|ecosystem)|kernel/(formal|docs|mez)|centcom/"}
hits = {key: [] for key in patterns}
for path in source_files:
    for line_no, line in enumerate(path.read_text().splitlines(), 1):
        for key, pattern in patterns.items():
            if re.search(pattern, line, re.I):
                hits[key].append({"path": str(path.relative_to(root)), "line": line_no, "text": line})
assert not any(hits.values()), hits
build = json.loads((report/"build-command.json").read_text())
last_pass = max(item["pass"] for item in build["passes"])
log = (report/"build"/f"pass{last_pass}.txt").read_text(errors="replace")
assert not re.search(r"Overfull|undefined|^!", log, re.M)
reader = (report/"build/reader.txt").read_text()
assert "The raw ordinary scalar pullback is zero" in reader
pdf = report/"build/scalar-restriction.pdf"
info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
assert pages == 29
render = {
    "pdf_sha256": digest(pdf), "pages": pages,
    "all_pages_contact_inspected": list(range(1, 30)),
    "new_chapter_and_bibliography_individually_inspected": list(range(23, 30)),
    "findings": [],
    "comments": "All pages have legible mathematics and complete margins. The changed chapter has no clipping, overlap or missing glyphs. Imported body files retain their exact source bytes.",
    "raster_command": "pdftoppm -r 90 -png <pdf> <owned render/page prefix>",
    "images": [{"path": str(p.relative_to(root)), "sha256": digest(p)}
               for p in sorted((report/"render").glob("*.png"))]}
write_json("render-check.json", render)
checks = {
    "closure_inputs": len(closure), "closure_mismatches": mismatches,
    "firewall_and_private_path_scan": hits, "tex_error": False,
    "undefined_references": False, "overfull_boxes": False,
    "new_chapter_underfull_boxes": False,
    "retained_nonblocking_diagnostics": [
        "Two underfull boxes in unchanged inherited source",
        "amsrefs recommendation in unchanged inherited source",
        "epstopdf warns that shell escape is disabled"],
    "verification_issue_resolved": "The first manifest attempt found a non-UTF-8 TeX diagnostic byte. The scanner now decodes diagnostics with replacement and preserves the raw build log.",
    "calculations_sha256": digest(report/"calculation-results.json"),
    "render_check_sha256": digest(report/"render-check.json"),
    "source_copies_verified": all(digest(Path(v["copy"])) == v["sha256"]
                                 for v in json.loads((report/"preserved-source-copies.json").read_text()))}
write_json("verification.json", checks)
scripts = [report/"build.py", report/"check_restriction.py", report/"freeze.py"]
patch = ""
for path in source_files+scripts:
    patch += "".join(difflib.unified_diff([], path.read_text().splitlines(keepends=True),
                                        fromfile="/dev/null", tofile=str(path.relative_to(root))))
(report/"candidate.patch").write_text(patch)
manifest = {
    "frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "base_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
    "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=root, text=True).strip(),
    "worktree": str(root), "status": "proposed_mathematical_candidate_requires_fresh_exact_review",
    "entrypoint": str(source/"integrated-main.tex"),
    "new_mathematical_source": str(source/"rank_two_one_restriction.tex"),
    "source_files": [{"path": str(p.relative_to(root)), "sha256": digest(p)} for p in source_files],
    "build_and_check_inputs": [{"path": str(p.relative_to(root)), "sha256": digest(p)}
                               for p in scripts+[report/"frozen-inputs/raeez-math-template.sty"]],
    "aggregate_source_diff_sha256": digest(report/"candidate.patch"),
    "input_freeze_sha256": digest(report/"input-freeze.json"),
    "primary_source_record_sha256": digest(report/"primary-sources.json"),
    "tex_input_closure_sha256": digest(report/"tex-input-closure.json"),
    "verification_sha256": digest(report/"verification.json"),
    "pdf_path": str(pdf), "pdf_sha256": digest(pdf), "pdf_pages": pages,
    "build_command": "python3 reports/research/cy3_hall026/candidate004/build.py",
    "calculation_command": "/opt/homebrew/bin/python3 reports/research/cy3_hall026/candidate004/check_restriction.py",
    "runtime_requirement": {"model": "gpt-6-astra", "reasoning_effort": "ultra",
                            "observed_controls": "unavailable_unverified"},
    "residual_obligations": ["Fresh exact mathematical acceptance review",
                             "Full-source polynomial divisibility beyond the specified two-generator submodule",
                             "Higher-rank compatibility", "Actual physical/native hCS-to-Hall comparison"],
    "custody": {"no_staging": True, "no_commit_push": True, "no_central_pdf_write": True,
                "no_standalone_pdf_opening": True}}
write_json("manifest.json", manifest)
print(json.dumps({"manifest_sha256": digest(report/"manifest.json"),
                  "new_source_sha256": digest(source/"rank_two_one_restriction.tex"),
                  "aggregate_source_diff_sha256": manifest["aggregate_source_diff_sha256"],
                  "pdf_sha256": manifest["pdf_sha256"], "pages": pages, "inputs": len(closure)}, indent=2))
