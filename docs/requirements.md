# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
An event backbone for applications that publish bookings, attendance updates and operational events. The project defines topic ownership, schema evolution, partitioning, consumer coordination and recovery procedures around explicit delivery guarantees.

## Target capabilities
- Document a topic catalog, ownership, retention, partition keys, compatibility policy and delivery assumptions.
- Build a reproducible local KRaft environment with pinned image versions. Add topic creation as an explicit operation and a cleanup command.
- Implement producers and consumers. Explore keys, partitions, ordering, offset commits, poison messages and consumer rebalances.
- Run a separate multi-broker resilience development environment. Specify replication factor, minimum in-sync replicas and producer acknowledgements; add scoped identities and ACLs.
- Instrument lag, produce latency, rebalances and broker health. Run load/recovery experiments and publish a capacity and operations report.

## Acceptance criteria
- A retained input set can be replayed with documented duplicate behavior.
- Unauthorized producer/consumer operations fail in explicit ACL tests.
- Broker-loss results include exact topology and durability settings.
- Ordering guarantees are stated per partition; no unqualified exactly-once claim.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
