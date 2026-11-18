# Kafka Event Platform

A Kafka-based messaging platform with versioned event contracts, access control and operational visibility.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

An event backbone for applications that publish bookings, attendance updates and operational events. The project defines topic ownership, schema evolution, partitioning, consumer coordination and recovery procedures around explicit delivery guarantees.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- A versioned topic catalog with ownership, retention and schema compatibility rules.
- Reproducible Kafka KRaft deployment configurations.
- Producer and consumer interfaces with explicit partition and offset semantics.
- Scoped identities and ACLs for multi-broker deployments.
- Consumer-lag visibility, broker health dashboards and recovery procedures.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Synthetic producer -> Kafka topics -> independent consumer groups
                         |
                         +-> metrics -> dashboard / alerts
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Kafka · KRaft · Schemas · Consumer groups · ACLs · Monitoring.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/kafka-event-platform.git
cd kafka-event-platform
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/kafka_event_platform/interfaces.py`](src/kafka_event_platform/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- A retained input set can be replayed with documented duplicate behavior.
- Unauthorized producer/consumer operations fail in explicit ACL tests.
- Broker-loss results include exact topology and durability settings.
- Ordering guarantees are stated per partition; no unqualified exactly-once claim.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/kafka_event_platform/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://kafka.apache.org/documentation/
