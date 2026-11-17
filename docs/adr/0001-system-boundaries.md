# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Build a Kafka platform for WorkshopHub booking and attendance events. Local single-node development is the first milestone; a separate multi-broker experiment explores resilience without pretending a laptop is production.

## Decision questions
- Partition-key selection and hot-key mitigation
- Schema registry versus repository contracts
- Offset commit relative to downstream side effects

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
