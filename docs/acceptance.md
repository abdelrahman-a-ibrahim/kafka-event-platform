# Acceptance and assessment

Status: not evaluated. These are targets, never achieved claims.

## Required project outcomes
- [ ] A retained input set can be replayed with documented duplicate behavior.
- [ ] Unauthorized producer/consumer operations fail in explicit ACL tests.
- [ ] Broker-loss results include exact topology and durability settings.
- [ ] Ordering guarantees are stated per partition; no unqualified exactly-once claim.

## Shared quality criteria
- [ ] A new reader can reproduce setup from documented inputs.
- [ ] Behavior tests exercise actual implementations, including invalid inputs and failures.
- [ ] Relevant concurrency and replay cases are exercised against durable state.
- [ ] The implementation’s guarantees and limitations match its evidence.
- [ ] Resources, secrets, permissions and cleanup are documented.
- [ ] Implementation decisions include alternatives and consequences.
- [ ] An incident/recovery report links raw observations to its conclusions.
- [ ] A short teaching walkthrough explains one non-obvious failure.

## Self-review rubric
Score each dimension 0–3: 0 missing; 1 described; 2 implemented with a basic demonstration; 3 independently reproducible and tested under relevant failure.

| Dimension | Score | Evidence |
|---|---|---|
| Correctness and invariants | Pending | |
| Architecture and tradeoffs | Pending | |
| Failure handling and recovery | Pending | |
| Security and trust boundaries | Pending | |
| Observability and operations | Pending | |
| Reproducibility and cleanup | Pending | |
| Technical explanation | Pending | |

This rubric is a learning aid, not a certification or proof of production readiness. Do not average away a failed core correctness or authorization requirement.
