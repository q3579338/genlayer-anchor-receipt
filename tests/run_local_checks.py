"""Run local fake-backed unit tests and persist accurately scoped evidence."""

from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import sys
import unittest


root = Path(__file__).resolve().parents[1]
suite = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test_*.py")
output = io.StringIO()
result = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
evidence = root / "evidence"
evidence.mkdir(exist_ok=True)
scope = "LOCAL PYTHON FAKE ONLY; no GenVM, real models, deployment or network consensus"
(evidence / "local-tests.txt").write_text(scope + "\n\n" + output.getvalue(), encoding="utf-8")
files = ["contracts/AnchorReceipt.py", "tests/test_anchor_receipt.py", "tests/run_local_checks.py",
         "README.md", "NODE_VALIDATION.md", "CONTRIBUTION_DRAFT.md"]
report = {
    "recorded_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
    "scope": scope,
    "python": sys.version.split()[0],
    "command": "python -B tests/run_local_checks.py",
    "tests_run": result.testsRun,
    "failures": len(result.failures), "errors": len(result.errors),
    "successful": result.wasSuccessful(),
    "deployed": False, "signed": False, "submitted": False,
    "real_node_execution": False, "real_llm_evaluation": False,
    "sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in files},
}
(evidence / "local-test-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(output.getvalue())
print("Evidence saved. Scope:", scope)
raise SystemExit(0 if result.wasSuccessful() else 1)
