"""Checks on names sent to the service."""

MAX_NAME_LENGTH = 50


def is_valid_name(name: str) -> bool:
    """Return True for a non-empty name of letters and spaces, up to MAX_NAME_LENGTH characters."""
    stripped = name.strip()
    return 0 < len(stripped) <= MAX_NAME_LENGTH and all(ch.isalpha() or ch == " " for ch in stripped)
