# Security review lenses

Apply these to the actual architecture. Historical defects are regression ideas, not assertions that every new target has them.

## Framework coverage

At extraction on November 23, 2026, official sources identify [Web Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/), [API Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/) and [LLM Top 10:2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/). Refresh the official sources for each new review. Historical PR #71 used older Web/LLM editions; do not copy its category numbers into a newer matrix.

Create one row per category for each selected edition, including categories without confirmed findings. Trace code/tests to the category; “not applicable” needs architectural evidence. Review supply chain, cryptography, logging/alerting and exceptional conditions even when no scanner flags them. Add platform-specific controls where the Top 10 lists are too broad.

## Authentication, authorization and tenant isolation

Test an actor matrix: anonymous, owner, another user, disabled user, revoked/expired session, integration key, interactive mobile token, administrator, and a limited-scope key owned by an administrator.

- Normalize identity identically for lookup and throttling. Exercise Unicode/IDNA aliases and multiple login transports. Check password timing, reset enumeration, MFA challenges/recovery/replay, temporary-password restrictions and session invalidation.
- Distinguish user role, token scope and token kind. An admin's read-only inventory key must not inherit administrator reach. Integration keys must not silently gain interactive password/export/deletion powers.
- Check direct URLs, nested IDs, writable properties, collections/search, attachments, public directories and cached results, not only list pages. Reject booleans/fractions/non-finite numbers as IDs instead of coercing them.
- Exercise admin-on-admin email/password changes, token minting, demotion and last-admin races. Audit the actual actor/key issuer without storing secrets.
- Verify CSRF on browser mutations and bearer-only API boundaries; enforce private/no-store responses where needed.
- Test shared records populated from private free text. Public photos do not automatically authorize publication of a private maker name, notes, metadata or unverified “official” URL.

## Outbound requests, upstream data and parsers

- Validate scheme, hostname, effective port, credentials and destination policy before attaching secrets. Check redirects, proxies, IPv4/IPv6, mapped/NAT64 addresses, private/link-local/metadata targets and DNS rebinding.
- Host validation followed by a separate DNS resolution at connection time leaves a gap. For hardened public fetches, pin the validated address while preserving original Host and TLS hostname verification; do not “fix” SSRF by disabling TLS verification.
- Stream with byte/deadline limits, including error bodies. Check truncation, recursive JSON, invalid encodings, control characters, enormous integers, NaN/infinity and unexpected types. Bound before buffering or decoding.
- Treat provider/retailer URLs as untrusted. A model-generated URL is not automatically safe to fetch, render as a trusted source or mark verified.
- Inspect uploaded content, extension/MIME disagreement, decompression/pixel/page limits and truncated images. Revalidate staged bytes/hash immediately before model processing.
- Isolate PDF/scanner processes with fixed commands, minimal environment, bounded CPU/memory/time and private temporary files. Apply limits in a safe child process; copied parser paths must retain the same isolation.
- Check output escaping in templates/DOM, URL sanitization and subprocess argument construction. Metadata stripping on images does not establish PDF/TXT sanitization or active-content removal.
- Bound downloads, pagination, caches, polling, token creation, uploads and expensive business flows. Account-level budgets must not reset when a user creates another token or session.

## AI, prompt injection and provider privacy

Trace each stage separately: image/text extraction, search/research, assembly, summary, document chat, cache reuse, display, export and confirmed mutations.

Use harmless synthetic adversarial material in each reachable input: photographed text, pattern PDF/text, notes, source filenames, search results, citation titles/URLs, prior chat and intermediate model JSON. Check instructions that try to change models/endpoints, invoke forbidden tools, leak a canary, overwrite known data, fabricate authority, amplify paid calls or trigger an application mutation.

