# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
An event backbone for applications that publish bookings, attendance updates and operational events. The project defines topic ownership, schema evolution, partitioning, consumer coordination and recovery procedures around explicit delivery guarantees.

## Component view
```text
Synthetic producer -> Kafka topics -> independent consumer groups
                         |
                         +-> metrics -> dashboard / alerts
```

## Design decisions
- Partition-key selection and hot-key mitigation
- Schema registry versus repository contracts
- Offset commit relative to downstream side effects

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/kafka_event_platform/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
