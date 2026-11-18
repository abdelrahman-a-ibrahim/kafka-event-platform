# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
An event backbone for applications that publish bookings, attendance updates and operational events. The project defines topic ownership, schema evolution, partitioning, consumer coordination and recovery procedures around explicit delivery guarantees.

## Questions
- Partition-key selection and hot-key mitigation
- Schema registry versus repository contracts
- Offset commit relative to downstream side effects

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