- Enforce tool and endpoint capabilities in code. Private documents should not enter a public-search stage merely because a model asks. A no-tools claim must be rechecked when a later researcher gains provider-hosted search.
- Refresh user consent, grants, enabled status and model configuration before later stages, fallbacks and HTTP retries. A stale ORM object is not a fresh authorization check.
- Separate consent for extraction, external summaries and sharing. Enforce it on stored intermediate components as well as visible fields. Record unavoidable already-dispatched work honestly.
- Persist only bounded, allowlisted model fields and accounting. Unknown fields must not become instructions or hidden retained data. Do not execute generated code or trust the model for access control.
- Validate source membership and separately check whether evidence supports the claim. Keep uncertainty, source conflicts, original observations and photo-specific values; current web specifications must not overwrite label facts.
- Scope caches to owner and complete input set, notes, source revision, models, prompt/pipeline version, consent and privacy settings as relevant. Retained artifacts without a valid fingerprint should not bypass stricter hot-cache rules.
- Distinguish authoritative catalogs from user/model observations. Promotion must not bless poisoned metadata. Check deletion of orphaned private observations and partial imports.
- Account for retries, search loops, nested billing, BYOK, malformed/unknown cost and parallel overshoot. A continuation threshold is not a hard invoice cap.
- Recheck provider retention flags/routing eligibility against current official documentation. A preference sent to a provider is not independent proof of its internal handling.
- Test requirements/record confirmation separately from chat answers. Pattern counts, inventory amounts, source permissions and measured machine settings must not be silently mutated by a response.

## Workers, transactions and privacy lifecycle

- Check leases on success **and every failure path**. A superseded attempt must not fail/requeue a newer attempt, duplicate a record or erase its staged photos. Exercise stale recovery, terminal jobs and bounded attempts.
- Enqueue durable object erasure in the same transaction that removes references. A storage outage must retain a retry record. Test rollback after object writes and interruption around commit.
- Avoid holding database locks across network calls. Release safely and recheck source fingerprint/revision, permissions and state before applying results.
- Test inventory/reservation changes atomically under genuine database concurrency. Partial PATCH avoids unrelated overwrites but is not same-field optimistic concurrency.
- Review account deletion, shared exports, local caches, S3 versions and backups separately. A queue entry does not prove bytes were erased; remote deletion cannot recall a previously exported copy.

## Android transport, session and offline behavior

- Forward bearer tokens only to the exact approved HTTPS origin, including effective port. Redirected storage media can be supported without forwarding credentials. API redirects must not leak bodies or headers.
- Bind requests, results, caches and offline files to account/server/session generation. Cancel work on sign-out and reject late responses; an old 401 must not log out a newly signed-in account.
- Preserve a known HTTP authentication failure even if its error body is oversized or unreadable. Confirmed revocation must still clear the token and protected offline data.
- Separate transient network failure from confirmed invalid credentials. Do not destroy valid offline access merely because startup networking failed.
- Prune revoked/deleted source bytes immediately after fresh server state is known, before progress conflict handling or later writes. Keep unrelated pending notes/row edits.
- Inspect Keystore usage, backup exclusions, cleartext policy, FileProvider paths/export flags, external intents, bounded response/upload/image cache sizes and downsampling.
- Test failed-save draft retention, duplicate submission, malformed numbers and partial edits through actual composables and backend transactions.
- Record emulator/API versions and physical-device gaps. An offline client cannot learn a revocation until reconnection; document that limit instead of claiming instant remote erasure.

## Deployment, supply chain and maintainability

Inspect production environment defaults, TLS/cookies/HSTS/trusted hosts, reverse-proxy trust, network bindings, shared rate-limit storage, audit/redaction, alerts, retention and restore readiness. A multi-worker process needs shared budgets even on one VM.

Check dependency advisories and transitive ecosystems separately; Python scanning does not audit Android. Inspect immutable action pins, wrapper integrity, build contexts, signing secrets limited to necessary steps, trusted artifact provenance, publisher symlink/rename races and directory ownership.

Find duplicated validation, authorization, serialization, persistence and cleanup rules whose behavior has diverged. Compare web/API/admin paths before extracting a shared service. Separate useful fixes from speculative rewrites; do not roll unrelated catalog/UI work into a security patch.
