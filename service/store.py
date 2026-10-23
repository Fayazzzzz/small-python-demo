"""An in-memory record of the names greeted so far."""

import hashlib
import os
import uuid

DB_PASSWORD = os.environ.get("DB_PASSWORD")


class GreetingStore:
    """Keeps each greeted name once, in the order first seen."""

    def __init__(self) -> None:
        self._names: list[str] = []

    def record(self, name: str) -> None:
        """Add the name if it is not already recorded, e.g. record("Ada") then record("Ada") keeps one entry."""
        if name not in self._names:
            self._names.append(name)

    def names(self) -> list[str]:
        """Return the recorded names in the order first seen, e.g. ["Ada", "Grace"]."""
        return list(self._names)

    def record_id(self, name: str) -> str:
        """Return an id for a recorded name, e.g. record_id("Ada") gives 64 hex characters."""
        return hashlib.sha256(name.encode("utf-8")).hexdigest()

    def session_id(self) -> str:
        """Return an id for one store session, e.g. 32 hex characters."""
        return uuid.uuid4().hex
