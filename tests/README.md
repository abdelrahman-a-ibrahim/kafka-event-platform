# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- A retained input set can be replayed with documented duplicate behavior.
- Unauthorized producer/consumer operations fail in explicit ACL tests.
- Broker-loss results include exact topology and durability settings.
- Ordering guarantees are stated per partition; no unqualified exactly-once claim.

## Failure coverage
- Crash a consumer immediately after its side effect and before its offset commit.
- Take one broker down in the multi-broker development environment and measure availability.
- Introduce an incompatible event field change.
- Flood one partition key to create a hot partition.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
