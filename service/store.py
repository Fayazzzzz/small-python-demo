"""An in-memory record of the names greeted so far."""


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
