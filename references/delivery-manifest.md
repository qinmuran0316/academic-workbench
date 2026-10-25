# Delivery manifest schema v1

The optional checker accepts a JSON object like this:

```json
{
  "schema_version": 1,
  "task": {"id": "java-library-demo", "synthetic": true},
  "deliverables": [
    {"path": "src/Main.java", "kind": "source", "required": true}
  ],
  "checks": [
    {"id": "compile-java-11", "status": "passed", "required": true,
     "evidence": "evidence/compile.txt"},
    {"id": "native-cad-viewer", "status": "not_run", "required": false}
  ],
  "limitations": ["AutoCAD was not installed in this environment."]
}
```

Paths are relative to the delivery root. An artifact may include a `sha256` field containing its actual 64-character lowercase hex digest. The checker rejects traversal, absolute/drive paths, symlink escapes, duplicates, empty required files, malformed known containers, hash mismatches, failed required checks, and executed checks without evidence. It never runs a command stored in JSON. A pass means the checker observed the stated structural condition; it does not prove academic correctness or native application compatibility. The helper scripts require Python 3.10 or later; `inspect_dxf.py` additionally needs `ezdxf` in that interpreter.

`not_applicable` requires a nonblank `reason`. The Office probe only checks ZIP integrity and the expected root elements/namespaces in `[Content_Types].xml` and the main document part. It reports a shallow-check warning: it does not validate all OPC relationships, renderability, formulas, or native Office behavior. Use an actual parser or application and inspect rendered output for those checks.
