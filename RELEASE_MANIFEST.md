# Authorized public release manifest

This is the concrete file allowlist for public release to [q3579338/genlayer-anchor-receipt](https://github.com/q3579338/genlayer-anchor-receipt). On 2026-10-22 the user explicitly authorized public release and submission of both contributions, including this AnchorReceipt repository, the NoticeDelta repository, the Sites public demo and portal submissions. The root workflow will perform and verify all actual uploads/submissions. This local manifest records authorization and prepared contents; it does not claim the source has already been uploaded or the portal submission completed. Only listed files form this release; excluded/internal paths remain local.

## Source, license, documentation and tests

| Proposed public path | Contents |
| --- | --- |
| `.gitattributes` | Fixed LF checkout policy. |
| `.gitignore` | Cache, environment and key-file exclusions. |
| `LICENSE` | MIT license for the proposed source release. |
| `contracts/AnchorReceipt.py` | Exact deployed contract source, SHA-256 `d53bf94155c164844630fca8ce3a9ddc6ffdb440db877ffdf3b4bc1b70f5a620`. |
| `README.md` | Implementation, two exact completed synthetic date-claim cases and explicit limitations. |
| `CONTRIBUTION_DRAFT.md` | Draft portal submission; does not claim submission or points. |
| `NODE_VALIDATION.md` | Two completed real-node cases and remaining scenario/provider checks. |
| `RELEASE_MANIFEST.md` | This proposed public file allowlist. |
| `tests/test_anchor_receipt.py` | 22 fake-backed local tests; not represented as network execution. |
| `tests/run_local_checks.py` | Standard-library local test runner and evidence generator. |

## Minimized evidence prepared for future publication

| Proposed public path | Scope and source |
| --- | --- |
| `evidence/public/deployment-summary.json` | Allowed fields projected from local `evidence/deployment.json`: contract/network, transaction hash, finality, aggregate consensus and execution outcomes. |
| `evidence/public/registration-summary.json` | Allowed fields projected from local `evidence/register-receipt.json`; preserves quorum-cancellation caveat without sender, validator addresses or full calldata. |
| `evidence/public/supported-check-summary.json` | Allowed fields from local `evidence/check-receipt.json`, limited to finalized transaction `0xc638c8d69c5d9921adcaf1ae999c0b07e243fe5926438591f5bcb80355b7a70e`. No case still in progress. |
| `evidence/public/supported-state-summary.json` | Selected fields from local `evidence/checked-state.json`: one synthetic claim/source, bound body/input/observation hashes, state and verbatim quote/offsets. Owner address omitted; hashes remain recorded chain values. |
| `evidence/public/contradiction-check-summary.json` | Allowed fields from local `evidence/contradiction-check-receipt.json`, limited to finalized transaction `0xc8e8ff726fdfdd1cfc924abf50f060355e57594afe7af782ffdbedf80cf87682`. |
| `evidence/public/contradiction-state-summary.json` | Selected fields from local `evidence/contradiction-state.json`: second synthetic date claim, actual `SEALED`/`CONTRADICTED` state, bound hashes and exact source quote/offsets. Owner address omitted. |
| `evidence/public/local-test-summary.json` | 22 local tests, zero errors/failures, original run time, exact source/test hashes and explicit fake-only scope. Does not imply a real-provider result. |

These are human-readable field-minimized summaries, not unmodified full node receipts or independently signed attestations. They retain public contract and transaction identifiers for lookup and accurately distinguish source behavior from source truth. Omitting sender/validator addresses reduces unnecessary publication; it does not anonymize public chain identifiers. The two observed synthetic cases demonstrate support and explicit date contradiction on one source. Model-provider diversity, `UNKNOWN` behavior, general contradiction accuracy and real injection robustness are not established by this release.

## Excluded from public upload

- `evidence/publication-status.json`: internal automatic-approval decision and local workflow record. **Never include it in the public commit.**
- All raw `evidence/*.json`, including raw deployment, registration/check receipts, full checked state and failed-deployment diagnostics. Publish only the specifically listed minimized copies above.
- Original local test report/output unless separately reviewed; the listed minimized local summary avoids stale documentation hashes from an earlier snapshot.
- Any additional scenario or pending case not explicitly listed above.
- Private keys, seed phrases, passwords, access tokens, `.env`, credentials/configuration stores, virtual environments, caches and generated runtime files.
- `.git/`, shell/login-helper diagnostics and automatic-approval logs.

The previous local source-only commit is `51acea74c086fc0c891dccd7c19beb8c2ea8478b`. The 2026-10-22 user authorization is recorded; the root workflow will prepare the final release commit and perform the public upload and submission. No public operation is performed by this local documentation update.
