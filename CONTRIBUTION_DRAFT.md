# Intelligent Contracts contribution draft

**Submission status: draft only; not submitted to the contribution portal. A public repository has been created but the prepared source commit is still local, awaiting explicit publication approval. Studionet deployment plus registration are finalized. The semantic `check` path has not been run or verified. No points claimed.**

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

Missing before a strong submission: successful and adversarial real `check` observations, independent source/model comparison evidence, public raw finalized receipts, observed fee/runtime limits, and a real provider adversarial corpus. Deployment/registration alone do not prove any semantic verdict. The accompanying `NODE_VALIDATION.md` records completed work separately from those gaps. Raw evidence is currently local and excluded from the initial public source commit pending its separate evidence review.

## Limitations to include in the submission

The contract verifies what one source says, not whether that source is truthful or historically complete. Strict agreement can fail for mutable content or differing evidence choices. It supports only short UTF-8 text/Markdown/JSON, at most two fixed source units per determinate decision and 16 agreed attempts per receipt. Initial-host allowlisting does not establish publisher identity or redirect/DNS safety; the actual host environment must enforce and verify its outbound controls. Model injection and correlated semantic errors remain possible despite output limits and independent execution.

## Distinct contribution statement

AnchorReceipt is a new standalone reusable evidence primitive. It does not resubmit the separate Event Duels application as another category or milestone and does not inherit any application address or execution claim from it.

## Links

Source destination: [q3579338/genlayer-anchor-receipt](https://github.com/q3579338/genlayer-anchor-receipt). Repository created; source contents are not yet uploaded. The initial source commit is prepared locally and publication awaits approval.

Deployed contract: Studionet chain ID `61999`, `0xf20c3D5C8Ed12AC923b20150016Ee397C6636e08`.

Real-node deployment and registration: the finalized transaction IDs above. Semantic observation transactions: not run or verified yet.

Demo/usage evidence: local tests, official static/schema validation and real deployment/registration. Full source retrieval and semantic observation remain unverified.

Never replace these status statements with invented links, transaction IDs or deployment claims.
