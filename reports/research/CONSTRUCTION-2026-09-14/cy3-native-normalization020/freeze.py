from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/cy3-native-normalization020/source'
assert not (R/'source-freeze.json').exists(),'Frozen candidate is immutable; use a new candidate for changes'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rec(p):return {'path':str(p.relative_to(W)) if p.is_relative_to(W) else str(p),'sha256':sha(p),'bytes':p.stat().st_size}
def save(n,o):(R/n).write_text(json.dumps(o,indent=2)+'\n')
base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip();branch=subprocess.check_output(['git','branch','--show-current'],cwd=W,text=True).strip()
assert base=='aaf325a7b7c4d9a8da252ce1a8db5448e5300aa9'
assert branch=='intake/resume-cy3-normalization-020-20260914'
# Verify the predecessor custody manifest once more without writing there.
O=Path('/Users/raeez/mathematics/worktrees/frontier-mine-cy3-20260913');OR=O/'reports/research/CONSTRUCTION-2026-09-14/cy3-native221002'
assert sha(OR/'source-freeze.json')=='02bd496c44c7cffe61c565ffd96cec06829656bce7bf11f6d5c452c5f8da2a2a'
old=json.loads((OR/'artifact-manifest.json').read_text())
for x in old['owned_files']:assert sha(O/x['path'])==x['sha256'],x['path']
save('preservation-final.json',{'predecessor_source_freeze_sha256':sha(OR/'source-freeze.json'),'predecessor_artifact_manifest_sha256':sha(OR/'artifact-manifest.json'),'all_owned_records_match':True,'owned_records_checked':len(old['owned_files']),'old_candidate_modified':False})
# Verify each frozen dependency, including BibTeX inputs and the actual final PDFs.
dep=json.loads((R/'dependency-manifest.json').read_text())
for mode,data in dep.items():
 for row in data['files']+data['generated_inputs']+data['additional_bibtex_inputs']:
  p=Path(row['path']);p=p if p.is_absolute() else W/p
  assert sha(p)==row['sha256'],str(p)
for row in json.loads((R/'pdf-records.json').read_text()).values():assert sha(W/row['path'])==row['sha256']
assert json.loads((R/'final-native-raster-verification.json').read_text())['pdf_sha256']==sha(R/'build-candidate/cy3_candidate.pdf')
assert all(x['byte_identical'] for x in json.loads((R/'pdf-reproduction.json').read_text())['exact_command_repeats'])
assert json.loads((R/'firewall-check.json').read_text())['passed']
controls=json.loads((R/'runtime-controls.json').read_text());assert controls['observed_model']=='gpt-6-astra' and controls['observed_effort']=='ultra'
(R/'git-status-final.txt').write_text(subprocess.check_output(['git','status','--short'],cwd=W,text=True))
sources=[rec(p) for p in sorted(S.rglob('*')) if p.is_file()]
aggregate=hashlib.sha256(json.dumps(sources,sort_keys=True,separators=(',',':')).encode()).hexdigest()
gates={'internal_normalization_proof':'Constructed: positive disks, cone generator, support product, lower normal projection, scalar generator comparison','derived_maps_and_associativity':'Preserved exactly through full source prefixes; both consumer proof bodies unchanged','singular_cyclic_specialization':'Constructed comparison on whole cyclic bundles and action diagrams; existing actual gluing proof preserved','exact_calculations':'PASS: rational determinants, binary regular signs through rank five, both ordered flag counts and factorizations','build':'PASS: baseline541/native541/focused22; converged passes; no fatal/undefined/duplicate errors','pdf_reproduction':'PASS for exact commands/directories. Fresh different directories differ only in pdfTeX trailer IDs; all remaining bytes are identical. No postprocessing.','render':'PASS diagnostic: full native/focused rendered; all23 native affected/transition pages,22 focused pages and14 baseline pages inspected; all564 final native rasters reverified','archive_and_patch':'PASS: all28 archive entries match; four-file patch passes git apply --check and independent in-memory replay','input_closure':'PASS: raw recorder352 native and326 focused; complete native build355 including BibTeX databases/style; all hashes verified','firewall':'PASS: all reader source, PDF text and metadata scanned; sole inherited unused formatting identifier documented','independent_normalization_full_return':'Read in full; exact first-stage orientation, cone, flag and rank-normalization calculations agree. This is predecessor evidence. Fresh exact-candidate acceptance remains required.','root_acceptance':'PENDING','whole_book_mathematical_acceptance':'NOT CLAIMED','formalization':'NOT RUN; internal sheaf and orientation proof is the mathematical argument','publication':'NOT PERFORMED'}
save('gate-results.json',gates)
refs=['normalization-integration.patch','reader-source.tar.gz','archive-manifest.json','dependency-manifest.json','changed-paths.json','patch-check.json','normalization-calculations.json','build.py','compose.py','check_normalization.py','package.py','verify_rasters.py','tool-versions.json','build-diagnostics.json','pdf-records.json','pdf-reproduction.json','cross-directory-reproduction.json','render-manifest.json','final-native-raster-verification.json','label-check.json','firewall-check.json','source-anchors.json','preservation-final.json','runtime-controls.json','instruction-inputs.json','primary-source-and-dispositions.md','question-and-spine.md','independent-normalization-input-check.json','RETURN.md']
manifest={'candidate':'cy3-native-normalization020','status':'Constructed normalization comparison pending fresh root acceptance; neither whole-book nor publication acceptance','base_commit':base,'branch':branch,'worktree':str(W),'predecessor_source_freeze_sha256':sha(OR/'source-freeze.json'),'source_entrypoint':str((S/'platonic/collision_geometry.tex').relative_to(W)),'focused_entrypoint':str((S/'platonic/focused_hall.tex').relative_to(W)),'source_files':sources,'source_aggregate_sha256':aggregate,'source_delta_files':4,'unchanged_predecessor_source_files':24,'records':{name:rec(R/name) for name in refs},'inputs':[rec(p) for p in sorted((R/'inputs').rglob('*')) if p.is_file()],'gates':gates,'pdfs':json.loads((R/'pdf-records.json').read_text())}
save('source-freeze.json',manifest)
owned=[rec(p) for root in [S.parent,R] for p in sorted(root.rglob('*')) if p.is_file() and p.name!='artifact-manifest.json']
artifact={'source_freeze':rec(R/'source-freeze.json'),'source_aggregate_sha256':aggregate,'owned_files':owned,'owned_aggregate_sha256':hashlib.sha256(json.dumps(owned,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'owned_count':len(owned),'rule':'All recorded source, PDFs and evidence bytes are frozen. Subsequent source changes require a new candidate and review. This manifest excludes itself.'}
save('artifact-manifest.json',artifact)
print(json.dumps({'source_freeze':rec(R/'source-freeze.json'),'artifact_manifest':rec(R/'artifact-manifest.json'),'source_aggregate_sha256':aggregate,'owned_count':len(owned),'archive':rec(R/'reader-source.tar.gz'),'patch':rec(R/'normalization-integration.patch'),'pdfs':manifest['pdfs']},indent=2))
