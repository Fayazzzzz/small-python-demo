"""Builds the greeting text."""

from service.validators import is_valid_name


def greet(name: str) -> str:
    """Return "Hello, <name>!" with the name trimmed, or raise ValueError for an invalid name."""
    if not is_valid_name(name):
        raise ValueError("name must be letters and spaces, up to 50 characters")
    return f"Hello, {name.strip()}!"
