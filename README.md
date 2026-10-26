# AnchorReceipt

A standalone GenLayer Intelligent Contract for a narrow question: **does one fixed public source currently provide explicit evidence for or against this exact claim?**

AnchorReceipt turns that check into a reusable receipt with an immutable input hash, byte-level source hash, exact source excerpts, an append-only attempt journal, caller ownership and idempotent requests. It holds no funds and has no wager, rewards, settlement or prediction-market logic.

**Status: Studionet prototype; chain observations recorded 2026-10-22.** Deployment, registration and two real `check` transactions are finalized with `MAJORITY_AGREE` on GenLayer Studionet (chain ID `61999`). The deployed source matches this contract source. Two observations of the same explicitly declared, developer-controlled synthetic fixture sealed `SUPPORTED` and `CONTRADICTED` results for different date claims. These demonstrate those specific source/hash/quote paths; they do not establish `UNKNOWN` behavior, real prompt-injection robustness, heterogeneous-model availability or general accuracy. This repository and its minimized evidence were published, and the Portal contribution was submitted, on 2026-10-22. Acceptance and awarded points require separate Portal confirmation; this README does not claim either. No fee or performance result is claimed. Local unit tests use a deliberately small fake of the GenLayer API and remain distinct from actual chain execution.

### Observed deployment and registration

| Item | Recorded result |
| --- | --- |
| Environment | Studionet, chain ID `61999` |
| Contract | `0xf20c3D5C8Ed12AC923b20150016Ee397C6636e08` |
| Deployment transaction | `0x657cfe993dd21c85f29506e2aa0de22cac8156732e8c976b626f62b6cda2f9d9` — `FINALIZED`, `MAJORITY_AGREE` |
| Registration transaction | `0x3aeb55ccf3ab7b3d097cb8a8aa3e31f76d989d7ed90a1db691d222d0963a66c4` — `FINALIZED`, `MAJORITY_AGREE`; leader execution `SUCCESS` |
| Supporting observation transaction | `0xc638c8d69c5d9921adcaf1ae999c0b07e243fe5926438591f5bcb80355b7a70e` — `FINALIZED`, `MAJORITY_AGREE`; leader execution `SUCCESS` |
| Contradicting observation transaction | `0xc8e8ff726fdfdd1cfc924abf50f060355e57594afe7af782ffdbedf80cf87682` — `FINALIZED`, `MAJORITY_AGREE`; leader execution `SUCCESS` |
| Source match | Confirmed against deployed code; contract source SHA-256 `d53bf94155c164844630fca8ce3a9ddc6ffdb440db877ffdf3b4bc1b70f5a620` |
| Supporting state | Receipt `1`, attempt `1`, `SEALED`, `SUPPORTED`: claim states 30 October 2026 at 18:00 UTC |
| Contradicting state | Receipt `2`, attempt `1`, `SEALED`, `CONTRADICTED`: claim states 1 November 2026 at 18:00 UTC, while source explicitly states 30 October |
| Shared observed source | HTTP `200`, body `450` bytes; the same fixture and expected body hash are used for both cases |
| Bound fixture body SHA-256 | `9b7ef32ce39692d42629c0f5f45f24a11b0f1c5a8efe63088300f85b2f256e8d` |

Both cases cite the same verbatim quote: `Applications for the example workshop close on 30 October 2026 at 18:00 UTC.`, selected from evidence unit `3`, character offsets `[211:287]` (start inclusive, end exclusive). The source is a synthetic example workshop notice, not an official live event or an independently authenticated publisher. Its public URL and each case's distinct claim/input/observation hashes are recorded in the corresponding minimized state summaries.

#### Reproducing the historical source bytes

