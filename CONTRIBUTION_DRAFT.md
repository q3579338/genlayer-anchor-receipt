# Intelligent Contracts contribution draft

**Submission status: draft prepared. On 2026-10-22 the user explicitly authorized public release and submission of this contribution. The root workflow will perform the actual source/evidence upload and portal submission; this local update does not claim either is complete. Studionet deployment, registration and two synthetic-fixture checks (`SUPPORTED` and `CONTRADICTED`) are finalized. Broader semantic/adversarial behavior is not established. No points claimed.**

## Title

AnchorReceipt — source-scoped claims with independently reproduced evidence receipts

## Short description

A standalone GenLayer contract that registers immutable HTTPS source/claim inputs and produces conservative, source-scoped evidence receipts. Each validator independently retrieves the source and extracts its own structured verdict; deterministic code binds the response bytes and exact quoted units to the immutable inputs. It provides owner controls, idempotent requests, a bounded retry journal and pagination without holding user funds.

## Problem

Applications often need evidence that a particular source explicitly said a particular thing: a published eligibility condition, a release capability or a public announcement. A bare AI yes/no output loses the evidence, cannot show which source bytes were used and does not explain what happens when a source fails or changes. Universal truth is a larger claim than such an application can support.

## What the implementation does

- Freezes one URL, one claim, an owner and an optional predeclared SHA-256 per receipt, all bound by a canonical input hash.
- Independently fetches and semantically extracts on leader and validators; compares the exact normalized output, not merely its JSON shape.
- Limits model output to `SUPPORTED`, `CONTRADICTED` or `UNKNOWN` plus evidence-unit IDs. Programmatic code creates verbatim quotes and checks actual offsets, size and hashes after consensus.
- Treats unavailable, omitted and ambiguous evidence conservatively. Agreed failures are retryable; consensus disagreement cannot persist an intermediate status.
- Seals definitive observations, retains earlier attempts, supports bounded pages and separates each owner's idempotency keys.
- Contains no token deposits, payout, prediction game or monetary settlement.

## Why the GenLayer integration is substantial

Semantic entailment/contradiction is the main computation. It runs inside the intelligent contract and uses custom independent leader/validator execution with actual source retrieval at each node. Deterministic state changes depend on that agreed result and additional byte/quote checks. There is no central verdict API or frontend-only GenLayer mention.

## Current validation evidence

Implemented source: `contracts/AnchorReceipt.py`.

Local Python test suite: `tests/test_anchor_receipt.py`, with run output and a file-hash manifest in `evidence/`. It injects source drift, independent model disagreement, tampered leader data, nonexistent quotes, malformed outputs and forged body hashes, and checks ownership, idempotency and failure recovery. **These are local mocks, not tests on GenVM or real provider results.**

Official `genvm-linter` 0.11.0 validation passed using the GenVM v0.2.16 bundle and the exact pinned runner dependency: 7 public methods (4 view, 3 write), 1 constructor parameter. Basic deployed import/hashing/registration storage is also exercised by actual chain transactions.

Studionet (chain ID `61999`) contract: `0xf20c3D5C8Ed12AC923b20150016Ee397C6636e08`.

- Deployment: `0x657cfe993dd21c85f29506e2aa0de22cac8156732e8c976b626f62b6cda2f9d9`, `FINALIZED` / `MAJORITY_AGREE`; deployed source matches contract source SHA-256 `d53bf94155c164844630fca8ce3a9ddc6ffdb440db877ffdf3b4bc1b70f5a620`.
- Registration: `0x3aeb55ccf3ab7b3d097cb8a8aa3e31f76d989d7ed90a1db691d222d0963a66c4`, `FINALIZED` / `MAJORITY_AGREE`, leader execution `SUCCESS`. The execution log also records a validator cancellation after quorum; it must not be reported as every validator completing.
- One real source check: `0xc638c8d69c5d9921adcaf1ae999c0b07e243fe5926438591f5bcb80355b7a70e`, `FINALIZED` / `MAJORITY_AGREE`, leader execution `SUCCESS`. Receipt `1` is `SEALED` with `SUPPORTED`, HTTP `200`, body `450` bytes and SHA-256 `9b7ef32ce39692d42629c0f5f45f24a11b0f1c5a8efe63088300f85b2f256e8d`. Its exact quote is `Applications for the example workshop close on 30 October 2026 at 18:00 UTC.`, at character offsets `[211:287]`. This is a developer-controlled synthetic fixture, not a claim about a real official event. The check log also has a validator cancellation after quorum, so it does not establish every validator's completion or model diversity.
- Second real source check: `0xc8e8ff726fdfdd1cfc924abf50f060355e57594afe7af782ffdbedf80cf87682`, `FINALIZED` / `MAJORITY_AGREE`, leader execution `SUCCESS`. Receipt `2` is `SEALED` with `CONTRADICTED`. Its claim says the same workshop closes on 1 November 2026 at 18:00 UTC; the same 450-byte source explicitly says 30 October 2026, and the exact evidence quote is again unit `3`, offsets `[211:287]`. Actual state readback confirms the verdict; transaction success alone was not treated as proof of contradiction.

The completed real-node semantic evidence is limited to those two date-claim scenarios on one synthetic fixture: one supporting fact and one explicitly contradicted date. Still missing: real `UNKNOWN` observations, source/model disagreement and recovery, real prompt-injection testing, heterogeneous-model availability, maximum-payload/fee measurements and a real provider adversarial corpus. The accompanying `NODE_VALIDATION.md` records these gaps. Field-minimized receipt/state summaries have been prepared locally under `evidence/public/`; their release is authorized and will be performed by the root workflow using `RELEASE_MANIFEST.md`, excluding raw internal records.

## Limitations to include in the submission

The contract verifies what one source says, not whether that source is truthful or historically complete. Strict agreement can fail for mutable content or differing evidence choices. It supports only short UTF-8 text/Markdown/JSON, at most two fixed source units per determinate decision and 16 agreed attempts per receipt. Initial-host allowlisting does not establish publisher identity or redirect/DNS safety; the actual host environment must enforce and verify its outbound controls. Model injection and correlated semantic errors remain possible despite output limits and independent execution.

## Distinct contribution statement

AnchorReceipt is a new standalone reusable evidence primitive. It does not resubmit the separate Event Duels application as another category or milestone and does not inherit any application address or execution claim from it.

## Links

Source destination: [q3579338/genlayer-anchor-receipt](https://github.com/q3579338/genlayer-anchor-receipt). Public release was explicitly authorized on 2026-10-22. The root workflow will perform and verify the upload; this draft does not prestate its completion.

Deployed contract: Studionet chain ID `61999`, `0xf20c3D5C8Ed12AC923b20150016Ee397C6636e08`.

Real-node deployment, registration and the two synthetic-fixture supporting/contradicting observations: the finalized transaction IDs above. `UNKNOWN` and adversarial/provider scenarios: not yet established.

Demo/usage evidence: local tests, official static/schema validation and two actual supporting/contradicting observations with source hashes and verbatim quotes. These are narrow synthetic examples, not a general accuracy or robustness evaluation.

Never replace these status statements with invented links, transaction IDs or deployment claims.
