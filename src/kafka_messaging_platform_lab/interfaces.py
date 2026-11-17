"""Proposed application boundary for Kafka Messaging Platform Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class MessagingPlatform:
    def publish(self, event: dict, partition_key: str) -> dict:
        """Publish a versioned event with an explicit acknowledgement policy."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def consume(self, group_id: str, limit: int) -> list:
        """Consume with documented offset and failure behavior."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