Use the [commit-pinned 30 October fixture](https://raw.githubusercontent.com/q3579338/genlayer-notice-delta/f2e77496d31cd2e92a60906e6f02d9256700f14b/fixtures/announcement.md) to inspect the source body used by both observations. It is 450 bytes with raw-body SHA-256 `9b7ef32ce39692d42629c0f5f45f24a11b0f1c5a8efe63088300f85b2f256e8d`, matching both receipts' expected and observed body hashes. The sentence above occurs at the recorded character offsets.

The mutable `main` URL recorded in the historical contract inputs was subsequently changed to 6 November for NoticeDelta's documented comparison test. Its current contents therefore differ from AnchorReceipt's sealed observation. The commit-pinned URL is a retained copy for independent byte/hash inspection; it does not replace the original registered URL or claim a new chain transaction. The original receipt inputs and transaction evidence remain unchanged. These public bytes and hashes were rechecked on 2026-10-26.

These facts are recorded in the deployment, registration and two check receipts plus the resulting states. Validator cancellations after quorum appear in the registration/check execution logs; the recorded transaction statuses are nevertheless finalized. Do not report every validator as having completed or infer model/provider diversity from the quorum results. Published field-minimized summaries are under `evidence/public/` and listed in `RELEASE_MANIFEST.md`. Both verdict claims above are based on actual state readback, not transaction success alone.

## Why this needs GenLayer

The primitive combines a semantic task with programmatic constraints. A model decides whether a source explicitly entails or contradicts a fact; ordinary code cannot generally make that language decision. Each validator independently retrieves the registered source and independently extracts its own decision. It then compares the normalized decision, evidence selections, response hash and input binding with the leader's result. A valid enum alone is never sufficient.

GenLayer is the core execution environment. The contract is not a frontend that asks an off-chain server for a verdict and stores it.

## Scope of a receipt

- `SUPPORTED`: the retrieved source explicitly supports the whole claim.
- `CONTRADICTED`: the source explicitly states an incompatible fact about the same subject, scope and time.
- `UNKNOWN`: omission, ambiguity, mixed claims, unsupported inferences or insufficient evidence. An unavailable source is also `UNKNOWN`, with a separate failure code.

These verdicts describe the source, not the truth of its contents. A malicious publisher can publish a false statement; consensus about that statement does not make it true. There is no proof of historical absence, universal truth, publisher identity or source independence.

## Processing and trust boundaries

1. At deployment choose 1–16 exact public HTTPS hostnames. The list has no update method. It restricts the initial request hostname and should contain controlled, nonredirecting public sources. Lexical validation does not establish DNS safety or validate the identity of a publisher. The pinned SDK exposes no redirect policy or final-response URL; any redirect/egress protection must be verified in the actual GenVM host before deployment.
2. An owner registers an 8–64 character request key, a fixed HTTPS URL, a 12–600 character claim and an optional expected SHA-256 of the response body. Ports, credentials, fragments, IP literals, local suffixes, invisible URL characters and encoded CR/LF/NUL are rejected. A source URL and a claim can never be edited after registration.
3. Deterministic code binds the normalized URL, claim, owner, optional body hash and schema version into `input_hash`. Reusing a request key returns the same receipt; reusing it for different inputs fails. Request keys belong to the caller's namespace.
4. `check` executes a custom `gl.vm.run_nondet_unsafe` leader/validator pair. Each node independently fetches the URL. HTTP 200, a 12–24,000 byte body, UTF-8 and an allowed content type are required. Allowed types are `text/plain`, `text/markdown` and `application/json`. HTML, PDF, rendered JavaScript pages, binary controls and oversized sources are rejected rather than silently truncated.
5. Exact source text is split into at most 128 deterministic units, each at most 320 characters. Units retain their exact character offsets. The model can return only a verdict and one or two unit IDs; it cannot supply a free-form quote or narrative that becomes evidence. `UNKNOWN` must have no IDs. Duplicate, unsorted, nonexistent or boolean IDs and extra keys fail.
6. Local code creates the quote records from the original units. The validator repeats the complete fetch/extraction/grounding process without trusting the leader's output. It accepts only exact canonical equality. It does not approve the leader merely because its JSON has the right shape.
7. After consensus, deterministic code checks the schema, input hash, expected source hash, returned body hash, body size, every evidence unit and every exact source offset again. It drops the full source text before saving the compact observation. The accepted text crosses the nondeterministic boundary but is not kept in contract state.
8. An observation hash binds the persisted result. Definitive observations are sealed. Failed/unknown attempts can be retried with a new attempt key, while the earlier entries remain available. A consensus failure performs no storage writes.

The design intentionally favors conservative rejection. Models may select different equally valid units or sources may change between nodes. Exact comparison then fails consensus instead of accepting a loosely similar evidence claim. Real-node testing is needed to measure whether this tradeoff yields usable completion rates.

## API

| Method | Behavior |
| --- | --- |
| `__init__(allowed_hosts)` | Freeze the exact initial-host allowlist; no network call. |
| `register(request_key, source_url, claim, expected_sha256="")` | Create or idempotently recover an immutable receipt; return its ID. |
| `check(receipt_id, attempt_key)` | Owner-only source observation. The same attempt key returns the original result without refetching, even after later attempts or sealing. |
| `cancel(receipt_id)` | Owner-only cancellation of a pending/retryable/unknown receipt. Sealed observations cannot be cancelled or rewritten. |
| `get_receipt(receipt_id)` | Return immutable inputs, latest observation, status, attempt count and scope. |
| `list_receipts(before=0, limit=20)` | Descending pages, maximum 50. Pass the last returned ID as `before`. |
| `list_attempts(receipt_id, after=0, limit=10)` | Ascending journal pages, maximum 16. Pass the last attempt number as `after`. |
| `get_config()` | Return the version, fixed host list and hard limits. |

`deployment_owner` is informational. It has no administrative power to edit another owner's receipts or change the host list. Ownership uses `sender_address`, so a contract wallet can own its own receipts. There is no requirement that sender equal transaction origin.

The runtime rejects value on nonpayable methods. There are no payable methods, transfers, token calls or user deposits. Ordinary network transaction fees still apply.

## State and recovery

```text
register → PENDING
check + agreed fetch/format/model error → RETRYABLE
check + agreed UNKNOWN → UNKNOWN
check + agreed SUPPORTED/CONTRADICTED → SEALED
owner cancel before sealing → CANCELLED
consensus disagreement / VM failure → previous state, no new journal entry
```

`PENDING`, `RETRYABLE` and `UNKNOWN` can be checked again. A receipt permits at most 16 agreed attempts. After that, create a new receipt with a new registration key. `SEALED` and `CANCELLED` reject new checks but replaying a previously completed attempt key still returns its original receipt entry.

There is no persisted `CHECKING` state, external callback or time-based lock. A transaction that fails before accepted execution cannot strand the receipt in an intermediate state. This prototype has no dedicated stored timestamp; consumers must obtain observation transaction time and finality from real chain receipts. An optimistic result should not be presented as final.

## Local usage example

The following is illustrative API usage; its placeholder URL is **not** the registered live fixture and is not an executed transaction:

```python
# Constructor hosts should be selected and reviewed for the intended deployment.
allowed_hosts = ["raw.githubusercontent.com"]

# Use a real public HTTPS raw text URL in an actual deployment.
receipt_id = register(
    "release_check_0001",
    "https://raw.githubusercontent.com/OWNER/REPO/COMMIT/announcement.txt",
    "The public beta opens on 15 November 2026.",
    "",  # Or the independently computed lowercase SHA-256 of the exact response bytes.
)

check(receipt_id, "observation_0001")
get_receipt(receipt_id)
list_attempts(receipt_id, 0, 10)
```

The URL contains placeholders and is not a demonstration source. An immutable Git commit URL and an independently obtained body hash are appropriate when a consumer wants to require specific bytes. Without `expected_sha256`, the receipt binds whatever bytes the nodes agreed they retrieved at the observation, even if those bytes differ from an earlier publication.

## Verification performed locally

Requires Python 3.10+ for standard-library local tests; no packages or credentials are needed:

```powershell
python -B -m unittest discover -s tests -v
```

The test double performs two separate fetch/extraction calls to exercise the validator path and injects changed sources, differing model outputs, forged leader data, malformed JSON, invented evidence and forged hashes. It also checks input and attempt idempotency, ownership, cancellation, pagination, source/body bounds, Unicode offsets, journal preservation and recovery. It does **not** emulate GenVM storage, serialization, fees, network consensus or LLM intelligence. The prompt-injection fixture verifies only prompt/data handling and output restrictions; its model answer is mocked.

The local run recorded 22 passing tests with no failures or errors. Run output and hashes are generated in `evidence/local-test-report.json` and `evidence/local-tests.txt`; the prepared release includes only the specifically listed public evidence summaries, not the complete local evidence directory. An official `genvm-linter` 0.11.0 check using the GenVM v0.2.16 bundle and the exact pinned dependency also passed schema and semantic validation (7 public methods: 4 views, 3 writes; 1 constructor parameter). `NODE_VALIDATION.md` separates the finalized synthetic `SUPPORTED`/`CONTRADICTED` observations from untested real scenarios. Do not relabel local test counts or static checks as testnet semantic results.

## Limits and honest failure modes

- The host may follow redirects; the pinned SDK cannot inspect their final URL. Initial-host checks do not prove final-source identity or prevent DNS rebinding. Host egress security and nonredirecting source behavior require independent verification.
- HTTP response bodies may be mutable, cached, personalized or unavailable. Exact hashes improve binding and detect disagreement but do not prove the upstream was truthful or that all nodes received an independent source.
- Prompt injection and correlated model errors remain possible. Source and claim data are explicitly marked untrusted, outputs are severely limited, evidence is grounded and validators repeat the task; none is a mathematical proof of semantic entailment.
- Quoted units may include irrelevant neighboring text or split a needed statement. One or two whole units are the only permitted evidence. Long, dynamic or HTML sources may need a different contract/version; this implementation never silently truncates them.
- An honest disagreement on quote IDs, source bytes or verdict prevents completion. The exact comparison policy is intentional and still needs real heterogeneous-provider evaluation.
- Failed attempts have generic machine codes and do not store raw provider errors. This limits information leakage but makes diagnosis depend on node logs.
- Full source text is transient and not archived by this contract. Anyone verifying a persisted quote later must retain the original public body independently and compare SHA-256; a current refetch may differ.
- There is no account-wide submission quota. Users pay network costs; each receipt bounds its body size, evidence output, pages and agreed attempts.
- SHA-256 uses Python `hashlib`. Actual deployment, registration and the two finalized 450-byte synthetic `SUPPORTED`/`CONTRADICTED` checks exercised basic imports, storage, check closure, source fetch, model extraction and post-consensus hash/quote paths on the deployed runner. Maximum-size payloads, disagreement recovery, `UNKNOWN`, real injection attacks and heterogeneous-model completion rates remain unvalidated.

## Official reference basis

Checked 2026-10-22, using official documentation and SDK reference. The contract pins the dependency shown in the current first-contract guide and official boilerplate:

`py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`

- [Your First Intelligent Contract](https://docs.genlayer.com/developers/intelligent-contracts/first-intelligent-contract) — dependency directive and nondeterministic-block boundary.
- [Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle) — independent source verification and custom leader/validator pattern.
- [GenVM SDK 0.2.9 reference](https://sdk.genlayer.com/v0.2.9/api/genlayer.html) — `gl.vm.Return`, `run_nondet_unsafe`, `TreeMap`, `exec_prompt` and `web.Response` signatures.
- [Official GenVM source](https://github.com/genlayerlabs/genvm) — response API cross-check performed against stable 0.2.x SDK source. The actual response field is `status`; some high-level documentation examples say `status_code`, which this contract deliberately does not use.

SDK release candidates and future network runners may expose different module layouts. The pinned source is not a claim that this prototype has been executed on the current network.

## Contribution boundaries

This is a separate library-style contract contribution, not a milestone or repackaging of Event Duels. It inherits no Event Duels prediction, staking, escrow, payout, GitHub release game, frontend or deployment evidence. The submission draft in `CONTRIBUTION_DRAFT.md` distinguishes the two finalized synthetic date-claim observations from broader untested scenarios. Before submission, perform the remaining real-node checks and publish only the approved files in `RELEASE_MANIFEST.md`, or retain each evidence gap as an explicit limitation.
