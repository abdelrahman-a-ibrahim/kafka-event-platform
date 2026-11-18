# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Document a topic catalog, ownership, retention, partition keys, compatibility policy and delivery assumptions.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Build a reproducible local KRaft environment with pinned image versions. Add topic creation as an explicit operation and a cleanup command.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Implement producers and consumers. Explore keys, partitions, ordering, offset commits, poison messages and consumer rebalances.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Run a separate multi-broker resilience development environment. Specify replication factor, minimum in-sync replicas and producer acknowledgements; add scoped identities and ACLs.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Instrument lag, produce latency, rebalances and broker health. Run load/recovery experiments and publish a capacity and operations report.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Kafka transactions inside a Kafka-to-Kafka workflow
- Consumer-lag autoscaling experiment
- Mirror or disaster-recovery topology comparison
- Tiered retention cost and recovery tradeoffs

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
