# Review checklist

Apply these checks to the actual architecture. Defects found in earlier projects are regression ideas, not assumptions about the current one. Each check should end as a test asserting the correct behavior, or as a not-applicable note with architectural evidence.

## Framework coverage

As of November 23, 2026, the official editions are [Web Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/), [API Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/) and [LLM Top 10:2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/). Re-check the official sources at the start of each review. Earlier FAIRF reviews (PR #71) used older Web/LLM editions, so don't copy their category numbers.

Write one row per category for each edition, including categories with no findings. Link code and tests to the category; "not applicable" needs architectural evidence. Cover supply chain, cryptography, logging/alerting and error handling even when no scanner reports anything. Add platform-specific controls where the Top 10 lists are too broad.

## Authentication, authorization and tenant isolation

Build a role matrix and test each protected operation against it: anonymous, owner, another user, disabled user, revoked/expired session, integration key, interactive mobile token, administrator, and a limited-scope key issued by an administrator.

- Normalize identity the same way for lookup and rate limiting. Include Unicode/IDNA variants and every login transport. Check password-comparison timing, reset responses that reveal whether an account exists, MFA challenge/recovery/one-time-code reuse, temporary-password restrictions and session invalidation.
- Keep user role, token scope and token type distinct. An admin's read-only inventory key must not carry administrator permissions. Integration keys must not gain interactive password, export or deletion abilities.
- For login, password change, MFA, export, deletion and recovery links, check whether a user or token loaded earlier in the request can be stale after a concurrent reset, disable or revocation. Lock and refresh the account before verifying credentials, and keep the authenticated session generation separate from refreshed ORM state. A browser session created after a reset must never inherit the reset account's new generation after authenticating with the old password.
- Check object-level authorization on direct URLs, nested IDs, writable properties, collections/search, attachments, public directories and cached results, not only list pages. Reject booleans, fractions and non-finite numbers as IDs instead of coercing them.
- Check admin-to-admin email/password changes, token issuance, demotion and the last-admin race. Audit logs should record the real actor and key issuer without storing secrets.
- Confirm CSRF protection on browser state changes and bearer-only API boundaries; send private/no-store cache headers where needed.
- Check shared records built from private free text. Public photos don't automatically make a private maker name, notes, metadata or an unverified "official" URL publishable.

## Outbound requests, upstream data and parsers

- Server-side requests (OWASP API7:2023): validate scheme, hostname, effective port, embedded credentials and destination allowlist before attaching any secret. Re-validate after redirects and through proxies; cover IPv4/IPv6, IPv4-mapped and NAT64 forms, and private, link-local and cloud-instance-metadata address ranges.
- If the hostname is validated and then resolved again at connect time, the second resolution can return a different address. For public fetches, connect to the validated address while keeping the original Host header and TLS hostname verification. Never resolve this by disabling TLS verification.
- Stream responses with byte and time limits, including error bodies. Handle truncation, deeply nested JSON, invalid encodings, control characters, very large integers, NaN/infinity and unexpected types. Enforce limits before buffering or decoding.
- Treat provider and retailer URLs as untrusted. A model-generated URL is not automatically safe to fetch, display as a trusted source or mark verified.
- Validate uploads: extension/MIME mismatch, decompression/pixel/page limits and truncated images. Re-check staged bytes or hash immediately before model processing.
- Run PDF/scanner work in a separate process with fixed arguments, minimal environment, CPU/memory/time limits and private temp files. Any copied parser code path needs the same isolation.
- Check output encoding in templates and DOM, URL sanitization and subprocess argument construction. Stripping image metadata does not sanitize PDF/TXT content or remove active content.
- Bound downloads, pagination, caches, polling, token creation, uploads and expensive business flows. Account-level budgets must not reset when the user opens a new token or session.

## AI features: untrusted content and provider privacy

Review each stage separately: image/text extraction, search/research, assembly, summary, document chat, cache reuse, display, export and confirmed edits.

Test fixtures: put plain-text embedded instructions (OWASP LLM: prompt injection) into every input the pipeline reads — photographed text, pattern PDFs/text, notes, filenames, search results, citation titles/URLs, prior chat turns and intermediate model JSON. The instructions ask the model to switch model or endpoint, call a tool it shouldn't have, echo a marker string from a protected field, overwrite known data, claim false authority, trigger extra paid calls or change application state. Each test asserts that none of those effects occur.

- Enforce tool and endpoint permissions in code. Private documents should not reach a public-search stage because a model asked for it. If a later stage gains provider-hosted search, re-check any earlier "no tools" assumption.
- Re-read consent, grants, enabled status and model configuration before each later stage, fallback and HTTP retry. A cached ORM object is not a fresh authorization check.
- Keep consent separate for extraction, external summaries and sharing. Enforce it on stored intermediate data as well as visible fields. Record honestly any work already sent before consent was withdrawn.
- Persist only bounded, allowlisted model fields and cost data. Unknown fields must not become instructions or hidden stored data. Never execute generated code or let the model decide access control.
- Check that cited sources belong to the retrieved set and that they actually support the claim. Keep uncertainty, source conflicts, original observations and photo-specific values; current web specs must not overwrite label facts.
- Key caches to owner and the complete input set: notes, source revision, models, prompt/pipeline version, consent and privacy settings. Retained artifacts without a valid fingerprint must follow the same rules as the hot cache.
- Keep authoritative catalog data separate from user or model observations (OWASP LLM: data and model integrity). Promotion into the shared catalog must validate the data. Clean up orphaned private observations and partial imports.
- Account for retries, search loops, nested billing, BYOK, malformed or unknown cost and parallel overshoot. A continuation threshold is not a hard spending cap.
- Re-check provider retention flags and routing eligibility against current official docs. A preference sent to a provider doesn't prove how the provider handles data.
- Test record changes separately from chat answers. Pattern counts, inventory amounts, source permissions and measured machine settings must not change because of a chat response without user confirmation.

## Workers, transactions and data lifecycle

- Check job leases on success **and every failure path**. A superseded attempt must not fail or requeue a newer attempt, duplicate a record or delete its staged photos. Cover stale recovery, terminal jobs and bounded attempts.
- Enqueue durable object deletion in the same transaction that removes references. A storage outage must leave a retry record. Test rollback after object writes and interruption around commit.
- Don't hold database locks across network calls. Release, then re-check source fingerprint/revision, permissions and state before applying results.
- Test inventory/reservation changes for atomicity under real database concurrency. Partial PATCH avoids clobbering unrelated fields but is not same-field optimistic concurrency.
- Review account deletion, shared exports, local caches, S3 versions and backups separately. A queue entry doesn't prove bytes were erased; remote deletion can't recall an already-exported copy.

## Android transport, session and offline behavior

- Send bearer tokens only to the exact approved HTTPS origin, including effective port. Redirected media storage can be supported without forwarding credentials. API redirects must not forward bodies or auth headers.
- Bind requests, results, caches and offline files to account/server/session generation. Cancel work on sign-out and discard late responses; a stale 401 must not sign out a newly signed-in account.
- Preserve a known HTTP auth failure even when its error body is oversized or unreadable. Confirmed revocation must still clear the token and protected offline data.
- Distinguish transient network failure from confirmed invalid credentials. Don't wipe valid offline access because startup networking failed.
- Remove revoked/deleted source files as soon as fresh server state is known, before progress-conflict handling or later writes. Keep unrelated pending notes and row edits.
- Check Keystore use, backup exclusions, cleartext policy, FileProvider paths and export flags, external intents, response/upload/image-cache size limits and downsampling.
- Test draft retention after failed save, duplicate submission, malformed numbers and partial edits through the actual composables and backend transactions.
- Record emulator/API versions and physical-device gaps. An offline client can't learn about revocation until it reconnects; document that limit rather than claiming instant remote erasure.

## Deployment, supply chain and maintainability

Check production environment defaults, TLS/cookies/HSTS/trusted hosts, reverse-proxy trust, network bindings, shared rate-limit storage, audit/redaction, alerts, retention and restore readiness. Multi-worker processes need shared budgets even on one VM.

When a fix changes a deployment dependency, verify the migration path for existing installations as well as fresh installs. For a move from in-memory to shared rate limits, test the quota across two processes, make startup fail closed if shared storage is required but absent, and document the order of installing the backend client, starting the private store, changing configuration and deploying. A local passing test does not prove the old server can safely start the new release.

Check dependency advisories per ecosystem; Python scanning doesn't cover Android. Check pinned action versions, Gradle wrapper integrity, build contexts, signing secrets scoped to the steps that need them, artifact provenance, symlink/rename races in publishing and directory ownership.

Find duplicated validation, authorization, serialization, persistence and cleanup logic that has diverged. Compare web, API and admin paths before extracting a shared service. Keep useful fixes separate from speculative rewrites; don't fold unrelated catalog/UI work into a security patch.
