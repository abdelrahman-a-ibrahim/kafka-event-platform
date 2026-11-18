# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Crash a consumer immediately after its side effect and before its offset commit.
- Take one broker down in the multi-broker development environment and measure availability.
- Introduce an incompatible event field change.
- Flood one partition key to create a hot partition.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- A retained input set can be replayed with documented duplicate behavior.
- Unauthorized producer/consumer operations fail in explicit ACL tests.
- Broker-loss results include exact topology and durability settings.
- Ordering guarantees are stated per partition; no unqualified exactly-once claim.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
